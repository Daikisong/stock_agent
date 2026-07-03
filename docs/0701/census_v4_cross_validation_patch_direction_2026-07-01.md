# Census v4 Cross Validation / Patch Direction - 2026-07-01

이 문서는 다음 에이전트가 빡세게 리뷰할 수 있도록, 현재 v4가 실제로 무엇을 통과했고 무엇을 아직 못 했는지 다시 쪼갠 기록이다.

## 최종 한 줄

```text
현재 v4는 "가짜 Stage/점수 완료 선언 방지"는 통과했다.
하지만 "실제 운영 full E2R thesis 점수/Stage 산출"은 아직 통과하지 않았다.
```

쉬운 예:

```text
지금 된 것:
  raw universe 3940개 중 eligible/stage 대상 3391개 출석부가 있고, 점수/claim이 있는 67개는 쪽지시험 채점지를 다시 펼쳐볼 수 있는지 확인했다.

아직 안 된 것:
  기말고사 100점 만점 종합 성적을 실제로 채점하지는 않았다.
```

## 재검산된 현재 숫자

기준 실행:

```bash
PYTHONPATH=src python -m e2r.cli.run_e2r_census_v4_until_pass \
  --as-of-date 2026-07-01 \
  --universe krx \
  --output-root output/census_v4/2026-07-01 \
  --v3-output-root output/census_v3/2026-07-01 \
  --run-mode LEDGER_REFRESH_CENSUS \
  --brain-web-mode disabled \
  --fail-on-critical-audit true \
  --write-operational-docs auto \
  --test-result-summary 'PYTHONPATH=src python -m unittest discover -s tests; Ran 4942 tests in 170.248s; OK' \
  --test-result-artifact output/census_v4/2026-07-01/test_result_artifact.json
```

관측값:

```text
rows: 3391

base_stage:
  Stage0:       3306
  Stage1:         54
  Stage2-Watch:   30
  Red:             1

canonical_stage:
  0:       3306
    1:         54
    2:         30
  3-Red:      1

full_thesis_stage:
  FULL_THESIS_NOT_RUN: 3391

verified_score_present_count: 0
full_e2r_verified_score_present_count: 0
event_evidence_score_present_count: 67
accepted_claim_count: 92
evidence_claim_payload_count: 92

candidate_event_scope:
  ASSESSMENT_ONLY:          3306
  CANDIDATE_EVENTS_PRESENT:   85

candidate_event_count: 226
score_eligible_candidate_event_count: 92
sample_leaf_bundle_count: 67
research_brain_bridge_verdict: SHADOW_OR_IMPORT_ONLY
research_brain_bridge_snapshot_url_count: 255
brain_web_attempt_verdict: NOT_REQUESTED
brain_stage_promotion_verdict: NOT_REQUESTED
brain_web_readiness_gate_verdict: NOT_REQUESTED
brain_web_evidence_pass_allowed: false
brain_stage_trace_count: 0
brain_stage_promoted_row_count: 0
```

주의:

```text
census_stage_summary.json의 legacy stage_distribution key는 base/display label 분포다.
canonical enum 분포는 canonical_stage_distribution이고,
새 alias base_stage_distribution도 함께 기록한다.
```

이 숫자의 의미:

```text
Stage가 있는 종목은 있다.
하지만 그것은 full thesis Stage가 아니라 daily/census event 상태 label이다.
92개 claim payload가 있지만, 이는 Brain/Web live claim이나 full thesis claim이 아니라
67개 부분 이벤트 score row를 뒷받침하는 source-backed accepted claim view다.
```

예:

```text
005930 삼성전자:
  base_stage: Stage1
  event_evidence_score: 4.0
  verified_score: null
  full_e2r_verified_score: null
  full_thesis_stage: FULL_THESIS_NOT_RUN

맞는 해석:
  daily event board에는 걸렸다.

틀린 해석:
  HBM/C06 full thesis 점수가 4점으로 확정됐다.
```

## 교차검증 결과

전체 테스트:

```text
PYTHONPATH=src python -m unittest discover -s tests
Ran 4942 tests in 170.248s
OK
```

