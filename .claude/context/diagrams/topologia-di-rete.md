---
generated-from-commit: 86b5c8a61a55a48997d7757592aa4d91da9e8581
generated-from-branch: main
generated-date: 2026-08-25
covers-paths:
  - docs/02-ftth-fastweb/**
  - docs/03-spunti-di-sviluppo/10-firewall-before-the-switch/**
  - docs/03-spunti-di-sviluppo/13-switch/**
  - docs/03-spunti-di-sviluppo/23-studio-home-lab/**
last-verified-commit: ee63b19
---

# Topologia della rete

> Diagrammi testuali della catena WAN e della segmentazione interna, ricavati dalla documentazione sotto `docs/`. Sono versionati e diffabili, a differenza di un file di disegno binario. Lo schema definitivo in draw.io resta da produrre e non sostituisce questi diagrammi: li affianca.

## La catena fisica, com'è oggi

Questa è la catena imposta dal vincolo dell'operatore, non una scelta di progetto. La fibra termina su una presa ottica, da lì una bretella ottica raggiunge il terminale di rete ottico che converte in Ethernet, e da quel punto in avanti è rete dati normale.

```
                 rete dell'operatore
                          |
                       fibra GPON
                          |
                  [ PTO ] presa terminale ottica
                          |
                    bretella ottica
                          |
                  [ ONT ] Zyxel PM5100-T1, uscita Ethernet 2,5 Gbps
                          |
                     cavo RJ45
                          |
              [ MODEM operatore ] porta WAN 2,5 Gbps
                 termina la sessione con l'ISP
                 detiene l'IP pubblico statico 203.0.113.10
                 fa NAT verso 192.168.1.0/24
                 gestisce la fonia VoIP
                 espone una Wi-Fi 7 fuori dal perimetro del firewall
                 porta LAN da 1 GbE: PS5, fuori perimetro
                          |
                 porta LAN 4, l'unica a 2,5 Gbps
                          |
              [ FIREWALL OPNsense 25.7 ]
```

Il modem non può essere messo in bridge: l'interfaccia non espone modalità bridge, né passthrough PPPoE, né passthrough VLAN. Per la linea concreta in esame l'assistenza ha escluso il collegamento diretto dell'OPNsense all'ONT e una prova di terzi ha riferito un rifiuto del nuovo apparato; la documentazione pubblica Fastweb, però, descrive anche scenari con apparato proprio e non dichiara in modo generale un vincolo MAC dell'ONT. Il progetto tratta quindi il collegamento diretto come non verificato e non supportato per questa linea, mantenendo il percorso ONT -> Seven -> OPNsense. Il doppio NAT è il vincolo operativo di progetto.

## Il firewall e la segmentazione interna, come sarà

Tre interfacce fisiche, tre zone. La disposizione delle velocità non è vincolata dal ruolo logico: la scelta di mettere la DMZ sulla gigabit integrata dipende dal fatto che il servizio esposto non ha bisogno di banda multigigabit, non da un vincolo dell'apparato.

```
              [ MODEM operatore ] 192.168.1.254/24
                          |
                          | WAN del firewall, indirizzo privato nella rete del modem
                          | gateway della WAN: 192.168.1.254
                          |
  +----------------------[ OPNsense ]----------------------+
  |            i3 7a gen, 8 GB RAM, SSD 120 GB              |
  |   NIC integrata 1 GbE  +  2x TP-Link TX201 2,5 GbE      |
  +--------------------------------------------------------+
        |                                        |
   LAN 2,5 Gbps, trunk                     DMZ 1 Gbps
   gateway delle VLAN                      192.168.20.1/24
        |                                        |
        |                              [ server esposto ]
        |                               port forwarding
        |                               dalla WAN, nessun
        |                               accesso verso la LAN
        |
  [ SWITCH Zyxel XMG1915-10EP ]  8 porte 2,5 GbE PoE++ + 2 SFP+ 10 Gbps
        |  porta 1: trunk verso il firewall, VLAN 10/30/40/50/60/99
        |
   porte 2-3      porta 4      porta 5      porta 6       porta 7      porta 8
   trunk e PoE    access 10    access 30    trunk 30-99   access 10    access 99
        |             |            |            |             |            |
   [ AP 1 piano 3 ] client     [ NAS ]     host servizi  workstation   recupero
   [ AP 2 piano 2 ] cablato    1 GbE       Proxmox, proposto
   SSID CASA 10, IOT 40, OSPITI 50: tutto il Wi-Fi degli AP passa dal firewall
```

Dal 07/10/2026 la variante è decisa (ADR-017): XMG1915-10EP con due AP, senza iniettore e senza terzo AP. ADR-018 colloca i due AP, cablati e alimentati in PoE, al terzo e al secondo dei quattro piani, e mette la PS5 su una porta LAN da 1 GbE del Seven, fuori dal perimetro. Il disegno aggiornato è `docs/03-spunti-di-sviluppo/23-studio-home-lab/topologia-proposta.svg`. Il paragrafo che segue resta come storia della scelta. La variante dello switch era una scelta aperta dal 22/09/2026, documentata nello [studio switch e AP](../../../docs/03-spunti-di-sviluppo/23-studio-home-lab/03-switch-e-access-point-zyxel.md): la 10EP con PoE integrato è il candidato principale per due o tre AP, la 10E senza PoE con un iniettore resta sensata se l'AP è uno solo. Il diagramma mostra la prima. Lo switch avrebbe funzioni di livello 3 limitate, interfacce IP per VLAN e rotte statiche, ma non si usano: trasporta soltanto. La porta che va al firewall è configurata come trunk 802.1Q, le porte verso i dispositivi come access, e il firewall crea un'interfaccia logica per ogni VLAN sopra l'unica interfaccia fisica che lo collega allo switch. Il routing fra VLAN, il NAT verso Internet e ogni regola di sicurezza vivono solo sul firewall. Non usare il routing di livello 3 dello switch non è un limite in questo scenario, perché non esiste traffico fra VLAN che debba evitare il firewall.

## Il piano di indirizzamento previsto

Gli indirizzi privati sono scelte di progetto e restano in chiaro nella documentazione: non sono raggiungibili dall'esterno e sostituirli renderebbe illeggibile la segmentazione.

| Zona | Rete | Ruolo |
|---|---|---|
| WAN del firewall | 192.168.1.0/24, gateway 192.168.1.254 | rete privata del modem, non è Internet |
| VLAN 10, client fidati | 192.168.10.0/24 | postazioni e telefoni, SSID CASA |
| DMZ, porta fisica | 192.168.20.0/24 | server esposto verso l'esterno, vuota finché non serve |
| VLAN 30, servizi e storage | 192.168.30.0/24 | NAS a indirizzo statico e host di servizio |
| VLAN 40, IoT | 192.168.40.0/24 | televisori e dispositivi con supporto incerto, SSID IOT |
| VLAN 50, ospiti | 192.168.50.0/24 | solo Internet, SSID OSPITI |
| VLAN 60, laboratorio | 192.168.60.0/24 | esperimenti e macchine bersaglio |
| VLAN 99, gestione | 192.168.99.0/24 | switch, AP e interfacce amministrative |

Il piano a VLAN 10, 20 e 30 compare in due varianti nel documento sorgente, una senza firewall con la segmentazione fatta sul modem e una con il firewall come unico punto di decisione. Solo la seconda è coerente con la topologia adottata; la prima resta come analisi dello scenario alternativo. Lo studio del 22/09/2026 ha esteso il piano alle VLAN 40, 50, 60 e 99, e il 07/10/2026 il NAS è stato collocato nella 30 (ADR-018).

## Il buco noto

Nella configurazione attuale, con il firewall a valle del modem, la Wi-Fi generata dal modem è interna alla LAN del modem stesso e non attraversa il firewall. Ogni dispositivo wireless connesso a quella rete è quindi fuori dal perimetro controllato, e continuerà a esserlo finché gli access point a valle dello switch non saranno installati e la radio del modem non sarà spenta o ridotta a rete ospite. Questa rete upstream può essere tollerata temporaneamente per dispositivi ordinari o legacy, ma non va presentata come copertura di sicurezza dell'intera abitazione. Gli access point a valle dello switch chiudono il buco: senza di essi la segmentazione copre il cablato e lascia scoperto il wireless.

Dal 07/10/2026 la chiusura è decisa: due AP cablati ai piani centrali (ADR-017, ADR-018). Resta fuori dal perimetro per scelta la PS5, sulla porta LAN da 1 GbE del modem, e può restare la Wi-Fi del modem come rete esterna dichiarata, decisione rimandata dall'utente.

## Diagramma della sequenza di decisione sulla WAN

Serve per non ripercorrere ogni volta il ragionamento quando ci si chiede se il firewall possa diventare l'apparato di frontiera.

```
Il modem si puo' mettere in bridge?
        |
        +-- NO (verificato: nessuna voce nell'interfaccia)
        |
        v
Il firewall si puo' collegare direttamente all'ONT?
        |
        +-- NON VERIFICATO SULLA LINEA (assistenza e prova di terzi
        |       indicano un rifiuto; le pagine pubbliche non provano
        |       un vincolo MAC generale)
        |
        v
Allora il modem resta l'apparato di frontiera.
        |
        v
Servono i parametri di accesso WAN (protocollo e VLAN ID) ?
        |
        +-- NO, perche' la sessione con l'ISP la termina il modem.
                Servirebbero solo se un giorno il firewall parlasse con l'ONT.
        |
        v
Che cosa serve sapere, allora?
        |
        +-- L'indirizzo LAN effettivo del Seven e la prenotazione
                DHCP della WAN del firewall, da rilevare prima del collaudo.
        |
        +-- Lo stato WAN con la fibra attiva: le schermate del censimento
                sono state prese sul collegamento LTE di riserva.
```
