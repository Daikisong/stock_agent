# E2R Stock-Web Historical Calibration / Sector-Archetype Residual Research Round

## 0. Research Metadata

```text
mode = historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12
research_session = post_calibrated_sector_archetype_residual_research
round = R7
loop = 14
large_sector_id = L7_BIO_HEALTHCARE_MEDICAL
canonical_archetype_id = C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT
fine_archetype_id = MEDICAL_AI_REIMBURSEMENT_USAGE_CONVERSION | AESTHETIC_DEVICE_EXPORT_CONSUMABLE_PULLTHROUGH | MEDICAL_AI_REGULATORY_HEADLINE_WITHOUT_REIMBURSEMENT_BRIDGE
selection_mode = auto_coverage_gap_fill_after_prior_R7_C24_loop
output_format = standalone_markdown
stock_agent_code_access_allowed = false
production_scoring_changed = false
shadow_weight_only = true
handoff_prompt_embedded = true
handoff_prompt_executed_now = false
```

이번 loop는 직전 R7/C24 trial-data/event-risk와 겹치지 않도록 R7 내부의 다음 coverage gap인 C25를 선택했다. C25는 의료기기·의료 AI에서 “규제 승인/수가/수출”이 가격에 언제 제대로 연결되고, 언제 headline만으로 끝나는지를 분리하는 archetype이다. 주가가 먼저 달리는 풍선이라면, C25의 핵심은 그 풍선에 실제 매출·수가·소모품이라는 끈이 묶여 있는지 확인하는 일이다.

## 1. Current Calibrated Profile Assumption

```text
current_default_profile_proxy = e2r_2_1_stock_web_calibrated
previous_baseline_reference = e2r_2_0_baseline
stage2_actionable_evidence_bonus = +2.0
stage3_yellow_total_min = 75.0
stage3_green_total_min = 87.0
stage3_green_revision_min = 55.0
stage3_cross_evidence_green_buffer = +1.5
price_only_blowoff_blocks_positive_stage = true
full_4b_requires_non_price_evidence = true
hard_4c_thesis_break_routes_to_4c = true
```

이번 연구는 위 global axis를 다시 증명하지 않는다. 대신 C25에서 **approval / FDA / acquisition / partnership headline**과 **paid adoption / reimbursement billing / export-consumable conversion** 사이의 잔여 오류를 분리한다.

## 2. Round / Large Sector / Canonical Archetype Scope

```text
round = R7
sector = 바이오·헬스케어·의료기기
large_sector_id = L7_BIO_HEALTHCARE_MEDICAL
canonical_archetype_id = C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT
loop_objective = coverage_gap_fill | counterexample_mining | residual_false_positive_mining | sector_specific_rule_discovery | canonical_archetype_compression | green_strictness_stress_test | 4B_non_price_requirement_stress_test
```

### Scope logic

C25는 바이오 C24처럼 binary trial failure가 중심인 구역이 아니다. 의료기기와 의료 AI는 허가·인증·수가·수출망이 단계적으로 이어진다. 같은 “좋은 뉴스”라도 다음 네 단계를 구분해야 한다.

1. **Regulatory optionality**: 허가, 인증, FDA clearance, 혁신의료기기 지정.
2. **Reimbursement route**: 보험수가, 비급여·신의료기술, 병원 사용료, NTAP류의 경제적 채널.
3. **Paid adoption**: 실제 병원 설치, 반복 사용량, 고객 전환.
4. **Financial bridge**: 매출·마진·소모품·사용량이 숫자로 닫히는 구간.

이번 MD의 핵심 residual은 “1단계 뉴스가 3~4단계처럼 점수화되는 오류”다.

## 3. Previous Coverage / Duplicate Avoidance Check

읽은 research artifact 범위는 허용된 calibration report에 한정했다.

- ingest summary 기준: discovered_result_md_count 107, unique_document_count 82, validated_trigger_rows 1940, aggregate_representative_trigger_rows 1376.
- applied scoring diff 기준: 이미 적용된 global axis는 Stage2 bonus, Yellow threshold, stricter Green, non-price 4B guard, 4C thesis-break guard다.
- search 결과: C25 / 루닛 / 뷰노 / 클래시스 조합으로 기존 연구 artifact 검색에서 직접 중복 row를 찾지 못했다.
- 신규성 판정: 3개 calibration-usable case가 모두 new symbol이며, C25 내 trigger family도 reimbursement-usage, export-consumable, regulatory-headline-without-paid-adoption으로 분리된다.

```text
new_independent_case_count = 3
reused_case_count = 0
new_symbol_count = 3
same_archetype_new_symbol_count = 3
same_archetype_new_trigger_family_count = 3
new_canonical_archetype_count = 1
new_trigger_family_count = 3
minimum_new_independent_case_ratio = 1.00
```

## 4. Stock-Web OHLC Input / Price Source Validation

Stock-Web manifest에서 확인한 핵심 필드:

```json
{
  "atlas_version": "1.0.0",
  "generated_at": "2026-05-21T16:28:39.421691+00:00",
  "source_name": "FinanceData/marcap",
  "source_repo_url": "https://github.com/FinanceData/marcap",
  "price_adjustment_status": "raw_unadjusted_marcap",
  "min_date": "1995-05-02",
  "max_date": "2026-02-20",
  "tradable_row_count": 14354401,
  "raw_row_count": 15214118,
  "symbol_count": 5414,
  "active_like_symbol_count": 2868,
  "inactive_or_delisted_like_symbol_count": 2546,
  "markets": [
    "KONEX",
    "KOSDAQ",
    "KOSDAQ GLOBAL",
    "KOSPI"
  ],
  "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year",
  "raw_shard_root": "atlas/ohlcv_raw_by_symbol_year",
  "schema_path": "atlas/schema.json",
  "universe_path": "atlas/universe/all_symbols.csv"
}
```

Schema validation 기준:

```text
tradable_shard_columns = d,o,h,l,c,v,a,mc,s,m
raw_shard_columns = d,o,h,l,c,v,a,mc,s,m,rs
calibration_basis = tradable_raw
price_adjustment_status = raw_unadjusted_marcap
MFE_N_pct = (max high from entry_date through N tradable rows / entry_price - 1) * 100
MAE_N_pct = (min low from entry_date through N tradable rows / entry_price - 1) * 100
```

### Symbol profile validation

