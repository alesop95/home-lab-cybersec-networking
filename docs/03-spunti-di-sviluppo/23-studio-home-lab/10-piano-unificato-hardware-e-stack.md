# Piano unificato: hardware, server Proxmox e stack open source

Ritorno allo [studio](README.md). Documento di progetto dell'8/10/2026, chiesto dall'utente per riorganizzare il progetto attorno a tutte le informazioni raccolte, con la migliore soluzione open source per ogni funzione e con un server Proxmox su macchina fisica ricavato dall'hardware disponibile. Ogni scelta porta il suo stato: *deciso* se c'è una decisione registrata, *proposto* se aspetta l'utente, *pendente* se aspetta un dato, *scartato* se è esclusa con una ragione. Nulla di quanto descritto è installato.

## L'hardware e il suo ruolo

| Macchina | Che cosa è | Ruolo | Stato |
|---|---|---|---|
| NET-04, firewall | i3 di settima generazione, 8 GB, SSD 120 GB, tre schede di rete | OPNsense | deciso; installato il 16/01/2026, non configurato |
| `PC-DESKTOP-A` | base del consolidamento, 32 GB DDR4, due SSD SATA, due NVMe | NAS con TrueNAS SCALE (ADR-015, ADR-026) | deciso; montaggio fermo al Passo 1.6 |
| `linux-desktop-A` | ASRock H270M Pro4, i7-7700 a 4 core e 8 thread, 16 GB DDR4 in quattro moduli, rete Intel I219-V, nessun disco | server Proxmox, cioè l'host di servizio sempre acceso SRV-01 | proposto |
| `PC-DESKTOP-B` | ASUS B150-PRO, i7-6700, senza memoria né disco | scorta gemella del NAS, non si tocca | deciso dall'inventario delle scorte |
| `linux-desktop-B` | ASUS Z97-P, i7-4790, 16 GB DDR3, nessun disco | secondo nodo sacrificabile per prove distruttive, solo se serve | proposto, priorità bassa |
| PC-03, anduinOS | seconda ASUS Z97-P, processore LGA1150 da leggere, 16 GB DDR3, Samsung 850 EVO M.2 SATA da 250 GB | fornitore di disco e memoria DDR3; in alternativa nodo con 32 GB DDR3 | proposto, letto dalle foto del 09/10/2026 |
| PC-02, Xubuntu | ASUS serie P55, LGA1156, DDR3-1333, grafica dedicata, SSD Kingston V300 da 240 GB, disco meccanico da 500 GB | fornitore di dischi e alimentatore, nessun servizio | proposto, letto dalle foto del 09/10/2026 |

La scelta di `linux-desktop-A` per Proxmox viene dall'[inventario delle scorte](../02-storage-di-rete-nas/06-inventario-delle-scorte-dopo-il-consolidamento.md), che la indica già come candidata naturale a un nodo ipervisore: è la più recente, conserva tutta la sua memoria e ha l'unica scheda di rete Intel del gruppo, la famiglia che gli ipervisori open source trattano meglio. Le manca soltanto un disco. Proxmox VE, oggi alla versione 9.2 su Debian 13, richiede le estensioni di virtualizzazione attive nel firmware e consiglia dischi ridondanti per l'uso continuo (S88); sul processore Intel le dichiara presenti, e l'impostazione del firmware va controllata alla prima accensione, come l'inventario raccomanda per la macchina gemella. Le foto dei due PC arrivate il 09/10/2026 non cambiano la scelta e ne tolgono il costo: nessuno dei due ha memoria DDR4, ma insieme portano due SSD SATA da circa 250 GB. Il dettaglio è nell'inventario delle scorte, alla sezione sui due PC in più.

