---
generated-from-commit: e89779723cb1ed715b781763011255a81a82700e
generated-from-branch: main
generated-date: 2026-08-25
covers-paths:
  - tools/**
  - scripts/**
  - docs/_CONVERSION-REPORT.md
last-verified-commit: 494b45e
---

# Verifica e casi limite

> Scheda tecnica. In un progetto documentale non esistono test unitari nel senso consueto: esiste la verifica che la documentazione sia coerente e pubblicabile. Questa scheda descrive i quattro controlli deterministici che assolvono a quel compito, che cosa ciascuno garantisce e soprattutto che cosa nessuno di essi puo' garantire.

## I quattro controlli

Il primo e' `tools/check-docs-tree.py`, che verifica che l'albero regga come struttura navigabile: nessun documento scollegato dagli indici, nessun collegamento relativo che punti nel vuoto.

Il secondo e' `tools/md-unwrap.py --check`, che verifica la convenzione di formattazione su tutti i file Markdown ed esce con codice diverso da zero se qualcuno non la rispetta. La sua garanzia forte e' che non altera mai il rendering: lo strumento confronta il risultato con l'originale e rifiuta di scrivere se il documento reso cambierebbe. Il suo limite dichiarato e' che non entra nei blocchi recintati.

Il terzo e' `tools/lint-md-commands.py`, che copre esattamente quel punto cieco, cioe' i comandi di shell spezzati su piu' righe dentro un blocco di codice.

Il quarto e' `scripts/Test-Anonymization.py`, che passa i file tracciati alla ricerca di valori reali. E' quello che decide se il repository e' pubblicabile.

## La prova di completezza, fatta una volta

La conversione iniziale e' stata verificata il 25/08/2026 con un confronto paragrafo per paragrafo fra il documento Word e l'albero, su testo normalizzato e con le stesse redazioni applicate al sorgente: 1591 paragrafi su 1591 ritrovati, zero mancanti. Non e' un controllo ricorrente e non ha senso che lo sia, perche' l'albero non discende piu' dal Word: e' la prova, fatta una volta, che l'ingestione non ha perso niente. I conteggi restano in `docs/_CONVERSION-REPORT.md` come documento storico.

Vale la pena ricordare perche' quel confronto e' stato costruito invece di fidarsi del conteggio dei titoli. Il conteggio garantisce che nessuna sezione sia sparita, non che il contenuto dentro le sezioni sia integro: un paragrafo perso dentro una sezione che conserva il titolo non sarebbe stato rilevato da nessuno. E infatti il confronto ha trovato un difetto reale, cioe' sette sezioni ridotte a file vuoti dalla pulizia opzionale, che il conteggio dichiarava preservate.

## Che cosa garantisce il guard-rail, e che cosa no

Garantisce che i valori reali censiti nel file dei pattern non compaiano in un file tracciato. Non garantisce nulla su un valore reale che nessuno gli ha insegnato a cercare, ed e' il suo limite piu' importante: e' un controllo per elenco, non un rilevatore semantico. Ogni volta che si aggiunge una voce alla mappa dei segnaposto va aggiunta anche al file dei pattern, altrimenti il verde diventa una falsa rassicurazione.

Due categorie restano deliberatamente non bloccanti perche' producono soprattutto falsi positivi. Gli indirizzi pubblici che non appartengono ai prefissi noti finiscono in "da valutare", perche' includono gli hop di transito di un traceroute e i resolver pubblici, che per decisione restano reali. Gli importi finiscono anch'essi in "da valutare", con una lista di cifre ammesse che copre i prezzi di listino pubblici e le tariffe unitarie usate nel calcolo del consumo elettrico. Entrambe le categorie vanno lette da un umano a ogni corsa, non ignorate.

Il caso limite piu' insidioso e' la reversibilita'. Il guard-rail cerca i valori reali, non le corrispondenze: una riga che accostasse un segnaposto al suo valore reale verrebbe rilevata perche' contiene il valore, ma una riga che rendesse la corrispondenza deducibile senza citarla, per esempio descrivendo una persona in modo univoco accanto alla sua etichetta, non verrebbe rilevata da nessuno strumento. Quella resta responsabilita' di chi scrive.

## Il caso limite del file non ancora tracciato

Lo script legge l'elenco dei file da git, quindi in modalita' predefinita un file nuovo e non ancora aggiunto all'indice non verrebbe esaminato. E' esattamente la situazione di un primo commit che introduce molti file, cioe' la situazione di questo progetto il 24/08/2026, e per questo lo script ha l'opzione `--includi-nuovi`, che aggiunge all'elenco i file non tracciati ma non ignorati, cioe' esattamente quelli che un `git add` porterebbe dentro. E' la modalita' da usare prima di un commit che introduce file nuovi; senza di essa l'esito sarebbe verde su un insieme che non comprende cio' che si sta per pubblicare.

## Due difetti trovati eseguendo il controllo, e corretti

Vale la pena registrarli perche' sono la dimostrazione che un controllo va eseguito e non solo scritto.

La ricerca dei nomi propri era a sottostringa e non a confine di parola, quindi uno dei nomi di battesimo censiti veniva trovato dentro parole italiane comuni che lo contengono come sequenza di lettere, e produceva riscontri bloccanti su testo del tutto innocuo. Corretto passando a una ricerca con confini di parola. Il nome non si riporta qui, e la ragione e' la stessa regola: scriverlo accanto alla descrizione del suo segnaposto renderebbe reversibile l'anonimizzazione, ed e' un caso che il controllo ha effettivamente intercettato su una prima stesura di questo paragrafo. Il caso limite residuo e' il nome che compare legittimamente in un contesto estraneo al progetto, per esempio la citazione di un autore pubblico dentro un file del pacchetto template: si gestisce con la lista delle eccezioni di contesto nel file dei pattern, non allargando o restringendo la ricerca.

L'espressione che riconosce gli importi accettava un simbolo di valuta seguito da un punto, quindi segnalava come importo la fine di una frase che terminava con il simbolo. Corretta richiedendo almeno una cifra, e nell'occasione estesa alla forma con il simbolo posposto, che prima sfuggiva del tutto: gli importi scritti come cifra seguita dal simbolo non venivano rilevati affatto, il che e' il difetto piu' grave dei due perche' era un mancato rilevamento e non un falso positivo.

## Il controllo di coerenza dell'albero

Dal 25/08/2026 l'albero e' scritto a mano, e con questo perde la coerenza che prima aveva per costruzione: quando la struttura discendeva dai titoli del sorgente, un file scollegato o un collegamento rotto erano impossibili. `tools/check-docs-tree.py` verifica le due cose che ora possono rompersi in silenzio, cioe' i documenti che nessun indice collega e i riferimenti relativi che non risolvono. E' in sola lettura: un orfano puo' essere un errore o una scelta, e la differenza la sa solo chi scrive.

Anche questo controllo ha mostrato subito che uno strumento va eseguito e non solo scritto. Alla prima corsa segnalava settantatre documenti irraggiungibili dalla home, che era un falso allarme completo: l'espressione che riconosce i collegamenti vietava la parentesi quadra dentro il testo del collegamento, e negli indici molte voci hanno la forma con il marcatore fra parentesi quadre premesso al titolo. Corretta ammettendo un livello di annidamento, l'esito e' passato a zero. Un controllo che grida al lupo su settantatre file su centoventisei non viene corretto, viene ignorato, ed e' il modo in cui un guard-rail muore.

Cio' che questo controllo non fa: non sa se un collegamento punta al documento *giusto*, solo che punta a qualcosa che esiste. E ignora deliberatamente le immagini, perche' nell'albero puntano a file non versionati e la loro assenza in un clone e' voluta.

## Il caso limite della rigenerazione parziale, ora impedito

Era il rischio piu' serio del modello precedente: cambiando un titolo nel sorgente il file generato cambiava nome, la corsa successiva scriveva il file nuovo e lasciava l'orfano al suo posto, e il conteggio dei titoli non lo rilevava perche' conta cio' che ha scritto, non cio' che trova sul disco. Oggi il caso non si presenta piu', perche' non si rigenera. Al suo posto c'e' il rischio speculare, cioe' il file rinominato a mano che lascia collegamenti rotti, ed e' esattamente cio' che il controllo di coerenza intercetta.

Resta un rischio residuo di natura diversa, e vale la pena nominarlo: una sessione futura che legge una procedura di rigenerazione in un documento non aggiornato potrebbe eseguirla in buona fede e sovrascrivere mesi di lavoro. Per questo il lucchetto non e' una nota scritta ma un controllo nel convertitore, che si rifiuta di scrivere in una cartella che contiene documenti senza il timbro di generazione. Una nota si puo' non leggere, un codice di uscita 2 no.

## Che cosa non e' verificato in nessun modo

L'esattezza tecnica dei contenuti. Nessuno degli strumenti descritti sa se un'affermazione sulla rete e' vera: sanno che il documento esiste, che e' raggiungibile, che e' formattato bene e che non contiene dati reali. La distinzione fra affermazione verificata e ragionamento plausibile e' affidata alla disciplina di scrittura codificata in `interaction-style.md`, e la sua attuazione concreta sono i marcatori nel testo, censiti in `docs/pendenze-aperte.md`. Quella lista e' il vero registro di cio' che non e' stato verificato, e ora che l'albero si scrive a mano va aggiornata mentre si scrive, perche' non c'e' piu' una rigenerazione che la ricalcoli dai marcatori del sorgente.
