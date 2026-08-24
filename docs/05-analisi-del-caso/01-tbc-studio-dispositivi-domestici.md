# [TBC] Studio dispositivi domestici

> CENSIMENTO INCOMPLETO E ANONIMIZZATO. Diverse voci hanno solo l'intestazione; i nomi macchina, gli identificativi di dispositivo e i numeri di serie sono segnaposto secondo `.claude/rules/anonymization.md` e i valori reali vivono in `_notes/.anonymization-map.md`, non versionato. Vedi `../pendenze-aperte.md` per l'elenco delle voci da completare.

### Introduzione

Innanzitutto, anche se *Seven* supporta Wi-Fi 7 e teoricamente velocità wireless elevate, le velocità effettive sul Wi-Fi sono inferiori alla porta cablata 2,5 Gbit/s per via di limiti dei client e delle condizioni RF.

Con Fastweb Wi-Fi 7 dual band con tecnologia Multi-Link Operation (MLO): combina le bande 2.4GHz e 5GHz per darti connessioni più stabili e veloci, anche in condizioni estreme.
Copertura estesa, segnale costante in ogni angolo della casa [https://www.fastweb.it/myfastweb/seven/](https://www.fastweb.it/myfastweb/seven/).

Sul link dicono esplicitamente che “il livello massimo della velocità e segnale wireless è dato dalle specifiche dello standard IEEE 802.11. La velocità effettiva e la copertura wireless potrebbero variare e subire rallentamenti a causa di condizioni della rete e fattori ambientali, tra cui il volume del traffico di rete, limitazioni dei dispositivi collegati (es. numero di antenne), e struttura del fabbricato.”.

### PC (Windows, Linux)

Una domanda naturale è come si fa a vedere dentro Ubuntu o Windows la velocità massima di scambio della scheda di rete. In Windows basta andare nel Task Manager (CTRL + SHIFT + ESC) e selezionare la scheda Ethernet:

![](assets/img-0072.png)

A quel punto in alto a destra c’è scritto esplicitamente (es. in questo caso Realtek Gaming 2.5GbE Family Controller). Altrimenti c’è un comando powershell:

**Get**-NetAdapter | **Select** Name, LinkSpeed

Questa è la velocità di link negoziata tra la scheda e lo switch/router. In Ubuntu / Linux basta andare nel terminale (CTRL+ALT+T) e, se non si sa l’interfaccia, alternativamente *uno dei due* comandi:

**ip link
nmcli device show**

una volta letta qual è l’interfaccia:

ethtool eth0 | grep Speed

La “velocità massima” è *la velocità negoziata dal PHY*; quindi, la combinazione porta del router / switch, cavo e scheda di rete. Chiaramente se si collega un PC con NIC 2.5G alla porta 1G del Seven, la velocità negoziata sarà sempre 1 Gbps, anche se la scheda supporta 2.5G.

#### PC fisso 1 - Windows 11 Pro (forced)

##### Scheda(e) di rete

#### PC fisso 2 - Xubuntu

##### Scheda(e) di rete

#### PC fisso 3 - anduinOS

##### Scheda(e) di rete

#### PC fisso 4 - Windows 11 Pro (forced) - VHS converter

Riconsideriamo le specifiche hardware del PC, ovvero il processore i7-6700@3.40GHz, 16GB RAM, SSD 233GB (85% buono con report da CrystalDisk Info) di marca: Samsung850EvoM.2) e HDD 298GB - marca: Samsung HD322GJ.

Si può vedere inoltre da Impostazioni > sistema > Informazioni sul sistema si possono avere informazioni come:

- Nome dispositivo: DESKTOP-XXXXXXX
- Processore: Intel(R) Core(TM) i7-6700 CPU @ 3.40GHz 3.41 GHz
- RAM installata: 16,0 GB (15,9 GB utilizzabile)
- ID dispositivo: 00000000-0000-0000-0000-000000000000
- ID prodotto: XXXXX-XXXXX-XXXXX-XXXXX
- Tipo sistema: Sistema operativo a 64 bit, processore basato su x64

E per le specifiche Windows l’edizione è Windows 11 Pro - Versione: 24H2 - Data installazione: 26/09/2025 - Build sistema operativo: 26100.1742 - Esperienza: Windows Feature Experience Pack 1000.26100.18.0.

##### Scheda(e) di rete

#### PC fisso 5 - Firewall OPNsense

##### Scheda(e) di rete

