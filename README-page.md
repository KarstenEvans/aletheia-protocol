# Animated Aletheia Protocol README page specification

[Aletheia Protocol](https://github.com/KarstenEvans/aletheia-protocol/blob/main/README.md) — authoritative source and provenance.
[Thalia Protocol](https://github.com/KarstenEvans/thalia-protocol/blob/main/THALIA_PROTOCOL.md) — optional humane humour.

**Status:** Source committed, live visual/audio testing pending. 1 October 2026.

- `README.md` remains authoritative. `README.htm` is a replaceable animated reader; it does not amend protocol normative material.
- The visual engine was **cloned** (not moved or overwritten) from `KarstenEvans/aletheia-app/aletheia-threejs-animation/aletheia-threejs-animation.htm`. Preserve its Spiral → AI → Aletheia stages, gold perspective crawl, WebGL2/WebGL1/Canvas2D fallback and reduced-motion support.
- The scrolling crawl is generated from the actual **current** `README.md` text at build time. A subsequent README.md edit requires refreshing the rendition. Do not claim live automatic syncing.
- Opening page displays an explicit `Start reading` button, because browser narration requires a user gesture. Start crawl and queue speech after a user-requested three-second delay.
- Narrator voice selection prefers an available voice named **Caroline**, then Australian English (`en-AU`) fallback. Exact voice availability is device/browser-specific; do not download or impersonate voices.
- Keep on-screen pause/restart and voice controls, direct visible link to README.md, and avoid progress counts that are not actionable.
- Audio chunking is used to prevent giant utterances and to allow stop/restart. Browser autoplay/voice selection can vary: test and provide a retry.
- The Three.js CDN and Google font are optional dependencies and must not prevent text crawl or visible fallback if unavailable.
- Validate source syntax, README content synchronization, user-gesture playback, three-second delay, UK/Australian voices, pause/restart, narrow mobile and reduced motion.
- Direct source: https://github.com/KarstenEvans/aletheia-protocol/blob/main/README.htm
- Proposed published URL (unverified): https://karstenevans.github.io/aletheia-protocol/README.htm
