# Introduzione

Qual è la soluzione migliore, gratis, open source che sia un'alternativa a NinjaOne RMM Management per utilizzo dentro la mia rete domestica nel mio progetto? La strada corretta e univoca per avere un’alternativa gratis e open-source a NinjaOne RMM in un contesto di rete domestica con LAN dietro OPNsense e switch è MeshCentral self-hosted senza costi di licenza e con pieno controllo on-premise.

Si può installare MeshCentral su un server nella LAN (Linux/VM/container) e poi configurarlo per gestire i dispositivi interni tramite agenti MeshCentral: fornisce inventario hardware/software, accesso remoto (WebRTC/SSH/RDP/VNC), esecuzione comandi, script remoti e raccolta log senza dipendere da servizi cloud esterni.

MeshCentral è completamente open source (MIT) e puoi esporre l’interfaccia in HTTPS attraverso OPNsense con autenticazione forte. Usa certificati validi e limita l’accesso tramite firewall/Zenarmor IPS se esposto dall’esterno. Gli agenti possono essere distribuiti manualmente sui client Windows/Linux/macOS all’interno della LAN.

## Requisiti

Per MeshCentral self-hosted in una LAN domestica dietro OPNsense, i requisiti tecnici verificabili reali sono modesti e compatibili con hardware fisico datato, purché x86-64 stabile.

