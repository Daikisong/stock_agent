# Census v4 0701 Stage Scope Current Truth / Next Patch Attack Packet

작성 시점: 2026-07-02 KST  
repo: `/home/eorb915/projects/stock_agent`  
canonical output: `output/census_v4/2026-07-01`  
as_of_date: `2026-07-01`

이 문서는 다음 에이전트가 가장 먼저 공격적으로 검토해야 하는 최신 상태 진단서다.

2026-07-02 추가 교차검증:

```text
이 문서의 Brain/Web 보조 진단 일부는 schema-v2 기준으로 작성됐다.
그 뒤 feedback-v1 diagnostic이 추가 실행됐다.

최신 Brain/Web 수치와 다음 패치 공격 지점은 아래 문서를 우선한다.
docs/0701/census_v4_0701_brain_web_metric_split_patch_result_2026-07-02.md
docs/0701/census_v4_0701_next_agent_hard_review_after_metricsplit_2026-07-02.md
```

`schema-v2`는 Codex extractor schema 오류가 해결됐음을 보여 주는 직전 증거로 남긴다.
`feedback-v1`은 post-extraction rejection ledger가 비어 있던 직전 진단이다.
`postextract-v1`은 web rejection ledger가 생긴 진단이다.
최신 상태 판단은 `metricsplit-v1` 기준으로 읽는다.

## 한 줄 결론

```text
Stage가 있는 애들은 있다.
하지만 운영 FULL_THESIS Stage가 있는 애들은 현재 canonical output 기준 0개다.
```

정확히 말하면:

```text
Stage1/Stage2-Watch/Red = 85개
전부 stage_scope = CENSUS_EVENT_BOARD

FULL_THESIS row = 0개
FULL_E2R_100 verified score row = 0개
Brain/Web evidence pass = false
goal_completion_ready = false
```

최신 Brain/Web 보조 진단까지 포함하면:

```text
output/census_v4/2026-07-01-brain-web-diagnostic-metricsplit-v1
  BRAIN_WEB_PARTIAL row = 1개
  FULL_THESIS row = 0개
  FULL_E2R_100 verified score row = 0개
  operator_stage_use = NOT_FULL_THESIS_STAGE 3391개
  verdict = NOT_READY
  accepted web/news score claim = 0개
  brain_accepted_claim_count = 1개
  official_accepted_claim_count = 1개
  web_or_llm_accepted_claim_count = 0개
  web_rejected_documents = 5개
```

따라서 더 정확한 답은 이렇다.

```text
상태판 Stage는 있다.
metricsplit 최신 진단에서는 Brain/Web partial Stage 1개가 있지만 official-only accepted claim 기반이라
web/LLM accepted claim은 0개다.
하지만 운영 FULL_THESIS Stage는 아직 0개다.
```

쉬운 예:

```text
지금 있는 Stage는 "출석부 상태 표시"에 가깝다.
예: 이 학생은 오늘 상담 필요, 자료 부족, 확인 완료.

우리가 원하는 운영 Stage는 "기말고사 채점지"에 가깝다.
예: 이 학생은 전 과목 답안과 근거가 있어서 87점, Yellow.

현재 출석부는 3391명 전부 있다.
하지만 기말고사 채점지는 0명이다.
```

## 왜 이 문서를 새로 썼나

`docs/0701`에는 중간 스냅샷 문서가 많다. 예전 문서에는 다음처럼 당시에는 맞았지만 지금은 superseded된 숫자가 남아 있을 수 있다.

```text
source_backed_ready_count = 0 / 1 / 3 / 4 / 5
controlled_semantic pass_count = 4 / 5 / 7 / 8 / 9
test_count = 4942 / 4951 / 4954 / 4957 / 4959 / 4975 / 4983 / 4992 / 4996
```

이 문서의 기준은 최신 canonical 산출물과 C28 패치 이후 상태다.

```text
source_backed_ready_count = 6
guard_replay_ready_count = 6
missing_required_archetype_count = 26
controlled_semantic_replay_pass = true
controlled_semantic pass_count = 10
controlled_semantic pending_count = 0
full unittest artifact test_count = 4997
```

### 숫자 해석 주의

`all_archetype_replay_matrix.json`은 총 36개 row를 가진다.

```text
required archetype = C01~C32, 32개
cross-archetype guard contract = R13_*, 4개
total archetype rows = 36개
```

따라서 다음 두 숫자는 모순이 아니다.

```text
missing_required_archetype_count = 26
R13_*까지 포함해 ready가 아닌 row = 30
```

해석:

```text
goal completion에서 요구하는 source-backed replay parity는 C01~C32 32개 기준이다.
R13_* 4개는 cross-archetype guard contract row라서
required_before_goal_completion=false로 기록되어 있다.
```

쉬운 예:

```text
본시험 과목은 32개다.
감독관 체크리스트 4개가 별도로 있다.
본시험 미완료는 26개이고, 감독관 체크리스트까지 세면 미완료처럼 보이는 row는 30개다.
```

## 교차검증한 파일

직접 대조한 산출물:

```text
output/census_v4/2026-07-01/acceptance_report.md
output/census_v4/2026-07-01/operator_digest.md
output/census_v4/2026-07-01/census_stage_summary.json
output/census_v4/2026-07-01/census_stage_status.jsonl
output/census_v4/2026-07-01/goal_completion_audit.json
output/census_v4/2026-07-01/goal_requirement_matrix_audit.json
output/census_v4/2026-07-01/readiness_verdict.json
output/census_v4/2026-07-01/brain_web_attempt_audit.json
output/census_v4/2026-07-01/brain_web_readiness_gate_audit.json
output/census_v4/2026-07-01/brain_stage_promotion_audit.json
output/census_v4/2026-07-01/full_thesis_production_audit.json
output/census_v4/2026-07-01/samsung_hynix_full_thesis_smoke.json
output/census_v4/2026-07-01/samsung_hynix_full_thesis_smoke_audit.json
output/census_v4/2026-07-01/all_archetype_replay_matrix.json
output/census_v4/2026-07-01-brain-web-diagnostic-schema-v2/acceptance_report.md
output/census_v4/2026-07-01-brain-web-diagnostic-schema-v2/readiness_verdict.json
output/census_v4/2026-07-01-brain-web-diagnostic-schema-v2/brain_web_attempt_audit.json
output/census_v4/2026-07-01-brain-web-diagnostic-schema-v2/brain_web_readiness_gate_audit.json
output/census_v4/2026-07-01-brain-web-diagnostic-schema-v2/brain_stage_promotion_audit.json
output/census_v4/2026-07-01-brain-web-diagnostic-schema-v2/claim_extractor_runs.jsonl
output/census_v4/2026-07-01-brain-web-diagnostic-schema-v2/raw_assertions.jsonl
output/census_v4/2026-07-01-brain-web-diagnostic-schema-v2/accepted_claims.jsonl
output/census_v4/2026-07-01-brain-web-diagnostic-feedback-v1/acceptance_report.md
output/census_v4/2026-07-01-brain-web-diagnostic-feedback-v1/readiness_verdict.json
output/census_v4/2026-07-01-brain-web-diagnostic-feedback-v1/brain_web_attempt_audit.json
output/census_v4/2026-07-01-brain-web-diagnostic-feedback-v1/brain_web_readiness_gate_audit.json
output/census_v4/2026-07-01-brain-web-diagnostic-feedback-v1/planner_runs.jsonl
output/census_v4/2026-07-01-brain-web-diagnostic-feedback-v1/source_task_executions.jsonl
output/census_v4/2026-07-01-brain-web-diagnostic-feedback-v1/web_fetched_documents.jsonl
output/census_v4/2026-07-01-brain-web-diagnostic-feedback-v1/web_rejected_documents.jsonl
output/census_v4/2026-07-01-brain-web-diagnostic-feedback-v1/claim_extractor_runs.jsonl
output/census_v4/2026-07-01-brain-web-diagnostic-feedback-v1/raw_assertions.jsonl
output/census_v4/2026-07-01-brain-web-diagnostic-feedback-v1/accepted_claims.jsonl
```

직접 대조한 코드/테스트:

```text
src/e2r/census/census_runner_v4.py
src/e2r/census/census_v4_auditor.py
tests/test_census_v4_full_thesis_smoke_tasks.py
tests/test_census_v4_brain_stage_promotion_gate.py
tests/test_census_v4_goal_required_audits.py
tests/test_census_v4_run_mode_honesty.py
src/e2r/production/claim_extraction/extractor_provider.py
tests/test_cutover_contract_blind_extraction.py
```

## 현재 Stage 분포

`census_stage_status.jsonl` 직접 집계:

```text
rows = 3391

base_stage:
  Stage0 = 3306
  Stage1 = 54
  Stage2-Watch = 30
  Red = 1

canonical_stage:
  0 = 3306
  1 = 54
  2 = 30
  3-Red = 1

stage_scope:
  CENSUS_EVENT_BOARD = 3391

operator_stage_use:
  NOT_FULL_THESIS_STAGE = 3391

full_thesis_stage:
  FULL_THESIS_NOT_RUN = 3391

score_scope:
  NO_SCORE = 3324
  EVENT_WEIGHTED_PARTIAL = 67
  FULL_E2R_100 = 0

candidate_event_scope:
  ASSESSMENT_ONLY = 3306
  CANDIDATE_EVENTS_PRESENT = 85

operator scope warning:
  stage_scope_notice = NO_FULL_THESIS_STAGE_ROWS_EVENT_BOARD_STAGE_ROWS_EXIST
  operational_stage_use_allowed = false
  event_board_stage_rows_are_operational_full_thesis = false
```

해석:

```text
Stage0 3306개:
  현재 catalyst가 확인되지 않은 Census 상태판 row다.
  나쁜 종목이라서 E2R 0점이라는 뜻이 아니다.

Stage1 54개:
  공식 이벤트나 source pending 신호가 있는 daily/event-board row다.
  전체 아키타입 thesis Stage1이 아니다.

Stage2-Watch 30개:
  material claim watch row다.
  multi-source, cash/revision, Green gate가 닫힌 full thesis Stage2가 아니다.

Red 1개:
  event-board risk review row다.
  기존 thesis가 깨져 4C로 전이된 full thesis hard break와 같은 뜻이 아니다.
```

쉬운 예:

```text
단일판매공급계약 공시 하나가 있으면 Stage2-Watch 상태판은 가능하다.
하지만 그 계약이 수주잔고, 마진, FCF, EPS revision까지 이어졌는지 확인하지 않았으면
운영 Green/Yellow thesis Stage로 쓰면 안 된다.
```

## 현재 Score 분포

직접 집계:

```text
score_valid_status:
  NO_CURRENT_EVENT = 3306
  FINAL_WITH_NONMATERIAL_GAPS = 37
  PENDING_MATERIAL_GAPS = 30
  NOT_SCORED = 11
  INVALID_EVIDENCE = 7

stage_decision_status:
  NO_CURRENT_CATALYST = 3306
  FINAL = 36
  PENDING_MATERIAL_GAPS = 30
  SOURCE_PENDING = 18
  RISK_REVIEW = 1

accepted_claims.jsonl = 92 rows
score_contributions.jsonl = 92 rows
stagecourt_traces.jsonl = 92 rows
source_tasks.jsonl = 92 rows
source_task_executions.jsonl = 92 rows

web_search_tasks.jsonl = 0 rows
web_fetched_documents.jsonl = 0 rows
```

해석:

```text
현재 67개 event score row는 EVENT_WEIGHTED_PARTIAL이다.
FULL_E2R_100 점수는 없다.
Brain/Web이 새로 웹 문서를 fetch해서 Stage까지 올린 row도 없다.
```

## 최신 Brain/Web 보조 진단

