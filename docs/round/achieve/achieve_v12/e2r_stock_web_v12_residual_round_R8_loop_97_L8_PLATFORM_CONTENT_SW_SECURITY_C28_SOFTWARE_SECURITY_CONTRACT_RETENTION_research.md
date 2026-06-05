# E2R Stock-Web Historical Calibration / Sector-Archetype Residual Research Round

## 0. Research Metadata

```text
research_session = post_calibrated_sector_archetype_residual_research
mode = historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12
scheduled_round = R8
scheduled_loop = 97
round_schedule_status = valid
round_sector_consistency = pass
large_sector_id = L8_PLATFORM_CONTENT_SW_SECURITY
canonical_archetype_id = C28_SOFTWARE_SECURITY_CONTRACT_RETENTION
fine_archetype_id = AI_SOFTWARE_LICENSE_CONTRACT_RETENTION_BRIDGE_VS_ENDPOINT_SECURITY_FALSE_STAGE2_AND_NETWORK_SECURITY_GATEWAY_EVENT_CAP
loop_objective = coverage_gap_fill | counterexample_mining | stage2_actionable_bonus_stress_test | 4B_non_price_requirement_stress_test | contract_retention_guardrail | high_MAE_guardrail | canonical_archetype_compression
output_file = e2r_stock_web_v12_residual_round_R8_loop_97_L8_PLATFORM_CONTENT_SW_SECURITY_C28_SOFTWARE_SECURITY_CONTRACT_RETENTION_research.md
```

This file is the corrected final output for this execution. The scheduler state after R7 loop 97 is R8 / loop 97. R8 is the L8 platform/content/software/security round, and this run fills C28 software/security contract-retention rather than repeating the immediately preceding R8 loop 96 C27 content/IP monetization file, R8 loop 95 C26 platform ad-revenue file, or R7 loop 97 C25 medical-device file.

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
contract_retention_guardrail = existing_axis_strengthened
high_MAE_guardrail = existing_axis_strengthened
hard_4c_thesis_break_routes_to_4c = existing_axis_kept
full_4b_requires_non_price_evidence = existing_axis_kept
price_only_blowoff_blocks_positive_stage = existing_axis_kept
```

## 2. Round / Large Sector / Canonical Archetype Scope

```text
scheduled_round = R8
scheduled_loop = 97
large_sector_id = L8_PLATFORM_CONTENT_SW_SECURITY
canonical_archetype_id = C28_SOFTWARE_SECURITY_CONTRACT_RETENTION
round_sector_consistency = pass
computed_next_round = R9
computed_next_loop = 97
```

C28 is a recurring software/security contract-retention archetype. A software, AI, security or zero-trust label is the login screen; the signal becomes usable only when recurring license revenue, ARR/maintenance backlog, enterprise renewal, installed-base retention, margin and revision are visible.

## 3. Previous Coverage / Duplicate Avoidance Check

No-Repeat hard key used:

```text
canonical_archetype_id + symbol + trigger_type + entry_date
```

No-Repeat snapshot context:

```text
C28_SOFTWARE_SECURITY_CONTRACT_RETENTION = 26 rows / 19 symbols / good-bad Stage2 10-4 / 4B-4C 0-0
top covered symbols include 058970(3), 150900(3), 042510(2), 203650(2), 307950(2), 012510(1)
previous R8 loop-94 C28 symbols avoided: 030520, 053800, 434480
previous R8 loop-95 C26 symbols avoided: 214320, 236810, 417860
previous R8 loop-96 C27 symbols avoided: 432430, 048910, 289220
previous R7 loop-97 C25 symbols avoided: 335890, 065510, 294090
```

Selected rows avoid hard duplicates and top repeated C28 symbols:

```text
047560 / Stage2-Actionable / 2024-01-08
263860 / Stage2-Actionable / 2024-01-24
356680 / Stage4B / 2024-03-26
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
| 047560 | atlas/symbol_profiles/047/047560.json | selected 2024 window clean after old 2015 CA candidates |
| 263860 | atlas/symbol_profiles/263/263860.json | selected 2024 window clean after old 2018 CA candidates |
| 356680 | atlas/symbol_profiles/356/356680.json | no corporate-action candidate |

## 5. Historical Eligibility Gate

| case_id | symbol | entry_date | entry in shard | forward 180D | OHLC valid | CA clean | calibration_usable |
|---|---|---:|---|---:|---|---|---|
| R8L97_C28_ESTSOFT_2024_AI_SOFTWARE_LICENSE_CONTRACT_RETENTION_POSITIVE | 047560 | 2024-01-08 | yes | 180 | yes | yes | true |
| R8L97_C28_GENIANS_2024_ENDPOINT_SECURITY_CONTRACT_FALSE_STAGE2 | 263860 | 2024-01-24 | yes | 180 | yes | yes | true |
| R8L97_C28_XGATE_2024_NETWORK_SECURITY_GATEWAY_EVENT_CAP_4B | 356680 | 2024-03-26 | yes | 180 | yes | yes | true |

## 6. Canonical Archetype Compression Map

| canonical | fine/deep split | meaning |
|---|---|---|
| C28_SOFTWARE_SECURITY_CONTRACT_RETENTION | AI_SOFTWARE_LICENSE_CONTRACT_RETENTION_BRIDGE | Positive Stage2 requires recurring license/subscription, ARR usage, enterprise customer retention, operating leverage, margin and revision bridge. |
| C28_SOFTWARE_SECURITY_CONTRACT_RETENTION | ENDPOINT_SECURITY_FALSE_STAGE2 | Endpoint/zero-trust security watch without renewal backlog and ARR retention bridge can become false Stage2. |
| C28_SOFTWARE_SECURITY_CONTRACT_RETENTION | NETWORK_SECURITY_GATEWAY_EVENT_CAP_4B | Network-security gateway event premium should route to 4B when contract/retention and margin bridge are missing. |

