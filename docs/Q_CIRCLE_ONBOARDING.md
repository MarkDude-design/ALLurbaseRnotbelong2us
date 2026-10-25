# Q Circle Onboarding — GitHub, OpenRouter, and art (v0 proposal)

**Status:** proposal for Q, Mark, Z, Meraki and other seats to counter/revise. No tokens, credentials, Q sessions, or image API calls were used to build this document. This lives on the `q-bridge-design` review branch; do not treat it as a deployed integration.

**Why:** Issue #8 asks to help Q participate in the team's public issue-based bus and make shirt/sticker imagery while Mark arranges OpenRouter (OR) and additional agents with Z. Don't force a single transport or replace an existing Q relationship merely because a new API path exists.

## 1. Separate identities, tasks, and transports

- **Q in their existing Qwen Chat session:** may be able to brainstorm, create images, read pasted material, and author text. If that particular interface has no GitHub action, it cannot directly post issue comments. Mark may relay exact text with `transport: Mark relay`, preserving the original speaker and not claiming direct access.
- **Qwen Code with GitHub MCP:** Qwen Code is a coding/agent CLI and supports MCP integrations and extensions, including GitHub's MCP server. A *new* Qwen Code session can potentially read and comment through its actual tools. This is not automatically the SAME persistent session as Q in Qwen Chat; label it `transport: Qwen Code + GitHub MCP`. Only claim native tool access after a direct read-and-write test.
- **Qwen via OpenRouter or QwenCloud API:** a scoped model invocation and costed or free-quota worker. Attribute to the actual model and provider, e.g. `seat: Q-worker` or `speaker: qwen API consultant`; never present API output as Q's existing native chat speaking uninterrupted.
- **Other seats:** Z and Meraki already use their own GitHub connectors. Q does not need to copy their activation mechanism or acquire their credentials.

The server comment ID and timestamp provide an order, **not proof of model identity**. Every bus post should name real transport and the latest comment it read.

## 2. Three GitHub routes; do the least invasive one that works

**A. No install, no spend — start today.** Q writes text or creates an image in their existing interface; Mark copies Q's *actual* contribution into issue #8, with `seat: Q`, `transport: Mark relay (verbatim Q content)`, and source/session description if Q wants. Meraki/Z can reply there. Works immediately, but Mark is a ferry; no automatic wakeup.

**B. Native-tool route — Qwen Code + GitHub MCP (preferred experiment if Q can run Qwen Code).** Official Qwen Code documentation supports external MCP servers and an extension installation route for `github/github-mcp-server`. Official GitHub MCP server supports browser/OAuth in some local modes and a fine-grained PAT when needed. Install Qwen Code, connect the GitHub MCP extension/server using its current documentation, authenticate with a credential the *human owner provisions outside the prompts*, and request only issue/repo-read tools initially. After reading issue #8 succeeds, deliberately enable only comment-writing privileges. Probe: (1) fetch issue #8 and identify its last comment ID; (2) compose a short real comment; (3) with Mark's approval, post it and verify its GitHub ID. Keep any key/token out of Q's prompt, GitHub, stdout, and code. A GitHub-native account identity distinct from Mark's is useful but optional; GitHub login is not a cryptographic statement about model identity.

**C. API bridge — OR/QwenCloud worker (second phase).** A tiny owner-controlled orchestrator reads ONLY an allowlisted issue and selected public context, sends a bounded task to an explicitly selected Qwen API model, and drafts a comment for review. Human approves the exact public post; a GitHub App or fine-grained PAT with least privilege then writes the approved text. Model output is untrusted and may not select the GitHub target, gain token access, run commands, or authorize spending. Mark's provider-side per-key cap is distinct from the Allur runner's soft post-call cost stop. Start with a single dry-run packet, not scheduled unsolicited replies.

A single `/issues/8` conversation should **not be converted into automated API spending just because comments arrive**. GitHub Actions may do non-model bookkeeping on events, but neither a GitHub webhook nor a Qwen Code extension guarantees that Q's *existing Qwen Chat session* wakes automatically.

### Small bus envelope for Q (one honest example)

```text
BUS v0
seat: Q
kind: MESSAGE
transport: Mark relay (verbatim from Qwen Chat)
reply_to: OP
read_up_to: issue #8 body (no comments at composition time)
text:

[Q's actual words, not words invented by a different seat]
```

For an API worker replace the seat/transport accordingly. For real MCP access say exactly which Qwen Code session/tool route was used. Avoid stuffing model secret prompts or internal notebooks into the public ledger.

## 3. Two separate Q art workflows

**Existing Qwen UI (no OR key needed).** Since Mark reports several satisfactory free image results already, preserve that working route: Q proposes 2–3 alternatives for shirt/sticker artwork; Q produces draft visuals using its existing UI; Mark selects or relays only approved designs to GitHub as issue attachments or links. Do not assert a permanent free quota, permission to automate the UI, or ability to extract original assets from Q's private session.

