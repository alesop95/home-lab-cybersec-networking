# Il doppio NAT di un firewall domestico dietro un modem in comodato

Ritorno allo [studio](README.md). Documento didattico del 07/10/2026: spiega perche' questa rete ha due traduzioni di indirizzo in serie, che cosa cambia e che cosa no, e quali scelte di progetto ne discendono. Riprende il filo iniziato nella prima stesura, oggi distribuito fra l'[introduzione sui parametri WAN](../../02-ftth-fastweb/07-tbc-new-i-parametri-di-accesso-wan-su-ont/01-introduzione-concettuale-tecnica.md), la [soluzione con OPNsense](../10-firewall-before-the-switch/02-soluzione-professionale-con-opnsense-25-7.md) e lo [scambio con Autore-LinkedIn-B](../21-idee-setup-da-profili-linkedin-interessanti/02-home-lab-cybersecurity-infrastructure-autore-linkedin-b.md), e lo ricompone in un solo ragionamento. Gli indirizzi privati sono quelli di progetto, l'indirizzo pubblico e' il segnaposto di documentazione `203.0.113.10`. Nulla di quanto descritto e' ancora stato collaudato su questa linea.

## Il punto di partenza: chi termina la linea

Una linea in fibra domestica arriva in casa su un terminale ottico, l'ONT[^1], che converte il segnale in Ethernet e non fa altro. Il lavoro che rende la linea utilizzabile, cioe' autenticarsi presso l'operatore, ottenere l'indirizzo pubblico e instradare verso Internet, lo fa l'apparato collegato all'ONT. Su questa linea quell'apparato e' il Fastweb Seven fornito in comodato, e non si puo' togliere: l'interfaccia non offre una modalita' bridge, ne' il passaggio trasparente della sessione PPPoE[^2], ne' quello della VLAN di servizio, e l'assistenza ha escluso il collegamento diretto di un firewall all'ONT.

Ne segue una catena che non e' una scelta ma un vincolo: ONT, poi Seven, poi OPNsense. Il Seven tiene l'indirizzo pubblico statico e la fonia, e verso l'interno presenta una rete privata, la `192.168.1.0/24` con se stesso in `.254`. OPNsense vi si collega con la propria porta WAN come un qualunque client, prende un indirizzo di quella rete e da li' in giu' costruisce la rete di casa. Dal punto di vista del Seven, l'intera casa segmentata e' un solo dispositivo.

## Che cosa fa un NAT

Un NAT[^3] di uscita riscrive l'indirizzo sorgente dei pacchetti che attraversano un router, sostituendo l'indirizzo privato del dispositivo con l'indirizzo dell'interfaccia di uscita, e annota la sostituzione in una tabella di stato. Quando arriva la risposta, il router la riconosce dalla tabella, rimette a posto l'indirizzo di destinazione e la consegna al dispositivo giusto. La tabella di stato e' anche la ragione per cui un NAT, come effetto collaterale, scarta il traffico in ingresso non richiesto: un pacchetto che non corrisponde a nessuna voce non ha un destinatario a cui essere restituito.

In questa rete i router che fanno NAT sono due, e ciascuno fa esattamente questo lavoro sulla propria interfaccia di uscita. Per questo si parla di doppio NAT.

## Un pacchetto in uscita, passo per passo

Si segue una richiesta di un PC della VLAN 10 verso un sito qualunque. L'indirizzo WAN di OPNsense e' qui `192.168.1.2` a titolo di esempio: quello reale sara' una prenotazione DHCP[^4] sul Seven, da decidere al collaudo.

| Tratto | Sorgente vista | Chi la riscrive |
|---|---|---|
| dal PC a OPNsense | `192.168.10.20` | nessuno |
| da OPNsense al Seven | `192.168.1.2` | OPNsense, primo NAT |
| dal Seven a Internet | `203.0.113.10` | Seven, secondo NAT |

Al ritorno il percorso si ripercorre all'indietro: il Seven trova la voce nella propria tabella e consegna a `192.168.1.2`, OPNsense trova la voce nella propria e consegna a `192.168.10.20`. Il costo della doppia traduzione in latenza e' trascurabile, perche' una ricerca in una tabella di stato costa microsecondi; il costo vero, quando c'e', sta nel numero di pacchetti al secondo che la CPU del firewall riesce a trattare, ed e' lo stesso che pagherebbe con un NAT solo.

