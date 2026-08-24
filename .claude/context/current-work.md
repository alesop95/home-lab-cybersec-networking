---
generated-from-commit: e89779723cb1ed715b781763011255a81a82700e
generated-from-branch: main
generated-date: 2026-08-24
covers-paths:
  - docs/**
  - tools/**
  - scripts/**
last-verified-commit: e89779723cb1ed715b781763011255a81a82700e
---

# Lavoro corrente

> Scheda tecnica della feature attiva. Va riletta a inizio sessione e riscritta quando la feature cambia, non accresciuta all'infinito: il registro storico e' `.claude/memory/progress.md`, questa scheda descrive solo cio' che e' aperto adesso.

## Feature attiva

Riorganizzazione completa del materiale scritto a mano in documentazione versionata e anonimizzata, e messa in sicurezza del repository in vista del primo push su un remoto pubblico.

## Perche' adesso

Il materiale esisteva come un documento Word di ventuno megabyte, una cartella di fotografie, due file di appunti, un output diagnostico e due collegamenti, tutti alla radice del progetto e tutti esclusi dal versionamento per tipo di file. Il repository conteneva quindi un `README.md` che descriveva il materiale senza contenerlo, e chi lo avesse clonato non avrebbe ottenuto nulla di utile.

Va corretta una premessa che la documentazione precedente dava per buona: il remoto non era da collegare, esisteva gia' ed era gia' pushato. L'anonimizzazione si fa quindi in anticipo su cio' che si sta per pubblicare adesso, che e' la quasi totalita' del contenuto tecnico, mentre per i due valori gia' finiti nella storia in un commit precedente vale la procedura descritta in `design-and-security.md`, cioe' segnalazione e bonifica pianificata a parte.

## Che cosa e' stato fatto

L'allineamento del sistema di progetto al template di riferimento, che era indietro di alcuni commit e a cui mancavano il pacchetto di normalizzazione Markdown e il linter dei comandi.

L'impianto di anonimizzazione, composto dalla regola `anonymization.md`, dalla mappa privata dei segnaposto, dal file privato dei pattern, dal sidecar di redazione applicato in fase di conversione e dal guard-rail eseguibile. Il censimento dei dati reali ha prodotto ventidue voci fra ubicazione, indirizzamento pubblico, identificativi di apparato, identificativi macchina, numeri di serie, nomi di persona e riferimenti contrattuali.

La conversione del documento sorgente in un albero di 120 file Markdown, con tutti i 338 titoli preservati e cinquantaquattro sostituzioni di anonimizzazione applicate, di cui cinque su titoli e quindi anche su slug e nomi di cartella. Il convertitore e' stato modificato per applicare la redazione ai titoli, che nella versione di origine non la riceveva: senza quella modifica due nomi propri sarebbero finiti nei percorsi dei file.

Il layer curato sopra l'albero generato, cioe' l'hub di navigazione, il verbale fotografico dell'installazione, la trascrizione degli appunti sulle alternative privacy, l'inventario delle fonti, il registro delle pendenze, i due diagrammi, le schede tecniche e la memoria di progetto.

## Che cosa resta da fare in questa feature

Eseguire il guard-rail di anonimizzazione con i file aggiunti all'indice, perche' finche' non sono tracciati lo script non li esamina. Verificare la convenzione di formattazione su tutti i Markdown nuovi. Verificare i blocchi di comando con il linter. Poi il primo commit e la creazione del remoto, che sono operazioni manuali dell'utente.

## Definizione di fatto

La feature e' chiusa quando un clone del repository, senza accesso al materiale locale, permette a un lettore tecnico di capire la topologia della rete, il vincolo che la determina, le scelte di componente con le alternative scartate e il loro motivo, lo stato reale di avanzamento, e cio' che resta da fare, senza incontrare un solo dato che identifichi l'abitazione, la linea o le persone.

## Confine da non superare

Questa feature riguarda la documentazione, non la rete. Non si configura nulla sul firewall, non si acquista nulla, non si modifica lo stato del lab. Le sezioni marcate come da chiarire restano tali: il compito era censirle, non chiuderle. Chiuderle e' il lavoro successivo, ed e' descritto nella roadmap.
