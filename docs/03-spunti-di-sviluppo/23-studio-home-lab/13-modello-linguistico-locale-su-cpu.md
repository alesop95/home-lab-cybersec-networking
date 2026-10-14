# Modello linguistico locale su CPU: colibri sull'hardware di casa

Ritorno allo [studio](README.md). Studio del 13/10/2026, nato da una segnalazione dell'utente: il progetto [colibri](https://github.com/JustVugg/colibri) promette di eseguire modelli linguistici molto grandi sui PC che si hanno già, senza scheda grafica. La domanda era se i 16 o i 32 GB di memoria che la casa può comporre bastino, e dove metterlo dentro il piano. Fonti S104 e S105 del [registro](../../../SOURCES.md). Nulla è installato e nessun numero di velocità sulle macchine di casa è misurato: quelli scritti qui sono stime dichiarate come tali, da sostituire con la misura descritta più avanti.

Stato al 13/10/2026: la collocazione è decisa dall'utente (ADR-034), cioè colibri sul nodo di laboratorio PC-03, nella VLAN 60, acceso solo quando serve, senza costo e senza cambiare l'ordine della roadmap. Resta subordinato alla misura che decide se tenerlo. Lo studio di un'espansione con una scheda grafica è rimandato a un documento futuro, di cui la penultima sezione elenca le domande. Chi riprende in mano il tema parte dalla sezione «Da dove si riparte», in fondo.

## Che cosa fa, e perché cambia una premessa del piano

Fino al 12/10/2026 il piano diceva che un modello linguistico locale chiede una GPU moderna, e lo rimandava a una macchina dedicata da comprare, fuori dalla roadmap. colibri toglie quella premessa per una classe precisa di modelli. Un modello *mixture of experts*[^1] di decine o centinaia di miliardi di parametri ne usa solo una piccola parte per ogni token: colibri tiene in memoria la parte che serve sempre, cioè attenzione, esperti condivisi ed embedding, e legge dal disco gli esperti che il modello chiama, con una cache che impara quali servono di più (S104). È scritto in C, senza dipendenze, e la compilazione predefinita su x86 chiede le istruzioni AVX2 (S104, Makefile del motore); la GPU è facoltativa e serve solo ad andare più veloci. Espone un'interfaccia compatibile con quella di OpenAI e con quella di Anthropic, ascolta per impostazione predefinita sul solo indirizzo locale e accetta una chiave con `COLI_API_KEY`, senza la quale non chiede credenziali (S104).

Il progetto è nato il 01/07/2026, da un autore italiano a titolo individuale, con licenza Apache-2.0; il 13/10/2026 aveva circa 41.700 stelle e un aggiornamento nello stesso giorno. È giovane e cambia ogni giorno, che per uno strumento da laboratorio è accettabile e per un servizio no.

## Che cosa ci sta in 16 e in 32 GB

Il catalogo di colibri dà per ogni modello due numeri di memoria: sotto il primo il modello non parte, dal secondo gira come misurato dall'autore (S104). In mezzo parte, ma legge dal disco una parte maggiore degli esperti, e la velocità scende verso quella del disco.

| Modello | Scaricamento | Memoria, minimo e piena | Con 16 GB | Con 32 GB |
|---|---|---|---|---|
| Qwen3.6-35B-A3B, conversazione con ragionamento e strumenti | 23 GB | 10 / 20 GB | parte, legge esperti dal disco | gira dalla memoria, con circa 12 GB di margine |
| Qwen3-Coder-30B-A3B, codice | 19 GB | 8 / 18 GB | parte, legge esperti dal disco | gira dalla memoria |
| OLMoE 7B, per imparare lo strumento | 14 GB, 7 dopo la conversione | 8 GB | gira | gira |
| DeepSeek V4 Flash, 284B | 167 GB | 16 / 32 GB | parte, inservibile | parte, ma tutto il peso è sul disco |
| GLM-5.2, 744B | 429 GB | 16 / 24 GB | non sta su nessun disco di casa | non sta su nessun disco di casa |

La risposta alla domanda dell'utente è quindi che 32 GB fanno al caso, 16 no: con 32 GB i due modelli medi girano interamente dalla memoria, con 16 GB partono ma dipendono dal disco. I modelli grandi, quelli che danno il nome al progetto, non sono alla portata della casa per un motivo che non è la memoria ma il disco: la loro velocità la decide la lettura degli esperti, e la tabella delle prove riporta per GLM-5.2 0,10 token al secondo su un Crucial P3 Gen3 a 1,51 GB/s, su un processore molto più recente dei nostri (S105). Lo stesso disco è uno dei due NVMe del server, e i dischi del nodo di laboratorio sono SATA, circa tre volte più lenti; il più grande dei dischi liberi è da 500 GB e meccanico.

