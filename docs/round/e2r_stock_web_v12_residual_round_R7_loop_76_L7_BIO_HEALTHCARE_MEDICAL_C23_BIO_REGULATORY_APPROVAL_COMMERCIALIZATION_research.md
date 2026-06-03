# E2R Stock-Web Historical Calibration / Sector-Archetype Residual Research Round

## 0. Research Metadata

```text
scheduled_round: R7
scheduled_loop: 76
round_schedule_status: valid
round_sector_consistency: pass
computed_next_round: R8
computed_next_loop: 76
large_sector_id: L7_BIO_HEALTHCARE_MEDICAL
canonical_archetype_id: C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION
fine_archetype_id: C23_COMMERCIALIZATION_BACKLOG_SALES_MARGIN_CASHFLOW_BRIDGE_GUARD
loop_objective: coverage_gap_fill | counterexample_mining | stage2_actionable_bonus_stress_test | 4B_non_price_requirement_stress_test | 4C_thesis_break_timing_test | canonical_archetype_compression
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

R7 maps directly to `L7_BIO_HEALTHCARE_MEDICAL`. The previous R7 loop used C24 trial/data event-risk, and earlier R7 work used C25 medical-device export/reimbursement. This run rotates to C23 bio regulatory approval/commercialization. The branch selected here is not binary clinical-event risk; it is commercialization quality: CDMO backlog, commercial batch capacity, product sales, partner validation, margin and cashflow.

| layer | id | definition |
|---|---|---|
| round | R7 | bio / healthcare / medical |
| large_sector | L7_BIO_HEALTHCARE_MEDICAL | biotech, pharma, CDMO, commercialization, medical/healthcare |
| canonical | C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION | regulatory approval, commercialization, sales ramp and CDMO value |
| fine | C23_COMMERCIALIZATION_BACKLOG_SALES_MARGIN_CASHFLOW_BRIDGE_GUARD | bio signal must become backlog/sales/margin/cashflow evidence |
| deep | BIOLOGICS_CDMO_BACKLOG_TO_COMMERCIAL_BATCH_REVENUE_MARGIN_AND_CAPACITY_VALUE | biologics CDMO positive |
| deep | OLIGONUCLEOTIDE_CDMO_COMMERCIAL_ORDER_AND_CAPACITY_TO_REVENUE_MARGIN_OPTION_VALUE | oligo CDMO positive |
| deep | PHARMA_PRODUCT_COMMERCIALIZATION_AND_OVERSEAS_OPTIONALITY_WITHOUT_PRESCRIPTION_GROWTH_MARGIN_OR_CASHFLOW_CONVERSION | product commercialization false positive |

## 3. No-Repeat / Coverage Check

No-Repeat hard duplicate key:

```text
canonical_archetype_id + symbol + trigger_type + entry_date
```

C23 top-covered symbols are `000100`, `028300`, `UNKNOWN_SYMBOL`, `145020`, `196170`, and `068270`. This run avoids that cluster and also avoids the previous R7/C24 representatives `141080`, `950220`, `299660` and C25 representatives `214450`, `200670`, `060280`.

| archetype | selected symbol | duplicate status | reason |
|---|---:|---|---|
| C23 | 207940 | new independent | not top-covered C23 symbol; CDMO backlog/commercial-batch capacity bridge |
| C23 | 237690 | new independent | not top-covered C23 symbol; oligo CDMO commercial-order/capacity bridge |
| C23 | 195940 | new independent | not top-covered C23 symbol; product commercialization MFE without durable growth/margin bridge |

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
207940 has a 2025-11-24 corporate-action candidate, outside the selected 2024 representative window.
237690 has no corporate-action candidate dates.
195940 has no corporate-action candidate dates.
All three representative windows are treated as clean for this residual calibration.
```

## 6. Case Selection Summary

| role | symbol | company | trigger | entry | price | result |
|---|---:|---|---|---:|---:|---|
| CDMO_backlog_commercialization_success_then_4B_watch | 207940 | 삼성바이오로직스 | Stage2-Actionable | 2024-01-29 | 800000 | biologics CDMO backlog/commercial-batch capacity bridge worked |
| oligo_CDMO_commercial_order_success_then_4B_high_MAE_watch | 237690 | 에스티팜 | Stage2-Actionable | 2024-01-29 | 62800 | oligo CDMO commercial-order/capacity bridge worked, but drawdown guard required |
| product_commercialization_theme_MFE_then_high_MAE_counterexample | 195940 | HK이노엔 | Stage2-Actionable | 2024-01-29 | 42950 | product commercialization MFE lacked durable sales/margin/cashflow bridge |

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
| 207940 | 삼성바이오로직스 | Stage2-Actionable | 2024-01-29 | 800000 | 10.0 | 10.0 | 39.13 | -3.5 | -9.88 | -9.88 | 2024-10-22 | 1113000 | -18.51 |
| 237690 | 에스티팜 | Stage2-Actionable | 2024-01-29 | 62800 | 57.64 | 57.64 | 92.36 | -4.62 | -4.62 | -4.62 | 2024-08-29 | 120800 | -40.4 |
| 195940 | HK이노엔 | Stage2-Actionable | 2024-01-29 | 42950 | 2.33 | 2.44 | 19.67 | -16.88 | -19.79 | -19.79 | 2024-09-23 | 51400 | -32.98 |