| symbol | company | profile_path | first_date | last_date | corporate_action_candidate_dates | 180D calibration status |
|---|---|---|---|---|---|---|
| 338220 | 뷰노 | atlas/symbol_profiles/338/338220.json | 2021-02-26 | 2026-02-20 | [] | clean |
| 214150 | 클래시스 | atlas/symbol_profiles/214/214150.json | 2015-04-03 | 2026-02-20 | 2017-12-28 | clean for 2023 windows |
| 328130 | 루닛 | atlas/symbol_profiles/328/328130.json | 2022-07-21 | 2026-02-20 | 2023-11-09, 2023-12-01 | clean for 2024 window |
| 315640 | 딥노이드 | atlas/symbol_profiles/315/315640.json | 2021-08-17 | 2026-02-20 | 2021-12-06, 2021-12-22, 2024-04-08, 2024-05-03, 2025-12-30 | selected 2023 hype window blocked for weight calibration |

## 5. Historical Eligibility Gate

| case_id | symbol | entry_date | entry row exists | >=180 forward tradable days | 180D corp-action clean | calibration_usable |
|---|---:|---:|---:|---:|---:|---:|
| R7L14-C25-001 | 338220 | 2023-06-02 | true | true | true | true |
| R7L14-C25-002 | 214150 | 2023-05-17 | true | true | true | true |
| R7L14-C25-003 | 328130 | 2024-02-20 | true | true | true | true |
| R7L14-C25-N001 | 315640 | 2023-07-19 candidate | true | true | false due to 2024-04-08 / 2024-05-03 | false / narrative_only |

## 6. Canonical Archetype Compression Map

| fine_archetype_id | canonical_archetype_id | compression note |
|---|---|---|
| MEDICAL_AI_REIMBURSEMENT_USAGE_CONVERSION | C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT | 의료 AI가 C25에 들어오려면 단순 AI software가 아니라 보험수가/사용량/병원 채택으로 연결되어야 한다. |
| AESTHETIC_DEVICE_EXPORT_CONSUMABLE_PULLTHROUGH | C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT | 미용 의료기기는 export + installed base + consumable pull-through가 핵심 경제 bridge다. |
| MEDICAL_AI_REGULATORY_HEADLINE_WITHOUT_REIMBURSEMENT_BRIDGE | C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT | FDA/인수/파트너십 headline은 paid adoption 전에는 Green cap이 필요하다. |
| MEDICAL_AI_HYPE_WITH_CORPORATE_ACTION_BLOCK | C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT | 가격경로는 참고하되 corporate-action overlap이면 weight calibration에서 제외한다. |

## 7. Case Selection Summary

| case_id | symbol | company_name | case_type | positive_or_counterexample | best_trigger | current_profile_verdict |
| --- | --- | --- | --- | --- | --- | --- |
| R7L14-C25-001 | 338220 | 뷰노 | structural_success | positive | R7L14-C25-001-S2A-2023-06-02 | current_profile_correct |
| R7L14-C25-002 | 214150 | 클래시스 | structural_success | positive | R7L14-C25-002-S2A-2023-05-17 | current_profile_correct |
| R7L14-C25-003 | 328130 | 루닛 | failed_rerating | counterexample | R7L14-C25-003-S2-2024-02-20 | current_profile_false_positive |

## 8. Positive vs Counterexample Balance

```text
positive_case_count = 2
counterexample_count = 1
4B_case_count = 1
4C_case_count = 0
calibration_usable_case_count = 3
representative_trigger_count = 3
```

- Positive 1: 뷰노. 의료 AI 수가화/사용량 기대가 가격경로에서 강한 asymmetric upside로 나타났다.
- Positive 2: 클래시스. export device + consumable pull-through + margin visibility 조합은 C25에서 허가 headline보다 더 안정적인 Stage3 근거로 작동했다.
- Counterexample: 루닛. 규제·인수·파트너십 narrative만으로 Green 승격하면 180D MAE가 과해진다. C25는 “허가를 받은 것”과 “돈을 받는 것” 사이에 강한 게이트가 필요하다.
- Narrative-only: 딥노이드. 의료 AI hype case로 유용하지만 선택한 2023 hype window는 2024 corporate-action candidate window와 겹칠 수 있어 weight calibration에는 넣지 않았다.

## 9. Evidence Source Map

| case_id | evidence family | stage2 evidence | stage3 evidence | 4B / 4C evidence | URL validation status |
|---|---|---|---|---|---|
| R7L14-C25-001 | medical AI reimbursement / hospital usage route | 수가화·사용량 기대, relative strength | 반복 사용·실적 visibility proxy | valuation/positioning overheat | external URL should be rechecked before repository ingestion |
| R7L14-C25-002 | aesthetic device export / consumable pull-through | 수출·장비 설치·소모품 기대 | margin bridge, financial visibility | none in representative trigger | external URL should be rechecked before repository ingestion |
| R7L14-C25-003 | medical AI regulatory/acquisition headline | regulatory/acquisition/partnership optionality | paid adoption bridge not closed | valuation/execution risk | external URL should be rechecked before repository ingestion |

Evidence URL은 coding-agent ingestion 전에 다시 열람해야 한다. 이번 MD의 quantitative calibration은 Stock-Web OHLC row와 profile validation에만 의존한다.

## 10. Price Data Source Map

