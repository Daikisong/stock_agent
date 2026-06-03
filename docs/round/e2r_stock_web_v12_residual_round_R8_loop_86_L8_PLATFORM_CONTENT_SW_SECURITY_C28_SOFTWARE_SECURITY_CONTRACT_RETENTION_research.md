# E2R Stock-Web v12 Residual Research — R8 Loop 86 / L8 / C28

## 0. Research Metadata

```json
{
  "research_session": "post_calibrated_sector_archetype_residual_research",
  "mode": "historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12",
  "scheduled_round": "R8",
  "scheduled_loop": 86,
  "round_schedule_status": "valid",
  "round_sector_consistency": "pass",
  "completed_round": "R8",
  "completed_loop": 86,
  "computed_next_round": "R9",
  "computed_next_loop": 86,
  "large_sector_id": "L8_PLATFORM_CONTENT_SW_SECURITY",
  "canonical_archetype_id": "C28_SOFTWARE_SECURITY_CONTRACT_RETENTION",
  "fine_archetype_id": "DATA_SECURITY_AUTHENTICATION_THREAT_INTELLIGENCE_CONTRACT_RETENTION_ARR_RENEWAL_MARGIN_BRIDGE_VS_SECURITY_AI_THEME_FADE",
  "loop_objective": [
    "coverage_gap_fill",
    "counterexample_mining",
    "software_security_contract_retention_guardrail",
    "security_theme_MFE_vs_contract_retention_ARR_margin_bridge_test",
    "identity_authentication_and_threat_intelligence_theme_fade_test",
    "local_4B_timing_after_security_software_MFE",
    "hard_4C_non_price_contract_churn_or_retention_break_protection",
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
scheduled_loop = 86
allowed_large_sector = L8_PLATFORM_CONTENT_SW_SECURITY
selected_large_sector = L8_PLATFORM_CONTENT_SW_SECURITY
selected_canonical_archetype_id = C28_SOFTWARE_SECURITY_CONTRACT_RETENTION
computed_next_round = R9
computed_next_loop = 86
round_schedule_status = valid
round_sector_consistency = pass
```

R8 is the platform / content / software / security round. This run selects C28 because loop85 R8 used C26 and C28 is the thinner software-security contract-retention route versus C27.

The tested mechanism:

```text
security software / AI security / authentication headline
→ enterprise contract conversion
→ ARR or recurring revenue
→ renewal retention and churn control
→ backlog / pipeline quality
→ gross margin and operating leverage
→ durable rerating or security-theme fade
```

C28 is the renewal ledger. A security theme can pull the door open, but ARR, retention, contract backlog and margin decide whether customers stay inside.

## 3. Previous Coverage / Duplicate Avoidance Check

No-Repeat is used only as a duplicate ledger.

```text
hard_duplicate_key = canonical_archetype_id + symbol + trigger_type + entry_date
```

C28 top-covered symbols include `012510`, `053800`, `263860`, `030520`, `131370`, and `136540`. This run avoids that top-covered set and uses:

```text
150900 / 파수
203650 / 드림시큐리티
411080 / 샌즈랩
```

All three are treated as new independent C28 software/security contract-retention cases for this loop. No hard duplicate is intentionally reused.

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
| 150900 | 파수 | `atlas/symbol_profiles/150/150900.json` | no profile-level CA candidate |
| 203650 | 드림시큐리티 | `atlas/symbol_profiles/203/203650.json` | old 2019 CA candidate; selected 2024 forward window clean |
| 411080 | 샌즈랩 | `atlas/symbol_profiles/411/411080.json` | no profile-level CA candidate |

## 5. Historical Eligibility Gate

| case_id | symbol | entry_date | entry_price | forward window | 180D status | calibration_usable |
|---|---:|---|---:|---:|---|---|
| R8L86-C28-01 | 150900 | 2024-03-26 | 6,710 | 180D | clean | true |
| R8L86-C28-02 | 203650 | 2024-02-13 | 3,725 | 180D | clean | true |
| R8L86-C28-03 | 411080 | 2024-01-23 | 11,410 | 180D | clean | true |

## 6. Canonical Archetype Compression Map

| canonical_archetype_id | fine/deep route | keep / reject logic |
|---|---|---|
| C28_SOFTWARE_SECURITY_CONTRACT_RETENTION | DATA_SECURITY_DRM_CONTRACT_RETENTION | keep Stage2 with enterprise contract, ARR/renewal and margin bridge; add local 4B after MFE |
| C28_SOFTWARE_SECURITY_CONTRACT_RETENTION | AUTHENTICATION_SECURITY_THEME_FADE | reject low-MFE authentication/security rebound without ARR retention and margin bridge |
| C28_SOFTWARE_SECURITY_CONTRACT_RETENTION | AI_THREAT_INTELLIGENCE_THEME_BLOWOFF | reject AI/cyber threat-intelligence MFE without paid retention and contract evidence |

