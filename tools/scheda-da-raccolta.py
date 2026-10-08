# -*- coding: utf-8 -*-
"""Scheda dispositivo anonimizzata a partire da una raccolta in sola lettura (ADR-021).

Legge il JSON scritto da `tools/raccolta-dispositivo.ps1` o `tools/raccolta-dispositivo.sh`
e stampa la scheda a campi fissi descritta in
`docs/05-analisi-del-caso/02-scheda-dispositivo.md`, in Markdown, pronta da copiare nel
censimento. È deterministico: ciò che si ricava dalla raccolta si compila, il resto resta
"da compilare" e lo si scrive a mano, perché collocazione ed esposizione sono decisioni e
non fatti della macchina.

Che cosa non esce mai: nome macchina, indirizzi MAC, SSID, versione esatta dei driver. Sono
nella raccolta, che vive in `_notes/`, e restano lì. La scheda porta solo l'ID documentale.

Le chiavi di `netsh` cambiano con la lingua di Windows, quindi gli standard Wi-Fi e WPA3 si
cercano nei valori e non nei nomi delle chiavi.

Uso:
    python tools/scheda-da-raccolta.py _notes/censimento/raccolte/PC-01-2026-10-08.json
    python tools/scheda-da-raccolta.py <raccolta.json> --categoria "PC fisso"
    python tools/scheda-da-raccolta.py --autotest
"""

import argparse
import io
import json
import re
import sys

for _flusso in (sys.stdout, sys.stderr):
    try:
        _flusso.reconfigure(encoding="utf-8", errors="replace")
    except (AttributeError, ValueError):
        pass

DA_COMPILARE = "da compilare"
GENERAZIONI = [("be", "Wi-Fi 7"), ("ax", "Wi-Fi 6/6E"), ("ac", "Wi-Fi 5"), ("n", "Wi-Fi 4")]


def velocita_mbps(testo):
    """'2.5 Gbps Full Duplex' -> 2500; '100 Mbps' -> 100; altrimenti None."""
    m = re.search(r"(\d+(?:[.,]\d+)?)\s*([GM])b(?:ps|/s|it)", testo or "", re.I)
    if not m:
        m = re.search(r"(\d+)base", testo or "", re.I)
        return int(m.group(1)) if m else None
    n = float(m.group(1).replace(",", "."))
    return int(n * 1000) if m.group(2).upper() == "G" else int(n)


def formato_velocita(mbps):
    if mbps is None:
        return DA_COMPILARE
    return ("%g Gbps" % (mbps / 1000)) if mbps >= 1000 else ("%d Mbps" % mbps)


def standard_wifi(testi):
    """Dagli standard 802.11 elencati nei testi, la generazione più alta e l'elenco."""
    trovati = set()
    for t in testi:
        for m in re.finditer(r"802\.11\s*([a-z]{1,2}(?:/[a-z]{1,2})*)", t or "", re.I):
            for s in m.group(1).lower().split("/"):
                trovati.add(s)
        # forme come "802.11a 802.11g 802.11ax" o "802.11b/g/n/ax/be"
        for m in re.finditer(r"\b802\.11([a-z]{1,2})\b", t or "", re.I):
            trovati.add(m.group(1).lower())
    for sigla, nome in GENERAZIONI:
        if sigla in trovati:
            return nome, sorted(trovati)
    return (None, sorted(trovati))


def da_windows(d):
    righe_eth, wifi = [], None
    for s in d.get("schede_di_rete", []):
        desc = s.get("descrizione") or ""
        tipo = (s.get("tipo_fisico") or "").lower()
        ammesse = [velocita_mbps(v) for v in (s.get("velocita_ammesse") or [])]
        massima = max([v for v in ammesse if v] or [None]) if any(ammesse) else None
        if "802.11" in tipo or "wireless" in tipo or "wi-fi" in desc.lower() or "wireless" in desc.lower():
            wifi = desc
            continue
        righe_eth.append((desc, formato_velocita(massima),
                          s.get("velocita_negoziata") or DA_COMPILARE, s.get("stato") or ""))
    valori = [c.get("valore", "") for c in d.get("wifi_driver", [])]
    generazione, sigle = standard_wifi(valori)
    wpa3 = any("WPA3" in v for v in valori)
    connessione = [c.get("valore", "") for c in d.get("wifi_connessione", [])]
    gen_conn, _ = standard_wifi(connessione)
    sistema = d.get("sistema", {})
    return {
        "sistema": "%s, build %s" % (sistema.get("nome", DA_COMPILARE), sistema.get("build", "?")),
        "eth": righe_eth,
        "wifi_chip": wifi,
        "wifi_gen": generazione,
        "wifi_sigle": sigle,
        "wpa3": ("sì" if wpa3 else "no") if valori else None,
        "wifi_in_uso": gen_conn,
    }


