# Anonimizzazione della documentazione del lab

> Regola modulare, da caricare sempre. Questo repository e' destinato a un remoto pubblico su GitHub sotto l'identita' personale: tutto cio' che si scrive in un file tracciato diventa visibile a chiunque, per sempre, anche dopo una correzione successiva, perche' la storia git resta consultabile finche' non viene riscritta. La regola vale per ogni contenuto scritto d'ora in avanti nei file tracciati, e in particolare per l'albero `docs/` generato dal documento sorgente e per le schede sotto `.claude/context/`.

## Il rischio specifico di questo progetto

Un progetto di home lab documenta la rete di un'abitazione privata, e la combinazione dei dati che vi compaiono e' piu' sensibile della somma delle sue parti. L'indirizzo civico dice dove si trova la casa; l'indirizzo IP pubblico statico dice come raggiungerla da Internet e resta valido nel tempo proprio perche' statico; l'SSID di fabbrica del modem lega la casa alla linea dell'operatore; il censimento dei dispositivi dice che cosa c'e' dentro e con quale sistema operativo, cioe' quale superficie d'attacco esiste. Pubblicare l'insieme significa pubblicare una mappa d'ingaggio di una casa reale, ed e' esattamente il contrario dello scopo di un lab di sicurezza. Nessuno di questi elementi va in un file tracciato.

## Cosa si anonimizza sempre

L'indirizzo civico dell'abitazione, il comune e la provincia. L'indirizzo IP pubblico statico assegnato alla linea, il gateway della WAN e ogni indirizzo derivato da essi, comprese le URL degli strumenti di lookup che contengono l'indirizzo nel percorso e i blocchi whois che ne discendono. L'SSID di fabbrica del modem e ogni SSID reale della rete domestica. Il numero di serie e il codice di tipo hardware degli apparati forniti dall'operatore. I nomi macchina, gli identificativi di dispositivo, i product ID di sistema operativo e i numeri di serie dei computer, dei portatili e dei dischi del censimento. Ogni MAC address di un dispositivo reale. Il nome proprio completo di una persona fisica, incluse le persone terze citate come fonte di ispirazione da post pubblici. Il fornitore di energia elettrica e i codici di offerta contrattuale.

## Cosa resta reale, e perche'

Il nome dell'operatore di telecomunicazioni e dei vendor (Fastweb, Zyxel, MikroTik, Ubiquiti, Proxmox, OPNsense, Wazuh, e cosi' via) resta scritto per esteso: sono nomi di organizzazione e di prodotto, non dati personali, e senza di essi la documentazione tecnica perde ogni valore d'uso. I modelli di apparato restano reali per lo stesso motivo: sapere che l'analisi riguarda uno ZYXEL XMG1915-10E e non uno switch generico e' il contenuto stesso del documento.

Gli indirizzi privati RFC1918 del piano di indirizzamento del lab restano come sono. Non sono un dato reale trapelato ma una scelta di progetto, non sono raggiungibili dall'esterno, e sostituirli renderebbe incomprensibile la segmentazione che il progetto documenta. Stesso discorso per gli indirizzi di gestione di fabbrica degli apparati, come il `192.168.1.254` del modem dell'operatore, che sono valori di default pubblicati nei manuali.

Restano reali gli indirizzi pubblici di transito che compaiono in un traceroute e i contatti pubblici di un registro regionale come RIPE NCC: sono infrastruttura di rete pubblica e contatti istituzionali, non identificano l'abitazione, e appaiono identici in qualunque traceroute effettuato dallo stesso strumento. E' l'indirizzo di destinazione a essere identificante, non il percorso per arrivarci.

Restano infine i prezzi di listino di un'offerta commerciale pubblica e le tariffe unitarie usate in un calcolo tecnico, per esempio la stima del consumo elettrico del lab acceso ventiquattro ore su ventiquattro. Sono cifre pubblicate dal fornitore, non dati personali, e senza di esse il calcolo diventa inverificabile. E' il legame fra la cifra e il contratto della persona a essere sensibile, quindi si anonimizzano il nome del fornitore e i codici di offerta, non il numero.

## Convenzione dei segnaposto

Gli indirizzi IP pubblici reali si sostituiscono con gli intervalli di documentazione RFC 5737, cioe' `203.0.113.0/24`, `198.51.100.0/24` e `192.0.2.0/24`, che non sono instradabili su Internet reale e non possono quindi puntare per sbaglio a un sistema di qualcun altro. L'indirizzo pubblico della linea diventa `203.0.113.10` e il suo gateway `203.0.113.1`, cosi' che il rapporto fra i due resti leggibile. I MAC address diventano `AA:BB:CC:00:00:NN` progressivi. I nomi macchina conservano il prefisso di sistema e perdono il suffisso, quindi `DESKTOP-XXXXXXX` e `LAPTOP-XXXXXXX`. Gli identificativi a GUID diventano `00000000-0000-0000-0000-000000000000`. I numeri di serie e i codici hardware diventano un segnaposto parlante fra parentesi angolari, per esempio `<sn-modem>` o `<hw-type-modem>`, cosi' che nel testo si capisca ancora di che dato si trattava. Le persone terze diventano `Autore-LinkedIn-A` e `Autore-LinkedIn-B` in ordine di prima apparizione, oppure un'etichetta di ruolo quando il ruolo dice piu' del nome.

Il segnaposto va scelto una volta e riusato sempre: se lo stesso indirizzo o la stessa persona ricompaiono in un altro documento, ricompare lo stesso segnaposto, altrimenti la documentazione perde coerenza interna e diventa impossibile capire che due passaggi parlano della stessa cosa.

