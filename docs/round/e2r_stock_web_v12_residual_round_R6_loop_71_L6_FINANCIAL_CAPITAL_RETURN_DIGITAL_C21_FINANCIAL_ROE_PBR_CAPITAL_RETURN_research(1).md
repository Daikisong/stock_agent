# E2R Stock-Web Historical Calibration / Sector-Archetype Residual Research Round

## 0. Research Metadata

```text
research_session = post_calibrated_sector_archetype_residual_research
mode = historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12
scheduled_round = R6
scheduled_loop = 71
large_sector_id = L6_FINANCIAL_CAPITAL_RETURN_DIGITAL
canonical_archetype_id = C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN
fine_archetype_id = REGIONAL_FINANCIAL_VALUEUP_CAPITAL_RETURN_CREDIT_COST_SPLIT
loop_objective = residual_false_positive_mining | stage2_actionable_bonus_stress_test | sector_specific_rule_discovery | counterexample_mining | coverage_gap_fill
output_file = e2r_stock_web_v12_residual_round_R6_loop_71_L6_FINANCIAL_CAPITAL_RETURN_DIGITAL_C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN_research.md
production_scoring_changed = false
shadow_weight_only = true
```

This loop adds 4 new independent cases, 2 counterexamples, and 2 residual errors for R6/L6_FINANCIAL_CAPITAL_RETURN_DIGITAL/C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN.

## 1. Current Calibrated Profile Assumption

```text
before_profile_id = e2r_2_1_stock_web_calibrated_proxy
rollback_reference_profile_id = e2r_2_0_baseline_reference
stage2_actionable_evidence_bonus = +2.0
stage3_yellow_total_min = 75.0
stage3_green_total_min = 87.0
stage3_green_revision_min = 55.0
stage3_cross_evidence_green_buffer = +1.5
price_only_blowoff_blocks_positive_stage = true
full_4b_requires_non_price_evidence = true
hard_4c_thesis_break_routes_to_4c = true
```

R6 financial calibration should not loosen Green. The practical residual is narrower: policy/value-up headlines created a broad financial-sector Stage2 watch signal, but the realized path split sharply between banks with ROE/capital-return execution and financials where policy enthusiasm lacked an executable capital-return bridge.

## 2. Round / Large Sector / Canonical Archetype Scope

| field | value |
|---|---|
| scheduled_round | R6 |
| scheduled_loop | 71 |
| large_sector_id | L6_FINANCIAL_CAPITAL_RETURN_DIGITAL |
| canonical_archetype_id | C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN |
| fine_archetype_id | REGIONAL_FINANCIAL_VALUEUP_CAPITAL_RETURN_CREDIT_COST_SPLIT |
| round_schedule_status | valid |
| round_sector_consistency | pass |

R6 hard gate is satisfied because the MD uses `L6_FINANCIAL_CAPITAL_RETURN_DIGITAL` and C21 financial ROE/PBR/capital-return scope.

## 3. Previous Coverage / Duplicate Avoidance Check

The No-Repeat rule is applied as:

```text
hard_duplicate_key = canonical_archetype_id + symbol + trigger_type + entry_date
```

This loop avoids the repeatedly covered C21 combinations around KB금융(105560), 하나금융지주(086790), 카카오뱅크(323410), UNKNOWN_SYMBOL, and 제주은행(006220). The selected symbols are less-saturated R6 C21 names and each representative trigger uses the same macro event date but a different symbol, producing new independent case coverage rather than a duplicate exact key.

| symbol | company | duplicate stance | reason |
|---|---|---|---|
| 175330 | JB금융지주 | new independent | same C21 archetype, new symbol for regional-bank capital-return execution |
| 138930 | BNK금융지주 | new independent | same C21 archetype, new symbol; stronger 180D follow-through than policy-only names |
| 139130 | DGB금융지주 / iM금융지주 | new independent | same C21 archetype, new failure-mode sample: credit/ROE quality drag |
| 006800 | 미래에셋증권 | new independent | same C21 archetype, new failure-mode sample: brokerage beta without bank-like ROE/PBR bridge |

## 4. Stock-Web OHLC Input / Price Source Validation

The price source is `Songdaiki/stock-web`. Manifest confirms `source_name = FinanceData/marcap`, `price_adjustment_status = raw_unadjusted_marcap`, `min_date = 1995-05-02`, `max_date = 2026-02-20`, `tradable_row_count = 14354401`, `raw_row_count = 15214118`, `symbol_count = 5414`, `active_like_symbol_count = 2868`, and `calibration_shard_root = atlas/ohlcv_tradable_by_symbol_year`.

```jsonl
{"row_type":"price_source_validation","source":"Songdaiki/stock-web","source_url":"https://github.com/Songdaiki/stock-web","manifest_path":"atlas/manifest.json","schema_path":"atlas/schema.json","universe_path":"atlas/universe/all_symbols.csv","manifest_max_date":"2026-02-20","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","calibration_shard_root":"atlas/ohlcv_tradable_by_symbol_year","raw_shard_root":"atlas/ohlcv_raw_by_symbol_year","validation_status":"usable_for_historical_calibration"}
```

## 5. Historical Eligibility Gate

All representative triggers use `entry_date = 2024-02-27`, the next stock-web tradable date after the 2024-02-26 Korea value-up policy event, because exact intraday evidence availability is treated conservatively. All selected symbols have 180 trading-day forward windows available inside stock-web max date and no corporate-action candidate dates inside the 2024-02-27~D+180 calibration window.

| symbol | profile_path | entry_date | entry_price | 180D window | corporate-action window | calibration_usable |
|---|---|---:|---:|---|---|---|
| 175330 | atlas/symbol_profiles/175/175330.json | 2024-02-27 | 13610 | available | clean_180D_window | true |
| 138930 | atlas/symbol_profiles/138/138930.json | 2024-02-27 | 7720 | available | clean_180D_window | true |
| 139130 | atlas/symbol_profiles/139/139130.json | 2024-02-27 | 9230 | available | clean_180D_window | true |
| 006800 | atlas/symbol_profiles/006/006800.json | 2024-02-27 | 8660 | available | clean_180D_window | true |

## 6. Canonical Archetype Compression Map

