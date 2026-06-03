# E2R Stock-Web Historical Calibration / Sector-Archetype Residual Research Round

## 0. Research Metadata

```text
scheduled_round: R6
scheduled_loop: 75
round_schedule_status: valid
round_sector_consistency: pass
computed_next_round: R7
computed_next_loop: 75
large_sector_id: L6_FINANCIAL_CAPITAL_RETURN_DIGITAL
canonical_archetype_id: C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN
fine_archetype_id: C21_ROE_PBR_CAPITAL_RETURN_EARNINGS_BRIDGE_GUARD
loop_objective: coverage_gap_fill | counterexample_mining | stage2_actionable_bonus_stress_test | 4B_non_price_requirement_stress_test | canonical_archetype_compression
price_source: Songdaiki/stock-web
stock_web_manifest_max_date: 2026-02-20
production_scoring_changed: false
shadow_weight_only: true
```

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

## 2. Round / Large Sector / Canonical Archetype Scope

R6 maps to `L6_FINANCIAL_CAPITAL_RETURN_DIGITAL`. The previous R6 loop used C22 insurance/rate-cycle, so this run rotates to C21 financial ROE/PBR/capital-return. The selected branch avoids the top-covered bank/holding cluster and focuses on brokerage/financial-holdco value-up where ROE and shareholder-return bridge is real versus small-finance theme heat.

| layer | id | definition |
|---|---|---|
| round | R6 | financial / capital return / digital |
| large_sector | L6_FINANCIAL_CAPITAL_RETURN_DIGITAL | banks, brokers, insurers, financial holdings, capital return |
| canonical | C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN | ROE recovery, PBR repair, capital-return bridge |
| fine | C21_ROE_PBR_CAPITAL_RETURN_EARNINGS_BRIDGE_GUARD | financial value-up signal must become ROE/PBR/capital-return evidence |
| deep | FINANCIAL_HOLDCO_BROKERAGE_ROE_RECOVERY_TO_PBR_REPAIR_AND_SHAREHOLDER_RETURN | financial holdco positive |
| deep | BROKERAGE_TRADING_INCOME_AND_DIVIDEND_VISIBILITY_TO_ROE_PBR_REPAIR | brokerage positive |
| deep | SMALL_SECURITIES_PBR_THEME_WITHOUT_ROE_RECOVERY_DIVIDEND_OR_CAPITAL_RETURN_EXECUTION | small-securities false positive |

## 3. No-Repeat / Coverage Check

No-Repeat hard duplicate key:

```text
canonical_archetype_id + symbol + trigger_type + entry_date
```

C21 top-covered symbols are `105560`, `323410`, `086790`, `UNKNOWN_SYMBOL`, `006220`, and `055550`. This run avoids that cluster and also avoids the previous R6/C22 insurance representatives `000370`, `082640`, and `000540`.

| archetype | selected symbol | duplicate status | reason |
|---|---:|---|---|
| C21 | 071050 | new independent | not top-covered C21 symbol; financial holdco ROE/PBR/capital-return bridge |
| C21 | 016360 | new independent | not top-covered C21 symbol; brokerage dividend/ROE/capital-return bridge |
| C21 | 001510 | new independent | not top-covered C21 symbol; small securities value-up theme without durable ROE/capital-return bridge |

## 4. Stock-Web OHLC Input / Price Source Validation

```jsonl
{"row_type":"price_source_validation","source":"Songdaiki/stock-web","source_url":"https://github.com/Songdaiki/stock-web","manifest_path":"atlas/manifest.json","schema_path":"atlas/schema.json","universe_path":"atlas/universe/all_symbols.csv","manifest_max_date":"2026-02-20","source_name":"FinanceData/marcap","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","calibration_shard_root":"atlas/ohlcv_tradable_by_symbol_year","raw_shard_root":"atlas/ohlcv_raw_by_symbol_year","validation_status":"usable_for_historical_calibration"}
```

Stock-web assumptions:

```text
source_name = FinanceData/marcap
price_adjustment_status = raw_unadjusted_marcap
min_date = 1995-05-02
max_date = 2026-02-20
tradable_row_count = 14354401
symbol_count = 5414
calibration_shard_root = atlas/ohlcv_tradable_by_symbol_year
tradable columns = d,o,h,l,c,v,a,mc,s,m
```

## 5. Historical Eligibility Gate

```text
entry row exists = true
forward 180 trading days available = true
MFE/MAE 30D/90D/180D computed = true
price_basis = tradable_raw
price_adjustment_status = raw_unadjusted_marcap
corporate_action_window_status = clean_180D_window
```

Corporate-action caveat:

```text
071050 has no corporate-action candidate dates.
016360 has corporate-action candidates ending 2001, outside the selected 2024 representative window.
001510 has corporate-action candidates ending 2018, outside the selected 2024 representative window.
All three representative 180D windows are treated as clean for this residual calibration.
```

## 6. Case Selection Summary

