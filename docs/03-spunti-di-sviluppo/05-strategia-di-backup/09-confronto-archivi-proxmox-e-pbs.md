# Archivi Proxmox e Proxmox Backup Server

Il [piano del laboratorio](02-piano-di-backup-e-ripristino-del-lab.md) propone inizialmente archivi completi su una condivisione del NAS. Il piccolo mirror SATA rende utile valutare anche Proxmox Backup Server, abbreviato PBS. Questo confronto del 20/10/2026 prepara la scelta senza assegnare una macchina, installare un servizio o promettere una conservazione già sostenibile.

## Che cosa cambia nella copia

PVE distingue il backup su storage a file, che produce archivi completi, dal backend PBS, che usa blocchi riutilizzabili. Con gli archivi ogni nuova generazione richiede un altro archivio intero; con PBS il vantaggio dipende dai blocchi realmente nuovi e dal contenuto conservato. Compressione e deduplicazione non hanno qui un rapporto misurato. [Backup PVE](https://raw.githubusercontent.com/proxmox/pve-docs/master/vzdump.adoc).

| Aspetto | Archivi su NAS | PBS da valutare |
|---|---|---|
| primo percorso studiato | PVE scrive su una share dedicata | PVE parla al servizio PBS, che gestisce il datastore |
| spazio delle versioni | generazioni complete più nuova corsa | blocchi necessari ai punti conservati più nuovi blocchi e manutenzione |
| recupero dopo perdita del nodo | ricostruire PVE e raggiungere gli archivi | rendere disponibile anche PBS e il suo datastore prima dei guest |
| amministrazione aggiuntiva | identità SMB, quote e ciclo degli archivi | sistema PBS, identità API, datastore e manutenzioni proprie |
| misura decisiva | byte degli archivi e durata delle corse | occupazione dopo più corse, pruning e raccolta dei blocchi inutilizzati |

Come semplice esempio aritmetico, una base di 60 GB e sei gruppi di modifiche uniche da 2 GB danno 72 GB di contenuto conservato; sette archivi completi da 60 GB danno 420 GB. Sono numeri costruiti, senza metadati, spazio temporaneo o vecchi blocchi ancora presenti. Non sono un benchmark PBS e non sostituiscono i cinque [scenari del calcolatore](03-dimensionamento-e-scenari-di-backup.md). Quel modello accetta quantità dichiarate: non rileva la deduplicazione e non simula il ciclo interno di PBS.

## Risorse e destinazione ancora da assegnare

Il manuale PBS consultato, versione documentale 4.2.8-1, distingue requisiti minimi per valutazione e requisiti raccomandati. Questi ultimi indicano almeno quattro core, 4 GiB per sistema, cache e servizi, un altro GiB per TiB di spazio e almeno 32 GiB per il sistema operativo. Raccomanda storage locale rapido per gli accessi casuali. La soglia di 2 GB della configurazione di valutazione non diventa il dimensionamento operativo del lab. [Installazione e requisiti PBS](https://pbs.proxmox.com/docs/installation.html).

Un eventuale guest PBS sul server da 24 GB sottrarrebbe memoria, CPU e spazio ai servizi già previsti. Il suo disco di sistema e la sua occupazione effettiva entrerebbero nel budget server; i dati di backup devono avere una destinazione distinta dagli originali NVMe che si vogliono proteggere. Una VM con datastore conservato soltanto sullo stesso mirror degli originali non risolve la perdita di quel mirror. La condivisione dell'host mantiene inoltre un guasto comune e richiede una procedura di ricostruzione indipendente.

Per il datastore su filesystem il manuale descrive una directory su ext4, xfs o ZFS e la configurazione in `/etc/proxmox-backup/datastore.cfg`. La share CIFS usata dagli archivi PVE non si trasforma automaticamente in un datastore PBS qualificato. Restano da scegliere e provare percorso, filesystem, permessi, montaggio persistente e comportamento degli accessi. La documentazione letta non giustifica una dichiarazione generale di incompatibilità di ogni storage di rete. [Datastore PBS](https://pbs.proxmox.com/docs/storage.html).

Non si propone qui di installare PBS direttamente dentro TrueNAS né di riformattare i dischi già assegnati. Un'alternativa che richiedesse un altro supporto resterebbe una proposta da valutare con l'utente. I requisiti ufficiali sono il riferimento per il confronto, non una lista di acquisti autorizzata.

## Conservazione e finestra di manutenzione

Il pruning PBS rimuove i metadati dei punti scartati; la garbage collection elimina i blocchi divenuti inutilizzati. Le due operazioni non coincidono. La raccolta legge indici, aggiorna gli accessi dei blocchi e applica una soglia temporale; il manuale corrente descrive una tolleranza di 24 ore e 5 minuti, condizionata anche dagli scrittori attivi. Blocchi in attesa possono restare dopo una corsa. Le verifiche di integrità sono un'ulteriore attività e non dimostrano il recupero dell'applicazione. [Manutenzione PBS](https://pbs.proxmox.com/docs/maintenance.html).

Per questo NAS acceso a finestre, l'ammissione deve considerare lo spazio prima della liberazione effettiva e i turni di raccolta e verifica oltre alla scrittura ordinaria. Le istantanee ZFS possono trattenere dati rimossi dal datastore: il loro budget rimane separato. Una riduzione immediata della conservazione non garantisce spazio immediatamente disponibile per il prossimo backup. Si misurano durata, occupazione e blocchi in attesa su più cicli prima di approvare quote e orari.

## Identità e materiali di recupero

La proposta usa un token PVE con ruolo `DatastoreBackup` limitato al datastore o namespace scelto: consente backup e recupero dei gruppi posseduti. `DatastorePowerUser` aggiunge il pruning dei gruppi posseduti e non è il ruolo iniziale proposto. I diritti effettivi del token sono l'intersezione delle sue ACL con quelle dell'utente; servono entrambe. Conservazione e manutenzione si amministrano separatamente dal writer ordinario. [Ruoli e token PBS](https://raw.githubusercontent.com/proxmox/proxmox-backup/master/docs/user-management.rst).

Questa separazione limita il token, ma un host che controlla la VM PBS o un amministratore che controlla i dischi conserva poteri ulteriori: è un'inferenza del modello di minaccia del lab. Non si attribuisce immutabilità o indipendenza fisica alla sola assegnazione di un ruolo.

Il backend PVE usa per default TCP 8007. L'eventuale nuovo flusso da PVE al servizio PBS e l'accesso amministrativo richiederebbero alias e regole specifici, dopo aver scelto la collocazione. L'impronta TLS va verificata. Se si abilita la cifratura client, PVE conserva la chiave in `/etc/pve/priv/storage/<STORAGE-ID>.enc`: perderla insieme al nodo può rendere i backup irrecuperabili. Una copia utilizzabile deve stare fuori dal sistema protetto. [Backend PBS e chiavi PVE](https://raw.githubusercontent.com/proxmox/pve-docs/master/pve-storage-pbs.adoc).

Il [fascicolo di emergenza](08-fascicolo-di-emergenza-della-rete.md) dovrà allora includere ubicazione e versione PBS, percorso del datastore, configurazione, ACL, materiali di autenticazione e chiave client, custoditi privatamente. La prova deve partire senza il vecchio nodo disponibile: ricostruire l'host necessario, predisporre PBS senza dipendere dal backup della sua stessa VM, collegare il datastore esistente senza inizializzarlo, recuperare accessi e chiavi, poi ripristinare un guest isolato e verificarne dati e servizio. È una condizione di collaudo, non una procedura già eseguita.

## Criterio di scelta per questo laboratorio

Gli archivi rimangono il primo percorso proposto perché consentono di qualificare una copia selezionata con meno servizi da recuperare. Si apre la prova PBS se i punti desiderati non rientrano nel budget degli archivi o se le misure mostrano un vantaggio utile. Per adottarlo devono risultare sostenibili risorse del servizio, datastore distinto, spazio prima della raccolta, finestre di manutenzione e recupero senza circoli. Il verbale deve comprendere anche accesso negato al token fuori ambito e tentativo di pruning negato al writer.

Nessuna delle due alternative copre da sola la configurazione dell'host, i documenti originali sul NAS o la copia scollegata e fuori sede ancora da assegnare. Le procedure già scritte mantengono quei perimetri separati. Al 20/10/2026 il confronto documentale è pronto; la scelta e ogni misura PBS restano aperte, mentre la qualificazione RAM impedisce ancora l'attivazione del NAS.
