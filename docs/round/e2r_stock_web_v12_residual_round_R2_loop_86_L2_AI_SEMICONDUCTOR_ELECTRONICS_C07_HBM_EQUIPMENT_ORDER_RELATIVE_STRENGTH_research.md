# E2R Stock-Web v12 Residual Research — R2 Loop 86 / L2 / C07

## 0. Research Metadata

```json
{
  "research_session": "post_calibrated_sector_archetype_residual_research",
  "mode": "historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12",
  "scheduled_round": "R2",
  "scheduled_loop": 86,
  "round_schedule_status": "valid",
  "round_sector_consistency": "pass",
  "completed_round": "R2",
  "completed_loop": 86,
  "computed_next_round": "R3",
  "computed_next_loop": 86,
  "large_sector_id": "L2_AI_SEMICONDUCTOR_ELECTRONICS",
  "canonical_archetype_id": "C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH",
  "fine_archetype_id": "OVERLAY_METROLOGY_ETCH_EQUIPMENT_SIC_PARTS_RELATIVE_STRENGTH_ORDER_ACCEPTANCE_REVENUE_BRIDGE_VS_EQUIPMENT_THEME_BLOWOFF_FADE",
  "loop_objective": [
    "coverage_gap_fill",
    "counterexample_mining",
    "HBM_equipment_order_relative_strength_guardrail",
    "equipment_relative_strength_to_named_order_acceptance_revenue_bridge_test",
    "customer_quality_to_delivery_utilization_margin_bridge_test",
    "local_4B_timing_after_equipment_MFE",
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
scheduled_round = R2
scheduled_loop = 86
allowed_large_sector = L2_AI_SEMICONDUCTOR_ELECTRONICS
selected_large_sector = L2_AI_SEMICONDUCTOR_ELECTRONICS
selected_canonical_archetype_id = C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH
computed_next_round = R3
computed_next_loop = 86
round_schedule_status = valid
round_sector_consistency = pass
```

R2 continues loop86 after R1/C04. This run selects C07 because loop85 R2 used C08, loop84 R2 used C09, and loop83 R2 used C10. The selected route is not the heavily covered HBM ticker basket; it tests equipment/parts relative strength outside the top-covered C07 symbols.

The tested mechanism:

```text
HBM / advanced equipment / parts relative-strength headline
→ named customer order or acceptance
→ qualification and delivery backlog
→ utilization
→ revenue and gross/OP margin bridge
→ durable rerating or equipment-theme fade
```

C07 is the purchase-order gate. Relative strength can point to attention, but the model should not call it clean Stage2/Green until customer order, acceptance and revenue bridge are visible.

## 3. Previous Coverage / Duplicate Avoidance Check

No-Repeat is used only as a duplicate ledger.

```text
hard_duplicate_key = canonical_archetype_id + symbol + trigger_type + entry_date
```

C07 top-covered symbols include `UNKNOWN_SYMBOL`, `232140`, `031980`, `042700`, `003160`, and `089030`. This run avoids that top-covered set and uses:

```text
064760 / 티씨케이
322310 / 오로스테크놀로지
089970 / 브이엠
```

All three are treated as new independent C07 HBM/equipment relative-strength cases for this loop. No hard duplicate is intentionally reused.

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
| 064760 | 티씨케이 | `atlas/symbol_profiles/064/064760.json` | no profile-level CA candidate |
| 322310 | 오로스테크놀로지 | `atlas/symbol_profiles/322/322310.json` | no profile-level CA candidate |
| 089970 | 브이엠 | `atlas/symbol_profiles/089/089970.json` | no profile-level CA candidate; renamed from 에이피티씨 in 2024 |

## 5. Historical Eligibility Gate

| case_id | symbol | entry_date | entry_price | forward window | 180D status | calibration_usable |
|---|---:|---|---:|---:|---|---|
| R2L86-C07-01 | 064760 | 2024-02-13 | 97,200 | 180D | clean | true |
| R2L86-C07-02 | 322310 | 2024-02-13 | 31,200 | 180D | clean | true |
| R2L86-C07-03 | 089970 | 2024-02-13 | 13,110 | 180D | clean | true |

## 6. Canonical Archetype Compression Map

| canonical_archetype_id | fine/deep route | keep / reject logic |
|---|---|---|
| C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH | SIC_PARTS_CUSTOMER_QUALITY_ORDER_ACCEPTANCE | keep Stage2 only with named customer/order acceptance, utilization and margin bridge |
| C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH | OVERLAY_METROLOGY_EQUIPMENT_THEME_BLOWOFF | reject early MFE when customer/order/revenue bridge is absent and MAE later widens |
| C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH | ETCH_EQUIPMENT_RELATIVE_STRENGTH_FADE | reject equipment-cycle MFE without shipment, order and margin bridge |

