---
generated-from-commit: 4245e21
generated-from-branch: main
generated-date: 2026-10-07
covers-paths:
  - docs/**
  - .claude/**
last-verified-commit: 6769dc4
---

# Lavoro corrente

> Scheda tecnica del lavoro aperto. Va riletta a inizio sessione e riscritta quando il lavoro cambia, non accresciuta all'infinito: il registro storico e' `.claude/memory/progress.md`, questa scheda descrive solo cio' che e' aperto adesso. Riscritta il 07/10/2026.

## Due fili, uno attivo e uno in pausa

Dal 07/10/2026 il filo attivo e' la progettazione della rete domestica e della sua topologia. Il filo del NAS e' in pausa, in un punto preciso e per una ragione sola: manca l'adattatore da PCIe a M.2 che ospita il secondo NVMe, e l'utente non puo' ordinarlo subito. La pausa non lascia nulla a meta' sul banco: i prelievi sono chiusi e il montaggio non e' cominciato.

## Filo attivo: progettazione della rete e della topologia

La baseline e' ONT, poi il modem dell'operatore, poi la WAN di OPNsense, poi la LAN di OPNsense in trunk verso lo switch Zyxel, poi gli access point. La Wi-Fi del modem resta a monte e fuori dal perimetro del firewall finche' gli access point non sono installati, e non va descritta come protetta. Il collegamento diretto di OPNsense all'ONT non e' la baseline, perche' sulla linea concreta non e' stato validato. Il ragionamento e' in `docs/03-spunti-di-sviluppo/23-studio-home-lab/`, a partire da `01-architettura.md`, con la guida operativa in `05-guida-configurazione-opnsense-in-casa.md` e il riepilogo degli acquisti in `ACQUISTI-E-CONFIGURAZIONE-DA-FINIRE.md`.

Le decisioni aperte del filo sono di progetto e non di esecuzione. La prima, numero di access point e switch, e' chiusa il 07/10/2026 da ADR-017: XMG1915-10EP e due AP, modello degli AP ancora da scegliere. Il rilievo fisico della casa serve ora alla posizione degli AP e al percorso dei cavi. La topologia confermata dall'utente e' in `docs/03-spunti-di-sviluppo/23-studio-home-lab/topologia-proposta.svg`; collocazione fisica, PS5 sul Seven e rinuncia al FRITZ!Box sono ADR-018. La seconda e' il piano delle VLAN, proposto in `01-architettura.md` con i segmenti 10, 30, 40, 50, 60 e 99, e il contratto fra zone che lo accompagna. La terza e' la collocazione del NAS nella topologia, che ora e' una macchina reale con un indirizzo e un ruolo e non piu' un'ipotesi: va deciso in quale segmento sta e quali zone lo raggiungono. Deciso il 07/10/2026: VLAN 30 servizi e storage, raggiunta dalla VLAN 10 sui soli protocolli di condivisione e amministrata dalla sola VLAN 99, a 1 GbE.

Il primo passo che cambia lo stato della rete e non solo la sua descrizione resta la fase 2 della roadmap, cioe' l'identificazione fisica delle tre schede di rete del firewall dalla console e la loro assegnazione ai ruoli. Si fa alla macchina, non al repository, e un abbinamento sbagliato puo' chiudere fuori dall'interfaccia di gestione: la mappatura fisica con la verifica a LED e' un prerequisito.

## Filo in pausa: assemblaggio del NAS

La fonte di verita' sull'avanzamento e' la guida privata `_notes/nas-consolidation/GUIDA-PASSO-A-PASSO.md`, l'unica con i timbri; le fotografie di ogni passo sono in `_notes/nas-consolidation/foto/` con un indice per data e passo.

Al 07/10/2026 sono chiusi il giorno zero e tutti i prelievi, dal Passo 1.1 al 1.7. Sul tavolo ci sono i due moduli di memoria e l'SSD SATA con cavo e slitta della prima macchina, l'NVMe P2 della seconda e l'NVMe P3 della terza, tutti etichettati e verificati contro il censimento. Le tre macchine donatrici sono richiuse ed etichettate con cio' che manca, e restano scorte intere. L'alimentatore resta quello gia' montato nella base (ADR-016), con tre condizioni di accettazione ancora da verificare durante il montaggio. Il NAS parte senza dischi meccanici, con i due NVMe in specchio come unico pool di dati e applicazioni (ADR-014 e ADR-015).

Quando si riprende: Passo 1.6, inventario sul tavolo e confronto dei codici data della memoria, che comprende la lettura dell'etichetta dei due moduli gia' montati nella base; poi il montaggio dal Passo 2.1. Il montaggio puo' anche cominciare senza adattatore: il P3 resta sul tavolo e il pool nasce con un disco solo, ma senza copia dei dati finche' l'adattatore non arriva. Il prodotto indicato e' AXAGON PCEM2-N, registrato come fonte S54.

## Definizione di fatto del NAS

Una macchina montata, con trentadue gigabyte verificati da una notte di test della memoria, i dischi passati al test SMART lungo, il sistema installato e raggiungibile su un insieme di avvio in mirror sui due SSD SATA, e il pool dei due NVMe in specchio. Le tre condizioni di ADR-016 sull'alimentatore verificate. A valle si scrive un verbale sotto `docs/`, sul modello di `docs/verbale-installazione-opnsense.md`, collegato dalla home dell'albero.

## Confine da non superare

L'agente non esegue operazioni git e non tocca lo stato della rete: prepara file e propone comandi, e il commit passa da `chiudi`. Sul banco l'agente ragiona sulle compatibilita', verifica contro i manuali e interpreta le fotografie e gli esiti dei test, ma montaggio e test li esegue l'utente.

## Filo nuovo: dalla documentazione dell'autore alla documentazione tecnica di progetto

Richiesta dell'utente del 07/10/2026: rileggere tutta la documentazione scritta originariamente da lui, cioe' l'albero `docs/` nato dalla conversione del `.docx`, e trasformarla in documentazione tecnica di progetto. Il primo esempio indicato e' l'interfaccia del Seven: tutte le voci di menu raggiungibili dal suo gateway e, per ciascuna, come si combina con il progetto di rete. Il lavoro si fa per area, una alla volta, partendo dal Seven sotto `docs/02-ftth-fastweb/`, e per ogni area si dichiara che cosa e' stato letto e che cosa no.

Stato al 07/10/2026: fatta la parte sul Seven, con `02-ftth-fastweb/08-il-seven-nel-progetto-di-rete-voce-per-voce.md`. Il resto di `02-ftth-fastweb` e le altre aree restano da fare; la misura in parole e' nel work-log. La forma scelta e' un documento tecnico nuovo per area, con il materiale dell'autore conservato e collegato, salvo diversa indicazione dell'utente.
