# E2R LIVE CURRENT MATERIALIZATION & OPERATIONAL ORCHESTRATION MASTER GOAL v1
## Phase 17+ — Current-State Bootstrap / Bounded Live Acquisition / Research Brain / Evidence OS / Current & Census Cutover

너는 `Daikisong/stock_agent` 레포의 수석 아키텍트이자 구현 에이전트다.

이번 Goal은 이전 `E2R Evidence Intelligence Reconstruction Program`의 후속 작업이다.
이전 작업에서 내부 연구 두뇌, research corpus compiler, Evidence Recipe, historical blind replay,
claim/score/stage 안전성은 상당 부분 재건되었다.

그러나 현재 canonical current/Census 경로는 실제 시장을 보지 않는다.

현재 구조는 대략 다음과 같다.

```text
run_e2r_current_operation
→ 완성된 CurrentOperationRunnerInput manifest가 있는지 확인
→ manifest가 없으면
   CURRENT_KRX_UNIVERSE_AND_LIVE_SOURCE_INPUT_MANIFEST_UNAVAILABLE
   Stage 0
   score_valid=false
   exit 3
→ 종료
```

`CurrentOperationRunnerInput`에는 이미 아래가 들어 있어야 한다.

```text
universe
baseline_lanes
triggers
claims
claim_provenance
source_tasks
atomic_decisions
deep_executions
config
```

즉 현재 canonical CLI는 실제 KRX universe, DART/KIND/KRX/CompanyGuide/IR/뉴스,
Research Brain, Evidence OS를 실행해 입력을 만드는 운영 엔진이 아니라,
거의 완성된 입력 manifest를 받아 deterministic하게 조립·감사하는 evaluator다.

이번 Goal의 목적은 사용자가 이 JSON을 직접 만들어 제공하게 하는 것이 아니다.

이번 Goal의 목적은 기존 레포에 이미 존재하는 공식 source connector, Naver/Web transport,
Research Brain, Evidence OS, deterministic scorer, StageCourt를 하나의 bounded live path로 연결해,
canonical current/Census CLI가 입력 manifest를 스스로 materialize하고 실제 운영 결과를 내게 만드는 것이다.

---

# 0. 이번 요청의 명시적 Live 연결 승인

이 Goal은 루트 `AGENTS.md`의 다음 제한에 대한 **사용자의 명시적 별도 승인**이다.

```text
live web scraping이나 live API 연결은 별도 요청 전까지 추가하지 않는다.
```

사용자는 이번 Goal에서 다음을 명시적으로 승인한다.

```text
1. 기존 레포에 구현된 OpenDART, KIND, KRX, CompanyGuide, IssuerIR,
   TrustedNews, Naver/Web connector와 현재 `.env` provider 구성을 사용하는
   bounded live current-input materialization 구현 및 실행을 승인한다.

2. 필요한 경우 기존 connector가 generic portal page만 가져오거나 symbol-specific
   데이터를 만들지 못하는 부분을 공식 공개 endpoint/페이지 기준으로 보강하는 것을 승인한다.

3. canonical current/Census CLI가 KRX universe부터 source acquisition,
   Research Brain, Evidence OS claim, deterministic score/Stage까지 실행해
   CurrentOperationRunnerInput manifest를 스스로 생성하도록 구현하는 것을 승인한다.

4. 무제한 scraping은 승인하지 않는다.
   Production daily와 Census selective-deep는 official-first, bounded budget,
   rate limit, circuit breaker, shard/checkpoint, stop-on-resolution을 유지한다.

5. Naver/general web는 모든 티커에 무차별 실행하지 않는다.
   Research Brain이 선별한 L3/L4 후보의 exact source gap에만 bounded fallback으로 사용한다.

6. `.env` secret 값은 절대 출력·커밋하지 않는다.
   credential 존재 여부와 provider error category만 기록한다.
```

이 승인 이후 다음 행위는 금지한다.

```text
- input manifest가 없다는 이유만으로 외부 blocker를 선언하고 종료
- 사용자에게 universe/claim/atomic decision이 든 완성 manifest를 달라고 요구
- 기존 connector를 실행하지 않고 "외부 데이터 부재"로 책임 전가
- generic portal homepage fetch를 symbol-specific evidence로 계산
- snapshot/fixture를 live evidence로 위장
```

---

# 1. 최종 목표

최종 운영 플로우는 다음이어야 한다.

## 1.1 Initial Current-State Bootstrap

```text
현재 KRX 전체 universe
→ 종목/시장/상장상태/보통주 eligibility
→ bulk official baseline
→ latest regular financial state
→ open material events / contracts / investments / risk lifecycle
→ existing accepted claim ledger refresh
→ source timeline / last effective thesis
→ versioned CurrentStateStore
```

초기 지도는 최근 며칠 공시만 보는 지도가 아니다.

```text
한 달 전, 일 년 전, 그보다 오래된 사건이라도
계약 기간이 남았거나,
시설투자가 진행 중이거나,
리스크가 아직 OPEN이거나,
latest regular report에 의해 supersede되지 않았다면
현재 상태에 포함한다.
```

`recent window`는 source refresh 우선순위일 뿐 Stage cutoff가 아니다.

## 1.2 Daily Current Operation

```text
CurrentStateStore
+ 오늘/최근 delta source
+ current market/risk/report/news event
→ CandidateEvent/Trigger pool
→ DepthPolicy
→ selected Research Brain planning
→ official-first SourceTask
→ bounded IR/report/Naver/Web fallback
→ full source fetch
→ EvidenceDocument / Anchor
→ RawAssertion
→ adjudicated current claim
→ append-only claim ledger
→ PrimitiveState
→ ScoreContribution
→ deterministic scorer
→ StageCourt
→ CurrentOperationRunnerInput manifest
→ pure CurrentOperationRunner evaluator
→ daily watchlist / pending / risk review
```

## 1.3 Full-Universe Census

```text
동일한 current source corpus / claim ledger / atomic decision
→ 전 eligible symbol의 baseline status
→ 필요한 종목만 selective deep
→ Stage0 / Stage1 / Stage2 / Yellow / Green / Red / 4A/4B/4C
   또는 Provider/Source/Budget Pending
→ 전체 Stage map
```

모든 티커가 full-thesis 점수를 받아야 하는 것은 아니다.
그러나 모든 eligible symbol은 실제 current source attempt와 상태 이유를 가져야 한다.

---

# 2. 최종 역할 분리

## 2.1 Pure Evaluator는 유지한다

`src/e2r/research_brain/runtime/current_operation_runner.py`의 핵심 원칙은 유지한다.

```text
- live I/O를 하지 않는다.
- 이미 materialize된 입력을 deterministic하게 검증·조립한다.
- same input → same leaf output
- leaf artifact / manifest / audit를 재현한다.
```

이 evaluator에 네트워크 호출을 마구 넣지 않는다.

## 2.2 새 Live Materializer를 만든다

새 계층이 실제 데이터를 만든다.

예시 구조:

```text
src/e2r/research_brain/runtime/live_materialization/
    __init__.py
    authorization.py
    schemas.py
    provider_capabilities.py
    credential_audit.py
    universe_materializer.py
    baseline_materializer.py
    current_state_store.py
    source_timeline_bootstrap.py
    trigger_fusion.py
    depth_selector.py
    brain_planner_runner.py
    source_task_builder.py
    source_acquisition_runner.py
    claim_compiler_runner.py
    adaptive_closure_controller.py
    atomic_decision_builder.py
    current_input_manifest_builder.py
    census_orchestrator.py
    current_orchestrator.py
    checkpoint_store.py
    observability.py
    audits.py
```

