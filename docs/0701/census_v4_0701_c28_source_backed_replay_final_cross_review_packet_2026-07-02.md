# Census v4 0701 C28 Source-Backed Replay Final Cross-Review Packet

작성일: 2026-07-02  
대상 repo: `/home/eorb915/projects/stock_agent`  
기준 as_of_date: `2026-07-01`  
기준 canonical output: `output/census_v4/2026-07-01`  
기준 full test artifact: `output/test_full_repo_0701/full_unittest_result_artifact.json`

## 한 줄 결론

```text
C28 controlled semantic replay까지 닫혔다.
하지만 이것은 운영 FULL_THESIS 점수가 생겼다는 뜻이 아니다.
현재 Stage row 3391개는 전부 CENSUS_EVENT_BOARD 상태판 Stage이고, FULL_THESIS row는 0개다.
```

쉬운 예:

```text
이번 패치는 "소프트웨어/보안 아키타입의 채점 칸에 들어갈 증거를 제대로 읽는지" 확인한 것이다.
아직 "실제 종목을 오늘부터 운영 파이프라인으로 끝까지 채점했다"는 단계가 아니다.
```

## 이 문서를 먼저 읽어야 하는 이유

`docs/0701`에는 중간 스냅샷 문서가 많다.

예전 문서에는 다음 값들이 남아 있을 수 있다.

```text
source_backed_ready_count = 0 / 1 / 3 / 4 / 5
controlled_semantic pass_count = 4 / 5 / 7 / 8 / 9
C28 pending
test_count = 4942 / 4951 / 4954 / 4957 / 4959 / 4975 / 4983 / 4992 / 4996
```

이 문서 작성 시점의 최신 기준은 아래다.

```text
source_backed_ready_count = 6
guard_replay_ready_count = 6
missing_required_archetype_count = 26
controlled_semantic_replay_pass = true
controlled_semantic pass_count = 10
controlled_semantic pending_count = 0
full unittest artifact test_count = 4997
```

## 이번 패치가 고친 것

### 1. C28 replay 산출물 연결

새 산출물:

```text
output/census_v4/2026-07-01/c28_source_backed_semantic_replay.json
```

runner 연결:

```text
src/e2r/census/census_runner_v4.py
```

auditor 필수 파일 연결:

```text
src/e2r/census/census_v4_auditor.py
```

테스트 연결:

```text
tests/test_census_v4_all_archetype_replay_matrix.py
tests/test_census_v4_goal_required_audits.py
```

### 2. C28 predicate 분류 오류 수정

수정 파일:

```text
src/e2r/production/claim_extraction/contract_blind_extractor.py
```

문제:

```text
CrowdStrike "annual recurring revenue" 문장이
software_arr_growth_claim이 아니라 generic material_profitability_bridge_claim으로 먼저 잡혔다.
```

쉬운 예:

```text
원래:
  "annual recurring revenue"를 보기 전에 "revenue"라는 큰 그물에 걸림
  -> ARR primitive 누락

패치 후:
  software ARR/NRR/renewal/deferred revenue/subscription margin 문장을 먼저 분류
  -> C28 primitive로 정확히 매핑
```

중요:

```text
종목명 예외를 넣은 것이 아니다.
"CrowdStrike면 통과" 같은 조건은 없다.
일반 소프트웨어 recurring economics 문장을 generic revenue 문장보다 먼저 분류하도록 순서를 고친 것이다.
```

## C28 source-backed replay 실측

명령:

```bash
PYTHONPATH=src python - <<'PY'
from pathlib import Path
from e2r.census.census_runner_v4 import CensusV4RunConfig, _c28_source_backed_semantic_replay
r=_c28_source_backed_semantic_replay(
    config=CensusV4RunConfig(as_of_date='2026-07-01'),
    output_root=Path('output/census_v4/2026-07-01'),
)
for k in [
    'positive_replay_pass',
    'guard_replay_pass',
    'accepted_claim_count',
    'positive_claim_count',
    'guard_claim_count',
    'positive_support_primitive_ids',
    'guard_support_primitive_ids',
    'guard_accepted_claim_ids',
    'keyword_only_guard_leaked_support_primitives',
    'document_urls',
    'blockers',
]:
    print(k, '=', r.get(k))
PY
```

결과:

```text
positive_replay_pass = true
guard_replay_pass = true
accepted_claim_count = 7
positive_claim_count = 7
guard_claim_count = 0

positive_support_primitive_ids:
  arr_growth_visible
  nrr
  retention_or_renewal
  rpo_to_sales
  recurring_margin_leverage

guard_support_primitive_ids = []
guard_accepted_claim_ids = []
keyword_only_guard_leaked_support_primitives = []
blockers = []
production_score_evidence_allowed = false
```

사용한 source-backed fixture:

```text
Positive:
  CrowdStrike fiscal 2025 Form 10-K
  URL: https://www.sec.gov/Archives/edgar/data/1535527/000153552725000009/crwd-20250131.htm

Guard:
  CrowdStrike Falcon Next-Gen SIEM ISV ecosystem press release
  URL: https://ir.crowdstrike.com/news-releases/news-release-details/crowdstrike-announces-falcon-next-gen-siem-isv-ecosystem-open
```

쉬운 예:

```text
Positive source:
  "ARR 23% 증가"
  "dollar-based net retention 112%"
  "renewals / expansion / contraction / churn"
  "deferred revenue, next 12 months revenue recognition"
  "subscription gross margin 78%"
  -> C28 recurring economics primitive 통과

Guard source:
  "SIEM ecosystem"
  "AI-native SOC"
  "security teams ingest/retain/search/analyze data"
  -> 보안 제품 설명일 뿐 ARR/NRR/RPO/renewal/margin 증거가 아님
  -> C28 score primitive로 새면 안 됨
```

현재 guard 결과는 이 오염을 막는다.

```text
guard_claim_count = 0
keyword_only_guard_leaked_support_primitives = []
```

## 최신 Stage / Score 진실

명령:

```bash
python - <<'PY'
import json
from pathlib import Path
from collections import Counter
rows=[json.loads(line) for line in Path('output/census_v4/2026-07-01/census_stage_status.jsonl').read_text().splitlines() if line.strip()]
print('row_count', len(rows))
print('stage_scope', Counter(r.get('stage_scope') for r in rows))
print('base_stage', Counter(r.get('base_stage') for r in rows))
print('canonical_stage', Counter(r.get('canonical_stage') for r in rows))
print('score_scope', Counter(r.get('score_scope') for r in rows))
print('score_valid_status', Counter(r.get('score_valid_status') for r in rows))
print('full_thesis_rows', sum(1 for r in rows if r.get('stage_scope') == 'FULL_THESIS'))
print('nonzero_full_e2r_verified_score', sum(1 for r in rows if r.get('full_e2r_verified_score') is not None))
print('event_score_rows', sum(1 for r in rows if r.get('event_evidence_score') is not None))
PY
```

결과:

```text
row_count = 3391

stage_scope:
  CENSUS_EVENT_BOARD = 3391

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

score_scope:
  NO_SCORE = 3324
  EVENT_WEIGHTED_PARTIAL = 67

score_valid_status:
  NO_CURRENT_EVENT = 3306
  FINAL_WITH_NONMATERIAL_GAPS = 37
  PENDING_MATERIAL_GAPS = 30
  NOT_SCORED = 11
  INVALID_EVIDENCE = 7

full_thesis_rows = 0
nonzero_full_e2r_verified_score = 0
event_score_rows = 67
```

해석:

```text
Stage가 있는 종목은 있다.
하지만 그 Stage는 전부 Census 상태판 Stage다.
운영 FULL_THESIS Stage와 FULL_E2R_100 verified score는 아직 없다.
```

쉬운 예:

```text
Stage1:
  "최근 공식 이벤트가 있어 watch 상태"라는 표식이다.
  "전체 E2R 100점 채점 결과 Stage1"이라는 뜻이 아니다.

Stage2-Watch:
  "material claim이 있어 더 봐야 한다"는 상태다.
  "Green 직전의 운영 thesis"라는 뜻이 아니다.
```

## 삼성전자 / SK하이닉스 현재 의미

canonical output 기준:

```text
삼성전자 005930:
  stage_scope = CENSUS_EVENT_BOARD
  base_stage = Stage1
  canonical_stage = 1
  event_evidence_score = 4.0
  full_thesis_stage = FULL_THESIS_NOT_RUN
  full_e2r_verified_score = null
  primary_archetype = C05_EPC_MEGA_CONTRACT_MARGIN_GAP

SK하이닉스 000660:
  stage_scope = CENSUS_EVENT_BOARD
  base_stage = Stage1
  canonical_stage = 1
  event_evidence_score = 4.0
  full_thesis_stage = FULL_THESIS_NOT_RUN
  full_e2r_verified_score = null
  primary_archetype = C05_EPC_MEGA_CONTRACT_MARGIN_GAP
```

