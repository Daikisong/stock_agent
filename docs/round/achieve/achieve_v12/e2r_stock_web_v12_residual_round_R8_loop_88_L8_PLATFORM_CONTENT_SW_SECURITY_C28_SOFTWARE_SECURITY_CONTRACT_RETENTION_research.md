# E2R Stock-Web Historical Calibration / Sector-Archetype Residual Research Round

## 0. Research Metadata

```text
research_session = post_calibrated_sector_archetype_residual_research
mode = historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12
scheduled_round = R8
scheduled_loop = 88
round_schedule_status = valid
round_sector_consistency = pass
large_sector_id = L8_PLATFORM_CONTENT_SW_SECURITY
canonical_archetype_id = C28_SOFTWARE_SECURITY_CONTRACT_RETENTION
fine_archetype_id = AI_OFFICE_SOFTWARE_CONTRACT_BRIDGE_VS_SECURITY_AND_DATA_AI_THEME_EVENT_CAP
loop_objective = coverage_gap_fill | counterexample_mining | stage2_actionable_bonus_stress_test | 4B_non_price_requirement_stress_test | canonical_archetype_compression
output_file = e2r_stock_web_v12_residual_round_R8_loop_88_L8_PLATFORM_CONTENT_SW_SECURITY_C28_SOFTWARE_SECURITY_CONTRACT_RETENTION_research.md
```

This loop continues loop 88 after R7. It adds 3 C28 software/security cases: one AI office software / product-contract bridge positive, one security-quality false Stage2, and one data/AI software theme 4B event-cap counterexample.

## 1. Current Calibrated Profile Assumption

```text
current_default_profile_proxy = e2r_2_1_stock_web_calibrated
previous_baseline_reference = e2r_2_0_baseline
production_scoring_changed = false
shadow_weight_only = true
```

Existing axes tested:

```text
stage2_required_bridge = existing_axis_strengthened
local_4b_watch_guard = existing_axis_strengthened
full_4b_requires_non_price_evidence = existing_axis_kept
price_only_blowoff_blocks_positive_stage = existing_axis_kept
hard_4c_thesis_break_routes_to_4c = existing_axis_kept
```

## 2. Round / Large Sector / Canonical Archetype Scope

```text
scheduled_round = R8
scheduled_loop = 88
large_sector_id = L8_PLATFORM_CONTENT_SW_SECURITY
canonical_archetype_id = C28_SOFTWARE_SECURITY_CONTRACT_RETENTION
round_sector_consistency = pass
computed_next_round = R9
computed_next_loop = 88
```

R8 permits L8 platform/content/software/security research. This loop chooses C28 rather than C26/C27 because the residual question is clean: software/security names can look recurring by label, but the price path separates real product/contract bridge from AI/security theme premium.

## 3. Previous Coverage / Duplicate Avoidance Check

No-Repeat hard key used:

```text
canonical_archetype_id + symbol + trigger_type + entry_date
```

No-Repeat snapshot context:

```text
C28_SOFTWARE_SECURITY_CONTRACT_RETENTION = 26 rows / 19 symbols / good-bad Stage2 10-4 / 4B-4C 0-0
top covered symbols include 058970(3), 150900(3), 042510(2), 203650(2), 307950(2), 012510(1)
```

Selected rows avoid those repeated combinations:

```text
030520 / Stage2-Actionable / 2024-01-05
053800 / Stage2-Actionable / 2024-01-22
263800 / Stage4B / 2024-04-01
```

## 4. Stock-Web OHLC Input / Price Source Validation

| field | value |
|---|---|
| source | Songdaiki/stock-web |
| upstream_source | FinanceData/marcap |
| manifest | atlas/manifest.json |
| stock_web_manifest_max_date | 2026-02-20 |
| price_basis | tradable_raw |
| price_adjustment_status | raw_unadjusted_marcap |
| calibration_shard_root | atlas/ohlcv_tradable_by_symbol_year |

| symbol | profile path | CA window status |
|---|---|---|
| 030520 | atlas/symbol_profiles/030/030520.json | selected 2024 window clean; CA candidates are pre-2007 |
| 053800 | atlas/symbol_profiles/053/053800.json | selected 2024 window clean; CA candidate is 2005-03-31 |
| 263800 | atlas/symbol_profiles/263/263800.json | no corporate-action candidate |

## 5. Historical Eligibility Gate

| case_id | symbol | entry_date | entry in shard | forward 180D | OHLC valid | CA clean | calibration_usable |
|---|---|---:|---|---:|---|---|---|
| R8L88_C28_HAANSOFT_2024_AI_OFFICE_SOFTWARE_RERATING_POSITIVE | 030520 | 2024-01-05 | yes | 180 | yes | yes | true |
| R8L88_C28_AHNLAB_2024_SECURITY_QUALITY_FALSE_STAGE2 | 053800 | 2024-01-22 | yes | 180 | yes | yes | true |
| R8L88_C28_DATASOLUTION_2024_DATA_AI_THEME_EVENT_CAP_4B | 263800 | 2024-04-01 | yes | 180 | yes | yes | true |

## 6. Canonical Archetype Compression Map