leaf artifact audit:

```text
verdict: PASS
critical_count: 0
```

새로 추가/강화된 방어막:

```text
sample_leaf_bundle.jsonl exists
artifact_manifest.json has sample_leaf_bundle.jsonl
artifact_manifest.json does not hash itself
sample_bundle_missing_scored_row_count: 0
legacy_runner_production_reachable_count: 0
legacy_v3_runner_production_reachable_count: 0
empty_claims_stage_builder_production_count: 0
old_cli_can_claim_pass_count: 0
official_cli_not_v4_runner_count: 0
claim_to_stage_forensic_audit.json exists
source_task_realness_audit.json exists
existing_ledger_reuse_audit.json exists
last_effective_thesis_audit.json exists
source_coverage_audit.json exists
runtime_plausibility_audit.json exists
brain_web_readiness_gate_audit.json exists
```

해석:

```text
1. 부분 점수 또는 claim-backed row는 sample bundle에서 빠지지 않는다.
2. 예전 v1 CLI가 production Census pass를 주장하는 경로는 막혀 있다.
3. 빈 accepted_claims/score_contributions로 Stage를 만드는 production wiring은 현재 static audit상 없다.
4. 공식 v4 CLI는 v4 runner를 호출한다.
5. `accepted_claims.jsonl`과 `evidence_claims.jsonl`의 claim_id set이 일치한다.
6. Research Brain v4 기존 보고서는 import 검토만 됐고, snapshot/source blocker 때문에 production cutover evidence로 승격되지 않는다.
7. `brain_stage_promotion_audit.json`이 Brain StageCourt trace의 대표 Stage 승격을 별도 감사한다.
8. `brain_web_readiness_gate_audit.json`이 Brain/Web 개별 감사의 0건 PASS 착시를 막는다.
9. Brain/Web readiness gate는 accepted claim, trace, score contribution, StageCourt trace, promoted row가 같은 claim ID로 이어지는지도 본다.
10. Goal 문서가 요구한 claim-to-stage, source realness, 기존 ledger 재사용, last effective thesis, source coverage, runtime plausibility, Brain/Web readiness gate 감사를 별도 파일로 남긴다.
```

추가 enabled smoke 교차검증:

```text
run_mode: BRAIN_AND_WEB_ACQUISITION_ENABLED
brain_web_mode: enabled
brain_planner_provider: codex
brain_universe_limit: 3
brain_max_fetches_per_task: 2
target_gate: meaningful

result:
  readiness_verdict: NOT_READY
  brain_web_attempt_verdict: ATTEMPTED_NOT_CUTOVER_READY
  real_provider_success_count: 1
  source_task_execution_count: 10
  attempt_real_document_fetched_count: 12
  real_document_fetched_count: 0
  accepted_claim_count: 5
  unique_accepted_claim_count: 2
  brain_to_census_claim_exported_count: 2
  brain_stagecourt_trace_exported_count: 1
  brain_to_census_stage_exported_count: 0
  claim_acceptance_ready: true
  stagecourt_trace_ready: true
  cutover_export_ready: false
  brain_web_readiness_gate_verdict: BLOCKED
```

이 smoke로 확인한 것:

```text
Codex planner와 source task는 제한적으로 실행될 수 있다.
accepted claim, score contribution, StageCourt trace도 일부 만들 수 있다.
하지만 representative census_stage_status row 승격이 0개면 Brain/Web evidence pass가 아니다.
따라서 "채점 초안이 생겼다"와 "운영 Stage가 확정됐다"를 반드시 분리해야 한다.
```

이번 패치로 representative row 승격이 0개인 enabled attempt는
`ATTEMPTED_WITH_SOURCE_TASKS`로 남을 수 없고,
`ATTEMPTED_NOT_CUTOVER_READY`와 blocker를 남긴다.

쉬운 예:

```text
책을 빌려오고 답안지 초안을 쓴 것과 공식 성적표에 반영한 것은 다르다.
성적표 반영이 없으면 운영 Stage는 열리지 않는다.
```

쉬운 예:

```text
예전 문제:
  "채점지 없음" 상태인데 성적표만 만들어짐.

현재 방어:
  점수 row는 accepted_claim_ids, score_contribution_ids, stagecourt_trace_id, sample bundle, artifact manifest로 다시 따라갈 수 있어야 한다.
```

## Goal-required 감사 파일별 판정

다음 감사들은 `leaf_artifact_audit.json`을 쪼갠 보조 장부다. 다음 에이전트는 이 파일들을 독립적으로 열어야 한다.

```text
claim_to_stage_forensic_audit:
  verdict: PASS
  critical_count: 0
  scored_row_count: 67
  stage2plus_or_risk_row_count: 36

source_task_realness_audit:
  verdict: PASS_LEDGER_REFRESH_REALNESS
  verdict_scope: LEDGER_REFRESH_REALNESS_PASS
  live_source_pass_allowed: false
  source_task_execution_count: 92
  source_task_claim_producing_count: 60
  source_task_real_fetch_count: 0
  source_task_fresh_provider_cache_count: 60
  source_task_lifecycle_refresh_count: 32

existing_ledger_reuse_audit:
  verdict: PASS
  reused_claim_count: 92
  lifecycle_refreshed_reused_claim_count: 92
  new_brain_web_claim_count: 0

last_effective_thesis_audit:
  verdict: PASS
  last_effective_thesis_count: 3391
  source_timeline_count: 3391
  status_distribution:
    ACTIVE_THESIS: 74
    NEEDS_REFRESH: 3
    NO_KNOWN_THESIS: 3306
    SOURCE_PENDING: 8

source_coverage_audit:
  verdict: PASS_LEDGER_REFRESH_COVERAGE
  accepted_claim_count: 92
  reused_or_imported_claim_count: 92
  newly_verified_claim_count: 0
  cutover_replay_only_symbol_count: 67
  operational_live_source_coverage_pass: false

runtime_plausibility_audit:
  verdict: PASS_LEDGER_REFRESH_RUNTIME_HONESTY
  runtime_mode: LEDGER_REFRESH
  provider_call_count: 0
  llm_call_count: 0
  web_search_task_count: 0
  evidence_extraction_count: 0

brain_web_readiness_gate_audit:
  verdict: NOT_REQUESTED
  brain_web_evidence_pass_allowed: false
  brain_trace_missing_accepted_claim_count: 0
  brain_trace_missing_score_contribution_ref_count: 0
  brain_trace_missing_stagecourt_ref_count: 0
  brain_contribution_without_accepted_support_count: 0
  brain_stage_trace_without_accepted_claim_count: 0
  promoted_stage_without_brain_trace_count: 0
```

쉬운 예:

```text
claim_to_stage_forensic:
  "67개 점수 row의 채점지 번호가 실제 claim/trace 장부에 있나?"를 본다.
  대표 row id가 trace 집계 목록 전체와 1:1 동일한지를 보는 감사가 아니다.

source_task_realness:
  "이번에 live fetch를 했나, 기존 검증 장부를 다시 펼쳤나?"를 본다.
  source_task_executions 원시 row가 live-looking 필드를 갖더라도
  source_task_execution_origin과 source_task_real_fetch_count를 함께 봐야 한다.

existing_ledger_reuse:
  "기존 claim을 눈감고 복사했나, source locator와 lifecycle을 다시 확인했나?"를 본다.

source_coverage:
  "모든 종목에 census-time source 시도 기록은 있나? 다만 live full-source pass라고 부르지는 않는가?"를 본다.

runtime_plausibility:
  "0초대 실행인데 LLM 3000번 돌렸다는 식의 말이 있지 않나?"를 본다.

brain_web_readiness_gate:
  "Brain/Web을 실제로 했는가?"와 "accepted claim ID가 trace, contribution, StageCourt, promoted row까지 같은 줄로 이어지는가?"를 함께 본다.
  현재 0들은 Brain/Web이 disabled라 연결 대상이 없다는 뜻이지, live Brain/Web 연결 성공이 아니다.
```

현재 결론:

```text
Goal-required 감사 파일들은 anti-fake / ledger-refresh 정직성은 보강한다.
하지만 source_task_real_fetch_count=0, provider_call_count=0, llm_call_count=0이므로
full live operation 또는 full thesis scoring을 증명하지 않는다.
```

## 현재 PASS가 말하는 것

맞는 주장:

```text
ANTI_FAKE_FULL_UNIVERSE_STATUS_PASS
ATOMIC_STAGE_DECISION_PASS
SCORE_SCALE_PASS
STAGE_SEMANTICS_PASS
SEMANTIC_PRIMITIVE_GUARD_PASS
DAILY_EVENT_FULL_THESIS_SEPARATION_PASS
CENSUS_ASSESSMENT_CANDIDATE_EVENT_SEPARATION_PASS
```

위 label의 뜻:

```text
전 종목 row가 있다.
CensusAssessmentEvent와 CandidateEvent가 분리된다.
assessment-only row는 점수를 받지 않는다.
event_evidence_score와 full_e2r_verified_score가 분리된다.
Brain/Web disabled run에서 Brain/Web pass를 주장하지 않는다.
score/claim/trace가 다른 row에서 섞이면 audit fail이다.
```

## 현재 PASS가 말하지 않는 것

금지된 주장:

```text
전 종목 full E2R 100점 verified score가 있다.
삼성전자/하이닉스 HBM thesis 점수가 산출됐다.
Stage3-Green/Yellow/Red 운영 판정이 나왔다.
4A/4B/4C transition이 운영 기준으로 판정됐다.
Brain/Web/LLM acquisition이 실제로 통과했다.
Brain/Web StageCourt trace가 representative census_stage_status row로 승격됐다.
과거 연구자료 replay parity가 전 아키타입에서 증명됐다.
```

가장 중요한 금지:

```text
event_evidence_score 4.0
-> verified_score 4.0
-> "삼성전자 4점"이라고 출력
```

이건 다시 점수 혼동을 만든다.

## 아직 위험한 지점

### 1. 현재 산출물은 still event board다

모든 row가 다음 상태다.

```text
full_thesis_stage: FULL_THESIS_NOT_RUN
full_e2r_verified_score: null
```

따라서 full thesis runner가 붙지 않으면 Stage3-Green/Yellow/Red/4B/4C 운영 이야기를 하면 안 된다.

### 2. Brain/Web/LLM은 일부러 꺼져 있다

현재 run mode:

```text
run_mode: LEDGER_REFRESH_CENSUS
brain_web_mode: disabled
planner_run_count: 0
web_search_task_count: 0
claim_extractor_run_count: 0
```

이 숫자는 실패가 아니라 정직성이다.

추가 구현 상태:

```text
brain_web_mode=enabled 경로는 별도 smoke에서 Research Brain v4 attempt를 실행해
planner/source/document/raw/adjudicated/accepted claim/brain trace leaf export를 검증해야 한다.
그러나 canonical run은 disabled이고,
enabled attempt에서 accepted claim이 생겨도 아직 Census StageCourt row로 승격하지 않는다.
```

승격 감사 현재값:

```text
brain_stage_promotion_verdict: NOT_REQUESTED
brain_stage_trace_count: 0
brain_stage_promoted_row_count: 0
unsafe_promoted_stage_row_count: 0
```

쉬운 예:

```text
새 조사 서류철을 보관함에 넣는 길은 생겼다.
하지만 그 서류철을 최종 성적표에 반영하는 채점 단계는 아직 남아 있다.
```

추가 bridge audit:

```text
research_brain_bridge_verdict: SHADOW_OR_IMPORT_ONLY
research_brain_bridge_usable_for_census_cutover: false
research_brain_bridge_snapshot_url_count: 255
```

뜻:

```text
기존 Research Brain v4 보고서에는 accepted claim이 있지만,
snapshot:// record와 fixture/cutover blocker가 있어서
현재 Census v4 production evidence로 수입하면 안 된다.
```

쉬운 예:

```text
모의시험 답안지는 절차 연습을 보여 주지만,
실제 시험 성적표로 제출할 수 없다.
```

