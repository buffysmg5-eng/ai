#!/bin/bash
# 사용법: scripts/gen-image.sh "프롬프트" [출력파일.png] [크기]
#   크기: 1024x1024(기본) | 1536x1024(가로) | 1024x1536(세로)
#   모델은 IMAGE_MODEL 환경변수로 변경 가능 (기본 gpt-image-1)
set -euo pipefail
prompt="${1:?프롬프트를 입력하세요}"
out="${2:-image-$(date +%Y%m%d-%H%M%S).png}"
size="${3:-1024x1024}"
: "${OPENAI_API_KEY:?OPENAI_API_KEY 가 설정되어 있지 않습니다}"

body=$(jq -n --arg m "${IMAGE_MODEL:-gpt-image-1}" --arg p "$prompt" --arg s "$size" \
  '{model:$m, prompt:$p, size:$s, n:1}')
resp=$(curl -sS https://api.openai.com/v1/images/generations \
  -H "Authorization: Bearer $OPENAI_API_KEY" -H "Content-Type: application/json" -d "$body")

b64=$(jq -r '.data[0].b64_json // empty' <<<"$resp")
if [ -z "$b64" ]; then
  echo "이미지 생성 실패: $(jq -r '.error.message // .' <<<"$resp")" >&2
  exit 1
fi
mkdir -p "$(dirname "$out")"
base64 -d <<<"$b64" > "$out"
echo "$out"
