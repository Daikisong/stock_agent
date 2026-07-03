# Census v4 0701 SourceQuality v9 Candidate Order / Continuation Patch Result And Next Router Bottleneck

작성일: 2026-07-02

이 문서는 2026-07-01 Census v4 Brain/Web 최신 진단(`sourcequality-v9`)을 다음 에이전트가 강하게 공격할 수 있도록 정리한 감사 노트다.

결론부터 말하면:

```text
Stage label이 있는 row는 있다.
하지만 운영 FULL_THESIS Stage는 아직 없다.

v9에서는 후보 순서와 추가 후보 시도가 개선됐다.
첫 실제 Brain 후보가 대웅 시설투자 정정에서 그린생명과학 공급계약 정정으로 바뀌었고,
accepted claim target을 못 채우면 다음 후보까지 이어 가는 continuation도 실제로 동작했다.

하지만 운영 승격은 여전히 0개다.
web/LLM accepted claim = 0
BRAIN_WEB_PARTIAL row = 0
FULL_THESIS row = 0
```

쉬운 예:

```text
전에는 시험 볼 학생을 잘못 먼저 세웠다.
v9에서는 "공급계약 공시"처럼 답안지가 나올 가능성이 큰 학생을 먼저 세웠다.

하지만 그 학생의 답안지를 채점하는 과목이 잘못 배정됐다.
공급계약 답안지를 "매출/물량 증가" 과목으로 채점하려 해서,
계약금액과 상대방이 있어도 점수로 못 들어갔다.
```

## 1. 감사 대상 산출물

최신 진단:

```text
output/census_v4/2026-07-01-brain-web-diagnostic-sourcequality-v9
```

실행 명령 핵심:

```text
python -m e2r.cli.run_e2r_census_v4_until_pass
  --as-of-date 2026-07-01
  --run-mode BRAIN_AND_WEB_ACQUISITION_ENABLED
  --brain-web-mode enabled
  --brain-planner-provider codex_cli
  --brain-source-acquisition live_full_bounded
  --brain-universe-limit 1
  --brain-planner-success-limit 1
  --brain-planner-batch-size 1
  --brain-max-source-tasks-per-plan 5
  --brain-max-fetches-per-task 1
  --brain-accepted-claim-target 1
  --brain-max-distinct-candidate-attempts 4
  --brain-claim-extractor-provider codex_cli
  --brain-stage-promotion-mode strict
  --target-gate brain_web
  --max-iterations 1
```

중요한 해석:

```text
brain-universe-limit = 1 이지만, v9에서는 discovery limit을 동적으로 넓힌다.
planner_success_limit = 1 이지만, accepted_claim_target을 못 채우면 다음 후보를 추가 시도한다.

따라서 v9 output에 실제 후보가 2개 나온 것은 설정 오류가 아니라
accepted claim target 기반 continuation 동작의 증거다.
```

## 2. Stage가 있긴 한가?

있다. 하지만 전부 `CENSUS_EVENT_BOARD` 범위다.

`output/census_v4/2026-07-01-brain-web-diagnostic-sourcequality-v9/census_stage_summary.json` 기준:

```text
stage_status_count = 3391

stage_scope_distribution:
  CENSUS_EVENT_BOARD = 3391
  BRAIN_WEB_PARTIAL = 0
  FULL_THESIS = 0

score_scope_distribution:
  NO_SCORE = 3324
  EVENT_WEIGHTED_PARTIAL = 67
  FULL_E2R_100 = 0

base_stage_display_distribution:
  EVENT_BOARD_STAGE0 = 3306
  EVENT_BOARD_STAGE1 = 54
  EVENT_BOARD_STAGE2_WATCH = 30
  EVENT_BOARD_RED = 1

canonical_stage_distribution:
  0 = 3306
  1 = 54
  2 = 30
  3-Red = 1

event_board_non_stage0_count = 85
verified_score_present_count = 0
full_thesis_stage_row_count = 0
full_e2r_verified_score_row_count = 0
```

직접 답:

```text
Stage가 있는 애들은 있다.
하지만 운영 full thesis Stage가 있는 애들은 없다.
```

쉬운 예:

```text
Stage1:
  "공식 이벤트가 있으니 watchlist에 올려 확인하라"는 상태판이다.

FULL_THESIS Stage:
  "공시/IR/뉴스 원문 claim이 accepted되고,
   primitive와 score contribution을 거쳐 StageCourt가 확정했다"는 운영 채점 결과다.

현재는 첫 번째만 있고 두 번째는 0개다.
```

## 3. v9 Brain/Web readiness 결과

`brain_web_readiness_gate_audit.json` 기준:

```text
verdict = BLOCKED
run_mode = BRAIN_AND_WEB_ACQUISITION_ENABLED

llm_planner_call_count = 22
llm_real_provider_success_count = 3
source_task_execution_count = 21
web_search_task_count = 10
web_search_result_count = 66
web_fetched_document_count = 3
web_rejected_document_count = 53
llm_claim_extractor_attempt_count = 3

brain_accepted_claim_count = 2
official_accepted_claim_count = 2
web_or_llm_accepted_claim_count = 0
brain_score_contribution_count = 5
brain_stage_trace_count = 1
brain_promoted_stage_row_count = 0
```

blockers:

```text
web/LLM accepted claim count is zero
Brain/Web StageCourt traces are not promoted into census_stage_status
brain stage promotion verdict is not PROMOTION_APPLIED: BLOCKED
Brain/Web operational minimum planner runs not met: 22/30
Brain/Web operational minimum web search tasks not met: 10/20
Brain/Web operational minimum web/news search calls not met: 10/20
Brain/Web operational minimum fetched documents not met: 3/10
Brain/Web operational minimum claim extractor attempts not met: 3/10
Brain/Web operational minimum web/LLM accepted claims not met: 0/3
```

해석:

```text
v8보다 좋아진 점:
  Brain accepted official claim 2개
  Brain score contribution 5개
  Brain StageCourt trace 1개

아직 막힌 점:
  web/LLM accepted claim 0개
  promotion 0개
  operational minimum 미달
```

쉬운 예:

```text
DART 원문에서 공식 claim은 일부 닫혔다.
하지만 "웹/뉴스/LLM이 읽은 비공식 원문까지 accepted claim으로 닫힌 경로"는 아직 없다.

그래서 strict mode에서는 BRAIN_WEB_PARTIAL로 올리면 안 된다.
```

## 4. v9 patch가 실제로 고친 것

코드 변경 요약:

```text
ProductionShadowV4Config:
  accepted_claim_target 추가
  max_distinct_candidate_attempts 추가

Research Brain v4 orchestrator:
  후보를 evidence-likelihood 기준으로 정렬
  accepted claim target 미달이면 다음 후보를 추가 시도
  retry bundle merge 중 같은 claim_id가 다른 adjudication으로 들어와도 크래시하지 않고 ledger event로 남김
  candidate report의 accepted_claim_count를 watchlist item이 아니라 bundle accepted claim 기준으로 보정

CLI / Census runner:
  --brain-accepted-claim-target
  --brain-max-distinct-candidate-attempts
  옵션 전달 추가
```

중요한 원칙:

```text
후보 정렬은 조사 순서만 바꾼다.
점수 증거는 여전히 accepted claim만 만든다.
```

쉬운 예:

```text
"공급계약 공시"를 먼저 조사하는 것은 허용된다.
"공급계약 공시니까 무조건 점수 +10"은 금지다.
```

## 5. v9가 증명한 개선

`planner_runs.jsonl` 기준 실제 real planner call:

```text
real provider success = 3

1. initial
   CE-LIVE-DART-114450-20260630901605
   그린생명과학 / [기재정정]단일판매ㆍ공급계약체결

2. initial
   CE-LIVE-DART-003090-20260630801612
   대웅 / [기재정정]신규시설투자등(자회사의 주요경영사항)

3. feedback_retry
   CE-LIVE-DART-114450-20260630901605
   그린생명과학 / rejected mapping feedback 반영 재시도
```

