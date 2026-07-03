# Census v4 0701 Raw Assertion Rejection Audit Patch And Stage Truth

작성 시점: 2026-07-02 KST  
latest diagnostic: `output/census_v4/2026-07-01-brain-web-diagnostic-rawreject-v4`  
canonical output: `output/census_v4/2026-07-01`  
as_of_date: `2026-07-01`

> 최신 주의: 이 문서는 `rawreject-v4` 당시의 감사 스냅샷이다. 이후 `promptleaf-v1`과
> `sourcefilter-v1` 진단이 추가됐다. 최신 Brain/Web 보조 진단과 full-test 숫자는
> `census_v4_0701_sourcefilter_promptleaf_live_diagnostic_2026-07-02.md`와 `README.md`를 기준으로 읽는다.
> rawreject-v4 본문 숫자는 당시 재현 기록으로 보존한다.

## 직접 답

```text
Stage가 있는 애들은 있다.
하지만 운영 FULL_THESIS Stage가 있는 애들은 없다.
```

숫자로 나누면:

```text
canonical / latest diagnostic 공통:
  census_stage_status rows = 3391
  event-board non-Stage0 rows = 85
  FULL_THESIS rows = 0
  FULL_E2R_100 verified score rows = 0
  BRAIN_WEB_PARTIAL rows = 0
```

쉬운 예:

```text
지금 있는 Stage는 출석부다.
예: 오늘 전체 종목을 확인했고, 85개는 공시/이벤트 때문에 watch 표시가 붙었다.

우리가 원하는 Stage는 채점지다.
예: C06 HBM thesis의 고객 배정, capacity, revenue mix, FCF bridge가 claim으로 확인되어 87점 Yellow.

출석부는 있다.
채점지는 아직 없다.
```

## 한 줄 결론

```text
official-only claim이 BRAIN_WEB_PARTIAL로 승격되는 문제는 막혔다.
웹/LLM raw assertion이 왜 점수 claim으로 못 갔는지 raw assertion 단위 장부도 생겼다.
claim별 raw rejection reason이 planner feedback retry context에 들어가기 시작했다.
하지만 web/LLM accepted score claim은 여전히 0개라서 Brain/Web cutover와 운영 full thesis Stage는 아직 NOT_READY다.
```

점수 증거 원칙:

```text
CensusAssessmentEvent / CandidateEvent / CensusEvent는 행정적 발견, 분류, 라우팅 이벤트다.
이 객체 자체는 score evidence가 아니다.
score_contribution은 반드시 accepted_claim_id를 support로 가져야 한다.
EVENT_WEIGHTED_PARTIAL도 예외가 아니며, 공식 이벤트 제목/메타데이터만으로 nonzero score를 만들면 critical fail이다.
```

쉬운 예:

```text
DART에서 "단일판매공급계약" 공시를 발견했다.
  -> 후보를 조사 대상으로 올리는 이벤트다.

그 공시 원문에서 계약 상대방, 금액, 기간, 대상회사 직접성, 현재성이
accepted_claim으로 검증됐다.
  -> 그때부터 점수 칸에 들어갈 수 있다.

공시 제목만 있다.
  -> event는 있지만 score evidence는 아니다.
```

즉 이번 패치의 의미는:

```text
좋아진 점:
  "웹을 읽었다"와 "웹 증거가 점수로 채택됐다"를 분리했다.
  "웹 raw assertion이 왜 탈락했는지"를 볼 수 있게 했다.

아직 아닌 점:
  웹/LLM claim이 실제 운영 점수 칸에 들어간 것은 아니다.
  full thesis 점수/Stage가 생긴 것도 아니다.
```

## 패치 요약

변경 파일:

```text
src/e2r/census/census_runner_v4.py
src/e2r/research_brain/v4_evidence_extraction_bridge.py
src/e2r/research_brain/v4_production_orchestrator.py
tests/test_census_v4_brain_bundle_export.py
tests/test_research_brain_v4_evidence_extraction_from_real_document.py
tests/test_research_brain_v4_operational_modes.py
```

