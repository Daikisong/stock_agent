# V12 Operational Research Parity Goalcheck

이 문서는 2026-06-21 기준으로, 누적 연구자료의 Green/guard 사례가 현재 운영 replay 경로에서 다시 점수와 Stage로 복원되는지 확인한 결과다.

## 결론

SK하이닉스 C06 사례는 현재 운영 replay에서 연구 ledger와 거의 같은 값으로 복원된다.

| symbol | as-of | archetype | 운영 Stage/score | 연구 ledger Stage/score | 판정 |
| --- | --- | --- | --- | --- | --- |
| 000660 | 2024-04-25 | C06_HBM_MEMORY_CUSTOMER_CAPACITY | 3-Green / 97.423 | old runtime_fixture_injected 3-Green / 97.3447, latest claim-backed fixture 3-Green / 98.173 | near parity, latest gap 0.75 |
| 000660 | 2024-04-30 | C06_HBM_MEMORY_CUSTOMER_CAPACITY | 3-Green / 98.2804 | old runtime_fixture_spec carried-forward 3-Green / 97.9877 from the 2024-04-25 source fixture; 독립 4/30 raw research row는 아님 | 운영 Green 복원 확인 |

중요한 점은 두 운영 replay 모두 `runtime_fixture_injected=false`, `score_source_mode=operational_merged`라는 것이다. 즉 연구 정답 점수를 직접 꽂아서 맞춘 것이 아니라, 운영 replay가 source-backed evidence를 읽고 feature/score/stage를 계산했다.

2024-04-25의 `97.3447`은 과거 artifact의 exact `runtime_fixture_spec` row에 있던 값이고, `97.9877`은 같은 2024-04-25 source fixture를 이후 날짜로 carried-forward한 과거 `runtime_fixture_spec` row에 있던 값이다. 이번 확인의 핵심은 그 값을 다시 주입했다는 뜻이 아니라, 현재 운영 replay가 fixture 주입 없이 각각 `97.423`, `98.2804`를 계산했다는 점이다.

쉬운 예:

- 예전 문제: Reuters HBM sold-out/capacity/revision 근거가 있어도 runtime field가 비어 `76점대 Yellow`로 떨어졌다.
- 현재 결과: 같은 근거가 C06 source-backed bridge와 claim-backed component로 올라가 `97~98점 Green`으로 복원된다.

또한 이 패치는 SK하이닉스나 삼성전자 이름을 조건으로 점수를 주는 방식이 아니다. `src/e2r/pipeline`, `src/e2r/research`, `src/e2r/features.py`, `src/e2r/scoring.py`, `src/e2r/staging.py`, `src/e2r/stage_gate_diagnostics.py`, `src/e2r/score_validity.py`, `src/e2r/agentic`, `src/e2r/backtest` runtime 경로에서 `000660`, `005930`, `SK하이닉스`, `하이닉스`, `SK Hynix`, `Hynix`, `삼성전자`, `Samsung` 조건 검색 결과는 0건이었다. 종목명은 calibration/audit/fixture/sector research 파일에만 사례로 남아 있다.

2026-06-21 추가 정정:

```text
guard primitive는 이제 세 상태로 분리한다.
1. guard_present: 위험이 실제 확인됨 → Green 금지
2. guard_missing: 위험을 확인/반박하지 못함 → Green 보류
3. guard_cleared: 위험을 확인했고 source-backed counterclaim으로 해소됨 → Green 검증 통과 가능
```

쉬운 예:

```text
C05 EPC에서 positive bridge가 다 있어도 cost_overrun 확인이 없으면 운영-only는 Yellow다.
하지만 연구-ledger fixture가 "cost_overrun 리스크 해소" counterclaim을 갖고 있으면 guard_cleared=1, guard_missing=0이라 Green이 가능하다.
반대로 cost_overrun 발생 claim이면 guard_present=1이라 Green 금지다.
```

## 2024-04-30 Component Breakdown

`/tmp/e2r_single_hynix_20240430_components/2024-04-30_to_2024-04-30/discovered_candidates.json`에서 확인한 `000660` row:

| component | score |
| --- | ---: |
| EPS/FCF explosion | 20.0 |
| Earnings visibility | 19.5138 |
| Bottleneck pricing | 19.5138 |
| Market mispricing | 14.8455 |
| Valuation rerating | 14.8841 |
| Capital allocation | 5.0 |
| Information confidence | 3.0 |
| Risk penalty | 0.0 |
| Total | 98.2804 |

Claim-backed diagnostics:

| diagnostic | value |
| --- | ---: |
| claim_backed_claim_count | 100.0 |
| claim_backed_primitive_count | 100.0 |
| score_claim_backed_component_count | 7.0 |
| orphan_score_component_count | 0.0 |
| score_claim_backed_component_ratio | 100.0 |
| source_backed_green_bridge_raw | 97.5692 |
| evidence_contract_required_primitive_count | 6.0 |
| evidence_contract_present_primitive_count | 6.0 |
| evidence_contract_missing_primitive_count | 0.0 |
| evidence_contract_coverage_pct | 100.0 |
| evidence_contract_positive_coverage_pct | 100.0 |
| evidence_contract_positive_missing_primitive_count | 0.0 |
| evidence_contract_guard_present_primitive_count | 0.0 |
| evidence_contract_guard_missing_primitive_count | 0.0 |

2024-04-25도 같은 방식으로 확인했다.

```text
000660 / 2024-04-25 / C06
stage: 3-Green
score: 97.423
score_source_mode: operational_merged
runtime_fixture_injected: false
contract coverage: 6/6, missing 0, coverage 100
positive coverage: 100, missing positive 0, guard present 0, guard missing 0
claim-backed ratio: 100, orphan 0
```

## 전체 Replay Parity

새 구조화 출력, 아키타입 mismatch guard, Evidence Contract Green gate primitive, raw `Stage3-Green` fixture 기준을 반영한 전체 replay 결과:

```text
period: 2020-01-01 to 2026-05-14
replay_dates: 133
discovered_candidates: 3827
Stage 3-Green count after guard-unverified block: 378
Stage 3-Yellow count after guard-unverified block: 335
documents_rejected_after_asof: 0
documents_date_verified: 126770
documents_date_unverified: 0
```

연구 ledger parity audit 최신 결과:

```text
green_case_count: 26
guard_case_count: 36
green_bucket_counts: {'near_parity_green': 15, 'ledger_only_green': 11}
guard_bucket_counts: {'guard_pass': 36}
green_missing_lane_counts: {}
carried_fixture_count: 302
carried_fixture_green_count: 273
```

따라서 raw `Stage3-Green` 중 guard primitive가 없는 Green fixture는 운영 replay가 연구처럼 evidence를 읽어 거의 같은 Stage/score를 낸다. guard primitive가 있는 raw Green fixture는 연구-ledger에 `guard_cleared` counterclaim이 붙으면 Green이 되지만, 운영-only에서 해당 해소 claim을 못 찾으면 Yellow로 보류한다. 이전에 4개 `ledger_only_green`으로 보였던 C12/C16/C24 일부 row는 원문 연구 라벨이 `Stage3-Yellow` 또는 `Stage2-Actionable`이어서 Green fixture로 세면 안 되는 과집계였다.

최신 guard-status 전체 replay:

```text
operational output_root: /tmp/e2r_goal_operational_guard_status_20260621/2020-01-01_to_2026-05-14
operational candidates: 3827
operational Stage 3-Green / 3-Yellow: 378 / 335
ledger output_root: /tmp/e2r_goal_ledger_guard_status_20260621/2020-01-01_to_2026-05-14
ledger candidates: 4191
ledger Stage 3-Green / 3-Yellow: 677 / 346
parity output_root: /tmp/e2r_goalcheck_parity_guard_status_20260621
score output contract findings: operational 0, ledger 0
Green rows with claim/orphan/guard-present/guard-missing findings: 0
ledger Green rows with guard_cleared: 126 rows across 11 guard-bearing archetypes
tests: 4057 passed
```