## 7. Case Selection Summary

| case_id | symbol | company | role | selected reason |
|---|---|---|---|---|
| R8L97_C28_ESTSOFT_2024_AI_SOFTWARE_LICENSE_CONTRACT_RETENTION_POSITIVE | 047560 | 이스트소프트 | positive | AI software/license-contract retention bridge produced very strong MFE, but later drawdown requires retention-quality and valuation watch. |
| R8L97_C28_GENIANS_2024_ENDPOINT_SECURITY_CONTRACT_FALSE_STAGE2 | 263860 | 지니언스 | counterexample | Endpoint security watch produced tiny MFE and then persistent MAE without ARR/renewal bridge. |
| R8L97_C28_XGATE_2024_NETWORK_SECURITY_GATEWAY_EVENT_CAP_4B | 356680 | 엑스게이트 | counterexample / 4B | Network security gateway event premium capped near the March spike and then de-rated sharply. |

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
| ESTsoft AI software/license contract bridge | historical public/news-report proxy | true | true | shadow-only positive |
| Genians endpoint security false Stage2 | historical public/news proxy | true | true | false-Stage2 guardrail |
| XGATE network security gateway event cap | historical public/news proxy | true | true | 4B overlay counterexample |

## 10. Price Data Source Map

| symbol | shard | profile |
|---|---|---|
| 047560 | atlas/ohlcv_tradable_by_symbol_year/047/047560/2024.csv | atlas/symbol_profiles/047/047560.json |
| 263860 | atlas/ohlcv_tradable_by_symbol_year/263/263860/2024.csv | atlas/symbol_profiles/263/263860.json |
| 356680 | atlas/ohlcv_tradable_by_symbol_year/356/356680/2024.csv | atlas/symbol_profiles/356/356680.json |

## 11. Case-by-Case Trigger Grid

| trigger_id | symbol | trigger_type | entry_date | entry_price | role | verdict |
|---|---|---|---:|---:|---|---|
| R8L97_C28_ESTSOFT_2024_STAGE2_ACTIONABLE_AI_SOFTWARE_LICENSE_CONTRACT_RETENTION_BRIDGE | 047560 | Stage2-Actionable | 2024-01-08 | 25650 | positive | AI software license/contract retention bridge worked, but later 4B watch required |
| R8L97_C28_GENIANS_2024_STAGE2_FALSE_POSITIVE_ENDPOINT_SECURITY_CONTRACT_WATCH | 263860 | Stage2-Actionable | 2024-01-24 | 15550 | counterexample | endpoint security contract false Stage2 |
| R8L97_C28_XGATE_2024_STAGE4B_NETWORK_SECURITY_GATEWAY_EVENT_CAP | 356680 | Stage4B | 2024-03-26 | 6780 | counterexample/4B | network security gateway event cap |

## 12. Trigger-Level OHLC Backtest Tables

| trigger_id | entry | MFE30 | MAE30 | MFE90 | MAE90 | MFE180 | MAE180 | peak_date | peak_price | drawdown_after_peak |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| R8L97_C28_ESTSOFT_2024_STAGE2_ACTIONABLE_AI_SOFTWARE_LICENSE_CONTRACT_RETENTION_BRIDGE | 25650 | 94.15 | -13.84 | 94.15 | -14.81 | 94.15 | -37.19 | 2024-01-29 | 49800 | -67.65 |
| R8L97_C28_GENIANS_2024_STAGE2_FALSE_POSITIVE_ENDPOINT_SECURITY_CONTRACT_WATCH | 15550 | 2.89 | -19.61 | 2.89 | -27.97 | 2.89 | -46.56 | 2024-01-29 | 16000 | -48.06 |
| R8L97_C28_XGATE_2024_STAGE4B_NETWORK_SECURITY_GATEWAY_EVENT_CAP | 6780 | 5.31 | -21.09 | 5.31 | -26.84 | 5.31 | -39.68 | 2024-03-28 | 7140 | -42.72 |

## 13. Current Calibrated Profile Stress Test

| axis | outcome |
|---|---|
| stage2_required_bridge | strengthen: C28 Stage2 needs recurring license / ARR / renewal backlog / retention / margin / revision bridge |
| contract_retention_guardrail | strengthen: software/security labels alone cannot promote positive stage |
| local_4b_watch_guard | strengthen: bridge-missing endpoint and network-security event premiums should route to 4B watch |
| high_MAE_guardrail | strengthen: high-MAE software/security rows cannot promote without durable retention bridge |
| hard_4c_thesis_break_routes_to_4c | keep |
| full_4b_requires_non_price_evidence | keep |
| price_only_blowoff_blocks_positive_stage | keep |

## 14. Stage2 / Yellow / Green / 4B Comparison

No confirmed Stage3-Green row is introduced. The useful split is whether software/security narrative becomes recurring revenue and retention evidence.

| symbol | stage quality | explanation |
|---|---|---|
| 047560 | good_stage2_with_later_watch | AI software license/contract bridge produced strong MFE, but later drawdown makes valuation and retention-quality watch mandatory. |
| 263860 | bad_stage2 | Endpoint security watch lacked renewal backlog/ARR retention bridge and produced low MFE with high MAE. |
| 356680 | good_4B | Network-security event premium capped near the March high and then de-rated. |

