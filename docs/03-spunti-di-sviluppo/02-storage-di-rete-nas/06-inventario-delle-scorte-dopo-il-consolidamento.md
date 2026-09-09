# Inventario delle scorte dopo il consolidamento

> Che cosa resta disponibile nelle macchine dismesse una volta che il NAS[^1] ha preso i pezzi che gli servono. Risponde a una domanda sola: se fra sei mesi serve mettere insieme un'altra macchina, con che cosa la si fa. Il materiale di lavoro con i valori reali, cioè nomi macchina, numeri di serie, indirizzi e utenze, vive fuori dall'albero versionato e non è riferito qui: in questa scheda le macchine hanno segnaposto, gli stessi della scheda di consolidamento.

## Stato di questo documento

I dati vengono dai censimenti hardware raccolti sul campo con due script di sola lettura, uno per Windows e uno per Linux, e dove un dato non compare nel censimento questo documento lo dichiara mancante invece di dedurlo a occhio: l'ultima sezione elenca proprio quei buchi.

È un inventario a consuntivo previsto e non osservato. Al momento della scrittura lo smontaggio è iniziato e non concluso: dalla prima scorta i pezzi sono stati prelevati, le altre due non sono state aperte. Diventa un inventario osservato quando la fase di smontaggio si chiude, e la differenza fra le due cose non è formale, perché un pezzo si conferma presente quando lo si ha in mano e non quando un censimento lo elenca.

Il rapporto con il resto del progetto è quello della fase 4 della roadmap, cioè lo storage di rete. La scheda che porta l'analisi e le decisioni è [Consolidamento di quattro desktop dismessi in un NAS](03-consolidamento-di-quattro-desktop-dismessi-in-un-nas.md), la sequenza da eseguire al banco è nella [Guida all'assemblaggio e all'installazione di TrueNAS](04-guida-assemblaggio-e-installazione-truenas.md), e la finestra di accensione è in [Consumo elettrico del NAS e finestra di accensione](05-consumo-elettrico-e-finestra-di-accensione.md). Questa scheda guarda il lato opposto: non la macchina che nasce, ma ciò che resta delle quattro che si smontano.

## Il confine, cioè che cosa esce e non torna

Cinque pezzi lasciano le tre macchine di scorta e finiscono nella base, dove si sommano ai due moduli di memoria e all'unico disco che la base ha già dentro.

| Pezzo | Da | Dove finisce |
|---|---|---|
| Modulo 8 GB DDR4-2400 | `PC-DESKTOP-B`, primo alloggiamento | uno dei quattro alloggiamenti del NAS |
| Modulo 8 GB DDR4-2400 | `PC-DESKTOP-B`, terzo alloggiamento | uno dei quattro alloggiamenti del NAS |
| SSD SATA da 250 GB | `PC-DESKTOP-B` | seconda metà dell'insieme di avvio in mirror |
| NVMe da 1 TB, Crucial P2 | `linux-desktop-A` | alloggiamento M.2 della scheda madre |
| NVMe da 1 TB, Crucial P3 | `linux-desktop-B` | adattatore da PCIe verso M.2 nel secondo slot x16 |

La conseguenza che conta non è che cosa esce ma che cosa non resta: dopo il consolidamento le tre macchine di scorta hanno zero dischi. Nessuna delle tre si avvia senza comprarne almeno uno, ed è il vincolo che governa qualunque ricostruzione, non la memoria e non il processore. Vale scriverlo in chiaro proprio perché è controintuitivo: si dismettono quattro computer e non rimane un solo disco.

## Che cosa resta in ciascun telaio

### `PC-DESKTOP-A`, che diventa il NAS e non è una scorta

Va tenuta fuori dal magazzino, perché è la macchina di destinazione e non una riserva di pezzi. Resta elencata qui solo perché due cose al suo interno diventano inutili nel ruolo di NAS e si possono prelevare senza danno: l'unità ottica DVD, che su un NAS non ha nessun impiego, e il monitor collegato, che serve durante l'installazione e i test e poi non più.

