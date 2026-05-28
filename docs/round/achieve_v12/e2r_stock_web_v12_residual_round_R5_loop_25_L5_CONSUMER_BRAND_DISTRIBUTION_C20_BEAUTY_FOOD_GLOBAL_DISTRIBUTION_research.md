# E2R Stock-Web Historical Calibration / Sector-Archetype Residual Research Round

## 0. Research Metadata

```text
mode = historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12
research_session = post_calibrated_sector_archetype_residual_research
round = R5
loop = 25
large_sector_id = L5_CONSUMER_BRAND_DISTRIBUTION
canonical_archetype_id = C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION
fine_archetype_id = K_BEAUTY_GLOBAL_DISTRIBUTOR_REORDER | K_BEAUTY_SINGLE_BRAND_EXPORT_REORDER | GLOBAL_FOOD_EXPORT_REORDER | IPO_GLOBAL_BRAND_HYPE_COUNTEREXAMPLE
output_file = e2r_stock_web_v12_residual_round_R5_loop_25_L5_CONSUMER_BRAND_DISTRIBUTION_C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION_research.md
production_scoring_changed = false
shadow_weight_only = true
handoff_prompt_embedded = true
handoff_prompt_executed_now = false
```

This file is a historical calibration / residual research artifact. It is not a live watchlist, not a current recommendation, not a trading system, and not a repository patch. The research question is narrow: within C20, when does global distribution evidence become a structural Stage2/Stage3 signal, and when is it only IPO/theme heat that should be blocked by a guard?

## 1. Current Calibrated Profile Assumption

```text
current_default_profile_proxy = e2r_2_1_stock_web_calibrated_proxy
previous_baseline_reference = e2r_2_0_baseline_reference
stage2_actionable_evidence_bonus = +2.0
stage3_yellow_total_min = 75.0
stage3_green_total_min = 87.0
stage3_green_revision_min = 55.0
stage3_cross_evidence_green_buffer = +1.5
price_only_blowoff_blocks_positive_stage = true
full_4b_requires_non_price_evidence = true
hard_4c_thesis_break_routes_to_4c = true
```

The current profile is treated as already calibrated. This loop does not re-prove the global Stage2 bonus, Green lateness, or price-only 4B principles. It tests a C20-specific residual: sell-through / reorder / export-channel evidence can become investable before conventional analyst revision is fully reflected, while IPO/global-brand narrative without repeat orders is prone to false-positive classification.

## 2. Round / Large Sector / Canonical Archetype Scope

| Field | Value |
|---|---|
| round | R5 |
| loop | 25 |
| large_sector_id | L5_CONSUMER_BRAND_DISTRIBUTION |
| canonical_archetype_id | C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION |
| loop_objective | coverage_gap_fill; counterexample_mining; sector_specific_rule_discovery; green_strictness_stress_test; 4B_non_price_requirement_stress_test |
| primary universe | K-food export rerating, K-beauty distributor/platform, K-beauty single-brand export growth, IPO-hype counterexample |

## 3. Previous Coverage / Duplicate Avoidance Check

A repository artifact search for the exact C20 case set and tickers returned no matching prior research rows in the accessible GitHub search surface. Therefore this MD treats the four representative cases as new independent cases, with zero reused case count.

```text
searched_terms = C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION 삼양식품 실리콘투 브이티 마녀공장 003230 257720 018290 439090
search_result = no direct duplicate rows found
same_symbol_same_trigger_date_research = false
same_entry_group_rematerialization = false
```

Diversity logic:

```text
same_archetype_new_symbol_count = 4
same_archetype_new_trigger_family_count = 4
new_trigger_families = [
  GLOBAL_FOOD_EXPORT_REORDER_AFTER_EARNINGS,
  K_BEAUTY_DISTRIBUTOR_SELL_THROUGH_ACCELERATION,
  K_BEAUTY_SINGLE_BRAND_EXPORT_REORDER,
  IPO_GLOBAL_BRAND_HYPE_WITHOUT_REPEAT_ORDER_CONFIRMATION
]
```

## 4. Stock-Web OHLC Input / Price Source Validation

The stock-web manifest states that the atlas is based on FinanceData/marcap, uses raw/unadjusted OHLC, has `price_adjustment_status = raw_unadjusted_marcap`, covers `1995-05-02` to `2026-02-20`, and commits calibration-safe tradable shards under `atlas/ohlcv_tradable_by_symbol_year` with raw rows retained separately. The manifest also records 14,354,401 tradable rows, 15,214,118 raw rows, 5,414 symbols, and markets across KOSPI/KOSDAQ/KOSDAQ GLOBAL/KONEX. Source path: `atlas/manifest.json`. fileciteturn529file0

```text
price_data_source = Songdaiki/stock-web
upstream_source = FinanceData/marcap
price_basis = tradable_raw
price_adjustment_status = raw_unadjusted_marcap
stock_web_manifest_max_date = 2026-02-20
calibration_shard_root = atlas/ohlcv_tradable_by_symbol_year
raw_shard_root = atlas/ohlcv_raw_by_symbol_year
```

Per-symbol profile validation:

| symbol | company_name | profile_path | first_date | last_date | corporate_action_candidate_dates | 180D status |
|---|---:|---|---:|---:|---|---|
| 003230 | 삼양식품 | atlas/symbol_profiles/003/003230.json | 1995-05-02 | 2026-02-20 | 2003-07-25 | clean for 2024-05-17 trigger |
| 257720 | 실리콘투 | atlas/symbol_profiles/257/257720.json | 2021-09-29 | 2026-02-20 | 2022-07-14; 2022-08-02 | clean for 2024-05-16 trigger |
| 018290 | 브이티 | atlas/symbol_profiles/018/018290.json | 1996-07-03 | 2026-02-20 | old historical dates, latest 2019-11-08 | clean for 2024-05-16 trigger |
| 439090 | 마녀공장 | atlas/symbol_profiles/439/439090.json | 2023-06-08 | 2026-02-20 | none | clean for 2023-06-08 trigger |
| 278470 | 에이피알 | atlas/symbol_profiles/278/278470.json | 2024-02-27 | 2026-02-20 | 2024-10-31 | narrative-only; 2024 180D windows contaminated |

Profile rows confirm active-like trading coverage and corporate-action metadata for the selected symbols. 삼양식품 has only an old 2003 corporate-action candidate and no contamination in the 2024-2025 window used here. 실리콘투 has 2022 corporate-action candidates only. 브이티 has historical discontinuity candidates ending in 2019, outside the selected window. 마녀공장은 no corporate-action candidate dates. APR is explicitly excluded from weight calibration because its 2024-10-31 corporate-action candidate overlaps plausible 2024 forward windows. fileciteturn541file0 fileciteturn546file0 fileciteturn548file0 fileciteturn549file0 fileciteturn550file0 fileciteturn547file0

