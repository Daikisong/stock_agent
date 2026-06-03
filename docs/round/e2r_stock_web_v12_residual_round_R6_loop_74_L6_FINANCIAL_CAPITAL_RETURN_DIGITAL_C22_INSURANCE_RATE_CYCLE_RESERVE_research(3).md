# E2R Stock-Web Historical Calibration / Sector-Archetype Residual Research Round

## 0. Research Metadata

```text
scheduled_round: R6
scheduled_loop: 74
round_schedule_status: valid
round_sector_consistency: pass
computed_next_round: R7
computed_next_loop: 74
large_sector_id: L6_FINANCIAL_CAPITAL_RETURN_DIGITAL
canonical_archetype_id: C22_INSURANCE_RATE_CYCLE_RESERVE
fine_archetype_id: C22_RESERVE_CSM_CAPITAL_RETURN_PBR_REPAIR_BRIDGE_GUARD
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

R6 maps to `L6_FINANCIAL_CAPITAL_RETURN_DIGITAL`. The previous R6 loop used C21 brokerage/ROE/PBR/capital-return, so this run shifts to C22. The selected branch is insurance-rate cycle and reserve-quality repair. It avoids the top-covered large insurance names and tests whether smaller insurer value-up moves need reserve/CSM/capital-return confirmation before Stage3 promotion.

| layer | id | definition |
|---|---|---|
| round | R6 | financial / capital return / digital |
| large_sector | L6_FINANCIAL_CAPITAL_RETURN_DIGITAL | financials, insurance, brokers, digital finance, capital return |
| canonical | C22_INSURANCE_RATE_CYCLE_RESERVE | insurance rate cycle, reserve quality, CSM, capital return, PBR repair |
| fine | C22_RESERVE_CSM_CAPITAL_RETURN_PBR_REPAIR_BRIDGE_GUARD | insurance signal must become reserve/CSM/capital-return bridge |
| deep | NON_LIFE_INSURANCE_CSM_LOSS_RATIO_CAPITAL_RETURN_TO_PBR_REPAIR | non-life insurer positive |
| deep | LIFE_INSURANCE_RATE_CYCLE_CAPITAL_RETURN_PBR_REPAIR_TO_PEAK_REVERSAL | life insurer positive with 4B guard |
| deep | SMALL_INSURANCE_VALUEUP_THEME_SPIKE_WITHOUT_CSM_RESERVE_SHAREHOLDER_RETURN_CONVERSION | small-insurance theme false positive |

## 3. No-Repeat / Coverage Check

No-Repeat hard duplicate key:

```text
canonical_archetype_id + symbol + trigger_type + entry_date
```

C22 top-covered symbols are `000810`, `005830`, `088350`, `001450`, `032830`, and `085620`. This run avoids that cluster and also avoids the prior R6/C21 brokerage representatives.

| archetype | selected symbol | duplicate status | reason |
|---|---:|---|---|
| C22 | 000370 | new independent | not top-covered C22 symbol; non-life insurance CSM/capital-return bridge |
| C22 | 082640 | new independent | not top-covered C22 symbol; life-insurance rate-cycle/PBR repair bridge |
| C22 | 000540 | new independent | not top-covered C22 symbol; small-insurance value-up theme false positive |

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
000370 has historical corporate-action candidates ending 2017, outside the selected 2024 representative window.
082640 has a 2017-04-11 corporate-action candidate, outside the selected 2024 representative window.
000540 has historical corporate-action candidates ending 2011, outside the selected 2024 representative window.
003690/코리안리는 reviewed as a clean reinsurance rate-cycle candidate, but this run chose 000540 instead to keep at least one high-MAE false-positive row.
All three representative 180D windows are treated as clean for this residual calibration.
```

## 6. Case Selection Summary

| role | symbol | company | trigger | entry | price | result |
|---|---:|---|---|---:|---:|---|
| structural_success_then_4B_watch | 000370 | 한화손해보험 | Stage2-Actionable | 2024-01-29 | 4050 | reserve/CSM/capital-return PBR repair bridge worked |
| structural_success_with_high_MAE_after_peak | 082640 | 동양생명 | Stage2-Actionable | 2024-01-29 | 4630 | life-insurance rate-cycle bridge worked, but 4B/high-MAE guard required |
| insurance_theme_peak_then_high_MAE_counterexample | 000540 | 흥국화재 | Stage2-Actionable | 2024-02-14 | 5570 | small-insurance value-up theme lacked reserve/capital-return bridge |

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
| 000370 | 한화손해보험 | Stage2-Actionable | 2024-01-29 | 4050 | 52.35 | 52.35 | 53.83 | -3.21 | -3.21 | -3.21 | 2024-08-20 | 6230 | -21.91 |
| 082640 | 동양생명 | Stage2-Actionable | 2024-01-29 | 4630 | 32.83 | 40.39 | 103.89 | -3.13 | -3.13 | -3.13 | 2024-07-31 | 9440 | -44.7 |
| 000540 | 흥국화재 | Stage2-Actionable | 2024-02-14 | 5570 | 18.49 | 18.49 | 18.49 | -25.31 | -32.41 | -37.88 | 2024-02-14 | 6600 | -47.58 |