C'è un'alternativa che vale scrivere per non scartarla senza averla vista. Con PC-03 le Z97-P diventano due, e una delle due può tenere i quattro moduli DDR3 delle due macchine, cioè 32 GB: il doppio della memoria di `linux-desktop-A`, su un processore di tre generazioni prima, con una rete Realtek invece che Intel e con un consumo maggiore. Per il conto della memoria qui sotto il guadagno è reale, perché toglie il vincolo che lascia al laboratorio solo 4 GB. Resta preferibile `linux-desktop-A`, per la rete Intel e per i problemi di avvio e di tastiera già osservati su `linux-desktop-B`; ma è una scelta dell'utente, e il dato che la decide è il modello del processore di PC-03, da leggere con la raccolta.

## Quale macchina fa da server Proxmox: il confronto, e la combinazione finale

Sezione del 09/10/2026, scritta perché l'utente sta smontando PC-02 e PC-03 e vuole riassemblare una volta sola. Le due candidate sono `linux-desktop-A` e una Z97-P portata a 32 GB con la memoria DDR3 di `linux-desktop-B` e di PC-03. Per la Z97-P si sceglie la scheda di PC-03, che funziona con anduinOS, e non quella di `linux-desktop-B`, su cui il censimento ha osservato un avvio intermittente e la tastiera che non risponde nel firmware.

| Criterio | `linux-desktop-A` | Z97-P a 32 GB |
|---|---|---|
| processore | i7-7700, Kaby Lake, 14 nm, 4 core e 8 thread | i7-4790 se si sposta quello di `linux-desktop-B`, Haswell, 22 nm, 4 core e 8 thread; quello di PC-03 è da leggere |
| prestazioni (S100) | CPU Mark 8.640, single thread 2.441, circa il 19% in più | CPU Mark 7.257, single thread 2.226 |
| TDP (S100) | 65 W | 84 W |
| virtualizzazione (S101) | VT-x, EPT, VT-d | VT-x, EPT, VT-d |
| memoria oggi | 16 GB DDR4-2400 | 32 GB DDR3, quattro moduli di tre codici, a 1333 MHz |
| memoria in futuro | fino a 64 GB, comprando DDR4 (S98) | 32 GB è il tetto, e la DDR3 non si compra più volentieri |
| che cosa ci sta | Proxmox, Wazuh e AdGuard, più circa 4 GB di laboratorio | gli stessi servizi più circa 20 GB di laboratorio |
| rete | Intel I219-V | Realtek, che Proxmox gestisce ma con meno garanzie; si può aggiungere una scheda Intel PCIe |
| dischi | due alloggiamenti M.2 PCIe e SATA (S98, da confermare sul manuale) e sei porte SATA | M.2 SATA, già provato con il Samsung di PC-03, e porte SATA |
| consumo sempre acceso | il più basso dei due | più alto, perché la piattaforma è di tre anni prima; la differenza non è misurata e va presa con una presa wattmetrica |
| età | 2017 | 2014 |
| costo oggi | nessuno | nessuno |

Il consumo è il criterio che pesa negli anni, e qui va detto che cosa si sa e che cosa no. Il TDP misura il calore a pieno carico, non il consumo a riposo, che è lo stato in cui un server domestico passa quasi tutto il tempo; il TDP più alto e la piattaforma più vecchia fanno presumere che la Z97-P consumi di più anche a riposo, ma il quanto non è misurato. Per dare un ordine di grandezza: con il costo marginale di 0,256 euro al kWh del [documento sui consumi](../02-storage-di-rete-nas/05-consumo-elettrico-e-finestra-di-accensione.md), ogni 10 W di differenza continua valgono circa 88 kWh e circa 22 euro all'anno. La misura vera si prende con una presa wattmetrica, una volta assemblate le due macchine.

Il parere, del 09/10/2026: `linux-desktop-A`. Vince su processore, consumo presunto, rete e crescita della memoria, cioè su tutto ciò che conta per una macchina sempre accesa che ospita il monitoraggio; la Z97-P vince sulla sola memoria di oggi, e quel vantaggio si recupera comprando DDR4 quando il laboratorio lo chiederà, mentre gli svantaggi della Z97-P non si recuperano. La Z97-P resta preziosa nel ruolo in cui la memoria conta e il consumo no, perché è accesa a richiesta: laboratorio e analisi dei campioni.

