---
covers-paths: ["docs/03-spunti-di-sviluppo/23-studio-home-lab/15-cloudflare-zero-trust-e-alternative.md", "docs/03-spunti-di-sviluppo/23-studio-home-lab/16-bisogni-controlli-e-flussi.md", "docs/03-spunti-di-sviluppo/23-studio-home-lab/08-regole-fra-le-zone.md", "docs/03-spunti-di-sviluppo/23-studio-home-lab/09-accesso-amministrativo.md"]
last-verified-commit: c1f6eb0e8852e0913c373f08e01f3a9a8947c33b
---

# Refactor 01 - Distinguere bisogno, collegamento e decisione di accesso

Scheda del 23/10/2026, avvio del livello tecnico-didattico approvato con ADR-038. Ritorno al [racconto](studio-didattico-master.md) e alla [matrice tecnica corrente](../../docs/03-spunti-di-sviluppo/23-studio-home-lab/16-bisogni-controlli-e-flussi.md).

L'ancora identifica HEAD del branch osservato all'inizio del lavoro. Gli estratti prima e dopo sono stati acquisiti dai file reali nell'albero di lavoro del 23/10, prima del commit manuale: lo studio Cloudflare era ancora una modifica locale. Non si attribuisce a quel commit una configurazione di rete che non contiene. Il repository documenta il lab; i frammenti seguenti sono sorgente Markdown delle regole proposte e delle spiegazioni, non configurazioni già applicate agli apparati.

## Le fondamenta

Un bisogno è un risultato atteso: leggere un file, amministrare un apparato o impedire a un ospite di raggiungere il NAS. Una connessione è il percorso attraverso cui il traffico arriva a destinazione. Una policy è la decisione che consente o nega una richiesta in un punto preciso. Una misura è il riscontro che permette di sapere se quel risultato si è verificato.

Una VPN[^1] rende disponibile un percorso cifrato tra estremi autorizzati, ma lungo quel percorso possono esistere regole del firewall e permessi dell'applicazione. Un filtro DNS[^2] decide sui nomi richiesti, prima che avvenga la connessione al servizio. Un controllo di identità applicativo decide invece chi può usare quella risorsa e per quanto tempo. Il fatto che tutti concorrano alla sicurezza non li rende intercambiabili.

Nel nostro progetto la separazione tra VLAN[^3] definisce le zone, OPNsense governa i passaggi instradati e i servizi applicano i propri permessi. La presenza di Cloudflare, di un tunnel o di un allarme non realizza da sola tutte queste decisioni.

## Il problema, partendo dal caso vero

La domanda era se il piano gratuito Cloudflare avesse senso per proteggere la casa. La risposta per bisogni è stata approvata e l'utente ha chiesto di renderla un metodo di studio permanente. Il rischio da evitare è documentale: comprare o attivare una funzione perché il nome del prodotto sembra coprire tutto, senza sapere dove viene presa la decisione e che cosa si è realmente verificato.

La sezione Alternative secondo il bisogno del file 15 conteneva questo estratto reale:

```markdown
| Bisogno | Soluzione | Gratuito verificato al 23/10/2026 | Valutazione per il progetto |
|---|---|---|---|
| amministrare casa da fuori, accedere privatamente al NAS | WireGuard su OPNsense | nessun abbonamento al servizio VPN | scelta già adottata; sfrutta l'IP pubblico statico, richiede l'inoltro UDP sul modem e regole sul firewall |
```

La tabella era già utile: nominava il bisogno e il prodotto coerente. Il limite era lasciare implicita la catena delle decisioni e la prova che ne misura l'effetto. La modifica attuale la espande, senza inventare una rete precedente compromessa o sostituire la storia delle decisioni.

## Il principio della soluzione

Si segue la richiesta fino al punto che la può ammettere o negare. Per ogni bisogno si documentano anche il controllo successivo, ciò che resta fuori e lo stato di messa in opera. La prima riga della nuova matrice tecnica è realmente questa:

```markdown
| Bisogno concreto | Strumento scelto o candidato | Dove si applica il controllo | Che cosa resta fuori | Stato |
|---|---|---|---|---|
| amministrare firewall, switch, AP e NAS da fuori casa | WireGuard su OPNsense, poi credenziali delle interfacce | chiave del dispositivo al tunnel; regole verso la VLAN 99; autenticazione del servizio | il tunnel non autorizza ogni porta e non filtra automaticamente la navigazione Internet | deciso, ADR-025 e ADR-037; collaudo da eseguire |
```

Il nuovo campo sul punto di applicazione impedisce di saltare direttamente da VPN a permesso del file. Quello sui confini chiarisce che un collegamento remoto non filtra implicitamente tutta la navigazione. Lo stato conserva la differenza fra una scelta approvata e il suo collaudo. Le quote commerciali restano nello studio Cloudflare datato, invece di essere copiate in ogni scheda.

## Il percorso reale previsto dalle regole

La rilettura del file 08-regole-fra-le-zone.md ha trovato un caso concreto. L'alias della prima stesura era questo:

```markdown
| PORTE_CONDIVISIONE | porte | TCP 445, TCP 443 | SMB e interfaccia web delle applicazioni del NAS |
```

La porta 443 serviva alla vecchia idea di applicazioni sul NAS. ADR-032 ha separato quel ruolo, e la gestione amministrativa è stata collocata nella VLAN 99. Lasciare la porta nell'alias generale avrebbe conservato un'autorizzazione non motivata dal piano attuale. La bozza è quindi riallineata così:

```markdown
| PORTE_CONDIVISIONE | porte | TCP 445 | sole condivisioni SMB; gestione HTTPS separata nella VLAN 99 |
```

