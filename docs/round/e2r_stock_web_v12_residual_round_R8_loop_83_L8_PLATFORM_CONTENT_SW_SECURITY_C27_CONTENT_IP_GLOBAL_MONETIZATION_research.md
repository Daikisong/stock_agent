# E2R Stock-Web v12 Residual Research — R8 Loop 83 / L8 / C27

## 0. Research Metadata

```json
{
  "research_session": "post_calibrated_sector_archetype_residual_research",
  "mode": "historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12",
  "scheduled_round": "R8",
  "scheduled_loop": 83,
  "round_schedule_status": "valid",
  "round_sector_consistency": "pass",
  "completed_round": "R8",
  "completed_loop": 83,
  "computed_next_round": "R9",
  "computed_next_loop": 83,
  "large_sector_id": "L8_PLATFORM_CONTENT_SW_SECURITY",
  "canonical_archetype_id": "C27_CONTENT_IP_GLOBAL_MONETIZATION",
  "fine_archetype_id": "GAME_CONTENT_IP_GLOBAL_LAUNCH_LIVEOPS_RETENTION_BRIDGE_VS_THEME_MFE_FADE",
  "loop_objective": [
    "coverage_gap_fill",
    "counterexample_mining",
    "4B_non_price_requirement_stress_test",
    "canonical_archetype_compression",
    "content_ip_monetization_bridge_guardrail",
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
scheduled_round = R8
scheduled_loop = 83
allowed_large_sector = L8_PLATFORM_CONTENT_SW_SECURITY
selected_large_sector = L8_PLATFORM_CONTENT_SW_SECURITY
selected_canonical_archetype_id = C27_CONTENT_IP_GLOBAL_MONETIZATION
computed_next_round = R9
computed_next_loop = 83
round_schedule_status = valid
round_sector_consistency = pass
```

R8 is the platform / content / software / security round. This run uses C27 because the residual being tested is the difference between:

```text
content IP / global launch / fan-platform headline
```

and

```text
launch cadence + live-ops + sales ranking + retention + ARPU/subscriber bridge + margin conversion
```

The economic mechanism is the same as a game update queue or subscription flywheel. A new IP headline is a spark. The durable rerating only starts if that spark catches the kindling: users return, spend repeats, ARPU or subscriber base expands, and margins actually convert.

## 3. Previous Coverage / Duplicate Avoidance Check

No-Repeat is used only as a duplicate ledger.

```text
hard_duplicate_key = canonical_archetype_id + symbol + trigger_type + entry_date
```

C27 coverage is already concentrated in `035900`, `194480`, `259960`, `352820`, `225570`, and `253450`. This run avoids that top-covered set and uses:

```text
112040 / 위메이드
095660 / 네오위즈
376300 / 디어유
```

All three are treated as new independent C27 cases for this loop. No hard duplicate is intentionally reused.

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
| 112040 | 위메이드 | `atlas/symbol_profiles/112/112040.json` | profile-level CA candidate only in old 2012/2021 windows; selected 2024 window clean |
| 095660 | 네오위즈 | `atlas/symbol_profiles/095/095660.json` | profile-level CA candidate only in old 2007/2009 windows; selected 2024 window clean |
| 376300 | 디어유 | `atlas/symbol_profiles/376/376300.json` | no profile-level CA candidate |

## 5. Historical Eligibility Gate

| case_id | symbol | entry_date | entry_price | forward window | 180D status | calibration_usable |
|---|---:|---|---:|---:|---|---|
| R8L83-C27-01 | 112040 | 2024-03-11 | 55,000 | 180D | clean | true |
| R8L83-C27-02 | 095660 | 2024-02-02 | 26,400 | 180D | clean | true |
| R8L83-C27-03 | 376300 | 2024-02-22 | 38,000 | 180D | clean | true |

## 6. Canonical Archetype Compression Map