| role | symbol | company | trigger | entry | price | result |
|---|---:|---|---|---:|---:|---|
| financial_holdco_success_then_4B_watch | 071050 | 한국금융지주 | Stage2-Actionable | 2024-01-29 | 58700 | ROE/PBR/capital-return bridge worked, but Green blocked |
| brokerage_capital_return_success_then_4B_watch | 016360 | 삼성증권 | Stage2-Actionable | 2024-01-29 | 36950 | brokerage dividend/ROE/capital-return bridge worked, but 4B drawdown watch required |
| small_securities_theme_low_MFE_high_MAE_counterexample | 001510 | SK증권 | Stage2-Actionable | 2024-02-01 | 647 | small-securities value-up theme lacked ROE/capital-return bridge |

## 7. Positive vs Counterexample Balance

```text
positive_case_count: 2
counterexample_count: 1
4B_case_count: 3
4C_or_high_MAE_watch_count: 2
calibration_usable_case_count: 3
current_profile_error_count: 1
```

## 8. Trigger-Level OHLC Backtest Table

| symbol | company | trigger | entry_date | entry_price | MFE30 | MFE90 | MFE180 | MAE30 | MAE90 | MAE180 | peak_date | peak_price | DD after peak |
|---:|---|---|---|---:|---:|---:|---:|---:|---:|---:|---|---:|---:|
| 071050 | 한국금융지주 | Stage2-Actionable | 2024-01-29 | 58700 | 28.11 | 28.11 | 32.37 | -2.21 | -2.21 | -2.21 | 2024-07-17 | 77700 | -19.05 |
| 016360 | 삼성증권 | Stage2-Actionable | 2024-01-29 | 36950 | 15.7 | 15.7 | 32.34 | -2.03 | -2.03 | -2.03 | 2024-08-26 | 48900 | -19.22 |
| 001510 | SK증권 | Stage2-Actionable | 2024-02-01 | 647 | 3.4 | 3.4 | 3.4 | -2.78 | -9.27 | -23.34 | 2024-02-19 | 669 | -25.86 |

## 9. Case-by-Case Notes

### 9.1 071050 / 한국금융지주 — financial holdco ROE/PBR bridge

The entry row is 2024-01-29 at 58,700. The 30D/90D path reached 75,200 and the wider window reached 77,700. This is a valid C21 positive because the signal was not just “value-up theme.” The bridge is brokerage/holdco ROE recovery, PBR discount repair and shareholder-return visibility. The post-peak low still requires 4B watch.

### 9.2 016360 / 삼성증권 — brokerage dividend/ROE capital-return bridge

The entry row is 2024-01-29 at 36,950. The 30D/90D path reached 42,750, and the broader window reached 48,900. This row validates the brokerage branch: dividend visibility, trading-income/fee ROE and PBR repair can carry a rerating. It still routes to Yellow plus 4B/drawdown watch, not Green loosening.

### 9.3 001510 / SK증권 — small securities value-up false positive

The entry row is 2024-02-01 at 647. The best 180D high was only 669, while the 180D low fell to 496. This is the C21 trap: a small securities or financial value-up label can create a small spike, but without ROE recovery, dividend visibility, shareholder-return execution or earnings bridge, it is a Watch/4B/high-MAE case.

## 10. Current Calibrated Profile Stress Test

| question | result |
|---|---|
| Stage2 actionable bonus too strong? | Yes when C21 treats small-finance value-up/PBR theme strength as enough evidence. |
| Stage3 Yellow threshold too loose? | Not globally; C21 needs ROE/PBR/capital-return/earnings bridge before Yellow. |
| Stage3 Green too strict? | Correct. This round reinforces strict Green. |
| Price-only blowoff guard appropriate? | Yes, especially for 001510 and for post-peak financial value-up crowding. |
| Full 4B non-price requirement appropriate? | Yes. 071050/016360 have non-price bridges; 001510 does not. |
| 4C timing issue? | High-MAE watch is useful; no immediate hard 4C production delta proposed. |

## 11. Stage2 / Yellow / Green Comparison

```text
071050:
  Stage2-Actionable = correct
  Stage3-Yellow = allowed after ROE/PBR/capital-return bridge
  Stage3-Green = reject unless shareholder-return execution and post-MFE durability clear

016360:
  Stage2-Actionable = correct
  Stage3-Yellow = allowed after brokerage ROE/dividend bridge
  Stage3-Green = reject because 4B drawdown and value-up crowding remain active

001510:
  Stage2-Actionable = too generous if based only on small securities/PBR value-up theme
  Stage3-Yellow = reject without ROE recovery, dividend/capital return or earnings bridge
  Stage3-Green = reject
```

## 12. 4B Local vs Full-window Timing Audit

| symbol | local_peak_proximity | full_window_peak_proximity | verdict |
|---:|---:|---:|---|
| 071050 | 0.92 | 1.00 | financial holdco ROE/PBR bridge positive but 4B watch |
| 016360 | 0.88 | 1.00 | brokerage ROE/capital-return positive but full-window 4B watch |
| 001510 | 1.00 | 1.00 | small securities theme local 4B watch, not positive stage |

## 13. Canonical-Archetype Rule Candidate

```text
canonical_archetype_rule_candidate: true
rule_scope: canonical_archetype_specific
rule_id: c21_requires_roe_pbr_capital_return_earnings_bridge

rule:
  For C21 financial ROE/PBR/capital-return rows, do not promote bank,
  brokerage, financial holding, value-up, PBR discount, or small-finance Stage2
  signals into Stage3-Yellow/Green unless at least one non-price bridge is visible:
  ROE recovery, PBR discount repair, dividend visibility, capital-return execution,
  shareholder-return policy, earnings revision, solvency/balance quality, or fee/trading-income durability.
```