실제 파일명은 현재 레포 구조에 맞게 조정할 수 있으나,
**live materializer와 pure evaluator 경계는 반드시 유지**한다.

## 2.3 새 Operational Envelope를 만든다

기존 `CurrentOperationRunnerResult.production_runtime_ready=False`는
fixture/contract evaluator의 안전 경계로 유지할 수 있다.

대신 최종 live readiness는 별도 envelope에서 판정한다.

```text
LiveOperationalRunEnvelope
- materialization_run_id
- evaluator_run_id
- as_of_date
- run_mode
- source_corpus_hash
- input_manifest_hash
- evaluator_leaf_hash
- actual_live_source_count
- fresh_provider_cache_count
- accepted_current_claim_count
- current_atomic_decision_count
- provider_blockers
- critical_counts
- production_runtime_ready
```

Pure evaluator 결과 하나만 보고 production ready를 선언하지 않는다.

---

# 3. 절대 금지사항

1. scoring weight와 Stage threshold를 변경해 통과하지 마라.
2. 삼성전자, SK하이닉스, C06 등 특정 종목/아키타입을 production logic에 하드코딩하지 마라.
3. current/Census CLI가 manifest를 기다리기만 하는 상태에서 완료 선언하지 마라.
4. KRX/KIND main homepage 하나를 전 종목의 universe/risk evidence로 세지 마라.
5. generic CompanyGuide page fetch를 symbol consensus evidence로 세지 마라.
6. snapshot, fixture, example.com, reserved test URL을 live claim provenance로 쓰지 마라.
7. Naver headline/snippet을 score evidence로 쓰지 마라.
8. source_proxy_only, evidence_url_pending, price_path_only historical memory를 current score에 쓰지 마라.
9. historical MFE/MAE/outcome을 current planner/extractor prompt에 넣지 마라.
10. LLM이 score/stage를 직접 결정하거나 AtomicScoreContribution을 임의 생성하지 못하게 하라.
11. deterministic hardcoded query template를 canonical live path에 쓰지 마라.
12. 기존 `naver_news.py`의 고정 query templates를 canonical Research Brain query로 사용하지 마라.
13. provider failure를 NO_RESULT로 숨기지 마라.
14. provider/source/runtime failure를 낮은 점수나 Red로 확정하지 마라.
15. old risk를 current OPEN claim 없이 penalty/hard break로 쓰지 마라.
16. rerouted claim이 accepted되었다고 원래 primitive gap을 닫지 마라.
17. current material gap이 남았는데 FULL_E2R_100 final score를 만들지 마라.
18. 모든 티커에 Naver/LLM deep research를 무차별 실행하지 마라.
19. 모든 아키타입을 현재 시장에 억지로 하나씩 materialize하지 마라.
20. report summary 수치로만 PASS하지 마라.
21. 테스트 fixture 결과로 live production ready를 선언하지 마라.
22. 실패 후 같은 명령만 반복하고 self-repair라고 부르지 마라.
23. threshold 완화, fixture 추가, 특정 종목 예외로 acceptance를 통과하지 마라.
24. 외부 blocker와 내부 materializer 미구현을 하나의 blocker로 합치지 마라.
25. 사용자가 수정한 `docs/core/goal*.md`를 임의로 되돌리거나 삭제하지 마라.

---

# 4. Phase 17 — Read-Only Live Gap Forensic

코드를 고치기 전에 현재 live/current 경로를 전수 감사한다.

대상:

```text
AGENTS.md
src/e2r/cli/run_e2r_current_operation.py
src/e2r/cli/run_e2r_census_mode.py
src/e2r/research_brain/runtime/current_operation_runner.py
src/e2r/pipeline/korea_live_lite.py
src/e2r/production/source_connectors/**
src/e2r/sources/**
src/e2r/research_brain/planning/**
src/e2r/research_brain/runtime/**
src/e2r/evidence/**
src/e2r/scoring/**
src/e2r/stage/**
tests/**
docs/operational/e2r_reconstruction_phase16*
```

생성:

```text
docs/operational/e2r_live_materialization_forensic_baseline.md
docs/operational/e2r_live_materialization_call_graph_before.json
docs/operational/e2r_provider_capability_inventory_before.json
docs/operational/e2r_current_manifest_dependency_inventory.json
```

반드시 답할 질문:

1. canonical current/Census CLI가 실제로 어디서 manifest를 찾는가?
2. manifest 부재 시 어떤 함수가 exit 3를 만드는가?
3. `CurrentOperationRunnerInput`의 각 필드를 현재 어느 코드가 만들 수 있는가?
4. 기존 KoreaLiveLite의 어떤 부분을 재사용할 수 있고, 어떤 부분은 legacy/unsafe인가?
5. OpenDART/KIND/KRX/CompanyGuide connector가 실제 symbol-specific 데이터를 주는가?
6. generic portal fetch가 실질 evidence로 오인될 경로가 있는가?
7. KRX current universe를 실제로 materialize하는 기존 코드가 있는가?
8. Naver/Web transport와 LLM query generation이 분리되어 있는가?
9. current accepted claim → provenance → atomic decision을 만드는 canonical 경로가 있는가?
10. initial full-universe bootstrap과 daily incremental update가 분리되어 있는가?
11. 내부 구현 blocker와 credential/provider blocker가 어떻게 섞여 있는가?

Phase 17 완료 조건:

```text
- MISSING_INTERNAL_MATERIALIZER와 EXTERNAL_PROVIDER_BLOCKER를 분리
- production reachable manifest-only path를 정확히 기록
- 재사용 가능한 connector/service 목록 확정
- 폐기/adapter/deprecate할 legacy 경로 확정
```

한글 커밋:

```text
Phase 17 현재 운영 입력 단절과 live connector 경로 감사
```

---

# 5. Phase 18 — Architecture & Authorization Contract

생성:

```text
docs/operational/e2r_live_materialization_architecture.md
configs/e2r_live_materialization_v1.json
configs/e2r_current_bootstrap_v1.json
configs/e2r_production_daily_v1.json
configs/e2r_census_selective_deep_v1.json
```

운영 모드:

```text
MANIFEST_REPLAY
LIVE_BOOTSTRAP
LIVE_DAILY_INCREMENTAL
LIVE_CENSUS_BASELINE
LIVE_CENSUS_SELECTIVE_DEEP
TARGETED_LIVE_SMOKE
TEST_FIXTURE
```

각 모드는 다음을 명시한다.

```text
- live authorization required?
- allowed providers
- universe policy
- baseline policy
- Brain candidate budget
- source task budget
- LLM budget
- Naver/Web budget
- checkpoint/resume
- final label ceiling
```

CLI authorization:

```text
--input-manifest <path>
```

가 있으면 기존 replay/evaluator 모드.

```text
--materialize-live-input true
--live-materialization-authorized true
```

이면 기존 connector를 사용해 manifest를 스스로 만든다.

둘 다 없으면 기존 fail-closed Stage 0/Pending을 유지한다.

중요:

```text
live-materialization-authorized=true가 있는데
manifest가 없다는 이유로 바로 exit 3 하면 critical fail.
```

한글 커밋:

```text
Phase 18 bounded live materialization 승인과 실행 계약 추가
```

---

# 6. Phase 19 — Provider Capability Matrix & Credential Audit

각 provider를 기능별로 분해한다.

```text
ProviderCapability
- provider_name
- required_for_bootstrap
- required_for_daily
- can_build_universe
- can_fetch_bulk_price
- can_fetch_symbol_price
- can_fetch_disclosure_index
- can_fetch_full_official_document
- can_fetch_risk_status
- can_fetch_consensus_revision
- can_discover_issuer_ir
- can_search_news
- can_fetch_full_article
- supports_batch
- supports_checkpoint
- auth_env_keys
- live_ready
- blocker_reason
```

