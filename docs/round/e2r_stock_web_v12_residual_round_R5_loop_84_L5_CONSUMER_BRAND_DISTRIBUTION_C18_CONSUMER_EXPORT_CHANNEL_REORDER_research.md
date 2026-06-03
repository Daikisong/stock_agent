# E2R Stock-Web v12 Residual Research — R5 Loop 84 / L5 / C18

## 0. Research Metadata

```json
{
  "research_session": "post_calibrated_sector_archetype_residual_research",
  "mode": "historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12",
  "scheduled_round": "R5",
  "scheduled_loop": 84,
  "round_schedule_status": "valid",
  "round_sector_consistency": "pass",
  "completed_round": "R5",
  "completed_loop": 84,
  "computed_next_round": "R6",
  "computed_next_loop": 84,
  "large_sector_id": "L5_CONSUMER_BRAND_DISTRIBUTION",
  "canonical_archetype_id": "C18_CONSUMER_EXPORT_CHANNEL_REORDER",
  "fine_archetype_id": "K_BEAUTY_ODM_EXPORT_CHANNEL_REORDER_SELL_THROUGH_MARGIN_BRIDGE_VS_CHANNEL_THEME_OVERHEAT_FADE",
  "loop_objective": [
    "coverage_gap_fill",
    "counterexample_mining",
    "consumer_export_channel_reorder_guardrail",
    "sell_through_to_reorder_margin_bridge_test",
    "local_4B_timing_after_channel_MFE",
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
scheduled_loop = 84
allowed_large_sector = L5_CONSUMER_BRAND_DISTRIBUTION
selected_large_sector = L5_CONSUMER_BRAND_DISTRIBUTION
selected_canonical_archetype_id = C18_CONSUMER_EXPORT_CHANNEL_REORDER
computed_next_round = R6
computed_next_loop = 84
round_schedule_status = valid
round_sector_consistency = pass
```

R5 is the consumer / brand / distribution round. This run selects C18 because loop83 already tested C19, while C20 is the thickest R5 bucket. The test here is not “K-beauty went up.” It is whether export-channel evidence can walk through the retail pipe:

```text
export or global-channel headline
→ sell-through
→ reorder cadence
→ capacity fulfillment
→ customer concentration control
→ gross-margin conversion
→ durable rerating or local 4B / false-positive fade
```

A channel headline is a purchase order whisper. C18 only becomes durable when shelves empty, reorders repeat, and the margin line carries the story.

## 3. Previous Coverage / Duplicate Avoidance Check

No-Repeat is used only as a duplicate ledger.

```text
hard_duplicate_key = canonical_archetype_id + symbol + trigger_type + entry_date
```

C18 top-covered symbols include `003230`, `005180`, `004370`, `192820`, `097950`, and `271560`. This run avoids that top-covered set and uses:

```text
241710 / 코스메카코리아
950140 / 잉글우드랩
214420 / 토니모리
```

All three are treated as new independent C18 export-channel / reorder cases for this loop. No hard duplicate is intentionally reused.

## 4. Stock-Web OHLC Input / Price Source Validation

```text
price_source = Songdaiki/stock-web
source_basis = FinanceData/marcap transformed into symbol-year CSV shards
price_basis = tradable_raw
price_adjustment_status = raw_unadjusted_marcap
manifest_max_date = 2026-02-20
calibration_shard_root = atlas/ohlcv_tradable_by_symbol_year
```

Per-symbol profile status:

| symbol | company | profile path | corporate-action caveat |
|---|---|---|---|
| 241710 | 코스메카코리아 | `atlas/symbol_profiles/241/241710.json` | old 2018 CA candidates; selected 2024 forward window clean |
| 950140 | 잉글우드랩 | `atlas/symbol_profiles/950/950140.json` | no profile-level CA candidate |
| 214420 | 토니모리 | `atlas/symbol_profiles/214/214420.json` | old 2022 CA candidate; selected 2024 forward window clean |

## 5. Historical Eligibility Gate

| case_id | symbol | entry_date | entry_price | forward window | 180D status | calibration_usable |
|---|---:|---|---:|---:|---|---|
| R5L84-C18-01 | 241710 | 2024-04-01 | 38,200 | 180D | clean | true |
| R5L84-C18-02 | 950140 | 2024-02-21 | 15,480 | 180D | clean | true |
| R5L84-C18-03 | 214420 | 2024-06-26 | 12,860 | 180D | clean | true |

## 6. Canonical Archetype Compression Map