## 14. Before / After Backtest Comparison

| profile | eligible triggers | avg MFE90 | avg MAE90 | false positive rate | verdict |
|---|---:|---:|---:|---:|---|
| P0 e2r_2_1_stock_web_calibrated_proxy | 3 | 15.74 | -4.5 | 33.3% | useful but can over-credit small-finance value-up theme |
| P0b e2r_2_0_baseline_reference | 3 | 15.74 | -4.5 | 0% | safer but may miss 071050/016360 |
| P1 sector_specific_candidate_profile | 3 | 15.74 | -4.5 | 33.3% | no broad L6 loosen |
| P2 canonical_archetype_candidate_profile | 2 selected positives | 21.91 | -2.12 | 0% after bridge gate | preferred shadow |
| P3 counterexample_guard_profile | 1 rejected | 3.4 | -9.27 | 0% after demotion | useful guard |

## 15. Score-Return Alignment Matrix

| case | current profile verdict | alignment |
|---|---|---|
| 071050 | current_profile_correct_but_no_green | ROE/PBR/capital-return bridge aligned with MFE but Green blocked by 4B |
| 016360 | current_profile_correct_with_drawdown_guard | brokerage dividend/ROE bridge aligned with MFE, but drawdown guard remains |
| 001510 | current_profile_false_positive | small securities value-up theme produced weak MFE and high MAE |

## 16. Coverage Matrix

| large_sector_id | canonical_archetype_id | fine_archetype_id | positive | counterexample | 4B | 4C/watch | new_independent | reused | usable_triggers | representative | profile_errors | sector_rule | canonical_rule | coverage_gap_after |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|---|---|
| L6_FINANCIAL_CAPITAL_RETURN_DIGITAL | C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN | C21_ROE_PBR_CAPITAL_RETURN_EARNINGS_BRIDGE_GUARD | 2 | 1 | 3 | 2 | 3 | 0 | 3 | 3 | 1 | false | true | R6/C21 non-top-covered financial ROE/PBR/capital-return residual reduced |

## 17. Residual Contribution Summary

```text
new_independent_case_count: 3
reused_case_count: 0
reused_case_ids: []
new_symbol_count: 3
new_canonical_archetype_count: 0
new_fine_archetype_count: 1
new_trigger_family_count: 3
tested_existing_calibrated_axes:
- stage2_actionable_evidence_bonus
- price_only_blowoff_blocks_positive_stage
- full_4b_requires_non_price_evidence
- local_4b_watch_guard
- high_MAE_guardrail
residual_error_types_found:
- small finance value-up theme without ROE/capital-return bridge
- financial holdco winner needs 4B watch
- brokerage capital-return winner needs drawdown guard
new_axis_proposed: null
existing_axis_strengthened:
- stage2_required_bridge
- full_4b_requires_non_price_evidence
- local_4b_watch_guard
- high_MAE_watch_guard
existing_axis_weakened: null
existing_axis_kept:
- stage3_green_total_min
- stage3_green_revision_min
sector_specific_rule_candidate: false
canonical_archetype_rule_candidate: true
loop_contribution_label: canonical_archetype_rule_candidate
```

## 18. Validation Scope / Non-Validation Scope

Validated:

```text
- stock-web tradable_raw OHLC rows
- entry_date / entry_price
- MFE/MAE/peak/drawdown
- R6 direct L6 sector consistency
- large_sector/canonical consistency
- duplicate avoidance at symbol level
- representative rows use clean 180D windows
```

Not validated:

```text
- exact disclosure/report URLs
- exact capital-return announcement URLs
- production scoring behavior
- live candidate status
```

## 19. Shadow Weight Calibration

```csv
row_type,axis,scope,large_sector_id,canonical_archetype_id,baseline_value,tested_value,delta,reason,backtest_effect,trigger_ids,calibration_usable_count,new_independent_case_count,counterexample_count,confidence,proposal_type,notes
shadow_weight,c21_requires_roe_pbr_capital_return_earnings_bridge,canonical_archetype_specific,L6_FINANCIAL_CAPITAL_RETURN_DIGITAL,C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN,0,1,+1,"C21 financial ROE/PBR/capital-return rows should not promote toward Stage3-Yellow/Green unless financial value-up signal converts into ROE recovery, PBR discount repair, dividend/capital-return execution, shareholder-return policy, or earnings bridge","071050 and 016360 survive after ROE/PBR/capital-return bridge; 001510 is demoted because small-securities value-up theme lacks durable ROE and capital-return bridge","TRG_R6L75_C21_071050_20240129_FINANCIAL_HOLDCO_ROE_PBR_CAPITAL_RETURN_BRIDGE|TRG_R6L75_C21_016360_20240129_BROKERAGE_DIVIDEND_ROE_CAPITAL_RETURN_BRIDGE|TRG_R6L75_C21_001510_20240201_SMALL_SECURITIES_VALUEUP_THEME_NO_ROE_CAPITAL_RETURN_BRIDGE",3,3,1,medium,canonical_shadow_only,"not production; post-calibrated residual"
shadow_weight,c21_financial_valueup_4b_high_mae_watch_guard,canonical_archetype_specific,L6_FINANCIAL_CAPITAL_RETURN_DIGITAL,C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN,1,1,0,"Financial value-up winners and small-finance false starts can peak before ROE/capital-return durability is confirmed; local/full-window 4B and high-MAE watch should remain active","preserves 071050/016360 positives while preventing 001510 finance-theme false positive","TRG_R6L75_C21_071050_20240129_FINANCIAL_HOLDCO_ROE_PBR_CAPITAL_RETURN_BRIDGE|TRG_R6L75_C21_016360_20240129_BROKERAGE_DIVIDEND_ROE_CAPITAL_RETURN_BRIDGE|TRG_R6L75_C21_001510_20240201_SMALL_SECURITIES_VALUEUP_THEME_NO_ROE_CAPITAL_RETURN_BRIDGE",3,3,1,medium,existing_axis_kept,"strengthens local/full-window 4B and high-MAE watch without global delta"
```

