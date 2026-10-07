# Google Calendar for OctoSense

English | [简体中文](README.zh-CN.md)

A **macOS development preview** for viewing Google Calendar, keeping event
drafts, reviewing edits and discussing an event with your configured assistant.
Publisher: **ymote**. App ID: `org.octosense.samples.googlecalendar`; version: `0.1.1` (publisher-signed preview).
This is an independent sample, not a Google product.

Use the [OctoSense desktop-v0.1.0-beta.2 macOS Apple Silicon preview](https://github.com/OctoSense-org/OctoSense/releases/tag/desktop-v0.1.0-beta.2).
The signed `0.1.1` bundle is available in the official App Hub catalog
([sequence 10, App Hub #133](https://github.com/OctoSense-org/OctoSense-App-Hub/pull/133)).
**Live Google login, reads, writes and physical approval have not been validated
for this sample.** Android Google authorization is missing; Android, Linux and
Windows are not listed as supported platforms.

## Use the app

In OctoSense, open **App Hub → Search**, search **Google Calendar**, then choose
**Get → Install → Open** after reviewing the requested permissions. You can prepare
local event drafts before connecting an account. The `v0.1.1` release tag and
previous `v0.1.0` tag remain immutable.

For Google access, the host operator must configure a Google OAuth client outside
this repository; follow the [versioned host setup guide](https://github.com/OctoSense-org/OctoSense/blob/desktop-v0.1.0-beta.2/crates/oauth-service/README.md). Enter credentials
only in the host/provider flow. No separate OctoSense account is required.

1. Open **Account → Connect Google**, complete consent and choose a calendar.
2. Use **Refresh** to sync. The updated host returns a finite agenda: **past 30 days /
   next 366 days**, relative to the successful refresh. The app displays that range
   for both refreshed and cached data. A failed sync keeps the last complete cache.
   Older hosts/caches without window metadata say **date range unavailable**;
   refresh with the updated host to obtain a bounded agenda. An event absent from
   this window is not necessarily deleted from Google Calendar.
3. Select **+ Event** or an event's **Edit** action. Set both dates/times and an
   explicit IANA timezone; **Keep draft** retains unfinished work locally.
4. **Review & Save** opens a host-owned review of the exact event. Check the
   account, calendar, time and content before approving. Conflicts keep your
   draft and require reviewing the latest event instead of overwriting it.
5. **Glance** publishes the selected event for 24 hours without a notification.
   Its **Open Calendar** action returns to that event in this app.
6. **Chat** sends the selected event context and your question to your configured
   model after host consent. The assistant can read through four private tools;
   it **cannot book, create or edit events**. Apply suggestions in the editor.

Recurring series show their original start; occurrence expansion, recurrence
editing and attendee invitations are outside this version. Glance-card and
full-app chats have not been verified to share conversation history.

## Evidence and development

Version 0.1.1 changes only range/status handling and release metadata; its UI
layout, agent instructions, tool declarations and original screenshots remain
unchanged. The 0.1.0 source originated in the [immutable App Design Flow sample](https://github.com/OctoSense-org/OctoScript-App-Design-Flow/tree/5b0fde7ed0e9e4131751d16f55ba3d8a3180dd95/examples/connected-apps/google-calendar).
Historical macOS tests covered eight signed-install/provider-fixture journeys,
six Glance/routing journeys, real DeepSeek advice about synthetic events, and a
36-cycle/620-second native soak. These are **synthetic Calendar provider tests**,
not live Google validation. Original captures and receipts are in [evidence/](evidence/);
[provenance and limitations](ACCEPTANCE.md) preserve their original identities.
They are not new native/provider execution evidence for 0.1.1. Run
`python3 -m unittest discover -s tests -v` for its focused release-contract checks.
The signed 0.1.0 gate/release records are archived in `review/releases/0.1.0/`;
current signed verification is in `review/GATE.txt` and `review/RELEASE.json`.

To verify a signed release, put the compatible App Hub tools on `PATH` and run
from this repository (Python reads only the published public key):

```sh
CALENDAR_PUBLISHER_KEY="$(python3 -c 'import json; print(json.load(open("publisher.json"))["public_key"])')"
hub check bundle --publisher-key "ymote=$CALENDAR_PUBLISHER_KEY"
mkdir -p build
hub scan bundle --publisher-key "ymote=$CALENDAR_PUBLISHER_KEY" --packet build/review.json
```

Do not stamp or edit a release before verifying it. For development, use a
separate editable copy and follow the [Hub publishing sequence](https://github.com/OctoSense-org/OctoSense-App-Hub/blob/main/docs/PUBLISHING.md):
restamp changed bytes, check the unsigned copy, then sign with your own publisher
key and verify again. `--allow-unsigned` only permits genuinely unsigned local
bundles; it does not trust an unknown signature or bypass installation checks.
Only `bundle/` is submitted. [Review answers](review/ANSWERS.md)
cover all eight scanner questions. Runtime-dependent reproduction commands stay
in the [original acceptance document](https://github.com/OctoSense-org/OctoScript-App-Design-Flow/blob/5b0fde7ed0e9e4131751d16f55ba3d8a3180dd95/examples/connected-apps/google-calendar/ACCEPTANCE.md).

Read the [privacy policy](PRIVACY.md) before connecting an account or using AI.
Report problems through [GitHub issues](https://github.com/ymote/octosense-google-calendar/issues)
without account data, tokens or private event details. Licensed under
[Apache-2.0](LICENSE); see [NOTICE](NOTICE) for attribution.

The [post-admission catalog receipt](review/CATALOG-0.1.1.json) verifies the default
public catalog, signed pack and listing assets. This adds publication evidence,
not new native, model or live-provider acceptance. The tagged release record
remains the historical record from signing time.
