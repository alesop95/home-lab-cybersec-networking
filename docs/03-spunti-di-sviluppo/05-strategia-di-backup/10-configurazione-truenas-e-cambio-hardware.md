# Conservare la configurazione TrueNAS anche cambiando macchina

Ritorno alla [strategia di backup](README.md). Requisito esplicito dell’utente del28/10/2026, ADR-043: tutte le personalizzazioni del NAS devono avere una copia recuperabile fuori dal NAS, così che il guasto o la sostituzione della macchina non costringa a rifarle. Questo documento applica le procedure [NAS-01 e NAS-02](04-procedure-di-backup-e-ripristino.md); al28/10 il primo export con seed è acquisito e verificato fuori NAS, mentre il ripristino rimane da collaudare.

## Che cosa dobbiamo conservare

| Oggetto | Come viene protetto | Stato attuale |
|---|---|---|
| impostazioni TrueNAS, utenti, servizi, rete e attività configurate | export nativo del database con Password Secret Seed e copia esterna versionata | tre generazioni con seed acquisite e verificate fuori NAS: impostazioni iniziali, tank e documenti cifrato; seconda copia indipendente e restore aperti |
| documenti e contenuti dei dataset | copie dei dati e verifica del loro recupero | tank e primo dataset documenti cifrato creati; condivisioni e copie dei contenuti ancora da configurare e collaudare |
| materiali esterni alla configurazione | custodia privata dei materiali di recupero necessari, separata dal solo NAS | identità Google protetta da2FA, codici backup rinviati; chiave JSON documenti acquisita e verificata fuori NAS, copia indipendente e sblocco ancora da provare |

