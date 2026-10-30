---
covers-paths: [".claude/memory/decisions.md", "docs/03-spunti-di-sviluppo/02-storage-di-rete-nas/09-registro-del-montaggio.md", "docs/03-spunti-di-sviluppo/23-studio-home-lab/16-bisogni-controlli-e-flussi.md"]
last-verified-commit: 76ec0d2bedcb32371b193e72290d3ef0dbf85123
---

# Refactor04 - Identità Google e notifiche della casa

Scheda del27/10/2026. Ritorno al [racconto](studio-didattico-master.md). Il [registro NAS](../../docs/03-spunti-di-sviluppo/02-storage-di-rete-nas/09-registro-del-montaggio.md) conserva campi, osservazioni e piano operativo; ADR-041 e ADR-042 in [decisions](../memory/decisions.md) distinguono destinatario e identità di invio.

## Il ruolo prima del prodotto

L'utente non dispone di un Gmail dei servizi e vuole creare un normale account Google personale per la propria rete domestica, utilizzabile anche altrove. La scelta è coerente con il percorso Gmail OAuth della GUI. Il tipo Per uso personale descrive l'account del provider; servizi domestici descrive il suo ruolo nel progetto. Il precedente Gmail personale indicato in chat rimane soltanto un possibile destinatario alternativo, non viene assunto come mittente.

Nella matrice tecnica reale, prima:

```markdown
| ricevere avvisi e rapporti di salute del NAS | email TrueNAS verso `<email-destinatario-nas>` su Proton, Gmail alternativo; GMail OAuth selezionato nel modulo, autenticazione e salvataggio pendenti | generazione sul NAS, invio tramite provider, consegna alla casella e filtro Log NAS | la cartella contiene notifiche e rapporti, non sostituisce raccolta e conservazione dei log completi; nessun server di posta domestico attivato | preferenza registrata in ADR-041; invio, ricezione, servizio alert e filtro ancora da configurare e provare, fonti S214-S216 |
```

Dopo l'aggiornamento nell'albero di lavoro:

```markdown
| ricevere avvisi e rapporti di salute del NAS | email TrueNAS verso `<email-destinatario-nas>` su Proton, Gmail alternativo; mittente `<email-servizi-casa>` da creare come account Google personale dei servizi domestici; GMail OAuth selezionato, non autenticato o salvato | generazione sul NAS, invio tramite provider, consegna alla casella e filtro Log NAS | la cartella contiene notifiche e rapporti, non sostituisce raccolta e conservazione dei log completi; nessun server di posta domestico attivato | destinatario ADR-041, identità dei servizi casa ADR-042; invio, ricezione, servizio alert e filtro ancora da configurare e provare, fonti S214-S216 |
```

Il prima specificava il trasporto, lasciando implicita l'identità. Il dopo nomina un mittente ancora da creare e mantiene distinti destinatario, autenticazione e prova di consegna. Non è una configurazione eseguita sul NAS: entrambi sono estratti del documento tecnico del repository.

## Tre campi, tre responsabilità

From Email sarà l'indirizzo Gmail del nuovo account autenticato. From Name sarà il nome leggibile mostrato al destinatario, proposto come NAS domestico. La casella Proton riceverà gli avvisi una volta configurata la destinazione effettiva. L'account locale truenas_admin resta il login del NAS: non diventa un account Google modificando un campo email. Il tooltip osservato cita un percorso Accounts > Users > Edit, da verificare nella versione effettiva prima di ricavarne una procedura sui destinatari.

## Una casella di servizio e un service account IAM

Qui si crea un normale account Google con Gmail attraverso la registrazione per uso personale, S218, e il NAS ne chiede il consenso OAuth, S214. Un service account di Google Cloud, S219, è un'identità di workload con autorizzazioni API e un modello di amministrazione diverso. Il nome account di servizio, usato informalmente per la casella della casa, non trasforma il percorso Gmail in un progetto Cloud.

## Riutilizzo e compromesso

L'account dei servizi domestici potrà essere collegato ad altre applicazioni compatibili, valutando per ciascuna funzioni e permessi. Le connessioni all'account Google si possono rivedere e gestire, S220. Riutilizzare l'identità evita di moltiplicare gli account subito; concentra anche le dipendenze future. La conseguenza pratica è registrare i collegamenti quando esistono, così da sapere che cosa dipende dall'account prima di modificarlo o revocare un'applicazione. Nessun altro servizio è già collegato.

La verifica avanza per riscontri: account creato, account corretto scelto nel consenso, autorizzazione salvata, messaggio ricevuto su Proton e classificazione Log NAS. La creazione e tutti i passi successivi sono ancora pendenti. Indirizzo reale, password e recupero restano nel livello privato; la documentazione pubblica conserva il ruolo e lo stato. Lo studio generale della posta dai server interni continua più avanti.

Riscontro di registrazione del27/10/2026: Google offre anche di usare un indirizzo email o numero esistente. L'account Google e la casella Gmail sono elementi distinti, S221. Per il mittente previsto si prosegue verso la creazione di una nuova Gmail tramite il collegamento visibile nella schermata; arrivare al modulo anagrafico non dimostra che la casella o l'account siano già stati creati. I dati personali del titolare restano fuori dalla documentazione pubblica.