## 7. Case Selection Summary

| case_id | symbol | company | trigger_type | entry_date | entry_price | MFE_180D_pct | MAE_180D_pct | current_profile_verdict |
|---|---:|---|---|---|---:|---:|---:|---|
| R8L86-C28-01 | 150900 | 파수 | Stage2-Actionable | 2024-03-26 | 6,710 | 101.94 | -25.78 | current_profile_partially_correct_local_4B_contract_retention_watch_needed |
| R8L86-C28-02 | 203650 | 드림시큐리티 | Stage2-FalsePositive | 2024-02-13 | 3,725 | 9.4 | -38.39 | current_profile_false_positive_low_MFE_high_MAE |
| R8L86-C28-03 | 411080 | 샌즈랩 | Stage2-FalsePositive | 2024-01-23 | 11,410 | 30.59 | -54.25 | current_profile_false_positive_event_blowoff_high_MAE |

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

This MD creates a source-repair queue and a C28 software-security shadow guardrail candidate. It must not be promoted directly into runtime weights until a later source-repair pass attaches primary evidence URLs: enterprise contract wins, ARR/recurring revenue, renewal retention, churn/cohort data, backlog/pipeline quality, gross margin and operating leverage evidence, disclosure or report evidence.

## 10. Price Data Source Map

| symbol | shard path | profile path |
|---|---|---|
| 150900 | `atlas/ohlcv_tradable_by_symbol_year/150/150900/2024.csv` | `atlas/symbol_profiles/150/150900.json` |
| 203650 | `atlas/ohlcv_tradable_by_symbol_year/203/203650/2024.csv` | `atlas/symbol_profiles/203/203650.json` |
| 411080 | `atlas/ohlcv_tradable_by_symbol_year/411/411080/2024.csv` | `atlas/symbol_profiles/411/411080.json` |

## 11. Case-by-Case Trigger Grid

### Case 1 — 150900 / 파수

C28 data-security/DRM positive with local 4B watch. The March trigger produced a large MFE into April. It is kept as Stage2-Actionable, but clean Green requires ARR, renewal, contract backlog and margin evidence.

### Case 2 — 203650 / 드림시큐리티

C28 authentication/security false positive. The February trigger created only small MFE and later drawdown widened. Identity/security theme language without ARR and renewal evidence should be rejected.

### Case 3 — 411080 / 샌즈랩

C28 AI threat-intelligence false positive. The January AI/security theme spike produced MFE but then collapsed into high MAE. AI security heat without paid contract retention and margin bridge is not clean Stage2.

## 12. Trigger-Level OHLC Backtest Tables

| symbol | entry | MFE30 | MAE30 | MFE90 | MAE90 | MFE180 | MAE180 | peak | post-peak DD |
|---|---:|---:|---:|---:|---:|---:|---:|---|---:|
| 150900 | 6,710 | 101.94 | -6.86 | 101.94 | -16.69 | 101.94 | -25.78 | 2024-04-11 / 13,550 | -63.25 |
| 203650 | 3,725 | 9.40 | -1.07 | 9.40 | -17.45 | 9.40 | -38.39 | 2024-03-13 / 4,075 | -43.80 |
| 411080 | 11,410 | 30.59 | -23.31 | 30.59 | -43.73 | 30.59 | -54.25 | 2024-01-29 / 14,900 | -64.97 |

## 13. Current Calibrated Profile Stress Test

| case_id | P0 likely behavior | actual path | verdict |
|---|---|---|---|
| R8L86-C28-01 | Stage2-Actionable if ARR/renewal bridge exists | large MFE, later drawdown | partially correct; local 4B/contract-retention watch needed |
| R8L86-C28-02 | risk of treating authentication security rebound as Stage2 | low MFE / high MAE | false positive |
| R8L86-C28-03 | risk of treating AI security theme as Stage2 | MFE then severe MAE | false positive / event blowoff |

## 14. Stage2 / Yellow / Green Comparison

```text
green_lateness_ratio = not_applicable
reason = no confirmed Stage3-Green trigger is assigned in this residual MD
```

For C28, the residual is whether security/software MFE becomes clean Stage2/Green before enterprise contract, ARR, renewal retention and margin evidence are proven.

## 15. 4B Local vs Full-window Timing Audit

| case_id | local proximity | full-window proximity | verdict |
|---|---:|---:|---|
| R8L86-C28-01 | 0.90 | 0.80 | local 4B watch after security SW MFE if ARR/renewal/margin bridge stalls |
| R8L86-C28-02 | 0.35 | 0.30 | authentication-security theme rejected without contract retention/ARR bridge |
| R8L86-C28-03 | 0.35 | 0.30 | AI security theme rejected without paid retention/contract bridge |

