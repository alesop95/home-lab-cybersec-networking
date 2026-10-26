# Studio tecnico-didattico del progetto

Adottato dall'utente il 23/10/2026, ADR-038. Questo è il racconto evolutivo del perché delle scelte. Lo stato corrente rimane nei documenti tecnici e nei registri; qui si conserva il passaggio da una forma di ragionare o documentare a quella successiva, con il caso reale e i compromessi.

Le voci crescono in ordine cronologico e non si riordinano né si riscrivono per uniformarle al presente. Ogni voce porta contesto, situazione precedente, principio adottato e dettaglio. Si parte dall'adozione attuale, senza inventare voci retroattive per tutta la storia del progetto.

La [matrice tecnica dei bisogni](../../docs/03-spunti-di-sviluppo/23-studio-home-lab/16-bisogni-controlli-e-flussi.md) è il riferimento corrente. La prima scheda di dettaglio è [Bisogni, strumenti e punti di controllo](refactor-01-bisogni-controlli-e-flussi.md).

## 1. Dal confronto dei prodotti al percorso che applica il controllo

Contesto. Il 23/10/2026 l'utente ha chiesto se Cloudflare Zero Trust Free servisse alla rete domestica. Ha poi approvato la lettura per bisogni, chiedendo di espanderla nei livelli tecnico e tecnico-didattico e di mantenerla negli sviluppi successivi. In parallelo il NAS era nel BIOS per verificare memoria, dischi e modalità SATA.

Com'era e perché era fragile. La prima tabella dello studio Cloudflare collegava già bisogni e prodotti, e rendeva utile il confronto. Restavano però da esplicitare il punto che prende ogni decisione, le responsabilità che non copre e la differenza fra un'impostazione, una funzione disponibile e un risultato provato. Senza questi campi si rischia di leggere VPN, filtro DNS, login applicativo e monitoraggio come risposte intercambiabili alla parola protezione. La rilettura ha inoltre trovato un residuo concreto nella bozza: PORTE_CONDIVISIONE comprendeva ancora HTTPS per vecchie applicazioni NAS, mentre ADR-032 assegna le applicazioni al server. Non è stato osservato un difetto della rete operativa: gran parte della rete deve ancora essere configurata.

Il salto e perché è meglio. La matrice tecnica lega ogni bisogno a strumento, punto di applicazione, confini e stato. Le spiegazioni seguono un file attraverso WireGuard e i permessi NAS, una richiesta web attraverso Access e Tunnel, e un nome attraverso il DNS. Il caso BIOS mostra lo stesso principio: AHCI osservato e SMART abilitato non sono l'esito di un test lungo del disco. La bozza limita ora le condivisioni NAS a TCP 445 e lascia HTTPS nel perimetro amministrativo: il controllo viene ricondotto al bisogno attuale. Le approvazioni diventano ADR-037 e ADR-038; le fonti restano datate. Il compromesso è mantenere più di un livello documentale, con ruoli distinti: stato tecnico corrente, fatti nel work log e ragionamento storico qui.

Dove leggere il dettaglio: [refactor-01-bisogni-controlli-e-flussi.md](refactor-01-bisogni-controlli-e-flussi.md). Nessuna prova di accesso remoto o configurazione Cloudflare è stata eseguita in questa voce; il riscontro BIOS e la registrazione delle decisioni sono nel registro NAS e nel work log.
