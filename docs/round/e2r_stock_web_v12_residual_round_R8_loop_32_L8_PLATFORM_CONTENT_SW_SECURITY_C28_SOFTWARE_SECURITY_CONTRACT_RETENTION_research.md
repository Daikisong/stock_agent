# E2R Stock-Web Historical Calibration / Sector-Archetype Residual Research Round

## 0. Research Metadata

```text
research_session = post_calibrated_sector_archetype_residual_research
mode = historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12
round = R8
loop = 32
large_sector_id = L8_PLATFORM_CONTENT_SW_SECURITY
canonical_archetype_id = C28_SOFTWARE_SECURITY_CONTRACT_RETENTION
fine_archetype_id = ENTERPRISE_ERP_CLOUD_AI_RETENTION; SECURITY_VENDOR_POLITICAL_THEME_FALSE_POSITIVE; REMOTE_SUPPORT_COVID_USAGE_TO_RETENTION_4B
selection_mode = auto_coverage_gap_fill
price_source = Songdaiki/stock-web
price_basis = tradable_raw
price_adjustment_status = raw_unadjusted_marcap
stock_web_manifest_max_date = 2026-02-20
production_scoring_changed = false
shadow_weight_only = true
handoff_prompt_embedded = true
handoff_prompt_executed_now = false
```

This MD is not live candidate research and does not recommend any current stock. It is a historical calibration artifact. The research unit is the residual gap in C28, where a software/security company can look strong on price, AI narrative, or public attention, while the decisive difference is whether recurring contract retention, enterprise conversion, or renewal-quality evidence is actually present.

## 1. Current Calibrated Profile Assumption

The current profile proxy is `e2r_2_1_stock_web_calibrated_proxy`.

```text
stage2_actionable_evidence_bonus = +2.0
stage3_yellow_total_min = 75.0
stage3_green_total_min = 87.0
stage3_green_revision_min = 55.0
stage3_cross_evidence_green_buffer = +1.5
price_only_blowoff_blocks_positive_stage = true
full_4b_requires_non_price_evidence = true
hard_4c_thesis_break_routes_to_4c = true
```

The tested residual question is not whether these global axes are broadly correct. The question is narrower: in C28, should software/security names require a contract-retention proof layer before Green, and should public-attention spikes be capped even when MFE is large?

## 2. Round / Large Sector / Canonical Archetype Scope

| Field | Value |
|---|---|
| round | R8 |
| loop | 32 |
| large_sector_id | L8_PLATFORM_CONTENT_SW_SECURITY |
| canonical_archetype_id | C28_SOFTWARE_SECURITY_CONTRACT_RETENTION |
| fine_archetype_id | ENTERPRISE_ERP_CLOUD_AI_RETENTION; SECURITY_VENDOR_POLITICAL_THEME_FALSE_POSITIVE; REMOTE_SUPPORT_COVID_USAGE_TO_RETENTION_4B |
| loop_objective | coverage_gap_fill; counterexample_mining; 4B_non_price_requirement_stress_test; green_strictness_stress_test; canonical_archetype_compression |
| output | one standalone Markdown research file |

## 3. Previous Coverage / Duplicate Avoidance Check

The previous generated R8 loop covered C27 content/IP global monetization with game/IP and P2E/tokenized thesis-break patterns. This loop deliberately moves to C28 and uses a different evidence grammar: recurring software revenue, enterprise contract-retention, security vendor theme risk, and remote-support usage normalization.

```text
auto_selected_coverage_gap = R8/C28 lacked a focused software/security retention residual file after C27 content/IP coverage.
new_independent_case_count = 3
reused_case_count = 0
new_symbol_count = 3
same_archetype_new_symbol_count = 3
same_archetype_new_trigger_family_count = 3
new_canonical_archetype_count = 1
new_trigger_family_count = 3
minimum_new_independent_case_ratio = 1.00
```

Duplicate gate:

```text
same_symbol_same_trigger_date_research = false
schema_rematerialization_only = false
duplicate_low_value_loop = false
```

## 4. Stock-Web OHLC Input / Price Source Validation

Stock-Web manifest fields checked for this MD:

```text
source_name = FinanceData/marcap
source_repo_url = https://github.com/FinanceData/marcap
price_adjustment_status = raw_unadjusted_marcap
min_date = 1995-05-02
max_date = 2026-02-20
tradable_row_count = 14354401
raw_row_count = 15214118
symbol_count = 5414
active_like_symbol_count = 2868
inactive_or_delisted_like_symbol_count = 2546
markets = KONEX; KOSDAQ; KOSDAQ GLOBAL; KOSPI
calibration_shard_root = atlas/ohlcv_tradable_by_symbol_year
raw_shard_root = atlas/ohlcv_raw_by_symbol_year
schema_path = atlas/schema.json
universe_path = atlas/universe/all_symbols.csv
```

Validated Stock-Web paths used:

| symbol | company_name | tradable shard(s) | profile |
|---|---|---|---|
| 012510 | 더존비즈온 | atlas/ohlcv_tradable_by_symbol_year/012/012510/2024.csv; 2025.csv | atlas/symbol_profiles/012/012510.json |
| 053800 | 안랩 | atlas/ohlcv_tradable_by_symbol_year/053/053800/2022.csv | atlas/symbol_profiles/053/053800.json |
| 131370 | 알서포트 | atlas/ohlcv_tradable_by_symbol_year/131/131370/2020.csv | atlas/symbol_profiles/131/131370.json |

Profile contamination status:

| symbol | corporate_action_candidate_dates | 180D window status |
|---|---:|---|
| 012510 | 2002-04-22; 2006-06-28; 2009-12-09 | clean_180D_window for 2024 triggers |
| 053800 | 2005-03-31 | clean_180D_window for 2022 triggers |
| 131370 | 2014-01-07 | clean_180D_window for 2020 triggers |

## 5. Historical Eligibility Gate

All representative triggers meet the historical eligibility gate.

