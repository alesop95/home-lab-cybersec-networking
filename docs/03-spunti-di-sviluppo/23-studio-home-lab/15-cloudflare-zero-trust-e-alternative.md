# Cloudflare Zero Trust Free nel progetto domestico

Ritorno allo [studio](README.md). Valutazione richiesta il 23/10/2026, basata sulla documentazione ufficiale e sulle decisioni già adottate nel progetto. È uno studio: nessun account creato, software installato, tunnel aperto o criterio di rete modificato. I limiti commerciali sono quelli letti in questa data e vanno ricontrollati prima di un'eventuale adozione.

Approvazione del 23/10/2026: l'utente conferma le raccomandazioni, registrate come ADR-037, e adotta il livello tecnico-didattico con ADR-038. Cloudflare resta un esperimento applicativo facoltativo, non un servizio già adottato; DNS locale e WireGuard amministrativo rimangono le scelte. La [matrice dei bisogni](16-bisogni-controlli-e-flussi.md) espande punti di controllo, confini e prove; il [racconto tecnico-didattico](../../../.claude/context/studio-didattico-master.md) ne segue gli sviluppi.

## Valutazione per questa casa

Cloudflare Zero Trust Free ha senso come esperimento mirato per accedere a una singola applicazione web attraverso un controllo di identità. Non emerge una necessità di adottarlo come protezione generale della casa. Il progetto ha già scelto OPNsense come punto di controllo, VLAN separate, AdGuard Home davanti a Unbound ricorsivo, WireGuard per amministrare da fuori e Wazuh con Suricata per il monitoraggio. Queste sono scelte progettuali, non servizi già tutti in esercizio.

Le priorità restano portare i dispositivi dietro OPNsense, completare switch e access point, provare le regole fra zone, mettere in servizio il DNS locale e collaudare l'accesso WireGuard. Un tunnel cloud non realizza la separazione fra client, IoT, ospiti, laboratorio e storage; quella dipende dai [flussi ammessi fra zone](08-regole-fra-le-zone.md). Il NAS continua il proprio percorso di montaggio in parallelo.

## Le funzioni da distinguere

| Funzione | Utilità possibile | Effetto nel progetto |
|---|---|---|
| Access con Cloudflare Tunnel | login davanti a una specifica applicazione; collegamento iniziato in uscita dal connettore | candidato per un servizio web di prova, senza creare un nuovo accesso amministrativo |
| Cloudflare One Client, già WARP, e accesso a reti private | collegare dispositivi remoti alle risorse autorizzate | si sovrappone al bisogno già assegnato a WireGuard; richiede client, identità e policy |
| Gateway con filtro DNS | applicare categorie e blocchi alle richieste inoltrate a Cloudflare | cambierebbe la scelta di risolvere localmente senza un resolver pubblico a monte |
| Gateway con filtro HTTP/HTTPS | ispezionare destinazioni e contenuti web dei dispositivi gestiti | introduce client, proxy e, per decifrare HTTPS, un certificato radice fidato sul dispositivo |

