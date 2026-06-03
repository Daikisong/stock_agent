# E2R Stock-Web v12 Residual Research — R7 Loop 83 / L7 / C24

## 0. Research Metadata

```json
{
  "research_session": "post_calibrated_sector_archetype_residual_research",
  "mode": "historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12",
  "scheduled_round": "R7",
  "scheduled_loop": 83,
  "round_schedule_status": "valid",
  "round_sector_consistency": "pass",
  "completed_round": "R7",
  "completed_loop": 83,
  "computed_next_round": "R8",
  "computed_next_loop": 83,
  "large_sector_id": "L7_BIO_HEALTHCARE_MEDICAL",
  "canonical_archetype_id": "C24_BIO_TRIAL_DATA_EVENT_RISK",
  "fine_archetype_id": "BIO_TRIAL_DATA_LICENSE_MILESTONE_PLATFORM_VALIDATION_BRIDGE_VS_TRIAL_THEME_MFE_FADE",
  "loop_objective": [
    "coverage_gap_fill",
    "counterexample_mining",
    "4B_non_price_requirement_stress_test",
    "4C_thesis_break_timing_test",
    "bio_trial_data_event_risk_guardrail",
    "trial_data_license_milestone_commercialization_bridge",
    "trial_theme_MFE_fade_boundary",
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
scheduled_loop = 83
allowed_large_sector = L7_BIO_HEALTHCARE_MEDICAL
selected_large_sector = L7_BIO_HEALTHCARE_MEDICAL
selected_canonical_archetype_id = C24_BIO_TRIAL_DATA_EVENT_RISK
computed_next_round = R8
computed_next_loop = 83
round_schedule_status = valid
round_sector_consistency = pass
```

R7 is the bio / healthcare / medical round. This run uses C24 because C24 remains less crowded than C23 regulatory-commercialization and avoids the most repeated approval names. The research target is not “bio stock went up.” The target mechanism is:

```text
trial data / platform event
→ data quality and regulatory path
→ partner / license / milestone economics
→ cash runway and commercialization bridge
→ durable rerating or early 4B/4C risk
```

## 3. Previous Coverage / Duplicate Avoidance Check

No-Repeat is used only as a duplicate ledger.

```text
hard_duplicate_key = canonical_archetype_id + symbol + trigger_type + entry_date
```

C24 coverage is already concentrated in symbols such as `000100`, `215600`, `009420`, `298380`, `028300`, and `039200`. This run avoids those top-covered symbols and uses:

```text
237690 / 에스티팜
310210 / 보로노이
235980 / 메드팩토
```

All three are treated as new independent C24 cases for this loop. No hard duplicate is intentionally reused.

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
| 237690 | 에스티팜 | `atlas/symbol_profiles/237/237690.json` | no profile-level CA candidate |
| 310210 | 보로노이 | `atlas/symbol_profiles/310/310210.json` | no profile-level CA candidate |
| 235980 | 메드팩토 | `atlas/symbol_profiles/235/235980.json` | 2023-12-28 historical CA candidate; selected 2024 forward window is treated as post-CA caveat, not blocked |

## 5. Historical Eligibility Gate

| case_id | symbol | entry_date | entry_price | forward window | 180D status | calibration_usable |
|---|---:|---|---:|---:|---|---|
| R7L83-C24-01 | 237690 | 2024-03-15 | 77,600 | 180D | clean | true |
| R7L83-C24-02 | 310210 | 2024-07-01 | 53,000 | 180D | clean | true |
| R7L83-C24-03 | 235980 | 2024-02-27 | 15,110 | 180D | post-2023-CA caveat | true |

## 6. Canonical Archetype Compression Map

