# home-lab-cybersec-networking

> Istruzioni di progetto, versionate. Indice dei satelliti e procedura di ripresa. Le preferenze personali vivono in `CLAUDE.local.md`, ignorato da git, non qui.

## Cos'e' questo progetto

La progettazione documentata di una rete domestica segmentata con firewall dedicato, monitoraggio di sicurezza e servizi self-hosted, costruita sopra una linea in fibra il cui operatore non consente di sostituire il proprio modem. Il repository non contiene il software del lab: contiene la sua documentazione e gli strumenti che la producono e la verificano.

La documentazione ha due layer. Uno generato, l'albero `docs/`, prodotto in modo deterministico dal documento Word sorgente e mai modificato a mano. Uno curato, scritto a mano, composto dai documenti trasversali dentro `docs/`, dalle schede sotto `.claude/context/` e dalla memoria sotto `.claude/memory/`.

## Avvertenza sullo stato reale

Quasi tutto cio' che si legge e' progettazione, non stato di fatto. Di realizzato c'e' l'installazione del sistema operativo del firewall del 16/01/2026, senza configurazione di rete, e l'indirizzo pubblico statico ottenuto dall'operatore. Lo switch non e' acquistato, gli access point non esistono, nessun servizio interno e' in esercizio. Trattare le schede tecniche come descrizione di un sistema funzionante e' l'errore piu' facile da fare su questo repository.

## Procedura di ripresa in una sessione nuova

Leggere per primo `.claude/memory/index.md`, che fotografa branch, commit di riferimento, stato delle schede e punto di ripresa. Leggere poi `.claude/context/current-work.md` se c'e' una feature attiva. Invocare la skill `sync-context` per verificare il disallineamento fra schede e stato del repository. Leggere solo le schede pertinenti al task, mai tutte insieme.

Per orientarsi nella documentazione tecnica si parte da `docs/DEVELOPMENT.md`, che e' l'hub scritto a mano, e da `docs/pendenze-aperte.md`, che dice che cosa e' dichiarato incompleto. Per il documento sorgente, che e' voluminoso, vale la disclosure progressiva descritta in `token-economy.md`: si parte dallo scheletro, si scende nelle sezioni pertinenti, e si legge una sezione intera solo per rispondere a una domanda precisa. Gli estratti temporanei stanno sotto `_notes/.tmp-doc-progetto-rete/`.

## Il repository e' gia' su un remoto pubblico

Il remoto `origin` e' collegato e la storia e' gia' pushata: non c'e' una finestra in cui correggere prima della pubblicazione, c'e' solo il commit successivo. E' la cosa che vincola di piu' il modo di lavorare. Prima di ogni commit che tocchi documentazione va eseguito `python scripts/Test-Anonymization.py`, che passa tutti i file tracciati e fallisce se trova valori reali; quando il commit introduce file nuovi si aggiunge `--includi-nuovi`, altrimenti l'esito e' verde su un insieme che non comprende cio' che si sta per pubblicare. La regola completa e' `.claude/rules/anonymization.md`, da caricare sempre. Le due cose da non fare mai: scrivere un valore reale in un file tracciato, e citare in un file tracciato la corrispondenza fra un segnaposto e il suo valore, che renderebbe reversibile ogni anonimizzazione fatta altrove.

## Come si rigenera la documentazione

```powershell
python tools/docx-to-md.py "PROGETTO rete e networking domestica.docx" --out docs --clean
```

```bash
python tools/docx-to-md.py "PROGETTO rete e networking domestica.docx" --out docs --clean
```

Il convertitore sovrascrive i file che produce ma non svuota la cartella, quindi i documenti curati dentro `docs/` sopravvivono. Se si sono rinominate sezioni nel sorgente vanno cancellate prima le sole cartelle numerate e il `README.md` di radice, mai l'intera cartella `docs/`. La procedura completa, con i controlli che la seguono, e' in `.claude/context/deployment.md`.

