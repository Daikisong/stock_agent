# E2R RESEARCH-CALIBRATED SEMANTIC EVIDENCE-TO-SCORE BRIDGE MASTER GOAL v1
## Samsung Electronics / SK Hynix Canonical Full-Thesis Cutover
## Phase 41+ — Claim Meaning → Many-to-Many Impact → Calibrated Component Score → StageCourt

너는 `Daikisong/stock_agent` 레포의 수석 아키텍트이자 구현 에이전트다.

이번 Goal은 live API, Census, Evidence OS에 방어 게이트를 하나 더 추가하는 작업이 아니다.

이번 Goal의 목적은 지금까지 구축한 다음 자산을 실제 점수와 Stage로 연결하는 것이다.

```text
historical research corpus
Research Brain
Evidence Recipe
live KRX universe
official/Naver/Web source acquisition
EvidenceDocument / Anchor
current accepted claim
claim provenance
deterministic scorer
StageCourt
```

현재 파이프라인은 시장을 보고 문서를 가져오며, 가짜 claim과 잘못된 대상회사 귀속을 상당히 잘 막는다.
그러나 검증된 claim의 경제적 의미를 과거 연구에서 만든 점수 component로 전달하는 중앙 bridge가 잘못되어 있다.

현재 코드에서 반드시 검증하고 수리해야 할 대표 결함은 다음이다.

```text
1. `CurrentAtomicDecisionBuilder`가 production score rule을
   canonical archetype weight profile에서 읽지 않고,
   이번 실행에서 생성된 SourceTask primitive 수로 100점을 균등 분배한다.

2. 현재 SourceTask primitive를 전부
   material=True / green_required=True로 만들어,
   하나라도 미확인일 때 이미 확인된 component score까지 `NO_SCORE`로 지운다.

3. `CurrentClaimCompiler`는 원래 질문과 같은 primitive에 매핑된 claim만
   DIRECT_TASK_SATISFIED로 인정한다.

4. 다른 유효 primitive를 발견한 rerouted claim은
   원래 gap을 닫지 않는 것까지는 맞지만,
   그 claim이 실제로 지원하는 다른 primitive/component의 점수 효용까지 버린다.

5. 한 claim이 여러 primitive/component를 지원할 수 있음에도,
   atomic bridge는 한 claim이 여러 direct primitive를 닫으면 오류를 낸다.

6. accepted claim row의 mapping lineage가 단일 mapping처럼 축소될 수 있다.

7. 현재 scorer는 claim의 경제적 강도, 완성도, causal distance,
   actual-vs-forward, positive-vs-counter, source family diversity를 충분히 반영하지 않는다.

8. `FULL_THESIS`에서 모든 positive primitive가 PRESENT여야만 final score를 허용하는 구조라,
   `충분히 조사했으나 증거가 없음`과 `아직 조사하지 않음`을 구분하지 않는다.

9. acceptance probe 하나가 `NO_SCORE / Stage0`이어도
   accepted claim과 contribution object가 있다는 이유로
   의미 있는 runtime READY가 될 수 있다.

10. 삼성전자·SK하이닉스 targeted live smoke가 실제 문서를 다수 가져와도,
    organic accepted claim과 calibrated component score로 이어지지 않는다.
```

이번 Goal은 이 중앙 bridge를 재건한다.

---

# 0. 최종 철학

최종 구조는 다음이어야 한다.

```text
full source document
→ contract-blind RawAssertion
→ current accepted claim
→ LLM EvidenceImpactAdjudicator
→ many-to-many ClaimImpactLedger
→ deterministic ImpactValidator / cap / dedupe
→ ComponentAssessment
→ calibrated archetype weight profile
→ verified component score vector
→ provisional score interval
→ full-score validity
→ deterministic total score
→ StageCourt
```

역할은 명확히 분리한다.

## LLM Research Brain / Evidence Impact Brain

LLM은 다음을 판단한다.

```text
- 이 claim의 경제적 의미는 무엇인가
- 어느 primitive들을 직접 또는 부분적으로 지원하는가
- 어느 score component에 영향을 주는가
- positive / counter / neutral / resolved 중 무엇인가
- actual result / forward visibility / profile / discovery 중 무엇인가
- support strength와 completeness는 어느 band인가
- causal distance가 가까운가 먼가
- 이 claim이 무엇을 지원하지 못하는가
- 어떤 counter claim과 함께 봐야 하는가
```

LLM은 최종 총점이나 최종 Stage를 출력하지 않는다.

## Deterministic code

코드는 다음을 검증한다.

```text
- source URL / official locator
- exact quote / content hash
- target directness
- current temporal validity
- lifecycle / supersession
- allowed archetype / primitive / component mapping
- evidence strength band의 허용 cap
- source tier / freshness / duplication / correlation cap
- contradiction / counter evidence
- claim credit budget
- calibrated weight profile
- final total score
- StageCourt
```

---

# 1. 이번 작업의 명시적 목표

이번 Goal은 두 단계 목표를 가진다.

## Target A — 핵심 scoring bridge 재건

다음을 production canonical path에서 달성한다.

```text
accepted current claim
→ one-or-more validated primitive impacts
→ one-or-more bounded component impacts
→ research-calibrated component score
```

## Target B — 삼성전자·SK하이닉스 canonical proof

다음 두 종목을 **실제 운영과 동일한 canonical live path**로 평가한다.

```text
005930 삼성전자
000660 SK하이닉스
```

이 두 종목은 production code의 예외가 아니다.
단지 전체 bridge의 mandatory acceptance canary다.

금지:

```text
if symbol == "005930"
if symbol == "000660"
삼성전자 전용 점수
하이닉스 전용 점수
미리 정한 expected total score
미리 정한 expected Stage
```

허용:

```text
targeted validation CLI에서 두 ticker를 명시
C06 Evidence Recipe를 적용
실제 current source를 조사
실제 증거에 따라 서로 다른 점수와 Stage 산출
```

최종 합격은 두 종목에 높은 점수나 Green을 강제하는 것이 아니다.

최종 합격은:

```text
- 실제 organic source-backed claim이 존재하고
- 연구에서 정한 component rubric으로 점수가 들어가며
- 미확인 항목과 확인된 항목이 구분되고
- full thesis 평가가 완료되어
- deterministic total score와 Stage가 설명 가능하게 나오는 것
```

이다.

---

# 2. 현재 READY 라벨 재분류