| canonical | fine/deep split | meaning |
|---|---|---|
| C28_SOFTWARE_SECURITY_CONTRACT_RETENTION | AI_OFFICE_SOFTWARE_CONTRACT_BRIDGE | Positive Stage2 requires product/contract/revenue bridge, not AI label alone. |
| C28_SOFTWARE_SECURITY_CONTRACT_RETENTION | SECURITY_QUALITY_FALSE_STAGE2 | Security-quality label without renewal/retention/revision bridge can be weak-MFE false Stage2. |
| C28_SOFTWARE_SECURITY_CONTRACT_RETENTION | DATA_AI_THEME_EVENT_CAP | Data/AI software theme spikes route to 4B if contract-retention bridge is missing. |

## 7. Case Selection Summary

| case_id | symbol | company | role | selected reason |
|---|---|---|---|---|
| R8L88_C28_HAANSOFT_2024_AI_OFFICE_SOFTWARE_RERATING_POSITIVE | 030520 | 한글과컴퓨터 | positive | AI office/product bridge produced very high MFE with low initial MAE. |
| R8L88_C28_AHNLAB_2024_SECURITY_QUALITY_FALSE_STAGE2 | 053800 | 안랩 | counterexample | Security-quality label produced weak MFE and slow drawdown without bridge. |
| R8L88_C28_DATASOLUTION_2024_DATA_AI_THEME_EVENT_CAP_4B | 263800 | 데이타솔루션 | counterexample / 4B | Data/AI theme premium capped quickly and drew down. |

## 8. Positive vs Counterexample Balance

```text
positive_case_count = 1
counterexample_count = 2
4B_case_count = 1
4C_case_count = 0
calibration_usable_case_count = 3
calibration_usable_trigger_count = 3
```

## 9. Evidence Source Map

| case | evidence status | evidence_url_pending | source_proxy_only | usage |
|---|---|---|---|---|
| Hancom AI office software | historical public/report proxy | true | true | shadow-only positive |
| AhnLab security quality | historical public/report proxy | true | true | false-Stage2 guardrail |
| DataSolution data/AI cap | historical public/news proxy | true | true | 4B overlay counterexample |

## 10. Price Data Source Map

| symbol | shard | profile |
|---|---|---|
| 030520 | atlas/ohlcv_tradable_by_symbol_year/030/030520/2024.csv | atlas/symbol_profiles/030/030520.json |
| 053800 | atlas/ohlcv_tradable_by_symbol_year/053/053800/2024.csv | atlas/symbol_profiles/053/053800.json |
| 263800 | atlas/ohlcv_tradable_by_symbol_year/263/263800/2024.csv | atlas/symbol_profiles/263/263800.json |

## 11. Case-by-Case Trigger Grid

| trigger_id | symbol | trigger_type | entry_date | entry_price | role | verdict |
|---|---|---|---:|---:|---|---|
| R8L88_C28_HAANSOFT_2024_STAGE2_ACTIONABLE_AI_OFFICE_SOFTWARE | 030520 | Stage2-Actionable | 2024-01-05 | 14970 | positive | AI office software bridge worked |
| R8L88_C28_AHNLAB_2024_STAGE2_FALSE_POSITIVE_SECURITY_QUALITY | 053800 | Stage2-Actionable | 2024-01-22 | 72500 | counterexample | security quality false Stage2 |
| R8L88_C28_DATASOLUTION_2024_STAGE4B_DATA_AI_THEME_CAP | 263800 | Stage4B | 2024-04-01 | 7630 | counterexample/4B | data/AI theme event cap |

## 12. Trigger-Level OHLC Backtest Tables

| trigger_id | entry | MFE30 | MAE30 | MFE90 | MAE90 | MFE180 | MAE180 | peak_date | peak_price | drawdown_after_peak |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| R8L88_C28_HAANSOFT_2024_STAGE2_ACTIONABLE_AI_OFFICE_SOFTWARE | 14970 | 156.85 | -5.68 | 156.85 | -5.68 | 156.85 | -5.68 | 2024-01-22 | 38450 | -48.63 |
| R8L88_C28_AHNLAB_2024_STAGE2_FALSE_POSITIVE_SECURITY_QUALITY | 72500 | 4.14 | -5.52 | 4.28 | -14.48 | 4.28 | -22.76 | 2024-04-12 | 75600 | -25.93 |
| R8L88_C28_DATASOLUTION_2024_STAGE4B_DATA_AI_THEME_CAP | 7630 | 8.78 | -15.33 | 8.78 | -37.55 | 8.78 | -49.54 | 2024-04-02 | 8300 | -53.61 |

## 13. Current Calibrated Profile Stress Test

| axis | outcome |
|---|---|
| stage2_required_bridge | strengthen: C28 Stage2 needs product/contract/retention/revenue or revision bridge |
| local_4b_watch_guard | strengthen: software/data/AI theme premium should route to 4B watch |
| full_4b_requires_non_price_evidence | keep |
| price_only_blowoff_blocks_positive_stage | keep |
| hard_4c_thesis_break_routes_to_4c | keep |

## 14. Stage2 / Yellow / Green Comparison

