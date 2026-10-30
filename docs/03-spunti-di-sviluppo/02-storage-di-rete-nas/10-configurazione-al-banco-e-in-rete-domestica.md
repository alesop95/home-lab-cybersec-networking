# Configurare il NAS al banco e nella rete domestica

Ritorno allo [storage di rete](README.md). Quadro tecnico del28/10/2026, dopo la creazione di tank e la seconda acquisizione della configurazione con seed. Il [registro del montaggio](09-registro-del-montaggio.md) conserva la cronologia; la [matrice dei bisogni](../23-studio-home-lab/16-bisogni-controlli-e-flussi.md) collega ogni controllo al suo scopo. Le impostazioni avanzate si cambiano quando esistono un bisogno, una dipendenza disponibile e una verifica dell’esito.

## La preparazione che segue la macchina

Sono già osservati installazione TrueNAS25.10.7, localizzazione, accesso amministrativo, posta e alert ricevuti e pool tank in specchio. Dataset per documenti e backup, utenti dei servizi e permessi possono essere progettati e preparati sulla rete temporanea. Le regole che autorizzano client, reti e servizi si verificano nella topologia definitiva. La riuscita dell’accesso aziendale non collauda VLAN, firewall o VPN domestici.

La pagina Advanced Settings presenta funzioni disponibili e valori già impostati; i riquadri vuoti non diventano automaticamente attività mancanti. S241 documenta la presenza di valori iniziali ragionevoli. Nel progetto si procede dal bisogno: il NAS conserva file e copie, mentre applicazioni e macchine virtuali sono previste sul server.

## Lettura dei pannelli e momento della configurazione

| Pannello o ambito | Riscontro al banco | Quando interviene il progetto | Criterio di verifica |
|---|---|---|---|
| rete, fuori da questi pannelli | interfaccia in DHCP sulla LAN temporanea | a casa si applicano indirizzo o prenotazione, gateway, DNS e collocazione nella VLAN30 secondo il piano | accesso dai client previsti e gestione dal percorso amministrativo approvato |
| Allowed IP Addresses | elenco vuoto | con gli indirizzi definitivi si valuta la restrizione della GUI/API, includendo il client amministrativo corrente | accesso ammesso e accesso respinto verificati senza perdere il percorso di recupero |
| Syslog | livello Info, server remoti assenti, Include Audit Logs No | quando esiste il ricevitore e sono definite le regole di rete e la conservazione | un evento del NAS arriva al ricevitore con orario e origine corretti |
| Audit | conservazione7giorni, reservation e quota non impostate, soglie75%/95% | si valuta volume e conservazione richiesti al momento di collegare osservazione e servizi reali | dati effettivamente raccolti, spazio occupato e recupero di un evento |
| NTP Servers | tre nomi Debian già configurati, IBurst Yes, Burst/Prefer No, Min Poll6 e Max Poll10 | verificare la sincronizzazione; eventuale destinazione domestica segue il piano e la connettività | la presenza delle righe non dimostra che l’orologio sia sincronizzato |
| Storage | System Dataset Pool tank; priorità resilver Never | mantenuto ora, senza spostare il dataset di sistema | dato osservato anche nel nuovo export; non equivale ai dataset applicativi dell’utente |
| Replication | limite di esecuzione simultanea5 | quando esistono destinazioni e attività di replica definite | completamento e recupero della replica; il valore5 non conta attività già configurate |
| Access | timeout5minuti e nessun login banner | gestione amministrativa e comodità possono essere valutate separatamente dalla rete | scadenza e accesso coerenti con la politica scelta |
| Console | console testuale senza richiesta password abilitata; seriale disabilitata | rivedere l’accesso fisico e la procedura di recupero prima dell’uso ordinario | accesso locale controllato e recupero ancora praticabile |
| Global Two Factor Authentication | Global2FA Disabled e2FA SSH Disabled | protezione TrueNAS da valutare prima dell’uso ordinario, dopo verifica dell’ora e del recupero | login e recupero provati; è distinta dalla2FA Google già attiva |
| Kernel e Sysctl | kernel di debug disabilitato e nessun parametro personalizzato | nessuna modifica prevista senza un problema concreto da risolvere | un eventuale cambiamento deve produrre un effetto misurabile |
| Cron Jobs e Init/Shutdown Scripts | nessuna voce aggiunta | nessuna personalizzazione richiesta adesso; si preferiscono le funzioni gestite dalla piattaforma | attività definite solo con scopo, responsabilità ed esito verificabile |
| Isolated GPU Devices | nessun dispositivo isolato | nessuna esigenza nel ruolo NAS corrente | nessuna assegnazione GPU o macchina virtuale viene introdotta dalla presenza del pannello |

La lista Allowed IP Addresses vuota ammette gli indirizzi alla GUI/API secondo S241; rimangono autenticazione e controlli della rete. La restrizione va costruita con il percorso amministrativo reale, non con indirizzi provvisori scelti al banco. Il progetto mantiene gestione dalla VLAN99 e dal percorso WireGuard previsto, da collaudare quando disponibili.

La2FA Google protegge l’identità usata per autorizzare l’invio della posta. La2FA TrueNAS riguarda invece l’accesso amministrativo del NAS. Il valore Disabled qui osservato non modifica la conferma Google già acquisita e non riapre quel flusso. S242 richiede un orologio corretto per i codici temporali; la sola lista dei server NTP non chiude questa verifica. Nessuna nuova attivazione è eseguita in questo giro.

## La tappa salvata e il prossimo sviluppo

Sono conservate due generazioni dell’export con seed, prima e dopo la creazione del pool. La seconda contiene il record tank con GUID e la scelta del system dataset pool; l’impronta coincide con il download e SQLite supera quick_check. La copia esterna al NAS è acquisita sul PC operatore; seconda destinazione indipendente, inclusione Veeam e ripristino restano aperti. La [procedura di continuità](../05-strategia-di-backup/10-configurazione-truenas-e-cambio-hardware.md) precisa i limiti.

Il prossimo passo è leggere Datasets e preparare la separazione dei contenuti. Ogni sviluppo aggiunge configurazione osservata, verifica e nuova generazione dell’export al termine della relativa tappa. Al trasferimento a casa si applicano e collaudano le dipendenze di rete senza rifare le impostazioni già valide.

Fonti primarie: S241, [Advanced Settings25.10](https://www.truenas.com/docs/scale/25.10/scaleuireference/systemsettings/advancedsettingsscreen/), per pannelli e significato dei campi; S242, [2FA TrueNAS25.10](https://www.truenas.com/docs/scale/25.10/scaletutorials/systemsettings/advanced/manageglobal2fascale/), per il controllo di accesso e la dipendenza dall’ora. La suddivisione delle attività è applicazione del piano di progetto, ADR-040/043, non un’impostazione eseguita dalla sola lettura.