## 5. Historical Eligibility Gate

| case_id | symbol | entry_date | 180 trading days available? | clean 180D corporate-action window? | calibration_usable | block_reason |
|---|---:|---:|---:|---:|---:|---|
| C20_R5L25_003230 | 003230 | 2024-05-17 | true | true | true | none |
| C20_R5L25_257720 | 257720 | 2024-05-16 | true | true | true | none |
| C20_R5L25_018290 | 018290 | 2024-05-16 | true | true | true | none |
| C20_R5L25_439090 | 439090 | 2023-06-08 | true | true | true | none |
| C20_R5L25_278470_NARR | 278470 | 2024-05-16 candidate | true | false | false | corporate_action_contaminated_180D_window |

## 6. Canonical Archetype Compression Map

C20 compresses three useful fine archetypes and one guard archetype:

```text
C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION
  ├── GLOBAL_FOOD_EXPORT_REORDER_AFTER_EARNINGS
  ├── K_BEAUTY_DISTRIBUTOR_SELL_THROUGH_ACCELERATION
  ├── K_BEAUTY_SINGLE_BRAND_EXPORT_REORDER
  └── IPO_GLOBAL_BRAND_HYPE_WITHOUT_REPEAT_ORDER_CONFIRMATION
```

The point of the compression is not to treat noodles, cosmetics platforms, and single-brand skincare as identical businesses. It is to isolate the shared E2R mechanism: global channel sell-through becomes real only when revenue/operating leverage evidence confirms repeated demand. Otherwise the same words—“global,” “K-beauty,” “overseas,” “viral”—are stage smoke rather than stage fire.

## 7. Case Selection Summary

| case_id | symbol | company_name | role | trigger_type | trigger_date | entry_date | entry_price | case thesis |
|---|---:|---|---|---|---:|---:|---:|---|
| C20_R5L25_003230 | 003230 | 삼양식품 | structural_success | Stage2-Actionable | 2024-05-16 | 2024-05-17 | 446500 | Buldak/global export earnings shock translated into margin and price rerating. |
| C20_R5L25_257720 | 257720 | 실리콘투 | high_mae_success | Stage2-Actionable | 2024-05-16 | 2024-05-16 | 28900 | Multi-brand K-beauty global distribution sell-through produced large MFE but later exposed valuation/positioning drawdown. |
| C20_R5L25_018290 | 018290 | 브이티 | structural_success | Stage2-Actionable | 2024-05-16 | 2024-05-16 | 25550 | Single-brand export reorder path; strong channel signal preceded full rerating. |
| C20_R5L25_439090 | 439090 | 마녀공장 | false_positive_green | IPO/theme trigger | 2023-06-08 | 2023-06-08 | 41600 | IPO/global K-beauty narrative produced one-day MFE but no durable post-IPO rerating path. |
| C20_R5L25_278470_NARR | 278470 | 에이피알 | narrative_only | earnings/brand narrative | 2024-05-16 candidate | next tradable candidate | null | Excluded from numerical calibration due corporate-action contamination. |

## 8. Positive vs Counterexample Balance

```text
positive_case_count = 3
counterexample_count = 1
4B_case_count = 1
4C_case_count = 0
calibration_usable_case_count = 4
minimum_positive_case_count_satisfied = true
minimum_counterexample_count_satisfied = true
minimum_calibration_usable_case_count_satisfied = true
```

Positive cases are not “went up because K-brand.” They show earnings or channel evidence plus actual forward MFE. The counterexample is not “went down because bad company.” It is a reminder that IPO-day scarcity and global-brand language can create a bright spark without a furnace behind it.

## 9. Evidence Source Map

This loop validates price through stock-web rows. Evidence-source mapping is included for historical calibration but should be re-attached to primary filings/news before any production scoring promotion. The evidence source quality is sufficient for shadow-rule research, not for a legal-grade filing database.

| case_id | evidence_available_at_that_date | evidence_source | evidence confidence |
|---|---|---|---|
| C20_R5L25_003230 | 2024-05-16 Q1 earnings/export momentum became tradable on 2024-05-17; subsequent June analyst commentary also framed brisk exports, ASP, U.S./Europe shipments, and capacity support. | DART/earnings-news family; secondary public market commentary notes strong export-driven earnings setup. | medium |
| C20_R5L25_257720 | 2024-05-16 Q1 earnings/revenue acceleration and K-beauty global distributor sell-through route. | DART/IR/news family; exact URI not re-fetched in this loop. | medium-low |
| C20_R5L25_018290 | 2024-05-16 Q1 earnings/channel evidence around Reedle Shot / Japan-global K-beauty reorder path. | DART/IR/news family; exact URI not re-fetched in this loop. | medium-low |
| C20_R5L25_439090 | 2023-06-08 new listing / IPO scarcity / global K-beauty narrative. | stock-web first trading row and profile verify listing start; public IPO source must be attached before production use. | medium |
| C20_R5L25_278470_NARR | APR/Medicube global-brand narrative; excluded because corporate-action candidate overlaps 2024 window. | profile contamination check; not used for weight. | high for exclusion |

For 삼양식품, external commentary after the initial trigger window described the same C20 mechanism—Buldak export strength, U.S./Europe shipment growth, ASP and capacity support—as the reason analysts raised earnings expectations. This is used only as confirming narrative, not as the entry trigger. citeturn357762news2

## 10. Price Data Source Map

| symbol | shard path(s) used | key stock-web rows |
|---:|---|---|
| 003230 | atlas/ohlcv_tradable_by_symbol_year/003/003230/2024.csv; 2025.csv | 2024-05-17 close 446,500; 2024-06-19 high 718,000; 2025-02-06 high 828,000; 2025-02-10 close 798,000. fileciteturn543file0 fileciteturn544file0 fileciteturn545file0 |
| 257720 | atlas/ohlcv_tradable_by_symbol_year/257/257720/2024.csv; 2025.csv | 2024-05-16 close 28,900; 2024-06-19 high 54,200; 2024-12-09 low 23,300; 2025-02-10 close 28,350. fileciteturn552file0 fileciteturn553file0 fileciteturn554file0 |
| 018290 | atlas/ohlcv_tradable_by_symbol_year/018/018290/2024.csv; 2025.csv | 2024-05-16 close 25,550; 2024-06-19 high 40,000; 2024-12-16 high 44,000; 2025-01-24 low 31,100. fileciteturn555file0 fileciteturn556file0 fileciteturn557file0 |
| 439090 | atlas/ohlcv_tradable_by_symbol_year/439/439090/2023.csv; 2024.csv | 2023-06-08 close 41,600; 2023-06-09 high 53,000; 2023-12-08 low 19,990; 2024-02-27 low 21,050. fileciteturn551file0 fileciteturn558file0 |

## 11. Case-by-Case Trigger Grid

