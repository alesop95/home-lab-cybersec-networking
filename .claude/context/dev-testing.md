---
generated-from-commit: 86b5c8a61a55a48997d7757592aa4d91da9e8581
generated-from-branch: main
generated-date: 2026-08-25
covers-paths:
  - tools/**
  - docs/_CONVERSION-REPORT.md
last-verified-commit: a7eda8a
---

# Verifica e casi limite

> Scheda tecnica. In un progetto documentale non esistono test unitari nel senso consueto: esiste la verifica che la documentazione sia coerente e pubblicabile. Questa scheda descrive i controlli deterministici che assolvono a quel compito, che cosa ciascuno garantisce e soprattutto che cosa nessuno di essi può garantire.

## I controlli

Il primo è `tools/check-docs-tree.py`, che verifica che l'albero regga come struttura navigabile: nessun documento scollegato dagli indici, nessun collegamento relativo che punti nel vuoto.

Il secondo è `tools/md-unwrap.py --check`, che verifica la convenzione di formattazione su tutti i file Markdown ed esce con codice diverso da zero se qualcuno non la rispetta. La sua garanzia forte è che non altera mai il rendering: lo strumento confronta il risultato con l'originale e rifiuta di scrivere se il documento reso cambierebbe. Il suo limite dichiarato è che non entra nei blocchi recintati.

Il terzo è `tools/lint-md-commands.py`, che copre esattamente quel punto cieco, cioè i comandi di shell spezzati su più righe dentro un blocco di codice.

Il quarto è `tools/Test-Anonymization.py`, che passa i file tracciati e quelli nuovi non ancora aggiunti alla ricerca di valori reali. È quello che decide se il repository è pubblicabile.

Dall'8/10/2026 a questi quattro si aggiungono i controlli che `chiudi` trova istanziati dal template (ADR-022): riferimenti a file inesistenti, fine riga miste, carico delle istruzioni, schede di contesto superate, i tre correttori tipografici in modalità di verifica e l'allineamento degli adattatori Codex. Tre strumenti misurano senza fermare il commit e vanno letti da una persona: `lint-prosa`, i cui avvisi sui segni del testo generato erano 77 in 57 file alla prima corsa, `lint-md-tables` e `verifica-ripresa`. Il controllo dell'albero resta fuori da `chiudi` e si lancia a parte.

Gli strumenti di raccolta della scheda dispositivo (ADR-021) hanno una prova propria: `tools/scheda-da-raccolta.py --autotest` verifica che nome macchina, MAC e SSID non escano mai nella scheda pubblica. Lo script di raccolta per Windows è stato provato su una macchina reale l'8/10/2026; quello per Linux è verificato solo nella sintassi, e la sua prima corsa vera va controllata a campione.

## La prova di completezza, fatta una volta

La conversione iniziale è stata verificata il 25/08/2026 con un confronto paragrafo per paragrafo fra il documento Word e l'albero, su testo normalizzato e con le stesse redazioni applicate al sorgente: 1591 paragrafi su 1591 ritrovati, zero mancanti. Non è un controllo ricorrente e non ha senso che lo sia, perché l'albero non discende più dal Word: è la prova, fatta una volta, che l'ingestione non ha perso niente. I conteggi restano in `docs/_CONVERSION-REPORT.md` come documento storico.

Quel "zero mancanti" valeva per il suo perimetro, che era di soli paragrafi, e per questo la prova non poteva vedere le 53 note a piè di pagina del Word, circa 19 mila caratteri, che il convertitore aveva scartato. Le ha trovate la verifica del 07/10/2026, fatta prima di eliminare il Word (ADR-019) su paragrafi, celle di tabella, note, immagini e collegamenti; le note sono state inserite nei punti dei loro richiami. Il metodo e i numeri sono in `docs/fonti-e-materiali.md`.

Vale la pena ricordare perché quel confronto è stato costruito invece di fidarsi del conteggio dei titoli. Il conteggio garantisce che nessuna sezione sia sparita, non che il contenuto dentro le sezioni sia integro: un paragrafo perso dentro una sezione che conserva il titolo non sarebbe stato rilevato da nessuno. E infatti il confronto ha trovato un difetto reale, cioè sette sezioni ridotte a file vuoti dalla pulizia opzionale, che il conteggio dichiarava preservate.

## Che cosa garantisce il guard-rail, e che cosa no

Garantisce che i valori reali censiti nel file dei pattern non compaiano in un file tracciato. Non garantisce nulla su un valore reale che nessuno gli ha insegnato a cercare, ed è il suo limite più importante: è un controllo per elenco, non un rilevatore semantico. Ogni volta che si aggiunge una voce alla mappa dei segnaposto va aggiunta anche al file dei pattern, altrimenti il verde diventa una falsa rassicurazione.

Due categorie restano deliberatamente non bloccanti perché producono soprattutto falsi positivi. Gli indirizzi pubblici che non appartengono ai prefissi noti finiscono in "da valutare", perché includono gli hop di transito di un traceroute e i resolver pubblici, che per decisione restano reali. Gli importi finiscono anch'essi in "da valutare", con una lista di cifre ammesse che copre i prezzi di listino pubblici e le tariffe unitarie usate nel calcolo del consumo elettrico. Entrambe le categorie vanno lette da un umano a ogni corsa, non ignorate.

La versione in uso dall'8/10/2026 è quella del template con sei estensioni del progetto. Prima di adottarla è stata confrontata con la copia precedente sullo stesso perimetro, con esito identico dopo due correzioni emerse proprio dal confronto, e ogni estensione è stata provata sul valore vero del file dei pattern e su una sua variante.

Il caso limite più insidioso è la reversibilità. Il guard-rail cerca i valori reali, non le corrispondenze: una riga che accostasse un segnaposto al suo valore reale verrebbe rilevata perché contiene il valore, ma una riga che rendesse la corrispondenza deducibile senza citarla, per esempio descrivendo una persona in modo univoco accanto alla sua etichetta, non verrebbe rilevata da nessuno strumento. Quella resta responsabilità di chi scrive.

## Il caso limite del file non ancora tracciato

Lo script legge l'elenco dei file da git, quindi in modalità predefinita un file nuovo e non ancora aggiunto all'indice non verrebbe esaminato. È esattamente la situazione di un primo commit che introduce molti file, cioè la situazione di questo progetto il 24/08/2026, e per questo la copia di allora aveva l'opzione `--includi-nuovi`. Dal 08/10/2026 la versione in uso, `tools/Test-Anonymization.py`, comprende quei file per impostazione predefinita, e l'opzione non esiste più.

## Due difetti trovati eseguendo il controllo, e corretti

Vale la pena registrarli perché sono la dimostrazione che un controllo va eseguito e non solo scritto.

La ricerca dei nomi propri era a sottostringa e non a confine di parola, quindi uno dei nomi di battesimo censiti veniva trovato dentro parole italiane comuni che lo contengono come sequenza di lettere, e produceva riscontri bloccanti su testo del tutto innocuo. Corretto passando a una ricerca con confini di parola. Il nome non si riporta qui, e la ragione è la stessa regola: scriverlo accanto alla descrizione del suo segnaposto renderebbe reversibile l'anonimizzazione, ed è un caso che il controllo ha effettivamente intercettato su una prima stesura di questo paragrafo. Il caso limite residuo è il nome che compare legittimamente in un contesto estraneo al progetto, per esempio la citazione di un autore pubblico dentro un file del pacchetto template: si gestisce con la lista delle eccezioni di contesto nel file dei pattern, non allargando o restringendo la ricerca.

L'espressione che riconosce gli importi accettava un simbolo di valuta seguito da un punto, quindi segnalava come importo la fine di una frase che terminava con il simbolo. Corretta richiedendo almeno una cifra, e nell'occasione estesa alla forma con il simbolo posposto, che prima sfuggiva del tutto: gli importi scritti come cifra seguita dal simbolo non venivano rilevati affatto, il che è il difetto più grave dei due perché era un mancato rilevamento e non un falso positivo.

Altri due difetti dello stesso genere sono emersi il 07/10/2026, quando il controllo, eseguito sull'intero albero dopo un allineamento al template, ha dato nove riscontri bloccanti tutti falsi. La ricerca delle organizzazioni private era a sottostringa, come lo era stata quella dei nomi, e una ragione sociale di cinque lettere combaciava dentro i numerali italiani in «centonovanta-»: corretta passando ai confini di parola. E le caselle di posta d'esempio nei test e negli esempi del template, su domini riservati dagli RFC 2606 e 6761, risultavano personali: ora quei domini si ammettono per costruzione, mentre una casella d'esempio su un dominio reale si aggiunge alle ammesse nel file privato. La prova che misura è stata fatta su un file costruito, verificando che il nome dell'organizzazione scritto come parola e una casella sul suo dominio reale restino intercettati. Gli allineamenti fra il 24 e il 30/09/2026 erano stati committati con quel rosso, che nessuno aveva letto come falso: un controllo che segnala troppo smette di essere guardato.

## Il controllo di coerenza dell'albero

Dal 25/08/2026 l'albero è scritto a mano, e con questo perde la coerenza che prima aveva per costruzione: quando la struttura discendeva dai titoli del sorgente, un file scollegato o un collegamento rotto erano impossibili. `tools/check-docs-tree.py` verifica le due cose che ora possono rompersi in silenzio, cioè i documenti che nessun indice collega e i riferimenti relativi che non risolvono. È in sola lettura: un orfano può essere un errore o una scelta, e la differenza la sa solo chi scrive.

Anche questo controllo ha mostrato subito che uno strumento va eseguito e non solo scritto. Alla prima corsa segnalava settantatre documenti irraggiungibili dalla home, che era un falso allarme completo: l'espressione che riconosce i collegamenti vietava la parentesi quadra dentro il testo del collegamento, e negli indici molte voci hanno la forma con il marcatore fra parentesi quadre premesso al titolo. Corretta ammettendo un livello di annidamento, l'esito è passato a zero. Un controllo che grida al lupo su settantatre file su centoventisei non viene corretto, viene ignorato, ed è il modo in cui un guard-rail muore.

Ciò che questo controllo non fa: non sa se un collegamento punta al documento *giusto*, solo che punta a qualcosa che esiste. E ignora deliberatamente le immagini, perché nell'albero puntano a file non versionati e la loro assenza in un clone è voluta.

## Il caso limite della rigenerazione parziale, ora impedito

Era il rischio più serio del modello precedente: cambiando un titolo nel sorgente il file generato cambiava nome, la corsa successiva scriveva il file nuovo e lasciava l'orfano al suo posto, e il conteggio dei titoli non lo rilevava perché conta ciò che ha scritto, non ciò che trova sul disco. Oggi il caso non si presenta più, perché non si rigenera. Al suo posto c'è il rischio speculare, cioè il file rinominato a mano che lascia collegamenti rotti, ed è esattamente ciò che il controllo di coerenza intercetta.

Resta un rischio residuo di natura diversa, e vale la pena nominarlo: una sessione futura che legge una procedura di rigenerazione in un documento non aggiornato potrebbe eseguirla in buona fede e sovrascrivere mesi di lavoro. Per questo il lucchetto non è una nota scritta ma un controllo nel convertitore, che si rifiuta di scrivere in una cartella che contiene documenti senza il timbro di generazione. Una nota si può non leggere, un codice di uscita 2 no.

## Che cosa non è verificato in nessun modo

L'esattezza tecnica dei contenuti. Nessuno degli strumenti descritti sa se un'affermazione sulla rete è vera: sanno che il documento esiste, che è raggiungibile, che è formattato bene e che non contiene dati reali. La distinzione fra affermazione verificata e ragionamento plausibile è affidata alla disciplina di scrittura codificata in `interaction-style.md`, e la sua attuazione concreta sono i marcatori nel testo, censiti in `docs/pendenze-aperte.md`. Quella lista è il vero registro di ciò che non è stato verificato, e ora che l'albero si scrive a mano va aggiornata mentre si scrive, perché non c'è più una rigenerazione che la ricalcoli dai marcatori del sorgente.
