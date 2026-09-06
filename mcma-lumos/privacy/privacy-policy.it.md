# Informativa sulla privacy — Lumos

**Ultimo aggiornamento: 3 settembre 2026**

Lumos è una torcia. Fa una cosa sola e raccoglie il meno possibile per farla.

Titolare del trattamento: MindContact — mindcontact.apps@gmail.com

## In breve

* Lumos **non** crea account, **non** chiede registrazione, **non** raccoglie
  nome, email o rubrica.
* L'audio del microfono **non** viene registrato, salvato o inviato ai nostri
  server. Non abbiamo server.
* La fotocamera **non** cattura né foto né video: viene aperta solo per
  accendere il flash LED.
* L'unico dato che lascia il dispositivo è quello raccolto da Google AdMob per
  mostrare gli annunci.

## Permessi e a cosa servono

| Permesso | Perché | Cosa lascia il dispositivo |
|---|---|---|
| Fotocamera | il flash LED è accessibile solo attraverso lo stack fotocamera | nulla: nessuna immagine viene acquisita |
| Microfono | riconoscere gli incantesimi «Lumos», «Lumos Maxima», «Nox» | vedi "Riconoscimento vocale" |
| Internet | riconoscimento vocale di rete e annunci | vedi le due sezioni seguenti |
| Wake lock | tenere lo schermo acceso mentre la luce serve | nulla |

## Riconoscimento vocale

Il riconoscimento vocale non è svolto da Lumos: usiamo il servizio di
riconoscimento **installato sul tuo dispositivo** (su Android tipicamente quello
di Google, su iOS quello di Apple).

* Lumos riceve solo il testo riconosciuto, lo confronta con i tre incantesimi e
  lo scarta subito dopo.
* Il testo non viene salvato su disco né trasmesso da noi a nessuno.
* A seconda delle impostazioni del dispositivo, il riconoscimento può avvenire
  sul dispositivo o sui server del fornitore del sistema operativo. In
  quest'ultimo caso l'audio è trattato da quel fornitore secondo la sua
  informativa:
  * Google — https://policies.google.com/privacy
  * Apple — https://www.apple.com/legal/privacy/
* Il microfono si apre **solo** dopo che hai toccato il pulsante del microfono,
  e si chiude quando lo tocchi di nuovo o esci dall'app.

### Quale dei due riconoscitori usa Lumos

Lumos preferisce sempre il riconoscitore **locale** del dispositivo (su Android
`createOnDeviceSpeechRecognizer`, dalla versione 12 in poi): il modello gira sul
telefono e l'audio non viene inviato a nessuno per essere trascritto.

Se quel motore manca o rifiuta di funzionare, Lumos ripiega sul riconoscitore
predefinito del sistema — **e quello, a seconda del dispositivo e della lingua,
può inviare l'audio ai server del fornitore.** Il ripiego esiste perché su molti
telefoni il modello locale non è installato, e una torcia che non sente è una
torcia rotta.

Se preferisci che questo non accada mai, attiva **«Ascolta solo in locale»**
(tocca la scritta LUMOS in alto a sinistra). Con quell'opzione Lumos usa
esclusivamente il riconoscitore locale e, dove non c'è, dichiara di non poter
sentire invece di prendere la strada di rete. È una garanzia, non una
preferenza: l'opzione «preferisci offline» del riconoscitore di sistema è una
richiesta che il sistema può ignorare, e per questo Lumos non ci si affida.

## Pubblicità

Lumos mostra annunci tramite **Google AdMob**. AdMob può raccogliere e trattare:

* l'identificativo pubblicitario del dispositivo (Advertising ID / IDFA);
* l'indirizzo IP e informazioni tecniche sul dispositivo;
* dati di interazione con gli annunci.

Questi dati sono trattati da Google come titolare autonomo. Informativa e
opzioni: https://policies.google.com/technologies/ads

Puoi limitare gli annunci personalizzati dalle impostazioni del sistema:

* **Android** — Impostazioni › Privacy › Annunci
* **iOS** — Impostazioni › Privacy e sicurezza › Tracciamento

Nell'Area economica europea, nel Regno Unito e in Svizzera, prima di mostrare
annunci personalizzati viene richiesto il consenso tramite il messaggio di
Google (Consent Management Platform). Puoi rifiutare e continuare a usare
l'app: vedrai annunci non personalizzati.

## Dati raccolti da noi

Nessuno. Lumos non ha backend, non invia telemetria, non usa analytics e non
salva alcun dato personale sul dispositivo. Le uniche cose salvate sono le
preferenze — nucleo della bacchetta, suoni silenziati, gesti, «Ascolta solo in
locale» — che restano sul telefono e non vengono mai trasmesse.

## Minori

Lumos non è indirizzata ai minori di 13 anni e non raccoglie
consapevolmente dati di minori.

## I tuoi diritti

Non trattando dati personali, non abbiamo dati da esportare o cancellare.
Per i dati raccolti da Google AdMob, i diritti si esercitano verso Google
secondo la sua informativa. Disinstallare l'app interrompe ogni raccolta.

## Modifiche

Eventuali modifiche a questa informativa saranno pubblicate a questo indirizzo,
con la data di aggiornamento in cima.

## Contatti

mindcontact.apps@gmail.com
