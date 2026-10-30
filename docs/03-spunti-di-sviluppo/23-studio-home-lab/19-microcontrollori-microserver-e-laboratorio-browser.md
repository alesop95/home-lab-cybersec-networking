# Microcontrollori, microserver e laboratorio nel browser

Studio richiesto il29/10/2026, ADR-047. Integra lo [studio17 sull’assistente](17-assistente-personale-hermes-nix-e-memoria.md) e la [matrice dei bisogni](16-bisogni-controlli-e-flussi.md). Sono direzioni di progetto e candidati da confrontare: nessuna scheda acquistata, assegnata o configurata; nessun consumo reale misurato. Fonti S269-S276 e S282/S284 nel [registro](../../../SOURCES.md).

## Prima il compito, poi il processore

Un microcontrollore esegue firmware per leggere un sensore, pubblicare un messaggio, comandare un relè o mostrare un risultato. Può avere un piccolo server HTTP senza essere un computer Linux. Il microserver dell’assistente deve invece sostenere il runtime dell’agente, archivio persistente, dipendenze, accesso remoto e aggiornamenti del sistema. Un modello remoto riduce il lavoro di inferenza locale; non elimina il runtime e lo stato di Hermes. Nix/NixOS e Tailscale dello studio17 appartengono al piano dell’host compatibile, senza presumere che siano installabili sul firmware di una MCU[^1].

| Famiglia candidata | Impiego utile qui | Limite da conservare nella scelta |
|---|---|---|
| ESP32-C6 e famiglia ESP32 | telemetria, pulsanti e piccoli servizi Wi-Fi; primo confronto per nodi IoT | confrontare la scheda completa, alimentatore e ciclo radio; nessun Hermes completo dimostrato su MCU |
| ESP32-S3 | periferica audio o interfaccia più articolata da studiare; Wi-Fi e periferiche I2S documentati da Espressif, S284 | istruzioni per reti neurali e DSP non equivalgono a eseguire un agente Linux o un grande modello |
| Raspberry Pi Pico/RP2040; Pico W per radio integrata | acquisizione e controllo, raccordo con lo studio dell’analizzatore audio | Pico base non ha Wi-Fi integrata; Pico W sì; restano microcontrollori, S282 |
| Arduino Uno R3/R4 | esercizi di sensori, seriale e controllo | R3 ha2KB SRAM e non ha radio integrata; R4 WiFi e R4 Minima sono modelli differenti, S276 |
| Raspberry Pi Zero2W | candidato Linux piccolo per servizi molto leggeri |512MB RAM e Wi-Fi2,4GHz, S274; margine per Hermes e dipendenze da provare, non scelta già approvata |
| Raspberry Pi4B con memoria adeguata, oppure altro SBC Linux | candidato al prototipo dedicato dell’assistente con modello remoto | classe4GB come ipotesi iniziale, non minimo ufficiale Hermes; compatibilità ARM64, RAM e consumi da misurare, S275 |
| VM o container su host già previsto | primo prototipo senza acquisti, prima di scegliere un SBC o mini PC | consumi incrementali e disponibilità dell’host contano; non tenere un desktop acceso solo per risparmiare l’acquisto della schedina |

Per il nodo IoT semplice il primo confronto è ESP32 contro Pico W se il caso audio porta riuso di codice; per un terminale audio va studiato anche ESP32-S3. Per il cervello Hermes si parte dal prototipo su host disponibile e solo dopo dalle misure su SBC. Non si assegna al NAS da8GB il nuovo stack per comodità: NAS a orario e assistente sempre raggiungibile hanno dipendenze diverse. Non si spostano RAM o pezzi già destinati al futuro server.

Il progetto audio conserva uno studio su Pico/RP2040 per analizzatore di spettro. La lettura del suo registro il29/10 non dimostra una scheda già acquistata o disponibile. Quella voce non è un Raspberry Linux libero da riutilizzare per Hermes; nessuna doppia allocazione. Specifiche del prototipo audio e licenza del materiale restano da verificare nella sua sede canonica.

## Wi-Fi, SSID e VLAN hanno ruoli diversi

Preferenza dell’utente: piccoli nodi in Wi-Fi per contenere cablaggio e uso delle porte dello switch. L’access point associa un SSID[^2] alla VLAN[^3] di destinazione. Nel disegno attuale i nodi MCU non fidati vanno verso VLAN40 IoT; l’host Linux dell’assistente verso VLAN30 servizi, con autorizzazioni specifiche. VLAN99 rimane gestione. Non si mette tutto nella stessa zona soltanto perché usa la radio. Gli AP mantengono il loro uplink Ethernet/PoE e trasportano le VLAN previste; nessuna porta aggiuntiva per ciascun sensore.