주의:

```text
이 값은 C06/HBM 운영 thesis 점수가 아니다.
daily event-board가 DART/공식 이벤트를 보고 붙인 상태판 점수다.
```

예전의 90점/60점 혼란을 막는 핵심:

```text
event_evidence_score 4.0
  -> 일일 이벤트 상태판의 부분 점수

full_e2r_verified_score null
  -> 운영 full thesis 100점 채점은 아직 안 했음
```

## All-Archetype Replay Matrix

산출물:

```text
output/census_v4/2026-07-01/all_archetype_replay_matrix.json
```

실측:

```text
all_archetype_replay_pass = false
archetype_count = 36
required_archetype_count = 32
source_backed_ready_count = 6
guard_replay_ready_count = 6
controlled_wiring_smoke_ready_count = 0
missing_required_archetype_count = 26

status_counts:
  SOURCE_BACKED_POSITIVE_AND_GUARD_REPLAY_READY = 6
  SOURCE_GAP_PENDING = 26
  GUARDRAIL_CONTRACT_ONLY_PENDING_SOURCE_BACKED_REPLAY = 4
```

READY:

```text
C06_HBM_MEMORY_CUSTOMER_CAPACITY
C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY
C15_MATERIAL_SPREAD_SUPERCYCLE
C17_CHEMICAL_COMMODITY_MARGIN_SPREAD
C24_BIO_TRIAL_DATA_EVENT_RISK
C28_SOFTWARE_SECURITY_CONTRACT_RETENTION
```

PENDING required archetypes:

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
C28까지 통과했지만 전체 아키타입 parity는 아직 아니다.
따라서 goal completion은 계속 blocked가 맞다.
```

## Controlled Semantic Replay

산출물:

```text
output/census_v4/2026-07-01/controlled_semantic_replay_audit.json
```

실측:

```text
controlled_semantic_replay_pass = true
case_count = 10
required_case_count = 10
pass_count = 10
pending_count = 0
fail_count = 0
blockers = []
```

닫힌 10개 케이스:

```text
C06_HBM_POSITIVE_AND_QUALIFICATION_LAG_GUARD
C08_TEST_SOCKET_CUSTOMER_ORDER_PROFILE_ONLY_GUARD
C15_MATERIAL_SPREAD_PASS_THROUGH_RAW_COMMODITY_GUARD
C17_CHEMICAL_SPREAD_REALIZED_MARGIN_BRIDGE_GUARD
C24_CLINICAL_BINARY_EVENT_GUARD
C28_SOFTWARE_SECURITY_RETENTION_BRIDGE_GUARD
WRONG_SUBJECT_RISK_FIXTURE
OLD_RISK_RESOLVED_FIXTURE
PROVIDER_FAILURE_PENDING_FIXTURE
SEMANTIC_CONTRACT_GUARD_FIXTURE
```

의미:

```text
우선순위 semantic guard 10개는 source-backed/lifecycle-clean 기준으로 닫혔다.
하지만 이것은 32개 required archetype 전체 replay parity가 아니다.
```

## Goal Matrix

산출물:

```text
output/census_v4/2026-07-01/goal_requirement_matrix_audit.json
output/census_v4/2026-07-01/goal_completion_audit.json
```

실측:

```text
goal_completion_minimum_pass = false
required_goal_completion_count = 17
required_goal_completion_pass_count = 13
required_goal_completion_pending_count = 4

pending_gate_ids:
  FULL_THESIS_SMOKE_PASS
  FULL_THESIS_PRODUCTION_PASS
  BRAIN_WEB_EVIDENCE_PASS
  ALL_ARCHETYPE_SOURCE_BACKED_REPLAY_PASS

goal_completion_ready = false
```

이미 닫힌 것:

```text
CONTROLLED_SEMANTIC_REPLAY_PASS = PASS
FULL_TEST_ARTIFACT_PASS = PASS
SELF_REPAIR_LOOP_PASS = PASS
STAGE_SEMANTICS_PASS = PASS
```

주의:

```text
goal matrix row에는 PASS row에도 blocker 문자열이 설명용으로 남아 있을 수 있다.
실제 gate 상태는 status와 pending_gate_ids를 봐야 한다.
예: CONTROLLED_SEMANTIC_REPLAY_PASS row의 blocker 필드 문자열은 남아도 status=PASS이고 pending_gate_ids에는 없다.
```

## Leaf Audit / Full Tests / Canonical Run

### py_compile

```bash
PYTHONPATH=src python -m py_compile \
  src/e2r/census/census_runner_v4.py \
  src/e2r/census/census_v4_auditor.py \
  src/e2r/production/claim_extraction/contract_blind_extractor.py \
  src/e2r/production/claim_extraction/primitive_mapper.py
