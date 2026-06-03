# E2R Stock-Web v12 Residual Research — R11 Loop 86 / L10 / C32

## 0. Research Metadata

```json
{
  "research_session": "post_calibrated_sector_archetype_residual_research",
  "mode": "historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12",
  "scheduled_round": "R11",
  "scheduled_loop": 86,
  "round_schedule_status": "valid",
  "round_sector_consistency": "pass",
  "completed_round": "R11",
  "completed_loop": 86,
  "computed_next_round": "R12",
  "computed_next_loop": 86,
  "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC",
  "canonical_archetype_id": "C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP",
  "fine_archetype_id": "TENDER_OFFER_DELISTING_CONTROL_PREMIUM_ACCEPTANCE_THRESHOLD_CAP_VS_TENDER_CAP_LOW_MFE_FADE",
  "loop_objective": [
    "coverage_gap_fill",
    "counterexample_mining",
    "governance_control_premium_tender_cap_guardrail",
    "tender_offer_price_to_upside_cap_bridge_test",
    "control_premium_MFE_vs_acceptance_threshold_delisting_risk_test",
    "local_4B_timing_after_tender_war_MFE",
    "hard_4C_non_price_tender_failure_or_control_break_protection",
    "source_proxy_runtime_promotion_blocker",
    "low_MFE_cap_guardrail",
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
scheduled_loop = 86
allowed_large_sector = L10_POLICY_EVENT_CROSS_REDTEAM_MISC or L1 defense-linked policy
selected_large_sector = L10_POLICY_EVENT_CROSS_REDTEAM_MISC
selected_canonical_archetype_id = C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP
computed_next_round = R12
computed_next_loop = 86
round_schedule_status = valid
round_sector_consistency = pass
```

R11 is the policy/event/cross-redteam slot. This run selects C32 rather than repeating loop85 R11/R12 C31 policy-event rows.

The tested mechanism:

```text
tender offer / control premium / governance contest headline
→ tender price and residual spread
→ acceptance threshold and financing
→ regulatory / delisting / control path
→ minority shareholder and litigation risk
→ durable control-premium rerating, tender-cap flatline, or tender-war blowoff
```

C32 is not a normal earnings rerating. It is an auction book: the upside is bounded by offer price, acceptance probability and control path.

## 3. Previous Coverage / Duplicate Avoidance Check

No-Repeat is used only as a duplicate ledger.

```text
hard_duplicate_key = canonical_archetype_id + symbol + trigger_type + entry_date
```

C32 top-covered symbols include `010130`, `041510`, `008930`, `011200`, `UNKNOWN_SYMBOL`, and `003920`. This run avoids that top-covered set and uses:

```text
119860 / 커넥트웨이브
003410 / 쌍용C&E
036560 / 영풍정밀
```

All three are treated as new independent C32 governance/control-premium/tender-cap cases for this loop. No hard duplicate is intentionally reused.

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
| 119860 | 커넥트웨이브 | `atlas/symbol_profiles/119/119860.json` | old 2022 name-change CA candidate; selected 2024 tender window clean |
| 003410 | 쌍용C&E | `atlas/symbol_profiles/003/003410.json` | old 2018 CA candidate; selected 2024 tender window clean |
| 036560 | 영풍정밀 | `atlas/symbol_profiles/036/036560.json` | old 2008 CA candidate; selected 2024 tender-war window clean |

## 5. Historical Eligibility Gate

| case_id | symbol | entry_date | entry_price | forward window | 180D status | calibration_usable |
|---|---:|---|---:|---:|---|---|
| R11L86-C32-01 | 119860 | 2024-04-25 | 13,100 | 180D | clean through delisting/tender window | true |
| R11L86-C32-02 | 003410 | 2024-02-05 | 6,940 | 180D | clean through delisting/tender window | true |
| R11L86-C32-03 | 036560 | 2024-09-13 | 12,180 | 180D | clean | true |

## 6. Canonical Archetype Compression Map

| canonical_archetype_id | fine/deep route | keep / reject logic |
|---|---|---|
| C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP | TENDER_DELISTING_CONTROL_PREMIUM_POSITIVE | keep Stage2 only with tender price, acceptance threshold, financing and delisting path |
| C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP | LATE_TENDER_CAP_LOW_MFE_FALSE_POSITIVE | reject if the offer price cap already removed residual spread |
| C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP | TENDER_WAR_CONTROL_PREMIUM_BLOWOFF | keep Stage2 with local 4B if competing-bid/control path is unresolved |