| case_id | symbol | entry_date | 180D available by manifest max date | OHLCV present | corporate-action contaminated 180D? | calibration_usable |
|---|---:|---:|---:|---:|---:|---:|
| C28-012510-2024-ERP-AI | 012510 | 2024-01-18 | true | true | false | true |
| C28-053800-2022-THEME-GUARD | 053800 | 2022-01-05 | true | true | false | true |
| C28-131370-2020-REMOTE-SUPPORT | 131370 | 2020-02-18 | true | true | false | true |

## 6. Canonical Archetype Compression Map

| fine_archetype_id | canonical_archetype_id | compression reason |
|---|---|---|
| ENTERPRISE_ERP_CLOUD_AI_RETENTION | C28_SOFTWARE_SECURITY_CONTRACT_RETENTION | Enterprise software recurring revenue can deserve Stage2/Yellow when contract usage and revision begin to close. |
| SECURITY_VENDOR_POLITICAL_THEME_FALSE_POSITIVE | C28_SOFTWARE_SECURITY_CONTRACT_RETENTION | Security vendor price strength without security contract or renewal evidence must be capped. |
| REMOTE_SUPPORT_COVID_USAGE_TO_RETENTION_4B | C28_SOFTWARE_SECURITY_CONTRACT_RETENTION | Sudden software usage can work as Stage2, but if retention/margin bridge is not visible, 4B overlay should arrive before Green extrapolation. |

## 7. Case Selection Summary

| case_id | symbol | company_name | case_type | positive_or_counterexample | best_trigger | current_profile_verdict |
|---|---:|---|---|---|---|---|
| C28-012510-2024-ERP-AI | 012510 | 더존비즈온 | structural_success | positive | TR-C28-012510-S2-2024-01-18 | current_profile_correct |
| C28-053800-2022-THEME-GUARD | 053800 | 안랩 | false_positive_green | counterexample | TR-C28-053800-S2-2022-01-05 | current_profile_false_positive |
| C28-131370-2020-REMOTE-SUPPORT | 131370 | 알서포트 | 4B_overlay_success | counterexample | TR-C28-131370-S2-2020-02-18 | current_profile_4B_too_late |

## 8. Positive vs Counterexample Balance

```text
positive_case_count = 1
counterexample_count = 2
4B_case_count = 2
4C_case_count = 0
calibration_usable_case_count = 3
calibration_usable_trigger_count = 6
```

The balance is intentionally asymmetric: C28 does not need more proof that software can re-rate. It needs guardrails for when public attention, AI wording, political association, or temporary usage growth gets mistaken for durable contract retention.

## 9. Evidence Source Map

| trigger_id | evidence timing note | stage2 evidence | stage3 evidence | 4B/4C evidence |
|---|---|---|---|---|
| TR-C28-012510-S2-2024-01-18 | Historical public AI/cloud enterprise-software rerating window. Entry uses same-day close. | public_event_or_disclosure; customer_or_order_quality; relative_strength; early_revision_signal | none at initial S2 | none |
| TR-C28-012510-GREEN-2024-04-29 | Stage3 requires earnings/revision confirmation after initial AI/cloud rerating. | early_revision_signal | confirmed_revision; margin_bridge; financial_visibility; multiple_public_sources | none |
| TR-C28-053800-S2-2022-01-05 | Price strength and public attention did not equal security-contract retention evidence. | relative_strength only | none | valuation_blowoff; positioning_overheat; explicit_event_cap |
| TR-C28-053800-4B-2022-03-23 | Blowoff window; full 4B should not be allowed from price alone, but political/event-premium cap is a non-fundamental risk overlay. | none | none | valuation_blowoff; positioning_overheat; control_premium_or_event_premium |
| TR-C28-131370-S2-2020-02-18 | Remote-support demand shock became visible, but durable enterprise retention was not yet confirmed. | public_event_or_disclosure; capacity_or_volume_route; relative_strength | none | none |
| TR-C28-131370-4B-2020-08-28 | Full-window peak region; usage-to-retention uncertainty plus extreme positioning warrants 4B overlay. | none | none | valuation_blowoff; positioning_overheat; margin_or_backlog_slowdown |

## 10. Price Data Source Map

| symbol | entry basis | stock-web row evidence used | profile evidence used |
|---:|---|---|---|
| 012510 | 2024-01-18 close = 40,800 | 2024 OHLC rows; 2025 continuation rows | profile confirms name, market, dates, available years, and historical corporate-action dates |
| 053800 | 2022-01-05 close = 120,500 | 2022 OHLC rows | profile confirms name, market, dates, available years, and historical corporate-action date |
| 131370 | 2020-02-18 close = 3,200 | 2020 OHLC rows | profile confirms name, market, dates, available years, and historical corporate-action date |

## 11. Case-by-Case Trigger Grid

| trigger_id | case_id | symbol | trigger_type | trigger_date | entry_date | entry_price | evidence summary | dedupe_for_aggregate |
|---|---|---:|---|---:|---:|---:|---|---:|
| TR-C28-012510-S2-2024-01-18 | C28-012510-2024-ERP-AI | 012510 | Stage2-Actionable | 2024-01-18 | 2024-01-18 | 40800 | Enterprise ERP/cloud/AI rerating with early revision and real software revenue base. | true |
| TR-C28-012510-GREEN-2024-04-29 | C28-012510-2024-ERP-AI | 012510 | Stage3-Green | 2024-04-29 | 2024-04-29 | 56000 | Green only after revision/margin bridge becomes more visible. | false |
| TR-C28-053800-S2-2022-01-05 | C28-053800-2022-THEME-GUARD | 053800 | Stage2-Blocked | 2022-01-05 | 2022-01-05 | 120500 | Relative-strength spike without security contract-retention evidence. | true |
| TR-C28-053800-4B-2022-03-23 | C28-053800-2022-THEME-GUARD | 053800 | Stage4B-overlay | 2022-03-23 | 2022-03-23 | 175800 | Blowoff/event-premium overlay. | false |
| TR-C28-131370-S2-2020-02-18 | C28-131370-2020-REMOTE-SUPPORT | 131370 | Stage2-Actionable | 2020-02-18 | 2020-02-18 | 3200 | Remote-support usage shock, but not yet durable retention. | true |
| TR-C28-131370-4B-2020-08-28 | C28-131370-2020-REMOTE-SUPPORT | 131370 | Stage4B-overlay | 2020-08-28 | 2020-08-28 | 19950 | Full-window peak region with retention-normalization risk. | false |