```text
green_lateness_ratio = not_applicable
reason = no confirmed Stage3-Green trigger
```

## 15. 4B Local vs Full-window Timing Audit

| trigger | local proximity | full-window proximity | timing verdict |
|---|---:|---:|---|
| 263860 endpoint security false Stage2 | 0.97 | 0.97 | false Stage2 due missing ARR / renewal / retention / margin bridge |
| 356680 network security gateway cap | 0.95 | 0.95 | good full-window 4B timing after network-security event premium |
| 047560 AI software bridge | n/a | n/a | positive Stage2, but later software valuation and retention-quality watch required |

## 16. 4C Protection Audit

```text
4C_case_count = 0
four_c_protection_label = thesis_break_watch_only for 263860 / 356680
```

No hard 4C candidate is introduced in this R8 loop 97 file. The counterexamples are bridge-missing / event-cap rows, not confirmed thesis-break rows.

## 17. Sector-Specific Rule Candidate

```text
sector_specific_rule_candidate = true
rule_scope = sector_specific
rule = In L8 software/security contract-retention cases, Stage2 requires verified recurring license/subscription revenue, ARR or maintenance backlog, enterprise customer retention, renewal contract visibility, installed base, margin, or revision bridge. AI software, security, zero-trust, network gateway, quantum security, software license or relative-strength label alone remains watch/4B.
proposal_status = shadow_only
```

## 18. Canonical-Archetype Rule Candidate

```text
canonical_archetype_rule_candidate = true
canonical_archetype_id = C28_SOFTWARE_SECURITY_CONTRACT_RETENTION
rule = C28 should split true recurring license/ARR/contract-retention positives from endpoint-security false Stage2 and network-security event caps. Event-cap rows are 4B overlay/risk calibration, not Stage3-Green promotion evidence.
proposal_status = shadow_only_not_production
```

## 19. Before / After Backtest Comparison

| profile | hypothesis | eligible triggers | avg_MFE90 | avg_MAE90 | false_positive_or_guardrail_rate | verdict |
|---|---|---:|---:|---:|---:|---|
| P0 e2r_2_1_stock_web_calibrated_proxy | current profile | 3 | 34.12 | -23.21 | 0.67 | mixed; C28 bridge split needed |
| P0b e2r_2_0_baseline_reference | older baseline | 3 | 34.12 | -23.21 | 0.67 | weaker 4B/Stage2 separation |
| P1 sector_specific_candidate_profile | L8 recurring-license/ARR/retention bridge required | 2 | 48.52 | -21.39 | 0.50 | better |
| P2 canonical_archetype_candidate_profile | C28 bridge vs event-cap split | 2 | 48.52 | -21.39 | 0.50 | best explanatory fit |
| P3 counterexample_guard_profile | reject bridge-missing software/security themes as positive | 1 | 94.15 | -14.81 | 0.00 | safest but source-proxy blockers remain |

## 20. Score-Return Alignment Matrix

| trigger | score before | stage before | score after | stage after | MFE90 | MAE90 | alignment |
|---|---:|---|---:|---|---:|---:|---|
| 047560 AI software bridge | 66 | Stage2-Watch | 80 | Stage2-Actionable | 94.15 | -14.81 | AI_software_contract_retention_positive |
| 263860 endpoint false | 66 | Stage2-Actionable | 52 | Stage1/Watch | 2.89 | -27.97 | endpoint_security_contract_false_stage2 |
| 356680 network security cap | 70 | Stage3-Yellow-like | 54 | Stage4B-watch | 5.31 | -26.84 | network_security_gateway_event_cap_4B_guard |

## 21. Coverage Matrix

