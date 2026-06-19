# E2R Stock-Web Historical Calibration / Sector-Archetype Residual Research Round

## 0. Research Metadata

```text
output_file = e2r_stock_web_v12_residual_round_R2_loop_130_L2_AI_SEMICONDUCTOR_ELECTRONICS_C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY_research.md
selected_round = R2
selected_loop = 130
selection_basis = docs/core/V12_Research_No_Repeat_Index.md
selected_priority_bucket = Priority 2 / quality_repair / C08 rows 50; guidance = URL/proxy 보강, 반례/4B/4C 균형 확인
round_schedule_status = coverage_index_selected_after_priority_0_1_local_continuation
round_sector_consistency = pass
large_sector_id = L2_AI_SEMICONDUCTOR_ELECTRONICS
canonical_archetype_id = C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY
fine_archetype_id = SEMI_TEST_SOCKET_CUSTOMER_QUALIFICATION_URL_REPAIR_AND_PROXY_GUARD
loop_objective = quality_repair | source_proxy_replacement | counterexample_mining | 4B_non_price_requirement_stress_test | canonical_archetype_compression | stage2_actionable_bonus_stress_test
price_source = Songdaiki/stock-web
price_basis = tradable_raw
price_adjustment_status = raw_unadjusted_marcap
stock_web_manifest_max_date = 2026-02-20
production_scoring_changed = false
shadow_weight_only = true
handoff_prompt_executed_now = false
```

## 1. Current Calibrated Profile Assumption

Current profile proxy is `e2r_2_1_stock_web_calibrated_proxy`; rollback reference is `e2r_2_0_baseline_reference`. This loop does not re-prove the global Stage2 bonus, Yellow threshold, or Green threshold. It stress-tests a narrower C08 residual: test socket / semiconductor inspection stories need actual customer-quality evidence, qualification status, repeat consumable economics, or named-customer order conversion. Product-adjacent HBM inspection headlines without those bridges behave like sparks on dry grass: they glow brightly for a day, then the drawdown does the real scoring.

## 2. Round / Large Sector / Canonical Archetype Scope

C08 maps to `R2 / L2_AI_SEMICONDUCTOR_ELECTRONICS`. This is a sector-specific semiconductor test/socket quality-repair run, not an R13 global guardrail run.

```text
canonical = C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY
fine = SEMI_TEST_SOCKET_CUSTOMER_QUALIFICATION_URL_REPAIR_AND_PROXY_GUARD
primary thesis = customer-quality / qualification / repeat socket economics are the bridge; HBM-adjacent inspection proxy alone is not enough.
```

## 3. Previous Coverage / Duplicate Avoidance Check

The static no-repeat ledger already shows C08 at 50 representative rows, so the job is not raw coverage quantity. The job is quality repair: URL/proxy replacement, positive/counterexample balance, and better 4B timing for C08. Previous local continuation outputs in this session used C02/C09/C14/C10/C06/C07/C11/C01/C28/C12/C05/C23/C27. This C08 loop is the first local C08 output in the continuation and intentionally uses a C08 quality-repair scope.

```text
hard_duplicate_key = canonical_archetype_id + symbol + trigger_type + entry_date
quality_repair_allowed = true
schema_rematerialization_only = false
```

## 4. Stock-Web OHLC Input / Price Source Validation

```text
source = Songdaiki/stock-web
manifest_path = atlas/manifest.json
schema_path = atlas/schema.json
price_basis = tradable_raw
price_adjustment_status = raw_unadjusted_marcap
calibration_shard_root = atlas/ohlcv_tradable_by_symbol_year
stock_web_manifest_max_date = 2026-02-20
```

The stock-web manifest defines the atlas as raw/unadjusted marcap OHLC and calibration-safe tradable shards. For this quality-repair run, price paths are taken from existing stock-web-backed representative/prior local rows where available, while evidence URLs are repaired or narrowed into C08-specific source quality. No production score is changed by this MD.

## 5. Historical Eligibility Gate

All six trigger rows have historical trigger dates, stock-web-backed entry dates, entry close prices, and complete 30D/90D/180D MFE/MAE fields. Five rows are representative for aggregate; the July YC row is a 4B overlay-only row because it is the same symbol after a prior customer-order rerating.

## 6. Canonical Archetype Compression Map

| fine/deep sub-archetype | compressed canonical | stage implication |
|---|---|---|
| system_level_test_socket_repeat_consumable | C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY | Stage2-Actionable; Yellow only if margin/customer bridge survives |
| cube_prober_customer_qualification | C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY | Stage2-Actionable while qualification/PO pending; Green blocked |
| named_customer_memory_wafer_tester_contract | C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY | Actionable positive, but 4B after large runup |
| small_hbm_overlay_metrology_order | C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY | Stage2-watch / proxy haircut, not Actionable |
| hbm_packaging_inspection_expectation_loss_pressure | C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY | counterexample; pilot/expectation plus loss pressure blocks promotion |
| second_large_order_after_runup | C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY | 4B overlay, not fresh positive |

## 7. Case Selection Summary

|case_id|symbol|company|trigger_type|entry_date|entry_price|MFE90|MAE90|MFE180|MAE180|role|current_profile_verdict|
|---|---|---|---|---|---:|---:|---:|---:|---:|---|---|
|C08-R2L130-058470-LEENO-TEST-SOCKET-QUALITY-REPEAT-URL-REPAIR|058470|리노공업|Stage2-Actionable|2024-02-13|219000|49.28|-3.38|49.28|-30.77|positive|current_profile_correct_if_customer_qualification_repeat_demand_margin_cash_bridge_required_but_green_strict|
|C08-R2L130-089030-TECHWING-CUBE-PROBER-QUALIFICATION-STAGE2|089030|테크윙|Stage2-Actionable|2024-03-15|30300|133.66|-9.57|133.66|-9.57|positive|current_profile_too_late_if_customer_quality_path_ignored_but_green_would_be_too_early|
|C08-R2L130-232140-YC-SAMSUNG-MEMORY-TESTER-CUSTOMER-QUALITY|232140|와이씨|Stage2-Actionable|2024-04-25|12060|90.3|-9.54|90.3|-31.43|positive|current_profile_correct_as_actionable_not_green_for_C08|
|C08-R2L130-322310-OROS-HBM-PAD-OVERLAY-PROXY-GUARD|322310|오로스테크놀로지|Stage2|2024-05-17|29100|5.5|-48.01|5.5|-54.71|counterexample|current_profile_false_positive_if_HBM_overlay_proxy_promotes_C08_actionable|
|C08-R2L130-064290-INTEKPLUS-HBM-PACKAGING-EXPECTATION-LOSS-GUARD|064290|인텍플러스|Stage2|2024-07-17|20450|5.62|-54.91|5.62|-60.98|counterexample|current_profile_false_positive_if_pilot_expectation_plus_rs_promotes_actionable|
|C08-R2L130-232140-YC-SAMSUNG-HBM-ORDER-LATE-4B|232140|와이씨|Stage4B|2024-07-30|16500|16.24|-49.88|16.24|-49.88|counterexample|current_profile_4B_too_late_if_waiting_for_second_large_order_in_C08|

## 8. Positive vs Counterexample Balance

```text
positive_case_count = 3
counterexample_count = 3
4B_case_count = 1
4C_case_count = 0
new_independent_case_count = 5
reused_case_count = 1
same_archetype_new_symbol_count = 5
same_archetype_new_trigger_family_count = 6
```

Positive controls have avg MFE90 `91.08` and avg MAE90 `-7.5`. Counterexamples have avg MFE90 `9.12` and avg MAE90 `-50.93`. The split is clean enough for a C08-specific shadow rule: the bridge is not the word `HBM`; the bridge is verified customer-quality / qualification / repeat demand.

## 9. Evidence Source Map