## 20. Machine-Readable Rows

### 20.1 price_source_validation

```jsonl
{"row_type":"price_source_validation","source":"Songdaiki/stock-web","source_url":"https://github.com/Songdaiki/stock-web","manifest_path":"atlas/manifest.json","schema_path":"atlas/schema.json","universe_path":"atlas/universe/all_symbols.csv","manifest_max_date":"2026-02-20","source_name":"FinanceData/marcap","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","calibration_shard_root":"atlas/ohlcv_tradable_by_symbol_year","raw_shard_root":"atlas/ohlcv_raw_by_symbol_year","validation_status":"usable_for_historical_calibration"}
```

### 20.2 case rows

```jsonl
{"row_type":"case","case_id":"R6L75_C21_071050_20240129_FINANCIAL_HOLDCO_ROE_PBR_CAPITAL_RETURN_BRIDGE","symbol":"071050","company_name":"한국금융지주","round":"R6","loop":"75","large_sector_id":"L6_FINANCIAL_CAPITAL_RETURN_DIGITAL","canonical_archetype_id":"C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN","fine_archetype_id":"C21_FINANCIAL_HOLDCO_ROE_PBR_CAPITAL_RETURN_BRIDGE","deep_sub_archetype_id":"FINANCIAL_HOLDCO_BROKERAGE_ROE_RECOVERY_TO_PBR_REPAIR_AND_SHAREHOLDER_RETURN","case_type":"financial_holdco_success_then_4B_watch","positive_or_counterexample":"positive","best_trigger":"Stage2-Actionable","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"score_return_aligned","current_profile_verdict":"current_profile_correct_but_no_green","price_source":"Songdaiki/stock-web","notes":"C21 financial ROE/PBR/capital-return rows require ROE recovery, PBR discount repair, dividend/capital-return execution, shareholder-return policy, or earnings bridge; finance/value-up theme alone is insufficient."}
{"row_type":"case","case_id":"R6L75_C21_016360_20240129_BROKERAGE_DIVIDEND_ROE_CAPITAL_RETURN_BRIDGE","symbol":"016360","company_name":"삼성증권","round":"R6","loop":"75","large_sector_id":"L6_FINANCIAL_CAPITAL_RETURN_DIGITAL","canonical_archetype_id":"C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN","fine_archetype_id":"C21_BROKERAGE_DIVIDEND_ROE_CAPITAL_RETURN_BRIDGE","deep_sub_archetype_id":"BROKERAGE_TRADING_INCOME_AND_DIVIDEND_VISIBILITY_TO_ROE_PBR_REPAIR","case_type":"brokerage_capital_return_success_then_4B_watch","positive_or_counterexample":"positive","best_trigger":"Stage2-Actionable","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"score_return_aligned","current_profile_verdict":"current_profile_correct_with_drawdown_guard","price_source":"Songdaiki/stock-web","notes":"C21 financial ROE/PBR/capital-return rows require ROE recovery, PBR discount repair, dividend/capital-return execution, shareholder-return policy, or earnings bridge; finance/value-up theme alone is insufficient."}
{"row_type":"case","case_id":"R6L75_C21_001510_20240201_SMALL_SECURITIES_VALUEUP_THEME_NO_ROE_CAPITAL_RETURN_BRIDGE","symbol":"001510","company_name":"SK증권","round":"R6","loop":"75","large_sector_id":"L6_FINANCIAL_CAPITAL_RETURN_DIGITAL","canonical_archetype_id":"C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN","fine_archetype_id":"C21_SMALL_SECURITIES_VALUEUP_THEME_WITHOUT_ROE_CAPITAL_RETURN_BRIDGE","deep_sub_archetype_id":"SMALL_SECURITIES_PBR_THEME_WITHOUT_ROE_RECOVERY_DIVIDEND_OR_CAPITAL_RETURN_EXECUTION","case_type":"small_securities_theme_low_MFE_high_MAE_counterexample","positive_or_counterexample":"counterexample","best_trigger":"Stage2-Actionable","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"score_return_misaligned","current_profile_verdict":"current_profile_false_positive","price_source":"Songdaiki/stock-web","notes":"C21 financial ROE/PBR/capital-return rows require ROE recovery, PBR discount repair, dividend/capital-return execution, shareholder-return policy, or earnings bridge; finance/value-up theme alone is insufficient."}
```