## 7. Case Selection Summary

| case_id | symbol | company | trigger_type | entry_date | entry_price | MFE_180D_pct | MAE_180D_pct | current_profile_verdict |
|---|---:|---|---|---|---:|---:|---:|---|
| R11L86-C32-01 | 119860 | 커넥트웨이브 | Stage2-Actionable | 2024-04-25 | 13,100 | 39.69 | -0.84 | current_profile_partially_correct_tender_cap_watch_needed |
| R11L86-C32-02 | 003410 | 쌍용C&E | Stage2-FalsePositive | 2024-02-05 | 6,940 | 1.44 | -2.31 | current_profile_false_positive_low_MFE_tender_cap |
| R11L86-C32-03 | 036560 | 영풍정밀 | Stage2-Actionable | 2024-09-13 | 12,180 | 201.31 | 0.0 | current_profile_partially_correct_local_4B_tender_war_watch_needed |

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

This MD creates a source-repair queue and a C32 governance/tender-cap shadow guardrail candidate. It must not be promoted directly into runtime weights until a later source-repair pass attaches primary evidence URLs: tender price, offeror, financing, acceptance threshold, tender period, regulatory/delisting path, competing offer path, minority shareholder risk and litigation/control-break evidence.

## 10. Price Data Source Map

| symbol | shard path | profile path |
|---|---|---|
| 119860 | `atlas/ohlcv_tradable_by_symbol_year/119/119860/2024.csv` | `atlas/symbol_profiles/119/119860.json` |
| 003410 | `atlas/ohlcv_tradable_by_symbol_year/003/003410/2024.csv` | `atlas/symbol_profiles/003/003410.json` |
| 036560 | `atlas/ohlcv_tradable_by_symbol_year/036/036560/2024.csv` | `atlas/symbol_profiles/036/036560.json` |

## 11. Case-by-Case Trigger Grid

### Case 1 — 119860 / 커넥트웨이브

C32 tender-offer / delisting control-premium positive. The pre-announcement/announcement-window price path repriced sharply toward the tender cap and then flattened. This is not a normal momentum Green; it is a tender-cap positive that needs residual-spread and acceptance-threshold modeling.

### Case 2 — 003410 / 쌍용C&E

C32 successful tender but late-entry low-MFE false positive. After the offer cap was reflected, residual upside was tiny. The tender may succeed, but Stage2 alpha is gone if the model enters after the price cap.

### Case 3 — 036560 / 영풍정밀

C32 tender-war control-premium positive with local 4B watch. The control-premium path produced extreme MFE, but the post-peak drawdown was large. This row strengthens local 4B after tender-war MFE, not hard 4C.

## 12. Trigger-Level OHLC Backtest Tables

| symbol | entry | MFE30 | MAE30 | MFE90 | MAE90 | MFE180 | MAE180 | peak | post-peak DD |
|---|---:|---:|---:|---:|---:|---:|---:|---|---:|
| 119860 | 13,100 | 36.87 | -0.84 | 39.69 | -0.84 | 39.69 | -0.84 | 2024-06-26 / 18,300 | -2.95 |
| 003410 | 6,940 | 1.44 | -2.31 | 1.44 | -2.31 | 1.44 | -2.31 | 2024-03-15 / 7,040 | -2.70 |
| 036560 | 12,180 | 201.31 | 0.00 | 201.31 | 0.00 | 201.31 | 0.00 | 2024-10-07 / 36,700 | -48.64 |

## 13. Current Calibrated Profile Stress Test

| case_id | P0 likely behavior | actual path | verdict |
|---|---|---|---|
| R11L86-C32-01 | Stage2-Actionable if tender spread/threshold bridge exists | repricing then cap flatline | partially correct; tender-cap watch needed |
| R11L86-C32-02 | risk of treating successful tender as Stage2 | tiny residual MFE | false positive / low-MFE cap |
| R11L86-C32-03 | Stage2-Actionable if tender war remains live | extreme MFE then drawdown | partially correct; local 4B watch needed |

## 14. Stage2 / Yellow / Green Comparison

```text
green_lateness_ratio = not_applicable
reason = no confirmed Stage3-Green trigger is assigned in this residual MD
```

For C32, the residual is not Green lateness. The residual is whether control-premium MFE has remaining residual spread after tender price, acceptance threshold and regulatory/control path are known.