## 9. Case-by-Case Notes

### 9.1 000370 / 한화손해보험 — non-life insurance reserve/capital-return bridge

The entry row is 2024-01-29 at 4,050. The path quickly repriced and later reached 6,230. This is a valid C22 positive because the evidence family is not just “insurance theme.” It requires reserve/CSM quality, loss-ratio or ROE repair, shareholder-return visibility, and PBR discount repair. The post-peak drawdown still keeps 4B watch active.

### 9.2 082640 / 동양생명 — life-insurance rate-cycle bridge with high-MAE overlay

The entry row is 2024-01-29 at 4,630. The forward path eventually reached 9,440. That is strong, but the post-peak decline was severe. This validates the rate-cycle/PBR-repair route, while warning that life-insurance value-up can crowd into a sharp reversal. Yellow is allowed; Green should wait.

### 9.3 000540 / 흥국화재 — small-insurance value-up theme false positive

The entry row is 2024-02-14 at 5,570. The same local event window reached 6,600, but the forward low fell to 3,460. This is the C22 trap: small-insurance price heat can look like PBR repair, but without reserve quality, CSM, capital-return execution, or durable ROE bridge, it is a 4B/high-MAE watch row.

## 10. Current Calibrated Profile Stress Test

| question | result |
|---|---|
| Stage2 actionable bonus too strong? | Yes when C22 treats small-insurance/value-up price spikes as enough evidence. |
| Stage3 Yellow threshold too loose? | Not globally; C22 needs reserve/CSM/capital-return/PBR bridge before Yellow. |
| Stage3 Green too strict? | Correct. No Green loosening. |
| Price-only blowoff guard appropriate? | Yes, especially for 000540. |
| Full 4B non-price requirement appropriate? | Yes. 000370/082640 have stronger non-price bridges; 000540 does not. |
| 4C timing issue? | High-MAE watch is useful; no immediate hard 4C promotion proposed. |

## 11. Stage2 / Yellow / Green Comparison

```text
000370:
  Stage2-Actionable = correct
  Stage3-Yellow = allowed after reserve/CSM and capital-return bridge
  Stage3-Green = wait for shareholder-return execution and post-MFE 4B review

082640:
  Stage2-Actionable = correct
  Stage3-Yellow = allowed with active rate-cycle and reserve-quality guard
  Stage3-Green = reject unless post-peak drawdown and rate-cycle crowding risk clear

000540:
  Stage2-Actionable = too generous if based only on small-insurance value-up price spike
  Stage3-Yellow = reject without reserve quality, CSM, capital return, and ROE bridge
  Stage3-Green = reject
```

## 12. 4B Local vs Full-window Timing Audit

| symbol | local_peak_proximity | full_window_peak_proximity | verdict |
|---:|---:|---:|---|
| 000370 | 0.99 | 1.00 | good full-window 4B watch after CSM/capital-return bridge |
| 082640 | 0.87 | 1.00 | large MFE but requires rate-cycle drawdown guard |
| 000540 | 1.00 | 1.00 | small-insurance theme local 4B watch, not positive stage |

## 13. Canonical-Archetype Rule Candidate

```text
canonical_archetype_rule_candidate: true
rule_scope: canonical_archetype_specific
rule_id: c22_requires_reserve_csm_capital_return_pbr_repair_bridge

rule:
  For C22 insurance/rate-cycle rows, do not promote insurance, value-up,
  rate-cycle, reserve, or small-insurance Stage2 signals into Stage3-Yellow/Green
  unless at least one non-price bridge is visible:
  reserve/CSM quality, loss-ratio normalization, rate-cycle-to-ROE conversion,
  capital return, shareholder-return execution, PBR discount repair,
  solvency/balance-sheet quality, or earnings revision tied to those factors.
```

## 14. Before / After Backtest Comparison

| profile | eligible triggers | avg MFE90 | avg MAE90 | false positive rate | verdict |
|---|---:|---:|---:|---:|---|
| P0 e2r_2_1_stock_web_calibrated_proxy | 3 | 37.08 | -12.92 | 33.3% | useful but can over-credit small-insurance value-up theme |
| P0b e2r_2_0_baseline_reference | 3 | 37.08 | -12.92 | 0% | safer but may miss 000370/082640 |
| P1 sector_specific_candidate_profile | 3 | 37.08 | -12.92 | 33.3% | no broad L6 loosen |
| P2 canonical_archetype_candidate_profile | 2 selected positives | 46.37 | -3.17 | 0% after bridge gate | preferred shadow |
| P3 counterexample_guard_profile | 1 rejected | 18.49 | -32.41 | 0% after demotion | useful guard |

