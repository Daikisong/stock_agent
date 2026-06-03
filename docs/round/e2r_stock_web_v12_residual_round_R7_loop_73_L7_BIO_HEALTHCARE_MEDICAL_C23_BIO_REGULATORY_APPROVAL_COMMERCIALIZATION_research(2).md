# E2R Stock-Web Historical Calibration / Sector-Archetype Residual Research Round

## 0. Research Metadata

```text
scheduled_round: R7
scheduled_loop: 73
round_schedule_status: valid
round_sector_consistency: pass
computed_next_round: R8
computed_next_loop: 73
large_sector_id: L7_BIO_HEALTHCARE_MEDICAL
canonical_archetype_id: C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION
fine_archetype_id: C23_APPROVAL_PARTNER_REVENUE_PROFITABILITY_BRIDGE_GUARD
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

R7 maps to `L7_BIO_HEALTHCARE_MEDICAL`. The prior R7 loop used C24 trial/data event risk, so this run shifts to C23. C23 is the more commercial side of biotech: regulatory approval, commercialization, partner execution, drug sales, and profitability. The residual is that an event spike can look like commercialization, but it only becomes useful when revenue, profit, margin, partner execution, or operating leverage actually carries it.

| layer | id | definition |
|---|---|---|
| round | R7 | bio / healthcare / medical |
| large_sector | L7_BIO_HEALTHCARE_MEDICAL | biotech, pharma, healthcare, commercial-stage bio |
| canonical | C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION | regulatory approval, commercialization, partner/revenue bridge |
| fine | C23_APPROVAL_PARTNER_REVENUE_PROFITABILITY_BRIDGE_GUARD | approval/commercial event must become partner/revenue/profit bridge |
| deep | US_COMMERCIAL_DRUG_REVENUE_TO_PROFITABILITY_AND_OPERATING_LEVERAGE | commercial-drug profitability success |
| deep | K_CAB_GLOBAL_PARTNER_SALES_TO_MARGIN_COMMERCIAL_EXECUTION | approved-drug/global partner bridge |
| deep | RNA_PLATFORM_OPTIONALITY_PRICE_SPIKE_WITHOUT_APPROVAL_PARTNER_REVENUE | platform/regulatory event MFE without commercial bridge |

## 3. No-Repeat / Coverage Check

No-Repeat hard duplicate key:

```text
canonical_archetype_id + symbol + trigger_type + entry_date
```

C23 top-covered symbols are `000100`, `028300`, `UNKNOWN_SYMBOL`, `145020`, `196170`, and `068270`. This run avoids that top cluster and also avoids the prior R7/C24 symbols `220100`, `007390`, and `226950`.

| archetype | selected symbol | duplicate status | reason |
|---|---:|---|---|
| C23 | 326030 | new independent | not top-covered C23 symbol; commercial-drug sales/profitability bridge |
| C23 | 195940 | new independent | not top-covered C23 symbol; approved-drug global commercialization bridge |
| C23 | 244460 | new independent | not top-covered C23 symbol; platform/regulatory event MFE without commercial bridge |

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
326030 and 195940 have no corporate-action candidate dates in their symbol profiles.
244460 has corporate-action candidates on 2021-04-16 and 2024-10-30; the selected 2023-08-10 representative window avoids those blocked dates.
141080/리가켐바이오는 reviewed as a strong license/event case but excluded here because the 2024-04-23 corporate-action candidate falls inside a clean 180D representative window after the 2023-12-26 trigger.
```

## 6. Case Selection Summary

| role | symbol | company | trigger | entry | price | result |
|---|---:|---|---|---:|---:|---|
| structural_success_delayed_with_MAE_watch | 326030 | SK바이오팜 | Stage2-Actionable | 2024-01-29 | 93900 | commercial-drug sales/profitability bridge worked later, but early MAE required watch |
| structural_success_with_bridge_and_drawdown_watch | 195940 | HK이노엔 | Stage2-Actionable | 2024-07-09 | 40150 | approved-drug/global partner commercialization bridge worked with drawdown guard |
| event_MFE_but_no_commercialization_bridge_counterexample | 244460 | 올리패스 | Stage2-Actionable | 2023-08-10 | 2190 | platform/regulatory event produced MFE but lacked commercial bridge |

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
| 326030 | SK바이오팜 | Stage2-Actionable | 2024-01-29 | 93900 | 4.26 | 5.11 | 27.26 | -10.12 | -19.6 | -22.68 | 2024-08-29 | 119500 | -17.99 |
| 195940 | HK이노엔 | Stage2-Actionable | 2024-07-09 | 40150 | 6.72 | 28.02 | 28.02 | -14.2 | -14.2 | -14.2 | 2024-09-23 | 51400 | -6.13 |
| 244460 | 올리패스 | Stage2-Actionable | 2023-08-10 | 2190 | 27.85 | 57.53 | 57.53 | -26.71 | -26.71 | -26.71 | 2023-09-27 | 3450 | -30.43 |

