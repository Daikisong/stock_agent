# E2R Stock-Web Historical Calibration / Sector-Archetype Residual Research Round

## 0. Research Metadata

```text
research_session = post_calibrated_sector_archetype_residual_research
mode = historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12
scheduled_round = R8
scheduled_loop = 91
round_schedule_status = valid
round_sector_consistency = pass
large_sector_id = L8_PLATFORM_CONTENT_SW_SECURITY
canonical_archetype_id = C28_SOFTWARE_SECURITY_CONTRACT_RETENTION
fine_archetype_id = NETWORK_SECURITY_ADC_MAINTENANCE_CONTRACT_BRIDGE_VS_SECURITY_RETENTION_FALSE_STAGE2_AND_MSS_THEME_EVENT_CAP
loop_objective = coverage_gap_fill | counterexample_mining | stage2_actionable_bonus_stress_test | 4B_non_price_requirement_stress_test | high_MAE_guardrail | canonical_archetype_compression
output_file = e2r_stock_web_v12_residual_round_R8_loop_91_L8_PLATFORM_CONTENT_SW_SECURITY_C28_SOFTWARE_SECURITY_CONTRACT_RETENTION_research.md
```

This file is the corrected final output for this execution. The scheduler state after R7 loop 91 is R8 / loop 91. This round uses the C28 software/security contract-retention archetype and avoids the R8 loop 88/89/90 symbol sets.

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
high_MAE_guardrail = existing_axis_strengthened
full_4b_requires_non_price_evidence = existing_axis_kept
price_only_blowoff_blocks_positive_stage = existing_axis_kept
hard_4c_thesis_break_routes_to_4c = existing_axis_kept
```

## 2. Round / Large Sector / Canonical Archetype Scope

```text
scheduled_round = R8
scheduled_loop = 91
large_sector_id = L8_PLATFORM_CONTENT_SW_SECURITY
canonical_archetype_id = C28_SOFTWARE_SECURITY_CONTRACT_RETENTION
round_sector_consistency = pass
computed_next_round = R9
computed_next_loop = 91
```

R8 permits L8 platform/content/software/security research. Previous R8 loop 88 used C28 with different symbols, loop 89 used C26, and loop 90 used C27. This loop returns to C28 with fresh non-top-covered symbols.

## 3. Previous Coverage / Duplicate Avoidance Check

No-Repeat hard key used:

```text
canonical_archetype_id + symbol + trigger_type + entry_date
```

No-Repeat snapshot context:

```text
C28_SOFTWARE_SECURITY_CONTRACT_RETENTION = 26 rows / 19 symbols / good-bad Stage2 10-4 / 4B-4C 0-0
top covered symbols include 058970(3), 150900(3), 042510(2), 203650(2), 307950(2), 012510(1)
previous R8 loop-88 C28 symbols avoided: 030520, 053800, 263800
previous R8 loop-89 C26 symbols avoided: 067160, 216050, 273060
previous R8 loop-90 C27 symbols avoided: 419530, 408900, 417180
previous R7 loop-91 C25 symbols avoided: 206640, 043150, 246710
```

Selected rows avoid hard duplicates and top repeated C28 symbols:

```text
170790 / Stage2-Actionable / 2024-01-24
136540 / Stage2-Actionable / 2024-06-25
356890 / Stage4B / 2024-06-04
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
| 170790 | atlas/symbol_profiles/170/170790.json | selected 2024 window clean after old 2015 CA |
| 136540 | atlas/symbol_profiles/136/136540.json | no corporate-action candidate |
| 356890 | atlas/symbol_profiles/356/356890.json | selected post-2024-05-07 CA window |

## 5. Historical Eligibility Gate

| case_id | symbol | entry_date | entry in shard | forward 180D | OHLC valid | CA clean | calibration_usable |
|---|---|---:|---|---:|---|---|---|
| R8L91_C28_PIOLINK_2024_NETWORK_SECURITY_ADC_MAINTENANCE_CONTRACT_POSITIVE | 170790 | 2024-01-24 | yes | 180 | yes | yes | true |
| R8L91_C28_WINS_2024_SECURITY_RETENTION_FALSE_STAGE2 | 136540 | 2024-06-25 | yes | 180 | yes | yes | true |
| R8L91_C28_CYBERONE_2024_MSS_SECURITY_THEME_EVENT_CAP_4B | 356890 | 2024-06-04 | yes | 180 | yes | post-CA | true |

## 6. Canonical Archetype Compression Map

| canonical | fine/deep split | meaning |
|---|---|---|
| C28_SOFTWARE_SECURITY_CONTRACT_RETENTION | NETWORK_SECURITY_ADC_MAINTENANCE_CONTRACT_BRIDGE | Positive Stage2 requires recurring maintenance, renewal, retention, enterprise/public-sector order, margin, and revision bridge. |
| C28_SOFTWARE_SECURITY_CONTRACT_RETENTION | SECURITY_RETENTION_FALSE_STAGE2 | Security-retention label without recurring contract/margin bridge can become false Stage2. |
| C28_SOFTWARE_SECURITY_CONTRACT_RETENTION | MSS_SECURITY_THEME_EVENT_CAP_4B | Managed-security theme premium should route to 4B when recurring contract bridge is missing. |