## 12. Trigger-Level OHLC Backtest Tables

Representative trigger rows:

| trigger_id | symbol | entry_price | MFE_30D_pct | MAE_30D_pct | MFE_90D_pct | MAE_90D_pct | MFE_180D_pct | MAE_180D_pct | peak_date | peak_price | drawdown_after_peak_pct | calibration_usable |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| TR-C28-012510-S2-2024-01-18 | 012510 | 40800 | 37.99 | -11.27 | 60.78 | -11.27 | 91.91 | -11.27 | 2024-07-08 | 78300 | -40.68 | true |
| TR-C28-053800-S2-2022-01-05 | 053800 | 120500 | 6.64 | -44.81 | 81.33 | -47.30 | 81.33 | -47.30 | 2022-03-24 | 218500 | -62.93 | true |
| TR-C28-131370-S2-2020-02-18 | 131370 | 3200 | 89.69 | -25.78 | 174.06 | -25.78 | 639.06 | -25.78 | 2020-08-28 | 23650 | -50.53 | true |

Label-comparison / overlay rows:

| trigger_id | symbol | trigger_type | entry_price | MFE_30D_pct | MAE_30D_pct | MFE_90D_pct | MAE_90D_pct | MFE_180D_pct | MAE_180D_pct | use in aggregate? |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|
| TR-C28-012510-GREEN-2024-04-29 | 012510 | Stage3-Green | 56000 | 17.14 | -9.46 | 39.82 | -13.39 | 39.82 | -19.82 | false |
| TR-C28-053800-4B-2022-03-23 | 053800 | Stage4B-overlay | 175800 | 24.29 | -30.77 | 24.29 | -53.92 | 24.29 | -62.93 | false |
| TR-C28-131370-4B-2020-08-28 | 131370 | Stage4B-overlay | 19950 | 18.55 | -18.05 | 18.55 | -41.35 | 18.55 | -41.35 | false |

Notes:

```text
- 1Y/2Y fields are present in machine-readable rows; 30D/90D/180D are the only quantitative weight-calibration windows used in this loop.
- 012510 2Y continuation was checked against 2025 rows and profile latest close, but the shadow rule does not depend on 1Y/2Y.
- 053800 and 131370 are intentionally retained despite high MFE because the residual question is not “did price move?” but “was Green justified by contract-retention evidence?”
```

## 13. Current Calibrated Profile Stress Test

### C28-012510-2024-ERP-AI

The current calibrated profile should accept Stage2-Actionable because price was not the only evidence: the company had an enterprise software revenue base, cloud/AI optionality, and later revision/margin confirmation. The current profile should delay Green until confirmation. This is correct: the early Stage2 entry captured more upside, while Green was later but still not peak-only.

```text
current_profile_verdict = current_profile_correct
existing_axis_tested = stage3_green_revision_min
existing_axis_strengthened = null
existing_axis_weakened = null
```

### C28-053800-2022-THEME-GUARD

The current profile risks a false positive if relative strength or public attention is interpreted as security contract retention. The price path had high MFE, but the 30D MAE was already severe and the move was event-premium-like. C28 needs a specific Green cap: no contract retention / renewal / enterprise security budget evidence means no Green, regardless of MFE.

```text
current_profile_verdict = current_profile_false_positive
existing_axis_strengthened = price_only_blowoff_blocks_positive_stage
new_axis_proposed = c28_contract_retention_required_for_green
```

### C28-131370-2020-REMOTE-SUPPORT

The current profile should allow Stage2 because a real usage shock existed. But the same profile should avoid durable Green extrapolation unless retention, repeat subscription conversion, and margin bridge appear. The 4B overlay should arrive when usage shock becomes a crowded valuation story.

```text
current_profile_verdict = current_profile_4B_too_late
existing_axis_strengthened = full_4b_requires_non_price_evidence
new_axis_proposed = c28_usage_spike_requires_retention_conversion_for_green
```

## 14. Stage2 / Yellow / Green Comparison

| case_id | Stage2 entry | Stage3 Green entry | Stage2 entry_price | Green entry_price | peak after Stage2 | green_lateness_ratio | verdict |
|---|---:|---:|---:|---:|---:|---:|---|
| C28-012510-2024-ERP-AI | 2024-01-18 | 2024-04-29 | 40800 | 56000 | 78300 | 0.405 | Green was somewhat late but still valid; Stage2 was the useful capture. |
| C28-053800-2022-THEME-GUARD | 2022-01-05 | none | 120500 | n/a | 218500 | not_applicable | No confirmed Green trigger; price-only/theme should be blocked. |
| C28-131370-2020-REMOTE-SUPPORT | 2020-02-18 | none | 3200 | n/a | 23650 | not_applicable | Stage2 usage shock worked, but Green required retention conversion that was not available at trigger. |

## 15. 4B Local vs Full-window Timing Audit

| trigger_id | Stage2 entry_price | Stage4B entry_price | local_peak_price | full_window_peak_price | four_b_local_peak_proximity | four_b_full_window_peak_proximity | evidence_type | timing_verdict |
|---|---:|---:|---:|---:|---:|---:|---|---|
| TR-C28-053800-4B-2022-03-23 | 120500 | 175800 | 218500 | 218500 | 0.564 | 0.564 | valuation_blowoff; positioning_overheat; control_premium_or_event_premium | acceptable_overlay_but_not_positive_stage |
| TR-C28-131370-4B-2020-08-28 | 3200 | 19950 | 23650 | 23650 | 0.819 | 0.819 | valuation_blowoff; positioning_overheat; retention_normalization_risk | good_full_window_4B_timing |

C28 4B implication: price-only local peaks should not be used as full exit signals, but when the non-price evidence is “temporary usage surge lacks retention conversion” or “event-premium without contract evidence,” the overlay becomes useful.

