# E2R Stock-Web v12 Residual Research — R8 Loop 84 / L8 / C28

## 0. Research Metadata

```json
{
  "research_session": "post_calibrated_sector_archetype_residual_research",
  "mode": "historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12",
  "scheduled_round": "R8",
  "scheduled_loop": 84,
  "round_schedule_status": "valid",
  "round_sector_consistency": "pass",
  "completed_round": "R8",
  "completed_loop": 84,
  "computed_next_round": "R9",
  "computed_next_loop": 84,
  "large_sector_id": "L8_PLATFORM_CONTENT_SW_SECURITY",
  "canonical_archetype_id": "C28_SOFTWARE_SECURITY_CONTRACT_RETENTION",
  "fine_archetype_id": "ERP_SECURITY_CONTACTCENTER_CONTRACT_RETENTION_ARR_RENEWAL_MARGIN_BRIDGE_VS_AI_SOFTWARE_THEME_FADE",
  "loop_objective": [
    "coverage_gap_fill",
    "counterexample_mining",
    "software_security_contract_retention_guardrail",
    "ARR_renewal_churn_margin_bridge_test",
    "local_4B_timing_after_software_MFE",
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
scheduled_round = R8
scheduled_loop = 84
allowed_large_sector = L8_PLATFORM_CONTENT_SW_SECURITY
selected_large_sector = L8_PLATFORM_CONTENT_SW_SECURITY
selected_canonical_archetype_id = C28_SOFTWARE_SECURITY_CONTRACT_RETENTION
computed_next_round = R9
computed_next_loop = 84
round_schedule_status = valid
round_sector_consistency = pass
```

R8 is the platform / content / software / security round. This run selects C28 because loop83 already tested C27, and this route isolates software-security contract economics rather than content/IP monetization.

The tested mechanism:

```text
software / security / ERP / contact-center theme
→ recurring contract base
→ renewal quality and churn control
→ implementation backlog or maintenance revenue
→ gross/OP margin conversion
→ durable rerating or local 4B / false-positive fade
```

C28 is not “software theme.” It is the renewal flywheel: software only compounds when the customer stays, expands, and the retained revenue carries margin.

## 3. Previous Coverage / Duplicate Avoidance Check

No-Repeat is used only as a duplicate ledger.

```text
hard_duplicate_key = canonical_archetype_id + symbol + trigger_type + entry_date
```

C28 top-covered symbols include `012510`, `053800`, `263860`, `030520`, `131370`, and `136540`. This run avoids that top-covered set and uses:

```text
060850 / 영림원소프트랩
064480 / 브리지텍
053350 / 이니텍
```

All three are treated as new independent C28 software-security contract retention cases for this loop. No hard duplicate is intentionally reused.

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
| 060850 | 영림원소프트랩 | `atlas/symbol_profiles/060/060850.json` | no profile-level CA candidate |
| 064480 | 브리지텍 | `atlas/symbol_profiles/064/064480.json` | old 2013 CA candidate; selected 2024 forward window clean |
| 053350 | 이니텍 | `atlas/symbol_profiles/053/053350.json` | old 2011 CA candidate; selected 2024 forward window clean |

## 5. Historical Eligibility Gate

| case_id | symbol | entry_date | entry_price | forward window | 180D status | calibration_usable |
|---|---:|---|---:|---:|---|---|
| R8L84-C28-01 | 060850 | 2024-04-01 | 8,850 | 180D | clean | true |
| R8L84-C28-02 | 064480 | 2024-01-23 | 9,980 | 180D | clean | true |
| R8L84-C28-03 | 053350 | 2024-04-01 | 3,535 | 180D | clean | true |

## 6. Canonical Archetype Compression Map

| canonical_archetype_id | fine/deep route | keep / reject logic |
|---|---|---|
| C28_SOFTWARE_SECURITY_CONTRACT_RETENTION | ERP_SAAS_RENEWAL_ARR_MARGIN_BRIDGE | keep Stage2 only with recurring base, renewal quality, implementation backlog and margin conversion |
| C28_SOFTWARE_SECURITY_CONTRACT_RETENTION | CONTACTCENTER_AI_THEME_FADE | reject when AI/contact-center theme lacks contract retention and customer expansion evidence |
| C28_SOFTWARE_SECURITY_CONTRACT_RETENTION | SECURITY_AUTH_MAINTENANCE_CONTRACT_FADE | reject low-quality MFE without churn/renewal/margin bridge |

## 7. Case Selection Summary

