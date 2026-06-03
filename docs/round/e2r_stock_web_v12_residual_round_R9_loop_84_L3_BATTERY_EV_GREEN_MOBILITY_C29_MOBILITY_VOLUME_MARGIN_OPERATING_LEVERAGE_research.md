# E2R Stock-Web v12 Residual Research — R9 Loop 84 / L3 / C29

## 0. Research Metadata

```json
{
  "research_session": "post_calibrated_sector_archetype_residual_research",
  "mode": "historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12",
  "scheduled_round": "R9",
  "scheduled_loop": 84,
  "round_schedule_status": "valid",
  "round_sector_consistency": "pass",
  "completed_round": "R9",
  "completed_loop": 84,
  "computed_next_round": "R10",
  "computed_next_loop": 84,
  "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY",
  "canonical_archetype_id": "C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE",
  "fine_archetype_id": "TIRE_EXPORT_VOLUME_RAWMATERIAL_COST_MARGIN_AUTO_PARTS_UTILIZATION_BRIDGE_VS_VEHICLE_THEME_FADE",
  "loop_objective": [
    "coverage_gap_fill",
    "counterexample_mining",
    "mobility_volume_margin_operating_leverage_guardrail",
    "tire_export_volume_rawmaterial_margin_bridge_test",
    "auto_parts_utilization_margin_bridge_false_positive_test",
    "local_4B_timing_after_mobility_MFE",
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
scheduled_loop = 84
allowed_large_sector = L3_BATTERY_EV_GREEN_MOBILITY or L9_CONSTRUCTION_REALESTATE_HOUSING depending on mobility/transport nature
selected_large_sector = L3_BATTERY_EV_GREEN_MOBILITY
selected_canonical_archetype_id = C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE
computed_next_round = R10
computed_next_loop = 84
round_schedule_status = valid
round_sector_consistency = pass
```

R9 is routed to C29 because this run tests tire / auto-parts mobility operating leverage rather than PF or construction balance-sheet stress.

The tested mechanism:

```text
mobility / tire / auto-parts volume headline
→ shipment or production volume
→ utilization and product mix
→ ASP or raw-material cost spread
→ gross/OP margin conversion
→ durable rerating or local 4B / false-positive fade
```

C29 is not “car cycle up.” It is the factory floor turning faster while the spread meter widens. Without utilization and margin conversion, volume is only noise.

## 3. Previous Coverage / Duplicate Avoidance Check

No-Repeat is used only as a duplicate ledger.

```text
hard_duplicate_key = canonical_archetype_id + symbol + trigger_type + entry_date
```

C29 top-covered symbols include `UNKNOWN_SYMBOL`, `000270`, `161390`, `012330`, `005380`, and `018880`. This run avoids that top-covered set and uses:

```text
073240 / 금호타이어
002350 / 넥센타이어
011210 / 현대위아
```

All three are treated as new independent C29 mobility-volume / margin-operating-leverage cases for this loop. No hard duplicate is intentionally reused.

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
| 073240 | 금호타이어 | `atlas/symbol_profiles/073/073240.json` | old 2010/2018 CA candidates; selected 2024 forward window clean |
| 002350 | 넥센타이어 | `atlas/symbol_profiles/002/002350.json` | old CA candidates through 2008; selected 2024 forward window clean |
| 011210 | 현대위아 | `atlas/symbol_profiles/011/011210.json` | no profile-level CA candidate |

## 5. Historical Eligibility Gate

| case_id | symbol | entry_date | entry_price | forward window | 180D status | calibration_usable |
|---|---:|---|---:|---:|---|---|
| R9L84-C29-01 | 073240 | 2024-01-25 | 5,900 | 180D | clean | true |
| R9L84-C29-02 | 002350 | 2024-02-02 | 8,230 | 180D | clean | true |
| R9L84-C29-03 | 011210 | 2024-02-02 | 64,500 | 180D | clean | true |

## 6. Canonical Archetype Compression Map