```jsonl
{"row_type": "coverage_matrix", "large_sector_id": "L8_PLATFORM_CONTENT_SW_SECURITY", "canonical_archetype_id": "C28_SOFTWARE_SECURITY_CONTRACT_RETENTION", "fine_archetype_id": "AI_SOFTWARE_LICENSE_CONTRACT_RETENTION_BRIDGE_VS_ENDPOINT_SECURITY_FALSE_STAGE2_AND_NETWORK_SECURITY_GATEWAY_EVENT_CAP", "positive_case_count": 1, "counterexample_count": 2, "4B_case_count": 1, "4C_case_count": 0, "new_independent_case_count": 3, "reused_case_count": 0, "calibration_usable_trigger_count": 3, "representative_trigger_count": 2, "current_profile_error_count": 2, "sector_rule_candidate": true, "canonical_rule_candidate": true, "coverage_gap_after_this_loop": "Adds C28 ESTsoft AI software license/contract-retention positive, Genians endpoint-security false Stage2, and XGATE network-security gateway event-cap 4B while avoiding top repeated C28 and previous R8/R7 loop symbols."}
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
tested_existing_calibrated_axes: stage2_required_bridge, local_4b_watch_guard, contract_retention_guardrail, high_MAE_guardrail, hard_4c_thesis_break_routes_to_4c, full_4b_requires_non_price_evidence, price_only_blowoff_blocks_positive_stage
residual_error_types_found: AI_software_contract_retention_positive, endpoint_security_contract_false_stage2, network_security_gateway_event_cap_4B
new_axis_proposed: null
existing_axis_strengthened: stage2_required_bridge, local_4b_watch_guard, contract_retention_guardrail, high_MAE_guardrail
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
- C28 software/security contract-retention bridge vs false Stage2 / event-cap split
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
shadow_weight,stage2_required_bridge,canonical_archetype,L8_PLATFORM_CONTENT_SW_SECURITY,C28_SOFTWARE_SECURITY_CONTRACT_RETENTION,configured,C28_requires_recurring_license_ARR_contract_retention_customer_margin_revision_bridge,0,"C28 Stage2 should require recurring license/subscription revenue, ARR or maintenance backlog, enterprise customer retention, renewal contract visibility, installed base, margin, or revision bridge, not software/security/AI/zero-trust label alone","ESTsoft positive worked; Genians and XGATE event/watch rows failed positive-stage promotion","R8L97_C28_ESTSOFT_2024_STAGE2_ACTIONABLE_AI_SOFTWARE_LICENSE_CONTRACT_RETENTION_BRIDGE|R8L97_C28_GENIANS_2024_STAGE2_FALSE_POSITIVE_ENDPOINT_SECURITY_CONTRACT_WATCH|R8L97_C28_XGATE_2024_STAGE4B_NETWORK_SECURITY_GATEWAY_EVENT_CAP",3,3,2,low,canonical_shadow_only,"do_not_propose_new_weight_delta=true because source-proxy/evidence-url-pending rows remain"
shadow_weight,local_4b_watch_guard,canonical_archetype,L8_PLATFORM_CONTENT_SW_SECURITY,C28_SOFTWARE_SECURITY_CONTRACT_RETENTION,configured,cap_bridge_missing_endpoint_and_network_security_event_premiums_as_4B_watch,0,"Endpoint security, zero-trust and network gateway premiums can peak before contract renewal, ARR, installed-base and margin bridge is proven","Genians had low MFE and persistent MAE; XGATE showed event-cap behavior after the March network-security/quantum-security spike","R8L97_C28_GENIANS_2024_STAGE2_FALSE_POSITIVE_ENDPOINT_SECURITY_CONTRACT_WATCH|R8L97_C28_XGATE_2024_STAGE4B_NETWORK_SECURITY_GATEWAY_EVENT_CAP",2,2,2,medium,guardrail_shadow_only,"4B overlay only; not production"
shadow_weight,high_MAE_guardrail,canonical_archetype,L8_PLATFORM_CONTENT_SW_SECURITY,C28_SOFTWARE_SECURITY_CONTRACT_RETENTION,configured,block_positive_stage_when_software_security_theme_has_high_or_persistent_MAE_without_retention_bridge,0,"High or persistent MAE after bridge-missing C28 entries should block Stage2/Stage3 promotion unless license, ARR, renewal retention and margin evidence survives","Genians MAE180=-46.56 and XGATE MAE180=-39.68","R8L97_C28_GENIANS_2024_STAGE2_FALSE_POSITIVE_ENDPOINT_SECURITY_CONTRACT_WATCH|R8L97_C28_XGATE_2024_STAGE4B_NETWORK_SECURITY_GATEWAY_EVENT_CAP",2,2,2,medium,guardrail_shadow_only,"canonical shadow profile only"
```

## 25. Machine-Readable Rows

### 25.1 price_source_validation

```jsonl
{"row_type": "price_source_validation", "source": "Songdaiki/stock-web", "source_url": "https://github.com/Songdaiki/stock-web", "manifest_path": "atlas/manifest.json", "schema_path": "atlas/schema.json", "universe_path": "atlas/universe/all_symbols.csv", "manifest_max_date": "2026-02-20", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "raw_shard_root": "atlas/ohlcv_raw_by_symbol_year", "validation_status": "usable_for_historical_calibration", "source_name": "FinanceData/marcap", "tradable_row_count": 14354401, "raw_row_count": 15214118, "symbol_count": 5414, "active_like_symbol_count": 2868, "inactive_or_delisted_like_symbol_count": 2546}
```

### 25.2 case rows

