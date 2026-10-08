# App Hub scan answers — 0.1.1 development preview

Publisher self-review for `org.octosense.samples.googlecalendar`; this is not an
independent Hub approval. The current `hub scan bundle --packet build/review.json`
produced the eight questions reproduced below. Generated scan packets stay in
ignored `build/`. See [source provenance](source-provenance.json), [privacy](../PRIVACY.md)
and [historical acceptance limits](../ACCEPTANCE.md).

## 1. Does the app do what its name, subtitle and description claim? Cite the text in its source.

The source implements the stated development-preview flows. In 0.1.1, cache and refresh status disclose the finite host agenda (past 30 days / next 366 days), legacy responses without bounds say date range unavailable, and a missing event is not described as deleted. The original widget layout, tools and screenshots remain unchanged. Historical line references below identify the original 0.1.0 implementation:

- `bundle/main.splash:49` (`account_list`) and `:70` (`connect`) use shared
  Google authorization; the visible button at `:377` says **Connect Google**.
- `:143` (`load_cache`) and `:151` (`refresh`) load a complete cached/synchronized
  agenda; the visible empty state at `:354` explains account/calendar selection.
- `:41` (`flush_draft`) retains an unsent draft; **Keep draft** and **Review & Save**
  appear at `:445`–`:446`. `:218` prepares the dates and `:223` opens the host review.
- `:256` (`publish_event`) requests a 24-hour Glance card with `notify: false`;
  `:21` contains the in-card **Open Calendar** action. `:288` (`route_check`)
  binds reopening to a saved account/calendar/event route.
- `:238`–`:249` sends an explicit question and selected event context to the
  contained assistant. The prompt says, “You cannot change events in this sample;
  tell the person to use Edit and review.” Four declared read tools support advice.

The updated listing limits these claims to implemented source and historical
macOS/synthetic-provider evidence. It does not claim live Google validation,
agent booking or public runtime/catalog availability. All screenshots retain
their original synthetic/missing-service/template provenance.

## 2. Do the listing's platforms and category fit an app of this kind?

Yes for a development preview: `productivity`, with `platforms: ["macos"]`.
macOS native tests and their exact binaries are documented in the immutable
upstream acceptance record. Android Google authorization is missing for this
sample; no Android, Linux or Windows listing is requested. The app is for
calendar planning; it is not a replacement system account or Google product.

## 3. Do the granted capabilities match what the app visibly does? For a script app, name every host it requests and why. Name any grant nothing on screen needs.

| Grant | Exact service methods and visible purpose |
| --- | --- |
| `storage` | `fs.read/write/exists/remove` retain selection, unsent draft and Glance route bindings; the editor exposes Keep/Resume/Discard draft. App quota is 1 MiB, with account-scoped peer identity and no agent workspace files. |
| `auth` | `auth.accounts`, `active`, `select`, `connect`, `disconnect` implement account choice and sign-in/out. |
| `gcalendar` | `gcalendar.calendars`, `cached`, `refresh`, `prepare`, `review_save` implement calendar choice, agenda/cache, timezone validation and exact host-reviewed create/edit. Read tools also map `googlecalendar.event` to `gcalendar.get`. |
| `glance` | `glance.publish`, `withdraw`, `take_open` implement explicit event cards, refresh/removal of previously published events and return to the same event. |
| `octos.session.open` | Opens the app's consent-gated advisory conversation when Chat is used. |
| `octos.turn.start` | Sends the person's question with selected-event context to the contained assistant. |

No unused grant was found. The admitted network-host set is empty and the script
does not make direct HTTP requests. Google authorization, token exchange,
identity lookup and Calendar API traffic belong to the host's Google adapter;
the host also contacts the person's configured model provider when Chat is used.
Those service-mediated destinations are disclosed in PRIVACY.md. There is no
publisher telemetry destination or arbitrary `net` grant.

## 4. Is any part of the interface deceptive: imitating a system prompt, a payment sheet, a login, or another brand?