## Dove vive la mappatura

La traduzione da segnaposto a valore reale non si scrive mai in un file tracciato: vive in `_notes/.anonymization-map.md`, ignorato da git, e si estende con nuove voci mano a mano che si anonimizza altro materiale. Chi opera davvero sulla rete consulta quel file in locale per tradurre. Questa e' la ragione per cui la mappa stessa e' il dato piu' sensibile del progetto, piu' di qualunque singolo valore che contiene: chi la legge puo' invertire ogni anonimizzazione fatta altrove, quindi non va mai citata per estratto in un file tracciato, nemmeno in un work-log, nemmeno per un solo esempio.

## Quando si applica: mentre si scrive

Fino al 25/08/2026 l'albero `docs/` si generava dal documento Word e l'anonimizzazione era una regola di generazione, applicata a ogni corsa dal sidecar `tools/redactions.json`. Da quando l'albero e' passato a manutenzione manuale, quel meccanismo non gira piu': il contenuto nuovo si scrive gia' anonimizzato, e non c'e' nessuna sostituzione automatica che rimedi a un valore reale digitato per distrazione.

E' un cambiamento che sposta responsabilita' e non protezione, perche' la parte che protegge davvero e' sempre stata il guard-rail: il sidecar sostituiva i valori che qualcuno gli aveva insegnato, il guard-rail verifica il risultato. Quello che cambia e' l'ordine dei gesti. Prima di scrivere un valore reale nuovo si aggiunge la voce a `_notes/.anonymization-map.md`, per ricordarsi la traduzione, e a `_notes/.anonymization-patterns.json`, perche' il controllo lo sappia cercare; poi si scrive il segnaposto nel testo. Fare il contrario significa affidarsi al fatto che il guard-rail indovini un valore che nessuno gli ha descritto, e per i numeri di serie e i nomi propri non indovina.

Il sidecar `tools/redactions.json` si conserva come registro di cio' che e' stato sostituito nella prima stesura, ed e' la fonte da cui ricostruire la mappa se andasse persa. Resta inoltre attivo se un giorno si convertisse un altro documento verso una destinazione nuova.

## Il controllo automatico, e perche' non basta la buona volonta'

`scripts/Test-Anonymization.py` passa tutti i file tracciati da git e riporta indirizzi reali, MAC reali, nomi propri di persona, caselle di posta personali, numeri di serie e identificativi macchina noti, numeri di telefono, IBAN e partite IVA. Si lancia dalla radice del progetto, esce con codice diverso da zero se trova qualcosa nelle categorie bloccanti, e va eseguito prima di ogni commit che tocchi documentazione.

```powershell
python scripts/Test-Anonymization.py
```

Quando il commit introduce file nuovi, non ancora aggiunti all'indice, si aggiunge l'opzione che li comprende, altrimenti l'esito sarebbe verde su un insieme che non contiene cio' che si sta per pubblicare.

```powershell
python scripts/Test-Anonymization.py --includi-nuovi
```

Lo script e' versionato e non contiene nessun valore reale: cio' che deve cercare vive in `_notes/.anonymization-patterns.json`, ignorato da git accanto alla mappa dei segnaposto. Se quel file manca lo script si ferma e lo dichiara, invece di restituire un esito verde che non ha calcolato. Quando la mappa cresce, cresce anche quel file: sono due facce dello stesso dato, e vanno aggiornati insieme.

Il controllo si fa sull'intero albero tracciato, non sui soli file toccati dalla sessione. Un residuo non si introduce, si eredita: un valore reale entrato in un commit di mesi prima resta li' finche' qualcuno non passa tutto l'albero, e restare puliti sui propri file non dice niente sul repository.

Due cose che lo script non puo' fare e restano umane. Non distingue un falso positivo da una fuga quando il valore e' ambiguo, per esempio un numero di build che somiglia a un indirizzo o un codice prodotto che somiglia a un seriale: quei riscontri finiscono nelle categorie non bloccanti e vanno guardati uno per uno. E non conosce il contesto: lo stesso identificativo puo' essere pubblico in una riga di whois istituzionale e identificante due righe piu' sotto, e la lista delle eccezioni di contesto va tenuta aggiornata a mano nel file dei pattern.

## Materiale non versionato che resta comunque sensibile

Il documento `.docx` sorgente, le fotografie della sessione di installazione, il file DxDiag e gli estratti temporanei sotto `_notes/` non sono tracciati e non finiscono su GitHub, ma restano sul disco in chiaro e contengono i valori reali per intero. Quando da uno di questi si ricava un contenuto per un file tracciato, per esempio una descrizione di una schermata fotografata, la trascrizione va fatta gia' anonimizzata: un numero di serie leggibile su un monitor in una fotografia e' un numero di serie, e trascriverlo in un catalogo tracciato lo pubblica esattamente come lo pubblicherebbe la fotografia stessa.

## Cosa fare quando si trova un valore reale gia' pubblicato

Non si riscrive la storia git di propria iniziativa: la riscrittura di una storia gia' spinta su un remoto e' un'operazione pianificata, con backup, mai un'azione improvvisata a valle di una sessione. Si segnala il valore trovato, lo si aggiunge alla mappa privata e al file dei pattern, lo si corregge nel file tracciato corrente, e si annota la necessita' di una bonifica della storia come lavoro a parte nel registro delle pendenze. Finche' il repository non e' stato spinto su un remoto, invece, la correzione e' semplice e va fatta subito: e' esattamente la finestra in cui si trova questo progetto oggi, ed e' la ragione per cui l'anonimizzazione si fa adesso e non dopo il primo push.
