# [TBC] L'interfaccia del Seven su 192.168.1.254, voce per voce

Censimento dell'autore delle voci dell'interfaccia web del Fastweb Seven, riscritto l'8/10/2026 come documento tecnico di progetto (ADR-020): ogni pagina conserva la descrizione originale della voce e vi aggiunge come quella voce si imposta nella topologia adottata. Fino a quella data la lettura tecnica stava in un documento separato, ora assorbito qui. I valori che identificano la linea restano anonimizzati, con l'indirizzo pubblico nel segnaposto `203.0.113.10`. Nessuna impostazione descritta è ancora stata applicata. La marcatura resta da chiarire perché diverse voci hanno il solo titolo e alcune schermate vanno rifatte.

## Il ruolo del Seven nella topologia

Nella catena ONT, Seven, OPNsense il Seven fa quattro cose che nessun altro apparato può fare al suo posto: termina la sessione con l'operatore, tiene l'indirizzo pubblico statico, fa il primo NAT[^1] e porta la fonia sulle due porte telefoniche. Tutto il resto delle sue funzioni, cioè Wi-Fi, condivisioni, DHCP[^2] per la casa, inoltri verso i client, diventa nel progetto o superfluo o limitato a quanto serve ai pochi dispositivi che restano fuori dal perimetro di OPNsense. Il criterio con cui si legge il menu è quindi uno solo: ogni funzione del Seven che resta attiva agisce su una rete che OPNsense non vede, e va accesa solo se serve a qualcosa che sta su quella rete.

Fuori dal perimetro, collegati al Seven, restano tre soggetti. La WAN di OPNsense, sulla porta LAN 4, l'unica a 2,5 GbE. La PS5, su una porta LAN da 1 GbE (ADR-018). E i client della Wi-Fi del Seven, finché la radio resta accesa. La rete che li unisce è la `192.168.1.0/24` del Seven, ed è a tutti gli effetti la zona esterna del progetto: il perché del doppio NAT che ne deriva è spiegato nel [documento didattico dedicato](../../03-spunti-di-sviluppo/23-studio-home-lab/07-doppio-nat-dietro-modem-in-comodato.md).

## Una premessa sulla rilevazione

Le schermate censite sono state catturate mentre la fibra non portava traffico, nel periodo del guasto seguito dal ticket del 28/02/2026, come l'autore aveva già osservato nella [prima lettura dei parametri di accesso](../07-tbc-new-i-parametri-di-accesso-wan-su-ont/02-prima-lettura-pre-durante-fix-ticket-28022026-da-rifare.md). Nella tabella dello stato WAN l'interfaccia GPON[^3] risulta abilitata ma giù, mentre la connessione mobile LTE risulta su da oltre dieci giorni e porta l'indirizzo pubblico e i DNS dell'operatore. I valori della pagina Internet e dello stato WAN descrivono quindi il collegamento di riserva, non la linea in fibra. Prima del collaudo del firewall le schermate di stato vanno rifatte con la GPON su, verificando che l'indirizzo pubblico statico sia lo stesso sui due collegamenti: se non lo fosse, l'inoltro della VPN smetterebbe di funzionare proprio quando il modem passa alla riserva.

## Contenuti

- [Panoramica](01-panoramica-not-of-interest-here.md): i dispositivi collegati, utile per censire i client da migrare
- [Telefono](02-telefono-not-of-interest-here.md): la fonia, che resta invariata
- [Internet](03-internet.md): inoltri, host esposto, DNS, DDNS e UPnP
- [Wi-fi](04-wi-fi-not-of-interest-here.md): la rete esterna al perimetro e la sua rete ospiti
- [Impostazioni](05-impostazioni.md): rete locale, prenotazioni DHCP, servizi da spegnere
- [Stato e supporto](06-stato-e-supporto.md): i valori rilevati e che cosa dicono

I nomi dei file conservano la marcatura `not-of-interest-here` della prima stesura perché i nomi sono stabili e rinominarli romperebbe i collegamenti; il giudizio è invece cambiato, e ciascuna pagina dice perché quella voce conta.

## La configurazione del Seven, in ordine di esecuzione

Prima del collaudo del firewall si rifanno le schermate dello stato WAN con la GPON su, dello stato LAN e della sezione LAN switch, e si annota il firmware. Al collaudo si collega la WAN di OPNsense alla porta LAN 4, si crea la prenotazione DHCP del suo indirizzo e si verifica che la porta negozi 2,5 GbE. Quando la VPN su OPNsense è pronta si aggiunge l'inoltro della sola porta UDP di WireGuard verso quell'indirizzo, e si prova da una rete esterna. Si spengono la rete guest del Seven, le condivisioni e la modalità ECO. Per la PS5 si prenota l'indirizzo e si scrivono gli inoltri statici; si accende UPnP solo se il tipo di NAT resta insufficiente. Dopo il collaudo dei due AP si decide la radio del Seven: spenta, oppure tenuta come rete esterna dichiarata, con i canali coordinati con quelli degli AP.

Restano invariati l'indirizzo e il DHCP della LAN del Seven, il suo firewall, i DNS dell'operatore sul modem e la fonia.

[^1]: *NAT*, Network Address Translation: riscrittura degli indirizzi dei pacchetti che attraversano un router.

[^2]: *DHCP*, Dynamic Host Configuration Protocol: assegnazione automatica degli indirizzi; la prenotazione lega un indirizzo fisso a un dispositivo.

[^3]: *GPON*, Gigabit-capable Passive Optical Network: la tecnologia della fibra fino all'ONT, con velocità di linea nominali di 2,488 Gbps in discesa e 1,244 Gbps in salita, condivise fra le utenze dello stesso ramo ottico.
