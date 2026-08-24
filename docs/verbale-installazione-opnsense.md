# Verbale dell'installazione di OPNsense 25.7

> Documento curato, non generato dal documento sorgente. Trascrive e commenta le trentuno fotografie scattate durante la sessione di installazione del 16/01/2026, che nel `.docx` sono richiamate ma non incorporate. Le fotografie non sono versionate: vivono nella cartella locale `QuickShare_2601161748/`, esclusa dal `.gitignore` insieme a tutti i formati immagine. Questo file e' quindi l'unica traccia recuperabile da un clone di cio' che e' stato realmente fatto quel giorno.

## Perche' esiste

Il documento sorgente descrive l'installazione come procedura, cioe' come sequenza di scelte motivate. Le fotografie sono la prova che quella procedura e' stata eseguita e con quale esito, e contengono dati che nel testo non compaiono: il modello del disco, la sequenza reale del boot, l'esito dell'assignation delle interfacce, la durata complessiva della sessione. Distinguere il piano dall'esecuzione e' esattamente il confine fra un progetto documentato e un progetto realizzato, e senza questo verbale la distinzione andrebbe persa.

Vale l'avvertenza della regola di anonimizzazione sul materiale non versionato: le fotografie mostrano in chiaro numeri di serie di dischi e identificativi di macchina, e la trascrizione che segue li sostituisce con i segnaposto della mappa privata. Cio' che si legge su un monitor fotografato resta un dato reale, e trascriverlo in un file tracciato lo pubblicherebbe esattamente come lo pubblicherebbe la fotografia.

## Contesto della sessione

La macchina e' il PC con Intel i3 di settima generazione, 8 GB di RAM e SSD, con la scheda di rete gigabit integrata e due TP-Link TX201 a 2,5 Gbps su PCIe. L'immagine e' `OPNsense-25.7-vga-amd64`, scritta su chiavetta con Rufus 4.11.2285 dopo estrazione con 7-Zip e verifica del checksum SHA-256, come descritto in `03-spunti-di-sviluppo/10-firewall-before-the-switch/02-soluzione-professionale-con-opnsense-25-7.md`. Le fotografie coprono tre momenti separati, riconoscibili dagli orari: il boot dell'ambiente live intorno alle 16:37, la scelta della tastiera e l'avvio dell'installer intorno alle 16:51, e la configurazione ZFS con l'installazione vera e propria fra le 17:06 e le 17:39.

## Il boot dell'ambiente live

Le prime fotografie mostrano il kernel FreeBSD che enumera l'hardware. Il disco interno viene rilevato come `ada0`, un SSD SATA da circa 114 GB reali con trasferimenti a 600 MB/s in SATA 3.x, la chiavetta di installazione come `da0` su USB, e il lettore ottico come `cd0` in SATA 1.x. Compaiono due avvisi non bloccanti: `camcontrol: ATA_IDENTIFY via pass_16 failed` sul lettore ottico, che e' normale su unita' ATAPI, e `hostid: unable to figure out a UUID from DMI data`, che porta il sistema a generarne uno nuovo, comportamento atteso su hardware desktop generico privo di UUID nel firmware.

Il file system dell'immagine live risulta pulito e i controlli vengono saltati. Parte poi la catena di script di avvio di OPNsense, e qui c'e' l'unico esito degno di nota di tutta la fase: `Generating configuration: templates...failed`. E' un fallimento della generazione dei template nell'ambiente live, non nell'installazione su disco, e non impedisce il proseguimento; resta comunque un punto da riverificare sul sistema installato, ed e' registrato fra le pendenze.

Subito dopo il kernel segnala `re0: link state changed to UP`, cioe' la prima interfaccia Realtek che rileva il cavo collegato, e prosegue con il device manager: chipset Skylake PCH 100, controller SMBus Intel Sunrise Point-H, mouse ottico USB e tastiera USB. La configurazione dei servizi arriva in fondo con la sequenza completa, dal logging al firewall alle interfacce hardware, LAGG, VLAN e LAN, poi OpenSSH, la GUI web, il servizio DHCPv6, il router advertisement, Dnsmasq, Unbound DNS, il gateway monitor, le impostazioni OpenVPN e NTP.

## L'assignation nell'ambiente live

Una fotografia cattura il momento in cui l'installer chiede il nome dell'interfaccia LAN e riceve `re0`, mentre alla richiesta dell'interfaccia opzionale numero uno non viene indicato nulla. Il riepilogo conferma una sola assegnazione, `LAN -> re0`, e la conferma viene data.

