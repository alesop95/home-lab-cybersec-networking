#!/usr/bin/env python3
"""Calcola spazio di picco e tempi ipotetici da uno scenario JSON esplicito.

Legge soltanto il file indicato. Non esamina dati, dischi o rete, non esegue
backup e non certifica un ripristino. GB e GiB sono unità distinte.
"""

from __future__ import annotations

import argparse
from fractions import Fraction
import json
from pathlib import Path
import re
import sys


UNITS = {
    "B": 1,
    "kB": 10**3,
    "MB": 10**6,
    "GB": 10**9,
    "TB": 10**12,
    "KiB": 2**10,
    "MiB": 2**20,
    "GiB": 2**30,
    "TiB": 2**40,
}
SIZE = re.compile(r"([0-9]+(?:\.[0-9]+)?)\s+(B|kB|MB|GB|TB|KiB|MiB|GiB|TiB)")
DECIMAL = re.compile(r"[0-9]+(?:\.[0-9]+)?")


class ScenarioError(ValueError):
    """Scenario incompleto, ambiguo o fuori dal modello dichiarato."""


def fields(value, required, name, optional=()):
    if not isinstance(value, dict):
        raise ScenarioError(f"{name}: atteso oggetto JSON")
    missing = set(required) - value.keys()
    unknown = value.keys() - set(required) - set(optional)
    if missing or unknown:
        raise ScenarioError(
            f"{name}: campi mancanti {sorted(missing)}, sconosciuti {sorted(unknown)}"
        )
    return value


def sequence(value, name):
    if not isinstance(value, list):
        raise ScenarioError(f"{name}: attesa lista")
    return value


def count(value, name, minimum=0):
    if type(value) is not int or value < minimum:
        raise ScenarioError(f"{name}: atteso intero >= {minimum}, booleani esclusi")
    return value


def size_bytes(value, name="size", positive=False):
    match = SIZE.fullmatch(value) if isinstance(value, str) else None
    if not match:
        raise ScenarioError(f"{name}: specificare una dimensione, per esempio '20 GB' o '20 GiB'")
    result = Fraction(match[1]) * UNITS[match[2]]
    if result.denominator != 1 or result < 0 or (positive and result <= 0):
        raise ScenarioError(f"{name}: atteso numero intero di byte {'positivo' if positive else 'non negativo'}")
    return int(result)


def ratio(value, name):
    if not isinstance(value, str) or not DECIMAL.fullmatch(value):
        raise ScenarioError(f"{name}: attesa frazione decimale come stringa, per esempio '0.8'")
    result = Fraction(value)
    if not 0 < result <= 1:
        raise ScenarioError(f"{name}: la frazione deve essere > 0 e <= 1")
    return result


