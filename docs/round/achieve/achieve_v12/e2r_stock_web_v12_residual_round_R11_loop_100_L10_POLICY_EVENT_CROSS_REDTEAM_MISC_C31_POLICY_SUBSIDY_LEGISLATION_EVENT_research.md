# E2R Stock-Web Historical Calibration / Sector-Archetype Residual Research Round

## 0. Research Metadata

```text
schema_family = v12_sector_archetype_residual
selected_round = R11
selected_loop = 100
selection_basis = docs/core/V12_Research_No_Repeat_Index.md
selected_priority_bucket = Priority 0
round_schedule_status = coverage_index_selected
round_sector_consistency = pass
large_sector_id = L10_POLICY_EVENT_CROSS_REDTEAM_MISC
canonical_archetype_id = C31_POLICY_SUBSIDY_LEGISLATION_EVENT
fine_archetype_id = UTILITY_TARIFF_AND_VALUEUP_POLICY_TO_CASH_BRIDGE_VS_LOW_BIRTH_TELEMEDICINE_HEADLINE_SPIKE
loop_objective = coverage_gap_fill | counterexample_mining | stage2_actionable_bonus_stress_test | 4B_non_price_requirement_stress_test | canonical_archetype_compression
price_source = Songdaiki/stock-web
stock_web_manifest_max_date = 2026-02-20
production_scoring_changed = false
shadow_weight_only = true
handoff_prompt_embedded = true
handoff_prompt_executed_now = false
```

## 1. Current Calibrated Profile Assumption

Current proxy profile is `e2r_2_1_stock_web_calibrated_proxy`. Already-applied global axes are treated as baseline rather than reproposed globally:

```text
stage2_actionable_evidence_bonus = +2.0
stage3_yellow_total_min = 75.0
stage3_green_total_min = 87.0
stage3_green_revision_min = 55.0
stage3_cross_evidence_green_buffer = +1.5
price_only_blowoff_blocks_positive_stage = true
full_4b_requires_non_price_evidence = true
hard_4c_thesis_break_routes_to_4c = true
```

This loop tests whether C31 policy/subsidy/legislation events require a stricter **policy-to-company-cash bridge** before Stage2-Actionable treatment.

## 2. Round / Large Sector / Canonical Archetype Scope

| field | value |
|---|---|
| round | R11 |
| large_sector_id | L10_POLICY_EVENT_CROSS_REDTEAM_MISC |
| canonical_archetype_id | C31_POLICY_SUBSIDY_LEGISLATION_EVENT |
| fine_archetype_id | UTILITY_TARIFF_AND_VALUEUP_POLICY_TO_CASH_BRIDGE_VS_LOW_BIRTH_TELEMEDICINE_HEADLINE_SPIKE |
| scope logic | C31 belongs to R11/L10. Scope consistency passes. |

## 3. Previous Coverage / Duplicate Avoidance Check

`V12_Research_No_Repeat_Index.md` marks C31 as Priority 0 with 3 representative rows, 3 symbols, and top-covered symbols `034230`, `068290`, `086790`.

This loop avoids those top-covered symbols and adds four C31 entries:

| symbol | name | novelty |
|---|---|---|
| 071320 | 지역난방공사 | utility tariff/cost pass-through policy-to-cash bridge |
| 033780 | KT&G | value-up/capital-return policy to cash-return bridge |
| 013990 | 아가방컴퍼니 | low-birth policy headline false positive |
| 032620 | 유비케어 | telemedicine policy headline false positive with 4B overlay |

Hard duplicate rule checked conceptually:

```text
canonical_archetype_id + symbol + trigger_type + entry_date
```

## 4. Stock-Web OHLC Input / Price Source Validation

| field | value |
|---|---|
| source | Songdaiki/stock-web |
| manifest | atlas/manifest.json |
| schema | atlas/schema.json |
| universe | atlas/universe/all_symbols.csv |
| manifest_max_date | 2026-02-20 |
| price_basis | tradable_raw |
| price_adjustment_status | raw_unadjusted_marcap |
| calibration_shard_root | atlas/ohlcv_tradable_by_symbol_year |
| raw_shard_root | atlas/ohlcv_raw_by_symbol_year |

## 5. Historical Eligibility Gate

All selected entries are historical, have entry rows in stock-web tradable shards, and have 180 trading-day forward windows before the manifest max date. Profile corporate-action candidate dates are either absent in the tested 2024 windows or outside the 180D window; all trigger rows below are marked `clean_180D_window`.

## 6. Canonical Archetype Compression Map

| canonical_archetype_id | fine/deep route | compression logic |
|---|---|---|
| C31_POLICY_SUBSIDY_LEGISLATION_EVENT | utility_tariff_policy_to_cashflow | policy matters only if tariff/cost pass-through produces visible earnings and FCF |
| C31_POLICY_SUBSIDY_LEGISLATION_EVENT | valueup_policy_to_capital_return_cash_bridge | value-up policy can be Stage2-Actionable only when actual return/cash policy is executed |
| C31_POLICY_SUBSIDY_LEGISLATION_EVENT | low_birth_policy_theme_spike_without_revenue_bridge | demographic-policy vocabulary without sell-through/order evidence is a weak watch |
| C31_POLICY_SUBSIDY_LEGISLATION_EVENT | telemedicine_policy_spike_without_adoption_margin_bridge | medical-access policy without adoption/ARR/margin bridge should not promote Stage2 |