| canonical_archetype_id | fine/deep sub-archetype | compression rule |
|---|---|---|
| C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN | REGIONAL_BANK_ROE_CAPITAL_RETURN_EXECUTION | policy/value-up signal is useful only when ROE, CET1/capital return, and shareholder-return execution bridge are visible |
| C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN | POLICY_ONLY_FINANCIAL_RERATING_TRAP | policy event plus low PBR is insufficient if credit cost, earnings beta, or weak execution blocks capital return |
| C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN | BROKERAGE_BETA_WITHOUT_ROE_BRIDGE | brokerage price beta should not be promoted like bank/insurance capital-return quality unless earnings visibility and buyback/dividend bridge improve |

## 7. Case Selection Summary

| case_id | symbol | company | role | representative trigger | entry_price | MFE_90D | MAE_90D | current_profile_verdict |
|---|---|---|---|---|---:|---:|---:|---|
| R6L71_C21_175330_VALUEUP_POS | 175330 | JB금융지주 | structural_success | Stage2-Actionable | 13610 | 18.66 | -16.31 | current_profile_too_early |
| R6L71_C21_138930_VALUEUP_POS | 138930 | BNK금융지주 | structural_success | Stage2-Actionable | 7720 | 16.58 | -5.18 | current_profile_correct |
| R6L71_C21_139130_POLICY_COUNTER | 139130 | DGB금융지주/iM금융지주 | failed_rerating | Stage2-Actionable | 9230 | 1.95 | -16.03 | current_profile_false_positive |
| R6L71_C21_006800_POLICY_COUNTER | 006800 | 미래에셋증권 | failed_rerating | Stage2-Actionable | 8660 | 5.77 | -19.98 | current_profile_false_positive |

## 8. Positive vs Counterexample Balance

| bucket | count | cases |
|---|---:|---|
| positive_structural_success | 2 | JB금융지주, BNK금융지주 |
| counterexample_or_failed_rerating | 2 | DGB금융지주/iM금융지주, 미래에셋증권 |
| 4B_or_4C_case | 2 | JB금융지주 2024-10-25/11-12 risk overlay, BNK금융지주 2024-08-26 risk overlay |
| calibration_usable_case_count | 4 | all representative cases |

## 9. Evidence Source Map

This is historical calibration, not live candidate research. Evidence is treated as of trigger date and not upgraded with hindsight.

| evidence family | as-of interpretation |
|---|---|
| policy_or_regulatory_optionality | 2024-02-26 Korea corporate value-up policy created sector-wide ROE/PBR/capital-return optionality |
| capital_return_quality | regional banks with higher visible shareholder-return discipline scored better than policy-only financials |
| relative_strength | stock-web 1D OHLC shows follow-through dispersion after the common event |
| credit_or_execution_risk | DGB/iM and brokerage beta cases required stricter bridge before Stage3 promotion |
| valuation/positioning overheat | later JB/BNK upside required 4B watch treatment rather than Green loosening |

## 10. Price Data Source Map

| symbol | tradable shard | profile |
|---|---|---|
| 175330 | atlas/ohlcv_tradable_by_symbol_year/175/175330/2024.csv | atlas/symbol_profiles/175/175330.json |
| 138930 | atlas/ohlcv_tradable_by_symbol_year/138/138930/2024.csv | atlas/symbol_profiles/138/138930.json |
| 139130 | atlas/ohlcv_tradable_by_symbol_year/139/139130/2024.csv | atlas/symbol_profiles/139/139130.json |
| 006800 | atlas/ohlcv_tradable_by_symbol_year/006/006800/2024.csv | atlas/symbol_profiles/006/006800.json |

## 11. Case-by-Case Trigger Grid

| trigger_id | case_id | trigger_type | trigger_date | entry_date | entry_price | stage2 evidence | stage3 evidence | 4B evidence | 4C evidence | calibration_usable |
|---|---|---|---|---|---:|---|---|---|---|---|
| T_R6L71_175330_S2 | R6L71_C21_175330_VALUEUP_POS | Stage2-Actionable | 2024-02-26 | 2024-02-27 | 13610 | policy_or_regulatory_optionality, relative_strength, early_revision_signal | capital_return_quality, ROE/PBR bridge later confirmed | none at entry | none | true |
| T_R6L71_138930_S2 | R6L71_C21_138930_VALUEUP_POS | Stage2-Actionable | 2024-02-26 | 2024-02-27 | 7720 | policy_or_regulatory_optionality, relative_strength, early_revision_signal | capital_return_quality, financial_visibility later confirmed | none at entry | none | true |
| T_R6L71_139130_S2 | R6L71_C21_139130_POLICY_COUNTER | Stage2-Actionable | 2024-02-26 | 2024-02-27 | 9230 | policy_or_regulatory_optionality | weak capital-return bridge, credit-cost watch | none at entry | thesis quality not broken, but promotion failed | true |
| T_R6L71_006800_S2 | R6L71_C21_006800_POLICY_COUNTER | Stage2-Actionable | 2024-02-26 | 2024-02-27 | 8660 | policy_or_regulatory_optionality, brokerage beta | no bank-like ROE/PBR bridge | none at entry | thesis quality not broken, but policy rerating failed | true |
| T_R6L71_175330_4B | R6L71_C21_175330_VALUEUP_POS | Stage4B-Overlay | 2024-10-25 | 2024-10-25 | 18290 | n/a | n/a | valuation_blowoff, positioning_overheat, capital_return_event_premium | none | true |
| T_R6L71_138930_4B | R6L71_C21_138930_VALUEUP_POS | Stage4B-Overlay | 2024-08-26 | 2024-08-26 | 10210 | n/a | n/a | valuation_blowoff, positioning_overheat | none | true |

## 12. Trigger-Level OHLC Backtest Tables

