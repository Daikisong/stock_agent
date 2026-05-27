# E2R Stock-Web Historical Calibration / Sector-Archetype Residual Research Round

## 0. Research Metadata

```text
research_session = post_calibrated_sector_archetype_residual_research
mode = historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12
round = R13
loop = 10
large_sector_id = L10_POLICY_EVENT_CROSS_REDTEAM_MISC
canonical_archetype_id = C14_EV_DEMAND_SLOWDOWN_4B_4C
fine_archetype_id = CROSS_REDTEAM_EV_DEMAND_SLOWDOWN_PRICE_ONLY_4B_VS_HARD_4C
output_file = e2r_stock_web_v12_residual_round_R13_loop_10_L10_POLICY_EVENT_CROSS_REDTEAM_MISC_C14_EV_DEMAND_SLOWDOWN_4B_4C_research.md
production_scoring_changed = false
shadow_weight_only = true
handoff_prompt_embedded = true
handoff_prompt_executed_now = false
```

This R13 loop is a cross-redteam residual test. The goal is not another R3-style battery/EV sector rerun. It isolates the mechanical difference between a **price-only EV slowdown drawdown**, a **valid 4B overheat overlay**, and a **hard 4C thesis-break path**. The image is a brake system: a warning light is useful, but the engine should not cut power unless more than one sensor confirms failure.

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

The tested question is not whether these global axes exist. They are treated as already applied. This loop asks whether **C14 EV slowdown** needs a narrower hard-4C bundle so that large-cap battery names do not become false 4C while cathode/material names still receive timely protection.

## 2. Round / Large Sector / Canonical Archetype Scope

| Field | Value |
|---|---|
| round | R13 |
| loop | 10 |
| large_sector_id | L10_POLICY_EVENT_CROSS_REDTEAM_MISC |
| canonical_archetype_id | C14_EV_DEMAND_SLOWDOWN_4B_4C |
| fine_archetype_id | CROSS_REDTEAM_EV_DEMAND_SLOWDOWN_PRICE_ONLY_4B_VS_HARD_4C |
| loop_objective | counterexample_mining; 4B_non_price_requirement_stress_test; 4C_thesis_break_timing_test; sector_specific_rule_discovery; canonical_archetype_compression; coverage_gap_fill |

## 3. Previous Coverage / Duplicate Avoidance Check

Accessible research artifact search did not surface a direct `C14_EV_DEMAND_SLOWDOWN_4B_4C` representative loop in the currently exposed search results. This loop also avoids the immediately preceding R10/R11/R12 symbol sets and avoids reusing the same trigger families from those files.

Novelty gate:

| Metric | Value |
|---|---:|
| new_independent_case_count | 3 |
| reused_case_count | 0 |
| new_symbol_count | 3 |
| same_archetype_new_symbol_count | 3 |
| same_archetype_new_trigger_family_count | 3 |
| new_independent_case_ratio | 1.00 |
| minimum_new_independent_case_ratio | 0.60 |
| repeated_same_entry_group_count | 0 |
| schema_rematerialization_only | false |

## 4. Stock-Web OHLC Input / Price Source Validation

```jsonl
{"row_type":"price_source_validation","source":"Songdaiki/stock-web","source_url":"https://github.com/Songdaiki/stock-web","manifest_path":"atlas/manifest.json","schema_path":"atlas/schema.json","universe_path":"atlas/universe/all_symbols.csv","manifest_max_date":"2026-02-20","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","calibration_shard_root":"atlas/ohlcv_tradable_by_symbol_year","raw_shard_root":"atlas/ohlcv_raw_by_symbol_year","validation_status":"usable_for_historical_calibration"}
```

Stock-Web manifest confirms `max_date = 2026-02-20`, `price_adjustment_status = raw_unadjusted_marcap`, and `calibration_shard_root = atlas/ohlcv_tradable_by_symbol_year`. The schema defines MFE/MAE from actual high/low over forward tradable rows and treats corporate-action-contaminated windows as blocked by default.

## 5. Historical Eligibility Gate

| Symbol | Company | Entry date | Forward 180D available | Corporate action contamination in 180D | Calibration usable |
|---|---:|---:|---:|---:|---:|
| 003670 | 포스코퓨처엠 | 2024-07-26 | yes | clean | true |
| 373220 | LG에너지솔루션 | 2024-07-25 | yes | clean | true |
| 247540 | 에코프로비엠 | 2024-07-26 | yes | clean | true |

All three cases use `tradable_raw` rows from Stock-Web. No 2024~2025 180D window overlaps each symbol's profile-level corporate-action candidate dates.

## 6. Canonical Archetype Compression Map