#### [TBC] PC fisso 6 - Ubuntu Studio 25

##### Scheda(e) di rete

#### PC portatile 1 - Windows 11 Home (asus X513EAN)

##### Output di dxdiag windows

###### [TBC] System information

La prima parte dell’output del comando  è:

------------------
System Information
------------------
      Time of this report: 1/19/2026, 15:11:03
             Machine name: LAPTOP-XXXXXXX
               Machine Id: {00000000-0000-0000-0000-000000000000}
         Operating System: Windows 11 Home 64-bit (10.0, Build 26200) (26100.ge_release.240331-1435)
                 Language: English (Regional Setting: English)
      System Manufacturer: ASUSTeK COMPUTER INC.
             System Model: VivoBook_ASUSLaptop X513EAN_K513EA
                     BIOS: X513EAN.307 (type: UEFI)
                Processor: 11th Gen Intel(R) Core(TM) i5-1135G7 @ 2.40GHz (8 CPUs), ~2.4GHz
                   Memory: 8192MB RAM
      Available OS Memory: 7886MB RAM
                Page File: 10597MB used, 6505MB available
              Windows Dir: C:\WINDOWS
          DirectX Version: DirectX 12
      DX Setup Parameters: **Not** found
         User DPI Setting: 120 DPI (125 percent)
       System DPI Setting: 120 DPI (125 percent)
          DWM DPI Scaling: UnKnown
                 Miracast: Available, with HDCP
Microsoft Graphics Hybrid: **Not** Supported
 DirectX Database Version: 1.7.7
   Auto Super Res Version: Unknown
       System Mux Support: Mux Support Inactive - Ok
           Mux Target GPU: dGPU
    Mux Incompatible List:
           DxDiag Version: 10.00.26100.7309 64bit Unicode

###### Pulizia dei “problemi”

Lanciato in data 19/01/2025, L’output WER9 indica che Windows ha registrato un errore appartenente alla categoria WindowsWcpOtherFailure3, ossia un problema interno al Windows Component Platform (WCP) legato alla manutenzione e alla gestione del Component Store (il repository WinSxS da cui Windows recupera file di sistema, aggiornamenti e componenti durante operazioni come installazioni, riparazioni o aggiornamenti), e nello specifico il modulo che fallisce è la funzione ComponentStore::CRawStoreLayout::OpenComponentFile, richiamata nel file sorgente storelayout.cpp alla riga 2204, la quale tenta di aprire un file essenziale di un componente del sistema operativo ma non riesce a farlo, generando il codice d’errore 0x800F0983 (che indica file o payload mancanti, danneggiati o incoerenti all’interno del Component Store) e lasciando come informazione aggiuntiva il valore 0xADF53FDF, interpretabile come hash o riferimento interno associato al file o al componente coinvolto; l’insieme di queste condizioni suggerisce che Windows Update, DISM o altre operazioni di gestione dei componenti stessero accedendo a un file che non è più presente, è corrotto o non corrisponde alla struttura attesa, causando un fallimento non bloccante ma comunque anomalo che Windows registra come evento diagnostico di tipo 0 senza associare un fault bucket definitivo, mostrando che il problema è reale ma non classificato in un gruppo di errori noto.

Per risolvere in modo concreto e definitivo il problema segnalato da WindowsWcpOtherFailure3 con errore 0x800F0983, devi intervenire sul Component Store (WinSxS) perché l’errore indica chiaramente che Windows non riesce ad aprire uno dei file interni dei componenti di sistema, molto probabilmente perché è corrotto, mancante o incoerente rispetto alla struttura prevista. In ordine logico e con la procedura più efficace possibile, aprire Prompt dei comandi come amministratore ed eseguire questi tre comandi nell’ordine esatto:

DISM /Online /Cleanup-Image /CheckHealth
DISM /Online /Cleanup-Image /ScanHealth
DISM /Online /Cleanup-Image /RestoreHealth

Il terzo comando è quello che effettivamente ripara i file corrotti mancanti nel WinSxS usando copie locali oppure Windows Update. Inoltre, il classico comando:

sfc /scannow

corregge file di sistema che DISM ha reso nuovamente ripristinabili. Se il problema persiste c’è un comando per il controllo integrità WinSxS avanzato:

DISM /Online /Cleanup-Image /StartComponentCleanup