La licenza Windows Professional di questa macchina, di canale legato all'hardware, muore con il consolidamento, perché il suo disco viene riscritto dall'installazione di TrueNAS. È una perdita accettata e va saputa, non scoperta a cose fatte.

### `PC-DESKTOP-B`, la scorta gemella della base

È la scorta più preziosa delle tre, e la ragione è che condivide con la base il socket, la generazione di memoria e lo stesso modello di processore: se la scheda madre del NAS muore, questa parte al suo posto e i pezzi del NAS le entrano senza adattare niente. Resta con la sua scheda madre ASUS B150-PRO in formato ATX, quattro alloggiamenti di memoria con massimo dichiarato di 64 GB e sette slot di espansione, cioè uno in più della base, il processore Intel i7-6700 con il suo dissipatore, la grafica integrata, la rete integrata Realtek, l'unità ottica DVD e il case con il suo alimentatore.

Resta senza memoria e senza disco, ed è la macchina più scomoda da riaccendere delle tre. Paradossalmente è anche la più utile da tenere intatta proprio in quello stato, perché il suo valore è quello di un ricambio e non quello di una postazione.

Due dettagli da ricordare il giorno in cui la si rimettesse in servizio. La virtualizzazione hardware nel suo firmware risulta disattivata, quindi va abilitata prima di pensarla come nodo di un ipervisore: è un'impostazione e non un limite del processore, che la supporta. Il suo Windows Professional ha una licenza legata alla macchina, e una reinstallazione su un disco nuovo dovrebbe riattivarsi da sola contro lo stesso hardware, ma questa è un'inferenza sul comportamento dell'attivazione digitale e va verificata al momento invece di essere data per certa.

Un'ultima nota che evita un errore di lettura del censimento: fra le interfacce di rete di questa macchina compare un adattatore virtuale creato da un client VPN[^2] installato. Non è hardware e con l'inventario dei pezzi non ha niente a che fare.

### `linux-desktop-A`, la più recente e la sola con rete Intel

È la macchina che si riaccende con la spesa minore, perché conserva tutta la sua memoria e le manca soltanto un disco. Resta con la scheda madre ASRock H270M Pro4 in formato micro-ATX, il processore Intel i7-7700 di generazione Kaby Lake, la grafica integrata, l'unità ottica DVD, il case con il suo alimentatore, e la memoria completa e non toccata dal consolidamento, cioè quattro moduli Crucial `CT4G4DFS824A.C8FHP` da 4 GB DDR4-2400 che occupano tutti e quattro gli alloggiamenti.

La cosa che la distingue davvero è la rete, perché la sua interfaccia integrata è un controller Intel I219-V invece del Realtek delle altre, ed è esattamente la famiglia che i firewall e gli ipervisori open source trattano meglio. Il rovescio della medaglia è che essendo integrata nel chipset non si trapianta: chi vuole quella rete deve usare quella macchina, non spostarne un pezzo.

### `linux-desktop-B`, un'isola di piattaforma a sé

È la più vecchia e la sola che non condivide niente di elettrico con le altre tre, quindi va pensata come una macchina intera o come niente. Resta con la scheda madre ASUS Z97-P in formato ATX, il processore Intel i7-4790 di generazione Haswell su socket LGA1150, cioè un socket diverso da quello delle altre tre, la grafica integrata, la rete integrata Realtek, l'unità ottica e il case con il suo alimentatore. La memoria che le resta dentro è di 16 GB in due moduli DDR3, con due alloggiamenti liberi.

Sulla scheda risulta anche un ponte da PCIe verso PCI, che è il modo in cui questa generazione offriva ancora slot PCI legacy: se un giorno servisse ospitare una scheda PCI vecchia, questa è la sola delle quattro che può farlo.

