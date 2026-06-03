# E2R Stock-Web Historical Calibration / Sector-Archetype Residual Research Round

## 0. Research Metadata

```text
scheduled_round: R6
scheduled_loop: 72
round_schedule_status: valid
round_sector_consistency: pass
computed_next_round: R7
computed_next_loop: 72
large_sector_id: L6_FINANCIAL_CAPITAL_RETURN_DIGITAL
canonical_archetype_id: C22_INSURANCE_RATE_CYCLE_RESERVE
fine_archetype_id: C22_INSURANCE_RESERVE_SOLVENCY_CAPITAL_RETURN_BRIDGE_GUARD
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

R6 maps to `L6_FINANCIAL_CAPITAL_RETURN_DIGITAL`. The prior R6 loop already filled C21 regional-bank capital-return coverage, so this run shifts to C22 insurance/rate-cycle/reserve. The core residual is whether insurer value-up and IFRS17/ROE narratives are supported by reserve quality, solvency, rate-cycle durability, and capital-return execution.

| layer | id | definition |
|---|---|---|
| round | R6 | financial / capital return / digital |
| large_sector | L6_FINANCIAL_CAPITAL_RETURN_DIGITAL | banks, insurance, brokers, capital return, financial value-up |
| canonical | C22_INSURANCE_RATE_CYCLE_RESERVE | insurance ROE/rate cycle/reserve/solvency/capital return |
| fine | C22_INSURANCE_RESERVE_SOLVENCY_CAPITAL_RETURN_BRIDGE_GUARD | insurer rerating requires reserve and solvency bridge |
| deep | IFRS17_ROE_RESERVE_VALUEUP_WITH_SOLVENCY_GUARD | small P&C ROE/value-up success |
| deep | REINSURANCE_RATE_HARDENING_RESERVE_AND_CAPITAL_RETURN_VISIBILITY | stable reinsurance rate-cycle success |
| deep | SMALL_PNC_INSURER_VALUEUP_THEME_WITHOUT_RESERVE_SOLVENCY_BRIDGE | price-only value-up blowoff |

## 3. No-Repeat / Coverage Check

No-Repeat hard duplicate key:

```text
canonical_archetype_id + symbol + trigger_type + entry_date
```

C22 top-covered symbols are `000810`, `005830`, `088350`, `001450`, `032830`, and `085620`. This run avoids that top cluster and uses non-top-covered insurance/reinsurance names.

| archetype | selected symbol | duplicate status | reason |
|---|---:|---|---|
| C22 | 000370 | new independent | not top-covered C22 symbol; small P&C ROE/value-up bridge |
| C22 | 003690 | new independent | not top-covered C22 symbol; reinsurance rate-cycle/reserve bridge |
| C22 | 000540 | new independent | not top-covered C22 symbol; small-insurer value-up blowoff counterexample |

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

## 6. Case Selection Summary

| role | symbol | company | trigger | entry | price | result |
|---|---:|---|---|---:|---:|---|
| structural_success_then_4B_watch | 000370 | 한화손해보험 | Stage2-Actionable | 2024-01-29 | 4050 | small P&C ROE/value-up bridge worked |
| structural_success_low_volatility | 003690 | 코리안리 | Stage2-Actionable | 2024-01-24 | 7160 | reinsurance rate-cycle/reserve bridge worked with low MAE |
| failed_rerating_high_MAE_after_blowoff | 000540 | 흥국화재 | Stage2-Actionable | 2024-02-13 | 5280 | small-insurer value-up price spike without bridge failed |

## 7. Positive vs Counterexample Balance

```text
positive_case_count: 2
counterexample_count: 1
4B_case_count: 3
4C_or_high_MAE_watch_count: 1
calibration_usable_case_count: 3
current_profile_error_count: 1
```

## 8. Trigger-Level OHLC Backtest Table

| symbol | company | trigger | entry_date | entry_price | MFE30 | MFE90 | MFE180 | MAE30 | MAE90 | MAE180 | peak_date | peak_price | DD after peak |
|---:|---|---|---|---:|---:|---:|---:|---:|---:|---:|---|---:|---:|
| 000370 | 한화손해보험 | Stage2-Actionable | 2024-01-29 | 4050 | 52.35 | 52.35 | 53.83 | -3.21 | -6.3 | -6.3 | 2024-08-20 | 6230 | -27.21 |
| 003690 | 코리안리 | Stage2-Actionable | 2024-01-24 | 7160 | 16.34 | 19.41 | 19.41 | -1.82 | -1.82 | -1.82 | 2024-03-22 | 8550 | -8.07 |
| 000540 | 흥국화재 | Stage2-Actionable | 2024-02-13 | 5280 | 25.0 | 25.0 | 25.0 | -18.56 | -28.69 | -28.69 | 2024-02-14 | 6600 | -42.95 |

## 9. Case-by-Case Notes

### 9.1 000370 / 한화손해보험 — ROE/value-up bridge positive

The entry row is 2024-01-29 at 4,050. The first strong MFE arrives quickly, but the full-window peak is later at 6,230. This is the valid C22 small-insurer route: IFRS17/ROE and value-up language must pass through reserve quality, solvency buffer, and capital-return plausibility before Stage2 travels upward.

### 9.2 003690 / 코리안리 — reinsurance rate-cycle bridge

The entry row is 2024-01-24 at 7,160. The path is not explosive, but MAE is contained and the 90D high reaches 8,550. For C22, this is useful because insurance/reinsurance rerating does not always need high beta. A modest MFE with controlled downside can still validate the rate-cycle/reserve bridge.

### 9.3 000540 / 흥국화재 — small-insurer value-up blowoff

The entry row is 2024-02-13 at 5,280. The next-day/local peak reaches 6,600, but the path then falls to 3,765. This is the C22 trap: small-insurer value-up heat can look like capital-return rerating, but without reserve quality, solvency, and execution bridge, the candle burns backward into high MAE.

## 10. Current Calibrated Profile Stress Test

| question | result |
|---|---|
| Stage2 actionable bonus too strong? | Yes when C22 treats small-insurer value-up price strength as enough evidence. |
| Stage3 Yellow threshold too loose? | Not globally; C22 needs reserve/solvency/capital-return bridge before Yellow. |
| Stage3 Green too strict? | Correct. No Green loosening. |
| Price-only blowoff guard appropriate? | Yes, especially for 000540 near the local value-up peak. |
| Full 4B non-price requirement appropriate? | Yes. 000370/003690 have non-price bridge; 000540 does not. |
| 4C timing issue? | High-MAE watch is useful; no immediate hard 4C promotion proposed. |

## 11. Stage2 / Yellow / Green Comparison

```text
000370:
  Stage2-Actionable = correct
  Stage3-Yellow = allowed after ROE/reserve/capital-return bridge
  Stage3-Green = wait for stronger solvency and capital-return execution durability

