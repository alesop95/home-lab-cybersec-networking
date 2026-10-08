# Accesso amministrativo: tre ingressi, tre barriere

Ritorno allo [studio](README.md). Documento di progetto dell'8/10/2026, che sviluppa la decisione dell'utente registrata come ADR-025: firewall, switch, access point e NAS si amministrano soltanto dalla workstation designata, dalla porta di recupero della VLAN 99 e dal tunnel WireGuard. Le regole di rete corrispondenti sono in [Regole fra le zone](08-regole-fra-le-zone.md). Nulla è ancora configurato; i punti da verificare sull'apparato sono marcati come tali.

## Il principio: chi non deve amministrare non deve nemmeno arrivare alla porta

Un'interfaccia di amministrazione protetta solo da una password è raggiungibile da chiunque stia in rete, e la password è l'unica cosa fra un dispositivo compromesso e il controllo della casa. Il progetto mette tre barriere in serie. La prima è di rete: da qualunque punto che non sia uno dei tre ingressi, le porte di amministrazione non rispondono, perché il firewall blocca il traffico e perché i servizi di gestione non ascoltano sugli indirizzi delle altre zone. La seconda è l'autenticazione: chi arriva alla porta deve ancora presentare credenziali forti. La terza è il registro: ogni tentativo bloccato lascia una traccia. Ciascuna barriera copre un difetto delle altre, ed è la ragione per cui nessuna da sola basta.

## I tre ingressi

| Ingresso | Dove sta | Come è riconosciuto | Quando si usa |
|---|---|---|---|
| Workstation ADMIN | VLAN 10, cablata | indirizzo fisso dato dal DHCP in base al suo MAC, alias `ADMIN` | amministrazione ordinaria da casa |
| Porta di recupero | porta 8 dello switch, VLAN 99, al piano più alto | si collega fisicamente un portatile con indirizzo statico nella VLAN 99 | emergenza, quando una regola sbagliata chiude fuori dagli altri due |
| Tunnel WireGuard | rete `192.168.98.0/24` | chiave del singolo dispositivo | amministrazione da fuori casa |

Tutto converge su un unico indirizzo di gestione per apparato, nella VLAN 99. Il firewall risponde all'amministrazione soltanto sul suo indirizzo della VLAN 99, `192.168.99.1`; switch e access point hanno l'indirizzo di gestione solo nella VLAN 99; il NAS, che sta nella VLAN 30 per i dati, ha un secondo indirizzo nella VLAN 99 riservato alla gestione. La workstation ADMIN e i peer del tunnel raggiungono quegli indirizzi attraverso il firewall, che lo consente soltanto a loro.

## Prima barriera: la rete

### Il firewall ascolta solo dove deve

OPNsense permette di scegliere su quali interfacce ascolta l'interfaccia web, con l'impostazione *Listen Interfaces* nelle opzioni di amministrazione, e lo stesso per il servizio SSH; la documentazione avverte di usare con cautela la restrizione su SSH (S79). Si seleziona la sola VLAN 99. Ne segue che l'interfaccia web non esiste sugli indirizzi `192.168.10.1`, `192.168.40.1`, `192.168.50.1` e sugli altri gateway: un client della VLAN 40 che prova ad aprirla non trova nessun servizio in ascolto, anche prima che una regola lo blocchi. È la ragione per cui la regola 3 della VLAN 10 fa passare la workstation ADMIN verso l'indirizzo della VLAN 99 e non verso il gateway della VLAN 10.

Il pacchetto della workstation entra nel firewall dall'interfaccia della VLAN 10 ed è destinato a un indirizzo del firewall stesso sulla VLAN 99. OPNsense lo valuta con le regole della VLAN 10, cioè dell'interfaccia da cui entra, e consegna la connessione al servizio che ascolta su `192.168.99.1`. La workstation non deve avere un indirizzo nella VLAN 99 per farlo.

### Switch e access point

