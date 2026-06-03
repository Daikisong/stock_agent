# E2R Stock-Web v12 Residual Research — R7 Loop 85 / L7 / C23

## 0. Research Metadata

```json
{
  "research_session": "post_calibrated_sector_archetype_residual_research",
  "mode": "historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12",
  "scheduled_round": "R7",
  "scheduled_loop": 85,
  "round_schedule_status": "valid",
  "round_sector_consistency": "pass",
  "completed_round": "R7",
  "completed_loop": 85,
  "computed_next_round": "R8",
  "computed_next_loop": 85,
  "large_sector_id": "L7_BIO_HEALTHCARE_MEDICAL",
  "canonical_archetype_id": "C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION",
  "fine_archetype_id": "PHARMA_LICENSING_REGULATORY_COMMERCIALIZATION_REVENUE_MARGIN_BRIDGE_VS_PIPELINE_EVENT_FADE",
  "loop_objective": [
    "coverage_gap_fill",
    "counterexample_mining",
    "bio_regulatory_approval_commercialization_guardrail",
    "approval_to_revenue_margin_bridge_test",
    "pipeline_event_vs_commercial_execution_split",
    "local_4B_timing_after_commercialization_MFE",
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
scheduled_round = R7
scheduled_loop = 85
allowed_large_sector = L7_BIO_HEALTHCARE_MEDICAL
selected_large_sector = L7_BIO_HEALTHCARE_MEDICAL
selected_canonical_archetype_id = C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION
computed_next_round = R8
computed_next_loop = 85
round_schedule_status = valid
round_sector_consistency = pass
```

R7 is the bio / healthcare / medical round. This run selects C23 because loop83 tested C24 and loop84 tested C25.

The tested mechanism:

```text
approval / launch / licensing / commercialization headline
→ partner quality and milestone visibility
→ reimbursement or launch timing
→ sales uptake and channel execution
→ gross / OP margin conversion
→ durable rerating or event-MFE fade
```

C23 is not “bio event went up.” It is the bridge from a laboratory or regulatory event into a commercial income statement.

## 3. Previous Coverage / Duplicate Avoidance Check

No-Repeat is used only as a duplicate ledger.

```text
hard_duplicate_key = canonical_archetype_id + symbol + trigger_type + entry_date
```

C23 top-covered symbols include `000100`, `028300`, `UNKNOWN_SYMBOL`, `145020`, `196170`, and `068270`. This run avoids that top-covered set and uses:

```text
170900 / 동아에스티
185750 / 종근당
003850 / 보령
```

All three are treated as new independent C23 bio/pharma commercialization cases for this loop. No hard duplicate is intentionally reused.

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
| 170900 | 동아에스티 | `atlas/symbol_profiles/170/170900.json` | no profile-level CA candidate |
| 185750 | 종근당 | `atlas/symbol_profiles/185/185750.json` | no profile-level CA candidate |
| 003850 | 보령 | `atlas/symbol_profiles/003/003850.json` | 2024-11-29 CA candidate; selected 2024-02-13 forward window before candidate and treated as clean through 180D |

## 5. Historical Eligibility Gate

| case_id | symbol | entry_date | entry_price | forward window | 180D status | calibration_usable |
|---|---:|---|---:|---:|---|---|
| R7L85-C23-01 | 170900 | 2024-02-13 | 66,200 | 180D | clean | true |
| R7L85-C23-02 | 185750 | 2024-02-13 | 114,000 | 180D | clean | true |
| R7L85-C23-03 | 003850 | 2024-02-13 | 12,180 | 180D | clean before later CA candidate | true |

## 6. Canonical Archetype Compression Map

| canonical_archetype_id | fine/deep route | keep / reject logic |
|---|---|---|
| C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION | PHARMA_LICENSING_COMMERCIALIZATION_MFE | keep Stage2 only with approval/launch timing, partner quality, milestone/reimbursement and revenue bridge |
| C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION | PIPELINE_COMMERCIALIZATION_HIGH_MAE_FADE | reject high-MAE pipeline narrative without launch/revenue/margin bridge |
| C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION | COMMERCIAL_STAGE_PHARMA_THEME_FADE | reject sales/portfolio theme when MFE is low-quality and MAE widens |

## 7. Case Selection Summary

