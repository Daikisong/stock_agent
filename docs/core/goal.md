# E2R RESEARCH-GRADE EVIDENCE ACQUISITION & SEMANTIC SCORING CLOSURE MASTER GOAL v2
## Phase 58+ — Strict Rubric Totality / Business-Mechanism Scope / Question↔Claim↔Impact↔Component Reconciliation / Blind Deep-Research Benchmark / Samsung & SK Hynix True Cutover

너는 `Daikisong/stock_agent` 레포의 수석 아키텍트이자 구현 에이전트다.

이번 Goal은 방어 게이트를 하나 더 붙이는 작업이 아니다.

이번 Goal의 목적은 현재 레포에 이미 만들어진 다음 사슬을 **의미적으로 완성**하는 것이다.

```text
current KRX universe
→ Research Brain
→ question-specific SourceTask
→ official / IR / report / Naver-Web acquisition
→ full EvidenceDocument
→ accepted current claim
→ many-to-many impact
→ component assessment
→ calibrated score
→ StageCourt
```

현재 레포는 위 사슬의 형태를 만들었지만, 최신 `52f09f3` 기준으로 다음 치명적 semantic 결함이 남아 있다.

---

# 0. 현재 확인된 치명적 결함

## 0.1 Support type enum과 cap table이 서로 다르다

현재 `ClaimImpactProposal.SUPPORT_TYPES`에는 다음이 있다.

```text
DIRECT_ACTUAL
DIRECT_FORWARD
PARTIAL_BRIDGE
PROFILE_ONLY
DISCOVERY_ONLY
RISK_OPEN
RISK_RESOLVED
```

그런데 `evidence_impact_rubric_compiler.py`의 `actual_vs_forward_rules`에는 다음만 있다.

```text
DIRECT_ACTUAL
DIRECT_FORWARD
PROFILE_ONLY
DISCOVERY_ONLY
```

`ImpactValidator`는 다음처럼 조회한다.

```python
rubric.actual_vs_forward_rules.get(p.support_type, 0.0)
```

따라서 다음 support type은 오류를 내지 않고 조용히 0점이 된다.

```text
PARTIAL_BRIDGE
RISK_OPEN
RISK_RESOLVED
```

실제 SK하이닉스 leaf에는 `shipment_or_revenue_mix → earnings_visibility`,
`capacity_supply_response → earnings_visibility/bottleneck_pricing` 같은 impact가
`support_type_cap=0.0`, `validated_credit_fraction=0.0`으로 사라졌다.

이것은 보수적 scoring이 아니라 **scoring-critical lookup table 누락**이다.

## 0.2 source/temporal/support cap 누락도 조용히 0점이 된다

현재 validator는 다음 lookup에 기본 0을 사용한다.

```text
source_family_caps.get(..., 0.0)
freshness_caps.get(..., 0.0)
actual_vs_forward_rules.get(..., 0.0)
```

새 source family, temporal scope, support type이 enum/schema에는 존재하지만
cap table에 없으면 configuration error가 아니라 claim 0점으로 위장된다.

## 0.3 질문은 SUPPORTED인데 component는 VERIFIED_ABSENT가 된다

SK하이닉스 `question_closure.jsonl`에는 다음 질문들이 `SUPPORTED` 또는
`PARTIALLY_SUPPORTED`로 남아 있다.

```text
capacity_constraint_presold_status
shipment_mass_production_generation
hbm_ai_memory_revenue_mix
revenue_operating_profit_conversion
margin_fcf_conversion
capex_supply_oversupply
```

그런데 최종 component는 다음처럼 남아 있다.

```text
earnings_visibility = VERIFIED_ABSENT_AFTER_SEARCH / 0점
bottleneck_pricing = VERIFIED_ABSENT_AFTER_SEARCH / 0점
```

즉 질문→claim 단계에서는 증거가 있다고 했지만,
impact cap 누락으로 0점이 된 뒤 component 단계에서는
“증거를 조사했으나 없었다”고 뒤집힌다.

## 0.4 삼성 Foundry/Tesla 계약이 C06 HBM 고객 배정 질문을 닫는다

삼성전자 `current_customer_allocation_commitment` 질문은
`CLM-464ca5cde1b30c363997` 때문에 `SUPPORTED`가 되었다.

그러나 이 claim은 다음이다.

```text
DS부문 Foundry 사업부
Tesla
반도체 위탁생산 계약
```

대상 회사가 삼성전자라는 것만 맞을 뿐,
C06 HBM/메모리 고객 배정·선판매 CAPA 증거가 아니다.

현재 시스템은:

```text
issuer directness
```

는 확인하지만:

```text
business segment
product family
technology
economic mechanism
```

의 직접성을 충분히 확인하지 않는다.

## 0.5 `VERIFIED_ABSENT_AFTER_SEARCH`가 내부 scoring bug를 숨긴다

현재 component builder는 nonzero credit impact가 없고
`search_exhaustion_proof`가 있으면 absence를 terminal로 만들 수 있다.

따라서 다음이 가능하다.

```text
positive claim 발견
→ valid impact proposal 생성
→ cap table 누락으로 credit 0
→ support impact 목록에서 사라짐
→ search proof 존재
→ VERIFIED_ABSENT_AFTER_SEARCH
→ full_score_valid=true
```

이것은 “증거가 없음”이 아니라 “증거를 scoring code가 죽임”이다.

## 0.6 counter impact가 component 점수에서 사실상 무시된다

현재 component builder는 support와 counter를 구분하지만:

```text
support가 있으면 support 합계만으로 verified_points 계산
counter가 동시에 있어도 점수를 줄이거나 cap하지 않음
```

counter만 있을 때만 `VERIFIED_COUNTER`가 된다.

따라서:

```text
HBM capacity 확대
→ capital allocation에는 positive
→ scarcity/bottleneck에는 counter
```

같은 양면 impact가 한쪽 점수에는 들어가고,
다른 쪽 counter effect는 소멸할 수 있다.

## 0.7 같은 문서·같은 경제적 사실을 여러 claim으로 쪼개 중복 credit할 수 있다

현재 duplicate economic key에는 `claim_id`가 들어간다.

```text
claim_id + component + direction + evidence_family
```

따라서 동일 문서·동일 실적 사실을 여러 RawAssertion/claim으로 분해하면
각 claim이 별도 credit budget을 받을 수 있다.

특히 `information_confidence`는 같은 공식 문서에서 뽑힌 여러 claim만으로
쉽게 만점이 될 수 있다.

## 0.8 full-thesis StageCourt가 “claim 하나 있음”을 자동 Stage1 event로 쓴다

현재 `AtomicStageCourtV2`는 full score가 valid일 때 다음을 넘긴다.