| canonical_archetype_id | fine/deep route | keep / reject logic |
|---|---|---|
| C27_CONTENT_IP_GLOBAL_MONETIZATION | GAME_GLOBAL_LAUNCH_LIVEOPS_BRIDGE | keep Stage2 only when launch cadence, live-ops, sales ranking and revenue conversion are visible |
| C27_CONTENT_IP_GLOBAL_MONETIZATION | FAN_PLATFORM_SUBSCRIBER_ARPU_BRIDGE | require subscriber retention, ARPU and artist roster expansion before Stage2-Actionable |
| C27_CONTENT_IP_GLOBAL_MONETIZATION | IP_THEME_MFE_FADE | reject or demote when the only support is IP headline / thematic price movement |

## 7. Case Selection Summary

| case_id | symbol | company | trigger_type | entry_date | entry_price | MFE_180D_pct | MAE_180D_pct | current_profile_verdict |
|---|---:|---|---|---|---:|---:|---:|---|
| R8L83-C27-01 | 112040 | 위메이드 | Stage2-Actionable | 2024-03-11 | 55,000 | 46.36 | -45.45 | current_profile_4B_too_late |
| R8L83-C27-02 | 095660 | 네오위즈 | Stage2-FalsePositive | 2024-02-02 | 26,400 | 8.71 | -33.52 | current_profile_false_positive |
| R8L83-C27-03 | 376300 | 디어유 | Stage2-FalsePositive | 2024-02-22 | 38,000 | 2.37 | -53.58 | current_profile_false_positive |

## 8. Positive vs Counterexample Balance

```text
positive_case_count = 1
counterexample_count = 2
4B_or_4C_case_count = 1
calibration_usable_case_count = 3
new_independent_case_count = 3
```

## 9. Evidence Source Map

All selected evidence is currently `source_proxy_only=true / evidence_url_pending=true`.

This MD therefore creates a source-repair queue and a C27 shadow guardrail candidate. It must not be promoted directly into runtime weights until a later source-repair pass attaches primary evidence URLs: game launch/MAU/sales ranking data, platform subscriber metrics, revenue split, margin bridge, company IR, report, or disclosure evidence.

## 10. Price Data Source Map

| symbol | shard path | profile path |
|---|---|---|
| 112040 | `atlas/ohlcv_tradable_by_symbol_year/112/112040/2024.csv` | `atlas/symbol_profiles/112/112040.json` |
| 095660 | `atlas/ohlcv_tradable_by_symbol_year/095/095660/2024.csv` | `atlas/symbol_profiles/095/095660.json` |
| 376300 | `atlas/ohlcv_tradable_by_symbol_year/376/376300/2024.csv` | `atlas/symbol_profiles/376/376300.json` |

## 11. Case-by-Case Trigger Grid

### Case 1 — 112040 / 위메이드

C27 high-MFE positive with mandatory 4B watch. The entry path shows a strong IP/platform MFE burst, but the later drawdown says the model must not let IP momentum masquerade as durable monetization. Stage2 can be allowed only if the repair pass proves live-ops / sales ranking / retention / revenue conversion.

### Case 2 — 095660 / 네오위즈

C27 post-launch IP fade. The initial global game IP route had weak upside after entry and a wide MAE. The model should reject Stage2-Actionable if the evidence is only narrative and lacks follow-on launch cadence, DLC, sales-rank persistence or retention.

### Case 3 — 376300 / 디어유

C27 fan-platform subscription fade. The economics should be subscription-like, but the selected path did not show a usable subscriber / ARPU / roster expansion bridge in this proxy run. Without that bridge, the stock behaved like a theme fade.

## 12. Trigger-Level OHLC Backtest Tables

| symbol | entry | MFE30 | MAE30 | MFE90 | MAE90 | MFE180 | MAE180 | peak | post-peak DD |
|---|---:|---:|---:|---:|---:|---:|---:|---|---:|
| 112040 | 55,000 | 46.36 | -2.36 | 46.36 | -23.45 | 46.36 | -45.45 | 2024-03-20 / 80,500 | -62.73 |
| 095660 | 26,400 | 8.71 | -17.23 | 8.71 | -25.19 | 8.71 | -33.52 | 2024-02-02 / 28,700 | -38.85 |
| 376300 | 38,000 | 2.37 | -27.89 | 2.37 | -40.26 | 2.37 | -53.58 | 2024-02-22 / 38,900 | -54.65 |

## 13. Current Calibrated Profile Stress Test