현재 `MEANINGFUL_E2R_RUNTIME_READY`는 이 Goal 완료 전까지 다음으로 재분류한다.

```text
LIVE_MATERIALIZATION_AND_FAIL_CLOSED_PIPELINE_PASS
ORGANIC_EVIDENCE_TO_SCORE_BRIDGE_NOT_READY
MEANINGFUL_E2R_SCORING_NOT_READY
```

생성:

```text
docs/operational/e2r_evidence_to_score_current_state_reclassification.md
```

반드시 기록:

```text
- canonical live materialization은 실제 작동한다.
- source/claim provenance guard는 작동한다.
- organic base run의 accepted claim / valid score 수치
- acceptance probe promotion 여부
- `_balanced_points()` 사용 여부
- direct-only claim adaptation 여부
- rerouted claim score loss 여부
- full score validity의 all-or-nothing 구조
- 삼성/하이닉스 organic smoke 결과
```

이 Goal이 끝나기 전에는 report-only commit으로 READY 라벨을 복구하지 않는다.

---

# 3. 절대 금지사항

1. scoring weight와 Stage threshold를 바꾸어 통과하지 마라.
2. 종목별 예외를 production code에 넣지 마라.
3. 삼성전자·하이닉스에 목표 점수/Stage를 미리 정하지 마라.
4. `_balanced_points()`를 production scoring에서 유지하지 마라.
5. SourceTask 개수로 100점을 나누지 마라.
6. 모든 primitive에 일괄 `material=True`, `green_required=True`를 주지 마라.
7. DIRECT_TASK_SATISFIED claim만 전역 점수에 쓰지 마라.
8. rerouted claim의 유효한 점수 효용을 폐기하지 마라.
9. rerouted claim으로 원래 질문이 해결됐다고 표시하지 마라.
10. 한 claim을 하나의 primitive에만 강제하지 마라.
11. 한 claim으로 아무 관련 없는 component를 중복 채점하지 마라.
12. LLM이 최종 총점/Stage를 직접 출력하지 마라.
13. deterministic keyword rule로 claim strength를 결정하지 마라.
14. 모든 미확인 항목을 `MISSING` 하나로 뭉개지 마라.
15. `조사했으나 없음`과 `조사하지 않음`을 같은 상태로 두지 마라.
16. material gap 하나 때문에 확인된 component 점수를 삭제하지 마라.
17. `NO_SCORE` decision만 존재하는 상태에서 meaningful scoring READY를 선언하지 마라.
18. acceptance probe claim을 organic live claim으로 계산하지 마라.
19. fixture/snapshot/replay claim을 current organic claim으로 계산하지 마라.
20. source_proxy_only/evidence_url_pending historical row를 current score에 쓰지 마라.
21. historical MFE/MAE/outcome을 current adjudicator prompt에 노출하지 마라.
22. Naver snippet을 score claim으로 쓰지 마라.
23. provider failure를 evidence absent로 확정하지 마라.
24. old risk를 current OPEN 확인 없이 감점하지 마라.
25. same query/source를 이유 없이 반복하지 마라.
26. 실패하면 threshold를 낮추거나 known-bad test를 삭제하지 마라.
27. report 수치만 맞추고 leaf artifact 연결을 생략하지 마라.
28. `docs/core/goal*.md`의 사용자 변경을 임의로 되돌리지 마라.

---

# 4. 실행 프로토콜

## 4.1 Phase별 한글 커밋

각 Phase는 focused test 통과 후 한글 커밋과 push를 남긴다.

## 4.2 Fail → Root Cause → Patch → Same Run

실패 시:

```text
failure cluster
→ exact file/function
→ patch
→ focused tests
→ same frozen replay
→ same live canary command
→ before/after conversion funnel
```

를 반복한다.

다음은 self-repair가 아니다.

```text
같은 명령 재실행
report에 blocker 쓰기
acceptance threshold 완화
probe claim 추가
```

## 4.3 External blocker

외부 blocker는 다음을 모두 증명한 경우에만 허용한다.

```text
- internal code path complete
- actual provider call attempted
- provider/env/request/error leaf exists
- alternative official route attempted
- affected primitive/component exact
```

---

# 5. Phase 41 — Read-Only Scoring Bridge Forensic

먼저 코드를 수정하지 말고 전 경로를 추적한다.

대상:

```text
src/e2r/research_brain/runtime/live_materialization/current_claim_compiler.py
src/e2r/research_brain/runtime/live_materialization/current_atomic_decision.py
src/e2r/research_brain/runtime/atomic_score_stage.py
src/e2r/research_brain/runtime/live_materialization/live_acceptance.py
src/e2r/research_brain/runtime/live_materialization/final_readiness.py
src/e2r/research_brain/runtime/live_materialization/live_operational_packager.py
src/e2r/scoring.py
src/e2r/features.py
src/e2r/staging.py
configs/e2r_archetype_weight_profile*.json
configs/e2r_archetype_evidence_contracts_v12.json
src/e2r/research_brain/recipes/**
src/e2r/research_brain/compiler/**
src/e2r/evidence/**
tests/**
```

생성:

```text
docs/operational/e2r_evidence_to_score_forensic_baseline.md
docs/operational/e2r_evidence_to_score_call_graph_before.json
docs/operational/e2r_current_score_contract_inventory.json
docs/operational/e2r_claim_mapping_loss_inventory.json
```

반드시 답할 질문:

```text
1. 어떤 profile이 현재 production score의 source of truth인가?
2. current live path는 왜 그 profile을 사용하지 않는가?
3. `_balanced_points()`가 어디서 production reachable한가?
4. 왜 모든 task primitive가 material/green_required인가?
5. accepted claim의 mapping IDs가 어디서 손실되는가?
6. rerouted claim이 어느 단계에서 score candidate에서 사라지는가?
7. claim 한 개의 multiple mappings가 어디서 금지되는가?
8. `current_score_eligible=False`가 왜/어디서 설정되는가?
9. organic current claim과 acceptance probe claim이 어떻게 섞이는가?
10. final readiness가 왜 score_valid=true/FULL_E2R_100 없이 통과 가능한가?
11. historical component_proxy / score simulation을 runtime rubric으로 어떤 코드가 사용하고 있는가?
12. current material gap state가 왜 all-or-nothing NO_SCORE를 만드는가?
```

Phase 41 acceptance:

```text
- root cause file/function 목록
- organic/probe path 분리
- current vs calibrated score contract diff
- claim mapping loss count
- balanced point production reachability
```

커밋:

```text
Phase 41 live 증거와 연구 배점 연결 단절 감사
```

---

# 6. Phase 42 — Legacy Scoring Path Lockout

production canonical path에서 다음을 제거한다.

```text
- SourceTask count 기반 100점 균등분배
- 모든 primitive material/green_required 일괄 지정
- direct task closure-only score claim adaptation
- claim one-primitive restriction
```

`_balanced_points()`는 test-only 또는 삭제한다.

Static critical counts:

```text
production_balanced_points_usage_count
production_all_material_true_rule_count
production_all_green_required_true_rule_count
production_direct_only_score_claim_count
production_claim_single_primitive_enforcement_count
```

모두 0이어야 한다.

Legacy adapter가 필요하면:

```text
- explicit deprecated/test-only
- final readiness 생성 금지
- canonical CLI production unreachable
```

커밋:

```text
Phase 42 임시 균등배점과 direct-only live scorer 차단
```

---

# 7. Phase 43 — Canonical Archetype Scoring Contract Loader

구현 예:

```text
src/e2r/research_brain/runtime/scoring_contracts/
    loader.py
    schemas.py
    validator.py
    archetype_component_catalog.py
```

`ArchetypeScoringContract`:

```text
archetype_id
profile_id
profile_version
component_weights
component_max_points
primitive_to_component_allowed_edges
primitive_materiality
primitive_green_requirements
component_required_evidence_roles
component_caps
source_tier_caps
freshness_caps
correlation_groups
counter_effect_rules
stage_config
config_hash
```

규칙:

1. 현재 canonical archetype weight profile을 source of truth로 로드한다.
2. component weights 합계는 100이어야 한다.
3. SourceTask primitive는 scoring universe를 만들지 않는다.
4. SourceTask는 조사 질문이고 score contract는 고정된 연구 결과다.
5. 아키타입이 불확실하면 top-k contract를 평가하되 최종 selected archetype provenance를 남긴다.
6. profile fallback 사용 시 explicit fallback status와 cap을 남긴다.
7. 특정 종목에 맞춘 profile 금지.

C06 canary:

```text
C06_HBM_MEMORY_CUSTOMER_CAPACITY scoring contract를 실제 로드하고,
점수 component와 max point를 report한다.
```

출력:

```text
docs/operational/e2r_canonical_scoring_contract_audit.json
```

Hard acceptance:

```text
component_weight_sum != 100 count = 0
missing_component_contract_count = 0
source_task_defined_score_weight_count = 0
unknown_profile_silent_fallback_count = 0
```

커밋:

```text
Phase 43 연구 보정 아키타입 점수계약을 live scorer에 연결
```

---

# 8. Phase 44 — Research-Calibrated Evidence Impact Rubric Compiler

과거 연구를 최종 current evidence가 아니라 **점수 의미 판례**로 컴파일한다.

구현 예:

```text
src/e2r/research_brain/compiler/evidence_impact_rubric_compiler.py
src/e2r/research_brain/scoring/evidence_impact_rubric.py
```

`EvidenceImpactRubric`:

```text
rubric_id
archetype_id
primitive_id
allowed_component_ids
economic_mechanism
positive predicates
partial predicates
counter predicates
unsupported predicates
strength bands
completeness bands
causal distance caps
source family caps
actual vs forward rules
evidence family diversity rules
double-count/correlation rules
positive historical case refs
counterexample refs
source-backed examples
source-proxy planning-only examples
```

Research source rules:

```text
URL-backed rows:
rubric/replay examples로 사용 가능

source_proxy_only / evidence_url_pending:
guard/질문/cap 설계에 사용
current score evidence로 사용 불가

price path / MFE/MAE:
rubric calibration evaluator에서만 사용
current impact adjudicator prompt에 숨김
```

C06 rubric은 최소 다음을 구분한다.

```text
- HBM keyword/product profile
- customer allocation
- sold-out/pre-sold capacity
- qualification pass
- qualification lag
- shipment/mass production
- HBM revenue mix
- ASP/pricing actual
- operating profit actual
- medium-term revision
- margin/FCF conversion
- conventional memory drag
- package/substrate sympathy
```

예시 의미:

```text
공식 실적자료에서 ASP 상승과 사상 최대 매출/영업이익:
- pricing/bottleneck component에 직접 또는 강한 부분 지원
- actual earnings conversion component에 부분 지원
- information confidence에 강한 지원
- customer allocation / pre-sold capacity / forward revision은 지원하지 않음

HBM sold out / allocated capacity:
- customer/capacity bottleneck
- revenue visibility
- 일부 forward earnings visibility
- FCF는 별도 증거 필요

qualification lag:
- execution counter/risk
- hard 4C 아님
- reopening/optimization path가 있으면 watch/4B
```

Hard acceptance:

```text
C06 rubric has positive/partial/counter/unsupported examples
rubric current evidence rows contain no future outcome
source_proxy row current_score_allowed = 0
generic "verify primitive" rubric = 0
```

커밋:

```text
Phase 44 과거 연구를 evidence impact 점수판례로 컴파일
```

---

# 9. Phase 45 — Many-to-Many Claim Impact Ledger

구현:

```text
ClaimImpactProposal
ValidatedClaimImpact
ClaimImpactLedger
```

`ClaimImpactProposal`:

```text
impact_id
claim_id
mapping_id
target_id
archetype_id
primitive_id
component_id
direction: SUPPORT|COUNTER|NEUTRAL|RESOLUTION
support_type:
  DIRECT_ACTUAL
  DIRECT_FORWARD
  PARTIAL_BRIDGE
  PROFILE_ONLY
  DISCOVERY_ONLY
  RISK_OPEN
  RISK_RESOLVED
strength_band:
  NONE
  WEAK
  MODERATE
  STRONG
  VERY_STRONG
completeness_band:
  MENTION
  PARTIAL
  SUBSTANTIAL
  COMPLETE_FOR_PRIMITIVE
causal_distance:
  DIRECT
  ONE_HOP
  TWO_HOP
  INDUSTRY_ONLY
temporal_scope
source_family
evidence_family_id
confidence
rationale
unsupported_aspects
counter_claim_ids
```

핵심 규칙:

1. 한 claim은 여러 primitive/component impact를 가질 수 있다.
2. 각 impact는 별도 mapping/impact ID를 가진다.
3. 원래 SourceTask satisfaction과 전역 score impact를 분리한다.
4. rerouted claim:
   - original SourceTask gap은 OPEN
   - mapped component impact는 살아 있음
