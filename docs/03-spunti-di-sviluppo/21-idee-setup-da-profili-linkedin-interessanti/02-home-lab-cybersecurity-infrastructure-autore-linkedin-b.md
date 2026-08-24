# Home Lab Cybersecurity & Infrastructure (Autore-LinkedIn-B)

In un post del 20/01/2026 [Autore-LinkedIn-B](https://www.linkedin.com/in/Autore-LinkedIn-B-Autore-LinkedIn-B-4738771a9/) fa un post in cui dice che proseguendo il suo studio in cybersecurity, infrastrutture e sviluppo, ha deciso di realizzare un home lab strutturato, con l’obiettivo di replicare scenari enterprise-like per test, studio e sperimentazione pratica per:

- laboratori di cybersecurity
- test di infrastruttura e sviluppo
- simulazioni reali di ambienti IT

E lì si va a lavorare su:

1. Windows Server (Domain Controller, Active Directory, DNS, DHCP)
1. Proxmox VE (virtualizzazione e cluster)
1. pfSense virtualizzato (firewalling e segmentazione)
1. Switch managed (VLAN e isolamento di rete)

Autore-LinkedIn-B fa anche un dettaglio sullo stato attuale dei nodi del cluster:

- Lenovo ThinkCentre M700 Tiny
- ![](assets/img-0060.png)
   - Intel Core i7-6700T
   - 32 GB RAM
   - SSD 500 GB
- Lenovo ThinkCentre M710Q Tiny
   - Intel Core i5 (6ª gen)
   - 24 GB RAM
   - HDD 500 GB (upgrade previsto)

Con queste risorse iniziali, grazie al corso “[Proxmox per comuni mortali](https://www.udemy.com/course/proxmox-per-comuni-mortali/?couponCode=KEEPLEARNING)” di Autore-Corso-A in Udemy, inizierò la creazione del mio primo cluster Proxmox casalingo. In evoluzione si prevede:

- Switch Zyxel managed
- NAS Synology 2-bay per backup e shared storage
- Integrazione completa in un rack da 10”

È uno scenario simile a quello desiderato. In un post del 25/01/2026, sempre su LinkedIn, c’è un aggiornamento specifico su:

- Installazione di Proxmox su entrambi i nodi
- Assegnazione di IP statici e configurazione iniziale dei sistemi
- Preparazione dell’ambiente in vista della creazione del cluster

Inoltre, per quanto riguarda il monitoring e l’observability, sul nodo più prestante c’è stato il deploy di una VM Ubuntu Server unicamente dedicata al monitoraggio, all’interno della quale si è configurato:

- Grafana per la visualizzazione
- Prometheus per la raccolta delle metriche
- InfluxDB come datastore temporale

L’obiettivo preciso, difatti, è avere una dashboard centralizzata che permetta di monitorare in tempo reale lo stato dei nodi, le risorse (CPU, RAM, storage) e la salute generale dell’ambiente Proxmox.

![](assets/img-0061.png)  ![](assets/img-0062.png)  ![](assets/img-0063.png)

In data 02/02/2025 viene pubblicato un altro aggiornamento in cui si parla di Wazuh, una [soluzione open-source](https://wazuh.com/) come security platform, con installazione e registrazione degli agent (endpoint Windows) e successiva verifica del corretto ingestion dei log e dello stato degli agent.

![](assets/img-0064.png)

L’obiettivo è fare pratica reale su detection, monitoring e incident response e comprendere a fondo il funzionamento di un SIEM/XDR open source, utile in contesti SOC e Security Operations, ma anche vedere in tempo reale cosa viene rilevato durante gli attacchi simulati (processi, eventi di sicurezza, inventory di sistema, ecc.).

Tecnicamente, Wazuh si può installare su una VM Ubuntu, utilizzando Docker (single-node deployment) come SIEM/XDR all’interno di un laboratorio di cybersecurity e quindi farne il deployment in versione Docker su quella VM Ubuntu. Poi c’è anche la generazione e gestione dei certificati per la comunicazione sicura tra componenti.

Il 05/03/2026 c’è un altro post in cui si parla di un vecchio ThinkPad trasformato in firewall proprio con OPNsese per mantenere il laboratorio completamente separato dalla rete domestica dove sono collegate le TV, lo smartpone e altri dispositivi. Ha quindi progettato la rete in questo modo:

- LAN domestica: la rete di casa e quella del laboratorio sono completamente isolate tra loro.
- VLAN 50 - Lab Network: qui girano le macchine virtuali che utilizzo per studiare e fare test:
   - Ubuntu Server
   - Windows Server
   - Metasploitable
- VLAN 60 - Management Network: configurata su uno switch Zyxel tramite Nebula, è dedicata esclusivamente alla gestione dei nodi Proxmox.

Separare il management permette di proteggere l’infrastruttura, evitare errori durante i test e mantenere i backup e i nodi al sicuro.

![](assets/img-0065.png) ![](assets/img-0066.png)

Si è anche configurato una regola firewall su OPNsense che permette l’accesso alla VLAN di management solo dal mio indirizzo IP, anche quando mi collego dalla rete domestica.

C’è stato un aggiornamento del 09/03/2026 in cui:

![](assets/img-0067.png)  ![](assets/img-0068.png)

aa
