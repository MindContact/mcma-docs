# Privacy policy — Seal

*Last updated: 20 October 2026*

Data controller: MindContact — [privacy@mindcontact.net](mailto:privacy@mindcontact.net)

## In short

- Seal creates no account, asks for no registration, collects no name, email or contacts.

- We have no servers: no code, no secret and no passphrase is ever sent to us.

- Your codes are stored **encrypted**, on the phone too. The passphrase that protects them is not stored anywhere.

- The only data that leaves the device because of the app is what Google AdMob collects.

## Permissions and what they are for

| Permission | Why | What leaves the device |
|---|---|---|
| Camera | scanning a service's QR; frames are analysed on the phone and never saved | nothing |
| Fingerprint or screen lock | opening the app; Android does the check, Seal only gets "yes" or "no" | nothing |
| Internet | ads | see "Advertising" |

Seal does **not** ask for access to storage, photos, contacts or location.

## Your codes

The secrets of your verification codes — with the service and account names — are stored as **encrypted files**, one per code, in a folder on the phone (`Android/media/app.mindcontact.seal`). Each file is encrypted with XChaCha20-Poly1305 under a random key; that key is in turn encrypted with a key derived from your passphrase (Argon2id).

**The passphrase is never stored**: not on the phone, not anywhere else. The phone keeps only the already opened key, held by the Android Keystore, so that the app opens with your fingerprint without asking for the passphrase every time. Without the passphrase the files in the folder cannot be read — not even by us, who never receive them anyway.

**If you lose both the passphrase and the phone, the codes are lost.** There is no recovery, because there is nobody who could perform one.

## The folder and sharing

The codes folder can be read by other apps with access to media files, and can be copied by a sync service you already use (for example Syncthing, Mega or Drive), between your devices or to other people. That service does the copying, under its own terms and privacy policy: Seal only writes the files. Whoever hosts the files sees how many there are, when they change and the names of shared groups; not their content.

A **shared group** is a subfolder with its own passphrase, which you give to the other people. Whoever has that passphrase sees and can use the group's codes. The name you write in the settings travels, inside the encrypted files, with the codes you add to a group.

Deleted codes stay in the folder as encrypted placeholders for thirty days — so that another device cannot bring them back — and then disappear.

## Clipboard

When you tap a code, Seal copies it to the clipboard marked as sensitive (on Android 13 and later it does not appear in the preview) and clears it after 30 seconds, unless you copied something else meanwhile.

## Advertising

Seal shows a banner through Google AdMob, which may collect the advertising identifier, the IP address, technical information about the device and ad interaction data. Google processes them as an independent controller: [policies.google.com/technologies/ads](https://policies.google.com/technologies/ads)

In the European Economic Area, the United Kingdom and Switzerland, Google's consent message appears at first launch: until you answer, the app requests no ads. Neither the codes nor their names reach the ad network.

## Data that stays on the device

The app's preferences (fingerprint lock, your name for groups, a random device identifier generated locally) stay on the device. Seal is excluded from Google backup and from device-to-device transfer.

**Uninstalling Seal makes Android delete the codes folder too.** Copies a sync service has already carried elsewhere stay there, encrypted: on another phone they open with the passphrase.

## Children

The app is not directed at children under 13.

## Your rights

Having no accounts and no backend, we hold no data about you. For data processed by Google AdMob, rights are exercised with Google.

Questions: [privacy@mindcontact.net](mailto:privacy@mindcontact.net)