```text
검색을 안 했는데 "검색 성공"이라고 말하지 않는 상태.
```

다음 패치는 이 숫자를 실제로 늘려야 한다. 다만 provider 실패를 낮은 점수로 확정하면 안 된다.

### 2-1. Samsung/Hynix full thesis smoke task는 계획서까지만 있다

현재 추가된 leaf:

```text
full_thesis_smoke_tasks.jsonl
row_count: 14
symbols: 005930, 000660
primitive_count_per_symbol: 7
hardcoded_query_count: 0
score_allowed_before_execution: false
score_evidence: false
```

뜻:

```text
삼성전자/하이닉스 C06/HBM full thesis를 조사하기 위한 숙제 목록은 생겼다.
하지만 아직 답안지, 채점표, 최종 성적표는 없다.
```

다음 패치 방향:

```text
1. 이 14개 task를 LLM planner 입력으로 넘긴다.
2. LLM이 query를 만들고 deterministic validator가 as_of_date/company scope/중복을 검증한다.
3. official-first bounded fetch를 실행한다.
4. accepted full thesis claim -> primitive -> contribution -> StageCourt trace를 만든다.
5. 그 전까지 full_thesis_stage는 계속 FULL_THESIS_NOT_RUN이다.
```

### 3. semantic guard는 아직 전체 Evidence OS가 아니다

현재 guard는 일부 오판을 막는다.

예:

```text
자사주 신탁계약
담보/질권 계약
월덱스 감사의견 + 삼성전자 고객사 언급
```

하지만 최종 목표는 키워드 차단이 아니다.

최종 목표:

```text
EvidenceDocument
-> EvidenceAnchor
-> RawAssertion
-> Target/Temporal Adjudication
-> PrimitiveMappingProposal
-> AcceptedPrimitiveState
-> ScoreContributionLedger
-> StageCourt
```

### 4. Red와 4C는 아직 다르다

현재 `Red 1`은 full thesis 4C가 아니다.

```text
base_stage Red
canonical_stage 3-Red
full_thesis_stage FULL_THESIS_NOT_RUN
```

쉬운 예:

```text
처음 본 종목에서 위험 신호가 있음:
  Red/RiskReview 가능

기존 Green thesis가 현재 OPEN hard-break로 깨짐:
  4C transition 후보 가능
```

두 개를 섞으면 예전처럼 오래된 뉴스 하나로 4C가 생긴다.

## 다음 패치 방향

### P0. v4 anti-fake 상태 계속 고정

이미 통과한 anti-fake 불변식을 깨면 안 된다.

계속 0이어야 하는 항목:

```text
assessment_only_nonzero_score_count
score_eligible_candidate_without_accepted_claim_count
stage_trace_stage_mismatch_count
stage_trace_score_interval_mismatch_count
stage_trace_claim_set_mismatch_count
stage_trace_contribution_set_mismatch_count
verified_score_not_full_e2r_count
canonical_stage_display_label_count
web_claimed_but_zero_search_count
llm_claimed_but_zero_calls_count
legacy_runner_production_reachable_count
legacy_v3_runner_production_reachable_count
empty_claims_stage_builder_production_count
old_cli_can_claim_pass_count
official_cli_not_v4_runner_count
sample_bundle_missing_scored_row_count
brain_stage_promotion_unsafe_promoted_count
brain_stage_promotion_trace_promoted_reference_count
brain_stage_trace_not_promoted_marker_missing_count
```

### P1. Production SourceTask -> EvidenceClaim 실행

목표:

```text
CandidateEvent
-> SourceTask
-> provider request
-> EvidenceDocument/EvidenceAnchor
-> RawAssertion
-> EvidenceClaim
```

`EvidenceClaim`은 독립 장부여야 한다.
LLM이 "이 종목 90점"이라고 말하는 대신, 다음처럼 anchor가 붙은 claim 후보를 만든다.

```text
subject_entity
target_entity
predicate/value
event_date
source_anchor_id
quote/table/API locator
```

그 다음 deterministic 코드가 다음을 판정한다.

```text
target directness
as_of_date 이전 여부
current/open/resolved/superseded
source-backed 여부
accepted/rejected/pending
```

