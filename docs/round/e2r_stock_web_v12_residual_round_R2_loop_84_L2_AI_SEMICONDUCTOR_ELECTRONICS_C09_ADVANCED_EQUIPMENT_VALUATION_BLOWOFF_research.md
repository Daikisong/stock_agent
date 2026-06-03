# E2R Stock-Web v12 Residual Research — R2 Loop 84 / L2 / C09

## 0. Research Metadata

```json
{
  "research_session": "post_calibrated_sector_archetype_residual_research",
  "mode": "historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12",
  "scheduled_round": "R2",
  "scheduled_loop": 84,
  "round_schedule_status": "valid",
  "round_sector_consistency": "pass",
  "completed_round": "R2",
  "completed_loop": 84,
  "computed_next_round": "R3",
  "computed_next_loop": 84,
  "large_sector_id": "L2_AI_SEMICONDUCTOR_ELECTRONICS",
  "canonical_archetype_id": "C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF",
  "fine_archetype_id": "ADVANCED_INSPECTION_METROLOGY_EQUIPMENT_ORDER_QUALIFICATION_VALUATION_BLOWOFF_VS_THEME_FADE",
  "loop_objective": [
    "coverage_gap_fill",
    "counterexample_mining",
    "advanced_equipment_order_qualification_guardrail",
    "valuation_blowoff_local_4B_timing_test",
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
scheduled_loop = 84
allowed_large_sector = L2_AI_SEMICONDUCTOR_ELECTRONICS
selected_large_sector = L2_AI_SEMICONDUCTOR_ELECTRONICS
selected_canonical_archetype_id = C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF
computed_next_round = R3
computed_next_loop = 84
round_schedule_status = valid
round_sector_consistency = pass
```

R2 is the AI / semiconductor / electronics round. This run selects C09 because loop83 already tested C10 memory-recovery equipment cycle. C09 is the more surgical question: when does advanced equipment MFE represent actual order/qualification conversion, and when is it merely valuation blowoff?

The tested mechanism:

```text
advanced process / inspection / metrology / CMP equipment theme
→ named customer or qualification
→ tool acceptance / delivery backlog
→ revenue and margin conversion
→ durable rerating or local 4B / false-positive fade
```

A tool can sparkle on the lab bench, but the stock only deserves a durable Stage2 if the tool reaches the customer line, then the revenue line.

## 3. Previous Coverage / Duplicate Avoidance Check

No-Repeat is used only as a duplicate ledger.

```text
hard_duplicate_key = canonical_archetype_id + symbol + trigger_type + entry_date
```

C09 top-covered symbols include `240810`, `036930`, `039030`, `403870`, `003160`, and `042700`. This run avoids that top-covered set and uses:

```text
281820 / 케이씨텍
322310 / 오로스테크놀로지
348210 / 넥스틴
```

All three are treated as new independent C09 cases for this loop. No hard duplicate is intentionally reused.

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
| 281820 | 케이씨텍 | `atlas/symbol_profiles/281/281820.json` | no profile-level CA candidate |
| 322310 | 오로스테크놀로지 | `atlas/symbol_profiles/322/322310.json` | no profile-level CA candidate |
| 348210 | 넥스틴 | `atlas/symbol_profiles/348/348210.json` | old 2021 CA candidates; selected 2024/2025 forward window clean |

## 5. Historical Eligibility Gate

| case_id | symbol | entry_date | entry_price | forward window | 180D status | calibration_usable |
|---|---:|---|---:|---:|---|---|
| R2L84-C09-01 | 281820 | 2024-02-13 | 33,200 | 180D | clean | true |
| R2L84-C09-02 | 322310 | 2024-01-24 | 34,650 | 180D | clean | true |
| R2L84-C09-03 | 348210 | 2024-02-28 | 74,800 | 180D | clean | true |

## 6. Canonical Archetype Compression Map

| canonical_archetype_id | fine/deep route | keep / reject logic |
|---|---|---|
| C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF | EQUIPMENT_ORDER_QUALIFICATION_HIGH_MFE | keep Stage2 only when order/qualification/revenue bridge exists; add local 4B after high MFE |
| C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF | METROLOGY_THEME_MFE_FADE | reject or local-4B-watch when MFE occurs without named order/tool acceptance |
| C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF | INSPECTION_VALUATION_BLOWOFF_FALSE_POSITIVE | reject valuation rerating if revenue bridge is absent |