No confirmed Stage3-Green row is introduced. The useful split is Stage2/4B quality:

| symbol | stage quality | explanation |
|---|---|---|
| 030520 | good_stage2 | Product/AI software narrative aligned with strong early rerating. |
| 053800 | bad_stage2 | Security quality alone did not produce enough MFE. |
| 263800 | good_4B | Data/AI theme premium capped and then drew down heavily. |

```text
green_lateness_ratio = not_applicable
reason = no_confirmed_Stage3_Green_trigger
```

## 15. 4B Local vs Full-window Timing Audit

| trigger | local proximity | full-window proximity | timing verdict |
|---|---:|---:|---|
| 263800 data/AI software cap | 1.00 | 1.00 | good_full_window_4B_timing_data_AI_software_theme_event_cap |
| 053800 security false Stage2 | 0.04 | 0.04 | weak_MFE_false_stage2_security_quality_without_contract_revision_bridge |
| 030520 AI office software | n/a | n/a | positive Stage2; later valuation watch only |

## 16. 4C Protection Audit

```text
4C_case_count = 0
four_c_protection_label = thesis_break_watch_only for 263800
```

No hard 4C candidate is proposed. C28 residual here is Stage2 bridge quality and 4B event-cap timing.

## 17. Sector-Specific Rule Candidate

```text
sector_specific_rule_candidate = true
rule_scope = sector_specific
rule = In L8 software/security cases, Stage2 requires verified product adoption, contract retention, ARR/revenue visibility, renewal quality, or margin/revision bridge. AI/security/data labels alone remain watch/4B.
proposal_status = shadow_only
```

## 18. Canonical-Archetype Rule Candidate

```text
canonical_archetype_rule_candidate = true
canonical_archetype_id = C28_SOFTWARE_SECURITY_CONTRACT_RETENTION
rule = C28 should split software contract/revenue bridge positives from security-quality false Stage2 and AI/data theme event caps. Event-cap rows are 4B overlay/risk calibration, not Stage3-Green promotion evidence.
proposal_status = shadow_only_not_production
```

## 19. Before / After Backtest Comparison

| profile | hypothesis | eligible triggers | avg_MFE90 | avg_MAE90 | false_positive_rate | verdict |
|---|---|---:|---:|---:|---:|---|
| P0 e2r_2_1_stock_web_calibrated_proxy | current profile | 3 | 56.64 | -19.24 | 0.67 | mixed; C28 split needed |
| P0b e2r_2_0_baseline_reference | older baseline | 3 | 56.64 | -19.24 | 0.67 | weaker bridge/theme guard |
| P1 sector_specific_candidate_profile | L8 contract bridge required | 2 | 80.57 | -10.08 | 0.50 | better |
| P2 canonical_archetype_candidate_profile | C28 bridge vs event-cap split | 2 | 80.57 | -10.08 | 0.50 | best explanatory fit |
| P3 counterexample_guard_profile | reject security/data theme caps as positive | 1 | 156.85 | -5.68 | 0.00 | safest but source-proxy blockers remain |

## 20. Score-Return Alignment Matrix

| trigger | score before | stage before | score after | stage after | MFE90 | MAE90 | alignment |
|---|---:|---|---:|---|---:|---:|---|
| 030520 AI office software | 66 | Stage2-Watch | 75 | Stage2-Actionable | 156.85 | -5.68 | AI_office_software_contract_bridge_positive |
| 053800 security quality | 65 | Stage2-Actionable | 55 | Stage1/Watch | 4.28 | -14.48 | security_quality_without_contract_bridge_false_stage2 |
| 263800 data/AI cap | 70 | Stage3-Yellow-like | 54 | Stage4B-watch | 8.78 | -37.55 | data_AI_theme_event_cap_4B_guard |

## 21. Coverage Matrix

```jsonl
{"row_type": "coverage_matrix", "large_sector_id": "L8_PLATFORM_CONTENT_SW_SECURITY", "canonical_archetype_id": "C28_SOFTWARE_SECURITY_CONTRACT_RETENTION", "fine_archetype_id": "AI_OFFICE_SOFTWARE_CONTRACT_BRIDGE_VS_SECURITY_AND_DATA_AI_THEME_EVENT_CAP", "positive_case_count": 1, "counterexample_count": 2, "4B_case_count": 1, "4C_case_count": 0, "new_independent_case_count": 3, "reused_case_count": 0, "calibration_usable_trigger_count": 3, "representative_trigger_count": 2, "current_profile_error_count": 2, "sector_rule_candidate": true, "canonical_rule_candidate": true, "coverage_gap_after_this_loop": "Adds C28 AI office software bridge positive, security-quality false Stage2, and data/AI theme event-cap 4B split using non-top-covered symbols."}
```

## 22. Residual Contribution Summary

