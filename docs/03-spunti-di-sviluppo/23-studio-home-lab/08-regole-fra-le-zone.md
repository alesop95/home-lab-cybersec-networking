# Regole fra le zone, in forma di configurazione OPNsense

Ritorno allo [studio](README.md). Documento di progetto dell'8/10/2026: traduce il contratto fra zone di [Architettura proposta](01-architettura.md) in alias e regole per interfaccia, nella forma in cui si inseriranno in OPNsense. È una proposta da collaudare regola per regola alla fase 2 e 3 della roadmap, non una configurazione applicata. Gli indirizzi sono quelli di progetto, privati; gli indirizzi dei singoli host marcati come proposta si confermano con le prenotazioni DHCP.

## Come le valuta OPNsense

Le regole stanno sull'interfaccia da cui il traffico entra nel firewall: una regola sulla VLAN 10 decide che cosa i client della VLAN 10 possono aprire, non che cosa possono ricevere. Dentro un'interfaccia le regole si leggono dall'alto e vince la prima che corrisponde; se nessuna corrisponde il traffico è bloccato. Il filtro è a stati, quindi una connessione permessa in un verso porta con sé le risposte e non servono regole di ritorno. Le regole di sistema che OPNsense aggiunge da sé, come quelle per il DHCP sulle interfacce dove il servizio è attivo, restano e non si riscrivono.

Due conseguenze guidano l'ordine. I permessi verso le reti interne vanno prima del blocco generico delle reti interne, che va prima del permesso verso Internet: è il modo di dire "Internet sì, il resto della casa no" con una regola sola per ciascuna delle due cose. E il traffico fra due dispositivi della stessa VLAN resta sullo switch e non passa dal firewall: nessuna regola lo vede, e l'isolamento dentro una VLAN si ottiene sugli AP o sugli host.

## Alias

Gli alias danno un nome a un insieme di indirizzi o di porte, così che una regola si legga e si modifichi in un punto solo.

| Alias | Tipo | Contenuto | Uso |
|---|---|---|---|
| RETI_INTERNE | reti | 192.168.10.0/24, 192.168.20.0/24, 192.168.30.0/24, 192.168.40.0/24, 192.168.50.0/24, 192.168.60.0/24, 192.168.99.0/24, rete WireGuard | il blocco generico verso il resto della casa |
| NAS | host | 192.168.30.10, proposta | destinazione dei servizi di condivisione |
| GESTIONE | host | 192.168.99.1 del firewall, indirizzi di switch e AP, 192.168.99.10 del NAS, proposte | dove ascoltano le interfacce di amministrazione, tutte nella VLAN 99 |
| HOST_SERVIZI | host | 192.168.30.20, proposta; macchina da individuare | DNS filtrante e monitoraggio, quando esisterà |
| ADMIN | host | workstation della VLAN 10 con prenotazione DHCP, più la rete WireGuard | chi può amministrare |
| WG_RETE | rete | 192.168.98.0/24, proposta | indirizzi dei peer WireGuard |
| PORTE_CONDIVISIONE | porte | TCP 445, TCP 443 | SMB e interfaccia web delle applicazioni del NAS |
| PORTE_GESTIONE | porte | TCP 22, TCP 443 | SSH e interfacce web di firewall, switch, AP e NAS |
| PORTE_BASE | porte | TCP e UDP 53, UDP 123 | DNS e NTP |

La rete WireGuard va scelta in modo che non coincida con le reti più comuni degli alberghi e degli uffici da cui ci si collegherà, che sono spesso `192.168.0.0/24` e `192.168.1.0/24`: per questo la proposta è `192.168.98.0/24`.

## Regole per interfaccia

In tutte le tabelle "Firewall" è l'alias predefinito di OPNsense per gli indirizzi del firewall stesso, e "Internet" si ottiene come destinazione "qualsiasi" dopo il blocco di RETI_INTERNE.

### WAN

| # | Azione | Protocollo | Origine | Destinazione | Porte | Motivo |
|---|---|---|---|---|---|---|
| 1 | consenti | UDP | qualsiasi | indirizzo WAN | porta WireGuard scelta | unico servizio raggiungibile da fuori, inoltrato dal Seven |

