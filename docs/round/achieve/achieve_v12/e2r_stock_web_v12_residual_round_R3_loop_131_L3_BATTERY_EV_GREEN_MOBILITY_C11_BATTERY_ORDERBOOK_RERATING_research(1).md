# E2R Stock-Web v12 Residual Research — R3 loop 131 — L3 / C11_BATTERY_ORDERBOOK_RERATING

```text
mode = historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12
research_session = post_calibrated_sector_archetype_residual_research
selected_round = R3
selected_loop = 131
selection_basis = docs/core/V12_Research_No_Repeat_Index.md
selected_priority_bucket = Priority 0
round_schedule_status = coverage_index_selected_not_sequential
round_sector_consistency = pass
large_sector_id = L3_BATTERY_EV_GREEN_MOBILITY
canonical_archetype_id = C11_BATTERY_ORDERBOOK_RERATING
fine_archetype_id = mixed_c11_orderbook_to_revenue_margin_conversion_leaf_set
output_filename = e2r_stock_web_v12_residual_round_R3_loop_131_L3_BATTERY_EV_GREEN_MOBILITY_C11_BATTERY_ORDERBOOK_RERATING_research.md
production_scoring_changed = false
shadow_weight_only = true
stock_agent_code_patch_allowed = false
current_stock_discovery_allowed = false
```

## 0. Execution interpretation

이번 MD는 `Songdaiki/stock-web`의 실제 1D OHLCV row를 사용해 C11_BATTERY_ORDERBOOK_RERATING의 잔여 오류를 보강하는 standalone calibration artifact다. 이번 실행은 현재 종목 추천, live watchlist, 자동매매, stock_agent 코드 패치가 아니다. 연구 단위는 R3 순환이 아니라 No-Repeat Index의 coverage gap이며, R3/L3는 C11 선택 뒤 따라오는 metadata다.

## 1. No-Repeat / coverage selection

No-Repeat Index 기준 C11은 Priority 0 구역이다. 직전 세션 산출물에서 C02, C09, C14, C10, C06, C07을 이미 보강했으므로, 같은 symbol/date/trigger 재사용을 피하고 C11의 신규 심볼·신규 trigger family로 이동했다.

```text
coverage_before = C11 rows 18
minimum_stability_target = 30 rows
need_to_30_before = 12
need_to_50_before = 32
coverage_after_if_accepted = 23
need_to_30_after_if_accepted = 7
need_to_50_after_if_accepted = 27
```

Novelty check:

```text
new_independent_case_count = 5
reused_case_count = 0
same_archetype_new_symbol_count = 5
same_archetype_new_trigger_family_count = 5
hard_duplicate_key_reuse = 0
```

## 2. Price source validation

```text
price_source = Songdaiki/stock-web
price_data_repo = https://github.com/Songdaiki/stock-web
price_basis = tradable_raw
price_adjustment_status = raw_unadjusted_marcap
stock_web_manifest_max_date = 2026-02-20
calibration_shard_root = atlas/ohlcv_tradable_by_symbol_year
profile_root = atlas/symbol_profiles
```

MFE/MAE formula:

```text
MFE_N_pct = (max(high from entry_date through N trading days) / entry_price - 1) * 100
MAE_N_pct = (min(low from entry_date through N trading days) / entry_price - 1) * 100
N = 30D, 90D, 180D trading rows
```

All 5 representative trigger rows have the six mandatory canonical price fields: `MFE_30D_pct`, `MFE_90D_pct`, `MFE_180D_pct`, `MAE_30D_pct`, `MAE_90D_pct`, `MAE_180D_pct`.

## 3. Archetype hypothesis

C11_BATTERY_ORDERBOOK_RERATING should not treat every “수주잔고 증가” as the same signal. Battery equipment backlog is a reservoir; the rerating only happens when the reservoir has a pipe into revenue recognition and margin conversion. If the pipe is blocked by delayed customer projects, uncertain backlog quality, EV demand slowdown, or capex deferral, the same large backlog number can become a trap.

Working rule:

```text
C11 positive = named customer/order quality + backlog/delivery visibility + revenue/margin/revision bridge
C11 false positive = nominal backlog only + uncertain customer/delay + no margin bridge + EV chasm context
C11 4B watch = backlog headline coexists with explicit capex slowdown, contract delay, or high-MAE path
```

## 4. Case universe summary

| symbol | company | case_role | trigger_type | trigger_date | entry_date | entry_price | MFE_30D | MAE_30D | MFE_90D | MAE_90D | MFE_180D | MAE_180D | current_profile_verdict |
|---|---|---|---|---|---|---:|---:|---:|---:|---:|---:|---:|---|
| 282880 | 코윈테크 | structural_success | Stage2-Actionable | 2023-02-22 | 2023-02-22 | 25100 | 37.85 | -4.38 | 67.33 | -4.38 | 87.25 | -4.38 | current_profile_correct |
| 372170 | 윤성에프앤씨 | structural_success | Stage2-Actionable | 2022-12-16 | 2022-12-19 | 45100 | 20.62 | -10.75 | 307.98 | -10.75 | 495.34 | -10.75 | current_profile_correct |
| 217820 | 원익피앤이 | failed_rerating | Stage2-Actionable | 2023-10-20 | 2023-10-23 | 6880 | 13.37 | -12.50 | 13.37 | -21.22 | 13.37 | -42.15 | current_profile_false_positive |
| 299030 | 하나기술 | failed_rerating | Stage2-Actionable | 2024-03-04 | 2024-03-05 | 60200 | 21.43 | -16.94 | 21.43 | -43.94 | 21.43 | -69.27 | current_profile_false_positive |
| 277880 | 티에스아이 | 4B_overlay_success | Stage4B | 2024-05-28 | 2024-05-29 | 8270 | 3.87 | -11.73 | 3.87 | -34.70 | 3.87 | -46.25 | current_profile_false_positive |

## 5. Evidence map

### 5.1 코윈테크 — structural success

- Evidence date: 2023-02-22 08:01.
- Evidence source: https://dealsite.co.kr/articles/99504/068020
- At-date evidence: 2차전지 자동화 턴키 사업 본궤도, 수주잔고 2022년 말 2500억 수준, Ultium Cells 800억 계약, CAPA 확장과 수익성 개선 논리.
- Entry rule: before market article time, `entry_date = 2023-02-22` close.
- Result: 180D MFE +87.25%, 180D MAE -4.38%.

### 5.2 윤성에프앤씨 — structural success

- Evidence date: 2022-12-16.
- Evidence source: https://ssl.pstatic.net/imgstock/upload/research/company/1671150716387.pdf
- At-date evidence: SK온 북미 공장 31개 라인, 최소 3000억 이상 수주 가능성, 1H22 수주잔고 2372억에서 연말 4000억 이상 가능성, lead time 1~1.5년, 2023년 매출/OP 성장 전망.
- Entry rule: report date, conservative next trading day close, `entry_date = 2022-12-19`.
- Result: 180D MFE +495.34%, 180D MAE -10.75%.