## 7. Case Selection Summary

| case_id | symbol | company | role | selected reason |
|---|---|---|---|---|
| R8L91_C28_PIOLINK_2024_NETWORK_SECURITY_ADC_MAINTENANCE_CONTRACT_POSITIVE | 170790 | 파이오링크 | positive | Network-security ADC / maintenance-contract bridge produced high MFE before later reset. |
| R8L91_C28_WINS_2024_SECURITY_RETENTION_FALSE_STAGE2 | 136540 | 윈스테크넷 | counterexample | Security-retention spike had limited forward MFE and later drawdown. |
| R8L91_C28_CYBERONE_2024_MSS_SECURITY_THEME_EVENT_CAP_4B | 356890 | 싸이버원 | counterexample / 4B | Managed-security theme premium capped around the post-CA June spike. |

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
| Piolink network-security ADC contract bridge | historical public/report proxy | true | true | shadow-only positive |
| Wins security retention false Stage2 | historical public/report proxy | true | true | false-Stage2 guardrail |
| CyberOne MSS theme cap | historical public/news proxy | true | true | 4B overlay counterexample |

## 10. Price Data Source Map

| symbol | shard | profile |
|---|---|---|
| 170790 | atlas/ohlcv_tradable_by_symbol_year/170/170790/2024.csv | atlas/symbol_profiles/170/170790.json |
| 136540 | atlas/ohlcv_tradable_by_symbol_year/136/136540/2024.csv | atlas/symbol_profiles/136/136540.json |
| 356890 | atlas/ohlcv_tradable_by_symbol_year/356/356890/2024.csv | atlas/symbol_profiles/356/356890.json |

## 11. Case-by-Case Trigger Grid

| trigger_id | symbol | trigger_type | entry_date | entry_price | role | verdict |
|---|---|---|---:|---:|---|---|
| R8L91_C28_PIOLINK_2024_STAGE2_ACTIONABLE_NETWORK_SECURITY_ADC_CONTRACT_BRIDGE | 170790 | Stage2-Actionable | 2024-01-24 | 11420 | positive | network-security maintenance/contract bridge worked |
| R8L91_C28_WINS_2024_STAGE2_FALSE_POSITIVE_SECURITY_RETENTION_SPIKE | 136540 | Stage2-Actionable | 2024-06-25 | 14720 | counterexample | security retention false Stage2 |
| R8L91_C28_CYBERONE_2024_STAGE4B_MSS_SECURITY_THEME_EVENT_CAP | 356890 | Stage4B | 2024-06-04 | 3695 | counterexample/4B | MSS security theme event cap |

## 12. Trigger-Level OHLC Backtest Tables

| trigger_id | entry | MFE30 | MAE30 | MFE90 | MAE90 | MFE180 | MAE180 | peak_date | peak_price | drawdown_after_peak |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| R8L91_C28_PIOLINK_2024_STAGE2_ACTIONABLE_NETWORK_SECURITY_ADC_CONTRACT_BRIDGE | 11420 | 16.90 | -7.79 | 33.10 | -7.79 | 33.10 | -20.49 | 2024-05-07 | 15200 | -40.13 |
| R8L91_C28_WINS_2024_STAGE2_FALSE_POSITIVE_SECURITY_RETENTION_SPIKE | 14720 | 1.56 | -9.10 | 1.56 | -15.96 | 6.99 | -18.68 | 2024-06-28 | 14950 | -19.93 |
| R8L91_C28_CYBERONE_2024_STAGE4B_MSS_SECURITY_THEME_EVENT_CAP | 3695 | 17.19 | -9.47 | 17.19 | -27.74 | 17.19 | -27.74 | 2024-06-04 | 4330 | -38.34 |

## 13. Current Calibrated Profile Stress Test

| axis | outcome |
|---|---|
| stage2_required_bridge | strengthen: C28 Stage2 needs recurring contract / retention / maintenance / margin / revision bridge |
| local_4b_watch_guard | strengthen: security-service and MSS theme premiums should route to 4B watch when bridge is missing |
| high_MAE_guardrail | strengthen: high-MAE security theme rows cannot promote without durable contract bridge |
| full_4b_requires_non_price_evidence | keep |
| price_only_blowoff_blocks_positive_stage | keep |
| hard_4c_thesis_break_routes_to_4c | keep; no hard 4C promoted |

## 14. Stage2 / Yellow / Green Comparison

No confirmed Stage3-Green row is introduced. The useful split is contract-retention bridge quality:

| symbol | stage quality | explanation |
|---|---|---|
| 170790 | good_stage2 | Network-security contract/maintenance bridge produced high 90D MFE. |
| 136540 | bad_stage2 | Security retention spike had limited MFE and lacked contract/margin bridge. |
| 356890 | good_4B | MSS/security-service premium capped near the post-CA event spike. |

```text
green_lateness_ratio = not_applicable
reason = no confirmed Stage3-Green trigger
```