## Dal nuovo indirizzo al recupero dell'identità

Il passo successivo mostra il limite della parola creato. Un indirizzo è stato scelto e compare nel riepilogo, ma il flusso presenta ancora Next; non è ancora osservato l'accesso all'account completato. Il QR precedente serviva alla verifica antiabuso, S222, non dimostra l'attivazione della verifica in due passaggi.

Le nuove immagini mostrano il precedente Gmail personale nei campi email e contatto di recupero. La prima è una casella per il recupero e gli avvisi di sicurezza (S224); il secondo è un aiuto tramite un account invitato, con accettazione e disponibilità da verificare (S223). Sono proprietà diverse dal mittente delle notifiche del NAS. Anche dopo il riepilogo restano quindi passi osservabili separati: completare l'account, verificare il recupero, autorizzare il nuovo account nel NAS, salvare e ricevere un test su Proton. I valori identificanti e il QR rimangono solo nel livello privato.

## La creazione è chiusa, le altre verifiche restano proprie

La nuova sequenza termina nella Home Google autenticata: questo è il riscontro che chiude la creazione dell'identità. Nel flusso sono state scelte cronologie non salvate, annunci non personalizzati e promemoria privacy attivi. Queste preferenze riguardano la personalizzazione dei dati. Non sono una prova della protezione di accesso, che richiede la lettura delle proprie impostazioni.

Per l'account dei servizi si raccomanda la verifica in due passaggi con codici di backup conservati privatamente, S225-S226. Non è un vincolo tecnico aggiunto a Gmail OAuth: è la preparazione dell'identità che autorizzerà il NAS. Il suo stato è ancora da leggere in Security & sign-in, insieme alle opzioni di recupero. La Home invita ad aggiungere un telefono, ma il banner non sostituisce l'inventario dei metodi.

Rimane distinta la prova operativa: consenso OAuth del nuovo account in TrueNAS, salvataggio, destinatario Proton effettivo, messaggio e alert ricevuti, filtro Log NAS. L'account creato rende questi passi possibili; non li chiude. Le credenziali, i QR dell'autenticatore e i codici di backup rimangono in possesso del proprietario, fuori dal racconto e dai documenti pubblici.

Riscontro seguente del27/10/2026: la GUI conferma Authenticator app has been set up e contemporaneamente richiede Turn on 2-Step Verification. Il metodo è stato registrato; l'uso obbligatorio del secondo passaggio non è ancora confermato. La distinzione è visibile nelle stesse schermate, non dedotta da una regola astratta. Indicato il pulsante finale, poi ritorno al NAS senza rifare il setup. I codici di backup sono codici di scorta per accedere quando il secondo passaggio normale non è disponibile (S226); dopo la spiegazione vengono rinviati per avanzare come richiesto dall'utente. Rinviato rimane uno stato distinto da generato e conservato.

## Quando il riscontro smentisce il prossimo passo previsto

Il tentativo successivo non mostra2FA attiva: Google apre Add second steps to your account e indica un metodo come telefono o passkey. Dietro il dialogo Authenticator è già elencato con spunta verde. Il codice dell'app è un secondo fattore; il fatto che il provider rifiuti questo tentativo non cambia la sua natura. Il messaggio non specifica perché quel metodo registrato non soddisfi il criterio di attivazione in questo flusso.

La previsione ultimo clic, poi NAS viene quindi corretta nel registro e nello stato corrente. Si segue il percorso mostrato, Go back e Phone number come proposta concreta; non si aggiungono a tentativi più metodi e non si diagnostica un bug dal solo avviso. S227 documenta dal2024 la possibilità di aggiungere metodi prima di attivare2SV, anche per account personali: aiuta a leggere gli stati, non prova il motivo del blocco attuale. L'attivazione rimane da osservare, i codici di backup restano rinviati e il collegamento OAuth mantiene requisiti distinti.

## L'accesso ordinario non prova il consenso a una modifica sensibile

Il nuovo accesso Chrome arriva alla pagina Google, ma aprire la verifica in due passaggi produce ancora We couldn't verify it's you. Il profilo e la pagina mostrano lo stesso account: scegliere l'identità corretta è necessario, non è prova sufficiente che Google consenta ogni operazione. Il metodo Authenticator registrato, la sessione autenticata, la verifica dell'identità per la modifica e2FA attiva restano quattro riscontri diversi.

S228 documenta separatamente le azioni sensibili, inclusa l'attivazione2FA, e possibili limiti di7giorni quando la verifica non riesce. Propone anche accesso da app Google o Gmail sul dispositivo mobile. È il prossimo percorso indicato, non la promessa di un superamento immediato del controllo. Il caso concreto non espone un timer o una causa verificata, quindi non viene assegnata una data di sblocco.

L'utente chiede di completare2FA ora: il mancato esito non viene trasformato unilateralmente in rinvio o in successo. La prova che chiude la fase è la conferma di attivazione fornita da Google. I codici di backup restano rinviati e il NAS non viene dichiarato già autorizzato. Il pulsante Attiva nel menu Chrome, relativo alla sincronizzazione, non sostituisce quella conferma.