### 5.3 원익피앤이 — false positive / margin quality fail

- Evidence date: 2023-10-20.
- Evidence source: https://www.hanaw.com/download/research/FileServer/WEB/info/small_cap/2023/10/20/231023_wonikpne.pdf
- At-date evidence: 신규수주 5000억 이상 기대, 수주잔고 1H23 6580억, 최근 7000억 이상 추정, 2024년 성장 전망.
- Failure mechanism: backlog number was large, but price path did not confirm conversion. Entry day high became the 180D high and 180D MAE reached -42.15%.
- Rule implication: nominal backlog without margin/revenue-quality bridge should be Stage2-Watch, not Stage2-Actionable.

### 5.4 하나기술 — false positive / backlog quality delay

- Evidence date: 2024-03-04.
- Evidence source: https://ssl.pstatic.net/imgstock/upload/research/company/1709507639094.pdf
- At-date evidence: 2023년 말 수주잔고 3872억, but Britishvolt향 1198억 uncertainty, 아시아 고객 1724억 2025년 지연, 본격 성장/수익성 개선은 2025년부터.
- Failure mechanism: nominal backlog existed, but backlog quality and timing were explicitly discounted. 30D MFE +21.43% was short-lived; 180D MAE reached -69.27%.
- Rule implication: delayed or uncertain customer backlog should apply a C11-specific actionability penalty.

### 5.5 티에스아이 — 4B overlay success / EV chasm context

- Evidence date: 2024-05-28 16:22.
- Evidence source: https://www.thelec.kr/news/articleView.html?idxno=28149
- At-date evidence: 믹싱 장비 수주잔고 증가 and TSI backlog +101% YoY, but same article context included EV demand slowdown and cell-maker capex speed control.
- Entry rule: after-market article, `entry_date = 2024-05-29` close.
- Result: 180D MFE +3.87%, 180D MAE -46.25%.
- Rule implication: backlog headline under explicit EV chasm context should be Stage4B-Watch / high-MAE guard, not Actionable rerating.

## 6. Current calibrated profile stress test

Current proxy: `e2r_2_1_stock_web_calibrated_proxy`.

| case | likely current profile behavior | actual path verdict | residual error |
|---|---|---|---|
| 코윈테크 | Stage2-Actionable allowed by order/backlog/margin evidence | correct | none |
| 윤성에프앤씨 | Stage2-Actionable allowed by named customer/orderbook/lead-time | correct | none |
| 원익피앤이 | Stage2-Actionable too easily allowed by large backlog vocabulary | false positive | nominal backlog overpromoted |
| 하나기술 | Stage2-Actionable too easily allowed by backlog vocabulary | false positive | backlog quality/delay underweighted |
| 티에스아이 | Stage2-Actionable could be allowed by backlog growth headline | false positive | EV chasm and capex slowdown should force 4B watch |

Answers to required profile questions:

```text
1. current calibrated profile likely handles the two clean positives correctly.
2. It still overpromotes three nominal/orderbook headlines when quality, delay, or EV chasm is present.
3. Stage2 actionable evidence bonus is not globally excessive, but C11 needs a quality bridge before it applies.
4. Yellow threshold 75 is not the main issue; the input component composition is.
5. Green threshold 87 / revision 55 should not be loosened for C11.
6. price-only blowoff guard is appropriate and should remain.
7. full 4B non-price requirement is appropriate; TSI shows non-price 4B evidence can exist inside a backlog-positive article.
8. hard 4C routing should not fire on backlog delay alone; use Stage4B-Watch / thesis-break-watch until contract cancellation or call-off is explicit.
```

## 7. Stage evidence separation

C11 Stage2 evidence must be separated from Stage3 and 4B evidence.

```text
Stage2 useful evidence:
- signed order or credible named-customer backlog
- backlog/delivery visibility
- capacity or shipment route
- early revision signal

Stage3 useful evidence:
- margin bridge
- confirmed revenue recognition
- repeated conversion of backlog into sales
- durable customer confirmation

Stage4B evidence:
- contract delay
- backlog quality discount
- EV chasm / capex slowdown in same evidence context
- high-MAE path after nominal orderbook headline

Stage4C evidence:
- customer project cancellation
- call-off/order cut
- bankruptcy/insolvency of major customer
- thesis evidence broken
```

## 8. Stage3 Yellow / Green lateness audit

No confirmed Stage3-Green trigger is used as representative in this loop. Therefore:

```text
green_lateness_ratio = not_applicable
reason = no_confirmed_Stage3_Green_trigger
```

The two structural successes suggest Stage2-Actionable was the useful entry layer. Waiting for full Stage3-Green confirmation would likely have consumed a large portion of upside in 윤성에프앤씨 and 코윈테크.

## 9. 4B timing audit

Representative 4B row: 티에스아이, 2024-05-28 trigger / 2024-05-29 entry.

```text
four_b_evidence_type = margin_or_backlog_slowdown|contract_delay|positioning_overheat
four_b_timing_verdict = good_full_window_4b_timing_as_watch_not_sale_signal
four_b_local_peak_proximity = not_computed_because_no_prior_stage2_entry_in_same_case
four_b_full_window_peak_proximity = not_computed_because_no_prior_stage2_entry_in_same_case
```

The lesson is not “sell every backlog headline.” The lesson is narrower: if the same evidence packet says backlog rose but EV demand slowed and cell makers are slowing investment, C11 should mark the row as Stage4B-Watch / high-MAE guard until margin conversion is confirmed.

## 10. 4C protection audit

```text
four_c_protection_label = thesis_break_watch_only
hard_4c_success_count = 0
hard_4c_late_count = 0
false_break_count = 0
```

This loop does not recommend hard Stage4C for C11 merely because backlog is delayed. 4C should require stronger break evidence such as explicit order cut, cancellation, customer bankruptcy, or conversion failure that destroys the original thesis.

## 11. Score component simulation

| profile_id | scope | eligible | avg_MFE_90D | avg_MAE_90D | avg_MFE_180D | avg_MAE_180D | false_positive_rate | alignment |
|---|---|---:|---:|---:|---:|---:|---:|---|
| P0_e2r_2_1_stock_web_calibrated_proxy | current_proxy | 5 | 82.8 | -23.0 | 124.25 | -34.56 | 0.6 | weak_alignment_due_nominal_backlog_false_positives |
| P0b_e2r_2_0_baseline_reference | rollback_reference | 5 | 82.8 | -23.0 | 124.25 | -34.56 | 0.6 | worse_than_current_because_ev_chasm_delay_not_discounted |
| P1_L3_sector_orderbook_margin_profile | sector_specific | 3 | 126.39 | -16.61 | 195.49 | -20.46 | 0.33 | better_but_tsi_still_needs_stage4b_watch_override |
| P2_C11_backlog_quality_delay_margin_profile | canonical_archetype_specific | 2 | 187.66 | -7.56 | 291.29 | -7.56 | 0.0 | strong_alignment_positive_set_has_large_MFE_and_shallow_MAE |
| P3_C11_counterexample_guard_profile | counterexample_guard | 2 | 187.66 | -7.56 | 291.29 | -7.56 | 0.0 | best_guardrail_for_current_loop |

