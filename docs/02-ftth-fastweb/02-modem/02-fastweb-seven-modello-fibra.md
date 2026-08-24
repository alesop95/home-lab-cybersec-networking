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
      - La porta WAN 2,5G è quella che riceve fisicamente la connessione dalla fibra (la limitazione a 1 Gbit/s per singolo dispositivo non si applica a Seven)
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
   - Gestione avanzata tramite app MyFastweb o interfaccia web (configurazione SSID, password, rete ospite, Eco-mode, ecc.)

Il modem è progettato con packaging sostenibile con plastica riciclata al 95 %.

Non esiste ad oggi specifica ufficiale dettagliata del chipset, CPU, RAM o memoria flash interne (marca/model numerico) da parte di Fastweb nelle pagine tecniche o nei materiali pubblici.

La gestione di subnet multiple e VLAN su *Seven* *non* è documentata come una funzione di livello avanzato nel portal/app Fastweb (che è semplificata per utente finale).

### Il seven booster (compatibilità extender)

Seven Booster è semplicemente un extender mesh Wi-Fi 7 progettato per lavorare esclusivamente in accoppiata con il modem Internet Box Seven.

Il Seven crea una rete Wi-Fi 7 con tecnologia MLO (Multi-Link Operation) e il Booster è un nodo aggiuntivo che si collega in modalità mesh al Seven usando lo stesso Wi-Fi 7 ad alta capacità. Questo permette di estendere la copertura in casa senza creare reti separate, mantenendo roaming continuo, stessa SSID, stessa gestione QoS, stesso controller integrato nel modem. Non è un modem, non è uno switch, non aumenta la velocità della fibra. Serve solo per copertura Wi-Fi estesa e stabile con le stesse prestazioni radio del modem principale.