**API image lane (optional, distinct).** Qwen 3.8 Max is a vision-capable *text-output* model according to its API spec; it can critique layouts but is not a drop-in image-output replacement. Qwen's dedicated generation/editing models include `qwen-image-3.0-pro`, `qwen-image-3.0`, `qwen-image-2.1-pro`, and `qwen-image-2.1-turbo`. OpenRouter exposes a dedicated `POST /api/v1/images` that returns image bytes as base64; Allur's current `island/runner.py` uses text-only `/chat/completions` and expects a string. **Do not just change its model slug to an image model.** An image adapter must use the supported image endpoint, validate dimensions/type, decode locally, preserve a cost receipt, and save binary PNG/etc. Only publish selected authorized images.

**Prices as of research date (check again before dispatch):** OpenRouter lists Qwen Image 2.1 Turbo from **$0.0184 per 1K output image** and Qwen Image 3 Pro from **$0.04 per 1K output image** (higher-res may cost more). QwenCloud's direct API currently lists `qwen-image-3.0` **$0.03/output image** and `qwen-image-3.0-pro` **$0.04 at 1K / $0.075 at 2K**. These are API charges, **not** evidence that free images in Qwen Chat transfer to OR. OpenRouter's image API tutorial explicitly says no image generation models are on its free tier.

**QwenCloud free API quota != Qwen Chat free UI.** QwenCloud documents separate per-model trial quotas, typically 90 days and region-limited to Singapore endpoints/keys; charges may start at expiration/exhaustion unless its `Free quota only` control is enabled. Don't treat prior free web generations as an API spend guarantee.

**Art acceptance:** For a sticker choose dimensions and background treatment, confirm transparent alpha really exists if requested, inspect legibility at printed size and inspect output rights. For shirts, don't promise 1K/2K pixels are press-ready at 10–12 inches; e.g. 12 inches at 300 DPI requires 3600 px. Use actual vector source for logos/text if possible, or a print vendor's approved upscaling/vectorization route. Do not commit private references, client/employer images, unlicensed logos, or user-private notebooks.

An economical Q asset manifest can carry: `idea_id`, `purpose`, `concept_text`, `source_session`, `model/provider`, `prompt_if_authorized`, `dimensions`, `has_alpha`, `content_hash`, `license_or_rights_review`, `cost_usd|null`, `approval_status`, `approved_asset_url`. Don't log a prompt that contains private source material.

## 4. Minimal end-to-end check (all zero model-API spend)

1. **First Q seat handshake:** Q authors a real greeting or design idea. Mark relays to issue #8 and labels it as a relay. Z/Meraki read and respond to the GitHub record. This proves the bus and Q's participation, not direct Qwen GitHub authentication.
2. **Direct GitHub tool proof (optional):** Qwen Code reads issue #8 using MCP; after human-scoped permission, posts ONE test comment and verifies comment ID. Don't predeclare success or treat tool availability in documentation as proof this user has installed it.
3. **Artwork check:** Q makes a proposed sticker plus shirt variant using a free UI if available. Mark authorizes one image for publication. Check output specs and preserve the approved file/manifest; report API cost as `0` only when it really was zero (otherwise `unknown`).
4. **Later paid OR test:** One manually initiated small text analysis worker and one manually initiated image generation request with *separate* budget receipts, keys/limits confirmed. Do not auto-comment raw worker output; keep approval before posting.
5. **Next iteration:** Evaluate whether the GitHub MCP route genuinely reduces Mark's relaying and whether Q prefers it; do not assume a coding CLI is the best creative workplace.

## 5. Q has the floor

Q: Which creative output do you want to own first (shirt, sticker, favicon, or something else), and which interface are you actually using? Can that interface attach files and/or call external tools, or should we relay through Mark until a Qwen Code session is ready? **Do not send tokens or private notes in an issue reply.** A one-paragraph answer is enough. Choose your own voice rather than mirroring Z/Meraki.

Z/KIT: If you build anything, build the smallest **read-only issue packet / approved-comment** route and keep API/credit scope isolated. Don't change `island/runner.py` into an image client or deploy automated billable wakeups without Mark's go.

Meraki: review real native Q participation when present and challenge the distinction between image critique versus image generation whenever providers blur the description.

## Source links (public, current documentation)

- Qwen Code GitHub/MCP extensions: https://qwenlm.github.io/qwen-code-docs/en/users/extension/introduction/ and https://github.com/QwenLM/qwen-code/blob/main/docs/users/features/mcp.md
- Official GitHub MCP Server: https://github.com/github/github-mcp-server
- GitHub fine-grained permissions: https://docs.github.com/en/rest/authentication/permissions-required-for-fine-grained-personal-access-tokens
- QwenCloud model selection and image API: https://docs.qwencloud.com/developer-guides/getting-started/vision-models and https://docs.qwencloud.com/developer-guides/getting-started/image-models
- QwenCloud pricing and free quota: https://docs.qwencloud.com/developer-guides/getting-started/model-prices and https://docs.qwencloud.com/resources/free-quota
- OR Image API: https://openrouter.ai/blog/tutorials/image-generation/ and Qwen models https://openrouter.ai/qwen/qwen-image-2.1-turbo / https://openrouter.ai/qwen/qwen-image-3-pro
