# Census v4 0701 v30 Provider Timeout Guard and Full Thesis Queue Cross Validation

작성일: 2026-07-02 KST

## 0. 결론

이번 v30 패치는 운영 `FULL_THESIS` Stage를 만든 패치가 아니다.

이번 패치의 목적은 두 가지다.

```text
1. CENSUS_EVENT_BOARD 비 Stage0 행 85개를 운영 Stage로 오해하지 않고
   FULL_THESIS refresh queue로 계속 추적한다.

2. codex_cli claim extractor가 멈추거나 timeout/provider_error를 내면
   READY 근거로 쓰지 못하게 감사 카운트와 gate blocker에 남긴다.
```

쉽게 말하면:

```text
Stage1/Stage2-Watch처럼 보이는 행이 85개 있다.
하지만 이건 "운영 점수/Stage가 완성됐다"가 아니라
"FULL_THESIS 심사를 열어야 할 후보가 85개 있다"는 뜻이다.

또 LLM 추출기가 멈추면 그 결과는 0점/Red도 아니고 READY도 아니다.
그냥 provider pending / not ready로 남겨야 한다.
```

## 1. Stage가 있는가

정확한 답:

```text
CENSUS_EVENT_BOARD 상태판 Stage:
  있다.
  row_count = 3391
  non_Stage0 = 85

운영 FULL_THESIS Stage:
  아직 없다.
  row_count = 0

FULL_E2R_100 verified score:
  아직 없다.
  row_count = 0
```

따라서 다음 표현은 금지다.

```text
나쁜 표현:
  "Stage가 85개 나왔으니 운영 Stage가 있다."

정확한 표현:
  "상태판 비 Stage0 행은 85개다.
   운영 FULL_THESIS Stage는 0개라서 아직 운영 점수/Stage로 말할 수 없다."
```

예시:

```text
SK하이닉스가 queue 첫 row에 있다.
source_base_stage = Stage1
source_stage_scope = CENSUS_EVENT_BOARD
operator_stage_use = NOT_FULL_THESIS_STAGE
target_archetype_status = BRAIN_HYPOTHESIS_REQUIRED

즉 이 row는 "HBM/C06 운영 Stage1"이 아니다.
FULL_THESIS 심사를 시작해야 하는 대기열 row다.
```

## 2. 코드 패치

변경된 핵심 파일:

```text
src/e2r/production/claim_extraction/extractor_provider.py
src/e2r/research_brain/v4_schemas.py
src/e2r/research_brain/v4_production_orchestrator.py
src/e2r/research_brain/v4_evidence_extraction_bridge.py
src/e2r/census/census_runner_v4.py
src/e2r/cli/run_e2r_census_v4_until_pass.py
tests/test_research_brain_v4_operational_modes.py
tests/test_census_v4_brain_web_readiness_gate.py
```

## 3. Provider timeout guard

추가한 설정:

```text
ProductionShadowV4Config.claim_extractor_timeout_seconds = 60.0
CensusV4RunConfig.brain_claim_extractor_timeout_seconds = 60.0
CLI:
  --brain-claim-extractor-timeout-seconds 60.0
```

Codex extractor timeout 처리:

```text
기존:
  subprocess.TimeoutExpired가 일반 예외 문자열처럼 묻힐 수 있음.
  partial output을 사람이 READY 증거로 오해할 여지가 있음.

변경:
  provider_error = codex_cli_timeout:60s
  timeout_seconds = 60.0
  claim_extractor_runs.jsonl row에 timeout_seconds 기록
  llm_claim_extraction_audit.json에 provider_error_count / timeout_count 기록
  brain_web_readiness_gate_audit.json에서 provider_error/timeout이 있으면 BLOCKED
```

쉬운 예:

```text
뉴스 원문 fetch는 됐다.
하지만 LLM claim extractor가 60초 안에 claim을 못 뽑고 timeout.

잘못된 처리:
  "자료가 없으니 0점 또는 Red"
  또는
  "LLM 호출 row가 있으니 Brain/Web READY"

정확한 처리:
  "claim 추출 provider failed"
  "점수/Stage 승격 금지"
  "ProviderPending / Not ready"
```

## 4. Brain/Web gate 보강

새로 gate에 들어간 카운트:

```text
llm_claim_extractor_provider_error_count
llm_claim_extractor_timeout_count
```

새 blocker:

```text
LLM claim extractor provider errors are unresolved: N
LLM claim extractor timeouts are unresolved: N
```

중요한 구분:

```text
비핵심 source task 1개가 PROVIDER_FAILED:
  다른 claim-backed 경로가 완전히 닫혔다면 READY를 막지 않을 수 있다.

claim extractor 자체가 PROVIDER_FAILED:
  문서에서 점수 claim을 못 만든 것이므로 Brain/Web READY를 막는다.
```

예시:

```text
IR PDF 하나가 안 열렸지만 DART 원문 claim과 StageCourt가 닫힘
  -> 비핵심 provider gap일 수 있음.

LLM extractor가 timeout이라 raw assertion을 못 뽑음
  -> 해당 문서의 claim path가 끊김.
  -> READY 불가.
```

## 5. v30 산출물 검증

검증 output:

```text
output/census_v4/2026-07-01-full-thesis-refresh-queue-provider-timeout-v30
```

실행:

```text
PYTHONPATH=src python -m e2r.cli.run_e2r_census_v4_until_pass \
  --as-of-date 2026-07-01 \
  --universe krx \
  --output-root output/census_v4/2026-07-01-full-thesis-refresh-queue-provider-timeout-v30 \
  --v3-output-root output/census_v3/2026-07-01 \
  --run-mode LEDGER_REFRESH_CENSUS \
  --brain-web-mode disabled \
  --brain-planner-provider none \
  --brain-source-acquisition frozen_real_source_snapshot \
  --brain-stage-promotion-mode disabled \
  --full-thesis-smoke-mode disabled \
  --target-gate anti_fake \
  --max-iterations 1 \
  --fail-on-run-mode-overclaim false \
  --fail-on-atomic-mismatch false \
  --fail-on-semantic-guard false \
  --fail-on-critical-audit false \
  --test-result-artifact output/test_full_repo_0701/full_unittest_after_p0f_p0j_postextract_bounded_retry_artifact.json \
  --write-operational-docs false
```

결과:

```text
stdout = ANTI_FAKE_FULL_UNIVERSE_STATUS_PASS
```

핵심 수치:

```text
stage_scope_distribution:
  CENSUS_EVENT_BOARD = 3391

event_board_non_stage0_count = 85
full_thesis_refresh_queue_candidate_count = 85
full_thesis_stage_row_count = 0
full_e2r_verified_score_row_count = 0
```

## 6. FULL_THESIS refresh queue 검증

Queue audit:

```text
verdict = PASS
queue_candidate_count = 85
event_board_non_stage0_count = 85
full_thesis_stage_row_count = 0
```

Critical counts:

```text
queue_missing_event_board_count = 0
score_allowed_before_execution_count = 0
stage_promotion_allowed_before_execution_count = 0
hardcoded_query_count = 0
unbounded_budget_count = 0
operator_stage_copy_count = 0
```

Queue priority:

```text
P2_EVENT_WATCH_REFRESH = 36
P1_MATERIAL_STAGE_REFRESH = 30
P1_PENDING_MATERIAL_REFRESH = 18
P0_RISK_REVIEW_REFRESH = 1
```

Source base stage:

```text
Stage1 = 54
Stage2-Watch = 30
Red = 1
```

Decision status:

```text
FINAL = 36
PENDING_MATERIAL_GAPS = 30
SOURCE_PENDING = 18
RISK_REVIEW = 1
```

Score scale:

```text
EVENT_WEIGHTED_PARTIAL = 67
NO_SCORE = 18
```

Queue safety:

```text
score_allowed_before_execution = false for all 85
stage_promotion_allowed_before_execution = false for all 85
hardcoded_queries = [] for all 85
query_intents = [] for all 85
official_first_required = true
```

쉬운 예:

```text
source_base_stage = Stage2-Watch인 row도 있다.
하지만 queue row의 score_allowed_before_execution=false이고
stage_promotion_allowed_before_execution=false다.

즉 "Stage2-Watch니까 운영 Stage2"가 아니라
"Stage2처럼 보이는 상태판 이벤트라서 FULL_THESIS 검증을 예약"한 것이다.
```

## 7. LLM claim extraction audit 검증

v30은 `brain_web_mode=disabled`로 돌린 ledger-refresh 검증이다.
그래서 LLM claim extraction은 요청되지 않았다.

```text
llm_claim_extraction_audit.verdict = DISABLED_HONESTY_PASS
pass_scope = disabled_honesty
llm_claim_extractor_attempt_count = 0
llm_claim_extractor_real_provider_count = 0
llm_claim_extractor_provider_error_count = 0
llm_claim_extractor_timeout_count = 0
configured_timeout_seconds = 60.0
```

중요:

```text
이 값은 "LLM path가 성공했다"가 아니다.
"이번 ledger-refresh run은 LLM path를 요청하지 않았고,
 그 사실을 정직하게 기록했다"는 뜻이다.
```

Brain/Web readiness gate:

```text
verdict = NOT_REQUESTED
brain_web_evidence_pass_allowed = false
llm_claim_extractor_provider_error_count = 0
llm_claim_extractor_timeout_count = 0
```

## 8. Manifest 교차검증

Artifact manifest:

```text
full_thesis_refresh_queue.jsonl
  row_count = 85
  sha256 = 544ae1447cfbca9c37606199011fc351ef59fb507b57a47ab7cf4701c6616c7b

full_thesis_refresh_queue_audit.json
  sha256 = cf0036952ddf6b559da41f84695fa75049823d897c9ac54ff0dd4d25d264835b

llm_claim_extraction_audit.json
  sha256 = dd8254f5368a77ca01aeac004e18d6a1dbf96c9ea61a983586f54a87df995d79
```

