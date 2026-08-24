# Mini-PC x86 (VM virtuale) con pfSense (VPN server)

un mini-PC x86 con pfSense è una scelta corretta e tecnicamente solida per fare da server VPN. pfSense integra nativamente OpenVPN e IPsec, WireGuard è disponibile come pacchetto; offre firewall stateful, NAT, policy routing e accelerazione AES-NI se l’hardware la supporta. In questo scenario pfSense è il server VPN, non un semplice endpoint.

Alternativa: un mini-PC o VM Linux dedicata (Debian/Ubuntu) con WireGuard o OpenVPN “bare metal”. È più efficiente, meno overhead, ma richiede competenze operative maggiori per firewalling, hardening e gestione utenti.

Scelta migliore nel contesto tipico SMB/home-lab: pfSense su mini-PC fanless x86 con doppia NIC e CPU con AES-NI. Offre il miglior compromesso tra prestazioni, sicurezza, manutenzione e controllo centralizzato.

Una NIC (Network Interface Card) è l’interfaccia hardware che collega un dispositivo a una rete, tipicamente Ethernet o Wi-Fi, e gestisce l’invio e la ricezione dei frame a livello 2 OSI.

AES-NI (Advanced Encryption Standard New Instructions) è un insieme di istruzioni hardware nelle CPU x86 che accelera le operazioni di cifratura AES.

Riduce drasticamente il carico CPU e la latenza nei tunnel VPN che usano AES

## Open VPN (per creare la propria VPN)

![](assets/img-0044.png)![](assets/img-0045.png)![](assets/img-0046.png)![](assets/img-0047.png)![](assets/img-0048.png)![](assets/img-0049.png)![](assets/img-0050.png)![](assets/img-0051.png)

![](assets/img-0052.png)

(Credits from codelivly instagram page)