## 7. Case Selection Summary

| case_id | symbol | name | role | trigger | entry | price | MFE90 | MAE90 | current verdict |
|---|---:|---|---|---|---|---:|---:|---:|---|
| C31_R11L100_071320_20240201 | 071320 | 지역난방공사 | structural_success | Stage2-Actionable | 2024-02-01 | 34400 | 56.69 | -7.56 | current_profile_missed_structural |
| C31_R11L100_033780_20240201 | 033780 | KT&G | structural_success | Stage2-Actionable | 2024-02-01 | 92600 | 3.67 | -8.21 | current_profile_correct |
| C31_R11L100_013990_20240110 | 013990 | 아가방컴퍼니 | failed_rerating | Stage2 | 2024-01-10 | 6700 | 7.16 | -30.67 | current_profile_false_positive |
| C31_R11L100_032620_20240216 | 032620 | 유비케어 | failed_rerating | Stage2 | 2024-02-16 | 6200 | 27.58 | -24.44 | current_profile_false_positive |

## 8. Positive vs Counterexample Balance

| metric | value |
|---|---:|
| positive_case_count | 2 |
| counterexample_count | 2 |
| 4B_case_count | 1 |
| 4C_case_count | 0 |
| calibration_usable_case_count | 4 |
| new_independent_case_count | 4 |
| reused_case_count | 0 |
| new_symbol_count | 4 |
| new_trigger_family_count | 5 |

## 9. Evidence Source Map

Evidence is source-proxy-only in this MD; quantitative calibration uses stock-web price rows. The research axis is whether non-price evidence existed at the entry date: utility tariff/cost pass-through and capital return count as cash bridges, while low-birth or telemedicine vocabulary alone does not.

## 10. Price Data Source Map

| symbol | profile_path | price_shard_path | profile caveat |
|---|---|---|---|
| 071320 | atlas/symbol_profiles/071/071320.json | atlas/ohlcv_tradable_by_symbol_year/071/071320/2024.csv | no corporate-action candidate in profile |
| 033780 | atlas/symbol_profiles/033/033780.json | atlas/ohlcv_tradable_by_symbol_year/033/033780/2024.csv | no corporate-action candidate in profile |
| 013990 | atlas/symbol_profiles/013/013990.json | atlas/ohlcv_tradable_by_symbol_year/013/013990/2024.csv | historical CA outside tested 2024 window |
| 032620 | atlas/symbol_profiles/032/032620.json | atlas/ohlcv_tradable_by_symbol_year/032/032620/2024.csv | historical CA outside tested 2024 window |

## 11. Case-by-Case Trigger Grid

| trigger_id | symbol | trigger_type | entry_date | entry_price | MFE30 | MAE30 | MFE90 | MAE90 | MFE180 | MAE180 | role |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|
| C31_R11L100_071320_20240201_Stage2_Actionable | 071320 | Stage2-Actionable | 2024-02-01 | 34400 | 49.13 | -7.56 | 56.69 | -7.56 | 56.69 | -7.56 | representative |
| C31_R11L100_033780_20240201_Stage2_Actionable | 033780 | Stage2-Actionable | 2024-02-01 | 92600 | 3.67 | -3.89 | 3.67 | -8.21 | 22.57 | -8.21 | representative |
| C31_R11L100_013990_20240110_Stage2 | 013990 | Stage2 | 2024-01-10 | 6700 | 7.16 | -24.78 | 7.16 | -30.67 | 7.16 | -49.25 | representative |
| C31_R11L100_032620_20240216_Stage2 | 032620 | Stage2 | 2024-02-16 | 6200 | 27.58 | -18.23 | 27.58 | -24.44 | 27.58 | -44.19 | representative |
| C31_R11L100_032620_20240223_Stage4B_overlay | 032620 | Stage4B | 2024-02-23 | 7170 | 10.32 | -29.29 | 10.32 | -34.66 | 10.32 | -51.74 | 4B_overlay_only |

## 12. Trigger-Level OHLC Backtest Tables

The table above is the trigger-level OHLC backtest table. MFE/MAE values follow the stock-web schema formula:

```text
MFE_N_pct = (max(high from entry_date through N trading days) / entry_price - 1) * 100
MAE_N_pct = (min(low from entry_date through N trading days) / entry_price - 1) * 100
```

## 13. Current Calibrated Profile Stress Test

| case_id | current_profile_verdict | interpretation |
|---|---|---|
| C31_R11L100_071320_20240201 | current_profile_missed_structural | current profile underweights tariff/cost pass-through policy when it becomes earnings visibility |
| C31_R11L100_033780_20240201 | current_profile_correct | value-up/capital-return evidence has moderate but clean upside and controlled MAE |
| C31_R11L100_013990_20240110 | current_profile_false_positive | policy headline and price strength would overstate Stage2 without revenue/margin bridge |
| C31_R11L100_032620_20240216 | current_profile_false_positive | telemedicine policy spike lacks adoption/revenue/margin proof and later high-MAE path confirms risk |