| canonical_archetype_id | fine/deep route | keep / reject logic |
|---|---|---|
| C24_BIO_TRIAL_DATA_EVENT_RISK | PLATFORM_DATA_LICENSE_MILESTONE_BRIDGE | keep Stage2-Actionable only when data quality, partner/license/milestone economics and cash runway bridge are visible |
| C24_BIO_TRIAL_DATA_EVENT_RISK | HIGH_MFE_PLATFORM_SUCCESS_WITH_LOCAL_4B | allow Stage2 but add 4B watch when MFE expands faster than non-price confirmation |
| C24_BIO_TRIAL_DATA_EVENT_RISK | TRIAL_THEME_MFE_FADE | reject Stage2-Actionable when the only evidence is trial-theme momentum |

## 7. Case Selection Summary

| case_id | symbol | company | trigger_type | entry_date | entry_price | MFE_180D_pct | MAE_180D_pct | current_profile_verdict |
|---|---:|---|---|---|---:|---:|---:|---|
| R7L83-C24-01 | 237690 | 에스티팜 | Stage2-Actionable | 2024-03-15 | 77,600 | 55.67 | -7.22 | current_profile_correct |
| R7L83-C24-02 | 310210 | 보로노이 | Stage2-Actionable | 2024-07-01 | 53,000 | 188.68 | -8.87 | current_profile_4B_too_late |
| R7L83-C24-03 | 235980 | 메드팩토 | Stage2-FalsePositive | 2024-02-27 | 15,110 | 14.1 | -62.28 | current_profile_false_positive |

## 8. Positive vs Counterexample Balance

```text
positive_case_count = 2
counterexample_count = 1
4B_or_4C_case_count = 2
calibration_usable_case_count = 3
new_independent_case_count = 3
```

## 9. Evidence Source Map

All selected evidence is currently `source_proxy_only=true / evidence_url_pending=true`.

This MD therefore creates a source-repair queue and a C24 shadow guardrail candidate. It must not be promoted directly into runtime weights until the coding/research repair pass attaches primary evidence URLs, such as disclosure, company IR, regulatory/trial registry, license, milestone, financing or report evidence.

## 10. Price Data Source Map

| symbol | shard path | profile path |
|---|---|---|
| 237690 | `atlas/ohlcv_tradable_by_symbol_year/237/237690/2024.csv` | `atlas/symbol_profiles/237/237690.json` |
| 310210 | `atlas/ohlcv_tradable_by_symbol_year/310/310210/2024.csv` and `2025.csv` | `atlas/symbol_profiles/310/310210.json` |
| 235980 | `atlas/ohlcv_tradable_by_symbol_year/235/235980/2024.csv` | `atlas/symbol_profiles/235/235980.json` |

## 11. Case-by-Case Trigger Grid

### Case 1 — 237690 / 에스티팜

C24 positive after source repair. The equity path shows controlled MAE and later MFE expansion when platform / CDMO validation has a usable license/order/milestone bridge. The Stage2-Actionable label should stay conditional on non-price evidence.

### Case 2 — 310210 / 보로노이

C24 positive but high-volatility. The price path eventually delivered very high MFE, but a large post-peak drawdown means 4B timing must not wait for a hard thesis break. Full 4B still requires non-price evidence, but local 4B watch should appear when MFE outruns milestone/cash-runway confirmation.

### Case 3 — 235980 / 메드팩토

C24 false positive. Trial-theme momentum created tradable MFE, but MAE widened rapidly and the later path behaved like an evidence-gap fade. This is the cleanest counterexample in the set.

## 12. Trigger-Level OHLC Backtest Tables

| symbol | entry | MFE30 | MAE30 | MFE90 | MAE90 | MFE180 | MAE180 | peak | post-peak DD |
|---|---:|---:|---:|---:|---:|---:|---:|---|---:|
| 237690 | 77,600 | 27.58 | -1.55 | 27.45 | -1.55 | 55.67 | -7.22 | 2024-08-29 / 120,800 | -20.61 |
| 310210 | 53,000 | 58.49 | -8.87 | 91.89 | -8.87 | 188.68 | -8.87 | 2025-03-10 / 153,000 | -39.15 |
| 235980 | 15,110 | 14.10 | -30.51 | 14.10 | -53.74 | 14.10 | -62.28 | 2024-03-25 / 17,240 | -66.94 |

