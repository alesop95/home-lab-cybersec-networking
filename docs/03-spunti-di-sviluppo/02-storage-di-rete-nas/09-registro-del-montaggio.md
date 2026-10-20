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
