SCRIVANIA DIGITALE
==================

La "Scrivania Digitale" è un’applicazione web che permette la gestione
dei flussi Documentali all’interno di un Ente, di un'azienda o di una
qualsiasi realtà strutturata di medie e grandi dimensioni.

Il Sistema ha come obiettivo principale quello di guidare gli utenti nella gestione dei vari procedimenti amministrativi. In
particolare è stata predisposta per:

-  **Dematerializzare** (dematerializzazione del cartaceo)

-  **Semplificare** (firma leggera, firma digitale, reingegnerizzazione)

-  **Velocizzare** (smistamento ed assegnazione in automatico dei
   compiti ai diversi attori coinvolti);

-  **Organizzare** (ogni utente ha la lista dei propri compiti)

-  **Proteggere** (Migliora la protezione delle informazioni: permessi
   utenti)

-  **Tracciare** (tracciamento delle attività con possibilità di
   monitoraggio dello stato di avanzamento)

-  **Informare** (notifiche)

-  **Armonizzare** (armonizzazione delle modalità operative di
   espletamento del procedimento amministrativo da parte delle diverse
   strutture)

-  **Ottimizzare** (ottimizzazione dei processi amministrativi)

-  **Facilitare** adempimento agli obblighi Normativi (es. per Acquisti
   adempimento automatico degli obblighi di trasparenza.)

-  **Guidare** (guida e limita l’utente nelle azioni fornendo una
   maggior aderenza ai processi )

-  **Supervisionare** (la ricerca dei flussi permette avere sotto
   controllo i processi)

Le funzionalità sviluppate a supporto dell'esecuzione dei processi
amministrativi sono:

-  **Gestione dell'autenticazione** che può avvenire attraverso utenze
   locali all'applicazione, attraverso LDAP oppure attraverso ulteriori
   gestori di utenze (es. ACE, da aggiungere ad-hoc)

-  **Gestione delle autorizzazioni** sia in locale che attraverso
   gestori esterni (es. ACE)

-  **Gestione dei metadati** per ogni processo, compresi gli allegati, e
   la cronologia dettagliata (chi ha fatto cosa e quando)

-  **Gestione dei compiti e delle visibilità** dei flussi amministrativi

-  **Notifiche email** sia predefinite (es. "hai un nuovo compito") che
   personalizzate (es. "Il tuo compito è in attesa da X giorni")

-  **Gestione Firma Digitale** interna ai flussi amministrativi
   (richiede sign-server esterno)

-  **Comunicazione con altre applicazioni** attraverso interfacce REST
   (altre applicazioni possono eseguire compiti in Scrivania ed eventi
   in Scrivania possono chiamare REST di altre applicazioni)

-  **Azioni custom** per ogni tipo di evento (da sviluppare ad hoc)

-  **Generazione report e statistiche** in .pdf e in .csv

**VERSIONE STAND ALONE**

La versione "Stand Alone" di Scrivania Digitale è una versione che tende
ad utilizzare quanto più possibile risorse interne rispetto ad
applicazioni aggiuntive. Ad esempio non si appoggia a nessun Repository
Documentale esterno per i documenti che vengono inseriti nel DB o nel
filesystem locale. Utilizza un sistema interno per la profilazione,
l'autenticazione e la gestione delle utenze e dei ruoli assegnati.

**VERSIONE INTEGRATA**

La versione "Integrata" di Scrivania Digitale è una versione che tende
ad integrare quanto più possibile risorse e applicazioni esterne sia
open source e commerciali quali: un repository documentale esterno (es.
Alfresco, Azure, ...), un sistema di firma remota (es. ARSS Aruba Sign
Server); Questa versione è predisposta anche per integrarsi con
applicazioni realizzate internamente come l'Anagrafica Centralizzata, e
altre applicazioni che possono collegarsi direttamente a flussi
specifici. Tali applicazioni avranno una propria gestione interna dei
dati e si avvarranno di Scrivania per la parte amministrativa (es. firma
digitale).

`Vai al codice <https://github.com/consiglionazionaledellericerche/sprint-flows>`_