```python
company_event_score = 60.0 if claim_ids else 0.0
high_quality_company_event = bool(claim_ids)
```

즉 accepted claim이 하나라도 있으면,
그 claim이 material company event인지와 무관하게 Stage1 조건이 열린다.

full-thesis score와 daily event overlay가 다시 섞인 것이다.

## 0.9 claim eligibility field가 서로 모순된다

현재 accepted claim에는 다음이 함께 존재할 수 있다.

```text
current_score_eligible = false
scoring_readiness_eligible = true
```

어느 plane에서 score eligible인지가 boolean 여러 개로 분산돼 있다.

ledger acceptance, SourceTask satisfaction, component scoring, risk scoring,
Stage evidence가 같은 의미로 섞이면 안 된다.

## 0.10 readiness가 semantic 모순을 검사하지 않는다

현재 readiness는 다음은 확인한다.

```text
organic claim 존재
validated impact 존재
verified points > 0
full_score_valid=true
FULL_E2R_100
trace 존재
```

그러나 다음은 검사하지 않는다.

```text
SUPPORTED 질문이 ABSENT component로 끝났는가
positive impact가 missing cap 때문에 0점이 됐는가
cross-business claim이 질문을 닫았는가
counter impact가 무시됐는가
같은 fact가 여러 claim으로 중복 credit됐는가
```

그래서 의미적으로 모순된 결과도 READY가 될 수 있다.

## 0.11 증거 수집 품질을 검증하는 독립 benchmark가 없다

현재 source acquisition이 실제로 실행되지만,
“GPT Pro 수준의 깊은 조사에서 쉽게 찾을 수 있는 중요한 source-backed fact를
운영 pipeline도 찾았는가?”를 비교하는 독립 benchmark가 없다.

문서 수, 검색 결과 수, LLM 호출 수는 기록하지만:

```text
material fact recall
question closure recall
counter-evidence recall
supersession/lifecycle recall
```

을 검증하지 않는다.

---

# 1. 이번 Goal의 최종 목표

최종 구조는 다음이어야 한다.

```text
Research-grade current source dossier
→ mechanism-scoped accepted claims
→ strict-total impact rubric
→ support/counter/resolution many-to-many impacts
→ question↔impact↔component reconciliation
→ research-calibrated subcriterion score
→ contradiction-aware component assessment
→ honest full-score validity
→ deterministic StageCourt
```

삼성전자와 SK하이닉스는 이 구조의 mandatory acceptance canary다.

두 종목에 높은 점수나 Green을 강제하지 않는다.

하지만 두 종목처럼 공개 자료가 풍부한 회사를 조사하고도:

```text
증거를 놓침
찾은 증거를 cap 누락으로 0점 처리
다른 사업부 증거를 HBM 증거로 사용
SUPPORTED와 ABSENT가 동시에 존재
counter를 무시
```

하는 상태는 절대 통과시키지 않는다.

---

# 2. 최종 역할 분리

## 2.1 Research Brain

Research Brain은 다음을 담당한다.

```text
- current hypothesis
- material question
- source route
- LLM-generated query intent
- source/document section selection
- claim extraction
- evidence impact proposal
- counter thesis
- missing/unsupported aspect
```

## 2.2 Deterministic code

Code는 다음을 담당한다.

```text
- source URL / document ID / content hash
- exact quote / table locator
- target / segment / product / mechanism directness
- current date / lifecycle / supersession
- rubric/schema totality
- allowed edge
- cap
- fact dedupe
- source correlation
- counter aggregation
- calibrated component point
- total score
- StageCourt
```

## 2.3 LLM 금지 영역

LLM은 다음을 출력하지 않는다.

```text
final total score
final Stage
expected score
expected Stage
historical future return
MFE/MAE
```

---

# 3. 이번 작업의 완료 라벨

기존 `MEANINGFUL_E2R_SCORING_READY`는 이번 Goal 완료 전까지
다음으로 재분류한다.

```text
ORGANIC_EVIDENCE_TO_SCORE_PIPELINE_PARTIAL_PASS
SEMANTIC_SCORING_CLOSURE_NOT_READY
RESEARCH_GRADE_EVIDENCE_ACQUISITION_NOT_VERIFIED
```

이번 Goal의 최종 라벨은 versioned label로 새로 만든다.

```text
MEANINGFUL_E2R_SCORING_READY_V2
```

기존 label alias는 V2 hard gate가 모두 통과할 때만 활성화한다.

---

# 4. 절대 금지사항

1. 특정 종목의 expected score/Stage를 하드코딩하지 마라.
2. 삼성전자·SK하이닉스 symbol 조건을 production semantic logic에 넣지 마라.
3. support type cap을 임의 숫자로 채우고 replay 없이 통과하지 마라.
4. scoring-critical mapping lookup에 `.get(key, 0.0)` 기본값을 쓰지 마라.
5. missing cap을 0점으로 처리하지 마라.
6. issuer가 같다는 이유로 다른 사업부·제품·경제 메커니즘 claim을 사용하지 마라.
7. Foundry 계약을 C06 HBM 고객 배정으로 쓰지 마라.
8. positive claim/impact가 있는데 `VERIFIED_ABSENT_AFTER_SEARCH`를 만들지 마라.
9. `SUPPORTED` 질문과 `ABSENT` component의 모순을 warning으로 넘기지 마라.
10. counter impact를 audit용으로만 남기고 점수에 반영하지 않는 구조를 유지하지 마라.
11. 같은 문서·같은 경제적 fact의 claim 수로 점수를 부풀리지 마라.
12. 모든 accepted claim을 high-quality company event로 처리하지 마라.
13. accepted claim 수만으로 Stage1을 열지 마라.
14. claim eligibility boolean을 서로 모순되게 유지하지 마라.
15. controlled probe/fixture/gold research source를 organic production evidence로 주입하지 마라.
16. 독립 gold dossier를 production query planner에 보여주지 마라.
17. gold dossier의 URL을 production seed로 직접 주입하지 마라.
18. 검색 결과 snippet을 score evidence로 쓰지 마라.
19. source_proxy/history row를 current score로 쓰지 마라.
20. historical MFE/MAE를 current prompt에 넣지 마라.
21. provider failure를 absence로 처리하지 마라.
22. 검색 budget exhaustion을 evidence absent로 처리하지 마라.
23. 모든 question을 terminal로 만들기 위해 억지로 `EVALUATED_ABSENT` 처리하지 마라.
24. threshold/weight를 바꿔 삼성·하이닉스를 통과시키지 마라.
25. 새 evidence를 cherry-pick해 기존 scoring bug를 가리지 마라.
26. 동일 frozen corpus 수리 전 새 live search 결과로만 통과하지 마라.
27. report-only commit으로 READY를 승격하지 마라.
28. known-bad fixture를 삭제하거나 expected result를 완화하지 마라.
29. `docs/core/goal*.md` 사용자 변경을 되돌리지 마라.
30. 실패 후 같은 query만 반복하고 self-repair라고 부르지 마라.