운영 규칙:

```text
official-first
production daily mode는 bounded budget
provider failure는 ProviderPending
source gap은 낮은 점수 확정이 아니라 Pending
Pending이면 full_e2r_verified_score=null
Pending이면 score_valid=false
Pending이면 canonical stage를 낮은 Red로 확정하지 않음
claim 확인 시 stop-on-resolution
```

쉬운 예:

```text
FCF gap:
  뉴스 1000개를 긁지 말고 DART/IR/CompanyGuide부터 bounded task로 실행.

provider 실패:
  0점 확정이 아니라 Source/Provider Pending.
```

### P2. Brain/Web Stage promotion strict gate

P1에서 live claim과 StageCourt trace가 생겨도 바로 대표 row가 되면 안 된다.

먼저 다음 조건을 audit로 통과해야 한다.

```text
brain_web_mode=enabled
brain_stage_promotion_mode=strict
real planner/provider success > 0
source task executions > 0
accepted brain claims > 0
claim-backed score contributions > 0
brain StageCourt traces > 0
zero snapshot:// promoted evidence documents
zero fake provider rows
zero unsafe promoted representative rows
```

그 다음에만 `census_stage_status.jsonl` 대표 row 병합을 구현한다.

쉬운 예:

```text
증거 서류가 생김
-> 채점 메모가 생김
-> promotion audit 통과
-> 공식 성적표 반영

증거 서류가 snapshot/fake/provider failure임
-> 채점 메모가 있어도 공식 성적표 반영 금지
```

### P3. Full thesis smoke

먼저 삼성전자/하이닉스부터 돌린다.

필수:

```text
daily event score와 full thesis score 분리
C06/HBM primitive coverage 확인
old qualification delay lifecycle/supersession 확인
direct target + current OPEN + source quorum 없는 hard break 금지
score delta가 claim delta로 설명됨
삼성/하이닉스 전용 하드코딩 금지
generic Evidence Contract와 SourceTask 위에서만 smoke 실행
```

결과가 안 나오면 실패가 아니라 이렇게 표시해야 한다.

```text
score_status: PENDING_MATERIAL_GAPS
full_thesis_stage: FULL_THESIS_NOT_RUN
full_thesis_status: PENDING_FULL_THESIS_REFRESH
missing_primitives: [...]
```

### P3. 전 아키타입 Evidence Contract v2

각 아키타입은 코드 분기가 아니라 registry/spec로 가져야 한다.

필수 항목:

```text
required primitives
alternative primitives
k-of-n gate
source quorum
freshness / expiry / supersession rule
guard mode
hard-break rule
score cap
unknown/material gap policy
```

나쁜 방식:

```text
if C06 then hardcoded HBM query
if "감사의견" in text then risk true
```

좋은 방식:

```text
LLM이 현재 evidence와 gap을 보고 query를 제안
코드는 query/source/date/entity/future leakage만 검증
Score/Stage는 accepted claim ledger만 사용
```

### P4. 과거 연구자료 replay parity

연구자료는 그대로 정답지가 아니다.

사용 가능:

```text
원문 URL
snapshot
quote/table/API record
source-backed claim
```

사용 금지:

```text
source_proxy_only score
evidence_url_pending score
미래 MFE/MAE
사후 성공 label
```

성공 기준:

```text
같은 as_of_date와 같은 원문 snapshot에서
연구자료가 말한 positive/guard boundary를
Evidence OS가 claim-backed primitive로 재현한다.
```

## 다음 에이전트 공격 질문

아래 중 하나라도 답이 없으면 운영 완료가 아니다.

```text
1. 이 Stage는 event board인가 full thesis인가?
2. 이 점수는 event_evidence_score인가 FULL_E2R_100 verified_score인가?
3. 이 claim의 subject는 target 회사 자체인가?
4. event_date와 as_of_date가 분리됐는가?
5. 현재성은 current/open/resolved/superseded로 판정됐는가?
6. score contribution이 source anchor와 claim id를 갖는가?
7. ProviderPending이 낮은 score final로 바뀌지 않았는가?
8. Brain/Web pass를 말하려면 planner/search/fetch/extractor artifact가 실제로 있는가?
9. 점수 delta가 added/removed/superseded/contradicted claim으로 설명되는가?
10. 같은 corpus를 다시 돌렸을 때 claim id와 stage가 증식/흔들리지 않는가?
```

