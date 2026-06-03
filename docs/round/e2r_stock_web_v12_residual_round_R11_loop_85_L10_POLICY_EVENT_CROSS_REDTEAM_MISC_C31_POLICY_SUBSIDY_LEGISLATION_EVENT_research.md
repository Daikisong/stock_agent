# E2R Stock-Web v12 Residual Research — R11 Loop 85 / L10 / C31

## 0. Research Metadata

```json
{
  "research_session": "post_calibrated_sector_archetype_residual_research",
  "mode": "historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12",
  "scheduled_round": "R11",
  "scheduled_loop": 85,
  "round_schedule_status": "valid",
  "round_sector_consistency": "pass",
  "completed_round": "R11",
  "completed_loop": 85,
  "computed_next_round": "R12",
  "computed_next_loop": 85,
  "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC",
  "canonical_archetype_id": "C31_POLICY_SUBSIDY_LEGISLATION_EVENT",
  "fine_archetype_id": "EAST_SEA_GAS_EXPLORATION_POLICY_EVENT_RESOURCE_OPTIONALITY_VS_THEME_SPIKE_FADE",
  "loop_objective": [
    "coverage_gap_fill",
    "counterexample_mining",
    "policy_event_resource_optionality_guardrail",
    "exploration_policy_event_vs_project_economics_bridge_test",
    "theme_spike_MFE_vs_non_price_evidence_bridge_test",
    "local_4B_timing_after_policy_event_MFE",
    "hard_4C_non_price_thesis_break_protection",
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
scheduled_round = R11
scheduled_loop = 85
allowed_large_sector = L10_POLICY_EVENT_CROSS_REDTEAM_MISC or L1_INDUSTRIALS_INFRA_DEFENSE_GRID depending on policy-defense linkage
selected_large_sector = L10_POLICY_EVENT_CROSS_REDTEAM_MISC
selected_canonical_archetype_id = C31_POLICY_SUBSIDY_LEGISLATION_EVENT
computed_next_round = R12
computed_next_loop = 85
round_schedule_status = valid
round_sector_consistency = pass
```

R11 is the policy / event / cross-redteam slot. This run selects C31 and avoids repeating loop84 R11 governance/tender C32 and loop84 R12 agri-food C31. The fine route is East Sea gas exploration / resource optionality policy-event testing.

The tested mechanism:

```text
resource exploration / policy-event headline
→ direct beneficiary mapping
→ license or working-interest clarity
→ reserve probability and capex timeline
→ commercial project economics
→ earnings or margin bridge
→ durable rerating or policy-event theme spike fade
```

C31 here is an oil-rig map, not the oil itself. The model should not treat a map headline as a reservoir unless the license, ownership, reserve probability, capex and economics bridge are visible.

## 3. Previous Coverage / Duplicate Avoidance Check

No-Repeat is used only as a duplicate ledger.

```text
hard_duplicate_key = canonical_archetype_id + symbol + trigger_type + entry_date
```

C31 top-covered symbols include `UNKNOWN_SYMBOL`, `004090`, `036460`, `112610`, `005860`, and `008970`. This run avoids that top-covered set and uses:

```text
012320 / 경동인베스트
000440 / 중앙에너비스
128820 / 대성산업
```

All three are treated as new independent C31 policy/resource-optionality cases for this loop. No hard duplicate is intentionally reused.

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
| 012320 | 경동인베스트 | `atlas/symbol_profiles/012/012320.json` | old 2017 CA candidates; selected 2024 forward window clean |
| 000440 | 중앙에너비스 | `atlas/symbol_profiles/000/000440.json` | old 2018 CA candidate; selected 2024 forward window clean |
| 128820 | 대성산업 | `atlas/symbol_profiles/128/128820.json` | old 2017 CA candidates; selected 2024 forward window clean |

## 5. Historical Eligibility Gate

| case_id | symbol | entry_date | entry_price | forward window | 180D status | calibration_usable |
|---|---:|---|---:|---:|---|---|
| R11L85-C31-01 | 012320 | 2024-06-03 | 89,700 | 180D | clean | true |
| R11L85-C31-02 | 000440 | 2024-06-03 | 24,750 | 180D | clean | true |
| R11L85-C31-03 | 128820 | 2024-06-03 | 4,370 | 180D | clean | true |

## 6. Canonical Archetype Compression Map