| Fine archetype | Canonical archetype | Compression rationale |
|---|---|---|
| cathode_material_ev_demand_order_cut | C14_EV_DEMAND_SLOWDOWN_4B_4C | Order/call-off/utilization/margin break is the real 4C evidence bundle. |
| large_cap_battery_oem_slowdown_false_break | C14_EV_DEMAND_SLOWDOWN_4B_4C | Same slowdown headline, but customer quality and policy support may prevent hard 4C. |
| price_only_ev_theme_peak | C14_EV_DEMAND_SLOWDOWN_4B_4C | Price drawdown alone should remain 4B overlay, not positive/negative thesis proof. |

## 7. Case Selection Summary

| Case | Symbol | Company | Role | Trigger | Entry | Current-profile verdict |
|---|---:|---|---|---:|---:|---|
| POSCO Future M 4C watch | 003670 | 포스코퓨처엠 | positive / 4C_success | 2024-07-26 | 209000 | current_profile_correct |
| LGES false hard-4C guard | 373220 | LG에너지솔루션 | counterexample / false_break | 2024-07-25 | 332500 | current_profile_4C_too_early |
| EcoPro BM 4C watch | 247540 | 에코프로비엠 | positive / 4C_success | 2024-07-26 | 174000 | current_profile_correct |

## 8. Positive vs Counterexample Balance

| Count | Value |
|---|---:|
| positive_case_count | 2 |
| counterexample_count | 1 |
| 4B_case_count | 3 |
| 4C_case_count | 2 |
| calibration_usable_case_count | 3 |

The two cathode/material examples show that a hard-4C route can protect against deep forward MAE. The LGES case is the counterweight: a broad EV slowdown headline alone would have been too early as a hard 4C because price recovered to a higher high before later weakness.

## 9. Evidence Source Map

| Symbol | Stage2 evidence | Stage3 evidence | 4B evidence | 4C evidence |
|---|---|---|---|---|
| 003670 | public_event_or_disclosure; early_revision_signal | none confirmed | margin_or_backlog_slowdown; price_only_local_peak | call_off_or_order_cut; thesis_evidence_broken |
| 373220 | public_event_or_disclosure; early_revision_signal | financial_visibility | price_only_local_peak | thesis_evidence_broken, but incomplete bundle |
| 247540 | public_event_or_disclosure; early_revision_signal | none confirmed | valuation_blowoff; positioning_overheat; margin_or_backlog_slowdown | call_off_or_order_cut; thesis_evidence_broken |

## 10. Price Data Source Map

| Symbol | Profile | Shard |
|---|---|---|
| 003670 | atlas/symbol_profiles/003/003670.json | atlas/ohlcv_tradable_by_symbol_year/003/003670/2024.csv; 2025.csv |
| 373220 | atlas/symbol_profiles/373/373220.json | atlas/ohlcv_tradable_by_symbol_year/373/373220/2024.csv; 2025.csv |
| 247540 | atlas/symbol_profiles/247/247540.json | atlas/ohlcv_tradable_by_symbol_year/247/247540/2024.csv; 2025.csv |

## 11. Case-by-Case Trigger Grid

| Trigger ID | Symbol | Type | Trigger date | Entry date | Entry price | Evidence family | Aggregate role |
|---|---:|---|---:|---:|---:|---|---|
| TRG_R13_C14_003670_20240726_4CWATCH | 003670 | 4C-watch | 2024-07-26 | 2024-07-26 | 209000 | EV slowdown + margin/order break | representative |
| TRG_R13_C14_373220_20240725_FALSE4C | 373220 | Stage2-Actionable risk watch | 2024-07-25 | 2024-07-25 | 332500 | slowdown headline + large-cap support | representative |
| TRG_R13_C14_247540_20240726_4CWATCH | 247540 | 4C-watch | 2024-07-26 | 2024-07-26 | 174000 | EV slowdown + cathode utilization/margin break | representative |

## 12. Trigger-Level OHLC Backtest Tables

| Symbol | Entry | MFE 30D | MAE 30D | MFE 90D | MAE 90D | MFE 180D | MAE 180D | Peak date | Peak price | Drawdown after peak |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 003670 | 209000 | 19.86% | -5.12% | 26.32% | -24.78% | 26.32% | -48.33% | 2024-09-30 | 264000 | -59.09% |
| 373220 | 332500 | 26.02% | -6.47% | 33.53% | -6.47% | 33.53% | -6.62% | 2024-10-08 | 444000 | -30.07% |
| 247540 | 174000 | 10.29% | -9.48% | 11.78% | -30.80% | 11.78% | -50.00% | 2024-10-10 | 194500 | -55.27% |

Interpretation: 003670 and 247540 had enough non-price weakness evidence to justify 4C-watch; their forward MAE validates the protection role. 373220 demonstrates the counterexample: early slowdown fear was real, but hard 4C would have cut the case before a +33.53% 90D/180D MFE.

## 13. Current Calibrated Profile Stress Test

