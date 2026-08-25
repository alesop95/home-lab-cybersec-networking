---
generated-from-commit: e89779723cb1ed715b781763011255a81a82700e
generated-from-branch: main
generated-date: 2026-08-24
covers-paths:
  - tools/**
  - scripts/**
  - docs/**
last-verified-commit: e89779723cb1ed715b781763011255a81a82700e
---

# Esecuzione e rigenerazione

> Scheda tecnica. Descrive le procedure eseguibili di questo repository. Qui non si distribuisce software: si rigenera documentazione e si verifica che sia pubblicabile. La sequenza va rispettata nell'ordine indicato, perche' ogni passo assume l'esito del precedente.

## Prerequisiti

Python 3 sul PATH e il pacchetto `python-docx` installato, piu' `Pillow` se si rigenerano le copie ridotte delle fotografie. Il documento sorgente presente in `_notes/sorgenti/`, dove e' stato archiviato il 25/08/2026 insieme al resto del materiale grezzo: senza di esso il convertitore non ha nulla da leggere e l'albero `docs/` resta all'ultima versione generata. Il file `tools/redactions.json` presente: senza di esso la conversione gira ugualmente ma produce un albero con i valori reali in chiaro, che non va assolutamente committato. Il file `_notes/.anonymization-patterns.json` presente: senza di esso il guard-rail si ferma con codice 2 invece di dare un verde non calcolato.

Nessuno dei due file privati e' nel repository, per costruzione. Su una macchina nuova vanno ricostruiti a partire da `_notes/.anonymization-map.md`, che a sua volta non e' versionato: in pratica un clone del repository puo' leggere la documentazione ma non puo' rigenerarla anonimizzata senza il materiale privato dell'autore. E' una conseguenza voluta.

## Rigenerare l'albero della documentazione

```powershell
python tools/docx-to-md.py "_notes/sorgenti/PROGETTO rete e networking domestica.docx" --out docs --clean
```

```bash
python tools/docx-to-md.py "_notes/sorgenti/PROGETTO rete e networking domestica.docx" --out docs --clean
```

Il comando e' idempotente e sovrascrive i file che produce. L'opzione `--clean` rimuove il rumore ereditato dal sorgente, cioe' emoji, trattini lunghi normalizzati in trattini brevi e righe segnaposto composte da una sola lettera ripetuta; senza quell'opzione la conversione e' strettamente verbatim.

Attenzione a un punto che puo' costare lavoro. Il convertitore non svuota la cartella di destinazione, quindi i documenti curati che vivono in `docs/` sopravvivono. Cio' che non sopravvive a un cambio di titolo nel sorgente e' il file generato con il vecchio slug, che resta orfano accanto al nuovo. Quando si rigenera dopo aver rinominato una sezione si cancellano le sole cartelle numerate e il `README.md` di radice, mai l'intera cartella `docs/`, perche' li' dentro vivono anche `DEVELOPMENT.md`, `pendenze-aperte.md`, `fonti-e-materiali.md`, `alternative-privacy-oriented.md` e `verbale-installazione-opnsense.md`.

## Verificare l'esito della conversione

Il file `docs/_CONVERSION-REPORT.md` riporta i conteggi di ogni corsa. I due numeri da guardare sono il rapporto fra titoli scritti e titoli nel sorgente, che deve essere pari, e il totale delle sostituzioni di redazione, che deve restare stabile o crescere. Un calo improvviso delle sostituzioni significa quasi sempre che una regola ha smesso di trovare riscontri perche' il testo sorgente e' cambiato, e quindi che un valore reale potrebbe essere passato in una forma diversa.

Il report elenca anche le sezioni marcate dall'autore e la mappa completa delle immagini estratte, che sono la base con cui si aggiorna `docs/pendenze-aperte.md`.

## Normalizzare i file Markdown scritti a mano

```powershell
python tools/md-unwrap.py .
```

```bash
python tools/md-unwrap.py .
```

Attua la convenzione di un paragrafo per riga sorgente descritta in `interaction-style.md`. Lo strumento rifiuta di scrivere un file il cui rendering cambierebbe, quindi e' sicuro da lanciare sull'intero albero. La verifica non distruttiva, adatta a un controllo prima del commit, esce con codice diverso da zero se qualcosa non rispetta la convenzione.

```powershell
python tools/md-unwrap.py --check .
```

```bash
python tools/md-unwrap.py --check .
```

## Controllare i comandi dentro i blocchi di codice

```powershell
python tools/lint-md-commands.py .
```

```bash
python tools/lint-md-commands.py .
```

Esiste perche' lo strumento precedente per contratto non tocca il contenuto dei blocchi recintati, quindi un comando spezzato su piu' righe dentro un blocco di codice non lo corregge nessuno. Il linter e' in sola lettura ed esce 0 se non trova niente.

## Il guard-rail di anonimizzazione, prima di ogni commit

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

Si modifica il documento sorgente, si rigenera l'albero, si legge il report, si normalizzano i Markdown, si controllano i blocchi di comando, si aggiunge all'indice, si esegue il guard-rail, si committa e si pusha. Le ultime due operazioni sono manuali dell'utente e l'agente non le esegue.

## Non c'e' distribuzione

Non esiste un deploy: non c'e' un sito, non c'e' un pacchetto, non c'e' un servizio. La pubblicazione coincide con il push su GitHub, ed e' per questo che il guard-rail e' l'ultima cosa che gira prima di essa. Se un giorno la documentazione venisse pubblicata come sito statico, quella sarebbe una nuova procedura da aggiungere qui, e il guard-rail resterebbe comunque il passo che la precede.
