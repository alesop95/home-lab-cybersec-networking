# Studio soluzioni pratiche per passaggi cavi fisici

O faccio passare su presa di cavo telefonico vecchio legato con nastro isolante (eventualmente passando per scatola di derivazione) E con sonda [https://www.amazon.it/Lotvic-Passacavi-Elettricista-Poliestere-LInstallazione/dp/B0B8SPBVZB](https://www.amazon.it/Lotvic-Passacavi-Elettricista-Poliestere-LInstallazione/dp/B0B8SPBVZB) oppure [https://www.amazon.it/Passacavi-Professionale-Elettricista-LInstallazione-terminali/dp/B0DKP9N6J2/](https://www.amazon.it/Passacavi-Professionale-Elettricista-LInstallazione-terminali/dp/B0DKP9N6J2/) e si valuta di fare la stessa cosa sulla maschera della presa antenna.

Per un cavo Cat 6, l’idea è un passaggio esterno alle pareti fino al piano superiore, estetica ordinata e possibilità di rimuovere tutto senza danni: canaline adesive rimovibili con copertura con coperchio chiudibile: protegge il cavo e dà un aspetto pulito.

Nel caso si dovesse procedere internamente c’è questo prodotto basic universale [https://www.amazon.it/gp/product/B0F1LLNDMH/ref=ewc_pr_img_1?smid=AXJYC9MH9K5LP&psc=1](https://www.amazon.it/gp/product/B0F1LLNDMH/ref=ewc_pr_img_1?smid=AXJYC9MH9K5LP&psc=1).

## Perché evitare gli accoppiatori

Gli accoppiatori RJ45 (coupler) sono piccoli dispositivi femmina-femmina che permettono di unire due cavi RJ45 maschio. Soprattutto se non si stanno terminando i cavi con connettori RJ45 fai-da-te e li si vuole collegare in mezzo al percorso e probabilmente una soluzione lunga basta e non c'è una patch panel / muro → pozzetto → stanza con più segmenti è meglio evitarli se possibile.

Ogni accoppiatore è un punto di giunzione e introduce qualche perdita di segnale e potenziale riflessione, aumenta leggermente la latenza e la perdita di ritorno (RL), che in reti 2,5 Gbps conta più che su 1 Gbps e può essere un punto di debolezza meccanico se tirato/torto. Figuriamoci su un impianto Cat 6A ben fatto dove le velocità arrivano a 10Gbps.

Se proprio uno deve usarli è meglio scegliere accoppiatori schermati (STP) e anch’essi Cat 6A-rated: devono essere metal-shielded e specificare supporto 500 MHz/10 Gbps. Quelli generici economici (senza schermatura) possono degradare la qualità del link e la performance, soprattutto se si fanno PoE o si hanno tratti lunghi.

La migliore pratica di cablaggio è portare un unico cavo Cat 6A con rame solido da punto A a punto B quando possibile. La distanza non supera ~50-70 m per cui non serve installare uno switch intermedio (ad esempio in un ripostiglio o controsoffitto) piuttosto che usare accoppiatori. In ogni caso eventualmente sarebbe sempre meglio scegliere connettori RJ45 e patch cord anch’essi Cat 6A schermati (S/FTP o F/FTP) se il cavo è schermato.

Se la distanza è effettivamente ≤30 m e il cavo va solo entro muri/canaline interne (senza condizioni estreme o interferenze forti), si può prendere un cavo Cat6A senza guaina outdoor (solo interno) e valutare versioni piatte/sottile se l’estetica è importante e la posa è semplice.

## Buona norma di acquisto cavi

Bisogna evitare extra lunghezze troppo eccessive (es. 50 m → 30 m più patch panel), perché spesso il prezzo cresce più che proporzionalmente. Questi cavi puntano tutti a solid copper + RJ45 già montati al prezzo più basso possibile. filtra i risultati per prezzo crescente. Cerca un prodotto che abbia:

- Cat6A certificato / 500 MHz o superiore
- Solid copper / rame solido” nel titolo o nella descrizione
- Schermatura S/FTP o F/FTP (meglio degli UTP base)

Così si evitano i prodotti solo nominalmente Cat6A ma che in realtà non rispettano i requisiti per 10 Gbps [https://www.reddit.com/r/Ubiquiti/comments/1au5zm2/how_bad_did_i_mess_up/](https://www.reddit.com/r/Ubiquiti/comments/1au5zm2/how_bad_did_i_mess_up/).

Un buon esempio di cavo ehernet cat6a è [https://www.amazon.it/HB-DIGITAL-Cat-6a-connettore-resistente-impermeabile/dp/B08P5S42ZL/ref=sr_1_4?__mk_it_IT=%C3%85M%C3%85%C5%BD%C3%95%C3%91&crid=1C6YY14AY9J0P&dib=eyJ2IjoiMSJ9.-WySkLGXEXcFQcW51MvTpHRB6lv3XzoxYePrCHrbLz9m2A7bbIBoUNJX8FWFPJCkaboHYKlc7fgln5SC8LpvO6li2mubaVXmPJkGXxrLhnwZXvX5SFRAKaBPDLelWoqo2RD1iiwOzDYMBFiIh_6r4NAqf_rIlFSL_LkwyjCBoyKuahysaOtFwrCTuoi1GECqyCayCGtCma7MSiW8_ea1xO5lqGKnb0pBDXXSEGB5BC1XItBqvoSxaSUzSauqz5ApL-6Fe1XXM4h98Zsvnjp7V1OPxQMGFfjVILAQ0aUDtJw.8z4Tp8E5IL1v6JxQOQIB4Yy_krWHPBfqHzMmbXofbQI&dib_tag=se&keywords=Cavo+Ethernet+Cat6A+30m+Solid+%28Outdoor%2FInterno%29&qid=1765970076&s=electronics&sprefix=cavo+ethernet+cat6a+30m+solid+outdoor%2Finterno+%2Celectronics%2C232&sr=1-4](https://www.amazon.it/HB-DIGITAL-Cat-6a-connettore-resistente-impermeabile/dp/B08P5S42ZL/ref=sr_1_4?__mk_it_IT=%C3%85M%C3%85%C5%BD%C3%95%C3%91&crid=1C6YY14AY9J0P&dib=eyJ2IjoiMSJ9.-WySkLGXEXcFQcW51MvTpHRB6lv3XzoxYePrCHrbLz9m2A7bbIBoUNJX8FWFPJCkaboHYKlc7fgln5SC8LpvO6li2mubaVXmPJkGXxrLhnwZXvX5SFRAKaBPDLelWoqo2RD1iiwOzDYMBFiIh_6r4NAqf_rIlFSL_LkwyjCBoyKuahysaOtFwrCTuoi1GECqyCayCGtCma7MSiW8_ea1xO5lqGKnb0pBDXXSEGB5BC1XItBqvoSxaSUzSauqz5ApL-6Fe1XXM4h98Zsvnjp7V1OPxQMGFfjVILAQ0aUDtJw.8z4Tp8E5IL1v6JxQOQIB4Yy_krWHPBfqHzMmbXofbQI&dib_tag=se&keywords=Cavo+Ethernet+Cat6A+30m+Solid+%28Outdoor%2FInterno%29&qid=1765970076&s=electronics&sprefix=cavo+ethernet+cat6a+30m+solid+outdoor%2Finterno+%2Celectronics%2C232&sr=1-4).  È cat 6A reale (supporta 10 Gbps fino a 30 m) e ha un conduttore in rame solido (23 AWG), non CCA: questo è quello che serve per percorsi fissi e lunghezze anche impegnative, perché mantiene bassa attenuazione e performance stabile. I connettori sono RJ45 già montati e lo schema di pin è standard T568B (il più usato). Quest’ultimo è classificato anche per uso esterno, il che implica guaina più robusta rispetto a un semplice cavo interno UTP: non è un “lusso”, ma una durabilità maggiore anche dentro canaline interne.

Ad esempio, come prestazioni attese nella pratica si può avere su ~30 m, una connessione FTTH da 2,5 Gbps pienamente supportata senza degradazioni. Se in futuro uno installa un dispositivo 10 Gbps (switch o scheda di rete), il cavo non sarà il collo di bottiglia entro questa distanza. La schermatura S/FTP riduce il rischio di errori o perdite di pacchetti anche in presenza di campi elettromagnetici generati da altri cavi o dispositivi lungo la traiettoria.

## Canaline per passaggio cavi

Per un cavo Cat 6A, passaggio esterno alle pareti fino al piano superiore, estetica ordinata e possibilità di rimuovere tutto senza danni: canaline adesive rimovibili con copertura [https://www.amazon.it/gp/product/B0F1LLNDMH/ref=ewc_pr_img_1?smid=AXJYC9MH9K5LP&psc=1](https://www.amazon.it/gp/product/B0F1LLNDMH/ref=ewc_pr_img_1?smid=AXJYC9MH9K5LP&psc=1). Economiche, pulite, modulabili, compatibili con più cavi se serve. Perfette per reti FTTH fino a 2,5 Gbps e oltre.

Sono fatte di plastica/PVC autoadesiva (es. D-Line, AiQInu, Electronio). La larghezza minima 25-40 mm per un singolo Cat 6A, più larga se prevedi più cavi. Copertura con coperchio chiudibile: protegge il cavo e dà un aspetto pulito.