Questo e' il fatto piu' importante del verbale, e va letto con attenzione perche' contraddice una lettura frettolosa del piano. Il documento sorgente descrive una topologia a tre zone, con una 2,5 GbE come WAN, l'altra come LAN e la gigabit integrata come DMZ. In questa sessione quella segmentazione non e' stata realizzata: e' stata assegnata una sola interfaccia, e nessuna WAN. La schermata finale dell'ambiente live lo conferma mostrando `LAN (re0) -> v4: 192.168.1.1/24`, cioe' il default di fabbrica di OPNsense, e nessun'altra interfaccia. La sessione del 16/01/2026 ha quindi installato il sistema, non configurato la rete, e l'assignation a tre zone resta da fare.

La stessa schermata riporta il fingerprint SHA-256 del certificato HTTPS e le tre chiavi host SSH generate, che non si trascrivono qui perche' sono identificatori crittografici di quella macchina, e la nota di benvenuto che indica le due credenziali dell'ambiente live, `root` per continuare in live mode e `installer` per avviare l'installazione. Viene usata `installer`.

## La scelta della tastiera

Tre fotografie mostrano la selezione del keymap nell'installer FreeBSD, con il cursore che scorre l'elenco fino a `Italian` e la selezione che si fissa. Segue la voce `Test it.kbd keymap`, e una fotografia mostra la casella di prova con una frase digitata per verificare che i caratteri corrispondano ai tasti; la frase contiene un nome proprio e non viene trascritta. La verifica ha esito positivo e si prosegue con `Continue with it.kbd keymap`.

## Il menu dell'installer e la scelta del filesystem

Il menu principale dell'installer di OPNsense 25.7 offre le due installazioni, ZFS e UFS, entrambe in variante GPT/UEFI Hybrid, piu' le modalita' estese, il caricamento di una configurazione, il recupero di un'installazione, il reset della password e le due uscite. Viene scelta `Install (ZFS)` con `ZFS GPT/UEFI Hybrid`, coerentemente con il razionale scritto nel documento sorgente: ZFS porta checksumming e protezione dalla corruzione logica anche su disco singolo, e la variante ibrida garantisce l'avvio sia in UEFI sia in modalita' legacy.

## La configurazione ZFS

La schermata `Select Virtual Device type` elenca le sei modalita' di pool, da `stripe` senza ridondanza fino a `raidz3` a tripla ridondanza. Con un solo disco l'unica scelta tecnicamente possibile e' `stripe`, ed e' quella presa.

La schermata successiva chiede quali dischi comporranno il pool e ne mostra uno solo: `ada0`, un `KINGSTON SA400S37120G`, cioe' un SSD SATA da 120 GB della serie A400. Il disco viene selezionato, e l'installer presenta l'avviso `Last Chance! Are you sure you want to destroy the current contents of the following disks: ada0`, al quale si risponde affermativamente.

Il modello del disco e' un dato utile che nel documento sorgente non compare: la serie A400 di quel produttore e' una linea entry-level senza DRAM cache, adeguata a un firewall che scrive log ma non la scelta migliore per longevita' sotto scrittura continua, e questo va tenuto presente quando si valutera' l'attivazione di logging esteso o di un IDS con molte regole.

## L'installazione e la chiusura

Parte la fase `Cloning current system`, con la doppia barra di avanzamento dell'installer. Al termine compare `Final Configuration`, che offre il cambio della password di root oppure il completamento; le fotografie mostrano prima la voce `Root Password` evidenziata e poi `Complete Install` selezionata, quindi la password di root e' stata gestita in quella schermata prima di confermare.

La schermata `Installation Complete` avverte che il sistema potrebbe riavviarsi dal supporto di installazione se non viene rimosso correttamente, e offre `Reboot now` oppure `Halt now`. Viene scelto lo spegnimento. Le ultime fotografie mostrano `The installation finished successfully`, il conto alla rovescia di cinque secondi, l'attesa dei processi `vnlru` e `syncer`, la sincronizzazione dei dischi e infine `All buffers synced. Uptime: 1h2m18s`.

L'uptime chiude il verbale con il dato piu' sintetico che contiene: dall'accensione allo spegnimento sono passate un'ora e due minuti, il che colloca l'inizio della sessione intorno alle 16:35 e conferma la sequenza degli orari delle fotografie.

## Che cosa resta da fare dopo questa sessione

Il sistema e' installato su ZFS in stripe su disco singolo, con keymap italiana, password di root impostata e una sola interfaccia assegnata come LAN sul default di fabbrica. Non sono state fatte l'identificazione fisica delle tre schede di rete con `pciconf -lv` e `ifconfig`, l'assignation a tre zone, la configurazione degli indirizzi delle interfacce, ne' alcuna regola firewall. Sono esattamente i passi descritti come da fare nelle sezioni marcate da chiarire sotto `03-spunti-di-sviluppo/10-firewall-before-the-switch/`, e sono riportati in `pendenze-aperte.md`.

Resta inoltre aperto l'avviso `Generating configuration: templates...failed` osservato nell'ambiente live, da riverificare sul sistema installato prima di considerare conclusa l'installazione.