쉬운 예:

```text
Stage3-Yellow row = 시험 답안에 "아직 A는 아니고 B+"라고 적힌 사례
이걸 Green fixture = A 정답으로 세면 운영이 Yellow를 내도 실패처럼 보인다.
정정 후에는 raw Stage3-Green만 Green 검증 대상으로 센다.
```

새 contract diagnostics와 raw Green 기준 정정 후에도 전체 replay를 다시 실행했다.

```text
output_root: /tmp/e2r_v12_parity_after_claim_gate_v3/2020-01-01_to_2026-05-14
discovered_candidates: 3827
Stage 3-Green count before guard-unverified block: 713
Stage 3-Yellow count: 0
documents_date_verified: 126770
documents_rejected_after_asof: 0
parity before guard-present correction: Green 26/26 near_parity_green, guard 36/36 guard_pass
Green rows with missing Green gate primitives: 0
```

Ledger fixture replay도 별도로 확인했다.

```text
output_root: /tmp/e2r_v12_parity_ledger_after_claim_gate_v3/2020-01-01_to_2026-05-14
discovered_candidates: 4191
Stage 3-Green count: 1015
Stage 3-Yellow count: 11
documents_date_verified: 140081
documents_rejected_after_asof: 12
```

여기서 `documents_rejected_after_asof=12`는 미래 문서를 점수에 넣었다는 뜻이 아니라, as-of 이후 문서가 필터에서 걸러졌다는 뜻이다.

## 제외 범위

이 문서는 “모든 연구 row를 Green으로 만들었다”는 뜻이 아니다.

- C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY: 연구자료의 direct URL row들은 대부분 `Stage2-Actionable`, `green_brake`, `actionable_not_green`으로 정리되어 있다. 즉 고객/소켓 근거가 있어도 Green은 막으라는 연구 결론이다.
- R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL: Green 발굴 아키타입이 아니라 높은 MAE/과열/붕괴 위험으로 Green 승격을 막는 cross-archetype guardrail이다. 따라서 guard pass가 핵심 검증이다.

이 둘을 proxy Green으로 억지 승격하면, 원래 문제였던 “근거 없는 점수”를 다시 만들게 된다.

## 구현상 보강된 점