canonical output은 Brain/Web disabled라서 `NOT_REQUESTED`가 맞다.
그래서 별도 output root에서 Brain/Web enabled diagnostic을 다시 돌렸다.

### 실행

```bash
PYTHONPATH=src python -m e2r.cli.run_e2r_census_v4_until_pass \
  --as-of-date 2026-07-01 \
  --universe krx \
  --output-root output/census_v4/2026-07-01-brain-web-diagnostic-schema-v2 \
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
runtime_seconds = 185.08
```

### Stage/Score 분포

`census_stage_status.jsonl` 직접 집계:

```text
rows = 3391

stage_scope:
  CENSUS_EVENT_BOARD = 3390
  BRAIN_WEB_PARTIAL = 1
  FULL_THESIS = 0

operator_stage_use:
  NOT_FULL_THESIS_STAGE = 3391

full_thesis_stage:
  FULL_THESIS_NOT_RUN = 3391

score_scope:
  NO_SCORE = 3323
  EVENT_WEIGHTED_PARTIAL = 67
  BRAIN_WEB_CLAIM_BACKED_PARTIAL = 1
  FULL_E2R_100 = 0

base_stage:
  Stage0 = 3306
  Stage1 = 53
  Stage2-Watch = 30
  0 = 1
  Red = 1

canonical_stage:
  0 = 3307
  1 = 53
  2 = 30
  3-Red = 1
```

`BRAIN_WEB_PARTIAL` 1개:

```text
symbol = 003090
company_name = 대웅
stage_scope = BRAIN_WEB_PARTIAL
operator_stage_use = NOT_FULL_THESIS_STAGE
full_thesis_stage = FULL_THESIS_NOT_RUN
score_scope = BRAIN_WEB_CLAIM_BACKED_PARTIAL
base_stage = 0
canonical_stage = 0
accepted_claim_count = 1
score_contribution_count = 5
stagecourt_trace_id = SCT-BRAIN-b83dbf04df6d4b548367
primary_archetype = C05_EPC_MEGA_CONTRACT_MARGIN_GAP
operator_scope_note = brain_web_claim_backed_partial_not_full_thesis
```

해석:

```text
대웅 1개 row는 Brain/Web partial trace가 닫힌 것이다.
하지만 full thesis Stage가 아니고, 운영자가 Stage로 쓰면 안 된다.
```

쉬운 예:

```text
부분 면담 기록 1장이 생겼다.
하지만 전 과목 성적표가 나온 것은 아니다.
```

### Brain/Web readiness gate (`schema-v2` snapshot)

`output/census_v4/2026-07-01-brain-web-diagnostic-schema-v2/brain_web_readiness_gate_audit.json` 기준:

```text
verdict = BLOCKED
brain_web_evidence_pass_allowed = false

planner_run_count = 21 / required 30
web_search_task_count = 3 / required 20
web_search_call_count = 3 / required 20
web_fetched_document_count = 4 / required 10
llm_claim_extractor_attempt_count = 4 / required 10
web_or_llm_accepted_claim_count = 1 / required 3

brain_score_contribution_count = 5
brain_stage_trace_count = 1
brain_promoted_stage_row_count = 1
```

해석:

```text
실제 provider/source/extractor/partial promotion은 돌았다.
하지만 operational minimum을 못 채워서 Brain/Web evidence pass는 false다.
```

### LLM extractor 상태

이전 `schema` diagnostic에서는 Codex extractor가 4/4 `PROVIDER_FAILED`였다.
원인은 Codex structured output schema가 엄격 schema 요구사항을 만족하지 못했기 때문이다.

구체 오류:

```text
invalid_json_schema:
required is required to be supplied and to be an array including every key in properties.
Missing 'uncertainty_reason'.
```

적용한 최소 패치:

```text
src/e2r/production/claim_extraction/extractor_provider.py
  - EXTRACTOR_OUTPUT_SCHEMA에서 event_date / uncertainty_reason을 null union이 아닌 string으로 변경
  - uncertainty_reason을 required에 추가
  - unknown predicate는 계속 mention_only로 downgrade

tests/test_cutover_contract_blind_extraction.py
  - schema properties와 required가 동일해야 함을 테스트
  - event_date / uncertainty_reason type이 string임을 테스트
```

검증:

```text
PYTHONPATH=src python -m unittest \
  tests.test_cutover_contract_blind_extraction \
  tests.test_research_brain_v4_evidence_extraction_from_real_document -v

Ran 22 tests
OK
```

직접 Codex smoke:

```text
provider_error = None
raw_assertion_count = 1
predicate = customer_allocation_or_qualification_claim
```

`schema-v2` diagnostic:

```text
claim_extractor_runs.jsonl = 4 rows
status:
  SUCCESS = 4
provider_error_count = 0
raw_assertion_count total = 29
```

중요:

```text
LLM extractor는 이제 성공한다.
하지만 `schema-v2` 기준 LLM raw assertion 29개는 accepted_claims.jsonl에 들어간 score claim이 아니다.
accepted_claims.jsonl의 Brain/Web 추가 accepted 1건은 RAWASSERTV4 OpenDART 구조화 claim이다.
```

왜 LLM claim이 accepted되지 않았나:

```text
source_task_executions.jsonl의 대웅 web task:
  status = NO_EVIDENCE_FOUND
  rejected_claim_count = 29
  accepted_claim_ids = []
  not_eligible_reasons:
    mapping_not_accepted:REJECTED
    primitive_mapping_rejected:no_allowed_primitive_for_predicate
    semantic_rejected
    target_scope_not_allowed:UNRELATED
    target_not_direct:NOT_TARGET_SCOPED
    temporal_not_allowed:HISTORICAL
    primitive_mapping_rejected:normal_or_positive_audit_is_not_trust_break
```

해석:

```text
LLM이 문장을 뽑기는 했다.
하지만 그 문장들은 대부분 시세/공시목록/기업개요/자회사 언급/과거 공시 제목이었다.
대상 primitive gap인 subsidy_capture_visible 같은 score claim으로 인정되지는 않았다.
```

쉬운 예:

```text
"대웅 현재가 17,380원"
  -> 실제 문장이지만 full thesis 점수 재료 아님.

"대웅 자회사 신규시설투자 정정 공시 제목"
  -> 후속 조사 단서일 수는 있지만 곧바로 positive capacity/subsidy score는 아님.

"대웅제약은 나보타를 보유"
  -> 대웅 자체 score claim으로 직접 귀속하면 안 됨.
```

### 최신 diagnostic 결론

```text
고친 것:
  Codex extractor schema failure는 해결했다.
  LLM provider가 실제로 raw assertion을 만들었다.

아직 못 고친 것:
  LLM raw assertion이 score-eligible primitive claim으로 연결되지 않는다.
  web search/fetch/extractor/accepted claim operational minimum이 부족하다.
  promoted row도 BRAIN_WEB_PARTIAL이지 FULL_THESIS가 아니다.

따라서 현재 Brain/Web은 "작동 흔적 있음"이지 "운영 Stage 가능"이 아니다.
```

쉬운 예:

```text
EVENT_WEIGHTED_PARTIAL:
  "오늘 확인된 공식 이벤트 하나의 상태 점수"

FULL_E2R_100:
  "아키타입 전체 채점표를 claim-backed primitive로 채운 운영 점수"

현재는 첫 번째만 일부 있고, 두 번째는 0개다.
```

## 이번 P0 패치 반영 상태

이번 패치로 “Stage가 보이지만 운영 Stage는 아니다”를 문서에만 적어둔 것이 아니라, leaf audit / summary / readiness / report에 기계 필드로 고정했다.

반영 파일:

```text
src/e2r/census/census_runner_v4.py
src/e2r/census/census_v4_auditor.py
tests/test_census_v4_report_generated_from_leaf_audit.py
tests/test_census_v4_full_thesis_smoke_tasks.py
```

새로 고정된 output 필드:

```text
readiness_verdict.json:
  stage_scope_notice = NO_FULL_THESIS_STAGE_ROWS_EVENT_BOARD_STAGE_ROWS_EXIST
  operational_stage_use_allowed = false
  full_thesis_stage_row_count = 0
  full_e2r_verified_score_row_count = 0
  event_board_non_stage0_count = 85
  event_board_stage_rows_are_operational_full_thesis = false

census_stage_summary.json:
  full_thesis_stage_row_count = 0
  full_e2r_verified_score_row_count = 0
  event_board_stage_row_count = 3391
  event_board_non_stage0_count = 85
  operator_stage_scope_notice = NO_FULL_THESIS_STAGE_ROWS_EVENT_BOARD_STAGE_ROWS_EXIST

leaf_artifact_audit.json.metrics:
  full_thesis_stage_row_count = 0
  full_e2r_verified_score_present_count = 0
  event_board_stage_row_count = 3391
  event_board_non_stage0_count = 85
  operator_stage_scope_notice = NO_FULL_THESIS_STAGE_ROWS_EVENT_BOARD_STAGE_ROWS_EXIST
```

`acceptance_report.md` 최상단도 이제 0번 경고를 먼저 출력한다.

```text
0. Operator stage warning:
  stage_scope_notice=NO_FULL_THESIS_STAGE_ROWS_EVENT_BOARD_STAGE_ROWS_EXIST
  operational_stage_use_allowed=False
  full_thesis_rows=0
  full_e2r_verified_score_rows=0
  event_board_non_stage0_rows=85
  event_board_stage_rows_are_operational_full_thesis=False
```

쉬운 예:

```text
이전:
  성적표 첫 줄에 "Stage1/Stage2 있음"만 보여서 실제 성적처럼 오해할 수 있었다.

패치 후:
  성적표 첫 줄에 "이건 출석부 상태표이고, 정식 기말고사 점수는 0명"이라고 박아둔다.
```

검증 결과:

```text
PYTHONPATH=src python -m unittest \
  tests.test_census_v4_report_generated_from_leaf_audit \
  tests.test_census_v4_full_thesis_smoke_tasks \
  tests.test_census_v4_run_mode_honesty \
  tests.test_census_v4_score_field_split \
  tests.test_census_v4_stage_signal_split -v

result = OK, 40 tests

PYTHONPATH=src python -m unittest $(rg --files tests | rg 'tests/test_census_v4_.*\.py$' | sed 's#/#.#g; s#\.py$##') -v

result = OK, 116 tests

PYTHONPATH=src python -m e2r.cli.run_test_command_with_artifact \
  --artifact output/test_full_repo_0701/full_unittest_result_artifact.json \
  --log output/test_full_repo_0701/full_unittest_result_artifact.log \
  -- python -m unittest discover -s tests -v

result = OK, 4997 tests
duration_seconds = 175.633
artifact_sha256 = de58aefb7bbd19b75f324560c6a06bbca397af4e2470f8c5a64ed89491d3eb49
log_sha256 = 239ab6e199336486ffec25d3e6cb34a5487eaefd1db21e2bc3ccddde53de9839
```

canonical output도 최신 artifact로 다시 생성했다.

```bash
PYTHONPATH=src python -m e2r.cli.run_e2r_census_v4_until_pass \
  --as-of-date 2026-07-01 \
  --output-root output/census_v4/2026-07-01 \
  --v3-output-root output/census_v3/2026-07-01 \
  --target-gate anti_fake \
  --test-result-artifact output/test_full_repo_0701/full_unittest_result_artifact.json

result = ANTI_FAKE_FULL_UNIVERSE_STATUS_PASS
```

동기화 확인:

```text
output/census_v4/2026-07-01/test_result_artifact.json
output/test_full_repo_0701/full_unittest_result_artifact.json

test_result_artifact_file_sha256 = de58aefb7bbd19b75f324560c6a06bbca397af4e2470f8c5a64ed89491d3eb49
artifact_json_cmp = identical
```

주의:

```text
test_result_artifact.json 안의 log_path/log_sha256은
output/test_full_repo_0701/full_unittest_result_artifact.log를 가리킨다.

output/census_v4/2026-07-01/test_result_artifact.log는 별도 복사/생성 로그라서
외부 full-test log와 byte-identical이라고 전제하면 안 된다.

확정 증거는 JSON artifact 자체가 byte-identical이고,
JSON 내부 artifact_status=OK, test_count=4997, log_sha256=239ab6... 이라는 점이다.
```

## 삼성전자 / SK하이닉스 현재 truth

현재 canonical output에서 삼성전자와 SK하이닉스는 HBM/C06 full thesis 평가가 아니다.

### 삼성전자 `005930`

```text
base_stage = Stage1
canonical_stage = 1
stage_scope = CENSUS_EVENT_BOARD
operator_stage_use = NOT_FULL_THESIS_STAGE
score_scope = EVENT_WEIGHTED_PARTIAL
full_thesis_stage = FULL_THESIS_NOT_RUN
full_e2r_verified_score = null
primary_archetype = C05_EPC_MEGA_CONTRACT_MARGIN_GAP
accepted_claim_count = 1
score_contribution_count = 1
stage_signal = OFFICIAL_EVENT_WATCH
full_thesis_missing_primitives = ["full_thesis_refresh_task_not_run"]
```

해석:

```text
이 row는 삼성전자 HBM/C06 운영 점수가 아니다.
DART 해명/공식 이벤트 1개를 상태판에 올린 것이다.
```

### SK하이닉스 `000660`

```text
base_stage = Stage1
canonical_stage = 1
stage_scope = CENSUS_EVENT_BOARD
operator_stage_use = NOT_FULL_THESIS_STAGE
score_scope = EVENT_WEIGHTED_PARTIAL
full_thesis_stage = FULL_THESIS_NOT_RUN
full_e2r_verified_score = null
primary_archetype = C05_EPC_MEGA_CONTRACT_MARGIN_GAP
accepted_claim_count = 1
score_contribution_count = 1
stage_signal = OFFICIAL_EVENT_WATCH
full_thesis_missing_primitives = ["full_thesis_refresh_task_not_run"]
```

해석:

```text
이 row도 SK하이닉스 HBM/C06 운영 점수가 아니다.
최근 DART 이벤트를 상태판에 올린 것이다.
```

주의:

```text
이 둘을 보고 "삼성전자 Stage1", "하이닉스 Stage1"이라고 운영 결론을 내리면 안 된다.
정확한 표현은 "Census event-board 기준 Stage1 상태"다.
```

## Goal gate 현재 상태

`goal_completion_audit.json`:

```text
goal_completion_ready = false

blockers:
  brain_web_evidence_pass_false
  full_thesis_smoke_pending
  full_thesis_production_pass_false
  source_backed_replay_parity_all_archetypes_pending
  goal_requirement_matrix_pass_false
```

`goal_requirement_matrix_audit.json`:

```text
PASS = 13 / 17
PENDING = 4 / 17
FAIL = 0 / 17

pending gates:
  FULL_THESIS_SMOKE_PASS
  FULL_THESIS_PRODUCTION_PASS
  BRAIN_WEB_EVIDENCE_PASS
  ALL_ARCHETYPE_SOURCE_BACKED_REPLAY_PASS
```

해석:

```text
Anti-fake 상태판은 통과했다.
하지만 goal.md/goal2.md/goal3.md 최종 목적은 아직 통과하지 않았다.
```

쉬운 예:

```text
집 주소록이 다 만들어진 것은 맞다.
하지만 각 집을 방문해서 상태 점검하고, 사진 찍고, 보고서까지 닫은 것은 아니다.
```

## Brain/Web 현재 상태

현재 canonical run:

```text
run_mode = LEDGER_REFRESH_CENSUS
brain_web_mode = disabled

brain_web_attempt_audit.verdict = NOT_REQUESTED
brain_web_readiness_gate_audit.verdict = NOT_REQUESTED
brain_stage_promotion_audit.verdict = NOT_REQUESTED

planner_run_count = 0
llm_real_provider_success_count = 0
web_search_task_count = 0
web_search_call_count = 0
web_fetched_document_count = 0
llm_claim_extractor_attempt_count = 0
web_or_llm_accepted_claim_count = 0
```

해석:

```text
이번 canonical output은 Brain/Web operational evidence run이 아니다.
따라서 "LLM 두뇌가 실제 웹/뉴스/IR/리포트를 읽고 Stage를 정했다"라고 말하면 안 된다.
```

중요:

```text
NOT_REQUESTED는 실패도 성공도 아니다.
다만 "이번 run에서는 그 기능을 요구하지 않았다"는 정직한 라벨이다.
```

## Full thesis smoke / production 현재 상태

현재 canonical run:

```text
samsung_hynix_full_thesis_smoke.verdict = PENDING_FULL_THESIS_REFRESH
full_thesis_production_audit.verdict = PENDING_FULL_THESIS_PRODUCTION
production_pass_allowed = false
production_mode_requested = false
production_full_thesis_row_count = 0
controlled_smoke_full_thesis_row_count = 0
```

`samsung_hynix_full_thesis_smoke_audit.json`에서 삼성전자/하이닉스 모두:

```text
full_thesis_stage = FULL_THESIS_NOT_RUN
operator_stage_use = NOT_FULL_THESIS_STAGE
stage_scope = CENSUS_EVENT_BOARD
score_scope = EVENT_WEIGHTED_PARTIAL
```

해석:

```text
controlled smoke는 코드에 존재하지만 canonical anti_fake run에서는 꺼져 있다.
production full thesis row도 없다.
```

테스트가 보장하는 의도:

```text
기본 run에서는 controlled smoke가 꺼져 있어야 한다.
controlled smoke는 explicit full_thesis_smoke target에서만 pass 가능하다.
controlled smoke는 production full thesis나 meaningful operational gate를 대신 만족하면 안 된다.
```

쉬운 예:

```text
모의고사는 시험장 시스템 점검에는 쓸 수 있다.
하지만 모의고사 점수를 실제 성적표로 제출하면 안 된다.
```