Lo switch ha l'interfaccia di gestione nella sola VLAN 99, e le porte verso la workstation e verso gli altri client non portano la VLAN 99. Gli access point ricevono un trunk con la VLAN 99 come rete di gestione e le VLAN 10, 40 e 50 per gli SSID: l'indirizzo dell'AP sta nella 99, gli SSID non lo espongono. Su entrambi si disattivano i protocolli di gestione in chiaro, cioè HTTP e Telnet, se presenti, lasciando HTTPS e SSH. Come si chiamano queste impostazioni sull'XMG1915 e sul NWA130BE si verifica sui manuali al momento della configurazione.

### Il NAS

Il NAS sta nella VLAN 30 per servire i file. Per la gestione si propone una porta trunk sullo switch, con la VLAN 30 senza etichetta e la VLAN 99 con etichetta, un'interfaccia VLAN 99 su TrueNAS e l'interfaccia web legata al solo indirizzo della VLAN 99. Serve perché il traffico fra due host della stessa VLAN non passa dal firewall: senza questo accorgimento, qualunque futuro host della VLAN 30 raggiungerebbe l'interfaccia web del NAS senza che nessuna regola lo veda. La possibilità di legare l'interfaccia web di TrueNAS a un indirizzo specifico si verifica sulla versione installata.

### Le regole che lo realizzano

Nelle regole della VLAN 10, la terza consente al solo alias `ADMIN` le porte TCP 22 e 443 verso `192.168.99.1`, la VLAN 99 e l'indirizzo di gestione del NAS; le regole successive bloccano tutto il resto verso le reti interne e verso il firewall. Sull'interfaccia WireGuard, la seconda regola fa lo stesso per la rete del tunnel. Sulla VLAN 99, la porta di recupero raggiunge il firewall direttamente nella sua rete. Nessun'altra zona ha una regola verso le porte di gestione.

## Seconda barriera: l'autenticazione

Sul firewall si crea un utente amministratore personale e non si usa `root` per il lavoro ordinario, come raccomanda la documentazione (S79). L'interfaccia web chiede la password più un codice TOTP: OPNsense lo implementa secondo RFC 6238 con un server di autenticazione locale con codice a tempo, compatibile con le app di autenticazione comuni, e la documentazione precisa che il secondo fattore copre l'intero sistema tranne la console e SSH (S80). Per questo SSH accetta solo chiavi: si disattivano l'accesso di `root` e quello con password, e la chiave pubblica della workstation e del portatile di recupero si registra sull'utente amministratore (S79). L'interfaccia web si serve solo in HTTPS, con HSTS attivo, che secondo la documentazione impedisce al browser di accettare un certificato non valido anche in caso di intercettazione (S79), e con un tempo di scadenza delle sessioni inattive.

Su switch, access point e NAS si cambiano le credenziali di fabbrica prima di collegarli alla rete definitiva, con password lunghe diverse fra loro, conservate in un gestore di password e non in un file del progetto. Lo SNMP che l'host di servizio leggerà dagli apparati usa, dove disponibile, la versione 3 con autenticazione; se un apparato offre solo la versione 2c, la sua stringa di accesso si tratta come una password e la regola limita comunque le letture al solo host di servizio.

## Il punto debole dichiarato: l'identità della workstation

La workstation ADMIN è riconosciuta dal suo indirizzo IP, che il DHCP le assegna in base al MAC. Un dispositivo nella VLAN 10 che si attribuisse lo stesso indirizzo, o lo stesso MAC, passerebbe la prima barriera. Il progetto lo accetta per tre ragioni. Dietro la prima barriera resta la seconda, cioè password, codice a tempo e chiavi SSH, che un impostore non ha. La prenotazione DHCP su OPNsense può essere accompagnata da una voce ARP statica, che lega l'indirizzo al MAC sul firewall e rende inservibili le risposte a chi usa l'indirizzo con un altro MAC; il nome esatto dell'opzione si verifica sulla versione installata. E la VLAN 10 ospita solo dispositivi fidati. Sulla workstation va disattivato l'indirizzo hardware casuale di Windows per la rete di casa, altrimenti la prenotazione smette di riconoscerla. Il passo successivo, se servisse, è l'autenticazione 802.1X della porta della workstation sullo switch, da verificare sull'XMG1915.