## 최종 판단

```text
현재 위치:
  anti-fake census status board는 통과.

아직 목표:
  실제 SourceTask와 LLM claim extraction을 통해
  EvidenceClaim -> PrimitiveState -> ScoreContribution -> StageCourt
  경로를 모든 아키타입에 대해 source-backed로 닫기.
```

따라서 다음 패치는 Stage label을 더 많이 만드는 작업이 아니다.

```text
다음 패치는 "증거가 없으면 점수 없음"을 유지하면서,
실제 운영 source에서 증거 claim을 찾아 점수 칸을 채우는 작업이어야 한다.
```

## Cross-Validation P0.5 - Completion Gate Honesty

교차검증 결과, 실제 Brain/Web 구현 전에 먼저 닫아야 할 정직성 패치가 추가로 확인됐다.

현재 아직 주면 안 되는 label:

```text
MEANINGFUL_OPERATIONAL_STAGE_PASS
BRAIN_WEB_EVIDENCE_PASS
FULL_THESIS_SMOKE_PASS
```

현재는 줘도 되지만 goal completion으로 읽으면 안 되는 label:

```text
KNOWN_BAD_REGRESSION_PASS
SELF_REPAIR_LOOP_PASS
```

쉬운 예:

```text
known-bad/self-repair는 쪽지시험 재검산 통과다.
full thesis와 Brain/Web이 남아 있으면 기말고사 전체 완료는 아니다.
```