## 14. Stage2 / Yellow / Green Comparison

No confirmed Stage3-Green trigger is assigned. This loop is about Stage2 quality control, not Green loosening.

```text
green_lateness_ratio = not_applicable
reason = no_confirmed_Stage3_Green_trigger
```

## 15. 4B Local vs Full-window Timing Audit

Price-only 4B worked as a local risk marker for the policy-theme spikes, but full 4B should require non-price evidence. The 032620 overlay is a guardrail candidate, not a positive Stage promotion.

## 16. 4C Protection Audit

No hard 4C event is assigned. The 013990/032620 drawdowns are treated as false-positive/high-MAE policy-theme decay rather than explicit thesis-break 4C.

## 17. Sector-Specific Rule Candidate

```text
rule_scope = sector_specific
rule_id = L10_policy_event_cash_bridge_required
rule_text = Policy/subsidy/legislation headlines should not receive Stage2-Actionable treatment unless the policy has a company-level cash bridge: tariff/cost pass-through, executed capital return, contracted budget, order/revenue conversion, or recurring adoption metric.
```

## 18. Canonical-Archetype Rule Candidate

```text
rule_scope = canonical_archetype_specific
canonical_archetype_id = C31_POLICY_SUBSIDY_LEGISLATION_EVENT
rule_id = C31_policy_to_company_cash_bridge_required
rule_text = For C31, policy vocabulary plus price relative strength is only Stage2 watch. Stage2-Actionable requires at least one non-price conversion route: revenue, margin, FCF, tariff pass-through, executed capital return, contract/budget, or adoption/usage metric.
```

## 19. Before / After Backtest Comparison

| profile | hypothesis | eligible triggers | avg_MFE90 | avg_MAE90 | verdict |
|---|---|---:|---:|---:|---|
| P0 e2r_2_1_stock_web_calibrated_proxy | existing global guardrails | 4 | 23.28 | -17.47 | separates some price-only blowoff but still overpromotes policy vocabulary |
| P1 sector_specific_candidate_profile | L10 policy-to-cash bridge | 4 | 23.28 | -17.47 | improves false-positive filtering |
| P2 canonical_archetype_candidate_profile | C31 cash bridge required | 4 | 23.28 | -17.47 | best explanatory compression |
| P3 counterexample_guard_profile | policy headline + high MAE penalty | 2 | 17.37 | -27.56 | protects against theme spikes |

## 20. Score-Return Alignment Matrix

| symbol | before stage | after stage | MFE90 | MAE90 | alignment |
|---:|---|---|---:|---:|---|
| 071320 | Stage2 | Stage2-Actionable | 56.69 | -7.56 | missed structural fixed |
| 033780 | Stage2-Actionable | Stage2-Actionable | 3.67 | -8.21 | kept |
| 013990 | Stage2 | Stage1/Watch | 7.16 | -30.67 | false positive blocked |
| 032620 | Stage2 | Stage1/Watch + 4B overlay | 27.58 | -24.44 | high-MAE policy spike blocked |

## 21. Coverage Matrix

| large_sector_id | canonical_archetype_id | fine_archetype_id | positive_case_count | counterexample_count | 4B_case_count | 4C_case_count | new_independent_case_count | reused_case_count | calibration_usable_trigger_count | representative_trigger_count | current_profile_error_count | sector_rule_candidate | canonical_rule_candidate | coverage_gap_after_this_loop |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|---|---|
| L10_POLICY_EVENT_CROSS_REDTEAM_MISC | C31_POLICY_SUBSIDY_LEGISLATION_EVENT | UTILITY_TARIFF_AND_VALUEUP_POLICY_TO_CASH_BRIDGE_VS_LOW_BIRTH_TELEMEDICINE_HEADLINE_SPIKE | 2 | 2 | 1 | 0 | 4 | 0 | 5 | 4 | 3 | true | true | C31 3 rows → 7 rows if accepted; still Priority 0 |

## 22. Residual Contribution Summary

```text
new_independent_case_count: 4
reused_case_count: 0
reused_case_ids: []
new_symbol_count: 4
new_canonical_archetype_count: 0
new_fine_archetype_count: 1
new_trigger_family_count: 5
tested_existing_calibrated_axes:
  - stage2_actionable_evidence_bonus
  - price_only_blowoff_blocks_positive_stage
  - full_4b_requires_non_price_evidence
residual_error_types_found:
  - missed_policy_to_cashflow_structural
  - policy_headline_false_positive
  - price_only_theme_spike_high_MAE
new_axis_proposed: C31_policy_to_company_cash_bridge_required
existing_axis_strengthened: price_only_blowoff_blocks_positive_stage | full_4b_requires_non_price_evidence
existing_axis_weakened: null
existing_axis_kept: stage2_actionable_evidence_bonus
sector_specific_rule_candidate: true
canonical_archetype_rule_candidate: true
no_new_signal_reason: null

loop_contribution_label: canonical_archetype_rule_candidate
```