## 15. 4B Local vs Full-window Timing Audit

| trigger | local proximity | full-window proximity | timing verdict |
|---|---:|---:|---|
| 136540 security retention false Stage2 | 0.98 | 0.93 | false Stage2 due missing contract/margin bridge |
| 356890 MSS security cap | 1.00 | 1.00 | good full-window 4B timing |
| 170790 network security bridge | n/a | n/a | positive Stage2, but later security-contract valuation watch required |

## 16. 4C Protection Audit

```text
4C_case_count = 0
four_c_protection_label = thesis_break_watch_only for 136540 / 356890
```

No hard 4C candidate is proposed. R8 loop 91 is about Stage2 bridge quality and 4B event-cap timing.

## 17. Sector-Specific Rule Candidate

```text
sector_specific_rule_candidate = true
rule_scope = sector_specific
rule = In L8 software/security contract-retention cases, Stage2 requires verified recurring contract, renewal/retention, enterprise/public-sector order, maintenance revenue, channel backlog, margin, or revision bridge. Security, MSS, software, cloud, ADC, or retention label alone remains watch/4B.
proposal_status = shadow_only
```

## 18. Canonical-Archetype Rule Candidate

```text
canonical_archetype_rule_candidate = true
canonical_archetype_id = C28_SOFTWARE_SECURITY_CONTRACT_RETENTION
rule = C28 should split true recurring-contract retention positives from security-retention false Stage2 and managed-security event caps. Event-cap rows are 4B overlay/risk calibration, not Stage3-Green promotion evidence.
proposal_status = shadow_only_not_production
```

## 19. Before / After Backtest Comparison

| profile | hypothesis | eligible triggers | avg_MFE90 | avg_MAE90 | false_positive_rate | verdict |
|---|---|---:|---:|---:|---:|---|
| P0 e2r_2_1_stock_web_calibrated_proxy | current profile | 3 | 17.28 | -17.16 | 0.67 | mixed; C28 bridge split needed |
| P0b e2r_2_0_baseline_reference | older baseline | 3 | 17.28 | -17.16 | 0.67 | weaker bridge/event-cap guard |
| P1 sector_specific_candidate_profile | L8 recurring security contract bridge required | 2 | 17.33 | -11.88 | 0.50 | better |
| P2 canonical_archetype_candidate_profile | C28 bridge vs event-cap split | 2 | 17.33 | -11.88 | 0.50 | best explanatory fit |
| P3 counterexample_guard_profile | reject bridge-missing security themes as positive | 1 | 33.10 | -7.79 | 0.00 | safest but source-proxy blockers remain |

## 20. Score-Return Alignment Matrix

| trigger | score before | stage before | score after | stage after | MFE90 | MAE90 | alignment |
|---|---:|---|---:|---|---:|---:|---|
| 170790 network-security bridge | 66 | Stage2-Watch | 74 | Stage2-Actionable | 33.10 | -7.79 | network_security_ADC_contract_bridge_positive |
| 136540 security retention false | 66 | Stage2-Actionable | 53 | Stage1/Watch | 1.56 | -15.96 | security_retention_false_stage2 |
| 356890 MSS security cap | 70 | Stage3-Yellow-like | 54 | Stage4B-watch | 17.19 | -27.74 | MSS_security_theme_event_cap_4B_guard |

## 21. Coverage Matrix

