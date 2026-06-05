# E2R Stock-Web Historical Calibration / Sector-Archetype Residual Research Round

## 0. Research Metadata

```text
research_session = post_calibrated_sector_archetype_residual_research
mode = historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12
scheduled_round = R8
scheduled_loop = 92
round_schedule_status = valid
round_sector_consistency = pass
large_sector_id = L8_PLATFORM_CONTENT_SW_SECURITY
canonical_archetype_id = C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE
fine_archetype_id = COMMERCE_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE_BRIDGE_VS_DIGITAL_AD_REP_FALSE_STAGE2_AND_AD_AGENCY_EVENT_CAP
loop_objective = coverage_gap_fill | counterexample_mining | stage2_actionable_bonus_stress_test | 4B_non_price_requirement_stress_test | high_MAE_guardrail | canonical_archetype_compression
output_file = e2r_stock_web_v12_residual_round_R8_loop_92_L8_PLATFORM_CONTENT_SW_SECURITY_C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE_research.md
```

This file is the corrected final output for this execution. The scheduler state after R7 loop 92 is R8 / loop 92. It fills C26 platform/ad revenue operating-leverage behavior after the prior R8 loop 91 used C28, loop 90 used C27, and loop 89 used C26 with different symbols.

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
scheduled_loop = 92
large_sector_id = L8_PLATFORM_CONTENT_SW_SECURITY
canonical_archetype_id = C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE
round_sector_consistency = pass
computed_next_round = R9
computed_next_loop = 92
```

R8 permits L8 platform/content/software/security research. This loop returns to under-covered C26 with a platform operating-leverage positive and two bridge-missing ad-revenue counterexamples.

## 3. Previous Coverage / Duplicate Avoidance Check

No-Repeat hard key used:

```text
canonical_archetype_id + symbol + trigger_type + entry_date
```

No-Repeat snapshot context:

```text
C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE = 13 rows / 10 symbols / good-bad Stage2 2-6 / 4B-4C 0-1
top covered symbols include 042000(2), 214270(2), 237820(2), 030000(1), 035420(1), 035720(1)
previous R8 loop-89 C26 symbols avoided: 067160, 216050, 273060
previous R8 loop-90 C27 symbols avoided: 419530, 408900, 417180
previous R8 loop-91 C28 symbols avoided: 170790, 136540, 356890
previous R7 loop-92 C23 symbols avoided: 196170, 003850, 950160
```

Selected rows avoid hard duplicate keys:

```text
042000 / Stage2-Actionable / 2024-05-09
089600 / Stage2-Actionable / 2024-01-24
123570 / Stage4B / 2024-03-06
```

`042000` is a reduced-weight soft expansion because it already appears in top-covered C26, but the entry date and bridge family are fresh.

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
| 042000 | atlas/symbol_profiles/042/042000.json | selected 2024 window clean after old 2021 CA candidates |
| 089600 | atlas/symbol_profiles/089/089600.json | no corporate-action candidate |
| 123570 | atlas/symbol_profiles/123/123570.json | selected 2024 window clean after old 2016/2018 CA candidates |

## 5. Historical Eligibility Gate

| case_id | symbol | entry_date | entry in shard | forward 180D | OHLC valid | CA clean | calibration_usable |
|---|---|---:|---|---:|---|---|---|
| R8L92_C26_CAFE24_2024_COMMERCE_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE_POSITIVE | 042000 | 2024-05-09 | yes | 180 | yes | yes | true |
| R8L92_C26_NASMEDIA_2024_DIGITAL_AD_REP_RECOVERY_FALSE_STAGE2 | 089600 | 2024-01-24 | yes | 180 | yes | yes | true |
| R8L92_C26_EMNET_2024_DIGITAL_AD_AGENCY_EVENT_CAP_4B | 123570 | 2024-03-06 | yes | 180 | yes | yes | true |

## 6. Canonical Archetype Compression Map

| canonical | fine/deep split | meaning |
|---|---|---|
| C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE | COMMERCE_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE_BRIDGE | Positive Stage2 requires platform traffic, GMV/seller activity, ad/solution revenue, operating leverage, margin and revision bridge. |
| C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE | DIGITAL_AD_REP_FALSE_STAGE2 | Ad-recovery label without advertiser-budget/take-rate/margin bridge can become false Stage2. |
| C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE | DIGITAL_AD_AGENCY_EVENT_CAP_4B | Digital-ad event premium should route to 4B when budget and margin evidence are capped or missing. |

## 7. Case Selection Summary

| case_id | symbol | company | role | selected reason |
|---|---|---|---|---|
| R8L92_C26_CAFE24_2024_COMMERCE_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE_POSITIVE | 042000 | 카페24 | positive | Commerce-platform traffic / seller-tools / ad-revenue bridge produced very high MFE with controlled MAE. |
| R8L92_C26_NASMEDIA_2024_DIGITAL_AD_REP_RECOVERY_FALSE_STAGE2 | 089600 | 나스미디어 | counterexample | Digital ad-recovery watch peaked near entry and then produced deep 90D/180D MAE. |
| R8L92_C26_EMNET_2024_DIGITAL_AD_AGENCY_EVENT_CAP_4B | 123570 | 이엠넷 | counterexample / 4B | Digital ad-agency event premium capped at the March spike and then de-rated deeply. |

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
| Cafe24 commerce platform operating leverage | historical public/report proxy | true | true | shadow-only positive |
| Nasmedia digital ad recovery false Stage2 | historical public/news proxy | true | true | false-Stage2 guardrail |
| eMnet digital ad agency event cap | historical public/news proxy | true | true | 4B overlay counterexample |

## 10. Price Data Source Map

| symbol | shard | profile |
|---|---|---|
| 042000 | atlas/ohlcv_tradable_by_symbol_year/042/042000/2024.csv | atlas/symbol_profiles/042/042000.json |
| 089600 | atlas/ohlcv_tradable_by_symbol_year/089/089600/2024.csv | atlas/symbol_profiles/089/089600.json |
| 123570 | atlas/ohlcv_tradable_by_symbol_year/123/123570/2024.csv | atlas/symbol_profiles/123/123570.json |

## 11. Case-by-Case Trigger Grid

| trigger_id | symbol | trigger_type | entry_date | entry_price | role | verdict |
|---|---|---|---:|---:|---|---|
| R8L92_C26_CAFE24_2024_STAGE2_ACTIONABLE_COMMERCE_PLATFORM_AD_REVENUE_LEVERAGE | 042000 | Stage2-Actionable | 2024-05-09 | 19390 | positive | commerce platform ad/revenue operating-leverage bridge worked |
| R8L92_C26_NASMEDIA_2024_STAGE2_FALSE_POSITIVE_DIGITAL_AD_REP_RECOVERY | 089600 | Stage2-Actionable | 2024-01-24 | 25350 | counterexample | digital ad-recovery false Stage2 |
| R8L92_C26_EMNET_2024_STAGE4B_DIGITAL_AD_AGENCY_EVENT_CAP | 123570 | Stage4B | 2024-03-06 | 4800 | counterexample/4B | digital ad-agency event cap |

## 12. Trigger-Level OHLC Backtest Tables

| trigger_id | entry | MFE30 | MAE30 | MFE90 | MAE90 | MFE180 | MAE180 | peak_date | peak_price | drawdown_after_peak |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| R8L92_C26_CAFE24_2024_STAGE2_ACTIONABLE_COMMERCE_PLATFORM_AD_REVENUE_LEVERAGE | 19390 | 120.99 | -8.77 | 121.51 | -8.77 | 121.51 | -8.77 | 2024-06-26 | 42950 | -43.54 |
| R8L92_C26_NASMEDIA_2024_STAGE2_FALSE_POSITIVE_DIGITAL_AD_REP_RECOVERY | 25350 | 5.72 | -10.45 | 5.72 | -36.29 | 5.72 | -40.08 | 2024-01-24 | 26800 | -43.32 |
| R8L92_C26_EMNET_2024_STAGE4B_DIGITAL_AD_AGENCY_EVENT_CAP | 4800 | 8.96 | -23.54 | 8.96 | -38.02 | 8.96 | -50.10 | 2024-03-06 | 5230 | -54.21 |

## 13. Current Calibrated Profile Stress Test

| axis | outcome |
|---|---|
| stage2_required_bridge | strengthen: C26 Stage2 needs platform traffic / GMV / advertiser budget / take-rate / operating-leverage bridge |
| local_4b_watch_guard | strengthen: bridge-missing digital-ad event premiums should route to 4B watch |
| high_MAE_guardrail | strengthen: high-MAE ad-recovery rows cannot promote without durable revenue/margin bridge |
| full_4b_requires_non_price_evidence | keep |
| price_only_blowoff_blocks_positive_stage | keep |
| hard_4c_thesis_break_routes_to_4c | keep; no hard 4C promoted |

## 14. Stage2 / Yellow / Green Comparison

No confirmed Stage3-Green row is introduced. The useful split is platform operating-leverage bridge quality:

| symbol | stage quality | explanation |
|---|---|---|
| 042000 | good_stage2_with_later_watch | Platform traffic / seller-tools / ad-solution revenue bridge produced very high MFE. |
| 089600 | bad_stage2 | Ad recovery label lacked budget/take-rate bridge and drew down deeply. |
| 123570 | good_4B | Digital ad-agency event premium capped near entry and de-rated. |

```text
green_lateness_ratio = not_applicable
reason = no confirmed Stage3-Green trigger
```

## 15. 4B Local vs Full-window Timing Audit

| trigger | local proximity | full-window proximity | timing verdict |
|---|---:|---:|---|
| 089600 digital ad-recovery false Stage2 | 0.95 | 0.95 | false Stage2 due missing budget/take-rate/margin bridge |
| 123570 digital ad-agency cap | 0.92 | 0.92 | good full-window 4B timing |
| 042000 commerce-platform bridge | n/a | n/a | positive Stage2, but later platform valuation watch required |

## 16. 4C Protection Audit

```text
4C_case_count = 0
four_c_protection_label = thesis_break_watch_only for 089600 / 123570
```

No hard 4C candidate is proposed. R8 loop 92 is about Stage2 bridge quality and 4B event-cap timing.

## 17. Sector-Specific Rule Candidate

```text
sector_specific_rule_candidate = true
rule_scope = sector_specific
rule = In L8 platform/ad revenue operating-leverage cases, Stage2 requires verified platform traffic, GMV/seller activity, advertiser budget, take-rate, ad/solution revenue, operating leverage, margin, or revision bridge. Platform, digital ad, online marketing, e-commerce, or ad-agency label alone remains watch/4B.
proposal_status = shadow_only
```

## 18. Canonical-Archetype Rule Candidate

```text
canonical_archetype_rule_candidate = true
canonical_archetype_id = C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE
rule = C26 should split true platform ad/revenue operating-leverage positives from digital-ad recovery false Stage2 and digital-ad agency event caps. Event-cap rows are 4B overlay/risk calibration, not Stage3-Green promotion evidence.
proposal_status = shadow_only_not_production
```

## 19. Before / After Backtest Comparison

| profile | hypothesis | eligible triggers | avg_MFE90 | avg_MAE90 | false_positive_rate | verdict |
|---|---|---:|---:|---:|---:|---|
| P0 e2r_2_1_stock_web_calibrated_proxy | current profile | 3 | 45.40 | -27.69 | 0.67 | mixed; C26 bridge split needed |
| P0b e2r_2_0_baseline_reference | older baseline | 3 | 45.40 | -27.69 | 0.67 | weaker bridge/event-cap guard |
| P1 sector_specific_candidate_profile | L8 traffic/budget/operating-leverage bridge required | 2 | 63.62 | -22.53 | 0.50 | better |
| P2 canonical_archetype_candidate_profile | C26 bridge vs event-cap split | 2 | 63.62 | -22.53 | 0.50 | best explanatory fit |
| P3 counterexample_guard_profile | reject bridge-missing ad/platform themes as positive | 1 | 121.51 | -8.77 | 0.00 | safest but source-proxy blockers remain |

## 20. Score-Return Alignment Matrix

| trigger | score before | stage before | score after | stage after | MFE90 | MAE90 | alignment |
|---|---:|---|---:|---|---:|---:|---|
| 042000 commerce-platform bridge | 66 | Stage2-Watch | 76 | Stage2-Actionable | 121.51 | -8.77 | commerce_platform_ad_revenue_operating_leverage_positive |
| 089600 digital ad false | 66 | Stage2-Actionable | 52 | Stage1/Watch | 5.72 | -36.29 | digital_ad_recovery_false_stage2 |
| 123570 ad-agency cap | 70 | Stage3-Yellow-like | 54 | Stage4B-watch | 8.96 | -38.02 | digital_ad_agency_event_cap_4B_guard |

## 21. Coverage Matrix

```jsonl
{"row_type": "coverage_matrix", "large_sector_id": "L8_PLATFORM_CONTENT_SW_SECURITY", "canonical_archetype_id": "C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE", "fine_archetype_id": "COMMERCE_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE_BRIDGE_VS_DIGITAL_AD_REP_FALSE_STAGE2_AND_AD_AGENCY_EVENT_CAP", "positive_case_count": 1, "counterexample_count": 2, "4B_case_count": 1, "4C_case_count": 0, "new_independent_case_count": 3, "reused_case_count": 0, "calibration_usable_trigger_count": 3, "representative_trigger_count": 2, "current_profile_error_count": 2, "sector_rule_candidate": true, "canonical_rule_candidate": true, "coverage_gap_after_this_loop": "Adds C26 commerce-platform ad/revenue operating-leverage positive, digital ad-rep recovery false Stage2, and digital ad-agency event-cap 4B split using two new symbols plus one reduced-weight soft expansion."}
```

## 22. Residual Contribution Summary

```text
new_independent_case_count: 3
reused_case_count: 0
reused_case_ids: []
new_symbol_count: 2
new_canonical_archetype_count: 0
new_fine_archetype_count: 1
new_trigger_family_count: 3
tested_existing_calibrated_axes: stage2_required_bridge, local_4b_watch_guard, high_MAE_guardrail, full_4b_requires_non_price_evidence, price_only_blowoff_blocks_positive_stage
residual_error_types_found: commerce_platform_ad_revenue_operating_leverage_positive, digital_ad_recovery_false_stage2, digital_ad_agency_event_cap_4B
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
- C26 platform/ad revenue operating-leverage bridge vs false Stage2 / event-cap split
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
shadow_weight,stage2_required_bridge,canonical_archetype,L8_PLATFORM_CONTENT_SW_SECURITY,C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE,configured,C26_requires_traffic_GMV_ad_budget_take_rate_margin_revision_bridge,0,"C26 Stage2 should require platform traffic, GMV/seller activity, advertiser budget, take-rate, ad/solution revenue, operating leverage, margin, or revision bridge, not platform/ad/online-marketing label alone","Cafe24 positive worked; Nasmedia and eMnet theme/event rows failed positive-stage promotion","R8L92_C26_CAFE24_2024_STAGE2_ACTIONABLE_COMMERCE_PLATFORM_AD_REVENUE_LEVERAGE|R8L92_C26_NASMEDIA_2024_STAGE2_FALSE_POSITIVE_DIGITAL_AD_REP_RECOVERY|R8L92_C26_EMNET_2024_STAGE4B_DIGITAL_AD_AGENCY_EVENT_CAP",3,3,2,low,canonical_shadow_only,"do_not_propose_new_weight_delta=true because source-proxy/evidence-url-pending rows remain"
shadow_weight,local_4b_watch_guard,canonical_archetype,L8_PLATFORM_CONTENT_SW_SECURITY,C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE,configured,cap_bridge_missing_ad_recovery_and_agency_event_premiums_as_4B_watch,0,"Ad-revenue and agency event premiums can peak before traffic/budget/take-rate evidence is proven","Nasmedia had limited MFE and deep MAE; eMnet showed 4B event-cap behavior after March spike","R8L92_C26_NASMEDIA_2024_STAGE2_FALSE_POSITIVE_DIGITAL_AD_REP_RECOVERY|R8L92_C26_EMNET_2024_STAGE4B_DIGITAL_AD_AGENCY_EVENT_CAP",2,2,2,medium,guardrail_shadow_only,"4B overlay only; not production"
shadow_weight,high_MAE_guardrail,canonical_archetype,L8_PLATFORM_CONTENT_SW_SECURITY,C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE,configured,block_positive_stage_when_ad_theme_has_high_MAE_without_operating_leverage_bridge,0,"High MAE after bridge-missing ad/platform event entries should block Stage2/Stage3 promotion unless traffic, budget, take-rate and margin evidence survives","Nasmedia MAE90=-36.29 and eMnet MAE90=-38.02","R8L92_C26_NASMEDIA_2024_STAGE2_FALSE_POSITIVE_DIGITAL_AD_REP_RECOVERY|R8L92_C26_EMNET_2024_STAGE4B_DIGITAL_AD_AGENCY_EVENT_CAP",2,2,2,medium,guardrail_shadow_only,"canonical shadow profile only"
```

## 25. Machine-Readable Rows

### 25.1 price_source_validation

```jsonl
{"row_type": "price_source_validation", "source": "Songdaiki/stock-web", "source_url": "https://github.com/Songdaiki/stock-web", "manifest_path": "atlas/manifest.json", "schema_path": "atlas/schema.json", "universe_path": "atlas/universe/all_symbols.csv", "manifest_max_date": "2026-02-20", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "raw_shard_root": "atlas/ohlcv_raw_by_symbol_year", "validation_status": "usable_for_historical_calibration", "source_name": "FinanceData/marcap", "tradable_row_count": 14354401, "raw_row_count": 15214118, "symbol_count": 5414, "active_like_symbol_count": 2868, "inactive_or_delisted_like_symbol_count": 2546}
```

### 25.2 case rows

```jsonl
{"row_type": "case", "case_id": "R8L92_C26_CAFE24_2024_COMMERCE_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE_POSITIVE", "symbol": "042000", "company_name": "카페24", "round": "R8", "loop": "92", "large_sector_id": "L8_PLATFORM_CONTENT_SW_SECURITY", "canonical_archetype_id": "C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE", "fine_archetype_id": "COMMERCE_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE_BRIDGE_VS_DIGITAL_AD_REP_FALSE_STAGE2_AND_AD_AGENCY_EVENT_CAP", "case_type": "structural_success_with_later_platform_valuation_watch", "positive_or_counterexample": "positive", "best_trigger": "R8L92_C26_CAFE24_2024_STAGE2_ACTIONABLE_COMMERCE_PLATFORM_AD_REVENUE_LEVERAGE", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": "Soft expansion: 042000 appears in C26 coverage, but this row uses a new 2024 entry date and commerce-platform ad/revenue operating-leverage bridge family.", "independent_evidence_weight": 0.75, "score_price_alignment": "Commerce platform / creator-commerce / ad-revenue operating-leverage bridge produced very high 30D/90D MFE with controlled initial MAE. C26 works when platform traffic, GMV, seller tools, ad/solution revenue and operating leverage convert into margin/revision bridge.", "current_profile_verdict": "current_profile_kept_but_C26_positive_requires_platform_traffic_GMV_ad_revenue_margin_revision_bridge_not_platform_label_only", "price_source": "Songdaiki/stock-web", "notes": "Selected 2024 window clean after old 2021 CA candidates. Reduced evidence weight because 042000 is already a top-covered C26 symbol."}
{"row_type": "case", "case_id": "R8L92_C26_NASMEDIA_2024_DIGITAL_AD_REP_RECOVERY_FALSE_STAGE2", "symbol": "089600", "company_name": "나스미디어", "round": "R8", "loop": "92", "large_sector_id": "L8_PLATFORM_CONTENT_SW_SECURITY", "canonical_archetype_id": "C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE", "fine_archetype_id": "COMMERCE_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE_BRIDGE_VS_DIGITAL_AD_REP_FALSE_STAGE2_AND_AD_AGENCY_EVENT_CAP", "case_type": "failed_rerating_ad_revenue_bridge_missing", "positive_or_counterexample": "counterexample", "best_trigger": "R8L92_C26_NASMEDIA_2024_STAGE2_FALSE_POSITIVE_DIGITAL_AD_REP_RECOVERY", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "Digital ad-rep / platform ad recovery watch peaked near the entry and then produced deep 90D/180D MAE. C26 Stage2 should not be awarded without traffic/advertiser budget recovery, take-rate, margin and revision bridge.", "current_profile_verdict": "current_profile_false_positive_if_digital_ad_recovery_counts_without_traffic_budget_margin_revision_bridge", "price_source": "Songdaiki/stock-web", "notes": "No corporate-action caveat in selected 2024 window. Source-proxy only."}
{"row_type": "case", "case_id": "R8L92_C26_EMNET_2024_DIGITAL_AD_AGENCY_EVENT_CAP_4B", "symbol": "123570", "company_name": "이엠넷", "round": "R8", "loop": "92", "large_sector_id": "L8_PLATFORM_CONTENT_SW_SECURITY", "canonical_archetype_id": "C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE", "fine_archetype_id": "COMMERCE_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE_BRIDGE_VS_DIGITAL_AD_REP_FALSE_STAGE2_AND_AD_AGENCY_EVENT_CAP", "case_type": "event_cap_4b_counterexample", "positive_or_counterexample": "counterexample", "best_trigger": "R8L92_C26_EMNET_2024_STAGE4B_DIGITAL_AD_AGENCY_EVENT_CAP", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "Digital ad-agency / online marketing event premium capped at the March spike and then suffered high MAE. C26 should route bridge-missing ad-agency event premiums to 4B unless advertiser budget, platform traffic, take-rate and margin bridge remain visible.", "current_profile_verdict": "current_profile_4B_too_late_if_digital_ad_agency_event_premium_not_capped", "price_source": "Songdaiki/stock-web", "notes": "Selected 2024 window clean after old 2016/2018 CA candidates. Source-proxy only."}
```

### 25.3 trigger rows

```jsonl
{"row_type": "trigger", "trigger_id": "R8L92_C26_CAFE24_2024_STAGE2_ACTIONABLE_COMMERCE_PLATFORM_AD_REVENUE_LEVERAGE", "case_id": "R8L92_C26_CAFE24_2024_COMMERCE_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE_POSITIVE", "symbol": "042000", "company_name": "카페24", "round": "R8", "loop": "92", "large_sector_id": "L8_PLATFORM_CONTENT_SW_SECURITY", "canonical_archetype_id": "C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE", "fine_archetype_id": "COMMERCE_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE_BRIDGE_VS_DIGITAL_AD_REP_FALSE_STAGE2_AND_AD_AGENCY_EVENT_CAP", "sector": "commerce_platform_ad_revenue_operating_leverage", "primary_archetype": "commerce_platform_GMV_ad_solution_revenue_margin_revision_bridge", "loop_objective": "coverage_gap_fill | counterexample_mining | stage2_actionable_bonus_stress_test | 4B_non_price_requirement_stress_test | high_MAE_guardrail | canonical_archetype_compression", "trigger_type": "Stage2-Actionable", "trigger_date": "2024-05-09", "entry_date": "2024-05-09", "entry_price": 19390.0, "evidence_available_at_that_date": "commerce-platform traffic, creator/YouTube commerce integration, seller GMV, ad/solution revenue and operating-leverage margin/revision bridge proxy; exact as-of source URL pending", "evidence_source": "source_proxy_historical_public_report_proxy", "stage2_evidence_fields": ["platform_traffic_proxy", "GMV_seller_tool_proxy", "ad_solution_revenue_bridge", "operating_leverage_margin_bridge", "relative_strength_reversal"], "stage3_evidence_fields": ["very_high_MFE30", "very_high_MFE90", "controlled_initial_MAE"], "stage4b_evidence_fields": ["later_platform_valuation_watch", "positioning_overheat_watch"], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/042/042000/2024.csv", "profile_path": "atlas/symbol_profiles/042/042000.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": 120.99, "MFE_90D_pct": 121.51, "MFE_180D_pct": 121.51, "MFE_1Y_pct": "not_calculated", "MFE_2Y_pct": "not_calculated", "MAE_30D_pct": -8.77, "MAE_90D_pct": -8.77, "MAE_180D_pct": -8.77, "MAE_1Y_pct": "not_calculated", "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2024-06-26", "peak_price": 42950.0, "drawdown_after_peak_pct": -43.54, "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": null, "four_b_full_window_peak_proximity": null, "four_b_timing_verdict": "positive_stage2_but_later_platform_valuation_4B_watch_needed", "four_b_evidence_type": ["valuation_repricing", "positioning_overheat", "platform_ad_revenue_premium"], "four_c_protection_label": "not_applicable", "trigger_outcome_label": "good_stage2_commerce_platform_ad_revenue_operating_leverage_bridge_success", "current_profile_verdict": "current_profile_kept_but_source_proxy_blocks_positive_delta", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window_after_old_2021_CA", "same_entry_group_id": "R8L92_C26_042000_2024-05-09_19390", "dedupe_for_aggregate": true, "aggregate_group_role": "representative_soft_expansion", "is_new_independent_case": true, "reuse_reason": "soft_expansion_same_C26_symbol_new_entry_date_and_bridge_family", "independent_evidence_weight": 0.75, "do_not_count_as_new_case": false, "evidence_url_pending": true, "source_proxy_only": true}
{"row_type": "trigger", "trigger_id": "R8L92_C26_NASMEDIA_2024_STAGE2_FALSE_POSITIVE_DIGITAL_AD_REP_RECOVERY", "case_id": "R8L92_C26_NASMEDIA_2024_DIGITAL_AD_REP_RECOVERY_FALSE_STAGE2", "symbol": "089600", "company_name": "나스미디어", "round": "R8", "loop": "92", "large_sector_id": "L8_PLATFORM_CONTENT_SW_SECURITY", "canonical_archetype_id": "C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE", "fine_archetype_id": "COMMERCE_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE_BRIDGE_VS_DIGITAL_AD_REP_FALSE_STAGE2_AND_AD_AGENCY_EVENT_CAP", "sector": "digital_ad_rep_recovery_watch", "primary_archetype": "digital_ad_recovery_without_budget_take_rate_margin_bridge", "loop_objective": "coverage_gap_fill | counterexample_mining | stage2_actionable_bonus_stress_test | 4B_non_price_requirement_stress_test | high_MAE_guardrail | canonical_archetype_compression", "trigger_type": "Stage2-Actionable", "trigger_date": "2024-01-24", "entry_date": "2024-01-24", "entry_price": 25350.0, "evidence_available_at_that_date": "digital ad-rep / media sales recovery watch and platform ad-budget rebound proxy; exact as-of source URL pending", "evidence_source": "source_proxy_historical_public_news_proxy", "stage2_evidence_fields": ["digital_ad_recovery_watch", "ad_budget_rebound_expectation", "relative_strength_spike"], "stage3_evidence_fields": [], "stage4b_evidence_fields": ["limited_MFE90", "traffic_budget_margin_bridge_missing", "post_spike_drawdown"], "stage4c_evidence_fields": ["thesis_break_watch_only"], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/089/089600/2024.csv", "profile_path": "atlas/symbol_profiles/089/089600.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": 5.72, "MFE_90D_pct": 5.72, "MFE_180D_pct": 5.72, "MFE_1Y_pct": "not_calculated", "MFE_2Y_pct": "not_calculated", "MAE_30D_pct": -10.45, "MAE_90D_pct": -36.29, "MAE_180D_pct": -40.08, "MAE_1Y_pct": "not_calculated", "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2024-01-24", "peak_price": 26800.0, "drawdown_after_peak_pct": -43.32, "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": 0.95, "four_b_full_window_peak_proximity": 0.95, "four_b_timing_verdict": "digital_ad_recovery_watch_was_false_stage2_due_missing_budget_take_rate_margin_bridge", "four_b_evidence_type": ["digital_ad_recovery_premium", "positioning_overheat", "bridge_missing"], "four_c_protection_label": "thesis_break_watch_only", "trigger_outcome_label": "bad_stage2_digital_ad_recovery_without_budget_take_rate_margin_bridge", "current_profile_verdict": "current_profile_false_positive_if_digital_ad_recovery_counts_without_traffic_budget_margin_revision_bridge", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window_no_CA_candidate", "same_entry_group_id": "R8L92_C26_089600_2024-01-24_25350", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false, "evidence_url_pending": true, "source_proxy_only": true}
{"row_type": "trigger", "trigger_id": "R8L92_C26_EMNET_2024_STAGE4B_DIGITAL_AD_AGENCY_EVENT_CAP", "case_id": "R8L92_C26_EMNET_2024_DIGITAL_AD_AGENCY_EVENT_CAP_4B", "symbol": "123570", "company_name": "이엠넷", "round": "R8", "loop": "92", "large_sector_id": "L8_PLATFORM_CONTENT_SW_SECURITY", "canonical_archetype_id": "C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE", "fine_archetype_id": "COMMERCE_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE_BRIDGE_VS_DIGITAL_AD_REP_FALSE_STAGE2_AND_AD_AGENCY_EVENT_CAP", "sector": "digital_ad_agency_event_premium", "primary_archetype": "digital_ad_agency_event_cap_4B", "loop_objective": "coverage_gap_fill | counterexample_mining | stage2_actionable_bonus_stress_test | 4B_non_price_requirement_stress_test | high_MAE_guardrail | canonical_archetype_compression", "trigger_type": "Stage4B", "trigger_date": "2024-03-06", "entry_date": "2024-03-06", "entry_price": 4800.0, "evidence_available_at_that_date": "digital ad-agency / online marketing event premium after March spike; exact as-of source URL pending", "evidence_source": "source_proxy_historical_public_news_proxy", "stage2_evidence_fields": ["digital_ad_agency_event_premium", "online_marketing_theme", "relative_strength_spike"], "stage3_evidence_fields": [], "stage4b_evidence_fields": ["event_premium_cap", "deep_MAE90", "ad_budget_take_rate_bridge_recheck"], "stage4c_evidence_fields": ["thesis_break_watch_only"], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/123/123570/2024.csv", "profile_path": "atlas/symbol_profiles/123/123570.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": 8.96, "MFE_90D_pct": 8.96, "MFE_180D_pct": 8.96, "MFE_1Y_pct": "not_calculated", "MFE_2Y_pct": "not_calculated", "MAE_30D_pct": -23.54, "MAE_90D_pct": -38.02, "MAE_180D_pct": -50.1, "MAE_1Y_pct": "not_calculated", "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2024-03-06", "peak_price": 5230.0, "drawdown_after_peak_pct": -54.21, "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": 0.92, "four_b_full_window_peak_proximity": 0.92, "four_b_timing_verdict": "good_full_window_4B_timing_digital_ad_agency_event_cap", "four_b_evidence_type": ["digital_ad_agency_premium", "positioning_overheat", "price_only"], "four_c_protection_label": "thesis_break_watch_only", "trigger_outcome_label": "event_cap_4B_success_digital_ad_agency_event_premium", "current_profile_verdict": "current_profile_4B_too_late_if_digital_ad_agency_event_premium_not_capped", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window_after_old_2016_2018_CA", "same_entry_group_id": "R8L92_C26_123570_2024-03-06_4800", "dedupe_for_aggregate": false, "aggregate_group_role": "4B_overlay_only", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false, "evidence_url_pending": true, "source_proxy_only": true}
```

### 25.4 score_simulation rows

```jsonl
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R8L92_C26_CAFE24_2024_COMMERCE_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE_POSITIVE", "trigger_id": "R8L92_C26_CAFE24_2024_STAGE2_ACTIONABLE_COMMERCE_PLATFORM_AD_REVENUE_LEVERAGE", "symbol": "042000", "large_sector_id": "L8_PLATFORM_CONTENT_SW_SECURITY", "canonical_archetype_id": "C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE", "raw_component_scores_before": {"contract_score": 10, "backlog_visibility_score": 25, "margin_bridge_score": 30, "revision_score": 30, "relative_strength_score": 70, "customer_quality_score": 35, "policy_or_regulatory_score": 5, "valuation_repricing_score": 60, "execution_risk_score": 55, "legal_or_contract_risk_score": 20, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_before": 66, "stage_label_before": "Stage2-Watch", "raw_component_scores_after": {"contract_score": 25, "backlog_visibility_score": 50, "margin_bridge_score": 55, "revision_score": 55, "relative_strength_score": 75, "customer_quality_score": 50, "policy_or_regulatory_score": 5, "valuation_repricing_score": 55, "execution_risk_score": 35, "legal_or_contract_risk_score": 15, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_after": 76, "stage_label_after": "Stage2-Actionable", "changed_components": ["backlog_visibility_score", "margin_bridge_score", "revision_score", "relative_strength_score", "customer_quality_score", "valuation_repricing_score", "execution_risk_score"], "component_delta_explanation": "commerce_platform_ad_revenue_operating_leverage_positive", "MFE_90D_pct": 121.51, "MAE_90D_pct": -8.77, "score_return_alignment_label": "commerce_platform_ad_revenue_operating_leverage_positive", "current_profile_verdict": "current_profile_kept_but_source_proxy_blocks_positive_delta"}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R8L92_C26_NASMEDIA_2024_DIGITAL_AD_REP_RECOVERY_FALSE_STAGE2", "trigger_id": "R8L92_C26_NASMEDIA_2024_STAGE2_FALSE_POSITIVE_DIGITAL_AD_REP_RECOVERY", "symbol": "089600", "large_sector_id": "L8_PLATFORM_CONTENT_SW_SECURITY", "canonical_archetype_id": "C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE", "raw_component_scores_before": {"contract_score": 10, "backlog_visibility_score": 25, "margin_bridge_score": 30, "revision_score": 30, "relative_strength_score": 70, "customer_quality_score": 35, "policy_or_regulatory_score": 5, "valuation_repricing_score": 60, "execution_risk_score": 55, "legal_or_contract_risk_score": 20, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_before": 66, "stage_label_before": "Stage2-Actionable", "raw_component_scores_after": {"contract_score": 5, "backlog_visibility_score": 5, "margin_bridge_score": 5, "revision_score": 5, "relative_strength_score": 25, "customer_quality_score": 10, "policy_or_regulatory_score": 5, "valuation_repricing_score": 25, "execution_risk_score": 90, "legal_or_contract_risk_score": 35, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_after": 52, "stage_label_after": "Stage1/Watch", "changed_components": ["backlog_visibility_score", "margin_bridge_score", "revision_score", "relative_strength_score", "customer_quality_score", "valuation_repricing_score", "execution_risk_score"], "component_delta_explanation": "digital_ad_recovery_false_stage2", "MFE_90D_pct": 5.72, "MAE_90D_pct": -36.29, "score_return_alignment_label": "digital_ad_recovery_false_stage2", "current_profile_verdict": "current_profile_false_positive_if_digital_ad_recovery_counts_without_traffic_budget_margin_revision_bridge"}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R8L92_C26_EMNET_2024_DIGITAL_AD_AGENCY_EVENT_CAP_4B", "trigger_id": "R8L92_C26_EMNET_2024_STAGE4B_DIGITAL_AD_AGENCY_EVENT_CAP", "symbol": "123570", "large_sector_id": "L8_PLATFORM_CONTENT_SW_SECURITY", "canonical_archetype_id": "C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE", "raw_component_scores_before": {"contract_score": 10, "backlog_visibility_score": 25, "margin_bridge_score": 30, "revision_score": 30, "relative_strength_score": 70, "customer_quality_score": 35, "policy_or_regulatory_score": 5, "valuation_repricing_score": 60, "execution_risk_score": 55, "legal_or_contract_risk_score": 20, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_before": 70, "stage_label_before": "Stage3-Yellow-like", "raw_component_scores_after": {"contract_score": 5, "backlog_visibility_score": 5, "margin_bridge_score": 5, "revision_score": 5, "relative_strength_score": 25, "customer_quality_score": 10, "policy_or_regulatory_score": 5, "valuation_repricing_score": 25, "execution_risk_score": 90, "legal_or_contract_risk_score": 35, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_after": 54, "stage_label_after": "Stage4B-watch", "changed_components": ["backlog_visibility_score", "margin_bridge_score", "revision_score", "relative_strength_score", "customer_quality_score", "valuation_repricing_score", "execution_risk_score"], "component_delta_explanation": "digital_ad_agency_event_cap_4B_guard", "MFE_90D_pct": 8.96, "MAE_90D_pct": -38.02, "score_return_alignment_label": "digital_ad_agency_event_cap_4B_guard", "current_profile_verdict": "current_profile_4B_too_late_if_digital_ad_agency_event_premium_not_capped"}
```

### 25.5 residual_contribution row

```jsonl
{"row_type": "residual_contribution", "round": "R8", "loop": "92", "large_sector_id": "L8_PLATFORM_CONTENT_SW_SECURITY", "canonical_archetype_id": "C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE", "fine_archetype_id": "COMMERCE_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE_BRIDGE_VS_DIGITAL_AD_REP_FALSE_STAGE2_AND_AD_AGENCY_EVENT_CAP", "new_independent_case_count": 3, "reused_case_count": 0, "new_symbol_count": 2, "same_archetype_new_symbol_count": 2, "same_archetype_new_trigger_family_count": 3, "new_trigger_family_count": 3, "positive_case_count": 1, "counterexample_count": 2, "4B_case_count": 1, "4C_case_count": 0, "tested_existing_calibrated_axes": ["stage2_required_bridge", "local_4b_watch_guard", "full_4b_requires_non_price_evidence", "price_only_blowoff_blocks_positive_stage", "high_MAE_guardrail"], "residual_error_types_found": ["commerce_platform_ad_revenue_operating_leverage_positive", "digital_ad_recovery_false_stage2", "digital_ad_agency_event_cap_4B"], "loop_contribution_label": "canonical_archetype_rule_candidate", "do_not_propose_new_weight_delta": true, "source_proxy_only_count": 3, "evidence_url_pending_count": 3}
```

### 25.6 narrative_only row

```jsonl
{"row_type":"narrative_only","case_id":"none","symbol":"none","large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE","reason":"all selected rows have usable 180D stock-web windows; no narrative-only price row required","price_source":"Songdaiki/stock-web","usage":"not_weight_calibration"}
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
- Soft-expansion rows should receive reduced evidence weight if the symbol already appears in the same archetype.
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
10. Add tests that bridge-missing C26 rows cannot promote positive stages.

### Expected output

- Concise implementation summary.
- Rows accepted/rejected.
- New sector/canonical archetype coverage.
- Existing axis strengthened/weakened/kept.
- No investment recommendation language.

## 27. Next Round State

```text
completed_round = R8
completed_loop = 92
next_round = R9
next_loop = 92
round_schedule_status = valid
round_sector_consistency = pass
```

## 28. Source Notes

- Main execution prompt: Songdaiki/stock_agent docs/core/e2r_v12_prompt_round_scheduler_corrected.txt.
- No-repeat index: Songdaiki/stock_agent docs/core/V12_Research_No_Repeat_Index.md.
- Price atlas: Songdaiki/stock-web atlas/manifest.json and per-symbol tradable shards.
- This file contains no investment recommendation and no production scoring change.