| canonical_archetype_id | fine/deep route | keep / reject logic |
|---|---|---|
| C18_CONSUMER_EXPORT_CHANNEL_REORDER | K_BEAUTY_ODM_EXPORT_REORDER_MARGIN_BRIDGE | keep Stage2 only with export sell-through, reorder cadence, fulfillment and margin bridge; add local 4B after large channel MFE |
| C18_CONSUMER_EXPORT_CHANNEL_REORDER | US_ODM_CHANNEL_HIGH_MAE_RISKWATCH | allow Stage2 only with high-MAE RiskWatch when MFE is real but customer/reorder durability is unrepaired |
| C18_CONSUMER_EXPORT_CHANNEL_REORDER | BRAND_CHANNEL_THEME_OVERHEAT_FADE | reject when brand/channel theme has low MFE and high MAE without reorder/margin bridge |

## 7. Case Selection Summary

| case_id | symbol | company | trigger_type | entry_date | entry_price | MFE_180D_pct | MAE_180D_pct | current_profile_verdict |
|---|---:|---|---|---|---:|---:|---:|---|
| R5L84-C18-01 | 241710 | 코스메카코리아 | Stage2-Actionable | 2024-04-01 | 38,200 | 157.85 | -9.55 | current_profile_partially_correct_local_4B_watch_needed |
| R5L84-C18-02 | 950140 | 잉글우드랩 | Stage2-Actionable | 2024-02-21 | 15,480 | 61.5 | -28.94 | current_profile_4B_too_late_high_MAE |
| R5L84-C18-03 | 214420 | 토니모리 | Stage2-FalsePositive | 2024-06-26 | 12,860 | 5.75 | -41.68 | current_profile_false_positive_high_MAE |

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

This MD therefore creates a source-repair queue and a C18 shadow guardrail candidate. It must not be promoted directly into runtime weights until a later source-repair pass attaches primary evidence URLs: export customs data, channel sell-through, reorder data, customer/channel concentration, ODM capacity utilization, gross-margin bridge, company disclosure or report evidence.

## 10. Price Data Source Map

| symbol | shard path | profile path |
|---|---|---|
| 241710 | `atlas/ohlcv_tradable_by_symbol_year/241/241710/2024.csv` | `atlas/symbol_profiles/241/241710.json` |
| 950140 | `atlas/ohlcv_tradable_by_symbol_year/950/950140/2024.csv` | `atlas/symbol_profiles/950/950140.json` |
| 214420 | `atlas/ohlcv_tradable_by_symbol_year/214/214420/2024.csv` | `atlas/symbol_profiles/214/214420.json` |

## 11. Case-by-Case Trigger Grid

### Case 1 — 241710 / 코스메카코리아

C18 high-MFE positive with local 4B watch. The entry path ultimately produced a large export/ODM rerating, but the size of the later move means the model should not wait for a full-window 4B if sell-through and margin confirmation stalls.

### Case 2 — 950140 / 잉글우드랩

C18 positive but high-MAE. The price path had large MFE, but early drawdown was too wide for a clean Green. It can remain Stage2-Actionable only with high-MAE RiskWatch until customer/reorder durability and gross-margin bridge are repaired.

### Case 3 — 214420 / 토니모리

C18 brand/channel theme false positive. The entry after the large prior move produced low MFE and deep MAE. This is the rejection case: channel or brand momentum does not equal reorder visibility.

## 12. Trigger-Level OHLC Backtest Tables

| symbol | entry | MFE30 | MAE30 | MFE90 | MAE90 | MFE180 | MAE180 | peak | post-peak DD |
|---|---:|---:|---:|---:|---:|---:|---:|---|---:|
| 241710 | 38,200 | 38.22 | -9.55 | 142.15 | -9.55 | 157.85 | -9.55 | 2024-09-27 / 98,500 | -22.94 |
| 950140 | 15,480 | 7.24 | -28.94 | 55.36 | -28.94 | 61.50 | -28.94 | 2024-07-24 / 25,000 | -55.32 |
| 214420 | 12,860 | 5.75 | -41.68 | 5.75 | -41.68 | 5.75 | -41.68 | 2024-06-27 / 13,600 | -44.85 |

## 13. Current Calibrated Profile Stress Test

| case_id | P0 likely behavior | actual path | verdict |
|---|---|---|---|
| R5L84-C18-01 | Stage2-Actionable if reorder/margin bridge exists | high MFE, later drawdown | partially correct; local 4B watch needed |
| R5L84-C18-02 | Stage2-Actionable if US channel reorder is over-credited | high MFE but high MAE | high-MAE RiskWatch needed |
| R5L84-C18-03 | risk of treating brand/channel momentum as Stage2 | low MFE / very high MAE | false positive |