| case_id | P0 likely behavior | actual path | verdict |
|---|---|---|---|
| R8L83-C27-01 | Stage2-Actionable if global/IP route is over-credited | high MFE followed by deep drawdown | current_profile_4B_too_late |
| R8L83-C27-02 | risk of treating post-launch IP as Stage2 | low MFE / high MAE | current_profile_false_positive |
| R8L83-C27-03 | risk of treating fan-platform IP as Stage2 | minimal MFE / high MAE | current_profile_false_positive |

## 14. Stage2 / Yellow / Green Comparison

```text
green_lateness_ratio = not_applicable
reason = no confirmed Stage3-Green trigger is assigned in this residual MD
```

For C27, the residual is not Green lateness. The residual is whether Stage2-Actionable is allowed before the monetization bridge has actual traction.

## 15. 4B Local vs Full-window Timing Audit

| case_id | local proximity | full-window proximity | verdict |
|---|---:|---:|---|
| R8L83-C27-01 | 0.92 | 0.92 | good local 4B needed after IP-theme MFE without retention bridge |
| R8L83-C27-02 | 0.25 | 0.25 | theme rally rejected as Stage2 without live-ops bridge |
| R8L83-C27-03 | 0.25 | 0.25 | subscriber/ARPU bridge absent; reject Stage2 |

## 16. 4C Protection Audit

No hard 4C is promoted from this file.

```text
four_c_protection_label = thesis_break_watch_only
hard_4c_price_only_allowed = false
```

## 17. Sector-Specific Rule Candidate

```text
rule_scope = no_new_global_rule
sector_specific_rule_candidate = L8 content/IP rows need actual retention, ARPU, sales ranking, or recurring monetization bridge before Stage2-Actionable
confidence = low
reason = all evidence rows are source_proxy_only / evidence_url_pending
```

## 18. Canonical-Archetype Rule Candidate

```text
canonical_archetype_id = C27_CONTENT_IP_GLOBAL_MONETIZATION
candidate_axis = C27_liveops_retention_global_monetization_bridge_required
effect = keep high-MFE IP cases only with 4B watch; demote IP-theme-only false positives
production_scoring_changed = false
shadow_weight_only = true
do_not_propose_new_weight_delta = true
```

## 19. Before / After Backtest Comparison

| profile | eligible triggers | avg MFE90 | avg MAE90 | false-positive behavior | verdict |
|---|---:|---:|---:|---|---|
| P0 e2r_2_1_stock_web_calibrated_proxy | 3 | 19.15 | -29.63 | may over-credit IP theme and platform narrative | needs C27 bridge repair |
| P1 canonical shadow bridge profile | 3 | 46.36 on kept positive | -2.36 near initial positive entry but requires 4B watch | demotes 095660/376300 | better alignment, source repair required |

## 20. Score-Return Alignment Matrix

| case_id | weighted before | label before | weighted after | label after | alignment |
|---|---:|---|---:|---|---|
| R8L83-C27-01 | 76 | Stage2-Actionable | 78 | Stage2-Actionable + local 4B watch | partially aligned |
| R8L83-C27-02 | 60 | Stage2-Watch/FalsePositive | 52 | Rejected-Stage2 / RiskWatch | improved |
| R8L83-C27-03 | 60 | Stage2-Watch/FalsePositive | 52 | Rejected-Stage2 / RiskWatch | improved |

## 21. Coverage Matrix

| large_sector_id | canonical_archetype_id | fine_archetype_id | positive | counterexample | 4B | 4C | new cases | reused | usable triggers | current errors | sector rule | canonical rule | coverage gap after |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---|---|---|
| L8_PLATFORM_CONTENT_SW_SECURITY | C27_CONTENT_IP_GLOBAL_MONETIZATION | GAME_CONTENT_IP_GLOBAL_LAUNCH_LIVEOPS_RETENTION_BRIDGE_VS_THEME_MFE_FADE | 1 | 2 | 1 | 0 | 3 | 0 | 3 | 3 | no | yes | source repair needed |

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
residual_error_types_found:
  - content_IP_theme_false_positive_high_MAE
  - 4B_too_late_after_IP_theme_MFE
  - retention_ARPU_liveops_bridge_required
