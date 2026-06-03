# E2R Stock-Web v12 Residual Research — R9 Loop 85 / L3 / C29

## 0. Research Metadata

```json
{
  "research_session": "post_calibrated_sector_archetype_residual_research",
  "mode": "historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12",
  "scheduled_round": "R9",
  "scheduled_loop": 85,
  "round_schedule_status": "valid",
  "round_sector_consistency": "pass",
  "completed_round": "R9",
  "completed_loop": 85,
  "computed_next_round": "R10",
  "computed_next_loop": 85,
  "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY",
  "canonical_archetype_id": "C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE",
  "fine_archetype_id": "AUTO_LIGHTING_ADAS_CHASSIS_PARTS_VOLUME_MIX_COST_SPREAD_MARGIN_BRIDGE_VS_AUTO_PARTS_BETA_FADE",
  "loop_objective": [
    "coverage_gap_fill",
    "counterexample_mining",
    "mobility_volume_margin_operating_leverage_guardrail",
    "auto_lighting_ADAS_chassis_parts_volume_mix_margin_bridge_test",
    "auto_parts_beta_MFE_vs_cost_spread_margin_bridge_test",
    "local_4B_timing_after_auto_parts_MFE",
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
scheduled_loop = 85
allowed_large_sector = L3_BATTERY_EV_GREEN_MOBILITY or L9_CONSTRUCTION_REALESTATE_HOUSING depending on mobility/transport vs construction/PF nature
selected_large_sector = L3_BATTERY_EV_GREEN_MOBILITY
selected_canonical_archetype_id = C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE
computed_next_round = R10
computed_next_loop = 85
round_schedule_status = valid
round_sector_consistency = pass
```

R9 is routed to C29 because this run tests mobility / auto-parts operating leverage rather than construction/PF stress. Loop84 already tested tire-volume rows, so loop85 uses a different C29 fine route: lighting, ADAS/chassis, platform mix and cost-spread margin bridge.

The tested mechanism:

```text
auto-parts / lighting / ADAS / chassis volume headline
→ OEM platform or order mix
→ utilization and product mix
→ ASP or raw-material cost spread
→ gross / OP margin conversion
→ durable rerating or auto-parts beta fade
```

C29 is the assembly line test. Volume alone is the conveyor belt; margin appears only when the right mix, utilization and spread move together.

## 3. Previous Coverage / Duplicate Avoidance Check

No-Repeat is used only as a duplicate ledger.

```text
hard_duplicate_key = canonical_archetype_id + symbol + trigger_type + entry_date
```

C29 top-covered symbols include `UNKNOWN_SYMBOL`, `000270`, `161390`, `012330`, `005380`, and `018880`. This run avoids that top-covered set and uses:

```text
005850 / 에스엘
204320 / HL만도
010690 / 화신
```

All three are treated as new independent C29 auto-parts volume / margin-operating-leverage cases for this loop. No hard duplicate is intentionally reused.

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
| 005850 | 에스엘 | `atlas/symbol_profiles/005/005850.json` | old CA candidates through 2019; selected 2024 forward window clean |
| 204320 | HL만도 | `atlas/symbol_profiles/204/204320.json` | old 2018 CA candidate; selected 2024 forward window clean |
| 010690 | 화신 | `atlas/symbol_profiles/010/010690.json` | old CA candidates through 2001; selected 2024 forward window clean |

## 5. Historical Eligibility Gate

| case_id | symbol | entry_date | entry_price | forward window | 180D status | calibration_usable |
|---|---:|---|---:|---:|---|---|
| R9L85-C29-01 | 005850 | 2024-02-13 | 34,300 | 180D | clean | true |
| R9L85-C29-02 | 204320 | 2024-02-13 | 34,150 | 180D | clean | true |
| R9L85-C29-03 | 010690 | 2024-02-13 | 12,710 | 180D | clean | true |

## 6. Canonical Archetype Compression Map

| canonical_archetype_id | fine/deep route | keep / reject logic |
|---|---|---|
| C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE | AUTO_LIGHTING_GLOBAL_MIX_MARGIN_BRIDGE | keep Stage2 with OEM volume, product mix, utilization, ASP/cost spread and margin bridge |
| C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE | ADAS_CHASSIS_PARTS_BETA_RISKWATCH | keep Stage2 only with high-MAE/local 4B watch until platform mix and margin bridge are repaired |
| C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE | CHASSIS_AUTO_PARTS_BETA_FADE | reject auto-parts beta MFE without platform mix, cost pass-through and margin bridge |