| trigger_id | entry | MFE_30D | MAE_30D | MFE_90D | MAE_90D | MFE_180D | MAE_180D | peak_date | peak_price | drawdown_after_peak |
|---|---:|---:|---:|---:|---:|---:|---:|---|---:|---:|
| T_R6L71_175330_S2 | 13610 | 3.60 | -10.29 | 18.66 | -16.31 | 38.06 | -16.31 | 2024-11-12 | 18790 | -5.53 |
| T_R6L71_138930_S2 | 7720 | 8.94 | -5.18 | 16.58 | -5.18 | 33.94 | -5.18 | 2024-08-26 | 10340 | -12.57 |
| T_R6L71_139130_S2 | 9230 | 1.95 | -9.97 | 1.95 | -16.03 | 1.95 | -19.39 | 2024-03-15 | 9410 | -20.93 |
| T_R6L71_006800_S2 | 8660 | 5.77 | -14.32 | 5.77 | -19.98 | 5.77 | -19.98 | 2024-02-29 | 9160 | -24.34 |
| T_R6L71_175330_4B | 18290 | 2.73 | -5.30 | 12.08 | -11.75 | null | null | 2024-12-03 | 20500 | -21.56 |
| T_R6L71_138930_4B | 10210 | 1.27 | -11.46 | 1.27 | -12.93 | null | null | 2024-08-26 | 10340 | -12.93 |

## 13. Current Calibrated Profile Stress Test

| case | P0 likely label | realized path | verdict | interpretation |
|---|---|---|---|---|
| JB금융지주 | Stage2-Actionable, maybe Yellow after execution evidence | large 180D upside but high early MAE | current_profile_too_early | Stage2 was useful, but Green should wait for capital-return/ROE bridge because early MAE was high |
| BNK금융지주 | Stage2-Actionable | positive MFE with manageable MAE | current_profile_correct | sector value-up Stage2 worked when price and capital-return quality aligned |
| DGB/iM금융지주 | Stage2-Actionable if policy-only bonus over-applies | low MFE, large MAE | current_profile_false_positive | policy optionality without capital-return/credit-quality bridge should be watch only |
| 미래에셋증권 | Stage2-Actionable if low-PBR financial proxy is overbroad | low MFE, large MAE | current_profile_false_positive | brokerage beta should not inherit bank-style capital-return credit without ROE/earnings bridge |

Stress-test answers:

1. Current calibrated profile would likely recognize the 2024-02-26 value-up policy as a Stage2 candidate signal across C21.
2. That was aligned for BNK and eventually JB, but failed for DGB/iM and 미래에셋증권.
3. The Stage2 bonus was useful but too broad if triggered by policy alone.
4. Yellow threshold 75 should be kept; early promotion would have admitted high-MAE cases.
5. Green threshold 87 / revision 55 should be kept; Green loosening is not supported.
6. Price-only blowoff guard remains appropriate.
7. Full 4B non-price requirement remains appropriate; JB/BNK overlays are risk overlays, not immediate thesis breaks.
8. Hard 4C routing is not activated; these are failed rerating / watch cases rather than hard thesis breaks.

## 14. Stage2 / Yellow / Green Comparison

| case | Stage2 entry | hypothetical Green condition | green_lateness_ratio | audit |
|---|---:|---|---:|---|
| JB금융지주 | 13610 | after capital-return/ROE confirmation and price already near 15k~16k | 0.30~0.50 | Green could be later but should not be loosened because early MAE was severe |
| BNK금융지주 | 7720 | after rerating durability and capital-return execution | 0.35~0.55 | Yellow/Green delay acceptable; Stage2 captured enough upside |
| DGB/iM금융지주 | 9230 | no confirmed Green | not_applicable | no Green promotion should occur |
| 미래에셋증권 | 8660 | no confirmed Green | not_applicable | no Green promotion should occur |

## 15. 4B Local vs Full-window Timing Audit

| trigger | stage2_entry | 4B entry | local peak | full observed peak | local proximity | full-window proximity | verdict |
|---|---:|---:|---:|---:|---:|---:|---|
| JB 4B overlay | 13610 | 18290 | 18790 | 20500 | 0.90 | 0.68 | local_4B_watch_not_full_exit |
| BNK 4B overlay | 7720 | 10210 | 10340 | 10340 | 0.95 | 0.95 | good_full_window_4B_timing |

JB illustrates why 4B must split local and full-window proximity. The 2024-10-25 overlay was close to a local peak, but a later 2024-12 high remained possible. BNK’s 2024-08-26 overlay was closer to the full observed peak and worked better as a full-window 4B watch.

## 16. 4C Protection Audit

No hard 4C row is promoted in this loop. DGB/iM and 미래에셋증권 are failed rerating / false-positive Stage2 cases, not hard thesis-break cases. The correct protection is stricter Stage2 bridge / Stage3 promotion gate rather than 4C routing.

## 17. Sector-Specific Rule Candidate

```text
rule_scope = sector_specific
large_sector_id = L6_FINANCIAL_CAPITAL_RETURN_DIGITAL
candidate_rule = financial_valueup_stage2_requires_capital_return_or_roe_quality_bridge
```

For L6 financials, a policy/value-up event can produce Stage2 watch, but Stage2-Actionable should require at least one non-price bridge: executed or clearly announced shareholder return, ROE/PBR rerating math, capital adequacy/credit-cost comfort, or earnings visibility. Without that bridge, policy-only low-PBR names should remain watch-only.

## 18. Canonical-Archetype Rule Candidate

```text
rule_scope = canonical_archetype_specific
canonical_archetype_id = C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN
candidate_rule = C21_policy_only_financials_require_executed_capital_return_or_ROE_quality_bridge
```

C21 should separate:

- bank/financial-holding capital-return execution cases,
- regional-bank credit-cost drag cases,
- brokerage beta cases without ROE/PBR capital-return conversion.

This does not weaken the existing Stage2 bonus globally. It scopes the bonus behind a capital-return/ROE quality bridge.

## 19. Before / After Backtest Comparison

| profile | hypothesis | selected triggers | avg MFE_90 | avg MAE_90 | false-positive rate | score-return alignment |
|---|---|---:|---:|---:|---:|---|
| P0 e2r_2_1_stock_web_calibrated_proxy | broad C21 policy/value-up Stage2 allowed | 4 | 10.74 | -14.38 | 50% | mixed |
| P0b e2r_2_0_baseline_reference | slower recognition, less Stage2 policy credit | 2 | 17.62 | -10.75 | 0~25% | misses some early positives |
| P1 sector_specific_candidate_profile | L6 requires capital-return/ROE bridge | 2 | 17.62 | -10.75 | 0% | improved precision, lower coverage |
| P2 canonical_archetype_candidate_profile | C21 bridge by ROE/PBR + shareholder return | 2 | 17.62 | -10.75 | 0% | improved C21 precision |
| P3 counterexample_guard_profile | policy-only / brokerage beta watch-only | 2 rejected | 3.86 | -18.01 | n/a | rejects false positives |

