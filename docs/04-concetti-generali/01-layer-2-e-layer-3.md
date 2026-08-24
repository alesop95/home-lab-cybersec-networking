# Layer 2 e layer 3

In FTTH l’ONT è un bridge layer 2 puro: converte GPON in Ethernet senza fare routing. Il primo dispositivo layer 3 può essere proprio OPNsense. Bisogna configurare la WAN del firewall in DHCP su Ethernet oppure su VLAN 835 se la linea Fastweb la richiede. NAT, firewalling, DHCP server e policy routing li gestisce OPNsense.

Il concetto corretto da fissare è questo: VLAN e routing sono due funzioni distinte che operano su livelli diversi del modello OSI[1]. Una VLAN segmenta il dominio Layer 2, cioè Ethernet, mentre il routing collega domini Layer 3, cioè IP. Il fatto che uno switch supporti VLAN non implica automaticamente che sappia instradare traffico tra esse. Significa soltanto che sa classificare, separare e inoltrare frame Ethernet[2] in base a un identificatore VLAN inserito nel frame tramite standard IEEE 802.1Q[3].

Architetturalmente, una VLAN equivale a creare più switch logici sopra lo stesso hardware fisico. Se esistono VLAN 10 e VLAN 20, lo switch L2 si comporta come se fossero due reti fisicamente separate anche se condividono backplane[4], porte e cablaggio. Il traffico broadcast[5], ARP[6] e unicast resta confinato dentro ciascuna VLAN. Questo è il motivo reale del tagging: isolamento logico, non routing.

Esempio concreto. Si immagini un’infrastruttura con due switch collegati tramite una porta trunk[7]. Sul primo switch sono presenti un PC amministrativo e una stampante in VLAN 10; sul secondo switch un PC guest in VLAN 20.

PC Admin -------- VLAN 10 -----+

                               |

                           Switch A

                               |

                     trunk 802.1Q

                               |

                           Switch B

                               |

PC Guest -------- VLAN 20 -----+

Quando il PC amministrativo invia un frame Ethernet verso la stampante, lo switch associa quel traffico alla VLAN 10. Sul link trunk il frame viene trasportato aggiungendo un tag 802.1Q che contiene l’ID VLAN. Lo switch remoto legge quel tag e inoltra il frame soltanto alle porte appartenenti alla VLAN 10. Il PC guest in VLAN 20 non riceve nulla perché per lo switch quel traffico appartiene a un dominio logico differente.

Il punto fondamentale è che lo switch L2 non guarda gli indirizzi IP per decidere il forwarding; guarda MAC address[8] e VLAN ID[9]. Per questo motivo un host in VLAN 10 non può raggiungere un host in VLAN 20 anche se entrambi hanno subnet IP compatibili. Manca una funzione di routing inter-VLAN[10], che richiede una routing table[11], interfacce Layer 3 e decisioni basate su IP destination.

Uno switch L3 aggiunge esattamente questo componente. Non sostituisce il funzionamento L2 ma lo estende: ogni VLAN riceve una SVI[12], cioè un’interfaccia virtuale IP, e lo switch può fare routing interno tra VLAN senza passare da un router esterno.

Uno switch L2 inoltra traffico soltanto all’interno dello stesso dominio Ethernet. Sa apprendere MAC address, mantenere tabelle CAM[13], gestire VLAN e decidere su quale porta inviare un frame, ma resta confinato al livello Ethernet. Non prende decisioni basate sugli indirizzi IP. Uno switch L3 aggiunge capacità di routing IP direttamente nello switch. Questo significa che oltre alla tabella MAC introduce una routing table e interfacce IP associate alle VLAN. In pratica ogni VLAN può avere un gateway IP locale nello switch stesso.

Esempio: VLAN 10 con subnet 192.168.10.0/24 e VLAN 20 con subnet 192.168.20.0/24. In uno switch L2 puro, un host della VLAN 10 non raggiunge la VLAN 20 senza un router esterno. In uno switch L3 si configurano due SVI:

interface vlan 10

 ip address 192.168.10.1/24