## 15. 4B Local vs Full-window Timing Audit

| case_id | local proximity | full-window proximity | verdict |
|---|---:|---:|---|
| R11L86-C32-01 | 0.75 | 0.65 | tender-cap watch after control-premium MFE if price/threshold bridge stalls |
| R11L86-C32-02 | 0.35 | 0.30 | late tender entry rejected when offer-price cap removes remaining E2R |
| R11L86-C32-03 | 0.75 | 0.65 | local 4B watch after tender-war MFE if offer escalation/control path stalls |

## 16. 4C Protection Audit

No hard 4C is promoted from this file.

```text
four_c_protection_label = hard_4C_requires_non_price_tender_failure_control_loss_or_regulatory_block
hard_4c_price_only_allowed = false
```

Price drawdown alone is not hard 4C. C32 hard 4C requires confirmed tender failure, acceptance shortfall, offer withdrawal, financing failure, regulatory block, control loss, litigation block or delisting-path break.

## 17. Sector-Specific Rule Candidate

```text
rule_scope = no_new_global_rule
sector_specific_rule_candidate = L10/C32 rows need tender price, residual spread, acceptance threshold, financing, regulatory/delisting path and minority/control risk before clean Stage2/Green
confidence = low
reason = all evidence rows are source_proxy_only / evidence_url_pending
```

## 18. Canonical-Archetype Rule Candidate

```text
canonical_archetype_id = C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP
candidate_axis = C32_tender_control_premium_acceptance_threshold_residual_spread_cap_bridge_required
effect = keep tender-control positives with local 4B/tender-cap watch; demote low-MFE late tender cap false positives
production_scoring_changed = false
shadow_weight_only = true
do_not_propose_new_weight_delta = true
```

## 19. Before / After Backtest Comparison

| profile | eligible triggers | avg MFE90 | avg MAE90 | false-positive behavior | verdict |
|---|---:|---:|---:|---|---|
| P0 e2r_2_1_stock_web_calibrated_proxy | 3 | 80.81 | -1.05 | may over-credit post-announcement tender cap or tender-war MFE | needs C32 tender residual-spread repair |
| P1 canonical shadow bridge profile | 3 | keeps 119860/036560 with cap watch | demotes 003410 late tender cap | better alignment, source repair required |

## 20. Score-Return Alignment Matrix

| case_id | weighted before | label before | weighted after | label after | alignment |
|---|---:|---|---:|---|---|
| R11L86-C32-01 | 77 | Stage2-Actionable | 73 | Stage2-Actionable + local 4B/tender-cap watch | partially aligned |
| R11L86-C32-02 | 56 | Stage2-Watch/FalsePositive | 42 | Rejected-Stage2 / Tender-cap low-MFE RiskWatch | improved |
| R11L86-C32-03 | 77 | Stage2-Actionable | 73 | Stage2-Actionable + local 4B/tender-cap watch | partially aligned |

## 21. Coverage Matrix

| large_sector_id | canonical_archetype_id | fine_archetype_id | positive | counterexample | 4B | 4C | new cases | reused | usable triggers | current errors | sector rule | canonical rule | coverage gap after |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---|---|---|
| L10_POLICY_EVENT_CROSS_REDTEAM_MISC | C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP | TENDER_OFFER_DELISTING_CONTROL_PREMIUM_ACCEPTANCE_THRESHOLD_CAP_VS_TENDER_CAP_LOW_MFE_FADE | 2 | 1 | 3-watch | 0-hard | 3 | 0 | 3 | 2 | no | yes | source repair needed |

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
  - low_MFE_guardrail
  - local_4B_watch_before_full_4B_when_MFE_outruns_bridge
residual_error_types_found:
  - late_tender_cap_low_MFE_false_positive
  - tender_control_premium_acceptance_threshold_residual_spread_bridge_required
  - tender_war_local_4B_after_MFE
  - source_proxy_runtime_promotion_risk
  - hard_4C_requires_non_price_tender_failure_or_control_break
new_axis_proposed: false
existing_axis_strengthened:
  - C32_tender_control_premium_acceptance_threshold_residual_spread_cap_bridge_required
  - source_proxy_only_blocks_runtime_promotion
  - local_4B_watch_before_full_4B_when_MFE_outruns_bridge
  - hard_4C_requires_non_price_thesis_break