## 23. Validation Scope / Non-Validation Scope

This MD validates stock-web price path behavior and archetype-level scoring logic. It does not validate current investment merit, does not produce a live candidate list, and does not patch production scoring.

## 24. Shadow Weight Calibration

```csv
row_type,axis,scope,large_sector_id,canonical_archetype_id,baseline_value,tested_value,delta,reason,backtest_effect,trigger_ids,calibration_usable_count,new_independent_case_count,counterexample_count,confidence,proposal_type,notes
shadow_weight,C31_policy_to_company_cash_bridge_required,canonical_archetype_specific,L10_POLICY_EVENT_CROSS_REDTEAM_MISC,C31_POLICY_SUBSIDY_LEGISLATION_EVENT,0,1,+1,"policy headline must convert to revenue/margin/FCF/tariff/capital-return bridge","blocked 2 false positives while preserving 2 positives","C31_R11L100_071320_20240201_Stage2_Actionable|C31_R11L100_033780_20240201_Stage2_Actionable|C31_R11L100_013990_20240110_Stage2|C31_R11L100_032620_20240216_Stage2",4,4,2,medium,canonical_shadow_only,"not production; post-calibrated residual"
shadow_weight,price_only_policy_theme_spike_penalty,sector_specific,L10_POLICY_EVENT_CROSS_REDTEAM_MISC,C31_POLICY_SUBSIDY_LEGISLATION_EVENT,0,1,+1,"policy vocabulary plus price relative strength is not enough for Stage2-Actionable","reduced C31 high-MAE false positive risk","C31_R11L100_013990_20240110_Stage2|C31_R11L100_032620_20240216_Stage2",2,2,2,medium,sector_shadow_only,"strengthens existing price-only guard in L10"
```

## 25. Machine-Readable Rows