## 20. Score-Return Alignment Matrix

| case | raw component summary before | weighted score before | stage before | weighted score after | stage after | alignment |
|---|---|---:|---|---:|---|---|
| JB금융지주 | policy 14, relative strength 12, capital return 12, ROE bridge 12, risk 8 | 72 | Stage2-Actionable | 75 | Stage2-Actionable / Yellow-watch | aligned with upside but high-MAE watch |
| BNK금융지주 | policy 14, relative strength 14, capital return 14, ROE bridge 13, risk 6 | 76 | Stage2-Actionable | 78 | Stage2-Actionable / Yellow-watch | aligned |
| DGB/iM금융지주 | policy 14, relative strength 4, capital return 4, credit risk 16 | 66 | Stage2-Watch or false Stage2 | 58 | Watch-only | improved rejection |
| 미래에셋증권 | policy 14, brokerage beta 8, capital return 4, earnings beta risk 15 | 65 | Stage2-Watch or false Stage2 | 57 | Watch-only | improved rejection |

## 21. Coverage Matrix

| large_sector_id | canonical_archetype_id | fine_archetype_id | positive_case_count | counterexample_count | 4B_case_count | 4C_case_count | new_independent_case_count | reused_case_count | calibration_usable_trigger_count | representative_trigger_count | current_profile_error_count | sector_rule_candidate | canonical_rule_candidate | coverage_gap_after_this_loop |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|---|---|
| L6_FINANCIAL_CAPITAL_RETURN_DIGITAL | C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN | REGIONAL_FINANCIAL_VALUEUP_CAPITAL_RETURN_CREDIT_COST_SPLIT | 2 | 2 | 2 | 0 | 4 | 0 | 6 | 4 | 2 | true | true | more non-bank C21 counterexamples and non-price 4B overlays still useful |

## 22. Residual Contribution Summary

```text
new_independent_case_count: 4
reused_case_count: 0
reused_case_ids: []
new_symbol_count: 4
new_canonical_archetype_count: 0
new_fine_archetype_count: 1
new_trigger_family_count: 2
tested_existing_calibrated_axes: [stage2_actionable_evidence_bonus, stage3_yellow_total_min, stage3_green_total_min, full_4b_requires_non_price_evidence]
residual_error_types_found: [policy_only_stage2_false_positive, brokerage_beta_without_capital_return_bridge, local_4B_vs_full_window_split]
new_axis_proposed: C21_policy_only_financials_require_executed_capital_return_or_ROE_quality_bridge
existing_axis_strengthened: stage2_actionable_evidence_bonus_requires_non_price_bridge_in_C21; full_4b_requires_non_price_evidence
existing_axis_weakened: null
existing_axis_kept: stage3_yellow_total_min; stage3_green_total_min; stage3_green_revision_min; hard_4c_thesis_break_routes_to_4c
sector_specific_rule_candidate: true
canonical_archetype_rule_candidate: true
no_new_signal_reason: null
loop_contribution_label: canonical_archetype_rule_candidate
do_not_propose_new_weight_delta: false
```

## 23. Validation Scope / Non-Validation Scope

Validation scope:

- Uses Songdaiki/stock-web tradable_raw OHLCV rows.
- Uses 2024-02-27 close as conservative entry price for the 2024-02-26 policy event.
- Uses 30D/90D/180D MFE/MAE windows and 4B local/full proximity split.
- Uses no live candidate scan and no current recommendation language.

Non-validation scope:

- Does not assert production scoring changes.
- Does not use future MFE/MAE as runtime scoring input.
- Does not open or patch stock_agent code.
- Does not promote global deltas.

## 24. Shadow Weight Calibration

```csv
row_type,axis,scope,large_sector_id,canonical_archetype_id,baseline_value,tested_value,delta,reason,backtest_effect,trigger_ids,calibration_usable_count,new_independent_case_count,counterexample_count,confidence,proposal_type,notes
shadow_weight,C21_policy_only_financials_require_executed_capital_return_or_ROE_quality_bridge,canonical_archetype_specific,L6_FINANCIAL_CAPITAL_RETURN_DIGITAL,C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN,0,1,+1,"policy-only value-up triggers split sharply; capital-return/ROE bridge separates positives from false positives","rejects DGB/iM and Mirae-style false positives while keeping JB/BNK",T_R6L71_175330_S2|T_R6L71_138930_S2|T_R6L71_139130_S2|T_R6L71_006800_S2,4,4,2,medium,canonical_shadow_only,"not production; post-calibrated residual"
shadow_weight,C21_local_4B_watch_vs_full_4B_split,canonical_archetype_specific,L6_FINANCIAL_CAPITAL_RETURN_DIGITAL,C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN,0,1,+1,"JB local 4B was early vs full-window peak; BNK full-window 4B worked better","keeps full_4b_requires_non_price_evidence and separates local watch from full overlay",T_R6L71_175330_4B|T_R6L71_138930_4B,2,2,0,low,canonical_shadow_only,"4B overlay/risk calibration only"
```

## 25. Machine-Readable Rows

### 25.1 price_source_validation

```jsonl
{"row_type":"price_source_validation","source":"Songdaiki/stock-web","source_url":"https://github.com/Songdaiki/stock-web","manifest_path":"atlas/manifest.json","schema_path":"atlas/schema.json","universe_path":"atlas/universe/all_symbols.csv","manifest_max_date":"2026-02-20","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","calibration_shard_root":"atlas/ohlcv_tradable_by_symbol_year","raw_shard_root":"atlas/ohlcv_raw_by_symbol_year","validation_status":"usable_for_historical_calibration"}
```

### 25.2 case rows