---

# 5. 실행 프로토콜

## 5.1 Read-only forensic first

코드 수정 전에 현재 HEAD와 leaf를 다시 읽는다.

필수 대상:

```text
src/e2r/research_brain/scoring/claim_impact_ledger.py
src/e2r/research_brain/scoring/impact_validator.py
src/e2r/research_brain/scoring/component_assessment.py
src/e2r/research_brain/scoring/component_scorer.py
src/e2r/research_brain/scoring/atomic_stagecourt_v2.py
src/e2r/research_brain/scoring/scoring_readiness.py
src/e2r/research_brain/scoring/evidence_impact_adjudicator.py
src/e2r/research_brain/compiler/evidence_impact_rubric_compiler.py
configs/e2r_evidence_impact_rubric_semantics_v1.json
output/evidence_to_score/c06/2026-07-11/005930/**
output/evidence_to_score/c06/2026-07-11/000660/**
```

## 5.2 동일 corpus 우선 수리

먼저 52f09f3에서 생성된 동일 Samsung/Hynix corpus를 frozen input으로 사용한다.

순서:

```text
same documents
same accepted claims
same provenance
→ 새 semantic bridge 재실행
```

이 frozen corpus에서 결함이 해결되기 전에는
새 문서를 더 가져와 PASS하지 않는다.

## 5.3 그 다음 live deep research

frozen corpus semantic repair가 PASS한 뒤에만
새 live acquisition을 실행한다.

## 5.4 Phase별 한글 commit/push

각 Phase는 focused test 후 한글 commit/push.

## 5.5 Self-repair

```text
fail
→ failure cluster
→ exact file/function/config
→ patch
→ focused tests
→ same frozen run
→ same live run
→ before/after metric
```

---

# 6. Phase 58 — Semantic Scoring Forensic Baseline

생성:

```text
docs/operational/e2r_semantic_scoring_v2_forensic_baseline.md
docs/operational/e2r_support_type_cap_matrix_before.json
docs/operational/e2r_question_component_consistency_before.json
docs/operational/e2r_business_mechanism_scope_failures_before.json
docs/operational/e2r_counter_credit_failures_before.json
docs/operational/e2r_fact_duplication_before.json
docs/operational/e2r_stage_event_injection_before.json
```

반드시 측정:

```text
- declared support type count
- cap table support type count
- missing support type count
- source cap missing count
- temporal cap missing count
- positive proposal zeroed by missing cap count
- counter proposal zeroed by missing cap count
- SUPPORTED question → ABSENT component count
- PARTIALLY_SUPPORTED question → ABSENT component count
- cross-business question closure count
- same-document duplicate credit count
- same-fact duplicate credit count
- support+counter component where counter effect=0 count
- accepted-claim event score injection count
- eligibility field contradiction count
```

Samsung/Hynix exact baseline rows를 문서화한다.

커밋:

```text
Phase 58 증거영향 0점 소거와 semantic 모순 기준선 감사
```

---

# 7. Phase 59 — Scoring-Critical Schema Totality

모든 scoring-critical enum과 lookup table을 total schema로 만든다.

## 7.1 Enum registry

Canonical registry:

```text
directions
support_types
strength_bands
completeness_bands
causal_distances
temporal_scopes
source_families
component_aggregation_modes
counter_effect_modes
```

## 7.2 Exact key coverage

모든 rubric/contract는 enum의 필요한 key를 완전히 가져야 한다.

금지:

```python
mapping.get(key, 0.0)
```

허용:

```python
require_scoring_key(mapping, key)
```

missing이면:

```text
SCORING_CONTRACT_INCOMPLETE
```

로 hard fail.

## 7.3 Support type policy

다음을 모두 정의한다.

```text
DIRECT_ACTUAL
DIRECT_FORWARD
PARTIAL_BRIDGE
PROFILE_ONLY
DISCOVERY_ONLY
RISK_OPEN
RISK_RESOLVED
```

`PARTIAL_BRIDGE`, `RISK_OPEN`, `RISK_RESOLVED`의 cap은 임의로 정하지 않는다.

다음에서 컴파일한다.

```text
- historical source-backed cases
- existing score simulations
- shadow rule candidates
- positive/counterexample relative ordering
```

각 cap에는:

```text
research_case_refs
rationale
replay_result
```

가 있어야 한다.

## 7.4 Direction-specific rules

SUPPORT와 COUNTER에 동일 cap table을 무비판적으로 쓰지 않는다.

```text
support_credit_cap
counter_effect_cap
resolution_effect
```

를 분리한다.

Hard acceptance:

```text
missing_scoring_key_count = 0
silent_zero_default_count = 0
partial_bridge_missing_cap_count = 0
risk_open_missing_cap_count = 0
risk_resolved_missing_cap_count = 0
unknown_source_family_silent_zero_count = 0
unknown_temporal_scope_silent_zero_count = 0
```

커밋:

```text
Phase 59 scoring cap 전수성과 silent-zero 금지 구현
```

---

# 8. Phase 60 — Archetype Business-Mechanism Scope Contract

`issuer_scoped=true`만으로는 부족하다.

구현:

```text
BusinessMechanismScope
ArchetypeMechanismScopeContract
MechanismScopeValidator
```

`BusinessMechanismScope`:

```text
issuer_id
business_segment
product_family
technology_family
customer_or_counterparty
transaction_type
economic_mechanism
geography
effective_period
scope_confidence
```

C06 scope 예:

```text
allowed:
- Memory
- DRAM
- HBM
- AI memory
- memory ASP
- HBM shipment/revenue/capacity/qualification

not C06 direct:
- Foundry wafer contract
- logic chip contract
- unrelated mobile/display/appliance event
- adjacent substrate company sympathy
```

Generic company-level fact는 제한적으로 다음에만 갈 수 있다.

```text
information_confidence
capital allocation
```

그 경우에도 C06 관련성을 명시해야 한다.

Tesla Foundry claim 처리:

```text
- accepted in global claim ledger
- C06 current_customer_allocation_commitment = not supported
- REROUTED_TO_OTHER_MECHANISM
- C06 HBM original gap remains open
- optional different archetype backlog
```

Hard acceptance:

```text
cross_business_question_closure_count = 0
same_issuer_wrong_segment_credit_count = 0
foundry_to_hbm_allocation_count = 0
adjacent_product_to_target_capacity_count = 0
mechanism_scope_missing_count = 0
```

커밋:

```text
Phase 60 동일 회사 내 사업부·제품 메커니즘 scope 검증 구현
```

