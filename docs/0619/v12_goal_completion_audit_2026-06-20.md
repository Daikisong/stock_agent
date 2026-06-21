# V12 Goal Completion Audit

이 문서는 원래 질문을 요구사항별로 쪼개서, 현재 워킹트리와 replay 결과가 어디까지 증명하는지 정리한다.

## Overall Status

`complete_for_claim_backed_guard_status_fixture_scope`

완전히 막연한 의미의 "모든 연구 row가 운영에서 Green으로 재현된다"까지 증명된 것은 아니다. 대신 다음 범위는 증명됐다.

- raw `Stage3-Green`이고 source-backed 준비가 된 Green fixture 26개 중 guard primitive가 없는 15개는 운영/ledger replay에서 `near_parity_green`
- raw Green fixture 11개는 `cost_overrun`, `valuation_overheat`, `call_off_risk` 같은 guard primitive가 같이 있었고, 최신 guard-status 분리 후에는 연구-ledger의 `guard_cleared` counterclaim을 붙인 경우 `ledger_only_green`으로 복원된다. 운영-only는 guard 해소 claim이 없으면 보수적으로 `3-Yellow`에 남는다.
- guard fixture 36개는 모두 `guard_pass`
- 이전에 `4개 ledger_only_green`으로 보였던 row는 원문 연구 라벨이 `Stage3-Yellow` 또는 `Stage2-Actionable`이라 Green fixture가 아니었음
- SK하이닉스 C06 2024-04-25와 2024-04-30은 현재 운영 replay에서 더 이상 증거 부족 Yellow로 떨어지지 않음
- 운영 출력에 아키타입, component score, claim-backed diagnostics가 구조화됨
- 36개 canonical archetype의 Evidence Contract가 `configs/e2r_archetype_evidence_contracts_v12.json`로 runtime에 올라갔고, post-parse/post-score LLM gap context에 contract primitive가 전달됨
- 운영 replay row에 `evidence_contract_coverage_pct`, `evidence_contract_missing_primitives`가 저장되어 낮은 점수의 빈 primitive를 직접 볼 수 있음
- positive primitive와 guard primitive가 분리되어, guard-only 아키타입을 positive coverage 100으로 오해하지 않음
- Green gate primitive가 missing이거나 guard primitive가 PRESENT이면 총점이 높아도 Stage 3-Green으로 승격하지 않음. 다만 guard primitive가 negative/counter claim으로 해소되면 `guard_cleared`로 세어 Green 검증을 통과할 수 있음
- claim compiler가 운영 bookkeeping 필드를 claim으로 세지 않게 조여졌고, 이 조임 후에도 하닉과 전체 준비 fixture parity가 유지됨
- replay output이 component별 `score_contribution_claim_ids`를 저장하므로 "어느 claim 때문에 어떤 component 점수가 들어갔는지"를 row 단위로 감사할 수 있음
- score output contract가 high-confidence row의 component claim mapping 누락까지 잡으므로, ratio만 100이고 실제 mapping이 비는 출력은 통과하지 못함
- replay output이 `score_contribution_ledger`도 저장하므로 component별 `raw_points/max_points/support_claim_ids/cap_reason`을 직접 확인할 수 있음
- score output contract가 high-confidence row의 contribution ledger 누락까지 잡으므로, claim ID mapping만 있고 점수 row ledger가 비는 출력도 통과하지 못함

## Requirement Audit