I due moduli DDR3 vanno etichettati come coppia spaiata, ed è il dettaglio meno intuitivo dell'intero magazzino. Sembrano una coppia e non lo sono: hanno codici prodotto diversi, `CMV8GX3M1A1333C9` nominale da 1333 MHz e `CMV8GX3M1A1600C11` nominale da 1600 MHz, e girano entrambi a 1333 allineandosi al più lento. Funzionano così da anni e non c'è niente da correggere, ma chi li ritrovasse fra due anni in un sacchetto li crederebbe appaiati e proverebbe a farli girare a 1600.

### `linux-desktop-C`, in servizio e non disponibile

È una quinta postazione, censita a smontaggio già avviato, che non fa parte del consolidamento e non è una scorta: è in esercizio con Ubuntu Studio. Sta in questo inventario perché ignorarla sarebbe peggio che elencarla, e la ragione è una sola, che riguarda la gerarchia dei ricambi.

Al NAS non porta niente, e la verifica lo conferma su tutti e tre i fronti. Il processore è lo stesso modello della base, quindi non sarebbe un miglioramento. La memoria non entra, perché con i quattro moduli da 8 GB il NAS arriva a 32 GB e i quattro alloggiamenti sono pieni, e per superarli servirebbero moduli da 16 GB che in casa non esistono. Il disco non serve, perché è un NVMe e il NAS ne ha già due da un terabyte, mentre ciò che manca al magazzino sono dischi SATA, e questa macchina non ne ha nessuno.

La ragione per cui va comunque registrata è che la sua scheda madre è la gemella identica di quella della base, stesso modello e stessa versione di firmware, con numeri di serie contigui, cioè due esemplari dello stesso lotto di produzione. Cambia la gerarchia dei ricambi: il sostituto ideale della scheda del NAS è questa e non la B150-PRO di `PC-DESKTOP-B`, ma essendo in servizio non è disponibile, quindi la scorta gemella resta il ricambio utilizzabile e questa resta l'informazione da ricordare il giorno in cui la scheda del NAS si guasta davvero.

C'è anche un beneficio collaterale, piccolo ma concreto. Questa macchina è una H170-PRO che avvia in UEFI[^3] da un Crucial P2 montato nel proprio alloggiamento M.2, cioè la prova sul campo che la stessa combinazione di scheda e famiglia di disco funziona, ed è esattamente quella che si userà sulla base al momento del montaggio del primo NVMe.

Va corretta infine un'affermazione fatta prima di censirla, quando l'unico dato disponibile era il nome host. Non è vero che il suo disco da 500 GB sia l'unico candidato a disco di scorta della casa: è un NVMe in uso su una macchina in esercizio, e il magazzino resta senza dischi.

## Il magazzino, per categoria

La stessa sostanza riordinata per tipo di pezzo, che è il taglio utile quando si cerca un componente e non si sa in quale telaio sia.

### Memoria disponibile

| Quantità | Tipo | Codice prodotto | Dove sta | Utilizzabile su |
|---|---|---|---|---|
| 4 × 4 GB = 16 GB | DDR4-2400 | `CT4G4DFS824A.C8FHP` | montata in `linux-desktop-A` | le tre schede LGA1151 |
| 2 × 8 GB = 16 GB | DDR3, coppia spaiata | `CMV8GX3M1A1333C9` e `CMV8GX3M1A1600C11` | montata in `linux-desktop-B` | solo `linux-desktop-B` |

I quattro moduli DDR4 sono il pezzo più fungibile del magazzino, ed è su di loro che si decide quale delle scorte si riaccende. Restano dove sono se si vuole tenere pronta `linux-desktop-A`, si spostano in `PC-DESKTOP-B` se si preferisce far rivivere la gemella della base; non esistono due kit, quindi le due cose si escludono.

### Dischi disponibili

