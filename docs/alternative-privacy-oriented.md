# Alternative rispettose della privacy ai servizi mainstream

> Documento curato, non generato dal documento sorgente. Riporta integralmente il contenuto di `privacy pack.txt`, il file di appunti alla radice del progetto, che non e' versionato perche' il `.gitignore` esclude i `.txt`. E' materiale di orientamento, non una configurazione: dice quali servizi si vorrebbero sottrarre a un fornitore terzo, e quindi quali carichi il lab dovra' eventualmente ospitare.

## A che cosa serve in questo progetto

Un home lab non nasce per il gusto di avere apparati in casa: nasce per riportare sotto controllo diretto dei servizi che altrimenti vivono su infrastruttura altrui. Questo elenco e' la lista della spesa che giustifica il lab, e va letta come tale. Ogni riga che indica una alternativa self-hostabile, dal cloud personale al server di posta al media server al DNS, e' un carico che prima o poi dovra' trovare posto su una macchina della rete, con il suo consumo, il suo backup e la sua superficie d'attacco. Le righe che indicano invece un servizio esterno diverso, per esempio un fornitore di posta orientato alla privacy al posto di un altro, non hanno impatto sull'infrastruttura e restano decisioni personali di uso quotidiano.

La fonte dichiarata nel file di appunti e' la trascrizione di PrivacyPack.org. E' un elenco di terze parti, non una valutazione fatta in proprio: nessuna delle alternative qui sotto e' stata verificata sul campo in questo progetto, e vanno trattate come candidature da istruire, non come raccomandazioni consolidate.

## Le righe che diventano carichi del lab

Le voci che seguono sono quelle che, se adottate nella loro forma self-hosted, richiedono una macchina, una VLAN e una politica di backup dentro la rete progettata.

| Servizio da sostituire | Alternativa | Impatto sul lab |
|---|---|---|
| OneDrive, Google Drive, iCloud, Samsung Cloud | Nextcloud, OwnCloud | storage di rete, spazio disco reale, backup, esposizione controllata verso l'esterno |
| Plex | Jellyfin | media server, transcodifica, banda in LAN verso i client |
| Google Home | Home Assistant | dominio domotico, tipicamente una VLAN separata perche' popolata da dispositivi IoT poco aggiornabili |
| Google Play Store | F-Droid | nessun impatto infrastrutturale |
| Clipboard e file sharing cloud | Syncthing, KDE Connect | traffico laterale in LAN fra dispositivi, da tenere presente nelle regole inter-VLAN |
| DNS dell'operatore | Quad9, NextDNS | si incrocia con la scelta gia' documentata di un resolver ricorsivo interno con Unbound dietro Pi-hole, che e' l'opzione piu' forte perche' non delega a nessun terzo |

La suite di posta self-hosted non compare in questo elenco ma e' trattata nel documento sorgente sotto `03-spunti-di-sviluppo/07-further-protection/`, con Mailcow come candidata; e' il carico piu' impegnativo dell'insieme, perche' un server di posta esposto richiede reputazione IP, record SPF, DKIM e DMARC corretti e manutenzione continua.

## L'elenco completo, come trascritto

Lo schema della fonte e' costante: applicazione di uso comune, poi alternativa proposta.

### Posta, ricerca, browser

Gmail diventa Proton Mail. Google Photos diventa Ente Photos. Google Search diventa Qwant. Chrome diventa Firefox. Microsoft Edge diventa Firefox oppure LibreWolf. Bing Search diventa DuckDuckGo oppure Qwant. OneDrive diventa Proton Drive oppure Nextcloud.

### Messaggistica

WhatsApp diventa Signal.

### Note, file, password

Google Keep diventa Joplin. Google Drive diventa Proton Drive. Google Passwords diventa Proton Pass.

### Calendario e contatti

Google Calendar diventa Proton Calendar. Google Contacts diventa Proton Contacts.

### Autenticazione, video, store, sicurezza

L'account Microsoft diventa un account locale piu' un gestore di password, Proton Pass oppure Bitwarden. Windows Hello con sincronizzazione cloud diventa Windows Hello solo locale, senza sync. Google Play Store diventa F-Droid. Google Cast diventa Proton Cast. Dove non esiste un servizio di partenza, la fonte propone Proton VPN, notando che offre un piano gratuito illimitato nel traffico e senza pubblicita', con politica dichiarata di assenza di log, ma con limiti su velocita', numero di dispositivi (uno solo) e posizioni dei server. ChatGPT diventa LeChat.

### Assistenti e mappe

Google Home diventa Home Assistant. Google Maps diventa Organic Maps. Google Translate diventa DeepL.

### Community, social, videoconferenze

Discord diventa Matrix. X, gia' Twitter, diventa Mastodon. Zoom diventa Proton Meet.

### Pagamenti, DNS, sistemi

PayPal diventa Hero. Il DNS dell'operatore diventa Quad9. Windows diventa Ubuntu. Android diventa GrapheneOS.

### Media, cloud, documenti

Plex diventa Jellyfin. Google Workspace diventa Proton Docs. iCloud diventa OwnCloud. La fonte nomina inoltre GoDaddy come servizio citato, senza indicarne un sostituto.

### Produttivita'

Microsoft Office diventa OnlyOffice oppure LibreOffice. Microsoft To Do diventa Joplin oppure Tasks.org. Clipchamp diventa Kdenlive oppure Shotcut. Come suite per ufficio la fonte rimanda anche a ufficiozero.org.

### Ecosistema Samsung, su un telefono di fascia alta con One UI

L'account Samsung diventa un account locale con backup manuale. Samsung Cloud diventa Proton Drive oppure Nextcloud. Samsung Internet diventa Firefox oppure Brave con hardening.

### Foto e media su mobile

La sincronizzazione cloud della galleria Samsung diventa Ente Photos. YouTube diventa NewPipe oppure LibreTube. Spotify diventa Spotube oppure file audio locali.

### Tastiera e input

Samsung Keyboard diventa OpenBoard oppure FlorisBoard. L'input vocale Google diventa nessun servizio cloud, oppure una soluzione offline dove possibile.

### Sistema e controllo su mobile

I Google Device Services diventano microG, se la ROM e' compatibile. I Play Services completi diventano Play Services limitati, o un approccio in stile GrapheneOS.

### Sicurezza avanzata su mobile

Le funzioni cloud di Samsung Knox diventano Knox locale piu' un firewall applicativo, TrackerControl oppure NetGuard.

### Cross-platform fra Windows e Android

La clipboard cloud, di Google o di Microsoft, diventa sincronizzazione locale con KDE Connect. La condivisione file cloud diventa Syncthing. L'autofill delle password di sistema diventa Proton Pass oppure Bitwarden. Il DNS di sistema diventa Quad9 oppure NextDNS, gia' citati ma qui nell'accezione valida su tutti i dispositivi.

## Osservazione critica

L'elenco e' fortemente concentrato su un singolo fornitore per una larga parte delle voci, il che sposta la dipendenza invece di eliminarla: sostituire cinque servizi di un grande operatore con cinque servizi di un operatore piu' piccolo riduce l'esposizione pubblicitaria ma non l'accentramento. Le voci che spostano davvero il controllo sono quelle self-hostabili, cioe' il cloud personale, il media server, la domotica, la sincronizzazione file e il DNS, ed e' su quelle che il lab ha un ruolo. Questa e' una lettura del progetto, non della fonte, che si limita a elencare.
