# E2R Stock-Web v12 Residual Research — R1 Loop 86 / L1 / C04

## 0. Research Metadata

```json
{
  "research_session": "post_calibrated_sector_archetype_residual_research",
  "mode": "historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12",
  "scheduled_round": "R1",
  "scheduled_loop": 86,
  "round_schedule_status": "valid",
  "round_sector_consistency": "pass",
  "completed_round": "R1",
  "completed_loop": 86,
  "computed_next_round": "R2",
  "computed_next_loop": 86,
  "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID",
  "canonical_archetype_id": "C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY",
  "fine_archetype_id": "CZECH_NUCLEAR_POLICY_PROJECT_EQUIPMENT_SUPPLY_LEGAL_DELAY_MARGIN_BRIDGE_VS_NUCLEAR_THEME_FADE",
  "loop_objective": [
    "coverage_gap_fill",
    "counterexample_mining",
    "nuclear_policy_project_legal_delay_guardrail",
    "nuclear_project_award_to_order_margin_bridge_test",
    "policy_theme_spike_vs_named_order_project_margin_bridge_test",
    "local_4B_timing_after_nuclear_policy_MFE",
    "hard_4C_non_price_project_or_legal_break_protection",
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
scheduled_round = R1
scheduled_loop = 86
allowed_large_sector = L1_INDUSTRIALS_INFRA_DEFENSE_GRID
selected_large_sector = L1_INDUSTRIALS_INFRA_DEFENSE_GRID
selected_canonical_archetype_id = C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY
computed_next_round = R2
computed_next_loop = 86
round_schedule_status = valid
round_sector_consistency = pass
```

R1 restarts loop86 after loop85 R13 completed. This run selects C04 because loop85 R1 used C01 and loop84 R1 used C05. C04 is also a cleaner R1 redteam bucket because policy/project headlines can generate MFE before named orders, legal clearance and project-margin economics are visible.

The tested mechanism:

```text
nuclear policy / project award headline
→ named supplier or equipment/service scope
→ legal clearance and project schedule
→ delivery / backlog conversion
→ gross or OP margin bridge
→ durable rerating or nuclear-theme fade
```

C04 is the reactor building permit. The headline can light the control room, but the rerating needs the contract, the legal path and the margin bridge.

## 3. Previous Coverage / Duplicate Avoidance Check

No-Repeat is used only as a duplicate ledger.

```text
hard_duplicate_key = canonical_archetype_id + symbol + trigger_type + entry_date
```

C04 top-covered symbols include `032820`, `094820`, `105840`, `006910`, `034020`, and `052690`. This run avoids that top-covered set and also avoids recent loop85 R1 C01 and loop84 R1 C05 symbols.

```text
selected_loop86_symbols = 083650 / 011700 / 046120
```

All three are treated as new independent C04 nuclear policy / project legal-delay cases for this loop. No hard duplicate is intentionally reused.

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
| 083650 | 비에이치아이 | `atlas/symbol_profiles/083/083650.json` | old CA candidates through 2015; selected 2024/2025 forward window clean |
| 011700 | 한신기계 | `atlas/symbol_profiles/011/011700.json` | old CA candidates through 2006; selected 2024/2025 forward window clean |
| 046120 | 오르비텍 | `atlas/symbol_profiles/046/046120.json` | old 2017 CA candidate; selected 2024/2025 forward window clean |

## 5. Historical Eligibility Gate

| case_id | symbol | entry_date | entry_price | forward window | 180D status | calibration_usable |
|---|---:|---|---:|---:|---|---|
| R1L86-C04-01 | 083650 | 2024-07-18 | 8,810 | 180D | clean | true |
| R1L86-C04-02 | 011700 | 2024-07-18 | 4,585 | 180D | clean | true |
| R1L86-C04-03 | 046120 | 2024-07-18 | 2,795 | 180D | clean | true |

## 6. Canonical Archetype Compression Map

| canonical_archetype_id | fine/deep route | keep / reject logic |
|---|---|---|
| C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY | NUCLEAR_EQUIPMENT_PROJECT_AWARD_DELAYED_MFE | keep Stage2 only with named order scope, legal clearance, delivery schedule and margin bridge; add local 4B watch |
| C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY | NUCLEAR_COMPRESSOR_EQUIPMENT_THEME_FADE | reject high-MAE equipment theme MFE without supplier scope and margin bridge |
| C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY | NUCLEAR_INSPECTION_SERVICE_THEME_FADE | reject service/safety theme MFE without recurring contract and project linkage |