## 7. Case Selection Summary

| case_id | symbol | company | trigger_type | entry_date | entry_price | MFE_180D_pct | MAE_180D_pct | current_profile_verdict |
|---|---:|---|---|---|---:|---:|---:|---|
| R2L84-C09-01 | 281820 | 케이씨텍 | Stage2-Actionable | 2024-02-13 | 33,200 | 77.71 | -10.99 | current_profile_4B_too_late_after_high_MFE |
| R2L84-C09-02 | 322310 | 오로스테크놀로지 | Stage2-FalsePositive | 2024-01-24 | 34,650 | 17.6 | -56.33 | current_profile_false_positive_4B_too_late |
| R2L84-C09-03 | 348210 | 넥스틴 | Stage2-FalsePositive | 2024-02-28 | 74,800 | 4.14 | -46.06 | current_profile_false_positive |

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

This MD therefore creates a source-repair queue and a C09 shadow guardrail candidate. It must not be promoted directly into runtime weights until a later source-repair pass attaches primary evidence URLs: named customer order, qualification or tool acceptance, delivery backlog, revenue bridge, margin bridge, company disclosure, or report evidence.

## 10. Price Data Source Map

| symbol | shard path | profile path |
|---|---|---|
| 281820 | `atlas/ohlcv_tradable_by_symbol_year/281/281820/2024.csv` and `2025.csv` | `atlas/symbol_profiles/281/281820.json` |
| 322310 | `atlas/ohlcv_tradable_by_symbol_year/322/322310/2024.csv` and `2025.csv` | `atlas/symbol_profiles/322/322310.json` |
| 348210 | `atlas/ohlcv_tradable_by_symbol_year/348/348210/2024.csv` and `2025.csv` | `atlas/symbol_profiles/348/348210.json` |

## 11. Case-by-Case Trigger Grid

### Case 1 — 281820 / 케이씨텍

C09 high-MFE positive with local 4B requirement. The price path produced very high MFE from the early equipment-capex trigger, but the later drawdown makes it unsafe to treat as clean Green. The correct label is Stage2-Actionable only if source repair confirms order/qualification/revenue bridge, plus local 4B watch after blowoff.

### Case 2 — 322310 / 오로스테크놀로지

C09 metrology theme MFE fade. The early MFE was real enough to be tradable, but the later MAE and drawdown show that a metrology theme burst is not durable C09 evidence by itself.

### Case 3 — 348210 / 넥스틴

C09 advanced inspection valuation false positive. The MFE after entry was small, and MAE widened heavily. The model should reject valuation rerating without a new order/customer qualification/revenue bridge.

## 12. Trigger-Level OHLC Backtest Tables

| symbol | entry | MFE30 | MAE30 | MFE90 | MAE90 | MFE180 | MAE180 | peak | post-peak DD |
|---|---:|---:|---:|---:|---:|---:|---:|---|---:|
| 281820 | 33,200 | 62.95 | -3.77 | 77.71 | -6.63 | 77.71 | -10.99 | 2024-07-11 / 59,000 | -58.81 |
| 322310 | 34,650 | 17.60 | -5.92 | 17.60 | -35.93 | 17.60 | -56.33 | 2024-02-27 / 40,750 | -62.87 |
| 348210 | 74,800 | 4.14 | -13.64 | 4.14 | -26.34 | 4.14 | -46.06 | 2024-03-04 / 77,900 | -48.20 |

## 13. Current Calibrated Profile Stress Test

| case_id | P0 likely behavior | actual path | verdict |
|---|---|---|---|
| R2L84-C09-01 | Stage2-Actionable if bridge exists | high MFE, later deep drawdown | 4B too late after high MFE |
| R2L84-C09-02 | risk of treating metrology theme as Stage2 | short MFE / very high MAE | false positive / 4B too late |
| R2L84-C09-03 | risk of treating valuation rerating as Stage2 | low MFE / high MAE | false positive |

## 14. Stage2 / Yellow / Green Comparison

```text
green_lateness_ratio = not_applicable
reason = no confirmed Stage3-Green trigger is assigned in this residual MD
```

