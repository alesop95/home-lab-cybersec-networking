# Telefonia su cavo dati

La fonia può viaggiare su un cavo dati Ethernet, ma il punto chiave è come è cablato e terminato il cavo, non il tipo di presa visibile a parete. Innanzitutto, un cavo Cat 5e / Cat 6 contiene quattro coppie twistate:

![](assets/img-0069.png)

La telefonia analogica POTS usa una sola coppia (due fili) e non ha alcun requisito di banda o impedenza paragonabile a Ethernet. Per questo motivo, storicamente e ancora oggi, è normalissimo usare cavi Ethernet come semplice doppino telefonico.

Dunque, in generale, il fatto che il cavo sia “Ethernet-grade” non implica che l’impianto sia dati.

Una presa RJ45 è solo un connettore meccanico e non è una “presa dati” per definizione. Diventa tale solo se:

   1. il cavo è a 4 coppie integre,
   1. le coppie sono terminate correttamente secondo T568A o T568B (la differenza principale tra T568A e T568B è lo scambio delle coppie di fili verde e arancione)
   1. l’altro capo arriva a un patch panel o a uno switch Ethernet
   1. l’impianto stesso non è collegato alla rete telefonica analogica.

Nel caso specifico del mio impianto domestico, sebbene ci sia scritto “DATI” nella presentazione del lavoro preliminare dell’impianto:

![](assets/img-0070.png)

Ci sia scritto:

![](assets/img-0071.png)

la presa RJ45 è stata cablata come presa telefonica: una sola coppia del cavo (tipicamente la centrale blu o arancione) è collegata alla linea telefonica, le altre coppie sono inutilizzate o nemmeno terminate. Elettricamente è quindi un impianto POTS, anche se esteticamente sembra “dati”.

Questo accade spesso perché nei cablaggi un po' più recenti si posa solo Cat 5e/6 perché costa poco, è universale e future-proof e il costruttore o l’elettricista usa RJ45 ovunque anche per uniformità estetica (soprattutto su richiesta). La destinazione d’uso iniziale era solo telefonica, quindi non si è completata la terminazione Ethernet ma è la stessa infrastruttura fisica.

In ambito aziendale si facevano (e si fanno) tre cose diverse come il telefono analogico su una coppia del Cat 5e e il telefono digitale proprietario su una o due coppie mentre il telefono VoIP è quello che usa Ethernet vero e proprio (tutte le coppie, switch, VLAN, PoE).

Nel tuo caso sei nel primo scenario: cavo dati usato come doppino telefonico.

La conseguenza è importante e netta: quella presa non è utilizzabile come Ethernet finché l’impianto resta attestato sulla linea telefonica. Collegarci uno switch o un PC non funziona e può anche danneggiare l’apparato se sulla linea c’è tensione di chiamata (tipicamente ~70-90 V AC a riposo di squillo).

Per trasformarla in presa dati serve un intervento preciso e non ambiguo:

scollegare completamente la linea telefonica analogica;

verificare che il cavo sia Cat 5e o superiore continuo fino all’altro capo;

terminare tutte e quattro le coppie su RJ45 secondo standard T568A o B, uguale da entrambi i lati;

portare l’altro capo su patch panel o direttamente su uno switch Ethernet.

Se questo non è stato fatto, la presa è e rimane telefonica, indipendentemente dalla scritta “RJ45”.

Sui corrugati: sì, la fonia può passare anche nei corrugati dell’impianto elettrico solo se si rispettano le distanze e le norme CEI sulla separazione dei circuiti SELV da quelli a 230 V. In pratica, nei lavori moderni seri si evitano corrugati promiscui o si usano separatori interni. Il fatto che funzioni elettricamente non significa che sia conforme.

Conclusione tecnica, senza ambiguità:

hai una presa RJ45 che non è una presa dati, ma una presa telefonica cablata su cavo dati. È una scelta diffusissima, corretta dal punto di vista funzionale, ma che genera confusione perché il connettore non racconta la verità sull’impianto. Il discriminante non è la presa, è la terminazione e cosa c’è dall’altra parte del cavo.

O faccio passare
