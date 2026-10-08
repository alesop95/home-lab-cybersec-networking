# Il Fastweb Seven nel progetto di rete, voce per voce

> Documento tecnico di progetto del 07/10/2026. Riprende le voci dell'interfaccia web del Seven censite dall'autore in [I parametri di interfaccia modem](06-tbc-i-parametri-di-interfaccia-modem-su-192-168-1-254-rotte/README.md) e nella [scheda del modello](02-modem/02-fastweb-seven-modello-fibra.md), e per ciascuna dice che cosa fa, che valore aveva alla rilevazione e come va impostata nella topologia adottata. I valori reali che identificano la linea restano anonimizzati: l'indirizzo pubblico è il segnaposto `203.0.113.10`. Nessuna impostazione qui descritta è ancora stata applicata.

## Il ruolo del Seven nella topologia

Nella catena ONT, Seven, OPNsense il Seven fa quattro cose che nessun altro apparato può fare al suo posto: termina la sessione con l'operatore, tiene l'indirizzo pubblico statico, fa il primo NAT[^1] e porta la fonia sulle due porte telefoniche. Tutto il resto delle sue funzioni, cioè Wi-Fi, condivisioni, DHCP[^2] per la casa, inoltri verso i client, diventa nel progetto o superfluo o limitato a quanto serve ai pochi dispositivi che restano fuori dal perimetro di OPNsense. Il criterio con cui si legge il menu è quindi uno solo: ogni funzione del Seven che resta attiva agisce su una rete che OPNsense non vede, e va accesa solo se serve a qualcosa che sta su quella rete.

Fuori dal perimetro, collegati al Seven, restano tre soggetti. La WAN di OPNsense, sulla porta LAN da 2,5 GbE. La PS5, su una porta LAN da 1 GbE (ADR-018). E i client della Wi-Fi del Seven, finché la radio resta accesa. La rete che li unisce è la `192.168.1.0/24` del Seven, ed è a tutti gli effetti la zona esterna del progetto: il perché del doppio NAT che ne deriva è spiegato nel [documento didattico dedicato](../03-spunti-di-sviluppo/23-studio-home-lab/07-doppio-nat-dietro-modem-in-comodato.md).

## Una premessa sulla rilevazione

Le schermate censite dall'autore sono state catturate in un momento in cui la fibra non portava traffico. Nella tabella dello stato WAN l'interfaccia GPON[^3] risulta abilitata ma giù, con zero secondi di connessione, mentre la connessione mobile LTE risulta su da oltre dieci giorni e porta l'indirizzo pubblico e i DNS dell'operatore. I valori della sezione Internet e dello stato WAN descrivono quindi il collegamento di riserva, non la linea in fibra. Prima del collaudo del firewall la sezione Stato e supporto va rifotografata con la GPON su, e in particolare va verificato che l'indirizzo pubblico statico sia lo stesso su entrambi i collegamenti: se non lo fosse, l'inoltro della VPN smetterebbe di funzionare proprio quando il modem passa alla riserva.

## Internet

| Voce | Che cosa fa | Rilevato | Impostazione di progetto |
|---|---|---|---|
| Port Mapping | inoltra una porta pubblica a un host della LAN del Seven | nessuna regola documentata | una regola UDP per WireGuard verso l'indirizzo prenotato della WAN di OPNsense; regole statiche verso la PS5 se servono al tipo di NAT |
| Port Triggering | apre una porta in ingresso dopo un traffico in uscita su un'altra porta | sezione vuota nel censimento | spento; da fotografare per confermarlo |
| Host pubblico (DMZ) | inoltra tutte le porte a un solo host, escludendo il firewall del Seven per quell'host | interruttore presente, stato non chiaro dalla trascrizione | spento all'inizio; candidato futuro verso la WAN di OPNsense se la DMZ ospiterà un servizio pubblico |
| DNS | i DNS che il Seven usa e distribuisce | DNS dell'operatore, assegnati automaticamente | invariato: i client interni usano Unbound su OPNsense, che risolve da sé o inoltra a un resolver scelto, non il Seven |
| DDNS | lega un nome di dominio a un indirizzo che cambia | non configurato | non serve: l'indirizzo pubblico è statico |
| UPnP | lascia ai dispositivi della LAN del Seven la creazione di inoltri | attivo, con le funzioni IGD Parental e Device Finder accese nello stato | spento se la PS5 raggiunge un tipo di NAT accettabile con le regole statiche; acceso solo se quelle non bastano, sapendo che ogni dispositivo del Seven potrebbe aprirsi porte |

