# E2R Stock-Web Historical Calibration / Sector-Archetype Residual Research Round

## 0. Research Metadata

```text
scheduled_round: R6
scheduled_loop: 76
round_schedule_status: valid
round_sector_consistency: pass
computed_next_round: R7
computed_next_loop: 76
large_sector_id: L6_FINANCIAL_CAPITAL_RETURN_DIGITAL
canonical_archetype_id: C22_INSURANCE_RATE_CYCLE_RESERVE
fine_archetype_id: C22_RATE_RESERVE_ROE_CAPITAL_RETURN_BRIDGE_GUARD
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

R6 maps directly to `L6_FINANCIAL_CAPITAL_RETURN_DIGITAL`. The previous R6 loop used C21 financial ROE/PBR/capital-return, so this run rotates to C22 insurance rate-cycle/reserve. It avoids the top-covered life/non-life insurer cluster and tests a fresh split: insurance value-up survives only when reserve, ROE, capital buffer and capital-return bridge are visible; small insurance M&A theme MFE alone is demoted.

| layer | id | definition |
|---|---|---|
| round | R6 | financial / capital return / digital |
| large_sector | L6_FINANCIAL_CAPITAL_RETURN_DIGITAL | insurance, financial holding, capital return, reserve/capital buffer |
| canonical | C22_INSURANCE_RATE_CYCLE_RESERVE | insurance rate-cycle, reserve, solvency, ROE and capital return |
| fine | C22_RATE_RESERVE_ROE_CAPITAL_RETURN_BRIDGE_GUARD | insurance signal must become rate/reserve/ROE/capital-return evidence |
| deep | INSURANCE_FINANCIAL_HOLDCO_CAPITAL_RETURN_ROE_RESERVE_BUFFER_TO_PBR_RERATING | insurance holdco positive |
| deep | REINSURANCE_HARD_MARKET_RATE_CYCLE_AND_RESERVE_BUFFER_TO_ROE_CAPITAL_RETURN | reinsurance positive |
| deep | SMALL_NONLIFE_INSURANCE_SALE_OR_MNA_OPTIONALITY_WITHOUT_RESERVE_BUFFER_ROE_CAPITAL_RETURN_CONVERSION | small non-life false positive |

## 3. No-Repeat / Coverage Check

No-Repeat hard duplicate key:

```text
canonical_archetype_id + symbol + trigger_type + entry_date
```

C22 top-covered symbols are `000810`, `005830`, `088350`, `001450`, `032830`, and `085620`. This run avoids that cluster and also avoids the previous R6/C21 representatives `071050`, `016360`, and `001510`.

| archetype | selected symbol | duplicate status | reason |
|---|---:|---|---|
| C22 | 138040 | new independent | not top-covered C22 symbol; insurance-linked holdco capital-return/reserve buffer bridge |
| C22 | 003690 | new independent | not top-covered C22 symbol; reinsurance rate-cycle/reserve bridge |
| C22 | 000400 | new independent | not top-covered C22 symbol; small non-life M&A theme without reserve/ROE/capital-return bridge |

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
MFE/MAE/peak/drawdown computed = true
price_basis = tradable_raw
price_adjustment_status = raw_unadjusted_marcap
corporate_action_window_status = clean_180D_window
```

Corporate-action caveat:

```text
138040 has corporate-action candidates ending 2023-04-25, outside the selected 2024 representative window.
003690 has corporate-action candidates ending 2004-07-20, outside the selected 2024 representative window.
000400 has corporate-action candidates ending 2019-10-25, outside the selected 2024 representative window.
All three representative windows are treated as clean for this residual calibration.
```

## 6. Case Selection Summary

| role | symbol | company | trigger | entry | price | result |
|---|---:|---|---|---:|---:|---|
| insurance_holdco_capital_return_success_then_4B_watch | 138040 | 메리츠금융지주 | Stage2-Actionable | 2024-01-29 | 64300 | insurance-linked holdco ROE/capital-return/reserve-buffer bridge worked |
| reinsurance_rate_reserve_success_then_4B_watch | 003690 | 코리안리 | Stage2-Actionable | 2024-01-29 | 7400 | reinsurance rate-cycle/underwriting/reserve bridge worked |
| small_nonlife_MNA_theme_MFE_then_high_MAE_counterexample | 000400 | 롯데손해보험 | Stage2-Actionable | 2024-02-13 | 3370 | small non-life M&A theme MFE lacked reserve/ROE/capital-return bridge |

## 7. Positive vs Counterexample Balance

```text
positive_case_count: 2
counterexample_count: 1
4B_case_count: 3
4C_or_high_MAE_watch_count: 3
calibration_usable_case_count: 3
current_profile_error_count: 1
```

## 8. Trigger-Level OHLC Backtest Table