## 14. Stage2 / Yellow / Green Comparison

```text
green_lateness_ratio = not_applicable
reason = no confirmed Stage3-Green trigger is assigned in this residual MD
```

For C18, the residual is not Green lateness. The residual is whether channel and export MFE becomes Stage2-Actionable before sell-through, reorder cadence, customer durability and gross-margin conversion are proven.

## 15. 4B Local vs Full-window Timing Audit

| case_id | local proximity | full-window proximity | verdict |
|---|---:|---:|---|
| R5L84-C18-01 | 0.88 | 0.78 | local 4B watch after export reorder MFE if sell-through bridge stalls |
| R5L84-C18-02 | 0.88 | 0.78 | local 4B and high-MAE RiskWatch when channel MFE outruns evidence |
| R5L84-C18-03 | 0.30 | 0.25 | channel theme overheat rejected without reorder/margin bridge |

## 16. 4C Protection Audit

No hard 4C is promoted from this file.

```text
four_c_protection_label = hard_4C_requires_non_price_reorder_or_customer_break
hard_4c_price_only_allowed = false
```

## 17. Sector-Specific Rule Candidate

```text
rule_scope = no_new_global_rule
sector_specific_rule_candidate = L5 export-channel rows need sell-through, reorder cadence, capacity fulfillment and margin bridge before clean Stage2/Green
confidence = low
reason = all evidence rows are source_proxy_only / evidence_url_pending
```

## 18. Canonical-Archetype Rule Candidate

```text
canonical_archetype_id = C18_CONSUMER_EXPORT_CHANNEL_REORDER
candidate_axis = C18_export_channel_sellthrough_reorder_margin_bridge_required
effect = keep channel positives with local 4B/high-MAE watch; demote brand/channel theme false positives
production_scoring_changed = false
shadow_weight_only = true
do_not_propose_new_weight_delta = true
```

## 19. Before / After Backtest Comparison

| profile | eligible triggers | avg MFE90 | avg MAE90 | false-positive behavior | verdict |
|---|---:|---:|---:|---|---|
| P0 e2r_2_1_stock_web_calibrated_proxy | 3 | 67.75 | -26.72 | may over-credit channel/export theme MFE | needs C18 bridge repair |
| P1 canonical shadow bridge profile | 3 | 98.76 on kept positives | -19.25 on kept positives | demotes 214420 | better alignment, source repair required |

## 20. Score-Return Alignment Matrix

| case_id | weighted before | label before | weighted after | label after | alignment |
|---|---:|---|---:|---|---|
| R5L84-C18-01 | 82 | Stage2-Actionable | 80 | Stage2-Actionable + local 4B watch | partially aligned |
| R5L84-C18-02 | 76 | Stage2-Actionable | 73 | Stage2-Actionable + high-MAE RiskWatch/local 4B watch | partially aligned |
| R5L84-C18-03 | 58 | Stage2-Watch/FalsePositive | 47 | Rejected-Stage2 / RiskWatch | improved |

## 21. Coverage Matrix

| large_sector_id | canonical_archetype_id | fine_archetype_id | positive | counterexample | 4B | 4C | new cases | reused | usable triggers | current errors | sector rule | canonical rule | coverage gap after |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---|---|---|
| L5_CONSUMER_BRAND_DISTRIBUTION | C18_CONSUMER_EXPORT_CHANNEL_REORDER | K_BEAUTY_ODM_EXPORT_CHANNEL_REORDER_SELL_THROUGH_MARGIN_BRIDGE_VS_CHANNEL_THEME_OVERHEAT_FADE | 2 | 1 | 3-watch | 0 | 3 | 0 | 3 | 2 | no | yes | source repair needed |

## 22. Residual Contribution Summary

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
  - hard_4c_thesis_break_routes_to_4c
  - source_proxy_only_blocks_runtime_promotion
  - high_MAE_guardrail
residual_error_types_found:
  - consumer_channel_theme_false_positive_high_MAE
  - export_sellthrough_reorder_margin_bridge_required
  - local_4B_late_after_channel_MFE
  - source_proxy_runtime_promotion_risk
  - high_MAE_positive_Green_blocker
new_axis_proposed: false
existing_axis_strengthened:
  - C18_export_channel_sellthrough_reorder_margin_bridge_required
  - source_proxy_only_blocks_runtime_promotion
  - local_4B_watch_before_full_4B_when_MFE_outruns_bridge
  - high_MAE_blocks_clean_Green
existing_axis_weakened: null
existing_axis_kept:
  - full_4b_requires_non_price_evidence
  - hard_4c_thesis_break_routes_to_4c