핵심 변경:

```text
1. EvidenceOSExecutionBundleV4에 raw_assertion_rejections를 추가했다.
2. LLM/document raw assertion이 score claim으로 채택되지 않으면 raw_assertion_rejections.jsonl에 남긴다.
3. bundle에 rejection row가 없더라도 brain_claim_mapping_trace rejected row에서 fallback rejection row를 만든다.
4. fallback reason은 task/document 단위로 섞인 eligibility_reasons보다 row 자체의 축별 상태를 우선한다.
5. official-only claim은 web/LLM accepted claim으로 세지 않고 BRAIN_WEB_PARTIAL promotion에서도 제외한다.
6. rejected claim feedback은 execution 단위 not_eligible_reasons보다 claim별 raw_assertion_rejections를 우선한다.
7. retry bundle merge 시 raw_assertion_rejections가 사라지지 않게 보존한다.
8. row 자체가 DIRECT/CURRENT/PASS인데 task/document 단위 eligibility reason이 오염돼 있으면 row 축을 우선한다.
9. PlannerRunV4에 planner_run_id, prompt_hash, response_hash, raw_prompt_path, raw_response_path를 추가했다.
10. Census Brain/Web export가 llm_prompts.jsonl, llm_responses.jsonl, planner_raw/prompts/*.json, planner_raw/responses/*.json을 쓰게 했다.
```

이번에 특히 고친 버그:

```text
이전 fallback:
  같은 문서/태스크 안의 다른 assertion에서 나온 target_scope_not_allowed가 섞이면
  DIRECT/CURRENT/PASS인 assertion도 target mismatch로 분류될 수 있었다.

패치 후:
  row.target_scope_status = DIRECT
  row.directness = DIRECT
  row.temporal_status = CURRENT
  row.semantic_status = PASS
  row.mapping_status = REJECTED
  이면 rejection_reason = primitive_mapping_rejected
```

쉬운 예:

```text
한 기사 안에 A문장과 B문장이 있다.
A문장은 대상 회사와 무관해서 탈락했다.
B문장은 대상 회사 문장이지만 점수 primitive와 맞지 않아 탈락했다.

이전에는 B문장도 A문장의 "대상 불일치" 사유를 뒤집어쓸 수 있었다.
이제 B문장은 "primitive mapping 실패"로 남는다.
```

## 검증 명령

Targeted regression:

```bash
PYTHONPATH=src python -m unittest \
  tests.test_research_brain_v4_operational_modes \
  tests.test_census_v4_brain_bundle_export \
  tests.test_research_brain_v4_evidence_extraction_from_real_document \
  tests.test_census_v4_brain_stage_promotion_gate \
  tests.test_census_v4_brain_web_readiness_gate -v
```

결과:

```text
Ran 63 tests
OK
```

Full regression:

```bash
PYTHONPATH=src python -m e2r.cli.run_test_command_with_artifact \
  --artifact output/test_full_repo_0701/full_unittest_result_artifact.json \
  --log output/test_full_repo_0701/full_unittest.log \
  -- python -m unittest discover -s tests -v
```

결과:

```text
status = OK
test_count = 5008
failed_count = 0
error_count = 0
duration_seconds = 185.308
artifact_sha256 = 313b1a232060a40e8bca8ffecb760fd24bb13b256720baf8148546f2a4abf113
log_sha256 = ff59e3d40e1fb38cda323d28d3afa6012f85761fdadbe33ca8ab7fa087ed4d64
```

주의:

```text
rawreject-v4 diagnostic output 내부의 test_result_artifact.json은
진단 실행 당시 복사된 이전 성적표라 test_count=4997이다.
최신 full regression 증거는 output/test_full_repo_0701/full_unittest_result_artifact.json의 5008 OK다.
```

Live diagnostic:

```bash
PYTHONPATH=src python -m e2r.cli.run_e2r_census_v4_until_pass \
  --as-of-date 2026-07-01 \
  --universe krx \
  --output-root output/census_v4/2026-07-01-brain-web-diagnostic-rawreject-v4 \
  --v3-output-root output/census_v3/2026-07-01 \
  --run-mode BRAIN_AND_WEB_ACQUISITION_ENABLED \
  --brain-web-mode enabled \
  --research-brain-report-dir docs/operational \
  --brain-planner-provider codex_cli \
  --brain-source-acquisition live_full_bounded \
  --brain-universe-limit 1 \
  --brain-planner-success-limit 1 \
  --brain-planner-batch-size 1 \
  --brain-max-fetches-per-task 1 \
  --brain-claim-extractor-provider codex_cli \
  --brain-stage-promotion-mode strict \
  --full-thesis-smoke-mode disabled \
  --target-gate brain_web \
  --max-iterations 1 \
  --fail-on-run-mode-overclaim false \
  --fail-on-atomic-mismatch false \
  --fail-on-semantic-guard false \
  --fail-on-critical-audit false \
  --test-result-artifact output/test_full_repo_0701/full_unittest_result_artifact.json \
  --write-operational-docs false
```

결과:

```text
stdout = NOT_READY
process exit code = 1
runtime_seconds = 394.72초
```

이 실패는 정상이다. 이 run의 목적은 pass가 아니라, gate와 rejection ledger가 거짓 승격 없이 기록되는지 확인하는 것이다.

## 최신 산출물 교차검증

### 1. Stage / Score scope

검증 파일:

```text
output/census_v4/2026-07-01-brain-web-diagnostic-rawreject-v4/census_stage_summary.json
output/census_v4/2026-07-01-brain-web-diagnostic-rawreject-v4/acceptance_report.md
```

핵심:

```text
stage_scope_distribution:
  CENSUS_EVENT_BOARD = 3391

score_scope_distribution:
  NO_SCORE = 3324
  EVENT_WEIGHTED_PARTIAL = 67

operator_stage_use_distribution:
  NOT_FULL_THESIS_STAGE = 3391

operator_score_use_distribution:
  NOT_FULL_E2R_SCORE = 3391

canonical_stage_distribution:
  0 = 3306
  1 = 54
  2 = 30
  3-Red = 1

full_thesis_stage_row_count = 0
full_e2r_verified_score_row_count = 0
verified_score_present_count = 0
event_board_non_stage0_count = 85
```

해석:

```text
85개 non-Stage0 row는 event-board 상태 표시다.
운영자가 쓸 수 있는 full thesis Stage가 아니다.
```

### 2. Brain/Web gate

검증 파일:

```text
output/census_v4/2026-07-01-brain-web-diagnostic-rawreject-v4/brain_web_readiness_gate_audit.json
output/census_v4/2026-07-01-brain-web-diagnostic-rawreject-v4/brain_stage_promotion_audit.json
```

핵심:

```text
brain_web_readiness_gate_audit.verdict = BLOCKED
brain_stage_promotion_audit.verdict = BLOCKED

brain_accepted_claim_count = 0
official_accepted_claim_count = 0
web_news_accepted_claim_count = 0
llm_extracted_accepted_claim_count = 0
web_or_llm_accepted_claim_count = 0
brain_promoted_stage_row_count = 0

planner_run_row_count = 22
real_llm_planner_call_count = 2
feedback_retry_planner_run_count = 1
rejected_claim_feedback_count = 8
web_search_task_count = 6
web_search_call_count = 6
web_fetched_document_count = 10
web_rejected_document_count = 12
llm_claim_extractor_attempt_count = 10
```

해석:

```text
LLM/web 경로는 시도됐다.
하지만 accepted score claim으로 들어간 web/LLM claim은 0개다.
따라서 Brain/Web evidence pass도 아니고, BRAIN_WEB_PARTIAL promotion도 아니다.
```

planner count 주의:

```text
brain_web_readiness_gate_audit.json과 acceptance_report.md의 llm_planner_call_count=22는
실제 LLM provider 성공 호출 22회를 뜻하지 않는다.
planner_runs.jsonl 장부 행이 22개이고, 그중 real_provider_success=True는 2개다.
20개는 planner_not_attempted_after_real_planner_limit이다.
```

쉬운 예:

```text
출석부에는 22명이 적혀 있다.
하지만 실제 발표한 사람은 2명이다.
```

주의:

```text
source_task_executions.jsonl line count는 99개다.
하지만 readiness gate의 current Brain/Web attempt source_task_execution_count는 7개다.
파일에는 ledger refresh/copied leaf row가 같이 들어갈 수 있으므로 gate 숫자와 leaf file line count를 섞으면 안 된다.
```

### 3. Raw assertion rejection ledger

검증 파일:

```text
output/census_v4/2026-07-01-brain-web-diagnostic-rawreject-v4/raw_assertions.jsonl
output/census_v4/2026-07-01-brain-web-diagnostic-rawreject-v4/raw_assertion_rejections.jsonl
output/census_v4/2026-07-01-brain-web-diagnostic-rawreject-v4/brain_claim_mapping_trace.jsonl
```

핵심:

```text
raw_assertions = 151
raw_assertion_rejections = 62
brain_claim_mapping_trace = 61

rejection_reason:
  primitive_mapping_rejected = 29
  target_scope_or_directness_rejected = 27
  temporal_status_rejected = 5
  anchor_validation:quote_not_found_in_document_text = 1

mapping_status:
  REJECTED = 61
  None = 1

target_scope_status:
  DIRECT = 34
  UNRELATED = 27
  None = 1

directness:
  DIRECT = 34
  NOT_TARGET_SCOPED = 27
  None = 1

temporal_status:
  CURRENT = 55
  HISTORICAL = 4
  UNKNOWN = 2
  None = 1

semantic_status:
  REJECTED = 32
  PASS = 29
  None = 1

support_direction:
  NEUTRAL = 60
  SUPPORT = 1
  None = 1
```

가장 중요한 해석:

```text
탈락 사유가 더 세분화됐다.
primitive mapping 실패 29건, wrong-subject/directness 실패 27건, historical/temporal 실패 5건이다.
즉 다음 병목은 두 갈래다.

1. target/directness가 틀린 문서를 덜 가져오게 source task/query를 바꿔야 한다.
2. DIRECT/CURRENT/PASS인데 mapping이 막힌 문장은 더 직접적인 primitive evidence를 찾도록 retry해야 한다.
```

쉬운 예:

```text
뉴스에서 "신규 시설투자 정정"을 읽었다.
이 문장은 대상 회사와 현재 문서일 수 있다.
하지만 이것만으로 "volume growth visible"이나 "operating leverage visible" 점수를 줄 수는 없다.

그래서 raw assertion은 존재하지만 score claim은 0개가 된다.
```

## v2와 v4 숫자 차이를 어떻게 읽어야 하나

여기서 `accepted_claims`는 Evidence OS bundle 내부 claim 총량을 말한다.
운영 Brain/Web 승격 gate가 요구하는 `brain_accepted_claim_count`,
`official_accepted_claim_count`, `web_or_llm_accepted_claim_count`와 같은 뜻이 아니다.

쉬운 예:

```text
창고에 claim 박스가 92개 있다.
하지만 오늘 Brain/Web 심사대에서 점수표에 올려도 된다고 승인된 웹/LLM claim은 0개다.
그래서 accepted_claims=92와 web_or_llm_accepted_claim_count=0은 동시에 참일 수 있다.
```

`rawreject-v2`:

```text
accepted_claims = 93
raw_assertions = 151
raw_assertion_rejections = 58
claim_extractor_runs = 7
web_fetched_documents = 7
web_rejected_documents = 11
brain_accepted_claim_count = 1
official_accepted_claim_count = 1
web_or_llm_accepted_claim_count = 0
```

