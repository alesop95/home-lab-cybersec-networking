# Architettura proposta e diagrammi

[Apri il diagramma vettoriale](topologia-proposta.svg), leggibile nel browser e stampabile senza perdere definizione. I diagrammi Mermaid qui sotto ne dettagliano stati e flussi.

![Topologia proposta del laboratorio](topologia-proposta.svg)

Ritorno allo [studio](README.md). Stato e vincoli derivano dal [verbale OPNsense](../../verbale-installazione-opnsense.md), dalla [topologia preesistente](../../../.claude/context/diagrams/topologia-di-rete.md) e dal piano NAS. Le subnet seguenti sono proposte private, non indirizzi pubblici o prova di configurazione eseguita. La versione OPNsense installata nel verbale è storica: prima di collegarla stabilmente si verifica il percorso di aggiornamento supportato e si esporta la configurazione.

## Stato documentato e bersaglio

È documentata la linea con modem operatore obbligato, l'IP pubblico statico e l'installazione del firewall su i3 di settima generazione, 8 GB RAM, SSD 120 GB, una NIC Gigabit e due TP-Link TX201 a 2,5 GbE. La catena di riferimento diventa ONT -> Seven -> OPNsense: il collegamento diretto ONT -> firewall resta non verificato sulla linea reale e non costituisce il percorso di base. Non è documentato un collaudo del firewall in transito. Il doppio NAT resta il vincolo locale di progetto, senza estenderlo a tutte le linee FTTH. Soltanto la radio integrata nel Seven è esterna al perimetro OPNsense; gli access point collegati allo switch stanno a valle del firewall e le loro reti Wi-Fi sono filtrate e instradate da OPNsense.

```mermaid
flowchart TD
  NET[Internet] --> ONT[ONT Fastweb]
  ONT --> SEVEN[Fastweb Seven: termina la WAN e fa il primo NAT]
  SEVEN --> CASA[Wi-Fi Seven: rete upstream fuori da OPNsense]
  SEVEN -->|LAN 2.5 GbE| FW[WAN OPNsense: secondo NAT e firewall del lab]
  FW -. "acquisto e configurazione" .-> SW[Switch gestito Zyxel]
  SW -. "acquisto, cavi gia' posati" .-> AP[Due AP cablati e PoE, piani 3 e 2]
  SW -. "integrazione dopo collaudo" .-> NAS[NAS in assemblaggio nella sessione dedicata]
```

Nel diagramma operativo proposto la rete essenziale è indipendente dal NAS. Le scelte del 07/10/2026 che lo hanno aggiornato sono nella sezione che segue. Le linee rappresentano collegamenti e funzioni desiderati, non una distribuzione già attiva.

```mermaid
flowchart TB
  WAN[Internet] --> O[ONT Fastweb]
  O --> M[Fastweb Seven: primo NAT, fonia e Wi-Fi upstream]
  M -->|LAN 2.5 GbE| F[OPNsense: secondo NAT, firewall, DHCP, Unbound, WireGuard]
  F -->|LAN trunk 802.1Q a 2.5 GbE| S[Zyxel XMG1915-10E o 10EP: switching; routing VLAN non usato]
  F -->|NIC separata 1 GbE| D[DMZ 192.168.20.0/24: futura, inizialmente vuota]
  S -->|trunk e PoE| A1[AP 1]
  S -->|trunk e PoE| A2[AP 2]
  S -->|access VLAN 10| PC[Client fidati]
  S -->|access VLAN 30| H[Host sempre acceso: da individuare]
  S -->|access VLAN 30| N[NAS a orario: dati e backup, 1 GbE oggi]
  H --> DNS[AdGuard opzionale / monitoraggio leggero]
  H -. "solo dopo dimensionamento" .-> LAB[VM LAB isolate sulla VLAN 60]
  A1 --> WIFI[SSID CASA / IOT / OSPITI: a valle di OPNsense]
  A2 --> WIFI
  M -. "temporanea, non ispezionata da OPNsense" .-> OLDWIFI[Client Wi-Fi Seven]
  M -->|LAN 1 GbE, NAT singolo| PS5[PS5 fuori perimetro]
  ADM[Postazione amministrativa / VPN] -. "regole dedicate" .-> F
```

La DMZ è qui una porta fisica separata e non viene contemporaneamente duplicata come VLAN 20 sul trunk. Un eventuale consolidamento futuro sullo switch richiede una revisione esplicita. Per l'host con VM LAB si usa un trunk limitato alle VLAN necessarie e bridge virtuali distinti; la porta access disegnata rappresenta il caso iniziale con soli servizi. Non collegare una VM bersaglio contemporaneamente al bridge fidato. La Wi-Fi del Seven resta una rete upstream: OPNsense non ne vede i flussi e non può applicare le sue policy a quei client. È una scelta transitoria accettabile per dispositivi ordinari o legacy, non una protezione completa dell'intera abitazione.