## Quanto andrebbe veloce: stima, non misura

L'unico riferimento diretto è la macchina A dell'autore, un Ryzen 7 PRO 8700GE a otto core con DDR5: Qwen3.6-35B-A3B decodifica a 6,0 token al secondo sul solo processore, e un prompt di 512 token richiede 35,7 secondi prima della risposta (S104). Il processore del nodo di laboratorio, nel caso migliore l'i7-4790 a quattro core con DDR3-1333, ha metà dei core, non ha le istruzioni VNNI che accelerano i prodotti fra interi e ha circa un quarto della banda di memoria della DDR5. La stima, che è un'inferenza da questi rapporti e non un dato, è fra 1 e 2 token al secondo, con alcuni minuti di attesa su un prompt lungo. Il server, con un i7 di settima generazione e DDR4-2400, starebbe poco sopra, nello stesso ordine di grandezza.

A quella velocità una risposta di trecento parole richiede alcuni minuti, quindi il modello serve per lavori che si lanciano e si ritirano dopo. È adatto a ciò che il progetto chiede a un modello locale, cioè leggere dati che non devono uscire di casa senza fretta: l'analisi dell'uscita di una scansione, come nello studio [METATRON](../16-va-e-pentesting/03-metatron-pentesting-assistito-da-llm-locale.md), oppure il riassunto notturno degli allarmi di Wazuh. Che METATRON accetti un'interfaccia compatibile OpenAI al posto del proprio motore non è verificato.

## Dove va, considerando il tutto

Decisione dell'utente del 13/10/2026, ADR-034, su proposta dell'agente. Sul nodo di laboratorio, la Z97-P di PC-03 a 32 GB DDR3, acceso a richiesta, nella VLAN 60. Le ragioni sono quattro e vengono tutte da decisioni già prese. È l'unica macchina di casa con 32 GB, cioè l'unica su cui i modelli medi girano dalla memoria. È accesa solo quando serve, e un carico che satura i quattro core per minuti non deve stare sul server che ospita il monitoraggio: è lo stesso principio per cui ADR-030 ha separato il laboratorio dalla macchina che lo sorveglia. La VLAN 60 non ha uscita verso Internet salvo aperture a tempo (ADR-025), e un modello che lavora senza rete è esattamente il caso d'uso: lo si scarica una volta, in un'apertura a tempo, e poi i dati che legge non escono. E non costa nulla, perché il nodo si assembla comunque al passo 9 dell'[allocazione](12-allocazione-dell-hardware.md).

Gli scarti, con la ragione. Il server Proxmox ha il processore più veloce e i dischi NVMe, ma con Wazuh a 8 GB e Proxmox a 2 GB gli restano circa 12 GB, sotto i 20 che Qwen3.6 chiede per girare dalla memoria, e l'inferenza toglierebbe processore al monitoraggio; torna in discussione solo se un giorno il server sale a 64 GB comprando DDR4. Il NAS ha 16 GB e per ADR-032 non ospita applicazioni. Le due scorte non hanno memoria. La GPU non entra nel conto: colibri chiede Vulkan 1.2, il modello della scheda grafica di PC-02 si legge solo al passo 1 e, per una piattaforma del 2010, è probabile che non lo supporti, e la grafica integrata di quarta generazione non compare fra le misure del progetto; sono inferenze, e il nodo si valuta sul solo processore. La postazione da cui l'utente lavora al progetto avrebbe di gran lunga le risorse migliori, ma non fa parte della rete di casa e resta fuori dal computo, come deciso il 09/10/2026.

Due vincoli seguono dalla collocazione. Il nodo ha anche il ruolo di banco di analisi dei campioni, e i due usi vogliono entrambi tutta la memoria: si alternano, non convivono, e durante l'analisi di un campione il modello è spento. E il processore conta: la compilazione predefinita chiede AVX2, che tutti gli i5 e gli i7 di quarta generazione hanno e i Pentium e i Celeron della stessa serie no. Il processore di PC-03 non è ancora letto; l'i7-4790 di `linux-desktop-B` ha AVX2 (S101), ed è un motivo in più per lo scambio previsto al passo 8 dell'allocazione se il processore di PC-03 risultasse inferiore.

