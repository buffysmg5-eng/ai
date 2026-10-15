#!/bin/bash
# 클라우드 세션 시작 시 Codex CLI 설치 + API 키 로그인.
# API 키는 저장소에 넣지 않는다. 환경 설정의 OPENAI_API_KEY 환경변수에서 읽는다.
set -uo pipefail

# 원격(클라우드) 세션에서만 실행
if [ "${CLAUDE_CODE_REMOTE:-}" != "true" ]; then
  exit 0
fi

if ! command -v codex >/dev/null 2>&1; then
  echo "Codex CLI 설치 중..." >&2
  npm install -g @openai/codex >/dev/null 2>&1 || { echo "Codex CLI 설치 실패" >&2; exit 0; }
fi

if [ -z "${OPENAI_API_KEY:-}" ]; then
  echo "OPENAI_API_KEY 가 없어 Codex 로그인을 건너뜁니다." >&2
  exit 0
fi

if ! codex login status >/dev/null 2>&1; then
  if printenv OPENAI_API_KEY | codex login --with-api-key >/dev/null 2>&1; then
    echo "Codex 로그인 완료" >&2
  else
    echo "Codex 로그인 실패" >&2
  fi
fi
exit 0