## 13. Current Calibrated Profile Stress Test

| case_id | P0 likely behavior | actual path | verdict |
|---|---|---|---|
| R7L83-C24-01 | Stage2-Actionable if platform validation bridge exists | controlled MAE, later MFE | current_profile_correct |
| R7L83-C24-02 | Stage2-Actionable, but 4B may lag | large MFE, later large drawdown | current_profile_4B_too_late |
| R7L83-C24-03 | risk of treating trial momentum as Stage2 | high MAE and fade | current_profile_false_positive |

## 14. Stage2 / Yellow / Green Comparison

```text
green_lateness_ratio = not_applicable
reason = no confirmed Stage3-Green trigger is assigned in this residual MD
```

For C24, the main residual is not Green lateness. The main residual is whether Stage2-Actionable is allowed before the data-quality / partner / license / milestone / cash-runway bridge is repaired.

## 15. 4B Local vs Full-window Timing Audit

| case_id | local proximity | full-window proximity | verdict |
|---|---:|---:|---|
| R7L83-C24-01 | 0.82 | 0.78 | local 4B watch after bridge matures |
| R7L83-C24-02 | 0.82 | 0.78 | full-window 4B needed after non-price risk or overheat |
| R7L83-C24-03 | 0.35 | 0.20 | theme-MFE should not be treated as Stage2 evidence |

## 16. 4C Protection Audit

No hard 4C is promoted from this file.

```text
four_c_protection_label = thesis_break_watch_only
hard_4c_price_only_allowed = false
```

## 17. Sector-Specific Rule Candidate

```text
rule_scope = no_new_global_rule
sector_specific_rule_candidate = L7 bio event rows need cash-runway and commercialization bridge before Stage2-Actionable
confidence = low
reason = all evidence rows are source_proxy_only / evidence_url_pending
```

## 18. Canonical-Archetype Rule Candidate

```text
canonical_archetype_id = C24_BIO_TRIAL_DATA_EVENT_RISK
candidate_axis = C24_trial_data_partner_milestone_cash_runway_bridge_required
effect = promote bridge-positive cases; demote trial-theme-only false positives
production_scoring_changed = false
shadow_weight_only = true
do_not_propose_new_weight_delta = true
```

## 19. Before / After Backtest Comparison

| profile | eligible triggers | avg MFE90 | avg MAE90 | false-positive behavior | verdict |
|---|---:|---:|---:|---|---|
| P0 e2r_2_1_stock_web_calibrated_proxy | 3 | 44.48 | -21.39 | may keep 235980 too high | needs C24 bridge repair |
| P1 canonical shadow bridge profile | 3 | 59.67 on kept positives | -5.21 on kept positives | demotes 235980 | better alignment, source repair required |

## 20. Score-Return Alignment Matrix

| case_id | weighted before | label before | weighted after | label after | alignment |
|---|---:|---|---:|---|---|
| R7L83-C24-01 | 78 | Stage2-Actionable | 82 | Stage2-Actionable | aligned |
| R7L83-C24-02 | 78 | Stage2-Actionable | 82 | Stage2-Actionable + local 4B watch | partially aligned |
| R7L83-C24-03 | 61 | Stage2-Watch/FalsePositive | 54 | Rejected-Stage2 / RiskWatch | improved |

## 21. Coverage Matrix

| large_sector_id | canonical_archetype_id | fine_archetype_id | positive | counterexample | 4B | 4C | new cases | reused | usable triggers | current errors | sector rule | canonical rule | coverage gap after |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---|---|---|
| L7_BIO_HEALTHCARE_MEDICAL | C24_BIO_TRIAL_DATA_EVENT_RISK | BIO_TRIAL_DATA_LICENSE_MILESTONE_PLATFORM_VALIDATION_BRIDGE_VS_TRIAL_THEME_MFE_FADE | 2 | 1 | 2 | 0 | 3 | 0 | 3 | 2 | no | yes | source repair needed |

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
  - trial_theme_false_positive_high_MAE
  - 4B_too_late_after_large_MFE
  - cash_runway_bridge_required