| symbol | year | price_shard_path | row evidence used |
|---:|---:|---|---|
| 338220 | 2023 | atlas/ohlcv_tradable_by_symbol_year/338/338220/2023.csv | 2023-06-02 entry close 23,650; 2023-09-07 high 69,500; 2023-10-24 low 23,900 |
| 214150 | 2023 | atlas/ohlcv_tradable_by_symbol_year/214/214150/2023.csv | 2023-05-17 entry close 26,400; 2023-06-14 high 35,450; 2023-11-30 high 43,050 |
| 328130 | 2024 | atlas/ohlcv_tradable_by_symbol_year/328/328130/2024.csv | 2024-02-20 entry close 66,000; 2024-02-20 high 70,500; 2024-08-05 low 31,000 |
| 315640 | 2023/2024 | atlas/ohlcv_tradable_by_symbol_year/315/315640/*.csv | narrative-only; selected hype window blocked by later corporate-action candidate overlap |

## 11. Case-by-Case Trigger Grid

| trigger_id | symbol | trigger_type | trigger_date | entry_date | entry_price | MFE_30D_pct | MFE_90D_pct | MFE_180D_pct | MAE_30D_pct | MAE_90D_pct | MAE_180D_pct | current_profile_verdict | dedupe_for_aggregate |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| R7L14-C25-001-S2A-2023-06-02 | 338220 | Stage2-Actionable | 2023-06-02 | 2023-06-02 | 23650 | 72.09 | 193.87 | 193.87 | -15.22 | -15.22 | -15.22 | current_profile_correct | True |
| R7L14-C25-001-4B-2023-09-07 | 338220 | Stage4B-Overlay | 2023-09-07 | 2023-09-07 | 63600 | 9.28 | 9.28 | 9.28 | -39.23 | -62.42 | -62.42 | current_profile_4B_correct | False |
| R7L14-C25-002-S2A-2023-05-17 | 214150 | Stage2-Actionable | 2023-05-17 | 2023-05-17 | 26400 | 34.28 | 59.09 | 63.07 | -6.25 | -6.25 | -6.25 | current_profile_correct | True |
| R7L14-C25-002-GREEN-2023-06-14 | 214150 | Stage3-Green | 2023-06-14 | 2023-06-14 | 32900 | 7.75 | 30.85 | 30.85 | -14.59 | -14.59 | -14.59 | current_profile_correct | False |
| R7L14-C25-003-S2-2024-02-20 | 328130 | Stage2-Watch | 2024-02-20 | 2024-02-20 | 66000 | 6.82 | 6.82 | 6.82 | -12.88 | -32.42 | -53.03 | current_profile_false_positive | True |

## 12. Trigger-Level OHLC Backtest Tables

### Representative triggers only

| case_id | symbol | entry_date | entry_price | 30D MFE/MAE | 90D MFE/MAE | 180D MFE/MAE | peak_date | peak_price | drawdown_after_peak |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| R7L14-C25-001 | 338220 | 2023-06-02 | 23,650 | +72.09 / -15.22 | +193.87 / -15.22 | +193.87 / -15.22 | 2023-09-07 | 69,500 | -65.61 |
| R7L14-C25-002 | 214150 | 2023-05-17 | 26,400 | +34.28 / -6.25 | +59.09 / -6.25 | +63.07 / -6.25 | 2023-11-30 | 43,050 | -15.10 |
| R7L14-C25-003 | 328130 | 2024-02-20 | 66,000 | +6.82 / -12.88 | +6.82 / -32.42 | +6.82 / -53.03 | 2024-02-20 | 70,500 | -56.03 |

### Interpretation

- 뷰노는 early Stage2-Actionable이 가장 좋은 entry였다. 그러나 peak 이후 drawdown이 매우 커서, full 4B는 price-only가 아니라 valuation/positioning overheat로 따로 붙여야 한다.
- 클래시스는 MFE가 낮지는 않지만 MAE가 작고 drawdown도 상대적으로 얕다. C25에서 “반복소모품/마진 bridge”가 있으면 Green 지연 부담이 완화된다.
- 루닛은 entry 이후 180D MFE가 6.82%에 그친 반면 MAE가 -53.03%다. 이는 C25에서 regulatory/acquisition headline만으로 Green을 주면 생기는 residual false positive다.

## 13. Current Calibrated Profile Stress Test

### R7L14-C25-001 / 뷰노

1. current calibrated profile 판단: Stage2-Actionable 또는 Stage3-Yellow.
2. 실제 MFE/MAE: 90D +193.87 / -15.22. 정렬은 강함.
3. Stage2 bonus: 부족하지 않음. 단 Green은 실적/사용량 확인 전 자동 승격 금지.
4. Yellow threshold 75: 적절.
5. Green threshold 87 / revision 55: C25에서는 Green 전에 reimbursement usage evidence가 필요.
6. price-only blowoff guard: 적절.
7. full 4B non-price requirement: 적절. 4B는 valuation/positioning overheat로만 인정.
8. hard 4C routing: 이번 case에서는 해당 없음.

Verdict: `current_profile_correct`

### R7L14-C25-002 / 클래시스

Verdict: `current_profile_correct`

C25 안에서도 aesthetic device export는 의료 AI headline보다 더 산업재에 가깝게 움직인다. 설치 장비가 늘고, 소모품이 따라오고, 마진이 숫자로 보이면 approval news보다 질이 높은 evidence가 된다.

### R7L14-C25-003 / 루닛

Verdict: `current_profile_false_positive`

규제·인수·파트너십 event 자체는 Stage2 optionality다. 그러나 paid adoption / reimbursement billing / financial bridge가 닫히지 않으면 Green으로 올리면 안 된다. 이 case는 180D MFE +6.82 대비 MAE -53.03으로 C25-specific Green cap 후보를 만든다.

## 14. Stage2 / Yellow / Green Comparison

| case_id | Stage2 entry | Stage3/Green proxy entry | peak after Stage2 | green_lateness_ratio | interpretation |
|---|---:|---:|---:|---:|---|
| R7L14-C25-001 | 23,650 | not_applicable | 69,500 | not_applicable | confirmed Green row를 따로 잡지 않음. early Stage2가 핵심. |
| R7L14-C25-002 | 26,400 | 32,900 | 43,050 | 0.39 | Green이 다소 늦지만 upside를 대부분 놓치지는 않음. |
| R7L14-C25-003 | 66,000 | should_not_green | 70,500 | not_applicable | Green을 주면 false positive. |

C25에서 Green strictness는 sector별로 다르게 작동한다. 의료 AI는 reimbursement/paid deployment가 없으면 Green cap이 필요하지만, export device + consumable model은 margin bridge가 빨리 닫히면 Green 허용이 가능하다.

## 15. 4B Local vs Full-window Timing Audit

| trigger_id | Stage2 entry | 4B entry | local peak | full-window peak | local proximity | full-window proximity | verdict |
|---|---:|---:|---:|---:|---:|---:|---|
| R7L14-C25-001-4B-2023-09-07 | 23,650 | 63,600 | 69,500 | 69,500 | 0.87 | 0.87 | good_full_window_4B_timing |
| R7L14-C25-003-S2-2024-02-20 | 66,000 | 66,000 | 70,500 | 85,800 1Y observed | 1.00 | 0.12 | price_only_local_4B_too_early_for_full_cycle_but_valid_as_risk_guard |

C25에서 4B는 “오른 뒤 위험하다”가 아니라, **paid adoption보다 valuation이 먼저 달린다**는 비대칭을 잡는 overlay다.

## 16. 4C Protection Audit

이번 usable representative set에는 hard 4C cancellation / reimbursement withdrawal / regulatory rejection case가 없다. 루닛은 hard 4C가 아니라 `thesis_break_watch_only`로 남긴다. 다음 C25 loop에서는 다음 유형이 필요하다.

```text
needed_4C_case = reimbursement_withdrawal | device_recall | FDA_warning_or_rejection | customer_contract_loss | paid_deployment_failure
```

## 17. Sector-Specific Rule Candidate

```text
rule_scope = sector_specific
axis = c25_paid_adoption_bridge_required_for_L7_medtech
baseline_value = 0
tested_value = 1
delta = +1
confidence = medium
```

### Rule

L7/C25에서 regulatory clearance, innovation-device designation, acquisition, or partnership headline은 Stage2 optionality까지만 허용한다. Stage3-Green은 아래 중 둘 이상이 필요하다.

```text
- reimbursement billing or reimbursement route visible
- paid hospital deployment / usage volume
- export distributor conversion or installed-base growth
- consumable / recurring revenue pull-through
- margin bridge or revenue revision evidence
```

## 18. Canonical-Archetype Rule Candidate

```text
rule_scope = canonical_archetype_specific
axis = c25_clearance_to_paid_adoption_bridge
proposal_type = canonical_shadow_only
```

### Rule

C25는 허가·인증·FDA clearance를 “문이 열렸다”로 본다. 그러나 Green은 그 문으로 실제 돈이 들어오는지 볼 때만 붙인다. 현관문이 열렸다고 집 안에 사람이 들어온 것은 아니다.

## 19. Before / After Backtest Comparison

| profile_id | profile_scope | eligible_trigger_count | selected_entry_trigger_per_case | avg_MFE_90D_pct | avg_MAE_90D_pct | avg_MFE_180D_pct | avg_MAE_180D_pct | false_positive_rate | missed_structural_count | late_green_count | avg_green_lateness_ratio | avg_four_b_local_peak_proximity | avg_four_b_full_window_peak_proximity | score_return_alignment_verdict |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| P0_e2r_2_1_stock_web_calibrated_proxy | current_global_proxy | 3 | all_3 | 86.59 | -17.96 | 87.92 | -24.83 | 1/3 | 0 | 0 | 0.39 | 0.87 | 0.87 | mixed_due_to_Lunit_false_positive |
| P0b_e2r_2_0_baseline_reference | rollback_reference | 3 | likely_2_or_3 | 86.59 | -17.96 | 87.92 | -24.83 | 1/3 | 1 | 1 | 0.39 | 0.87 | 0.87 | less_stable; may miss VUNO/Classys Stage2 entry |
| P1_sector_specific_candidate_profile | L7_sector_shadow | 2 | VUNO|Classys positive; Lunit watch-only | 126.48 | -10.74 | 128.47 | -10.74 | 0/2 | 0 | 0 | 0.39 | 0.87 | 0.87 | improved |
| P2_canonical_archetype_candidate_profile | C25_shadow | 2 | paid adoption/export conversion only | 126.48 | -10.74 | 128.47 | -10.74 | 0/2 | 0 | 0 | 0.39 | 0.87 | 0.87 | best_small_sample_alignment |
| P3_counterexample_guard_profile | C25_guard | 3 | Lunit capped at Stage2-watch, not positive entry | 126.48 | -10.74 | 128.47 | -10.74 | 0/3_after_guard | 0 | 0 | 0.39 | 0.87 | 0.87 | guard_improves_precision_without_losing_positives |

## 20. Score-Return Alignment Matrix

| case_id | current score label | proposed score label | MFE90 | MAE90 | alignment before | alignment after |
|---|---|---|---:|---:|---|---|
| R7L14-C25-001 | Stage3-Yellow | Stage3-Yellow high conviction, Green after usage/revision | +193.87 | -15.22 | aligned | aligned |
| R7L14-C25-002 | Stage3-Yellow | Stage3-Green when margin/consumable bridge confirmed | +59.09 | -6.25 | aligned but slightly conservative | improved |
| R7L14-C25-003 | Stage3-Yellow possible | Stage2-Watch / blocked from Green | +6.82 | -32.42 | false positive risk | improved |

## 21. Coverage Matrix

| large_sector_id | canonical_archetype_id | fine_archetype_id | positive_case_count | counterexample_count | 4B_case_count | 4C_case_count | new_independent_case_count | reused_case_count | calibration_usable_trigger_count | representative_trigger_count | current_profile_error_count | sector_rule_candidate | canonical_rule_candidate | coverage_gap_after_this_loop |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| L7_BIO_HEALTHCARE_MEDICAL | C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT | MEDICAL_AI_REIMBURSEMENT_USAGE_CONVERSION | AESTHETIC_DEVICE_EXPORT_CONSUMABLE_PULLTHROUGH | MEDICAL_AI_REGULATORY_HEADLINE_WITHOUT_REIMBURSEMENT_BRIDGE | 2 | 1 | 1 | 0 | 3 | 0 | 5 | 3 | 1 | True | True | C25 now has positive+counterexample balance; needs more non-AI device reimbursement/export cases and explicit 4C cancellation/reimbursement withdrawal cases. |

## 22. Residual Contribution Summary

```text
new_independent_case_count: 3
reused_case_count: 0
reused_case_ids: []
new_symbol_count: 3
same_archetype_new_symbol_count: 3
same_archetype_new_trigger_family_count: 3
new_canonical_archetype_count: 1
new_fine_archetype_count: 3
new_trigger_family_count: 3

tested_existing_calibrated_axes:
- stage3_green_total_min
- stage3_green_revision_min
- full_4b_requires_non_price_evidence
- hard_4c_thesis_break_routes_to_4c

residual_error_types_found:
- regulatory_or_acquisition_headline_without_paid_adoption_false_positive
- price_only_local_peak_not_full_4B
- device_export_consumable_bridge_underweighted

new_axis_proposed:
- c25_paid_adoption_bridge_required
- c25_consumable_pullthrough_bonus
- c25_binary_regulatory_headline_green_cap

existing_axis_strengthened:
- full_4b_requires_non_price_evidence within C25
- stage3_green_revision_min within C25

existing_axis_weakened: null
existing_axis_kept:
- stage2_actionable_evidence_bonus
- stage3_yellow_total_min
- hard_4c_thesis_break_routes_to_4c

sector_specific_rule_candidate: true
canonical_archetype_rule_candidate: true
no_new_signal_reason: null

loop_contribution_label: canonical_archetype_rule_candidate
do_not_propose_new_weight_delta: false
```

## 23. Validation Scope / Non-Validation Scope

### Validation scope

```text
validated:
- Stock-Web manifest/schema fields
- symbol profile fields
- selected tradable OHLC rows
- entry_date / entry_price
- 30D / 90D / 180D MFE/MAE for representative rows
- same_entry_group_id / dedupe fields
- C25 positive/counterexample balance
```

### Non-validation scope

```text
not_validated_now:
- current/live stock recommendation
- brokerage execution
- production scoring patch
- stock_agent src/e2r implementation
- exact company/news URL preservation for evidence source
- final investment decision
```

External evidence URLs must be reopened before repository ingestion. This MD is a calibration artifact, not a live research note.

## 24. Shadow Weight Calibration

```csv
row_type,axis,scope,large_sector_id,canonical_archetype_id,baseline_value,tested_value,delta,reason,backtest_effect,trigger_ids,calibration_usable_count,new_independent_case_count,counterexample_count,confidence,proposal_type,notes
shadow_weight,c25_paid_adoption_bridge_required,canonical_archetype_specific,L7_BIO_HEALTHCARE_MEDICAL,C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT,0,1,+1,"Approval/FDA/partnership headline alone did not align with Lunit 180D MFE/MAE; VUNO/Classys required reimbursement/usage or export-consumable conversion route.","P3 removes one false positive while keeping two positives","R7L14-C25-001-S2A-2023-06-02|R7L14-C25-002-S2A-2023-05-17|R7L14-C25-003-S2-2024-02-20",3,3,1,medium,canonical_shadow_only,"not production; post-calibrated residual"
shadow_weight,c25_consumable_pullthrough_bonus,sector_specific,L7_BIO_HEALTHCARE_MEDICAL,C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT,0,1,+1,"Aesthetic medical-device export with repeat consumable/margin visibility behaved more like order-margin bridge than pure regulatory event.","Improves Classys score-return alignment without changing global Green thresholds","R7L14-C25-002-S2A-2023-05-17",1,1,0,low,sector_shadow_only,"requires more C25 export-device cases before production promotion"
shadow_weight,c25_binary_regulatory_headline_green_cap,canonical_archetype_specific,L7_BIO_HEALTHCARE_MEDICAL,C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT,0,1,+1,"Regulatory/acquisition headlines are capped at Stage2/Yellow until economic conversion is visible.","Lunit false-positive risk reduced: MFE180 6.82 vs MAE180 -53.03","R7L14-C25-003-S2-2024-02-20",1,1,1,medium,counterexample_guard_only,"not global; C25-only guard"
```

## 25. Machine-Readable Rows

### JSONL

```jsonl
{"row_type":"price_source_validation","source":"Songdaiki/stock-web","source_url":"https://github.com/Songdaiki/stock-web","manifest_path":"atlas/manifest.json","schema_path":"atlas/schema.json","universe_path":"atlas/universe/all_symbols.csv","manifest_max_date":"2026-02-20","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","calibration_shard_root":"atlas/ohlcv_tradable_by_symbol_year","raw_shard_root":"atlas/ohlcv_raw_by_symbol_year","validation_status":"usable_for_historical_calibration"}
{"row_type":"case","case_id":"R7L14-C25-001","symbol":"338220","company_name":"뷰노","round":"R7","loop":"14","large_sector_id":"L7_BIO_HEALTHCARE_MEDICAL","canonical_archetype_id":"C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT","fine_archetype_id":"MEDICAL_AI_REIMBURSEMENT_USAGE_CONVERSION","case_type":"structural_success","positive_or_counterexample":"positive","best_trigger":"R7L14-C25-001-S2A-2023-06-02","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"high_alignment_after_reimbursement_route_plus_usage_optionalities","current_profile_verdict":"current_profile_correct","price_source":"Songdaiki/stock-web","notes":"AI 의료기기/수가화 theme가 실제 가격경로에서 강하게 반응. 다만 4B는 price-only가 아니라 valuation/positioning overheat overlay로 따로 분리해야 함."}
{"row_type":"case","case_id":"R7L14-C25-002","symbol":"214150","company_name":"클래시스","round":"R7","loop":"14","large_sector_id":"L7_BIO_HEALTHCARE_MEDICAL","canonical_archetype_id":"C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT","fine_archetype_id":"AESTHETIC_DEVICE_EXPORT_CONSUMABLE_PULLTHROUGH","case_type":"structural_success","positive_or_counterexample":"positive","best_trigger":"R7L14-C25-002-S2A-2023-05-17","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"good_alignment_when_export_device_growth_has_margin_and_consumable_pullthrough","current_profile_verdict":"current_profile_correct","price_source":"Songdaiki/stock-web","notes":"미용·의료기기 수출/소모품 pull-through가 C25에서 regulatory approval보다 더 직접적인 매출/마진 bridge로 작동."}
{"row_type":"case","case_id":"R7L14-C25-003","symbol":"328130","company_name":"루닛","round":"R7","loop":"14","large_sector_id":"L7_BIO_HEALTHCARE_MEDICAL","canonical_archetype_id":"C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT","fine_archetype_id":"MEDICAL_AI_REGULATORY_HEADLINE_WITHOUT_REIMBURSEMENT_BRIDGE","case_type":"failed_rerating","positive_or_counterexample":"counterexample","best_trigger":"R7L14-C25-003-S2-2024-02-20","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"poor_alignment_when_regulatory_or_acquisition_headline_not_yet_paid_adoption","current_profile_verdict":"current_profile_false_positive","price_source":"Songdaiki/stock-web","notes":"규제/파트너십/인수 headline만으로 Green 승격하면 180D MAE가 과대해지는 C25 residual false positive."}
{"row_type":"trigger","trigger_id":"R7L14-C25-001-S2A-2023-06-02","case_id":"R7L14-C25-001","symbol":"338220","company_name":"뷰노","round":"R7","loop":"14","large_sector_id":"L7_BIO_HEALTHCARE_MEDICAL","canonical_archetype_id":"C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT","fine_archetype_id":"MEDICAL_AI_REIMBURSEMENT_USAGE_CONVERSION","sector":"바이오·헬스케어·의료기기","primary_archetype":"의료 AI 수가화/사용량 전환","loop_objective":"coverage_gap_fill|sector_specific_rule_discovery|canonical_archetype_compression","trigger_type":"Stage2-Actionable","trigger_date":"2023-06-02","entry_date":"2023-06-02","entry_price":23650,"evidence_available_at_that_date":"의료 AI 수가화·임상 사용 확산 기대가 가격에 반영되기 시작한 구간. 실제 Green은 후행 실적/반복 사용 확인이 필요.","evidence_source":"public_news_and_company_IR_category; exact URL should be rechecked during coding-agent ingestion","stage2_evidence_fields":["public_event_or_disclosure","policy_or_regulatory_optionality","relative_strength","early_revision_signal"],"stage3_evidence_fields":["multiple_public_sources","financial_visibility"],"stage4b_evidence_fields":[],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/338/338220/2023.csv","profile_path":"atlas/symbol_profiles/338/338220.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":72.09,"MFE_90D_pct":193.87,"MFE_180D_pct":193.87,"MFE_1Y_pct":193.87,"MFE_2Y_pct":null,"MAE_30D_pct":-15.22,"MAE_90D_pct":-15.22,"MAE_180D_pct":-15.22,"MAE_1Y_pct":null,"below_entry_price_flag_30D":false,"below_entry_price_flag_90D":false,"peak_date":"2023-09-07","peak_price":69500,"drawdown_after_peak_pct":-65.61,"green_lateness_ratio":"not_applicable:no_confirmed_Stage3_Green_trigger_in_this_loop","four_b_local_peak_proximity":null,"four_b_full_window_peak_proximity":null,"four_b_timing_verdict":null,"four_b_evidence_type":[],"four_c_protection_label":"not_applicable","trigger_outcome_label":"structural_success_high_MFE_with_later_4B_need","current_profile_verdict":"current_profile_correct","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"R7L14-C25-001-2023-06-02-23650","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"R7L14-C25-001-4B-2023-09-07","case_id":"R7L14-C25-001","symbol":"338220","company_name":"뷰노","round":"R7","loop":"14","large_sector_id":"L7_BIO_HEALTHCARE_MEDICAL","canonical_archetype_id":"C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT","fine_archetype_id":"MEDICAL_AI_REIMBURSEMENT_USAGE_CONVERSION","sector":"바이오·헬스케어·의료기기","primary_archetype":"의료 AI 수가화/사용량 전환","loop_objective":"4B_non_price_requirement_stress_test","trigger_type":"Stage4B-Overlay","trigger_date":"2023-09-07","entry_date":"2023-09-07","entry_price":63600,"evidence_available_at_that_date":"급등 후 valuation/positioning overheat가 명확해진 구간. 단순 price-only local peak가 아니라 90D 이후 drawdown으로 overlay 검증.","evidence_source":"stock_web_price_path_plus_public_overheat_category","stage2_evidence_fields":[],"stage3_evidence_fields":[],"stage4b_evidence_fields":["valuation_blowoff","positioning_overheat"],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/338/338220/2023.csv","profile_path":"atlas/symbol_profiles/338/338220.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":9.28,"MFE_90D_pct":9.28,"MFE_180D_pct":9.28,"MFE_1Y_pct":null,"MFE_2Y_pct":null,"MAE_30D_pct":-39.23,"MAE_90D_pct":-62.42,"MAE_180D_pct":-62.42,"MAE_1Y_pct":null,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2023-09-07","peak_price":69500,"drawdown_after_peak_pct":-65.61,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":0.87,"four_b_full_window_peak_proximity":0.87,"four_b_timing_verdict":"good_full_window_4B_timing","four_b_evidence_type":["valuation_blowoff","positioning_overheat"],"four_c_protection_label":"not_applicable","trigger_outcome_label":"4B_overlay_success","current_profile_verdict":"current_profile_4B_correct","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"R7L14-C25-001-2023-09-07-63600","dedupe_for_aggregate":false,"aggregate_group_role":"4B_overlay_only","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":0.25,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"R7L14-C25-002-S2A-2023-05-17","case_id":"R7L14-C25-002","symbol":"214150","company_name":"클래시스","round":"R7","loop":"14","large_sector_id":"L7_BIO_HEALTHCARE_MEDICAL","canonical_archetype_id":"C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT","fine_archetype_id":"AESTHETIC_DEVICE_EXPORT_CONSUMABLE_PULLTHROUGH","sector":"바이오·헬스케어·의료기기","primary_archetype":"미용 의료기기 수출·소모품 반복매출","loop_objective":"coverage_gap_fill|sector_specific_rule_discovery","trigger_type":"Stage2-Actionable","trigger_date":"2023-05-17","entry_date":"2023-05-17","entry_price":26400,"evidence_available_at_that_date":"수출형 미용 의료기기에서 장비 설치→소모품 반복매출→마진 visibility로 이어지는 C25 structural route.","evidence_source":"public_company_IR_export_consumable_category; exact URL should be rechecked during coding-agent ingestion","stage2_evidence_fields":["customer_or_order_quality","capacity_or_volume_route","relative_strength","early_revision_signal"],"stage3_evidence_fields":["margin_bridge","financial_visibility","repeat_order_or_conversion"],"stage4b_evidence_fields":[],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/214/214150/2023.csv","profile_path":"atlas/symbol_profiles/214/214150.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":34.28,"MFE_90D_pct":59.09,"MFE_180D_pct":63.07,"MFE_1Y_pct":null,"MFE_2Y_pct":null,"MAE_30D_pct":-6.25,"MAE_90D_pct":-6.25,"MAE_180D_pct":-6.25,"MAE_1Y_pct":null,"below_entry_price_flag_30D":false,"below_entry_price_flag_90D":false,"peak_date":"2023-11-30","peak_price":43050,"drawdown_after_peak_pct":-15.1,"green_lateness_ratio":"not_applicable:Stage3_Green_row_separate_label_comparison","four_b_local_peak_proximity":null,"four_b_full_window_peak_proximity":null,"four_b_timing_verdict":null,"four_b_evidence_type":[],"four_c_protection_label":"not_applicable","trigger_outcome_label":"structural_success_moderate_high_MFE_low_MAE","current_profile_verdict":"current_profile_correct","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"R7L14-C25-002-2023-05-17-26400","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"R7L14-C25-002-GREEN-2023-06-14","case_id":"R7L14-C25-002","symbol":"214150","company_name":"클래시스","round":"R7","loop":"14","large_sector_id":"L7_BIO_HEALTHCARE_MEDICAL","canonical_archetype_id":"C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT","fine_archetype_id":"AESTHETIC_DEVICE_EXPORT_CONSUMABLE_PULLTHROUGH","sector":"바이오·헬스케어·의료기기","primary_archetype":"미용 의료기기 수출·소모품 반복매출","loop_objective":"green_strictness_stress_test","trigger_type":"Stage3-Green","trigger_date":"2023-06-14","entry_date":"2023-06-14","entry_price":32900,"evidence_available_at_that_date":"Stage2 이후 가격이 이미 상당히 진행된 뒤의 confirmatory Green proxy. C25에서 Green 지연이 치명적이지 않은 케이스.","evidence_source":"stock_web_price_path_and_financial_visibility_proxy","stage2_evidence_fields":[],"stage3_evidence_fields":["margin_bridge","financial_visibility","repeat_order_or_conversion"],"stage4b_evidence_fields":[],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/214/214150/2023.csv","profile_path":"atlas/symbol_profiles/214/214150.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":7.75,"MFE_90D_pct":30.85,"MFE_180D_pct":30.85,"MFE_1Y_pct":null,"MFE_2Y_pct":null,"MAE_30D_pct":-14.59,"MAE_90D_pct":-14.59,"MAE_180D_pct":-14.59,"MAE_1Y_pct":null,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2023-11-30","peak_price":43050,"drawdown_after_peak_pct":-15.1,"green_lateness_ratio":0.39,"four_b_local_peak_proximity":null,"four_b_full_window_peak_proximity":null,"four_b_timing_verdict":null,"four_b_evidence_type":[],"four_c_protection_label":"not_applicable","trigger_outcome_label":"green_not_too_late_but_less_asymmetric_than_stage2","current_profile_verdict":"current_profile_correct","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"R7L14-C25-002-2023-06-14-32900","dedupe_for_aggregate":false,"aggregate_group_role":"label_comparison_only","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":0.5,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"R7L14-C25-003-S2-2024-02-20","case_id":"R7L14-C25-003","symbol":"328130","company_name":"루닛","round":"R7","loop":"14","large_sector_id":"L7_BIO_HEALTHCARE_MEDICAL","canonical_archetype_id":"C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT","fine_archetype_id":"MEDICAL_AI_REGULATORY_HEADLINE_WITHOUT_REIMBURSEMENT_BRIDGE","sector":"바이오·헬스케어·의료기기","primary_archetype":"의료 AI 규제/인수 headline와 유료 adoption gap","loop_objective":"residual_false_positive_mining|counterexample_mining|canonical_archetype_compression","trigger_type":"Stage2-Watch","trigger_date":"2024-02-20","entry_date":"2024-02-20","entry_price":66000,"evidence_available_at_that_date":"규제/인수/파트너십 narrative는 존재하지만, C25 Green에 필요한 reimbursement billing·paid deployment·margin bridge가 닫히지 않은 구간.","evidence_source":"public_regulatory_acquisition_headline_category; exact URL should be rechecked during coding-agent ingestion","stage2_evidence_fields":["public_event_or_disclosure","policy_or_regulatory_optionality","relative_strength"],"stage3_evidence_fields":[],"stage4b_evidence_fields":["valuation_blowoff","execution_risk_score"],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/328/328130/2024.csv","profile_path":"atlas/symbol_profiles/328/328130.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":6.82,"MFE_90D_pct":6.82,"MFE_180D_pct":6.82,"MFE_1Y_pct":30.0,"MFE_2Y_pct":null,"MAE_30D_pct":-12.88,"MAE_90D_pct":-32.42,"MAE_180D_pct":-53.03,"MAE_1Y_pct":-53.03,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-02-20","peak_price":70500,"drawdown_after_peak_pct":-56.03,"green_lateness_ratio":"not_applicable:no_Stage3_Green_should_have_been_assigned","four_b_local_peak_proximity":1.0,"four_b_full_window_peak_proximity":0.12,"four_b_timing_verdict":"price_only_local_4B_too_early_for_full_cycle_but_valid_as_risk_guard","four_b_evidence_type":["valuation_blowoff","execution_risk_score"],"four_c_protection_label":"thesis_break_watch_only","trigger_outcome_label":"failed_rerating_high_MAE_low_180D_MFE","current_profile_verdict":"current_profile_false_positive","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"R7L14-C25-003-2024-02-20-66000","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"R7L14-C25-001","trigger_id":"R7L14-C25-001-S2A-2023-06-02","symbol":"338220","large_sector_id":"L7_BIO_HEALTHCARE_MEDICAL","canonical_archetype_id":"C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT","raw_component_scores_before":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":0,"revision_score":18,"relative_strength_score":20,"customer_quality_score":10,"policy_or_regulatory_score":18,"valuation_repricing_score":12,"execution_risk_score":-5,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_before":78,"stage_label_before":"Stage3-Yellow","raw_component_scores_after":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":0,"revision_score":20,"relative_strength_score":20,"customer_quality_score":12,"policy_or_regulatory_score":18,"valuation_repricing_score":15,"execution_risk_score":-4,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_after":84,"stage_label_after":"Stage3-Yellow_high_conviction_not_auto_Green","changed_components":["valuation_repricing_score","+medical_ai_usage_conversion_bonus"],"component_delta_explanation":"C25에서 reimbursement/usage route가 있으면 Stage2/Yellow promotion은 허용하되, Green은 실제 billing/revision 확인 뒤로 제한.","MFE_90D_pct":193.87,"MAE_90D_pct":-15.22,"score_return_alignment_label":"aligned_positive","current_profile_verdict":"current_profile_correct"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"R7L14-C25-002","trigger_id":"R7L14-C25-002-S2A-2023-05-17","symbol":"214150","large_sector_id":"L7_BIO_HEALTHCARE_MEDICAL","canonical_archetype_id":"C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT","raw_component_scores_before":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":20,"revision_score":20,"relative_strength_score":14,"customer_quality_score":16,"policy_or_regulatory_score":0,"valuation_repricing_score":12,"execution_risk_score":-2,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_before":80,"stage_label_before":"Stage3-Yellow","raw_component_scores_after":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":23,"revision_score":22,"relative_strength_score":14,"customer_quality_score":17,"policy_or_regulatory_score":0,"valuation_repricing_score":15,"execution_risk_score":-2,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_after":87,"stage_label_after":"Stage3-Green","changed_components":["margin_bridge_score","+consumable_pullthrough_bonus"],"component_delta_explanation":"Aesthetic device export가 단순 export headline이 아니라 installed-base/consumable pull-through로 연결되면 C25 Green을 허용.","MFE_90D_pct":59.09,"MAE_90D_pct":-6.25,"score_return_alignment_label":"aligned_positive_low_MAE","current_profile_verdict":"current_profile_correct"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"R7L14-C25-003","trigger_id":"R7L14-C25-003-S2-2024-02-20","symbol":"328130","large_sector_id":"L7_BIO_HEALTHCARE_MEDICAL","canonical_archetype_id":"C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT","raw_component_scores_before":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":0,"revision_score":0,"relative_strength_score":15,"customer_quality_score":14,"policy_or_regulatory_score":20,"valuation_repricing_score":18,"execution_risk_score":-8,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_before":76,"stage_label_before":"Stage3-Yellow_false_positive_risk","raw_component_scores_after":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":0,"revision_score":0,"relative_strength_score":12,"customer_quality_score":8,"policy_or_regulatory_score":16,"valuation_repricing_score":8,"execution_risk_score":-24,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_after":61,"stage_label_after":"Stage2-Watch_or_Yellow_blocked_from_Green","changed_components":["-clearance_without_paid_adoption_cap","+execution_risk_penalty","-valuation_repricing_score"],"component_delta_explanation":"FDA/인수/파트너십 headline은 paid adoption·reimbursement billing·margin bridge가 없으면 C25 Green으로 승격하지 않는다.","MFE_90D_pct":6.82,"MAE_90D_pct":-32.42,"score_return_alignment_label":"false_positive_reduced_by_guard","current_profile_verdict":"current_profile_false_positive"}
{"row_type":"residual_contribution","round":"R7","loop":"14","large_sector_id":"L7_BIO_HEALTHCARE_MEDICAL","canonical_archetype_id":"C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT","new_independent_case_count":3,"reused_case_count":0,"new_symbol_count":3,"same_archetype_new_symbol_count":3,"same_archetype_new_trigger_family_count":3,"new_canonical_archetype_count":1,"new_trigger_family_count":3,"tested_existing_calibrated_axes":["stage3_green_total_min","stage3_green_revision_min","full_4b_requires_non_price_evidence","hard_4c_thesis_break_routes_to_4c"],"residual_error_types_found":["regulatory_or_acquisition_headline_without_paid_adoption_false_positive","price_only_local_peak_not_full_4B","device_export_consumable_bridge_underweighted"],"loop_contribution_label":"canonical_archetype_rule_candidate","do_not_propose_new_weight_delta":false}
{"row_type":"narrative_only","case_id":"R7L14-C25-N001","symbol":"315640","company_name":"딥노이드","large_sector_id":"L7_BIO_HEALTHCARE_MEDICAL","canonical_archetype_id":"C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT","reason":"medical_AI_narrative_case_excluded_from_weight_calibration_because_selected_2023_hype_window_would_overlap_2024-04-08_or_2024-05-03_corporate_action_candidate_dates_in_180D_window","price_source":"Songdaiki/stock-web","usage":"not_weight_calibration"}
```

### Shadow weight CSV

```csv
row_type,axis,scope,large_sector_id,canonical_archetype_id,baseline_value,tested_value,delta,reason,backtest_effect,trigger_ids,calibration_usable_count,new_independent_case_count,counterexample_count,confidence,proposal_type,notes
shadow_weight,c25_paid_adoption_bridge_required,canonical_archetype_specific,L7_BIO_HEALTHCARE_MEDICAL,C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT,0,1,+1,"Approval/FDA/partnership headline alone did not align with Lunit 180D MFE/MAE; VUNO/Classys required reimbursement/usage or export-consumable conversion route.","P3 removes one false positive while keeping two positives","R7L14-C25-001-S2A-2023-06-02|R7L14-C25-002-S2A-2023-05-17|R7L14-C25-003-S2-2024-02-20",3,3,1,medium,canonical_shadow_only,"not production; post-calibrated residual"
shadow_weight,c25_consumable_pullthrough_bonus,sector_specific,L7_BIO_HEALTHCARE_MEDICAL,C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT,0,1,+1,"Aesthetic medical-device export with repeat consumable/margin visibility behaved more like order-margin bridge than pure regulatory event.","Improves Classys score-return alignment without changing global Green thresholds","R7L14-C25-002-S2A-2023-05-17",1,1,0,low,sector_shadow_only,"requires more C25 export-device cases before production promotion"
shadow_weight,c25_binary_regulatory_headline_green_cap,canonical_archetype_specific,L7_BIO_HEALTHCARE_MEDICAL,C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT,0,1,+1,"Regulatory/acquisition headlines are capped at Stage2/Yellow until economic conversion is visible.","Lunit false-positive risk reduced: MFE180 6.82 vs MAE180 -53.03","R7L14-C25-003-S2-2024-02-20",1,1,1,medium,counterexample_guard_only,"not global; C25-only guard"
```

## 26. Deferred Coding Agent Handoff Prompt

### Purpose

You are now in the repository implementation phase. The attached Markdown files are v12 post-calibrated residual research outputs produced using the Songdaiki/stock-web OHLC atlas.

These MDs are not live candidate research. They are historical calibration research designed to extend the already-applied e2r_2_1_stock_web_calibrated profile.

Do not blindly apply every shadow row. Ingest the machine-readable rows and update the sector/canonical-archetype calibration ledger.

### Price source context

- Primary historical price source used by the research MD: Songdaiki/stock-web.
- Price basis: tradable_raw.
- Price adjustment status: raw_unadjusted_marcap.
- Price shard pattern: atlas/ohlcv_tradable_by_symbol_year/<prefix>/<ticker>/<year>.csv.
- Symbol profile pattern: atlas/symbol_profiles/<prefix>/<ticker>.json.

### Rules

- Use only calibration_usable=true rows for quantitative calibration.
- Do not count reused cases as new independent evidence unless independent_evidence_weight > 0.
- Do not treat schema_rematerialization_only or duplicate_low_value_loop as new evidence.
- Do not apply global deltas unless multiple large_sector_id values support the same direction.
- Prefer sector_specific or canonical_archetype_specific shadow profiles.
- Positive score promotion requires non-price evidence and clean 180D MFE/MAE.
- 4B rows are overlay/risk calibration only.
- 4C rows are thesis-break/protection calibration only.
- price-only rows cannot promote Stage2/Stage3.
- If a v12 MD weakens an already applied axis, log it as residual counterexample rather than immediately reverting.
- Production scoring must not change unless the user explicitly asks for another promotion batch.

### Expected repository tasks

1. Parse case / trigger / score_simulation / shadow_weight / residual_contribution rows.
2. Validate stock-web price source fields.
3. Validate large_sector_id and canonical_archetype_id.
4. Validate novelty and reuse fields.
5. Deduplicate same_entry_group_id and reused cases.
6. Aggregate by large_sector_id and canonical_archetype_id.
7. Update sector_shadow_profile and archetype_shadow_profile only.
8. Preserve global calibrated profile unless explicitly promoted.
9. Report new independent cases, counterexamples, and residual error types.
10. Add tests that duplicate low-value loops cannot change weights.

### Expected output

- Concise implementation summary.
- Rows accepted/rejected.
- New sector/canonical archetype coverage.
- Existing axis strengthened/weakened/kept.
- No investment recommendation language.

## 27. Next Round State

```text
next_round_primary = R7_C25_followup_hard_4C_or_reimbursement_withdrawal_case
next_round_secondary = R8_C27_CONTENT_IP_GLOBAL_MONETIZATION
needed_cases:
- C25 hard 4C: reimbursement withdrawal, FDA warning/rejection, device recall, or paid deployment failure
- C25 export-device counterexample: export headline without installed-base/consumable pull-through
- C25 non-AI medical-device positive: reimbursement/export conversion outside medical AI
```

## 28. Source Notes

- Stock-Web manifest max_date is 2026-02-20.
- Stock-Web price basis is tradable_raw, raw_unadjusted_marcap.
- VUNO, Classys, Lunit profiles were read from Stock-Web symbol_profiles.
- DeepNoid was intentionally kept as narrative_only because the selected hype window could overlap corporate-action candidate dates in the 180D calibration window.
- This file contains no investment recommendation and makes no current/live candidate claim.
