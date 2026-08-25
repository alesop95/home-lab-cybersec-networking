# -*- coding: utf-8 -*-
"""Controllo di coerenza dell'albero della documentazione.

Perche' esiste. Dal 25/08/2026 l'albero `docs/` non e' piu' generato dal documento
sorgente ma scritto e manutenuto a mano, sessione dopo sessione (ADR-010). Un albero
generato era coerente per costruzione, perche' la struttura discendeva dai titoli del
sorgente; un albero scritto a mano si sfalda in due modi silenziosi, ed e' quello che
questo strumento cerca.

Il primo modo e' il file orfano: un documento che esiste sul disco ma che nessun indice
collega, quindi nessuno lo trova navigando e nessuno si accorge che e' rimasto indietro.
E' il residuo tipico di una sezione rinominata o spostata.

Il secondo modo e' il collegamento rotto: un riferimento relativo che punta a un percorso
che non esiste piu'. Nella documentazione tecnica un collegamento rotto e' peggio di un
collegamento assente, perche' promette una fonte che non c'e'.

Lo strumento e' in sola lettura: non cancella e non riscrive niente. Un orfano puo' essere
un errore o una scelta, e la differenza la sa solo chi scrive.

Uso, dalla radice del progetto:
    python tools/check-docs-tree.py
    python tools/check-docs-tree.py --radice docs --indice README.md
    python tools/check-docs-tree.py --quiet

Codice di uscita: 0 se non ci sono collegamenti rotti ne' orfani, 1 altrimenti.
"""

import argparse
import io
import os
import posixpath
import re
import sys
from urllib.parse import unquote

# Collegamenti Markdown in linea: [testo](destinazione). Si escludono le immagini,
# che nell'albero puntano a file non versionati e la cui assenza e' voluta.
#
# Il testo del collegamento puo' contenere a sua volta una coppia di parentesi quadre,
# ed e' il caso normale qui: molti titoli portano il marcatore [TBC], quindi negli indici
# generati compaiono voci nella forma [[TBC] Titolo](percorso). Un'espressione che vieta
# la parentesi quadra dentro il testo non riconosce quelle voci, e il risultato non e' un
# errore visibile ma un falso allarme: decine di documenti perfettamente collegati che
# risultano irraggiungibili. Si ammette quindi un livello di annidamento.
LINK = re.compile(r"(?<!\!)\[(?:[^\[\]\n]|\[[^\]\n]*\])*\]\(([^)\s]+)(?:\s+\"[^\"]*\")?\)")
ESTERNO = re.compile(r"^(?:https?:|mailto:|#)")


def elenca_documenti(radice):
    trovati = []
    for base, dirs, files in os.walk(radice):
        dirs.sort()
        for f in sorted(files):
            if f.endswith(".md"):
                trovati.append(os.path.join(base, f).replace(os.sep, "/"))
    return trovati


def collegamenti(percorso):
    testo = io.open(percorso, encoding="utf-8", errors="replace").read()
    for m in LINK.finditer(testo):
        dest = m.group(1).split("#", 1)[0]
        if not dest or ESTERNO.match(dest):
            continue
        yield unquote(dest)


def risolvi(sorgente, destinazione):
    return posixpath.normpath(posixpath.join(posixpath.dirname(sorgente), destinazione))


def main():
    ap = argparse.ArgumentParser(description="Coerenza dell'albero della documentazione.")
    ap.add_argument("--radice", default="docs", help="cartella da esaminare")
    ap.add_argument("--indice", default="README.md",
                    help="nome del file indice da cui parte la raggiungibilita'")
    ap.add_argument("--quiet", action="store_true", help="stampa solo il riepilogo")
    args = ap.parse_args()

    if not os.path.isdir(args.radice):
        sys.stderr.write("Cartella non trovata: %s\n" % args.radice)
        return 2

    documenti = elenca_documenti(args.radice)
    esistenti = set(documenti)

    # 1. Collegamenti rotti, su tutti i documenti.
    rotti = []
    grafo = {}
    for doc in documenti:
        uscenti = []
        for dest in collegamenti(doc):
            risolto = risolvi(doc, dest)
            uscenti.append(risolto)
            if risolto in esistenti:
                continue
            if os.path.exists(risolto):
                continue  # punta a qualcosa che non e' un .md ma esiste
            rotti.append((doc, dest, risolto))
        grafo[doc] = uscenti

    # 2. Raggiungibilita' dagli indici: visita a partire dall'indice di radice.
    partenza = "%s/%s" % (args.radice.rstrip("/"), args.indice)
    raggiunti = set()
    if partenza in esistenti:
        coda = [partenza]
        while coda:
            corrente = coda.pop()
            if corrente in raggiunti:
                continue
            raggiunti.add(corrente)
            for prossimo in grafo.get(corrente, []):
                if prossimo in esistenti and prossimo not in raggiunti:
                    coda.append(prossimo)
    else:
        sys.stderr.write("Indice di radice assente: %s\n" % partenza)

    # Un documento e' orfano se nessun altro documento lo collega. Gli indici di cartella
    # non lo sono mai, perche' rappresentano la cartella stessa.
    collegati = set()
    for uscenti in grafo.values():
        collegati.update(uscenti)
    orfani = [d for d in documenti
              if d not in collegati
              and d != partenza
              and os.path.basename(d) != args.indice]

    # Un documento raggiungibile ma non dall'indice di radice e' un caso a parte: esiste
    # un collegamento, ma navigando dalla home non ci si arriva.
    isolati = [d for d in documenti if d not in raggiunti and d not in orfani and d != partenza]

    if not args.quiet:
        if rotti:
            print("\n" + "=" * 78)
            print("COLLEGAMENTI ROTTI  [BLOCCANTE]  -  %d" % len(rotti))
            print("=" * 78)
            for doc, dest, risolto in rotti:
                print("  %s" % doc)
                print("      -> %s   (risolve in %s)" % (dest, risolto))
        if orfani:
            print("\n" + "=" * 78)
            print("DOCUMENTI ORFANI  [BLOCCANTE]  -  %d" % len(orfani))
            print("=" * 78)
            print("  Esistono sul disco ma nessun indice li collega.")
            for d in orfani:
                print("  %s" % d)
        if isolati:
            print("\n" + "=" * 78)
            print("NON RAGGIUNGIBILI DALLA HOME  [da valutare]  -  %d" % len(isolati))
            print("=" * 78)
            print("  Qualcuno li collega, ma non si arriva navigando da %s." % partenza)
            for d in isolati:
                print("  %s" % d)

    print("\n%d documenti esaminati, %d raggiungibili dalla home."
          % (len(documenti), len(raggiunti)))
    print("Collegamenti rotti: %d.  Orfani: %d.  Non raggiungibili: %d."
          % (len(rotti), len(orfani), len(isolati)))
    if rotti or orfani:
        print("ESITO: FALLITO.")
        return 1
    print("ESITO: albero coerente.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
