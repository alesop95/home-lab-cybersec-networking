# Introduzione concettuale tecnica

A livello fisico si è in presenza di FTTH, Fiber To The Home, con terminazione ottica su ONT, Optical Network Terminal. L’ONT converte il segnale GPON o XGS-PON in Ethernet rame. Da quel punto in avanti la configurazione è puramente Ethernet e IP, ma ciò che transita sull’interfaccia Ethernet può essere incapsulato su VLAN specifica e autenticato con protocolli differenti.

Tutto questo deve quindi comunque presuppone contattare l’assistenza tecnica Fastweb o aprire ticket dall’area clienti chiedendo esplicitamente i parametri di accesso WAN su ONT. La richiesta deve includere: tecnologia FTTH attiva sulla linea, protocollo di autenticazione (PPPoE o IPoE DHCP), presenza e valore della VLAN Internet, credenziali PPPoE se previste.

Per configurare correttamente la terminazione WAN su ONT in presenza di IP statico assegnato dall’operatore è necessario disporre dei parametri di livello 2 e livello 3 effettivamente utilizzati sulla linea FTTH. Se è PPPoE servono username, password e l’eventuale VLAN ID sulla WAN.

In generale, poichè serve capire come la FTTH viene incapsulata, le combinazioni reali sono solo queste:

1. IPoE senza VLAN → DHCP direttamente sulla porta WAN.
1. IPoE con VLAN → DHCP ma solo se il traffico è taggato con l’ID corretto.
1. PPPoE senza VLAN → sessione PPPoE direttamente su Ethernet.
1. PPPoE con VLAN → prima VLAN, sopra quella la sessione PPPoE.

L’impatto pratico è che la VLAN, se richiesta, è obbligatoria indipendentemente dal fatto che sia DHCP o PPPoE; se nella configurazione del firewall  Se sbagli o non metti il VLAN ID, non ottieni né lease DHCP né sessione PPPoE anche se username e password sono corretti. Pertanto, l’informazione minima necessaria dall’assistenza è duplice e concatenata: quale protocollo di accesso viene utilizzato sulla linea FTTH attiva e se tale protocollo transita su una VLAN specifica, con relativo VLAN ID. Solo con questi parametri di livello 2 e 3 è possibile configurare in modo corretto e ripetibile l’interfaccia WAN su OPNsense dietro ONT. Senza entrambe le informazioni non si può configurare in modo deterministico la WAN di OPNsense.

Il primo elemento determinante è il protocollo di accesso a livello 3. PPPoE, Point-to-Point Protocol over Ethernet, prevede instaurazione di una sessione autenticata tramite username e password e genera un’interfaccia logica con negoziazione di parametri IP. IPoE, IP over Ethernet, utilizza tipicamente DHCP, Dynamic Host Configuration Protocol, senza sessione PPP e senza credenziali applicative, salvo eventuali vincoli MAC o opzioni DHCP specifiche lato operatore.

Il secondo elemento, indipendente dal primo, è la VLAN Internet. VLAN significa Virtual LAN, identificata da un VLAN ID numerico nel tag 802.1Q. Se l’operatore consegna il servizio su VLAN specifica, il traffico WAN deve essere taggato con quell’ID. In assenza del corretto VLAN ID il traffico non viene accettato a monte: nel caso DHCP non viene rilasciato alcun lease perché le richieste non raggiungono il server dell’operatore; nel caso PPPoE non viene instaurata alcuna sessione perché i pacchetti PADI/PADO non transitano sul dominio corretto. Username e password corretti risultano irrilevanti se il traffico è incapsulato sulla VLAN sbagliata o non taggato.

La richiesta di IP statico non elimina la necessità di conoscere protocollo e VLAN. Anche un IP statico può essere consegnato via PPPoE o via IPoE con DHCP riservato o assegnazione statica lato operatore. Senza sapere se l’IP statico è legato a una sessione PPPoE oppure a un lease DHCP vincolato, non è possibile impostare correttamente l’interfaccia WAN. Nel caso PPPoE l’IP statico viene assegnato all’interno della sessione autenticata: dopo login PPP, il BRAS dell’operatore assegna sempre lo stesso indirizzo pubblico a quelle credenziali. Nel caso IPoE con DHCP vincolato non esiste sessione PPP. Il firewall invia una richiesta DHCP e il server dell’operatore rilascia sempre lo stesso IP pubblico perché è associato a un identificativo di livello 2 o 3, tipicamente il MAC address della WAN o un Option 82 lato rete di accesso. L’IP è quindi “statico” per policy lato operatore, ma tecnicamente viene consegnato tramite lease DHCP rinnovabile.

## Approfondimento su topologia di rete ipotizzata insieme a modem

La configurazione proposta:

