# home-lab-cybersec-networking

> Istruzioni di progetto, versionate. Indice dei satelliti e procedura di ripresa. Le preferenze personali vivono in `CLAUDE.local.md`, ignorato da git, non qui.

## Cos'è questo progetto

La progettazione documentata di una rete domestica segmentata con firewall dedicato, monitoraggio di sicurezza e servizi self-hosted, costruita sopra una linea in fibra il cui operatore non consente di sostituire il proprio modem. Il repository non contiene il software del lab: contiene la sua documentazione e gli strumenti che la producono e la verificano.

La documentazione si scrive e si mantiene qui dentro, a mano, sessione dopo sessione. L'albero `docs/` è nato da una conversione deterministica di un documento Word, ma dal 25/08/2026 quel documento è un archivio e non una fonte: la continuità del lavoro sta nel repository, non altrove. Il razionale è in ADR-010.

## Avvertenza sullo stato reale

Quasi tutto ciò che si legge è progettazione, non stato di fatto. Di realizzato c'è l'installazione del sistema operativo del firewall del 16/01/2026, senza configurazione di rete, e l'indirizzo pubblico statico ottenuto dall'operatore. Lo switch non è acquistato, gli access point non esistono, nessun servizio interno è in esercizio. Trattare le schede tecniche come descrizione di un sistema funzionante è l'errore più facile da fare su questo repository.

## Procedura di ripresa in una sessione nuova

Leggere per primo `.claude/memory/index.md`, che fotografa branch, commit di riferimento, stato delle schede e punto di ripresa. Leggere poi `.claude/context/current-work.md` se c'è una feature attiva. Invocare la skill `sync-context` per verificare il disallineamento fra schede e stato del repository. Leggere solo le schede pertinenti al task, mai tutte insieme.

Per orientarsi nella documentazione tecnica si parte da `docs/README.md`, che è l'indice, e poi da `docs/DEVELOPMENT.md`, che propone i percorsi di lettura per argomento, e da `docs/pendenze-aperte.md`, che dice che cosa è dichiarato incompleto. L'albero è fatto di file piccoli per sezione: si legge quello pertinente al task, non l'area intera.

## Il repository è già su un remoto pubblico

Il remoto `origin` è collegato e la storia è già pushata: non c'è una finestra in cui correggere prima della pubblicazione, c'è solo il commit successivo. È la cosa che vincola di più il modo di lavorare. Prima di ogni commit che tocchi documentazione va eseguito `python tools/Test-Anonymization.py`, che passa tutti i file tracciati e quelli nuovi non ancora aggiunti, e fallisce se trova valori reali. La regola completa è `.claude/rules/anonymization.md`, da caricare sempre. Le due cose da non fare mai: scrivere un valore reale in un file tracciato, e citare in un file tracciato la corrispondenza fra un segnaposto e il suo valore, che renderebbe reversibile ogni anonimizzazione fatta altrove.

## Come si modifica la documentazione

Si modifica il file, direttamente. Non c'è generazione, non c'è un sorgente altrove da tenere allineato, e il convertitore non va eseguito su `docs/`: è protetto da un timbro e si rifiuta di sovrascrivere.

Tre regole, tutte conseguenza del fatto che l'albero è navigabile e pubblico. Un file nuovo va collegato dall'indice della sua cartella. Un file rinominato o spostato lascia collegamenti rotti, che vanno sistemati nello stesso commit. Un valore reale va anonimizzato mentre lo si scrive, aggiungendolo prima alla mappa e al file dei pattern, perché nessuna sostituzione automatica gira più al posto tuo.

I prefissi numerici di cartelle e file sono nomi stabili ereditati dalla generazione iniziale: per inserire qualcosa si usa il primo numero libero, non si rinumera.

Prima di ogni commit si lancia il controllo dell'albero, che è proprio di questo progetto, e poi `chiudi`, che trova da solo ed esegue i dodici controlli istanziati dal template: formattazione, comandi, guard-rail con il suo autotest, riferimenti, fine riga, carico delle istruzioni, schede, accenti, trattini, accenti mancanti e adattatori Codex. L'agente li esegue prima di proporre il commit con `chiudi -SoloControlli`. Il dettaglio è in `.claude/context/deployment.md`.