Questo elimina componenti obsoleti che possono creare incoerenze nei metadati del Component Store. L’errore 0x800F0983 può indicare che un aggiornamento cumulativo è incompleto, quindi si scarica l’update corrispondente alla build dal catalogo Microsoft e si installa manualmente.

##### Scheda(e) di rete

#### PC portatile 2 - Ubuntu 24.04 LTS (asus)

Il PC è il vecchio PC Asus F550CC-XX698H (SN: <sn-portatile-2>, CN: <cn-portatile-2>). Il PC Asus F550CC-XX698H è un laptop consumer di fascia media, caratterizzato da un design standard in plastica con finitura opaca, uno schermo da 15,6 pollici con risoluzione HD 1366x768, processore Intel Core i3 di terza generazione, 4 GB di RAM DDR3 espandibili e un disco rigido da 500 GB a 5400 RPM. Il sistema operativo originale è Windows 8, aggiornabile a versioni successive di Windows, e la macchina dispone di un insieme di porte sufficienti per uso quotidiano: USB 2.0 e 3.0, HDMI, VGA, lettore schede SD e jack audio combinato. La batteria è integrata agli ioni di litio da circa 37 Wh, con autonomia ridotta se sottoposta a carichi elevati o multitasking intensivo. Il raffreddamento è affidato a un singolo heatpipe con ventola e il case presenta un layout tipico Asus, con tasti isolati e touchpad multitouch. Il peso si aggira attorno ai 2,3 kg, rendendolo portabile ma non leggerissimo. Il notebook supporta connettività wireless standard e Bluetooth integrato per periferiche. La scheda grafica dedicata è una NVIDIA GeForce GT 720M con 2 GB di VRAM DDR3, adatta a carichi grafici leggeri e giochi datati.

##### Scheda(e) di rete

La scheda di rete wireless integrata è una Intel Centrino Wireless-N 2230, che supporta standard 802.11b/g/n con banda a 2,4 GHz e velocità fino a 300 Mbps, compatibile con WEP, WPA e WPA2. Non è presente supporto nativo per Wi-Fi a 5 GHz.

Il dispositivo dispone anche di una scheda Ethernet Realtek PCIe GBE Family Controller, che consente connessioni cablate fino a 1 Gbps, con funzionalità di Wake-on-LAN e gestione avanzata del traffico tramite driver Realtek. La gestione delle interfacce di rete è affidabile e stabile, con latenze ridotte su LAN cablata e buona sensibilità del modulo Wi-Fi su segnali standard indoor.

#### PC portatile 3 - macOS

Il PC è il vecchio macOS Monterey versione 12.7.6, quindi un MacBook Air (13-inch, 2017) con:

- Processore: 1,8 GHz Intel Core i5 dual-core
- Memoria: 8GB 1600 MHz DDR3
- Scheda grafica: Intel HD Graphics 6000 1536 MC
- Numero di serie: <sn-macbook>

Come si può vedere dall’interno del sistema operativo:

![](assets/img-0073.png)

Il MacBook Air 13-inch del 2017 con macOS Monterey 12.7.6 è un laptop ultrasottile orientato alla mobilità e all’efficienza energetica, con chassis unibody in alluminio spazzolato.

Il processore Intel Core i5 dual-core a 1,8 GHz, supportato da 8 GB di RAM DDR3 a 1600 MHz, garantisce prestazioni adeguate per attività quotidiane, navigazione, produttività e multitasking leggero, mentre la Intel HD Graphics 6000 con 1536 MB di memoria condivisa gestisce elaborazioni grafiche di base, rendering video leggero e output su display esterni fino a risoluzioni 2560x1600.

Il dispositivo integra un SSD da 128 o 256 GB NVMe, offrendo tempi di accesso rapidi e avvio immediato del sistema operativo. Lo schermo da 13,3 pollici con retroilluminazione LED presenta un’ottima resa cromatica e angoli di visione ampi. La batteria integrata da 54 Wh assicura autonomie superiori alle 10 ore in uso standard. Il layout della tastiera è a farfalla con tasti retroilluminati, il trackpad è Force Touch con rilevamento della pressione, e la connettività fisica è limitata a due porte USB 3.0, Thunderbolt 2 e jack audio combinato. Il sistema è complessivamente leggero, con peso di circa 1,35 kg, e garantisce un’esperienza macOS fluida e coerente.

##### Scheda(e) di rete

