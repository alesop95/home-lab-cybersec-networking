---
generated-from-commit: 4245e21
generated-from-branch: main
generated-date: 2026-10-07
covers-paths:
  - docs/**
  - .claude/**
last-verified-commit: ee63b19
---

# Lavoro corrente

> Scheda tecnica del lavoro aperto. Va riletta a inizio sessione e riscritta quando il lavoro cambia, non accresciuta all'infinito: il registro storico è `.claude/memory/progress.md`, questa scheda descrive solo ciò che è aperto adesso. Riscritta il 07/10/2026, aggiornata l'8/10/2026.

## Due fili, uno attivo e uno in pausa

Dal 07/10/2026 il filo attivo è la progettazione della rete domestica e della sua topologia. Il filo del NAS è in pausa, in un punto preciso e per una ragione sola: manca l'adattatore da PCIe a M.2 che ospita il secondo NVMe, e l'utente non può ordinarlo subito. La pausa non lascia nulla a metà sul banco: i prelievi sono chiusi e il montaggio non è cominciato.

Aggiornamento del 12/10/2026. La fibra, giù dal 9/10 per un guasto in cabina, è tornata con una riparazione fatta fuori casa e senza toccare nulla all'interno; la parte del guasto è chiusa e il suo racconto sta in `docs/02-ftth-fastweb/08-guasto-in-cabina-ottobre-2026.md`. Su richiesta dell'utente il filo attivo torna al banco, cioè all'assemblaggio del NAS e alla sequenza in dodici passi su PC-02 e PC-03; la progettazione della rete resta scritta e decisa dove è, e riprende quando il banco è chiuso. Il ritorno della fibra non sposta lavoro sull'agente: sblocca un'azione dell'utente, il giro di schermate dello stato WAN del Seven con la GPON attiva e il confronto dell'indirizzo pubblico statico fra fibra e collegamento di riserva. Il 14/10/2026 la pratica con l'operatore è chiusa e una prova di velocità a VPN spenta ha confermato l'indirizzo statico sulla fibra, 903,57 Mbit/s in scarico in Wi-Fi: restano il lato del collegamento di riserva e il giro di schermate.

## Filo attivo: progettazione della rete e della topologia

La baseline è ONT, poi il modem dell'operatore, poi la WAN di OPNsense, poi la LAN di OPNsense in trunk verso lo switch Zyxel, poi gli access point. La Wi-Fi del modem resta a monte e fuori dal perimetro del firewall finché gli access point non sono installati, e non va descritta come protetta. Il collegamento diretto di OPNsense all'ONT non è la baseline, perché sulla linea concreta non è stato validato. Il ragionamento è in `docs/03-spunti-di-sviluppo/23-studio-home-lab/`, a partire da `01-architettura.md`, con la guida operativa in `05-guida-configurazione-opnsense-in-casa.md` e il riepilogo degli acquisti in `ACQUISTI-E-CONFIGURAZIONE-DA-FINIRE.md`.

Le decisioni di topologia sono prese: XMG1915-10EP e due AP (ADR-017); AP cablati ai piani 3 e 2 con roaming, PS5 sul Seven, niente FRITZ!Box (ADR-018); NAS nella VLAN 30 a 1 GbE, amministrato dalla sola VLAN 99. La topologia confermata dall'utente è `docs/03-spunti-di-sviluppo/23-studio-home-lab/topologia-proposta.svg`. Gli AP sono due NWA130BE (ADR-024) e lo switch è confermato ai prezzi dell'8/10/2026 (ADR-023). L'amministrazione è decisa con ADR-025 e descritta in `docs/03-spunti-di-sviluppo/23-studio-home-lab/09-accesso-amministrativo.md`; il NAS resta su TrueNAS SCALE (ADR-026). Il contratto fra zone è tradotto in regole per interfaccia l'8/10/2026, in `docs/03-spunti-di-sviluppo/23-studio-home-lab/08-regole-fra-le-zone.md`, da collaudare alla configurazione, a partire dalla tabella di `01-architettura.md`. Sul Seven vanno rifatte le schermate dello stato WAN con la fibra attiva, perché quelle del censimento sono state prese sul collegamento di riserva; dal 12/10/2026 la fibra è su e la cattura è possibile.

Il primo passo che cambia lo stato della rete e non solo la sua descrizione resta la fase 2 della roadmap, cioè l'identificazione fisica delle tre schede di rete del firewall dalla console e la loro assegnazione ai ruoli. Si fa alla macchina, non al repository, e un abbinamento sbagliato può chiudere fuori dall'interfaccia di gestione: la mappatura fisica con la verifica a LED è un prerequisito.

## Filo in pausa: assemblaggio del NAS

La fonte di verità sull'avanzamento è la guida privata `_notes/nas-consolidation/GUIDA-PASSO-A-PASSO.md`, l'unica con i timbri; le fotografie di ogni passo sono in `_notes/nas-consolidation/foto/` con un indice per data e passo.

Al 07/10/2026 sono chiusi il giorno zero e tutti i prelievi, dal Passo 1.1 al 1.7. Sul tavolo ci sono i due moduli di memoria e l'SSD SATA con cavo e slitta della prima macchina, l'NVMe P2 della seconda e l'NVMe P3 della terza, tutti etichettati e verificati contro il censimento. Le tre macchine donatrici sono richiuse ed etichettate con ciò che manca, e restano scorte intere. L'alimentatore resta quello già montato nella base (ADR-016), con tre condizioni di accettazione ancora da verificare durante il montaggio. Il NAS parte senza dischi meccanici, con i due NVMe in specchio come unico pool di dati e applicazioni (ADR-014 e ADR-015).

Il 12/10/2026 il montaggio è avviato con cinque pezzi, senza adattatore né scheda Intel, e la memoria è stata ridistribuita (ADR-032): il NAS resta a 16 GB con i suoi due moduli, i due moduli da 8 GB prelevati vanno al server Proxmox. Sempre il 12/10/2026 i due NVMe passano al server Proxmox (ADR-033): il NAS si monta con il Kingston V300 come avvio e i due SSD SATA in specchio per i dati, senza adattatore. La fonte canonica di dove va ogni pezzo è `docs/03-spunti-di-sviluppo/23-studio-home-lab/12-allocazione-dell-hardware.md`. Quando si riprende: la sezione «PERCORSO RAPIDO dal 12/10/2026» della guida privata, gesto 1, cioè estrarre il V300 da PC-02. Il montaggio può anche cominciare senza adattatore: il P3 resta sul tavolo e il pool nasce con un disco solo, ma senza copia dei dati finché l'adattatore non arriva. Il prodotto indicato è AXAGON PCEM2-N, registrato come fonte S54.

Aggiornamento del 16/10/2026: il NAS è assemblato con i tre dischi e acceso a case aperto; il firmware vede 16 GB in doppio canale e i tre dischi, il ramo a +12 V sta a 12,192 V. Il test della memoria ha trovato un errore singolo dopo quasi quattro ore e quattro passaggi puliti, quindi la quarta condizione di ADR-016 non è soddisfatta; il test resta acceso fino a lunedì 19/10/2026, poi si isolano i due moduli uno per volta. TrueNAS non si installa prima. La cronologia completa del banco, con letture e ragioni, è in `docs/03-spunti-di-sviluppo/02-storage-di-rete-nas/09-registro-del-montaggio.md`.

## Definizione di fatto del NAS

Una macchina montata, con sedici gigabyte verificati da una notte di test della memoria (ADR-032; erano trentadue), i dischi passati al test SMART lungo, il sistema installato e raggiungibile sul Kingston V300 con la configurazione esportata, e il pool in specchio sui due SSD SATA SanDisk e WD Blue (ADR-033). Le tre condizioni di ADR-016 sull'alimentatore verificate. A valle si scrive un verbale sotto `docs/`, sul modello di `docs/verbale-installazione-opnsense.md`, collegato dalla home dell'albero.

## Confine da non superare

L'agente non esegue operazioni git e non tocca lo stato della rete: prepara file e propone comandi, e il commit passa da `chiudi`. Sul banco l'agente ragiona sulle compatibilità, verifica contro i manuali e interpreta le fotografie e gli esiti dei test, ma montaggio e test li esegue l'utente.

## Filo nuovo: dalla documentazione dell'autore alla documentazione tecnica di progetto

Richiesta dell'utente del 07/10/2026: rileggere tutta la documentazione scritta originariamente da lui, cioè l'albero `docs/` nato dalla conversione del `.docx`, e trasformarla in documentazione tecnica di progetto. Il primo esempio indicato è l'interfaccia del Seven: tutte le voci di menu raggiungibili dal suo gateway e, per ciascuna, come si combina con il progetto di rete. Il lavoro si fa per area, una alla volta, partendo dal Seven sotto `docs/02-ftth-fastweb/`, e per ogni area si dichiara che cosa è stato letto e che cosa no.

Forma decisa con ADR-020: ogni documento dell'autore si riscrive al suo posto come documento tecnico, e dopo ogni riscrittura il confronto paragrafo per paragrafo deve dimostrare che ogni contenuto è ancora presente o tolto con una ragione scritta. Il primo lavoro, fatto l'8/10/2026, è stato riassorbire il documento separato sul Seven nel censimento delle voci di menu sotto `02-ftth-fastweb/06-tbc-i-parametri-di-interfaccia-modem-su-192-168-1-254-rotte/`, con verifica di copertura, e lo stesso giorno il resto di `02-ftth-fastweb` in tre blocchi; ora restano `05-analisi-del-caso`, `04-concetti-generali` e per ultima `03-spunti-di-sviluppo`. Durante la riscrittura si rileggono le segnalazioni di `lint-prosa` e le forme di accento ambigue di ciascun documento.

Filo collegato, ADR-021: la scheda dispositivo a campi fissi, con raccolta in sola lettura per sistema operativo; i dati grezzi in `_notes/`, nel repository la sola scheda anonimizzata, partendo dal censimento in `docs/05-analisi-del-caso/`. L'8/10/2026 sono pronti il metodo, `docs/05-analisi-del-caso/02-scheda-dispositivo.md`, e gli strumenti `tools/raccolta-dispositivo.ps1`, `.sh` e `tools/scheda-da-raccolta.py`; restano le raccolte sui singoli dispositivi, che l'utente esegue o autorizza PC per PC.

## Stato delle decisioni, da tenere aggiornato a ogni giro

Quadro chiesto dall'utente l'8/10/2026, perché ogni ripresa sappia che cosa è chiuso e che cosa no. Si aggiorna nello stesso giro in cui una voce cambia stato.

Decise: catena ONT, Seven, OPNsense, switch, AP; switch XMG1915-10EP (ADR-017, ADR-023); due NWA130BE cablati ai piani 3 e 2 (ADR-018, ADR-024); PS5 sul Seven, niente FRITZ!Box (ADR-018); NAS su TrueNAS SCALE nella VLAN 30 (ADR-015, ADR-026); amministrazione da tre ingressi verso la VLAN 99 e rete WireGuard 192.168.98.0/24 (ADR-025); laboratorio senza uscita salvo aperture a tempo (ADR-025); riscrittura al posto con verifica di copertura (ADR-020); scheda dispositivo (ADR-021); strumenti del template in `tools/` (ADR-022).

Deciso anche, l'8/10/2026: flusso di monitoraggio Wazuh con Suricata in OPNsense (ADR-028); eliminazione dei contenuti sugli strumenti scartati (ADR-027).

Deciso il 15/10/2026 (ADR-036): Netdata come raccoglitore di metriche, agenti sugli host verso un parent sul server Proxmox, che è Linux, e lettura SNMP di switch e access point, studio in `docs/03-spunti-di-sviluppo/23-studio-home-lab/14-metriche-con-netdata.md`. Proposte che aspettano l'utente: la Z97-P anche come banco di analisi dei campioni; l'eventuale adattatore da due pollici e mezzo per il Kingston V300, se il case di `linux-desktop-A` non lo monta da sé, perché le slitte di PC-02 risultano rotte; caduta il 14/10/2026, perché il V300 va nel NAS ed è avvitato su un adattatore Corsair apparentemente integro. Il confronto, la combinazione finale, la matrice, le porte, lo smontaggio e la sequenza del da farsi al banco sono nelle sezioni del 09/10/2026 del piano unificato. Caduta il 09/10/2026: l'idea di prendere la DDR4 da uno dei due PC, perché le foto mostrano che entrambi hanno solo DDR3.

Idee future, fuori dalla sequenza: un modello linguistico locale, idea dell'utente dell'8/10/2026, che dal 13/10/2026 non chiede più una GPU: colibri sul nodo di laboratorio a 32 GB, VLAN 60, deciso (ADR-034) e da tenere solo se una misura supera la soglia, studio 13 della cartella dello studio; più avanti uno studio di espansione con una GPU, senza data; un eventuale nodo Tor, che se mai si farà va su una macchina dedicata in DMZ e non sul firewall.

Chiuso il 12/10/2026: allocazione completa dell'hardware fissata in `docs/03-spunti-di-sviluppo/23-studio-home-lab/12-allocazione-dell-hardware.md`, fonte canonica; i due NVMe vanno al server, il NAS si fa con gli SSD SATA, l'adattatore non si compra (ADR-033). La memoria DDR4 si ridistribuisce, NAS a 16 GB e server Proxmox a 24 GB, scorta di due moduli da 4 GB (ADR-032); lo scambio sul server si fa al passo 8 della sequenza del banco. I moduli DDR3 di PC-02 sono quattro, due di taglia da leggere.

Chiuso il 09/10/2026: il server Proxmox è `linux-desktop-A` (ADR-030), la Z97-P di PC-03 a 32 GB è il nodo di laboratorio e banco di analisi, PC-02 si svuota e si smaltisce (ADR-031); i due tablet sono di casa, Tab S6 Lite = TAB-01, il più vecchio = TAB-02. `linux-desktop-C` (Ubuntu Studio, PC-06) resta per produzione musicale, in Wi-Fi con adattatore USB, raccolta via SSH fatta. Si resta sul 10EP, moduli SFP in rame se servono (ADR-029). La postazione di lavoro dell'utente non è della rete di casa.

Pendenti per un dato o un'azione: compatibilità dei moduli SFP in rame con lo XMG1915; preventivo del fornitore per switch e AP; disattivazione del Booster dopo il collaudo degli AP; schermate del Seven a fibra attiva, ora possibili; raccolta con `tools/raccolta-dispositivo.sh` su PC-03 per processore e memoria totale, e lettura SMART dei tre dischi di PC-02 e PC-03; su PC-02, svuotato il 15/10/2026 anche dell'alimentatore, la raccolta non è più possibile e la sigla del processore si legge solo togliendo il dissipatore, utile al solo inventario perché la piattaforma va al conferimento; supporto SATA dell'M.2 della H270M Pro4; estensioni di virtualizzazione e memoria massima di `linux-desktop-A`; prezzo dell'SSD per Proxmox; verifiche di Netdata a cose accese (ADR-036); scelte sulla protezione degli endpoint, studio del 15/10/2026 in `docs/03-spunti-di-sviluppo/07-further-protection/03-studio-protezione-endpoint-2026.md`, primo passo irrigidire Defender in audit su un PC Windows; raccolte sui PC per le schede dispositivo; riscrittura di `04-concetti-generali` e `03-spunti-di-sviluppo`; zona isolata per l'analisi dei campioni.