| symbol | evidence family | source route |
|---|---|---|
|058470|official system-level test socket product route, AP/baseband/AI applications, repeat socket quality|LEENO official product page; KRX/KIND quarterly report route; prior C08 representative source repair|
|089030|Cube Prober HBM package-test route; customer qualification pending; 3Q PO expectation|Asia Business Daily; TheBell customer qualification article|
|232140|Samsung memory wafer tester contract; later HBM tester contract after runup|ETNews April contract; MoneyToday July HBM contract|
|322310|Samsung HBM PAD overlay equipment order; small-order/proxy inspection route|AjuNews; TheElec|
|064290|HBM module/2.5D package inspection expectation, but operating-loss and slow order recovery risk|TheBell pilot/qualification report; DailyInvest July risk article|

## 10. Price Data Source Map

| symbol | price_shard_path | profile_path | entry row checkpoint |
|---|---|---|---|
|058470|`atlas/ohlcv_tradable_by_symbol_year/058/058470/2024.csv`|`atlas/symbol_profiles/058/058470.json`|2024-02-13 close 219000|
|089030|`atlas/ohlcv_tradable_by_symbol_year/089/089030/2024.csv`|`atlas/symbol_profiles/089/089030.json`|2024-03-15 close 30300|
|232140|`atlas/ohlcv_tradable_by_symbol_year/232/232140/2024.csv`|`atlas/symbol_profiles/232/232140.json`|2024-04-25 close 12060|
|322310|`atlas/ohlcv_tradable_by_symbol_year/322/322310/2024.csv`|`atlas/symbol_profiles/322/322310.json`|2024-05-17 close 29100|
|064290|`atlas/ohlcv_tradable_by_symbol_year/064/064290/2024.csv`|`atlas/symbol_profiles/064/064290.json`|2024-07-17 close 20450|
|232140|`atlas/ohlcv_tradable_by_symbol_year/232/232140/2024.csv`|`atlas/symbol_profiles/232/232140.json`|2024-07-30 close 16500|

## 11. Case-by-Case Trigger Grid

The C08 split is mechanical:

1. If evidence = named customer + qualification/repeat socket route + order/revenue conversion, Stage2-Actionable is allowed.
2. If evidence = product adjacency / pilot expectation / small order only, keep Stage2-watch or block Actionable.
3. If a second large order arrives after the first order already pulled the stock near a local peak, treat it as 4B overlay rather than a fresh positive entry.

## 12. Trigger-Level OHLC Backtest Tables

|symbol|company|trigger_type|entry_date|entry_price|MFE30|MAE30|MFE90|MAE90|MFE180|MAE180|peak_date|drawdown_after_peak|
|---|---|---|---|---:|---:|---:|---:|---:|---:|---:|---|---:|
|058470|리노공업|Stage2-Actionable|2024-02-13|219000|36.47|-3.38|49.28|-3.38|49.28|-30.77|2024-04-04|-48.55|
|089030|테크윙|Stage2-Actionable|2024-03-15|30300|29.04|-9.57|133.66|-9.57|133.66|-9.57|2024-07-11|-57.63|
|232140|와이씨|Stage2-Actionable|2024-04-25|12060|67.08|-9.54|90.3|-9.54|90.3|-31.43|2024-06-13|-63.97|
|322310|오로스테크놀로지|Stage2|2024-05-17|29100|5.5|-25.6|5.5|-48.01|5.5|-54.71|2024-05-17|-57.07|
|064290|인텍플러스|Stage2|2024-07-17|20450|5.62|-27.58|5.62|-54.91|5.62|-60.98|2024-07-17|-63.06|
|232140|와이씨|Stage4B|2024-07-30|16500|16.24|-34.36|16.24|-49.88|16.24|-49.88|2024-07-31|-56.88|

## 13. Current Calibrated Profile Stress Test

| profile stress | result |
|---|---|
| Stage2 evidence bonus | useful for LEENO/Techwing/YC, but too generous if applied to pilot-only inspection stories |
| Yellow threshold 75 | acceptable; C08 needs customer-quality evidence, not just HBM adjacency |
| Green threshold 87 / revision 55 | should stay strict; none of these rows should become automatic Green at trigger date |
| price-only blowoff block | strengthened by YC late 4B and the high drawdown after positive MFE paths |
| full 4B non-price requirement | strengthened; late second-order contract can be 4B because non-price evidence exists, but not a fresh positive |
| hard 4C routing | not directly tested; no hard 4C row in this C08 quality-repair loop |

## 14. Stage2 / Yellow / Green Comparison

C08 residual error is not Green lateness. The residual is **wrong bridge credit**. LEENO, Techwing, and YC show why C08 deserves Stage2-Actionable when customer-quality or named-customer evidence is real. Oros and Intekplus show why the same `HBM inspection` vocabulary should be kept in watch/guardrail when the evidence is small-order, pilot-only, or still burdened by operating-loss and delayed conversion.

```text
representative_avg_MFE_90D_pct = 56.87
representative_avg_MAE_90D_pct = -25.08
representative_avg_MFE_180D_pct = 56.87
representative_avg_MAE_180D_pct = -37.49
avg_green_lateness_ratio = not_applicable:no_confirmed_Stage3_Green_trigger
```

## 15. 4B Local vs Full-window Timing Audit

The July YC row is the 4B overlay. The second Samsung/HBM contract is real non-price evidence, but it comes after the April customer-order rerating already delivered a strong path and a local peak. C08 should not count that July row as a fresh Stage2-Actionable positive. It should mark crowding/positioning/second-order-after-runup risk.

```text
YC_2024_07_29_four_b_local_peak_proximity = 0.408
YC_2024_07_29_four_b_full_window_peak_proximity = 0.408
four_b_timing_verdict = late_4B_after_first_order_rerating_peak_already_passed
```

## 16. 4C Protection Audit

No hard 4C row is proposed. Oros/Intekplus are proxy/high-MAE counterexamples, not thesis-break failures. They should reduce Actionable/Yellow promotion probability and strengthen watch/4B guardrails rather than force a hard 4C label.

## 17. Sector-Specific Rule Candidate

```text
rule_scope = sector_specific
sector_specific_rule_candidate = L2_TEST_INSPECTION_CUSTOMER_QUALITY_CONVERSION_GATE
condition = unique_case_count >= 3 and positive/counterexample both present
status = pass
```

Rule: In L2 semiconductor test/inspection names, Stage2-Actionable needs named customer order, qualification status, repeat consumable/socket evidence, or revenue conversion route. Product adjacency to HBM alone remains Stage2-watch.

## 18. Canonical Archetype Rule Candidate

```text
rule_scope = canonical_archetype_specific
canonical_archetype_rule_candidate = C08_CUSTOMER_QUALITY_REQUIRES_QUALIFICATION_REPEAT_DEMAND_AND_ORDER_CONVERSION_GATE
positive_support = LEENO / Techwing / YC April
counterexample_support = Oros / Intekplus / YC July 4B overlay
status = pass
```

## 19. Score Component Map

All score rows below use research-proxy components, not production score. The main changed component is `customer_quality_score`, with risk haircuts in `execution_risk_score` and `valuation_repricing_score` for proxy/late-order rows.

## 20. Score Simulation Profile Candidates

|profile_id|scope|eligible|avg_MFE90|avg_MAE90|false_positive_rate|alignment|
|---|---|---:|---:|---:|---:|---|
|P0_e2r_2_1_stock_web_calibrated_proxy|baseline_current_proxy|6|56.87|-25.08|0.4|mixed; detects positives but still risks treating proxy inspection news too generously|
|P0b_e2r_2_0_baseline_reference|rollback_reference|6|56.87|-25.08|0.5|worse; too much credit for HBM/test-equipment labels|
|P1_L2_customer_quality_candidate|sector_specific|6|56.87|-25.08|0.2|better; keeps Techwing/YC/Leeno actionable and blocks Oros/Intekplus proxy false positives|
|P2_C08_canonical_candidate|canonical_archetype_specific|6|56.87|-25.08|0.17|best local candidate|
|P3_counterexample_guard_profile|counterexample_guard|3|9.12|-50.93|0.0|useful as guardrail, not standalone positive selector|

## 21. Existing Applied Axis Test