def da_linux(d):
    pretty = re.search(r'PRETTY_NAME="?([^"\n]+)', d.get("os_release", ""))
    righe_eth = []
    for dev, testo in (d.get("ethtool") or {}).items():
        if not isinstance(testo, str) or "Supported link modes" not in testo:
            continue
        modi = re.search(r"Supported link modes:(.*?)(?:\n\s*Supported pause|\n\s*Supports auto)", testo, re.S)
        massima = max([velocita_mbps(x) or 0 for x in re.findall(r"\d+base\S*", modi.group(1))] or [0]) if modi else 0
        att = re.search(r"Speed:\s*(\S+)", testo)
        righe_eth.append((dev, formato_velocita(massima or None), att.group(1) if att else DA_COMPILARE, ""))
    iw = d.get("iw_list", "")
    sigle = set()
    if isinstance(iw, str) and "non installato" not in iw:
        if "EHT" in iw:
            sigle.add("be")
        if "HE Iftypes" in iw or "HE PHY" in iw:
            sigle.add("ax")
        if "VHT" in iw:
            sigle.add("ac")
        if "HT20" in iw or "HT Capab" in iw:
            sigle.add("n")
    generazione = next((nome for s, nome in GENERAZIONI if s in sigle), None)
    return {
        "sistema": "%s, kernel %s" % (pretty.group(1) if pretty else DA_COMPILARE, d.get("kernel", "?")),
        "eth": righe_eth,
        "wifi_chip": None,
        "wifi_gen": generazione,
        "wifi_sigle": sorted(sigle),
        "wpa3": ("sì" if "SAE" in iw else "da verificare") if isinstance(iw, str) and sigle else None,
        "wifi_in_uso": None,
    }


def scheda(d, categoria=None):
    estratto = da_windows(d) if d.get("piattaforma") == "windows" else da_linux(d)
    hw = d.get("hardware", {})
    mem = hw.get("memoria_gb")
    if mem is None and hw.get("memoria_kb"):
        try:
            mem = round(int(hw["memoria_kb"]) / 1048576, 1)
        except ValueError:
            mem = None
    righe = ["### %s" % d.get("id", "ID mancante"), ""]

    def campo(nome, valore):
        righe.append("**%s.** %s" % (nome, valore if valore else DA_COMPILARE))
        righe.append("")

    modello = "%s %s" % (hw.get("produttore") or "", hw.get("modello") or "")
    # Sui PC assemblati il modello di sistema è un segnaposto del firmware: vale la scheda madre.
    if re.search(r"system product name|to be filled|default string", modello, re.I) and hw.get("scheda_madre"):
        modello = "assemblato, scheda madre %s" % hw["scheda_madre"]
    campo("Identità", "categoria %s; %s; proprietario per ruolo: %s" % (
        categoria or DA_COMPILARE, modello.strip() or DA_COMPILARE, DA_COMPILARE))
    campo("Sistema", "%s; processore %s; memoria %s GB; supporto e aggiornamenti: %s" % (
        estratto["sistema"], (hw.get("processore") or DA_COMPILARE).strip(), mem if mem else "?", DA_COMPILARE))
    if estratto["eth"]:
        parti = ["%s, massima %s, negoziata %s" % (desc, mx, neg) for desc, mx, neg, _ in estratto["eth"]]
        campo("Rete cablata", "; ".join(parti))
    else:
        campo("Rete cablata", "nessuna scheda Ethernet rilevata")
    if estratto["wifi_gen"] or estratto["wifi_chip"]:
        campo("Wi-Fi", "%s%s; standard 802.11 %s; WPA3 %s; 802.1X: %s" % (
            (estratto["wifi_chip"] + ", ") if estratto["wifi_chip"] else "",
            estratto["wifi_gen"] or "generazione non rilevata",
            "/".join(estratto["wifi_sigle"]) or "?",
            estratto["wpa3"] or "da verificare", "da verificare"))
    else:
        campo("Wi-Fi", "nessuna radio rilevata")
    campo("Collocazione", "cablato o Wi-Fi, piano, porta dello switch o SSID, VLAN: %s" % DA_COMPILARE)
    campo("Esposizione", "servizi offerti, inoltri necessari, sensibilità dei dati: %s" % DA_COMPILARE)
    campo("Fonte", "raccolta in sola lettura del %s, conservata in `_notes/censimento/raccolte/`" % (
        (d.get("raccolto_il") or "?")[:10]))
    return "\n".join(righe).rstrip() + "\n"