## 9. Case-by-Case Notes

### 9.1 326030 / SK바이오팜 — commercial-drug profitability bridge with early MAE

The entry row is 2024-01-29 at 93,900. The first 90D window is not clean, and the adverse path reaches -19.6%. But the broader 180D path eventually reaches 119,500. This is a C23 success only after the commercial drug / profitability bridge becomes visible. It should not loosen Green because the early drawdown says the bridge was not yet fully paved.

### 9.2 195940 / HK이노엔 — approved-drug/global commercialization bridge

The entry row is 2024-07-09 at 40,150. The 90D path reaches 51,400, while early MAE is meaningful. This validates the approved-drug/global partner commercialization route, but again with 4B/high-MAE watch. Commercialization is not a press release; it is a checkout counter that has to ring repeatedly.

### 9.3 244460 / 올리패스 — platform/regulatory event MFE without commercial bridge

The entry row is 2023-08-10 at 2,190. The path reaches 3,450, so price alone looks impressive. But the evidence is platform/regulatory optionality without approval, partner execution, revenue, profit, or commercialization bridge. This is a C23 Green false-positive counterexample: MFE can be real and still not be durable evidence.

## 10. Current Calibrated Profile Stress Test

| question | result |
|---|---|
| Stage2 actionable bonus too strong? | Yes when C23 treats platform/regulatory event MFE as enough evidence. |
| Stage3 Yellow threshold too loose? | Not globally; C23 needs approval/partner/revenue/profitability bridge before Yellow. |
| Stage3 Green too strict? | Correct. No Green loosening. |
| Price-only blowoff guard appropriate? | Yes, especially for 244460 and early event spikes. |
| Full 4B non-price requirement appropriate? | Yes. MFE alone does not promote 244460; 326030/195940 have better commercial bridges. |
| 4C timing issue? | High-MAE watch is useful; no immediate hard 4C promotion proposed. |

## 11. Stage2 / Yellow / Green Comparison

```text
326030:
  Stage2-Actionable = correct
  Stage3-Yellow = allowed only after commercial sales/profitability bridge becomes visible
  Stage3-Green = reject unless early MAE and execution risk are cleared

195940:
  Stage2-Actionable = correct
  Stage3-Yellow = allowed after approved-drug commercialization / partner bridge
  Stage3-Green = wait for margin and repeated revenue durability

244460:
  Stage2-Actionable = acceptable as event watch
  Stage3-Yellow = reject without approval, partner execution, revenue, or commercialization bridge
  Stage3-Green = reject despite MFE
```

## 12. 4B Local vs Full-window Timing Audit

| symbol | local_peak_proximity | full_window_peak_proximity | verdict |
|---:|---:|---:|---|
| 326030 | 0.82 | 1.00 | delayed full-window 4B watch after commercial profitability bridge |
| 195940 | 0.91 | 1.00 | good 4B watch after global commercialization bridge |
| 244460 | 0.81 | 1.00 | large MFE but no commercialization bridge; keep 4B/high-MAE watch |

## 13. Canonical-Archetype Rule Candidate

```text
canonical_archetype_rule_candidate: true
rule_scope: canonical_archetype_specific
rule_id: c23_requires_approval_partner_revenue_profitability_bridge

rule:
  For C23 bio regulatory approval/commercialization rows, do not promote regulatory,
  platform, approval-expectation, partner-expectation, or commercial-stage Stage2 signals
  into Stage3-Yellow/Green unless at least one non-price bridge is visible:
  approved-drug revenue, prescription/sales growth, partner execution, license milestone,
  margin conversion, profitability turn, operating leverage, or commercialization cashflow.
```

## 14. Before / After Backtest Comparison