필수 provider:

```text
OpenDART
KRX
KIND
CompanyGuide
IssuerIR
TrustedNews
NaverSearch
GeneralWebFetcher
ExistingLedger
ResearchMemory
```

Credential audit:

```text
- load_project_env로 `.env`를 읽는다.
- secret 값은 출력하지 않는다.
- PRESENT / MISSING / INVALID / AUTH_FAILED만 기록한다.
- `.env`에 키가 있는데 process env에 없다는 이유로 missing 처리하지 않는다.
```

Blocker taxonomy:

```text
MISSING_INTERNAL_MATERIALIZER
MISSING_CREDENTIAL
INVALID_CREDENTIAL
PROVIDER_AUTH_FAILURE
PROVIDER_RATE_LIMIT
PROVIDER_SCHEMA_CHANGED
PROVIDER_NETWORK_FAILURE
UNIVERSE_FETCH_FAILURE
DOCUMENT_FETCH_FAILURE
LLM_PROVIDER_FAILURE
SOURCE_EXHAUSTED
RUNTIME_BUDGET_EXHAUSTED
```

금지:

```text
CURRENT_KRX_UNIVERSE_AND_LIVE_SOURCE_INPUT_MANIFEST_UNAVAILABLE
```

하나로 모든 문제를 뭉개지 마라.

Generic portal guard:

```text
- KRX main page fetch != KRX universe
- KIND main page fetch != symbol risk status
- CompanyGuide homepage != symbol consensus
- generic portal document는 provider health check일 수는 있어도
  symbol-specific baseline/evidence source로 세지 않는다.
```

출력:

```text
docs/operational/e2r_live_provider_capability_matrix.json
docs/operational/e2r_live_credential_audit.json
docs/operational/e2r_live_provider_blocker_matrix.json
```

한글 커밋:

```text
Phase 19 live provider 기능과 credential blocker 분리
```

---

# 7. Phase 20 — Current KRX Universe Materializer

구현 예:

```text
src/e2r/research_brain/runtime/live_materialization/universe_materializer.py
```

목표:

```text
KRX current full universe
→ market / name / symbol / security type / listing status
→ eligible common-stock universe
→ DailyUniverseMember
```

필수 규칙:

1. official KRX source 또는 현재성이 증명된 official-derived data를 사용한다.
2. KRX main HTML page만 가져와 universe가 만들어졌다고 하지 않는다.
3. ETF, ETN, SPAC, preferred share, REIT 등 제외 정책을 config로 명시한다.
4. excluded instrument도 count와 reason을 남긴다.
5. symbol/company/market/eligibility가 없는 row는 quarantine한다.
6. `as_of_date` 이후 데이터 사용 금지.
7. same source snapshot + same config에서 deterministic.
8. bulk-first로 구현한다.
9. full universe를 symbol별 HTTP 3천 번으로 만들지 않는다.
10. source URL/official document ID/content hash/fetched time/provider request ID를 남긴다.

출력:

```text
output/live_materialization/<AS_OF_DATE>/universe_raw.jsonl
output/live_materialization/<AS_OF_DATE>/universe_eligible.jsonl
output/live_materialization/<AS_OF_DATE>/universe_excluded.jsonl
output/live_materialization/<AS_OF_DATE>/universe_provenance.json
```

Hard acceptance:

```text
raw_universe_count > 1000
eligible_universe_count > 1000
missing_symbol_count = 0
missing_company_name_count = 0
duplicate_eligible_symbol_count = 0
fixture_symbol_count = 0
generic_portal_counted_as_universe_count = 0
future_universe_data_count = 0
```

한글 커밋:

```text
Phase 20 KRX 현재 전체 universe materializer 구현
```

---

# 8. Phase 21 — Versioned CurrentStateStore & Initial Bootstrap

초기 전체 지도는 daily recent window만으로 만들 수 없다.

구현 예:

```text
current_state_store.py
source_timeline_bootstrap.py
claim_ledger_loader.py
lifecycle_refresher.py
```

CurrentStateStore:

```text
- target identity
- universe snapshot
- baseline source attempts
- latest regular financial state
- material official events
- open contract/investment/capacity events
- current risk lifecycle
- consensus/revision state
- accepted current claims
- historical-only claims
- pending source tasks
- last effective thesis
- last updated source corpus hash
```

Initial bootstrap source policy:

```text
1. latest regular report / latest financial actual
2. latest material disclosure
3. open supply contract / investment / financing / risk event lifecycle
4. existing claim ledger
5. previous Census/daily state
6. latest consensus/revision where available
7. price/volume baseline
```

중요:

```text
최근 30/90/365일 밖이라는 이유만으로 active event를 버리지 않는다.
```

Lifecycle examples:

```text
공급계약:
contract end/cancellation/supersession까지 active

시설투자:
completion/cancellation/revenue conversion까지 active

정기보고서:
latest report가 prior financial state를 supersede

리스크:
official clear/resolution/supersession까지 OPEN 가능

뉴스/IR:
full source current claim + later official contradiction check 필요

가격 이상:
짧은 investigation trigger일 뿐 current thesis evidence가 아님
```

Bootstrap completeness:

```text
COMPLETE
PARTIAL_HISTORY_PENDING
PROVIDER_PENDING
SOURCE_GAP
```

history가 불완전한 종목을 `NoCurrentCatalyst`로 위장하지 않는다.

출력:

```text
output/current_state/<AS_OF_DATE>/current_state_store.jsonl
output/current_state/<AS_OF_DATE>/source_timelines.jsonl
output/current_state/<AS_OF_DATE>/last_effective_thesis.jsonl
output/current_state/<AS_OF_DATE>/bootstrap_completeness.json
```

Hard acceptance:

```text
source_timeline_count == eligible_universe_count
last_effective_thesis_count == eligible_universe_count
symbol_without_any_source_attempt_count = 0
recent_window_used_as_stage_cutoff_count = 0
old_active_contract_dropped_count = 0
old_resolved_risk_scored_count = 0
provider_failure_mapped_no_thesis_count = 0
```

한글 커밋:

```text
Phase 21 전 종목 current state bootstrap과 claim lifecycle 구현
```

---

# 9. Phase 22 — Four Required Baseline Lanes

`CurrentOperationRunnerInput`이 요구하는 baseline lane을 실제로 만든다.

각 eligible symbol에 대해:

```text
OFFICIAL
PRICE
RISK
EXISTING_LEDGER
```

## OFFICIAL

```text
- latest regular report checked
- latest material official event checked
- source IDs / observed date
- no result vs provider failed 분리
```

## PRICE

```text
- current/as-of price
- trading value
- relative strength / anomaly
- price는 trigger 우선순위용
- score evidence 아님
```

## RISK

```text
- trading halt
- management issue
- delisting/listing risk
- disclosure violation
- investment warning
- current official lifecycle
```

## EXISTING_LEDGER

```text
- prior current accepted claim
- stale needs refresh
- superseded/contradicted
- no prior ledger
```

Bulk-first 원칙:

```text
KRX price/universe/risk, DART disclosure index는 가능한 한 batch/pagination으로 수집한다.
symbol별 3천 번 동일 portal page를 요청하지 않는다.
```

Provider failure는 해당 symbol/lane에만 붙인다.
전 universe를 ProviderPending으로 만들지 않는다.

Hard acceptance:

```text
baseline_lane_count == eligible_count * 4
missing_required_baseline_lane_count = 0
baseline_lane_provider_failure_without_error_count = 0
observed_lane_without_source_id_count = 0
price_lane_to_score_count = 0
generic_portal_observed_lane_count = 0
```

