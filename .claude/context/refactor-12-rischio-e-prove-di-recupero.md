---
covers-paths: ["docs/03-spunti-di-sviluppo/23-studio-home-lab/20-governo-sicurezza-e-privacy-domestiche.md", "docs/03-spunti-di-sviluppo/23-studio-home-lab/21-aggiornamento-e-vulnerabilita-opnsense.md", "AGENTS.md", "tools/sync-codex-skills.py"]
last-verified-commit: 3c876a64c6530edd1482284575a36ca631cce678
---

# Refactor12 - Una dichiarazione di copertura deve avere una prova

Scheda del29/10/2026. Ritorno al [racconto](studio-didattico-master.md). Dettagli negli studi [20](../../docs/03-spunti-di-sviluppo/23-studio-home-lab/20-governo-sicurezza-e-privacy-domestiche.md) e [21](../../docs/03-spunti-di-sviluppo/23-studio-home-lab/21-aggiornamento-e-vulnerabilita-opnsense.md).

## Le etichette che potevano chiudere il lavoro troppo presto

Un export integro non dimostra un restore.26.7.7 in una schermata non dimostra il hotfix successivo del pacchetto PHP. Una skill chiamata ISO27001 non attesta conformità. Nel progetto il controllo dei wrapper Codex era verde anche senza il file di ingresso AGENTS.md: verificava gli adattatori ma non il ponte che rende leggibili le istruzioni canoniche all’avvio.

## Il cambiamento nel codice reale

Il generatore tools/sync-codex-skills.py ora controlla il ponte nei progetti del sistema sulla destinazione standard. Questo è l’estratto effettivo:

```python
progetto_di_sistema = (radice / ".claude" / "PROJECT-SYSTEM.md").is_file()
destinazione_standard = destinazione == radice / ".agents" / "skills"
if progetto_di_sistema and destinazione_standard and not ponte.is_file():
    if ponte.exists() or not modello_ponte.is_file():
        print("Ponte Codex non riparabile: AGENTS.md o modello canonico assente/non valido.")
        return 2
    difformi.append(ponte)
    if not solo_controllo:
        ponte.write_bytes(modello_ponte.read_bytes())
```

La prova discriminante allinea prima tutti i wrapper, elimina soltanto il ponte nella fixture e pretende esito rosso senza scritture. Così distingue il difetto osservato da un generico wrapper mancante. Il modello viene copiato byte per byte, mentre un file personalizzato esistente non viene riscritto dal generatore. La passata del template tratta il ponte con la storia e il report ordinari; la propagazione globale richiede il commit manuale della correzione a monte.

## Dalla prova al governo della rete

Lo stesso criterio guida lo studio20: associare rischio, controllo e riscontro. Per il NAS manca il recupero da una destinazione indipendente; per il firewall manca la lettura della macchina aggiornata; per le VLAN manca il rifiuto reale del flusso vietato. Non si allarga il perimetro GDPR perché il server è in casa e non si deduce un’esenzione perché l’hardware è domestico: si guarda l’attività concreta.

Un nuovo controllo si aggiunge quando misura una conseguenza, con un caso che fallirebbe se il difetto tornasse. Le evidenze del codice sono nel work-log e nel registro delle lezioni; quelle dei servizi si raccolgono alla loro attivazione. In questo giro nessun sistema remoto è stato aggiornato o certificato.