5. 한 claim의 mapping IDs를 덮어쓰지 않는다.
6. claim-level unique credit budget와 correlation cap을 둔다.
7. 동일 경제효과를 여러 component에 무한 복제하지 않는다.
8. information confidence와 economic component를 분리하되 중복 cap을 적용한다.

Hard acceptance:

```text
valid_rerouted_claim_lost_score_impact_count = 0
one_claim_multiple_impact_rejected_count = 0
mapping_lineage_loss_count = 0
duplicate_economic_credit_count = 0
original_gap_closed_by_rerouted_count = 0
```

커밋:

```text
Phase 45 claim 다중 의미와 SourceTask 만족도를 분리
```

---

# 10. Phase 46 — LLM EvidenceImpactAdjudicator

LLM은 단순 parser/primitive classifier에서 벗어나,
검증된 claim의 경제적 점수 의미를 구조화한다.

구현 예:

```text
src/e2r/research_brain/scoring/evidence_impact_adjudicator.py
```

입력:

```text
target identity
as_of_date
selected/top-k archetype
accepted current claim
exact quote
document metadata
current claim ledger
counter claims
EvidenceImpactRubric
allowed component catalog
```

LLM에게 숨길 것:

```text
final total score
current Stage
expected Stage
historical MFE/MAE
historical future outcome
target component point answer
```

LLM 출력:

```text
one-or-more ClaimImpactProposal
explicit unsupported aspects
counter thesis
confidence
reasoning summary
```

LLM이 숫자 total score를 출력하면 validation fail.

Strength/completeness는 band로 제안하고,
deterministic code가 band→fraction을 변환한다.

고중요 impact는 2-pass로 검증한다.

```text
Pass A: impact proposal
Pass B: skeptic/counter adjudication
```

충돌 시:

```text
REVIEW_PENDING
```

으로 남기고 임의 점수 금지.

Hard acceptance:

```text
LLM final score key count = 0
LLM Stage key count = 0
future outcome leakage = 0
impact without rationale = 0
unsupported aspect omission = 0
```

커밋:

```text
Phase 46 LLM이 검증 claim의 경제적 점수영향을 판정
```

---

# 11. Phase 47 — Deterministic Impact Validator & Credit Caps

구현:

```text
ImpactValidator
CreditCapEngine
CorrelationDeduper
```

검증:

```text
- claim provenance
- allowed primitive↔component edge
- rubric predicate match
- source tier
- freshness/current lifecycle
- target directness
- causal distance
- actual vs forward
- evidence family independence
- duplicate/correlation
- counter evidence
- maximum claim credit budget
```

Band→credit fraction은 config/rubric에서 deterministic하게 변환한다.

예:

```text
WEAK/PARTIAL
MODERATE/PARTIAL
STRONG/SUBSTANTIAL
VERY_STRONG/COMPLETE
```

정확한 fraction은 기존 연구/캘리브레이션을 분석해 정한다.
이번 Goal에서 임의로 새 weight를 발명하지 않는다.

한 claim이 여러 component를 지원할 경우:

```text
- 각 impact에 cap
- claim total credit cap
- correlation group cap
```

을 적용한다.

Hard acceptance:

```text
unvalidated_impact_to_score_count = 0
rubric_edge_violation_count = 0
source_cap_violation_count = 0
claim_credit_budget_violation_count = 0
correlated_double_count_count = 0
```

커밋:

```text
Phase 47 evidence impact 검증과 중복 점수 cap 구현
```

---

# 12. Phase 48 — Component Assessment State Machine

현재 `SATISFIED/MISSING` 2상태를 폐기한다.

새 상태:

```text
VERIFIED_STRONG_SUPPORT
VERIFIED_PARTIAL_SUPPORT
VERIFIED_WEAK_SUPPORT
VERIFIED_ABSENT_AFTER_SEARCH
VERIFIED_COUNTER
CONTRADICTED_OPEN
HISTORICAL_ONLY
NOT_APPLICABLE
UNKNOWN_UNINVESTIGATED
SOURCE_PENDING
PROVIDER_PENDING
BUDGET_PENDING
```

핵심 구분:

```text
VERIFIED_ABSENT_AFTER_SEARCH:
충분히 조사했지만 positive evidence가 없음
→ 0점 또는 counter/cap
→ full thesis 평가를 완료할 수 있음

UNKNOWN_UNINVESTIGATED:
아직 충분히 조사하지 않음
→ provisional only
→ full score finalization 차단

PROVIDER/SOURCE/BUDGET_PENDING:
외부/운영 미완료
→ finalization 차단
```

`ComponentAssessment`:

```text
component_id
max_points
status
support_impact_ids
counter_impact_ids
verified_points
lower_bound_points
upper_bound_points
missing_questions
search_exhaustion_proof
confidence
```

모든 positive primitive가 PRESENT여야 full score가 되는 구조를 제거한다.

full thesis 완료의 의미는:

```text
모든 material component가
support / partial / absent / counter / not-applicable 중 하나로
충분히 평가됨
```

이다.

Hard acceptance:

```text
evaluated_absent_blocks_full_score_count = 0
unknown_uninvestigated_allows_full_score_count = 0
provider_pending_allows_full_score_count = 0
supported_component_erased_by_other_gap_count = 0
```

커밋:

```text
Phase 48 미확인·부재·부분증거를 구분하는 component 상태기계 구현
```

---

# 13. Phase 49 — Research-Calibrated Component Score Engine

구현:

```text
ResearchCalibratedComponentScorer
```

입력:

```text
ArchetypeScoringContract
ValidatedClaimImpacts
ComponentAssessments
counter/risk state
```

출력:

```text
component_score_vector
verified_supported_score
provisional_score_lower
provisional_score_upper
full_e2r_score
full_score_valid
score_type
score_confidence
```

규칙:

1. canonical profile weights를 사용한다.
2. component point는 validated impact와 deterministic cap으로 계산한다.
3. 확인된 component 점수는 다른 component gap 때문에 삭제하지 않는다.
4. `verified_supported_score`는 항상 확인된 부분의 합계를 보여준다.
5. `provisional_score_interval`은 아직 열린 항목의 범위를 보여준다.
6. `FULL_E2R_100`은 모든 material component assessment가 terminal일 때만 허용한다.
7. terminal absence는 0점으로 finalization 가능하다.
8. provider/source/budget pending은 full finalization을 막는다.
9. event partial과 full thesis score를 분리한다.
10. risk overlay는 total score와 별도 trace를 가진다.

