# -*- coding: utf-8 -*-
"""
Guard-rail di anonimizzazione sui file tracciati da git.

Perche' esiste. Il repository e' destinato a un remoto pubblico: tutto cio' che entra in un
file tracciato diventa visibile a chiunque, per sempre, anche dopo una correzione successiva,
perche' la storia git resta consultabile. La regola che governa la materia e'
`.claude/rules/anonymization.md`, ma una regola scritta non impedisce un residuo. Il controllo
va fatto sull'intero albero tracciato e non sui soli file toccati dalla sessione: un residuo
non si introduce, si eredita.

Come non tradisce se stesso. Questo script e' versionato e non contiene nessun valore reale.
Prefissi di rete, nomi propri, numeri di serie, frammenti di ubicazione e organizzazioni
private da cercare vivono in `_notes/.anonymization-patterns.json`, ignorato da git accanto
alla mappa dei segnaposto. Se quel file manca, lo script lo dice e si ferma invece di dare un
esito verde che non ha calcolato.

Uso, dalla radice del progetto:
    python scripts/Test-Anonymization.py
    python scripts/Test-Anonymization.py --quiet     # solo il conteggio e l'esito
    python scripts/Test-Anonymization.py --max 20    # limita le righe stampate per categoria

Codice di uscita: 0 se non ci sono riscontri nelle categorie bloccanti, 1 altrimenti, 2 se il
file dei pattern manca o lo script non gira dalla radice del repository. Le categorie non
bloccanti raccolgono cio' che va guardato da un umano e che e' spesso un falso positivo, per
esempio un numero di build che somiglia a un indirizzo.
"""

import argparse
import collections
import io
import json
import os
import re
import subprocess
import sys

PATTERNS_FILE = os.path.join("_notes", ".anonymization-patterns.json")
SKIP_EXT = {".png", ".jpg", ".jpeg", ".gif", ".bmp", ".pdf", ".docx", ".doc",
            ".xlsx", ".xls", ".zip", ".7z", ".ico", ".drawio", ".pyc"}

# Categorie che fanno fallire il controllo: sono valori reali, non ambiguita'.
BLOCCANTI = {"IP REALE", "MAC REALE", "NOME PROPRIO", "SERIALE/ID MACCHINA",
             "UBICAZIONE", "ORGANIZZAZIONE PRIVATA", "SEGRETO LETTERALE",
             "EMAIL PERSONALE", "TELEFONO", "IBAN", "PIVA/CF"}

ORDINE = ["IP REALE", "MAC REALE", "SERIALE/ID MACCHINA", "UBICAZIONE",
          "ORGANIZZAZIONE PRIVATA", "SEGRETO LETTERALE", "NOME PROPRIO",
          "EMAIL PERSONALE", "TELEFONO", "IBAN", "PIVA/CF",
          "IMPORTO da valutare", "IP privato fuori schema", "IP pubblico da valutare"]

IPV4 = re.compile(r"\b(?:\d{1,3}\.){3}\d{1,3}(?:/\d{1,2})?\b")
MAC = re.compile(r"\b(?:[0-9A-Fa-f]{2}[:-]){5}[0-9A-Fa-f]{2}\b")
EMAIL = re.compile(r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}\b")
PHONE = re.compile(r"(?<![\d.+])(?:\+39[\s.]?)?3\d{2}[\s.-]?\d{3}[\s.-]?\d{3,4}(?![\d.])")
MONEY = re.compile(r"(?:€\s?\d[\d.,]*|\b\d[\d.,]*\s?€|\b[\d.]+[,.]\d{2}\s?(?:€|euro|EUR)\b|\b\d+(?:[.,]\d+)?\s?euro\b)", re.I)
IBAN = re.compile(r"\bIT\d{2}[A-Z0-9]{20,25}\b")
PIVA = re.compile(r"\b(?:P\.?\s?IVA|partita iva|cod\.?\s?fisc|codice fiscale)\b[^\n]{0,40}\d{11,16}", re.I)
# Segnaposto legittimi per la posta: persona-a@, autore-linkedin-a@, e simili.
MAIL_PLACEHOLDER = re.compile(r"^(persona|autore|referente|collaboratore|consulente)-", re.I)


def carica_pattern():
    if not os.path.exists(PATTERNS_FILE):
        sys.stderr.write(
            "File dei pattern non trovato: %s\n"
            "Serve per sapere che cosa cercare, e non e' versionato perche' contiene i valori\n"
            "reali. Ricostruirlo da _notes/.anonymization-map.md.\n" % PATTERNS_FILE)
        sys.exit(2)
    with io.open(PATTERNS_FILE, encoding="utf-8") as fh:
        return json.load(fh)


def file_tracciati(includi_nuovi=False):
    """Elenco dei file da esaminare.

    Di default sono i soli file tracciati. Con `includi_nuovi` si aggiungono i file non
    ancora aggiunti all'indice ma non ignorati dal `.gitignore`, cioe' esattamente quelli
    che un `git add` porterebbe dentro. Serve perche' il controllo va fatto prima del
    commit, e prima del primo commit di una feature i file nuovi non sono ancora tracciati:
    senza questa opzione il verde sarebbe un verde non calcolato su di essi.
    """
    argomenti = ["git", "ls-files", "--cached"]
    if includi_nuovi:
        argomenti += ["--others", "--exclude-standard"]
    out = subprocess.run(argomenti, capture_output=True, text=True).stdout
    return sorted({f for f in out.split("\n") if f.strip()})


