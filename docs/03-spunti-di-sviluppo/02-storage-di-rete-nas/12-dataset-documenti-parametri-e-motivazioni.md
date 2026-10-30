# Dataset documenti: parametri, motivazioni e punto di ripresa

Fotografia del modulo e del risultato del29/10/2026. Le immagini sono archiviate nel livello privato con verifica SHA-256. Alle11:18 tank/documenti è creato, cifrato e Unlocked, ancora Not Shared. Le sezioni del modulo conservano le letture preparatorie; il riscontro finale qui sotto distingue proprietà applicate e campi ancora da verificare.

## Scopo e scelte

Il primo dataset proposto è `tank/documenti`, con preset SMB, per separare documenti, accessi e future copie dagli altri impieghi del pool. L’utente ha scelto esplicitamente la cifratura con chiave automatica consigliata. La scelta è acquisita: non va chiesta nuovamente. Creazione cifrata nella GUI osservata; chiave JSON e terzo export della configurazione con seed post-dataset acquisiti e verificati fuori NAS. ACL Type SMB/NFSv4 e ACL Mode Restricted ora letti nel modulo identificato di documenti; accessi e condivisione restano da configurare.

La lettura iniziale mostrava Name vuoto e preset Generic; il successivo controllo del29/10 alle11:12 conferma Parent Path tank, Name `documenti` e Dataset Preset SMB. Create SMB Share è selezionato e SMB Name vale `documenti`. Prima di salvare si toglie Create SMB Share: il modulo creerà il solo dataset, mentre utente, ACL finale e condivisione saranno preparati nei passi successivi. Nessun clic Save o risultato di creazione è ancora osservato.

## Quote, prenotazioni e avvisi

Le due colonne visibili si chiamano This Dataset e This Dataset and Child Datasets. Nella tabella vuoto significa nessun importo digitato nel modulo; non descrive una partizione né riserva tutto il pool.

| Campo | This Dataset | This Dataset and Child Datasets | Motivazione e conseguenza |
|---|---|---|---|
| Quota | vuoto | vuoto | nessun limite numerico inserito ora; si dimensiona sul contenuto e sulle copie reali |
| Quota warning alert | 80%, Inherit selezionato | 80%, Inherit selezionato | soglia percentuale di avviso, distinta dal limite in byte |
| Quota critical alert | 95%, Inherit selezionato | 95%, Inherit selezionato | soglia critica, non spazio aggiunto né prenotato |
| Reserved space | vuoto | vuoto | nessuna prenotazione numerica inserita; lascia flessibile lo spazio condiviso |

In termini ZFS, refquota limita lo spazio del dataset senza includere discendenti e snapshot; quota considera l’albero e il relativo consumo. Refreservation e reservation garantiscono spazio con ambiti differenti. Le soglie percentuali del modulo non costituiscono da sole una quota. Questi limiti sono rivedibili quando crescono dischi e contenuti, ADR-044; il tetto iniziale proposto nel piano backup non è una quota già applicata. Riferimenti S159 e S249.

## Cifratura e recupero

| Campo | Osservato nel modulo | Scelta successiva già autorizzata |
|---|---|---|
| Encryption Options | Inherit (non-encrypted) deselezionato | lasciare così: cifratura indipendente dalla radice |
| Encryption | selezionato | mantenere per il solo dataset figlio |
| Encryption Type | Key | mantenere |
| Generate Key | selezionato | mantenere la generazione automatica della chiave |
| Algorithm | AES-256-GCM | mantenere |

La radice tank resta non cifrata. Una chiave conservata dal sistema favorisce l’avvio automatico; protegge la lettura dei soli dischi dati rimossi senza chiave, mentre non garantisce protezione dal furto dell’intero NAS con il materiale di sblocco. La passphrase manuale avrebbe un diverso costo operativo, già valutato nella scelta dell’utente. Non occorre riaprire il confronto per proseguire.

S247 descrive la creazione del figlio cifrato sotto una radice non cifrata. La cifratura non si aggiunge in seguito a un dataset non cifrato già creato: quel cambio richiede un nuovo dataset e migrazione. Dopo la creazione occorre esportare la chiave nel livello privato, conservarla fuori NAS e aggiornare l’export con Password Secret Seed. S137 distingue le chiavi dei dataset recuperabili con il seed dalle passphrase, che non sono incluse. Non si pubblicano chiavi, seed o archivi nel repository. Una copia sullo stesso client non dimostra ancora una seconda destinazione indipendente né un restore riuscito.

## Proprietà dei file e dello spazio