sector_specific_rule_candidate: null
canonical_archetype_rule_candidate: C18_export_channel_sellthrough_reorder_margin_bridge_required
no_new_signal_reason: null
loop_contribution_label: canonical_archetype_rule_candidate
do_not_propose_new_weight_delta: true
```

This loop adds 3 new independent cases, 1 counterexample, and 2 residual errors for R5/L5_CONSUMER_BRAND_DISTRIBUTION/C18_CONSUMER_EXPORT_CHANNEL_REORDER.

## 23. Validation Scope / Non-Validation Scope

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
- export customs or channel sell-through source
- reorder cadence
- customer concentration and capacity utilization
- gross-margin conversion
- production scoring implementation
```

## 24. Shadow Weight Calibration

```csv
row_type,axis,scope,large_sector_id,canonical_archetype_id,baseline_value,tested_value,delta,reason,backtest_effect,trigger_ids,calibration_usable_count,new_independent_case_count,counterexample_count,confidence,proposal_type,notes
shadow_weight,C18_export_channel_sellthrough_reorder_margin_bridge_required,canonical_archetype_specific,L5_CONSUMER_BRAND_DISTRIBUTION,C18_CONSUMER_EXPORT_CHANNEL_REORDER,0,1,+1,"Require export-channel sell-through, reorder cadence, capacity fulfillment and margin bridge before clean Stage2/Green","keeps 241710/950140 with local 4B or high-MAE RiskWatch; demotes 214420","R5L84-C18-01-S2A-20240401|R5L84-C18-02-S2A-20240221|R5L84-C18-03-S2FP-20240626",3,3,1,low,canonical_shadow_only,"source repair required; not production"
```

## 25. Machine-Readable Rows