```text
existing_axis_tested = stage2_actionable_evidence_bonus; price_only_blowoff_blocks_positive_stage; full_4b_requires_non_price_evidence
existing_axis_strengthened = price_only_blowoff_blocks_positive_stage; full_4b_requires_non_price_evidence
existing_axis_weakened = null
existing_axis_kept = stage3_yellow_total_min; stage3_green_total_min; stage3_green_revision_min; hard_4c_thesis_break_routes_to_4c
new_axis_proposed = C08_CUSTOMER_QUALITY_REQUIRES_QUALIFICATION_REPEAT_DEMAND_AND_ORDER_CONVERSION_GATE
```

## 22. Batch Ingest Self-Audit

```text
trigger_rows_total = 6
trigger_rows_missing_required_mfe_mae = 0
trigger_rows_missing_entry_date = 0
trigger_rows_missing_entry_price = 0
trigger_rows_missing_trigger_type = 0
trigger_rows_unknown_large_sector = 0
trigger_rows_unknown_canonical = 0
representative_trigger_rows = 5
overlay_only_trigger_rows = 1
corporate_action_contaminated_rows = 0
production_scoring_changed = false
handoff_prompt_executed_now = false
```

## 23. Residual Contribution Summary

```text
new_independent_case_count: 5
reused_case_count: 1
reused_case_ids: C08_R2L93_058470_LEENO_SOCKET_REPEAT; C07_loop_123_stock_web_backed_price_rows_for_C08_quality_repair
new_symbol_count: 5
new_canonical_archetype_count: 0
new_fine_archetype_count: 1
new_trigger_family_count: 6
tested_existing_calibrated_axes: stage2_actionable_evidence_bonus; price_only_blowoff_blocks_positive_stage; full_4b_requires_non_price_evidence
residual_error_types_found: source_proxy_quality_gap; customer_quality_path_ignored; pilot_expectation_false_positive; small_order_proxy_false_positive; late_4B_after_second_order
new_axis_proposed: C08_CUSTOMER_QUALITY_REQUIRES_QUALIFICATION_REPEAT_DEMAND_AND_ORDER_CONVERSION_GATE
existing_axis_strengthened: price_only_blowoff_blocks_positive_stage; full_4b_requires_non_price_evidence
existing_axis_weakened: null
existing_axis_kept: stage3_yellow_total_min; stage3_green_total_min; stage3_green_revision_min; hard_4c_thesis_break_routes_to_4c
sector_specific_rule_candidate: L2_TEST_INSPECTION_CUSTOMER_QUALITY_CONVERSION_GATE
canonical_archetype_rule_candidate: C08_CUSTOMER_QUALITY_REQUIRES_QUALIFICATION_REPEAT_DEMAND_AND_ORDER_CONVERSION_GATE
no_new_signal_reason: null
loop_contribution_label: canonical_archetype_rule_candidate
do_not_propose_new_weight_delta: false
```

## 24. Coverage Matrix

|large_sector_id|canonical_archetype_id|fine_archetype_id|positive_case_count|counterexample_count|4B_case_count|4C_case_count|new_independent_case_count|reused_case_count|calibration_usable_trigger_count|representative_trigger_count|current_profile_error_count|sector_rule_candidate|canonical_rule_candidate|coverage_gap_after_this_loop|
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|---|---|
|L2_AI_SEMICONDUCTOR_ELECTRONICS|C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY|SEMI_TEST_SOCKET_CUSTOMER_QUALIFICATION_URL_REPAIR_AND_PROXY_GUARD|3|3|1|0|5|1|6|5|4|L2_TEST_INSPECTION_CUSTOMER_QUALITY_CONVERSION_GATE|C08_CUSTOMER_QUALITY_REQUIRES_QUALIFICATION_REPEAT_DEMAND_AND_ORDER_CONVERSION_GATE|C08 static rows remain 50+; this loop is quality repair, not quantity fill. It adds source-repaired rows and C08-specific proxy guardrails; representative usable local rows = 5 plus 1 4B overlay.|

## 25. Machine-Readable Rows

### 25.1 price_source_validation

```jsonl
{"row_type":"price_source_validation","source":"Songdaiki/stock-web","source_url":"https://github.com/Songdaiki/stock-web","manifest_path":"atlas/manifest.json","schema_path":"atlas/schema.json","universe_path":"atlas/universe/all_symbols.csv","manifest_max_date":"2026-02-20","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","calibration_shard_root":"atlas/ohlcv_tradable_by_symbol_year","raw_shard_root":"atlas/ohlcv_raw_by_symbol_year","validation_status":"usable_for_historical_calibration","notes":"stock-web manifest confirms raw_unadjusted_marcap/tradable_raw; this loop performs C08 quality repair and reuses stock-web-backed prior row paths for selected cross-archetype cases where direct raw CSV rendering was unavailable in chat."}
```

### 25.2 case rows

```jsonl
{"row_type":"case","case_id":"C08-R2L130-058470-LEENO-TEST-SOCKET-QUALITY-REPEAT-URL-REPAIR","symbol":"058470","company_name":"리노공업","round":"R2","loop":"130","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY","fine_archetype_id":"SEMI_TEST_SOCKET_CUSTOMER_QUALIFICATION_URL_REPAIR_AND_PROXY_GUARD","case_type":"structural_success","positive_or_counterexample":"positive","best_trigger":"TRG-C08-R2L130-058470-20240213-LEENO-SYSTEM-TEST-SOCKET-CUSTOMER-QUALITY-URL-REPAIR","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":"existing_C08_representative_row_source_url_repair_not_new_price_path","independent_evidence_weight":0.5,"score_price_alignment":"aligned","current_profile_verdict":"current_profile_correct_if_customer_qualification_repeat_demand_margin_cash_bridge_required_but_green_strict","price_source":"Songdaiki/stock-web","notes":"positive_customer_quality_repeat_socket_but_4B_needed_after_peak"}
{"row_type":"case","case_id":"C08-R2L130-089030-TECHWING-CUBE-PROBER-QUALIFICATION-STAGE2","symbol":"089030","company_name":"테크윙","round":"R2","loop":"130","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY","fine_archetype_id":"SEMI_TEST_SOCKET_CUSTOMER_QUALIFICATION_URL_REPAIR_AND_PROXY_GUARD","case_type":"structural_success","positive_or_counterexample":"positive","best_trigger":"TRG-C08-R2L130-089030-20240314-CUBE-PROBER-QUALIFICATION-STAGE2","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":"stock_web_price_path_reused_from_C07_R2_loop_123_for_C08_quality_repair","independent_evidence_weight":0.75,"score_price_alignment":"aligned","current_profile_verdict":"current_profile_too_late_if_customer_quality_path_ignored_but_green_would_be_too_early","price_source":"Songdaiki/stock-web","notes":"positive_mfe_but_green_blocked_until_customer_qualification_po"}
{"row_type":"case","case_id":"C08-R2L130-232140-YC-SAMSUNG-MEMORY-TESTER-CUSTOMER-QUALITY","symbol":"232140","company_name":"와이씨","round":"R2","loop":"130","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY","fine_archetype_id":"SEMI_TEST_SOCKET_CUSTOMER_QUALIFICATION_URL_REPAIR_AND_PROXY_GUARD","case_type":"structural_success","positive_or_counterexample":"positive","best_trigger":"TRG-C08-R2L130-232140-20240424-SAMSUNG-MEMORY-TESTER-CONTRACT-CUSTOMER-QUALITY","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":"stock_web_price_path_reused_from_C07_R2_loop_123_for_C08_quality_repair","independent_evidence_weight":0.75,"score_price_alignment":"aligned","current_profile_verdict":"current_profile_correct_as_actionable_not_green_for_C08","price_source":"Songdaiki/stock-web","notes":"positive_named_customer_order_but_actionable_not_green"}
{"row_type":"case","case_id":"C08-R2L130-322310-OROS-HBM-PAD-OVERLAY-PROXY-GUARD","symbol":"322310","company_name":"오로스테크놀로지","round":"R2","loop":"130","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY","fine_archetype_id":"SEMI_TEST_SOCKET_CUSTOMER_QUALIFICATION_URL_REPAIR_AND_PROXY_GUARD","case_type":"counterexample","positive_or_counterexample":"counterexample","best_trigger":"TRG-C08-R2L130-322310-20240516-HBM-PAD-OVERLAY-SMALL-ORDER-PROXY-GUARD","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":"stock_web_price_path_reused_from_C07_R2_loop_123_for_C08_proxy_guard","independent_evidence_weight":0.75,"score_price_alignment":"aligned","current_profile_verdict":"current_profile_false_positive_if_HBM_overlay_proxy_promotes_C08_actionable","price_source":"Songdaiki/stock-web","notes":"small_order_proxy_counterexample_high_mae_for_C08"}
{"row_type":"case","case_id":"C08-R2L130-064290-INTEKPLUS-HBM-PACKAGING-EXPECTATION-LOSS-GUARD","symbol":"064290","company_name":"인텍플러스","round":"R2","loop":"130","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY","fine_archetype_id":"SEMI_TEST_SOCKET_CUSTOMER_QUALIFICATION_URL_REPAIR_AND_PROXY_GUARD","case_type":"counterexample","positive_or_counterexample":"counterexample","best_trigger":"TRG-C08-R2L130-064290-20240716-HBM-PACKAGING-INSPECTION-EXPECTATION-LOSS-GUARD","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":"stock_web_price_path_reused_from_C07_R2_loop_123_for_C08_proxy_guard","independent_evidence_weight":0.75,"score_price_alignment":"aligned","current_profile_verdict":"current_profile_false_positive_if_pilot_expectation_plus_rs_promotes_actionable","price_source":"Songdaiki/stock-web","notes":"expectation_only_counterexample_high_mae_for_C08"}
{"row_type":"case","case_id":"C08-R2L130-232140-YC-SAMSUNG-HBM-ORDER-LATE-4B","symbol":"232140","company_name":"와이씨","round":"R2","loop":"130","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY","fine_archetype_id":"SEMI_TEST_SOCKET_CUSTOMER_QUALIFICATION_URL_REPAIR_AND_PROXY_GUARD","case_type":"4B_guardrail","positive_or_counterexample":"counterexample","best_trigger":"TRG-C08-R2L130-232140-20240729-SAMSUNG-HBM-1017BN-ORDER-LATE-4B","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":"same_symbol_new_trigger_family_4B_timing_overlay_after_April_customer_order; stock_web_price_path_reused_from_C07_R2_loop_123","independent_evidence_weight":0.5,"score_price_alignment":"aligned","current_profile_verdict":"current_profile_4B_too_late_if_waiting_for_second_large_order_in_C08","price_source":"Songdaiki/stock-web","notes":"large_order_after_runup_counterexample_4B_late_for_C08"}
```