ONT → WAN modem Fastweb → LAN modem → WAN OPNsense

è architetturalmente corretta e viene utilizzata spesso quando il modem dell’operatore non può essere sostituito. In questo schema il modem Fastweb continua a gestire autenticazione e accesso alla rete dell’ISP mentre OPNsense diventa il vero router e firewall interno.

### Double-NAT

Con le informazioni disponibili dall’interfaccia del modem Fastweb Seven e dalle voci di menu fornite, non compare alcuna opzione che consenta una modalità bridge reale della WAN, né funzionalità equivalenti come PPPoE passthrough o VLAN passthrough quindi uno deve assumere che, in assenza di queste capacità, il modem rimane necessariamente il dispositivo che stabilisce la sessione WAN con l’ISP e quindi il primo punto di NAT della rete. Se una di queste due funzioni fosse presente, l’architettura potrebbe essere diversa. In quel caso il firewall potrebbe diventare il dispositivo che stabilisce la sessione WAN reale. Il flusso diventerebbe, concettualmente:

ONT → firewall OPNsense → modem (solo Wi-Fi o switch)

oppure il modem potrebbe essere eliminato del tutto. Nel modem Fastweb Seven, dalle schermate fornite, non compare alcuna funzione di questo tipo. Non compare bridge mode, non compare PPPoE passthrough, non compare VLAN passthrough. Di conseguenza il modem è obbligatoriamente il dispositivo che termina la connessione con la rete Fastweb.

Questo porta alla topologia ONT → modem Fastweb → OPNsense → switch → access point in cui si risolve la wi-fi protetta con l’access point proprietario.

Il problema principale di questa architettura non è tecnico ma quindi conseguentemente, di livello NAT. Il modem Fastweb effettua Network Address Translation tra l’indirizzo pubblico e la rete privata 192.168.1.0/24. OPNsense a sua volta effettuerà NAT tra la sua LAN e la WAN privata ricevuta dal modem. Si crea quindi una configurazione detta double NAT.

La presenza di un IP pubblico statico riduce alcuni problemi operativi perché consente di esporre servizi tramite port forwarding, ma il traffico deve comunque attraversare due livelli di traduzione.

Il modem Fastweb fornisce una funzione chiamata Exposed Host. Questa funzione è di fatto una DMZ completa verso un dispositivo interno. In pratica tutte le porte in ingresso sull’IP pubblico vengono inoltrate verso un singolo host della LAN. Nel caso in esame quell’host sarebbe l’interfaccia WAN di OPNsense. Non elimina il NAT perché il modem continua comunque a tradurre l’indirizzo IP pubblico verso un indirizzo privato della sua LAN, ad esempio 192.168.1.x. La funzione Exposed Host inoltra semplicemente tutte le porte verso quell’indirizzo interno, ma la traduzione degli indirizzi rimane attiva nel modem. Di conseguenza OPNsense riceve traffico già NATtato sulla propria interfaccia WAN privata e applica un secondo NAT verso la propria LAN. Questo è il vero motivo per cui la topologia rimane tecnicamente una configurazione di double NAT. In ogni caso, se configurata correttamente, questa soluzione fa sì che tutto il traffico in ingresso venga gestito dal firewall OPNsense e non dal firewall del modem. Non elimina tecnicamente il NAT del modem, ma riduce il problema operativo perché il firewall reale diventa OPNsense.

### Wi-fi (conferma architettura ipotizzata)

Nel modello in cui OPNsense è collegato alla LAN del modem, la Wi-Fi del modem rimane fuori dal firewall perché è bridgiata internamente alla LAN del modem stesso. Il traffico Wi-Fi non attraversa OPNsense ma il NAT del modem.

Questo è esattamente il problema architetturale che è stato identificato. Non dipende dal fatto che il modem sia proprietario o meno, dipende dal fatto che il modem è il router che autentica la linea FTTH.

Per far passare la Wi-Fi attraverso il firewall esistono solo due architetture reali:

1. utilizzare access point collegati alla LAN di OPNsense (come individuato in precedenza)
1. utilizzare il modem in modalità bridge reale

Il modem Fastweb Seven non espone una modalità bridge completa. Non è possibile verificarlo direttamente dalla documentazione mostrata perché quella voce non compare nella configurazione, ma non appare alcuna impostazione tipica come bridge mode, PPPoE passthrough o VLAN passthrough.

Questo significa che si può assumere che l’unica architettura corretta possibile e coerente con ciò che è stato descritto, è la 1):

ONT → modem Fastweb (autenticazione ISP) → OPNsense → switch → access point

In questa configurazione il Wi-Fi non deve provenire dal modem ma da access point collegati allo switch gestito da OPNsense. In questo modo tutto il traffico, cablato e wireless, passa attraverso il firewall.