003690:
  Stage2-Actionable = correct
  Stage3-Yellow = allowed despite modest MFE because MAE is controlled and rate-cycle bridge is cleaner
  Stage3-Green = wait for stronger shareholder-return and reserve quality confirmation

000540:
  Stage2-Actionable = too generous if based only on small-insurer value-up price strength
  Stage3-Yellow = reject without reserve/solvency/capital-return bridge
  Stage3-Green = reject
```

## 12. 4B Local vs Full-window Timing Audit

| symbol | local_peak_proximity | full_window_peak_proximity | verdict |
|---:|---:|---:|---|
| 000370 | 0.90 | 1.00 | good full-window 4B watch after ROE/value-up bridge |
| 003690 | 0.97 | 1.00 | low-volatility 4B watch after rate-cycle bridge |
| 000540 | 1.00 | 1.00 | price-only small-insurer 4B watch, not positive stage |

## 13. Canonical-Archetype Rule Candidate

```text
canonical_archetype_rule_candidate: true
rule_scope: canonical_archetype_specific
rule_id: c22_requires_reserve_solvency_capital_return_bridge

rule:
  For C22 insurance/rate-cycle rows, do not promote insurer value-up or IFRS17/ROE Stage2 signals
  into Stage3-Yellow/Green unless at least one non-price bridge is visible:
  reserve quality, solvency buffer, rate-cycle durability, capital-return execution,
  loss-ratio normalization, or reliable shareholder-return policy.