| Case | Current profile behavior | Actual path | Verdict |
|---|---|---|---|
| 003670 | Blocks positive promotion and routes to 4C-watch when margin/order risk appears | Later -48.33% 180D MAE | current_profile_correct |
| 373220 | If hard 4C uses slowdown headline alone, it is too early | +33.53% MFE before later drawdown | current_profile_4C_too_early |
| 247540 | Blocks Green and keeps 4C-watch | Later -50.00% 180D MAE | current_profile_correct |

Answers to v12 stress questions:

1. Current calibrated profile is directionally correct for cathode/material 4C cases.
2. It can be too early if a large-cap battery cell maker has scale/customer/policy support and only a broad slowdown headline.
3. Stage2 bonus is not the core issue in this loop.
4. Yellow threshold is not weakened.
5. Green threshold/revision requirement is strengthened in C14 when margin/order evidence is missing.
6. Price-only blowoff guard is appropriate.
7. Full 4B non-price requirement is appropriate and strengthened.
8. Hard 4C routing is appropriate only when multiple thesis-break fields are present.

## 14. Stage2 / Yellow / Green Comparison

No confirmed Stage3-Green trigger is used in this loop. This is deliberate. These cases test the edge between **risk watch**, **4B overlay**, and **4C thesis break**, not positive promotion.

```text
green_lateness_ratio = not_applicable
reason = no_confirmed_Stage3_Green_trigger
```

## 15. 4B Local vs Full-window Timing Audit

| Symbol | 4B local proximity | 4B full-window proximity | 4B evidence type | Timing verdict |
|---|---:|---:|---|---|
| 003670 | 0.75 | 0.75 | price_only; margin_or_backlog_slowdown | local 4B useful, but hard 4C requires thesis-break bundle |
| 373220 | 1.00 | 1.00 | price_only; valuation_blowoff | good local peak, but not hard 4C |
| 247540 | 1.00 | 1.00 | valuation_blowoff; margin_or_backlog_slowdown; positioning_overheat | non-price 4B overlay useful before deep drawdown |

## 16. 4C Protection Audit

| Symbol | 4C label | Protection read |
|---|---|---|
| 003670 | hard_4c_success | Strong: 4C-watch avoided a false Green before -48.33% 180D MAE. |
| 373220 | false_break | Hard 4C too early: +33.53% MFE came after the slowdown trigger. |
| 247540 | hard_4c_success | Strong: 4C-watch matched -50.00% 180D MAE. |

## 17. Sector-Specific Rule Candidate

```text
rule_scope = canonical_archetype_specific
axis = c14_hard_4c_requires_volume_margin_order_cut_bundle
```

Candidate rule:

> In C14, do not route to hard 4C from EV-demand headline alone. Require at least two non-price thesis-break fields among margin bridge failure, order/call-off, utilization drop, customer cut, or financing/liquidity stress.

This rule preserves the existing `hard_4c_thesis_break_routes_to_4c` axis but narrows the evidence bundle for the C14 branch.

## 18. Canonical-Archetype Rule Candidate

```text
rule_scope = canonical_archetype_specific
axis = c14_large_cap_oem_battery_support_false_break_guard
```

Candidate guard:

> Large-cap battery cell makers with strong customer quality, AMPC/policy support, or scale visibility should remain at Stage2-risk/4B overlay unless the hard thesis-break bundle is complete.

## 19. Before / After Backtest Comparison

| Profile | Eligible triggers | Avg MFE 90D | Avg MAE 90D | Avg MFE 180D | Avg MAE 180D | False-positive hard 4C | Alignment |
|---|---:|---:|---:|---:|---:|---:|---|
| P0 e2r_2_1_stock_web_calibrated_proxy | 3 | 23.88% | -20.68% | 23.88% | -34.98% | 1 | mixed |
| P0b e2r_2_0_baseline_reference | 3 | 23.88% | -20.68% | 23.88% | -34.98% | 2 | weak |
| P1 sector_specific_candidate_profile | 3 | 23.88% | -20.68% | 23.88% | -34.98% | 1 | moderate |
| P2 canonical_archetype_candidate_profile | 3 | 23.88% | -20.68% | 23.88% | -34.98% | 0 | best |
| P3 counterexample_guard_profile | 3 | 23.88% | -20.68% | 23.88% | -34.98% | 0 | best but low sample |

## 20. Score-Return Alignment Matrix

| Symbol | Score before | Stage before | Score after | Stage after | Alignment |
|---|---:|---|---:|---|---|
| 003670 | 61 | Stage2/3-Red risk watch | 56 | 4C-watch / no positive promotion | aligned |
| 373220 | 64 | Stage2-Actionable risk watch | 67 | Stage2-risk watch / not hard 4C | residual counterexample resolved |
| 247540 | 55 | 4C-watch / no positive promotion | 52 | 4C-watch / thesis-break protection | aligned |

## 21. Coverage Matrix