```jsonl
{"row_type": "coverage_matrix", "large_sector_id": "L8_PLATFORM_CONTENT_SW_SECURITY", "canonical_archetype_id": "C28_SOFTWARE_SECURITY_CONTRACT_RETENTION", "fine_archetype_id": "NETWORK_SECURITY_ADC_MAINTENANCE_CONTRACT_BRIDGE_VS_SECURITY_RETENTION_FALSE_STAGE2_AND_MSS_THEME_EVENT_CAP", "positive_case_count": 1, "counterexample_count": 2, "4B_case_count": 1, "4C_case_count": 0, "new_independent_case_count": 3, "reused_case_count": 0, "calibration_usable_trigger_count": 3, "representative_trigger_count": 2, "current_profile_error_count": 2, "sector_rule_candidate": true, "canonical_rule_candidate": true, "coverage_gap_after_this_loop": "Adds C28 network-security ADC/maintenance-contract positive, security retention false Stage2, and MSS security-service event-cap 4B split using non-top-covered symbols."}
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
tested_existing_calibrated_axes: stage2_required_bridge, local_4b_watch_guard, high_MAE_guardrail, full_4b_requires_non_price_evidence, price_only_blowoff_blocks_positive_stage
residual_error_types_found: network_security_ADC_contract_bridge_positive, security_retention_false_stage2, MSS_security_theme_event_cap_4B
new_axis_proposed: null
existing_axis_strengthened: stage2_required_bridge, local_4b_watch_guard, high_MAE_guardrail
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
- C28 software/security contract-retention bridge vs event-cap split
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
shadow_weight,stage2_required_bridge,canonical_archetype,L8_PLATFORM_CONTENT_SW_SECURITY,C28_SOFTWARE_SECURITY_CONTRACT_RETENTION,configured,C28_requires_recurring_contract_retention_margin_revision_bridge,0,"C28 Stage2 should require recurring contract, renewal/retention, enterprise/public-sector order, channel backlog, maintenance revenue, margin, or revision bridge, not software/security label alone","Piolink positive worked; Wins and CyberOne theme/event rows failed positive-stage promotion","R8L91_C28_PIOLINK_2024_STAGE2_ACTIONABLE_NETWORK_SECURITY_ADC_CONTRACT_BRIDGE|R8L91_C28_WINS_2024_STAGE2_FALSE_POSITIVE_SECURITY_RETENTION_SPIKE|R8L91_C28_CYBERONE_2024_STAGE4B_MSS_SECURITY_THEME_EVENT_CAP",3,3,2,low,canonical_shadow_only,"do_not_propose_new_weight_delta=true because source-proxy/evidence-url-pending rows remain"
shadow_weight,local_4b_watch_guard,canonical_archetype,L8_PLATFORM_CONTENT_SW_SECURITY,C28_SOFTWARE_SECURITY_CONTRACT_RETENTION,configured,cap_MSS_security_service_and_retention_theme_premiums_as_4B_watch,0,"Security-service and retention theme premiums can peak before recurring contract/retention evidence is proven","Wins had limited forward MFE after retention spike; CyberOne showed full-window event-cap behavior after post-CA June spike","R8L91_C28_WINS_2024_STAGE2_FALSE_POSITIVE_SECURITY_RETENTION_SPIKE|R8L91_C28_CYBERONE_2024_STAGE4B_MSS_SECURITY_THEME_EVENT_CAP",2,2,2,medium,guardrail_shadow_only,"4B overlay only; not production"
shadow_weight,high_MAE_guardrail,canonical_archetype,L8_PLATFORM_CONTENT_SW_SECURITY,C28_SOFTWARE_SECURITY_CONTRACT_RETENTION,configured,block_positive_stage_when_security_theme_has_high_MAE_without_contract_bridge,0,"High or persistent MAE after a security/software theme entry should block Stage2/Stage3 promotion unless contract-retention and margin evidence survives","CyberOne MAE90=-27.74 and Wins had weak MFE with persistent drawdown","R8L91_C28_WINS_2024_STAGE2_FALSE_POSITIVE_SECURITY_RETENTION_SPIKE|R8L91_C28_CYBERONE_2024_STAGE4B_MSS_SECURITY_THEME_EVENT_CAP",2,2,2,medium,guardrail_shadow_only,"canonical shadow profile only"
```

## 25. Machine-Readable Rows

### 25.1 price_source_validation

```jsonl
{"row_type": "price_source_validation", "source": "Songdaiki/stock-web", "source_url": "https://github.com/Songdaiki/stock-web", "manifest_path": "atlas/manifest.json", "schema_path": "atlas/schema.json", "universe_path": "atlas/universe/all_symbols.csv", "manifest_max_date": "2026-02-20", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "raw_shard_root": "atlas/ohlcv_raw_by_symbol_year", "validation_status": "usable_for_historical_calibration", "source_name": "FinanceData/marcap", "tradable_row_count": 14354401, "raw_row_count": 15214118, "symbol_count": 5414, "active_like_symbol_count": 2868, "inactive_or_delisted_like_symbol_count": 2546}
```

### 25.2 case rows

