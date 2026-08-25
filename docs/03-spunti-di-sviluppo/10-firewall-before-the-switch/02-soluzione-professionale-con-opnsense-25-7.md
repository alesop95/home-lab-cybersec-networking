# Soluzione professionale con OPNSense 25.7

## Introduzione

Invece di usare un mini-PC generico per firewall e routing, la soluzione migliore in ambito domestico ma con progettazione di classe IT manager è adottare un appliance dedicato o un sistema di routing/firewall consolidato (per esempio una unità Ubiquiti UniFi Dream Machine Pro o Pro SE, o una appliance Protectli/Netgate con CPU adeguata e supporto per OPNsense/pfSense) per gestire VLAN, firewall stateful, QoS e VPN in modo robusto, accompagnato da uno switch gestito L2+/L3 con capacità di VLAN tagging 802.1Q per segmentare i domini di broadcast e applicare policy (ciò evita proxy ARP o bridging accidentale tra reti), e access point Wi-Fi 6/6E di classe enterprise (come Ubiquiti U7 Pro o equivalenti Wi-Fi6) per copertura uniforme e roaming ottimizzato. Questa architettura centralizza controllo, permette configurazioni standardizzate e strumenti di monitoring, e riduce il rischio di errori di sicurezza o incompatibilità.

Nel contesto dell’obiettivo dichiarato (VLAN separate, firewalling, wifi completo, accesso remoto sicuro), la scelta univoca e categorica è di non usare il mini-PC generico proposto nel thread per il firewall di rete ma di adottare un appliance firewall/router dedicato con supporto software consolidato, uno switch gestito con VLAN tagging e access point Wi-Fi progettati per uso enterprise/prosumer, configurando le VLAN su tutto l’infrastruttura, abilitando firewalling inter-VLAN e ip-based access control, e implementando l’accesso remoto tramite un concentratore VPN aziendale (WireGuard/OpenVPN) integrato nel firewall dedicato, lasciando eventualmente la LogicMachine esclusivamente per funzioni di building automation e non come elemento di connettività remota primaria; questo design è il più coerente con criteri di gestione, sicurezza e scalabilità tipici di un IT manager.