## 7. Case Selection Summary

| case_id | symbol | company | trigger_type | entry_date | entry_price | MFE_180D_pct | MAE_180D_pct | current_profile_verdict |
|---|---:|---|---|---|---:|---:|---:|---|
| R9L85-C29-01 | 005850 | 에스엘 | Stage2-Actionable | 2024-02-13 | 34,300 | 35.28 | -11.37 | current_profile_partially_correct_local_4B_watch_needed |
| R9L85-C29-02 | 204320 | HL만도 | Stage2-Actionable | 2024-02-13 | 34,150 | 35.87 | -9.66 | current_profile_partially_correct_high_MAE_watch_needed |
| R9L85-C29-03 | 010690 | 화신 | Stage2-FalsePositive | 2024-02-13 | 12,710 | 25.02 | -38.08 | current_profile_false_positive_high_MAE_4B_late |

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

This MD therefore creates a source-repair queue and a C29 auto-parts shadow guardrail candidate. It must not be promoted directly into runtime weights until a later source-repair pass attaches primary evidence URLs: OEM platform order mix, shipment volume, utilization, ASP, FX/raw-material spread, gross/OP margin bridge, company disclosure or report evidence.

## 10. Price Data Source Map

| symbol | shard path | profile path |
|---|---|---|
| 005850 | `atlas/ohlcv_tradable_by_symbol_year/005/005850/2024.csv` | `atlas/symbol_profiles/005/005850.json` |
| 204320 | `atlas/ohlcv_tradable_by_symbol_year/204/204320/2024.csv` | `atlas/symbol_profiles/204/204320.json` |
| 010690 | `atlas/ohlcv_tradable_by_symbol_year/010/010690/2024.csv` | `atlas/symbol_profiles/010/010690.json` |

## 11. Case-by-Case Trigger Grid

### Case 1 — 005850 / 에스엘

C29 auto-lighting positive with local 4B watch. The February entry eventually produced a delayed MFE into early summer. However, the post-peak drawdown shows that volume/platform mix alone is not clean Green. It needs product mix, ASP/cost spread and margin bridge repair.

### Case 2 — 204320 / HL만도

C29 ADAS/chassis positive but beta-sensitive. The path generated a meaningful MFE, but it later retraced. This should remain Stage2-Actionable only with local 4B/high-MAE RiskWatch until utilization and margin evidence are repaired.

### Case 3 — 010690 / 화신

C29 chassis auto-parts beta counterexample. The MFE was tradable, but the later MAE was deep. This is the rejection row: platform or vehicle-cycle beta without cost pass-through and margin conversion should not become clean Stage2.

## 12. Trigger-Level OHLC Backtest Tables

| symbol | entry | MFE30 | MAE30 | MFE90 | MAE90 | MFE180 | MAE180 | peak | post-peak DD |
|---|---:|---:|---:|---:|---:|---:|---:|---|---:|
| 005850 | 34,300 | 4.81 | -8.16 | 32.94 | -9.04 | 35.28 | -11.37 | 2024-07-01 / 46,400 | -34.48 |
| 204320 | 34,150 | 3.22 | -5.86 | 35.87 | -5.86 | 35.87 | -9.66 | 2024-06-26 / 46,400 | -33.51 |
| 010690 | 12,710 | 3.38 | -16.21 | 25.02 | -16.21 | 25.02 | -38.08 | 2024-06-27 / 15,890 | -50.47 |

## 13. Current Calibrated Profile Stress Test

| case_id | P0 likely behavior | actual path | verdict |
|---|---|---|---|
| R9L85-C29-01 | Stage2-Actionable if volume/mix bridge exists | delayed MFE, later drawdown | partially correct; local 4B watch needed |
| R9L85-C29-02 | Stage2-Actionable if ADAS/platform mix is over-credited | MFE then retrace | high-MAE / beta RiskWatch needed |
| R9L85-C29-03 | risk of treating auto-parts beta as Stage2 | MFE then deep MAE | false positive / high-MAE guardrail |

## 14. Stage2 / Yellow / Green Comparison

```text
green_lateness_ratio = not_applicable
reason = no confirmed Stage3-Green trigger is assigned in this residual MD
```

For C29, the residual is whether mobility/auto-parts MFE becomes clean Stage2/Green before platform mix, utilization, ASP/cost spread and margin conversion are proven.