의미:

```text
v8 병목:
  첫 후보 하나만 깊게 보고 accepted claim이 없으면 사실상 멈춤.

v9 개선:
  직접 공급계약 후보가 먼저 올라옴.
  첫 후보가 target을 못 채우면 다음 후보도 실제로 시도함.
  rejected mapping feedback retry도 기록됨.
```

`source_task_executions.jsonl` 기준:

```text
total rows = 113

source_task_execution_origin:
  production_cutover_v3_leaf_artifact = 92
  research_brain_v4_attempt = 21

research_brain_v4_attempt 후보별:
  그린생명과학 114450 = 13 executions
  대웅 003090 = 8 executions

research_brain_v4_attempt status:
  NO_EVIDENCE_FOUND = 15
  PROVIDER_FAILED = 3
  EVIDENCE_OS_ACCEPTED = 2
  REJECTED_BY_POLICY = 1
```

## 6. accepted claims 94건을 잘못 읽으면 안 된다

v9의 `accepted_claims.jsonl`은 94행이다.

하지만 전부 운영 Brain/Web 승격 증거로 읽으면 안 된다.

```text
accepted_claims total = 94

대부분:
  production_cutover_v3_leaf_artifact / census_v3_leaf 계열 공식 이벤트 claim

이번 research_brain_v4_attempt에서 Brain trace까지 닫힌 claim:
  2개
  둘 다 대웅 003090 DART official claim

web_or_llm accepted claim:
  0개
```

`brain_to_claim_trace.jsonl` 기준 Brain trace 2개:

```text
CE-LIVE-DART-003090-20260630801612
symbol = 003090
accepted_claim_id = CLM-f203bcba72dc41930da4
primitive gap = implementation_timeline
source_task_id = dart_detail_20260630801612
trace_status = CLAIM_SCORE_TRACE_EXPORTED_STAGE_NOT_PROMOTED

CE-LIVE-DART-003090-20260630801612
symbol = 003090
accepted_claim_id = CLM-c0ca528888c8fc24ef41
source_task_id = official_status_003090_dart
trace_status = CLAIM_SCORE_TRACE_EXPORTED_STAGE_NOT_PROMOTED
```

쉬운 예:

```text
창고에 계약서가 94장 있다.
그중 오늘 Brain/Web 조사원이 새로 심사해 stage trace까지 연결한 것은 2장이다.
그 2장도 모두 DART 공식문서라서,
"웹/뉴스/LLM 경로가 운영 점수로 닫혔다"는 증거는 아직 아니다.
```

## 7. v9의 핵심 새 병목: 직접 공급계약 공시가 C29 volume 쪽으로 오배정됨

가장 중요한 실패 사례:

```text
candidate_event:
  CE-LIVE-DART-114450-20260630901605
  그린생명과학 / [기재정정]단일판매ㆍ공급계약체결

공시 원문에서 확인된 구조화 정보:
  계약상대방 = UPL Limited
  판매공급지역 = 브라질
  판매ㆍ공급계약 내용 = Plant Health & Protection Chemicals
  확정 계약금액 = 10,238,670,000원
  최근 매출액 = 24,860,636,227원
  매출액 대비 = 41.18%
  조건부 계약여부 = 미해당
```

그런데 planner가 만든 must verify primitive:

```text
volume_growth_visible
cash_or_revision_conversion
operating_leverage_visible
mix_improvement
```

실제 mapping rejection:

```text
primitive_mapping_rejected:
  v4_signal:structured_field_contract_quality_revenue_visibility_contract_export_contract
  v4_signal:structured_field_contract_quality_revenue_visibility_contract

primitive_gap:
  volume_growth_visible
  cash_or_revision_conversion
```

해석:

```text
공시 원문은 "계약 품질 / 매출 가시성 계약" 쪽 claim을 만들 수 있다.
하지만 planner가 "물량 증가 / 영업 레버리지" 점수칸을 열었다.
그래서 실제 계약 정보가 있어도 해당 primitive에는 안 맞아 rejected 됐다.
```