## 7. Case Selection Summary

| case_id | symbol | company | trigger_type | entry_date | entry_price | MFE_180D_pct | MAE_180D_pct | current_profile_verdict |
|---|---:|---|---|---|---:|---:|---:|---|
| R1L86-C04-01 | 083650 | 비에이치아이 | Stage2-Actionable | 2024-07-18 | 8,810 | 181.5 | -20.54 | current_profile_partially_correct_delayed_MFE_local_4B_watch_needed |
| R1L86-C04-02 | 011700 | 한신기계 | Stage2-FalsePositive | 2024-07-18 | 4,585 | 14.94 | -48.53 | current_profile_false_positive_high_MAE_4B_too_late |
| R1L86-C04-03 | 046120 | 오르비텍 | Stage2-FalsePositive | 2024-07-18 | 2,795 | 14.49 | -28.94 | current_profile_false_positive_high_MAE |

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

This MD creates a source-repair queue and a C04 nuclear-policy shadow guardrail candidate. It must not be promoted directly into runtime weights until a later source-repair pass attaches primary evidence URLs: policy/project award source, named supplier or package scope, legal-clearance status, project schedule, delivery/backlog conversion, customer quality, margin bridge, company disclosure or report evidence.

## 10. Price Data Source Map

| symbol | shard path | profile path |
|---|---|---|
| 083650 | `atlas/ohlcv_tradable_by_symbol_year/083/083650/2024.csv` and `2025.csv` | `atlas/symbol_profiles/083/083650.json` |
| 011700 | `atlas/ohlcv_tradable_by_symbol_year/011/011700/2024.csv` and `2025.csv` | `atlas/symbol_profiles/011/011700.json` |
| 046120 | `atlas/ohlcv_tradable_by_symbol_year/046/046120/2024.csv` and `2025.csv` | `atlas/symbol_profiles/046/046120.json` |

## 11. Case-by-Case Trigger Grid

### Case 1 — 083650 / 비에이치아이

C04 nuclear-equipment project-award positive with delayed MFE. The July policy event first produced a same-day spike and then a sharp drawdown, but the delayed 2025 project/equipment rerating generated a much larger MFE. This is a positive row, but not a clean Green row at entry because named order, legal clearance, schedule and margin evidence are still source-proxy only.

### Case 2 — 011700 / 한신기계

C04 nuclear-compressor equipment theme false positive. The same-day MFE was tradable, but the later MAE and post-peak drawdown were severe. This should be rejected unless supplier scope, delivery timing and project-margin economics are source-repaired.

### Case 3 — 046120 / 오르비텍

C04 nuclear inspection / safety-service theme false positive. The entry day produced a policy spike, but there was no durable follow-through. Safety-service theme MFE is not enough without direct project linkage, recurring contract and margin bridge.

## 12. Trigger-Level OHLC Backtest Tables

| symbol | entry | MFE30 | MAE30 | MFE90 | MAE90 | MFE180 | MAE180 | peak | post-peak DD |
|---|---:|---:|---:|---:|---:|---:|---:|---|---:|
| 083650 | 8,810 | 19.52 | -19.41 | 19.52 | -20.54 | 181.50 | -20.54 | 2025-02-14 / 24,800 | -38.43 |
| 011700 | 4,585 | 14.94 | -32.82 | 14.94 | -32.82 | 14.94 | -48.53 | 2024-07-18 / 5,270 | -55.22 |
| 046120 | 2,795 | 14.49 | -27.01 | 14.49 | -27.01 | 14.49 | -28.94 | 2024-07-18 / 3,200 | -37.94 |

## 13. Current Calibrated Profile Stress Test

| case_id | P0 likely behavior | actual path | verdict |
|---|---|---|---|
| R1L86-C04-01 | Stage2-Actionable if project/order bridge exists | delayed huge MFE after early drawdown | partially correct; local 4B and source repair needed |
| R1L86-C04-02 | risk of treating nuclear equipment theme as Stage2 | same-day MFE / deep MAE | false positive |
| R1L86-C04-03 | risk of treating inspection/safety theme as Stage2 | same-day MFE / high MAE | false positive |

## 14. Stage2 / Yellow / Green Comparison

```text
green_lateness_ratio = not_applicable
reason = no confirmed Stage3-Green trigger is assigned in this residual MD
```

For C04, the residual is not Green lateness. The residual is whether nuclear policy/project MFE becomes clean Stage2/Green before named order, legal clearance, schedule and margin bridge are proven.