interface vlan 20

 ip address 192.168.20.1/24

Da quel momento lo switch esegue inter-VLAN routing internamente: riceve il frame Ethernet, estrae il pacchetto IP[14], consulta la routing table e reinstrada il traffico verso la VLAN corretta senza uscire dall’apparato.

Quindi uno switch L2 puro dovrei usarlo quando voglio separare, se non avessi L3 separerei e basta senza raggiungibilità. Uno switch L2 puro serve quando l’obiettivo è segmentare la rete senza permettere comunicazione tra i segmenti. La VLAN in questo caso crea isolamento logico: ogni VLAN diventa un dominio Ethernet indipendente con il proprio traffico broadcast, ARP e forwarding MAC.

Riprendendo l’esempio, il PC in VLAN 10 con IP 192.168.10.50 può parlare con la stampante 192.168.10.100 perché entrambi stanno nella stessa subnet e nella stessa VLAN. Quando invece tenta di raggiungere un host 192.168.20.x della VLAN 20, il sistema operativo capisce che la destinazione appartiene a una rete differente e prova a inviare il traffico verso il gateway configurato. Se lo switch è solo L2, quel gateway non esiste dentro lo switch. Quindi il traffico non viene instradato e la comunicazione fallisce. La separazione resta totale. Lo switch continua a fare correttamente switching Ethernet, ma non esiste alcuna funzione che colleghi logicamente le due reti IP. Con uno switch L3, invece, il gateway delle VLAN risiede nello switch stesso. Quando il PC invia traffico verso 192.168.20.x, lo switch riceve il frame destinato al proprio MAC gateway, legge il pacchetto IP, decide la VLAN di uscita tramite routing table e inoltra il traffico verso VLAN 20. In quel momento lo switch sta operando contemporaneamente come switch Ethernet e router IP.

In uno switch puramente L2 non esiste alcuna logica di routing IP, quindi due subnet separate non possono comunicare attraverso lo switch da sole. I pacchetti non “attraversano” la subnet differente perché l’host sorgente, appena vede che l’IP destinazione appartiene a una rete diversa, non prova nemmeno a cercare direttamente il MAC del destinatario. Invia invece il traffico al default gateway[15]. Se il gateway non esiste oppure non è raggiungibile, il pacchetto si ferma all’host sorgente e la comunicazione fallisce prima ancora che lo switch possa fare qualcosa di utile. Lo switch L2 vede soltanto frame Ethernet locali. Se riceve traffico destinato a MAC appartenenti alla stessa VLAN lo inoltra; se il traffico dovrebbe uscire verso un’altra subnet, manca completamente il componente che faccia routing tra reti IP differenti.

Quindi uno switch L2 può:

- separare reti tramite VLAN;

- trasportare traffico Ethernet;

- inoltrare frame dentro la stessa VLAN;

ma non può collegare subnet differenti senza un router o uno switch L3 esterno.

Quindi in uno scenario domestico con Zyxel XMG1915-10E Gestito L2 2.5G Ethernet (100/1000/2500) che cosa è possibile fare se ad esempio creo una VLAN di tutti i dispositivi domestici, e una porta la decreto a DMZ perchè magari voglio far uscire fuori internet dei servizi sotto lo stesso IP pubblico?  Con uno switch L2 come il Zyxel XMG1915-10E Managed L2 2.5G Switch la VLAN serve solo a separare i domini Ethernet; tutta la logica di sicurezza, NAT[16], DMZ[17], firewall e routing resta demandata al router.

In uno scenario domestico corretto, lo switch non “crea una DMZ” in senso reale. Può soltanto trasportare una VLAN dedicata alla DMZ. La vera separazione e l’esposizione verso Internet vengono gestite dal router/firewall. Esempio architetturale:

Internet

    |

Router / Firewall

    |

 trunk VLAN

    |

Switch L2

 |            |

VLAN 10    VLAN 20

LAN        DMZ

La VLAN 10 contiene dispositivi domestici interni; la VLAN 20 contiene un server esposto pubblicamente, ad esempio reverse proxy, NAS o applicazione web. Lo switch si limita a mantenere separato il traffico. Il router invece possiede:

