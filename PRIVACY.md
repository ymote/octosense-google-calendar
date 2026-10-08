# Privacy — Google Calendar for OctoSense

Effective 2026-10-08 · Publisher: ymote · [简体中文](PRIVACY.zh-CN.md)

This describes version `0.2.0`, app ID `io.github.ymote.googlecalendar`,
running in the compatible OctoSense development host. Live Google operation
remains unverified for this sample. The publisher operates no account service,
analytics endpoint or separate Calendar backend for this app.

## What is processed, and where

| Data | Purpose and destination |
| --- | --- |
| Google account identity, email and OAuth tokens | The host performs Google authorization. The bundle receives an app-bound opaque connection handle and account metadata, never the token or password. On macOS the normal host uses the platform credential vault for tokens. Google processes the authorization and API requests. |
| Calendar names, IDs, timezone and event records | The updated host reads a finite agenda from the selected calendar through Google APIs (past 30 days / next 366 days at refresh); this is not a complete historical export. It stores a local cache partitioned by app, connection and calendar, including event contents, ETags and sync state. Failed sync pages do not replace the last complete cache. |
| Unsent event draft and selected account/calendar | Stored in the app's local files, along with published-event route bindings. Draft contents include title, dates, times, timezone, location and notes. They are not submitted as event writes until the host review is approved. |
| Event changes | The host shows the exact proposed event before a create/update request to Google. Google and people permitted to access the destination calendar may see the resulting event. This sample does not implement invitation sending. |
| Explicitly published Glance card | Event title, time, location, description and app-bound identity are passed to the local OctoSense Glance host for display and durable restoration. Anyone able to view that device screen may see them. Cards have a 24-hour display expiry; this is not a guarantee of immediate erasure from storage. Publication requests `notify: false`. |
| Optional AI conversation | When you send a question, the app supplies the selected event's title, times, timezone, location, notes, calendar/event IDs and opaque connection handle to its contained assistant. The configured model can also receive results from its four allowed Calendar read tools. Your configured model provider, which may be remote, processes this context. Host/model settings govern history and retention; no local-only model restriction is declared. |

The app asks for Google `openid` and `email`, calendar-list read access, and
calendar-event read/edit access. The host expands its `calendar.list` and
`calendar.events` aliases into Google's scope URIs. The selected calendar is an
app/host request boundary; the OAuth event scope itself is broader than one
calendar. Review Google's consent screen before granting it.

The bundle has no arbitrary network or device-file access grant. Its assistant
has no workspace-file access and no background trigger. The four declared tools
list calendars, read the cache, refresh events and read one event; all are private,
not shareable, and read-only. The assistant cannot book or modify events. Using
host services still sends data to Google or your chosen model as described above.
The app does not implement automatic preference export to the system agent.

## Your controls and retention

- Use the app without AI, or decline its first-use agent consent. Avoid putting
  sensitive event details in AI questions unless your provider settings suit them.
- **Disconnect** removes the app's usable host connection and its stored token.
  It deliberately retains unsent local drafts; do not treat disconnect as deleting
  every cached file, card or conversation. It does not implement a Google-side
  OAuth revocation request. You can separately revoke access with Google.
- The compatible host's uninstall cleanup removes app connection bindings,
  Calendar cache and published-card records. Local app data and conversation
  lifecycle are managed by the host. Provider copies, already saved Google events,
  backups and model-provider retention are separate; uninstall does not delete them.
- No credentials or private calendars are bundled in the repository. Public
  screenshots and receipts use fictional events. Historical real-model evidence
  used synthetic event contents, not a real Google calendar.

For privacy questions use [the repository issue tracker](https://github.com/ymote/octosense-google-calendar/issues).
It is public: share only a minimal, redacted description. Do not attach tokens,
profiles, real event exports or unredacted screenshots. There is no private support
inbox advertised by this repository.