## Le cautele, per un laboratorio di sicurezza

Lo strumento si compila dai sorgenti a una revisione fissata, non si prende l'ultima a ogni avvio. L'interfaccia si espone solo con `COLI_API_KEY` impostata, e solo verso la postazione di amministrazione con una regola puntuale del firewall, non verso la VLAN 10. I pesi dei modelli si scaricano da Hugging Face durante un'apertura a tempo e portano ciascuno la propria licenza, da leggere prima dell'uso: il Qwen-Image-2.1 dello stesso catalogo, per esempio, è dichiarato non commerciale (S104). Il registro d'uso degli esperti che colibri scrive su disco descrive che cosa si è chiesto al modello, e va trattato come i dati che il modello ha letto.

## La misura che decide

Qui la versione breve; quella passo per passo, con i comandi, è nella sezione «La misura, passo per passo». Un pomeriggio, dopo il passo 10 dell'allocazione, con il nodo già assemblato e la presa wattmetrica già sul banco, e senza bisogno che la rete nuova esista: per lo scaricamento basta la rete di oggi. Si compila colibri, si scaricano Qwen3.6-35B-A3B e OLMoE, si lascia che `coli tune` misuri le impostazioni della macchina, e si annotano quattro numeri: token al secondo in decodifica a cache calda, secondi di attesa su un prompt di 512 token, memoria residente, e consumo alla presa durante l'inferenza. Il consumo a riposo del nodo si misura comunque al passo 10, quindi la seconda lettura costa un minuto.

La soglia per tenerlo la si fissa prima di misurare, per non adattarla al risultato: almeno 2 token al secondo su Qwen3.6, e un'attesa sotto i tre minuti sul prompt di prova. Sopra la soglia diventa uno strumento del laboratorio nella VLAN 60, al servizio della fase di verifica di sicurezza. Sotto la soglia si archivia questo studio con i numeri misurati, e l'idea della macchina dedicata con GPU torna fuori dalla roadmap com'era.

## Spiegato da zero: le parole di questo studio

Questa sezione è scritta per chi non ha mai fatto girare un modello linguistico, su richiesta dell'utente del 13/10/2026 di tracciare ogni passaggio tecnico come se non ne conoscesse nessuno. Ogni riga dice che cos'è la cosa e perché conta qui.

| Parola | Che cos'è | Perché conta in questo studio |
|---|---|---|
| modello linguistico | un programma addestrato a continuare un testo; è un file molto grande di numeri, i *pesi*, più un motore che li usa | colibri è il motore; Qwen3.6-35B-A3B è il modello, cioè il file di pesi che si scarica |
| parametro | uno dei numeri che compongono il modello; «35B» vuol dire 35 miliardi | più parametri vuol dire, di solito, risposte migliori e più memoria occupata |
| token | il pezzo di testo che il modello produce a ogni passo, in media tre quarti di parola | la velocità si misura in token al secondo: a 2 token al secondo una risposta di trecento parole richiede poco più di tre minuti |
| decodifica | la fase in cui il modello scrive la risposta, un token dopo l'altro | è il primo dei due numeri da misurare |
| elaborazione del prompt | la fase prima della risposta, in cui il modello legge la domanda e il testo allegato | su un processore vecchio è lunga: è il secondo numero da misurare, l'attesa prima che compaia la prima parola |
| *mixture of experts* | un modello diviso in tante sottoreti, gli *esperti*, di cui solo poche lavorano per ogni token | è il trucco che rende possibile colibri: «A3B» nel nome vuol dire che per ogni token lavorano circa 3 miliardi di parametri su 35 |
| quantizzazione int4 | i pesi salvati con 4 bit l'uno invece di 16, cioè in un quarto dello spazio, con una piccola perdita di qualità | è il motivo per cui un modello da 35 miliardi di parametri si scarica in 23 GB |
| memoria, o RAM | dove il processore tiene i dati su cui lavora; veloce, ma si svuota allo spegnimento | se il modello sta tutto in memoria va alla velocità della memoria; se no aspetta il disco |
| disco, SSD SATA e NVMe | dove i file restano a macchina spenta; un SSD SATA legge circa 0,5 GB al secondo, un NVMe come il P3 da 1,5 a più di 3 | i modelli grandi leggono dal disco a ogni token, e il disco ne decide la velocità |
| cache | la parte della memoria che tiene una copia dei dati letti dal disco, per non rileggerli | a «cache calda» il modello è già in memoria; a «cache fredda» lo deve ancora leggere, e va più piano |
| AVX2 | un insieme di istruzioni del processore che fanno molti calcoli in un colpo solo; esiste dal 2013 negli i3, i5 e i7, non nei Pentium e nei Celeron | colibri, compilato nel modo predefinito, non parte senza |
| VNNI | istruzioni più recenti, dedicate ai prodotti fra numeri interi | i processori di casa non le hanno, ed è una delle ragioni per cui la stima è più bassa dei numeri dell'autore |
| banda di memoria | quanti GB al secondo il processore riesce a leggere dalla memoria; la DDR3-1333 a doppio canale ne dà al massimo circa 21, la DDR5 circa quattro volte tanto | nella decodifica il processore rilegge i pesi attivi a ogni token, e la banda fa da tetto |
| GPU, scheda grafica | un processore con migliaia di unità di calcolo semplici, molto più veloce sui calcoli di un modello | con colibri è facoltativa; con una GPU recente la stessa Qwen3.6 sale a circa 30 token al secondo (S104) |
| Vulkan | un'interfaccia standard con cui un programma usa una GPU di qualunque marca | colibri la chiede in versione 1.2 per usare la GPU; le schede vecchie spesso non la hanno |
| interfaccia compatibile OpenAI | un modo standard di parlare al modello attraverso la rete, lo stesso dei servizi commerciali | molti programmi, forse anche METATRON, possono usare colibri senza modifiche puntando a quell'indirizzo |
| chiave dell'interfaccia | una parola segreta che il programma deve presentare per essere servito; in colibri si imposta con `COLI_API_KEY` | senza chiave chiunque raggiunga l'indirizzo può usare il modello |
| VLAN 60 | la zona di rete del laboratorio, separata dalle altre dal firewall e senza uscita verso Internet salvo aperture a tempo (ADR-025) | il modello lavora senza rete, quindi ciò che gli si fa leggere non esce di casa |
| presa wattmetrica | una presa che si mette fra la spina e il muro e mostra quanti watt passano | serve a sapere quanto costa in corrente un'ora di modello acceso |

