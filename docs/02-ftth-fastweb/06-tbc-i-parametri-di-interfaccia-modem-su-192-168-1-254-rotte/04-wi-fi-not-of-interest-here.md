# Wi-fi

La prima stesura marcava questa sezione come non rilevante. Nel progetto è invece la sezione che governa l'unico segmento wireless fuori dal perimetro di OPNsense: finché la radio del Seven resta accesa, queste impostazioni sono l'unico controllo disponibile su quella rete. La decisione sulla radio è rimandata dall'utente (ADR-018), e le due strade si configurano in modo diverso. Spenta, la rete esterna si riduce a due cavi e la questione si chiude. Accesa, la Wi-Fi del Seven diventa una rete dichiaratamente esterna, utile per esempio per collegarsi al modem senza passare dal firewall: va tenuta con un SSID che non si confonda con quelli interni, e nessun dispositivo di casa vi si deve associare per abitudine, perché da lì non è né protetto né segmentato.

## Generale

Il Gateway supporta lo standard WiFi 7 in grado raggiungere velocità fino a 7200 Mbits/s utilizzando in modo contemporaneo ed ottimizzato tutte le radio presenti nel CPE (2.4 GHz e 5 GHz).

È possibile ottenere il massimo livello delle prestazioni previste dallo standard solo mantenendo unite le radio.

Nel progetto, se la radio resta accesa, si usa solo WPA3 dove i client lo reggono, con una password diversa da tutte quelle degli AP interni. L'unione delle radio per MLO resta come è.

![](assets/img-0013.png)

Nella rete guest è stata attivata l’opzione di “sola navigazione”:

![](assets/img-0014.png)

Spento → la rete guest resta attiva finché non la disattivi manualmente

30 / 60 / 90 / 120 minuti (ecc.) → la rete guest si spegne automaticamente dopo quel tempo

Il timer parte dal momento in cui attivi la rete guest

![](assets/img-0015.png)

Non è quindi un orario (tipo pianificazione), ma un timer di durata.

Uso tipico:

Se hai ospiti temporanei → imposti 60-120 minuti

Se vuoi evitare dimenticanze → imposti un limite breve

Se ti serve sempre disponibile → lasci “Spento” (cioè senza autospegnimento)

Nota tecnica: questa funzione agisce solo sulla SSID guest, non sulla rete principale, e non “sospende” le sessioni: semplicemente disattiva l’SSID, quindi i dispositivi vengono disconnessi.

Nel progetto la rete guest del Seven si spegne. Gli ospiti usano l'SSID OSPITI degli access point, nella VLAN 50, isolata sull'AP e su OPNsense: è l'unica rete ospiti che il firewall vede e può limitare.

## Programmazione

Settato così il 27/04/2026:

![](assets/img-0016.png)

![](assets/img-0017.png)

![](assets/img-0018.png)

Nel progetto la programmazione si può mantenere se la radio resta accesa. Non è un controllo di sicurezza: riduce le ore in cui la rete esterna esiste, non chi vi accede.

## Impostazioni radio

Nel blocco 2,4 GHz compare “Mixed 802.11b/g/n/ax/be”. Questo indica che l’access point espone contemporaneamente più standard IEEE 802.11 sulla stessa radio, consentendo a client con capacità diverse di associarsi. Gli standard elencati rappresentano generazioni successive: 802.11b e g sono legacy, n introduce MIMO e maggiore efficienza spettrale, ax è Wi-Fi 6 e be è Wi-Fi 7. “Mixed” significa che non viene forzato un singolo standard ma viene mantenuta retrocompatibilità.

Il punto operativo è che la retrocompatibilità ha un costo. I client più vecchi impongono meccanismi di protezione del mezzo trasmissivo che riducono l’efficienza complessiva. Un dispositivo 802.11b, anche se raramente presente oggi, obbliga l’AP a usare modalità di protezione come RTS/CTS o frame a bassa velocità che aumentano il tempo d’aria occupato. Anche i client g e n, se numerosi, limitano l’adozione piena delle tecniche più avanzate di ax e be come OFDMA e scheduling più efficiente.

![](assets/img-0019.png)

Nel blocco 5 GHz la logica è identica ma con standard “a/n/ac/ax/be”. Qui non esiste la componente b/g perché non sono previsti su questa banda. 802.11ac (Wi-Fi 5) e 802.11ax (Wi-Fi 6) sono gli standard dominanti, mentre 802.11be (Wi-Fi 7) è la generazione più recente. Anche qui “Mixed” abilita la coesistenza.

![](assets/img-0020.png)

In ambienti domestici o piccoli uffici con dispositivi eterogenei, la modalità mixed è la scelta di default perché evita problemi di compatibilità. In ambienti controllati, dove si conosce con precisione il parco client, ridurre il set di standard migliora le prestazioni medie e la latenza, perché elimina overhead di compatibilità. Ad esempio, su 2,4 GHz mantenere solo n/ax elimina completamente i meccanismi legacy di b/g. Su 5 GHz mantenere ac/ax (o ax/be se tutti i client lo supportano) consente di sfruttare meglio modulazioni più spinte e pianificazione più efficiente.

Alla rilevazione la radio a 2,4 GHz usava il canale 10 a 20 MHz e quella a 5 GHz il canale 36 a 80 MHz, come riporta la pagina di stato. Nel progetto, se la radio resta accesa, i canali del Seven si coordinano con quelli degli AP, a cominciare da quello del terzo piano, il più vicino al modem.

Nota sugli acronimi. IEEE 802.11 è la famiglia di standard Wi-Fi. MIMO indica multiple input multiple output, cioè più antenne per trasmissione parallela. OFDMA è orthogonal frequency division multiple access, tecnica che suddivide il canale in sottoportanti assegnate a più client nello stesso intervallo temporale.

### Debug problema wi-fi

Prendere documentazione in “27. Debug problema wi-fi 7 Samsung S25 Ultra”.

## Filtro MAC

Sezione con il solo titolo nella prima stesura. Il filtro ammette o esclude client per indirizzo MAC. Nel progetto non si usa: un indirizzo MAC si imita, e non è un controllo d'accesso.

## Easy Mesh

Sezione con il solo titolo nella prima stesura. Easy Mesh estende la rete del Seven con nodi aggiuntivi, come il Seven Booster. Nel progetto non si usa: la copertura della casa la danno gli AP Zyxel, dentro il perimetro, mentre un Booster estenderebbe la rete esterna.

## Analizzatore

Sezione con il solo titolo nella prima stesura. L'analizzatore mostra l'occupazione dei canali radio. Nel progetto serve una volta, prima di scegliere i canali degli AP.