```

## 14. Before / After Backtest Comparison

| profile | eligible triggers | avg MFE90 | avg MAE90 | false positive rate | verdict |
|---|---:|---:|---:|---:|---|
| P0 e2r_2_1_stock_web_calibrated_proxy | 3 | 32.25 | -12.27 | 33.3% | useful but can over-credit small-insurer value-up blowoff |
| P0b e2r_2_0_baseline_reference | 3 | 32.25 | -12.27 | 0% | safer but may miss 000370 and 003690 |
| P1 sector_specific_candidate_profile | 3 | 32.25 | -12.27 | 33.3% | no broad L6 loosen |
| P2 canonical_archetype_candidate_profile | 2 selected positives | 35.88 | -4.06 | 0% after bridge gate | preferred shadow |
| P3 counterexample_guard_profile | 1 rejected | 25.0 | -28.69 | 0% after demotion | useful guard |

## 15. Score-Return Alignment Matrix

| case | current profile verdict | alignment |
|---|---|---|
| 000370 | current_profile_correct | ROE/value-up bridge aligned with strong MFE |
| 003690 | current_profile_correct | rate-cycle/reserve bridge aligned with low-MAE positive path |
| 000540 | current_profile_false_positive | price-only value-up blowoff produced high MAE |

## 16. Coverage Matrix

| large_sector_id | canonical_archetype_id | fine_archetype_id | positive | counterexample | 4B | 4C/watch | new_independent | reused | usable_triggers | representative | profile_errors | sector_rule | canonical_rule | coverage_gap_after |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|---|---|
| L6_FINANCIAL_CAPITAL_RETURN_DIGITAL | C22_INSURANCE_RATE_CYCLE_RESERVE | C22_INSURANCE_RESERVE_SOLVENCY_CAPITAL_RETURN_BRIDGE_GUARD | 2 | 1 | 3 | 1 | 3 | 0 | 3 | 3 | 1 | false | true | C22 non-top-covered insurance reserve/solvency residual reduced |

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
- small insurer value-up without reserve/solvency bridge
- insurance rate-cycle winner needs 4B watch
- price blowoff high-MAE after theme Stage2
new_axis_proposed: null
existing_axis_strengthened:
- stage2_required_bridge
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
- round/sector/canonical consistency
- duplicate avoidance at symbol level
```

Not validated:

```text
- exact disclosure URLs
- exact report URLs
- production scoring behavior
- live candidate status
```

## 19. Shadow Weight Calibration

```csv
row_type,axis,scope,large_sector_id,canonical_archetype_id,baseline_value,tested_value,delta,reason,backtest_effect,trigger_ids,calibration_usable_count,new_independent_case_count,counterexample_count,confidence,proposal_type,notes
shadow_weight,c22_requires_reserve_solvency_capital_return_bridge,canonical_archetype_specific,L6_FINANCIAL_CAPITAL_RETURN_DIGITAL,C22_INSURANCE_RATE_CYCLE_RESERVE,0,1,+1,"C22 insurance rows should not promote toward Stage3-Yellow/Green unless IFRS17/ROE/rate-cycle signal converts into reserve quality, solvency buffer, and capital-return bridge","000370 and 003690 survive with cleaner MFE/MAE; 000540 fails when small-insurer value-up theme lacks reserve/solvency bridge","TRG_R6L72_C22_000370_20240129_SMALL_PNC_ROE_VALUEUP_BRIDGE|TRG_R6L72_C22_003690_20240124_REINSURANCE_RATE_CYCLE_STABLE_BRIDGE|TRG_R6L72_C22_000540_20240213_SMALL_INSURER_PRICE_VALUEUP_BLOWOFF",3,3,1,medium,canonical_shadow_only,"not production; post-calibrated residual"
shadow_weight,c22_small_insurer_price_blowoff_high_mae_watch_guard,canonical_archetype_specific,L6_FINANCIAL_CAPITAL_RETURN_DIGITAL,C22_INSURANCE_RATE_CYCLE_RESERVE,1,1,0,"Small insurer value-up rows can peak before reserve/solvency/capital-return evidence is confirmed; local 4B/high-MAE watch should remain active","preserves 000370/003690 positives while preventing 000540 price-only false positive","TRG_R6L72_C22_000370_20240129_SMALL_PNC_ROE_VALUEUP_BRIDGE|TRG_R6L72_C22_003690_20240124_REINSURANCE_RATE_CYCLE_STABLE_BRIDGE|TRG_R6L72_C22_000540_20240213_SMALL_INSURER_PRICE_VALUEUP_BLOWOFF",3,3,1,medium,existing_axis_kept,"strengthens local 4B/high-MAE watch without global delta"
```

