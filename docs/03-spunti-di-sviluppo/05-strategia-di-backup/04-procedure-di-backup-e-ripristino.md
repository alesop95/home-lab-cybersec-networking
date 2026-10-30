# Procedure di backup e ripristino del laboratorio

Queste procedure completano il [piano del laboratorio](02-piano-di-backup-e-ripristino-del-lab.md). Preparate il19/10/2026; al28/10 sono acquisite due generazioni dell’export configurazione NAS con seed, prima e dopo la creazione di tank, copiate e verificate fuori NAS secondo NAS-01. Le altre prove, la seconda destinazione indipendente e i ripristini rimangono da eseguire. Prima dell’uso si registrano versione installata, identificativi privati, destinazioni e dimensioni effettive. I segnaposto non sono valori da applicare. Il [collaudo](05-permessi-finestre-e-collaudo.md) stabilisce le prove necessarie per dichiarare una copertura operativa.

## Condizioni comuni di avvio

Il NAS deve avere memoria e dischi qualificati, un pool sano e una copia dei contenuti precedenti dei dischi da riutilizzare, oppure la conferma che quei contenuti siano sacrificabili. La creazione del pool non appartiene a una procedura di backup: è una fase precedente e distruttiva. Al28/10 tank è creato dopo dichiarazione sui dati già salvati e conferma dell’utente, con dashboard Online no errors e mirror a due dischi. Questo non dimostra un backup né chiude l’obiettivo16GB ancora aperto: il NAS mantiene RAM-03/A2 da8GB.

Per ogni oggetto si censiscono originale, copia, responsabile, contenuti esclusi, credenziale di lettura, materiale di sblocco e destinazione di recupero. Si misura lo spazio di picco con il [calcolatore](03-dimensionamento-e-scenari-di-backup.md), includendo nuova generazione, versioni protette, istantanee e spazio della prova di ripristino. Se manca la misura, si può collaudare con dati artificiali limitati; non si ammettono per questo gli originali dell'utente.

Le credenziali e gli export grezzi vivono in un archivio privato fuori dal repository pubblico. Un verbale pubblico contiene soltanto segnaposto, versione, data, metodo e risultato anonimizzato. Prima di ogni prova si verifica che la destinazione sia distinta dall'originale e che lo spazio temporaneo sia disponibile.

## PVE-01: salvare VM e contenitori sul NAS

La proposta iniziale usa il backend CIFS nativo di Proxmox verso una condivisione NAS dedicata al solo contenuto Backup. Si configura dalla gestione storage, con un utente SMB dedicato e senza accesso ospite. Non si combina quel backend con un secondo montaggio manuale della stessa share. La documentazione descrive gestione del montaggio e credenziale sotto `/etc/pve/priv/storage/`; quel livello è sensibile e va incluso nel piano di recupero dell'host. [Backend CIFS Proxmox](https://raw.githubusercontent.com/proxmox/pve-docs/master/pve-storage-cifs.adoc).