For C09, the residual is not Green lateness. The residual is whether advanced equipment valuation MFE becomes Stage2-Actionable before named order, qualification, tool acceptance and revenue bridge are proven.

## 15. 4B Local vs Full-window Timing Audit

| case_id | local proximity | full-window proximity | verdict |
|---|---:|---:|---|
| R2L84-C09-01 | 0.90 | 0.80 | local 4B watch required when equipment MFE outruns order bridge |
| R2L84-C09-02 | 0.90 | 0.80 | theme MFE should be local 4B watch or reject without order bridge |
| R2L84-C09-03 | 0.35 | 0.30 | valuation theme rejected without new order/revenue bridge |

## 16. 4C Protection Audit

No hard 4C is promoted from this file.

```text
four_c_protection_label = hard_4C_requires_non_price_order_or_customer_break
hard_4c_price_only_allowed = false
```

## 17. Sector-Specific Rule Candidate

```text
rule_scope = no_new_global_rule
sector_specific_rule_candidate = L2 advanced-equipment rows need named order/customer qualification/tool acceptance/revenue bridge before Stage2-Actionable
confidence = low
reason = all evidence rows are source_proxy_only / evidence_url_pending
```

## 18. Canonical-Archetype Rule Candidate

```text
canonical_archetype_id = C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF
candidate_axis = C09_advanced_equipment_order_qualification_revenue_bridge_required
effect = keep high-MFE positive only with local 4B watch; demote valuation/theme false positives
production_scoring_changed = false
shadow_weight_only = true
do_not_propose_new_weight_delta = true
```

## 19. Before / After Backtest Comparison

| profile | eligible triggers | avg MFE90 | avg MAE90 | false-positive behavior | verdict |
|---|---:|---:|---:|---|---|
| P0 e2r_2_1_stock_web_calibrated_proxy | 3 | 33.15 | -22.97 | may over-credit advanced-equipment valuation MFE | needs C09 bridge repair |
| P1 canonical shadow bridge profile | 3 | 77.71 on kept positive | -6.63 on kept positive | demotes 322310/348210 | better alignment, source repair required |

## 20. Score-Return Alignment Matrix

| case_id | weighted before | label before | weighted after | label after | alignment |
|---|---:|---|---:|---|---|
| R2L84-C09-01 | 80 | Stage2-Actionable | 78 | Stage2-Actionable + local 4B/high-MAE watch | partially aligned |
| R2L84-C09-02 | 59 | Stage2-Watch/FalsePositive | 46 | Rejected-Stage2 / RiskWatch or local 4B watch | improved |
| R2L84-C09-03 | 59 | Stage2-Watch/FalsePositive | 46 | Rejected-Stage2 / RiskWatch or local 4B watch | improved |

## 21. Coverage Matrix

| large_sector_id | canonical_archetype_id | fine_archetype_id | positive | counterexample | 4B | 4C | new cases | reused | usable triggers | current errors | sector rule | canonical rule | coverage gap after |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---|---|---|
| L2_AI_SEMICONDUCTOR_ELECTRONICS | C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF | ADVANCED_INSPECTION_METROLOGY_EQUIPMENT_ORDER_QUALIFICATION_VALUATION_BLOWOFF_VS_THEME_FADE | 1 | 2 | 3-watch | 0 | 3 | 0 | 3 | 3 | no | yes | source repair needed |

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
  - advanced_equipment_valuation_theme_false_positive
  - local_4B_late_after_equipment_MFE
  - order_qualification_revenue_bridge_required
  - source_proxy_runtime_promotion_risk
  - high_MAE_positive_Green_blocker
new_axis_proposed: false
existing_axis_strengthened:
  - C09_advanced_equipment_order_qualification_revenue_bridge_required
  - source_proxy_only_blocks_runtime_promotion
  - local_4B_watch_before_full_4B_when_MFE_outruns_bridge
  - high_MAE_blocks_clean_Green
existing_axis_weakened: null
existing_axis_kept:
  - full_4b_requires_non_price_evidence
  - hard_4c_thesis_break_routes_to_4c
