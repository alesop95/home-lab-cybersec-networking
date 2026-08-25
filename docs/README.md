# Progetto rete domestica

> Home della documentazione. Dal 25/08/2026 questo albero e' scritto e manutenuto a mano: non si rigenera piu' dal documento Word, che resta in `../_notes/sorgenti/` come archivio della prima stesura. Si modifica direttamente qui, si verifica con i controlli descritti in `../.claude/context/deployment.md`, si committa. Il razionale della scelta e' in ADR-010, `../.claude/memory/decisions.md`.

Per orientarsi conviene partire da `DEVELOPMENT.md`, che spiega come e' organizzato l'albero e propone i percorsi di lettura per argomento. Per sapere che cosa manca, `pendenze-aperte.md`.

## Documenti trasversali

- [Guida alla documentazione del lab](DEVELOPMENT.md)
- [Pendenze aperte](pendenze-aperte.md)
- [Verbale dell'installazione di OPNsense](verbale-installazione-opnsense.md)
- [Fonti e materiali del progetto](fonti-e-materiali.md)
- [Alternative rispettose della privacy](alternative-privacy-oriented.md)
- [Report della conversione iniziale](_CONVERSION-REPORT.md)

## Aree

- [Introduzione](01-introduzione/README.md)
- [FTTH Fastweb](02-ftth-fastweb/README.md)
- [[TBC] Spunti di sviluppo e implementazione](03-spunti-di-sviluppo/README.md)
- [Concetti generali](04-concetti-generali/README.md)
- [Analisi tecniche specifiche del caso](05-analisi-del-caso/README.md)
- [PROGETTO rete domestica effettivamente implementato](06-progetto-rete-domestica-effettivamente-implementato/README.md)

## Come si aggiunge qualcosa

Un nuovo elemento di studio e' un file dentro l'area pertinente, quasi sempre sotto `03-spunti-di-sviluppo/`, aggiunto all'indice della sua cartella. Un nuovo dispositivo dell'inventario e' un sottotitolo dentro `05-analisi-del-caso/01-tbc-studio-dispositivi-domestici.md`, senza creare file. Un intervento eseguito davvero e' un documento trasversale nuovo, sul modello del verbale di installazione, collegato qui sopra.

I prefissi numerici delle cartelle e dei file vengono dalla generazione iniziale e ora sono soltanto nomi stabili: non vanno rinumerati per inserire qualcosa in mezzo, si usa il numero successivo libero. Dopo ogni modifica, `python tools/check-docs-tree.py` verifica che non restino file scollegati ne' collegamenti rotti.