`rawreject-v4`:

```text
accepted_claims = 92
raw_assertions = 151
  RAWPROD = 92
  RAWLLM = 57
  RAWASSERTV4 = 2
claim_extractor_raw_assertion_ids = 60
claim_extractor_unique_raw_assertion_ids = 58
raw_assertion_rejections = 62
claim_extractor_runs = 10
web_fetched_documents = 10
web_rejected_documents = 12
brain_accepted_claim_count = 0
official_accepted_claim_count = 0
web_or_llm_accepted_claim_count = 0
feedback_retry_planner_run_count = 1
rejected_claim_feedback_count = 8
```

이 둘은 live LLM/web diagnostic이라 source corpus와 provider response가 달라질 수 있다. 점수 전후 비교처럼 읽으면 안 된다.

비교해야 할 invariant는 이것이다:

```text
FULL_THESIS row = 0
FULL_E2R_100 verified score row = 0
BRAIN_WEB_PARTIAL row = 0
web_or_llm_accepted_claim_count = 0
brain_stage_promotion = BLOCKED
raw_assertion_rejections > 0
```

쉬운 예:

```text
v2는 7장을 읽고 58개 탈락 사유를 남겼다.
v4는 10장을 읽고 62개 탈락 사유를 남겼고, 그중 8개를 planner feedback retry에 넣었다.

두 run 모두 "웹 증거로 점수 채택"은 0개다.
그래서 둘 다 운영 Stage 준비 완료가 아니다.
```

## 현재 뭐가 잘못되고 있나

목표 관점에서는 아직 잘못된 상태가 맞다.

```text
목표:
  실제 운영 파이프라인에서 web/official/LLM 증거를 claim으로 만들고,
  그 claim으로 full thesis score/stage를 결정한다.

현재:
  Census 상태판 Stage는 있다.
  기존 ledger/event partial score는 있다.
  하지만 Brain/Web이 새 web/LLM accepted claim을 만들지 못한다.
  full thesis score/stage는 0개다.
```

다만 이전보다 좋아진 부분도 명확하다.

```text
이전 문제:
  official-only claim이 Brain/Web partial로 포장될 수 있었다.
  web raw assertion이 왜 탈락했는지 assertion 단위로 보이지 않았다.

현재:
  official-only promotion은 막혔다.
  raw assertion 탈락 사유가 장부에 남는다.
```

즉 현재 상태는:

```text
거짓 합격은 막았다.
진짜 합격자는 아직 못 만들었다.
```

## 다음 에이전트가 공격해야 할 지점

### P0-1. Primitive mapping rejection 29건의 원인 분해

현재 rawreject-v4의 가장 큰 단일 탈락 사유는 `primitive_mapping_rejected=29`다.

다음 질문:

```text
1. SourceTask의 primitive_gap이 너무 넓거나 틀렸나?
2. LLM extractor가 사실은 잘 뽑았는데 primitive_mapper가 너무 좁게 막았나?
3. LLM이 neutral mention만 많이 뽑고 점수 primitive에 필요한 bridge claim은 못 뽑았나?
4. planner가 missing primitive를 보고도 같은 종류의 관련 없는 뉴스만 가져오고 있나?
```

절대 하면 안 되는 패치:

```text
primitive_mapping_rejected가 많으니 mapping 기준을 낮춘다.
```

해야 하는 패치:

```text
rejection_reason을 planner feedback context로 되돌려 LLM planner가 다음 검색/소스 선택을 바꾸게 한다.
예: "CURRENT/DIRECT/PASS 문장은 찾았지만 mapping이 NEUTRAL이라 score claim이 0개다.
     operating leverage를 직접 뒷받침하는 매출/마진/가동률/수주 전환 evidence를 찾아라."
```

현재 완료된 부분:

```text
rawreject-v4에서 rejected_claim_feedback_count = 8
feedback_retry_planner_run_count = 1

claim별 raw_assertion_rejections의 rejection_reason이 execution 단위 not_eligible_reasons보다 우선해
planner feedback retry context에 들어간다.
```