La selezione iniziale riguarda servizi necessari e dati irrinunciabili, dopo il loro censimento. Le VM di laboratorio ricostruibili non entrano automaticamente nel job. Per ogni guest si controllano tutti i dischi, le opzioni Backup e le dipendenze esterne: un disco escluso, una share montata nel guest o un dispositivo passato direttamente non acquistano copertura perché il job termina bene. Per i contenitori, i mount aggiuntivi gestiti vanno verificati singolarmente; il contenuto dei bind mount e dei device mount non è salvato da vzdump. [Inclusioni e modi di backup](https://raw.githubusercontent.com/proxmox/pve-docs/master/vzdump.adoc).

La prima esecuzione resta manuale e sorvegliata. Si sceglie il modo di consistenza adatto al servizio e si prova il recupero prima di attivare la pianificazione. Per una VM con database si documenta l'export o il metodo applicativo; l'eventuale guest agent deve risultare operativo e il log deve confermare freeze/thaw quando previsto. Se il servizio non offre un metodo verificato, si preferisce un arresto concordato del servizio o del guest durante la prima qualificazione. Questa è una proposta prudente del piano, non una garanzia di consistenza ricavata dal nome del modo Snapshot.

Si annotano guest inclusi ed esclusi, identificativo del job, data e ora con fuso, archivio prodotto, byte effettivi, durata, esito e avvisi del task. Un archivio presente ma proveniente da un altro guest o da una data precedente non soddisfa il giro corrente. Si mantiene la copia precedente fino a nuova verifica secondo la politica ammessa dallo spazio; il piano non presume l'ordine interno del pruning.

Gli archivi su storage a file sono completi. La conservazione iniziale proposta è di due punti riusciti per i guest selezionati, subordinata al picco misurato; non è una promessa di due giorni coperti se un job viene saltato. Le copie protette vanno contate separatamente: la protezione PVE le esclude dal pruning ordinario, ma un soggetto che scrive sul filesystem può eliminarle. [Conservazione e protezione](https://raw.githubusercontent.com/proxmox/pve-docs/master/vzdump.adoc).

## PVE-02: recuperare un guest senza interferire con quello originale

Si sceglie un archivio identificato esattamente, un ID libero e uno storage di destinazione con spazio sufficiente anche per l'originale ancora presente. Il recupero di prova usa una rete senza percorso verso casa, Internet, storage e servizi reali. Prima dell'avvio si controllano tutte le schede, l'avvio al boot, eventuali hook, dischi esterni e passthrough. Nuovo ID e nuovo MAC non cambiano da soli un indirizzo statico, una credenziale o un servizio che tenta di contattare l'esterno.

Per le VM, la forma seguente è un modello da compilare nella futura sessione di collaudo, non un comando già eseguito. Il target esplicito impedisce di affidarsi allo storage originario scritto nell'archivio; l'avvio resta disattivato. La presenza delle opzioni si controlla nella versione installata.

```bash
qmrestore '<PERCORSO_ARCHIVIO_VM>' '<ID_VM_LIBERO>' --storage '<STORAGE_DI_PROVA>' --unique 1 --start 0
```

Il significato di `--storage`, `--unique` e `--start` è documentato nel [riferimento ufficiale di qmrestore](https://raw.githubusercontent.com/proxmox/pve-docs/master/generated/qmrestore.1-synopsis.adoc); senza target esplicito i volumi sono allocati sullo storage originale secondo il [manuale di ripristino](https://raw.githubusercontent.com/proxmox/pve-docs/master/qmrestore.adoc). Non si usa `--force` per una prova.

Per i contenitori si usa il ripristino della GUI verso un ID libero, controllando storage, mount e rete prima di avviare. La presenza della sola configurazione di un bind mount non prova che il suo contenuto sia nell'archivio. Se il contenuto esterno manca, il verbale riporta recupero incompleto anche quando il contenitore parte.

Si avvia la copia isolata dalla console, si verificano i dati campione e lo stato applicativo specificati nel verbale di collaudo. Per il DNS si interroga la copia da un client isolato con casi attesi; per Wazuh si verifica l'accesso ai dati conservati e si invia un evento sintetico da un agente di prova isolato. Il solo stato Running non chiude la prova. La pulizia dell'ID di prova avviene dopo aver identificato con certezza quella copia e conservato il verbale, mai tramite un comando distruttivo generico.

## HOST-01: conservare ciò che serve a ricostruire Proxmox

Il salvataggio dei guest non è un'immagine dell'intero host. Il fascicolo privato di ricostruzione deve contenere versione PVE e pacchetti rilevanti, nome del nodo, configurazione di rete e bridge VLAN, dischi e pool con mappatura privata, definizioni storage, job, opzioni guest, firewall, account e dipendenze di avvio. Il documento pubblico descrive soltanto struttura e segnaposto. Si conserva anche il supporto di installazione verificato, fuori dai dischi del server.

La configurazione distribuita sotto `/etc/pve` include chiavi, token, password storage e dati di autenticazione. Il suo archivio va quindi trattato come un segreto, con lettura amministrativa e cifratura nella destinazione. Il database pmxcfs in `/var/lib/pve-cluster/config.db` appartiene a una procedura specifica di recupero; non si presenta una copia grezza a caldo come backup coerente senza averne verificato il metodo. [Contenuto e recupero pmxcfs](https://raw.githubusercontent.com/proxmox/pve-docs/master/pmxcfs.adoc).

Il fascicolo si prepara in una finestra senza modifiche amministrative concorrenti. Si raccolgono rete da `/etc/network/interfaces`, nome e risoluzione locale da `/etc/hostname` e `/etc/hosts`, inventario versioni, definizioni storage, job e configurazioni guest. Si aggiungono soltanto le personalizzazioni effettivamente introdotte, compresi eventuali hook e snippet: i percorsi del sistema di base non elencano da soli tutto ciò che un amministratore può avere installato. Si confronta il fascicolo con i componenti reali prima di chiudere il salvataggio.

Per il database, un metodo candidato da collaudare sul futuro nodo è una copia tramite l'API di backup SQLite, anziché una semplice copia del file mentre viene scritto. SQLite documenta una vista coerente del singolo database e la CLI espone `.backup`; si usa una destinazione privata nuova, sorgente aperta in sola lettura e nessun comando di modifica al database originale. Il fascicolo include esito dell'operazione, data, permessi restrittivi e impronta della copia. Questa è un'inferenza progettuale basata sul motore SQLite, non una procedura PVE provata sul nodo del lab. Versione, accesso e compatibilità pmxcfs vanno verificati prima dell'automazione. [API di backup SQLite](https://www.sqlite.org/backup.html), [CLI e apertura in sola lettura](https://www.sqlite.org/cli.html).

Sulla copia si può eseguire `PRAGMA integrity_check;`, controllando il risultato e non il solo codice di uscita. Un risultato `ok` riguarda la struttura SQLite; non prova la ricostruzione dell'host, la corrispondenza con file esterni o l'esistenza dei dischi guest. Il controllo non verifica i vincoli di chiave esterna. Se il metodo non è qualificato, il database non si dichiara protetto da una copia grezza: resta aperto il recupero integrale e si mantiene il percorso di ricostruzione da inventario con backup guest separati. [Perimetro di integrity_check](https://www.sqlite.org/pragma.html#pragma_integrity_check).

Per il primo nodo singolo, la proposta più controllabile è ricostruire un host vuoto da un inventario verificato, ripristinare rete e storage con accesso locale disponibile, riagganciare la destinazione backup e recuperare i guest con PVE-02. La configurazione esportata funge da riferimento; non si sovrascrive in blocco `/etc/pve` su un'installazione diversa. L'eventuale recupero integrale di config.db richiede nodo nuovo senza carichi attivi, servizio fermato, permessi e identità coerenti con la procedura ufficiale. Non è parte automatica del recupero dei guest.

Si conserva almeno una copia del fascicolo host fuori dal server e una possibilità di lettura che non dipenda da un guest del server stesso. Una cartella sul solo mirror NVMe non supera il guasto dell'host; una cartella presente soltanto sul NAS resta indisponibile quando il NAS è spento o guasto. Il supporto esterno del fascicolo di emergenza resta da assegnare e il recupero completo dell'host resta non collaudato.

## NAS-01: salvare configurazione e materiali di sblocco

Dal28/10/2026 ADR-043 rende questo export il prossimo passo dopo la tappa mail riuscita. Il [dettaglio per cambio hardware](10-configurazione-truenas-e-cambio-hardware.md) definisce inclusioni, versioni esterne e rapporto con il materiale Veeam Linux già disponibile. Primo file con seed ora acquisito e verificato fuori NAS il28/10: archivio/database leggibili, copia identica e campi della tappa controllati. Seconda destinazione indipendente, inclusione nel lavoro di backup e restore ancora da verificare.

Dopo la prima configurazione e dopo ogni modifica significativa si esporta la configurazione dalla GUI TrueNAS con Export Password Secret Seed selezionato. Si registrano versione, data, nome logico e impronta del file, senza pubblicare il file o il suo contenuto. Si verifica che l'archivio cifrato di destinazione sia leggibile da un'altra macchina e che il materiale necessario per aprirlo sia disponibile indipendentemente dal NAS. [Gestione configurazione TrueNAS 25.10](https://www.truenas.com/docs/scale/25.10/scaletutorials/systemsettings/advanced/managesysconfig/).

La configurazione non contiene i documenti dei dataset. Le passphrase ZFS non sono memorizzate nel file; si conservano separatamente i materiali di sblocco previsti dalla scelta di cifratura, con una copia di emergenza. L'impronta rileva una modifica o una copia incompleta del file, ma non verifica la validità dell'importazione né la possibilità di sbloccare i dati. Queste ultime richiedono una prova separata.

## NAS-02: guasto del solo dispositivo di avvio

Si registra quali dischi appartengono al pool dati e si verifica che il problema riguardi il dispositivo di avvio. La procedura futura prevede un supporto di avvio sostitutivo e una versione compatibile con la configurazione salvata; non si improvvisa un downgrade. Durante la reinstallazione i dischi dati vanno protetti da una selezione accidentale del target, seguendo una procedura al banco con controllo dei modelli e della mappatura privata.

Si recupera l'accesso amministrativo locale, si carica la configurazione salvata secondo la versione e si verifica se il pool è già riconosciuto. Se serve importarlo, si usa Import Pool dalla GUI o l'API supportata; non Create Pool. Si verificano sblocco, dataset, utenti, ACL e condivisioni con un account autorizzato e con uno che deve essere respinto. La documentazione TrueNAS supporta l'importazione di pool ZFS esistenti dopo reinstallazione e prescrive GUI/API per questa operazione. [Import Pool, versione 25.10](https://www.truenas.com/docs/scale/25.10/scaletutorials/storage/importpoolscale/).

Il recupero si ferma se i dischi non sono identificati, il pool è assente o danneggiato, manca il materiale di sblocco oppure la versione non è compatibile. Non si crea un nuovo pool per far scomparire l'errore. Questo ramo recupera la configurazione e un pool ancora esistente; la perdita del pool richiede la copia distinta dei dati descritta in NAS-03.

## NAS-03: seconda copia dei documenti originali del NAS

La destinazione preferita da valutare senza comprare altro hardware è uno spazio dedicato sul mirror NVMe del server, esterno ai dischi dei guest e conteggiato nel suo budget. È una proposta: spazio libero, sistema di gestione del dataset e software devono ancora essere verificati. Il server non può conservare su se stesso la propria unica copia, ma può conservare una copia distinta dei documenti originali del NAS mentre il NAS conserva gli archivi dei guest.

Un'ipotesi di flusso è il prelievo dal nodo PVE con una credenziale SMB NAS di sola lettura sul solo dataset documenti e un repository restic locale al server. È separata dalla credenziale con cui PVE scrive gli archivi sul NAS. Il repository deve essere accessibile anche da un ambiente di recupero senza dover avviare una VM perduta. Si misura lo spazio sottratto ai guest e si esclude dal prelievo la share degli archivi PVE, evitando una copia ricorsiva dei backup dei backup. Le condizioni del [salvataggio file con restic](06-salvataggio-dei-file-con-restic.md) valgono anche qui.

Questa soluzione non conserva automaticamente tutta la semantica ZFS o le ACL native del NAS: si definiscono i metadati da preservare e si prova il recupero. Per dati aperti o applicativi si preleva una vista coerente o si sospendono le modifiche; una lettura SMB del contenuto vivo non garantisce da sola un istante unico. La replica ZFS verso un'altra destinazione compatibile resta un'alternativa, da progettare con permessi e flusso di rete propri.

Il recupero dopo perdita del pool NAS deve funzionare leggendo il repository dal server o da un ambiente di emergenza, verso una cartella o un pool nuovo distinto. Si controllano contenuti e permessi prima di renderlo originale. Le due copie nella stessa casa restano esposte a un guasto comune, al furto e alla compromissione amministrativa; una copia scollegata o fuori sede resta una pendenza, con destinazione e frequenza da assegnare.

## Stato di esecuzione

| Procedura | Prerequisito materiale ancora aperto | Evidenza richiesta per chiuderla |
|---|---|---|
| PVE-01 | host, NAS e share ancora da configurare | log del job, contenuti e dimensioni reali, esito senza avvisi non risolti |
| PVE-02 | archivio reale e spazio/rete di prova | contenuto ripristinato e servizio verificato in isolamento |
| HOST-01 | host non installato e supporto esterno non assegnato | ricostruzione del nodo documentata con accesso al backup indipendente |
| NAS-01 | due generazioni pre/post-tank con seed acquisite e verificate; seconda destinazione indipendente e verifica del recupero ancora aperte | export con seed custodito e recupero provato separatamente |
| NAS-02 | supporto di prova e configurazione futura | reinstallazione/import su ambiente di prova senza alterare gli originali |
| NAS-03 | destinazione distinta e quota non assegnate | recupero dei documenti dalla copia anche con NAS indisponibile |
