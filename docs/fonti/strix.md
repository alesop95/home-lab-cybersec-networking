---
tags: [fonti, sicurezza, pentest]
---

# Strix nel laboratorio

Fonte U05: [repository ufficiale](https://github.com/usestrix/strix), README letto il 22/09/2026. Il progetto presenta agenti che eseguono test applicativi e validano vulnerabilita' con prove attive. Per la modalita' locale documenta Docker e accesso a un modello; supporta anche un endpoint per modelli locali. La licenza mostrata dal repository e' Apache-2.0. Queste sono dichiarazioni e istruzioni del progetto, non una misura della sua efficacia sulle nostre applicazioni.

La distinzione economica e' decisiva: codice liberamente disponibile non significa inferenza senza costo. API esterne possono essere a consumo; un modello locale richiede hardware, energia e verifica della qualita'. Non si promette un pentest completo gratuito ne' si tratta un risultato senza finding come certificazione di sicurezza.

## Applicazione proposta

Strix resta un esperimento successivo al collaudo della rete. Si prepara una VM nella VLAN LAB, con copie sacrificabili delle applicazioni, snapshot, bersagli espliciti e budget di tempo/risorse. Il runner non riceve credenziali del NAS, del firewall o dell'amministrazione domestica. I bersagli reali della casa non si aggiungono per discovery automatica. Il traffico dal LAB alle altre VLAN e' negato salvo eccezioni documentate. In questa sessione non e' stato installato ne' eseguito.

La progressione consigliata e' controllare prima immagini e configurazioni con [Trivy](https://trivy.dev/docs/latest/guide/), poi una copia dell'applicazione con [ZAP Baseline](https://www.zaproxy.org/docs/docker/baseline-scan/), infine confrontare Strix sugli stessi casi. ZAP Baseline genera traffico di crawling e applica controlli passivi: non equivale all'assenza di richieste, ma e' distinto dalla scansione attiva.

Si conserva per ogni prova versione, target, precondizioni, tempi, costo effettivo, finding riprodotti, falsi positivi, correzione e riesecuzione. Il vantaggio da misurare e' quanti problemi reali aggiunge rispetto ai controlli di base, non quanti report produce. Il [piano di lavoro](../03-spunti-di-sviluppo/23-studio-home-lab/04-piano-di-lavoro.md) ne fissa le dipendenze; il [registro](../../SOURCES.md) conserva la fonte originale.
