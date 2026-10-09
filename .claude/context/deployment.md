---
generated-from-commit: 86b5c8a61a55a48997d7757592aa4d91da9e8581
generated-from-branch: main
generated-date: 2026-08-25
covers-paths:
  - tools/**
  - docs/**
last-verified-commit: ee63b19
---

# Esecuzione e manutenzione della documentazione

> Scheda tecnica. Descrive le procedure eseguibili di questo repository. Qui non si distribuisce software: si scrive documentazione e si verifica che sia coerente e pubblicabile. La sequenza va rispettata nell'ordine indicato, perché ogni passo assume l'esito del precedente.

## Il modello, dal 25/08/2026

L'albero `docs/` si scrive e si modifica a mano. Non si rigenera più dal documento Word, che è stato eliminato il 07/10/2026 dopo la verifica di ADR-019: `docs/` è l'unica fonte. Il razionale è in ADR-010; qui conta la conseguenza operativa, che è semplice: si apre una sessione, si modifica un file Markdown, si eseguono i controlli, si committa.

Il convertitore `tools/docx-to-md.py` resta nel repository come strumento che ha prodotto l'albero, ma non va eseguito su `docs/`. Non è una raccomandazione affidata alla memoria: il convertitore scrive nella destinazione un timbro `.generato-da-docx` e si rifiuta di scrivere in una cartella che contiene documenti senza quel timbro. Su `docs/` il timbro è stato rimosso, quindi una corsa accidentale si ferma con codice 2 e un messaggio che spiega perché. Resta utilizzabile su una destinazione nuova, per esempio se un giorno servisse convertire un altro documento.

## Prerequisiti

Python 3 sul PATH. Per i soli controlli non serve altro. Il pacchetto `python-docx` serve unicamente al convertitore, che ormai non si usa; `Pillow` serve solo se si rigenerano le copie ridotte delle fotografie.

Il file `_notes/.anonymization-patterns.json` deve esistere, altrimenti il guard-rail si ferma con codice 2 invece di dare un verde non calcolato. Non è nel repository per costruzione, e su una macchina nuova va ricostruito da `_notes/.anonymization-map.md`, anch'esso non versionato. In pratica un clone del repository può leggere e modificare la documentazione, ma non può verificarne l'anonimizzazione senza il materiale privato dell'autore. È una conseguenza voluta.

## Modificare la documentazione

Non c'è una procedura: si modifica il file. Contano tre regole, e sono tutte conseguenze del fatto che l'albero è navigabile e pubblico.

Un file nuovo va collegato dall'indice della sua cartella, altrimenti esiste ma nessuno lo trova. Un file spostato o rinominato lascia collegamenti rotti altrove, che vanno sistemati nello stesso commit. Un contenuto nuovo che contiene un valore reale va anonimizzato mentre lo si scrive, aggiungendo prima la voce alla mappa e al file dei pattern: il sidecar di redazione non gira più, quindi nessuno lo fa più al posto tuo.

I prefissi numerici di cartelle e file vengono dalla generazione iniziale e ora sono soltanto nomi stabili. Non si rinumerano per inserire qualcosa in mezzo: si usa il primo numero libero, anche se rompe l'ordine alfabetico, perché rinumerare significa rinominare file e rompere ogni collegamento che li citava.

## I controlli prima di ogni commit

Dall'8/10/2026 i controlli sono quelli che `chiudi` trova istanziati in `tools/` ed esegue tutti, fermandosi prima del commit se uno fallisce: `md-unwrap`, `lint-md-commands`, il guard-rail con il suo `--autotest`, `lint-doc-references --solo-vivi`, `check-eol`, `misura-istruzioni`, `verifica-schede`, i tre correttori tipografici in modalità di verifica e `sync-codex-skills --check`. L'agente li esegue con `chiudi -SoloControlli` prima di proporre un commit. Il controllo dell'albero resta fuori da `chiudi`, perché è proprio di questo progetto, e si lancia a parte. I quattro che seguono sono quelli storici del progetto, descritti uno per uno.

Il primo verifica che l'albero regga come struttura navigabile: nessun documento scollegato dagli indici, nessun collegamento relativo che punti a un percorso inesistente.

```powershell
python tools/check-docs-tree.py
```

```bash
python tools/check-docs-tree.py
```

Il secondo attua la convenzione di formattazione, cioè un paragrafo per riga sorgente. Lo strumento rifiuta di scrivere un file il cui rendering cambierebbe, quindi è sicuro da lanciare sull'intero albero; con `--check` non scrive e segnala soltanto. Lanciato su `.` percorre anche il materiale ignorato sotto `_notes/` e lì trova righe da unire, che non sono un difetto pubblicabile: l'opzione `--only-tracked` limita il controllo ai file tracciati, ed è la forma che usa `chiudi`. Dal 07/10/2026 quell'opzione salta i file tracciati ma cancellati nell'albero di lavoro, così un commit che rimuove un documento non si ferma più su questo controllo.

```powershell
python tools/md-unwrap.py --check .
```

```bash
python tools/md-unwrap.py --check .
```

Il terzo copre il punto cieco del secondo, che per contratto non entra nei blocchi recintati, e segnala i comandi di shell spezzati su più righe.

```powershell
python tools/lint-md-commands.py .
```

```bash
python tools/lint-md-commands.py .
```

Il quarto è quello che decide se il commit è pubblicabile.

```powershell
python tools/Test-Anonymization.py
```

```bash
python tools/Test-Anonymization.py
```

Passa tutti i file tracciati da git, e quelli nuovi non ancora aggiunti, ed esce con codice diverso da zero se trova riscontri nelle categorie bloccanti. Le categorie non bloccanti raccolgono ciò che va guardato da un umano, tipicamente indirizzi pubblici di transito e cifre che somigliano a importi. Va eseguito sull'intero albero e non sui soli file toccati.

Dal 08/10/2026 lo strumento è `tools/Test-Anonymization.py`, la versione del pacchetto del template con le estensioni di questo progetto (ADR-022): esamina per impostazione predefinita i file tracciati più quelli non tracciati e non ignorati, cioè tutto ciò che un `git add` porterebbe dentro, quindi l'opzione `--includi-nuovi` della copia precedente non serve più e non esiste. Con `--autotest` prova i propri riconoscitori di IBAN e carte di pagamento, ed è la prova che `chiudi` esegue a ogni commit.

## La sequenza completa

Si modifica un file, si collega dall'indice se è nuovo, si esegue il controllo di coerenza, si normalizza la formattazione, si controllano i blocchi di comando, si aggiunge all'indice di git, si esegue il guard-rail, si committa e si pusha. Le ultime due operazioni sono manuali dell'utente e l'agente non le esegue.

Dal 07/10/2026 la via ordinaria per committare è `chiudi`, lanciato dall'utente nel proprio terminale con il messaggio che l'agente prepara in `_notes/COMMIT-MSG.txt`. Esegue i controlli istanziati del template, fra cui `md-unwrap --only-tracked`, `lint-md-commands` e il guard-rail con il suo autotest; si ferma prima del commit se uno fallisce. Non conosce `tools/check-docs-tree.py`, che è proprio di questo progetto: dopo uno spostamento o un file nuovo nell'albero quel controllo si lancia a mano prima di `chiudi`.

```bash
python tools/check-docs-tree.py && powershell -NoProfile -ExecutionPolicy Bypass -File tools/chiudi-sessione.ps1 -SoloControlli
```

Dopo il push `chiudi` registra l'impronta che `tools/verifica-ripresa.py` confronta all'apertura della sessione successiva, attraverso la skill `riprendi`.

## Rigenerare da un documento Word, se un giorno servisse

Non su `docs/`, che è protetto dal timbro. Su una destinazione nuova, per confrontare o per importare un documento diverso.

```powershell
python tools/docx-to-md.py "percorso/del/documento.docx" --out cartella-nuova --clean
```

```bash
python tools/docx-to-md.py "percorso/del/documento.docx" --out cartella-nuova --clean
```

L'opzione `--clean` rimuove il rumore ereditato dal sorgente, cioè emoji, trattini lunghi normalizzati in trattini brevi e righe segnaposto di corpo composte da una sola lettera ripetuta; senza quell'opzione la conversione è strettamente verbatim. Il report scritto nella destinazione riporta i conteggi, e il rapporto fra titoli scritti e titoli del sorgente deve risultare pari. Il sidecar `tools/redactions.json`, se presente, viene ancora applicato: su un documento nuovo con dati reali va aggiornato prima, non dopo.

## Non c'è distribuzione

Non esiste un deploy: non c'è un sito, non c'è un pacchetto, non c'è un servizio. La pubblicazione coincide con il push su GitHub, ed è per questo che il guard-rail è l'ultima cosa che gira prima di essa. Se un giorno la documentazione venisse pubblicata come sito statico, quella sarebbe una nuova procedura da aggiungere qui, e il guard-rail resterebbe comunque il passo che la precede.