Tutto il resto entra nel blocco predefinito, e l'interfaccia di gestione non ascolta sulla WAN.

Le due opzioni di blocco della WAN restano attive, e sul punto la prima stesura di questo documento sbagliava. L'opzione *Block private networks* scarta il traffico che arriva sulla WAN dichiarando come sorgente un indirizzo privato, e la documentazione di OPNsense dice che sulla WAN quel traffico non dovrebbe esistere legittimamente (S78). La prima stesura ne chiedeva la disattivazione perché la WAN sta nella rete privata del Seven, ma l'opzione guarda la sorgente di chi apre la connessione, non l'indirizzo della WAN. Il traffico di risposta, cioè il Seven che risponde al firewall come gateway, al DHCP o al controllo del collegamento, appartiene a connessioni aperte dal firewall, ed è consentito dagli stati o, per il DHCP, dalle regole di sistema che OPNsense crea per il client DHCP della WAN. L'unico traffico in ingresso voluto è WireGuard, che arriva con l'indirizzo pubblico del dispositivo remoto, perché l'inoltro del Seven riscrive la destinazione e non la sorgente. L'opzione blocca invece ciò che non deve passare: un dispositivo della rete del Seven, la PS5 o un client della sua Wi-Fi, che provasse ad aprire una connessione verso il firewall. Si disattiverebbe solo se il Seven riscrivesse anche la sorgente del traffico inoltrato, cosa che si verifica al primo collaudo del tunnel guardando nel registro con quale sorgente arriva. *Block bogon networks* scarta le sorgenti mai assegnate o riservate, e resta attiva anch'essa.

### VLAN 10, client fidati

| # | Azione | Protocollo | Origine | Destinazione | Porte | Motivo |
|---|---|---|---|---|---|---|
| 1 | consenti | TCP/UDP | VLAN 10 | Firewall | PORTE_BASE | DNS e ora dal firewall |
| 2 | consenti | TCP | VLAN 10 | NAS | PORTE_CONDIVISIONE | file e applicazioni del NAS |
| 3 | consenti | TCP | ADMIN | GESTIONE | PORTE_GESTIONE | amministrazione solo dalla workstation designata, verso gli indirizzi della VLAN 99; il dettaglio è in [Accesso amministrativo](09-accesso-amministrativo.md) |
| 4 | blocca, con registro | qualsiasi | VLAN 10 | RETI_INTERNE | qualsiasi | il resto della casa |
| 5 | blocca, con registro | qualsiasi | VLAN 10 | Firewall | qualsiasi | altre porte del firewall |
| 6 | consenti | qualsiasi | VLAN 10 | qualsiasi | qualsiasi | Internet |

### VLAN 30, servizi e storage

| # | Azione | Protocollo | Origine | Destinazione | Porte | Motivo |
|---|---|---|---|---|---|---|
| 1 | consenti | TCP/UDP | VLAN 30 | Firewall | PORTE_BASE | DNS e ora |
| 2 | consenti | UDP | HOST_SERVIZI | VLAN 99 | 161 | lettura SNMP di switch e AP per il monitoraggio |
| 3 | blocca, con registro | qualsiasi | VLAN 30 | RETI_INTERNE | qualsiasi | un servizio non apre connessioni verso le altre zone |
| 4 | blocca, con registro | qualsiasi | VLAN 30 | Firewall | qualsiasi | altre porte del firewall |
| 5 | consenti | qualsiasi | VLAN 30 | qualsiasi | qualsiasi | aggiornamenti e servizi esterni |

### VLAN 40, IoT

| # | Azione | Protocollo | Origine | Destinazione | Porte | Motivo |
|---|---|---|---|---|---|---|
| 1 | consenti | TCP/UDP | VLAN 40 | Firewall | PORTE_BASE | DNS e ora |
| 2 | blocca, con registro | qualsiasi | VLAN 40 | RETI_INTERNE | qualsiasi | nessun accesso alla casa |
| 3 | blocca, con registro | qualsiasi | VLAN 40 | Firewall | qualsiasi | altre porte del firewall |
| 4 | consenti | qualsiasi | VLAN 40 | qualsiasi | qualsiasi | servizi del produttore |