Decisione dell'utente del 09/10/2026, registrata come ADR-030: il server è `linux-desktop-A`. Le righe che seguono restano come storia del confronto. Il server è sempre acceso e ospita il monitoraggio, quindi contano consumo, rete e margine di crescita più della memoria di oggi, e i 16 GB bastano ai servizi decisi. La Z97-P vince solo se il laboratorio deve girare sulla stessa macchina con molte macchine virtuali insieme già adesso.

Le due strade usano gli stessi pezzi, cambiano solo i dischi. Con `linux-desktop-A` server, i due SSD vanno su di lei in specchio e la Z97-P a 32 GB diventa il nodo di laboratorio, acceso solo quando serve, con il disco meccanico da 500 GB: il laboratorio sta così su una macchina fisica separata da quella che lo sorveglia, che è anche una separazione di sicurezza. Con la Z97-P server, i due SSD vanno sulla Z97-P e `linux-desktop-A` con il disco meccanico diventa il nodo di laboratorio. In entrambi i casi la Z97-P si monta allo stesso modo, quindi la si può assemblare prima della decisione e rimandare solo i dischi.

| Macchina | Che cosa contiene | Ruolo con la raccomandazione |
|---|---|---|
| `linux-desktop-A` | H270M Pro4, i7-7700, 4 × 4 GB DDR4 già montati, alimentatore suo; Samsung 850 EVO M.2 da PC-03 e Kingston V300 da PC-02 in specchio | server Proxmox SRV-01 |
| Z97-P di PC-03 | scheda e case di PC-03; i7-4790 di `linux-desktop-B` se il processore di PC-03 è inferiore; i due kit DDR3, 32 GB; disco meccanico Samsung da 500 GB di PC-02; l'alimentatore fra Atlantis e Tecnoware con la targa migliore | nodo di laboratorio, acceso a richiesta |
| `linux-desktop-B` | scheda Z97-P, processore che resta, case e alimentatore; niente memoria e niente disco | scorta del nodo di laboratorio |
| PC-02 | ne escono i due dischi, l'alimentatore, le slitte, i cavi, l'unità ottica, la minuteria, la scheda grafica e i due moduli Kingston | svuotato e smaltito (ADR-031) |
| `PC-DESKTOP-B` | invariata | scorta gemella del NAS, non si tocca |

Il nodo di laboratorio ha un costo che non è hardware: lo switch ha le otto porte già assegnate, e una macchina in più nella VLAN 60 richiede una porta. Le strade sono un modulo SFP+ con presa RJ45 in una delle due gabbie SFP+, che si compra, oppure la porta 4, oggi un client cablato nella VLAN 10, convertita alla VLAN 60 se quel client non serve. È una decisione che si prende quando il nodo serve davvero, non prima di assemblarlo.

Sullo specchio dei due SSD la scelta è fra tre strade. Con lo specchio, gratis, i due dischi tengono la stessa copia e il server continua a funzionare se uno si guasta: il V300 è il più debole e si sostituisce quando lo SMART lo indica. Con il solo Samsung, gratis, non c'è ridondanza, e un guasto ferma il server finché non si ripristina dalle copie sul NAS. Comprando un SSD nuovo si spende, e si consiglia comunque di affiancargli il Samsung in specchio. La raccomandazione è la prima, ammesso che i due dischi superino lo SMART.

## Matrice rivista e porte dello switch, 09/10/2026