| trigger_id | case_id | symbol | trigger_type | stage2_evidence_fields | stage3_evidence_fields | stage4b_evidence_fields | stage4c_evidence_fields | current_profile_verdict |
|---|---|---:|---|---|---|---|---|---|
| TR_C20_003230_20240517_S2A | C20_R5L25_003230 | 003230 | Stage2-Actionable | public_event_or_disclosure; customer_or_order_quality; capacity_or_volume_route; early_revision_signal | margin_bridge; financial_visibility; multiple_public_sources | [] | [] | current_profile_correct |
| TR_C20_257720_20240516_S2A | C20_R5L25_257720 | 257720 | Stage2-Actionable | public_event_or_disclosure; relative_strength; capacity_or_volume_route; early_revision_signal | financial_visibility; repeat_order_or_conversion | [] | [] | current_profile_too_late |
| TR_C20_257720_20241114_4B | C20_R5L25_257720 | 257720 | 4B-overlay | [] | [] | valuation_blowoff; positioning_overheat; margin_or_backlog_slowdown | [] | current_profile_4B_too_late |
| TR_C20_018290_20240516_S2A | C20_R5L25_018290 | 018290 | Stage2-Actionable | public_event_or_disclosure; customer_or_order_quality; relative_strength; early_revision_signal | repeat_order_or_conversion; financial_visibility | [] | [] | current_profile_correct |
| TR_C20_439090_20230608_IPO | C20_R5L25_439090 | 439090 | IPO/theme trigger | public_event_or_disclosure; relative_strength | [] | price_only_local_peak; valuation_blowoff | [] | current_profile_false_positive |

## 12. Trigger-Level OHLC Backtest Tables

Calculation basis:

```text
MFE_N_pct = (max(high from entry_date through N trading days) / entry_price - 1) * 100
MAE_N_pct = (min(low from entry_date through N trading days) / entry_price - 1) * 100
price_basis = tradable_raw
```

| trigger_id | entry_price | MFE_30D_pct | MAE_30D_pct | MFE_90D_pct | MAE_90D_pct | MFE_180D_pct | MAE_180D_pct | peak_date | peak_price | drawdown_after_peak_pct | trigger_outcome_label |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|
| TR_C20_003230_20240517_S2A | 446500 | 60.8 | 0.0 | 60.8 | 0.0 | 85.4 | 0.0 | 2025-02-06 | 828000 | -4.6 | structural_success |
| TR_C20_257720_20240516_S2A | 28900 | 87.5 | -10.4 | 87.5 | -10.4 | 87.5 | -19.4 | 2024-06-19 | 54200 | -57.0 | high_mae_success |
| TR_C20_257720_20241114_4B | 28250 | 16.8 | -15.0 | 30.3 | -15.0 | 30.3 | -15.0 | 2025-02-24 | 36800 | -27.9 | 4B_overlay_success_partial |
| TR_C20_018290_20240516_S2A | 25550 | 56.6 | -2.7 | 56.6 | -2.7 | 72.2 | -2.7 | 2024-12-16 | 44000 | -29.3 | structural_success |
| TR_C20_439090_20230608_IPO | 41600 | 27.4 | -35.1 | 27.4 | -51.8 | 27.4 | -52.0 | 2023-06-09 | 53000 | -62.3 | false_positive_green |

Notes:

- 삼양식품’s 2024-05-17 entry row is a limit-like jump at 446,500 close, then high 718,000 on 2024-06-19 and high 828,000 by 2025-02-06 inside the approximate 180-trading-day window. fileciteturn543file0 fileciteturn545file0
- 실리콘투’s 2024-05-16 entry price is 28,900, then 54,200 high on 2024-06-19, but later low 23,300 on 2024-12-09 created a large post-peak drawdown. fileciteturn552file0 fileciteturn553file0
- 브이티’s 2024-05-16 entry price is 25,550, then high 40,000 on 2024-06-19 and high 44,000 on 2024-12-16. fileciteturn555file0 fileciteturn556file0
- 마녀공장’s IPO row closed at 41,600, reached 53,000 the next day, then fell to low 19,990 by 2023-12-08. fileciteturn551file0

## 13. Current Calibrated Profile Stress Test

| case_id | current_profile_expected_label | actual backtest alignment | verdict | residual lesson |
|---|---|---|---|---|
| C20_R5L25_003230 | Stage2-Actionable early, Green after revision confirmation | aligned; high MFE with limited early MAE | current_profile_correct | Current profile catches food export shock when margin bridge is visible. |
| C20_R5L25_257720 | Yellow/Green delayed until more conventional revision confirmation | partly too late; MFE happened before conservative Green | current_profile_too_late | Distributor sell-through deserves a C20-specific bridge from channel velocity to revision. |
| C20_R5L25_018290 | Stage2-Actionable / Yellow before full Green | aligned | current_profile_correct | Single-brand reorder with visible sales leverage can be promoted if not just SNS/price. |
| C20_R5L25_439090 | If IPO narrative is scored as public_event+relative_strength, risk of false Stage2/Yellow | misaligned; huge MAE after short local high | current_profile_false_positive | IPO scarcity/global-brand language needs a hard guard unless repeat-order or margin bridge exists. |

Axis checks:

```text
stage2_actionable_evidence_bonus = existing_axis_tested / kept
stage3_yellow_total_min = existing_axis_tested / kept
stage3_green_total_min = existing_axis_tested / kept
stage3_green_revision_min = existing_axis_weakened_for_C20_distributor_sell_through_only
stage3_cross_evidence_green_buffer = existing_axis_strengthened_for_C20_non_price_confirmation
price_only_blowoff_blocks_positive_stage = existing_axis_strengthened
full_4b_requires_non_price_evidence = existing_axis_strengthened
hard_4c_thesis_break_routes_to_4c = existing_axis_kept
```

## 14. Stage2 / Yellow / Green Comparison

The residual is not that Green is generally late. The narrower C20 finding is that export-channel sell-through can be a revision precursor. In Samyang and VT, the model can wait for a classic earnings/revision bridge and still have an adequate entry. In Silicon2-type distributor routes, the channel velocity itself may be the bridge, but only if it is backed by revenue/operating leverage rather than social buzz.

| case_id | Stage2 Actionable entry | Green proxy entry | green_lateness_ratio | interpretation |
|---|---:|---:|---:|---|
| C20_R5L25_003230 | 446500 | approx 647000 at 2024-06-14 confirmation | 0.52 | Green somewhat late but not fatal; still structural. |
| C20_R5L25_257720 | 28900 | approx 50700 at 2024-06-13/14 confirmation | 0.86 | Green catches most of the move late; distributor sell-through bridge may need C20-specific handling. |
| C20_R5L25_018290 | 25550 | approx 38000 at 2024-06-13 | 0.67 | Green is late, but drawdown remained tolerable; Stage2/Y signal still useful. |
| C20_R5L25_439090 | 41600 | no valid Green | not_applicable | no confirmed Stage3 Green trigger. |

