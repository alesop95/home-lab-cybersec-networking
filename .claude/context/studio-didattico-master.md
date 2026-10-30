# Studio tecnico-didattico del progetto

Adottato dall'utente il 23/10/2026, ADR-038. Questo è il racconto evolutivo del perché delle scelte. Lo stato corrente rimane nei documenti tecnici e nei registri; qui si conserva il passaggio da una forma di ragionare o documentare a quella successiva, con il caso reale e i compromessi.

Le voci crescono in ordine cronologico e non si riordinano né si riscrivono per uniformarle al presente. Ogni voce porta contesto, situazione precedente, principio adottato e dettaglio. Si parte dall'adozione attuale, senza inventare voci retroattive per tutta la storia del progetto.

La [matrice tecnica dei bisogni](../../docs/03-spunti-di-sviluppo/23-studio-home-lab/16-bisogni-controlli-e-flussi.md) è il riferimento corrente. La prima scheda di dettaglio è [Bisogni, strumenti e punti di controllo](refactor-01-bisogni-controlli-e-flussi.md).

## 1. Dal confronto dei prodotti al percorso che applica il controllo

Contesto. Il 23/10/2026 l'utente ha chiesto se Cloudflare Zero Trust Free servisse alla rete domestica. Ha poi approvato la lettura per bisogni, chiedendo di espanderla nei livelli tecnico e tecnico-didattico e di mantenerla negli sviluppi successivi. In parallelo il NAS era nel BIOS per verificare memoria, dischi e modalità SATA.

Com'era e perché era fragile. La prima tabella dello studio Cloudflare collegava già bisogni e prodotti, e rendeva utile il confronto. Restavano però da esplicitare il punto che prende ogni decisione, le responsabilità che non copre e la differenza fra un'impostazione, una funzione disponibile e un risultato provato. Senza questi campi si rischia di leggere VPN, filtro DNS, login applicativo e monitoraggio come risposte intercambiabili alla parola protezione. La rilettura ha inoltre trovato un residuo concreto nella bozza: PORTE_CONDIVISIONE comprendeva ancora HTTPS per vecchie applicazioni NAS, mentre ADR-032 assegna le applicazioni al server. Non è stato osservato un difetto della rete operativa: gran parte della rete deve ancora essere configurata.

Il salto e perché è meglio. La matrice tecnica lega ogni bisogno a strumento, punto di applicazione, confini e stato. Le spiegazioni seguono un file attraverso WireGuard e i permessi NAS, una richiesta web attraverso Access e Tunnel, e un nome attraverso il DNS. Il caso BIOS mostra lo stesso principio: AHCI osservato e SMART abilitato non sono l'esito di un test lungo del disco. La bozza limita ora le condivisioni NAS a TCP 445 e lascia HTTPS nel perimetro amministrativo: il controllo viene ricondotto al bisogno attuale. Le approvazioni diventano ADR-037 e ADR-038; le fonti restano datate. Il compromesso è mantenere più di un livello documentale, con ruoli distinti: stato tecnico corrente, fatti nel work log e ragionamento storico qui.

Dove leggere il dettaglio: [refactor-01-bisogni-controlli-e-flussi.md](refactor-01-bisogni-controlli-e-flussi.md). Nessuna prova di accesso remoto o configurazione Cloudflare è stata eseguita in questa voce; il riscontro BIOS e la registrazione delle decisioni sono nel registro NAS e nel work log.

## 2. Dalla capacità progettata alla memoria realmente disponibile

Contesto. Il26/10 l'utente ha chiesto perché il NAS fosse rimasto a8 GB, che uso dare alle altre tre RAM e un riepilogo dell'intero hardware. I tre SSD avevano completato i test estesi; la chiavetta TrueNAS veniva preparata.

Com'era e perché era fragile. L'allocazione continuava a mostrare NAS16 GB, server24 GB e due Crucial di scorta, mentre gli aggiornamenti del banco avevano escluso tre moduli da8 GB e impegnato RAM-03 nel NAS. Una tabella di destinazioni future veniva letta come inventario fisico, contando due volte pezzi non disponibili. Anche la parola scorta lasciava credere che un modulo con errori diventasse utile cambiandogli ruolo.

Il salto e perché è meglio. L'inventario distingue capacità censita, prova osservata, assegnazione e proposta. Si contano24 GB DDR4 senza errori segnalati, con la differenza fra RAM-03 provata e Crucial soltanto censiti; i tre moduli con errori rimangono separati. I confronti8/16,12/12 e16/8 esplicitano dove si toglie memoria per aumentarla altrove. Il limite è scegliere consapevolmente una base NAS con meno margine e preservare memoria per il server, senza dichiarare già misurate le prestazioni o impossibile un futuro recupero dei moduli.

