# E2R Stock-Web v12 Residual Research — R5 Loop 87 / L5 / C18

## 0. Research Metadata

```json
{
  "research_session": "post_calibrated_sector_archetype_residual_research",
  "mode": "historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12",
  "scheduled_round": "R5",
  "scheduled_loop": 87,
  "round_schedule_status": "valid",
  "round_sector_consistency": "pass",
  "completed_round": "R5",
  "completed_loop": 87,
  "computed_next_round": "R6",
  "computed_next_loop": 87,
  "large_sector_id": "L5_CONSUMER_BRAND_DISTRIBUTION",
  "canonical_archetype_id": "C18_CONSUMER_EXPORT_CHANNEL_REORDER",
  "fine_archetype_id": "K_BEAUTY_ODM_BRAND_AND_FOOD_EXPORT_CHANNEL_REORDER_SELLTHROUGH_MARGIN_BRIDGE_VS_CONSUMER_DEFENSIVE_LOW_MFE_FADE",
  "loop_objective": [
    "coverage_gap_fill",
    "counterexample_mining",
    "consumer_export_channel_reorder_guardrail",
    "beauty_brand_ODM_channel_reorder_to_sellthrough_margin_bridge_test",
    "food_defensive_export_theme_low_MFE_false_positive_test",
    "local_4B_timing_after_consumer_export_MFE",
    "hard_4C_non_price_reorder_channel_or_margin_break_protection",
    "source_proxy_runtime_promotion_blocker",
    "high_MAE_guardrail",
    "canonical_archetype_compression",
    "source_repair_queue_creation"
  ],
  "price_source": "Songdaiki/stock-web",
  "price_basis": "tradable_raw",
  "price_adjustment_status": "raw_unadjusted_marcap",
  "stock_web_manifest_max_date": "2026-02-20",
  "production_scoring_changed": false,
  "shadow_weight_only": true,
  "handoff_prompt_executed_now": false,
  "do_not_propose_new_weight_delta": true
}
```

## 1. Current Calibrated Profile Assumption

```text
current_default_profile_proxy = e2r_2_1_stock_web_calibrated
previous_baseline_reference = e2r_2_0_baseline
production_scoring_changed = false
shadow_weight_only = true
handoff_prompt_executed_now = false
```

This file is a standalone historical calibration / sector-archetype residual research artifact. It does not patch `stock_agent`, does not run live discovery, and does not propose immediate production scoring changes.

## 2. Round / Large Sector / Canonical Archetype Scope

```text
scheduled_round = R5
scheduled_loop = 87
allowed_large_sector = L5_CONSUMER_BRAND_DISTRIBUTION
selected_large_sector = L5_CONSUMER_BRAND_DISTRIBUTION
selected_canonical_archetype_id = C18_CONSUMER_EXPORT_CHANNEL_REORDER
computed_next_round = R6
computed_next_loop = 87
round_schedule_status = valid
round_sector_consistency = pass
```

R5 is the consumer / brand / distribution round. This run selects C18 because loop87 has just reached R5 and recent R5 work already covered C19/C20 routes. The selected route is K-beauty brand/ODM and defensive food export/channel reorder.

The tested mechanism:

```text
consumer export / K-beauty / food channel reorder headline
→ channel sell-through
→ reorder cadence and inventory turn
→ ASP / discount control and customer or channel quality
→ gross / OP margin conversion
→ durable rerating or consumer-theme fade
```

C18 is the store shelf plus reorder ticket. A headline can move the display, but sell-through and reorder determine whether inventory leaves the warehouse twice.

## 3. Previous Coverage / Duplicate Avoidance Check

No-Repeat is used only as a duplicate ledger.

```text
hard_duplicate_key = canonical_archetype_id + symbol + trigger_type + entry_date
```

C18 top-covered symbols include `003230`, `005180`, `004370`, `192820`, `097950`, and `271560`. This run avoids that top-covered set and uses:

```text
214420 / 토니모리
950140 / 잉글우드랩
007310 / 오뚜기
```

All three are treated as new independent C18 consumer-export/channel-reorder cases for this loop. No hard duplicate is intentionally reused.

## 4. Stock-Web OHLC Input / Price Source Validation

```text
price_source = Songdaiki/stock-web
source_basis = FinanceData/marcap transformed into symbol-year CSV shards
price_basis = tradable_raw
price_adjustment_status = raw_unadjusted_marcap
manifest_max_date = 2026-02-20
```

Per-symbol profile status:

| symbol | company | profile path | corporate-action caveat |
|---|---|---|---|
| 214420 | 토니모리 | `atlas/symbol_profiles/214/214420.json` | old 2022 CA candidate; selected 2024 forward window clean |
| 950140 | 잉글우드랩 | `atlas/symbol_profiles/950/950140.json` | no profile-level CA candidate |
| 007310 | 오뚜기 | `atlas/symbol_profiles/007/007310.json` | no profile-level CA candidate |