| case_id | symbol | company | trigger_type | entry_date | entry_price | MFE_180D_pct | MAE_180D_pct | current_profile_verdict |
|---|---:|---|---|---|---:|---:|---:|---|
| R8L84-C28-01 | 060850 | 영림원소프트랩 | Stage2-Actionable | 2024-04-01 | 8,850 | 27.34 | -21.81 | current_profile_partially_correct_high_MAE_watch_needed |
| R8L84-C28-02 | 064480 | 브리지텍 | Stage2-FalsePositive | 2024-01-23 | 9,980 | 11.92 | -31.16 | current_profile_false_positive_high_MAE |
| R8L84-C28-03 | 053350 | 이니텍 | Stage2-FalsePositive | 2024-04-01 | 3,535 | 13.72 | -16.27 | current_profile_false_positive_low_quality_MFE |

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

This MD therefore creates a source-repair queue and a C28 shadow guardrail candidate. It must not be promoted directly into runtime weights until a later source-repair pass attaches primary evidence URLs: ARR/maintenance revenue, renewal rate, churn, implementation backlog, security-contract renewal, customer expansion, gross/OP margin bridge, company disclosure or report evidence.

## 10. Price Data Source Map

| symbol | shard path | profile path |
|---|---|---|
| 060850 | `atlas/ohlcv_tradable_by_symbol_year/060/060850/2024.csv` | `atlas/symbol_profiles/060/060850.json` |
| 064480 | `atlas/ohlcv_tradable_by_symbol_year/064/064480/2024.csv` | `atlas/symbol_profiles/064/064480.json` |
| 053350 | `atlas/ohlcv_tradable_by_symbol_year/053/053350/2024.csv` | `atlas/symbol_profiles/053/053350.json` |

## 11. Case-by-Case Trigger Grid

### Case 1 — 060850 / 영림원소프트랩

C28 ERP/SaaS bounded positive with high-MAE watch. The price path produced an MFE spike, but the later drawdown says the model should not mark this clean Green unless ARR/maintenance quality, renewal rate and margin conversion are source-repaired.

### Case 2 — 064480 / 브리지텍

C28 contact-center / AI software false positive. The price path had a short MFE and then a deep MAE. This is the archetypal AI software theme case: tradable heat, weak contract-retention proof.

### Case 3 — 053350 / 이니텍

C28 security/authentication maintenance fade. It eventually had a later MFE, but the original entry window did not show a clean contract-retention bridge. The model should not validate the initial Stage2 trigger from delayed low-quality MFE.

## 12. Trigger-Level OHLC Backtest Tables

| symbol | entry | MFE30 | MAE30 | MFE90 | MAE90 | MFE180 | MAE180 | peak | post-peak DD |
|---|---:|---:|---:|---:|---:|---:|---:|---|---:|
| 060850 | 8,850 | 27.34 | -2.71 | 27.34 | -5.65 | 27.34 | -21.81 | 2024-04-05 / 11,270 | -38.60 |
| 064480 | 9,980 | 11.92 | -25.65 | 11.92 | -31.16 | 11.92 | -31.16 | 2024-01-25 / 11,170 | -38.23 |
| 053350 | 3,535 | 1.27 | -9.48 | 4.81 | -16.27 | 13.72 | -16.27 | 2024-08-02 / 4,020 | -24.88 |

## 13. Current Calibrated Profile Stress Test

| case_id | P0 likely behavior | actual path | verdict |
|---|---|---|---|
| R8L84-C28-01 | Stage2-Actionable if ARR/renewal bridge exists | bounded MFE, later high MAE | partially correct; high-MAE/local 4B watch needed |
| R8L84-C28-02 | risk of treating AI software heat as Stage2 | short MFE / high MAE | false positive |
| R8L84-C28-03 | risk of treating security contract theme as Stage2 | low-quality MFE / MAE | false positive |

## 14. Stage2 / Yellow / Green Comparison

```text
green_lateness_ratio = not_applicable
reason = no confirmed Stage3-Green trigger is assigned in this residual MD
```

For C28, the residual is not Green lateness. The residual is whether software/security theme MFE becomes clean Stage2/Green before recurring contract base, renewal quality, churn control and margin conversion are proven.

## 15. 4B Local vs Full-window Timing Audit