Le eccezioni per il casting da un telefono della VLAN 10 a un televisore della VLAN 40 si aggiungono una alla volta quando servono, con porte e destinazione precise; un ripetitore mDNS generico fra le due VLAN annullerebbe la separazione.

### VLAN 50, ospiti

| # | Azione | Protocollo | Origine | Destinazione | Porte | Motivo |
|---|---|---|---|---|---|---|
| 1 | consenti | TCP/UDP | VLAN 50 | Firewall | 53 | solo DNS |
| 2 | blocca, con registro | qualsiasi | VLAN 50 | RETI_INTERNE | qualsiasi | nessun accesso alla casa |
| 3 | blocca, con registro | qualsiasi | VLAN 50 | Firewall | qualsiasi | nessun accesso al firewall |
| 4 | consenti | qualsiasi | VLAN 50 | qualsiasi | qualsiasi | Internet |

Sugli AP l'SSID OSPITI ha l'isolamento dei client attivo, perché due ospiti nella stessa VLAN non passano dal firewall.

### VLAN 60, laboratorio

| # | Azione | Protocollo | Origine | Destinazione | Porte | Motivo |
|---|---|---|---|---|---|---|
| 1 | consenti | TCP/UDP | VLAN 60 | Firewall | PORTE_BASE | DNS e ora |
| 2 | blocca, con registro | qualsiasi | VLAN 60 | RETI_INTERNE | qualsiasi | il laboratorio non tocca la casa |
| 3 | blocca, con registro | qualsiasi | VLAN 60 | qualsiasi | qualsiasi | nessuna uscita predefinita |

L'uscita verso Internet si apre con una regola esplicita, sopra la 3, per il tempo e le destinazioni di un esperimento, e si richiude dopo: macchine bersaglio vulnerabili per costruzione non escono da sole. Il progetto delle aperture è nella sezione che segue.

### Le aperture temporanee del laboratorio

Il laboratorio non ha uscita verso Internet, perché ospita macchine vulnerabili per costruzione e prove di intrusione: un bersaglio compromesso che potesse uscire diventerebbe un punto di partenza verso l'esterno o verso servizi di controllo remoto. Molti esperimenti però hanno bisogno di Internet per un tempo breve, per installare pacchetti, scaricare un'immagine o aggiornare un sistema. Il progetto prevede due aperture, preparate in anticipo, disattivate, ciascuna con il proprio limite.

| Apertura | Alias usati | Regola, sopra la 3 della VLAN 60 | Quando serve |
|---|---|---|---|
| A, aggiornamenti | `LAB_USCITA`: le macchine del laboratorio autorizzate; `LAB_REPOSITORY`: nomi di dominio dei repository, per esempio quelli di Debian, Ubuntu, Kali e del sistema dei contenitori | consenti TCP 80 e 443 da `LAB_USCITA` verso `LAB_REPOSITORY`, con registro | installare e aggiornare software, il caso più frequente |
| B, uscita libera | `LAB_USCITA` | consenti qualsiasi da `LAB_USCITA` verso qualsiasi destinazione, sotto la regola che blocca `RETI_INTERNE`, con registro | un esperimento che deve parlare con un servizio esterno preciso; mai con campioni di malware |

Le due regole esistono sempre e sono disattivate: OPNsense permette di disattivare una regola senza cancellarla proprio per le politiche usate di rado (S81). Per aprirne una le si associa una pianificazione oraria e la si attiva. Alla scadenza della pianificazione la regola smette di valere e OPNsense rimuove gli stati delle connessioni che aveva permesso (S81), quindi anche un download in corso si interrompe: è il comportamento voluto, perché un'apertura dimenticata si chiude da sola. Un alias di tipo host può contenere nomi di dominio, che il firewall risolve e aggiorna, ed è il modo di indicare i repository senza elencarne gli indirizzi; il comportamento esatto della risoluzione si verifica sulla versione installata.