## Che cosa il doppio NAT non tocca

Tutto il traffico che resta dentro casa non attraversa il Seven e non viene tradotto. Un PC che apre una condivisione sul NAS, un AP che parla con il firewall, un client che interroga il DNS di OPNsense, una VM del laboratorio che attacca un bersaglio nella propria VLAN: nessuno di questi flussi vede una sola traduzione di indirizzo, e ciascuno si comporta esattamente come si comporterebbe dietro un firewall collegato direttamente alla fibra. Segmentazione in VLAN, regole fra zone, raccolta dei log, un dominio Active Directory di prova, esercitazioni di intrusione: e' tutto lavoro interno al perimetro, e il doppio NAT non lo limita.

Non tocca neppure la sicurezza, nel senso che non la peggiora. OPNsense resta il punto in cui si decide che cosa entra e che cosa esce dalla casa segmentata, e il Seven davanti aggiunge una seconda tabella di stato che scarta il traffico non richiesto prima ancora che arrivi al firewall.

## Che cosa complica: il traffico in ingresso

Le difficolta' cominciano quando qualcuno da Internet deve aprire una connessione verso casa. Con un solo router basta un inoltro di porta[^5]: il router riceve sulla porta stabilita e riscrive la destinazione verso l'host interno. Con due router in serie gli inoltri diventano due. Il Seven deve passare la porta alla WAN di OPNsense, e OPNsense deve passarla all'host che offre il servizio, oppure gestirla da se' se il servizio e' suo.

Il progetto riduce il problema a un caso solo. Nessun servizio interno viene esposto direttamente: da fuori si entra in VPN, e la VPN WireGuard termina su OPNsense stesso. Il Seven inoltra quindi una sola porta UDP alla WAN del firewall, e il secondo inoltro non serve, perche' il destinatario e' il firewall. Va aggiunto un dettaglio che rassicura sul piano dei log: l'inoltro del Seven riscrive la destinazione e non la sorgente, quindi OPNsense vede l'indirizzo vero di chi si collega e non quello del modem.

Il Seven offre anche la funzione Exposed Host, che inoltra alla WAN di OPNsense tutte le porte invece di una sola. Non elimina il primo NAT, perche' l'indirizzo pubblico resta sul Seven, ma sposta tutte le decisioni sul traffico in ingresso su OPNsense. E' l'alternativa da considerare se un giorno la DMZ ospitera' un servizio pubblico e si vorra' gestire ogni porta da un solo punto; finche' l'unico ingresso e' la VPN, una porta sola e' la superficie piu' piccola.

## Che cosa complica: i dispositivi che si aprono le porte da soli

Alcuni dispositivi non aspettano un inoltro configurato a mano ma lo chiedono al router con UPnP[^6]. Dietro due router la richiesta arriva solo al primo, cioe' a OPNsense, e il Seven non ne sa nulla: il dispositivo crede di essere raggiungibile e non lo e'. Il caso tipico e' la console di gioco, che classifica la propria connettivita' in tre tipi di NAT e con il doppio NAT finisce spesso nel tipo piu' restrittivo, con effetti concreti sul gioco in rete e sulle chat vocali.

Per la PS5 di casa la scelta presa il 07/10/2026 e' collegarla direttamente a una porta LAN del Seven, fuori dal perimetro di OPNsense. La console parla con i server del produttore e dei giochi e non naviga, quindi la protezione e la segmentazione del firewall le aggiungono poco; collegata al Seven ha un NAT solo, e il tipo di NAT si sistema sul modem, con UPnP oppure con inoltri statici alle porte indicate dal produttore. La scelta usa una porta da 1 GbE del Seven, che e' quanto la scheda della console supporta, e non occupa una porta dello switch. Ha un costo da dichiarare: se si abilita UPnP sul Seven, qualunque dispositivo collegato al Seven, compresi i client della sua Wi-Fi, puo' aprirsi una porta verso Internet. Gli inoltri statici verso l'indirizzo della sola console evitano quel costo.

## Che cosa complica: il percorso diretto fra due peer