## 20. Machine-Readable Rows

### 20.1 price_source_validation

```jsonl
{"row_type":"price_source_validation","source":"Songdaiki/stock-web","source_url":"https://github.com/Songdaiki/stock-web","manifest_path":"atlas/manifest.json","schema_path":"atlas/schema.json","universe_path":"atlas/universe/all_symbols.csv","manifest_max_date":"2026-02-20","source_name":"FinanceData/marcap","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","calibration_shard_root":"atlas/ohlcv_tradable_by_symbol_year","raw_shard_root":"atlas/ohlcv_raw_by_symbol_year","validation_status":"usable_for_historical_calibration"}
```

### 20.2 case rows

```jsonl
{"row_type":"case","case_id":"R6L72_C22_000370_20240129_SMALL_PNC_ROE_VALUEUP_BRIDGE","symbol":"000370","company_name":"한화손해보험","round":"R6","loop":"72","large_sector_id":"L6_FINANCIAL_CAPITAL_RETURN_DIGITAL","canonical_archetype_id":"C22_INSURANCE_RATE_CYCLE_RESERVE","fine_archetype_id":"C22_SMALL_PNC_INSURANCE_ROE_CAPITAL_RETURN_BRIDGE","deep_sub_archetype_id":"IFRS17_ROE_RESERVE_VALUEUP_WITH_SOLVENCY_GUARD","case_type":"structural_success_then_4B_watch","positive_or_counterexample":"positive","best_trigger":"Stage2-Actionable","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"score_return_aligned","current_profile_verdict":"current_profile_correct","price_source":"Songdaiki/stock-web","notes":"C22 insurance rows require ROE/rate-cycle/reserve-quality/solvency/capital-return bridge; small-insurer value-up price spike alone is insufficient."}
{"row_type":"case","case_id":"R6L72_C22_003690_20240124_REINSURANCE_RATE_CYCLE_STABLE_BRIDGE","symbol":"003690","company_name":"코리안리","round":"R6","loop":"72","large_sector_id":"L6_FINANCIAL_CAPITAL_RETURN_DIGITAL","canonical_archetype_id":"C22_INSURANCE_RATE_CYCLE_RESERVE","fine_archetype_id":"C22_REINSURANCE_RATE_CYCLE_RESERVE_BRIDGE","deep_sub_archetype_id":"REINSURANCE_RATE_HARDENING_RESERVE_AND_CAPITAL_RETURN_VISIBILITY","case_type":"structural_success_low_volatility","positive_or_counterexample":"positive","best_trigger":"Stage2-Actionable","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"score_return_aligned","current_profile_verdict":"current_profile_correct","price_source":"Songdaiki/stock-web","notes":"C22 insurance rows require ROE/rate-cycle/reserve-quality/solvency/capital-return bridge; small-insurer value-up price spike alone is insufficient."}
{"row_type":"case","case_id":"R6L72_C22_000540_20240213_SMALL_INSURER_PRICE_VALUEUP_BLOWOFF","symbol":"000540","company_name":"흥국화재","round":"R6","loop":"72","large_sector_id":"L6_FINANCIAL_CAPITAL_RETURN_DIGITAL","canonical_archetype_id":"C22_INSURANCE_RATE_CYCLE_RESERVE","fine_archetype_id":"C22_SMALL_INSURER_PRICE_ONLY_VALUEUP_BLOWOFF_GUARD","deep_sub_archetype_id":"SMALL_PNC_INSURER_VALUEUP_THEME_WITHOUT_RESERVE_SOLVENCY_BRIDGE","case_type":"failed_rerating_high_MAE_after_blowoff","positive_or_counterexample":"counterexample","best_trigger":"Stage2-Actionable","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"score_return_misaligned","current_profile_verdict":"current_profile_false_positive","price_source":"Songdaiki/stock-web","notes":"C22 insurance rows require ROE/rate-cycle/reserve-quality/solvency/capital-return bridge; small-insurer value-up price spike alone is insufficient."}
```

### 20.3 trigger rows