## 5. Historical Eligibility Gate

| case_id | symbol | entry_date | entry_price | forward window | 180D status | calibration_usable |
|---|---:|---|---:|---:|---|---|
| R5L87-C18-01 | 214420 | 2024-02-13 | 5,960 | 180D | clean | true |
| R5L87-C18-02 | 950140 | 2024-02-13 | 13,790 | 180D | clean | true |
| R5L87-C18-03 | 007310 | 2024-02-13 | 412,000 | 180D | clean | true |

## 6. Canonical Archetype Compression Map

| canonical_archetype_id | fine/deep route | keep / reject logic |
|---|---|---|
| C18_CONSUMER_EXPORT_CHANNEL_REORDER | K_BEAUTY_BRAND_EXPORT_REORDER | keep Stage2 with sell-through, reorder cadence, inventory turn and margin bridge |
| C18_CONSUMER_EXPORT_CHANNEL_REORDER | K_BEAUTY_ODM_US_CHANNEL_REORDER | keep Stage2 with high-MAE/local-4B watch until customer/order/margin bridge is repaired |
| C18_CONSUMER_EXPORT_CHANNEL_REORDER | DEFENSIVE_FOOD_EXPORT_LOW_MFE_FADE | reject defensive food export/channel language when MFE is too low and bridge evidence is absent |

## 7. Case Selection Summary

| case_id | symbol | company | trigger_type | entry_date | entry_price | MFE_180D_pct | MAE_180D_pct | current_profile_verdict |
|---|---:|---|---|---|---:|---:|---:|---|
| R5L87-C18-01 | 214420 | 토니모리 | Stage2-Actionable | 2024-02-13 | 5,960 | 128.19 | -10.91 | current_profile_partially_correct_local_4B_reorder_margin_watch_needed |
| R5L87-C18-02 | 950140 | 잉글우드랩 | Stage2-Actionable | 2024-02-13 | 13,790 | 81.29 | -20.23 | current_profile_partially_correct_high_MAE_local_4B_watch_needed |
| R5L87-C18-03 | 007310 | 오뚜기 | Stage2-FalsePositive | 2024-02-13 | 412,000 | 7.65 | -7.52 | current_profile_false_positive_low_MFE_defensive_consumer |

## 8. Positive vs Counterexample Balance

```text
positive_case_count = 2
counterexample_count = 1
4B_or_4C_case_count = 3
calibration_usable_case_count = 3
new_independent_case_count = 3
```

## 9. Evidence Source Map

All selected evidence is currently `source_proxy_only=true / evidence_url_pending=true`.

This MD creates a source-repair queue and a C18 shadow guardrail candidate. It must not be promoted directly into runtime weights until a later source-repair pass attaches primary evidence URLs: channel sell-through, reorder cadence, inventory turn, customer/channel quality, ASP/discount control, gross/OP margin bridge, disclosure or report evidence.

## 10. Price Data Source Map

| symbol | shard path | profile path |
|---|---|---|
| 214420 | `atlas/ohlcv_tradable_by_symbol_year/214/214420/2024.csv` | `atlas/symbol_profiles/214/214420.json` |
| 950140 | `atlas/ohlcv_tradable_by_symbol_year/950/950140/2024.csv` | `atlas/symbol_profiles/950/950140.json` |
| 007310 | `atlas/ohlcv_tradable_by_symbol_year/007/007310/2024.csv` | `atlas/symbol_profiles/007/007310.json` |

## 11. Case-by-Case Trigger Grid

### Case 1 — 214420 / 토니모리

C18 K-beauty brand export/channel reorder positive with local 4B watch. The February entry produced a large MFE into June, but the post-peak drawdown shows that brand heat needs sell-through, channel inventory and margin bridge repair before clean Green.

### Case 2 — 950140 / 잉글우드랩

C18 K-beauty ODM / US channel reorder positive with high-volatility watch. The price path produced a strong MFE into July, but deep intermediate drawdowns mean it should stay Stage2-Actionable plus local 4B/reorder-margin watch until customer order and margin evidence are repaired.

### Case 3 — 007310 / 오뚜기

C18 defensive food export / channel reorder low-MFE false positive. The 180D MFE was too small relative to the evidence gap. This rejects defensive food/channel language unless export acceleration, sell-through and margin bridge are explicit.

## 12. Trigger-Level OHLC Backtest Tables

| symbol | entry | MFE30 | MAE30 | MFE90 | MAE90 | MFE180 | MAE180 | peak | post-peak DD |
|---|---:|---:|---:|---:|---:|---:|---:|---|---:|
| 214420 | 5,960 | 33.22 | -10.91 | 128.19 | -10.91 | 128.19 | -10.91 | 2024-06-27 / 13,600 | -44.85 |
| 950140 | 13,790 | 20.38 | -13.71 | 74.40 | -20.23 | 81.29 | -20.23 | 2024-07-24 / 25,000 | -55.32 |
| 007310 | 412,000 | 1.46 | -7.52 | 7.65 | -7.52 | 7.65 | -7.52 | 2024-06-26 / 443,500 | -12.85 |