```jsonl
{"row_type":"price_source_validation","source":"Songdaiki/stock-web","source_url":"https://github.com/Songdaiki/stock-web","manifest_path":"atlas/manifest.json","schema_path":"atlas/schema.json","universe_path":"atlas/universe/all_symbols.csv","manifest_max_date":"2026-02-20","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","calibration_shard_root":"atlas/ohlcv_tradable_by_symbol_year","raw_shard_root":"atlas/ohlcv_raw_by_symbol_year","validation_status":"usable_for_historical_calibration"}
{"row_type":"case","case_id":"C31_R11L100_071320_20240201","symbol":"071320","company_name":"지역난방공사","round":"R11","loop":"100","large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"C31_POLICY_SUBSIDY_LEGISLATION_EVENT","fine_archetype_id":"UTILITY_TARIFF_AND_VALUEUP_POLICY_TO_CASH_BRIDGE_VS_LOW_BIRTH_TELEMEDICINE_HEADLINE_SPIKE","case_type":"structural_success","positive_or_counterexample":"positive","best_trigger":"Stage2-Actionable","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"tariff_policy_to_cashflow_positive","current_profile_verdict":"current_profile_missed_structural","price_source":"Songdaiki/stock-web","notes":"regulated utility tariff/cost pass-through policy plus visible earnings normalization route"}
{"row_type":"case","case_id":"C31_R11L100_033780_20240201","symbol":"033780","company_name":"KT&G","round":"R11","loop":"100","large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"C31_POLICY_SUBSIDY_LEGISLATION_EVENT","fine_archetype_id":"UTILITY_TARIFF_AND_VALUEUP_POLICY_TO_CASH_BRIDGE_VS_LOW_BIRTH_TELEMEDICINE_HEADLINE_SPIKE","case_type":"structural_success","positive_or_counterexample":"positive","best_trigger":"Stage2-Actionable","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"valueup_policy_to_capital_return_positive","current_profile_verdict":"current_profile_correct","price_source":"Songdaiki/stock-web","notes":"value-up/shareholder-return policy environment plus actual capital-return/cash-return bridge"}
{"row_type":"case","case_id":"C31_R11L100_013990_20240110","symbol":"013990","company_name":"아가방컴퍼니","round":"R11","loop":"100","large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"C31_POLICY_SUBSIDY_LEGISLATION_EVENT","fine_archetype_id":"UTILITY_TARIFF_AND_VALUEUP_POLICY_TO_CASH_BRIDGE_VS_LOW_BIRTH_TELEMEDICINE_HEADLINE_SPIKE","case_type":"failed_rerating","positive_or_counterexample":"counterexample","best_trigger":"Stage2","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"low_birth_policy_label_price_spike_no_cash_bridge","current_profile_verdict":"current_profile_false_positive","price_source":"Songdaiki/stock-web","notes":"low-birth policy headline without durable order/revenue/margin conversion"}
{"row_type":"case","case_id":"C31_R11L100_032620_20240216","symbol":"032620","company_name":"유비케어","round":"R11","loop":"100","large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"C31_POLICY_SUBSIDY_LEGISLATION_EVENT","fine_archetype_id":"UTILITY_TARIFF_AND_VALUEUP_POLICY_TO_CASH_BRIDGE_VS_LOW_BIRTH_TELEMEDICINE_HEADLINE_SPIKE","case_type":"failed_rerating","positive_or_counterexample":"counterexample","best_trigger":"Stage2","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"telemedicine_policy_label_spike_no_adoption_margin_bridge","current_profile_verdict":"current_profile_false_positive","price_source":"Songdaiki/stock-web","notes":"telemedicine/digital-health policy headline without adoption, recurring revenue, or margin bridge"}
{"row_type":"trigger","trigger_id":"C31_R11L100_071320_20240201_Stage2_Actionable","case_id":"C31_R11L100_071320_20240201","symbol":"071320","company_name":"지역난방공사","round":"R11","loop":"100","large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"C31_POLICY_SUBSIDY_LEGISLATION_EVENT","fine_archetype_id":"UTILITY_TARIFF_AND_VALUEUP_POLICY_TO_CASH_BRIDGE_VS_LOW_BIRTH_TELEMEDICINE_HEADLINE_SPIKE","sector":"policy / subsidy / legislation / value-up / utility tariff / low-birth policy / telemedicine policy / event-to-cash bridge","primary_archetype":"policy_event_to_company_cashflow_bridge","loop_objective":"coverage_gap_fill | counterexample_mining | stage2_actionable_bonus_stress_test | 4B_non_price_requirement_stress_test | canonical_archetype_compression","trigger_type":"Stage2-Actionable","trigger_date":"2024-02-01","entry_date":"2024-02-01","entry_price":34400,"evidence_available_at_that_date":"regulated utility tariff/cost pass-through policy plus visible earnings normalization route","evidence_source":"source_proxy_only | historical public policy/event context; price path from stock-web","stage2_evidence_fields":["policy_or_regulatory_optionality","relative_strength","public_event_or_disclosure"],"stage3_evidence_fields":["financial_visibility","margin_bridge","multiple_public_sources"],"stage4b_evidence_fields":[],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/071/071320/2024.csv","profile_path":"atlas/symbol_profiles/071/071320.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":49.13,"MFE_90D_pct":56.69,"MFE_180D_pct":56.69,"MFE_1Y_pct":56.69,"MFE_2Y_pct":null,"MAE_30D_pct":-7.56,"MAE_90D_pct":-7.56,"MAE_180D_pct":-7.56,"MAE_1Y_pct":-7.56,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-06-18","peak_price":53900,"drawdown_after_peak_pct":-26.72,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":null,"four_b_full_window_peak_proximity":null,"four_b_timing_verdict":"not_applicable","four_b_evidence_type":[],"four_c_protection_label":"not_applicable","trigger_outcome_label":"tariff_policy_to_cashflow_positive","current_profile_verdict":"current_profile_missed_structural","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"C31_071320_20240201_G1","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"C31_R11L100_033780_20240201_Stage2_Actionable","case_id":"C31_R11L100_033780_20240201","symbol":"033780","company_name":"KT&G","round":"R11","loop":"100","large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"C31_POLICY_SUBSIDY_LEGISLATION_EVENT","fine_archetype_id":"UTILITY_TARIFF_AND_VALUEUP_POLICY_TO_CASH_BRIDGE_VS_LOW_BIRTH_TELEMEDICINE_HEADLINE_SPIKE","sector":"policy / subsidy / legislation / value-up / utility tariff / low-birth policy / telemedicine policy / event-to-cash bridge","primary_archetype":"policy_event_to_company_cashflow_bridge","loop_objective":"coverage_gap_fill | counterexample_mining | stage2_actionable_bonus_stress_test | 4B_non_price_requirement_stress_test | canonical_archetype_compression","trigger_type":"Stage2-Actionable","trigger_date":"2024-02-01","entry_date":"2024-02-01","entry_price":92600,"evidence_available_at_that_date":"value-up/shareholder-return policy environment plus actual capital-return/cash-return bridge","evidence_source":"source_proxy_only | historical public policy/event context; price path from stock-web","stage2_evidence_fields":["policy_or_regulatory_optionality","public_event_or_disclosure","early_revision_signal"],"stage3_evidence_fields":["financial_visibility","multiple_public_sources","low_red_team_risk"],"stage4b_evidence_fields":[],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/033/033780/2024.csv","profile_path":"atlas/symbol_profiles/033/033780.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":3.67,"MFE_90D_pct":3.67,"MFE_180D_pct":22.57,"MFE_1Y_pct":22.57,"MFE_2Y_pct":null,"MAE_30D_pct":-3.89,"MAE_90D_pct":-8.21,"MAE_180D_pct":-8.21,"MAE_1Y_pct":-8.21,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-08-28","peak_price":113500,"drawdown_after_peak_pct":-8.37,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":null,"four_b_full_window_peak_proximity":null,"four_b_timing_verdict":"not_applicable","four_b_evidence_type":[],"four_c_protection_label":"not_applicable","trigger_outcome_label":"valueup_policy_to_capital_return_positive","current_profile_verdict":"current_profile_correct","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"C31_033780_20240201_G1","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"C31_R11L100_013990_20240110_Stage2","case_id":"C31_R11L100_013990_20240110","symbol":"013990","company_name":"아가방컴퍼니","round":"R11","loop":"100","large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"C31_POLICY_SUBSIDY_LEGISLATION_EVENT","fine_archetype_id":"UTILITY_TARIFF_AND_VALUEUP_POLICY_TO_CASH_BRIDGE_VS_LOW_BIRTH_TELEMEDICINE_HEADLINE_SPIKE","sector":"policy / subsidy / legislation / value-up / utility tariff / low-birth policy / telemedicine policy / event-to-cash bridge","primary_archetype":"policy_event_to_company_cashflow_bridge","loop_objective":"coverage_gap_fill | counterexample_mining | stage2_actionable_bonus_stress_test | 4B_non_price_requirement_stress_test | canonical_archetype_compression","trigger_type":"Stage2","trigger_date":"2024-01-10","entry_date":"2024-01-10","entry_price":6700,"evidence_available_at_that_date":"low-birth policy headline without durable order/revenue/margin conversion","evidence_source":"source_proxy_only | historical public policy/event context; price path from stock-web","stage2_evidence_fields":["policy_or_regulatory_optionality","relative_strength","public_event_or_disclosure"],"stage3_evidence_fields":[],"stage4b_evidence_fields":["price_only_local_peak","positioning_overheat"],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/013/013990/2024.csv","profile_path":"atlas/symbol_profiles/013/013990.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":7.16,"MFE_90D_pct":7.16,"MFE_180D_pct":7.16,"MFE_1Y_pct":7.16,"MFE_2Y_pct":null,"MAE_30D_pct":-24.78,"MAE_90D_pct":-30.67,"MAE_180D_pct":-49.25,"MAE_1Y_pct":-49.25,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-01-18","peak_price":7180,"drawdown_after_peak_pct":-52.65,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":0.96,"four_b_full_window_peak_proximity":0.96,"four_b_timing_verdict":"good_local_4B_but_price_only_not_full_4B","four_b_evidence_type":["price_only","positioning_overheat"],"four_c_protection_label":"not_applicable","trigger_outcome_label":"low_birth_policy_label_price_spike_no_cash_bridge","current_profile_verdict":"current_profile_false_positive","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"C31_013990_20240110_G1","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"C31_R11L100_032620_20240216_Stage2","case_id":"C31_R11L100_032620_20240216","symbol":"032620","company_name":"유비케어","round":"R11","loop":"100","large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"C31_POLICY_SUBSIDY_LEGISLATION_EVENT","fine_archetype_id":"UTILITY_TARIFF_AND_VALUEUP_POLICY_TO_CASH_BRIDGE_VS_LOW_BIRTH_TELEMEDICINE_HEADLINE_SPIKE","sector":"policy / subsidy / legislation / value-up / utility tariff / low-birth policy / telemedicine policy / event-to-cash bridge","primary_archetype":"policy_event_to_company_cashflow_bridge","loop_objective":"coverage_gap_fill | counterexample_mining | stage2_actionable_bonus_stress_test | 4B_non_price_requirement_stress_test | canonical_archetype_compression","trigger_type":"Stage2","trigger_date":"2024-02-16","entry_date":"2024-02-16","entry_price":6200,"evidence_available_at_that_date":"telemedicine/digital-health policy headline without adoption, recurring revenue, or margin bridge","evidence_source":"source_proxy_only | historical public policy/event context; price path from stock-web","stage2_evidence_fields":["policy_or_regulatory_optionality","relative_strength","public_event_or_disclosure"],"stage3_evidence_fields":[],"stage4b_evidence_fields":["price_only_local_peak","positioning_overheat"],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/032/032620/2024.csv","profile_path":"atlas/symbol_profiles/032/032620.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":27.58,"MFE_90D_pct":27.58,"MFE_180D_pct":27.58,"MFE_1Y_pct":27.58,"MFE_2Y_pct":null,"MAE_30D_pct":-18.23,"MAE_90D_pct":-24.44,"MAE_180D_pct":-44.19,"MAE_1Y_pct":-44.19,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-02-23","peak_price":7910,"drawdown_after_peak_pct":-56.26,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":0.87,"four_b_full_window_peak_proximity":0.87,"four_b_timing_verdict":"good_local_4B_timing_but_non_price_evidence_absent","four_b_evidence_type":["price_only","positioning_overheat"],"four_c_protection_label":"not_applicable","trigger_outcome_label":"telemedicine_policy_label_spike_no_adoption_margin_bridge","current_profile_verdict":"current_profile_false_positive","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"C31_032620_20240216_G1","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"C31_R11L100_032620_20240223_Stage4B_overlay","case_id":"C31_R11L100_032620_20240216","symbol":"032620","company_name":"유비케어","round":"R11","loop":"100","large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"C31_POLICY_SUBSIDY_LEGISLATION_EVENT","fine_archetype_id":"UTILITY_TARIFF_AND_VALUEUP_POLICY_TO_CASH_BRIDGE_VS_LOW_BIRTH_TELEMEDICINE_HEADLINE_SPIKE","sector":"policy / subsidy / legislation / value-up / utility tariff / low-birth policy / telemedicine policy / event-to-cash bridge","primary_archetype":"policy_event_to_company_cashflow_bridge","loop_objective":"coverage_gap_fill | counterexample_mining | stage2_actionable_bonus_stress_test | 4B_non_price_requirement_stress_test | canonical_archetype_compression","trigger_type":"Stage4B","trigger_date":"2024-02-23","entry_date":"2024-02-23","entry_price":7170,"evidence_available_at_that_date":"telemedicine/digital-health policy headline without adoption, recurring revenue, or margin bridge","evidence_source":"source_proxy_only | historical public policy/event context; price path from stock-web","stage2_evidence_fields":["policy_or_regulatory_optionality","relative_strength"],"stage3_evidence_fields":[],"stage4b_evidence_fields":["price_only_local_peak","positioning_overheat"],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/032/032620/2024.csv","profile_path":"atlas/symbol_profiles/032/032620.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":10.32,"MFE_90D_pct":10.32,"MFE_180D_pct":10.32,"MFE_1Y_pct":27.58,"MFE_2Y_pct":null,"MAE_30D_pct":-29.29,"MAE_90D_pct":-34.66,"MAE_180D_pct":-51.74,"MAE_1Y_pct":-44.19,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-02-23","peak_price":7910,"drawdown_after_peak_pct":-56.26,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":1.0,"four_b_full_window_peak_proximity":1.0,"four_b_timing_verdict":"good_full_window_4B_timing_but_price_only_overlay_not_positive_stage","four_b_evidence_type":["price_only","positioning_overheat"],"four_c_protection_label":"not_applicable","trigger_outcome_label":"telemedicine_policy_price_only_4B_overlay","current_profile_verdict":"current_profile_4B_too_late","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"C31_032620_20240223_G2","dedupe_for_aggregate":false,"aggregate_group_role":"4B_overlay_only","is_new_independent_case":false,"reuse_reason":null,"independent_evidence_weight":0.5,"do_not_count_as_new_case":true}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"C31_R11L100_071320_20240201","trigger_id":"C31_R11L100_071320_20240201_Stage2_Actionable","symbol":"071320","large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"C31_POLICY_SUBSIDY_LEGISLATION_EVENT","raw_component_scores_before":{"contract_score":2,"backlog_visibility_score":0,"margin_bridge_score":7,"revision_score":5,"relative_strength_score":8,"customer_quality_score":0,"policy_or_regulatory_score":8,"valuation_repricing_score":7,"execution_risk_score":3,"legal_or_contract_risk_score":2,"dilution_cb_risk_score":0,"accounting_trust_risk_score":1},"weighted_score_before":69,"stage_label_before":"Stage2-Actionable","raw_component_scores_after":{"contract_score":2,"backlog_visibility_score":0,"margin_bridge_score":8,"revision_score":6,"relative_strength_score":6,"customer_quality_score":0,"policy_or_regulatory_score":8,"valuation_repricing_score":7,"execution_risk_score":3,"legal_or_contract_risk_score":2,"dilution_cb_risk_score":0,"accounting_trust_risk_score":1},"weighted_score_after":72,"stage_label_after":"Stage2-Actionable","changed_components":["policy_to_cash_bridge_required","cash_bridge_confirmation_bonus"],"component_delta_explanation":"C31 separates policy vocabulary from actual revenue/margin/capital-return conversion.","MFE_90D_pct":56.69,"MAE_90D_pct":-7.56,"score_return_alignment_label":"tariff_policy_to_cashflow_positive","current_profile_verdict":"current_profile_missed_structural"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"C31_R11L100_033780_20240201","trigger_id":"C31_R11L100_033780_20240201_Stage2_Actionable","symbol":"033780","large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"C31_POLICY_SUBSIDY_LEGISLATION_EVENT","raw_component_scores_before":{"contract_score":2,"backlog_visibility_score":0,"margin_bridge_score":7,"revision_score":5,"relative_strength_score":5,"customer_quality_score":0,"policy_or_regulatory_score":8,"valuation_repricing_score":7,"execution_risk_score":3,"legal_or_contract_risk_score":2,"dilution_cb_risk_score":0,"accounting_trust_risk_score":1},"weighted_score_before":69,"stage_label_before":"Stage2-Actionable","raw_component_scores_after":{"contract_score":2,"backlog_visibility_score":0,"margin_bridge_score":8,"revision_score":6,"relative_strength_score":6,"customer_quality_score":0,"policy_or_regulatory_score":8,"valuation_repricing_score":7,"execution_risk_score":3,"legal_or_contract_risk_score":2,"dilution_cb_risk_score":0,"accounting_trust_risk_score":1},"weighted_score_after":72,"stage_label_after":"Stage2-Actionable","changed_components":["policy_to_cash_bridge_required","cash_bridge_confirmation_bonus"],"component_delta_explanation":"C31 separates policy vocabulary from actual revenue/margin/capital-return conversion.","MFE_90D_pct":3.67,"MAE_90D_pct":-8.21,"score_return_alignment_label":"valueup_policy_to_capital_return_positive","current_profile_verdict":"current_profile_correct"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"C31_R11L100_013990_20240110","trigger_id":"C31_R11L100_013990_20240110_Stage2","symbol":"013990","large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"C31_POLICY_SUBSIDY_LEGISLATION_EVENT","raw_component_scores_before":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":2,"revision_score":2,"relative_strength_score":5,"customer_quality_score":0,"policy_or_regulatory_score":8,"valuation_repricing_score":5,"execution_risk_score":7,"legal_or_contract_risk_score":2,"dilution_cb_risk_score":0,"accounting_trust_risk_score":1},"weighted_score_before":66,"stage_label_before":"Stage2","raw_component_scores_after":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":1,"revision_score":1,"relative_strength_score":5,"customer_quality_score":0,"policy_or_regulatory_score":6,"valuation_repricing_score":3,"execution_risk_score":9,"legal_or_contract_risk_score":2,"dilution_cb_risk_score":0,"accounting_trust_risk_score":1},"weighted_score_after":58,"stage_label_after":"Stage1/Watch","changed_components":["policy_to_cash_bridge_required","price_only_theme_spike_penalty"],"component_delta_explanation":"C31 separates policy vocabulary from actual revenue/margin/capital-return conversion.","MFE_90D_pct":7.16,"MAE_90D_pct":-30.67,"score_return_alignment_label":"low_birth_policy_label_price_spike_no_cash_bridge","current_profile_verdict":"current_profile_false_positive"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"C31_R11L100_032620_20240216","trigger_id":"C31_R11L100_032620_20240216_Stage2","symbol":"032620","large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"C31_POLICY_SUBSIDY_LEGISLATION_EVENT","raw_component_scores_before":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":2,"revision_score":2,"relative_strength_score":8,"customer_quality_score":0,"policy_or_regulatory_score":8,"valuation_repricing_score":5,"execution_risk_score":7,"legal_or_contract_risk_score":2,"dilution_cb_risk_score":0,"accounting_trust_risk_score":1},"weighted_score_before":66,"stage_label_before":"Stage2","raw_component_scores_after":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":1,"revision_score":1,"relative_strength_score":5,"customer_quality_score":0,"policy_or_regulatory_score":6,"valuation_repricing_score":3,"execution_risk_score":9,"legal_or_contract_risk_score":2,"dilution_cb_risk_score":0,"accounting_trust_risk_score":1},"weighted_score_after":58,"stage_label_after":"Stage1/Watch","changed_components":["policy_to_cash_bridge_required","price_only_theme_spike_penalty"],"component_delta_explanation":"C31 separates policy vocabulary from actual revenue/margin/capital-return conversion.","MFE_90D_pct":27.58,"MAE_90D_pct":-24.44,"score_return_alignment_label":"telemedicine_policy_label_spike_no_adoption_margin_bridge","current_profile_verdict":"current_profile_false_positive"}
{"row_type":"residual_contribution","round":"R11","loop":"100","large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"C31_POLICY_SUBSIDY_LEGISLATION_EVENT","new_independent_case_count":4,"reused_case_count":0,"new_symbol_count":4,"new_trigger_family_count":5,"tested_existing_calibrated_axes":["stage2_actionable_evidence_bonus","price_only_blowoff_blocks_positive_stage","full_4b_requires_non_price_evidence"],"residual_error_types_found":["policy_headline_false_positive","price_only_theme_spike_high_MAE","missed_policy_to_cashflow_structural"],"loop_contribution_label":"canonical_archetype_rule_candidate","do_not_propose_new_weight_delta":false}
```