## 7. Case Selection Summary

| case_id | symbol | company | trigger_type | entry_date | entry_price | MFE_180D_pct | MAE_180D_pct | current_profile_verdict |
|---|---:|---|---|---|---:|---:|---:|---|
| R2L86-C07-01 | 064760 | 티씨케이 | Stage2-Actionable | 2024-02-13 | 97,200 | 54.22 | -13.58 | current_profile_partially_correct_local_4B_watch_needed |
| R2L86-C07-02 | 322310 | 오로스테크놀로지 | Stage2-FalsePositive | 2024-02-13 | 31,200 | 30.61 | -51.51 | current_profile_false_positive_high_MAE_4B_too_late |
| R2L86-C07-03 | 089970 | 브이엠 | Stage2-FalsePositive | 2024-02-13 | 13,110 | 34.94 | -36.69 | current_profile_false_positive_high_MAE |

## 8. Positive vs Counterexample Balance

```text
positive_case_count = 1
counterexample_count = 2
4B_or_4C_case_count = 3
calibration_usable_case_count = 3
new_independent_case_count = 3
```

## 9. Evidence Source Map

All selected evidence is currently `source_proxy_only=true / evidence_url_pending=true`.

This MD creates a source-repair queue and a C07 shadow guardrail candidate. It must not be promoted directly into runtime weights until a later source-repair pass attaches primary evidence URLs: named customer order, equipment acceptance, parts qualification, delivery backlog, utilization, revenue conversion, gross/OP margin bridge, company disclosure or report evidence.

## 10. Price Data Source Map

| symbol | shard path | profile path |
|---|---|---|
| 064760 | `atlas/ohlcv_tradable_by_symbol_year/064/064760/2024.csv` | `atlas/symbol_profiles/064/064760.json` |
| 322310 | `atlas/ohlcv_tradable_by_symbol_year/322/322310/2024.csv` | `atlas/symbol_profiles/322/322310.json` |
| 089970 | `atlas/ohlcv_tradable_by_symbol_year/089/089970/2024.csv` | `atlas/symbol_profiles/089/089970.json` |

## 11. Case-by-Case Trigger Grid

### Case 1 — 064760 / 티씨케이

C07 SiC parts/customer-quality positive with local 4B watch. The entry path produced a clean MFE into June, but the later peak-to-trough drawdown shows that relative strength alone is not clean Green. Customer order, qualification, utilization and margin bridge need source repair.

### Case 2 — 322310 / 오로스테크놀로지

C07 overlay-metrology equipment theme false positive. The early MFE was large, but it later collapsed into deep MAE. This is the cleanest C07 lesson: equipment theme MFE without customer/order acceptance should be rejected or local-4B-watched.

### Case 3 — 089970 / 브이엠

C07 etch-equipment relative-strength theme fade. The path had a March/July MFE, but it later fell sharply. Equipment-cycle language without named order and revenue/margin bridge should not validate Stage2.

## 12. Trigger-Level OHLC Backtest Tables

| symbol | entry | MFE30 | MAE30 | MFE90 | MAE90 | MFE180 | MAE180 | peak | post-peak DD |
|---|---:|---:|---:|---:|---:|---:|---:|---|---:|
| 064760 | 97,200 | 9.57 | -4.22 | 45.16 | -4.22 | 54.22 | -13.58 | 2024-06-14 / 149,900 | -43.96 |
| 322310 | 31,200 | 30.61 | -6.09 | 30.61 | -6.09 | 30.61 | -51.51 | 2024-02-27 / 40,750 | -62.87 |
| 089970 | 13,110 | 29.67 | -4.96 | 29.67 | -4.96 | 34.94 | -36.69 | 2024-07-01 / 17,690 | -53.08 |

## 13. Current Calibrated Profile Stress Test

| case_id | P0 likely behavior | actual path | verdict |
|---|---|---|---|
| R2L86-C07-01 | Stage2-Actionable if customer/order bridge exists | strong MFE, later drawdown | partially correct; local 4B/order-acceptance watch needed |
| R2L86-C07-02 | risk of treating metrology theme MFE as Stage2 | early MFE then deep MAE | false positive / high-MAE guardrail |
| R2L86-C07-03 | risk of treating etch-equipment cycle MFE as Stage2 | MFE then large MAE | false positive / theme fade |

## 14. Stage2 / Yellow / Green Comparison