sector_specific_rule_candidate: null
canonical_archetype_rule_candidate: C09_advanced_equipment_order_qualification_revenue_bridge_required
no_new_signal_reason: null
loop_contribution_label: canonical_archetype_rule_candidate
do_not_propose_new_weight_delta: true
```

This loop adds 3 new independent cases, 2 counterexamples, and 3 residual errors for R2/L2_AI_SEMICONDUCTOR_ELECTRONICS/C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF.

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
- named customer/order detail
- qualification or tool acceptance detail
- delivery backlog and revenue conversion
- margin bridge
- production scoring implementation
```

## 24. Shadow Weight Calibration

```csv
row_type,axis,scope,large_sector_id,canonical_archetype_id,baseline_value,tested_value,delta,reason,backtest_effect,trigger_ids,calibration_usable_count,new_independent_case_count,counterexample_count,confidence,proposal_type,notes
shadow_weight,C09_advanced_equipment_order_qualification_revenue_bridge_required,canonical_archetype_specific,L2_AI_SEMICONDUCTOR_ELECTRONICS,C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF,0,1,+1,"Require named order, customer qualification, tool acceptance and revenue/margin bridge before Stage2-Actionable","keeps 281820 as high-MFE positive with local 4B watch; demotes 322310/348210","R2L84-C09-01-S2A-20240213|R2L84-C09-02-S2FP-20240124|R2L84-C09-03-S2FP-20240228",3,3,2,low,canonical_shadow_only,"source repair required; not production"
```

## 25. Machine-Readable Rows