```bash
python tools/check-docs-tree.py && powershell -NoProfile -ExecutionPolicy Bypass -File tools/chiudi-sessione.ps1 -SoloControlli
```

## Indice dei file satellite tracciati

Memoria e meta-stato, sotto `.claude/memory/`, letti a inizio sessione.

```
.claude/memory/index.md       snapshot e tabella di sincronizzazione, da leggere per primo
.claude/memory/progress.md    work-log append-only di passi e riconciliazioni
.claude/memory/decisions.md   registro ADR-lite delle decisioni architetturali
```

Schede tecniche, sotto `.claude/context/`, con frontmatter di riconciliazione.

```
.claude/context/STACK.md                       stack del repository e stack del lab, tenuti distinti
.claude/context/design-and-security.md         zone, contratto fra zone, sicurezza del repository
.claude/context/deployment.md                  manutenzione della documentazione e i controlli prima del commit
.claude/context/dev-testing.md                 che cosa i controlli garantiscono e che cosa no
.claude/context/current-work.md                feature attiva e definizione di fatto
.claude/context/roadmap.md                     fasi in ordine di dipendenza
.claude/context/diagrams/topologia-di-rete.md  catena WAN, tre zone, piano di indirizzamento
.claude/context/diagrams/monitoraggio-open-source.md  flusso SIEM e percorso di analisi
```

Documentazione, sotto `docs/`. Le sei cartelle numerate raccolgono il contenuto per area, i file elencati sono trasversali. Tutto è scritto a mano.

```
docs/README.md                          indice dell'albero, punto di ingresso
docs/DEVELOPMENT.md                     percorsi di lettura per argomento
docs/pendenze-aperte.md                 cio' che e' dichiarato incompleto, cinquanta voci
docs/verbale-installazione-opnsense.md  che cosa e' stato realmente fatto il 16/01/2026
docs/fonti-e-materiali.md               inventario delle fonti, versionate e non
docs/alternative-privacy-oriented.md    che cosa si vorrebbe self-hostare, e perche'
docs/_CONVERSION-REPORT.md              conteggi della conversione iniziale, storico
```

Regole modulari, sotto `.claude/rules/`.

```
.claude/rules/interaction-style.md      stile di documentazione e di risposta (caricare sempre)
.claude/rules/anonymization.md          segnaposto e guard-rail, repo pubblico (caricare sempre)
.claude/rules/token-economy.md          pratiche di risparmio di contesto (caricare sempre)
.claude/rules/chat-non-e-memoria.md     persistenza su disco a ogni giro e recap a campi fissi (caricare sempre)
.claude/rules/documenti-personali.md    documenti personali mai letti senza richiesta espressa (caricare sempre)
.claude/rules/git-commands-format.md    formato dei comandi git consegnati all'utente
.claude/rules/manual-screenshots.md     flusso di cattura screenshot per verifica visiva
.claude/rules/security-permissions.md   modalita' di permesso, sandbox, sessioni autonome
```

Strumenti, sotto `tools/`. Quelli copiati dai pacchetti del template (ADR-022) li aggiorna `allinea-dal-template.py`; il guard-rail è una copia adattata, registrata in `.claude/allineamento-risolti.json`.