| symbol | company | trigger | entry_date | entry_price | MFE30 | MFE90 | MFE180 | MAE30 | MAE90 | MAE180 | peak_date | peak_price | DD after peak |
|---:|---|---|---|---:|---:|---:|---:|---:|---:|---:|---|---:|---:|
| 138040 | 메리츠금융지주 | Stage2-Actionable | 2024-01-29 | 64300 | 37.33 | 37.33 | 55.37 | -1.87 | -1.87 | -1.87 | 2024-10-07 | 99900 | -3.2 |
| 003690 | 코리안리 | Stage2-Actionable | 2024-01-29 | 7400 | 13.78 | 15.54 | 25.27 | -2.97 | -2.97 | -2.97 | 2024-10-24 | 9270 | -14.89 |
| 000400 | 롯데손해보험 | Stage2-Actionable | 2024-02-13 | 3370 | 8.9 | 8.9 | 21.36 | -19.88 | -19.88 | -35.46 | 2024-06-26 | 4090 | -46.82 |

## 9. Case-by-Case Notes

### 9.1 138040 / 메리츠금융지주 — insurance holdco capital-return bridge

The entry row is 2024-01-29 at 64,300. The forward path reached 88,300 in the early rerating zone and later reached 99,900. This is a valid C22 positive because the signal is not just low-PBR financial value-up. It is capital-return execution, ROE visibility, reserve/capital-buffer confidence and PBR repair. Full-window 4B remains active because reserve/capital sensitivity can still cap Green.

### 9.2 003690 / 코리안리 — reinsurance rate-cycle reserve bridge

The entry row is 2024-01-29 at 7,400. The path reached 8,420 in the early window and 9,270 around the broader window. This is a C22 positive because reinsurance rate-cycle and underwriting-margin visibility create a reserve-buffer and capital-return bridge. It still routes to guarded Yellow, not Green loosening.

### 9.3 000400 / 롯데손해보험 — small non-life M&A theme without reserve/ROE bridge

The entry row is 2024-02-13 at 3,370. The local path reached 3,670 and later 4,090, but the low fell to 2,175. This is the C22 trap: sale/M&A optionality can produce MFE, but without reserve-buffer confidence, solvency, ROE recovery and capital-return execution, it should be Watch/4B/high-MAE rather than Stage3 evidence.

## 10. Current Calibrated Profile Stress Test

| question | result |
|---|---|
| Stage2 actionable bonus too strong? | Yes when C22 treats insurance M&A/value-up theme as enough evidence. |
| Stage3 Yellow threshold too loose? | Not globally; C22 needs rate/reserve/ROE/capital-return bridge before Yellow. |
| Stage3 Green too strict? | Correct. This round reinforces strict Green. |
| Price-only blowoff guard appropriate? | Yes, especially for 000400 and post-peak insurer value-up crowding. |
| Full 4B non-price requirement appropriate? | Yes. 138040/003690 have stronger non-price bridges; 000400 does not. |
| 4C timing issue? | High-MAE watch is useful; no immediate hard 4C production delta proposed. |

## 11. Stage2 / Yellow / Green Comparison

```text
138040:
  Stage2-Actionable = correct
  Stage3-Yellow = allowed after ROE / reserve buffer / capital-return bridge
  Stage3-Green = reject unless capital sensitivity and post-MFE durability clear

003690:
  Stage2-Actionable = correct
  Stage3-Yellow = allowed after rate-cycle / underwriting-margin / reserve bridge
  Stage3-Green = reject because reserve/capital-return durability still needs 4B watch

000400:
  Stage2-Actionable = acceptable only as insurance sale/M&A watch
  Stage3-Yellow = reject without reserve buffer, ROE, solvency and capital-return bridge
  Stage3-Green = reject despite MFE
```

## 12. 4B Local vs Full-window Timing Audit

| symbol | local_peak_proximity | full_window_peak_proximity | verdict |
|---:|---:|---:|---|
| 138040 | 0.88 | 1.00 | insurance holdco capital-return bridge positive but full-window 4B watch |
| 003690 | 0.91 | 1.00 | reinsurance rate/reserve bridge positive but 4B drawdown watch |
| 000400 | 0.90 | 1.00 | small non-life M&A MFE but no reserve/ROE bridge; keep 4B/high-MAE watch |

## 13. Canonical-Archetype Rule Candidate

```text
canonical_archetype_rule_candidate: true
rule_scope: canonical_archetype_specific
rule_id: c22_requires_rate_reserve_roe_capital_return_bridge

rule:
  For C22 insurance/rate-cycle rows, do not promote life insurance,
  non-life insurance, reinsurance, insurance holding, low-PBR insurer,
  M&A/sale, or insurance value-up Stage2 signals into Stage3-Yellow/Green
  unless at least one non-price bridge is visible:
  rate-cycle improvement, underwriting-margin improvement, reserve/capital buffer,
  solvency confidence, ROE recovery, capital-return execution, dividend visibility,
  earnings revision, or PBR discount repair tied to insurance economics.
```

## 14. Before / After Backtest Comparison