한글 커밋:

```text
Phase 22 current operation 필수 baseline lane 실제 연결
```

---

# 10. Phase 23 — Trigger Fusion & Candidate Pool

Current trigger type:

```text
OFFICIAL
EARNINGS
IR
REPORT
NEWS
MARKET
RISK
EXISTING_LEDGER
```

Trigger source:

```text
OpenDART/KIND/KRX
CompanyGuide/report radar
Issuer IR/newsroom
TrustedNews/Naver discovery
market anomaly
existing current claim/pending thesis
```

규칙:

1. trigger는 investigation을 연다.
2. trigger 자체는 score evidence가 아니다.
3. headline/snippet은 verification task를 만든다.
4. current source-backed claim만 score를 연다.
5. trigger dedupe는 symbol + source event + effective date 기준.
6. wrong subject / related company / customer company를 target event로 오인하지 않는다.
7. existing active thesis와 pending source task도 trigger pool에 포함한다.
8. active contract가 오래됐다는 이유로 trigger pool에서 사라지지 않는다.
9. current market에 실제 trigger가 없는 archetype을 억지로 만들지 않는다.

출력:

```text
candidate_events.jsonl
trigger_signals.jsonl
trigger_dedupe_report.json
trigger_source_distribution.json
```

Hard acceptance:

```text
full_universe_trigger_scan_attempted = true
market_trigger_to_score_count = 0
news_snippet_to_score_count = 0
wrong_subject_trigger_count = 0
trigger_without_source_ref_count = 0
```

한글 커밋:

```text
Phase 23 공식·리포트·뉴스·시장·기존 장부 trigger 통합
```

---

# 11. Phase 24 — DepthPolicy & Bounded Candidate Selection

전 종목 baseline은 실행하지만 deep research는 선별한다.

Depth:

```text
L0_UNIVERSE
L1_BASELINE
L2_OFFICIAL_LIGHT
L3_RESEARCH_BRAIN
L4_ACQUISITION
L5_FULL_THESIS
```

Selection inputs:

```text
- trigger materiality
- current risk
- existing active thesis
- pending material gap
- official event
- earnings/revision
- report/IR/news verification need
- market anomaly
- provider/source gap
- random sector audit sample
```

중요:

```text
current operation에서 archetype quota를 강제로 채우지 않는다.
```

Historical parity는 historical replay에서 검증한다.
현재 시장에서는 실제 후보만 선택한다.

Budgets:

```text
max_official_light_targets
max_deep_candidates
max_brain_candidates
max_acquisition_candidates
max_llm_calls_per_candidate
max_source_tasks_per_candidate
max_fetches_per_candidate
max_retries_per_candidate
max_general_web_fetches_per_candidate
max_runtime_seconds
```

`CurrentOperationRunnerConfig`의 nested budget 조건을 유지한다.

출력:

```text
depth_decisions.jsonl
candidate_selection_audit.json
budget_allocation.json
not_selected_budget.jsonl
```

Hard acceptance:

```text
every eligible symbol has depth decision
selected_deep_count > 0 on full live validation unless exact low-signal proof
unbounded_candidate_count = 0
forced_archetype_quota_count = 0
not_selected_without_reason_count = 0
```

한글 커밋:

```text
Phase 24 전 종목 baseline과 bounded selective deep 정책 연결
```

---

# 12. Phase 25 — Canonical Research Brain Live Planning

이전 reconstruction에서 만든 canonical Research Brain을 사용한다.
legacy keyword router 또는 primitive-name query template를 사용하지 않는다.

Planner input:

```text
- target identity
- as_of_date
- current source timeline
- current baseline events
- existing current claims
- last effective thesis
- balanced historical memory
- Evidence Recipes
- provider capability/gap
- budget
```

Planner input에서 숨길 것:

```text
- score
- Stage
- future MFE/MAE
- historical outcome
- expected archetype answer
- source_primary archetype binding
```

Two-pass:

```text
Pass A:
current facts만 보고 top-k mechanism/hypothesis

Pass B:
balanced positive/counter/source-success/source-failure memory로 critique
```

Planner output:

```text
- top-k archetype hypotheses
- current supporting facts
- current counter thesis
- must-verify questions
- red-team questions
- do-not-promote reasons
- SourceTask drafts
- LLM-generated query intents
- ambiguity/abstention
```

금지:

```text
- score output
- Stage output
- hard break final
- current_score_eligible final
- deterministic hardcoded query
```

LLM provider failure:

```text
PlannerPending / ProviderPending
```

으로 남긴다.

출력:

```text
planner_runs.jsonl
llm_prompts.jsonl
llm_responses.jsonl
planner_validation.json
```

Hard acceptance:

```text
selected_L3_count > 0
planner_call_count > 0
real_planner_success_count > 0 or exact LLM blocker
planner_score_stage_key_count = 0
future_outcome_prompt_leak_count = 0
source_primary_copy_without_reason_count = 0
provider_failure_final_score_count = 0
```

한글 커밋:

```text
Phase 25 canonical Research Brain current 조사계획 실제 실행
```

---

# 13. Phase 26 — Question-Centric SourceTask Materialization

`DailySourceTaskRecord`에 맞는 bounded task를 실제 생성한다.

각 task에는 내부적으로 다음이 있어야 한다.

```text
task_id
target_id
question_task_id
recipe_id
question_to_answer
why_material
accepted_predicates
required_entities
required_values_units
time_scope
counter_questions
rejection_conditions
source_class
preferred_document_types
preferred_sections
max_queries
max_candidates
max_fetches
max_retries
stop_on_resolution
allows_general_web
official_first_attempted
official_gap_reasons
```

공식 우선:

```text
DART/KIND/KRX/CompanyGuide/IssuerIR
→ gap 남음
→ TrustedNews/Naver/Web bounded fallback
```

예:

```text
FCF gap을 Naver부터 보내지 않는다.
공급계약 gap을 DART보다 Naver 먼저 보내지 않는다.
```

기존 `naver_news.py`의 deterministic company/sector query templates는
canonical live path에서 사용 금지한다.

Naver는 transport 역할만 한다.

```text
Research Brain query
→ validation
→ Naver API request
```

Hard acceptance:

```text
generic_verify_primitive_task_count = 0
empty_question_task_count = 0
empty_success_condition_count = 0
official_first_violation_count = 0
hardcoded_query_template_used_in_canonical_path_count = 0
unbounded_source_task_count = 0
```

한글 커밋:

```text
Phase 26 질문 중심 SourceTask와 official-first query 경로 구현
```

---

# 14. Phase 27 — Real Source Acquisition Orchestrator

기존 connector를 재사용하되 실제 기능이 약하면 보강한다.

## OpenDART

필수:

```text
- corp code index
- bulk disclosure index by date
- symbol/corp mapping
- latest regular report
- material disclosure
- full official document/API record
- financial actual where available
- correction/cancellation/supersession
```

## KRX

필수:

```text
- current universe
- current market/status
- price/trading value baseline
- actual relevant structured output
```

KRX main page HTML health check만으로 충족 금지.

## KIND

필수:

```text
- symbol-specific risk/listing/disclosure status
```

KIND main portal page 하나를 모든 symbol의 risk evidence로 쓰지 않는다.

## CompanyGuide

필수:

```text
- symbol-specific consensus/revision
- fetched page date/currentness
- structured parse provenance
```

## IssuerIR

필수:

```text
- official IR/newsroom discovery
- earnings presentation / conference call / business update
- source URL/content hash/published date
```

## TrustedNews/Naver/Web

필수:

```text
- Research Brain-generated query만
- result discovery
- original source preference
- full article/PDF fetch
- repost dedupe
- wrong-subject rejection
- snippet score 금지
```

Acquisition result classes:

```text
REAL_PROVIDER_FETCH
FRESH_PROVIDER_CACHE
EXISTING_LEDGER_REFRESH
NO_RESULT
PROVIDER_FAILED
AUTH_FAILED
RATE_LIMITED
REJECTED_BY_POLICY
SOURCE_EXHAUSTED
BUDGET_EXHAUSTED
```

Generic portal result는:

```text
PROVIDER_HEALTH_ONLY
```

로 분리하고 symbol evidence로 쓰지 않는다.

출력:

```text
provider_requests.jsonl
provider_fetch_results.jsonl
evidence_documents.jsonl
web_search_tasks.jsonl
web_search_results.jsonl
web_fetched_documents.jsonl
web_rejected_documents.jsonl
provider_call_report.json
```

Hard acceptance:

```text
actual_live_or_fresh_document_count > 0
generic_portal_counted_as_symbol_evidence = 0
fetched_without_content_hash_count = 0
future_document_count = 0
snippet_document_count = 0
snapshot_counted_live_count = 0
wrong_subject_document_to_claim_count = 0
provider_failure_masked_no_result_count = 0
```

한글 커밋:

```text
Phase 27 official-first live source acquisition과 full document provenance 구현
```

---

# 15. Phase 28 — Current Claim Compiler & Provenance

실제 fetched document에서 current claim을 만든다.

순서:

```text
EvidenceDocument
→ EvidenceAnchor
→ contract-blind RawAssertion
→ subject/target resolution
→ temporal/effective period
→ lifecycle/supersession
→ contradiction
→ recipe/primitive mapping
→ accepted claim
→ DailyClaimProvenance
```

`DailyClaimProvenance` 요구사항을 만족한다.

```text
- document_id
- source_url
- published_date
- available_date
- content_sha256
- full document text
- exact quote
- source IDs
- anchor IDs
- mapping IDs
- extraction provider
- mapping provider
- DIRECT
- CURRENT
- ACCEPTED
- fetched=true
- anchor_verified=true
- source_proxy_only=false
```

LLM raw extractor는 보지 않는다.

```text
- desired primitive
- score
- Stage
- failed Green gate
- historical outcome
```

Structured official API는 deterministic extraction을 허용하되,
명확한 subject/date/value/locator가 있어야 한다.

Unstructured text는 LLM extractor가 실패하면 mention-only/pending이다.

Task satisfaction:

```text
DIRECT_TASK_SATISFIED
REROUTED_CLAIM_ACCEPTED_ORIGINAL_GAP_OPEN
BASELINE_CLAIM_REUSED
LIFECYCLE_REFRESH_ONLY
COUNTER_CLAIM_FOUND
NO_RELEVANT_CLAIM
WRONG_SUBJECT
STALE_ONLY
PROVIDER_FAILED
SOURCE_EXHAUSTED
```

Hard acceptance:

```text
accepted_claim_without_provenance_count = 0
accepted_claim_without_exact_quote_count = 0
accepted_claim_without_content_hash_count = 0
wrong_subject_score_count = 0
source_proxy_current_claim_count = 0
rerouted_claim_closed_original_gap_count = 0
old_unknown_risk_penalty_count = 0
unstructured_rule_fallback_score_count = 0
```

한글 커밋:

```text
Phase 28 live fetched document를 current claim provenance로 연결
```

---

# 16. Phase 29 — Append-Only Ledger & Adaptive Gap Closure

Current claim ledger는 append-only다.

```text
새 claim 추가
supersession 명시
contradiction 연결
invalidation reason
lifecycle refresh
```

기존 claim을 조용히 덮어쓰거나 삭제하지 않는다.

실패 원인별 next action:

```text
NO_DOCUMENT_FOUND
WRONG_SUBJECT
STALE_ONLY
GENERIC_CONTEXT_ONLY
REROUTED_PRIMITIVE
MAPPING_REJECTED
CONTRADICTION_OPEN
PROVIDER_FAILED
SOURCE_EXHAUSTED
BUDGET_EXHAUSTED
```

각 원인별로 다음 attempt가 달라야 한다.

```text
- query 수정
- provider 변경
- document section 변경
- target directness 강화
- date/lifecycle query
- counter-claim search
```

동일 query 반복 금지.

LLM에게 rejection context를 돌려주되,
deterministic fallback query template를 만들지 않는다.

종료:

```text
RESOLVED
DISPROVED
SOURCE_PENDING
PROVIDER_PENDING
BUDGET_PENDING
SOURCE_EXHAUSTED
```

material gap이 남으면:

```text
score_valid=false
raw reference score optional
canonical Stage 0/Pending
```

Hard acceptance:

```text
silent_claim_overwrite_count = 0
identical_retry_count = 0
retry_without_failure_reason_count = 0
unresolved_material_gap_final_score_count = 0
provider_failure_low_score_count = 0
round_limit_score_valid_true_count = 0
```

한글 커밋:

```text
Phase 29 append-only current claim ledger와 adaptive evidence closure 구현
```

---

# 17. Phase 30 — Primitive / Score / Atomic Stage Decision

검증된 current claims만 PrimitiveState에 들어간다.

```text
PRESENT_CURRENT
ABSENT_CURRENT
UNKNOWN
CONTRADICTED
HISTORICAL_ONLY
RESOLVED
```

ScoreContribution:

```text
nonzero score
→ support claim IDs 필수
```

Score type:

```text
EVENT_EVIDENCE_PARTIAL
FULL_E2R_100
NO_SCORE
```

FULL_E2R_100 조건:

```text
- material primitive assessment 완료
- accepted current claim 존재
- contradiction 상태 정리
- required source gap 없음
- score_valid=true
- StageCourt trace
```

Atomic decision에서 한 번에 가져온다.

```text
stage
score
score status
claims
contributions
hard break
missing conditions
trace
```

Hard break:

```text
target direct
current OPEN
source-backed
material
unresolved
```

이 모두 필요하다.

금지:

```text
qualification delay 하나로 sticky hard 4C
old audit issue로 current hard break
provider failure로 Red
```

Hard acceptance:

```text
claimless_nonzero_score_count = 0
orphan_score_count = 0
event_partial_as_full_score_count = 0
atomic_stage_trace_mismatch_count = 0
hard_break_without_current_direct_open_count = 0
unexplained_score_delta_count = 0
```

한글 커밋:

```text
Phase 30 current claim 기반 deterministic score와 Atomic StageDecision 연결
```

---

# 18. Phase 31 — CurrentOperationRunnerInput Manifest Builder

가장 중요한 Phase다.

구현:

```text
CurrentOperationInputMaterializer
CurrentOperationRunnerInputBuilder
```

스스로 생성해야 하는 필드:

```text
as_of_date
universe
baseline_lanes
triggers
claims
claim_provenance
source_tasks
atomic_decisions
deep_executions
config
```

절대 사용자에게 수동 작성 요청하지 않는다.

Manifest output:

```text
output/current_operation_inputs/<AS_OF_DATE>.json
output/live_materialization/<AS_OF_DATE>/current_operation_input_manifest.json
```

Manifest validation:

```text
- full universe nonempty
- as_of_date match
- production config test_mode=false
- claim provenance exact
- budgets bounded
- source task official-first
- atomic decisions linked
- provider/runtime pending explicit
```

`run_e2r_current_operation.py` 수정:

```text
A. --input-manifest가 있으면 replay/evaluate
B. --materialize-live-input true
   + --live-materialization-authorized true이면
   materializer 실행 → manifest 저장 → evaluator 실행
C. 둘 다 없으면 기존 fail-closed
```