Interpretation:

- P0 captures the two successes but allows too many C11 nominal-backlog false positives.
- P2 is the cleanest candidate because it preserves the Cowin/Yoonsung successes and blocks Wonik/Hana/TSI unless they later show conversion evidence.
- P3 is useful as a counterexample guard; it should be implemented as a C11-specific watch/penalty rather than a global rule.

## 12. Proposed sector / canonical shadow rules

```text
rule_scope = canonical_archetype_specific
sector_specific_rule_candidate = L3_ORDERBOOK_TO_REVENUE_MARGIN_CONVERSION_GATE_V1
canonical_archetype_rule_candidate = C11_BACKLOG_QUALITY_DELAY_AND_MARGIN_BRIDGE_GATE_V1
new_axis_proposed = c11_backlog_quality_delay_margin_bridge_gate
existing_axis_tested = stage2_actionable_evidence_bonus|price_only_blowoff_blocks_positive_stage|full_4b_requires_non_price_evidence|hard_4c_thesis_break_routes_to_4c
existing_axis_strengthened = stage2_required_bridge|full_4b_requires_non_price_evidence|price_only_blowoff_blocks_positive_stage
existing_axis_weakened = null
existing_axis_kept = stage3_green_total_min|stage3_green_revision_min|stage3_cross_evidence_green_buffer|hard_4c_thesis_break_routes_to_4c
```

Rule candidate:

```text
C11 Stage2-Actionable requires at least 2 of 3:
1. named customer / signed order / credible order intake quality
2. delivery or revenue-recognition visibility within a reasonable lead-time window
3. margin/revision bridge or confirmed conversion of backlog into earnings

Downgrade to Stage2-Watch or Stage4B-Watch if any of the following are explicit:
- uncertain customer backlog is material
- major customer/project revenue is delayed beyond the trigger year
- EV chasm / battery capex slowdown appears in the same evidence context
- backlog rises but operating margin bridge is absent or deteriorating
```

## 13. Shadow weight table

```csv
scope_id,axis,proposed_delta,confidence,applies_to,block_if,reason
L3_BATTERY_EV_GREEN_MOBILITY,l3_orderbook_to_revenue_margin_bridge_required,+1.0,medium,C11/C12/C13 battery equipment orderbook rows,no_named_customer_or_no_delivery_visibility,L3 orderbook rows work only when backlog converts into revenue/margin timing
C11_BATTERY_ORDERBOOK_RERATING,c11_backlog_quality_delay_margin_bridge_gate,+1.5,medium_high,C11 Stage2-Actionable,uncertain_customer_or_backlog_delay_or_no_margin_bridge,Cowin/Yoonsung positives vs Wonik/Hana/TSI counters separate cleanly
C11_BATTERY_ORDERBOOK_RERATING,c11_uncertain_backlog_delay_penalty,-2.0,medium,C11 nominal backlog rows,Britishvolt_uncertain_or_customer_project_delayed,nominal backlog can be poison when revenue timing shifts beyond 1Y
C11_BATTERY_ORDERBOOK_RERATING,c11_ev_chasm_4b_overlay,+1.0,medium,C11 rows with same-date EV slowdown evidence,EV_chasm_or_cell_capex_slowdown_in_same_evidence_context,TSI shows backlog growth can coexist with high-MAE macro/customer capex risk
```

## 14. Coverage matrix

| large_sector_id | canonical_archetype_id | fine_archetype_id | positive_case_count | counterexample_count | 4B_case_count | 4C_case_count | new_independent_case_count | reused_case_count | calibration_usable_trigger_count | representative_trigger_count | current_profile_error_count | sector_rule_candidate | canonical_rule_candidate | coverage_gap_after_this_loop |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|---|---|
| L3_BATTERY_EV_GREEN_MOBILITY | C11_BATTERY_ORDERBOOK_RERATING | mixed_c11_orderbook_to_revenue_margin_conversion_leaf_set | 2 | 3 | 1 | 0 | 5 | 0 | 5 | 5 | 3 | L3_ORDERBOOK_TO_REVENUE_MARGIN_CONVERSION_GATE_V1 | C11_BACKLOG_QUALITY_DELAY_AND_MARGIN_BRIDGE_GATE_V1 | C11 18→23, need 7 to 30 |

## 15. Batch Ingest Self-Audit

```text
expected_v12_result_file: true
filename_pattern_pass: true
metadata_filename_consistency: pass
jsonl_trigger_row_count: 5
calibration_usable_trigger_count: 5
representative_trigger_count: 5
new_weight_evidence_candidate_count: 5
guardrail_candidate_count: 3
narrative_only_or_rejected_count: 0
rows_missing_required_mfe_mae: 0
rows_missing_entry_price_or_date: 0
rows_with_noncanonical_trigger_type: 0
rows_with_compact_mfe_mae_alias_only: 0
ready_for_batch_ingest: true
```

## 16. Residual Contribution Summary

```text
new_independent_case_count: 5
reused_case_count: 0
reused_case_ids: []
new_symbol_count: 5
new_canonical_archetype_count: 0_existing_priority0_scope
new_fine_archetype_count: 5
new_trigger_family_count: 5
tested_existing_calibrated_axes: stage2_actionable_evidence_bonus|price_only_blowoff_blocks_positive_stage|full_4b_requires_non_price_evidence|hard_4c_thesis_break_routes_to_4c
residual_error_types_found: nominal_backlog_false_positive|backlog_quality_delay_underweighted|ev_chasm_4b_underweighted|stage2_actionable_overpromotion
new_axis_proposed: c11_backlog_quality_delay_margin_bridge_gate
existing_axis_strengthened: stage2_required_bridge|full_4b_requires_non_price_evidence|price_only_blowoff_blocks_positive_stage
existing_axis_weakened: null
existing_axis_kept: stage3_green_total_min|stage3_green_revision_min|stage3_cross_evidence_green_buffer|hard_4c_thesis_break_routes_to_4c
sector_specific_rule_candidate: L3_ORDERBOOK_TO_REVENUE_MARGIN_CONVERSION_GATE_V1
canonical_archetype_rule_candidate: C11_BACKLOG_QUALITY_DELAY_AND_MARGIN_BRIDGE_GATE_V1
no_new_signal_reason: null
loop_contribution_label: canonical_archetype_rule_candidate
do_not_propose_new_weight_delta: false
```