```
tools/check-docs-tree.py      orfani e collegamenti rotti nell'albero; proprio del progetto, fuori da chiudi
tools/md-unwrap.py            attua la convenzione di un paragrafo per riga sorgente
tools/lint-md-commands.py     segnala comandi di shell spezzati dentro i blocchi di codice
tools/Test-Anonymization.py   guard-rail sui file tracciati e nuovi, ultimo controllo prima del commit
tools/docx-to-md.py           archiviato: ha prodotto l'albero, non va eseguito su docs/
tools/annotations.json        storico: banner della generazione, ora testo dentro i file
tools/redactions.json         sostituzioni della prima stesura (privato, non versionato)
tools/chiudi-sessione.ps1     chiusura: controlli, commit, push, impronta di ripresa (anche .sh)
tools/verifica-ripresa.py     confronta l'impronta di chiusura con lo stato di git; skill riprendi
tools/verifica-schede.py      schede di contesto superate rispetto all'ancora; skill sync-context
tools/lint-doc-references.py  riferimenti a file inesistenti nei documenti vivi
tools/lint-md-tables.py       struttura delle tabelle Markdown
tools/check-eol.py            file con fine riga miste
tools/misura-istruzioni.py    carico delle istruzioni sempre attive rispetto alla soglia
tools/fix-accents.py          accenti scritti con l'apostrofo (con fix-missing-accents, fix-dashes)
tools/test-tipografia.py      prova della catena tipografica
tools/lint-prosa.py           segni del testo generato, avvisi da rileggere (guida in docs/anti-slop/)
tools/lint-ui.py              come sopra per le interfacce; istanziato perché la guida lo cita
tools/sync-codex-skills.py    adattatori .agents/skills per Codex
tools/latest-screenshot.ps1   screenshot più recente, per la regola manual-screenshots
tools/test-documenti-personali.py  prova della regola documenti-personali; gira solo nel template
tools/raccolta-dispositivo.ps1  raccolta in sola lettura di un PC Windows per la scheda dispositivo (anche .sh per Linux)
tools/scheda-da-raccolta.py   scheda dispositivo anonimizzata dalla raccolta, con autotest
```

Skill richiamabili, sotto `.claude/skills/`.

```
.claude/skills/sync-context/   verifica disallineamento fra schede e repository
.claude/skills/repo-status/    riepilogo branch, commit recenti, diff non committato
.claude/skills/git-sync/       aggiorna il contesto dopo un pull o un merge
```

## Materiali e dati locali

Il materiale grezzo vive in `_notes/sorgenti/`, ignorato da git. Dal 07/10/2026 (ADR-019) il documento Word, i due file di appunti, i due collegamenti e `quickprint.docx` sono eliminati dopo la verifica che `docs/` ne contenga tutto; restano le fotografie della sessione di installazione, lo schema del monitoraggio e il whitepaper del firewall; l'output diagnostico DxDiag è eliminato lo stesso giorno. L'inventario completo, con l'indicazione di dove il loro contenuto è confluito, è in `docs/fonti-e-materiali.md`. La cartella `_notes/` raccoglie estratti temporanei e materiale privato, ed è ignorata.

Norme caricate su richiesta, una riga per situazione con le parole con cui si presenta, così che il caricamento non dipenda dal ricordare che la norma esista.

- `git worktree list` mostra più di un albero, se ne crea o se ne rimuove uno, si deve decidere da dove leggere la memoria versionata: skill `alberi-di-lavoro`.
- Un recupero web fallisce con 403 o con una pagina di verifica anti-bot, la fonte sta su Reddit o su Discord, serve la trascrizione di un video, si sta per annotare una fonte non letta: skill `fonti-non-recuperabili`.
- Si scrive o si valuta una prova automatica, si chiude un difetto, una verifica manuale smentisce una suite verde, si sta per dichiarare completo un intervento il cui scopo era un effetto misurabile: skill `prove-che-misurano`.
- Si inizializza o si allinea il progetto, oppure cambia il modo in cui si prova e si rilascia, e va deciso come separare test e produzione: skill `separazione-ambienti`.
- Si imposta o si verifica user.name e user.email, si collega o si cambia il remoto o l'alias SSH, si inizializza un repository, un push fallisce per permessi, `/status` mostra un account Claude diverso da quello atteso, si autentica o si usa `gh`: skill `identita-git`.

## Vincoli di team

Le operazioni di `git add`, commit e push restano sempre manuali dell'utente: l'agente prepara i file e propone i comandi, non committa. I comandi si consegnano nel formato definito da `git-commands-format.md`, cioè un comando per riga, mai spezzato, in due blocchi separati per PowerShell e per bash. L'identità git è locale al repository, profilo personale, secondo la skill `identita-git`. Lo standard di sistema completo è in `.claude/PROJECT-SYSTEM.md`.
