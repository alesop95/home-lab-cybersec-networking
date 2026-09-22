# Home lab: prossimi acquisti e configurazione da finire

## Topologia di riferimento

```text
ONT -> Fastweb Seven -> WAN OPNsense -> LAN OPNsense -> switch Zyxel -> AP al piano inferiore
```

La Wi-Fi del Seven resta fuori da OPNsense finche' gli access point a valle non sono installati. Non collegare OPNsense direttamente all'ONT come baseline: sulla linea concreta il percorso non e' stato validato.

## Acquisti

| Priorita' | Acquisto | Scelta attuale | Nota |
|---|---|---|---|
| 1 | switch gestito multigigabit | Zyxel XMG1915-10E | 8 porte 2,5 GbE e 2 SFP+; per un AP usare un iniettore PoE 2,5 GbE 802.3at |
| 1 alternativa | switch con PoE | Zyxel XMG1915-10EP | preferibile se si comprano subito due o tre AP; PoE centralizzato |
| 2 | access point | Zyxel NWA130BE | tre radio, 2 porte 2,5 GbE, 802.1X/RADIUS e SNMP; verificare firmware |
| 2 economica | access point | Zyxel NWA50BE Pro | costo minore, ma 2,4 GHz piu' una sola fra 5/6 GHz e funzioni enterprise piu' limitate |
| 3 | alimentazione AP | iniettore 2,5 GbE 802.3at | necessario con XMG1915-10E; non usare un iniettore Gigabit se serve il link 2,5 GbE |
| 4 | cablaggio | Cat6/Cat6A, etichette e patch | misurare il percorso verso il piano inferiore prima della posa |
| 5 | continuita' | UPS dimensionato | valutare dopo aver rilevato consumi reali |

Non comprare ora i dischi NAS: il loro inserimento e' previsto non prima dell'inizio 2027.

## Prima dell'ordine

Rilevare numero di piani, percorso cavi, posizione degli AP, numero di client cablati, disponibilita' di prese e budget. Chiudere inoltre il numero di AP: un solo AP rende sensato XMG1915-10E con iniettore, due o tre AP rendono piu' ordinato XMG1915-10EP.

## Sequenza di configurazione

1. Annotare subnet e gateway del Seven ed esportare OPNsense.
2. Collegare Seven LAN 2,5 GbE a OPNsense WAN e collaudare una sola LAN piatta.
3. Collegare OPNsense LAN 2,5 GbE allo switch e verificare DHCP, DNS e Internet.
4. Attivare VLAN 10, 30, 40, 50, 60 e 99 progressivamente, mantenendo il routing su OPNsense.
5. Installare un AP con uplink trunk e iniettore PoE, quindi migrare gli SSID.
6. Spegnere o restringere la Wi-Fi del Seven solo dopo il collaudo degli AP.

La guida operativa completa e' [qui](05-guida-configurazione-opnsense-in-casa.md).