Access applica le proprie policy prima di inoltrare le richieste alla risorsa. Tunnel usa un connettore che apre connessioni in uscita; la presenza del tunnel non crea da sola una policy Access restrittiva. Sono funzioni da configurare insieme per il caso web qui proposto. Fonti: [tipi di applicazione Access](https://developers.cloudflare.com/cloudflare-one/access-controls/applications/choose-application-type/) e [metodi di connessione](https://developers.cloudflare.com/cloudflare-one/networks/connectivity-options/).

Il filtro DNS può operare anche su una rete senza installare un client su ogni apparato, inoltrando le richieste al resolver Gateway. Questo copre le richieste DNS che lo attraversano, non tutto il traffico né le connessioni laterali interne. Per filtrare il contenuto HTTPS il percorso documentato comprende invece Cloudflare One Client, proxy e decifrazione con certificato radice. La sola attivazione del client non dimostra una protezione completa. Fonti: [filtro DNS](https://developers.cloudflare.com/cloudflare-one/traffic-controls/get-started/dns/) e [filtro HTTP](https://developers.cloudflare.com/cloudflare-one/traffic-controls/get-started/http/).

## Che cosa offre il gratuito e che cosa costa gestirlo

Il [listino Cloudflare](https://www.cloudflare.com/plans/) indica per Zero Trust Free fino a 50 utenti, assistenza di community e conservazione standard dei log fino a 24 ore. Il limite è espresso in utenti, non in dispositivi. È una taglia compatibile con un esperimento domestico, ma i log brevi non sostituiscono lo storico del monitoraggio previsto dal progetto. Non si presume una raccolta automatica di questi log in Wazuh.

Il canone nullo lascia comunque da gestire account, secondo fattore, sessioni, policy, aggiornamenti del connettore e dipendenza dal fornitore. Per un'applicazione con nome pubblico serve anche un dominio disponibile e una configurazione DNS compatibile; l'eventuale registrazione del dominio ha un costo separato. Il connettore deve essere disponibile quando serve l'applicazione: nel progetto il NAS acceso a orario è una collocazione inadatta. Un'eventuale prova userebbe una macchina virtuale o un contenitore separato, quando il server sarà effettivamente disponibile, con accesso al solo servizio sperimentale.

Il compromesso di riservatezza dipende dalla funzione scelta. Inoltrare il DNS a Gateway significa affidargli quelle richieste; abilitare l'ispezione HTTPS significa consentirgli di leggerne il contenuto sul percorso ispezionato. Non si deduce che qualsiasi protocollo cifrato instradato attraverso un tunnel diventi leggibile. Sono decisioni diverse da avere un resolver ricorsivo locale e una VPN verso il proprio firewall.

## Compatibilità con le decisioni esistenti

ADR-007 stabilisce un DNS interno di controllo, con resolver ricorsivo senza delega a un resolver pubblico. Usare Gateway come DNS principale della casa richiederebbe rivedere quella scelta; affiancarlo come DNS alternativo ai client consentirebbe di aggirare il filtro locale e non è una soluzione di ridondanza coerente con il progetto. Il riferimento è la [scheda dei principi di sicurezza](../../../.claude/context/design-and-security.md).

ADR-025 ammette tre ingressi amministrativi: workstation designata, porta di recupero e WireGuard. Pubblicare tramite Access le interfacce di OPNsense, Proxmox o TrueNAS introdurrebbe un altro ingresso, anche se protetto da autenticazione. Per questo lo studio non propone di farlo. Il riferimento operativo resta [Accesso amministrativo](09-accesso-amministrativo.md).

Un eventuale connettore non deve avere accesso indiscriminato alle VLAN interne. Per un'applicazione destinata alla pubblicazione stabile si parte dalla DMZ e dal suo divieto di accesso alla LAN; per una prova si usa un'applicazione non critica in un ambiente isolato, con le sole aperture necessarie. L'uso del tunnel non autorizza implicitamente nuove rotte o eccezioni sul firewall. Sono valutazioni architetturali per questa rete, non limitazioni tecniche generali del prodotto.

## Alternative secondo il bisogno

| Bisogno | Soluzione | Gratuito verificato al 23/10/2026 | Valutazione per il progetto |
|---|---|---|---|
| amministrare casa da fuori, accedere privatamente al NAS | WireGuard su OPNsense | nessun abbonamento al servizio VPN | scelta già adottata; sfrutta l'IP pubblico statico, richiede l'inoltro UDP sul modem e regole sul firewall |
| collegare dispositivi con poco lavoro sul NAT | Tailscale Personal | fino a 6 utenti, dispositivi personali illimitati, 50 risorse con tag incluse e 3 gruppi ACL | alternativa pratica; piano di coordinamento esterno e policy da limitare alle risorse necessarie |
| rete privata con controllo di accesso e possibile gestione in proprio | NetBird | cloud Free: 5 utenti e 100 macchine; Community Edition gratuita da ospitare in proprio | alternativa valida da studiare, ma il controllo gestito in proprio aggiunge un servizio da mantenere |
| filtrare il DNS della casa | AdGuard Home e Unbound | stack locale già previsto | più coerente con ADR-007; occorrono instradamento e regole che impediscano di aggirare il resolver |
| dare accesso con login a una singola applicazione web | Cloudflare Access e Tunnel | entro il piano Free verificato sopra | il caso più interessante per una prova aggiuntiva, separata dalla gestione della rete |

Fonti dei limiti: [Tailscale Personal](https://tailscale.com/pricing), [piani NetBird](https://docs.netbird.io/manage/settings/plans-and-billing) e [distinzione Community/Enterprise NetBird](https://docs.netbird.io/selfhosted/enterprise). La gratuità Community non include automaticamente tutte le funzioni commerciali dell'edizione Enterprise. Per WireGuard il percorso ufficiale è [Road Warrior su OPNsense](https://docs.opnsense.org/manual/how-tos/wireguard-client.html); il confronto con il progetto è in [Accesso remoto VPN](06-accesso-remoto-vpn.md). La vecchia cifra di 100 dispositivi non descrive il nuovo listino Tailscale letto qui: distingue dispositivi personali e risorse con tag.

Per condivisioni SMB, copie e amministrazione del NAS la raccomandazione resta l'accesso privato tramite WireGuard. Un login davanti a un'applicazione web risolve un bisogno diverso dal collegare privatamente i protocolli del NAS. Tailscale e NetBird sono alternative a quel collegamento, non prodotti da sommare tutti insieme.

## Eventuale prova che darebbe informazione

La prova è facoltativa e non è stata richiesta come installazione. Può partire dopo la disponibilità dell'ambiente e delle regole di rete necessarie. Si usa una sola applicazione web di laboratorio, senza dati sensibili e senza interfacce amministrative; nessuna rotta generale verso le VLAN, nessuna modifica al DNS della casa e nessuna ispezione HTTPS dei dispositivi personali. Il secondo fattore si imposta sul provider di identità; un semplice codice ricevuto per posta non viene assunto come prova di autenticazione multifattore.

| Riscontro | Informazione cercata | Esito necessario |
|---|---|---|
| account autorizzato da rete mobile | il percorso funziona dall'esterno | raggiunge soltanto l'applicazione scelta |
| account non autorizzato o sessione anonima | la policy applica davvero il confine di identità | accesso negato; questo è il passo discriminante, una sola prova riuscita non misura la protezione |
| tentativo di aggirare il nome protetto | non esiste un percorso alternativo scoperto verso la stessa applicazione | nessun accesso pubblico che eluda Access |
| revoca dell'accesso e delle sessioni | è possibile togliere l'autorizzazione | il client precedentemente autorizzato perde l'accesso secondo la policy verificata |
| arresto del connettore | l'esperimento non è diventato infrastruttura critica | cade la sola applicazione di prova; DNS locale e accesso amministrativo esistente restano indipendenti |

Si annotano configurazione, tempi di gestione, log realmente disponibili e risultato delle prove positive e negative. Il ritorno indietro riguarda soltanto connettore, applicazione e record creati per l'esperimento. Finché queste misure non esistono, il beneficio operativo è un'ipotesi documentata. Nessun test di questa tabella è stato eseguito.

La raccomandazione approvata dall'utente il 23/10/2026 è completare l'architettura scelta e tenere Cloudflare come studio facoltativo per una singola applicazione. L'adozione come DNS della casa o come ingresso di gestione richiederebbe una decisione esplicita che riveda ADR-007 o ADR-025; questo documento non la prende.

## Raccordo con il requisito assistente del29/10/2026

La valutazione del23/10 e i limiti commerciali qui citati conservano quella data. ADR-045 aggiunge Tailscale come direzione esplicita richiesta per accesso domestico e assistente, superando il suo precedente stato di sola alternativa. Percorso nello [studio17](17-assistente-personale-hermes-nix-e-memoria.md), senza installazioni o subnet già approvate. WireGuard rimane il disegno amministrativo esistente finché il raccordo degli ingressi non è dettagliato; Cloudflare resta studio facoltativo e non diventa VPN, DNS di casa o accesso alle interfacce per effetto del nuovo filone.
