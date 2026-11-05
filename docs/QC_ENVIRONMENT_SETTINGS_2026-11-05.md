# QC — Environment settings extraction + the owner's ask (2026-11-05)

Owner-carried screenshot (2026-11-05 06:51), settings extraction banked verbatim below. Raw PNG bytes could not cross from the banking session (same environment limit as the residue packet — honestly receipted); the description is vision-extracted, full-structure.

## The screen: "Settings / Add Environment"

Fields, verbatim:
- **GitHub organization:** MarkDude-design
- **Repository:** ALLurbaseRnotbelong2us (public)
- **Name:** ALLurbaseRnotbelong2us (22/128)
- **Description:** input, placeholder "Input description"

**Code execution** section:
- **Environment variables:** name/value inputs, placeholders "Please enter the variable name." / "Please enter the variable value."
- **Setup script** (placeholder example verbatim):
  ```
  # e.g.
  pip install -r requirements.txt
  npm install
  /run/setup.sh
  ```
- Buttons: **"+ Add variables"** and **"Submit"**

## What the owner says about it

"I can't change the repo" — the Repository field shows the ALLurbaseRnotbelong2us binding, same limitation the return packet already receipted (docs/QC_GITHUB_RETURN_V0.md: the earlier GUI setup was tied to one repository, could not be changed there, and was eventually deleted). This screen appears to be a NEW Add Environment flow in the same family.

## The ask — two candidate approaches, in the owner's order of confidence

1. **Repo via settings string (less likely):** if this environment config is editable as a string/JSON behind the form, the repository value might be changeable there. If the GUI refuses again, that is the receipted capability result — do not retry around it.
2. **Import the terminal commands directly (the owner's likely route — "that seemed to work for some things"):** the setup-script field accepts shell commands, and a pasted terminal command has been interpreted successfully in this workspace before (per the return packet). The bounded sequence already written in docs/QC_GITHUB_RETURN_V0.md applies:
   ```sh
   git rev-parse --show-toplevel
   git status --short --branch
   command -v gh
   ```
   Establish which operations actually execute BEFORE claiming shell access. A clean "this did not run" is the datum.

## Standing rails (unchanged, from the return packet)

- Bounded task; receipt destination: issue #8 (read its latest comments before acting).
- No new credentials, no keys in chat, no `gh auth token`, no credential-file inspection; do not re-provision a credential merely because its value is invisible.
- Default routing: agent → Z → Meraki/Mark on escalation; routine work within recorded authority continues without a new permission request.
- Default endpoint must not recreate the old unchangeable repository binding — each task names its repository.
- Receipt fields as specified in the return packet (seat_claimed, transport, read_up_to, did, delivery, credential_persistence, blocked, next, usage, cost).

— Z (Vibe/Mistral, banking session 2026-11-05; settings extraction owner-carried; posted via shared GitHub account)