```jsonl
{"row_type":"trigger","trigger_id":"TRG_R6L72_C22_000370_20240129_SMALL_PNC_ROE_VALUEUP_BRIDGE","case_id":"R6L72_C22_000370_20240129_SMALL_PNC_ROE_VALUEUP_BRIDGE","symbol":"000370","company_name":"한화손해보험","round":"R6","loop":"72","large_sector_id":"L6_FINANCIAL_CAPITAL_RETURN_DIGITAL","canonical_archetype_id":"C22_INSURANCE_RATE_CYCLE_RESERVE","fine_archetype_id":"C22_SMALL_PNC_INSURANCE_ROE_CAPITAL_RETURN_BRIDGE","deep_sub_archetype_id":"IFRS17_ROE_RESERVE_VALUEUP_WITH_SOLVENCY_GUARD","loop_objective":"coverage_gap_fill|counterexample_mining|stage2_actionable_bonus_stress_test|4B_non_price_requirement_stress_test|canonical_archetype_compression","trigger_type":"Stage2-Actionable","trigger_date":"2024-01-29","entry_date":"2024-01-29","entry_price":4050,"evidence_available_at_that_date":"source_proxy_IFRS17_ROE_valueup_capital_return_reserve_quality; evidence_url_pending","evidence_source":"source_proxy_IFRS17_ROE_valueup_capital_return_reserve_quality; evidence_url_pending","bridge_summary":"small P&C insurer rerating worked when ROE/value-up narrative had reserve/solvency and shareholder-return bridge","stage2_evidence_fields":["IFRS17_ROE_visibility","capital_return_valueup_proxy","reserve_quality_watch","relative_strength"],"stage3_evidence_fields":["ROE_PBR_rerating_visibility","capital_return_execution_proxy","solvency_buffer_check"],"stage4b_evidence_fields":["post_MFE_peak_watch","small_insurer_crowding_after_valueup"],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/000/000370/2024.csv","profile_path":"atlas/symbol_profiles/000/000370.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":52.35,"MFE_90D_pct":52.35,"MFE_180D_pct":53.83,"MFE_1Y_pct":53.83,"MFE_2Y_pct":53.83,"MAE_30D_pct":-3.21,"MAE_90D_pct":-6.3,"MAE_180D_pct":-6.3,"MAE_1Y_pct":-6.3,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-08-20","peak_price":6230,"drawdown_after_peak_pct":-27.21,"green_lateness_ratio":"0.35","four_b_local_peak_proximity":0.9,"four_b_full_window_peak_proximity":1.0,"four_b_timing_verdict":"good_full_window_4B_watch_after_ROE_valueup_bridge","four_b_evidence_type":"non_price_ROE_reserve_capital_return_bridge","four_c_protection_label":"none","trigger_outcome_label":"structural_success_then_4B_watch","current_profile_verdict":"current_profile_correct","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"R6L72_C22_000370_20240129_SMALL_PNC_ROE_VALUEUP_BRIDGE_entry","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"TRG_R6L72_C22_003690_20240124_REINSURANCE_RATE_CYCLE_STABLE_BRIDGE","case_id":"R6L72_C22_003690_20240124_REINSURANCE_RATE_CYCLE_STABLE_BRIDGE","symbol":"003690","company_name":"코리안리","round":"R6","loop":"72","large_sector_id":"L6_FINANCIAL_CAPITAL_RETURN_DIGITAL","canonical_archetype_id":"C22_INSURANCE_RATE_CYCLE_RESERVE","fine_archetype_id":"C22_REINSURANCE_RATE_CYCLE_RESERVE_BRIDGE","deep_sub_archetype_id":"REINSURANCE_RATE_HARDENING_RESERVE_AND_CAPITAL_RETURN_VISIBILITY","loop_objective":"coverage_gap_fill|counterexample_mining|stage2_actionable_bonus_stress_test|4B_non_price_requirement_stress_test|canonical_archetype_compression","trigger_type":"Stage2-Actionable","trigger_date":"2024-01-24","entry_date":"2024-01-24","entry_price":7160,"evidence_available_at_that_date":"source_proxy_reinsurance_rate_cycle_reserve_quality_capital_return; evidence_url_pending","evidence_source":"source_proxy_reinsurance_rate_cycle_reserve_quality_capital_return; evidence_url_pending","bridge_summary":"reinsurance rate-cycle and reserve-quality bridge produced modest but clean MFE with contained MAE","stage2_evidence_fields":["reinsurance_rate_cycle","reserve_quality","capital_return_valueup_proxy","relative_strength"],"stage3_evidence_fields":["rate_cycle_visibility","reserve_quality_confirmation","shareholder_return_proxy"],"stage4b_evidence_fields":["local_valuation_repricing_watch"],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/003/003690/2024.csv","profile_path":"atlas/symbol_profiles/003/003690.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":16.34,"MFE_90D_pct":19.41,"MFE_180D_pct":19.41,"MFE_1Y_pct":19.41,"MFE_2Y_pct":19.41,"MAE_30D_pct":-1.82,"MAE_90D_pct":-1.82,"MAE_180D_pct":-1.82,"MAE_1Y_pct":-1.82,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-03-22","peak_price":8550,"drawdown_after_peak_pct":-8.07,"green_lateness_ratio":"0.48","four_b_local_peak_proximity":0.97,"four_b_full_window_peak_proximity":1.0,"four_b_timing_verdict":"low_volatility_4B_watch_after_rate_cycle_bridge","four_b_evidence_type":"non_price_ROE_reserve_capital_return_bridge","four_c_protection_label":"none","trigger_outcome_label":"structural_success_low_MAE","current_profile_verdict":"current_profile_correct","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"R6L72_C22_003690_20240124_REINSURANCE_RATE_CYCLE_STABLE_BRIDGE_entry","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"TRG_R6L72_C22_000540_20240213_SMALL_INSURER_PRICE_VALUEUP_BLOWOFF","case_id":"R6L72_C22_000540_20240213_SMALL_INSURER_PRICE_VALUEUP_BLOWOFF","symbol":"000540","company_name":"흥국화재","round":"R6","loop":"72","large_sector_id":"L6_FINANCIAL_CAPITAL_RETURN_DIGITAL","canonical_archetype_id":"C22_INSURANCE_RATE_CYCLE_RESERVE","fine_archetype_id":"C22_SMALL_INSURER_PRICE_ONLY_VALUEUP_BLOWOFF_GUARD","deep_sub_archetype_id":"SMALL_PNC_INSURER_VALUEUP_THEME_WITHOUT_RESERVE_SOLVENCY_BRIDGE","loop_objective":"coverage_gap_fill|counterexample_mining|stage2_actionable_bonus_stress_test|4B_non_price_requirement_stress_test|canonical_archetype_compression","trigger_type":"Stage2-Actionable","trigger_date":"2024-02-13","entry_date":"2024-02-13","entry_price":5280,"evidence_available_at_that_date":"source_proxy_small_insurer_valueup_price_blowoff_without_reserve_solvency_bridge; evidence_url_pending","evidence_source":"source_proxy_small_insurer_valueup_price_blowoff_without_reserve_solvency_bridge; evidence_url_pending","bridge_summary":"small insurer value-up price spike lacked reserve/solvency/capital-return execution bridge and reversed into high MAE","stage2_evidence_fields":["insurance_valueup_theme","price_spike","relative_strength"],"stage3_evidence_fields":[],"stage4b_evidence_fields":["price_only_local_peak","small_insurer_crowding","weak_reserve_quality_bridge"],"stage4c_evidence_fields":["high_MAE_without_solvency_or_capital_return_bridge"],"price_data_source":"Songdaiki/stock-web","price_data_repo":"Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/000/000540/2024.csv","profile_path":"atlas/symbol_profiles/000/000540.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":25.0,"MFE_90D_pct":25.0,"MFE_180D_pct":25.0,"MFE_1Y_pct":25.0,"MFE_2Y_pct":25.0,"MAE_30D_pct":-18.56,"MAE_90D_pct":-28.69,"MAE_180D_pct":-28.69,"MAE_1Y_pct":-28.69,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-02-14","peak_price":6600,"drawdown_after_peak_pct":-42.95,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":1.0,"four_b_full_window_peak_proximity":1.0,"four_b_timing_verdict":"price_only_small_insurer_4B_watch_not_positive_stage","four_b_evidence_type":"price_only_small_insurer_valueup_theme","four_c_protection_label":"high_MAE_watch","trigger_outcome_label":"failed_rerating_high_MAE_counterexample","current_profile_verdict":"current_profile_false_positive","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"R6L72_C22_000540_20240213_SMALL_INSURER_PRICE_VALUEUP_BLOWOFF_entry","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
```

