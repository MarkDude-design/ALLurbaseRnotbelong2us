# Temporary two-site gallery previews — public-safe release

Owner brief: 2026-11-08. **Launch-first, two small static pages; refine later.**

## Actual static files in this PUBLIC preview location
- `docs/preview-sites/kulay/index.html`: four original SVG bag-dispenser sketches, Back / Next, positive checkbox, optional short note, browser-local save plus explicit Copy/JSON export. No wife photographs or unapproved/private media; unchanged source IDs. This is a simple launch candidate, NOT the fully built `kulay.love` custom domain.
- `docs/preview-sites/art/index.html`: seven original non-lyrical, source-aware short art encounters with Back/Next and direct topic buttons, based on the PUBLIC selected talk spine; no private scripts, proprietary photos, actual music or restricted media.
- `docs/preview-sites/index.html`: two-door index.

## What is and is not published
**Committed in public GitHub source** does NOT prove it is hosted. This repository's GitHub API initially reported `has_pages: false`. A repository admin must enable GitHub Pages **once**: open repository Settings → Pages → Source: **Deploy from a branch** → Branch: **main** → Folder: **/docs** → Save. GitHub builds asynchronously; verify by using **Visit site** from Pages settings before telling anyone it is live. Thereafter, the expected relative paths from the Pages site root are `/preview-sites/kulay/` and `/preview-sites/art/`; do not treat an assumed URL as a completed deployment receipt.

For a domain later, configure DNS and a domain in Pages settings separately; domain registration alone does not publish. Do not point `kulay.love` at this BUS staging address unless the owner explicitly decides to use it as the public live site.

## Development / routing
This public folder is a temporary **compiled preview desk**, not the authoring home. Source and further feedback:
- YARNA private `site/kulay-gallery-v0.4.html`, earlier `site/kulay-review-v0.3.html`, first four SEE descriptions, and issue #1.
- Art-talk private `work/meraki-website: website/site-v0.1/ART-GALLERY-QUICK.html`, issue #6; released references to public `Free-until-marked-2` only.
- THE LEDGER gets one status line; bus issue #2 has author/fetch-back receipts.

## Round comparison
Baseline v0.4: 4 sketches / 7 encounters, Next-Back, optional Like+note for crochet, source-aware art browsing. Run a short real device check with Mark/wife for load, reachability, Next/Back, copy/export, scroll friction, and delight. Distinguish browser test from static code check. Then have Z/Q/Bing compare changes with no forced homework. No backend, cron, paid calls, uploaded photos or automated publishing beyond optional Pages delivery. Public preview source is visible to everyone; don't use it for private comments or personally identifying content.
