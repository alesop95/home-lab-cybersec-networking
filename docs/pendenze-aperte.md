# Pendenze aperte

> Documento curato, non generato. Vista consolidata di cio' che nel progetto risulta dichiarato incompleto: sezioni marcate dall'autore come da chiarire, percorsi esplicitamente abbandonati, titoli rimasti segnaposto e verifiche sospese. Non e' una fonte: ogni voce punta al file generato che la contiene, e la verita' su ciascuna sta li'. Va riletto quando si riprende il progetto, perche' e' l'unico posto da cui si vede quanto della documentazione e' progetto e quanto e' stato di fatto.

Rilevazione automatica alla data del 24/08/2026, sull'albero generato dal documento sorgente: cinquanta intestazioni fra sezioni aperte e segnaposto, su un totale di 338 titoli. Il conteggio si riproduce percorrendo le intestazioni dei file sotto `docs/` alla ricerca dei marcatori dell'autore.

## Le tre categorie di marcatore

L'autore ha usato tre convenzioni, che hanno significato diverso e vanno lette diversamente.

Il marcatore `[TBC]`, da chiarire, indica una sezione dove l'analisi e' iniziata ma manca una verifica o una decisione. E' il marcatore piu' frequente ed e' quello che porta il lavoro residuo vero.

Il marcatore `aborted` indica un percorso valutato e chiuso. Non e' lavoro residuo: e' una decisione presa, e la sezione resta come traccia del motivo per cui quella strada e' stata scartata. Cancellarla farebbe perdere l'informazione piu' utile, cioe' l'alternativa gia' esclusa.

Il marcatore `not-of-interest-here` indica una parte dell'interfaccia del modem che e' stata censita per completezza ma non rileva per il progetto. Non e' lavoro residuo neppure questo, ed e' segnalato solo perche' un lettore che cerca contenuto in quelle sezioni non ne trovera'.

A queste si aggiungono i titoli rimasti segnaposto, cioe' composti da una lettera ripetuta o da soli punti, che sono strutture predisposte e mai riempite.

## Il vuoto piu' significativo

La macrosezione `06-progetto-rete-domestica-effettivamente-implementato/` esiste nel sorgente come intestazione con tre sottotitoli segnaposto e nessun contenuto. E' la sezione destinata alla rete realizzata, e il fatto che sia vuota e' la sintesi piu' onesta dello stato del progetto: tutto il resto della documentazione e' progettazione, confronto fra alternative e censimento, mentre di realizzato c'e' l'installazione del sistema operativo del firewall documentata in `verbale-installazione-opnsense.md` e nient'altro.

## Lavoro residuo sul firewall

Sono le pendenze che bloccano il progetto, nel senso che finche' non si chiudono la rete non cambia forma. Stanno tutte sotto `03-spunti-di-sviluppo/10-firewall-before-the-switch/02-soluzione-professionale-con-opnsense-25-7.md`, tranne dove indicato.

| Sezione | Che cosa manca |
|---|---|
| Scan porte ethernet e NIC | identificare quale nome di interfaccia corrisponde a quale connettore fisico, con `pciconf -lv`, `ifconfig` e la verifica a LED, distinguendo la gigabit integrata dalle due schede a 2,5 Gbps |
| L'assignation (segmentazione logica) | assegnare le tre interfacce ai ruoli WAN, LAN e OPT1 poi rinominata DMZ; nella sessione del 16/01/2026 e' stata assegnata la sola LAN |
| Scenario con l'operatore che espone IPoE via DHCP | resta ipotesi non confermata; nella topologia adottata il firewall parla con il modem e non con l'ONT, quindi lo scenario diventa rilevante solo se un giorno il modem venisse superato |
| Configurare i parametri delle interfacce | indirizzi delle tre reti, server DHCP interno, verifica che LAN e DMZ non si sovrappongano |
| Due sottosezioni con titolo segnaposto | strutture predisposte e mai riempite, dentro lo stesso file |
| Con una live Ubuntu | percorso abbandonato: la mappatura delle schede si fa dalla console di OPNsense, non da una live esterna, per non introdurre un secondo stack di driver |
| Punti salienti della documentazione per il firewalling | la sezione contiene solo il collegamento alla documentazione ufficiale, senza estrazione |

Si aggiunge una pendenza che non viene dal documento sorgente ma dal verbale fotografico: durante il boot dell'ambiente live e' comparso `Generating configuration: templates...failed`, e va riverificato sul sistema installato.

## Lavoro residuo sul lato operatore

Sotto `02-ftth-fastweb/`.