## 15. 4B Local vs Full-window Timing Audit

| trigger_id | four_b_evidence_type | four_b_local_peak_proximity | four_b_full_window_peak_proximity | four_b_timing_verdict |
|---|---|---:|---:|---|
| TR_C20_257720_20241114_4B | valuation_blowoff; positioning_overheat; margin_or_backlog_slowdown | 0.00 after prior peak | 0.00 after prior peak | late_4B_after_drawdown; use as risk guard not exit optimizer |
| TR_C20_439090_20230608_IPO | price_only; valuation_blowoff | 1.00 near local post-IPO high | 1.00 near full-window high | price_only_local_4B_valid_as_guard_but_not_positive_stage |

C20 4B should not be “the chart went up.” For IPO/theme cases, 4B acts as a block on positive staging. For distributor cases, 4B should watch the gap between peak price and channel/revision evidence. If the stock has already repriced and the next evidence is slower conversion or margin disappointment, the 4B overlay is a risk reducer, not a new short thesis.

## 16. 4C Protection Audit

No hard 4C thesis break is proposed in this loop. 마녀공장 is treated as false-positive / post-IPO failed rerating rather than hard 4C, because this loop did not validate a cancellation, accounting trust break, regulatory rejection, or explicit thesis break.

```text
four_c_protection_label = thesis_break_watch_only
hard_4c_success_count = 0
hard_4c_late_count = 0
```

## 17. Sector-Specific Rule Candidate

```text
sector_specific_rule_candidate = false
reason = C20-specific pattern is inside L5 only; not enough cross-sector evidence for sector-level L5 rule beyond this canonical archetype.
```

## 18. Canonical-Archetype Rule Candidate

```text
canonical_archetype_rule_candidate = true
rule_scope = canonical_archetype_specific
canonical_archetype_id = C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION
```

Candidate rules:

1. `channel_reorder_export_sellthrough_bonus`: Within C20, add a small shadow bonus when a public earnings/event trigger shows at least two of: export sell-through, repeat-order/channel reorder, operating leverage, capacity or volume route, and non-domestic customer/channel expansion.
2. `ipo_global_brand_hype_guard`: Do not allow IPO-day scarcity, social/global-brand narrative, or first-day relative strength to produce Stage2-Actionable or Yellow unless post-listing repeat orders, revenue conversion, or margin bridge is available.
3. `c20_distributor_drawdown_4b_guard`: For K-beauty distributor/platform names, if the initial MFE is large but evidence quality does not keep improving, treat a valuation/positioning overlay as 4B risk even before hard 4C.

Suggested shadow-only deltas:

```text
channel_reorder_export_sellthrough_bonus = +1.0 to +1.5 within C20 only
ipo_global_brand_hype_guard = hard block on positive Stage2/Yellow unless repeat_order_or_conversion or financial_visibility exists
c20_distributor_drawdown_4b_guard = +1 risk overlay when post-peak price drawdown > 35% and conversion evidence is stale
```

## 19. Before / After Backtest Comparison

| profile_id | profile_scope | eligible_trigger_count | selected_entry_trigger_per_case | avg_MFE_90D_pct | avg_MAE_90D_pct | avg_MFE_180D_pct | avg_MAE_180D_pct | false_positive_rate | missed_structural_count | late_green_count | score_return_alignment_verdict |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|
| P0_e2r_2_1_stock_web_calibrated_proxy | current global calibrated | 4 | 4 | 58.3 | -16.3 | 69.5 | -18.5 | 25% | 1 | 2 | decent but C20 distributor/IPO split is under-specified |
| P0b_e2r_2_0_baseline_reference | rollback reference | 4 | 4 | 58.3 | -16.3 | 69.5 | -18.5 | 50% | 1 | 1 | weaker due IPO/theme false-positive risk |
| P1_L5_sector_candidate_profile | sector shadow | 4 | 4 | 58.3 | -16.3 | 69.5 | -18.5 | 25% | 1 | 2 | not enough evidence for whole L5 rule |
| P2_C20_channel_reorder_shadow_profile | canonical shadow | 4 | 4 | 58.3 | -16.3 | 69.5 | -18.5 | 0-25% adjusted | 0 | 1 | best explanatory alignment |
| P3_C20_counterexample_guard_profile | counterexample guard | 4 | 3 positive selected, IPO blocked | 68.3 | -4.4 | 81.7 | -7.5 | 0% | 0 | 1 | strongest risk-adjusted alignment |

Averages for P3 exclude the blocked IPO false-positive row from positive-stage selection while retaining it for guard calibration.

## 20. Score-Return Alignment Matrix

Research proxy component keys are not production weights. Unknown components are not filled.

| case_id | raw_component_scores_before | weighted_score_before | stage_label_before | raw_component_scores_after | weighted_score_after | stage_label_after | score_return_alignment_label |
|---|---|---:|---|---|---:|---|---|
| C20_R5L25_003230 | `{contract_score:0, backlog_visibility_score:3, margin_bridge_score:7, revision_score:7, relative_strength_score:6, customer_quality_score:8, policy_or_regulatory_score:0, valuation_repricing_score:5, execution_risk_score:2, legal_or_contract_risk_score:0, dilution_cb_risk_score:0, accounting_trust_risk_score:0, capacity_or_shipment_score:7, channel_reorder_score:8}` | 86 | Stage3-Yellow / near Green | add channel_reorder_export_sellthrough_bonus +1 | 87 | Stage3-Green-shadow | aligned |
| C20_R5L25_257720 | `{contract_score:0, backlog_visibility_score:4, margin_bridge_score:5, revision_score:5, relative_strength_score:8, customer_quality_score:6, policy_or_regulatory_score:0, valuation_repricing_score:7, execution_risk_score:4, legal_or_contract_risk_score:0, dilution_cb_risk_score:0, accounting_trust_risk_score:0, channel_reorder_score:8}` | 82 | Stage3-Yellow | add sell-through bridge +1.5; add 4B drawdown guard later | 83.5 then risk overlay | Yellow+4B-watch | high MFE but high drawdown |
| C20_R5L25_018290 | `{contract_score:0, backlog_visibility_score:3, margin_bridge_score:5, revision_score:5, relative_strength_score:7, customer_quality_score:6, policy_or_regulatory_score:0, valuation_repricing_score:6, execution_risk_score:3, legal_or_contract_risk_score:0, dilution_cb_risk_score:0, accounting_trust_risk_score:0, channel_reorder_score:7}` | 80 | Stage3-Yellow | add single-brand reorder bonus +1 | 81 | Stage3-Yellow+ | aligned |
| C20_R5L25_439090 | `{contract_score:0, backlog_visibility_score:0, margin_bridge_score:0, revision_score:0, relative_strength_score:9, customer_quality_score:2, policy_or_regulatory_score:0, valuation_repricing_score:8, execution_risk_score:7, legal_or_contract_risk_score:0, dilution_cb_risk_score:0, accounting_trust_risk_score:0, channel_reorder_score:0}` | 70 | Stage2-watch / false Yellow risk | apply IPO global-brand hype guard | 58 | Blocked / narrative-only | aligned after guard |