| case_id | symbol | company | trigger_type | entry_date | entry_price | MFE_180D_pct | MAE_180D_pct | current_profile_verdict |
|---|---:|---|---|---|---:|---:|---:|---|
| R7L85-C23-01 | 170900 | 동아에스티 | Stage2-Actionable | 2024-02-13 | 66,200 | 32.93 | -6.5 | current_profile_partially_correct_local_4B_watch_needed |
| R7L85-C23-02 | 185750 | 종근당 | Stage2-FalsePositive | 2024-02-13 | 114,000 | 14.21 | -16.14 | current_profile_false_positive_high_MAE_bridge_gap |
| R7L85-C23-03 | 003850 | 보령 | Stage2-FalsePositive | 2024-02-13 | 12,180 | 12.89 | -24.38 | current_profile_false_positive_high_MAE |

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

This MD creates a source-repair queue and a C23 shadow guardrail candidate. It must not be promoted directly into runtime weights until a later source-repair pass attaches primary evidence URLs: approval filing, product launch, partner agreement, milestone schedule, reimbursement, sales uptake, channel execution, gross/OP margin bridge, company disclosure or report evidence.

## 10. Price Data Source Map

| symbol | shard path | profile path |
|---|---|---|
| 170900 | `atlas/ohlcv_tradable_by_symbol_year/170/170900/2024.csv` | `atlas/symbol_profiles/170/170900.json` |
| 185750 | `atlas/ohlcv_tradable_by_symbol_year/185/185750/2024.csv` | `atlas/symbol_profiles/185/185750.json` |
| 003850 | `atlas/ohlcv_tradable_by_symbol_year/003/003850/2024.csv` | `atlas/symbol_profiles/003/003850.json` |

## 11. Case-by-Case Trigger Grid

### Case 1 — 170900 / 동아에스티

C23 commercialization positive with local 4B watch. The February entry created strong MFE into early March. The post-peak path later gave back a meaningful part of the move, so clean Green should require source-repaired approval, launch, partner and sales-uptake evidence.

### Case 2 — 185750 / 종근당

C23 pipeline/commercialization false positive with delayed MFE. The 30D/90D path was weak and high-MAE, and the later MFE arrived only after a drawdown. This is not a clean Stage2 unless milestone, launch and margin bridge are visible at the original entry.

### Case 3 — 003850 / 보령

C23 commercial-stage pharma false positive. The initial MFE was tradable, but the later MAE widened. Portfolio or commercialization narrative without approval-to-sales bridge should remain RiskWatch.

## 12. Trigger-Level OHLC Backtest Tables

| symbol | entry | MFE30 | MAE30 | MFE90 | MAE90 | MFE180 | MAE180 | peak | post-peak DD |
|---|---:|---:|---:|---:|---:|---:|---:|---|---:|
| 170900 | 66,200 | 32.93 | -2.11 | 32.93 | -5.44 | 32.93 | -6.50 | 2024-03-07 / 88,000 | -29.66 |
| 185750 | 114,000 | 2.46 | -8.95 | 2.46 | -16.14 | 14.21 | -16.14 | 2024-08-28 / 130,200 | -15.59 |
| 003850 | 12,180 | 12.89 | -4.93 | 12.89 | -22.58 | 12.89 | -24.38 | 2024-03-20 / 13,750 | -33.02 |

## 13. Current Calibrated Profile Stress Test

| case_id | P0 likely behavior | actual path | verdict |
|---|---|---|---|
| R7L85-C23-01 | Stage2-Actionable if commercialization bridge exists | strong MFE, later drawdown | partially correct; local 4B watch needed |
| R7L85-C23-02 | risk of treating pipeline/commercialization narrative as Stage2 | weak early MFE, high MAE, delayed MFE | false positive / bridge gap |
| R7L85-C23-03 | risk of treating commercial-stage pharma theme as Stage2 | initial MFE then high MAE | false positive |

## 14. Stage2 / Yellow / Green Comparison

```text
green_lateness_ratio = not_applicable
reason = no confirmed Stage3-Green trigger is assigned in this residual MD
```

For C23, the residual is whether bio/pharma commercialization MFE becomes clean Stage2/Green before approval, launch, partner, sales and margin bridge are proven.

## 15. 4B Local vs Full-window Timing Audit

| case_id | local proximity | full-window proximity | verdict |
|---|---:|---:|---|
| R7L85-C23-01 | 0.80 | 0.70 | local 4B watch after commercialization MFE if launch/revenue bridge stalls |
| R7L85-C23-02 | 0.35 | 0.30 | pipeline MFE rejected without approval/launch/revenue/margin bridge |
| R7L85-C23-03 | 0.35 | 0.30 | commercialization theme MFE rejected without approval-to-sales bridge |