## All-archetype replay 현재 상태

`all_archetype_replay_matrix.json`:

```text
archetype_count = 36
required_archetype_count = 32
source_backed_ready_count = 6
guard_replay_ready_count = 6
missing_required_archetype_count = 26
all_archetype_replay_pass = false

status_counts:
  SOURCE_BACKED_POSITIVE_AND_GUARD_REPLAY_READY = 6
  SOURCE_GAP_PENDING = 26
  GUARDRAIL_CONTRACT_ONLY_PENDING_SOURCE_BACKED_REPLAY = 4
```

`GUARDRAIL_CONTRACT_ONLY_PENDING_SOURCE_BACKED_REPLAY = 4`는 아래 R13 cross-archetype guard contract row다.

```text
R13_CROSS_ARCHETYPE_STAGE2_FALSE_POSITIVE_REVIEW
R13_CROSS_ARCHETYPE_4B_4C_REDTEAM
R13_CROSS_ARCHETYPE_ACCOUNTING_TRUST_PRICE_VALIDATION
R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL
```

이 4개는 `required_before_goal_completion=false`라서
`missing_required_archetype_count=26`에 포함되지 않는다.

현재 source-backed ready:

```text
C06_HBM_MEMORY_CUSTOMER_CAPACITY
C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY
C15_MATERIAL_SPREAD_SUPERCYCLE
C17_CHEMICAL_COMMODITY_MARGIN_SPREAD
C24_BIO_TRIAL_DATA_EVENT_RISK
C28_SOFTWARE_SECURITY_CONTRACT_RETENTION
```

남은 required gap 26개:

```text
C01_ORDER_BACKLOG_MARGIN_BRIDGE
C02_POWER_GRID_DATACENTER_CAPEX
C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG
C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY
C05_EPC_MEGA_CONTRACT_MARGIN_GAP
C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH
C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF
C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE
C11_BATTERY_ORDERBOOK_RERATING
C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK
C13_BATTERY_JV_UTILIZATION_AMPC_IRA
C14_EV_DEMAND_SLOWDOWN_4B_4C
C16_STRATEGIC_RESOURCE_POLICY_SUPPLY
C18_CONSUMER_EXPORT_CHANNEL_REORDER
C19_BRAND_RETAIL_INVENTORY_MARGIN
C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION
C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN
C22_INSURANCE_RATE_CYCLE_RESERVE
C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION
C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT
C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE
C27_CONTENT_IP_GLOBAL_MONETIZATION
C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE
C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK
C31_POLICY_SUBSIDY_LEGISLATION_EVENT
C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP
```

해석:

```text
증거 읽기/replay가 전 아키타입에 아직 다 닫히지 않았다.
따라서 운영 파이프라인이 모든 아키타입에서 과거 연구 결과 수준으로 점수/stage를 재현한다고 말할 수 없다.
```

## 무엇이 잘못되고 있나

설계가 모두 틀렸다는 뜻은 아니다. 현재 구조는 anti-fake 쪽은 많이 좋아졌다.

현재 잘 된 것:

```text
1. CensusAssessmentEvent와 CandidateEvent가 분리되어 있다.
2. Stage row에 stage_scope/operator_stage_use가 있어 상태판과 full thesis를 구분한다.
3. FULL_E2R_100 점수와 EVENT_WEIGHTED_PARTIAL 점수를 섞지 않는다.
4. Brain/Web이 안 돌았으면 NOT_REQUESTED라고 말한다.
5. controlled smoke가 production full thesis를 대체하지 못하게 막는다.
6. source_proxy leak count가 0이다.
7. C06/C08/C15/C17/C24/C28 source-backed replay가 ready다.
8. full unittest artifact는 4997 tests OK다.
```

현재 부족한 것:

```text
1. canonical run에는 운영 FULL_THESIS Stage가 0개다.
2. Brain/Web operational evidence run이 canonical output에 없다.
3. web/news/IR/report fetch가 0개다.
4. full thesis production promotion이 아직 실제 canonical에서 발생하지 않았다.
5. all-archetype source-backed replay가 6/32까지만 닫혔다.
6. CENSUS_EVENT_BOARD Stage가 UI/운영에서 실제 Stage처럼 오해될 위험이 아직 크다.
7. Stage1/Stage2-Watch/Red 85개가 실제 full thesis로 보이지 않도록 출력/문서/CLI에서 더 강하게 막아야 한다.
```

## 가장 위험한 오해

### 오해 1. Stage1/Stage2가 있으니 운영 Stage가 있다

틀림.

```text
Stage1/Stage2-Watch 84개는 event-board 상태다.
stage_scope = CENSUS_EVENT_BOARD
operator_stage_use = NOT_FULL_THESIS_STAGE
```

운영 Stage 후보는 최소한:

```text
stage_scope = FULL_THESIS
score_scope = FULL_E2R_100
operator_stage_use = FULL_THESIS_STAGE
full_e2r_verified_score != null
accepted_claim_ids / score_contribution_ids / stagecourt_trace_id 존재
```

현재 canonical에는 0개다.

### 오해 2. 삼성전자/하이닉스가 Stage1이니까 HBM thesis가 약하다

틀림.

현재 삼성전자/하이닉스 Stage1은 HBM/C06 평가가 아니다.

```text
현재 row의 primary_archetype = C05_EPC_MEGA_CONTRACT_MARGIN_GAP
full_thesis_stage = FULL_THESIS_NOT_RUN
full_e2r_verified_score = null
```

즉:

```text
삼성전자/Hynix HBM thesis가 Stage1인 것이 아니다.
삼성전자/Hynix에 최근 공식 이벤트 상태 row가 Stage1로 표시된 것이다.
```

### 오해 3. C06/C28 replay가 됐으니 production scoring도 된다

틀림.

source-backed replay는 “원문을 읽고 primitive를 뽑는 기능” 검증이다.
production scoring은 “오늘 실제 후보에서 source acquisition부터 StageCourt까지 닫는 기능”이다.