Report generation audit도 같은 숫자를 본다.

```text
operator_stage_warning:
  full_thesis_rows=0
  full_thesis_refresh_queue_candidates=85
  full_e2r_verified_score_rows=0
  event_board_non_stage0_rows=85
```

## 9. 테스트

Targeted:

```text
PYTHONPATH=src python -m unittest \
  tests.test_research_brain_v4_operational_modes \
  tests.test_census_v4_brain_web_readiness_gate -v

result:
  Ran 54 tests / OK
```

이 테스트가 새로 확인하는 것:

```text
ProductionShadowV4Config 기본 claim_extractor_timeout_seconds = 60.0
claim_extractor_timeout_seconds <= 0 이면 config validate 실패
auto + live_full_bounded이면 CodexCLIExtractorProvider를 쓰고 timeout 값이 provider에 전달됨
LLM claim extractor provider_error / timeout이 있으면 Brain/Web READY gate BLOCKED
비핵심 provider_failed source task는 완전히 닫힌 claim-backed path를 자동으로 막지 않음
```

## 10. 아직 완료가 아닌 이유

v30 이후에도 다음은 여전히 0이다.

```text
FULL_THESIS production row = 0
FULL_E2R_100 verified score row = 0
Brain/Web accepted live web/LLM claim = 0
```

따라서 목표는 아직 완료가 아니다.

이번 패치가 닫은 것은:

```text
"Stage가 있는 것처럼 보이는 row를 운영 Stage로 오해하는 문제"
"LLM provider가 멈춘 partial output을 READY 근거로 오해하는 문제"
```

아직 닫지 못한 것은:

```text
FULL_THESIS refresh queue 85개를 실제 Research Brain / Evidence OS / StageCourt로 실행
source-backed primitive coverage 확보
모든 아키타입 replay parity
operating FULL_E2R_100 score 생성
```

## 11. 다음 패치 방향

다음 작업은 두 갈래다.

```text
P0-K provider timeout/pending cutover:
  이번 패치로 timeout 설정과 audit blocker는 생겼다.
  다음은 live Brain/Web run에서 timeout이 발생해도 partial output directory를
  invalid/pending으로 명확히 닫고, operator report에 "무효 산출물"로 표시해야 한다.

P0-G source route quality:
  Tistory/블로그/급등종목/텔레그램 같은 source를 점수 route에서 더 빨리 reject.
  DART detail / KIND / KRX / IssuerIR / CompanyGuide / trusted report PDF / 회사 newsroom을
  official-first task로 우선 라우팅.
```

우선순위:

```text
1. live run이 멈춰도 안전하게 pending으로 닫히게 하는 P0-K 마무리
2. 85개 FULL_THESIS refresh queue 중 우선순위 P0/P1부터 source route 품질 개선
3. 실제 accepted claim -> score contribution -> StageCourt -> FULL_THESIS row까지 닫는 smoke
4. C01~C36 replay parity와 adversarial suite 확장
```

## 12. 다음 에이전트 공격 체크리스트

다음 에이전트는 아래를 공격적으로 확인해야 한다.

```text
1. full_thesis_refresh_queue 85개가 정말 event_board_non_stage0 85개와 1:1인가?
2. queue row 중 score_allowed_before_execution=true가 하나라도 있는가?
3. queue row 중 stage_promotion_allowed_before_execution=true가 하나라도 있는가?
4. queue row 중 hardcoded query가 들어간 row가 있는가?
5. queue row budget이 0 또는 unbounded인 row가 있는가?
6. CENSUS_EVENT_BOARD stage가 operator FULL_THESIS stage로 복사된 row가 있는가?
7. llm_claim_extraction_audit가 provider_error/timeout을 PASS로 숨기는가?
8. brain_web_readiness_gate가 LLM provider timeout이 있어도 READY를 허용하는가?
9. partial live output directory를 readiness evidence로 쓰는 문서/코드가 남아 있는가?
10. FULL_THESIS row 0인데 "운영 Stage 있음"이라고 말하는 문서가 남아 있는가?
```

## 13. 최종 판정

```text
v30 patch status:
  PASS for queue/audit/timeout guard wiring

operational FULL_THESIS:
  still NOT_READY

safe wording:
  "상태판 비 Stage0 85개가 있고, 이 85개는 FULL_THESIS refresh queue에 올라갔다.
   운영 FULL_THESIS Stage와 FULL_E2R_100 점수는 아직 0개다."
```

한 줄 결론:

```text
지금은 Stage가 없는 게 아니라, Stage의 종류를 분리해야 한다.
Census 상태판 Stage는 있지만 운영 FULL_THESIS Stage는 아직 없고,
이번 패치는 그 차이를 산출물과 timeout guard로 더 안전하게 고정했다.
```