```text
green_lateness_ratio = not_applicable
reason = no confirmed Stage3-Green trigger is assigned in this residual MD
```

For C07, the residual is whether equipment relative strength becomes clean Stage2/Green before named customer order, acceptance, delivery and margin bridge are proven.

## 15. 4B Local vs Full-window Timing Audit

| case_id | local proximity | full-window proximity | verdict |
|---|---:|---:|---|
| R2L86-C07-01 | 0.82 | 0.72 | local 4B watch after SiC parts MFE if order/utilization/margin bridge stalls |
| R2L86-C07-02 | 0.35 | 0.30 | overlay-metrology MFE rejected without order/acceptance/revenue bridge |
| R2L86-C07-03 | 0.35 | 0.30 | etch-equipment MFE rejected without customer order/delivery/revenue bridge |

## 16. 4C Protection Audit

No hard 4C is promoted from this file.

```text
four_c_protection_label = hard_4C_requires_non_price_order_loss_or_customer_acceptance_break
hard_4c_price_only_allowed = false
```

Price drawdown alone is not hard 4C. C07 hard 4C requires confirmed order loss, customer acceptance failure, qualification loss, delivery cancellation, capex pullback, or margin thesis break.

## 17. Sector-Specific Rule Candidate

```text
rule_scope = no_new_global_rule
sector_specific_rule_candidate = L2/C07 equipment rows need named customer order, qualification/acceptance, delivery backlog, utilization and revenue/margin bridge before clean Stage2/Green
confidence = low
reason = all evidence rows are source_proxy_only / evidence_url_pending
```

## 18. Canonical-Archetype Rule Candidate

```text
canonical_archetype_id = C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH
candidate_axis = C07_equipment_relative_strength_customer_order_acceptance_revenue_margin_bridge_required
effect = keep SiC parts/customer-quality positive with local 4B watch; demote equipment-theme false positives
production_scoring_changed = false
shadow_weight_only = true
do_not_propose_new_weight_delta = true
```

## 19. Before / After Backtest Comparison

| profile | eligible triggers | avg MFE90 | avg MAE90 | false-positive behavior | verdict |
|---|---:|---:|---:|---|---|
| P0 e2r_2_1_stock_web_calibrated_proxy | 3 | 35.15 | -5.09 | may over-credit equipment relative-strength theme MFE | needs C07 order/acceptance bridge repair |
| P1 canonical shadow bridge profile | 3 | 45.16 on kept positive | demotes 322310/089970 | blocks clean Green until source repair | better alignment, source repair required |

## 20. Score-Return Alignment Matrix

| case_id | weighted before | label before | weighted after | label after | alignment |
|---|---:|---|---:|---|---|
| R2L86-C07-01 | 78 | Stage2-Actionable | 74 | Stage2-Actionable + local 4B/order-acceptance watch | partially aligned |
| R2L86-C07-02 | 58 | Stage2-Watch/FalsePositive | 44 | Rejected-Stage2 / Equipment-theme RiskWatch | improved |
| R2L86-C07-03 | 58 | Stage2-Watch/FalsePositive | 44 | Rejected-Stage2 / Equipment-theme RiskWatch | improved |

## 21. Coverage Matrix

| large_sector_id | canonical_archetype_id | fine_archetype_id | positive | counterexample | 4B | 4C | new cases | reused | usable triggers | current errors | sector rule | canonical rule | coverage gap after |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---|---|---|
| L2_AI_SEMICONDUCTOR_ELECTRONICS | C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH | OVERLAY_METROLOGY_ETCH_EQUIPMENT_SIC_PARTS_RELATIVE_STRENGTH_ORDER_ACCEPTANCE_REVENUE_BRIDGE_VS_EQUIPMENT_THEME_BLOWOFF_FADE | 1 | 2 | 3-watch | 0-hard | 3 | 0 | 3 | 2 | no | yes | source repair needed |

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
  - semi_equipment_theme_false_positive_high_MAE
  - customer_order_acceptance_revenue_margin_bridge_required
  - local_4B_late_after_equipment_MFE
  - source_proxy_runtime_promotion_risk
  - high_MAE_positive_Green_blocker
new_axis_proposed: false
existing_axis_strengthened:
  - C07_equipment_relative_strength_customer_order_acceptance_revenue_margin_bridge_required
  - source_proxy_only_blocks_runtime_promotion
  - local_4B_watch_before_full_4B_when_MFE_outruns_bridge
  - high_MAE_blocks_clean_Green
existing_axis_weakened: null
existing_axis_kept:
  - full_4b_requires_non_price_evidence
  - hard_4c_thesis_break_routes_to_4c