## 15. 4B Local vs Full-window Timing Audit

| case_id | local proximity | full-window proximity | verdict |
|---|---:|---:|---|
| R1L86-C04-01 | 0.82 | 0.72 | local 4B watch after nuclear project MFE if named-order/legal/margin bridge stalls |
| R1L86-C04-02 | 0.35 | 0.30 | nuclear-equipment theme MFE rejected without named order/schedule/margin bridge |
| R1L86-C04-03 | 0.35 | 0.30 | nuclear-service theme rejected without project contract/legal/margin bridge |

## 16. 4C Protection Audit

No hard 4C is promoted from this file.

```text
four_c_protection_label = hard_4C_requires_non_price_project_cancel_legal_block_or_order_loss
hard_4c_price_only_allowed = false
```

Price drawdown alone is not hard 4C. C04 hard 4C requires confirmed project cancellation, legal block, tender loss, supplier-scope exclusion, order loss, schedule slip or margin thesis break.

## 17. Sector-Specific Rule Candidate

```text
rule_scope = no_new_global_rule
sector_specific_rule_candidate = L1/C04 nuclear rows need named order scope, legal clearance, project schedule, backlog conversion and margin bridge before clean Stage2/Green
confidence = low
reason = all evidence rows are source_proxy_only / evidence_url_pending
```

## 18. Canonical-Archetype Rule Candidate

```text
canonical_archetype_id = C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY
candidate_axis = C04_nuclear_policy_project_named_order_legal_margin_bridge_required
effect = keep delayed-MFE nuclear equipment positive with local 4B watch; demote theme-only false positives
production_scoring_changed = false
shadow_weight_only = true
do_not_propose_new_weight_delta = true
```

## 19. Before / After Backtest Comparison

| profile | eligible triggers | avg MFE90 | avg MAE90 | false-positive behavior | verdict |
|---|---:|---:|---:|---|---|
| P0 e2r_2_1_stock_web_calibrated_proxy | 3 | 16.32 | -26.79 | may over-credit nuclear policy/equipment theme MFE | needs C04 project/legal/margin bridge repair |
| P1 canonical shadow bridge profile | 3 | 181.50 on delayed kept positive at 180D | demotes 011700/046120 | keeps hard 4C non-price requirement | better alignment, source repair required |

## 20. Score-Return Alignment Matrix

| case_id | weighted before | label before | weighted after | label after | alignment |
|---|---:|---|---:|---|---|
| R1L86-C04-01 | 76 | Stage2-Actionable | 72 | Stage2-Actionable + local 4B/nuclear-project bridge watch | partially aligned |
| R1L86-C04-02 | 58 | Stage2-Watch/FalsePositive | 44 | Rejected-Stage2 / Nuclear-policy theme RiskWatch | improved |
| R1L86-C04-03 | 58 | Stage2-Watch/FalsePositive | 44 | Rejected-Stage2 / Nuclear-policy theme RiskWatch | improved |

## 21. Coverage Matrix

| large_sector_id | canonical_archetype_id | fine_archetype_id | positive | counterexample | 4B | 4C | new cases | reused | usable triggers | current errors | sector rule | canonical rule | coverage gap after |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---|---|---|
| L1_INDUSTRIALS_INFRA_DEFENSE_GRID | C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY | CZECH_NUCLEAR_POLICY_PROJECT_EQUIPMENT_SUPPLY_LEGAL_DELAY_MARGIN_BRIDGE_VS_NUCLEAR_THEME_FADE | 1 | 2 | 3-watch | 0-hard | 3 | 0 | 3 | 2 | no | yes | source repair needed |

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
  - nuclear_policy_theme_false_positive_high_MAE
  - named_order_legal_clearance_margin_bridge_required
  - delayed_MFE_positive_needs_local_4B_watch
  - source_proxy_runtime_promotion_risk
  - hard_4C_requires_non_price_project_or_legal_break
new_axis_proposed: false
existing_axis_strengthened:
  - C04_nuclear_policy_project_named_order_legal_margin_bridge_required
  - source_proxy_only_blocks_runtime_promotion
  - local_4B_watch_before_full_4B_when_MFE_outruns_bridge
  - hard_4C_requires_non_price_thesis_break
existing_axis_weakened: null
existing_axis_kept:
  - full_4b_requires_non_price_evidence
  - hard_4c_thesis_break_routes_to_4c