La voce Host pubblico merita una riga di spiegazione in più, perché l'avviso dell'interfaccia dice che con l'Exposed Host si esclude il firewall del Gateway. È vero per l'host esposto e solo per lui: tutto il traffico non richiesto che arriva all'indirizzo pubblico viene consegnato a quell'host invece di essere scartato dal Seven. Se l'host è la WAN di OPNsense, la protezione passa interamente a OPNsense, che è quello che il progetto vuole comunque. Finché l'unico servizio raggiungibile da fuori è la VPN, però, un inoltro di una porta sola lascia al Seven lo scarto di tutto il resto, ed è la superficie più piccola.

Le regole per la PS5 vanno scritte verso un indirizzo fisso della console, prenotato nel DHCP del Seven. Le porte vanno prese dalla pagina di supporto del produttore al momento della configurazione e non da una lista ricopiata qui, perché cambiano nel tempo.

## Wi-Fi

| Voce | Che cosa fa | Rilevato | Impostazione di progetto |
|---|---|---|---|
| Generale | SSID, sicurezza, unione delle radio per MLO | due radio unite, WPA2 e WPA3 | se la radio resta accesa: solo WPA3 dove i client lo reggono, password diversa da tutte quelle degli AP interni; altrimenti spenta |
| Rete guest | SSID ospiti in sola navigazione, con spegnimento a tempo | attiva in sola navigazione, con timer di durata | spenta: gli ospiti usano l'SSID OSPITI degli AP, nella VLAN 50 isolata da OPNsense |
| Programmazione | accensione e spegnimento della Wi-Fi per fasce orarie | impostata il 27/04/2026 | mantenibile se la radio resta accesa; non è un controllo di sicurezza |
| Impostazioni radio | standard ammessi, canale, larghezza di banda | modalità mixed su entrambe le bande, canale 10 a 20 MHz e canale 36 a 80 MHz | da coordinare con gli AP: i canali del Seven non devono sovrapporsi a quelli dell'AP del piano 3, il più vicino |
| Filtro MAC | ammette o esclude client per indirizzo MAC | sezione vuota nel censimento | non usato: un indirizzo MAC si imita, non è un controllo d'accesso |
| Easy Mesh | estende la rete del Seven con nodi aggiuntivi, come il Seven Booster | sezione vuota nel censimento | non usato: la copertura della casa la danno gli AP Zyxel, dentro il perimetro; un Booster estenderebbe la rete esterna |
| Analizzatore | analisi dei canali radio | sezione vuota nel censimento | utile una volta, prima di scegliere i canali degli AP |

La decisione sulla radio del Seven è rimandata dall'utente (ADR-018), e le due strade si configurano in modo diverso. Spenta, la rete esterna si riduce a due cavi e la questione si chiude. Accesa, la Wi-Fi del Seven diventa una rete dichiaratamente esterna, utile per esempio per collegarsi al modem senza passare dal firewall: va tenuta con un SSID che non si confonda con quelli interni, e nessun dispositivo di casa vi si deve associare per abitudine, perché da lì non è né protetto né segmentato.

## Impostazioni

| Voce | Che cosa fa | Rilevato | Impostazione di progetto |
|---|---|---|---|
| USB, Condivisione contenuti, Condivisione stampante | servizi di condivisione sulla LAN del Seven | non documentati, marcati non rilevanti | spenti: offrirebbero servizi a una rete fuori dal perimetro, e il NAS è dentro |
| LAN IPv4 | indirizzo del Seven, maschera, DHCP | `192.168.1.254/24`, DHCP attivo da `.10` a `.250`, durata 24 ore | invariato: la rete non si sovrappone a nessuna delle VLAN interne |
| Static DHCP | prenotazioni per indirizzo MAC | nessuna regola | due prenotazioni: la WAN di OPNsense e la PS5, così che gli inoltri puntino sempre allo stesso indirizzo |
| LAN switch | impostazioni delle porte LAN | non documentato | da fotografare: se espone velocità o VLAN per porta, la porta 4 va lasciata in negoziazione automatica a 2,5 GbE |
| Modalità ECO | riduzione dei consumi in due livelli | non documentata | spenta, finché non si verifica che cosa spegne il livello Deep: non deve toccare la porta LAN 4 né la fonia |