| profile | eligible triggers | avg MFE90 | avg MAE90 | false positive rate | verdict |
|---|---:|---:|---:|---:|---|
| P0 e2r_2_1_stock_web_calibrated_proxy | 3 | 30.22 | -20.17 | 33.3% | useful but can over-credit platform/event MFE |
| P0b e2r_2_0_baseline_reference | 3 | 30.22 | -20.17 | 0% | safer but may miss 326030/195940 |
| P1 sector_specific_candidate_profile | 3 | 30.22 | -20.17 | 33.3% | no broad L7 loosen |
| P2 canonical_archetype_candidate_profile | 2 selected positives | 16.57 | -16.9 | 0% after bridge gate | preferred shadow |
| P3 counterexample_guard_profile | 1 rejected | 57.53 | -26.71 | 0% after no-Green routing | useful guard |

## 15. Score-Return Alignment Matrix

| case | current profile verdict | alignment |
|---|---|---|
| 326030 | current_profile_partially_correct | commercialization bridge worked later, but early MAE requires watch |
| 195940 | current_profile_correct_with_drawdown_guard | approved-drug/global commercialization bridge aligned with MFE |
| 244460 | current_profile_false_positive_if_green | event MFE existed but no commercial bridge |

## 16. Coverage Matrix

| large_sector_id | canonical_archetype_id | fine_archetype_id | positive | counterexample | 4B | 4C/watch | new_independent | reused | usable_triggers | representative | profile_errors | sector_rule | canonical_rule | coverage_gap_after |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|---|---|
| L7_BIO_HEALTHCARE_MEDICAL | C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION | C23_APPROVAL_PARTNER_REVENUE_PROFITABILITY_BRIDGE_GUARD | 2 | 1 | 3 | 3 | 3 | 0 | 3 | 3 | 1 | false | true | C23 non-top-covered approval/commercialization residual reduced |

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
- hard_4c_thesis_break_routes_to_4c
residual_error_types_found:
- platform event MFE without commercial bridge
- commercialization winner needs 4B watch
- early MAE before revenue/profit bridge confirmation
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
- 141080 as representative row, because 2024-04-23 corporate-action candidate contaminates the post-2023-12-26 180D window
```

## 19. Shadow Weight Calibration

```csv
row_type,axis,scope,large_sector_id,canonical_archetype_id,baseline_value,tested_value,delta,reason,backtest_effect,trigger_ids,calibration_usable_count,new_independent_case_count,counterexample_count,confidence,proposal_type,notes
shadow_weight,c23_requires_approval_partner_revenue_profitability_bridge,canonical_archetype_specific,L7_BIO_HEALTHCARE_MEDICAL,C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION,0,1,+1,"C23 bio commercialization rows should not promote toward Stage3-Yellow/Green unless approval/commercialization signal converts into approved-drug sales, partner execution, revenue/profitability, margin, or operating leverage bridge","326030 and 195940 survive after commercialization bridge, though with MAE/4B watch; 244460 remains 4B/high-MAE watch because event MFE lacks commercial bridge","TRG_R7L73_C23_326030_20240129_XCOPRI_COMMERCIALIZATION_PROFITABILITY_BRIDGE|TRG_R7L73_C23_195940_20240709_KCAB_GLOBAL_COMMERCIALIZATION_BRIDGE|TRG_R7L73_C23_244460_20230810_RNA_PLATFORM_REGULATORY_EVENT_NO_COMMERCIAL_BRIDGE",3,3,1,medium,canonical_shadow_only,"not production; post-calibrated residual"
shadow_weight,c23_event_mfe_4b_high_mae_watch_guard,canonical_archetype_specific,L7_BIO_HEALTHCARE_MEDICAL,C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION,1,1,0,"Bio commercialization winners and platform-event MFE rows can peak before revenue durability is confirmed; local/full-window 4B and high-MAE watch must remain active","prevents 244460 from Green routing while preserving 326030/195940 as guarded positives","TRG_R7L73_C23_326030_20240129_XCOPRI_COMMERCIALIZATION_PROFITABILITY_BRIDGE|TRG_R7L73_C23_195940_20240709_KCAB_GLOBAL_COMMERCIALIZATION_BRIDGE|TRG_R7L73_C23_244460_20230810_RNA_PLATFORM_REGULATORY_EVENT_NO_COMMERCIAL_BRIDGE",3,3,1,medium,existing_axis_kept,"strengthens local/full-window 4B and high-MAE watch without global delta"
```

## 20. Machine-Readable Rows

### 20.1 price_source_validation

```jsonl
{"row_type":"price_source_validation","source":"Songdaiki/stock-web","source_url":"https://github.com/Songdaiki/stock-web","manifest_path":"atlas/manifest.json","schema_path":"atlas/schema.json","universe_path":"atlas/universe/all_symbols.csv","manifest_max_date":"2026-02-20","source_name":"FinanceData/marcap","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","calibration_shard_root":"atlas/ohlcv_tradable_by_symbol_year","raw_shard_root":"atlas/ohlcv_raw_by_symbol_year","validation_status":"usable_for_historical_calibration"}
```

### 20.2 case rows

```jsonl
{"row_type":"case","case_id":"R7L73_C23_326030_20240129_XCOPRI_COMMERCIALIZATION_PROFITABILITY_BRIDGE","symbol":"326030","company_name":"SK바이오팜","round":"R7","loop":"73","large_sector_id":"L7_BIO_HEALTHCARE_MEDICAL","canonical_archetype_id":"C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION","fine_archetype_id":"C23_COMMERCIAL_DRUG_SALES_PROFITABILITY_BRIDGE","deep_sub_archetype_id":"US_COMMERCIAL_DRUG_REVENUE_TO_PROFITABILITY_AND_OPERATING_LEVERAGE","case_type":"structural_success_delayed_with_MAE_watch","positive_or_counterexample":"positive","best_trigger":"Stage2-Actionable","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"score_return_mixed","current_profile_verdict":"current_profile_partially_correct","price_source":"Songdaiki/stock-web","notes":"C23 commercialization rows require approved-drug sales, partner execution, revenue, profit, margin, or commercialization bridge; platform/regulatory event MFE alone is insufficient."}
{"row_type":"case","case_id":"R7L73_C23_195940_20240709_KCAB_GLOBAL_COMMERCIALIZATION_BRIDGE","symbol":"195940","company_name":"HK이노엔","round":"R7","loop":"73","large_sector_id":"L7_BIO_HEALTHCARE_MEDICAL","canonical_archetype_id":"C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION","fine_archetype_id":"C23_APPROVED_DRUG_GLOBAL_COMMERCIALIZATION_BRIDGE","deep_sub_archetype_id":"K_CAB_GLOBAL_PARTNER_SALES_TO_MARGIN_COMMERCIAL_EXECUTION","case_type":"structural_success_with_bridge_and_drawdown_watch","positive_or_counterexample":"positive","best_trigger":"Stage2-Actionable","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"score_return_aligned","current_profile_verdict":"current_profile_correct_with_drawdown_guard","price_source":"Songdaiki/stock-web","notes":"C23 commercialization rows require approved-drug sales, partner execution, revenue, profit, margin, or commercialization bridge; platform/regulatory event MFE alone is insufficient."}
{"row_type":"case","case_id":"R7L73_C23_244460_20230810_RNA_PLATFORM_REGULATORY_EVENT_NO_COMMERCIAL_BRIDGE","symbol":"244460","company_name":"올리패스","round":"R7","loop":"73","large_sector_id":"L7_BIO_HEALTHCARE_MEDICAL","canonical_archetype_id":"C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION","fine_archetype_id":"C23_PLATFORM_REGULATORY_EVENT_WITHOUT_COMMERCIAL_BRIDGE","deep_sub_archetype_id":"RNA_PLATFORM_OPTIONALITY_PRICE_SPIKE_WITHOUT_APPROVAL_PARTNER_REVENUE","case_type":"event_MFE_but_no_commercialization_bridge_counterexample","positive_or_counterexample":"counterexample","best_trigger":"Stage2-Actionable","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"score_return_mixed","current_profile_verdict":"current_profile_false_positive_if_green","price_source":"Songdaiki/stock-web","notes":"C23 commercialization rows require approved-drug sales, partner execution, revenue, profit, margin, or commercialization bridge; platform/regulatory event MFE alone is insufficient."}
```

### 20.3 trigger rows

```jsonl
{"row_type":"trigger","trigger_id":"TRG_R7L73_C23_326030_20240129_XCOPRI_COMMERCIALIZATION_PROFITABILITY_BRIDGE","case_id":"R7L73_C23_326030_20240129_XCOPRI_COMMERCIALIZATION_PROFITABILITY_BRIDGE","symbol":"326030","company_name":"SK바이오팜","round":"R7","loop":"73","large_sector_id":"L7_BIO_HEALTHCARE_MEDICAL","canonical_archetype_id":"C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION","fine_archetype_id":"C23_COMMERCIAL_DRUG_SALES_PROFITABILITY_BRIDGE","deep_sub_archetype_id":"US_COMMERCIAL_DRUG_REVENUE_TO_PROFITABILITY_AND_OPERATING_LEVERAGE","loop_objective":"coverage_gap_fill|counterexample_mining|stage2_actionable_bonus_stress_test|4B_non_price_requirement_stress_test|canonical_archetype_compression","trigger_type":"Stage2-Actionable","trigger_date":"2024-01-29","entry_date":"2024-01-29","entry_price":93900,"evidence_available_at_that_date":"source_proxy_Xcopri_US_sales_profitability_operating_leverage_bridge; evidence_url_pending","evidence_source":"source_proxy_Xcopri_US_sales_profitability_operating_leverage_bridge; evidence_url_pending","bridge_summary":"commercial-stage drug sales/profitability bridge eventually converted into strong MFE, but early MAE means this is not a loose Green case","stage2_evidence_fields":["commercial_drug_sales_growth","profitability_turn_proxy","relative_strength_repair","operating_leverage_bridge"],"stage3_evidence_fields":["sales_to_profitability_visibility","commercial_execution_proxy","earnings_revision_proxy"],"stage4b_evidence_fields":["delayed_MFE_peak_watch","commercial_bio_valuation_repricing_after_profit_turn"],"stage4c_evidence_fields":["early_MAE_watch_before_profitability_confirmation"],"price_data_source":"Songdaiki/stock-web","price_data_repo":"Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/326/326030/2024.csv","profile_path":"atlas/symbol_profiles/326/326030.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":4.26,"MFE_90D_pct":5.11,"MFE_180D_pct":27.26,"MFE_1Y_pct":27.26,"MFE_2Y_pct":27.26,"MAE_30D_pct":-10.12,"MAE_90D_pct":-19.6,"MAE_180D_pct":-22.68,"MAE_1Y_pct":-22.68,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-08-29","peak_price":119500,"drawdown_after_peak_pct":-17.99,"green_lateness_ratio":"0.58","four_b_local_peak_proximity":0.82,"four_b_full_window_peak_proximity":1.0,"four_b_timing_verdict":"delayed_full_window_4B_watch_after_commercial_profitability_bridge","four_b_evidence_type":"non_price_commercialization_revenue_bridge","four_c_protection_label":"early_MAE_watch","trigger_outcome_label":"commercialization_success_delayed_then_4B_watch","current_profile_verdict":"current_profile_partially_correct","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"R7L73_C23_326030_20240129_XCOPRI_COMMERCIALIZATION_PROFITABILITY_BRIDGE_entry","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"TRG_R7L73_C23_195940_20240709_KCAB_GLOBAL_COMMERCIALIZATION_BRIDGE","case_id":"R7L73_C23_195940_20240709_KCAB_GLOBAL_COMMERCIALIZATION_BRIDGE","symbol":"195940","company_name":"HK이노엔","round":"R7","loop":"73","large_sector_id":"L7_BIO_HEALTHCARE_MEDICAL","canonical_archetype_id":"C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION","fine_archetype_id":"C23_APPROVED_DRUG_GLOBAL_COMMERCIALIZATION_BRIDGE","deep_sub_archetype_id":"K_CAB_GLOBAL_PARTNER_SALES_TO_MARGIN_COMMERCIAL_EXECUTION","loop_objective":"coverage_gap_fill|counterexample_mining|stage2_actionable_bonus_stress_test|4B_non_price_requirement_stress_test|canonical_archetype_compression","trigger_type":"Stage2-Actionable","trigger_date":"2024-07-09","entry_date":"2024-07-09","entry_price":40150,"evidence_available_at_that_date":"source_proxy_KCAB_global_partner_sales_commercialization_margin_bridge; evidence_url_pending","evidence_source":"source_proxy_KCAB_global_partner_sales_commercialization_margin_bridge; evidence_url_pending","bridge_summary":"approved-drug commercialization/global partner route converted into MFE, but early drawdown required bridge confirmation and 4B watch","stage2_evidence_fields":["approved_drug_commercialization","global_partner_sales_proxy","relative_strength","margin_bridge_proxy"],"stage3_evidence_fields":["commercial_sales_visibility","partner_market_expansion_proxy","margin_conversion_watch"],"stage4b_evidence_fields":["post_MFE_peak_watch","commercialization_crowding_watch"],"stage4c_evidence_fields":["early_MAE_watch"],"price_data_source":"Songdaiki/stock-web","price_data_repo":"Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/195/195940/2024.csv","profile_path":"atlas/symbol_profiles/195/195940.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":6.72,"MFE_90D_pct":28.02,"MFE_180D_pct":28.02,"MFE_1Y_pct":28.02,"MFE_2Y_pct":28.02,"MAE_30D_pct":-14.2,"MAE_90D_pct":-14.2,"MAE_180D_pct":-14.2,"MAE_1Y_pct":-14.2,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-09-23","peak_price":51400,"drawdown_after_peak_pct":-6.13,"green_lateness_ratio":"0.42","four_b_local_peak_proximity":0.91,"four_b_full_window_peak_proximity":1.0,"four_b_timing_verdict":"good_4B_watch_after_global_commercialization_bridge","four_b_evidence_type":"non_price_commercialization_revenue_bridge","four_c_protection_label":"early_MAE_watch","trigger_outcome_label":"commercialization_success_but_needs_4B_watch","current_profile_verdict":"current_profile_correct_with_drawdown_guard","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"R7L73_C23_195940_20240709_KCAB_GLOBAL_COMMERCIALIZATION_BRIDGE_entry","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"TRG_R7L73_C23_244460_20230810_RNA_PLATFORM_REGULATORY_EVENT_NO_COMMERCIAL_BRIDGE","case_id":"R7L73_C23_244460_20230810_RNA_PLATFORM_REGULATORY_EVENT_NO_COMMERCIAL_BRIDGE","symbol":"244460","company_name":"올리패스","round":"R7","loop":"73","large_sector_id":"L7_BIO_HEALTHCARE_MEDICAL","canonical_archetype_id":"C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION","fine_archetype_id":"C23_PLATFORM_REGULATORY_EVENT_WITHOUT_COMMERCIAL_BRIDGE","deep_sub_archetype_id":"RNA_PLATFORM_OPTIONALITY_PRICE_SPIKE_WITHOUT_APPROVAL_PARTNER_REVENUE","loop_objective":"coverage_gap_fill|counterexample_mining|stage2_actionable_bonus_stress_test|4B_non_price_requirement_stress_test|canonical_archetype_compression","trigger_type":"Stage2-Actionable","trigger_date":"2023-08-10","entry_date":"2023-08-10","entry_price":2190,"evidence_available_at_that_date":"source_proxy_RNA_platform_regulatory_or_partner_expectation_without_approval_commercial_revenue_bridge; evidence_url_pending","evidence_source":"source_proxy_RNA_platform_regulatory_or_partner_expectation_without_approval_commercial_revenue_bridge; evidence_url_pending","bridge_summary":"platform/regulatory event produced MFE, but absence of approval, partner execution, revenue, or commercialization bridge means it should remain 4B/high-MAE watch, not Stage3-Green","stage2_evidence_fields":["platform_regulatory_event","price_spike","relative_strength"],"stage3_evidence_fields":[],"stage4b_evidence_fields":["large_MFE_without_commercial_bridge","event_crowding","partner_or_approval_bridge_absent"],"stage4c_evidence_fields":["high_MAE_without_approval_or_revenue_bridge"],"price_data_source":"Songdaiki/stock-web","price_data_repo":"Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/244/244460/2023.csv","profile_path":"atlas/symbol_profiles/244/244460.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":27.85,"MFE_90D_pct":57.53,"MFE_180D_pct":57.53,"MFE_1Y_pct":57.53,"MFE_2Y_pct":57.53,"MAE_30D_pct":-26.71,"MAE_90D_pct":-26.71,"MAE_180D_pct":-26.71,"MAE_1Y_pct":-26.71,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2023-09-27","peak_price":3450,"drawdown_after_peak_pct":-30.43,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":0.81,"four_b_full_window_peak_proximity":1.0,"four_b_timing_verdict":"large_MFE_but_no_commercialization_bridge_keep_4B_high_MAE_watch","four_b_evidence_type":"event_MFE_without_commercial_bridge","four_c_protection_label":"high_MAE_watch","trigger_outcome_label":"event_MFE_but_green_false_positive_counterexample","current_profile_verdict":"current_profile_false_positive_if_green","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"R7L73_C23_244460_20230810_RNA_PLATFORM_REGULATORY_EVENT_NO_COMMERCIAL_BRIDGE_entry","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
```

### 20.4 score_simulation rows

```jsonl
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"R7L73_C23_326030_20240129_XCOPRI_COMMERCIALIZATION_PROFITABILITY_BRIDGE","trigger_id":"TRG_R7L73_C23_326030_20240129_XCOPRI_COMMERCIALIZATION_PROFITABILITY_BRIDGE","symbol":"326030","large_sector_id":"L7_BIO_HEALTHCARE_MEDICAL","canonical_archetype_id":"C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION","raw_component_scores_before":{"approval_commercial_score":11,"partner_execution_score":10,"revenue_profit_bridge_score":11,"margin_operating_leverage_score":8,"relative_strength_score":9,"event_binary_risk_penalty":5},"weighted_score_before":73,"stage_label_before":"Stage2-Actionable","raw_component_scores_after":{"approval_commercial_score":13,"partner_execution_score":13,"revenue_profit_bridge_score":15,"margin_operating_leverage_score":11,"relative_strength_score":7,"event_binary_risk_penalty":6},"weighted_score_after":81,"stage_label_after":"Stage3-Yellow","changed_components":["approval_commercial_score","partner_execution_score","revenue_profit_bridge_score","margin_operating_leverage_score","relative_strength_score","event_binary_risk_penalty"],"component_delta_explanation":"C23 row is promoted only when approved-drug or commercialization signal converts into revenue/profitability or partner-execution bridge.","MFE_90D_pct":5.11,"MAE_90D_pct":-19.6,"score_return_alignment_label":"score_return_mixed","current_profile_verdict":"current_profile_partially_correct"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"R7L73_C23_195940_20240709_KCAB_GLOBAL_COMMERCIALIZATION_BRIDGE","trigger_id":"TRG_R7L73_C23_195940_20240709_KCAB_GLOBAL_COMMERCIALIZATION_BRIDGE","symbol":"195940","large_sector_id":"L7_BIO_HEALTHCARE_MEDICAL","canonical_archetype_id":"C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION","raw_component_scores_before":{"approval_commercial_score":11,"partner_execution_score":10,"revenue_profit_bridge_score":11,"margin_operating_leverage_score":8,"relative_strength_score":9,"event_binary_risk_penalty":5},"weighted_score_before":73,"stage_label_before":"Stage2-Actionable","raw_component_scores_after":{"approval_commercial_score":13,"partner_execution_score":13,"revenue_profit_bridge_score":15,"margin_operating_leverage_score":11,"relative_strength_score":7,"event_binary_risk_penalty":6},"weighted_score_after":81,"stage_label_after":"Stage3-Yellow","changed_components":["approval_commercial_score","partner_execution_score","revenue_profit_bridge_score","margin_operating_leverage_score","relative_strength_score","event_binary_risk_penalty"],"component_delta_explanation":"C23 row is promoted only when approved-drug or commercialization signal converts into revenue/profitability or partner-execution bridge.","MFE_90D_pct":28.02,"MAE_90D_pct":-14.2,"score_return_alignment_label":"score_return_aligned","current_profile_verdict":"current_profile_correct_with_drawdown_guard"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"R7L73_C23_244460_20230810_RNA_PLATFORM_REGULATORY_EVENT_NO_COMMERCIAL_BRIDGE","trigger_id":"TRG_R7L73_C23_244460_20230810_RNA_PLATFORM_REGULATORY_EVENT_NO_COMMERCIAL_BRIDGE","symbol":"244460","large_sector_id":"L7_BIO_HEALTHCARE_MEDICAL","canonical_archetype_id":"C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION","raw_component_scores_before":{"approval_commercial_score":5,"partner_execution_score":2,"revenue_profit_bridge_score":0,"margin_operating_leverage_score":0,"relative_strength_score":12,"event_binary_risk_penalty":8},"weighted_score_before":62,"stage_label_before":"Stage2-Actionable","raw_component_scores_after":{"approval_commercial_score":2,"partner_execution_score":0,"revenue_profit_bridge_score":0,"margin_operating_leverage_score":0,"relative_strength_score":5,"event_binary_risk_penalty":15},"weighted_score_after":41,"stage_label_after":"Stage1-Watch_or_4B-Watch","changed_components":["approval_commercial_score","partner_execution_score","revenue_profit_bridge_score","margin_operating_leverage_score","relative_strength_score","event_binary_risk_penalty"],"component_delta_explanation":"C23 guard demotes platform/regulatory event rows when approval, partner execution, revenue, or commercialization bridge is absent.","MFE_90D_pct":57.53,"MAE_90D_pct":-26.71,"score_return_alignment_label":"score_return_mixed","current_profile_verdict":"current_profile_false_positive_if_green"}
```

### 20.5 shadow_weight rows

```csv
row_type,axis,scope,large_sector_id,canonical_archetype_id,baseline_value,tested_value,delta,reason,backtest_effect,trigger_ids,calibration_usable_count,new_independent_case_count,counterexample_count,confidence,proposal_type,notes
shadow_weight,c23_requires_approval_partner_revenue_profitability_bridge,canonical_archetype_specific,L7_BIO_HEALTHCARE_MEDICAL,C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION,0,1,+1,"C23 bio commercialization rows should not promote toward Stage3-Yellow/Green unless approval/commercialization signal converts into approved-drug sales, partner execution, revenue/profitability, margin, or operating leverage bridge","326030 and 195940 survive after commercialization bridge, though with MAE/4B watch; 244460 remains 4B/high-MAE watch because event MFE lacks commercial bridge","TRG_R7L73_C23_326030_20240129_XCOPRI_COMMERCIALIZATION_PROFITABILITY_BRIDGE|TRG_R7L73_C23_195940_20240709_KCAB_GLOBAL_COMMERCIALIZATION_BRIDGE|TRG_R7L73_C23_244460_20230810_RNA_PLATFORM_REGULATORY_EVENT_NO_COMMERCIAL_BRIDGE",3,3,1,medium,canonical_shadow_only,"not production; post-calibrated residual"
shadow_weight,c23_event_mfe_4b_high_mae_watch_guard,canonical_archetype_specific,L7_BIO_HEALTHCARE_MEDICAL,C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION,1,1,0,"Bio commercialization winners and platform-event MFE rows can peak before revenue durability is confirmed; local/full-window 4B and high-MAE watch must remain active","prevents 244460 from Green routing while preserving 326030/195940 as guarded positives","TRG_R7L73_C23_326030_20240129_XCOPRI_COMMERCIALIZATION_PROFITABILITY_BRIDGE|TRG_R7L73_C23_195940_20240709_KCAB_GLOBAL_COMMERCIALIZATION_BRIDGE|TRG_R7L73_C23_244460_20230810_RNA_PLATFORM_REGULATORY_EVENT_NO_COMMERCIAL_BRIDGE",3,3,1,medium,existing_axis_kept,"strengthens local/full-window 4B and high-MAE watch without global delta"
```

### 20.6 residual_contribution row

```jsonl
{"row_type":"residual_contribution","round":"R7","loop":"73","large_sector_id":"L7_BIO_HEALTHCARE_MEDICAL","canonical_archetype_id":"C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION","new_independent_case_count":3,"reused_case_count":0,"new_symbol_count":3,"new_trigger_family_count":3,"tested_existing_calibrated_axes":["stage2_actionable_evidence_bonus","price_only_blowoff_blocks_positive_stage","full_4b_requires_non_price_evidence","local_4b_watch_guard","high_MAE_guardrail","hard_4c_thesis_break_routes_to_4c"],"residual_error_types_found":["platform_event_MFE_without_commercial_bridge","commercialization_winner_needs_4B_watch","early_MAE_before_revenue_profit_bridge_confirmation"],"loop_contribution_label":"canonical_archetype_rule_candidate","do_not_propose_new_weight_delta":false}
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
- price-only/platform-event-only rows cannot promote Stage2/Stage3.
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
11. Add validation that C23 commercialization rows cannot promote without approval, partner execution, revenue/profitability, margin, operating leverage, or commercialization cashflow bridge.
12. Add validation that corporate-action-contaminated rows like 141080 post-2023-12-26 cannot become representative rows unless a clean forward window is available.

### Expected output

- Concise implementation summary.
- Rows accepted/rejected.
- New sector/canonical archetype coverage.
- Existing axis strengthened/weakened/kept.
- No investment recommendation language.

## 22. Next Round State

```text
completed_round = R7
completed_loop = 73
next_round = R8
next_loop = 73
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
atlas/symbol_profiles/326/326030.json
atlas/symbol_profiles/195/195940.json
atlas/symbol_profiles/244/244460.json
atlas/symbol_profiles/141/141080.json
atlas/ohlcv_tradable_by_symbol_year/326/326030/2024.csv
atlas/ohlcv_tradable_by_symbol_year/195/195940/2024.csv
atlas/ohlcv_tradable_by_symbol_year/244/244460/2023.csv
atlas/ohlcv_tradable_by_symbol_year/141/141080/2023.csv
```

This loop continues loop 73 with R7 and adds 3 new independent C23 representative cases, 2 positives, 1 counterexample/watch case, and 1 canonical-archetype residual guard candidate for R7/L7.
