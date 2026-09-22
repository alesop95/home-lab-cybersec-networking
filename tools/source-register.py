"""Censisce i riferimenti pubblici senza perdere quelli rimossi dai documenti.

SOURCES.md resta il registro canonico. Questo programma modifica soltanto il
blocco derivato delimitato dai marker; non cambia le schede curate. Non accede
alla rete, a _notes o ai template di altri progetti. --check e' sola lettura.
"""

import argparse
import hashlib
import json
import re
import subprocess
from pathlib import Path
from urllib.parse import urlsplit

ROOT = Path(__file__).resolve().parents[1]
START = "<!-- BEGIN SOURCE COVERAGE -->"
END = "<!-- END SOURCE COVERAGE -->"
URL = re.compile(r"https?://[^\s<>\"`\]\[()]+")


def urls(text):
    return {m.group().rstrip(".,;:") for m in URL.finditer(text)}


def public_files():
    proc = subprocess.run(
        ["git", "ls-files", "--cached", "--others", "--exclude-standard", "-z"],
        cwd=ROOT, check=True, capture_output=True,
    )
    for name in sorted(set(proc.stdout.decode("utf-8").split("\0"))):
        if not name.endswith(".md") or name == "SOURCES.md":
            continue
        if name.startswith(("docs/", "nas-consolidation/", ".claude/context/", ".claude/memory/")) or name in ("README.md", "CLAUDE.md"):
            path = ROOT / name
            if path.is_file():
                yield name, path.read_text(encoding="utf-8-sig")


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--check", action="store_true")
    args = parser.parse_args()
    target = ROOT / "SOURCES.md"
    original = target.read_text(encoding="utf-8")
    before, tail = original.split(START, 1)
    old_block, after = tail.split(END, 1)
    records = {}
    for line in old_block.splitlines():
        if not line.startswith("| H-"):
            continue
        cells = [s.strip() for s in line.strip("|").split("|")]
        records[cells[1]] = set(re.findall(r"`([^`]+)`", cells[2]))
    curated = urls(before + after)
    current = {}
    for name, content in public_files():
        for url in urls(content):
            current.setdefault(url, set()).add(name)
    discovery = ROOT / "docs/fonti/ricerca-2026-09-22.json"
    if discovery.exists():
        for url in json.loads(discovery.read_text(encoding="utf-8"))["urls"]:
            current.setdefault(url, set()).add("docs/fonti/ricerca-2026-09-22.json")
    missing = sorted(set(current) - curated - set(records))
    if args.check:
        print(f"Riferimenti rilevati: {len(current)}; non registrati: {len(missing)}")
        for url in missing:
            print(url)
        return bool(missing)
    for url, locations in current.items():
        if url not in curated or url in records:
            records.setdefault(url, set()).update(locations)
    lines = ["", "", "| ID stabile | URL esatto | Provenienza conservata | Stato |", "|---|---|---|---|"]
    for url, locations in sorted(records.items()):
        # L'hash dipende dall'URL, non dall'ordine: gli ID non si rinumerano.
        # Inseriamo separatori alfabetici: gli ID restano stabili ma non
        # sembrano numeri telefonici al guard-rail di anonimizzazione.
        digest = hashlib.sha256(url.encode()).hexdigest()[:12]
        key = "x".join(digest[i:i + 3] for i in range(0, 12, 3))
        origin = "; ".join(f"`{p}`" for p in sorted(locations))
        status = "scheda curata sopra" if url in curated else "censita; lettura e contenuto da verificare"
        lines.append(f"| H-{key} | {url} | {origin} | {status} |")
    target.write_text(before + START + "\n".join(lines) + "\n\n" + END + after, encoding="utf-8")
    print(f"Registro aggiornato: {len(records)} riferimenti nel censimento; {len(missing)} nuovi.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