| Campo | Valore letto | Indicazione attuale e significato |
|---|---|---|
| Comments | vuoto | facoltativo; nessun commento applicato |
| Sync | Inherit (STANDARD) | mantenere; rispetta le richieste sincrone, senza forzare tutte le scritture a sincrone o disabilitarle |
| Compression Level | Inherit (LZ4) | mantenere; compressione trasparente già scelta sulla radice, risparmio dipendente dai file |
| Enable Atime | Inherit (OFF) | mantenere; evita l’aggiornamento dell’ora di accesso a ogni lettura |
| ZFS Deduplication | Inherit (OFF) | mantenere; nessun bisogno misurato che giustifichi deduplicazione e relativo costo |
| Case Sensitivity | Insensitive, campo bloccato | comportamento previsto per SMB; nome del file confrontato senza distinguere maiuscole/minuscole, scelta da fissare prima della creazione |
| Checksum | Inherit (ON) | mantenere; controllo d’integrità, che non sostituisce la copia esterna |
| Read-only | Inherit (OFF) | mantenere; il dataset potrà essere scritto dagli utenti autorizzati |
| Exec | Inherit (ON) | mantenere il default; non conferisce credenziali e non costituisce un’autorizzazione amministrativa |
| Snapshot Directory | Invisible nel modulo Edit identificato | mantenere; chiusa la precedente lettura non esplicita `--` |
| Snapdev | Inherit (HIDDEN) | mantenere; riguarda i dispositivi degli snapshot dei volumi, distinto dalla directory filesystem `.zfs` |
| Copies | 1 | mantenere; copie logiche aggiuntive del dataset, indipendenti dalla ridondanza del mirror a due SSD |
| Record Size | Inherit (128 KiB) | mantenere per i documenti; niente tuning da database senza quel carico |
| Metadata (Special) Small Block Size | Inherit (0) | mantenere; nessun invio dei piccoli blocchi a un dispositivo special configurato da questo campo |

Le proprietà ereditate seguono la radice finché non viene impostato un valore locale. Ereditare non significa assenza di configurazione: significa che l’origine è un antenato. Il riferimento dei campi è S248; S249 chiarisce in particolare Copies, quote, Sync e la differenza fra snapdir e snapdev. L’implementazione ACL va letta nella documentazione TrueNAS, senza trasferire automaticamente ogni limite di piattaforma del manuale OpenZFS generico.

## ACL e accesso SMB

| Campo | Osservato | Indicazione prima di salvare |
|---|---|---|
| ACL Type | SMB/NFSv4 nel modulo Edit identificato | già corretto, nessun cambio |
| ACL Mode | Restricted nel modulo Edit identificato | già corretto; è una modalità di gestione delle ACL, non l’elenco dei permessi finali |

La radice è distinta dal figlio di condivisione. Lasciare ACL Type Inherit senza verificarne l’origine potrebbe trasferire il tipo della radice invece del tipo voluto. NFSv4 è il tipo indicato da TrueNAS per SMB, S245/S248. Restricted limita certe modifiche ai permessi mediante chmod in presenza di ACL articolate; non significa che l’utente corretto abbia già accesso ai documenti. Utente, gruppo, ACL finale e condivisione saranno passaggi successivi, con prova di lettura/scrittura dal client. Non si cambiano i permessi della radice tank per preparare questo figlio.

## Stato verificato e sequenza successiva

Il controllo delle11:12 chiude la lettura di nome/preset e cifratura: documenti, SMB, Key, Generate Key e AES-256-GCM sono nel modulo. Quote visibili ancora vuote, Comments vuoto, Sync Inherit(STANDARD) e Compression Inherit(LZ4); tank sullo sfondo12.57MiB usati e213.18GiB disponibili, Unencrypted. ACL Type e Mode non sono inquadrati nelle nuove immagini: ultimo riscontro Inherit/Restricted. Il passo assegnato è togliere Create SMB Share nella parte superiore, scendere in fondo e scegliere ACL Type NFSv4 mantenendo Mode Restricted, quindi premere Save. Si legge il risultato o l’eventuale dialogo successivo prima di dichiarare creato il dataset o acquisita una chiave. Non occorre un altro controllo degli stessi campi prima di questo passaggio.

Dopo la creazione si registra l’esito nella pagina Datasets, si esporta la chiave, si acquisisce una nuova generazione della configurazione e si preparano accessi e condivisione. Non occorre ripetere i test hardware per questa navigazione. I due export già verificati conservano le tappe precedenti; non coprono un dataset ancora non salvato.

