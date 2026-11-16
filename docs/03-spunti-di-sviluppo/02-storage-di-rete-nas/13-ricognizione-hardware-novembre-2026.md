# Riorganizzazione hardware: ricognizione del 16/11/2026

Ritorno al [NAS](README.md). Questa ricognizione aggiorna i dati disponibili per l'[allocazione canonica](../23-studio-home-lab/12-allocazione-dell-hardware.md), senza dichiarare eseguiti trasferimenti, clonazioni o ampliamenti. L'utente dà priorità alla riorganizzazione prima di proseguire utenti e condivisioni TrueNAS; il PC Windows quotidiano deve rimanere utilizzabile.

Chiarimento successivo del 16/11/2026. Il Samsung 850 EVO M.2 SATA da250GB è hardware già posseduto e censito dalle foto del09/10; la nota del17/10 sul disco non montato in PC-03 riguardava la sua ubicazione dopo il prelievo, non la sua assenza dall'inventario. L'utente propone ora questo SSD per il Windows quotidiano, liberando il BX5001TB verso il NAS dopo migrazione verificata. La precedente destinazione al laboratorio è da rivalutare. Non si dichiara che il disco sia stato ritrovato o montato in questo giro: questo riscontro si farà al momento della preparazione fisica. ASRock elenca sei porte SATA e nessun alloggiamento M.2 per la H97 Anniversary; il collegamento dell'850EVO M.2 SATA richiede quindi un adattatore appropriato da M.2 SATA a SATA, non un adattatore solo NVMe. Fonti: [ASRock H97 Anniversary](https://www.asrock.com/mb/intel/h97%20anniversary/) e [Samsung MZ-N5E250BW](https://www.samsung.com/es/support/model/MZ-N5E250BW/). Collegamento e avvio effettivi ancora da verificare.

## Componenti recuperati da PC-03

L'utente dichiara AnduinOS, PC-03, e Xubuntu, PC-02, ora smembrati. L'alimentatore Atlantis P016-MPW-6000-W e i due moduli Corsair precedentemente censiti su PC-03 sono recuperati e disponibili. Non sono un alimentatore e un kit aggiuntivi rispetto all'inventario precedente. La disponibilità degli altri componenti non si deduce da questa dichiarazione. Da PC-02 risultavano già prelevati quattro moduli DDR3, due da 2 GB e due da 4 GB, per 12 GB; il recupero del DVD resta non confermato.

La targa dell'Atlantis riporta 600 W massimi, due rami +12 V da 22 A, +3,3 V da 24 A e +5 V da 30 A, con 150 W combinati su queste ultime due tensioni. La foto identifica il prodotto e non misura salute elettrica, efficienza o stabilità. Resta una scorta non collaudata; nessuna sostituzione del Corsair HX520W del NAS è decisa.

Le due immagini della RAM sono trattate come viste della stessa coppia, coerentemente con i due moduli dichiarati dall'utente. Le etichette identificano CMV16GX3M2A1600C11: Corsair conferma un kit ValueSelect da 2 × 8 GB, DDR3, 1,5 V, velocità di prova 1600 e SPD 1333. La precedente denominazione Vengeance nell'inventario è errata. Nessun test di questa coppia nella nuova destinazione è ancora eseguito.

## Nuovo PC Windows quotidiano, PC-07

Identificativo documentale nuovo, distinto dalle macchine già censite. Fonte: report hardware generato il 15/11/2026 e letto integralmente il 16/11; originale acquisito nel livello privato con impronta identica prima della cancellazione richiesta dall'utente. Foto e report restano privati. Il nome host reale non viene pubblicato.

| Componente | Stato riportato | Implicazione per la redistribuzione |
|---|---|---|
| Scheda e CPU | ASRock H97 Anniversary, BIOS P1.50, Intel i7-4790, 4 core/8 thread | piattaforma DDR3, distinta dal NAS DDR4 |
| Memoria | quattro Kingston da 4 GB, 16 GB nominali, 1333 MT/s; 15,7 GB visibili | tutti gli slot occupati: aumentare la RAM richiede sostituzioni |
| Codici memoria | 99U5584-005.A00LF, 99U5584-007.A00LF, due KHX1600C9D3/4GX | l'eventuale combinazione con Corsair va verificata al banco |
| SSD sistema | Crucial BX500 CT1000BX500SSD1, SATA, 1 TB nominale, 931,51 GiB riportati | candidato al NAS soltanto dopo migrazione Windows verificata |
| Volume C: | 929,89 GiB totali e 789,40 GiB liberi | circa 140,49 GiB occupati; SSD SATA 240/250 GB potenzialmente sufficiente, non prova della clonabilità |
| HDD dati | Samsung HD502HJ 500 GB, volume G: con circa 275,28 GiB occupati | contiene dati: non è un disco libero né il disco di PC-02 per sola coincidenza del modello |
| Dispositivo USB | circa 238,75 GiB, modello generico | supporto non identificato; non si conta come SSD SATA disponibile |
| Avvio e cifratura | Windows 11 Pro build 26100, GPT/UEFI, Secure Boot False, TPM assente, BitLocker Off sui volumi elencati | uso di Rufus dichiarato dall'utente, non dimostrato dal report; preservare avvio e ambiente quotidiano |

