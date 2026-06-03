# E2R Stock-Web v12 Residual Research — R7 Loop 86 / L7 / C24

## 0. Research Metadata

```json
{
  "research_session": "post_calibrated_sector_archetype_residual_research",
  "mode": "historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12",
  "scheduled_round": "R7",
  "scheduled_loop": 86,
  "round_schedule_status": "valid",
  "round_sector_consistency": "pass",
  "completed_round": "R7",
  "completed_loop": 86,
  "computed_next_round": "R8",
  "computed_next_loop": 86,
  "large_sector_id": "L7_BIO_HEALTHCARE_MEDICAL",
  "canonical_archetype_id": "C24_BIO_TRIAL_DATA_EVENT_RISK",
  "fine_archetype_id": "ADC_BIOSIMILAR_CELL_THERAPY_TRIAL_DATA_LICENSE_MILESTONE_REIMBURSEMENT_BRIDGE_VS_EVENT_BLOWOFF_FADE",
  "loop_objective": [
    "coverage_gap_fill",
    "counterexample_mining",
    "bio_trial_data_event_risk_guardrail",
    "trial_data_to_license_milestone_reimbursement_bridge_test",
    "bio_event_MFE_vs_non_price_data_quality_and_commercial_bridge_test",
    "local_4B_timing_after_bio_event_MFE",
    "hard_4C_non_price_trial_failure_or_regulatory_break_protection",
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
scheduled_loop = 86
allowed_large_sector = L7_BIO_HEALTHCARE_MEDICAL
selected_large_sector = L7_BIO_HEALTHCARE_MEDICAL
selected_canonical_archetype_id = C24_BIO_TRIAL_DATA_EVENT_RISK
computed_next_round = R8
computed_next_loop = 86
round_schedule_status = valid
round_sector_consistency = pass
```

R7 is the bio / healthcare / medical round. This run selects C24 because loop85 R7 used C23 and loop84 R7 used C25. C24 is the trial/data/event-risk bucket.

The tested mechanism:

```text
trial data / regulatory data / licensing headline
→ data durability and regulatory path
→ partner quality and milestone visibility
→ reimbursement or launch path
→ revenue and gross/OP margin conversion
→ durable rerating or event blowoff
```

C24 is not the press conference. It is the data room: an event only becomes E2R when the data, regulator, partner, milestone and commercial bridge line up.

## 3. Previous Coverage / Duplicate Avoidance Check

No-Repeat is used only as a duplicate ledger.

```text
hard_duplicate_key = canonical_archetype_id + symbol + trigger_type + entry_date
```

C24 top-covered symbols include `000100`, `215600`, `009420`, `298380`, `028300`, and `039200`. This run avoids that top-covered set and uses:

```text
000250 / 삼천당제약
141080 / 리가켐바이오
174900 / 앱클론
```

All three are treated as new independent C24 bio trial/data event-risk cases for this loop. No hard duplicate is intentionally reused.

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
| 000250 | 삼천당제약 | `atlas/symbol_profiles/000/000250.json` | old 2002 CA candidate; selected 2024 forward window clean |
| 141080 | 리가켐바이오 | `atlas/symbol_profiles/141/141080.json` | 2024-04-23 CA candidate; selected 2024-06-20 forward window after candidate |
| 174900 | 앱클론 | `atlas/symbol_profiles/174/174900.json` | old 2020 CA candidates; selected 2024 forward window clean |

## 5. Historical Eligibility Gate

| case_id | symbol | entry_date | entry_price | forward window | 180D status | calibration_usable |
|---|---:|---|---:|---:|---|---|
| R7L86-C24-01 | 000250 | 2024-03-18 | 86,500 | 180D | clean | true |
| R7L86-C24-02 | 141080 | 2024-06-20 | 75,500 | 180D | clean after 2024-04-23 CA candidate | true |
| R7L86-C24-03 | 174900 | 2024-03-05 | 21,100 | 180D | clean | true |

## 6. Canonical Archetype Compression Map

| canonical_archetype_id | fine/deep route | keep / reject logic |
|---|---|---|
| C24_BIO_TRIAL_DATA_EVENT_RISK | BIOSIMILAR_REGULATORY_DATA_LICENSE | keep Stage2 with filing clarity, partner milestone, launch/reimbursement and margin bridge |
| C24_BIO_TRIAL_DATA_EVENT_RISK | ADC_PLATFORM_DATA_LICENSE_MILESTONE | keep Stage2 with data durability, partner quality, milestone economics and commercial bridge |
| C24_BIO_TRIAL_DATA_EVENT_RISK | CELL_THERAPY_TRIAL_DATA_EVENT_BLOWOFF | reject event MFE without pivotal data, partner, regulatory and revenue bridge |