L'utente ha chiesto di rifare la matrice cercando l'uso migliore di ogni macchina alla luce delle aree di studio, e di rivedere le porte dello switch. Due fatti nuovi. `linux-desktop-C`, la postazione con Ubuntu Studio (PC-06 nel censimento), resta in servizio per produzione musicale e registrazione e andrà in Wi-Fi con un adattatore USB, perché la sua scheda madre non ne ha uno integrato: la raccolta via SSH del 09/10/2026 mostra la sola rete cablata Realtek. La postazione da cui l'utente lavora a questo progetto non fa parte della rete di casa e resta fuori dal computo. I due tablet sono entrambi di casa (TAB-01 e TAB-02).

Rilette le aree di `03-spunti-di-sviluppo`, una sola cambia l'uso dell'hardware: l'analisi dei campioni sospetti (area 08), che il piano lascia pendente come zona isolata distinta dalla VLAN 60. La sandbox dinamica è il carico che chiede più memoria fra quelli del progetto, e va su una macchina fisica che non ospita servizi; la Z97-P con 32 GB, accesa a richiesta, è la candidata naturale, e aggiunge al ruolo di nodo di laboratorio quello di banco di analisi. La rete di quella zona resta da progettare. Le altre aree si risolvono senza macchine nuove: scansione delle vulnerabilità (area 16), bot (area 22) e MeshCentral (area 04) sono macchine virtuali su Proxmox; il resolver DNS dedicato dell'area 11 è già coperto da Unbound sul firewall e AdGuard su Proxmox; le telecamere dell'area 20 sono previste in Wi-Fi, perché il cavo fuori dal portone non passa; il modello linguistico locale chiede una GPU moderna, e la scheda grafica di PC-02 non lo è.

| Macchina | Ruolo proposto | Rete |
|---|---|---|
| NET-04 | firewall OPNsense | WAN, trunk LAN, DMZ fisica vuota |
| `PC-DESKTOP-A` | NAS TrueNAS SCALE | porta 5 |
| `linux-desktop-A` | server Proxmox SRV-01 | porta 6, trunk 30-60-99 |
| Z97-P di PC-03 | nodo di laboratorio e banco di analisi dei campioni, acceso a richiesta | porta da trovare, vedi sotto |
| `linux-desktop-C` | postazione multimediale con Ubuntu Studio | Wi-Fi, VLAN 10 |
| `PC-DESKTOP-B` | scorta gemella del NAS | nessuna |
| `linux-desktop-B` | scorta della Z97-P; candidata al server della DMZ se un giorno nasce un servizio pubblico | nessuna |
| PC-02 | smaltito dopo il prelievo dei pezzi (ADR-031) | nessuna |

Le porte del XMG1915-10EP sono otto in rame e due gabbie SFP+, e quelle in rame sono tutte assegnate.

| Porta | Uso | Note |
|---|---|---|
| 1 | trunk verso il firewall | |
| 2, 3 | i due AP, PoE | |
| 4 | client cablato della VLAN 10 | da assegnare a un dispositivo reale, oppure al nodo di laboratorio |
| 5 | NAS | con il secondo indirizzo di gestione di ADR-025 |
| 6 | server Proxmox, trunk 30-60-99 | |
| 7 | workstation ADMIN | |
| 8 | porta di recupero, VLAN 99 | vuota in esercizio, ma deve restare pronta |
| SFP+ 9, 10 | libere | con un modulo SFP in rame diventano due porte cablate in più |

La proposta è di non passare al modello a 16 porte. Lo XMG1915-18EP costa da circa 474 a circa 750 euro secondo il venditore (S99), contro i circa 291 euro del 10EP (ADR-023), quindi da circa 180 a circa 460 euro in più, e porta le stesse otto porte PoE: in più dà solo porte senza PoE. Due moduli SFP in rame nelle gabbie SFP+ danno due porte cablate per pochi euro ciascuno; la compatibilità dei moduli di terzi con lo switch e la velocità che accettano vanno verificate sulla documentazione Zyxel prima di comprarli. Con quelle due porte il nodo di laboratorio ha la sua porta senza togliere la 4 a un client. Il 18EP torna sensato solo se i dispositivi cablati superano le dieci prese, per esempio con telecamere cablate in PoE, che oggi non sono previste.