### 20.3 trigger rows

```jsonl
{"row_type":"trigger","trigger_id":"TRG_R6L75_C21_071050_20240129_FINANCIAL_HOLDCO_ROE_PBR_CAPITAL_RETURN_BRIDGE","case_id":"R6L75_C21_071050_20240129_FINANCIAL_HOLDCO_ROE_PBR_CAPITAL_RETURN_BRIDGE","symbol":"071050","company_name":"한국금융지주","round":"R6","loop":"75","large_sector_id":"L6_FINANCIAL_CAPITAL_RETURN_DIGITAL","canonical_archetype_id":"C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN","fine_archetype_id":"C21_FINANCIAL_HOLDCO_ROE_PBR_CAPITAL_RETURN_BRIDGE","deep_sub_archetype_id":"FINANCIAL_HOLDCO_BROKERAGE_ROE_RECOVERY_TO_PBR_REPAIR_AND_SHAREHOLDER_RETURN","loop_objective":"coverage_gap_fill|counterexample_mining|stage2_actionable_bonus_stress_test|4B_non_price_requirement_stress_test|canonical_archetype_compression","trigger_type":"Stage2-Actionable","trigger_date":"2024-01-29","entry_date":"2024-01-29","entry_price":58700,"evidence_available_at_that_date":"source_proxy_financial_holdco_ROE_recovery_PBR_repair_capital_return_bridge; evidence_url_pending","evidence_source":"source_proxy_financial_holdco_ROE_recovery_PBR_repair_capital_return_bridge; evidence_url_pending","bridge_summary":"financial-holdco and brokerage ROE recovery converted into PBR repair and shareholder-return visibility rather than value-up theme only","stage2_evidence_fields":["financial_valueup","ROE_recovery_proxy","PBR_discount_repair","relative_strength"],"stage3_evidence_fields":["brokerage_ROE_to_PBR_visibility","capital_return_policy_proxy","earnings_revision_proxy"],"stage4b_evidence_fields":["post_MFE_peak_watch","financial_valueup_crowding_after_rerating"],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/071/071050/2024.csv","profile_path":"atlas/symbol_profiles/071/071050.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":28.11,"MFE_90D_pct":28.11,"MFE_180D_pct":32.37,"MFE_1Y_pct":32.37,"MFE_2Y_pct":32.37,"MAE_30D_pct":-2.21,"MAE_90D_pct":-2.21,"MAE_180D_pct":-2.21,"MAE_1Y_pct":-2.21,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-07-17","peak_price":77700,"drawdown_after_peak_pct":-19.05,"green_lateness_ratio":"0.41","four_b_local_peak_proximity":0.92,"four_b_full_window_peak_proximity":1.0,"four_b_timing_verdict":"financial_holdco_ROE_PBR_bridge_positive_but_4B_watch","four_b_evidence_type":"non_price_ROE_PBR_capital_return_bridge","four_c_protection_label":"none","trigger_outcome_label":"structural_success_then_4B_watch","current_profile_verdict":"current_profile_correct_but_no_green","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"R6L75_C21_071050_20240129_FINANCIAL_HOLDCO_ROE_PBR_CAPITAL_RETURN_BRIDGE_entry","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"TRG_R6L75_C21_016360_20240129_BROKERAGE_DIVIDEND_ROE_CAPITAL_RETURN_BRIDGE","case_id":"R6L75_C21_016360_20240129_BROKERAGE_DIVIDEND_ROE_CAPITAL_RETURN_BRIDGE","symbol":"016360","company_name":"삼성증권","round":"R6","loop":"75","large_sector_id":"L6_FINANCIAL_CAPITAL_RETURN_DIGITAL","canonical_archetype_id":"C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN","fine_archetype_id":"C21_BROKERAGE_DIVIDEND_ROE_CAPITAL_RETURN_BRIDGE","deep_sub_archetype_id":"BROKERAGE_TRADING_INCOME_AND_DIVIDEND_VISIBILITY_TO_ROE_PBR_REPAIR","loop_objective":"coverage_gap_fill|counterexample_mining|stage2_actionable_bonus_stress_test|4B_non_price_requirement_stress_test|canonical_archetype_compression","trigger_type":"Stage2-Actionable","trigger_date":"2024-01-29","entry_date":"2024-01-29","entry_price":36950,"evidence_available_at_that_date":"source_proxy_brokerage_dividend_ROE_PBR_repair_capital_return_bridge; evidence_url_pending","evidence_source":"source_proxy_brokerage_dividend_ROE_PBR_repair_capital_return_bridge; evidence_url_pending","bridge_summary":"brokerage value-up and dividend/ROE visibility converted into capital-return and PBR repair bridge, but post-peak drawdown required 4B watch","stage2_evidence_fields":["brokerage_valueup","dividend_visibility","ROE_recovery_proxy","relative_strength"],"stage3_evidence_fields":["capital_return_to_PBR_repair","trading_income_or_fee_ROE_proxy","shareholder_return_execution_proxy"],"stage4b_evidence_fields":["post_MFE_peak_watch","brokerage_valueup_crowding"],"stage4c_evidence_fields":["post_peak_drawdown_watch"],"price_data_source":"Songdaiki/stock-web","price_data_repo":"Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/016/016360/2024.csv","profile_path":"atlas/symbol_profiles/016/016360.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":15.7,"MFE_90D_pct":15.7,"MFE_180D_pct":32.34,"MFE_1Y_pct":32.34,"MFE_2Y_pct":32.34,"MAE_30D_pct":-2.03,"MAE_90D_pct":-2.03,"MAE_180D_pct":-2.03,"MAE_1Y_pct":-2.03,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-08-26","peak_price":48900,"drawdown_after_peak_pct":-19.22,"green_lateness_ratio":"0.48","four_b_local_peak_proximity":0.88,"four_b_full_window_peak_proximity":1.0,"four_b_timing_verdict":"brokerage_ROE_capital_return_positive_but_full_window_4B_watch","four_b_evidence_type":"non_price_ROE_PBR_capital_return_bridge","four_c_protection_label":"drawdown_watch_after_peak","trigger_outcome_label":"structural_success_then_4B_watch","current_profile_verdict":"current_profile_correct_with_drawdown_guard","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"R6L75_C21_016360_20240129_BROKERAGE_DIVIDEND_ROE_CAPITAL_RETURN_BRIDGE_entry","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"TRG_R6L75_C21_001510_20240201_SMALL_SECURITIES_VALUEUP_THEME_NO_ROE_CAPITAL_RETURN_BRIDGE","case_id":"R6L75_C21_001510_20240201_SMALL_SECURITIES_VALUEUP_THEME_NO_ROE_CAPITAL_RETURN_BRIDGE","symbol":"001510","company_name":"SK증권","round":"R6","loop":"75","large_sector_id":"L6_FINANCIAL_CAPITAL_RETURN_DIGITAL","canonical_archetype_id":"C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN","fine_archetype_id":"C21_SMALL_SECURITIES_VALUEUP_THEME_WITHOUT_ROE_CAPITAL_RETURN_BRIDGE","deep_sub_archetype_id":"SMALL_SECURITIES_PBR_THEME_WITHOUT_ROE_RECOVERY_DIVIDEND_OR_CAPITAL_RETURN_EXECUTION","loop_objective":"coverage_gap_fill|counterexample_mining|stage2_actionable_bonus_stress_test|4B_non_price_requirement_stress_test|canonical_archetype_compression","trigger_type":"Stage2-Actionable","trigger_date":"2024-02-01","entry_date":"2024-02-01","entry_price":647,"evidence_available_at_that_date":"source_proxy_small_securities_valueup_theme_without_ROE_recovery_dividend_or_capital_return_bridge; evidence_url_pending","evidence_source":"source_proxy_small_securities_valueup_theme_without_ROE_recovery_dividend_or_capital_return_bridge; evidence_url_pending","bridge_summary":"small-securities value-up/PBR theme did not convert into durable ROE recovery, dividend visibility, capital-return execution, or earnings bridge","stage2_evidence_fields":["small_securities_valueup_theme","PBR_discount_optionality","price_rebound","relative_strength"],"stage3_evidence_fields":[],"stage4b_evidence_fields":["weak_local_peak","ROE_bridge_absent","capital_return_execution_absent"],"stage4c_evidence_fields":["high_MAE_without_ROE_or_capital_return_bridge"],"price_data_source":"Songdaiki/stock-web","price_data_repo":"Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/001/001510/2024.csv","profile_path":"atlas/symbol_profiles/001/001510.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":3.4,"MFE_90D_pct":3.4,"MFE_180D_pct":3.4,"MFE_1Y_pct":3.4,"MFE_2Y_pct":3.4,"MAE_30D_pct":-2.78,"MAE_90D_pct":-9.27,"MAE_180D_pct":-23.34,"MAE_1Y_pct":-23.34,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-02-19","peak_price":669,"drawdown_after_peak_pct":-25.86,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":1.0,"four_b_full_window_peak_proximity":1.0,"four_b_timing_verdict":"small_securities_theme_local_4B_watch_not_positive_stage","four_b_evidence_type":"financial_valueup_theme_without_ROE_capital_return_bridge","four_c_protection_label":"high_MAE_watch","trigger_outcome_label":"failed_small_securities_valueup_counterexample","current_profile_verdict":"current_profile_false_positive","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"R6L75_C21_001510_20240201_SMALL_SECURITIES_VALUEUP_THEME_NO_ROE_CAPITAL_RETURN_BRIDGE_entry","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
```

