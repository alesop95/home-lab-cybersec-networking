# Fastweb, ONT e modem: riscontro per la topologia

Le pagine ufficiali [compatibilità del modem di proprietà](https://www.fastweb.it/myfastweb/assistenza/guide/compatibilita-tecniche-del-modem-di-tua-proprieta/), [altri modem](https://www.fastweb.it/adsl-fibra-ottica/dettagli/altri-modem/), [installazione Seven BS-GPON](https://www.fastweb.it/myfastweb/assistenza/guide/seven-installazione-bs-gpon) e [connessione Fastweb](https://www.fastweb.it/adsl-fibra-ottica/connessione-fastweb/) documentano scenari in cui l'ONT esterno è collegato al Seven oppure, per apparati propri e tecnologie compatibili, forniscono parametri WAN come VLAN, credenziali e indirizzamento.

Nelle pagine consultate non è stata trovata una dichiarazione pubblica generale secondo cui l'ONT lega il servizio al MAC del Seven. Per la linea concreta, invece, l'assistenza ha escluso il collegamento diretto ONT -> OPNsense e una prova riferita da terzi ha riportato il fallimento della sostituzione. La baseline del progetto è quindi ONT -> Seven -> OPNsense: è una decisione prudenziale basata sull'evidenza locale, non una generalizzazione a tutte le linee Fastweb.

La conseguenza è il doppio NAT e la presenza di una Wi-Fi del Seven a monte del firewall. Quella rete va trattata come rete ordinaria o legacy temporanea; la segmentazione e l'ispezione OPNsense valgono solo per client collegati a valle del firewall.
