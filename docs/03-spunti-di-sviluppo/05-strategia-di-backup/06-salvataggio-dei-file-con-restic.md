# Salvataggio e recupero dei file con restic

Questo è un percorso proposto per i file selezionati degli endpoint e per una copia distinta dei documenti NAS, collegato al [piano del laboratorio](02-piano-di-backup-e-ripristino-del-lab.md). Non risulta un repository restic installato o inizializzato nel lab. Il riferimento consultato il 19/10/2026 è la documentazione stabile 0.19.1; versione del programma e formato del repository andranno registrati all'installazione.

## Che cosa protegge questo percorso

Il recupero qui previsto riguarda file e metadati verificati. Non è una procedura per ricostruire automaticamente l'avvio di un computer o l'intero sistema operativo. Per un'immagine Windows si valuta il [percorso Veeam](01-veeam-agent-for-windows.md); per un guest si applicano le [procedure Proxmox](04-procedure-di-backup-e-ripristino.md). Non si sovrappongono due strumenti sullo stesso contenuto senza attribuire uno scopo e uno spazio a ciascuno.

Prima si compila in privato il perimetro: cartelle incluse, esclusioni, dimensioni, file aperti, requisiti di permesso e destinazione. Il salvataggio deve escludere la propria destinazione e gli altri repository di backup, salvo una copia fra repository espressamente progettata. Non si include tutto il profilo o tutto un disco per evitare il censimento. La scelta dei documenti personali da proteggere e la loro lettura richiedono una richiesta specifica dell'utente; questo progetto non ne ha aperti per definire il metodo.

La destinazione proposta per un endpoint è una propria share NAS con identità e quota separate. Per i documenti originali NAS, una share sullo stesso pool non costituisce la copia distinta: la proposta è spazio sul server, secondo NAS-03. Una cartella di sincronizzazione cloud non è automaticamente un repository remoto affidabile o una copia scollegata.

## Preparazione del repository

Si installa una versione verificata dallo sviluppo ufficiale e si conserva il materiale necessario al recupero anche fuori dall'endpoint. Si sceglie un repository nuovo, distinto dagli originali, e si verifica la destinazione prima di inizializzarlo. Per un repository già esistente si recuperano identità e segreto corretti, senza creare un altro repository per aggirare un errore di accesso.