## 17. Machine-readable JSONL rows

```jsonl
{"row_type":"price_source_validation","price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","calibration_shard_root":"atlas/ohlcv_tradable_by_symbol_year","symbol_count":5414,"tradable_row_count":14354401,"computed_mfe_mae_horizons":["30D","90D","180D"],"window_corporate_action_rule":"block if corporate action candidate inside forward 180D window","validation_status":"pass"}
{"row_type":"case","case_id":"C11-282880-20230222-COWIN-BACKLOG-TURNKEY-MARGIN","symbol":"282880","company_name":"코윈테크","round":"R3","loop":131,"large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C11_BATTERY_ORDERBOOK_RERATING","fine_archetype_id":"C11_AUTOMATION_TURNKEY_BACKLOG_MARGIN_CONVERSION","case_role":"structural_success","evidence_source":"https://dealsite.co.kr/articles/99504/068020","trigger_date":"2023-02-22","entry_date":"2023-02-22","trigger_outcome_label":"turnkey_backlog_to_revenue_margin_positive","current_profile_verdict":"current_profile_correct","is_new_independent_case":true,"reuse_reason":null,"calibration_usable":true,"case_summary":"초기 MAE가 얕고 90D/180D MFE가 크다. backlog 증가와 턴키 공급의 margin bridge가 가격경로와 정렬된다."}
{"row_type":"case","case_id":"C11-372170-20221216-YUNSUNG-MIXING-BACKLOG-SKON","symbol":"372170","company_name":"윤성에프앤씨","round":"R3","loop":131,"large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C11_BATTERY_ORDERBOOK_RERATING","fine_archetype_id":"C11_MIXING_EQUIPMENT_CUSTOMER_BACKLOG_LEADTIME","case_role":"structural_success","evidence_source":"https://ssl.pstatic.net/imgstock/upload/research/company/1671150716387.pdf","trigger_date":"2022-12-16","entry_date":"2022-12-19","trigger_outcome_label":"named_customer_backlog_leadtime_margin_positive","current_profile_verdict":"current_profile_correct","is_new_independent_case":true,"reuse_reason":null,"calibration_usable":true,"case_summary":"C11의 이상적인 성공형. 고객·라인·수주 규모·lead time·OPM forecast가 한 묶음으로 제시되고 90D/180D MFE가 압도적이다."}
{"row_type":"case","case_id":"C11-217820-20231020-WONIKPNE-BACKLOG-MARGIN-QUALITY-FAIL","symbol":"217820","company_name":"원익피앤이","round":"R3","loop":131,"large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C11_BATTERY_ORDERBOOK_RERATING","fine_archetype_id":"C11_NOMINAL_BACKLOG_NO_MARGIN_CONVERSION","case_role":"failed_rerating","evidence_source":"https://www.hanaw.com/download/research/FileServer/WEB/info/small_cap/2023/10/20/231023_wonikpne.pdf","trigger_date":"2023-10-20","entry_date":"2023-10-23","trigger_outcome_label":"nominal_backlog_false_positive_margin_quality_failed","current_profile_verdict":"current_profile_false_positive","is_new_independent_case":true,"reuse_reason":null,"calibration_usable":true,"case_summary":"수주잔고 숫자만으로는 Stage2-Actionable을 주면 안 된다는 반례. MFE는 entry day 고점 이후 멈췄고 180D MAE가 -42.15%까지 깊어졌다."}
{"row_type":"case","case_id":"C11-299030-20240304-HANATECH-BACKLOG-DELAY-QUALITY-FAIL","symbol":"299030","company_name":"하나기술","round":"R3","loop":131,"large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C11_BATTERY_ORDERBOOK_RERATING","fine_archetype_id":"C11_BACKLOG_QUALITY_DELAY_BATTERY_EQUIPMENT","case_role":"failed_rerating","evidence_source":"https://ssl.pstatic.net/imgstock/upload/research/company/1709507639094.pdf","trigger_date":"2024-03-04","entry_date":"2024-03-05","trigger_outcome_label":"backlog_quality_delay_false_positive","current_profile_verdict":"current_profile_false_positive","is_new_independent_case":true,"reuse_reason":null,"calibration_usable":true,"case_summary":"backlog는 있었지만 품질·지연·고객별 매출 인식 할인 신호가 동시에 있었다. 30D 고점 뒤 180D MAE -69.27%로 C11 high-MAE guard가 필요했다."}
{"row_type":"case","case_id":"C11-277880-20240528-TSI-MIXING-BACKLOG-CHASM-4B","symbol":"277880","company_name":"티에스아이","round":"R3","loop":131,"large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C11_BATTERY_ORDERBOOK_RERATING","fine_archetype_id":"C11_MIXING_BACKLOG_CHASM_4B_GUARD","case_role":"4B_overlay_success","evidence_source":"https://www.thelec.kr/news/articleView.html?idxno=28149","trigger_date":"2024-05-28","entry_date":"2024-05-29","trigger_outcome_label":"backlog_growth_inside_ev_chasm_high_mae_4b","current_profile_verdict":"current_profile_false_positive","is_new_independent_case":true,"reuse_reason":null,"calibration_usable":true,"case_summary":"수주잔고 증가는 있었지만 바로 같은 문맥에 EV chasm과 투자 속도 조절이 붙었다. MFE가 3.87%에 그치고 180D MAE -46.25%라 4B watch가 더 정확했다."}
{"row_type":"trigger","trigger_id":"TRG-C11-282880-20230222-STAGE2A","case_id":"C11-282880-20230222-COWIN-BACKLOG-TURNKEY-MARGIN","symbol":"282880","company_name":"코윈테크","round":"R3","loop":131,"large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C11_BATTERY_ORDERBOOK_RERATING","fine_archetype_id":"C11_AUTOMATION_TURNKEY_BACKLOG_MARGIN_CONVERSION","sector":"battery_ev_green_mobility","primary_archetype":"battery_orderbook_rerating","loop_objective":"coverage_gap_fill|counterexample_mining|canonical_archetype_rule_discovery|stage2_actionable_bonus_stress_test|4b_non_price_requirement_stress_test","trigger_type":"Stage2-Actionable","trigger_date":"2023-02-22","evidence_available_at_that_date":true,"evidence_source":"https://dealsite.co.kr/articles/99504/068020","stage2_evidence_fields":["public_event_or_disclosure","customer_or_order_quality","backlog_or_delivery_visibility","capacity_or_volume_route","early_revision_signal"],"stage3_evidence_fields":["margin_bridge","financial_visibility","repeat_order_or_conversion","durable_customer_confirmation"],"stage4b_evidence_fields":["price_only_local_peak"],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/282/282880/2023.csv","profile_path":"atlas/symbol_profiles/282/282880.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","entry_date":"2023-02-22","entry_price":25100.0,"MFE_30D_pct":37.85,"MFE_90D_pct":67.33,"MFE_180D_pct":87.25,"MFE_1Y_pct":null,"MFE_2Y_pct":null,"MAE_30D_pct":-4.38,"MAE_90D_pct":-4.38,"MAE_180D_pct":-4.38,"MAE_1Y_pct":null,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2023-07-25","peak_price":47000.0,"drawdown_after_peak_pct":-41.91,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":null,"four_b_full_window_peak_proximity":null,"four_b_timing_verdict":"not_applicable","four_b_evidence_type":"none","four_c_protection_label":"not_applicable","trigger_outcome_label":"turnkey_backlog_to_revenue_margin_positive","current_profile_verdict":"current_profile_correct","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"C11-282880-20230222-COWIN-BACKLOG-TURNKEY-MARGIN|2023-02-22","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"TRG-C11-372170-20221216-STAGE2A","case_id":"C11-372170-20221216-YUNSUNG-MIXING-BACKLOG-SKON","symbol":"372170","company_name":"윤성에프앤씨","round":"R3","loop":131,"large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C11_BATTERY_ORDERBOOK_RERATING","fine_archetype_id":"C11_MIXING_EQUIPMENT_CUSTOMER_BACKLOG_LEADTIME","sector":"battery_ev_green_mobility","primary_archetype":"battery_orderbook_rerating","loop_objective":"coverage_gap_fill|counterexample_mining|canonical_archetype_rule_discovery|stage2_actionable_bonus_stress_test|4b_non_price_requirement_stress_test","trigger_type":"Stage2-Actionable","trigger_date":"2022-12-16","evidence_available_at_that_date":true,"evidence_source":"https://ssl.pstatic.net/imgstock/upload/research/company/1671150716387.pdf","stage2_evidence_fields":["public_event_or_disclosure","customer_or_order_quality","backlog_or_delivery_visibility","capacity_or_volume_route","early_revision_signal"],"stage3_evidence_fields":["margin_bridge","financial_visibility","durable_customer_confirmation","repeat_order_or_conversion"],"stage4b_evidence_fields":["positioning_overheat","price_only_local_peak"],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/372/372170/2022.csv;atlas/ohlcv_tradable_by_symbol_year/372/372170/2023.csv","profile_path":"atlas/symbol_profiles/372/372170.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","entry_date":"2022-12-19","entry_price":45100.0,"MFE_30D_pct":20.62,"MFE_90D_pct":307.98,"MFE_180D_pct":495.34,"MFE_1Y_pct":null,"MFE_2Y_pct":null,"MAE_30D_pct":-10.75,"MAE_90D_pct":-10.75,"MAE_180D_pct":-10.75,"MAE_1Y_pct":null,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2023-07-25","peak_price":268500.0,"drawdown_after_peak_pct":-33.78,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":null,"four_b_full_window_peak_proximity":null,"four_b_timing_verdict":"local_4b_possible_but_not_full_without_nonprice_overheat","four_b_evidence_type":"price_only|positioning_overheat_watch","four_c_protection_label":"not_applicable","trigger_outcome_label":"named_customer_backlog_leadtime_margin_positive","current_profile_verdict":"current_profile_correct","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"C11-372170-20221216-YUNSUNG-MIXING-BACKLOG-SKON|2022-12-19","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"TRG-C11-217820-20231020-STAGE2A-FP","case_id":"C11-217820-20231020-WONIKPNE-BACKLOG-MARGIN-QUALITY-FAIL","symbol":"217820","company_name":"원익피앤이","round":"R3","loop":131,"large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C11_BATTERY_ORDERBOOK_RERATING","fine_archetype_id":"C11_NOMINAL_BACKLOG_NO_MARGIN_CONVERSION","sector":"battery_ev_green_mobility","primary_archetype":"battery_orderbook_rerating","loop_objective":"coverage_gap_fill|counterexample_mining|canonical_archetype_rule_discovery|stage2_actionable_bonus_stress_test|4b_non_price_requirement_stress_test","trigger_type":"Stage2-Actionable","trigger_date":"2023-10-20","evidence_available_at_that_date":true,"evidence_source":"https://www.hanaw.com/download/research/FileServer/WEB/info/small_cap/2023/10/20/231023_wonikpne.pdf","stage2_evidence_fields":["public_event_or_disclosure","backlog_or_delivery_visibility","early_revision_signal"],"stage3_evidence_fields":["financial_visibility"],"stage4b_evidence_fields":["margin_or_backlog_slowdown","contract_delay","positioning_overheat"],"stage4c_evidence_fields":["thesis_evidence_broken"],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/217/217820/2023.csv;atlas/ohlcv_tradable_by_symbol_year/217/217820/2024.csv","profile_path":"atlas/symbol_profiles/217/217820.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","entry_date":"2023-10-23","entry_price":6880.0,"MFE_30D_pct":13.37,"MFE_90D_pct":13.37,"MFE_180D_pct":13.37,"MFE_1Y_pct":null,"MFE_2Y_pct":null,"MAE_30D_pct":-12.5,"MAE_90D_pct":-21.22,"MAE_180D_pct":-42.15,"MAE_1Y_pct":null,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2023-10-23","peak_price":7800.0,"drawdown_after_peak_pct":-48.97,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":null,"four_b_full_window_peak_proximity":null,"four_b_timing_verdict":"nonprice_4b_watch_should_have_overruled_stage2_actionable","four_b_evidence_type":"margin_or_backlog_slowdown|contract_delay","four_c_protection_label":"thesis_break_watch_only","trigger_outcome_label":"nominal_backlog_false_positive_margin_quality_failed","current_profile_verdict":"current_profile_false_positive","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window_candidate_outside_window","same_entry_group_id":"C11-217820-20231020-WONIKPNE-BACKLOG-MARGIN-QUALITY-FAIL|2023-10-23","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"TRG-C11-299030-20240304-STAGE2A-FP","case_id":"C11-299030-20240304-HANATECH-BACKLOG-DELAY-QUALITY-FAIL","symbol":"299030","company_name":"하나기술","round":"R3","loop":131,"large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C11_BATTERY_ORDERBOOK_RERATING","fine_archetype_id":"C11_BACKLOG_QUALITY_DELAY_BATTERY_EQUIPMENT","sector":"battery_ev_green_mobility","primary_archetype":"battery_orderbook_rerating","loop_objective":"coverage_gap_fill|counterexample_mining|canonical_archetype_rule_discovery|stage2_actionable_bonus_stress_test|4b_non_price_requirement_stress_test","trigger_type":"Stage2-Actionable","trigger_date":"2024-03-04","evidence_available_at_that_date":true,"evidence_source":"https://ssl.pstatic.net/imgstock/upload/research/company/1709507639094.pdf","stage2_evidence_fields":["public_event_or_disclosure","backlog_or_delivery_visibility"],"stage3_evidence_fields":[],"stage4b_evidence_fields":["contract_delay","margin_or_backlog_slowdown","positioning_overheat"],"stage4c_evidence_fields":["thesis_evidence_broken"],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/299/299030/2024.csv","profile_path":"atlas/symbol_profiles/299/299030.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","entry_date":"2024-03-05","entry_price":60200.0,"MFE_30D_pct":21.43,"MFE_90D_pct":21.43,"MFE_180D_pct":21.43,"MFE_1Y_pct":null,"MFE_2Y_pct":null,"MAE_30D_pct":-16.94,"MAE_90D_pct":-43.94,"MAE_180D_pct":-69.27,"MAE_1Y_pct":null,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-03-08","peak_price":73100.0,"drawdown_after_peak_pct":-74.69,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":null,"four_b_full_window_peak_proximity":null,"four_b_timing_verdict":"good_nonprice_4b_watch_needed_before_full_stage2","four_b_evidence_type":"contract_delay|margin_or_backlog_slowdown","four_c_protection_label":"thesis_break_watch_only","trigger_outcome_label":"backlog_quality_delay_false_positive","current_profile_verdict":"current_profile_false_positive","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window_candidate_outside_window","same_entry_group_id":"C11-299030-20240304-HANATECH-BACKLOG-DELAY-QUALITY-FAIL|2024-03-05","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"TRG-C11-277880-20240528-STAGE4B","case_id":"C11-277880-20240528-TSI-MIXING-BACKLOG-CHASM-4B","symbol":"277880","company_name":"티에스아이","round":"R3","loop":131,"large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C11_BATTERY_ORDERBOOK_RERATING","fine_archetype_id":"C11_MIXING_BACKLOG_CHASM_4B_GUARD","sector":"battery_ev_green_mobility","primary_archetype":"battery_orderbook_rerating","loop_objective":"coverage_gap_fill|counterexample_mining|canonical_archetype_rule_discovery|stage2_actionable_bonus_stress_test|4b_non_price_requirement_stress_test","trigger_type":"Stage4B","trigger_date":"2024-05-28","evidence_available_at_that_date":true,"evidence_source":"https://www.thelec.kr/news/articleView.html?idxno=28149","stage2_evidence_fields":["public_event_or_disclosure","backlog_or_delivery_visibility","customer_or_order_quality"],"stage3_evidence_fields":[],"stage4b_evidence_fields":["margin_or_backlog_slowdown","contract_delay","positioning_overheat"],"stage4c_evidence_fields":["thesis_evidence_broken"],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/277/277880/2024.csv;atlas/ohlcv_tradable_by_symbol_year/277/277880/2025.csv","profile_path":"atlas/symbol_profiles/277/277880.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","entry_date":"2024-05-29","entry_price":8270.0,"MFE_30D_pct":3.87,"MFE_90D_pct":3.87,"MFE_180D_pct":3.87,"MFE_1Y_pct":null,"MFE_2Y_pct":null,"MAE_30D_pct":-11.73,"MAE_90D_pct":-34.7,"MAE_180D_pct":-46.25,"MAE_1Y_pct":null,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-06-12","peak_price":8590.0,"drawdown_after_peak_pct":-48.25,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":null,"four_b_full_window_peak_proximity":null,"four_b_timing_verdict":"good_full_window_4b_timing_as_watch_not_sale_signal","four_b_evidence_type":"margin_or_backlog_slowdown|contract_delay|positioning_overheat","four_c_protection_label":"thesis_break_watch_only","trigger_outcome_label":"backlog_growth_inside_ev_chasm_high_mae_4b","current_profile_verdict":"current_profile_false_positive","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window_candidate_outside_window","same_entry_group_id":"C11-277880-20240528-TSI-MIXING-BACKLOG-CHASM-4B|2024-05-29","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"score_profile_aggregate","profile_id":"P0_e2r_2_1_stock_web_calibrated_proxy","profile_scope":"current_proxy","profile_hypothesis":"Nominal C11 orderbook/backlog evidence can receive Stage2-Actionable when there is public order/backlog support. Existing global guards are present but not C11-specific enough.","changed_axes":"none","changed_thresholds":"none","eligible_trigger_count":5,"selected_entry_trigger_per_case":5,"avg_MFE_90D_pct":82.8,"avg_MAE_90D_pct":-23.0,"avg_MFE_180D_pct":124.25,"avg_MAE_180D_pct":-34.56,"false_positive_rate":0.6,"missed_structural_count":0,"late_green_count":0,"avg_green_lateness_ratio":"not_applicable","avg_four_b_local_peak_proximity":"not_applicable","avg_four_b_full_window_peak_proximity":"not_applicable","score_return_alignment_verdict":"weak_alignment_due_nominal_backlog_false_positives"}
{"row_type":"score_profile_aggregate","profile_id":"P0b_e2r_2_0_baseline_reference","profile_scope":"rollback_reference","profile_hypothesis":"Old baseline would be more narrative-sensitive and less protected by price-only/4B/4C guards.","changed_axes":"rollback_to_pre_stock_web_calibration","changed_thresholds":"lower_stage2_bridge","eligible_trigger_count":5,"selected_entry_trigger_per_case":5,"avg_MFE_90D_pct":82.8,"avg_MAE_90D_pct":-23.0,"avg_MFE_180D_pct":124.25,"avg_MAE_180D_pct":-34.56,"false_positive_rate":0.6,"missed_structural_count":0,"late_green_count":0,"avg_green_lateness_ratio":"not_applicable","avg_four_b_local_peak_proximity":"not_applicable","avg_four_b_full_window_peak_proximity":"not_applicable","score_return_alignment_verdict":"worse_than_current_because_ev_chasm_delay_not_discounted"}
{"row_type":"score_profile_aggregate","profile_id":"P1_L3_sector_orderbook_margin_profile","profile_scope":"sector_specific","profile_hypothesis":"For L3 battery equipment, Stage2-Actionable requires orderbook + delivery/revenue timing + at least one margin/revision bridge; EV demand-slowdown vocabulary lowers actionability.","changed_axes":"l3_orderbook_to_revenue_margin_bridge_required; l3_ev_chasm_backlog_discount","changed_thresholds":"stage2_actionable_bridge_min=2_of_4","eligible_trigger_count":3,"selected_entry_trigger_per_case":3,"avg_MFE_90D_pct":126.39,"avg_MAE_90D_pct":-16.61,"avg_MFE_180D_pct":195.49,"avg_MAE_180D_pct":-20.46,"false_positive_rate":0.33,"missed_structural_count":0,"late_green_count":0,"avg_green_lateness_ratio":"not_applicable","avg_four_b_local_peak_proximity":"not_applicable","avg_four_b_full_window_peak_proximity":"not_applicable","score_return_alignment_verdict":"better_but_tsi_still_needs_stage4b_watch_override"}
{"row_type":"score_profile_aggregate","profile_id":"P2_C11_backlog_quality_delay_margin_profile","profile_scope":"canonical_archetype_specific","profile_hypothesis":"C11 Stage2-Actionable only when nominal orderbook is backed by named customer/order quality, backlog delivery visibility, and margin/revision bridge; backlog delay/uncertain customer converts to Watch/4B.","changed_axes":"c11_backlog_quality_delay_margin_bridge_gate","changed_thresholds":"stage2_actionable_requires_named_customer_or_signed_order + delivery_visibility + margin_bridge_or_revision; delay_or_uncertain_customer_penalty=-8_to_-15","eligible_trigger_count":2,"selected_entry_trigger_per_case":2,"avg_MFE_90D_pct":187.66,"avg_MAE_90D_pct":-7.56,"avg_MFE_180D_pct":291.29,"avg_MAE_180D_pct":-7.56,"false_positive_rate":0.0,"missed_structural_count":0,"late_green_count":0,"avg_green_lateness_ratio":"not_applicable","avg_four_b_local_peak_proximity":"not_applicable","avg_four_b_full_window_peak_proximity":"not_applicable","score_return_alignment_verdict":"strong_alignment_positive_set_has_large_MFE_and_shallow_MAE"}
{"row_type":"score_profile_aggregate","profile_id":"P3_C11_counterexample_guard_profile","profile_scope":"counterexample_guard","profile_hypothesis":"Explicit guard blocks Stage2-Actionable when backlog quality is uncertain, major customer project is delayed, EV chasm appears in same evidence context, or high-MAE 4B watch evidence exists.","changed_axes":"c11_backlog_delay_discount;c11_ev_chasm_4b_overlay;nominal_backlog_no_margin_block","changed_thresholds":"4b_watch_if_delay_or_chasm_and_no_margin_bridge;stage2_actionable_block_when_uncertain_backlog_value_gt_25pct_backlog","eligible_trigger_count":2,"selected_entry_trigger_per_case":2,"avg_MFE_90D_pct":187.66,"avg_MAE_90D_pct":-7.56,"avg_MFE_180D_pct":291.29,"avg_MAE_180D_pct":-7.56,"false_positive_rate":0.0,"missed_structural_count":0,"late_green_count":0,"avg_green_lateness_ratio":"not_applicable","avg_four_b_local_peak_proximity":"not_applicable","avg_four_b_full_window_peak_proximity":"not_applicable","score_return_alignment_verdict":"best_guardrail_for_current_loop"}
{"row_type":"score_simulation","trigger_id":"TRG-C11-282880-20230222-STAGE2A","case_id":"C11-282880-20230222-COWIN-BACKLOG-TURNKEY-MARGIN","symbol":"282880","before_profile_id":"P0_e2r_2_1_stock_web_calibrated_proxy","after_profile_id":"P2_C11_backlog_quality_delay_margin_profile","rollback_reference_profile_id":"P0b_e2r_2_0_baseline_reference","raw_component_scores_before":{"contract_score":78,"backlog_visibility_score":84,"margin_bridge_score":73,"revision_score":68,"relative_strength_score":70,"customer_quality_score":78,"policy_or_regulatory_score":45,"valuation_repricing_score":62,"execution_risk_score":28,"legal_or_contract_risk_score":15,"dilution_cb_risk_score":10,"accounting_trust_risk_score":10},"weighted_score_before":78,"stage_label_before":"Stage2-Actionable","raw_component_scores_after":{"contract_score":80,"backlog_visibility_score":87,"margin_bridge_score":78,"revision_score":70,"relative_strength_score":72,"customer_quality_score":82,"policy_or_regulatory_score":45,"valuation_repricing_score":63,"execution_risk_score":25,"legal_or_contract_risk_score":13,"dilution_cb_risk_score":10,"accounting_trust_risk_score":10},"weighted_score_after":82,"stage_label_after":"Stage2-Actionable","component_delta_explanation":"C11 proposed gate increases weight on named customer/order quality, delivery/revenue timing, margin/revision bridge, and penalizes backlog delay/uncertain customer/EV chasm context."}
{"row_type":"score_simulation","trigger_id":"TRG-C11-372170-20221216-STAGE2A","case_id":"C11-372170-20221216-YUNSUNG-MIXING-BACKLOG-SKON","symbol":"372170","before_profile_id":"P0_e2r_2_1_stock_web_calibrated_proxy","after_profile_id":"P2_C11_backlog_quality_delay_margin_profile","rollback_reference_profile_id":"P0b_e2r_2_0_baseline_reference","raw_component_scores_before":{"contract_score":86,"backlog_visibility_score":88,"margin_bridge_score":82,"revision_score":74,"relative_strength_score":68,"customer_quality_score":85,"policy_or_regulatory_score":45,"valuation_repricing_score":64,"execution_risk_score":25,"legal_or_contract_risk_score":15,"dilution_cb_risk_score":10,"accounting_trust_risk_score":10},"weighted_score_before":80,"stage_label_before":"Stage2-Actionable","raw_component_scores_after":{"contract_score":90,"backlog_visibility_score":92,"margin_bridge_score":86,"revision_score":78,"relative_strength_score":70,"customer_quality_score":90,"policy_or_regulatory_score":45,"valuation_repricing_score":66,"execution_risk_score":22,"legal_or_contract_risk_score":12,"dilution_cb_risk_score":10,"accounting_trust_risk_score":10},"weighted_score_after":85,"stage_label_after":"Stage2-Actionable","component_delta_explanation":"C11 proposed gate increases weight on named customer/order quality, delivery/revenue timing, margin/revision bridge, and penalizes backlog delay/uncertain customer/EV chasm context."}
{"row_type":"score_simulation","trigger_id":"TRG-C11-217820-20231020-STAGE2A-FP","case_id":"C11-217820-20231020-WONIKPNE-BACKLOG-MARGIN-QUALITY-FAIL","symbol":"217820","before_profile_id":"P0_e2r_2_1_stock_web_calibrated_proxy","after_profile_id":"P2_C11_backlog_quality_delay_margin_profile","rollback_reference_profile_id":"P0b_e2r_2_0_baseline_reference","raw_component_scores_before":{"contract_score":72,"backlog_visibility_score":82,"margin_bridge_score":58,"revision_score":64,"relative_strength_score":55,"customer_quality_score":60,"policy_or_regulatory_score":40,"valuation_repricing_score":56,"execution_risk_score":45,"legal_or_contract_risk_score":25,"dilution_cb_risk_score":15,"accounting_trust_risk_score":15},"weighted_score_before":77,"stage_label_before":"Stage2-Actionable","raw_component_scores_after":{"contract_score":65,"backlog_visibility_score":70,"margin_bridge_score":38,"revision_score":45,"relative_strength_score":45,"customer_quality_score":48,"policy_or_regulatory_score":40,"valuation_repricing_score":50,"execution_risk_score":65,"legal_or_contract_risk_score":35,"dilution_cb_risk_score":15,"accounting_trust_risk_score":15},"weighted_score_after":61,"stage_label_after":"Stage2-Watch","component_delta_explanation":"C11 proposed gate increases weight on named customer/order quality, delivery/revenue timing, margin/revision bridge, and penalizes backlog delay/uncertain customer/EV chasm context."}
{"row_type":"score_simulation","trigger_id":"TRG-C11-299030-20240304-STAGE2A-FP","case_id":"C11-299030-20240304-HANATECH-BACKLOG-DELAY-QUALITY-FAIL","symbol":"299030","before_profile_id":"P0_e2r_2_1_stock_web_calibrated_proxy","after_profile_id":"P2_C11_backlog_quality_delay_margin_profile","rollback_reference_profile_id":"P0b_e2r_2_0_baseline_reference","raw_component_scores_before":{"contract_score":70,"backlog_visibility_score":80,"margin_bridge_score":50,"revision_score":55,"relative_strength_score":62,"customer_quality_score":55,"policy_or_regulatory_score":40,"valuation_repricing_score":58,"execution_risk_score":50,"legal_or_contract_risk_score":35,"dilution_cb_risk_score":12,"accounting_trust_risk_score":15},"weighted_score_before":75,"stage_label_before":"Stage2-Actionable","raw_component_scores_after":{"contract_score":55,"backlog_visibility_score":58,"margin_bridge_score":30,"revision_score":35,"relative_strength_score":48,"customer_quality_score":42,"policy_or_regulatory_score":40,"valuation_repricing_score":48,"execution_risk_score":78,"legal_or_contract_risk_score":55,"dilution_cb_risk_score":12,"accounting_trust_risk_score":15},"weighted_score_after":55,"stage_label_after":"Stage2-Watch/Stage4B","component_delta_explanation":"C11 proposed gate increases weight on named customer/order quality, delivery/revenue timing, margin/revision bridge, and penalizes backlog delay/uncertain customer/EV chasm context."}
{"row_type":"score_simulation","trigger_id":"TRG-C11-277880-20240528-STAGE4B","case_id":"C11-277880-20240528-TSI-MIXING-BACKLOG-CHASM-4B","symbol":"277880","before_profile_id":"P0_e2r_2_1_stock_web_calibrated_proxy","after_profile_id":"P2_C11_backlog_quality_delay_margin_profile","rollback_reference_profile_id":"P0b_e2r_2_0_baseline_reference","raw_component_scores_before":{"contract_score":75,"backlog_visibility_score":78,"margin_bridge_score":45,"revision_score":42,"relative_strength_score":48,"customer_quality_score":58,"policy_or_regulatory_score":38,"valuation_repricing_score":52,"execution_risk_score":55,"legal_or_contract_risk_score":30,"dilution_cb_risk_score":12,"accounting_trust_risk_score":12},"weighted_score_before":72,"stage_label_before":"Stage2-Actionable","raw_component_scores_after":{"contract_score":70,"backlog_visibility_score":70,"margin_bridge_score":28,"revision_score":30,"relative_strength_score":38,"customer_quality_score":52,"policy_or_regulatory_score":38,"valuation_repricing_score":45,"execution_risk_score":78,"legal_or_contract_risk_score":45,"dilution_cb_risk_score":12,"accounting_trust_risk_score":12},"weighted_score_after":58,"stage_label_after":"Stage4B-Watch","component_delta_explanation":"C11 proposed gate increases weight on named customer/order quality, delivery/revenue timing, margin/revision bridge, and penalizes backlog delay/uncertain customer/EV chasm context."}
{"row_type":"residual_contribution","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C11_BATTERY_ORDERBOOK_RERATING","round":"R3","loop":131,"new_independent_case_count":5,"reused_case_count":0,"new_symbol_count":5,"new_trigger_family_count":5,"positive_case_count":2,"counterexample_count":3,"current_profile_error_count":3,"new_axis_proposed":"c11_backlog_quality_delay_margin_bridge_gate","existing_axis_strengthened":"stage2_required_bridge|full_4b_requires_non_price_evidence|price_only_blowoff_blocks_positive_stage","existing_axis_weakened":null,"sector_specific_rule_candidate":"L3_ORDERBOOK_TO_REVENUE_MARGIN_CONVERSION_GATE_V1","canonical_archetype_rule_candidate":"C11_BACKLOG_QUALITY_DELAY_AND_MARGIN_BRIDGE_GATE_V1","loop_contribution_label":"canonical_archetype_rule_candidate","coverage_before_rows":18,"coverage_after_if_accepted_rows":23,"need_to_30_after_if_accepted":7,"need_to_50_after_if_accepted":27}
```