Un file generato non si corregge mai a mano: la correzione sparirebbe alla rigenerazione successiva. Si corregge il documento sorgente, oppure si aggiunge un banner in `tools/annotations.json`, oppure una sostituzione in `tools/redactions.json` se si tratta di anonimizzazione.

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
.claude/context/deployment.md                  rigenerazione della documentazione e controlli
.claude/context/dev-testing.md                 che cosa i controlli garantiscono e che cosa no
.claude/context/current-work.md                feature attiva e definizione di fatto
.claude/context/roadmap.md                     fasi in ordine di dipendenza
.claude/context/diagrams/topologia-di-rete.md  catena WAN, tre zone, piano di indirizzamento
.claude/context/diagrams/monitoraggio-open-source.md  flusso SIEM e percorso di analisi
```

Documentazione, sotto `docs/`. Le sei cartelle numerate sono generate, i cinque file elencati sono scritti a mano.

```
docs/DEVELOPMENT.md                     hub di navigazione, da leggere per primo
docs/pendenze-aperte.md                 cio' che e' dichiarato incompleto, cinquanta voci
docs/verbale-installazione-opnsense.md  che cosa e' stato realmente fatto il 16/01/2026
docs/fonti-e-materiali.md               inventario delle fonti, versionate e non
docs/alternative-privacy-oriented.md    che cosa si vorrebbe self-hostare, e perche'
docs/_CONVERSION-REPORT.md              conteggi dell'ultima generazione
```

Regole modulari, sotto `.claude/rules/`.

```
.claude/rules/interaction-style.md      stile di documentazione e di risposta (caricare sempre)
.claude/rules/anonymization.md          segnaposto e guard-rail, repo pubblico (caricare sempre)
.claude/rules/token-economy.md          pratiche di risparmio di contesto (caricare sempre)
.claude/rules/git-commands-format.md    formato dei comandi git consegnati all'utente
.claude/rules/git-identity-and-repo.md  profili SSH, identita' git, bootstrap del remoto
.claude/rules/manual-screenshots.md     flusso di cattura screenshot per verifica visiva
.claude/rules/security-permissions.md   modalita' di permesso, sandbox, sessioni autonome
```

Strumenti, sotto `tools/` e `scripts/`.

```
tools/docx-to-md.py           genera l'albero docs/ dal documento sorgente
tools/annotations.json        banner curati iniettati nei file generati
tools/redactions.json         sostituzioni di anonimizzazione (privato, non versionato)
tools/md-unwrap.py            attua la convenzione di un paragrafo per riga sorgente
tools/lint-md-commands.py     segnala comandi di shell spezzati dentro i blocchi di codice
scripts/Test-Anonymization.py guard-rail sui file tracciati, prima di ogni commit
```

Skill richiamabili, sotto `.claude/skills/`.

```
.claude/skills/sync-context/   verifica disallineamento fra schede e repository
.claude/skills/repo-status/    riepilogo branch, commit recenti, diff non committato
.claude/skills/git-sync/       aggiorna il contesto dopo un pull o un merge
```

## Materiali e dati locali

Il materiale scritto a mano vive alla radice ed e' escluso dal versionamento per tipo di file: il documento Word sorgente, le fotografie della sessione di installazione, il whitepaper del firewall, l'output diagnostico, i due file di appunti e i due collegamenti. L'inventario completo, con l'indicazione di dove il loro contenuto e' confluito, e' in `docs/fonti-e-materiali.md`. La cartella `_notes/` raccoglie estratti temporanei e materiale privato, ed e' ignorata.

## Vincoli di team

Le operazioni di `git add`, commit e push restano sempre manuali dell'utente: l'agente prepara i file e propone i comandi, non committa. I comandi si consegnano nel formato definito da `git-commands-format.md`, cioe' un comando per riga, mai spezzato, in due blocchi separati per PowerShell e per bash. L'identita' git e' locale al repository, profilo personale, secondo `git-identity-and-repo.md`. Lo standard di sistema completo e' in `.claude/PROJECT-SYSTEM.md`.
