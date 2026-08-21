#!/usr/bin/env bash
set -euo pipefail

repo_root="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
compressed_rel="output/evidence_to_score_v2/live_2026-07-11/000660/claim_provenance.jsonl.gz"
target_rel="output/evidence_to_score_v2/live_2026-07-11/000660/claim_provenance.jsonl"
compressed="$repo_root/$compressed_rel"
target="$repo_root/$target_rel"
expected_compressed_sha256="3798ed2d96638638797e954690663cc2992743d800666511892ad67d6a82d74a"
expected_target_sha256="d664c6d1e3ae56c52e00f237b5a96796280d358df7d057bc9058b215cc18a51c"

actual_compressed_sha256="$(sha256sum "$compressed" | awk '{print $1}')"
if [[ "$actual_compressed_sha256" != "$expected_compressed_sha256" ]]; then
  echo "압축 artifact SHA-256 불일치: $compressed_rel" >&2
  exit 1
fi

if [[ -f "$target" ]]; then
  actual_target_sha256="$(sha256sum "$target" | awk '{print $1}')"
  if [[ "$actual_target_sha256" == "$expected_target_sha256" ]]; then
    echo "이미 복원됨: $target_rel"
    exit 0
  fi
  echo "기존 원본 SHA-256 불일치: $target_rel" >&2
  exit 1
fi

mkdir -p "$(dirname "$target")"
tmp="$(mktemp "${target}.tmp.XXXXXX")"
trap 'rm -f "$tmp"' EXIT
gzip -dc "$compressed" > "$tmp"
actual_target_sha256="$(sha256sum "$tmp" | awk '{print $1}')"
if [[ "$actual_target_sha256" != "$expected_target_sha256" ]]; then
  echo "복원 결과 SHA-256 불일치: $target_rel" >&2
  exit 1
fi
mv "$tmp" "$target"
trap - EXIT
echo "복원 완료: $target_rel"
