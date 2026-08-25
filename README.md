# Home lab di rete e cybersecurity

Progettazione documentata di una rete domestica segmentata: firewall dedicato, VLAN, monitoraggio di sicurezza e servizi self-hosted, costruiti sopra una linea in fibra il cui operatore non consente di sostituire il proprio modem. Il repository non contiene il software del lab, contiene la sua documentazione e gli strumenti che la producono e la verificano.

Tutto cio' che vi si legge e' anonimizzato: indirizzi pubblici, ubicazione, identificativi di apparato, numeri di serie, nomi macchina e nomi di persona sono segnaposto. La convenzione e il controllo automatico che la fa rispettare sono descritti in `.claude/rules/anonymization.md`.

## Stato reale

Quasi tutto e' progettazione, non stato di fatto, e vale la pena dirlo prima di ogni altra cosa perche' e' l'errore piu' facile da fare leggendo la documentazione tecnica.

| Componente | Stato |
|---|---|
| Indirizzo pubblico statico dall'operatore | ottenuto |
| Sistema operativo del firewall | installato il 16/01/2026, rete non configurata |
| Assegnazione delle interfacce a WAN, LAN e DMZ | da fare |
| Switch gestito | scelto, non acquistato |
| Access point a valle del firewall | da acquistare |
| Virtualizzazione, DNS interno, monitoraggio, storage | pianificati |

## Il vincolo che determina tutta l'architettura

Il terminale ottico dell'operatore accetta traffico solo dall'indirizzo hardware del modem fornito in comodato, e quel modem non espone alcuna modalita' bridge o passthrough. Una prova sul campo e la conferma esplicita dell'assistenza convergono sullo stesso esito: il firewall non puo' essere l'apparato di frontiera.

Ne discende la topologia adottata, con il firewall a valle del modem invece che al suo posto.

```
fibra -> PTO -> ONT -> MODEM operatore -> FIREWALL -> SWITCH -> access point
                       (IP pubblico,      (unico punto  (L2,      (tutto il
                        primo NAT,         di decisione  trunk     wireless
                        Wi-Fi fuori        L3, tre       802.1Q)   passa dal
                        dal perimetro)     zone)                   firewall)
```

Le due conseguenze accettate sono il doppio NAT, strutturale e non eliminabile, e la rete wireless del modem che resta fuori dal perimetro del firewall finche' non viene sostituita da access point a valle. La seconda non e' un dettaglio: e' la ragione per cui gli access point non sono un accessorio del progetto ma il suo completamento.

## Da dove si comincia a leggere

`docs/DEVELOPMENT.md` e' l'hub: spiega come e' organizzato l'albero e propone i percorsi di lettura per argomento. `docs/pendenze-aperte.md` dice che cosa e' dichiarato incompleto, con cinquanta voci rilevate automaticamente sulle intestazioni. `docs/verbale-installazione-opnsense.md` e' l'unico documento che descrive qualcosa di realmente accaduto, ricavato dalle trentuno fotografie della sessione di installazione.

Le decisioni architetturali, con le alternative scartate e il motivo, stanno in `.claude/memory/decisions.md`. La topologia disegnata sta in `.claude/context/diagrams/topologia-di-rete.md`.

## Che cosa contiene la documentazione

L'albero `docs/` e' la conversione di un documento sorgente da 338 sezioni, distribuita in 120 file. Copre la linea in fibra e l'apparato dell'operatore fin nel dettaglio dell'interfaccia di gestione, il firewall OPNsense dal confronto con le alternative fino all'installazione passo per passo e alla stima del consumo elettrico, lo switch con le due alternative scartate, lo storage di rete, la virtualizzazione, la gestione endpoint, il DNS interno come punto di controllo, le VPN, il monitoraggio con SIEM e sonda di rete, l'analisi dei campioni sospetti, i fondamenti di livello 2 e 3, il cablaggio fisico e il censimento dei dispositivi domestici.

## Come si mantiene

L'albero e' nato da una conversione deterministica di un documento Word, verificata paragrafo per paragrafo: 1591 su 1591 ritrovati, zero mancanti. Da quel momento il Word e' un archivio e la documentazione si scrive direttamente qui, sessione dopo sessione. Il convertitore resta nel repository ma si rifiuta di sovrascrivere l'albero, protetto da un timbro.

Prima di ogni commit girano quattro controlli: coerenza dell'albero, convenzione di formattazione, comandi di shell copiabili, e il guard-rail che verifica che non sia rimasto nessun dato reale.

```bash
python tools/check-docs-tree.py && python tools/md-unwrap.py --check . && python tools/lint-md-commands.py . && python scripts/Test-Anonymization.py --includi-nuovi
```

L'ultimo dei quattro ha bisogno di materiale che resta privato, quindi chi clona il repository puo' leggere e modificare la documentazione ma non puo' verificarne l'anonimizzazione. E' una conseguenza voluta. La procedura completa e' in `.claude/context/deployment.md`.

## Licenza e ambito

Documentazione di un progetto personale, pubblicata come materiale di studio. Le procedure descritte riguardano una rete privata di proprieta' di chi scrive; nulla di quanto documentato e' pensato per essere applicato a infrastrutture di terzi.