```text
new_independent_case_count: 3
reused_case_count: 0
reused_case_ids: []
new_symbol_count: 3
new_canonical_archetype_count: 0
new_fine_archetype_count: 1
new_trigger_family_count: 3
tested_existing_calibrated_axes: stage2_required_bridge, local_4b_watch_guard, full_4b_requires_non_price_evidence, price_only_blowoff_blocks_positive_stage
residual_error_types_found: AI_office_software_contract_bridge_positive, security_quality_false_stage2, data_AI_theme_event_cap_4B
new_axis_proposed: null
existing_axis_strengthened: stage2_required_bridge, local_4b_watch_guard
existing_axis_weakened: null
existing_axis_kept: full_4b_requires_non_price_evidence, price_only_blowoff_blocks_positive_stage, hard_4c_thesis_break_routes_to_4c
sector_specific_rule_candidate: true
canonical_archetype_rule_candidate: true
no_new_signal_reason: null
loop_contribution_label: canonical_archetype_rule_candidate
do_not_propose_new_weight_delta: true
```

## 23. Validation Scope / Non-Validation Scope

Validation scope:

```text
- Stock-web tradable raw OHLC path
- entry_date / entry_price
- MFE/MAE 30D/90D/180D
- corporate-action window cleanliness
- C28 software/security contract-retention bridge vs software/AI theme event-cap split
```

Non-validation scope:

```text
- Exact as-of evidence URLs remain pending for all selected cases.
- No production scoring update.
- No live candidate scan.
- No investment recommendation.
```

## 24. Shadow Weight Calibration

```csv
row_type,axis,scope,large_sector_id,canonical_archetype_id,baseline_value,tested_value,delta,reason,backtest_effect,trigger_ids,calibration_usable_count,new_independent_case_count,counterexample_count,confidence,proposal_type,notes
shadow_weight,stage2_required_bridge,canonical_archetype,L8_PLATFORM_CONTENT_SW_SECURITY,C28_SOFTWARE_SECURITY_CONTRACT_RETENTION,configured,C28_requires_contract_retention_revenue_revision_bridge,0,"C28 Stage2 should require product/contract retention, renewal, ARR/revenue or margin/revision bridge, not software/security/AI theme label alone","Hancom positive worked; AhnLab and DataSolution rows failed positive-stage promotion","R8L88_C28_HAANSOFT_2024_STAGE2_ACTIONABLE_AI_OFFICE_SOFTWARE|R8L88_C28_AHNLAB_2024_STAGE2_FALSE_POSITIVE_SECURITY_QUALITY|R8L88_C28_DATASOLUTION_2024_STAGE4B_DATA_AI_THEME_CAP",3,3,2,low,canonical_shadow_only,"do_not_propose_new_weight_delta=true because source-proxy/evidence-url-pending rows remain"
shadow_weight,local_4b_watch_guard,canonical_archetype,L8_PLATFORM_CONTENT_SW_SECURITY,C28_SOFTWARE_SECURITY_CONTRACT_RETENTION,configured,cap_software_AI_theme_premium_as_4B_watch,0,"Data/AI and security/software theme premiums can peak before verified contract-retention or revenue bridge appears","DataSolution showed full-window event-cap behavior; AhnLab showed weak-MFE false Stage2 behavior","R8L88_C28_AHNLAB_2024_STAGE2_FALSE_POSITIVE_SECURITY_QUALITY|R8L88_C28_DATASOLUTION_2024_STAGE4B_DATA_AI_THEME_CAP",2,2,2,low,guardrail_shadow_only,"4B overlay only; not production"
```

## 25. Machine-Readable Rows

### 25.1 price_source_validation

```jsonl
{"row_type": "price_source_validation", "source": "Songdaiki/stock-web", "source_url": "https://github.com/Songdaiki/stock-web", "manifest_path": "atlas/manifest.json", "schema_path": "atlas/schema.json", "universe_path": "atlas/universe/all_symbols.csv", "manifest_max_date": "2026-02-20", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "raw_shard_root": "atlas/ohlcv_raw_by_symbol_year", "validation_status": "usable_for_historical_calibration", "source_name": "FinanceData/marcap", "tradable_row_count": 14354401, "raw_row_count": 15214118, "symbol_count": 5414, "active_like_symbol_count": 2868, "inactive_or_delisted_like_symbol_count": 2546}
```

### 25.2 case rows

