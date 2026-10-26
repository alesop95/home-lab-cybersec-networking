---
generated-from-commit: 86b5c8a61a55a48997d7757592aa4d91da9e8581
generated-from-branch: main
generated-date: 2026-08-25
covers-paths:
  - docs/**
last-verified-commit: ee63b19
---

# Roadmap

> Scheda tecnica. Fasi del progetto in ordine di dipendenza, non di preferenza: ogni fase assume che la precedente sia chiusa, e saltarne una produce lavoro da rifare. Le date non sono impegni: sono l'ordine in cui le cose possono accadere.

## Fase 0, conclusa: raccolta e studio

Durata effettiva dal gennaio al marzo 2026, con code successive. Ha prodotto il documento sorgente nella sua estensione attuale, il ticket all'operatore con l'esclusione del collegamento diretto del firewall all'ONT per questa linea, evidenza locale e non generalizzata, la richiesta e l'ottenimento dell'indirizzo pubblico statico, il confronto fra le distribuzioni firewall, la scelta dello switch con le due alternative scartate, e l'installazione del sistema operativo del firewall il 16 gennaio 2026.

L'esito architetturale della fase è uno solo e vale tutto il resto: il firewall non può essere l'apparato di frontiera, quindi la topologia è a cascata dietro il modem dell'operatore, con doppio NAT e wireless inizialmente scoperto.

## Fase 1, conclusa il 25/08/2026: documentazione versionata e pubblicabile

Il materiale scritto a mano è diventato documentazione versionata, anonimizzata e verificata, e il repository è allineato al remoto con i quattro controlli verdi. Il modello di manutenzione è definitivo: la documentazione si scrive a mano nel repository, non si genera più da un documento esterno (ADR-010).

Dal 07/10/2026 il lavoro documentale continua in tre forme decise dall'utente: `docs/` è l'unica fonte dopo l'eliminazione dei testi originali (ADR-019); ogni documento dell'autore si riscrive al suo posto come documento tecnico, con verifica di copertura (ADR-020); il censimento dei dispositivi segue una scheda a campi fissi (ADR-021).

## Fase 2: configurazione del firewall

È il primo lavoro che cambia lo stato della rete, e dipende dalla fase 1 solo nel senso che conviene avere la documentazione in ordine prima di modificarla.

Si comincia identificando fisicamente le tre interfacce dalla console del firewall, correlando nome di driver, indirizzo hardware e connettore con la verifica a LED. Si prosegue con l'assegnazione dei ruoli, ricordando che dopo l'assegnazione il firewall crea una regola permissiva sulla sola LAN mentre le altre zone partono chiuse in ingresso, quindi un errore di assegnazione espone verso l'esterno oppure taglia fuori dall'interfaccia di gestione. Si configurano poi gli indirizzi delle tre reti, verificando che non si sovrappongano, e infine le regole, partendo dal contratto fra zone descritto in `design-and-security.md`.

Sul modem la stessa fase comprende la prenotazione DHCP della WAN del firewall, collegata alla porta LAN 4, l'unica a 2,5 GbE, e a VPN pronta il solo inoltro UDP di WireGuard, nell'ordine scritto nel README di `docs/02-ftth-fastweb/06-tbc-i-parametri-di-interfaccia-modem-su-192-168-1-254-rotte/`. Prima vanno rifotografate le schermate dello stato WAN con la fibra attiva.

Resta da riverificare, prima di considerare chiusa la fase, l'avviso sulla generazione dei template osservato durante il boot dell'ambiente live.

## Fase 3: switch, segmentazione e wireless

Dipende dalla fase 2, perché senza le interfacce del firewall configurate non c'è nulla a cui collegare il trunk.

Si acquista e si configura lo switch gestito, definendo le VLAN e quali porte sono di accesso e quale è il trunk verso il firewall. Lo switch è lo XMG1915-10EP (ADR-017). Si portano a valle due access point, al terzo e al secondo piano, alimentati dallo switch (ADR-018); poi si decide la radio del modem, spenta oppure tenuta come rete esterna dichiarata. La fase chiude il buco strutturale del progetto, cioè il wireless fuori dal perimetro, ed è per questo che non è facoltativa.

Il passaggio dei cavi era la parte materialmente più difficile; al 07/10/2026 l'utente li ha già posati, uno per AP. L'analisi resta nel documento sorgente, con la preferenza per un unico cavo continuo in rame solido invece che tratte accoppiate, e con la nota che la presa esistente a parete è cablata come telefonica su cavo dati, quindi non utilizzabile come presa Ethernet finché non viene riterminata su tutte e quattro le coppie.

## Fase 4: servizi interni

Dipende dalla fase 3 per la segmentazione, perché ogni servizio va collocato in una zona e non in una rete piatta.

Nell'ordine di dipendenza: l'hypervisor sull'hardware disponibile, poi il resolver DNS interno con il motore di policy davanti, che è il servizio con il maggior rapporto fra beneficio e sforzo e che richiede la regola di uscita sul firewall per essere reale; poi lo storage di rete, poi la gestione endpoint, ora nella variante con indirizzo statico dato che l'indirizzo dinamico è decaduto.

Lo storage di rete è l'eccezione all'ordine, per una ragione materiale: il suo hardware si assembla senza toccare la rete, quindi dal 03/09/2026 procede in parallelo alle fasi 2 e 3, ricavato da quattro desktop dismessi. Al 19/10/2026 il NAS è assemblato con Kingston V300 per l'avvio e SanDisk più WD Blue per lo specchio dati previsto (ADR-033), ma TrueNAS non è installato: dopo l'errore con due moduli del 16/10, i contatori del test sono risultati fermi. La prova individuale del solo A1 da 8 GB mostra anch'essa un errore, Pass 3 e Time 2:51:08. L'utente ha poi montato l'ex B1 da solo nello stesso A1: la lettura del 20/10 mostra due errori, Failed, Time 3:03:15 e Pass 3. Entrambe le prove individuali fallite impongono un confronto sulle cause comuni, cambiando una variabile alla volta, senza attribuire già la colpa a entrambi i moduli. Nessun modulo qualificato, installazione sospesa; il 20/10 l'utente riferisce poi lo stesso secondo modulo spostato da A1 ad A2 e assenza di video alla riaccensione; dopo preparazione a corrente tolta e reinserimento richiesto nello stesso A2 dichiara la ripartenza. Richiesta la schermata attuale, senza nuovo Memtest o firmware osservati. L'utente chiarisce che vuole finire il NAS e capire il rischio concreto: il passaggio al server proposto dall'agente era un fraintendimento ed è superato. L'utente richiama poi esplicitamente la fase dei test: confronto dello stesso modulo da solo in A2, temporaneamente 8 GB, e se supera prova della coppia finale A2+B2 da 16 GB prima di TrueNAS. Per ciascuna configurazione quattro passaggi completi senza errori come confronto operativo, stop al primo errore o blocco documentato; nessuna ripetizione identica automatica dopo un fallimento. Etichette RAM-01 e RAM-02 applicate su conferma dell'utente. RAM-02/A2 è ora fallita: un errore già visibile a Time 0:23:17, con stesso indirizzo e bit 42 del primo errore RAM-02/A1. Il 21/10 fallisce anche RAM-01/A2: Time 0:55:10, Pass 1, Errors 1, stesso indirizzo e bit 53 del suo precedente A1. RAM-01 e RAM-02 hanno entrambe fallito A1 e A2; nessun modulo qualificato né notte intera di test attivo documentata. Il 21/10 nuove foto confermano RAM-03/A2 e RAM-04/B2, due TEAMGROUP da 8 GB recuperati da PC-DESKTOP-B, etichette applicate e coppia montata; A1/B1 vuoti e RAM-01/RAM-02 fuori. Stato NAS del 26/10/2026: RAM-03 da sola in A2, 8192 MB a 2133 MHz, AHCI e tre SSD sulle porte 1/2/6 verificati. SystemRescue 8.07 e GSmartControl avviati. Mappa della sessione: /dev/sda SanDisk, /dev/sdb Kingston V300, /dev/sdc WD Blue; /dev/sdd USB. Tutti e tre gli SSD hanno controllo SMART generale PASSED e un autotest esteso documentato: Extended offline, Completed without error, 100%, una voce ciascuno. Test estesi dei tre SSD conclusi positivamente, senza ripetizioni richieste. Restano le schede General dei tre SSD e Attributes di Kingston/WD per firmware e usura; Attributes del SanDisk già acquisita. Dati SanDisk da chiarire prima del pool: domanda inviata il 26/10 e risposta attesa. Accettazione ADR-016 e riallocazione NAS/server ADR-032 ancora aperte. TrueNAS non installato, nessun pool creato. PC-DESKTOP-B resta scorta assemblata e spenta senza RAM/SSD, nessun altro prelievo. Diagnosi e quarta condizione di ADR-016 restano aperte; nessuna garanzia di affidabilità, migrazione di copie uniche o cancellazione implicita. Il versionamento NAS/backup è concluso. I due NVMe sono destinati al server Proxmox `linux-desktop-A`, con 24 GB DDR4 previsti; l'adattatore non si compra. PC-03 si conserva come nodo di laboratorio da portare a 32 GB DDR3, con Samsung 850 EVO previsto per il sistema e disco da 500 GB di PC-02 per le prove. Al 17/10 l'utente dichiara PC-03 senza SSD: il Samsung va localizzato, non è confermato montato. L'Atlantis è identificato dalla targa come P016-MPW-6000-W da 600 W massimi dichiarati. PC-02 è dismesso e la GeForce 210 recuperata come scorta video; il recupero del lettore ottico resta non documentato. L'ordine fisico e lo stato dei gesti sono nel documento canonico `docs/03-spunti-di-sviluppo/23-studio-home-lab/12-allocazione-dell-hardware.md`. Ciò che dipende dalla segmentazione è soltanto la sua collocazione in una zona, decisa il 07/10/2026 nella VLAN 30, che si realizza in questa fase.

## Fase 5: monitoraggio

Dall'8/10/2026 il percorso è deciso (ADR-028): Wazuh su una macchina virtuale del server Proxmox, Suricata integrato in OPNsense prima in sola rilevazione, il plugin `os-wazuh-agent` del firewall e il syslog degli apparati, nell'ordine di messa in opera di `docs/03-spunti-di-sviluppo/23-studio-home-lab/11-monitoraggio-wazuh-suricata.md`. Il server Proxmox che lo ospita, proposto su `linux-desktop-A`, appartiene alla fase 4 insieme ad AdGuard Home.

Dipende dalla fase 4 perché un SIEM senza sorgenti da correlare non serve a niente. Si parte dal solo componente centrale, che copre da solo SIEM, rilevamento sull'host e integrità dei file, con gli agenti sugli endpoint e i log del firewall via syslog. L'indicizzazione con lo stack completo, la sonda sul traffico e i motori di correlazione si aggiungono solo se e quando il volume lo giustifica.

## Fase 6: verifica di sicurezza

Dipende da tutto il resto, perché si verifica ciò che esiste. Scansione delle vulnerabilità dall'interno su una macchina virtuale dedicata, con gli obiettivi definiti per rete. Prima di questa fase va aggiunta al piano di segmentazione una zona isolata per l'analisi dei campioni, oggi non prevista: eseguire codice sospetto su una rete che raggiunge la LAN vanifica l'intera architettura.

## Fase 7: la sezione oggi vuota

La macrosezione della documentazione destinata alla rete effettivamente realizzata si riempie man mano che le fasi da 2 a 6 si chiudono. Va scritta a valle di ogni fase e non alla fine di tutto, perché scritta alla fine sarebbe ricostruzione a memoria e non documentazione.

## Fuori roadmap

Idea dell'utente dell'8/10/2026: un modello linguistico locale. Si collega allo studio METATRON già presente fra le idee di pentesting. Dal 13/10/2026 non chiede più una macchina dedicata con GPU: per decisione dell'utente (ADR-034) va sul nodo di laboratorio a 32 GB, nella VLAN 60, con colibri sul solo processore; studio in `docs/03-spunti-di-sviluppo/23-studio-home-lab/13-modello-linguistico-locale-su-cpu.md`. Non entra nella sequenza delle fasi e non la rallenta: è una misura di un pomeriggio, a nodo assemblato, con una soglia fissata in anticipo. Sopra la soglia diventa uno strumento della fase 6; sotto, l'idea della macchina con GPU torna qui com'era. In ogni caso un giorno si farà uno studio di espansione con una GPU, deciso dall'utente il 13/10/2026 senza data.

Sono idee presenti nel documento sorgente che non hanno una collocazione nella sequenza sopra e che si affrontano solo se emerge un bisogno concreto: le telecamere esterne, con il problema irrisolto dell'alimentazione fuori dal portone; il rack; la telefonia su apparato proprio, che dipende dalla disponibilità delle credenziali della fonia; e la posta self-hosted, che è il servizio con il rapporto peggiore fra manutenzione richiesta e beneficio in un contesto domestico.

Raccomandazioni approvate il 23/10/2026, ADR-037: la [matrice dei bisogni](../../docs/03-spunti-di-sviluppo/23-studio-home-lab/16-bisogni-controlli-e-flussi.md) conferma WireGuard, DNS locale e priorità alla segmentazione. Cloudflare resta un eventuale esperimento applicativo non critico; nessuna installazione o nuovo ingresso amministrativo. ADR-038 adotta il racconto tecnico-didattico e il dettaglio delle scelte mentre ciascuna fase viene realizzata. La bozza di condivisione NAS è riallineata al solo SMB; collaudo delle regole e dei casi negati nella fase di rete.