| canonical_archetype_id | fine/deep route | keep / reject logic |
|---|---|---|
| C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE | TIRE_EXPORT_VOLUME_COST_SPREAD_MARGIN_BRIDGE | keep Stage2 only with shipment volume, utilization, ASP/raw-material spread and margin bridge |
| C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE | TIRE_TURNAROUND_HIGH_MAE_RISKWATCH | allow Stage2 only with high-MAE RiskWatch and local 4B when MFE outruns margin evidence |
| C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE | AUTO_PARTS_PLATFORM_UTILIZATION_THEME_FADE | reject if mobility/auto-parts theme lacks platform mix, utilization and margin conversion |

## 7. Case Selection Summary

| case_id | symbol | company | trigger_type | entry_date | entry_price | MFE_180D_pct | MAE_180D_pct | current_profile_verdict |
|---|---:|---|---|---|---:|---:|---:|---|
| R9L84-C29-01 | 073240 | 금호타이어 | Stage2-Actionable | 2024-01-25 | 5,900 | 17.46 | -30.0 | current_profile_4B_too_late_high_MAE |
| R9L84-C29-02 | 002350 | 넥센타이어 | Stage2-Actionable | 2024-02-02 | 8,230 | 17.25 | -17.98 | current_profile_partially_correct_local_4B_watch_needed |
| R9L84-C29-03 | 011210 | 현대위아 | Stage2-FalsePositive | 2024-02-02 | 64,500 | 3.88 | -29.53 | current_profile_false_positive_high_MAE |

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

This MD therefore creates a source-repair queue and a C29 shadow guardrail candidate. It must not be promoted directly into runtime weights until a later source-repair pass attaches primary evidence URLs: shipment volume, tire export/order data, OE/replacement mix, raw-material cost spread, ASP, plant utilization, platform mix, gross/OP margin bridge, company disclosure or report evidence.

## 10. Price Data Source Map

| symbol | shard path | profile path |
|---|---|---|
| 073240 | `atlas/ohlcv_tradable_by_symbol_year/073/073240/2024.csv` | `atlas/symbol_profiles/073/073240.json` |
| 002350 | `atlas/ohlcv_tradable_by_symbol_year/002/002350/2024.csv` | `atlas/symbol_profiles/002/002350.json` |
| 011210 | `atlas/ohlcv_tradable_by_symbol_year/011/011210/2024.csv` | `atlas/symbol_profiles/011/011210.json` |

## 11. Case-by-Case Trigger Grid

### Case 1 — 073240 / 금호타이어

C29 tire-volume positive but high-MAE. The initial tire-cycle MFE was real, but the later drawdown says the model must not treat this as clean Green unless the repaired source shows shipment growth, utilization, cost-spread and capital-structure/margin bridge.

### Case 2 — 002350 / 넥센타이어

C29 bounded tire-margin positive with local 4B watch. The MFE appeared early and then faded. This supports the idea that tire spread positives can be Stage2, but local 4B watch is needed when the margin bridge stops expanding.

### Case 3 — 011210 / 현대위아

C29 auto-parts false positive. The forward path gave only small MFE and deep MAE. Auto-parts or powertrain volume narrative should not become Stage2 unless platform mix, utilization and cost pass-through margin bridge are visible at entry.

## 12. Trigger-Level OHLC Backtest Tables

| symbol | entry | MFE30 | MAE30 | MFE90 | MAE90 | MFE180 | MAE180 | peak | post-peak DD |
|---|---:|---:|---:|---:|---:|---:|---:|---|---:|
| 073240 | 5,900 | 16.61 | -4.24 | 16.61 | -5.42 | 17.46 | -30.00 | 2024-06-26 / 6,930 | -40.40 |
| 002350 | 8,230 | 17.25 | -1.58 | 17.25 | -6.93 | 17.25 | -17.98 | 2024-02-26 / 9,650 | -30.05 |
| 011210 | 64,500 | 3.88 | -12.40 | 3.88 | -13.49 | 3.88 | -29.53 | 2024-02-05 / 67,000 | -32.16 |

## 13. Current Calibrated Profile Stress Test

| case_id | P0 likely behavior | actual path | verdict |
|---|---|---|---|
| R9L84-C29-01 | Stage2-Actionable if tire volume/margin bridge exists | positive MFE but large later MAE | 4B too late / high-MAE RiskWatch |
| R9L84-C29-02 | Stage2-Actionable if tire spread bridge exists | bounded MFE then fade | partially correct; local 4B watch needed |
| R9L84-C29-03 | risk of treating auto-parts theme as Stage2 | low MFE / high MAE | false positive |

