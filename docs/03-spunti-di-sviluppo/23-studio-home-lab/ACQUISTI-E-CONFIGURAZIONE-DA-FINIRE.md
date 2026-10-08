# Home lab: prossimi acquisti e configurazione da finire

## Topologia di riferimento

```text
ONT -> Fastweb Seven -> WAN OPNsense -> LAN OPNsense -> switch Zyxel -> due AP ai piani 3 e 2
Fastweb Seven -> LAN 1 GbE -> PS5, fuori dal perimetro
```

La Wi-Fi del Seven resta fuori da OPNsense finché gli access point a valle non sono installati. Non collegare OPNsense direttamente all'ONT come baseline: sulla linea concreta il percorso non è stato validato.

## Acquisti

| Priorità | Acquisto | Scelta attuale | Nota |
|---|---|---|---|
| 1 | switch gestito multigigabit | Zyxel XMG1915-10E | 8 porte 2,5 GbE e 2 SFP+; per un AP usare un iniettore PoE 2,5 GbE 802.3at |
| 1 alternativa | switch con PoE | Zyxel XMG1915-10EP | preferibile se si comprano subito due o tre AP; PoE centralizzato |
| 2 | access point | Zyxel NWA130BE | tre radio, 2 porte 2,5 GbE, 802.1X/RADIUS e SNMP; verificare firmware |
| 2 economica | access point | Zyxel NWA50BE Pro | costo minore, ma 2,4 GHz più una sola fra 5/6 GHz e funzioni enterprise più limitate |
| 3 | alimentazione AP | iniettore 2,5 GbE 802.3at | necessario con XMG1915-10E; non usare un iniettore Gigabit se serve il link 2,5 GbE |
| 4 | cablaggio | Cat6/Cat6A, etichette e patch | misurare il percorso verso il piano inferiore prima della posa |
| 5 | continuità | UPS dimensionato | valutare dopo aver rilevato consumi reali |

Non comprare ora i dischi NAS: il loro inserimento è previsto non prima dell'inizio 2027. Facoltativa e senza urgenza: una scheda di rete Intel da 2,5 GbE per il NAS, che oggi lavora a 1 GbE. Non si acquista un FRITZ!Box: non migliora la topologia, il ragionamento è nel [documento sul doppio NAT](07-doppio-nat-dietro-modem-in-comodato.md).

## Prima dell'ordine

Il numero di AP è deciso il 07/10/2026: due, alimentati dallo switch XMG1915-10EP, quindi le righe dello XMG1915-10E e dell'iniettore restano solo come storia della scelta. Resta aperto il modello degli AP. Prima dell'ordine vanno ancora rilevati numero di piani, percorso cavi, posizione dei due AP, numero di client cablati, disponibilità di prese e budget.

## Sequenza di configurazione

1. Annotare subnet e gateway del Seven ed esportare OPNsense.
2. Collegare Seven LAN 2,5 GbE a OPNsense WAN e collaudare una sola LAN piatta.
3. Collegare OPNsense LAN 2,5 GbE allo switch e verificare DHCP, DNS e Internet.
4. Attivare VLAN 10, 30, 40, 50, 60 e 99 progressivamente, mantenendo il routing su OPNsense.
5. Installare un AP con uplink trunk e iniettore PoE, quindi migrare gli SSID.
6. Spegnere o restringere la Wi-Fi del Seven solo dopo il collaudo degli AP.

La guida operativa completa è [qui](05-guida-configurazione-opnsense-in-casa.md).
