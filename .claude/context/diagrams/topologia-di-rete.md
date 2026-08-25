---
generated-from-commit: e89779723cb1ed715b781763011255a81a82700e
generated-from-branch: main
generated-date: 2026-08-25
covers-paths:
  - docs/02-ftth-fastweb/**
  - docs/03-spunti-di-sviluppo/10-firewall-before-the-switch/**
  - docs/03-spunti-di-sviluppo/13-switch/**
last-verified-commit: 494b45e
---

# Topologia della rete

> Diagrammi testuali della catena WAN e della segmentazione interna, ricavati dalla documentazione sotto `docs/`. Sono versionati e diffabili, a differenza di un file di disegno binario. Lo schema definitivo in draw.io resta da produrre e non sostituisce questi diagrammi: li affianca.

## La catena fisica, com'e' oggi

Questa e' la catena imposta dal vincolo dell'operatore, non una scelta di progetto. La fibra termina su una presa ottica, da li' una bretella ottica raggiunge il terminale di rete ottico che converte in Ethernet, e da quel punto in avanti e' rete dati normale.

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
                          |
                 porta LAN 2,5 Gbps
                          |
              [ FIREWALL OPNsense 25.7 ]
```

Il modem non puo' essere messo in bridge: l'interfaccia non espone modalita' bridge, ne' passthrough PPPoE, ne' passthrough VLAN. L'ONT accetta traffico solo dal MAC del modem dell'operatore, quindi non si puo' nemmeno superarlo collegandosi direttamente. Le due cose insieme rendono il doppio NAT strutturale e non eliminabile senza cambiare contratto o apparato.

## Il firewall e la segmentazione interna, come sara'

Tre interfacce fisiche, tre zone. La disposizione delle velocita' non e' vincolata dal ruolo logico: la scelta di mettere la DMZ sulla gigabit integrata dipende dal fatto che il servizio esposto non ha bisogno di banda multigigabit, non da un vincolo dell'apparato.

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
   LAN 2,5 Gbps                            DMZ 1 Gbps
   192.168.10.1/24                         192.168.20.1/24
        |                                        |
        |                              [ server esposto ]
        |                               port forwarding
        |                               dalla WAN, nessun
        |                               accesso verso la LAN
        |
  [ SWITCH Zyxel XMG1915-10E ]  managed L2, 8 porte 2,5 GbE + 2 SFP+ 10 Gbps
        |            |              |               |
    porta access  porta access  porta access    porta PoE via
    VLAN 10       VLAN 10       VLAN 30         iniettore Cudy PoE200H
        |            |              |               |
      PC/NAS      workstation    storage        [ ACCESS POINT ]
                                                 piano inferiore
                                                 tutto il Wi-Fi passa
                                                 dal firewall
```

Lo switch non instrada: e' di livello 2 e trasporta soltanto. La porta che va al firewall e' configurata come trunk 802.1Q, le porte verso i dispositivi come access, e il firewall crea un'interfaccia logica per ogni VLAN sopra l'unica interfaccia fisica che lo collega allo switch. Il routing fra VLAN, il NAT verso Internet e ogni regola di sicurezza vivono solo sul firewall. L'assenza di routing di livello 3 sullo switch non e' un limite in questo scenario, perche' non esiste traffico fra VLAN che debba evitare il firewall.

## Il piano di indirizzamento previsto

Gli indirizzi privati sono scelte di progetto e restano in chiaro nella documentazione: non sono raggiungibili dall'esterno e sostituirli renderebbe illeggibile la segmentazione.

| Zona | Rete | Ruolo |
|---|---|---|
| WAN del firewall | 192.168.1.0/24, gateway 192.168.1.254 | rete privata del modem, non e' Internet |
| LAN principale | 192.168.10.0/24 | postazioni, NAS, access point |
| DMZ | 192.168.20.0/24 | server esposto verso l'esterno |
| Storage o server | 192.168.30.0/24 | ipotesi di terza VLAN interna, indirizzo statico previsto per il NAS |

Il piano a VLAN 10, 20 e 30 compare in due varianti nel documento sorgente, una senza firewall con la segmentazione fatta sul modem e una con il firewall come unico punto di decisione. Solo la seconda e' coerente con la topologia adottata; la prima resta come analisi dello scenario alternativo.

## Il buco noto

Nella configurazione attuale, con il firewall a valle del modem, la Wi-Fi generata dal modem e' interna alla LAN del modem stesso e non attraversa il firewall. Ogni dispositivo wireless connesso a quella rete e' quindi fuori dal perimetro controllato, e continuera' a esserlo finche' gli access point a valle dello switch non saranno installati e la radio del modem non sara' spenta o ridotta a rete ospite. Questo e' il motivo per cui gli access point non sono un accessorio del progetto ma la sua chiusura: senza di essi la segmentazione copre il cablato e lascia scoperto il wireless, che e' il segmento con la superficie d'attacco piu' ampia.

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
        +-- NO (l'ONT e' vincolato al MAC del modem;
        |       confermato dall'assistenza e da una prova di terzi)
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
        +-- Solo l'indirizzo LAN del modem: 192.168.1.254/24.
                E' il gateway della WAN del firewall.
```