| case_id | local proximity | full-window proximity | verdict |
|---|---:|---:|---|
| R8L84-C28-01 | 0.75 | 0.65 | local 4B watch after SaaS MFE if ARR/renewal bridge stalls |
| R8L84-C28-02 | 0.30 | 0.25 | AI software theme MFE rejected without contract retention bridge |
| R8L84-C28-03 | 0.30 | 0.25 | security contract theme rejected without retention/churn bridge |

## 16. 4C Protection Audit

No hard 4C is promoted from this file.

```text
four_c_protection_label = hard_4C_requires_non_price_churn_or_contract_loss
hard_4c_price_only_allowed = false
```

## 17. Sector-Specific Rule Candidate

```text
rule_scope = no_new_global_rule
sector_specific_rule_candidate = L8 software/security rows need recurring contract base, renewal quality, churn control and margin conversion before clean Stage2/Green
confidence = low
reason = all evidence rows are source_proxy_only / evidence_url_pending
```

## 18. Canonical-Archetype Rule Candidate

```text
canonical_archetype_id = C28_SOFTWARE_SECURITY_CONTRACT_RETENTION
candidate_axis = C28_contract_retention_ARR_renewal_churn_margin_bridge_required
effect = keep software positives only with high-MAE/local 4B watch; demote AI/security theme false positives
production_scoring_changed = false
shadow_weight_only = true
do_not_propose_new_weight_delta = true
```

## 19. Before / After Backtest Comparison

| profile | eligible triggers | avg MFE90 | avg MAE90 | false-positive behavior | verdict |
|---|---:|---:|---:|---|---|
| P0 e2r_2_1_stock_web_calibrated_proxy | 3 | 14.69 | -17.69 | may over-credit AI/software/security theme MFE | needs C28 bridge repair |
| P1 canonical shadow bridge profile | 3 | 27.34 on kept positive | -5.65 on kept positive but high-MAE watch | demotes 064480/053350 | better alignment, source repair required |

## 20. Score-Return Alignment Matrix

| case_id | weighted before | label before | weighted after | label after | alignment |
|---|---:|---|---:|---|---|
| R8L84-C28-01 | 74 | Stage2-Actionable | 71 | Stage2-Actionable + high-MAE/local 4B watch | partially aligned |
| R8L84-C28-02 | 58 | Stage2-Watch/FalsePositive | 46 | Rejected-Stage2 / RiskWatch | improved |
| R8L84-C28-03 | 58 | Stage2-Watch/FalsePositive | 46 | Rejected-Stage2 / RiskWatch | improved |

## 21. Coverage Matrix

| large_sector_id | canonical_archetype_id | fine_archetype_id | positive | counterexample | 4B | 4C | new cases | reused | usable triggers | current errors | sector rule | canonical rule | coverage gap after |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---|---|---|
| L8_PLATFORM_CONTENT_SW_SECURITY | C28_SOFTWARE_SECURITY_CONTRACT_RETENTION | ERP_SECURITY_CONTACTCENTER_CONTRACT_RETENTION_ARR_RENEWAL_MARGIN_BRIDGE_VS_AI_SOFTWARE_THEME_FADE | 1 | 2 | 3-watch | 0 | 3 | 0 | 3 | 2 | no | yes | source repair needed |

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
  - software_security_theme_false_positive_high_MAE
  - contract_retention_ARR_renewal_churn_margin_bridge_required
  - local_4B_late_after_software_MFE
  - source_proxy_runtime_promotion_risk
  - high_MAE_positive_Green_blocker
new_axis_proposed: false
existing_axis_strengthened:
  - C28_contract_retention_ARR_renewal_churn_margin_bridge_required
  - source_proxy_only_blocks_runtime_promotion
  - local_4B_watch_before_full_4B_when_MFE_outruns_bridge
  - high_MAE_blocks_clean_Green
existing_axis_weakened: null
existing_axis_kept:
  - full_4b_requires_non_price_evidence
  - hard_4c_thesis_break_routes_to_4c
sector_specific_rule_candidate: null
canonical_archetype_rule_candidate: C28_contract_retention_ARR_renewal_churn_margin_bridge_required
no_new_signal_reason: null
loop_contribution_label: canonical_archetype_rule_candidate
do_not_propose_new_weight_delta: true
```

This loop adds 3 new independent cases, 2 counterexamples, and 2 residual errors for R8/L8_PLATFORM_CONTENT_SW_SECURITY/C28_SOFTWARE_SECURITY_CONTRACT_RETENTION.

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
- ARR or maintenance-revenue source
- renewal rate / churn / contract duration
- implementation backlog
- gross/OP margin conversion
- production scoring implementation
```

