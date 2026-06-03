# E2R Stock-Web v12 Residual Research — R9 Loop 86 / L3 / C29

## 0. Research Metadata

```json
{
  "research_session": "post_calibrated_sector_archetype_residual_research",
  "mode": "historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12",
  "scheduled_round": "R9",
  "scheduled_loop": 86,
  "round_schedule_status": "valid",
  "round_sector_consistency": "pass",
  "completed_round": "R9",
  "completed_loop": 86,
  "computed_next_round": "R10",
  "computed_next_loop": 86,
  "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY",
  "canonical_archetype_id": "C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE",
  "fine_archetype_id": "HYBRID_CANISTER_SEAT_INTERIOR_AUTO_PARTS_VOLUME_PLATFORM_MIX_MARGIN_BRIDGE_VS_AUTO_PARTS_THEME_FADE",
  "loop_objective": [
    "coverage_gap_fill",
    "counterexample_mining",
    "mobility_volume_margin_operating_leverage_guardrail",
    "hybrid_canister_seat_interior_parts_platform_mix_margin_bridge_test",
    "auto_parts_volume_theme_vs_cost_pass_through_margin_conversion_test",
    "local_4B_timing_after_mobility_parts_MFE",
    "hard_4C_non_price_volume_platform_or_margin_break_protection",
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
scheduled_round = R9
scheduled_loop = 86
allowed_large_sector = L3_BATTERY_EV_GREEN_MOBILITY or L9_CONSTRUCTION_REALESTATE_HOUSING depending on mobility/transport vs construction/PF nature
selected_large_sector = L3_BATTERY_EV_GREEN_MOBILITY
selected_canonical_archetype_id = C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE
computed_next_round = R10
computed_next_loop = 86
round_schedule_status = valid
round_sector_consistency = pass
```

R9 is routed to C29 because this run tests mobility / auto-parts operating leverage rather than construction/PF stress. Loop85 R9 already tested auto-lighting / ADAS / chassis parts, so loop86 shifts to a hybrid-canister / seat / interior parts route.

The tested mechanism:

```text
hybrid / seat / interior / auto-parts volume headline
→ OEM platform or order mix
→ customer orderbook and utilization
→ ASP or raw-material cost spread
→ gross / OP margin conversion
→ durable rerating or auto-parts theme fade
```

C29 is the assembly-line margin test. Unit volume matters, but the rerating is built when platform mix, utilization, cost spread and margin move together.

## 3. Previous Coverage / Duplicate Avoidance Check

No-Repeat is used only as a duplicate ledger.

```text
hard_duplicate_key = canonical_archetype_id + symbol + trigger_type + entry_date
```

C29 top-covered symbols include `UNKNOWN_SYMBOL`, `000270`, `161390`, `012330`, `005380`, and `018880`. This run avoids that top-covered set and also avoids loop85 R9 symbols:

```text
previous_loop85_R9_symbols = 005850 / 204320 / 010690
selected_loop86_symbols = 123410 / 005710 / 024900
```

All three are treated as new independent C29 mobility volume / margin-operating-leverage cases for this loop. No hard duplicate is intentionally reused.

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
| 123410 | 코리아에프티 | `atlas/symbol_profiles/123/123410.json` | old 2012 SPAC CA candidate; selected 2024 forward window clean |
| 005710 | 대원산업 | `atlas/symbol_profiles/005/005710.json` | old CA candidates through 2011; selected 2024 forward window clean |
| 024900 | 덕양산업 | `atlas/symbol_profiles/024/024900.json` | old CA candidates through 2014; selected 2024 forward window clean |

## 5. Historical Eligibility Gate

| case_id | symbol | entry_date | entry_price | forward window | 180D status | calibration_usable |
|---|---:|---|---:|---:|---|---|
| R9L86-C29-01 | 123410 | 2024-02-13 | 4,955 | 180D | clean | true |
| R9L86-C29-02 | 005710 | 2024-01-26 | 5,650 | 180D | clean | true |
| R9L86-C29-03 | 024900 | 2024-02-02 | 5,240 | 180D | clean | true |

## 6. Canonical Archetype Compression Map

| canonical_archetype_id | fine/deep route | keep / reject logic |
|---|---|---|
| C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE | HYBRID_CANISTER_PLATFORM_MIX_POSITIVE | keep Stage2 with platform/order mix, OEM volume, utilization and margin bridge; add local 4B after MFE |
| C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE | SEAT_INTERIOR_CONTROLLED_MAE_POSITIVE | keep Stage2 only with platform volume and margin bridge watch |
| C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE | AUTO_INTERIOR_THEME_HIGH_MAE_FADE | reject auto-interior theme MFE without platform mix, orderbook, cost pass-through and margin conversion |