```

결과:

```text
PASS
```

### Targeted tests

```bash
PYTHONPATH=src python -m unittest \
  tests.test_census_v4_all_archetype_replay_matrix \
  tests.test_census_v4_goal_required_audits -v
```

결과:

```text
Ran 13 tests
OK
```

### Census v4 tests

```bash
PYTHONPATH=src python -m unittest $(rg --files tests | rg 'tests/test_census_v4_.*\.py$' | sed 's#/#.#g; s#\.py$##') -v
```

결과:

```text
Ran 116 tests
OK
```

### Full repo tests

```bash
PYTHONPATH=src python -m e2r.cli.run_test_command_with_artifact \
  --artifact output/test_full_repo_0701/full_unittest_result_artifact.json \
  --log output/test_full_repo_0701/full_unittest.log \
  -- python -m unittest discover -s tests -v
```

결과:

```text
schema_version = e2r_test_result_artifact_v1
status = OK
exit_code = 0
test_count = 4997
failed_count = 0
error_count = 0
duration_seconds = 182.0206
```

### Canonical Census v4 run

```bash
PYTHONPATH=src python -m e2r.cli.run_e2r_census_v4_until_pass \
  --as-of-date 2026-07-01 \
  --output-root output/census_v4/2026-07-01 \
  --v3-output-root output/census_v3/2026-07-01 \
  --target-gate anti_fake \
  --test-result-artifact output/test_full_repo_0701/full_unittest_result_artifact.json
```

결과:

```text
ANTI_FAKE_FULL_UNIVERSE_STATUS_PASS
```

주의:

```text
ANTI_FAKE_FULL_UNIVERSE_STATUS_PASS는 "fake full thesis를 만들지 않았다"는 pass다.
meaningful_operational_stage_pass는 여전히 false다.
```

## 현재 정상인 것

```text
1. CensusAssessmentEvent가 score evidence로 새지 않는다.
2. price/news snippet/source_proxy/evidence_url_pending이 score로 새지 않는다.
3. wrong-subject audit opinion이 target risk로 새지 않는다.
4. old resolved risk가 current hard break로 새지 않는다.
5. provider failure가 낮은 final score로 확정되지 않는다.
6. C06 qualification lag guard가 4C hard break로 새지 않는다.
7. C08 profile-only guard가 named customer/margin bridge로 새지 않는다.
8. C15 raw commodity headline이 issuer pass-through로 새지 않는다.
9. C17 spread-only / inventory-loss guard가 realized margin positive로 새지 않는다.
10. C24 binary futility/discontinuation이 trial-quality positive로 새지 않는다.
11. C28 security product keyword가 ARR/NRR/RPO/renewal/margin positive로 새지 않는다.
12. C28 ARR/NRR/renewal/deferred revenue/subscription margin source는 required primitives를 모두 연다.
```

## 아직 정상 완료가 아닌 것

```text
1. FULL_THESIS row = 0
2. FULL_E2R_100 verified score row = 0
3. 삼성전자/하이닉스 C06/HBM full thesis production run = not run
4. Brain/Web evidence pass = false / NOT_REQUESTED
5. production full thesis pass = false / PENDING_FULL_THESIS_PRODUCTION
6. all-archetype source-backed replay parity = false
7. required archetype source gap = 26
```

따라서 다음 문장은 금지다.

```text
운영 파이프라인 준비 완료
삼성전자/하이닉스 full thesis Stage 확정
전 아키타입 source-backed replay 완료
Brain/Web live evidence 운영 통과
```

현재 허용되는 표현:

```text
Census event-board 상태판은 anti-fake 기준으로 pass.
C06/C08/C15/C17/C24/C28 priority semantic replay는 source-backed positive+guard 통과.
FULL_THESIS 운영 점수와 Brain/Web 운영 gate는 아직 pending.
```

## 다음 패치 방향

### P0. 지금 고치면 안 되는 것

```text
가중치 / Stage threshold 변경 금지
종목명 예외 하드코딩 금지
"C28이면 항상 이런 query" 같은 deterministic query 템플릿 확장 금지
source_proxy_only 연구자료를 운영 정답으로 쓰기 금지
```

### P1. FULL_THESIS smoke를 다시 정직하게 닫기

현재 blocker:

```text
FULL_THESIS_SMOKE_PASS
```

해야 할 일:

```text
삼성전자/하이닉스 C06/HBM smoke를 daily event-board row와 분리된 FULL_THESIS scope로 실행한다.
단, controlled smoke는 production pass를 대체하면 안 된다.
```

쉬운 예:

```text
현재:
  삼성전자 Stage1 / event_evidence_score 4.0 / FULL_THESIS_NOT_RUN

