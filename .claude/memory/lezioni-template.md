# Lezioni per il template

> Le lezioni nate in questo progetto che valgono oltre il progetto, cioè che passano le due domande della sezione 16 di `.claude/PROJECT-SYSTEM.md`: restano vere tolti i nomi propri, e non sono già nella testa di chi lavora bene. Una voce per lezione, creata con `python .claude/templates/tools/lezioni-template.py nuova` nel giro di lavoro in cui la lezione nasce. Lo stato non si scrive qui: una lezione è recepita quando il template la elenca in `.claude/templates/lezioni-recepite.json`, che arriva con l'allineamento.

Adottato il: 2026-10-20

## L-001 - 2026-10-20 - Il controllo delle colonne non rileva righe Markdown staccate dalla tabella

Nel lavoro sui backup il registro fonti aveva otto separatori vuoti fra gruppi di righe dello stesso corpo. Il controllo tools/lint-md-tables.py riportava zero difetti su dieci file, anche prima della correzione. Le righe dopo il vuoto non appartengono alla tabella in Markdown. La verifica manuale ha mantenuto tutte le 171 righe fonte e ha rimosso soltanto gli otto separatori: le righe S ora formano un blocco continuo sotto la stessa intestazione.

Riproduttore minimo verificato il 20/10/2026 con la copia istanziata: il comando `python tools/lint-md-tables.py _notes/backup-restore/prova-tabella-spezzata.md` esce 0 e dichiara un file e zero difetti sul contenuto seguente. Il file privato serve soltanto alla riproduzione; il contenuto e il comando bastano a ricrearlo altrove.

```markdown
| Fonte | Stato |
|---|---|
| A | letta |

| B | letta |
```

Proposta per la fonte del template: distinguere blocchi con intestazione e separatore dalle righe pipe isolate, segnalando una riga che somiglia a una riga dati ma resta fuori da una tabella. Conservare il caso negativo di una pipe legittima nel codice, così da non allargare il riconoscitore a ogni carattere pipe. Una coppia di prove deve distinguere il corpo continuo dalla riga staccata. Non è stato modificato il linter copiato nel progetto e non è stata aggiunta un'esclusione: la correzione dello strumento appartiene al template.

Il punto non è il numero di colonne, che era già corretto, ma il perimetro della garanzia. Un check verde sulle colonne non certifica che ogni riga fonte venga resa come tabella.


## L-002 - 2026-10-20 - La registrazione di una lezione appiattisce anche la struttura Markdown

La registrazione della lezione L-001 ha ricevuto --testo come stringa con paragrafi separati e un blocco Markdown recintato. Il comando ha restituito successo, ma il corpo scritto è un unico paragrafo: `" ".join(testo.split())` elimina anche gli a capo strutturali e il recinto diventa inline. La rilettura del file ha fatto fallire il confronto con il corpo originale e ha impedito di dichiararlo salvato correttamente. Proposta alla fonte: preservare le righe Markdown nel corpo e applicare la convenzione di un paragrafo per riga soltanto alla prosa, senza toccare codice, tabelle o separatori fra paragrafi; in alternativa dichiarare e validare esplicitamente un input di solo testo. La prova deve conservare un corpo con due paragrafi e codice o tabella; il solo caso a riga unica non misura il difetto. Nel progetto è stata corretta soltanto la voce L-001 già creata, senza modificare la copia dello strumento del template. La copia originale appiattita e il riproduttore sono conservati nel livello privato.

## L-003 - 2026-10-20 - Un riferimento condizionale a un file di configurazione opzionale blocca la chiusura

Dopo l'allineamento del 20/10/2026 il controllo lint-doc-references della chiusura si ferma su craft-apps, nel paragrafo --stile auto della sua skill: viene nominato il JSON di stile del progetto e il testo precisa che si usa soltanto se il progetto ne ha scelto uno. Nel repository quel file non esiste e non deve essere creato per usare il fallback documentato. Il controllo tratta invece il riferimento condizionale come un file vivo obbligatorio. La prova sullo stato reale e il suo output sono conservati nel livello privato del progetto. Proposta alla fonte: rendere esplicita nella skill la natura di percorso opzionale con una forma che il controllo riconosca, oppure aggiungere al riconoscitore una semantica di modello dichiarata e provata. Verificare entrambi i casi, riferimento realmente obbligatorio assente e configurazione opzionale assente. Il progetto non ha creato un file di stile fittizio, aggiunto esclusioni o modificato il linter copiato.

## L-004 - 2026-10-20 - Le fixture TemporaryDirectory possono fallire nel runner Windows prima di misurare il codice