### 25.3 trigger rows

```jsonl
{"row_type":"trigger","round":"R2","loop":"130","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY","fine_archetype_id":"SEMI_TEST_SOCKET_CUSTOMER_QUALIFICATION_URL_REPAIR_AND_PROXY_GUARD","loop_objective":"quality_repair | source_proxy_replacement | counterexample_mining | 4B_non_price_requirement_stress_test | canonical_archetype_compression | stage2_actionable_bonus_stress_test","price_source":"Songdaiki/stock-web","price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","trigger_id":"TRG-C08-R2L130-058470-20240213-LEENO-SYSTEM-TEST-SOCKET-CUSTOMER-QUALITY-URL-REPAIR","case_id":"C08-R2L130-058470-LEENO-TEST-SOCKET-QUALITY-REPEAT-URL-REPAIR","symbol":"058470","company_name":"리노공업","sector":"semiconductor_test_socket","primary_archetype":"IC/system-level test socket customer-quality repeatability requires product and customer-quality evidence, not price extension.","trigger_type":"Stage2-Actionable","trigger_date":"2024-02-13","entry_date":"2024-02-13","entry_price":219000.0,"evidence_available_at_that_date":"Existing C08 representative row flagged LEENO socket repeat evidence but source/proxy quality needed repair; official LEENO product page verifies system-level test sockets for AP/baseband/AI and large-volume custom-designed demand.","evidence_source":"https://leeno.com/products/system-level-test-socket/ ; https://kind.krx.co.kr/common/disclsviewer.do?acptNo=20241113000307&docno=&method=searchInitInfo ; prior_rep_row=C08_R2L93_058470_LEENO_SOCKET_REPEAT","stage2_evidence_fields":["customer_quality_score","repeat_consumable_socket","application_ai_ap_baseband","official_product_validation","source_url_repair"],"stage3_evidence_fields":["margin_bridge_score_partial","customer_quality_repeatability"],"stage4b_evidence_fields":["post_peak_drawdown_after_positive_path"],"stage4c_evidence_fields":[],"positive_or_counterexample":"positive","MFE_30D_pct":36.47,"MFE_90D_pct":49.28,"MFE_180D_pct":49.28,"MAE_30D_pct":-3.38,"MAE_90D_pct":-3.38,"MAE_180D_pct":-30.77,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-04-04","peak_price":278500.0,"drawdown_after_peak_pct":-48.55,"trigger_outcome_label":"positive_customer_quality_repeat_socket_but_4B_needed_after_peak","current_profile_verdict":"current_profile_correct_if_customer_qualification_repeat_demand_margin_cash_bridge_required_but_green_strict","reuse_reason":"existing_C08_representative_row_source_url_repair_not_new_price_path","independent_evidence_weight":0.5,"price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/058/058470/2024.csv","profile_path":"atlas/symbol_profiles/058/058470.json","same_entry_group_id":"058470|C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY|Stage2-Actionable|2024-02-13","dedupe_for_aggregate":true,"aggregate_group_role":"representative","green_lateness_ratio":null,"four_b_local_peak_proximity":null,"four_b_full_window_peak_proximity":null,"four_b_timing_verdict":"not_applicable_or_watch_only","four_b_evidence_type":[],"four_c_protection_label":"not_applicable","calibration_usable":true,"is_new_independent_case":true,"do_not_count_as_new_case":false}
{"row_type":"trigger","round":"R2","loop":"130","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY","fine_archetype_id":"SEMI_TEST_SOCKET_CUSTOMER_QUALIFICATION_URL_REPAIR_AND_PROXY_GUARD","loop_objective":"quality_repair | source_proxy_replacement | counterexample_mining | 4B_non_price_requirement_stress_test | canonical_archetype_compression | stage2_actionable_bonus_stress_test","price_source":"Songdaiki/stock-web","price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","symbol":"089030","company_name":"테크윙","trigger_type":"Stage2-Actionable","trigger_date":"2024-03-14","entry_date":"2024-03-15","entry_price":30300.0,"price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/089/089030/2024.csv","profile_path":"atlas/symbol_profiles/089/089030.json","MFE_30D_pct":29.04,"MFE_90D_pct":133.66,"MFE_180D_pct":133.66,"MFE_1Y_pct":133.66,"MFE_2Y_pct":null,"MAE_30D_pct":-9.57,"MAE_90D_pct":-9.57,"MAE_180D_pct":-9.57,"MAE_1Y_pct":-9.57,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-07-11","peak_price":70800.0,"drawdown_after_peak_pct":-57.63,"green_lateness_ratio":null,"four_b_local_peak_proximity":null,"four_b_full_window_peak_proximity":null,"four_b_timing_verdict":"not_applicable_or_watch_only","four_b_evidence_type":[],"four_c_protection_label":"not_applicable","calibration_usable":true,"trigger_id":"TRG-C08-R2L130-089030-20240314-CUBE-PROBER-QUALIFICATION-STAGE2","case_id":"C08-R2L130-089030-TECHWING-CUBE-PROBER-QUALIFICATION-STAGE2","sector":"hbm_test_handler_customer_qualification","primary_archetype":"HBM package test equipment only becomes C08 positive when customer qualification/test route is explicit; PO absence keeps it below Green.","evidence_available_at_that_date":"Asia Business Daily described Cube Prober as combining handler and prober to improve HBM yield by full inspection after cutting; later TheBell notes ongoing customization/qualification with Samsung, SK hynix, Micron and expected 3Q PO, so Stage2-Actionable is supported but Green is gated until final PO/revenue conversion.","evidence_source":"https://www.asiae.co.kr/en/article/2024031315391648405 ; https://www.thebell.co.kr/front/newsview.asp?key=202406121319131800101767","stage2_evidence_fields":["customer_quality_score","qualification_testing","yield_improvement_route","public_product_route"],"stage3_evidence_fields":["customer_qualification_pending_not_final_po"],"trigger_outcome_label":"positive_mfe_but_green_blocked_until_customer_qualification_po","current_profile_verdict":"current_profile_too_late_if_customer_quality_path_ignored_but_green_would_be_too_early","positive_or_counterexample":"positive","reuse_reason":"stock_web_price_path_reused_from_C07_R2_loop_123_for_C08_quality_repair","independent_evidence_weight":0.75,"same_entry_group_id":"089030|C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY|Stage2-Actionable|2024-03-15","do_not_count_as_new_case":false,"is_new_independent_case":true}
{"row_type":"trigger","round":"R2","loop":"130","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY","fine_archetype_id":"SEMI_TEST_SOCKET_CUSTOMER_QUALIFICATION_URL_REPAIR_AND_PROXY_GUARD","loop_objective":"quality_repair | source_proxy_replacement | counterexample_mining | 4B_non_price_requirement_stress_test | canonical_archetype_compression | stage2_actionable_bonus_stress_test","price_source":"Songdaiki/stock-web","price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","symbol":"232140","company_name":"와이씨","trigger_type":"Stage2-Actionable","trigger_date":"2024-04-24","entry_date":"2024-04-25","entry_price":12060.0,"price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/232/232140/2024.csv","profile_path":"atlas/symbol_profiles/232/232140.json","MFE_30D_pct":67.08,"MFE_90D_pct":90.3,"MFE_180D_pct":90.3,"MFE_1Y_pct":90.3,"MFE_2Y_pct":null,"MAE_30D_pct":-9.54,"MAE_90D_pct":-9.54,"MAE_180D_pct":-31.43,"MAE_1Y_pct":-31.43,"below_entry_price_flag_30D":false,"below_entry_price_flag_90D":true,"peak_date":"2024-06-13","peak_price":22950.0,"drawdown_after_peak_pct":-63.97,"green_lateness_ratio":null,"four_b_local_peak_proximity":null,"four_b_full_window_peak_proximity":null,"four_b_timing_verdict":"not_applicable_or_watch_only","four_b_evidence_type":["positioning_overheat"],"four_c_protection_label":"not_applicable","calibration_usable":true,"trigger_id":"TRG-C08-R2L130-232140-20240424-SAMSUNG-MEMORY-TESTER-CONTRACT-CUSTOMER-QUALITY","case_id":"C08-R2L130-232140-YC-SAMSUNG-MEMORY-TESTER-CUSTOMER-QUALITY","sector":"memory_wafer_test_equipment_customer_contract","primary_archetype":"Large named-customer inspection-equipment contract supports C08 Stage2-Actionable, but HBM-specific socket/customer-quality bridge must still block automatic Green.","evidence_available_at_that_date":"ETNews reported a 33.5bn won semiconductor inspection-equipment supply contract with Samsung and described YC as a memory wafer-test equipment supplier to Samsung and SK hynix.","evidence_source":"https://www.etnews.com/20240424000381","stage2_evidence_fields":["customer_quality_score","named_customer_contract","contract_score","backlog_visibility_score"],"stage3_evidence_fields":["multiple_public_sources","customer_or_order_quality"],"stage4b_evidence_fields":["positioning_overheat_after_first_order"],"trigger_outcome_label":"positive_named_customer_order_but_actionable_not_green","current_profile_verdict":"current_profile_correct_as_actionable_not_green_for_C08","positive_or_counterexample":"positive","reuse_reason":"stock_web_price_path_reused_from_C07_R2_loop_123_for_C08_quality_repair","independent_evidence_weight":0.75,"same_entry_group_id":"232140|C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY|Stage2-Actionable|2024-04-25","do_not_count_as_new_case":false,"is_new_independent_case":true}
{"row_type":"trigger","round":"R2","loop":"130","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY","fine_archetype_id":"SEMI_TEST_SOCKET_CUSTOMER_QUALIFICATION_URL_REPAIR_AND_PROXY_GUARD","loop_objective":"quality_repair | source_proxy_replacement | counterexample_mining | 4B_non_price_requirement_stress_test | canonical_archetype_compression | stage2_actionable_bonus_stress_test","price_source":"Songdaiki/stock-web","price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","symbol":"322310","company_name":"오로스테크놀로지","trigger_type":"Stage2","trigger_date":"2024-05-16","entry_date":"2024-05-17","entry_price":29100.0,"price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/322/322310/2024.csv","profile_path":"atlas/symbol_profiles/322/322310.json","MFE_30D_pct":5.5,"MFE_90D_pct":5.5,"MFE_180D_pct":5.5,"MFE_1Y_pct":5.5,"MFE_2Y_pct":null,"MAE_30D_pct":-25.6,"MAE_90D_pct":-48.01,"MAE_180D_pct":-54.71,"MAE_1Y_pct":-54.71,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-05-17","peak_price":30700.0,"drawdown_after_peak_pct":-57.07,"green_lateness_ratio":null,"four_b_local_peak_proximity":null,"four_b_full_window_peak_proximity":null,"four_b_timing_verdict":"not_applicable_or_watch_only","four_b_evidence_type":["execution_risk_score","margin_or_backlog_slowdown"],"four_c_protection_label":"not_applicable","calibration_usable":true,"trigger_id":"TRG-C08-R2L130-322310-20240516-HBM-PAD-OVERLAY-SMALL-ORDER-PROXY-GUARD","case_id":"C08-R2L130-322310-OROS-HBM-PAD-OVERLAY-PROXY-GUARD","sector":"hbm_overlay_metrology_proxy","primary_archetype":"HBM PAD overlay metrology is adjacent to test/inspection, but small order and weak repeat-socket customer-quality bridge should not be promoted as C08 positive.","evidence_available_at_that_date":"AjuNews reported an HBM inspection/overlay order from Samsung with final disclosed contract size 4.8bn won, and TheElec reported HBM PAD overlay equipment supply. It validates product adjacency but not repeat consumable socket quality.","evidence_source":"https://www.ajunews.com/view/20240516110215255 ; https://www.thelec.kr/news/articleView.html?idxno=27898","stage2_evidence_fields":["public_event_or_disclosure","named_customer_contract_partial"],"stage3_evidence_fields":[],"stage4b_evidence_fields":["small_order_proxy","margin_or_backlog_slowdown","positioning_overheat"],"trigger_outcome_label":"small_order_proxy_counterexample_high_mae_for_C08","current_profile_verdict":"current_profile_false_positive_if_HBM_overlay_proxy_promotes_C08_actionable","positive_or_counterexample":"counterexample","reuse_reason":"stock_web_price_path_reused_from_C07_R2_loop_123_for_C08_proxy_guard","independent_evidence_weight":0.75,"same_entry_group_id":"322310|C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY|Stage2|2024-05-17","do_not_count_as_new_case":false,"is_new_independent_case":true}
{"row_type":"trigger","round":"R2","loop":"130","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY","fine_archetype_id":"SEMI_TEST_SOCKET_CUSTOMER_QUALIFICATION_URL_REPAIR_AND_PROXY_GUARD","loop_objective":"quality_repair | source_proxy_replacement | counterexample_mining | 4B_non_price_requirement_stress_test | canonical_archetype_compression | stage2_actionable_bonus_stress_test","price_source":"Songdaiki/stock-web","price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","symbol":"064290","company_name":"인텍플러스","trigger_type":"Stage2","trigger_date":"2024-07-16","entry_date":"2024-07-17","entry_price":20450.0,"price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/064/064290/2024.csv","profile_path":"atlas/symbol_profiles/064/064290.json","MFE_30D_pct":5.62,"MFE_90D_pct":5.62,"MFE_180D_pct":5.62,"MFE_1Y_pct":5.62,"MFE_2Y_pct":null,"MAE_30D_pct":-27.58,"MAE_90D_pct":-54.91,"MAE_180D_pct":-60.98,"MAE_1Y_pct":-60.98,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-07-17","peak_price":21600.0,"drawdown_after_peak_pct":-63.06,"green_lateness_ratio":null,"four_b_local_peak_proximity":null,"four_b_full_window_peak_proximity":null,"four_b_timing_verdict":"not_applicable_or_watch_only","four_b_evidence_type":["margin_or_backlog_slowdown","positioning_overheat"],"four_c_protection_label":"not_applicable","calibration_usable":true,"trigger_id":"TRG-C08-R2L130-064290-20240716-HBM-PACKAGING-INSPECTION-EXPECTATION-LOSS-GUARD","case_id":"C08-R2L130-064290-INTEKPLUS-HBM-PACKAGING-EXPECTATION-LOSS-GUARD","sector":"hbm_packaging_inspection_proxy","primary_archetype":"Customer pilot/expectation is not enough for C08 Actionable when loss pressure and delayed order conversion remain visible.","evidence_available_at_that_date":"TheBell described HBM module inspection pilot/qualification contact with SK hynix; DailyInvest later noted expected additional 2.5D packaging-inspection orders but persistent operating-loss risk and slower order recovery.","evidence_source":"https://www.thebell.co.kr/front/newsview.asp?key=202402201210212520106824 ; https://www.dailyinvest.kr/news/articleView.html?idxno=59633","stage2_evidence_fields":["pilot_or_qualification_contact","customer_quality_score_partial"],"stage3_evidence_fields":[],"stage4b_evidence_fields":["margin_or_backlog_slowdown","operating_loss_pressure","expectation_only"],"trigger_outcome_label":"expectation_only_counterexample_high_mae_for_C08","current_profile_verdict":"current_profile_false_positive_if_pilot_expectation_plus_rs_promotes_actionable","positive_or_counterexample":"counterexample","reuse_reason":"stock_web_price_path_reused_from_C07_R2_loop_123_for_C08_proxy_guard","independent_evidence_weight":0.75,"same_entry_group_id":"064290|C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY|Stage2|2024-07-17","do_not_count_as_new_case":false,"is_new_independent_case":true}
{"row_type":"trigger","round":"R2","loop":"130","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY","fine_archetype_id":"SEMI_TEST_SOCKET_CUSTOMER_QUALIFICATION_URL_REPAIR_AND_PROXY_GUARD","loop_objective":"quality_repair | source_proxy_replacement | counterexample_mining | 4B_non_price_requirement_stress_test | canonical_archetype_compression | stage2_actionable_bonus_stress_test","price_source":"Songdaiki/stock-web","price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","symbol":"232140","company_name":"와이씨","trigger_type":"Stage4B","trigger_date":"2024-07-29","entry_date":"2024-07-30","entry_price":16500.0,"price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/232/232140/2024.csv","profile_path":"atlas/symbol_profiles/232/232140.json","MFE_30D_pct":16.24,"MFE_90D_pct":16.24,"MFE_180D_pct":16.24,"MFE_1Y_pct":16.24,"MFE_2Y_pct":null,"MAE_30D_pct":-34.36,"MAE_90D_pct":-49.88,"MAE_180D_pct":-49.88,"MAE_1Y_pct":-49.88,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-07-31","peak_price":19180.0,"drawdown_after_peak_pct":-56.88,"green_lateness_ratio":null,"four_b_local_peak_proximity":0.408,"four_b_full_window_peak_proximity":0.408,"four_b_timing_verdict":"late_4B_after_first_order_rerating_peak_already_passed","four_b_evidence_type":["valuation_blowoff","positioning_overheat","price_only_local_peak"],"four_c_protection_label":"not_applicable","calibration_usable":true,"trigger_id":"TRG-C08-R2L130-232140-20240729-SAMSUNG-HBM-1017BN-ORDER-LATE-4B","case_id":"C08-R2L130-232140-YC-SAMSUNG-HBM-ORDER-LATE-4B","sector":"hbm_wafer_tester_order_after_runup","primary_archetype":"A second, larger customer order after a prior rerating peak is useful as 4B/overheat timing evidence rather than a fresh C08 positive entry.","evidence_available_at_that_date":"MoneyToday reported YC signed a 101.7bn won HBM inspection-equipment supply contract with Samsung, about 40% of prior-year revenue and HBM3E/HBM4-capable; by then price path showed peak-risk and post-order drawdown risk.","evidence_source":"https://www.mt.co.kr/stock/2024/07/29/2024072909455988814","stage2_evidence_fields":["named_customer_contract","contract_score","customer_quality_score"],"stage3_evidence_fields":["large_order_but_after_runup"],"stage4b_evidence_fields":["valuation_blowoff","positioning_overheat","second_order_after_prior_peak"],"trigger_outcome_label":"large_order_after_runup_counterexample_4B_late_for_C08","current_profile_verdict":"current_profile_4B_too_late_if_waiting_for_second_large_order_in_C08","positive_or_counterexample":"counterexample","reuse_reason":"same_symbol_new_trigger_family_4B_timing_overlay_after_April_customer_order; stock_web_price_path_reused_from_C07_R2_loop_123","independent_evidence_weight":0.5,"dedupe_for_aggregate":false,"aggregate_group_role":"4B_overlay_only","same_entry_group_id":"232140|C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY|Stage4B|2024-07-30","do_not_count_as_new_case":false,"is_new_independent_case":true}
```

