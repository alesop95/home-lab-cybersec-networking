# Scheda dispositivo: campi fissi e raccolta in sola lettura

Metodo deciso dall'utente l'8/10/2026 (ADR-021) per caratterizzare in modo completo e omogeneo ogni dispositivo della rete. Si applica alle voci del [censimento](01-tbc-studio-dispositivi-domestici.md), che resta l'inventario canonico con i suoi ID documentali: questa pagina dice che cosa si scrive per ciascun ID, dove si legge ogni dato e che cosa non si pubblica.

## Perché una scheda a campi fissi

Le descrizioni storiche del censimento sono nate in momenti diversi e con domande diverse: per un portatile c'è l'uscita completa di una diagnostica, per un telefono soltanto il nome. Due dispositivi descritti in modo diverso non si confrontano, e le domande che il progetto deve chiudere sono tutte di confronto: quanti apparati vanno cablati, quali reggono il WPA3 e quindi l'SSID CASA senza ripieghi, quali hanno una scheda che sfrutta una porta a 2,5 GbE, quali stanno nella VLAN IoT perché non ricevono più aggiornamenti. Una scheda con gli stessi campi per tutti rende queste domande una lettura di colonna invece di una ricerca.

## I campi

Ogni scheda ha sei campi, sempre nello stesso ordine, più la fonte. Un campo che non si conosce si scrive "da compilare", mai si omette: un campo assente e un campo dimenticato non si distinguono.

| Campo | Contenuto | Da dove si legge |
|---|---|---|
| Identità | ID documentale, categoria, produttore e modello, proprietario per ruolo | raccolta automatica per i PC; etichetta o impostazioni per gli altri |
| Sistema | sistema operativo e versione, processore e memoria dove ha senso, supporto e aggiornamenti | raccolta automatica; supporto dalla pagina del produttore, con la fonte nel registro |
| Rete cablata | chip della scheda, velocità massima ammessa, velocità negoziata | raccolta automatica; sulle console e sui televisori, dalle impostazioni di rete |
| Wi-Fi | generazione, standard 802.11, supporto WPA3, supporto 802.1X | raccolta automatica dove c'è una radio; per telefoni e tablet, scheda tecnica del modello |
| Collocazione | cablato o Wi-Fi, piano, porta dello switch o SSID, VLAN | decisione di progetto, non dato della macchina |
| Esposizione | servizi che offre, inoltri che richiede, sensibilità dei dati che contiene | decisione di progetto e uso dichiarato |
| Fonte | data e mezzo della rilevazione | scritta da chi compila |

La velocità massima e quella negoziata sono due dati distinti e servono entrambi: la prima dice che cosa la scheda potrebbe fare, la seconda che cosa fa sul cavo e sulla porta di oggi. Nessuna delle due è una misura di prestazioni: la si misura, se serve, con un trasferimento reale.

## La raccolta in sola lettura

Per i computer i dati dei primi quattro campi si raccolgono con uno strumento che legge e non modifica nulla, e che scrive un file JSON nel livello privato `_notes/censimento/raccolte/`, ignorato da git. Il file si chiama con l'ID documentale e la data, non con il nome della macchina.

Su Windows, dalla radice del progetto oppure copiando lo script sul PC da censire, in PowerShell.

```powershell
powershell -NoProfile -ExecutionPolicy Bypass -File tools/raccolta-dispositivo.ps1 -Id PC-01
```

Su Linux, in bash.

```bash
bash tools/raccolta-dispositivo.sh PC-02
```

Lo script Windows legge il sistema, il produttore, il modello e la scheda madre, il processore, la memoria, le schede di rete fisiche con le velocità ammesse dal driver e, con `netsh`, il driver Wi-Fi e la connessione corrente. Lo script Linux legge `/etc/os-release`, i dati DMI esposti senza privilegi, `ip`, e se installati `ethtool` e `iw`. Nessuno dei due raccoglie numeri di serie, product ID, chiavi di licenza, utenti o programmi installati. Lo script Windows è stato provato l'8/10/2026 su un PC di sviluppo che non appartiene alla rete domestica, e la sua raccolta di prova è stata eliminata; quello Linux è verificato soltanto nella sintassi, e la prima corsa vera su una macchina Linux va controllata a campione.

Dal JSON la scheda pubblica si ricava con uno strumento deterministico, che compila ciò che la raccolta sa e lascia "da compilare" il resto. Non scrive mai nome macchina, indirizzi MAC, SSID o versioni dei driver, e la sua prova interna lo verifica su una raccolta costruita.

```powershell
python tools/scheda-da-raccolta.py _notes/censimento/raccolte/PC-01-2026-10-08.json --categoria "PC fisso"
```

## I dispositivi senza script

Console, televisori, telefoni e tablet non eseguono script. Per questi i dati si leggono dalle impostazioni e si scrivono a mano nella stessa scheda, con la fonte dichiarata: per la PS5 le impostazioni di rete mostrano lo stato della connessione e il tipo di NAT; per i televisori la sezione di rete o di informazioni sul dispositivo; per telefoni e tablet la pagina di informazioni sul telefono per il modello e la versione, e la scheda tecnica del produttore per gli standard Wi-Fi e il WPA3, che le impostazioni di solito non mostrano. Una schermata utile si conserva in `_notes/`, non nel repository.

## Che cosa resta privato

Il file di raccolta contiene il nome macchina, gli indirizzi MAC e l'SSID a cui il computer è collegato. Resta in `_notes/` e non si copia nei file tracciati, secondo la regola di anonimizzazione. Su un client che rende casuale il proprio MAC per ogni rete, poi, quell'indirizzo non è un'identità stabile, e per riconoscere il dispositivo nelle tabelle del router serve l'ID documentale e non il MAC.

## Il modello della scheda

```
### <ID>

**Identità.** categoria; produttore e modello; proprietario per ruolo

**Sistema.** sistema operativo e versione; processore; memoria; supporto e aggiornamenti

**Rete cablata.** chip, massima, negoziata

**Wi-Fi.** generazione; standard 802.11; WPA3; 802.1X

**Collocazione.** cablato o Wi-Fi, piano, porta dello switch o SSID, VLAN

**Esposizione.** servizi offerti, inoltri necessari, sensibilità dei dati

**Fonte.** data e mezzo della rilevazione
```