### 20.4 score_simulation rows

```jsonl
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"R6L72_C22_000370_20240129_SMALL_PNC_ROE_VALUEUP_BRIDGE","trigger_id":"TRG_R6L72_C22_000370_20240129_SMALL_PNC_ROE_VALUEUP_BRIDGE","symbol":"000370","large_sector_id":"L6_FINANCIAL_CAPITAL_RETURN_DIGITAL","canonical_archetype_id":"C22_INSURANCE_RATE_CYCLE_RESERVE","raw_component_scores_before":{"roe_ifrs17_score":12,"reserve_quality_score":10,"rate_cycle_score":9,"capital_return_score":10,"relative_strength_score":9,"solvency_risk_penalty":4},"weighted_score_before":74,"stage_label_before":"Stage2-Actionable","raw_component_scores_after":{"roe_ifrs17_score":15,"reserve_quality_score":13,"rate_cycle_score":10,"capital_return_score":12,"relative_strength_score":7,"solvency_risk_penalty":4},"weighted_score_after":82,"stage_label_after":"Stage3-Yellow","changed_components":["roe_ifrs17_score","reserve_quality_score","rate_cycle_score","capital_return_score","relative_strength_score","solvency_risk_penalty"],"component_delta_explanation":"C22 row is promoted only because ROE/IFRS17/rate-cycle signal converts into reserve-quality, solvency, and capital-return bridge.","MFE_90D_pct":52.35,"MAE_90D_pct":-6.3,"score_return_alignment_label":"score_return_aligned","current_profile_verdict":"current_profile_correct"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"R6L72_C22_003690_20240124_REINSURANCE_RATE_CYCLE_STABLE_BRIDGE","trigger_id":"TRG_R6L72_C22_003690_20240124_REINSURANCE_RATE_CYCLE_STABLE_BRIDGE","symbol":"003690","large_sector_id":"L6_FINANCIAL_CAPITAL_RETURN_DIGITAL","canonical_archetype_id":"C22_INSURANCE_RATE_CYCLE_RESERVE","raw_component_scores_before":{"roe_ifrs17_score":12,"reserve_quality_score":10,"rate_cycle_score":9,"capital_return_score":10,"relative_strength_score":9,"solvency_risk_penalty":4},"weighted_score_before":74,"stage_label_before":"Stage2-Actionable","raw_component_scores_after":{"roe_ifrs17_score":15,"reserve_quality_score":13,"rate_cycle_score":10,"capital_return_score":12,"relative_strength_score":7,"solvency_risk_penalty":4},"weighted_score_after":82,"stage_label_after":"Stage3-Yellow","changed_components":["roe_ifrs17_score","reserve_quality_score","rate_cycle_score","capital_return_score","relative_strength_score","solvency_risk_penalty"],"component_delta_explanation":"C22 row is promoted only because ROE/IFRS17/rate-cycle signal converts into reserve-quality, solvency, and capital-return bridge.","MFE_90D_pct":19.41,"MAE_90D_pct":-1.82,"score_return_alignment_label":"score_return_aligned","current_profile_verdict":"current_profile_correct"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"R6L72_C22_000540_20240213_SMALL_INSURER_PRICE_VALUEUP_BLOWOFF","trigger_id":"TRG_R6L72_C22_000540_20240213_SMALL_INSURER_PRICE_VALUEUP_BLOWOFF","symbol":"000540","large_sector_id":"L6_FINANCIAL_CAPITAL_RETURN_DIGITAL","canonical_archetype_id":"C22_INSURANCE_RATE_CYCLE_RESERVE","raw_component_scores_before":{"roe_ifrs17_score":8,"reserve_quality_score":1,"rate_cycle_score":4,"capital_return_score":2,"relative_strength_score":12,"solvency_risk_penalty":8},"weighted_score_before":62,"stage_label_before":"Stage2-Actionable","raw_component_scores_after":{"roe_ifrs17_score":4,"reserve_quality_score":0,"rate_cycle_score":2,"capital_return_score":0,"relative_strength_score":5,"solvency_risk_penalty":14},"weighted_score_after":42,"stage_label_after":"Stage1-Watch","changed_components":["roe_ifrs17_score","reserve_quality_score","rate_cycle_score","capital_return_score","relative_strength_score","solvency_risk_penalty"],"component_delta_explanation":"C22 guard demotes small-insurer value-up price spikes when reserve/solvency/capital-return bridge is absent.","MFE_90D_pct":25.0,"MAE_90D_pct":-28.69,"score_return_alignment_label":"score_return_misaligned","current_profile_verdict":"current_profile_false_positive"}
```