sector_specific_rule_candidate: null
canonical_archetype_rule_candidate: C07_equipment_relative_strength_customer_order_acceptance_revenue_margin_bridge_required
no_new_signal_reason: null
loop_contribution_label: canonical_archetype_rule_candidate
do_not_propose_new_weight_delta: true
```

This loop adds 3 new independent cases, 2 counterexamples, and 2 residual errors for R2/L2_AI_SEMICONDUCTOR_ELECTRONICS/C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH.

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
- named customer order
- qualification / acceptance
- delivery backlog and utilization
- revenue and gross/OP margin conversion
- production scoring implementation
```

## 24. Shadow Weight Calibration

```csv
row_type,axis,scope,large_sector_id,canonical_archetype_id,baseline_value,tested_value,delta,reason,backtest_effect,trigger_ids,calibration_usable_count,new_independent_case_count,counterexample_count,confidence,proposal_type,notes
shadow_weight,C07_equipment_relative_strength_customer_order_acceptance_revenue_margin_bridge_required,canonical_archetype_specific,L2_AI_SEMICONDUCTOR_ELECTRONICS,C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH,0,1,+1,"Require named customer order, qualification/acceptance, delivery backlog, utilization and revenue/margin bridge before clean Stage2/Green","keeps 064760 with local 4B/order-acceptance watch; demotes 322310/089970","R2L86-C07-01-S2A-20240213|R2L86-C07-02-S2FP-20240213|R2L86-C07-03-S2FP-20240213",3,3,2,low,canonical_shadow_only,"source repair required; not production"
```

## 25. Machine-Readable Rows