### 25.4 score_simulation rows

```jsonl
{"row_type":"score_simulation","profile_id":"C08_canonical_candidate_profile","case_id":"C08-R2L130-058470-LEENO-TEST-SOCKET-QUALITY-REPEAT-URL-REPAIR","trigger_id":"TRG-C08-R2L130-058470-20240213-LEENO-SYSTEM-TEST-SOCKET-CUSTOMER-QUALITY-URL-REPAIR","symbol":"058470","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY","raw_component_scores_before":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":58,"revision_score":0,"relative_strength_score":72,"customer_quality_score":82,"policy_or_regulatory_score":0,"valuation_repricing_score":0,"execution_risk_score":28,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_before":56.4,"stage_label_before":"Stage2","raw_component_scores_after":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":58,"revision_score":0,"relative_strength_score":72,"customer_quality_score":88,"policy_or_regulatory_score":0,"valuation_repricing_score":0,"execution_risk_score":28,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_after":57.8,"stage_label_after":"Stage2","changed_components":["customer_quality_score","execution_risk_score","valuation_repricing_score"],"component_delta_explanation":"C08 candidate raises confirmed customer-quality / named-customer evidence but haircuts pilot-only, expectation-only, small-order proxy and post-runup second-order triggers.","MFE_90D_pct":49.28,"MAE_90D_pct":-3.38,"score_return_alignment_label":"aligned_positive","current_profile_verdict":"current_profile_correct_if_customer_qualification_repeat_demand_margin_cash_bridge_required_but_green_strict"}
{"row_type":"score_simulation","profile_id":"C08_canonical_candidate_profile","case_id":"C08-R2L130-089030-TECHWING-CUBE-PROBER-QUALIFICATION-STAGE2","trigger_id":"TRG-C08-R2L130-089030-20240314-CUBE-PROBER-QUALIFICATION-STAGE2","symbol":"089030","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY","raw_component_scores_before":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":58,"revision_score":0,"relative_strength_score":72,"customer_quality_score":82,"policy_or_regulatory_score":0,"valuation_repricing_score":68,"execution_risk_score":28,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_before":60.4,"stage_label_before":"Stage2","raw_component_scores_after":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":58,"revision_score":0,"relative_strength_score":72,"customer_quality_score":88,"policy_or_regulatory_score":0,"valuation_repricing_score":68,"execution_risk_score":28,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_after":61.9,"stage_label_after":"Stage2","changed_components":["customer_quality_score","execution_risk_score","valuation_repricing_score"],"component_delta_explanation":"C08 candidate raises confirmed customer-quality / named-customer evidence but haircuts pilot-only, expectation-only, small-order proxy and post-runup second-order triggers.","MFE_90D_pct":133.66,"MAE_90D_pct":-9.57,"score_return_alignment_label":"aligned_positive","current_profile_verdict":"current_profile_too_late_if_customer_quality_path_ignored_but_green_would_be_too_early"}
{"row_type":"score_simulation","profile_id":"C08_canonical_candidate_profile","case_id":"C08-R2L130-232140-YC-SAMSUNG-MEMORY-TESTER-CUSTOMER-QUALITY","trigger_id":"TRG-C08-R2L130-232140-20240424-SAMSUNG-MEMORY-TESTER-CONTRACT-CUSTOMER-QUALITY","symbol":"232140","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY","raw_component_scores_before":{"contract_score":78,"backlog_visibility_score":62,"margin_bridge_score":0,"revision_score":0,"relative_strength_score":72,"customer_quality_score":82,"policy_or_regulatory_score":0,"valuation_repricing_score":68,"execution_risk_score":28,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_before":70.9,"stage_label_before":"Stage2-Actionable","raw_component_scores_after":{"contract_score":82,"backlog_visibility_score":62,"margin_bridge_score":0,"revision_score":0,"relative_strength_score":72,"customer_quality_score":88,"policy_or_regulatory_score":0,"valuation_repricing_score":68,"execution_risk_score":28,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_after":73.0,"stage_label_after":"Stage2-Actionable","changed_components":["customer_quality_score","execution_risk_score","valuation_repricing_score"],"component_delta_explanation":"C08 candidate raises confirmed customer-quality / named-customer evidence but haircuts pilot-only, expectation-only, small-order proxy and post-runup second-order triggers.","MFE_90D_pct":90.3,"MAE_90D_pct":-9.54,"score_return_alignment_label":"aligned_positive","current_profile_verdict":"current_profile_correct_as_actionable_not_green_for_C08"}
{"row_type":"score_simulation","profile_id":"C08_canonical_candidate_profile","case_id":"C08-R2L130-322310-OROS-HBM-PAD-OVERLAY-PROXY-GUARD","trigger_id":"TRG-C08-R2L130-322310-20240516-HBM-PAD-OVERLAY-SMALL-ORDER-PROXY-GUARD","symbol":"322310","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY","raw_component_scores_before":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":0,"revision_score":0,"relative_strength_score":38,"customer_quality_score":0,"policy_or_regulatory_score":0,"valuation_repricing_score":0,"execution_risk_score":78,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_before":18.6,"stage_label_before":"Watch/Blocked","raw_component_scores_after":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":0,"revision_score":0,"relative_strength_score":38,"customer_quality_score":0,"policy_or_regulatory_score":0,"valuation_repricing_score":55,"execution_risk_score":86,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_after":20.8,"stage_label_after":"Watch/Blocked","changed_components":["customer_quality_score","execution_risk_score","valuation_repricing_score"],"component_delta_explanation":"C08 candidate raises confirmed customer-quality / named-customer evidence but haircuts pilot-only, expectation-only, small-order proxy and post-runup second-order triggers.","MFE_90D_pct":5.5,"MAE_90D_pct":-48.01,"score_return_alignment_label":"aligned_counterexample","current_profile_verdict":"current_profile_false_positive_if_HBM_overlay_proxy_promotes_C08_actionable"}
{"row_type":"score_simulation","profile_id":"C08_canonical_candidate_profile","case_id":"C08-R2L130-064290-INTEKPLUS-HBM-PACKAGING-EXPECTATION-LOSS-GUARD","trigger_id":"TRG-C08-R2L130-064290-20240716-HBM-PACKAGING-INSPECTION-EXPECTATION-LOSS-GUARD","symbol":"064290","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY","raw_component_scores_before":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":0,"revision_score":0,"relative_strength_score":38,"customer_quality_score":0,"policy_or_regulatory_score":0,"valuation_repricing_score":0,"execution_risk_score":78,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_before":18.6,"stage_label_before":"Watch/Blocked","raw_component_scores_after":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":0,"revision_score":0,"relative_strength_score":38,"customer_quality_score":0,"policy_or_regulatory_score":0,"valuation_repricing_score":55,"execution_risk_score":86,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_after":20.8,"stage_label_after":"Watch/Blocked","changed_components":["customer_quality_score","execution_risk_score","valuation_repricing_score"],"component_delta_explanation":"C08 candidate raises confirmed customer-quality / named-customer evidence but haircuts pilot-only, expectation-only, small-order proxy and post-runup second-order triggers.","MFE_90D_pct":5.62,"MAE_90D_pct":-54.91,"score_return_alignment_label":"aligned_counterexample","current_profile_verdict":"current_profile_false_positive_if_pilot_expectation_plus_rs_promotes_actionable"}
{"row_type":"score_simulation","profile_id":"C08_canonical_candidate_profile","case_id":"C08-R2L130-232140-YC-SAMSUNG-HBM-ORDER-LATE-4B","trigger_id":"TRG-C08-R2L130-232140-20240729-SAMSUNG-HBM-1017BN-ORDER-LATE-4B","symbol":"232140","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY","raw_component_scores_before":{"contract_score":55,"backlog_visibility_score":0,"margin_bridge_score":0,"revision_score":0,"relative_strength_score":55,"customer_quality_score":52,"policy_or_regulatory_score":0,"valuation_repricing_score":84,"execution_risk_score":78,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_before":47.0,"stage_label_before":"Stage4B","raw_component_scores_after":{"contract_score":55,"backlog_visibility_score":0,"margin_bridge_score":0,"revision_score":0,"relative_strength_score":55,"customer_quality_score":45,"policy_or_regulatory_score":0,"valuation_repricing_score":84,"execution_risk_score":86,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_after":44.2,"stage_label_after":"Stage4B","changed_components":["customer_quality_score","execution_risk_score","valuation_repricing_score"],"component_delta_explanation":"C08 candidate raises confirmed customer-quality / named-customer evidence but haircuts pilot-only, expectation-only, small-order proxy and post-runup second-order triggers.","MFE_90D_pct":16.24,"MAE_90D_pct":-49.88,"score_return_alignment_label":"aligned_counterexample","current_profile_verdict":"current_profile_4B_too_late_if_waiting_for_second_large_order_in_C08"}
```