### 20.4 score_simulation rows

```jsonl
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"R6L75_C21_071050_20240129_FINANCIAL_HOLDCO_ROE_PBR_CAPITAL_RETURN_BRIDGE","trigger_id":"TRG_R6L75_C21_071050_20240129_FINANCIAL_HOLDCO_ROE_PBR_CAPITAL_RETURN_BRIDGE","symbol":"071050","large_sector_id":"L6_FINANCIAL_CAPITAL_RETURN_DIGITAL","canonical_archetype_id":"C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN","raw_component_scores_before":{"ROE_recovery_score":12,"PBR_repair_score":12,"capital_return_score":11,"earnings_bridge_score":10,"relative_strength_score":10,"theme_risk_penalty":6},"weighted_score_before":74,"stage_label_before":"Stage2-Actionable","raw_component_scores_after":{"ROE_recovery_score":15,"PBR_repair_score":15,"capital_return_score":14,"earnings_bridge_score":13,"relative_strength_score":8,"theme_risk_penalty":8},"weighted_score_after":83,"stage_label_after":"Stage3-Yellow","changed_components":["ROE_recovery_score","PBR_repair_score","capital_return_score","earnings_bridge_score","relative_strength_score","theme_risk_penalty"],"component_delta_explanation":"C21 row is promoted only because financial value-up converts into ROE recovery, PBR repair, capital-return and earnings bridge; 4B drawdown/crowding watch blocks Green.","MFE_90D_pct":28.11,"MAE_90D_pct":-2.21,"score_return_alignment_label":"score_return_aligned","current_profile_verdict":"current_profile_correct_but_no_green"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"R6L75_C21_016360_20240129_BROKERAGE_DIVIDEND_ROE_CAPITAL_RETURN_BRIDGE","trigger_id":"TRG_R6L75_C21_016360_20240129_BROKERAGE_DIVIDEND_ROE_CAPITAL_RETURN_BRIDGE","symbol":"016360","large_sector_id":"L6_FINANCIAL_CAPITAL_RETURN_DIGITAL","canonical_archetype_id":"C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN","raw_component_scores_before":{"ROE_recovery_score":12,"PBR_repair_score":12,"capital_return_score":11,"earnings_bridge_score":10,"relative_strength_score":10,"theme_risk_penalty":6},"weighted_score_before":74,"stage_label_before":"Stage2-Actionable","raw_component_scores_after":{"ROE_recovery_score":15,"PBR_repair_score":15,"capital_return_score":14,"earnings_bridge_score":13,"relative_strength_score":8,"theme_risk_penalty":8},"weighted_score_after":83,"stage_label_after":"Stage3-Yellow","changed_components":["ROE_recovery_score","PBR_repair_score","capital_return_score","earnings_bridge_score","relative_strength_score","theme_risk_penalty"],"component_delta_explanation":"C21 row is promoted only because financial value-up converts into ROE recovery, PBR repair, capital-return and earnings bridge; 4B drawdown/crowding watch blocks Green.","MFE_90D_pct":15.7,"MAE_90D_pct":-2.03,"score_return_alignment_label":"score_return_aligned","current_profile_verdict":"current_profile_correct_with_drawdown_guard"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"R6L75_C21_001510_20240201_SMALL_SECURITIES_VALUEUP_THEME_NO_ROE_CAPITAL_RETURN_BRIDGE","trigger_id":"TRG_R6L75_C21_001510_20240201_SMALL_SECURITIES_VALUEUP_THEME_NO_ROE_CAPITAL_RETURN_BRIDGE","symbol":"001510","large_sector_id":"L6_FINANCIAL_CAPITAL_RETURN_DIGITAL","canonical_archetype_id":"C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN","raw_component_scores_before":{"ROE_recovery_score":1,"PBR_repair_score":4,"capital_return_score":1,"earnings_bridge_score":0,"relative_strength_score":10,"theme_risk_penalty":9},"weighted_score_before":61,"stage_label_before":"Stage2-Actionable","raw_component_scores_after":{"ROE_recovery_score":0,"PBR_repair_score":1,"capital_return_score":0,"earnings_bridge_score":0,"relative_strength_score":4,"theme_risk_penalty":16},"weighted_score_after":39,"stage_label_after":"Stage1-Watch_or_4B-HighMAE","changed_components":["ROE_recovery_score","PBR_repair_score","capital_return_score","earnings_bridge_score","relative_strength_score","theme_risk_penalty"],"component_delta_explanation":"C21 guard demotes small finance/value-up theme rows when ROE recovery, dividend/capital-return execution, PBR repair and earnings bridge are absent.","MFE_90D_pct":3.4,"MAE_90D_pct":-9.27,"score_return_alignment_label":"score_return_misaligned","current_profile_verdict":"current_profile_false_positive"}
```