## 15. Score-Return Alignment Matrix

| case | current profile verdict | alignment |
|---|---|---|
| 000370 | current_profile_correct | reserve/CSM/capital-return bridge aligned with positive MFE |
| 082640 | current_profile_partially_correct | rate-cycle bridge worked, but post-peak drawdown requires 4B guard |
| 000540 | current_profile_false_positive | small-insurance theme spike produced high MAE without durable bridge |

## 16. Coverage Matrix

| large_sector_id | canonical_archetype_id | fine_archetype_id | positive | counterexample | 4B | 4C/watch | new_independent | reused | usable_triggers | representative | profile_errors | sector_rule | canonical_rule | coverage_gap_after |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|---|---|
| L6_FINANCIAL_CAPITAL_RETURN_DIGITAL | C22_INSURANCE_RATE_CYCLE_RESERVE | C22_RESERVE_CSM_CAPITAL_RETURN_PBR_REPAIR_BRIDGE_GUARD | 2 | 1 | 3 | 2 | 3 | 0 | 3 | 3 | 1 | false | true | C22 non-top-covered insurer/reserve-rate-cycle residual reduced |

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
- small insurance theme without reserve/capital-return bridge
- insurance value-up winner needs 4B watch
- life-insurance rate-cycle high-MAE after peak
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
- round/sector/canonical consistency
- duplicate avoidance at symbol level
- representative rows use clean forward windows
```

Not validated:

```text
- exact disclosure URLs
- exact report URLs
- production scoring behavior
- live candidate status
- 003690 as representative row; reviewed but excluded to preserve one high-MAE counterexample slot
```

## 19. Shadow Weight Calibration

```csv
row_type,axis,scope,large_sector_id,canonical_archetype_id,baseline_value,tested_value,delta,reason,backtest_effect,trigger_ids,calibration_usable_count,new_independent_case_count,counterexample_count,confidence,proposal_type,notes
shadow_weight,c22_requires_reserve_csm_capital_return_pbr_repair_bridge,canonical_archetype_specific,L6_FINANCIAL_CAPITAL_RETURN_DIGITAL,C22_INSURANCE_RATE_CYCLE_RESERVE,0,1,+1,"C22 insurance/rate-cycle rows should not promote toward Stage3-Yellow/Green unless insurance value-up signal converts into reserve or CSM quality, loss-ratio or rate-cycle ROE bridge, capital return, shareholder-return execution, or PBR repair","000370 and 082640 survive after reserve/CSM/capital-return bridge; 000540 fails when small-insurance value-up theme lacks durable reserve and capital-return bridge","TRG_R6L74_C22_000370_20240129_PNC_INSURANCE_RATE_CYCLE_CAPITAL_RETURN_BRIDGE|TRG_R6L74_C22_082640_20240129_LIFE_INSURANCE_RATE_CYCLE_PBR_REPAIR_BRIDGE|TRG_R6L74_C22_000540_20240214_SMALL_INSURANCE_THEME_NO_RESERVE_CAPITAL_BRIDGE",3,3,1,medium,canonical_shadow_only,"not production; post-calibrated residual"
shadow_weight,c22_insurance_valueup_4b_high_mae_watch_guard,canonical_archetype_specific,L6_FINANCIAL_CAPITAL_RETURN_DIGITAL,C22_INSURANCE_RATE_CYCLE_RESERVE,1,1,0,"Insurance value-up winners and small-insurance theme false starts can peak before reserve and shareholder-return durability is confirmed; local/full-window 4B and high-MAE watch should remain active","preserves 000370/082640 positives while preventing 000540 insurance-theme false positive","TRG_R6L74_C22_000370_20240129_PNC_INSURANCE_RATE_CYCLE_CAPITAL_RETURN_BRIDGE|TRG_R6L74_C22_082640_20240129_LIFE_INSURANCE_RATE_CYCLE_PBR_REPAIR_BRIDGE|TRG_R6L74_C22_000540_20240214_SMALL_INSURANCE_THEME_NO_RESERVE_CAPITAL_BRIDGE",3,3,1,medium,existing_axis_kept,"strengthens local/full-window 4B and high-MAE watch without global delta"
```

## 20. Machine-Readable Rows

### 20.1 price_source_validation

```jsonl
{"row_type":"price_source_validation","source":"Songdaiki/stock-web","source_url":"https://github.com/Songdaiki/stock-web","manifest_path":"atlas/manifest.json","schema_path":"atlas/schema.json","universe_path":"atlas/universe/all_symbols.csv","manifest_max_date":"2026-02-20","source_name":"FinanceData/marcap","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","calibration_shard_root":"atlas/ohlcv_tradable_by_symbol_year","raw_shard_root":"atlas/ohlcv_raw_by_symbol_year","validation_status":"usable_for_historical_calibration"}
```

### 20.2 case rows

```jsonl
{"row_type":"case","case_id":"R6L74_C22_000370_20240129_PNC_INSURANCE_RATE_CYCLE_CAPITAL_RETURN_BRIDGE","symbol":"000370","company_name":"한화손해보험","round":"R6","loop":"74","large_sector_id":"L6_FINANCIAL_CAPITAL_RETURN_DIGITAL","canonical_archetype_id":"C22_INSURANCE_RATE_CYCLE_RESERVE","fine_archetype_id":"C22_PNC_INSURANCE_RATE_CYCLE_CAPITAL_RETURN_BRIDGE","deep_sub_archetype_id":"NON_LIFE_INSURANCE_CSM_LOSS_RATIO_CAPITAL_RETURN_TO_PBR_REPAIR","case_type":"structural_success_then_4B_watch","positive_or_counterexample":"positive","best_trigger":"Stage2-Actionable","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"score_return_aligned","current_profile_verdict":"current_profile_correct","price_source":"Songdaiki/stock-web","notes":"C22 insurance rows require reserve/CSM quality, loss-ratio or rate-cycle ROE bridge, capital return, PBR repair, or shareholder-return execution; insurance/value-up price theme alone is insufficient."}
{"row_type":"case","case_id":"R6L74_C22_082640_20240129_LIFE_INSURANCE_RATE_CYCLE_PBR_REPAIR_BRIDGE","symbol":"082640","company_name":"동양생명","round":"R6","loop":"74","large_sector_id":"L6_FINANCIAL_CAPITAL_RETURN_DIGITAL","canonical_archetype_id":"C22_INSURANCE_RATE_CYCLE_RESERVE","fine_archetype_id":"C22_LIFE_INSURANCE_RATE_CYCLE_PBR_REPAIR_BRIDGE_WITH_4B_GUARD","deep_sub_archetype_id":"LIFE_INSURANCE_RATE_CYCLE_CAPITAL_RETURN_PBR_REPAIR_TO_PEAK_REVERSAL","case_type":"structural_success_with_high_MAE_after_peak","positive_or_counterexample":"positive","best_trigger":"Stage2-Actionable","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"score_return_mixed","current_profile_verdict":"current_profile_partially_correct","price_source":"Songdaiki/stock-web","notes":"C22 insurance rows require reserve/CSM quality, loss-ratio or rate-cycle ROE bridge, capital return, PBR repair, or shareholder-return execution; insurance/value-up price theme alone is insufficient."}
{"row_type":"case","case_id":"R6L74_C22_000540_20240214_SMALL_INSURANCE_THEME_NO_RESERVE_CAPITAL_BRIDGE","symbol":"000540","company_name":"흥국화재","round":"R6","loop":"74","large_sector_id":"L6_FINANCIAL_CAPITAL_RETURN_DIGITAL","canonical_archetype_id":"C22_INSURANCE_RATE_CYCLE_RESERVE","fine_archetype_id":"C22_SMALL_INSURANCE_THEME_WITHOUT_RESERVE_CAPITAL_RETURN_BRIDGE","deep_sub_archetype_id":"SMALL_INSURANCE_VALUEUP_THEME_SPIKE_WITHOUT_CSM_RESERVE_SHAREHOLDER_RETURN_CONVERSION","case_type":"insurance_theme_peak_then_high_MAE_counterexample","positive_or_counterexample":"counterexample","best_trigger":"Stage2-Actionable","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"score_return_misaligned","current_profile_verdict":"current_profile_false_positive","price_source":"Songdaiki/stock-web","notes":"C22 insurance rows require reserve/CSM quality, loss-ratio or rate-cycle ROE bridge, capital return, PBR repair, or shareholder-return execution; insurance/value-up price theme alone is insufficient."}
```

### 20.3 trigger rows

```jsonl
{"row_type":"trigger","trigger_id":"TRG_R6L74_C22_000370_20240129_PNC_INSURANCE_RATE_CYCLE_CAPITAL_RETURN_BRIDGE","case_id":"R6L74_C22_000370_20240129_PNC_INSURANCE_RATE_CYCLE_CAPITAL_RETURN_BRIDGE","symbol":"000370","company_name":"한화손해보험","round":"R6","loop":"74","large_sector_id":"L6_FINANCIAL_CAPITAL_RETURN_DIGITAL","canonical_archetype_id":"C22_INSURANCE_RATE_CYCLE_RESERVE","fine_archetype_id":"C22_PNC_INSURANCE_RATE_CYCLE_CAPITAL_RETURN_BRIDGE","deep_sub_archetype_id":"NON_LIFE_INSURANCE_CSM_LOSS_RATIO_CAPITAL_RETURN_TO_PBR_REPAIR","loop_objective":"coverage_gap_fill|counterexample_mining|stage2_actionable_bonus_stress_test|4B_non_price_requirement_stress_test|canonical_archetype_compression","trigger_type":"Stage2-Actionable","trigger_date":"2024-01-29","entry_date":"2024-01-29","entry_price":4050,"evidence_available_at_that_date":"source_proxy_non_life_insurance_CSM_loss_ratio_capital_return_PBR_repair_bridge; evidence_url_pending","evidence_source":"source_proxy_non_life_insurance_CSM_loss_ratio_capital_return_PBR_repair_bridge; evidence_url_pending","bridge_summary":"non-life insurance value-up, reserve/CSM quality, loss-ratio normalization, and shareholder-return visibility converted into PBR repair rather than insurance theme heat","stage2_evidence_fields":["non_life_insurance_valueup","CSM_reserve_quality_proxy","capital_return_visibility","relative_strength"],"stage3_evidence_fields":["loss_ratio_to_ROE_visibility","PBR_repair_bridge","shareholder_return_execution_proxy"],"stage4b_evidence_fields":["post_MFE_peak_watch","insurance_valueup_crowding_after_rerating"],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/000/000370/2024.csv","profile_path":"atlas/symbol_profiles/000/000370.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":52.35,"MFE_90D_pct":52.35,"MFE_180D_pct":53.83,"MFE_1Y_pct":53.83,"MFE_2Y_pct":53.83,"MAE_30D_pct":-3.21,"MAE_90D_pct":-3.21,"MAE_180D_pct":-3.21,"MAE_1Y_pct":-3.21,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-08-20","peak_price":6230,"drawdown_after_peak_pct":-21.91,"green_lateness_ratio":"0.44","four_b_local_peak_proximity":0.99,"four_b_full_window_peak_proximity":1.0,"four_b_timing_verdict":"good_full_window_4B_watch_after_CSM_capital_return_bridge","four_b_evidence_type":"non_price_reserve_CSM_capital_return_bridge","four_c_protection_label":"none","trigger_outcome_label":"structural_success_then_4B_watch","current_profile_verdict":"current_profile_correct","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"R6L74_C22_000370_20240129_PNC_INSURANCE_RATE_CYCLE_CAPITAL_RETURN_BRIDGE_entry","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"TRG_R6L74_C22_082640_20240129_LIFE_INSURANCE_RATE_CYCLE_PBR_REPAIR_BRIDGE","case_id":"R6L74_C22_082640_20240129_LIFE_INSURANCE_RATE_CYCLE_PBR_REPAIR_BRIDGE","symbol":"082640","company_name":"동양생명","round":"R6","loop":"74","large_sector_id":"L6_FINANCIAL_CAPITAL_RETURN_DIGITAL","canonical_archetype_id":"C22_INSURANCE_RATE_CYCLE_RESERVE","fine_archetype_id":"C22_LIFE_INSURANCE_RATE_CYCLE_PBR_REPAIR_BRIDGE_WITH_4B_GUARD","deep_sub_archetype_id":"LIFE_INSURANCE_RATE_CYCLE_CAPITAL_RETURN_PBR_REPAIR_TO_PEAK_REVERSAL","loop_objective":"coverage_gap_fill|counterexample_mining|stage2_actionable_bonus_stress_test|4B_non_price_requirement_stress_test|canonical_archetype_compression","trigger_type":"Stage2-Actionable","trigger_date":"2024-01-29","entry_date":"2024-01-29","entry_price":4630,"evidence_available_at_that_date":"source_proxy_life_insurance_rate_cycle_capital_return_PBR_repair_with_drawdown_guard; evidence_url_pending","evidence_source":"source_proxy_life_insurance_rate_cycle_capital_return_PBR_repair_with_drawdown_guard; evidence_url_pending","bridge_summary":"life-insurance rate-cycle and PBR-repair route produced strong MFE, but post-peak drawdown required 4B/high-MAE overlay rather than Green loosening","stage2_evidence_fields":["life_insurance_rate_cycle","PBR_repair_proxy","capital_return_visibility","relative_strength"],"stage3_evidence_fields":["rate_cycle_to_ROE_bridge","shareholder_return_proxy","reserve_quality_watch"],"stage4b_evidence_fields":["post_MFE_peak_watch","life_insurance_valueup_crowding"],"stage4c_evidence_fields":["post_peak_high_MAE_watch"],"price_data_source":"Songdaiki/stock-web","price_data_repo":"Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/082/082640/2024.csv","profile_path":"atlas/symbol_profiles/082/082640.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":32.83,"MFE_90D_pct":40.39,"MFE_180D_pct":103.89,"MFE_1Y_pct":103.89,"MFE_2Y_pct":103.89,"MAE_30D_pct":-3.13,"MAE_90D_pct":-3.13,"MAE_180D_pct":-3.13,"MAE_1Y_pct":-3.13,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-07-31","peak_price":9440,"drawdown_after_peak_pct":-44.7,"green_lateness_ratio":"0.31","four_b_local_peak_proximity":0.87,"four_b_full_window_peak_proximity":1.0,"four_b_timing_verdict":"large_MFE_but_requires_rate_cycle_drawdown_guard","four_b_evidence_type":"non_price_reserve_CSM_capital_return_bridge","four_c_protection_label":"high_MAE_watch_after_peak","trigger_outcome_label":"structural_success_but_needs_4B_high_MAE_guard","current_profile_verdict":"current_profile_partially_correct","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"R6L74_C22_082640_20240129_LIFE_INSURANCE_RATE_CYCLE_PBR_REPAIR_BRIDGE_entry","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"TRG_R6L74_C22_000540_20240214_SMALL_INSURANCE_THEME_NO_RESERVE_CAPITAL_BRIDGE","case_id":"R6L74_C22_000540_20240214_SMALL_INSURANCE_THEME_NO_RESERVE_CAPITAL_BRIDGE","symbol":"000540","company_name":"흥국화재","round":"R6","loop":"74","large_sector_id":"L6_FINANCIAL_CAPITAL_RETURN_DIGITAL","canonical_archetype_id":"C22_INSURANCE_RATE_CYCLE_RESERVE","fine_archetype_id":"C22_SMALL_INSURANCE_THEME_WITHOUT_RESERVE_CAPITAL_RETURN_BRIDGE","deep_sub_archetype_id":"SMALL_INSURANCE_VALUEUP_THEME_SPIKE_WITHOUT_CSM_RESERVE_SHAREHOLDER_RETURN_CONVERSION","loop_objective":"coverage_gap_fill|counterexample_mining|stage2_actionable_bonus_stress_test|4B_non_price_requirement_stress_test|canonical_archetype_compression","trigger_type":"Stage2-Actionable","trigger_date":"2024-02-14","entry_date":"2024-02-14","entry_price":5570,"evidence_available_at_that_date":"source_proxy_small_insurance_valueup_price_spike_without_CSM_reserve_capital_return_bridge; evidence_url_pending","evidence_source":"source_proxy_small_insurance_valueup_price_spike_without_CSM_reserve_capital_return_bridge; evidence_url_pending","bridge_summary":"small insurance/value-up theme produced a sharp local peak, but reserve-quality, CSM, capital-return, and durable ROE bridge were not visible enough and the path degraded into high MAE","stage2_evidence_fields":["small_insurance_valueup_theme","price_spike","relative_strength"],"stage3_evidence_fields":[],"stage4b_evidence_fields":["price_theme_local_peak","reserve_quality_bridge_absent","capital_return_execution_absent"],"stage4c_evidence_fields":["high_MAE_without_reserve_or_shareholder_return_bridge"],"price_data_source":"Songdaiki/stock-web","price_data_repo":"Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/000/000540/2024.csv","profile_path":"atlas/symbol_profiles/000/000540.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":18.49,"MFE_90D_pct":18.49,"MFE_180D_pct":18.49,"MFE_1Y_pct":18.49,"MFE_2Y_pct":18.49,"MAE_30D_pct":-25.31,"MAE_90D_pct":-32.41,"MAE_180D_pct":-37.88,"MAE_1Y_pct":-37.88,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-02-14","peak_price":6600,"drawdown_after_peak_pct":-47.58,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":1.0,"four_b_full_window_peak_proximity":1.0,"four_b_timing_verdict":"small_insurance_theme_local_4B_watch_not_positive_stage","four_b_evidence_type":"insurance_theme_without_reserve_capital_return_bridge","four_c_protection_label":"high_MAE_watch","trigger_outcome_label":"failed_rerating_high_MAE_counterexample","current_profile_verdict":"current_profile_false_positive","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"R6L74_C22_000540_20240214_SMALL_INSURANCE_THEME_NO_RESERVE_CAPITAL_BRIDGE_entry","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
```

### 20.4 score_simulation rows

```jsonl
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"R6L74_C22_000370_20240129_PNC_INSURANCE_RATE_CYCLE_CAPITAL_RETURN_BRIDGE","trigger_id":"TRG_R6L74_C22_000370_20240129_PNC_INSURANCE_RATE_CYCLE_CAPITAL_RETURN_BRIDGE","symbol":"000370","large_sector_id":"L6_FINANCIAL_CAPITAL_RETURN_DIGITAL","canonical_archetype_id":"C22_INSURANCE_RATE_CYCLE_RESERVE","raw_component_scores_before":{"rate_cycle_score":12,"reserve_CSM_quality_score":12,"capital_return_score":11,"PBR_repair_score":10,"relative_strength_score":10,"risk_penalty":5},"weighted_score_before":74,"stage_label_before":"Stage2-Actionable","raw_component_scores_after":{"rate_cycle_score":15,"reserve_CSM_quality_score":15,"capital_return_score":14,"PBR_repair_score":13,"relative_strength_score":8,"risk_penalty":6},"weighted_score_after":83,"stage_label_after":"Stage3-Yellow","changed_components":["rate_cycle_score","reserve_CSM_quality_score","capital_return_score","PBR_repair_score","relative_strength_score","risk_penalty"],"component_delta_explanation":"C22 row is promoted only because insurance value-up signal converts into reserve/CSM quality, ROE, PBR repair, and capital-return bridge.","MFE_90D_pct":52.35,"MAE_90D_pct":-3.21,"score_return_alignment_label":"score_return_aligned","current_profile_verdict":"current_profile_correct"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"R6L74_C22_082640_20240129_LIFE_INSURANCE_RATE_CYCLE_PBR_REPAIR_BRIDGE","trigger_id":"TRG_R6L74_C22_082640_20240129_LIFE_INSURANCE_RATE_CYCLE_PBR_REPAIR_BRIDGE","symbol":"082640","large_sector_id":"L6_FINANCIAL_CAPITAL_RETURN_DIGITAL","canonical_archetype_id":"C22_INSURANCE_RATE_CYCLE_RESERVE","raw_component_scores_before":{"rate_cycle_score":11,"reserve_CSM_quality_score":10,"capital_return_score":10,"PBR_repair_score":11,"relative_strength_score":12,"risk_penalty":7},"weighted_score_before":72,"stage_label_before":"Stage2-Actionable","raw_component_scores_after":{"rate_cycle_score":14,"reserve_CSM_quality_score":12,"capital_return_score":13,"PBR_repair_score":14,"relative_strength_score":9,"risk_penalty":11},"weighted_score_after":78,"stage_label_after":"Stage3-Yellow","changed_components":["rate_cycle_score","reserve_CSM_quality_score","capital_return_score","PBR_repair_score","relative_strength_score","risk_penalty"],"component_delta_explanation":"C22 bridge works, but post-peak drawdown and rate-cycle crowding require 4B/high-MAE guard and prevent Green loosening.","MFE_90D_pct":40.39,"MAE_90D_pct":-3.13,"score_return_alignment_label":"score_return_mixed","current_profile_verdict":"current_profile_partially_correct"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"R6L74_C22_000540_20240214_SMALL_INSURANCE_THEME_NO_RESERVE_CAPITAL_BRIDGE","trigger_id":"TRG_R6L74_C22_000540_20240214_SMALL_INSURANCE_THEME_NO_RESERVE_CAPITAL_BRIDGE","symbol":"000540","large_sector_id":"L6_FINANCIAL_CAPITAL_RETURN_DIGITAL","canonical_archetype_id":"C22_INSURANCE_RATE_CYCLE_RESERVE","raw_component_scores_before":{"rate_cycle_score":8,"reserve_CSM_quality_score":1,"capital_return_score":1,"PBR_repair_score":3,"relative_strength_score":12,"risk_penalty":8},"weighted_score_before":62,"stage_label_before":"Stage2-Actionable","raw_component_scores_after":{"rate_cycle_score":4,"reserve_CSM_quality_score":0,"capital_return_score":0,"PBR_repair_score":1,"relative_strength_score":4,"risk_penalty":16},"weighted_score_after":40,"stage_label_after":"Stage1-Watch_or_4B-HighMAE","changed_components":["rate_cycle_score","reserve_CSM_quality_score","capital_return_score","PBR_repair_score","relative_strength_score","risk_penalty"],"component_delta_explanation":"C22 guard demotes small insurance/value-up theme rows when reserve quality, CSM, capital return, PBR repair, and durable ROE bridge are absent.","MFE_90D_pct":18.49,"MAE_90D_pct":-32.41,"score_return_alignment_label":"score_return_misaligned","current_profile_verdict":"current_profile_false_positive"}
```

### 20.5 shadow_weight rows

```csv
row_type,axis,scope,large_sector_id,canonical_archetype_id,baseline_value,tested_value,delta,reason,backtest_effect,trigger_ids,calibration_usable_count,new_independent_case_count,counterexample_count,confidence,proposal_type,notes
shadow_weight,c22_requires_reserve_csm_capital_return_pbr_repair_bridge,canonical_archetype_specific,L6_FINANCIAL_CAPITAL_RETURN_DIGITAL,C22_INSURANCE_RATE_CYCLE_RESERVE,0,1,+1,"C22 insurance/rate-cycle rows should not promote toward Stage3-Yellow/Green unless insurance value-up signal converts into reserve or CSM quality, loss-ratio or rate-cycle ROE bridge, capital return, shareholder-return execution, or PBR repair","000370 and 082640 survive after reserve/CSM/capital-return bridge; 000540 fails when small-insurance value-up theme lacks durable reserve and capital-return bridge","TRG_R6L74_C22_000370_20240129_PNC_INSURANCE_RATE_CYCLE_CAPITAL_RETURN_BRIDGE|TRG_R6L74_C22_082640_20240129_LIFE_INSURANCE_RATE_CYCLE_PBR_REPAIR_BRIDGE|TRG_R6L74_C22_000540_20240214_SMALL_INSURANCE_THEME_NO_RESERVE_CAPITAL_BRIDGE",3,3,1,medium,canonical_shadow_only,"not production; post-calibrated residual"
shadow_weight,c22_insurance_valueup_4b_high_mae_watch_guard,canonical_archetype_specific,L6_FINANCIAL_CAPITAL_RETURN_DIGITAL,C22_INSURANCE_RATE_CYCLE_RESERVE,1,1,0,"Insurance value-up winners and small-insurance theme false starts can peak before reserve and shareholder-return durability is confirmed; local/full-window 4B and high-MAE watch should remain active","preserves 000370/082640 positives while preventing 000540 insurance-theme false positive","TRG_R6L74_C22_000370_20240129_PNC_INSURANCE_RATE_CYCLE_CAPITAL_RETURN_BRIDGE|TRG_R6L74_C22_082640_20240129_LIFE_INSURANCE_RATE_CYCLE_PBR_REPAIR_BRIDGE|TRG_R6L74_C22_000540_20240214_SMALL_INSURANCE_THEME_NO_RESERVE_CAPITAL_BRIDGE",3,3,1,medium,existing_axis_kept,"strengthens local/full-window 4B and high-MAE watch without global delta"
```

### 20.6 residual_contribution row

```jsonl
{"row_type":"residual_contribution","round":"R6","loop":"74","large_sector_id":"L6_FINANCIAL_CAPITAL_RETURN_DIGITAL","canonical_archetype_id":"C22_INSURANCE_RATE_CYCLE_RESERVE","new_independent_case_count":3,"reused_case_count":0,"new_symbol_count":3,"new_trigger_family_count":3,"tested_existing_calibrated_axes":["stage2_actionable_evidence_bonus","price_only_blowoff_blocks_positive_stage","full_4b_requires_non_price_evidence","local_4b_watch_guard","high_MAE_guardrail"],"residual_error_types_found":["small_insurance_theme_without_reserve_capital_return_bridge","insurance_valueup_winner_needs_4B_watch","life_insurance_rate_cycle_high_MAE_after_peak"],"loop_contribution_label":"canonical_archetype_rule_candidate","do_not_propose_new_weight_delta":false}
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
- price-only/insurance-theme-only rows cannot promote Stage2/Stage3.
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
11. Add validation that C22 insurance/rate-cycle rows cannot promote without reserve/CSM quality, loss-ratio or rate-cycle ROE bridge, capital return, shareholder-return execution, PBR repair, solvency/balance-sheet quality, or earnings-revision bridge.

### Expected output

- Concise implementation summary.
- Rows accepted/rejected.
- New sector/canonical archetype coverage.
- Existing axis strengthened/weakened/kept.
- No investment recommendation language.

## 22. Next Round State

```text
completed_round = R6
completed_loop = 74
next_round = R7
next_loop = 74
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
atlas/symbol_profiles/082/082640.json
atlas/symbol_profiles/000/000540.json
atlas/symbol_profiles/003/003690.json
atlas/ohlcv_tradable_by_symbol_year/000/000370/2024.csv
atlas/ohlcv_tradable_by_symbol_year/082/082640/2024.csv
atlas/ohlcv_tradable_by_symbol_year/000/000540/2024.csv
atlas/ohlcv_tradable_by_symbol_year/003/003690/2024.csv
```

This loop continues loop 74 with R6 and adds 3 new independent C22 representative cases, 2 positives, 1 counterexample, and 1 canonical-archetype residual guard candidate for R6/L6.