```jsonl
{"row_type": "price_source_validation", "source": "Songdaiki/stock-web", "source_url": "https://github.com/Songdaiki/stock-web", "manifest_path": "atlas/manifest.json", "schema_path": "atlas/schema.json", "universe_path": "atlas/universe/all_symbols.csv", "manifest_max_date": "2026-02-20", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "raw_shard_root": "atlas/ohlcv_raw_by_symbol_year", "validation_status": "usable_for_historical_calibration"}
{"row_type": "case", "case_id": "R2L86-C07-01", "symbol": "064760", "company_name": "티씨케이", "round": "R2", "loop": 86, "large_sector_id": "L2_AI_SEMICONDUCTOR_ELECTRONICS", "canonical_archetype_id": "C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH", "fine_archetype_id": "OVERLAY_METROLOGY_ETCH_EQUIPMENT_SIC_PARTS_RELATIVE_STRENGTH_ORDER_ACCEPTANCE_REVENUE_BRIDGE_VS_EQUIPMENT_THEME_BLOWOFF_FADE", "case_type": "SiC_parts_customer_quality_relative_strength_positive_with_local_4B_watch", "positive_or_counterexample": "positive", "best_trigger": "R2L86-C07-01-S2A-20240213", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "large_positive_MFE_but_local_4B_and_customer_order_margin_bridge_required", "current_profile_verdict": "current_profile_partially_correct_local_4B_watch_needed", "price_source": "Songdaiki/stock-web", "notes": "C07 can keep Stage2 only when relative strength converts into named customer order, delivery/utilization, qualification and gross/OP margin bridge."}
{"row_type": "trigger", "trigger_id": "R2L86-C07-01-S2A-20240213", "case_id": "R2L86-C07-01", "symbol": "064760", "company_name": "티씨케이", "round": "R2", "loop": 86, "large_sector_id": "L2_AI_SEMICONDUCTOR_ELECTRONICS", "canonical_archetype_id": "C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH", "fine_archetype_id": "OVERLAY_METROLOGY_ETCH_EQUIPMENT_SIC_PARTS_RELATIVE_STRENGTH_ORDER_ACCEPTANCE_REVENUE_BRIDGE_VS_EQUIPMENT_THEME_BLOWOFF_FADE", "loop_objective": "coverage_gap_fill|counterexample_mining|HBM_equipment_order_relative_strength_guardrail|order_acceptance_revenue_margin_bridge|canonical_archetype_compression", "trigger_type": "Stage2-Actionable", "trigger_date": "2024-02-13", "evidence_available_at_that_date": "HBM/advanced memory equipment-chain, SiC ring/parts customer quality and capacity recovery proxy; primary customer order and margin evidence pending", "evidence_source": "source_proxy_only; evidence_url_pending", "stage2_evidence_fields": ["relative_strength_proxy", "customer_quality_proxy", "equipment_or_parts_order_proxy"], "stage3_evidence_fields": ["named_customer_order", "qualification_acceptance", "delivery_backlog", "utilization", "revenue_margin_conversion"], "stage4b_evidence_fields": ["equipment_MFE_without_order_bridge", "valuation_blowoff", "post_peak_drawdown"], "stage4c_evidence_fields": ["hard_order_loss_or_customer_acceptance_break_watch_only"], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/064/064760/2024.csv", "profile_path": "atlas/symbol_profiles/064/064760.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "entry_date": "2024-02-13", "entry_price": 97200, "MFE_30D_pct": 9.57, "MFE_90D_pct": 45.16, "MFE_180D_pct": 54.22, "MFE_1Y_pct": null, "MFE_2Y_pct": null, "MAE_30D_pct": -4.22, "MAE_90D_pct": -4.22, "MAE_180D_pct": -13.58, "MAE_1Y_pct": null, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2024-06-14", "peak_price": 149900, "drawdown_after_peak_pct": -43.96, "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": 0.82, "four_b_full_window_peak_proximity": 0.72, "four_b_timing_verdict": "local_4B_watch_after_SiC_parts_MFE_if_named_customer_order_utilization_margin_bridge_stalls", "four_b_evidence_type": ["equipment_MFE_without_order_bridge", "post_peak_drawdown", "source_proxy_gap"], "four_c_protection_label": "hard_4C_requires_non_price_order_loss_or_customer_acceptance_break", "trigger_outcome_label": "large_positive_MFE_but_local_4B_and_customer_order_margin_bridge_required", "current_profile_verdict": "current_profile_partially_correct_local_4B_watch_needed", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_2024_window_no_profile_CA_candidate", "same_entry_group_id": "R2L86-C07-01", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R2L86-C07-01", "trigger_id": "R2L86-C07-01-S2A-20240213", "symbol": "064760", "large_sector_id": "L2_AI_SEMICONDUCTOR_ELECTRONICS", "canonical_archetype_id": "C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH", "raw_component_scores_before": {"relative_strength_score": 65, "customer_quality_score": 55, "named_order_score": 40, "delivery_backlog_score": 40, "qualification_acceptance_score": 45, "utilization_score": 40, "revenue_bridge_score": 40, "gross_margin_bridge_score": 40, "valuation_blowoff_risk_score": 60, "execution_risk_score": 55, "source_quality_score": 20, "4B_watch_score": 45}, "weighted_score_before": 78, "stage_label_before": "Stage2-Actionable", "raw_component_scores_after": {"relative_strength_score": 65, "customer_quality_score": 55, "named_order_score": 40, "delivery_backlog_score": 40, "qualification_acceptance_score": 45, "utilization_score": 40, "revenue_bridge_score": 40, "gross_margin_bridge_score": 40, "valuation_blowoff_risk_score": 75, "execution_risk_score": 55, "source_quality_score": 10, "4B_watch_score": 80}, "weighted_score_after": 74, "stage_label_after": "Stage2-Actionable + local 4B/order-acceptance watch", "changed_components": ["customer_quality_score", "named_order_score", "delivery_backlog_score", "qualification_acceptance_score", "revenue_bridge_score", "gross_margin_bridge_score", "source_quality_score", "4B_watch_score"], "component_delta_explanation": "C07 requires equipment/parts relative strength to convert into named customer order, qualification/acceptance, delivery backlog, utilization and revenue/margin bridge before clean Stage2/Green; equipment-theme MFE alone is demoted or wrapped with local 4B/high-MAE watch.", "MFE_90D_pct": 45.16, "MAE_90D_pct": -4.22, "score_return_alignment_label": "large_positive_MFE_but_local_4B_and_customer_order_margin_bridge_required", "current_profile_verdict": "current_profile_partially_correct_local_4B_watch_needed"}
{"row_type": "case", "case_id": "R2L86-C07-02", "symbol": "322310", "company_name": "오로스테크놀로지", "round": "R2", "loop": 86, "large_sector_id": "L2_AI_SEMICONDUCTOR_ELECTRONICS", "canonical_archetype_id": "C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH", "fine_archetype_id": "OVERLAY_METROLOGY_ETCH_EQUIPMENT_SIC_PARTS_RELATIVE_STRENGTH_ORDER_ACCEPTANCE_REVENUE_BRIDGE_VS_EQUIPMENT_THEME_BLOWOFF_FADE", "case_type": "overlay_metrology_equipment_theme_blowoff_false_positive", "positive_or_counterexample": "counterexample", "best_trigger": "R2L86-C07-02-S2FP-20240213", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "early_equipment_MFE_then_deep_MAE_false_positive", "current_profile_verdict": "current_profile_false_positive_high_MAE_4B_too_late", "price_source": "Songdaiki/stock-web", "notes": "Metrology/equipment relative-strength MFE is not durable C07 evidence unless customer acceptance, order backlog, delivery and margin bridge are source-repaired."}
{"row_type": "trigger", "trigger_id": "R2L86-C07-02-S2FP-20240213", "case_id": "R2L86-C07-02", "symbol": "322310", "company_name": "오로스테크놀로지", "round": "R2", "loop": 86, "large_sector_id": "L2_AI_SEMICONDUCTOR_ELECTRONICS", "canonical_archetype_id": "C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH", "fine_archetype_id": "OVERLAY_METROLOGY_ETCH_EQUIPMENT_SIC_PARTS_RELATIVE_STRENGTH_ORDER_ACCEPTANCE_REVENUE_BRIDGE_VS_EQUIPMENT_THEME_BLOWOFF_FADE", "loop_objective": "coverage_gap_fill|counterexample_mining|HBM_equipment_order_relative_strength_guardrail|order_acceptance_revenue_margin_bridge|canonical_archetype_compression", "trigger_type": "Stage2-FalsePositive", "trigger_date": "2024-02-13", "evidence_available_at_that_date": "overlay metrology / HBM advanced equipment relative-strength theme proxy without confirmed named order, acceptance and revenue bridge", "evidence_source": "source_proxy_only; evidence_url_pending", "stage2_evidence_fields": ["relative_strength_proxy", "customer_quality_proxy", "equipment_or_parts_order_proxy"], "stage3_evidence_fields": ["named_customer_order", "qualification_acceptance", "delivery_backlog", "utilization", "revenue_margin_conversion"], "stage4b_evidence_fields": ["equipment_MFE_without_order_bridge", "valuation_blowoff", "post_peak_drawdown"], "stage4c_evidence_fields": ["hard_order_loss_or_customer_acceptance_break_watch_only"], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/322/322310/2024.csv", "profile_path": "atlas/symbol_profiles/322/322310.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "entry_date": "2024-02-13", "entry_price": 31200, "MFE_30D_pct": 30.61, "MFE_90D_pct": 30.61, "MFE_180D_pct": 30.61, "MFE_1Y_pct": null, "MFE_2Y_pct": null, "MAE_30D_pct": -6.09, "MAE_90D_pct": -6.09, "MAE_180D_pct": -51.51, "MAE_1Y_pct": null, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2024-02-27", "peak_price": 40750, "drawdown_after_peak_pct": -62.87, "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": 0.35, "four_b_full_window_peak_proximity": 0.3, "four_b_timing_verdict": "overlay_metrology_MFE_rejected_without_named_order_acceptance_revenue_margin_bridge", "four_b_evidence_type": ["equipment_MFE_without_order_bridge", "post_peak_drawdown", "source_proxy_gap"], "four_c_protection_label": "hard_4C_requires_non_price_order_loss_or_customer_acceptance_break", "trigger_outcome_label": "early_equipment_MFE_then_deep_MAE_false_positive", "current_profile_verdict": "current_profile_false_positive_high_MAE_4B_too_late", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_2024_window_no_profile_CA_candidate", "same_entry_group_id": "R2L86-C07-02", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R2L86-C07-02", "trigger_id": "R2L86-C07-02-S2FP-20240213", "symbol": "322310", "large_sector_id": "L2_AI_SEMICONDUCTOR_ELECTRONICS", "canonical_archetype_id": "C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH", "raw_component_scores_before": {"relative_strength_score": 55, "customer_quality_score": 20, "named_order_score": 5, "delivery_backlog_score": 10, "qualification_acceptance_score": 10, "utilization_score": 15, "revenue_bridge_score": 5, "gross_margin_bridge_score": 5, "valuation_blowoff_risk_score": 75, "execution_risk_score": 80, "source_quality_score": 15, "4B_watch_score": 75}, "weighted_score_before": 58, "stage_label_before": "Stage2-Watch/FalsePositive", "raw_component_scores_after": {"relative_strength_score": 55, "customer_quality_score": 5, "named_order_score": 0, "delivery_backlog_score": 0, "qualification_acceptance_score": 0, "utilization_score": 15, "revenue_bridge_score": 0, "gross_margin_bridge_score": 0, "valuation_blowoff_risk_score": 75, "execution_risk_score": 90, "source_quality_score": 5, "4B_watch_score": 90}, "weighted_score_after": 44, "stage_label_after": "Rejected-Stage2 / Equipment-theme RiskWatch", "changed_components": ["customer_quality_score", "named_order_score", "delivery_backlog_score", "qualification_acceptance_score", "revenue_bridge_score", "gross_margin_bridge_score", "source_quality_score", "4B_watch_score"], "component_delta_explanation": "C07 requires equipment/parts relative strength to convert into named customer order, qualification/acceptance, delivery backlog, utilization and revenue/margin bridge before clean Stage2/Green; equipment-theme MFE alone is demoted or wrapped with local 4B/high-MAE watch.", "MFE_90D_pct": 30.61, "MAE_90D_pct": -6.09, "score_return_alignment_label": "early_equipment_MFE_then_deep_MAE_false_positive", "current_profile_verdict": "current_profile_false_positive_high_MAE_4B_too_late"}
{"row_type": "case", "case_id": "R2L86-C07-03", "symbol": "089970", "company_name": "브이엠", "round": "R2", "loop": 86, "large_sector_id": "L2_AI_SEMICONDUCTOR_ELECTRONICS", "canonical_archetype_id": "C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH", "fine_archetype_id": "OVERLAY_METROLOGY_ETCH_EQUIPMENT_SIC_PARTS_RELATIVE_STRENGTH_ORDER_ACCEPTANCE_REVENUE_BRIDGE_VS_EQUIPMENT_THEME_BLOWOFF_FADE", "case_type": "etch_equipment_relative_strength_theme_high_MAE_counterexample", "positive_or_counterexample": "counterexample", "best_trigger": "R2L86-C07-03-S2FP-20240213", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "equipment_cycle_MFE_then_high_MAE_theme_fade", "current_profile_verdict": "current_profile_false_positive_high_MAE", "price_source": "Songdaiki/stock-web", "notes": "Etch-equipment cycle MFE should remain RiskWatch unless named orders, shipment timing, customer acceptance and margin conversion are explicit."}
{"row_type": "trigger", "trigger_id": "R2L86-C07-03-S2FP-20240213", "case_id": "R2L86-C07-03", "symbol": "089970", "company_name": "브이엠", "round": "R2", "loop": 86, "large_sector_id": "L2_AI_SEMICONDUCTOR_ELECTRONICS", "canonical_archetype_id": "C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH", "fine_archetype_id": "OVERLAY_METROLOGY_ETCH_EQUIPMENT_SIC_PARTS_RELATIVE_STRENGTH_ORDER_ACCEPTANCE_REVENUE_BRIDGE_VS_EQUIPMENT_THEME_BLOWOFF_FADE", "loop_objective": "coverage_gap_fill|counterexample_mining|HBM_equipment_order_relative_strength_guardrail|order_acceptance_revenue_margin_bridge|canonical_archetype_compression", "trigger_type": "Stage2-FalsePositive", "trigger_date": "2024-02-13", "evidence_available_at_that_date": "etch equipment / memory capex recovery / HBM equipment relative strength proxy without confirmed named order, shipment and margin bridge", "evidence_source": "source_proxy_only; evidence_url_pending", "stage2_evidence_fields": ["relative_strength_proxy", "customer_quality_proxy", "equipment_or_parts_order_proxy"], "stage3_evidence_fields": ["named_customer_order", "qualification_acceptance", "delivery_backlog", "utilization", "revenue_margin_conversion"], "stage4b_evidence_fields": ["equipment_MFE_without_order_bridge", "valuation_blowoff", "post_peak_drawdown"], "stage4c_evidence_fields": ["hard_order_loss_or_customer_acceptance_break_watch_only"], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/089/089970/2024.csv", "profile_path": "atlas/symbol_profiles/089/089970.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "entry_date": "2024-02-13", "entry_price": 13110, "MFE_30D_pct": 29.67, "MFE_90D_pct": 29.67, "MFE_180D_pct": 34.94, "MFE_1Y_pct": null, "MFE_2Y_pct": null, "MAE_30D_pct": -4.96, "MAE_90D_pct": -4.96, "MAE_180D_pct": -36.69, "MAE_1Y_pct": null, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2024-07-01", "peak_price": 17690, "drawdown_after_peak_pct": -53.08, "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": 0.35, "four_b_full_window_peak_proximity": 0.3, "four_b_timing_verdict": "etch_equipment_theme_MFE_rejected_without_customer_order_delivery_revenue_margin_bridge", "four_b_evidence_type": ["equipment_MFE_without_order_bridge", "post_peak_drawdown", "source_proxy_gap"], "four_c_protection_label": "hard_4C_requires_non_price_order_loss_or_customer_acceptance_break", "trigger_outcome_label": "equipment_cycle_MFE_then_high_MAE_theme_fade", "current_profile_verdict": "current_profile_false_positive_high_MAE", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_2024_window_no_profile_CA_candidate", "same_entry_group_id": "R2L86-C07-03", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R2L86-C07-03", "trigger_id": "R2L86-C07-03-S2FP-20240213", "symbol": "089970", "large_sector_id": "L2_AI_SEMICONDUCTOR_ELECTRONICS", "canonical_archetype_id": "C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH", "raw_component_scores_before": {"relative_strength_score": 55, "customer_quality_score": 20, "named_order_score": 5, "delivery_backlog_score": 10, "qualification_acceptance_score": 10, "utilization_score": 15, "revenue_bridge_score": 5, "gross_margin_bridge_score": 5, "valuation_blowoff_risk_score": 75, "execution_risk_score": 80, "source_quality_score": 15, "4B_watch_score": 75}, "weighted_score_before": 58, "stage_label_before": "Stage2-Watch/FalsePositive", "raw_component_scores_after": {"relative_strength_score": 55, "customer_quality_score": 5, "named_order_score": 0, "delivery_backlog_score": 0, "qualification_acceptance_score": 0, "utilization_score": 15, "revenue_bridge_score": 0, "gross_margin_bridge_score": 0, "valuation_blowoff_risk_score": 75, "execution_risk_score": 90, "source_quality_score": 5, "4B_watch_score": 90}, "weighted_score_after": 44, "stage_label_after": "Rejected-Stage2 / Equipment-theme RiskWatch", "changed_components": ["customer_quality_score", "named_order_score", "delivery_backlog_score", "qualification_acceptance_score", "revenue_bridge_score", "gross_margin_bridge_score", "source_quality_score", "4B_watch_score"], "component_delta_explanation": "C07 requires equipment/parts relative strength to convert into named customer order, qualification/acceptance, delivery backlog, utilization and revenue/margin bridge before clean Stage2/Green; equipment-theme MFE alone is demoted or wrapped with local 4B/high-MAE watch.", "MFE_90D_pct": 29.67, "MAE_90D_pct": -4.96, "score_return_alignment_label": "equipment_cycle_MFE_then_high_MAE_theme_fade", "current_profile_verdict": "current_profile_false_positive_high_MAE"}
{"row_type": "shadow_weight", "axis": "C07_equipment_relative_strength_customer_order_acceptance_revenue_margin_bridge_required", "scope": "canonical_archetype_specific", "large_sector_id": "L2_AI_SEMICONDUCTOR_ELECTRONICS", "canonical_archetype_id": "C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH", "baseline_value": 0, "tested_value": 1, "delta": "+1", "reason": "HBM/semi equipment relative-strength rerating requires named customer order, qualification/acceptance, delivery backlog, utilization and revenue/margin conversion; equipment-theme MFE without bridge fades into high MAE or needs local 4B watch.", "backtest_effect": "keeps 064760 with local 4B/order-acceptance watch; demotes 322310/089970 equipment-theme false positives", "trigger_ids": "R2L86-C07-01-S2A-20240213|R2L86-C07-02-S2FP-20240213|R2L86-C07-03-S2FP-20240213", "calibration_usable_count": 3, "new_independent_case_count": 3, "counterexample_count": 2, "confidence": "low", "proposal_type": "canonical_shadow_only", "notes": "source_proxy_only/evidence_url_pending; not production"}
{"row_type": "residual_contribution", "round": "R2", "loop": 86, "large_sector_id": "L2_AI_SEMICONDUCTOR_ELECTRONICS", "canonical_archetype_id": "C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH", "new_independent_case_count": 3, "reused_case_count": 0, "new_symbol_count": 3, "new_trigger_family_count": 3, "tested_existing_calibrated_axes": ["stage2_actionable_evidence_bonus", "price_only_blowoff_blocks_positive_stage", "full_4b_requires_non_price_evidence", "hard_4c_thesis_break_routes_to_4c", "source_proxy_only_blocks_runtime_promotion", "high_MAE_guardrail", "local_4B_watch_before_full_4B_when_MFE_outruns_bridge"], "residual_error_types_found": ["semi_equipment_theme_false_positive_high_MAE", "customer_order_acceptance_revenue_margin_bridge_required", "local_4B_late_after_equipment_MFE", "source_proxy_runtime_promotion_risk", "high_MAE_positive_Green_blocker"], "loop_contribution_label": "canonical_archetype_rule_candidate", "do_not_propose_new_weight_delta": true}
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
- For C07, test a canonical-archetype guard requiring named customer order, qualification/acceptance, delivery backlog, utilization and revenue/gross-margin conversion before clean Stage2/Green.

## 27. Next Round State

```text
completed_round = R2
completed_loop = 86
next_round = R3
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
