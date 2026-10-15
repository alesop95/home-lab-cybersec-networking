# Allocazione dell'hardware: ogni macchina e ogni pezzo, con la ragione

Ritorno allo [studio](README.md). Documento del 12/10/2026, chiesto dall'utente per avere in un posto solo dove va ogni pezzo che ha in mano e perché. È la fonte canonica dell'allocazione: dove il [piano unificato](10-piano-unificato-hardware-e-stack.md), le schede della [cartella NAS](../02-storage-di-rete-nas/README.md) o le decisioni precedenti dicono altro su memoria e dischi, vale questo documento. Le decisioni che lo fondano sono ADR-030, ADR-031, ADR-032, ADR-033 e, per il modello linguistico locale, ADR-034. Nulla è ancora montato: è la configurazione da raggiungere, non lo stato di fatto.

## Le macchine

| Macchina | Ruolo | Scheda e processore | Memoria | Dischi | Perché |
|---|---|---|---|---|---|
| NET-04 | firewall OPNsense | i3 di settima generazione | 8 GB | SSD 120 GB | installato il 16/01/2026, fuori da questa allocazione |
| `linux-desktop-A` | server Proxmox SRV-01, sempre acceso | ASRock H270M Pro4, i7-7700 | 24 GB DDR4 | i due NVMe da 1 TB, Crucial P2 e P3, in specchio ZFS, sistema e macchine virtuali | il processore più recente, la sola rete Intel, due alloggiamenti M.2 NVMe; è la macchina che scrive di continuo (ADR-030, ADR-033) |
| `PC-DESKTOP-A` | NAS TrueNAS SCALE | ASUS H170-PRO, i7-6700 | 16 GB DDR4 | avvio sul Kingston V300; dati in specchio sui due SSD SATA SanDisk e WD Blue | ripristino automatico dell'accensione, sei porte SATA; serve file su rete a 1 Gbit, che un SSD SATA già satura (ADR-016, ADR-026, ADR-033) |
| PC-03 con la sua Z97-P | nodo di laboratorio, banco di analisi e, se la misura lo giustifica, modello linguistico locale su CPU (ADR-034); acceso a richiesta | ASUS Z97-P, processore LGA1150 migliore fra i due | 32 GB DDR3 | Samsung 850 EVO M.2 per il sistema, già montato; disco meccanico da 500 GB per le prove | il carico che chiede memoria sta su una macchina fisica separata da quella che lo sorveglia (ADR-030); è l'unica con 32 GB, la soglia a cui i modelli medi di colibri girano dalla memoria ([studio](13-modello-linguistico-locale-su-cpu.md)) |
| `PC-DESKTOP-B` | scorta gemella del NAS | ASUS B150-PRO, i7-6700 | nessuna | nessuno | se muore la scheda del NAS, memoria e dischi del NAS si spostano qui: stesso socket, stessa memoria, stesso processore |
| `linux-desktop-B` | scorta del nodo di laboratorio | ASUS Z97-P, il processore LGA1150 che resta | nessuna | nessuno | stessa scheda del nodo di laboratorio |
| PC-02 | da svuotare e smaltire | serie P55, LGA1156 | quattro moduli DDR3 Kingston, ricambio del laboratorio | Kingston V300 al NAS, disco da 500 GB al laboratorio | piattaforma del 2010 senza ruolo (ADR-031) |
| `linux-desktop-C` | postazione Ubuntu Studio | | | | in esercizio, fuori dall'allocazione |

## I dischi

| Disco | Va in | Perché |
|---|---|---|
| Crucial P2, NVMe 1 TB | server, primo alloggiamento M.2 | torna nella macchina da cui era uscito; specchio con il P3 |
| Crucial P3, NVMe 1 TB | server, secondo alloggiamento M.2 | la H270M Pro4 ha due M.2 NVMe x4 (S103), quindi non serve l'adattatore |
| SanDisk SDSSDA240G, SATA 240 GB | NAS, dati, `SATA6G_1` | sano, usura nulla dal censimento; metà dello specchio dei dati |
| WD Blue 250 GB, SATA | NAS, dati, `SATA6G_2` | sano, usura nulla; altra metà dello specchio |
| Kingston V300, SATA 240 GB | NAS, avvio, `SATA6G_3` | il più debole va dove un guasto costa meno: se cede, si reinstalla e si ricarica il file di configurazione, e i dati restano sul pool |
| Samsung 850 EVO M.2 SATA 250 GB | nodo di laboratorio, dove già si trova | nessuno spostamento |
| Samsung HD502HJ, meccanico 500 GB | nodo di laboratorio | quindici anni, adatto alle sole prove |

## La memoria