## 14. Stage2 / Yellow / Green Comparison

```text
green_lateness_ratio = not_applicable
reason = no confirmed Stage3-Green trigger is assigned in this residual MD
```

For C29, the residual is not Green lateness. The residual is whether mobility/tire/auto-parts MFE becomes clean Stage2/Green before utilization, ASP/cost spread and margin conversion are proven.

## 15. 4B Local vs Full-window Timing Audit

| case_id | local proximity | full-window proximity | verdict |
|---|---:|---:|---|
| R9L84-C29-01 | 0.82 | 0.72 | local 4B and high-MAE RiskWatch when tire-volume MFE outruns evidence |
| R9L84-C29-02 | 0.82 | 0.72 | local 4B watch after tire margin MFE if volume/cost bridge stalls |
| R9L84-C29-03 | 0.30 | 0.25 | auto-parts theme rejected without order mix/utilization/margin bridge |

## 16. 4C Protection Audit

No hard 4C is promoted from this file.

```text
four_c_protection_label = hard_4C_requires_non_price_volume_or_utilization_break
hard_4c_price_only_allowed = false
```

## 17. Sector-Specific Rule Candidate

```text
rule_scope = no_new_global_rule
sector_specific_rule_candidate = L3/C29 mobility rows need shipment volume, utilization, ASP/raw-material spread and margin conversion before clean Stage2/Green
confidence = low
reason = all evidence rows are source_proxy_only / evidence_url_pending
```

## 18. Canonical-Archetype Rule Candidate

```text
canonical_archetype_id = C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE
candidate_axis = C29_mobility_volume_utilization_cost_spread_margin_bridge_required
effect = keep tire positives with local 4B/high-MAE watch; demote auto-parts theme false positives
production_scoring_changed = false
shadow_weight_only = true
do_not_propose_new_weight_delta = true
```

## 19. Before / After Backtest Comparison

| profile | eligible triggers | avg MFE90 | avg MAE90 | false-positive behavior | verdict |
|---|---:|---:|---:|---|---|
| P0 e2r_2_1_stock_web_calibrated_proxy | 3 | 12.58 | -8.61 | may over-credit mobility/tire/auto-parts theme MFE | needs C29 bridge repair |
| P1 canonical shadow bridge profile | 3 | 16.93 on kept positives | -6.18 on 90D kept positives, but 180D high-MAE watch | demotes 011210 | better alignment, source repair required |

## 20. Score-Return Alignment Matrix

| case_id | weighted before | label before | weighted after | label after | alignment |
|---|---:|---|---:|---|---|
| R9L84-C29-01 | 76 | Stage2-Actionable | 73 | Stage2-Actionable + high-MAE/local 4B watch | partially aligned |
| R9L84-C29-02 | 76 | Stage2-Actionable | 74 | Stage2-Actionable + local 4B watch | partially aligned |
| R9L84-C29-03 | 58 | Stage2-Watch/FalsePositive | 46 | Rejected-Stage2 / RiskWatch | improved |

## 21. Coverage Matrix

| large_sector_id | canonical_archetype_id | fine_archetype_id | positive | counterexample | 4B | 4C | new cases | reused | usable triggers | current errors | sector rule | canonical rule | coverage gap after |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---|---|---|
| L3_BATTERY_EV_GREEN_MOBILITY | C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE | TIRE_EXPORT_VOLUME_RAWMATERIAL_COST_MARGIN_AUTO_PARTS_UTILIZATION_BRIDGE_VS_VEHICLE_THEME_FADE | 2 | 1 | 3-watch | 0 | 3 | 0 | 3 | 2 | no | yes | source repair needed |

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
  - mobility_volume_theme_false_positive_high_MAE
  - tire_export_volume_cost_spread_margin_bridge_required
  - local_4B_late_after_mobility_MFE
  - source_proxy_runtime_promotion_risk
  - high_MAE_positive_Green_blocker