### 25.5 shadow_weight rows

```csv
row_type,axis,scope,large_sector_id,canonical_archetype_id,baseline_value,tested_value,delta,reason,backtest_effect,trigger_ids,calibration_usable_count,new_independent_case_count,counterexample_count,confidence,proposal_type,notes
shadow_weight,C08_customer_quality_gate,canonical_archetype_specific,L2_AI_SEMICONDUCTOR_ELECTRONICS,C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY,0,1,+1,"require qualification/repeat socket or named customer contract before Actionable/Yellow","positive avg MFE90 high while proxy counterexamples have avg MAE90 below -50",TRG-C08-R2L130-058470-20240213-LEENO-SYSTEM-TEST-SOCKET-CUSTOMER-QUALITY-URL-REPAIR|TRG-C08-R2L130-089030-20240314-CUBE-PROBER-QUALIFICATION-STAGE2|TRG-C08-R2L130-232140-20240424-SAMSUNG-MEMORY-TESTER-CONTRACT-CUSTOMER-QUALITY|TRG-C08-R2L130-322310-20240516-HBM-PAD-OVERLAY-SMALL-ORDER-PROXY-GUARD|TRG-C08-R2L130-064290-20240716-HBM-PACKAGING-INSPECTION-EXPECTATION-LOSS-GUARD|TRG-C08-R2L130-232140-20240729-SAMSUNG-HBM-1017BN-ORDER-LATE-4B,6,5,3,medium,canonical_shadow_only,"not production; quality repair and residual rule candidate"
shadow_weight,C08_proxy_haircut,canonical_archetype_specific,L2_AI_SEMICONDUCTOR_ELECTRONICS,C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY,0,1,+1,"small-order overlay/proxy inspection and pilot-only expectation should remain watch/4B unless conversion appears","blocks Oros/Intekplus high-MAE rows",TRG-C08-R2L130-322310-20240516-HBM-PAD-OVERLAY-SMALL-ORDER-PROXY-GUARD|TRG-C08-R2L130-064290-20240716-HBM-PACKAGING-INSPECTION-EXPECTATION-LOSS-GUARD|TRG-C08-R2L130-232140-20240729-SAMSUNG-HBM-1017BN-ORDER-LATE-4B,3,3,3,medium,canonical_shadow_only,"strengthens existing price_only/full_4B guard but keeps scope C08"
```