## 16. 4C Protection Audit

No hard 4C is promoted from this file.

```text
four_c_protection_label = hard_4C_requires_non_price_regulatory_or_commercial_break
hard_4c_price_only_allowed = false
```

A biotech or pharma drawdown alone is not hard 4C. C23 hard 4C requires confirmed regulatory failure, approval delay, reimbursement failure, partner termination, failed launch, milestone loss, or commercialization thesis break.

## 17. Sector-Specific Rule Candidate

```text
rule_scope = no_new_global_rule
sector_specific_rule_candidate = L7/C23 rows need approval/launch timing, partner quality, milestone/reimbursement, sales uptake and margin bridge before clean Stage2/Green
confidence = low
reason = all evidence rows are source_proxy_only / evidence_url_pending
```

## 18. Canonical-Archetype Rule Candidate

```text
canonical_archetype_id = C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION
candidate_axis = C23_approval_launch_partner_revenue_margin_bridge_required
effect = keep commercialization positives with local 4B watch; demote high-MAE commercialization-theme false positives
production_scoring_changed = false
shadow_weight_only = true
do_not_propose_new_weight_delta = true
```

## 19. Before / After Backtest Comparison

| profile | eligible triggers | avg MFE90 | avg MAE90 | false-positive behavior | verdict |
|---|---:|---:|---:|---|---|
| P0 e2r_2_1_stock_web_calibrated_proxy | 3 | 16.09 | -14.72 | may over-credit commercialization/pipeline event MFE | needs C23 launch/revenue bridge repair |
| P1 canonical shadow bridge profile | 3 | 32.93 on kept positive | demotes 185750/003850 | blocks clean Green until launch/revenue/margin repair | better alignment, source repair required |

## 20. Score-Return Alignment Matrix

| case_id | weighted before | label before | weighted after | label after | alignment |
|---|---:|---|---:|---|---|
| R7L85-C23-01 | 76 | Stage2-Actionable | 73 | Stage2-Actionable + commercialization/local 4B watch | partially aligned |
| R7L85-C23-02 | 58 | Stage2-Watch/FalsePositive | 45 | Rejected-Stage2 / Bio-commercialization RiskWatch | improved |
| R7L85-C23-03 | 58 | Stage2-Watch/FalsePositive | 45 | Rejected-Stage2 / Bio-commercialization RiskWatch | improved |

## 21. Coverage Matrix

| large_sector_id | canonical_archetype_id | fine_archetype_id | positive | counterexample | 4B | 4C | new cases | reused | usable triggers | current errors | sector rule | canonical rule | coverage gap after |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---|---|---|
| L7_BIO_HEALTHCARE_MEDICAL | C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION | PHARMA_LICENSING_REGULATORY_COMMERCIALIZATION_REVENUE_MARGIN_BRIDGE_VS_PIPELINE_EVENT_FADE | 1 | 2 | 3-watch | 0-hard | 3 | 0 | 3 | 2 | no | yes | source repair needed |

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
  - bio_commercialization_theme_false_positive_high_MAE
  - approval_launch_partner_revenue_margin_bridge_required
  - local_4B_late_after_commercialization_MFE
  - source_proxy_runtime_promotion_risk
  - hard_4C_requires_non_price_regulatory_or_commercial_break
new_axis_proposed: false
existing_axis_strengthened:
  - C23_approval_launch_partner_revenue_margin_bridge_required
  - source_proxy_only_blocks_runtime_promotion
  - local_4B_watch_before_full_4B_when_MFE_outruns_bridge
  - hard_4C_requires_non_price_thesis_break
existing_axis_weakened: null
existing_axis_kept:
  - full_4b_requires_non_price_evidence
  - hard_4c_thesis_break_routes_to_4c
sector_specific_rule_candidate: null
canonical_archetype_rule_candidate: C23_approval_launch_partner_revenue_margin_bridge_required
no_new_signal_reason: null
loop_contribution_label: canonical_archetype_rule_candidate
do_not_propose_new_weight_delta: true
```

This loop adds 3 new independent cases, 2 counterexamples, and 2 residual errors for R7/L7_BIO_HEALTHCARE_MEDICAL/C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION.

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
- regulatory approval / filing source
- launch timing and reimbursement detail
- partner quality and milestone schedule
- sales uptake and gross/OP margin conversion
- production scoring implementation
```