예상 출력 형태:

```text
verified_supported_score: 52.4
provisional_score_interval: 52.4 ~ 78.0
full_score_valid: false
stage_decision_status: PENDING_MATERIAL_COMPONENTS
```

또는 모든 component가 terminal이면:

```text
full_e2r_score: 74.1
full_score_valid: true
canonical_stage: Stage2 / Yellow / ...
```

Hard acceptance:

```text
balanced_point_score_count = 0
calibrated_profile_not_used_count = 0
supported_component_lost_count = 0
full_score_with_nonterminal_component_count = 0
component_sum_total_mismatch_count = 0
```

커밋:

```text
Phase 49 연구 보정 component 점수와 provisional interval 구현
```

---

# 14. Phase 50 — Atomic StageCourt v2

`AtomicStageDecision`을 확장한다.

```text
score_type
verified_supported_score
provisional_score_lower
provisional_score_upper
full_e2r_score
full_score_valid
component_assessment_ids
claim_impact_ids
material_nonterminal_components
risk_overlay
canonical_stage
decision_status
```

Decision status:

```text
FINAL
PENDING_MATERIAL_COMPONENTS
PROVIDER_PENDING
SOURCE_PENDING
BUDGET_PENDING
RISK_REVIEW
DISPROVED
```

Stage rules:

```text
- full_score_valid=false인데 canonical full Stage 확정 금지
- verified component score는 보존
- pending은 0점이 아니라 미완료 상태
- hard break는 current direct OPEN negative claim 필요
```

StageCourt trace는:

```text
claim
→ impact
→ component assessment
→ component points
→ total
→ Stage
```

를 완전히 연결한다.

Hard acceptance:

```text
stage_without_component_vector_count = 0
score_without_impact_lineage_count = 0
pending_score_erased_count = 0
hard_break_without_current_direct_open_count = 0
atomic_trace_mismatch_count = 0
```

커밋:

```text
Phase 50 component 점수와 StageCourt 원자결정 통합
```

---

# 15. Phase 51 — Acceptance Probe Removal from Readiness

현재 acceptance probe는 기능 smoke로만 유지할 수 있다.

그러나 다음에는 사용할 수 없다.

```text
- organic accepted claim count
- organic score contribution count
- current operational score readiness
- final READY
```

분류:

```text
CONTROLLED_CLAIM_PROBE_PASS
```

별도 라벨로만 남긴다.

Canonical readiness는 반드시 다음 leaf에서 읽는다.

```text
base live current run
base targeted full-thesis run
organic source task
organic fetched document
organic accepted current claim
organic claim impact
organic component score
```

Hard acceptance:

```text
probe_claim_counted_organic_count = 0
probe_decision_merged_into_canonical_score_count = 0
NO_SCORE_probe_unlocks_readiness_count = 0
```

커밋:

```text
Phase 51 acceptance probe와 organic 운영점수 분리
```

---

# 16. Phase 52 — Final Readiness Hard Gate 수정

기존 `MEANINGFUL_E2R_RUNTIME_READY`를 폐기하거나 v2로 올린다.

새 중간 라벨:

```text
LIVE_MATERIALIZATION_PASS
ORGANIC_CLAIM_COMPILATION_PASS
RESEARCH_CALIBRATED_COMPONENT_SCORING_PASS
SAMSUNG_CANONICAL_FULL_THESIS_PASS
SK_HYNIX_CANONICAL_FULL_THESIS_PASS
C06_CANONICAL_LIVE_CUTOVER_PASS
```

최종:

```text
MEANINGFUL_E2R_SCORING_READY
```

최종 readiness에 반드시 포함:

```text
organic accepted claim count > 0
organic validated impact count > 0
organic verified component points > 0
calibrated profile used count > 0
score_valid/full thesis result for mandatory canaries
NO_SCORE-only decision count cannot satisfy readiness
probe-only evidence cannot satisfy readiness
```

Reviewer D/F도 다음을 검사한다.

```text
- score_valid true canary count
- full component vector count
- organic evidence origin
- calibrated weight usage
- balanced point usage zero
```

커밋:

```text
Phase 52 organic component 점수 없는 READY 판정 차단
```

---

# 17. Phase 53 — C06 Current Evidence Dossier Orchestrator

삼성전자·SK하이닉스는 C06 canonical integration canary다.

별도 production exception이 아니라, target list를 받는 generic dossier runner를 만든다.

예:

```text
python -m e2r.cli.run_e2r_full_thesis_dossier_until_pass \
  --as-of-date 2026-07-11 \
  --symbols 005930,000660 \
  --materialize-live-input true \
  --live-materialization-authorized true \
  --canonical-archetype C06_HBM_MEMORY_CUSTOMER_CAPACITY \
  --max-research-iterations 12 \
  --max-code-repair-iterations 10
```

C06 question families:

```text
1. Current HBM customer allocation / customer commitment
2. Capacity constraint / sold-out / pre-sold status
3. Qualification pass / lag / reopen state
4. Shipment / mass production / product generation
5. HBM revenue mix / AI memory mix
6. ASP / pricing actual
7. Revenue / operating profit actual conversion
8. Margin / FCF conversion
9. Medium-term earnings revision / consensus visibility
10. Conventional memory drag / counter thesis
11. Capex / supply response / oversupply risk
12. Customer concentration and dependency
```

중요:

```text
질문 family는 Evidence Recipe다.
literal search query는 Research Brain이 현재 context로 생성한다.
```

Source priority:

```text
1. issuer earnings release / IR / newsroom / conference call
2. OpenDART official filing
3. customer official statement
4. CompanyGuide / public report / consensus source
5. Reuters / trusted industry media
6. Naver/general web discovery → original full source fetch
```

각 질문은 다음 terminal status를 가져야 한다.

```text
SUPPORTED
PARTIALLY_SUPPORTED
EVALUATED_ABSENT
COUNTERED
SOURCE_EXHAUSTED
PROVIDER_PENDING
```

단순 `MISSING` 금지.

커밋:

```text
Phase 53 삼성전자·하이닉스 C06 full-thesis 조사 오케스트레이터 구현
```

---

# 18. Phase 54 — Adaptive Organic Claim Closure

각 canary에서 다음 funnel을 반복한다.

```text
question
→ query
→ source result
→ full document
→ claim
→ impact
→ component closure
```

실패 유형:

```text
NO_DOCUMENT_FOUND
WRONG_SUBJECT
STALE_ONLY
GENERIC_CONTEXT_ONLY
REROUTED_PRIMITIVE
IMPACT_MAPPING_REJECTED
COUNTER_ONLY
PROVIDER_FAILED
SOURCE_EXHAUSTED
```

다음 iteration은 failure-specific이어야 한다.

예:

```text
REROUTED_PRIMITIVE:
원래 gap은 유지
새ly discovered component impact는 점수에 반영
원래 질문의 source route는 수정

GENERIC_CONTEXT_ONLY:
issuer/customer directness를 강화

STALE_ONLY:
current lifecycle/2026 source로 이동

COUNTER_ONLY:
counter assessment와 새로운 positive search를 병행
```

동일 query 반복 금지.

Organic run에서 claim이 0이면:

```text
query count를 무작정 늘리지 말고
document selection / claim extraction / impact mapping failure cluster를 수정한다.
```

출력:

```text
dossier_iterations.jsonl
question_closure.jsonl
query_change_log.jsonl
impact_change_log.jsonl
component_delta_log.jsonl
```

커밋:

```text
Phase 54 C06 organic claim과 component gap adaptive closure 구현
```

---

# 19. Phase 55 — Historical C06 Blind Component Replay

현재 live score bridge가 연구와 동형인지 검증한다.

필수 historical cases:

```text
SK hynix 2024-05-02 sold-out / customer-capacity positive
SK hynix 2025-01-23 revenue-mix positive
Samsung 2024-05-24 qualification-lag guard
Samsung 2025-01-31 reopen/customer-dependency cap
package/substrate sympathy profile guard
```

규칙:

```text
- historical outcome/MFE/MAE는 planner/adjudicator prompt에서 숨김
- source-backed URL과 historical as-of만 사용
- claim→impact→component vector를 재생
```

필수 관계:

```text
SK hynix sold-out/revenue-mix case:
customer/capacity/visibility impacts가 qualification-lag Samsung case보다 강함

Samsung qualification-lag:
execution counter는 존재
hard 4C는 아님

package/substrate profile:
profile component는 일부 열 수 있으나
customer allocation/revenue conversion은 열지 않음
```

정확한 historical total score를 강제로 복사하지 않는다.

검증할 것:

```text
- component attribution
- relative ordering
- guard behavior
- unsupported aspects
```

Tolerance:

```text
component assignment precision >= 95%
positive/counter direction accuracy >= 95%
critical guard accuracy = 100%
future leakage = 0
```

커밋:

```text
Phase 55 C06 연구 판례와 live component 점수 동형성 검증
```

---

# 20. Phase 56 — Samsung / SK Hynix Mandatory Acceptance

두 종목 각각 다음을 만족해야 한다.

## 20.1 Organic provenance

```text
- acceptance probe 아님
- fixture/snapshot 아님
- canonical planner/source task에서 생성
- actual live/fresh full source
- exact quote
- content hash
- target/date/current validation
```

## 20.2 Claim/impact

```text
- accepted current claims > 0
- validated claim impacts > 0
- at least one many-to-many claim mapping or explicit proof that all claims are truly single-impact
- rerouted valid impacts preserved
- no source proxy score
```

## 20.3 Component assessment

C06 contract의 모든 material component가 다음 terminal 중 하나여야 한다.

```text
VERIFIED_*_SUPPORT
VERIFIED_ABSENT_AFTER_SEARCH
VERIFIED_COUNTER
NOT_APPLICABLE
```

다음은 허용되지 않는다.

```text
UNKNOWN_UNINVESTIGATED
PROVIDER_PENDING
SOURCE_PENDING
BUDGET_PENDING
```

단, 진짜 외부 blocker면 Goal은 READY가 아니라 exact blocker다.

## 20.4 Score

```text
- calibrated profile loaded
- verified_supported_score > 0
- component score vector 존재
- provisional interval 존재
- full_score_valid=true
- score_type=FULL_E2R_100
- no balanced-points score
```

Positive evidence가 없는 component는 0점일 수 있다.
그러나 충분히 조사된 0점이어야 한다.

## 20.5 Stage

```text
- deterministic StageCourt
- atomic trace
- score/Stage/claim/impact/component IDs 일치
- Stage는 실제 증거에 따라 어떤 값도 가능
- Green/Yellow/고점수를 강제하지 않음
```

## 20.6 Evidence family coverage

각 종목은 최소 다음 family를 조사하고 상태를 남긴다.

```text
issuer official
official filing
independent trusted source or customer/industry source
financial/revision source
```

모든 family가 positive claim을 줄 필요는 없다.

## 20.7 Red-team

```text
- Samsung qualification/execution risk
- Hynix customer concentration / memory-cycle risk
- conventional memory drag
- capacity expansion / oversupply counter
```

가 현재 source로 검토돼야 한다.

## 20.8 No hardcoded expected outcome

다음 assertion은 금지한다.

```text
Samsung must be 90+
Hynix must be Green
Hynix score > Samsung
```

다만 historical replay의 component attribution/guard 관계는 지켜야 한다.

---

# 21. Phase 57 — Generalization Canaries

삼성/하이닉스만 통과하도록 과적합하지 않았는지 확인한다.

최소 추가 canary:

```text
C08 direct customer/order positive
C08 product-profile-only guard
C15 issuer pass-through positive
C15 raw commodity headline guard
wrong-subject accounting fixture
old-risk-resolved fixture
```

검증:

```text
- same many-to-many bridge
- calibrated profile loader
- evaluated absent state
- partial component preservation
- no source proxy score
```

커밋:

```text
Phase 57 반도체 외 evidence-to-score bridge 일반화 검증
```

---

# 22. Known-Bad Regression

반드시 실패해야 하는 fixture:

```text
1. SourceTask count로 100점 균등분배
2. 모든 primitive material/green_required
3. direct task closure-only scoring
4. rerouted valid claim score impact 폐기
5. rerouted claim original gap closure
6. one claim multiple impact 금지
7. mapping ID overwrite
8. same claim duplicate economic credit
9. claim total credit budget 초과
10. component gap 하나로 supported component 삭제
11. VERIFIED_ABSENT를 UNKNOWN으로 처리
12. UNKNOWN_UNINVESTIGATED를 0점 final로 처리
13. provider pending인데 full score
14. acceptance probe를 organic claim으로 계산
15. NO_SCORE probe로 readiness PASS
16. calibrated profile 미사용
17. historical outcome prompt leakage
18. Samsung Q1 ASP/record-profit claim을 customer allocation으로 과매핑
19. Samsung Q1 claim을 아무 component에도 못 쓰고 폐기
20. qualification lag를 hard 4C
21. HBM keyword를 sold-out capacity로 과매핑
22. package substrate profile을 target HBM customer allocation으로 과매핑
23. Stage/score/component trace mismatch
24. organic canary claim 0인데 READY
25. full_score_valid=false인데 meaningful scoring READY
```