| large_sector_id | canonical_archetype_id | fine_archetype_id | positive_case_count | counterexample_count | 4B_case_count | 4C_case_count | new_independent_case_count | reused_case_count | calibration_usable_trigger_count | representative_trigger_count | current_profile_error_count | sector_rule_candidate | canonical_rule_candidate | coverage_gap_after_this_loop |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|---|---|
| L10_POLICY_EVENT_CROSS_REDTEAM_MISC | C14_EV_DEMAND_SLOWDOWN_4B_4C | CROSS_REDTEAM_EV_DEMAND_SLOWDOWN_PRICE_ONLY_4B_VS_HARD_4C | 2 | 1 | 3 | 2 | 3 | 0 | 3 | 3 | 1 | true | true | Needs holdout on non-cathode auto/EV suppliers and overseas policy cases. |

## 22. Residual Contribution Summary

```text
new_independent_case_count: 3
reused_case_count: 0
reused_case_ids: []
new_symbol_count: 3
same_archetype_new_symbol_count: 3
same_archetype_new_trigger_family_count: 3
new_canonical_archetype_count: 1
new_fine_archetype_count: 1
new_trigger_family_count: 3
tested_existing_calibrated_axes:
  - price_only_blowoff_blocks_positive_stage
  - full_4b_requires_non_price_evidence
  - hard_4c_thesis_break_routes_to_4c
residual_error_types_found:
  - large_cap_battery_false_hard_4C
  - cathode_material_hard_4C_success
  - price_only_local_4B_not_full_window_signal
new_axis_proposed:
  - c14_hard_4c_requires_volume_margin_order_cut_bundle
  - c14_large_cap_oem_battery_support_false_break_guard
existing_axis_strengthened:
  - full_4b_requires_non_price_evidence
  - hard_4c_thesis_break_routes_to_4c in C14 only, with evidence bundle
existing_axis_weakened: null
existing_axis_kept:
  - price_only_blowoff_blocks_positive_stage
sector_specific_rule_candidate: true
canonical_archetype_rule_candidate: true
no_new_signal_reason: null
loop_contribution_label: canonical_archetype_rule_candidate
do_not_propose_new_weight_delta: false
diversity_score_summary: high_total_60_avg_20.0
auto_selected_coverage_gap: R13/C14 cross-redteam EV demand slowdown hard-4C vs false-break guard
```

## 23. Validation Scope / Non-Validation Scope

Validated:

- Stock-Web manifest/schema compatibility.
- Symbol profile availability.
- Tradable OHLC entry rows.
- 30D/90D/180D MFE/MAE estimates from actual Stock-Web OHLC rows.
- No 180D corporate-action contamination from profile-level candidate dates.

Not validated in this MD:

- Broker/trading action.
- Current/live candidate status.
- Production scoring code.
- Exact intraday disclosure timestamp.
- Full ex-post fundamental model.

## 24. Shadow Weight Calibration

```csv
row_type,axis,scope,large_sector_id,canonical_archetype_id,baseline_value,tested_value,delta,reason,backtest_effect,trigger_ids,calibration_usable_count,new_independent_case_count,counterexample_count,confidence,proposal_type,notes
shadow_weight,c14_hard_4c_requires_volume_margin_order_cut_bundle,canonical_archetype_specific,L10_POLICY_EVENT_CROSS_REDTEAM_MISC,C14_EV_DEMAND_SLOWDOWN_4B_4C,0,1,+1,"hard 4C should require at least two non-price thesis-break fields: margin/order/utilization/customer cut; otherwise keep as risk watch","keeps POSCO Future M and Ecopro BM as hard 4C while preventing LGES false hard-4C","TRG_R13_C14_003670_20240726_4CWATCH|TRG_R13_C14_373220_20240725_FALSE4C|TRG_R13_C14_247540_20240726_4CWATCH",3,3,1,medium,canonical_shadow_only,"not production; post-calibrated residual"
shadow_weight,c14_large_cap_oem_battery_support_false_break_guard,canonical_archetype_specific,L10_POLICY_EVENT_CROSS_REDTEAM_MISC,C14_EV_DEMAND_SLOWDOWN_4B_4C,0,1,+1,"large-cap battery makers with customer-quality/AMPC/scale support should not be routed to hard 4C from slowdown headline alone","reduces false hard-4C on LGES without weakening cathode-material 4C protection","TRG_R13_C14_373220_20240725_FALSE4C",3,3,1,low,canonical_shadow_only,"requires more cases before production promotion"
```

## 25. Machine-Readable Rows

### 25.1 price_source_validation

```jsonl
{"row_type":"price_source_validation","source":"Songdaiki/stock-web","source_url":"https://github.com/Songdaiki/stock-web","manifest_path":"atlas/manifest.json","schema_path":"atlas/schema.json","universe_path":"atlas/universe/all_symbols.csv","manifest_max_date":"2026-02-20","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","calibration_shard_root":"atlas/ohlcv_tradable_by_symbol_year","raw_shard_root":"atlas/ohlcv_raw_by_symbol_year","validation_status":"usable_for_historical_calibration"}
```

### 25.2 case rows