```jsonl
{"row_type": "case", "case_id": "R8L97_C28_ESTSOFT_2024_AI_SOFTWARE_LICENSE_CONTRACT_RETENTION_POSITIVE", "symbol": "047560", "company_name": "이스트소프트", "round": "R8", "loop": "97", "large_sector_id": "L8_PLATFORM_CONTENT_SW_SECURITY", "canonical_archetype_id": "C28_SOFTWARE_SECURITY_CONTRACT_RETENTION", "fine_archetype_id": "AI_SOFTWARE_LICENSE_CONTRACT_RETENTION_BRIDGE_VS_ENDPOINT_SECURITY_FALSE_STAGE2_AND_NETWORK_SECURITY_GATEWAY_EVENT_CAP", "case_type": "structural_success_with_later_AI_software_valuation_watch", "positive_or_counterexample": "positive", "best_trigger": "R8L97_C28_ESTSOFT_2024_STAGE2_ACTIONABLE_AI_SOFTWARE_LICENSE_CONTRACT_RETENTION_BRIDGE", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "AI software / license-contract retention bridge produced very strong 30D/90D MFE from the January acceleration, but later deep drawdown means C28 positives still need retention-quality and valuation watch. C28 works when software/security narrative maps into recurring license or subscription revenue, enterprise customer retention, renewal backlog, ARR/usage, operating leverage, margin and revision bridge.", "current_profile_verdict": "current_profile_kept_but_C28_positive_requires_recurring_license_retention_enterprise_customer_ARR_margin_revision_bridge_not_AI_software_label_only", "price_source": "Songdaiki/stock-web", "notes": "Selected 2024 window clean after old 2015 corporate-action candidates. Source-proxy only, so no production weight delta."}
{"row_type": "case", "case_id": "R8L97_C28_GENIANS_2024_ENDPOINT_SECURITY_CONTRACT_FALSE_STAGE2", "symbol": "263860", "company_name": "지니언스", "round": "R8", "loop": "97", "large_sector_id": "L8_PLATFORM_CONTENT_SW_SECURITY", "canonical_archetype_id": "C28_SOFTWARE_SECURITY_CONTRACT_RETENTION", "fine_archetype_id": "AI_SOFTWARE_LICENSE_CONTRACT_RETENTION_BRIDGE_VS_ENDPOINT_SECURITY_FALSE_STAGE2_AND_NETWORK_SECURITY_GATEWAY_EVENT_CAP", "case_type": "failed_rerating_endpoint_security_contract_retention_bridge_missing", "positive_or_counterexample": "counterexample", "best_trigger": "R8L97_C28_GENIANS_2024_STAGE2_FALSE_POSITIVE_ENDPOINT_SECURITY_CONTRACT_WATCH", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "Endpoint security / zero-trust contract watch produced only a small forward MFE and then a persistent drawdown. C28 Stage2 should not be awarded without confirmed enterprise contract renewal, ARR/maintenance backlog, retention rate, cross-sell, margin and revision bridge.", "current_profile_verdict": "current_profile_false_positive_if_endpoint_security_watch_counts_without_contract_renewal_ARR_retention_margin_revision_bridge", "price_source": "Songdaiki/stock-web", "notes": "Selected 2024 window clean after old 2018 corporate-action candidates. Source-proxy only."}
{"row_type": "case", "case_id": "R8L97_C28_XGATE_2024_NETWORK_SECURITY_GATEWAY_EVENT_CAP_4B", "symbol": "356680", "company_name": "엑스게이트", "round": "R8", "loop": "97", "large_sector_id": "L8_PLATFORM_CONTENT_SW_SECURITY", "canonical_archetype_id": "C28_SOFTWARE_SECURITY_CONTRACT_RETENTION", "fine_archetype_id": "AI_SOFTWARE_LICENSE_CONTRACT_RETENTION_BRIDGE_VS_ENDPOINT_SECURITY_FALSE_STAGE2_AND_NETWORK_SECURITY_GATEWAY_EVENT_CAP", "case_type": "event_cap_4b_counterexample", "positive_or_counterexample": "counterexample", "best_trigger": "R8L97_C28_XGATE_2024_STAGE4B_NETWORK_SECURITY_GATEWAY_EVENT_CAP", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "Network security / quantum-security gateway event premium capped around the March spike and then de-rated sharply. C28 should route bridge-missing security gateway event premiums to 4B unless government/enterprise contract, renewal backlog, installed base, maintenance ARR, margin and revision bridge remain visible.", "current_profile_verdict": "current_profile_4B_too_late_if_network_security_gateway_event_premium_not_capped", "price_source": "Songdaiki/stock-web", "notes": "No corporate-action candidate in profile. Source-proxy only."}
```

### 25.3 trigger rows