## 16. 4C Protection Audit

No hard 4C row is promoted in this loop. The loop uses 4B overlay rows only.

```text
four_c_protection_label = thesis_break_watch_only
hard_4c_success_count = 0
hard_4c_late_count = 0
```

## 17. Sector-Specific Rule Candidate

```text
rule_scope = sector_specific
large_sector_id = L8_PLATFORM_CONTENT_SW_SECURITY
axis = l8_software_security_contract_retention_green_gate
proposal_type = sector_shadow_only
baseline_value = 0
tested_value = +1
confidence = medium_low
```

Rule text:

> In L8 software/security names, Green promotion requires at least one non-price evidence item that ties the narrative to recurring contract retention, enterprise renewal, subscription conversion, or confirmed software margin bridge. Relative strength, AI wording, security brand attention, or temporary usage spike alone can support Stage2-watch/Stage2-actionable but should not promote Green.

Backtest effect in this loop:

```text
positive kept = 012510
false positive capped = 053800
4B earlier = 131370
```

## 18. Canonical-Archetype Rule Candidate

```text
rule_scope = canonical_archetype_specific
canonical_archetype_id = C28_SOFTWARE_SECURITY_CONTRACT_RETENTION
axis = c28_contract_retention_required_for_green
baseline_value = false
tested_value = true
delta = +1 guard
confidence = medium
```

Rule text:

> For C28, Stage3-Green requires confirmed revision/margin plus contract-retention evidence. “Software usage increased,” “AI product launched,” or “security vendor drew attention” is not enough unless it closes into recurring revenue quality.

Counterexample guard profile:

```text
axis = c28_theme_or_usage_spike_green_cap
if relative_strength_score is high but contract_score/backlog_visibility/customer_quality/revision are weak:
    cap_stage_label = Stage2-Actionable or Stage3-Yellow
    block_stage_label = Stage3-Green
```

## 19. Before / After Backtest Comparison

| profile_id | selected representative triggers | avg_MFE_90D_pct | avg_MAE_90D_pct | false_positive_rate | missed_structural_count | late_green_count | score_return_alignment_verdict |
|---|---|---:|---:|---:|---:|---:|---|
| P0 e2r_2_1_stock_web_calibrated_proxy | 012510; 053800; 131370 | 105.39 | -28.12 | 0.33 | 0 | 1 | mixed: high MFE hides severe false-positive/retention risk |
| P0b e2r_2_0_baseline_reference | 012510 late; 053800 likely over-scored; 131370 price-chasing | 105.39 | -28.12 | 0.67 | 1 | 1 | weaker: too sensitive to price/public narrative |
| P1 sector_specific_candidate_profile | 012510 kept; 053800 capped; 131370 4B overlay | 105.39 | -28.12 | 0.00 for Green | 0 | 1 | improved label quality without deleting Stage2 optionality |
| P2 canonical_archetype_candidate_profile | same as P1 but C28 only | 105.39 | -28.12 | 0.00 for Green | 0 | 1 | best scope: C28-specific, not global |
| P3 counterexample_guard_profile | blocks Green if no retention/contract evidence | 60.78 accepted Green-track MFE90 on 012510 | -11.27 accepted Green-track MAE90 | 0.00 | 0 | 1 | strongest precision; may under-capture temporary software blowoffs |

## 20. Score-Return Alignment Matrix

| case_id | raw component drivers before | weighted_score_before | label_before | proposed change | weighted_score_after | label_after | price alignment |
|---|---|---:|---|---|---:|---|---|
| C28-012510-2024-ERP-AI | revision, margin_bridge, customer_quality, relative_strength | 82 | Stage3-Yellow / late Green candidate | add retention-aware positive bridge | 88 | Stage3-Green after confirmation | aligned |
| C28-053800-2022-THEME-GUARD | relative_strength, valuation_repricing only | 78 | false Stage3-Yellow/Green risk | cap if no contract-retention evidence | 64 | Stage2-Blocked / 4B watch | improved |
| C28-131370-2020-REMOTE-SUPPORT | usage shock, relative_strength, no durable conversion | 80 | Stage3-Yellow risk | require subscription/renewal proof for Green; add 4B usage-normalization overlay | 68 | Stage2-Actionable then 4B overlay | improved |

## 21. Coverage Matrix

| large_sector_id | canonical_archetype_id | fine_archetype_id | positive_case_count | counterexample_count | 4B_case_count | 4C_case_count | new_independent_case_count | reused_case_count | calibration_usable_trigger_count | representative_trigger_count | current_profile_error_count | sector_rule_candidate | canonical_rule_candidate | coverage_gap_after_this_loop |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|
| L8_PLATFORM_CONTENT_SW_SECURITY | C28_SOFTWARE_SECURITY_CONTRACT_RETENTION | ENTERPRISE_ERP_CLOUD_AI_RETENTION; SECURITY_VENDOR_POLITICAL_THEME_FALSE_POSITIVE; REMOTE_SUPPORT_COVID_USAGE_TO_RETENTION_4B | 1 | 2 | 2 | 0 | 3 | 0 | 6 | 3 | 3 | true | true | Remaining gap: pure SaaS/security contract-renewal small-cap positive holdout; hard 4C cyber/accounting trust break case. |

## 22. Residual Contribution Summary

```text
new_independent_case_count: 3
reused_case_count: 0
reused_case_ids: []
new_symbol_count: 3
same_archetype_new_symbol_count: 3
same_archetype_new_trigger_family_count: 3
new_canonical_archetype_count: 1
new_fine_archetype_count: 3
new_trigger_family_count: 3
positive_case_count: 1
counterexample_count: 2
current_profile_error_count: 3
tested_existing_calibrated_axes: [stage3_green_revision_min, price_only_blowoff_blocks_positive_stage, full_4b_requires_non_price_evidence, hard_4c_thesis_break_routes_to_4c]
residual_error_types_found: [theme_false_positive_without_contract_retention, usage_spike_green_overpromotion, 4B_late_after_temporary_software_demand]
new_axis_proposed: [c28_contract_retention_required_for_green, c28_theme_or_usage_spike_green_cap, l8_software_security_contract_retention_green_gate]
existing_axis_strengthened: [price_only_blowoff_blocks_positive_stage, full_4b_requires_non_price_evidence, stage3_green_revision_min]
existing_axis_weakened: []
existing_axis_kept: [hard_4c_thesis_break_routes_to_4c]
sector_specific_rule_candidate: true
canonical_archetype_rule_candidate: true
no_new_signal_reason: null
loop_contribution_label: canonical_archetype_rule_candidate
do_not_propose_new_weight_delta: false
auto_selected_coverage_gap: R8/C28 software/security contract-retention gap after C27 content/IP loop
```