쉬운 예:

```text
자동차 엔진 테스트는 통과했다.
하지만 도로 주행 테스트를 통과한 것은 아니다.
```

## 다음 패치 방향

### P0. 출력/UI/CLI에서 event-board Stage 오해 차단

목표:

```text
운영자가 CENSUS_EVENT_BOARD Stage를 FULL_THESIS Stage로 착각하지 못하게 만든다.
```

구체 작업:

```text
1. operator_digest와 acceptance_report 최상단에 "FULL_THESIS row=0" 경고를 더 크게 표시한다.
2. census_stage_map.csv/jsonl에 operator-facing field를 추가하거나 기존 field를 더 명확히 한다.
3. target_gate=meaningful/full_thesis/brain_web일 때 CENSUS_EVENT_BOARD만 있으면 exit code 1을 유지한다.
4. 문서/테스트에서 "non-Stage0 count" 대신 "event-board non-Stage0 count"라고 부르게 한다.
```

Acceptance:

```text
Stage label만 있는 run이 READY_FOR_OPERATIONAL_STAGE_USE로 보이면 실패.
FULL_THESIS row 0인데 "operational stage ready" 문구가 나오면 실패.
```

### P1. Samsung/Hynix controlled smoke를 canonical과 별도 artifact로 더 선명히 분리

목표:

```text
controlled smoke는 wiring 검증, production full thesis는 live/Brain evidence 검증으로 분리한다.
```

구체 작업:

```text
1. canonical anti_fake output에는 controlled smoke가 꺼져 있음을 계속 유지한다.
2. 별도 smoke output root를 생성해 README에 링크한다.
3. smoke pass가 goal_completion_ready를 true로 만들 수 없게 현재 guard를 유지한다.
4. smoke 점수는 production score가 아니라 primitive contribution sum test임을 더 명확히 산출물에 기록한다.
```

Acceptance:

```text
controlled smoke target은 pass 가능.
production full thesis target은 controlled smoke만으로 pass 불가.
```

### P2. Brain/Web enabled run을 별도 canonical candidate로 생성하고 blocker를 실제로 본다

목표:

```text
NOT_REQUESTED 상태를 넘어서, 실제 Brain/Web이 어디서 막히는지 leaf artifact로 확인한다.
```

실행 방향:

```text
run_mode = FULL_LIVE_BRAIN_CENSUS 또는 BRAIN_AND_WEB_ACQUISITION_ENABLED
brain_web_mode = enabled
brain_stage_promotion_mode = strict
target_gate = brain_web 또는 meaningful
```

예상 확인 항목:

```text
planner_runs.jsonl row > 0
web_search_tasks.jsonl row > 0
web_fetched_documents.jsonl row > 0
claim_extractor_runs.jsonl row > 0
brain_to_claim_trace.jsonl row > 0
brain promoted stage row > 0
```

주의:

```text
provider failure면 낮은 점수로 확정하지 말고 ProviderPending/SourcePending으로 남겨야 한다.
```

schema-v2 보조 진단 기준으로 P2는 일부 달성됐지만 아직 pass가 아니었다.
postextract-v1 기준으로는 web rejection ledger가 추가로 생겼지만 Brain/Web pass는 여전히 막혀 있다.

```text
달성:
  planner_runs > 0
  real provider success > 0
  web_search_tasks > 0
  web_fetched_documents > 0
  claim_extractor_runs > 0
  claim_extractor provider_error = 0
  schema-v2 BRAIN_WEB_PARTIAL row = 1
  postextract-v1 web_rejected_documents = 8

미달:
  postextract-v1 operational minimum planner runs 22/30
  postextract-v1 web search tasks 4/20
  postextract-v1 web search calls 4/20
  postextract-v1 fetched docs 7/10
  postextract-v1 extractor attempts 7/10
  postextract-v1 accepted claims 0/3
  FULL_THESIS rows 0
```

다음 세부 패치:

```text
1. LLM planner가 `subsidy_capture_visible` 같은 gap에 대해
   단순 포털 시세/공시목록 페이지가 아니라 issuer/DART/KIND/IR/신뢰뉴스 원문을 우선 찾게 만든다.

2. Source acquisition이 네이버 시세 페이지처럼 quote는 많지만 primitive score가 안 되는 문서를
   빨리 reject하고 같은 budget 안에서 더 적합한 source candidate를 fetch하게 한다.

3. schema-v2 당시 LLM raw assertion 29개처럼 "실제 추출은 됐지만 전부 rejected"인 경우,
   rejected reason을 planner feedback으로 돌려 다음 query/source class를 다시 묻게 한다.

4. accepted_claim_count가 1건이어도 `BRAIN_WEB_PARTIAL`로만 표시하고,
   FULL_THESIS promotion은 source quorum/primitive coverage/full thesis refresh가 닫힐 때까지 계속 금지한다.
```

쉬운 예:

```text
현재:
  "대웅 신규시설투자 보조금"을 찾으려 했는데
  네이버 시세 페이지와 공시 목록이 많이 들어왔다.
  LLM은 문장을 잘 뽑았지만 점수 재료가 아니어서 전부 탈락했다.

원하는 다음 상태:
  탈락 사유를 LLM planner에 돌려준다.
  "시세 페이지 말고 DART 본문/회사 IR/공장 투자 관련 회사 발표/신뢰뉴스 원문을 찾아라"는 새 계획을 LLM이 만든다.
  코드는 그 계획이 as_of_date, source budget, target scope를 지키는지만 검증한다.
```

금지:

```text
if primitive_gap == "subsidy_capture_visible":
    query = "{company} 보조금 인허가 ..."
```

이런 deterministic query 하드코딩으로 해결하면 안 된다.
검색 방향 판단은 LLM이 하고, deterministic 코드는 검증/예산/중복/미래누수 방어만 해야 한다.

### P3. Production FULL_THESIS promotion fixture와 live path 간 차이 줄이기