## Decisioni del 07/10/2026

La casa si sviluppa in altezza su quattro piani. Al piano più alto stanno il Seven e lo switch, e con ogni probabilità il firewall, che va collegato a entrambi con cavi corti: la collocazione del firewall è da confermare. I due access point stanno ai due piani centrali, il terzo e il secondo, e il piano terra non ne ha. I cavi sono già predisposti: due cavi RJ45 partono da due porte dello switch e arrivano ciascuno a un AP, che ne prende anche l'alimentazione PoE. Lo switch è quindi lo XMG1915-10EP (ADR-017).

L'utente vuole i due AP in mesh. Con il collegamento cablato a entrambi, il requisito si traduce in una sola rete Wi-Fi con roaming fra i due AP, cioè stessi SSID, stesse chiavi e assistenza al passaggio del client da un AP all'altro, e non in un collegamento radio fra AP: il mesh senza fili serve agli AP che il cavo non raggiunge e dimezza la banda disponibile, mentre qui il cavo c'è. I nomi delle funzioni Zyxel che lo realizzano, in modalità Nebula o autonoma, e il supporto dei protocolli di roaming 802.11k, v e r sul modello scelto vanno verificati sulla scheda tecnica. La copertura del piano terra dall'AP del secondo piano è da misurare dopo l'installazione; un terzo AP resta la risposta solo se la misura la smentisce.

La rete ospiti resta separata dalla rete di casa anche sugli AP: l'SSID OSPITI è legato alla VLAN 50, l'AP isola i client fra loro e OPNsense nega dalla VLAN 50 ogni rete privata e le proprie interfacce, salvo DNS e DHCP. La Wi-Fi del Seven può restare accesa come rete esterna al perimetro, se all'utente serve: in quel caso la si dichiara fuori perimetro e non la si confonde con la rete ospiti, e sulla WAN di OPNsense non devono rispondere né l'interfaccia di gestione né altri servizi.

La PS5 si collega direttamente a una porta LAN del Seven, fuori dal perimetro di OPNsense: ha un NAT solo e non occupa una porta dello switch. Il Seven ha una porta LAN da 2,5 GbE, riservata alla WAN di OPNsense, e altre porte da 1 GbE, una delle quali va alla console. Il ragionamento, compreso il costo di UPnP sul Seven, è nel [documento sul doppio NAT](07-doppio-nat-dietro-modem-in-comodato.md). Un FRITZ!Box non si acquista: in nessuna posizione della catena migliora la topologia.

Il NAS resta nella VLAN 30 a 1 GbE, che per l'uso previsto non è un limite. Una scheda di rete Intel da 2,5 GbE è un'aggiunta economica possibile in un secondo momento, nello stesso slot previsto per la scheda Intel da 1 GbE della guida di montaggio. Il firewall ha tre porte secondo il verbale e l'utente lo ricorda verificato da terminale; l'identificazione con `pciconf -lv` e `ifconfig` resta comunque il primo passo della fase 2. Resta da fare il censimento dei client, distinguendo quelli che saranno cablati da quelli che resteranno in Wi-Fi.

## Segmenti proposti

| Segmento | VLAN | Subnet proposta | Funzione e criterio |
|---|---|---|---|
| WAN OPNsense | nessuna interna | 192.168.1.0/24 | transito dal modem, gestione casa fuori perimetro durante migrazione |
| Client fidati | 10 | 192.168.10.0/24 | PC e telefoni aggiornati; accesso ai servizi selezionati |
| DMZ fisica | non sul trunk iniziale | 192.168.20.0/24 | solo se nasce un servizio pubblico |
| Servizi / storage | 30 | 192.168.30.0/24 | host di servizio e NAS; gestione consentita da amministrazione |
| IoT / legacy | 40 | 192.168.40.0/24 | TV, dispositivi con supporto incerto, eventuali camere |
| Ospiti | 50 | 192.168.50.0/24 | Internet e infrastruttura strettamente necessaria |
| Esperimenti | 60 | 192.168.60.0/24 | test NovaSCM/PXE e pentest su copie sacrificabili |
| Gestione | 99 | 192.168.99.0/24 | switch, AP e interfacce amministrative; nessun SSID pubblico |

