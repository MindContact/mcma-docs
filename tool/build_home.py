#!/usr/bin/env python3
"""Genera la home di mindcontact.app, in italiano e in inglese.

Le app si accendono una alla volta: finché `published` è false in
tool/apps.json l'app non compare in home, e la pagina dice che sta per
arrivare. Quando pubblichi, metti true e rilancia:

    python3 tool/build_home.py

Le pagine delle singole app restano dove sono in ogni caso — servono agli
store, che vogliono un'informativa raggiungibile senza login — ma stanno
fuori dai motori di ricerca finché non le si toglie da robots.txt.
"""

from __future__ import annotations

import json
import re
import pathlib

APPS = json.loads((pathlib.Path(__file__).parent / "apps.json").read_text())

STRINGS = {
    "it": dict(
        lang="it", css="style.css", base="", other='<strong>Italiano</strong><a href="en/">English</a>',
        title="MindContact — piccole app che fanno una cosa sola",
        desc="App per Android che fanno una cosa sola: nessun account, nessun server, i calcoli restano sul telefono.",
        h1="Piccole app che fanno<br>una cosa sola",
        lede="Uno strumento per mestiere — la bussola, l'accordatore, il fonometro, il calendario dell'orto. Ognuno fa il suo e basta: si apre e funziona, senza chiedere niente prima.",
        facts=["Nessun account", "Nessun server nostro", "Un'informativa per ognuna"],
        soon_h2="Stanno arrivando",
        soon_lede="Le prime app sono in lavorazione e arrivano su Google Play una alla volta. Questa pagina si aggiorna appena la prima è pubblicata: qui sotto comparirà, con la sua pagina e la sua informativa.",
        soon_note="Nel frattempo non c'è niente da scaricare.",
        apps_h2="Le app",
        apps_note="Arrivano su Google Play una alla volta.",
        more="e altre in arrivo",
        common_h2="Quello che vale per tutte",
        promise=[("Non ti viene chiesto chi sei", "Nessuna app crea un account o chiede una registrazione."),
                 ("Quello che calcola resta lì", "Non c'è un server nostro: il lavoro dell'app finisce sul telefono."),
                 ("Quello che esce è scritto", "L'unico dato che lascia il dispositivo è quello di Google AdMob per gli annunci, e ogni informativa lo dice per esteso.")],
        privacy="Privacy", play="Google Play", other_lang="English",
        contact=dict(
            h2="Scrivici",
            lede="Una domanda su un'app, un problema, un'idea: rispondiamo noi, non un bot.",
            name="Nome", email="Email", message="Messaggio",
            consent='Ho letto l\'<a href="#privacy-form">informativa</a> e acconsento al trattamento dei dati per ricevere una risposta.',
            button="Invia il messaggio",
            sending="Invio in corso…",
            sent="Grazie, il messaggio è arrivato. Ti rispondiamo a breve.",
            error="Non siamo riusciti a inviare il messaggio. Riprova tra qualche minuto.",
            next="https://mindcontact.app/?inviato#contatti",
            close="Chiudi"),
        footer_privacy="Informativa del modulo di contatto"),
    "en": dict(
        lang="en", css="../style.css", base="../", other='<a href="../">Italiano</a><strong>English</strong>',
        title="MindContact — small apps that do one thing",
        desc="Android apps that do one thing: no account, no server, the work stays on the phone.",
        h1="Small apps that do<br>one thing",
        lede="One tool per job — the compass, the tuner, the sound level meter, the kitchen garden calendar. Each does its own and nothing else: it opens and works, without asking for anything first.",
        facts=["No account", "No server of ours", "A policy for each one"],
        soon_h2="On their way",
        soon_lede="The first apps are being built, and they reach Google Play one at a time. This page updates as soon as the first one is out: it will appear right here, with its own page and its privacy policy.",
        soon_note="In the meantime there is nothing to download.",
        apps_h2="The apps",
        apps_note="They reach Google Play one at a time.",
        more="and more on the way",
        common_h2="True of every one",
        promise=[("Nobody asks who you are", "No app creates an account or asks you to register."),
                 ("What it works out stays there", "There is no server of ours: the app's work ends on the phone."),
                 ("What leaves is written down", "The only data leaving the device is Google AdMob's, for the ads, and every policy spells it out.")],
        privacy="Privacy", play="Google Play", other_lang="Italiano",
        contact=dict(
            h2="Write to us",
            lede="A question about an app, a problem, an idea: a person answers, not a bot.",
            name="Name", email="Email", message="Message",
            consent='I have read the <a href="#privacy-form">notice</a> and agree to the processing of my data in order to receive a reply.',
            button="Send the message",
            sending="Sending…",
            sent="Thank you, your message has arrived. We will get back to you shortly.",
            error="We could not send your message. Please try again in a few minutes.",
            next="https://mindcontact.app/en/?sent#contatti",
            close="Close"),
        footer_privacy="Contact form privacy notice"),
}


