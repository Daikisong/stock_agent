# E2R Stock-Web v12 Residual Research — R2 Loop 85 / L2 / C08

## 0. Research Metadata

```json
{
  "research_session": "post_calibrated_sector_archetype_residual_research",
  "mode": "historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12",
  "scheduled_round": "R2",
  "scheduled_loop": 85,
  "round_schedule_status": "valid",
  "round_sector_consistency": "pass",
  "completed_round": "R2",
  "completed_loop": 85,
  "computed_next_round": "R3",
  "computed_next_loop": 85,
  "large_sector_id": "L2_AI_SEMICONDUCTOR_ELECTRONICS",
  "canonical_archetype_id": "C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY",
  "fine_archetype_id": "HBM_TEST_HANDLER_PROBE_CARD_OSAT_CUSTOMER_QUALITY_REVENUE_BRIDGE_VS_TEST_THEME_BLOWOFF_FADE",
  "loop_objective": [
    "coverage_gap_fill",
    "counterexample_mining",
    "semi_test_socket_customer_quality_guardrail",
    "customer_quality_to_revenue_margin_bridge_test",
    "test_theme_blowoff_high_MAE_counterexample_test",
    "local_4B_timing_after_test_equipment_MFE",
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
scheduled_loop = 85
allowed_large_sector = L2_AI_SEMICONDUCTOR_ELECTRONICS
selected_large_sector = L2_AI_SEMICONDUCTOR_ELECTRONICS
selected_canonical_archetype_id = C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY
computed_next_round = R3
computed_next_loop = 85
round_schedule_status = valid
round_sector_consistency = pass
```

R2 is the AI / semiconductor / electronics round. This run selects C08 because loop84 already tested C09 and loop83 tested C10. The tested mechanism is:

```text
test handler / socket / probe-card / OSAT test-capacity headline
→ named customer quality or acceptance
→ delivery backlog and utilization
→ revenue conversion
→ gross / OP margin bridge
→ durable rerating or local 4B / high-MAE theme fade
```

C08 is the tester’s proof. A handler, socket or probe-card headline is only a signal; the rerating begins when the tool is accepted, shipped, utilized and converted into margin.

## 3. Previous Coverage / Duplicate Avoidance Check

No-Repeat is used only as a duplicate ledger.

```text
hard_duplicate_key = canonical_archetype_id + symbol + trigger_type + entry_date
```

C08 top-covered symbols include `098120`, `080580`, `058470`, `095340`, `131290`, and `219130`. This run avoids that top-covered set and uses:

```text
089030 / 테크윙
330860 / 네패스아크
252990 / 샘씨엔에스
```

All three are treated as new independent C08 semi-test / customer-quality cases for this loop. No hard duplicate is intentionally reused.

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
| 089030 | 테크윙 | `atlas/symbol_profiles/089/089030.json` | old 2022 CA candidate; selected 2024 forward window clean |
| 330860 | 네패스아크 | `atlas/symbol_profiles/330/330860.json` | no profile-level CA candidate |
| 252990 | 샘씨엔에스 | `atlas/symbol_profiles/252/252990.json` | no profile-level CA candidate |

## 5. Historical Eligibility Gate

| case_id | symbol | entry_date | entry_price | forward window | 180D status | calibration_usable |
|---|---:|---|---:|---:|---|---|
| R2L85-C08-01 | 089030 | 2024-02-13 | 18,690 | 180D | clean | true |
| R2L85-C08-02 | 330860 | 2024-02-21 | 36,900 | 180D | clean | true |
| R2L85-C08-03 | 252990 | 2024-01-23 | 6,860 | 180D | clean | true |

## 6. Canonical Archetype Compression Map

| canonical_archetype_id | fine/deep route | keep / reject logic |
|---|---|---|
| C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY | HBM_TEST_HANDLER_CUSTOMER_ACCEPTANCE | keep Stage2 only with named customer quality, order/acceptance, delivery and revenue/margin bridge |
| C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY | OSAT_TEST_CAPACITY_THEME_FADE | reject when OSAT/test capacity MFE lacks durable customer utilization and revenue bridge |
| C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY | PROBE_CARD_CUSTOMER_QUALITY_THEME_FADE | reject probe-card/customer-quality theme heat without reorder and gross-margin conversion |

## 7. Case Selection Summary