| profile | eligible triggers | avg MFE90 | avg MAE90 | false positive rate | verdict |
|---|---:|---:|---:|---:|---|
| P0 e2r_2_1_stock_web_calibrated_proxy | 3 | 20.59 | -8.24 | 33.3% | useful but can over-credit insurance M&A/theme MFE |
| P0b e2r_2_0_baseline_reference | 3 | 20.59 | -8.24 | 0% | safer but may miss 138040/003690 |
| P1 sector_specific_candidate_profile | 3 | 20.59 | -8.24 | 33.3% | no broad L6 loosen |
| P2 canonical_archetype_candidate_profile | 2 selected positives | 26.43 | -2.42 | 0% after bridge gate | preferred shadow |
| P3 counterexample_guard_profile | 1 rejected/watch | 8.9 | -19.88 | 0% after no-Green routing | useful guard |

## 15. Score-Return Alignment Matrix

| case | current profile verdict | alignment |
|---|---|---|
| 138040 | current_profile_correct_but_no_green | capital-return/reserve bridge aligned with MFE but 4B watch remains |
| 003690 | current_profile_correct_with_drawdown_guard | reinsurance rate/reserve bridge aligned with MFE but drawdown guard remains |
| 000400 | current_profile_false_positive_if_green | M&A MFE lacked reserve/ROE/capital-return bridge |

## 16. Coverage Matrix

