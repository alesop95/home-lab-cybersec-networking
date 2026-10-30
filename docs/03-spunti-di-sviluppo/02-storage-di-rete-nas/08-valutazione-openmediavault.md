# Perché questo NAS usa TrueNAS e quando avrebbe senso OpenMediaVault

Ritorno alla [cartella del NAS](README.md). Valutazione iniziata l’8/10/2026 e riallineata il28/10/2026 su richiesta dell’utente. ADR-026 conserva la decisione originaria; ADR-033 ne ha cambiato i dischi e ADR-039 distingue la memoria prevista da quella effettivamente disponibile. L’[allocazione hardware](../23-studio-home-lab/12-allocazione-dell-hardware.md) descrive dove sono i pezzi, il [registro](09-registro-del-montaggio.md) che cosa è stato realmente eseguito.

## La ragione della scelta attuale

Il progetto vuole un archivio per documenti e copie del server, con controllo dell’integrità e una storia recuperabile dei file. Manteniamo TrueNAS perché organizza intorno a ZFS[^1] la gestione dello storage, delle istantanee e della replica. È una preferenza per una piattaforma integrata da imparare e amministrare, non la dimostrazione che OpenMediaVault perda dati o che serva TrueNAS per condividere cartelle.

OpenMediaVault può usare ZFS. La sua documentazione distingue il sistema di base dal plugin omv-extras e raccomanda un percorso con plugin del kernel e kernel Proxmox per i moduli precompilati. Il plugin documenta anche snapshot, scrub e replica: queste funzioni non sono esclusive di TrueNAS. Il confronto riguarda l’integrazione e le dipendenze da mantenere, a parità di corretta configurazione del filesystem. Fonti primarie S231 e S74: [filesystem OMV](https://docs.openmediavault.org/en/latest/administration/storage/filesystems.html), [plugin ZFS](https://wiki.omv-extras.org/doku.php?id=omv8%3Aomv8_plugins%3Azfs).

## Che cosa otteniamo tecnicamente da ZFS

Immaginiamo un file conservato per mesi: un settore restituisce dati diversi da quelli scritti. ZFS verifica i blocchi tramite somme di controllo. Se il pool dispone di un’altra copia valida, come nello specchio dati previsto, può correggere il blocco; se non ha una copia buona, rilevare l’errore non significa poterlo riparare. Lo scrub è la lettura periodica dei dati per cercare questi problemi anche nei file che nessuno apre. È una proprietà di ZFS utilizzabile anche su OMV, non del marchio TrueNAS. Fonte S233, [ZFS Primer](https://www.truenas.com/docs/references/zfsprimer/).

Se invece cancelliamo per errore un documento, il disco e il suo specchio possono essere perfettamente sani: entrambi registrano la cancellazione. Una snapshot conservata permette di recuperare lo stato precedente. TrueNAS offre pianificazioni e durata delle istantanee nella propria interfaccia, S235, [snapshot periodiche](https://www.truenas.com/docs/scale/25.10/scaletutorials/dataprotection/periodicsnapshottasksscale/). La replica è un altro passo: trasferire gli stati conservati verso un’altra destinazione compatibile. TrueNAS ne gestisce le attività, ma destinazione, accessi e conservazione devono essere configurati, S236, [replica](https://www.truenas.com/docs/scale/25.10/scaletutorials/dataprotection/replication/).

Per questo progetto distinguiamo quattro bisogni: continuare dopo il guasto di un disco, riconoscere dati alterati, recuperare una versione precedente e avere una copia fuori dal NAS. Lo specchio, le somme di controllo, le snapshot e il backup separato rispondono a problemi diversi. Nessuna singola casella selezionata nella GUI li rende tutti risolti.

## Il confronto sulle esigenze reali

| Esigenza | TrueNAS25.10 | OpenMediaVault8 | Peso nel nostro progetto |
|---|---|---|---|
| usare ZFS | componente centrale della piattaforma | supporto tramite omv-extras e relativo percorso kernel/moduli | preferiamo seguire il percorso integrato TrueNAS; OMV con ZFS resta una soluzione valida |
| programmare protezione e recupero | interfaccia per snapshot e replica | il plugin ZFS documenta attività analoghe | il vantaggio scelto è l’ambiente amministrativo, non una funzione negata a OMV |
| condividere cartelle via SMB[^2] | copre il bisogno | copre il bisogno | la sola condivisione non decide il confronto |
| ridurre il requisito di memoria della piattaforma | minimo base dichiarato8GB | minimo base dichiarato1GiB | OMV ha un vantaggio per macchine più limitate; i minimi non misurano lo stesso carico con ZFS |
| far girare applicazioni e macchine virtuali | possibilità non usata come motivo per scegliere il NAS | possibilità non usata come motivo per scegliere il NAS | nel piano questi carichi stanno sul server Proxmox |
| tollerare il guasto del disco di avvio | il nostro Kingston è singolo | anche una scelta OMV può avere avvio singolo | nessun vantaggio di specchio di avvio nella configurazione attuale |

Le fonti dei requisiti sono S204, [hardware TrueNAS25.10](https://www.truenas.com/docs/scale/25.10/gettingstarted/scalehardwareguide/), e S232, [prerequisiti OMV](https://docs.openmediavault.org/en/latest/prerequisites.html). Gli8GB attuali sono il minimo base TrueNAS, non un errore di installazione né una prova che ogni carico futuro starà bene. L’obiettivo del progetto resta16GB, aperto; prima di attribuire lentezza alla RAM servono carico e misure reali. Non esiste qui un confronto di consumi o prestazioni sulle due installazioni.

## Quali argomenti della prima valutazione non valgono più

L’8/10 il piano prevedeva32GB, avvio in specchio sui SATA e dati sui due NVMe[^3]. Il12/10 ADR-033 ha assegnato i NVMe al server e lasciato al NAS il Kingston per l’avvio, con SanDisk e WD per il futuro specchio dati. Dopo le prove RAM, lo stato attuale è RAM-03 da8GB in A2. Il vantaggio dell’installatore capace di preparare l’avvio in specchio non giustifica una configurazione che oggi avvia da un solo disco. Non lo usiamo come ragione attuale per escludere OMV.

Se il Kingston si guasta, il piano richiede reinstallazione e recupero della configurazione, poi importazione del pool dati se integro e compatibile. La copia della configurazione con secret seed è ancora da esportare. Il sistema scelto non rende quel backup già esistente; vale il [piano di ripristino](../05-strategia-di-backup/02-piano-di-backup-e-ripristino-del-lab.md).

Correggiamo anche un’altra generalizzazione della prima valutazione: rinunciare a ZFS non implica che ogni alternativa perda le somme di controllo. Btrfs verifica dati e metadati per impostazione predefinita, S234, [Checksumming](https://btrfs.readthedocs.io/en/latest/Checksumming.html). La sua configurazione e la sua integrazione in OMV andrebbero valutate per quel percorso; non le abbiamo collaudate. Non basiamo il confronto su un generico “gli altri filesystem non controllano i dati”.

Il precedente episodio di aggiornamento riportato da un blog, S75, rimane nel registro delle fonti come materiale storico. La conclusione attuale usa il percorso kernel/moduli dichiarato dai manutentori OMV e omv-extras; non deduce che ogni aggiornamento OMV rompa ZFS. Non ripropone neppure il vecchio numero di versione come rilevazione della release attuale.

## Quando rivaluteremmo OMV

Se il bisogno si riducesse a poche cartelle condivise e il criterio principale diventasse una base Debian con requisiti inferiori, OMV sarebbe una scelta sensata. Lo sarebbe anche volendo ZFS e accettando consapevolmente la manutenzione del relativo plugin e kernel. La nostra preferenza per l’integrazione TrueNAS è una valutazione di progetto: non deriva da un benchmark né da una garanzia di affidabilità superiore del medesimo ZFS.

Con i pezzi attuali e il piano di protezione dei dati già impostato manteniamo TrueNAS. Questa spiegazione chiarisce la decisione esistente; non avvia migrazioni, nuovi acquisti o altre prove della RAM. La separazione fra NAS e server Proxmox è una scelta indipendente, possibile anche con OMV.

## Che cosa è già vero e che cosa costruiremo

| Elemento | Stato al28/10/2026 |
|---|---|
| sistema e memoria | TrueNAS25.10.7 installato sul Kingston; sola RAM-03/A2 da8GB, obiettivo16GB aperto |
| pool dei dati | assente; specchio SanDisk/WD previsto, contenuto SanDisk da chiarire prima della creazione |
| condivisioni, snapshot, scrub e replica dei dati | da configurare e verificare sul futuro pool; la scelta del prodotto non ne dimostra l’esecuzione |
| notifiche e ripristino | OAuth salvato, Google2FA attiva e prima mail NAS ricevuta su Proton; test alert ricevuto e filtro ancora aperto, primo export configurazione con seed acquisito e verificato fuori NAS, seconda copia e restore aperti ADR-043 |

Quando arriveremo a queste configurazioni, il registro conserverà impostazioni, esiti e recuperi realmente provati. Il percorso didattico approfondisce il ragionamento in [Perché manteniamo TrueNAS](../../../.claude/context/refactor-05-scelta-truenas-e-alternativa-omv.md).

[^1]: ZFS è il filesystem e gestore dello storage del progetto OpenZFS; collega organizzazione dei dati, integrità e ridondanza.
[^2]: SMB, Server Message Block, è il protocollo usato per le cartelle condivise in rete.
[^3]: NVMe, Non-Volatile Memory Express, è il protocollo degli SSD collegati tramite PCI Express.