| case_id | symbol | company | trigger_type | entry_date | entry_price | MFE_180D_pct | MAE_180D_pct | current_profile_verdict |
|---|---:|---|---|---|---:|---:|---:|---|
| R2L85-C08-01 | 089030 | 테크윙 | Stage2-Actionable | 2024-02-13 | 18,690 | 278.81 | -6.04 | current_profile_4B_too_late_after_extreme_test_equipment_MFE |
| R2L85-C08-02 | 330860 | 네패스아크 | Stage2-FalsePositive | 2024-02-21 | 36,900 | 25.75 | -67.48 | current_profile_false_positive_high_MAE_4B_late |
| R2L85-C08-03 | 252990 | 샘씨엔에스 | Stage2-FalsePositive | 2024-01-23 | 6,860 | 28.86 | -30.76 | current_profile_false_positive_theme_MFE_fade |

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

This MD therefore creates a source-repair queue and a C08 shadow guardrail candidate. It must not be promoted directly into runtime weights until a later source-repair pass attaches primary evidence URLs: customer order, tool acceptance, probe-card reorder, delivery backlog, utilization, revenue conversion, gross/OP margin bridge, company disclosure or report evidence.

## 10. Price Data Source Map

| symbol | shard path | profile path |
|---|---|---|
| 089030 | `atlas/ohlcv_tradable_by_symbol_year/089/089030/2024.csv` | `atlas/symbol_profiles/089/089030.json` |
| 330860 | `atlas/ohlcv_tradable_by_symbol_year/330/330860/2024.csv` | `atlas/symbol_profiles/330/330860.json` |
| 252990 | `atlas/ohlcv_tradable_by_symbol_year/252/252990/2024.csv` | `atlas/symbol_profiles/252/252990.json` |

## 11. Case-by-Case Trigger Grid

### Case 1 — 089030 / 테크윙

C08 HBM test-handler positive with mandatory local 4B watch. The MFE after the February trigger was extreme, but the post-peak drawdown shows why a clean Green label is unsafe without repaired customer/order/acceptance evidence. The right treatment is Stage2-Actionable plus local 4B watch when price outruns the bridge.

### Case 2 — 330860 / 네패스아크

C08 OSAT/test-capacity false positive. The early MFE was tradable, but MAE widened deeply. This is the row that rejects “test capacity theme” when customer acceptance, utilization and revenue/margin conversion are not visible.

### Case 3 — 252990 / 샘씨엔에스

C08 probe-card/customer-quality theme fade. The early spike did not become durable rerating. The model should demote probe-card theme MFE unless reorder visibility, ASP and gross-margin bridge are source-repaired.

## 12. Trigger-Level OHLC Backtest Tables

| symbol | entry | MFE30 | MAE30 | MFE90 | MAE90 | MFE180 | MAE180 | peak | post-peak DD |
|---|---:|---:|---:|---:|---:|---:|---:|---|---:|
| 089030 | 18,690 | 92.62 | -6.04 | 244.03 | -6.04 | 278.81 | -6.04 | 2024-07-11 / 70,800 | -57.63 |
| 330860 | 36,900 | 25.75 | -12.47 | 25.75 | -42.68 | 25.75 | -67.48 | 2024-03-12 / 46,400 | -74.14 |
| 252990 | 6,860 | 28.86 | -6.99 | 28.86 | -15.74 | 28.86 | -30.76 | 2024-02-07 / 8,840 | -46.27 |

## 13. Current Calibrated Profile Stress Test

| case_id | P0 likely behavior | actual path | verdict |
|---|---|---|---|
| R2L85-C08-01 | Stage2-Actionable if customer/order bridge exists | extreme MFE, later drawdown | 4B too late after test-equipment MFE |
| R2L85-C08-02 | risk of treating OSAT/test capacity theme as Stage2 | short MFE / deep MAE | false positive / high-MAE guardrail |
| R2L85-C08-03 | risk of treating probe-card theme spike as Stage2 | early MFE / later MAE | false positive / theme fade |

## 14. Stage2 / Yellow / Green Comparison

```text
green_lateness_ratio = not_applicable
reason = no confirmed Stage3-Green trigger is assigned in this residual MD
```

For C08, the residual is not Green lateness. The residual is whether semi-test MFE becomes clean Stage2/Green before customer quality, order acceptance, delivery and revenue/margin bridge are proven.

## 15. 4B Local vs Full-window Timing Audit