## 18. Deferred Coding Agent Handoff Prompt

```text
You are a coding agent operating on Songdaiki/stock_agent. Do not treat this MD as a command to patch production immediately. First run the normal v12 ingestion/validation pipeline over docs/round. If this file passes schema validation and dedupe, evaluate the proposed C11_BACKLOG_QUALITY_DELAY_AND_MARGIN_BRIDGE_GATE_V1 only as a shadow/canonical-archetype-specific candidate. Do not loosen Stage3-Green. Do not globally alter Stage2 bonus. Apply only if aggregate validation across representative C11 rows supports lower false positives without missing structural positives. Preserve rollback metadata.

Required checks:
- filename is standard v12 result filename
- large_sector_id == L3_BATTERY_EV_GREEN_MOBILITY
- canonical_archetype_id == C11_BATTERY_ORDERBOOK_RERATING
- all trigger rows have entry_date, entry_price, MFE_30D_pct, MFE_90D_pct, MFE_180D_pct, MAE_30D_pct, MAE_90D_pct, MAE_180D_pct
- all trigger_type values are canonical Stage labels
- stock-web price source fields are present
- representative dedupe key is canonical_archetype_id + symbol + trigger_type + entry_date
- no corporate action contamination inside 180D forward window
```

## 19. Final interpretation

C11은 단순히 “수주잔고가 커졌다”를 사는 아키타입이 아니다. 좋은 C11은 배터리 장비 업체의 backlog가 고객·납기·매출 인식·마진 다리로 흘러가야 한다. 코윈테크와 윤성에프앤씨는 그 다리가 있었고, 원익피앤이·하나기술·티에스아이는 backlog 숫자 옆에 품질 할인, 지연, EV chasm, margin bridge 부재가 있었다. 따라서 이번 loop의 핵심 기여는 `C11_BACKLOG_QUALITY_DELAY_AND_MARGIN_BRIDGE_GATE_V1`이다.
