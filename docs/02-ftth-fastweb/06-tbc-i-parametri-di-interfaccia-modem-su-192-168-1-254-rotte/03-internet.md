# Internet

## Port mapping

### Port Mapping

La funzionalità di Port Mapping permette a computer remoti di collegarsi a dispositivi specifici sulla LAN.

![](assets/img-0010.png)  ![](assets/img-0011.png)

Ci sono diverse opzioni settabili.

### Port Triggering

## Host pubblico (DMZ)

Nella schermata viene detto:

 Se c’è un dispositivo sulla LAN non accessibile tramite Internet dietro al NAT Firewall, puoi abilitare il traffico bidirezionale senza restrizioni configurandolo come Virtual Exposed Host.

Funzione DMZ:

(interruttore ON/OFF)

![](assets/img-0012.png)

Attenzione: utilizzando la funzionalità di “Exposed Host” si esclude il firewall del Gateway. Si prega quindi di assicurarsi che il dispositivo in oggetto sia protetto da eventuali attacchi da Internet, in quanto ossia esposto per il nome stesso esposte:

192.168.1.100, 8000:4000-> 49188, 8888:79584, 6844:2254, 82:1:500

Un dispositivo può essere autorizzato alla connessione bidirezionale ad Internet, per esempio per giochi online, videocamere o connessioni configurabili come “Exposed Host”, perché per questo il dispositivo deve avere un indirizzo IP statico

Indirizzo IP pubblico: 203.0.113.10.

## DNS & DDNS

### DNS

La configurazione del DNS viene eseguita automaticamente quando ci si connette alla rete. In alternativa si può configurare manualmente il DNS sui propri dispositivi.

### DDNS

Il DDNS consente di accedere al proprio dispositivo tramite Internet utilizzando un nome di dominio invece di un indirizzo IP. È necessario avere un account con un DDNS Provider.

## UPnP

Abilita l’UPnP per permettere ai dispositivi che lo supportano di effettuare varie azioni, ad esempio recuperare l'indirizzo IP esterno del dispositivo, elencare le regole di Port Mapping esistenti, cancellarle o aggiungerne.