```text
P0.5-A CLI exit target 분리
  구현됨: CLI는 --target-gate anti_fake|meaningful|brain_web|full_thesis를 받는다.
  anti_fake exit 0과 meaningful/brain_web/full_thesis completion exit 0이 분리됐다.
  남음: meaningful/brain_web/full_thesis gate 자체는 아직 닫히지 않았으므로 해당 target은 NOT_READY가 정상이다.

P0.5-B goal3 CLI flag 지원
  --mode
    구현됨: --run-mode alias로 동작한다.
  --max-iterations
    구현됨: config와 self_repair_log audit/recheck loop에 기록된다.
  --fail-on-run-mode-overclaim
  --fail-on-atomic-mismatch
  --fail-on-semantic-guard
    구현됨: CLI/config 입력은 받는다.
  구현됨: known-bad 재실행과 v4 self-repair audit/recheck loop가 `self_repair_log.json`에 기록된다.
  남음: 이 self-repair pass는 Brain/Web/full-thesis deferred blocker를 대신 닫지 않는다.
  즉 "옵션 파싱"과 "audit/recheck loop"는 됐지만, goal3 전체 완료는 Brain/Web/full-thesis가 닫혀야 한다.

P0.5-C test result artifact화
  구현됨: test_result_evidence_audit.json이 문자열 summary를 완료 증거로 인정하지 않는다.
  구현됨: command, exit_code, start/end time, sha256, test count를 가진 e2r_test_result_artifact_v1 JSON을 검증한다.
  현재 verdict: MACHINE_READABLE_TEST_ARTIFACT_PASS
  현재 test_count: 4942
  남음: 이 테스트 증거는 completion blocker 하나만 닫는다. known-bad와 self-repair blocker도 별도 suite/loop로 닫혔다. full thesis/Brain-Web blockers는 그대로 남아 있다.

P0.5-C2 known-bad regression suite
  구현됨: known_bad_regression_report.json이 실제 deterministic 회귀 suite를 실행한다.
  현재 status: PASS
  현재 case_count: 10
  현재 failed_case_count: 0
  포함 범위: wrong-subject audit opinion, non-revenue contract guard, trace mismatch, source_proxy/evidence_url_pending/snippet/provider-failure score guard, Samsung/Hynix daily-event/full-thesis 분리.
  남음: 이 suite 통과는 "가짜 결과 방지" 증거다. Brain/Web live evidence, self-repair loop, full thesis smoke를 대신하지 않는다.

P0.5-D PASS scope naming
  구현됨:
    source_task_realness PASS -> PASS_LEDGER_REFRESH_REALNESS / LIVE_SOURCE_PASS
    runtime_plausibility PASS -> PASS_LEDGER_REFRESH_RUNTIME_HONESTY / PASS_LIVE_RUNTIME_PLAUSIBILITY
    web/LLM audit PASS -> DISABLED_HONESTY_PASS / REAL_ACQUISITION_PASS
    source_task_satisfaction PASS -> PASS_LEDGER_REFRESH_SOURCE_TASK_SATISFACTION
  남음: brain_planner/official_event_counter처럼 아직 generic PASS가 남은 보조 audit도 scope를 더 잘게 쪼개야 한다.

P0.5-E v4 self-repair 원본성
  구현됨: output/census_v4/2026-07-01/self_repair_log.json은 v4 schema audit/recheck loop 실행 로그다.
  현재 schema: e2r_census_v4_self_repair_log_v1
  현재 status: RUN_COMPLETE
  현재 final_status: PASS
  현재 unresolved_failures: []
  현재 deferred_goal_blockers: brain_web_evidence_pass_false, full_thesis_smoke_pending
  남음: Brain/Web/full-thesis deferred blocker를 실제 source/claim/stage trace로 닫는 것은 아직 아니다.

P0.5-F Brain/Web minimum gate 강화
  BRAIN_AND_WEB_ACQUISITION_ENABLED에서 accepted claim 1개만으로 web/search/fetch 조건을 우회하면 안 된다.
  goal2 최소 수량 또는 명시적 external blocker가 필요하다.
  추가 반영: attempt count는 proof가 아니다. 실제 source_task_executions/evidence_documents/evidence_anchors/accepted_claims row가 resolve되어야 한다.

P0.5-G promotion evidence quality
  Brain/Web promoted row는 ID 연결성뿐 아니라 document_id, anchor_id, source date, target directness,
  temporal current/open status를 hard gate로 가져야 한다.
  추가 반영: accepted claim의 document_id/anchor_id 문자열이 실제 evidence_documents/evidence_anchors row에 없으면 blocker다.

P0.5-H reviewer 독립성
  reviewer A/B/C/D/E가 leaf audit wrapper이면 독립 reviewer pass가 아니다.
  별도 입력을 읽고 별도 count를 계산해야 한다.

P0.5-I full thesis pending/pass 분리
  FULL_THESIS_SMOKE_PASS는 task planned 또는 explicitly pending으로 닫으면 안 된다.
  source task 실행, accepted claim, primitive mapping, score contribution, StageCourt trace, representative row promotion까지 이어져야 한다.
  미해결 material blocker가 있으면 FULL_THESIS_SMOKE_PENDING으로 남겨야 한다.

P0.5-J LLM classification proposal 제한
  LLM이 contract type 또는 primitive 후보를 제안할 수는 있다.
  하지만 accepted primitive 확정과 score eligibility는 deterministic guard가 결정해야 한다.
  즉 LLM classification은 proposal/diagnostic이고 점수 입력값 그 자체가 아니다.

P0.5-K query provenance gate
  non-official query는 planner_run_id/prompt_response_id에서 나온 것이어야 한다.
  deterministic 코드는 query를 생성하지 않고 as_of_date, target company, duplicate, future leakage만 검증한다.

P0.5-L symbol branch 금지
  Samsung/Hynix smoke는 fixture이지 종목명 예외가 아니다.
  symbol_specific_scoring_branch_count=0, symbol_specific_stage_branch_count=0, hardcoded_query_count=0이 hard gate다.
```

쉬운 예:

```text
지금 필요한 P0.5는 "시험을 보기" 전에 "합격증 양식이 거짓말하지 못하게 고치는 작업"이다.
이걸 닫지 않으면 작은 Brain/Web fixture 하나만 붙이고도 또 운영 완료처럼 보일 수 있다.
```
