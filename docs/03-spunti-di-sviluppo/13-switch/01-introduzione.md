# Introduzione

Il Seven funziona come switch 4 porte integrate, ma solo una porta può realmente andare oltre 1 Gbit/s. Tutto il resto del traffico LAN verso porte 1 Gbit/s rimane limitato, quindi se si vuole sfruttare 2,5 Gbit/s per un singolo dispositivo, è quella porta lì da collegare ad uno switch esterno 2,5G e lasciare ad esempio la porta a 1Gbps singolarmente per dispositivi la cui scheda di rete è intrinsecamente limitata come la Playstation 5, tuttavia non facendola passare per il firewall in questo modo.

Se più dispositivi devono sfruttare 2.5 Gbps, si può prendere uno switch Multi-Gig (2.5G) unmanaged che va bene per la maggior parte degli home lab. Ad esempio:

- TP-Link TL-SG108-M2 (8 porte 2.5G, unmanaged, fanless): è un ottimo rapporto qualità/prezzo per casa/ufficio; plug-and-play e auto-negozia 2.5/1/0.1 G [https://www.tp-link.com/it/home-networking/soho-switch/tl-sg108-m2/](https://www.tp-link.com/it/home-networking/soho-switch/tl-sg108-m2/)
- TP-Link TL-SG108-M2 V2 [https://www.tp-link.com/us/business-networking/unmanaged-switch/tl-sg108-m2/](https://www.tp-link.com/us/business-networking/unmanaged-switch/tl-sg108-m2/)

Con uno switch unmanaged, la segmentazione però viene gestita sul router/Seven mentre per VLAN L2 completa bisogna prendere uno switch managed. Ad esempio:

esistono switch con molte porte 2.5G (TP-Link 8x2.5G) o soluzioni miste con uplink 10G per aggregare backplane e scegliere in base al numero di client che si vogliono a 2.5G.