Dove leggere il dettaglio: [refactor-02-inventario-e-ram-nas.md](refactor-02-inventario-e-ram-nas.md). ADR-039 registra l'obiettivo finale NAS16 GB precisato dall'utente:8 GB restano lo stato fisico, il secondo modulo è da rendere utilizzabile. L'utente autorizza una prova mirata16 GB conRAM-03/A2 eRAM-01/B2; le scorteRAM-02/04 conservano gli errori registrati.

Sviluppo successivo del 26/10/2026. La coppia RAM-03/A2 + RAM-01/B2 è stata montata e riconosciuta dal BIOS a 16 GB, poi ha fallito Memtest prima del primo passaggio completo. La scheda 02 è ampliata con la differenza fra volatilità e integrità: un dato può essere alterato mentre è in RAM e poi diventare persistente sul disco, anche sulle due copie del mirror. Il confronto Expected/Found della prova reale mostra un bit diverso; non viene trasformato in una percentuale inventata di file corrotti. La prova della coppia è conclusa negativamente, l'obiettivo 16 GB resta aperto.

## 3. Separare la preparazione della macchina dalla rete in cui si trova

Contesto. Il27/10 il primo boot TrueNAS è documentato in17 foto. Il NAS si trova temporaneamente in azienda e deve poi andare a casa; l'utente teme di configurare cose da rifare. La console non mostra un indirizzo web e la scheda enp3s0 risulta già in DHCP.

Com'era e perché era fragile. La riga Storage di rete di STACK continuava a dire non installato. Usare una sola etichetta per installazione, accesso web e rete finale rendeva invisibile il progresso reale e trasformava la futura collocazione in una premessa per qualunque attività. Si rischiava di inserire indirizzi domestici nella rete temporanea o di rimandare anche impostazioni indipendenti dall'indirizzo.

Il salto e perché è meglio. Si registrano separatamente sistema avviato, indirizzo, login e rete definitiva. DHCP già Yes è un riscontro, non un'azione appena compiuta: prima si legge il collegamento. Dopo accesso si preparano localizzazione, stato del boot-pool ed export; IP e accessi domestici si verificano nel luogo previsto. Il compromesso è dover rivedere rete ed export al trasferimento, senza scambiare la preparazione per un collaudo finale. Nessun valore IP, pool o servizio è inventato come già configurato.

Dove leggere il dettaglio: [refactor-03-preparazione-nas-e-rete-temporanea.md](refactor-03-preparazione-nas-e-rete-temporanea.md). Piano tecnico nel registro NAS, scelta operativa in ADR-040. Accesso web e indirizzo ancora aperti al momento della voce.

Sviluppo del27/10/2026: ottenuto il lease DHCP sulla LAN temporanea e osservato il login amministrativo, lo stato corrente avanza nella scheda03 senza riscrivere i limiti iniziali. General Settings mostra ancora fuso e tastiera da adattare. La stessa scheda distingue ora generazione, trasporto e destinazione degli avvisi, in seguito alla preferenza Proton e raccolta Log NAS: il metodo salvato, la consegna e il filtro richiedono riscontri propri. Studio della posta dai server domestici rinviato; nessun server di posta configurato, ADR-041.

Sviluppo ulteriore del27/10/2026: la selezione GMail OAuth è ora visibile nel modulo, prima di consenso e salvataggio. Alla domanda sul cambio di browser e rete, la scheda03 aggiunge la differenza fra autorizzazione del servizio salvata nel NAS e percorso usato per aprirne la GUI. Il primo accompagna la macchina finché valido; il secondo richiede connettività e accessi verificati. Nessun login o invio ancora osservato, fonti S214 e S217.

## 4. Tipo di account e ruolo dei servizi domestici

Contesto. Durante la configurazione degli avvisi, l'utente chiede perché usare il proprio Gmail e propone un nuovo account Google personale per le esigenze della rete domestica, riutilizzabile in altri servizi. Il pannello OAuth è aperto ma nessuna autorizzazione è completata.

Com'era e perché era fragile. Il metodo GMail OAuth era stato scelto senza fissare esplicitamente quale identità lo avrebbe autorizzato. Mittente, account locale del NAS, destinatario e nome visualizzato potevano sembrare la stessa cosa. Anche la parola personale aveva due significati: il tipo di account offerto da Google e l'account abituale dell'utente. Il suggerimento di usare il Gmail personale avrebbe legato il servizio a un'identità non scelta per quel ruolo.