## Come è stato fatto questo studio, passo per passo

Il 13/10/2026 l'agente ha letto la pagina principale del progetto su GitHub e poi, per non fidarsi di un riassunto, ha scaricato il file README completo e ne ha letto le sezioni su requisiti, catalogo dei modelli, GPU, installazione e comandi. Ha letto i metadati del repository con l'interfaccia di GitHub, da cui vengono la data di nascita del 01/07/2026, la licenza e il numero di stelle. Ha cercato nel Makefile del motore, il file che dice al compilatore come costruire il programma, quali istruzioni del processore richieda, trovando la riga che fissa come predefinito il livello x86-64-v3, che comprende AVX2. Ha letto la pagina sull'interfaccia di rete, da cui vengono l'ascolto predefinito sul solo indirizzo locale e la chiave `COLI_API_KEY`, e la tabella delle prove della comunità, da cui viene il dato del Crucial P3. Ha letto infine il protocollo di misura del progetto e l'intestazione dello strumento `c/tools/datapoint.py`, da cui viene la procedura della sezione seguente.

Ha poi confrontato quei requisiti con l'[allocazione](12-allocazione-dell-hardware.md) macchina per macchina: memoria libera, dischi, processore, ruolo e zona di rete. La stima di velocità viene da un confronto in proporzione con la macchina dell'autore, su tre rapporti: numero di core, presenza delle istruzioni VNNI e banda di memoria. Per questo è un'inferenza e non un dato, e la misura la sostituirà.

## La misura, passo per passo

Si fa sul nodo di laboratorio già assemblato, cioè dopo i passi 8, 9 e 10 dell'[allocazione](12-allocazione-dell-hardware.md), con un sistema Linux Debian o Ubuntu installato sul Samsung 850 EVO e il nodo collegato con un cavo alla rete di oggi, che serve solo per scaricare. I comandi sono per il terminale di quella macchina, uno per riga.

Primo, si controlla che il processore abbia AVX2. Il comando stampa la parola `avx2` se c'è, e niente se manca: in quel caso ci si ferma, perché colibri non partirebbe, e si valuta lo scambio con l'i7-4790 di `linux-desktop-B`.

```bash
grep -o -w avx2 /proc/cpuinfo | head -1
```

Secondo, si controllano memoria e disco. Il primo comando deve mostrare circa 31 GB alla voce totale, perché una parte dei 32 la tiene la scheda; il secondo deve mostrare almeno 45 GB liberi, cioè 23 per Qwen3.6, 14 per OLMoE e il resto per il programma.