남은 부분:

```text
feedback retry가 실행됐지만 accepted web/LLM claim은 아직 0개다.
다음 패치는 retry output의 SourceTask가 실제로 이전 실패 유형을 피했는지,
그리고 피하지 못했다면 planner prompt/schema를 더 강하게 고쳐야 한다.
```

### P0-2. Rejection row enrichment

fallback rejection row에는 아직 일부 축이 비어 있다.

rawreject-v4 기준:

```text
verification_status = SEMANTIC_VERIFIED 61건, None 1건
source_type = None
provider_mode = None
origin_type = None
```

추가 무결성 gap:

```text
raw_assertion_rejections 62건 중
  raw_assertions.jsonl에 없는 raw_assertion_id = 1건
  같은 raw_assertion_id가 중복 rejection row로 남는 사례 = 2개 id
```

이 gap은 다음 패치에서 의미를 분리해야 한다.

```text
선택지 A:
  anchor validation 실패 raw도 raw_assertions.jsonl에 materialize한다.

선택지 B:
  raw_assertion_rejections는 rejection_id 기준 ledger이고,
  raw_assertion_id는 중복될 수 있는 input assertion reference라고 명시한다.
```

다음 패치:

```text
raw_assertion_rejections fallback 생성 시
adjudicated_claims / evidence_documents / raw_assertions / claim_extractor_runs를 join해서
verification_status, source_type, provider_mode, published_at, exact_quote/hash 상태를 채운다.
raw_assertion_id idempotency 규칙도 명확히 한다.
```

쉬운 예:

```text
"왜 탈락했나"만으로는 부족하다.
"어디서 온 어떤 문장이고, LLM에서 온 건지 공식 API에서 온 건지"까지 보여야 한다.
```

### P0-3. Rejection-driven retry loop

현재는 rejection이 장부에 남고, 일부 사유는 다음 검색 계획으로 들어간다.
하지만 accepted claim이 0개라서 아직 충분하지 않다.

필요한 흐름:

```text
raw assertion rejected:
  primitive_mapping_rejected
  target_scope_or_directness_rejected
  temporal_status_rejected

↓

score_gap_context에 축별 사유 주입

↓

LLM planner가 새 SourceTask 생성

↓

같은 실패 유형 반복 시 task 종료 또는 source class 변경
```

쉬운 예:

```text
5개 문서가 모두 "시설투자 정정"만 말하고 매출/마진 전환을 말하지 않았다.
그러면 다음 query는 시설투자 뉴스를 더 긁는 게 아니라,
실적발표/IR/수주/가동률/마진 bridge를 찾는 쪽으로 바뀌어야 한다.
```

### P0-4. Accepted web/LLM claim unblock

현재 cutover를 막는 직접 이유:

```text
web_or_llm_accepted_claim_count = 0
minimum_required web_or_llm_accepted_claim_count = 3
```

다음 성공 조건:

```text
web/LLM accepted claim >= 3
claim-backed score contribution 존재
StageCourt trace가 해당 claim ids를 참조
BRAIN_WEB_PARTIAL promotion이 strict mode에서 PROMOTION_APPLIED
```

주의:

```text
이 숫자를 0으로 낮추면 안 된다.
accepted claim이 실제로 생기게 해야 한다.
```

### P0-5. Planner prompt/response leaf logging

rawreject-v4에서 planner는 실행됐고 feedback retry도 남았다.

```text
planner_run_row_count = 22
real_llm_planner_call_count = 2
feedback_retry_planner_run_count = 1
llm_prompts.jsonl rows = 0
llm_responses.jsonl rows = 0
```

rawreject-v4 산출물만 보면 아직 운영 감사 관점에서 부족하다.
다만 promptleaf-v1 코드 패치로 새 실행에서는 leaf를 쓸 수 있게 됐다.