## Smontare i due PC: che cosa si recupera, che cosa resta in piedi, che cosa si butta

Sezione del 09/10/2026, scritta perché l'utente ha chiesto se possa smontare interamente PC-02 e PC-03 e buttare i case. La risposta è diversa per i due, e la ragione è che il case non è un contenitore vuoto: è l'unico pezzo che non si ricompra per pochi euro quando serve, perché porta con sé l'alimentatore, le gabbie dei dischi, le slitte, la minuteria e i cavi del pannello frontale.

PC-03 non si smonta: diventa il nodo di laboratorio e il banco di analisi, quindi la sua scheda Z97-P resta dentro il suo case, che va soltanto pulito dalla polvere. Ciò che entra sono i due moduli DDR3 di `linux-desktop-B`, per arrivare a 32 GB, il disco meccanico di PC-02 e, se il confronto dei modelli lo giustifica, l'i7-4790 di `linux-desktop-B`. Ciò che esce è il solo Samsung 850 EVO M.2, che va nel server.

PC-02 si smonta e il suo case si può eliminare, ma solo dopo aver tolto sei cose, e l'ordine conta perché alcune si vedono solo a case aperto. I due dischi, cioè il Kingston V300 e il Samsung HD502HJ. L'alimentatore Tecnoware FAL550FS12, di cui si conosce la targa, da confrontare con l'Atlantis di PC-03: uno dei due alimenta il nodo di laboratorio, l'altro è la scorta. Le slitte o gli adattatori da due pollici e mezzo a tre e mezzo su cui i dischi sono montati, che servono a montare gli SSD nel server e che la guida di smontaggio del NAS ha già imparato a non lasciare nel case. I cavi dati SATA, che non costano nulla ma mancano sempre quando servono. L'unità ottica, se si vuole tenere un lettore DVD in casa. E la minuteria, cioè viti del pannello, viti della gabbia dei dischi e distanziali.

L'utente ha scelto il 09/10/2026 di svuotare PC-02 e smaltirlo (ADR-031). Scheda madre, processore e case vanno insieme al conferimento, perché la piattaforma LGA1156 è del 2010, non ha ruolo nel progetto, e una scheda senza case non si rimette in servizio senza ricomprare proprio il pezzo che si è buttato. Due pezzi sfuggono alla regola e restano in casa. I due moduli Kingston si conservano in una busta etichettata: sono ridondanti, perché il nodo di laboratorio arriva già a 32 GB con i due kit Corsair, ma non occupano spazio e sono l'unico ricambio di memoria di quel nodo, a capacità ridotta, se un modulo Corsair si guastasse. E la scheda grafica dedicata si estrae e si guarda prima del conferimento, perché il suo modello non si legge nelle foto ed è l'unico pezzo di PC-02 che potrebbe servire al nodo di laboratorio.

Due verifiche prima di muovere i cacciaviti. Il case di PC-03 deve avere un alloggiamento da tre pollici e mezzo libero per il disco meccanico, e lo si guarda mentre si pulisce: se non ce l'ha, si inverte la scelta e la scheda Z97-P trasloca nel case di PC-02, perché è la scheda a essere legata al ruolo, non il telaio. E il dissipatore, una volta tolto per leggere la sigla del processore, non si rimonta senza pasta termica nuova, che va procurata prima e non dopo.

Sui pezzi che escono di casa vale una regola che il progetto applica già ai dispositivi: un disco che viene smaltito o ceduto porta con sé tutto ciò che conteneva, quindi si cancella prima di lasciarlo andare. Qui i tre dischi restano tutti in casa e vengono riscritti dall'installazione, quindi il problema non si pone; si porrebbe se si decidesse di disfarsi di uno di loro dopo averne letto lo SMART. Il case e la scheda madre non contengono dati e vanno al conferimento dei rifiuti elettronici, non al cassonetto, perché sono apparecchiature elettriche ed elettroniche.