existing_axis_weakened: null
existing_axis_kept:
  - full_4b_requires_non_price_evidence
  - hard_4c_thesis_break_routes_to_4c
sector_specific_rule_candidate: null
canonical_archetype_rule_candidate: C32_tender_control_premium_acceptance_threshold_residual_spread_cap_bridge_required
no_new_signal_reason: null
loop_contribution_label: canonical_archetype_rule_candidate
do_not_propose_new_weight_delta: true
```

This loop adds 3 new independent cases, 1 counterexample, and 2 residual errors for R11/L10_POLICY_EVENT_CROSS_REDTEAM_MISC/C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP.

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
- tender price and offeror source
- acceptance threshold and tender period
- financing / regulatory / delisting path
- litigation, minority-shareholder or control-break evidence
- production scoring implementation
```

## 24. Shadow Weight Calibration

```csv
row_type,axis,scope,large_sector_id,canonical_archetype_id,baseline_value,tested_value,delta,reason,backtest_effect,trigger_ids,calibration_usable_count,new_independent_case_count,counterexample_count,confidence,proposal_type,notes
shadow_weight,C32_tender_control_premium_acceptance_threshold_residual_spread_cap_bridge_required,canonical_archetype_specific,L10_POLICY_EVENT_CROSS_REDTEAM_MISC,C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP,0,1,+1,"Require tender price, residual spread, acceptance threshold, financing, regulatory/delisting path and minority/control risk before clean Stage2/Green","keeps 119860/036560 with tender-cap or tender-war watch; demotes 003410","R11L86-C32-01-S2A-20240425|R11L86-C32-02-S2FP-20240205|R11L86-C32-03-S2A-20240913",3,3,1,low,canonical_shadow_only,"source repair required; not production"
```

## 25. Machine-Readable Rows

