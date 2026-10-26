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