## 9. Case-by-Case Notes

### 9.1 207940 / 삼성바이오로직스 — CDMO backlog and commercial-batch bridge

The entry row is 2024-01-29 at 800,000. The path initially reached the high-800,000 zone and later reached 1,113,000. This is a valid C23 positive because the source bridge is CDMO backlog, commercial-batch capacity, utilization and margin value. It is still not a Green-loosening case because post-peak valuation and capacity-timing risk keep 4B active.

### 9.2 237690 / 에스티팜 — oligo CDMO commercial-order bridge

The entry row is 2024-01-29 at 62,800. The path reached 99,000 early and later reached 120,800. This is a positive C23 commercialization row because the move depends on oligonucleotide CDMO commercial orders, capacity and margin optionality. The later fall toward 72,000 means the correct stage is guarded Yellow plus 4B/high-MAE watch.

### 9.3 195940 / HK이노엔 — product commercialization MFE without durable bridge

The entry row is 2024-01-29 at 42,950. The path first fell into the mid-30,000 range, then later reached 51,400. That delayed MFE is not enough by itself. Without durable prescription growth, export royalty, partner validation, margin and cashflow evidence, this row should not be promoted to Stage3-Green.

## 10. Current Calibrated Profile Stress Test

| question | result |
|---|---|
| Stage2 actionable bonus too strong? | Yes when C23 treats product commercialization theme MFE as enough evidence. |
| Stage3 Yellow threshold too loose? | Not globally; C23 needs backlog/sales/margin/cashflow bridge before Yellow. |
| Stage3 Green too strict? | Correct. This round reinforces strict Green. |
| Price-only blowoff guard appropriate? | Yes, especially for 195940 and post-peak 237690. |
| Full 4B non-price requirement appropriate? | Yes. 207940/237690 have stronger non-price bridges; 195940 does not. |
| 4C timing issue? | High-MAE and delayed-MFE watch are useful; no immediate hard 4C production delta proposed. |

## 11. Stage2 / Yellow / Green Comparison

```text
207940:
  Stage2-Actionable = correct
  Stage3-Yellow = allowed after CDMO backlog / commercial-batch capacity / margin bridge
  Stage3-Green = reject unless valuation/capacity timing and post-peak durability clear

237690:
  Stage2-Actionable = correct
  Stage3-Yellow = allowed after oligo CDMO commercial-order / capacity / revenue-margin bridge
  Stage3-Green = reject because post-peak drawdown and CDMO cycle crowding remain active

195940:
  Stage2-Actionable = acceptable only as product commercialization watch
  Stage3-Yellow = reject without durable product sales, prescription growth, margin and cashflow bridge
  Stage3-Green = reject despite delayed MFE
```

## 12. 4B Local vs Full-window Timing Audit

| symbol | local_peak_proximity | full_window_peak_proximity | verdict |
|---:|---:|---:|---|
| 207940 | 0.79 | 1.00 | CDMO backlog/commercialization bridge positive but full-window 4B watch |
| 237690 | 0.82 | 1.00 | oligo CDMO order bridge positive but full-window 4B/high-MAE watch |
| 195940 | 0.86 | 1.00 | product commercialization MFE but no durable sales/margin bridge; keep 4B/high-MAE watch |

## 13. Canonical-Archetype Rule Candidate

```text
canonical_archetype_rule_candidate: true
rule_scope: canonical_archetype_specific
rule_id: c23_requires_commercialization_backlog_sales_margin_cashflow_bridge

rule:
  For C23 bio regulatory approval/commercialization rows, do not promote
  pharma product, biosimilar, biologics CDMO, oligo CDMO, overseas commercialization,
  approval, or product-launch Stage2 signals into Stage3-Yellow/Green unless at least
  one non-price bridge is visible:
  regulatory-to-commercial conversion, CDMO backlog, commercial-batch revenue,
  prescription or product-sales growth, partner validation, capacity utilization,
  margin conversion, FCF/cash conversion, or earnings revision tied to the asset.
```

## 14. Before / After Backtest Comparison

| profile | eligible triggers | avg MFE90 | avg MAE90 | false positive rate | verdict |
|---|---:|---:|---:|---:|---|
| P0 e2r_2_1_stock_web_calibrated_proxy | 3 | 23.36 | -11.43 | 33.3% | useful but can over-credit commercialization-theme delayed MFE |
| P0b e2r_2_0_baseline_reference | 3 | 23.36 | -11.43 | 0% | safer but may miss 207940/237690 |
| P1 sector_specific_candidate_profile | 3 | 23.36 | -11.43 | 33.3% | no broad L7 loosen |
| P2 canonical_archetype_candidate_profile | 2 selected positives | 33.82 | -7.25 | 0% after bridge gate | preferred shadow |
| P3 counterexample_guard_profile | 1 rejected/watch | 2.44 | -19.79 | 0% after no-Green routing | useful guard |