## 16. 4C Protection Audit

No hard 4C is promoted from this file.

```text
four_c_protection_label = hard_4C_requires_non_price_contract_churn_or_retention_break
hard_4c_price_only_allowed = false
```

Price drawdown alone is not hard 4C. C28 hard 4C requires confirmed contract loss, renewal/churn deterioration, ARR contraction, backlog/pipeline break, gross-margin compression or operating-leverage thesis break.

## 17. Sector-Specific Rule Candidate

```text
rule_scope = no_new_global_rule
sector_specific_rule_candidate = L8/C28 security-software rows need enterprise contracts, ARR/recurring revenue, renewal retention, backlog/pipeline, gross margin and operating leverage before clean Stage2/Green
confidence = low
reason = all evidence rows are source_proxy_only / evidence_url_pending
```

## 18. Canonical-Archetype Rule Candidate

```text
canonical_archetype_id = C28_SOFTWARE_SECURITY_CONTRACT_RETENTION
candidate_axis = C28_security_SW_contract_retention_ARR_renewal_margin_bridge_required
effect = keep data-security positive with local 4B watch; demote authentication/AI-security theme false positives
production_scoring_changed = false
shadow_weight_only = true
do_not_propose_new_weight_delta = true
```

## 19. Before / After Backtest Comparison

| profile | eligible triggers | avg MFE90 | avg MAE90 | false-positive behavior | verdict |
|---|---:|---:|---:|---|---|
| P0 e2r_2_1_stock_web_calibrated_proxy | 3 | 47.31 | -25.96 | may over-credit security/AI theme MFE without ARR bridge | needs C28 contract-retention repair |
| P1 canonical shadow bridge profile | 3 | 101.94 on kept positive | demotes 203650/411080 | better alignment, source repair required |

## 20. Score-Return Alignment Matrix

| case_id | weighted before | label before | weighted after | label after | alignment |
|---|---:|---|---:|---|---|
| R8L86-C28-01 | 78 | Stage2-Actionable | 73 | Stage2-Actionable + local 4B/contract-retention watch | partially aligned |
| R8L86-C28-02 | 58 | Stage2-Watch/FalsePositive | 42 | Rejected-Stage2 / Security-SW theme RiskWatch | improved |
| R8L86-C28-03 | 58 | Stage2-Watch/FalsePositive | 42 | Rejected-Stage2 / Security-SW theme RiskWatch | improved |

## 21. Coverage Matrix

| large_sector_id | canonical_archetype_id | fine_archetype_id | positive | counterexample | 4B | 4C | new cases | reused | usable triggers | current errors | sector rule | canonical rule | coverage gap after |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---|---|---|
| L8_PLATFORM_CONTENT_SW_SECURITY | C28_SOFTWARE_SECURITY_CONTRACT_RETENTION | DATA_SECURITY_AUTHENTICATION_THREAT_INTELLIGENCE_CONTRACT_RETENTION_ARR_RENEWAL_MARGIN_BRIDGE_VS_SECURITY_AI_THEME_FADE | 1 | 2 | 3-watch | 0-hard | 3 | 0 | 3 | 2 | no | yes | source repair needed |

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
  - security_SW_theme_false_positive_high_MAE
  - contract_retention_ARR_renewal_margin_bridge_required
  - AI_security_theme_blowoff
  - local_4B_late_after_security_SW_MFE
  - source_proxy_runtime_promotion_risk
  - hard_4C_requires_non_price_contract_churn_or_retention_break
new_axis_proposed: false
existing_axis_strengthened:
  - C28_security_SW_contract_retention_ARR_renewal_margin_bridge_required
  - source_proxy_only_blocks_runtime_promotion
  - local_4B_watch_before_full_4B_when_MFE_outruns_bridge
  - high_MAE_blocks_clean_Green
existing_axis_weakened: null
existing_axis_kept:
  - full_4b_requires_non_price_evidence
  - hard_4c_thesis_break_routes_to_4c