```jsonl
{"row_type": "case", "case_id": "R8L88_C28_HAANSOFT_2024_AI_OFFICE_SOFTWARE_RERATING_POSITIVE", "symbol": "030520", "company_name": "한글과컴퓨터", "round": "R8", "loop": "88", "large_sector_id": "L8_PLATFORM_CONTENT_SW_SECURITY", "canonical_archetype_id": "C28_SOFTWARE_SECURITY_CONTRACT_RETENTION", "fine_archetype_id": "AI_OFFICE_SOFTWARE_CONTRACT_BRIDGE_VS_SECURITY_AND_DATA_AI_THEME_EVENT_CAP", "case_type": "structural_success", "positive_or_counterexample": "positive", "best_trigger": "R8L88_C28_HAANSOFT_2024_STAGE2_ACTIONABLE_AI_OFFICE_SOFTWARE", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "AI office/software rerating worked as a Stage2 path when the market could map product/contract narrative into software revenue leverage; 30D/90D MFE was very high with limited initial MAE.", "current_profile_verdict": "current_profile_kept_but_C28_positive_requires_product_contract_retention_bridge_not_AI_label_only", "price_source": "Songdaiki/stock-web", "notes": "Source-proxy only; exact as-of product/contract evidence URL remains pending, so no production weight delta."}
{"row_type": "case", "case_id": "R8L88_C28_AHNLAB_2024_SECURITY_QUALITY_FALSE_STAGE2", "symbol": "053800", "company_name": "안랩", "round": "R8", "loop": "88", "large_sector_id": "L8_PLATFORM_CONTENT_SW_SECURITY", "canonical_archetype_id": "C28_SOFTWARE_SECURITY_CONTRACT_RETENTION", "fine_archetype_id": "AI_OFFICE_SOFTWARE_CONTRACT_BRIDGE_VS_SECURITY_AND_DATA_AI_THEME_EVENT_CAP", "case_type": "failed_rerating", "positive_or_counterexample": "counterexample", "best_trigger": "R8L88_C28_AHNLAB_2024_STAGE2_FALSE_POSITIVE_SECURITY_QUALITY", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "Security-quality / steady contract label alone produced weak forward upside and meaningful MAE; C28 Stage2 should require ARR/renewal/contract-retention or margin bridge.", "current_profile_verdict": "current_profile_false_positive_if_security_quality_counts_without_contract_retention_revision_bridge", "price_source": "Songdaiki/stock-web", "notes": "New C28 security-quality false Stage2 row; source-proxy only."}
{"row_type": "case", "case_id": "R8L88_C28_DATASOLUTION_2024_DATA_AI_THEME_EVENT_CAP_4B", "symbol": "263800", "company_name": "데이타솔루션", "round": "R8", "loop": "88", "large_sector_id": "L8_PLATFORM_CONTENT_SW_SECURITY", "canonical_archetype_id": "C28_SOFTWARE_SECURITY_CONTRACT_RETENTION", "fine_archetype_id": "AI_OFFICE_SOFTWARE_CONTRACT_BRIDGE_VS_SECURITY_AND_DATA_AI_THEME_EVENT_CAP", "case_type": "event_cap_4b_counterexample", "positive_or_counterexample": "counterexample", "best_trigger": "R8L88_C28_DATASOLUTION_2024_STAGE4B_DATA_AI_THEME_CAP", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "Data/AI software theme premium capped quickly and later drew down heavily; theme momentum without retention/contract bridge should route to 4B watch.", "current_profile_verdict": "current_profile_4B_too_late_if_data_AI_theme_premium_not_capped", "price_source": "Songdaiki/stock-web", "notes": "New C28 data/AI software event-cap row; no corporate-action caveat."}
```

### 25.3 trigger rows