new_axis_proposed: false
existing_axis_strengthened: C27_liveops_retention_global_monetization_bridge_required
existing_axis_weakened: null
existing_axis_kept: full_4b_requires_non_price_evidence, hard_4c_thesis_break_routes_to_4c
sector_specific_rule_candidate: null
canonical_archetype_rule_candidate: C27_liveops_retention_global_monetization_bridge_required
no_new_signal_reason: null
loop_contribution_label: canonical_archetype_rule_candidate
do_not_propose_new_weight_delta: true
```

This loop adds 3 new independent cases, 2 counterexamples, and 3 residual errors for R8/L8_PLATFORM_CONTENT_SW_SECURITY/C27_CONTENT_IP_GLOBAL_MONETIZATION.

## 23. Validation Scope / Non-Validation Scope

Validated in this MD:

```text
- Stock-Web profile path exists for selected symbols
- Stock-Web tradable shard path exists for selected symbols
- entry_date / entry_price are taken from tradable_raw close
- MFE / MAE / peak / post-peak drawdown are computed from observed OHLC windows
- corporate-action windows are checked at profile level
```

Not validated in this MD:

```text
- primary evidence URL
- exact publication time
- MAU/DAU or sales-rank persistence
- live-ops retention cohort
- ARPU / subscriber bridge
- margin conversion detail
- production scoring implementation
```

## 24. Shadow Weight Calibration

```csv
row_type,axis,scope,large_sector_id,canonical_archetype_id,baseline_value,tested_value,delta,reason,backtest_effect,trigger_ids,calibration_usable_count,new_independent_case_count,counterexample_count,confidence,proposal_type,notes
shadow_weight,C27_liveops_retention_global_monetization_bridge_required,canonical_archetype_specific,L8_PLATFORM_CONTENT_SW_SECURITY,C27_CONTENT_IP_GLOBAL_MONETIZATION,0,1,+1,"Require launch/live-ops/sales ranking/retention/ARPU or subscriber bridge before Stage2-Actionable","keeps 112040 with 4B watch; demotes 095660/376300","R8L83-C27-01-S2A-20240311|R8L83-C27-02-S2FP-20240202|R8L83-C27-03-S2FP-20240222",3,3,2,low,canonical_shadow_only,"source repair required; not production"
```

## 25. Machine-Readable Rows

```jsonl
{"row_type": "price_source_validation", "source": "Songdaiki/stock-web", "source_url": "https://github.com/Songdaiki/stock-web", "manifest_path": "atlas/manifest.json", "schema_path": "atlas/schema.json", "universe_path": "atlas/universe/all_symbols.csv", "manifest_max_date": "2026-02-20", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "raw_shard_root": "atlas/ohlcv_raw_by_symbol_year", "validation_status": "usable_for_historical_calibration"}
{"row_type": "case", "case_id": "R8L83-C27-01", "symbol": "112040", "company_name": "위메이드", "round": "R8", "loop": 83, "large_sector_id": "L8_PLATFORM_CONTENT_SW_SECURITY", "canonical_archetype_id": "C27_CONTENT_IP_GLOBAL_MONETIZATION", "fine_archetype_id": "GAME_CONTENT_IP_GLOBAL_LAUNCH_LIVEOPS_RETENTION_BRIDGE_VS_THEME_MFE_FADE", "case_type": "high_MFE_content_IP_theme_with_4B_need", "positive_or_counterexample": "positive", "best_trigger": "R8L83-C27-01-S2A-20240311", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "positive_MFE_but_full_window_4B_needed", "current_profile_verdict": "current_profile_4B_too_late", "price_source": "Songdaiki/stock-web", "notes": "C27 positive path needs launch/live-ops/sales-ranking/retention conversion, not only IP headline."}
{"row_type": "trigger", "trigger_id": "R8L83-C27-01-S2A-20240311", "case_id": "R8L83-C27-01", "symbol": "112040", "company_name": "위메이드", "round": "R8", "loop": 83, "large_sector_id": "L8_PLATFORM_CONTENT_SW_SECURITY", "canonical_archetype_id": "C27_CONTENT_IP_GLOBAL_MONETIZATION", "fine_archetype_id": "GAME_CONTENT_IP_GLOBAL_LAUNCH_LIVEOPS_RETENTION_BRIDGE_VS_THEME_MFE_FADE", "loop_objective": "coverage_gap_fill|counterexample_mining|4B_non_price_requirement_stress_test|canonical_archetype_compression", "trigger_type": "Stage2-Actionable", "trigger_date": "2024-03-11", "evidence_available_at_that_date": "global game/IP and platform monetization route proxy; live-ops/retention economics pending", "evidence_source": "source_proxy_only; evidence_url_pending", "stage2_evidence_fields": ["IP_or_global_launch_event", "monetization_bridge_proxy"], "stage3_evidence_fields": ["sales_ranking", "retention", "ARPU", "liveops_cadence", "margin_conversion"], "stage4b_evidence_fields": ["valuation_blowoff", "post_launch_retention_fade", "positioning_overheat"], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/112/112040/2024.csv", "profile_path": "atlas/symbol_profiles/112/112040.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "entry_date": "2024-03-11", "entry_price": 55000, "MFE_30D_pct": 46.36, "MFE_90D_pct": 46.36, "MFE_180D_pct": 46.36, "MFE_1Y_pct": null, "MFE_2Y_pct": null, "MAE_30D_pct": -2.36, "MAE_90D_pct": -23.45, "MAE_180D_pct": -45.45, "MAE_1Y_pct": null, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2024-03-20", "peak_price": 80500, "drawdown_after_peak_pct": -62.73, "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": 0.92, "four_b_full_window_peak_proximity": 0.92, "four_b_timing_verdict": "good_local_4B_needed_after_IP_theme_MFE_without_retention_bridge", "four_b_evidence_type": ["valuation_blowoff", "retention_or_liveops_fade", "positioning_overheat"], "four_c_protection_label": "thesis_break_watch_only", "trigger_outcome_label": "positive_MFE_but_full_window_4B_needed", "current_profile_verdict": "current_profile_4B_too_late", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window", "same_entry_group_id": "R8L83-C27-01", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R8L83-C27-01", "trigger_id": "R8L83-C27-01-S2A-20240311", "symbol": "112040", "large_sector_id": "L8_PLATFORM_CONTENT_SW_SECURITY", "canonical_archetype_id": "C27_CONTENT_IP_GLOBAL_MONETIZATION", "raw_component_scores_before": {"contract_score": 15, "backlog_visibility_score": 10, "margin_bridge_score": 35, "revision_score": 40, "relative_strength_score": 65, "customer_quality_score": 35, "policy_or_regulatory_score": 5, "valuation_repricing_score": 60, "execution_risk_score": 45, "legal_or_contract_risk_score": 20, "dilution_cb_risk_score": 10, "accounting_trust_risk_score": 10, "liveops_retention_score": 35, "global_monetization_score": 45}, "weighted_score_before": 76, "stage_label_before": "Stage2-Actionable", "raw_component_scores_after": {"contract_score": 15, "backlog_visibility_score": 10, "margin_bridge_score": 35, "revision_score": 40, "relative_strength_score": 65, "customer_quality_score": 35, "policy_or_regulatory_score": 5, "valuation_repricing_score": 60, "execution_risk_score": 50, "legal_or_contract_risk_score": 20, "dilution_cb_risk_score": 10, "accounting_trust_risk_score": 10, "liveops_retention_score": 45, "global_monetization_score": 45}, "weighted_score_after": 78, "stage_label_after": "Stage2-Actionable + local 4B watch", "changed_components": ["liveops_retention_score", "global_monetization_score", "execution_risk_score"], "component_delta_explanation": "C27 requires launch/live-ops/sales-ranking/retention/ARPU or subscriber bridge; theme-only IP momentum is demoted.", "MFE_90D_pct": 46.36, "MAE_90D_pct": -23.45, "score_return_alignment_label": "positive_MFE_but_full_window_4B_needed", "current_profile_verdict": "current_profile_4B_too_late"}
{"row_type": "case", "case_id": "R8L83-C27-02", "symbol": "095660", "company_name": "네오위즈", "round": "R8", "loop": 83, "large_sector_id": "L8_PLATFORM_CONTENT_SW_SECURITY", "canonical_archetype_id": "C27_CONTENT_IP_GLOBAL_MONETIZATION", "fine_archetype_id": "GAME_CONTENT_IP_GLOBAL_LAUNCH_LIVEOPS_RETENTION_BRIDGE_VS_THEME_MFE_FADE", "case_type": "post_launch_content_IP_monetization_fade", "positive_or_counterexample": "counterexample", "best_trigger": "R8L83-C27-02-S2FP-20240202", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "failed_rerating_low_MFE_high_MAE", "current_profile_verdict": "current_profile_false_positive", "price_source": "Songdaiki/stock-web", "notes": "Post-launch IP rerating fades when sequel/DLC/retention bridge is absent."}
{"row_type": "trigger", "trigger_id": "R8L83-C27-02-S2FP-20240202", "case_id": "R8L83-C27-02", "symbol": "095660", "company_name": "네오위즈", "round": "R8", "loop": 83, "large_sector_id": "L8_PLATFORM_CONTENT_SW_SECURITY", "canonical_archetype_id": "C27_CONTENT_IP_GLOBAL_MONETIZATION", "fine_archetype_id": "GAME_CONTENT_IP_GLOBAL_LAUNCH_LIVEOPS_RETENTION_BRIDGE_VS_THEME_MFE_FADE", "loop_objective": "coverage_gap_fill|counterexample_mining|4B_non_price_requirement_stress_test|canonical_archetype_compression", "trigger_type": "Stage2-FalsePositive", "trigger_date": "2024-02-02", "evidence_available_at_that_date": "global game IP narrative proxy without visible new launch cadence / retention / revenue conversion bridge", "evidence_source": "source_proxy_only; evidence_url_pending", "stage2_evidence_fields": ["IP_or_global_launch_event", "monetization_bridge_proxy"], "stage3_evidence_fields": ["sales_ranking", "retention", "ARPU", "liveops_cadence", "margin_conversion"], "stage4b_evidence_fields": ["valuation_blowoff", "post_launch_retention_fade", "positioning_overheat"], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/095/095660/2024.csv", "profile_path": "atlas/symbol_profiles/095/095660.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "entry_date": "2024-02-02", "entry_price": 26400, "MFE_30D_pct": 8.71, "MFE_90D_pct": 8.71, "MFE_180D_pct": 8.71, "MFE_1Y_pct": null, "MFE_2Y_pct": null, "MAE_30D_pct": -17.23, "MAE_90D_pct": -25.19, "MAE_180D_pct": -33.52, "MAE_1Y_pct": null, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2024-02-02", "peak_price": 28700, "drawdown_after_peak_pct": -38.85, "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": 0.25, "four_b_full_window_peak_proximity": 0.25, "four_b_timing_verdict": "theme_rally_rejected_as_stage2_without_liveops_bridge", "four_b_evidence_type": ["valuation_blowoff", "retention_or_liveops_fade", "positioning_overheat"], "four_c_protection_label": "thesis_break_watch_only", "trigger_outcome_label": "failed_rerating_low_MFE_high_MAE", "current_profile_verdict": "current_profile_false_positive", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window", "same_entry_group_id": "R8L83-C27-02", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R8L83-C27-02", "trigger_id": "R8L83-C27-02-S2FP-20240202", "symbol": "095660", "large_sector_id": "L8_PLATFORM_CONTENT_SW_SECURITY", "canonical_archetype_id": "C27_CONTENT_IP_GLOBAL_MONETIZATION", "raw_component_scores_before": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 5, "revision_score": 20, "relative_strength_score": 45, "customer_quality_score": 20, "policy_or_regulatory_score": 0, "valuation_repricing_score": 35, "execution_risk_score": 70, "legal_or_contract_risk_score": 15, "dilution_cb_risk_score": 10, "accounting_trust_risk_score": 10, "liveops_retention_score": 5, "global_monetization_score": 10}, "weighted_score_before": 60, "stage_label_before": "Stage2-Watch/FalsePositive", "raw_component_scores_after": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 5, "revision_score": 20, "relative_strength_score": 45, "customer_quality_score": 20, "policy_or_regulatory_score": 0, "valuation_repricing_score": 35, "execution_risk_score": 85, "legal_or_contract_risk_score": 15, "dilution_cb_risk_score": 10, "accounting_trust_risk_score": 10, "liveops_retention_score": 0, "global_monetization_score": 0}, "weighted_score_after": 52, "stage_label_after": "Rejected-Stage2 / RiskWatch", "changed_components": ["liveops_retention_score", "global_monetization_score", "execution_risk_score"], "component_delta_explanation": "C27 requires launch/live-ops/sales-ranking/retention/ARPU or subscriber bridge; theme-only IP momentum is demoted.", "MFE_90D_pct": 8.71, "MAE_90D_pct": -25.19, "score_return_alignment_label": "failed_rerating_low_MFE_high_MAE", "current_profile_verdict": "current_profile_false_positive"}
{"row_type": "case", "case_id": "R8L83-C27-03", "symbol": "376300", "company_name": "디어유", "round": "R8", "loop": 83, "large_sector_id": "L8_PLATFORM_CONTENT_SW_SECURITY", "canonical_archetype_id": "C27_CONTENT_IP_GLOBAL_MONETIZATION", "fine_archetype_id": "GAME_CONTENT_IP_GLOBAL_LAUNCH_LIVEOPS_RETENTION_BRIDGE_VS_THEME_MFE_FADE", "case_type": "fan_platform_IP_subscription_growth_fade", "positive_or_counterexample": "counterexample", "best_trigger": "R8L83-C27-03-S2FP-20240222", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "theme_fade_high_MAE", "current_profile_verdict": "current_profile_false_positive", "price_source": "Songdaiki/stock-web", "notes": "Fan-platform IP must show subscriber retention, ARPU, artist roster expansion, and margin bridge."}
{"row_type": "trigger", "trigger_id": "R8L83-C27-03-S2FP-20240222", "case_id": "R8L83-C27-03", "symbol": "376300", "company_name": "디어유", "round": "R8", "loop": 83, "large_sector_id": "L8_PLATFORM_CONTENT_SW_SECURITY", "canonical_archetype_id": "C27_CONTENT_IP_GLOBAL_MONETIZATION", "fine_archetype_id": "GAME_CONTENT_IP_GLOBAL_LAUNCH_LIVEOPS_RETENTION_BRIDGE_VS_THEME_MFE_FADE", "loop_objective": "coverage_gap_fill|counterexample_mining|4B_non_price_requirement_stress_test|canonical_archetype_compression", "trigger_type": "Stage2-FalsePositive", "trigger_date": "2024-02-22", "evidence_available_at_that_date": "fan-platform / artist IP monetization proxy without subscriber retention and ARPU bridge", "evidence_source": "source_proxy_only; evidence_url_pending", "stage2_evidence_fields": ["IP_or_global_launch_event", "monetization_bridge_proxy"], "stage3_evidence_fields": ["sales_ranking", "retention", "ARPU", "liveops_cadence", "margin_conversion"], "stage4b_evidence_fields": ["valuation_blowoff", "post_launch_retention_fade", "positioning_overheat"], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/376/376300/2024.csv", "profile_path": "atlas/symbol_profiles/376/376300.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "entry_date": "2024-02-22", "entry_price": 38000, "MFE_30D_pct": 2.37, "MFE_90D_pct": 2.37, "MFE_180D_pct": 2.37, "MFE_1Y_pct": null, "MFE_2Y_pct": null, "MAE_30D_pct": -27.89, "MAE_90D_pct": -40.26, "MAE_180D_pct": -53.58, "MAE_1Y_pct": null, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2024-02-22", "peak_price": 38900, "drawdown_after_peak_pct": -54.65, "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": 0.25, "four_b_full_window_peak_proximity": 0.25, "four_b_timing_verdict": "subscriber_ARPU_bridge_absent_reject_stage2", "four_b_evidence_type": ["valuation_blowoff", "retention_or_liveops_fade", "positioning_overheat"], "four_c_protection_label": "thesis_break_watch_only", "trigger_outcome_label": "theme_fade_high_MAE", "current_profile_verdict": "current_profile_false_positive", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window", "same_entry_group_id": "R8L83-C27-03", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R8L83-C27-03", "trigger_id": "R8L83-C27-03-S2FP-20240222", "symbol": "376300", "large_sector_id": "L8_PLATFORM_CONTENT_SW_SECURITY", "canonical_archetype_id": "C27_CONTENT_IP_GLOBAL_MONETIZATION", "raw_component_scores_before": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 5, "revision_score": 20, "relative_strength_score": 45, "customer_quality_score": 20, "policy_or_regulatory_score": 0, "valuation_repricing_score": 35, "execution_risk_score": 70, "legal_or_contract_risk_score": 15, "dilution_cb_risk_score": 10, "accounting_trust_risk_score": 10, "liveops_retention_score": 5, "global_monetization_score": 10}, "weighted_score_before": 60, "stage_label_before": "Stage2-Watch/FalsePositive", "raw_component_scores_after": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 5, "revision_score": 20, "relative_strength_score": 45, "customer_quality_score": 20, "policy_or_regulatory_score": 0, "valuation_repricing_score": 35, "execution_risk_score": 85, "legal_or_contract_risk_score": 15, "dilution_cb_risk_score": 10, "accounting_trust_risk_score": 10, "liveops_retention_score": 0, "global_monetization_score": 0}, "weighted_score_after": 52, "stage_label_after": "Rejected-Stage2 / RiskWatch", "changed_components": ["liveops_retention_score", "global_monetization_score", "execution_risk_score"], "component_delta_explanation": "C27 requires launch/live-ops/sales-ranking/retention/ARPU or subscriber bridge; theme-only IP momentum is demoted.", "MFE_90D_pct": 2.37, "MAE_90D_pct": -40.26, "score_return_alignment_label": "theme_fade_high_MAE", "current_profile_verdict": "current_profile_false_positive"}
{"row_type": "shadow_weight", "axis": "C27_liveops_retention_global_monetization_bridge_required", "scope": "canonical_archetype_specific", "large_sector_id": "L8_PLATFORM_CONTENT_SW_SECURITY", "canonical_archetype_id": "C27_CONTENT_IP_GLOBAL_MONETIZATION", "baseline_value": 0, "tested_value": 1, "delta": "+1", "reason": "Content IP rerating requires launch/live-ops cadence, sales ranking, retention/ARPU or subscriber bridge; IP headline alone fades.", "backtest_effect": "keeps 112040 as high-MFE with 4B watch; rejects 095660 and 376300 false positives", "trigger_ids": "R8L83-C27-01-S2A-20240311|R8L83-C27-02-S2FP-20240202|R8L83-C27-03-S2FP-20240222", "calibration_usable_count": 3, "new_independent_case_count": 3, "counterexample_count": 2, "confidence": "low", "proposal_type": "canonical_shadow_only", "notes": "source_proxy_only/evidence_url_pending; not production"}
{"row_type": "residual_contribution", "round": "R8", "loop": 83, "large_sector_id": "L8_PLATFORM_CONTENT_SW_SECURITY", "canonical_archetype_id": "C27_CONTENT_IP_GLOBAL_MONETIZATION", "new_independent_case_count": 3, "reused_case_count": 0, "new_symbol_count": 3, "new_trigger_family_count": 3, "tested_existing_calibrated_axes": ["stage2_actionable_evidence_bonus", "price_only_blowoff_blocks_positive_stage", "full_4b_requires_non_price_evidence", "hard_4c_thesis_break_routes_to_4c"], "residual_error_types_found": ["content_IP_theme_false_positive_high_MAE", "4B_too_late_after_IP_theme_MFE", "retention_ARPU_liveops_bridge_required"], "loop_contribution_label": "canonical_archetype_rule_candidate", "do_not_propose_new_weight_delta": true}
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
- For C27, test a canonical-archetype guard requiring launch/live-ops/sales-ranking/retention/ARPU or subscriber bridge before Stage2-Actionable.

## 27. Next Round State

```text
completed_round = R8
completed_loop = 83
next_round = R9
next_loop = 83
round_schedule_status = valid
round_sector_consistency = pass
```

## 28. Source Notes

```text
MAIN_EXECUTION_PROMPT = docs/core/e2r_v12_prompt_round_scheduler_corrected.txt
NO_REPEAT_INDEX = docs/core/V12_Research_No_Repeat_Index.md
price_source = Songdaiki/stock-web
```