La prenotazione della WAN di OPNsense è il dettaglio da cui dipendono tutti gli inoltri: se la WAN prendesse dal DHCP un indirizzo diverso dopo un riavvio, la VPN smetterebbe di rispondere senza alcun messaggio d'errore. Se l'interfaccia del Seven ammette prenotazioni fuori dall'intervallo dinamico, conviene un indirizzo basso come `192.168.1.2`; altrimenti un indirizzo dentro l'intervallo, prenotato. Lo si verifica sull'interfaccia al momento del collaudo.

## Stato e supporto

| Voce | Che cosa mostra | Rilevato | Uso nel progetto |
|---|---|---|---|
| Informazioni generali, Internet | indirizzo pubblico, gateway, DNS, firewall, IPv6 | firewall attivo; IPv6 assente, solo link-local | il firewall del Seven resta attivo; con IPv6 assente la WAN di OPNsense non chiede IPv6 e la casa resta solo IPv4 finché l'operatore non delega un prefisso |
| Informazioni generali, Rete LAN | stato delle porte, DHCPv6, router advertisement | LAN 3 attiva a 1 Gbps, LAN 4 attiva a 2,5 Gbps; DHCPv6 e RA accesi | la LAN 4 è la porta da 2,5 GbE e va alla WAN di OPNsense; la PS5 va su una delle porte da 1 GbE |
| Informazioni generali, Wi-Fi | SSID, sicurezza, canale, banda | due radio attive, WPA2 e WPA3 | riferimento per il coordinamento dei canali con gli AP |
| Informazioni generali, Sistema | seriale, firmware, hardware | firmware rilevato; seriale e tipo hardware anonimizzati | il firmware si annota a ogni rilevazione: un aggiornamento remoto dell'operatore può cambiare il comportamento delle voci qui sopra |
| Stato WAN | interfacce di accesso e loro stato | GPON giù, LTE su, vedi premessa | da rifotografare con la GPON su |
| Stato LAN | dettaglio della LAN | mancante nel censimento | da fotografare |
| Stato GPON | stato e velocità massime della fibra | velocità massima 1240 Mbps in un verso e 2490 Mbps nell'altro | sono le velocità di linea della GPON, condivise sul ramo ottico: il tetto teorico è circa 2,5 Gbps in ricezione e 1,25 Gbps in trasmissione, e la velocità reale va misurata |
| Fonia, Diagnostica, Riavvio, Info | servizi accessori | non rilevanti | fonia invariata; la diagnostica serve solo in caso di guasto |

Il router advertisement e il DHCPv6 accesi sulla LAN del Seven, in assenza di un prefisso globale, distribuiscono al più configurazioni locali. Non disturbano OPNsense se la sua WAN è configurata senza IPv6, che è la scelta coerente con lo stato rilevato.

## La configurazione del Seven in sintesi, in ordine di esecuzione

Prima del collaudo del firewall si rifotografano lo stato WAN con la GPON su, lo stato LAN e la sezione LAN switch, e si annota il firmware. Al collaudo si collega la WAN di OPNsense alla porta LAN 4, si crea la prenotazione DHCP del suo indirizzo e si verifica che la porta negozi 2,5 GbE. Quando la VPN su OPNsense è pronta si aggiunge l'inoltro della sola porta UDP di WireGuard verso quell'indirizzo, e si prova da una rete esterna. Si spengono la rete guest del Seven, le condivisioni e la modalità ECO. Per la PS5 si prenota l'indirizzo e si scrivono gli inoltri statici; si accende UPnP solo se il tipo di NAT resta insufficiente. Dopo il collaudo dei due AP si decide la radio del Seven: spenta, oppure tenuta come rete esterna dichiarata, con i canali coordinati con quelli degli AP.

Restano invariati l'indirizzo e il DHCP della LAN del Seven, il suo firewall, i DNS dell'operatore sul modem e la fonia.

[^1]: *NAT*, Network Address Translation: riscrittura degli indirizzi dei pacchetti che attraversano un router.

[^2]: *DHCP*, Dynamic Host Configuration Protocol: assegnazione automatica degli indirizzi; la prenotazione lega un indirizzo fisso a un dispositivo.

[^3]: *GPON*, Gigabit-capable Passive Optical Network: la tecnologia della fibra fino all'ONT, con velocità di linea nominali di 2,488 Gbps in discesa e 1,244 Gbps in salita, condivise fra le utenze dello stesso ramo ottico.