## 15. 4B Local vs Full-window Timing Audit

| case_id | local proximity | full-window proximity | verdict |
|---|---:|---:|---|
| R9L85-C29-01 | 0.78 | 0.68 | local 4B watch after auto-lighting MFE if order mix/cost spread margin bridge stalls |
| R9L85-C29-02 | 0.78 | 0.68 | local 4B and auto-parts beta RiskWatch when ADAS parts MFE outruns margin bridge |
| R9L85-C29-03 | 0.35 | 0.30 | auto-chassis beta rejected without platform mix/utilization/cost spread margin bridge |

## 16. 4C Protection Audit

No hard 4C is promoted from this file.

```text
four_c_protection_label = hard_4C_requires_non_price_volume_platform_or_margin_break
hard_4c_price_only_allowed = false
```

Price drawdown alone is not hard 4C. C29 hard 4C requires confirmed volume collapse, OEM platform loss, utilization break, cost-spread compression, or margin thesis break.

## 17. Sector-Specific Rule Candidate

```text
rule_scope = no_new_global_rule
sector_specific_rule_candidate = L3/C29 auto-parts rows need shipment volume, platform/order mix, utilization, ASP/raw-material spread and margin conversion before clean Stage2/Green
confidence = low
reason = all evidence rows are source_proxy_only / evidence_url_pending
```

## 18. Canonical-Archetype Rule Candidate

```text
canonical_archetype_id = C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE
candidate_axis = C29_auto_parts_volume_platform_mix_cost_spread_margin_bridge_required
effect = keep auto-parts positives with local 4B/high-MAE watch; demote beta false positives
production_scoring_changed = false
shadow_weight_only = true
do_not_propose_new_weight_delta = true
```

## 19. Before / After Backtest Comparison

| profile | eligible triggers | avg MFE90 | avg MAE90 | false-positive behavior | verdict |
|---|---:|---:|---:|---|---|
| P0 e2r_2_1_stock_web_calibrated_proxy | 3 | 31.28 | -10.37 | may over-credit auto-parts beta without margin bridge | needs C29 auto-parts bridge repair |
| P1 canonical shadow bridge profile | 3 | 34.41 on kept positives | -7.45 on kept positives | demotes 010690 | better alignment, source repair required |

## 20. Score-Return Alignment Matrix

| case_id | weighted before | label before | weighted after | label after | alignment |
|---|---:|---|---:|---|---|
| R9L85-C29-01 | 76 | Stage2-Actionable | 73 | Stage2-Actionable + local 4B/auto-parts margin watch | partially aligned |
| R9L85-C29-02 | 76 | Stage2-Actionable | 73 | Stage2-Actionable + local 4B/auto-parts margin watch | partially aligned |
| R9L85-C29-03 | 58 | Stage2-Watch/FalsePositive | 44 | Rejected-Stage2 / Auto-parts beta RiskWatch | improved |

## 21. Coverage Matrix

| large_sector_id | canonical_archetype_id | fine_archetype_id | positive | counterexample | 4B | 4C | new cases | reused | usable triggers | current errors | sector rule | canonical rule | coverage gap after |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---|---|---|
| L3_BATTERY_EV_GREEN_MOBILITY | C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE | AUTO_LIGHTING_ADAS_CHASSIS_PARTS_VOLUME_MIX_COST_SPREAD_MARGIN_BRIDGE_VS_AUTO_PARTS_BETA_FADE | 2 | 1 | 3-watch | 0-hard | 3 | 0 | 3 | 2 | no | yes | source repair needed |

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
  - auto_parts_beta_false_positive_high_MAE
  - volume_platform_mix_cost_spread_margin_bridge_required
  - local_4B_late_after_auto_parts_MFE
  - source_proxy_runtime_promotion_risk
  - high_MAE_positive_Green_blocker
new_axis_proposed: false
existing_axis_strengthened:
  - C29_auto_parts_volume_platform_mix_cost_spread_margin_bridge_required
  - source_proxy_only_blocks_runtime_promotion
  - local_4B_watch_before_full_4B_when_MFE_outruns_bridge
  - high_MAE_blocks_clean_Green
existing_axis_weakened: null
existing_axis_kept:
  - full_4b_requires_non_price_evidence
  - hard_4c_thesis_break_routes_to_4c