Nel campione di memoria risultano 9,57 GiB in uso su 15,7 visibili e 6,13 liberi. È una fotografia, non il picco del carico quotidiano. I valori virtualizzazione firmware False e hypervisor presente True non bastano a diagnosticare il firmware: nessuna modifica proposta da questi soli campi. Le unità etichettate GB dal report sembrano calcolate in base binaria dalle capacità dei dischi; qui si usa GiB per non confonderle con i tagli commerciali.

Il report mostra BX500 a 28 °C e 1855 ore, HDD a 27 °C e 43616 ore con 7571 cicli. Healthy e i pochi contatori disponibili non equivalgono a un esame SMART completo, né certificano usura nulla. Nessun test esteso o controllo dei settori pendenti è attestato da questo report.

## Alternative da scegliere, senza doppio conteggio

| Opzione | Composizione | Compromesso |
|---|---|---|
| Windows con RAM attuale | quattro Kingston da 4 GB, 16 GB | mantiene il PC com'è; Corsair recuperati disponibili per altro uso |
| Windows a 24 GB, prima proposta | due Corsair da 8 GB e due Kingston da 4 GB | usa la sola coppia recuperata; libera due Kingston, richiede disposizione per canale e prova della combinazione |
| Windows a 32 GB | quattro moduli da 8 GB | servono altri due moduli da 8 GB oltre ai recuperati: quelli di linux-desktop-B erano previsti per il laboratorio; disponibilità e priorità da confermare |

ASRock dichiara quattro slot DDR3/DDR3L e massimo 32 GB. Il tetto supportato non dimostra stabilità di una combinazione specifica. Il NAS H170-PRO usa DDR4: queste DDR3 non risolvono il suo obiettivo ancora aperto di 16 GB. I Crucial DDR4 del server restano assegnati al server finché non viene approvato un nuovo piano.

Per lo storage si valuta Windows su un SSD SATA più piccolo e BX500 verso il NAS. Prima occorre identificare il sostituto realmente disponibile e sano, conservare i dati, verificare riduzione delle partizioni e avvio indipendente dal vecchio disco. Un Samsung 850 EVO M.2 non va confuso con un SATA da 2,5 pollici né considerato disponibile prima di localizzarlo.

Il mirror NAS attuale rimane composto da SanDisk 240 GB e WD 250 GB. Sostituire soltanto un membro con il BX500 non produce un mirror da 1 TB: la capacità resta limitata dal membro più piccolo. La crescita richiede un secondo membro adeguato e la procedura appropriata; non si propone l'aggiunta del BX500 come singolo vdev dati privo di ridondanza. Non sono autorizzate cancellazioni di dischi o ricreazione del pool da questa ricognizione.

Restano da chiarire la disponibilità dei due moduli da 8 GB di linux-desktop-B, la priorità attuale del laboratorio ora che PC-03 è smembrato, gli altri SSD realmente liberi e il secondo membro del futuro mirror. Nessun acquisto deciso. Il punto operativo NAS precedente è conservato nel registro e riprenderà dopo questo confronto.

## Fonti e riscontri

Fonti locali: report del nuovo PC, dichiarazione dell'utente sullo smembramento e sull'uso quotidiano di Windows, tre fotografie acquisite con confronto SHA-256. Manifest e originali acquisiti restano nel livello privato del progetto.