```jsonl
{"row_type":"case","case_id":"R6L71_C21_175330_VALUEUP_POS","symbol":"175330","company_name":"JB금융지주","round":"R6","loop":"71","large_sector_id":"L6_FINANCIAL_CAPITAL_RETURN_DIGITAL","canonical_archetype_id":"C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN","fine_archetype_id":"REGIONAL_FINANCIAL_VALUEUP_CAPITAL_RETURN_CREDIT_COST_SPLIT","case_type":"structural_success","positive_or_counterexample":"positive","best_trigger":"T_R6L71_175330_S2","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"positive_after_high_MAE","current_profile_verdict":"current_profile_too_early","price_source":"Songdaiki/stock-web","notes":"Regional bank value-up succeeded but required ROE/capital-return bridge; early MAE argues against Green loosening."}
{"row_type":"case","case_id":"R6L71_C21_138930_VALUEUP_POS","symbol":"138930","company_name":"BNK금융지주","round":"R6","loop":"71","large_sector_id":"L6_FINANCIAL_CAPITAL_RETURN_DIGITAL","canonical_archetype_id":"C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN","fine_archetype_id":"REGIONAL_FINANCIAL_VALUEUP_CAPITAL_RETURN_CREDIT_COST_SPLIT","case_type":"structural_success","positive_or_counterexample":"positive","best_trigger":"T_R6L71_138930_S2","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"aligned","current_profile_verdict":"current_profile_correct","price_source":"Songdaiki/stock-web","notes":"Stage2 value-up signal aligned with manageable MAE and strong 180D MFE."}
{"row_type":"case","case_id":"R6L71_C21_139130_POLICY_COUNTER","symbol":"139130","company_name":"DGB금융지주/iM금융지주","round":"R6","loop":"71","large_sector_id":"L6_FINANCIAL_CAPITAL_RETURN_DIGITAL","canonical_archetype_id":"C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN","fine_archetype_id":"REGIONAL_FINANCIAL_VALUEUP_CAPITAL_RETURN_CREDIT_COST_SPLIT","case_type":"failed_rerating","positive_or_counterexample":"counterexample","best_trigger":"T_R6L71_139130_S2","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"false_positive_policy_only","current_profile_verdict":"current_profile_false_positive","price_source":"Songdaiki/stock-web","notes":"Policy-only signal did not convert into strong rerating; credit/ROE quality bridge was insufficient."}
{"row_type":"case","case_id":"R6L71_C21_006800_POLICY_COUNTER","symbol":"006800","company_name":"미래에셋증권","round":"R6","loop":"71","large_sector_id":"L6_FINANCIAL_CAPITAL_RETURN_DIGITAL","canonical_archetype_id":"C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN","fine_archetype_id":"REGIONAL_FINANCIAL_VALUEUP_CAPITAL_RETURN_CREDIT_COST_SPLIT","case_type":"failed_rerating","positive_or_counterexample":"counterexample","best_trigger":"T_R6L71_006800_S2","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"false_positive_brokerage_beta","current_profile_verdict":"current_profile_false_positive","price_source":"Songdaiki/stock-web","notes":"Brokerage beta and value-up policy did not behave like bank capital-return rerating."}
```

### 25.3 trigger rows

