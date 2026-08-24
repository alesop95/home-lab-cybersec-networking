# [TBC] Seconda lettura parametri di interesse

quando la voce GPON è Up e mostra un indirizzo IP reale. Solo in quel momento è possibile dedurre il protocollo di accesso utilizzato dalla linea……….

Nel caso specifico, dato il comportamento del modem Fastweb Seven e l’assenza di modalità bridge o passthrough nell’interfaccia mostrata, quei parametri non cambiano la conclusione architetturale. Il modem rimane il punto di accesso alla rete dell’ISP e quindi il primo router della catena.

In questo scenario specifico, cioè:

ONT → modem Fastweb → OPNsense → switch → access point

non serve conoscere alcun parametro della connessione FTTH per configurare OPNsense se la sessione con l’ISP viene terminata dal modem Fastweb, non da OPNsense. Tutti i parametri di accesso alla rete dell’operatore (protocollo, VLAN, autenticazione, ecc.) rimangono interni al modem e non devono essere replicati sul firewall.

L’unico dato utile da leggere nell’interfaccia del modem riguarda l’indirizzo IP della LAN del modem stesso. Questo è visibile nella sezione Stato e supporto → Informazioni generali → Rete LAN, dove compare “Indirizzo IP - 192.168.1.254/24”. Questo valore definisce la rete interna del modem.

Serve esclusivamente per configurare la WAN di OPNsense. L’interfaccia WAN del firewall dovrà ottenere un indirizzo nella stessa rete privata del modem (tipicamente via DHCP dal modem oppure tramite indirizzo statico nella rete 192.168.1.0/24). Il gateway della WAN di OPNsense sarà l’indirizzo del modem, cioè 192.168.1.254.

Tutti gli altri parametri della FTTH, compresi protocollo WAN, VLAN e configurazione GPON, non sono necessari in questa architettura perché il firewall non parla direttamente con l’ONT ma con il modem.

## I veri parametri che serve configurare in OPN sense

Quindi in questa architettura perché il firewall non parla direttamente con l’ONT ma con il modem, su OPN Sense su un PC con Intel i7-6700 @3,40 GHz, 16 GB di RAM DDR4 e SSD Crucial CT500P25SD8 con due schede di rete da 2,5Gbps e una per DMZ nel senso che ci attacco un server per dare un servizio all'esterno, la WAN di OPNsense è l’interfaccia fisica che viene collegata alla LAN del modem Fastweb.

Il modem rimane il router che possiede l’indirizzo IP pubblico e che parla con la rete dell’ISP. OPNsense quindi non vede l’ONT e non stabilisce alcuna sessione con l’operatore. Dal punto di vista di OPNsense la WAN non è Internet ma la rete privata del modem.

Di conseguenza la configurazione logica è questa. La porta WAN del firewall viene collegata alla porta LAN del modem Fastweb. L’interfaccia WAN di OPNsense riceve un indirizzo privato nella rete del modem, cioè nella rete 192.168.1.0/24. Il gateway della WAN diventa l’indirizzo del modem, cioè 192.168.1.254.

La porta LAN di OPNsense diventa la rete interna reale della propria infrastruttura. Qui si collega lo switch Zyxel e da quello partono tutti i dispositivi della rete, inclusi gli access point Wi-Fi.

La terza scheda di rete, quella destinata alla DMZ, è semplicemente un’altra interfaccia di livello 3 separata dalla LAN. Su quella rete si colloca il server che deve esporre servizi verso Internet. Il traffico in ingresso da Internet arriverà prima al modem Fastweb, verrà inoltrato all’IP WAN di OPNsense (tramite port forwarding o Exposed Host) e poi OPNsense potrà applicare NAT e regole firewall verso l’host nella DMZ.

In sintesi, con tre schede di rete sul firewall:

1. una interfaccia è WAN e parla con il modem
1. una interfaccia è LAN e parla con lo switch e gli access point
1. una interfaccia è DMZ e collega il server esposto verso Internet

Il modem resta il punto di uscita verso l’ISP, mentre OPNsense diventa il router e firewall reale della rete interna e della DMZ.

## Chiarimenti

### [TBC] La differenza tra port forwarding o Exposed Host (Fastweb seven)

Il traffico in ingresso da Internet arriverà prima al modem Fastweb, verrà inoltrato all’IP WAN di OPNsense (tramite port forwarding o Exposed Host)

	Considerando il menù sopra per come è fatto il Fastweb seven, che cambia?

### [TBC] La differenza tra le due DMZ in atto

Abbiamo visto che il modem Fastweb fornisce una funzione chiamata Exposed Host, di fatto una DMZ completa verso *un* dispositivo interno. In pratica tutte le porte in ingresso sull’IP pubblico vengono inoltrate verso un singolo host della LAN e nel caso in esame quell’host sarebbe l’interfaccia WAN di OPNsense.

Questa DMZ che fa il modem fastweb è diversa dalla DMZ che sta sulla scheda di rete da 1Gbps del firewall. cercare

	____________

Sembra si sì perché prima si diceva . Il traffico in ingresso da Internet arriverà prima al modem Fastweb, verrà inoltrato all’IP WAN di OPNsense (tramite port forwarding o Exposed Host) e poi OPNsense potrà applicare NAT e regole firewall verso l’host nella DMZ.