| canonical_archetype_id | fine/deep route | keep / reject logic |
|---|---|---|
| C31_POLICY_SUBSIDY_LEGISLATION_EVENT | RESOURCE_EXPLORATION_DIRECT_BENEFICIARY | keep Stage2 only with beneficiary mapping, license/working interest, reserve and economics bridge |
| C31_POLICY_SUBSIDY_LEGISLATION_EVENT | ENERGY_DISTRIBUTOR_POLICY_THEME_SPIKE | reject or local-4B-watch when policy MFE lacks direct exploration economics |
| C31_POLICY_SUBSIDY_LEGISLATION_EVENT | RESOURCE_OPTIONALITY_LOW_MFE_FADE | reject low-MFE resource optionality without project economics or earnings bridge |

## 7. Case Selection Summary

| case_id | symbol | company | trigger_type | entry_date | entry_price | MFE_180D_pct | MAE_180D_pct | current_profile_verdict |
|---|---:|---|---|---|---:|---:|---:|---|
| R11L85-C31-01 | 012320 | 경동인베스트 | Stage2-Actionable | 2024-06-03 | 89,700 | 21.52 | -25.08 | current_profile_partially_correct_local_4B_watch_needed |
| R11L85-C31-02 | 000440 | 중앙에너비스 | Stage2-FalsePositive | 2024-06-03 | 24,750 | 25.66 | -27.27 | current_profile_false_positive_theme_spike_4B_too_late |
| R11L85-C31-03 | 128820 | 대성산업 | Stage2-FalsePositive | 2024-06-03 | 4,370 | 9.27 | -28.83 | current_profile_false_positive_low_MFE_high_MAE |

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

This MD creates a source-repair queue and a C31 resource-policy shadow guardrail candidate. It must not be promoted directly into runtime weights until a later source-repair pass attaches primary evidence URLs: official exploration disclosure, license/working-interest ownership, reserve probability, government policy text, capex schedule, commercial feasibility, earnings or margin bridge.

## 10. Price Data Source Map

| symbol | shard path | profile path |
|---|---|---|
| 012320 | `atlas/ohlcv_tradable_by_symbol_year/012/012320/2024.csv` | `atlas/symbol_profiles/012/012320.json` |
| 000440 | `atlas/ohlcv_tradable_by_symbol_year/000/000440/2024.csv` | `atlas/symbol_profiles/000/000440.json` |
| 128820 | `atlas/ohlcv_tradable_by_symbol_year/128/128820/2024.csv` | `atlas/symbol_profiles/128/128820.json` |

## 11. Case-by-Case Trigger Grid

### Case 1 — 012320 / 경동인베스트

C31 resource-policy positive with local 4B watch. The price path produced a policy-event MFE but then suffered a large drawdown. This is a good positive-with-guardrail row: it can stay Stage2 only if direct beneficiary and project economics evidence are later repaired.

### Case 2 — 000440 / 중앙에너비스

C31 oil/gas policy theme spike false positive. The MFE was large and immediate, but the bridge to direct exploration economics is weak. Energy distributor theme MFE should not become clean Stage2 without pass-through, volume or margin bridge.

### Case 3 — 128820 / 대성산업

C31 resource optionality low-MFE / high-MAE false positive. The MFE was small relative to the later drawdown. Resource optionality without reserve, ownership, capex and earnings bridge should be rejected.

## 12. Trigger-Level OHLC Backtest Tables

| symbol | entry | MFE30 | MAE30 | MFE90 | MAE90 | MFE180 | MAE180 | peak | post-peak DD |
|---|---:|---:|---:|---:|---:|---:|---:|---|---:|
| 012320 | 89,700 | 21.52 | -15.05 | 21.52 | -25.08 | 21.52 | -25.08 | 2024-06-11 / 109,000 | -38.35 |
| 000440 | 24,750 | 25.66 | -17.17 | 25.66 | -27.27 | 25.66 | -27.27 | 2024-06-04 / 31,100 | -42.12 |
| 128820 | 4,370 | 9.27 | -13.73 | 9.27 | -28.83 | 9.27 | -28.83 | 2024-06-04 / 4,775 | -34.87 |

## 13. Current Calibrated Profile Stress Test

| case_id | P0 likely behavior | actual path | verdict |
|---|---|---|---|
| R11L85-C31-01 | Stage2-Actionable if resource policy bridge exists | positive MFE but high MAE | partially correct; local 4B/resource-economics watch needed |
| R11L85-C31-02 | risk of treating energy policy spike as Stage2 | immediate MFE and large drawdown | false positive / theme spike |
| R11L85-C31-03 | risk of treating resource optionality as Stage2 | low MFE / high MAE | false positive |

## 14. Stage2 / Yellow / Green Comparison