Hard acceptance:

```text
authorized_live_run_manifest_missing_exit_count = 0
user_manual_manifest_required_count = 0
materialized_manifest_schema_error_count = 0
materializer_evaluator_as_of_mismatch_count = 0
```

한글 커밋:

```text
Phase 31 canonical current CLI live input 자동 materialization 연결
```

---

# 19. Phase 32 — Live Current Operational Orchestrator

공식 CLI:

```bash
PYTHONPATH=src python -m e2r.cli.run_e2r_current_operation \
  --as-of-date 2026-07-10 \
  --mode production_bounded \
  --universe krx \
  --materialize-live-input true \
  --live-materialization-authorized true \
  --run-profile configs/e2r_production_daily_v1.json \
  --output-root output/current_operation/live_2026-07-10 \
  --fail-on-critical true
```

실행 단계:

```text
authorization
→ credential/provider preflight
→ current universe
→ current state load/bootstrap
→ baseline lanes
→ trigger fusion
→ depth selection
→ Research Brain
→ SourceTask
→ acquisition
→ claim compiler
→ adaptive closure
→ atomic decision
→ CurrentOperationRunnerInput
→ pure evaluator
→ Operational Envelope
```

최종 output:

```text
universe.jsonl
baseline_lanes.jsonl
trigger_signals.jsonl
planner_runs.jsonl
source_tasks.jsonl
source_task_executions.jsonl
evidence_documents.jsonl
evidence_anchors.jsonl
raw_assertions.jsonl
adjudicated_claims.jsonl
accepted_claims.jsonl
claim_provenance.jsonl
primitive_states.jsonl
score_contributions.jsonl
atomic_decisions.jsonl
deep_executions.jsonl
current_operation_input_manifest.json
current_stage_status.jsonl
current_watchlist.json
operator_digest.md
live_operational_envelope.json
audit_summary.json
```

완료 상태:

```text
FULL_THESIS
DISPROVED
SOURCE_PENDING
PROVIDER_PENDING
BUDGET_PENDING
BASELINE_ONLY
OFFICIAL_LIGHT
```

Stage0/Pending은 정직한 결과일 수 있다.
하지만 manifest 부재 때문에 전부 Stage0인 것은 실패다.

한글 커밋:

```text
Phase 32 실제 current operation live 오케스트레이터 완성
```

---

# 20. Phase 33 — Full-Universe Census Orchestrator

공식 Census CLI:

```bash
PYTHONPATH=src python -m e2r.cli.run_e2r_census_mode \
  --as-of-date 2026-07-10 \
  --mode census_selective_deep \
  --universe krx \
  --materialize-live-input true \
  --live-materialization-authorized true \
  --run-profile configs/e2r_census_selective_deep_v1.json \
  --shard-count <N> \
  --resume true \
  --output-root output/census/live_2026-07-10 \
  --fail-on-critical true
```

Census 규칙:

1. full eligible universe baseline.
2. all symbols get source timeline/last effective thesis/baseline lanes.
3. selected candidates only L3/L4/L5.
4. no-event/no-thesis can be Stage0.
5. provider/source failure is Pending.
6. active old thesis remains.
7. market anomaly only gets investigation signal.
8. score requires accepted claim.
9. no forced score for every ticker.
10. no forced archetype quota.

Sharding:

```text
- deterministic shard
- checkpoint
- resume
- idempotent rerun
- no duplicate claims
- deterministic merge
```

Census outputs:

```text
census_stage_map.jsonl
census_stage_map.csv
stage_distribution.json
sector_distribution.json
depth_distribution.json
provider_gap_report.json
source_gap_report.json
watchlist_seed.json
deep_backfill_queue.json
operator_digest.md
```

Hard acceptance:

```text
every eligible symbol represented exactly once
missing_symbol_count = 0
duplicate_symbol_count = 0
source_timeline_count == eligible_count
baseline_lane_count == eligible_count * 4
unknown_default_count = 0
provider_pending_without_failure_count = 0
stage0_without_source_attempt_count = 0
claimless_nonzero_score_count = 0
```

한글 커밋:

```text
Phase 33 current source corpus 기반 전체 Census selective-deep 완성
```

---

# 21. Phase 34 — Historical Source-Backed Replay Closure

이전 historical replay는 semantic parity와 future-leakage 안전성은 통과했지만,
실제 replay-ready source가 0인 상태를 그대로 최종 READY에 포함하면 안 된다.

Historical replay와 current operation은 분리한다.

작업:

```text
- URL-backed historical case의 full source fetch
- content hash
- published/available date
- historical as-of
- target directness
- exact quote/table/API locator
- positive/guard mapping
- frozen Evidence OS replay
```

source_proxy/evidence_url_pending case:

```text
SOURCE_REPAIR_REQUIRED
```

로 남기고 score하지 않는다.

Canary:

```text
C06
C08
C15
C17
C24
C28
```

는 상세 source-backed positive/guard replay를 수행한다.

전체 registry:

```text
URL-backed case가 있는 archetype은
replay-ready 또는 exact external blocker여야 한다.
```

출력:

```text
historical_source_backed_replay.jsonl
historical_source_repair_queue.jsonl
historical_replay_provenance.jsonl
```

Hard acceptance:

```text
URL string only replay ready = 0
source proxy replay score = 0
future leakage = 0
wrong subject replay accepted = 0
canary source-backed replay count > 0
```

한글 커밋:

```text
Phase 34 historical URL-backed case 실제 source replay 연결
```

---

# 22. Phase 35 — Targeted Live Smoke

Production logic에는 종목 하드코딩 금지지만,
explicit smoke/validation target은 허용한다.

필수 smoke:

```text
005930 삼성전자
000660 SK하이닉스
```

추가로 대형 섹터 L1~L9에서 최소 1개씩 무작위/규칙 기반 sample.

삼성/하이닉스 출력은 분리한다.

```text
daily event status
full thesis status
accepted current claims
source tasks
provider/source gaps
score type
StageCourt trace
```

DART event partial score를 HBM full thesis score로 부르지 않는다.

C06 full-thesis task는 다음을 검사한다.

```text
- customer allocation
- sold-out/pre-sold capacity
- qualification
- shipment
- revenue mix
- margin/FCF/revision bridge
- conventional memory drag
- current lifecycle
```

Smoke pass는 Green을 강제하지 않는다.

Pass:

```text
- actual live/fresh docs
- real planner trace if deep selected
- claim provenance
- deterministic terminal status
```

Blocker가 있으면 exact pending.

출력:

```text
docs/operational/e2r_live_targeted_smoke_report.json
```

한글 커밋:

```text
Phase 35 삼성전자·하이닉스와 전 섹터 live smoke 검증
```

---

# 23. Phase 36 — Full Live Acceptance Run

최초 acceptance 기준일:

```text
2026-07-10 KST
```

실행일이 달라지면 명시적 `as_of_date`를 사용하고 보고서에 적는다.

필수 실행:

```text
1. live bootstrap
2. live daily current
3. live full-universe Census baseline
4. live Census selective deep
5. historical source-backed replay
6. same manifest replay determinism
```

최소 current/Census 증거:

```text
eligible_universe_count > 1000
baseline lanes complete
nonempty trigger pool
selected L3/L4 count > 0
real planner calls > 0
source tasks > 0
real/fresh fetched docs > 0
accepted current claims > 0
claim provenance rows > 0
atomic decisions > 0
```

현재 시장이 조용하다는 이유로 Green을 요구하지 않는다.

그러나 full KRX에서:

```text
trigger=0
document=0
claim=0
```

이면 low-signal day로 통과하지 않는다.
materialization/source/selection failure로 조사한다.

