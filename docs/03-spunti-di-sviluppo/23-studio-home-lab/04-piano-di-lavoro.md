# Piano di lavoro e criteri di completamento

Ritorno allo [studio](README.md). Questo piano riguarda la rete e i servizi; la guida NAS nella sessione parallela resta autorita' sull'assemblaggio. Nessun passo fisico e' marcato eseguito perche' ne e' stata scritta la procedura.

| Fase | Attivita' | Prerequisito | Evidenza per chiuderla |
|---|---|---|---|
| 0 | consolidare fonti e inventario documentale | documenti locali e fonti dell'utente | registro con tutti i sei riferimenti iniziali e censimento controllato; tabella dispositivi con lacune esplicite |
| 1 | sopralluogo rete e conteggio porte | disponibilita' locale | elenco prese, piani, stanze, client cablati simultanei, posizione AP e budget |
| 2 | identificare NIC firewall, backup e aggiornamento | console e accesso locale | corrispondenza porte fisiche, versione e config salvata; una postazione di prova naviga senza spostare tutta la casa |
| 3 | scegliere e acquistare switch/AP | fase 1 e confronto modelli | preventivo EU completo, PoE e porte sufficienti, firmware/supporto verificati |
| 4 | configurare switch e primo AP | firewall e apparati | VLAN di gestione accessibile, SSID su subnet corretta, blocchi inter-VLAN provati, recupero locale possibile |
| 5 | estendere Wi-Fi e migrare client | fase 4 | misure copertura e roaming, scelta motivata del terzo AP, stato del Wi-Fi modem dichiarato |
| 6 | host sempre acceso, DNS opzionale e monitor | hardware e consumi misurati | rete funzionante con NAS spento; backup e ritorno a Unbound provati |
| 7 | integrare NAS e backup | collaudo NAS concluso dall'altra sessione | NIC/servizi/finestra di accensione confermati, un ripristino completato |
| 8 | pilota inventario e NovaSCM | VM LAB isolata | enrollment, raccolta, workflow controllato e ripristino documentati |
| 9 | Wazuh/Suricata e pentest | risorse, log e LAB disponibili | alert atteso riprodotto, prestazioni misurate, finding confermati e ritestati |

La fase 0 e' documentale. L'inventario fisico e la scelta definitiva di quanti AP acquistare restano aperti finche' non si dispone dei dati della fase 1. Questo non impedisce lo studio degli scenari di spesa e della configurazione.

## Informazioni da rilevare senza duplicare il lavoro NAS

Per la casa servono numero di piani e aree, materiali dei muri/solai, punti Ethernet e prese di alimentazione, eventuali aree esterne, client che devono lavorare cablati insieme e budget apparati/posa. La mappa dell'abitazione e gli identificativi reali restano nel livello privato. Per ogni dispositivo gia' citato si confermano presenza, uso, connettivita', supporto aggiornamenti e dipendenza da discovery locale.

Dalla sessione NAS basta ricevere un riepilogo anonimizzato del sistema finale: modello/NIC e velocita', servizi previsti, finestre di disponibilita', interfaccia di gestione, backup e collaudi conclusi. Non si ricensisce il lotto donatore e non si cambia la configurazione di storage per rendere piu' comodo questo piano.

## Decisioni proposte, non ancora eseguite

Il firewall resta fisico, con routing fra zone su OPNsense. Lo switch principale e' candidato 10EP; gli AP sono due cablati con possibile terzo dopo misure. La variante 130BE favorisce funzioni di laboratorio, la 50BE Pro riduce il costo. Il DNS iniziale resta Unbound; AdGuard entra dopo individuazione dell'host sempre acceso. Il primo inventario e' documentale, NovaSCM e Strix sono piloti isolati. Le scelte potranno essere promosse a decisioni adottate nel registro ADR dopo riscontro dell'utente e collaudo pertinente, senza dichiarare gia' acquistato o funzionante cio' che e' proposto.

## Collaudo minimo prima della migrazione completa

Si documentano almeno una prova positiva e una negativa per ogni zona: client autorizzato raggiunge il servizio, ospite non raggiunge NAS o gestione. Si include IPv6 se attivo. Si prova la perdita di DNS, riavvio AP/switch, accesso console firewall e ripristino di una configurazione. Si misura trasferimento locale verso un host cablato per separare prestazioni Wi-Fi da velocita' Internet. Per WireGuard si usa una rete esterna e si verifica accesso solo ai servizi autorizzati.

Ogni prova registra atteso, osservato, data, versione e riferimento alle evidenze private, con una sintesi anonimizzata nel repository. Un test non svolto resta `da eseguire`; il documento di architettura non puo' essere usato come verbale.

## Continuita' fra sessioni

Il punto di ingresso di questo filone e' questo indice di studio, collegato dalla home. Il registro delle fonti e' [SOURCES.md](../../../SOURCES.md); dopo nuovi link si esegue `python tools/source-register.py` e poi `python tools/source-register.py --check`. I file di avanzamento NAS non vengono riscritti per rappresentare questo filone parallelo. Commit, push e deploy restano manuali dell'utente.