Riscontro mobile seguente del27/10/2026: compare Recovery phone confirmed ed è visibile una passkey Galaxy S25 Ultra non sincronizzabile e non ancora usata. La barra2 verification methods è chiusa e non si legge2-Step Verification attiva. Un recapito confermato e una credenziale presente sono progressi osservabili, ma non vengono chiamati attivazione della protezione globale. Il passo informativo è leggere il contenuto della barra; non aumentare i metodi o accettare ogni raccomandazione della pagina. Il numero di telefono è conservato solo nel livello privato, l'email completa non è visibile nelle due immagini e l'OAuth del NAS resta ancora da eseguire.

## Il consenso concesso non dimostra la consegna e non attiva la2FA

Il28/10/2026 il flusso reale arriva a Gmail credentials have been applied, poi a Email settings updated e al riepilogo GMail OAuth con il mittente salvato. L’autorizzazione del NAS è acquisita e non va rifatta. La notifica Google che TrueNAS ha accesso è generata dal provider; non prova che il NAS abbia inviato una mail. Il test si ferma per email mancante nell’amministratore locale, prima di una consegna osservata. La guida S214 descrive un campo destinatari che qui non è visibile: il messaggio della versione effettiva indirizza la successiva verifica dell’account locale.

Nelle stesse evidenze il telefono mostra esplicitamente2-Step Verification is off pur elencando Authenticator e Google prompt. Consenso applicativo, metodo registrato e protezione globale hanno quindi prove separate. L’email di recupero riceve una copia dell’avviso, ma continua a mostrare Verify: consegna e verifica del recapito sono ancora proprietà diverse. Prossimo aprire2-Step Verification, non ricreare metodi o consenso OAuth.

La registrazione rende il lavoro riprendibile, ma non salva da sola la configurazione del NAS. Il backup con seed e la sua custodia privata restano necessari e non ancora eseguiti, S137/S158. La possibilità di ricostruire i passaggi dai documenti non viene chiamata ripristino collaudato.

## Il criterio di chiusura finalmente osservato

Nel lotto successivo del28/10 la pagina passa da Turn on a Turning on, poi mostra You’re now protected with 2-Step Verification. L’email Google contiene2-Step Verification turned on per la nuova identità. Questo è il riscontro che mancava alle sole voci Authenticator e Google prompt: l’attivazione2FA è chiusa, senza trasformarla in prova di recapito NAS o verifica dell’email di recupero. Non si richiedono altre configurazioni per chiudere questa sottovoce; codici backup restano rinviati.

Per ritrovare gli avvisi, il registro privato conserva casella, evento e orari visibili. Un messaggio aperto sul telefono a una certa ora non prova che sia arrivato allora: il campo dell’header rimane sconosciuto finché non lo si vede. Anche il titolo nel corpo non viene chiamato oggetto SMTP senza leggerne l’intestazione. È la stessa disciplina che distingue una configurazione salvata dal suo risultato operativo.

Riscontro successivo del28/10/2026: Edit User di truenas_admin mostra Email Not Set in Additional Details. Il percorso del destinatario locale è finalmente visibile. Inserire Proton in quel campo non cambia l’account Google che invia tramite OAuth, né il login o la password dell’amministratore. Al momento della lettura il valore è ancora assente e il salvataggio/ricezione rimangono da verificare. Il messaggio del test guida questa configurazione della versione osservata, pur con la differenza rispetto al campo Email Recipients descritto nella guida generale.

Riscontro del28/10/2026 successivo: il recapito è salvato e il nuovo test produce Test email sent; la mail viene ricevuta su Proton. La prova attraversa ora NAS, provider e casella destinataria, senza dedurre la consegna dal solo salvataggio. Ora messaggio12:25 e lettura telefono12:26 nel registro privato, con limiti di data/fuso espliciti. Servizio alert e filtro Log NAS rimangono altri passi; le impostazioni acquisite diventano la prima tappa da salvare con export e seed, ADR-043 e scheda06.

Riscontro del28/10/2026 nel pannello del servizio E-Mail: Enabled selezionato, Warning e Override Admin Email vuoto. S239 spiega che il vuoto eredita il recapito dell’amministratore; il destinatario Proton già nel profilo resta il riferimento senza ricopiarlo in un secondo campo. Il prossimo Send Test Alert verifica il servizio notifiche oltre al trasporto già riuscito. Nessun esito alert è ancora visto e nessuna modifica richiede qui un nuovo export della configurazione.

Riscontro conclusivo del test servizio,28/10/2026: Test alert sent e messaggio This is a test alert ricevuto su Proton con13:01 mostrato. L’override è vuoto e i valori invariati: il percorso ereditato usa il recapito amministratore già salvato. Sono ora provati sia il test posta sia il test sintetico del servizio alert; il filtro Log NAS resta da impostare. Non si provoca un guasto per confermare la stessa consegna e non si riscarica il checkpoint di configurazione senza un cambiamento delle impostazioni.