코드 패치 후 기대 경로:

```text
PlannerRunV4:
  planner_run_id
  prompt_hash
  response_hash
  raw_prompt_path
  raw_response_path

Census export:
  llm_prompts.jsonl
  llm_responses.jsonl
  planner_raw/prompts/*.json
  planner_raw/responses/*.json
```

검증:

```text
targeted regression = Ran 63 tests / OK
full regression = Ran 5008 tests / OK
```

쉬운 예:

```text
전에는 성적표에 "선생님이 재채점했다"만 남아 있었다.
이제는 재채점 때 선생님에게 보여준 문제지와 답안지 파일 경로/hash도 남길 수 있다.
```

남은 패치:

```text
rawreject-v4 live diagnostic을 promptleaf-v1 코드로 재실행한다.
llm_prompts.jsonl / llm_responses.jsonl row 수가 real planner success/retry와 맞는지 확인한다.
feedback retry prompt 원문에 rejected_claim_feedback이 실제 들어갔는지 artifact에서 검증한다.
```

주의:

```text
prompt/response leaf를 추가하더라도 score/stage는 여전히 LLM이 직접 만들면 안 된다.
기록 목적은 감사와 재현성이다.
```

### P0-6. Full thesis와 all-archetype replay는 여전히 별도 문제

canonical all-archetype replay:

```text
required_archetype_count = 32
source_backed_ready_count = 6
missing_required_archetype_count = 26
```

즉 Brain/Web accepted claim을 뚫어도 바로 goal complete가 아니다.

최종 목표:

```text
1. Brain/Web accepted claim 생성
2. BRAIN_WEB_PARTIAL strict promotion 검증
3. Full thesis smoke/prod row 생성
4. C01~C32 source-backed positive/guard replay parity 확보
5. FULL_E2R_100 verified score/stage 생성
```

## 다음 리뷰어용 공격 질문

아래 질문에 통과하지 못하면 아직 운영 준비가 아니다.

```text
1. Stage1/Stage2 row 85개를 운영 Stage로 오해할 여지가 완전히 차단됐나?
2. BRAIN_WEB_PARTIAL row가 생겼다면 그 row의 StageCourt trace가 web/LLM accepted claim ids를 직접 참조하나?
3. raw_assertion_rejections의 rejection_reason은 row 자체의 target/temporal/semantic/mapping 축과 일관되나?
4. 같은 문서 안 다른 assertion의 eligibility reason이 한 assertion의 rejection_reason을 오염시키지 않나?
5. primitive_mapping_rejected가 다음 LLM planner retry의 score_gap_context로 들어가나?
6. source task가 같은 실패 유형을 반복할 때 stop/change-source 조건이 있나?
7. official-only accepted claim이 web/LLM metric에 섞이지 않나?
8. source_task_executions leaf count와 Brain/Web current attempt count를 문서가 섞어 말하지 않나?
9. FULL_THESIS row가 0인 상태에서 readiness report가 pass처럼 보이는 문구를 내지 않나?
10. all-archetype 26개 missing replay를 숨기지 않나?
11. CensusAssessmentEvent / CandidateEvent / CensusEvent 자체가 score evidence로 쓰이지 않나?
12. EVENT_WEIGHTED_PARTIAL nonzero row가 accepted_claim_id 없이 만들어지지 않나?
13. score_contribution_without_accepted_claim_support_count가 0으로 유지되나?
```

## 최종 판단

```text
현재는 운영 Stage가 있는 상태가 아니다.
그러나 이전처럼 거짓으로 있는 척하는 상태도 아니다.

Stage board는 있고, full thesis 채점지는 없다.
웹/LLM은 문서를 읽고 raw assertion을 만들지만, score claim 채택은 아직 0개다.
raw assertion rejection ledger가 생겼으므로 이제 다음 패치는 감으로 고치는 게 아니라
탈락 사유 분포를 보고 acquisition / extraction / mapping / retry loop를 고쳐야 한다.
```