Il [registro del banco](09-registro-del-montaggio.md) conserva la cronologia; la [scheda didattica07](../../../.claude/context/refactor-07-pool-dataset-e-cifratura.md) spiega perché cifratura, permessi, mirror e backup rispondono a bisogni diversi. La [guida alla crescita](11-crescita-del-nas-e-indipendenza-dall-hardware.md) mantiene separate queste scelte dalle taglie dei componenti.

## Ultimo riscontro e checklist unica prima del Save

Alle11:14 Create SMB Share è deselezionato, come richiesto, e il campo SMB Name non compare più. Quote e riserve vuote, soglie80/95 ereditate in entrambe le colonne confermate. L’utente chiede una sola istruzione con tutti i parametri per evitare la scadenza della sessione: nessun altro screenshot intermedio richiesto prima del Save.

- Parent tank; Name documenti; preset SMB; Create SMB Share disattivato.
- Quote e Reserved space vuoti in entrambe le colonne; warning80% e critical95% con Inherit selezionato.
- Encryption: Inherit(non-encrypted) disattivato, Encryption attivo, Type Key, Generate Key attivo, Algorithm AES-256-GCM.
- Comments vuoto; Sync Inherit(STANDARD), Compression Inherit(LZ4), Atime Inherit(OFF), Dedup Inherit(OFF), Case Sensitivity Insensitive, Checksum Inherit(ON), Read-only Inherit(OFF), Exec Inherit(ON).
- Snapshot Directory lasciare --; Snapdev Inherit(HIDDEN); Copies1; Record Size Inherit(128KiB); Metadata(Special)Small Block Size Inherit(0).
- ACL Type NFSv4; ACL Mode Restricted. Poi Save e leggere la schermata ottenuta.

Questa checklist è l’istruzione assegnata, non un’attestazione di salvataggio o di proprietà del dataset già creato. Chiave esterna e nuovo export seguiranno l’esito di creazione.

## Creazione riuscita e recupero della nuova tappa

Creazione osservata alle11:18: selezione documenti e messaggio Switched to new dataset. Dataset cifrato Unlocked, Usage Not Shared, Path tank/documenti. Used192KiB e Available213.17GiB; Total Allocation192KiB e Data Written192KiB(100%). SyncSTANDARD, Compression Inherit(1.00x(LZ4)), AtimeOFF, DedupOFF e CaseSensitivityOFF. UserQuotasNone. Per questa selezione Snapshots0,SnapshotTasks0,NoBackupTasks: nessuna attività dati ancora configurata. Radice tank Unencrypted,12.93MiB usati/213.17GiB disponibili. Owner root:root, pannello NFSv4 con tre ACE visibili: owner@root AllowFullControl,group@root AllowModify,builtin_users AllowModify; parte inferiore tagliata, non è una trascrizione completa delle ACL.

Prima del risultato compare ACL Types & ACL Modes, avviso generale sulla conversione delle ACL. L’anteprima sottostante mostra ACL Type SMB/NFSv4 e ACL Mode Passthrough. La dashboard successiva conferma NFSv4 ma non espone ACL Mode: non si dichiara Restricted applicato. Il valore finale va letto nella modifica delle proprietà prima di completare i permessi e la share; non si ricrea il dataset né si riaprono test hardware. Non occorre una snapshot preventiva per una migrazione di dati esistenti che questa creazione nuova non sta eseguendo.

Prossimo passo: mantenere documenti selezionato, scorrere nel pannello destro fino al riquadro Encryption e premere Export Key. S248 conferma che scarica un JSON; il file va acquisito nel livello privato senza trascrivere la chiave nei documenti o nella chat. S247 descrive la custodia esterna. Serve inoltre una nuova generazione dell’export con Password Secret Seed, conservando le due precedenti. Due copie sullo stesso client non chiudono la destinazione indipendente o il ripristino. Nessuna chiave esterna o nuovo export post-dataset è già acquisito.

## Acquisizione della chiave conclusa

Registrato 2026-10-29T11:46:22+01:00. Chiave di tank/documenti acquisita dal file indicato dall’utente:86byte, originale conservato e copia privata ignorata da git, impronte SHA-256 uguali. JSON valido per il solo dataset atteso, chiave in formato esadecimale256bit; nessun valore stampato o trascritto nei documenti pubblici. Acquisizione della chiave fuori NAS conclusa. Download e archivio sono sullo stesso client: destinazione indipendente e prova di sblocco/ripristino ancora aperti. Nessuna dimostrazione del valore finale ACL Mode da questa lettura del file.