sector_specific_rule_candidate: null
canonical_archetype_rule_candidate: C04_nuclear_policy_project_named_order_legal_margin_bridge_required
no_new_signal_reason: null
loop_contribution_label: canonical_archetype_rule_candidate
do_not_propose_new_weight_delta: true
```

This loop adds 3 new independent cases, 2 counterexamples, and 2 residual errors for R1/L1_INDUSTRIALS_INFRA_DEFENSE_GRID/C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY.

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
- named order or supplier package scope
- legal-clearance path and project schedule
- delivery/backlog conversion
- gross/OP margin conversion
- production scoring implementation
```

## 24. Shadow Weight Calibration

```csv
row_type,axis,scope,large_sector_id,canonical_archetype_id,baseline_value,tested_value,delta,reason,backtest_effect,trigger_ids,calibration_usable_count,new_independent_case_count,counterexample_count,confidence,proposal_type,notes
shadow_weight,C04_nuclear_policy_project_named_order_legal_margin_bridge_required,canonical_archetype_specific,L1_INDUSTRIALS_INFRA_DEFENSE_GRID,C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY,0,1,+1,"Require named order scope, legal clearance, delivery schedule, backlog conversion and margin bridge before clean Stage2/Green","keeps 083650 with delayed-MFE local 4B watch; demotes 011700/046120","R1L86-C04-01-S2A-20240718|R1L86-C04-02-S2FP-20240718|R1L86-C04-03-S2FP-20240718",3,3,2,low,canonical_shadow_only,"source repair required; not production"
```

## 25. Machine-Readable Rows