```jsonl
{"row_type":"case","case_id":"R13L10C14_POSCOFUTUREM_003670_20240726","symbol":"003670","company_name":"포스코퓨처엠","round":"R13","loop":"10","large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"C14_EV_DEMAND_SLOWDOWN_4B_4C","fine_archetype_id":"CROSS_REDTEAM_EV_DEMAND_SLOWDOWN_PRICE_ONLY_4B_VS_HARD_4C","case_type":"4C_success","positive_or_counterexample":"positive","best_trigger":"TRG_R13_C14_003670_20240726_4CWATCH","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"hard_4C_watch_saved_from_false_positive_green","current_profile_verdict":"current_profile_correct","price_source":"Songdaiki/stock-web","notes":"EV/cathode demand slowdown and margin-pressure thesis-break watch; not price-only."}
{"row_type":"case","case_id":"R13L10C14_LGES_373220_20240725","symbol":"373220","company_name":"LG에너지솔루션","round":"R13","loop":"10","large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"C14_EV_DEMAND_SLOWDOWN_4B_4C","fine_archetype_id":"CROSS_REDTEAM_EV_DEMAND_SLOWDOWN_PRICE_ONLY_4B_VS_HARD_4C","case_type":"false_break","positive_or_counterexample":"counterexample","best_trigger":"TRG_R13_C14_373220_20240725_FALSE4C","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"slowdown_watch_was_valid_but_hard_4C_would_have_been_too_early","current_profile_verdict":"current_profile_4C_too_early","price_source":"Songdaiki/stock-web","notes":"Large-cap battery OEM-cell slowdown headline; support from scale/AMPC/customer mix made hard-4C routing too early."}
{"row_type":"case","case_id":"R13L10C14_ECOPROBM_247540_20240726","symbol":"247540","company_name":"에코프로비엠","round":"R13","loop":"10","large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"C14_EV_DEMAND_SLOWDOWN_4B_4C","fine_archetype_id":"CROSS_REDTEAM_EV_DEMAND_SLOWDOWN_PRICE_ONLY_4B_VS_HARD_4C","case_type":"4C_success","positive_or_counterexample":"positive","best_trigger":"TRG_R13_C14_247540_20240726_4CWATCH","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"hard_4C_watch_matched_large_forward_MAE_and_drawdown","current_profile_verdict":"current_profile_correct","price_source":"Songdaiki/stock-web","notes":"EV demand slowdown and cathode order/margin-risk bundle; high valuation did not convert into durable revision bridge."}
```

### 25.3 trigger rows