- un’interfaccia IP per VLAN 10;

- un’interfaccia IP per VLAN 20;

- regole firewall;

- eventuale port forwarding[3] dall’IP pubblico verso l’host DMZ.

Se il router è configurato correttamente, un host DMZ può essere raggiungibile da Internet ma isolato dalla LAN interna. Senza router L3/firewall, lo switch L2 non può fare nulla di tutto questo perché non gestisce traffico IP né policy di sicurezza.

Ok, e se ho quindi un firewall con OPNSense come firewall connesso ad una porta di quello switch? Con OPNsense la situazione cambia completamente, perché il routing e la sicurezza vengono centralizzati nel firewall mentre lo switch L2 diventa un puro apparato di trasporto e segmentazione VLAN. L’architettura corretta è questa:

Internet

    |

OPNsense

    |

 trunk VLAN

    |

Switch L2

 |            |

VLAN 10    VLAN 20

LAN        DMZ

La porta tra OPNsense e switch viene configurata come trunk 802.1Q. Dentro quel singolo link transitano contemporaneamente più VLAN taggate. OPNsense crea un’interfaccia logica per ogni VLAN, ad esempio:

igc0_vlan10 -> 192.168.10.1/24

igc0_vlan20 -> 192.168.20.1/24

In questo scenario OPNsense diventa:

- gateway delle VLAN;

- router inter-VLAN;

- firewall stateful[18];

- punto NAT verso Internet.

Lo switch L2 continua a non fare routing. Però trasporta le VLAN fino a OPNsense, che decide quali reti possono comunicare, quali porte esporre pubblicamente e quali traffici bloccare.

Questa è l’architettura standard corretta anche in ambienti enterprise piccoli e medi: switch L2 per accesso e segmentazione, firewall/router L3 centrale per policy e routing.

La DMZ quindi non nasce nello switch ma nella policy del firewall. Una porta dello switch assegnata alla VLAN DMZ diventa semplicemente un punto di accesso Ethernet a quella rete isolata.

Ok, dunque per terminare, in un'architettura come ONT → modem Fastweb → OPNsense → switch L2, in questo schema il dispositivo “Router Modem Fastweb” deve essere considerato esclusivamente come edge verso Internet. Se mantiene funzioni di routing interno (DHCP, NAT, firewall attivo), diventa un doppio livello di controllo che introduce sovrapposizioni con OPNsense.

In pratica si crea una doppia NAT[19] e una doppia gestione delle reti, che può funzionare ma non è coerente come design pulito. Lo schema tecnicamente corretto diventa quindi questo:

Internet

    |

Router Fastweb (solo modem o bridge)

    |

OPNsense (gateway e firewall principale)

    |

trunk 802.1Q

    |

Switch L2 Zyxel

 |            |

VLAN 10    VLAN 20

LAN        DMZ

In questa configurazione OPNsense è l’unico punto di decisione per:

routing tra VLAN;

NAT verso Internet;

policy firewall tra LAN e DMZ;

esposizione servizi pubblici.

Lo switch L2 resta solo un livello di distribuzione: non applica regole, non instrada, non interpreta IP. Il tag VLAN serve solo a mantenere separati i domini Ethernet fino a OPNsense.

Se invece il router Fastweb resta in modalità router attiva, il risultato è una catena:

Fastweb NAT > OPNsense NAT > rete interna. Funziona, ma introduce complessità inutile e riduce la trasparenza del traffico. La topologia è completamente corretta solo se OPNsense è il punto unico di routing/firewall e il dispositivo Fastweb è ridotto a funzione di accesso WAN.

Il punto tecnico non è la posizione, ma il ruolo effettivo del modem Fastweb. Se quel dispositivo resta in modalità router, allora continua a fare NAT e assegnazione rete propria, e OPNsense si ritrova dietro un upstream già “chiuso”. In quel caso la topologia funziona comunque, ma si entra in doppio livello di routing. Se il modem Fastweb non può essere messo in bridge puro, lo scenario resta valido ma con questo vincolo: OPNsense riceve un IP privato dal modem e diventa un firewall “dietro NAT”. Tutto il routing interno (VLAN 10, VLAN 20, DMZ) continua a essere gestito correttamente da OPNsense verso lo switch L2, ma l’esposizione verso Internet dipende dal modem Fastweb. In sintesi operativa:

