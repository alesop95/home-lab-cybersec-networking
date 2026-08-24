# Gestire dati su disco e renderli disponibili in modo ordinato, sicuro e persistente

## Studio hardware

Voglio valutare l'acquisto di un NAS in rete che posso utilizzare come archiviazione domestica ma anche come un qualcosa al quale mi posso collegare e mi funge anche da server multimediale se collegato ad alcune macchine Windows o Linux. Un NAS di rete completo che parla con le sottolan e con questo modem Seven mi permette la segmentazione.

Ci sono dei requisiti impliciti come multimedia (Plex/Emby), condivisione file, servizi verso Windows/Linux, possibilità di usare due sottoreti (VLAN) verso il Seven. Raccomando NAS con porta(e) 2.5GbE built-in (o slot PCIe per aggiungere NIC Intel), CPU x86 decente e supporto a Plex/Docker/app.

Alcuni modelli consigliati potrebbero essere:

- QNAP TS-464 (4-bay) - dual 2.5GbE: buon bilanciamento CPU, 2×2.5GbE built-in (possono essere aggregate/uso separato per VLAN), ottimo supporto Plex, container, espandibilità PCIe (se si vuole segmentazione, QTS gestisce VLAN e più interfacce) [https://www.qnap.com/en/product/ts-464](https://www.qnap.com/en/product/ts-464), [https://www.qnap.com/en-in/performance/model/ts-464](https://www.qnap.com/en-in/performance/model/ts-464)
- Synology DS925+ / DS925 (modelli Synology con 2×2.5GbE nelle revisioni recenti) eccellente UX, Synology Drive, Video Station/Plex; [https://www.synology.com/en-af/products/DS925%2B](https://www.synology.com/en-af/products/DS925%2B)
- Synology
- TerraMaster F2-425 (2-bay) - 2.5GbE: solida opzione economica per NAS domestico o studio, CPU N5095, buono per Plex e backup; versione 2-bay se non servono 4 bay. (buon rapporto prezzo/prestazioni) [https://www.techradar.com/computing/terramaster-f2-425-nas-review](https://www.techradar.com/computing/terramaster-f2-425-nas-review), [https://www.neowin.net/reviews/terramaster-f2-425-review-a-low-cost-local-cloud-backup-and-streaming-nas/](https://www.neowin.net/reviews/terramaster-f2-425-review-a-low-cost-local-cloud-backup-and-streaming-nas/)

## Studio software

### OpenMediaVault (OMV)

[OpenMediaVault](https://www.openmediavault.org/) (OMV), con alternativi diretti: TrueNAS CORE/SCALE, UnRAID è progettato per essere un sistema operativo dedicato allo storage di rete (NAS), quindi prima di tutto per gestire dischi, dati e condivisioni in modo centralizzato, affidabile e amministrabile via web.

OMV va pensata come un'alternativa open-source a Synology/QNAP che permette di non amministrare tutto a mano su Debian puro ma che al contempo possa garantire affidabilità dei dati con storage centralizzato, particolarmente indicato per un NAS casalingo o small business. Chiaramente se non ci sono dischi da gestire non ha senso, ma il livello rimane quello. OpenMediaVault serve a gestire dati su disco e renderli disponibili in rete in modo ordinato, sicuro e persistente. Se il problema principale non è “come gestisco e condivido storage”, allora OMV non è lo strumento giusto e NON è  comparabile con: Proxmox, ESXi o un Ubuntu Server generico.

OpenMediaVault è una distribuzione Linux basata su Debian, è un SISTEMA OPERATIVO COMPLETO, pensato esclusivamente per aggregare dischi locali, esportare dati in rete, gestire permessi, utenti e servizi di storage e monitorare lo stato dell'hardware di archiviazione. Serve a TRASFORMARE un PC, un mini-PC o un server IN UN NAS (Network Attached Storage), cioè un punto unico dove conservare dati accessibile da altri computer, server, VM, container tramite protocolli standard di rete.

OVM fornisce via interfaccia web:

- Gestione dischi (SATA, USB, NVMe)

- File system (ext4, XFS; ZFS tramite plugin)

- RAID software (mdadm)

- Condivisioni di rete:

	- SMB/CIFS (Windows)

	- NFS (Linux/Unix)

	- FTP / SFTP

	- rsync

- Gestione utenti e gruppi

	- ACL e permessi

	- SMART monitoring (salute dei dischi)

	- Notifiche di errore (mail)

Tutto questo senza lavorare da shell, anche se la shell resta disponibile.

Dopodiché OMV PUO' ospitare servizi, ma sempre come estensione dello storage, non come scopo principale:

- Docker / Docker Compose

- Backup (UrBackup, rsnapshot)

- Media server (Jellyfin, Plex)

- Download (Transmission)

- Cloud personale (Nextcloud, con cautela)

Ma OMV NON NASCE come hypervisor, application server o piattaforma DevOps. Se lo si usa così, si forza il modello.

