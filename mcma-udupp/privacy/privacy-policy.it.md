# Informativa sulla privacy — udUPp

*Ultimo aggiornamento: 2 ottobre 2026*

Titolare del trattamento: MindContact — privacy@mindcontact.net

## In breve

- udUPp lavora sul **tuo** server Odoo, con il **tuo** account Odoo. Non crea
  account presso di noi e non abbiamo server: le tue fatture non passano da noi.
- **La password non viene mai salvata**: resta in memoria finché l'app è aperta
  e sparisce quando il sistema la chiude.
- Sul telefono restano l'indirizzo del server, il nome del database, il nome
  utente e una copia delle fatture mostrate, per poterle leggere senza rete.
- Oltre al traffico verso il tuo server, l'unico dato che lascia il dispositivo
  è quello raccolto da Google AdMob.

## Permessi e cosa servono

| Permesso | Perché | Cosa lascia il dispositivo |
|---|---|---|
| Internet | leggere le fatture dal tuo Odoo e registrare i pagamenti | l'indirizzo IP, nome utente e password (cifrati in HTTPS) e le richieste dell'app, **verso il tuo server Odoo** |
| Internet | annunci | vedi «Pubblicità» |

## Il tuo server Odoo

L'app parla direttamente con l'indirizzo che scrivi tu, solo in **HTTPS**:
gli indirizzi `http://` sono rifiutati, perché la password viaggerebbe in
chiaro. Nessun server intermedio nostro vede quel traffico.

Il server Odoo è tuo o di chi lo gestisce per te, che ne è titolare autonomo:
quello che succede lì — i registri degli accessi, i dati delle fatture, i
pagamenti registrati — segue le regole di quel server, non le nostre. Quando
premi «Segna come pagata», l'app registra il pagamento su Odoo con la stessa
procedura del client web, a nome del tuo utente.

## Quello che resta sul telefono

| Dato | Perché | Come si cancella |
|---|---|---|
| Indirizzo del server, database, nome utente | per chiederti solo la password al prossimo avvio | «Esci e dimentica», o disinstallando l'app |
| Copia delle fatture aperte e di quelle incassate nell'anno | per aprire l'app sull'elenco, anche senza rete | «Esci e dimentica», o disinstallando l'app |
| Password | **non viene salvata** | — |

Questi dati restano nella memoria privata dell'app: non finiscono in log, in
diagnostica né in parametri passati ad altri servizi, annunci compresi.

## Pubblicità

udUPp mostra annunci tramite Google AdMob, che può raccogliere
l'identificativo pubblicitario, l'indirizzo IP, informazioni tecniche sul
dispositivo e i dati di interazione con gli annunci. Google li tratta come
titolare autonomo: <https://policies.google.com/technologies/ads>

Nello Spazio economico europeo, nel Regno Unito e in Svizzera, al primo avvio
compare il messaggio di consenso di Google: fino alla risposta l'app non
richiede alcun annuncio.

## Minori

L'app non è rivolta a minori di 13 anni.

## I tuoi diritti

Non avendo account né backend, non deteniamo dati che ti riguardano: quelli
sul telefono li cancelli tu, quelli sul server Odoo li gestisce chi gestisce il
server. Per i dati trattati da Google AdMob, i diritti si esercitano presso
Google.

Domande: privacy@mindcontact.net

---

Questo file è il sorgente della pagina pubblicata su
<https://mindcontact.app/mcma-udupp/privacy/>. Le due copie — qui e in
`mcma-docs` — si aggiornano insieme, data compresa.
