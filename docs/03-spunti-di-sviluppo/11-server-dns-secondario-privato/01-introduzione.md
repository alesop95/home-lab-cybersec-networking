# Introduzione

La soluzione corretta, se vuoi un DNS “tra firewall e rete privata”, non è un authoritative server né un forwarder banale, ma un resolver ricorsivo completo, validante DNSSEC, con policy di controllo, posizionato come choke point logico del traffico DNS. L’implementazione migliore, verificabile e industrialmente usata, è Unbound con Pyhole [https://www.navigaresenzapubblicita.org/unbound-e-pi-hole-una-soluzione-dns-completa/](https://www.navigaresenzapubblicita.org/unbound-e-pi-hole-una-soluzione-dns-completa/). La logica è quella di un controllo, auditabilità e assenza di dipendenze esterne.

Unbound è scritto per fare una cosa sola: risolvere DNS in modo corretto, sicuro e prevedibile. Questo è verificabile nei sorgenti e nella documentazione tecnica ufficiale.

Si ha una macchina fisica connessa alla LAN. Questa macchina ha una sola funzione: DNS recursive resolver. Il firewall non risolve DNS, filtra solo. Tutti i client interni possono parlare DNS solo con questa macchina.

Firewall ↔ DNS Resolver (Unbound) ↔ LAN privata

Il DNS resolver ha un IP statico interno, ad esempio 192.168.1.2. Il firewall consente traffico UDP/TCP 53 solo da 192.168.1.2 verso Internet e blocca qualsiasi pacchetto 53 proveniente da altri host e questo crea una DNS egress control reale.

Il DNS non deve stare “fuori” dal firewall, perché perderebbe visibilità e controllo e non deve stare “dentro” la LAN come un servizio generico, perché diventerebbe bypassabile. Questa posizione consente ispezione centralizzata delle query, logging deterministico, rate limiting, blocco per dominio, TLD, categoria, mitigazione DNS tunneling e protezione da cache poisoning via DNSSEC. Tutto questo *prima* che il traffico IP vero e proprio esista.

In questo modo tutto il traffico DNS è forzato, osservabile, validato crittograficamente e nessun client può parlare DNS con l’esterno e al contempo nessun provider terzo vede le proprie query. Il firewall lavora su flussi IP già “risolti” e non su nomi e il DNS diventa un punto di controllo infrastrutturale, non un servizio accessorio.

## Flusso pacchetti (wire-level, senza semplificazioni)

Facendo un esempio pratico, un client interno chiede [www.example.com](http://www.example.com) e a quel punto il client invia un pacchetto UDP 53 a 192.168.1.2. A quel punto Unbound riceve la query, controlla la cache locale in RAM. Se c’è hit, risponde immediatamente mnetre se c’è un miss, Unbound non inoltra la query a Google, Cloudflare o ISP.

Unbound genera una query iterativa verso un Root Name Server, tipicamente via UDP 53 verso uno degli IP anycast di IANA root. Il firewall vede un pacchetto UDP 53 solo proveniente da 192.168.1.2 e lo lascia uscire.

Il root risponde con una delega NS per il TLD (.com). Unbound valida la risposta, memorizza i glue record, e genera una nuova query verso il TLD server .com.

Il TLD risponde con i name server autoritativi di example.com e Unbound valida la catena DNSSEC (se presente).

Unbound interroga l’authoritative name server di example.com, ottiene l’A/AAAA record finale, valida DNSSEC se disponibile, mette tutto in cache rispettando i TTL, e risponde al client.

Il client non vede mai root, TLD o authoritative server. Dal punto di vista del client, esiste un solo DNS: 192.168.1.2.

## Pyhole

Pi-hole [https://pi-hole.net/](https://pi-hole.net/) non sostituisce ciò che è stato descritto prima: Pi-hole è un DNS filtering engine con interfaccia di policy, non un resolver DNS completo. Pi-hole è un'applicazione Linux pensata per bloccare la pubblicità e il tracciamento degli utenti su Internet a livello di rete locale [https://it.wikipedia.org/wiki/Pi-hole](https://it.wikipedia.org/wiki/Pi-hole). Fondamentalmente trasforma Linux in un server DNS.

Di default, durante l’installazione, Pi-hole chiede di scegliere un upstream pubblico tipo 1.1.1.1 o 8.8.8.8. Questa scelta è una scorciatoia funzionale, non una buona architettura. In quel caso Pi-hole diventa un semplice proxy filtrante verso DNS di terzi, con tutte le conseguenze: dipendenza esterna, perdita di controllo reale, esposizione delle query, single point of failure geografico e politico. Questo non è un DNS infrastrutturale, è un ad-blocker centralizzato.

Quindi l’architettura corretta, senza ambiguità, giusta e completa è:

client → Pi-hole come unico DNS distribuito via DHCP → Unbound come upstream locale ricorsivo → root/TLD/authoritative via firewall.

Qualsiasi configurazione in cui Pi-hole punta a 1.1.1.1 o 8.8.8.8 è funzionale ma comunque architettonicamente architettonicamente debole. Qui Pi-hole è la politica, Unbound è la fisica del DNS per un’infrastruttura concreta di alto livello.

Sicuramente la figata di personalizzazione come valore aggiunto rispetto a quelli commerciali è che quando è finita l'installazione lui dirà che se chiamo linux all'indirizzo IP che mi hai dato, si entra su un pannello di amministrazione solo di DNS e si può mettere white list, black list e cosa bloccare e le liste.

### Legame tra Unbound e Pi-hole

Il legame corretto è gerarchico e funzionale: Pi-hole sta davanti a Unbound, non al posto di Unbound a livello architetturale. Pi-hole, tecnicamente, è un demone che ascolta sulla porta 53 e intercetta le query DNS dei client, le confronta contro blacklist, whitelist e regole locali, e solo se la query è ammessa la inoltra a un upstream DNS.

Il modo corretto di “legare tutto” è che Pi-hole rimane il frontend DNS per i client, Unbound diventa l’unico upstream di Pi-hole e opera come resolver ricorsivo completo. Pi-hole risponde ai client sulla 53, applica le policy di blocco, e quando deve risolvere un dominio consentito passa la query a Unbound, tipicamente su 127.0.0.1:5335 o su un IP dedicato se sono su macchine diverse. Unbound, a quel punto, fa esattamente ciò che ho descritto prima: risoluzione iterativa root → TLD → authoritative, validazione DNSSEC, cache locale, nessun DNS pubblico coinvolto. Pi-hole non parla mai con Internet, Unbound sì, ed è l’unico autorizzato dal firewall.

### Chiarimento tecnico

Il firewall non “risponde” per dire chi comanda: è il DHCP server che distribuisce gateway e DNS, spesso ospitato sul firewall ma concettualmente distinto. Configurare “2/3 server DNS” lato client è una cattiva pratica se uno di questi è esterno, perché il client userà fallback o round-robin e potrà bypassare Pi-hole; se Google DNS è configurato come secondario e Pi-hole rallenta o risponde NXDOMAIN, molti stack passano direttamente a 8.8.8.8. Questo distrugge il modello di controllo. L’unico DNS distribuito via DHCP deve essere Pi-hole. La resilienza non si fa con DNS pubblici paralleli, si fa con ridondanza interna.

È vero che Pi-hole “trasforma Linux in un server DNS” nel senso che apre la porta 53, ma non è un resolver: senza upstream non sa risolvere nulla. La “figata” del pannello web è reale ma va letta per quello che è: un motore di policy DNS, non l’infrastruttura DNS. Il valore aggiunto rispetto ai DNS commerciali non è la GUI in sé, è il fatto che le decisioni avvengono prima della risoluzione, sotto il tuo controllo, con liste versionabili e auditabili.