```jsonl
{"row_type": "case", "case_id": "R8L91_C28_PIOLINK_2024_NETWORK_SECURITY_ADC_MAINTENANCE_CONTRACT_POSITIVE", "symbol": "170790", "company_name": "파이오링크", "round": "R8", "loop": "91", "large_sector_id": "L8_PLATFORM_CONTENT_SW_SECURITY", "canonical_archetype_id": "C28_SOFTWARE_SECURITY_CONTRACT_RETENTION", "fine_archetype_id": "NETWORK_SECURITY_ADC_MAINTENANCE_CONTRACT_BRIDGE_VS_SECURITY_RETENTION_FALSE_STAGE2_AND_MSS_THEME_EVENT_CAP", "case_type": "structural_success_with_later_watch", "positive_or_counterexample": "positive", "best_trigger": "R8L91_C28_PIOLINK_2024_STAGE2_ACTIONABLE_NETWORK_SECURITY_ADC_CONTRACT_BRIDGE", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "Network security / ADC / cloud-security maintenance-contract bridge produced high 30D/90D MFE before later valuation reset. C28 works when appliance/project revenue is supported by recurring maintenance, retention, channel order, and margin/revision bridge.", "current_profile_verdict": "current_profile_kept_but_C28_positive_requires_recurring_contract_retention_margin_revision_bridge_not_security_label_only", "price_source": "Songdaiki/stock-web", "notes": "Selected 2024 window clean after old 2015 CA candidate. Source-proxy only, so no production weight delta."}
{"row_type": "case", "case_id": "R8L91_C28_WINS_2024_SECURITY_RETENTION_FALSE_STAGE2", "symbol": "136540", "company_name": "윈스테크넷", "round": "R8", "loop": "91", "large_sector_id": "L8_PLATFORM_CONTENT_SW_SECURITY", "canonical_archetype_id": "C28_SOFTWARE_SECURITY_CONTRACT_RETENTION", "fine_archetype_id": "NETWORK_SECURITY_ADC_MAINTENANCE_CONTRACT_BRIDGE_VS_SECURITY_RETENTION_FALSE_STAGE2_AND_MSS_THEME_EVENT_CAP", "case_type": "failed_rerating_retention_bridge_missing", "positive_or_counterexample": "counterexample", "best_trigger": "R8L91_C28_WINS_2024_STAGE2_FALSE_POSITIVE_SECURITY_RETENTION_SPIKE", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "Security appliance / maintenance-retention spike had very limited forward MFE and later persistent drawdown. C28 Stage2 should not be awarded without contract renewal, ARR/retention, public-sector/enterprise order, and margin/revision bridge.", "current_profile_verdict": "current_profile_false_positive_if_security_retention_theme_counts_without_contract_margin_revision_bridge", "price_source": "Songdaiki/stock-web", "notes": "No corporate-action caveat in profile. Source-proxy only."}
{"row_type": "case", "case_id": "R8L91_C28_CYBERONE_2024_MSS_SECURITY_THEME_EVENT_CAP_4B", "symbol": "356890", "company_name": "싸이버원", "round": "R8", "loop": "91", "large_sector_id": "L8_PLATFORM_CONTENT_SW_SECURITY", "canonical_archetype_id": "C28_SOFTWARE_SECURITY_CONTRACT_RETENTION", "fine_archetype_id": "NETWORK_SECURITY_ADC_MAINTENANCE_CONTRACT_BRIDGE_VS_SECURITY_RETENTION_FALSE_STAGE2_AND_MSS_THEME_EVENT_CAP", "case_type": "event_cap_4b_counterexample", "positive_or_counterexample": "counterexample", "best_trigger": "R8L91_C28_CYBERONE_2024_STAGE4B_MSS_SECURITY_THEME_EVENT_CAP", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "Managed security / security-service theme premium capped near the post-CA June spike and then drew down deeply. C28 should route bridge-missing security-service event premiums to 4B unless renewal, recurring contract, margin, and retention bridge remain visible.", "current_profile_verdict": "current_profile_4B_too_late_if_MSS_security_theme_premium_not_capped", "price_source": "Songdaiki/stock-web", "notes": "Selected post-2024-05-07 corporate-action window only. Source-proxy only."}
```

### 25.3 trigger rows

