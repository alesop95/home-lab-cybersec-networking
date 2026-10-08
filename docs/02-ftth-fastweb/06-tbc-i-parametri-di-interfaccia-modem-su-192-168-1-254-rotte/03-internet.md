# Internet

## Port mapping

### Port Mapping

La funzionalità di Port Mapping permette a computer remoti di collegarsi a dispositivi specifici sulla LAN.

![](assets/img-0010.png)  ![](assets/img-0011.png)

Ci sono diverse opzioni settabili.

Nel progetto le regole sono due e nessuna di più. La prima inoltra la porta UDP scelta per WireGuard all'indirizzo prenotato della WAN di OPNsense, che termina il tunnel. La seconda serve alla PS5: inoltri statici verso l'indirizzo fisso della console, prenotato nel DHCP del Seven, con le porte prese dalla pagina di supporto del produttore al momento della configurazione e non da una lista ricopiata qui, perché cambiano nel tempo.

### Port Triggering

Sezione con il solo titolo nella prima stesura. Il port triggering apre una porta in ingresso dopo un traffico in uscita su un'altra porta. Nel progetto resta spento; la schermata va rifatta per confermarlo.

## Host pubblico (DMZ)

Nella schermata viene detto:

 Se c’è un dispositivo sulla LAN non accessibile tramite Internet dietro al NAT Firewall, puoi abilitare il traffico bidirezionale senza restrizioni configurandolo come Virtual Exposed Host.

Funzione DMZ:

(interruttore ON/OFF)

![](assets/img-0012.png)

Attenzione: utilizzando la funzionalità di “Exposed Host” si esclude il firewall del Gateway. Si prega quindi di assicurarsi che il dispositivo in oggetto sia protetto da eventuali attacchi da Internet, in quanto ossia esposto per il nome stesso esposte:

Sotto l'avviso, la prima trascrizione riportava una sequenza di numeri, un indirizzo della rete del Seven seguito da coppie di porte, che non corrisponde a nessun campo dell'interfaccia: è una lettura sbagliata della schermata, rimossa l'8/10/2026 nella riscrittura. Il valore da leggere è lo stato dell'interruttore, da ricontrollare sulla schermata.

Un dispositivo può essere autorizzato alla connessione bidirezionale ad Internet, per esempio per giochi online, videocamere o connessioni configurabili come “Exposed Host”, perché per questo il dispositivo deve avere un indirizzo IP statico

Indirizzo IP pubblico: 203.0.113.10.

Nel progetto l'host esposto è spento all'inizio. L'avviso dell'interfaccia è esatto ma va letto per intero: si esclude il firewall del Seven per l'host esposto e solo per lui, perché tutto il traffico non richiesto che arriva all'indirizzo pubblico viene consegnato a quell'host invece di essere scartato. Se l'host è la WAN di OPNsense la protezione passa interamente a OPNsense, che è ciò che il progetto vuole comunque; ma finché l'unico servizio raggiungibile da fuori è la VPN, l'inoltro di una porta sola lascia al Seven lo scarto di tutto il resto ed è la superficie più piccola. L'host esposto verso la WAN del firewall resta il candidato per quando la DMZ ospiterà un servizio pubblico. L'indirizzo pubblico riportato è quello del collegamento di riserva in uso alla rilevazione, come spiega la premessa del [README](README.md).

## DNS & DDNS

### DNS

La configurazione del DNS viene eseguita automaticamente quando ci si connette alla rete. In alternativa si può configurare manualmente il DNS sui propri dispositivi.

Nel progetto i DNS del Seven restano quelli dell'operatore e servono soltanto al modem e ai pochi dispositivi fuori dal perimetro. I client interni non li usano: interrogano Unbound su OPNsense, che risolve da sé o inoltra a un resolver scelto.

### DDNS

Il DDNS consente di accedere al proprio dispositivo tramite Internet utilizzando un nome di dominio invece di un indirizzo IP. È necessario avere un account con un DDNS Provider.

Nel progetto il DDNS non serve, perché l'indirizzo pubblico è statico.

## UPnP

Abilita l’UPnP per permettere ai dispositivi che lo supportano di effettuare varie azioni, ad esempio recuperare l'indirizzo IP esterno del dispositivo, elencare le regole di Port Mapping esistenti, cancellarle o aggiungerne.

Alla rilevazione UPnP risulta attivo, con le funzioni IGD Parental e IGD Device Finder accese nella pagina di stato. Nel progetto si spegne se la PS5 raggiunge un tipo di NAT accettabile con gli inoltri statici, e si accende solo se quelli non bastano. Il costo va dichiarato: con UPnP acceso qualunque dispositivo collegato al Seven, compresi i client della sua Wi-Fi, può aprirsi una porta verso Internet, mentre gli inoltri statici verso l'indirizzo della sola console non hanno questo effetto.