Nel progetto, con Python 3.13 e il runner Windows confinato, una TemporaryDirectory viene creata ma successive aperture o pulizia falliscono con Accesso negato; collocarla sotto il workspace non era bastato nelle prove CLI del calcolatore. Lo stesso problema ricompare nell'autotest del guard-rail: la scansione ordinaria passa, la prova sintetica si interrompe sul temporaneo. Rieseguito il vero autotest invariato tramite pytest con il prefisso di test già autorizzato: 20 casi, zero errori; output e hash della sorgente conservati. Le prove del calcolatore erano state rese eseguibili nel runner ordinario usando file univoci in una cartella di lavoro già accessibile, senza eliminare casi. Proposta per le fixture del template: provare il ciclo completo crea-riapri-pulisci sotto lo stesso token del runner e scegliere una gestione temporanea portabile, con verifica dei percorsi posseduti prima della pulizia. Un test verde fuori dal confinamento non dimostra che la fixture sia portabile al runner normale; un errore di accesso non va convertito in uno skip verde.

## L-005 - 2026-10-20 - Lo splatting PowerShell deve conservare un array anche con un solo argomento

Il controllo lezioni del comando di chiusura PowerShell non raggiunge il sottocomando previsto nei progetti istanziati. Nel log completo del 20/10/2026 compare argparse invalid choice: 'c', mentre l'invocazione diretta della utility con controlla funziona.

La copia ricevuta assegna il risultato di if a una variabile e poi la espande con splatting:

```powershell
$argLez = if ($bundle) { @("raccogli", "--solo-locali") } else { @("controlla") }
$uscitaLez = & $python $lezioni @argLez 2>&1
```

Il ramo con un elemento viene emesso dalla pipeline come stringa, non come array. Il riproduttore locale legge System.String e l'invocazione Python riceve i singoli caratteri di controlla. La verifica discriminante deve esercitare sia il ramo con un argomento sia quello con due e controllare gli argomenti effettivamente ricevuti dal processo, non soltanto il testo del file PowerShell. La correzione va alla fonte del template, conservando un array anche nel caso singolo. Le copie degli strumenti nel progetto non sono modificate. Evidenza: _notes/backup-restore/controlli-riaudit-2026-10-20.txt, sezione Lezioni per il template.

## L-006 - 2026-10-26 - Il marcatore di allineamento nasce con fine riga miste

allinea-tutti.ps1, riga 638, scrive .claude/allineamento-template.json come (ConvertTo-Json) più un LF nudo. Su Windows PowerShell 5.1 ConvertTo-Json separa le righe con CRLF, quindi il file nasce con sei CRLF e un LF finale, e check-eol dentro chiudi -SoloControlli lo blocca al primo commit dopo l'allineamento. Osservato il 26/10/2026 sul marcatore del commit c1f6eb0, normalizzato a mano a CRLF. Rimedio nello strumento: accodare [Environment]::NewLine, oppure normalizzare la stringa a un solo fine riga prima di Scrivi-Testo.

## L-007 - 2026-10-26 - L'allineamento non vede gli strumenti nella radice di un pacchetto

allinea-dal-template.py, passo 3 (riga 623), aggiorna una copia in tools/ del progetto solo se nel template il file sta in .claude/templates/<pacchetto>/tools/<nome>. Tre script di codice stanno invece nella radice del pacchetto: doc-ingest/doc-ingest.py, doc-ingest/cache-storage.py e docx-to-docs/docx-to-md.py. Le loro copie istanziate non si aggiornano mai e l'esito dell'allineamento non le nomina, quindi nessuno se ne accorge. Misurato il 26/10/2026 sui progetti in E:: doc-ingest.py differisce dal template in diy-2way-monitors-home, e-scooter-diagnosys, harmony-book e spanish-learning, cache-storage.py in harmony-book, docx-to-md.py in e-scooter-diagnosys e sony-xperia-1-III-customization (in home-lab-cybersec-networking è archiviato per scelta, ADR-010). Due copie di doc-ingest.py non avevano --esclusi, entrato nel template il 07/10/2026 con 4f4f9d0: diy-2way-monitors-home, intatta e quindi sostituita il 26/10 dopo che chiudi falliva su --autotest, e spanish-learning, adattata con l'OCR eng+spa e da fondere. È la regola documenti-personali che resta senza attuazione nello strumento, cioè proprio dove la regola dice che deve stare. Non è emersa nessuna conversione senza esclusione dopo il 07/10, perché converti-fonti.py esclude da sé e le cache sono più vecchie; la falla era latente. Il secondo difetto è che test-documenti-personali.py prova il pacchetto nel template e non la copia istanziata nel progetto, quindi niente segnala una copia senza --esclusi finché chiudi non chiama --autotest. Rimedio nel template: nel passo 3 mappare anche i file di codice nella radice di un pacchetto, oppure spostarli in <pacchetto>/tools/ con una rinomina registrata; elencare nell'esito dell'allineamento le copie in tools/ senza origine riconosciuta; fare verificare a test-documenti-personali.py, in ogni progetto che abbia tools/doc-ingest.py, che l'opzione --esclusi esista. Poi riallineare tutti i progetti e fondere a mano la copia di spanish-learning.