## 23. Validation Scope / Non-Validation Scope

Validation scope:

```text
- Historical OHLCV rows from Songdaiki/stock-web tradable shards.
- Entry/peak/MFE/MAE checked on 30D/90D/180D trading windows.
- Corporate-action dates checked from stock-web symbol profiles.
- Current calibrated profile stress-tested as a research proxy.
```

Non-validation scope:

```text
- No current/live candidate scan.
- No investment recommendation.
- No stock_agent src/e2r code inspection.
- No production scoring patch.
- No brokerage/API execution.
- No new price data route discovery.
```

## 24. Shadow Weight Calibration

```csv
row_type,axis,scope,large_sector_id,canonical_archetype_id,baseline_value,tested_value,delta,reason,backtest_effect,trigger_ids,calibration_usable_count,new_independent_case_count,counterexample_count,confidence,proposal_type,notes
shadow_weight,c28_contract_retention_required_for_green,canonical_archetype_specific,L8_PLATFORM_CONTENT_SW_SECURITY,C28_SOFTWARE_SECURITY_CONTRACT_RETENTION,false,true,+1,"C28 Green should require renewal/retention/subscription conversion or confirmed software margin bridge","Kept 012510 after confirmation; capped 053800; forced 4B overlay discipline on 131370","TR-C28-012510-GREEN-2024-04-29|TR-C28-053800-S2-2022-01-05|TR-C28-131370-4B-2020-08-28",3,3,2,medium,archetype_shadow_only,"not production; post-calibrated residual"
shadow_weight,c28_theme_or_usage_spike_green_cap,canonical_archetype_specific,L8_PLATFORM_CONTENT_SW_SECURITY,C28_SOFTWARE_SECURITY_CONTRACT_RETENTION,0,1,+1,"Relative strength plus AI/security/usage story is capped without contract-retention proof","Reduced Green false positives in 053800 and 131370 while preserving Stage2 optionality","TR-C28-053800-S2-2022-01-05|TR-C28-131370-S2-2020-02-18",2,2,2,medium,guard_shadow_only,"not production; applies to label cap not entry deletion"
shadow_weight,l8_software_security_contract_retention_green_gate,sector_specific,L8_PLATFORM_CONTENT_SW_SECURITY,C28_SOFTWARE_SECURITY_CONTRACT_RETENTION,0,1,+1,"L8 software/security rerating quality depends on recurring contract evidence more than public attention","Improved score-return alignment by separating Stage2 usage/theme from Stage3 Green","TR-C28-012510-S2-2024-01-18|TR-C28-053800-S2-2022-01-05|TR-C28-131370-S2-2020-02-18",3,3,2,medium_low,sector_shadow_only,"not production; needs C28 holdout"
```

## 25. Machine-Readable Rows