```jsonl
{"row_type": "price_source_validation", "source": "Songdaiki/stock-web", "source_url": "https://github.com/Songdaiki/stock-web", "manifest_path": "atlas/manifest.json", "schema_path": "atlas/schema.json", "universe_path": "atlas/universe/all_symbols.csv", "manifest_max_date": "2026-02-20", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "raw_shard_root": "atlas/ohlcv_raw_by_symbol_year", "validation_status": "usable_for_historical_calibration"}
{"row_type": "case", "case_id": "R5L84-C18-01", "symbol": "241710", "company_name": "코스메카코리아", "round": "R5", "loop": 84, "large_sector_id": "L5_CONSUMER_BRAND_DISTRIBUTION", "canonical_archetype_id": "C18_CONSUMER_EXPORT_CHANNEL_REORDER", "fine_archetype_id": "K_BEAUTY_ODM_EXPORT_CHANNEL_REORDER_SELL_THROUGH_MARGIN_BRIDGE_VS_CHANNEL_THEME_OVERHEAT_FADE", "case_type": "K_beauty_ODM_export_channel_reorder_positive_with_local_4B_watch", "positive_or_counterexample": "positive", "best_trigger": "R5L84-C18-01-S2A-20240401", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "large_positive_MFE_but_local_4B_required", "current_profile_verdict": "current_profile_partially_correct_local_4B_watch_needed", "price_source": "Songdaiki/stock-web", "notes": "C18 can keep Stage2 only when export reorder, channel sell-through, capacity and gross-margin conversion are visible."}
{"row_type": "trigger", "trigger_id": "R5L84-C18-01-S2A-20240401", "case_id": "R5L84-C18-01", "symbol": "241710", "company_name": "코스메카코리아", "round": "R5", "loop": 84, "large_sector_id": "L5_CONSUMER_BRAND_DISTRIBUTION", "canonical_archetype_id": "C18_CONSUMER_EXPORT_CHANNEL_REORDER", "fine_archetype_id": "K_BEAUTY_ODM_EXPORT_CHANNEL_REORDER_SELL_THROUGH_MARGIN_BRIDGE_VS_CHANNEL_THEME_OVERHEAT_FADE", "loop_objective": "coverage_gap_fill|counterexample_mining|consumer_export_channel_reorder_guardrail|local_4B_timing_after_channel_MFE|canonical_archetype_compression", "trigger_type": "Stage2-Actionable", "trigger_date": "2024-04-01", "evidence_available_at_that_date": "K-beauty ODM export-channel reorder and margin leverage proxy; primary channel/sell-through evidence pending", "evidence_source": "source_proxy_only; evidence_url_pending", "stage2_evidence_fields": ["export_channel_proxy", "sell_through_proxy", "reorder_visibility_proxy"], "stage3_evidence_fields": ["confirmed_channel_reorder", "customer_concentration_control", "capacity_fulfillment", "gross_margin_conversion", "revision_confirmation"], "stage4b_evidence_fields": ["channel_MFE_without_reorder_bridge", "valuation_overheat", "post_peak_drawdown"], "stage4c_evidence_fields": ["hard_customer_reorder_break_watch_only"], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/241/241710/2024.csv", "profile_path": "atlas/symbol_profiles/241/241710.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "entry_date": "2024-04-01", "entry_price": 38200, "MFE_30D_pct": 38.22, "MFE_90D_pct": 142.15, "MFE_180D_pct": 157.85, "MFE_1Y_pct": null, "MFE_2Y_pct": null, "MAE_30D_pct": -9.55, "MAE_90D_pct": -9.55, "MAE_180D_pct": -9.55, "MAE_1Y_pct": null, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2024-09-27", "peak_price": 98500, "drawdown_after_peak_pct": -22.94, "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": 0.88, "four_b_full_window_peak_proximity": 0.78, "four_b_timing_verdict": "local_4B_watch_after_export_reorder_MFE_if_sell_through_margin_bridge_stalls", "four_b_evidence_type": ["channel_MFE_without_reorder_bridge", "post_peak_drawdown", "source_proxy_gap"], "four_c_protection_label": "hard_4C_requires_non_price_reorder_or_customer_break", "trigger_outcome_label": "large_positive_MFE_but_local_4B_required", "current_profile_verdict": "current_profile_partially_correct_local_4B_watch_needed", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window_after_old_2018_CA_candidates", "same_entry_group_id": "R5L84-C18-01", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R5L84-C18-01", "trigger_id": "R5L84-C18-01-S2A-20240401", "symbol": "241710", "large_sector_id": "L5_CONSUMER_BRAND_DISTRIBUTION", "canonical_archetype_id": "C18_CONSUMER_EXPORT_CHANNEL_REORDER", "raw_component_scores_before": {"export_channel_score": 55, "sell_through_score": 40, "reorder_visibility_score": 45, "customer_quality_score": 40, "capacity_fulfillment_score": 40, "gross_margin_bridge_score": 45, "revision_score": 50, "relative_strength_score": 65, "valuation_blowoff_risk_score": 60, "execution_risk_score": 40, "source_quality_score": 20, "4B_watch_score": 45}, "weighted_score_before": 82, "stage_label_before": "Stage2-Actionable", "raw_component_scores_after": {"export_channel_score": 55, "sell_through_score": 40, "reorder_visibility_score": 45, "customer_quality_score": 40, "capacity_fulfillment_score": 40, "gross_margin_bridge_score": 45, "revision_score": 50, "relative_strength_score": 65, "valuation_blowoff_risk_score": 60, "execution_risk_score": 40, "source_quality_score": 10, "4B_watch_score": 80}, "weighted_score_after": 80, "stage_label_after": "Stage2-Actionable + local 4B watch", "changed_components": ["sell_through_score", "reorder_visibility_score", "gross_margin_bridge_score", "source_quality_score", "execution_risk_score", "4B_watch_score"], "component_delta_explanation": "C18 requires export-channel sell-through, reorder cadence, capacity fulfillment and gross-margin bridge before clean Stage2/Green; channel-theme MFE alone is demoted or wrapped with local 4B watch.", "MFE_90D_pct": 142.15, "MAE_90D_pct": -9.55, "score_return_alignment_label": "large_positive_MFE_but_local_4B_required", "current_profile_verdict": "current_profile_partially_correct_local_4B_watch_needed"}
{"row_type": "case", "case_id": "R5L84-C18-02", "symbol": "950140", "company_name": "잉글우드랩", "round": "R5", "loop": 84, "large_sector_id": "L5_CONSUMER_BRAND_DISTRIBUTION", "canonical_archetype_id": "C18_CONSUMER_EXPORT_CHANNEL_REORDER", "fine_archetype_id": "K_BEAUTY_ODM_EXPORT_CHANNEL_REORDER_SELL_THROUGH_MARGIN_BRIDGE_VS_CHANNEL_THEME_OVERHEAT_FADE", "case_type": "US_ODM_export_channel_positive_but_high_MAE_risk", "positive_or_counterexample": "positive", "best_trigger": "R5L84-C18-02-S2A-20240221", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "high_MFE_high_MAE_positive_requires_RiskWatch", "current_profile_verdict": "current_profile_4B_too_late_high_MAE", "price_source": "Songdaiki/stock-web", "notes": "ODM export-channel rerating can be real, but customer/reorder durability and margin bridge must be repaired before clean Green."}
{"row_type": "trigger", "trigger_id": "R5L84-C18-02-S2A-20240221", "case_id": "R5L84-C18-02", "symbol": "950140", "company_name": "잉글우드랩", "round": "R5", "loop": 84, "large_sector_id": "L5_CONSUMER_BRAND_DISTRIBUTION", "canonical_archetype_id": "C18_CONSUMER_EXPORT_CHANNEL_REORDER", "fine_archetype_id": "K_BEAUTY_ODM_EXPORT_CHANNEL_REORDER_SELL_THROUGH_MARGIN_BRIDGE_VS_CHANNEL_THEME_OVERHEAT_FADE", "loop_objective": "coverage_gap_fill|counterexample_mining|consumer_export_channel_reorder_guardrail|local_4B_timing_after_channel_MFE|canonical_archetype_compression", "trigger_type": "Stage2-Actionable", "trigger_date": "2024-02-21", "evidence_available_at_that_date": "US-facing ODM / indie-brand channel reorder proxy without repaired sell-through and customer concentration details", "evidence_source": "source_proxy_only; evidence_url_pending", "stage2_evidence_fields": ["export_channel_proxy", "sell_through_proxy", "reorder_visibility_proxy"], "stage3_evidence_fields": ["confirmed_channel_reorder", "customer_concentration_control", "capacity_fulfillment", "gross_margin_conversion", "revision_confirmation"], "stage4b_evidence_fields": ["channel_MFE_without_reorder_bridge", "valuation_overheat", "post_peak_drawdown"], "stage4c_evidence_fields": ["hard_customer_reorder_break_watch_only"], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/950/950140/2024.csv", "profile_path": "atlas/symbol_profiles/950/950140.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "entry_date": "2024-02-21", "entry_price": 15480, "MFE_30D_pct": 7.24, "MFE_90D_pct": 55.36, "MFE_180D_pct": 61.5, "MFE_1Y_pct": null, "MFE_2Y_pct": null, "MAE_30D_pct": -28.94, "MAE_90D_pct": -28.94, "MAE_180D_pct": -28.94, "MAE_1Y_pct": null, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2024-07-24", "peak_price": 25000, "drawdown_after_peak_pct": -55.32, "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": 0.88, "four_b_full_window_peak_proximity": 0.78, "four_b_timing_verdict": "local_4B_and_high_MAE_RiskWatch_needed_when_channel_reorder_MFE_outruns_evidence", "four_b_evidence_type": ["channel_MFE_without_reorder_bridge", "post_peak_drawdown", "source_proxy_gap"], "four_c_protection_label": "hard_4C_requires_non_price_reorder_or_customer_break", "trigger_outcome_label": "high_MFE_high_MAE_positive_requires_RiskWatch", "current_profile_verdict": "current_profile_4B_too_late_high_MAE", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window_no_profile_CA_candidate", "same_entry_group_id": "R5L84-C18-02", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R5L84-C18-02", "trigger_id": "R5L84-C18-02-S2A-20240221", "symbol": "950140", "large_sector_id": "L5_CONSUMER_BRAND_DISTRIBUTION", "canonical_archetype_id": "C18_CONSUMER_EXPORT_CHANNEL_REORDER", "raw_component_scores_before": {"export_channel_score": 55, "sell_through_score": 40, "reorder_visibility_score": 45, "customer_quality_score": 40, "capacity_fulfillment_score": 40, "gross_margin_bridge_score": 45, "revision_score": 50, "relative_strength_score": 65, "valuation_blowoff_risk_score": 60, "execution_risk_score": 60, "source_quality_score": 20, "4B_watch_score": 45}, "weighted_score_before": 76, "stage_label_before": "Stage2-Actionable", "raw_component_scores_after": {"export_channel_score": 55, "sell_through_score": 40, "reorder_visibility_score": 45, "customer_quality_score": 40, "capacity_fulfillment_score": 40, "gross_margin_bridge_score": 45, "revision_score": 50, "relative_strength_score": 65, "valuation_blowoff_risk_score": 60, "execution_risk_score": 70, "source_quality_score": 10, "4B_watch_score": 80}, "weighted_score_after": 73, "stage_label_after": "Stage2-Actionable + high-MAE RiskWatch/local 4B watch", "changed_components": ["sell_through_score", "reorder_visibility_score", "gross_margin_bridge_score", "source_quality_score", "execution_risk_score", "4B_watch_score"], "component_delta_explanation": "C18 requires export-channel sell-through, reorder cadence, capacity fulfillment and gross-margin bridge before clean Stage2/Green; channel-theme MFE alone is demoted or wrapped with local 4B watch.", "MFE_90D_pct": 55.36, "MAE_90D_pct": -28.94, "score_return_alignment_label": "high_MFE_high_MAE_positive_requires_RiskWatch", "current_profile_verdict": "current_profile_4B_too_late_high_MAE"}
{"row_type": "case", "case_id": "R5L84-C18-03", "symbol": "214420", "company_name": "토니모리", "round": "R5", "loop": 84, "large_sector_id": "L5_CONSUMER_BRAND_DISTRIBUTION", "canonical_archetype_id": "C18_CONSUMER_EXPORT_CHANNEL_REORDER", "fine_archetype_id": "K_BEAUTY_ODM_EXPORT_CHANNEL_REORDER_SELL_THROUGH_MARGIN_BRIDGE_VS_CHANNEL_THEME_OVERHEAT_FADE", "case_type": "brand_channel_theme_overheat_false_positive", "positive_or_counterexample": "counterexample", "best_trigger": "R5L84-C18-03-S2FP-20240626", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "theme_overheat_low_MFE_high_MAE_false_positive", "current_profile_verdict": "current_profile_false_positive_high_MAE", "price_source": "Songdaiki/stock-web", "notes": "Brand/channel theme after a large move should be rejected unless sell-through, reorder cadence and margin conversion are visible at entry."}
{"row_type": "trigger", "trigger_id": "R5L84-C18-03-S2FP-20240626", "case_id": "R5L84-C18-03", "symbol": "214420", "company_name": "토니모리", "round": "R5", "loop": 84, "large_sector_id": "L5_CONSUMER_BRAND_DISTRIBUTION", "canonical_archetype_id": "C18_CONSUMER_EXPORT_CHANNEL_REORDER", "fine_archetype_id": "K_BEAUTY_ODM_EXPORT_CHANNEL_REORDER_SELL_THROUGH_MARGIN_BRIDGE_VS_CHANNEL_THEME_OVERHEAT_FADE", "loop_objective": "coverage_gap_fill|counterexample_mining|consumer_export_channel_reorder_guardrail|local_4B_timing_after_channel_MFE|canonical_archetype_compression", "trigger_type": "Stage2-FalsePositive", "trigger_date": "2024-06-26", "evidence_available_at_that_date": "brand/channel recovery and export-channel theme proxy without reorder durability and margin bridge", "evidence_source": "source_proxy_only; evidence_url_pending", "stage2_evidence_fields": ["export_channel_proxy", "sell_through_proxy", "reorder_visibility_proxy"], "stage3_evidence_fields": ["confirmed_channel_reorder", "customer_concentration_control", "capacity_fulfillment", "gross_margin_conversion", "revision_confirmation"], "stage4b_evidence_fields": ["channel_MFE_without_reorder_bridge", "valuation_overheat", "post_peak_drawdown"], "stage4c_evidence_fields": ["hard_customer_reorder_break_watch_only"], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/214/214420/2024.csv", "profile_path": "atlas/symbol_profiles/214/214420.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "entry_date": "2024-06-26", "entry_price": 12860, "MFE_30D_pct": 5.75, "MFE_90D_pct": 5.75, "MFE_180D_pct": 5.75, "MFE_1Y_pct": null, "MFE_2Y_pct": null, "MAE_30D_pct": -41.68, "MAE_90D_pct": -41.68, "MAE_180D_pct": -41.68, "MAE_1Y_pct": null, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2024-06-27", "peak_price": 13600, "drawdown_after_peak_pct": -44.85, "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": 0.3, "four_b_full_window_peak_proximity": 0.25, "four_b_timing_verdict": "channel_theme_overheat_rejected_without_sell_through_reorder_margin_bridge", "four_b_evidence_type": ["channel_MFE_without_reorder_bridge", "post_peak_drawdown", "source_proxy_gap"], "four_c_protection_label": "hard_4C_requires_non_price_reorder_or_customer_break", "trigger_outcome_label": "theme_overheat_low_MFE_high_MAE_false_positive", "current_profile_verdict": "current_profile_false_positive_high_MAE", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window_after_old_2022_CA_candidates", "same_entry_group_id": "R5L84-C18-03", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R5L84-C18-03", "trigger_id": "R5L84-C18-03-S2FP-20240626", "symbol": "214420", "large_sector_id": "L5_CONSUMER_BRAND_DISTRIBUTION", "canonical_archetype_id": "C18_CONSUMER_EXPORT_CHANNEL_REORDER", "raw_component_scores_before": {"export_channel_score": 25, "sell_through_score": 10, "reorder_visibility_score": 5, "customer_quality_score": 20, "capacity_fulfillment_score": 15, "gross_margin_bridge_score": 5, "revision_score": 20, "relative_strength_score": 35, "valuation_blowoff_risk_score": 75, "execution_risk_score": 80, "source_quality_score": 15, "4B_watch_score": 70}, "weighted_score_before": 58, "stage_label_before": "Stage2-Watch/FalsePositive", "raw_component_scores_after": {"export_channel_score": 25, "sell_through_score": 0, "reorder_visibility_score": 0, "customer_quality_score": 20, "capacity_fulfillment_score": 15, "gross_margin_bridge_score": 0, "revision_score": 20, "relative_strength_score": 35, "valuation_blowoff_risk_score": 75, "execution_risk_score": 90, "source_quality_score": 5, "4B_watch_score": 85}, "weighted_score_after": 47, "stage_label_after": "Rejected-Stage2 / RiskWatch", "changed_components": ["sell_through_score", "reorder_visibility_score", "gross_margin_bridge_score", "source_quality_score", "execution_risk_score", "4B_watch_score"], "component_delta_explanation": "C18 requires export-channel sell-through, reorder cadence, capacity fulfillment and gross-margin bridge before clean Stage2/Green; channel-theme MFE alone is demoted or wrapped with local 4B watch.", "MFE_90D_pct": 5.75, "MAE_90D_pct": -41.68, "score_return_alignment_label": "theme_overheat_low_MFE_high_MAE_false_positive", "current_profile_verdict": "current_profile_false_positive_high_MAE"}
{"row_type": "shadow_weight", "axis": "C18_export_channel_sellthrough_reorder_margin_bridge_required", "scope": "canonical_archetype_specific", "large_sector_id": "L5_CONSUMER_BRAND_DISTRIBUTION", "canonical_archetype_id": "C18_CONSUMER_EXPORT_CHANNEL_REORDER", "baseline_value": 0, "tested_value": 1, "delta": "+1", "reason": "Consumer export-channel rerating requires sell-through, reorder cadence, capacity fulfillment and margin bridge; channel-theme MFE without bridge fades into high MAE or needs local 4B watch.", "backtest_effect": "keeps 241710/950140 with local 4B or high-MAE RiskWatch; demotes 214420 channel-theme false positive", "trigger_ids": "R5L84-C18-01-S2A-20240401|R5L84-C18-02-S2A-20240221|R5L84-C18-03-S2FP-20240626", "calibration_usable_count": 3, "new_independent_case_count": 3, "counterexample_count": 1, "confidence": "low", "proposal_type": "canonical_shadow_only", "notes": "source_proxy_only/evidence_url_pending; not production"}
{"row_type": "residual_contribution", "round": "R5", "loop": 84, "large_sector_id": "L5_CONSUMER_BRAND_DISTRIBUTION", "canonical_archetype_id": "C18_CONSUMER_EXPORT_CHANNEL_REORDER", "new_independent_case_count": 3, "reused_case_count": 0, "new_symbol_count": 3, "new_trigger_family_count": 3, "tested_existing_calibrated_axes": ["stage2_actionable_evidence_bonus", "price_only_blowoff_blocks_positive_stage", "full_4b_requires_non_price_evidence", "hard_4c_thesis_break_routes_to_4c", "source_proxy_only_blocks_runtime_promotion", "high_MAE_guardrail"], "residual_error_types_found": ["consumer_channel_theme_false_positive_high_MAE", "export_sellthrough_reorder_margin_bridge_required", "local_4B_late_after_channel_MFE", "source_proxy_runtime_promotion_risk", "high_MAE_positive_Green_blocker"], "loop_contribution_label": "canonical_archetype_rule_candidate", "do_not_propose_new_weight_delta": true}
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
- Do not treat source_proxy_only or evidence_url_pending rows as runtime promotion-ready.
- Keep production scoring unchanged unless a later batch validates primary evidence and aggregate thresholds.
- For C18, test a canonical-archetype guard requiring export-channel sell-through, reorder cadence, capacity fulfillment and gross-margin bridge before clean Stage2/Green.

## 27. Next Round State

```text
completed_round = R5
completed_loop = 84
next_round = R6
next_loop = 84
round_schedule_status = valid
round_sector_consistency = pass
```

## 28. Source Notes

```text
MAIN_EXECUTION_PROMPT = docs/core/e2r_v12_prompt_round_scheduler_corrected.txt
NO_REPEAT_INDEX = docs/core/V12_Research_No_Repeat_Index.md
price_source = Songdaiki/stock-web
```