| id | status | 핵심 판정 |
| --- | --- | --- |
| R1_skhynix_20240425_research_value | proven | 2024-04-25 `3-Green / 97.3447`은 이전 연구 ledger artifact에서 확인됨. 최신 claim-backed fixture replay 값은 `3-Green / 98.173` |
| R2_skhynix_20240430_979877_value | proven_as_carried_forward_fixture | `97.9877`은 4/25 source fixture를 이후 날짜로 carried-forward한 과거 runtime fixture 값으로 확인됨. 독립 4/30 raw research row는 아님. 현재 운영 replay는 `98.2804` |
| R3_skhynix_current_operational_replay | proven | 4/25와 4/30 모두 운영 replay에서 C06 Green 복원 |
| R4_component_weight_visibility | proven | replay JSON/CSV에 7개 component score와 risk penalty를 구조화 |
| R5_claim_backed_score_guard | proven_for_verified_replay_scope | SK하이닉스와 준비 fixture 범위에서 claim-backed ratio 100, orphan 0 |
| R6_prepared_research_fixture_parity | proven_for_guard_status_raw_stage3_green_fixture_scope | guard 없는 raw Stage3-Green 15/15 near parity, guard-bearing raw Green 11개는 ledger guard-cleared counterclaim으로 ledger_only_green, guard 36/36 pass |
| R7_all_archetype_scope | proven_for_fixture_scope_not_universal_live | guard 36개와 raw Stage3-Green 26개를 모두 검사했고, Green 승격은 guard-safe 15개로 제한됨. 모든 미래 live 후보까지 보장한다는 뜻은 아님 |
| R8_no_archetype_mismatch_false_pass | proven | 다른 아키타입으로 맞은 Green은 parity 통과 못 하게 mismatch bucket 추가 |
| R9_archetype_evidence_contract_runtime_context | proven_as_runtime_gap_context | 36개 아키타입 primitive contract가 LLM gap search 문맥에 전달됨 |
| R10_runtime_contract_coverage_output | proven | 운영 replay JSON/CSV에 contract coverage와 missing primitive가 출력됨 |
| R11_positive_guard_primitive_split | proven | positive bridge, Green gate, Green 차단 guard primitive를 분리함 |

## 쉬운 예

하닉 2024-04-25는 이제 이렇게 된다.

```text
Reuters HBM/capacity/revision 근거
→ C06 source-backed field
→ claim-backed component score
→ evidence contract coverage 6/6
→ positive coverage 100, guard present 0
→ orphan score 0
→ 3-Green / 97.423
```

예전처럼 이렇게 되지 않는다.

```text
Reuters 근거는 있음
→ runtime field가 비어 있음
→ backlog/contract/CAPA 0
→ 76점대 Yellow
```

아키타입 contract는 이런 식으로 작동한다.

```text
C28 SOFTWARE_SECURITY
→ required_primitives: arr_growth_visible, nrr, retention_or_renewal, rpo_to_sales, recurring_margin_leverage
→ post-score gap context에 위 primitive가 들어감
→ replay output에 missing primitive가 row 단위로 남음
→ LLM이 "소프트웨어 유지율/ARR/RPO evidence"를 찾는 query를 만들 수 있음
→ 코드는 URL/as_of/claim/source-backed 여부만 검증하고 점수는 deterministic scorer가 계산
```

Guard-only 예시는 이렇게 다룬다.

```text
R13 HIGH_MAE
→ positive_primitives: none
→ guard_primitives: high_mae_history, valuation_overheat, liquidity_or_microcap_risk ...
→ positive coverage를 100으로 표시하지 않음
→ guard present가 있으면 Green 차단/주의 쪽으로 해석
```

Guard가 있는 Green 예시는 이렇게 다룬다.

```text
C05 EPC
→ positive bridge는 다 있음
→ cost_overrun을 확인하지 못함: 운영-only는 3-Yellow 보류
→ cost_overrun 리스크가 해소됐다는 source-backed counterclaim 있음: ledger fixture는 guard_cleared=1, guard_missing=0, Green 가능
→ cost_overrun이 실제 발생했다는 claim 있음: guard_present=1, Green 금지
```

이번 피드백 기준으로 보면, 남아 있던 가장 큰 오해는 "연구 row가 좋으면 전부 Green fixture"라고 본 부분이었다.

```text
Stage3-Green = Green 복원 검증 대상
Stage3-Yellow = 좋은 근거는 있지만 Green 문턱 미달
Stage2-Actionable = 추적할 후보지만 Green 아님
guard = Green으로 열리면 안 되는 반례
```

그래서 C12/C16/C24 일부 row가 Yellow로 막힌 것은 evidence compiler 실패가 아니라 연구 라벨과 운영 판정이 맞은 사례다.

## Known Exclusions

C08은 현재 "빠진 Green"이라기보다 "Green으로 만들면 안 되는 Actionable/green-brake 자료"다. 예를 들어 direct URL이 있어도 연구 row가 `actionable_not_green`, `green_brake`로 적혀 있으면 Green fixture로 승격하지 않는다.

R13 high-MAE는 Green 발굴 아키타입이 아니라, 급등 후 큰 낙폭/과열/붕괴 위험이면 Green을 막는 guardrail이다. 따라서 이 아키타입의 acceptance는 `guard_pass`가 핵심이다.