Il salto e perché è meglio. ADR-042 fissa un normale account Google personale nel ruolo di servizi domestici, inizialmente mittente del NAS e riutilizzabile in integrazioni compatibili da valutare. Proton resta destinatario e From Name un'etichetta. La matrice tecnica nomina ora la nuova identità ancora da creare. Il compromesso è concentrare le future autorizzazioni in un account unico: la gestione resta semplice, con permessi e dipendenze da valutare quando si aggiunge un servizio. Non si crea un progetto Google Cloud per risolvere il solo invio email.

Dove leggere il dettaglio: [refactor-04-identita-google-e-notifiche.md](refactor-04-identita-google-e-notifiche.md). Registro NAS per i campi effettivi e la prova futura; fonti S214 e S218-S220. Account, OAuth salvato e consegna non sono ancora osservati.

Sviluppo della voce4,27/10/2026: la Home Google autenticata chiude ora la creazione dell'account. La scheda04 distingue le preferenze privacy scelte nel flusso dalla protezione di accesso ancora da leggere e dall'OAuth del NAS ancora da autorizzare. Raccomandati verifica in due passaggi e codici di backup privati; nessun secondo fattore o recapito già accreditato dalle sole schermate.

Sviluppo della voce4,28/10/2026: Gmail OAuth è autorizzato e salvato sul NAS; il test resta fermo per recapito amministratore mancante. Il successivo dialogo Google e il corpo dell’email chiudono invece l’attivazione2FA della nuova identità. La scheda04 distingue la conferma del provider dal messaggio inviato dal NAS e registra il limite degli orari: lettura sul telefono, notifica e ricezione dell’header non sono automaticamente lo stesso evento.

## 5. La motivazione del NAS deve descrivere la macchina attuale

Contesto. Il28/10/2026 l’utente chiede che sia comprensibile perché è stato scelto TrueNAS rispetto a OpenMediaVault, mentre procede la configurazione degli avvisi. La decisione ADR-026 esiste, ma il confronto tecnico è ancora quello dell’8/10.

Com’era e perché era fragile. La conclusione usava32GB, avvio in specchio e NVMe nel NAS, superati da ADR-033 e dagli esiti della memoria. Alcune frasi lasciavano intendere perdita automatica di ZFS con OMV o assenza generale di controlli in Btrfs. La decisione poteva sembrare obbligata da vantaggi non più presenti.

Il salto e perché è meglio. Il confronto parte dai problemi dei documenti e delle copie, distingue proprietà ZFS e integrazione della piattaforma e riconosce il plugin OMV con snapshot, scrub e replica. La preferenza TrueNAS viene spiegata con il suo costo di memoria e le condizioni in cui OMV avrebbe senso. La macchina presente è8GB, avvio singolo, pool dati ancora assente: i benefici desiderati diventano passi da configurare e verificare, non risultati già acquisiti. Non cambiamo il sistema operativo per correggere una motivazione scritta male.

Dove leggere il dettaglio: [scheda05](refactor-05-scelta-truenas-e-alternativa-omv.md), con estratti reali prima/dopo del [confronto tecnico](../../docs/03-spunti-di-sviluppo/02-storage-di-rete-nas/08-valutazione-openmediavault.md). Fonti primarie S74,S204,S231-S236; nessun benchmark o nuova prova hardware.

## 6. Conservare le impostazioni, non soltanto il racconto dei passaggi

Contesto. Il28/10 la mail NAS arriva su Proton. L’utente chiede che anche le configurazioni sopravvivano al guasto o alla sostituzione hardware e ricorda il lavoro Veeam Linux già disponibile.

Com’era e perché era fragile. La procedura NAS-01 prevedeva l’export ma il primo file era ancora una pendenza. Registro e fotografie ricostruivano i clic, senza costituire un database di configurazione recuperabile. Il riferimento generico a backup Linux poteva inoltre confondere un backup file già verificato altrove con il ripristino di questa appliance.

Il salto e perché è meglio. ADR-043 lega la tappa riuscita al primo export con seed, versioni fuori NAS e verifica del file. Impostazioni, dati e materiali esterni hanno percorsi distinti. Il materiale Veeam viene ritrovato e riusato con il suo perimetro di prova, non trasformato in una copertura NAS già esistente. Il cambio hardware conserva l’impianto logico ma richiede la verifica dei collegamenti reali. Il primo export resta da scaricare e non dichiariamo un recupero già collaudato.