Il seed permette di recuperare anche i campi cifrati del database su un nuovo dispositivo di sistema. L’export conserva l’impianto amministrativo; non contiene i file dei dataset. Le passphrase ZFS e i segreti conservati da servizi esterni hanno una custodia propria. Fonte S137, [gestione della configurazione25.10](https://www.truenas.com/docs/scale/25.10/scaletutorials/systemsettings/advanced/managesysconfig/). Dopo un recupero, il consenso Google va verificato con un invio reale: un export non impedisce al provider di revocare un’autorizzazione.

## La prima tappa salvata

Sono osservati TrueNAS25.10.7, localizzazione Europe/Rome, tastiera italiana, account amministrativo, Gmail OAuth salvato e destinatario Proton nel profilo locale. Il test mail è stato inviato e ricevuto su Proton il28/10/2026, con12:25 mostrato sul messaggio e sulla notifica. Il registro privato conserva indirizzi, oggetto e immagini. Questa tappa è ora esportata con seed e copiata fuori NAS; servizio alert e filtro Log NAS potranno produrre una successiva versione.

Per acquisire una versione dalla GUI, chiudere eventuali pannelli e aprire System > Advanced Settings. In Manage Configuration scegliere Download File. Nel dialogo selezionare Export Password Secret Seed e salvare il file sul PC. Non caricare configurazioni e non ripristinare impostazioni durante questa acquisizione. La [guida al backup TrueNAS](https://www.truenas.com/docs/scale/25.10/gettingstarted/configure/setupbackupscale/), S158, descrive il salvataggio dopo le modifiche.

Quando il file esiste, nel livello privato si registrano versione, tappa, data di acquisizione, dimensione, impronta SHA-256 e percorso delle copie. L’archivio e il seed non entrano in git né nelle fotografie pubbliche. Si mantiene la versione precedente e una copia fuori dal NAS in una destinazione protetta; il solo nome di una cartella predisposta non costituisce un backup. La verifica dell’impronta conferma la copia del file, non sostituisce una prova di ripristino.

## Come recuperiamo l’impianto su altro hardware

La procedura prevista parte da un supporto di sistema nuovo con una versione TrueNAS compatibile, poi ripristina l’export con seed. Non si presume che vecchi nomi di interfaccia e collegamenti fisici coincidano: si verifica la rete dalla console e si recupera l’accesso amministrativo. La documentazione ufficiale descrive nomi di scheda dipendenti dall’hardware e accesso locale per correggere la rete, S238, [interfacce](https://www.truenas.com/docs/scale/25.10/scaletutorials/network/interfaces/).

Se i dischi dati sono sopravvissuti, si identificano per modello e mappatura privata e si verifica il pool prima dell’eventuale importazione, secondo NAS-02. Se i dati sono perduti, occorre la loro copia separata, NAS-03. Dopo il recupero si controllano accessi e servizi, inclusa una nuova mail di test. Il primo export è già acquisito: non si provoca un guasto o una reinstallazione per questa verifica di acquisizione.

## Il materiale Veeam Linux già disponibile

Il pacchetto [veeam-linux](../../../.claude/templates/veeam-linux/README.md), S237, contiene guida e riscontri già acquisiti. Il suo README documenta una procedura percorsa manualmente su Linux il15/10/2026, backup a livello di file e rilettura del punto montato; distingue questo risultato dall’esecuzione completa degli script e dal recupero avviabile della macchina. Il richiamo dell’utente viene quindi recepito senza richiedergli nuovamente quei materiali.

Quel lavoro è la base da riusare per le macchine Linux del lab e per una successiva protezione della cartella degli export dove sarà effettivamente collocata. Non è prova che l’export acquisito sia già incluso in un lavoro Veeam: percorsi inclusi, destinazione indipendente e recupero del file TrueNAS dovranno risultare nel relativo lavoro di backup. L’export nativo conserva ora la configurazione dell’appliance; il collegamento al percorso Veeam non richiede di installare un agente sul NAS in questo giro.

Ogni modifica di configurazione aggiorna il requisito di copia; salviamo checkpoint identificabili al termine delle tappe, prima dei cambi rilevanti e prima del trasferimento di rete o hardware. La tappa è protetta solo quando esiste il relativo file esterno verificato. Il [registro NAS](../02-storage-di-rete-nas/09-registro-del-montaggio.md) tiene distinti modifica effettuata, export acquisito, copia protetta e ripristino provato.

## Verifica della prima acquisizione

Il28/10/2026 è acquisito un export TrueNAS25.10.7 di849920byte, con database e seed. L’originale e la copia nel livello privato del PC hanno lo stesso SHA-256. Il database letto in memoria supera quick_check; controlli booleani confermano i campi della tappa per mittente, nome, OAuth presente, destinatario locale e fuso. Valori segreti non pubblicati. Manifesto e percorso reale sono nel livello privato; download e copia di archivio sono sullo stesso PC. Questa verifica chiude l’acquisizione di una prima copia fuori NAS, non la seconda destinazione indipendente, l’inclusione in Veeam o l’importazione su un sistema sostitutivo.

## Pool non cifrato e recupero dei dataset

Nel wizard del28/10 il nome tank ed Encryption None sono osservati prima della creazione. S240 raccomanda di lasciare non cifrato il dataset radice del pool e gestire eventuali dataset cifrati separatamente. Il materiale di sblocco va custodito fuori NAS e la recuperabilità verificata; l’export con seed non sostituisce le passphrase ZFS. Prima dei primi dati reali va definito quali dataset cifrare. Dal29/10 tank/documenti è creato cifrato e Unlocked, ancora Not Shared; chiave esterna e nuovo export ancora da acquisire. [Creazione del pool25.10](https://www.truenas.com/docs/scale/25.10/scaletutorials/storage/createpoolwizard/).

## Nuova tappa dopo la creazione del pool

Il28/10 tank è creato e la dashboard mostra Online no errors, un mirror a due dischi e213.19GiB utilizzabili. Il primo export con seed resta il checkpoint precedente: non viene presentato come copia della configurazione post-pool. La pagina tank VDEVs è ora letta: MIRROR e membri sda/sdc ONLINE con ZFS Errors No errors. La lettura è conclusa; la nuova generazione con seed è ora acquisita, copiata e verificata fuori NAS mantenendo la precedente. Il nuovo archivio contiene il record tank con GUID e System Dataset Pool tank; questi campi distinguono la tappa post-pool dal primo export. Seconda destinazione indipendente, inclusione Veeam e restore restano aperti. La creazione non chiude la protezione dei dati futuri, che richiede dataset, condivisioni, copie e prove proprie.

## Riscontro dell’export post-pool

Acquisizione e controlli eseguiti il28/10/2026, raccordati qui il29/10. Secondo archivio nativo di849920byte, stessa dimensione del primo ma impronta differente. Originale e copia hanno SHA-256 identici; database SQLite quick_check ok, seed32byte presente e nessuna estrazione di database o seed su file. Il record univoco tank con GUID è presente nel nuovo database e assente nel precedente. Confronti booleani confermano mittente, nome visualizzato, OAuth non vuoto, recapito amministratore Proton, Europe/Rome e System Dataset Pool tank; seed coerente con la prima generazione. Nessun segreto viene stampato o pubblicato. Il mirror e la salute dei membri restano la verifica GUI distinta. Entrambi gli archivi sono conservati nel livello privato; copia indipendente, inclusione Veeam e ripristino non ancora dimostrati.

## Crescita mantenendo la struttura

ADR-044 del29/10 richiede che anche SSD più capienti e RAM compatibile conservino il lavoro logico. La [guida alla crescita](../02-storage-di-rete-nas/11-crescita-del-nas-e-indipendenza-dall-hardware.md) mantiene pool, dataset e nomi delle condivisioni separati dalle taglie attuali; quote, budget delle copie e conservazione si rivedono sulla capacità reale. Prima e dopo il futuro intervento si conservano configurazione con seed e copia dei dati secondo il piano. I due export acquisiti coprono la tappa attuale, non dimostrano un upgrade o un restore già riuscito. Nessuna modifica fisica assegnata nel giro corrente.

## Nuova tappa: documenti cifrato creato,29/10/2026

Il dataset tank/documenti esiste, con cifratura Key predisposta e stato Unlocked. I due archivi precedenti restano validi per le loro tappe, ma non attestano la nuova configurazione. Prossimo Export Key dal riquadro Encryption, acquisizione privata del JSON e nuova generazione export con seed. Nessuna chiave o nuova generazione già scaricata nel riscontro corrente. ACL Mode finale non esposto nella dashboard, ultimo modulo Passthrough: leggere il valore prima di completare accessi e share. Copia indipendente e restore restano aperti, come la protezione futura dei documenti stessi.

## Chiave documenti acquisita,29/10/2026

JSON della chiave acquisito e verificato:86byte, copia privata byte-identica con SHA-256 coerente, dataset atteso e formato256bit confermati senza divulgare il valore. Originale conservato. Acquisizione della chiave fuori NAS conclusa; non è una prova di sblocco e non è ancora una copia su un dominio di guasto indipendente. La nuova generazione configurazione con seed post-dataset resta da acquisire; le due del28/10 sono conservate. La lettura del JSON non misura ACL Mode o permessi dei file.

## Terzo checkpoint con seed acquisito,29/10/2026

Registrato 2026-10-29T11:53:05+01:00. Terzo export TrueNAS25.10.7 post-dataset acquisito:849920byte, copia privata ignorata identica al download per SHA-256, originale conservato. SQLite835584byte letto soltanto in memoria supera quick_check; seed32byte presente e coerente con la precedente. Quindici controlli di checkpoint tutti positivi: record tank/documenti univoco con campo chiave non vuoto e gestione locale, assente nell’export post-pool; pool/GUID invariati; share documenti non creata nel database; mittente/nome e recapito amministratore coerenti, OAuth presente, Europe/Rome e System Dataset Pool tank. Archivio differente da entrambe le generazioni precedenti, che restano conservate. Chiave JSON separata già acquisita e riletta per impronta. Nessun valore segreto stampato, nessun database o seed estratti su file. Il campo chiave del database non è stato decifrato o confrontato in valore con il JSON: la verifica non prova uno sblocco o restore.

Acquisizione dell’export di questa tappa conclusa. Download, archivio e chiave sono sul medesimo client: seconda destinazione indipendente, inclusione Veeam e recupero restano aperti. ACL Mode non è dimostrato dai controlli del database: ultima anteprima Passthrough, valore finale ancora da leggere. Prossimo Datasets > documenti > Edit nel riquadro Details > Advanced Options, scorrere fino a ACL Type/ACL Mode e leggere i valori; poi utente, permessi e condivisione. Nessun altro export identico o test hardware richiesto.
