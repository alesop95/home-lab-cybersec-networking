---
generated-from-commit: e89779723cb1ed715b781763011255a81a82700e
generated-from-branch: main
generated-date: 2026-08-24
covers-paths:
  - tools/**
  - scripts/**
  - docs/_CONVERSION-REPORT.md
last-verified-commit: e89779723cb1ed715b781763011255a81a82700e
---

# Verifica e casi limite

> Scheda tecnica. In un progetto documentale non esistono test unitari nel senso consueto: esiste la verifica che la documentazione sia completa, coerente con la sua fonte e pubblicabile. Questa scheda descrive i tre controlli deterministici che assolvono a quel compito, che cosa ciascuno garantisce e soprattutto che cosa nessuno di essi puo' garantire.

## I tre controlli

Il primo e' interno alla conversione. Al termine di ogni corsa il convertitore confronta i titoli scritti con i titoli presenti nel sorgente, conta tabelle e immagini, e scrive il tutto in `docs/_CONVERSION-REPORT.md`. La verifica di completezza e' quindi automatica e non richiede un passo separato: se il rapporto fra titoli scritti e titoli del sorgente non e' pari, qualcosa e' andato perso e va indagato prima di fare altro.

Il secondo e' `tools/md-unwrap.py --check`, che verifica la convenzione di formattazione su tutti i file Markdown ed esce con codice diverso da zero se qualcuno non la rispetta. La sua garanzia forte e' che non altera mai il rendering: lo strumento confronta il risultato con l'originale e rifiuta di scrivere se il documento reso cambierebbe. Il suo limite dichiarato e' che non entra nei blocchi recintati.

Il terzo e' `scripts/Test-Anonymization.py`, che passa i file tracciati alla ricerca di valori reali. E' l'unico controllo bloccante nel senso pieno: un suo fallimento significa che il repository non e' pubblicabile.

A questi si affianca `tools/lint-md-commands.py`, che copre esattamente il punto cieco del secondo controllo, cioe' i comandi di shell spezzati su piu' righe dentro un blocco di codice.

## Che cosa garantisce il conteggio dei titoli, e che cosa no

Garantisce che nessuna sezione sia sparita nella conversione. Non garantisce che il contenuto di ciascuna sezione sia integro: un paragrafo perso dentro una sezione che conserva il proprio titolo non verrebbe rilevato dal conteggio. Il controllo di secondo livello disponibile e' il conteggio dei caratteri di testo del sorgente, anch'esso riportato nel report, che va confrontato a occhio fra una corsa e la successiva: una variazione grande senza una modifica corrispondente al sorgente e' un segnale.

Il caso limite noto e' il documento con tabelle. Questo sorgente non ne contiene nessuna, quindi il ramo del convertitore che le gestisce non e' mai stato esercitato su questo progetto: se in futuro il documento sorgente acquisisse tabelle, la loro resa andrebbe verificata a mano alla prima corsa.

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

## Il caso limite della rigenerazione parziale

Se si cambia un titolo nel documento sorgente, il file generato cambia nome, e la corsa successiva scrive il file nuovo lasciando l'orfano al suo posto. L'albero risulta allora piu' grande del sorgente e contiene una sezione che non esiste piu'. Il conteggio dei titoli nel report non lo rileva, perche' conta cio' che ha scritto, non cio' che trova sul disco. La contromisura e' la procedura descritta nella scheda di esecuzione, cioe' cancellare le cartelle numerate prima di rigenerare quando si sono rinominate sezioni.

## Verifica dei collegamenti interni

Non esiste oggi un controllo automatico dei collegamenti relativi fra i documenti curati e l'albero generato. E' una lacuna reale: i documenti curati puntano a percorsi che dipendono dagli slug, e uno slug cambia quando cambia un titolo nel sorgente. Finche' non esiste un controllo, dopo ogni rigenerazione con titoli modificati vanno riletti a mano i collegamenti in `DEVELOPMENT.md` e in `pendenze-aperte.md`, che sono i due file che ne contengono di piu'.

## Che cosa non e' verificato in nessun modo

L'esattezza tecnica dei contenuti. Nessuno degli strumenti descritti sa se un'affermazione sulla rete e' vera: sa solo che esiste e che non contiene dati reali. La distinzione fra affermazione verificata e ragionamento plausibile e' affidata alla disciplina di scrittura codificata in `interaction-style.md`, e la sua attuazione concreta sono i marcatori dell'autore nel documento sorgente, censiti in `docs/pendenze-aperte.md`. Quella lista e' il vero registro di cio' che non e' stato verificato.