```jsonl
{"row_type": "trigger", "trigger_id": "R8L91_C28_PIOLINK_2024_STAGE2_ACTIONABLE_NETWORK_SECURITY_ADC_CONTRACT_BRIDGE", "case_id": "R8L91_C28_PIOLINK_2024_NETWORK_SECURITY_ADC_MAINTENANCE_CONTRACT_POSITIVE", "symbol": "170790", "company_name": "파이오링크", "round": "R8", "loop": "91", "large_sector_id": "L8_PLATFORM_CONTENT_SW_SECURITY", "canonical_archetype_id": "C28_SOFTWARE_SECURITY_CONTRACT_RETENTION", "fine_archetype_id": "NETWORK_SECURITY_ADC_MAINTENANCE_CONTRACT_BRIDGE_VS_SECURITY_RETENTION_FALSE_STAGE2_AND_MSS_THEME_EVENT_CAP", "sector": "network_security_ADC_cloud_contract", "primary_archetype": "network_security_ADC_maintenance_retention_margin_bridge", "loop_objective": "coverage_gap_fill | counterexample_mining | stage2_actionable_bonus_stress_test | 4B_non_price_requirement_stress_test | high_MAE_guardrail | canonical_archetype_compression", "trigger_type": "Stage2-Actionable", "trigger_date": "2024-01-24", "entry_date": "2024-01-24", "entry_price": 11420.0, "evidence_available_at_that_date": "network security ADC/cloud security, recurring maintenance, channel order, retention and margin/revision bridge proxy; exact as-of source URL pending", "evidence_source": "source_proxy_historical_public_report_proxy", "stage2_evidence_fields": ["network_security_contract_proxy", "ADC_cloud_security_order_proxy", "maintenance_retention_bridge", "margin_revision_bridge_proxy", "relative_strength_reversal"], "stage3_evidence_fields": ["strong_MFE30", "strong_MFE90", "controlled_MAE90"], "stage4b_evidence_fields": ["valuation_watch_after_security_contract_rerating"], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/170/170790/2024.csv", "profile_path": "atlas/symbol_profiles/170/170790.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": 16.9, "MFE_90D_pct": 33.1, "MFE_180D_pct": 33.1, "MFE_1Y_pct": "not_calculated", "MFE_2Y_pct": "not_calculated", "MAE_30D_pct": -7.79, "MAE_90D_pct": -7.79, "MAE_180D_pct": -20.49, "MAE_1Y_pct": "not_calculated", "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2024-05-07", "peak_price": 15200.0, "drawdown_after_peak_pct": -40.13, "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": null, "four_b_full_window_peak_proximity": null, "four_b_timing_verdict": "positive_stage2_but_later_security_contract_valuation_watch_needed", "four_b_evidence_type": ["valuation_repricing", "positioning_overheat", "security_contract_premium"], "four_c_protection_label": "not_applicable", "trigger_outcome_label": "good_stage2_network_security_ADC_contract_bridge_success", "current_profile_verdict": "current_profile_kept_but_source_proxy_blocks_positive_delta", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window_after_2015_CA", "same_entry_group_id": "R8L91_C28_170790_2024-01-24_11420", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false, "evidence_url_pending": true, "source_proxy_only": true}
{"row_type": "trigger", "trigger_id": "R8L91_C28_WINS_2024_STAGE2_FALSE_POSITIVE_SECURITY_RETENTION_SPIKE", "case_id": "R8L91_C28_WINS_2024_SECURITY_RETENTION_FALSE_STAGE2", "symbol": "136540", "company_name": "윈스테크넷", "round": "R8", "loop": "91", "large_sector_id": "L8_PLATFORM_CONTENT_SW_SECURITY", "canonical_archetype_id": "C28_SOFTWARE_SECURITY_CONTRACT_RETENTION", "fine_archetype_id": "NETWORK_SECURITY_ADC_MAINTENANCE_CONTRACT_BRIDGE_VS_SECURITY_RETENTION_FALSE_STAGE2_AND_MSS_THEME_EVENT_CAP", "sector": "security_appliance_maintenance_retention", "primary_archetype": "security_retention_theme_without_contract_margin_bridge", "loop_objective": "coverage_gap_fill | counterexample_mining | stage2_actionable_bonus_stress_test | 4B_non_price_requirement_stress_test | high_MAE_guardrail | canonical_archetype_compression", "trigger_type": "Stage2-Actionable", "trigger_date": "2024-06-25", "entry_date": "2024-06-25", "entry_price": 14720.0, "evidence_available_at_that_date": "security appliance / maintenance retention and public-sector/enterprise order recovery watch proxy; exact as-of source URL pending", "evidence_source": "source_proxy_historical_public_report_proxy", "stage2_evidence_fields": ["security_retention_theme", "maintenance_contract_watch", "relative_strength_spike"], "stage3_evidence_fields": [], "stage4b_evidence_fields": ["limited_MFE90", "contract_margin_revision_bridge_missing", "post_spike_drawdown"], "stage4c_evidence_fields": ["thesis_break_watch_only"], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/136/136540/2024.csv", "profile_path": "atlas/symbol_profiles/136/136540.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": 1.56, "MFE_90D_pct": 1.56, "MFE_180D_pct": 6.99, "MFE_1Y_pct": "not_calculated", "MFE_2Y_pct": "not_calculated", "MAE_30D_pct": -9.1, "MAE_90D_pct": -15.96, "MAE_180D_pct": -18.68, "MAE_1Y_pct": "not_calculated", "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2024-06-28", "peak_price": 14950.0, "drawdown_after_peak_pct": -19.93, "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": 0.98, "four_b_full_window_peak_proximity": 0.93, "four_b_timing_verdict": "security_retention_spike_was_false_stage2_due_missing_contract_margin_revision_bridge", "four_b_evidence_type": ["security_retention_theme", "positioning_overheat", "contract_bridge_missing"], "four_c_protection_label": "thesis_break_watch_only", "trigger_outcome_label": "bad_stage2_security_retention_theme_without_contract_margin_bridge", "current_profile_verdict": "current_profile_false_positive_if_security_retention_theme_counts_without_contract_margin_revision_bridge", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window", "same_entry_group_id": "R8L91_C28_136540_2024-06-25_14720", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false, "evidence_url_pending": true, "source_proxy_only": true}
{"row_type": "trigger", "trigger_id": "R8L91_C28_CYBERONE_2024_STAGE4B_MSS_SECURITY_THEME_EVENT_CAP", "case_id": "R8L91_C28_CYBERONE_2024_MSS_SECURITY_THEME_EVENT_CAP_4B", "symbol": "356890", "company_name": "싸이버원", "round": "R8", "loop": "91", "large_sector_id": "L8_PLATFORM_CONTENT_SW_SECURITY", "canonical_archetype_id": "C28_SOFTWARE_SECURITY_CONTRACT_RETENTION", "fine_archetype_id": "NETWORK_SECURITY_ADC_MAINTENANCE_CONTRACT_BRIDGE_VS_SECURITY_RETENTION_FALSE_STAGE2_AND_MSS_THEME_EVENT_CAP", "sector": "managed_security_service_theme", "primary_archetype": "MSS_security_theme_event_cap_4B", "loop_objective": "coverage_gap_fill | counterexample_mining | stage2_actionable_bonus_stress_test | 4B_non_price_requirement_stress_test | high_MAE_guardrail | canonical_archetype_compression", "trigger_type": "Stage4B", "trigger_date": "2024-06-04", "entry_date": "2024-06-04", "entry_price": 3695.0, "evidence_available_at_that_date": "managed security service / security operation theme premium after post-CA June spike; exact as-of source URL pending", "evidence_source": "source_proxy_historical_public_news_proxy", "stage2_evidence_fields": ["MSS_security_theme", "security_service_event_premium", "relative_strength_spike"], "stage3_evidence_fields": [], "stage4b_evidence_fields": ["event_premium_cap", "post_peak_drawdown", "retention_contract_bridge_missing"], "stage4c_evidence_fields": ["thesis_break_watch_only"], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/356/356890/2024.csv", "profile_path": "atlas/symbol_profiles/356/356890.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": 17.19, "MFE_90D_pct": 17.19, "MFE_180D_pct": 17.19, "MFE_1Y_pct": "not_calculated", "MFE_2Y_pct": "not_calculated", "MAE_30D_pct": -9.47, "MAE_90D_pct": -27.74, "MAE_180D_pct": -27.74, "MAE_1Y_pct": "not_calculated", "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2024-06-04", "peak_price": 4330.0, "drawdown_after_peak_pct": -38.34, "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": 1.0, "four_b_full_window_peak_proximity": 1.0, "four_b_timing_verdict": "good_full_window_4B_timing_MSS_security_theme_event_cap", "four_b_evidence_type": ["security_service_theme_premium", "positioning_overheat", "price_only"], "four_c_protection_label": "thesis_break_watch_only", "trigger_outcome_label": "event_cap_4B_success_MSS_security_theme_premium", "current_profile_verdict": "current_profile_4B_too_late_if_MSS_security_theme_premium_not_capped", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_post_2024-05-07_CA_window", "same_entry_group_id": "R8L91_C28_356890_2024-06-04_3695", "dedupe_for_aggregate": false, "aggregate_group_role": "4B_overlay_only", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false, "evidence_url_pending": true, "source_proxy_only": true}
```