## Il da farsi al banco, in ordine

Sequenza aggiornata al 09/10/2026, dopo ADR-030 e ADR-031. Vale per il lavoro fisico sulle macchine; la messa in opera dei servizi resta quella descritta più avanti e comincia solo quando la rete è collaudata. Il principio che ordina i passi è uno solo: ogni lettura che richiede di aprire o smontare qualcosa si fa mentre quella cosa è già aperta, perché riaprire un case per leggere un'etichetta è il modo più comune di perdere un pomeriggio.

| Passo | Che cosa si fa | Perché adesso |
|---|---|---|
| 1 | procurare pasta termica | serve ai passi 3 e 5, e senza non si rimonta un dissipatore |
| 2 | aprire PC-02, prelevare i due dischi con le loro slitte e adattatori, i cavi SATA, l'unità ottica, la minuteria, la scheda grafica e i due moduli Kingston | è lo svuotamento di ADR-031, e la scheda grafica va guardata prima che la macchina esca di casa |
| 3 | togliere il dissipatore di PC-02 e leggere la sigla del processore | è l'ultima occasione: dopo, scheda e processore vanno al conferimento |
| 4 | leggere la targa dell'alimentatore Atlantis di PC-03 e confrontarla con il Tecnoware da 550 W | decide quale dei due alimenta il nodo di laboratorio |
| 5 | aprire PC-03, pulirlo, leggere la sigla del suo processore e verificare che ci sia un alloggiamento da tre pollici e mezzo libero | se l'alloggiamento manca, la scheda Z97-P trasloca nel case di PC-02 e il conferimento si rimanda |
| 6 | confrontare i due processori LGA1150 e, se quello di `linux-desktop-B` è migliore, scambiarli | si fa con entrambe le macchine già aperte |
| 7 | montare nel nodo di laboratorio i due moduli DDR3 di `linux-desktop-B`, per arrivare a 32 GB, e il disco meccanico da 500 GB | completa il nodo di laboratorio |
| 8 | montare sul server `linux-desktop-A` i due SSD, il Samsung nell'alloggiamento M.2 e il Kingston su una porta SATA | è la configurazione di ADR-030, da riconsiderare se l'M.2 non accetta dischi SATA |
| 9 | accendere le due macchine e leggere lo SMART dei tre dischi con il test lungo | è la verifica che decide se lo specchio si può fare senza comprare niente |
| 10 | nel firmware di `linux-desktop-A`, verificare che le estensioni di virtualizzazione siano attive | Proxmox le richiede, ed è un'impostazione e non un limite del processore |
| 11 | misurare con una presa wattmetrica il consumo delle due macchine a riposo | è il numero che manca al confronto di ADR-030, e va scritto nel documento sui consumi |
| 12 | conferire scheda madre, processore e case di PC-02 ai rifiuti elettronici | solo dopo il passo 5, perché il case serve ancora se l'alloggiamento di PC-03 manca |

Fuori da questa sequenza restano due acquisti che non la bloccano, cioè l'SSD per il server se lo SMART boccia uno dei due recuperati, e i moduli SFP in rame quando il nodo di laboratorio chiede la sua porta (ADR-029).

## Il server Proxmox

È l'host di servizio sempre acceso che il progetto aspettava senza averlo individuato: ospita i servizi che non possono stare sul NAS, che si accende a orario, né sul firewall, che non esegue servizi estranei alla sicurezza di rete.

La rete è un solo cavo dalla scheda Intel alla porta 6 dello switch, configurata come trunk con le VLAN 30, 60 e 99. Su Proxmox un unico bridge consapevole delle VLAN assegna ogni macchina virtuale alla sua zona. L'interfaccia di amministrazione di Proxmox sta nella sola VLAN 99, secondo ADR-025.