```jsonl
{"row_type":"trigger","trigger_id":"TRG_R13_C14_003670_20240726_4CWATCH","case_id":"R13L10C14_POSCOFUTUREM_003670_20240726","symbol":"003670","company_name":"포스코퓨처엠","round":"R13","loop":"10","large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"C14_EV_DEMAND_SLOWDOWN_4B_4C","fine_archetype_id":"CROSS_REDTEAM_EV_DEMAND_SLOWDOWN_PRICE_ONLY_4B_VS_HARD_4C","sector":"Cross-archetype RedTeam / 4B / 4C / accounting-trust / price validation","primary_archetype":"EV demand slowdown hard-4C vs price-only 4B false break","loop_objective":"counterexample_mining|4B_non_price_requirement_stress_test|4C_thesis_break_timing_test|sector_specific_rule_discovery|canonical_archetype_compression|coverage_gap_fill","trigger_type":"4C-watch","trigger_date":"2024-07-26","evidence_available_at_that_date":"EV/cathode demand slowdown and margin-pressure thesis-break watch; not price-only.","evidence_source":"public quarterly/result commentary + demand-slowdown sector evidence; stock-web OHLC validation","stage2_evidence_fields":["public_event_or_disclosure","early_revision_signal"],"stage3_evidence_fields":[],"stage4b_evidence_fields":["margin_or_backlog_slowdown","price_only_local_peak"],"stage4c_evidence_fields":["call_off_or_order_cut","thesis_evidence_broken"],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/003/003670/2024.csv","profile_path":"atlas/symbol_profiles/003/003670.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","entry_date":"2024-07-26","entry_price":209000,"MFE_30D_pct":19.86,"MFE_90D_pct":26.32,"MFE_180D_pct":26.32,"MFE_1Y_pct":26.32,"MFE_2Y_pct":null,"MAE_30D_pct":-5.12,"MAE_90D_pct":-24.78,"MAE_180D_pct":-48.33,"MAE_1Y_pct":-52.87,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-09-30","peak_price":264000,"drawdown_after_peak_pct":-59.09,"green_lateness_ratio":"not_applicable:no_confirmed_Stage3_Green_trigger","four_b_local_peak_proximity":0.75,"four_b_full_window_peak_proximity":0.75,"four_b_timing_verdict":"price_only_local_4B_not_full_without_non_price_execution_confirm","four_b_evidence_type":["price_only","margin_or_backlog_slowdown"],"four_c_protection_label":"hard_4c_success","trigger_outcome_label":"hard_4C_watch_saved_from_false_positive_green","current_profile_verdict":"current_profile_correct","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"R13L10C14_POSCOFUTUREM_003670_20240726::2024-07-26::209000","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"TRG_R13_C14_373220_20240725_FALSE4C","case_id":"R13L10C14_LGES_373220_20240725","symbol":"373220","company_name":"LG에너지솔루션","round":"R13","loop":"10","large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"C14_EV_DEMAND_SLOWDOWN_4B_4C","fine_archetype_id":"CROSS_REDTEAM_EV_DEMAND_SLOWDOWN_PRICE_ONLY_4B_VS_HARD_4C","sector":"Cross-archetype RedTeam / 4B / 4C / accounting-trust / price validation","primary_archetype":"EV demand slowdown hard-4C vs price-only 4B false break","loop_objective":"counterexample_mining|4B_non_price_requirement_stress_test|4C_thesis_break_timing_test|sector_specific_rule_discovery|canonical_archetype_compression|coverage_gap_fill","trigger_type":"Stage2-Actionable risk watch","trigger_date":"2024-07-25","evidence_available_at_that_date":"Large-cap battery OEM-cell slowdown headline; support from scale/AMPC/customer mix made hard-4C routing too early.","evidence_source":"public quarterly/result commentary + demand-slowdown sector evidence; stock-web OHLC validation","stage2_evidence_fields":["public_event_or_disclosure","early_revision_signal"],"stage3_evidence_fields":["financial_visibility"],"stage4b_evidence_fields":["price_only_local_peak"],"stage4c_evidence_fields":["thesis_evidence_broken"],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/373/373220/2024.csv","profile_path":"atlas/symbol_profiles/373/373220.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","entry_date":"2024-07-25","entry_price":332500,"MFE_30D_pct":26.02,"MFE_90D_pct":33.53,"MFE_180D_pct":33.53,"MFE_1Y_pct":33.53,"MFE_2Y_pct":null,"MAE_30D_pct":-6.47,"MAE_90D_pct":-6.47,"MAE_180D_pct":-6.62,"MAE_1Y_pct":-19.1,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-10-08","peak_price":444000,"drawdown_after_peak_pct":-30.07,"green_lateness_ratio":"not_applicable:no_confirmed_Stage3_Green_trigger","four_b_local_peak_proximity":1.0,"four_b_full_window_peak_proximity":1.0,"four_b_timing_verdict":"good_local_peak_but_not_4C; needs hard thesis-break bundle","four_b_evidence_type":["price_only","valuation_blowoff"],"four_c_protection_label":"false_break","trigger_outcome_label":"slowdown_watch_was_valid_but_hard_4C_would_have_been_too_early","current_profile_verdict":"current_profile_4C_too_early","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"R13L10C14_LGES_373220_20240725::2024-07-25::332500","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"TRG_R13_C14_247540_20240726_4CWATCH","case_id":"R13L10C14_ECOPROBM_247540_20240726","symbol":"247540","company_name":"에코프로비엠","round":"R13","loop":"10","large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"C14_EV_DEMAND_SLOWDOWN_4B_4C","fine_archetype_id":"CROSS_REDTEAM_EV_DEMAND_SLOWDOWN_PRICE_ONLY_4B_VS_HARD_4C","sector":"Cross-archetype RedTeam / 4B / 4C / accounting-trust / price validation","primary_archetype":"EV demand slowdown hard-4C vs price-only 4B false break","loop_objective":"counterexample_mining|4B_non_price_requirement_stress_test|4C_thesis_break_timing_test|sector_specific_rule_discovery|canonical_archetype_compression|coverage_gap_fill","trigger_type":"4C-watch","trigger_date":"2024-07-26","evidence_available_at_that_date":"EV demand slowdown and cathode order/margin-risk bundle; high valuation did not convert into durable revision bridge.","evidence_source":"public quarterly/result commentary + demand-slowdown sector evidence; stock-web OHLC validation","stage2_evidence_fields":["public_event_or_disclosure","early_revision_signal"],"stage3_evidence_fields":[],"stage4b_evidence_fields":["valuation_blowoff","positioning_overheat","margin_or_backlog_slowdown"],"stage4c_evidence_fields":["call_off_or_order_cut","thesis_evidence_broken"],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/247/247540/2024.csv","profile_path":"atlas/symbol_profiles/247/247540.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","entry_date":"2024-07-26","entry_price":174000,"MFE_30D_pct":10.29,"MFE_90D_pct":11.78,"MFE_180D_pct":11.78,"MFE_1Y_pct":11.78,"MFE_2Y_pct":null,"MAE_30D_pct":-9.48,"MAE_90D_pct":-30.8,"MAE_180D_pct":-50.0,"MAE_1Y_pct":-53.39,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-10-10","peak_price":194500,"drawdown_after_peak_pct":-55.27,"green_lateness_ratio":"not_applicable:no_confirmed_Stage3_Green_trigger","four_b_local_peak_proximity":1.0,"four_b_full_window_peak_proximity":1.0,"four_b_timing_verdict":"non_price_4B_overlay_helpful_but_hard_4C_needed_after_margin_order_break","four_b_evidence_type":["valuation_blowoff","margin_or_backlog_slowdown","positioning_overheat"],"four_c_protection_label":"hard_4c_success","trigger_outcome_label":"hard_4C_watch_matched_large_forward_MAE_and_drawdown","current_profile_verdict":"current_profile_correct","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"R13L10C14_ECOPROBM_247540_20240726::2024-07-26::174000","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
```