Se io voglio avere quindi un PC assemblato anche con vecchio intel (come di 4a o 5a generazione) in cui metto due schede di rete e personalizzo un linux sopra faccio fare il firewall a lui con la migliore soluzione open-source nel 2026 che ora mi descriverai. Traffico a 2,5Gbps. Se assembli un PC x86 con CPU Intel di 4ª o 5ª generazione (Haswell/Broadwell), due NIC da 2,5 GbE PCIe e installi sopra Linux con l’obiettivo di fare firewalling serio a 2,5 Gbps reali, la scelta migliore, univoca e tecnicamente corretta nel 2026 è [OPNsense](https://opnsense.org/).

Non pfSense, non OpenWrt x86, non una distribuzione Linux “pura” con nftables manuale: OPNsense è un sistema firewall open-source basato su FreeBSD, con stack di rete maturo, pf come packet filter stateful, supporto completo a VLAN 802.1Q, NAT ad alte prestazioni, policy routing, traffic shaping e VPN moderne, ed è progettato esplicitamente come appliance di sicurezza e non come sistema general purpose adattato ex-post.

Dal punto di vista architetturale, con una CPU Haswell i5 o i7 quad-core, NIC Intel i225/i226 o equivalenti ben supportate, interrupt steering corretto e offload controllati, OPNsense è in grado di gestire 2,5 Gbps full-duplex su traffico IPv4 NATtato con regole firewall complesse, mantenendo latenza bassa e stato consistente, cosa che su una distro Linux generica richiederebbe tuning profondo di nftables, conntrack, IRQ affinity, RPS/XPS e gestione manuale degli update di sicurezza, aumentando il rischio operativo; pfSense nel 2026 rimane tecnicamente valido ma è una scelta peggiore perché legato a decisioni di licensing e roadmap meno aperte, mentre OPNsense mantiene governance comunitaria, aggiornamenti frequenti e una separazione chiara tra core firewall e plugin.

[OPNsense®](https://opnsense.org/) is an open source, easy-to-use and easy-to-build FreeBSD based firewall and routing platform. La configurazione corretta prevede OPNsense bare-metal, WAN e LAN su NIC fisicamente separate, VLAN terminate sul firewall e propagate a uno switch gestito, inter-VLAN traffic bloccato di default e aperto solo per policy esplicite, VPN WireGuard terminata direttamente sul firewall, logging centralizzato e nessun servizio non di sicurezza eseguito sulla macchina, perché il firewall deve restare un punto deterministico e noioso, non un server multitasking; in questo scenario, per una rete domestica progettata con mentalità da IT manager, OPNsense su hardware x86 dedicato è la soluzione migliore, più pulita e più sicura, e qualsiasi alternativa è un compromesso o verso la complessità inutile o verso l’affidabilità ridotta.

## Requisiti Hardware

### Esempio di hardware

Ad esempio, è assolutamente possibile installare gratuitamente OPNsense su un PC con Intel i7-6700 @3,40 GHz, 16 GB di RAM DDR4 e SSD Crucial CT500P25SD8 (come quello di Ubuntu Studio), ed è una piattaforma più che adeguata per fare firewalling a 2,5 Gbps reali, con ampio margine operativo; questa affermazione è verificabile perché OPNsense è distribuito sotto licenza open-source BSD ed è progettato per funzionare su hardware x86-64 standard senza vincoli di licenza o attivazione. Dal punto di vista architetturale, l’i7-6700 (Skylake, 4 core / 8 thread, IPC elevato) è nettamente superiore al minimo necessario per NAT stateful, VLAN tagging, firewalling pf, WireGuard e logging a 2,5 Gbps, e resta valido anche se il processore fosse un po’ più vecchio, come un i5/i7 Haswell o Broadwell quad-core, purché non si scenda sotto CPU a 4 core reali con clock decente, perché il collo di bottiglia in questi scenari non è il throughput puro ma la gestione degli stati, delle interruzioni e del packet filtering; in altre parole, Skylake è una scelta solida ma non strettamente necessaria, mentre architetture dual-core o molto vecchie diventano un rischio operativo. Per quanto riguarda le schede di rete, le NIC 2,5 GbE PCIe sono pienamente supportate, a condizione che si scelgano modelli basati su chipset affidabili e ben gestiti dallo stack FreeBSD di OPNsense, come Intel i225-V o i226-V, che operano su PCIe x1 o x2 e forniscono banda sufficiente senza saturare il bus, mentre soluzioni USB-to-2,5 GbE vanno escluse perché introducono latenza, jitter e instabilità sotto carico; con NIC PCIe dedicate, interrupt steering corretto e offload configurati in modo coerente, questa piattaforma gestisce 2,5 Gbps simmetrici senza problemi strutturali. In sintesi, la scelta migliore e categorica è installare OPNsense bare-metal su quell’hardware (o leggermente più vecchio ma equivalente per core e IPC), usare due NIC PCIe 2,5 GbE di classe Intel, terminare lì VLAN, firewall e VPN, e trattare la macchina come appliance di sicurezza dedicata, perché in questo modo ottieni prestazioni, controllabilità e affidabilità coerenti con un design di rete domestica di alto livello pensato con mentalità da IT manager.

### Requisiti minimi (OPNSense)

I requisiti minimi realistici e tecnicamente corretti per installare OPNsense su una macchina con due interfacce di rete a 2,5 Gbps simmetrici non vanno confusi con i requisiti “di avvio” dichiarati dal progetto, perché quelli servono solo a far partire il sistema, non a garantire throughput, latenza e stabilità sotto carico continuo.

In un contesto reale, con NAT stateful, firewalling pf, VLAN 802.1Q e qualche servizio essenziale come WireGuard, la soglia minima affidabile è una CPU x86-64 con almeno 4 core fisici, preferibilmente Intel da Haswell (4ª gen) in poi, con clock reale ≥ 3,0 GHz e IPC moderno, poiché il packet filtering è fortemente sensibile alla latenza per pacchetto e alla gestione delle interruzioni più che al numero di thread teorici, mentre CPU dual-core o architetture molto vecchie diventano rapidamente il collo di bottiglia

La RAM minima operativa è 8 GB, che consente cache, stato delle connessioni e logging senza pressione sulla memoria, anche se OPNsense può avviarsi con meno, e lo storage minimo pratico è un SSD da 32-64 GB, preferibilmente SATA o NVMe, perché il sistema effettua scritture di log continue e un supporto flash di bassa qualità introduce degrado e latenza nel tempo. Le schede di rete devono essere PCIe dedicate, non USB, basate su chipset con supporto nativo e stabile in FreeBSD, in pratica Intel i225 o i226, collegate su slot PCIe x1 o superiore, perché il bus PCIe fornisce banda sufficiente per 2,5 Gbps full-duplex senza saturazione e consente una corretta gestione degli interrupt e degli offload; configurazioni con una sola NIC e bridging interno o con adattatori USB non rientrano nei requisiti minimi seri per questo scenario. In definitiva, il minimo hardware sensato per OPNsense a 2,5 Gbps è CPU quad-core x86-64 ≥ Haswell a ~3 GHz, 8 GB di RAM, SSD affidabile e due NIC PCIe 2,5 GbE Intel, e scendere sotto questa soglia non è una semplificazione progettuale ma un compromesso che erode prevedibilità, stabilità e margine operativo in una rete domestica disegnata con criteri da IT manager.

## Macchina scelta e implementazioni

### Analisi preliminare della macchina

Si ha la possibilità di comprare un computer funzionante e in buone condizioni i3 settima generazione, SSD e 8GB di RAM Ha 1 scheda rete gigabit, ma 2 slot liberi PCI-Express quindi ci si potrebbero montare 2 schede di rete PCI-EXPRESS 2,5 gbit avendone un totale di 3, 2x2,5 e 1x1. Come schede di rete acquistare 2x di queste [https://www.amazon.it/TP-Link-Adattatore-Express-supporta-TX201/dp/B0BKTHJDHX/?th=1](https://www.amazon.it/TP-Link-Adattatore-Express-supporta-TX201/dp/B0BKTHJDHX/?th=1) con spesa totale 50€.

Quella macchina è sufficiente per un firewall domestico basato su OPNsense. Il processore i3 di settima generazione, insieme a 8 GB di RAM e SSD, è più che adeguato per gestire traffico domestico anche con qualche VLAN o servizi aggiuntivi come VPN, IDS/IPS e logging base. La presenza di una scheda di rete gigabit integrata e la possibilità di aggiungere due schede PCI-Express 2,5 Gbit permette anche, ad esempio, di configurare una topologia con almeno tre interfacce fisiche, utile per separare LAN, WAN e DMZ.

Il limite principale sarebbe la CPU: non supporta accelerazione hardware per crittografia VPN avanzata (come AES-NI sulle connessioni molto veloci), quindi il throughput VPN massimo sarà inferiore rispetto a macchine più recenti. Tuttavia, per traffico domestico e VPN moderate va comunque bene. Difatti, la “crittografia VPN avanzata” in questo contesto non indica un algoritmo diverso, ma il modo in cui gli algoritmi crittografici vengono eseguiti dalla CPU. Le VPN moderne, come IPsec o OpenVPN, usano algoritmi simmetrici standardizzati e verificabili come AES per cifrare e decifrare ogni pacchetto che transita nel tunnel; questo lavoro è computazionalmente intenso perché ogni byte deve essere trasformato matematicamente in tempo reale. In assenza di AES-NI, come nel caso di molti i3 di settima generazione, la crittografia viene eseguita interamente in software: funziona correttamente, è sicura allo stesso livello crittografico, ma consuma molta più CPU e quindi limita la velocità massima del tunnel VPN. Questo significa che la VPN resta perfettamente utilizzabile per accesso remoto, traffico domestico e collegamenti moderati, ma non è adatta a scenari in cui si vogliono cifrare link molto veloci mantenendo latenze e carichi bassi.

L’SSD invece garantisce comunque tempi di avvio rapidi e buona reattività del sistema, mentre 8 GB di RAM sono più che sufficienti per il normale funzionamento di OPNsense e dei suoi servizi integrati considerando che il sistema richiede limitate risorse di memoria e storage, mentre la CPU i3 consente gestione stabile del traffico domestico senza colli di bottiglia evidenti.

In sintesi, si può comunque usare come firewall domestico senza problemi per arrivare a un totale di tre interfacce, configurabili come WAN, LAN e una rete interna o DMZ separata. La macchina, nella sua configurazione attuale, ha sufficiente potenza per gestire traffico domestico fino a qualche centinaio di Mbps reali, con NAT, VPN, QoS o altre regole moderate tipiche di un firewall domestico con OPNsense. Per le schede aggiuntive è prevista l’installazione di adattatori come il TP-Link TX201 che utilizza chip Realtek 8125B e risulta compatibile con FreeBSD tramite il driver rge; in caso di necessità il driver può essere installato manualmente.

In futuro sarà possibile aggiornare a un i5 o i7 di generazione compatibile per incrementare le prestazioni, senza modificare l’infrastruttura esistente. Questa configurazione permette di avere un firewall domestico completo e modulare, con separazione delle reti e capacità di gestione di traffico elevato in ambito casalingo.

#### Compatibilità delle schede di rete

Il modello che si è acquistato è una TP-Link TX201 - PCIe 2.0 x1 - 2.5 Gbps con chipset Realtek RTL8125B e Il driver re(4) / rge(4) per Realtek RTL8125 è pienamente supportato nelle versioni recenti di OPNsense (derivate da FreeBSD 13+ e FreeBSD 14-based release da inizio 2025).

Le Realtek 2.5GbE non sono “top tier” come Intel, ma su OPNsense oggi funzionano bene (driver maturi), sono ottime per LAN interne e perfette per collegamenti a NAS o switch 2.5G. sono state montate e assemblate all’interno della macchina nei rispettivi slot PCIe della scheda madre:

![](assets/img-0023.png)  ![](assets/img-0024.png)

Con 3 NIC totali si ha una cosa del tipo:

- NIC1: onboard Intel Gigabit (WAN o LAN)
- NIC2: TP-Link 2.5G (LAN principale o trunk)
- NIC3: TP-Link 2.5G (per server, NAS, VLAN, trunk, DMZ, ecc.)

Questa è una configurazione ottima per un firewall di fascia small business/piccolo ufficio. Se in futuro uno vuole migliorare ci sono delle NIC più compatibili in assoluto con OPNsense come la [Intel i225-V / i226-V (2.5GbE)](https://www.intel.com/content/www/us/en/products/sku/184676/intel-ethernet-controller-i225v/specifications.html) ma le TP-Link vanno benissimo per iniziare, e nel tuo contesto sono perfettamente adeguate.

### Separazione LAN, WAN e DMZ

È possibile fare esattamente questa configurazione con OPNsense su questa macchina. OPNsense supporta nativamente più interfacce fisiche, la loro assegnazione a ruoli distinti (WAN, LAN, DMZ) e l’applicazione di policy di firewalling e routing separate per ciascuna rete, senza limitazioni legate all’hardware descritto.

In questa configurazione la DMZ può viaggiare sulla scheda di rete integrata a 1 Gbps. L’assegnazione della velocità non è vincolata dal ruolo logico dell’interfaccia ma solo dalla scheda fisica a cui viene associata; quindi, WAN e LAN possono essere sulle due PCIe da 2,5 Gbps e la DMZ sulla porta gigabit integrata, oppure qualsiasi altra combinazione coerente con le esigenze di banda.

### NAT

In questo contesto il NAT viene usato per permettere ai dispositivi della LAN e, se previsto, della DMZ di uscire verso Internet utilizzando l’unico indirizzo IP pubblico assegnato sulla WAN. Con OPNsense l’implementazione tipica è il source NAT automatico: tutto il traffico che origina dalla LAN viene tradotto sull’interfaccia WAN, riscrivendo l’indirizzo sorgente privato con quello pubblico.

Dal punto di vista operativo significa che un PC in LAN con IP privato, ad esempio 192.168.1.10, quando apre una connessione verso Internet viene visto all’esterno come proveniente dall’IP pubblico della WAN; il firewall mantiene una tabella di stato che associa ogni connessione interna alla risposta in ingresso, consentendo il traffico di ritorno e bloccando quello non correlato.

Per la DMZ il NAT può essere configurato in modo analogo per l’uscita, ma con la possibilità aggiuntiva di creare regole di port forwarding dalla WAN verso un host specifico in DMZ, ad esempio per esporre un servizio web, senza concedere alcun accesso diretto alla LAN.

#### Puntualizzazione su DMZ, NAT e portforwarding

Qui fondamentalmente il punto chiave è separare tre concetti diversi che spesso vengono confusi: uscita verso Internet, accesso dall’esterno e isolamento dalla LAN. Dire che “la DMZ usa il NAT in uscita”, significa che anche i dispositivi nella DMZ, come quelli in LAN, possono aprire connessioni verso Internet usando l’IP pubblico della WAN. Dopodichè dal punto di vista di Internet non c’è differenza perché il firewall traduce l’indirizzo sorgente privato della DMZ nell’IP pubblico e tiene traccia della connessione. Questo serve, ad esempio, per aggiornamenti di sistema o per servizi che devono contattare risorse esterne. In questo passaggio si intende esattamente il caso di un server collocato in DMZ che ospita un’applicazione in sviluppo o in esercizio, come fosse una piccola VPS domestica, e che deve poter uscire verso Internet per aggiornamenti di sistema, download di dipendenze, accesso a API esterne o altri scambi di traffico in uscita.

Il port forwarding è invece un meccanismo diverso perché serve a permettere a una connessione che nasce dall’esterno, quindi dalla WAN, di arrivare a un host interno. In questo caso il firewall riceve un pacchetto destinato all’IP pubblico su una certa porta, per esempio la porta 80 o 443, e lo “gira” verso un indirizzo specifico nella DMZ, per esempio un server web. Qui il NAT lavora in ingresso, riscrivendo l’indirizzo di destinazione e inoltrando il traffico solo verso quell’host e solo su quelle porte. Il punto cruciale è che questo inoltro riguarda esclusivamente la DMZ. Il firewall non crea nessuna regola che permetta a quel traffico, o al server in DMZ, di raggiungere liberamente la LAN e di default la DMZ è isolata: può parlare verso Internet se autorizzata, può ricevere traffico dall’esterno solo sulle porte esplicitamente esposte, ma non può iniziare connessioni verso la LAN. In questo modo, anche se il servizio esposto in DMZ venisse compromesso, l’attaccante resterebbe confinato in quella rete e non avrebbe accesso diretto ai dispositivi interni.

### QoS

Il QoS, nello stesso scenario, serve a controllare come la banda disponibile viene distribuita tra i vari flussi di traffico, soprattutto quando la linea Internet è satura.

Su OPNsense questo si traduce nella creazione di code di traffico sull’interfaccia WAN, tipicamente basate su priorità o su bandwidth shaping. Un esempio concreto è dare priorità alta al traffico interattivo e sensibile alla latenza, come VoIP o VPN, e priorità più bassa a download massivi o streaming. Quando un dispositivo in LAN avvia un grosso download e contemporaneamente un altro dispositivo sta usando una VPN o una chiamata VoIP, il QoS interviene facendo sì che i pacchetti critici vengano trasmessi per primi, evitando jitter e ritardi percepibili. In pratica il firewall diventa un arbitro: non aumenta la banda disponibile, ma decide chi la usa per primo e quanto, mantenendo la rete reattiva anche sotto carico.

## Implementazione

### Primo download

Andando su [https://opnsense.org/](https://opnsense.org/) si può “Download OPNsense®”, in questo caso in riferimento alla release 25.7 (january 2026) con codename “Visionary Viper”:

![](assets/img-0025.png)

Le cui features sono documentate [https://www.deciso.com/opnsense-25-7-visionary-viper-launches-with-smarter-security-and-faster-setup/](https://www.deciso.com/opnsense-25-7-visionary-viper-launches-with-smarter-security-and-faster-setup/) ed è possibile scaricare anche un whitepaper.

E si apre una pagina in cui dice “Depending on your hardware and use case different installation files are provided to Install OPNsense®. Select the right version for your system and download the best open source firewall.”. Dunque:

![](assets/img-0026.png)

L’installer vga è praticamente l’installer classico, ed è l’immagine standard per installare OPNsense su qualsiasi PC, server o VM e si usa per creare una chiavetta USB avviabile con interfaccia VGA/UEFI. Contiene il full installer con ambiente live, supporta VGA e UEFI e permette una normale installazione su SSD/HD/VM. L’altra “nano” è  pensata per dispositivi embedded tipo APU, PC Engines, routerbox, dove il sistema viene avviato direttamente da SD card, USB stick o compact flash.

Nel caso di un hardware (i3 7th gen + SSD + 8GB RAM) c’è un SSD interno, un hardware x86 moderno che è compatibile con UEFI/GPT e 8GB di RAM rendono possibile un’installazione standard.

L’architettura è forzata a amd64 e denota l’architettura 64 bit [x86](https://en.wikipedia.org/wiki/X86-64) proprio come Intel i3 7th gen. Questo è perché l’unica architettura supportata oggi per l’installazione standard di OPNsense è amd64 e non esistono più immagini per i386 (32 bit) o ARM (solo per pochi casi embedded) o altri tipi di architetture alternative. Tutte le versioni moderne di OPNsense (e di FreeBSD da cui deriva) sono orientate a firewall/router di fascia media e alta e privilegiano sicurezza e performance (IDS/IPS, Suricata, ZenArmor ecc.)

Il file scaricato è OPNsense-25.7-vga-amd64.img.bz2.

#### Estrazione dell’archivio

È normalissimo vedere in Windows, ad esempio, il file .img da 0 KB se si sta guardando dentro l’archivio .bz2 non ancora estratto correttamente:

![](assets/img-0027.png)

Windows non supporta nativamente il formato .bz2, e infatti succede spesso che apre l’archivio, mostra il contenuto ma estrae male: il file .img è apparso ma non è stato estratto correttamente.

Per ottenere l’immagine disco reale bisogna decomprimere il .img.bz2 usando uno strumento che supporti davvero BZIP2; Il .bz2 contiene un'immagine .img da circa 800-900 MB. Per risolvere il problema basta scaricare [7-zip](https://www.7-zip.org/download.html):

![](assets/img-0028.png)

Per ottenere un file del tipo OPNsense-25.7-vga-amd64.img:

![](assets/img-0029.png)

In realtà alcune versioni recenti di Rufus accetttano direttamente gli .img.bz2.

### Initial Installation & Configuration

#### Chiavetta con .img

Si è preparata una chiavetta con Rufus scaricato all’ultima versione 4.11.2285 in data 16/01/2025 alle 11:18 con l’immagine OPNsense-25.7-vga-amd64:

![](assets/img-0030.png)   ![](assets/img-0031.png)

Dopo aver estratto con 7-Zip l’archivio si può scrivere l’immagine con Rufus. Prendendo la chiavetta con Rufus e facendola partire al boot sulla macchina selezionata si possono seguire gli step per l’installazione.

##### Checksum verification

C’è anche la possibilità di fare Checksum verification e sulla pagina di download dice esplicitamente “Checksum files next to the images may not prove authenticity of images on any particular mirror. The checksums can also be found in the forum annoucements, mailing lists, blog posts or GitHub.

OPNsense-25.7-vga-amd64.img.bz2 (SHA256) :

705e112e3c0566e6e568605173a8353a51d48074d48facf5c5831d2a0f7fb175

In the following link [https://docs.opnsense.org/manual/install.html#download-and-verification](https://docs.opnsense.org/manual/install.html), it says 4 files are needed for verification process:

The SHA-256 checksum file (<filename>.sha256)

The bzip-compressed image file (<filename>.<image>.bz2)

The signature file for the uncompressed image file (<filename>.<image>.sig)

The OpenSSL public key (<filename>.pub)

OpenSSL is used for image file verification. Questo controllo può essere fatto anche dentro Rufus:

![](assets/img-0032.png)

Chiaramente l’hash sul sito OPNsense *non* è uguale a quello mostrato da Rufus perché sul sito OPNsense viene indicato l’hash di OPNsense-25.7-vga-amd64.img.bz2, ovvero del file archivio originale. È semplicemente l’hash dell’immagine non compressa, che ovviamente non può coincidere con l’hash del .bz2.

Su Windows (PowerShell) si può verificare semplicemente con il comando:

**Get-FileHash** .\**OPNsense-25**.7-vga-amd64.img.bz2 **-Algorithm** **SHA256**

E vedere:

![](assets/img-0033.png)

Dunque, che i due coincidono.

#### Step installazione

Si è inserita la chiavetta e si è fatta partire al boot. Dunque, le prime schermate che si possono osservare sono le seguenti:

![](assets/img-0034.jpeg)

![](assets/img-0035.jpeg)

![](assets/img-0036.jpeg)

		Prendere da qui il QuickShare_2601161748 dentro J:\googleDrive_sync\Portfolio and ongoing studies\Progetti (DEVELOPING)\Home lab networking through ISP

come specificato nella documentazione ufficiale per la “[Initial Installation & Configuration](https://docs.opnsense.org/manual/install.html)**”** “When the live environment has been started, log in with user **installer** and password **opnsense**”, quindi si è entrati con root e password *opnsense*.

….

….

…

Ad un certo punto:

![](assets/img-0037.png)

Le due scelte principali sono il tipo di filesystem e il tipo di schema di partizionamento/boot. Vediamo le varie opzioni:

- Install (ZFS) significa installare OPNsense usando il filesystem ZFS. ZFS offre integrità dei dati, snapshot, gestione avanzata dei volumi. Su un firewall ha senso perché è molto resiliente in caso di corruzione del disco. Consuma un po' più RAM rispetto a UFS ma l’hardware (i3 7th gen, SSD, 8 GB RAM) lo gestisce senza problemi.
- Install (UFS) significa usare il filesystem UFS, più semplice e leggero. Ha meno funzionalità rispetto a ZFS ma leggermente più veloce e con minori consumi di RAM. È quello tradizionale di FreeBSD.

Sul lato destro si trovano delle varianti che specificano lo schema di partizione/boot:

- ZFS GPT/UEFI Hybrid significa installare ZFS su un disco partizionato in GPT con supporto UEFI e fallback BIOS.
   - È la modalità più compatibile con hardware recente. L’installazione crea partizioni GPT e un bootloader UEFI, ma mantiene anche la possibilità di avviare in modalità legacy/BIOS; quindi, l’installazione funziona su qualunque scheda madre degli ultimi 10-15 anni.
- UFS GPT/UEFI Hybrid è la stessa cosa ma usando UFS invece di ZFS.

Quindi scegliendo Install (ZFS) dal menu principale (come nel mio caso), si verrà poi poi guidati a scegliere esattamente il layout, ma *l’opzione equivalente sul lato destro* è ZFS GPT/UEFI Hybrid, cioè ZFS con partizionamento GPT e boot UEFI/Legacy ibrido.

Per questo hardware, la scelta giusta è ZFS + GPT/UEFI Hybrid perché si ha un SSD, 8 GB di RAM e CPU moderna e ZFS porta vantaggi reali in caso di problemi del disco. GPT/UEFI Hybrid garantisce che il sistema si avvii senza problemi oggi e anche in futuro su eventuale migrazione ad altro hardware.

Dopodichè il passo successivo è:

![](assets/img-0038.png)

L’immagine mostra le modalità con cui ZFS può creare il pool del disco. Ogni opzione definisce il livello di ridondanza e quindi la tolleranza ai guasti. In questo caso, avendo un **solo SSD**, la scelta giusta è semplice (*stripe*). Disaminiamo comunque le opzioni:

- stripe - No Redundancy
   - Significa usare un singolo disco senza ridondanza. Se il disco muore, perdi tutto, ma hai massime prestazioni e la configurazione più semplice. Con un solo SSD è l’unica opzione tecnicamente possibile perché tutte le altre richiedono più dischi.
- mirror - n-way mirroring
   - Serve per avere due o più dischi identici, dove ogni scrittura viene duplicata. Ridondanza elevata. Non puoi usarlo perché hai un solo SSD.
- raid10 - RAID 1+0
   - Richiede almeno quattro dischi. Non applicabile nel tuo caso.
- raidz1 - Single Redundant RAID
   - Paragonabile a RAID5. Richiede minimo tre dischi. Non possibile.
- raidz2 - Double Redundant RAID
   - Richiede minimo quattro dischi. Non possibile.
- raidz3 - Triple Redundant RAID
   - Richiede minimo cinque dischi. Non possibile.

con un singolo SSD l’unica scelta valida è stripe, che è esattamente ciò che serve per un firewall a disco singolo. Dunque, in questo caso specifico si è selezionato stripe e si è continuato. ZFS ti dà già vantaggi come checksumming e protezione dalla corruzione logica dei dati anche senza ridondanza fisica. Per un firewall OPNSense domestico o SMB va benissimo, soprattutto con un SSD nuovo (o comunque il cui funzionamento è stato testato a livello hardware prima dell’installazione).

Se in futuro aggiungi un secondo SSD identico potrai valutare di reinstallare e usare mirror.

### Punti salienti della documentazione per firewalling application

Aaaaaaaaaaaaa [https://docs.opnsense.org/firewall.html](https://docs.opnsense.org/firewall.html)

### Configurazione OPNSense

L’obiettivo è che con *ifconfig* si identificano e validano le NIC a livello fisico e driver. Con “Assign Interfaces” si può creare la segmentazione logica. Con la configurazione IP si definiscono i domini layer 3 e con le regole firewall invece la politica di sicurezza tra quei domini.

#### [TBC] Scan porte ethernet e NIC

Si può ottenere questo risultato direttamente dal terminale di OPNsense senza passare da una live Linux. Dal punto di vista operativo, se l’obiettivo è identificare con certezza quali interfacce fisiche corrispondono alla 1 GbE integrata e quali alle due TP-Link 2.5 Gigabit PCIe Network Adapter TX201, farlo nativamente su OPNsense è più coerente perché si lavora già nell’ambiente definitivo in cui il firewall opererà. Difatti, il vantaggio rispetto alla live Ubuntu è quello di non introdurre un secondo stack di driver Linux che potrebbe comportarsi in modo leggermente diverso rispetto a quello BSD, soprattutto con Realtek 2.5 GbE che in passato hanno avuto differenze di stabilità tra driver Linux r8169 e implementazione BSD. In questo modo si sta verificando esattamente ciò che il firewall utilizzerà “in produzione”.

Dal punto di vista architetturale, dopo aver installato OPNsense, è accedere alla console prima di assegnare le interfacce logiche WAN e LAN, e identificare quale è la 1 GbE integrata e quali sono le due 2.5 GbE, annotando MAC address e posizione fisica, poi soltanto dopo procedere all’assignation. È lineare, non richiede media esterni e soprattutto elimina ogni possibile divergenza tra ambiente di test e ambiente operativo.

OPNsense è basato su FreeBSD che utilizza una nomenclatura delle interfacce legata al driver, non al naming “predictable” di systemd tipico di Linux. Dunque, il nome dell’interfaccia in FreeBSD riflette direttamente il modulo driver agganciato al controller PCI. Questa differenza di prefisso è già un primo livello di identificazione tecnica; se la TX201 è basata su chipset Realtek RTL8125, come dichiarato dal produttore, il driver caricato sarà tipicamente re(4) o rge(4) a seconda della versione del kernel. Le interfacce appariranno quindi come re0, re1, re2 oppure rge0, rge1. La NIC integrata 1 GbE invece, se Intel, comparirà come em0 o igb0.

Dopo l’installazione e il primo boot, OPNsense presenta un menu testuale. Da lì si può entrare nella shell scegliendo l’opzione per accedere alla console (“8 - Shell”):

![](assets/img-0039.png)

Tutto quello che segue avviene a livello di sistema operativo FreeBSD; quindi, stai parlando direttamente con il kernel che governerà il traffico reale. Pertanto, daal menu console di OPNsense si può accedere subito alla shell e il primo comando è:

pciconf -lv

Questo interroga il bus PCI e restituisce vendor ID, device ID e descrizione del controller. Qui si ottiene già un mapping preciso tra slot PCIe fisico e dispositivo logico tramite la lettura diretta della configurazione hardware esposta dal firmware al sistema operativo.

Dopodichè si può passare al classico:

ifconfig

Questo comando in ambiente BSD mostra stato link, MAC address e media negotiated. Il campo media indica sia la modalità sia la velocità negoziata a livello PHY, cioè Physical Layer del modello OSI. Pertanto, se si legge un output come “media: Ethernet autoselect (2500base-T <full-duplex>)” significa che quella interfaccia sta negoziando a 2.5 Gbps altrimenti con “1000base-T”, è 1 Gbps.

Se si vuole un dato ancora più specifico si può puoi usare invece:

ifconfig re0 media

oppure:

ifconfig rge0 media

per interrogare solo il media layer di una singola interfaccia. In alternativa:

sysctl dev.re.0

o:

sysctl dev.rge.0

restituisce informazioni driver-level, inclusa la revisione del chipset. Questo consente di distinguere senza ambiguità le due TX201, perché entrambe saranno esposte dallo stesso driver ma con unit number differente.

Per associare fisicamente connettore RJ45 e nome interfaccia non serve poi alcuna GUI: basta portare l’interfaccia down con:

ifconfig re1 down

e osservare quale LED si spegne. Il LED è direttamente pilotato dal PHY della scheda e quando l’interfaccia è down, il link layer viene disabilitato e il LED cade, allora a quel punto si può collegare lì ed è una verifica deterministica.

Siccome dopo l’assignation iniziale, OPNsense crea automaticamente una regola “allow all” solo sulla LAN e WAN e DMZ partono implicitamente bloccate in ingresso. Se si assegnano male le interfacce, rischi di esporti verso Internet o di bloccarti fuori dalla GUI. Per questo la mappatura fisica precedente con ifconfig e verifica LED non è un dettaglio, è un prerequisito operativo.

#### [TBC] L’assignation (segmentazione logica)

Dopo tutto ciò si può fare assignation dentro OPNsense dato l’obiettivo che una NIC a 2,5Gbps sarà la WAN a cui arriva l'ONT della FTTH Fastweb mentre l'altra porta a 2,5Gbps sarà la LAN che arriva al modem Fastweb e la porta a 1Gbps sarà per la DMZ del firewall. L’assignation crea il binding tra nome fisico e funzione logica. Da lì in avanti tutte le regole firewall, il NAT (Network Address Translation, traduzione degli indirizzi IP tra reti), il DHCP server (Dynamic Host Configuration Protocol, assegnazione automatica degli IP) e le policy di routing si agganciano a quel ruolo, non al nome driver.

Questo scenario ha una topologia a tre zone. Una 2.5 GbE sarà la WAN collegata all’ONT e qui OPNsense si comporta da edge firewall e riceve connettività IP dal provider. Se Fastweb espone IPoE via DHCP, si configura la WAN in DHCP client, se fosse PPPoE (Point-to-Point Protocol over Ethernet), si configura una sessione PPPoE sopra quell’interfaccia fisica. La seconda 2.5 GbE la si assegna come LAN e questa diventa la rete *trusted*: qui si attiva il DHCP server interno, si definiscono subnet private, gateway del segmento, eventuali VLAN (Virtual LAN, segmentazione logica layer 2 su un’unica interfaccia fisica). È questa la vera zona con policy permissiva in uscita e controllata in ingresso. La 1 GbE la si assegna come OPT1, che poi può essere rinominata DMZ. La DMZ (Demilitarized Zone) è una rete intermedia tra WAN e LAN. Non è un’etichetta estetica: è un segmento con policy firewall esplicite. Tipicamente si permette traffico in ingresso dalla WAN solo verso servizi specifici in DMZ, si limita fortemente il traffico dalla DMZ verso LAN, e si consente uscita verso WAN in modo controllato. Dal punto di vista del firewall, DMZ è semplicemente un’altra interfaccia con una subnet diversa e regole dedicate. La sicurezza deriva dalle regole che vengono scritte, non dal nome.

Per fare tutto questo si può lavorare dalla console locale di OPNsense, prima ancora di toccare la GUI [https://docs.opnsense.org/manual/gui.html](https://docs.opnsense.org/manual/gui.html). Dopo aver annotato dal passo precedente quale interfaccia fisica si vuole utilizzare come WAN, quale come LAN e quale come DMZ, bisogna uscire dalla shell e tornare al menu principale della console e da lì scegliere l’opzione “1 - Assign Interfaces”.

![](assets/img-0040.png)

Il sistema poi chiede se si vuole configurare VLAN per il momento si può rispondere di no e demandare al passaggio successivo. Poi chiede di inserire manualmente il nome dell’interfaccia per WAN e si può inserire esattamente il nome visto prima, ad esempio rge0. Poi chiede la LAN, ad esempio rge1. Se si ha una terza interfaccia (come nel caso della volontà di accomodare una DMZ), si può aggiungere come detto in precedenza come OPT1 quando richiesto (inserendo, ad esempio, em0).

A questo punto OPNsense crea il binding logico. rge0 diventa WAN. rge1 diventa LAN. em0 diventa OPT1. Dopo il completamento si può rientrare nella GUI web dalla LAN e rinominare OPT1 in “DMZ” per chiarezza amministrativa. La rinomina è solo etichetta, non cambia il binding.

##### [TBC] Scenario con Fastweb che spone IPoE via DHCP

Se come scenario operativo: Fastweb espone connettività IPoE via DHCP sulla porta WAN a 2.5 GbE collegata all’ONT, l’IPoE significa IP over Ethernet. Non esiste incapsulamento PPP come nel PPPoE; l’interfaccia Ethernet negozia il link a livello fisico e successivamente richiede un indirizzo IP tramite DHCP, cioè un meccanismo client-server con cui il dispositivo ottiene automaticamente indirizzo IP, subnet mask, gateway predefinito e DNS. In questo scenario OPNsense non crea nessuna sessione logica sopra l’interfaccia fisica: l’interfaccia stessa è il layer 2 su cui viene eseguito direttamente il client DHCP. Nel caso IPoE via DHCP, la WAN di OPNsense è un semplice client DHCP su Ethernet, riceve configurazione IP completa dal provider, installa automaticamente la default route e diventa l’unico punto di NAT e firewalling tra Internet e le tue reti interne. Non c’è nessun tunnel, nessuna sessione PPP, nessun livello logico aggiuntivo. È il modello più lineare possibile per un edge firewall.

Dal punto di vista tecnico, la WAN *rge0* (nell’esempio precedente) deve essere configurata come “IPv4 Configuration Type: DHCP”. Questo significa che all’avvio del servizio di rete il processo dhclient di FreeBSD invierà un pacchetto DHCPDISCOVER in broadcast sulla rete collegata all’ONT. L’ONT, che è un semplice media converter GPON-Ethernet, *non* assegna IP; il server DHCP è lato Fastweb. Quando Fastweb risponde con DHCPOFFER, OPNsense completa il four-way handshake DHCPREQUEST / DHCPACK e applica i parametri ricevuti direttamente allo stack TCP/IP dell’interfaccia WAN.

È importante chiarire un punto architetturale: in IPoE l’indirizzo IP pubblico viene assegnato direttamente all’interfaccia WAN del firewall, e non c’è un modem che fa NAT davanti. Questo implica che OPNsense diventa l’unico dispositivo di edge routing e NAT verso la LAN. Il gateway predefinito che Fastweb fornisce via DHCP viene automaticamente inserito nella routing table come default route. Questo si può anche verificare con il comando:

netstat -rn

oppure:

route -n get default

dalla shell di OPNsense. Se il DHCP è andato a buon fine, si vedrà una default route puntare verso l’indirizzo del gateway Fastweb.

Dal punto di vista del livello *fisico*, prima ancora di guardare l’IP, la WAN deve mostrare con ifconfig uno stato “status: active” e una negoziazione “media: 2500base-T <full-duplex>”. Questo ti conferma che il PHY sta lavorando a 2.5 Gbps. Se si legge 1000base-T, la limitazione è a livello di cavo, switch intermedio o ONT. Il DHCP non influisce sulla velocità di link, che è puramente layer 1.

Una volta ottenuto l’indirizzo pubblico, OPNsense attiva automaticamente il servizio di gateway monitoring tramite *dpinger*. Questo processo invia pacchetti ICMP echo verso il gateway per misurare latenza e perdita. Non è un dettaglio estetico: il firewall utilizza questo stato per determinare se la WAN è “up” o “down” a livello operativo. Se il monitor fallisce, può marcare il gateway come down e, in scenari multi-WAN, deviare il traffico. Nel tuo caso single-WAN serve per visibilità operativa.

In configurazione standard con IPoE DHCP non è necessario impostare manualmente VLAN sulla WAN, a meno che Fastweb non richieda una VLAN taggata specifica. Se non è documentato dal provider, non va introdotto nulla. L’interfaccia resta Ethernet pura con MTU standard 1500 byte. Diversamente dal PPPoE, non esiste overhead PPP che riduce l’MTU a 1492 byte. Questo è un vantaggio concreto in termini di semplicità e assenza di frammentazione.

Un aspetto da considerare è la natura dell’indirizzo assegnato. Se Fastweb fornisce un IP pubblico dinamico, l’indirizzo può cambiare alla scadenza del lease DHCP. Il lease time è indicato nei parametri ricevuti e puoi verificarlo nella GUI sotto Status > Interfaces o leggendo il file */var/db/dhclient.leases.rge0*. Questo ha impatto su eventuali pubblicazioni di servizi verso Internet, perché richiede l’uso di un servizio Dynamic DNS se l’IP non è statico. Nello scenario la fibra termina sulla borchia ottica e poi sull’Zyxel PM5100-T1, che è un ONT GPON, cioè un Optical Network Terminal che converte il segnale ottico GPON in Ethernet 2.5 GbE. L’ONT non assegna indirizzi IP, non fa NAT e non decide se l’IP sia statico o dinamico. È un puro livello fisico e parte del livello 2. L’assegnazione dell’indirizzo IP avviene a monte, nella rete del provider, tramite IPoE con DHCP oppure altro meccanismo definito da Fastweb.

Il fatto che tu colleghi la porta 2.5 GbE dell’ONT direttamente alla WAN di OPNsense invece che al Fastweb Seven Booster non cambia la natura dell’indirizzo che il provider ti assegna. Cambia solo chi fa da edge router e NAT: nel primo caso il tuo firewall, nel secondo il dispositivo Fastweb. Si può chiedere un IP statico al provider; no, non lo “ottieni” semplicemente bypassando il loro router. La decisione è esclusivamente lato Fastweb.

##### In che cosa consiste l’ultimo problema

Se la WAN riceve un indirizzo pubblico dinamico via DHCP, qualunque servizio che pubblichi dalla DMZ verso Internet sarà raggiungibile solo tramite quell’IP pubblico, e se quell’IP cambia, cambia anche il punto di ingresso dall’esterno.

Realisticamente, sugli accessi FTTH consumer con IP dinamico via DHCP, l’IP pubblico *non* viene cambiato con cadenza fissa giornaliera. In pratica può restare invariato per settimane o mesi e cambiare in occasione di riavvio dell’ONT/modem, reset della sessione lato operatore o riassegnazione infrastrutturale. Non esiste comunque una periodicità garantita; è event-driven, non calendarizzato.

In ogni caso, è fondamentale separare i piani. L’IP della DMZ è un indirizzo privato, ad esempio 192.168.x.x. non è mai visibile direttamente su Internet. Quando si pubblica un servizio in DMZ, OPNsense crea una regola di NAT, Network Address Translation, cioè una traduzione tra indirizzo pubblico WAN e indirizzo privato interno. In pratica Internet vede solo l’IP della WAN; il firewall intercetta il traffico in ingresso su una certa porta e lo inoltra verso l’host DMZ.

Se l’IP WAN è dinamico, non puoi “far vedere a Internet” un IP statico che non possiedi. Non esiste un workaround locale che trasformi un IP dinamico in statico. L’unico modo per avere un IP pubblico statico reale è che il provider te lo assegni contrattualmente. Questo è un vincolo strutturale: l’IP pubblico è sotto il controllo del provider, non del firewall.

Quello che si può fare, e che nella pratica è la soluzione corretta quando l’IP è dinamico, è rendere stabile il nome DNS, non l’IP. Si utilizza un servizio Dynamic DNS, cioè un sistema che aggiorna automaticamente un record DNS quando cambia l’IP pubblico. OPNsense integra client Dynamic DNS che, al rinnovo o cambio del lease DHCP, aggiornano il record A (Address Record, associazione nome → IPv4) presso il provider DNS scelto. In questo modo dall’esterno si accede sempre a un nome, ad esempio servizio.tuodominio.it, e il DNS punta ogni volta al nuovo IP pubblico. Dal punto di vista tecnico, questo non rende l’IP statico, ma rende stabile l’identificatore logico. È una differenza sostanziale. Le connessioni già attive cadono nel momento in cui l’IP cambia, perché il socket TCP è legato all’indirizzo precedente. Non c’è modo di evitarlo su una linea con IP dinamico.

Se invece l’esigenza è avere endpoint realmente statici, ad esempio per whitelist presso terze parti, VPN site-to-site con peer che accetta solo IP fissi, o policy di sicurezza basate su IP sorgente, allora la soluzione corretta è una sola: IP pubblico statico assegnato dal provider. Tutto il resto è mitigazione, non equivalenza. Tutto ciò che si basa su whitelist lato terzi, VPN site-to-site con peer configurato su IP fisso, ACL (Access Control List) basate su IP sorgente o destinazione, presuppone che quell’IP sia stabile.

Dunque, che implicazioni ha se io, ad esempio, nella macchina che collego alla DMZ instalo un virtualizzatore che offre più servizi su VM separate? facciamo un esempio pratico di un servizio a cui questa cosa potrebbe dare fastidio? Il fatto che tu abbia un hypervisor con più VM aumenta l’impatto operativo, non cambia la natura tecnica del problema. Con un solo IP pubblico dinamico, tutte le VM condividono la stessa identità pubblica. Se quella identità cambia, l’intero blocco di servizi viene colpito simultaneamente. L’IP dinamico è compatibile con servizi pubblicati se si accettano due condizioni:

1. eventuali cadute di sessione quando cambia l’IP
1. dipendenza dal DNS per la raggiungibilità.

Se invece il requisito è continuità di endpoint e affidabilità verso terze parti che basano le loro policy su IP fisso, l’IP statico non è un lusso, è un prerequisito architetturale.

Con IP dinamico via DHCP, l’indirizzo WAN può cambiare al rinnovo del lease o in caso di riassegnazione lato provider. Quando cambia, il firewall passa da IP_A a IP_B. Dal punto di vista dello stack TCP/IP, ogni connessione TCP è identificata da una quaterna:

1. IP sorgente
1. porta sorgente
1. IP destinazione
1. porta destinazione.

Questa quaterna identifica univocamente il *socket*. Se l’IP sorgente cambia, quella quaterna non è più valida. Il peer remoto continua a inviare pacchetti verso IP_A, ma tu ora rispondi da IP_B. Per il protocollo è una connessione completamente diversa. Il risultato è che la sessione cade. Non è una questione di configurazione del firewall; è una conseguenza diretta del modo in cui TCP è definito. Non esiste un meccanismo standard che “trasferisca” una sessione TCP attiva da un IP pubblico a un altro su Internet aperta. Le sessioni devono essere ristabilite. Questo è strutturale.

Ora portiamo il discorso nella DMZ con un host che esegue un hypervisor e più VM. Dal punto di vista esterno non cambia nulla. Tutte le VM pubblicate sono esposte tramite NAT sull’unico IP pubblico della WAN. Il firewall mantiene una tabella di stato per ogni connessione che mappa IP pubblico:porta → IP privato VM:porta. Se l’IP WAN cambia, tutte quelle mappature diventano invalide istantaneamente perché il lato pubblico della traduzione non esiste più.

Facciamo un esempio concreto dove questo è critico. Immaginiamo una VM in DMZ che ospita un server SIP per VoIP aziendale. SIP, Session Initiation Protocol, stabilisce una sessione di segnalazione e poi flussi RTP per l’audio. Se l’IP pubblico cambia mentre sono attive chiamate, il provider SIP continuerà a inviare traffico verso il vecchio IP. Le chiamate in corso cadono immediatamente. Inoltre, finché il record DNS non viene aggiornato e propagato, anche nuove chiamate potrebbero fallire. Un altro esempio più “infrastrutturale”: una VPN site-to-site IPsec con un partner che accetta solo peer configurati su IP statico. Se il tuo IP cambia, il tunnel cade. Alcune implementazioni IPsec possono ristabilire il tunnel automaticamente se il peer è configurato tramite FQDN, Fully Qualified Domain Name, cioè nome DNS completo. Ma se il partner ha configurato il tuo peer come indirizzo IP fisso in whitelist, quando cambi IP il traffico viene semplicemente scartato. Non è un problema di virtualizzazione in DMZ; è un problema di identità di rete lato WAN.

Il terzo caso ancora più concreto potrebbe essere proprio un reverse proxy in DMZ che espone applicazioni web per clienti enterprise. Se quei clienti hanno configurato firewall che permettono traffico solo verso il tuo IP specifico, un cambio IP comporta interruzione finché non aggiornano le loro regole. Anche con Dynamic DNS, la propagazione DNS non è istantanea. Il TTL, Time To Live, del record DNS può introdurre minuti o ore di incoerenza. Abbiamo visto che quando l’IP WAN cambia, accadono tre fenomeni distinti e indipendenti:

1. perdita delle sessioni TCP attive,
1. invalidazione delle policy di whitelist lato cliente,
1. disallineamento DNS temporaneo.

Sul primo punto, una sessione HTTPS è una connessione TCP su cui gira TLS (Transport Layer Security). Se l’IP pubblico cambia, il flusso TCP si interrompe perché il peer remoto continua a inviare segmenti verso il vecchio IP. Il firewall non riceve più quei pacchetti, quindi non può rispondere con ACK. Dal punto di vista del client, la sessione va in *timeout* o riceve un RST (reset) se il percorso di rete segnala esplicitamente l’errore. L’utente finale vede un errore di connessione o una pagina che non risponde. Non c’è “migrazione” della sessione TLS: la chiave di sessione è legata a quel canale TCP specifico.

Sul secondo punto, se il cliente ha configurato il proprio firewall per consentire traffico solo verso IP_A, quando si passa a IP_B il loro firewall continua a permettere traffico solo verso IP_A. Anche se il DNS del proprio dominio viene aggiornato rapidamente, il firewall del cliente potrebbe bloccare a monte qualsiasi connessione verso IP_B perché non presente in whitelist. In questo caso il problema non è DNS ma controllo di accesso basato su indirizzo.

Sul terzo punto, il DNS. Quando aggiorni un record A tramite Dynamic DNS, l’autorità DNS cambia immediatamente il mapping tra nome e IP. Tuttavia, i resolver intermedi e i client rispettano il TTL, Time To Live, cioè il tempo massimo per cui possono mantenere in cache il record precedente. Se il TTL è 3600 secondi, per un’ora alcuni client continueranno a risolvere il nome verso il vecchio IP. Durante quel periodo le nuove connessioni falliranno, anche se la tua infrastruttura è già operativa sul nuovo IP.

Per quanto riguarda il ripristino automatico, esistono solo meccanismi di riconnessione, non di continuità trasparente. I client web moderni tentano automaticamente di ristabilire una connessione HTTPS se la precedente cade. Se nel frattempo il DNS si è aggiornato e la nuova risoluzione punta al nuovo IP, la sessione applicativa può ripartire con una nuova connessione TCP e un nuovo handshake TLS. Dal punto di vista dell’utente, può tradursi in un semplice refresh della pagina o in una breve interruzione.

Per le integrazioni machine-to-machine, ad esempio webhook o API REST, il client applicativo deve essere progettato con retry logico: gestione degli errori di connessione, tentativi esponenziali, verifica di idempotenza delle richieste. Se questo è implementato correttamente, un cambio IP si traduce in una finestra di errore temporanea seguita da ripristino automatico.

Ciò che non puoi ottenere con IP dinamico è la garanzia di continuità delle sessioni in corso e la certezza che terze parti con whitelist rigide non debbano intervenire manualmente. Se accetti che una variazione dell’IP comporti caduta delle connessioni attive, possibile finestra di irraggiungibilità legata al TTL DNS e necessità che i peer siano configurati per accettare un nome DNS anziché un IP fisso, allora l’architettura è coerente. Se questi vincoli non sono accettabili a livello di SLA, l’IP statico diventa requisito non negoziabile.

Il punto non è la fibra in sé. FTTH è solo il mezzo fisico. Il vero discrimine è il profilo di servizio IP che il provider ti assegna: dinamico, statico, con o senza SLA (Service Level Agreement, accordo sui livelli di servizio), con o senza indirizzi aggiuntivi.

Hai tre modelli architetturali distinti.

1. Primo modello: FTTH con IP pubblico statico assegnato dal provider. In questo caso puoi esporre direttamente il tuo reverse proxy in DMZ, pubblicare servizi, fare whitelist presso terzi, stabilire VPN site-to-site su IP fisso. Dal punto di vista tecnico è perfettamente equivalente a una linea “business”, salvo eventuali differenze di SLA e tempi di intervento.
1. Secondo modello: FTTH con IP dinamico ma servizi progettati correttamente. Se tutti i clienti accedono tramite DNS, se le integrazioni applicative prevedono retry automatici, se non esistono whitelist rigide su IP, allora puoi operare anche con IP dinamico. Accetti che in caso di cambio IP le sessioni attive cadano e che possa esserci una finestra di disallineamento DNS. Per molti scenari web standard questo è tollerabile.
1. Terzo modello: disaccoppiare completamente l’esposizione pubblica dalla tua linea FTTH. Qui entrano in gioco servizi terzi, ma non come “pezza”, bensì come scelta architetturale. Un esempio è collocare il reverse proxy su una VPS (Virtual Private Server) con IP statico in data center e creare un tunnel persistente dalla tua DMZ verso quella VPS. In questo schema l’IP pubblico stabile è quello della VPS, non della tua FTTH. Se la tua linea cambia IP, il tunnel si ristabilisce in uscita; i clienti continuano a puntare sempre allo stesso endpoint pubblico. È un modello diffuso, non un ripiego.

Esiste anche l’approccio CDN o cloud reverse proxy, dove il traffico Internet termina su infrastruttura distribuita con IP statici e alta disponibilità, e da lì viene inoltrato verso il tuo backend tramite tunnel sicuri. In questo caso la FTTH diventa solo un uplink verso un’infrastruttura più robusta.

Quindi la trasformazione di una FTTH in piattaforma di erogazione servizi non è impedita tecnicamente. È una questione di coerenza tra requisiti di business e caratteristiche della connettività. Se il requisito è “endpoint pubblico immutabile con continuità e whitelist IP lato terzi”, allora o ottieni IP statico dal provider o sposti l’esposizione pubblica su un’infrastruttura con IP statico. Tutto il resto è compromesso consapevole, non impossibilità tecnica.

#### [TBC] Configurare i parametri delle interfacce

Subito dopo l’assignation, si possono configurare i parametri di ciascuna interfaccia. Sempre dal menu console si può scegliere l’opzione per configurare l’indirizzo IP della LAN.

Si può quindi impostare subnet privata, ad esempio 192.168.10.1/24. Per la WAN, se Fastweb usa IPoE via DHCP, nella GUI si imposterà qui l’interfaccia WAN come DHCP client. Se usa PPPoE, si configurerà PPPoE indicando le credenziali fornite.

La DMZ (OPT1) va configurata con una subnet diversa dalla LAN, ad esempio 192.168.20.1/24. Non ci deve essere sovrapposizione di reti, altrimenti il routing interno fallisce. OPNsense abilita automaticamente il routing tra interfacce, ma il traffico è bloccato finché non si creano regole firewall esplicite.

#### La problematica dato il vincolo del provider

Con FTTH da 2.5gb [Autore-LinkedIn-A](https://www.linkedin.com/in/ACoAABSc9aABi8vyWB72YzZwoXloPfaest2-sm0) togliendo il loro modem originale e mettendo Fritzbox 7690 con ont comunque del provider, la fibra passa da lì ma se non ho capito male hai settato il firewall opnsense dopo il modem perché hai lo stesso problema che ho citato io in pratica. Perché un mio fornitore mi ha detto che ha fatto finta di chiamare l’assistenza tecnica del provider dicendo che non gli funzionava il modem e mettendocene un altro aveva fatto la prova (come volevo fare io) del tipo:

---ONT---WAN in 2,5Gbps firewall---LAN out 2,5gbps firewall --- LAN in 2,5Gbps modem Fastweb seven

Senza usare la porta WAN del modem perché così il modem praticamente fa solo bridge e la wi-fi anche passa da OPNsense. NON gli funzionava e ha scoperto che il vero motivo è che l’ONT si aspetta (tra i vari parametri) il MAC address esattamente del modem di default del provider.

Quindi l’unica configurazione possibile è ---ONT---WAN in 2,5Gbps modem Fastweb seven.

Dunque, io allora avevo pensato come workaround:

---ONT---WAN in 2,5Gbps modem Fastweb seven---LAN out 2,5gbps modem Fastweb seven---WAN 2,5Gbps OPNsense e da qui settare tutto il networking poi la LAN 2,5Gbps di OPNsense che parlerà con lo switch 8 porte che compro (pensavo ZYXEL XMG1915-10E (no PoE)) e a quel punto prendo una porta da 2,5Gbps e la porto di sotto (come farò non lo so che strutturalmente è complesso ahahahah)  e da lì access point con adattatore PoE per servire Wi-fi protetta di sotto

Lascio poi un’uscita dell’OPN sense ad una sorta di DMZ a cui collego un server fisico, l’unica cosa è che se vorrò dare un servizio fuori per dei progetti privati, Fastweb come gli altri hanno l’IP pubblico dinamico in DHCP (assumo che non sia PPoE, non mi hanno risposto a più riprese quelli dell’assistenza), magari allora avevo pensato di usare quella porta per un RMM management open source a cui mi connetto io da remoto alla LAN. Non penso ci sia modo di aggirare questo limite invece.

nfatti anche la mia wifi nn passa per il firewall però nel mio caso nn è essenziale mi basta solo che la lan sia protetta. Volendo potevo usare opnsense come ppoe però a quel punto dovevo utilizzare un Fritzbox da 300 euro solo per wifi e visto che da lì ottengo ip pubblico poi era un problema diciamo ho optato la scelta migliore!

Io perchè ho la mia FTTH Fastweb con il modem Seven, però l'ho comunque sempre dovuto acquistare da contratto con la solita cosa a rate. In più siccome non ho molto tempo questo periodo ho preso anche l'extender wi-fi (casa è su 4 piani) intanto per sopravvivere di sotto. Quindi mi confermi che è impossibile

#### Aaaa

#### Bbbb

#### cccc

#### Con una live Ubuntu (aborted)

Per mappare bene le porte del traffico di rete è intelligente, in questo contesto, far partire una live da una chiavetta con un sistema operativo o qualcosa, un tool che dica semplicemente quale sia la scheda di rete delle tre sulla mia macchina che è ad 1Gbps e quali altre due sono quelle dove ho montato alla scheda madre 2 tp-link 2.5 Gigabit PCIe Network Adapter TX201.

![](assets/img-0041.png)

![](assets/img-0042.png)

La soluzione la più semplice e migliore per fare questo è avviare una live Linux minimale (Ubuntu Desktop LTS) da chiavetta USB e identificare le interfacce tramite driver e velocità negoziata. Questa è la strada migliore perché non richiede installazioni permanenti, funziona su qualsiasi hardware x86 moderno, riconosce correttamente i chipset Realtek/Intel/TPLINK e mostra in modo diretto sia il modello della NIC sia la velocità reale (1 Gbps vs 2.5 Gbps). È anche completamente indipendente da OPNsense, quindi non introduce ambiguità durante la fase di installazione del firewall. Basta scaricare Ubuntu Desktop LTS (amd64) dal sito ufficiale Canonical. L’immagine .iso è firmata e ampiamente documentata basta scriverla su una chiavetta USB con Rufus in modalità standard (GPT + UEFI) perché non serve persistenza e poi si avvia la macchina target dalla chiavetta con “Try Ubuntu”.

Rimanendo con una chiavetta Ubuntu 24.04.3 LTS già preparata in precedenza, soluzione più semplice, sufficiente e tecnicamente corretta per l’obiettivo specifico (mappare le NIC e distinguerle per velocità e chipset). Se la chiavetta è stata creata con Rufus partendo da ubuntu-24.04.3-desktop-amd64.iso, allora è già corretta per definizione per un i3 di settima generazione.

Una volta dentro Ubuntu, dal terminale si può lanciare:

	lspci -nn | grep -i ethernet

Questo comando mostra esattamente quali controller di rete sono presenti e il vendor/device ID. Le TP-Link TX201 risultano come controller basati su Realtek RTL8125 (2.5GbE), mentre la porta 1 Gbps integrata sulla motherboard appare come Intel o Realtek 1 GbE, a seconda del modello.

Poi si verifica la velocità negoziata reale delle interfacce:

ip link

E si individuano i nomi delle interfacce (es. enp0s25, enp3s0, enp4s0). Per ciascuna eseguire:

	ethtool enp3s0

L’output riporta chiaramente Speed: 1000Mb/s oppure Speed: 2500Mb/s. Questo dato non è un’inferenza: è la velocità negoziata a livello PHY. Le due TX201 risulteranno a 2500 Mb/s, la NIC integrata a 1000 Mb/s.

Per essere certi al 100% di quale connettore RJ45 corrisponde a quale interfaccia, basta collegare un cavo Ethernet a una porta alla volta e osservare:

ip link set enp3s0 up

E:

ip link set enp3s0 down

Il LED fisico della porta corrispondente si accende/spegne immediatamente. Questo elimina qualsiasi dubbio e consente di annotare con precisione: la porta motherboard corrisponde a quella con velocità massima1 Gbps, i due slot PCIe 1 = 2.5 Gbps, slot PCIe 2 = 2.5 Gbps a quelle montate in aggiunta.

### Third-party plugins evaluation

#### Zenarmor (Sensei)

Dalla documentazione [https://docs.opnsense.org/third_party_plugins.html](https://docs.opnsense.org/third_party_plugins.html) e andando su Zenarmor (Sensei) [https://docs.opnsense.org/vendor/sunnyvalley/zenarmor.html](https://docs.opnsense.org/vendor/sunnyvalley/zenarmor.html) ci sono un sacco di feature:

1. Application Control
1. Cloud Application Control (Web 2.0 Controls)
1. Advanced Network Analytics
1. Web Filtering & Security
1. Cloud Threat Intelligence
1. User-based Filtering and Reporting
1. Active Directory Integration
1. RESTful API
1. Cloud-based centralized management & Reporting
1. Application / Web-category-based Traffic Shaping and Prioritization
1. Policy-based filtering and QoS
1. Encrypted Threats Prevention
1. All-ports full TLS Inspection (for every TCP port, not just HTTPS) Coming soon

## Consumo energia

Ci si vuole chiedere quale sia un consumo stimato probabile mensile di energia elettrica considerando che ho i seguenti costi (dal mio PlicoContrattuale_elettricità.pdf) con <fornitore-energia> di offerta <cod-offerta-energia> con Peel= 0,0000, codice <cod-componente-energia>, tenendo anche presente che: Il prezzo della fornitura della materia prima, energia elettrica sarà determinato applicando i valori economici del Prezzo Unico Nazionale (PUN) che varierà mensilmente secondo i valori assunti nelle ore appartenenti alle fasce corrispondenti di F1, F2, F3, presso la Borsa Elettrica, in caso di contatore di tipo 2G i valori economici del PUN saranno calcolati in modalità oraria, in entrambi i casi verrà integrato lo Spread sopra esposto per ogni singola fascia pari a € 0,00 (zero/00).

I prezzi saranno indicizzati ai valori zonali di area ripartito sui consumi in prelievo di zona, a titolo esemplificativo, il corrispettivo energia riferito al mese di Settembre 2025 è stato pari a €/kWh F1=0,10959; F2=0,12093; F3=0,10188. Le fasce orarie Fl, F2, F3, sono definite in base alla Delibera 181/06 e s.m.i. dalla Autorità di Regolazione per Energia Reti e Ambiente (ARERA). Il prezzo PUN assunto mensilmente in Borsa, per l'energia elettrica, è da intendersi al netto di: perdite di rete, oneri di sistema Arim (comprese le componenti A e UC); la componente Asos per finanziare gli incentivi per la produzione di energia elettrica prodotta da fonti rinnovabili; un corrispettivo fisso per punto di prelievo a remunerazione delle attività commerciali pari a 0,23 €/giorno; i corrispettivi di trasmissione, misura, connessione e distribuzione; gli oneri di dispacciamento come da Del. 111/06 e s.m.i. oltre ai corrispettivi di CMOR se determinati dal precedente fornitore, come previsto dalla Del.ARG/ elt 191/09 e s.m.i.

Per stimare il consumo e il costo elettrico del firewall basato su i3 7a gen, 8GB RAM, SSD e 3 schede di rete (2x2,5 Gbit TP-Link, 1x1 Gbit integrata), consideriamo i valori medi di potenza assorbita:

- i3 7a gen idle con SSD: 25-30 W
- 8GB RAM: circa 3 W
- 2 schede di rete PCIe 2,5 Gbit: 4-5 W ciascuna sotto carico leggero
- Scheda integrata: trascurabile, 1 W

Consumo complessivo medio in idle/uso tipico di firewall domestico possiamo stare sui 35-40 W. Per semplicità prendiamo 38 W come consumo medio costante 24/7. Sempre per semplicità consideriamo il calcolo dell’energia mensile in kWh: 0,038 kW × 24 h × 30 giorni che sono circa 27,36 kWh/mese.

Considerando i prezzi indicativi (febbraio ’26) riportati (F1=0,10959 €/kWh, F2=0,12093 €/kWh, F3=0,10188 €/kWh) e una distribuzione tipica di consumo domestico serale/mattina/pomeriggio, il valore medio ponderato sarà circa 0,112 €/kWh.

A quel punto si può considerare il costo dell’energia elettrica come 27,36 kWh × 0,112 €/kWh ≈ 3,06 €/mese. A questo andrebbe aggiunto il corrispettivo fisso per punto di prelievo 0,23 €/giorno × 30 giorni = 6,9 €/mese ma chiaramente questo si applica all’intera fornitura.

Questa stima deriva dalla moltiplicazione della potenza media assorbita per le ore mensili e dal prezzo unitario medio ponderato delle fasce orarie F1-F3 più il fisso giornaliero previsto dal contratto. Il consumo effettivo potrebbe variare ±10% a seconda del carico reale della macchina e del traffico di rete. I consumi stimati sono realistici per un contesto domestico con massimo tre dispositivi connessi contemporaneamente. La macchina rimane praticamente in idle per la maggior parte del tempo; il carico generato da poche connessioni non aumenta significativamente il consumo. Il fattore dominante è la CPU idle e la gestione della scheda di rete, non il numero di dispositivi connessi. Le schede TP-Link PCIe 2,5 Gbit consumano al massimo 4-5 W ciascuna in trasmissione, ma con traffico domestico leggero raramente arrivano a quel livello. L’SSD e i 8 GB di RAM hanno un consumo costante molto basso, e l’assenza di monitor o periferiche video elimina un carico aggiuntivo. Quindi la stima di circa 38 W medi è coerente e prudente.