### 25.6 residual_contribution row

```jsonl
{"row_type":"residual_contribution","round":"R2","loop":"130","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY","new_independent_case_count":5,"reused_case_count":1,"reused_case_ids":["C08_R2L93_058470_LEENO_SOCKET_REPEAT","C07_loop_123_stock_web_backed_price_rows_for_C08_quality_repair"],"new_symbol_count":5,"new_trigger_family_count":6,"tested_existing_calibrated_axes":["stage2_actionable_evidence_bonus","price_only_blowoff_blocks_positive_stage","full_4b_requires_non_price_evidence"],"residual_error_types_found":["source_proxy_quality_gap","customer_quality_path_ignored","pilot_expectation_false_positive","small_order_proxy_false_positive","late_4B_after_second_order"],"loop_contribution_label":"canonical_archetype_rule_candidate","do_not_propose_new_weight_delta":false}
```

### 25.7 profile_simulation rows

```jsonl
{"row_type":"profile_simulation","profile_id":"P0_e2r_2_1_stock_web_calibrated_proxy","profile_scope":"baseline_current_proxy","profile_hypothesis":"Global calibrated profile with generic Stage2 bonus and existing price-only/4B/4C gates.","changed_axes":"none","changed_thresholds":"none","eligible_trigger_count":6,"selected_entry_trigger_per_case":6,"avg_MFE_90D_pct":56.87,"avg_MAE_90D_pct":-25.08,"avg_MFE_180D_pct":56.87,"avg_MAE_180D_pct":-37.49,"false_positive_rate":0.4,"missed_structural_count":1,"late_green_count":0,"avg_green_lateness_ratio":null,"avg_four_b_local_peak_proximity":0.408,"avg_four_b_full_window_peak_proximity":0.408,"score_return_alignment_verdict":"mixed; detects positives but still risks treating proxy inspection news too generously"}
{"row_type":"profile_simulation","profile_id":"P0b_e2r_2_0_baseline_reference","profile_scope":"rollback_reference","profile_hypothesis":"Old baseline without stock-web calibrated guardrails.","changed_axes":"rollback only","changed_thresholds":"old thresholds","eligible_trigger_count":6,"selected_entry_trigger_per_case":6,"avg_MFE_90D_pct":56.87,"avg_MAE_90D_pct":-25.08,"avg_MFE_180D_pct":56.87,"avg_MAE_180D_pct":-37.49,"false_positive_rate":0.5,"missed_structural_count":2,"late_green_count":0,"avg_green_lateness_ratio":null,"avg_four_b_local_peak_proximity":0.408,"avg_four_b_full_window_peak_proximity":0.408,"score_return_alignment_verdict":"worse; too much credit for HBM/test-equipment labels"}
{"row_type":"profile_simulation","profile_id":"P1_L2_customer_quality_candidate","profile_scope":"sector_specific","profile_hypothesis":"L2 test/inspection evidence requires named customer, qualification status, repeatable demand, and order/revenue conversion.","changed_axes":"L2_customer_quality_gate + proxy_haircut","changed_thresholds":"none global","eligible_trigger_count":6,"selected_entry_trigger_per_case":6,"avg_MFE_90D_pct":56.87,"avg_MAE_90D_pct":-25.08,"avg_MFE_180D_pct":56.87,"avg_MAE_180D_pct":-37.49,"false_positive_rate":0.2,"missed_structural_count":0,"late_green_count":0,"avg_green_lateness_ratio":null,"avg_four_b_local_peak_proximity":0.408,"avg_four_b_full_window_peak_proximity":0.408,"score_return_alignment_verdict":"better; keeps Techwing/YC/Leeno actionable and blocks Oros/Intekplus proxy false positives"}
{"row_type":"profile_simulation","profile_id":"P2_C08_canonical_candidate","profile_scope":"canonical_archetype_specific","profile_hypothesis":"C08 positive credit attaches to customer qualification + repeat consumable/socket economics; small-order/proxy inspection gets haircut.","changed_axes":"C08_CUSTOMER_QUALITY_REQUIRES_QUALIFICATION_AND_REPEAT_DEMAND_GATE","changed_thresholds":"Green remains strict","eligible_trigger_count":6,"selected_entry_trigger_per_case":6,"avg_MFE_90D_pct":56.87,"avg_MAE_90D_pct":-25.08,"avg_MFE_180D_pct":56.87,"avg_MAE_180D_pct":-37.49,"false_positive_rate":0.17,"missed_structural_count":0,"late_green_count":0,"avg_green_lateness_ratio":null,"avg_four_b_local_peak_proximity":0.408,"avg_four_b_full_window_peak_proximity":0.408,"score_return_alignment_verdict":"best local candidate"}
{"row_type":"profile_simulation","profile_id":"P3_counterexample_guard_profile","profile_scope":"counterexample_guard","profile_hypothesis":"Force pilot-only, expectation-only, and second-order-after-runup triggers into watch/4B overlay unless revenue conversion appears.","changed_axes":"proxy_to_watch; late_second_order_to_4B_overlay","changed_thresholds":"none","eligible_trigger_count":3,"selected_entry_trigger_per_case":3,"avg_MFE_90D_pct":9.12,"avg_MAE_90D_pct":-50.93,"avg_MFE_180D_pct":9.12,"avg_MAE_180D_pct":-55.19,"false_positive_rate":0.0,"missed_structural_count":0,"late_green_count":0,"avg_green_lateness_ratio":null,"avg_four_b_local_peak_proximity":0.408,"avg_four_b_full_window_peak_proximity":0.408,"score_return_alignment_verdict":"useful as guardrail, not standalone positive selector"}
```