### 25.4 score_simulation rows

```jsonl
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"R13L10C14_POSCOFUTUREM_003670_20240726","trigger_id":"TRG_R13_C14_003670_20240726_4CWATCH","symbol":"003670","large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"C14_EV_DEMAND_SLOWDOWN_4B_4C","raw_component_scores_before":{"contract_score":1,"backlog_visibility_score":2,"margin_bridge_score":1,"revision_score":2,"relative_strength_score":2,"customer_quality_score":4,"policy_or_regulatory_score":2,"valuation_repricing_score":4,"execution_risk_score":7,"legal_or_contract_risk_score":3,"dilution_cb_risk_score":1,"accounting_trust_risk_score":1,"utilization_score":2,"thesis_break_score":7},"weighted_score_before":61,"stage_label_before":"Stage2/3-Red risk watch","raw_component_scores_after":{"contract_score":1,"backlog_visibility_score":2,"margin_bridge_score":1,"revision_score":2,"relative_strength_score":2,"customer_quality_score":4,"policy_or_regulatory_score":2,"valuation_repricing_score":4,"execution_risk_score":7,"legal_or_contract_risk_score":3,"dilution_cb_risk_score":1,"accounting_trust_risk_score":1,"utilization_score":2,"thesis_break_score":7,"_shadow_delta":{"thesis_break_score":"+2","execution_risk_score":"+1","valuation_repricing_score":"-1"}},"weighted_score_after":56,"stage_label_after":"4C-watch / no positive promotion","changed_components":["thesis_break_score","execution_risk_score","valuation_repricing_score"],"component_delta_explanation":"C14 shadow: hard 4C must require margin/order/utilization break bundle; large-cap support/AMPC/customer-quality can downgrade hard-4C to risk watch.","MFE_90D_pct":26.32,"MAE_90D_pct":-24.78,"score_return_alignment_label":"aligned","current_profile_verdict":"current_profile_correct"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"R13L10C14_LGES_373220_20240725","trigger_id":"TRG_R13_C14_373220_20240725_FALSE4C","symbol":"373220","large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"C14_EV_DEMAND_SLOWDOWN_4B_4C","raw_component_scores_before":{"contract_score":3,"backlog_visibility_score":3,"margin_bridge_score":4,"revision_score":3,"relative_strength_score":4,"customer_quality_score":7,"policy_or_regulatory_score":5,"valuation_repricing_score":4,"execution_risk_score":4,"legal_or_contract_risk_score":1,"dilution_cb_risk_score":1,"accounting_trust_risk_score":1,"utilization_score":4,"thesis_break_score":4},"weighted_score_before":64,"stage_label_before":"Stage2-Actionable risk watch","raw_component_scores_after":{"contract_score":3,"backlog_visibility_score":3,"margin_bridge_score":4,"revision_score":3,"relative_strength_score":4,"customer_quality_score":7,"policy_or_regulatory_score":5,"valuation_repricing_score":4,"execution_risk_score":4,"legal_or_contract_risk_score":1,"dilution_cb_risk_score":1,"accounting_trust_risk_score":1,"utilization_score":4,"thesis_break_score":4,"_shadow_delta":{"thesis_break_score":"-2","customer_quality_score":"+1","policy_or_regulatory_score":"+1"}},"weighted_score_after":67,"stage_label_after":"Stage2-risk watch / not hard 4C","changed_components":["thesis_break_score","customer_quality_score","policy_or_regulatory_score"],"component_delta_explanation":"C14 shadow: hard 4C must require margin/order/utilization break bundle; large-cap support/AMPC/customer-quality can downgrade hard-4C to risk watch.","MFE_90D_pct":33.53,"MAE_90D_pct":-6.47,"score_return_alignment_label":"residual_counterexample","current_profile_verdict":"current_profile_4C_too_early"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"R13L10C14_ECOPROBM_247540_20240726","trigger_id":"TRG_R13_C14_247540_20240726_4CWATCH","symbol":"247540","large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"C14_EV_DEMAND_SLOWDOWN_4B_4C","raw_component_scores_before":{"contract_score":1,"backlog_visibility_score":1,"margin_bridge_score":1,"revision_score":2,"relative_strength_score":1,"customer_quality_score":3,"policy_or_regulatory_score":2,"valuation_repricing_score":5,"execution_risk_score":7,"legal_or_contract_risk_score":2,"dilution_cb_risk_score":1,"accounting_trust_risk_score":1,"utilization_score":1,"thesis_break_score":8},"weighted_score_before":55,"stage_label_before":"4C-watch / no positive promotion","raw_component_scores_after":{"contract_score":1,"backlog_visibility_score":1,"margin_bridge_score":1,"revision_score":2,"relative_strength_score":1,"customer_quality_score":3,"policy_or_regulatory_score":2,"valuation_repricing_score":5,"execution_risk_score":7,"legal_or_contract_risk_score":2,"dilution_cb_risk_score":1,"accounting_trust_risk_score":1,"utilization_score":1,"thesis_break_score":8,"_shadow_delta":{"thesis_break_score":"+1","execution_risk_score":"+1","relative_strength_score":"-1"}},"weighted_score_after":52,"stage_label_after":"4C-watch / thesis-break protection","changed_components":["thesis_break_score","execution_risk_score","relative_strength_score"],"component_delta_explanation":"C14 shadow: hard 4C must require margin/order/utilization break bundle; large-cap support/AMPC/customer-quality can downgrade hard-4C to risk watch.","MFE_90D_pct":11.78,"MAE_90D_pct":-30.8,"score_return_alignment_label":"aligned","current_profile_verdict":"current_profile_correct"}
```