ONT → modem Fastweb: livello fisico e accesso ISP

modem Fastweb → OPNsense: WAN di OPNsense (può essere bridged o NAT a seconda del modem)

OPNsense → switch L2: unica rete interna con trunk VLAN e routing inter-VLAN

Lo switch L2 rimane coerente in questo schema perché non deve conoscere nulla di IP, solo VLAN taggate. Il punto critico non è lo switch, ma il grado di controllo del modem Fastweb: se non è in bridge, OPNsense non diventa il vero edge della rete ma un livello intermedio.

La confusione nasce dal significato di “instradare” rispetto a “trasportare VLAN”. Uno switch L2 non instrada traffico IP tra reti diverse. Questo resta vero. Però uno switch L2 può trasportare frame Ethernet già appartenenti a VLAN differenti, purché siano correttamente taggati. Il tagging VLAN non è routing. È solo un’etichetta dentro il frame Ethernet che dice “questo frame appartiene alla VLAN 10” oppure “alla VLAN 20”. Lo switch L2 non interpreta IP, non decide percorsi, non modifica subnet. Si limita a leggere quel tag e inoltrare il frame sulle porte configurate per quella VLAN. Quindi la divisione è questa:

OPNsense fa due cose:

	a) crea le VLAN logiche e assegna IP gateway (es. 192.168.10.1, 192.168.20.1);

	b) decide il routing tra VLAN e verso Internet.

Lo switch L2 Zyxel non “capisce” le VLAN come reti IP: riceve frame Ethernet con tag 802.1Q, li mantiene comunque separati per VLAN ID, li inoltra solo sulle porte configurate per quella VLAN o sul trunk.

L'esempio mentale corretto è che OPNsense invia un frame VLAN 10, lo switch lo riceve già taggato e lo switch lo manda solo alle porte VLAN 10 e fine. Non c’è alcuna decisione di rete. Il punto chiave è questo: il tagging avviene su OPNsense (o sul dispositivo che genera il frame), ma lo switch L2 non deve “capire” il significato del tag, deve solo rispettarlo. Quindi non c’è contraddizione: L2 non instrada, ma può trasportare traffico VLAN taggato senza interpretarlo.

La presenza dello switch non cambia il principio logico. OPNsense non “vede” le porte fisiche dei dispositivi finali, vede soltanto le VLAN che gli arrivano sul trunk. La connessione tra switch e firewall diventa il punto di aggregazione di tutta la rete interna. Tutti i dispositivi collegati allo switch vengono instradati logicamente dentro una VLAN specifica prima ancora di arrivare a OPNsense. Il funzionamento reale è questo:

	1. Le porte dello switch sono configurate come access port o trunk.

	2. Una porta access è associata a una sola VLAN. Un PC collegato lì non sa nulla delle VLAN; lo switch gli assegna automaticamente la VLAN corretta.

	3. Il PC in VLAN 10 genera traffico Ethernet “normale”.

Lo switch aggiunge il tag VLAN 10 internamente.

	4. Quel traffico sale sul trunk verso OPNsense già etichettato.

OPNsense riceve il frame sul suo unico link fisico, ma lo interpreta come interfacce logiche separate: igc0_vlan10 e igc0_vlan20.

Quindi la configurazione in OPNsense non si basa sulle porte dei dispositivi finali, ma sulle interfacce VLAN create sopra l’unica scheda fisica collegata allo switch. Esempio concreto di mapping logico in OPNsense:

  igc0 (fisico verso switch)

    ├── VLAN 10 → LAN 192.168.10.1/24

    └── VLAN 20 → DMZ 192.168.20.1/24