## 7. Case Selection Summary

| case_id | symbol | company | trigger_type | entry_date | entry_price | MFE_180D_pct | MAE_180D_pct | current_profile_verdict |
|---|---:|---|---|---|---:|---:|---:|---|
| R7L86-C24-01 | 000250 | 삼천당제약 | Stage2-Actionable | 2024-03-18 | 86,500 | 165.9 | -10.06 | current_profile_partially_correct_local_4B_watch_needed |
| R7L86-C24-02 | 141080 | 리가켐바이오 | Stage2-Actionable | 2024-06-20 | 75,500 | 74.17 | -11.39 | current_profile_partially_correct_data_milestone_watch_needed |
| R7L86-C24-03 | 174900 | 앱클론 | Stage2-FalsePositive | 2024-03-05 | 21,100 | 4.98 | -48.67 | current_profile_false_positive_high_MAE_event_blowoff |

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

This MD creates a source-repair queue and a C24 shadow guardrail candidate. It must not be promoted directly into runtime weights until a later source-repair pass attaches primary evidence URLs: trial/data release, regulatory filing, partner agreement, milestone schedule, reimbursement/launch path, sales uptake, margin bridge, disclosure or report evidence.

## 10. Price Data Source Map

| symbol | shard path | profile path |
|---|---|---|
| 000250 | `atlas/ohlcv_tradable_by_symbol_year/000/000250/2024.csv` | `atlas/symbol_profiles/000/000250.json` |
| 141080 | `atlas/ohlcv_tradable_by_symbol_year/141/141080/2024.csv` and `2025.csv` | `atlas/symbol_profiles/141/141080.json` |
| 174900 | `atlas/ohlcv_tradable_by_symbol_year/174/174900/2024.csv` | `atlas/symbol_profiles/174/174900.json` |

## 11. Case-by-Case Trigger Grid

### Case 1 — 000250 / 삼천당제약

C24 biosimilar/regulatory data positive with local 4B watch. The March event produced a large MFE. It is kept positive, but clean Green requires filing clarity, partner milestone, reimbursement/launch and margin bridge.

### Case 2 — 141080 / 리가켐바이오

C24 ADC platform/data-license positive with local 4B watch. The post-CA clean window produced a strong MFE into autumn. It needs data durability, partner quality and milestone/commercial economics before clean Green.

### Case 3 — 174900 / 앱클론

C24 cell-therapy trial-data event false positive. The event spike was already mature at entry and then turned into a high-MAE path. This is the row that rejects trial-data MFE without pivotal data, partner, regulatory path and revenue bridge.

## 12. Trigger-Level OHLC Backtest Tables

| symbol | entry | MFE30 | MAE30 | MFE90 | MAE90 | MFE180 | MAE180 | peak | post-peak DD |
|---|---:|---:|---:|---:|---:|---:|---:|---|---:|
| 000250 | 86,500 | 74.80 | -10.06 | 165.90 | -10.06 | 165.90 | -10.06 | 2024-07-10 / 230,000 | -44.17 |
| 141080 | 75,500 | 15.50 | -10.33 | 39.07 | -11.39 | 74.17 | -11.39 | 2024-10-21 / 131,500 | -31.94 |
| 174900 | 21,100 | 4.98 | -24.08 | 4.98 | -31.52 | 4.98 | -48.67 | 2024-03-05 / 22,150 | -51.11 |

## 13. Current Calibrated Profile Stress Test

| case_id | P0 likely behavior | actual path | verdict |
|---|---|---|---|
| R7L86-C24-01 | Stage2-Actionable if data/regulatory bridge exists | huge MFE, later drawdown | partially correct; local 4B/data-commercial bridge needed |
| R7L86-C24-02 | Stage2-Actionable if ADC platform data bridge exists | large MFE, later drawdown | partially correct; milestone/commercial bridge needed |
| R7L86-C24-03 | risk of treating trial-data event as Stage2 | low MFE / severe MAE | false positive / high-MAE guardrail |

## 14. Stage2 / Yellow / Green Comparison

```text
green_lateness_ratio = not_applicable
reason = no confirmed Stage3-Green trigger is assigned in this residual MD
```

For C24, the residual is whether bio event MFE becomes clean Stage2/Green before data durability, regulatory path, partner milestone and commercial bridge are proven.

## 15. 4B Local vs Full-window Timing Audit