La scheda di rete wireless integrata è una Broadcom BCM4360 802.11ac che supporta dual-band a 2,4 e 5 GHz, velocità fino a 867 Mbps e protocolli WPA/WPA2. Il modulo Wi-Fi garantisce latenza contenuta e ottima stabilità in ambienti con più reti vicine, con roaming fluido tra access point compatibili.

La scheda Ethernet non è presente, ma la connettività cablata è ottenibile tramite adattatori Thunderbolt a Gigabit Ethernet, consentendo collegamenti stabili fino a 1 Gbps. Il Bluetooth integrato 4.0 gestisce periferiche wireless con basso consumo energetico e bassa latenza.

#### PC portatile 4 - …………… (Lenovo)

……………………………….

##### Scheda(e) di rete

La scheda di rete wireless

### PS5

La PlayStation 5 standard è una console di gioco di nuova generazione progettata per offrire prestazioni elevate in ambito gaming, con supporto per risoluzioni fino a 4K nativo e frequenze di aggiornamento fino a 120 Hz, ray tracing hardware, e architettura basata su CPU AMD Ryzen Zen 2 a 8 core da 3,5 GHz con GPU AMD RDNA 2 personalizzata da 10,28 TFLOPS.

Il sistema include 16 GB di RAM GDDR6 a 448 GB/s e un SSD NVMe da 825 GB con velocità di lettura sequenziale fino a 5,5 GB/s, garantendo caricamenti quasi istantanei. La console integra un sistema di raffreddamento ibrido con ventola radiale e dissipatore a liquido, e l’alimentatore interno gestisce picchi di potenza elevati senza degradazione delle prestazioni. Il lettore ottico UHD Blu-ray 4K consente la riproduzione di giochi fisici e film ad alta definizione.

Il design esterno è asimmetrico, con carenatura bianca e inserti neri, e la console supporta l’output audio 3D tramite Tempest Engine, fornendo immersione acustica avanzata. L’interfaccia utente è basata su un sistema operativo PlayStation OS ottimizzato, con aggiornamenti regolari per stabilità e compatibilità.

#### Scheda(e) di rete

Nello specifico, la PlayStation 5 (non Pro) ha queste specifiche di rete:

- Wi-Fi 6 (IEEE 802.11 a/b/g/n/ac/ax)
   - Frequenze: 2,4 GHz e 5 GHz
   - Velocità teorica massima Wi-Fi 6: oltre 1 Gbps (ma realisticamente, molto meno, soprattutto su 5 GHz a distanza o con muri)
- Porta Ethernet
   - Standard: 10/100/1000BASE-T (Gigabit Ethernet)
   - Velocità massima cablata: 1 Gbps (≈1000 Mbps)

Quindi la PS5 può sfruttare al massimo una connessione da 1 Gbps, sia via cavo sia (potenzialmente) via Wi-Fi, se il router è vicino e supporta Wi-Fi 6.

Quindi la scheda di rete wireless integrata è una soluzione Wi-Fi 6 (802.11ax) dual-band che supporta velocità teoriche fino a 1,2 Gbps, gestione avanzata di MU-MIMO e OFDMA per ridurre la latenza in ambienti congestionati, garantendo streaming stabile di giochi e download rapidi.

La console dispone anche di una porta Ethernet Gigabit RJ-45, utilizzabile per connessioni cablate a bassa latenza e massima stabilità, essenziale per sessioni multiplayer competitive e trasferimenti di dati ad alta velocità. Il Bluetooth 5.1 integrato consente l’uso di controller DualSense e periferiche wireless con latenza ridotta, gestione simultanea di più dispositivi e basso consumo energetico.

Per la PS5 per il gaming online 3-10 Mbps in download e 1-3 Mbps in upload bastano. Per il download giochi (molto pesanti, anche 100-150 GB) chiaramente più uno ha banda, meglio è. Per lo streaming o remote Play, 15-50 Mbps sono consigliati. Quindi, anche 100 Mbps sono più che sufficienti per giocare. Oltre 300-500 Mbps è utile solo se si scaricano giochi enormi frequentemente.

### TV

#### Analisi specifiche

### Persona-A

#### Analisi specifiche

### Samsung S25 Ultra

#### Analisi specifiche

#### …………

……….

#### …………

……….

### Sony Xperia III ………..

#### Analisi specifiche

### Samsung S20 FE 5G

#### Analisi specifiche

### Tablet Samsung vecchio

#### Analisi specifiche

### Tablet Samsung nuovo di Persona-B

#### Analisi specifiche