| Moduli | Vanno in | Perché |
|---|---|---|
| 2 × 8 GB DDR4 TEAMGROUP già nella base | NAS, 16 GB | TrueNAS chiede almeno 8 GB fino a otto dischi (S102); il NAS non ospita applicazioni (ADR-032) |
| 2 × 8 GB DDR4 TEAMGROUP prelevati da `PC-DESKTOP-B` | server | con due dei suoi moduli da 4 GB fanno 24 GB, un 8 e un 4 per canale |
| 2 dei 4 moduli Crucial da 4 GB DDR4 | server | |
| 2 moduli Crucial da 4 GB DDR4 | scorta | ridanno 16 GB al NAS se un suo modulo si guasta |
| 2 × 8 GB DDR3 di PC-03 e 2 × 8 GB DDR3 di `linux-desktop-B` | nodo di laboratorio, 32 GB | il tetto della Z97-P |
| 4 moduli DDR3 Kingston di PC-02, 2 × 2 GB e 2 × 4 GB | busta delle scorte | ricambio a capacità ridotta del laboratorio, 12 GB in tutto, taglie lette il 15/10/2026 |

## Gli acquisti

Nessuno è necessario per far partire le tre macchine. L'adattatore da PCIe a M.2 non serve più, perché i due NVMe stanno nel server. La scheda di rete Intel per il NAS resta subordinata alla prova di trasferimento sulla Realtek. Due dischi meccanici CMR in specchio si comprano quando i dati del NAS si avvicinano al limite qui sotto. Restano fuori da questo documento gli acquisti di rete già decisi, cioè switch e access point.

## I limiti accettati, scritti per non scoprirli dopo

Il NAS parte con circa 223 GB utili, cioè circa 180 GB pianificabili con la regola dell'ottanta per cento. Bastano per i documenti di casa e per alcune copie compresse delle macchine virtuali del server, che è un'inferenza da verificare sulla prima copia reale; non bastano per un archivio di foto e video. Quando servirà più spazio, due dischi meccanici in specchio diventano un secondo pool senza reinstallare. Il V300 ha poche scritture garantite, ma come disco di avvio scrive poco. L'avvio del NAS non è in specchio: un guasto del disco di avvio ferma il NAS per il tempo di una reinstallazione e del caricamento della configurazione, che va quindi esportata dopo ogni modifica. Il server conserva le copie delle sue macchine virtuali sul NAS, cioè su un'altra macchina.

## L'ordine dei gesti al banco

Il principio è montare per prime le due macchine che non richiedono pasta termica, perché la pasta serve solo dove si toglie un dissipatore da rimontare.

| Passo | Che cosa si fa |
|---|---|
| 1 | PC-02: estrarre il V300, il disco da 500 GB, i cavi dati SATA, la minuteria e i due moduli DDR3 ancora inseriti, leggendone la taglia; guardare la scheda grafica. Fatto il 15/10/2026 secondo le foto: fuori anche l'alimentatore Tecnoware, moduli 2 × 2 GB e 2 × 4 GB, scheda grafica GeForce 210 da 1 GB ancora nel case |
| 2 | NAS: SanDisk su `SATA6G_1`, WD Blue su `SATA6G_2`, V300 su `SATA6G_3`, ciascuno con cavo dati e alimentazione; contare che l'alimentatore abbia tre connettori SATA; memoria e M.2 non si toccano |
| 3 | NAS: primo avvio a case aperto, firmware secondo la guida, +12 V fra 11,4 e 12,6 V, memoria a 16 GB, tre dischi visibili; test della memoria una notte |
| 4 | NAS: installazione di TrueNAS sul solo V300, pool in specchio su SanDisk e WD Blue, test SMART lungo dalla shell, esportazione della configurazione |
| 5 | server: togliere due moduli da 4 GB e montare i due da 8 GB, un 8 e un 4 per canale secondo il manuale; P2 e P3 nei due alloggiamenti M.2 |
| 6 | server: firmware con virtualizzazione attiva, 24 GB, due NVMe visibili; test della memoria una notte; installazione di Proxmox su ZFS in specchio sui due NVMe |
| 7 | procurare la pasta termica |
| 8 | PC-03: pulizia, sigla del processore, alloggiamento da tre pollici e mezzo; confronto con il processore di `linux-desktop-B` e scambio se conviene |
| 9 | nodo di laboratorio: i due moduli DDR3 di `linux-desktop-B` per 32 GB, il disco da 500 GB, l'alimentatore migliore fra quello di PC-03 e il Tecnoware di PC-02 |
| 10 | SMART lungo sui dischi del laboratorio; consumo a riposo delle tre macchine con una presa wattmetrica |
| 11 | conferimento di scheda, processore e case di PC-02, solo dopo il passo 8 |
| 12 | facoltativo, quando si vuole: misura di colibri sul nodo di laboratorio, con la soglia fissata nel [suo studio](13-modello-linguistico-locale-su-cpu.md) |