목표:
  삼성전자 daily event row는 그대로 두고,
  별도 FULL_THESIS smoke row가 source-backed claim, primitive, contribution, stagecourt trace를 가진다.
```

### P2. FULL_THESIS production runner를 실제 운영 모드로 닫기

현재 blocker:

```text
FULL_THESIS_PRODUCTION_PASS
```

해야 할 일:

```text
controlled smoke substitution 없이 production_full_thesis_row_count > 0을 만든다.
FULL_THESIS row에는 full_e2r_verified_score, accepted_claim_ids, score_contribution_ids, stagecourt_trace_id가 닫혀야 한다.
```

### P3. Brain/Web evidence gate를 실제 LLM/web leaf로 닫기

현재 blocker:

```text
BRAIN_WEB_EVIDENCE_PASS
```

현재 canonical:

```text
brain_web_mode = disabled
llm_planner_call_count = 0
web_search_task_count = 0
web_fetched_document_count = 0
llm_claim_extractor_attempt_count = 0
web_or_llm_accepted_claim_count = 0
```

목표:

```text
real planner/provider/source acquisition/extractor trace가 leaf로 남아야 한다.
snapshot://나 fixture-like report bundle은 cutover proof가 아니다.
```

### P4. 남은 26개 required archetype source-backed replay 확장

현재 blocker:

```text
ALL_ARCHETYPE_SOURCE_BACKED_REPLAY_PASS
```

남은 26개는 각 아키타입별로 다음이 필요하다.

```text
1. 실제 URL 또는 API/table anchor가 있는 positive source
2. false-positive guard source
3. contract-blind extraction
4. target/temporal/lifecycle adjudication
5. primitive mapping
6. positive + guard replay PASS
7. production_score_evidence_allowed=false인 replay-only 증거
```

주의:

```text
이 replay는 운영 점수 정답이 아니다.
운영 점수에 넣기 전에 같은 경로가 production SourceTask, live/official source, StageCourt까지 이어져야 한다.
```

## 다음 에이전트 공격 질문

완료 주장 전에 아래 질문을 반드시 던진다.

```text
1. stage_scope=FULL_THESIS row가 실제로 생겼나?
2. FULL_THESIS row의 full_e2r_verified_score가 null이 아닌가?
3. daily event score와 full thesis score를 같은 점수처럼 설명하지 않았나?
4. 삼성전자/하이닉스 C06 row가 C05 daily event로 남아 있는 상태를 HBM 평가라고 말하지 않았나?
5. C28 guard에서 "retain data"를 "customer retention"으로 오해하지 않았나?
6. "subscription revenue recognized ratably"를 RPO/deferred revenue와 혼동해 과대 primitive를 만들지 않았나?
7. nonzero score contribution에 support claim id가 모두 있나?
8. accepted claim에 document_id/anchor_id/source_url이 모두 있나?
9. source_proxy_only/evidence_url_pending/snapshot URL이 production score로 새지 않았나?
10. Brain/Web pass라고 말하려면 planner/web/fetch/extractor leaf가 실제 minimum count를 넘었나?
11. provider failure를 Stage0/Red final로 확정하지 않았나?
12. old risk를 current hard break로 만들지 않았나?
13. wrong subject claim을 target risk로 붙이지 않았나?
14. all-archetype replay pass라고 말하려면 missing_required_archetype_count가 0인가?
15. goal_completion_ready가 true인가? 현재 false다.
```

## 최종 판단

```text
C28 패치는 성공했다.
controlled semantic replay 10/10도 성공했다.
전체 테스트와 canonical anti-fake run도 통과했다.

하지만 이 상태는 "운영 준비 완료"가 아니다.
현재 시스템은 Census 상태판과 priority semantic replay guard를 더 정직하게 만든 단계다.
다음 핵심은 FULL_THESIS production row와 real Brain/Web evidence gate다.
```