```text
green_lateness_ratio = not_applicable
reason = no confirmed Stage3-Green trigger is assigned in this residual MD
```

For C31 resource-policy rows, the residual is whether policy-event MFE becomes clean Stage2/Green before direct beneficiary, license, reserve, capex and economics bridge are proven.

## 15. 4B Local vs Full-window Timing Audit

| case_id | local proximity | full-window proximity | verdict |
|---|---:|---:|---|
| R11L85-C31-01 | 0.75 | 0.65 | local 4B watch after exploration-policy MFE if project economics bridge stalls |
| R11L85-C31-02 | 0.35 | 0.30 | energy policy theme MFE rejected or local-4B-watch without direct-beneficiary bridge |
| R11L85-C31-03 | 0.35 | 0.30 | resource optionality theme rejected without reserve/project economics bridge |

## 16. 4C Protection Audit

No hard 4C is promoted from this file.

```text
four_c_protection_label = hard_4C_requires_non_price_policy_reversal_or_exploration_failure
hard_4c_price_only_allowed = false
```

Price drawdown alone is not hard 4C. C31 hard 4C requires confirmed policy reversal, exploration failure, license/working-interest failure, reserve probability break, capex cancellation or commercial feasibility break.

## 17. Sector-Specific Rule Candidate

```text
rule_scope = no_new_global_rule
sector_specific_rule_candidate = L10/C31 resource-policy rows need direct beneficiary mapping, license/working-interest clarity, reserve probability, capex timeline and commercial economics bridge before clean Stage2/Green
confidence = low
reason = all evidence rows are source_proxy_only / evidence_url_pending
```

## 18. Canonical-Archetype Rule Candidate

```text
canonical_archetype_id = C31_POLICY_SUBSIDY_LEGISLATION_EVENT
candidate_axis = C31_resource_policy_direct_beneficiary_license_economics_bridge_required
effect = keep resource-policy positives with local 4B watch; demote energy/resource theme false positives
production_scoring_changed = false
shadow_weight_only = true
do_not_propose_new_weight_delta = true
```

## 19. Before / After Backtest Comparison

| profile | eligible triggers | avg MFE90 | avg MAE90 | false-positive behavior | verdict |
|---|---:|---:|---:|---|---|
| P0 e2r_2_1_stock_web_calibrated_proxy | 3 | 18.82 | -27.06 | may over-credit policy/resource theme MFE | needs C31 direct-beneficiary/economics bridge repair |
| P1 canonical shadow bridge profile | 3 | 21.52 on kept positive | demotes 000440/128820 | blocks clean Green until source repair | better alignment, source repair required |

## 20. Score-Return Alignment Matrix

| case_id | weighted before | label before | weighted after | label after | alignment |
|---|---:|---|---:|---|---|
| R11L85-C31-01 | 74 | Stage2-Actionable | 70 | Stage2-Actionable + local 4B/resource-economics watch | partially aligned |
| R11L85-C31-02 | 58 | Stage2-Watch/FalsePositive | 44 | Rejected-Stage2 / Policy-event theme RiskWatch | improved |
| R11L85-C31-03 | 58 | Stage2-Watch/FalsePositive | 44 | Rejected-Stage2 / Policy-event theme RiskWatch | improved |

## 21. Coverage Matrix

| large_sector_id | canonical_archetype_id | fine_archetype_id | positive | counterexample | 4B | 4C | new cases | reused | usable triggers | current errors | sector rule | canonical rule | coverage gap after |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---|---|---|
| L10_POLICY_EVENT_CROSS_REDTEAM_MISC | C31_POLICY_SUBSIDY_LEGISLATION_EVENT | EAST_SEA_GAS_EXPLORATION_POLICY_EVENT_RESOURCE_OPTIONALITY_VS_THEME_SPIKE_FADE | 1 | 2 | 3-watch | 0-hard | 3 | 0 | 3 | 2 | no | yes | source repair needed |

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
  - policy_resource_theme_false_positive_high_MAE
  - direct_beneficiary_license_project_economics_bridge_required
  - local_4B_late_after_policy_event_MFE
  - source_proxy_runtime_promotion_risk
  - hard_4C_requires_non_price_policy_or_exploration_break
new_axis_proposed: false
existing_axis_strengthened:
  - C31_resource_policy_direct_beneficiary_license_economics_bridge_required
  - source_proxy_only_blocks_runtime_promotion
  - local_4B_watch_before_full_4B_when_MFE_outruns_bridge
  - hard_4C_requires_non_price_thesis_break
