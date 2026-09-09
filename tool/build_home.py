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
import pathlib

APPS = json.loads((pathlib.Path(__file__).parent / "apps.json").read_text())

STRINGS = {
    "it": dict(
        lang="it", css="style.css", base="", other='<strong>Italiano</strong><a href="en/">English</a>',
        title="MindContact — piccole app che fanno una cosa sola",
        desc="Ventisei app per Android: nessun account, nessun server, i calcoli restano sul telefono.",
        h1="Piccole app che fanno<br>una cosa sola",
        lede="Ventisei strumenti per Android — la bussola, l'accordatore, il fonometro, il calendario dell'orto. Ognuno fa il suo mestiere e basta: si apre e funziona, senza chiedere niente prima.",
        facts=["Nessun account", "Nessun server nostro", "Un'informativa per ognuna"],
        soon_h2="Stanno arrivando",
        soon_lede="Le prime app sono in lavorazione e arrivano su Google Play una alla volta. Questa pagina si aggiorna appena la prima è pubblicata: qui sotto comparirà, con la sua pagina e la sua informativa.",
        soon_note="Nel frattempo non c'è niente da scaricare e niente da lasciare: nessuna mail, nessun modulo.",
        apps_h2="Le app",
        apps_note="Arrivano su Google Play una alla volta.",
        more="e altre in arrivo",
        common_h2="Quello che vale per tutte",
        promise=[("Non ti viene chiesto chi sei", "Nessuna app crea un account o chiede una registrazione."),
                 ("Quello che calcola resta lì", "Non c'è un server nostro: il lavoro dell'app finisce sul telefono."),
                 ("Quello che esce è scritto", "L'unico dato che lascia il dispositivo è quello di Google AdMob per gli annunci, e ogni informativa lo dice per esteso.")],
        contact="Scrivici:", privacy="Privacy", other_lang="English"),
    "en": dict(
        lang="en", css="../style.css", base="../", other='<a href="../">Italiano</a><strong>English</strong>',
        title="MindContact — small apps that do one thing",
        desc="Twenty-six Android apps: no account, no server, the work stays on the phone.",
        h1="Small apps that do<br>one thing",
        lede="Twenty-six tools for Android — the compass, the tuner, the sound level meter, the kitchen garden calendar. Each does its own job and nothing else: it opens and works, without asking for anything first.",
        facts=["No account", "No server of ours", "A policy for each one"],
        soon_h2="On their way",
        soon_lede="The first apps are being built, and they reach Google Play one at a time. This page updates as soon as the first one is out: it will appear right here, with its own page and its privacy policy.",
        soon_note="In the meantime there is nothing to download and nothing to leave behind: no email, no form.",
        apps_h2="The apps",
        apps_note="They reach Google Play one at a time.",
        more="and more on the way",
        common_h2="True of every one",
        promise=[("Nobody asks who you are", "No app creates an account or asks you to register."),
                 ("What it works out stays there", "There is no server of ours: the app's work ends on the phone."),
                 ("What leaves is written down", "The only data leaving the device is Google AdMob's, for the ads, and every policy spells it out.")],
        contact="Write to us:", privacy="Privacy", other_lang="Italiano"),
}


def _cards(lang: str, t: dict) -> str:
    base = t["base"]
    out = []
    for app in sorted((a for a in APPS if a["published"]), key=lambda a: a["name"].lower()):
        slug = app["slug"]
        page = f"{base}{slug}/en/" if lang == "en" else f"{base}{slug}/"
        privacy = f"{base}{slug}/privacy/en/" if lang == "en" else f"{base}{slug}/privacy/"
        alt = f"{base}{slug}/" if lang == "en" else f"{base}{slug}/en/"
        out.append(f"""    <li class="card">
      <img src="{base}{slug}/assets/icon.png" alt="" width="44" height="44" loading="lazy" decoding="async">
      <div class="card-body">
        <h3><a href="{page}">{app['name']}</a></h3>
        <p>{app[lang]}</p>
        <p class="card-links"><a href="{privacy}">{t['privacy']}</a><span>·</span><a href="{alt}">{t['other_lang']}</a></p>
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
  <p class="updated">{t['more']}</p>
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

  <p class="contact">{t['contact']} <a href="mailto:support@mindcontact.net">support@mindcontact.net</a></p>

  <footer>
    MindContact · <a href="https://github.com/MindContact">github.com/MindContact</a>
  </footer>
</main>
</body>
</html>
"""


def main() -> None:
    root = pathlib.Path(__file__).parent.parent
    (root / "index.html").write_text(build("it"))
    (root / "en" / "index.html").write_text(build("en"))
    live = sum(1 for a in APPS if a["published"])
    print(f"home rigenerata: {live} app pubblicate su {len(APPS)}")


if __name__ == "__main__":
    main()