### 20.5 shadow_weight rows

```csv
row_type,axis,scope,large_sector_id,canonical_archetype_id,baseline_value,tested_value,delta,reason,backtest_effect,trigger_ids,calibration_usable_count,new_independent_case_count,counterexample_count,confidence,proposal_type,notes
shadow_weight,c21_requires_roe_pbr_capital_return_earnings_bridge,canonical_archetype_specific,L6_FINANCIAL_CAPITAL_RETURN_DIGITAL,C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN,0,1,+1,"C21 financial ROE/PBR/capital-return rows should not promote toward Stage3-Yellow/Green unless financial value-up signal converts into ROE recovery, PBR discount repair, dividend/capital-return execution, shareholder-return policy, or earnings bridge","071050 and 016360 survive after ROE/PBR/capital-return bridge; 001510 is demoted because small-securities value-up theme lacks durable ROE and capital-return bridge","TRG_R6L75_C21_071050_20240129_FINANCIAL_HOLDCO_ROE_PBR_CAPITAL_RETURN_BRIDGE|TRG_R6L75_C21_016360_20240129_BROKERAGE_DIVIDEND_ROE_CAPITAL_RETURN_BRIDGE|TRG_R6L75_C21_001510_20240201_SMALL_SECURITIES_VALUEUP_THEME_NO_ROE_CAPITAL_RETURN_BRIDGE",3,3,1,medium,canonical_shadow_only,"not production; post-calibrated residual"
shadow_weight,c21_financial_valueup_4b_high_mae_watch_guard,canonical_archetype_specific,L6_FINANCIAL_CAPITAL_RETURN_DIGITAL,C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN,1,1,0,"Financial value-up winners and small-finance false starts can peak before ROE/capital-return durability is confirmed; local/full-window 4B and high-MAE watch should remain active","preserves 071050/016360 positives while preventing 001510 finance-theme false positive","TRG_R6L75_C21_071050_20240129_FINANCIAL_HOLDCO_ROE_PBR_CAPITAL_RETURN_BRIDGE|TRG_R6L75_C21_016360_20240129_BROKERAGE_DIVIDEND_ROE_CAPITAL_RETURN_BRIDGE|TRG_R6L75_C21_001510_20240201_SMALL_SECURITIES_VALUEUP_THEME_NO_ROE_CAPITAL_RETURN_BRIDGE",3,3,1,medium,existing_axis_kept,"strengthens local/full-window 4B and high-MAE watch without global delta"
```