| case_id | local proximity | full-window proximity | verdict |
|---|---:|---:|---|
| R2L85-C08-01 | 0.95 | 0.85 | local 4B watch required when HBM test MFE outruns order/customer-quality bridge |
| R2L85-C08-02 | 0.35 | 0.30 | test-capacity theme rejected without customer acceptance/revenue bridge |
| R2L85-C08-03 | 0.35 | 0.30 | probe-card theme MFE rejected without customer reorder/margin bridge |

## 16. 4C Protection Audit

No hard 4C is promoted from this file.

```text
four_c_protection_label = hard_4C_requires_non_price_order_loss_or_customer_acceptance_break
hard_4c_price_only_allowed = false
```

## 17. Sector-Specific Rule Candidate

```text
rule_scope = no_new_global_rule
sector_specific_rule_candidate = L2/C08 semi-test rows need customer quality, order/acceptance, delivery, utilization and revenue/margin bridge before clean Stage2/Green
confidence = low
reason = all evidence rows are source_proxy_only / evidence_url_pending
```

## 18. Canonical-Archetype Rule Candidate

```text
canonical_archetype_id = C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY
candidate_axis = C08_customer_quality_order_acceptance_revenue_margin_bridge_required
effect = keep HBM test-handler positive with local 4B/customer-quality watch; demote OSAT/probe-card theme false positives
production_scoring_changed = false
shadow_weight_only = true
do_not_propose_new_weight_delta = true
```

## 19. Before / After Backtest Comparison

| profile | eligible triggers | avg MFE90 | avg MAE90 | false-positive behavior | verdict |
|---|---:|---:|---:|---|---|
| P0 e2r_2_1_stock_web_calibrated_proxy | 3 | 99.55 | -21.49 | may over-credit test-equipment/test-capacity theme MFE | needs C08 bridge repair |
| P1 canonical shadow bridge profile | 3 | 244.03 on kept positive | -6.04 on kept positive | demotes 330860/252990 | better alignment, source repair required |

## 20. Score-Return Alignment Matrix

| case_id | weighted before | label before | weighted after | label after | alignment |
|---|---:|---|---:|---|---|
| R2L85-C08-01 | 84 | Stage2-Actionable | 79 | Stage2-Actionable + local 4B/customer-quality watch | partially aligned |
| R2L85-C08-02 | 58 | Stage2-Watch/FalsePositive | 45 | Rejected-Stage2 / Test-theme RiskWatch | improved |
| R2L85-C08-03 | 58 | Stage2-Watch/FalsePositive | 45 | Rejected-Stage2 / Test-theme RiskWatch | improved |

## 21. Coverage Matrix

| large_sector_id | canonical_archetype_id | fine_archetype_id | positive | counterexample | 4B | 4C | new cases | reused | usable triggers | current errors | sector rule | canonical rule | coverage gap after |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---|---|---|
| L2_AI_SEMICONDUCTOR_ELECTRONICS | C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY | HBM_TEST_HANDLER_PROBE_CARD_OSAT_CUSTOMER_QUALITY_REVENUE_BRIDGE_VS_TEST_THEME_BLOWOFF_FADE | 1 | 2 | 3-watch | 0 | 3 | 0 | 3 | 3 | no | yes | source repair needed |

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
  - semi_test_theme_false_positive_high_MAE
  - customer_quality_order_acceptance_revenue_margin_bridge_required
  - local_4B_late_after_test_equipment_MFE
  - source_proxy_runtime_promotion_risk
  - high_MAE_positive_Green_blocker
new_axis_proposed: false
existing_axis_strengthened:
  - C08_customer_quality_order_acceptance_revenue_margin_bridge_required
  - source_proxy_only_blocks_runtime_promotion
  - local_4B_watch_before_full_4B_when_MFE_outruns_bridge
  - high_MAE_blocks_clean_Green
existing_axis_weakened: null
existing_axis_kept:
  - full_4b_requires_non_price_evidence
  - hard_4c_thesis_break_routes_to_4c
sector_specific_rule_candidate: null
canonical_archetype_rule_candidate: C08_customer_quality_order_acceptance_revenue_margin_bridge_required
no_new_signal_reason: null
loop_contribution_label: canonical_archetype_rule_candidate
do_not_propose_new_weight_delta: true
```

This loop adds 3 new independent cases, 2 counterexamples, and 3 residual errors for R2/L2_AI_SEMICONDUCTOR_ELECTRONICS/C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY.

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
- customer/order disclosure
- tool acceptance and delivery backlog
- utilization
- revenue and gross/OP margin conversion
- production scoring implementation
```