| Ospite | Tipo | Zona | Memoria | Disco | Stato |
|---|---|---|---|---|---|
| Wazuh, server, indicizzatore e dashboard insieme | macchina virtuale | VLAN 30 | 8 GB | 50 GB | proposto |
| AdGuard Home, DNS filtrante davanti a Unbound | contenitore | VLAN 30 | 0,5 GB | 2 GB | proposto |
| macchine del laboratorio | macchine virtuali | VLAN 60 | il resto, circa 4 GB | secondo l'esperimento | proposto |
| Proxmox stesso | sistema ospite | VLAN 99 | 2 GB | sistema | proposto |

Il conto della memoria è il vincolo vero. Wazuh, nella configurazione con i tre componenti sulla stessa macchina, chiede 4 vCPU, 8 GB di memoria e 50 GB di spazio per un massimo di 25 agenti e 90 giorni di allarmi (S87). Con 16 GB restano circa 4 GB per il laboratorio, che bastano per due o tre macchine leggere alla volta. Portare la macchina a 32 GB toglie il vincolo; che la scheda accetti 64 GB in quattro alloggiamenti va verificato sulla scheda del costruttore, e il costo dei moduli va cercato. È una decisione dell'utente, non un requisito di partenza. La via di prendere i moduli da un altro PC di casa è chiusa dal 09/10/2026: i due PC fotografati hanno solo DDR3, e la DDR4 a 32 GB si ottiene soltanto comprandola.

Il disco forse non si compra. I due PC fotografati il 09/10/2026 portano un Samsung 850 EVO M.2 SATA da 250 GB e un Kingston V300 SATA da 240 GB, e due dischi di taglia simile sono esattamente lo specchio che Proxmox consiglia: con ZFS in mirror restano circa 240 GB utili, contro i 50 GB di Wazuh, i 2 GB di AdGuard e il sistema. Valgono tre condizioni. Entrambi devono passare la lettura SMART e il test lungo. L'alloggiamento M.2 della H270M Pro4 deve accettare un disco SATA e non solo NVMe, e lo si verifica sul manuale ASRock; altrimenti il Samsung va in un adattatore da M.2 SATA a 2,5 pollici, oppure si usa un altro disco. E il V300 ha poche scritture garantite per il carico continuo dell'indicizzatore di Wazuh, che è un'inferenza da verificare sulla scheda tecnica: se si conferma, lo specchio regge finché uno dei due non si consuma, e quel momento lo dice lo SMART. Se una delle tre condizioni cade, resta il piano di prima, cioè comprare un SSD SATA da 500 GB o 1 TB. Le copie delle macchine virtuali vanno sul NAS, nella sua finestra di accensione.

## Lo stack open source, funzione per funzione

| Funzione | Scelta | Dove | Stato |
|---|---|---|---|
| firewall, routing, VPN | OPNsense, WireGuard | NET-04 | deciso |
| rilevamento sul traffico | Suricata integrato in OPNsense, prima in sola rilevazione | NET-04 | deciso (ADR-028) |
| SIEM, rilevamento sugli host, integrità dei file | Wazuh | Proxmox, VLAN 30, dashboard nella VLAN 99 | deciso (ADR-028) |
| raccolta dei log di firewall e apparati | plugin os-wazuh-agent per il firewall e gli allarmi di Suricata; syslog per switch, AP e NAS | NET-04, apparati | deciso (ADR-028), dettaglio in [Monitoraggio](11-monitoraggio-wazuh-suricata.md) |
| indicizzazione e ricerca | l'indicizzatore di Wazuh, incluso | Proxmox | proposto |
| DNS | Unbound su OPNsense, poi AdGuard Home | NET-04, poi Proxmox | deciso dallo studio del 22/09/2026 |
| storage e copie | TrueNAS SCALE | NAS | deciso |
| scansione delle vulnerabilità | Greenbone OpenVAS, acceso quando serve | Proxmox, VLAN 60 | proposto, fase 6 |
| gestione remota degli endpoint | MeshCentral, dagli studi del documento sorgente | Proxmox, VLAN 30 | proposto, fase 4 |
| metriche di switch, AP e host | lettura SNMP dall'host di servizio, con un raccoglitore da scegliere | Proxmox | pendente |
| analisi di campioni sospetti | zona isolata a parte, non la VLAN 60 | da progettare | pendente, fase 6 |

