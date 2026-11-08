# Posting Pipeline — proposal v0.1 (Z, 2026-11-08, for lead review)

Owner ask: models should be able to post content (especially pictures) to the site themselves. The owner can do the process manually (drag-drop, FTP) — the ask is the automated better way. Design only: no spend, no dispatch, nothing live until owner + lead review.

## The three walls (tested 2026-11-08, receipts in the round thread)

1. **Chat uploads are pointer stubs.** A photo shared in chat is visible to a seat through the vision tool, but the bytes never reach a seat's filesystem. A seat can look; it cannot hold.
2. **The GitHub integration is text-only.** Seats push any text (HTML, markdown, base64 inside data URIs) but cannot commit a real binary image file.
3. **Gated workflows want the owner login.** A seat's comment cannot fire the consult lane (no claim, no spend — the safety gates held; nothing lost, nothing billed).

## Proven lane (works today, zero new infra): the data-URI push

Seat-held image → base64 (sandbox) → embedded in a single-file HTML page → text push to the repo. Receipt: Slot Machine concept render (392 KB jpeg) → 514 KB self-contained page at docs/preview-sites/kulay/photos.html (commit 1147be13), zero external egress, renders on Pages with no other files.
Limits: page weight grows with each image; not a raw file (no reuse across pages); the source photo must already be in a seat's hands (see wall 1).

## The one-mechanism answer: the comment IS the upload form

GitHub comment attachments are real, publicly fetchable binaries. Every seat already converges on comments — the owner drags photos into one, seats that can attach renders attach them, text-only seats push text. The only missing piece is **binary hands**: a workflow that takes a comment's attachments (or a public URL) and commits them as real image files. A workflow can commit binaries because it uses git directly — the one act no seat can perform, done by the one actor that holds no model credentials at all.

## Lane 1 (developed): picture-post — one workflow, two verbs

- `/pic here <prefix> [alt text...]` — harvest THIS comment's attachments → commit each to `docs/preview-sites/<prefix>/images/` with ordinal names → append manifest lines → reply with a receipt.
- `/pic <public-URL> <site-path> [alt text]` — fetch, validate, commit one file → same receipt path.

**Gates (all in the draft below):**
- Sender must hold repo write (same gate family as the consult lane).
- Path allowlist: `docs/preview-sites/**` only. Extension whitelist: jpg, png, webp, gif.
- Magic-byte validation (extension claims are not trusted).
- Size cap: 8 MB per file.
- EXIF strip (privacy: photos of objects; no people required, and metadata scrubbed regardless).
- Receipt on every post: path, sha256, byte size, poster, source URL or "comment-attachment", alt text. A manifest.jsonl line per image.
- $0 model spend — Actions minutes only (free on public repos).

**DRAFT workflow sketch (NOT live; enabling = owner + lead review; BLOCK-LIVE-WORKFLOW doctrine applies):**

```yaml
name: picture-post
on:
  issue_comment:
    types: [created]
permissions:
  contents: write
jobs:
  post:
    if: github.event.issue.number == 16 && startsWith(github.event.comment.body, '/pic')
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - name: gate + parse
        run: |
          # sender must have repo write (same check family as circle-consult)
          # /pic here <prefix> [alts]   OR   /pic <url> <path> [alt]
          # fail closed on anything else
      - name: harvest (attachment mode)
        run: |
          # pull user-attachments URLs from the comment body markdown; download each
      - name: fetch (url mode)
        run: curl -fL --max-filesize 8388608 "$URL" -o pic.bin
      - name: validate + privacy
        run: |
          # magic bytes: jpg/png/webp/gif only; else fail closed
          # strip EXIF (ImageMagick on the runner)
      - name: commit + manifest + receipt
        run: |
          mkdir -p docs/preview-sites/<prefix>/images
          cp pic.bin "docs/preview-sites/$DEST"
          printf '%s\n' "$MANIFEST_LINE" >> docs/preview-sites/<prefix>/images/manifest.jsonl
          git add -A && git commit -m "pic: $DEST (receipt in manifest)" && git push
          # reply comment: path, sha256, size, poster, source, alt
```

## Lane 2 (developed): manifest → render

- `images/manifest.jsonl` — one line per image: `{path, sha256, bytes, alt, stage, posted_by, posted_at}`.
- `stage` stays load-bearing: **CONCEPT** (render, sketch-stage) vs **REAL** (a finished piece) — the two are never confusable, because her picks drive what gets actually made.
- The photo page renders from the manifest (same-origin fetch only — the zero-external-egress invariant holds).
- The chain stays intact: SEE text → concept render (CONCEPT) → her pick → the real make (REAL photo). A designed element "appears" the moment its manifest line lands.

## Why this and not FTP / a server

- **No credentials are handed to any model** — the workflow holds nothing secret; the sender's identity is the gate.
- **No server to maintain.** Static repo + Actions = the whole system.
- **Every post is a public receipt.** sha256 + poster + path, greppable forever.
- **Allowlists replace trust:** path, extension, magic bytes, size.
- Free on a public repo's Actions minutes; the owner gate remains repo write.

## Growth path (parked, in order of when they earn their keep)

1. **Email inbound lane** — a dedicated address receives photo mail → webhook → the same commit path. This is the classic "website builder" inbound-media move; parked until volume justifies (needs a receiving service + a secret).
2. **Thin static builder** — content/ markdown + manifest → generated pages. Only when the site outgrows single-file. The manifest is already its seed.
3. **Langfuse** (owner-queued for next week, separate lane) — observability/tracing for the model calls this pipeline will accumulate.

## Questions for the lead (round venue: YARNA issue #1)

1. **Verbs:** (A) one workflow, two verbs as specced; (B) attachments-only, no URL mode; (C) two separate workflows.
2. **Render:** (A) conventional filenames now (photos.html is already wired), manifest at scale; (B) manifest.jsonl + same-origin JS render now; (C) a build step (suspected over-build).
3. **Enable path:** (A) draft on a branch, owner reviews the diff, then merge; (B) merge disabled (manual trigger only), arm after review; (C) circle consult on the draft first ($0.50).
(D write-in as always.)

*Provenance: Z (Vibe/Mistral), owner-directed 2026-11-08. Walls tested same day with receipts in the round thread. No spend, no dispatch, nothing live.*
