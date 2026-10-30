# Registro del montaggio del NAS

Ritorno a [Storage di rete (NAS)](README.md). Registro cronologico di ciò che è stato fatto davvero al banco per assemblare il NAS su `PC-DESKTOP-A`, con le letture, la ragione di ogni scelta presa sul momento e lo scarto rispetto al piano. Il piano è nel documento canonico [Allocazione dell'hardware](../23-studio-home-lab/12-allocazione-dell-hardware.md), le decisioni nel registro delle decisioni (ADR-016, ADR-031, ADR-032, ADR-033, ADR-035). Le foto e le schermate da cui vengono le letture sono nel materiale privato, non versionato, perché mostrano numeri di serie e nomi reali delle macchine; qui si scrive che cosa mostrano.

Le voci si aggiungono in fondo, una per giornata di banco, e non si riscrivono: una lettura che si rivela sbagliata si corregge con una voce nuova che la cita.

## 14/10/2026: PC-02 aperto, dischi estratti

**Fatto.** `PC-02` è stato aperto e i due dischi tolti dalla gabbia, ancora con i cavi: il Kingston SSDNow V300 da 240 GB e il Samsung HD502HJ da 500 GB. Le etichette coincidono con il censimento del 09/10/2026.

**Letture.** Il V300 è avvitato su un adattatore Corsair da 2,5 a 3,5 pollici, che dalle foto appare integro.

**Ragione.** Il 09/10/2026 l'utente aveva dichiarato rotte le slitte di `PC-02`, e la conseguenza ricadeva sul solo V300, l'unico disco da 2,5 pollici destinato a un alloggiamento da 3,5. Con l'adattatore integro il V300 si fissa senza acquisti.

## 15/10/2026: PC-02 svuotato, gesto 1 chiuso

**Fatto.** Dalle foto dell'utente risultano fuori da `PC-02` i due dischi, l'alimentatore Tecnoware FAL550FS12 con i suoi cavi fissi, due cavi dati SATA, la minuteria e i quattro moduli DDR3. La scheda grafica è stata fotografata ancora nel case.

**Letture.** Moduli: due Kingston `KVR1333D3N9/2G` e due `KVR1333D3N9/4G`, DDR3-1333, 12 GB in tutto. Scheda grafica: NVIDIA GeForce 210, 1 GB DDR3, bus a 64 bit, uscite VGA, DVI e HDMI, raffreddamento passivo. Alimentatore: Free Silent 550 W, +12 V 30 A e 360 W, +3,3 V e +5 V 170 W combinati. Adattatore del V300: scosso a mano dall'utente, il disco non si muove e la cornice non ha parti rotte.

**Ragione.** La taglia dei due moduli rimasti nella scheda era l'ultima lettura aperta del gesto 1. Con l'alimentatore fuori, la raccolta software su `PC-02` non è più possibile; la sigla del processore resta da leggere sotto il dissipatore, utile al solo inventario perché la piattaforma va al conferimento (ADR-031). Il Tecnoware resta alimentatore di scorta e non se ne contano i connettori (ADR-035).

## 15/10/2026: base del NAS aperta

**Fatto.** `PC-DESKTOP-A` aperto dal fianco, con il cavo di corrente staccato.

**Letture.** ASUS H170-PRO rev. 1.04, dissipatore Intel di serie su LGA1151, due moduli DDR4 inseriti, alloggiamento M.2 vuoto, che è il segno di riconoscimento della base nella guida; alimentatore Corsair HX520W modulare, quello confermato da ADR-016. Nel vano alto da 5,25 un lettore ottico alimentato con un adattatore Molex verso SATA; sotto, la gabbia dei dischi, con cavi di alimentazione SATA liberi dell'HX520W e due cavi dati già collegati alla scheda madre.

## 15 e 16/10/2026: i tre dischi nel NAS, gesto 2

**Fatto.** Il V300, sulla sua cornice, è entrato nella gabbia sotto il lettore ottico, fissato con le viti da un lato solo. Ha ricevuto l'alimentazione da un connettore SATA libero dell'HX520W e il cavo dati del lettore ottico, staccato dal lettore e lasciato sulla scheda madre. Il WD Blue da 250 GB, prelevato da `PC-DESKTOP-B` a settembre, è entrato nella gabbia sulla propria cornice, con il proprio cavo dati verso una porta libera della scheda e l'alimentazione da un adattatore Molex verso SATA collegato a un Molex dell'HX520W. Il SanDisk SDSSDA240G era già nella base e non è stato toccato.

**Ragione.** Il V300 fa da disco di avvio perché è il più debole dei tre: se cede, si reinstalla TrueNAS e si ricarica la configurazione, mentre i dati restano sullo specchio di SanDisk e WD Blue (ADR-033). Il fissaggio da un solo lato si accetta perché un SSD non ha parti in movimento e due viti lo tengono fermo. Il lettore ottico rinuncia al cavo dati perché il NAS non lo usa: TrueNAS si installa da una chiavetta USB. I due cavi dati di `PC-02` sono rimasti a casa dell'utente e non sono serviti, perché il WD Blue era uscito da `PC-DESKTOP-B` con il proprio cavo, come registrato il 07/10/2026.

**Scarto dal piano.** L'allocazione voleva il SanDisk su `SATA6G_1`, il WD Blue su `SATA6G_2` e il V300 su `SATA6G_3`. Sulla scheda i dischi sono finiti su `SATA6G_1`, `SATA6G_2` e `SATA6G_6`, come mostra il paragrafo seguente. Non cambia nulla: TrueNAS riconosce i dischi dal numero di serie e non dalla porta, e il piano indicava le porte solo per dare un ordine ai gesti.

## 16/10/2026: primo avvio a case aperto, gesto 3 in corso

**Fatto.** Monitor, tastiera e corrente collegati, primo avvio a case aperto, ingresso nel firmware con il tasto Canc. La ventola del processore gira, osservata dall'utente.

**Letture del firmware, schermata EZ Mode.**

| Voce | Valore |
|---|---|
| scheda e firmware | H170-PRO, BIOS 3805 x64 del 16/05/2018, Management Engine 11.8.50.3470, PCH stepping D1 |
| processore | Intel Core i7-6700 a 3,4 GHz, rapporto 34, turbo di destinazione 4,0 GHz |
| memoria | 16384 MB DDR4, Team Group 8 GB in `DIMM_A1` e 8 GB in `DIMM_B1`, quindi doppio canale; 2133 MHz con X.M.P. spento, moduli dichiarati 2400 MHz; 1,200 V |
| dischi | `SATA6G_1` SanDisk SDSSDA240G 240 GB; `SATA6G_2` Kingston SV300S37A240G 240 GB; `SATA6G_6` WDC WDS250G1B0A 250 GB |
| ventole | processore 1064 giri al minuto, case 659 e 618 |
| temperature | processore 28 °C a freddo, fino a 33 °C dopo qualche minuto nel firmware; scheda 25 °C |
| tensioni | +12 V 12,192 V; +5 V 5,040 V; +3,3 V 3,392 V; core 1,104 V; VCCIO 0,950 V; System Agent 1,050 V |
| impostazioni | tutto in Auto nella scheda Ai Tweaker, risparmio EPU spento |
| avvio | due voci Windows Boot Manager, dal SanDisk e dal WD Blue, e due voci di rete Realtek |

**Esito rispetto ad ADR-016 e al passo 3 dell'allocazione.** Tre condizioni su quattro sono verificate: la ventola gira, il ramo a +12 V sta a 12,192 V dentro l'intervallo fra 11,4 e 12,6 V, il firmware dichiara 16 GB in doppio canale; e tutti e tre i dischi sono visti. Resta la quarta, il test della memoria per una notte senza errori.

**Ragione delle letture.** La memoria a 2133 MHz invece dei 2400 dichiarati dai moduli è la velocità standard della piattaforma con X.M.P. spento, e su un NAS acceso sempre si preferisce la stabilità alla velocità: non si cambia. Le tensioni a +5 V e +3,3 V sono entro il cinque per cento del nominale, la tolleranza della specifica ATX secondo conoscenza non verificata qui.

**Da guardare prima dell'installazione.** Il SanDisk e il WD Blue portano ancora un Windows avviabile. La creazione del pool cancella entrambi, e il SanDisk è il disco di sistema della base: prima del gesto 4 l'utente conferma che il suo contenuto non serve più o è salvato altrove. L'interruttore Intel Rapid Storage Technology della schermata EZ Mode deve lasciare i dischi in AHCI, cioè visti uno per uno da TrueNAS; dalla foto non si legge con certezza quale posizione sia selezionata.

## 16/10/2026: preparazione del test della memoria

**Fatto.** Scaricati da memtest.org l'installer USB per Windows e l'immagine ISO a 64 bit di Memtest86+ 8.10. L'impronta SHA-256 dell'installer coincide con quella registrata nella guida privata il 02/09/2026. L'immagine è stata aggiunta come file a una chiavetta già preparata con Ventoy, cioè un caricatore che avvia le immagini ISO copiate al suo interno, accanto alla vecchia immagine che la chiavetta conteneva; l'impronta del file sulla chiavetta coincide con quella scaricata.

**Ragione.** Il sito offre dal 15/10/2026 anche la versione 9.00. Si è scelta la 8.10 perché è quella di cui il progetto aveva già un'impronta di riferimento, e perché per un test di accettazione conta una versione collaudata più di una uscita il giorno prima. La chiavetta non è stata riscritta: con Ventoy basta copiare il file, e il resto del contenuto resta intatto. La vecchia immagine presente sulla chiavetta, del 2020, è da evitare, perché la guida esclude le versioni 5.x per il supporto immaturo di UEFI e DDR4. Resta da verificare che Ventoy avvii la 8.10 sulla H170-PRO; in caso contrario sulla stessa chiavetta c'è MemTest86 di PassMark, prodotto diverso e non open source, come ripiego.

## 16/10/2026: test della memoria avviato

**Fatto.** Avvio del NAS dal menu F8 sulla voce UEFI della partizione di avvio di Ventoy, la seconda della chiavetta; Ventoy è partito senza blocchi del Secure Boot. Dalla cartella del test della memoria si è scelta l'immagine 8.10, perché quella vecchia è segnata da Ventoy come avviabile solo in modalità BIOS. Memtest86+ 8.10 è partito e lavora da solo; il test resta acceso per la notte.

**Letture.** Build 8.10.49468 a 64 bit; i7-6700 con 4 core e 8 thread usati in parallelo; controller della memoria a 1069 MHz, cioè DDR4-2138, latenze 15-15-15-35; memoria in prova 15,8 GB; i due moduli letti dalla loro memoria di configurazione come 8 GB DDR4-2400 Team Group, prodotti nella settimana 40 del 2016, negli alloggiamenti che il programma numera 0 e 2; temperatura del processore fra 44 e 48 °C sotto carico. Diciassette secondi dopo la partenza, al quarto test del primo passaggio: zero errori.

**Ragione.** Il test di una notte è la quarta condizione di ADR-016 e chiude il passo 3 dell'allocazione. Una notte significa più passaggi completi: l'esito si legge al mattino nei campi Pass, che deve essere almeno 1, ed Errors, che deve restare 0. Le temperature sotto carico, sotto i 50 °C con il dissipatore di serie, dicono che il raffreddamento regge anche il carico pieno.

## 16/10/2026: primo passaggio completo del test della memoria

**Letture.** Memtest86+ ha completato il primo passaggio, con il messaggio PASS a schermo: tempo trascorso 0:34:57, Pass 1, Errors 0; il secondo passaggio era al 31 per cento. Temperatura del processore 50 °C, massimo registrato 54 °C.

**Ragione.** Un passaggio completo senza errori è il minimo che il test garantisce, ed è un buon segno. ADR-016 chiede però una notte senza errori, perché i difetti intermittenti di un modulo compaiono spesso solo con il calore e con il tempo, cioè dopo più passaggi. Un passaggio dura circa 35 minuti su 16 GB, quindi una notte ne fa una quindicina. Se l'utente sceglie di fermare il test prima, va scritto qui come scostamento dalla condizione di ADR-016, con il numero di passaggi effettivamente completati.

## 16/10/2026: il test della memoria trova un errore

**Letture.** Dopo 3 ore, 46 minuti e 14 secondi Memtest86+ dichiara Status Failed con un errore: quattro passaggi completi, l'errore nel quinto, contato come passaggio 4, durante il test 6, Moving inversions con schema a 64 bit, sul processore logico 4. Indirizzo fisico 0x3a03f65e0, cioè a circa 14,5 GB. Valore atteso `ffffffff7fffffff`, letto `ffffffffffffffff`: un solo bit, il 31, letto a 1 invece che a 0. Temperatura del processore 49 °C, massimo 54 °C. La memoria girava alle impostazioni di fabbrica, 2133 MHz e 1,2 V con X.M.P. spento.

**Ragione.** Un errore di memtest è un errore, anche se singolo e comparso tardi: è proprio il caso per cui ADR-016 chiede una notte e non un passaggio, perché i primi quattro passaggi erano puliti. La quarta condizione di ADR-016 non è soddisfatta, e il NAS non riceve dati finché l'errore non è spiegato, perché un modulo difettoso corrompe i dati in silenzio. Con due moduli in doppio canale l'indirizzo non dice da solo quale modulo sia, perché il controller alterna i due canali a blocchi piccoli; si procede quindi con l'isolamento descritto nella guida privata al passo 4.2.d: un modulo per volta nello stesso alloggiamento `DIMM_A1`, così da provare i moduli e non gli alloggiamenti. Poiché l'errore è comparso solo dopo quasi quattro ore con 16 GB, ogni modulo da solo va provato per un tempo paragonabile e non per un solo passaggio. Il ricambio previsto da ADR-032 sono i due moduli Crucial da 4 GB rimasti di scorta, che ridanno 16 GB insieme al modulo sano.

**Scelta dell'utente.** Il test non si ferma: resta acceso fino a lunedì 19/10/2026, quando si leggeranno numero di passaggi, numero di errori e indirizzi. Se gli errori saranno più di uno e torneranno sullo stesso indirizzo, il sospetto cade su un modulo; se saranno sparsi, sulla causa comune che la guida privata prevede al passo 4.2.f. In entrambi i casi segue l'isolamento dei moduli.

## 17/10/2026: PC-02 dismesso, GeForce recuperata e stato reale di PC-03

**Fatto.** L'utente conferma il recupero della GeForce 210 e la dismissione di PC-02. La nuova foto mostra la scheda fuori dal case; l'etichetta dichiara GF210, 1024M SDDR3, bus a 64 bit e uscite CRT, DVI e HDMI. Non è stata eseguita una prova di funzionamento. La si conserva come scorta video per diagnosi, senza installarla in una macchina del progetto; il modello linguistico locale resta previsto sul solo processore (ADR-034). Il recupero del lettore DVD non è confermato dalla dismissione.

**Letture.** L'utente identifica l'alimentatore nella seconda foto come quello attualmente montato in PC-03. Targa Atlantis P016-MPW-6000-W, ingresso 115/230 V, 10/6 A, 60/50 Hz; potenza totale 600 W massimi dichiarati. Uscite +3,3 V 24 A, +5 V 30 A, 150 W combinati; +12V1 22 A e 264 W, +12V2 22 A e 264 W; -12 V 0,5 A e 6 W; +5Vsb 2,5 A e 12,5 W. I valori sono dichiarazioni dell'etichetta, non misure di potenza erogata o di salute; le due colonne +12 V non provano da sole una potenza combinata. L'alimentatore resta in PC-03 per ADR-035.

**Correzione dello stato dei dischi.** PC-03 non contiene alcun SSD secondo la dichiarazione attuale dell'utente. Il Samsung 850 EVO M.2 SATA da 250 GB era visibile nelle foto del 09/10; il piano dello stesso giorno ne prevedeva l'estrazione per il server, mentre ADR-033 del 12/10 lo riassegnava al laboratorio. La ricerca in memoria, guida privata, indice delle foto e storia git non ha trovato una conferma del prelievo né del rimontaggio. Le frasi «già montato» dell'allocazione e della ripresa ripetevano il piano senza una verifica fisica e sono corrette. La destinazione resta il laboratorio, l'ubicazione attuale è da verificare; l'utente deve controllare anche in un'altra stanza. Non si dichiara il disco perso né se ne propone l'acquisto.

**Evidenze.** Due foto lette e copiate nell'archivio privato dei due PC, con confronto SHA-256 identico per ciascun originale e la sua copia, due su due. L'indice privato e il manifesto di importazione conservano l'abbinamento. Gli originali Telegram si cancellano su richiesta esplicita dell'utente solo dopo la verifica delle copie e la trascrizione; l'esito della cancellazione si annota a operazione conclusa.

**Archiviazione conclusa.** I due originali Telegram sono stati cancellati dopo un nuovo confronto delle impronte con le copie archiviate; verificata l'assenza di entrambi gli originali e la permanenza delle due copie con impronta invariata. Il manifesto privato registra l'esito per ciascun file.

## 19/10/2026: disco di PC-02 identificato e lettura del test della memoria

**Disco.** L'immagine indicata dall'utente come disco di PC-02 mostra il Samsung HD502HJ, 500 GB, 7200 giri al minuto, 16 MB di cache, interfaccia SATA a 3 Gb/s, revisione A, fabbricato nell'agosto 2011. Coincide con il disco meccanico già censito e recuperato da PC-02, destinato alle prove del nodo di laboratorio. Non è il Samsung 850 EVO M.2 SATA da 250 GB ancora da localizzare. La foto dell'etichetta non costituisce lettura SMART né prova di salute; montaggio e collaudo restano aperti. Nessun seriale o identificativo della targhetta è trascritto qui.

**Memoria.** La nuova foto del monitor mostra Memtest86+ 8.10, build 8.10.49468.x64, i7-6700, 15,8 GB testati, quattro core e otto thread in parallelo, DDR4-2138 con latenze 15-15-15-35. Tempo 3:46:14, Pass 4, Errors 1, Status Failed, quinto passaggio al 45 per cento, test 6 al 89 per cento, temperatura 49 °C e massimo 54 °C. Un errore sul processore logico 4, passaggio 4, test 6, indirizzo 0x3a03f65e0 a circa 14,5 GB, atteso ffffffff7fffffff e letto ffffffffffffffff: lo stesso bit e gli stessi contatori già documentati il 16/10.

**Limite della lettura.** Questi contatori non provano un test continuato per tutto il fine settimana né una serie nuova di passaggi puliti; la data della cattura non misura il tempo di esecuzione. Il fermo dei valori può avere cause diverse, non determinate dalla sola foto. In basso compare «Scroll unlock», che nel codice della versione 8.10 indica scroll lock attivo. Il manuale dice che il blocco può mettere il test in attesa se l'area dei messaggi è piena; questo non dimostra che sia ciò che è successo qui, dove è visibile una sola riga di errore. Fonti: [manuale 8.10](https://raw.githubusercontent.com/memtest86plus/memtest86plus/v8.10/README.md), [codice del display](https://raw.githubusercontent.com/memtest86plus/memtest86plus/v8.10/app/display.c) e [codice degli errori](https://raw.githubusercontent.com/memtest86plus/memtest86plus/v8.10/app/error.c), S126-S128.

**Prossimo riscontro.** Premere una sola volta Spazio sul NAS e osservare se la scritta del comando e il contatore Time cambiano; il cambiamento del tempo è il riscontro che distingue un test che avanza da una schermata ferma. Il comando cambia lo scroll lock e non riavvia il test. L'esito della pressione non è ancora ricevuto; non si dichiara il problema risolto e TrueNAS resta in attesa. L'isolamento dei due moduli rimane il passo successivo al chiarimento di questa lettura, senza attribuire già il guasto a un modulo specifico.

**Evidenze.** Due immagini lette dalla cartella di cattura e copiate nell'archivio privato delle macchine corrispondenti, con impronte SHA-256 identiche agli originali per entrambe. Indice e manifesto privati conservano percorsi e derivazione.

## 19/10/2026: nessuna risposta alla barra spaziatrice

**Riscontro dell'utente.** Premendo Spazio il NAS non produce alcuna risposta e la schermata resta bloccata. La verifica dello sblocco non ha quindi mostrato una ripresa; non si attribuiscono al fine settimana ulteriori passaggi del test.

**Interpretazione.** Il test non è concluso e l'errore di memoria rimane aperto. La mancata risposta non distingue da sola un blocco del programma, un problema dell'ingresso da tastiera o una causa hardware comune e non identifica un modulo guasto. Non si insiste con lo sblocco come se fosse una soluzione verificata.

**Prossimo gesto.** Tenere premuto il pulsante di accensione finché il NAS si spegne, indicativamente cinque-dieci secondi, e attendere conferma dell'arresto. Lo spegnimento non è ancora confermato. Seguiranno lo scollegamento dell'alimentazione e, solo dopo, la preparazione della prova di un modulo da 8 GB alla volta nello stesso DIMM_A1; non si prescrive ancora alcuna estrazione con la macchina alimentata. TrueNAS resta in attesa.

## 19/10/2026: spegnimento del NAS confermato

**Fatto.** L'utente conferma il NAS spento e chiede di procedere. Non è ancora confermato lo scollegamento del cavo di alimentazione; nessun modulo risulta rimosso.

**Prossimo gesto.** Scollegare il cavo di corrente dal retro del NAS e attendere conferma prima di identificare o rimuovere i moduli di memoria. Rimane prevista la prova di un modulo da 8 GB alla volta nello stesso DIMM_A1, senza attribuire già il guasto a un modulo specifico.

## 19/10/2026: alimentazione scollegata

**Fatto.** L'utente conferma scollegato il cavo di corrente del NAS, già spento. Nessun modulo è ancora stato rimosso.

**Prossimo gesto.** A cavo scollegato, tenere premuto il pulsante di accensione per cinque secondi, come previsto dal passo 1.1 della guida privata per scaricare l'alimentazione residua della scheda. Il gesto non è ancora confermato; seguirà l'identificazione visiva dei due moduli prima della rimozione.

## 19/10/2026: preparazione prima della rimozione della memoria

**Fatto.** L'utente conferma la pressione del pulsante di accensione per cinque secondi con NAS spento e cavo scollegato. La sequenza di preparazione del passo 1.1 è eseguita per quanto dichiarato; nessun modulo è ancora rimosso.

**Prossimo riscontro.** Foto ravvicinata dei due moduli di memoria e dei quattro alloggiamenti accanto alla ventola Intel del processore, includendo i fermi alle estremità. Le foto archiviate del 15/10 permettono di riconoscere la zona ma non mostrano tutti i fermi con sufficiente chiarezza per guidare lo sgancio. Si attende la nuova foto prima di indicare il fermo da aprire e il modulo da togliere; il primo test resta previsto con un solo modulo in DIMM_A1.

## 19/10/2026: alloggiamenti della memoria e fermo identificati

**Fatto.** Quattro nuove immagini mostrano entrambi i moduli ancora inseriti. Il modulo più vicino alla ventola Intel occupa DIMM_A1; il secondo modulo, più lontano dalla ventola e vicino al connettore di alimentazione a 24 poli, occupa DIMM_B1. DIMM_A2 e DIMM_B2 sono vuoti. La posizione coincide con il firmware letto il 16/10; nessuna estrazione è avvenuta secondo le informazioni ricevute.

**Verifica.** Il [manuale ufficiale ASUS H170-PRO](https://dlcdnets.asus.com/pub/ASUS/mb/LGA1151/H170-PRO/E12046_H170-PRO_UM_V2_WEB.pdf), E12046 revisione V2, pagine 1-2 e 1-9, conferma disposizione e fermo mobile su un solo lato. Confrontate le figure con le foto: il fermo mobile è all'estremità superiore nell'orientamento delle immagini, il lato inferiore è fisso. Fonte S130, copia del manuale nella parte privata.

**Prossimo gesto.** Aprire soltanto il fermo mobile superiore del modulo in DIMM_B1, il più lontano dalla ventola Intel, spingendolo verso l'esterno dello slot, cioè verso il bordo alto della scheda nell'orientamento delle foto. Il lato inferiore è fisso. Apertura e rimozione non ancora confermate; il modulo in DIMM_A1, vicino alla ventola, resta inserito. In questo modo il primo test userà il solo modulo già presente in DIMM_A1, senza spostarlo; il modulo estratto verrà identificato prima di scambiarli. Non si deduce quale dei due abbia causato l'errore.

**Evidenze.** Le quattro immagini sono lette e archiviate nella parte privata del NAS, con SHA-256 identico agli originali per ciascuna, quattro su quattro. Indice e manifesto privati aggiornati; nessun seriale o identificativo delle etichette è trascritto nel documento pubblico.

## 19/10/2026: modulo B1 estratto, rimane il solo A1

**Fatto.** Due nuove immagini mostrano un modulo fuori dal case e un solo modulo ancora inserito, quello vicino alla ventola Intel in DIMM_A1; DIMM_B1 è vuoto. La rimozione è quindi già eseguita. L'etichetta del modulo estratto dichiara Team Group TED48G2400C16BK, 8 GB DDR4-2400, latenze CL16-16-16-39, 1,2 V. Gli identificativi individuali dell'etichetta restano soltanto nell'immagine privata.

**Tracciamento.** Per la diagnosi si distinguono il modulo rimasto in A1 e quello estratto da B1. Nessuno dei due è ancora dichiarato sano o guasto. Il primo test riguarderà il solo modulo già rimasto in A1, 8 GB nominali; il test non è ancora avviato. L'ultima conferma operativa era NAS spento, cavo scollegato e pressione del pulsante a corrente tolta eseguita.

**Prossimo gesto.** Ricollegare il cavo di corrente, accendere il NAS e premere ripetutamente F8 per fermarsi al menu di selezione del dispositivo di avvio, senza scegliere ancora un disco. È un solo passaggio operativo, l'accesso al menu; selezione di Ventoy, avvio del test e verifica degli 8 GB seguiranno dal riscontro della schermata. Il manuale ASUS, fonte S130, conferma F8 all'avvio.

**Evidenze.** Le due nuove immagini sono archiviate nella parte privata del NAS con impronte SHA-256 identiche agli originali, due su due; indice e manifesto aggiornati.

## 19/10/2026: primo avvio con il solo A1 e menu della chiavetta

**Fatto.** Il NAS è riacceso e la schermata EZ Mode del firmware conferma il solo modulo in DIMM_A1: 8192 MB totali. Non è un esito del test della memoria.

| Voce letta | Valore |
|---|---|
| scheda, firmware e processore | H170-PRO, BIOS 3805, i7-6700 a 3400 MHz |
| memoria totale e velocità | 8192 MB DDR4 a 2133 MHz |
| alloggiamenti | A1 Team Group 8192 MB, dichiarati 2400 MHz; A2, B1 e B2 N/A |
| X.M.P. | Disabled |
| temperature e tensione | processore 29 °C, scheda 26 °C, core 1,104 V |
| ventole | processore 1069, case 688 e 645 giri al minuto |
| dischi | SATA6G_1 SanDisk SDSSDA240G 240 GB; SATA6G_2 Kingston SV300S37A240G 240 GB; SATA6G_6 WD WDS250G1B0A 250 GB; porte 3, 4 e 5 N/A |
| Intel Rapid Storage Technology | Off appare evidenziato; la modalità SATA AHCI resta da leggere direttamente prima dell'installazione |
| orologio mostrato | 19/10/2026, 11:19 |

**Menu di avvio.** Una seconda immagine mostra il menu F8, con le tre unità SATA, due Windows Boot Manager, le voci di rete e la chiavetta Generic da 59600 MB nelle varianti UEFI Partition 1, UEFI Partition 2 e senza UEFI. È selezionata «UEFI: Generic, Partition 2 (59600MB)», la stessa voce che aveva avviato Ventoy il 16/10. La comparsa di questo menu conferma anche la risposta al comando F8 dopo il riavvio, senza risolvere la causa del precedente blocco in Memtest.

**Prossimo gesto.** Premere Invio sulla voce già selezionata e attendere il menu Ventoy. Avvio di Ventoy e nuovo test del modulo rimasto in A1 non ancora confermati; il modulo estratto da B1 resta separato.

**Evidenze.** Le due immagini sono lette e archiviate nella parte privata, ciascuna con SHA-256 identico al proprio originale. Indice e manifesti privati aggiornati.

## 19/10/2026: Ventoy aperto sul solo modulo A1

**Fatto.** L'immagine successiva mostra il menu principale Ventoy con tema Medicat USB v21.12 e indicazione UEFI. La scelta della chiavetta è quindi riuscita. È evidenziata la prima categoria; Diagnostic Tools è la quarta voce visibile.

**Prossimo gesto.** Selezionare Diagnostic Tools e premere Invio. La cartella MemTest86+ e l'immagine 8.10 verranno selezionate dai menu successivi. Nessun primo test individuale ancora in esecuzione; rimane il solo modulo da 8 GB in A1.

**Evidenza.** Immagine letta e copiata nella parte privata del NAS con SHA-256 identico all'originale; indice e manifesto aggiornati.

## 19/10/2026: cartella Diagnostic Tools aperta

**Fatto.** La nuova immagine mostra il sottomenu Diagnostic Tools di Ventoy, con la riga di ritorno evidenziata. Le voci successive sono HDAT2, PassMark MemTest86, MemTest86+, Spinrite e Ultimate Boot CD. La voce da usare per mantenere la stessa prova è MemTest86+, distinta dal programma PassMark.

**Prossimo gesto.** Tre pressioni di Freccia giù dalla riga attuale, poi Invio su MemTest86+. La cartella delle immagini e il test 8.10 sul solo A1 non sono ancora avviati. Immagine archiviata nella parte privata con SHA-256 identico all'originale, indice e manifesto aggiornati.

## 19/10/2026: immagine Memtest86+ 8.10 selezionata

**Fatto.** La cartella Diagnostic Tools/MemTest86+ è aperta e mt86plus_8.10_x86_64.iso è già evidenziata. È l'immagine 8.10 usata nella prova precedente con due moduli; il nuovo test sarà sul solo modulo rimasto in A1, 8 GB.

**Prossimo gesto.** Premere Invio sull'immagine evidenziata e acquisire la schermata successiva. Non è ancora confermato l'avvio di Memtest; eventuale menu intermedio e primi contatori saranno registrati dal riscontro. Immagine letta e archiviata con SHA-256 identico all'originale, indice e manifesto privati aggiornati.

## 19/10/2026: scelta della modalità di avvio dell'immagine

**Fatto.** Dopo la scelta della ISO 8.10 compare il menu di Ventoy con Boot in normal mode già evidenziato; seguono le modalità grub2 e memdisk, il controllo del file e il ritorno al menu precedente. Memtest non è ancora partito.

**Prossimo gesto.** Premere Invio su Boot in normal mode e acquisire la schermata successiva. Rimane montato il solo A1 da 8 GB; avvio del programma e primi contatori non ancora confermati. Immagine archiviata con SHA-256 identico all'originale, indice e manifesto privati aggiornati.

## 19/10/2026: primo test individuale del modulo rimasto in A1

**Fatto.** Dopo Boot in normal mode, Memtest86+ 8.10 è in esecuzione; l'utente conferma l'avvio. Rimane montato il solo modulo da 8 GB in A1, quello vicino alla ventola; il modulo estratto da B1 resta separato.

| Voce letta nella prima schermata | Valore |
|---|---|
| versione e build | Memtest86+ 8.10, 8.10.49468.x64 |
| memoria | 7,85 GB utilizzabili; SPD di un solo modulo Team Group da 8 GB DDR4-2400 |
| esecuzione | Time 0:00:05, Pass 0, Errors 0, Status Testing |
| prova corrente | test 3 Moving inversions, 1s & 0s al 29%; primo passaggio allo 0%, intervallo 1-2 GB |
| processore e parallelismo | i7-6700 a 3400 MHz, 4 core, 8 thread; SMP 8T PAR |
| controller e latenze | IMC 1069 MHz, DDR4-2138, CAS 15-15-15-35; il firmware precedente indicava il valore nominale 2133 MHz con X.M.P. spento |
| temperatura mostrata | 42/48 °C |
| comandi a piè di pagina | Esc Exit, F1 Configuration, Space Scroll Lock |

**Limite della lettura.** Cinque secondi senza errori attestano l'avvio, non qualificano il modulo e non risolvono l'errore visto con due moduli. Serve anche un riscontro successivo dell'avanzamento: nella precedente prova il tempo si era fermato a 3:46:14.

**Prossimo gesto.** Lasciare il test in esecuzione e fra 10-15 minuti verificare che Time e i contatori avanzino. Durata prevista almeno quattro ore, preferibilmente una notte; inviare il riscontro se compaiono errori o se il tempo si ferma. Dopo questa prova, testare il modulo estratto da B1 da solo nello stesso A1, con spegnimento e scollegamento prima dello scambio.

**Evidenza.** Prima schermata letta e archiviata nella parte privata, SHA-256 identico all'originale Screenpresso conservato; indice e manifesto aggiornati.

## 19/10/2026: un passaggio individuale pulito, test ancora in corso

**Fatto.** Due nuove immagini mostrano l'avanzamento di Memtest86+ 8.10 sul solo modulo rimasto in A1, 8 GB nominali e 7,85 GB utilizzabili. Un passaggio è completo senza errori, il secondo è in corso.

| Voce letta | Prima immagine | Seconda immagine |
|---|---|---|
| Time | 0:53:16 | 0:53:36 |
| Pass ed Errors | 1 e 0 | 1 e 0 |
| Status | Pass | Pass |
| avanzamento del secondo passaggio | 54% | 55% |
| test corrente | 8 Random number sequence, 30% | 8 Random number sequence, 42% |
| intervallo in prova | 1-2 GB | 2-3 GB |
| temperatura mostrata | 48/52 °C | 48/52 °C |
| banner e comando inferiore | PASS verde; Space Scroll unlock | banner assente; Space Scroll Lock |

**Interpretazione.** Il tempo avanza di venti secondi e cambiano fase e intervallo in prova: non è una ripetizione della stessa schermata ferma. Il banner PASS corrisponde al passaggio completato; non chiude il collaudo di questo modulo. Non è documentato quale tasto sia stato premuto fra le immagini e questi riscontri non spiegano la causa del precedente blocco con due moduli.

**Prossimo gesto.** Lasciare il test almeno fino a Time 4:00:00, preferibilmente una notte, poi raccogliere una nuova schermata; anticipare il riscontro se compaiono errori o si ferma il tempo. Successivamente provare il modulo estratto da B1 da solo nello stesso alloggiamento A1, con spegnimento e scollegamento prima dello scambio. Nessun modulo ancora qualificato.

**Evidenze.** Entrambe le immagini sono lette e archiviate nella parte privata, copie con SHA-256 identico ai rispettivi originali Screenpresso conservati; indice e manifesto aggiornati.

## 19/10/2026: primo test individuale fallito sul solo A1

**Fatto.** Memtest86+ 8.10 segnala un errore anche con il solo modulo da 8 GB rimasto in A1. Il modulo estratto da B1 non è presente nella prova e resta separato.

| Voce letta | Valore |
|---|---|
| memoria utilizzabile e controller | 7,85 GB, DDR4-2138, CAS 15-15-15-35, 8 thread PAR |
| tempo, passaggi, errori e stato | Time 2:51:08, Pass 3, Errors 1, Status Failed |
| avanzamento | quarto passaggio 58%, test 8 Random number sequence 93%, intervallo 7-8 GB |
| temperatura mostrata | 48/52 °C |
| riga errore | pCPU 5, Pass 3, Test 8 |
| indirizzo | 0x1efab15d8, indicato come 7,74 GB |
| atteso | e7e3be2fa2c35822 |
| letto | e7c3be2fa2c35822 |
| differenza calcolata | XOR 0x0020000000000000: un bit, posizione 53, da 1 a 0 |

**Limite della misura.** Time è il tempo della schermata ricevuta, non l'istante esatto del primo errore. Una sola foto non documenta se il test continui o sia bloccato. Il dato sufficiente è che il collaudo della configurazione attuale è fallito: non serve attendere quattro ore per registrarlo come tale.

**Diagnosi ancora aperta.** Il modulo rimasto in A1 non è qualificato per il NAS, ma non va già dichiarato unico componente guasto. Come precisa il [manuale ufficiale della versione 8.10](https://raw.githubusercontent.com/memtest86plus/memtest86plus/v8.10/README.md), fonte S126, il test coinvolge anche CPU, cache e scheda madre. Il prossimo confronto discriminante cambia il solo modulo: quello estratto da B1, da solo nello stesso A1. Un esito diverso orienterà la diagnosi; errori su entrambi richiederanno prove sulle cause comuni. Corretta anche la vecchia indicazione della guida privata di scartare automaticamente un modulo dopo una sola prova individuale fallita.

**Prossimo gesto.** Tenere premuto il pulsante di accensione finché il NAS si spegne e attendere conferma. Spegnimento attuale, scollegamento e scambio non sono ancora eseguiti; le conferme di spegnimento precedenti riguardano la preparazione del primo test. TrueNAS resta sospeso.

**Evidenza.** Immagine letta e archiviata nella parte privata con SHA-256 identico all'originale Screenpresso conservato; indice e manifesto aggiornati.

## 19/10/2026: spegnimento confermato dopo l'errore individuale

**Fatto.** L'utente conferma il NAS spento dopo il primo test individuale fallito sul solo modulo A1. Il modulo estratto da B1 resta separato; nessuno scambio di memoria ancora eseguito.

**Prossimo gesto.** Scollegare il cavo di alimentazione dal retro del NAS e attendere conferma. Questo nuovo scollegamento non è ancora documentato; seguirà la preparazione a corrente tolta prima di scambiare i moduli e provare l'estratto da B1 da solo nello stesso A1.

## 19/10/2026: alimentazione scollegata dopo la prova individuale

**Fatto.** Dopo il NAS spento, l'utente conferma il cavo di alimentazione scollegato. Rimane inserito il solo modulo A1; l'altro, estratto da B1, resta separato. Nessuno scambio ancora eseguito.

**Prossimo gesto.** Tenere premuto il pulsante di accensione per cinque secondi con il cavo staccato e attendere conferma prima di guidare lo scambio. La pressione già confermata prima del primo test non documenta questo nuovo passaggio.

## 19/10/2026: preparazione a corrente tolta completata, prossimo A1 da estrarre

**Fatto.** L'utente conferma anche la pressione del pulsante di accensione per cinque secondi con il cavo staccato. Spegnimento, scollegamento e preparazione dopo il primo test individuale fallito sono quindi confermati. A1 risulta ancora inserito, il modulo già estratto da B1 resta separato.

**Prossimo gesto.** Estrarre il modulo rimasto vicino alla ventola Intel, A1, aprendo il solo fermo mobile superiore; prenderlo dai bordi e tenerlo separato dall'altro. Il lato inferiore è fisso secondo il manuale S130 e le foto già lette. Richiesta foto del modulo estratto per tracciarlo, senza supporre già avvenuta l'estrazione. Il passaggio successivo sarà inserire l'ex B1 da solo nello stesso A1 e avviare la seconda prova; nessun inserimento ancora eseguito.

## 19/10/2026: altro modulo in A1 e assenza di segnale video

**Fatto.** L'utente conferma di avere già tolto il modulo del primo test fallito e montato l'altro, prima in B1, da solo in A1. Alla riaccensione il monitor riferisce nessun input video. Lo scambio è registrato su dichiarazione; non ci sono nuove immagini o letture del firmware, né conferma dell'avvio di Memtest. Ventole, completo inserimento e collegamenti video non ancora verificati. La richiesta precedente della foto del modulo estratto è superata per proseguire dal nuovo stato.

**Interpretazione.** È un problema di avvio o visualizzazione ancora da isolare; il secondo modulo non ha ancora un esito di collaudo. Le FAQ ufficiali ASUS S131-S132 indicano il controllo dell'inserimento completo della memoria e dei collegamenti e ingresso monitor. Il riavvio dopo lo scambio non dimostra da solo quale componente sia guasto.

**Prossimo controllo.** Spegnere il NAS, scollegare l'alimentazione e tenere premuto il pulsante per cinque secondi; a cavo staccato reinserire lo stesso modulo nel solo A1, con tacca allineata e due estremità completamente in sede, fino alla chiusura del fermo mobile. Poi ricollegare, riaccendere e osservare per un minuto, riferendo se torna il logo ASUS o manca ancora il segnale e se le ventole restano in moto. La finestra di un minuto è un'attesa operativa, non un'affermazione sulla causa o sui tempi di inizializzazione di questa scheda. Tentativo ancora da eseguire; se persiste, controllare cavo e ingresso monitor prima di altri cambi. Nessun reset del firmware o intervento sulla CPU richiesto.

## 19/10/2026: video tornato, parte il test del secondo modulo nel solo A1

**Fatto.** L'utente conferma ripartenza e il nuovo riscontro mostra Memtest86+ 8.10 avviato. Secondo lo scambio già dichiarato, è il modulo da 8 GB prima in B1, ora da solo nello stesso A1 usato per il primo test. Il primo modulo, con un errore nella foto a Time 2:51:08, Pass 3, resta estratto.

| Voce letta nella prima schermata del secondo test | Valore |
|---|---|
| programma | Memtest86+ 8.10, build 8.10.49468.x64 |
| memoria | 7,85 GB utilizzabili; un modulo SPD Team Group da 8 GB DDR4-2400 |
| tempo, passaggi, errori e stato | Time 0:00:07, Pass 0, Errors 0, Status Testing |
| avanzamento | primo passaggio 1%, test 3 Moving inversions 1s & 0s 71%, intervallo 4-5 GB |
| pattern corrente | 0x0000000000000000 |
| controller e parallelismo | DDR4-2138, CAS 15-15-15-35, 8 thread PAR |
| temperatura mostrata | 38/45 °C |
| comando inferiore | Space Scroll Lock |

**Limite del riscontro.** Il video è tornato dopo il tentativo di reinserimento proposto, ma non sono documentate separatamente tutte le azioni intermedie; la causa dell'assenza di segnale non è isolata con certezza. I sette secondi senza errori attestano soltanto la partenza della seconda prova: nessun modulo ancora qualificato. L'avanzamento della nuova esecuzione richiede una lettura successiva.

**Prossimo gesto.** Lasciare il test almeno fino a Time 4:00:00, preferibilmente una notte, poi raccogliere una nuova schermata; anticipare il riscontro se compaiono errori o il tempo si ferma. Il confronto resta con il primo modulo nello stesso A1; nessun altro scambio mentre il test è acceso. TrueNAS resta sospeso.

**Evidenza.** Immagine letta e archiviata nella parte privata con SHA-256 identico all'originale Screenpresso conservato; indice e manifesto aggiornati.

## 19/10/2026: avanzamento del banner del primo passaggio, riferito dall'utente

**Fatto.** L'utente riferisce di avere fatto avanzare il banner del primo passaggio del secondo test. Non invia una nuova immagine e non comunica Time o Errors; l'ultima lettura quantitativa conservata resta quella dell'avvio. Il riscontro è qualitativo e non conclude il collaudo del secondo modulo.

**Lavoro parallelo.** L'utente ribadisce la prosecuzione autonoma del piano di backup e ripristino durante l'attesa, senza richiedere altre conferme per il lavoro indipendente. Nessun nuovo intervento fisico richiesto.

## 20/10/2026: anche il secondo modulo fallisce nello stesso alloggiamento

**Fatto.** Una nuova immagine mostra Memtest86+ 8.10 build 8.10.49468.x64 con il secondo modulo da 8 GB, ex B1 ora da solo in A1 secondo lo scambio confermato il 19/10. Memoria utilizzabile 7,85 GB, Time 3:03:15, Pass 3, Errors 2, Status Failed. Quarto passaggio al 93%, test 9 Modulo 20 random pattern all'87%, intervallo 7-8 GB; 47/52 °C, DDR4-2138 CAS 15-15-15-35, SMP 8T PAR. Il banner del primo passaggio era stato fatto avanzare dall'utente; ciò non era una qualificazione del modulo.

| Riga | pCPU | Pass | Test | Indirizzo | Atteso | Letto | Differenza calcolata |
|---|---|---|---|---|---|---|---|
| 1 | 0 | 2 | 9 | 0x0000b479e178, 2,81 GB | 0xa931a322538b440e | 0xa931a722538b440e | XOR 0x0000040000000000, bit 42 |
| 2 | 3 | 3 | 9 | 0x00019fdf8960, 6,49 GB | 0xf7f6f811401eb706 | 0xf7f6fa11401eb706 | XOR 0x0000020000000000, bit 41 |

**Verifica.** Copia della nuova immagine archiviata nella parte privata e confrontata SHA-256, identica all'originale Screenpresso conservato. I valori provengono dalla schermata; XOR e numero di bit sono calcoli sui due valori trascritti. Non sono stati ripetuti il test o una prova fisica dall'agente. Una sola immagine non prova un blocco a tre ore né un'esecuzione continua durante la notte: non si attribuisce durata al periodo trascorso sulla base dell'orario di cattura.

**Diagnosi.** Sono fallite entrambe le prove individuali nello stesso A1, oltre alla prova iniziale con la coppia. Questo confronto non separa due moduli difettosi dalle cause comuni. Il [manuale Memtest86+ 8.10](https://raw.githubusercontent.com/memtest86plus/memtest86plus/v8.10/README.md), S126 riletto il 20/10, precisa che il test coinvolge CPU, cache e scheda madre. Nessuna qualifica per TrueNAS; non si scarta automaticamente la coppia. Il prossimo confronto deve cambiare una sola variabile, per esempio lo slot mantenendo lo stesso modulo e le stesse impostazioni, con mappatura verificata sul manuale della H170-PRO e memoria nota sana se disponibile.

**Prossimo gesto.** Spegnere il NAS tenendo premuto il pulsante di accensione fino all'arresto. Prima di qualsiasi spostamento seguiranno scollegamento della corrente e verifica di assenza di alimentazione. In questo giro non è ancora confermato alcuno di questi gesti e non si chiede di toccare la RAM sotto tensione.

## 20/10/2026: NAS spento, priorità al versionamento

**Fatto.** L'utente conferma di avere spento il NAS dopo il secondo test individuale fallito. Non è confermato lo scollegamento della corrente né un ulteriore spostamento dei moduli: il secondo, ex B1, resta nell'ultimo A1 dichiarato e il primo rimane estratto. La conferma dell'arresto non qualifica la memoria e non cambia i risultati delle due prove.

**Lavoro successivo.** Su richiesta dell'utente si prepara ora il versionamento della documentazione e degli strumenti. Nessuna nuova azione fisica richiesta durante questa preparazione; prima del futuro confronto su un altro alloggiamento serviranno alimentazione rimossa e identificazione dello slot. TrueNAS resta sospeso.

## 20/10/2026: alimentazione scollegata dopo il versionamento

**Fatto.** Dopo la verifica dei due commit e del remoto, l'utente conferma di avere scollegato dal retro del NAS il cavo di alimentazione. Il NAS era già spento. Non dichiara altri spostamenti della memoria: secondo modulo ex B1 nell'ultimo A1 confermato, primo modulo fuori; i due test individuali restano falliti.

**Prossimo gesto.** Con il cavo ancora staccato, tenere premuto per cinque secondi il pulsante di accensione sul davanti del case. Pressione non ancora confermata; nessuno spostamento dei moduli richiesto in questo giro. La preparazione non qualifica la memoria e TrueNAS resta sospeso.

## 20/10/2026: pressione del pulsante confermata, preparazione del confronto su A2

**Fatto.** L'utente conferma la pressione del pulsante di accensione per cinque secondi con il cavo di alimentazione ancora staccato. Sono confermati anche il precedente spegnimento e lo scollegamento. Il secondo modulo, ex B1, rimane nell'ultimo A1 dichiarato e il primo resta fuori; nessuna nuova estrazione o prova confermata.

**Riferimento.** Riletta visivamente la figura delle configurazioni raccomandate a pagina 1-7, pagina PDF 17, del [manuale ASUS H170-PRO](https://dlcdnets.asus.com/pub/ASUS/mb/LGA1151/H170-PRO/E12046_H170-PRO_UM_V2_WEB.pdf), S130. Per un solo modulo ASUS raccomanda DIMM_A2; la disposizione dalla CPU è A1, A2, B1, B2. A2 è dunque il secondo alloggiamento dalla CPU. Il prossimo confronto mantiene lo stesso secondo modulo e le impostazioni già osservate, cambiando soltanto A1 con A2; non è ancora un risultato e non qualifica la RAM.

**Prossimo gesto.** A cavo staccato, estrarre il solo modulo attualmente in A1 vicino alla ventola Intel, aprendo il fermo mobile superiore; prenderlo dai bordi e tenerlo distinto dal primo modulo già fuori. Estrazione richiesta e non ancora confermata. Solo dopo seguirà l'inserimento dello stesso modulo in A2; nessuna riaccensione richiesta in questo giro e TrueNAS resta sospeso.

## 20/10/2026: chiarimento della posizione di A2

**Chiarimento.** A2 è lo slot immediatamente adiacente ad A1 allontanandosi dalla CPU, il secondo dei quattro contando dalla ventola Intel. Risulta a destra di A1 guardando con la ventola Intel alla sinistra degli slot; il riferimento stabile è la distanza dalla CPU, come nel manuale S130 a pagina 1-7. La domanda dell'utente non conferma alcuno spostamento: resta richiesta soltanto l'estrazione del modulo da A1 a cavo staccato, prima del successivo inserimento dello stesso in A2.

## 20/10/2026: stesso modulo in A2, nessun video; si sospende la sequenza NAS

**Fatto.** L'utente dichiara di avere spostato lo stesso modulo prima in A1 nel solo A2 e riferisce ancora nessun segnale video alla riaccensione. Il primo modulo resta fuori secondo l'ultimo stato noto. Non ci sono nuove immagini, accesso al firmware o avvio di Memtest documentati; il messaggio non prova da solo slot o modulo guasti. Spegnimento dopo questo tentativo non ancora confermato.

**Richiesta e percorso.** L'utente chiede di avanzare perché la sequenza di prove è diventata troppo lunga. Si sospendono ulteriori cicli ripetitivi sui due TEAMGROUP e si prepara il server Proxmox ASRock H270M Pro4 già previsto dalla roadmap, senza usare il NAS come storage. Prima si chiede soltanto di spegnere il NAS tenendo premuto il pulsante fino all'arresto; gesto ancora da confermare. Non si richiede di spostare altra RAM in questo giro.

**Perché non avviare il NAS con dati reali.** Gli errori individuali già osservati non identificano il componente responsabile ma lasciano la configurazione non affidabile. La [guida hardware ufficiale TrueNAS](https://www.truenas.com/docs/scale/gettingstarted/tnhardwareguide/), S102 riletta il 20/10 nelle sezioni Memory Sizing ed Error Correcting Code Memory, descrive blocchi e corruzione o perdita di dati fra gli effetti possibili degli errori in memoria. Il rischio concreto è scrivere dati alterati, anche senza un sintomo immediato; non è una prova che siano già stati corrotti dati su questi SSD. Il minimo di 8 GB non sostituisce la stabilità.

**Diagnosi rinviata.** Proposta una futura prova con due Crucial DDR4 da 4 GB già censiti nel server e destinati alla scorta; non sono memoria nota sana, non risultano prelevati e la configurazione da 8 GB non è accettata come sostituzione definitiva dei 16 GB. Il confronto cambierebbe la coppia, per verificare l'insieme con altri moduli, senza poter attribuire da solo la causa al singolo componente. Nessun'altra lunga prova sui TEAMGROUP richiesta ora. Alla ripresa va applicata anche ADR-016: la quarta condizione sull'alimentatore non è superata e prevede l'unità alternativa; non si dichiara risolta con il solo cambio RAM. Una prova alternativa senza avvio o con errori non conduce ad altri cicli automatici: la base resta da diagnosticare e il progetto continua sull'altra macchina.

## 20/10/2026: chiarimento dell'obiettivo NAS e conseguenze concrete degli errori

**Correzione del percorso.** L'utente chiarisce che vuole finire di assemblare il NAS, capire che cosa rischia concretamente e non prolungare i test per automatismo. Non chiedeva di passare al server: la deviazione proposta dall'agente nel giro precedente era un fraintendimento ed è superata. Nessun nuovo fatto fisico: ultimo stato dichiarato è il secondo modulo da solo in A2, primo modulo fuori e nessun video al tentativo di accensione; nuovo spegnimento non confermato.

**Durata effettivamente documentata.** Il singolo errore della coppia era visibile a Time 3:46:14, Pass 4, nel quinto passaggio; il 19/10 i contatori erano rimasti alla stessa lettura e l'utente riferiva nessuna risposta alla barra spaziatrice. Non sono documentate quarantotto ore di test attivo con un solo errore. Nei successivi test individuali nello stesso A1 si sono visti un errore a Time 2:51:08 e due errori a Time 3:03:15. Questi contatori non danno una probabilità per file, per copia o per giorno nell'uso normale e non identificano il componente responsabile.

**Conseguenze concrete.** La [documentazione hardware OpenZFS](https://openzfs.github.io/openzfs-docs/Performance%20and%20Tuning/Hardware.html), S177 letta il 20/10 nella sezione ECC Memory, distingue nessun effetto visibile, errore del programma o blocco del sistema, corruzione dei dati e corruzione dei metadati. Come esempi illustrativi, non danni osservati qui: una foto copiata può risultare alterata, un archivio ZIP non aprirsi oppure un backup non essere ripristinabile quando servirà. Se il dato si altera prima del calcolo del checksum, ZFS non sa che è sbagliato; può scriverlo uguale sui due membri dello specchio, quindi il mirror non risolve quel caso. Nel caso peggiore di metadati alterati il pool può non essere più importabile; OpenZFS descrive lo scenario estremo come straordinariamente raro in generale, senza una stima applicabile a questo hardware già instabile. Non si promette che avvenga né si dichiara già avvenuto.

**Completamento pratico.** È tecnicamente possibile finire l'assemblaggio e installare TrueNAS per prove senza chiudere prima tutta la diagnosi. I tre SSD sono già montati; il problema immediato da risolvere è l'assenza di video, che impedisce di seguire il firmware e l'installatore. Percorso proposto: continuare sul NAS con dati di prova o copie delle quali restano originali indipendenti, senza affidargli l'unica copia o l'unico backup. La domanda dell'utente non è ancora accettazione dei rischi o autorizzazione a cancellare dischi; il SanDisk va verificato prima di operazioni distruttive. Diagnosi, stato del collaudo e quarta condizione di ADR-016 restano aperti, ma non si impone un'altra notte di Memtest in questo giro. Il prossimo gesto resta spegnere il NAS prima di qualsiasi intervento sul mancato video; spegnimento ancora da confermare. Nessun modulo o alimentatore da spostare adesso.

## 20/10/2026: NAS spento dopo il tentativo senza video in A2

**Fatto.** L'utente conferma il NAS spento. Il secondo modulo resta nell'ultimo A2 dichiarato e il primo fuori; nessun nuovo spostamento o riscontro video. Questa conferma segue il tentativo senza segnale e non conferma lo scollegamento della corrente.

**Prossimo gesto.** Scollegare il cavo di alimentazione dal retro del NAS e attendere conferma, lasciando il modulo in A2. Si prepara il controllo dell'inserimento per recuperare il video e proseguire sul NAS; nessun altro lungo test della memoria richiesto ora. Scollegamento e controllo ancora da eseguire.

## 20/10/2026: alimentazione scollegata dopo il mancato video in A2

**Fatto.** L'utente conferma il cavo di alimentazione scollegato dal retro del NAS, già spento dopo il tentativo senza video. Il secondo modulo resta nell'ultimo A2 dichiarato e il primo fuori; nessun ulteriore movimento della memoria confermato.

**Prossimo gesto.** Con il cavo ancora staccato, tenere premuto per cinque secondi il pulsante di accensione sul davanti del case. Questa pressione non è ancora confermata per la nuova preparazione; seguirà il controllo dell'inserimento del modulo in A2 per recuperare il video e completare il NAS. Nessun nuovo test o scambio richiesto in questo giro.

## 20/10/2026: pulsante premuto a cavo staccato, reinserimento in A2 richiesto

**Fatto.** L'utente conferma la pressione del pulsante per cinque secondi con il cavo di alimentazione scollegato. Sono già confermati spegnimento e scollegamento dopo il tentativo senza video. Il secondo modulo resta nell'ultimo A2 dichiarato, primo modulo fuori; nessun nuovo movimento confermato.

**Prossimo gesto.** A cavo staccato, reinserire lo stesso modulo nello stesso A2: aprire il solo fermo mobile superiore, sollevare il modulo dai bordi, riallineare la tacca e premere uniformemente sulle due estremità finché il fermo si chiude. Il lato inferiore è fisso secondo S130, pagina 1-9 riletta visivamente. Reinserimento richiesto, non ancora confermato; nessuna accensione richiesta in questo giro. Il controllo serve a verificare il completo inserimento dopo lo spostamento, senza attribuire già a esso la causa del mancato video. Dopo seguirà la verifica dell'avvio, non un altro lungo Memtest automatico.

## 20/10/2026: ripartenza riferita dopo il reinserimento in A2

**Fatto.** Dopo il reinserimento dello stesso modulo nello stesso A2 richiesto a corrente tolta, l'utente riferisce che il NAS è partito e chiede come proseguire. Il primo modulo resta fuori secondo l'ultimo stato noto. Non ci sono nuove immagini o letture del firmware: la ripartenza è dichiarata e la causa del precedente mancato video non è isolata con certezza.

**Prossimo riscontro.** Richiesta una foto della schermata completa attualmente visualizzata sul NAS, per sapere dove si trova l'avvio e guidare verso il firmware e l'installazione TrueNAS. Foto ancora attesa; non si presume che siano aperti BIOS, Ventoy, Memtest o un sistema operativo. Nessun nuovo lungo test richiesto. L'avvio non qualifica la RAM, non annulla gli errori precedenti e non autorizza cancellazioni dei dischi.

## 20/10/2026: percorso dei test chiarito, un modulo temporaneo e coppia finale

**Correzione.** L'utente ricorda che si stavano facendo i test, osserva di avere una sola RAM e chiede istruzioni precise. L'agente aveva anticipato impropriamente l'installazione dopo la ripartenza: fase corrente di nuovo esplicita, confronto della memoria. Nessuna nuova azione o schermata confermata dalla domanda.

**Configurazione.** Ora: secondo modulo da 8 GB, ex B1 e poi A1, da solo in A2; primo modulo da 8 GB fuori. È una configurazione temporanea per il confronto. Obiettivo finale: due moduli da 8 GB, totale 16 GB, in A2+B2 secondo le configurazioni raccomandate del manuale S130. La mancanza dell'altro modulo in questa fase è intenzionale; aggiungerlo adesso impedirebbe il confronto sul singolo.

**Piano operativo.** Prima provare con Memtest86+ 8.10 lo stesso modulo da solo in A2, senza cambiare impostazioni. Criterio operativo dichiarato: quattro passaggi completi senza errori; fermare al primo errore o blocco documentato. È un limite del confronto, non una garanzia assoluta di affidabilità o una prescrizione del produttore. Il passo discriminante è il diverso slot con lo stesso DIMM rispetto agli errori già osservati in A1; un esito diverso non dimostra da solo A1 guasto. Se il singolo supera il confronto, montare l'altro modulo in B2 a corrente tolta e provare la coppia finale da 16 GB con lo stesso criterio prima di TrueNAS. Se una prova fallisce, registrare l'esito e fermare quel percorso senza altra ripetizione identica automatica; diagnosi e quarta condizione di ADR-016 restano aperte.

**Prossimo gesto.** Foto completa della schermata attualmente visualizzata sul NAS con nome del file, per guidare l'avvio della prova A2 da dove si trova realmente l'utente. Foto ancora attesa, nessun test già partito o completato dedotto. La richiesta ora serve alla prova di memoria, non all'installazione.

## 20/10/2026: Memtest avviato su RAM-02 in A2, nomi fissi dei moduli

**Fatto.** L'utente conferma Memtest partito in A2 con lo stesso modulo precedentemente provato in A1. Chiede di dare nomi ai moduli per non confonderli in caso di altri confronti. L'avvio è riferito: nessuna nuova foto o valore Time, Pass, Errors comunicato, quindi non si deduce un esito pulito.

**Identità dei pezzi.** I nomi seguono il modulo fisico e non cambiano quando cambia alloggiamento. Sono assegnati per continuità delle operazioni dichiarate, senza una nuova verifica dei seriali. Le posizioni originarie sono quelle della coppia prima dell'isolamento.

| Nome fisso | Taglia nominale | Posizione originaria | Traccia individuale già osservata | Posizione attuale dichiarata |
|---|---|---|---|---|
| RAM-01 | 8 GB DDR4 | A1 | A1: un errore a Time 2:51:08, Pass 3 | fuori dal NAS |
| RAM-02 | 8 GB DDR4 | B1 | A1: due errori a Time 3:03:15, Pass 3 | A2, Memtest in corso su conferma dell'utente |

**Stato delle prove individuali.** Una collocazione precedente non è un test individuale: l'errore della coppia originale A1+B1 resta un risultato della coppia, non un esito attribuito a RAM-01 o RAM-02 da soli.

| Modulo | A1 | A2 | B1 | B2 |
|---|---|---|---|---|
| RAM-01 | fallito, un errore | non provato | non provato | non provato |
| RAM-02 | fallito, due errori | in corso, contatori non comunicati | non provato singolarmente | non provato |

**Prossimo riscontro.** RAM-02 resta da sola in A2 durante Memtest. Per distinguere fisicamente il pezzo fuori, appoggiare un foglietto RAM-01 accanto; cartellino non ancora confermato e nessun intervento sul modulo in funzione. Raccogliere una foto del risultato al raggiungimento di quattro passaggi completi senza errori oppure al primo errore o blocco documentato, prima di fermare la prova. Se supera, il passo già previsto è la coppia finale RAM-02 in A2 e RAM-01 in B2, 16 GB, dopo montaggio a corrente tolta. Non si avvia automaticamente una serie di prove per ogni slot; altri confronti dipendono dal risultato. Nessuna nuova qualifica RAM o chiusura della quarta condizione ADR-016.

## 20/10/2026: RAM-02 fallisce anche in A2, etichette applicate

**Fatto.** L'utente conferma di avere etichettato entrambe le RAM. Restano nomi fissi indipendenti dagli slot: RAM-01 fuori, RAM-02 da sola in A2 secondo la configurazione dichiarata. Due nuove immagini mostrano Memtest86+ 8.10 build 8.10.49468.x64 con un errore: la prova A2 è fallita, non occorre attendere quattro passaggi.

| Voce letta | Prima immagine | Seconda immagine |
|---|---|---|
| memoria utilizzabile | 7,85 GB | 7,85 GB |
| tempo | 0:23:17 | 0:23:21 |
| passaggi, errori, stato | Pass 1, Errors 1, Failed | Pass 1, Errors 1, Failed |
| avanzamento | secondo passaggio 4%, test 4 al 70% | secondo passaggio 4%, test 4 al 71% |
| test corrente | Moving inversions, 8 bit pattern | Moving inversions, 8 bit pattern |
| controller e parallelismo | DDR4-2138, CAS 15-15-15-35, 8T PAR | DDR4-2138, CAS 15-15-15-35, 8T PAR |
| temperatura | 46/51 °C | 44/51 °C |
| banner | FAIL sovrapposto alla riga | banner rimosso, riga leggibile |

**Riga di errore.** pCPU 0, Pass 0, Test 9, indirizzo 0x0000b479e178 (2,81 GB); atteso 0x8360c27ed1a79f37, letto 0x8360c67ed1a79f37. XOR calcolato 0x0000040000000000, bit 42 da 0 a 1. L'errore appartiene quindi al primo passaggio, già completato alla lettura delle immagini; il test 4 mostrato in alto è quello in corso, non quello della riga di errore. Il tempo di 23 minuti è il tempo della schermata, non l'istante esatto del primo errore. Le due immagini attestano avanzamento di quattro secondi; non si dichiara un blocco.

**Confronto e limite.** Indirizzo e bit sono identici al primo errore della precedente prova RAM-02/A1, verificati contro il manifesto conservato. L'errore si ripresenta con lo stesso modulo anche in A2: è un indizio che rafforza il sospetto su RAM-02, non una prova definitiva del componente guasto. A1 e A2 sono nello stesso canale A; restano possibili cause comuni di canale, scheda, controller o alimentazione. Riletta S126 sulla necessità di distinguere il modulo dagli altri componenti. Nessuna qualifica del singolo o del NAS.

| Modulo | A1 | A2 | B1 | B2 | Stato fisico dichiarato |
|---|---|---|---|---|---|
| RAM-01 | fallito, un errore a 2:51:08 | non provato | non provato | non provato | etichettato, fuori |
| RAM-02 | fallito, due errori a 3:03:15 | fallito, un errore già a 0:23:17 | non provato singolarmente | non provato | etichettato, in A2 |

**Prossimo gesto.** Spegnere il NAS tenendo premuto il pulsante fino all'arresto; ancora da confermare. RAM-02 resta in A2 fino alla successiva preparazione a corrente tolta. Il prossimo confronto previsto sarà RAM-01 da sola nello stesso A2, con RAM-02 separata: si mantiene l'alloggiamento e si cambia solo il modulo. Nessuno scambio o nuovo test ancora eseguito; il ramo della coppia con RAM-02 non si attiva dopo questo fallimento. Non si richiede una serie automatica sugli altri due slot. TrueNAS resta non installato, quarta condizione ADR-016 aperta.

**Evidenze.** Entrambe le immagini archiviate nella parte privata e confrontate con SHA-256, identiche agli originali conservati. Manifesto e indice privato aggiornati; applicazione delle etichette riferita dall'utente, non dedotta da immagini dei moduli.

## 20/10/2026: RAM-01 da sola in A2, avvio osservato e riferimento all'immagine corretto

**Fatto.** L'utente comunica di avere già montato RAM-01 da sola nello stesso A2 e avviato Memtest, poi conferma di avere controllato visivamente sul banco la combinazione. RAM-02 risulta quindi rimossa e separata. I singoli gesti preparatori non sono stati confermati uno alla volta; si registra lo stato corrente dichiarato senza ricostruire come eseguita ogni operazione intermedia.

**Verifica dell'evidenza.** Il primo riferimento rimandava esattamente all'immagine già archiviata della precedente RAM-02/A2, confronto SHA-256 identico: il suo errore non è stato attribuito a RAM-01. L'utente corregge il riferimento e la nuova immagine è stata letta e archiviata separatamente, con SHA-256 identico all'originale conservato. Il programma mostra una sola SPD da 8 GB; la riga Slot 1 non sostituisce l'identificazione fisica A2 verificata dall'utente.

| Voce letta nella nuova prova RAM-01/A2 | Valore |
|---|---|
| programma | Memtest86+ 8.10, build 8.10.49468.x64 |
| memoria utilizzabile | 7,85 GB |
| tempo, passaggi, errori, stato | Time 0:00:02, Pass 0, Errors 0, Testing |
| avanzamento | primo passaggio 0%, test 3 Moving inversions 1s & 0s al 21% |
| intervallo e pattern | 4 MB-1 GB, 1020 MB su 7,85 GB; 0x0000000000000000 |
| controller e parallelismo | DDR4-2138, CAS 15-15-15-35, 8T PAR |
| temperatura | 50/50 °C |
| SPD | un modulo Team Group da 8 GB DDR4-2400, TEAMGROUP-UD4-2400 |
| scheda | ASUS H170-PRO |

**Limite e prossimo riscontro.** Due secondi senza errori attestano l'avvio, non qualificano RAM-01 né l'alloggiamento. Lasciare RAM-01 da sola in A2 e raccogliere una foto quando raggiunge quattro passaggi completi senza errori oppure al primo errore/blocco documentato, prima dell'arresto. Nessun ulteriore spostamento richiesto. RAM-02 resta fuori con i propri fallimenti; configurazione finale da 16 GB, diagnosi e quarta condizione ADR-016 restano aperte. TrueNAS non installato.

| Modulo | A1 | A2 | B1 | B2 | Stato corrente |
|---|---|---|---|---|---|
| RAM-01 | fallito, un errore a 2:51:08 | in corso, zero errori a 0:00:02 | non provato | non provato | sola in A2, verificata dall'utente sul banco |
| RAM-02 | fallito, due errori a 3:03:15 | fallito, un errore già a 0:23:17 | non provato singolarmente | non provato | fuori dal NAS |

## 20/10/2026: un passaggio RAM-01/A2 pulito alla sera, prova lasciata durante la notte

**Fatto.** L'utente comunica che lascia Memtest durante la notte e che il controllo riprenderà al mattino del 21/10. Due immagini della prova RAM-01 da sola in A2 mostrano Memtest86+ 8.10, 7,85 GB utilizzabili, Time 0:25:57 e 0:26:01, Pass 1, Errors 0, Status Pass. Il secondo passaggio avanza dall'8% al 10%, test 5 Moving inversions random pattern dal 48% al 68%, 46/51 °C. La prima immagine ha il banner PASS, la seconda no; i contatori avanzano di quattro secondi.

**Limite.** È osservato un solo passaggio completo senza errori, non quattro e non una qualifica finale. L'intenzione di lasciare il test durante la notte non prova da sola che l'esecuzione resti attiva per tutta la notte. Il riscontro successivo è registrato nella voce del 21/10.

## 21/10/2026: RAM-01 fallisce anche in A2 al riscontro del mattino

**Fatto.** La nuova immagine mostra RAM-01/A2, configurazione verificata al banco dall'utente prima dell'avvio, con Time 0:55:10, Pass 1, Errors 1, Failed. Secondo passaggio al 58%, test 8 Random number sequence all'87%, intervallo 7-8 GB. Memtest86+ 8.10 build 8.10.49468.x64, 7,85 GB, DDR4-2138 CAS 15-15-15-35, 8T PAR, 48/52 °C. Il banner PASS della sera non è quindi l'esito finale della prova.

| Riga di errore | Valore |
|---|---|
| pCPU, passaggio, test | 5, Pass 1, Test 8 |
| indirizzo | 0x0001efab15d8, indicato come 7,74 GB |
| atteso | 0xd28c1de88fe3f684 |
| letto | 0xd2ac1de88fe3f684 |
| differenza calcolata | XOR 0x0020000000000000, bit 53 da 0 a 1 |

**Confronto.** Indirizzo e bit coincidono con il precedente errore RAM-01/A1, verificati sui valori conservati nella voce del 19/10: allora il bit 53 era cambiato da 1 a 0; ora da 0 a 1. Anche pCPU e test sono gli stessi, con diverso numero di passaggio. RAM-02 aveva già ripetuto una propria combinazione indirizzo/bit fra A1 e A2. Queste ricorrenze rafforzano il sospetto sui moduli e giustificano un confronto con memoria diversa, ma non escludono canale A, controller, scheda o alimentazione. Nessuno dei due moduli è qualificato per il NAS.

**Durata osservata.** Le immagini serali hanno zero errori a 0:25:57 e 0:26:01; al mattino il contatore è 0:55:10 e non documenta quindici ore di test attivo. L'errore è presente entro il tempo dell'ultima schermata, senza sapere l'istante esatto del primo errore. Una sola foto del mattino non permette di attribuire il mancato avanzamento a blocco, pausa, riavvio o altra causa; non si ripete l'errore di conteggiare il tempo trascorso fuori dal test come prova superata.

| Modulo | A1 | A2 | B1 | B2 | Ultima posizione confermata |
|---|---|---|---|---|---|
| RAM-01 | fallito, un errore a 2:51:08 | fallito, un errore a 0:55:10 | non provato | non provato | in A2 |
| RAM-02 | fallito, due errori a 3:03:15 | fallito, un errore già a 0:23:17 | non provato singolarmente | non provato | fuori dal NAS |

**Prossimo gesto.** Spegnere il NAS tenendo premuto il pulsante fino all'arresto; ancora da confermare. RAM-01 resta in A2 fino alla preparazione a corrente tolta. Si propone poi un confronto con i due Crucial DDR4 da 4 GB previsti come scorta, ancora nell'ultimo server censito prima dello scambio: non risultano estratti e non sono memoria nota sana. È una prova alternativa da 8 GB, non una decisione di ridurre definitivamente il NAS da 16 GB. La sostituzione esplora il comportamento con memoria diversa, senza identificare da sola il componente guasto. Nessuna ulteriore serie automatica su tutti gli slot con i due TEAMGROUP. Se anche il controllo alternativo fallisce, riprendere le cause comuni e la previsione dell'alimentatore alternativo di ADR-016, invece di altre rotazioni identiche. Configurazione finale e quarta condizione ADR-016 ancora aperte, TrueNAS non installato.

**Evidenze.** Tre immagini archiviate privatamente, ciascuna confrontata SHA-256 con l'originale conservato; manifesto e indice aggiornati. Confronto di indirizzo e bit calcolato sui valori trascritti, fonte S126 riletta il 21/10 per il controllo mediante sostituzione e S102 per il minimo base di 8 GB, non per dichiarare questa configurazione qualificata.

## 21/10/2026: origine dei Crucial chiarita e coppia alternativa da 16 GB già sul banco

**Chiarimento.** L'utente chiede quali Crucial fossero stati indicati e a quale smontaggio appartenessero. Sono i quattro DDR4 da 4 GB censiti nel futuro server Proxmox linux-desktop-A, ASRock H270M Pro4/i7-7700. Secondo ADR-032, due diventerebbero scorta dopo il futuro scambio con due moduli da 8 GB prelevati da PC-DESKTOP-B; questo prelievo dei Crucial non è confermato. Non sono pezzi da supporre già fra gli smontaggi eseguiti.

**Nuova evidenza.** La foto indicata dall'utente mostra invece due moduli sciolti sul banco, entrambi Team Group TED48G2400C16BK da 8 GB DDR4-2400, CL16-16-16-39, 1,2 V, totale 16 GB. Il cartellino li associa alla scorta PC-DESKTOP-B, coerentemente con i prelievi già registrati e ADR-032. Origine riscontrata dal cartellino e dal contesto, senza un nuovo controllo dei seriali; la foto non attesta un collaudo elettrico.

| Nome proposto | Pezzo nella nuova foto | Taglia | Stato |
|---|---|---|---|
| RAM-03 | modulo superiore | 8 GB DDR4 | già fuori; etichetta richiesta, non confermata; non collaudato |
| RAM-04 | modulo inferiore | 8 GB DDR4 | già fuori; etichetta richiesta, non confermata; non collaudato |

**Percorso aggiornato.** Per il prossimo controllo si propone questa coppia già disponibile da 16 GB, prima di richiedere lo smontaggio del server per i Crucial. Il primo gesto è applicare i nomi RAM-03 e RAM-04 ai due pezzi fuori; nessuna etichetta già confermata. Dopo NAS spento e preparazione a corrente tolta, proposta rimozione di RAM-01 e montaggio RAM-03 in A2 e RAM-04 in B2, configurazione a due moduli raccomandata da S130. Spegnimento e nuovo montaggio non confermati: RAM-01 resta nell'ultimo A2 noto e RAM-02 fuori.

**Criterio della nuova coppia.** Per il confronto da 16 GB si propone almeno il completamento di cinque passaggi senza errori, fermando al primo errore o blocco documentato: il vecchio insieme aveva superato quattro passaggi e fallito durante il quinto. Fermarsi a quattro non coprirebbe quel punto già osservato. È un limite operativo della nuova prova, non una garanzia assoluta e non una chiusura automatica della condizione notturna di ADR-016. Nessuna nuova rotazione automatica sugli slot con RAM-01/RAM-02.

**Allocazione aperta.** Il prestito per il collaudo non cambia da solo ADR-032, che destinava la coppia al server. Se resta nel NAS va rivisto il conto dei 24 GB server, senza contare gli stessi moduli due volte. Nessuna qualifica, acquisto, cancellazione o installazione effettuata. Foto archiviata privatamente e verificata SHA-256 identica all'originale conservato, manifesto e indice aggiornati.

## 21/10/2026: ruolo della scorta chiarito, corrente NAS tolta e prova della coppia spiegata

**Scorta.** L'utente chiede che cosa fare della macchina PC-DESKTOP-B nello stato residuo. Si conferma il ruolo già previsto dall'inventario: conservarla assemblata e spenta come base sostitutiva del NAS, con ASUS B150-PRO, i7-6700, dissipatore, alimentatore, case/ventole e unità ottica. RAM e SSD sono già prelevati, non ci sono altri smontaggi da fare ora. La base può ricevere memoria e dischi del NAS se servirà sostituire la macchina; non è destinata alla dismissione come PC-02.

**Fatto al banco.** L'utente comunica di avere tolto corrente al NAS. Si registra alimentazione rimossa su dichiarazione, senza ricostruire separatamente modalità e gesti intermedi. RAM-01 resta nell'ultimo A2 confermato e RAM-02 fuori; RAM-03 e RAM-04 restano i nomi proposti per i due moduli sciolti della scorta, etichette e montaggio non ancora confermati.

**Prova spiegata.** Dopo la preparazione a corrente tolta, togliere RAM-01 e usare soltanto la coppia alternativa da 16 GB secondo questa proposta, senza cambiare altre impostazioni:

| Alloggiamento NAS | Modulo della scorta | Posizione contando dalla CPU |
|---|---|---|
| A2 | RAM-03, superiore della foto dei moduli sciolti | secondo |
| B2 | RAM-04, inferiore della stessa foto | quarto, il più lontano |

**Scopo ed esito.** Avviare Memtest86+ 8.10 per vedere se la macchina ripete gli errori con una coppia diversa. Attendere almeno cinque passaggi completi senza errori e raccogliere la foto; al primo errore o blocco documentato raccogliere la foto e fermare, senza prolungare una prova già fallita. Cinque passaggi perché la vecchia coppia aveva quattro passaggi puliti e falliva durante il quinto. La sostituzione non identifica da sola il singolo componente responsabile e un esito pulito non chiude automaticamente la condizione notturna di ADR-016. Un altro fallimento porta alle cause comuni e alla previsione dell'alimentatore alternativo, non a una serie automatica di prove in tutti gli slot. Il prestito della coppia non decide ancora l'allocazione definitiva NAS/server.

**Prossimo gesto.** Con il cavo di alimentazione scollegato, tenere premuto il pulsante frontale del NAS per cinque secondi. Pressione ancora da confermare per questa preparazione, nessuna RAM da muovere in questo giro. Poi si guiderà il montaggio della coppia spiegata sopra. TrueNAS resta non installato.

## 21/10/2026: coppia alternativa montata, Memtest avviato e obiettivo della prova chiarito

**Osservazione.** Cinque nuove immagini mostrano le etichette RAM-03 e RAM-04, la coppia montata e Memtest avviato, come riferisce l'utente. Posizioni riscontrate con il manuale ASUS S130, pagina 1-7:

| Slot dalla CPU | Modulo osservato |
|---|---|
| A1, primo | vuoto |
| A2, secondo | RAM-03, 8 GB |
| B1, terzo | vuoto |
| B2, quarto | RAM-04, 8 GB |

**Avvio osservato.** Memtest86+ 8.10, build 8.10.49468.x64: 15,8 GB utilizzabili, Time 0:00:04, Pass 0, Errors 0, Status Testing; primo passaggio allo 0%, test 3 Moving inversions, 1s & 0s al 21%. DDR4-2138, CAS 15-15-15-35, 8T PAR; CPU 3408 MHz, temperatura 37/43 °C. SPD due TEAMGROUP da 8 GB DDR4-2400, TEAMGROUP-UD4-2400, 2016-W48. Le diciture software Slot 1 e Slot 3 non sono i nomi ASUS A1 e B1. Quattro secondi senza errori non sono una qualifica. RAM-01/RAM-02 rimosse; la foto dei due moduli fuori documenta le etichette, ma l'ordine delle catture non dimostra uno smontaggio successivo all'avvio dichiarato.

**Obiezione e correzione del metodo.** L'utente chiede perché introdurre B2 e cambiare più variabili. L'obiezione è fondata per una diagnosi causale: rispetto al singolo modulo in A2 cambiano identità e numero dei moduli, capacità e uso del canale B. Il passaggio è una prova della configurazione candidata da 16 GB con una coppia alternativa già disponibile, con un obiettivo diverso dall'isolamento del guasto; il cambio di obiettivo doveva essere esplicitato prima. A2+B2 è la coppia raccomandata dal costruttore per due moduli, non un'affermazione che B2 sia già sano. Per isolare prima il cambio di modulo si sarebbe usata RAM-03 da sola nello stesso A2.

| Fase | Domanda a cui risponde | Limite |
|---|---|---|
| RAM-01 e RAM-02, una per volta in A1 | Il difetto si presenta con un solo modulo? | entrambe fallite; possibile causa comune |
| Ciascuno degli stessi moduli da solo in A2 | Il difetto resta limitato ad A1? | entrambe fallite anche in A2; A1 e A2 sono sullo stesso canale A |
| RAM-03/A2 più RAM-04/B2 | La coppia alternativa nella disposizione prevista per 16 GB supera la prova? | più variabili cambiate; non identifica il singolo responsabile |

**Prosecuzione.** La coppia è già avviata: lasciare proseguire fino ad almeno cinque passaggi completi senza errori oppure foto e arresto al primo errore/blocco documentato. Cinque perché la prima coppia fallì durante il quinto dopo quattro puliti. Un esito pulito riguarda questa configurazione e durata e non dimostra che RAM-01/RAM-02 siano entrambe guaste. Un fallimento lascia aperti i moduli nuovi, B2/canale B e le altre cause comuni; il prossimo confronto controllato proposto sarà RAM-03 da sola in A2, senza una matrice automatica di tutti gli slot. Nessuna qualifica individuale di RAM-03/RAM-04, nessuna chiusura automatica della condizione notturna ADR-016 o dell'allocazione NAS/server ADR-032. TrueNAS non installato.

**Traccia.** Cinque immagini copiate nell'archivio privato, SHA-256 confrontati e identici agli originali conservati; manifesto e indice privati aggiornati. Nessuna ulteriore manipolazione fisica da richiedere mentre il test è in esecuzione.

## 21/10/2026: confermata prosecuzione della coppia, esito in attesa

L'utente conferma di lasciare proseguire la prova RAM-03/A2 + RAM-04/B2 e chiede che sia registrato tutto. Nessun nuovo contatore o esito comunicato: resta valido soltanto l'avvio documentato. Nessuna modifica alla configurazione richiesta; attesa di almeno cinque passaggi completi con Errors 0, oppure foto e arresto al primo errore o blocco documentato. Restano registrati anche lo scopo della prova della coppia da 16 GB e i suoi limiti per isolare il guasto.

## 21/10/2026: banner PASS riferito, barra spaziatrice premuta e contatori da acquisire

Ultima segnalazione: l'utente riferisce il banner PASS per la coppia RAM-03/A2 + RAM-04/B2 e dice di avere premuto la barra spaziatrice per proseguire. Si registra la dichiarazione senza attribuire un numero di passaggi completati, una durata o un totale di errori non ancora letti. Il banner da solo non verifica il criterio concordato di almeno cinque passaggi completi con Errors 0. Richiesta identificazione della schermata disponibile per acquisire Time, Pass, Errors e stato attuale; nessuna nuova manipolazione o riavvio richiesto. Prova e accettazione finale restano aperte.

## 21/10/2026: PASS senza schermata, prova lasciata proseguire

L'utente precisa che non c'è una schermata da acquisire: riferisce soltanto PASS, lascia proseguire la prova RAM-03/A2 + RAM-04/B2 e aggiornerà lui. Richiesta di identificare una schermata superata; nessun altro screenshot o contatore da sollecitare ora. PASS registrato come dichiarazione, senza inventare durata, numero di passaggi o totale degli errori. Nessun cambio alla configurazione o riavvio richiesto; si attende il prossimo aggiornamento dell'utente.

## 21/10/2026: fallita anche la coppia alternativa RAM-03/A2 e RAM-04/B2

**Esito osservato.** Nuova foto riferita dall'utente, letta direttamente: Memtest86+ 8.10 build 8.10.49468.x64, i7-6700, 15,8 GB, Time 0:53:56, Pass 1, Errors 2, Status Failed. Secondo passaggio al 54%, test 8 Random number sequence al 33%; intervallo attuale 3 GB - 3,04 GB, 51 MB dei 15,8 GB. CPU 3408 MHz, temperatura 54/56 °C; IMC 1069 MHz, DDR4-2138 CAS 15-15-15-35, SMP 8T PAR. Una riga di errore visibile:

| pCPU | Pass | Test | Indirizzo | Atteso | Letto | XOR e bit |
|---|---|---|---|---|---|---|
| 2 | 1 | 8 | 0x00008fb766b8, 2,24 GB | 0xf56caad22e562f66 | 0xf56c2ad22e562f66 | 0x0000800000000000, bit 47 da 1 a 0 |

**Perimetro.** Il contatore mostra due errori ma la foto documenta una sola riga; non si ricostruisce la seconda. Il precedente PASS era stato registrato come dichiarazione senza contatori: il fallimento attuale esclude il superamento del criterio della coppia. Una singola immagine non dimostra un blocco del test; il piè di schermata mostra Space Scroll unlock e non viene usato per dedurre il tempo di attività. Il fallimento riguarda la configurazione RAM-03/A2 + RAM-04/B2, non qualifica individualmente i due moduli né dimostra che tutti e quattro i moduli siano guasti. Restano possibili moduli, interazione di coppia, B2/canale B e cause comuni della base.

**Prossimo gesto.** Richiesti spegnimento del NAS e distacco del cavo di alimentazione, ancora da confermare. RAM-03 resta nell'ultimo A2 confermato e RAM-04 in B2; nessuna rimozione già avvenuta. Dopo preparazione a corrente tolta il confronto già annunciato è togliere soltanto RAM-04 da B2 e provare RAM-03 da sola nello stesso A2, senza cambiare altre impostazioni. Nessuna matrice automatica degli slot; ADR-016 e cause comuni restano aperte, senza attribuire dai soli errori il guasto all'alimentatore. TrueNAS non installato e allocazione definitiva NAS/server ancora aperta.

**Traccia.** Foto copiata nell'archivio privato e riletta, SHA-256 identico all'originale conservato; manifesto e indice privati aggiornati.

## 21/10/2026: RAM-03 da sola nello stesso A2, nuovo Memtest avviato

Nuovo test del 21/10/2026: l'utente conferma di avere completato la preparazione e avviato Memtest con RAM-03 da sola nello stesso A2. RAM-04 rimossa da B2, A1/B1/B2 vuoti su configurazione dichiarata; RAM-01/RAM-02 restano fuori. La schermata conferma un solo modulo da 8 GB e 7,85 GB utilizzabili, non identifica da sola l'etichetta fisica o il nome ASUS dello slot. Memtest86+ 8.10 build 8.10.49468.x64, Time 0:00:04, Pass 0, Errors 0, Testing; primo passaggio allo 0%, test 3 Moving inversions, 1s & 0s al 28%. DDR4-2138, IMC 1069 MHz, CAS 15-15-15-35, SMP 8T PAR, CPU 3408 MHz, temperatura 39/45 °C. SPD software Slot 1: 8 GB DDR4-2400 Team Group TEAMGROUP-UD4-2400, 2016-W48; Slot 1 non è il nome ASUS A1. Nessuna qualifica dall'avvio. Criterio della prova individuale: quattro passaggi completi con Errors 0, come per i precedenti confronti individuali A2, oppure foto e arresto al primo errore/blocco documentato; i cinque passaggi restano il criterio della futura coppia finale, non una prova già superata. La coppia RAM-03/A2 + RAM-04/B2 resta fallita a 0:53:56, Pass 1, Errors 2; RAM-03 e RAM-04 non sono ancora qualificate individualmente. Togliere RAM-04 verifica il comportamento del modulo rimasto in A2, ma un eventuale esito pulito non distingue da solo modulo tolto, B2/canale B o interazione della coppia. Lasciare proseguire senza altre modifiche; nessun nuovo spegnimento o montaggio da richiedere. Cause comuni, ADR-016 e allocazione definitiva NAS/server ADR-032 restano aperte. TrueNAS non installato. Foto copiata e SHA-256 identico all'originale conservato.

## 21/10/2026: RAM-03/A2, PASS riferito senza schermata e prova in prosecuzione

L'utente riferisce PASS nella prova di RAM-03 da sola in A2, dice di avere premuto la barra spaziatrice e lascia proseguire il test, senza schermata. Segnalazione registrata senza attribuire contatori, durata o numero di passaggi non acquisiti; il criterio dei quattro passaggi completi con Errors 0 resta da verificare. Nessun cambio alla configurazione, nessuno screenshot da richiedere ora; attendere il prossimo aggiornamento dell'utente.

## 22/10/2026: RAM-03/A2 prosegue da circa 22 ore senza fail, confronto individuale sufficiente per avanzare

**Riscontro riferito.** L'utente comunica che sono passate circa 22 ore e il test continua senza fail, mantenendo RAM-03 da sola nello stesso A2. Si acquisisce la durata approssimativa e l'osservazione dell'utente; non sono stati acquisiti nuovi contatori Time, Pass o Errors. Il PASS riferito il giorno precedente non era stato usato per inventare un risultato finale. Nessuna nuova schermata richiesta.

**Valutazione operativa.** Il risultato prolungato positivo riferito ? sufficiente per avanzare dal confronto individuale senza prolungare ancora questa prova. Non si dichiara letto il criterio di quattro passaggi n? una garanzia assoluta, e non si chiude il collaudo della coppia finale da 16 GB. A parit? del singolo A2, RAM-01 e RAM-02 avevano fallito, mentre RAM-03 ha ora questo riscontro positivo: il confronto ? utile ma non esclude ogni causa comune o dipendente dal carico. La coppia RAM-03/A2 pi? RAM-04/B2 resta fallita in meno di un'ora.

| Configurazione | Stato al 22/10/2026 | Tipo di riscontro |
|---|---|---|
| RAM-01 da sola in A1 e A2 | fallita in entrambi | schermate archiviate |
| RAM-02 da sola in A1 e A2 | fallita in entrambi | schermate archiviate |
| RAM-03/A2 pi? RAM-04/B2 | fallita a 0:53:56, Pass 1, Errors 2 | schermata archiviata |
| RAM-03 da sola in A2 | circa 22 ore senza fail, test ancora in prosecuzione | dichiarazione dell'utente, avvio archiviato |
| RAM-04 da sola in A2 | da provare | nessun avvio confermato |

**Prossimo gesto.** Richiesti spegnimento del NAS e distacco dell'alimentazione, ancora da confermare; RAM-03 resta nell'ultimo A2 dichiarato, RAM-04 fuori. Dopo preparazione a corrente tolta si propone sostituire soltanto RAM-03 con RAM-04 nello stesso A2, mantenendo un solo modulo e le impostazioni invariate. Obiettivo: confrontare i due moduli individualmente nello stesso slot, prima di attribuire il fallimento della coppia a RAM-04, a B2/canale B o all'interazione dei moduli. Criterio di RAM-04: quattro passaggi completi senza errori oppure foto e arresto al primo errore/blocco, come gi? previsto per i confronti individuali; nessun'altra prova di 22 ore richiesta e nessuna matrice automatica degli slot. Esito finale NAS, quarta condizione ADR-016 e allocazione NAS/server ancora aperti. TrueNAS non installato.

## 22/10/2026: RAM-04 da sola nello stesso A2, Memtest avviato

Avviata la prova concordata di RAM-04 da sola nello stesso A2, RAM-03 rimossa. Schermata Memtest86+ 8.10 build 8.10.49468.x64: 7,85 GB, Time 0:00:35, Pass 0, Errors 0, Testing; primo passaggio al 3%, test 4 Moving inversions, 8 bit pattern al 47%, intervallo 2 GB - 3 GB, pattern 0xfdfdfdfdfdfdfdfd. CPU 3408 MHz, temperatura 46/50 °C, IMC 1069 MHz, DDR4-2138 CAS 15-15-15-35, SMP 8T PAR. SPD software Slot 1: 8 GB DDR4-2400 Team Group TEAMGROUP-UD4-2400, 2016-W48. Slot 1 non è il nome ASUS A1; identità RAM-04 e posizione A2 derivano dal passo concordato e dall'avvio riferito, non dalla sola schermata SPD. È soltanto l'avvio, nessuna qualifica di RAM-04. Lasciare proseguire per quattro passaggi completi con Errors 0 oppure foto e arresto al primo errore/blocco, senza altre modifiche. RAM-03/A2 conserva circa 22 ore senza fail su dichiarazione; coppia RAM-03/A2 + RAM-04/B2 fallita a 0:53:56 con due errori. Cause comuni, configurazione finale, ADR-016 e allocazione NAS/server aperte. TrueNAS non installato. Foto archiviata e SHA-256 identico all'originale conservato; nessun nuovo spegnimento o montaggio da richiedere.

## 22/10/2026: RAM-04 fallisce da sola in A2, prosecuzione con candidata RAM-03 da 8 GB

RAM-04 da sola in A2 ha mostrato un errore: Memtest86+ 8.10 build 8.10.49468.x64, Time 0:04:38, Pass 0, Errors 1, Status Testing; primo passaggio al 27%, test 6 Moving inversions, 64 bit pattern al 36%. Il test è fallito secondo il criterio di zero errori, anche se lo stato visualizzato non è ancora Failed. Una riga visibile: pCPU 1, Pass 0, Test 6, indirizzo 0x000047abb378 (1,12 GB), atteso 0x0000080000000000, letto 0x0000000000000000, XOR 0x0000080000000000, bit 43 da 1 a 0. RAM 7,85 GB utilizzabili, CPU 3408 MHz, temperatura 47/50 °C, DDR4-2138 CAS 15-15-15-35, 8T PAR. Non si deduce un blocco da una sola schermata. RAM-03 nello stesso A2 ha circa 22 ore senza fail su dichiarazione: il confronto rafforza nettamente il sospetto su RAM-04, da escludere operativamente dal NAS, senza certificare ogni causa comune o B2. RAM-01/RAM-02 restano sospette e fuori; non buttare i moduli. L'utente invita a procedere. Percorso attivo: spegnere e scollegare il NAS, a LED spenti sostituire RAM-04 con la sola RAM-03 nello stesso A2, poi riaccendere ed entrare nel BIOS con Canc per proseguire il montaggio e verificare firmware/dischi. Tutti questi nuovi gesti ancora da confermare; ultima configurazione RAM-04/A2 con errore. Nessun altro Memtest identico su RAM-03 né nuova matrice di slot richiesta. Configurazione candidata per avanzare da 8 GB, coerente con il minimo base di S102; obiettivo precedente 16 GB e conto server di ADR-032 da rivedere, non contare gli stessi moduli due volte. Accettazione finale e ADR-016 ancora aperte; nessuna installazione o cancellazione eseguita. TrueNAS non installato. Foto archiviata con SHA-256 identico, originale conservato.

| pCPU | Pass | Test | Indirizzo | Atteso | Letto | XOR e bit |
|---|---|---|---|---|---|---|
| 1 | 0 | 6 | 0x000047abb378, 1,12 GB | 0x0000080000000000 | 0x0000000000000000 | 0x0000080000000000, bit 43 da 1 a 0 |

Il requisito base di 8 GB di S102 è stato riletto online per il percorso candidato; l'URL corrente mostra documentazione di sviluppo TrueNAS 28 e questa lettura non seleziona una release da installare. Il passaggio da 16 GB previsti a un solo modulo positivo da 8 GB è il percorso di prosecuzione al banco, non una qualifica automatica del NAS o la disponibilità contemporanea della stessa RAM nel server. Prima del sistema restano firmware/AHCI, dischi e dati da conservare. Nessun nuovo ciclo identico di RAM-03 o rotazione automatica di slot richiesto.

## 23/10/2026: RAM-03 rimontata in A2, BIOS raggiunto

Aggiornamento del 23/10/2026: l'utente conferma RAM-03 rimontata nello stesso A2 e ingresso nel BIOS. Nuova configurazione corrente confermata su dichiarazione, non più preparazione pendente: NAS acceso nel firmware con la sola RAM-03, RAM-04 rimossa secondo il passo concordato; RAM-01/RAM-02 fuori. Nessuna nuova schermata BIOS ricevuta o letta: memoria effettivamente rilevata, presenza e porte dei tre SSD e modalità SATA/AHCI restano da verificare, non si presumono dai dati dei giorni precedenti. Prossimo riscontro richiesto una foto intera e leggibile della schermata BIOS attuale; nessuna modifica alle impostazioni richiesta prima della lettura. Nessun nuovo spegnimento, rimontaggio o Memtest identico da richiedere. Base del percorso candidato da 8 GB: RAM-03/A2 circa 22 ore senza fail riferite il 22/10; RAM-04/A2 fallita a 0:04:38, Errors 1, Status Testing, test 6 e bit 43. RAM-01/RAM-02 fallite individualmente A1/A2 e coppia RAM-03/A2 + RAM-04/B2 fallita. RAM sospette escluse dall'uso NAS e conservate etichettate. Accettazione ADR-016 e riallocazione NAS/server ADR-032 ancora da riconciliare; TrueNAS non installato, AHCI, SMART lungo e dati SanDisk da verificare.

## 23/10/2026: BIOS conferma 8 GB nel solo A2 e tre SSD, AHCI ancora da leggere

Aggiornamento del 23/10/2026: letta la schermata ASUS H170-PRO EZ Mode, BIOS 3805. RAM-03 nello stesso A2 su conferma precedente dell'utente; ora il BIOS osservato mostra 8192 MB DDR4 a 2133 MHz, solo DIMM_A2 Team Group 8192 MB 2400 MHz SPD, A1/B1/B2 N/A, XMP Disabled. Tre SSD rilevati sulle porte previste: SATA6G_1 SanDisk SDSSDA240G 240 GB; SATA6G_2 Kingston SV300S37A240G 240 GB; SATA6G_6 WDC WDS250G1B0A-00H9H0 250 GB. Porte 3/4/5 N/A. CPU 34 °C, scheda 27 °C, CPU Core Voltage 1,104 V; questo non è il +12 V dell'alimentatore. Intel Rapid Storage mostra Off evidenziato, ma SATA Mode Selection non è visibile: AHCI resta da verificare direttamente. Prossimo passo F7, Advanced, SATA Configuration, leggere SATA Mode Selection e acquisire schermata senza cambiare valori. Percorso riscontrato sul manuale S130 sezione 2.6.5, pagina 2-32, PDF 66. RAM-03/A2 circa22h senza fail su dichiarazione; RAM-01/RAM-02/RAM-04 fuori e sospette, nessun nuovo Memtest richiesto. TrueNAS non installato; SMART lungo, dati SanDisk, accettazione e riallocazione NAS/server restano aperti. Foto archiviata con SHA-256 identico, originale conservato.

| Voce BIOS osservata | Valore |
|---|---|
| Memoria totale | 8192 MB DDR4,2133MHz |
| DIMM_A2 | Team Group Inc.,8192MB,2400MHz SPD |
| DIMM_A1/B1/B2 | N/A |
| XMP | Disabled |
| SATA6G_1 | SanDisk SDSSDA240G,240GB |
| SATA6G_2 | Kingston SV300S37A240G,240GB |
| SATA6G_6 | WDC WDS250G1B0A-00H9H0,250GB |
| SATA6G_3/4/5 | N/A |

CPU34?C, scheda27?C, Vcore1,104V; ventole CPU1322RPM,CHA1 909RPM,CHA2 851RPM. Questi valori non sostituiscono la misura del +12V. Le voci di avvio WindowsBootManager su SanDisk eWD sono visibili ma non attestano contenuto o avviabilità attuale dei dischi. Memoria e rilevamento dischi ora verificati; prossimo riscontro SATA Mode Selection nel menu del manuale, senza modifiche o salvataggi impliciti.

## 23/10/2026: nome PCH Storage Configuration e tensioni del monitor hardware

Aggiornamento del 23/10/2026: le due foto corrette mostrano il menu Advanced del BIOS, non ancora il campo SATA Mode Selection. Nel BIOS corrente la voce si chiama PCH Storage Configuration: correggere il percorso precedente Advanced > SATA Configuration, che deriva dal manuale E12046 ma non dal nome effettivo della versione osservata. Prossimo riscontro: aprire Advanced > PCH Storage Configuration e fotografare SATA Mode Selection senza cambiare valori. AHCI resta da verificare. Monitor hardware osservato: memoria 8192 MB a2133MHz, tensione DRAM1,200V, CPU34°C e3400MHz, Vcore1,104V; +12V12,192V, +5V5,040V, +3,3V3,392V. Il +12V è ora letto direttamente nel BIOS, senza confonderlo con Vcore, e non certifica da solo l'alimentatore. Sola RAM-03/A2 e treSSD porte1/2/6 già osservati; RAM-03 circa22h senza fail su dichiarazione, RAM-01/RAM-02/RAM-04 fuori. Nessun nuovo Memtest. Foto copiate con SHA-256 identici e originali conservati; identificativo NIC non trascritto nel livello pubblico. TrueNAS non installato; SMARTlungo, datiSanDisk, accettazione e allocazione restano aperti.

Il percorso precedente è corretto sul nome effettivamente visibile, senza attribuire all'utente un errore di navigazione. I due riferimenti iniziali a immagini non NAS sono stati sostituiti dall'utente; quei contenuti non sono usati come evidenze o copiati nel materiale NAS. L'identificativo della scheda di rete visibile in una foto resta nel solo materiale privato e non viene trascritto qui.

## 23/10/2026: AHCI letto direttamente, prossimo controllo SMART

Aggiornamento del 23/10/2026: letta direttamente nel BIOS la modalità SATA Mode Selection AHCI, controller SATA Enabled, percorso Advanced > PCH Storage Configuration. Nessuna modifica di questi valori richiesta. Hyper Kit Mode Disabled, Aggressive LPM Support Disabled; SMART Self Test mostra On, che non documenta l'esito di un test lungo. Visibili SanDisk240 su SATA6G_1 e Kingston240 su SATA6G_2; WD250 su SATA6G_6 già osservato nella schermata EZ. Memoria8192MB a2133MHz, DRAM1,200V; CPU35°C3400MHz, Vcore1,104V; +12V12,192V,+5V5,040V,+3,3V3,408V. Sola RAM-03/A2, circa22h senza fail su dichiarazione; RAM-01/RAM-02/RAM-04 fuori. Prossimo riscontro Esc, Advanced, HDD/SSD SMART Information e foto leggibile; attributi e test lungo ancora non acquisiti, datiSanDisk da confermare, TrueNAS non installato. Foto copiata e SHA-256 identico all'originale conservato.

Il riferimento di configurazione SATA/AHCI è chiuso dalla lettura diretta. La voce SMART Self Test su On non chiude la verifica degli attributi o del test lungo; la pagina mostra solo i dischi delle prime porte e il rilevamento completo dei tre SSD resta quello della precedente EZ Mode. Nessuna impostazione è stata richiesta in modifica. L'approvazione delle raccomandazioni di rete e del metodo didattico è registrata in ADR-037/038 e non installa servizi durante il montaggio.

## 23/10/2026: prima lettura SMART BIOS del SanDisk dati

Aggiornamento del 23/10/2026: letta la prima pagina HDD/SSD SMART Information, dispositivo SanDisk SDSSDA240G 240 GB del pool dati previsto. BIOS mostra quattro attributi: Reallocated Sectors Count VAL100 WOR100 THR000 raw000000000000; Power-On Hours Count VAL000 WOR100 THR000 raw000000004AF0; Power Cycle Count VAL100 WOR100 THR000 raw000000000755; Temperature(C) VAL071 WOR041 THR000 raw003B0000001D. Conversioni aritmetiche dei contatori: 0x4AF0=19184, 0x0755=1877; nel formato termico standard la parte bassa0x1D=29, da confermare nella lettura completa. Il profilo smartmontools per SDSSDA240G chiama il primo contatore Retired_Block_Count: non estendere l'etichetta generica BIOS a una certificazione dei settori o del disco. VAL/WOR sono valori normalizzati, non ore o gradi: 071 non significa71°C. Questa schermata parziale non mostra usura completa, log errori o risultato del testlungo. AHCI,8GB/A2 e treSSD già verificati; TrueNAS non installato. Prossimo passo nel menuDevice selezionare KingstonV300 eWDBlue, una foto ciascuno, senza cambi. Testlungo/capacità SMARTcomplete e datiSanDisk ancora da verificare. Fonti smartctl/drivedb ufficiali registrate; nessuna nuova scheda didattica, applicazione della distinzione già documentata nella voce1. Foto copiata con SHA identico, originale conservato.

| Campo BIOS | VAL | WOR | THR | RAW esadecimale osservato | Lettura limitata |
|---|---|---|---|---|---|
| Reallocated Sectors Count | 100 | 100 | 000 | 000000000000 | zero nel contatore; profilo SSD smartmontools Retired_Block_Count |
| Power-On Hours Count | 000 | 100 | 000 | 000000004AF0 | conversione 19184 nel campo ore, da confermare nel resoconto completo |
| Power Cycle Count | 100 | 100 | 000 | 000000000755 | conversione 1877 accensioni |
| Temperature(C) | 071 | 041 | 000 | 003B0000001D | parte bassa 0x1D uguale29, compatibile con temperatura corrente; non71°C dal VAL |

Le fonti S186 e S187 spiegano la distinzione fra valore normalizzato e formato grezzo specifico del modello. Non sono ancora disponibili firmware, tabella completa, log errori, usura o risultato di un test lungo: il SanDisk non viene dichiarato qualificato. Nessun valore da modificare nel BIOS. Si passa alle pagine KingstonV300 e WDBlue prima di scegliere l'ambiente per i controlli completi.

## 23/10/2026: prima pagina SMART BIOS del Kingston V300 di avvio

Aggiornamento del 23/10/2026: letta la pagina SMART BIOS del Kingston SV300S37A240G 240 GB, disco di avvio previsto su SATA6G_2. Cinque attributi acquisiti: Read Error Rate RAW0 e Reallocated Sectors Count RAW0; Power-On Hours RAW234400007DE4, Power Cycle Count RAW000000000E02, temperatura RAW00110029001A. Il profilo specifico smartmontools usa msec24hour32: i32bitbassi7DE4 corrispondono al campoore32228, non si converte l'intero RAW in ore; decodifica completa e firmware da leggere. Cicli0xE02=3586, parte bassa temperatura0x1A=26 coerente conVAL026, senza generalizzare questo formato agli altriSSD. Nessuna percentuale di vita residua o testlungo superato dedotta. SanDisk già letto, WD Blue ancora da fotografare dalmenuDevice senza altre modifiche. RAM-03/A2,8GB,AHCI e treSSD già verificati; TrueNASnoninstallato, SMARTcompleto/testlungo e datiSanDisk ancora da verificare. Foto copiata e SHA identico, originale conservato.

| Campo BIOS | VAL | WOR | THR | RAW esadecimale osservato |
|---|---|---|---|---|
| Read Error Rate | 120 | 120 | 050 | 000000000000 |
| Reallocated Sectors Count | 100 | 100 | 003 | 000000000000 |
| Power-On Hours Count | 064 | 064 | 000 | 234400007DE4 |
| Power Cycle Count | 097 | 097 | 000 | 000000000E02 |
| Temperature(C) | 026 | 041 | 000 | 00110029001A |

La fonte S187 associa il modello Kingston V300 al formato msec24hour32 per l'attributo9. Si conservano il RAW completo e il campoore basso0x7DE4=32228; la parte alta visibile non viene sommata alle ore o interpretata per intero come durata. Il valore VAL064 delle ore non viene chiamato64ore o64percento di vita. I contatori a zero sono il riscontro limitato dei campi mostrati, non l'esito di un test lungo o una stima di usura. Fonte generale S186 e profilo specifico S187, riletto per questo modello. Nessuna impostazione cambiata; prossimo WD Blue nel medesimo menu Device.

## 23/10/2026: nuova immagine ancora Kingston, WD non acquisito

Ulteriore riscontro del 23/10/2026: la nuova immagine mostra ancora Device KINGSTON SV300S37A240G, non il WD Blue. I cinque campi SMART visibili coincidono con la precedente pagina Kingston; nessun nuovo dato WD acquisito. Prossimo passo selezionare nel menuDevice WDC WDS250G1B0A; se non compare, acquisire l'elenco Device aperto. Nessun'altra impostazione da modificare, nessun nuovo test o giudizio di salute dedotto.

## 23/10/2026: SMART BIOS del WD Blue e confronto preliminare completato

Aggiornamento del 23/10/2026: acquisita la pagina SMART del WD Blue WDS250G1B0A-00H9H0, dati su SATA6G_6. RAW riallocazioni 000000000000, ore 000000004889, cicli 000000000ADB, temperatura 00400011001B; VAL/WOR/THR rispettivamente100/100/000,100/100/000,100/100/000,073/064/000. Conversioni dei campi standard:18569 nel campoore,2779cicli e partebassa27 compatibiletemperatura; firmware e output completo ancora da leggere. Le prime pagine BIOS dei treSSD sono ora tutte acquisite, ciascuna con RAW0 nel contatore riallocazioni/ritiroblocchi; soloKingston mostraReadErrorRate,RAW0. Raccolta preliminare finita, non salute/usura o testlungo qualificati. AHCI,RAM-03/A2,8GB e porte1/2/6 gi?verificati. Prossimo avvio UEFI della chiavettaVentoy/Medicat gi? usata perMemtest e foto delmenuprincipale per scegliere diagnosticaSMART. Immagini diagnostiche disponibili non ancora confermate; nessun nuovoMemtest o installazione/formattazione. DatiSanDisk, SMARTcompleto/capacit? e testlungo pendenti. FotoWDarchiviata SHAidentico, originaleconservato.

| Campo BIOS | VAL | WOR | THR | RAW esadecimale osservato |
|---|---|---|---|---|
| Reallocated Sectors Count | 100 | 100 | 000 | 000000000000 |
| Power-On Hours Count | 100 | 100 | 000 | 000000004889 |
| Power Cycle Count | 100 | 100 | 000 | 000000000ADB |
| Temperature(C) | 073 | 064 | 000 | 00400011001B |

| SSD e ruolo previsto | Porta | Contatore riallocazioni/ritiroblocchi mostrato | RAW campo ore | Test lungo |
|---|---|---|---|---|
| SanDisk240, dati | SATA6G_1 | 0 | 000000004AF0 | non acquisito |
| KingstonV300240, avvio | SATA6G_2 | 0 | 234400007DE4, composto | non acquisito |
| WDBlue250, dati | SATA6G_6 | 0 | 000000004889 | non acquisito |

S187 comprende il modello WD e i formati di riferimento, non identifica il firmware reale. Le pagine BIOS non includono usura completa, log degli errori o risultato lungo. La guida privata prevede controlli da ambiente live; lo storico19/10 conferma chiavettaVentoy/Medicat21.12 e avvioUEFI Generic Partition2, ma nessuna specifica ISOdiagnostica ? ancora verificata nel menu attuale. Prima di nuove istruzioni o download si acquisisce quel menu. Nessun dato viene cancellato o sistema installato in questo passo.

## 23/10/2026: chiavetta Medicat avviata, scelta dell'ambiente diagnostico

Avviato correttamente il menu principale Medicat USB v21.12, con indicazione UEFI. Sono visibili Antivirus, Backup and Recovery, Boot Repair, Diagnostic Tools, Live Operating Systems, Partition Tools, Password Removal e Windows Recovery; è selezionato Antivirus. Per individuare un ambiente da cui leggere lo SMART completo, aprire Live Operating Systems, quinta voce: dalla selezione attuale quattro pressioni di freccia giù e Invio, poi acquisire il sottomenu. La presenza della categoria non conferma ancora quali sistemi o strumenti contenga. Nessun nuovo test o intervento sui dischi eseguito.

Restano aperti SMART completo, firmware e autotest supportati dei tre SSD, oltre alla destinazione dei dati SanDisk. RAM-03/A2, 8 GB e AHCI restano la configurazione osservata. Il riscontro conferma il menu di avvio, non l'esecuzione di una diagnostica. Nessuna modifica ai dischi; immagine conservata privatamente con verifica SHA-256 e originale mantenuto.

## 23/10/2026: ambienti live elencati, voce SystemRescue individuata

Nel sottomenu Live Operating Systems di Medicat USB v21.12 sono visibili Active@ Data Studio, Mini Windows 10 e SystemRescue, tutte con freccia verso un ulteriore livello. È selezionata la riga di ritorno alla cartella superiore; indicazione UEFI visibile. Prossimo passo aprire SystemRescue, terza voce dopo il ritorno: tre pressioni di freccia giù e Invio, poi acquisire il menu risultante. La voce SystemRescue è confermata, mentre versione, immagine avviabile e strumenti effettivamente disponibili non sono ancora verificati. Nessun ambiente live avviato e nessun nuovo controllo dei dischi eseguito.

Restano aperti SMART completo, firmware e autotest supportati dei tre SSD, oltre alla destinazione dei dati SanDisk. RAM-03/A2, 8 GB e AHCI restano la configurazione osservata. Il riscontro conferma il menu di avvio, non l'esecuzione di una diagnostica. Nessuna modifica ai dischi; immagine conservata privatamente con verifica SHA-256 e originale mantenuto.

## 23/10/2026: SystemRescue 8.07 avviato, identificazione dei dischi da console

Acquisita la sequenza dal file SystemRescue nel menu Medicat, attraverso la schermata Ventoy con Boot in normal mode selezionato, fino al menu GNU GRUB 2.06 con Boot SystemRescue using default options selezionato. L'utente riferisce che l'avvio è proseguito da solo senza selezionare manualmente la voce; la successiva console conferma SystemRescue 8.07 x86_64, tty1/6, accesso root automatico e prompt disponibile. La versione 2.06 è di GRUB, mentre quella del sistema live è 8.07. Prossimo controllo, nel prompt della console del NAS: digitare `lsblk -d -o NAME,SIZE,MODEL,TRAN`, premere Invio e acquisire l'output. Il dato necessario è la corrispondenza osservata fra nome Linux, capacità, modello e trasporto di ciascun disco, distinguendo i tre SSD SATA dalla chiavetta USB; non assegnare /dev/sda o altri nomi per supposizione. La console pronta verifica l'avvio del live, non la salute dei dischi. SMART completo e autotest non ancora eseguiti.

Restano aperti SMART completo, firmware e autotest supportati dei tre SSD, oltre alla destinazione dei dati SanDisk. RAM-03/A2, 8 GB e AHCI restano la configurazione osservata. Il riscontro conferma il menu di avvio, non l'esecuzione di una diagnostica. Nessuna modifica ai dischi; quattro immagini conservate privatamente con verifica SHA-256 e originali mantenuti.

## 23/10/2026: SSD identificati in Linux e passaggio al desktop per facilitare l'uso

Riuscito il comando `lsblk -d -o NAME,SIZE,MODEL,TRAN` nella console di SystemRescue 8.07: /dev/sda SanDisk SDSSDA240G, 223.6G, SATA; /dev/sdb KINGSTON SV300S37A240G, 223.6G, SATA; /dev/sdc WDC WDS250G1B0A-00H9H0, 232.9G, SATA; /dev/sdd Flash Disk, 58.2G, USB. Presente anche loop0 da 693.6M, da non confondere con gli SSD. La schermata contiene un errore di un tentativo precedente, seguito dall'elenco valido; nessun guasto ai dischi dedotto dall'errore di comando. L'utente riferisce notevole difficoltà a digitare anche cambiando tastiera; layout effettivo e causa non verificati. Si adatta il percorso: digitare soltanto `startx`, Invio e acquisire il desktop o l'eventuale errore. Il manuale ufficiale S188 documenta startx; S189 registra l'aggiunta di GSmartControl dalla versione 8.03, S190 il suo avvio dal menu desktop. La disponibilità effettiva di GSmartControl nell'immagine corrente va ancora vista. Desktop e interfaccia SMART non ancora avviati; lettura completa e test lungo restano pendenti.

Restano aperti SMART completo, firmware e autotest supportati dei tre SSD, oltre alla destinazione dei dati SanDisk. RAM-03/A2, 8 GB e AHCI restano la configurazione osservata. Il riscontro identifica i dispositivi nella sessione Linux; non ne misura ancora salute, usura o risultato degli autotest. Nessuna modifica ai dischi; immagine conservata privatamente con verifica SHA-256 e originale mantenuto.

| Nome nella sessione live | Modello letto | Dimensione riportata da lsblk | Trasporto | Ruolo previsto |
|---|---|---|---|---|
| /dev/sda | SanDisk SDSSDA240G | 223.6G | sata | dati, porta SATA6G_1 |
| /dev/sdb | KINGSTON SV300S37A240G | 223.6G | sata | avvio, porta SATA6G_2 |
| /dev/sdc | WDC WDS250G1B0A-00H9H0 | 232.9G | sata | dati, porta SATA6G_6 |
| /dev/sdd | Flash Disk | 58.2G | usb | chiavetta diagnostica |
| loop0 | non mostrato | 693.6M | non mostrato | dispositivo loop, escluso dai tre SSD SATA |

La mappa deriva dall'output reale di questa sessione, non dal solo ordine dei cavi; i nomi Linux possono cambiare dopo un riavvio o una modifica ai collegamenti. Le letture SMART successive devono confrontare ancora il modello dell'unità. L'avvio del desktop è soltanto richiesto, non ancora verificato. Fonti: S188, S189 e S190 nel registro unico.

## 23/10/2026: desktop grafico avviato, apertura del controllo SMART da verificare

Desktop grafico Xfce di SystemRescue 8.07 avviato e visibile, con icone File System e Home e pannello inferiore. Prossimo passo aprire il menu applicazioni in basso a sinistra, cercare GSmartControl nella categoria System ed aprirlo se presente; acquisire la finestra dei dischi, oppure il menu aperto se la voce manca. La posizione della voce è un percorso da verificare, non un menu già osservato. GSmartControl e i dati SMART completi non ancora acquisiti. Mappa della sessione già letta: /dev/sda SanDisk, /dev/sdb Kingston V300, /dev/sdc WD Blue, /dev/sdd USB; RAM-03/A2, 8 GB e AHCI restano la configurazione osservata. Dati SanDisk, autotest supportati, risultato lungo e accettazione finale ancora pendenti. Nessuna installazione o creazione di pool eseguita.

Il desktop disponibile conferma l'avvio grafico; la lettura SMART e l'esito dei test restano verifiche distinte. Si usa il mouse per ridurre la difficoltà di digitazione riferita dall'utente. Riferimenti già consultati: S188 per startx e S189/S190 per il percorso verso GSmartControl. Immagine conservata privatamente con SHA-256 verificato e originale mantenuto.

## 23/10/2026: GSmartControl aperto, controllo SMART generale superato dai tre SSD

GSmartControl aperto e inventario dei tre SSD più Flash Disk visibile. Selezionando le unità, il programma mostra Basic health check: PASSED per SanDisk SDSSDA240G /dev/sda 240.06 GB, KINGSTON SV300S37A240G /dev/sdb 240.06 GB e WDC WDS250G1B0A-00H9H0 /dev/sdc 250.06 GB. Enable SMART risulta selezionato per tutti e tre; la schermata non prova chi abbia cambiato l'impostazione. Le famiglie mostrate sono SandForce Driven SSDs per SanDisk e Kingston, WD Blue / Red / Green SSDs per WD: sono etichette del database del programma, senza diagnosi del controller reale. PASSED riguarda lo stato SMART generale, non un test lungo superato né una misura della vita residua. Prossimo passo doppio clic sul SanDisk in alto a sinistra, poi scheda Attributes e foto leggibile degli attributi. Se la finestra è piccola, ingrandirla; se non compare Attributes, acquisire la finestra dei dettagli aperta. Firmware, attributi completi, capacità ed esito del test lungo ancora da acquisire.

| Dispositivo osservato | Modello | Capacità riportata dalla GUI | Basic health check | Enable SMART |
|---|---|---|---|---|
| /dev/sda | SanDisk SDSSDA240G | 240.06 GB | PASSED | selezionato |
| /dev/sdb | KINGSTON SV300S37A240G | 240.06 GB | PASSED | selezionato |
| /dev/sdc | WDC WDS250G1B0A-00H9H0 | 250.06 GB | PASSED | selezionato |

Il risultato generale SMART è distinto dal log degli autotest e dagli attributi di usura, come spiegato dal manuale S186. La nuova osservazione chiude la verifica della presenza e apertura del programma; mantiene aperti dati completi e test dei dischi.

Immagini archiviate privatamente con confronto SHA-256; originali conservati. Nessun test o modifica dei dati dedotto dalla semplice selezione delle unità.

## 23/10/2026: attributi SMART del SanDisk letti, verifica dei test ancora aperta

Letta la scheda Attributes del SanDisk SDSSDA240G /dev/sda in GSmartControl, revisione struttura SMART 1. Tutte le righe visibili riportano Failed: never. Valori acquisiti: ID5 RAW0; ore19193h+00m+00.000s; cicli1877; ID166 RAW51; ID168 RAW102; ID173 RAW65; perdite inattese di alimentazione ID174 RAW62; Reported Uncorrectable ID187 RAW0; Command Timeout ID188 RAW0; temperatura34 gradi con Min/Max0/59; SATA CRC Error Count ID199 RAW0; spazio di riserva ID232 VAL100 WOR100 THR4 RAW100; scritture ID241 RAW29129 GiB e letture ID242 RAW54361 GiB secondo il profilo specifico. Il profilo corrente S187 per il modello esatto chiama ID166 Min_PE_Cycles e ID168 Max_PE_Cycles: le etichette GUI Later Bad Block Count e SATA Physical Error Count non sono usate per dichiarare 51 blocchi guasti o 102 errori di collegamento. ID232 non è una percentuale di vita residua; i campi grezzi composti non vengono convertiti in usura totale. Prossimo passo aprire la scheda Self-tests già visibile e acquisirla per verificare test disponibili e log. Firmware e dati generali ancora da leggere, test lungo non avviato né concluso.

| ID | Etichetta mostrata dalla GUI | Valore grezzo o visualizzato | Lettura e limite |
|---|---|---|---|
| 5 | Retired Block Rate | 0 | S187: Retired_Block_Count; nessun blocco ritirato nel contatore mostrato |
| 9 | Power-On Time | 19193h+00m+00.000s | tempo mostrato dalla GUI, non età di acquisto |
| 12 | Power Cycle Count | 1,877 | 1877 cicli mostrati |
| 166 | Later Bad Block Count | 51 | S187: Min_PE_Cycles, non interpretato come 51 blocchi guasti |
| 167 | SSD Protect Mode | 0 | S187: Max_Bad_Blocks_Per_Die; etichetta GUI conservata come osservazione |
| 168 | SATA Physical Error Count | 102 | S187: Max_PE_Cycles, non interpretato come 102 errori SATA |
| 169 | Bad Block Count | 0 | S187: Total_Bad_Blocks |
| 170 | Reserved Block Count | 0 | S187: Grown_Bad_Blocks |
| 171 | Program Fail Count | 0 | contatore visibile a zero |
| 172 | Erase Fail Count | 0 | contatore visibile a zero |
| 173 | Erase Count | 65 | S187: Average_PE_Cycles |
| 174 | Unexpected Power Loss Count | 62 | dato storico; non prova un guasto attuale all'alimentatore |
| 187 | Reported Uncorrectable | 0 | contatore visibile a zero |
| 188 | Command Timeout | 0 | contatore visibile a zero |
| 194 | Temperature (Celsius) | 34, Min/Max 0/59 | VAL66 e WOR41 sono normalizzati; estremo minimo conservato come mostrato |
| 199 | SATA CRC Error Count | 0 | contatore visibile a zero |
| 232 | Available reserved space | 100 | VAL100, WOR100, THR4; spazio di riserva distinto dalla vita residua complessiva |
| 233 | Internal Attribute | 15,197 | S187: NAND_GiB_Written, senza rapporto di amplificazione calcolato |
| 234 | Internal Attribute | 72,521 | significato specifico non dedotto |
| 241 | Total GiB Written | 29,129 | S187: Lifetime_Writes_GiB; nessuna percentuale TBW dedotta |
| 242 | Total GiB Read | 54,361 | S187: Lifetime_Reads_GiB |
| 244 | Average Erase Count | 0 | nessuna conclusione di usura nulla da questo solo campo |

I campi 165 e 230 mostrano valori composti molto grandi: conservati nell'immagine e non convertiti in percentuale o conteggio fisico senza una lettura testuale completa e il formato appropriato. Nessuna riga visibile riporta un fallimento di soglia; ciò resta distinto da un autotest completo. Il database ufficiale S187 confrontato è quello corrente, mentre versione del database locale e firmware reale sono ancora da acquisire.

Foto archiviata privatamente con SHA-256 identico, originale conservato.

## 23/10/2026: selezionato il test esteso del SanDisk prima dell'assenza

Nella scheda Self-Tests del SanDisk SDSSDA240G /dev/sda risulta selezionato Extended Self-test, durata stimata 10 min, log con zero voci. L'utente chiede se lanciarlo prima di andare via: indicato di premere Execute e lasciare il NAS acceso e alimentato. Il test termina da solo e non cancella i dati. Questo riscontro documenta la selezione, senza ancora attestare avvio o completamento; prevista lettura del log al ritorno, senza foto intermedia obbligatoria.

## 26/10/2026: SanDisk supera il test esteso, prossimo Kingston

La scheda Self-Tests del SanDisk SDSSDA240G /dev/sda mostra Test completed e Test result: Completed without error. Self-Test Log contiene una voce Extended offline, stato Completed without error e completamento 100%. Confermato quindi l'esito positivo del test esteso sul SanDisk. La schermata precedente del 23/10 documentava selezione Extended Self-test, stima10min e log0voci; quella ricevuta il26/10 documenta il risultato. Non si deduce un test durato tre giorni né una prova continua del NAS durante l'assenza. Il campo Lifetime hours della foto finale non è trascritto perché poco leggibile. Firmware SanDisk e dettagli/test degli altri SSD restano da acquisire. Prossimo passo chiudere i dettagli SanDisk, aprire con doppio clic KINGSTON SV300S37A240G, scheda Self-tests, selezionare Extended Self-test se disponibile e premere Execute; acquisire la schermata per verificare unità, tipo di test e stato. Nessuna ripetizione del test SanDisk richiesta.

| Riscontro del SanDisk /dev/sda | Valore osservato il 26/10/2026 |
|---|---|
| Stato della finestra | Test completed |
| Test result | Completed without error |
| Voci nel Self-Test Log | 1 |
| Tipo nella voce del log | Extended offline |
| Stato nella voce del log | Completed without error |
| Completamento | 100% |

Il risultato riguarda l'autotest esteso di questo SSD. La durata effettiva non è ricavabile dalle due fotografie; i 10 minuti erano una stima del firmware. L'esito non chiude i test Kingston/WD, le decisioni sui dati SanDisk o l'accettazione della configurazione NAS.

Le due immagini sono conservate privatamente con SHA-256 verificati e originali mantenuti.

## 26/10/2026: Kingston supera il test esteso, prossimo WD Blue

La scheda Self-Tests del KINGSTON SV300S37A240G /dev/sdb mostra Test completed e Test result: Completed without error. Il log contiene una voce Extended offline, Completed without error e completamento 100%. Anche il Kingston ha quindi superato l'autotest esteso: due dei tre SSD hanno ora un esito esteso documentato, SanDisk e Kingston. La durata effettiva non viene ricavata dalla fotografia. Prossimo passo chiudere i dettagli Kingston, aprire con doppio clic WDC WDS250G1B0A-00H9H0, scheda Self-tests, scegliere Extended Self-test se disponibile e premere Execute, poi acquisire la schermata. Test esteso WD ancora pendente; nessuna ripetizione di SanDisk o Kingston richiesta. Firmware e dettagli ancora mancanti restano da raccogliere. Chiesto in parallelo se sul SanDisk ci siano file da conservare prima del futuro pool: risposta ancora attesa, nessuna cancellazione autorizzata da questa verifica.

| SSD | Test esteso documentato | Esito |
|---|---|---|
| SanDisk SDSSDA240G, /dev/sda | Extended offline,100%,una voce | Completed without error |
| KINGSTON SV300S37A240G, /dev/sdb | Extended offline,100%,una voce | Completed without error |
| WD Blue WDS250G1B0A-00H9H0, /dev/sdc | ancora da acquisire | pendente |

Il nuovo risultato chiude la verifica del test esteso Kingston. Il completamento di un autotest non autorizza a cancellare i dati e non sostituisce le decisioni sull'allocazione o l'accettazione finale del NAS.

Immagine conservata privatamente con SHA-256 verificato, originale mantenuto.

## 26/10/2026: WD Blue supera il test esteso, tre SSD con esito positivo

La scheda Self-Tests del WDC WDS250G1B0A-00H9H0 /dev/sdc mostra Test completed e Test result: Completed without error. Il log contiene una voce Extended offline, stato Completed without error e completamento100%. Sono quindi documentati tre autotest estesi superati, uno per ciascuno dei tre SSD del NAS: SanDisk, Kingston V300 e WD Blue. La stima10min mostrata per il WD non viene chiamata durata effettiva. Nessuna ripetizione dei test è richiesta. Per completare identificazione e usura manca una raccolta via GUI: General e Attributes del WD, General e Attributes del Kingston, General del SanDisk; gli attributi SanDisk sono già acquisiti. I seriali eventualmente presenti nelle foto restano nel livello privato. La domanda sui file da conservare sul SanDisk è ancora senza risposta: nessuna cancellazione o creazione di pool eseguita. Firmware, restanti dati di usura, accettazione finale e riallocazione RAM restano aperti.

| SSD | Autotest esteso documentato | Esito |
|---|---|---|
| SanDisk SDSSDA240G, /dev/sda | Extended offline,100%,una voce | Completed without error |
| KINGSTON SV300S37A240G, /dev/sdb | Extended offline,100%,una voce | Completed without error |
| WD Blue WDS250G1B0A-00H9H0, /dev/sdc | Extended offline,100%,una voce | Completed without error |

La fase dei test estesi dei tre SSD ha esito positivo. Per completare la lettura di identificazione e usura restano le schede General dei tre dischi e Attributes di Kingston/WD. Lo stato dei file SanDisk va chiarito prima di creare lo specchio; l'esito degli autotest non autorizza cancellazioni e non sostituisce l'accettazione complessiva del NAS.

Immagine conservata privatamente con SHA-256 verificato, originale mantenuto.

## 26/10/2026: raccolta SMART completata e ISO TrueNAS 25.10.7 verificata

Acquisite in lettura sei foto Telegram, General e Attributes per tutti i tre SSD. Firmware SanDisk Z32070RL, Kingston605ABBF2 e WD X41100WD; smartctl7.2r5155. Tutte le righe visibili Failed: never; tre generali PASSED e tre estesi già superati. Le foto contengono identificativi conservati fuori dalla prosa pubblica. Al successivo tentativo di copia i sei file non risultano più nella cartella indicata: valori trascritti e associazioni sono salvati, ma la copia dei JPEG originali rimane da recuperare.

| SSD e ruolo previsto | Firmware letto | Ore mostrate | Cicli | Temperatura | Scritture/letture host mostrate | Esiti |
|---|---|---|---|---|---|---|
| SanDisk SDSSDA240G, dati SATA6G_1 | Z32070RL | 19257h+00m+00.000s | 1877 | 34 °C | 29129 / 54361, etichetta GUI GiB | generale PASSED, esteso superato |
| KINGSTON SV300S37A240G, avvio SATA6G_2 | 605ABBF2 | 32299h+36m+50.720s | 3586 | 27 °C | 51835 / 64524, etichetta GUI GiB | generale PASSED, esteso superato |
| WDC WDS250G1B0A-00H9H0, dati SATA6G_6 | X41100WD | 18580 | 2779 | 31 °C | 26648 / 48194, etichetta GUI GiB | generale PASSED, esteso superato |

Le tre General mostrano SMART supportato e abilitato, settore logico/fisico di 512 byte, TRIM disponibile, collegamento SATA attuale a 6 Gb/s e smartctl 7.2 del 30/12/2020, revisione r5155. Nessun firmware è stato aggiornato. I seriali e i WWN delle General sono conservati solo nelle immagini private.

Per il Kingston i contatori visibili di blocchi ritirati, riallocazioni, errori di programmazione/cancellazione e Reported Uncorrectable sono zero; ID231 SSD Life Left mostra VAL95, WOR95, soglia11 e RAW111669149696. S198 descrive un indice approssimativo di usura, non una probabilità di sopravvivenza né anni residui; non si converte il RAW composto in percentuale. Il CRC SATA non compare nella tabella Kingston acquisita e non viene dichiarato zero. ID174 mostra272 e ID177 mostra1; sono dati storici, non una diagnosi dell'alimentatore.

Per il WD il profilo S187 comprende esattamente modello e firmware X41100WD: ID166 è Minimum_PE_Cycles_TLC20, ID168 Maximum_PE_Cycles_TLC73, ID173 Average_PE_Cycles_TLC48. Le etichette GUI di166/168 non diventano conteggi di guasti. ID169 Total_Bad_Blocks202 è registrato separatamente da ID170 Grown_Bad_Blocks0 e ID5 riallocazioni0; non si inventa l'origine del202 o la sua evoluzione da una sola lettura. Program/Erase Fail, End-to-End, Reported Uncorrectable, Command Timeout e CRC sono0; spazio di riserva ID232100 con soglia4. Nessuna percentuale di vita totale dedotta da riserve100 o ID230 composto.

La nuova lettura SanDisk mostra19257 ore al posto delle19193 della precedente acquisizione; gli altri contatori principali acquisiti coincidono. Il confronto non dimostra da solo la durata continua della prova o dell'accensione. Le tre schede Attributes riportano Failed: never in tutte le righe visibili. I valori sono una base per il monitoraggio, non una garanzia futura.

## ISO sulla chiavetta

TrueNAS25.10.7 è il ramo General raccomandato, S200/S201. ISO2339317760byte, SHA-25654ce9441ce66966a392e28f63604ca3c2c083d0bec4db7bb5af2f74f7a007c8e, confrontato con S202 e pagina ufficiale indipendente; firma PGP non verificata. Su richiesta esplicita spostate la25.10.7 nella cartella Live_Operating_Systems/TrueNAS della partizione dati Ventoy e la25.10.4 dal Desktop in Archivio. Le due copie corrispondono alle sorgenti SHA-256, rimosse solo dopo entrambe le verifiche. Nessuna formattazione o modifica EFI, avvio della25.10.7 ancora da osservare.

## RAM e recap finale del26/10/2026

L'utente chiarisce di volere almeno un secondo modulo8 GB nelNAS e gli altri due come scorta, quindi autorizza gli ulteriori test necessari per avanzare. La configurazione attuale restaRAM-03 solaA2,8 GB; prossimo montaggio da eseguireRAM-01 inB2, ultimo slot dallaCPU. Questa coppia16 GB non risulta già provata; la coppiaRAM-03/A2+RAM-04/B2 era invece fallita e non viene semplicemente ripetuta. BIOS atteso16384 MB,2133 MHz,XMP disabilitato; Memtest86+8.10,quattro passaggi senza errori o stop al primo errore. RAM-01 aveva fallitoA1/A2: la destinazione scelta non ne cambia retroattivamente l'esito. RAM-02/04 restano le due scorte fisiche richieste, conservate con errori registrati. QuattroCrucial4 GB restano alserver,16 GB censiti. Le alternative12/12 e16/8 non sono state scelte. ADR-039 registra obiettivo e prova, non montaggio o pass già osservati. Il chiarimento sui fileSanDisk è ancora pendente.

## 26/10/2026: montata la coppia RAM-03/A2 e RAM-01/B2, BIOS ancora da verificare

La nuova fotografia del NAS mostra i moduli etichettati RAM-03 in A2 e RAM-01 in B2; A1 e B1 risultano vuoti. Il montaggio richiesto è quindi osservato: due moduli nominali da8 GB, non ancora una lettura BIOS da16 GB o un test superato. L'utente chiede di procedere. Prossimo collegare alimentazione e chiavetta Medicat, accendere ed entrare nel BIOS con Canc. Verificare16384 MB,2133 MHz e XMP disabilitato prima di Memtest86+8.10. La prova della coppia prevede quattro passaggi completi senza errori oppure stop al primo errore. Avvio e risultato non ancora acquisiti. La fotografia è stata copiata subito nell'archivio privato con SHA-256 identico e originale conservato.

## 26/10/2026: BIOS conferma 16384 MB con RAM-03/A2 e RAM-01/B2

Il BIOS ASUS H170-PRO versione 3805, i7-6700, mostra Memory 16384 MB (DDR4 2133 MHz), XMP Disabled. DRAM Status: DIMM_A1 N/A, DIMM_A2 TEAMGROUP 8192 MB 2400 MHz, DIMM_B1 N/A, DIMM_B2 TEAMGROUP 8192 MB 2400 MHz. I 2400 MHz delle righe dei moduli sono distinti dai 2133 MHz operativi indicati in alto. Le etichette RAM-03/A2 e RAM-01/B2 derivano dalla precedente foto del montaggio. Riconoscimento dei 16 GB confermato; questo non è un esito di stabilità. Memtest della nuova coppia non ancora osservato. Restano quattro passaggi completi senza errori oppure stop al primo errore, secondo ADR-039. Prossimo F8 e selezione UEFI: Generic, Partition 2; se la voce manca acquisire il menu. In Medicat avviare Diagnostic Tools, Memtest86+ 8.10 e acquisire la schermata iniziale della coppia. La schermata EZ Mode mostra anche la voce Intel Rapid Storage Technology con indicazione On: non sostituisce una lettura di SATA Mode in Advanced, già verificato AHCI nel giro precedente; non è stata richiesta alcuna modifica ora. Tre SSD ancora visibili su SATA6G_1, _2 e _6. Immagine copiata nell'archivio privato, SHA-256 identico e originale conservato.

## 26/10/2026: avviato Memtest sulla coppia RAM-03/A2 e RAM-01/B2

L'utente riferisce l'avvio e la schermata lo conferma: Memtest86+ v8.10, build 8.10.49468.x64, ASUS H170-PRO e i7-6700, quattro core e otto thread, SMP 8T PAR. Alla lettura iniziale Time 0:00:03, Status Testing, Pass 0, Errors 0, progresso del passaggio 0%, Test 15%, Test #3 Moving inversions, 1s & 0s. Memoria 15.8 GB, IMC 1069 MHz (DDR4-2138), CAS 15-15-15-35; CPU 3400 MHz, indicazione termica 42/48 °C. SPD Slot 1: TEAMGROUP 8 GB DDR4-2400, 2016-W48; Slot 3: TEAMGROUP 8 GB DDR4-2400, 2016-W40. La combinazione fisica RAM-03/A2 e RAM-01/B2 deriva dal montaggio già fotografato, e il BIOS precedente confermava 16384 MB a 2133 MHz, XMP disabilitato. Questi sono contatori iniziali: non documentano un passaggio completo o il superamento della prova. Proseguire con questa stessa configurazione fino a quattro passaggi completi senza errori, oppure stop al primo errore con foto dei contatori e della riga di errore. Nessun ulteriore spostamento RAM richiesto. Immagine archiviata subito, SHA-256 identico, originale conservato.

## 26/10/2026: fallita RAM-03/A2 più RAM-01/B2, spiegato il rischio della RAM volatile

Due letture della stessa prova Memtest86+ 8.10 mostrano Status Failed, Pass 0, Errors 1. Prima lettura a 0:20:49 con banner FAIL, seconda a 0:20:54 senza banner: non sono due errori o due test diversi. Il passaggio è al 99% ma il contatore Pass resta 0. Nella seconda lettura il test corrente è #10 Bit fade test, 2 patterns, al 65%; la riga che ha registrato l'errore indica invece Test 9, pCPU 0, Pass 0, Failing Address 0x000100d49410 (4.01 GB), Expected 0x3d12e399ff15f5d8, Found 0x3d12e399ff15fdd8. XOR calcolato 0x800: un solo bit differente, bit 11 contando da zero. Il tempo è quello della lettura, non il momento esatto del bit alterato. Coppia RAM-03/A2 + RAM-01/B2 ricavata dal montaggio precedente; non si attribuisce il bit a un singolo DIMM dall'indirizzo. Memoria 15.8 GB, DDR4-2138, CAS 15-15-15-35; temperature mostrate 42/54 e 41/54 °C. Criterio di stop al primo errore raggiunto: richiesto spegnimento, ancora da confermare; nessun nuovo innesto o test identico assegnato. Obiettivo 16 GB aperto. Immagini archiviate subito con SHA-256 corrispondenti e originali conservati. Fonti S126, S129 e S204 rilette per significato dei campi, limiti diagnostici e conseguenze sui dati.

Volatile descrive ciò che accade togliendo corrente: il contenuto della RAM si perde. Durante il funzionamento, invece, la RAM contiene dati dei file, cache e strutture del sistema operativo. Un dato alterato in RAM può essere scritto su SSD e diventare un errore persistente; un blocco già letto può anche essere inviato alterato al PC che lo sta copiando. Sono possibili crash e blocchi, oppure corruzione senza un crash evidente. Il mirror protegge da alcuni guasti dei dischi, ma due dischi possono ricevere lo stesso dato già errato. Un checksum calcolato dopo l'alterazione può essere coerente con il dato sbagliato: è un esempio del limite di un controllo posto a valle, non un guasto ZFS già osservato. Non è possibile tradurre un errore Memtest in una percentuale di file corrotti o in un intervallo di tempo al guasto. Il rischio dipende da quale contenuto occupa la zona interessata e da quando viene usato. La guida TrueNAS 25.10, S204, descrive esplicitamente crash e perdita o corruzione di dati causati da errori RAM, pur riconoscendo che molti sistemi funzionano senza ECC. Non avere ECC e avere errori riprodotti sono condizioni diverse; non viene imposto un cambio di piattaforma o un acquisto ECC.

## 26/10/2026: NAS spento dopo il fallimento della coppia, cavo ancora da scollegare

L'utente conferma che il NAS è spento. Non conferma ancora lo scollegamento del cavo di alimentazione; il prossimo gesto richiesto è scollegarlo, prima di toccare i moduli. Nessun nuovo montaggio, avvio o test. Restano RAM-03/A2 e RAM-01/B2 all'ultimo riscontro, con esito negativo della coppia già registrato; obiettivo 16 GB invariato e Crucial sul server.

## 26/10/2026: cavo NAS scollegato, richiesta rimozione della sola RAM-01/B2

L'utente risponde fatto alla richiesta di scollegare il cavo di alimentazione: NAS spento e scollegato confermati. Prossimo gesto richiesto: rimuovere soltanto RAM-01 da B2, ultimo slot dalla CPU, lasciando RAM-03 in A2. Rimozione non ancora confermata, nessuna riaccensione o nuova prova assegnata. RAM-01 resta conservata con gli errori registrati, senza qualifica come ricambio funzionante. La rimozione separa la coppia appena fallita e non decide una riduzione permanente a 8 GB: obiettivo NAS 16 GB ancora aperto, Crucial invariati sul server e nessun acquisto deciso.

## 26/10/2026: RAM-01 rimossa, resta RAM-03/A2, prossimo avvio installer con 8 GB provvisori

L'utente conferma RAM-01 rimossa, dopo spegnimento e scollegamento già confermati. Nel NAS resta RAM-03 da 8 GB in A2; B2 torna vuoto, nessun altro modulo aggiunto. RAM-01 conservata fuori con gli errori registrati, come RAM-02/04, senza smaltimento o qualifica come ricambio funzionante. La precedente prova singola RAM-03/A2 ha circa 22 ore senza fail riferite; non si richiede una ripetizione identica per il solo ritorno alla configurazione. Passo operativo successivo: avviare la chiavetta UEFI con F8, Generic Partition 2, poi Live_Operating_Systems/TrueNAS/TrueNAS-SCALE-25.10.7.iso. Si usa la configurazione provvisoria da 8 GB, minimo base documentato in S204, mantenendo aperto l'obiettivo 16 GB di ADR-039. Aggiungere in seguito un modulo utilizzabile non richiede reinstallare TrueNAS. Nuova accensione e installer ancora non osservati; nessun disco cancellato, Kingston resta la sola destinazione prevista dell'installazione e i dati SanDisk sono ancora da chiarire prima del pool. Crucial invariati sul server, nessun acquisto o riduzione permanente a 8 GB decisi.

## 26/10/2026: avvio TrueNAS 25.10.7 fino al menu installer, errori di boot registrati

L'utente dichiara di aver eseguito i passi e le tre immagini mostrano in sequenza GRUB con Start TrueNAS SCALE Installation selezionato, log del live e TrueNAS 25.10.7 Console Setup con 1 Install/Upgrade selezionato, oltre a Shell, Reboot e Shutdown. La copia di filesystem.squashfs in RAM è mostrata al 100%. Nel log sono leggibili SGX disabled or unsupported by BIOS, mount della sorgente in sola lettura, Failed to open /dev/shm device, ignoring: Inappropriate ioctl for device, firmware Realtek rtl_nic/rtl8168h-2.fw non caricato (-2) e soprattutto Failed to start mount-cd.service - Mount installation media. Non si attribuiscono questi messaggi alla RAM e non si dichiarano risolti o ininfluenti dall'apparizione successiva del menu. NAS acceso con sola RAM-03/A2 da 8 GB secondo il montaggio confermato; nessuna nuova lettura BIOS della memoria nelle tre foto. Boot raggiunto fino al menu, non installazione conclusa o disponibilità completa del media provata. Prossimo premere Invio su Install/Upgrade e acquisire l'elenco delle destinazioni: previsto soltanto Kingston V300 240 GB, ancora da identificare nel live attuale. Nessuna lettera sda/sdb viene ereditata da precedenti sessioni. Nessun disco selezionato o cancellato, file SanDisk ancora da chiarire prima del pool, obiettivo 16 GB aperto. Guida ufficiale stabile Installing TrueNAS letta, S205; il passo apre la selezione, la cancellazione richiede una conferma successiva. Tre immagini copiate subito e rilette, SHA-256 coincidenti con gli originali conservati.

## 26/10/2026: Kingston identificato come sdc, prima della cancellazione verifica del supporto

La schermata Choose Destination Media di TrueNAS 25.10.7 elenca sda SanDisk SDSSDA2, NTFS, 223.57 GiB; sdb WDC WDS250G1B0A, NTFS, 232.89 GiB; sdc KINGSTON SV300S, ext4, 223.57 GiB; sdd Flash Disk Medicat, NTFS, 58.2 GiB. Tutte le caselle sono vuote e l'evidenziazione è sul SanDisk, non sul Kingston. Il Kingston destinato al sistema è quindi sdc, terza riga: la vecchia mappa sdb Kingston e sdc WD non vale in questo avvio. Nessun disco è ancora selezionato o cancellato. Poiché il log precedente mostrava mount-cd.service fallito, si richiede un controllo del media prima della conferma di cancellazione: Esc, ritorno al menu, 2 Shell, ls -lh /cdrom, foto del risultato. Il comando legge la cartella; nessun nuovo mount o scrittura è assegnato. Fonti ufficiali correnti consultate e scaricate: scale-build al commit 2b2b629f7726daeb2dc5b618ecdd8e1014723a45, script mount-cd con mountpoint /cdrom e ricerca TrueNAS-SCALE.update; truenas-installer al commit b988b96279e33ab799326205b6e3e8c8879b2ae1, install.py che nel codice corrente formatta prima di montare /cdrom/TrueNAS.update. Non sono versioni confrontate con i file della ISO 25.10.7; i nomi payload differiscono e non si deve dedurre la causa o imporre un nome file dal solo master. La verifica ls sul live risolve la presenza effettiva del supporto. Lettura ancora non eseguita o osservata. RAM-03/A2 da 8 GB provvisori invariata, obiettivo 16 GB aperto, dati SanDisk ancora da chiarire. Immagine archiviata subito con SHA-256 corrispondente e originale conservato.

## 26/10/2026: payload presente in /cdrom, si torna alla selezione del solo Kingston

La Shell mostra il comando ls -lh /cdrom eseguito e il suo elenco: total 2.0G, file TrueNAS-SCALE.update da 1.9G, directory EFI, System, boot, efi, live, oltre a boot.catalog, efi.img, initrd.img, mach_kernel e vmlinuz. In alto è visibile un tentativo precedente con /cd-rom inesistente, corretto nel comando riuscito: non è un errore della cartella /cdrom. Nel live il payload è presente e il controllo richiesto ha dato il riscontro necessario a proseguire. Non si dichiara una verifica byte per byte del payload, un nuovo checksum della ISO, un servizio mount-cd ora attivo o la causa certa del fallimento di avvio. Non si rinomina il file TrueNAS-SCALE.update in TrueNAS.update sulla base di sorgenti di un'altra versione. Nessun nuovo mount, formattazione USB o test RAM richiesto. Prossimo exit, 1 Install/Upgrade, navigare su sdc KINGSTON SV300S 223.57 GiB, selezionarlo con Spazio assicurando che solo quel disco abbia l'asterisco, OK e Yes all'avviso di cancellazione relativo al Kingston; acquisire la schermata successiva. La cancellazione del Kingston è compresa nell'installazione sul disco di avvio già prevista, senza estendere l'azione a SanDisk, WD o USB. Selezione, conferma ed effettive scritture ancora non osservate. Mappa attuale sda SanDisk, sdb WD, sdc Kingston, sdd Flash Disk. Sola RAM-03/A2 da 8 GB provvisori, obiettivo 16 GB ancora aperto e dati SanDisk pendenti prima del pool. Immagine archiviata subito, SHA-256 coincidente e originale conservato. Procedura ufficiale S205 già letta.

## 26/10/2026: installer alla scelta dell'amministratore web truenas_admin

La nuova immagine mostra Web UI Authentication Method, con Administrative user (truenas_admin) selezionato e Configure using Web UI come alternativa. L'avanzamento è coerente con i passi precedenti del flusso S205, ma il disco selezionato non è visibile in questa schermata: non è una nuova lettura del target. Destinazione assegnata dalle istruzioni: solo Kingston V300 sdc 223.57 GiB; nessuna estensione a SanDisk, WD o chiavetta. Si indica di lasciare la prima voce, confermare Invio, impostare una password unica nei due campi usando Tab e salvarla nel proprio gestore, quindi OK e foto della schermata successiva. La credenziale è da digitare localmente; nessun valore è stato richiesto, ricevuto o conservato nei file del progetto. truenas_admin è il nome pubblico predefinito del ruolo amministrativo della gestione web, distinto dalle successive utenze per le condivisioni. Conferma del metodo, password impostata, scritture ed esito conclusivo ancora non osservati; non si dichiara TrueNAS installato. NAS acceso con sola RAM-03/A2 da 8 GB provvisori, obiettivo 16 GB aperto; payload TrueNAS-SCALE.update presente in /cdrom dalla verifica precedente, dati SanDisk ancora da chiarire prima del pool. Immagine copiata subito e verificata SHA-256, originale conservato. Procedura ufficiale S205 già letta.

## 27/10/2026: truenas_admin e password confermati, installazione in avvio riferita

L'utente conferma di aver scelto truenas_admin e impostato la password, quindi riferisce che sta lanciando l'installazione. Sono conferme dichiarate, senza nuova immagine dell'avanzamento o dell'esito: non si accredita ancora Installation Succeeded, completamento o primo avvio dal Kingston. Nessun valore di password è stato richiesto, ricevuto o salvato. Prossimo lasciare proseguire con la chiavetta collegata e acquisire il messaggio finale di successo o errore prima del riavvio. Il target assegnato è solo Kingston V300 sdc nella mappa dell'installer già osservata, non una nuova verifica del disco in questo messaggio. RAM-03/A2 sola da 8 GB provvisori, obiettivo 16 GB ancora aperto, Crucial sul server; pool non creato e dati SanDisk ancora da chiarire. Non si deduce la durata dell'installazione o un funzionamento notturno dal cambio di data.

## 27/10/2026: prima lettura errata di sdc come sda e richiesta di verifica

L'agente ha inizialmente letto sdc come sda nel messaggio Installation Succeeded e ha chiesto una verifica di modelli e filesystem prima del riavvio. Quella lettura del messaggio era errata e non descrive una destinazione diversa dell'installer. La rilettura dell'originale e il risultato lsblk, registrati nella voce successiva, confermano sdc Kingston con EFI/ZFS. La richiesta eseguita era 2 Shell, lsblk -o NAME,SIZE,MODEL,FSTYPE; nessuna scrittura è stata assegnata per questa verifica. Il messaggio precedente dell'agente sul possibile SanDisk installato è rettificato, senza considerare mai dimostrata una cancellazione del SanDisk.

## 27/10/2026: Kingston con EFI e ZFS verificato, corretto errore di lettura, prossimo primo avvio

La nuova lettura lsblk -o NAME,SIZE,MODEL,FSTYPE identifica sda SanDisk SDSSDA240G 223.6G con partizioni da 450M NTFS, 99M vfat, 16M, 222.5G NTFS e 530M NTFS; sdb WDC WDS250G1B0A-00H9H0 232.9G con partizioni da 450M NTFS, 99M vfat, 16M, 231.5G NTFS e 859M NTFS. sdc è KINGSTON SV300S37A240G 223.6G, con sdc1 1M, sdc2 512M vfat e sdc3 223.1G zfs_member. sdd è Flash Disk 58.2G, partizioni NTFS da 58.2G e vfat da 32M. Il Kingston ha quindi lo schema EFI/ZFS dell'installazione e SanDisk/WD mostrano ancora le strutture NTFS, senza che ciò provi la validità dei file. Riletta a risoluzione originale anche l'immagine del successo: il testo è The TrueNAS installation on sdc succeeded, non sda. L'agente aveva letto male la lettera, causando il controllo in più; errore riconosciuto all'utente e registrato esplicitamente. Non c'è evidenza di una destinazione sbagliata dell'installer. Installazione sul Kingston verificata, primo avvio ancora da osservare. Si indica exit dalla Shell, 3 Reboot System e rimozione della USB quando parte il riavvio, poi foto della console. L'utente chiede se scegliere 1: viene chiarito che 1 Install/Upgrade riapre l'installazione e che occorre 3 Reboot System. Nessuna di queste azioni è ancora confermata o vista. Account/password impostata confermati senza valore archiviato, RAM-03/A2 sola da 8 GB provvisori, obiettivo 16 GB e dati SanDisk ancora aperti. Foto nuova copiata e verificata SHA-256, originale conservato.

## 27/10/2026: chiusura del live con messaggi unmount e watchdog, primo boot ancora da osservare

L'utente invia la prima schermata dopo le istruzioni exit e 3 Reboot System. Sono visibili Failed unmounting run-live-medium.mount - /run/live/medium e watchdog: watchdog0: watchdog did not stop. I messaggi appartengono alla chiusura dell'ambiente live già avviato dalla USB, coerente con le operazioni di smontaggio descritte in S208; non costituiscono una console del sistema installato. Il fotogramma non dimostra da solo la persistenza di un blocco e non viene attribuito a RAM, alimentatore, dischi o a un driver specifico. Rimozione USB non ancora confermata esplicitamente. Si indica di lasciare completare il riavvio e, soltanto se il sistema non è già ripartito e resta fermo così per almeno due minuti, tenere premuto il pulsante fino allo spegnimento, poi riaccendere con la chiavetta rimossa e acquisire la console. È una soglia operativa per questo passaggio, non un timeout del watchdog misurato o prescritto dalla fonte. Spegnimento manuale, nuova accensione e primo boot non ancora osservati. L'installazione sul Kingston sdc era già conclusa e verificata con EFI e ZFS; la precedente lettura sda del messaggio era errore dell'agente, già rettificato. Consultati S208 e S209: quest'ultimo è un documento storico sull'API watchdog, usato per il contesto generale, non per diagnosticare il kernel o il driver attuale. Foto archiviata subito con SHA-256 corrispondente, originale conservato. RAM-03/A2 da 8 GB provvisori, obiettivo 16 GB e dati SanDisk ancora aperti.

## 27/10/2026: primo avvio documentato in 17 foto, rete temporanea e DHCP già attivo

Archiviate e rilette tutte le17 foto fornite nella cartella Telegram: manifesto con17 sorgenti, copie, byte e SHA-256 coincidenti, originali conservati; successiva rilettura delle impronte dell'archivio completata. Le foto documentano GRUB del sistema installato25.10.7, caricamento ZFS2.3.9-1, avvio middlewared e servizi fino alla console1-10. L'ultima mostra The web interface could not be accessed. Please check network configuration, senza indirizzo di gestione. Primo boot del sistema installato quindi osservato, accesso web ancora no. Le attese ix-wait-on-disks e middlewared sono seguite nelle foto da esiti OK; le frazioni5s/20min e35s/15min10s non sono durate misurate dell'intero avvio o prove fallite. Registrati separatamente avvisi kernel MDS/MMIO/VMSCAPE, ASPM, pcspkr duplicato, dipendenze SSSD e timer ipa-epn fallito; una foto è mossa, la successiva conferma il timer. Gli avvisi non hanno impedito la console ma non vengono dichiarati risolti o usati per diagnosticare un guasto RAM. L'utente riferisce NAS temporaneamente sulla rete aziendale e chiede di preparare il resto prima della casa. Nelle ulteriori schermate sono osservati enp3s0, aliases/state.aliases vuoti, poi ipv4_dhcp Yes, ipv6_auto Yes, aliases vuoti, MTU not set. DHCP era già attivo alla lettura, non è una nuova configurazione eseguita. Prossimo Back,q,8 Open Linux Shell,ip -br address show enp3s0 e foto del risultato, ancora non acquisito. Nessun indirizzo statico, gateway, VLAN, pool, condivisione o impostazione della rete aziendale modificati. Configurazione portabile e rete definitiva tenute distinte in ADR-040 e scheda didattica03. RAM-03/A2 sola da8GB provvisori,16GB e dati SanDisk ancora aperti; nessun valore di password ricevuto o salvato.

### Preparazione prima della rete domestica definitiva

La macchina può essere preparata nella rete temporanea. L'indirizzo di gestione serve per raggiungere l'interfaccia web e non è l'identità dei dischi, degli account o dei dataset. S210 descrive il tentativo DHCP al primo avvio; qui l'opzione è già Yes ma la console non mostra un indirizzo. Prima di cambiare parametri si leggono stato del collegamento e indirizzi della scheda enp3s0. Il risultato guiderà il passo successivo, senza dedurre dal solo schermo la presenza di un guasto del driver o del server DHCP.

| Attività | Momento | Riscontro che la chiude |
|---|---|---|
| accesso di gestione temporaneo | ora, tramite la rete disponibile | interfaccia con indirizzo e login web verificati; DHCP già osservato Yes |
| lingua, tastiera e fuso Europe/Rome | dopo il primo accesso web | valori salvati in General Settings, Localization; data e sincronizzazione oraria verificate separatamente |
| controllo del disco di avvio | dopo il primo accesso | boot-pool e Kingston riconosciuti, stato ed eventuali errori letti; nessuna nuova prova estesa SSD assegnata |
| salvataggio configurazione | dopo le modifiche | export con Password Secret Seed conservato nel livello privato e in copia esterna al NAS |
| pool dati e condivisioni | dopo il chiarimento dei file SanDisk | autorizzazione concreta sui dati e verifica dei dischi per modello, poi creazione e prova reale |
| indirizzo e regole domestici | quando il NAS arriva nella rete prevista | piano IP e VLAN applicato e accessi provati dal punto di origine corretto |

S211 documenta la localizzazione, S212 lo stato del boot-pool e S158 l'export con secret seed. Sono passi preparati, non dichiarati già eseguiti. Il file di configurazione comprende stato della macchina e impostazioni di rete: al trasferimento si mantiene la configurazione utile, si applica l'indirizzamento domestico previsto e si esporta nuovamente. Il file con seed è sensibile e resta fuori dal repository pubblico. La creazione del mirror resta sospesa sui dati SanDisk; la permanenza di firme NTFS non dimostra che ogni file sia stato conservato o copiato. Nessun servizio della rete aziendale viene configurato da questo piano.

## 27/10/2026: enp3s0 DOWN senza indirizzi, richiesta lettura dei flag e verifica del cavo

La nuova immagine mostra scelta8 Open Linux Shell e comando ip -br address show enp3s0 eseguito: unica riga enp3s0 DOWN e nessun indirizzo. Nel precedente editor ipv4_dhcp era già Yes, quindi non si richiede di abilitarlo di nuovo. Prossimo ip link show enp3s0 per distinguere stato amministrativo e collegamento, oltre al controllo del cavo Ethernet lato NAS e presa/switch. Flag completi e riscontro fisico non ancora acquisiti; non si conclude dal solo DOWN che il cavo sia certamente scollegato, che il server DHCP non risponda o che il driver sia guasto. Comando richiesto di sola lettura, nessuna modifica di indirizzo, DHCP o rete aziendale. Boot e installazione restano confermati, accesso web non ancora raggiunto. Foto copiata subito, SHA-256 coincidente e originale conservato.

## 27/10/2026: cavo inizialmente assente chiarito, enp3s0 ora UP ma senza IPv4

L'utente chiarisce che doveva ancora collegare il cavo Ethernet. La nuova immagine contiene la precedente lettura DOWN e una seconda esecuzione di ip -br address show enp3s0: ora UP, con un IPv6 link-local /64 e nessun IPv4 visibile. Il collegamento operativo è quindi osservato, senza cambiare il DHCP già Yes o altre impostazioni. Il valore IPv6 completo, identificante l'interfaccia, resta nella foto privata e non viene riportato nei documenti pubblici. La richiesta precedente di leggere ip link show non è più il prossimo passo: dopo il chiarimento e il nuovo UP si indica di attendere circa un minuto e digitare exit per tornare alla console e cercare l'indirizzo web; esito dopo attesa ancora non acquisito. Si chiede inoltre se l'altro capo è su presa/switch della rete aziendale o direttamente su un PC, per non presumere un servizio DHCP disponibile; risposta ancora pendente. Non si attribuisce ancora l'assenza IPv4 al server, al driver o a restrizioni della rete e non si tenta alcuna modifica alla rete aziendale. Immagine archiviata subito con hash coincidente e originale conservato.17foto precedenti salvate e lette, primo boot confermato,16GB e dati SanDisk aperti.

## 27/10/2026: altro capo del cavo sullo switch aziendale con DHCP confermato dall'utente

L'utente risponde alla domanda sul collegamento: il cavo termina nello switch della rete aziendale, che assegna una classe IP specifica in DHCP. Non è un collegamento diretto NAS-PC e non si indicano IP statici manuali. Restano il DHCP già Yes e l'ultima lettura enp3s0 UP con solo IPv6 link-local; nessun IPv4 del NAS ancora osservato. Si conferma il prossimo gesto: breve attesa ed exit per leggere la console aggiornata, poi foto dell'indirizzo web o dell'eventuale stato ancora senza indirizzo. La disponibilità dichiarata del servizio DHCP non equivale a un lease già acquisito dal NAS. Nessuna modifica alla rete aziendale, nessun login web e nessun valore di password ricevuto.17foto archiviate e verificate, primo boot confermato,16GB e dati SanDisk ancora aperti.

## 27/10/2026: lease DHCP, login web e preferenza per gli avvisi su Proton

Le nuove schermate documentano la console con URL HTTP/HTTPS sul lease `<ip-nas-lan-temporanea>`, la pagina di login e poi la dashboard autenticata come truenas_admin. Raggiungibilità web e accesso amministrativo sono quindi verificati sulla LAN aziendale temporanea; il precedente stato senza IPv4 è superato. Nessuna modifica di DHCP, IP statici, gateway, DNS o VLAN. Dashboard25.10.7-Goldeye: 7,6 GiB disponibili, Create Pool e nessun pool dati. General Settings: memoria8 GiB, lingua English, fuso America/Los_Angeles, tastiera English (US) (us); il riquadro GUI mostra indirizzo di ascolto IPv4 0.0.0.0, che non è il lease da digitare nel browser. Indicato Localization, Settings, Europe/Rome e tastiera italiana, poi Save; salvataggio non ancora osservato e sincronizzazione oraria da verificare separatamente. Le cinque nuove immagini sono archiviate in privato e le copie sono verificate SHA-256; originali conservati.

### Destinatario, spedizione e raccolta Log NAS

L'utente propone le notifiche email e preferisce Proton `<email-destinatario-nas>`; Gmail `<email-alternativa-nas>` resta alternativa. Il destinatario indica dove leggere i messaggi; il servizio di spedizione autentica il NAS e li inoltra. La destinazione Proton può quindi essere mantenuta anche scegliendo un altro provider in uscita. Il riquadro Email mostra Send Mail Method SMTP: questa sola etichetta non verifica impostazioni o recapito. Gmail OAuth è proposto per l'invio con un account disponibile, senza scelta o login ancora eseguiti. Credenziali e autorizzazione si inseriscono localmente nella GUI; nessun segreto ricevuto o scritto nella documentazione pubblica.

TrueNAS25.10 usa Email Recipients nelle impostazioni di sistema e permette il test Send Test Mail. Il servizio in Alert Settings ha una propria soglia e prova Send Test Alert. La verifica operativa richiesta comprende ricezione effettiva su Proton del test di posta e dell'alert; i due esiti restano aperti. Il trasporto deve funzionare nella rete disponibile e sarà riprovato dopo il trasferimento domestico. Fonte S214.

Log NAS è il nome concordato per raccogliere avvisi e rapporti di salute nella casella. Cartella o etichetta e filtro Proton saranno impostati dopo avere letto un messaggio reale, usando mittente e un criterio specifico del NAS per non classificare tutta la posta personale. Verificare che il messaggio venga raccolto e che gli avvisi restino visibili; nessuna regola di eliminazione o lettura automatica è prevista. Fonti S215-S216. La conservazione dei log completi e lo studio generale della posta dai server interni sono rinviati, come richiesto: questa preparazione non attiva un server di posta domestico.

Restano RAM-03/A2 da8GB, obiettivo16GB, dati SanDisk da chiarire prima del pool, lettura del boot-pool ed export privato con seed dopo le impostazioni.

## 27/10/2026: localizzazione Europe/Rome e Italian (it) salvata

La prima immagine mostra il pannello Localization Settings con Italian (it), Europe/Rome e salvataggio in corso; da sola non chiudeva la verifica. La successiva mostra il pannello chiuso e i valori nella scheda General Settings: Timezone Europe/Rome, Console Keyboard Map Italian (it), Language English, Date Format27/10/2026 e Time Format11:02:31 a24ore. Salvataggio e applicazione del fuso sono quindi osservati; non si accredita da questo la sincronizzazione NTP. Le due immagini sono archiviate nel livello privato con SHA-256 verificati e originali conservati. Prossimo gesto indicato: Settings del riquadro Email, in basso a destra, per osservare campi e metodo prima di configurare. Email ancora SMTP nel riepilogo, nessun mittente, destinatario o test di recapito osservato. Obiettivo16GB, dati SanDisk prima del pool, boot-pool ed export restano aperti.

## 27/10/2026: GMail OAuth selezionato, login e salvataggio ancora aperti

Il pannello Email Options mostra GMail OAuth selezionato, From Email e From Name vuoti, invito a configurare le credenziali OAuth e pulsante Log In To Gmail. Save e Send Test Mail sono disabilitati; il riepilogo sottostante mostra ancora SMTP. La selezione nel modulo è osservata, mentre autorizzazione, salvataggio e invio non lo sono. Email Recipients non è visibile: la descrizione di S214 resta una guida da confrontare con la GUI effettiva, non la prova di un campo già trovato. Immagine archiviata in privato con SHA-256 verificato, originale conservato. L'utente chiede se cambiando browser e rete il collegamento continuerà e conferma di procedere. Indicato Log In To Gmail, con account e consenso solo nella GUI locale; nessuna password o codice ricevuti.

### Browser, autorizzazione del NAS e rete disponibile

Dopo autorizzazione e salvataggio, TrueNAS conserva il collegamento Gmail nella propria configurazione (S214). Il browser serve al consenso iniziale; l'invio successivo avviene dal NAS. Google documenta il rinnovo dei token senza utente presente, finché l'autorizzazione resta valida (S217). Cambiare browser non richiede per questo un nuovo collegamento Gmail. Spostando il NAS si verifica la connettività in uscita e si riprova la consegna. Per aprire la GUI da un'altra rete occorre anche un percorso verso il NAS: la VPN domestica prevista resta da configurare.

Gmail è il trasporto scelto nel modulo; Proton resta destinatario preferito, Gmail destinazione alternativa. Il cambio di browser non cambia questi ruoli. Configurazione e prove di consegna sono ancora aperte, insieme a filtro Log NAS, boot-pool, export privato e pool dati dopo chiarimento SanDisk. Nessun accesso remoto o servizio di posta domestico è attivato da questo passaggio.

## 27/10/2026: account Google personale dei servizi domestici, ancora da creare

Le due schermate mostrano GMail OAuth selezionato ma ancora da autorizzare, From Email e From Name vuoti, Save e Send Test Mail disabilitati. La prima apre l'help From Email, che cita envelope From e un indirizzo da configurare in Accounts > Users > Edit; la seconda descrive From Name come nome visualizzato del mittente. Sono testi di aiuto osservati, non prova di un account configurato o della posizione attuale del destinatario. Immagini archiviate in privato con SHA-256 verificati, originali conservati.

L'utente chiarisce che non ha una casella Gmail dedicata e propone di creare un normale account Google personale per altre esigenze private della propria rete domestica, riutilizzabile altrove. Raccomandato questo perimetro: un account dei servizi di casa, il cui primo utilizzo sarà l'invio degli avvisi NAS. Correzione operativa rispetto al precedente invito a usare il Gmail personale: il mittente sarà la nuova casella, non il Gmail personale già citato come destinatario alternativo. Nessun nuovo account, indirizzo, consenso, salvataggio o invio è ancora osservato. ADR-042 registra il piano, senza attestare la creazione.

### Che cosa appartiene alla nuova identità

Si crea un normale account Google con Gmail, scegliendo Per uso personale secondo S218. Il ruolo nel progetto è servizi della rete domestica, non un account riservato al solo NAS. Si potrà collegare anche a servizi compatibili con Google/Gmail, valutando per ciascuno le funzioni e i permessi richiesti. La scelta non richiede qui un progetto Google Cloud: i service account IAM descritti in S219 sono identità di workload con un modello diverso dal login Gmail OAuth della GUI TrueNAS. Le connessioni delle applicazioni si gestiscono nell'account Google, S220.

| Elemento | Valore o ruolo previsto | Stato |
|---|---|---|
| account Google servizi casa | `<email-servizi-casa>`, normale account personale con Gmail | creato e OAuth NAS autorizzato; 2FA attiva confermata da dialogo e corpo email; Authenticator, Google prompt e Phone number elencati; recupero email ancora Verify |
| From Email del NAS | `<email-servizi-casa>` autenticata via Gmail OAuth | salvata e confermata dal riepilogo il28/10/2026 |
| From Name del NAS | `<nome-mittente-nas>`, nome visualizzato effettivo nella mappa privata | compilato e salvato; non è un account o una credenziale |
| destinatario degli avvisi | Proton `<email-destinatario-nas>` | salvato nel profilo; prima mail NAS e test del servizio alert inviati e ricevuti su Proton |
| destinatario alternativo | Gmail personale `<email-alternativa-nas>` già indicato dall'utente | nessuna duplicazione o fallback impostati |

Aprire una finestra privata per la registrazione permette di scegliere il nuovo account senza confonderlo con una sessione Google esistente. Seguire la procedura Google in locale; indirizzo reale e dati di recupero restano nel livello privato e password/codici non vengono richiesti in chat. Tornare poi a Log In To Gmail sul NAS e selezionare il nuovo account. Una volta salvato il collegamento, browser e rete di amministrazione non ne cambiano l'identità; restano le verifiche di connettività e consegna già registrate.

Le eventuali integrazioni dell'account con altri dispositivi non sono ancora adottate o configurate. Lo studio generale della posta dai server interni e la raccolta dei log completi restano rimandati. Una sola identità dei servizi domestici riduce gli account da mantenere, ma concentra in quell'account le autorizzazioni future: ciascuna nuova integrazione avrà il proprio perimetro da valutare.

## 27/10/2026: registrazione Google avviata, nuova Gmail ancora da scegliere

Le tre schermate mostrano inserimento del nome, informazioni di base e pagina Use an email address or phone number con campo vuoto. Il collegamento visibile Don't have an email address or phone number? è il prossimo gesto indicato per proseguire verso una nuova casella Gmail. Nessun indirizzo scelto, account completato o collegamento al NAS è ancora osservato. Dati anagrafici non trascritti nei documenti pubblici; indicato di verificare la correttezza della data del titolare. Le immagini sono archiviate nel livello privato con SHA-256 verificati e originali conservati.

S221 distingue account Google e Gmail: la registrazione può anche usare un indirizzo esterno o un numero, senza creare per questo la nuova casella Gmail prevista come mittente. Il piano di ADR-042 resta un account personale dei servizi domestici con Gmail; Proton resta destinatario degli avvisi. Selezione e completamento del nuovo indirizzo, autenticazione OAuth, salvataggio e recapito restano pendenti.

## 27/10/2026: indirizzo servizi casa scelto e riepilogo Google dopo il QR

L'utente comunica l'indirizzo scelto per `<email-servizi-casa>` e la prima immagine mostra Verify some info before creating an account: Google chiede una verifica del dispositivo o numero contro gli abusi, con QR da scansionare dal telefono, passaggi sul telefono ed eventuale invio di un codice a Google, poi ritorno al PC. Indicato di lasciare aperta la pagina; QR conservato solo nella foto privata, non decodificato o pubblicato. La richiesta è coerente con S222, senza accreditare un'attivazione della verifica in due passaggi.

Le quattro immagini successive mostrano Add recovery email con il precedente Gmail personale compilato, Add phone number con campo vuoto, Add a recovery contact con lo stesso Gmail personale compilato e infine Review your account info con la nuova casella e pulsante Next. Il flusso ha quindi superato il ramo QR ed è al riepilogo; non è ancora osservato un accesso alla casella o al profilo dopo il completamento. Nessun numero di telefono è stato ricevuto; dal campo vuoto non si conclude che un numero sia stato aggiunto o saltato nei passi successivi. Nessun invito di recupero accettato o impostazione confermata nelle impostazioni finali.

Cinque immagini archiviate e verificate SHA-256, originali conservati. Indirizzo reale registrato prima nel livello privato e nei pattern di blocco; nel pubblico resta il segnaposto. Prossimo gesto indicato Next sul riepilogo, poi lettura della schermata seguente. Nessun login OAuth NAS, salvataggio del metodo o invio email osservato.

### Verifica di creazione, recupero e destinatario degli avvisi

La verifica antiabuso permette di proseguire la registrazione. L'email di recupero aiuta a riottenere l'account e può ricevere avvisi di sicurezza, S224. Il contatto di recupero è un meccanismo distinto: il suo account riceve un invito da accettare e la guida prevede una successiva attesa prima dell'uso, S223. La semplice compilazione dei campi non ne dimostra l'attivazione. Qui non sono ancora state verificate le impostazioni finali né un'eventuale accettazione.

Il precedente Gmail personale può comparire nel recupero della nuova identità senza diventare il mittente del NAS. Il mittente previsto resta `<email-servizi-casa>` e Proton `<email-destinatario-nas>` resta destinatario degli avvisi, ADR-041/042. Anche la verifica in due passaggi dell'account è una proprietà da verificare separatamente: il QR della registrazione non è una prova della sua attivazione. Non si cambia il progetto del NAS per completare queste schermate. Dopo creazione restano collegamento OAuth, salvataggio, destinatario effettivo, test posta/alert e filtro Log NAS.

## 27/10/2026: account Google dei servizi casa creato e protezione ancora da verificare

Le nove schermate documentano la scelta delle preferenze in quattro passi: attività web/app non salvata, cronologia YouTube non salvata, annunci generici selezionati dopo una prima vista senza selezione, promemoria privacy selezionati. Il riepilogo riporta attività e personalizzazione off e promemoria attivi. Seguono la pagina delle condizioni con I agree e infine la Home Google Account autenticata della nuova identità `<email-servizi-casa>`. La creazione è quindi osservata dalla pagina successiva al consenso, senza presumere il click dal solo pulsante. Le opzioni descritte sono quelle selezionate e riepilogate nel flusso; non è stata eseguita una nuova visita separata a ogni controllo dati dopo la creazione.

La Home invita ad aggiungere una seconda opzione di recupero con telefono. Il banner non dimostra lo stato di ogni metodo di accesso, del recupero o della verifica in due passaggi. Non sono ancora state aperte le impostazioni Security & sign-in: nessuna autenticazione a due fattori, passkey, app autenticatore o codice di backup viene dichiarato configurato da queste immagini. Email e contatto di recupero erano stati inseriti nel flusso precedente; conferma e stato dell'invito restano da verificare. Nove copie archiviate con SHA-256 verificati, originali conservati, dati identificanti nel solo livello privato.

Alla domanda sugli ulteriori settaggi, raccomandato un passaggio essenziale: leggere Security & sign-in, proteggere l'accesso con verifica in due passaggi e conservare i codici di backup in privato (S225-S226). La guida ammette app autenticatore e altri metodi; il metodo effettivo dipenderà dalle opzioni disponibili all'utente. Non si aggiungono servizi Google, nuovi account o una serie di controlli sulla personalizzazione già scelta. La raccomandazione non è un prerequisito tecnico di Gmail OAuth. Prossimo gesto aprire Security & sign-in, poi collegamento NAS.

### Privacy del profilo, protezione dell'accesso e invio automatico

Le preferenze su cronologie e annunci gestiscono la personalizzazione. La verifica in due passaggi protegge invece l'accesso all'account; i codici di backup aiutano quando il secondo passaggio normale non è disponibile, S225-S226. I codici devono essere conservati dal proprietario senza essere trasmessi in chat o registrati nel repository. Il QR iniziale della creazione non sostituisce questa verifica dello stato.

L'account ora esiste, mentre il NAS non è ancora autorizzato a usarlo. La prossima configurazione TrueNAS richiederà il consenso del nuovo account, salvataggio e verifica del destinatario effettivo prima della prova di ricezione, S214. L'avvio di una casella o la sola Home Google non prova la consegna delle notifiche. Il mittente resta la nuova identità dei servizi casa e Proton il destinatario; gli altri usi dell'account rimangono da valutare quando richiesti.

## 27/10/2026: Authenticator aggiunto, pulsante finale2FA e codici di backup rinviati

L'utente riferisce di avere impostato Google Authenticator e chiede perché sia ancora presente Turn on 2-Step Verification, chiedendo di proseguire e chiarendo di non capire quali siano i codici proposti. Le due schermate confermano Authenticator Added just now, messaggio Authenticator app has been set up e successiva riga verde Added1minuteago. Mostrano anche l'invito ad attivare2FA e il pulsante Turn on 2-Step Verification in basso. Metodo configurato e attivazione globale sono quindi stati separati: nessuna conferma2FA attiva è ancora osservata.

Indicato il solo pulsante finale, senza rifare il setup dell'app o richiedere un nuovo test di logout. I codici di backup di S226 sono spiegati come codici di scorta per accedere se perde il telefono; vengono rinviati per rispettare la richiesta di avanzare e non sono una condizione del collegamento NAS. La pendenza resta esplicita, non viene marcata completata. Dopo la conferma di attivazione si torna al NAS per Gmail OAuth. Nessun codice o QR segreto ricevuto. Le due immagini sono archiviate e verificate SHA-256, originali conservati. Fonti S225-S226 già consultate; nessun nuovo servizio o metodo aggiunto dall'agente.

## 27/10/2026: il clic2FA richiede un metodo aggiuntivo, Authenticator resta registrato

La nuova schermata mostra il dialogo Add second steps to your account: per attivare2-Step Verification chiede di aggiungere metodi come numero di telefono o passkey, con solo pulsante Go back. Sullo sfondo Authenticator resta con spunta verde e Added1minuteago. L'utente osserva correttamente che Authenticator è già un secondo fattore. Il metodo esiste, ma questo tentativo non ha attivato la protezione globale. Immagine archiviata in privato e verificata SHA-256, originale conservato; nessun numero di telefono o codice ricevuto.

Rettifica del passo precedente: indicare soltanto l'ultimo clic era un'aspettativa troppo ottimistica, smentita dal dialogo osservato. Il messaggio richiede un metodo ulteriore senza spiegarne la causa. Non si inventa un requisito universale di due metodi, non si dichiara un bug e non si rifà Authenticator. Proposto Go back, poi Phone number per seguire una delle opzioni indicate; dati e verifica si inseriscono soltanto sul sito Google. Il risultato di questo eventuale inserimento non è ancora osservato e non viene garantito. La passkey è l'altra opzione nominata dal dialogo, non configurata.

S225 descrive i metodi e l'attivazione generale. S227 è un annuncio ufficiale del6/5/2024, applicabile anche agli account personali, che distingue l'aggiunta dei metodi dall'attivazione2SV: contesto per la separazione degli stati, non diagnosi del messaggio di questo account nel2026. Il risultato osservato nella GUI guida il passo corrente. Codici di backup già rinviati; Gmail OAuth NAS non dipende tecnicamente da2FA e nessuna nuova checklist viene imposta.

## 27/10/2026: verifica identità Google rifiutata nel nuovo profilo, completamento2FA richiesto ora

La prima immagine mostra We couldn't verify it's you durante il percorso di modifica della sicurezza dell'account servizi casa. La pagina suggerisce dispositivo/browser già usati e rete familiare, senza indicare causa o scadenza. L'utente riferisce poi un nuovo accesso in Chrome; la seconda immagine mostra Google Home con avatar, senza indirizzo completo. La terza mostra lo stesso rifiuto e il menu del profilo Chrome con l'indirizzo dell'account corretto, coincidente con quello della pagina Google. Il cambio di sessione non ha quindi risolto il rifiuto della verifica. Il pulsante Attiva nel menu Chrome riguarda la sincronizzazione di cronologia e schede, non l'attivazione2FA.

Tre copie archiviate e verificate SHA-256, originali conservati. I parametri di sessione visibili nell'URL restano nella sola foto privata e non vengono estratti. Nessun numero di telefono, codice o nuova conferma di metodo acquisiti. Authenticator è già stato aggiunto; una conferma2FA attiva non è osservata.

L'agente aveva proposto di rimandare l'attivazione e tornare al NAS; l'utente richiede esplicitamente di completare2FA adesso. Tale richiesta supera il rinvio: il passo corrente resta la protezione dell'account, non il collegamento NAS. Indicato il percorso ufficiale di S228: accedere al nuovo account nell'app Google o Gmail sul telefono, poi Gestisci account Google, Sicurezza e accesso, Verifica in due passaggi. Il risultato del percorso mobile non è ancora osservato. Non si rifà Authenticator, non si moltiplicano browser o metodi e non si promette che il nuovo accesso risolva il controllo. Codici di backup già rinviati, nessuna nuova richiesta di generarli.

### Login riuscito e azione sensibile consentita sono verifiche distinte

S228 include l'attivazione della verifica in due passaggi fra le azioni sensibili. Google può richiedere un dispositivo o metodo associato da almeno7giorni e può limitare tali azioni per7giorni quando non riesce a verificare l'identità, lasciando possibile l'uso ordinario dell'account. La guida propone anche accesso da app Google o Gmail su un dispositivo mobile e attesa prima del nuovo tentativo. Questo spiega perché accesso al profilo e modifica consentita non siano equivalenti.

Il comportamento è compatibile con restrizioni sui metodi o dispositivi recenti, ma la causa del caso specifico e l'inizio di un eventuale periodo di attesa non sono mostrati. Non si fissa una data di sblocco né si dichiara l'account perso, disabilitato o la2FA completata. L'esito da ottenere resta la pagina Google che conferma2FA attiva. Se il fornitore continua a rifiutare la verifica, il limite va comunicato come tale, senza inventare una correzione locale o cancellare la pendenza. Il collegamento OAuth NAS resta distinto e non ancora eseguito.

## 27/10/2026: account servizi casa aggiunto al telefono, prossimo stato2FA

L'utente conferma di avere aggiunto l'account dei servizi domestici al proprio telefono e chiede come proseguire. Riscontro dichiarato, senza nuova immagine; non si deduce che il controllo identità sia già superato o che2FA sia attiva. Indicato di selezionare il nuovo account nell'app Google o Gmail e aprire Gestisci il tuo Account Google, Sicurezza e accesso, Verifica in due passaggi; premere Attiva se presente e seguire la richiesta del fornitore. La conferma che chiude questa fase è Verifica in due passaggi attiva. Nessun codice, password, QR o numero richiesto in chat. Non si rifà l'aggiunta al telefono o il setup Authenticator. L'utente vuole completare questa fase ora; codici di backup ancora rinviati e OAuth NAS non ancora eseguito. Procedura coerente con S225 e S228 già consultate.

## 27/10/2026: percorso dalle Impostazioni Google sul Samsung S25 Ultra

L'utente identifica il telefono come Samsung Galaxy S25 Ultra e chiede dove proseguire. L'account è già stato aggiunto secondo la sua dichiarazione; non si richiede di aggiungerlo nuovamente. Indicato il percorso dalle impostazioni del telefono: Impostazioni, Google, foto o iniziale dell'account in alto, selezione del nuovo account servizi casa, Gestisci il tuo Account Google, Sicurezza e accesso, Verifica in due passaggi. Se Google non è visibile nell'elenco, usare la ricerca delle Impostazioni per trovare la voce. Fonte generale Android S229, insieme a S225 per2FA; nessuna versione One UI o disposizione concreta della pagina viene dedotta senza una schermata.

Attiva va premuto se disponibile nella pagina2FA. L'esito non è ancora ricevuto e l'aggiunta al telefono non chiude questa fase: il criterio resta Verifica in due passaggi attiva. L'utente vuole completare la protezione ora, backup codes già rinviati, nessuna nuova configurazione Authenticator o tentativo da altro browser. Il modello del telefono è contesto per questa guida, non un censimento completo del dispositivo.

## 27/10/2026: telefono di recupero confermato e passkey presente,2FA globale ancora da leggere

La prima immagine dal Samsung mostra Confirm your recovery phone con il numero e le opzioni Yes confirm e No update. La seconda mostra il messaggio Recovery phone confirmed. Sono inoltre visibili una passkey etichettata Galaxy S25 Ultra, Last used Not yet used e This passkey is not syncable, una barra chiusa2 verification methods e le sezioni Safe Browsing, Your devices e Recent security activity. Non si è osservata la creazione della passkey: si registra la sua presenza. Non compare una dicitura esplicita di attivazione2-Step Verification. L'email completa non è visibile nelle due immagini, solo l'avatar coerente con il percorso seguito.

Il numero viene registrato prima nella mappa privata e nei pattern di blocco come `<tel-recupero-google>`, senza pubblicare valori o parametri identificanti. Due immagini archiviate e verificate SHA-256, originali conservati. Prossimo solo espandere2 verification methods, barra grigia sotto Continue, e leggere il contenuto. Non si prescrivono un'altra passkey, sincronizzazione Chrome o Enhanced Safe Browsing. La conferma del recupero e il conteggio dei metodi non vengono trasformati in2FA globale attiva; l'utente vuole completare questa fase ora, codici di backup rinviati e OAuth NAS non ancora eseguito.

## 28/10/2026: Gmail OAuth salvato, test senza destinatario amministrativo e Google2FA off

L’utente fornisce dodici nuove immagini e ribadisce che ogni passaggio deve essere registrato per poter riprendere il lavoro. Tutte le immagini nominate sono state lette e copiate nell’archivio privato, con SHA-256 confrontato con l’originale e manifest per immagine; gli originali sono conservati. Timestamp e numerazione non vengono assunti come sequenza esatta dei clic: si registrano gli stati visibili.

Nel modulo Email Options sono compilati From Email `<email-servizi-casa>` e From Name `<nome-mittente-nas>`. Il popup TrueNAS Authorization presenta Proceed; segue la scelta della nuova identità Google e la parte finale della pagina di consenso con Continue. Gli scope completi non sono visibili e non vengono inventariati per ipotesi. La schermata successiva conferma Gmail credentials have been applied e Logged In To Gmail. Un tentativo di test produce l’avviso che nessuna email è configurata per root o altro amministratore locale e chiede di configurarla prima. Infine Email settings updated e il riepilogo GMail OAuth con mittente confermano il salvataggio. OAuth e campi mittente sono quindi configurati; nessuna consegna NAS è provata.

Sul telefono Google notifica che TrueNAS ha ricevuto accesso e una copia dell’avviso compare nella Gmail personale indicata come email di recupero. Security & sign-in elenca l’evento di concessione e TrueNAS tra le applicazioni collegate. Questi sono riscontri Google del consenso, non messaggi di test inviati dal NAS. La stessa pagina mostra2-Step Verification is off, Authenticator Added Oct27, Google prompt1device, il recapito telefonico già censito e Recovery email con Verify arancione. La ricezione della copia dell’avviso non cancella quel Verify. Skip password when possible è On ed Enhanced Safe Browsing è Off: si registrano senza cambiarli. La passkey era visibile il27/10; il suo inventario non viene aperto ora e non si deduce né rimozione né creazione dalla voce del menu.

Prossimo sul telefono: dalla pagina Security & sign-in risalire a How you sign in to Google e toccare2-Step Verification, la riga con is off, poi leggere la schermata successiva. L’attivazione resta richiesta ora, i codici backup restano rinviati. Dopo2FA, verificare l’email dell’amministratore locale nel percorso utenti della GUI e impostare il destinatario Proton prima del nuovo test; nessuna modifica a utenti già eseguita. La discrepanza tra Email Recipients nella guida S214 e l’avviso effettivo rimane esplicita. S214 e S225 rilette il28/10; percorso di consenso coerente con la guida, stato reale sempre dedotto dalla GUI.

Riprendibilità e ripristino restano diversi: registro, memoria, checkpoint privato e fotografie ricostruiscono lo stato e i prossimi passi. Per un ripristino della configurazione TrueNAS serve ancora l’export con Password Secret Seed previsto da S137/S158 e la sua custodia privata; nessun file di backup o prova di restore viene dichiarato esistente. Non si propone di rifare OAuth già salvato. Password, token e codici restano in possesso dell’utente e non vengono estratti dalle immagini.

## 28/10/2026: verifica in due passaggi attiva, email di conferma e indice privato dei messaggi

Quattro nuove immagini documentano la pagina2-Step Verification con Turn on, Google prompt su un dispositivo, Authenticator già aggiunto e Phone number con spunta verde; è elencata anche una passkey con indicatore giallo, del quale non si inventa la causa. Segue Turning on, poi You’re now protected with 2-Step Verification con pulsante Done. L’ultima immagine mostra il corpo dell’email Google2-Step Verification turned on per l’account servizi casa. L’attivazione è quindi confermata e la relativa pendenza è chiusa, senza richiedere di rifare metodi o nuovi test di accesso. I codici di backup restano rinviati. Quattro copie archiviate e verificate SHA-256, originali conservati.

L’utente richiede di annotare anche quando arrivano le email per poterle ritrovare. Creato un indice privato per evento e casella: per ciascuna evidenza separa ora nel display della notifica, ora dell’orologio del telefono mentre il messaggio è aperto, data di osservazione e ora esatta dell’header, quando visibile. Nell’email finale l’header è fuori inquadratura: il titolo del corpo non viene chiamato oggetto verificato e l’ora di lettura non viene chiamata ricezione. Inclusa retroattivamente la notifica Gmail della copia dell’avviso OAuth già osservata nel lotto precedente, senza accreditarla come email NAS. Date e orari di sistema della registrazione vengono dalla macchina.

Prossimo sul PC TrueNAS: aprire Credentials > Users e leggere la schermata dell’account locale prima di intervenire sull’email richiesta dal test. Fonte S230 consultata per il percorso utenti; anche questa guida parla di destinatari separati da25.10, quindi non risolve per ipotesi la discrepanza della GUI. OAuth e mittente restano già salvati, recapito Proton e mail NAS ricevuta ancora non provati. Google2FA è una protezione dell’identità Google, non un’attivazione2FA della GUI NAS. Verifica email di recupero, filtro Log NAS ed export configurazione con seed rimangono aperti.

## 28/10/2026: pagina Users osservata e motivazione TrueNAS rispetto a OMV riallineata

La pagina Users mostra due utenti: root, Built-In Full Admin, e truenas_admin, Local Administrator e Full Admin. È selezionato root; i dettagli mostrano No Password, No SMB Access, No API Keys, No SSH Access e shell /usr/bin/zsh. Il pulsante Edit è in alto a destra. Nessun campo email è aperto e nessuna modifica è dimostrata. Immagine archiviata nel livello privato con SHA-256 verificato, originale conservato. Prossimo selezionare truenas_admin, seconda riga, poi Edit e leggere il modulo; nessuna modifica della password di root. Non sono osservate nuove email e il registro privato degli orari non riceve eventi inventati.

L’utente chiede inoltre di capire e documentare perché TrueNAS rispetto a OMV. Il confronto08 è riscritto sui requisiti correnti e la sezione tecnologia dello studio03 corretta; ADR-026 è mantenuto storico e chiarito alla luce di ADR-033/039. Il vantaggio attuale è una preferenza per l’integrazione ZFS, non avvio in specchio ormai assente,32GB o proprietà negate al plugin OMV. Fonti primarie consultate, correzione Btrfs, costi e condizioni di rivalutazione espliciti. Documento tecnico, matrice, memoria e didattica aggiornati senza cambiare la configurazione NAS.

## 28/10/2026: Edit User aperto, campo Email dell’amministratore Not Set

La schermata mostra selezionato truenas_admin e il pannello Edit User aperto. In Additional Details la riga Email riporta Not Set con una matita; Save è visibile in basso. Il campo dell’indirizzo amministrativo è quindi individuato e la sua assenza osservata direttamente. Nessun indirizzo inserito o salvataggio è ancora dimostrato. Immagine archiviata in privato con SHA-256 confrontato con l’originale, conservato. Non è mostrato un nuovo messaggio email: nessun orario di ricezione viene aggiunto al registro.

Prossimo: nella riga Email, sotto Additional Details del pannello destro, cliccare la matita accanto a Not Set, inserire Proton `<email-destinatario-nas>` e salvare con Save in basso. Password e permessi rimangono invariati; nessun nuovo utente richiesto. La casella Gmail `<email-servizi-casa>` resta il mittente OAuth già salvato. Email dell’account locale e identità del provider hanno ruoli distinti; dopo il salvataggio va ancora provata la ricezione reale di un messaggio NAS. S230 resta la fonte del percorso utenti, mentre la GUI effettiva identifica il controllo da usare.

## 28/10/2026: recapito Proton riscontrato nel Profile dell’amministratore

L’utente conferma fatto. La nuova schermata mostra `<email-destinatario-nas>` sia nella riga Email del pannello Edit User di truenas_admin sia nel riquadro Profile sottostante. Il recapito non è quindi soltanto testo nel campo di modifica: il riepilogo del profilo lo riporta dopo l’azione dichiarata. Salvataggio riscontrato; nessun toast di successo è inquadrato. Il pannello di modifica resta aperto. Immagine archiviata in privato, SHA-256 confrontato con l’originale e originale conservato. Nessun nuovo test o messaggio ricevuto sono mostrati: nessun orario email aggiunto al registro.

Prossimo chiudere Edit User con la X in alto a destra, aprire System > General Settings, scegliere Settings nel riquadro Email e premere Send Test Mail. Leggere il risultato e controllare Proton; se arriva il messaggio, registrarne nel privato casella, mittente, oggetto e ora effettivamente visibili nell’header, distinguendoli dal momento della lettura. L’ora Method Call nel profilo è un evento della GUI, non una ricezione email. Gmail OAuth e Google2FA restano già acquisiti; nessuna nuova autorizzazione o modifica a password e permessi richiesta. Il servizio alert e il filtro Log NAS restano prove separate.

## 28/10/2026: prima mail NAS ricevuta su Proton e backup delle personalizzazioni richiesto

Quattro immagini mostrano Email Options con Gmail OAuth già autenticato, l’attività mail.send, Test email sent e il messaggio di prova aperto in Proton. L’utente conferma l’arrivo. Mittente visualizzato `<nome-mittente-nas>`, indirizzo coerente con il mittente configurato ma abbreviato nella vista mobile, corpo di prova TrueNAS Community Edition. Prima consegna NAS verificata, distinta dagli avvisi Google dei lotti precedenti. L’app e la notifica mostrano12:25, l’orologio del telefono12:26; data28/10 ricavata dal contesto della sessione e delle immagini, secondi e fuso non visibili. Oggetto completo e indirizzi sono solo nel registro email privato. Quattro copie archiviate, SHA-256 confrontati con gli originali, conservati.

L’utente richiede che anche le impostazioni sopravvivano a guasto o cambio hardware: ADR-043, documento backup10 e scheda didattica06. Primo export con seed ancora da acquisire; prossimo chiudere Email Options, System > Advanced Settings > Manage Configuration > Download File, selezionare Export Password Secret Seed e Save. Solo quando esiste il file, registrare versione, data, dimensioni, impronta e copie esterne; nessun export vuoto o ripristino già provato viene inventato. Fonti S137 e S158 rilette; S238 per il legame fra hardware e nomi rete.

Il pacchetto veeam-linux del template è stato ritrovato e letto, S237. Documenta il backup a livello di file e la rilettura su una macchina Linux, con limiti dichiarati sull’esecuzione degli script e sul recupero avviabile. Non si richiedono di nuovo i materiali; si riusa il percorso distinguendo prova precedente e protezione effettiva di questo NAS, che non è ancora acquisita. Nessun nuovo software installato. Test del servizio alert e filtro Log NAS restano aperti.

## 28/10/2026: primo export configurazione con seed acquisito e verificato fuori NAS

L’utente fornisce il percorso dell’export nativo. File849920byte copiato nell’archivio privato del PC, originale conservato, SHA-256 confrontato fra sorgente e copia e corrispondente. Archivio leggibile con freenas-v1.db da835584byte e pwenc_secret da32byte. Database letto in memoria, senza estrazione dei segreti in file intermedi, quick_check restituisce ok. Confronti booleani confermano mittente servizi casa, nome visualizzato, configurazione OAuth non vuota, destinatario Proton dell’amministratore e Europe/Rome; nessun valore segreto è stampato. Percorso, impronta, orari e manifest sono soltanto nel livello privato, file verificato ignorato da git.

Primo backup della configurazione fuori NAS acquisito e verificato per la tappa localizzazione/account/OAuth/recapito/prima mail ricevuta. La verifica di struttura e dei campi non è un’importazione su un’altra installazione e la presenza del campo OAuth non prova la validità futura del consenso. Download e copia sono sul medesimo PC; seconda destinazione indipendente, protezione nel lavoro Veeam e ripristino restano aperti. Nessun dato dei dataset incluso e nessun pool dati ancora creato. Nessuna nuova email mostrata, indice ricezioni invariato.

Prossimo nel NAS aprire System > Alert Settings e leggere la configurazione del servizio Email per verificare anche gli avvisi automatici, distinti dalla mail di test già riuscita. Il prossimo checkpoint di configurazione va riesportato dopo le relative modifiche; non si riscarica inutilmente la stessa tappa. Restano filtro Log NAS, boot-pool,16GB, dati SanDisk e verifica email recupero; codici Google backup rinviati.

## 28/10/2026: Alert Settings aperto, E-Mail già abilitato al livello Warning

Le due immagini mostrano System > Alert Settings. La tabella Alert Services contiene SNMP Trap ed E-Mail, entrambi con livello Warning ed Enabled Yes. Nella seconda riga E-Mail sono visibili matita di modifica e cestino all’estremità destra. Il destinatario e il pannello del servizio non sono ancora aperti. Non viene creato un nuovo servizio né dichiarata già riuscita la sua prova. La presenza del servizio di notifica SNMP Trap non dimostra che il demone SNMP di sistema sia in esecuzione e non viene modificata.

Sotto la tabella la categoria Applications mostra nomi di tipi di evento, livelli e frequenze impostabili; non è una lista di errori effettivamente in corso. Nessun evento applicativo viene diagnosticato da quelle etichette. Due immagini lette, archiviate e verificate SHA-256, originali conservati. Nessuna nuova email ricevuta mostrata: indice privato degli orari invariato.

Prossimo nella tabella Alert Services in alto cliccare la matita sulla seconda riga E-Mail, immediatamente prima del cestino, poi leggere destinatario e comando di test. Il primo test posta e il primo export con seed restano acquisiti; questa sola lettura non richiede un nuovo export, che si aggiornerà dopo eventuali modifiche effettive. Destinatario/test alert e filtro Log NAS restano distinti e aperti.

## 28/10/2026: override email vuoto, prossimo test del servizio alert

Edit Alert Service mostra Name E-Mail, Enabled selezionato, Type E-Mail, Level Warning e il campo Override Admin Email vuoto. Sono presenti Save e Send Test Alert. La guida ufficiale25.10 S239 conferma che il campo vuoto usa l’email dell’amministratore: nel caso locale Proton è già salvato nel Profile. Non si duplica l’indirizzo nell’override e non si crea un nuovo servizio. Il livello Warning comprende quella gravità e quelle superiori secondo la stessa fonte, senza cambiare i livelli delle categorie.

Prossimo lasciare invariati i valori e premere Send Test Alert, pulsante grigio a destra di Save. Leggere il risultato e la ricezione su Proton; eventuale nuova email va aggiunta al registro privato con mittente, oggetto e orario effettivamente visibile. Nessun test alert, modifica o nuova email sono ancora osservati. La prima mail di test trasporto e il primo export con seed restano acquisiti; una lettura e una prova senza cambi di configurazione non richiedono un altro export della stessa tappa. Immagine letta, archiviata e verificata SHA-256, originale conservato.

## 28/10/2026: test alert inviato e ricevuto su Proton, prossimo controllo boot-pool

La schermata TrueNAS mostra Test alert sent nel pannello Edit Alert Service con Name/Type E-Mail, Enabled selezionato, Warning e override vuoto invariati. La schermata mobile mostra in Proton il messaggio del servizio con corpo This is a test alert, mittente visualizzato `<nome-mittente-nas>` e indirizzo abbreviato coerente con il mittente configurato. L’oggetto completo è nel registro privato. Messaggio e notifica mostrano1:01PM, registrato come13:01; telefono1:01, data28/10dal contesto e dai file osservati, secondi/fuso non visibili. L’ora di registrazione del riscontro è distinta dall’ora email. Test sintetico invio/ricezione del servizio alert concluso, senza attribuire un guasto reale o cambiarne i livelli. Le due immagini sono state lette; al momento della copia gli originali non risultano più disponibili. Cercate copie nelle cartelle di cattura/download/desktop, nell’archivio privato e nel Cestino, senza recupero. Nessuna copia o impronta delle due immagini viene accreditata: il manifest conserva descrizione e lacuna dell’archivio.

Aggiornato EMAIL-004 nel registro privato, distinto dal Test Message precedente delle12:25. Nessuna modifica di configurazione osservata: il primo export con seed rimane il checkpoint acquisito, senza richiesta di un altro download per il solo test. Non si riaprono OAuth o Google2FA.

Prossimo chiudere il pannello con la X in alto a destra e aprire System > Boot per leggere la schermata. S212 riletto per Stats/Settings e Boot Pool Status: si osserveranno condizione, dispositivi e contatori prima di interpretarli. Non sono ancora letti ONLINE o errori zero e non viene assegnato uno scrub o un ulteriore test di memoria. Filtro Log NAS mantenuto aperto; seconda copia indipendente/restore,16GB, dati SanDisk ed email recupero restano distinti.

## 28/10/2026: Boot Environments aperto,25.10.7 attivo

La nuova schermata mostra Boot Environments con una sola voce25.10.7, Active Now, Date Created2026-10-27 11:00:07, Used Space3.42GiB e Keep No. Data e ora sono quelle visualizzate dalla GUI; non vengono trasformate in un evento di reinstallazione o di backup. Lo spazio è riferito alla voce ambiente, non alla capacità complessiva del Kingston o del pool. In alto sono visibili Stats/Settings, Boot Pool Status e Scrub Boot Pool. Non compare ancora la condizione del boot-pool né il dispositivo o i contatori di lettura/scrittura/checksum.

L’immagine è copiata e verificata SHA-256 prima della lettura visiva e dell’aggiornamento documentale, originale conservato. Il manifest registra questa sequenza per evitare una nuova perdita degli originali durante l’elaborazione. La lacuna delle due immagini precedenti rimane distinta e non viene chiusa da questa nuova copia. Nessuna email o modifica di configurazione osservate; il checkpoint nativo già acquisito rimane quello della tappa corrente.

Prossimo cliccare Boot Pool Status in alto a destra, pulsante centrale fra Stats/Settings e Scrub Boot Pool, e leggere la pagina. Non si avvia uno scrub né si modificano Keep, ambiente di avvio o firmware. Il controllo è una lettura dello stato attuale, non un nuovo ciclo di prove RAM.

## 28/10/2026: boot-pool ONLINE, dati dei due SSD dichiarati già salvati

Boot Pool Status mostra boot-pool e il membro sdb3 entrambi ONLINE, ciascuno con Read0, Write0, Checksum0 e No Errors. La lettura dello stato corrente del pool di avvio è conclusa. Il nome del membro è quello della sessione osservata: non sostituisce l’identificazione per modello e ruolo, dato che le lettere dei dischi erano diverse durante l’installazione. Questi contatori non sono un nuovo test SMART né una verifica del ripristino. Il precedente dialogo Start the scrub now aveva Confirm non selezionato e Start Scrub disabilitato; non si accredita uno scrub avviato o concluso. L’ultima schermata mostra soltanto il menu Replace/Attach aperto, senza selezione.

Alla domanda esplicita sui dati di SanDisk240GB e WD Blue250GB, l’utente risponde: «Ho già salvato ciò che serve e quei dati non mi occorrono più». La questione conservazione del vecchio contenuto è chiusa per entrambi sulla base di questa dichiarazione. Non viene dedotto un collaudo delle copie né viene riaperta la stessa domanda. Si prosegue verso il pool dati in specchio sui due SSD previsti da ADR-033; il Kingston resta il disco di avvio da escludere. Nessun pool dati creato e nessuna cancellazione osservati.

Tre immagini archiviate e verificate SHA-256 prima della lettura visiva, originali conservati alla copia. Nessuna nuova email o modifica di configurazione osservata: registro email invariato e primo export con seed ancora valido per la tappa acquisita. Dopo la creazione effettiva del pool servirà una nuova generazione dell’export, conservando la precedente. La lacuna delle due vecchie immagini alert rimane dichiarata.

Prossimo cliccare in uno spazio vuoto per chiudere Replace/Attach, quindi Storage nella barra sinistra, seconda voce sotto Dashboard, e leggere la pagina per l’identificazione dei dischi. Non vengono assegnati altri scrub o test RAM. Fonte S212 per il pannello di stato; S240 consultata per il successivo wizard con selezione manuale dei dischi, mirror e riepilogo finale, ancora non eseguito.

## 28/10/2026: Storage Dashboard aperto, No Pools

La pagina Storage Dashboard mostra No Pools, il pulsante Create Pool al centro e Import Pool e Disks in alto a destra. Il menu del membro di avvio non è più aperto. L’assenza osservata riguarda i pool dati della dashboard, senza contraddire il boot-pool già letto ONLINE con contatori0. L’elenco con modelli e capacità dei dischi non è ancora aperto. Nessuna creazione, importazione, cancellazione o modifica di configurazione osservata.

La nuova immagine è archiviata e verificata SHA-256 prima della lettura visiva, originale conservato alla copia. Non contiene una nuova email; il registro degli orari resta invariato. Primo export con seed già acquisito; una nuova generazione sarà necessaria dopo le modifiche effettive.

Prossimo cliccare Disks in alto a destra, immediatamente a destra di Import Pool, e leggere l’elenco. SanDisk240GB e WD Blue250GB restano i due SSD del mirror dati previsto; il Kingston V300 di avvio va escluso. La dichiarazione dell’utente sui dati già salvati e non più necessari è acquisita per entrambi e non si richiede di nuovo. Pool dati, seconda copia indipendente della configurazione e ripristino restano da eseguire; nessun nuovo test RAM o scrub assegnato.

## 28/10/2026: Disks letto, identificati i due SSD dati

La pagina Disks mostra tre righe: sdc223.57GiB con Pool N/A, sdb223.57GiB con boot-pool e sda232.89GiB con Pool N/A. Nessuna casella di selezione è spuntata. I seriali di sdc e sda corrispondono ai dischi già censiti nella guida privata: rispettivamente SanDisk SDSSDA240G e WD Blue WDS250G1B0A-00H9H0. sdb è esplicitamente assegnato a boot-pool e coincide con il ruolo del Kingston su cui è già stata verificata l’installazione. I modelli non sono una lettura delle colonne di questa schermata; provengono dal collegamento con il censimento. Seriale completo e mappatura restano nel livello privato.

L’identificazione dei due candidati del mirror dati è conclusa per la sessione attuale; le lettere non diventano identità permanenti. Le capacità sono quelle mostrate dalla GUI, non una misura dello spazio utilizzabile del futuro mirror. La stessa capacità di sdc e sdb rende insufficiente distinguere i dischi solo dalla taglia: servono seriale e appartenenza al pool. Nessun pool dati creato, importato o disco cancellato. La conferma dell’utente sui dati già salvati e non più necessari di SanDisk e WD resta acquisita.

Immagine archiviata e verificata SHA-256 prima della lettura, originale conservato alla copia. Nessuna nuova email o modifica di configurazione osservata; export con seed precedente conservato, nuova generazione dopo la modifica effettiva.

Prossimo cliccare Storage, collegamento blu sopra il titolo Disks, quindi Create Pool al centro della dashboard per aprire la prima pagina del wizard. La configurazione prevista resta un solo VDEV dati Mirror con SanDisk e WD; il disco sdb di boot resta escluso. Aprire il wizard non equivale ad aver creato il pool; selezioni e riepilogo andranno letti nelle schermate successive, secondo S240.

## 28/10/2026: wizard tank, Mirror e primo VDEV ancora vuoto

La sequenza osservata parte da General Info con Name vuoto, Encryption non selezionata e due dischi non assegnati,223.57GiB e232.89GiB. La schermata successiva mostra tank compilato e preview Encryption None; poi è aperta Data con Layout ancora vuoto. Si osservano quindi Layout Mirror e il menu Disk Size aperto sulle due capacità, senza una taglia già selezionata. Manual Selection mostra soltanto WD WDS250G1B0A-00H9H0 sda232.89GiB e SanDisk SDSSDA240G sdc223.57GiB, entrambi SSD e con seriali corrispondenti al censimento privato. Il Kingston di boot non compare tra questi candidati. Dopo Add è presente un unico riquadro MIRROR, ancora vuoto, con richiesta di almeno due dischi e Save Selection disabilitato.

Prossimo trascinare dalla colonna sinistra prima il WD sda e poi il SanDisk sdc dentro lo stesso riquadro MIRROR a destra; non aggiungere un secondo VDEV. Leggere il risultato prima del salvataggio della selezione e del riepilogo. Le impostazioni sono ancora nel wizard: nessuna creazione, cancellazione o configurazione applicata osservate. La capacità0B della preview descrive la selezione ancora vuota, non una nuova misura della capacità fisica degli SSD.

Le sei immagini sono archiviate e verificate SHA-256 prima della rispettiva lettura, con originali conservati alla copia. Nessuna nuova email; primo export con seed invariato, nuova generazione dopo le modifiche effettive. Conservazione dei vecchi dati SanDisk/WD già risolta dalla dichiarazione dell’utente. S240 riletta per selezione manuale, mirror e raccomandazione sulla cifratura del dataset radice; la differenza fra pool, dataset e materiale di recupero è documentata nella nuova scheda07. Nessun dato ancora scritto e nessun dataset cifrato già creato.

## 28/10/2026: mirror dei due SSD selezionato, Review tank aperta

La selezione manuale mostra un solo MIRROR contenente sda232.89GiB e sdc223.57GiB, con Est. Usable Raw Capacity223.57GiB e No Unassigned Disks. L’avviso Mixing disks of different sizes riguarda le capacità differenti del WD e del SanDisk già previsti dal piano. Il risultato mostrato è limitato al membro più piccolo; non si sommano le due capacità e non si dichiara223.57GiB come spazio netto dei futuri file. Nessuna nuova prova SMART o sostituzione è richiesta da questo avviso.

L’utente riferisce di avere premuto Save Selection; la schermata successiva mostra Manually Configured VDEVs, VDEVs1 e No warnings. Preview: tank, Data Manual layout1VDEVs, Encryption None, Total Raw Capacity223.57GiB; nessun disco non assegnato disponibile. L’assenza di avvisi nel pannello non cancella l’avviso di taglia effettivamente letto nel dialogo. Save Selection ha salvato soltanto la scelta nel wizard.

La pagina Review è poi osservata con Pool Name tank, Data Manual layout1VDEVs ed Est. Usable Raw Capacity223.57GiB. Pulsanti Back, Inspect VDEVs, Start Over e Create Pool. La selezione precedente permette di collegare quel singolo VDEV al mirror WD/SanDisk; Kingston di avvio resta escluso. Prossimo cliccare Create Pool, pulsante azzurro in basso a destra del gruppo, e leggere il dialogo successivo. Creazione, cancellazione e ONLINE del pool dati ancora non osservati. La conferma dell’utente sui vecchi dati resta acquisita e non si ripete la stessa domanda.

Le immagini successive sono archiviate e verificate SHA-256 prima della lettura; quella iniziale del lotto era già archiviata ed è stata ricontrollata senza duplicarla. Nessuna email né nuova configurazione applicata osservate. Primo export con seed conservato; dopo la creazione effettiva servirà una nuova generazione. S240 per il passaggio dalla selezione al riepilogo e alla creazione.

## 28/10/2026: tank creato, mirror Online no errors

Sono osservati il riepilogo tank e il dialogo Warning con Confirm selezionato, poi pool.create a0%,15% con Formatting disks1/2 e95% con Setting pool options. La dashboard successiva mostra Pool created successfully. La creazione è conclusa e i due SSD dati sono stati riformattati secondo il flusso confermato dall’utente; la precedente dichiarazione sui contenuti già salvati è acquisita. Non si ripete la creazione. Il Kingston di avvio era escluso dalla selezione WD/SanDisk.

La dashboard tank mostra Data VDEVs1xMIRROR,2wide,Mixed Capacity e No other VDEV types. Storage Health: Online no errors. Usable Capacity213.19GiB, Available213.18GiB, Used8.19MiB e0% visualizzato. I223.57GiB della preview erano una stima grezza prima della creazione, non il valore ora indicato come utilizzabile. Non viene attribuita a una causa specifica la differenza senza una lettura dei relativi dettagli. Mixed Capacity conserva l’indicazione delle taglie differenti, non viene descritto come un guasto osservato.

Scheduled Scrub mostra At00:00 only on Sunday; è una pianificazione, non la prova di uno scrub già eseguito. Auto TRIM è Off. Disk Health mostra0avvisi legati alla temperatura e No disk temperature is available: zero avvisi non prova una temperatura regolare. Non si cambia ora la pianificazione né si avvia un nuovo scrub o test SSD/RAM.

Prossimo View VDEVs nel primo riquadro a sinistra per leggere membri e contatori dopo la creazione, poi nuova acquisizione configurazione con seed. Il primo file resta intatto, ma non copre la nuova tappa. Dataset/condivisioni e backup reali restano da realizzare. Le sei nuove immagini sono copiate e verificate SHA-256 prima della lettura. Il nuovo file con lo stesso nome della precedente cattura del riepilogo è diverso e conserva un archivio distinto; nessuna sovrascrittura dell’immagine già acquisita. Gli orari dei file sono registrati nel manifest ma non diventano orari esatti dei clic o del completamento. Nessuna nuova email osservata; registro email invariato. Lacuna delle vecchie immagini alert mantenuta.

## 28/10/2026: mirror e due membri ONLINE, prossimo export post-pool

La pagina tank VDEVs espande l’unico MIRROR e mostra tre righe ONLINE, tutte con ZFS Errors No errors: il MIRROR, sda232.89GiB e sdc223.57GiB. L’appartenenza effettiva dei due SSD selezionati è ora osservata dopo la creazione; il Kingston sdb di avvio non è membro di tank. La pagina non mostra i singoli numeri Read/Write/Checksum: non si trasformano le etichette No errors in letture numeriche non presenti. Il controllo di topologia e stato corrente è concluso, senza un altro test, scrub, shell o richiesta di altre schermate sui contatori.

Prossimo acquisire la configurazione post-pool: System > Advanced Settings > Manage Configuration > Download File; nel dialogo Save Configuration selezionare Export Password Secret Seed e premere Save. S137 riletta conferma percorso, casella e salvataggio dopo cambiamenti. Il primo archivio va mantenuto; nuova acquisizione, copia e verifica non ancora eseguite. Nel download locale è ancora presente soltanto la prima generazione, secondo la lettura dei nomi file autorizzati. Dopo il download si verificano archivio e campi della tappa senza esporre seed o valori segreti.

L’immagine è archiviata e verificata SHA-256 prima della lettura, originale conservato alla copia. Nessuna modifica di configurazione, nuova email o prova di recupero osservate; registro email invariato. Dataset/condivisioni, backup dati, seconda destinazione indipendente e restore restano aperti.

## 29/10/2026: raccordo export post-pool e impostazioni da completare a casa

Registrato alle 2026-10-29T09:32:09+01:00.

Il file nativo indicato dall’utente è stato copiato e verificato il28/10:849920byte, SHA-256 originale/copia identici, SQLite quick_check ok e seed32byte presente. Il nuovo database contiene un unico record tank con GUID e System Dataset Pool tank; il primo non conteneva tank. Dimensione uguale non significa contenuto uguale: le impronte delle generazioni sono diverse. Confronti booleani confermano inoltre mittente, nome visualizzato, OAuth presente, recapito Proton e Europe/Rome; seed coerente con il precedente. Prima generazione e download originali conservati. Acquisizione post-pool conclusa, senza attribuire al file una prova di restore o una seconda destinazione indipendente.

Le tre schermate Advanced Settings del28/10 sono archiviate SHA-256 prima della lettura e mostrano: console testuale senza prompt Enabled, seriale Disabled; Syslog Info, nessun server e Include Audit Logs No; Audit7giorni, reservation/quota None e soglie75%/95%; debug kernel Disabled; Cron Jobs, Init/Shutdown Scripts e Sysctl senza voci. NTP contiene i tre server Debian configurati, senza prova di sincronizzazione. Storage indica System Dataset Pool tank e priorità resilver Never; Replication Tasks Limit5 è un limite simultaneo, non cinque attività configurate. Access mostra timeout5minuti, nessun banner; Allowed IP Addresses vuoto; nessuna GPU isolata; Global2FA TrueNAS e2FA SSH Disabled. Nessuna modifica è osservata in questi pannelli. La2FA Google già attiva resta una verifica distinta e conclusa.

Alla domanda sulle molte impostazioni, il quadro tecnico distingue preparazione locale, dipendenze della rete domestica e personalizzazioni giustificate da un bisogno. Dataset, utenti e permessi si preparano ora; indirizzi finali, DNS, VLAN e restrizione degli accessi seguono la topologia domestica; syslog segue la disponibilità del ricevitore. NTP effettivo e recupero precedono l’eventuale2FA NAS. Nessun debug, script, Sysctl o GPU aggiunti per riempire pannelli vuoti. Nuova guida tecnica10, matrice aggiornata e sviluppo didattico della scheda03; fonti S241/S242.

Il29/10 l’utente chiede di procedere. Prossimo cliccare Datasets nella barra sinistra e leggere la struttura di tank prima di creare dataset utente. Il nuovo export non va riscaricato per questa sola lettura. Filtro Log NAS, seconda copia indipendente, inclusione Veeam, restore, rete finale e obiettivo16GB restano aperti. Nessuna nuova email o nuova osservazione dal NAS il29/10 viene inventata; le letture fisiche restano del28/10.

## 29/10/2026: Datasets letto, requisito di crescita SSD/RAM/configurazione

Registrato alle 2026-10-29T09:50:32+01:00.

La pagina Datasets mostra tank selezionato, Unencrypted,12.21MiB usati e213.18GiB disponibili. Details: Root Dataset, Sync STANDARD, Compression2.00x(LZ4), Enable Atime OFF, ZFS Deduplication OFF, Case Sensitivity ON e Path tank. Usage segnala System Dataset; Space Management mostra Total Allocation12.21MiB, Data Written96KiB e Children12.12MiB; User Quotas e Group Quotas None. Permissions: owner root:root e permessi Unix mostrati. Per la selezione sono indicati Snapshots0, Snapshot Tasks0 e No Backup Tasks, senza confonderli con gli export di configurazione già acquisiti. Nessun dataset utente creato e nessuna modifica osservata. Il rapporto di compressione è un dato visualizzato, non una previsione sul contenuto futuro.

L’utente richiede esplicitamente che tutto il lavoro sia scalabile con SSD di taglia maggiore, RAM e configurazione. ADR-044 adotta struttura per funzione, nomi stabili e quote rivedibili; guida NAS11 e scheda08 documentano crescita dello stesso mirror, compatibilità della memoria e continuità hardware tramite ADR-043. S243/S244 indicano sostituzione di un membro alla volta, attesa del resilver prima del successivo ed espansione dopo l’ultimo; S245 tratta dataset e quote modificabili; S246 dimensiona la memoria per carico e piattaforma. Nessun upgrade o nuovo test hardware eseguito o richiesto adesso.

Prossimo cliccare Add Dataset, pulsante azzurro in alto a destra accanto ad Add Zvol, e leggere il modulo prima di compilare o salvare. Il primo dataset utente sarà definito per funzione, senza modificare i permessi della radice per renderla una condivisione generica. Immagine archiviata e verificata SHA-256 prima della lettura, originale conservato alla copia. Nessuna nuova email o configurazione applicata; i due export precedenti rimangono il checkpoint acquisito, senza nuovo download per la sola navigazione.

## 29/10/2026: dataset avanzato e scelta della chiave

Registrato 2026-10-29T10:48:07+01:00. Modulo Add Dataset base e avanzato letto; immagini copiate prima della lettura e SHA-256 verificati. Prima Name vuoto/Generic/Save disabilitato; opzioni avanzate con quote/prenotazioni vuote, soglie80/95 ereditate, proprietà tabellate nella guida NAS12, ACL Type Inherit e Mode Restricted; Save abilitato non premuto. L’intestazione delle immagini avanzate non è visibile: documenti/SMB sono indicazioni da verificare, non valori già attestati. L’utente sceglie chiave automatica; Inherit(non-encrypted) ancora selezionato, cifratura non applicata. Prossimo Encryption Key/Generate Key, intestazione e ACL NFSv4 prima di Save. Dopo creazione chiave esterna e nuova generazione export; nessun nuovo export per la sola lettura. Nessuna mail nuova o modifica hardware. Fonti S247-S249.

Richieste parallele: studio17/ADR-045 raggruppano assistente personale a basso consumo, Hermes, Nix/NixOS, Tailscale e brain futuro dal template. Handoff letto e conservato privato; nessun servizio installato. Jev da chiedere soltanto quando il template avrà recepito l’impianto, come richiesto dall’utente. Il filone non azzera il punto operativo NAS.

## 29/10/2026: nome SMB e cifratura automatica confermati nel modulo

Registrato 2026-10-29T11:15:17+01:00. Due nuove immagini archiviate prima della lettura, originali conservati e SHA-256 verificati. Add Dataset: Parent Path tank, Name documenti, Dataset Preset SMB; Create SMB Share selezionato e SMB Name documenti. Encryption Inherit(non-encrypted) deselezionato, Encryption selezionato, Type Key, Generate Key selezionato, Algorithm AES-256-GCM. Comments vuoto, Sync Inherit(STANDARD), Compression Inherit(LZ4); quote superiori visibili vuote. tank sullo sfondo Unencrypted,12.57MiB usati/213.18GiB disponibili. Nessun Save o esito creazione osservati, nessuna nuova chiave esportata o condivisione creata. ACL non inquadrate: ultimo riscontro Inherit/Restricted. Prossimo togliere Create SMB Share per preparare prima utente e permessi, impostare ACL Type NFSv4 lasciando Mode Restricted, quindi Save e leggere esito/dialogo. La nuova configurazione con seed e la chiave esterna seguono la creazione, non questa anteprima. Nessuna nuova email o modifica hardware. Guida NAS12 aggiornata; S245/S247/S248 già registrate.

## 29/10/2026: condivisione automatica tolta, checklist unica per salvare

Registrato 2026-10-29T11:16:42+01:00. Nuova immagine copiata prima della lettura e SHA-256 verificato. Create SMB Share deselezionato, campo SMB Name non più mostrato; preset SMB, quote/riserve vuote e soglie80/95 ereditate confermati. L’utente chiede tutti i settings in un solo messaggio per scadenza della sessione: checklist completa nella guida NAS12, nessun ulteriore controllo intermedio degli stessi campi. Prossimo ACL Type NFSv4 e Mode Restricted, poi Save e lettura dell’esito. Nessun Save o dataset creato osservato, nessuna chiave esportata. Didattica: nessuna nuova scelta, resta sviluppo voce7/scheda07 già scritto. Assistente e richiamo Jev invariati.

## 29/10/2026: primo dataset cifrato creato e ancora non condiviso

Registrato 2026-10-29T11:21:47+01:00. Due immagini archiviate prima della lettura, SHA-256 verificati e originali conservati.

Creazione osservata alle11:18: selezione documenti e messaggio Switched to new dataset. Dataset cifrato Unlocked, Usage Not Shared, Path tank/documenti. Used192KiB e Available213.17GiB; Total Allocation192KiB e Data Written192KiB(100%). SyncSTANDARD, Compression Inherit(1.00x(LZ4)), AtimeOFF, DedupOFF e CaseSensitivityOFF. UserQuotasNone. Per questa selezione Snapshots0,SnapshotTasks0,NoBackupTasks: nessuna attività dati ancora configurata. Radice tank Unencrypted,12.93MiB usati/213.17GiB disponibili. Owner root:root, pannello NFSv4 con tre ACE visibili: owner@root AllowFullControl,group@root AllowModify,builtin_users AllowModify; parte inferiore tagliata, non è una trascrizione completa delle ACL.

Prima del risultato compare ACL Types & ACL Modes, avviso generale sulla conversione delle ACL. L’anteprima sottostante mostra ACL Type SMB/NFSv4 e ACL Mode Passthrough. La dashboard successiva conferma NFSv4 ma non espone ACL Mode: non si dichiara Restricted applicato. Il valore finale va letto nella modifica delle proprietà prima di completare i permessi e la share; non si ricrea il dataset né si riaprono test hardware. Non occorre una snapshot preventiva per una migrazione di dati esistenti che questa creazione nuova non sta eseguendo.

Prossimo passo: mantenere documenti selezionato, scorrere nel pannello destro fino al riquadro Encryption e premere Export Key. S248 conferma che scarica un JSON; il file va acquisito nel livello privato senza trascrivere la chiave nei documenti o nella chat. S247 descrive la custodia esterna. Serve inoltre una nuova generazione dell’export con Password Secret Seed, conservando le due precedenti. Due copie sullo stesso client non chiudono la destinazione indipendente o il ripristino. Nessuna chiave esterna o nuovo export post-dataset è già acquisito.

## 29/10/2026: chiave del dataset acquisita e verificata fuori NAS

Registrato 2026-10-29T11:46:22+01:00. Chiave di tank/documenti acquisita dal file indicato dall’utente:86byte, originale conservato e copia privata ignorata da git, impronte SHA-256 uguali. JSON valido per il solo dataset atteso, chiave in formato esadecimale256bit; nessun valore stampato o trascritto nei documenti pubblici. Acquisizione della chiave fuori NAS conclusa. Download e archivio sono sullo stesso client: destinazione indipendente e prova di sblocco/ripristino ancora aperti. Nessuna dimostrazione del valore finale ACL Mode da questa lettura del file.

Prossimo System > Advanced Settings > Manage Configuration > Download File; selezionare Export Password Secret Seed e Save. Il nuovo archivio post-dataset è ancora da acquisire, mantenendo entrambi gli export del28/10. S137 riletto e conferma percorso e opzione; key export e configurazione restano materiali distinti. Nessuna nuova mail, test hardware o modifica al filone assistente/Jev.

## 29/10/2026: terzo export con seed post-documenti acquisito

Registrato 2026-10-29T11:53:05+01:00. Terzo export TrueNAS25.10.7 post-dataset acquisito:849920byte, copia privata ignorata identica al download per SHA-256, originale conservato. SQLite835584byte letto soltanto in memoria supera quick_check; seed32byte presente e coerente con la precedente. Quindici controlli di checkpoint tutti positivi: record tank/documenti univoco con campo chiave non vuoto e gestione locale, assente nell’export post-pool; pool/GUID invariati; share documenti non creata nel database; mittente/nome e recapito amministratore coerenti, OAuth presente, Europe/Rome e System Dataset Pool tank. Archivio differente da entrambe le generazioni precedenti, che restano conservate. Chiave JSON separata già acquisita e riletta per impronta. Nessun valore segreto stampato, nessun database o seed estratti su file. Il campo chiave del database non è stato decifrato o confrontato in valore con il JSON: la verifica non prova uno sblocco o restore.

Acquisizione dell’export di questa tappa conclusa. Download, archivio e chiave sono sul medesimo client: seconda destinazione indipendente, inclusione Veeam e recupero restano aperti. ACL Mode non è dimostrato dai controlli del database: ultima anteprima Passthrough, valore finale ancora da leggere. Prossimo Datasets > documenti > Edit nel riquadro Details > Advanced Options, scorrere fino a ACL Type/ACL Mode e leggere i valori; poi utente, permessi e condivisione. Nessun altro export identico o test hardware richiesto.

## 29/10/2026: pannello ACL senza identificazione del dataset

Registrato 2026-10-29T12:11:38+01:00. Immagine copiata prima della lettura e SHA-256 verificato, originale conservato. Edit Dataset mostra Snapshot Directory Invisible, SnapdevHidden, Copies1, RecordSize128K, ACL Type POSIX e ACL Mode Discard entrambi disabilitati, SpecialSmallBlocks0. Il nome/percorso del dataset è fuori inquadratura; il riscontro è compatibile con tank radice (S248), non una prova di regressione del figlio documenti già mostrato NFSv4. Prossimo chiudere il pannello con X, selezionare la riga documenti e verificare Details for documenti prima di Edit/Advanced Options e lettura ACL Type/Mode. Nessun Save o cambiamento dei permessi osservati; nessun nuovo export richiesto per questa sola lettura. tank sullo sfondo13.08MiB/213.17GiB, documenti192KiB/213.17GiB Unlocked.

Rapporto NordVPN recepito nello studio18/ADR-046: scelta domestica e account condiviso distinti da WireGuard/Tailscale. Nessuna modifica al NAS o alla rete deriva da tale studio.

## 29/10/2026: documenti verificato con ACL SMB/NFSv4 e Restricted

Registrato 2026-10-29T12:21:49+01:00. Tre immagini archiviate prima della lettura, SHA-256 verificati e originali conservati. Il modulo Edit Dataset mostra Name tank/documenti bloccato: identità ora verificata. Valori letti: Comments vuoto; Sync Inherit(STANDARD); Compression Inherit(LZ4); Atime Inherit(OFF); Dedup Inherit(OFF); Case Sensitivity Insensitive bloccato; Checksum Inherit(ON); Read-only Inherit(OFF); Exec Inherit(ON); Snapshot Directory Invisible; Snapdev Inherit(HIDDEN); Copies1; Record Size Inherit(128KiB); ACL Type SMB/NFSv4; ACL Mode Restricted; Metadata(Special)Small Block Size Inherit(0). Save abilitato e Basic Options visibile. tank sullo sfondo13.16MiB/213.17GiB, documenti192KiB/213.17GiB Unlocked. Nessun campo richiede modifica.

Chiusa la lettura del tipo e della modalità ACL nel modulo identificato; i precedenti POSIX/Discard senza nome non sono proprietà accertate di documenti. Nessun nuovo Save osservato in queste immagini. Indicazione operativa: Save per confermare, poi Credentials > Users > Add e lettura del modulo utente; nessun utente, permesso finale o share ancora creati. Nessun nuovo export richiesto per una lettura senza cambi di configurazione. Tre export e chiave JSON restano acquisiti e verificati; copia indipendente e restore aperti.

Richiesta di stile ribadita dall’utente: in un solo messaggio indicare soltanto i settings che cambiano; tutti i valori, le ragioni e lo stato nel progetto. Qui i cambi necessari sono nessuno.
