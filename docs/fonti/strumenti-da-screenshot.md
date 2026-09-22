---
tags: [fonti, strumenti, diagnostica]
---

# I tre screenshot: contenuto e applicazione

Fonti U01-U03 e S04-S05 nel [registro](../../SOURCES.md), immagini lette il 22/09/2026. I file originali restano nella cartella privata Screenpresso. Questa trascrizione conserva cio' che e' identificabile, senza attribuire alle immagini informazioni assenti.

`screenshot_149.png` mostra il collegamento `https://www.cloudflare.com/vi-vn/application-services/products/waf/` dentro una raccolta di strumenti. Non e' possibile identificare con certezza quella raccolta. Cloudflare WAF riguarda le richieste web che attraversano il suo servizio: non sostituisce OPNsense, la segmentazione o la protezione dei client. La [documentazione del WAF](https://developers.cloudflare.com/waf/) distingue funzionalita' e disponibilita' per piano. Nel lab e' un'opzione per un eventuale sito pubblico, con dipendenza da un fornitore esterno, non un componente gratuito self-hosted della rete interna.

`screenshot_150.png` mostra `cheat.sh`, una pagina di esempi da terminale e il repository `chubin/cheat.sh`. Il [README ufficiale](https://github.com/chubin/cheat.sh) descrive consultazione web/terminale e client. E' utile alla cassetta degli attrezzi dell'amministratore; non richiede un servizio permanente nel lab. Gli esempi restituiti vanno letti prima dell'esecuzione. L'immagine non prova l'origine del filmato che la contiene.

`screenshot_151.png` mostra CanYouSeeMe e il modulo per una porta, con elenco di porte comuni. La [pagina del servizio](https://canyouseeme.org/) serve a verificare raggiungibilita' dall'esterno e port forwarding. Nel progetto la prova va interpretata rispetto ai due NAT e a un servizio effettivamente in ascolto. Un esito negativo non identifica da solo il punto del blocco. Non e' un collaudo delle VLAN, non dimostra assenza di vulnerabilita' e non e' una prova dell'handshake UDP WireGuard. Nessuna verifica su indirizzi reali e' stata eseguita in questa sessione.

La [topologia proposta](../03-spunti-di-sviluppo/23-studio-home-lab/01-architettura.md) spiega dove collocare tali prove; lo [studio servizi](../03-spunti-di-sviluppo/23-studio-home-lab/02-servizi-gratuiti.md) ne distingue il ruolo dai servizi da ospitare.
