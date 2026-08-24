# Differenza tra LAN, WAN e DMZ

Prendendo ad esempio il contesto del firewall domestico con OPNsense, la WAN è l’interfaccia esposta verso l’esterno, cioè verso il modem o l’ONT del provider: è il lato non fidato della rete, da cui arriva traffico potenzialmente ostile, e su cui il firewall applica NAT, filtri e politiche restrittive, consentendo solo ciò che è esplicitamente permesso.

La LAN è la rete interna fidata, dove risiedono i dispositivi personali come PC, smartphone, server domestici o NAS, ed è l’interfaccia su cui il firewall consente comunicazioni in uscita e, di norma, blocca l’accesso diretto dall’esterno salvo regole specifiche.

La DMZ è una rete separata sia dalla WAN sia dalla LAN, pensata per ospitare sistemi che devono essere raggiungibili dall’esterno, come un server web, un servizio VPN o un dispositivo esposto a Internet, ma che non devono avere accesso libero alla LAN: il firewall fa da barriera logica, permettendo flussi controllati dalla WAN alla DMZ e, solo se necessario, dalla DMZ verso la LAN, riducendo l’impatto di un’eventuale compromissione di un servizio esposto. In questa configurazione a tre interfacce, la separazione fisica delle reti tramite schede dedicate rende il modello di sicurezza chiaro, verificabile e coerente con le best practice di segmentazione.