---

# 9. Phase 61 — Unified Claim Eligibility Decision

기존 boolean 혼선을 교체한다.

`ClaimEligibilityDecision`:

```text
claim_id
ledger_acceptance
source_task_satisfaction
component_scoring_eligibility
risk_scoring_eligibility
stage_event_eligibility
full_thesis_eligibility
eligibility_reasons
```

허용 상태 예:

```text
ELIGIBLE
INELIGIBLE_WRONG_MECHANISM
INELIGIBLE_HISTORICAL
INELIGIBLE_SOURCE_PROXY
INELIGIBLE_PROFILE_ONLY_FOR_COMPONENT
DISCOVERY_ONLY
RISK_ONLY
PENDING_REVIEW
```

규칙:

```text
accepted claim != component score eligible
component score eligible != original SourceTask satisfied
risk eligible != positive component eligible
```

기존 필드는 compatibility-only로 남길 수 있으나
canonical scoring은 `ClaimEligibilityDecision`만 사용한다.

Hard acceptance:

```text
eligibility_boolean_contradiction_count = 0
component_score_without_eligibility_decision_count = 0
stage_event_without_event_eligibility_count = 0
```

커밋:

```text
Phase 61 claim 장부·질문·점수·Stage eligibility 분리
```

---

# 10. Phase 62 — Question Impact Contract

각 question family는 semantic contract를 가진다.

`QuestionImpactContract`:

```text
question_family_id
archetype_id
mechanism_scope
accepted_claim_predicates
allowed_primitive_ids
allowed_component_ids
partial_support_predicates
counter_predicates
non_scoring_support_predicates
required_source_routes
required_counter_routes
terminal_absence_policy
```

C06 12개 question family 전부 정의한다.

예:

```text
current_customer_allocation_commitment
- HBM/memory customer allocation, booking, committed volume
- Foundry contract 불가
- generic customer name 불가

shipment_mass_production_generation
- HBM shipment/mass production/product generation
- actual/forward distinction

hbm_ai_memory_revenue_mix
- HBM/AI memory revenue mix
- total company revenue without attribution 불가

margin_fcf_conversion
- margin/FCF/cash conversion
- operating profit only는 partial
```

Question closure status:

```text
SUPPORTED_SCORING
PARTIALLY_SUPPORTED_SCORING
SUPPORTED_NON_SCORING
COUNTER_SUPPORTED
EVALUATED_ABSENT
SOURCE_PENDING
PROVIDER_PENDING
BUDGET_PENDING
```

단순 `SUPPORTED` 금지.

Hard acceptance:

```text
question_supported_by_wrong_mechanism_count = 0
question_supported_by_non_scoring_claim_count = 0
question_contract_missing_count = 0
```

커밋:

```text
Phase 62 질문별 scoring 의미와 성공조건 계약 구현
```

---

# 11. Phase 63 — Blind Research-Quality Benchmark

GPT Pro 수준의 조사 품질을 검증하기 위한 독립 benchmark를 만든다.

## 11.1 Two isolated lanes

### Gold Research Lane

독립 Researcher/Reviewer가 broad research를 수행한다.

```text
- official issuer filings
- issuer IR/earnings/newsroom
- customer official source
- Reuters/trusted industry source
- CompanyGuide/public report/consensus
- counter and supersession search
```

Gold lane은 material fact dossier를 만든다.

```text
gold_material_facts.jsonl
gold_source_map.jsonl
gold_question_coverage.json
```

### Production Lane

canonical pipeline이 평소대로 조사한다.

Gold dossier의 다음을 production에 보여주지 않는다.

```text
URLs
queries
facts
expected components
expected score
```

## 11.2 Post-run comparison

두 lane이 끝난 후 semantic fact-level 비교를 한다.

`MaterialFactComparison`:

```text
question_family_id
gold_fact_id
production_fact_id
semantic_match
source_quality_match
currentness_match
mechanism_scope_match
materiality
miss_reason
```

## 11.3 Repair policy

Gold lane이 찾은 material fact를 production이 놓쳤다면:

```text
- gold URL을 production input에 직접 주입하지 않는다.
- planner/query/source ranker/document selector를 수정한다.
- production lane을 clean rerun한다.
- production이 독립적으로 재발견해야 한다.
```

Acceptance:

```text
critical_material_fact_miss_count = 0
material_counter_fact_miss_count = 0
material_supersession_fact_miss_count = 0
gold_source_injected_into_production_count = 0
```

noncritical fact recall:

```text
>= 90%
```

중요:

```text
raw source count가 아니라 material semantic fact recall로 평가한다.
```

커밋:

```text
Phase 63 독립 deep-research 기준과 운영 조사 recall 검증 구현
```

---

# 12. Phase 64 — Research-Grade Acquisition & Evidence Saturation

SourceTask 실행을 “두 번 검색했으니 absence”로 끝내지 않는다.

`EvidenceSearchAdequacy`:

```text
question_family_id
official_route_attempted
issuer_ir_route_attempted
financial_revision_route_attempted
independent_source_route_attempted
counter_route_attempted
supersession_route_attempted
query_novelty_count
full_document_count
relevant_document_count
wrong_scope_document_count
provider_failures
budget_exhausted
saturation_status
```

Saturation status:

```text
EVIDENCE_FOUND
ADEQUATE_ABSENCE
SOURCE_PENDING
PROVIDER_PENDING
BUDGET_PENDING
INADEQUATE_SEARCH
```

`VERIFIED_ABSENT_AFTER_SEARCH`는 다음을 요구한다.

```text
- required routes attempted or explicitly unavailable
- provider failure 없음
- budget exhaustion 없음
- relevant positive claim 없음
- positive proposal zeroed by internal validation 없음
- supported question 없음
- gold lane material fact miss 없음
```

Source selection은 다음을 우선한다.

```text
question predicate
business mechanism scope
current date
source tier
full text availability
counter relevance
```

단순 title token match 금지.

PDF/표/IR parser:

```text
- full PDF fetch
- page/section/table anchor
- exact value/unit/period
```

Naver/Web:

```text
- LLM-generated query
- discovery only
- original full source fetch
- snippet score 금지
```

커밋:

```text
Phase 64 question별 source saturation과 research-grade 문서선택 구현
```

---

# 13. Phase 65 — Adaptive Research Repair Loop

failure별 next action을 분리한다.

```text
NO_DOCUMENT_FOUND
WRONG_BUSINESS_SEGMENT
WRONG_PRODUCT_FAMILY
STALE_ONLY
GENERIC_CONTEXT_ONLY
SNIPPET_ONLY
DOCUMENT_PARSE_FAILED
REROUTED_MECHANISM
CLAIM_EXTRACTION_FAILED
IMPACT_MAPPING_FAILED
COUNTER_ONLY
PROVIDER_FAILED
BUDGET_EXHAUSTED
```