| case_id | local proximity | full-window proximity | verdict |
|---|---:|---:|---|
| R7L86-C24-01 | 0.82 | 0.72 | local 4B watch after biosimilar event MFE if regulatory/license bridge stalls |
| R7L86-C24-02 | 0.82 | 0.72 | local 4B watch after ADC event MFE if data/milestone bridge stalls |
| R7L86-C24-03 | 0.35 | 0.30 | trial-data event MFE rejected without pivotal data/regulatory/revenue bridge |

## 16. 4C Protection Audit

No hard 4C is promoted from this file.

```text
four_c_protection_label = hard_4C_requires_non_price_trial_failure_or_regulatory_break
hard_4c_price_only_allowed = false
```

Price drawdown alone is not hard 4C. C24 hard 4C requires confirmed trial failure, data-quality break, safety issue, regulatory delay/rejection, partner termination, milestone failure, financing shock or commercialization thesis break.

## 17. Sector-Specific Rule Candidate

```text
rule_scope = no_new_global_rule
sector_specific_rule_candidate = L7/C24 rows need data durability, regulatory path, partner milestone, reimbursement/launch and revenue/margin bridge before clean Stage2/Green
confidence = low
reason = all evidence rows are source_proxy_only / evidence_url_pending
```

## 18. Canonical-Archetype Rule Candidate

```text
canonical_archetype_id = C24_BIO_TRIAL_DATA_EVENT_RISK
candidate_axis = C24_trial_data_regulatory_partner_milestone_commercial_bridge_required
effect = keep data-event positives with local 4B watch; demote high-MAE event blowoffs
production_scoring_changed = false
shadow_weight_only = true
do_not_propose_new_weight_delta = true
```

## 19. Before / After Backtest Comparison

| profile | eligible triggers | avg MFE90 | avg MAE90 | false-positive behavior | verdict |
|---|---:|---:|---:|---|---|
| P0 e2r_2_1_stock_web_calibrated_proxy | 3 | 69.98 | -17.66 | may over-credit bio event MFE without commercial bridge | needs C24 data/milestone bridge repair |
| P1 canonical shadow bridge profile | 3 | 102.49 on kept positives | demotes 174900 | better alignment, source repair required |

## 20. Score-Return Alignment Matrix

| case_id | weighted before | label before | weighted after | label after | alignment |
|---|---:|---|---:|---|---|
| R7L86-C24-01 | 78 | Stage2-Actionable | 73 | Stage2-Actionable + local 4B/data-commercial bridge watch | partially aligned |
| R7L86-C24-02 | 78 | Stage2-Actionable | 73 | Stage2-Actionable + local 4B/data-commercial bridge watch | partially aligned |
| R7L86-C24-03 | 58 | Stage2-Watch/FalsePositive | 42 | Rejected-Stage2 / Bio-event RiskWatch | improved |

## 21. Coverage Matrix

| large_sector_id | canonical_archetype_id | fine_archetype_id | positive | counterexample | 4B | 4C | new cases | reused | usable triggers | current errors | sector rule | canonical rule | coverage gap after |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---|---|---|
| L7_BIO_HEALTHCARE_MEDICAL | C24_BIO_TRIAL_DATA_EVENT_RISK | ADC_BIOSIMILAR_CELL_THERAPY_TRIAL_DATA_LICENSE_MILESTONE_REIMBURSEMENT_BRIDGE_VS_EVENT_BLOWOFF_FADE | 2 | 1 | 3-watch | 0-hard | 3 | 0 | 3 | 2 | no | yes | source repair needed |

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
  - bio_trial_data_event_false_positive_high_MAE
  - data_regulatory_partner_milestone_commercial_bridge_required
  - local_4B_late_after_bio_event_MFE
  - source_proxy_runtime_promotion_risk
  - hard_4C_requires_non_price_trial_or_regulatory_break
new_axis_proposed: false
existing_axis_strengthened:
  - C24_trial_data_regulatory_partner_milestone_commercial_bridge_required
  - source_proxy_only_blocks_runtime_promotion
  - local_4B_watch_before_full_4B_when_MFE_outruns_bridge
  - hard_4C_requires_non_price_thesis_break
existing_axis_weakened: null
existing_axis_kept:
  - full_4b_requires_non_price_evidence
  - hard_4c_thesis_break_routes_to_4c
sector_specific_rule_candidate: null
canonical_archetype_rule_candidate: C24_trial_data_regulatory_partner_milestone_commercial_bridge_required
no_new_signal_reason: null
loop_contribution_label: canonical_archetype_rule_candidate
do_not_propose_new_weight_delta: true
```

This loop adds 3 new independent cases, 1 counterexample, and 2 residual errors for R7/L7_BIO_HEALTHCARE_MEDICAL/C24_BIO_TRIAL_DATA_EVENT_RISK.

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
- trial/data source
- regulatory filing or approval path
- partner milestone schedule
- reimbursement / launch path
- revenue and margin conversion
- production scoring implementation
```