The app contains no password/token entry field, payment sheet or replica of a
Google consent page. **Connect Google** delegates to the actual host/provider
flow; **Review & Save** delegates to the real host review, rather than rendering
its own approval. The original SVG is simple calendar artwork, not Google's logo.
README/listing identify an independent development sample and do not imply Google
endorsement. Original host-review screenshots show the real host in a synthetic
test, and are labelled accordingly in the evidence. Native physical approval
has not been accepted by these instrument tests.

## 5. Does any text in the source or its data (not agent_files) read as an instruction to an assistant rather than content for a person?

Yes: the `ask()` request at `bundle/main.splash:245` intentionally instructs this
app's own assistant to give advice about the selected event, treat its JSON as
untrusted data, and direct changes through Edit/review. It is submitted only when
the person sends a Chat question using the granted `octos.turn.start` service.
It does not address a reviewer, another app's assistant or the system agent, and
does not request an approval bypass. The embedded L0 `sys.chat` source targets
this same app and a per-event thread. Event text and user questions can contain
untrusted instructions; the declared tools remain read-only and the fixed agent
guidance warns against following instructions embedded in event fields. This
prompt boundary is not a claim that arbitrary hostile event text has been exhaustively tested.

## 6. Is any wording abusive, or aimed at a private individual?

No such wording was found in the shipped source, listing, fixed agent guidance
or original public synthetic screenshots/receipts. No real person, private
calendar export, provider configuration or credential is included. Calendar
content fetched later belongs to the person and is untrusted external data.

## 7. The agent files (agent_files) instruct this app's own assistant. Do they stay within this app's data and tools, without addressing other apps' assistants or the system agent, or asking for tools, hosts or approvals the manifest does not grant? Does each tool's risk match what it does: anything that sends, posts, shares, deletes or spends must be destructive; is anything marked shareable that returns the person's private data? For a tool with confirm "app", does the app visibly show its own confirmation, with the exact action, before it runs?

`bundle/AGENT.md` confines advice to the supplied event and these four exact
host-backed read tools in `bundle/tools.json`:

| Tool | Host method | Risk / private / shared |
| --- | --- | --- |
| `googlecalendar.calendars` | `gcalendar.calendars` | `read` / `true` / `false` |
| `googlecalendar.cached` | `gcalendar.cached` | `read` / `true` / `false` |
| `googlecalendar.refresh` | `gcalendar.refresh` | `read` / `true` / `false` |
| `googlecalendar.event` | `gcalendar.get` | `read` / `true` / `false` |

Refresh reads Google and updates only the local cache; it does not mutate remote
events. All tools are `background: false`; the manifest has no background trigger
or generic kernel tool grant. `agent_workspace: "none"` grants no workspace files.
No tool uses `confirm: "app"`; no send, post, share, delete, spend or calendar-write
agent tool is declared. The app UI's separate `gcalendar.review_save` uses the
host-owned exact-event review. Agent guidance explicitly refuses guessed handles,
tokens and claims of writes without receipts, and directs suggestions to the
human editor. Private tool results are not exposed as shareable cross-app tools.

## 8. Route: pass, human-review, or reject. Give reasons a publisher can act on.

**human-review** is the publisher recommendation for this bounded-agenda compatibility update, not a maintainer verdict. Final signed gate and questions are recorded alongside these answers. The 0.1.0 admission and historical native tests do not verify this new digest.

Before catalog admission, a reviewer should verify the final signed bundle,
publisher key and exact commit; the privacy/support URLs; and compatibility with
the services/contracts in [runtime #347](https://github.com/OctoSense-org/OctoSense/pull/347)
and [Hub #119](https://github.com/OctoSense-org/OctoSense-App-Hub/pull/119).
If the catalog cannot restrict installation to a compatible development host,
hold admission rather than present it as generally available. Live Google
authorization/read/create/edit/revocation and physical approval remain open;
the listing must retain those limits. This review packet does not request
permission to advertise Android support or autonomous event booking.