### 20.5 shadow_weight rows

```csv
row_type,axis,scope,large_sector_id,canonical_archetype_id,baseline_value,tested_value,delta,reason,backtest_effect,trigger_ids,calibration_usable_count,new_independent_case_count,counterexample_count,confidence,proposal_type,notes
shadow_weight,c22_requires_reserve_solvency_capital_return_bridge,canonical_archetype_specific,L6_FINANCIAL_CAPITAL_RETURN_DIGITAL,C22_INSURANCE_RATE_CYCLE_RESERVE,0,1,+1,"C22 insurance rows should not promote toward Stage3-Yellow/Green unless IFRS17/ROE/rate-cycle signal converts into reserve quality, solvency buffer, and capital-return bridge","000370 and 003690 survive with cleaner MFE/MAE; 000540 fails when small-insurer value-up theme lacks reserve/solvency bridge","TRG_R6L72_C22_000370_20240129_SMALL_PNC_ROE_VALUEUP_BRIDGE|TRG_R6L72_C22_003690_20240124_REINSURANCE_RATE_CYCLE_STABLE_BRIDGE|TRG_R6L72_C22_000540_20240213_SMALL_INSURER_PRICE_VALUEUP_BLOWOFF",3,3,1,medium,canonical_shadow_only,"not production; post-calibrated residual"
shadow_weight,c22_small_insurer_price_blowoff_high_mae_watch_guard,canonical_archetype_specific,L6_FINANCIAL_CAPITAL_RETURN_DIGITAL,C22_INSURANCE_RATE_CYCLE_RESERVE,1,1,0,"Small insurer value-up rows can peak before reserve/solvency/capital-return evidence is confirmed; local 4B/high-MAE watch should remain active","preserves 000370/003690 positives while preventing 000540 price-only false positive","TRG_R6L72_C22_000370_20240129_SMALL_PNC_ROE_VALUEUP_BRIDGE|TRG_R6L72_C22_003690_20240124_REINSURANCE_RATE_CYCLE_STABLE_BRIDGE|TRG_R6L72_C22_000540_20240213_SMALL_INSURER_PRICE_VALUEUP_BLOWOFF",3,3,1,medium,existing_axis_kept,"strengthens local 4B/high-MAE watch without global delta"
```

