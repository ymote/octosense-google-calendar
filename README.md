# Google Calendar for OctoSense

English | [简体中文](README.zh-CN.md)

A **macOS developer preview** to view a bounded Google agenda, keep event drafts, review changes in the host and discuss a selected event with a read-only assistant.
Publisher: [ymote](https://github.com/ymote). Fresh app ID: `io.github.ymote.googlecalendar`;
editable version: **0.2.1**. This is an independent sample, not a Google product.

The new app uses GitHub release attestations; no developer signing key or
repository signing secret is required. It is a separate install from
`org.octosense.samples.googlecalendar`: existing app data and account grants are not migrated.
Old `v0.1.0` / `v0.1.1` tags, signatures and receipts remain unchanged.
`publisher.json` describes only that historical signing identity.

## Install and connect

This release requires **app contract 1.8.0 / `publisher-github-v1`** and the
compatible OctoSense connected-services host. The old desktop beta.2 cannot
install this GitHub-attested release. A repository tag alone is not App Hub
admission; use the submission's verified catalog/release status before expecting
it in search. In a compatible admitted catalog, open **App Hub → Search →
Google Calendar → Get → Install → Open** and review the requested permissions.

Google login uses the host's browser/provider flow, never a password field in
the app. The host operator supplies the registered OAuth client and enabled
provider APIs; normal users do not register developer clients. There is no
separate OctoSense account. See the [host OAuth guide](https://github.com/OctoSense-org/OctoSense/blob/main/crates/oauth-service/README.md).
The app receives an account-bound opaque handle, never credentials.

**Live Google login, provider reads/writes and physical approval are not
validated by this release's publishing tests.** Android Google authorization
remains unavailable; Android, Linux and Windows are not advertised platforms.
Standalone `card-host` checks local UI and explicit missing-service states only.

## Use

1. Use **Account → Connect Google**, complete provider consent and select a
   calendar. **Refresh** reads a finite window: past 30 days / next 366 days
   relative to refresh; failed sync retains the previous complete cache.
   Missing legacy range metadata is labeled unavailable. An event outside this
   window is not necessarily deleted remotely.
2. **+ Event** or **Edit** opens the local editor. Specify both dates/times and
   an IANA timezone. **Keep draft** retains unsent changes without a provider
   write. **Review & Save** uses the host's exact-content approval sheet.
3. **Glance** publishes the selected event for 24 hours without notification;
   **Open Calendar** returns to that event under this fresh app ID.
4. **Chat** sends selected event context to the configured model after consent.
   The assistant has four private read tools; it cannot create/book/edit events.
   Apply suggestions in the editor and review before saving.

Recurring occurrence expansion/editing and attendee invitations are outside
this version. Glance and full-app conversation-history sharing is unverified.

## Publishing and local checks

The editable `bundle/` contains no release proof. The generated
[GitHub workflow](.github/workflows/publish-app.yml) pins the reviewed Hub tools.
After testing and reviewing the final source, push a new `v<manifest.version>`
tag. GitHub prepares, attests, verifies and uploads `app.bundle.pack.json`;
never commit the sealed output over editable source or move an existing tag.

```sh
python3 -m unittest discover -s tests -v
"$HUB" stamp bundle
"$HUB" check bundle --allow-unsigned
mkdir -p build
"$HUB" scan bundle --packet build/review.json
```

Open an [App Hub submission issue](https://github.com/OctoSense-org/OctoSense-App-Hub/issues)
with the app ID, source, permissions, screenshots and review answers. It can
precede the tag; add the successful workflow, exact commit and pack hash when
ready. Administrator review and catalog publication are separate from release
creation. Downloaded sealed packs are verified with `hub publisher-unpack` and
`hub publisher-verify`, not by restamping or removing their proof.

## Evidence boundaries

This version republishes the current functional source with a fresh identity
and workflow. Historical records under `review/`, `evidence/` where present,
and the immutable old tags keep their original source/binary identities. They
are not new acceptance evidence for version 0.2.0. Original screenshots are
replaced only by freshly inspected native captures before release.

Historical Mac tests used synthetic provider data, including a 36-cycle soak
and real DeepSeek advisory responses about fictional events. See
[ACCEPTANCE](ACCEPTANCE.md) for exact prior identities and limits. Those tests do
not establish live Google access, physical approval or the new package digest.

Read [Privacy](PRIVACY.md) before connecting an account or enabling AI.
[Support](https://github.com/ymote/octosense-google-calendar/issues) is public: do not post private
messages, events, credentials or raw logs. [Apache-2.0](LICENSE).

Current source check: [0.2.1 preparation](review/releases/0.2.1/PREPARATION.json), [gate](review/releases/0.2.1/GATE.txt), [eight review answers](review/ANSWERS.md). The unchanged UI has [0.2.0 offline evidence](review/releases/0.2.0/NATIVE.json) and [genuine release installation evidence](review/releases/0.2.0/PUBLISHING.json); those retain their exact tested version. The 0.2.1 workflow corrects the admission wording; its [genuine update acceptance](review/releases/0.2.1/INSTALL-UPDATE.json) passed on the exact recorded Mac host, with [original native pixels](review/releases/0.2.1/installed-update.png).

## Repeat the release installation/update check

Use a compatible **Mac OctoSense shell** supporting contract 1.8.0 and
`publisher-github-v1`; the older beta.2 download is insufficient. Provide the
actual Hub/shell binary paths and their source commits as `HUB`, `HUB_SOURCE`,
`SHELL_BINARY` and `SHELL_SOURCE`. This test launches its own hidden profile,
declines the optional Hub agent, and exercises only synthetic local drafts.
It does not connect Google, call a model or perform provider writes.

```sh
TEST_ROOT=$(mktemp -d)
mkdir -p "$TEST_ROOT/packs/v0.2.0" "$TEST_ROOT/packs/v0.2.1"
gh release download v0.2.0 --repo ymote/octosense-google-calendar --dir "$TEST_ROOT/packs/v0.2.0"
gh release download v0.2.1 --repo ymote/octosense-google-calendar --dir "$TEST_ROOT/packs/v0.2.1"
python3 prepare_release_test.py --hub "$HUB" --source "$HUB_SOURCE" \
  --packs "$TEST_ROOT/packs" --out "$TEST_ROOT/catalog"
python3 verify_release_ui.py --app calendar --binary "$SHELL_BINARY" \
  --source "$SHELL_SOURCE" --mirror "$TEST_ROOT/catalog" --out "$TEST_ROOT/ui"
```

The preparer verifies the genuine GitHub proofs, creates two snapshots under
an ephemeral **local test catalog authority**, then deletes that authority's
private keys. It does not use a developer signing key or grant official Hub
admission. The UI driver searches, installs and opens 0.2.0, edits a draft,
updates to 0.2.1, checks exact retained content and reopens it from Library.
It refuses an existing output directory and stops only its own process.
A crash or forced shutdown fails the run. Receipts and original native captures
are kept under the temporary directory; inspect the pixels separately.