Prossimo System > Advanced Settings > Manage Configuration > Download File; selezionare Export Password Secret Seed e Save. Il nuovo archivio post-dataset è ancora da acquisire, mantenendo entrambi gli export del28/10. S137 riletto e conferma percorso e opzione; key export e configurazione restano materiali distinti. Nessuna nuova mail, test hardware o modifica al filone assistente/Jev.

## Terzo export verificato, prossimo controllo ACL Mode

Registrato 2026-10-29T11:53:05+01:00. Terzo export TrueNAS25.10.7 post-dataset acquisito:849920byte, copia privata ignorata identica al download per SHA-256, originale conservato. SQLite835584byte letto soltanto in memoria supera quick_check; seed32byte presente e coerente con la precedente. Quindici controlli di checkpoint tutti positivi: record tank/documenti univoco con campo chiave non vuoto e gestione locale, assente nell’export post-pool; pool/GUID invariati; share documenti non creata nel database; mittente/nome e recapito amministratore coerenti, OAuth presente, Europe/Rome e System Dataset Pool tank. Archivio differente da entrambe le generazioni precedenti, che restano conservate. Chiave JSON separata già acquisita e riletta per impronta. Nessun valore segreto stampato, nessun database o seed estratti su file. Il campo chiave del database non è stato decifrato o confrontato in valore con il JSON: la verifica non prova uno sblocco o restore.

Acquisizione dell’export di questa tappa conclusa. Download, archivio e chiave sono sul medesimo client: seconda destinazione indipendente, inclusione Veeam e recupero restano aperti. ACL Mode non è dimostrato dai controlli del database: ultima anteprima Passthrough, valore finale ancora da leggere. Prossimo Datasets > documenti > Edit nel riquadro Details > Advanced Options, scorrere fino a ACL Type/ACL Mode e leggere i valori; poi utente, permessi e condivisione. Nessun altro export identico o test hardware richiesto.

## Lettura del pannello: verificare quale dataset è aperto

Registrato 2026-10-29T12:11:38+01:00. Edit Dataset mostra Snapshot Directory Invisible, SnapdevHidden, Copies1, RecordSize128K, ACL Type POSIX e ACL Mode Discard entrambi disabilitati, SpecialSmallBlocks0. Il nome/percorso del dataset è fuori inquadratura; il riscontro è compatibile con tank radice (S248), non una prova di regressione del figlio documenti già mostrato NFSv4. Prossimo chiudere il pannello con X, selezionare la riga documenti e verificare Details for documenti prima di Edit/Advanced Options e lettura ACL Type/Mode. Nessun Save o cambiamento dei permessi osservati; nessun nuovo export richiesto per questa sola lettura. tank sullo sfondo13.08MiB/213.17GiB, documenti192KiB/213.17GiB Unlocked.

## Documento identificato: tutte le proprietà corrette

Registrato 2026-10-29T12:21:49+01:00. Tre immagini archiviate prima della lettura, SHA-256 verificati e originali conservati. Il modulo Edit Dataset mostra Name tank/documenti bloccato: identità ora verificata. Valori letti: Comments vuoto; Sync Inherit(STANDARD); Compression Inherit(LZ4); Atime Inherit(OFF); Dedup Inherit(OFF); Case Sensitivity Insensitive bloccato; Checksum Inherit(ON); Read-only Inherit(OFF); Exec Inherit(ON); Snapshot Directory Invisible; Snapdev Inherit(HIDDEN); Copies1; Record Size Inherit(128KiB); ACL Type SMB/NFSv4; ACL Mode Restricted; Metadata(Special)Small Block Size Inherit(0). Save abilitato e Basic Options visibile. tank sullo sfondo13.16MiB/213.17GiB, documenti192KiB/213.17GiB Unlocked. Nessun campo richiede modifica.

Chiusa la lettura del tipo e della modalità ACL nel modulo identificato; i precedenti POSIX/Discard senza nome non sono proprietà accertate di documenti. Nessun nuovo Save osservato in queste immagini. Indicazione operativa: Save per confermare, poi Credentials > Users > Add e lettura del modulo utente; nessun utente, permesso finale o share ancora creati. Nessun nuovo export richiesto per una lettura senza cambi di configurazione. Tre export e chiave JSON restano acquisiti e verificati; copia indipendente e restore aperti.

Richiesta di stile ribadita dall’utente: in un solo messaggio indicare soltanto i settings che cambiano; tutti i valori, le ragioni e lo stato nel progetto. Qui i cambi necessari sono nessuno.
