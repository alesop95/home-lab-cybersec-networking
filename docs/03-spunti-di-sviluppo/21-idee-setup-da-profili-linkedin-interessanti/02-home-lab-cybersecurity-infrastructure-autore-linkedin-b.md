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

## Lo scambio diretto del 14/09/2026: la stessa strozzatura sulla WAN, una scelta diversa a valle

Il 14/09/2026, in uno scambio diretto in chat e non in un post pubblico, Autore-LinkedIn-B descrive la propria catena di frontiera e risulta che sia la stessa di questo progetto, su una linea di un altro operatore. Anche lui ha l'ONT in casa, anche lui ha constatato che l'ONT si aspetta il modem originale del provider e non si aggira facilmente, e anche lui ne ha tratto la sola conseguenza possibile, cioe' collocare OPNsense a valle del modem invece che al posto suo. La testimonianza vale come riscontro indipendente e non come prova tecnica, perche' non e' stata verificata su quella linea: e' un terzo che riferisce il proprio esito, non una misura ripetuta qui.

Il valore del riscontro sta nel fatto che sposta il vincolo da peculiarita' a regola. Fino a questo scambio, l'impossibilita' di mettere il firewall in frontiera era documentata come proprieta' della linea di questo progetto, dedotta dall'interfaccia del modem, dall'assistenza dell'operatore e da una prova di collegamento diretto. Trovarla identica su un operatore diverso significa che il doppio NAT domestico non e' un errore di configurazione ne' una sfortuna contrattuale, ma la forma normale che assume un firewall personale dietro un ONT in comodato. E' un'informazione che chiude una domanda invece di aprirla: non c'e' una configurazione migliore da cercare sul modem, c'e' un'architettura da progettare a valle.

La differenza fra i due progetti non e' quindi nella catena WAN, che coincide, ma in che cosa si decide di mettere dietro il firewall. Autore-LinkedIn-B tiene la rete di casa sul modem del provider, dichiarandone la ragione, cioe' il Wi-Fi della famiglia, che deve restare semplice e stabile e non deve dipendere da un apparato su cui si sperimenta; dietro il firewall mette soltanto il laboratorio, solo cablato e isolato, e su quello fa dominio Active Directory, test e attivita' di intrusione controllata senza mai toccare la rete domestica. Sono due reti separate con due scopi separati, e la separazione e' voluta.

Questo progetto fa la scelta opposta, e vale enunciarla per contrasto perche' e' il punto in cui le due architetture divergono. Qui il firewall non deve proteggere un laboratorio dalla casa, deve proteggere la casa da Internet e i suoi segmenti fra loro: dietro OPNsense finiscono le postazioni, lo storage di rete e, alla fine del percorso, anche il wireless, quando gli access point a valle dello switch renderanno spegnibile la radio del modem. E' la ragione per cui la topologia di questo progetto tratta il Wi-Fi generato dal modem come un buco noto, cioe' come uno stato transitorio da chiudere, mentre nel modello di Autore-LinkedIn-B lo stesso wireless non e' un buco ma materia fuori perimetro per definizione, e non avendo niente di wireless nel laboratorio non gli serve nemmeno un access point.

Che cosa si puo' fare dentro una LAN di casa, letto attraverso questa testimonianza, ha una risposta piu' larga di quanto il vincolo sulla WAN lasci temere. Tutto il lavoro che vive dentro il perimetro si puo' fare per intero, perche' il doppio NAT non tocca il traffico interno: la traduzione degli indirizzi agisce solo in uscita, quindi un dominio Active Directory, un insieme di macchine bersaglio, la segmentazione in VLAN, un SIEM che raccoglie i log e un'esercitazione di intrusione si comportano esattamente come si comporterebbero dietro un firewall di frontiera. Cio' che il modem davanti complica e' l'altra direzione, cioe' l'esposizione di un servizio verso Internet, che richiede una traduzione di porta su due apparati in serie invece che su uno, con il modem che deve inoltrare al firewall e il firewall all'host della zona esposta. Ed e' un costo che pesa su questo progetto, dove la DMZ esiste proprio per esporre qualcosa, e non pesa affatto sul modello del laboratorio isolato, dove non c'e' niente da esporre e l'accesso dall'esterno si risolve, quando serve, con una VPN terminata sul firewall.

Dal confronto discende una lettura utile dello stato in cui questo progetto si trovera' fra poco. Il modello del laboratorio isolato non e' soltanto l'architettura di qualcun altro: e' anche, senza modifiche, la configurazione che questo progetto avra' il giorno in cui il firewall sara' configurato e lo switch e gli access point non saranno ancora arrivati. In quel momento la casa continuera' a vivere sul modem e dietro il firewall ci sara' un perimetro ridotto e solo cablato, che e' esattamente la forma descritta qui. Riconoscerla come configurazione utilizzabile, e non come stato incompleto da attraversare in fretta, permette di iniziare a lavorare sul segmento protetto senza aspettare gli acquisti della fase successiva.

Resta un limite da non perdere di vista, ed e' l'unico punto in cui il modello va imitato con cautela. Separare la casa dal laboratorio mettendoli su due reti diverse protegge il laboratorio dalla casa e la casa dal laboratorio, ma non protegge la casa da Internet: i dispositivi domestici restano su un apparato che non si puo' ispezionare, segmentare ne' sottoporre a regole, e la loro superficie d'attacco non cambia di un millimetro. Nel modello di Autore-LinkedIn-B questo e' coerente con l'obiettivo dichiarato, che e' esercitarsi senza fare danni in casa. Qui non lo sarebbe, perche' l'obiettivo comprende il controllo dei dispositivi domestici, e per questo la separazione dei due mondi resta uno stadio intermedio e non il punto d'arrivo.

La catena WAN di questo progetto e le sue conseguenze sono descritte in [Soluzione professionale con OPNSense 25.7](../10-firewall-before-the-switch/02-soluzione-professionale-con-opnsense-25-7.md), mentre le implicazioni dell'esporre un servizio da una linea domestica stanno in [Uscire con la LAN fuori](../10-firewall-before-the-switch/05-uscire-con-la-lan-fuori.md).