Nessuno, ed è il vincolo dominante del magazzino. Tutti e quattro i dischi delle quattro macchine finiscono nel NAS e nessuna scorta ne conserva uno.

### Unità ottiche disponibili

Tre masterizzatori DVD SATA, uno per ciascuna delle tre scorte, più un quarto prelevabile dalla base perché sul NAS non serve. Sono i pezzi meno preziosi e i più facili da dimenticare dentro un case, e il loro solo impiego residuo realistico è leggere un supporto vecchio una volta ogni tanto, per il quale uno basta.

### Schede madri e processori disponibili

| Scheda madre | Formato | Socket | Memoria | Processore montato |
|---|---|---|---|---|
| ASUS B150-PRO | ATX | LGA1151 | DDR4, 4 alloggiamenti, max 64 GB | i7-6700, Skylake |
| ASRock H270M Pro4 | micro-ATX | LGA1151 | DDR4, 4 alloggiamenti | i7-7700, Kaby Lake |
| ASUS Z97-P | ATX | LGA1150 | DDR3, 4 alloggiamenti | i7-4790, Haswell |

### Periferiche di ingresso e uscita

Due tastiere Logitech K120, un mouse ottico Sunplus e un mouse Logitech RX1000, rilevati sulle due macchine Linux, più due monitor, uno sulla base e uno su `PC-DESKTOP-B`, di cui il censimento non ha saputo leggere il modello. Sono materiale di servizio, e due di questi pezzi vanno tenuti a portata di mano invece che riposti, perché una tastiera e un monitor servono al montaggio del NAS e a tutti i passi di test.

## Che cosa si combina con che cosa

Il magazzino non è un mucchio omogeneo: contiene due piattaforme che non si parlano, e riconoscerlo evita l'errore più probabile, cioè provare a montare la memoria sbagliata sulla scheda sbagliata.

Tre delle quattro schede sono LGA1151 di serie 100 e 200, cioè la base, la B150-PRO e la H270M Pro4, e usano tutte DDR4. Fra loro i moduli di memoria si scambiano liberamente, ed è quello che il consolidamento fa già spostando i due moduli da 8 GB dalla scorta gemella alla base.

Lo scambio dei processori è un discorso diverso e più delicato. L'i7-6700 è Skylake, l'i7-7700 è Kaby Lake, e sulle schede di serie 100 il supporto a Kaby Lake dipende dalla versione del firmware. Il firmware della B150-PRO è del novembre 2015, cioè precedente all'esistenza commerciale di Kaby Lake, quindi montarci l'i7-7700 senza prima aggiornarlo è con ogni probabilità destinato a non dare video: è un'inferenza dalle date e non un dato verificato, e va confermata sulla lista dei processori supportati pubblicata dal costruttore per quella scheda prima di provarci. Il caso opposto, l'i7-6700 sulla H270M Pro4, è quello che di norma funziona, ma vale la stessa disciplina, cioè si controlla la lista del costruttore invece di dedurre.

La quarta scheda è LGA1150 con DDR3 e non condivide niente con le altre tre, né il processore né la memoria. Con lei si scambiano soltanto i pezzi indifferenti alla piattaforma, cioè dischi SATA, unità ottiche, schede di espansione PCIe e alimentatori.

Sugli alimentatori e sui case la compatibilità è meccanica e non elettronica, quindi ampia: sono tre case, di cui due ATX e uno micro-ATX, e una scheda micro-ATX entra in un case ATX mentre il contrario non vale. È l'unico verso da ricordare.

## Tre ricostruzioni possibili, e il vincolo che le limita

Il vincolo viene prima delle idee. Con zero dischi in magazzino e un solo kit di memoria DDR4 libero, senza comprare niente non si riaccende nessuna delle tre scorte, e comprando un disco solo se ne riaccende una sola. Le tre strade che seguono sono quindi alternative fra loro e non una lista da percorrere.