### Che cosa resta dello schema del documento sorgente

Lo schema di monitoraggio della prima stesura, con Wazuh, ELK, Snort, Sagan, MozDef e OSSIM, metteva insieme gli strumenti open source più citati. Verificati l'8/10/2026, la metà non è più una scelta possibile.

| Componente | Stato del progetto a monte | Esito nel piano |
|---|---|---|
| Wazuh | attivo | resta, al centro |
| ELK separato | attivo | scartato: Wazuh porta già il proprio indicizzatore e la propria dashboard, e uno stack separato duplicherebbe memoria e manutenzione su una macchina da 16 GB |
| Snort | attivo, ma gli sviluppatori di OPNsense non intendono integrarlo e indicano Suricata (S89) | sostituito da Suricata, già nel firewall |
| Sagan | ultima versione stabile del febbraio 2021 (S86) | scartato: la correlazione dei log la fa Wazuh |
| MozDef | deprecato e archiviato da Mozilla, ultimo aggiornamento nel 2021 (S84) | scartato |
| OSSIM | ritirato da LevelBlue a fine 2024 (S85) | scartato |
| Apache Metron, citato come estensione | ritirato nel dicembre 2020 e archiviato nel 2021 (S90) | scartato |
| Security Onion, alternativa integrata | attivo, ma chiede almeno 24 GB di memoria anche nella forma più piccola (S91) | scartato per questa macchina; da riconsiderare con un host dedicato |

Il flusso che ne risulta è più corto e tutto mantenuto. Gli endpoint mandano eventi a Wazuh con il suo agente; il firewall e gli apparati mandano i log a Wazuh via syslog; Suricata, nel firewall, rileva sul traffico e i suoi allarmi confluiscono nello stesso punto; Wazuh correla, conserva e mostra.

```
  [ endpoint: PC, NAS, VM ] --agente--> [ Wazuh su Proxmox, VLAN 30 ]
                                               ^          |
  [ OPNsense + Suricata ] --syslog e allarmi---+          v
  [ switch, AP ] ---------------syslog---------+     allarmi, ricerca,
                                                     dashboard
```

## In che ordine, e che cosa è pendente

La sequenza rispetta la roadmap. La rete viene prima, cioè firewall, switch e AP, perché senza segmentazione ogni servizio finirebbe in una rete piatta. Proxmox viene subito dopo il collaudo delle VLAN, perché porta DNS filtrante e monitoraggio. Il NAS procede in parallelo, perché si assembla senza toccare la rete.

Decisioni aspettate dall'utente: quale macchina diventa il server Proxmox, cioè `linux-desktop-A` con 16 GB DDR4 oppure una Z97-P con 32 GB DDR3; se usare i due SSD dei PC fotografati in specchio. L'idea dell'8/10/2026 di portare `linux-desktop-A` a 32 GB con la DDR4 di uno dei due PC è caduta il 09/10/2026: le foto mostrano solo DDR3. Dati aspettati: la raccolta in sola lettura su PC-02 e PC-03, che legge i processori e la memoria totale; la lettura SMART dei loro dischi; il supporto SATA dell'M.2 della H270M Pro4; la verifica delle estensioni di virtualizzazione nel firmware; il massimo di memoria della scheda e la compatibilità dei moduli; il prezzo di un SSD; il raccoglitore di metriche. Chiusi l'8/10/2026: Suricata al posto di Snort e l'integrazione con Wazuh, con il plugin di OPNsense (ADR-028). Da progettare più avanti: la zona isolata per l'analisi dei campioni.
