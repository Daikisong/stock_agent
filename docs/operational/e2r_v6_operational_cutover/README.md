# E2R v6 운영 인수 증거

이 디렉터리는 Phase 101~109 운영 인수 결과를 추적 가능한 작은 영수증으로 보관한다.

핵심 원칙은 원본 `output/`을 커밋하는 것이 아니라 최종 점수에 실제 사용된 fact, source, judge, anchor와 Stage 입력을 결박하는 것이다. 검증기는 영수증과 현재 코드·설정만 사용하며 `output/`, cache, `.env`, 협업 journal을 읽지 않는다.

현재 상태는 [starting_state.json](starting_state.json)과 [provider_lineage_blocker_audit.json](provider_lineage_blocker_audit.json)에 기록했다. Phase 106 실행 중 반복 leaf가 실제 진척처럼 보였던 원인과 재발 방지는 [phase106_semantic_retry_incident.md](phase106_semantic_retry_incident.md)에 기록했다. Phase 101 canonical receipt는 Codex-only 재생성 및 독립 검증 PASS 후 `canary_receipts/2026-07-12/`에 공개한다.

Codex-only는 신규 호출만 뜻하지 않는다. Source Graph, fact, component, judge,
Supervisor 어느 leaf에도 과거 로컬 LLM provider가 만든 checkpoint 계보를 재사용하지
않는다. 실행 가능한 로컬 provider·CLI·endpoint·모델 다운로드 경로는 저장소에서
제거됐고, 과거 명칭은 receipt/checkpoint를 거부하는 감사 denylist에만 남긴다.

Phase 94 계약상 `checkpoint_resume=true`는 필수다. 따라서 clean 최초 실행은
`false`로 바꾸는 방식이 아니라, **존재하지 않거나 완전히 비어 있는 output root**에
`true`로 시작한다. 이후 resume도 그 clean run이 자체 생성한 checkpoint만 읽는다.
과거 스키마는 candidate ranking과 component memo의 provider 계보를 모든 leaf에
영속화하지 않았으므로 pre-cutover root는 사후 검사만으로 clean을 증명할 수 없다.
해당 root의 query, document, fact, cache, collaboration journal, memo, score, stage를
하나도 이식하지 않고 전량 폐기하는 것이 실행 전제다.

최종 receipt는 알려진 Codex provider 이름만 허용한다. 이름에 `CODEX`라는 문자열을
붙인 임의 provider도 허용하지 않으며, provider call과 실제 scoring fact 계보를
각각 다시 계산한다. 21개 judge의 provider/route와 manifest의 현재 실행 provider도
같은 exact allowlist로 검사하며, 하나라도 허용 목록 밖이면 실패한다.

검증 명령:

```bash
PYTHONPATH=src python -m e2r.cli.verify_e2r_v6_tracked_receipts \
  --receipt-root docs/operational/e2r_v6_operational_cutover/canary_receipts/2026-07-12 \
  --offline true
```

같은 receipt를 두 번 독립 재생해 점수·Stage와 replay variance까지 확인하는
Phase 103 readiness 명령:

```bash
set -o pipefail; \
  git show HEAD:scripts/verify_e2r_v6_tracked_readiness.py | \
  python3 -I -S - --repo-root .
```

이 명령은 변경 가능한 worktree의 E2R 모듈을 먼저 import하지 않는다. Git HEAD의
stdlib-only bootstrap이 깨끗한 detached worktree를 만든 뒤, 그 안의 verifier만 별도
isolated Python process에서 실행한다. 또한 `output/`, `.env`, cache, 협업 journal을
입력으로 사용하지 않는다.
검증 결과의 `production_readiness_authority=false`는 이 작은 receipt 검증 하나가
Phase 104~109의 운영 인수를 대신할 수 없다는 뜻이다.

쉬운 예: 삼성전자 점수가 `66.8`이라는 숫자만 보관하지 않는다. 7개 component 합이 실제로 `66.8`인지, 세 judge의 제안으로 각 component 점수가 다시 나오는지, 사용된 fact가 source와 짧은 검수 인용 및 hash로 이어지는지, 그 점수 벡터로 Stage `2`가 다시 나오는지를 한 번에 확인한다.