1. 운영 replay 출력에 `canonical_archetype_id`, `large_sector_id`를 구조화해 저장한다.
2. 운영 replay 출력에 7개 component score와 `risk_penalty`를 구조화해 저장한다.
3. 운영 replay 출력에 claim-backed score diagnostics를 구조화해 저장한다.
4. parity audit가 운영 Green이 다른 아키타입으로 나온 경우 `operational_archetype_mismatch`로 분류한다.
5. 36개 canonical archetype Evidence Contract를 `configs/e2r_archetype_evidence_contracts_v12.json`로 runtime에 올렸다.
6. post-parse/post-score gap LLM context에 해당 archetype의 required primitive와 bridge axis를 전달한다.
7. `discovered_candidates.json/csv`에 `evidence_contract_coverage_pct`, `evidence_contract_positive_coverage_pct`, `evidence_contract_positive_missing_primitives`, `evidence_contract_guard_primitives` 등을 구조화해 저장한다.
8. positive primitive, Green gate primitive, guard primitive를 분리했다. 예를 들어 C11의 `customer_contract`는 Green gate이고 `call_off_risk`는 Green 차단 확인용 guard다.
9. Stage 3-Green은 Green gate primitive가 필요한 contract에서 `green gate coverage=100`과 `missing green gate=0`을 만족해야 한다.
10. `AsOfWebResearchRunner`가 공식 connector/cheap scan에서 만든 `base_feature_input`과 sector context를 받아 심층 조사 runner로 전달한다.
11. replay spec은 raw `Stage3-Green` trigger만 Green 검증 row로 만든다. `Stage3-Yellow`/`Stage2-Actionable` row는 Green이 아니라 skip/guard 쪽으로 남긴다.
12. R13 positive-control row가 C23/C02 같은 원천 아키타입을 재사용할 때 R13 guard primitive가 아니라 원천 아키타입 primitive로 fixture를 만든다.
13. 운영형 source-backed/evidence-contract 점수는 Stage 3-Green 승격 전에 `claim-backed component ratio=100`, `orphan score component=0`, `claim count>0`을 만족해야 한다. 이 조건을 못 맞추면 총점이 높아도 Yellow에 남고 `failed_claim_backed_green_score`로 진단된다.
14. serialized score output contract도 같은 기준을 검사한다. `score_valid=true`인 Stage 3 row 또는 visible score 65점 이상 row에서 source-backed/evidence-contract 문맥이 있는데 claim-backed gap이 있으면 `valid_high_confidence_claim_backed_gap` 위반으로 잡힌다.
15. claim compiler는 `date_verified`, `green_allowed_by_date`, `runtime_fixture_source_backed`, `canonical_archetype_id`, `large_sector_id`, `evidence_contract_*` 같은 운영 bookkeeping 필드를 claim으로 세지 않는다. 이 값들은 "문서 날짜가 검증됐다"는 메타정보이지 "고객 배정이 확인됐다"는 점수 claim이 아니기 때문이다.
16. `ScoreSnapshot`과 replay output에 `score_contribution_claim_ids`를 저장한다. 따라서 component별 점수에 어떤 claim ID가 붙었는지 JSON/CSV에서 바로 확인할 수 있다.
17. high-confidence source-backed/evidence-contract row에서 `score_contribution_claim_ids`가 없거나 nonzero component를 다 커버하지 않으면 `valid_high_confidence_score_contribution_claim_ids_missing`으로 잡힌다.
18. `ScoreSnapshot`과 replay output에 `score_contribution_ledger`를 저장한다. 각 row는 `component_key`, `raw_points`, `max_points`, `support_claim_ids`, `cap_reason`을 포함한다.
19. high-confidence source-backed/evidence-contract row에서 `score_contribution_ledger`가 없거나 nonzero component의 support claim을 다 담지 못하면 `valid_high_confidence_score_contribution_ledger_missing`으로 잡힌다.
20. 전체 tests와 `git diff --check`를 통과해야 한다.

쉬운 예:

```text
예전 gap: visibility 부족
현재 gap: C28에서 arr_growth_visible, nrr, retention_or_renewal, rpo_to_sales, recurring_margin_leverage가 부족
```

코드는 이 primitive로 deterministic query template을 찍어내지 않는다. LLM이 이 문맥을 보고 query를 제안하고, deterministic code는 as-of, 중복, source-backed claim 여부를 검증한다.

Guard-only 아키타입은 positive coverage를 100으로 표시하지 않는다. 예를 들어 R13 high-MAE나 C14 EV slowdown은 "좋은 증거가 다 찼다"가 아니라 "Green을 막는 guard primitive를 확인하는 contract"다.

현재 full replay 산출물에 새 score output contract를 적용하면 위반은 0개다.

```text
/tmp/e2r_v12_parity_after_claim_metadata_filter_v4/.../discovered_candidates.json: contract findings 0
/tmp/e2r_v12_parity_ledger_after_claim_metadata_filter_v4/.../discovered_candidates.json: contract findings 0
/tmp/e2r_verify_hynix_claim_metadata_filter_20260621/.../discovered_candidates.json: contract findings 0
```

orphan score는 남아 있지만 모두 Stage0/Stage1 저점 후보에만 있다. Stage3 또는 65점 이상 후보에는 없다.

메타 claim 제거 후 최신 v4 replay 결과도 동일하게 유지됐다.

```text
operational output_root: /tmp/e2r_v12_parity_after_claim_metadata_filter_v4/2020-01-01_to_2026-05-14
ledger output_root: /tmp/e2r_v12_parity_ledger_after_claim_metadata_filter_v4/2020-01-01_to_2026-05-14
parity output_root: /tmp/e2r_goalcheck_parity_after_claim_metadata_filter_v4
Green parity before guard-present correction: 26/26 near_parity_green
guard parity: 36/36 guard_pass
SK hynix 2024-04-25: operational 3-Green / 97.423, ledger 3-Green / 98.173, gap 0.75
```