## Verification

최근 확인:

```text
tests: 4014 passed
tests: 4017 passed after contract coverage output patch
focused contract tests: tests.test_evidence_claim tests.test_free_web_research_runner tests.test_asof_research_replay OK
git diff --check: passed
single SK hynix 2024-04-30 replay: 3-Green / 98.2804
single SK hynix 2024-04-25 replay: 3-Green / 97.423
SK hynix C06 contract coverage: 6/6, missing 0, coverage 100
tests: 4021 passed after Green gate primitive subset and CAPA claim alias patch
raw Stage3-Green fixture parity after feedback patch before guard-present correction: 26/26 near_parity_green, 36/36 guard_pass
full operational replay after feedback patch: 3827 candidates, 713 Stage 3-Green, 0 Stage 3-Yellow, 126770 date-verified documents, 0 future rejections
ledger fixture replay after feedback patch: 4191 candidates, 1015 Stage 3-Green, 11 Stage 3-Yellow, 140081 date-verified documents, 12 future documents rejected by as-of filter
tests: 4028 passed after claim-backed Green gate and score output contract patch
SK hynix 2024-04-25/04-30 after claim-backed Green gate: 3-Green 97.423 / 3-Green 98.2804, operational_merged, runtime_fixture_injected=false, claim-backed ratio 100, orphan 0, C06 primitive coverage 6/6
latest claim-backed fixture replay for SK hynix 2024-04-25: 3-Green 98.173; latest operational replay: 3-Green 97.423; parity gap 0.75
score output contract after high-confidence claim-backed gap patch: full operational replay findings 0, ledger fixture replay findings 0, SK hynix replay findings 0
orphan score rows after patch: operational 1843 rows and ledger 1843 rows, all Stage0/Stage1; Stage3/score>=65 orphan rows 0
claim compiler metadata filter patch: date_verified/green_allowed_by_date/runtime_fixture_source_backed/canonical_archetype_id/large_sector_id/evidence_contract_* are excluded from compiled claim primitives
post metadata filter replay v4 before guard-present correction: Green 26/26 near_parity_green, guard 36/36 guard_pass, full operational/ledger/Hynix score output contract findings 0
SK hynix 2024-04-25 after metadata filter: operational 3-Green 97.423, latest ledger 3-Green 98.173, gap 0.75
score contribution claim ledger output: SK hynix 2024-04-25 and 2024-04-30 both have score_contribution_claim_ids for 7/7 score components, score_claim_backed_component_ratio 100, orphan 0
post score contribution ledger contract replay v5 before guard-present correction: Green 26/26 near_parity_green, guard 36/36 guard_pass, operational/ledger/Hynix score output contract findings 0, high-confidence missing component claim mapping rows 0
post score contribution row ledger replay v6 before guard-present correction: Green 26/26 near_parity_green, guard 36/36 guard_pass, operational/ledger/Hynix score output contract findings 0, high-confidence missing score contribution ledger rows 0
SK hynix 2024-04-25 contribution rows: eps_fcf_explosion 20.0/20.0 with 58 claims, earnings_visibility 19.0851/20.0 with 50 claims, bottleneck_pricing 19.0851/20.0 with 29 claims
source-backed orphan guard replay: operational 3827 candidates / 713 Stage 3-Green; ledger 4191 candidates / 886 Stage 3-Green / 137 Stage 3-Yellow; guard-present Yellow blocks 126; Green claim ledger missing 0, orphan/ratio failures 0, unknown claim refs 0, Green contract findings 0
source-backed orphan guard parity audit: Green 15/26 near_parity_green, 11/26 intentionally blocked to Yellow by guard primitive, guard 36/36 guard_pass
raw agent numeric field guard: unbacked contract_duration/capa/asp numeric fields produce the same 0.0 score as baseline
raw agent text route guard: unbacked HBM agent field names no longer change archetype routing text
source-backed Green context orphan guard: source-backed/Green-gate rows with orphan score contributions are score_valid=false before Stage promotion
orphan score rows remain only in Stage0/Stage1 low-confidence rows; Stage2+/Green orphan rows 0
source-backed slot match strictness guard: matching now rejects token-only overlap and reversed-token matches, so a margin_quality evidence slot cannot back an unrelated unbacked_margin_bridge or broad margin field just because both contain "margin"
guard-unverified Green block: Stage 3-Green now requires guard_missing=0 when guard primitives are configured; latest operational replay moved 335 guard-UNKNOWN rows from Green to Yellow while SK hynix C06 remained Green
previous guard-unverified replay before guard_cleared polarity split: operational 3827 candidates / 378 Stage 3-Green / 335 Stage 3-Yellow; ledger 4191 candidates / 551 Stage 3-Green / 472 Stage 3-Yellow; score output contract findings 0; Green claim/orphan/guard findings 0
previous guard-unverified parity before guard_cleared polarity split: 15/26 near_parity_green, 11/26 both_not_green because operational and ledger both blocked to Yellow on guard verification, guard 36/36 guard_pass
tests: 4054 passed before guard_cleared polarity split after raw agent-field numeric/text claim gate, source-backed orphan guard, guard-present/guard-unverified Green block, carried-forward fixture parity guard, all-archetype Green gate missing block, all-archetype source-backed orphan score invalidation guard, all-archetype full-claim source-backed score validity guard, standard-flow official context/archetype contract propagation guard, Evidence Contract config integrity guard, all-archetype LLM contract gap-context guard, unbacked LLM primitive gap-context guard, evidence-contract stage-gate material gap guard, post-score search no-progress score-block guard, contract primitive-name progress signature guard, all-archetype source-field contract gap-context guard, all-archetype score contribution ledger unknown-claim guard, guard-only source-field gap-context guard, guard-only EvidenceContract gap-context guard, direct EvidenceContract positive/missing-positive split guard, source-backed slot ordered-token rejection guard, and score-state guard-unverified output contract guard
latest current-code daily replay 2024-04-25~2024-04-30: /tmp/e2r_goal_current_hynix_c06_20260621/2024-04-25_to_2024-04-30; 000660 rows are 3-Green 97.423 on 4/25 and 3-Green 98.2804 on 4/30, runtime_fixture_injected=false, claim-backed ratio 100, orphan 0
previous guard-unverified daily replay 2024-04-25~2024-04-30: /tmp/e2r_goal_current_hynix_guard_unverified_20260621/2024-04-25_to_2024-04-30; 000660 rows are still 3-Green 97.423 on 4/25 and 3-Green 98.2804 on 4/30, runtime_fixture_injected=false, claim-backed ratio 100, orphan 0, guard_missing 0
guard-status polarity fix: guard primitives now split into guard_present/support, guard_cleared/counter, and guard_missing/unknown; green fixture guard primitives are compiled as negative counterclaims, while guard fixture primitives remain positive risk claims
tests: 4058 passed after guard-status polarity fix, Stage/output-contract tests for guard_cleared and guard_present, and an all guard-bearing archetype regression test that guard_cleared does not leave guard archetypes permanently Yellow
latest guard-status daily replay 2024-04-25~2024-04-30: /tmp/e2r_goal_current_hynix_guard_status_20260621/2024-04-25_to_2024-04-30; 000660 rows are 3-Green 97.423 on 4/25 and 3-Green 98.2804 on 4/30, runtime_fixture_injected=false, score_source_mode=operational_merged, claim-backed ratio 100, orphan 0, contract/gate coverage 100, guard_present 0, guard_missing 0
latest guard-status operational replay: /tmp/e2r_goal_operational_guard_status_20260621/2020-01-01_to_2026-05-14; 3827 candidates, 378 Stage 3-Green, 335 Stage 3-Yellow, 126770 date-verified documents, 0 date-unverified documents, score output contract findings 0, Green bad 0
latest guard-status ledger replay: /tmp/e2r_goal_ledger_guard_status_20260621/2020-01-01_to_2026-05-14; 4191 candidates, 677 Stage 3-Green, 346 Stage 3-Yellow, 140081 date-verified documents, 12 future documents rejected by as-of filter, score output contract findings 0, Green bad 0
latest guard-status parity audit: /tmp/e2r_goalcheck_parity_guard_status_20260621/v12_research_ledger_operational_parity.json; green_bucket_counts {'near_parity_green': 15, 'ledger_only_green': 11}, guard_bucket_counts {'guard_pass': 36}, carried_fixture_green_count 273
latest guard-status ledger Green guard-cleared coverage: 126 Green rows carry guard_cleared counterclaims across 11 guard-bearing archetypes; Green rows with guard_present>0 or guard_missing>0 are 0
```