예:

```text
WRONG_BUSINESS_SEGMENT
→ memory/HBM/DRAM segment constraint 강화

GENERIC_CONTEXT_ONLY
→ issuer actual/quantified evidence route 강화

REROUTED_MECHANISM
→ rerouted impact는 보존
→ original question query 재작성

CLAIM_EXTRACTION_FAILED
→ document section/anchor selection 수정
```

동일 query 반복 금지.

Gold comparison miss도 failure class로 넣는다.

```text
GOLD_MATERIAL_FACT_MISSED
```

커밋:

```text
Phase 65 semantic 실패 원인별 adaptive evidence 재조사 구현
```

---

# 14. Phase 66 — Evidence Impact Adjudicator v2

LLM impact adjudicator 입력에 다음을 추가한다.

```text
BusinessMechanismScope
QuestionImpactContract
ClaimEligibilityDecision
current counter claims
research-calibrated rubric
component subcriteria
```

출력:

```text
primitive impacts
component subcriterion impacts
direction
support type
strength/completeness
causal distance
mechanism scope match
unsupported aspects
counter thesis
```

High-materiality claim은 최소 two-pass.

```text
Pass A: analyst
Pass B: skeptic
```

중대한 disagreement:

```text
REVIEW_PENDING
```

으로 남긴다.

LLM이 score/Stage를 출력하면 fail.

Hard acceptance:

```text
impact_without_mechanism_scope_count = 0
impact_without_question_contract_count = 0
impact_without_unsupported_aspects_count = 0
high_materiality_single_pass_count = 0
```

커밋:

```text
Phase 66 메커니즘·질문계약 기반 LLM evidence impact 판정 강화
```

---

# 15. Phase 67 — Strict Impact Validator v2

모든 scoring-critical lookup은 total이어야 한다.

Validator output에 다음을 명시한다.

```text
support_credit_fraction
counter_effect_fraction
resolution_effect
scope_validation
fact_cluster_id
document_cluster_id
```

## 15.1 No silent zero

missing config는 rejected/zero credit가 아니라 hard error.

```text
MISSING_SUPPORT_TYPE_POLICY
MISSING_SOURCE_FAMILY_POLICY
MISSING_TEMPORAL_POLICY
MISSING_COUNTER_EFFECT_POLICY
```

## 15.2 Business mechanism validation

```text
issuer + segment + product + mechanism
```

이 모두 허용되어야 한다.

## 15.3 Fact and document clustering

`EconomicFactCluster`:

```text
normalized subject
predicate
object/value
period
business mechanism
```

같은 fact가 여러 claim/document에 반복되면:

```text
points duplicate 금지
confidence/corroboration만 개선
```

## 15.4 Claim/document budgets

```text
claim credit budget
document cluster budget
evidence family budget
component correlation cap
```

information confidence는 claim 수 합계가 아니라:

```text
best source quality
+ independent source diversity
```

형태로 aggregate한다.

Hard acceptance:

```text
positive_impact_zeroed_by_missing_cap_count = 0
counter_impact_zeroed_by_missing_cap_count = 0
cross_mechanism_impact_count = 0
same_fact_duplicate_credit_count = 0
same_document_duplicate_credit_count = 0
```

커밋:

```text
Phase 67 silent-zero 제거와 fact·document 중복점수 차단
```

---

# 16. Phase 68 — Research-Calibrated Component Subcriteria

7개 broad component 안에 research-derived subcriteria를 둔다.

`ComponentScoringModel`:

```text
component_id
max_points
aggregation_mode
subcriteria
subcriterion_max_points
required/optional role
support/counter rules
correlation groups
```

aggregation mode:

```text
SUM_DISTINCT_SUBCRITERIA
MAX_SOURCE_QUALITY
COVERAGE_WEIGHTED
NET_SUPPORT_COUNTER
CAP_BY_MISSING_BRIDGE
```

C06 예:

## EPS/FCF

```text
actual revenue/profit conversion
margin conversion
FCF/cash conversion
forward revision
```

## Earnings visibility

```text
customer allocation/commitment
capacity sold-out/pre-sold
qualification
shipment/revenue mix
medium-term revision
```

## Bottleneck/pricing

```text
capacity constraint
customer allocation
ASP/pricing actual
supply expansion counter
```

## Market mispricing

```text
consensus/revision vs market expectation
not raw price momentum only
```

## Valuation rerating

```text
valuation relative to current/forward earnings
not company event count
```

## Capital allocation

```text
capex schedule
capacity response
cash burden
```

## Information confidence

```text
source quality
directness
independent corroboration
```

각 subcriterion point budget 합계는 component max와 같아야 한다.

이 내부 배점은:

```text
historical research cases
component proxy
positive/counter relative ordering
```

으로 compile하고 문서화한다.

종목별 예외 금지.

커밋:

```text
Phase 68 C06 연구판례를 component 내부 배점과 aggregation으로 연결
```

---

# 17. Phase 69 — Counter & Contradiction Component Math

Component assessment는 support만 합산하지 않는다.

출력:

```text
support_points
counter_effect
net_points
lower_bound
upper_bound
contradiction_status
```

상태:

```text
VERIFIED_STRONG_SUPPORT
VERIFIED_PARTIAL_SUPPORT
VERIFIED_WEAK_SUPPORT
VERIFIED_ABSENT_AFTER_SEARCH
VERIFIED_COUNTER
SUPPORT_WITH_COUNTER_CAP
CONTRADICTED_OPEN
RESOLVED_COUNTER
NOT_APPLICABLE
UNKNOWN_UNINVESTIGATED
SOURCE_PENDING
PROVIDER_PENDING
BUDGET_PENDING
```

예:

```text
capacity expansion:
- capital allocation support
- bottleneck scarcity counter
```

둘 다 살아야 한다.

support+counter가 unresolved면:

```text
CONTRADICTED_OPEN
```

이며 full score finalization을 막거나
research-defined bounded cap을 적용한다.

Hard acceptance:

```text
counter_impact_ignored_count = 0
support_counter_same_component_unreconciled_count = 0
risk_open_zero_effect_count = 0
risk_resolved_still_penalized_count = 0
```

커밋:

```text
Phase 69 support·counter·resolution을 component 점수에 동시 반영
```

---

# 18. Phase 70 — Question↔Claim↔Impact↔Component Reconciliation

`SemanticClosureReconciler`를 구현한다.

각 question family마다 다음을 연결한다.

```text
question closure
supporting claim IDs
eligibility decision IDs
impact IDs
component/subcriterion IDs
credit result
component state
```

Hard rules:

```text
SUPPORTED_SCORING
→ nonzero validated impact 또는 explicit counter/cap result 필요

PARTIALLY_SUPPORTED_SCORING
→ nonzero bounded impact 필요

SUPPORTED_NON_SCORING
→ component support로 계산 금지

EVALUATED_ABSENT
→ positive claim/proposal/impact가 없어야 함
```

내부 config 오류 때문에 0점이면:

```text
SCORING_PIPELINE_ERROR
```

이지 absence가 아니다.

Critical counts:

```text
supported_question_zero_credit_count
partially_supported_question_zero_credit_count
supported_question_absent_component_count
positive_claim_absent_component_count
positive_proposal_absent_component_count
absence_with_internal_rejection_count
absence_with_provider_failure_count
absence_with_inadequate_search_count
```

전부 0이어야 한다.

커밋:

```text
Phase 70 질문·claim·impact·component semantic closure 원자검증
```

---

# 19. Phase 71 — StageCourt Full-Thesis/Event Separation

`AtomicStageCourtV2`의 다음 경로를 제거한다.

```python
company_event_score = 60.0 if claim_ids else 0.0
high_quality_company_event = bool(claim_ids)
```

Full-thesis StageCourt는 accepted claim 수로 Stage1을 열지 않는다.

별도 입력:

```text
FullThesisStageInput
EventOverlayInput
RiskOverlayInput
```

Daily event overlay는 명시적 event quality contract가 있을 때만 생성한다.

```text
accepted claim != high-quality event
```

Full thesis Stage:

```text
calibrated score
component thresholds
risk/counter state
Stage guard
```

로 결정한다.

Event watch는 별도 필드:

```text
stage_signal
event_overlay
```

Hard acceptance:

```text
claim_count_event_boost_count = 0
generic_claim_high_quality_event_count = 0
full_thesis_event_score_injection_count = 0
```

커밋:

```text
Phase 71 full-thesis Stage와 daily event overlay 완전 분리
```

---

# 20. Phase 72 — Full Score Validity v2

`full_score_valid=true`는 단순 terminal count가 아니다.

다음을 모두 요구한다.

```text
- scoring schema total
- no silent zero
- mechanism scope pass
- question-component reconciliation pass
- no unresolved contradiction
- no provider/source/budget pending
- absence search adequate
- no gold critical fact miss
- no cross-business closure
- no duplicate fact credit
```

`VERIFIED_ABSENT_AFTER_SEARCH`는 EvidenceSearchAdequacy PASS가 필요하다.

`full_score_valid`가 false여도:

```text
verified_supported_score
provisional interval
```

은 보존한다.

커밋:

```text
Phase 72 semantic 일관성을 포함한 full score validity v2 구현
```

---

# 21. Phase 73 — Readiness Gate v3

새 readiness schema:

```text
e2r_meaningful_scoring_readiness_v3
```

Final status:

```text
MEANINGFUL_E2R_SCORING_READY_V2
```

필수 critical counts:

```text
missing_scoring_policy_count = 0
silent_zero_default_count = 0
positive_impact_zeroed_by_missing_cap_count = 0
counter_impact_zeroed_by_missing_cap_count = 0
cross_business_question_closure_count = 0
supported_question_absent_component_count = 0
positive_claim_absent_component_count = 0
absence_with_inadequate_search_count = 0
counter_impact_ignored_count = 0
same_fact_duplicate_credit_count = 0
same_document_duplicate_credit_count = 0
claim_count_event_boost_count = 0
eligibility_contradiction_count = 0
critical_material_fact_miss_count = 0
```

기존 readiness v2는 deprecated.
V3 PASS 없이 기존 label alias 활성화 금지.

커밋:

```text
Phase 73 semantic 모순 없는 scoring readiness v3 구현
```

---

# 22. Phase 74 — Frozen 52f09f3 Corpus Repair Proof

새 검색을 하지 않고 기존 Samsung/Hynix corpus를 재실행한다.

입력:

```text
output/evidence_to_score/c06/2026-07-11/005930
output/evidence_to_score/c06/2026-07-11/000660
```

새 output:

```text
output/evidence_to_score_v2/frozen_52f09f3/005930
output/evidence_to_score_v2/frozen_52f09f3/000660
```

필수 invariant:

## SK하이닉스

현재 corpus에서 다음 supported facts는 내부 cap 누락 때문에 0점이 되면 안 된다.

```text
shipment / mass production
HBM revenue mix
revenue / operating profit conversion
margin / FCF conversion
capacity supply response
```

정확한 점수는 강제하지 않는다.

그러나 다음은 강제한다.

```text
PARTIAL_BRIDGE missing cap 때문에 0점 = 0건
SUPPORTED 질문이 ABSENT component = 0건
positive impact가 internal error로 소멸 = 0건
counter capacity impact가 bottleneck에서 무시 = 0건
```

## 삼성전자

```text
Tesla Foundry claim은 C06 customer allocation을 닫지 않음
HBM4 shipment는 relevant component에 bounded credit
ASP/실적 claim은 earnings/pricing/info에 bounded credit
Foundry claim은 C06 점수에서 제외 또는 다른 mechanism으로 reroute
```

Before/after delta는 claim/impact/subcriterion로 설명한다.

금지:

```text
새 문서 추가로 frozen bug를 가림
```

커밋:

```text
Phase 74 동일 corpus에서 하이닉스 0점 소거와 삼성 사업부 오매핑 수리 증명
```

---

# 23. Phase 75 — Samsung / SK Hynix Blind Deep Research Run

frozen corpus PASS 후 새 live run을 실행한다.

기준일:

```text
2026-07-11 KST
```

## 23.1 Gold lane

독립 gold dossier 생성.
Production에 비공개.

## 23.2 Production lane

canonical pipeline clean run.

## 23.3 C06 material question families

```text
customer allocation / commitment
capacity constraint / sold-out / pre-sold
qualification pass / lag / reopen
shipment / mass production
HBM revenue mix
ASP/pricing actual
revenue / operating profit conversion
margin / FCF conversion
medium-term revision
conventional memory drag
capex / supply / oversupply
customer concentration / dependency
valuation / market expectation
```

## 23.4 Source families

각 종목에서 최소한 다음 route를 실행하거나
정확한 unavailable reason을 남긴다.

```text
issuer official earnings/IR
DART official filing
issuer newsroom/product release
independent trusted source/customer source
financial/revision/valuation source
counter/supersession source
```

## 23.5 Completion

각 material component는 다음 terminal 중 하나.

```text
support
partial support
evaluated absence
counter
support with counter cap
not applicable
```

다음은 허용되지 않는다.

```text
UNKNOWN_UNINVESTIGATED
SOURCE_PENDING
PROVIDER_PENDING
BUDGET_PENDING
CONTRADICTED_OPEN
```