component별 claim ledger 출력도 확인했다.

```text
/tmp/e2r_verify_hynix_score_contribution_ledger_20260621/.../discovered_candidates.json
2024-04-25 SK hynix C06: 7/7 score components have score_contribution_claim_ids, ratio 100, orphan 0
2024-04-30 SK hynix C06: 7/7 score components have score_contribution_claim_ids, ratio 100, orphan 0
```

component claim ledger 출력 contract까지 적용한 최신 v5 전체 replay도 통과했다.

```text
operational output_root: /tmp/e2r_v12_parity_after_score_contribution_ledger_v5/2020-01-01_to_2026-05-14
ledger output_root: /tmp/e2r_v12_parity_ledger_after_score_contribution_ledger_v5/2020-01-01_to_2026-05-14
parity output_root: /tmp/e2r_goalcheck_parity_after_score_contribution_ledger_v5
Green parity before guard-present correction: 26/26 near_parity_green
guard parity: 36/36 guard_pass
score output contract findings: operational 0, ledger 0, Hynix 0
high-confidence rows missing component claim mapping: operational 0, ledger 0, Hynix 0
```

`raw_points/max_points/support_claim_ids` 형태의 contribution row까지 추가한 최신 v6 전체 replay도 통과했다.

```text
operational output_root: /tmp/e2r_v12_parity_after_score_contribution_rows_v6/2020-01-01_to_2026-05-14
ledger output_root: /tmp/e2r_v12_parity_ledger_after_score_contribution_rows_v6/2020-01-01_to_2026-05-14
parity output_root: /tmp/e2r_goalcheck_parity_after_score_contribution_rows_v6
Green parity before guard-present correction: 26/26 near_parity_green
guard parity: 36/36 guard_pass
score output contract findings: operational 0, ledger 0, Hynix 0
high-confidence rows missing score contribution ledger: operational 0, ledger 0, Hynix 0
SK hynix 2024-04-25 contribution examples: eps_fcf_explosion 20.0/20.0 with 58 claims, earnings_visibility 19.0851/20.0 with 50 claims, bottleneck_pricing 19.0851/20.0 with 29 claims
```

component support claim이 실제 claim ledger 밖의 ID를 가리키는지도 막는 v7 replay를 추가로 확인했다.

```text
operational output_root: /tmp/e2r_v12_parity_after_claim_ledger_link_v7/2020-01-01_to_2026-05-14
ledger output_root: /tmp/e2r_v12_parity_ledger_after_claim_ledger_link_v7/2020-01-01_to_2026-05-14
parity output_root: /tmp/e2r_goalcheck_parity_after_claim_ledger_link_v7
operational rows before guard-unverified block: 3827, archetypes: 36, Stage 3-Green: 713
ledger rows: 4191, Stage 3-Green: 1015, Stage 3-Yellow: 11
score output contract findings: operational 0, ledger 0, Hynix 0
high-confidence rows missing claim ledger: operational 0, ledger 0, Hynix 0
high-confidence rows referencing unknown claim ids: operational 0, ledger 0, Hynix 0
Green parity before guard-present correction: 26/26 near_parity_green
guard parity: 36/36 guard_pass
SK hynix 2024-04-25: operational 3-Green / 97.423, ledger 3-Green / 98.173, gap 0.75
SK hynix 2024-04-30 dedicated replay: operational 3-Green / 98.2804, claim ledger IDs 138, unknown contribution refs 0
all-archetype regression: tests.test_runtime_generalization_guards covers every canonical archetype for claim ledger missing/unknown-reference failures
full test suite before guard-present correction: 4034 tests OK
```

사용자 피드백 후 guard primitive가 PRESENT인 경우뿐 아니라 UNKNOWN인 경우도 다시 막았다. 즉 "좋은 증거"가 있어도 `cost_overrun`, `call_off_risk`, `valuation_overheat` 같은 guard 확인이 비어 있으면 총점이 높아도 Green으로 두지 않는다.