동일 input manifest replay:

```text
same config/source/input hash
→ zero variance
```

---

# 24. Phase 37 — Runtime Observability & Conversion Funnel

다음을 provider/symbol/candidate/archetype별로 기록한다.

```text
universe
→ baseline attempt
→ trigger
→ depth
→ planner
→ SourceTask
→ query
→ search result
→ fetched document
→ relevant document
→ RawAssertion
→ adjudicated claim
→ accepted claim
→ primitive closure
→ score contribution
→ atomic decision
→ terminal status
```

핵심 지표:

```text
provider call/failure/rate limit
baseline coverage
trigger yield
deep selection yield
planner success
query novelty
full document fetch rate
relevant document rate
accepted claim rate
direct original-gap closure rate
rerouted claim rate
mapping rejection
full thesis/disproved/pending rate
runtime/cost/cache/checkpoint
```

Task shell 수나 search result 수만 progress로 말하지 않는다.

출력:

```text
docs/operational/e2r_live_conversion_funnel.json
docs/operational/e2r_live_runtime_sla.json
docs/operational/e2r_live_provider_performance.json
```

---

# 25. Phase 38 — Self-Repair Until Pass

이번 Goal은 실패 보고로 끝나지 않는다.

Coding-agent self-repair:

```text
run
→ leaf audit
→ failure cluster
→ root cause file/function
→ code/config/prompt/recipe patch
→ focused tests
→ same live/frozen run
→ before/after funnel
→ repeat
```

Runtime adaptive retry와 code self-repair를 분리한다.

Failure classes:

```text
MATERIALIZER_NOT_CALLED
UNIVERSE_NOT_MATERIALIZED
GENERIC_PORTAL_COUNTED_AS_DATA
BASELINE_LANE_MISSING
TRIGGER_FUSION_EMPTY
DEPTH_SELECTION_EMPTY
PLANNER_NOT_CALLED
QUERY_TEMPLATE_HARDCODED
OFFICIAL_FIRST_VIOLATION
DOCUMENT_NOT_FETCHED
CLAIM_PROVENANCE_MISSING
ORIGINAL_GAP_NOT_CLOSED
ATOMIC_DECISION_MISSING
CURRENT_MANIFEST_BUILD_FAILED
CENSUS_ALL_DEFAULT
EXTERNAL_PROVIDER_BLOCKER
```

규칙:

1. max iterations 10 이상.
2. 동일 failure가 남으면 계속 수정.
3. threshold 완화 금지.
4. fixture로 live pass 대체 금지.
5. report-only patch를 repair로 세지 않음.
6. 외부 blocker면 provider/env/request/error/affected scope를 정확히 남김.
7. 외부 blocker와 무관한 내부 Phase는 모두 완료.
8. 내부 미구현 blocker를 external blocker라고 부르지 않음.

생성:

```text
docs/operational/e2r_live_self_repair_log.json
docs/operational/e2r_live_self_repair_summary.md
```

---

# 26. 필수 Known-Bad Regression

반드시 실패해야 하는 fixture:

```text
1. live authorization=true인데 manifest 부재로 즉시 Stage0 종료
2. KRX homepage를 universe로 계산
3. KIND homepage를 모든 symbol의 risk observed로 계산
4. CompanyGuide generic page를 consensus로 계산
5. Naver snippet을 score claim으로 계산
6. deterministic hardcoded query template 사용
7. provider failure를 NO_RESULT로 변환
8. provider failure를 Red/low score로 확정
9. source_proxy historical memory를 current score로 사용
10. old resolved risk current penalty
11. rerouted claim으로 original gap closure
12. current material gap인데 FULL_E2R_100
13. claim provenance 없이 accepted claim
14. content hash와 document text 불일치
15. exact quote가 document에 없음
16. all Stage0 due source wiring failure를 Census PASS
17. test fixture manifest를 production live로 사용
18. snapshot URL을 live provenance로 사용
19. same source snapshot replay variance
20. current/Census source corpus hash 불일치
```

---

# 27. 필수 테스트

예시:

```text
tests/test_live_authorization_contract.py
tests/test_live_materializer_called_without_manifest.py
tests/test_live_provider_capability_matrix.py
tests/test_live_current_universe_materializer.py
tests/test_live_current_state_bootstrap.py
tests/test_live_baseline_lane_materializer.py
tests/test_live_trigger_fusion.py
tests/test_live_depth_policy.py
tests/test_live_brain_planner.py
tests/test_live_question_source_tasks.py
tests/test_live_official_first.py
tests/test_live_naver_transport_queries_from_llm.py
tests/test_live_source_acquisition.py
tests/test_live_claim_provenance.py
tests/test_live_adaptive_closure.py
tests/test_live_atomic_decision.py
tests/test_live_input_manifest_builder.py
tests/test_live_current_orchestrator.py
tests/test_live_census_orchestrator.py
tests/test_live_shard_resume.py
tests/test_live_runtime_observability.py
tests/test_live_known_bad_regressions.py
tests/test_historical_source_backed_replay.py
```

Hermetic full test:

```bash
PYTHONPATH=src python -m unittest discover -s tests -v
```

규칙:

```text
- no skipped Goal tests
- live credentials/network가 필요한 테스트는 transport fixture로 hermetic하게 검증
- 실제 live acceptance는 별도 command evidence로 검증
- test mode 결과로 production ready 선언 금지
```

---

# 28. 필수 출력 산출물

```text
docs/operational/e2r_live_materialization_forensic_baseline.md
docs/operational/e2r_live_materialization_architecture.md
docs/operational/e2r_live_provider_capability_matrix.json
docs/operational/e2r_live_credential_audit.json
docs/operational/e2r_live_provider_blocker_matrix.json
docs/operational/e2r_live_universe_audit.json
docs/operational/e2r_live_current_state_bootstrap_audit.json
docs/operational/e2r_live_baseline_lane_audit.json
docs/operational/e2r_live_trigger_fusion_audit.json
docs/operational/e2r_live_depth_selection_audit.json
docs/operational/e2r_live_brain_planner_audit.json
docs/operational/e2r_live_source_task_audit.json
docs/operational/e2r_live_source_acquisition_audit.json
docs/operational/e2r_live_claim_provenance_audit.json
docs/operational/e2r_live_adaptive_closure_audit.json
docs/operational/e2r_live_atomic_stage_audit.json
docs/operational/e2r_live_input_manifest_audit.json
docs/operational/e2r_live_current_acceptance_report.md
docs/operational/e2r_live_census_acceptance_report.md
docs/operational/e2r_historical_source_replay_report.md
docs/operational/e2r_live_targeted_smoke_report.json
docs/operational/e2r_live_conversion_funnel.json
docs/operational/e2r_live_runtime_sla.json
docs/operational/e2r_live_self_repair_summary.md
docs/operational/e2r_live_final_readiness_verdict.md
```

Leaf output:

```text
output/live_materialization/<AS_OF_DATE>/
output/current_state/<AS_OF_DATE>/
output/current_operation/live_<AS_OF_DATE>/
output/census/live_<AS_OF_DATE>/
output/historical_replay/source_backed_v1/
```

---

# 29. 독립 Reviewer Gate

Reviewer A — Universe & Baseline Fidelity

```text
actual current universe
eligibility
baseline lane completeness
generic portal misuse
```

Reviewer B — Brain & SourceTask Semantics

```text
LLM planner real use
hardcoded query absence
official-first
question-specific task
```

Reviewer C — Source & Claim Realness

```text
actual fetch
content hash
quote
target/date/current
source-proxy rejection
```

Reviewer D — Score & Stage Integrity

