# 보안·권한 경계

정적 감사 critical key 14개를 매 CI에서 재계산한다.

- Tampermonkey runtime dependency 0
- hidden/private ChatGPT API 0
- login automation 0
- credential/cookie persistence 또는 export 0
- approval 없는 submit 0
- DOM submit path 중복 0
- Pro score/Stage authority 0
- dossier 이후 full research restart 0
- corroboration/monitoring supplement 0
- deterministic query template 0
- PR delta의 raw/cache/output 추적 0

로컬 token은 프로세스 시작 때 메모리에서 생성하며 예제 config나 Git에 저장하지 않는다. screenshot은 로그인 정보가 포함될 수 있으므로 runtime의 `private/` 아래에만 두고 Git에 넣지 않는다.

CI는 mock UI만 사용하며 `E2R_RUN_LIVE_TESTS=0`을 강제한다. 실제 ChatGPT 계정, password, cookie를 GitHub Actions에 전달하지 않는다.
