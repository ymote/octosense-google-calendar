# Working on this app

This repository contains the standalone `io.github.ymote.googlecalendar`
App Hub preview. Read README.md, PRIVACY.md and review/ANSWERS.md first.

- Only `bundle/` is submitted. Preserve the ordinary app ID; do not use an `os.` identity.
- Credentials, OAuth registrations, user profiles, local state and raw test logs
  must remain outside version control. Use synthetic events in public evidence.
- Calendar writes must use the host's exact-content review. Do not add an agent
  mutation tool, approval bypass or direct network grant to this preview.
- `bundle/AGENT.md` is the shipped assistant instruction file. This AGENTS.md
  governs repository maintenance and is not part of the assistant's runtime input.
- Re-run `hub stamp`, `hub check` and `hub scan` after bundle changes; the GitHub workflow seals only the reviewed final bytes. No publisher signing key is needed.
- Keep old acceptance receipts immutable. New tests need new source/binary hashes
  and original captures; synthetic-provider tests do not establish live Google support.
- Update English and Chinese product/privacy docs together. Keep macOS-only
  development-preview limitations visible until supported by actual evidence.

- GitHub publishing uses `.github/workflows/publish-app.yml`, generated from
  merged App Design Flow. Push a new `v<manifest.version>` tag only after
  native checks and authorized review. Do not retag or adopt the old legacy ID.
- The old `org.octosense.samples.*` apps and their signed releases are historical.
  The fresh ID has separate storage/account grants and no automatic data migration.