## Il tunnel WireGuard

L'istanza WireGuard vive su OPNsense, ascolta su una porta UDP alta e non predefinita, e ha come indirizzo del tunnel `192.168.98.1/24`. Ogni dispositivo che deve entrare è un peer distinto, con la propria chiave pubblica, una chiave condivisa aggiuntiva e un solo indirizzo, `192.168.98.N/32`, come indica la guida ufficiale (S82). Lato dispositivo, il tunnel porta soltanto le reti da amministrare, cioè la VLAN 99 e l'indirizzo del NAS, e non `0.0.0.0/0`: il traffico Internet del dispositivo non passa dal tunnel, e per questo non serve la regola di NAT in uscita che la guida prevede per i tunnel completi. La regola WAN consente la porta del tunnel verso l'indirizzo WAN del firewall, come nella guida (S82), e sul Seven c'è l'unico inoltro verso quell'indirizzo.

WireGuard non ha un secondo fattore proprio: la chiave del dispositivo è la sola credenziale per entrare nel tunnel, e dentro il tunnel le interfacce di gestione chiedono comunque password, codice a tempo e chiave SSH. Un dispositivo perso si revoca togliendo il suo peer da OPNsense, che è immediato.

## La porta di recupero

La porta 8 dello switch è un'access della VLAN 99, al piano più alto. Ci si collega un portatile con un indirizzo statico della VLAN 99, e da lì si raggiunge il firewall anche se una regola sbagliata ha chiuso fuori la workstation e il tunnel. Il rischio è l'accesso fisico, accettabile in casa. Se si vuole ridurlo, la porta si spegne dallo switch e si riaccende quando serve, sapendo che in quel caso un errore che chiude fuori anche dallo switch obbliga alla console del firewall.

## L'ordine in cui si attiva, per non chiudersi fuori

OPNsense crea da sé una regola anti-lockout che tiene aperta l'interfaccia web sulla prima LAN; dove si disattiva va verificato nelle impostazioni di amministrazione della versione installata. La sequenza è questa. Si configurano utente, codice a tempo e chiavi SSH mentre l'anti-lockout è ancora attiva. Si crea la VLAN 99, si collega il portatile alla porta di recupero e si verifica l'accesso da lì. Si aggiunge la regola della workstation ADMIN e la si prova. Si attiva WireGuard e lo si prova da una rete esterna. Solo dopo che i tre ingressi funzionano si restringono le interfacce in ascolto alla VLAN 99 e si disattiva l'anti-lockout. In ogni momento la console fisica del firewall resta l'ultima via di ritorno.

## Terza barriera: il registro

Le regole che bloccano il traffico verso le reti interne e verso il firewall scrivono nel registro. Un tentativo di raggiungere una porta di gestione da una zona che non deve compare lì, e con il monitoraggio della fase 5 diventerà un allarme. Senza registro una barriera di rete ferma i tentativi ma non li fa vedere.

## Collaudo

Dalla workstation ADMIN l'interfaccia web e SSH del firewall rispondono su `192.168.99.1`. Da un altro PC della VLAN 10 non risponde nulla, né su `192.168.99.1` né sul gateway `192.168.10.1`, e il registro mostra il blocco. Da un telefono della VLAN 50 nessuna porta di gestione risponde. Dal portatile sulla porta di recupero il firewall risponde. Da un telefono fuori casa, con il tunnel attivo, il firewall risponde, e senza tunnel non risponde nulla. Un accesso SSH con password fallisce anche dalla workstation, e uno con chiave riesce.
