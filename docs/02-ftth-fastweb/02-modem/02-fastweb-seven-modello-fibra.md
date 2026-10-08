# Fastweb seven (modello fibra)

## Informazioni tecniche verificabili

Ecco le informazioni tecniche verificabili sul Fastweb Internet Box Seven (il modem/router che Fastweb fornisce con le nuove offerte FTTH fino a 2,5 Gbps). Tutto ciò che segue è basato su specifiche tecniche ufficiali o pubblicate da fonti caratteristiche del prodotto [https://www.fastweb.it/myfastweb/seven/](https://www.fastweb.it/myfastweb/seven/), [https://www.mondomobileweb.it/307166-fastweb-seven-e-vodafone-seven-nuovi-modem-con-wi-fi-7-caratteristiche-e-cosa-cambia/](https://www.mondomobileweb.it/307166-fastweb-seven-e-vodafone-seven-nuovi-modem-con-wi-fi-7-caratteristiche-e-cosa-cambia/).

![](assets/img-0000.png)

Dal link ufficiale di fastweb lo presentano così in termini di feature e caratteristiche hardware principali:

- Eco mode (risparmio energetico)
   - Modalità Light: fino al 20%
   - Modalità Deep: fino al 50%
- Wi-Fi e antenne
   - Supporto allo standard Wi-Fi 7 Dual Band (bande 2,4 GHz e 5 GHz, con tecnologia Multi-Link Operation - MLO - vedi sotto)
   - Antenne interne configurate in 4×4 per entrambe le bande (2,4 GHz e 5 GHz), per alimentare la trasmissione multipla di flussi dati simultanei (frame spatial streams)
      - 4x4 Antenne 2.4 GHz
      - 4x4 Antenne 5 GHz
      - 802.11 a/b/g/n/ac/ax/be
- Con velocità fino a 7.2 Gbps
- Multi-Link Operation (MLO)
   - MLO combina simultaneamente le bande 2.4GHz e 5GHz, garantendo velocità superiore, stabilità costante e prestazioni elevate anche con più dispositivi connessi. La tecnologia Wi-Fi 7 al suo meglio. Permette di sfruttare simultaneamente più bande per migliore throughput e stabilità del segnale wireless.
   - eMSLR, STR (con Fastweb Seven)
- Porte fisiche
   - 1 porta WAN Ethernet a 2,5 Gbps (sulla versione FTTH).
      - La porta WAN 2,5G è quella che riceve fisicamente la connessione dalla fibra (la limitazione a 1 Gbit/s per singolo dispositivo non si applica a Seven[^1])
   - 1 porta LAN a 2,5 Gbps
      - La porta LAN 2,5 G è una uscita di rete in grado di trasferire traffico a 2,5 Gbit/s verso *un singolo dispositivo compatibile cablato*.
   - 2 porte LAN a 1 Gbps nella versione fibra FTTH.
   - 2 porte telefoniche (RJ11) per linea voce/voip (sono linee FXS)
   - 1 porta USB-A (per collegare dispositivi come hard disk o stampanti, condivisi in LAN).
   - USB-A (per periferiche come stampanti, hard disk, etc…)
   - USB-C per *alimentazione* del dispositivo (*non* è una porta dati).
- ![](assets/img-0001.png)
- Il Fastweb Seven ha già uno “switch interno” integrato. Le porte LAN interne al Seven fungono da switch: puoi collegare più dispositivi contemporaneamente e traffico tra di essi passa attraverso il modem senza bisogno di switch esterno. In questo caso, consapevolmente, la porta LAN 2,5 Gbit/s è quella che può sfruttare l’intera portante ottica GPON. Le altre porte LAN 1 Gbit/s supportano traffico fino a 1 Gbit/s per singolo dispositivo, quindi collegando PC/NAS su queste porte, il throughput massimo sarà 1 Gbit/s, anche se la fibra arriva a 2,5 Gbit/s.
- Con Seven, si ha almeno 1 porta LAN fisica a 2,5 Gbit/s e un singolo PC o NAS con scheda di rete 2,5 GbE collegato a quella porta può raggiungere velocità di rete cablata superiori a 1 Gbit/s, fino a ~2,5 Gbit/s teorici (fermo restando la capacità del dispositivo finale e del cavo).
- Per sfruttare ~2,5 Gbit/s reali su un singolo PC/server tramite cablaggio basta collegare quel dispositivo alla porta LAN 2,5 Gbit/s di Seven e cavo Cat5e o superiore, solo così il throughput locale non è limitato a 1Gbit/s.
- Compatibilità Extender
   - È compatibile con l’extender Seven booster, che replica e estende lo stesso Wi-Fi 7 in mesh.
- Funzioni incluse riguardo la gestione
   - Gestione fino a ~128 dispositivi Wi-Fi contemporanei con assegnazione dinamica di banda e risorse.
   - Modalità Eco per riduzione consumi: Light e Deep con vari livelli di disattivazione servizi.
   - Gestione avanzata tramite app MyFastweb o interfaccia web (configurazione SSID[^2], password, rete ospite, Eco-mode, ecc.)

Il modem è progettato con packaging sostenibile con plastica riciclata al 95 %.

Non esiste ad oggi specifica ufficiale dettagliata del chipset, CPU, RAM o memoria flash interne (marca/model numerico) da parte di Fastweb nelle pagine tecniche o nei materiali pubblici.

La gestione di subnet multiple e VLAN su *Seven* *non* è documentata come una funzione di livello avanzato nel portal/app Fastweb (che è semplificata per utente finale).

### Il seven booster (compatibilità extender)

Seven Booster è semplicemente un extender mesh Wi-Fi 7 progettato per lavorare esclusivamente in accoppiata con il modem Internet Box Seven.

Il Seven crea una rete Wi-Fi 7 con tecnologia MLO (Multi-Link Operation) e il Booster è un nodo aggiuntivo che si collega in modalità mesh[^3] al Seven usando lo stesso Wi-Fi 7 ad alta capacità. Questo permette di estendere la copertura in casa senza creare reti separate, mantenendo roaming continuo, stessa SSID, stessa gestione QoS[^4], stesso controller integrato nel modem[^5]. Non è un modem, non è uno switch, non aumenta la velocità della fibra. Serve solo per copertura Wi-Fi estesa e stabile con le stesse prestazioni radio del modem principale.

## Nel progetto

Delle caratteristiche elencate, il progetto ne usa poche e in modo preciso. La porta WAN a 2,5 GbE riceve la fibra attraverso l'ONT esterno Zyxel PM5100-T1 e non direttamente, come chiarisce la pagina sulla [posatura](../04-come-avviene-la-posatura-e-il-passaggio-fibra.md) e come l'utente ha confermato l'8/10/2026. La porta LAN a 2,5 GbE, la LAN 4, va alla WAN di OPNsense ed è l'unico collegamento fra il modem e la rete di casa. Delle due porte LAN da 1 GbE una va alla PS5, fuori dal perimetro (ADR-018), e l'altra resta libera. Le due porte telefoniche restano alla fonia, invariata.

Non si usano lo switch interno come distribuzione della casa, perché la casa sta dietro OPNsense e lo switch Zyxel; la porta USB e le condivisioni, che offrirebbero servizi a una rete fuori dal perimetro; la modalità ECO, finché non si sa che cosa spegne il livello Deep; il Seven Booster, perché la copertura la danno due access point dentro il perimetro, e un Booster estenderebbe invece la rete esterna. L'assenza di VLAN e di sottoreti multiple, annotata qui sotto, è la ragione per cui la segmentazione sta tutta su OPNsense. La Wi-Fi del Seven è una decisione rimandata: spenta, oppure tenuta come rete esterna dichiarata. Le impostazioni voce per voce sono nella cartella sull'[interfaccia del Seven](../06-tbc-i-parametri-di-interfaccia-modem-su-192-168-1-254-rotte/README.md).

[^1]: Con i modem precedenti (NeXXt/FASTGate) tutte le LAN erano 1 Gbit/s e nessun singolo dispositivo poteva superare 1 Gbit/s.

[^2]: SSID è il nome della rete Wi-Fi ed è praticamente quello che si vede quando ci si connette ("Casa-2.4G", "MyWiFi", ecc.). Ad esempio, il Seven e il Booster usano lo stesso SSID per fare roaming continuo. Questo significa che un dispositivo Wi-Fi può spostarsi da un punto della casa all’altro passando automaticamente da un nodo all’altro della rete senza disconnessione: il passaggio avviene in modo trasparente e immediato, mantenendo la stessa sessione di rete (videochiamate, streaming, VPN restano attivi).

[^3]: Modalità mesh significa che modem e Booster formano un’unica rete Wi-Fi distribuita, con un’unica configurazione e roaming automatico. I dispositivi si spostano da un nodo all’altro senza disconnessioni. Le alternative non mesh sono due: extender Wi-Fi tradizionali che creano una seconda rete separata (SSID diverso, prestazioni peggiori), oppure access point cablati che creano Wi-Fi “manuale” ma richiedono configurazioni separate e non offrono roaming automatico.

[^4]: QoS (Quality of Service) è il sistema che dà priorità al traffico. Il modem decide chi ha precedenza: ad esempio videoconferenze, streaming o gaming prima dei download massivi. È un controllo su banda, latenza e jitter. In una rete domestica il QoS lo gestisce il modem/router. Nei dispositivi Fastweb tipo il Seven o il Booster, il modem principale ha un controller integrato che decide le priorità del traffico: assegna banda e priorità ai vari tipi di dati (videoconferenze, streaming, gaming, download) in base alle regole interne o a quelle eventualmente configurate dall’utente. Non c’è un “server centrale”: tutto avviene localmente sul modem/router, che monitora e instrada il traffico in tempo reale.

[^5]: Significa che è il modem Seven a “comandare” tutta la rete Wi-Fi mesh: decide potenza, canali, roaming, priorità, configurazioni: il Booster non è autonomo, è solo un nodo slave gestito centralmente dal master.