현재 테스트에는 `_write_live_brain_full_thesis_fixture`가 있고, 조건이 맞으면 FULL_THESIS row로 promote되는 길은 있다.

다음 패치 목표:

```text
fixture가 아니라 실제 Brain/Web bundle이 같은 조건을 만족하도록 한다.
```

필요 조건:

```text
real provider success > 0
source task executions > 0
accepted direct current claims > 0
score contributions > 0
StageCourt traces > 0
no snapshot:// promoted evidence
no fake provider
green gate primitive coverage 충족
```

최신 보조 진단의 핵심 차이:

```text
fixture:
  accepted direct/current claims + score contributions + StageCourt trace + full thesis markers가 함께 있다.

live diagnostic:
  partial accepted claim과 StageCourt trace는 1개 생겼지만,
  full thesis refresh task와 all required primitive coverage가 없다.
```

다음 패치 acceptance:

```text
1. BRAIN_WEB_PARTIAL row는 FULL_THESIS row로 자동 승격되지 않는다.
2. live run에서 FULL_THESIS row가 생기려면 full_thesis_stage != FULL_THESIS_NOT_RUN이어야 한다.
3. FULL_THESIS row에는 full_e2r_verified_score, accepted_claim_ids, score_contribution_ids, stagecourt_trace_id가 모두 있어야 한다.
4. FULL_THESIS row의 accepted_claim_ids에는 LLM/text/web 또는 official source에서 온 direct/current score-eligible claim이 포함되어야 한다.
5. 삼성전자/하이닉스 smoke는 controlled artifact로 남기되 production pass를 대신하지 않는다.
```

### P4. All-archetype source-backed replay 26개 남은 gap 닫기

목표:

```text
required 32개 아키타입 모두 positive + guard replay ready.
```

작업 방식:

```text
1. source_proxy_only 자료는 운영 fixture 정답으로 쓰지 않는다.
2. URL/source-backed fixture를 아키타입별로 만든다.
3. positive replay와 guard replay를 둘 다 통과시킨다.
4. replay_only=true, production_score_evidence_allowed=false를 유지한다.
```

쉬운 예:

```text
C05 공급계약:
  positive = 실제 revenue-facing supply contract + 규모/기간/마진 bridge source
  guard = 자기주식취득신탁/주식담보/관리성 계약이 contract_quality로 새지 않음
```

## 다음 에이전트 공격 체크리스트

다음 에이전트는 아래 질문에 전부 답해야 한다.

```text
1. FULL_THESIS row가 canonical output에 실제로 있는가?
2. 있으면 stage_scope, score_scope, operator_stage_use가 모두 FULL_THESIS/FULL_E2R 계열인가?
3. full_e2r_verified_score가 null이 아닌가?
4. 그 점수의 score_contribution_ids가 실제 accepted_claim_ids를 support하는가?
5. accepted_claim_ids가 evidence_document + evidence_anchor + source_task_execution까지 닫히는가?
6. Brain/Web enabled run이면 planner_runs, web_search_tasks, web_fetched_documents, claim_extractor_runs가 0이 아닌가?
7. provider failure가 낮은 점수/Red로 확정되지 않았는가?
8. source_proxy_only/evidence_url_pending/research memory가 production score로 새지 않았는가?
9. controlled smoke row가 production full thesis pass로 섞이지 않았는가?
10. CENSUS_EVENT_BOARD Stage가 operator-facing output에서 운영 Stage처럼 보이지 않는가?
11. all_archetype_replay_matrix의 missing 26개가 그대로인데 goal_completion_ready가 true가 되지 않는가?
12. 삼성전자/하이닉스 row를 HBM/C06 full thesis 결과로 오해하게 만드는 문구가 남아 있지 않은가?
```

## 재현 명령

현재 canonical 산출물 생성 명령:

```bash
PYTHONPATH=src python -m e2r.cli.run_e2r_census_v4_until_pass \
  --as-of-date 2026-07-01 \
  --output-root output/census_v4/2026-07-01 \
  --v3-output-root output/census_v3/2026-07-01 \
  --target-gate anti_fake \
  --test-result-artifact output/test_full_repo_0701/full_unittest_result_artifact.json
```

현재 full test artifact:

```text
output/test_full_repo_0701/full_unittest_result_artifact.json
status = OK
test_count = 4997
failures = 0
errors = 0
```

주의:

```text
이 테스트 통과는 anti-fake/guard/replay 테스트 통과다.
운영 FULL_THESIS row가 존재한다는 뜻은 아니다.
```

## 최종 판정

```text
질문: stage가 있는 애들이 있긴 해?
답: 있다. canonical 기준 85개가 Stage1/Stage2-Watch/Red다.
    schema-v2/feedback-v1 diagnostic에서는 그중 1개가 BRAIN_WEB_PARTIAL로 바뀐 적이 있다.
    postextract-v1 최신 diagnostic에서는 BRAIN_WEB_PARTIAL도 0개이고,
    canonical과 같이 CENSUS_EVENT_BOARD만 3391개다.

질문: 그게 실제 운영 E2R Stage냐?
답: 아니다. canonical 85개는 전부 CENSUS_EVENT_BOARD다.
    과거 diagnostic의 BRAIN_WEB_PARTIAL 1개도 operator_stage_use=NOT_FULL_THESIS_STAGE라 운영 Stage가 아니었다.

질문: 지금 뭔가 잘못되고 있는 거 맞냐?
답: 기대값이 "실제 운영 full thesis Stage"라면 맞다. 아직 없다.
    기대값이 "anti-fake full universe status board"라면 현재 산출물은 그 목적에는 맞게 정직하게 라벨링되어 있다.

질문: 다음에 무엇을 해야 하냐?
답: event-board 상태판을 운영 Stage처럼 보이지 않게 더 막고,
    Brain/Web enabled live run에서 LLM/web claim이 accepted primitive로 이어지게 만들고,
    production FULL_THESIS promotion을 실제 leaf artifact로 닫아야 한다.
```