existing_axis_weakened: null
existing_axis_kept:
  - full_4b_requires_non_price_evidence
  - hard_4c_thesis_break_routes_to_4c
sector_specific_rule_candidate: null
canonical_archetype_rule_candidate: C31_resource_policy_direct_beneficiary_license_economics_bridge_required
no_new_signal_reason: null
loop_contribution_label: canonical_archetype_rule_candidate
do_not_propose_new_weight_delta: true
```

This loop adds 3 new independent cases, 2 counterexamples, and 2 residual errors for R11/L10_POLICY_EVENT_CROSS_REDTEAM_MISC/C31_POLICY_SUBSIDY_LEGISLATION_EVENT.

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
- official exploration policy source
- license / working-interest ownership
- reserve probability and capex schedule
- commercial project economics
- production scoring implementation
```

## 24. Shadow Weight Calibration

```csv
row_type,axis,scope,large_sector_id,canonical_archetype_id,baseline_value,tested_value,delta,reason,backtest_effect,trigger_ids,calibration_usable_count,new_independent_case_count,counterexample_count,confidence,proposal_type,notes
shadow_weight,C31_resource_policy_direct_beneficiary_license_economics_bridge_required,canonical_archetype_specific,L10_POLICY_EVENT_CROSS_REDTEAM_MISC,C31_POLICY_SUBSIDY_LEGISLATION_EVENT,0,1,+1,"Require direct beneficiary mapping, license/working-interest clarity, reserve probability, capex timeline and commercial economics bridge before clean Stage2/Green","keeps 012320 with local 4B/resource-economics watch; demotes 000440/128820","R11L85-C31-01-S2A-20240603|R11L85-C31-02-S2FP-20240603|R11L85-C31-03-S2FP-20240603",3,3,2,low,canonical_shadow_only,"source repair required; not production"
```

## 25. Machine-Readable Rows