Ogni apertura si annota nel registro del progetto con data, macchine, regola, durata e scopo, e dopo la chiusura si controlla nel registro del firewall che il traffico sia cessato. Le macchine che analizzeranno campioni sospetti, previste dalla fase 6 della roadmap, non stanno nella VLAN 60 ma in una zona isolata a parte, ancora da progettare, e non hanno aperture.

### VLAN 99, gestione

| # | Azione | Protocollo | Origine | Destinazione | Porte | Motivo |
|---|---|---|---|---|---|---|
| 1 | consenti | TCP/UDP | VLAN 99 | Firewall | PORTE_BASE | DNS e ora per switch e AP |
| 2 | consenti | TCP | VLAN 99 | Firewall | PORTE_GESTIONE | amministrazione dalla porta di recupero |
| 3 | blocca, con registro | qualsiasi | VLAN 99 | RETI_INTERNE | qualsiasi | gli apparati non aprono connessioni verso la casa |
| 4 | consenti | TCP | VLAN 99 | qualsiasi | 443 | aggiornamenti del firmware |

### DMZ

| # | Azione | Protocollo | Origine | Destinazione | Porte | Motivo |
|---|---|---|---|---|---|---|
| 1 | consenti | TCP/UDP | DMZ | Firewall | PORTE_BASE | DNS e ora |
| 2 | blocca, con registro | qualsiasi | DMZ | RETI_INTERNE | qualsiasi | la regola che rende la DMZ una DMZ |
| 3 | blocca, con registro | qualsiasi | DMZ | Firewall | qualsiasi | altre porte del firewall |
| 4 | consenti | qualsiasi | DMZ | qualsiasi | qualsiasi | aggiornamenti e chiamate esterne |

La DMZ resta vuota finché non nasce un servizio pubblico. Quel giorno servono due inoltri in serie, sul Seven e su OPNsense, e la regola WAN corrispondente, come spiega la [seconda lettura dei parametri di accesso](../../02-ftth-fastweb/07-tbc-new-i-parametri-di-accesso-wan-su-ont/03-tbc-seconda-lettura-parametri-di-interesse.md).

### WireGuard

| # | Azione | Protocollo | Origine | Destinazione | Porte | Motivo |
|---|---|---|---|---|---|---|
| 1 | consenti | TCP/UDP | WG_RETE | Firewall | PORTE_BASE | DNS attraverso il tunnel |
| 2 | consenti | TCP | WG_RETE | GESTIONE | PORTE_GESTIONE | amministrazione da fuori |
| 3 | consenti | TCP | WG_RETE | NAS | PORTE_CONDIVISIONE | file da fuori |
| 4 | blocca, con registro | qualsiasi | WG_RETE | qualsiasi | qualsiasi | nient'altro, compresa l'uscita verso Internet |

## Che cosa resta fuori dalle regole

La PS5 e i client della Wi-Fi del Seven stanno sulla rete del modem, fuori dal perimetro (ADR-018): nessuna di queste regole li riguarda, e la loro unica separazione dalla casa è la regola WAN, che non lascia entrare nulla oltre al tunnel. IPv6 non si distribuisce finché non esiste un insieme di regole equivalente. Il NAT in uscita resta automatico. La regola anti-lockout di OPNsense, che tiene aperta l'interfaccia di gestione sulla prima LAN, si toglie solo dopo aver provato l'accesso dalla VLAN 99 e dalla workstation ADMIN.

## Collaudo

Ogni regola si prova dalla zona che governa, con una prova che deve riuscire e una che deve fallire. Dalla VLAN 10: il NAS su SMB riesce, l'SSH del NAS da un host che non è ADMIN fallisce, un indirizzo della VLAN 40 non risponde. Dalla VLAN 50: Internet riesce, il firewall e il NAS no, un altro ospite no. Dalla VLAN 60 senza regola temporanea: nessuna uscita. Dalla rete del Seven: nessun servizio di OPNsense risponde tranne WireGuard. Ogni blocco deve comparire nel registro del firewall: una regola di blocco che non scrive niente non si può collaudare.