Questa è una correzione della proposta documentale, non una regola applicata oggi. La gestione HTTPS resta nelle regole amministrative su indirizzi e porte propri. La regola di condivisione rimane strutturalmente questa:

```markdown
| 3 | consenti | TCP | WG_RETE | NAS | PORTE_CONDIVISIONE | file da fuori |
```

La rete del tunnel è la sorgente autorizzata; il NAS è la destinazione; l'alias PORTE_CONDIVISIONE è ora limitato a TCP[^4] 445. La regola non significa che qualunque porta del NAS sia aperta. Non sostituisce nemmeno i permessi della condivisione: un dispositivo può arrivare al servizio e non avere il diritto di leggere una certa cartella.

Per la gestione il documento 09-accesso-amministrativo.md prevede il perimetro della VLAN 99, credenziali del servizio e secondo fattore dove previsto. WireGuard riconosce il peer attraverso la sua chiave; l'autenticazione del servizio dentro il tunnel rimane un controllo distinto. La prova futura deve mostrare sia un accesso consentito sia il rifiuto di un accesso non previsto.

Nel caso di una singola app web, Cloudflare Access svolgerebbe invece la decisione di identità davanti all'applicazione, mentre Tunnel fornirebbe il percorso attraverso il connettore. Questa funzione può essere comoda per un familiare con il browser. Non autorizza il connettore a raggiungere ogni rete e non crea un quarto ingresso amministrativo accettato da ADR-025.

## Il parallelo osservato nel BIOS

Il lavoro sul NAS ha reso concreta la differenza fra impostazione e risultato. Il 23/10 il BIOS ha mostrato SATA Mode Selection su AHCI[^5], controller abilitato e SMART Self Test su On. La prima lettura conferma come il controller presenta i dispositivi al sistema. Il commutatore SMART[^6] è un valore di configurazione: nella schermata non c'è l'esito di un test lungo di ogni SSD.

Allo stesso modo, vedere un banner PASS durante Memtest non dice quanti passaggi siano stati completati. Il registro conserva separatamente l'avvio osservato, il PASS riferito, le circa 22 ore senza fail riferite per RAM-03/A2 e l'errore visibile di RAM-04 nello stesso slot. La spiegazione può confrontare questi dati, ma non aggiungere contatori mai acquisiti o dichiarare sano ogni componente comune.

Questa distinzione non allunga automaticamente il collaudo. Quando una prova è già fallita la si ferma; quando il confronto ha dato un risultato sufficiente si passa alla domanda successiva. Il presidio è sapere quale domanda si sta misurando.

## Le domande di dosaggio

Un nuovo prodotto è giustificato quando copre un bisogno che la catena attuale non soddisfa con un costo operativo accettabile. Se il bisogno è amministrare la rete, la raccomandazione approvata resta WireGuard su OPNsense. Se è dare a una persona una sola pagina web non critica, il test facoltativo Access e Tunnel diventa interessante. Se è filtrare il DNS della casa, il progetto ha già scelto AdGuard Home e Unbound e non modifica ADR-007 per aggiungere una funzione sovrapposta.

Non ogni foto richiede una nuova scheda didattica: la lettura puntuale si registra nel documento tecnico e nel work log. Quando il passo introduce una distinzione significativa, una decisione o una modifica della spiegazione, aggiunge una voce al racconto e la propria scheda. Non si rimanda la spiegazione a una soglia di casi che nessuno conta.

## Che cosa protegge questa scelta dal tornare indietro

CLAUDE.md rende il metodo un'istruzione di progetto, ADR-038 ne registra l'adozione e le nuove voci del work log dichiarano il collegamento didattico oppure la ragione per cui non ne serve uno nuovo. I collegamenti rendono raggiungibili la matrice tecnica e il racconto a chi riprende la sessione.

I controlli di collegamenti, tabelle e anonimizzazione verificano proprietà meccaniche dei file. Non dimostrano che una spiegazione sia buona né che una policy di rete funzioni. Non è stato introdotto un nuovo controllo automatico che possa garantire da solo la completezza semantica di questo metodo. Le prove positive e negative descritte per l'accesso remoto restano da eseguire sugli apparati.

## Come si estende

Al prossimo sviluppo si parte dalla domanda operativa, si identifica il controllo e si stabilisce la prova che distinguerebbe successo e fallimento. Si aggiornano il riferimento tecnico e il registro dei fatti con la fonte del riscontro. Una scelta non ovvia aggiunge una nuova voce cronologica e un dettaglio autoconsistente; le voci precedenti non vengono riscritte per far sembrare il passato uguale al presente.

Un lettore futuro può così sapere sia quale percorso il progetto prevede oggi sia perché è stato scelto. Lo storico didattico conserva i ragionamenti; la matrice tecnica conserva la risposta attuale; il collaudo conserva ciò che è stato davvero osservato.

[^1]: VPN, Virtual Private Network: collegamento privato realizzato attraverso un'altra rete.
[^2]: DNS, Domain Name System: sistema che traduce i nomi in informazioni utili a raggiungere i servizi.
[^3]: VLAN, Virtual Local Area Network: separazione logica di reti sul livello di collegamento.
[^4]: TCP, Transmission Control Protocol: trasporto usato, fra gli altri, dai servizi sulle porte citate.
[^5]: AHCI, Advanced Host Controller Interface: modalità del controller SATA letta nel BIOS.
[^6]: SMART, Self-Monitoring, Analysis and Reporting Technology: informazioni e funzioni diagnostiche esposte dai dispositivi di memorizzazione.