La password del repository è necessaria per leggerne i dati e non sostituisce le credenziali di accesso allo storage. Nel primo collaudo si può inserirla al prompt; l'automazione futura userà un file protetto o un comando di accesso al gestore di segreti. Si conserva una copia di emergenza leggibile senza l'endpoint e senza il NAS. [Preparazione e credenziali](https://restic.readthedocs.io/en/stable/030_preparing_a_new_repo.html).

I comandi seguenti sono modelli da compilare nel futuro collaudo. Non sono stati lanciati su dati o repository dell'utente. I segnaposto sono quotati; non contengono password in chiaro. La directory di destinazione deve essere controllata prima di `init`.

```bash
restic -r '<REPOSITORY_NUOVO>' init
restic -r '<REPOSITORY>' --password-file '<FILE_PRIVATO_PASSWORD>' backup '<CARTELLA_DI_PROVA>'
```

Si parte da una cartella artificiale piccola, con file riconoscibili e impronte attese annotate prima del backup. Dopo il primo recupero riuscito, si misura l'insieme reale autorizzato e si ammette il job solo quando capacità e durata sono compatibili. Per una lettura SMB di file vivi si documenta il metodo per ottenere consistenza. Su Windows l'opzione `--use-fs-snapshot` usa VSS per i file interessati; non trasforma il backup file in un'immagine di avvio e richiede verifica dei privilegi e dell'ambiente. [Backup e VSS](https://restic.readthedocs.io/en/stable/040_backup.html).

## Esito del giro e registro dei punti riusciti

Si conserva l'ID del nuovo snapshot, insieme a origine logica, ora con fuso, byte aggiunti, byte elaborati, durata ed errori. Gli snapshot si elencano e il loro contenuto si ispeziona con riferimento a un ID esplicito; `latest` senza filtri può indicare il salvataggio di un altro oggetto presente nello stesso repository. [Elenco di snapshot e file](https://restic.readthedocs.io/en/stable/045_working_with_repos.html).

```bash
restic -r '<REPOSITORY>' --password-file '<FILE_PRIVATO_PASSWORD>' snapshots
restic -r '<REPOSITORY>' --password-file '<FILE_PRIVATO_PASSWORD>' ls '<ID_SNAPSHOT>'
```

Per il comando backup, exit 0 indica il salvataggio riuscito; exit 1 indica un errore fatale senza nuovo snapshot e exit 3 uno snapshot incompleto perché alcuni file non sono stati letti. L'automazione deve registrare gli ultimi due come esiti da risolvere e non avanzare la data del punto completo. Un nuovo ID non basta a dimostrare che il perimetro richiesto sia interamente leggibile. [Codici di uscita del backup](https://restic.readthedocs.io/en/stable/040_backup.html).

Un timer futuro deve evitare corse sovrapposte, gestire NAS assente e conservare un log anche fuori dalla destinazione. L'esecuzione mancata non si presenta come un backup riuscito con zero modifiche. Prima di collegare notifiche a sistemi esterni si sceglierà esplicitamente quel canale; al 19/10 non è configurato alcun invio.

## Recupero verso una cartella distinta

Si seleziona l'ID corretto, si controllano i percorsi tramite `ls` e si riserva spazio fuori dal repository e fuori dagli originali. Il primo recupero usa una cartella vuota di prova. La simulazione aiuta a controllare la selezione, ma non dimostra la lettura completa e la scrittura effettiva del recupero. Il successivo comando è un recupero reale da eseguire soltanto nel collaudo predisposto.

```bash
restic -r '<REPOSITORY>' --password-file '<FILE_PRIVATO_PASSWORD>' restore '<ID_SNAPSHOT>' --target '<CARTELLA_VUOTA_DI_PROVA>' --dry-run --verbose=2
restic -r '<REPOSITORY>' --password-file '<FILE_PRIVATO_PASSWORD>' restore '<ID_SNAPSHOT>' --target '<CARTELLA_VUOTA_DI_PROVA>'
```

Il recupero normale può sovrascrivere file già presenti. L'opzione `--path` sceglie uno snapshot e non limita da sola i file da estrarre; per un sottoinsieme si controllano invece i percorsi di `--include` o la sintassi snapshot:sottocartella. Per il collaudo si evita il ripristino sul posto e non si usa `--delete`. Su Windows il recupero di link simbolici e descrittori completi di sicurezza richiede privilegi specifici: il contenuto corretto non prova che siano stati recuperati tutti i metadati. [Ripristino e limiti dei metadati](https://restic.readthedocs.io/en/stable/050_restore.html).

Il passaggio discriminante usa due versioni artificiali diverse: dopo aver salvato A si modifica soltanto l'originale in B, poi si recupera l'ID di A nella cartella vuota. Si confrontano l'impronta attesa e quella recuperata, verificando che differiscano da B. Per il perimetro reale si concordano anche apertura dei formati necessari, permessi e completezza dell'insieme; non si apre un documento personale senza la relativa autorizzazione.

## Verifica e manutenzione

`check` verifica la struttura del repository. `check --read-data` legge anche tutti i pacchetti di dati e richiede tempo e traffico ulteriori; una verifica di un sottoinsieme va registrata come tale. Nessuno dei due sostituisce il recupero applicativo. Se la verifica rileva un difetto, si sospendono le chiusure di collaudo e le rimozioni distruttive finché esiste una copia recuperabile e un piano di riparazione. [Verifiche del repository](https://restic.readthedocs.io/en/stable/045_working_with_repos.html).

```bash
restic -r '<REPOSITORY>' --password-file '<FILE_PRIVATO_PASSWORD>' check
restic -r '<REPOSITORY>' --password-file '<FILE_PRIVATO_PASSWORD>' check --read-data
```

La conservazione proposta per i piccoli insiemi file parte da sette punti giornalieri riusciti, subordinati al dimensionamento e alla necessità dell'utente. Il modello di capacità usa variazioni uniche per punto esplicite, da sostituire con misure: sette punti non occupano necessariamente sette volte i dati, ma nemmeno la sola base iniziale. Le modifiche di file grandi e la manutenzione possono cambiare molto il consumo.

La scelta dei punti da rimuovere con `forget` e la liberazione dello spazio con `prune` sono operazioni distinte. Prima della rimozione si esamina una simulazione della politica, includendo come vengono raggruppati host e percorsi. La manutenzione va misurata e separata dai backup; questo documento non propone un comando distruttivo da incollare su un repository non ancora censito. Dopo la manutenzione si ripete la verifica appropriata. [Conservazione e pruning](https://restic.readthedocs.io/en/stable/060_forget.html).

## Condizioni per dichiararlo operativo

Il job diventa operativo soltanto dopo primo backup del perimetro autorizzato, recupero distinto, prova delle credenziali di emergenza da un'altra macchina, verifica della quota e più giri senza conflitti con l'arresto del NAS. Si conserva un verbale secondo [Permessi, finestre e collaudo](05-permessi-finestre-e-collaudo.md). Al 19/10 tutte queste prove fisiche restano aperte; i test locali del calcolatore verificano soltanto l'aritmetica degli scenari.