## 13. Current Calibrated Profile Stress Test

| case_id | P0 likely behavior | actual path | verdict |
|---|---|---|---|
| R5L87-C18-01 | Stage2-Actionable if K-beauty reorder bridge exists | large MFE, later drawdown | partially correct; local 4B/reorder-margin watch needed |
| R5L87-C18-02 | Stage2-Actionable if ODM customer/order bridge exists | large MFE and high volatility | partially correct; high-MAE/local-4B watch needed |
| R5L87-C18-03 | risk of treating defensive food export as Stage2 | low MFE / weak alpha | false positive |

## 14. Stage2 / Yellow / Green Comparison

```text
green_lateness_ratio = not_applicable
reason = no confirmed Stage3-Green trigger is assigned in this residual MD
```

For C18, the residual is whether consumer export/channel reorder MFE becomes clean Stage2/Green before sell-through, reorder cadence, inventory turn and margin bridge are proven.

## 15. 4B Local vs Full-window Timing Audit

| case_id | local proximity | full-window proximity | verdict |
|---|---:|---:|---|
| R5L87-C18-01 | 0.82 | 0.72 | local 4B watch after K-beauty brand MFE if channel sell-through/reorder margin bridge stalls |
| R5L87-C18-02 | 0.82 | 0.72 | local 4B watch after ODM MFE if customer reorder margin bridge stalls |
| R5L87-C18-03 | 0.35 | 0.30 | food defensive export theme rejected without reorder/sell-through/pricing margin bridge |

## 16. 4C Protection Audit

No hard 4C is promoted from this file.

```text
four_c_protection_label = hard_4C_requires_non_price_channel_reorder_loss_or_margin_break
hard_4c_price_only_allowed = false
```

Price drawdown alone is not hard 4C. C18 hard 4C requires confirmed channel reorder collapse, inventory impairment, sell-through failure, ASP/discount compression, customer loss or margin thesis break.

## 17. Sector / Canonical Rule Candidate

```text
rule_scope = no_new_global_rule
canonical_archetype_rule_candidate = C18_consumer_export_sellthrough_reorder_inventory_margin_bridge_required
confidence = low
production_scoring_changed = false
shadow_weight_only = true
```

## 18. Before / After Backtest Comparison

| profile | eligible triggers | avg MFE90 | avg MAE90 | false-positive behavior | verdict |
|---|---:|---:|---:|---|---|
| P0 e2r_2_1_stock_web_calibrated_proxy | 3 | 70.08 | -12.89 | may over-credit consumer export/reorder theme without bridge | needs C18 sell-through/reorder margin repair |
| P1 canonical shadow bridge profile | 3 | keeps 214420/950140 with watch | demotes 007310 | better alignment, source repair required |

## 19. Coverage Matrix

| large_sector_id | canonical_archetype_id | fine_archetype_id | positive | counterexample | 4B | 4C | new cases | reused | usable triggers | current errors | canonical rule |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| L5_CONSUMER_BRAND_DISTRIBUTION | C18_CONSUMER_EXPORT_CHANNEL_REORDER | K_BEAUTY_ODM_BRAND_AND_FOOD_EXPORT_CHANNEL_REORDER_SELLTHROUGH_MARGIN_BRIDGE_VS_CONSUMER_DEFENSIVE_LOW_MFE_FADE | 2 | 1 | 3-watch | 0-hard | 3 | 0 | 3 | 1 | yes |

## 20. Residual Contribution Summary

```text
new_independent_case_count: 3
reused_case_count: 0
new_symbol_count: 3
new_trigger_family_count: 3
tested_existing_calibrated_axes:
  - stage2_actionable_evidence_bonus
  - price_only_blowoff_blocks_positive_stage
  - full_4b_requires_non_price_evidence
  - hard_4c_thesis_break_routes_to_4c
  - source_proxy_only_blocks_runtime_promotion
  - high_MAE_guardrail
  - local_4B_watch_before_full_4B_when_MFE_outruns_bridge
residual_error_types_found:
  - consumer_export_theme_false_positive_low_MFE
  - K_beauty_channel_reorder_sellthrough_margin_bridge_required
  - ODM_export_high_MAE_local_4B_watch
  - source_proxy_runtime_promotion_risk
  - hard_4C_requires_non_price_reorder_channel_or_margin_break
new_axis_proposed: false
existing_axis_strengthened:
  - C18_consumer_export_sellthrough_reorder_inventory_margin_bridge_required
  - source_proxy_only_blocks_runtime_promotion
  - local_4B_watch_before_full_4B_when_MFE_outruns_bridge
  - high_MAE_blocks_clean_Green
do_not_propose_new_weight_delta: true
```