MeshCentral è un’applicazione Node.js e gira tipicamente su Linux (Debian o Ubuntu) o Windows Server; richiede Node.js LTS, porte HTTPS e un processore x64 recente. La memoria indicata come base è nell’ordine di 1 GB o superiore e funziona su qualsiasi CPU x64 moderna [https://corpsystools.com/program/meshcentral/](https://corpsystools.com/program/meshcentral/). Altre documentazioni operative riportano come soglia minima pratica circa 4 GB di RAM e circa 25 GB di spazio disco per un’installazione server standard [https://help.sapphireims.com/Remote_Control_using_MeshCentral.htm](https://help.sapphireims.com/Remote_Control_using_MeshCentral.htm). Il runtime richiesto è Node.js 14+ o successivo, con porte tipiche 443 (HTTPS), 4433 per agent e 80 opzionale per redirect [https://adminhub.dev/program/meshcentral/](https://adminhub.dev/program/meshcentral/).

Traducendo questi dati in un sizing tecnico coerente con un laboratorio domestico ma con margine per virtualizzare altro sullo stesso host, la configurazione consigliata oggi è la seguente. CPU x86-64 con almeno due core fisici reali; qualsiasi piattaforma Intel o AMD relativamente moderna è sufficiente perché il carico di MeshCentral è principalmente I/O e sessioni remote, non compute-bound. RAM reale installata non inferiore a 8 GB se prevedi VM o servizi aggiuntivi, anche se il solo MeshCentral può operare con molto meno. Storage su SSD, con almeno 40-60 GB disponibili per sistema, database interno, log e registrazioni di sessione; la richiesta minima documentata è molto inferiore, ma lo spazio cresce con audit, file transfer e storico. Le porte 443 e 4433 devono essere raggiungibili dai client interni o tramite reverse proxy. Queste indicazioni derivano dai requisiti dichiarati (1 GB+ RAM, CPU x64, porte HTTPS) e dalle installazioni che indicano 4 GB RAM e ~25 GB disco come baseline operativa stabile.

## Idea implementazione

Su vecchio hardware fisico si può dedicare una macchina Linux x86-64 con almeno 2 core, 8 GB RAM e SSD locale. Con questa base puoi eseguire MeshCentral in modo stabile e mantenere headroom per virtualizzare servizi secondari senza saturare memoria o I/O, restando ampiamente sopra i requisiti minimi documentati. Questo significa virtualizzarli sullo stesso hardware fisico, non fare dual boot.

La strada corretta è installare un hypervisor bare-metal sull’hardware fisico, ad esempio Proxmox VE oppure, in alternativa, una distro Linux minimale con KVM. Sopra l’hypervisor si crea una VM dedicata a MeshCentral (Linux + Node.js) e, separatamente, altre VM o container per servizi secondari. In questo modo MeshCentral resta sempre attivo, isolato a livello di risorse e snapshot-abile.

Dedicare “tutto” l’host direttamente a MeshCentral su un singolo sistema operativo funziona, ma è tecnicamente meno solido: perdi isolamento, rollback rapido, snapshot consistenti e migrazione futura. Su hardware anche vecchio, l’overhead di virtualizzazione con KVM è trascurabile rispetto ai benefici operativi.

La scelta corretta è installare un hypervisor bare-metal come Proxmox VE anche in versione free sul fisico. La versione gratuita non è limitata nelle funzionalità core di virtualizzazione; cambia solo l’accesso ai repository enterprise e al supporto commerciale. Le capacità di KVM, LXC, snapshot, scheduling CPU/RAM e networking restano complete. Questa è una caratteristica documentata del modello di licensing di Proxmox: il software è open source e le subscription riguardano aggiornamenti enterprise e supporto, non il motore di virtualizzazione.

Con  un i7 (Haswell) si ha supporto hardware a Intel VT-x e EPT; questo è ciò che conta davvero per avere virtualizzazione efficiente. Di solito, anche senza verificare lo specifico modello di CPU, la famiglia i7 di quarta generazione normalmente include queste estensioni; in ogni caso basta controllare nel BIOS la presenza di Intel Virtualization Technology e, lato OS, il flag *vmx*. Con 16 GB di RAM la configurazione operativa sensata è dedicare una VM Linux leggera a MeshCentral con circa 2 vCPU e 2-4 GB di RAM e lasciare il resto per altre VM o container. MeshCentral non è compute-intensive; il collo di bottiglia reale, se compare, è più spesso lo storage per log e registrazioni di sessione. Per questo l’unico requisito veramente critico è usare un SSD locale invece di un HDD meccanico.

Dunque, si può installare Proxmox VE bare-metal su quel server fisico, creando una VM Linux dedicata a MeshCentral e usare il resto delle risorse per eventuali servizi secondari.

MeshCentral nasce proprio come piattaforma centralizzata di gestione endpoint: installi il server una volta, generi gli agent e li distribuisci su qualsiasi macchina o VM che vuoi controllare, indipendentemente da dove si trovi nella rete o su quale hypervisor giri. Gli agent fanno connessione outbound verso il server e funzionano anche dietro NAT o firewall tramite reverse tunneling; quindi, non serve esporre ogni nodo singolarmente [https://hossted.com/knowledge-base/osspedia/infrastructure-and-network/networking/empowering-secure-remote-device-management-with-meshcentral-self-hosted-scalable-and-privacy-first-control/](https://hossted.com/knowledge-base/osspedia/infrastructure-and-network/networking/empowering-secure-remote-device-management-with-meshcentral-self-hosted-scalable-and-privacy-first-control/). Questo significa che ogni host Proxmox, ogni VM e ogni macchina fisica può essere semplicemente registrata come dispositivo gestito dallo stesso MeshCentral (esattamente come accade per NinjaOne RMM Management).

MeshCentral è gratuito e open source, va semplicemente self-hostato e può essere eseguito come applicazione Node.js o dentro un container Docker perché gira ovunque sia disponibile il runtime Node. In pratica l’architettura giusta in uno scenario domestico è un unico MeshCentral su una VM o container nel Proxmox principale, tutti gli altri server Proxmox e le loro VM registrati come endpoint gestiti.

Solo se in futuro si cerca alta disponibilità o distribuzione del carico si passa a più server MeshCentral in peering con database condiviso. Reddit conferma che è comune eseguire MeshCentral in VM su Proxmox o in container e gestire più macchine da lì, anche in ambienti homelab [https://www.reddit.com/r/MeshCentral/comments/vvi1bt/meshcentral_agent_behind_reverse_proxy](https://www.reddit.com/r/MeshCentral/comments/vvi1bt/meshcentral_agent_behind_reverse_proxy).

La dockerizzazione è la strada più pulita e flessibile per MeshCentral in un contesto domestico o homelab perché consente di astrarre completamente l’applicazione dall’hardware sottostante, semplificando migrazioni future e gestione delle dipendenze. Non serve reinstallare Node.js, configurare certificati o dipendenze di sistema ogni volta: tutto è contenuto nel container. La struttura tipica è un container MeshCentral basato su un’immagine ufficiale o aggiornata dalla community, montando volumi esterni per dati persistenti: il database SQLite o MySQL, i certificati TLS, le configurazioni e i log devono essere fuori dal container. In questo modo, anche se si cambia host o VM, basta riallocare i volumi e rilanciare il container senza perdita di dati.

Inoltre, Docker consente anche di fare versioning e rollback: se una nuova versione di MeshCentral dà problemi, si può tornare alla precedente semplicemente usando l’immagine Docker precedente e mantenendo i volumi. Infine, si puoi combinare Docker con docker-compose per orchestrare altri servizi secondari sullo stesso host senza conflitti di porta o librerie.

Con Proxmox, il setup ideale è la VM Linux leggera (Debian/Ubuntu), installarci sopra Docker e *docker-compose*, creare il container MeshCentral con volumi montati su storage persistente SSD locale, e tutto il resto dell’infrastruttura (eventuali VM secondarie o container) gira nello stesso hypervisor senza interferenze. Questo approccio garantisce continuità del servizio, facilità di backup e portabilità dell’istanza verso un altro server o hardware futuro.

### Server peering (più server MeshCentral)

Se si hanno più server MeshCentral (non più nodi Proxmox ma proprio più server MeshCentral), esiste la modalità corretta per farli lavorare insieme e si chiama *server peering*. In questa modalità più server condividono lo stesso database, certificati e configurazione e collaborano nel gestire le connessioni dei client, tipicamente dietro un bilanciatore [https://ylianst.github.io/MeshCentral/meshcentral/](https://ylianst.github.io/MeshCentral/meshcentral/). È un setup da infrastruttura distribuita, non necessario in un homelab, ma tecnicamente previsto.

### Multi-tenancy nativa

Inoltre MeshCentral supporta multi-tenancy nativa: un singolo server può ospitare più “istanze logiche” o domini separati con utenti e macchine distinti, quindi nella maggior parte dei casi non serve proprio creare più server [https://it.scribd.com/document/543055536/MeshCentral2UserGuide-0-2-9](https://it.scribd.com/document/543055536/MeshCentral2UserGuide-0-2-9), [https://adminboxpro.com/program/meshcentral/](https://adminboxpro.com/program/meshcentral/).

## [TBC] check Xubuntu 24.04

           (verificare )

L’hardware indicato è tecnicamente sufficiente e la versione free di Proxmox non blocca nessuna funzione essenziale.

                MeshCentral nasce proprio

