# Wi-fi (not-of-interest-here)

## Generale

Il Gateway supporta lo standard WiFi 7 in grado raggiungere velocità fino a 7200 Mbits/s utilizzando in modo contemporaneo ed ottimizzato tutte le radio presenti nel CPE (2.4 GHz e 5 GHz).

E’ possibile ottenere il massimo livello delle prestazioni previste dallo standard solo mantenendo unite le radio.

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

## Programmazione

Settato così il 27/04/2026:

![](assets/img-0016.png)

![](assets/img-0017.png)

![](assets/img-0018.png)

## Impostazioni radio

Nel blocco 2,4 GHz compare “Mixed 802.11b/g/n/ax/be”. Questo indica che l’access point espone contemporaneamente più standard IEEE 802.11 sulla stessa radio, consentendo a client con capacità diverse di associarsi. Gli standard elencati rappresentano generazioni successive: 802.11b e g sono legacy, n introduce MIMO e maggiore efficienza spettrale, ax è Wi-Fi 6 e be è Wi-Fi 7. “Mixed” significa che non viene forzato un singolo standard ma viene mantenuta retrocompatibilità.

Il punto operativo è che la retrocompatibilità ha un costo. I client più vecchi impongono meccanismi di protezione del mezzo trasmissivo che riducono l’efficienza complessiva. Un dispositivo 802.11b, anche se raramente presente oggi, obbliga l’AP a usare modalità di protezione come RTS/CTS o frame a bassa velocità che aumentano il tempo d’aria occupato. Anche i client g e n, se numerosi, limitano l’adozione piena delle tecniche più avanzate di ax e be come OFDMA e scheduling più efficiente.

![](assets/img-0019.png)

Nel blocco 5 GHz la logica è identica ma con standard “a/n/ac/ax/be”. Qui non esiste la componente b/g perché non sono previsti su questa banda. 802.11ac (Wi-Fi 5) e 802.11ax (Wi-Fi 6) sono gli standard dominanti, mentre 802.11be (Wi-Fi 7) è la generazione più recente. Anche qui “Mixed” abilita la coesistenza.

![](assets/img-0020.png)

In ambienti domestici o piccoli uffici con dispositivi eterogenei, la modalità mixed è la scelta di default perché evita problemi di compatibilità. In ambienti controllati, dove si conosce con precisione il parco client, ridurre il set di standard migliora le prestazioni medie e la latenza, perché elimina overhead di compatibilità. Ad esempio, su 2,4 GHz mantenere solo n/ax elimina completamente i meccanismi legacy di b/g. Su 5 GHz mantenere ac/ax (o ax/be se tutti i client lo supportano) consente di sfruttare meglio modulazioni più spinte e pianificazione più efficiente.

Nota sugli acronimi. IEEE 802.11 è la famiglia di standard Wi-Fi. MIMO indica multiple input multiple output, cioè più antenne per trasmissione parallela. OFDMA è orthogonal frequency division multiple access, tecnica che suddivide il canale in sottoportanti assegnate a più client nello stesso intervallo temporale.

### Debug problema wi-fi

Prendere documentazione in “27. Debug problema wi-fi 7 Samsung S25 Ultra”.

## Filtro MAC

## Easy Mesh

## Analizzatore