```jsonl
{"row_type": "price_source_validation", "source": "Songdaiki/stock-web", "source_url": "https://github.com/Songdaiki/stock-web", "manifest_path": "atlas/manifest.json", "schema_path": "atlas/schema.json", "universe_path": "atlas/universe/all_symbols.csv", "manifest_max_date": "2026-02-20", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "raw_shard_root": "atlas/ohlcv_raw_by_symbol_year", "validation_status": "usable_for_historical_calibration"}
{"row_type": "case", "case_id": "R2L84-C09-01", "symbol": "281820", "company_name": "케이씨텍", "round": "R2", "loop": 84, "large_sector_id": "L2_AI_SEMICONDUCTOR_ELECTRONICS", "canonical_archetype_id": "C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF", "fine_archetype_id": "ADVANCED_INSPECTION_METROLOGY_EQUIPMENT_ORDER_QUALIFICATION_VALUATION_BLOWOFF_VS_THEME_FADE", "case_type": "advanced_equipment_positive_with_local_4B_blowoff", "positive_or_counterexample": "positive", "best_trigger": "R2L84-C09-01-S2A-20240213", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "high_MFE_positive_but_local_4B_needed", "current_profile_verdict": "current_profile_4B_too_late_after_high_MFE", "price_source": "Songdaiki/stock-web", "notes": "C09 can promote advanced equipment cases only when order/qualification/revenue bridge exists; large MFE needs local 4B watch."}
{"row_type": "trigger", "trigger_id": "R2L84-C09-01-S2A-20240213", "case_id": "R2L84-C09-01", "symbol": "281820", "company_name": "케이씨텍", "round": "R2", "loop": 84, "large_sector_id": "L2_AI_SEMICONDUCTOR_ELECTRONICS", "canonical_archetype_id": "C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF", "fine_archetype_id": "ADVANCED_INSPECTION_METROLOGY_EQUIPMENT_ORDER_QUALIFICATION_VALUATION_BLOWOFF_VS_THEME_FADE", "loop_objective": "coverage_gap_fill|counterexample_mining|advanced_equipment_order_qualification_guardrail|4B_non_price_requirement_stress_test|canonical_archetype_compression", "trigger_type": "Stage2-Actionable", "trigger_date": "2024-02-13", "evidence_available_at_that_date": "advanced process/CMP equipment and memory capex restart proxy; named order / qualification bridge pending", "evidence_source": "source_proxy_only; evidence_url_pending", "stage2_evidence_fields": ["advanced_equipment_or_metrology_proxy", "customer_qualification_proxy", "named_order_or_delivery_bridge_proxy"], "stage3_evidence_fields": ["named_customer", "tool_acceptance", "delivery_backlog", "revenue_margin_conversion", "revision_confirmation"], "stage4b_evidence_fields": ["valuation_blowoff", "theme_MFE_without_order_bridge", "post_peak_drawdown"], "stage4c_evidence_fields": ["hard_order_cancellation_or_customer_loss_watch_only"], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/281/281820/2024.csv", "profile_path": "atlas/symbol_profiles/281/281820.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "entry_date": "2024-02-13", "entry_price": 33200, "MFE_30D_pct": 62.95, "MFE_90D_pct": 77.71, "MFE_180D_pct": 77.71, "MFE_1Y_pct": null, "MFE_2Y_pct": null, "MAE_30D_pct": -3.77, "MAE_90D_pct": -6.63, "MAE_180D_pct": -10.99, "MAE_1Y_pct": null, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2024-07-11", "peak_price": 59000, "drawdown_after_peak_pct": -58.81, "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": 0.9, "four_b_full_window_peak_proximity": 0.8, "four_b_timing_verdict": "local_4B_watch_required_when_equipment_MFE_outruns_order_qualification_bridge", "four_b_evidence_type": ["valuation_blowoff", "order_bridge_gap", "post_peak_drawdown"], "four_c_protection_label": "hard_4C_requires_non_price_order_or_customer_break", "trigger_outcome_label": "high_MFE_positive_but_local_4B_needed", "current_profile_verdict": "current_profile_4B_too_late_after_high_MFE", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window_no_profile_CA_candidate", "same_entry_group_id": "R2L84-C09-01", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R2L84-C09-01", "trigger_id": "R2L84-C09-01-S2A-20240213", "symbol": "281820", "large_sector_id": "L2_AI_SEMICONDUCTOR_ELECTRONICS", "canonical_archetype_id": "C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF", "raw_component_scores_before": {"customer_qualification_score": 45, "named_order_score": 35, "delivery_backlog_score": 35, "revenue_bridge_score": 40, "margin_bridge_score": 35, "revision_score": 45, "relative_strength_score": 70, "valuation_blowoff_risk_score": 60, "execution_risk_score": 45, "source_quality_score": 20, "cycle_beta_risk_score": 35, "4B_watch_score": 40}, "weighted_score_before": 80, "stage_label_before": "Stage2-Actionable", "raw_component_scores_after": {"customer_qualification_score": 45, "named_order_score": 35, "delivery_backlog_score": 35, "revenue_bridge_score": 40, "margin_bridge_score": 35, "revision_score": 45, "relative_strength_score": 70, "valuation_blowoff_risk_score": 75, "execution_risk_score": 45, "source_quality_score": 10, "cycle_beta_risk_score": 35, "4B_watch_score": 80}, "weighted_score_after": 78, "stage_label_after": "Stage2-Actionable + local 4B/high-MAE watch", "changed_components": ["customer_qualification_score", "named_order_score", "delivery_backlog_score", "revenue_bridge_score", "margin_bridge_score", "source_quality_score", "4B_watch_score"], "component_delta_explanation": "C09 requires named order/customer qualification/tool acceptance/revenue bridge before Stage2-Actionable; valuation or AI-equipment theme MFE alone is demoted or wrapped with local 4B watch.", "MFE_90D_pct": 77.71, "MAE_90D_pct": -6.63, "score_return_alignment_label": "high_MFE_positive_but_local_4B_needed", "current_profile_verdict": "current_profile_4B_too_late_after_high_MFE"}
{"row_type": "case", "case_id": "R2L84-C09-02", "symbol": "322310", "company_name": "오로스테크놀로지", "round": "R2", "loop": 84, "large_sector_id": "L2_AI_SEMICONDUCTOR_ELECTRONICS", "canonical_archetype_id": "C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF", "fine_archetype_id": "ADVANCED_INSPECTION_METROLOGY_EQUIPMENT_ORDER_QUALIFICATION_VALUATION_BLOWOFF_VS_THEME_FADE", "case_type": "metrology_equipment_theme_MFE_fade", "positive_or_counterexample": "counterexample", "best_trigger": "R2L84-C09-02-S2FP-20240124", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "short_MFE_high_MAE_false_positive", "current_profile_verdict": "current_profile_false_positive_4B_too_late", "price_source": "Songdaiki/stock-web", "notes": "Metrology theme MFE is not durable C09 evidence without named customer, tool acceptance and revenue conversion."}
{"row_type": "trigger", "trigger_id": "R2L84-C09-02-S2FP-20240124", "case_id": "R2L84-C09-02", "symbol": "322310", "company_name": "오로스테크놀로지", "round": "R2", "loop": 84, "large_sector_id": "L2_AI_SEMICONDUCTOR_ELECTRONICS", "canonical_archetype_id": "C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF", "fine_archetype_id": "ADVANCED_INSPECTION_METROLOGY_EQUIPMENT_ORDER_QUALIFICATION_VALUATION_BLOWOFF_VS_THEME_FADE", "loop_objective": "coverage_gap_fill|counterexample_mining|advanced_equipment_order_qualification_guardrail|4B_non_price_requirement_stress_test|canonical_archetype_compression", "trigger_type": "Stage2-FalsePositive", "trigger_date": "2024-01-24", "evidence_available_at_that_date": "overlay/metrology equipment theme and advanced-process qualification proxy without confirmed order/revenue bridge", "evidence_source": "source_proxy_only; evidence_url_pending", "stage2_evidence_fields": ["advanced_equipment_or_metrology_proxy", "customer_qualification_proxy", "named_order_or_delivery_bridge_proxy"], "stage3_evidence_fields": ["named_customer", "tool_acceptance", "delivery_backlog", "revenue_margin_conversion", "revision_confirmation"], "stage4b_evidence_fields": ["valuation_blowoff", "theme_MFE_without_order_bridge", "post_peak_drawdown"], "stage4c_evidence_fields": ["hard_order_cancellation_or_customer_loss_watch_only"], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/322/322310/2024.csv", "profile_path": "atlas/symbol_profiles/322/322310.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "entry_date": "2024-01-24", "entry_price": 34650, "MFE_30D_pct": 17.6, "MFE_90D_pct": 17.6, "MFE_180D_pct": 17.6, "MFE_1Y_pct": null, "MFE_2Y_pct": null, "MAE_30D_pct": -5.92, "MAE_90D_pct": -35.93, "MAE_180D_pct": -56.33, "MAE_1Y_pct": null, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2024-02-27", "peak_price": 40750, "drawdown_after_peak_pct": -62.87, "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": 0.9, "four_b_full_window_peak_proximity": 0.8, "four_b_timing_verdict": "theme_MFE_should_be_local_4B_watch_or_reject_without_order_bridge", "four_b_evidence_type": ["valuation_blowoff", "order_bridge_gap", "post_peak_drawdown"], "four_c_protection_label": "hard_4C_requires_non_price_order_or_customer_break", "trigger_outcome_label": "short_MFE_high_MAE_false_positive", "current_profile_verdict": "current_profile_false_positive_4B_too_late", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window_no_profile_CA_candidate", "same_entry_group_id": "R2L84-C09-02", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R2L84-C09-02", "trigger_id": "R2L84-C09-02-S2FP-20240124", "symbol": "322310", "large_sector_id": "L2_AI_SEMICONDUCTOR_ELECTRONICS", "canonical_archetype_id": "C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF", "raw_component_scores_before": {"customer_qualification_score": 20, "named_order_score": 5, "delivery_backlog_score": 10, "revenue_bridge_score": 10, "margin_bridge_score": 5, "revision_score": 20, "relative_strength_score": 45, "valuation_blowoff_risk_score": 75, "execution_risk_score": 70, "source_quality_score": 15, "cycle_beta_risk_score": 70, "4B_watch_score": 45}, "weighted_score_before": 59, "stage_label_before": "Stage2-Watch/FalsePositive", "raw_component_scores_after": {"customer_qualification_score": 5, "named_order_score": 0, "delivery_backlog_score": 0, "revenue_bridge_score": 0, "margin_bridge_score": 0, "revision_score": 20, "relative_strength_score": 45, "valuation_blowoff_risk_score": 75, "execution_risk_score": 70, "source_quality_score": 5, "cycle_beta_risk_score": 70, "4B_watch_score": 85}, "weighted_score_after": 46, "stage_label_after": "Rejected-Stage2 / RiskWatch or local 4B watch", "changed_components": ["customer_qualification_score", "named_order_score", "delivery_backlog_score", "revenue_bridge_score", "margin_bridge_score", "source_quality_score", "4B_watch_score"], "component_delta_explanation": "C09 requires named order/customer qualification/tool acceptance/revenue bridge before Stage2-Actionable; valuation or AI-equipment theme MFE alone is demoted or wrapped with local 4B watch.", "MFE_90D_pct": 17.6, "MAE_90D_pct": -35.93, "score_return_alignment_label": "short_MFE_high_MAE_false_positive", "current_profile_verdict": "current_profile_false_positive_4B_too_late"}
{"row_type": "case", "case_id": "R2L84-C09-03", "symbol": "348210", "company_name": "넥스틴", "round": "R2", "loop": 84, "large_sector_id": "L2_AI_SEMICONDUCTOR_ELECTRONICS", "canonical_archetype_id": "C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF", "fine_archetype_id": "ADVANCED_INSPECTION_METROLOGY_EQUIPMENT_ORDER_QUALIFICATION_VALUATION_BLOWOFF_VS_THEME_FADE", "case_type": "inspection_equipment_valuation_theme_false_positive", "positive_or_counterexample": "counterexample", "best_trigger": "R2L84-C09-03-S2FP-20240228", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "low_MFE_high_MAE_valuation_fade", "current_profile_verdict": "current_profile_false_positive", "price_source": "Songdaiki/stock-web", "notes": "Advanced inspection valuation rerating should not be Stage2-Actionable when order/qualification bridge is not repaired."}
{"row_type": "trigger", "trigger_id": "R2L84-C09-03-S2FP-20240228", "case_id": "R2L84-C09-03", "symbol": "348210", "company_name": "넥스틴", "round": "R2", "loop": 84, "large_sector_id": "L2_AI_SEMICONDUCTOR_ELECTRONICS", "canonical_archetype_id": "C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF", "fine_archetype_id": "ADVANCED_INSPECTION_METROLOGY_EQUIPMENT_ORDER_QUALIFICATION_VALUATION_BLOWOFF_VS_THEME_FADE", "loop_objective": "coverage_gap_fill|counterexample_mining|advanced_equipment_order_qualification_guardrail|4B_non_price_requirement_stress_test|canonical_archetype_compression", "trigger_type": "Stage2-FalsePositive", "trigger_date": "2024-02-28", "evidence_available_at_that_date": "advanced inspection equipment valuation rerating proxy without enough new order/qualification bridge", "evidence_source": "source_proxy_only; evidence_url_pending", "stage2_evidence_fields": ["advanced_equipment_or_metrology_proxy", "customer_qualification_proxy", "named_order_or_delivery_bridge_proxy"], "stage3_evidence_fields": ["named_customer", "tool_acceptance", "delivery_backlog", "revenue_margin_conversion", "revision_confirmation"], "stage4b_evidence_fields": ["valuation_blowoff", "theme_MFE_without_order_bridge", "post_peak_drawdown"], "stage4c_evidence_fields": ["hard_order_cancellation_or_customer_loss_watch_only"], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/348/348210/2024.csv", "profile_path": "atlas/symbol_profiles/348/348210.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "entry_date": "2024-02-28", "entry_price": 74800, "MFE_30D_pct": 4.14, "MFE_90D_pct": 4.14, "MFE_180D_pct": 4.14, "MFE_1Y_pct": null, "MFE_2Y_pct": null, "MAE_30D_pct": -13.64, "MAE_90D_pct": -26.34, "MAE_180D_pct": -46.06, "MAE_1Y_pct": null, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2024-03-04", "peak_price": 77900, "drawdown_after_peak_pct": -48.2, "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": 0.35, "four_b_full_window_peak_proximity": 0.3, "four_b_timing_verdict": "valuation_theme_rejected_without_new_order_qualification_revenue_bridge", "four_b_evidence_type": ["valuation_blowoff", "order_bridge_gap", "post_peak_drawdown"], "four_c_protection_label": "hard_4C_requires_non_price_order_or_customer_break", "trigger_outcome_label": "low_MFE_high_MAE_valuation_fade", "current_profile_verdict": "current_profile_false_positive", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window_after_old_2021_CA_candidates", "same_entry_group_id": "R2L84-C09-03", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R2L84-C09-03", "trigger_id": "R2L84-C09-03-S2FP-20240228", "symbol": "348210", "large_sector_id": "L2_AI_SEMICONDUCTOR_ELECTRONICS", "canonical_archetype_id": "C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF", "raw_component_scores_before": {"customer_qualification_score": 20, "named_order_score": 5, "delivery_backlog_score": 10, "revenue_bridge_score": 10, "margin_bridge_score": 5, "revision_score": 20, "relative_strength_score": 45, "valuation_blowoff_risk_score": 75, "execution_risk_score": 70, "source_quality_score": 15, "cycle_beta_risk_score": 70, "4B_watch_score": 45}, "weighted_score_before": 59, "stage_label_before": "Stage2-Watch/FalsePositive", "raw_component_scores_after": {"customer_qualification_score": 5, "named_order_score": 0, "delivery_backlog_score": 0, "revenue_bridge_score": 0, "margin_bridge_score": 0, "revision_score": 20, "relative_strength_score": 45, "valuation_blowoff_risk_score": 75, "execution_risk_score": 70, "source_quality_score": 5, "cycle_beta_risk_score": 70, "4B_watch_score": 85}, "weighted_score_after": 46, "stage_label_after": "Rejected-Stage2 / RiskWatch or local 4B watch", "changed_components": ["customer_qualification_score", "named_order_score", "delivery_backlog_score", "revenue_bridge_score", "margin_bridge_score", "source_quality_score", "4B_watch_score"], "component_delta_explanation": "C09 requires named order/customer qualification/tool acceptance/revenue bridge before Stage2-Actionable; valuation or AI-equipment theme MFE alone is demoted or wrapped with local 4B watch.", "MFE_90D_pct": 4.14, "MAE_90D_pct": -26.34, "score_return_alignment_label": "low_MFE_high_MAE_valuation_fade", "current_profile_verdict": "current_profile_false_positive"}
{"row_type": "shadow_weight", "axis": "C09_advanced_equipment_order_qualification_revenue_bridge_required", "scope": "canonical_archetype_specific", "large_sector_id": "L2_AI_SEMICONDUCTOR_ELECTRONICS", "canonical_archetype_id": "C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF", "baseline_value": 0, "tested_value": 1, "delta": "+1", "reason": "Advanced equipment rerating requires named order, customer qualification, tool acceptance and revenue/margin bridge; valuation blowoff MFE alone should trigger local 4B watch or rejection.", "backtest_effect": "keeps 281820 as high-MFE positive with local 4B watch; demotes 322310/348210 false positives", "trigger_ids": "R2L84-C09-01-S2A-20240213|R2L84-C09-02-S2FP-20240124|R2L84-C09-03-S2FP-20240228", "calibration_usable_count": 3, "new_independent_case_count": 3, "counterexample_count": 2, "confidence": "low", "proposal_type": "canonical_shadow_only", "notes": "source_proxy_only/evidence_url_pending; not production"}
{"row_type": "residual_contribution", "round": "R2", "loop": 84, "large_sector_id": "L2_AI_SEMICONDUCTOR_ELECTRONICS", "canonical_archetype_id": "C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF", "new_independent_case_count": 3, "reused_case_count": 0, "new_symbol_count": 3, "new_trigger_family_count": 3, "tested_existing_calibrated_axes": ["stage2_actionable_evidence_bonus", "price_only_blowoff_blocks_positive_stage", "full_4b_requires_non_price_evidence", "hard_4c_thesis_break_routes_to_4c", "source_proxy_only_blocks_runtime_promotion", "high_MAE_guardrail"], "residual_error_types_found": ["advanced_equipment_valuation_theme_false_positive", "local_4B_late_after_equipment_MFE", "order_qualification_revenue_bridge_required", "source_proxy_runtime_promotion_risk", "high_MAE_positive_Green_blocker"], "loop_contribution_label": "canonical_archetype_rule_candidate", "do_not_propose_new_weight_delta": true}
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
- For C09, test a canonical-archetype guard requiring named order, customer qualification, tool acceptance, delivery/revenue bridge and margin conversion before Stage2-Actionable.

## 27. Next Round State

```text
completed_round = R2
completed_loop = 84
next_round = R3
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
