#!/usr/bin/env bash
# Prototype B: image bytes in this seat -> validated image -> GitHub Contents API.
# Runs DRY-RUN by default, and --publish is restricted to a NON-DEPLOYED branch.
# Never fetch arbitrary URLs; never print the credential or base64 image.
set -euo pipefail

REPO="MarkDude-design/ALLurbaseRnotbelong2us"
BRANCH="work/kulay-media-tools-rounds-2026-11-08"
ROOT="docs/preview-sites/kulay/images"

usage() {
  echo "Usage: $0 [--dry-run|--publish] LOCAL_FILE safe-name.jpg" >&2
  exit 2
}
[[ "${1:-}" == "--dry-run" || "${1:-}" == "--publish" ]] || usage
[[ $# -eq 3 ]] || usage
MODE="$1"
SOURCE="$2"
NAME="$3"
[[ -f "$SOURCE" && -r "$SOURCE" ]] || { echo "Input image absent/unreadable" >&2; exit 2; }
[[ "$NAME" =~ ^[a-z0-9][a-z0-9-]{0,55}\.(jpg|jpeg|png|webp)$ ]] || { echo "Unsafe filename" >&2; exit 2; }

bytes=$(wc -c < "$SOURCE" | tr -d ' ')
[[ "$bytes" =~ ^[0-9]+$ && "$bytes" -gt 12 && "$bytes" -le 8388608 ]] || { echo "Image size must be 13 bytes to 8MiB" >&2; exit 2; }

headhex=$(od -An -tx1 -N12 "$SOURCE" | tr -d '[:space:]')
ext="${NAME##*.}"
case "$ext" in
  jpg|jpeg) [[ "$headhex" == ffd8ff* ]] || { echo "Not JPEG bytes" >&2; exit 2; };;
  png) [[ "$headhex" == 89504e470d0a1a0a* ]] || { echo "Not PNG bytes" >&2; exit 2; };;
  webp) [[ "$headhex" == 52494646*57454250 ]] || { echo "Not WebP bytes" >&2; exit 2; };;
esac

dest="$ROOT/$NAME"
if command -v sha256sum >/dev/null 2>&1; then
  digest=$(sha256sum "$SOURCE" | cut -d' ' -f1)
else
  digest=$(shasum -a 256 "$SOURCE" | cut -d' ' -f1)
fi
printf 'validated image: repo=%s branch=%s dest=%s bytes=%s sha256=%s mode=%s\n' \
  "$REPO" "$BRANCH" "$dest" "$bytes" "$digest" "$MODE"

[[ "$MODE" == "--publish" ]] || { echo "DRY_RUN_ONLY: nothing uploaded."; exit 0; }
[[ -n "${GITHUB_TOKEN:-}" ]] || { echo "No GITHUB_TOKEN, refusing upload" >&2; exit 3; }
# Target branch is fixed above. This experiment CANNOT update deployed main.
bodyfile=$(mktemp)
responsefile=$(mktemp)
trap 'rm -f "$bodyfile" "$responsefile"' EXIT
encoded=$(base64 < "$SOURCE" | tr -d '\n\r')
printf '{"message":"lab: add image %s","branch":"%s","content":"%s"}' \
  "$NAME" "$BRANCH" "$encoded" > "$bodyfile"
unset encoded
status=$(curl --silent --show-error --max-time 60 \
  --request PUT "https://api.github.com/repos/$REPO/contents/$dest" \
  --header "Accept: application/vnd.github+json" \
  --header "Authorization: Bearer $GITHUB_TOKEN" \
  --header "Content-Type: application/json" \
  --data-binary "@$bodyfile" \
  --output "$responsefile" --write-out '%{http_code}')
if [[ "$status" != "201" && "$status" != "200" ]]; then
  echo "Upload rejected by GitHub HTTP $status (response withheld)" >&2
  exit 4
fi
echo "PUBLISHED_TO_LAB_BRANCH: $dest; readback verification still required."