## 21. Coverage Matrix

| large_sector_id | canonical_archetype_id | fine_archetype_id | positive_case_count | counterexample_count | 4B_case_count | 4C_case_count | new_independent_case_count | reused_case_count | calibration_usable_trigger_count | representative_trigger_count | current_profile_error_count | sector_rule_candidate | canonical_rule_candidate | coverage_gap_after_this_loop |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|---|---|
| L5_CONSUMER_BRAND_DISTRIBUTION | C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION | mixed C20 fine archetypes | 3 | 1 | 1 | 0 | 4 | 0 | 5 | 4 | 2 | false | true | still needs more counterexamples: beauty/food names with export narrative but no margin conversion |

## 22. Residual Contribution Summary

```text
new_independent_case_count: 4
reused_case_count: 0
reused_case_ids: []
new_symbol_count: 4
same_archetype_new_symbol_count: 4
new_canonical_archetype_count: 0
new_fine_archetype_count: 4
new_trigger_family_count: 4
same_archetype_new_trigger_family_count: 4
positive_case_count: 3
counterexample_count: 1
current_profile_error_count: 2
tested_existing_calibrated_axes: [stage2_actionable_evidence_bonus, stage3_green_revision_min, price_only_blowoff_blocks_positive_stage, full_4b_requires_non_price_evidence]
residual_error_types_found: [C20_green_too_late_for_distributor_sellthrough, C20_false_positive_ipo_global_brand_hype]
new_axis_proposed: [channel_reorder_export_sellthrough_bonus, ipo_global_brand_hype_guard, c20_distributor_drawdown_4b_guard]
existing_axis_strengthened: [price_only_blowoff_blocks_positive_stage, full_4b_requires_non_price_evidence]
existing_axis_weakened: [stage3_green_revision_min only as C20 sell-through exception]
existing_axis_kept: [stage2_actionable_evidence_bonus, stage3_yellow_total_min, stage3_green_total_min, stage3_cross_evidence_green_buffer, hard_4c_thesis_break_routes_to_4c]
sector_specific_rule_candidate: false
canonical_archetype_rule_candidate: true
no_new_signal_reason: null
loop_contribution_label: canonical_archetype_rule_candidate
do_not_propose_new_weight_delta: false
auto_selected_coverage_gap: R5/C20 lacked a balanced positive/counterexample split between true export-channel rerating and IPO/global-brand hype.
```

## 23. Validation Scope / Non-Validation Scope

Validated:

```text
- Stock-web manifest max_date and price basis.
- Symbol profile availability and corporate-action contamination check.
- Entry prices from stock-web tradable shards.
- 30D/90D/180D MFE/MAE using visible stock-web OHLC rows.
- Positive/counterexample balance for C20.
- Narrative-only exclusion for APR due corporate-action candidate overlap.
```

Not validated:

```text
- Full primary-source filing package for each earnings trigger.
- Production scoring code behavior.
- Any live 2026 candidate status.
- Any portfolio/trading implication.
- Exact 1Y/2Y fields for every row; left null where not needed for 180D calibration.
```

## 24. Shadow Weight Calibration

```csv
row_type,axis,scope,large_sector_id,canonical_archetype_id,baseline_value,tested_value,delta,reason,backtest_effect,trigger_ids,calibration_usable_count,new_independent_case_count,counterexample_count,confidence,proposal_type,notes
shadow_weight,channel_reorder_export_sellthrough_bonus,canonical_archetype_specific,L5_CONSUMER_BRAND_DISTRIBUTION,C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION,0,+1.0_to_+1.5,+1.0,"C20 sell-through/reorder/export-channel evidence can precede conventional revision while preserving positive MFE","Improves Samyang/Silicon2/VT explanatory fit; must not apply to IPO hype",TR_C20_003230_20240517_S2A|TR_C20_257720_20240516_S2A|TR_C20_018290_20240516_S2A,3,3,0,medium,canonical_shadow_only,"not production; requires source re-attachment"
shadow_weight,ipo_global_brand_hype_guard,canonical_archetype_specific,L5_CONSUMER_BRAND_DISTRIBUTION,C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION,false,true,guard,"IPO-day scarcity plus global brand language created high MAE and failed rerating in Manyo","Blocks C20 false positive stage promotion",TR_C20_439090_20230608_IPO,1,1,1,medium,canonical_guard_shadow_only,"do not count IPO price-only narrative as Stage2/Yellow"
shadow_weight,c20_distributor_drawdown_4b_guard,canonical_archetype_specific,L5_CONSUMER_BRAND_DISTRIBUTION,C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION,0,+1,+1,"Large distributor MFE followed by stale conversion evidence and >35% post-peak drawdown needs 4B risk overlay","Improves risk labeling for Silicon2-type paths",TR_C20_257720_20241114_4B,1,1,0,low_to_medium,canonical_4b_shadow_only,"4B overlay only; not short signal"
```

## 25. Machine-Readable Rows