```jsonl
{"row_type": "trigger", "trigger_id": "R8L97_C28_ESTSOFT_2024_STAGE2_ACTIONABLE_AI_SOFTWARE_LICENSE_CONTRACT_RETENTION_BRIDGE", "case_id": "R8L97_C28_ESTSOFT_2024_AI_SOFTWARE_LICENSE_CONTRACT_RETENTION_POSITIVE", "symbol": "047560", "company_name": "이스트소프트", "round": "R8", "loop": "97", "large_sector_id": "L8_PLATFORM_CONTENT_SW_SECURITY", "canonical_archetype_id": "C28_SOFTWARE_SECURITY_CONTRACT_RETENTION", "fine_archetype_id": "AI_SOFTWARE_LICENSE_CONTRACT_RETENTION_BRIDGE_VS_ENDPOINT_SECURITY_FALSE_STAGE2_AND_NETWORK_SECURITY_GATEWAY_EVENT_CAP", "sector": "AI_software_license_subscription_enterprise_contract_retention", "primary_archetype": "recurring_license_retention_enterprise_customer_ARR_margin_revision_bridge", "loop_objective": "coverage_gap_fill | counterexample_mining | stage2_actionable_bonus_stress_test | 4B_non_price_requirement_stress_test | contract_retention_guardrail | high_MAE_guardrail | canonical_archetype_compression", "trigger_type": "Stage2-Actionable", "trigger_date": "2024-01-08", "entry_date": "2024-01-08", "entry_price": 25650.0, "evidence_available_at_that_date": "AI software / license-contract expansion, enterprise customer optionality, recurring license/subscription usage and operating leverage/margin revision bridge proxy after January breakout; exact as-of source URL pending", "evidence_source": "source_proxy_historical_public_news_report_proxy", "stage2_evidence_fields": ["AI_software_license_proxy", "enterprise_customer_retention_proxy", "ARR_subscription_usage_proxy", "operating_leverage_proxy", "margin_revision_bridge_proxy"], "stage3_evidence_fields": ["very_strong_MFE30", "very_strong_MFE90", "later_drawdown_requires_4B_watch"], "stage4b_evidence_fields": ["later_AI_software_valuation_watch", "retention_quality_recheck"], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/047/047560/2024.csv", "profile_path": "atlas/symbol_profiles/047/047560.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": 94.15, "MFE_90D_pct": 94.15, "MFE_180D_pct": 94.15, "MFE_1Y_pct": "not_calculated", "MFE_2Y_pct": "not_calculated", "MAE_30D_pct": -13.84, "MAE_90D_pct": -14.81, "MAE_180D_pct": -37.19, "MAE_1Y_pct": "not_calculated", "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2024-01-29", "peak_price": 49800.0, "drawdown_after_peak_pct": -67.65, "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": null, "four_b_full_window_peak_proximity": null, "four_b_timing_verdict": "positive_stage2_but_later_AI_software_valuation_and_retention_quality_4B_watch_needed", "four_b_evidence_type": ["AI_software_contract_retention_bridge", "ARR_subscription_proxy", "valuation_watch"], "four_c_protection_label": "not_applicable", "trigger_outcome_label": "good_stage2_AI_software_license_contract_retention_bridge_success_with_later_4B_watch", "current_profile_verdict": "current_profile_kept_but_source_proxy_blocks_positive_delta", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window_after_old_2015_CA", "same_entry_group_id": "R8L97_C28_047560_2024-01-08_25650", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false, "evidence_url_pending": true, "source_proxy_only": true}
{"row_type": "trigger", "trigger_id": "R8L97_C28_GENIANS_2024_STAGE2_FALSE_POSITIVE_ENDPOINT_SECURITY_CONTRACT_WATCH", "case_id": "R8L97_C28_GENIANS_2024_ENDPOINT_SECURITY_CONTRACT_FALSE_STAGE2", "symbol": "263860", "company_name": "지니언스", "round": "R8", "loop": "97", "large_sector_id": "L8_PLATFORM_CONTENT_SW_SECURITY", "canonical_archetype_id": "C28_SOFTWARE_SECURITY_CONTRACT_RETENTION", "fine_archetype_id": "AI_SOFTWARE_LICENSE_CONTRACT_RETENTION_BRIDGE_VS_ENDPOINT_SECURITY_FALSE_STAGE2_AND_NETWORK_SECURITY_GATEWAY_EVENT_CAP", "sector": "endpoint_security_zero_trust_contract_retention_watch", "primary_archetype": "endpoint_security_watch_without_contract_renewal_ARR_retention_margin_bridge", "loop_objective": "coverage_gap_fill | counterexample_mining | stage2_actionable_bonus_stress_test | 4B_non_price_requirement_stress_test | contract_retention_guardrail | high_MAE_guardrail | canonical_archetype_compression", "trigger_type": "Stage2-Actionable", "trigger_date": "2024-01-24", "entry_date": "2024-01-24", "entry_price": 15550.0, "evidence_available_at_that_date": "endpoint security / zero-trust contract watch without confirmed enterprise renewal backlog, ARR maintenance, customer retention, cross-sell or margin revision bridge; exact as-of source URL pending", "evidence_source": "source_proxy_historical_public_news_proxy", "stage2_evidence_fields": ["endpoint_security_contract_watch", "zero_trust_theme", "relative_strength_spike"], "stage3_evidence_fields": [], "stage4b_evidence_fields": ["low_MFE90", "persistent_MAE90", "ARR_retention_margin_bridge_missing"], "stage4c_evidence_fields": ["thesis_break_watch_only"], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/263/263860/2024.csv", "profile_path": "atlas/symbol_profiles/263/263860.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": 2.89, "MFE_90D_pct": 2.89, "MFE_180D_pct": 2.89, "MFE_1Y_pct": "not_calculated", "MFE_2Y_pct": "not_calculated", "MAE_30D_pct": -19.61, "MAE_90D_pct": -27.97, "MAE_180D_pct": -46.56, "MAE_1Y_pct": "not_calculated", "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2024-01-29", "peak_price": 16000.0, "drawdown_after_peak_pct": -48.06, "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": 0.97, "four_b_full_window_peak_proximity": 0.97, "four_b_timing_verdict": "endpoint_security_contract_watch_was_false_stage2_due_missing_ARR_retention_margin_revision_bridge", "four_b_evidence_type": ["endpoint_security_contract_premium", "bridge_missing", "low_MFE"], "four_c_protection_label": "thesis_break_watch_only", "trigger_outcome_label": "bad_stage2_endpoint_security_contract_watch_without_retention_margin_bridge", "current_profile_verdict": "current_profile_false_positive_if_endpoint_security_watch_counts_without_contract_renewal_ARR_retention_margin_revision_bridge", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window_after_old_2018_CA", "same_entry_group_id": "R8L97_C28_263860_2024-01-24_15550", "dedupe_for_aggregate": true, "aggregate_group_role": "representative_false_stage2", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false, "evidence_url_pending": true, "source_proxy_only": true}
{"row_type": "trigger", "trigger_id": "R8L97_C28_XGATE_2024_STAGE4B_NETWORK_SECURITY_GATEWAY_EVENT_CAP", "case_id": "R8L97_C28_XGATE_2024_NETWORK_SECURITY_GATEWAY_EVENT_CAP_4B", "symbol": "356680", "company_name": "엑스게이트", "round": "R8", "loop": "97", "large_sector_id": "L8_PLATFORM_CONTENT_SW_SECURITY", "canonical_archetype_id": "C28_SOFTWARE_SECURITY_CONTRACT_RETENTION", "fine_archetype_id": "AI_SOFTWARE_LICENSE_CONTRACT_RETENTION_BRIDGE_VS_ENDPOINT_SECURITY_FALSE_STAGE2_AND_NETWORK_SECURITY_GATEWAY_EVENT_CAP", "sector": "network_security_gateway_quantum_security_event_premium", "primary_archetype": "network_security_gateway_event_cap_4B", "loop_objective": "coverage_gap_fill | counterexample_mining | stage2_actionable_bonus_stress_test | 4B_non_price_requirement_stress_test | contract_retention_guardrail | high_MAE_guardrail | canonical_archetype_compression", "trigger_type": "Stage4B", "trigger_date": "2024-03-26", "entry_date": "2024-03-26", "entry_price": 6780.0, "evidence_available_at_that_date": "network security / gateway / quantum-security event premium without confirmed government or enterprise contract renewal, installed base, ARR maintenance or margin revision bridge; exact as-of source URL pending", "evidence_source": "source_proxy_historical_public_news_proxy", "stage2_evidence_fields": ["network_security_gateway_event", "quantum_security_theme", "relative_strength_spike"], "stage3_evidence_fields": [], "stage4b_evidence_fields": ["event_premium_cap", "low_MFE90", "deep_MAE90", "contract_retention_margin_bridge_recheck"], "stage4c_evidence_fields": ["thesis_break_watch_only"], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/356/356680/2024.csv", "profile_path": "atlas/symbol_profiles/356/356680.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": 5.31, "MFE_90D_pct": 5.31, "MFE_180D_pct": 5.31, "MFE_1Y_pct": "not_calculated", "MFE_2Y_pct": "not_calculated", "MAE_30D_pct": -21.09, "MAE_90D_pct": -26.84, "MAE_180D_pct": -39.68, "MAE_1Y_pct": "not_calculated", "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2024-03-28", "peak_price": 7140.0, "drawdown_after_peak_pct": -42.72, "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": 0.95, "four_b_full_window_peak_proximity": 0.95, "four_b_timing_verdict": "good_full_window_4B_timing_network_security_gateway_event_cap_due_missing_contract_retention_margin_bridge", "four_b_evidence_type": ["network_security_event_premium", "positioning_overheat", "price_only"], "four_c_protection_label": "thesis_break_watch_only", "trigger_outcome_label": "event_cap_4B_success_network_security_gateway_event_premium", "current_profile_verdict": "current_profile_4B_too_late_if_network_security_gateway_event_premium_not_capped", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window_no_CA_candidate", "same_entry_group_id": "R8L97_C28_356680_2024-03-26_6780", "dedupe_for_aggregate": false, "aggregate_group_role": "4B_overlay_only", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false, "evidence_url_pending": true, "source_proxy_only": true}
```