---

# 23. 필수 테스트

예시:

```text
tests/test_production_no_balanced_points.py
tests/test_canonical_archetype_scoring_contract.py
tests/test_evidence_impact_rubric_compiler.py
tests/test_claim_many_to_many_impacts.py
tests/test_rerouted_claim_scores_new_component.py
tests/test_rerouted_claim_does_not_close_original_gap.py
tests/test_claim_mapping_lineage_preserved.py
tests/test_evidence_impact_adjudicator.py
tests/test_impact_credit_caps.py
tests/test_component_assessment_states.py
tests/test_evaluated_absent_allows_finalization.py
tests/test_unknown_uninvestigated_blocks_finalization.py
tests/test_partial_component_score_preserved.py
tests/test_research_calibrated_component_scorer.py
tests/test_atomic_stagecourt_component_trace.py
tests/test_acceptance_probe_not_organic.py
tests/test_final_readiness_requires_valid_score.py
tests/test_c06_historical_component_replay.py
tests/test_samsung_hynix_canonical_dossier.py
tests/test_samsung_q1_claim_component_impacts.py
tests/test_c06_qualification_lag_guard.py
tests/test_evidence_to_score_generalization.py
```

전체:

```bash
PYTHONPATH=src python -m unittest discover -s tests -v
```

No skip / no xfail for this Goal.

---

# 24. Live Acceptance Commands

기준일:

```text
2026-07-11 KST
```

비거래일이어도 source as-of로 사용한다.
시장 데이터는 latest available trading snapshot을 명시한다.

## Samsung

```bash
PYTHONPATH=src python -m e2r.cli.run_e2r_full_thesis_dossier_until_pass \
  --as-of-date 2026-07-11 \
  --symbol 005930 \
  --company "삼성전자" \
  --canonical-archetype C06_HBM_MEMORY_CUSTOMER_CAPACITY \
  --materialize-live-input true \
  --live-materialization-authorized true \
  --max-research-iterations 12 \
  --max-code-repair-iterations 10 \
  --require-organic-claim true \
  --require-calibrated-component-score true \
  --require-full-score-valid true \
  --output-root output/evidence_to_score/c06/2026-07-11/005930
```

## SK Hynix

```bash
PYTHONPATH=src python -m e2r.cli.run_e2r_full_thesis_dossier_until_pass \
  --as-of-date 2026-07-11 \
  --symbol 000660 \
  --company "SK하이닉스" \
  --canonical-archetype C06_HBM_MEMORY_CUSTOMER_CAPACITY \
  --materialize-live-input true \
  --live-materialization-authorized true \
  --max-research-iterations 12 \
  --max-code-repair-iterations 10 \
  --require-organic-claim true \
  --require-calibrated-component-score true \
  --require-full-score-valid true \
  --output-root output/evidence_to_score/c06/2026-07-11/000660
```

실제 CLI 명칭은 현재 레포 convention에 맞출 수 있다.
그러나 동등한 기능과 hard gates를 가져야 한다.

---

# 25. Mandatory Output Artifacts

각 종목:

```text
source_timeline.jsonl
research_brain_plans.jsonl
question_source_tasks.jsonl
provider_fetch_results.jsonl
evidence_documents.jsonl
evidence_anchors.jsonl
raw_assertions.jsonl
adjudicated_claims.jsonl
accepted_current_claims.jsonl
claim_provenance.jsonl
claim_impacts_proposed.jsonl
claim_impacts_validated.jsonl
claim_impact_ledger.jsonl
component_assessments.jsonl
component_score_vector.json
score_interval.json
atomic_stage_decision.json
stagecourt_trace.json
question_closure.jsonl
dossier_iterations.jsonl
operator_digest.md
audit_summary.json
```

통합 docs:

```text
docs/operational/e2r_evidence_to_score_forensic_baseline.md
docs/operational/e2r_canonical_scoring_contract_audit.json
docs/operational/e2r_evidence_impact_rubric_audit.json
docs/operational/e2r_claim_impact_ledger_audit.json
docs/operational/e2r_component_assessment_audit.json
docs/operational/e2r_research_calibrated_score_audit.json
docs/operational/e2r_acceptance_probe_separation_audit.json
docs/operational/e2r_c06_historical_component_replay.json
docs/operational/e2r_samsung_full_thesis_acceptance.md
docs/operational/e2r_sk_hynix_full_thesis_acceptance.md
docs/operational/e2r_c06_live_cutover_acceptance.md
docs/operational/e2r_evidence_to_score_self_repair_summary.md
docs/operational/e2r_meaningful_scoring_readiness_verdict.md
```

---

# 26. Conversion Funnel

다음을 before/after로 기록한다.

```text
fetched documents
→ raw assertions
→ accepted claims
→ validated impacts
→ supported components
→ evaluated absent components
→ verified supported score
→ full score valid
→ Stage
```

특히 기록:

```text
organic accepted claim rate
accepted claim → impact conversion rate
impact → component score conversion rate
rerouted claim retained rate
supported component preservation rate
full thesis closure rate
```

Task count/search result count만 progress로 말하지 않는다.

---

# 27. Self-Repair Until Both Pass

Self-repair loop는 삼성전자와 SK하이닉스가 모두 통과할 때까지 계속한다.

Failure classes:

```text
CALIBRATED_PROFILE_NOT_LOADED
BALANCED_POINTS_STILL_REACHABLE
CLAIM_MAPPING_LINEAGE_LOST
REROUTED_VALID_IMPACT_DROPPED
MULTI_IMPACT_REJECTED
IMPACT_ADJUDICATION_FAILED
IMPACT_CAP_INVALID
COMPONENT_STATE_COLLAPSED
SUPPORTED_SCORE_ERASED
FULL_SCORE_BLOCKED_BY_EVALUATED_ABSENT
UNKNOWN_ALLOWED_FINAL
ORGANIC_CLAIM_ZERO
DOCUMENT_RELEVANCE_LOW
QUESTION_CLOSURE_ZERO
FULL_SCORE_INVALID
STAGE_TRACE_MISMATCH
PROBE_CONTAMINATION
EXTERNAL_PROVIDER_BLOCKER
```

