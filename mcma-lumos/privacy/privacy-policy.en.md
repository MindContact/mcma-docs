# Privacy Policy — Lumos

**Last updated: 3 September 2026**

Lumos is a torch. It does one thing, and collects as little as possible to do it.

Data controller: MindContact — mindcontact.apps@gmail.com

## In short

* Lumos creates **no** account, asks for **no** sign-up, and collects **no**
  name, email or contacts.
* Microphone audio is **never** recorded, stored or sent to our servers. We have
  no servers.
* The camera captures **no** photos or video: it is opened only to switch on the
  LED flash.
* The only data that leaves your device is what Google AdMob collects in order
  to serve ads.

## Permissions and why they exist

| Permission | Why | What leaves the device |
|---|---|---|
| Camera | the LED flash is only reachable through the camera stack | nothing: no image is captured |
| Microphone | to hear the spells "Lumos", "Lumos Maxima", "Nox" | see "Speech recognition" |
| Internet | network speech recognition and ads | see the two sections below |
| Wake lock | keeping the screen awake while the light is needed | nothing |

## Speech recognition

Lumos does not perform speech recognition itself. It uses the recognition
service **installed on your device** (typically Google's on Android, Apple's on
iOS).

* Lumos receives only the recognised text, matches it against the three spells
  and discards it immediately.
* That text is never written to disk, and never transmitted by us to anyone.
* Depending on your device settings, recognition may happen on-device or on the
  operating system vendor's servers. In the latter case the audio is handled by
  that vendor under its own policy:
  * Google — https://policies.google.com/privacy
  * Apple — https://www.apple.com/legal/privacy/
* The microphone opens **only** after you tap the microphone button, and closes
  when you tap it again or leave the app.

### Which of the two recognisers Lumos uses

Lumos always prefers the device's **local** recogniser (on Android,
`createOnDeviceSpeechRecognizer`, available from version 12): the model runs on
the phone and the audio is not sent anywhere to be transcribed.

If that engine is missing or refuses to work, Lumos falls back to the system's
default recogniser — **and that one, depending on the device and the language,
may send the audio to the vendor's servers.** The fallback exists because on
many phones the local model is not installed, and a torch that cannot hear is a
broken torch.

If you would rather that never happened, turn on **"Listen offline only"** (tap
the LUMOS wordmark, top left). With that setting Lumos uses the local recogniser
and nothing else, and where there is none it says it cannot hear rather than
taking the network road. It is a guarantee, not a preference: the system
recogniser's own "prefer offline" flag is a request the platform may ignore,
which is why Lumos does not rely on it.

## Advertising

Lumos shows ads through **Google AdMob**. AdMob may collect and process:

* the device advertising identifier (Advertising ID / IDFA);
* IP address and technical device information;
* ad interaction data.

Google acts as an independent controller for this data. Policy and controls:
https://policies.google.com/technologies/ads

You can limit personalised ads from your system settings:

* **Android** — Settings › Privacy › Ads
* **iOS** — Settings › Privacy & Security › Tracking

In the European Economic Area, the United Kingdom and Switzerland, consent is
requested through Google's consent message before personalised ads are shown.
You may refuse and keep using the app: you will see non-personalised ads.

## Data we collect

None. Lumos has no backend, sends no telemetry, uses no analytics and stores no
personal data on the device. The only things stored are your preferences — wand
core, muted sounds, gestures, "Listen offline only" — which stay on the phone
and are never transmitted.

## Children

Lumos is not directed at children under 13 and does not knowingly collect data
from children.

## Your rights

Since we process no personal data, we hold nothing to export or delete. For data
collected by Google AdMob, those rights are exercised towards Google under its
policy. Uninstalling the app ends all collection.

## Changes

Any change to this policy will be published at this address, with the updated
date at the top.

## Contact

mindcontact.apps@gmail.com