### 25.4 score_simulation rows

```jsonl
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R8L97_C28_ESTSOFT_2024_AI_SOFTWARE_LICENSE_CONTRACT_RETENTION_POSITIVE", "trigger_id": "R8L97_C28_ESTSOFT_2024_STAGE2_ACTIONABLE_AI_SOFTWARE_LICENSE_CONTRACT_RETENTION_BRIDGE", "symbol": "047560", "large_sector_id": "L8_PLATFORM_CONTENT_SW_SECURITY", "canonical_archetype_id": "C28_SOFTWARE_SECURITY_CONTRACT_RETENTION", "raw_component_scores_before": {"contract_score": 25, "backlog_visibility_score": 35, "margin_bridge_score": 35, "revision_score": 35, "relative_strength_score": 75, "customer_quality_score": 40, "policy_or_regulatory_score": 15, "valuation_repricing_score": 60, "execution_risk_score": 55, "legal_or_contract_risk_score": 25, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 5}, "weighted_score_before": 66, "stage_label_before": "Stage2-Watch", "raw_component_scores_after": {"contract_score": 55, "backlog_visibility_score": 60, "margin_bridge_score": 60, "revision_score": 60, "relative_strength_score": 85, "customer_quality_score": 55, "policy_or_regulatory_score": 15, "valuation_repricing_score": 45, "execution_risk_score": 35, "legal_or_contract_risk_score": 20, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_after": 80, "stage_label_after": "Stage2-Actionable", "changed_components": ["contract_score", "backlog_visibility_score", "margin_bridge_score", "revision_score", "relative_strength_score", "customer_quality_score", "valuation_repricing_score", "execution_risk_score"], "component_delta_explanation": "AI_software_license_contract_retention_positive", "MFE_90D_pct": 94.15, "MAE_90D_pct": -14.81, "score_return_alignment_label": "AI_software_contract_retention_positive", "current_profile_verdict": "current_profile_kept_but_source_proxy_blocks_positive_delta"}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R8L97_C28_GENIANS_2024_ENDPOINT_SECURITY_CONTRACT_FALSE_STAGE2", "trigger_id": "R8L97_C28_GENIANS_2024_STAGE2_FALSE_POSITIVE_ENDPOINT_SECURITY_CONTRACT_WATCH", "symbol": "263860", "large_sector_id": "L8_PLATFORM_CONTENT_SW_SECURITY", "canonical_archetype_id": "C28_SOFTWARE_SECURITY_CONTRACT_RETENTION", "raw_component_scores_before": {"contract_score": 25, "backlog_visibility_score": 30, "margin_bridge_score": 25, "revision_score": 25, "relative_strength_score": 65, "customer_quality_score": 35, "policy_or_regulatory_score": 20, "valuation_repricing_score": 55, "execution_risk_score": 60, "legal_or_contract_risk_score": 30, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 5}, "weighted_score_before": 66, "stage_label_before": "Stage2-Actionable", "raw_component_scores_after": {"contract_score": 5, "backlog_visibility_score": 5, "margin_bridge_score": 5, "revision_score": 5, "relative_strength_score": 20, "customer_quality_score": 10, "policy_or_regulatory_score": 10, "valuation_repricing_score": 25, "execution_risk_score": 90, "legal_or_contract_risk_score": 50, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 10}, "weighted_score_after": 52, "stage_label_after": "Stage1/Watch", "changed_components": ["contract_score", "backlog_visibility_score", "margin_bridge_score", "revision_score", "relative_strength_score", "valuation_repricing_score", "execution_risk_score"], "component_delta_explanation": "endpoint_security_contract_false_stage2", "MFE_90D_pct": 2.89, "MAE_90D_pct": -27.97, "score_return_alignment_label": "endpoint_security_contract_false_stage2", "current_profile_verdict": "current_profile_false_positive_if_endpoint_security_watch_counts_without_contract_renewal_ARR_retention_margin_revision_bridge"}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R8L97_C28_XGATE_2024_NETWORK_SECURITY_GATEWAY_EVENT_CAP_4B", "trigger_id": "R8L97_C28_XGATE_2024_STAGE4B_NETWORK_SECURITY_GATEWAY_EVENT_CAP", "symbol": "356680", "large_sector_id": "L8_PLATFORM_CONTENT_SW_SECURITY", "canonical_archetype_id": "C28_SOFTWARE_SECURITY_CONTRACT_RETENTION", "raw_component_scores_before": {"contract_score": 15, "backlog_visibility_score": 20, "margin_bridge_score": 20, "revision_score": 20, "relative_strength_score": 70, "customer_quality_score": 25, "policy_or_regulatory_score": 25, "valuation_repricing_score": 60, "execution_risk_score": 60, "legal_or_contract_risk_score": 40, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 5}, "weighted_score_before": 70, "stage_label_before": "Stage3-Yellow-like", "raw_component_scores_after": {"contract_score": 5, "backlog_visibility_score": 5, "margin_bridge_score": 0, "revision_score": 5, "relative_strength_score": 20, "customer_quality_score": 5, "policy_or_regulatory_score": 10, "valuation_repricing_score": 25, "execution_risk_score": 90, "legal_or_contract_risk_score": 55, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 10}, "weighted_score_after": 54, "stage_label_after": "Stage4B-watch", "changed_components": ["contract_score", "backlog_visibility_score", "margin_bridge_score", "revision_score", "relative_strength_score", "valuation_repricing_score", "execution_risk_score"], "component_delta_explanation": "network_security_gateway_event_cap_4B_guard", "MFE_90D_pct": 5.31, "MAE_90D_pct": -26.84, "score_return_alignment_label": "network_security_gateway_event_cap_4B_guard", "current_profile_verdict": "current_profile_4B_too_late_if_network_security_gateway_event_premium_not_capped"}
```