Lo switch fa solo da estensione fisica. Tutta la segmentazione reale avviene tra porte access dello switch (assegnazione VLAN), trunk verso OPNsense (trasporto VLAN), interfacce VLAN su OPNsense (routing e firewall). Quindi i PC non devono essere collegati direttamente a OPNsense. Devono solo essere correttamente assegnati a una VLAN sullo switch.

E se quel traffico sale sul trunk verso OPNsense già etichettato, e se questo benedetto switch è L2, come fa a salire etichettato il traffico secondo quello che abbiamo detto all'inizio. come fa lo switch a dirgli che il cavo ethernet cat 6 che collega una porta dello switch alla scheda di rete di OPNsense sia trunk verso OPNsense (trasporto VLAN)? Proprio perché il tagging non è una funzione “L3” e non richiede uno switch L3. È una funzione L2.

Uno switch L2 può essere configurato in due modalità sulle porte Ethernet: porta access e porta trunk.

La differenza non è nel livello OSI, ma nel modo in cui lo switch tratta i frame Ethernet su quella porta.

Una porta access è collegata a un singolo dominio VLAN. Il dispositivo collegato non vede alcun tag VLAN. Lo switch aggiunge e rimuove il tag internamente.

Una porta trunk è una porta L2 che trasporta più VLAN contemporaneamente sullo stesso link fisico. In questo caso il tag 802.1Q non viene rimosso, ma mantenuto e trasmesso così com’è verso il dispositivo a valle. Quindi in questo caso la porta dello switch verso OPNsense viene configurata come trunk. Questo non significa routing, non significa L3, non significa intelligenza IP. Significa solo: “su questo cavo Ethernet posso trasportare frame appartenenti a più VLAN, usando il campo 802.1Q”.

Lo switch non “decide” il contenuto IP. Applica solo una regola di inoltro L2:

> se frame VLAN 10 → manda su trunk mantenendo tag 10

> se frame VLAN 20 → manda su trunk mantenendo tag 20

OPNsense dall’altra parte non riceve “un cavo speciale”. Riceve un normale frame Ethernet su una singola interfaccia fisica. La differenza è che il sistema operativo del firewall interpreta il campo 802.1Q e separa il traffico in interfacce logiche VLAN.

Quindi il punto chiave è questo: lo switch L2 non “capisce” il routing, ma è perfettamente in grado di trasportare VLAN taggate perché il tagging è parte dello standard Ethernet a livello 2, non una funzione di livello 3.

Note:

[1] OSI: Open Systems Interconnection, modello teorico a livelli per le comunicazioni di rete.

[2] Ethernet frame: unità dati del protocollo Ethernet.

[3] IEEE 802.1Q: standard per il tagging VLAN nei frame Ethernet.

[4] Backplane: bus interno ad alta velocità dello switch.

[5] Broadcast: traffico inviato a tutti gli host del dominio locale.

[6] ARP: Address Resolution Protocol, associa IP a MAC address.

[7] Trunk: collegamento che trasporta simultaneamente più VLAN.

[8] MAC address: identificatore hardware univoco della scheda di rete.

[9] VLAN ID: identificatore numerico della VLAN.

[10] Inter-VLAN routing: comunicazione IP tra VLAN differenti.

[11] Routing table: tabella usata per decidere dove inoltrare traffico IP.

[12] SVI: Switched Virtual Interface, interfaccia Layer 3 associata a una VLAN.

[13] CAM table: memoria usata dallo switch per associare MAC address e porte fisiche.

[14] Pacchetto IP: unità dati Layer 3 contenente indirizzi IP sorgente e destinazione.

[15] Default gateway: indirizzo IP del dispositivo incaricato di instradare traffico verso reti esterne alla subnet locale.

[16] NAT: Network Address Translation, meccanismo che traduce IP privati in IP pubblici.

[17] DMZ: Demilitarized Zone, rete isolata usata per esporre servizi verso reti non fidate.

[18] Stateful firewall: firewall che mantiene traccia dello stato delle connessioni di rete per consentire o bloccare traffico in modo contestuale.

[19] Double NAT: doppia traduzione degli indirizzi IP tra due dispositivi di rete, che complica port forwarding e tracciamento delle connessioni.