```jsonl
{"row_type":"trigger","trigger_id":"T_R6L71_175330_S2","case_id":"R6L71_C21_175330_VALUEUP_POS","symbol":"175330","company_name":"JB금융지주","round":"R6","loop":"71","large_sector_id":"L6_FINANCIAL_CAPITAL_RETURN_DIGITAL","canonical_archetype_id":"C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN","fine_archetype_id":"REGIONAL_FINANCIAL_VALUEUP_CAPITAL_RETURN_CREDIT_COST_SPLIT","sector":"financial","primary_archetype":"ROE/PBR capital return","loop_objective":"residual_false_positive_mining|stage2_actionable_bonus_stress_test|sector_specific_rule_discovery","trigger_type":"Stage2-Actionable","trigger_date":"2024-02-26","evidence_available_at_that_date":"Korea value-up policy optionality; regional bank ROE/PBR and capital-return setup visible but exact policy timing treated as next-trading-day entry","evidence_source":"public policy event + stock-web OHLC path","stage2_evidence_fields":["policy_or_regulatory_optionality","relative_strength","early_revision_signal"],"stage3_evidence_fields":["financial_visibility","capital_return_quality","ROE_PBR_bridge"],"stage4b_evidence_fields":[],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/175/175330/2024.csv","profile_path":"atlas/symbol_profiles/175/175330.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","entry_date":"2024-02-27","entry_price":13610,"MFE_30D_pct":3.60,"MFE_90D_pct":18.66,"MFE_180D_pct":38.06,"MFE_1Y_pct":null,"MFE_2Y_pct":null,"MAE_30D_pct":-10.29,"MAE_90D_pct":-16.31,"MAE_180D_pct":-16.31,"MAE_1Y_pct":null,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-11-12","peak_price":18790,"drawdown_after_peak_pct":-5.53,"green_lateness_ratio":0.40,"four_b_local_peak_proximity":null,"four_b_full_window_peak_proximity":null,"four_b_timing_verdict":null,"four_b_evidence_type":[],"four_c_protection_label":"not_applicable","trigger_outcome_label":"high_MAE_structural_success","current_profile_verdict":"current_profile_too_early","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"R6L71_C21_175330_2024-02-27_13610","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"T_R6L71_138930_S2","case_id":"R6L71_C21_138930_VALUEUP_POS","symbol":"138930","company_name":"BNK금융지주","round":"R6","loop":"71","large_sector_id":"L6_FINANCIAL_CAPITAL_RETURN_DIGITAL","canonical_archetype_id":"C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN","fine_archetype_id":"REGIONAL_FINANCIAL_VALUEUP_CAPITAL_RETURN_CREDIT_COST_SPLIT","sector":"financial","primary_archetype":"ROE/PBR capital return","loop_objective":"residual_false_positive_mining|stage2_actionable_bonus_stress_test|sector_specific_rule_discovery","trigger_type":"Stage2-Actionable","trigger_date":"2024-02-26","evidence_available_at_that_date":"Korea value-up policy optionality; regional bank capital-return setup; next-trading-day entry for timing conservatism","evidence_source":"public policy event + stock-web OHLC path","stage2_evidence_fields":["policy_or_regulatory_optionality","relative_strength","early_revision_signal"],"stage3_evidence_fields":["financial_visibility","capital_return_quality","low_red_team_risk"],"stage4b_evidence_fields":[],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/138/138930/2024.csv","profile_path":"atlas/symbol_profiles/138/138930.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","entry_date":"2024-02-27","entry_price":7720,"MFE_30D_pct":8.94,"MFE_90D_pct":16.58,"MFE_180D_pct":33.94,"MFE_1Y_pct":null,"MFE_2Y_pct":null,"MAE_30D_pct":-5.18,"MAE_90D_pct":-5.18,"MAE_180D_pct":-5.18,"MAE_1Y_pct":null,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-08-26","peak_price":10340,"drawdown_after_peak_pct":-12.57,"green_lateness_ratio":0.45,"four_b_local_peak_proximity":null,"four_b_full_window_peak_proximity":null,"four_b_timing_verdict":null,"four_b_evidence_type":[],"four_c_protection_label":"not_applicable","trigger_outcome_label":"structural_success","current_profile_verdict":"current_profile_correct","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"R6L71_C21_138930_2024-02-27_7720","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"T_R6L71_139130_S2","case_id":"R6L71_C21_139130_POLICY_COUNTER","symbol":"139130","company_name":"DGB금융지주/iM금융지주","round":"R6","loop":"71","large_sector_id":"L6_FINANCIAL_CAPITAL_RETURN_DIGITAL","canonical_archetype_id":"C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN","fine_archetype_id":"REGIONAL_FINANCIAL_VALUEUP_CAPITAL_RETURN_CREDIT_COST_SPLIT","sector":"financial","primary_archetype":"policy-only low-PBR trap","loop_objective":"counterexample_mining|stage2_actionable_bonus_stress_test","trigger_type":"Stage2-Actionable","trigger_date":"2024-02-26","evidence_available_at_that_date":"Korea value-up policy optionality, but weak capital-return/credit-quality bridge; next-trading-day entry for timing conservatism","evidence_source":"public policy event + stock-web OHLC path","stage2_evidence_fields":["policy_or_regulatory_optionality"],"stage3_evidence_fields":[],"stage4b_evidence_fields":[],"stage4c_evidence_fields":["thesis_evidence_broken"],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/139/139130/2024.csv","profile_path":"atlas/symbol_profiles/139/139130.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","entry_date":"2024-02-27","entry_price":9230,"MFE_30D_pct":1.95,"MFE_90D_pct":1.95,"MFE_180D_pct":1.95,"MFE_1Y_pct":null,"MFE_2Y_pct":null,"MAE_30D_pct":-9.97,"MAE_90D_pct":-16.03,"MAE_180D_pct":-19.39,"MAE_1Y_pct":null,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-03-15","peak_price":9410,"drawdown_after_peak_pct":-20.93,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":null,"four_b_full_window_peak_proximity":null,"four_b_timing_verdict":null,"four_b_evidence_type":[],"four_c_protection_label":"thesis_break_watch_only","trigger_outcome_label":"failed_rerating","current_profile_verdict":"current_profile_false_positive","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"R6L71_C21_139130_2024-02-27_9230","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"T_R6L71_006800_S2","case_id":"R6L71_C21_006800_POLICY_COUNTER","symbol":"006800","company_name":"미래에셋증권","round":"R6","loop":"71","large_sector_id":"L6_FINANCIAL_CAPITAL_RETURN_DIGITAL","canonical_archetype_id":"C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN","fine_archetype_id":"REGIONAL_FINANCIAL_VALUEUP_CAPITAL_RETURN_CREDIT_COST_SPLIT","sector":"financial","primary_archetype":"brokerage beta without ROE bridge","loop_objective":"counterexample_mining|stage2_actionable_bonus_stress_test","trigger_type":"Stage2-Actionable","trigger_date":"2024-02-26","evidence_available_at_that_date":"Korea value-up policy optionality, but brokerage earnings beta lacks bank-like ROE/PBR capital-return bridge; next-trading-day entry for timing conservatism","evidence_source":"public policy event + stock-web OHLC path","stage2_evidence_fields":["policy_or_regulatory_optionality"],"stage3_evidence_fields":[],"stage4b_evidence_fields":[],"stage4c_evidence_fields":["thesis_evidence_broken"],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/006/006800/2024.csv","profile_path":"atlas/symbol_profiles/006/006800.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","entry_date":"2024-02-27","entry_price":8660,"MFE_30D_pct":5.77,"MFE_90D_pct":5.77,"MFE_180D_pct":5.77,"MFE_1Y_pct":null,"MFE_2Y_pct":null,"MAE_30D_pct":-14.32,"MAE_90D_pct":-19.98,"MAE_180D_pct":-19.98,"MAE_1Y_pct":null,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-02-29","peak_price":9160,"drawdown_after_peak_pct":-24.34,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":null,"four_b_full_window_peak_proximity":null,"four_b_timing_verdict":null,"four_b_evidence_type":[],"four_c_protection_label":"thesis_break_watch_only","trigger_outcome_label":"failed_rerating","current_profile_verdict":"current_profile_false_positive","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"R6L71_C21_006800_2024-02-27_8660","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"T_R6L71_175330_4B","case_id":"R6L71_C21_175330_VALUEUP_POS","symbol":"175330","company_name":"JB금융지주","round":"R6","loop":"71","large_sector_id":"L6_FINANCIAL_CAPITAL_RETURN_DIGITAL","canonical_archetype_id":"C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN","fine_archetype_id":"REGIONAL_FINANCIAL_VALUEUP_CAPITAL_RETURN_CREDIT_COST_SPLIT","sector":"financial","primary_archetype":"ROE/PBR capital return 4B overlay","loop_objective":"4B_non_price_requirement_stress_test","trigger_type":"Stage4B-Overlay","trigger_date":"2024-10-25","evidence_available_at_that_date":"price and positioning overheat after capital-return rerating; local-vs-full-window split required","evidence_source":"stock-web OHLC path + valuation/positioning overlay proxy","stage2_evidence_fields":[],"stage3_evidence_fields":[],"stage4b_evidence_fields":["valuation_blowoff","positioning_overheat","explicit_event_cap"],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/175/175330/2024.csv","profile_path":"atlas/symbol_profiles/175/175330.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","entry_date":"2024-10-25","entry_price":18290,"MFE_30D_pct":2.73,"MFE_90D_pct":12.08,"MFE_180D_pct":null,"MFE_1Y_pct":null,"MFE_2Y_pct":null,"MAE_30D_pct":-5.30,"MAE_90D_pct":-11.75,"MAE_180D_pct":null,"MAE_1Y_pct":null,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-12-03","peak_price":20500,"drawdown_after_peak_pct":-21.56,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":0.90,"four_b_full_window_peak_proximity":0.68,"four_b_timing_verdict":"local_4B_watch_not_full_exit","four_b_evidence_type":["valuation_blowoff","positioning_overheat"],"four_c_protection_label":"not_applicable","trigger_outcome_label":"4B_too_early_local_only","current_profile_verdict":"current_profile_4B_too_early","calibration_usable":true,"forward_window_trading_days":90,"calibration_block_reasons":[],"corporate_action_window_status":"clean_90D_window","same_entry_group_id":"R6L71_C21_175330_2024-10-25_18290","dedupe_for_aggregate":false,"aggregate_group_role":"4B_overlay_only","is_new_independent_case":false,"reuse_reason":"4B overlay timing for already selected positive case","independent_evidence_weight":0.5,"do_not_count_as_new_case":true}
{"row_type":"trigger","trigger_id":"T_R6L71_138930_4B","case_id":"R6L71_C21_138930_VALUEUP_POS","symbol":"138930","company_name":"BNK금융지주","round":"R6","loop":"71","large_sector_id":"L6_FINANCIAL_CAPITAL_RETURN_DIGITAL","canonical_archetype_id":"C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN","fine_archetype_id":"REGIONAL_FINANCIAL_VALUEUP_CAPITAL_RETURN_CREDIT_COST_SPLIT","sector":"financial","primary_archetype":"ROE/PBR capital return 4B overlay","loop_objective":"4B_non_price_requirement_stress_test","trigger_type":"Stage4B-Overlay","trigger_date":"2024-08-26","evidence_available_at_that_date":"local/full-window peak proximity after value-up rerating; overlay only","evidence_source":"stock-web OHLC path + valuation/positioning overlay proxy","stage2_evidence_fields":[],"stage3_evidence_fields":[],"stage4b_evidence_fields":["valuation_blowoff","positioning_overheat"],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/138/138930/2024.csv","profile_path":"atlas/symbol_profiles/138/138930.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","entry_date":"2024-08-26","entry_price":10210,"MFE_30D_pct":1.27,"MFE_90D_pct":1.27,"MFE_180D_pct":null,"MFE_1Y_pct":null,"MFE_2Y_pct":null,"MAE_30D_pct":-11.46,"MAE_90D_pct":-12.93,"MAE_180D_pct":null,"MAE_1Y_pct":null,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-08-26","peak_price":10340,"drawdown_after_peak_pct":-12.93,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":0.95,"four_b_full_window_peak_proximity":0.95,"four_b_timing_verdict":"good_full_window_4B_timing","four_b_evidence_type":["valuation_blowoff","positioning_overheat"],"four_c_protection_label":"not_applicable","trigger_outcome_label":"4B_overlay_success","current_profile_verdict":"current_profile_correct","calibration_usable":true,"forward_window_trading_days":90,"calibration_block_reasons":[],"corporate_action_window_status":"clean_90D_window","same_entry_group_id":"R6L71_C21_138930_2024-08-26_10210","dedupe_for_aggregate":false,"aggregate_group_role":"4B_overlay_only","is_new_independent_case":false,"reuse_reason":"4B overlay timing for already selected positive case","independent_evidence_weight":0.5,"do_not_count_as_new_case":true}
```