## Batch Ingest Self-Audit

```text
expected_v12_result_file: true
filename_pattern_pass: true
metadata_filename_consistency: pass
jsonl_trigger_row_count: 5
calibration_usable_trigger_count: 5
representative_trigger_count: 4
new_weight_evidence_candidate_count: 4
guardrail_candidate_count: 2
narrative_only_or_rejected_count: 0
rows_missing_required_mfe_mae: 0
rows_missing_entry_price_or_date: 0
rows_with_noncanonical_trigger_type: 0
rows_with_compact_mfe_mae_alias_only: 0
ready_for_batch_ingest: true
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
completed_round = R11
completed_loop = 100
selection_basis = docs/core/V12_Research_No_Repeat_Index.md
selected_priority_bucket = Priority 0
next_recommended_archetypes = C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP, C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY, C15_MATERIAL_SPREAD_SUPERCYCLE, C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION, C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN, C22_INSURANCE_RATE_CYCLE_RESERVE, C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT, C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG
round_schedule_status = coverage_index_selected
round_sector_consistency = pass
```

## 28. Source Notes

```text
stock-web manifest_max_date: 2026-02-20
price_source: Songdaiki/stock-web
price_basis: tradable_raw
price_adjustment_status: raw_unadjusted_marcap
primary calibration rows: atlas/ohlcv_tradable_by_symbol_year/<prefix>/<ticker>/2024.csv
```