## 24. Shadow Weight Calibration

```csv
row_type,axis,scope,large_sector_id,canonical_archetype_id,baseline_value,tested_value,delta,reason,backtest_effect,trigger_ids,calibration_usable_count,new_independent_case_count,counterexample_count,confidence,proposal_type,notes
shadow_weight,C08_customer_quality_order_acceptance_revenue_margin_bridge_required,canonical_archetype_specific,L2_AI_SEMICONDUCTOR_ELECTRONICS,C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY,0,1,+1,"Require named customer quality, order/acceptance, delivery backlog, utilization and revenue/margin bridge before clean Stage2/Green","keeps 089030 with local 4B/customer-quality watch; demotes 330860/252990","R2L85-C08-01-S2A-20240213|R2L85-C08-02-S2FP-20240221|R2L85-C08-03-S2FP-20240123",3,3,2,low,canonical_shadow_only,"source repair required; not production"
```

## 25. Machine-Readable Rows

```jsonl
{"row_type": "price_source_validation", "source": "Songdaiki/stock-web", "source_url": "https://github.com/Songdaiki/stock-web", "manifest_path": "atlas/manifest.json", "schema_path": "atlas/schema.json", "universe_path": "atlas/universe/all_symbols.csv", "manifest_max_date": "2026-02-20", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "raw_shard_root": "atlas/ohlcv_raw_by_symbol_year", "validation_status": "usable_for_historical_calibration"}
{"row_type": "case", "case_id": "R2L85-C08-01", "symbol": "089030", "company_name": "테크윙", "round": "R2", "loop": 85, "large_sector_id": "L2_AI_SEMICONDUCTOR_ELECTRONICS", "canonical_archetype_id": "C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY", "fine_archetype_id": "HBM_TEST_HANDLER_PROBE_CARD_OSAT_CUSTOMER_QUALITY_REVENUE_BRIDGE_VS_TEST_THEME_BLOWOFF_FADE", "case_type": "HBM_test_handler_customer_quality_positive_with_local_4B_watch", "positive_or_counterexample": "positive", "best_trigger": "R2L85-C08-01-S2A-20240213", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "extreme_positive_MFE_but_local_4B_required_after_test_equipment_blowoff", "current_profile_verdict": "current_profile_4B_too_late_after_extreme_test_equipment_MFE", "price_source": "Songdaiki/stock-web", "notes": "C08 can keep Stage2 only when test-handler/socket/customer-quality signal converts into named order, customer acceptance, delivery, revenue and margin bridge."}
{"row_type": "trigger", "trigger_id": "R2L85-C08-01-S2A-20240213", "case_id": "R2L85-C08-01", "symbol": "089030", "company_name": "테크윙", "round": "R2", "loop": 85, "large_sector_id": "L2_AI_SEMICONDUCTOR_ELECTRONICS", "canonical_archetype_id": "C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY", "fine_archetype_id": "HBM_TEST_HANDLER_PROBE_CARD_OSAT_CUSTOMER_QUALITY_REVENUE_BRIDGE_VS_TEST_THEME_BLOWOFF_FADE", "loop_objective": "coverage_gap_fill|counterexample_mining|semi_test_socket_customer_quality_guardrail|local_4B_timing_after_test_MFE|canonical_archetype_compression", "trigger_type": "Stage2-Actionable", "trigger_date": "2024-02-13", "evidence_available_at_that_date": "HBM test handler / memory customer quality / inspection capacity proxy; primary order and customer acceptance evidence pending", "evidence_source": "source_proxy_only; evidence_url_pending", "stage2_evidence_fields": ["customer_quality_proxy", "test_handler_or_probe_card_proxy", "named_order_or_acceptance_proxy"], "stage3_evidence_fields": ["named_customer", "tool_acceptance", "delivery_backlog", "utilization", "revenue_margin_conversion"], "stage4b_evidence_fields": ["test_theme_MFE_without_customer_bridge", "valuation_blowoff", "post_peak_drawdown"], "stage4c_evidence_fields": ["hard_order_loss_or_customer_acceptance_break_watch_only"], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/089/089030/2024.csv", "profile_path": "atlas/symbol_profiles/089/089030.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "entry_date": "2024-02-13", "entry_price": 18690, "MFE_30D_pct": 92.62, "MFE_90D_pct": 244.03, "MFE_180D_pct": 278.81, "MFE_1Y_pct": null, "MFE_2Y_pct": null, "MAE_30D_pct": -6.04, "MAE_90D_pct": -6.04, "MAE_180D_pct": -6.04, "MAE_1Y_pct": null, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2024-07-11", "peak_price": 70800, "drawdown_after_peak_pct": -57.63, "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": 0.95, "four_b_full_window_peak_proximity": 0.85, "four_b_timing_verdict": "local_4B_watch_required_when_HBM_test_MFE_outruns_order_customer_quality_revenue_bridge", "four_b_evidence_type": ["test_MFE_without_customer_bridge", "post_peak_drawdown", "source_proxy_gap"], "four_c_protection_label": "hard_4C_requires_non_price_order_loss_or_customer_acceptance_break", "trigger_outcome_label": "extreme_positive_MFE_but_local_4B_required_after_test_equipment_blowoff", "current_profile_verdict": "current_profile_4B_too_late_after_extreme_test_equipment_MFE", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_2024_window_after_old_2022_CA_candidate", "same_entry_group_id": "R2L85-C08-01", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R2L85-C08-01", "trigger_id": "R2L85-C08-01-S2A-20240213", "symbol": "089030", "large_sector_id": "L2_AI_SEMICONDUCTOR_ELECTRONICS", "canonical_archetype_id": "C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY", "raw_component_scores_before": {"customer_quality_score": 55, "named_order_score": 45, "delivery_backlog_score": 45, "utilization_score": 40, "revenue_bridge_score": 45, "gross_margin_bridge_score": 40, "revision_score": 50, "relative_strength_score": 80, "valuation_blowoff_risk_score": 85, "execution_risk_score": 45, "source_quality_score": 20, "4B_watch_score": 45}, "weighted_score_before": 84, "stage_label_before": "Stage2-Actionable", "raw_component_scores_after": {"customer_quality_score": 55, "named_order_score": 45, "delivery_backlog_score": 45, "utilization_score": 40, "revenue_bridge_score": 45, "gross_margin_bridge_score": 40, "revision_score": 50, "relative_strength_score": 80, "valuation_blowoff_risk_score": 90, "execution_risk_score": 55, "source_quality_score": 10, "4B_watch_score": 90}, "weighted_score_after": 79, "stage_label_after": "Stage2-Actionable + local 4B/customer-quality watch", "changed_components": ["customer_quality_score", "named_order_score", "delivery_backlog_score", "utilization_score", "revenue_bridge_score", "gross_margin_bridge_score", "source_quality_score", "4B_watch_score"], "component_delta_explanation": "C08 requires test/socket/customer-quality signal to convert into named order, customer acceptance, delivery, utilization and revenue/margin bridge before clean Stage2/Green; test-theme MFE alone is demoted or wrapped with local 4B watch.", "MFE_90D_pct": 244.03, "MAE_90D_pct": -6.04, "score_return_alignment_label": "extreme_positive_MFE_but_local_4B_required_after_test_equipment_blowoff", "current_profile_verdict": "current_profile_4B_too_late_after_extreme_test_equipment_MFE"}
{"row_type": "case", "case_id": "R2L85-C08-02", "symbol": "330860", "company_name": "네패스아크", "round": "R2", "loop": 85, "large_sector_id": "L2_AI_SEMICONDUCTOR_ELECTRONICS", "canonical_archetype_id": "C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY", "fine_archetype_id": "HBM_TEST_HANDLER_PROBE_CARD_OSAT_CUSTOMER_QUALITY_REVENUE_BRIDGE_VS_TEST_THEME_BLOWOFF_FADE", "case_type": "OSAT_test_capacity_theme_blowoff_false_positive", "positive_or_counterexample": "counterexample", "best_trigger": "R2L85-C08-02-S2FP-20240221", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "short_MFE_deep_MAE_test_theme_false_positive", "current_profile_verdict": "current_profile_false_positive_high_MAE_4B_late", "price_source": "Songdaiki/stock-web", "notes": "OSAT/test capacity MFE is not durable C08 evidence unless customer-quality, utilization and revenue/margin conversion are visible at entry."}
{"row_type": "trigger", "trigger_id": "R2L85-C08-02-S2FP-20240221", "case_id": "R2L85-C08-02", "symbol": "330860", "company_name": "네패스아크", "round": "R2", "loop": 85, "large_sector_id": "L2_AI_SEMICONDUCTOR_ELECTRONICS", "canonical_archetype_id": "C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY", "fine_archetype_id": "HBM_TEST_HANDLER_PROBE_CARD_OSAT_CUSTOMER_QUALITY_REVENUE_BRIDGE_VS_TEST_THEME_BLOWOFF_FADE", "loop_objective": "coverage_gap_fill|counterexample_mining|semi_test_socket_customer_quality_guardrail|local_4B_timing_after_test_MFE|canonical_archetype_compression", "trigger_type": "Stage2-FalsePositive", "trigger_date": "2024-02-21", "evidence_available_at_that_date": "system-semi test / OSAT capacity and AI-test theme proxy without durable customer-quality and revenue bridge", "evidence_source": "source_proxy_only; evidence_url_pending", "stage2_evidence_fields": ["customer_quality_proxy", "test_handler_or_probe_card_proxy", "named_order_or_acceptance_proxy"], "stage3_evidence_fields": ["named_customer", "tool_acceptance", "delivery_backlog", "utilization", "revenue_margin_conversion"], "stage4b_evidence_fields": ["test_theme_MFE_without_customer_bridge", "valuation_blowoff", "post_peak_drawdown"], "stage4c_evidence_fields": ["hard_order_loss_or_customer_acceptance_break_watch_only"], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/330/330860/2024.csv", "profile_path": "atlas/symbol_profiles/330/330860.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "entry_date": "2024-02-21", "entry_price": 36900, "MFE_30D_pct": 25.75, "MFE_90D_pct": 25.75, "MFE_180D_pct": 25.75, "MFE_1Y_pct": null, "MFE_2Y_pct": null, "MAE_30D_pct": -12.47, "MAE_90D_pct": -42.68, "MAE_180D_pct": -67.48, "MAE_1Y_pct": null, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2024-03-12", "peak_price": 46400, "drawdown_after_peak_pct": -74.14, "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": 0.35, "four_b_full_window_peak_proximity": 0.3, "four_b_timing_verdict": "test_capacity_theme_MFE_rejected_without_customer_acceptance_revenue_margin_bridge", "four_b_evidence_type": ["test_MFE_without_customer_bridge", "post_peak_drawdown", "source_proxy_gap"], "four_c_protection_label": "hard_4C_requires_non_price_order_loss_or_customer_acceptance_break", "trigger_outcome_label": "short_MFE_deep_MAE_test_theme_false_positive", "current_profile_verdict": "current_profile_false_positive_high_MAE_4B_late", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window_no_profile_CA_candidate", "same_entry_group_id": "R2L85-C08-02", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R2L85-C08-02", "trigger_id": "R2L85-C08-02-S2FP-20240221", "symbol": "330860", "large_sector_id": "L2_AI_SEMICONDUCTOR_ELECTRONICS", "canonical_archetype_id": "C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY", "raw_component_scores_before": {"customer_quality_score": 20, "named_order_score": 5, "delivery_backlog_score": 10, "utilization_score": 15, "revenue_bridge_score": 10, "gross_margin_bridge_score": 5, "revision_score": 15, "relative_strength_score": 45, "valuation_blowoff_risk_score": 75, "execution_risk_score": 75, "source_quality_score": 15, "4B_watch_score": 70}, "weighted_score_before": 58, "stage_label_before": "Stage2-Watch/FalsePositive", "raw_component_scores_after": {"customer_quality_score": 5, "named_order_score": 0, "delivery_backlog_score": 0, "utilization_score": 5, "revenue_bridge_score": 0, "gross_margin_bridge_score": 0, "revision_score": 15, "relative_strength_score": 45, "valuation_blowoff_risk_score": 75, "execution_risk_score": 85, "source_quality_score": 5, "4B_watch_score": 85}, "weighted_score_after": 45, "stage_label_after": "Rejected-Stage2 / Test-theme RiskWatch", "changed_components": ["customer_quality_score", "named_order_score", "delivery_backlog_score", "utilization_score", "revenue_bridge_score", "gross_margin_bridge_score", "source_quality_score", "4B_watch_score"], "component_delta_explanation": "C08 requires test/socket/customer-quality signal to convert into named order, customer acceptance, delivery, utilization and revenue/margin bridge before clean Stage2/Green; test-theme MFE alone is demoted or wrapped with local 4B watch.", "MFE_90D_pct": 25.75, "MAE_90D_pct": -42.68, "score_return_alignment_label": "short_MFE_deep_MAE_test_theme_false_positive", "current_profile_verdict": "current_profile_false_positive_high_MAE_4B_late"}
{"row_type": "case", "case_id": "R2L85-C08-03", "symbol": "252990", "company_name": "샘씨엔에스", "round": "R2", "loop": 85, "large_sector_id": "L2_AI_SEMICONDUCTOR_ELECTRONICS", "canonical_archetype_id": "C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY", "fine_archetype_id": "HBM_TEST_HANDLER_PROBE_CARD_OSAT_CUSTOMER_QUALITY_REVENUE_BRIDGE_VS_TEST_THEME_BLOWOFF_FADE", "case_type": "probe_card_customer_quality_theme_fade", "positive_or_counterexample": "counterexample", "best_trigger": "R2L85-C08-03-S2FP-20240123", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "early_theme_MFE_later_high_MAE_false_positive", "current_profile_verdict": "current_profile_false_positive_theme_MFE_fade", "price_source": "Songdaiki/stock-web", "notes": "Probe-card/customer-quality theme heat should remain RiskWatch unless customer reorder, utilization, ASP and gross-margin bridge are repaired."}
{"row_type": "trigger", "trigger_id": "R2L85-C08-03-S2FP-20240123", "case_id": "R2L85-C08-03", "symbol": "252990", "company_name": "샘씨엔에스", "round": "R2", "loop": 85, "large_sector_id": "L2_AI_SEMICONDUCTOR_ELECTRONICS", "canonical_archetype_id": "C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY", "fine_archetype_id": "HBM_TEST_HANDLER_PROBE_CARD_OSAT_CUSTOMER_QUALITY_REVENUE_BRIDGE_VS_TEST_THEME_BLOWOFF_FADE", "loop_objective": "coverage_gap_fill|counterexample_mining|semi_test_socket_customer_quality_guardrail|local_4B_timing_after_test_MFE|canonical_archetype_compression", "trigger_type": "Stage2-FalsePositive", "trigger_date": "2024-01-23", "evidence_available_at_that_date": "probe-card / ceramic substrate / test customer-quality theme proxy without confirmed reorder and margin bridge", "evidence_source": "source_proxy_only; evidence_url_pending", "stage2_evidence_fields": ["customer_quality_proxy", "test_handler_or_probe_card_proxy", "named_order_or_acceptance_proxy"], "stage3_evidence_fields": ["named_customer", "tool_acceptance", "delivery_backlog", "utilization", "revenue_margin_conversion"], "stage4b_evidence_fields": ["test_theme_MFE_without_customer_bridge", "valuation_blowoff", "post_peak_drawdown"], "stage4c_evidence_fields": ["hard_order_loss_or_customer_acceptance_break_watch_only"], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/252/252990/2024.csv", "profile_path": "atlas/symbol_profiles/252/252990.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "entry_date": "2024-01-23", "entry_price": 6860, "MFE_30D_pct": 28.86, "MFE_90D_pct": 28.86, "MFE_180D_pct": 28.86, "MFE_1Y_pct": null, "MFE_2Y_pct": null, "MAE_30D_pct": -6.99, "MAE_90D_pct": -15.74, "MAE_180D_pct": -30.76, "MAE_1Y_pct": null, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2024-02-07", "peak_price": 8840, "drawdown_after_peak_pct": -46.27, "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": 0.35, "four_b_full_window_peak_proximity": 0.3, "four_b_timing_verdict": "probe_card_theme_MFE_rejected_without_customer_reorder_margin_bridge", "four_b_evidence_type": ["test_MFE_without_customer_bridge", "post_peak_drawdown", "source_proxy_gap"], "four_c_protection_label": "hard_4C_requires_non_price_order_loss_or_customer_acceptance_break", "trigger_outcome_label": "early_theme_MFE_later_high_MAE_false_positive", "current_profile_verdict": "current_profile_false_positive_theme_MFE_fade", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_2024_window_no_profile_CA_candidate", "same_entry_group_id": "R2L85-C08-03", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R2L85-C08-03", "trigger_id": "R2L85-C08-03-S2FP-20240123", "symbol": "252990", "large_sector_id": "L2_AI_SEMICONDUCTOR_ELECTRONICS", "canonical_archetype_id": "C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY", "raw_component_scores_before": {"customer_quality_score": 20, "named_order_score": 5, "delivery_backlog_score": 10, "utilization_score": 15, "revenue_bridge_score": 10, "gross_margin_bridge_score": 5, "revision_score": 15, "relative_strength_score": 45, "valuation_blowoff_risk_score": 75, "execution_risk_score": 75, "source_quality_score": 15, "4B_watch_score": 70}, "weighted_score_before": 58, "stage_label_before": "Stage2-Watch/FalsePositive", "raw_component_scores_after": {"customer_quality_score": 5, "named_order_score": 0, "delivery_backlog_score": 0, "utilization_score": 5, "revenue_bridge_score": 0, "gross_margin_bridge_score": 0, "revision_score": 15, "relative_strength_score": 45, "valuation_blowoff_risk_score": 75, "execution_risk_score": 85, "source_quality_score": 5, "4B_watch_score": 85}, "weighted_score_after": 45, "stage_label_after": "Rejected-Stage2 / Test-theme RiskWatch", "changed_components": ["customer_quality_score", "named_order_score", "delivery_backlog_score", "utilization_score", "revenue_bridge_score", "gross_margin_bridge_score", "source_quality_score", "4B_watch_score"], "component_delta_explanation": "C08 requires test/socket/customer-quality signal to convert into named order, customer acceptance, delivery, utilization and revenue/margin bridge before clean Stage2/Green; test-theme MFE alone is demoted or wrapped with local 4B watch.", "MFE_90D_pct": 28.86, "MAE_90D_pct": -15.74, "score_return_alignment_label": "early_theme_MFE_later_high_MAE_false_positive", "current_profile_verdict": "current_profile_false_positive_theme_MFE_fade"}
{"row_type": "shadow_weight", "axis": "C08_customer_quality_order_acceptance_revenue_margin_bridge_required", "scope": "canonical_archetype_specific", "large_sector_id": "L2_AI_SEMICONDUCTOR_ELECTRONICS", "canonical_archetype_id": "C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY", "baseline_value": 0, "tested_value": 1, "delta": "+1", "reason": "Semi test/socket rerating requires named customer quality, order/acceptance, delivery backlog, utilization and revenue/margin bridge; test-theme MFE without bridge fades into high MAE or needs local 4B watch.", "backtest_effect": "keeps 089030 with local 4B/customer-quality watch; demotes 330860/252990 test-theme false positives", "trigger_ids": "R2L85-C08-01-S2A-20240213|R2L85-C08-02-S2FP-20240221|R2L85-C08-03-S2FP-20240123", "calibration_usable_count": 3, "new_independent_case_count": 3, "counterexample_count": 2, "confidence": "low", "proposal_type": "canonical_shadow_only", "notes": "source_proxy_only/evidence_url_pending; not production"}
{"row_type": "residual_contribution", "round": "R2", "loop": 85, "large_sector_id": "L2_AI_SEMICONDUCTOR_ELECTRONICS", "canonical_archetype_id": "C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY", "new_independent_case_count": 3, "reused_case_count": 0, "new_symbol_count": 3, "new_trigger_family_count": 3, "tested_existing_calibrated_axes": ["stage2_actionable_evidence_bonus", "price_only_blowoff_blocks_positive_stage", "full_4b_requires_non_price_evidence", "hard_4c_thesis_break_routes_to_4c", "source_proxy_only_blocks_runtime_promotion", "high_MAE_guardrail", "local_4B_watch_before_full_4B_when_MFE_outruns_bridge"], "residual_error_types_found": ["semi_test_theme_false_positive_high_MAE", "customer_quality_order_acceptance_revenue_margin_bridge_required", "local_4B_late_after_test_equipment_MFE", "source_proxy_runtime_promotion_risk", "high_MAE_positive_Green_blocker"], "loop_contribution_label": "canonical_archetype_rule_candidate", "do_not_propose_new_weight_delta": true}
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
- For C08, test a canonical-archetype guard requiring named customer quality, order/acceptance, delivery backlog, utilization and revenue/gross-margin conversion before clean Stage2/Green.

## 27. Next Round State

```text
completed_round = R2
completed_loop = 85
next_round = R3
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