```bash
free -g
df -h /
```

Terzo, si installano gli strumenti di compilazione, si scarica colibri e si annota la revisione esatta, così che la misura dica su quale versione è stata presa.

```bash
sudo apt install git python3 build-essential
git clone https://github.com/JustVugg/colibri
cd colibri
git rev-parse --short HEAD
```

Quarto, si lancia lo script di avvio, che guarda la macchina, consiglia un modello, compila il motore e scarica i pesi; si accetta Qwen3.6-35B-A3B. Lo scaricamento di 23 GB si può interrompere e riprendere. Alla fine lo script avvia il modello e stampa l'indirizzo locale; si chiude con Ctrl+C e si annota la cartella in cui ha messo il modello, che qui sotto si chiama `CARTELLA_MODELLO`.

```bash
./start-here.sh
```

Quinto, dalla cartella `c`, si chiede a colibri se è tutto pronto, dove terrà il modello e quali impostazioni sono le più veloci su questa macchina. La seconda risposta deve dire che il modello sta tutto in memoria; se dice che legge dal disco, la memoria non basta e il motivo va capito prima di misurare.

```bash
cd c
./coli doctor --model CARTELLA_MODELLO
./coli plan --model CARTELLA_MODELLO
./coli tune --model CARTELLA_MODELLO
```

Sesto, la misura vera, con lo strumento standard del progetto. Fa una richiesta a cache fredda, una a cache calda e alcune con domande diverse, e riporta i token al secondo in decodifica, la quota di esperti trovati in memoria e la memoria occupata. Si annotano tutte e tre le righe, perché un numero a cache calda senza l'etichetta non dice la velocità vera del disco (S105). Le opzioni dello strumento sono state lette dalla sua intestazione e non provate: se il comando si lamenta, `--help` le elenca.

```bash
python3 tools/datapoint.py --snap CARTELLA_MODELLO
```

Settimo, l'attesa sul prompt lungo, che lo strumento non dà come numero a sé. Si avvia la conversazione, si incolla un testo di circa quattrocento parole con una domanda in fondo, e si misura con un cronometro il tempo fino alla prima parola della risposta. Durante l'attesa si legge la presa wattmetrica: è il consumo sotto carico.

```bash
./coli chat --model CARTELLA_MODELLO
```

I numeri si scrivono in questo documento, al posto della stima, con la data, la revisione di colibri e lo stato della cache, e si confrontano con la soglia: almeno 2 token al secondo e meno di tre minuti di attesa. OLMoE si misura dopo, con lo stesso comando del sesto passo, solo come confronto.

## Lo studio futuro: un'espansione con la GPU

Deciso dall'utente il 13/10/2026: un giorno si farà uno studio di espansione con una scheda grafica, in un documento a sé. Non è nella sequenza delle fasi e non ha una data. Le domande che dovrà chiudere sono già scritte qui, perché le ha aperte questo studio. Dove montarla: la scheda andrebbe nello slot PCIe principale del nodo di laboratorio, e l'alimentatore, da scegliere al passo 9 fra quello di PC-03 e il Tecnoware, deve reggerne il consumo e averne i connettori. Quanta memoria video serve: con colibri anche una scheda da 8 GB tiene le parti più usate del modello, e il progetto riporta circa 30 token al secondo con una RTX 3070 (S104), contro la stima di 1 o 2 sul solo processore. Quanto costa, all'acquisto e in corrente, con la presa wattmetrica. E se la misura di questo studio va sotto la soglia, se la GPU basti a superarla o se serva una macchina diversa.

## Da dove si riparte

Al 13/10/2026 lo studio è chiuso sulla carta: collocazione decisa (ADR-034), soglia fissata, procedura scritta, studio della GPU rimandato con le sue domande. Il passo che manca è fisico e non urgente: la misura della sezione «La misura, passo per passo», che si fa solo a nodo di laboratorio assemblato, cioè dopo i passi da 1 a 10 dell'[allocazione](12-allocazione-dell-hardware.md). Nel frattempo il lavoro di casa riparte dal banco del NAS, gesto 1: aprire PC-02 ed estrarre il Kingston V300 e il disco da 500 GB.

[^1]: *MoE*, mixture of experts: architettura in cui ogni strato contiene molte sottoreti, gli esperti, e un instradatore ne attiva solo poche per ciascun token, così che il costo di calcolo per token sia una frazione del totale dei parametri.