### 20.6 residual_contribution row

```jsonl
{"row_type":"residual_contribution","round":"R6","loop":"75","large_sector_id":"L6_FINANCIAL_CAPITAL_RETURN_DIGITAL","canonical_archetype_id":"C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN","new_independent_case_count":3,"reused_case_count":0,"new_symbol_count":3,"new_trigger_family_count":3,"tested_existing_calibrated_axes":["stage2_actionable_evidence_bonus","price_only_blowoff_blocks_positive_stage","full_4b_requires_non_price_evidence","local_4b_watch_guard","high_MAE_guardrail"],"residual_error_types_found":["small_finance_valueup_theme_without_ROE_capital_return_bridge","financial_holdco_winner_needs_4B_watch","brokerage_capital_return_winner_needs_drawdown_guard"],"loop_contribution_label":"canonical_archetype_rule_candidate","do_not_propose_new_weight_delta":false}
```

## 21. Deferred Coding Agent Handoff Prompt

### Purpose

You are now in the repository implementation phase. The attached Markdown files are v12 post-calibrated residual research outputs produced using the Songdaiki/stock-web OHLC atlas.

These MDs are not live candidate research. They are historical calibration research designed to extend the already-applied e2r_2_1_stock_web_calibrated profile.

Do not blindly apply every shadow row. Ingest the machine-readable rows and update the sector/canonical-archetype calibration ledger.

### R6-specific handling

- R6 maps to `L6_FINANCIAL_CAPITAL_RETURN_DIGITAL`.
- This MD uses `C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN`.
- Validate `round_schedule_status=valid` and `round_sector_consistency=pass` before accepting rows.

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
- price-only/financial-valueup-theme-only rows cannot promote Stage2/Stage3.
- If a v12 MD weakens an already applied axis, log it as residual counterexample rather than immediately reverting.
- Production scoring must not change unless the user explicitly asks for another promotion batch.

### Expected repository tasks

1. Parse case / trigger / score_simulation / shadow_weight / residual_contribution rows.
2. Validate stock-web price source fields.
3. Validate R6 direct L6 sector.
4. Validate canonical_archetype_id.
5. Validate novelty and reuse fields.
6. Deduplicate same_entry_group_id and reused cases.
7. Aggregate by large_sector_id and canonical_archetype_id.
8. Update sector_shadow_profile and archetype_shadow_profile only.
9. Preserve global calibrated profile unless explicitly promoted.
10. Report new independent cases, counterexamples, and residual error types.
11. Add tests that duplicate low-value loops cannot change weights.
12. Add validation that C21 financial ROE/PBR/capital-return rows cannot promote without ROE recovery, PBR discount repair, dividend visibility, capital-return execution, shareholder-return policy, earnings revision, solvency/balance quality, or fee/trading-income durability.

### Expected output

- Concise implementation summary.
- Rows accepted/rejected.
- New sector/canonical archetype coverage.
- Existing axis strengthened/weakened/kept.
- No investment recommendation language.

## 22. Next Round State

```text
completed_round = R6
completed_loop = 75
next_round = R7
next_loop = 75
round_schedule_status = valid
round_sector_consistency = pass
```

## 23. Source Notes

```text
MAIN EXECUTION PROMPT:
docs/core/e2r_v12_prompt_round_scheduler_corrected.txt

NO-REPEAT INDEX:
docs/core/V12_Research_No_Repeat_Index.md

Stock-web:
atlas/manifest.json
atlas/schema.json
atlas/symbol_profiles/071/071050.json
atlas/symbol_profiles/016/016360.json
atlas/symbol_profiles/001/001510.json
atlas/ohlcv_tradable_by_symbol_year/071/071050/2024.csv
atlas/ohlcv_tradable_by_symbol_year/016/016360/2024.csv
atlas/ohlcv_tradable_by_symbol_year/001/001510/2024.csv
```

This loop continues loop 75 with R6 and adds 3 new independent C21 representative cases, 2 positives, 1 counterexample/watch case, and 1 canonical-archetype residual guard candidate for R6/L6.