Sono sette domini logici contando DMZ e gestione, da attivare progressivamente. Nella prima fase bastano client, IoT/ospiti secondo bisogno e gestione; servizi e LAB arrivano quando esistono gli host. I gateway interni sono sul firewall. Sulla WAN privata va verificata l'opzione OPNsense che blocca reti private, per non scambiare il modem a monte per una sorgente illegittima. IPv6 va progettato con regole equivalenti oppure lasciato non distribuito finché collaudato; non basta aver filtrato IPv4.

## Contratto fra zone

La traduzione di questa tabella in alias e regole per interfaccia, nell'ordine in cui OPNsense le valuta, è nel documento [Regole fra le zone](08-regole-fra-le-zone.md). La politica proposta nega nuove connessioni fra zone salvo le eccezioni della tabella e consente il traffico di risposta degli stati ammessi. Gli alias dei servizi devono contenere destinazioni e porte specifiche, evitando una regola generica client-verso-server.

| Origine | Destinazione | Regola proposta |
|---|---|---|
| VLAN client / IoT / ospiti | DNS e NTP autorizzati | sole porte necessarie; eventuale AdGuard indicato esplicitamente |
| Client fidati | NAS e applicazioni | SMB/HTTPS o protocollo realmente usato; interfacce amministrative escluse |
| Postazione admin o peer VPN amministrativo | gestione e host | HTTPS/SSH e porte strettamente necessarie |
| Ospiti | Internet | accesso Internet, negazione reti locali e interfacce del firewall, isolamento fra client AP |
| IoT | Internet / servizio di controllo | eccezioni per produttore o funzione; nessun accesso generalizzato al NAS |
| LAB | bersagli LAB | ammesso nell'ambito di prova; altre VLAN negate; uscita Internet esplicita se necessaria |
| DMZ | LAN / gestione / storage | negato; eccezioni applicative valutate singolarmente |
| Monitor | apparati | ICMP, SNMP o endpoint autorizzati; nessuna facoltà implicita di amministrazione |

Tra dispositivi nella stessa VLAN il traffico può restare sullo switch e non attraversare OPNsense: il firewall di zona non impedisce lateralità interna. L'isolamento Wi-Fi degli ospiti e i firewall degli host fanno parte del collaudo. Casting e discovery multicast fra VLAN si aggiungono solo per un caso concreto; un relay mDNS generico indebolirebbe la separazione prevista.

## DNS e guasti

```mermaid
flowchart LR
  C[Client] -->|fase iniziale| U[Unbound su OPNsense]
  C -. "fase successiva" .-> A[AdGuard su host sempre acceso]
  A --> U
  U --> I[DNS ricorsivo o upstream scelto]
  N[NAS a orario] -. "non necessario alla catena DNS" .-> A
```

Il disegno delle fasi evita di dipendere da un host non ancora disponibile. La ridondanza richiede due servizi su domini di guasto differenti; due container nello stesso NAS non la forniscono. Per un guasto del singolo AdGuard si prepara una procedura di ritorno a Unbound, accettando esplicitamente l'eventuale sospensione temporanea del filtro. Non si introduce un DNS pubblico secondario fingendo che venga usato solo in emergenza. Dettagli nella [nota AdGuard](../../fonti/adguard-home.md).

## Prestazioni, accesso remoto e ripristino

Il link firewall-switch limita il traffico instradato tra VLAN e verso WAN alla sua capacità condivisa; i 2,5 GbE negoziati non provano throughput utile con IDS o VPN attivi. NAS con NIC Gigabit resta a Gigabit anche su porta multigigabit. Il traffico nella stessa VLAN può invece essere commutato localmente. Si misura prima routing di base, poi si valuta Suricata con un insieme limitato di regole, come indicato dalla [documentazione OPNsense](https://docs.opnsense.org/manual/ips.html).

Per l'accesso remoto iniziale si propone [WireGuard su OPNsense](https://docs.opnsense.org/manual/how-tos/wireguard-client.html): sul modem si inoltra la sola porta UDP scelta alla WAN privata del firewall; sul firewall si configura il listener con la regola WAN. Non occorre una seconda traduzione verso un server se l'endpoint VPN è il firewall stesso. Le applicazioni interne non vengono tutte esposte. La prova si fa da una connessione esterna verificando handshake e servizi autorizzati, non con il port checker TCP degli screenshot.

Prima della migrazione si salvano configurazioni, mappa porte e cablaggio precedente, si mantiene accesso console e una porta di recupero configurata. Si sposta un solo client/AP alla volta, si verifica gestione e segmentazione, poi si migrano gli altri. Il Wi-Fi del modem si disattiva solo dopo il collaudo; lasciarlo attivo richiede dichiararlo esplicitamente come rete fuori dal firewall.