new_axis_proposed: false
existing_axis_strengthened:
  - C29_mobility_volume_utilization_cost_spread_margin_bridge_required
  - source_proxy_only_blocks_runtime_promotion
  - local_4B_watch_before_full_4B_when_MFE_outruns_bridge
  - high_MAE_blocks_clean_Green
existing_axis_weakened: null
existing_axis_kept:
  - full_4b_requires_non_price_evidence
  - hard_4c_thesis_break_routes_to_4c
sector_specific_rule_candidate: null
canonical_archetype_rule_candidate: C29_mobility_volume_utilization_cost_spread_margin_bridge_required
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
- tire export / shipment source
- OE/replacement mix and ASP
- raw-material cost spread
- plant utilization
- auto-parts platform mix and OP margin conversion
- production scoring implementation
```

## 24. Shadow Weight Calibration

```csv
row_type,axis,scope,large_sector_id,canonical_archetype_id,baseline_value,tested_value,delta,reason,backtest_effect,trigger_ids,calibration_usable_count,new_independent_case_count,counterexample_count,confidence,proposal_type,notes
shadow_weight,C29_mobility_volume_utilization_cost_spread_margin_bridge_required,canonical_archetype_specific,L3_BATTERY_EV_GREEN_MOBILITY,C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE,0,1,+1,"Require shipment volume, utilization, ASP/raw-material spread and margin conversion before clean Stage2/Green","keeps 073240/002350 with local 4B or high-MAE RiskWatch; demotes 011210","R9L84-C29-01-S2A-20240125|R9L84-C29-02-S2A-20240202|R9L84-C29-03-S2FP-20240202",3,3,1,low,canonical_shadow_only,"source repair required; not production"
```

## 25. Machine-Readable Rows

```jsonl
{"row_type": "price_source_validation", "source": "Songdaiki/stock-web", "source_url": "https://github.com/Songdaiki/stock-web", "manifest_path": "atlas/manifest.json", "schema_path": "atlas/schema.json", "universe_path": "atlas/universe/all_symbols.csv", "manifest_max_date": "2026-02-20", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "raw_shard_root": "atlas/ohlcv_raw_by_symbol_year", "validation_status": "usable_for_historical_calibration"}
{"row_type": "case", "case_id": "R9L84-C29-01", "symbol": "073240", "company_name": "금호타이어", "round": "R9", "loop": 84, "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE", "fine_archetype_id": "TIRE_EXPORT_VOLUME_RAWMATERIAL_COST_MARGIN_AUTO_PARTS_UTILIZATION_BRIDGE_VS_VEHICLE_THEME_FADE", "case_type": "tire_export_volume_margin_positive_but_high_MAE_watch", "positive_or_counterexample": "positive", "best_trigger": "R9L84-C29-01-S2A-20240125", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "positive_MFE_but_high_MAE_RiskWatch", "current_profile_verdict": "current_profile_4B_too_late_high_MAE", "price_source": "Songdaiki/stock-web", "notes": "C29 tire rerating can be real, but shipment volume, ASP/raw-material spread, utilization and margin bridge must be repaired before clean Green."}
{"row_type": "trigger", "trigger_id": "R9L84-C29-01-S2A-20240125", "case_id": "R9L84-C29-01", "symbol": "073240", "company_name": "금호타이어", "round": "R9", "loop": 84, "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE", "fine_archetype_id": "TIRE_EXPORT_VOLUME_RAWMATERIAL_COST_MARGIN_AUTO_PARTS_UTILIZATION_BRIDGE_VS_VEHICLE_THEME_FADE", "loop_objective": "coverage_gap_fill|counterexample_mining|mobility_volume_margin_operating_leverage_guardrail|local_4B_timing_after_mobility_MFE|canonical_archetype_compression", "trigger_type": "Stage2-Actionable", "trigger_date": "2024-01-25", "evidence_available_at_that_date": "tire volume/export recovery and raw-material cost tailwind proxy; primary shipment/ASP/spread evidence pending", "evidence_source": "source_proxy_only; evidence_url_pending", "stage2_evidence_fields": ["volume_or_shipment_proxy", "utilization_proxy", "ASP_or_cost_spread_proxy"], "stage3_evidence_fields": ["confirmed_volume_growth", "yield_or_ASP", "raw_material_cost_spread", "plant_utilization", "gross_or_OP_margin_conversion"], "stage4b_evidence_fields": ["mobility_MFE_without_margin_bridge", "valuation_overheat", "post_peak_drawdown"], "stage4c_evidence_fields": ["hard_volume_or_utilization_break_watch_only"], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/073/073240/2024.csv", "profile_path": "atlas/symbol_profiles/073/073240.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "entry_date": "2024-01-25", "entry_price": 5900, "MFE_30D_pct": 16.61, "MFE_90D_pct": 16.61, "MFE_180D_pct": 17.46, "MFE_1Y_pct": null, "MFE_2Y_pct": null, "MAE_30D_pct": -4.24, "MAE_90D_pct": -5.42, "MAE_180D_pct": -30.0, "MAE_1Y_pct": null, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2024-06-26", "peak_price": 6930, "drawdown_after_peak_pct": -40.4, "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": 0.82, "four_b_full_window_peak_proximity": 0.72, "four_b_timing_verdict": "local_4B_and_high_MAE_RiskWatch_needed_when_tire_volume_MFE_outruns_margin_bridge", "four_b_evidence_type": ["mobility_MFE_without_margin_bridge", "post_peak_drawdown", "source_proxy_gap"], "four_c_protection_label": "hard_4C_requires_non_price_volume_or_utilization_break", "trigger_outcome_label": "positive_MFE_but_high_MAE_RiskWatch", "current_profile_verdict": "current_profile_4B_too_late_high_MAE", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window_after_old_2018_CA_candidate", "same_entry_group_id": "R9L84-C29-01", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R9L84-C29-01", "trigger_id": "R9L84-C29-01-S2A-20240125", "symbol": "073240", "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE", "raw_component_scores_before": {"volume_or_shipment_score": 50, "utilization_score": 45, "yield_or_ASP_score": 35, "raw_material_cost_spread_score": 45, "margin_bridge_score": 40, "customer_or_channel_quality_score": 35, "revision_score": 40, "relative_strength_score": 55, "valuation_blowoff_risk_score": 60, "execution_risk_score": 60, "source_quality_score": 20, "4B_watch_score": 45}, "weighted_score_before": 76, "stage_label_before": "Stage2-Actionable", "raw_component_scores_after": {"volume_or_shipment_score": 50, "utilization_score": 45, "yield_or_ASP_score": 35, "raw_material_cost_spread_score": 45, "margin_bridge_score": 40, "customer_or_channel_quality_score": 35, "revision_score": 40, "relative_strength_score": 55, "valuation_blowoff_risk_score": 60, "execution_risk_score": 75, "source_quality_score": 10, "4B_watch_score": 80}, "weighted_score_after": 73, "stage_label_after": "Stage2-Actionable + high-MAE/local 4B watch", "changed_components": ["volume_or_shipment_score", "utilization_score", "yield_or_ASP_score", "raw_material_cost_spread_score", "margin_bridge_score", "source_quality_score", "execution_risk_score", "4B_watch_score"], "component_delta_explanation": "C29 requires mobility/tire/auto-parts volume recovery to convert into utilization, ASP or raw-material spread, and margin bridge before clean Stage2/Green; mobility theme MFE alone is demoted or wrapped with local 4B/high-MAE watch.", "MFE_90D_pct": 16.61, "MAE_90D_pct": -5.42, "score_return_alignment_label": "positive_MFE_but_high_MAE_RiskWatch", "current_profile_verdict": "current_profile_4B_too_late_high_MAE"}
{"row_type": "case", "case_id": "R9L84-C29-02", "symbol": "002350", "company_name": "넥센타이어", "round": "R9", "loop": 84, "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE", "fine_archetype_id": "TIRE_EXPORT_VOLUME_RAWMATERIAL_COST_MARGIN_AUTO_PARTS_UTILIZATION_BRIDGE_VS_VEHICLE_THEME_FADE", "case_type": "tire_volume_margin_positive_with_later_fade", "positive_or_counterexample": "positive", "best_trigger": "R9L84-C29-02-S2A-20240202", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "bounded_positive_MFE_but_local_4B_watch_needed", "current_profile_verdict": "current_profile_partially_correct_local_4B_watch_needed", "price_source": "Songdaiki/stock-web", "notes": "Tire margin-cycle positives need volume, mix, cost spread and plant utilization bridge; short MFE alone should not become clean Green."}
{"row_type": "trigger", "trigger_id": "R9L84-C29-02-S2A-20240202", "case_id": "R9L84-C29-02", "symbol": "002350", "company_name": "넥센타이어", "round": "R9", "loop": 84, "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE", "fine_archetype_id": "TIRE_EXPORT_VOLUME_RAWMATERIAL_COST_MARGIN_AUTO_PARTS_UTILIZATION_BRIDGE_VS_VEHICLE_THEME_FADE", "loop_objective": "coverage_gap_fill|counterexample_mining|mobility_volume_margin_operating_leverage_guardrail|local_4B_timing_after_mobility_MFE|canonical_archetype_compression", "trigger_type": "Stage2-Actionable", "trigger_date": "2024-02-02", "evidence_available_at_that_date": "tire export/OE-replacement mix and cost-spread margin recovery proxy; primary channel and margin evidence pending", "evidence_source": "source_proxy_only; evidence_url_pending", "stage2_evidence_fields": ["volume_or_shipment_proxy", "utilization_proxy", "ASP_or_cost_spread_proxy"], "stage3_evidence_fields": ["confirmed_volume_growth", "yield_or_ASP", "raw_material_cost_spread", "plant_utilization", "gross_or_OP_margin_conversion"], "stage4b_evidence_fields": ["mobility_MFE_without_margin_bridge", "valuation_overheat", "post_peak_drawdown"], "stage4c_evidence_fields": ["hard_volume_or_utilization_break_watch_only"], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/002/002350/2024.csv", "profile_path": "atlas/symbol_profiles/002/002350.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "entry_date": "2024-02-02", "entry_price": 8230, "MFE_30D_pct": 17.25, "MFE_90D_pct": 17.25, "MFE_180D_pct": 17.25, "MFE_1Y_pct": null, "MFE_2Y_pct": null, "MAE_30D_pct": -1.58, "MAE_90D_pct": -6.93, "MAE_180D_pct": -17.98, "MAE_1Y_pct": null, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2024-02-26", "peak_price": 9650, "drawdown_after_peak_pct": -30.05, "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": 0.82, "four_b_full_window_peak_proximity": 0.72, "four_b_timing_verdict": "local_4B_watch_after_tire_margin_MFE_if_volume_cost_bridge_stalls", "four_b_evidence_type": ["mobility_MFE_without_margin_bridge", "post_peak_drawdown", "source_proxy_gap"], "four_c_protection_label": "hard_4C_requires_non_price_volume_or_utilization_break", "trigger_outcome_label": "bounded_positive_MFE_but_local_4B_watch_needed", "current_profile_verdict": "current_profile_partially_correct_local_4B_watch_needed", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window_after_old_2008_CA_candidates", "same_entry_group_id": "R9L84-C29-02", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R9L84-C29-02", "trigger_id": "R9L84-C29-02-S2A-20240202", "symbol": "002350", "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE", "raw_component_scores_before": {"volume_or_shipment_score": 50, "utilization_score": 45, "yield_or_ASP_score": 35, "raw_material_cost_spread_score": 45, "margin_bridge_score": 40, "customer_or_channel_quality_score": 35, "revision_score": 40, "relative_strength_score": 55, "valuation_blowoff_risk_score": 60, "execution_risk_score": 45, "source_quality_score": 20, "4B_watch_score": 45}, "weighted_score_before": 76, "stage_label_before": "Stage2-Actionable", "raw_component_scores_after": {"volume_or_shipment_score": 50, "utilization_score": 45, "yield_or_ASP_score": 35, "raw_material_cost_spread_score": 45, "margin_bridge_score": 40, "customer_or_channel_quality_score": 35, "revision_score": 40, "relative_strength_score": 55, "valuation_blowoff_risk_score": 60, "execution_risk_score": 45, "source_quality_score": 10, "4B_watch_score": 80}, "weighted_score_after": 74, "stage_label_after": "Stage2-Actionable + local 4B watch", "changed_components": ["volume_or_shipment_score", "utilization_score", "yield_or_ASP_score", "raw_material_cost_spread_score", "margin_bridge_score", "source_quality_score", "execution_risk_score", "4B_watch_score"], "component_delta_explanation": "C29 requires mobility/tire/auto-parts volume recovery to convert into utilization, ASP or raw-material spread, and margin bridge before clean Stage2/Green; mobility theme MFE alone is demoted or wrapped with local 4B/high-MAE watch.", "MFE_90D_pct": 17.25, "MAE_90D_pct": -6.93, "score_return_alignment_label": "bounded_positive_MFE_but_local_4B_watch_needed", "current_profile_verdict": "current_profile_partially_correct_local_4B_watch_needed"}
{"row_type": "case", "case_id": "R9L84-C29-03", "symbol": "011210", "company_name": "현대위아", "round": "R9", "loop": 84, "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE", "fine_archetype_id": "TIRE_EXPORT_VOLUME_RAWMATERIAL_COST_MARGIN_AUTO_PARTS_UTILIZATION_BRIDGE_VS_VEHICLE_THEME_FADE", "case_type": "auto_parts_powertrain_utilization_theme_false_positive", "positive_or_counterexample": "counterexample", "best_trigger": "R9L84-C29-03-S2FP-20240202", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "low_MFE_high_MAE_auto_parts_false_positive", "current_profile_verdict": "current_profile_false_positive_high_MAE", "price_source": "Songdaiki/stock-web", "notes": "Auto-parts volume or mobility theme should be rejected unless platform/order mix, utilization, cost pass-through and margin conversion are visible at entry."}
{"row_type": "trigger", "trigger_id": "R9L84-C29-03-S2FP-20240202", "case_id": "R9L84-C29-03", "symbol": "011210", "company_name": "현대위아", "round": "R9", "loop": 84, "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE", "fine_archetype_id": "TIRE_EXPORT_VOLUME_RAWMATERIAL_COST_MARGIN_AUTO_PARTS_UTILIZATION_BRIDGE_VS_VEHICLE_THEME_FADE", "loop_objective": "coverage_gap_fill|counterexample_mining|mobility_volume_margin_operating_leverage_guardrail|local_4B_timing_after_mobility_MFE|canonical_archetype_compression", "trigger_type": "Stage2-FalsePositive", "trigger_date": "2024-02-02", "evidence_available_at_that_date": "auto-parts / powertrain / mobility utilization theme proxy without confirmed order mix, utilization and margin bridge", "evidence_source": "source_proxy_only; evidence_url_pending", "stage2_evidence_fields": ["volume_or_shipment_proxy", "utilization_proxy", "ASP_or_cost_spread_proxy"], "stage3_evidence_fields": ["confirmed_volume_growth", "yield_or_ASP", "raw_material_cost_spread", "plant_utilization", "gross_or_OP_margin_conversion"], "stage4b_evidence_fields": ["mobility_MFE_without_margin_bridge", "valuation_overheat", "post_peak_drawdown"], "stage4c_evidence_fields": ["hard_volume_or_utilization_break_watch_only"], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/011/011210/2024.csv", "profile_path": "atlas/symbol_profiles/011/011210.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "entry_date": "2024-02-02", "entry_price": 64500, "MFE_30D_pct": 3.88, "MFE_90D_pct": 3.88, "MFE_180D_pct": 3.88, "MFE_1Y_pct": null, "MFE_2Y_pct": null, "MAE_30D_pct": -12.4, "MAE_90D_pct": -13.49, "MAE_180D_pct": -29.53, "MAE_1Y_pct": null, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2024-02-05", "peak_price": 67000, "drawdown_after_peak_pct": -32.16, "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": 0.3, "four_b_full_window_peak_proximity": 0.25, "four_b_timing_verdict": "auto_parts_theme_rejected_without_order_mix_utilization_margin_bridge", "four_b_evidence_type": ["mobility_MFE_without_margin_bridge", "post_peak_drawdown", "source_proxy_gap"], "four_c_protection_label": "hard_4C_requires_non_price_volume_or_utilization_break", "trigger_outcome_label": "low_MFE_high_MAE_auto_parts_false_positive", "current_profile_verdict": "current_profile_false_positive_high_MAE", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window_no_profile_CA_candidate", "same_entry_group_id": "R9L84-C29-03", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R9L84-C29-03", "trigger_id": "R9L84-C29-03-S2FP-20240202", "symbol": "011210", "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE", "raw_component_scores_before": {"volume_or_shipment_score": 25, "utilization_score": 15, "yield_or_ASP_score": 10, "raw_material_cost_spread_score": 5, "margin_bridge_score": 5, "customer_or_channel_quality_score": 20, "revision_score": 15, "relative_strength_score": 25, "valuation_blowoff_risk_score": 55, "execution_risk_score": 80, "source_quality_score": 15, "4B_watch_score": 70}, "weighted_score_before": 58, "stage_label_before": "Stage2-Watch/FalsePositive", "raw_component_scores_after": {"volume_or_shipment_score": 10, "utilization_score": 0, "yield_or_ASP_score": 0, "raw_material_cost_spread_score": 0, "margin_bridge_score": 0, "customer_or_channel_quality_score": 20, "revision_score": 15, "relative_strength_score": 25, "valuation_blowoff_risk_score": 55, "execution_risk_score": 90, "source_quality_score": 5, "4B_watch_score": 80}, "weighted_score_after": 46, "stage_label_after": "Rejected-Stage2 / RiskWatch", "changed_components": ["volume_or_shipment_score", "utilization_score", "yield_or_ASP_score", "raw_material_cost_spread_score", "margin_bridge_score", "source_quality_score", "execution_risk_score", "4B_watch_score"], "component_delta_explanation": "C29 requires mobility/tire/auto-parts volume recovery to convert into utilization, ASP or raw-material spread, and margin bridge before clean Stage2/Green; mobility theme MFE alone is demoted or wrapped with local 4B/high-MAE watch.", "MFE_90D_pct": 3.88, "MAE_90D_pct": -13.49, "score_return_alignment_label": "low_MFE_high_MAE_auto_parts_false_positive", "current_profile_verdict": "current_profile_false_positive_high_MAE"}
{"row_type": "shadow_weight", "axis": "C29_mobility_volume_utilization_cost_spread_margin_bridge_required", "scope": "canonical_archetype_specific", "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE", "baseline_value": 0, "tested_value": 1, "delta": "+1", "reason": "Mobility/tire/auto-parts rerating requires shipment volume, utilization, ASP or raw-material spread, and margin bridge; vehicle/mobility theme MFE without bridge fades into high MAE or needs local 4B watch.", "backtest_effect": "keeps 073240/002350 with local 4B or high-MAE RiskWatch; demotes 011210 auto-parts theme false positive", "trigger_ids": "R9L84-C29-01-S2A-20240125|R9L84-C29-02-S2A-20240202|R9L84-C29-03-S2FP-20240202", "calibration_usable_count": 3, "new_independent_case_count": 3, "counterexample_count": 1, "confidence": "low", "proposal_type": "canonical_shadow_only", "notes": "source_proxy_only/evidence_url_pending; not production"}
{"row_type": "residual_contribution", "round": "R9", "loop": 84, "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE", "new_independent_case_count": 3, "reused_case_count": 0, "new_symbol_count": 3, "new_trigger_family_count": 3, "tested_existing_calibrated_axes": ["stage2_actionable_evidence_bonus", "price_only_blowoff_blocks_positive_stage", "full_4b_requires_non_price_evidence", "hard_4c_thesis_break_routes_to_4c", "source_proxy_only_blocks_runtime_promotion", "high_MAE_guardrail"], "residual_error_types_found": ["mobility_volume_theme_false_positive_high_MAE", "tire_export_volume_cost_spread_margin_bridge_required", "local_4B_late_after_mobility_MFE", "source_proxy_runtime_promotion_risk", "high_MAE_positive_Green_blocker"], "loop_contribution_label": "canonical_archetype_rule_candidate", "do_not_propose_new_weight_delta": true}
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
- For C29, test a canonical-archetype guard requiring shipment volume, utilization, ASP/raw-material spread and margin conversion before clean Stage2/Green.

## 27. Next Round State

```text
completed_round = R9
completed_loop = 84
next_round = R10
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