```jsonl
{"row_type": "price_source_validation", "source": "Songdaiki/stock-web", "source_url": "https://github.com/Songdaiki/stock-web", "manifest_path": "atlas/manifest.json", "schema_path": "atlas/schema.json", "universe_path": "atlas/universe/all_symbols.csv", "manifest_max_date": "2026-02-20", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "raw_shard_root": "atlas/ohlcv_raw_by_symbol_year", "validation_status": "usable_for_historical_calibration"}
{"row_type": "case", "case_id": "R11L85-C31-01", "symbol": "012320", "company_name": "경동인베스트", "round": "R11", "loop": 85, "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "C31_POLICY_SUBSIDY_LEGISLATION_EVENT", "fine_archetype_id": "EAST_SEA_GAS_EXPLORATION_POLICY_EVENT_RESOURCE_OPTIONALITY_VS_THEME_SPIKE_FADE", "case_type": "East_Sea_gas_exploration_policy_event_positive_with_local_4B_watch", "positive_or_counterexample": "positive", "best_trigger": "R11L85-C31-01-S2A-20240603", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "policy_event_MFE_positive_but_local_4B_and_resource_economics_bridge_required", "current_profile_verdict": "current_profile_partially_correct_local_4B_watch_needed", "price_source": "Songdaiki/stock-web", "notes": "C31 policy exploration positives need direct beneficiary mapping, license/working-interest clarity, reserve probability, capex timeline and commercial economics bridge before clean Green."}
{"row_type": "trigger", "trigger_id": "R11L85-C31-01-S2A-20240603", "case_id": "R11L85-C31-01", "symbol": "012320", "company_name": "경동인베스트", "round": "R11", "loop": 85, "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "C31_POLICY_SUBSIDY_LEGISLATION_EVENT", "fine_archetype_id": "EAST_SEA_GAS_EXPLORATION_POLICY_EVENT_RESOURCE_OPTIONALITY_VS_THEME_SPIKE_FADE", "loop_objective": "coverage_gap_fill|counterexample_mining|policy_event_resource_optionality_guardrail|exploration_policy_event_vs_project_economics_bridge|canonical_archetype_compression", "trigger_type": "Stage2-Actionable", "trigger_date": "2024-06-03", "evidence_available_at_that_date": "East Sea gas exploration / resource optionality / policy-event beneficiary proxy; primary reserve, license, capex and economics evidence pending", "evidence_source": "source_proxy_only; evidence_url_pending", "stage2_evidence_fields": ["policy_event_proxy", "resource_optionality_proxy", "direct_beneficiary_proxy"], "stage3_evidence_fields": ["license_or_working_interest", "reserve_probability", "capex_timeline", "project_economics", "earnings_or_margin_bridge"], "stage4b_evidence_fields": ["policy_event_MFE_without_economics_bridge", "theme_spike_drawdown", "source_proxy_gap"], "stage4c_evidence_fields": ["hard_policy_reversal_or_exploration_failure_watch_only"], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/012/012320/2024.csv", "profile_path": "atlas/symbol_profiles/012/012320.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "entry_date": "2024-06-03", "entry_price": 89700, "MFE_30D_pct": 21.52, "MFE_90D_pct": 21.52, "MFE_180D_pct": 21.52, "MFE_1Y_pct": null, "MFE_2Y_pct": null, "MAE_30D_pct": -15.05, "MAE_90D_pct": -25.08, "MAE_180D_pct": -25.08, "MAE_1Y_pct": null, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2024-06-11", "peak_price": 109000, "drawdown_after_peak_pct": -38.35, "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": 0.75, "four_b_full_window_peak_proximity": 0.65, "four_b_timing_verdict": "local_4B_watch_after_exploration_policy_MFE_if_reserve_capex_economics_bridge_stalls", "four_b_evidence_type": ["policy_event_MFE_without_project_economics_bridge", "post_peak_drawdown", "source_proxy_gap"], "four_c_protection_label": "hard_4C_requires_non_price_policy_reversal_or_exploration_failure", "trigger_outcome_label": "policy_event_MFE_positive_but_local_4B_and_resource_economics_bridge_required", "current_profile_verdict": "current_profile_partially_correct_local_4B_watch_needed", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_2024_window_after_old_2017_CA_candidates", "same_entry_group_id": "R11L85-C31-01", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R11L85-C31-01", "trigger_id": "R11L85-C31-01-S2A-20240603", "symbol": "012320", "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "C31_POLICY_SUBSIDY_LEGISLATION_EVENT", "raw_component_scores_before": {"policy_specificity_score": 55, "direct_beneficiary_mapping_score": 45, "license_or_working_interest_score": 35, "reserve_probability_score": 25, "capex_timeline_score": 25, "commercial_economics_score": 20, "earnings_or_margin_bridge_score": 20, "event_momentum_score": 65, "valuation_blowoff_risk_score": 70, "execution_risk_score": 65, "source_quality_score": 20, "4B_watch_score": 45, "4C_watch_score": 30}, "weighted_score_before": 74, "stage_label_before": "Stage2-Actionable", "raw_component_scores_after": {"policy_specificity_score": 55, "direct_beneficiary_mapping_score": 45, "license_or_working_interest_score": 35, "reserve_probability_score": 25, "capex_timeline_score": 25, "commercial_economics_score": 20, "earnings_or_margin_bridge_score": 20, "event_momentum_score": 65, "valuation_blowoff_risk_score": 80, "execution_risk_score": 75, "source_quality_score": 10, "4B_watch_score": 80, "4C_watch_score": 30}, "weighted_score_after": 70, "stage_label_after": "Stage2-Actionable + local 4B/resource-economics watch", "changed_components": ["direct_beneficiary_mapping_score", "license_or_working_interest_score", "commercial_economics_score", "earnings_or_margin_bridge_score", "source_quality_score", "execution_risk_score", "4B_watch_score", "4C_watch_score"], "component_delta_explanation": "C31 resource-policy event rows require direct beneficiary mapping, license/working-interest clarity, reserve probability, capex timeline and commercial economics bridge before clean Stage2/Green; theme-spike MFE alone is demoted or wrapped with local 4B/high-MAE watch.", "MFE_90D_pct": 21.52, "MAE_90D_pct": -25.08, "score_return_alignment_label": "policy_event_MFE_positive_but_local_4B_and_resource_economics_bridge_required", "current_profile_verdict": "current_profile_partially_correct_local_4B_watch_needed"}
{"row_type": "case", "case_id": "R11L85-C31-02", "symbol": "000440", "company_name": "중앙에너비스", "round": "R11", "loop": 85, "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "C31_POLICY_SUBSIDY_LEGISLATION_EVENT", "fine_archetype_id": "EAST_SEA_GAS_EXPLORATION_POLICY_EVENT_RESOURCE_OPTIONALITY_VS_THEME_SPIKE_FADE", "case_type": "oil_gas_policy_theme_spike_false_positive", "positive_or_counterexample": "counterexample", "best_trigger": "R11L85-C31-02-S2FP-20240603", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "large_theme_MFE_then_deep_MAE_policy_event_false_positive", "current_profile_verdict": "current_profile_false_positive_theme_spike_4B_too_late", "price_source": "Songdaiki/stock-web", "notes": "Energy distributor policy-event MFE should not validate Stage2 unless direct beneficiary link, pass-through economics, volume or margin bridge is explicit."}
{"row_type": "trigger", "trigger_id": "R11L85-C31-02-S2FP-20240603", "case_id": "R11L85-C31-02", "symbol": "000440", "company_name": "중앙에너비스", "round": "R11", "loop": 85, "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "C31_POLICY_SUBSIDY_LEGISLATION_EVENT", "fine_archetype_id": "EAST_SEA_GAS_EXPLORATION_POLICY_EVENT_RESOURCE_OPTIONALITY_VS_THEME_SPIKE_FADE", "loop_objective": "coverage_gap_fill|counterexample_mining|policy_event_resource_optionality_guardrail|exploration_policy_event_vs_project_economics_bridge|canonical_archetype_compression", "trigger_type": "Stage2-FalsePositive", "trigger_date": "2024-06-03", "evidence_available_at_that_date": "oil/gas distribution and energy-policy theme proxy without direct exploration economics, reserve or margin bridge", "evidence_source": "source_proxy_only; evidence_url_pending", "stage2_evidence_fields": ["policy_event_proxy", "resource_optionality_proxy", "direct_beneficiary_proxy"], "stage3_evidence_fields": ["license_or_working_interest", "reserve_probability", "capex_timeline", "project_economics", "earnings_or_margin_bridge"], "stage4b_evidence_fields": ["policy_event_MFE_without_economics_bridge", "theme_spike_drawdown", "source_proxy_gap"], "stage4c_evidence_fields": ["hard_policy_reversal_or_exploration_failure_watch_only"], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/000/000440/2024.csv", "profile_path": "atlas/symbol_profiles/000/000440.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "entry_date": "2024-06-03", "entry_price": 24750, "MFE_30D_pct": 25.66, "MFE_90D_pct": 25.66, "MFE_180D_pct": 25.66, "MFE_1Y_pct": null, "MFE_2Y_pct": null, "MAE_30D_pct": -17.17, "MAE_90D_pct": -27.27, "MAE_180D_pct": -27.27, "MAE_1Y_pct": null, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2024-06-04", "peak_price": 31100, "drawdown_after_peak_pct": -42.12, "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": 0.35, "four_b_full_window_peak_proximity": 0.3, "four_b_timing_verdict": "energy_policy_theme_MFE_rejected_or_local_4B_watch_without_direct_beneficiary_economics_bridge", "four_b_evidence_type": ["policy_event_MFE_without_project_economics_bridge", "post_peak_drawdown", "source_proxy_gap"], "four_c_protection_label": "hard_4C_requires_non_price_policy_reversal_or_exploration_failure", "trigger_outcome_label": "large_theme_MFE_then_deep_MAE_policy_event_false_positive", "current_profile_verdict": "current_profile_false_positive_theme_spike_4B_too_late", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_2024_window_after_old_2018_CA_candidate", "same_entry_group_id": "R11L85-C31-02", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R11L85-C31-02", "trigger_id": "R11L85-C31-02-S2FP-20240603", "symbol": "000440", "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "C31_POLICY_SUBSIDY_LEGISLATION_EVENT", "raw_component_scores_before": {"policy_specificity_score": 35, "direct_beneficiary_mapping_score": 15, "license_or_working_interest_score": 5, "reserve_probability_score": 0, "capex_timeline_score": 0, "commercial_economics_score": 0, "earnings_or_margin_bridge_score": 0, "event_momentum_score": 55, "valuation_blowoff_risk_score": 75, "execution_risk_score": 80, "source_quality_score": 15, "4B_watch_score": 75, "4C_watch_score": 45}, "weighted_score_before": 58, "stage_label_before": "Stage2-Watch/FalsePositive", "raw_component_scores_after": {"policy_specificity_score": 35, "direct_beneficiary_mapping_score": 5, "license_or_working_interest_score": 0, "reserve_probability_score": 0, "capex_timeline_score": 0, "commercial_economics_score": 0, "earnings_or_margin_bridge_score": 0, "event_momentum_score": 55, "valuation_blowoff_risk_score": 75, "execution_risk_score": 90, "source_quality_score": 5, "4B_watch_score": 85, "4C_watch_score": 65}, "weighted_score_after": 44, "stage_label_after": "Rejected-Stage2 / Policy-event theme RiskWatch", "changed_components": ["direct_beneficiary_mapping_score", "license_or_working_interest_score", "commercial_economics_score", "earnings_or_margin_bridge_score", "source_quality_score", "execution_risk_score", "4B_watch_score", "4C_watch_score"], "component_delta_explanation": "C31 resource-policy event rows require direct beneficiary mapping, license/working-interest clarity, reserve probability, capex timeline and commercial economics bridge before clean Stage2/Green; theme-spike MFE alone is demoted or wrapped with local 4B/high-MAE watch.", "MFE_90D_pct": 25.66, "MAE_90D_pct": -27.27, "score_return_alignment_label": "large_theme_MFE_then_deep_MAE_policy_event_false_positive", "current_profile_verdict": "current_profile_false_positive_theme_spike_4B_too_late"}
{"row_type": "case", "case_id": "R11L85-C31-03", "symbol": "128820", "company_name": "대성산업", "round": "R11", "loop": 85, "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "C31_POLICY_SUBSIDY_LEGISLATION_EVENT", "fine_archetype_id": "EAST_SEA_GAS_EXPLORATION_POLICY_EVENT_RESOURCE_OPTIONALITY_VS_THEME_SPIKE_FADE", "case_type": "energy_policy_optional_theme_low_MFE_high_MAE_false_positive", "positive_or_counterexample": "counterexample", "best_trigger": "R11L85-C31-03-S2FP-20240603", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "low_MFE_high_MAE_resource_policy_false_positive", "current_profile_verdict": "current_profile_false_positive_low_MFE_high_MAE", "price_source": "Songdaiki/stock-web", "notes": "Resource optionality policy theme should stay RiskWatch unless reserve probability, ownership/working interest, capex and commercial earnings bridge are source-repaired."}
{"row_type": "trigger", "trigger_id": "R11L85-C31-03-S2FP-20240603", "case_id": "R11L85-C31-03", "symbol": "128820", "company_name": "대성산업", "round": "R11", "loop": 85, "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "C31_POLICY_SUBSIDY_LEGISLATION_EVENT", "fine_archetype_id": "EAST_SEA_GAS_EXPLORATION_POLICY_EVENT_RESOURCE_OPTIONALITY_VS_THEME_SPIKE_FADE", "loop_objective": "coverage_gap_fill|counterexample_mining|policy_event_resource_optionality_guardrail|exploration_policy_event_vs_project_economics_bridge|canonical_archetype_compression", "trigger_type": "Stage2-FalsePositive", "trigger_date": "2024-06-03", "evidence_available_at_that_date": "energy/resource optionality and policy-event theme proxy without confirmed reserve, project economics or earnings bridge", "evidence_source": "source_proxy_only; evidence_url_pending", "stage2_evidence_fields": ["policy_event_proxy", "resource_optionality_proxy", "direct_beneficiary_proxy"], "stage3_evidence_fields": ["license_or_working_interest", "reserve_probability", "capex_timeline", "project_economics", "earnings_or_margin_bridge"], "stage4b_evidence_fields": ["policy_event_MFE_without_economics_bridge", "theme_spike_drawdown", "source_proxy_gap"], "stage4c_evidence_fields": ["hard_policy_reversal_or_exploration_failure_watch_only"], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/128/128820/2024.csv", "profile_path": "atlas/symbol_profiles/128/128820.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "entry_date": "2024-06-03", "entry_price": 4370, "MFE_30D_pct": 9.27, "MFE_90D_pct": 9.27, "MFE_180D_pct": 9.27, "MFE_1Y_pct": null, "MFE_2Y_pct": null, "MAE_30D_pct": -13.73, "MAE_90D_pct": -28.83, "MAE_180D_pct": -28.83, "MAE_1Y_pct": null, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2024-06-04", "peak_price": 4775, "drawdown_after_peak_pct": -34.87, "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": 0.35, "four_b_full_window_peak_proximity": 0.3, "four_b_timing_verdict": "resource_policy_optional_theme_rejected_without_reserve_project_economics_margin_bridge", "four_b_evidence_type": ["policy_event_MFE_without_project_economics_bridge", "post_peak_drawdown", "source_proxy_gap"], "four_c_protection_label": "hard_4C_requires_non_price_policy_reversal_or_exploration_failure", "trigger_outcome_label": "low_MFE_high_MAE_resource_policy_false_positive", "current_profile_verdict": "current_profile_false_positive_low_MFE_high_MAE", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_2024_window_after_old_2017_CA_candidates", "same_entry_group_id": "R11L85-C31-03", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R11L85-C31-03", "trigger_id": "R11L85-C31-03-S2FP-20240603", "symbol": "128820", "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "C31_POLICY_SUBSIDY_LEGISLATION_EVENT", "raw_component_scores_before": {"policy_specificity_score": 35, "direct_beneficiary_mapping_score": 15, "license_or_working_interest_score": 5, "reserve_probability_score": 0, "capex_timeline_score": 0, "commercial_economics_score": 0, "earnings_or_margin_bridge_score": 0, "event_momentum_score": 55, "valuation_blowoff_risk_score": 75, "execution_risk_score": 80, "source_quality_score": 15, "4B_watch_score": 75, "4C_watch_score": 45}, "weighted_score_before": 58, "stage_label_before": "Stage2-Watch/FalsePositive", "raw_component_scores_after": {"policy_specificity_score": 35, "direct_beneficiary_mapping_score": 5, "license_or_working_interest_score": 0, "reserve_probability_score": 0, "capex_timeline_score": 0, "commercial_economics_score": 0, "earnings_or_margin_bridge_score": 0, "event_momentum_score": 55, "valuation_blowoff_risk_score": 75, "execution_risk_score": 90, "source_quality_score": 5, "4B_watch_score": 85, "4C_watch_score": 65}, "weighted_score_after": 44, "stage_label_after": "Rejected-Stage2 / Policy-event theme RiskWatch", "changed_components": ["direct_beneficiary_mapping_score", "license_or_working_interest_score", "commercial_economics_score", "earnings_or_margin_bridge_score", "source_quality_score", "execution_risk_score", "4B_watch_score", "4C_watch_score"], "component_delta_explanation": "C31 resource-policy event rows require direct beneficiary mapping, license/working-interest clarity, reserve probability, capex timeline and commercial economics bridge before clean Stage2/Green; theme-spike MFE alone is demoted or wrapped with local 4B/high-MAE watch.", "MFE_90D_pct": 9.27, "MAE_90D_pct": -28.83, "score_return_alignment_label": "low_MFE_high_MAE_resource_policy_false_positive", "current_profile_verdict": "current_profile_false_positive_low_MFE_high_MAE"}
{"row_type": "shadow_weight", "axis": "C31_resource_policy_direct_beneficiary_license_economics_bridge_required", "scope": "canonical_archetype_specific", "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "C31_POLICY_SUBSIDY_LEGISLATION_EVENT", "baseline_value": 0, "tested_value": 1, "delta": "+1", "reason": "Policy/resource exploration rerating requires direct beneficiary mapping, license or working-interest clarity, reserve probability, capex timeline and commercial economics bridge; policy-event theme MFE without bridge fades or needs local 4B/high-MAE watch.", "backtest_effect": "keeps 012320 with local 4B/resource-economics watch; demotes 000440/128820 policy-theme false positives", "trigger_ids": "R11L85-C31-01-S2A-20240603|R11L85-C31-02-S2FP-20240603|R11L85-C31-03-S2FP-20240603", "calibration_usable_count": 3, "new_independent_case_count": 3, "counterexample_count": 2, "confidence": "low", "proposal_type": "canonical_shadow_only", "notes": "source_proxy_only/evidence_url_pending; not production"}
{"row_type": "residual_contribution", "round": "R11", "loop": 85, "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "C31_POLICY_SUBSIDY_LEGISLATION_EVENT", "new_independent_case_count": 3, "reused_case_count": 0, "new_symbol_count": 3, "new_trigger_family_count": 3, "tested_existing_calibrated_axes": ["stage2_actionable_evidence_bonus", "price_only_blowoff_blocks_positive_stage", "full_4b_requires_non_price_evidence", "hard_4c_thesis_break_routes_to_4c", "source_proxy_only_blocks_runtime_promotion", "high_MAE_guardrail", "local_4B_watch_before_full_4B_when_MFE_outruns_bridge"], "residual_error_types_found": ["policy_resource_theme_false_positive_high_MAE", "direct_beneficiary_license_project_economics_bridge_required", "local_4B_late_after_policy_event_MFE", "source_proxy_runtime_promotion_risk", "hard_4C_requires_non_price_policy_or_exploration_break"], "loop_contribution_label": "canonical_archetype_rule_candidate", "do_not_propose_new_weight_delta": true}
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
- For C31 resource-policy rows, test a canonical-archetype guard requiring direct beneficiary mapping, license/working-interest clarity, reserve probability, capex timeline and commercial economics bridge before clean Stage2/Green. Keep hard 4C blocked unless a non-price policy reversal or exploration thesis break is confirmed.

## 27. Next Round State

```text
completed_round = R11
completed_loop = 85
next_round = R12
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