| Sezione | Che cosa manca |
|---|---|
| Topologia della rete teorica | il disegno definitivo, che oggi esiste come descrizione a parole e come diagramma testuale, non come schema |
| Questione fonia VoIP | verificare se le credenziali SIP sono ottenibili; se non lo sono, il modem resta necessario per la fonia e va tenuto come client SIP dentro la LAN |
| Alternativa modem libero | l'ipotesi di attivare un modem di proprieta' con procedura dedicata resta aperta, e cambierebbe l'intera topologia eliminando il doppio NAT |
| Seconda lettura dei parametri di interesse | rileggere lo stato WAN quando l'interfaccia in fibra risulta attiva; nella lettura di febbraio 2026 la connessione attiva era quella mobile di backup, quindi i parametri letti non erano quelli della fibra |
| Differenza fra port forwarding ed Exposed Host | domanda posta e non risolta nel sorgente |
| Differenza fra le due DMZ in atto | quella del modem verso il firewall e quella del firewall verso il server; la distinzione e' abbozzata ma non chiusa |
| Parametri di interfaccia del modem | la sezione contenitore e' marcata da chiarire nel suo insieme |

## Lavoro residuo sui componenti del lab

| Sezione | Che cosa manca |
|---|---|
| `03-spunti-di-sviluppo/13-switch/` | la configurazione dello switch nella rete, cioe' quali VLAN, quali porte access e quale trunk verso il firewall |
| `03-spunti-di-sviluppo/12-vpn/` | contestualizzare Tailscale alla rete domestica, e la questione del cambio di profilo sul piano gratuito |
| `03-spunti-di-sviluppo/04-rmm-management-.../` | l'implementazione con IP statico, che e' lo scenario diventato attuale dopo l'assegnazione dell'indirizzo fisso; e una verifica su una distribuzione candidata come host |
| `03-spunti-di-sviluppo/02-storage-di-rete-nas/` | compatibilita' con un lettore audio via USB, verifica non fatta |
| `03-spunti-di-sviluppo/10-firewall-.../04-...nethsecurity8.md` | alternativa citata e non valutata |

## Lavoro residuo sul censimento dei dispositivi

Sotto `05-analisi-del-caso/01-tbc-studio-dispositivi-domestici.md`, che e' marcato da chiarire nel suo insieme. Delle voci presenti, sei postazioni fisse e quattro portatili piu' console, televisore, telefoni e tablet, molte hanno la sola intestazione e la sottosezione sulle schede di rete lasciata a segnaposto. Le voci con contenuto reale sono la postazione fissa numero quattro, i portatili due e tre, e la console; le altre sono da compilare. Due voci di dispositivo hanno il titolo composto da soli punti, quindi non e' possibile sapere a che cosa si riferiscano senza chiederlo all'autore.

Il censimento e' meno accessorio di quanto sembri: e' la fonte che dice quale endpoint puo' realmente saturare una porta a 2,5 Gbps e quale no, e senza di esso il dimensionamento dello switch e la scelta di dove portare le porte veloci restano decisioni prese a intuito.

## Sezioni censite ma dichiarate non rilevanti

Undici sottosezioni dell'interfaccia del modem sono marcate `not-of-interest-here`: panoramica dei dispositivi connessi, telefono, l'intero ramo Wi-Fi, USB, condivisione contenuti, condivisione stampante, LAN switch, modalita' a risparmio energetico, stato della fonia, e le tre sezioni di dettaglio e statistica su IPv6 e IPv4 della WAN. Una sezione, lo stato LAN, e' marcata come mancante, cioe' l'autore ha annotato che avrebbe dovuto catturarla e non l'ha fatta.

Vale la pena una nota critica: il ramo Wi-Fi del modem e' marcato come non rilevante, ma nella topologia adottata la Wi-Fi del modem e' esattamente il pezzo di rete che resta fuori dal firewall, quindi le sue impostazioni di sicurezza, cioe' cifratura, canale e rete ospite, sono l'unico controllo disponibile su quel segmento finche' gli access point a valle non saranno installati. La marcatura andrebbe rivista.

## Come si aggiorna questo file

L'elenco si ricalcola percorrendo le intestazioni dei file generati alla ricerca dei tre marcatori e dei titoli segnaposto. Va rifatto dopo ogni rigenerazione dell'albero, perche' i marcatori vivono nel documento sorgente e cambiano quando l'autore lo modifica. Le voci che non vengono dal sorgente, come la pendenza sull'avviso dei template, si aggiungono a mano e si riconoscono perche' non hanno un marcatore corrispondente nell'albero.