## 7. Case Selection Summary

| case_id | symbol | company | trigger_type | entry_date | entry_price | MFE_180D_pct | MAE_180D_pct | current_profile_verdict |
|---|---:|---|---|---|---:|---:|---:|---|
| R9L86-C29-01 | 123410 | 코리아에프티 | Stage2-Actionable | 2024-02-13 | 4,955 | 48.74 | -17.86 | current_profile_partially_correct_local_4B_watch_needed |
| R9L86-C29-02 | 005710 | 대원산업 | Stage2-Actionable | 2024-01-26 | 5,650 | 19.82 | -1.59 | current_profile_partially_correct_but_bridge_required |
| R9L86-C29-03 | 024900 | 덕양산업 | Stage2-FalsePositive | 2024-02-02 | 5,240 | 17.37 | -42.94 | current_profile_false_positive_high_MAE |

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

This MD creates a source-repair queue and a C29 auto-parts shadow guardrail candidate. It must not be promoted directly into runtime weights until a later source-repair pass attaches primary evidence URLs: OEM platform mix, orderbook, shipment volume, utilization, ASP/cost pass-through, raw-material spread, gross/OP margin bridge, company disclosure or report evidence.

## 10. Price Data Source Map

| symbol | shard path | profile path |
|---|---|---|
| 123410 | `atlas/ohlcv_tradable_by_symbol_year/123/123410/2024.csv` | `atlas/symbol_profiles/123/123410.json` |
| 005710 | `atlas/ohlcv_tradable_by_symbol_year/005/005710/2024.csv` | `atlas/symbol_profiles/005/005710.json` |
| 024900 | `atlas/ohlcv_tradable_by_symbol_year/024/024900/2024.csv` | `atlas/symbol_profiles/024/024900.json` |

## 11. Case-by-Case Trigger Grid

### Case 1 — 123410 / 코리아에프티

C29 hybrid-canister / mobility-parts positive with local 4B watch. The February entry produced a large MFE and later a second push into August. However, the path also contained an August low, so clean Green requires platform mix, orderbook and margin evidence.

### Case 2 — 005710 / 대원산업

C29 seat/interior parts positive with controlled MAE. The January entry produced moderate MFE with comparatively controlled drawdown. This is useful because even controlled-MAE positives still need source-repaired platform-volume and margin bridge before Green.

### Case 3 — 024900 / 덕양산업

C29 auto-interior theme false positive. The early MFE quickly faded and later MAE became large. This rejects auto-interior/EV-parts theme language without platform mix, orderbook and cost-pass-through evidence.

## 12. Trigger-Level OHLC Backtest Tables

| symbol | entry | MFE30 | MAE30 | MFE90 | MAE90 | MFE180 | MAE180 | peak | post-peak DD |
|---|---:|---:|---:|---:|---:|---:|---:|---|---:|
| 123410 | 4,955 | 30.78 | -2.52 | 46.52 | -2.52 | 48.74 | -17.86 | 2024-08-29 / 7,370 | -22.12 |
| 005710 | 5,650 | 19.82 | -1.59 | 19.82 | -1.59 | 19.82 | -1.59 | 2024-02-02 / 6,770 | -17.73 |
| 024900 | 5,240 | 17.37 | -14.22 | 17.37 | -20.42 | 17.37 | -42.94 | 2024-02-05 / 6,150 | -51.38 |

## 13. Current Calibrated Profile Stress Test

| case_id | P0 likely behavior | actual path | verdict |
|---|---|---|---|
| R9L86-C29-01 | Stage2-Actionable if platform/order mix bridge exists | large MFE, later MAE | partially correct; local 4B/platform-margin watch needed |
| R9L86-C29-02 | Stage2-Actionable if platform-volume bridge exists | moderate MFE, controlled MAE | partially correct; bridge still required |
| R9L86-C29-03 | risk of treating auto-interior theme as Stage2 | MFE then deep MAE | false positive / high-MAE guardrail |

## 14. Stage2 / Yellow / Green Comparison

```text
green_lateness_ratio = not_applicable
reason = no confirmed Stage3-Green trigger is assigned in this residual MD
```

For C29, the residual is whether auto-parts MFE becomes clean Stage2/Green before platform/order mix, utilization, cost spread and margin bridge are proven.