def ceil_fraction(value):
    return -(-value.numerator // value.denominator)


def dimensiona(scenario):
    fields(scenario, {
        "schema_version", "input_status", "capacity", "fixed_allocations",
        "snapshot_hold", "workspace", "full_archives", "incremental_repositories",
        "run_time", "uncertainties",
    }, "scenario")
    if type(scenario["schema_version"]) is not int or scenario["schema_version"] != 1:
        raise ScenarioError("schema_version: è supportata soltanto la versione 1")
    if scenario["input_status"] not in ("illustrative", "mixed", "measured"):
        raise ScenarioError("input_status: usare illustrative, mixed o measured")
    uncertainties = sequence(scenario["uncertainties"], "uncertainties")
    if any(not isinstance(item, str) or not item.strip() for item in uncertainties):
        raise ScenarioError("uncertainties: usare stringhe non vuote")

    capacity = fields(scenario["capacity"], {
        "layout", "devices", "filesystem_reserve", "max_fraction", "planning_limit",
    }, "capacity")
    if capacity["layout"] != "mirror":
        raise ScenarioError("capacity.layout: questo modello supporta soltanto uno specchio")
    devices = sequence(capacity["devices"], "capacity.devices")
    if len(devices) < 2:
        raise ScenarioError("capacity.devices: uno specchio richiede almeno due dispositivi")
    nominal = min(size_bytes(x, "capacity.devices", positive=True) for x in devices)
    fs_reserve = size_bytes(capacity["filesystem_reserve"], "capacity.filesystem_reserve")
    if fs_reserve >= nominal:
        raise ScenarioError("capacity.filesystem_reserve: esaurisce la capacità dello specchio")
    fraction = ratio(capacity["max_fraction"], "capacity.max_fraction")
    fraction_limit = ((nominal - fs_reserve) * fraction).__floor__()
    explicit_limit = size_bytes(capacity["planning_limit"], "capacity.planning_limit", positive=True)
    limit = min(fraction_limit, explicit_limit)

    labels = set()

    def label(item, location):
        value = item["label"]
        if not isinstance(value, str) or not value.strip() or value in labels:
            raise ScenarioError(f"{location}.label: nome non vuoto e distinto dagli altri richiesto")
        labels.add(value)
        return value

    fixed = 0
    for i, item in enumerate(sequence(scenario["fixed_allocations"], "fixed_allocations")):
        loc = f"fixed_allocations[{i}]"
        fields(item, {"label", "size"}, loc)
        label(item, loc)
        fixed += size_bytes(item["size"], loc + ".size")

    retained_full = 0
    full_sizes = []
    full_details = []
    for i, item in enumerate(sequence(scenario["full_archives"], "full_archives")):
        loc = f"full_archives[{i}]"
        fields(item, {"label", "size", "keep", "protected"}, loc)
        name = label(item, loc)
        size = size_bytes(item["size"], loc + ".size", positive=True)
        keep = count(item["keep"], loc + ".keep", 1)
        protected = count(item["protected"], loc + ".protected")
        occupied = size * (keep + protected)
        retained_full += occupied
        full_sizes.append(size)
        full_details.append({"label": name, "retained_bytes": occupied})

    # Intera nuova generazione: anche lavori sequenziali possono coesistere
    # prima del pruning. Non assumere che ogni file liberi subito il precedente.
    new_full = sum(full_sizes)
    retained_incremental = 0
    new_incremental = 0
    first_incremental = 0
    maintenance_workspace = 0
    incremental_details = []
    for i, item in enumerate(sequence(scenario["incremental_repositories"], "incremental_repositories")):
        loc = f"incremental_repositories[{i}]"
        fields(item, {"label", "base", "unique_change_per_point", "points", "maintenance_workspace"}, loc)
        name = label(item, loc)
        base = size_bytes(item["base"], loc + ".base", positive=True)
        change = size_bytes(item["unique_change_per_point"], loc + ".unique_change_per_point")
        points = count(item["points"], loc + ".points", 1)
        occupied = base + change * (points - 1)
        retained_incremental += occupied
        new_incremental += change
        first_incremental += base
        maintenance_workspace += size_bytes(item["maintenance_workspace"], loc + ".maintenance_workspace")
        incremental_details.append({"label": name, "retained_bytes": occupied})

    snapshot_hold = size_bytes(scenario["snapshot_hold"], "snapshot_hold")
    workspace = size_bytes(scenario["workspace"], "workspace") + maintenance_workspace
    steady = fixed + retained_full + retained_incremental + snapshot_hold
    peak = steady + new_full + new_incremental + workspace
    headroom = limit - peak

    runtime = fields(scenario["run_time"], {
        "throughput", "overhead_minutes", "window_minutes",
    }, "run_time")
    throughput = runtime["throughput"]
    if not isinstance(throughput, str) or not throughput.endswith("/s"):
        raise ScenarioError("run_time.throughput: usare byte al secondo, per esempio '20 MiB/s'")
    rate = size_bytes(throughput[:-2], "run_time.throughput", positive=True)
    overhead = count(runtime["overhead_minutes"], "run_time.overhead_minutes") * 60
    window = count(runtime["window_minutes"], "run_time.window_minutes", 1) * 60
    initial_write = sum(full_sizes) + first_incremental
    recurring_write = sum(full_sizes) + new_incremental
    initial_seconds = ceil_fraction(Fraction(initial_write, rate)) + overhead
    recurring_seconds = ceil_fraction(Fraction(recurring_write, rate)) + overhead
    fits_capacity = headroom >= 0
    fits_initial = initial_seconds <= window
    fits_recurring = recurring_seconds <= window

    return {
        "schema_version": 1,
        "input_status": scenario["input_status"],
        "operationally_validated": False,
        "decision": "fits_planned_bounds" if fits_capacity and fits_initial and fits_recurring else "exceeds_planned_bounds",
        "capacity": {
            "mirror_nominal_bytes": nominal,
            "filesystem_reserve_bytes": fs_reserve,
            "fraction_limit_bytes": fraction_limit,
            "planning_limit_bytes": limit,
        },
        "occupancy": {
            "fixed_bytes": fixed,
            "retained_full_bytes": retained_full,
            "retained_incremental_bytes": retained_incremental,
            "snapshot_hold_bytes": snapshot_hold,
            "new_full_bytes": new_full,
            "new_incremental_bytes": new_incremental,
            "workspace_bytes": workspace,
            "steady_bytes": steady,
            "peak_bytes": peak,
            "headroom_bytes": headroom,
        },
        "full_archives": full_details,
        "incremental_repositories": incremental_details,
        "timing": {
            "throughput_bytes_per_second": rate,
            "initial_write_bytes": initial_write,
            "recurring_write_bytes": recurring_write,
            "initial_seconds": initial_seconds,
            "recurring_seconds": recurring_seconds,
            "window_seconds": window,
            "fits_initial_window": fits_initial,
            "fits_recurring_window": fits_recurring,
        },
        "fits_capacity": fits_capacity,
        "uncertainties": list(uncertainties),
        "limits": [
            "Le dimensioni degli archivi e il tasso di dati unici sono input, non misure effettuate dallo strumento.",
            "Il costo reale di metadati, snapshot, manutenzione e crescita deve essere incluso negli input.",
            "Il modello non identifica dati esclusi e non dimostra backup, integrità o ripristino.",
            "Una velocità ipotetica produce tempi ipotetici, senza garanzia sulla finestra reale.",
        ],
    }


def load_scenario(path):
    def reject_constant(value):
        raise ScenarioError(f"JSON: costante non finita {value} non ammessa")

    def reject_duplicates(pairs):
        result = {}
        for key, value in pairs:
            if key in result:
                raise ScenarioError(f"JSON: chiave duplicata {key}")
            result[key] = value
        return result

    return json.loads(
        Path(path).read_text(encoding="utf-8-sig"),
        parse_constant=reject_constant,
        object_pairs_hook=reject_duplicates,
    )


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("scenario", type=Path, help="JSON esplicito, nessuna raccolta automatica")
    parser.add_argument("--json", action="store_true", help="risultato completo in JSON")
    args = parser.parse_args(argv)
    try:
        result = dimensiona(load_scenario(args.scenario))
    except (ScenarioError, OSError, UnicodeError, json.JSONDecodeError) as exc:
        print(f"Scenario non valido: {exc}", file=sys.stderr)
        return 2
    if args.json:
        print(json.dumps(result, indent=2, ensure_ascii=True))
    else:
        occupied = result["occupancy"]
        cap = result["capacity"]["planning_limit_bytes"]
        print(f"Esito del modello: {result['decision']}")
        print(f"Input: {result['input_status']}; validazione operativa: non eseguita")
        print(f"Budget: {cap / 10**9:.3f} GB ({cap / 2**30:.3f} GiB)")
        print(f"Picco: {occupied['peak_bytes'] / 10**9:.3f} GB; margine: {occupied['headroom_bytes'] / 10**9:.3f} GB")
        print(f"Durata iniziale: {result['timing']['initial_seconds']} s; ordinaria: {result['timing']['recurring_seconds']} s")
        print(f"Finestra disponibile: {result['timing']['window_seconds']} s")
        for uncertainty in result["uncertainties"]:
            print(f"Da misurare: {uncertainty}")
    return 0 if result["decision"] == "fits_planned_bounds" else 1


if __name__ == "__main__":
    raise SystemExit(main())