sector_specific_rule_candidate: null
canonical_archetype_rule_candidate: C28_security_SW_contract_retention_ARR_renewal_margin_bridge_required
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
- enterprise contract evidence
- ARR / recurring revenue evidence
- renewal retention / churn data
- gross margin and operating leverage
- production scoring implementation
```

## 24. Shadow Weight Calibration

```csv
row_type,axis,scope,large_sector_id,canonical_archetype_id,baseline_value,tested_value,delta,reason,backtest_effect,trigger_ids,calibration_usable_count,new_independent_case_count,counterexample_count,confidence,proposal_type,notes
shadow_weight,C28_security_SW_contract_retention_ARR_renewal_margin_bridge_required,canonical_archetype_specific,L8_PLATFORM_CONTENT_SW_SECURITY,C28_SOFTWARE_SECURITY_CONTRACT_RETENTION,0,1,+1,"Require enterprise contracts, ARR/recurring revenue, renewal retention, backlog/pipeline, gross margin and operating leverage before clean Stage2/Green","keeps 150900 with local 4B/contract-retention watch; demotes 203650/411080","R8L86-C28-01-S2A-20240326|R8L86-C28-02-S2FP-20240213|R8L86-C28-03-S2FP-20240123",3,3,2,low,canonical_shadow_only,"source repair required; not production"
```

## 25. Machine-Readable Rows

```jsonl
{"row_type": "price_source_validation", "source": "Songdaiki/stock-web", "source_url": "https://github.com/Songdaiki/stock-web", "manifest_path": "atlas/manifest.json", "schema_path": "atlas/schema.json", "universe_path": "atlas/universe/all_symbols.csv", "manifest_max_date": "2026-02-20", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "raw_shard_root": "atlas/ohlcv_raw_by_symbol_year", "validation_status": "usable_for_historical_calibration"}
{"row_type": "case", "case_id": "R8L86-C28-01", "symbol": "150900", "company_name": "파수", "round": "R8", "loop": 86, "large_sector_id": "L8_PLATFORM_CONTENT_SW_SECURITY", "canonical_archetype_id": "C28_SOFTWARE_SECURITY_CONTRACT_RETENTION", "fine_archetype_id": "DATA_SECURITY_AUTHENTICATION_THREAT_INTELLIGENCE_CONTRACT_RETENTION_ARR_RENEWAL_MARGIN_BRIDGE_VS_SECURITY_AI_THEME_FADE", "case_type": "data_security_DRM_contract_retention_positive_with_local_4B_watch", "positive_or_counterexample": "positive", "best_trigger": "R8L86-C28-01-S2A-20240326", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "large_security_SW_MFE_but_contract_retention_ARR_margin_bridge_required", "current_profile_verdict": "current_profile_partially_correct_local_4B_contract_retention_watch_needed", "price_source": "Songdaiki/stock-web", "notes": "C28 can keep Stage2 only when security-software MFE converts into enterprise contract wins, ARR/renewal retention, backlog quality and margin bridge."}
{"row_type": "trigger", "trigger_id": "R8L86-C28-01-S2A-20240326", "case_id": "R8L86-C28-01", "symbol": "150900", "company_name": "파수", "round": "R8", "loop": 86, "large_sector_id": "L8_PLATFORM_CONTENT_SW_SECURITY", "canonical_archetype_id": "C28_SOFTWARE_SECURITY_CONTRACT_RETENTION", "fine_archetype_id": "DATA_SECURITY_AUTHENTICATION_THREAT_INTELLIGENCE_CONTRACT_RETENTION_ARR_RENEWAL_MARGIN_BRIDGE_VS_SECURITY_AI_THEME_FADE", "loop_objective": "coverage_gap_fill|counterexample_mining|software_security_contract_retention_guardrail|ARR_renewal_margin_bridge|canonical_archetype_compression", "trigger_type": "Stage2-Actionable", "trigger_date": "2024-03-26", "evidence_available_at_that_date": "data security / DRM / enterprise security contract and AI-security demand proxy; primary ARR, renewal, contract backlog and margin evidence pending", "evidence_source": "source_proxy_only; evidence_url_pending", "stage2_evidence_fields": ["security_SW_theme_proxy", "contract_win_proxy", "enterprise_customer_proxy"], "stage3_evidence_fields": ["confirmed_enterprise_contracts", "ARR_or_recurring_revenue", "renewal_retention", "backlog_or_pipeline", "gross_margin_conversion", "operating_leverage"], "stage4b_evidence_fields": ["security_SW_MFE_without_retention_bridge", "AI_security_theme_blowoff", "post_peak_drawdown"], "stage4c_evidence_fields": ["hard_contract_churn_or_retention_break_watch_only"], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/150/150900/2024.csv", "profile_path": "atlas/symbol_profiles/150/150900.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "entry_date": "2024-03-26", "entry_price": 6710, "MFE_30D_pct": 101.94, "MFE_90D_pct": 101.94, "MFE_180D_pct": 101.94, "MFE_1Y_pct": null, "MFE_2Y_pct": null, "MAE_30D_pct": -6.86, "MAE_90D_pct": -16.69, "MAE_180D_pct": -25.78, "MAE_1Y_pct": null, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2024-04-11", "peak_price": 13550, "drawdown_after_peak_pct": -63.25, "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": 0.9, "four_b_full_window_peak_proximity": 0.8, "four_b_timing_verdict": "local_4B_watch_after_security_SW_MFE_if_ARR_renewal_margin_bridge_stalls", "four_b_evidence_type": ["security_SW_MFE_without_contract_retention_bridge", "post_peak_drawdown", "source_proxy_gap"], "four_c_protection_label": "hard_4C_requires_non_price_contract_churn_or_retention_break", "trigger_outcome_label": "large_security_SW_MFE_but_contract_retention_ARR_margin_bridge_required", "current_profile_verdict": "current_profile_partially_correct_local_4B_contract_retention_watch_needed", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_2024_window_no_profile_CA_candidate", "same_entry_group_id": "R8L86-C28-01", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R8L86-C28-01", "trigger_id": "R8L86-C28-01-S2A-20240326", "symbol": "150900", "large_sector_id": "L8_PLATFORM_CONTENT_SW_SECURITY", "canonical_archetype_id": "C28_SOFTWARE_SECURITY_CONTRACT_RETENTION", "raw_component_scores_before": {"contract_win_score": 45, "ARR_or_recurring_revenue_score": 40, "renewal_retention_score": 40, "enterprise_customer_quality_score": 45, "backlog_or_pipeline_score": 40, "gross_margin_bridge_score": 35, "operating_leverage_score": 35, "relative_strength_score": 70, "theme_blowoff_risk_score": 80, "execution_risk_score": 60, "source_quality_score": 20, "4B_watch_score": 45, "4C_watch_score": 25}, "weighted_score_before": 78, "stage_label_before": "Stage2-Actionable", "raw_component_scores_after": {"contract_win_score": 45, "ARR_or_recurring_revenue_score": 40, "renewal_retention_score": 40, "enterprise_customer_quality_score": 45, "backlog_or_pipeline_score": 40, "gross_margin_bridge_score": 35, "operating_leverage_score": 35, "relative_strength_score": 70, "theme_blowoff_risk_score": 90, "execution_risk_score": 70, "source_quality_score": 10, "4B_watch_score": 90, "4C_watch_score": 25}, "weighted_score_after": 73, "stage_label_after": "Stage2-Actionable + local 4B/contract-retention watch", "changed_components": ["contract_win_score", "ARR_or_recurring_revenue_score", "renewal_retention_score", "backlog_or_pipeline_score", "gross_margin_bridge_score", "operating_leverage_score", "source_quality_score", "4B_watch_score", "4C_watch_score"], "component_delta_explanation": "C28 requires software/security MFE to convert into enterprise contracts, ARR/recurring revenue, renewal retention, backlog/pipeline, gross margin and operating leverage before clean Stage2/Green; AI/security theme MFE alone is demoted or wrapped with local 4B/high-MAE watch.", "MFE_90D_pct": 101.94, "MAE_90D_pct": -16.69, "score_return_alignment_label": "large_security_SW_MFE_but_contract_retention_ARR_margin_bridge_required", "current_profile_verdict": "current_profile_partially_correct_local_4B_contract_retention_watch_needed"}
{"row_type": "case", "case_id": "R8L86-C28-02", "symbol": "203650", "company_name": "드림시큐리티", "round": "R8", "loop": 86, "large_sector_id": "L8_PLATFORM_CONTENT_SW_SECURITY", "canonical_archetype_id": "C28_SOFTWARE_SECURITY_CONTRACT_RETENTION", "fine_archetype_id": "DATA_SECURITY_AUTHENTICATION_THREAT_INTELLIGENCE_CONTRACT_RETENTION_ARR_RENEWAL_MARGIN_BRIDGE_VS_SECURITY_AI_THEME_FADE", "case_type": "authentication_security_theme_high_MAE_false_positive", "positive_or_counterexample": "counterexample", "best_trigger": "R8L86-C28-02-S2FP-20240213", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "low_MFE_high_MAE_authentication_security_theme_false_positive", "current_profile_verdict": "current_profile_false_positive_low_MFE_high_MAE", "price_source": "Songdaiki/stock-web", "notes": "Authentication/security theme rebound should remain RiskWatch unless enterprise contract conversion, renewal retention, ARR expansion and gross/OP margin bridge are explicit."}
{"row_type": "trigger", "trigger_id": "R8L86-C28-02-S2FP-20240213", "case_id": "R8L86-C28-02", "symbol": "203650", "company_name": "드림시큐리티", "round": "R8", "loop": 86, "large_sector_id": "L8_PLATFORM_CONTENT_SW_SECURITY", "canonical_archetype_id": "C28_SOFTWARE_SECURITY_CONTRACT_RETENTION", "fine_archetype_id": "DATA_SECURITY_AUTHENTICATION_THREAT_INTELLIGENCE_CONTRACT_RETENTION_ARR_RENEWAL_MARGIN_BRIDGE_VS_SECURITY_AI_THEME_FADE", "loop_objective": "coverage_gap_fill|counterexample_mining|software_security_contract_retention_guardrail|ARR_renewal_margin_bridge|canonical_archetype_compression", "trigger_type": "Stage2-FalsePositive", "trigger_date": "2024-02-13", "evidence_available_at_that_date": "identity authentication / digital security and contract-rebound theme proxy without confirmed ARR, renewal retention or margin bridge", "evidence_source": "source_proxy_only; evidence_url_pending", "stage2_evidence_fields": ["security_SW_theme_proxy", "contract_win_proxy", "enterprise_customer_proxy"], "stage3_evidence_fields": ["confirmed_enterprise_contracts", "ARR_or_recurring_revenue", "renewal_retention", "backlog_or_pipeline", "gross_margin_conversion", "operating_leverage"], "stage4b_evidence_fields": ["security_SW_MFE_without_retention_bridge", "AI_security_theme_blowoff", "post_peak_drawdown"], "stage4c_evidence_fields": ["hard_contract_churn_or_retention_break_watch_only"], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/203/203650/2024.csv", "profile_path": "atlas/symbol_profiles/203/203650.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "entry_date": "2024-02-13", "entry_price": 3725, "MFE_30D_pct": 9.4, "MFE_90D_pct": 9.4, "MFE_180D_pct": 9.4, "MFE_1Y_pct": null, "MFE_2Y_pct": null, "MAE_30D_pct": -1.07, "MAE_90D_pct": -17.45, "MAE_180D_pct": -38.39, "MAE_1Y_pct": null, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2024-03-13", "peak_price": 4075, "drawdown_after_peak_pct": -43.8, "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": 0.35, "four_b_full_window_peak_proximity": 0.3, "four_b_timing_verdict": "authentication_security_theme_rejected_without_contract_retention_ARR_margin_bridge", "four_b_evidence_type": ["security_SW_MFE_without_contract_retention_bridge", "post_peak_drawdown", "source_proxy_gap"], "four_c_protection_label": "hard_4C_requires_non_price_contract_churn_or_retention_break", "trigger_outcome_label": "low_MFE_high_MAE_authentication_security_theme_false_positive", "current_profile_verdict": "current_profile_false_positive_low_MFE_high_MAE", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_2024_window_after_old_2019_CA_candidate", "same_entry_group_id": "R8L86-C28-02", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R8L86-C28-02", "trigger_id": "R8L86-C28-02-S2FP-20240213", "symbol": "203650", "large_sector_id": "L8_PLATFORM_CONTENT_SW_SECURITY", "canonical_archetype_id": "C28_SOFTWARE_SECURITY_CONTRACT_RETENTION", "raw_component_scores_before": {"contract_win_score": 15, "ARR_or_recurring_revenue_score": 5, "renewal_retention_score": 5, "enterprise_customer_quality_score": 15, "backlog_or_pipeline_score": 10, "gross_margin_bridge_score": 5, "operating_leverage_score": 5, "relative_strength_score": 40, "theme_blowoff_risk_score": 85, "execution_risk_score": 85, "source_quality_score": 15, "4B_watch_score": 80, "4C_watch_score": 45}, "weighted_score_before": 58, "stage_label_before": "Stage2-Watch/FalsePositive", "raw_component_scores_after": {"contract_win_score": 5, "ARR_or_recurring_revenue_score": 0, "renewal_retention_score": 0, "enterprise_customer_quality_score": 15, "backlog_or_pipeline_score": 0, "gross_margin_bridge_score": 0, "operating_leverage_score": 0, "relative_strength_score": 40, "theme_blowoff_risk_score": 85, "execution_risk_score": 95, "source_quality_score": 5, "4B_watch_score": 95, "4C_watch_score": 70}, "weighted_score_after": 42, "stage_label_after": "Rejected-Stage2 / Security-SW theme RiskWatch", "changed_components": ["contract_win_score", "ARR_or_recurring_revenue_score", "renewal_retention_score", "backlog_or_pipeline_score", "gross_margin_bridge_score", "operating_leverage_score", "source_quality_score", "4B_watch_score", "4C_watch_score"], "component_delta_explanation": "C28 requires software/security MFE to convert into enterprise contracts, ARR/recurring revenue, renewal retention, backlog/pipeline, gross margin and operating leverage before clean Stage2/Green; AI/security theme MFE alone is demoted or wrapped with local 4B/high-MAE watch.", "MFE_90D_pct": 9.4, "MAE_90D_pct": -17.45, "score_return_alignment_label": "low_MFE_high_MAE_authentication_security_theme_false_positive", "current_profile_verdict": "current_profile_false_positive_low_MFE_high_MAE"}
{"row_type": "case", "case_id": "R8L86-C28-03", "symbol": "411080", "company_name": "샌즈랩", "round": "R8", "loop": 86, "large_sector_id": "L8_PLATFORM_CONTENT_SW_SECURITY", "canonical_archetype_id": "C28_SOFTWARE_SECURITY_CONTRACT_RETENTION", "fine_archetype_id": "DATA_SECURITY_AUTHENTICATION_THREAT_INTELLIGENCE_CONTRACT_RETENTION_ARR_RENEWAL_MARGIN_BRIDGE_VS_SECURITY_AI_THEME_FADE", "case_type": "AI_threat_intelligence_security_theme_blowoff_counterexample", "positive_or_counterexample": "counterexample", "best_trigger": "R8L86-C28-03-S2FP-20240123", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "security_AI_theme_MFE_then_deep_MAE_false_positive", "current_profile_verdict": "current_profile_false_positive_event_blowoff_high_MAE", "price_source": "Songdaiki/stock-web", "notes": "AI/cyber threat-intelligence theme MFE should not validate C28 unless paid contract retention, ARR growth, renewal cohort quality and margin conversion are source-repaired."}
{"row_type": "trigger", "trigger_id": "R8L86-C28-03-S2FP-20240123", "case_id": "R8L86-C28-03", "symbol": "411080", "company_name": "샌즈랩", "round": "R8", "loop": 86, "large_sector_id": "L8_PLATFORM_CONTENT_SW_SECURITY", "canonical_archetype_id": "C28_SOFTWARE_SECURITY_CONTRACT_RETENTION", "fine_archetype_id": "DATA_SECURITY_AUTHENTICATION_THREAT_INTELLIGENCE_CONTRACT_RETENTION_ARR_RENEWAL_MARGIN_BRIDGE_VS_SECURITY_AI_THEME_FADE", "loop_objective": "coverage_gap_fill|counterexample_mining|software_security_contract_retention_guardrail|ARR_renewal_margin_bridge|canonical_archetype_compression", "trigger_type": "Stage2-FalsePositive", "trigger_date": "2024-01-23", "evidence_available_at_that_date": "AI threat intelligence / cyber-security platform theme proxy without confirmed paid contract retention, ARR or margin bridge", "evidence_source": "source_proxy_only; evidence_url_pending", "stage2_evidence_fields": ["security_SW_theme_proxy", "contract_win_proxy", "enterprise_customer_proxy"], "stage3_evidence_fields": ["confirmed_enterprise_contracts", "ARR_or_recurring_revenue", "renewal_retention", "backlog_or_pipeline", "gross_margin_conversion", "operating_leverage"], "stage4b_evidence_fields": ["security_SW_MFE_without_retention_bridge", "AI_security_theme_blowoff", "post_peak_drawdown"], "stage4c_evidence_fields": ["hard_contract_churn_or_retention_break_watch_only"], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/411/411080/2024.csv", "profile_path": "atlas/symbol_profiles/411/411080.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "entry_date": "2024-01-23", "entry_price": 11410, "MFE_30D_pct": 30.59, "MFE_90D_pct": 30.59, "MFE_180D_pct": 30.59, "MFE_1Y_pct": null, "MFE_2Y_pct": null, "MAE_30D_pct": -23.31, "MAE_90D_pct": -43.73, "MAE_180D_pct": -54.25, "MAE_1Y_pct": null, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2024-01-29", "peak_price": 14900, "drawdown_after_peak_pct": -64.97, "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": 0.35, "four_b_full_window_peak_proximity": 0.3, "four_b_timing_verdict": "AI_security_theme_MFE_rejected_without_paid_retention_contract_margin_bridge", "four_b_evidence_type": ["security_SW_MFE_without_contract_retention_bridge", "post_peak_drawdown", "source_proxy_gap"], "four_c_protection_label": "hard_4C_requires_non_price_contract_churn_or_retention_break", "trigger_outcome_label": "security_AI_theme_MFE_then_deep_MAE_false_positive", "current_profile_verdict": "current_profile_false_positive_event_blowoff_high_MAE", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_2024_window_no_profile_CA_candidate", "same_entry_group_id": "R8L86-C28-03", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R8L86-C28-03", "trigger_id": "R8L86-C28-03-S2FP-20240123", "symbol": "411080", "large_sector_id": "L8_PLATFORM_CONTENT_SW_SECURITY", "canonical_archetype_id": "C28_SOFTWARE_SECURITY_CONTRACT_RETENTION", "raw_component_scores_before": {"contract_win_score": 15, "ARR_or_recurring_revenue_score": 5, "renewal_retention_score": 5, "enterprise_customer_quality_score": 15, "backlog_or_pipeline_score": 10, "gross_margin_bridge_score": 5, "operating_leverage_score": 5, "relative_strength_score": 40, "theme_blowoff_risk_score": 85, "execution_risk_score": 85, "source_quality_score": 15, "4B_watch_score": 80, "4C_watch_score": 45}, "weighted_score_before": 58, "stage_label_before": "Stage2-Watch/FalsePositive", "raw_component_scores_after": {"contract_win_score": 5, "ARR_or_recurring_revenue_score": 0, "renewal_retention_score": 0, "enterprise_customer_quality_score": 15, "backlog_or_pipeline_score": 0, "gross_margin_bridge_score": 0, "operating_leverage_score": 0, "relative_strength_score": 40, "theme_blowoff_risk_score": 85, "execution_risk_score": 95, "source_quality_score": 5, "4B_watch_score": 95, "4C_watch_score": 70}, "weighted_score_after": 42, "stage_label_after": "Rejected-Stage2 / Security-SW theme RiskWatch", "changed_components": ["contract_win_score", "ARR_or_recurring_revenue_score", "renewal_retention_score", "backlog_or_pipeline_score", "gross_margin_bridge_score", "operating_leverage_score", "source_quality_score", "4B_watch_score", "4C_watch_score"], "component_delta_explanation": "C28 requires software/security MFE to convert into enterprise contracts, ARR/recurring revenue, renewal retention, backlog/pipeline, gross margin and operating leverage before clean Stage2/Green; AI/security theme MFE alone is demoted or wrapped with local 4B/high-MAE watch.", "MFE_90D_pct": 30.59, "MAE_90D_pct": -43.73, "score_return_alignment_label": "security_AI_theme_MFE_then_deep_MAE_false_positive", "current_profile_verdict": "current_profile_false_positive_event_blowoff_high_MAE"}
{"row_type": "shadow_weight", "axis": "C28_security_SW_contract_retention_ARR_renewal_margin_bridge_required", "scope": "canonical_archetype_specific", "large_sector_id": "L8_PLATFORM_CONTENT_SW_SECURITY", "canonical_archetype_id": "C28_SOFTWARE_SECURITY_CONTRACT_RETENTION", "baseline_value": 0, "tested_value": 1, "delta": "+1", "reason": "Software/security rerating requires confirmed enterprise contracts, ARR/recurring revenue, renewal retention, backlog/pipeline, gross margin and operating leverage; AI/security theme MFE without bridge fades into high MAE or event blowoff.", "backtest_effect": "keeps 150900 with local 4B/contract-retention watch; demotes 203650/411080 security theme false positives", "trigger_ids": "R8L86-C28-01-S2A-20240326|R8L86-C28-02-S2FP-20240213|R8L86-C28-03-S2FP-20240123", "calibration_usable_count": 3, "new_independent_case_count": 3, "counterexample_count": 2, "confidence": "low", "proposal_type": "canonical_shadow_only", "notes": "source_proxy_only/evidence_url_pending; not production"}
{"row_type": "residual_contribution", "round": "R8", "loop": 86, "large_sector_id": "L8_PLATFORM_CONTENT_SW_SECURITY", "canonical_archetype_id": "C28_SOFTWARE_SECURITY_CONTRACT_RETENTION", "new_independent_case_count": 3, "reused_case_count": 0, "new_symbol_count": 3, "new_trigger_family_count": 3, "tested_existing_calibrated_axes": ["stage2_actionable_evidence_bonus", "price_only_blowoff_blocks_positive_stage", "full_4b_requires_non_price_evidence", "hard_4c_thesis_break_routes_to_4c", "source_proxy_only_blocks_runtime_promotion", "high_MAE_guardrail", "local_4B_watch_before_full_4B_when_MFE_outruns_bridge"], "residual_error_types_found": ["security_SW_theme_false_positive_high_MAE", "contract_retention_ARR_renewal_margin_bridge_required", "AI_security_theme_blowoff", "local_4B_late_after_security_SW_MFE", "source_proxy_runtime_promotion_risk", "hard_4C_requires_non_price_contract_churn_or_retention_break"], "loop_contribution_label": "canonical_archetype_rule_candidate", "do_not_propose_new_weight_delta": true}
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
- For C28, test a canonical-archetype guard requiring enterprise contracts, ARR/recurring revenue, renewal retention, backlog/pipeline, gross margin and operating leverage before clean Stage2/Green. Keep hard 4C blocked unless a non-price contract churn or retention thesis break is confirmed.

## 27. Next Round State

```text
completed_round = R8
completed_loop = 86
next_round = R9
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