def autotest():
    errori = 0
    casi = [("2.5 Gbps Full Duplex", 2500), ("100 Mbps Half Duplex", 100), ("1000baseT/Full", 1000),
            ("Auto Negotiation", None)]
    for testo, atteso in casi:
        if velocita_mbps(testo) != atteso:
            errori += 1
            print("velocità %r: atteso %s, ottenuto %s" % (testo, atteso, velocita_mbps(testo)))
    gen, _ = standard_wifi(["802.11b 802.11g 802.11n 802.11a 802.11ac 802.11ax"])
    if gen != "Wi-Fi 6/6E":
        errori += 1
        print("standard: atteso Wi-Fi 6/6E, ottenuto %s" % gen)
    gen, _ = standard_wifi(["802.11b/g/n/ax/be"])
    if gen != "Wi-Fi 7":
        errori += 1
        print("standard a barre: atteso Wi-Fi 7, ottenuto %s" % gen)
    finto = {"formato": "raccolta-dispositivo/1", "id": "PC-99", "piattaforma": "windows",
             "nome_macchina": "SEGRETO-HOST", "raccolto_il": "2026-10-08T10:00:00",
             "sistema": {"nome": "Windows 11 Pro", "build": "26200"},
             "hardware": {"produttore": "Acme", "modello": "X1", "processore": "CPU", "memoria_gb": 16},
             "schede_di_rete": [{"descrizione": "Realtek 2.5GbE", "tipo_fisico": "802.3", "stato": "Up",
                                 "velocita_negoziata": "1 Gbps", "mac": "AA:BB:CC:00:00:99",
                                 "velocita_ammesse": ["1.0 Gbps Full Duplex", "2.5 Gbps Full Duplex"]}],
             "wifi_driver": [{"chiave": "Tipi di radio", "valore": "802.11ax 802.11ac"},
                             {"chiave": "Autenticazione", "valore": "WPA3-Personal CCMP"}],
             "wifi_connessione": [{"chiave": "SSID", "valore": "RETE-SEGRETA"}]}
    out = scheda(finto, "PC fisso")
    for vietato in ("SEGRETO-HOST", "AA:BB:CC:00:00:99", "RETE-SEGRETA"):
        if vietato in out:
            errori += 1
            print("la scheda contiene un dato che non deve uscire: %s" % vietato)
    for atteso in ("massima 2.5 Gbps", "Wi-Fi 6/6E", "WPA3 sì", "### PC-99"):
        if atteso not in out:
            errori += 1
            print("la scheda non contiene %r" % atteso)
    print("autotest: %d errori" % errori)
    return 1 if errori else 0


def main():
    if "--autotest" in sys.argv[1:]:
        return autotest()
    ap = argparse.ArgumentParser(description="Scheda dispositivo anonimizzata da una raccolta.")
    ap.add_argument("raccolta")
    ap.add_argument("--categoria", default=None)
    args = ap.parse_args()
    with io.open(args.raccolta, encoding="utf-8-sig") as fh:
        d = json.load(fh)
    sys.stdout.write(scheda(d, args.categoria))
    return 0


if __name__ == "__main__":
    sys.exit(main())