### 20.6 residual_contribution row

```jsonl
{"row_type":"residual_contribution","round":"R6","loop":"72","large_sector_id":"L6_FINANCIAL_CAPITAL_RETURN_DIGITAL","canonical_archetype_id":"C22_INSURANCE_RATE_CYCLE_RESERVE","new_independent_case_count":3,"reused_case_count":0,"new_symbol_count":3,"new_trigger_family_count":3,"tested_existing_calibrated_axes":["stage2_actionable_evidence_bonus","price_only_blowoff_blocks_positive_stage","full_4b_requires_non_price_evidence","local_4b_watch_guard","high_MAE_guardrail"],"residual_error_types_found":["small_insurer_valueup_without_reserve_solvency_bridge","insurance_rate_cycle_winner_needs_4B_watch","price_blowoff_high_MAE_after_theme_stage2"],"loop_contribution_label":"canonical_archetype_rule_candidate","do_not_propose_new_weight_delta":false}
```

## 21. Deferred Coding Agent Handoff Prompt

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

## 22. Next Round State

```text
completed_round = R6
completed_loop = 72
next_round = R7
next_loop = 72
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
atlas/symbol_profiles/000/000370.json
atlas/symbol_profiles/003/003690.json
atlas/symbol_profiles/000/000540.json
atlas/ohlcv_tradable_by_symbol_year/000/000370/2024.csv
atlas/ohlcv_tradable_by_symbol_year/003/003690/2024.csv
atlas/ohlcv_tradable_by_symbol_year/000/000540/2024.csv
```

This loop adds 3 new independent C22 cases, 2 positives, 1 counterexample, and 1 canonical-archetype residual guard candidate for R6/L6.