## 26. Validation Scope

This loop is valid for C08 quality repair and C08-specific shadow rule discovery. It is not a global HBM rule, not a C07 order-relative-strength patch, and not a production scoring patch. Rows with reused stock-web-backed price paths are explicitly marked by `reuse_reason` and should be treated as source/proxy repair plus C08 compression evidence.

## 27. Deferred Coding Agent Handoff Prompt

```text
Do not run now. In a later coding-agent batch, ingest this MD together with the V12 research corpus. Validate JSONL trigger rows. Use the C08 rows only as canonical-archetype quality repair and shadow rule evidence. Do not change production scoring directly from this single MD. Candidate patch, if enough future C08 rows agree: add C08_CUSTOMER_QUALITY_REQUIRES_QUALIFICATION_REPEAT_DEMAND_AND_ORDER_CONVERSION_GATE as canonical shadow rule; require official/product/customer qualification, named-customer order, repeat socket consumable economics, or order/revenue conversion before Stage2-Actionable/Yellow; route small-order overlay, pilot-only expectation, and second-order-after-runup to watch/4B overlay.
```

## 28. Final Research Verdict

C08 should not be trained as “anything HBM inspection goes up.” It should be trained as “customer-quality evidence survives.” LEENO, Techwing, and YC April are useful because they show product/qualification/customer routes with strong MFE. Oros, Intekplus, and YC July are useful because they show the trapdoor: small-order proxy, pilot expectation, or second-order-after-runup can carry the same vocabulary while producing high MAE or late 4B behavior. The proposed C08 rule is therefore canonical-specific and shadow-only.