### 25.4 score_simulation rows

```jsonl
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R8L91_C28_PIOLINK_2024_NETWORK_SECURITY_ADC_MAINTENANCE_CONTRACT_POSITIVE", "trigger_id": "R8L91_C28_PIOLINK_2024_STAGE2_ACTIONABLE_NETWORK_SECURITY_ADC_CONTRACT_BRIDGE", "symbol": "170790", "large_sector_id": "L8_PLATFORM_CONTENT_SW_SECURITY", "canonical_archetype_id": "C28_SOFTWARE_SECURITY_CONTRACT_RETENTION", "raw_component_scores_before": {"contract_score": 35, "backlog_visibility_score": 30, "margin_bridge_score": 30, "revision_score": 30, "relative_strength_score": 70, "customer_quality_score": 35, "policy_or_regulatory_score": 20, "valuation_repricing_score": 55, "execution_risk_score": 50, "legal_or_contract_risk_score": 15, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_before": 66, "stage_label_before": "Stage2-Watch", "raw_component_scores_after": {"contract_score": 55, "backlog_visibility_score": 50, "margin_bridge_score": 50, "revision_score": 45, "relative_strength_score": 60, "customer_quality_score": 45, "policy_or_regulatory_score": 20, "valuation_repricing_score": 50, "execution_risk_score": 35, "legal_or_contract_risk_score": 10, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_after": 74, "stage_label_after": "Stage2-Actionable", "changed_components": ["contract_score", "backlog_visibility_score", "margin_bridge_score", "revision_score", "relative_strength_score", "valuation_repricing_score", "execution_risk_score"], "component_delta_explanation": "network_security_ADC_contract_bridge_positive", "MFE_90D_pct": 33.1, "MAE_90D_pct": -7.79, "score_return_alignment_label": "network_security_ADC_contract_bridge_positive", "current_profile_verdict": "current_profile_kept_but_source_proxy_blocks_positive_delta"}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R8L91_C28_WINS_2024_SECURITY_RETENTION_FALSE_STAGE2", "trigger_id": "R8L91_C28_WINS_2024_STAGE2_FALSE_POSITIVE_SECURITY_RETENTION_SPIKE", "symbol": "136540", "large_sector_id": "L8_PLATFORM_CONTENT_SW_SECURITY", "canonical_archetype_id": "C28_SOFTWARE_SECURITY_CONTRACT_RETENTION", "raw_component_scores_before": {"contract_score": 35, "backlog_visibility_score": 30, "margin_bridge_score": 30, "revision_score": 30, "relative_strength_score": 70, "customer_quality_score": 35, "policy_or_regulatory_score": 20, "valuation_repricing_score": 55, "execution_risk_score": 50, "legal_or_contract_risk_score": 15, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_before": 66, "stage_label_before": "Stage2-Actionable", "raw_component_scores_after": {"contract_score": 10, "backlog_visibility_score": 10, "margin_bridge_score": 5, "revision_score": 5, "relative_strength_score": 20, "customer_quality_score": 10, "policy_or_regulatory_score": 20, "valuation_repricing_score": 25, "execution_risk_score": 85, "legal_or_contract_risk_score": 30, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_after": 53, "stage_label_after": "Stage1/Watch", "changed_components": ["contract_score", "backlog_visibility_score", "margin_bridge_score", "revision_score", "relative_strength_score", "valuation_repricing_score", "execution_risk_score"], "component_delta_explanation": "security_retention_false_stage2", "MFE_90D_pct": 1.56, "MAE_90D_pct": -15.96, "score_return_alignment_label": "security_retention_false_stage2", "current_profile_verdict": "current_profile_false_positive_if_security_retention_theme_counts_without_contract_margin_revision_bridge"}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R8L91_C28_CYBERONE_2024_MSS_SECURITY_THEME_EVENT_CAP_4B", "trigger_id": "R8L91_C28_CYBERONE_2024_STAGE4B_MSS_SECURITY_THEME_EVENT_CAP", "symbol": "356890", "large_sector_id": "L8_PLATFORM_CONTENT_SW_SECURITY", "canonical_archetype_id": "C28_SOFTWARE_SECURITY_CONTRACT_RETENTION", "raw_component_scores_before": {"contract_score": 35, "backlog_visibility_score": 30, "margin_bridge_score": 30, "revision_score": 30, "relative_strength_score": 70, "customer_quality_score": 35, "policy_or_regulatory_score": 20, "valuation_repricing_score": 55, "execution_risk_score": 50, "legal_or_contract_risk_score": 15, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_before": 70, "stage_label_before": "Stage3-Yellow-like", "raw_component_scores_after": {"contract_score": 10, "backlog_visibility_score": 10, "margin_bridge_score": 5, "revision_score": 5, "relative_strength_score": 20, "customer_quality_score": 10, "policy_or_regulatory_score": 20, "valuation_repricing_score": 25, "execution_risk_score": 85, "legal_or_contract_risk_score": 30, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_after": 54, "stage_label_after": "Stage4B-watch", "changed_components": ["contract_score", "backlog_visibility_score", "margin_bridge_score", "revision_score", "relative_strength_score", "valuation_repricing_score", "execution_risk_score"], "component_delta_explanation": "MSS_security_theme_event_cap_4B_guard", "MFE_90D_pct": 17.19, "MAE_90D_pct": -27.74, "score_return_alignment_label": "MSS_security_theme_event_cap_4B_guard", "current_profile_verdict": "current_profile_4B_too_late_if_MSS_security_theme_premium_not_capped"}
```