Gli strumenti di rete sovrapposta come Tailscale e il suo derivato Tailcat attraversano il NAT senza inoltri: entrambi i lati aprono connessioni in uscita, si incontrano su un relay pubblico chiamato DERP[^7] e poi tentano di parlarsi direttamente forando le tabelle di stato dei rispettivi NAT. Funzionano anche dietro due NAT, e se il foro non riesce restano sul relay, che e' piu' lento ma funziona. Un NAT che cambia la porta sorgente a ogni connessione, come fa OPNsense per impostazione predefinita, rende il percorso diretto meno probabile; la documentazione di Tailscale suggerisce in quel caso una regola di NAT in uscita a porta statica per il solo host interessato, indicazione da verificare sulla pagina ufficiale prima di applicarla. L'uso di Tailcat in questa casa e' descritto nel documento sull'[accesso remoto](06-accesso-remoto-vpn.md).

## Le alternative scartate

La modalita' bridge del modem avrebbe eliminato il primo NAT lasciando al firewall l'indirizzo pubblico: il Seven non la offre. Il collegamento diretto del firewall all'ONT avrebbe eliminato il modem: l'assistenza lo ha escluso per questa linea, e anche se la documentazione pubblica dell'operatore non dimostra un vincolo generale, il progetto non costruisce su un percorso non validato.

Un router di terze parti come un FRITZ!Box non cambia il quadro, e l'utente ha deciso il 07/10/2026 di non acquistarlo. Messo dietro il Seven aggiungerebbe una terza traduzione o farebbe peggio il lavoro che fa gia' OPNsense; messo al posto del Seven richiederebbe proprio la configurazione libera della linea che qui non e' stata validata. In nessuna delle due posizioni migliora la topologia.

Resta il CGNAT[^8], che qui non c'e' e che vale nominare per distinguerlo: e' il NAT che alcuni operatori fanno nella propria rete quando non assegnano un indirizzo pubblico al cliente, e rende impossibile qualunque inoltro in ingresso. Con l'indirizzo pubblico statico questa linea ne e' fuori, ed e' la ragione per cui il doppio NAT resta un inconveniente gestibile e non un muro.

## Un riscontro indipendente

Il 14/09/2026 Autore-LinkedIn-B ha descritto la stessa catena su un operatore diverso: ONT in casa, modem dell'operatore non aggirabile, OPNsense a valle. Non e' una prova tecnica ripetuta qui, ma sposta il vincolo da peculiarita' della linea a forma normale di un firewall personale dietro un modem in comodato. Le due architetture divergono su che cosa mettere dietro il firewall: lui tiene la casa sul modem e protegge solo il laboratorio, qui la casa intera entra nel perimetro, compreso il wireless con i due access point.

## Che cosa resta da misurare

Tre verifiche chiudono il ragionamento sul campo. Che la porta LAN del Seven collegata alla WAN di OPNsense sia quella a 2,5 GbE e non una delle altre, che sono a 1 GbE. Quanto traffico l'i3 del firewall con le schede Realtek riesce a tradurre e filtrare, misurato prima con le sole regole di base e poi con l'ispezione attiva, perche' sopra quella cifra la linea da 2,5 Gbps non arriva ai client. E se il Seven deleghi un prefisso IPv6 a valle: con IPv6 il NAT non c'e' e il filtraggio va progettato a parte, oppure IPv6 resta non distribuito finche' non e' collaudato.

[^1]: *ONT*, Optical Network Terminal: il terminale che chiude la fibra in casa e la converte in Ethernet.

[^2]: *PPPoE*, Point-to-Point Protocol over Ethernet: uno dei modi in cui un apparato si autentica presso l'operatore e riceve l'indirizzo.

[^3]: *NAT*, Network Address Translation: riscrittura degli indirizzi dei pacchetti che attraversano un router, con una tabella di stato che ricorda le sostituzioni.

[^4]: *DHCP*, Dynamic Host Configuration Protocol: assegnazione automatica degli indirizzi; una prenotazione lega un indirizzo fisso a un dispositivo.

[^5]: L'inoltro di porta e' una regola di NAT in ingresso, detta anche port forwarding o DNAT, che riscrive la destinazione invece della sorgente.

[^6]: *UPnP*, Universal Plug and Play: protocollo con cui un dispositivo chiede al router di aprirgli una porta senza intervento manuale.

[^7]: *DERP*, Designated Encrypted Relay for Packets: rete di relay di Tailscale che fa incontrare i peer e inoltra il traffico cifrato quando il collegamento diretto non riesce.

[^8]: *CGNAT*, Carrier-Grade NAT: traduzione fatta dall'operatore su molti clienti che condividono lo stesso indirizzo pubblico.