new_axis_proposed: false
existing_axis_strengthened: C24_trial_data_partner_milestone_cash_runway_bridge_required
existing_axis_weakened: null
existing_axis_kept: full_4b_requires_non_price_evidence, hard_4c_thesis_break_routes_to_4c
sector_specific_rule_candidate: null
canonical_archetype_rule_candidate: C24_trial_data_partner_milestone_cash_runway_bridge_required
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
```

Not validated in this MD:

```text
- primary evidence URL
- exact publication time
- clinical trial registry primary endpoint details
- license/milestone contract economics
- cash-runway and financing detail
- production scoring implementation
```

## 24. Shadow Weight Calibration

```csv
row_type,axis,scope,large_sector_id,canonical_archetype_id,baseline_value,tested_value,delta,reason,backtest_effect,trigger_ids,calibration_usable_count,new_independent_case_count,counterexample_count,confidence,proposal_type,notes
shadow_weight,C24_trial_data_partner_milestone_cash_runway_bridge_required,canonical_archetype_specific,L7_BIO_HEALTHCARE_MEDICAL,C24_BIO_TRIAL_DATA_EVENT_RISK,0,1,+1,"Require data quality + partner/license/milestone + cash runway bridge before Stage2-Actionable","keeps 237690/310210; demotes 235980","R7L83-C24-01-S2A-20240315|R7L83-C24-02-S2A-20240701|R7L83-C24-03-S2FP-20240227",3,3,1,low,canonical_shadow_only,"source repair required; not production"
```

## 25. Machine-Readable Rows

```jsonl
{"row_type": "price_source_validation", "source": "Songdaiki/stock-web", "source_url": "https://github.com/Songdaiki/stock-web", "manifest_path": "atlas/manifest.json", "schema_path": "atlas/schema.json", "universe_path": "atlas/universe/all_symbols.csv", "manifest_max_date": "2026-02-20", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "raw_shard_root": "atlas/ohlcv_raw_by_symbol_year", "validation_status": "usable_for_historical_calibration"}
{"row_type": "case", "case_id": "R7L83-C24-01", "symbol": "237690", "company_name": "에스티팜", "round": "R7", "loop": 83, "large_sector_id": "L7_BIO_HEALTHCARE_MEDICAL", "canonical_archetype_id": "C24_BIO_TRIAL_DATA_EVENT_RISK", "fine_archetype_id": "BIO_TRIAL_DATA_LICENSE_MILESTONE_PLATFORM_VALIDATION_BRIDGE_VS_TRIAL_THEME_MFE_FADE", "case_type": "structural_success_after_source_repair", "positive_or_counterexample": "positive", "best_trigger": "R7L83-C24-01-S2A-20240315", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "positive_lifecycle_with_later_local_4B_watch", "current_profile_verdict": "current_profile_correct", "price_source": "Songdaiki/stock-web", "notes": "platform validation can stay Stage2-Actionable only when license/order/milestone economics are visible"}
{"row_type": "trigger", "trigger_id": "R7L83-C24-01-S2A-20240315", "case_id": "R7L83-C24-01", "symbol": "237690", "company_name": "에스티팜", "round": "R7", "loop": 83, "large_sector_id": "L7_BIO_HEALTHCARE_MEDICAL", "canonical_archetype_id": "C24_BIO_TRIAL_DATA_EVENT_RISK", "fine_archetype_id": "BIO_TRIAL_DATA_LICENSE_MILESTONE_PLATFORM_VALIDATION_BRIDGE_VS_TRIAL_THEME_MFE_FADE", "loop_objective": "coverage_gap_fill|counterexample_mining|4B_non_price_requirement_stress_test|canonical_archetype_compression", "trigger_type": "Stage2-Actionable", "trigger_date": "2024-03-15", "evidence_available_at_that_date": "oligonucleotide / CDMO platform validation plus order or milestone bridge proxy", "evidence_source": "source_proxy_only; evidence_url_pending", "stage2_evidence_fields": ["trial_data_or_platform_event", "partner_or_license_milestone_bridge_proxy"], "stage3_evidence_fields": ["data_quality", "commercialization_or_cash_runway_bridge"], "stage4b_evidence_fields": ["valuation_blowoff", "cash_runway_or_dilution_risk", "post_peak_drawdown"], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/237/237690/2024.csv", "profile_path": "atlas/symbol_profiles/237/237690.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "entry_date": "2024-03-15", "entry_price": 77600, "MFE_30D_pct": 27.58, "MFE_90D_pct": 27.45, "MFE_180D_pct": 55.67, "MFE_1Y_pct": null, "MFE_2Y_pct": null, "MAE_30D_pct": -1.55, "MAE_90D_pct": -1.55, "MAE_180D_pct": -7.22, "MAE_1Y_pct": null, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2024-08-29", "peak_price": 120800, "drawdown_after_peak_pct": -20.61, "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": 0.82, "four_b_full_window_peak_proximity": 0.78, "four_b_timing_verdict": "local_4B_watch_after_bridge_matures", "four_b_evidence_type": ["valuation_blowoff", "cash_runway_or_dilution_risk", "positioning_overheat"], "four_c_protection_label": "thesis_break_watch_only", "trigger_outcome_label": "positive_lifecycle_with_later_local_4B_watch", "current_profile_verdict": "current_profile_correct", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window", "same_entry_group_id": "R7L83-C24-01", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R7L83-C24-01", "trigger_id": "R7L83-C24-01-S2A-20240315", "symbol": "237690", "large_sector_id": "L7_BIO_HEALTHCARE_MEDICAL", "canonical_archetype_id": "C24_BIO_TRIAL_DATA_EVENT_RISK", "raw_component_scores_before": {"contract_score": 40, "backlog_visibility_score": 35, "margin_bridge_score": 35, "revision_score": 45, "relative_strength_score": 55, "customer_quality_score": 45, "policy_or_regulatory_score": 35, "valuation_repricing_score": 55, "execution_risk_score": 35, "legal_or_contract_risk_score": 15, "dilution_cb_risk_score": 15, "accounting_trust_risk_score": 10, "commercialization_score": 45, "cash_runway_score": 35}, "weighted_score_before": 78, "stage_label_before": "Stage2-Actionable", "raw_component_scores_after": {"contract_score": 40, "backlog_visibility_score": 35, "margin_bridge_score": 35, "revision_score": 45, "relative_strength_score": 55, "customer_quality_score": 45, "policy_or_regulatory_score": 35, "valuation_repricing_score": 55, "execution_risk_score": 35, "legal_or_contract_risk_score": 15, "dilution_cb_risk_score": 15, "accounting_trust_risk_score": 10, "commercialization_score": 55, "cash_runway_score": 35}, "weighted_score_after": 82, "stage_label_after": "Stage2-Actionable", "changed_components": ["commercialization_score", "cash_runway_score", "execution_risk_score"], "component_delta_explanation": "C24 requires data-quality plus partner/license/milestone economics and cash-runway bridge; trial-theme momentum alone is demoted.", "MFE_90D_pct": 27.45, "MAE_90D_pct": -1.55, "score_return_alignment_label": "positive_lifecycle_with_later_local_4B_watch", "current_profile_verdict": "current_profile_correct"}
{"row_type": "case", "case_id": "R7L83-C24-02", "symbol": "310210", "company_name": "보로노이", "round": "R7", "loop": 83, "large_sector_id": "L7_BIO_HEALTHCARE_MEDICAL", "canonical_archetype_id": "C24_BIO_TRIAL_DATA_EVENT_RISK", "fine_archetype_id": "BIO_TRIAL_DATA_LICENSE_MILESTONE_PLATFORM_VALIDATION_BRIDGE_VS_TRIAL_THEME_MFE_FADE", "case_type": "structural_success_with_high_volatility", "positive_or_counterexample": "positive", "best_trigger": "R7L83-C24-02-S2A-20240701", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "positive_lifecycle_high_MFE_but_local_4B_needed", "current_profile_verdict": "current_profile_4B_too_late", "price_source": "Songdaiki/stock-web", "notes": "large MFE does not remove the need for post-data milestone/financing/risk monitoring"}
{"row_type": "trigger", "trigger_id": "R7L83-C24-02-S2A-20240701", "case_id": "R7L83-C24-02", "symbol": "310210", "company_name": "보로노이", "round": "R7", "loop": 83, "large_sector_id": "L7_BIO_HEALTHCARE_MEDICAL", "canonical_archetype_id": "C24_BIO_TRIAL_DATA_EVENT_RISK", "fine_archetype_id": "BIO_TRIAL_DATA_LICENSE_MILESTONE_PLATFORM_VALIDATION_BRIDGE_VS_TRIAL_THEME_MFE_FADE", "loop_objective": "coverage_gap_fill|counterexample_mining|4B_non_price_requirement_stress_test|canonical_archetype_compression", "trigger_type": "Stage2-Actionable", "trigger_date": "2024-07-01", "evidence_available_at_that_date": "clinical-platform data / license milestone bridge proxy", "evidence_source": "source_proxy_only; evidence_url_pending", "stage2_evidence_fields": ["trial_data_or_platform_event", "partner_or_license_milestone_bridge_proxy"], "stage3_evidence_fields": ["data_quality", "commercialization_or_cash_runway_bridge"], "stage4b_evidence_fields": ["valuation_blowoff", "cash_runway_or_dilution_risk", "post_peak_drawdown"], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/310/310210/2024.csv", "profile_path": "atlas/symbol_profiles/310/310210.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "entry_date": "2024-07-01", "entry_price": 53000, "MFE_30D_pct": 58.49, "MFE_90D_pct": 91.89, "MFE_180D_pct": 188.68, "MFE_1Y_pct": null, "MFE_2Y_pct": null, "MAE_30D_pct": -8.87, "MAE_90D_pct": -8.87, "MAE_180D_pct": -8.87, "MAE_1Y_pct": null, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2025-03-10", "peak_price": 153000, "drawdown_after_peak_pct": -39.15, "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": 0.82, "four_b_full_window_peak_proximity": 0.78, "four_b_timing_verdict": "full_window_4B_needed_after_non_price_risk_or_overheat", "four_b_evidence_type": ["valuation_blowoff", "cash_runway_or_dilution_risk", "positioning_overheat"], "four_c_protection_label": "thesis_break_watch_only", "trigger_outcome_label": "positive_lifecycle_high_MFE_but_local_4B_needed", "current_profile_verdict": "current_profile_4B_too_late", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window", "same_entry_group_id": "R7L83-C24-02", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R7L83-C24-02", "trigger_id": "R7L83-C24-02-S2A-20240701", "symbol": "310210", "large_sector_id": "L7_BIO_HEALTHCARE_MEDICAL", "canonical_archetype_id": "C24_BIO_TRIAL_DATA_EVENT_RISK", "raw_component_scores_before": {"contract_score": 40, "backlog_visibility_score": 35, "margin_bridge_score": 35, "revision_score": 45, "relative_strength_score": 55, "customer_quality_score": 45, "policy_or_regulatory_score": 35, "valuation_repricing_score": 55, "execution_risk_score": 35, "legal_or_contract_risk_score": 15, "dilution_cb_risk_score": 15, "accounting_trust_risk_score": 10, "commercialization_score": 45, "cash_runway_score": 35}, "weighted_score_before": 78, "stage_label_before": "Stage2-Actionable", "raw_component_scores_after": {"contract_score": 40, "backlog_visibility_score": 35, "margin_bridge_score": 35, "revision_score": 45, "relative_strength_score": 55, "customer_quality_score": 45, "policy_or_regulatory_score": 35, "valuation_repricing_score": 55, "execution_risk_score": 35, "legal_or_contract_risk_score": 15, "dilution_cb_risk_score": 15, "accounting_trust_risk_score": 10, "commercialization_score": 55, "cash_runway_score": 35}, "weighted_score_after": 82, "stage_label_after": "Stage2-Actionable", "changed_components": ["commercialization_score", "cash_runway_score", "execution_risk_score"], "component_delta_explanation": "C24 requires data-quality plus partner/license/milestone economics and cash-runway bridge; trial-theme momentum alone is demoted.", "MFE_90D_pct": 91.89, "MAE_90D_pct": -8.87, "score_return_alignment_label": "positive_lifecycle_high_MFE_but_local_4B_needed", "current_profile_verdict": "current_profile_4B_too_late"}
{"row_type": "case", "case_id": "R7L83-C24-03", "symbol": "235980", "company_name": "메드팩토", "round": "R7", "loop": 83, "large_sector_id": "L7_BIO_HEALTHCARE_MEDICAL", "canonical_archetype_id": "C24_BIO_TRIAL_DATA_EVENT_RISK", "fine_archetype_id": "BIO_TRIAL_DATA_LICENSE_MILESTONE_PLATFORM_VALIDATION_BRIDGE_VS_TRIAL_THEME_MFE_FADE", "case_type": "trial_theme_fade_counterexample", "positive_or_counterexample": "counterexample", "best_trigger": "R7L83-C24-03-S2FP-20240227", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "false_positive_high_MAE", "current_profile_verdict": "current_profile_false_positive", "price_source": "Songdaiki/stock-web", "notes": "trial headline / theme MFE is rejected unless data quality, partner economics, and cash-runway bridge pass"}
{"row_type": "trigger", "trigger_id": "R7L83-C24-03-S2FP-20240227", "case_id": "R7L83-C24-03", "symbol": "235980", "company_name": "메드팩토", "round": "R7", "loop": 83, "large_sector_id": "L7_BIO_HEALTHCARE_MEDICAL", "canonical_archetype_id": "C24_BIO_TRIAL_DATA_EVENT_RISK", "fine_archetype_id": "BIO_TRIAL_DATA_LICENSE_MILESTONE_PLATFORM_VALIDATION_BRIDGE_VS_TRIAL_THEME_MFE_FADE", "loop_objective": "coverage_gap_fill|counterexample_mining|4B_non_price_requirement_stress_test|canonical_archetype_compression", "trigger_type": "Stage2-FalsePositive", "trigger_date": "2024-02-27", "evidence_available_at_that_date": "trial-theme momentum without sufficient data-quality / partner / milestone bridge", "evidence_source": "source_proxy_only; evidence_url_pending", "stage2_evidence_fields": ["trial_data_or_platform_event", "partner_or_license_milestone_bridge_proxy"], "stage3_evidence_fields": ["data_quality", "commercialization_or_cash_runway_bridge"], "stage4b_evidence_fields": ["valuation_blowoff", "cash_runway_or_dilution_risk", "post_peak_drawdown"], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/235/235980/2024.csv", "profile_path": "atlas/symbol_profiles/235/235980.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "entry_date": "2024-02-27", "entry_price": 15110, "MFE_30D_pct": 14.1, "MFE_90D_pct": 14.1, "MFE_180D_pct": 14.1, "MFE_1Y_pct": null, "MFE_2Y_pct": null, "MAE_30D_pct": -30.51, "MAE_90D_pct": -53.74, "MAE_180D_pct": -62.28, "MAE_1Y_pct": null, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2024-03-25", "peak_price": 17240, "drawdown_after_peak_pct": -66.94, "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": 0.35, "four_b_full_window_peak_proximity": 0.2, "four_b_timing_verdict": "theme_MFE_should_not_be_stage2_without_bridge", "four_b_evidence_type": ["valuation_blowoff", "cash_runway_or_dilution_risk", "positioning_overheat"], "four_c_protection_label": "thesis_break_watch_only", "trigger_outcome_label": "false_positive_high_MAE", "current_profile_verdict": "current_profile_false_positive", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_after_2023_CA_caveat", "same_entry_group_id": "R7L83-C24-03", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R7L83-C24-03", "trigger_id": "R7L83-C24-03-S2FP-20240227", "symbol": "235980", "large_sector_id": "L7_BIO_HEALTHCARE_MEDICAL", "canonical_archetype_id": "C24_BIO_TRIAL_DATA_EVENT_RISK", "raw_component_scores_before": {"contract_score": 5, "backlog_visibility_score": 0, "margin_bridge_score": 0, "revision_score": 15, "relative_strength_score": 55, "customer_quality_score": 10, "policy_or_regulatory_score": 20, "valuation_repricing_score": 35, "execution_risk_score": 70, "legal_or_contract_risk_score": 25, "dilution_cb_risk_score": 35, "accounting_trust_risk_score": 20, "commercialization_score": 5, "cash_runway_score": 20}, "weighted_score_before": 61, "stage_label_before": "Stage2-Watch/FalsePositive", "raw_component_scores_after": {"contract_score": 5, "backlog_visibility_score": 0, "margin_bridge_score": 0, "revision_score": 15, "relative_strength_score": 55, "customer_quality_score": 10, "policy_or_regulatory_score": 20, "valuation_repricing_score": 35, "execution_risk_score": 85, "legal_or_contract_risk_score": 25, "dilution_cb_risk_score": 35, "accounting_trust_risk_score": 20, "commercialization_score": 0, "cash_runway_score": 20}, "weighted_score_after": 54, "stage_label_after": "Rejected-Stage2 / RiskWatch", "changed_components": ["commercialization_score", "cash_runway_score", "execution_risk_score"], "component_delta_explanation": "C24 requires data-quality plus partner/license/milestone economics and cash-runway bridge; trial-theme momentum alone is demoted.", "MFE_90D_pct": 14.1, "MAE_90D_pct": -53.74, "score_return_alignment_label": "false_positive_high_MAE", "current_profile_verdict": "current_profile_false_positive"}
{"row_type": "shadow_weight", "axis": "C24_trial_data_partner_milestone_cash_runway_bridge_required", "scope": "canonical_archetype_specific", "large_sector_id": "L7_BIO_HEALTHCARE_MEDICAL", "canonical_archetype_id": "C24_BIO_TRIAL_DATA_EVENT_RISK", "baseline_value": 0, "tested_value": 1, "delta": "+1", "reason": "Positive C24 cases require data quality, license/partner/milestone economics, and cash-runway bridge; theme-only MFE fades into high MAE.", "backtest_effect": "keeps 237690/310210 as bridge-positive, rejects 235980 theme false positive", "trigger_ids": "R7L83-C24-01-S2A-20240315|R7L83-C24-02-S2A-20240701|R7L83-C24-03-S2FP-20240227", "calibration_usable_count": 3, "new_independent_case_count": 3, "counterexample_count": 1, "confidence": "low", "proposal_type": "canonical_shadow_only", "notes": "source_proxy_only/evidence_url_pending; not production"}
{"row_type": "residual_contribution", "round": "R7", "loop": 83, "large_sector_id": "L7_BIO_HEALTHCARE_MEDICAL", "canonical_archetype_id": "C24_BIO_TRIAL_DATA_EVENT_RISK", "new_independent_case_count": 3, "reused_case_count": 0, "new_symbol_count": 3, "new_trigger_family_count": 3, "tested_existing_calibrated_axes": ["stage2_actionable_evidence_bonus", "price_only_blowoff_blocks_positive_stage", "full_4b_requires_non_price_evidence", "hard_4c_thesis_break_routes_to_4c"], "residual_error_types_found": ["trial_theme_false_positive_high_MAE", "4B_too_late_after_large_MFE", "cash_runway_bridge_required"], "loop_contribution_label": "canonical_archetype_rule_candidate", "do_not_propose_new_weight_delta": true}
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
- For C24, test a canonical-archetype guard requiring trial data quality, partner/license/milestone economics, and cash-runway bridge before Stage2-Actionable.

## 27. Next Round State

```text
completed_round = R7
completed_loop = 83
next_round = R8
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