## 15. Score-Return Alignment Matrix

| case | current profile verdict | alignment |
|---|---|---|
| 207940 | current_profile_correct_but_no_green | CDMO backlog/commercialization bridge aligned with MFE but 4B watch remains |
| 237690 | current_profile_correct_with_drawdown_guard | oligo CDMO commercial-order bridge aligned with strong MFE, but drawdown guard remains |
| 195940 | current_profile_false_positive_if_green | delayed MFE lacked durable sales/margin/cashflow bridge |

## 16. Coverage Matrix

| large_sector_id | canonical_archetype_id | fine_archetype_id | positive | counterexample | 4B | 4C/watch | new_independent | reused | usable_triggers | representative | profile_errors | sector_rule | canonical_rule | coverage_gap_after |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|---|---|
| L7_BIO_HEALTHCARE_MEDICAL | C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION | C23_COMMERCIALIZATION_BACKLOG_SALES_MARGIN_CASHFLOW_BRIDGE_GUARD | 2 | 1 | 3 | 3 | 3 | 0 | 3 | 3 | 1 | false | true | R7/C23 non-top-covered commercialization residual reduced |

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
- commercialization theme without sales/margin bridge
- CDMO commercialization winner needs 4B watch
- oligo CDMO winner needs drawdown guard
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
- R7 direct L7 sector consistency
- large_sector/canonical consistency
- duplicate avoidance at symbol level
- representative rows use clean windows outside listed corporate-action candidate dates
```

Not validated:

```text
- exact disclosure/report URLs
- exact CDMO order/commercial batch/product sales disclosure URLs
- production scoring behavior
- live candidate status
```

## 19. Shadow Weight Calibration

```csv
row_type,axis,scope,large_sector_id,canonical_archetype_id,baseline_value,tested_value,delta,reason,backtest_effect,trigger_ids,calibration_usable_count,new_independent_case_count,counterexample_count,confidence,proposal_type,notes
shadow_weight,c23_requires_commercialization_backlog_sales_margin_cashflow_bridge,canonical_archetype_specific,L7_BIO_HEALTHCARE_MEDICAL,C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION,0,1,+1,"C23 bio commercialization rows should not promote toward Stage3-Yellow/Green unless regulatory/commercial signal converts into CDMO backlog, commercial batch revenue, prescription or product sales growth, partner validation, capacity utilization, margin, FCF or cashflow bridge","207940 and 237690 survive as guarded positives after CDMO/commercial order and margin bridge; 195940 is demoted because product-commercialization theme MFE lacked durable sales/margin/cashflow bridge","TRG_R7L76_C23_207940_20240129_CDMO_BACKLOG_COMMERCIALIZATION_MARGIN_BRIDGE|TRG_R7L76_C23_237690_20240129_OLIGO_CDMO_COMMERCIAL_ORDER_MARGIN_BRIDGE|TRG_R7L76_C23_195940_20240129_PRODUCT_COMMERCIALIZATION_THEME_WITHOUT_DURABLE_GROWTH_BRIDGE",3,3,1,medium,canonical_shadow_only,"not production; post-calibrated residual"
shadow_weight,c23_bio_commercialization_4b_high_mae_watch_guard,canonical_archetype_specific,L7_BIO_HEALTHCARE_MEDICAL,C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION,1,1,0,"Bio commercialization winners and product-theme false starts can peak before sales, capacity and margin durability are confirmed; local/full-window 4B and high-MAE watch should remain active","preserves 207940/237690 guarded positives while preventing 195940 commercialization-theme false positive","TRG_R7L76_C23_207940_20240129_CDMO_BACKLOG_COMMERCIALIZATION_MARGIN_BRIDGE|TRG_R7L76_C23_237690_20240129_OLIGO_CDMO_COMMERCIAL_ORDER_MARGIN_BRIDGE|TRG_R7L76_C23_195940_20240129_PRODUCT_COMMERCIALIZATION_THEME_WITHOUT_DURABLE_GROWTH_BRIDGE",3,3,1,medium,existing_axis_kept,"strengthens local/full-window 4B and high-MAE watch without global delta"
```

## 20. Machine-Readable Rows

### 20.1 price_source_validation

```jsonl
{"row_type":"price_source_validation","source":"Songdaiki/stock-web","source_url":"https://github.com/Songdaiki/stock-web","manifest_path":"atlas/manifest.json","schema_path":"atlas/schema.json","universe_path":"atlas/universe/all_symbols.csv","manifest_max_date":"2026-02-20","source_name":"FinanceData/marcap","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","calibration_shard_root":"atlas/ohlcv_tradable_by_symbol_year","raw_shard_root":"atlas/ohlcv_raw_by_symbol_year","validation_status":"usable_for_historical_calibration"}
```

### 20.2 case rows

```jsonl
{"row_type":"case","case_id":"R7L76_C23_207940_20240129_CDMO_BACKLOG_COMMERCIALIZATION_MARGIN_BRIDGE","symbol":"207940","company_name":"삼성바이오로직스","round":"R7","loop":"76","large_sector_id":"L7_BIO_HEALTHCARE_MEDICAL","canonical_archetype_id":"C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION","fine_archetype_id":"C23_CDMO_BACKLOG_COMMERCIALIZATION_MARGIN_BRIDGE","deep_sub_archetype_id":"BIOLOGICS_CDMO_BACKLOG_TO_COMMERCIAL_BATCH_REVENUE_MARGIN_AND_CAPACITY_VALUE","case_type":"CDMO_backlog_commercialization_success_then_4B_watch","positive_or_counterexample":"positive","best_trigger":"Stage2-Actionable","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"score_return_aligned","current_profile_verdict":"current_profile_correct_but_no_green","price_source":"Songdaiki/stock-web","notes":"C23 commercialization rows require regulatory/commercial conversion, CDMO backlog, product sales/prescription growth, capacity utilization, margin, partner validation or cashflow bridge; bio-commercialization theme MFE alone is insufficient."}
{"row_type":"case","case_id":"R7L76_C23_237690_20240129_OLIGO_CDMO_COMMERCIAL_ORDER_MARGIN_BRIDGE","symbol":"237690","company_name":"에스티팜","round":"R7","loop":"76","large_sector_id":"L7_BIO_HEALTHCARE_MEDICAL","canonical_archetype_id":"C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION","fine_archetype_id":"C23_OLIGO_CDMO_COMMERCIAL_ORDER_MARGIN_BRIDGE","deep_sub_archetype_id":"OLIGONUCLEOTIDE_CDMO_COMMERCIAL_ORDER_AND_CAPACITY_TO_REVENUE_MARGIN_OPTION_VALUE","case_type":"oligo_CDMO_commercial_order_success_then_4B_high_MAE_watch","positive_or_counterexample":"positive","best_trigger":"Stage2-Actionable","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"score_return_aligned","current_profile_verdict":"current_profile_correct_with_drawdown_guard","price_source":"Songdaiki/stock-web","notes":"C23 commercialization rows require regulatory/commercial conversion, CDMO backlog, product sales/prescription growth, capacity utilization, margin, partner validation or cashflow bridge; bio-commercialization theme MFE alone is insufficient."}
{"row_type":"case","case_id":"R7L76_C23_195940_20240129_PRODUCT_COMMERCIALIZATION_THEME_WITHOUT_DURABLE_GROWTH_BRIDGE","symbol":"195940","company_name":"HK이노엔","round":"R7","loop":"76","large_sector_id":"L7_BIO_HEALTHCARE_MEDICAL","canonical_archetype_id":"C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION","fine_archetype_id":"C23_PRODUCT_COMMERCIALIZATION_THEME_WITHOUT_DURABLE_GROWTH_MARGIN_BRIDGE","deep_sub_archetype_id":"PHARMA_PRODUCT_COMMERCIALIZATION_AND_OVERSEAS_OPTIONALITY_WITHOUT_PRESCRIPTION_GROWTH_MARGIN_OR_CASHFLOW_CONVERSION","case_type":"product_commercialization_theme_MFE_then_high_MAE_counterexample","positive_or_counterexample":"counterexample","best_trigger":"Stage2-Actionable","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"score_return_mixed","current_profile_verdict":"current_profile_false_positive_if_green","price_source":"Songdaiki/stock-web","notes":"C23 commercialization rows require regulatory/commercial conversion, CDMO backlog, product sales/prescription growth, capacity utilization, margin, partner validation or cashflow bridge; bio-commercialization theme MFE alone is insufficient."}
```

### 20.3 trigger rows

```jsonl
{"row_type":"trigger","trigger_id":"TRG_R7L76_C23_207940_20240129_CDMO_BACKLOG_COMMERCIALIZATION_MARGIN_BRIDGE","case_id":"R7L76_C23_207940_20240129_CDMO_BACKLOG_COMMERCIALIZATION_MARGIN_BRIDGE","symbol":"207940","company_name":"삼성바이오로직스","round":"R7","loop":"76","large_sector_id":"L7_BIO_HEALTHCARE_MEDICAL","canonical_archetype_id":"C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION","fine_archetype_id":"C23_CDMO_BACKLOG_COMMERCIALIZATION_MARGIN_BRIDGE","deep_sub_archetype_id":"BIOLOGICS_CDMO_BACKLOG_TO_COMMERCIAL_BATCH_REVENUE_MARGIN_AND_CAPACITY_VALUE","loop_objective":"coverage_gap_fill|counterexample_mining|stage2_actionable_bonus_stress_test|4B_non_price_requirement_stress_test|4C_thesis_break_timing_test|canonical_archetype_compression","trigger_type":"Stage2-Actionable","trigger_date":"2024-01-29","entry_date":"2024-01-29","entry_price":800000,"evidence_available_at_that_date":"source_proxy_biologics_CDMO_backlog_commercial_batch_capacity_margin_bridge; evidence_url_pending","evidence_source":"source_proxy_biologics_CDMO_backlog_commercial_batch_capacity_margin_bridge; evidence_url_pending","bridge_summary":"CDMO backlog, commercial batch capacity and biologics manufacturing utilization converted into revenue/margin and capacity-value bridge; post-peak valuation and capacity-timing risk required 4B watch","stage2_evidence_fields":["CDMO_backlog","commercial_batch_capacity","relative_strength","biologics_capacity_value_proxy"],"stage3_evidence_fields":["backlog_to_revenue_visibility","capacity_utilization_margin_bridge","commercial_batch_mix_proxy"],"stage4b_evidence_fields":["post_MFE_peak_watch","CDMO_capacity_timing_risk","valuation_crowding_after_rerating"],"stage4c_evidence_fields":["post_peak_drawdown_watch"],"price_data_source":"Songdaiki/stock-web","price_data_repo":"Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/207/207940/2024.csv","profile_path":"atlas/symbol_profiles/207/207940.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":10.0,"MFE_90D_pct":10.0,"MFE_180D_pct":39.13,"MFE_1Y_pct":39.13,"MFE_2Y_pct":39.13,"MAE_30D_pct":-3.5,"MAE_90D_pct":-9.88,"MAE_180D_pct":-9.88,"MAE_1Y_pct":-9.88,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-10-22","peak_price":1113000,"drawdown_after_peak_pct":-18.51,"green_lateness_ratio":"0.52","four_b_local_peak_proximity":0.79,"four_b_full_window_peak_proximity":1.0,"four_b_timing_verdict":"CDMO_backlog_commercialization_bridge_positive_but_full_window_4B_watch","four_b_evidence_type":"non_price_commercialization_backlog_margin_bridge","four_c_protection_label":"post_peak_drawdown_watch","trigger_outcome_label":"CDMO_backlog_commercialization_success_then_4B_watch","current_profile_verdict":"current_profile_correct_but_no_green","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"R7L76_C23_207940_20240129_CDMO_BACKLOG_COMMERCIALIZATION_MARGIN_BRIDGE_entry","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"TRG_R7L76_C23_237690_20240129_OLIGO_CDMO_COMMERCIAL_ORDER_MARGIN_BRIDGE","case_id":"R7L76_C23_237690_20240129_OLIGO_CDMO_COMMERCIAL_ORDER_MARGIN_BRIDGE","symbol":"237690","company_name":"에스티팜","round":"R7","loop":"76","large_sector_id":"L7_BIO_HEALTHCARE_MEDICAL","canonical_archetype_id":"C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION","fine_archetype_id":"C23_OLIGO_CDMO_COMMERCIAL_ORDER_MARGIN_BRIDGE","deep_sub_archetype_id":"OLIGONUCLEOTIDE_CDMO_COMMERCIAL_ORDER_AND_CAPACITY_TO_REVENUE_MARGIN_OPTION_VALUE","loop_objective":"coverage_gap_fill|counterexample_mining|stage2_actionable_bonus_stress_test|4B_non_price_requirement_stress_test|4C_thesis_break_timing_test|canonical_archetype_compression","trigger_type":"Stage2-Actionable","trigger_date":"2024-01-29","entry_date":"2024-01-29","entry_price":62800,"evidence_available_at_that_date":"source_proxy_oligo_CDMO_commercial_order_capacity_revenue_margin_bridge; evidence_url_pending","evidence_source":"source_proxy_oligo_CDMO_commercial_order_capacity_revenue_margin_bridge; evidence_url_pending","bridge_summary":"oligonucleotide CDMO commercial-order and capacity optionality converted into revenue/margin bridge, but post-peak demand/capacity and valuation drawdown required 4B watch","stage2_evidence_fields":["oligo_CDMO_order","commercialization_capacity_optionality","relative_strength","margin_bridge_proxy"],"stage3_evidence_fields":["order_to_revenue_visibility","capacity_utilization_margin_bridge","commercial_pipeline_value_proxy"],"stage4b_evidence_fields":["post_MFE_peak_watch","capacity_demand_timing_risk","biotech_CDMO_crowding"],"stage4c_evidence_fields":["post_peak_high_MAE_watch"],"price_data_source":"Songdaiki/stock-web","price_data_repo":"Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/237/237690/2024.csv","profile_path":"atlas/symbol_profiles/237/237690.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":57.64,"MFE_90D_pct":57.64,"MFE_180D_pct":92.36,"MFE_1Y_pct":92.36,"MFE_2Y_pct":92.36,"MAE_30D_pct":-4.62,"MAE_90D_pct":-4.62,"MAE_180D_pct":-4.62,"MAE_1Y_pct":-4.62,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-08-29","peak_price":120800,"drawdown_after_peak_pct":-40.4,"green_lateness_ratio":"0.33","four_b_local_peak_proximity":0.82,"four_b_full_window_peak_proximity":1.0,"four_b_timing_verdict":"oligo_CDMO_order_bridge_positive_but_full_window_4B_high_MAE_watch","four_b_evidence_type":"non_price_commercialization_backlog_margin_bridge","four_c_protection_label":"post_peak_high_MAE_watch","trigger_outcome_label":"oligo_CDMO_commercial_order_success_then_4B_watch","current_profile_verdict":"current_profile_correct_with_drawdown_guard","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"R7L76_C23_237690_20240129_OLIGO_CDMO_COMMERCIAL_ORDER_MARGIN_BRIDGE_entry","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"TRG_R7L76_C23_195940_20240129_PRODUCT_COMMERCIALIZATION_THEME_WITHOUT_DURABLE_GROWTH_BRIDGE","case_id":"R7L76_C23_195940_20240129_PRODUCT_COMMERCIALIZATION_THEME_WITHOUT_DURABLE_GROWTH_BRIDGE","symbol":"195940","company_name":"HK이노엔","round":"R7","loop":"76","large_sector_id":"L7_BIO_HEALTHCARE_MEDICAL","canonical_archetype_id":"C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION","fine_archetype_id":"C23_PRODUCT_COMMERCIALIZATION_THEME_WITHOUT_DURABLE_GROWTH_MARGIN_BRIDGE","deep_sub_archetype_id":"PHARMA_PRODUCT_COMMERCIALIZATION_AND_OVERSEAS_OPTIONALITY_WITHOUT_PRESCRIPTION_GROWTH_MARGIN_OR_CASHFLOW_CONVERSION","loop_objective":"coverage_gap_fill|counterexample_mining|stage2_actionable_bonus_stress_test|4B_non_price_requirement_stress_test|4C_thesis_break_timing_test|canonical_archetype_compression","trigger_type":"Stage2-Actionable","trigger_date":"2024-01-29","entry_date":"2024-01-29","entry_price":42950,"evidence_available_at_that_date":"source_proxy_pharma_product_commercialization_overseas_optionality_without_prescription_growth_margin_cashflow_bridge; evidence_url_pending","evidence_source":"source_proxy_pharma_product_commercialization_overseas_optionality_without_prescription_growth_margin_cashflow_bridge; evidence_url_pending","bridge_summary":"product commercialization/overseas optionality eventually produced MFE, but prescription growth, export royalty, margin and cashflow bridge were not durable enough; earlier MAE and later drawdown required 4B demotion","stage2_evidence_fields":["product_commercialization_theme","overseas_optionality","relative_strength"],"stage3_evidence_fields":[],"stage4b_evidence_fields":["delayed_MFE_peak","prescription_growth_bridge_absent","margin_cashflow_bridge_absent"],"stage4c_evidence_fields":["high_MAE_without_durable_commercialization_bridge"],"price_data_source":"Songdaiki/stock-web","price_data_repo":"Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/195/195940/2024.csv","profile_path":"atlas/symbol_profiles/195/195940.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":2.33,"MFE_90D_pct":2.44,"MFE_180D_pct":19.67,"MFE_1Y_pct":19.67,"MFE_2Y_pct":19.67,"MAE_30D_pct":-16.88,"MAE_90D_pct":-19.79,"MAE_180D_pct":-19.79,"MAE_1Y_pct":-19.79,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-09-23","peak_price":51400,"drawdown_after_peak_pct":-32.98,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":0.86,"four_b_full_window_peak_proximity":1.0,"four_b_timing_verdict":"product_commercialization_MFE_but_no_durable_growth_margin_bridge_keep_4B_high_MAE_watch","four_b_evidence_type":"commercialization_theme_without_durable_growth_margin_bridge","four_c_protection_label":"high_MAE_watch","trigger_outcome_label":"product_commercialization_theme_MFE_then_high_MAE_counterexample","current_profile_verdict":"current_profile_false_positive_if_green","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"R7L76_C23_195940_20240129_PRODUCT_COMMERCIALIZATION_THEME_WITHOUT_DURABLE_GROWTH_BRIDGE_entry","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
```

### 20.4 score_simulation rows

```jsonl
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"R7L76_C23_207940_20240129_CDMO_BACKLOG_COMMERCIALIZATION_MARGIN_BRIDGE","trigger_id":"TRG_R7L76_C23_207940_20240129_CDMO_BACKLOG_COMMERCIALIZATION_MARGIN_BRIDGE","symbol":"207940","large_sector_id":"L7_BIO_HEALTHCARE_MEDICAL","canonical_archetype_id":"C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION","raw_component_scores_before":{"commercialization_score":12,"backlog_or_sales_score":12,"capacity_utilization_score":11,"margin_cashflow_score":10,"relative_strength_score":10,"event_risk_penalty":6},"weighted_score_before":74,"stage_label_before":"Stage2-Actionable","raw_component_scores_after":{"commercialization_score":15,"backlog_or_sales_score":15,"capacity_utilization_score":13,"margin_cashflow_score":13,"relative_strength_score":8,"event_risk_penalty":9},"weighted_score_after":82,"stage_label_after":"Stage3-Yellow","changed_components":["commercialization_score","backlog_or_sales_score","capacity_utilization_score","margin_cashflow_score","relative_strength_score","event_risk_penalty"],"component_delta_explanation":"C23 row is promoted only because bio commercialization signal converts into backlog/sales, capacity utilization, margin and cashflow bridge; valuation/event drawdown keeps 4B active and blocks Green.","MFE_90D_pct":10.0,"MAE_90D_pct":-9.88,"score_return_alignment_label":"score_return_aligned","current_profile_verdict":"current_profile_correct_but_no_green"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"R7L76_C23_237690_20240129_OLIGO_CDMO_COMMERCIAL_ORDER_MARGIN_BRIDGE","trigger_id":"TRG_R7L76_C23_237690_20240129_OLIGO_CDMO_COMMERCIAL_ORDER_MARGIN_BRIDGE","symbol":"237690","large_sector_id":"L7_BIO_HEALTHCARE_MEDICAL","canonical_archetype_id":"C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION","raw_component_scores_before":{"commercialization_score":12,"backlog_or_sales_score":12,"capacity_utilization_score":11,"margin_cashflow_score":10,"relative_strength_score":10,"event_risk_penalty":6},"weighted_score_before":74,"stage_label_before":"Stage2-Actionable","raw_component_scores_after":{"commercialization_score":15,"backlog_or_sales_score":15,"capacity_utilization_score":13,"margin_cashflow_score":13,"relative_strength_score":8,"event_risk_penalty":9},"weighted_score_after":82,"stage_label_after":"Stage3-Yellow","changed_components":["commercialization_score","backlog_or_sales_score","capacity_utilization_score","margin_cashflow_score","relative_strength_score","event_risk_penalty"],"component_delta_explanation":"C23 row is promoted only because bio commercialization signal converts into backlog/sales, capacity utilization, margin and cashflow bridge; valuation/event drawdown keeps 4B active and blocks Green.","MFE_90D_pct":57.64,"MAE_90D_pct":-4.62,"score_return_alignment_label":"score_return_aligned","current_profile_verdict":"current_profile_correct_with_drawdown_guard"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"R7L76_C23_195940_20240129_PRODUCT_COMMERCIALIZATION_THEME_WITHOUT_DURABLE_GROWTH_BRIDGE","trigger_id":"TRG_R7L76_C23_195940_20240129_PRODUCT_COMMERCIALIZATION_THEME_WITHOUT_DURABLE_GROWTH_BRIDGE","symbol":"195940","large_sector_id":"L7_BIO_HEALTHCARE_MEDICAL","canonical_archetype_id":"C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION","raw_component_scores_before":{"commercialization_score":8,"backlog_or_sales_score":2,"capacity_utilization_score":1,"margin_cashflow_score":0,"relative_strength_score":8,"event_risk_penalty":8},"weighted_score_before":61,"stage_label_before":"Stage2-Actionable","raw_component_scores_after":{"commercialization_score":3,"backlog_or_sales_score":0,"capacity_utilization_score":0,"margin_cashflow_score":0,"relative_strength_score":3,"event_risk_penalty":16},"weighted_score_after":39,"stage_label_after":"Stage1-Watch_or_4B-HighMAE","changed_components":["commercialization_score","backlog_or_sales_score","capacity_utilization_score","margin_cashflow_score","relative_strength_score","event_risk_penalty"],"component_delta_explanation":"C23 guard demotes product-commercialization theme rows when sales/prescription growth, partner validation, margin and cashflow bridge are absent.","MFE_90D_pct":2.44,"MAE_90D_pct":-19.79,"score_return_alignment_label":"score_return_mixed","current_profile_verdict":"current_profile_false_positive_if_green"}
```

### 20.5 shadow_weight rows

```csv
row_type,axis,scope,large_sector_id,canonical_archetype_id,baseline_value,tested_value,delta,reason,backtest_effect,trigger_ids,calibration_usable_count,new_independent_case_count,counterexample_count,confidence,proposal_type,notes
shadow_weight,c23_requires_commercialization_backlog_sales_margin_cashflow_bridge,canonical_archetype_specific,L7_BIO_HEALTHCARE_MEDICAL,C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION,0,1,+1,"C23 bio commercialization rows should not promote toward Stage3-Yellow/Green unless regulatory/commercial signal converts into CDMO backlog, commercial batch revenue, prescription or product sales growth, partner validation, capacity utilization, margin, FCF or cashflow bridge","207940 and 237690 survive as guarded positives after CDMO/commercial order and margin bridge; 195940 is demoted because product-commercialization theme MFE lacked durable sales/margin/cashflow bridge","TRG_R7L76_C23_207940_20240129_CDMO_BACKLOG_COMMERCIALIZATION_MARGIN_BRIDGE|TRG_R7L76_C23_237690_20240129_OLIGO_CDMO_COMMERCIAL_ORDER_MARGIN_BRIDGE|TRG_R7L76_C23_195940_20240129_PRODUCT_COMMERCIALIZATION_THEME_WITHOUT_DURABLE_GROWTH_BRIDGE",3,3,1,medium,canonical_shadow_only,"not production; post-calibrated residual"
shadow_weight,c23_bio_commercialization_4b_high_mae_watch_guard,canonical_archetype_specific,L7_BIO_HEALTHCARE_MEDICAL,C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION,1,1,0,"Bio commercialization winners and product-theme false starts can peak before sales, capacity and margin durability are confirmed; local/full-window 4B and high-MAE watch should remain active","preserves 207940/237690 guarded positives while preventing 195940 commercialization-theme false positive","TRG_R7L76_C23_207940_20240129_CDMO_BACKLOG_COMMERCIALIZATION_MARGIN_BRIDGE|TRG_R7L76_C23_237690_20240129_OLIGO_CDMO_COMMERCIAL_ORDER_MARGIN_BRIDGE|TRG_R7L76_C23_195940_20240129_PRODUCT_COMMERCIALIZATION_THEME_WITHOUT_DURABLE_GROWTH_BRIDGE",3,3,1,medium,existing_axis_kept,"strengthens local/full-window 4B and high-MAE watch without global delta"
```

### 20.6 residual_contribution row

```jsonl
{"row_type":"residual_contribution","round":"R7","loop":"76","large_sector_id":"L7_BIO_HEALTHCARE_MEDICAL","canonical_archetype_id":"C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION","new_independent_case_count":3,"reused_case_count":0,"new_symbol_count":3,"new_trigger_family_count":3,"tested_existing_calibrated_axes":["stage2_actionable_evidence_bonus","price_only_blowoff_blocks_positive_stage","full_4b_requires_non_price_evidence","local_4b_watch_guard","high_MAE_guardrail"],"residual_error_types_found":["commercialization_theme_without_sales_margin_bridge","CDMO_commercialization_winner_needs_4B_watch","oligo_CDMO_winner_needs_drawdown_guard"],"loop_contribution_label":"canonical_archetype_rule_candidate","do_not_propose_new_weight_delta":false}
```

## 21. Deferred Coding Agent Handoff Prompt

### Purpose

You are now in the repository implementation phase. The attached Markdown files are v12 post-calibrated residual research outputs produced using the Songdaiki/stock-web OHLC atlas.

These MDs are not live candidate research. They are historical calibration research designed to extend the already-applied e2r_2_1_stock_web_calibrated profile.

Do not blindly apply every shadow row. Ingest the machine-readable rows and update the sector/canonical-archetype calibration ledger.

### R7-specific handling

- R7 maps to `L7_BIO_HEALTHCARE_MEDICAL`.
- This MD uses `C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION`.
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
- price-only/bio-commercialization-theme-only rows cannot promote Stage2/Stage3.
- If a v12 MD weakens an already applied axis, log it as residual counterexample rather than immediately reverting.
- Production scoring must not change unless the user explicitly asks for another promotion batch.

### Expected repository tasks

1. Parse case / trigger / score_simulation / shadow_weight / residual_contribution rows.
2. Validate stock-web price source fields.
3. Validate R7 direct L7 sector.
4. Validate canonical_archetype_id.
5. Validate novelty and reuse fields.
6. Deduplicate same_entry_group_id and reused cases.
7. Aggregate by large_sector_id and canonical_archetype_id.
8. Update sector_shadow_profile and archetype_shadow_profile only.
9. Preserve global calibrated profile unless explicitly promoted.
10. Report new independent cases, counterexamples, and residual error types.
11. Add tests that duplicate low-value loops cannot change weights.
12. Add validation that C23 bio commercialization rows cannot promote without regulatory-to-commercial conversion, CDMO backlog, commercial-batch revenue, prescription/product sales growth, partner validation, capacity utilization, margin conversion, FCF/cash conversion, or earnings revision tied to the asset.

### Expected output

- Concise implementation summary.
- Rows accepted/rejected.
- New sector/canonical archetype coverage.
- Existing axis strengthened/weakened/kept.
- No investment recommendation language.

## 22. Next Round State

```text
completed_round = R7
completed_loop = 76
next_round = R8
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
atlas/symbol_profiles/207/207940.json
atlas/symbol_profiles/237/237690.json
atlas/symbol_profiles/195/195940.json
atlas/ohlcv_tradable_by_symbol_year/207/207940/2024.csv
atlas/ohlcv_tradable_by_symbol_year/237/237690/2024.csv
atlas/ohlcv_tradable_by_symbol_year/195/195940/2024.csv
```

This loop continues loop 76 with R7 and adds 3 new independent C23 representative cases, 2 positives, 1 counterexample/watch case, and 1 canonical-archetype residual guard candidate for R7/L7.