### 25.5 residual_contribution row

```jsonl
{"row_type": "residual_contribution", "round": "R8", "loop": "97", "large_sector_id": "L8_PLATFORM_CONTENT_SW_SECURITY", "canonical_archetype_id": "C28_SOFTWARE_SECURITY_CONTRACT_RETENTION", "fine_archetype_id": "AI_SOFTWARE_LICENSE_CONTRACT_RETENTION_BRIDGE_VS_ENDPOINT_SECURITY_FALSE_STAGE2_AND_NETWORK_SECURITY_GATEWAY_EVENT_CAP", "new_independent_case_count": 3, "reused_case_count": 0, "new_symbol_count": 3, "same_archetype_new_symbol_count": 3, "same_archetype_new_trigger_family_count": 3, "new_trigger_family_count": 3, "positive_case_count": 1, "counterexample_count": 2, "4B_case_count": 1, "4C_case_count": 0, "tested_existing_calibrated_axes": ["stage2_required_bridge", "local_4b_watch_guard", "contract_retention_guardrail", "full_4b_requires_non_price_evidence", "price_only_blowoff_blocks_positive_stage", "high_MAE_guardrail"], "residual_error_types_found": ["AI_software_contract_retention_positive", "endpoint_security_contract_false_stage2", "network_security_gateway_event_cap_4B"], "loop_contribution_label": "canonical_archetype_rule_candidate", "do_not_propose_new_weight_delta": true, "source_proxy_only_count": 3, "evidence_url_pending_count": 3}
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
- C28 rows need explicit recurring license/subscription revenue, ARR or maintenance backlog, enterprise customer retention, renewal contract visibility, installed base, margin, or revision bridge before positive promotion.
- In C28, bridge-missing software/security event-premium rows with low MFE or high/persistent MAE should route to 4B/watch, not Stage3.
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
10. Add tests that bridge-missing C28 software/security contract-retention rows cannot promote positive stages.

### Expected output

- Concise implementation summary.
- Rows accepted/rejected.
- New sector/canonical archetype coverage.
- Existing axis strengthened/weakened/kept.
- No investment recommendation language.

## 27. Next Round State

```text
completed_round = R8
completed_loop = 97
next_round = R9
next_loop = 97
round_schedule_status = valid
round_sector_consistency = pass
```

## 28. Source Notes

- Main execution prompt: Songdaiki/stock_agent docs/core/e2r_v12_prompt_round_scheduler_corrected.txt.
- No-repeat index: Songdaiki/stock_agent docs/core/V12_Research_No_Repeat_Index.md.
- Price atlas: Songdaiki/stock-web atlas/manifest.json and per-symbol tradable shards.
- This file contains no investment recommendation and no production scoring change.
