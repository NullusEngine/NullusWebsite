#!/usr/bin/env bash
set -euo pipefail

release_id="${1:-}"
if [[ ! "$release_id" =~ ^[0-9a-f]{40}$ ]]; then
  echo "Expected a full Git commit SHA." >&2
  exit 1
fi

base=/srv/nullus-website
archive="$base/incoming/$release_id.tar.gz"
release="$base/releases/$release_id"
pending_link="$base/.current-$release_id"
stage=""
previous=""
switched=0

exec 9>"$base/.deploy.lock"
flock -w 120 9

cleanup() {
  local status=$?
  if (( status != 0 && switched )); then
    echo "Health check failed. Restoring the previous release." >&2
    if [[ -n "$previous" ]]; then
      ln -sfn -- "$previous" "$pending_link"
      mv -Tf -- "$pending_link" "$base/current"
    else
      rm -f -- "$base/current"
    fi
  fi
  if [[ -n "$stage" && -d "$stage" ]]; then
    rm -rf -- "$stage"
  fi
  rm -f -- "$pending_link" "$archive"
  return "$status"
}
trap cleanup EXIT

test -s "$archive"
if [[ ! -d "$release" ]]; then
  stage="$(mktemp -d "$base/releases/.stage-XXXXXXXX")"
  tar -xzf "$archive" -C "$stage"
  for file in index.html zh-cn/index.html en/index.html styles.css script.js robots.txt sitemap.xml assets/NullusIcon.svg; do
    test -s "$stage/$file"
  done
  chmod -R a+rX "$stage"
  mv -- "$stage" "$release"
  stage=""
fi

if [[ -L "$base/current" ]]; then
  previous="$(readlink "$base/current")"
elif [[ -e "$base/current" ]]; then
  echo "The current website path exists and is not a symlink." >&2
  exit 1
fi

ln -sfn -- "releases/$release_id" "$pending_link"
mv -Tf -- "$pending_link" "$base/current"
switched=1

for path in / /zh-cn/ /en/ /styles.css /script.js /robots.txt /sitemap.xml /assets/NullusIcon.svg; do
  curl --fail --silent --show-error --noproxy '*' --connect-timeout 5 --max-time 15 \
    --resolve www.nullusengine.com:443:127.0.0.1 \
    "https://www.nullusengine.com$path" -o /dev/null
done
switched=0

echo "Published and verified release $release_id."

# Keep recent releases, the active release and the immediate rollback target.
while IFS= read -r old_release; do
  [[ "$old_release" =~ ^[0-9a-f]{40}$ ]] || continue
  if [[ "$old_release" == "$release_id" || "releases/$old_release" == "$previous" ]]; then
    continue
  fi
  rm -rf -- "$base/releases/$old_release"
done < <(find "$base/releases" -mindepth 1 -maxdepth 1 -type d \
  -printf '%T@ %f\n' | sort -nr | tail -n +6 | cut -d' ' -f2-)
