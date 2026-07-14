# Home Lab Cybersecurity e Networking

Questo repository raccoglie il materiale di pianificazione per un home lab di rete e
cybersecurity: non è ancora un progetto scritto in codice, ma la base di conoscenza che
precede la costruzione vera e propria di una rete domestica segmentata con un'appliance
firewall dedicata. Il lavoro qui dentro serve a decidere cosa costruire prima di mettere
mano a cavi, VLAN e regole del firewall.

## Stato del progetto

Il repository è nella fase di raccolta riferimenti e progettazione, non nella fase di
implementazione. Non ci sono ancora regole firewall, configurazioni di segmentazione VLAN,
stack di monitoraggio o script committati: quello che c'è è materiale di studio e di
riferimento, insieme a una bozza di schema di rete da finalizzare. Chi legge questo
repository aspettandosi un lab funzionante troverebbe solo l'impalcatura di pianificazione,
il che è intenzionale nello stato attuale.

## Materiale raccolto

La cartella `OPNsense/` contiene un whitepaper sulle funzionalità del firewall OPNsense,
scelto come appliance di riferimento per il lab, insieme a un documento di consultazione
rapida sulle stesse funzionalità. La cartella `Diagram/` contiene una bozza di schema di
rete, collegata a un file esterno draw.io più alcuni appunti scritti a mano, ancora da
finalizzare nello strumento di disegno. Un elenco comparativo (`privacy pack.txt`) confronta
alternative rispettose della privacy ai principali servizi cloud, dall'email allo storage
alle mappe alla messaggistica: materiale utile per decidere quali servizi ospitare
localmente nel lab piuttosto che affidare a terzi. È presente anche un link a un articolo di
terze parti su una piccola rete in stile enterprise, preso come riferimento di progettazione,
e un documento Word (`PROGETTO rete e networking domestica.docx`) che abbozza per esteso
l'intero progetto di rete domestica.

## Cosa manca

Manca tutto ciò che rende un home lab operativo: le regole del firewall OPNsense, la
segmentazione VLAN vera e propria, uno stack di monitoraggio per la sicurezza di base, e lo
schema di rete finale (oggi solo bozza). Il repository documenta l'intenzione di cablare una
rete domestica con firewall dedicato e monitoraggio di sicurezza di base, ma quella fase non
è ancora iniziata.