# Contact form backend shared by every MindContact site (../mindcontact-forms).
FORM_ENDPOINT = "https://forms.mindcontact.net/v1/contact"
PRIVACY_VERSION = "2026-10-29"
CONTROLLER = "MindContact di Luttino Roberto, Via Ivrea 41, 10016 Montalto Dora (TO), P.IVA 10699860010"

FORM_PRIVACY = {
    "it": ("Informativa del modulo di contatto", [
        (None, "Informativa ai sensi dell'art. 13 del Regolamento (UE) 2016/679 (GDPR) per chi scrive con il modulo di contatto di questo sito. Le app hanno ciascuna la propria informativa."),
        ("Titolare del trattamento", f"{CONTROLLER}, raggiungibile con il modulo di contatto di questa pagina."),
        ("Quali dati", "Nome, indirizzo email e il testo del messaggio. All'invio registriamo anche la prova del consenso: data e ora, versione di questa informativa e un'impronta cifrata (hash) dell'indirizzo IP, da cui non si risale all'indirizzo."),
        ("Perché", "Solo per leggere la richiesta e rispondere. Base giuridica: il consenso (art. 6.1.a). Nessuna profilazione, nessuna newsletter, nessuna cessione a terzi."),
        ("Come", "Il modulo è gestito da un servizio di MindContact su un server in Italia, che conserva il registro dei consensi e inoltra il messaggio per email. Il fornitore del server e quello della posta trattano i dati per nostro conto."),
        ("Per quanto", "I messaggi per il tempo necessario a rispondere, e comunque non oltre 12 mesi dall'ultimo contatto; il registro del consenso finché potremmo doverlo dimostrare."),
        ("I tuoi diritti", "Accesso, rettifica, cancellazione, limitazione, portabilità, opposizione (artt. 15–22) e revoca del consenso, scrivendoci con lo stesso modulo o all'indirizzo postale del titolare. Puoi anche rivolgerti al Garante per la protezione dei dati personali (garanteprivacy.it)."),
    ]),
    "en": ("Contact form privacy notice", [
        (None, "Information under Article 13 of Regulation (EU) 2016/679 (GDPR) for anyone who writes through the contact form on this site. Each app has its own privacy policy."),
        ("Data controller", f"{CONTROLLER}, reachable through the contact form on this page."),
        ("What data", "Name, email address and the text of the message. When you send it we also record proof of consent: date and time, the version of this notice and an encrypted fingerprint (hash) of the IP address, from which the address cannot be recovered."),
        ("Why", "Only to read the request and reply. Legal basis: consent (Art. 6.1.a). No profiling, no newsletter, no handing over to third parties."),
        ("How", "The form is handled by a MindContact service on a server in Italy, which keeps the consent register and forwards the message by email. The server and mail providers process the data on our behalf."),
        ("How long", "Messages for as long as needed to reply, and no longer than 12 months after the last contact; the consent record for as long as we may need to prove it."),
        ("Your rights", "Access, rectification, erasure, restriction, portability, objection (Arts. 15–22) and withdrawal of consent, by writing through the same form or to the controller's postal address. You can also complain to the Italian Data Protection Authority (garanteprivacy.it)."),
    ]),
}


def _contact(lang: str, t: dict) -> str:
    c = t["contact"]
    return f"""  <section id="contatti">
  <h2>{c['h2']}</h2>
  <p class="measure">{c['lede']}</p>
  <form class="form" action="{FORM_ENDPOINT}" method="POST" data-contact-form
        data-sending="{c['sending']}" data-sent="{c['sent']}" data-error="{c['error']}">
    <input type="hidden" name="site" value="mindcontact.app">
    <input type="hidden" name="lang" value="{lang}">
    <input type="hidden" name="privacy_version" value="{PRIVACY_VERSION}">
    <input type="hidden" name="_next" value="{c['next']}">
    <input class="honey" type="text" name="_honey" tabindex="-1" autocomplete="off" aria-hidden="true">
    <label class="field"><span>{c['name']}</span><input name="nome" type="text" required autocomplete="name" maxlength="120"></label>
    <label class="field"><span>{c['email']}</span><input name="email" type="email" required autocomplete="email" maxlength="254"></label>
    <label class="field field--full"><span>{c['message']}</span><textarea name="messaggio" rows="5" required maxlength="5000"></textarea></label>
    <label class="check field--full"><input type="checkbox" name="consenso" value="si" required><span>{c['consent']}</span></label>
    <div class="actions field--full">
      <button type="submit">{c['button']}</button>
      <p class="form-status" role="status" aria-live="polite"></p>
    </div>
  </form>
  </section>"""