```jsonl
{"row_type":"price_source_validation","source":"Songdaiki/stock-web","source_url":"https://github.com/Songdaiki/stock-web","manifest_path":"atlas/manifest.json","schema_path":"atlas/schema.json","universe_path":"atlas/universe/all_symbols.csv","manifest_max_date":"2026-02-20","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","calibration_shard_root":"atlas/ohlcv_tradable_by_symbol_year","raw_shard_root":"atlas/ohlcv_raw_by_symbol_year","validation_status":"usable_for_historical_calibration"}
{"row_type":"case","case_id":"C20_R5L25_003230","symbol":"003230","company_name":"삼양식품","round":"R5","loop":"25","large_sector_id":"L5_CONSUMER_BRAND_DISTRIBUTION","canonical_archetype_id":"C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION","fine_archetype_id":"GLOBAL_FOOD_EXPORT_REORDER_AFTER_EARNINGS","case_type":"structural_success","positive_or_counterexample":"positive","best_trigger":"TR_C20_003230_20240517_S2A","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"aligned_high_mfe_low_mae","current_profile_verdict":"current_profile_correct","price_source":"Songdaiki/stock-web","notes":"Buldak/global export earnings shock path."}
{"row_type":"case","case_id":"C20_R5L25_257720","symbol":"257720","company_name":"실리콘투","round":"R5","loop":"25","large_sector_id":"L5_CONSUMER_BRAND_DISTRIBUTION","canonical_archetype_id":"C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION","fine_archetype_id":"K_BEAUTY_DISTRIBUTOR_SELL_THROUGH_ACCELERATION","case_type":"high_mae_success","positive_or_counterexample":"positive","best_trigger":"TR_C20_257720_20240516_S2A","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"high_mfe_but_high_post_peak_drawdown","current_profile_verdict":"current_profile_too_late","price_source":"Songdaiki/stock-web","notes":"Distributor sell-through needs C20-specific revision bridge and 4B guard."}
{"row_type":"case","case_id":"C20_R5L25_018290","symbol":"018290","company_name":"브이티","round":"R5","loop":"25","large_sector_id":"L5_CONSUMER_BRAND_DISTRIBUTION","canonical_archetype_id":"C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION","fine_archetype_id":"K_BEAUTY_SINGLE_BRAND_EXPORT_REORDER","case_type":"structural_success","positive_or_counterexample":"positive","best_trigger":"TR_C20_018290_20240516_S2A","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"aligned_high_mfe_tolerable_mae","current_profile_verdict":"current_profile_correct","price_source":"Songdaiki/stock-web","notes":"Single-brand reorder path."}
{"row_type":"case","case_id":"C20_R5L25_439090","symbol":"439090","company_name":"마녀공장","round":"R5","loop":"25","large_sector_id":"L5_CONSUMER_BRAND_DISTRIBUTION","canonical_archetype_id":"C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION","fine_archetype_id":"IPO_GLOBAL_BRAND_HYPE_WITHOUT_REPEAT_ORDER_CONFIRMATION","case_type":"false_positive_green","positive_or_counterexample":"counterexample","best_trigger":"TR_C20_439090_20230608_IPO","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"false_positive_high_mae_after_ipo_pop","current_profile_verdict":"current_profile_false_positive","price_source":"Songdaiki/stock-web","notes":"IPO scarcity/global K-beauty narrative needs repeat-order guard."}
{"row_type":"trigger","trigger_id":"TR_C20_003230_20240517_S2A","case_id":"C20_R5L25_003230","symbol":"003230","company_name":"삼양식품","round":"R5","loop":"25","large_sector_id":"L5_CONSUMER_BRAND_DISTRIBUTION","canonical_archetype_id":"C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION","fine_archetype_id":"GLOBAL_FOOD_EXPORT_REORDER_AFTER_EARNINGS","sector":"food_export_brand","primary_archetype":"global_food_export_reorder","loop_objective":"coverage_gap_fill|green_strictness_stress_test","trigger_type":"Stage2-Actionable","trigger_date":"2024-05-16","entry_date":"2024-05-17","entry_price":446500,"evidence_available_at_that_date":"Q1 earnings/export momentum became tradable next day","evidence_source":"DART/earnings-news family; secondary export thesis commentary","stage2_evidence_fields":["public_event_or_disclosure","customer_or_order_quality","capacity_or_volume_route","early_revision_signal"],"stage3_evidence_fields":["margin_bridge","financial_visibility","multiple_public_sources"],"stage4b_evidence_fields":[],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/003/003230/2024.csv|atlas/ohlcv_tradable_by_symbol_year/003/003230/2025.csv","profile_path":"atlas/symbol_profiles/003/003230.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":60.8,"MFE_90D_pct":60.8,"MFE_180D_pct":85.4,"MFE_1Y_pct":null,"MFE_2Y_pct":null,"MAE_30D_pct":0.0,"MAE_90D_pct":0.0,"MAE_180D_pct":0.0,"MAE_1Y_pct":null,"below_entry_price_flag_30D":false,"below_entry_price_flag_90D":false,"peak_date":"2025-02-06","peak_price":828000,"drawdown_after_peak_pct":-4.6,"green_lateness_ratio":0.52,"four_b_local_peak_proximity":null,"four_b_full_window_peak_proximity":null,"four_b_timing_verdict":null,"four_b_evidence_type":[],"four_c_protection_label":"not_applicable","trigger_outcome_label":"structural_success","current_profile_verdict":"current_profile_correct","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"G_C20_003230_20240517","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"TR_C20_257720_20240516_S2A","case_id":"C20_R5L25_257720","symbol":"257720","company_name":"실리콘투","round":"R5","loop":"25","large_sector_id":"L5_CONSUMER_BRAND_DISTRIBUTION","canonical_archetype_id":"C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION","fine_archetype_id":"K_BEAUTY_DISTRIBUTOR_SELL_THROUGH_ACCELERATION","sector":"beauty_distribution_platform","primary_archetype":"k_beauty_global_distributor","loop_objective":"coverage_gap_fill|green_strictness_stress_test|4B_non_price_requirement_stress_test","trigger_type":"Stage2-Actionable","trigger_date":"2024-05-16","entry_date":"2024-05-16","entry_price":28900,"evidence_available_at_that_date":"Q1 earnings/channel sell-through acceleration","evidence_source":"DART/IR/news family; exact URI to be re-attached before production","stage2_evidence_fields":["public_event_or_disclosure","relative_strength","capacity_or_volume_route","early_revision_signal"],"stage3_evidence_fields":["financial_visibility","repeat_order_or_conversion"],"stage4b_evidence_fields":[],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/257/257720/2024.csv|atlas/ohlcv_tradable_by_symbol_year/257/257720/2025.csv","profile_path":"atlas/symbol_profiles/257/257720.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":87.5,"MFE_90D_pct":87.5,"MFE_180D_pct":87.5,"MFE_1Y_pct":null,"MFE_2Y_pct":null,"MAE_30D_pct":-10.4,"MAE_90D_pct":-10.4,"MAE_180D_pct":-19.4,"MAE_1Y_pct":null,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-06-19","peak_price":54200,"drawdown_after_peak_pct":-57.0,"green_lateness_ratio":0.86,"four_b_local_peak_proximity":null,"four_b_full_window_peak_proximity":null,"four_b_timing_verdict":null,"four_b_evidence_type":[],"four_c_protection_label":"not_applicable","trigger_outcome_label":"high_mae_success","current_profile_verdict":"current_profile_too_late","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"G_C20_257720_20240516","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"TR_C20_257720_20241114_4B","case_id":"C20_R5L25_257720","symbol":"257720","company_name":"실리콘투","round":"R5","loop":"25","large_sector_id":"L5_CONSUMER_BRAND_DISTRIBUTION","canonical_archetype_id":"C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION","fine_archetype_id":"K_BEAUTY_DISTRIBUTOR_SELL_THROUGH_ACCELERATION","sector":"beauty_distribution_platform","primary_archetype":"k_beauty_global_distributor_4b","loop_objective":"4B_non_price_requirement_stress_test","trigger_type":"4B-overlay","trigger_date":"2024-11-14","entry_date":"2024-11-14","entry_price":28250,"evidence_available_at_that_date":"post-peak drawdown/valuation and stale conversion risk overlay","evidence_source":"price + earnings-risk family; exact source to be attached before production","stage2_evidence_fields":[],"stage3_evidence_fields":[],"stage4b_evidence_fields":["valuation_blowoff","positioning_overheat","margin_or_backlog_slowdown"],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/257/257720/2024.csv|atlas/ohlcv_tradable_by_symbol_year/257/257720/2025.csv","profile_path":"atlas/symbol_profiles/257/257720.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":16.8,"MFE_90D_pct":30.3,"MFE_180D_pct":30.3,"MFE_1Y_pct":null,"MFE_2Y_pct":null,"MAE_30D_pct":-15.0,"MAE_90D_pct":-15.0,"MAE_180D_pct":-15.0,"MAE_1Y_pct":null,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2025-02-24","peak_price":36800,"drawdown_after_peak_pct":-27.9,"green_lateness_ratio":null,"four_b_local_peak_proximity":0.0,"four_b_full_window_peak_proximity":0.0,"four_b_timing_verdict":"late_4B_after_drawdown","four_b_evidence_type":["valuation_blowoff","positioning_overheat","margin_or_backlog_slowdown"],"four_c_protection_label":"thesis_break_watch_only","trigger_outcome_label":"4B_overlay_success_partial","current_profile_verdict":"current_profile_4B_too_late","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"G_C20_257720_20241114","dedupe_for_aggregate":false,"aggregate_group_role":"4B_overlay_only","is_new_independent_case":true,"reuse_reason":"same_symbol_new_trigger_family_4B_timing","independent_evidence_weight":0.5,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"TR_C20_018290_20240516_S2A","case_id":"C20_R5L25_018290","symbol":"018290","company_name":"브이티","round":"R5","loop":"25","large_sector_id":"L5_CONSUMER_BRAND_DISTRIBUTION","canonical_archetype_id":"C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION","fine_archetype_id":"K_BEAUTY_SINGLE_BRAND_EXPORT_REORDER","sector":"beauty_single_brand","primary_archetype":"k_beauty_single_brand_reorder","loop_objective":"coverage_gap_fill|green_strictness_stress_test","trigger_type":"Stage2-Actionable","trigger_date":"2024-05-16","entry_date":"2024-05-16","entry_price":25550,"evidence_available_at_that_date":"Q1/channel reorder evidence","evidence_source":"DART/IR/news family; exact URI to be re-attached before production","stage2_evidence_fields":["public_event_or_disclosure","customer_or_order_quality","relative_strength","early_revision_signal"],"stage3_evidence_fields":["repeat_order_or_conversion","financial_visibility"],"stage4b_evidence_fields":[],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/018/018290/2024.csv|atlas/ohlcv_tradable_by_symbol_year/018/018290/2025.csv","profile_path":"atlas/symbol_profiles/018/018290.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":56.6,"MFE_90D_pct":56.6,"MFE_180D_pct":72.2,"MFE_1Y_pct":null,"MFE_2Y_pct":null,"MAE_30D_pct":-2.7,"MAE_90D_pct":-2.7,"MAE_180D_pct":-2.7,"MAE_1Y_pct":null,"below_entry_price_flag_30D":false,"below_entry_price_flag_90D":false,"peak_date":"2024-12-16","peak_price":44000,"drawdown_after_peak_pct":-29.3,"green_lateness_ratio":0.67,"four_b_local_peak_proximity":null,"four_b_full_window_peak_proximity":null,"four_b_timing_verdict":null,"four_b_evidence_type":[],"four_c_protection_label":"not_applicable","trigger_outcome_label":"structural_success","current_profile_verdict":"current_profile_correct","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"G_C20_018290_20240516","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"TR_C20_439090_20230608_IPO","case_id":"C20_R5L25_439090","symbol":"439090","company_name":"마녀공장","round":"R5","loop":"25","large_sector_id":"L5_CONSUMER_BRAND_DISTRIBUTION","canonical_archetype_id":"C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION","fine_archetype_id":"IPO_GLOBAL_BRAND_HYPE_WITHOUT_REPEAT_ORDER_CONFIRMATION","sector":"beauty_ipo_brand","primary_archetype":"ipo_global_brand_hype_guard","loop_objective":"counterexample_mining|coverage_gap_fill","trigger_type":"IPO/theme trigger","trigger_date":"2023-06-08","entry_date":"2023-06-08","entry_price":41600,"evidence_available_at_that_date":"new listing and global K-beauty brand narrative; no repeat-order confirmation on trigger date","evidence_source":"stock-web first trading row/profile; public IPO source to be attached before production","stage2_evidence_fields":["public_event_or_disclosure","relative_strength"],"stage3_evidence_fields":[],"stage4b_evidence_fields":["price_only_local_peak","valuation_blowoff"],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/439/439090/2023.csv|atlas/ohlcv_tradable_by_symbol_year/439/439090/2024.csv","profile_path":"atlas/symbol_profiles/439/439090.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":27.4,"MFE_90D_pct":27.4,"MFE_180D_pct":27.4,"MFE_1Y_pct":null,"MFE_2Y_pct":null,"MAE_30D_pct":-35.1,"MAE_90D_pct":-51.8,"MAE_180D_pct":-52.0,"MAE_1Y_pct":null,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2023-06-09","peak_price":53000,"drawdown_after_peak_pct":-62.3,"green_lateness_ratio":null,"four_b_local_peak_proximity":1.0,"four_b_full_window_peak_proximity":1.0,"four_b_timing_verdict":"price_only_local_4B_valid_as_guard_but_not_positive_stage","four_b_evidence_type":["price_only","valuation_blowoff"],"four_c_protection_label":"thesis_break_watch_only","trigger_outcome_label":"false_positive_green","current_profile_verdict":"current_profile_false_positive","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"G_C20_439090_20230608","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"narrative_only","case_id":"C20_R5L25_278470_NARR","symbol":"278470","company_name":"에이피알","large_sector_id":"L5_CONSUMER_BRAND_DISTRIBUTION","canonical_archetype_id":"C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION","reason":"corporate_action_candidate_dates include 2024-10-31, which overlaps plausible 2024 180D windows; block from weight calibration","price_source":"Songdaiki/stock-web","usage":"not_weight_calibration"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"C20_R5L25_003230","trigger_id":"TR_C20_003230_20240517_S2A","symbol":"003230","large_sector_id":"L5_CONSUMER_BRAND_DISTRIBUTION","canonical_archetype_id":"C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION","raw_component_scores_before":{"contract_score":0,"backlog_visibility_score":3,"margin_bridge_score":7,"revision_score":7,"relative_strength_score":6,"customer_quality_score":8,"policy_or_regulatory_score":0,"valuation_repricing_score":5,"execution_risk_score":2,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_before":86,"stage_label_before":"Stage3-Yellow_near_Green","raw_component_scores_after":{"contract_score":0,"backlog_visibility_score":3,"margin_bridge_score":7,"revision_score":7,"relative_strength_score":6,"customer_quality_score":8,"policy_or_regulatory_score":0,"valuation_repricing_score":5,"execution_risk_score":2,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0,"channel_reorder_score":8},"weighted_score_after":87,"stage_label_after":"Stage3-Green-shadow","changed_components":["channel_reorder_score"],"component_delta_explanation":"C20 export-channel reorder bonus bridges visible global demand to revision","MFE_90D_pct":60.8,"MAE_90D_pct":0.0,"score_return_alignment_label":"aligned","current_profile_verdict":"current_profile_correct"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"C20_R5L25_257720","trigger_id":"TR_C20_257720_20240516_S2A","symbol":"257720","large_sector_id":"L5_CONSUMER_BRAND_DISTRIBUTION","canonical_archetype_id":"C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION","raw_component_scores_before":{"contract_score":0,"backlog_visibility_score":4,"margin_bridge_score":5,"revision_score":5,"relative_strength_score":8,"customer_quality_score":6,"policy_or_regulatory_score":0,"valuation_repricing_score":7,"execution_risk_score":4,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_before":82,"stage_label_before":"Stage3-Yellow","raw_component_scores_after":{"contract_score":0,"backlog_visibility_score":4,"margin_bridge_score":5,"revision_score":5,"relative_strength_score":8,"customer_quality_score":6,"policy_or_regulatory_score":0,"valuation_repricing_score":7,"execution_risk_score":4,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0,"channel_reorder_score":8,"positioning_overheat_score":6},"weighted_score_after":83.5,"stage_label_after":"Stage3-Yellow_plus_4B_watch","changed_components":["channel_reorder_score","positioning_overheat_score"],"component_delta_explanation":"C20 distributor sell-through gets positive bridge but later post-peak drawdown activates 4B guard","MFE_90D_pct":87.5,"MAE_90D_pct":-10.4,"score_return_alignment_label":"high_mfe_high_drawdown","current_profile_verdict":"current_profile_too_late"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"C20_R5L25_018290","trigger_id":"TR_C20_018290_20240516_S2A","symbol":"018290","large_sector_id":"L5_CONSUMER_BRAND_DISTRIBUTION","canonical_archetype_id":"C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION","raw_component_scores_before":{"contract_score":0,"backlog_visibility_score":3,"margin_bridge_score":5,"revision_score":5,"relative_strength_score":7,"customer_quality_score":6,"policy_or_regulatory_score":0,"valuation_repricing_score":6,"execution_risk_score":3,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_before":80,"stage_label_before":"Stage3-Yellow","raw_component_scores_after":{"contract_score":0,"backlog_visibility_score":3,"margin_bridge_score":5,"revision_score":5,"relative_strength_score":7,"customer_quality_score":6,"policy_or_regulatory_score":0,"valuation_repricing_score":6,"execution_risk_score":3,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0,"channel_reorder_score":7},"weighted_score_after":81,"stage_label_after":"Stage3-Yellow_plus","changed_components":["channel_reorder_score"],"component_delta_explanation":"single-brand export reorder path modestly improves score but does not force Green","MFE_90D_pct":56.6,"MAE_90D_pct":-2.7,"score_return_alignment_label":"aligned","current_profile_verdict":"current_profile_correct"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"C20_R5L25_439090","trigger_id":"TR_C20_439090_20230608_IPO","symbol":"439090","large_sector_id":"L5_CONSUMER_BRAND_DISTRIBUTION","canonical_archetype_id":"C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION","raw_component_scores_before":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":0,"revision_score":0,"relative_strength_score":9,"customer_quality_score":2,"policy_or_regulatory_score":0,"valuation_repricing_score":8,"execution_risk_score":7,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_before":70,"stage_label_before":"Stage2-watch_false_Yellow_risk","raw_component_scores_after":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":0,"revision_score":0,"relative_strength_score":2,"customer_quality_score":2,"policy_or_regulatory_score":0,"valuation_repricing_score":8,"execution_risk_score":8,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0,"channel_reorder_score":0},"weighted_score_after":58,"stage_label_after":"Blocked_narrative_only","changed_components":["relative_strength_score","execution_risk_score","channel_reorder_score"],"component_delta_explanation":"IPO/global-brand hype guard prevents positive Stage2/Yellow without repeat-order or margin bridge","MFE_90D_pct":27.4,"MAE_90D_pct":-51.8,"score_return_alignment_label":"aligned_after_guard","current_profile_verdict":"current_profile_false_positive"}
{"row_type":"residual_contribution","round":"R5","loop":"25","large_sector_id":"L5_CONSUMER_BRAND_DISTRIBUTION","canonical_archetype_id":"C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION","new_independent_case_count":4,"reused_case_count":0,"new_symbol_count":4,"same_archetype_new_symbol_count":4,"new_trigger_family_count":4,"same_archetype_new_trigger_family_count":4,"positive_case_count":3,"counterexample_count":1,"current_profile_error_count":2,"tested_existing_calibrated_axes":["stage2_actionable_evidence_bonus","stage3_green_revision_min","price_only_blowoff_blocks_positive_stage","full_4b_requires_non_price_evidence"],"residual_error_types_found":["C20_green_too_late_for_distributor_sellthrough","C20_false_positive_ipo_global_brand_hype"],"loop_contribution_label":"canonical_archetype_rule_candidate","do_not_propose_new_weight_delta":false,"auto_selected_coverage_gap":"C20 lacked balanced positive/counterexample split for global distribution rerating vs IPO hype"}
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
next_round = R7
next_large_sector_id = L7_BIO_HEALTHCARE_MEDICAL
next_canonical_archetype_id = C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION
next_loop_objective = counterexample_mining + 4C_thesis_break_timing_test
reason = R5/C20 now has at least one positive/counterexample set; R7/C23 likely needs more approval-to-commercialization positives and commercialization-failure counterexamples.
```

## 28. Source Notes

Primary price source:

```text
Songdaiki/stock-web
manifest = atlas/manifest.json
schema = atlas/schema.json
universe = atlas/universe/all_symbols.csv
price_basis = tradable_raw
price_adjustment_status = raw_unadjusted_marcap
stock_web_manifest_max_date = 2026-02-20
```

Key stock-web citations used in this MD:

- Manifest: fileciteturn529file0
- Profiles: 삼양식품 fileciteturn541file0; 실리콘투 fileciteturn546file0; 브이티 fileciteturn548file0 fileciteturn549file0; 마녀공장 fileciteturn550file0; 에이피알 narrative exclusion fileciteturn547file0
- OHLC shards: 삼양식품 fileciteturn543file0 fileciteturn544file0 fileciteturn545file0; 실리콘투 fileciteturn552file0 fileciteturn553file0 fileciteturn554file0; 브이티 fileciteturn555file0 fileciteturn556file0 fileciteturn557file0; 마녀공장 fileciteturn551file0 fileciteturn558file0

External narrative source used only as supporting context for Samyang’s export-driven mechanism: citeturn357762news2