```text
claim-backed score
atomic decision
pending semantics
hard break
```

Reviewer E — Current/Census Separation & Consistency

```text
same source corpus
full universe coverage
selective deep
no forced archetype
```

Reviewer F — Live Orchestration & Runtime Honesty

```text
materializer actually called
manifest self-generated
provider calls
LLM/web calls
runtime mode honesty
```

각 reviewer:

```text
- report generator counter를 공유하지 않는다.
- leaf artifacts를 다시 읽는다.
- critical 1개면 FAIL.
- 99/100이라도 critical 1개면 FAIL.
```

---

# 30. 완료 라벨

중간:

```text
LIVE_MATERIALIZER_ARCHITECTURE_PASS
LIVE_PROVIDER_CAPABILITY_PASS
CURRENT_UNIVERSE_MATERIALIZATION_PASS
CURRENT_STATE_BOOTSTRAP_PASS
CURRENT_BASELINE_LANES_PASS
CURRENT_TRIGGER_FUSION_PASS
CURRENT_BRAIN_PLANNER_PASS
CURRENT_SOURCE_ACQUISITION_PASS
CURRENT_CLAIM_PROVENANCE_PASS
CURRENT_INPUT_MANIFEST_PASS
CURRENT_OPERATIONAL_BRAIN_PASS
FULL_UNIVERSE_CENSUS_BASELINE_PASS
CENSUS_SELECTIVE_DEEP_PASS
HISTORICAL_SOURCE_BACKED_REPLAY_PASS
```

최종:

```text
MEANINGFUL_E2R_RUNTIME_READY
```

외부 blocker:

```text
EXTERNAL_SOURCE_BLOCKER_NOT_READY
```

단, external blocker는 다음 조건에서만 허용한다.

```text
- internal materializer 구현 완료
- provider 호출 실제 시도
- credential/provider/network error leaf 존재
- affected scope 명시
- 내부 미구현 blocker 0
```

---

# 31. `MEANINGFUL_E2R_RUNTIME_READY` Hard Gate

다음이 모두 참이어야 한다.

## Architecture

```text
pure evaluator와 live materializer 분리
canonical CLI live materialization 경로 존재
legacy manifest-only path가 final production 경로를 막지 않음
```

## Live universe/baseline

```text
actual eligible KRX universe > 1000
all eligible symbols have required baseline lanes
all eligible symbols have source timeline / last effective thesis
```

## Brain/acquisition

```text
selected deep candidates > 0
real planner calls > 0
question-specific SourceTasks > 0
actual official/fresh fetched docs > 0
bounded Naver/Web calls if exact gaps require
```

## Claims/score/stage

```text
accepted current claim > 0
claim provenance > 0
score contribution > 0
atomic decision > 0
claimless score = 0
source proxy score = 0
provider failure final score = 0
```

## Current/Census

```text
current operation command PASS
Census baseline PASS
Census selective deep PASS
manifest was self-materialized
not all Stage0 because manifest/source path missing
```

## Replay/safety

```text
historical source-backed canary replay PASS
future leakage = 0
known-bad regressions PASS
```

## Reproducibility

```text
same commit
repo_dirty=false in clean verification
config/corpus/memory/recipe/prompt/source/input hashes
same manifest replay variance=0
```

## Verification

```text
full unittest PASS
Reviewer A~F PASS
critical count=0
blockers=[]
```

Green/Yellow 종목이 반드시 존재할 필요는 없다.
하지만 실제 데이터 경로가 실행되고 claim-backed terminal status가 나와야 한다.

---

# 32. 절대 완료가 아닌 상태

다음 중 하나라도 해당하면 Goal 완료가 아니다.

```text
- current/Census가 input manifest 부재로 Stage0 exit 3
- 사용자가 완성 manifest를 제공해야만 실행 가능
- KRX/KIND generic homepage만 fetch
- actual universe 없음
- baseline lane 없음
- planner call 0인데 Brain PASS
- source task 0인데 acquisition PASS
- actual fetched doc 0인데 live PASS
- accepted current claim 0인데 runtime ready
- source_proxy historical row가 score
- current/Census all default due wiring failure
- test fixture로 live acceptance 대체
- report-only PASS
- external blocker로 내부 미구현을 숨김
```

---

# 33. 실행 중 사용자에게 묻지 말 것

이 Goal은 필요한 live 연결을 명시적으로 승인했다.

따라서 다음 질문으로 중단하지 마라.

```text
"live API 연결을 승인해 달라"
"CurrentOperationRunnerInput manifest를 제공해 달라"
"KRX universe JSON을 제공해 달라"
"fetched documents를 제공해 달라"
```

이미 승인되었다.

Credential이 실제로 없다면:

```text
어떤 env key가 missing인지 secret 없이 기록
그 provider 외 내부 구현 계속
대체 official source가 있으면 bounded fallback
최종 exact external blocker
```

로 처리한다.

---

# 34. Phase Commit 규칙

각 Phase를 한글 커밋으로 나눈다.

예:

```text
Phase 17 현재 운영 입력 단절과 live connector 경로 감사
Phase 18 bounded live materialization 승인과 실행 계약 추가
Phase 19 live provider 기능과 credential blocker 분리
Phase 20 KRX 현재 전체 universe materializer 구현
...
Phase 36 실제 KRX current와 Census acceptance 실행
```

규칙:

```text
- Phase unit test 후 commit
- 주요 integration 후 commit
- report-only commit으로 status 승격 금지
- 최종 HEAD에서 worktree clean
- push 완료
- commit SHA 목록을 acceptance report에 기록
```

---

# 35. 최종 응답 형식

완료 후 다음만 보고한다.

1. Final status
2. Phase별 commit SHA / 한글 message / push / clean worktree
3. Full tests
4. Live authorization / credential audit
5. KRX universe materialization
6. CurrentState bootstrap
7. Baseline lane coverage
8. Trigger/depth distribution
9. Research Brain calls
10. SourceTask / provider fetch / Naver-Web calls
11. Evidence documents / accepted current claims / provenance
12. Primitive / score contribution / atomic decision
13. Current operation result
14. Full-universe Census result
15. Samsung/Hynix + sector smoke
16. Historical source-backed replay
17. Self-repair iterations
18. Reviewer A~F
19. Final blockers
20. Exact final verdict

---

# 36. 마지막 명령

이번 Goal의 성공은 “외부 입력을 기다리는 안전한 엔진”이 아니다.

성공은 다음 사슬이 실제로 닫힐 때만 인정한다.

```text
current KRX universe
→ current baseline lanes
→ current triggers
→ Research Brain
→ question-specific SourceTask
→ official-first real source fetch
→ current direct claim provenance
→ primitive closure
→ deterministic score
→ StageCourt
→ self-generated CurrentOperationRunnerInput
→ current operation
→ full-universe Census
```

`CurrentOperationRunner`는 순수 evaluator로 유지하되,
그 앞의 live materializer와 orchestrator를 완성하라.

실패하면 `EXTERNAL_SOURCE_BLOCKER_NOT_READY`라고 쓰고 끝내지 마라.

먼저 다음을 판정하라.

```text
내부 materializer가 없는가?
connector가 generic page만 가져오는가?
credential이 없는가?
provider가 실패했는가?
문서는 가져왔지만 claim이 안 닫히는가?
```

내부 문제라면 코드를 수정하고 같은 실행을 다시 돌린다.

외부 provider 문제만 exact blocker로 남긴다.

최종적으로 current/Census가 실제 fetched document provenance를 사용해 PASS하고,
Reviewer A~F와 full tests가 모두 통과한 경우에만:

```text
MEANINGFUL_E2R_RUNTIME_READY
```

를 선언하라.