sector_specific_rule_candidate: null
canonical_archetype_rule_candidate: C29_auto_parts_volume_platform_mix_cost_spread_margin_bridge_required
no_new_signal_reason: null
loop_contribution_label: canonical_archetype_rule_candidate
do_not_propose_new_weight_delta: true
```

This loop adds 3 new independent cases, 1 counterexample, and 2 residual errors for R9/L3_BATTERY_EV_GREEN_MOBILITY/C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE.

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
- volume/shipment data
- utilization / ASP / raw-material cost spread
- gross/OP margin conversion
- production scoring implementation
```

## 24. Shadow Weight Calibration

```csv
row_type,axis,scope,large_sector_id,canonical_archetype_id,baseline_value,tested_value,delta,reason,backtest_effect,trigger_ids,calibration_usable_count,new_independent_case_count,counterexample_count,confidence,proposal_type,notes
shadow_weight,C29_auto_parts_volume_platform_mix_cost_spread_margin_bridge_required,canonical_archetype_specific,L3_BATTERY_EV_GREEN_MOBILITY,C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE,0,1,+1,"Require auto-parts volume, platform/order mix, utilization, ASP/raw-material spread and margin conversion before clean Stage2/Green","keeps 005850/204320 with local 4B or high-MAE RiskWatch; demotes 010690","R9L85-C29-01-S2A-20240213|R9L85-C29-02-S2A-20240213|R9L85-C29-03-S2FP-20240213",3,3,1,low,canonical_shadow_only,"source repair required; not production"
```

## 25. Machine-Readable Rows