Il firewall nega per impostazione di progetto IoT verso NAS e interfacce amministrative. Si apre soltanto il flusso necessario verso il broker MQTT o un endpoint HTTPS identificato, oltre a DNS, ora e aggiornamenti richiesti. Per MQTT la porta dipenderà da TLS e broker scelti; niente regola generica verso tutta la LAN. L’assistente vede servizi e cartelle autorizzati per compito, senza diventare amministratore di tutte le VLAN. Accesso Tailscale non implica exit node o subnet router attivi.

SSID e VLAN vanno configurati su AP/switch/firewall e poi collaudati. La Wi-Fi del Seven a monte di OPNsense non dimostra questo isolamento. L’isolamento fra client radio e le regole fra VLAN sono controlli distinti. AP e switch non risultano acquistati: questi flussi non sono già operativi. Ethernet resta possibile per un nodo che richieda continuità o banda: la preferenza Wi-Fi non dimostra un minor consumo in ogni caso.

## Il consumo si misura alla presa

La corrente del chip in deep sleep non è il consumo del servizio sempre disponibile. Espressif documenta lo spegnimento della radio nei modi di sonno considerati e modalità diverse da valutare, S273: un nodo che dorme e invia periodicamente è un carico diverso da un server HTTP sempre raggiungibile. Alimentatore, regolatore, LED, scheda SD/SSD e riconnessioni entrano nella misura reale. La potenza massima dell’alimentatore non equivale alla potenza assorbita.

La prova futura confronta lo stesso compito e la stessa disponibilità: energia totale su24ore alla presa, media W, picco, tempo di risposta, RAM massima, riavvii e riconnessioni, costo del modello remoto. Per la VM si misura anche la differenza rispetto all’host acceso senza agente. Un watt medio continuo vale8,76kWh all’anno; il costo si calcola con la tariffa privata corrente, senza pubblicarla. Nessun watt misurato è disponibile oggi e non si sceglie un vincitore energetico da un datasheet.

## Gli strumenti browser segnalati e le alternative

| Strumento | Lettura effettuata il29/10/2026 | Uso utile e limite |
|---|---|---|
| [Learn ESP32](https://learn-esp32.vercel.app/) | contenuto HTML e venti lezioni visibili, incluse Wi-Fi e un esempio HTTP; interfaccia dipendente da JavaScript | prima introduzione e codice di esercizio; simulazione interattiva non collaudata, licenza del sito non accertata |
| [Learn Arduino](https://learn-arduino-red.vercel.app/) | contenuto HTML e sedici lezioni visibili su Uno, sensori, seriale e attuatori | comprendere firmware e periferiche; non emula automaticamente un server Linux, licenza non accertata |
| [Wokwi](https://docs.wokwi.com/) | documentazione primaria di simulazione Arduino, ESP32, STM32 e Pico, con rete simulata | candidato per firmware e protocolli; condizioni personali e funzioni a pagamento da distinguere, nessuna esecuzione reale provata |
| [CircuitJS](https://www.falstad.com/circuit/) | pagina del simulatore e descrizione degli esempi di circuito | tensioni, correnti e componenti; non prova VLAN, consumo della scheda o compatibilità Hermes |

Il parametro pubblicitario del secondo link dell’utente è omesso dalla citazione canonica; la richiesta originale resta nel livello privato. Nessuna credenziale, chiave o corpus domestico va caricato in un simulatore pubblico per queste prove. Nel template si apre un filone di studio con fonti sorvegliate: non si dichiara un nuovo pacchetto pronto, non si installa un MCP e non si aggiunge un account.

## Prossima prova e risultato che serve

La prima prova utile è un sensore o pulsante simulato che produce un messaggio documentato e un agente su Linux che lo legge attraverso un servizio con permessi limitati. Salvare firmware, configurazione e dipendenze in repository; credenziali nel livello privato. Poi usare hardware per misurare consumo, radio e riavvio. Il passo discriminante dell’isolamento sarà il tentativo dalla VLAN IoT di raggiungere gestione/NAS: deve fallire mentre il solo endpoint autorizzato funziona. Il simulatore da solo non chiude questa prova. Il brain futuro del template, Obsidian e il promemoria «Jev» rimangono nello studio17; chiedere il nome solo alla tappa concordata.

[^1]: MCU: microcontroller unit, processore integrato per firmware e controllo. SBC: single-board computer, computer completo su scheda.
[^2]: SSID: service set identifier, nome logico della rete Wi-Fi.
[^3]: VLAN: virtual local area network, separazione logica della rete di livello2; le regole di accesso fra zone spettano al firewall previsto.