```jsonl
{"row_type": "price_source_validation", "source": "Songdaiki/stock-web", "source_url": "https://github.com/Songdaiki/stock-web", "manifest_path": "atlas/manifest.json", "schema_path": "atlas/schema.json", "universe_path": "atlas/universe/all_symbols.csv", "manifest_max_date": "2026-02-20", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "raw_shard_root": "atlas/ohlcv_raw_by_symbol_year", "validation_status": "usable_for_historical_calibration"}
{"row_type": "case", "case_id": "R11L86-C32-01", "symbol": "119860", "company_name": "커넥트웨이브", "round": "R11", "loop": 86, "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP", "fine_archetype_id": "TENDER_OFFER_DELISTING_CONTROL_PREMIUM_ACCEPTANCE_THRESHOLD_CAP_VS_TENDER_CAP_LOW_MFE_FADE", "case_type": "tender_offer_delisting_control_premium_positive_with_price_cap", "positive_or_counterexample": "positive", "best_trigger": "R11L86-C32-01-S2A-20240425", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "control_premium_positive_but_tender_price_cap_limits_followthrough", "current_profile_verdict": "current_profile_partially_correct_tender_cap_watch_needed", "price_source": "Songdaiki/stock-web", "notes": "C32 tender positives need tender price, acceptance threshold, financing, regulatory/delisting path and residual spread/cap analysis before clean Green."}
{"row_type": "trigger", "trigger_id": "R11L86-C32-01-S2A-20240425", "case_id": "R11L86-C32-01", "symbol": "119860", "company_name": "커넥트웨이브", "round": "R11", "loop": 86, "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP", "fine_archetype_id": "TENDER_OFFER_DELISTING_CONTROL_PREMIUM_ACCEPTANCE_THRESHOLD_CAP_VS_TENDER_CAP_LOW_MFE_FADE", "loop_objective": "coverage_gap_fill|counterexample_mining|governance_control_premium_tender_cap_guardrail|tender_price_acceptance_threshold_residual_spread_bridge|canonical_archetype_compression", "trigger_type": "Stage2-Actionable", "trigger_date": "2024-04-25", "evidence_available_at_that_date": "tender offer / delisting / control premium announcement-window proxy; primary tender price, acceptance threshold and delisting schedule evidence pending", "evidence_source": "source_proxy_only; evidence_url_pending", "stage2_evidence_fields": ["control_premium_proxy", "tender_price_proxy", "acceptance_threshold_proxy"], "stage3_evidence_fields": ["confirmed_tender_price", "acceptance_threshold", "financing_visibility", "regulatory_or_delisting_path", "residual_spread", "minority_shareholder_risk"], "stage4b_evidence_fields": ["control_premium_MFE_without_remaining_spread", "tender_cap_blowoff", "post_peak_drawdown"], "stage4c_evidence_fields": ["hard_tender_failure_control_loss_or_regulatory_block_watch_only"], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/119/119860/2024.csv", "profile_path": "atlas/symbol_profiles/119/119860.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "entry_date": "2024-04-25", "entry_price": 13100, "MFE_30D_pct": 36.87, "MFE_90D_pct": 39.69, "MFE_180D_pct": 39.69, "MFE_1Y_pct": null, "MFE_2Y_pct": null, "MAE_30D_pct": -0.84, "MAE_90D_pct": -0.84, "MAE_180D_pct": -0.84, "MAE_1Y_pct": null, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2024-06-26", "peak_price": 18300, "drawdown_after_peak_pct": -2.95, "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": 0.75, "four_b_full_window_peak_proximity": 0.65, "four_b_timing_verdict": "tender_cap_watch_after_control_premium_MFE_if_price_threshold_acceptance_bridge_stalls", "four_b_evidence_type": ["tender_MFE_without_residual_spread_bridge", "post_peak_drawdown", "source_proxy_gap"], "four_c_protection_label": "hard_4C_requires_non_price_tender_failure_control_loss_or_regulatory_block", "trigger_outcome_label": "control_premium_positive_but_tender_price_cap_limits_followthrough", "current_profile_verdict": "current_profile_partially_correct_tender_cap_watch_needed", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_2024_window_after_old_2022_name_change_CA_candidate", "same_entry_group_id": "R11L86-C32-01", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R11L86-C32-01", "trigger_id": "R11L86-C32-01-S2A-20240425", "symbol": "119860", "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP", "raw_component_scores_before": {"control_premium_score": 60, "tender_price_specificity_score": 50, "acceptance_threshold_score": 40, "financing_visibility_score": 35, "regulatory_or_delisting_path_score": 40, "residual_spread_score": 45, "minority_shareholder_risk_score": 45, "relative_strength_score": 70, "cap_blowoff_risk_score": 65, "execution_risk_score": 55, "source_quality_score": 20, "4B_watch_score": 45, "4C_watch_score": 25}, "weighted_score_before": 77, "stage_label_before": "Stage2-Actionable", "raw_component_scores_after": {"control_premium_score": 60, "tender_price_specificity_score": 50, "acceptance_threshold_score": 40, "financing_visibility_score": 35, "regulatory_or_delisting_path_score": 40, "residual_spread_score": 45, "minority_shareholder_risk_score": 45, "relative_strength_score": 70, "cap_blowoff_risk_score": 75, "execution_risk_score": 60, "source_quality_score": 10, "4B_watch_score": 85, "4C_watch_score": 25}, "weighted_score_after": 73, "stage_label_after": "Stage2-Actionable + local 4B/tender-cap watch", "changed_components": ["residual_spread_score", "acceptance_threshold_score", "regulatory_or_delisting_path_score", "source_quality_score", "cap_blowoff_risk_score", "4B_watch_score"], "component_delta_explanation": "C32 requires control-premium MFE to be evaluated against tender price, remaining spread, acceptance threshold, financing, regulatory/delisting path and minority risk; post-announcement tender caps or tender wars need local 4B/tender-cap watch.", "MFE_90D_pct": 39.69, "MAE_90D_pct": -0.84, "score_return_alignment_label": "control_premium_positive_but_tender_price_cap_limits_followthrough", "current_profile_verdict": "current_profile_partially_correct_tender_cap_watch_needed"}
{"row_type": "case", "case_id": "R11L86-C32-02", "symbol": "003410", "company_name": "쌍용C&E", "round": "R11", "loop": 86, "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP", "fine_archetype_id": "TENDER_OFFER_DELISTING_CONTROL_PREMIUM_ACCEPTANCE_THRESHOLD_CAP_VS_TENDER_CAP_LOW_MFE_FADE", "case_type": "successful_tender_but_late_entry_low_MFE_cap_false_positive", "positive_or_counterexample": "counterexample", "best_trigger": "R11L86-C32-02-S2FP-20240205", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "low_MFE_tender_cap_false_positive_after_announcement", "current_profile_verdict": "current_profile_false_positive_low_MFE_tender_cap", "price_source": "Songdaiki/stock-web", "notes": "A successful tender can still be a Stage2 false positive after the price cap is mostly reflected; remaining spread and acceptance risk must be modeled."}
{"row_type": "trigger", "trigger_id": "R11L86-C32-02-S2FP-20240205", "case_id": "R11L86-C32-02", "symbol": "003410", "company_name": "쌍용C&E", "round": "R11", "loop": 86, "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP", "fine_archetype_id": "TENDER_OFFER_DELISTING_CONTROL_PREMIUM_ACCEPTANCE_THRESHOLD_CAP_VS_TENDER_CAP_LOW_MFE_FADE", "loop_objective": "coverage_gap_fill|counterexample_mining|governance_control_premium_tender_cap_guardrail|tender_price_acceptance_threshold_residual_spread_bridge|canonical_archetype_compression", "trigger_type": "Stage2-FalsePositive", "trigger_date": "2024-02-05", "evidence_available_at_that_date": "tender offer / delisting price-cap proxy after event gap; primary residual spread and acceptance schedule evidence pending", "evidence_source": "source_proxy_only; evidence_url_pending", "stage2_evidence_fields": ["control_premium_proxy", "tender_price_proxy", "acceptance_threshold_proxy"], "stage3_evidence_fields": ["confirmed_tender_price", "acceptance_threshold", "financing_visibility", "regulatory_or_delisting_path", "residual_spread", "minority_shareholder_risk"], "stage4b_evidence_fields": ["control_premium_MFE_without_remaining_spread", "tender_cap_blowoff", "post_peak_drawdown"], "stage4c_evidence_fields": ["hard_tender_failure_control_loss_or_regulatory_block_watch_only"], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/003/003410/2024.csv", "profile_path": "atlas/symbol_profiles/003/003410.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "entry_date": "2024-02-05", "entry_price": 6940, "MFE_30D_pct": 1.44, "MFE_90D_pct": 1.44, "MFE_180D_pct": 1.44, "MFE_1Y_pct": null, "MFE_2Y_pct": null, "MAE_30D_pct": -2.31, "MAE_90D_pct": -2.31, "MAE_180D_pct": -2.31, "MAE_1Y_pct": null, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2024-03-15", "peak_price": 7040, "drawdown_after_peak_pct": -2.7, "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": 0.35, "four_b_full_window_peak_proximity": 0.3, "four_b_timing_verdict": "late_tender_entry_rejected_when_offer_price_cap_removes_remaining_E2R", "four_b_evidence_type": ["tender_MFE_without_residual_spread_bridge", "post_peak_drawdown", "source_proxy_gap"], "four_c_protection_label": "hard_4C_requires_non_price_tender_failure_control_loss_or_regulatory_block", "trigger_outcome_label": "low_MFE_tender_cap_false_positive_after_announcement", "current_profile_verdict": "current_profile_false_positive_low_MFE_tender_cap", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_2024_window_after_old_2018_CA_candidate", "same_entry_group_id": "R11L86-C32-02", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R11L86-C32-02", "trigger_id": "R11L86-C32-02-S2FP-20240205", "symbol": "003410", "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP", "raw_component_scores_before": {"control_premium_score": 30, "tender_price_specificity_score": 45, "acceptance_threshold_score": 20, "financing_visibility_score": 25, "regulatory_or_delisting_path_score": 30, "residual_spread_score": 5, "minority_shareholder_risk_score": 55, "relative_strength_score": 20, "cap_blowoff_risk_score": 75, "execution_risk_score": 65, "source_quality_score": 15, "4B_watch_score": 60, "4C_watch_score": 30}, "weighted_score_before": 56, "stage_label_before": "Stage2-Watch/FalsePositive", "raw_component_scores_after": {"control_premium_score": 30, "tender_price_specificity_score": 45, "acceptance_threshold_score": 20, "financing_visibility_score": 25, "regulatory_or_delisting_path_score": 30, "residual_spread_score": 0, "minority_shareholder_risk_score": 55, "relative_strength_score": 5, "cap_blowoff_risk_score": 75, "execution_risk_score": 65, "source_quality_score": 5, "4B_watch_score": 85, "4C_watch_score": 30}, "weighted_score_after": 42, "stage_label_after": "Rejected-Stage2 / Tender-cap low-MFE RiskWatch", "changed_components": ["residual_spread_score", "acceptance_threshold_score", "regulatory_or_delisting_path_score", "source_quality_score", "cap_blowoff_risk_score", "4B_watch_score"], "component_delta_explanation": "C32 requires control-premium MFE to be evaluated against tender price, remaining spread, acceptance threshold, financing, regulatory/delisting path and minority risk; post-announcement tender caps or tender wars need local 4B/tender-cap watch.", "MFE_90D_pct": 1.44, "MAE_90D_pct": -2.31, "score_return_alignment_label": "low_MFE_tender_cap_false_positive_after_announcement", "current_profile_verdict": "current_profile_false_positive_low_MFE_tender_cap"}
{"row_type": "case", "case_id": "R11L86-C32-03", "symbol": "036560", "company_name": "영풍정밀", "round": "R11", "loop": 86, "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP", "fine_archetype_id": "TENDER_OFFER_DELISTING_CONTROL_PREMIUM_ACCEPTANCE_THRESHOLD_CAP_VS_TENDER_CAP_LOW_MFE_FADE", "case_type": "control_premium_tender_war_positive_with_local_4B_watch", "positive_or_counterexample": "positive", "best_trigger": "R11L86-C32-03-S2A-20240913", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "tender_war_large_MFE_but_local_4B_required_after_control_premium_blowoff", "current_profile_verdict": "current_profile_partially_correct_local_4B_tender_war_watch_needed", "price_source": "Songdaiki/stock-web", "notes": "Tender-war positives need offer spread, competing-bid probability, acceptance threshold, legal/control path and post-peak cap risk before clean Green."}
{"row_type": "trigger", "trigger_id": "R11L86-C32-03-S2A-20240913", "case_id": "R11L86-C32-03", "symbol": "036560", "company_name": "영풍정밀", "round": "R11", "loop": 86, "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP", "fine_archetype_id": "TENDER_OFFER_DELISTING_CONTROL_PREMIUM_ACCEPTANCE_THRESHOLD_CAP_VS_TENDER_CAP_LOW_MFE_FADE", "loop_objective": "coverage_gap_fill|counterexample_mining|governance_control_premium_tender_cap_guardrail|tender_price_acceptance_threshold_residual_spread_bridge|canonical_archetype_compression", "trigger_type": "Stage2-Actionable", "trigger_date": "2024-09-13", "evidence_available_at_that_date": "control premium / tender war / governance contest proxy; primary offer price escalation, acceptance threshold and litigation-control evidence pending", "evidence_source": "source_proxy_only; evidence_url_pending", "stage2_evidence_fields": ["control_premium_proxy", "tender_price_proxy", "acceptance_threshold_proxy"], "stage3_evidence_fields": ["confirmed_tender_price", "acceptance_threshold", "financing_visibility", "regulatory_or_delisting_path", "residual_spread", "minority_shareholder_risk"], "stage4b_evidence_fields": ["control_premium_MFE_without_remaining_spread", "tender_cap_blowoff", "post_peak_drawdown"], "stage4c_evidence_fields": ["hard_tender_failure_control_loss_or_regulatory_block_watch_only"], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/036/036560/2024.csv", "profile_path": "atlas/symbol_profiles/036/036560.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "entry_date": "2024-09-13", "entry_price": 12180, "MFE_30D_pct": 201.31, "MFE_90D_pct": 201.31, "MFE_180D_pct": 201.31, "MFE_1Y_pct": null, "MFE_2Y_pct": null, "MAE_30D_pct": 0.0, "MAE_90D_pct": 0.0, "MAE_180D_pct": 0.0, "MAE_1Y_pct": null, "below_entry_price_flag_30D": false, "below_entry_price_flag_90D": false, "peak_date": "2024-10-07", "peak_price": 36700, "drawdown_after_peak_pct": -48.64, "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": 0.75, "four_b_full_window_peak_proximity": 0.65, "four_b_timing_verdict": "local_4B_watch_after_tender_war_MFE_if_offer_escalation_acceptance_control_bridge_stalls", "four_b_evidence_type": ["tender_MFE_without_residual_spread_bridge", "post_peak_drawdown", "source_proxy_gap"], "four_c_protection_label": "hard_4C_requires_non_price_tender_failure_control_loss_or_regulatory_block", "trigger_outcome_label": "tender_war_large_MFE_but_local_4B_required_after_control_premium_blowoff", "current_profile_verdict": "current_profile_partially_correct_local_4B_tender_war_watch_needed", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_2024_window_after_old_2008_CA_candidate", "same_entry_group_id": "R11L86-C32-03", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R11L86-C32-03", "trigger_id": "R11L86-C32-03-S2A-20240913", "symbol": "036560", "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP", "raw_component_scores_before": {"control_premium_score": 60, "tender_price_specificity_score": 50, "acceptance_threshold_score": 40, "financing_visibility_score": 35, "regulatory_or_delisting_path_score": 40, "residual_spread_score": 45, "minority_shareholder_risk_score": 45, "relative_strength_score": 70, "cap_blowoff_risk_score": 90, "execution_risk_score": 75, "source_quality_score": 20, "4B_watch_score": 45, "4C_watch_score": 25}, "weighted_score_before": 77, "stage_label_before": "Stage2-Actionable", "raw_component_scores_after": {"control_premium_score": 60, "tender_price_specificity_score": 50, "acceptance_threshold_score": 40, "financing_visibility_score": 35, "regulatory_or_delisting_path_score": 40, "residual_spread_score": 45, "minority_shareholder_risk_score": 45, "relative_strength_score": 70, "cap_blowoff_risk_score": 90, "execution_risk_score": 80, "source_quality_score": 10, "4B_watch_score": 85, "4C_watch_score": 25}, "weighted_score_after": 73, "stage_label_after": "Stage2-Actionable + local 4B/tender-cap watch", "changed_components": ["residual_spread_score", "acceptance_threshold_score", "regulatory_or_delisting_path_score", "source_quality_score", "cap_blowoff_risk_score", "4B_watch_score"], "component_delta_explanation": "C32 requires control-premium MFE to be evaluated against tender price, remaining spread, acceptance threshold, financing, regulatory/delisting path and minority risk; post-announcement tender caps or tender wars need local 4B/tender-cap watch.", "MFE_90D_pct": 201.31, "MAE_90D_pct": 0.0, "score_return_alignment_label": "tender_war_large_MFE_but_local_4B_required_after_control_premium_blowoff", "current_profile_verdict": "current_profile_partially_correct_local_4B_tender_war_watch_needed"}
{"row_type": "shadow_weight", "axis": "C32_tender_control_premium_acceptance_threshold_residual_spread_cap_bridge_required", "scope": "canonical_archetype_specific", "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP", "baseline_value": 0, "tested_value": 1, "delta": "+1", "reason": "Governance/control-premium rerating requires tender price, residual spread, acceptance threshold, financing, regulatory/delisting path and minority risk; post-announcement tender caps can be low-MFE false positives, while tender wars need local 4B after MFE.", "backtest_effect": "keeps 119860/036560 with tender-cap or tender-war watch; demotes 003410 late tender-cap low-MFE case", "trigger_ids": "R11L86-C32-01-S2A-20240425|R11L86-C32-02-S2FP-20240205|R11L86-C32-03-S2A-20240913", "calibration_usable_count": 3, "new_independent_case_count": 3, "counterexample_count": 1, "confidence": "low", "proposal_type": "canonical_shadow_only", "notes": "source_proxy_only/evidence_url_pending; not production"}
{"row_type": "residual_contribution", "round": "R11", "loop": 86, "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP", "new_independent_case_count": 3, "reused_case_count": 0, "new_symbol_count": 3, "new_trigger_family_count": 3, "tested_existing_calibrated_axes": ["stage2_actionable_evidence_bonus", "price_only_blowoff_blocks_positive_stage", "full_4b_requires_non_price_evidence", "hard_4c_thesis_break_routes_to_4c", "source_proxy_only_blocks_runtime_promotion", "low_MFE_guardrail", "local_4B_watch_before_full_4B_when_MFE_outruns_bridge"], "residual_error_types_found": ["late_tender_cap_low_MFE_false_positive", "tender_control_premium_acceptance_threshold_residual_spread_bridge_required", "tender_war_local_4B_after_MFE", "source_proxy_runtime_promotion_risk", "hard_4C_requires_non_price_tender_failure_or_control_break"], "loop_contribution_label": "canonical_archetype_rule_candidate", "do_not_propose_new_weight_delta": true}
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
- For C32, test a canonical-archetype guard requiring tender price, residual spread, acceptance threshold, financing, regulatory/delisting path and minority/control risk before clean Stage2/Green. Keep hard 4C blocked unless a non-price tender failure, control loss or regulatory block is confirmed.

## 27. Next Round State

```text
completed_round = R11
completed_loop = 86
next_round = R12
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
