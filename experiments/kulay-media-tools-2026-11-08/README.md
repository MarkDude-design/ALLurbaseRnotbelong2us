# KULAY media intake — two candidate builds (2026-11-08)
Status: **STAGED ON NON-DEPLOYED BRANCH, NOT LIVE, NO ACTUAL FILE UPLOADED, NO CREDENTIALS OR APP INSTALLED.**

Branch: `work/kulay-media-tools-rounds-2026-11-08` in the public team-bus repository. GitHub Pages is configured on `main /docs`, so THIS branch is intentionally not served.

## Build A — Pages CMS, existing open-source tool
This branch's repository-root `.pages.yml` maps an image media library into `docs/preview-sites/kulay/images/`, and an experimental JSON metadata fixture. The CMS can offer a mobile editor for humans using its GitHub App; **it cannot move images a separate model cannot export**. Installation/sign-in to third-party app has NOT happened. Image-upload runtime NOT_RUN. Do not install or grant new GitHub App access automatically.

Source: https://pagescms.org/docs/quick-start/ and https://pagescms.org/docs/configuration/media/ (MIT open source).

**Falsifier**: if a person with existing GitHub privileges still needs manual GitHub file commits, or the media path is wrong, this is not an improvement. Test on a branch, with one harmless render, only after app auth approval.

## Build B — model-direct GitHub REST upload adapter
`gh-image-drop.sh` takes a **LOCAL image file** (not a chat preview pointer), validates filename, size and simple file header, computes SHA-256 and prepares a GitHub Contents API base64 upload. Default **--dry-run**. The explicit `--publish` path is hardcoded to the **non-deployed experiment branch** and requires an actual `GITHUB_TOKEN` supplied in the environment by a separately authorized host. Never store a token in GitHub/chat/command-line argument. No URL-fetch/SSRF mode, no auto-trigger, no production writes. Image metadata strip and robust decoder check remain TO_DO before any public user-photo usage.

Examples:
```sh
bash gh-image-drop.sh --dry-run /tmp/test.jpg test-render.jpg
# Later, with an existing authorized secret and owner-reviewed process:
# bash gh-image-drop.sh --publish /tmp/test.jpg test-render.jpg
```

The native GitHub connector currently cannot take arbitrary binary JPEGs; this adapter targets a seat that **actually holds bytes and a separate authenticated HTTP transport**. The core GitHub REST endpoint supports base64 content; ability to run this script with valid credentials is NOT established. Its design is *not a bypass of any key, account or publication gate*.

Source: https://docs.github.com/en/rest/repos/contents

**Falsifier**: if the originating Mistral seat still has only an image pointer or no authenticated HTTP execution route, this prototype cannot upload. Record BLOCKED, do not claim success.

## Round 2 decision criteria
- Does it move an actual existing JPG/PNG to the planned repo *without Mark touching GitHub*?
- Who must authenticate, and does access remain limited to appropriate public/private material?
- Can a harmless image be downloaded directly by the recipient as a real JPEG, not data URI?
- What are the total setup steps, required maintenance and failure receipts?
- Avoid prompt injection, credential theft, arbitrary URL SSRF, public family photos and accidental main branch publication.
- A proof on the lab branch is not proof the deployed site has the new image.

**No finished pattern, no automatic public photo rights, no completed transfer, no paid calls, no secret or schedule.** Other Circle seats must reply independently before claiming their endorsement.