```jsonl
{"row_type": "trigger", "trigger_id": "R8L88_C28_HAANSOFT_2024_STAGE2_ACTIONABLE_AI_OFFICE_SOFTWARE", "case_id": "R8L88_C28_HAANSOFT_2024_AI_OFFICE_SOFTWARE_RERATING_POSITIVE", "symbol": "030520", "company_name": "한글과컴퓨터", "round": "R8", "loop": "88", "large_sector_id": "L8_PLATFORM_CONTENT_SW_SECURITY", "canonical_archetype_id": "C28_SOFTWARE_SECURITY_CONTRACT_RETENTION", "fine_archetype_id": "AI_OFFICE_SOFTWARE_CONTRACT_BRIDGE_VS_SECURITY_AND_DATA_AI_THEME_EVENT_CAP", "sector": "AI_office_software", "primary_archetype": "AI_office_software_product_contract_bridge", "loop_objective": "coverage_gap_fill | counterexample_mining | stage2_actionable_bonus_stress_test | 4B_non_price_requirement_stress_test | canonical_archetype_compression", "trigger_type": "Stage2-Actionable", "trigger_date": "2024-01-05", "entry_date": "2024-01-05", "entry_price": 14970.0, "evidence_available_at_that_date": "AI office/software product and contract/revenue leverage proxy; exact as-of source URL pending", "evidence_source": "source_proxy_historical_public_report_proxy", "stage2_evidence_fields": ["AI_office_product", "software_revenue_leverage_proxy", "contract_retention_proxy", "relative_strength_reversal"], "stage3_evidence_fields": ["very_high_MFE30", "very_high_MFE90", "low_initial_MAE"], "stage4b_evidence_fields": ["valuation_repricing_watch_after_fast_peak"], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/030/030520/2024.csv", "profile_path": "atlas/symbol_profiles/030/030520.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": 156.85, "MFE_90D_pct": 156.85, "MFE_180D_pct": 156.85, "MFE_1Y_pct": "not_calculated", "MFE_2Y_pct": "not_calculated", "MAE_30D_pct": -5.68, "MAE_90D_pct": -5.68, "MAE_180D_pct": -5.68, "MAE_1Y_pct": "not_calculated", "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2024-01-22", "peak_price": 38450.0, "drawdown_after_peak_pct": -48.63, "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": null, "four_b_full_window_peak_proximity": null, "four_b_timing_verdict": "positive_stage2_but_later_valuation_watch_needed_after_fast_AI_software_run", "four_b_evidence_type": ["valuation_blowoff", "positioning_overheat"], "four_c_protection_label": "not_applicable", "trigger_outcome_label": "good_stage2_AI_office_software_rerating_success", "current_profile_verdict": "current_profile_kept_but_source_proxy_blocks_positive_delta", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window", "same_entry_group_id": "R8L88_C28_030520_2024-01-05_14970", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false, "evidence_url_pending": true, "source_proxy_only": true}
{"row_type": "trigger", "trigger_id": "R8L88_C28_AHNLAB_2024_STAGE2_FALSE_POSITIVE_SECURITY_QUALITY", "case_id": "R8L88_C28_AHNLAB_2024_SECURITY_QUALITY_FALSE_STAGE2", "symbol": "053800", "company_name": "안랩", "round": "R8", "loop": "88", "large_sector_id": "L8_PLATFORM_CONTENT_SW_SECURITY", "canonical_archetype_id": "C28_SOFTWARE_SECURITY_CONTRACT_RETENTION", "fine_archetype_id": "AI_OFFICE_SOFTWARE_CONTRACT_BRIDGE_VS_SECURITY_AND_DATA_AI_THEME_EVENT_CAP", "sector": "cybersecurity_contract_retention", "primary_archetype": "security_quality_without_contract_revision_bridge", "loop_objective": "coverage_gap_fill | counterexample_mining | stage2_actionable_bonus_stress_test | 4B_non_price_requirement_stress_test | canonical_archetype_compression", "trigger_type": "Stage2-Actionable", "trigger_date": "2024-01-22", "entry_date": "2024-01-22", "entry_price": 72500.0, "evidence_available_at_that_date": "cybersecurity quality / contract-stability proxy; exact as-of source URL pending", "evidence_source": "source_proxy_historical_public_report_proxy", "stage2_evidence_fields": ["security_quality", "contract_stability_proxy", "relative_strength_watch"], "stage3_evidence_fields": [], "stage4b_evidence_fields": ["weak_MFE90", "contract_retention_revision_bridge_missing", "slow_drawdown"], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/053/053800/2024.csv", "profile_path": "atlas/symbol_profiles/053/053800.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": 4.14, "MFE_90D_pct": 4.28, "MFE_180D_pct": 4.28, "MFE_1Y_pct": "not_calculated", "MFE_2Y_pct": "not_calculated", "MAE_30D_pct": -5.52, "MAE_90D_pct": -14.48, "MAE_180D_pct": -22.76, "MAE_1Y_pct": "not_calculated", "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2024-04-12", "peak_price": 75600.0, "drawdown_after_peak_pct": -25.93, "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": 0.04, "four_b_full_window_peak_proximity": 0.04, "four_b_timing_verdict": "weak_MFE_false_stage2_security_quality_without_contract_revision_bridge", "four_b_evidence_type": ["margin_or_backlog_slowdown", "price_only"], "four_c_protection_label": "not_applicable", "trigger_outcome_label": "bad_stage2_security_quality_without_contract_bridge", "current_profile_verdict": "current_profile_false_positive_if_security_quality_counts_without_contract_retention_revision_bridge", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window", "same_entry_group_id": "R8L88_C28_053800_2024-01-22_72500", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false, "evidence_url_pending": true, "source_proxy_only": true}
{"row_type": "trigger", "trigger_id": "R8L88_C28_DATASOLUTION_2024_STAGE4B_DATA_AI_THEME_CAP", "case_id": "R8L88_C28_DATASOLUTION_2024_DATA_AI_THEME_EVENT_CAP_4B", "symbol": "263800", "company_name": "데이타솔루션", "round": "R8", "loop": "88", "large_sector_id": "L8_PLATFORM_CONTENT_SW_SECURITY", "canonical_archetype_id": "C28_SOFTWARE_SECURITY_CONTRACT_RETENTION", "fine_archetype_id": "AI_OFFICE_SOFTWARE_CONTRACT_BRIDGE_VS_SECURITY_AND_DATA_AI_THEME_EVENT_CAP", "sector": "data_AI_software_theme", "primary_archetype": "data_AI_theme_event_cap_4B", "loop_objective": "coverage_gap_fill | counterexample_mining | stage2_actionable_bonus_stress_test | 4B_non_price_requirement_stress_test | canonical_archetype_compression", "trigger_type": "Stage4B", "trigger_date": "2024-04-01", "entry_date": "2024-04-01", "entry_price": 7630.0, "evidence_available_at_that_date": "data/AI software theme premium spike proxy; exact as-of source URL pending", "evidence_source": "source_proxy_historical_public_news_proxy", "stage2_evidence_fields": ["data_AI_theme", "software_theme_premium", "relative_strength_spike"], "stage3_evidence_fields": [], "stage4b_evidence_fields": ["event_premium_cap", "weak_follow_through", "post_peak_drawdown"], "stage4c_evidence_fields": ["thesis_break_watch_only"], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/263/263800/2024.csv", "profile_path": "atlas/symbol_profiles/263/263800.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": 8.78, "MFE_90D_pct": 8.78, "MFE_180D_pct": 8.78, "MFE_1Y_pct": "not_calculated", "MFE_2Y_pct": "not_calculated", "MAE_30D_pct": -15.33, "MAE_90D_pct": -37.55, "MAE_180D_pct": -49.54, "MAE_1Y_pct": "not_calculated", "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2024-04-02", "peak_price": 8300.0, "drawdown_after_peak_pct": -53.61, "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": 1.0, "four_b_full_window_peak_proximity": 1.0, "four_b_timing_verdict": "good_full_window_4B_timing_data_AI_software_theme_event_cap", "four_b_evidence_type": ["valuation_blowoff", "positioning_overheat", "price_only"], "four_c_protection_label": "thesis_break_watch_only", "trigger_outcome_label": "event_cap_4B_success_not_positive_stage_promotion", "current_profile_verdict": "current_profile_4B_too_late_if_data_AI_theme_premium_not_capped", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window", "same_entry_group_id": "R8L88_C28_263800_2024-04-01_7630", "dedupe_for_aggregate": false, "aggregate_group_role": "4B_overlay_only", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false, "evidence_url_pending": true, "source_proxy_only": true}
```