Lo switch citato, Zyxel XMG1915-10E, è coerente con questo schema perché dispone di porte 2.5 GbE e può funzionare come switch di distribuzione verso access point e dispositivi cablati.

Se gli access point sono collegati alla LAN di OPNsense, il traffico dei client Wi-Fi entra prima nello switch, poi nell’interfaccia LAN del firewall OPNsense e viene filtrato dalle sue regole prima di uscire verso la WAN. In questo schema l’access point è solo un bridge di livello 2 (IEEE 802.11 ↔ Ethernet) e non fa routing né NAT; di conseguenza il traffico wireless viene trattato dal firewall esattamente come quello di un dispositivo cablato.

Il doppio NAT rimane tra OPNsense e il modem Fastweb, ma non cambia il fatto che tutto il traffico proveniente dagli access point passi attraverso OPNsense prima di arrivare a Internet (e viceversa agli endpoint privati domestici).

### Extra: WAN con firewall diretto su ONT o modem sostituito (teoria)

Questa è solo una riflessione per capire come si configura una WAN direttamente su un firewall collegato all’ONT. In altre parole, è la descrizione di cosa servirebbe sapere se si volesse sostituire il modem o collegarsi direttamente alla linea.

Per determinare come configurare correttamente la WAN su OPNsense dietro ONT servono soltanto i parametri che descrivono il livello 2 e il livello 3 della connessione attiva sulla fibra. Tutto il resto dell’interfaccia del modem è irrilevante per questo scopo.

1. Il primo parametro è il tipo di protocollo di accesso utilizzato sulla WAN FTTH. Deve risultare chiaramente se la sessione è stabilita tramite DHCP oppure tramite PPPoE. Questo è un parametro di livello 3, cioè il metodo con cui il dispositivo ottiene l’indirizzo IP pubblico dall’ISP.
- Stato e supporto → Stato WAN → Dettagli connessione WAN
- In questa schermata compare la tabella con le interfacce GPON, LTE/MBB1 e UMTS. Qui si leggono due parametri essenziali: il tipo di connessione indicato nella colonna “Tipo” e lo stato dell’interfaccia indicato nella colonna “Stato”. Quando la linea FTTH è realmente in uso, la riga GPON deve risultare Up e nella stessa riga comparirà il tipo di protocollo utilizzato per ottenere l’indirizzo IP.
1. Il secondo parametro è l’eventuale VLAN utilizzata tra ONT e modem. Questo è un parametro di livello 2 della rete Ethernet. Se presente, serve conoscere il VLAN ID con cui il traffico Internet viene taggato prima di uscire verso l’ONT.
- Stato e supporto → Stato WAN → Dettagli connessione WAN.
- Nella seconda tabella sottostante, chiamata “Dettagli connessione WAN”, si trovano i campi “Indirizzo IP”, “Maschera IPv4” e “Server DNS”. Questi valori sono quelli assegnati alla WAN dal provider e confermano il metodo di assegnazione dell’IP quando la GPON è attiva.
1. Il terzo parametro utile è l’interfaccia WAN reale su cui la connessione fibra è stabilita. Nel caso del modem Fastweb Seven deve risultare attiva l’interfaccia GPON e non quella LTE/MBB. Solo quando GPON risulta Up e possiede un indirizzo IP è possibile leggere i parametri corretti della linea FTTH.
- Stato e supporto → Stato GPON
- Questa schermata mostra lo stato fisico del collegamento in fibra e le velocità massime del link ottico. Non contiene il protocollo IP ma serve per verificare che la connessione GPON sia realmente attiva.
1. Il quarto parametro utile è il metodo di assegnazione dell’indirizzo IP sulla WAN quando la GPON è attiva. Questo dato conferma operativamente il protocollo di accesso perché apparirà come DHCP client attivo oppure come sessione PPPoE stabilita.
1. Il quinto parametro, se visibile, è l’eventuale presenza di VLAN tagging nella configurazione WAN. Alcuni firmware mostrano esplicitamente VLAN ID o 802.1Q nella pagina WAN o nelle informazioni avanzate della connessione.

Questi cinque elementi sono gli unici necessari per capire se un firewall collegato direttamente all’ONT possa funzionare e come dovrebbe essere configurata la sua interfaccia WAN. Tutti gli altri parametri dell’interfaccia del modem non influenzano questa decisione architetturale.

Tuttavia, per quanto riguarda la VLAN, nel menu che è stato riportato non compare alcuna voce dove sia visibile un VLAN ID della WAN. Questo significa che, con l’interfaccia mostrata, tale parametro non è esposto nella configurazione utente del modem. Non è quindi possibile leggerlo da quelle schermate.
