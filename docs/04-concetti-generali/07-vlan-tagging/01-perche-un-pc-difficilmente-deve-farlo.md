# Perché un PC difficilmente deve farlo

In pratica per i PC metti porte “access” e non serve VLAN tagging lato Windows/Linux. In generale anche questo dipende da come si configurano le porte del modem/router.

Di solito un PC non deve fare VLAN tagging perchè riceve già i frame “puliti” dal router come una normale rete ed è la configurazione più comune. Difficilmente il PC ha bisogno che la porta sia taggata come trunk perchè un PC deve vivere in più reti contemporaneamente.