```jsonl
{"row_type": "price_source_validation", "source": "Songdaiki/stock-web", "source_url": "https://github.com/Songdaiki/stock-web", "manifest_path": "atlas/manifest.json", "schema_path": "atlas/schema.json", "universe_path": "atlas/universe/all_symbols.csv", "manifest_max_date": "2026-02-20", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "raw_shard_root": "atlas/ohlcv_raw_by_symbol_year", "validation_status": "usable_for_historical_calibration"}
{"row_type": "case", "case_id": "R9L85-C29-01", "symbol": "005850", "company_name": "에스엘", "round": "R9", "loop": 85, "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE", "fine_archetype_id": "AUTO_LIGHTING_ADAS_CHASSIS_PARTS_VOLUME_MIX_COST_SPREAD_MARGIN_BRIDGE_VS_AUTO_PARTS_BETA_FADE", "case_type": "auto_lighting_global_mix_positive_with_local_4B_watch", "positive_or_counterexample": "positive", "best_trigger": "R9L85-C29-01-S2A-20240213", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "delayed_positive_MFE_but_local_4B_and_margin_bridge_watch_required", "current_profile_verdict": "current_profile_partially_correct_local_4B_watch_needed", "price_source": "Songdaiki/stock-web", "notes": "C29 auto-lighting positives need OEM volume, product mix, utilization, ASP/cost spread and gross/OP margin bridge before clean Green."}
{"row_type": "trigger", "trigger_id": "R9L85-C29-01-S2A-20240213", "case_id": "R9L85-C29-01", "symbol": "005850", "company_name": "에스엘", "round": "R9", "loop": 85, "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE", "fine_archetype_id": "AUTO_LIGHTING_ADAS_CHASSIS_PARTS_VOLUME_MIX_COST_SPREAD_MARGIN_BRIDGE_VS_AUTO_PARTS_BETA_FADE", "loop_objective": "coverage_gap_fill|counterexample_mining|mobility_volume_margin_operating_leverage_guardrail|auto_parts_volume_mix_cost_spread_margin_bridge|canonical_archetype_compression", "trigger_type": "Stage2-Actionable", "trigger_date": "2024-02-13", "evidence_available_at_that_date": "auto lighting / global OEM mix / vehicle volume and margin leverage proxy; primary order-mix and margin evidence pending", "evidence_source": "source_proxy_only; evidence_url_pending", "stage2_evidence_fields": ["volume_or_shipment_proxy", "platform_or_order_mix_proxy", "ASP_or_cost_spread_proxy"], "stage3_evidence_fields": ["confirmed_volume_growth", "platform_mix", "utilization", "ASP_or_raw_material_cost_spread", "gross_or_OP_margin_conversion"], "stage4b_evidence_fields": ["auto_parts_MFE_without_margin_bridge", "post_peak_drawdown", "source_proxy_gap"], "stage4c_evidence_fields": ["hard_volume_or_platform_mix_margin_break_watch_only"], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/005/005850/2024.csv", "profile_path": "atlas/symbol_profiles/005/005850.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "entry_date": "2024-02-13", "entry_price": 34300, "MFE_30D_pct": 4.81, "MFE_90D_pct": 32.94, "MFE_180D_pct": 35.28, "MFE_1Y_pct": null, "MFE_2Y_pct": null, "MAE_30D_pct": -8.16, "MAE_90D_pct": -9.04, "MAE_180D_pct": -11.37, "MAE_1Y_pct": null, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2024-07-01", "peak_price": 46400, "drawdown_after_peak_pct": -34.48, "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": 0.78, "four_b_full_window_peak_proximity": 0.68, "four_b_timing_verdict": "local_4B_watch_after_auto_lighting_MFE_if_order_mix_cost_spread_margin_bridge_stalls", "four_b_evidence_type": ["auto_parts_MFE_without_margin_bridge", "post_peak_drawdown", "source_proxy_gap"], "four_c_protection_label": "hard_4C_requires_non_price_volume_platform_or_margin_break", "trigger_outcome_label": "delayed_positive_MFE_but_local_4B_and_margin_bridge_watch_required", "current_profile_verdict": "current_profile_partially_correct_local_4B_watch_needed", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_2024_window_after_old_2019_CA_candidate", "same_entry_group_id": "R9L85-C29-01", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R9L85-C29-01", "trigger_id": "R9L85-C29-01-S2A-20240213", "symbol": "005850", "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE", "raw_component_scores_before": {"volume_or_shipment_score": 50, "platform_or_order_mix_score": 45, "utilization_score": 40, "ASP_or_cost_spread_score": 40, "gross_margin_bridge_score": 40, "OP_leverage_score": 40, "customer_quality_score": 40, "revision_score": 40, "relative_strength_score": 60, "valuation_blowoff_risk_score": 55, "execution_risk_score": 55, "source_quality_score": 20, "4B_watch_score": 45}, "weighted_score_before": 76, "stage_label_before": "Stage2-Actionable", "raw_component_scores_after": {"volume_or_shipment_score": 50, "platform_or_order_mix_score": 45, "utilization_score": 40, "ASP_or_cost_spread_score": 40, "gross_margin_bridge_score": 40, "OP_leverage_score": 40, "customer_quality_score": 40, "revision_score": 40, "relative_strength_score": 60, "valuation_blowoff_risk_score": 55, "execution_risk_score": 65, "source_quality_score": 10, "4B_watch_score": 80}, "weighted_score_after": 73, "stage_label_after": "Stage2-Actionable + local 4B/auto-parts margin watch", "changed_components": ["platform_or_order_mix_score", "utilization_score", "ASP_or_cost_spread_score", "gross_margin_bridge_score", "OP_leverage_score", "source_quality_score", "execution_risk_score", "4B_watch_score"], "component_delta_explanation": "C29 requires auto-parts volume or platform signal to convert into order mix, utilization, ASP/raw-material cost spread and margin conversion before clean Stage2/Green; auto-parts beta MFE alone is demoted or wrapped with local 4B/high-MAE watch.", "MFE_90D_pct": 32.94, "MAE_90D_pct": -9.04, "score_return_alignment_label": "delayed_positive_MFE_but_local_4B_and_margin_bridge_watch_required", "current_profile_verdict": "current_profile_partially_correct_local_4B_watch_needed"}
{"row_type": "case", "case_id": "R9L85-C29-02", "symbol": "204320", "company_name": "HL만도", "round": "R9", "loop": 85, "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE", "fine_archetype_id": "AUTO_LIGHTING_ADAS_CHASSIS_PARTS_VOLUME_MIX_COST_SPREAD_MARGIN_BRIDGE_VS_AUTO_PARTS_BETA_FADE", "case_type": "ADAS_chassis_parts_volume_margin_positive_with_beta_riskwatch", "positive_or_counterexample": "positive", "best_trigger": "R9L85-C29-02-S2A-20240213", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "positive_MFE_but_high_MAE_and_beta_RiskWatch", "current_profile_verdict": "current_profile_partially_correct_high_MAE_watch_needed", "price_source": "Songdaiki/stock-web", "notes": "ADAS/chassis parts positives need platform mix, orderbook quality, utilization, FX/raw-material spread and OP-margin conversion before clean Green."}
{"row_type": "trigger", "trigger_id": "R9L85-C29-02-S2A-20240213", "case_id": "R9L85-C29-02", "symbol": "204320", "company_name": "HL만도", "round": "R9", "loop": 85, "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE", "fine_archetype_id": "AUTO_LIGHTING_ADAS_CHASSIS_PARTS_VOLUME_MIX_COST_SPREAD_MARGIN_BRIDGE_VS_AUTO_PARTS_BETA_FADE", "loop_objective": "coverage_gap_fill|counterexample_mining|mobility_volume_margin_operating_leverage_guardrail|auto_parts_volume_mix_cost_spread_margin_bridge|canonical_archetype_compression", "trigger_type": "Stage2-Actionable", "trigger_date": "2024-02-13", "evidence_available_at_that_date": "ADAS/chassis global platform volume, order mix and margin recovery proxy; primary orderbook, utilization and margin evidence pending", "evidence_source": "source_proxy_only; evidence_url_pending", "stage2_evidence_fields": ["volume_or_shipment_proxy", "platform_or_order_mix_proxy", "ASP_or_cost_spread_proxy"], "stage3_evidence_fields": ["confirmed_volume_growth", "platform_mix", "utilization", "ASP_or_raw_material_cost_spread", "gross_or_OP_margin_conversion"], "stage4b_evidence_fields": ["auto_parts_MFE_without_margin_bridge", "post_peak_drawdown", "source_proxy_gap"], "stage4c_evidence_fields": ["hard_volume_or_platform_mix_margin_break_watch_only"], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/204/204320/2024.csv", "profile_path": "atlas/symbol_profiles/204/204320.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "entry_date": "2024-02-13", "entry_price": 34150, "MFE_30D_pct": 3.22, "MFE_90D_pct": 35.87, "MFE_180D_pct": 35.87, "MFE_1Y_pct": null, "MFE_2Y_pct": null, "MAE_30D_pct": -5.86, "MAE_90D_pct": -5.86, "MAE_180D_pct": -9.66, "MAE_1Y_pct": null, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2024-06-26", "peak_price": 46400, "drawdown_after_peak_pct": -33.51, "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": 0.78, "four_b_full_window_peak_proximity": 0.68, "four_b_timing_verdict": "local_4B_and_auto_parts_beta_RiskWatch_when_ADAS_parts_MFE_outruns_margin_bridge", "four_b_evidence_type": ["auto_parts_MFE_without_margin_bridge", "post_peak_drawdown", "source_proxy_gap"], "four_c_protection_label": "hard_4C_requires_non_price_volume_platform_or_margin_break", "trigger_outcome_label": "positive_MFE_but_high_MAE_and_beta_RiskWatch", "current_profile_verdict": "current_profile_partially_correct_high_MAE_watch_needed", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_2024_window_after_old_2018_CA_candidate", "same_entry_group_id": "R9L85-C29-02", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R9L85-C29-02", "trigger_id": "R9L85-C29-02-S2A-20240213", "symbol": "204320", "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE", "raw_component_scores_before": {"volume_or_shipment_score": 50, "platform_or_order_mix_score": 45, "utilization_score": 40, "ASP_or_cost_spread_score": 40, "gross_margin_bridge_score": 40, "OP_leverage_score": 40, "customer_quality_score": 40, "revision_score": 40, "relative_strength_score": 60, "valuation_blowoff_risk_score": 55, "execution_risk_score": 55, "source_quality_score": 20, "4B_watch_score": 45}, "weighted_score_before": 76, "stage_label_before": "Stage2-Actionable", "raw_component_scores_after": {"volume_or_shipment_score": 50, "platform_or_order_mix_score": 45, "utilization_score": 40, "ASP_or_cost_spread_score": 40, "gross_margin_bridge_score": 40, "OP_leverage_score": 40, "customer_quality_score": 40, "revision_score": 40, "relative_strength_score": 60, "valuation_blowoff_risk_score": 55, "execution_risk_score": 65, "source_quality_score": 10, "4B_watch_score": 80}, "weighted_score_after": 73, "stage_label_after": "Stage2-Actionable + local 4B/auto-parts margin watch", "changed_components": ["platform_or_order_mix_score", "utilization_score", "ASP_or_cost_spread_score", "gross_margin_bridge_score", "OP_leverage_score", "source_quality_score", "execution_risk_score", "4B_watch_score"], "component_delta_explanation": "C29 requires auto-parts volume or platform signal to convert into order mix, utilization, ASP/raw-material cost spread and margin conversion before clean Stage2/Green; auto-parts beta MFE alone is demoted or wrapped with local 4B/high-MAE watch.", "MFE_90D_pct": 35.87, "MAE_90D_pct": -5.86, "score_return_alignment_label": "positive_MFE_but_high_MAE_and_beta_RiskWatch", "current_profile_verdict": "current_profile_partially_correct_high_MAE_watch_needed"}
{"row_type": "case", "case_id": "R9L85-C29-03", "symbol": "010690", "company_name": "화신", "round": "R9", "loop": 85, "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE", "fine_archetype_id": "AUTO_LIGHTING_ADAS_CHASSIS_PARTS_VOLUME_MIX_COST_SPREAD_MARGIN_BRIDGE_VS_AUTO_PARTS_BETA_FADE", "case_type": "chassis_auto_parts_volume_beta_high_MAE_counterexample", "positive_or_counterexample": "counterexample", "best_trigger": "R9L85-C29-03-S2FP-20240213", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "MFE_then_deep_MAE_auto_parts_beta_false_positive", "current_profile_verdict": "current_profile_false_positive_high_MAE_4B_late", "price_source": "Songdaiki/stock-web", "notes": "Auto chassis / parts beta should be rejected unless platform mix, utilization, cost pass-through and margin conversion are visible at entry."}
{"row_type": "trigger", "trigger_id": "R9L85-C29-03-S2FP-20240213", "case_id": "R9L85-C29-03", "symbol": "010690", "company_name": "화신", "round": "R9", "loop": 85, "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE", "fine_archetype_id": "AUTO_LIGHTING_ADAS_CHASSIS_PARTS_VOLUME_MIX_COST_SPREAD_MARGIN_BRIDGE_VS_AUTO_PARTS_BETA_FADE", "loop_objective": "coverage_gap_fill|counterexample_mining|mobility_volume_margin_operating_leverage_guardrail|auto_parts_volume_mix_cost_spread_margin_bridge|canonical_archetype_compression", "trigger_type": "Stage2-FalsePositive", "trigger_date": "2024-02-13", "evidence_available_at_that_date": "auto chassis / parts volume and mobility beta proxy without confirmed platform mix, cost pass-through and margin bridge", "evidence_source": "source_proxy_only; evidence_url_pending", "stage2_evidence_fields": ["volume_or_shipment_proxy", "platform_or_order_mix_proxy", "ASP_or_cost_spread_proxy"], "stage3_evidence_fields": ["confirmed_volume_growth", "platform_mix", "utilization", "ASP_or_raw_material_cost_spread", "gross_or_OP_margin_conversion"], "stage4b_evidence_fields": ["auto_parts_MFE_without_margin_bridge", "post_peak_drawdown", "source_proxy_gap"], "stage4c_evidence_fields": ["hard_volume_or_platform_mix_margin_break_watch_only"], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/010/010690/2024.csv", "profile_path": "atlas/symbol_profiles/010/010690.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "entry_date": "2024-02-13", "entry_price": 12710, "MFE_30D_pct": 3.38, "MFE_90D_pct": 25.02, "MFE_180D_pct": 25.02, "MFE_1Y_pct": null, "MFE_2Y_pct": null, "MAE_30D_pct": -16.21, "MAE_90D_pct": -16.21, "MAE_180D_pct": -38.08, "MAE_1Y_pct": null, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2024-06-27", "peak_price": 15890, "drawdown_after_peak_pct": -50.47, "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": 0.35, "four_b_full_window_peak_proximity": 0.3, "four_b_timing_verdict": "auto_chassis_beta_rejected_without_platform_mix_utilization_cost_spread_margin_bridge", "four_b_evidence_type": ["auto_parts_MFE_without_margin_bridge", "post_peak_drawdown", "source_proxy_gap"], "four_c_protection_label": "hard_4C_requires_non_price_volume_platform_or_margin_break", "trigger_outcome_label": "MFE_then_deep_MAE_auto_parts_beta_false_positive", "current_profile_verdict": "current_profile_false_positive_high_MAE_4B_late", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_2024_window_after_old_2001_CA_candidate", "same_entry_group_id": "R9L85-C29-03", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R9L85-C29-03", "trigger_id": "R9L85-C29-03-S2FP-20240213", "symbol": "010690", "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE", "raw_component_scores_before": {"volume_or_shipment_score": 25, "platform_or_order_mix_score": 15, "utilization_score": 10, "ASP_or_cost_spread_score": 5, "gross_margin_bridge_score": 5, "OP_leverage_score": 5, "customer_quality_score": 20, "revision_score": 15, "relative_strength_score": 35, "valuation_blowoff_risk_score": 65, "execution_risk_score": 80, "source_quality_score": 15, "4B_watch_score": 75}, "weighted_score_before": 58, "stage_label_before": "Stage2-Watch/FalsePositive", "raw_component_scores_after": {"volume_or_shipment_score": 25, "platform_or_order_mix_score": 0, "utilization_score": 0, "ASP_or_cost_spread_score": 0, "gross_margin_bridge_score": 0, "OP_leverage_score": 0, "customer_quality_score": 20, "revision_score": 15, "relative_strength_score": 35, "valuation_blowoff_risk_score": 65, "execution_risk_score": 90, "source_quality_score": 5, "4B_watch_score": 85}, "weighted_score_after": 44, "stage_label_after": "Rejected-Stage2 / Auto-parts beta RiskWatch", "changed_components": ["platform_or_order_mix_score", "utilization_score", "ASP_or_cost_spread_score", "gross_margin_bridge_score", "OP_leverage_score", "source_quality_score", "execution_risk_score", "4B_watch_score"], "component_delta_explanation": "C29 requires auto-parts volume or platform signal to convert into order mix, utilization, ASP/raw-material cost spread and margin conversion before clean Stage2/Green; auto-parts beta MFE alone is demoted or wrapped with local 4B/high-MAE watch.", "MFE_90D_pct": 25.02, "MAE_90D_pct": -16.21, "score_return_alignment_label": "MFE_then_deep_MAE_auto_parts_beta_false_positive", "current_profile_verdict": "current_profile_false_positive_high_MAE_4B_late"}
{"row_type": "shadow_weight", "axis": "C29_auto_parts_volume_platform_mix_cost_spread_margin_bridge_required", "scope": "canonical_archetype_specific", "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE", "baseline_value": 0, "tested_value": 1, "delta": "+1", "reason": "Auto-parts/mobility rerating requires volume, platform or order mix, utilization, ASP/raw-material cost spread and gross/OP margin conversion; auto-parts beta MFE without bridge fades or needs local 4B/high-MAE watch.", "backtest_effect": "keeps 005850/204320 with local 4B or high-MAE RiskWatch; demotes 010690 auto-parts beta false positive", "trigger_ids": "R9L85-C29-01-S2A-20240213|R9L85-C29-02-S2A-20240213|R9L85-C29-03-S2FP-20240213", "calibration_usable_count": 3, "new_independent_case_count": 3, "counterexample_count": 1, "confidence": "low", "proposal_type": "canonical_shadow_only", "notes": "source_proxy_only/evidence_url_pending; not production"}
{"row_type": "residual_contribution", "round": "R9", "loop": 85, "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE", "new_independent_case_count": 3, "reused_case_count": 0, "new_symbol_count": 3, "new_trigger_family_count": 3, "tested_existing_calibrated_axes": ["stage2_actionable_evidence_bonus", "price_only_blowoff_blocks_positive_stage", "full_4b_requires_non_price_evidence", "hard_4c_thesis_break_routes_to_4c", "source_proxy_only_blocks_runtime_promotion", "high_MAE_guardrail", "local_4B_watch_before_full_4B_when_MFE_outruns_bridge"], "residual_error_types_found": ["auto_parts_beta_false_positive_high_MAE", "volume_platform_mix_cost_spread_margin_bridge_required", "local_4B_late_after_auto_parts_MFE", "source_proxy_runtime_promotion_risk", "high_MAE_positive_Green_blocker"], "loop_contribution_label": "canonical_archetype_rule_candidate", "do_not_propose_new_weight_delta": true}
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
- For C29 auto-parts rows, test a canonical-archetype guard requiring volume, platform/order mix, utilization, ASP/raw-material spread and gross/OP margin conversion before clean Stage2/Green.

## 27. Next Round State

```text
completed_round = R9
completed_loop = 85
next_round = R10
next_loop = 85
round_schedule_status = valid
round_sector_consistency = pass
```

## 28. Source Notes

```text
MAIN_EXECUTION_PROMPT = docs/core/e2r_v12_prompt_round_scheduler_corrected.txt
NO_REPEAT_INDEX = docs/core/V12_Research_No_Repeat_Index.md
price_source = Songdaiki/stock-web
```