쉬운 예:

```text
학생이 수학 답안을 냈다.
감독관이 그걸 영어 시험지 칸에 넣으려 했다.
답안 자체가 쓸모없는 게 아니라, 답안과 채점 칸이 안 맞은 것이다.
```

이것은 score gate를 낮춰서 해결하면 안 된다.

```text
나쁜 패치:
  단일판매공급계약이면 volume_growth_visible로 그냥 인정한다.

좋은 패치:
  planner가 직접 공급계약 이벤트를 보면
  contract_quality / contract_amount_to_prior_sales / revenue_visibility_contract 같은
  계약 호환 primitive를 가진 archetype/contract를 선택하게 한다.

  또는 planner가 C29를 유지하려면
  "이 계약이 실제 물량 증가/매출 전환/마진 전환으로 연결됐다"는 별도 bridge claim을 요구한다.
```

## 8. 왜 이걸 하드코딩으로 풀면 안 되는가

금지:

```python
if symbol == "114450":
    primitive = "contract_quality"

if "단일판매" in title:
    stage = "2"
```

허용해야 하는 방향:

```text
event ontology:
  이 이벤트는 direct supply/sales contract disclosure다.

contract compatibility:
  선택한 archetype/evidence contract에
  contract_quality, contract_amount_to_prior_sales, revenue_visibility_contract 같은
  contract-compatible primitive가 있는가?

planner feedback:
  원문에는 contract fields가 있는데 현재 selected primitive가 volume/mix/leverage라 탈락했다.
  다음 planner call은 contract-compatible route를 선택하거나,
  volume/mix/leverage bridge를 입증할 source task를 명시해야 한다.
```

쉬운 예:

```text
"주민등록증"을 보면 신원 확인 서류라는 것은 일반 규칙이다.
하지만 특정 사람 이름을 코드에 박으면 하드코딩이다.

마찬가지로 "단일판매공급계약 공시는 계약형 이벤트"라는 ontology는 필요하다.
하지만 "그린생명과학이면 Cxx"는 금지다.
```

## 9. 다음 P0 patch 방향

P0-1. Planner prompt / validator에 direct contract compatibility feedback 추가

```text
입력:
  CandidateEvent title/source_family/primary_disclosure_type
  accepted/rejected mapping trace
  structured signal family

검증:
  direct supply/sales contract event인데
  planner output primitive가 volume/mix/leverage only이면
  "contract fields found, current primitive incompatible" feedback을 강하게 제공한다.
```

P0-2. Event-origin structured replay task가 contract primitive를 잃지 않게 한다

```text
현재:
  원문에서 contract fields는 추출됐지만,
  source task primitive_gap이 volume_growth_visible이라 rejected.

목표:
  direct contract structured source는
  contract-compatible primitive proposal을 별도 mapping proposal로 남긴다.
  단, selected archetype에 없는 primitive를 조용히 점수로 넣지는 않는다.
```

P0-3. 선택 archetype과 source signal family가 안 맞으면 pending으로 남긴다

```text
계약 공시를 C29 volume_growth로 선택했는데
volume bridge가 없고 contract fields만 있으면:
  score = 0
  stage promotion = blocked
  planner feedback = contract-compatible route required

절대:
  contract fields를 volume_growth로 억지 인정하지 않는다.
```

P0-4. test 추가

```text
1. direct supply contract event가 first-order candidate로 우선 정렬된다.
2. direct contract event가 volume-only primitive로 닫히면 rejected reason에 contract compatibility warning이 남는다.
3. direct contract event에서 contract fields가 있으면 contract-compatible route feedback retry가 발생한다.
4. feedback retry가 같은 claim_id를 다르게 재판정해도 ledger event로 남고 실행은 크래시하지 않는다.
5. 그래도 web/LLM accepted claim이 0이면 promotion은 0이어야 한다.
```

## 10. v9 patch 검증

Targeted regression:

```text
PYTHONPATH=src python -m unittest tests.test_research_brain_v4_operational_modes -v

Ran 27 tests
OK
```

Wider targeted regression:

```text
PYTHONPATH=src python -m unittest \
  tests.test_research_brain_v4_candidate_discovery_live_official \
  tests.test_research_brain_v4_real_source_acquisition \
  tests.test_research_brain_v4_operational_modes \
  tests.test_census_v4_run_mode_honesty \
  tests.test_census_v4_brain_bundle_export \
  tests.test_census_v4_brain_web_readiness_gate \
  tests.test_census_v4_artifact_manifest \
  tests.test_census_v4_cli_uses_v4_runner -v

Ran 91 tests
OK
```

Full unittest after v9 patch:

```text
artifact = output/test_full_repo_0701/full_unittest_result_artifact.json
log = output/test_full_repo_0701/full_unittest.log

status = OK
test_count = 5027
duration_seconds = 209.1532
artifact sha256 = faec53cc31b7534a4ddf20694dd2584cbd489f69949acb7fee86b49feb3a95b8
log sha256 = 7f75a3a041b1fcd6c34652b087e9a6a2261e6509d2f92ce1a5e8755a4cc0efed
```

주의:

```text
테스트 OK는 "현재 코드가 기대한 guard를 통과했다"는 뜻이다.
운영 준비 완료라는 뜻은 아니다.

실제 readiness verdict는 여전히 NOT_READY / BLOCKED다.
```

문서 작성 후 핵심 숫자 재검산:

```text
doc key assertions OK

검증한 항목:
  brain_web_readiness_gate_audit.verdict = BLOCKED
  llm_real_provider_success_count = 3
  source_task_execution_count = 21
  web_fetched_document_count = 3
  brain_accepted_claim_count = 2
  web_or_llm_accepted_claim_count = 0
  brain_stage_trace_count = 1
  brain_promoted_stage_row_count = 0
  census_stage_summary.stage_status_count = 3391
  census_stage_summary.event_board_non_stage0_count = 85
  census_stage_summary.full_thesis_stage_row_count = 0
  census_stage_summary.full_e2r_verified_score_row_count = 0
  full_unittest.status = OK
  full_unittest.test_count = 5027
```

## 11. 다음 에이전트가 반드시 공격해야 할 질문

1. 그린생명과학 공급계약 공시가 왜 C29 volume/mix/leverage primitive로 들어갔는가?
2. Planner prompt가 direct contract event를 contract-compatible route로 유도하고 있는가?
3. deterministic router도 direct contract ontology를 이해하는가?
4. C05/C15/Cxx 중 어느 contract가 계약금액/매출대비/상대방/기간을 가장 자연스럽게 받아야 하는가?
5. contract fields를 selected archetype 밖 primitive로 조용히 인정하는 우회가 생기지 않는가?
6. web/LLM accepted claim 0개인데 promotion 0개가 계속 보장되는가?
7. official-only claim으로 BRAIN_WEB_PARTIAL이 다시 열리는 regression이 없는가?
8. rejected raw assertion feedback이 다음 planner call에서 실제 route 변경으로 이어지는가?
9. source task count와 max fetch count가 다시 섞이지 않는가?
10. Census event-board Stage와 FULL_THESIS Stage가 출력/문서/CLI에서 다시 섞이지 않는가?

## 12. 최종 판단

```text
v9는 "후보를 더 잘 고르고, accepted claim target 미달 시 다음 후보를 더 보는" 패치로는 성공했다.

하지만 "직접 계약 공시를 올바른 evidence contract/primitive로 보내는" 문제는 아직 실패다.
따라서 FULL_THESIS 운영 Stage는 여전히 0개이고, Brain/Web cutover는 아직 하면 안 된다.
```

한 줄 요약:

```text
v9는 문 앞까지 더 잘 갔지만, 아직 방 번호를 잘못 찾고 있다.
다음 패치는 source를 더 많이 긁는 것이 아니라,
direct contract event -> contract-compatible primitive route를 Brain/Web에 제대로 알려주는 것이다.
```
