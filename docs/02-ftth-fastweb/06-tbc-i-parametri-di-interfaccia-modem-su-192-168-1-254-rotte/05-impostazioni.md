# Impostazioni

## USB (not-of-interest-here)

## Condivisione Contenuti (not-of-interest-here)

## Condivisione della stampante (not-of-interest-here)

Le tre sezioni non sono state censite. Nel progetto i tre servizi si spengono: offrirebbero file e stampanti a una rete fuori dal perimetro, mentre lo storage della casa è il NAS nella VLAN 30.

## LAN IPv4

In questa pagina è possibile configurare gli indirizzi IPv4 della tua rete locale. Se si utilizza il DHCP, i dispositivi riceveranno un indirizzo tramite il server DHCP integrato nel modem. Se si utilizza un DHCP esterno, è possibile assegnare ai tuoi dispositivi indirizzi statici.

Nel progetto indirizzo, maschera e intervallo DHCP restano come sono: la rete `192.168.1.0/24` non si sovrappone a nessuna delle VLAN interne.

### Impostazioni di rete

Indirizzo IP del Gateway (caselle con valori: *192 - 168 - 1 - 254*)

Subnet Mask (caselle con valori: *255 - 255 - 255 - 0*)

Server DHCP (interruttore ON/OFF)

### Parametri del server DHCP

Primo indirizzo IP

(caselle con valori: 192 - 168 - 1 - 10)

Ultimo indirizzo IP

(caselle con valori: 192 - 168 - 1 - 250)

Durata

(menu a tendina con: 24 ore)

### Static DHCP - Home Network

Nome dispositivo | Indirizzo MAC | Indirizzo IP

(Nessuna regola impostata)

Nel progetto le prenotazioni diventano due: la WAN di OPNsense e la PS5, così che gli inoltri della pagina Internet puntino sempre allo stesso indirizzo. La prenotazione della WAN è il dettaglio da cui dipendono tutti gli inoltri: se dopo un riavvio la WAN prendesse un indirizzo diverso, la VPN smetterebbe di rispondere senza alcun messaggio d'errore. Se l'interfaccia ammette prenotazioni fuori dall'intervallo dinamico conviene un indirizzo basso come `192.168.1.2`, altrimenti un indirizzo dentro l'intervallo, prenotato; lo si verifica al collaudo.

## LAN switch (not-of-interest-here)

Sezione non censita. Va fotografata: se espone velocità o VLAN per porta, la porta LAN 4 va lasciata in negoziazione automatica a 2,5 GbE.

## Modalità ECO (not-of-interest-here)

Sezione non censita. La scheda del modello la descrive in due livelli, Light e Deep. Nel progetto resta spenta finché non si verifica che cosa spegne il livello Deep: non deve toccare la porta LAN 4 né la fonia.