### 25.4 score_simulation rows

```jsonl
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R8L88_C28_HAANSOFT_2024_AI_OFFICE_SOFTWARE_RERATING_POSITIVE", "trigger_id": "R8L88_C28_HAANSOFT_2024_STAGE2_ACTIONABLE_AI_OFFICE_SOFTWARE", "symbol": "030520", "large_sector_id": "L8_PLATFORM_CONTENT_SW_SECURITY", "canonical_archetype_id": "C28_SOFTWARE_SECURITY_CONTRACT_RETENTION", "raw_component_scores_before": {"contract_score": 25, "backlog_visibility_score": 30, "margin_bridge_score": 25, "revision_score": 35, "relative_strength_score": 70, "customer_quality_score": 30, "policy_or_regulatory_score": 0, "valuation_repricing_score": 60, "execution_risk_score": 40, "legal_or_contract_risk_score": 5, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_before": 66, "stage_label_before": "Stage2-Watch", "raw_component_scores_after": {"contract_score": 45, "backlog_visibility_score": 55, "margin_bridge_score": 50, "revision_score": 55, "relative_strength_score": 75, "customer_quality_score": 45, "policy_or_regulatory_score": 0, "valuation_repricing_score": 50, "execution_risk_score": 25, "legal_or_contract_risk_score": 5, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_after": 75, "stage_label_after": "Stage2-Actionable", "changed_components": ["contract_score", "backlog_visibility_score", "margin_bridge_score", "revision_score", "relative_strength_score", "valuation_repricing_score", "execution_risk_score"], "component_delta_explanation": "AI_office_software_contract_bridge_positive", "MFE_90D_pct": 156.85, "MAE_90D_pct": -5.68, "score_return_alignment_label": "AI_office_software_contract_bridge_positive", "current_profile_verdict": "current_profile_kept_but_source_proxy_blocks_positive_delta"}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R8L88_C28_AHNLAB_2024_SECURITY_QUALITY_FALSE_STAGE2", "trigger_id": "R8L88_C28_AHNLAB_2024_STAGE2_FALSE_POSITIVE_SECURITY_QUALITY", "symbol": "053800", "large_sector_id": "L8_PLATFORM_CONTENT_SW_SECURITY", "canonical_archetype_id": "C28_SOFTWARE_SECURITY_CONTRACT_RETENTION", "raw_component_scores_before": {"contract_score": 25, "backlog_visibility_score": 30, "margin_bridge_score": 25, "revision_score": 35, "relative_strength_score": 70, "customer_quality_score": 30, "policy_or_regulatory_score": 0, "valuation_repricing_score": 60, "execution_risk_score": 40, "legal_or_contract_risk_score": 5, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_before": 65, "stage_label_before": "Stage2-Actionable", "raw_component_scores_after": {"contract_score": 10, "backlog_visibility_score": 15, "margin_bridge_score": 5, "revision_score": 10, "relative_strength_score": 30, "customer_quality_score": 20, "policy_or_regulatory_score": 0, "valuation_repricing_score": 35, "execution_risk_score": 80, "legal_or_contract_risk_score": 5, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_after": 55, "stage_label_after": "Stage1/Watch", "changed_components": ["contract_score", "backlog_visibility_score", "margin_bridge_score", "revision_score", "relative_strength_score", "valuation_repricing_score", "execution_risk_score"], "component_delta_explanation": "security_quality_without_contract_bridge_false_stage2", "MFE_90D_pct": 4.28, "MAE_90D_pct": -14.48, "score_return_alignment_label": "security_quality_without_contract_bridge_false_stage2", "current_profile_verdict": "current_profile_false_positive_if_security_quality_counts_without_contract_retention_revision_bridge"}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R8L88_C28_DATASOLUTION_2024_DATA_AI_THEME_EVENT_CAP_4B", "trigger_id": "R8L88_C28_DATASOLUTION_2024_STAGE4B_DATA_AI_THEME_CAP", "symbol": "263800", "large_sector_id": "L8_PLATFORM_CONTENT_SW_SECURITY", "canonical_archetype_id": "C28_SOFTWARE_SECURITY_CONTRACT_RETENTION", "raw_component_scores_before": {"contract_score": 25, "backlog_visibility_score": 30, "margin_bridge_score": 25, "revision_score": 35, "relative_strength_score": 70, "customer_quality_score": 30, "policy_or_regulatory_score": 0, "valuation_repricing_score": 60, "execution_risk_score": 40, "legal_or_contract_risk_score": 5, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_before": 70, "stage_label_before": "Stage3-Yellow-like", "raw_component_scores_after": {"contract_score": 10, "backlog_visibility_score": 15, "margin_bridge_score": 5, "revision_score": 10, "relative_strength_score": 30, "customer_quality_score": 20, "policy_or_regulatory_score": 0, "valuation_repricing_score": 35, "execution_risk_score": 80, "legal_or_contract_risk_score": 5, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_after": 54, "stage_label_after": "Stage4B-watch", "changed_components": ["contract_score", "backlog_visibility_score", "margin_bridge_score", "revision_score", "relative_strength_score", "valuation_repricing_score", "execution_risk_score"], "component_delta_explanation": "data_AI_theme_event_cap_4B_guard", "MFE_90D_pct": 8.78, "MAE_90D_pct": -37.55, "score_return_alignment_label": "data_AI_theme_event_cap_4B_guard", "current_profile_verdict": "current_profile_4B_too_late_if_data_AI_theme_premium_not_capped"}
```