Fonti primarie lette il 16/11/2026: [ASRock H97 Anniversary](https://www.asrock.com/mb/intel/h97%20anniversary/), limiti e tipi di memoria; [Corsair CMV16GX3M2A1600C11](https://www.corsair.com/ca/en/p/memory/cmv16gx3m2a1600c11/corsair-memory-a-16gb-dual-channel-ddr3-memory-kit-cmv16gx3m2a1600c11), capacità, serie e tensioni; [manuale ASUS H170-PRO](https://dlcdnet.asus.com/pub/ASUS/mb/LGA1151/H170-PRO/E12046_H170-PRO_UM_V2_WEB.pdf), tipo DDR4 individuato dal risultato del produttore, senza rilettura integrale del PDF; [TrueNAS 25.10, sostituzione dischi](https://www.truenas.com/docs/scale/25.10/scaletutorials/storage/disks/replacingdisks/), requisiti del disco sostitutivo e ricostruzione del mirror. Le regole di crescita già documentate sono nella [guida alla crescita NAS](11-crescita-del-nas-e-indipendenza-dall-hardware.md).

## Quadro complessivo ricomposto prima delle assegnazioni

Recap richiesto dall'utente il 16/11/2026. Le etichette dei vecchi censimenti non dimostrano che oggi una macchina sia ancora assemblata: dove manca una conferma si conserva l'incertezza. Il nuovo report Windows e le dichiarazioni sullo smembramento prevalgono sulle vecchie destinazioni previste.

| Macchina riconoscibile | Etichetta precedente | Ultimo hardware documentato | Stato utile per la riorganizzazione |
|---|---|---|---|
| NAS TrueNAS | PC-DESKTOP-A | ASUS H170-PRO, i7-6700, 8 GB DDR4, Corsair HX520W | assemblato; Kingston V300 240 GB sistema, SanDisk 240 GB e WD Blue 250 GB nel mirror tank |
| Futuro server Proxmox | linux-desktop-A | ASRock H270M Pro4, i7-7700, quattro Crucial DDR4 da 4 GB | 16 GB documentati; due NVMe Crucial P2/P3 da 1 TB assegnati, montaggio e installazione non confermati |
| Windows quotidiano | nuovo PC-07 | ASRock H97 Anniversary, i7-4790, quattro Kingston DDR3 da 4 GB | in uso; BX500 SATA 1 TB sistema, Samsung HDD 500 GB dati; non è una macchina donatrice intera |
| Postazione musica Ubuntu Studio | linux-desktop-C | H170-PRO e i7-6700 secondo censimento storico | in uso, nessun prelievo richiesto; non si conta la sua RAM o il suo disco come scorta libera |
| Scorta del NAS | PC-DESKTOP-B | ASUS B150-PRO, i7-6700 | ultima descrizione assemblata senza RAM e SSD; conserva case, CPU, dissipatore e alimentatore |
| Seconda piattaforma Haswell | linux-desktop-B | ASUS Z97-P, i7-4790, due Corsair DDR3 da 8 GB con codici diversi | censimento storico distinto da AnduinOS; presenza attuale di macchina e moduli da riconfermare; precedenti problemi di avvio/firmware documentati nel consolidamento |
| AnduinOS | PC-03 | ASUS Z97-P, CPU LGA1150 non identificata | ora smembrato; Corsair ValueSelect 2 × 8 GB e Atlantis recuperati; altri pezzi da localizzare, non automaticamente smaltiti |
| Xubuntu | PC-02 | vecchia piattaforma P55/LGA1156 | ora smembrato/dismesso; DDR3 2 × 4 GB e 2 × 2 GB recuperate, Tecnoware 550 W e GeForce 210 conservati; Kingston V300 già nel NAS, HDD Samsung 500 GB destinato alle prove; DVD non confermato |
| Firewall dedicato | NET-04 | i3 settima generazione, 8 GB RAM, SSD 120 GB | OPNsense installato, rete ancora da configurare; componenti fuori dal lotto da riallocare |

Il budget DDR4 mobile resta quello già censito: 8 GB in uso sul NAS e 16 GB sul server, mentre tre TEAMGROUP da 8 GB con errori restano esclusi dall'uso affidabile. Non si sommano i 24 GB con errori alla capacità utilizzabile e non si conta la RAM delle postazioni in servizio come già prelevabile. Gli 8 GB DDR4 mancanti per NAS16/server16 non vengono forniti dalle DDR3 recuperate.

Il budget DDR3 distingue quattro gruppi: 16 GB Corsair recuperati da AnduinOS, 12 GB Kingston recuperati da Xubuntu, 16 GB Kingston in uso sul nuovo Windows, altri 16 GB Corsair soltanto dal censimento storico della seconda Z97-P. Questi ultimi non sono dichiarati disponibili oggi senza riscontro. La destinazione del vecchio laboratorio da32GB non è più fissata mentre PC-03 è smembrato.

Per i dischi, i due NVMe da1TB restano assegnati al server; il BX500 SATA da1TB è ancora il disco Windows. Il Samsung850EVO M.2 SATA250GB di AnduinOS è già censito e ora proposto dall'utente per Windows, con ubicazione da riscontrare nella preparazione fisica; non va considerato un SSD SATA2,5pollici pronto per la H97. Il Samsung HDD500GB del Windows contiene dati; quello omonimo di Xubuntu è un altro esemplare censito, non una capacità da contare due volte sulla stessa macchina.

La prima proposta conserva NAS e server nelle piattaforme DDR4, mantiene Windows e Ubuntu Studio come postazioni, valuta Windows16/24/32GB in base ai pezzi realmente presenti e concentra la crescita NAS su una coppia di dischi adeguata. Spostare il NAS a32GB DDR3 richiederebbe invece un cambio di scheda e processore e una valutazione distinta di stabilità, consumo e recupero: non è un semplice aumento di RAM della H170-PRO e non è stato scelto. Non si ordina alcuno smontaggio o trasferimento da questo recap.