## 15. 4B Local vs Full-window Timing Audit

| case_id | local proximity | full-window proximity | verdict |
|---|---:|---:|---|
| R9L86-C29-01 | 0.78 | 0.68 | local 4B watch after hybrid parts MFE if platform mix/cost spread margin bridge stalls |
| R9L86-C29-02 | 0.78 | 0.68 | seat/interior parts MFE allowed only with platform-volume margin bridge watch |
| R9L86-C29-03 | 0.35 | 0.30 | auto-interior theme rejected without platform mix/orderbook/cost-spread margin bridge |

## 16. 4C Protection Audit

No hard 4C is promoted from this file.

```text
four_c_protection_label = hard_4C_requires_non_price_volume_platform_or_margin_break
hard_4c_price_only_allowed = false
```

Price drawdown alone is not hard 4C. C29 hard 4C requires confirmed volume collapse, OEM platform loss, orderbook deterioration, utilization break, cost-spread compression or margin thesis break.

## 17. Sector-Specific Rule Candidate

```text
rule_scope = no_new_global_rule
sector_specific_rule_candidate = L3/C29 auto-parts rows need platform/order mix, OEM volume, utilization, ASP/raw-material spread and margin conversion before clean Stage2/Green
confidence = low
reason = all evidence rows are source_proxy_only / evidence_url_pending
```

## 18. Canonical-Archetype Rule Candidate

```text
canonical_archetype_id = C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE
candidate_axis = C29_mobility_parts_platform_mix_volume_cost_spread_margin_bridge_required
effect = keep hybrid/seat-interior positives with local 4B/platform-margin watch; demote auto-interior theme false positives
production_scoring_changed = false
shadow_weight_only = true
do_not_propose_new_weight_delta = true
```

## 19. Before / After Backtest Comparison

| profile | eligible triggers | avg MFE90 | avg MAE90 | false-positive behavior | verdict |
|---|---:|---:|---:|---|---|
| P0 e2r_2_1_stock_web_calibrated_proxy | 3 | 27.90 | -8.18 | may over-credit auto-parts theme MFE without margin bridge | needs C29 platform/margin bridge repair |
| P1 canonical shadow bridge profile | 3 | 33.17 on kept positives | -2.06 on kept positives | demotes 024900 | better alignment, source repair required |

## 20. Score-Return Alignment Matrix

| case_id | weighted before | label before | weighted after | label after | alignment |
|---|---:|---|---:|---|---|
| R9L86-C29-01 | 76 | Stage2-Actionable | 73 | Stage2-Actionable + local 4B/platform-margin watch | partially aligned |
| R9L86-C29-02 | 76 | Stage2-Actionable | 73 | Stage2-Actionable + local 4B/platform-margin watch | partially aligned |
| R9L86-C29-03 | 58 | Stage2-Watch/FalsePositive | 44 | Rejected-Stage2 / Auto-parts theme RiskWatch | improved |

## 21. Coverage Matrix

| large_sector_id | canonical_archetype_id | fine_archetype_id | positive | counterexample | 4B | 4C | new cases | reused | usable triggers | current errors | sector rule | canonical rule | coverage gap after |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---|---|---|
| L3_BATTERY_EV_GREEN_MOBILITY | C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE | HYBRID_CANISTER_SEAT_INTERIOR_AUTO_PARTS_VOLUME_PLATFORM_MIX_MARGIN_BRIDGE_VS_AUTO_PARTS_THEME_FADE | 2 | 1 | 3-watch | 0-hard | 3 | 0 | 3 | 1 | no | yes | source repair needed |

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
  - local_4B_watch_before_full_4B_when_MFE_outruns_bridge
residual_error_types_found:
  - auto_parts_theme_false_positive_high_MAE
  - platform_mix_cost_spread_margin_bridge_required
  - controlled_MAE_but_bridge_still_required
  - local_4B_late_after_mobility_parts_MFE
  - source_proxy_runtime_promotion_risk
new_axis_proposed: false
existing_axis_strengthened:
  - C29_mobility_parts_platform_mix_volume_cost_spread_margin_bridge_required
  - source_proxy_only_blocks_runtime_promotion
  - local_4B_watch_before_full_4B_when_MFE_outruns_bridge
  - high_MAE_blocks_clean_Green
existing_axis_weakened: null
existing_axis_kept:
  - full_4b_requires_non_price_evidence
  - hard_4c_thesis_break_routes_to_4c