def _form_privacy(lang: str, t: dict) -> str:
    title, parts = FORM_PRIVACY[lang]
    body = "\n".join((f"    <h3>{h}</h3>\n" if h else "") + f"    <p>{p}</p>" for h, p in parts)
    return f"""<dialog class="modal" id="privacy-form" aria-labelledby="privacy-form-title">
  <form method="dialog" class="modal-close"><button type="submit" aria-label="{t['contact']['close']}">×</button></form>
  <div class="modal-body">
    <h2 id="privacy-form-title">{title}</h2>
{body}
    <p class="updated">{PRIVACY_VERSION}</p>
  </div>
</dialog>"""


def _cards(lang: str, t: dict) -> str:
    base = t["base"]
    out = []
    for app in sorted((a for a in APPS if a["published"]), key=lambda a: a["name"].lower()):
        slug = app["slug"]
        page = f"{base}{slug}/en/" if lang == "en" else f"{base}{slug}/"
        privacy = f"{base}{slug}/privacy/en/" if lang == "en" else f"{base}{slug}/privacy/"
        alt = f"{base}{slug}/" if lang == "en" else f"{base}{slug}/en/"
        # The store link only exists once the app is live: an app can be
        # published on this page (its policy has to be reachable) before its
        # listing answers.
        play = (
            f'<a href="https://play.google.com/store/apps/details?id={app["package"]}">'
            f'{t["play"]}</a><span>·</span>'
            if app.get("package")
            else ""
        )
        out.append(f"""    <li class="card">
      <img src="{base}{slug}/assets/icon.png" alt="" width="44" height="44" loading="lazy" decoding="async">
      <div class="card-body">
        <h3><a href="{page}">{app['name']}</a></h3>
        <p>{app[lang]}</p>
        <p class="card-links">{play}<a href="{privacy}">{t['privacy']}</a><span>·</span><a href="{alt}">{t['other_lang']}</a></p>
      </div>
    </li>""")
    return "\n".join(out)


def build(lang: str) -> str:
    t = STRINGS[lang]
    published = [a for a in APPS if a["published"]]

    if published:
        body = f"""  <h2>{t['apps_h2']}</h2>
  <p class="updated">{t['apps_note']}</p>
  <ul class="grid">
{_cards(lang, t)}
  </ul>
  <p class="updated more">{t['more']}</p>
"""
    else:
        body = f"""  <h2>{t['soon_h2']}</h2>
  <p class="lede">{t['soon_lede']}</p>
  <p class="updated">{t['soon_note']}</p>
"""

    facts = "\n".join(f"    <li>{f}</li>" for f in t["facts"])
    promise = "\n".join(
        f"    <li><strong>{h}</strong><span>{p}</span></li>" for h, p in t["promise"]
    )
    return f"""<!doctype html>
<html lang="{t['lang']}">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{t['title']}</title>
<meta name="description" content="{t['desc']}">
<link rel="stylesheet" href="{t['css']}">
<link rel="icon" href="/favicon.svg" type="image/svg+xml">
<link rel="icon" href="/favicon.ico" sizes="48x48">
<link rel="apple-touch-icon" href="/apple-touch-icon.png">
</head>
<body>
<!-- Generata da tool/build_home.py: non modificarla a mano, si riscrive. -->
<main>
  <p class="lang">{t['other']}</p>

  <header class="hero">
    <h1>{t['h1']}</h1>
    <p class="lede">{t['lede']}</p>
    <ul class="facts">
{facts}
    </ul>
  </header>

{body}
  <h2>{t['common_h2']}</h2>
  <ul class="promise">
{promise}
  </ul>

{_contact(lang, t)}

  <footer>
    MindContact di Luttino Roberto · Via Ivrea 41, 10016 Montalto Dora (TO) · P.IVA 10699860010<br>
    <a href="#privacy-form">{t['footer_privacy']}</a> · <a href="https://github.com/MindContact">github.com/MindContact</a>
  </footer>
</main>
{_form_privacy(lang, t)}
<script src="{t['base']}form.js" defer></script>
</body>
</html>
"""


def main() -> None:
    root = pathlib.Path(__file__).parent.parent
    (root / "index.html").write_text(new_tab(build("it")))
    (root / "en" / "index.html").write_text(new_tab(build("en")))
    live = sum(1 for a in APPS if a["published"])
    print(f"home rigenerata: {live} app pubblicate su {len(APPS)}")



ANCHOR = re.compile(r'<a\b([^>]*?)\bhref="(https?://[^"]*)"([^>]*)>')


def new_tab(html):
    """Absolute links open in a new tab; in-page and relative links stay (owner rule, 2026-10-29).
    Same logic as ../mindcontact-identity/tools/link_nuova_scheda.py."""
    def fix(m):
        attrs = m.group(1) + m.group(3)
        if "target=" in attrs:
            return m.group(0)
        if 'rel="' in attrs:
            return m.group(0)[:-1] + ' target="_blank">'
        return m.group(0)[:-1] + ' target="_blank" rel="noopener">'
    return ANCHOR.sub(fix, html)

if __name__ == "__main__":
    main()