Dove leggere il dettaglio: [scheda06](refactor-06-configurazione-nas-e-continuita.md), con estratti reali prima/dopo e [procedura tecnica](../../docs/03-spunti-di-sviluppo/05-strategia-di-backup/10-configurazione-truenas-e-cambio-hardware.md). Fonti S137,S158,S237,S238; nessuna nuova installazione Veeam o prova hardware.

Avanzamento della voce6,28/10/2026: primo export TrueNAS con seed acquisito e copiato fuori NAS, integrità dell’archivio e del database controllata, campi della tappa riscontrati senza pubblicare segreti. La scheda06 mantiene distinta questa acquisizione dal ripristino su nuova installazione e dalla seconda destinazione indipendente, ancora da verificare.

## 7. La cifratura deve avere un percorso di recupero

Contesto. Nel wizard del pool compaiono Encryption e il primo VDEV Mirror. I dischi sono identificati ma non ancora assegnati; il pool non esiste ancora.

Com’era e perché era fragile. La guida distingueva export e passphrase, senza legare quella distinzione alla casella del pool. Aggiungere protezione senza definire custodia e ambito dei materiali di sblocco avrebbe lasciato incompleto il recupero.

Il salto e perché è meglio. La raccomandazione S240 viene collegata alla scelta dei dataset e al piano di recupero. La matrice separa conservazione, cifratura e copia esterna; lo stato distingue campi del wizard, configurazione applicata e recupero provato. Non si accredita una cifratura già eseguita.

Dove leggere il dettaglio: [scheda07](refactor-07-pool-dataset-e-cifratura.md), con estratti reali della [procedura](../../docs/03-spunti-di-sviluppo/05-strategia-di-backup/10-configurazione-truenas-e-cambio-hardware.md). Dataset e recupero ancora da configurare e verificare.

Avanzamento della voce7,28/10/2026: un solo Mirror contiene ora WD e SanDisk; Save Selection e Review sono osservati, con223.57GiB stimati. La scheda07 distingue il salvataggio della selezione dalla creazione effettiva del pool e la capacità grezza stimata dallo spazio netto dei file. Pool dati ancora non creato.

Avanzamento della voce7,28/10/2026: tank è ora creato e Online no errors, con213.19GiB utilizzabili mostrati dalla dashboard. La scheda07 distingue questo riscontro dalla preview grezza, da una prova di recupero e dal nuovo export con seed ancora da acquisire. La pendenza sulla creazione è chiusa nei riepiloghi correnti, senza attribuire al primo archivio configurazioni successive.

Sviluppo della voce3,29/10/2026: la domanda sui molti pannelli Advanced Settings estende la distinzione banco/rete. La scheda03 e la nuova guida tecnica10 collegano ogni parametro a bisogno, dipendenza e verifica: preparazione locale, rete definitiva o funzione speciale ancora non richiesta. Global2FA NAS Disabled resta distinta dalla2FA Google attiva; il nuovo export con seed post-tank è acquisito e verificato, senza prova di restore già attribuita.

## 8. La struttura dei dati deve durare più dei componenti

Contesto. Il29/10, prima di creare i dataset utente, l’utente richiede esplicitamente scalabilità con SSD più capienti, altra RAM e cambiamenti della macchina.

Com’era e perché era fragile. Le schede descrivevano con precisione240GB nominali e8GB di RAM, e il recupero delle impostazioni era già previsto. Mancava una spiegazione di come quella fotografia potesse crescere mantenendo la struttura logica, senza trasformare misure iniziali in vincoli permanenti.

Il salto e perché è meglio. ADR-044 assegna nomi e permessi alle funzioni dei dati e rende espliciti quote rivedibili, crescita progressiva dello stesso mirror e aumento di memoria compatibile. Il cambio completo della macchina continua nel percorso ADR-043. Si distingue il requisito adottato dall’upgrade ancora non eseguito; la capacità futura sarà verificata dopo l’intervento, non promessa dal firmware.

Dove leggere il dettaglio: [scheda08](refactor-08-crescita-nas-e-struttura-logica.md) e [guida tecnica NAS11](../../docs/03-spunti-di-sviluppo/02-storage-di-rete-nas/11-crescita-del-nas-e-indipendenza-dall-hardware.md), con fonti S243-S246 e riscontri della pagina Datasets.