### 25.5 residual_contribution row

```jsonl
{"row_type": "residual_contribution", "round": "R8", "loop": "88", "large_sector_id": "L8_PLATFORM_CONTENT_SW_SECURITY", "canonical_archetype_id": "C28_SOFTWARE_SECURITY_CONTRACT_RETENTION", "fine_archetype_id": "AI_OFFICE_SOFTWARE_CONTRACT_BRIDGE_VS_SECURITY_AND_DATA_AI_THEME_EVENT_CAP", "new_independent_case_count": 3, "reused_case_count": 0, "new_symbol_count": 3, "same_archetype_new_symbol_count": 3, "same_archetype_new_trigger_family_count": 3, "new_trigger_family_count": 3, "positive_case_count": 1, "counterexample_count": 2, "4B_case_count": 1, "4C_case_count": 0, "tested_existing_calibrated_axes": ["stage2_required_bridge", "local_4b_watch_guard", "full_4b_requires_non_price_evidence", "price_only_blowoff_blocks_positive_stage"], "residual_error_types_found": ["AI_office_software_contract_bridge_positive", "security_quality_false_stage2", "data_AI_theme_event_cap_4B"], "loop_contribution_label": "canonical_archetype_rule_candidate", "do_not_propose_new_weight_delta": true, "source_proxy_only_count": 3, "evidence_url_pending_count": 3}
```

### 25.6 narrative_only row

```jsonl
{"row_type":"narrative_only","case_id":"none","symbol":"none","large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C28_SOFTWARE_SECURITY_CONTRACT_RETENTION","reason":"all selected rows have usable 180D stock-web windows; no narrative-only price row required","price_source":"Songdaiki/stock-web","usage":"not_weight_calibration"}
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
- Do not treat schema_rematerialization_only or duplicate_low_value_loop as new evidence.
- Do not apply global deltas unless multiple large_sector_id values support the same direction.
- Prefer sector_specific or canonical_archetype_specific shadow profiles.
- Positive score promotion requires non-price evidence and clean 180D MFE/MAE.
- 4B rows are overlay/risk calibration only.
- 4C rows are thesis-break/protection calibration only.
- price-only rows cannot promote Stage2/Stage3.
- If a v12 MD weakens an already applied axis, log it as residual counterexample rather than immediately reverting.
- Production scoring must not change unless the user explicitly asks for another promotion batch.

### Expected repository tasks

1. Parse case / trigger / score_simulation / shadow_weight / residual_contribution rows.
2. Validate stock-web price source fields.
3. Validate large_sector_id and canonical_archetype_id.
4. Validate novelty and reuse fields.
5. Deduplicate same_entry_group_id and reused cases.
6. Aggregate by large_sector_id and canonical_archetype_id.
7. Update sector_shadow_profile and archetype_shadow_profile only.
8. Preserve global calibrated profile unless explicitly promoted.
9. Report new independent cases, counterexamples, and residual error types.
10. Add tests that duplicate low-value loops cannot change weights.

### Expected output

- Concise implementation summary.
- Rows accepted/rejected.
- New sector/canonical archetype coverage.
- Existing axis strengthened/weakened/kept.
- No investment recommendation language.

## 27. Next Round State

```text
completed_round = R8
completed_loop = 88
next_round = R9
next_loop = 88
round_schedule_status = valid
round_sector_consistency = pass
```

## 28. Source Notes

- Main execution prompt: Songdaiki/stock_agent docs/core/e2r_v12_prompt_round_scheduler_corrected.txt.
- No-repeat index: Songdaiki/stock_agent docs/core/V12_Research_No_Repeat_Index.md.
- Price atlas: Songdaiki/stock-web atlas/manifest.json and per-symbol tradable shards.
- This file contains no investment recommendation and no production scoring change.
