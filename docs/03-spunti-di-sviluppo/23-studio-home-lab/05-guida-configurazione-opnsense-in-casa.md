# Guida di configurazione OPNsense in casa

Questa guida descrive il percorso scelto per la linea attuale: ONT -> Fastweb Seven -> OPNsense -> switch gestito -> access point. Non certifica la compatibilita' della linea prima di una prova reale e non sostituisce il collaudo dell'operatore.

## Perche' il firewall non va collegato direttamente all'ONT come configurazione di base

La documentazione pubblica Fastweb descrive sia l'uso del modem proprietario sia, in determinate condizioni, l'uso di un apparato proprio collegato all'ONT con i parametri forniti dall'operatore. Non vi si trova una dichiarazione pubblica generale che il MAC dell'ONT sia bloccato al Seven. Nella linea dell'utente, pero', l'assistenza ha escluso il percorso desiderato e una prova riferita da terzi ha avuto esito negativo. Il progetto tratta quindi il vincolo come *evidenza locale da rispettare*, non come legge generale di tutte le FTTH Fastweb.

La configurazione di riferimento e' dunque:

```text
ONT Fastweb
  -> WAN 2,5 GbE del Fastweb Seven
  -> LAN 2,5 GbE del Seven
  -> WAN 2,5 GbE di OPNsense
  -> LAN 2,5 GbE di OPNsense, trunk 802.1Q
  -> Zyxel XMG1915-10E oppure XMG1915-10EP
  -> cavo verso il piano inferiore
  -> iniettore PoE 2,5 GbE oppure porta PoE dello switch
  -> access point Zyxel
```

Il risultato e' un doppio NAT. Soltanto i client collegati alla radio integrata del Seven si trovano sul lato upstream, insieme alla WAN di OPNsense, e non attraversano il firewall. Gli access point collegati allo switch sono invece a valle di OPNsense: i loro SSID, VLAN e client vengono gestiti dalle interfacce e dalle regole del firewall. Un client Wi-Fi Seven puo' avere Internet senza poter entrare nella LAN di OPNsense, salvo port forwarding, regole WAN permissive o errori di configurazione; OPNsense non puo' pero' filtrare il traffico fra client che restano sulla radio del Seven.

## Preparazione e sicurezza del cambio

Prima di collegare il firewall si annotano modello, subnet e gateway effettivi del Seven, si esporta la configurazione di OPNsense e si mantiene una console locale funzionante. Non si usa la subnet indicata nei documenti come fatto acquisito: `192.168.1.0/24` e `192.168.1.254` sono una proposta da verificare osservando il Seven.

Il primo collaudo usa una sola LAN piatta. Le VLAN si aggiungono dopo aver provato DHCP, DNS, Internet e rollback. Non si disattiva la Wi-Fi del Seven finche' almeno un access point a valle non e' stato installato e collaudato.

## Configurazione iniziale del Seven

Si collega una porta LAN 2,5 GbE del Seven alla WAN di OPNsense. Sul Seven si lascia attivo il DHCP e, se l'interfaccia lo consente, si crea una prenotazione per l'indirizzo WAN di OPNsense. Il port forwarding si aggiunge solo per servizi realmente necessari, per esempio la porta UDP di WireGuard; non si espone l'interfaccia di amministrazione di OPNsense.

La radio Wi-Fi integrata nel Seven puo' restare temporaneamente per telefoni, televisori o dispositivi legacy. Si abilita la rete ospiti e l'isolamento client quando disponibili, si evita di usare quella rete per host di laboratorio e si annota nel verbale che quel traffico non e' ispezionato da OPNsense. Gli SSID pubblicati dagli access point a valle sono invece parte della rete protetta e segmentata dal firewall. La migrazione finale consiste nel portare gli SSID necessari sugli access point a valle e spegnere o restringere la radio del Seven.

## Assegnazione delle interfacce OPNsense

Dalla console si identificano le NIC con `pciconf -lv` e `ifconfig`, senza assumere che l'ordine fisico coincida con il nome dell'interfaccia. Si assegna la NIC collegata al Seven come WAN e quella collegata allo switch come LAN. La terza interfaccia resta non assegnata finche' non esiste un requisito DMZ concreto.

Per il primo avvio si configura la WAN in DHCP, si sceglie una subnet LAN che non sovrapponga quella del Seven e si lascia l'amministrazione consentita soltanto dalla LAN locale. Dopo il collaudo si puo' sostituire il DHCP con una prenotazione sul Seven o con un indirizzo statico coerente con la rete upstream.

## Switch, VLAN e access point

Il collegamento OPNsense-switch diventa un trunk quando la LAN piatta funziona. Le interfacce VLAN vengono create su OPNsense e i gateway restano tutti sul firewall. Sullo switch la porta verso OPNsense e l'uplink verso l'access point sono trunk; le porte dei client sono access nella VLAN assegnata.

Le VLAN proposte sono 10 client fidati, 30 servizi e storage, 40 IoT, 50 ospiti, 60 esperimenti e 99 gestione. Si attivano una alla volta, con DHCP e regole minime, verificando dopo ogni modifica. L'iniettore PoE deve essere trasparente a livello 2 e compatibile con 2,5 GbE e 802.3at se l'access point lo richiede; un iniettore Gigabit limita il collegamento anche quando switch e AP sono multigigabit.

XMG1915-10E e' sufficiente per uno o pochi AP alimentati separatamente. XMG1915-10EP e' piu' adatto a due o tre AP perché centralizza l'alimentazione PoE e riduce gli alimentatori distribuiti. La scelta va chiusa prima dell'acquisto, non dopo la posa dei cavi.

## DNS e servizi dipendenti

All'inizio si usa Unbound su OPNsense. AdGuard Home si installa in seguito su un host sempre acceso, non sul NAS se il NAS rimane spento o a orario. Il passaggio richiede un record di destinazione stabile, regole DNS esplicite e una procedura di ritorno a Unbound.

## Collaudo minimo

Da un client cablato si verifica l'indirizzo DHCP, il gateway, la risoluzione DNS, l'accesso Internet e l'impossibilita' di raggiungere le VLAN non autorizzate. Si controllano gli stati e i log di OPNsense e si prova separatamente IPv6, oppure lo si lascia non distribuito finche' non esiste una politica equivalente.

Da un client sulla Wi-Fi del Seven si verifica che Internet funzioni, che la gestione WAN di OPNsense non sia esposta e che il client non raggiunga la LAN del laboratorio. Questo test dimostra la separazione topologica, non una protezione fornita da OPNsense: il traffico resta fuori dalla sua visibilita'.

Il rollback e' fisico: si scollega OPNsense, si ricollega il client al Seven, si ripristina la configurazione esportata e si annota quale modifica ha richiesto il ritorno. La definizione di completamento e' un verbale con porte, indirizzi osservati, VLAN collaudate, regole applicate, limiti della Wi-Fi Seven e data dell'ultimo firmware verificato.