def analizza(pat, files, escludi):
    trovati = collections.defaultdict(list)

    def aggiungi(cat, path, ln, riga, hit):
        trovati[cat].append((path, ln, hit, riga.strip()[:190]))

    doc_nets = tuple(pat["reti_documentali_ammesse"])
    ip_ok = set(pat["ip_ammessi"])
    reali = tuple(pat["prefissi_reali"])
    mac_ok = tuple(m.upper() for m in pat["mac_ammessi_prefissi"])
    mail_ok = set(m.lower() for m in pat["email_ammesse"])
    nomi = [(n, re.compile(r"\b" + re.escape(n) + r"\b", re.I))
            for n in pat.get("nomi_propri", []) if n]
    nomi_ctx = pat.get("nomi_ammessi_in_contesto", [])
    seriali = pat.get("seriali_e_id", [])
    ubicazione = pat.get("ubicazione", [])
    organizzazioni = pat.get("organizzazioni_private", [])
    segreti = pat.get("segreti_letterali", [])
    telefoni = pat.get("telefoni_reali", [])
    importi_ok = set(pat.get("importi_ammessi", []))

    for f in files:
        if os.path.splitext(f)[1].lower() in SKIP_EXT:
            continue
        if any(f.replace("\\", "/").startswith(p) for p in escludi):
            continue
        try:
            with io.open(f, encoding="utf-8", errors="replace") as fh:
                contenuto = fh.read()
        except (IOError, OSError):
            continue

        for ln, riga in enumerate(contenuto.split("\n"), 1):
            for m in IPV4.finditer(riga):
                ip = m.group(0)
                base = ip.split("/")[0]
                if base in ip_ok or base.startswith(doc_nets):
                    continue
                if base.startswith(reali):
                    aggiungi("IP REALE", f, ln, riga, ip)
                elif base.startswith(("10.", "192.168.", "172.")):
                    aggiungi("IP privato fuori schema", f, ln, riga, ip)
                else:
                    aggiungi("IP pubblico da valutare", f, ln, riga, ip)

            for m in MAC.finditer(riga):
                mac = m.group(0).upper()
                if not mac.startswith(mac_ok):
                    aggiungi("MAC REALE", f, ln, riga, mac)

            for m in EMAIL.finditer(riga):
                mail = m.group(0)
                if mail.lower() in mail_ok or MAIL_PLACEHOLDER.match(mail.split("@")[0]):
                    continue
                aggiungi("EMAIL PERSONALE", f, ln, riga, mail)

            for m in MONEY.finditer(riga):
                cifra = re.sub(r"[^\d.,]", "", m.group(0))
                if cifra in importi_ok:
                    continue
                aggiungi("IMPORTO da valutare", f, ln, riga, m.group(0)[:60])

            for regex, cat in ((PHONE, "TELEFONO"), (IBAN, "IBAN"), (PIVA, "PIVA/CF")):
                for m in regex.finditer(riga):
                    aggiungi(cat, f, ln, riga, m.group(0)[:60])

            for valore, cat in ([(s, "SERIALE/ID MACCHINA") for s in seriali] +
                                [(u, "UBICAZIONE") for u in ubicazione] +
                                [(o, "ORGANIZZAZIONE PRIVATA") for o in organizzazioni] +
                                [(t, "TELEFONO") for t in telefoni]):
                if valore and valore in riga:
                    aggiungi(cat, f, ln, riga, "<valore oscurato>")

            for s in segreti:
                if s and s in riga:
                    aggiungi("SEGRETO LETTERALE", f, ln, riga, "<valore oscurato>")

            bassa = riga.lower()
            for n, rx in nomi:
                if not rx.search(riga):
                    continue
                if any(c.lower() in bassa for c in nomi_ctx):
                    continue
                aggiungi("NOME PROPRIO", f, ln, riga, "<valore oscurato>")

    return trovati


def main():
    ap = argparse.ArgumentParser(description="Guard-rail di anonimizzazione sui file tracciati.")
    ap.add_argument("--quiet", action="store_true", help="stampa solo il riepilogo")
    ap.add_argument("--max", type=int, default=40, help="righe stampate per categoria")
    ap.add_argument("--escludi", nargs="*", default=[],
                    help="prefissi di percorso da saltare, per esempio .claude/templates/")
    ap.add_argument("--includi-nuovi", action="store_true", dest="includi_nuovi",
                    help="esamina anche i file non ancora tracciati ma non ignorati, "
                         "cioe' quelli che un git add porterebbe dentro")
    args = ap.parse_args()

    if not os.path.isdir(".git"):
        sys.stderr.write("Eseguire dalla radice del repository.\n")
        return 2

    pat = carica_pattern()
    files = file_tracciati(args.includi_nuovi)
    trovati = analizza(pat, files, args.escludi)

    bloccanti = 0
    da_guardare = 0
    for cat in ORDINE:
        voci = trovati.get(cat, [])
        if not voci:
            continue
        if cat in BLOCCANTI:
            bloccanti += len(voci)
        else:
            da_guardare += len(voci)
        if args.quiet:
            continue
        etichetta = "BLOCCANTE" if cat in BLOCCANTI else "da valutare"
        print("\n" + "=" * 78)
        print("%s  [%s]  -  %d riscontri" % (cat, etichetta, len(voci)))
        print("=" * 78)
        for path, ln, hit, testo in voci[:args.max]:
            print("  %s:%s  [%s]" % (path, ln, hit))
            print("      %s" % testo)
        if len(voci) > args.max:
            print("  ... e altri %d (usare --max)" % (len(voci) - args.max))

    etichetta = "tracciati e nuovi" if args.includi_nuovi else "tracciati"
    print("\n%d file %s esaminati." % (len(files), etichetta))
    print("Riscontri bloccanti: %d.  Da valutare a mano: %d." % (bloccanti, da_guardare))
    if bloccanti:
        print("ESITO: FALLITO. Bonificare i riscontri bloccanti prima del commit.")
        return 1
    print("ESITO: pulito sulle categorie bloccanti.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
