# Privacy policy — udUPp

*Last updated: 2 October 2026*

Data controller: MindContact — privacy@mindcontact.net

## In short

- udUPp works on **your** Odoo server, with **your** Odoo account. It creates
  no account with us and we have no servers: your invoices do not pass
  through us.
- **The password is never saved**: it stays in memory while the app is open
  and is gone when the system closes it.
- The phone keeps the server address, the database name, the user name and a
  copy of the invoices on screen, so they can be read offline.
- Besides the traffic to your server, the only data leaving the device is
  what Google AdMob collects.

## Permissions and what they are for

| Permission | Why | What leaves the device |
|---|---|---|
| Internet | read the invoices on your Odoo and register payments | the IP address, user name and password (encrypted over HTTPS) and the app's requests, **to your Odoo server** |
| Internet | ads | see "Advertising" |

## Your Odoo server

The app talks directly to the address you type, over **HTTPS** only: `http://`
addresses are refused, because the password would travel in the clear. No
server of ours sits in between.

The Odoo server is yours, or whoever runs it for you, who is an independent
controller: what happens there — access logs, invoice data, registered
payments — follows that server's rules, not ours. When you press "Mark as
paid", the app registers the payment on Odoo the way the web client does, as
your user.

## What stays on the phone

| Data | Why | How to delete it |
|---|---|---|
| Server address, database, user name | so that next time only the password is asked | "Sign out and forget", or uninstalling the app |
| Copy of open invoices and of those collected this year | to open the app on the list, offline too | "Sign out and forget", or uninstalling the app |
| Password | **not saved** | — |

This data stays in the app's private storage: it does not end up in logs, in
diagnostics or in parameters passed to other services, ads included.

## Advertising

udUPp shows ads through Google AdMob, which may collect the advertising ID,
the IP address, technical information about the device and ad interaction
data. Google processes them as an independent controller:
<https://policies.google.com/technologies/ads>

In the European Economic Area, the United Kingdom and Switzerland, Google's
consent message appears on first launch: until it is answered the app requests
no ads.

## Children

The app is not directed at children under 13.

## Your rights

With no accounts and no backend, we hold no data about you: what is on the
phone you delete yourself, what is on the Odoo server is managed by whoever
runs it. For data processed by Google AdMob, rights are exercised with Google.

Questions: privacy@mindcontact.net