```jsonl
{"row_type":"price_source_validation","source":"Songdaiki/stock-web","source_url":"https://github.com/Songdaiki/stock-web","manifest_path":"atlas/manifest.json","schema_path":"atlas/schema.json","universe_path":"atlas/universe/all_symbols.csv","manifest_max_date":"2026-02-20","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","calibration_shard_root":"atlas/ohlcv_tradable_by_symbol_year","raw_shard_root":"atlas/ohlcv_raw_by_symbol_year","validation_status":"usable_for_historical_calibration"}
{"row_type":"case","case_id":"C28-012510-2024-ERP-AI","symbol":"012510","company_name":"더존비즈온","round":"R8","loop":"32","large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C28_SOFTWARE_SECURITY_CONTRACT_RETENTION","fine_archetype_id":"ENTERPRISE_ERP_CLOUD_AI_RETENTION","case_type":"structural_success","positive_or_counterexample":"positive","best_trigger":"TR-C28-012510-S2-2024-01-18","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"aligned_stage2_then_confirmed_green","current_profile_verdict":"current_profile_correct","price_source":"Songdaiki/stock-web","notes":"Enterprise software/ERP/cloud-AI rerating where Green should wait for revision and margin bridge."}
{"row_type":"case","case_id":"C28-053800-2022-THEME-GUARD","symbol":"053800","company_name":"안랩","round":"R8","loop":"32","large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C28_SOFTWARE_SECURITY_CONTRACT_RETENTION","fine_archetype_id":"SECURITY_VENDOR_POLITICAL_THEME_FALSE_POSITIVE","case_type":"false_positive_green","positive_or_counterexample":"counterexample","best_trigger":"TR-C28-053800-S2-2022-01-05","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"high_MFE_but_unacceptable_MAE_and_no_contract_retention","current_profile_verdict":"current_profile_false_positive","price_source":"Songdaiki/stock-web","notes":"Security vendor attention/relative strength without security contract-retention evidence should be capped."}
{"row_type":"case","case_id":"C28-131370-2020-REMOTE-SUPPORT","symbol":"131370","company_name":"알서포트","round":"R8","loop":"32","large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C28_SOFTWARE_SECURITY_CONTRACT_RETENTION","fine_archetype_id":"REMOTE_SUPPORT_COVID_USAGE_TO_RETENTION_4B","case_type":"4B_overlay_success","positive_or_counterexample":"counterexample","best_trigger":"TR-C28-131370-S2-2020-02-18","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"stage2_usage_shock_worked_but_green_needs_retention_conversion","current_profile_verdict":"current_profile_4B_too_late","price_source":"Songdaiki/stock-web","notes":"Remote-support usage shock had huge MFE but needs 4B overlay when retention is unproven."}
{"row_type":"trigger","trigger_id":"TR-C28-012510-S2-2024-01-18","case_id":"C28-012510-2024-ERP-AI","symbol":"012510","company_name":"더존비즈온","round":"R8","loop":"32","large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C28_SOFTWARE_SECURITY_CONTRACT_RETENTION","fine_archetype_id":"ENTERPRISE_ERP_CLOUD_AI_RETENTION","sector":"platform_content_sw_security","primary_archetype":"software_security_contract_retention","loop_objective":"coverage_gap_fill|canonical_archetype_compression|green_strictness_stress_test","trigger_type":"Stage2-Actionable","trigger_date":"2024-01-18","evidence_available_at_that_date":"enterprise ERP/cloud/AI rerating with early revision signal; not yet confirmed Green","evidence_source":"historical public event/IR/news context; OHLC verified in stock-web","stage2_evidence_fields":["public_event_or_disclosure","customer_or_order_quality","relative_strength","early_revision_signal"],"stage3_evidence_fields":[],"stage4b_evidence_fields":[],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/012/012510/2024.csv","profile_path":"atlas/symbol_profiles/012/012510.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","entry_date":"2024-01-18","entry_price":40800,"MFE_30D_pct":37.99,"MFE_90D_pct":60.78,"MFE_180D_pct":91.91,"MFE_1Y_pct":91.91,"MFE_2Y_pct":135.29,"MAE_30D_pct":-11.27,"MAE_90D_pct":-11.27,"MAE_180D_pct":-11.27,"MAE_1Y_pct":-11.27,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-07-08","peak_price":78300,"drawdown_after_peak_pct":-40.68,"green_lateness_ratio":0.405,"four_b_local_peak_proximity":null,"four_b_full_window_peak_proximity":null,"four_b_timing_verdict":null,"four_b_evidence_type":[],"four_c_protection_label":"not_applicable","trigger_outcome_label":"structural_success_stage2_captured","current_profile_verdict":"current_profile_correct","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"C28-012510-2024-01-18-40800","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"TR-C28-012510-GREEN-2024-04-29","case_id":"C28-012510-2024-ERP-AI","symbol":"012510","company_name":"더존비즈온","round":"R8","loop":"32","large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C28_SOFTWARE_SECURITY_CONTRACT_RETENTION","fine_archetype_id":"ENTERPRISE_ERP_CLOUD_AI_RETENTION","sector":"platform_content_sw_security","primary_archetype":"software_security_contract_retention","loop_objective":"green_strictness_stress_test","trigger_type":"Stage3-Green","trigger_date":"2024-04-29","evidence_available_at_that_date":"revision/margin bridge confirmation after initial rerating","evidence_source":"historical public result/IR context; OHLC verified in stock-web","stage2_evidence_fields":["early_revision_signal"],"stage3_evidence_fields":["confirmed_revision","margin_bridge","financial_visibility","multiple_public_sources"],"stage4b_evidence_fields":[],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/012/012510/2024.csv","profile_path":"atlas/symbol_profiles/012/012510.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","entry_date":"2024-04-29","entry_price":56000,"MFE_30D_pct":17.14,"MFE_90D_pct":39.82,"MFE_180D_pct":39.82,"MFE_1Y_pct":64.29,"MFE_2Y_pct":71.43,"MAE_30D_pct":-9.46,"MAE_90D_pct":-13.39,"MAE_180D_pct":-19.82,"MAE_1Y_pct":-19.82,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-07-08","peak_price":78300,"drawdown_after_peak_pct":-40.68,"green_lateness_ratio":0.405,"four_b_local_peak_proximity":null,"four_b_full_window_peak_proximity":null,"four_b_timing_verdict":null,"four_b_evidence_type":[],"four_c_protection_label":"not_applicable","trigger_outcome_label":"confirmed_green_valid_but_late","current_profile_verdict":"current_profile_correct","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"C28-012510-2024-04-29-56000","dedupe_for_aggregate":false,"aggregate_group_role":"label_comparison_only","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"TR-C28-053800-S2-2022-01-05","case_id":"C28-053800-2022-THEME-GUARD","symbol":"053800","company_name":"안랩","round":"R8","loop":"32","large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C28_SOFTWARE_SECURITY_CONTRACT_RETENTION","fine_archetype_id":"SECURITY_VENDOR_POLITICAL_THEME_FALSE_POSITIVE","sector":"platform_content_sw_security","primary_archetype":"software_security_contract_retention","loop_objective":"counterexample_mining|residual_false_positive_mining","trigger_type":"Stage2-Blocked","trigger_date":"2022-01-05","evidence_available_at_that_date":"relative strength and public attention without confirmed security contract-retention evidence","evidence_source":"historical public event context; OHLC verified in stock-web","stage2_evidence_fields":["relative_strength"],"stage3_evidence_fields":[],"stage4b_evidence_fields":["valuation_blowoff","positioning_overheat","explicit_event_cap"],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/053/053800/2022.csv","profile_path":"atlas/symbol_profiles/053/053800.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","entry_date":"2022-01-05","entry_price":120500,"MFE_30D_pct":6.64,"MFE_90D_pct":81.33,"MFE_180D_pct":81.33,"MFE_1Y_pct":81.33,"MFE_2Y_pct":81.33,"MAE_30D_pct":-44.81,"MAE_90D_pct":-47.30,"MAE_180D_pct":-47.30,"MAE_1Y_pct":-47.30,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2022-03-24","peak_price":218500,"drawdown_after_peak_pct":-62.93,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":0.564,"four_b_full_window_peak_proximity":0.564,"four_b_timing_verdict":"acceptable_overlay_but_not_positive_stage","four_b_evidence_type":["valuation_blowoff","positioning_overheat","control_premium_or_event_premium"],"four_c_protection_label":"thesis_break_watch_only","trigger_outcome_label":"false_positive_green_risk_high_mae","current_profile_verdict":"current_profile_false_positive","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"C28-053800-2022-01-05-120500","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"TR-C28-053800-4B-2022-03-23","case_id":"C28-053800-2022-THEME-GUARD","symbol":"053800","company_name":"안랩","round":"R8","loop":"32","large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C28_SOFTWARE_SECURITY_CONTRACT_RETENTION","fine_archetype_id":"SECURITY_VENDOR_POLITICAL_THEME_FALSE_POSITIVE","sector":"platform_content_sw_security","primary_archetype":"software_security_contract_retention","loop_objective":"4B_non_price_requirement_stress_test","trigger_type":"Stage4B-overlay","trigger_date":"2022-03-23","evidence_available_at_that_date":"blowoff event-premium zone without contract-retention proof","evidence_source":"historical public event context; OHLC verified in stock-web","stage2_evidence_fields":[],"stage3_evidence_fields":[],"stage4b_evidence_fields":["valuation_blowoff","positioning_overheat","explicit_event_cap"],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/053/053800/2022.csv","profile_path":"atlas/symbol_profiles/053/053800.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","entry_date":"2022-03-23","entry_price":175800,"MFE_30D_pct":24.29,"MFE_90D_pct":24.29,"MFE_180D_pct":24.29,"MFE_1Y_pct":24.29,"MFE_2Y_pct":24.29,"MAE_30D_pct":-30.77,"MAE_90D_pct":-53.92,"MAE_180D_pct":-62.93,"MAE_1Y_pct":-62.93,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2022-03-24","peak_price":218500,"drawdown_after_peak_pct":-62.93,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":0.564,"four_b_full_window_peak_proximity":0.564,"four_b_timing_verdict":"acceptable_overlay_but_not_positive_stage","four_b_evidence_type":["valuation_blowoff","positioning_overheat","control_premium_or_event_premium"],"four_c_protection_label":"thesis_break_watch_only","trigger_outcome_label":"4B_overlay_success","current_profile_verdict":"current_profile_false_positive","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"C28-053800-2022-03-23-175800","dedupe_for_aggregate":false,"aggregate_group_role":"4B_overlay_only","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"TR-C28-131370-S2-2020-02-18","case_id":"C28-131370-2020-REMOTE-SUPPORT","symbol":"131370","company_name":"알서포트","round":"R8","loop":"32","large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C28_SOFTWARE_SECURITY_CONTRACT_RETENTION","fine_archetype_id":"REMOTE_SUPPORT_COVID_USAGE_TO_RETENTION_4B","sector":"platform_content_sw_security","primary_archetype":"software_security_contract_retention","loop_objective":"coverage_gap_fill|4B_non_price_requirement_stress_test","trigger_type":"Stage2-Actionable","trigger_date":"2020-02-18","evidence_available_at_that_date":"remote support usage shock visible but subscription-retention conversion not yet confirmed","evidence_source":"historical COVID remote-work usage context; OHLC verified in stock-web","stage2_evidence_fields":["public_event_or_disclosure","capacity_or_volume_route","relative_strength"],"stage3_evidence_fields":[],"stage4b_evidence_fields":[],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/131/131370/2020.csv","profile_path":"atlas/symbol_profiles/131/131370.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","entry_date":"2020-02-18","entry_price":3200,"MFE_30D_pct":89.69,"MFE_90D_pct":174.06,"MFE_180D_pct":639.06,"MFE_1Y_pct":639.06,"MFE_2Y_pct":639.06,"MAE_30D_pct":-25.78,"MAE_90D_pct":-25.78,"MAE_180D_pct":-25.78,"MAE_1Y_pct":-25.78,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2020-08-28","peak_price":23650,"drawdown_after_peak_pct":-50.53,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":0.819,"four_b_full_window_peak_proximity":0.819,"four_b_timing_verdict":"good_full_window_4B_timing","four_b_evidence_type":["valuation_blowoff","positioning_overheat","margin_or_backlog_slowdown"],"four_c_protection_label":"thesis_break_watch_only","trigger_outcome_label":"usage_shock_success_but_green_retention_missing","current_profile_verdict":"current_profile_4B_too_late","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"C28-131370-2020-02-18-3200","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"TR-C28-131370-4B-2020-08-28","case_id":"C28-131370-2020-REMOTE-SUPPORT","symbol":"131370","company_name":"알서포트","round":"R8","loop":"32","large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C28_SOFTWARE_SECURITY_CONTRACT_RETENTION","fine_archetype_id":"REMOTE_SUPPORT_COVID_USAGE_TO_RETENTION_4B","sector":"platform_content_sw_security","primary_archetype":"software_security_contract_retention","loop_objective":"4B_non_price_requirement_stress_test","trigger_type":"Stage4B-overlay","trigger_date":"2020-08-28","evidence_available_at_that_date":"peak-zone valuation and retention-normalization risk after remote-work usage shock","evidence_source":"historical COVID remote-work usage context; OHLC verified in stock-web","stage2_evidence_fields":[],"stage3_evidence_fields":[],"stage4b_evidence_fields":["valuation_blowoff","positioning_overheat","margin_or_backlog_slowdown"],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/131/131370/2020.csv","profile_path":"atlas/symbol_profiles/131/131370.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","entry_date":"2020-08-28","entry_price":19950,"MFE_30D_pct":18.55,"MFE_90D_pct":18.55,"MFE_180D_pct":18.55,"MFE_1Y_pct":18.55,"MFE_2Y_pct":18.55,"MAE_30D_pct":-18.05,"MAE_90D_pct":-41.35,"MAE_180D_pct":-41.35,"MAE_1Y_pct":-41.35,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2020-08-28","peak_price":23650,"drawdown_after_peak_pct":-50.53,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":0.819,"four_b_full_window_peak_proximity":0.819,"four_b_timing_verdict":"good_full_window_4B_timing","four_b_evidence_type":["valuation_blowoff","positioning_overheat","margin_or_backlog_slowdown"],"four_c_protection_label":"thesis_break_watch_only","trigger_outcome_label":"4B_overlay_success","current_profile_verdict":"current_profile_4B_too_late","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"C28-131370-2020-08-28-19950","dedupe_for_aggregate":false,"aggregate_group_role":"4B_overlay_only","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"C28-012510-2024-ERP-AI","trigger_id":"TR-C28-012510-S2-2024-01-18","symbol":"012510","large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C28_SOFTWARE_SECURITY_CONTRACT_RETENTION","raw_component_scores_before":{"contract_score":64,"backlog_visibility_score":55,"margin_bridge_score":50,"revision_score":58,"relative_strength_score":72,"customer_quality_score":65,"policy_or_regulatory_score":0,"valuation_repricing_score":58,"execution_risk_score":28,"legal_or_contract_risk_score":10,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_before":82,"stage_label_before":"Stage3-Yellow","raw_component_scores_after":{"contract_score":70,"backlog_visibility_score":60,"margin_bridge_score":62,"revision_score":68,"relative_strength_score":72,"customer_quality_score":70,"policy_or_regulatory_score":0,"valuation_repricing_score":58,"execution_risk_score":24,"legal_or_contract_risk_score":8,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_after":88,"stage_label_after":"Stage3-Green_after_confirmation","changed_components":["contract_score","margin_bridge_score","revision_score","customer_quality_score"],"component_delta_explanation":"C28 positive bridge rewards recurring enterprise software evidence only after revision/margin confirmation.","MFE_90D_pct":60.78,"MAE_90D_pct":-11.27,"score_return_alignment_label":"aligned","current_profile_verdict":"current_profile_correct"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"C28-053800-2022-THEME-GUARD","trigger_id":"TR-C28-053800-S2-2022-01-05","symbol":"053800","large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C28_SOFTWARE_SECURITY_CONTRACT_RETENTION","raw_component_scores_before":{"contract_score":10,"backlog_visibility_score":5,"margin_bridge_score":0,"revision_score":5,"relative_strength_score":90,"customer_quality_score":10,"policy_or_regulatory_score":0,"valuation_repricing_score":82,"execution_risk_score":70,"legal_or_contract_risk_score":20,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_before":78,"stage_label_before":"Stage3-Yellow_false_positive_risk","raw_component_scores_after":{"contract_score":10,"backlog_visibility_score":5,"margin_bridge_score":0,"revision_score":5,"relative_strength_score":55,"customer_quality_score":10,"policy_or_regulatory_score":0,"valuation_repricing_score":60,"execution_risk_score":82,"legal_or_contract_risk_score":25,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_after":64,"stage_label_after":"Stage2-Blocked_or_4B_watch","changed_components":["relative_strength_score","valuation_repricing_score","execution_risk_score"],"component_delta_explanation":"Contract-retention Green cap reduces price/theme score and raises execution/event-premium risk.","MFE_90D_pct":81.33,"MAE_90D_pct":-47.30,"score_return_alignment_label":"MFE_high_but_label_quality_bad_without_guard","current_profile_verdict":"current_profile_false_positive"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"C28-131370-2020-REMOTE-SUPPORT","trigger_id":"TR-C28-131370-S2-2020-02-18","symbol":"131370","large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C28_SOFTWARE_SECURITY_CONTRACT_RETENTION","raw_component_scores_before":{"contract_score":30,"backlog_visibility_score":15,"margin_bridge_score":10,"revision_score":18,"relative_strength_score":88,"customer_quality_score":25,"policy_or_regulatory_score":0,"valuation_repricing_score":82,"execution_risk_score":45,"legal_or_contract_risk_score":10,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_before":80,"stage_label_before":"Stage3-Yellow_risk","raw_component_scores_after":{"contract_score":28,"backlog_visibility_score":15,"margin_bridge_score":8,"revision_score":16,"relative_strength_score":70,"customer_quality_score":25,"policy_or_regulatory_score":0,"valuation_repricing_score":65,"execution_risk_score":72,"legal_or_contract_risk_score":12,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_after":68,"stage_label_after":"Stage2-Actionable_then_4B_overlay","changed_components":["relative_strength_score","valuation_repricing_score","execution_risk_score"],"component_delta_explanation":"Usage spike can be Stage2, but Green requires retention conversion; 4B overlay activates once valuation and usage-normalization risk rise.","MFE_90D_pct":174.06,"MAE_90D_pct":-25.78,"score_return_alignment_label":"Stage2_aligned_Green_not_aligned","current_profile_verdict":"current_profile_4B_too_late"}
{"row_type":"residual_contribution","round":"R8","loop":"32","large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C28_SOFTWARE_SECURITY_CONTRACT_RETENTION","new_independent_case_count":3,"reused_case_count":0,"new_symbol_count":3,"same_archetype_new_symbol_count":3,"same_archetype_new_trigger_family_count":3,"new_canonical_archetype_count":1,"new_trigger_family_count":3,"positive_case_count":1,"counterexample_count":2,"current_profile_error_count":3,"diversity_score_summary":"high: C28 new canonical gap with 3 new symbols and 3 trigger families","tested_existing_calibrated_axes":["stage3_green_revision_min","price_only_blowoff_blocks_positive_stage","full_4b_requires_non_price_evidence","hard_4c_thesis_break_routes_to_4c"],"residual_error_types_found":["theme_false_positive_without_contract_retention","usage_spike_green_overpromotion","4B_late_after_temporary_software_demand"],"loop_contribution_label":"canonical_archetype_rule_candidate","do_not_propose_new_weight_delta":false,"auto_selected_coverage_gap":"R8/C28 software/security contract-retention gap"}
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
next_round = R8 / C28 holdout with pure SaaS/security renewal-positive cases, or R9 / C29 mobility volume-margin operating leverage
suggested_next_coverage_gap = C28 pure security contract renewal positive; C28 hard 4C cyber/accounting trust break; C29 mobility margin operating leverage
```

## 28. Source Notes

Stock-Web source validation used the manifest and schema from Songdaiki/stock-web. Individual OHLC rows were checked from the tradable symbol-year shards listed in the Price Data Source Map. Symbol profile files were checked for name, market, available years, and corporate-action candidate dates. The research uses raw, unadjusted OHLC from FinanceData/marcap through the Stock-Web atlas and therefore blocks corporate-action-contaminated windows by default.

This MD does not change production scoring and does not implement repository code.
