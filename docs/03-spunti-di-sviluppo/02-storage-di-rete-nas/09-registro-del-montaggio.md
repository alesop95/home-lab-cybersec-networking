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
