# Informativa sulla privacy — Seal

*Ultimo aggiornamento: 20 ottobre 2026*

Titolare del trattamento: MindContact — [privacy@mindcontact.net](mailto:privacy@mindcontact.net)

## In breve

- Seal non crea account, non chiede registrazione, non raccoglie nome, email o rubrica.

- Non abbiamo server: nessun codice, nessun segreto e nessuna passphrase viene inviato a noi.

- I codici sono salvati **cifrati**, anche sul telefono. La passphrase che li protegge non viene salvata da nessuna parte.

- L'unico dato che lascia il dispositivo per opera dell'app è quello raccolto da Google AdMob.

## Permessi e a cosa servono

| Permesso | Perché | Cosa lascia il dispositivo |
|---|---|---|
| Fotocamera | inquadrare il QR di un servizio; le immagini sono analizzate sul telefono e non vengono salvate | niente |
| Impronta o blocco schermo | aprire l'app; la verifica la fa Android, Seal riceve solo «sì» o «no» | niente |
| Internet | annunci | vedi «Pubblicità» |

Seal **non** chiede l'accesso alla memoria, alle foto, ai contatti né alla posizione.

## I tuoi codici

I segreti dei codici di verifica — con il nome del servizio e dell'account — sono salvati come **file cifrati**, uno per codice, in una cartella del telefono (`Android/media/app.mindcontact.seal`). Ogni file è cifrato con XChaCha20-Poly1305 con una chiave casuale; quella chiave è a sua volta cifrata con una chiave ricavata dalla tua passphrase (Argon2id).

**La passphrase non viene mai salvata**: né sul telefono, né altrove. Sul telefono resta solo la chiave già aperta, custodita dal Keystore di Android, così che l'app si apra con l'impronta senza chiederti la passphrase ogni volta. Senza la passphrase, i file nella cartella non si possono leggere — nemmeno da noi, che non li riceviamo comunque.

**Se perdi la passphrase e il telefono, i codici sono persi.** Non esiste un recupero, perché non esiste nessuno che possa farlo.

## La cartella e la condivisione

La cartella dei codici è leggibile da altre app con accesso ai file multimediali, e può essere copiata da un servizio di sincronizzazione che usi già (per esempio Syncthing, Mega o Drive), fra i tuoi dispositivi o verso altre persone. A copiarla è quel servizio, con le sue condizioni e la sua informativa: Seal si limita a scrivere i file. Chi ospita i file vede quanti sono, quando cambiano e il nome dei gruppi condivisi; non ne vede il contenuto.

Un **gruppo condiviso** è una sottocartella con una passphrase sua, che comunichi tu alle altre persone. Chi ha quella passphrase vede e può usare i codici del gruppo. Il nome che scrivi nelle impostazioni accompagna, dentro i file cifrati, i codici che aggiungi a un gruppo.

I codici eliminati restano nella cartella come segnaposto cifrati per trenta giorni — serve a impedire che un altro dispositivo li faccia riapparire — e poi spariscono.

## Appunti

Quando tocchi un codice, Seal lo copia negli appunti segnandolo come dato sensibile (su Android 13 e successivi non compare nell'anteprima) e lo cancella dopo 30 secondi, se nel frattempo non hai copiato altro.

## Pubblicità

Seal mostra un banner tramite Google AdMob, che può raccogliere l'identificativo pubblicitario, l'indirizzo IP, informazioni tecniche sul dispositivo e i dati di interazione con gli annunci. Google li tratta come titolare autonomo: [policies.google.com/technologies/ads](https://policies.google.com/technologies/ads)

Nello Spazio economico europeo, nel Regno Unito e in Svizzera, al primo avvio compare il messaggio di consenso di Google: fino alla risposta l'app non richiede alcun annuncio. Né i codici né i loro nomi arrivano alla rete pubblicitaria.

## Dati che restano sul dispositivo

Le preferenze dell'app (blocco con impronta, il nome per i gruppi, un identificativo casuale del dispositivo generato in locale) restano sul dispositivo. Seal è escluso dal backup di Google e dal trasferimento fra dispositivi.

**Disinstallando Seal, Android cancella anche la cartella dei codici.** Le copie che un servizio di sincronizzazione ha già portato altrove restano lì, cifrate: su un altro telefono si aprono con la passphrase.

## Minori

L'app non è rivolta a minori di 13 anni.

## I tuoi diritti

Non avendo account né backend, non deteniamo dati che ti riguardano. Per i dati trattati da Google AdMob, i diritti si esercitano presso Google.

Domande: [privacy@mindcontact.net](mailto:privacy@mindcontact.net)