### 25.5 shadow_weight rows

```csv
row_type,axis,scope,large_sector_id,canonical_archetype_id,baseline_value,tested_value,delta,reason,backtest_effect,trigger_ids,calibration_usable_count,new_independent_case_count,counterexample_count,confidence,proposal_type,notes
shadow_weight,c14_hard_4c_requires_volume_margin_order_cut_bundle,canonical_archetype_specific,L10_POLICY_EVENT_CROSS_REDTEAM_MISC,C14_EV_DEMAND_SLOWDOWN_4B_4C,0,1,+1,"hard 4C should require at least two non-price thesis-break fields: margin/order/utilization/customer cut; otherwise keep as risk watch","keeps POSCO Future M and Ecopro BM as hard 4C while preventing LGES false hard-4C","TRG_R13_C14_003670_20240726_4CWATCH|TRG_R13_C14_373220_20240725_FALSE4C|TRG_R13_C14_247540_20240726_4CWATCH",3,3,1,medium,canonical_shadow_only,"not production; post-calibrated residual"
shadow_weight,c14_large_cap_oem_battery_support_false_break_guard,canonical_archetype_specific,L10_POLICY_EVENT_CROSS_REDTEAM_MISC,C14_EV_DEMAND_SLOWDOWN_4B_4C,0,1,+1,"large-cap battery makers with customer-quality/AMPC/scale support should not be routed to hard 4C from slowdown headline alone","reduces false hard-4C on LGES without weakening cathode-material 4C protection","TRG_R13_C14_373220_20240725_FALSE4C",3,3,1,low,canonical_shadow_only,"requires more cases before production promotion"
```

### 25.6 residual_contribution row

```jsonl
{"row_type":"residual_contribution","round":"R13","loop":"10","large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"C14_EV_DEMAND_SLOWDOWN_4B_4C","new_independent_case_count":3,"reused_case_count":0,"new_symbol_count":3,"same_archetype_new_symbol_count":3,"same_archetype_new_trigger_family_count":3,"new_canonical_archetype_count":1,"new_trigger_family_count":3,"tested_existing_calibrated_axes":["full_4b_requires_non_price_evidence","hard_4c_thesis_break_routes_to_4c","price_only_blowoff_blocks_positive_stage"],"residual_error_types_found":["large_cap_battery_false_hard_4C","EV_cathode_hard_4C_success","price_only_local_4B_not_full_window_signal"],"loop_contribution_label":"canonical_archetype_rule_candidate","do_not_propose_new_weight_delta":false}
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
next_round = R13_holdout_or_batch_promotion_review
priority = validate_C14_guard_on_additional_non-cathode_EV_supplier_cases
```

## 28. Source Notes

Primary price source: Songdaiki/stock-web.

The following Stock-Web paths were used:

- atlas/manifest.json
- atlas/schema.json
- atlas/symbol_profiles/003/003670.json
- atlas/symbol_profiles/373/373220.json
- atlas/symbol_profiles/247/247540.json
- atlas/ohlcv_tradable_by_symbol_year/003/003670/2024.csv and 2025.csv
- atlas/ohlcv_tradable_by_symbol_year/373/373220/2024.csv and 2025.csv
- atlas/ohlcv_tradable_by_symbol_year/247/247540/2024.csv and 2025.csv

All rows are raw/unadjusted `tradable_raw` calibration rows. This MD is not investment advice and does not contain live/current candidate discovery.