## 24. Shadow Weight Calibration

```csv
row_type,axis,scope,large_sector_id,canonical_archetype_id,baseline_value,tested_value,delta,reason,backtest_effect,trigger_ids,calibration_usable_count,new_independent_case_count,counterexample_count,confidence,proposal_type,notes
shadow_weight,C28_contract_retention_ARR_renewal_churn_margin_bridge_required,canonical_archetype_specific,L8_PLATFORM_CONTENT_SW_SECURITY,C28_SOFTWARE_SECURITY_CONTRACT_RETENTION,0,1,+1,"Require recurring contract base, ARR or maintenance revenue, renewal quality, churn control, implementation backlog and margin conversion before clean Stage2/Green","keeps 060850 with high-MAE/local 4B watch; demotes 064480/053350","R8L84-C28-01-S2A-20240401|R8L84-C28-02-S2FP-20240123|R8L84-C28-03-S2FP-20240401",3,3,2,low,canonical_shadow_only,"source repair required; not production"
```

## 25. Machine-Readable Rows

```jsonl
{"row_type": "price_source_validation", "source": "Songdaiki/stock-web", "source_url": "https://github.com/Songdaiki/stock-web", "manifest_path": "atlas/manifest.json", "schema_path": "atlas/schema.json", "universe_path": "atlas/universe/all_symbols.csv", "manifest_max_date": "2026-02-20", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "raw_shard_root": "atlas/ohlcv_raw_by_symbol_year", "validation_status": "usable_for_historical_calibration"}
{"row_type": "case", "case_id": "R8L84-C28-01", "symbol": "060850", "company_name": "영림원소프트랩", "round": "R8", "loop": 84, "large_sector_id": "L8_PLATFORM_CONTENT_SW_SECURITY", "canonical_archetype_id": "C28_SOFTWARE_SECURITY_CONTRACT_RETENTION", "fine_archetype_id": "ERP_SECURITY_CONTACTCENTER_CONTRACT_RETENTION_ARR_RENEWAL_MARGIN_BRIDGE_VS_AI_SOFTWARE_THEME_FADE", "case_type": "ERP_SaaS_contract_retention_positive_but_high_MAE_watch", "positive_or_counterexample": "positive", "best_trigger": "R8L84-C28-01-S2A-20240401", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "bounded_positive_MFE_but_high_MAE_RiskWatch", "current_profile_verdict": "current_profile_partially_correct_high_MAE_watch_needed", "price_source": "Songdaiki/stock-web", "notes": "C28 can keep Stage2 only when contract renewal, ARR/maintenance, implementation backlog, churn control and operating-margin bridge are visible."}
{"row_type": "trigger", "trigger_id": "R8L84-C28-01-S2A-20240401", "case_id": "R8L84-C28-01", "symbol": "060850", "company_name": "영림원소프트랩", "round": "R8", "loop": 84, "large_sector_id": "L8_PLATFORM_CONTENT_SW_SECURITY", "canonical_archetype_id": "C28_SOFTWARE_SECURITY_CONTRACT_RETENTION", "fine_archetype_id": "ERP_SECURITY_CONTACTCENTER_CONTRACT_RETENTION_ARR_RENEWAL_MARGIN_BRIDGE_VS_AI_SOFTWARE_THEME_FADE", "loop_objective": "coverage_gap_fill|counterexample_mining|software_security_contract_retention_guardrail|local_4B_timing_after_software_MFE|canonical_archetype_compression", "trigger_type": "Stage2-Actionable", "trigger_date": "2024-04-01", "evidence_available_at_that_date": "ERP/SaaS contract retention, renewal and enterprise implementation backlog proxy; primary ARR/churn evidence pending", "evidence_source": "source_proxy_only; evidence_url_pending", "stage2_evidence_fields": ["contract_retention_proxy", "ARR_or_maintenance_proxy", "enterprise_customer_proxy"], "stage3_evidence_fields": ["confirmed_ARR_or_recurring_base", "renewal_rate", "churn_control", "implementation_backlog", "gross_or_OP_margin_conversion"], "stage4b_evidence_fields": ["software_MFE_without_retention_bridge", "valuation_overheat", "post_peak_drawdown"], "stage4c_evidence_fields": ["hard_churn_or_contract_loss_watch_only"], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/060/060850/2024.csv", "profile_path": "atlas/symbol_profiles/060/060850.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "entry_date": "2024-04-01", "entry_price": 8850, "MFE_30D_pct": 27.34, "MFE_90D_pct": 27.34, "MFE_180D_pct": 27.34, "MFE_1Y_pct": null, "MFE_2Y_pct": null, "MAE_30D_pct": -2.71, "MAE_90D_pct": -5.65, "MAE_180D_pct": -21.81, "MAE_1Y_pct": null, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2024-04-05", "peak_price": 11270, "drawdown_after_peak_pct": -38.6, "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": 0.75, "four_b_full_window_peak_proximity": 0.65, "four_b_timing_verdict": "local_4B_watch_after_SaaS_MFE_if_ARR_renewal_margin_bridge_stalls", "four_b_evidence_type": ["software_MFE_without_retention_bridge", "post_peak_drawdown", "source_proxy_gap"], "four_c_protection_label": "hard_4C_requires_non_price_churn_or_contract_loss", "trigger_outcome_label": "bounded_positive_MFE_but_high_MAE_RiskWatch", "current_profile_verdict": "current_profile_partially_correct_high_MAE_watch_needed", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window_no_profile_CA_candidate", "same_entry_group_id": "R8L84-C28-01", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R8L84-C28-01", "trigger_id": "R8L84-C28-01-S2A-20240401", "symbol": "060850", "large_sector_id": "L8_PLATFORM_CONTENT_SW_SECURITY", "canonical_archetype_id": "C28_SOFTWARE_SECURITY_CONTRACT_RETENTION", "raw_component_scores_before": {"contract_retention_score": 45, "ARR_or_maintenance_score": 40, "renewal_visibility_score": 40, "implementation_backlog_score": 35, "customer_quality_score": 35, "gross_margin_bridge_score": 35, "operating_leverage_score": 35, "revision_score": 35, "relative_strength_score": 55, "valuation_blowoff_risk_score": 60, "execution_risk_score": 55, "source_quality_score": 20, "4B_watch_score": 45}, "weighted_score_before": 74, "stage_label_before": "Stage2-Actionable", "raw_component_scores_after": {"contract_retention_score": 45, "ARR_or_maintenance_score": 40, "renewal_visibility_score": 40, "implementation_backlog_score": 35, "customer_quality_score": 35, "gross_margin_bridge_score": 35, "operating_leverage_score": 35, "revision_score": 35, "relative_strength_score": 55, "valuation_blowoff_risk_score": 60, "execution_risk_score": 70, "source_quality_score": 10, "4B_watch_score": 80}, "weighted_score_after": 71, "stage_label_after": "Stage2-Actionable + high-MAE/local 4B watch", "changed_components": ["ARR_or_maintenance_score", "renewal_visibility_score", "gross_margin_bridge_score", "operating_leverage_score", "source_quality_score", "execution_risk_score", "4B_watch_score"], "component_delta_explanation": "C28 requires recurring contract base, renewal quality, churn control, implementation backlog and margin conversion before clean Stage2/Green; AI/software/security theme MFE alone is demoted or wrapped with local 4B/high-MAE watch.", "MFE_90D_pct": 27.34, "MAE_90D_pct": -5.65, "score_return_alignment_label": "bounded_positive_MFE_but_high_MAE_RiskWatch", "current_profile_verdict": "current_profile_partially_correct_high_MAE_watch_needed"}
{"row_type": "case", "case_id": "R8L84-C28-02", "symbol": "064480", "company_name": "브리지텍", "round": "R8", "loop": 84, "large_sector_id": "L8_PLATFORM_CONTENT_SW_SECURITY", "canonical_archetype_id": "C28_SOFTWARE_SECURITY_CONTRACT_RETENTION", "fine_archetype_id": "ERP_SECURITY_CONTACTCENTER_CONTRACT_RETENTION_ARR_RENEWAL_MARGIN_BRIDGE_VS_AI_SOFTWARE_THEME_FADE", "case_type": "contact_center_AI_software_theme_false_positive", "positive_or_counterexample": "counterexample", "best_trigger": "R8L84-C28-02-S2FP-20240123", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "short_MFE_high_MAE_software_theme_false_positive", "current_profile_verdict": "current_profile_false_positive_high_MAE", "price_source": "Songdaiki/stock-web", "notes": "AI/contact-center software heat should remain RiskWatch unless renewal base, implementation backlog, customer retention and margin conversion are explicit."}
{"row_type": "trigger", "trigger_id": "R8L84-C28-02-S2FP-20240123", "case_id": "R8L84-C28-02", "symbol": "064480", "company_name": "브리지텍", "round": "R8", "loop": 84, "large_sector_id": "L8_PLATFORM_CONTENT_SW_SECURITY", "canonical_archetype_id": "C28_SOFTWARE_SECURITY_CONTRACT_RETENTION", "fine_archetype_id": "ERP_SECURITY_CONTACTCENTER_CONTRACT_RETENTION_ARR_RENEWAL_MARGIN_BRIDGE_VS_AI_SOFTWARE_THEME_FADE", "loop_objective": "coverage_gap_fill|counterexample_mining|software_security_contract_retention_guardrail|local_4B_timing_after_software_MFE|canonical_archetype_compression", "trigger_type": "Stage2-FalsePositive", "trigger_date": "2024-01-23", "evidence_available_at_that_date": "contact-center AI / enterprise software theme proxy without confirmed recurring contract retention and margin bridge", "evidence_source": "source_proxy_only; evidence_url_pending", "stage2_evidence_fields": ["contract_retention_proxy", "ARR_or_maintenance_proxy", "enterprise_customer_proxy"], "stage3_evidence_fields": ["confirmed_ARR_or_recurring_base", "renewal_rate", "churn_control", "implementation_backlog", "gross_or_OP_margin_conversion"], "stage4b_evidence_fields": ["software_MFE_without_retention_bridge", "valuation_overheat", "post_peak_drawdown"], "stage4c_evidence_fields": ["hard_churn_or_contract_loss_watch_only"], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/064/064480/2024.csv", "profile_path": "atlas/symbol_profiles/064/064480.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "entry_date": "2024-01-23", "entry_price": 9980, "MFE_30D_pct": 11.92, "MFE_90D_pct": 11.92, "MFE_180D_pct": 11.92, "MFE_1Y_pct": null, "MFE_2Y_pct": null, "MAE_30D_pct": -25.65, "MAE_90D_pct": -31.16, "MAE_180D_pct": -31.16, "MAE_1Y_pct": null, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2024-01-25", "peak_price": 11170, "drawdown_after_peak_pct": -38.23, "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": 0.3, "four_b_full_window_peak_proximity": 0.25, "four_b_timing_verdict": "AI_software_theme_MFE_rejected_without_contract_retention_margin_bridge", "four_b_evidence_type": ["software_MFE_without_retention_bridge", "post_peak_drawdown", "source_proxy_gap"], "four_c_protection_label": "hard_4C_requires_non_price_churn_or_contract_loss", "trigger_outcome_label": "short_MFE_high_MAE_software_theme_false_positive", "current_profile_verdict": "current_profile_false_positive_high_MAE", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window_after_old_2013_CA_candidate", "same_entry_group_id": "R8L84-C28-02", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R8L84-C28-02", "trigger_id": "R8L84-C28-02-S2FP-20240123", "symbol": "064480", "large_sector_id": "L8_PLATFORM_CONTENT_SW_SECURITY", "canonical_archetype_id": "C28_SOFTWARE_SECURITY_CONTRACT_RETENTION", "raw_component_scores_before": {"contract_retention_score": 15, "ARR_or_maintenance_score": 10, "renewal_visibility_score": 5, "implementation_backlog_score": 10, "customer_quality_score": 15, "gross_margin_bridge_score": 5, "operating_leverage_score": 5, "revision_score": 15, "relative_strength_score": 35, "valuation_blowoff_risk_score": 70, "execution_risk_score": 75, "source_quality_score": 15, "4B_watch_score": 70}, "weighted_score_before": 58, "stage_label_before": "Stage2-Watch/FalsePositive", "raw_component_scores_after": {"contract_retention_score": 15, "ARR_or_maintenance_score": 0, "renewal_visibility_score": 0, "implementation_backlog_score": 10, "customer_quality_score": 15, "gross_margin_bridge_score": 0, "operating_leverage_score": 0, "revision_score": 15, "relative_strength_score": 35, "valuation_blowoff_risk_score": 70, "execution_risk_score": 85, "source_quality_score": 5, "4B_watch_score": 80}, "weighted_score_after": 46, "stage_label_after": "Rejected-Stage2 / RiskWatch", "changed_components": ["ARR_or_maintenance_score", "renewal_visibility_score", "gross_margin_bridge_score", "operating_leverage_score", "source_quality_score", "execution_risk_score", "4B_watch_score"], "component_delta_explanation": "C28 requires recurring contract base, renewal quality, churn control, implementation backlog and margin conversion before clean Stage2/Green; AI/software/security theme MFE alone is demoted or wrapped with local 4B/high-MAE watch.", "MFE_90D_pct": 11.92, "MAE_90D_pct": -31.16, "score_return_alignment_label": "short_MFE_high_MAE_software_theme_false_positive", "current_profile_verdict": "current_profile_false_positive_high_MAE"}
{"row_type": "case", "case_id": "R8L84-C28-03", "symbol": "053350", "company_name": "이니텍", "round": "R8", "loop": 84, "large_sector_id": "L8_PLATFORM_CONTENT_SW_SECURITY", "canonical_archetype_id": "C28_SOFTWARE_SECURITY_CONTRACT_RETENTION", "fine_archetype_id": "ERP_SECURITY_CONTACTCENTER_CONTRACT_RETENTION_ARR_RENEWAL_MARGIN_BRIDGE_VS_AI_SOFTWARE_THEME_FADE", "case_type": "security_authentication_contract_theme_fade", "positive_or_counterexample": "counterexample", "best_trigger": "R8L84-C28-03-S2FP-20240401", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "low_MFE_high_MAE_contract_theme_false_positive", "current_profile_verdict": "current_profile_false_positive_low_quality_MFE", "price_source": "Songdaiki/stock-web", "notes": "Security/authentication maintenance revenue should not be Stage2 unless retention, renewal quality, customer expansion and gross/OP margin bridge are proven at entry."}
{"row_type": "trigger", "trigger_id": "R8L84-C28-03-S2FP-20240401", "case_id": "R8L84-C28-03", "symbol": "053350", "company_name": "이니텍", "round": "R8", "loop": 84, "large_sector_id": "L8_PLATFORM_CONTENT_SW_SECURITY", "canonical_archetype_id": "C28_SOFTWARE_SECURITY_CONTRACT_RETENTION", "fine_archetype_id": "ERP_SECURITY_CONTACTCENTER_CONTRACT_RETENTION_ARR_RENEWAL_MARGIN_BRIDGE_VS_AI_SOFTWARE_THEME_FADE", "loop_objective": "coverage_gap_fill|counterexample_mining|software_security_contract_retention_guardrail|local_4B_timing_after_software_MFE|canonical_archetype_compression", "trigger_type": "Stage2-FalsePositive", "trigger_date": "2024-04-01", "evidence_available_at_that_date": "security/authentication and SI maintenance-contract theme proxy without ARR/renewal/churn or margin bridge", "evidence_source": "source_proxy_only; evidence_url_pending", "stage2_evidence_fields": ["contract_retention_proxy", "ARR_or_maintenance_proxy", "enterprise_customer_proxy"], "stage3_evidence_fields": ["confirmed_ARR_or_recurring_base", "renewal_rate", "churn_control", "implementation_backlog", "gross_or_OP_margin_conversion"], "stage4b_evidence_fields": ["software_MFE_without_retention_bridge", "valuation_overheat", "post_peak_drawdown"], "stage4c_evidence_fields": ["hard_churn_or_contract_loss_watch_only"], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/053/053350/2024.csv", "profile_path": "atlas/symbol_profiles/053/053350.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "entry_date": "2024-04-01", "entry_price": 3535, "MFE_30D_pct": 1.27, "MFE_90D_pct": 4.81, "MFE_180D_pct": 13.72, "MFE_1Y_pct": null, "MFE_2Y_pct": null, "MAE_30D_pct": -9.48, "MAE_90D_pct": -16.27, "MAE_180D_pct": -16.27, "MAE_1Y_pct": null, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2024-08-02", "peak_price": 4020, "drawdown_after_peak_pct": -24.88, "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": 0.3, "four_b_full_window_peak_proximity": 0.25, "four_b_timing_verdict": "security_contract_theme_rejected_without_retention_churn_margin_bridge", "four_b_evidence_type": ["software_MFE_without_retention_bridge", "post_peak_drawdown", "source_proxy_gap"], "four_c_protection_label": "hard_4C_requires_non_price_churn_or_contract_loss", "trigger_outcome_label": "low_MFE_high_MAE_contract_theme_false_positive", "current_profile_verdict": "current_profile_false_positive_low_quality_MFE", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window_after_old_2011_CA_candidate", "same_entry_group_id": "R8L84-C28-03", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R8L84-C28-03", "trigger_id": "R8L84-C28-03-S2FP-20240401", "symbol": "053350", "large_sector_id": "L8_PLATFORM_CONTENT_SW_SECURITY", "canonical_archetype_id": "C28_SOFTWARE_SECURITY_CONTRACT_RETENTION", "raw_component_scores_before": {"contract_retention_score": 15, "ARR_or_maintenance_score": 10, "renewal_visibility_score": 5, "implementation_backlog_score": 10, "customer_quality_score": 15, "gross_margin_bridge_score": 5, "operating_leverage_score": 5, "revision_score": 15, "relative_strength_score": 35, "valuation_blowoff_risk_score": 70, "execution_risk_score": 75, "source_quality_score": 15, "4B_watch_score": 70}, "weighted_score_before": 58, "stage_label_before": "Stage2-Watch/FalsePositive", "raw_component_scores_after": {"contract_retention_score": 15, "ARR_or_maintenance_score": 0, "renewal_visibility_score": 0, "implementation_backlog_score": 10, "customer_quality_score": 15, "gross_margin_bridge_score": 0, "operating_leverage_score": 0, "revision_score": 15, "relative_strength_score": 35, "valuation_blowoff_risk_score": 70, "execution_risk_score": 85, "source_quality_score": 5, "4B_watch_score": 80}, "weighted_score_after": 46, "stage_label_after": "Rejected-Stage2 / RiskWatch", "changed_components": ["ARR_or_maintenance_score", "renewal_visibility_score", "gross_margin_bridge_score", "operating_leverage_score", "source_quality_score", "execution_risk_score", "4B_watch_score"], "component_delta_explanation": "C28 requires recurring contract base, renewal quality, churn control, implementation backlog and margin conversion before clean Stage2/Green; AI/software/security theme MFE alone is demoted or wrapped with local 4B/high-MAE watch.", "MFE_90D_pct": 4.81, "MAE_90D_pct": -16.27, "score_return_alignment_label": "low_MFE_high_MAE_contract_theme_false_positive", "current_profile_verdict": "current_profile_false_positive_low_quality_MFE"}
{"row_type": "shadow_weight", "axis": "C28_contract_retention_ARR_renewal_churn_margin_bridge_required", "scope": "canonical_archetype_specific", "large_sector_id": "L8_PLATFORM_CONTENT_SW_SECURITY", "canonical_archetype_id": "C28_SOFTWARE_SECURITY_CONTRACT_RETENTION", "baseline_value": 0, "tested_value": 1, "delta": "+1", "reason": "Software/security rerating requires recurring contract base, ARR or maintenance revenue, renewal quality, churn control, implementation backlog and margin conversion; AI/software theme MFE alone fades into high MAE or needs local 4B watch.", "backtest_effect": "keeps 060850 only with high-MAE/local 4B watch; demotes 064480/053350 software-security theme false positives", "trigger_ids": "R8L84-C28-01-S2A-20240401|R8L84-C28-02-S2FP-20240123|R8L84-C28-03-S2FP-20240401", "calibration_usable_count": 3, "new_independent_case_count": 3, "counterexample_count": 2, "confidence": "low", "proposal_type": "canonical_shadow_only", "notes": "source_proxy_only/evidence_url_pending; not production"}
{"row_type": "residual_contribution", "round": "R8", "loop": 84, "large_sector_id": "L8_PLATFORM_CONTENT_SW_SECURITY", "canonical_archetype_id": "C28_SOFTWARE_SECURITY_CONTRACT_RETENTION", "new_independent_case_count": 3, "reused_case_count": 0, "new_symbol_count": 3, "new_trigger_family_count": 3, "tested_existing_calibrated_axes": ["stage2_actionable_evidence_bonus", "price_only_blowoff_blocks_positive_stage", "full_4b_requires_non_price_evidence", "hard_4c_thesis_break_routes_to_4c", "source_proxy_only_blocks_runtime_promotion", "high_MAE_guardrail"], "residual_error_types_found": ["software_security_theme_false_positive_high_MAE", "contract_retention_ARR_renewal_churn_margin_bridge_required", "local_4B_late_after_software_MFE", "source_proxy_runtime_promotion_risk", "high_MAE_positive_Green_blocker"], "loop_contribution_label": "canonical_archetype_rule_candidate", "do_not_propose_new_weight_delta": true}
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
- For C28, test a canonical-archetype guard requiring recurring contract base, ARR/maintenance revenue, renewal quality, churn control, implementation backlog and gross/OP margin conversion before clean Stage2/Green.

## 27. Next Round State

```text
completed_round = R8
completed_loop = 84
next_round = R9
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