sector_specific_rule_candidate: null
canonical_archetype_rule_candidate: C29_mobility_parts_platform_mix_volume_cost_spread_margin_bridge_required
no_new_signal_reason: null
loop_contribution_label: canonical_archetype_rule_candidate
do_not_propose_new_weight_delta: true
```

This loop adds 3 new independent cases, 1 counterexample, and 1 residual error for R9/L3_BATTERY_EV_GREEN_MOBILITY/C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE.

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
- OEM platform/order mix source
- shipment or customer orderbook data
- utilization / ASP / raw-material cost spread
- gross/OP margin conversion
- production scoring implementation
```

## 24. Shadow Weight Calibration

```csv
row_type,axis,scope,large_sector_id,canonical_archetype_id,baseline_value,tested_value,delta,reason,backtest_effect,trigger_ids,calibration_usable_count,new_independent_case_count,counterexample_count,confidence,proposal_type,notes
shadow_weight,C29_mobility_parts_platform_mix_volume_cost_spread_margin_bridge_required,canonical_archetype_specific,L3_BATTERY_EV_GREEN_MOBILITY,C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE,0,1,+1,"Require platform/order mix, OEM volume, utilization, ASP/raw-material spread and gross/OP margin conversion before clean Stage2/Green","keeps 123410/005710 with local 4B or platform-margin watch; demotes 024900","R9L86-C29-01-S2A-20240213|R9L86-C29-02-S2A-20240126|R9L86-C29-03-S2FP-20240202",3,3,1,low,canonical_shadow_only,"source repair required; not production"
```

## 25. Machine-Readable Rows

