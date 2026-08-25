---
generated-from-commit: e89779723cb1ed715b781763011255a81a82700e
generated-from-branch: main
generated-date: 2026-08-25
covers-paths:
  - tools/**
  - scripts/**
  - docs/**
last-verified-commit: 494b45e
---

# Esecuzione e manutenzione della documentazione

> Scheda tecnica. Descrive le procedure eseguibili di questo repository. Qui non si distribuisce software: si scrive documentazione e si verifica che sia coerente e pubblicabile. La sequenza va rispettata nell'ordine indicato, perche' ogni passo assume l'esito del precedente.

## Il modello, dal 25/08/2026

L'albero `docs/` si scrive e si modifica a mano. Non si rigenera piu' dal documento Word, che resta in `_notes/sorgenti/` come archivio della prima stesura. Il razionale e' in ADR-010; qui conta la conseguenza operativa, che e' semplice: si apre una sessione, si modifica un file Markdown, si eseguono i controlli, si committa.

Il convertitore `tools/docx-to-md.py` resta nel repository come strumento che ha prodotto l'albero, ma non va eseguito su `docs/`. Non e' una raccomandazione affidata alla memoria: il convertitore scrive nella destinazione un timbro `.generato-da-docx` e si rifiuta di scrivere in una cartella che contiene documenti senza quel timbro. Su `docs/` il timbro e' stato rimosso, quindi una corsa accidentale si ferma con codice 2 e un messaggio che spiega perche'. Resta utilizzabile su una destinazione nuova, per esempio se un giorno servisse convertire un altro documento.

## Prerequisiti

Python 3 sul PATH. Per i soli controlli non serve altro. Il pacchetto `python-docx` serve unicamente al convertitore, che ormai non si usa; `Pillow` serve solo se si rigenerano le copie ridotte delle fotografie.

Il file `_notes/.anonymization-patterns.json` deve esistere, altrimenti il guard-rail si ferma con codice 2 invece di dare un verde non calcolato. Non e' nel repository per costruzione, e su una macchina nuova va ricostruito da `_notes/.anonymization-map.md`, anch'esso non versionato. In pratica un clone del repository puo' leggere e modificare la documentazione, ma non puo' verificarne l'anonimizzazione senza il materiale privato dell'autore. E' una conseguenza voluta.

## Modificare la documentazione

Non c'e' una procedura: si modifica il file. Contano tre regole, e sono tutte conseguenze del fatto che l'albero e' navigabile e pubblico.

Un file nuovo va collegato dall'indice della sua cartella, altrimenti esiste ma nessuno lo trova. Un file spostato o rinominato lascia collegamenti rotti altrove, che vanno sistemati nello stesso commit. Un contenuto nuovo che contiene un valore reale va anonimizzato mentre lo si scrive, aggiungendo prima la voce alla mappa e al file dei pattern: il sidecar di redazione non gira piu', quindi nessuno lo fa piu' al posto tuo.

I prefissi numerici di cartelle e file vengono dalla generazione iniziale e ora sono soltanto nomi stabili. Non si rinumerano per inserire qualcosa in mezzo: si usa il primo numero libero, anche se rompe l'ordine alfabetico, perche' rinumerare significa rinominare file e rompere ogni collegamento che li citava.

## I quattro controlli, prima di ogni commit

Il primo verifica che l'albero regga come struttura navigabile: nessun documento scollegato dagli indici, nessun collegamento relativo che punti a un percorso inesistente.

```powershell
python tools/check-docs-tree.py
```

```bash
python tools/check-docs-tree.py
```

Il secondo attua la convenzione di formattazione, cioe' un paragrafo per riga sorgente. Lo strumento rifiuta di scrivere un file il cui rendering cambierebbe, quindi e' sicuro da lanciare sull'intero albero; con `--check` non scrive e segnala soltanto.

```powershell
python tools/md-unwrap.py --check .
```

```bash
python tools/md-unwrap.py --check .
```

Il terzo copre il punto cieco del secondo, che per contratto non entra nei blocchi recintati, e segnala i comandi di shell spezzati su piu' righe.

```powershell
python tools/lint-md-commands.py .
```

```bash
python tools/lint-md-commands.py .
```

Il quarto e' quello che decide se il commit e' pubblicabile.

```powershell
python scripts/Test-Anonymization.py
```

```bash
python scripts/Test-Anonymization.py
```

Passa tutti i file tracciati da git ed esce con codice diverso da zero se trova riscontri nelle categorie bloccanti. Le categorie non bloccanti raccolgono cio' che va guardato da un umano, tipicamente indirizzi pubblici di transito e cifre che somigliano a importi. Va eseguito sull'intero albero e non sui soli file toccati.

Quando il commit introduce file nuovi, non ancora aggiunti all'indice, va eseguito con l'opzione che li comprende, altrimenti l'esito sarebbe verde su un insieme che non contiene cio' che si sta per pubblicare.

```powershell
python scripts/Test-Anonymization.py --includi-nuovi
```

```bash
python scripts/Test-Anonymization.py --includi-nuovi
```

L'opzione aggiunge all'elenco i file non tracciati ma non ignorati dal `.gitignore`, cioe' esattamente quelli che un `git add` porterebbe dentro. Non tocca l'indice e non modifica nulla.

## La sequenza completa

Si modifica un file, si collega dall'indice se e' nuovo, si esegue il controllo di coerenza, si normalizza la formattazione, si controllano i blocchi di comando, si aggiunge all'indice di git, si esegue il guard-rail con l'opzione sui file nuovi, si committa e si pusha. Le ultime due operazioni sono manuali dell'utente e l'agente non le esegue.

```bash
python tools/check-docs-tree.py && python tools/md-unwrap.py --check . && python tools/lint-md-commands.py . && python scripts/Test-Anonymization.py --includi-nuovi
```

## Rigenerare da un documento Word, se un giorno servisse

Non su `docs/`, che e' protetto dal timbro. Su una destinazione nuova, per confrontare o per importare un documento diverso.

```powershell
python tools/docx-to-md.py "percorso/del/documento.docx" --out cartella-nuova --clean
```

```bash
python tools/docx-to-md.py "percorso/del/documento.docx" --out cartella-nuova --clean
```

L'opzione `--clean` rimuove il rumore ereditato dal sorgente, cioe' emoji, trattini lunghi normalizzati in trattini brevi e righe segnaposto di corpo composte da una sola lettera ripetuta; senza quell'opzione la conversione e' strettamente verbatim. Il report scritto nella destinazione riporta i conteggi, e il rapporto fra titoli scritti e titoli del sorgente deve risultare pari. Il sidecar `tools/redactions.json`, se presente, viene ancora applicato: su un documento nuovo con dati reali va aggiornato prima, non dopo.

## Non c'e' distribuzione

Non esiste un deploy: non c'e' un sito, non c'e' un pacchetto, non c'e' un servizio. La pubblicazione coincide con il push su GitHub, ed e' per questo che il guard-rail e' l'ultima cosa che gira prima di essa. Se un giorno la documentazione venisse pubblicata come sito statico, quella sarebbe una nuova procedura da aggiungere qui, e il guard-rail resterebbe comunque il passo che la precede.