```jsonl
{"row_type": "price_source_validation", "source": "Songdaiki/stock-web", "source_url": "https://github.com/Songdaiki/stock-web", "manifest_path": "atlas/manifest.json", "schema_path": "atlas/schema.json", "universe_path": "atlas/universe/all_symbols.csv", "manifest_max_date": "2026-02-20", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "raw_shard_root": "atlas/ohlcv_raw_by_symbol_year", "validation_status": "usable_for_historical_calibration"}
{"row_type": "case", "case_id": "R1L86-C04-01", "symbol": "083650", "company_name": "비에이치아이", "round": "R1", "loop": 86, "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "canonical_archetype_id": "C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY", "fine_archetype_id": "CZECH_NUCLEAR_POLICY_PROJECT_EQUIPMENT_SUPPLY_LEGAL_DELAY_MARGIN_BRIDGE_VS_NUCLEAR_THEME_FADE", "case_type": "nuclear_equipment_project_award_positive_with_delayed_MFE_and_local_4B_watch", "positive_or_counterexample": "positive", "best_trigger": "R1L86-C04-01-S2A-20240718", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "delayed_large_MFE_but_project_legal_margin_bridge_required", "current_profile_verdict": "current_profile_partially_correct_delayed_MFE_local_4B_watch_needed", "price_source": "Songdaiki/stock-web", "notes": "C04 positives can survive delayed MFE, but only when policy/project award converts into named supply scope, legal clearance, schedule and margin bridge."}
{"row_type": "trigger", "trigger_id": "R1L86-C04-01-S2A-20240718", "case_id": "R1L86-C04-01", "symbol": "083650", "company_name": "비에이치아이", "round": "R1", "loop": 86, "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "canonical_archetype_id": "C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY", "fine_archetype_id": "CZECH_NUCLEAR_POLICY_PROJECT_EQUIPMENT_SUPPLY_LEGAL_DELAY_MARGIN_BRIDGE_VS_NUCLEAR_THEME_FADE", "loop_objective": "coverage_gap_fill|counterexample_mining|nuclear_policy_project_legal_delay_guardrail|project_award_to_order_margin_bridge|canonical_archetype_compression", "trigger_type": "Stage2-Actionable", "trigger_date": "2024-07-18", "evidence_available_at_that_date": "Czech nuclear project / nuclear equipment / project award policy-event proxy; primary named order, legal-clearance and margin evidence pending", "evidence_source": "source_proxy_only; evidence_url_pending", "stage2_evidence_fields": ["nuclear_policy_award_proxy", "project_beneficiary_proxy", "equipment_or_service_scope_proxy"], "stage3_evidence_fields": ["named_order_scope", "legal_clearance", "delivery_schedule", "customer_quality", "backlog_conversion", "gross_or_OP_margin_bridge"], "stage4b_evidence_fields": ["nuclear_policy_MFE_without_order_bridge", "legal_delay_or_theme_blowoff", "post_peak_drawdown"], "stage4c_evidence_fields": ["hard_project_cancel_legal_block_or_order_loss_watch_only"], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/083/083650/2024.csv", "profile_path": "atlas/symbol_profiles/083/083650.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "entry_date": "2024-07-18", "entry_price": 8810, "MFE_30D_pct": 19.52, "MFE_90D_pct": 19.52, "MFE_180D_pct": 181.5, "MFE_1Y_pct": null, "MFE_2Y_pct": null, "MAE_30D_pct": -19.41, "MAE_90D_pct": -20.54, "MAE_180D_pct": -20.54, "MAE_1Y_pct": null, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2025-02-14", "peak_price": 24800, "drawdown_after_peak_pct": -38.43, "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": 0.82, "four_b_full_window_peak_proximity": 0.72, "four_b_timing_verdict": "local_4B_watch_after_nuclear_project_MFE_if_named_order_legal_margin_bridge_stalls", "four_b_evidence_type": ["nuclear_policy_MFE_without_order_margin_bridge", "post_peak_drawdown", "source_proxy_gap"], "four_c_protection_label": "hard_4C_requires_non_price_project_cancel_legal_block_or_order_loss", "trigger_outcome_label": "delayed_large_MFE_but_project_legal_margin_bridge_required", "current_profile_verdict": "current_profile_partially_correct_delayed_MFE_local_4B_watch_needed", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_2024_2025_window_after_old_2015_CA_candidates", "same_entry_group_id": "R1L86-C04-01", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R1L86-C04-01", "trigger_id": "R1L86-C04-01-S2A-20240718", "symbol": "083650", "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "canonical_archetype_id": "C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY", "raw_component_scores_before": {"policy_project_specificity_score": 55, "named_order_scope_score": 40, "legal_clearance_score": 35, "delivery_schedule_score": 35, "customer_quality_score": 45, "margin_bridge_score": 35, "backlog_conversion_score": 40, "revision_score": 40, "relative_strength_score": 70, "theme_blowoff_risk_score": 75, "execution_risk_score": 65, "source_quality_score": 20, "4B_watch_score": 45, "4C_watch_score": 25}, "weighted_score_before": 76, "stage_label_before": "Stage2-Actionable", "raw_component_scores_after": {"policy_project_specificity_score": 55, "named_order_scope_score": 40, "legal_clearance_score": 35, "delivery_schedule_score": 35, "customer_quality_score": 45, "margin_bridge_score": 35, "backlog_conversion_score": 40, "revision_score": 40, "relative_strength_score": 70, "theme_blowoff_risk_score": 85, "execution_risk_score": 75, "source_quality_score": 10, "4B_watch_score": 85, "4C_watch_score": 25}, "weighted_score_after": 72, "stage_label_after": "Stage2-Actionable + local 4B/nuclear-project bridge watch", "changed_components": ["named_order_scope_score", "legal_clearance_score", "delivery_schedule_score", "margin_bridge_score", "backlog_conversion_score", "source_quality_score", "execution_risk_score", "4B_watch_score", "4C_watch_score"], "component_delta_explanation": "C04 requires nuclear policy/project event to convert into named order scope, legal clearance, delivery schedule, backlog conversion and margin bridge before clean Stage2/Green; theme MFE alone is demoted or wrapped with local 4B/high-MAE watch.", "MFE_90D_pct": 19.52, "MAE_90D_pct": -20.54, "score_return_alignment_label": "delayed_large_MFE_but_project_legal_margin_bridge_required", "current_profile_verdict": "current_profile_partially_correct_delayed_MFE_local_4B_watch_needed"}
{"row_type": "case", "case_id": "R1L86-C04-02", "symbol": "011700", "company_name": "한신기계", "round": "R1", "loop": 86, "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "canonical_archetype_id": "C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY", "fine_archetype_id": "CZECH_NUCLEAR_POLICY_PROJECT_EQUIPMENT_SUPPLY_LEGAL_DELAY_MARGIN_BRIDGE_VS_NUCLEAR_THEME_FADE", "case_type": "nuclear_compressor_equipment_theme_spike_high_MAE_false_positive", "positive_or_counterexample": "counterexample", "best_trigger": "R1L86-C04-02-S2FP-20240718", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "same_day_MFE_then_deep_MAE_nuclear_theme_false_positive", "current_profile_verdict": "current_profile_false_positive_high_MAE_4B_too_late", "price_source": "Songdaiki/stock-web", "notes": "Nuclear-equipment theme spikes should not validate Stage2 unless supplier scope, order conversion, delivery timing and margin economics are visible at entry."}
{"row_type": "trigger", "trigger_id": "R1L86-C04-02-S2FP-20240718", "case_id": "R1L86-C04-02", "symbol": "011700", "company_name": "한신기계", "round": "R1", "loop": 86, "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "canonical_archetype_id": "C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY", "fine_archetype_id": "CZECH_NUCLEAR_POLICY_PROJECT_EQUIPMENT_SUPPLY_LEGAL_DELAY_MARGIN_BRIDGE_VS_NUCLEAR_THEME_FADE", "loop_objective": "coverage_gap_fill|counterexample_mining|nuclear_policy_project_legal_delay_guardrail|project_award_to_order_margin_bridge|canonical_archetype_compression", "trigger_type": "Stage2-FalsePositive", "trigger_date": "2024-07-18", "evidence_available_at_that_date": "nuclear equipment / compressor and policy-award theme proxy without named order, legal-clearance, delivery schedule or margin bridge", "evidence_source": "source_proxy_only; evidence_url_pending", "stage2_evidence_fields": ["nuclear_policy_award_proxy", "project_beneficiary_proxy", "equipment_or_service_scope_proxy"], "stage3_evidence_fields": ["named_order_scope", "legal_clearance", "delivery_schedule", "customer_quality", "backlog_conversion", "gross_or_OP_margin_bridge"], "stage4b_evidence_fields": ["nuclear_policy_MFE_without_order_bridge", "legal_delay_or_theme_blowoff", "post_peak_drawdown"], "stage4c_evidence_fields": ["hard_project_cancel_legal_block_or_order_loss_watch_only"], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/011/011700/2024.csv", "profile_path": "atlas/symbol_profiles/011/011700.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "entry_date": "2024-07-18", "entry_price": 4585, "MFE_30D_pct": 14.94, "MFE_90D_pct": 14.94, "MFE_180D_pct": 14.94, "MFE_1Y_pct": null, "MFE_2Y_pct": null, "MAE_30D_pct": -32.82, "MAE_90D_pct": -32.82, "MAE_180D_pct": -48.53, "MAE_1Y_pct": null, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2024-07-18", "peak_price": 5270, "drawdown_after_peak_pct": -55.22, "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": 0.35, "four_b_full_window_peak_proximity": 0.3, "four_b_timing_verdict": "nuclear_equipment_theme_MFE_rejected_without_named_order_schedule_margin_bridge", "four_b_evidence_type": ["nuclear_policy_MFE_without_order_margin_bridge", "post_peak_drawdown", "source_proxy_gap"], "four_c_protection_label": "hard_4C_requires_non_price_project_cancel_legal_block_or_order_loss", "trigger_outcome_label": "same_day_MFE_then_deep_MAE_nuclear_theme_false_positive", "current_profile_verdict": "current_profile_false_positive_high_MAE_4B_too_late", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_2024_2025_window_after_old_2006_CA_candidate", "same_entry_group_id": "R1L86-C04-02", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R1L86-C04-02", "trigger_id": "R1L86-C04-02-S2FP-20240718", "symbol": "011700", "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "canonical_archetype_id": "C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY", "raw_component_scores_before": {"policy_project_specificity_score": 35, "named_order_scope_score": 5, "legal_clearance_score": 5, "delivery_schedule_score": 5, "customer_quality_score": 20, "margin_bridge_score": 5, "backlog_conversion_score": 5, "revision_score": 15, "relative_strength_score": 35, "theme_blowoff_risk_score": 75, "execution_risk_score": 85, "source_quality_score": 15, "4B_watch_score": 80, "4C_watch_score": 45}, "weighted_score_before": 58, "stage_label_before": "Stage2-Watch/FalsePositive", "raw_component_scores_after": {"policy_project_specificity_score": 35, "named_order_scope_score": 0, "legal_clearance_score": 0, "delivery_schedule_score": 0, "customer_quality_score": 20, "margin_bridge_score": 0, "backlog_conversion_score": 0, "revision_score": 15, "relative_strength_score": 35, "theme_blowoff_risk_score": 75, "execution_risk_score": 90, "source_quality_score": 5, "4B_watch_score": 90, "4C_watch_score": 65}, "weighted_score_after": 44, "stage_label_after": "Rejected-Stage2 / Nuclear-policy theme RiskWatch", "changed_components": ["named_order_scope_score", "legal_clearance_score", "delivery_schedule_score", "margin_bridge_score", "backlog_conversion_score", "source_quality_score", "execution_risk_score", "4B_watch_score", "4C_watch_score"], "component_delta_explanation": "C04 requires nuclear policy/project event to convert into named order scope, legal clearance, delivery schedule, backlog conversion and margin bridge before clean Stage2/Green; theme MFE alone is demoted or wrapped with local 4B/high-MAE watch.", "MFE_90D_pct": 14.94, "MAE_90D_pct": -32.82, "score_return_alignment_label": "same_day_MFE_then_deep_MAE_nuclear_theme_false_positive", "current_profile_verdict": "current_profile_false_positive_high_MAE_4B_too_late"}
{"row_type": "case", "case_id": "R1L86-C04-03", "symbol": "046120", "company_name": "오르비텍", "round": "R1", "loop": 86, "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "canonical_archetype_id": "C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY", "fine_archetype_id": "CZECH_NUCLEAR_POLICY_PROJECT_EQUIPMENT_SUPPLY_LEGAL_DELAY_MARGIN_BRIDGE_VS_NUCLEAR_THEME_FADE", "case_type": "nuclear_inspection_safety_policy_theme_high_MAE_counterexample", "positive_or_counterexample": "counterexample", "best_trigger": "R1L86-C04-03-S2FP-20240718", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "policy_theme_MFE_then_high_MAE_project_bridge_false_positive", "current_profile_verdict": "current_profile_false_positive_high_MAE", "price_source": "Songdaiki/stock-web", "notes": "Nuclear safety/inspection service MFE should remain RiskWatch unless recurring contract conversion, direct project linkage and margin bridge are source-repaired."}
{"row_type": "trigger", "trigger_id": "R1L86-C04-03-S2FP-20240718", "case_id": "R1L86-C04-03", "symbol": "046120", "company_name": "오르비텍", "round": "R1", "loop": 86, "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "canonical_archetype_id": "C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY", "fine_archetype_id": "CZECH_NUCLEAR_POLICY_PROJECT_EQUIPMENT_SUPPLY_LEGAL_DELAY_MARGIN_BRIDGE_VS_NUCLEAR_THEME_FADE", "loop_objective": "coverage_gap_fill|counterexample_mining|nuclear_policy_project_legal_delay_guardrail|project_award_to_order_margin_bridge|canonical_archetype_compression", "trigger_type": "Stage2-FalsePositive", "trigger_date": "2024-07-18", "evidence_available_at_that_date": "nuclear inspection / safety-service / policy-award theme proxy without direct project award, recurring contract, legal-clearance or margin bridge", "evidence_source": "source_proxy_only; evidence_url_pending", "stage2_evidence_fields": ["nuclear_policy_award_proxy", "project_beneficiary_proxy", "equipment_or_service_scope_proxy"], "stage3_evidence_fields": ["named_order_scope", "legal_clearance", "delivery_schedule", "customer_quality", "backlog_conversion", "gross_or_OP_margin_bridge"], "stage4b_evidence_fields": ["nuclear_policy_MFE_without_order_bridge", "legal_delay_or_theme_blowoff", "post_peak_drawdown"], "stage4c_evidence_fields": ["hard_project_cancel_legal_block_or_order_loss_watch_only"], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/046/046120/2024.csv", "profile_path": "atlas/symbol_profiles/046/046120.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "entry_date": "2024-07-18", "entry_price": 2795, "MFE_30D_pct": 14.49, "MFE_90D_pct": 14.49, "MFE_180D_pct": 14.49, "MFE_1Y_pct": null, "MFE_2Y_pct": null, "MAE_30D_pct": -27.01, "MAE_90D_pct": -27.01, "MAE_180D_pct": -28.94, "MAE_1Y_pct": null, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2024-07-18", "peak_price": 3200, "drawdown_after_peak_pct": -37.94, "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": 0.35, "four_b_full_window_peak_proximity": 0.3, "four_b_timing_verdict": "nuclear_service_theme_rejected_without_project_contract_legal_margin_bridge", "four_b_evidence_type": ["nuclear_policy_MFE_without_order_margin_bridge", "post_peak_drawdown", "source_proxy_gap"], "four_c_protection_label": "hard_4C_requires_non_price_project_cancel_legal_block_or_order_loss", "trigger_outcome_label": "policy_theme_MFE_then_high_MAE_project_bridge_false_positive", "current_profile_verdict": "current_profile_false_positive_high_MAE", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_2024_2025_window_after_old_2017_CA_candidate", "same_entry_group_id": "R1L86-C04-03", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R1L86-C04-03", "trigger_id": "R1L86-C04-03-S2FP-20240718", "symbol": "046120", "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "canonical_archetype_id": "C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY", "raw_component_scores_before": {"policy_project_specificity_score": 35, "named_order_scope_score": 5, "legal_clearance_score": 5, "delivery_schedule_score": 5, "customer_quality_score": 20, "margin_bridge_score": 5, "backlog_conversion_score": 5, "revision_score": 15, "relative_strength_score": 35, "theme_blowoff_risk_score": 75, "execution_risk_score": 85, "source_quality_score": 15, "4B_watch_score": 80, "4C_watch_score": 45}, "weighted_score_before": 58, "stage_label_before": "Stage2-Watch/FalsePositive", "raw_component_scores_after": {"policy_project_specificity_score": 35, "named_order_scope_score": 0, "legal_clearance_score": 0, "delivery_schedule_score": 0, "customer_quality_score": 20, "margin_bridge_score": 0, "backlog_conversion_score": 0, "revision_score": 15, "relative_strength_score": 35, "theme_blowoff_risk_score": 75, "execution_risk_score": 90, "source_quality_score": 5, "4B_watch_score": 90, "4C_watch_score": 65}, "weighted_score_after": 44, "stage_label_after": "Rejected-Stage2 / Nuclear-policy theme RiskWatch", "changed_components": ["named_order_scope_score", "legal_clearance_score", "delivery_schedule_score", "margin_bridge_score", "backlog_conversion_score", "source_quality_score", "execution_risk_score", "4B_watch_score", "4C_watch_score"], "component_delta_explanation": "C04 requires nuclear policy/project event to convert into named order scope, legal clearance, delivery schedule, backlog conversion and margin bridge before clean Stage2/Green; theme MFE alone is demoted or wrapped with local 4B/high-MAE watch.", "MFE_90D_pct": 14.49, "MAE_90D_pct": -27.01, "score_return_alignment_label": "policy_theme_MFE_then_high_MAE_project_bridge_false_positive", "current_profile_verdict": "current_profile_false_positive_high_MAE"}
{"row_type": "shadow_weight", "axis": "C04_nuclear_policy_project_named_order_legal_margin_bridge_required", "scope": "canonical_archetype_specific", "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "canonical_archetype_id": "C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY", "baseline_value": 0, "tested_value": 1, "delta": "+1", "reason": "Nuclear policy/project rerating requires named order scope, legal clearance, delivery schedule, backlog conversion and margin bridge; nuclear theme MFE without bridge fades into high MAE or needs local 4B watch.", "backtest_effect": "keeps 083650 with delayed-MFE local 4B watch; demotes 011700/046120 nuclear-policy theme false positives", "trigger_ids": "R1L86-C04-01-S2A-20240718|R1L86-C04-02-S2FP-20240718|R1L86-C04-03-S2FP-20240718", "calibration_usable_count": 3, "new_independent_case_count": 3, "counterexample_count": 2, "confidence": "low", "proposal_type": "canonical_shadow_only", "notes": "source_proxy_only/evidence_url_pending; not production"}
{"row_type": "residual_contribution", "round": "R1", "loop": 86, "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "canonical_archetype_id": "C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY", "new_independent_case_count": 3, "reused_case_count": 0, "new_symbol_count": 3, "new_trigger_family_count": 3, "tested_existing_calibrated_axes": ["stage2_actionable_evidence_bonus", "price_only_blowoff_blocks_positive_stage", "full_4b_requires_non_price_evidence", "hard_4c_thesis_break_routes_to_4c", "source_proxy_only_blocks_runtime_promotion", "high_MAE_guardrail", "local_4B_watch_before_full_4B_when_MFE_outruns_bridge"], "residual_error_types_found": ["nuclear_policy_theme_false_positive_high_MAE", "named_order_legal_clearance_margin_bridge_required", "delayed_MFE_positive_needs_local_4B_watch", "source_proxy_runtime_promotion_risk", "hard_4C_requires_non_price_project_or_legal_break"], "loop_contribution_label": "canonical_archetype_rule_candidate", "do_not_propose_new_weight_delta": true}
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
- For C04, test a canonical-archetype guard requiring named order scope, legal clearance, delivery schedule, backlog conversion and gross/OP margin bridge before clean Stage2/Green. Keep hard 4C blocked unless a non-price project/legal/order thesis break is confirmed.

## 27. Next Round State

```text
completed_round = R1
completed_loop = 86
next_round = R2
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