```jsonl
{"row_type": "price_source_validation", "source": "Songdaiki/stock-web", "source_url": "https://github.com/Songdaiki/stock-web", "manifest_path": "atlas/manifest.json", "schema_path": "atlas/schema.json", "universe_path": "atlas/universe/all_symbols.csv", "manifest_max_date": "2026-02-20", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "raw_shard_root": "atlas/ohlcv_raw_by_symbol_year", "validation_status": "usable_for_historical_calibration"}
{"row_type": "case", "case_id": "R9L86-C29-01", "symbol": "123410", "company_name": "코리아에프티", "round": "R9", "loop": 86, "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE", "fine_archetype_id": "HYBRID_CANISTER_SEAT_INTERIOR_AUTO_PARTS_VOLUME_PLATFORM_MIX_MARGIN_BRIDGE_VS_AUTO_PARTS_THEME_FADE", "case_type": "hybrid_canister_mobility_parts_platform_mix_positive_with_local_4B_watch", "positive_or_counterexample": "positive", "best_trigger": "R9L86-C29-01-S2A-20240213", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "large_auto_parts_MFE_but_platform_mix_cost_spread_margin_bridge_required", "current_profile_verdict": "current_profile_partially_correct_local_4B_watch_needed", "price_source": "Songdaiki/stock-web", "notes": "C29 hybrid/auto-parts positives need OEM volume, platform/order mix, utilization, ASP/cost spread and gross/OP margin bridge before clean Green."}
{"row_type": "trigger", "trigger_id": "R9L86-C29-01-S2A-20240213", "case_id": "R9L86-C29-01", "symbol": "123410", "company_name": "코리아에프티", "round": "R9", "loop": 86, "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE", "fine_archetype_id": "HYBRID_CANISTER_SEAT_INTERIOR_AUTO_PARTS_VOLUME_PLATFORM_MIX_MARGIN_BRIDGE_VS_AUTO_PARTS_THEME_FADE", "loop_objective": "coverage_gap_fill|counterexample_mining|mobility_volume_margin_operating_leverage_guardrail|platform_mix_cost_spread_margin_bridge|canonical_archetype_compression", "trigger_type": "Stage2-Actionable", "trigger_date": "2024-02-13", "evidence_available_at_that_date": "hybrid canister / global auto platform mix / mobility volume and margin recovery proxy; primary order mix and margin evidence pending", "evidence_source": "source_proxy_only; evidence_url_pending", "stage2_evidence_fields": ["auto_parts_volume_proxy", "platform_or_order_mix_proxy", "cost_spread_or_margin_proxy"], "stage3_evidence_fields": ["confirmed_platform_mix", "customer_orderbook_or_OEM_volume", "utilization", "ASP_or_raw_material_cost_spread", "gross_or_OP_margin_conversion"], "stage4b_evidence_fields": ["mobility_parts_MFE_without_margin_bridge", "theme_spike_drawdown", "source_proxy_gap"], "stage4c_evidence_fields": ["hard_volume_platform_or_margin_break_watch_only"], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/123/123410/2024.csv", "profile_path": "atlas/symbol_profiles/123/123410.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "entry_date": "2024-02-13", "entry_price": 4955, "MFE_30D_pct": 30.78, "MFE_90D_pct": 46.52, "MFE_180D_pct": 48.74, "MFE_1Y_pct": null, "MFE_2Y_pct": null, "MAE_30D_pct": -2.52, "MAE_90D_pct": -2.52, "MAE_180D_pct": -17.86, "MAE_1Y_pct": null, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2024-08-29", "peak_price": 7370, "drawdown_after_peak_pct": -22.12, "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": 0.78, "four_b_full_window_peak_proximity": 0.68, "four_b_timing_verdict": "local_4B_watch_after_hybrid_parts_MFE_if_platform_mix_cost_spread_margin_bridge_stalls", "four_b_evidence_type": ["auto_parts_MFE_without_platform_margin_bridge", "post_peak_drawdown", "source_proxy_gap"], "four_c_protection_label": "hard_4C_requires_non_price_volume_platform_or_margin_break", "trigger_outcome_label": "large_auto_parts_MFE_but_platform_mix_cost_spread_margin_bridge_required", "current_profile_verdict": "current_profile_partially_correct_local_4B_watch_needed", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_2024_window_after_old_2012_SPAC_CA_candidate", "same_entry_group_id": "R9L86-C29-01", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R9L86-C29-01", "trigger_id": "R9L86-C29-01-S2A-20240213", "symbol": "123410", "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE", "raw_component_scores_before": {"volume_or_shipment_score": 45, "platform_or_order_mix_score": 45, "customer_quality_score": 40, "utilization_score": 40, "ASP_or_cost_spread_score": 35, "gross_margin_bridge_score": 35, "OP_leverage_score": 35, "revision_score": 35, "relative_strength_score": 65, "valuation_blowoff_risk_score": 70, "execution_risk_score": 55, "source_quality_score": 20, "4B_watch_score": 45}, "weighted_score_before": 76, "stage_label_before": "Stage2-Actionable", "raw_component_scores_after": {"volume_or_shipment_score": 45, "platform_or_order_mix_score": 45, "customer_quality_score": 40, "utilization_score": 40, "ASP_or_cost_spread_score": 35, "gross_margin_bridge_score": 35, "OP_leverage_score": 35, "revision_score": 35, "relative_strength_score": 65, "valuation_blowoff_risk_score": 80, "execution_risk_score": 65, "source_quality_score": 10, "4B_watch_score": 80}, "weighted_score_after": 73, "stage_label_after": "Stage2-Actionable + local 4B/platform-margin watch", "changed_components": ["platform_or_order_mix_score", "utilization_score", "ASP_or_cost_spread_score", "gross_margin_bridge_score", "OP_leverage_score", "source_quality_score", "4B_watch_score"], "component_delta_explanation": "C29 requires mobility/auto-parts MFE to convert into platform/order mix, OEM volume, utilization, ASP/raw-material cost spread and margin conversion before clean Stage2/Green; auto-parts theme MFE alone is demoted or wrapped with local 4B/high-MAE watch.", "MFE_90D_pct": 46.52, "MAE_90D_pct": -2.52, "score_return_alignment_label": "large_auto_parts_MFE_but_platform_mix_cost_spread_margin_bridge_required", "current_profile_verdict": "current_profile_partially_correct_local_4B_watch_needed"}
{"row_type": "case", "case_id": "R9L86-C29-02", "symbol": "005710", "company_name": "대원산업", "round": "R9", "loop": 86, "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE", "fine_archetype_id": "HYBRID_CANISTER_SEAT_INTERIOR_AUTO_PARTS_VOLUME_PLATFORM_MIX_MARGIN_BRIDGE_VS_AUTO_PARTS_THEME_FADE", "case_type": "seat_interior_parts_volume_margin_positive_with_controlled_MAE_watch", "positive_or_counterexample": "positive", "best_trigger": "R9L86-C29-02-S2A-20240126", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "controlled_MAE_positive_MFE_but_margin_bridge_required", "current_profile_verdict": "current_profile_partially_correct_but_bridge_required", "price_source": "Songdaiki/stock-web", "notes": "Seat/interior parts positives need platform mix, capacity utilization, ASP/cost spread and OP-margin conversion before clean Green."}
{"row_type": "trigger", "trigger_id": "R9L86-C29-02-S2A-20240126", "case_id": "R9L86-C29-02", "symbol": "005710", "company_name": "대원산업", "round": "R9", "loop": 86, "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE", "fine_archetype_id": "HYBRID_CANISTER_SEAT_INTERIOR_AUTO_PARTS_VOLUME_PLATFORM_MIX_MARGIN_BRIDGE_VS_AUTO_PARTS_THEME_FADE", "loop_objective": "coverage_gap_fill|counterexample_mining|mobility_volume_margin_operating_leverage_guardrail|platform_mix_cost_spread_margin_bridge|canonical_archetype_compression", "trigger_type": "Stage2-Actionable", "trigger_date": "2024-01-26", "evidence_available_at_that_date": "seat/interior auto parts, OEM volume and controlled-margin recovery proxy; primary platform mix and utilization evidence pending", "evidence_source": "source_proxy_only; evidence_url_pending", "stage2_evidence_fields": ["auto_parts_volume_proxy", "platform_or_order_mix_proxy", "cost_spread_or_margin_proxy"], "stage3_evidence_fields": ["confirmed_platform_mix", "customer_orderbook_or_OEM_volume", "utilization", "ASP_or_raw_material_cost_spread", "gross_or_OP_margin_conversion"], "stage4b_evidence_fields": ["mobility_parts_MFE_without_margin_bridge", "theme_spike_drawdown", "source_proxy_gap"], "stage4c_evidence_fields": ["hard_volume_platform_or_margin_break_watch_only"], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/005/005710/2024.csv", "profile_path": "atlas/symbol_profiles/005/005710.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "entry_date": "2024-01-26", "entry_price": 5650, "MFE_30D_pct": 19.82, "MFE_90D_pct": 19.82, "MFE_180D_pct": 19.82, "MFE_1Y_pct": null, "MFE_2Y_pct": null, "MAE_30D_pct": -1.59, "MAE_90D_pct": -1.59, "MAE_180D_pct": -1.59, "MAE_1Y_pct": null, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2024-02-02", "peak_price": 6770, "drawdown_after_peak_pct": -17.73, "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": 0.78, "four_b_full_window_peak_proximity": 0.68, "four_b_timing_verdict": "seat_interior_parts_MFE_allowed_only_with_platform_volume_margin_bridge_watch", "four_b_evidence_type": ["auto_parts_MFE_without_platform_margin_bridge", "post_peak_drawdown", "source_proxy_gap"], "four_c_protection_label": "hard_4C_requires_non_price_volume_platform_or_margin_break", "trigger_outcome_label": "controlled_MAE_positive_MFE_but_margin_bridge_required", "current_profile_verdict": "current_profile_partially_correct_but_bridge_required", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_2024_window_after_old_2011_CA_candidate", "same_entry_group_id": "R9L86-C29-02", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R9L86-C29-02", "trigger_id": "R9L86-C29-02-S2A-20240126", "symbol": "005710", "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE", "raw_component_scores_before": {"volume_or_shipment_score": 45, "platform_or_order_mix_score": 45, "customer_quality_score": 40, "utilization_score": 40, "ASP_or_cost_spread_score": 35, "gross_margin_bridge_score": 35, "OP_leverage_score": 35, "revision_score": 35, "relative_strength_score": 50, "valuation_blowoff_risk_score": 45, "execution_risk_score": 45, "source_quality_score": 20, "4B_watch_score": 45}, "weighted_score_before": 76, "stage_label_before": "Stage2-Actionable", "raw_component_scores_after": {"volume_or_shipment_score": 45, "platform_or_order_mix_score": 45, "customer_quality_score": 40, "utilization_score": 40, "ASP_or_cost_spread_score": 35, "gross_margin_bridge_score": 35, "OP_leverage_score": 35, "revision_score": 35, "relative_strength_score": 50, "valuation_blowoff_risk_score": 45, "execution_risk_score": 45, "source_quality_score": 10, "4B_watch_score": 80}, "weighted_score_after": 73, "stage_label_after": "Stage2-Actionable + local 4B/platform-margin watch", "changed_components": ["platform_or_order_mix_score", "utilization_score", "ASP_or_cost_spread_score", "gross_margin_bridge_score", "OP_leverage_score", "source_quality_score", "4B_watch_score"], "component_delta_explanation": "C29 requires mobility/auto-parts MFE to convert into platform/order mix, OEM volume, utilization, ASP/raw-material cost spread and margin conversion before clean Stage2/Green; auto-parts theme MFE alone is demoted or wrapped with local 4B/high-MAE watch.", "MFE_90D_pct": 19.82, "MAE_90D_pct": -1.59, "score_return_alignment_label": "controlled_MAE_positive_MFE_but_margin_bridge_required", "current_profile_verdict": "current_profile_partially_correct_but_bridge_required"}
{"row_type": "case", "case_id": "R9L86-C29-03", "symbol": "024900", "company_name": "덕양산업", "round": "R9", "loop": 86, "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE", "fine_archetype_id": "HYBRID_CANISTER_SEAT_INTERIOR_AUTO_PARTS_VOLUME_PLATFORM_MIX_MARGIN_BRIDGE_VS_AUTO_PARTS_THEME_FADE", "case_type": "auto_interior_parts_theme_high_MAE_false_positive", "positive_or_counterexample": "counterexample", "best_trigger": "R9L86-C29-03-S2FP-20240202", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "theme_MFE_then_deep_MAE_auto_interior_false_positive", "current_profile_verdict": "current_profile_false_positive_high_MAE", "price_source": "Songdaiki/stock-web", "notes": "Auto interior/parts theme MFE should be rejected unless platform mix, orderbook quality, cost pass-through and margin conversion are explicit."}
{"row_type": "trigger", "trigger_id": "R9L86-C29-03-S2FP-20240202", "case_id": "R9L86-C29-03", "symbol": "024900", "company_name": "덕양산업", "round": "R9", "loop": 86, "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE", "fine_archetype_id": "HYBRID_CANISTER_SEAT_INTERIOR_AUTO_PARTS_VOLUME_PLATFORM_MIX_MARGIN_BRIDGE_VS_AUTO_PARTS_THEME_FADE", "loop_objective": "coverage_gap_fill|counterexample_mining|mobility_volume_margin_operating_leverage_guardrail|platform_mix_cost_spread_margin_bridge|canonical_archetype_compression", "trigger_type": "Stage2-FalsePositive", "trigger_date": "2024-02-02", "evidence_available_at_that_date": "auto interior / EV parts / mobility volume recovery theme proxy without confirmed platform mix, orderbook, cost pass-through or margin bridge", "evidence_source": "source_proxy_only; evidence_url_pending", "stage2_evidence_fields": ["auto_parts_volume_proxy", "platform_or_order_mix_proxy", "cost_spread_or_margin_proxy"], "stage3_evidence_fields": ["confirmed_platform_mix", "customer_orderbook_or_OEM_volume", "utilization", "ASP_or_raw_material_cost_spread", "gross_or_OP_margin_conversion"], "stage4b_evidence_fields": ["mobility_parts_MFE_without_margin_bridge", "theme_spike_drawdown", "source_proxy_gap"], "stage4c_evidence_fields": ["hard_volume_platform_or_margin_break_watch_only"], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/024/024900/2024.csv", "profile_path": "atlas/symbol_profiles/024/024900.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "entry_date": "2024-02-02", "entry_price": 5240, "MFE_30D_pct": 17.37, "MFE_90D_pct": 17.37, "MFE_180D_pct": 17.37, "MFE_1Y_pct": null, "MFE_2Y_pct": null, "MAE_30D_pct": -14.22, "MAE_90D_pct": -20.42, "MAE_180D_pct": -42.94, "MAE_1Y_pct": null, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2024-02-05", "peak_price": 6150, "drawdown_after_peak_pct": -51.38, "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": 0.35, "four_b_full_window_peak_proximity": 0.3, "four_b_timing_verdict": "auto_interior_theme_rejected_without_platform_mix_orderbook_cost_spread_margin_bridge", "four_b_evidence_type": ["auto_parts_MFE_without_platform_margin_bridge", "post_peak_drawdown", "source_proxy_gap"], "four_c_protection_label": "hard_4C_requires_non_price_volume_platform_or_margin_break", "trigger_outcome_label": "theme_MFE_then_deep_MAE_auto_interior_false_positive", "current_profile_verdict": "current_profile_false_positive_high_MAE", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_2024_window_after_old_2014_CA_candidate", "same_entry_group_id": "R9L86-C29-03", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R9L86-C29-03", "trigger_id": "R9L86-C29-03-S2FP-20240202", "symbol": "024900", "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE", "raw_component_scores_before": {"volume_or_shipment_score": 25, "platform_or_order_mix_score": 10, "customer_quality_score": 20, "utilization_score": 10, "ASP_or_cost_spread_score": 5, "gross_margin_bridge_score": 5, "OP_leverage_score": 5, "revision_score": 15, "relative_strength_score": 45, "valuation_blowoff_risk_score": 70, "execution_risk_score": 80, "source_quality_score": 15, "4B_watch_score": 75}, "weighted_score_before": 58, "stage_label_before": "Stage2-Watch/FalsePositive", "raw_component_scores_after": {"volume_or_shipment_score": 25, "platform_or_order_mix_score": 0, "customer_quality_score": 20, "utilization_score": 0, "ASP_or_cost_spread_score": 0, "gross_margin_bridge_score": 0, "OP_leverage_score": 0, "revision_score": 15, "relative_strength_score": 45, "valuation_blowoff_risk_score": 70, "execution_risk_score": 90, "source_quality_score": 5, "4B_watch_score": 90}, "weighted_score_after": 44, "stage_label_after": "Rejected-Stage2 / Auto-parts theme RiskWatch", "changed_components": ["platform_or_order_mix_score", "utilization_score", "ASP_or_cost_spread_score", "gross_margin_bridge_score", "OP_leverage_score", "source_quality_score", "4B_watch_score"], "component_delta_explanation": "C29 requires mobility/auto-parts MFE to convert into platform/order mix, OEM volume, utilization, ASP/raw-material cost spread and margin conversion before clean Stage2/Green; auto-parts theme MFE alone is demoted or wrapped with local 4B/high-MAE watch.", "MFE_90D_pct": 17.37, "MAE_90D_pct": -20.42, "score_return_alignment_label": "theme_MFE_then_deep_MAE_auto_interior_false_positive", "current_profile_verdict": "current_profile_false_positive_high_MAE"}
{"row_type": "shadow_weight", "axis": "C29_mobility_parts_platform_mix_volume_cost_spread_margin_bridge_required", "scope": "canonical_archetype_specific", "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE", "baseline_value": 0, "tested_value": 1, "delta": "+1", "reason": "Mobility/auto-parts rerating requires platform or order mix, OEM volume, utilization, ASP/raw-material cost spread and gross/OP margin conversion; auto-parts theme MFE without bridge fades into high MAE or remains only watchable.", "backtest_effect": "keeps 123410/005710 with local 4B or platform-margin watch; demotes 024900 auto-interior theme false positive", "trigger_ids": "R9L86-C29-01-S2A-20240213|R9L86-C29-02-S2A-20240126|R9L86-C29-03-S2FP-20240202", "calibration_usable_count": 3, "new_independent_case_count": 3, "counterexample_count": 1, "confidence": "low", "proposal_type": "canonical_shadow_only", "notes": "source_proxy_only/evidence_url_pending; not production"}
{"row_type": "residual_contribution", "round": "R9", "loop": 86, "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE", "new_independent_case_count": 3, "reused_case_count": 0, "new_symbol_count": 3, "new_trigger_family_count": 3, "tested_existing_calibrated_axes": ["stage2_actionable_evidence_bonus", "price_only_blowoff_blocks_positive_stage", "full_4b_requires_non_price_evidence", "hard_4c_thesis_break_routes_to_4c", "source_proxy_only_blocks_runtime_promotion", "high_MAE_guardrail", "local_4B_watch_before_full_4B_when_MFE_outruns_bridge"], "residual_error_types_found": ["auto_parts_theme_false_positive_high_MAE", "platform_mix_cost_spread_margin_bridge_required", "controlled_MAE_but_bridge_still_required", "local_4B_late_after_mobility_parts_MFE", "source_proxy_runtime_promotion_risk"], "loop_contribution_label": "canonical_archetype_rule_candidate", "do_not_propose_new_weight_delta": true}
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
- For C29, test a canonical-archetype guard requiring platform/order mix, OEM volume, utilization, ASP/raw-material spread and gross/OP margin conversion before clean Stage2/Green. Keep hard 4C blocked unless a non-price volume/platform/margin thesis break is confirmed.

## 27. Next Round State

```text
completed_round = R9
completed_loop = 86
next_round = R10
next_loop = 86
round_schedule_status = valid
round_sector_consistency = pass
```

## 28. Source Notes

```text
MAIN_EXECUTION_PROMPT = docs/core/e2r_v12_prompt_round_scheduler_corrected.txt
NO_REPEAT_INDEX = docs/core/V12_Research_No_Repeat_Index.md
price_source = Songdaiki/stock-web
```