## 24. Shadow Weight Calibration

```csv
row_type,axis,scope,large_sector_id,canonical_archetype_id,baseline_value,tested_value,delta,reason,backtest_effect,trigger_ids,calibration_usable_count,new_independent_case_count,counterexample_count,confidence,proposal_type,notes
shadow_weight,C24_trial_data_regulatory_partner_milestone_commercial_bridge_required,canonical_archetype_specific,L7_BIO_HEALTHCARE_MEDICAL,C24_BIO_TRIAL_DATA_EVENT_RISK,0,1,+1,"Require data durability, regulatory path, partner milestone, reimbursement/launch and revenue/margin bridge before clean Stage2/Green","keeps 000250/141080 with local 4B/data-commercial bridge watch; demotes 174900","R7L86-C24-01-S2A-20240318|R7L86-C24-02-S2A-20240620|R7L86-C24-03-S2FP-20240305",3,3,1,low,canonical_shadow_only,"source repair required; not production"
```

## 25. Machine-Readable Rows

```jsonl
{"row_type": "price_source_validation", "source": "Songdaiki/stock-web", "source_url": "https://github.com/Songdaiki/stock-web", "manifest_path": "atlas/manifest.json", "schema_path": "atlas/schema.json", "universe_path": "atlas/universe/all_symbols.csv", "manifest_max_date": "2026-02-20", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "raw_shard_root": "atlas/ohlcv_raw_by_symbol_year", "validation_status": "usable_for_historical_calibration"}
{"row_type": "case", "case_id": "R7L86-C24-01", "symbol": "000250", "company_name": "삼천당제약", "round": "R7", "loop": 86, "large_sector_id": "L7_BIO_HEALTHCARE_MEDICAL", "canonical_archetype_id": "C24_BIO_TRIAL_DATA_EVENT_RISK", "fine_archetype_id": "ADC_BIOSIMILAR_CELL_THERAPY_TRIAL_DATA_LICENSE_MILESTONE_REIMBURSEMENT_BRIDGE_VS_EVENT_BLOWOFF_FADE", "case_type": "biosimilar_regulatory_data_event_positive_with_local_4B_watch", "positive_or_counterexample": "positive", "best_trigger": "R7L86-C24-01-S2A-20240318", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "large_positive_MFE_but_trial_regulatory_license_bridge_required", "current_profile_verdict": "current_profile_partially_correct_local_4B_watch_needed", "price_source": "Songdaiki/stock-web", "notes": "C24 can keep Stage2 when data/regulatory event converts into filing clarity, partner milestone, reimbursement/launch path and revenue/margin bridge."}
{"row_type": "trigger", "trigger_id": "R7L86-C24-01-S2A-20240318", "case_id": "R7L86-C24-01", "symbol": "000250", "company_name": "삼천당제약", "round": "R7", "loop": 86, "large_sector_id": "L7_BIO_HEALTHCARE_MEDICAL", "canonical_archetype_id": "C24_BIO_TRIAL_DATA_EVENT_RISK", "fine_archetype_id": "ADC_BIOSIMILAR_CELL_THERAPY_TRIAL_DATA_LICENSE_MILESTONE_REIMBURSEMENT_BRIDGE_VS_EVENT_BLOWOFF_FADE", "loop_objective": "coverage_gap_fill|counterexample_mining|bio_trial_data_event_risk_guardrail|data_to_milestone_commercial_bridge|canonical_archetype_compression", "trigger_type": "Stage2-Actionable", "trigger_date": "2024-03-18", "evidence_available_at_that_date": "biosimilar/regulatory data and overseas license-commercialization proxy; primary filing, partner milestone, launch/reimbursement and margin evidence pending", "evidence_source": "source_proxy_only; evidence_url_pending", "stage2_evidence_fields": ["trial_data_or_regulatory_event_proxy", "partner_quality_proxy", "milestone_or_commercial_proxy"], "stage3_evidence_fields": ["data_durability", "regulatory_path", "partner_milestone", "reimbursement_or_launch_path", "revenue_margin_conversion"], "stage4b_evidence_fields": ["bio_event_MFE_without_commercial_bridge", "event_blowoff", "post_peak_drawdown"], "stage4c_evidence_fields": ["hard_trial_failure_or_regulatory_break_watch_only"], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/000/000250/2024.csv", "profile_path": "atlas/symbol_profiles/000/000250.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "entry_date": "2024-03-18", "entry_price": 86500, "MFE_30D_pct": 74.8, "MFE_90D_pct": 165.9, "MFE_180D_pct": 165.9, "MFE_1Y_pct": null, "MFE_2Y_pct": null, "MAE_30D_pct": -10.06, "MAE_90D_pct": -10.06, "MAE_180D_pct": -10.06, "MAE_1Y_pct": null, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2024-07-10", "peak_price": 230000, "drawdown_after_peak_pct": -44.17, "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": 0.82, "four_b_full_window_peak_proximity": 0.72, "four_b_timing_verdict": "local_4B_watch_after_biosimilar_event_MFE_if_regulatory_license_reimbursement_margin_bridge_stalls", "four_b_evidence_type": ["bio_event_MFE_without_commercial_bridge", "post_peak_drawdown", "source_proxy_gap"], "four_c_protection_label": "hard_4C_requires_non_price_trial_failure_or_regulatory_break", "trigger_outcome_label": "large_positive_MFE_but_trial_regulatory_license_bridge_required", "current_profile_verdict": "current_profile_partially_correct_local_4B_watch_needed", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_2024_window_after_old_2002_CA_candidate", "same_entry_group_id": "R7L86-C24-01", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R7L86-C24-01", "trigger_id": "R7L86-C24-01-S2A-20240318", "symbol": "000250", "large_sector_id": "L7_BIO_HEALTHCARE_MEDICAL", "canonical_archetype_id": "C24_BIO_TRIAL_DATA_EVENT_RISK", "raw_component_scores_before": {"data_quality_score": 50, "regulatory_path_score": 45, "partner_quality_score": 45, "milestone_visibility_score": 40, "commercialization_bridge_score": 35, "revenue_bridge_score": 35, "cash_runway_or_financing_score": 40, "relative_strength_score": 70, "event_blowoff_risk_score": 70, "execution_risk_score": 60, "source_quality_score": 20, "4B_watch_score": 45, "4C_watch_score": 25}, "weighted_score_before": 78, "stage_label_before": "Stage2-Actionable", "raw_component_scores_after": {"data_quality_score": 50, "regulatory_path_score": 45, "partner_quality_score": 45, "milestone_visibility_score": 40, "commercialization_bridge_score": 35, "revenue_bridge_score": 35, "cash_runway_or_financing_score": 40, "relative_strength_score": 70, "event_blowoff_risk_score": 80, "execution_risk_score": 70, "source_quality_score": 10, "4B_watch_score": 85, "4C_watch_score": 25}, "weighted_score_after": 73, "stage_label_after": "Stage2-Actionable + local 4B/data-commercial bridge watch", "changed_components": ["data_quality_score", "regulatory_path_score", "partner_quality_score", "milestone_visibility_score", "commercialization_bridge_score", "revenue_bridge_score", "source_quality_score", "4B_watch_score", "4C_watch_score"], "component_delta_explanation": "C24 requires trial/data/regulatory event MFE to convert into data durability, regulatory path, partner milestone, reimbursement/launch and revenue/margin bridge before clean Stage2/Green; event MFE alone is demoted or wrapped with local 4B/high-MAE watch.", "MFE_90D_pct": 165.9, "MAE_90D_pct": -10.06, "score_return_alignment_label": "large_positive_MFE_but_trial_regulatory_license_bridge_required", "current_profile_verdict": "current_profile_partially_correct_local_4B_watch_needed"}
{"row_type": "case", "case_id": "R7L86-C24-02", "symbol": "141080", "company_name": "리가켐바이오", "round": "R7", "loop": 86, "large_sector_id": "L7_BIO_HEALTHCARE_MEDICAL", "canonical_archetype_id": "C24_BIO_TRIAL_DATA_EVENT_RISK", "fine_archetype_id": "ADC_BIOSIMILAR_CELL_THERAPY_TRIAL_DATA_LICENSE_MILESTONE_REIMBURSEMENT_BRIDGE_VS_EVENT_BLOWOFF_FADE", "case_type": "ADC_platform_data_license_positive_with_local_4B_watch", "positive_or_counterexample": "positive", "best_trigger": "R7L86-C24-02-S2A-20240620", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "ADC_platform_MFE_positive_but_event_data_milestone_bridge_required", "current_profile_verdict": "current_profile_partially_correct_data_milestone_watch_needed", "price_source": "Songdaiki/stock-web", "notes": "C24 ADC-platform positives need data durability, target/payload differentiation, partner quality, milestone economics and commercialization bridge before clean Green."}
{"row_type": "trigger", "trigger_id": "R7L86-C24-02-S2A-20240620", "case_id": "R7L86-C24-02", "symbol": "141080", "company_name": "리가켐바이오", "round": "R7", "loop": 86, "large_sector_id": "L7_BIO_HEALTHCARE_MEDICAL", "canonical_archetype_id": "C24_BIO_TRIAL_DATA_EVENT_RISK", "fine_archetype_id": "ADC_BIOSIMILAR_CELL_THERAPY_TRIAL_DATA_LICENSE_MILESTONE_REIMBURSEMENT_BRIDGE_VS_EVENT_BLOWOFF_FADE", "loop_objective": "coverage_gap_fill|counterexample_mining|bio_trial_data_event_risk_guardrail|data_to_milestone_commercial_bridge|canonical_archetype_compression", "trigger_type": "Stage2-Actionable", "trigger_date": "2024-06-20", "evidence_available_at_that_date": "ADC platform/data event, global licensing optionality and partner quality proxy; primary data durability, milestone and commercial economics evidence pending", "evidence_source": "source_proxy_only; evidence_url_pending", "stage2_evidence_fields": ["trial_data_or_regulatory_event_proxy", "partner_quality_proxy", "milestone_or_commercial_proxy"], "stage3_evidence_fields": ["data_durability", "regulatory_path", "partner_milestone", "reimbursement_or_launch_path", "revenue_margin_conversion"], "stage4b_evidence_fields": ["bio_event_MFE_without_commercial_bridge", "event_blowoff", "post_peak_drawdown"], "stage4c_evidence_fields": ["hard_trial_failure_or_regulatory_break_watch_only"], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/141/141080/2024.csv", "profile_path": "atlas/symbol_profiles/141/141080.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "entry_date": "2024-06-20", "entry_price": 75500, "MFE_30D_pct": 15.5, "MFE_90D_pct": 39.07, "MFE_180D_pct": 74.17, "MFE_1Y_pct": null, "MFE_2Y_pct": null, "MAE_30D_pct": -10.33, "MAE_90D_pct": -11.39, "MAE_180D_pct": -11.39, "MAE_1Y_pct": null, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2024-10-21", "peak_price": 131500, "drawdown_after_peak_pct": -31.94, "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": 0.82, "four_b_full_window_peak_proximity": 0.72, "four_b_timing_verdict": "local_4B_watch_after_ADC_event_MFE_if_data_quality_milestone_commercial_bridge_stalls", "four_b_evidence_type": ["bio_event_MFE_without_commercial_bridge", "post_peak_drawdown", "source_proxy_gap"], "four_c_protection_label": "hard_4C_requires_non_price_trial_failure_or_regulatory_break", "trigger_outcome_label": "ADC_platform_MFE_positive_but_event_data_milestone_bridge_required", "current_profile_verdict": "current_profile_partially_correct_data_milestone_watch_needed", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_after_2024_04_23_CA_candidate", "same_entry_group_id": "R7L86-C24-02", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R7L86-C24-02", "trigger_id": "R7L86-C24-02-S2A-20240620", "symbol": "141080", "large_sector_id": "L7_BIO_HEALTHCARE_MEDICAL", "canonical_archetype_id": "C24_BIO_TRIAL_DATA_EVENT_RISK", "raw_component_scores_before": {"data_quality_score": 50, "regulatory_path_score": 45, "partner_quality_score": 45, "milestone_visibility_score": 40, "commercialization_bridge_score": 35, "revenue_bridge_score": 35, "cash_runway_or_financing_score": 40, "relative_strength_score": 70, "event_blowoff_risk_score": 70, "execution_risk_score": 60, "source_quality_score": 20, "4B_watch_score": 45, "4C_watch_score": 25}, "weighted_score_before": 78, "stage_label_before": "Stage2-Actionable", "raw_component_scores_after": {"data_quality_score": 50, "regulatory_path_score": 45, "partner_quality_score": 45, "milestone_visibility_score": 40, "commercialization_bridge_score": 35, "revenue_bridge_score": 35, "cash_runway_or_financing_score": 40, "relative_strength_score": 70, "event_blowoff_risk_score": 80, "execution_risk_score": 70, "source_quality_score": 10, "4B_watch_score": 85, "4C_watch_score": 25}, "weighted_score_after": 73, "stage_label_after": "Stage2-Actionable + local 4B/data-commercial bridge watch", "changed_components": ["data_quality_score", "regulatory_path_score", "partner_quality_score", "milestone_visibility_score", "commercialization_bridge_score", "revenue_bridge_score", "source_quality_score", "4B_watch_score", "4C_watch_score"], "component_delta_explanation": "C24 requires trial/data/regulatory event MFE to convert into data durability, regulatory path, partner milestone, reimbursement/launch and revenue/margin bridge before clean Stage2/Green; event MFE alone is demoted or wrapped with local 4B/high-MAE watch.", "MFE_90D_pct": 39.07, "MAE_90D_pct": -11.39, "score_return_alignment_label": "ADC_platform_MFE_positive_but_event_data_milestone_bridge_required", "current_profile_verdict": "current_profile_partially_correct_data_milestone_watch_needed"}
{"row_type": "case", "case_id": "R7L86-C24-03", "symbol": "174900", "company_name": "앱클론", "round": "R7", "loop": 86, "large_sector_id": "L7_BIO_HEALTHCARE_MEDICAL", "canonical_archetype_id": "C24_BIO_TRIAL_DATA_EVENT_RISK", "fine_archetype_id": "ADC_BIOSIMILAR_CELL_THERAPY_TRIAL_DATA_LICENSE_MILESTONE_REIMBURSEMENT_BRIDGE_VS_EVENT_BLOWOFF_FADE", "case_type": "cell_therapy_trial_data_event_blowoff_high_MAE_counterexample", "positive_or_counterexample": "counterexample", "best_trigger": "R7L86-C24-03-S2FP-20240305", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "trial_data_MFE_then_high_MAE_event_risk_false_positive", "current_profile_verdict": "current_profile_false_positive_high_MAE_event_blowoff", "price_source": "Songdaiki/stock-web", "notes": "Trial/data event spikes should remain RiskWatch unless pivotal data quality, regulatory path, partner milestone and commercial bridge are explicit at entry."}
{"row_type": "trigger", "trigger_id": "R7L86-C24-03-S2FP-20240305", "case_id": "R7L86-C24-03", "symbol": "174900", "company_name": "앱클론", "round": "R7", "loop": 86, "large_sector_id": "L7_BIO_HEALTHCARE_MEDICAL", "canonical_archetype_id": "C24_BIO_TRIAL_DATA_EVENT_RISK", "fine_archetype_id": "ADC_BIOSIMILAR_CELL_THERAPY_TRIAL_DATA_LICENSE_MILESTONE_REIMBURSEMENT_BRIDGE_VS_EVENT_BLOWOFF_FADE", "loop_objective": "coverage_gap_fill|counterexample_mining|bio_trial_data_event_risk_guardrail|data_to_milestone_commercial_bridge|canonical_archetype_compression", "trigger_type": "Stage2-FalsePositive", "trigger_date": "2024-03-05", "evidence_available_at_that_date": "cell-therapy / CAR-T trial data and pipeline event proxy without confirmed pivotal data, partner milestone, approval or revenue bridge", "evidence_source": "source_proxy_only; evidence_url_pending", "stage2_evidence_fields": ["trial_data_or_regulatory_event_proxy", "partner_quality_proxy", "milestone_or_commercial_proxy"], "stage3_evidence_fields": ["data_durability", "regulatory_path", "partner_milestone", "reimbursement_or_launch_path", "revenue_margin_conversion"], "stage4b_evidence_fields": ["bio_event_MFE_without_commercial_bridge", "event_blowoff", "post_peak_drawdown"], "stage4c_evidence_fields": ["hard_trial_failure_or_regulatory_break_watch_only"], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/174/174900/2024.csv", "profile_path": "atlas/symbol_profiles/174/174900.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "entry_date": "2024-03-05", "entry_price": 21100, "MFE_30D_pct": 4.98, "MFE_90D_pct": 4.98, "MFE_180D_pct": 4.98, "MFE_1Y_pct": null, "MFE_2Y_pct": null, "MAE_30D_pct": -24.08, "MAE_90D_pct": -31.52, "MAE_180D_pct": -48.67, "MAE_1Y_pct": null, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2024-03-05", "peak_price": 22150, "drawdown_after_peak_pct": -51.11, "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": 0.35, "four_b_full_window_peak_proximity": 0.3, "four_b_timing_verdict": "trial_data_event_MFE_rejected_without_pivotal_data_partner_regulatory_revenue_bridge", "four_b_evidence_type": ["bio_event_MFE_without_commercial_bridge", "post_peak_drawdown", "source_proxy_gap"], "four_c_protection_label": "hard_4C_requires_non_price_trial_failure_or_regulatory_break", "trigger_outcome_label": "trial_data_MFE_then_high_MAE_event_risk_false_positive", "current_profile_verdict": "current_profile_false_positive_high_MAE_event_blowoff", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_2024_window_after_old_2020_CA_candidates", "same_entry_group_id": "R7L86-C24-03", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R7L86-C24-03", "trigger_id": "R7L86-C24-03-S2FP-20240305", "symbol": "174900", "large_sector_id": "L7_BIO_HEALTHCARE_MEDICAL", "canonical_archetype_id": "C24_BIO_TRIAL_DATA_EVENT_RISK", "raw_component_scores_before": {"data_quality_score": 15, "regulatory_path_score": 10, "partner_quality_score": 5, "milestone_visibility_score": 5, "commercialization_bridge_score": 0, "revenue_bridge_score": 0, "cash_runway_or_financing_score": 25, "relative_strength_score": 35, "event_blowoff_risk_score": 85, "execution_risk_score": 85, "source_quality_score": 15, "4B_watch_score": 85, "4C_watch_score": 55}, "weighted_score_before": 58, "stage_label_before": "Stage2-Watch/FalsePositive", "raw_component_scores_after": {"data_quality_score": 0, "regulatory_path_score": 0, "partner_quality_score": 0, "milestone_visibility_score": 0, "commercialization_bridge_score": 0, "revenue_bridge_score": 0, "cash_runway_or_financing_score": 25, "relative_strength_score": 35, "event_blowoff_risk_score": 85, "execution_risk_score": 95, "source_quality_score": 5, "4B_watch_score": 95, "4C_watch_score": 75}, "weighted_score_after": 42, "stage_label_after": "Rejected-Stage2 / Bio-event RiskWatch", "changed_components": ["data_quality_score", "regulatory_path_score", "partner_quality_score", "milestone_visibility_score", "commercialization_bridge_score", "revenue_bridge_score", "source_quality_score", "4B_watch_score", "4C_watch_score"], "component_delta_explanation": "C24 requires trial/data/regulatory event MFE to convert into data durability, regulatory path, partner milestone, reimbursement/launch and revenue/margin bridge before clean Stage2/Green; event MFE alone is demoted or wrapped with local 4B/high-MAE watch.", "MFE_90D_pct": 4.98, "MAE_90D_pct": -31.52, "score_return_alignment_label": "trial_data_MFE_then_high_MAE_event_risk_false_positive", "current_profile_verdict": "current_profile_false_positive_high_MAE_event_blowoff"}
{"row_type": "shadow_weight", "axis": "C24_trial_data_regulatory_partner_milestone_commercial_bridge_required", "scope": "canonical_archetype_specific", "large_sector_id": "L7_BIO_HEALTHCARE_MEDICAL", "canonical_archetype_id": "C24_BIO_TRIAL_DATA_EVENT_RISK", "baseline_value": 0, "tested_value": 1, "delta": "+1", "reason": "Bio trial/data event rerating requires data durability, regulatory path, partner milestone, reimbursement/launch and revenue/margin conversion; event MFE without bridge fades into high MAE or event blowoff.", "backtest_effect": "keeps 000250/141080 with local 4B/data-commercial bridge watch; demotes 174900 high-MAE trial-data event false positive", "trigger_ids": "R7L86-C24-01-S2A-20240318|R7L86-C24-02-S2A-20240620|R7L86-C24-03-S2FP-20240305", "calibration_usable_count": 3, "new_independent_case_count": 3, "counterexample_count": 1, "confidence": "low", "proposal_type": "canonical_shadow_only", "notes": "source_proxy_only/evidence_url_pending; not production"}
{"row_type": "residual_contribution", "round": "R7", "loop": 86, "large_sector_id": "L7_BIO_HEALTHCARE_MEDICAL", "canonical_archetype_id": "C24_BIO_TRIAL_DATA_EVENT_RISK", "new_independent_case_count": 3, "reused_case_count": 0, "new_symbol_count": 3, "new_trigger_family_count": 3, "tested_existing_calibrated_axes": ["stage2_actionable_evidence_bonus", "price_only_blowoff_blocks_positive_stage", "full_4b_requires_non_price_evidence", "hard_4c_thesis_break_routes_to_4c", "source_proxy_only_blocks_runtime_promotion", "high_MAE_guardrail", "local_4B_watch_before_full_4B_when_MFE_outruns_bridge"], "residual_error_types_found": ["bio_trial_data_event_false_positive_high_MAE", "data_regulatory_partner_milestone_commercial_bridge_required", "local_4B_late_after_bio_event_MFE", "source_proxy_runtime_promotion_risk", "hard_4C_requires_non_price_trial_or_regulatory_break"], "loop_contribution_label": "canonical_archetype_rule_candidate", "do_not_propose_new_weight_delta": true}
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
- For C24, test a canonical-archetype guard requiring data durability, regulatory path, partner milestone, reimbursement/launch and revenue/gross-margin conversion before clean Stage2/Green. Keep hard 4C blocked unless a non-price trial/regulatory/commercial thesis break is confirmed.

## 27. Next Round State

```text
completed_round = R7
completed_loop = 86
next_round = R8
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