### 25.4 score_simulation rows

```jsonl
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"R6L71_C21_175330_VALUEUP_POS","trigger_id":"T_R6L71_175330_S2","symbol":"175330","large_sector_id":"L6_FINANCIAL_CAPITAL_RETURN_DIGITAL","canonical_archetype_id":"C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN","raw_component_scores_before":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":8,"revision_score":12,"relative_strength_score":12,"customer_quality_score":0,"policy_or_regulatory_score":14,"valuation_repricing_score":12,"execution_risk_score":8,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0,"roe_pbr_capital_return_score":12},"weighted_score_before":72,"stage_label_before":"Stage2-Actionable","raw_component_scores_after":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":8,"revision_score":12,"relative_strength_score":12,"customer_quality_score":0,"policy_or_regulatory_score":14,"valuation_repricing_score":12,"execution_risk_score":8,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0,"roe_pbr_capital_return_score":15},"weighted_score_after":75,"stage_label_after":"Stage2-Actionable/Yellow-watch","changed_components":["roe_pbr_capital_return_score"],"component_delta_explanation":"ROE/capital-return bridge allows Stage2 but high early MAE prevents Green loosening.","MFE_90D_pct":18.66,"MAE_90D_pct":-16.31,"score_return_alignment_label":"positive_high_MAE","current_profile_verdict":"current_profile_too_early"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"R6L71_C21_138930_VALUEUP_POS","trigger_id":"T_R6L71_138930_S2","symbol":"138930","large_sector_id":"L6_FINANCIAL_CAPITAL_RETURN_DIGITAL","canonical_archetype_id":"C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN","raw_component_scores_before":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":8,"revision_score":12,"relative_strength_score":14,"customer_quality_score":0,"policy_or_regulatory_score":14,"valuation_repricing_score":12,"execution_risk_score":6,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0,"roe_pbr_capital_return_score":14},"weighted_score_before":76,"stage_label_before":"Stage2-Actionable","raw_component_scores_after":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":8,"revision_score":12,"relative_strength_score":14,"customer_quality_score":0,"policy_or_regulatory_score":14,"valuation_repricing_score":12,"execution_risk_score":6,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0,"roe_pbr_capital_return_score":16},"weighted_score_after":78,"stage_label_after":"Stage2-Actionable/Yellow-watch","changed_components":["roe_pbr_capital_return_score"],"component_delta_explanation":"Capital-return/ROE bridge supports Stage2 and forward MFE/MAE alignment.","MFE_90D_pct":16.58,"MAE_90D_pct":-5.18,"score_return_alignment_label":"aligned","current_profile_verdict":"current_profile_correct"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"R6L71_C21_139130_POLICY_COUNTER","trigger_id":"T_R6L71_139130_S2","symbol":"139130","large_sector_id":"L6_FINANCIAL_CAPITAL_RETURN_DIGITAL","canonical_archetype_id":"C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN","raw_component_scores_before":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":3,"revision_score":4,"relative_strength_score":4,"customer_quality_score":0,"policy_or_regulatory_score":14,"valuation_repricing_score":10,"execution_risk_score":16,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0,"roe_pbr_capital_return_score":4},"weighted_score_before":66,"stage_label_before":"Stage2-Watch/false Stage2 risk","raw_component_scores_after":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":3,"revision_score":4,"relative_strength_score":4,"customer_quality_score":0,"policy_or_regulatory_score":8,"valuation_repricing_score":8,"execution_risk_score":18,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0,"roe_pbr_capital_return_score":2},"weighted_score_after":58,"stage_label_after":"Watch-only","changed_components":["policy_or_regulatory_score","roe_pbr_capital_return_score","execution_risk_score"],"component_delta_explanation":"Policy-only signal loses credit when capital-return/credit-quality bridge is absent.","MFE_90D_pct":1.95,"MAE_90D_pct":-16.03,"score_return_alignment_label":"rejects_false_positive","current_profile_verdict":"current_profile_false_positive"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"R6L71_C21_006800_POLICY_COUNTER","trigger_id":"T_R6L71_006800_S2","symbol":"006800","large_sector_id":"L6_FINANCIAL_CAPITAL_RETURN_DIGITAL","canonical_archetype_id":"C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN","raw_component_scores_before":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":4,"revision_score":5,"relative_strength_score":8,"customer_quality_score":0,"policy_or_regulatory_score":14,"valuation_repricing_score":10,"execution_risk_score":15,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0,"roe_pbr_capital_return_score":4},"weighted_score_before":65,"stage_label_before":"Stage2-Watch/false Stage2 risk","raw_component_scores_after":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":4,"revision_score":5,"relative_strength_score":5,"customer_quality_score":0,"policy_or_regulatory_score":8,"valuation_repricing_score":8,"execution_risk_score":17,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0,"roe_pbr_capital_return_score":2},"weighted_score_after":57,"stage_label_after":"Watch-only","changed_components":["relative_strength_score","policy_or_regulatory_score","roe_pbr_capital_return_score","execution_risk_score"],"component_delta_explanation":"Brokerage beta cannot inherit bank-style capital-return Stage2 credit without ROE/earnings bridge.","MFE_90D_pct":5.77,"MAE_90D_pct":-19.98,"score_return_alignment_label":"rejects_false_positive","current_profile_verdict":"current_profile_false_positive"}
```

