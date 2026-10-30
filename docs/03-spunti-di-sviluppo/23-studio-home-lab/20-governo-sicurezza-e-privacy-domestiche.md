# Governo della sicurezza e privacy della rete domestica

Filone richiesto il29/10/2026, ADR-048. Raccorda [matrice dei bisogni](16-bisogni-controlli-e-flussi.md), [backup](../05-strategia-di-backup/02-piano-di-backup-e-ripristino-del-lab.md), [assistente](17-assistente-personale-hermes-nix-e-memoria.md) e [aggiornamenti firewall](21-aggiornamento-e-vulnerabilita-opnsense.md). Le skill canoniche iso27001 e gdpr-compliance del pacchetto grc-skills v2.1.0 sono state istanziate dal template; i wrapper Codex rimandano a quelle stesse procedure. Non è un audit o una certificazione conseguita.

## Usare il metodo senza inventare obblighi

ISO/IEC27001:2022 organizza un sistema di gestione della sicurezza basato sul rischio. La pagina ufficiale ISO, S279, è stata letta; il testo integrale a pagamento non è stato acquisito e non si certifica la copertura delle clausole o dell’Annex A. Qui si adotta il metodo proporzionato: quali beni proteggiamo, da quale evento, con quale controllo e quale prova. La revisione del rischio va collegata ai cambiamenti della rete e a incidenti reali, senza moduli compilati per simulare un’organizzazione aziendale.

Per il GDPR[^1] si valuta prima il perimetro concreto. Il Garante richiama l’esclusione dell’articolo2(2)(c) per attività esclusivamente personali o domestiche e il considerando18; il provvedimento S280 chiarisce anche i limiti quando si esce da quella sfera. Un server collocato in casa non rende domestico ogni trattamento. Lavoro, servizi a terzi, pubblicazione di dati o telecamere oltre la pertinenza privata richiedono una valutazione propria. Non si impongono automaticamente DPO, registro formale o DPIA al semplice lab familiare; se cambia l’uso, si riapre l’analisi di applicabilità prima di estendere il servizio. Le due pagine EUR-Lex tentate sono rimaste dietro verifica automatica: non dichiarate lette; qui il riscontro giuridico è la fonte primaria del Garante.

Le skill sono materiale operativo di supporto. Affermazioni normative, scadenze, notifica e casi particolari vanno verificati su fonti primarie aggiornate prima di applicarli; un testo di skill non è prova di conformità. Nessuna attività sulla rete aziendale temporanea è autorizzata da questo filone. Nessuno scanner eseguito contro terzi.

## Registro iniziale dei rischi e delle prove

| Bene o flusso | Evento concreto | Controllo previsto o già osservato | Prova e stato al29/10/2026 |
|---|---|---|---|
| Documenti nel NAS | guasto di un SSD, cancellazione, perdita dell’intera macchina | mirror creato; copie/versioni e backup separati ancora da attuare | mirror ONLINE osservato; recupero di un file da backup e restore macchina non provati |
| Dataset cifrato e configurazione | perdere chiave o segreti dopo cambio hardware | JSON chiave e tre export con seed acquisiti privatamente fuori NAS | integrità/formato verificati; stessa macchina client, destinazione indipendente e sblocco da copia ancora aperti |
| Firewall | software vecchio o gestione esposta | aggiornamento prima dell’attivazione, gestione limitata e copie configurazione | installazione storica25.7; versione attuale e patch non osservate, studio21 |
| Sensori e MCU | firmware compromesso che raggiunge NAS o gestione | SSID IoT/VLAN40, soli endpoint ammessi | progetto, nessuna prova di isolamento radio o rete eseguita |
| Assistente e brain | prompt malevolo, accesso eccessivo ai file, invio di contenuto personale al provider | identità separata, corpus minimo, strumenti limitati, provenienza e registri protetti | studio17/19; agente, permessi e provider ancora da collaudare |
| Accesso remoto | autorizzazione troppo ampia o identità condivisa | Tailscale per bisogno; niente Meshnet dell’account commerciale condiviso | scelta documentata; nessuna rotta o regola già attiva |
| Notifiche | mancata consegna o messaggi con segreti | invio NAS verificato, recapito personale privato e separato dal mittente servizi | mail test ricevute; classificazione Log NAS e verifica periodica future |

La vulnerabilità, il guasto e il dato mancante restano eventi distinti. Il mirror migliora disponibilità per il guasto di un membro; non elimina la necessità di backup. La cifratura protegge la confidenzialità a riposo; non ricostruisce un dato cancellato e non impedisce la lettura da un servizio già autorizzato. Monitoraggio e alert servono alla rilevazione, senza diventare prevenzione universale.

## Dati, conservazione e risposta

Per ogni nuovo servizio il registro dovrà indicare categorie di dati, origine, destinatari, luogo di conservazione, soggetti autorizzati, durata e modalità di recupero/cancellazione. Per Hermes distinguere documento originale, indice, cronologia, memoria derivata e log del provider. Non assegnare una retention uguale a tutto: i log di accesso non sono automaticamente documenti familiari da conservare per anni. Le durate si decidono sul bisogno prima di attivare la raccolta. Le informazioni identificanti e le chiavi restano nel livello privato, mai nel remoto pubblico.

La risposta iniziale a un evento sarà limitare l’accesso del nodo coinvolto, conservare gli elementi utili privatamente, distinguere guasto da compromissione e recuperare da una copia verificata. Le eventuali comunicazioni legali dipendono dall’applicabilità e dai fatti; nessuna notifica automatica viene inventata per il lab. Per i servizi esposti o professionali serve una valutazione distinta prima della pubblicazione.

## Criterio per avanzare

Si chiude una tappa con una prova piccola: recuperare un file con ACL attese, importare la configurazione su ambiente sostitutivo, negare un collegamento IoT verso gestione, verificare un accesso remoto autorizzato e uno rifiutato. Si registra cosa è stato osservato e ciò che resta aperto. La revisione delle fonti avverrà prima di modifiche o nuove esposizioni, oltre alle revisioni pianificate del lab. Le attività future restano nelle pendenze; installare una skill oggi non le segna eseguite.

[^1]: GDPR: regolamento generale sulla protezione dei dati. DPO: responsabile della protezione dei dati. DPIA: valutazione d’impatto sulla protezione dei dati.