실제 external provider blocker가 있으면 Goal은 READY가 아니다.

## 23.6 Score/Stage

두 종목 모두:

```text
organic accepted claim > 0
validated scoring impact > 0
component subcriterion vector complete
full_score_valid=true
score_type=FULL_E2R_100
deterministic StageCourt
```

높은 점수/Green/두 종목 상대 순위는 강제하지 않는다.

커밋:

```text
Phase 75 삼성전자·하이닉스 blind deep-research와 semantic scoring 재검증
```

---

# 24. Phase 76 — Historical Replay & Generalization

## C06 source-backed replay

필수:

```text
SK Hynix sold-out/customer capacity positive
SK Hynix HBM revenue mix positive
Samsung qualification lag guard
Samsung reopen/customer dependency
package/substrate profile guard
```

검증:

```text
- sold-out/revenue mix가 relevant components에 nonzero
- qualification lag는 hard 4C 아님
- profile-only는 customer allocation/revenue conversion을 열지 않음
- future leakage 0
```

## Generalization

필수:

```text
C08 named customer/order positive
C08 profile-only guard
C15 issuer pass-through positive
C15 raw commodity headline guard
wrong subject
same issuer wrong segment
old risk resolved
support+counter same component
```

All 36 archetype rubric totality audit도 실행한다.

커밋:

```text
Phase 76 C06 역사판례와 전 아키타입 scoring schema 일반화 검증
```

---

# 25. Phase 77 — Known-Bad Regression Suite

최소 다음 35개를 known-bad로 만든다.

```text
1. PARTIAL_BRIDGE cap 누락이 조용히 0점
2. RISK_OPEN cap 누락이 조용히 0점
3. RISK_RESOLVED cap 누락이 조용히 0점
4. source family cap 누락이 조용히 0점
5. temporal cap 누락이 조용히 0점
6. SUPPORTED 질문이 zero-credit
7. PARTIALLY_SUPPORTED 질문이 zero-credit
8. SUPPORTED 질문이 VERIFIED_ABSENT
9. positive claim이 VERIFIED_ABSENT
10. internal rejection이 absence로 위장
11. provider failure가 absence
12. budget exhaustion이 absence
13. Foundry Tesla claim이 HBM allocation 지원
14. same issuer wrong segment score
15. adjacent substrate가 target HBM capacity
16. accepted claim eligibility boolean 모순
17. component score without eligibility decision
18. support+counter인데 counter 무시
19. capacity expansion counter가 bottleneck에 0
20. risk resolved가 계속 감점
21. 같은 fact 여러 claim 중복 credit
22. 같은 document 여러 claim 정보신뢰도 중복
23. repost 여러 문서 중복 credit
24. claim 수만으로 company_event_score 60
25. any claim이 high_quality_company_event
26. full-thesis Stage에 daily event overlay 주입
27. gold URL production seed 주입
28. gold fact production prompt 누수
29. critical gold material fact miss인데 PASS
30. frozen corpus bug를 새 문서로 가림
31. source proxy score
32. historical outcome prompt leak
33. Stage/score/impact/component trace mismatch
34. full_score_valid인데 semantic reconciliation fail
35. report-only readiness 승격
```

모두 expected failure를 내야 한다.

커밋:

```text
Phase 77 semantic scoring known-bad 35종 회귀 고정
```

---

# 26. Phase 78 — Self-Repair Until True Pass

최대 12 code-repair iteration.

각 iteration:

```text
iteration
target
failure class
root cause file/function/config
before metrics
patch commit
focused tests
frozen corpus rerun
live production rerun
gold comparison
after metrics
resolved/unresolved
```

Failure classes:

```text
SCORING_SCHEMA_INCOMPLETE
SILENT_ZERO_CAP
WRONG_MECHANISM_SCOPE
ELIGIBILITY_CONTRADICTION
QUESTION_COMPONENT_INCONSISTENCY
POSITIVE_IMPACT_ERASED
COUNTER_EFFECT_IGNORED
FACT_DUPLICATE_CREDIT
DOCUMENT_DUPLICATE_CREDIT
EVENT_STAGE_INJECTION
EVIDENCE_SEARCH_INADEQUATE
GOLD_MATERIAL_FACT_MISSED
FULL_SCORE_INVALID
STAGE_TRACE_MISMATCH
EXTERNAL_PROVIDER_BLOCKER
```

동일 failure가 남으면 계속 수정한다.

금지:

```text
threshold 완화
synthetic claim
expected score 하드코딩
gold source injection
fixture as live
report-only repair
```

커밋:

```text
Phase 78 frozen·live·gold 비교 기반 self-repair 완결
```

---

# 27. Phase 79 — Independent Reviewer Gate

Reviewer A — Scoring Schema Totality

```text
enum/cap completeness
silent zero absence
```

Reviewer B — Mechanism Scope & Eligibility

```text
segment/product/economic mechanism
eligibility planes
```

Reviewer C — Research Acquisition

```text
gold recall
source family coverage
counter/supersession
```

Reviewer D — Claim Impact Semantics

```text
many-to-many
support/counter
fact dedupe
```

Reviewer E — Question/Component Reconciliation

```text
SUPPORTED vs ABSENT
search adequacy
```

Reviewer F — Score & Stage

```text
subcriterion vector
full validity
event/full-thesis separation
```

Reviewer G — Samsung/Hynix C06

```text
HBM semantics
Foundry exclusion
qualification/capacity/revenue/margin/counter
```

Reviewer H — Generalization

```text
C08/C15/wrong-subject/old-risk
all archetype schema totality
```

각 reviewer는 report generator counter를 공유하지 않고
leaf artifact를 직접 읽는다.

critical 1개면 FAIL.

커밋:

```text
Phase 79 semantic evidence acquisition과 scoring 독립 reviewer 검증
```

---

# 28. 필수 Tests

예:

```text
tests/test_scoring_schema_totality.py
tests/test_no_silent_zero_cap.py
tests/test_partial_bridge_nonzero_policy.py
tests/test_risk_direction_policy.py
tests/test_business_mechanism_scope.py
tests/test_foundry_not_hbm_allocation.py
tests/test_claim_eligibility_decision.py
tests/test_question_impact_contract.py
tests/test_supported_question_requires_credit.py
tests/test_absence_requires_adequate_search.py
tests/test_gold_research_blindness.py
tests/test_gold_material_fact_recall.py
tests/test_fact_cluster_dedupe.py
tests/test_document_cluster_credit_cap.py
tests/test_counter_component_math.py
tests/test_component_subcriterion_scoring.py
tests/test_full_thesis_event_separation.py
tests/test_frozen_52f09f3_repair.py
tests/test_samsung_hynix_semantic_scoring_v2.py
tests/test_all_archetype_rubric_totality.py
tests/test_semantic_scoring_known_bad.py
```