Sviluppo della voce7,29/10/2026: modulo avanzato tabellato nella guida NAS12; chiave automatica scelta dall’utente, non ancora applicata. La scheda07 collega eredità, ACL NFSv4, mirror, Copies e recupero al loro effetto reale, distinguendo Save abilitato da dataset creato.

## 9. Un assistente personale deve avere confini e memoria portabile

Contesto. L’utente apre il filone a basso consumo con Hermes, Nix/NixOS e Tailscale e aggiunge un brain con Obsidian da sviluppare prima nel template.

Com’era e perché era fragile. VPN, modello locale e catalogo pacchetti esistevano separatamente. La scheda STACK conservava Tailscale come prima fase mentre il confronto successivo lo lasciava come sola alternativa. Nomi di strumenti e handoff potevano sembrare una configurazione già decisa e funzionante.

Il salto e perché è meglio. ADR-045 e studio17 collegano agente, modello, archivio personale, ambiente ricostruibile e rete per bisogno. Si riutilizzano le capacità già censite senza duplicare la memoria del lab; il consumo va misurato sullo stesso compito e lo stato applicativo va recuperato oltre ai pacchetti. Tailscale diventa una direzione richiesta, senza rotte già applicate. Jev si identifica alla tappa del template, come indicato dall’utente.

Dettaglio nella [scheda09](refactor-09-assistente-e-memoria-personale.md) e nello [studio17](../../docs/03-spunti-di-sviluppo/23-studio-home-lab/17-assistente-personale-hermes-nix-e-memoria.md). Fonti S250-S260; nessuna installazione, acquisto o prova di consumo/recupero eseguita.

## 10. Una VPN di uscita e l’accesso a casa richiedono identità diverse

Contesto. Il29/10 l’utente richiama il rapporto NordVPN per il non uso domestico e le cautele dell’account condiviso, mentre procede la lettura delle ACL NAS.

Com’era e perché era fragile. Il rapporto citava il solo WireGuard, mentre il progetto aveva appena richiesto Tailscale per l’assistente. Gli appunti storici negavano troppo in generale la protezione del canale e riducevano tutti i componenti accessori al DNS; Android sempre attiva e blocco fuori VPN rischiavano di essere confusi.

Il salto e perché è meglio. ADR-046 e studio18 separano uscita commerciale, identità condivisa e ingresso domestico, conservano Tailscale e registrano funzioni, punti di controllo e verifiche reali. La fonte locale resta intatta; qui si precisano i limiti con fonti primarie. La stessa disciplina richiede l’identità del dataset prima di attribuire POSIX/Discard al figlio NAS.

Dettaglio nella [scheda10](refactor-10-vpn-commerciale-e-accesso-domestico.md) e nello [studio18](../../docs/03-spunti-di-sviluppo/23-studio-home-lab/18-nordvpn-account-condiviso-e-confini-domestici.md), fonti S261-S268. Nessuna modifica del telefono o della rete e nessun test di raggiungibilità già eseguiti.

## 11. Firmware piccolo e host dell’assistente hanno bisogni diversi

Contesto. L’utente propone strumenti browser per ESP32/Arduino, piccoli nodi Wi-Fi e minimo consumo per Hermes.

Com’era e perché era fragile. La parola microserver poteva far scegliere una MCU al posto di Linux, contare il Pico audio come SBC disponibile o usare il consumo in sonno per promettere un servizio sempre pronto.

Il salto e perché è meglio. ADR-047 separa firmware, host e inferenza, conferma il prototipo prima dell’acquisto e associa SSID alle zone per fiducia. La misura confronta disponibilità e compito uguali. Dettaglio nella [scheda11](refactor-11-firmware-agente-e-vlan.md) e studio19; nessun watt o isolamento già misurato.

## 12. La copertura si dimostra sul rischio concreto

Contesto. L’utente richiede ISO27001/GDPR, aggiornamento OPNsense e un ponte Codex realmente presente e propagabile.

Com’era e perché era fragile. Il controllo degli adattatori restava verde senza AGENTS.md. Analogamente versione nominale, export e skill avrebbero potuto essere scambiati per patch, recupero e conformità.

Il salto e perché è meglio. Il generatore ora verifica l’ingresso, la passata lo gestisce a monte e le prove esercitano il ponte mancante. ADR-048 associa rischi e prove al perimetro domestico reale;26.7.7 richiede anche il hotfix successivo. Dettaglio nella [scheda12](refactor-12-rischio-e-prove-di-recupero.md) e studi20/21. Propagazione globale e prove sui servizi restano passi distinti.