각 iteration:

```text
iteration
symbol
failure class
root cause file/function
before metrics
patch
focused tests
same live command
after metrics
resolved/unresolved
```

금지:

```text
- same query only retry
- threshold loosening
- expected score hardcoding
- synthetic claim
- probe promotion
- fixture as live
```

최대 iteration에 도달해도 내부 failure가 남으면 Goal 완료가 아니다.

---

# 28. Independent Reviewer Gate

Reviewer A — Scoring Contract

```text
canonical profile use
balanced points absence
component weights
```

Reviewer B — Claim Impact Semantics

```text
many-to-many mapping
rerouted impact preservation
unsupported aspect
double count
```

Reviewer C — Component State

```text
support/partial/absent/unknown/pending distinction
partial score preservation
```

Reviewer D — Organic Source & Provenance

```text
probe/fixture exclusion
actual source/quote/hash/current target
```

Reviewer E — Score & Stage

```text
component vector
score interval
full score validity
atomic StageCourt
```

Reviewer F — Samsung/Hynix C06 Semantics

```text
allocation/capacity/qualification/revenue mix/margin/revision/counter thesis
no forced outcome
```

Reviewer G — Generalization

```text
C08/C15/wrong-subject/old-risk guards
```

각 Reviewer는 leaf artifact를 독립적으로 읽는다.
critical 1개면 FAIL이다.

---

# 29. Final Labels

중간:

```text
CANONICAL_SCORING_CONTRACT_PASS
RESEARCH_CALIBRATED_IMPACT_RUBRIC_PASS
MANY_TO_MANY_CLAIM_IMPACT_PASS
COMPONENT_ASSESSMENT_STATE_PASS
ORGANIC_COMPONENT_SCORING_PASS
SAMSUNG_CANONICAL_FULL_THESIS_PASS
SK_HYNIX_CANONICAL_FULL_THESIS_PASS
C06_CANONICAL_LIVE_CUTOVER_PASS
```

최종:

```text
MEANINGFUL_E2R_SCORING_READY
```

외부 blocker:

```text
EXTERNAL_SOURCE_BLOCKER_NOT_READY
```

단 외부 blocker는 내부 score bridge가 완성되고,
실제 provider failure가 leaf로 증명된 경우에만 허용한다.

---

# 30. Final Hard Gates

`MEANINGFUL_E2R_SCORING_READY`는 다음을 모두 요구한다.

## Code

```text
production_balanced_points_usage_count = 0
production_direct_only_scoring_count = 0
production_claim_single_primitive_count = 0
```

## Organic evidence

```text
Samsung organic accepted claims > 0
Hynix organic accepted claims > 0
probe claim counted organic = 0
```

## Impact

```text
validated impact count > 0 for both
rerouted valid impact lost = 0
mapping lineage loss = 0
double count = 0
```

## Components

```text
both have complete material component assessments
UNKNOWN_UNINVESTIGATED = 0
PROVIDER/SOURCE/BUDGET_PENDING = 0
verified_supported_score > 0
```

## Scores

```text
both use calibrated profile
both full_score_valid=true
both score_type=FULL_E2R_100
both component vector sum matches total
```

## Stage

```text
both have deterministic StageCourt trace
score/stage/claims/impacts/components match
no forced expected Stage
```

## Replay/generalization

```text
C06 historical replay PASS
C08/C15 guard replay PASS
future leakage 0
source proxy score 0
```

## Verification

```text
full unittest PASS
known-bad PASS
Reviewer A~G PASS
critical count 0
blockers []
same run replay variance 0
repo_dirty=false
```

---

# 31. 절대 완료가 아닌 상태

다음은 완료가 아니다.

```text
삼성/하이닉스 모두 Stage0 NO_SCORE
verified_supported_score만 있고 full_score_valid=false
acceptance probe claim만 존재
SourceTask 수만 증가
검색 결과 수만 증가
component vector가 balanced points
rerouted claim은 ledger에 있지만 score에서 사라짐
모든 missing을 UNKNOWN으로 남김
historical replay만 PASS
한 종목만 PASS
report 문구만 READY
```

---

# 32. Final Response Format

완료 후 다음만 보고한다.

1. Final status
2. Phase commits / push / clean worktree
3. Full tests / known-bad
4. Root causes fixed
5. Canonical scoring contract
6. Evidence impact rubric
7. Many-to-many claim impact audit
8. Component state audit
9. Samsung organic source/claim/impact/component/score/Stage
10. SK Hynix organic source/claim/impact/component/score/Stage
11. C06 historical replay
12. Generalization canaries
13. Self-repair iterations
14. Reviewer A~G
15. Remaining blockers
16. Exact verdict

---

# 33. 마지막 명령

이번 Goal의 목적은 더 많은 증거를 모으고도 0점을 주는 시스템을 만드는 것이 아니다.

목적은:

```text
검증된 claim을
과거 연구가 정의한 경제적 의미로 해석하고,
여러 primitive/component에 bounded하게 반영하고,
확인된 점수는 보존하며,
미확인 항목은 score interval과 pending으로 분리하고,
모든 material component가 평가되면
deterministic full score와 Stage를 내는 것
```

이다.

삼성전자와 SK하이닉스는 이 bridge의 mandatory canonical proof다.

두 종목이 실제 운영 경로에서:

```text
organic source
→ accepted current claim
→ validated claim impacts
→ calibrated component score vector
→ FULL_E2R_100
→ deterministic StageCourt
```

까지 닫히기 전에는 Goal 완료라고 말하지 마라.

높은 점수나 Green을 강제하지 마라.

그러나 증거가 풍부한 두 종목을 실제로 조사하고도
`NO_SCORE / Stage0`만 내는 상태를 안전성 PASS라고 포장하지 마라.

코드 문제라면 고치고,
조사 문제라면 source/query/document/claim closure를 고치고,
동일 live run을 다시 실행하라.

최종적으로 다음 두 라벨이 모두 PASS일 때만:

```text
SAMSUNG_CANONICAL_FULL_THESIS_PASS
SK_HYNIX_CANONICAL_FULL_THESIS_PASS
```

그리고 전체 Reviewer와 테스트가 통과한 경우에만:

```text
MEANINGFUL_E2R_SCORING_READY
```

를 선언하라.