## 21. Validation Scope / Non-Validation Scope

Validated in this MD:

```text
- Stock-Web profile path exists for selected symbols
- Stock-Web tradable shard path exists for selected symbols
- entry_date / entry_price are taken from tradable_raw close
- MFE / MAE / peak / post-peak drawdown are computed from observed OHLC windows
- corporate-action windows are checked at profile level
- scheduled_round / scheduled_loop / large_sector consistency
```

Not validated in this MD:

```text
- primary evidence URL
- exact publication time
- sell-through and reorder data
- channel inventory and customer quality
- ASP / discount control
- gross/OP margin conversion
- production scoring implementation
```

## 22. Shadow Weight Calibration

```csv
row_type,axis,scope,large_sector_id,canonical_archetype_id,baseline_value,tested_value,delta,reason,backtest_effect,trigger_ids,calibration_usable_count,new_independent_case_count,counterexample_count,confidence,proposal_type,notes
shadow_weight,C18_consumer_export_sellthrough_reorder_inventory_margin_bridge_required,canonical_archetype_specific,L5_CONSUMER_BRAND_DISTRIBUTION,C18_CONSUMER_EXPORT_CHANNEL_REORDER,0,1,+1,"Require sell-through, reorder cadence, inventory turn, ASP/discount control, customer/channel quality and gross/OP margin conversion before clean Stage2/Green","keeps 214420/950140 with local 4B/reorder-margin watch; demotes 007310 low-MFE defensive consumer false positive","R5L87-C18-01-S2A-20240213|R5L87-C18-02-S2A-20240213|R5L87-C18-03-S2FP-20240213",3,3,1,low,canonical_shadow_only,"source repair required; not production"
```

## 23. Machine-Readable Rows

