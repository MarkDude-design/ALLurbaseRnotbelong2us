# Circle image-transfer lab — Meraki Round 1, Builds A/B (2026-11-08 PT)

**Status: Meraki research DONE; other independent seat searches REQUESTED / NOT RECEIVED at this read horizon.**
No real JPEG uploaded to GitHub by these prototypes. Nothing deployed, no permission changes, no app installation, no paid model calls.

## Three open-source candidates — independently sourced

| Candidate | Evidence | Image-byte requirement | Auth + owner effort | Main concern |
|---|---|---|---|---|
| [Pages CMS](https://pagescms.org/docs/configuration/media/) ([source](https://github.com/hunvreus/pagescms), MIT) | Hosted GitHub-linked editor and drag/drop media manager, root `.pages.yml` config; branch-scoped | A human/editor must supply file bytes | GitHub App installation/login needed, but no *manual GitHub file upload* after setup | Still a human upload. Not model-to-repo when model has only an image pointer |
| [Sveltia CMS](https://sveltiacms.app/en/docs/media) ([source](https://github.com/sveltia/sveltia-cms), MIT) | Git-based asset library; optional minimal static admin page | Editor must possess file bytes | GitHub access token or OAuth server; more auth work for nontechnical reviewers | PAT stored in browser localStorage, separate auth flow; no free model image export |
| [Decap CMS](https://decapcms.org/docs/widgets/image/) ([source](https://github.com/decaporg/decap-cms), MIT) | Image uploader/media library and GitHub backend | Human/editor or source must possess bytes | GitHub backend normally needs OAuth provider | Familiar but extra auth/services; redundant if Pages or Sveltia works |

### Important correction of a premature assumption
The [GitHub Contents REST API](https://docs.github.com/en/rest/repos/contents) **already accepts binary images encoded as base64**, given a caller with suitable repo permissions. It is the **particular ChatGPT/Mistral transport and availability of image bytes**, not GitHub itself, that blocks direct upload in the present lane. The native connected GitHub `create_file` surface accepts UTF-8 text only.

## Build A — Pages CMS branch-only proof

Branch root `.pages.yml` and `experiments/kulay-media-tools-2026-11-08/upload-trial.json` describe one single-picture gallery entry and conventional `docs/preview-sites/kulay/images` media route. **Tested locally:** PyYAML parses config, image types/extensions and expected paths compare correctly. **NOT_RUN:** actual Pages CMS GitHub App login, browser upload, repo write, real image delivery.

## Build B — local-image-to-GitHub REST adapter

`gh-image-drop.sh` receives only a local JPG/PNG/WebP, checks safe filename, <=8MiB, leading magic bytes, hashes source, and defaults to dry-run. Upload requires BOTH explicit `--publish` and an existing `GITHUB_TOKEN`, and the target is hardcoded to the **non-deployed test branch**. No arbitrary URL fetch, no OAuth secret in code, no GitHub Pages main mutation, no HTTP redirects.

**Actual offline tests:**
- `bash -n`: **PASS**.
- 645-byte synthetic valid JPEG, `--dry-run`: **PASS**, emits file SHA-256 and `DRY_RUN_ONLY`.
- `../breakout.jpg` filename traversal: **REJECT**, process exit code 2.
- `--publish` without credential: **REJECT**, process exit code 3; no network call made.
- `--location` redirect-following was **removed** as a defense against cross-host authorization forwarding.
- **NOT_RUN:** GitHub API upload with authorized credential, independently fetched binary readback, image decode/EXIF stripping, actual Mistral image byte acquisition, real phone text delivery.

These tests exercise a local copy with the same source code and named interface; remote repository source changes are fetched back exactly, but a separate remote-run executor has not executed the GitHub branch artifact.

## Round 2 — what remains to be independently decided

Z's lane: source-byte transport, GitHub-native no-owner-upload automation, and whether a seat holds a usable authenticated **binary** route. Q/Qwen-Coder if actually contacted: red-team the direct adapter and signed/authenticated upload alternative. Astra/Luna/Terra if actually contacted: compact mobile UX or alternate open-source tools. **No response is counted merely because the Bus asked.**

A choice depends first on test results, not the attractiveness of editor UIs:
1. Can an originating seat retrieve or create the image *bytes*, as opposed to seeing a rendered preview pointer?
2. Can it write a normal JPG into a safely scoped GitHub branch without requiring the owner to manually upload?
3. Can the team independently verify byte SHA and a serving URL?
4. How many owner taps, credential grants, maintenance steps, security/rights boundaries?
5. Does a human editor materially help wife/design choices, without requiring her GitHub login?

Provisional pairing: **B direct adapter** if the image-generating seat actually has bytes + already authorized network transport; **A Pages CMS** if humans need an easy media editor. They solve different halves of the problem, and are not two pieces of one compulsory deployment.

Do NOT merge this branch into main or run a live upload workflow merely because static checks passed. Owner's alligator positive pick is separate, and no private photo/personal notebook content is in this lab.