### 25.5 shadow_weight rows

```csv
row_type,axis,scope,large_sector_id,canonical_archetype_id,baseline_value,tested_value,delta,reason,backtest_effect,trigger_ids,calibration_usable_count,new_independent_case_count,counterexample_count,confidence,proposal_type,notes
shadow_weight,C21_policy_only_financials_require_executed_capital_return_or_ROE_quality_bridge,canonical_archetype_specific,L6_FINANCIAL_CAPITAL_RETURN_DIGITAL,C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN,0,1,+1,"policy/value-up headline alone over-admits weak bridge names","keeps JB/BNK positives and rejects DGB/iM + Mirae counterexamples",T_R6L71_175330_S2|T_R6L71_138930_S2|T_R6L71_139130_S2|T_R6L71_006800_S2,4,4,2,medium,canonical_shadow_only,"not production; post-calibrated residual"
shadow_weight,C21_local_4B_watch_vs_full_4B_split,canonical_archetype_specific,L6_FINANCIAL_CAPITAL_RETURN_DIGITAL,C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN,0,1,+1,"local 4B peak proximity can be early in financial reratings","separates JB local watch from BNK fuller 4B timing",T_R6L71_175330_4B|T_R6L71_138930_4B,2,0,0,low,canonical_shadow_only,"4B overlay/risk calibration only"
```

### 25.6 residual_contribution row

```jsonl
{"row_type":"residual_contribution","round":"R6","loop":"71","scheduled_round":"R6","scheduled_loop":"71","round_schedule_status":"valid","round_sector_consistency":"pass","large_sector_id":"L6_FINANCIAL_CAPITAL_RETURN_DIGITAL","canonical_archetype_id":"C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN","fine_archetype_id":"REGIONAL_FINANCIAL_VALUEUP_CAPITAL_RETURN_CREDIT_COST_SPLIT","new_independent_case_count":4,"reused_case_count":0,"new_symbol_count":4,"same_archetype_new_symbol_count":4,"same_archetype_new_trigger_family_count":2,"new_trigger_family_count":2,"positive_case_count":2,"counterexample_count":2,"current_profile_error_count":2,"tested_existing_calibrated_axes":["stage2_actionable_evidence_bonus","stage3_yellow_total_min","stage3_green_total_min","full_4b_requires_non_price_evidence"],"residual_error_types_found":["policy_only_stage2_false_positive","brokerage_beta_without_capital_return_bridge","local_4B_vs_full_window_split"],"diversity_score_summary":"new_symbols=4,new_trigger_family=2,counterexamples=2,residual_errors=2,wrong_round_penalty=0","loop_contribution_label":"canonical_archetype_rule_candidate","do_not_propose_new_weight_delta":false}
```

### 25.7 narrative_only rows

```jsonl
{"row_type":"narrative_only","case_id":"R6L71_C21_NO_HARD_4C","symbol":"MULTI","large_sector_id":"L6_FINANCIAL_CAPITAL_RETURN_DIGITAL","canonical_archetype_id":"C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN","reason":"failed_rerating_cases_are_watch_or_false_positive_not_hard_4C","price_source":"Songdaiki/stock-web","usage":"not_weight_calibration"}
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
completed_round = R6
completed_loop = 71
next_round = R7
next_loop = 71
round_schedule_status = valid
round_sector_consistency = pass
```

## 28. Source Notes

- Price source: Songdaiki/stock-web, `atlas/manifest.json`, max date 2026-02-20.
- All OHLC rows use `tradable_raw` stock-web shards under `atlas/ohlcv_tradable_by_symbol_year`.
- The 2024-02-26 value-up policy event is used as a historical sector trigger; entry is set to 2024-02-27 close because exact publication/trading reaction timing is treated conservatively.
- This MD intentionally avoids current/live candidate language and contains no investment recommendation.