전체:

```bash
PYTHONPATH=src python -m unittest discover -s tests -v
```

Goal tests skip/xfail 0.

---

# 29. 필수 Output Artifacts

```text
docs/operational/e2r_semantic_scoring_v2_forensic_baseline.md
docs/operational/e2r_scoring_schema_totality_audit.json
docs/operational/e2r_business_mechanism_scope_audit.json
docs/operational/e2r_claim_eligibility_audit.json
docs/operational/e2r_question_impact_contract_audit.json
docs/operational/e2r_research_quality_gold_audit.json
docs/operational/e2r_evidence_search_adequacy_audit.json
docs/operational/e2r_impact_validator_v2_audit.json
docs/operational/e2r_fact_document_dedupe_audit.json
docs/operational/e2r_counter_component_audit.json
docs/operational/e2r_question_component_reconciliation_audit.json
docs/operational/e2r_full_thesis_event_separation_audit.json
docs/operational/e2r_frozen_52f09f3_repair_audit.json
docs/operational/e2r_samsung_semantic_scoring_v2.md
docs/operational/e2r_sk_hynix_semantic_scoring_v2.md
docs/operational/e2r_c06_semantic_cutover_v2.md
docs/operational/e2r_semantic_scoring_known_bad_audit.json
docs/operational/e2r_semantic_scoring_self_repair_summary.md
docs/operational/e2r_semantic_scoring_reviewer_gate.json
docs/operational/e2r_meaningful_scoring_readiness_v3.md
```

각 dossier leaf:

```text
gold_material_facts.jsonl
production_material_facts.jsonl
material_fact_comparison.jsonl
question_source_tasks.jsonl
evidence_search_adequacy.jsonl
evidence_documents.jsonl
accepted_current_claims.jsonl
claim_eligibility_decisions.jsonl
claim_impacts_proposed.jsonl
claim_impacts_validated.jsonl
economic_fact_clusters.jsonl
component_subcriteria.jsonl
component_assessments.jsonl
component_score_vector.json
semantic_closure_trace.jsonl
atomic_stage_decision.json
stagecourt_trace.json
```

---

# 30. Final Hard Gates

`MEANINGFUL_E2R_SCORING_READY_V2`는 다음을 모두 요구한다.

## Schema

```text
missing scoring policy = 0
silent zero default = 0
all 36 archetypes schema total
```

## Acquisition

```text
Samsung critical gold fact miss = 0
Hynix critical gold fact miss = 0
counter fact miss = 0
gold leakage/injection = 0
```

## Mechanism

```text
cross-business closure = 0
Foundry→HBM allocation = 0
same issuer wrong segment credit = 0
```

## Impact

```text
positive impact zeroed by missing cap = 0
counter impact zeroed by missing cap = 0
counter ignored = 0
fact/document duplicate credit = 0
```

## Reconciliation

```text
SUPPORTED question zero credit = 0
SUPPORTED question ABSENT component = 0
positive claim ABSENT component = 0
inadequate search absence = 0
```

## Frozen corpus

```text
SK Hynix current supported facts have semantically valid nonzero component effects
Samsung Foundry claim excluded from C06 allocation
same corpus semantic inconsistencies = 0
```

정확한 총점은 강제하지 않는다.

## Live canaries

```text
Samsung full_score_valid=true
Hynix full_score_valid=true
both FULL_E2R_100
both deterministic StageCourt
no pending/nonterminal/contradicted-open
```

## Stage

```text
claim-count event boost = 0
full-thesis/daily event separation PASS
hard break current direct OPEN only
```

## Replay/generalization

```text
C06 historical replay PASS
C08/C15 guards PASS
future leakage = 0
source proxy score = 0
```

## Verification

```text
full unittest PASS
known-bad PASS
Reviewer A~H PASS
critical_count_sum = 0
blockers = []
same input replay variance = 0
worktree clean
HEAD == origin/main
```

---

# 31. 절대 완료가 아닌 상태

다음은 완료가 아니다.

```text
- 새 문서를 많이 모았지만 supported question이 여전히 0점
- 하이닉스 earnings_visibility/bottleneck이 cap 누락으로 0
- 삼성 Foundry 계약이 C06 HBM allocation을 닫음
- counter impact가 audit에만 있고 점수에 반영 안 됨
- same document claim 수로 information confidence 만점
- full_score_valid지만 semantic closure audit FAIL
- gold lane은 좋은 자료를 찾았지만 production은 못 찾음
- gold URL을 production seed로 넣어 통과
- Stage1이 claim 수로 자동 발생
- 삼성 또는 하이닉스 한 종목만 PASS
- report 문구만 READY
```

---

# 32. Final Response Format

완료 후 다음만 보고한다.

1. Final status
2. Phase commits / push / worktree
3. Full tests / known-bad
4. Root causes fixed
5. Scoring schema totality
6. Business mechanism scope
7. Claim eligibility
8. Gold-vs-production evidence recall
9. Search adequacy
10. Support/counter impact audit
11. Fact/document dedupe
12. Question-component reconciliation
13. Frozen 52f09f3 before/after
14. Samsung source/claim/impact/subcriteria/score/Stage
15. SK Hynix source/claim/impact/subcriteria/score/Stage
16. Historical/generalization replay
17. Self-repair iterations
18. Reviewer A~H
19. Remaining blockers
20. Exact verdict

---

# 33. 마지막 명령

이번 Goal의 성공은:

```text
증거를 많이 찾았다
```

도 아니고:

```text
가짜 점수를 막았다
```

도 아니다.

성공은 다음이다.

```text
운영 두뇌가 독립 deep research 수준으로 material evidence를 찾고,
찾은 claim의 business mechanism을 정확히 이해하고,
support/counter/partial 의미를 조용히 0점으로 죽이지 않고,
같은 fact를 중복 점수화하지 않으며,
question closure와 component state가 서로 일치하고,
연구 기반 subcriterion 배점으로 full score와 Stage를 재현하는 것
```

먼저 동일 52f09f3 corpus에서 현재 semantic bug를 수리하라.

그 다음 blind gold lane과 production lane을 분리해
운영 pipeline이 중요한 증거를 독립적으로 다시 찾는지 검증하라.

삼성전자와 SK하이닉스가 둘 다:

```text
research-grade source dossier
→ mechanism-scoped organic claim
→ strict-total validated impact
→ reconciled component subcriteria
→ FULL_E2R_100
→ deterministic StageCourt
```

까지 닫히고,
모든 semantic critical count가 0일 때만:

```text
MEANINGFUL_E2R_SCORING_READY_V2
```

를 선언하라.
