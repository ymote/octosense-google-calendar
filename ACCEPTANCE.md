# Evidence provenance

This repository preserves the functional bundle and original public synthetic
evidence from [App Design Flow 5b0fde7ed0e9e4131751d16f55ba3d8a3180dd95](https://github.com/OctoSense-org/OctoScript-App-Design-Flow/tree/5b0fde7ed0e9e4131751d16f55ba3d8a3180dd95/examples/connected-apps/google-calendar).
Read its [full acceptance record and reproduction commands](https://github.com/OctoSense-org/OctoScript-App-Design-Flow/blob/5b0fde7ed0e9e4131751d16f55ba3d8a3180dd95/examples/connected-apps/google-calendar/ACCEPTANCE.md),
with the companion [OctoSense source snapshot 26b9fe9fa51ef3c1fe6f833743144a2e12cf54e3](https://github.com/OctoSense-org/OctoSense/tree/26b9fe9fa51ef3c1fe6f833743144a2e12cf54e3).
Individual historical receipts retain the executable hashes actually used;
the companion snapshot does not relabel those builds as a later run.

`bundle/main.splash` SHA-256 remains
`7292894f1576d2283726eeafdb79742bd6fe6fb9a651cb1646462bbde4185ff0`.
[review/source-provenance.json](review/source-provenance.json) records the original
hash of every copied file. Only listing metadata and its restamped manifest
integrity change in the publisher bundle; executable source, tools, agent
instructions, SVG and screenshot bytes are unchanged. Historical receipts in
[evidence/](evidence/) retain their original bundle digest. They do not certify
the new publisher identity, signature, listing or public catalog admission.

| Historical check | Result and boundary |
| --- | --- |
| Native local UI | Five journeys; missing-service errors, draft editing and restart |
| Signed installed app | Eight cases using synthetic Google transport/vault: immutable review/cancel, create/readback, ETag edit/conflict, cached agenda and draft restart |
| Full shell Glance | Six cases: explicit publication, warm/cold exact-event route and durable restoration |
| Actual DeepSeek v4 Flash | Seven shell cases including a private read tool and advisory answer about a synthetic event; zero Calendar writes |
| Native macOS soak | 36 cycles/620.010 seconds; three saves/readbacks, three refused conflicts and four restarts |

Original listing screenshots show local synthetic drafts, standalone host-service
unavailability and an embedded L0 template. They are not live Google screenshots.
The original captures in `evidence/` also use fictional event/account data.

Open acceptance: live Google OAuth/read/create/edit/revocation, physical host
approval, Glance-card chat/shared app history, expanded-card workspace, Android,
Linux and Windows. Soak RSS rose within each process; the historical test is not
a leak-free or steady-state memory claim. Runtime dependencies remain
[OctoSense #347](https://github.com/OctoSense-org/OctoSense/pull/347) and
[App Hub #119](https://github.com/OctoSense-org/OctoSense-App-Hub/pull/119).

中文说明：以上为固定版本的历史验证，不是新发布者版本的重新实测。
代码、工具、代理指令和原始截图字节未改变；发布者资料及相应包摘要已更新。
模拟日历服务验证、真实模型对模拟数据的回答，均不代表真实 Google 授权或读写已通过。