```text
operational output_root: /tmp/e2r_goal_operational_guard_unverified_20260621/2020-01-01_to_2026-05-14
ledger output_root: /tmp/e2r_goal_ledger_guard_unverified_20260621/2020-01-01_to_2026-05-14
parity output_root: /tmp/e2r_goalcheck_parity_guard_unverified_20260621
operational rows: 3827, archetypes: 36, Stage 3-Green: 378, Stage 3-Yellow: 335
ledger rows: 4191, archetypes: 36, Stage 3-Green: 551, Stage 3-Yellow: 472
guard-unverified Yellow blocks: operational 335, ledger 335
Green rows missing claim ledger: operational 0, ledger 0
Green rows with orphan score or claim-backed ratio != 100: operational 0, ledger 0
Green rows referencing unknown claim ids: operational 0, ledger 0
Green rows with positive missing, guard present, or guard missing contract findings: operational 0, ledger 0
Previous Green parity before guard_cleared polarity split: 15/26 near_parity_green, 11/26 both_not_green because operational and ledger both blocked to Yellow on guard verification
guard parity: 36/36 guard_pass
raw agent numeric field replay guard: unbacked contract_duration/capa/asp numeric fields produce the same 0.0 score as baseline
raw agent text route guard: unbacked HBM agent field names no longer change archetype routing text
source-backed Green context orphan guard: source-backed/Green-gate rows with orphan score contributions are score_valid=false before Stage promotion
source-backed guard-unverified guard: Green requires guard_missing=0; example C11 call_off_risk UNKNOWN is Stage 3-Yellow, not Stage 3-Green
score pending rows from unresolved as-of web score: operational 70 Stage0, ledger 74 Stage0
remaining orphan score rows remain only in Stage0/Stage1 low-confidence rows; Stage2+/Green orphan rows 0
previous full test suite before guard_cleared polarity split: 4054 tests OK
latest full test suite after guard_cleared polarity split and all guard-bearing archetype regression: 4058 tests OK
```

쉬운 예:

```text
이전 보장: 점수 row에 support_claim_ids가 있어야 한다.
추가 보장: 그 support_claim_ids가 실제 claim ledger 안에 존재해야 한다.

즉 "CLM-FAKE" 같은 ID를 component에 붙여 점수를 통과시키면
valid_high_confidence_score_contribution_claim_ids_unknown 위반으로 잡힌다.
```

## 검증 명령

SK하이닉스 2024-04-30 단건:

```bash
PYTHONPATH=src python -m e2r.cli.run_asof_research_replay \
  --start-date 2024-04-30 \
  --end-date 2024-04-30 \
  --frequency daily \
  --output-directory /tmp/e2r_single_hynix_20240430_components \
  --official-root data/historical_official \
  --search-snapshot-root /tmp/e2r_v12_backfilled_snapshots/search \
  --report-snapshot-root /tmp/e2r_v12_backfilled_snapshots/reports \
  --max-results-per-query 100 \
  --fixture-search \
  --allow-snapshot-derived-universe \
  --no-theme-evidence-review
```

전체 준비 fixture parity:

```bash
PYTHONPATH=src python -m e2r.cli.run_asof_research_replay \
  --start-date 2020-01-01 \
  --end-date 2026-05-14 \
  --frequency monthly \
  --extra-replay-dates-file docs/0619/v12_runtime_replay_fixture_spec_2026-06-19.json \
  --output-directory /tmp/e2r_v12_parity_after_claim_gate_v3 \
  --official-root data/historical_official \
  --search-snapshot-root /tmp/e2r_v12_backfilled_snapshots/search \
  --report-snapshot-root /tmp/e2r_v12_backfilled_snapshots/reports \
  --max-results-per-query 100 \
  --fixture-search \
  --allow-snapshot-derived-universe \
  --no-theme-evidence-review
```

전체 테스트:

```bash
PYTHONPATH=src python -m unittest discover -s tests -q
git diff --check
```