```jsonl
{"row_type": "price_source_validation", "source": "Songdaiki/stock-web", "source_url": "https://github.com/Songdaiki/stock-web", "manifest_path": "atlas/manifest.json", "schema_path": "atlas/schema.json", "universe_path": "atlas/universe/all_symbols.csv", "manifest_max_date": "2026-02-20", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "raw_shard_root": "atlas/ohlcv_raw_by_symbol_year", "validation_status": "usable_for_historical_calibration"}
{"row_type": "case", "case_id": "R5L87-C18-01", "symbol": "214420", "company_name": "토니모리", "round": "R5", "loop": 87, "large_sector_id": "L5_CONSUMER_BRAND_DISTRIBUTION", "canonical_archetype_id": "C18_CONSUMER_EXPORT_CHANNEL_REORDER", "fine_archetype_id": "K_BEAUTY_ODM_BRAND_AND_FOOD_EXPORT_CHANNEL_REORDER_SELLTHROUGH_MARGIN_BRIDGE_VS_CONSUMER_DEFENSIVE_LOW_MFE_FADE", "case_type": "K_beauty_brand_export_channel_reorder_positive_with_local_4B_watch", "positive_or_counterexample": "positive", "best_trigger": "R5L87-C18-01-S2A-20240213", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "large_K_beauty_MFE_but_channel_reorder_sellthrough_margin_bridge_required", "current_profile_verdict": "current_profile_partially_correct_local_4B_reorder_margin_watch_needed", "price_source": "Songdaiki/stock-web", "notes": "C18 K-beauty brand positives need export sell-through, channel reorder cadence, inventory turn, ASP/discount control and margin bridge before clean Green."}
{"row_type": "trigger", "trigger_id": "R5L87-C18-01-S2A-20240213", "case_id": "R5L87-C18-01", "symbol": "214420", "company_name": "토니모리", "round": "R5", "loop": 87, "large_sector_id": "L5_CONSUMER_BRAND_DISTRIBUTION", "canonical_archetype_id": "C18_CONSUMER_EXPORT_CHANNEL_REORDER", "fine_archetype_id": "K_BEAUTY_ODM_BRAND_AND_FOOD_EXPORT_CHANNEL_REORDER_SELLTHROUGH_MARGIN_BRIDGE_VS_CONSUMER_DEFENSIVE_LOW_MFE_FADE", "loop_objective": "coverage_gap_fill|counterexample_mining|consumer_export_channel_reorder_guardrail|sellthrough_reorder_margin_bridge|canonical_archetype_compression", "trigger_type": "Stage2-Actionable", "trigger_date": "2024-02-13", "evidence_available_at_that_date": "K-beauty brand export / channel reorder / tourist and global distribution proxy; primary sell-through, reorder and margin evidence pending", "evidence_source": "source_proxy_only; evidence_url_pending", "stage2_evidence_fields": ["consumer_export_proxy", "channel_reorder_proxy", "brand_or_ODM_restocking_proxy"], "stage3_evidence_fields": ["channel_sellthrough", "reorder_cadence", "inventory_turn", "ASP_discount_control", "customer_or_channel_quality", "gross_or_OP_margin_conversion"], "stage4b_evidence_fields": ["consumer_export_MFE_without_reorder_bridge", "post_peak_drawdown", "source_proxy_gap"], "stage4c_evidence_fields": ["hard_channel_reorder_loss_or_margin_break_watch_only"], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/214/214420/2024.csv", "profile_path": "atlas/symbol_profiles/214/214420.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "entry_date": "2024-02-13", "entry_price": 5960, "MFE_30D_pct": 33.22, "MAE_30D_pct": -10.91, "MFE_90D_pct": 128.19, "MAE_90D_pct": -10.91, "MFE_180D_pct": 128.19, "MAE_180D_pct": -10.91, "peak_date": "2024-06-27", "peak_price": 13600, "drawdown_after_peak_pct": -44.85, "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": 0.82, "four_b_full_window_peak_proximity": 0.72, "four_b_timing_verdict": "local_4B_watch_after_K_beauty_brand_MFE_if_channel_sellthrough_reorder_margin_bridge_stalls", "four_b_evidence_type": ["consumer_export_MFE_without_reorder_margin_bridge", "post_peak_drawdown", "source_proxy_gap"], "four_c_protection_label": "hard_4C_requires_non_price_channel_reorder_loss_or_margin_break", "trigger_outcome_label": "large_K_beauty_MFE_but_channel_reorder_sellthrough_margin_bridge_required", "current_profile_verdict": "current_profile_partially_correct_local_4B_reorder_margin_watch_needed", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_2024_window_after_old_2022_CA_candidate", "same_entry_group_id": "R5L87-C18-01", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R5L87-C18-01", "trigger_id": "R5L87-C18-01-S2A-20240213", "symbol": "214420", "large_sector_id": "L5_CONSUMER_BRAND_DISTRIBUTION", "canonical_archetype_id": "C18_CONSUMER_EXPORT_CHANNEL_REORDER", "raw_component_scores_before": {"export_channel_score": 55, "sellthrough_score": 40, "reorder_cadence_score": 40, "inventory_turn_score": 35, "ASP_discount_control_score": 35, "gross_margin_bridge_score": 40, "customer_or_channel_quality_score": 45, "relative_strength_score": 70, "valuation_blowoff_risk_score": 75, "execution_risk_score": 60, "source_quality_score": 20, "4B_watch_score": 45, "4C_watch_score": 25}, "weighted_score_before": 76, "stage_label_before": "Stage2-Actionable", "raw_component_scores_after": {"export_channel_score": 55, "sellthrough_score": 40, "reorder_cadence_score": 40, "inventory_turn_score": 35, "ASP_discount_control_score": 35, "gross_margin_bridge_score": 40, "customer_or_channel_quality_score": 45, "relative_strength_score": 70, "valuation_blowoff_risk_score": 85, "execution_risk_score": 70, "source_quality_score": 10, "4B_watch_score": 85, "4C_watch_score": 25}, "weighted_score_after": 72, "stage_label_after": "Stage2-Actionable + local 4B/export-channel margin watch", "changed_components": ["sellthrough_score", "reorder_cadence_score", "inventory_turn_score", "ASP_discount_control_score", "gross_margin_bridge_score", "source_quality_score", "4B_watch_score"], "component_delta_explanation": "C18 requires consumer export/channel reorder MFE to convert into sell-through, reorder cadence, inventory turn, ASP/discount control and margin bridge before clean Stage2/Green.", "MFE_90D_pct": 128.19, "MAE_90D_pct": -10.91, "score_return_alignment_label": "large_K_beauty_MFE_but_channel_reorder_sellthrough_margin_bridge_required", "current_profile_verdict": "current_profile_partially_correct_local_4B_reorder_margin_watch_needed"}
{"row_type": "case", "case_id": "R5L87-C18-02", "symbol": "950140", "company_name": "잉글우드랩", "round": "R5", "loop": 87, "large_sector_id": "L5_CONSUMER_BRAND_DISTRIBUTION", "canonical_archetype_id": "C18_CONSUMER_EXPORT_CHANNEL_REORDER", "fine_archetype_id": "K_BEAUTY_ODM_BRAND_AND_FOOD_EXPORT_CHANNEL_REORDER_SELLTHROUGH_MARGIN_BRIDGE_VS_CONSUMER_DEFENSIVE_LOW_MFE_FADE", "case_type": "K_beauty_ODM_US_channel_reorder_positive_with_high_volatility_watch", "positive_or_counterexample": "positive", "best_trigger": "R5L87-C18-02-S2A-20240213", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "large_ODM_channel_MFE_but_high_MAE_and_reorder_margin_bridge_required", "current_profile_verdict": "current_profile_partially_correct_high_MAE_local_4B_watch_needed", "price_source": "Songdaiki/stock-web", "notes": "C18 ODM positives need customer reorder, sell-through, channel inventory, utilization and gross/OP margin conversion before clean Green."}
{"row_type": "trigger", "trigger_id": "R5L87-C18-02-S2A-20240213", "case_id": "R5L87-C18-02", "symbol": "950140", "company_name": "잉글우드랩", "round": "R5", "loop": 87, "large_sector_id": "L5_CONSUMER_BRAND_DISTRIBUTION", "canonical_archetype_id": "C18_CONSUMER_EXPORT_CHANNEL_REORDER", "fine_archetype_id": "K_BEAUTY_ODM_BRAND_AND_FOOD_EXPORT_CHANNEL_REORDER_SELLTHROUGH_MARGIN_BRIDGE_VS_CONSUMER_DEFENSIVE_LOW_MFE_FADE", "loop_objective": "coverage_gap_fill|counterexample_mining|consumer_export_channel_reorder_guardrail|sellthrough_reorder_margin_bridge|canonical_archetype_compression", "trigger_type": "Stage2-Actionable", "trigger_date": "2024-02-13", "evidence_available_at_that_date": "K-beauty ODM / US channel reorder / global customer restocking proxy; primary customer order, sell-through and margin evidence pending", "evidence_source": "source_proxy_only; evidence_url_pending", "stage2_evidence_fields": ["consumer_export_proxy", "channel_reorder_proxy", "brand_or_ODM_restocking_proxy"], "stage3_evidence_fields": ["channel_sellthrough", "reorder_cadence", "inventory_turn", "ASP_discount_control", "customer_or_channel_quality", "gross_or_OP_margin_conversion"], "stage4b_evidence_fields": ["consumer_export_MFE_without_reorder_bridge", "post_peak_drawdown", "source_proxy_gap"], "stage4c_evidence_fields": ["hard_channel_reorder_loss_or_margin_break_watch_only"], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/950/950140/2024.csv", "profile_path": "atlas/symbol_profiles/950/950140.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "entry_date": "2024-02-13", "entry_price": 13790, "MFE_30D_pct": 20.38, "MAE_30D_pct": -13.71, "MFE_90D_pct": 74.4, "MAE_90D_pct": -20.23, "MFE_180D_pct": 81.29, "MAE_180D_pct": -20.23, "peak_date": "2024-07-24", "peak_price": 25000, "drawdown_after_peak_pct": -55.32, "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": 0.82, "four_b_full_window_peak_proximity": 0.72, "four_b_timing_verdict": "local_4B_watch_after_ODM_MFE_if_customer_reorder_margin_bridge_stalls", "four_b_evidence_type": ["consumer_export_MFE_without_reorder_margin_bridge", "post_peak_drawdown", "source_proxy_gap"], "four_c_protection_label": "hard_4C_requires_non_price_channel_reorder_loss_or_margin_break", "trigger_outcome_label": "large_ODM_channel_MFE_but_high_MAE_and_reorder_margin_bridge_required", "current_profile_verdict": "current_profile_partially_correct_high_MAE_local_4B_watch_needed", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_2024_window_no_profile_CA_candidate", "same_entry_group_id": "R5L87-C18-02", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R5L87-C18-02", "trigger_id": "R5L87-C18-02-S2A-20240213", "symbol": "950140", "large_sector_id": "L5_CONSUMER_BRAND_DISTRIBUTION", "canonical_archetype_id": "C18_CONSUMER_EXPORT_CHANNEL_REORDER", "raw_component_scores_before": {"export_channel_score": 55, "sellthrough_score": 40, "reorder_cadence_score": 40, "inventory_turn_score": 35, "ASP_discount_control_score": 35, "gross_margin_bridge_score": 40, "customer_or_channel_quality_score": 45, "relative_strength_score": 70, "valuation_blowoff_risk_score": 75, "execution_risk_score": 60, "source_quality_score": 20, "4B_watch_score": 45, "4C_watch_score": 25}, "weighted_score_before": 76, "stage_label_before": "Stage2-Actionable", "raw_component_scores_after": {"export_channel_score": 55, "sellthrough_score": 40, "reorder_cadence_score": 40, "inventory_turn_score": 35, "ASP_discount_control_score": 35, "gross_margin_bridge_score": 40, "customer_or_channel_quality_score": 45, "relative_strength_score": 70, "valuation_blowoff_risk_score": 85, "execution_risk_score": 70, "source_quality_score": 10, "4B_watch_score": 85, "4C_watch_score": 25}, "weighted_score_after": 72, "stage_label_after": "Stage2-Actionable + local 4B/export-channel margin watch", "changed_components": ["sellthrough_score", "reorder_cadence_score", "inventory_turn_score", "ASP_discount_control_score", "gross_margin_bridge_score", "source_quality_score", "4B_watch_score"], "component_delta_explanation": "C18 requires consumer export/channel reorder MFE to convert into sell-through, reorder cadence, inventory turn, ASP/discount control and margin bridge before clean Stage2/Green.", "MFE_90D_pct": 74.4, "MAE_90D_pct": -20.23, "score_return_alignment_label": "large_ODM_channel_MFE_but_high_MAE_and_reorder_margin_bridge_required", "current_profile_verdict": "current_profile_partially_correct_high_MAE_local_4B_watch_needed"}
{"row_type": "case", "case_id": "R5L87-C18-03", "symbol": "007310", "company_name": "오뚜기", "round": "R5", "loop": 87, "large_sector_id": "L5_CONSUMER_BRAND_DISTRIBUTION", "canonical_archetype_id": "C18_CONSUMER_EXPORT_CHANNEL_REORDER", "fine_archetype_id": "K_BEAUTY_ODM_BRAND_AND_FOOD_EXPORT_CHANNEL_REORDER_SELLTHROUGH_MARGIN_BRIDGE_VS_CONSUMER_DEFENSIVE_LOW_MFE_FADE", "case_type": "food_defensive_export_channel_reorder_low_MFE_false_positive", "positive_or_counterexample": "counterexample", "best_trigger": "R5L87-C18-03-S2FP-20240213", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "low_MFE_consumer_defensive_reorder_false_positive", "current_profile_verdict": "current_profile_false_positive_low_MFE_defensive_consumer", "price_source": "Songdaiki/stock-web", "notes": "Defensive food channel-reorder language should not validate Stage2 unless export acceleration, channel sell-through, price/mix and margin conversion are explicit."}
{"row_type": "trigger", "trigger_id": "R5L87-C18-03-S2FP-20240213", "case_id": "R5L87-C18-03", "symbol": "007310", "company_name": "오뚜기", "round": "R5", "loop": 87, "large_sector_id": "L5_CONSUMER_BRAND_DISTRIBUTION", "canonical_archetype_id": "C18_CONSUMER_EXPORT_CHANNEL_REORDER", "fine_archetype_id": "K_BEAUTY_ODM_BRAND_AND_FOOD_EXPORT_CHANNEL_REORDER_SELLTHROUGH_MARGIN_BRIDGE_VS_CONSUMER_DEFENSIVE_LOW_MFE_FADE", "loop_objective": "coverage_gap_fill|counterexample_mining|consumer_export_channel_reorder_guardrail|sellthrough_reorder_margin_bridge|canonical_archetype_compression", "trigger_type": "Stage2-FalsePositive", "trigger_date": "2024-02-13", "evidence_available_at_that_date": "food export / defensive consumer channel reorder proxy without confirmed export acceleration, inventory turn or margin bridge", "evidence_source": "source_proxy_only; evidence_url_pending", "stage2_evidence_fields": ["consumer_export_proxy", "channel_reorder_proxy", "brand_or_ODM_restocking_proxy"], "stage3_evidence_fields": ["channel_sellthrough", "reorder_cadence", "inventory_turn", "ASP_discount_control", "customer_or_channel_quality", "gross_or_OP_margin_conversion"], "stage4b_evidence_fields": ["consumer_export_MFE_without_reorder_bridge", "post_peak_drawdown", "source_proxy_gap"], "stage4c_evidence_fields": ["hard_channel_reorder_loss_or_margin_break_watch_only"], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/007/007310/2024.csv", "profile_path": "atlas/symbol_profiles/007/007310.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "entry_date": "2024-02-13", "entry_price": 412000, "MFE_30D_pct": 1.46, "MAE_30D_pct": -7.52, "MFE_90D_pct": 7.65, "MAE_90D_pct": -7.52, "MFE_180D_pct": 7.65, "MAE_180D_pct": -7.52, "peak_date": "2024-06-26", "peak_price": 443500, "drawdown_after_peak_pct": -12.85, "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": 0.35, "four_b_full_window_peak_proximity": 0.3, "four_b_timing_verdict": "food_defensive_export_theme_rejected_without_reorder_sellthrough_pricing_margin_bridge", "four_b_evidence_type": ["consumer_export_MFE_without_reorder_margin_bridge", "post_peak_drawdown", "source_proxy_gap"], "four_c_protection_label": "hard_4C_requires_non_price_channel_reorder_loss_or_margin_break", "trigger_outcome_label": "low_MFE_consumer_defensive_reorder_false_positive", "current_profile_verdict": "current_profile_false_positive_low_MFE_defensive_consumer", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_2024_window_no_profile_CA_candidate", "same_entry_group_id": "R5L87-C18-03", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R5L87-C18-03", "trigger_id": "R5L87-C18-03-S2FP-20240213", "symbol": "007310", "large_sector_id": "L5_CONSUMER_BRAND_DISTRIBUTION", "canonical_archetype_id": "C18_CONSUMER_EXPORT_CHANNEL_REORDER", "raw_component_scores_before": {"export_channel_score": 25, "sellthrough_score": 10, "reorder_cadence_score": 5, "inventory_turn_score": 15, "ASP_discount_control_score": 15, "gross_margin_bridge_score": 10, "customer_or_channel_quality_score": 25, "relative_strength_score": 20, "valuation_blowoff_risk_score": 35, "execution_risk_score": 55, "source_quality_score": 15, "4B_watch_score": 55, "4C_watch_score": 25}, "weighted_score_before": 56, "stage_label_before": "Stage2-Watch/FalsePositive", "raw_component_scores_after": {"export_channel_score": 25, "sellthrough_score": 0, "reorder_cadence_score": 0, "inventory_turn_score": 15, "ASP_discount_control_score": 15, "gross_margin_bridge_score": 0, "customer_or_channel_quality_score": 25, "relative_strength_score": 20, "valuation_blowoff_risk_score": 35, "execution_risk_score": 55, "source_quality_score": 5, "4B_watch_score": 75, "4C_watch_score": 25}, "weighted_score_after": 43, "stage_label_after": "Rejected-Stage2 / Consumer defensive low-MFE RiskWatch", "changed_components": ["sellthrough_score", "reorder_cadence_score", "inventory_turn_score", "ASP_discount_control_score", "gross_margin_bridge_score", "source_quality_score", "4B_watch_score"], "component_delta_explanation": "C18 requires consumer export/channel reorder MFE to convert into sell-through, reorder cadence, inventory turn, ASP/discount control and margin bridge before clean Stage2/Green.", "MFE_90D_pct": 7.65, "MAE_90D_pct": -7.52, "score_return_alignment_label": "low_MFE_consumer_defensive_reorder_false_positive", "current_profile_verdict": "current_profile_false_positive_low_MFE_defensive_consumer"}
{"row_type": "shadow_weight", "axis": "C18_consumer_export_sellthrough_reorder_inventory_margin_bridge_required", "scope": "canonical_archetype_specific", "large_sector_id": "L5_CONSUMER_BRAND_DISTRIBUTION", "canonical_archetype_id": "C18_CONSUMER_EXPORT_CHANNEL_REORDER", "baseline_value": 0, "tested_value": 1, "delta": "+1", "reason": "Consumer export/channel reorder rerating requires sell-through, reorder cadence, inventory turn, ASP/discount control, customer/channel quality and gross/OP margin conversion; consumer theme or defensive food MFE without bridge fades into low-MFE or local 4B watch.", "backtest_effect": "keeps 214420/950140 with local 4B/reorder-margin watch; demotes 007310 low-MFE defensive consumer false positive", "trigger_ids": "R5L87-C18-01-S2A-20240213|R5L87-C18-02-S2A-20240213|R5L87-C18-03-S2FP-20240213", "calibration_usable_count": 3, "new_independent_case_count": 3, "counterexample_count": 1, "confidence": "low", "proposal_type": "canonical_shadow_only", "notes": "source_proxy_only/evidence_url_pending; not production"}
{"row_type": "residual_contribution", "round": "R5", "loop": 87, "large_sector_id": "L5_CONSUMER_BRAND_DISTRIBUTION", "canonical_archetype_id": "C18_CONSUMER_EXPORT_CHANNEL_REORDER", "new_independent_case_count": 3, "reused_case_count": 0, "new_symbol_count": 3, "new_trigger_family_count": 3, "tested_existing_calibrated_axes": ["stage2_actionable_evidence_bonus", "price_only_blowoff_blocks_positive_stage", "full_4b_requires_non_price_evidence", "hard_4c_thesis_break_routes_to_4c", "source_proxy_only_blocks_runtime_promotion", "high_MAE_guardrail", "local_4B_watch_before_full_4B_when_MFE_outruns_bridge"], "residual_error_types_found": ["consumer_export_theme_false_positive_low_MFE", "K_beauty_channel_reorder_sellthrough_margin_bridge_required", "ODM_export_high_MAE_local_4B_watch", "source_proxy_runtime_promotion_risk", "hard_4C_requires_non_price_reorder_channel_or_margin_break"], "loop_contribution_label": "canonical_archetype_rule_candidate", "do_not_propose_new_weight_delta": true}
```

## 24. Deferred Coding Agent Handoff Prompt

Use only `calibration_usable=true` rows. Do not treat `source_proxy_only/evidence_url_pending` rows as runtime promotion-ready. For C18, test a canonical guard requiring sell-through, reorder cadence, inventory turn, ASP/discount control, customer/channel quality and gross/OP margin conversion before clean Stage2/Green.

## 25. Next Round State

```text
completed_round = R5
completed_loop = 87
next_round = R6
next_loop = 87
round_schedule_status = valid
round_sector_consistency = pass
```

## 26. Source Notes

```text
MAIN_EXECUTION_PROMPT = docs/core/e2r_v12_prompt_round_scheduler_corrected.txt
NO_REPEAT_INDEX = docs/core/V12_Research_No_Repeat_Index.md
price_source = Songdaiki/stock-web
```