### 25.5 residual_contribution row

```jsonl
{"row_type": "residual_contribution", "round": "R8", "loop": "91", "large_sector_id": "L8_PLATFORM_CONTENT_SW_SECURITY", "canonical_archetype_id": "C28_SOFTWARE_SECURITY_CONTRACT_RETENTION", "fine_archetype_id": "NETWORK_SECURITY_ADC_MAINTENANCE_CONTRACT_BRIDGE_VS_SECURITY_RETENTION_FALSE_STAGE2_AND_MSS_THEME_EVENT_CAP", "new_independent_case_count": 3, "reused_case_count": 0, "new_symbol_count": 3, "same_archetype_new_symbol_count": 3, "same_archetype_new_trigger_family_count": 3, "new_trigger_family_count": 3, "positive_case_count": 1, "counterexample_count": 2, "4B_case_count": 1, "4C_case_count": 0, "tested_existing_calibrated_axes": ["stage2_required_bridge", "local_4b_watch_guard", "full_4b_requires_non_price_evidence", "price_only_blowoff_blocks_positive_stage", "high_MAE_guardrail"], "residual_error_types_found": ["network_security_ADC_contract_bridge_positive", "security_retention_false_stage2", "MSS_security_theme_event_cap_4B"], "loop_contribution_label": "canonical_archetype_rule_candidate", "do_not_propose_new_weight_delta": true, "source_proxy_only_count": 3, "evidence_url_pending_count": 3}
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
- Do not apply global deltas unless multiple large_sector_id values support the same direction.
- Positive score promotion requires non-price evidence and clean 180D MFE/MAE.
- 4B rows are overlay/risk calibration only.
- 4C rows are thesis-break/protection calibration only.
- False-positive rows should strengthen bridge requirements, not generate positive promotion.
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
10. Add tests that bridge-missing C28 rows cannot promote positive stages.

### Expected output

- Concise implementation summary.
- Rows accepted/rejected.
- New sector/canonical archetype coverage.
- Existing axis strengthened/weakened/kept.
- No investment recommendation language.

## 27. Next Round State

```text
completed_round = R8
completed_loop = 91
next_round = R9
next_loop = 91
round_schedule_status = valid
round_sector_consistency = pass
```

## 28. Source Notes

- Main execution prompt: Songdaiki/stock_agent docs/core/e2r_v12_prompt_round_scheduler_corrected.txt.
- No-repeat index: Songdaiki/stock_agent docs/core/V12_Research_No_Repeat_Index.md.
- Price atlas: Songdaiki/stock-web atlas/manifest.json and per-symbol tradable shards.
- This file contains no investment recommendation and no production scoring change.