## 24. Shadow Weight Calibration

```csv
row_type,axis,scope,large_sector_id,canonical_archetype_id,baseline_value,tested_value,delta,reason,backtest_effect,trigger_ids,calibration_usable_count,new_independent_case_count,counterexample_count,confidence,proposal_type,notes
shadow_weight,C23_approval_launch_partner_revenue_margin_bridge_required,canonical_archetype_specific,L7_BIO_HEALTHCARE_MEDICAL,C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION,0,1,+1,"Require approval/launch timing, partner quality, milestone/reimbursement, sales uptake and margin bridge before clean Stage2/Green","keeps 170900 with local 4B commercialization watch; demotes 185750/003850","R7L85-C23-01-S2A-20240213|R7L85-C23-02-S2FP-20240213|R7L85-C23-03-S2FP-20240213",3,3,2,low,canonical_shadow_only,"source repair required; not production"
```

## 25. Machine-Readable Rows

```jsonl
{"row_type": "price_source_validation", "source": "Songdaiki/stock-web", "source_url": "https://github.com/Songdaiki/stock-web", "manifest_path": "atlas/manifest.json", "schema_path": "atlas/schema.json", "universe_path": "atlas/universe/all_symbols.csv", "manifest_max_date": "2026-02-20", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "raw_shard_root": "atlas/ohlcv_raw_by_symbol_year", "validation_status": "usable_for_historical_calibration"}
{"row_type": "case", "case_id": "R7L85-C23-01", "symbol": "170900", "company_name": "동아에스티", "round": "R7", "loop": 85, "large_sector_id": "L7_BIO_HEALTHCARE_MEDICAL", "canonical_archetype_id": "C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION", "fine_archetype_id": "PHARMA_LICENSING_REGULATORY_COMMERCIALIZATION_REVENUE_MARGIN_BRIDGE_VS_PIPELINE_EVENT_FADE", "case_type": "pharma_commercialization_pipeline_positive_with_local_4B_watch", "positive_or_counterexample": "positive", "best_trigger": "R7L85-C23-01-S2A-20240213", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "commercialization_MFE_positive_but_local_4B_required", "current_profile_verdict": "current_profile_partially_correct_local_4B_watch_needed", "price_source": "Songdaiki/stock-web", "notes": "C23 can keep Stage2 only when approval/licensing event converts into launch timing, reimbursement, partner quality, revenue and margin bridge."}
{"row_type": "trigger", "trigger_id": "R7L85-C23-01-S2A-20240213", "case_id": "R7L85-C23-01", "symbol": "170900", "company_name": "동아에스티", "round": "R7", "loop": 85, "large_sector_id": "L7_BIO_HEALTHCARE_MEDICAL", "canonical_archetype_id": "C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION", "fine_archetype_id": "PHARMA_LICENSING_REGULATORY_COMMERCIALIZATION_REVENUE_MARGIN_BRIDGE_VS_PIPELINE_EVENT_FADE", "loop_objective": "coverage_gap_fill|counterexample_mining|bio_regulatory_approval_commercialization_guardrail|approval_to_revenue_margin_bridge|canonical_archetype_compression", "trigger_type": "Stage2-Actionable", "trigger_date": "2024-02-13", "evidence_available_at_that_date": "pharma pipeline/regulatory commercialization and overseas licensing proxy; primary approval, launch and revenue evidence pending", "evidence_source": "source_proxy_only; evidence_url_pending", "stage2_evidence_fields": ["regulatory_or_commercialization_proxy", "partner_or_launch_proxy", "revenue_bridge_proxy"], "stage3_evidence_fields": ["approval_or_launch_timing", "partner_quality", "milestone_or_reimbursement", "sales_uptake", "gross_or_OP_margin_conversion"], "stage4b_evidence_fields": ["bio_event_MFE_without_sales_bridge", "post_peak_drawdown", "source_proxy_gap"], "stage4c_evidence_fields": ["hard_regulatory_failure_or_commercial_launch_break_watch_only"], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/170/170900/2024.csv", "profile_path": "atlas/symbol_profiles/170/170900.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "entry_date": "2024-02-13", "entry_price": 66200, "MFE_30D_pct": 32.93, "MFE_90D_pct": 32.93, "MFE_180D_pct": 32.93, "MFE_1Y_pct": null, "MFE_2Y_pct": null, "MAE_30D_pct": -2.11, "MAE_90D_pct": -5.44, "MAE_180D_pct": -6.5, "MAE_1Y_pct": null, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2024-03-07", "peak_price": 88000, "drawdown_after_peak_pct": -29.66, "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": 0.8, "four_b_full_window_peak_proximity": 0.7, "four_b_timing_verdict": "local_4B_watch_after_commercialization_MFE_if_launch_revenue_bridge_stalls", "four_b_evidence_type": ["bio_event_MFE_without_revenue_bridge", "post_peak_drawdown", "source_proxy_gap"], "four_c_protection_label": "hard_4C_requires_non_price_regulatory_or_commercial_break", "trigger_outcome_label": "commercialization_MFE_positive_but_local_4B_required", "current_profile_verdict": "current_profile_partially_correct_local_4B_watch_needed", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_2024_window_no_profile_CA_candidate", "same_entry_group_id": "R7L85-C23-01", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R7L85-C23-01", "trigger_id": "R7L85-C23-01-S2A-20240213", "symbol": "170900", "large_sector_id": "L7_BIO_HEALTHCARE_MEDICAL", "canonical_archetype_id": "C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION", "raw_component_scores_before": {"regulatory_specificity_score": 45, "approval_or_launch_score": 40, "partner_quality_score": 40, "milestone_visibility_score": 35, "revenue_bridge_score": 40, "margin_bridge_score": 35, "cash_runway_or_balance_score": 45, "revision_score": 40, "relative_strength_score": 65, "event_blowoff_risk_score": 65, "execution_risk_score": 50, "source_quality_score": 20, "4B_watch_score": 45}, "weighted_score_before": 76, "stage_label_before": "Stage2-Actionable", "raw_component_scores_after": {"regulatory_specificity_score": 45, "approval_or_launch_score": 40, "partner_quality_score": 40, "milestone_visibility_score": 35, "revenue_bridge_score": 40, "margin_bridge_score": 35, "cash_runway_or_balance_score": 45, "revision_score": 40, "relative_strength_score": 65, "event_blowoff_risk_score": 75, "execution_risk_score": 50, "source_quality_score": 10, "4B_watch_score": 80}, "weighted_score_after": 73, "stage_label_after": "Stage2-Actionable + commercialization/local 4B watch", "changed_components": ["approval_or_launch_score", "milestone_visibility_score", "revenue_bridge_score", "margin_bridge_score", "source_quality_score", "execution_risk_score", "4B_watch_score"], "component_delta_explanation": "C23 requires regulatory/commercialization event to convert into launch timing, partner quality, milestone/reimbursement, sales uptake and margin bridge before clean Stage2/Green; event MFE alone is demoted or wrapped with local 4B/high-MAE watch.", "MFE_90D_pct": 32.93, "MAE_90D_pct": -5.44, "score_return_alignment_label": "commercialization_MFE_positive_but_local_4B_required", "current_profile_verdict": "current_profile_partially_correct_local_4B_watch_needed"}
{"row_type": "case", "case_id": "R7L85-C23-02", "symbol": "185750", "company_name": "종근당", "round": "R7", "loop": 85, "large_sector_id": "L7_BIO_HEALTHCARE_MEDICAL", "canonical_archetype_id": "C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION", "fine_archetype_id": "PHARMA_LICENSING_REGULATORY_COMMERCIALIZATION_REVENUE_MARGIN_BRIDGE_VS_PIPELINE_EVENT_FADE", "case_type": "pharma_pipeline_commercialization_high_MAE_false_positive", "positive_or_counterexample": "counterexample", "best_trigger": "R7L85-C23-02-S2FP-20240213", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "delayed_MFE_but_high_MAE_commercialization_bridge_false_positive", "current_profile_verdict": "current_profile_false_positive_high_MAE_bridge_gap", "price_source": "Songdaiki/stock-web", "notes": "Pipeline/commercialization narrative should stay RiskWatch unless partner milestone, launch cadence, revenue contribution and margin bridge are explicit."}
{"row_type": "trigger", "trigger_id": "R7L85-C23-02-S2FP-20240213", "case_id": "R7L85-C23-02", "symbol": "185750", "company_name": "종근당", "round": "R7", "loop": 85, "large_sector_id": "L7_BIO_HEALTHCARE_MEDICAL", "canonical_archetype_id": "C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION", "fine_archetype_id": "PHARMA_LICENSING_REGULATORY_COMMERCIALIZATION_REVENUE_MARGIN_BRIDGE_VS_PIPELINE_EVENT_FADE", "loop_objective": "coverage_gap_fill|counterexample_mining|bio_regulatory_approval_commercialization_guardrail|approval_to_revenue_margin_bridge|canonical_archetype_compression", "trigger_type": "Stage2-FalsePositive", "trigger_date": "2024-02-13", "evidence_available_at_that_date": "large pharma pipeline/commercialization and licensing narrative proxy without confirmed product launch, milestone, revenue and margin bridge", "evidence_source": "source_proxy_only; evidence_url_pending", "stage2_evidence_fields": ["regulatory_or_commercialization_proxy", "partner_or_launch_proxy", "revenue_bridge_proxy"], "stage3_evidence_fields": ["approval_or_launch_timing", "partner_quality", "milestone_or_reimbursement", "sales_uptake", "gross_or_OP_margin_conversion"], "stage4b_evidence_fields": ["bio_event_MFE_without_sales_bridge", "post_peak_drawdown", "source_proxy_gap"], "stage4c_evidence_fields": ["hard_regulatory_failure_or_commercial_launch_break_watch_only"], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/185/185750/2024.csv", "profile_path": "atlas/symbol_profiles/185/185750.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "entry_date": "2024-02-13", "entry_price": 114000, "MFE_30D_pct": 2.46, "MFE_90D_pct": 2.46, "MFE_180D_pct": 14.21, "MFE_1Y_pct": null, "MFE_2Y_pct": null, "MAE_30D_pct": -8.95, "MAE_90D_pct": -16.14, "MAE_180D_pct": -16.14, "MAE_1Y_pct": null, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2024-08-28", "peak_price": 130200, "drawdown_after_peak_pct": -15.59, "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": 0.35, "four_b_full_window_peak_proximity": 0.3, "four_b_timing_verdict": "pharma_pipeline_MFE_rejected_without_approval_launch_revenue_margin_bridge", "four_b_evidence_type": ["bio_event_MFE_without_revenue_bridge", "post_peak_drawdown", "source_proxy_gap"], "four_c_protection_label": "hard_4C_requires_non_price_regulatory_or_commercial_break", "trigger_outcome_label": "delayed_MFE_but_high_MAE_commercialization_bridge_false_positive", "current_profile_verdict": "current_profile_false_positive_high_MAE_bridge_gap", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_2024_window_no_profile_CA_candidate", "same_entry_group_id": "R7L85-C23-02", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R7L85-C23-02", "trigger_id": "R7L85-C23-02-S2FP-20240213", "symbol": "185750", "large_sector_id": "L7_BIO_HEALTHCARE_MEDICAL", "canonical_archetype_id": "C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION", "raw_component_scores_before": {"regulatory_specificity_score": 25, "approval_or_launch_score": 15, "partner_quality_score": 15, "milestone_visibility_score": 10, "revenue_bridge_score": 10, "margin_bridge_score": 5, "cash_runway_or_balance_score": 35, "revision_score": 15, "relative_strength_score": 35, "event_blowoff_risk_score": 70, "execution_risk_score": 75, "source_quality_score": 15, "4B_watch_score": 70}, "weighted_score_before": 58, "stage_label_before": "Stage2-Watch/FalsePositive", "raw_component_scores_after": {"regulatory_specificity_score": 25, "approval_or_launch_score": 0, "partner_quality_score": 15, "milestone_visibility_score": 0, "revenue_bridge_score": 0, "margin_bridge_score": 0, "cash_runway_or_balance_score": 35, "revision_score": 15, "relative_strength_score": 35, "event_blowoff_risk_score": 70, "execution_risk_score": 85, "source_quality_score": 5, "4B_watch_score": 85}, "weighted_score_after": 45, "stage_label_after": "Rejected-Stage2 / Bio-commercialization RiskWatch", "changed_components": ["approval_or_launch_score", "milestone_visibility_score", "revenue_bridge_score", "margin_bridge_score", "source_quality_score", "execution_risk_score", "4B_watch_score"], "component_delta_explanation": "C23 requires regulatory/commercialization event to convert into launch timing, partner quality, milestone/reimbursement, sales uptake and margin bridge before clean Stage2/Green; event MFE alone is demoted or wrapped with local 4B/high-MAE watch.", "MFE_90D_pct": 2.46, "MAE_90D_pct": -16.14, "score_return_alignment_label": "delayed_MFE_but_high_MAE_commercialization_bridge_false_positive", "current_profile_verdict": "current_profile_false_positive_high_MAE_bridge_gap"}
{"row_type": "case", "case_id": "R7L85-C23-03", "symbol": "003850", "company_name": "보령", "round": "R7", "loop": 85, "large_sector_id": "L7_BIO_HEALTHCARE_MEDICAL", "canonical_archetype_id": "C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION", "fine_archetype_id": "PHARMA_LICENSING_REGULATORY_COMMERCIALIZATION_REVENUE_MARGIN_BRIDGE_VS_PIPELINE_EVENT_FADE", "case_type": "pharma_commercialization_theme_high_MAE_false_positive", "positive_or_counterexample": "counterexample", "best_trigger": "R7L85-C23-03-S2FP-20240213", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "initial_MFE_then_high_MAE_pharma_commercialization_false_positive", "current_profile_verdict": "current_profile_false_positive_high_MAE", "price_source": "Songdaiki/stock-web", "notes": "Commercial-stage pharma theme should not be clean Stage2 unless sales uptake, reimbursement/channel execution and margin conversion are visible at entry."}
{"row_type": "trigger", "trigger_id": "R7L85-C23-03-S2FP-20240213", "case_id": "R7L85-C23-03", "symbol": "003850", "company_name": "보령", "round": "R7", "loop": 85, "large_sector_id": "L7_BIO_HEALTHCARE_MEDICAL", "canonical_archetype_id": "C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION", "fine_archetype_id": "PHARMA_LICENSING_REGULATORY_COMMERCIALIZATION_REVENUE_MARGIN_BRIDGE_VS_PIPELINE_EVENT_FADE", "loop_objective": "coverage_gap_fill|counterexample_mining|bio_regulatory_approval_commercialization_guardrail|approval_to_revenue_margin_bridge|canonical_archetype_compression", "trigger_type": "Stage2-FalsePositive", "trigger_date": "2024-02-13", "evidence_available_at_that_date": "pharma product commercialization / specialty drug portfolio and distribution narrative proxy without confirmed approval-to-sales bridge", "evidence_source": "source_proxy_only; evidence_url_pending", "stage2_evidence_fields": ["regulatory_or_commercialization_proxy", "partner_or_launch_proxy", "revenue_bridge_proxy"], "stage3_evidence_fields": ["approval_or_launch_timing", "partner_quality", "milestone_or_reimbursement", "sales_uptake", "gross_or_OP_margin_conversion"], "stage4b_evidence_fields": ["bio_event_MFE_without_sales_bridge", "post_peak_drawdown", "source_proxy_gap"], "stage4c_evidence_fields": ["hard_regulatory_failure_or_commercial_launch_break_watch_only"], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/003/003850/2024.csv", "profile_path": "atlas/symbol_profiles/003/003850.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "entry_date": "2024-02-13", "entry_price": 12180, "MFE_30D_pct": 12.89, "MFE_90D_pct": 12.89, "MFE_180D_pct": 12.89, "MFE_1Y_pct": null, "MFE_2Y_pct": null, "MAE_30D_pct": -4.93, "MAE_90D_pct": -22.58, "MAE_180D_pct": -24.38, "MAE_1Y_pct": null, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2024-03-20", "peak_price": 13750, "drawdown_after_peak_pct": -33.02, "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": 0.35, "four_b_full_window_peak_proximity": 0.3, "four_b_timing_verdict": "commercialization_theme_MFE_rejected_without_approval_to_sales_margin_bridge", "four_b_evidence_type": ["bio_event_MFE_without_revenue_bridge", "post_peak_drawdown", "source_proxy_gap"], "four_c_protection_label": "hard_4C_requires_non_price_regulatory_or_commercial_break", "trigger_outcome_label": "initial_MFE_then_high_MAE_pharma_commercialization_false_positive", "current_profile_verdict": "current_profile_false_positive_high_MAE", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_before_2024_11_29_CA_candidate", "same_entry_group_id": "R7L85-C23-03", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R7L85-C23-03", "trigger_id": "R7L85-C23-03-S2FP-20240213", "symbol": "003850", "large_sector_id": "L7_BIO_HEALTHCARE_MEDICAL", "canonical_archetype_id": "C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION", "raw_component_scores_before": {"regulatory_specificity_score": 25, "approval_or_launch_score": 15, "partner_quality_score": 15, "milestone_visibility_score": 10, "revenue_bridge_score": 10, "margin_bridge_score": 5, "cash_runway_or_balance_score": 35, "revision_score": 15, "relative_strength_score": 35, "event_blowoff_risk_score": 70, "execution_risk_score": 75, "source_quality_score": 15, "4B_watch_score": 70}, "weighted_score_before": 58, "stage_label_before": "Stage2-Watch/FalsePositive", "raw_component_scores_after": {"regulatory_specificity_score": 25, "approval_or_launch_score": 0, "partner_quality_score": 15, "milestone_visibility_score": 0, "revenue_bridge_score": 0, "margin_bridge_score": 0, "cash_runway_or_balance_score": 35, "revision_score": 15, "relative_strength_score": 35, "event_blowoff_risk_score": 70, "execution_risk_score": 85, "source_quality_score": 5, "4B_watch_score": 85}, "weighted_score_after": 45, "stage_label_after": "Rejected-Stage2 / Bio-commercialization RiskWatch", "changed_components": ["approval_or_launch_score", "milestone_visibility_score", "revenue_bridge_score", "margin_bridge_score", "source_quality_score", "execution_risk_score", "4B_watch_score"], "component_delta_explanation": "C23 requires regulatory/commercialization event to convert into launch timing, partner quality, milestone/reimbursement, sales uptake and margin bridge before clean Stage2/Green; event MFE alone is demoted or wrapped with local 4B/high-MAE watch.", "MFE_90D_pct": 12.89, "MAE_90D_pct": -22.58, "score_return_alignment_label": "initial_MFE_then_high_MAE_pharma_commercialization_false_positive", "current_profile_verdict": "current_profile_false_positive_high_MAE"}
{"row_type": "shadow_weight", "axis": "C23_approval_launch_partner_revenue_margin_bridge_required", "scope": "canonical_archetype_specific", "large_sector_id": "L7_BIO_HEALTHCARE_MEDICAL", "canonical_archetype_id": "C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION", "baseline_value": 0, "tested_value": 1, "delta": "+1", "reason": "Bio/pharma regulatory-commercialization rerating requires approval or launch timing, partner quality, milestone or reimbursement, sales uptake and margin bridge; pipeline/commercialization theme MFE without bridge fades or needs local 4B/high-MAE watch.", "backtest_effect": "keeps 170900 with local 4B commercialization watch; demotes 185750/003850 high-MAE commercialization-theme false positives", "trigger_ids": "R7L85-C23-01-S2A-20240213|R7L85-C23-02-S2FP-20240213|R7L85-C23-03-S2FP-20240213", "calibration_usable_count": 3, "new_independent_case_count": 3, "counterexample_count": 2, "confidence": "low", "proposal_type": "canonical_shadow_only", "notes": "source_proxy_only/evidence_url_pending; not production"}
{"row_type": "residual_contribution", "round": "R7", "loop": 85, "large_sector_id": "L7_BIO_HEALTHCARE_MEDICAL", "canonical_archetype_id": "C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION", "new_independent_case_count": 3, "reused_case_count": 0, "new_symbol_count": 3, "new_trigger_family_count": 3, "tested_existing_calibrated_axes": ["stage2_actionable_evidence_bonus", "price_only_blowoff_blocks_positive_stage", "full_4b_requires_non_price_evidence", "hard_4c_thesis_break_routes_to_4c", "source_proxy_only_blocks_runtime_promotion", "high_MAE_guardrail", "local_4B_watch_before_full_4B_when_MFE_outruns_bridge"], "residual_error_types_found": ["bio_commercialization_theme_false_positive_high_MAE", "approval_launch_partner_revenue_margin_bridge_required", "local_4B_late_after_commercialization_MFE", "source_proxy_runtime_promotion_risk", "hard_4C_requires_non_price_regulatory_or_commercial_break"], "loop_contribution_label": "canonical_archetype_rule_candidate", "do_not_propose_new_weight_delta": true}
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
- For C23, test a canonical-archetype guard requiring approval/launch timing, partner quality, milestone/reimbursement, sales uptake and gross/OP margin conversion before clean Stage2/Green. Keep hard 4C blocked unless a non-price regulatory or commercial thesis break is confirmed.

## 27. Next Round State

```text
completed_round = R7
completed_loop = 85
next_round = R8
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