La prima, e la più economica, è `linux-desktop-A` così com'è più un disco. È l'unica scorta che conserva la propria memoria, quindi la spesa è un disco e nient'altro, e in cambio si ottiene la macchina più recente delle quattro con la sola rete Intel del gruppo. È la candidata naturale a diventare un secondo nodo di laboratorio, per esempio un ipervisore su cui provare le macchine virtuali di monitoraggio previste dalla roadmap, senza toccare il NAS.

La seconda è `PC-DESKTOP-B` più i quattro moduli da 4 GB prelevati da `linux-desktop-A` più un disco. Dà una macchina Skylake con 16 GB e un case ATX comodo con sette slot di espansione, e ha senso solo se serve proprio quel formato o quegli slot. Ha due controindicazioni: spegne definitivamente `linux-desktop-A`, e consuma la scorta gemella della base, che è l'assicurazione del NAS. Fra le tre è quella che conviene meno.

La terza è `linux-desktop-B` più un disco. È la macchina più vecchia e la più esosa in consumo a pari lavoro, ma è anche interamente autosufficiente, perché la sua memoria DDR3 non serve a nessun altro e resta là comunque. È il banco di prova da sacrificare, quello su cui si installa qualcosa di distruttivo senza pensarci, e l'unica delle quattro che può ancora ospitare una scheda PCI legacy.

Sopra tutte e tre resta una regola di condotta che vale più delle idee: la scorta gemella della base non si cannibalizza. È la sola macchina del gruppo che può sostituire la base con un trapianto invece che con una ricostruzione, perché ha lo stesso socket, la stessa generazione di memoria e lo stesso modello di processore, e il giorno in cui la scheda madre del NAS si guasta il valore di quella coincidenza supera di molto il valore di qualunque ricostruzione fatta prima per curiosità.

## Che cosa manca a questo inventario

Quattro cose, tutte rilevabili solo a mano e a case aperti, e la prima è anche un passo formale della guida di smontaggio.

Gli alimentatori. Il censimento software non li vede, perché un alimentatore ATX non ha nessuna interfaccia dati verso la scheda madre e l'etichetta è la sola fonte: marca, modello, potenza nominale, eventuale certificazione di efficienza e numero di connettori SATA vanno letti a case aperto e trascritti, e sono il dato che decide quale dei quattro alimentatori alimenta il NAS.

I case. Marca e modello non compaiono da nessuna parte, perché il firmware di tutte e quattro le macchine dichiara un tipo di telaio generico e un numero di serie vuoto. A case aperti conviene annotare almeno il formato, il numero di alloggiamenti da tre pollici e mezzo e da due e mezzo, e la presenza o assenza di slitte di montaggio, perché è esattamente ciò che serve sapere quando si cerca dove mettere un disco.

I dissipatori dei processori. Non risultano dal censimento e non sono stati guardati. Se un giorno un processore si sposta, il dissipatore lo segue o va sostituito, e la pasta termica va rifatta comunque: sono componenti che invecchiano e vanno controllati quando si aprono i case, non dati per buoni.

I codici data dei moduli di memoria. Vanno annotati per i due moduli che si prelevano e per i due già montati sulla base, e restano da annotare anche per i quattro moduli da 4 GB di `linux-desktop-A`, che questo documento elenca per codice prodotto e non per codice data.

[^1]: *NAS*, Network Attached Storage - unità di memorizzazione collegata alla rete, che espone il proprio spazio disco come condivisione invece che come disco locale.

[^2]: *VPN*, Virtual Private Network - collegamento cifrato che estende una rete privata attraverso una rete pubblica; il suo client crea sul sistema operativo un'interfaccia di rete virtuale, che i censimenti hardware elencano accanto a quelle fisiche.

[^3]: *UEFI*, Unified Extensible Firmware Interface - firmware di avvio che ha sostituito il BIOS legacy, con cui una macchina può avviare da dischi partizionati in GPT e superare i limiti dello schema di avvio precedente.