| large_sector_id | canonical_archetype_id | fine_archetype_id | positive | counterexample | 4B | 4C/watch | new_independent | reused | usable_triggers | representative | profile_errors | sector_rule | canonical_rule | coverage_gap_after |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|---|---|
| L6_FINANCIAL_CAPITAL_RETURN_DIGITAL | C22_INSURANCE_RATE_CYCLE_RESERVE | C22_RATE_RESERVE_ROE_CAPITAL_RETURN_BRIDGE_GUARD | 2 | 1 | 3 | 3 | 3 | 0 | 3 | 3 | 1 | false | true | R6/C22 non-top-covered insurance reserve/capital-return residual reduced |

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
- insurance M&A theme without reserve/ROE bridge
- insurance holdco capital-return winner needs 4B watch
- reinsurance rate/reserve winner needs drawdown guard
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
- representative rows use clean windows outside listed corporate-action candidate dates
```

Not validated:

```text
- exact disclosure/report URLs
- exact reserve/capital-return/M&A announcement URLs
- production scoring behavior
- live candidate status
- additional insurer alternatives such as 000370/082640/000540 because previous R6/C22 work already used them
```

## 19. Shadow Weight Calibration

```csv
row_type,axis,scope,large_sector_id,canonical_archetype_id,baseline_value,tested_value,delta,reason,backtest_effect,trigger_ids,calibration_usable_count,new_independent_case_count,counterexample_count,confidence,proposal_type,notes
shadow_weight,c22_requires_rate_reserve_roe_capital_return_bridge,canonical_archetype_specific,L6_FINANCIAL_CAPITAL_RETURN_DIGITAL,C22_INSURANCE_RATE_CYCLE_RESERVE,0,1,+1,"C22 insurance/rate-cycle rows should not promote toward Stage3-Yellow/Green unless insurance signal converts into rate-cycle, underwriting margin, reserve/capital buffer, solvency, ROE, capital-return, or earnings bridge","138040 and 003690 survive as guarded positives after capital-return/reserve/rate-cycle bridge; 000400 is demoted because small non-life M&A theme lacked durable reserve, solvency, ROE and capital-return bridge","TRG_R6L76_C22_138040_20240129_INSURANCE_HOLDCO_CAPITAL_RETURN_RESERVE_BUFFER_BRIDGE|TRG_R6L76_C22_003690_20240129_REINSURANCE_UNDERWRITING_RATE_RESERVE_BRIDGE|TRG_R6L76_C22_000400_20240213_SMALL_NONLIFE_MNA_THEME_NO_RESERVE_ROE_BRIDGE",3,3,1,medium,canonical_shadow_only,"not production; post-calibrated residual"
shadow_weight,c22_insurance_theme_4b_high_mae_watch_guard,canonical_archetype_specific,L6_FINANCIAL_CAPITAL_RETURN_DIGITAL,C22_INSURANCE_RATE_CYCLE_RESERVE,1,1,0,"Insurance winners and M&A/theme false starts can peak before reserve/ROE/capital-return durability is confirmed; local/full-window 4B and high-MAE watch should remain active","preserves 138040/003690 guarded positives while preventing 000400 insurance-theme false positive","TRG_R6L76_C22_138040_20240129_INSURANCE_HOLDCO_CAPITAL_RETURN_RESERVE_BUFFER_BRIDGE|TRG_R6L76_C22_003690_20240129_REINSURANCE_UNDERWRITING_RATE_RESERVE_BRIDGE|TRG_R6L76_C22_000400_20240213_SMALL_NONLIFE_MNA_THEME_NO_RESERVE_ROE_BRIDGE",3,3,1,medium,existing_axis_kept,"strengthens local/full-window 4B and high-MAE watch without global delta"
```

## 20. Machine-Readable Rows

### 20.1 price_source_validation

```jsonl
{"row_type":"price_source_validation","source":"Songdaiki/stock-web","source_url":"https://github.com/Songdaiki/stock-web","manifest_path":"atlas/manifest.json","schema_path":"atlas/schema.json","universe_path":"atlas/universe/all_symbols.csv","manifest_max_date":"2026-02-20","source_name":"FinanceData/marcap","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","calibration_shard_root":"atlas/ohlcv_tradable_by_symbol_year","raw_shard_root":"atlas/ohlcv_raw_by_symbol_year","validation_status":"usable_for_historical_calibration"}
```

### 20.2 case rows

```jsonl
{"row_type":"case","case_id":"R6L76_C22_138040_20240129_INSURANCE_HOLDCO_CAPITAL_RETURN_RESERVE_BUFFER_BRIDGE","symbol":"138040","company_name":"메리츠금융지주","round":"R6","loop":"76","large_sector_id":"L6_FINANCIAL_CAPITAL_RETURN_DIGITAL","canonical_archetype_id":"C22_INSURANCE_RATE_CYCLE_RESERVE","fine_archetype_id":"C22_INSURANCE_HOLDCO_CAPITAL_RETURN_RESERVE_BUFFER_BRIDGE","deep_sub_archetype_id":"INSURANCE_FINANCIAL_HOLDCO_CAPITAL_RETURN_ROE_RESERVE_BUFFER_TO_PBR_RERATING","case_type":"insurance_holdco_capital_return_success_then_4B_watch","positive_or_counterexample":"positive","best_trigger":"Stage2-Actionable","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"score_return_aligned","current_profile_verdict":"current_profile_correct_but_no_green","price_source":"Songdaiki/stock-web","notes":"C22 insurance rows require rate-cycle, underwriting margin, reserve/capital buffer, solvency, ROE, capital-return or earnings bridge; insurance/M&A/value-up theme MFE alone is insufficient."}
{"row_type":"case","case_id":"R6L76_C22_003690_20240129_REINSURANCE_UNDERWRITING_RATE_RESERVE_BRIDGE","symbol":"003690","company_name":"코리안리","round":"R6","loop":"76","large_sector_id":"L6_FINANCIAL_CAPITAL_RETURN_DIGITAL","canonical_archetype_id":"C22_INSURANCE_RATE_CYCLE_RESERVE","fine_archetype_id":"C22_REINSURANCE_UNDERWRITING_RATE_RESERVE_BRIDGE","deep_sub_archetype_id":"REINSURANCE_HARD_MARKET_RATE_CYCLE_AND_RESERVE_BUFFER_TO_ROE_CAPITAL_RETURN","case_type":"reinsurance_rate_reserve_success_then_4B_watch","positive_or_counterexample":"positive","best_trigger":"Stage2-Actionable","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"score_return_aligned","current_profile_verdict":"current_profile_correct_with_drawdown_guard","price_source":"Songdaiki/stock-web","notes":"C22 insurance rows require rate-cycle, underwriting margin, reserve/capital buffer, solvency, ROE, capital-return or earnings bridge; insurance/M&A/value-up theme MFE alone is insufficient."}
{"row_type":"case","case_id":"R6L76_C22_000400_20240213_SMALL_NONLIFE_MNA_THEME_NO_RESERVE_ROE_BRIDGE","symbol":"000400","company_name":"롯데손해보험","round":"R6","loop":"76","large_sector_id":"L6_FINANCIAL_CAPITAL_RETURN_DIGITAL","canonical_archetype_id":"C22_INSURANCE_RATE_CYCLE_RESERVE","fine_archetype_id":"C22_SMALL_NONLIFE_MNA_THEME_WITHOUT_RESERVE_ROE_BRIDGE","deep_sub_archetype_id":"SMALL_NONLIFE_INSURANCE_SALE_OR_MNA_OPTIONALITY_WITHOUT_RESERVE_BUFFER_ROE_CAPITAL_RETURN_CONVERSION","case_type":"small_nonlife_MNA_theme_MFE_then_high_MAE_counterexample","positive_or_counterexample":"counterexample","best_trigger":"Stage2-Actionable","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"score_return_mixed","current_profile_verdict":"current_profile_false_positive_if_green","price_source":"Songdaiki/stock-web","notes":"C22 insurance rows require rate-cycle, underwriting margin, reserve/capital buffer, solvency, ROE, capital-return or earnings bridge; insurance/M&A/value-up theme MFE alone is insufficient."}
```

### 20.3 trigger rows

```jsonl
{"row_type":"trigger","trigger_id":"TRG_R6L76_C22_138040_20240129_INSURANCE_HOLDCO_CAPITAL_RETURN_RESERVE_BUFFER_BRIDGE","case_id":"R6L76_C22_138040_20240129_INSURANCE_HOLDCO_CAPITAL_RETURN_RESERVE_BUFFER_BRIDGE","symbol":"138040","company_name":"메리츠금융지주","round":"R6","loop":"76","large_sector_id":"L6_FINANCIAL_CAPITAL_RETURN_DIGITAL","canonical_archetype_id":"C22_INSURANCE_RATE_CYCLE_RESERVE","fine_archetype_id":"C22_INSURANCE_HOLDCO_CAPITAL_RETURN_RESERVE_BUFFER_BRIDGE","deep_sub_archetype_id":"INSURANCE_FINANCIAL_HOLDCO_CAPITAL_RETURN_ROE_RESERVE_BUFFER_TO_PBR_RERATING","loop_objective":"coverage_gap_fill|counterexample_mining|stage2_actionable_bonus_stress_test|4B_non_price_requirement_stress_test|canonical_archetype_compression","trigger_type":"Stage2-Actionable","trigger_date":"2024-01-29","entry_date":"2024-01-29","entry_price":64300,"evidence_available_at_that_date":"source_proxy_insurance_financial_holdco_capital_return_ROE_reserve_buffer_PBR_repair_bridge; evidence_url_pending","evidence_source":"source_proxy_insurance_financial_holdco_capital_return_ROE_reserve_buffer_PBR_repair_bridge; evidence_url_pending","bridge_summary":"insurance-linked financial holding value-up converted into capital-return execution, ROE visibility, reserve/capital-buffer confidence and PBR repair rather than generic value-up theme only","stage2_evidence_fields":["insurance_holdco_valueup","capital_return_policy_proxy","ROE_recovery_proxy","relative_strength"],"stage3_evidence_fields":["capital_return_execution","reserve_buffer_confidence","PBR_discount_repair","earnings_visibility_proxy"],"stage4b_evidence_fields":["post_MFE_peak_watch","financial_valueup_crowding","reserve_capital_sensitivity"],"stage4c_evidence_fields":["post_peak_drawdown_watch"],"price_data_source":"Songdaiki/stock-web","price_data_repo":"Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/138/138040/2024.csv","profile_path":"atlas/symbol_profiles/138/138040.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":37.33,"MFE_90D_pct":37.33,"MFE_180D_pct":55.37,"MFE_1Y_pct":55.37,"MFE_2Y_pct":55.37,"MAE_30D_pct":-1.87,"MAE_90D_pct":-1.87,"MAE_180D_pct":-1.87,"MAE_1Y_pct":-1.87,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-10-07","peak_price":99900,"drawdown_after_peak_pct":-3.2,"green_lateness_ratio":"0.39","four_b_local_peak_proximity":0.88,"four_b_full_window_peak_proximity":1.0,"four_b_timing_verdict":"insurance_holdco_capital_return_bridge_positive_but_full_window_4B_watch","four_b_evidence_type":"non_price_rate_reserve_capital_return_bridge","four_c_protection_label":"post_peak_drawdown_watch","trigger_outcome_label":"insurance_holdco_capital_return_success_then_4B_watch","current_profile_verdict":"current_profile_correct_but_no_green","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"R6L76_C22_138040_20240129_INSURANCE_HOLDCO_CAPITAL_RETURN_RESERVE_BUFFER_BRIDGE_entry","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"TRG_R6L76_C22_003690_20240129_REINSURANCE_UNDERWRITING_RATE_RESERVE_BRIDGE","case_id":"R6L76_C22_003690_20240129_REINSURANCE_UNDERWRITING_RATE_RESERVE_BRIDGE","symbol":"003690","company_name":"코리안리","round":"R6","loop":"76","large_sector_id":"L6_FINANCIAL_CAPITAL_RETURN_DIGITAL","canonical_archetype_id":"C22_INSURANCE_RATE_CYCLE_RESERVE","fine_archetype_id":"C22_REINSURANCE_UNDERWRITING_RATE_RESERVE_BRIDGE","deep_sub_archetype_id":"REINSURANCE_HARD_MARKET_RATE_CYCLE_AND_RESERVE_BUFFER_TO_ROE_CAPITAL_RETURN","loop_objective":"coverage_gap_fill|counterexample_mining|stage2_actionable_bonus_stress_test|4B_non_price_requirement_stress_test|canonical_archetype_compression","trigger_type":"Stage2-Actionable","trigger_date":"2024-01-29","entry_date":"2024-01-29","entry_price":7400,"evidence_available_at_that_date":"source_proxy_reinsurance_rate_cycle_underwriting_margin_reserve_buffer_capital_return_bridge; evidence_url_pending","evidence_source":"source_proxy_reinsurance_rate_cycle_underwriting_margin_reserve_buffer_capital_return_bridge; evidence_url_pending","bridge_summary":"reinsurance hard-market rate cycle and underwriting-margin visibility converted into reserve-buffer and capital-return bridge, but post-peak capital/reserve sensitivity required 4B watch","stage2_evidence_fields":["reinsurance_rate_cycle","underwriting_margin_proxy","reserve_buffer_proxy","relative_strength"],"stage3_evidence_fields":["rate_cycle_to_ROE_visibility","reserve_buffer_confidence","capital_return_visibility"],"stage4b_evidence_fields":["post_MFE_peak_watch","reserve_cycle_sensitivity","financial_valueup_crowding"],"stage4c_evidence_fields":["post_peak_drawdown_watch"],"price_data_source":"Songdaiki/stock-web","price_data_repo":"Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/003/003690/2024.csv","profile_path":"atlas/symbol_profiles/003/003690.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":13.78,"MFE_90D_pct":15.54,"MFE_180D_pct":25.27,"MFE_1Y_pct":25.27,"MFE_2Y_pct":25.27,"MAE_30D_pct":-2.97,"MAE_90D_pct":-2.97,"MAE_180D_pct":-2.97,"MAE_1Y_pct":-2.97,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-10-24","peak_price":9270,"drawdown_after_peak_pct":-14.89,"green_lateness_ratio":"0.46","four_b_local_peak_proximity":0.91,"four_b_full_window_peak_proximity":1.0,"four_b_timing_verdict":"reinsurance_rate_reserve_bridge_positive_but_4B_drawdown_watch","four_b_evidence_type":"non_price_rate_reserve_capital_return_bridge","four_c_protection_label":"post_peak_drawdown_watch","trigger_outcome_label":"reinsurance_rate_reserve_success_then_4B_watch","current_profile_verdict":"current_profile_correct_with_drawdown_guard","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"R6L76_C22_003690_20240129_REINSURANCE_UNDERWRITING_RATE_RESERVE_BRIDGE_entry","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"TRG_R6L76_C22_000400_20240213_SMALL_NONLIFE_MNA_THEME_NO_RESERVE_ROE_BRIDGE","case_id":"R6L76_C22_000400_20240213_SMALL_NONLIFE_MNA_THEME_NO_RESERVE_ROE_BRIDGE","symbol":"000400","company_name":"롯데손해보험","round":"R6","loop":"76","large_sector_id":"L6_FINANCIAL_CAPITAL_RETURN_DIGITAL","canonical_archetype_id":"C22_INSURANCE_RATE_CYCLE_RESERVE","fine_archetype_id":"C22_SMALL_NONLIFE_MNA_THEME_WITHOUT_RESERVE_ROE_BRIDGE","deep_sub_archetype_id":"SMALL_NONLIFE_INSURANCE_SALE_OR_MNA_OPTIONALITY_WITHOUT_RESERVE_BUFFER_ROE_CAPITAL_RETURN_CONVERSION","loop_objective":"coverage_gap_fill|counterexample_mining|stage2_actionable_bonus_stress_test|4B_non_price_requirement_stress_test|canonical_archetype_compression","trigger_type":"Stage2-Actionable","trigger_date":"2024-02-13","entry_date":"2024-02-13","entry_price":3370,"evidence_available_at_that_date":"source_proxy_small_nonlife_insurance_MNA_sale_theme_without_reserve_buffer_ROE_capital_return_bridge; evidence_url_pending","evidence_source":"source_proxy_small_nonlife_insurance_MNA_sale_theme_without_reserve_buffer_ROE_capital_return_bridge; evidence_url_pending","bridge_summary":"small non-life insurance sale/M&A optionality produced MFE, but reserve-buffer confidence, ROE recovery, solvency and capital-return bridge were weak; the path later printed high MAE","stage2_evidence_fields":["small_nonlife_MNA_theme","insurance_sale_optionality","relative_strength"],"stage3_evidence_fields":[],"stage4b_evidence_fields":["MNA_theme_peak","reserve_buffer_bridge_absent","capital_return_execution_absent"],"stage4c_evidence_fields":["high_MAE_without_reserve_or_ROE_bridge"],"price_data_source":"Songdaiki/stock-web","price_data_repo":"Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/000/000400/2024.csv","profile_path":"atlas/symbol_profiles/000/000400.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":8.9,"MFE_90D_pct":8.9,"MFE_180D_pct":21.36,"MFE_1Y_pct":21.36,"MFE_2Y_pct":21.36,"MAE_30D_pct":-19.88,"MAE_90D_pct":-19.88,"MAE_180D_pct":-35.46,"MAE_1Y_pct":-35.46,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-06-26","peak_price":4090,"drawdown_after_peak_pct":-46.82,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":0.9,"four_b_full_window_peak_proximity":1.0,"four_b_timing_verdict":"small_nonlife_MNA_MFE_but_no_reserve_ROE_bridge_keep_4B_high_MAE_watch","four_b_evidence_type":"insurance_MNA_theme_without_reserve_ROE_bridge","four_c_protection_label":"high_MAE_watch","trigger_outcome_label":"small_nonlife_MNA_theme_MFE_then_high_MAE_counterexample","current_profile_verdict":"current_profile_false_positive_if_green","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"R6L76_C22_000400_20240213_SMALL_NONLIFE_MNA_THEME_NO_RESERVE_ROE_BRIDGE_entry","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
```

### 20.4 score_simulation rows

```jsonl
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"R6L76_C22_138040_20240129_INSURANCE_HOLDCO_CAPITAL_RETURN_RESERVE_BUFFER_BRIDGE","trigger_id":"TRG_R6L76_C22_138040_20240129_INSURANCE_HOLDCO_CAPITAL_RETURN_RESERVE_BUFFER_BRIDGE","symbol":"138040","large_sector_id":"L6_FINANCIAL_CAPITAL_RETURN_DIGITAL","canonical_archetype_id":"C22_INSURANCE_RATE_CYCLE_RESERVE","raw_component_scores_before":{"rate_cycle_score":12,"reserve_buffer_score":11,"ROE_score":12,"capital_return_score":12,"relative_strength_score":10,"theme_risk_penalty":6},"weighted_score_before":74,"stage_label_before":"Stage2-Actionable","raw_component_scores_after":{"rate_cycle_score":14,"reserve_buffer_score":14,"ROE_score":15,"capital_return_score":15,"relative_strength_score":8,"theme_risk_penalty":8},"weighted_score_after":82,"stage_label_after":"Stage3-Yellow","changed_components":["rate_cycle_score","reserve_buffer_score","ROE_score","capital_return_score","relative_strength_score","theme_risk_penalty"],"component_delta_explanation":"C22 row is promoted only because insurance value-up/rate-cycle signal converts into reserve buffer, ROE and capital-return bridge; 4B drawdown/reserve sensitivity blocks Green.","MFE_90D_pct":37.33,"MAE_90D_pct":-1.87,"score_return_alignment_label":"score_return_aligned","current_profile_verdict":"current_profile_correct_but_no_green"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"R6L76_C22_003690_20240129_REINSURANCE_UNDERWRITING_RATE_RESERVE_BRIDGE","trigger_id":"TRG_R6L76_C22_003690_20240129_REINSURANCE_UNDERWRITING_RATE_RESERVE_BRIDGE","symbol":"003690","large_sector_id":"L6_FINANCIAL_CAPITAL_RETURN_DIGITAL","canonical_archetype_id":"C22_INSURANCE_RATE_CYCLE_RESERVE","raw_component_scores_before":{"rate_cycle_score":12,"reserve_buffer_score":11,"ROE_score":12,"capital_return_score":12,"relative_strength_score":10,"theme_risk_penalty":6},"weighted_score_before":74,"stage_label_before":"Stage2-Actionable","raw_component_scores_after":{"rate_cycle_score":14,"reserve_buffer_score":14,"ROE_score":15,"capital_return_score":15,"relative_strength_score":8,"theme_risk_penalty":8},"weighted_score_after":82,"stage_label_after":"Stage3-Yellow","changed_components":["rate_cycle_score","reserve_buffer_score","ROE_score","capital_return_score","relative_strength_score","theme_risk_penalty"],"component_delta_explanation":"C22 row is promoted only because insurance value-up/rate-cycle signal converts into reserve buffer, ROE and capital-return bridge; 4B drawdown/reserve sensitivity blocks Green.","MFE_90D_pct":15.54,"MAE_90D_pct":-2.97,"score_return_alignment_label":"score_return_aligned","current_profile_verdict":"current_profile_correct_with_drawdown_guard"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"R6L76_C22_000400_20240213_SMALL_NONLIFE_MNA_THEME_NO_RESERVE_ROE_BRIDGE","trigger_id":"TRG_R6L76_C22_000400_20240213_SMALL_NONLIFE_MNA_THEME_NO_RESERVE_ROE_BRIDGE","symbol":"000400","large_sector_id":"L6_FINANCIAL_CAPITAL_RETURN_DIGITAL","canonical_archetype_id":"C22_INSURANCE_RATE_CYCLE_RESERVE","raw_component_scores_before":{"rate_cycle_score":4,"reserve_buffer_score":1,"ROE_score":1,"capital_return_score":1,"relative_strength_score":10,"theme_risk_penalty":9},"weighted_score_before":61,"stage_label_before":"Stage2-Actionable","raw_component_scores_after":{"rate_cycle_score":1,"reserve_buffer_score":0,"ROE_score":0,"capital_return_score":0,"relative_strength_score":4,"theme_risk_penalty":16},"weighted_score_after":38,"stage_label_after":"Stage1-Watch_or_4B-HighMAE","changed_components":["rate_cycle_score","reserve_buffer_score","ROE_score","capital_return_score","relative_strength_score","theme_risk_penalty"],"component_delta_explanation":"C22 guard demotes insurance M&A/sale theme rows when reserve buffer, ROE, solvency and capital-return bridge are absent.","MFE_90D_pct":8.9,"MAE_90D_pct":-19.88,"score_return_alignment_label":"score_return_mixed","current_profile_verdict":"current_profile_false_positive_if_green"}
```

### 20.5 shadow_weight rows

```csv
row_type,axis,scope,large_sector_id,canonical_archetype_id,baseline_value,tested_value,delta,reason,backtest_effect,trigger_ids,calibration_usable_count,new_independent_case_count,counterexample_count,confidence,proposal_type,notes
shadow_weight,c22_requires_rate_reserve_roe_capital_return_bridge,canonical_archetype_specific,L6_FINANCIAL_CAPITAL_RETURN_DIGITAL,C22_INSURANCE_RATE_CYCLE_RESERVE,0,1,+1,"C22 insurance/rate-cycle rows should not promote toward Stage3-Yellow/Green unless insurance signal converts into rate-cycle, underwriting margin, reserve/capital buffer, solvency, ROE, capital-return, or earnings bridge","138040 and 003690 survive as guarded positives after capital-return/reserve/rate-cycle bridge; 000400 is demoted because small non-life M&A theme lacked durable reserve, solvency, ROE and capital-return bridge","TRG_R6L76_C22_138040_20240129_INSURANCE_HOLDCO_CAPITAL_RETURN_RESERVE_BUFFER_BRIDGE|TRG_R6L76_C22_003690_20240129_REINSURANCE_UNDERWRITING_RATE_RESERVE_BRIDGE|TRG_R6L76_C22_000400_20240213_SMALL_NONLIFE_MNA_THEME_NO_RESERVE_ROE_BRIDGE",3,3,1,medium,canonical_shadow_only,"not production; post-calibrated residual"
shadow_weight,c22_insurance_theme_4b_high_mae_watch_guard,canonical_archetype_specific,L6_FINANCIAL_CAPITAL_RETURN_DIGITAL,C22_INSURANCE_RATE_CYCLE_RESERVE,1,1,0,"Insurance winners and M&A/theme false starts can peak before reserve/ROE/capital-return durability is confirmed; local/full-window 4B and high-MAE watch should remain active","preserves 138040/003690 guarded positives while preventing 000400 insurance-theme false positive","TRG_R6L76_C22_138040_20240129_INSURANCE_HOLDCO_CAPITAL_RETURN_RESERVE_BUFFER_BRIDGE|TRG_R6L76_C22_003690_20240129_REINSURANCE_UNDERWRITING_RATE_RESERVE_BRIDGE|TRG_R6L76_C22_000400_20240213_SMALL_NONLIFE_MNA_THEME_NO_RESERVE_ROE_BRIDGE",3,3,1,medium,existing_axis_kept,"strengthens local/full-window 4B and high-MAE watch without global delta"
```

### 20.6 residual_contribution row

```jsonl
{"row_type":"residual_contribution","round":"R6","loop":"76","large_sector_id":"L6_FINANCIAL_CAPITAL_RETURN_DIGITAL","canonical_archetype_id":"C22_INSURANCE_RATE_CYCLE_RESERVE","new_independent_case_count":3,"reused_case_count":0,"new_symbol_count":3,"new_trigger_family_count":3,"tested_existing_calibrated_axes":["stage2_actionable_evidence_bonus","price_only_blowoff_blocks_positive_stage","full_4b_requires_non_price_evidence","local_4b_watch_guard","high_MAE_guardrail"],"residual_error_types_found":["insurance_MNA_theme_without_reserve_ROE_bridge","insurance_holdco_capital_return_winner_needs_4B_watch","reinsurance_rate_reserve_winner_needs_drawdown_guard"],"loop_contribution_label":"canonical_archetype_rule_candidate","do_not_propose_new_weight_delta":false}
```

## 21. Deferred Coding Agent Handoff Prompt

### Purpose

You are now in the repository implementation phase. The attached Markdown files are v12 post-calibrated residual research outputs produced using the Songdaiki/stock-web OHLC atlas.

These MDs are not live candidate research. They are historical calibration research designed to extend the already-applied e2r_2_1_stock_web_calibrated profile.

Do not blindly apply every shadow row. Ingest the machine-readable rows and update the sector/canonical-archetype calibration ledger.

### R6-specific handling

- R6 maps to `L6_FINANCIAL_CAPITAL_RETURN_DIGITAL`.
- This MD uses `C22_INSURANCE_RATE_CYCLE_RESERVE`.
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
- Positive score promotion requires non-price evidence and clean MFE/MAE.
- 4B rows are overlay/risk calibration only.
- 4C rows are thesis-break/protection calibration only.
- price-only/insurance-theme-only rows cannot promote Stage2/Stage3.
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
12. Add validation that C22 insurance/rate-cycle rows cannot promote without rate-cycle improvement, underwriting-margin improvement, reserve/capital buffer, solvency confidence, ROE recovery, capital-return execution, dividend visibility, earnings revision, or PBR discount repair tied to insurance economics.

### Expected output

- Concise implementation summary.
- Rows accepted/rejected.
- New sector/canonical archetype coverage.
- Existing axis strengthened/weakened/kept.
- No investment recommendation language.

## 22. Next Round State

```text
completed_round = R6
completed_loop = 76
next_round = R7
next_loop = 76
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
atlas/symbol_profiles/138/138040.json
atlas/symbol_profiles/003/003690.json
atlas/symbol_profiles/000/000400.json
atlas/ohlcv_tradable_by_symbol_year/138/138040/2024.csv
atlas/ohlcv_tradable_by_symbol_year/003/003690/2024.csv
atlas/ohlcv_tradable_by_symbol_year/000/000400/2024.csv
```

This loop continues loop 76 with R6 and adds 3 new independent C22 representative cases, 2 positives, 1 counterexample/watch case, and 1 canonical-archetype residual guard candidate for R6/L6.
