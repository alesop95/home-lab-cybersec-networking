# OpenMediaVault come alternativa a TrueNAS per questo NAS

Ritorno alla [cartella del NAS](README.md). Valutazione dell'8/10/2026, chiesta dall'utente: se OpenMediaVault sia un'opzione per il NAS ricavato dai quattro desktop dismessi. Il documento raccoglie il materiale per decidere; la decisione resta dell'utente. Il progetto oggi prevede TrueNAS SCALE, con l'insieme di avvio in specchio sui due SSD SATA e un solo pool ZFS in specchio sui due NVMe (ADR-015).

## Una correzione a quanto scritto finora

Il [consolidamento dei quattro desktop](03-consolidamento-di-quattro-desktop-dismessi-in-un-nas.md) descrive OpenMediaVault come un sistema che porta ext4 o btrfs sopra il RAID software del kernel, e conclude che sceglierlo significa perdere ZFS. È impreciso: OpenMediaVault non ha ZFS nel sistema di base, ma lo supporta con il plugin `openmediavault-zfs` del repository omv-extras, documentato per la versione 7 e per la versione 8 (S74). La differenza vera non è se ZFS c'è, ma come ci arriva, ed è il punto che decide.

## Il confronto sui requisiti di questo NAS

| Requisito del progetto | TrueNAS SCALE | OpenMediaVault 8 |
|---|---|---|
| ZFS per il pool dei due NVMe | nativo, è il file system del sistema | con il plugin `openmediavault-zfs`; la documentazione raccomanda il kernel Proxmox, installato con un altro plugin, perché porta i moduli ZFS già compilati e allineati |
| avvio in specchio sui due SSD SATA | previsto dall'installatore | non previsto dall'installatore: un disco di sistema solo, oppure un RAID del kernel costruito a mano, procedura non supportata in modo ordinario (S76) |
| robustezza degli aggiornamenti | sistema e ZFS aggiornati insieme dallo stesso progetto | ZFS dipende dall'allineamento fra kernel e moduli; a maggio 2026 un aggiornamento del kernel Debian ha rotto la compilazione dei moduli ZFS sui sistemi con il plugin (S75) |
| memoria e consumo | più esigente; i 32 GB della macchina sono nella fascia consigliata | più leggero, è in sostanza un Debian con un'interfaccia di amministrazione |
| applicazioni in container | catalogo integrato | plugin per Docker Compose |
| curva di apprendimento | più ripida, interfaccia ricca | più dolce, vicina a un Debian amministrato |

La versione corrente rilevata è OpenMediaVault 8.0.8 del 25/01/2026 (S77).

## Che cosa cambierebbe nel progetto

Scegliere OpenMediaVault mantenendo ZFS significa accettare due differenze rispetto ad ADR-015. La prima è l'avvio: senza specchio sui due SSD SATA, il guasto del disco di sistema ferma il NAS fino alla reinstallazione, mentre i dati restano sul pool degli NVMe e si reimportano; il secondo SSD resterebbe libero o diventerebbe un disco di copia del sistema. La seconda è la manutenzione: ogni aggiornamento del kernel diventa un punto da controllare, perché ZFS è un componente aggiunto e non il cuore del sistema. In cambio si ottiene un sistema più leggero e più familiare a chi conosce Debian.

Scegliere OpenMediaVault rinunciando a ZFS, con ext4 o btrfs sopra un RAID del kernel, toglie il secondo problema ma anche le somme di controllo da un capo all'altro della catena, che sono la ragione per cui il progetto aveva scelto ZFS per un archivio.

## Lettura per questo progetto

Per una macchina con 32 GB di memoria, due SSD destinati proprio a un avvio in specchio e un pool ZFS come unico deposito dei dati, TrueNAS SCALE resta la scelta più coerente: fa nativamente le due cose che OpenMediaVault fa con componenti aggiunti o non fa. OpenMediaVault diventerebbe preferibile se cambiassero i presupposti, cioè una macchina con poca memoria, un solo disco di sistema, oppure la scelta consapevole di rinunciare a ZFS per un sistema più semplice. La decisione resta dell'utente; se la conferma, nulla cambia nella guida di montaggio.
