# E2R Stock-Web Historical Calibration / Sector-Archetype Residual Research Round

## 0. Research Metadata

```text
research_session = post_calibrated_sector_archetype_residual_research
mode = historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12
scheduled_round = R8
scheduled_loop = 99
round_schedule_status = valid
round_sector_consistency = pass
large_sector_id = L8_PLATFORM_CONTENT_SW_SECURITY
canonical_archetype_id = C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE
fine_archetype_id = COMMERCE_PLATFORM_GMV_AD_TAKE_RATE_OPERATING_LEVERAGE_BRIDGE_VS_SEARCH_PORTAL_AD_RECOVERY_FALSE_STAGE2_AND_DIGITAL_ADTECH_EVENT_CAP
loop_objective = priority1_to_50_fill | coverage_gap_fill | counterexample_mining | stage2_actionable_bonus_stress_test | 4B_non_price_requirement_stress_test | platform_ad_revenue_operating_leverage_guardrail | high_MAE_guardrail | canonical_archetype_compression
output_file = e2r_stock_web_v12_residual_round_R8_loop_99_L8_PLATFORM_CONTENT_SW_SECURITY_C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE_research.md
```

This file is the corrected final output for this execution. The scheduler is coverage-index-first. A C25 duplicate path was inspected during this run but is not the final artifact because C25 was already finalized immediately before. Priority 1 already added C03, C16, C04, C05, C15, C18, C20 and C25, so C26 is the next unsupplemented Priority 1 gap below the 50-row practical calibration zone. Since R8 loop97/98 were used locally for C27/C28, this file uses R8 loop99 to avoid local round-loop collision.

## 1. Current Calibrated Profile Assumption

```text
current_default_profile_proxy = e2r_2_2_rolling_calibrated
previous_baseline_reference = e2r_2_1_stock_web_calibrated
production_scoring_changed = false
shadow_weight_only = true
```

Existing axes tested:

```text
stage2_required_bridge = existing_axis_strengthened
local_4b_watch_guard = existing_axis_strengthened
platform_ad_revenue_operating_leverage_guardrail = existing_axis_strengthened
high_MAE_guardrail = existing_axis_strengthened
hard_4c_thesis_break_routes_to_4c = existing_axis_kept
full_4b_requires_non_price_evidence = existing_axis_kept
price_only_blowoff_blocks_positive_stage = existing_axis_kept
```

## 2. Round / Large Sector / Canonical Archetype Scope

```text
scheduled_round = R8
scheduled_loop = 99
large_sector_id = L8_PLATFORM_CONTENT_SW_SECURITY
canonical_archetype_id = C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE
round_sector_consistency = pass
coverage_index_override_previous_round = true
```

C26 is a platform ad-revenue / operating-leverage archetype. Platform traffic is the crowd in the mall; the signal exists only when GMV, ad/solution take-rate, advertiser or merchant retention, margin and revision turn that crowd into operating leverage.

## 3. Previous Coverage / Duplicate Avoidance Check

No-Repeat hard key used:

```text
canonical_archetype_id + symbol + trigger_type + entry_date
```

No-Repeat snapshot context:

```text
C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE = 36 rows / Priority 1
top covered C26 symbols avoided: 067160, 089600, 230360, 123570, 216050, 236810
recent local Priority 0/1 artifacts accounted for: C08, C09, C01, C07, C06, C10, C14, C11, C02, C13, C19, C27, C12, C24, C28, C17, C23, C03, C16, C04, C05, C15, C18, C20, C25
```

Selected rows avoid hard duplicates and add new C26 trigger families:

```text
042000 / Stage2-Actionable / 2024-05-09
035420 / Stage2-Actionable / 2024-01-10
237820 / Stage4B / 2024-02-27
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
| 042000 | atlas/symbol_profiles/042/042000.json | selected 2024 window clean after old 2021 CA candidates |
| 035420 | atlas/symbol_profiles/035/035420.json | selected 2024 window clean after old CA candidates |
| 237820 | atlas/symbol_profiles/237/237820.json | no corporate-action candidate |

## 5. Historical Eligibility Gate

| case_id | symbol | entry_date | entry in shard | forward 180D | OHLC valid | CA clean | calibration_usable |
|---|---|---:|---|---:|---|---|---|
| R8L99_C26_CAFE24_2024_COMMERCE_PLATFORM_GMV_AD_TAKE_RATE_OPERATING_LEVERAGE_POSITIVE | 042000 | 2024-05-09 | yes | 180 | yes | yes | true |
| R8L99_C26_NAVER_2024_SEARCH_PORTAL_AD_RECOVERY_FALSE_STAGE2 | 035420 | 2024-01-10 | yes | 180 | yes | yes | true |
| R8L99_C26_PLAYD_2024_DIGITAL_ADTECH_EVENT_CAP_4B | 237820 | 2024-02-27 | yes | 180 | yes | yes | true |

## 6. Canonical Archetype Compression Map

| canonical | fine/deep split | meaning |
|---|---|---|
| C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE | COMMERCE_PLATFORM_GMV_AD_TAKE_RATE_OPERATING_LEVERAGE_BRIDGE | Positive Stage2 requires GMV/traffic conversion, ad or solution take-rate, operating leverage, margin and revision bridge. |
| C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE | SEARCH_PORTAL_AD_RECOVERY_FALSE_STAGE2 | Search portal ad recovery watch without ad revenue acceleration and operating leverage can become false Stage2. |
| C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE | DIGITAL_ADTECH_EVENT_CAP_4B | Digital adtech event premium should route to 4B when advertiser retention and margin bridge are missing. |

## 7. Case Selection Summary

| case_id | symbol | company | role | selected reason |
|---|---|---|---|---|
| R8L99_C26_CAFE24_2024_COMMERCE_PLATFORM_GMV_AD_TAKE_RATE_OPERATING_LEVERAGE_POSITIVE | 042000 | 카페24 | positive | Commerce-platform GMV/take-rate bridge produced very strong MFE after the May base. |
| R8L99_C26_NAVER_2024_SEARCH_PORTAL_AD_RECOVERY_FALSE_STAGE2 | 035420 | NAVER | counterexample | Search/ad recovery watch had tiny MFE and persistent MAE without ad-revenue operating-leverage bridge. |
| R8L99_C26_PLAYD_2024_DIGITAL_ADTECH_EVENT_CAP_4B | 237820 | 플레이디 | counterexample / 4B | Digital adtech premium capped after the February-March spike and then de-rated sharply. |

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
| Cafe24 commerce platform GMV/ad take-rate bridge | historical public/report proxy | true | true | shadow-only positive |
| NAVER search portal ad recovery false Stage2 | historical public/news proxy | true | true | false-Stage2 guardrail |
| PlayD digital adtech event cap | historical public/news proxy | true | true | 4B overlay counterexample |

## 10. Price Data Source Map

| symbol | shard | profile |
|---|---|---|
| 042000 | atlas/ohlcv_tradable_by_symbol_year/042/042000/2024.csv | atlas/symbol_profiles/042/042000.json |
| 035420 | atlas/ohlcv_tradable_by_symbol_year/035/035420/2024.csv | atlas/symbol_profiles/035/035420.json |
| 237820 | atlas/ohlcv_tradable_by_symbol_year/237/237820/2024.csv | atlas/symbol_profiles/237/237820.json |

## 11. Case-by-Case Trigger Grid

| trigger_id | symbol | trigger_type | entry_date | entry_price | role | verdict |
|---|---|---|---:|---:|---|---|
| R8L99_C26_CAFE24_2024_STAGE2_ACTIONABLE_COMMERCE_PLATFORM_GMV_AD_TAKE_RATE_OPERATING_LEVERAGE | 042000 | Stage2-Actionable | 2024-05-09 | 19390 | positive | GMV/take-rate operating leverage bridge worked |
| R8L99_C26_NAVER_2024_STAGE2_FALSE_POSITIVE_SEARCH_PORTAL_AD_RECOVERY_WATCH | 035420 | Stage2-Actionable | 2024-01-10 | 231000 | counterexample | search/ad recovery false Stage2 |
| R8L99_C26_PLAYD_2024_STAGE4B_DIGITAL_ADTECH_EVENT_CAP | 237820 | Stage4B | 2024-02-27 | 8900 | counterexample/4B | digital adtech event cap |

## 12. Trigger-Level OHLC Backtest Tables

| trigger_id | entry | MFE30 | MAE30 | MFE90 | MAE90 | MFE180 | MAE180 | peak_date | peak_price | drawdown_after_peak |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| R8L99_C26_CAFE24_2024_STAGE2_ACTIONABLE_COMMERCE_PLATFORM_GMV_AD_TAKE_RATE_OPERATING_LEVERAGE | 19390 | 121.00 | -8.77 | 121.51 | -8.77 | 121.51 | -8.77 | 2024-06-26 | 42950 | -36.09 |
| R8L99_C26_NAVER_2024_STAGE2_FALSE_POSITIVE_SEARCH_PORTAL_AD_RECOVERY_WATCH | 231000 | 1.95 | -13.20 | 1.95 | -21.17 | 1.95 | -31.60 | 2024-01-16 | 235500 | -32.91 |
| R8L99_C26_PLAYD_2024_STAGE4B_DIGITAL_ADTECH_EVENT_CAP | 8900 | 19.78 | -21.24 | 19.78 | -40.34 | 19.78 | -40.34 | 2024-03-06 | 10660 | -50.19 |

## 13. Current Calibrated Profile Stress Test

| axis | outcome |
|---|---|
| stage2_required_bridge | strengthen: C26 Stage2 needs GMV/traffic conversion, ad/take-rate, repeat advertiser or merchant demand, operating leverage, margin and revision bridge |
| platform_ad_revenue_operating_leverage_guardrail | strengthen: platform/ad/AI-search label alone cannot promote positive stage |
| local_4b_watch_guard | strengthen: bridge-missing search portal and digital-adtech premiums should route to 4B watch |
| high_MAE_guardrail | strengthen: high-MAE C26 rows cannot promote without durable ad revenue or operating leverage bridge |
| hard_4c_thesis_break_routes_to_4c | keep |
| full_4b_requires_non_price_evidence | keep |
| price_only_blowoff_blocks_positive_stage | keep |

## 14. Stage2 / Yellow / Green / 4B Comparison

No confirmed Stage3-Green row is introduced. The useful split is whether platform traffic becomes GMV, take-rate, advertiser/merchant retention and margin evidence.

| symbol | stage quality | explanation |
|---|---|---|
| 042000 | good_stage2_with_later_watch | GMV/take-rate operating-leverage bridge produced very strong MFE, but later platform valuation watch remains necessary. |
| 035420 | bad_stage2 | Search/ad recovery watch lacked ad-revenue acceleration and operating leverage, producing tiny MFE with persistent drawdown. |
| 237820 | good_4B | Digital adtech event premium peaked quickly and later de-rated without client-retention/margin bridge. |

```text
green_lateness_ratio = not_applicable
reason = no confirmed Stage3-Green trigger
```

## 15. 4B Local vs Full-window Timing Audit

| trigger | local proximity | full-window proximity | timing verdict |
|---|---:|---:|---|
| 035420 search portal false Stage2 | 0.98 | 0.98 | false Stage2 due missing ad revenue / operating leverage / revision bridge |
| 237820 digital adtech event cap | 0.83 | 0.83 | good 4B timing after digital adtech event premium |
| 042000 commerce platform bridge | n/a | n/a | positive Stage2, but later platform valuation watch required |

## 16. 4C Protection Audit

```text
4C_case_count = 0
four_c_protection_label = ad_revenue_revision_break_watch_only for 035420
four_c_protection_label = ad_budget_reversal_watch_only for 237820
```

No hard 4C candidate is introduced in this C26 file. The counterexamples are bridge-missing / event-cap rows, not confirmed thesis-break rows.

## 17. Sector-Specific Rule Candidate

```text
sector_specific_rule_candidate = true
rule_scope = sector_specific
rule = In L8 platform/ad revenue operating-leverage cases, Stage2 requires verified GMV or traffic conversion, ad/solution take-rate, advertiser or merchant retention, operating leverage, margin and revision bridge. Platform, adtech, AI search, portal traffic, creator commerce or relative-strength label alone remains watch/4B.
proposal_status = shadow_only
```

## 18. Canonical-Archetype Rule Candidate

```text
canonical_archetype_rule_candidate = true
canonical_archetype_id = C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE
rule = C26 should split true GMV/ad take-rate operating-leverage positives from search-portal false Stage2 and digital-adtech event caps. Event-cap rows are 4B overlay/risk calibration, not Stage3-Green promotion evidence.
proposal_status = shadow_only_not_production
```

## 19. Before / After Backtest Comparison

| profile | hypothesis | eligible triggers | avg_MFE90 | avg_MAE90 | false_positive_or_guardrail_rate | verdict |
|---|---|---:|---:|---:|---:|---|
| P0 e2r_2_2_rolling_calibrated_proxy | current profile | 3 | 47.75 | -23.43 | 0.67 | mixed; C26 operating-leverage bridge split needed |
| P0b e2r_2_1_stock_web_calibrated_reference | older calibrated baseline | 3 | 47.75 | -23.43 | 0.67 | weaker C26 bridge split |
| P1 sector_specific_candidate_profile | L8 GMV/ad-revenue operating leverage bridge required | 2 | 61.73 | -14.97 | 0.50 | better |
| P2 canonical_archetype_candidate_profile | C26 bridge vs event-cap split | 2 | 61.73 | -14.97 | 0.50 | best explanatory fit |
| P3 counterexample_guard_profile | reject bridge-missing platform/ad themes as positive | 1 | 121.51 | -8.77 | 0.00 | safest but source-proxy blockers remain |

## 20. Score-Return Alignment Matrix

| trigger | score before | stage before | score after | stage after | MFE90 | MAE90 | alignment |
|---|---:|---|---:|---|---:|---:|---|
| 042000 commerce platform bridge | 66 | Stage2-Watch | 82 | Stage2-Actionable | 121.51 | -8.77 | platform_ad_revenue_operating_leverage_positive |
| 035420 search portal false | 66 | Stage2-Actionable | 52 | Stage1/Watch | 1.95 | -21.17 | search_portal_false_stage2 |
| 237820 digital adtech cap | 70 | Stage3-Yellow-like | 54 | Stage4B-watch | 19.78 | -40.34 | digital_adtech_event_cap_4B_guard |

## 21. Coverage Matrix

```jsonl
{"row_type": "coverage_matrix", "large_sector_id": "L8_PLATFORM_CONTENT_SW_SECURITY", "canonical_archetype_id": "C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE", "fine_archetype_id": "COMMERCE_PLATFORM_GMV_AD_TAKE_RATE_OPERATING_LEVERAGE_BRIDGE_VS_SEARCH_PORTAL_AD_RECOVERY_FALSE_STAGE2_AND_DIGITAL_ADTECH_EVENT_CAP", "positive_case_count": 1, "counterexample_count": 2, "4B_case_count": 1, "4C_case_count": 0, "new_independent_case_count": 3, "reused_case_count": 0, "calibration_usable_trigger_count": 3, "representative_trigger_count": 2, "current_profile_error_count": 2, "sector_rule_candidate": true, "canonical_rule_candidate": true, "coverage_gap_after_this_loop": "C26 is the next unsupplemented Priority 1 archetype after C03/C16/C04/C05/C15/C18/C20/C25 and remains below the practical 50-row calibration zone. This run adds Cafe24, NAVER and PlayD while avoiding top-covered C26 symbols 067160, 089600, 230360, 123570, 216050 and 236810."}
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
tested_existing_calibrated_axes: stage2_required_bridge, local_4b_watch_guard, platform_ad_revenue_operating_leverage_guardrail, high_MAE_guardrail, hard_4c_thesis_break_routes_to_4c, full_4b_requires_non_price_evidence, price_only_blowoff_blocks_positive_stage
residual_error_types_found: platform_ad_revenue_operating_leverage_positive, search_portal_false_stage2, digital_adtech_event_cap_4B
new_axis_proposed: null
existing_axis_strengthened: stage2_required_bridge, local_4b_watch_guard, platform_ad_revenue_operating_leverage_guardrail, high_MAE_guardrail
existing_axis_weakened: null
existing_axis_kept: full_4b_requires_non_price_evidence, price_only_blowoff_blocks_positive_stage, hard_4c_thesis_break_routes_to_4c
sector_specific_rule_candidate: true
canonical_archetype_rule_candidate: true
no_new_signal_reason: null
loop_contribution_label: priority1_canonical_archetype_rule_candidate
do_not_propose_new_weight_delta: true
```

## 23. Validation Scope / Non-Validation Scope

Validation scope:

```text
- Stock-web tradable raw OHLC path
- entry_date / entry_price
- MFE/MAE 30D/90D/180D
- corporate-action window cleanliness
- C26 platform ad-revenue operating-leverage bridge vs false Stage2 / event-cap split
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
shadow_weight,stage2_required_bridge,canonical_archetype,L8_PLATFORM_CONTENT_SW_SECURITY,C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE,configured,C26_requires_GMV_take_rate_ad_revenue_operating_leverage_margin_revision_bridge,0,"C26 Stage2 should require GMV/traffic conversion, ad or solution take-rate, repeat advertiser/merchant demand, operating leverage, margin and revision bridge, not platform/ad/AI-search label alone","Cafe24 positive worked; NAVER and PlayD event/watch rows failed positive-stage promotion","R8L99_C26_CAFE24_2024_STAGE2_ACTIONABLE_COMMERCE_PLATFORM_GMV_AD_TAKE_RATE_OPERATING_LEVERAGE|R8L99_C26_NAVER_2024_STAGE2_FALSE_POSITIVE_SEARCH_PORTAL_AD_RECOVERY_WATCH|R8L99_C26_PLAYD_2024_STAGE4B_DIGITAL_ADTECH_EVENT_CAP",3,3,2,low,canonical_shadow_only,"do_not_propose_new_weight_delta=true because source-proxy/evidence-url-pending rows remain"
shadow_weight,local_4b_watch_guard,canonical_archetype,L8_PLATFORM_CONTENT_SW_SECURITY,C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE,configured,cap_bridge_missing_search_portal_and_digital_adtech_event_premiums_as_4B_watch,0,"Search portal and digital adtech premiums can peak before ad revenue acceleration, client retention and operating leverage bridge is proven","NAVER had tiny MFE and persistent MAE after January ad-recovery watch; PlayD showed 4B event-cap behavior after February-March adtech premium","R8L99_C26_NAVER_2024_STAGE2_FALSE_POSITIVE_SEARCH_PORTAL_AD_RECOVERY_WATCH|R8L99_C26_PLAYD_2024_STAGE4B_DIGITAL_ADTECH_EVENT_CAP",2,2,2,medium,guardrail_shadow_only,"4B overlay only; not production"
shadow_weight,high_MAE_guardrail,canonical_archetype,L8_PLATFORM_CONTENT_SW_SECURITY,C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE,configured,block_positive_stage_when_platform_ad_theme_has_high_or_persistent_MAE_without_operating_leverage_bridge,0,"High or persistent MAE after bridge-missing C26 entries should block Stage2/Stage3 promotion unless GMV/ad revenue, client retention, operating leverage and margin evidence survives","NAVER MAE90=-21.17 and PlayD MAE90=-40.34","R8L99_C26_NAVER_2024_STAGE2_FALSE_POSITIVE_SEARCH_PORTAL_AD_RECOVERY_WATCH|R8L99_C26_PLAYD_2024_STAGE4B_DIGITAL_ADTECH_EVENT_CAP",2,2,2,medium,guardrail_shadow_only,"canonical shadow profile only"
```

## 25. Machine-Readable Rows

### 25.1 price_source_validation

```jsonl
{"row_type": "price_source_validation", "source": "Songdaiki/stock-web", "source_url": "https://github.com/Songdaiki/stock-web", "manifest_path": "atlas/manifest.json", "schema_path": "atlas/schema.json", "universe_path": "atlas/universe/all_symbols.csv", "manifest_max_date": "2026-02-20", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "raw_shard_root": "atlas/ohlcv_raw_by_symbol_year", "validation_status": "usable_for_historical_calibration", "source_name": "FinanceData/marcap", "tradable_row_count": 14354401, "raw_row_count": 15214118, "symbol_count": 5414, "active_like_symbol_count": 2868, "inactive_or_delisted_like_symbol_count": 2546}
```

### 25.2 case rows

```jsonl
{"row_type": "case", "case_id": "R8L99_C26_CAFE24_2024_COMMERCE_PLATFORM_GMV_AD_TAKE_RATE_OPERATING_LEVERAGE_POSITIVE", "symbol": "042000", "company_name": "카페24", "round": "R8", "loop": "99", "large_sector_id": "L8_PLATFORM_CONTENT_SW_SECURITY", "canonical_archetype_id": "C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE", "fine_archetype_id": "COMMERCE_PLATFORM_GMV_AD_TAKE_RATE_OPERATING_LEVERAGE_BRIDGE_VS_SEARCH_PORTAL_AD_RECOVERY_FALSE_STAGE2_AND_DIGITAL_ADTECH_EVENT_CAP", "case_type": "structural_success_with_later_platform_valuation_watch", "positive_or_counterexample": "positive", "best_trigger": "R8L99_C26_CAFE24_2024_STAGE2_ACTIONABLE_COMMERCE_PLATFORM_GMV_AD_TAKE_RATE_OPERATING_LEVERAGE", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "Commerce platform / GMV / ad-take-rate and operating leverage bridge produced very strong 30D/90D MFE after the May platform-commerce rerating base. C26 works when platform traffic is tied to merchant GMV, ad/solution take-rate, conversion data, operating leverage, margin and revision bridge.", "current_profile_verdict": "current_profile_kept_but_C26_positive_requires_GMV_take_rate_ad_revenue_operating_leverage_margin_revision_bridge_not_platform_label_only", "price_source": "Songdaiki/stock-web", "notes": "Selected 2024 window clean after old 2021 CA candidates. Source-proxy only, so no production weight delta."}
{"row_type": "case", "case_id": "R8L99_C26_NAVER_2024_SEARCH_PORTAL_AD_RECOVERY_FALSE_STAGE2", "symbol": "035420", "company_name": "NAVER", "round": "R8", "loop": "99", "large_sector_id": "L8_PLATFORM_CONTENT_SW_SECURITY", "canonical_archetype_id": "C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE", "fine_archetype_id": "COMMERCE_PLATFORM_GMV_AD_TAKE_RATE_OPERATING_LEVERAGE_BRIDGE_VS_SEARCH_PORTAL_AD_RECOVERY_FALSE_STAGE2_AND_DIGITAL_ADTECH_EVENT_CAP", "case_type": "failed_rerating_search_portal_ad_recovery_bridge_missing", "positive_or_counterexample": "counterexample", "best_trigger": "R8L99_C26_NAVER_2024_STAGE2_FALSE_POSITIVE_SEARCH_PORTAL_AD_RECOVERY_WATCH", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "Search portal / platform ad recovery watch at the January high had tiny MFE and persistent MAE. C26 Stage2 should not be awarded without ad revenue re-acceleration, commerce/GMV conversion, AI/search monetization, operating leverage, margin and revision bridge.", "current_profile_verdict": "current_profile_false_positive_if_search_portal_ad_recovery_watch_counts_without_ad_revenue_operating_leverage_revision_bridge", "price_source": "Songdaiki/stock-web", "notes": "Selected 2024 window clean after old corporate-action candidates. Source-proxy only."}
{"row_type": "case", "case_id": "R8L99_C26_PLAYD_2024_DIGITAL_ADTECH_EVENT_CAP_4B", "symbol": "237820", "company_name": "플레이디", "round": "R8", "loop": "99", "large_sector_id": "L8_PLATFORM_CONTENT_SW_SECURITY", "canonical_archetype_id": "C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE", "fine_archetype_id": "COMMERCE_PLATFORM_GMV_AD_TAKE_RATE_OPERATING_LEVERAGE_BRIDGE_VS_SEARCH_PORTAL_AD_RECOVERY_FALSE_STAGE2_AND_DIGITAL_ADTECH_EVENT_CAP", "case_type": "event_cap_4b_counterexample", "positive_or_counterexample": "counterexample", "best_trigger": "R8L99_C26_PLAYD_2024_STAGE4B_DIGITAL_ADTECH_EVENT_CAP", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "Digital adtech / performance marketing event premium capped after the February-March spike and then de-rated. C26 should route bridge-missing adtech event premiums to 4B unless repeat advertiser budget, ROAS proof, client retention, gross-margin leverage and revision bridge remain visible.", "current_profile_verdict": "current_profile_4B_too_late_if_digital_adtech_event_premium_not_capped", "price_source": "Songdaiki/stock-web", "notes": "No corporate-action candidate in profile. Source-proxy only."}
```

### 25.3 trigger rows

```jsonl
{"row_type": "trigger", "trigger_id": "R8L99_C26_CAFE24_2024_STAGE2_ACTIONABLE_COMMERCE_PLATFORM_GMV_AD_TAKE_RATE_OPERATING_LEVERAGE", "case_id": "R8L99_C26_CAFE24_2024_COMMERCE_PLATFORM_GMV_AD_TAKE_RATE_OPERATING_LEVERAGE_POSITIVE", "symbol": "042000", "company_name": "카페24", "round": "R8", "loop": "99", "large_sector_id": "L8_PLATFORM_CONTENT_SW_SECURITY", "canonical_archetype_id": "C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE", "fine_archetype_id": "COMMERCE_PLATFORM_GMV_AD_TAKE_RATE_OPERATING_LEVERAGE_BRIDGE_VS_SEARCH_PORTAL_AD_RECOVERY_FALSE_STAGE2_AND_DIGITAL_ADTECH_EVENT_CAP", "sector": "commerce_platform_GMV_ad_take_rate_operating_leverage", "primary_archetype": "GMV_take_rate_ad_revenue_operating_leverage_margin_revision_bridge", "loop_objective": "priority1_to_50_fill | coverage_gap_fill | counterexample_mining | stage2_actionable_bonus_stress_test | 4B_non_price_requirement_stress_test | platform_ad_revenue_operating_leverage_guardrail | high_MAE_guardrail | canonical_archetype_compression", "trigger_type": "Stage2-Actionable", "trigger_date": "2024-05-09", "entry_date": "2024-05-09", "entry_price": 19390.0, "evidence_available_at_that_date": "commerce platform / creator-commerce and merchant GMV rerating, ad/solution take-rate, traffic conversion and operating-leverage margin/revision bridge proxy after May breakout; exact as-of source URL pending", "evidence_source": "source_proxy_historical_public_report_proxy", "stage2_evidence_fields": ["GMV_proxy", "merchant_solution_take_rate_proxy", "ad_revenue_proxy", "traffic_conversion_proxy", "operating_leverage_revision_bridge_proxy"], "stage3_evidence_fields": ["very_strong_MFE30", "very_strong_MFE90", "controlled_initial_MAE"], "stage4b_evidence_fields": ["later_platform_valuation_watch", "post_peak_recheck"], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/042/042000/2024.csv", "profile_path": "atlas/symbol_profiles/042/042000.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": 121.0, "MFE_90D_pct": 121.51, "MFE_180D_pct": 121.51, "MFE_1Y_pct": "not_calculated", "MFE_2Y_pct": "not_calculated", "MAE_30D_pct": -8.77, "MAE_90D_pct": -8.77, "MAE_180D_pct": -8.77, "MAE_1Y_pct": "not_calculated", "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2024-06-26", "peak_price": 42950.0, "drawdown_after_peak_pct": -36.09, "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": null, "four_b_full_window_peak_proximity": null, "four_b_timing_verdict": "positive_stage2_but_later_platform_valuation_4B_watch_needed", "four_b_evidence_type": ["platform_revenue_leverage_bridge", "GMV_take_rate", "valuation_watch"], "four_c_protection_label": "not_applicable", "trigger_outcome_label": "good_stage2_commerce_platform_ad_take_rate_operating_leverage_success", "current_profile_verdict": "current_profile_kept_but_source_proxy_blocks_positive_delta", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window_after_old_2021_CA", "same_entry_group_id": "R8L99_C26_042000_2024-05-09_19390", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false, "evidence_url_pending": true, "source_proxy_only": true}
{"row_type": "trigger", "trigger_id": "R8L99_C26_NAVER_2024_STAGE2_FALSE_POSITIVE_SEARCH_PORTAL_AD_RECOVERY_WATCH", "case_id": "R8L99_C26_NAVER_2024_SEARCH_PORTAL_AD_RECOVERY_FALSE_STAGE2", "symbol": "035420", "company_name": "NAVER", "round": "R8", "loop": "99", "large_sector_id": "L8_PLATFORM_CONTENT_SW_SECURITY", "canonical_archetype_id": "C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE", "fine_archetype_id": "COMMERCE_PLATFORM_GMV_AD_TAKE_RATE_OPERATING_LEVERAGE_BRIDGE_VS_SEARCH_PORTAL_AD_RECOVERY_FALSE_STAGE2_AND_DIGITAL_ADTECH_EVENT_CAP", "sector": "search_portal_ad_revenue_recovery_watch", "primary_archetype": "search_portal_ad_watch_without_ad_revenue_operating_leverage_revision_bridge", "loop_objective": "priority1_to_50_fill | coverage_gap_fill | counterexample_mining | stage2_actionable_bonus_stress_test | 4B_non_price_requirement_stress_test | platform_ad_revenue_operating_leverage_guardrail | high_MAE_guardrail | canonical_archetype_compression", "trigger_type": "Stage2-Actionable", "trigger_date": "2024-01-10", "entry_date": "2024-01-10", "entry_price": 231000.0, "evidence_available_at_that_date": "search portal / platform ad recovery watch without confirmed ad revenue acceleration, commerce conversion, AI-search monetization, margin leverage or revision bridge; exact as-of source URL pending", "evidence_source": "source_proxy_historical_public_news_proxy", "stage2_evidence_fields": ["search_ad_recovery_watch", "AI_search_theme", "platform_beta"], "stage3_evidence_fields": [], "stage4b_evidence_fields": ["tiny_MFE90", "persistent_MAE90", "ad_revenue_operating_leverage_bridge_missing"], "stage4c_evidence_fields": ["ad_revenue_revision_break_watch_only"], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/035/035420/2024.csv", "profile_path": "atlas/symbol_profiles/035/035420.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": 1.95, "MFE_90D_pct": 1.95, "MFE_180D_pct": 1.95, "MFE_1Y_pct": "not_calculated", "MFE_2Y_pct": "not_calculated", "MAE_30D_pct": -13.2, "MAE_90D_pct": -21.17, "MAE_180D_pct": -31.6, "MAE_1Y_pct": "not_calculated", "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2024-01-16", "peak_price": 235500.0, "drawdown_after_peak_pct": -32.91, "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": 0.98, "four_b_full_window_peak_proximity": 0.98, "four_b_timing_verdict": "search_portal_ad_recovery_watch_was_false_stage2_due_missing_ad_revenue_operating_leverage_revision_bridge", "four_b_evidence_type": ["search_ad_recovery_premium", "bridge_missing", "tiny_MFE_high_MAE"], "four_c_protection_label": "ad_revenue_revision_break_watch_only", "trigger_outcome_label": "bad_stage2_search_portal_ad_recovery_without_operating_leverage_bridge", "current_profile_verdict": "current_profile_false_positive_if_search_portal_ad_recovery_watch_counts_without_ad_revenue_operating_leverage_revision_bridge", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window_after_old_CA_candidates", "same_entry_group_id": "R8L99_C26_035420_2024-01-10_231000", "dedupe_for_aggregate": true, "aggregate_group_role": "representative_false_stage2", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false, "evidence_url_pending": true, "source_proxy_only": true}
{"row_type": "trigger", "trigger_id": "R8L99_C26_PLAYD_2024_STAGE4B_DIGITAL_ADTECH_EVENT_CAP", "case_id": "R8L99_C26_PLAYD_2024_DIGITAL_ADTECH_EVENT_CAP_4B", "symbol": "237820", "company_name": "플레이디", "round": "R8", "loop": "99", "large_sector_id": "L8_PLATFORM_CONTENT_SW_SECURITY", "canonical_archetype_id": "C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE", "fine_archetype_id": "COMMERCE_PLATFORM_GMV_AD_TAKE_RATE_OPERATING_LEVERAGE_BRIDGE_VS_SEARCH_PORTAL_AD_RECOVERY_FALSE_STAGE2_AND_DIGITAL_ADTECH_EVENT_CAP", "sector": "digital_adtech_performance_marketing_event_premium", "primary_archetype": "digital_adtech_event_cap_4B", "loop_objective": "priority1_to_50_fill | coverage_gap_fill | counterexample_mining | stage2_actionable_bonus_stress_test | 4B_non_price_requirement_stress_test | platform_ad_revenue_operating_leverage_guardrail | high_MAE_guardrail | canonical_archetype_compression", "trigger_type": "Stage4B", "trigger_date": "2024-02-27", "entry_date": "2024-02-27", "entry_price": 8900.0, "evidence_available_at_that_date": "digital adtech / performance marketing event premium without confirmed repeat advertiser budget, ROAS proof, client retention, take-rate, margin or revision bridge; exact as-of source URL pending", "evidence_source": "source_proxy_historical_public_news_proxy", "stage2_evidence_fields": ["digital_adtech_event", "performance_marketing_theme", "relative_strength_spike"], "stage3_evidence_fields": [], "stage4b_evidence_fields": ["event_premium_cap", "high_MAE90", "client_retention_margin_bridge_recheck"], "stage4c_evidence_fields": ["ad_budget_reversal_watch_only"], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/237/237820/2024.csv", "profile_path": "atlas/symbol_profiles/237/237820.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": 19.78, "MFE_90D_pct": 19.78, "MFE_180D_pct": 19.78, "MFE_1Y_pct": "not_calculated", "MFE_2Y_pct": "not_calculated", "MAE_30D_pct": -21.24, "MAE_90D_pct": -40.34, "MAE_180D_pct": -40.34, "MAE_1Y_pct": "not_calculated", "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2024-03-06", "peak_price": 10660.0, "drawdown_after_peak_pct": -50.19, "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": 0.83, "four_b_full_window_peak_proximity": 0.83, "four_b_timing_verdict": "good_full_window_4B_timing_digital_adtech_event_cap_due_missing_client_retention_margin_bridge", "four_b_evidence_type": ["digital_adtech_event_premium", "positioning_overheat", "bridge_missing"], "four_c_protection_label": "ad_budget_reversal_watch_only", "trigger_outcome_label": "event_cap_4B_success_digital_adtech_event_premium", "current_profile_verdict": "current_profile_4B_too_late_if_digital_adtech_event_premium_not_capped", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window_no_CA_candidate", "same_entry_group_id": "R8L99_C26_237820_2024-02-27_8900", "dedupe_for_aggregate": false, "aggregate_group_role": "4B_overlay_only", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false, "evidence_url_pending": true, "source_proxy_only": true}
```

### 25.4 score_simulation rows

```jsonl
{"row_type": "score_simulation", "profile_id": "e2r_2_2_rolling_calibrated_proxy", "case_id": "R8L99_C26_CAFE24_2024_COMMERCE_PLATFORM_GMV_AD_TAKE_RATE_OPERATING_LEVERAGE_POSITIVE", "trigger_id": "R8L99_C26_CAFE24_2024_STAGE2_ACTIONABLE_COMMERCE_PLATFORM_GMV_AD_TAKE_RATE_OPERATING_LEVERAGE", "symbol": "042000", "large_sector_id": "L8_PLATFORM_CONTENT_SW_SECURITY", "canonical_archetype_id": "C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE", "raw_component_scores_before": {"contract_score": 20, "backlog_visibility_score": 30, "margin_bridge_score": 35, "revision_score": 35, "relative_strength_score": 70, "customer_quality_score": 45, "policy_or_regulatory_score": 20, "valuation_repricing_score": 60, "execution_risk_score": 55, "legal_or_contract_risk_score": 30, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 5}, "weighted_score_before": 66, "stage_label_before": "Stage2-Watch", "raw_component_scores_after": {"contract_score": 55, "backlog_visibility_score": 60, "margin_bridge_score": 65, "revision_score": 65, "relative_strength_score": 85, "customer_quality_score": 60, "policy_or_regulatory_score": 25, "valuation_repricing_score": 45, "execution_risk_score": 35, "legal_or_contract_risk_score": 20, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_after": 82, "stage_label_after": "Stage2-Actionable", "changed_components": ["contract_score", "backlog_visibility_score", "margin_bridge_score", "revision_score", "relative_strength_score", "customer_quality_score", "valuation_repricing_score", "execution_risk_score"], "component_delta_explanation": "commerce_platform_GMV_ad_take_rate_positive", "MFE_90D_pct": 121.51, "MAE_90D_pct": -8.77, "score_return_alignment_label": "platform_ad_revenue_operating_leverage_positive", "current_profile_verdict": "current_profile_kept_but_source_proxy_blocks_positive_delta"}
{"row_type": "score_simulation", "profile_id": "e2r_2_2_rolling_calibrated_proxy", "case_id": "R8L99_C26_NAVER_2024_SEARCH_PORTAL_AD_RECOVERY_FALSE_STAGE2", "trigger_id": "R8L99_C26_NAVER_2024_STAGE2_FALSE_POSITIVE_SEARCH_PORTAL_AD_RECOVERY_WATCH", "symbol": "035420", "large_sector_id": "L8_PLATFORM_CONTENT_SW_SECURITY", "canonical_archetype_id": "C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE", "raw_component_scores_before": {"contract_score": 20, "backlog_visibility_score": 25, "margin_bridge_score": 25, "revision_score": 25, "relative_strength_score": 55, "customer_quality_score": 40, "policy_or_regulatory_score": 20, "valuation_repricing_score": 55, "execution_risk_score": 60, "legal_or_contract_risk_score": 35, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 5}, "weighted_score_before": 66, "stage_label_before": "Stage2-Actionable", "raw_component_scores_after": {"contract_score": 5, "backlog_visibility_score": 5, "margin_bridge_score": 5, "revision_score": 5, "relative_strength_score": 15, "customer_quality_score": 15, "policy_or_regulatory_score": 10, "valuation_repricing_score": 25, "execution_risk_score": 85, "legal_or_contract_risk_score": 50, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 10}, "weighted_score_after": 52, "stage_label_after": "Stage1/Watch", "changed_components": ["backlog_visibility_score", "margin_bridge_score", "revision_score", "relative_strength_score", "valuation_repricing_score", "execution_risk_score"], "component_delta_explanation": "search_portal_ad_recovery_false_stage2", "MFE_90D_pct": 1.95, "MAE_90D_pct": -21.17, "score_return_alignment_label": "search_portal_false_stage2", "current_profile_verdict": "current_profile_false_positive_if_search_portal_ad_recovery_watch_counts_without_ad_revenue_operating_leverage_revision_bridge"}
{"row_type": "score_simulation", "profile_id": "e2r_2_2_rolling_calibrated_proxy", "case_id": "R8L99_C26_PLAYD_2024_DIGITAL_ADTECH_EVENT_CAP_4B", "trigger_id": "R8L99_C26_PLAYD_2024_STAGE4B_DIGITAL_ADTECH_EVENT_CAP", "symbol": "237820", "large_sector_id": "L8_PLATFORM_CONTENT_SW_SECURITY", "canonical_archetype_id": "C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE", "raw_component_scores_before": {"contract_score": 10, "backlog_visibility_score": 20, "margin_bridge_score": 20, "revision_score": 20, "relative_strength_score": 75, "customer_quality_score": 20, "policy_or_regulatory_score": 10, "valuation_repricing_score": 60, "execution_risk_score": 65, "legal_or_contract_risk_score": 35, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 5}, "weighted_score_before": 70, "stage_label_before": "Stage3-Yellow-like", "raw_component_scores_after": {"contract_score": 5, "backlog_visibility_score": 5, "margin_bridge_score": 0, "revision_score": 5, "relative_strength_score": 20, "customer_quality_score": 5, "policy_or_regulatory_score": 5, "valuation_repricing_score": 25, "execution_risk_score": 90, "legal_or_contract_risk_score": 55, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 10}, "weighted_score_after": 54, "stage_label_after": "Stage4B-watch", "changed_components": ["backlog_visibility_score", "margin_bridge_score", "revision_score", "relative_strength_score", "valuation_repricing_score", "execution_risk_score"], "component_delta_explanation": "digital_adtech_event_cap_4B_guard", "MFE_90D_pct": 19.78, "MAE_90D_pct": -40.34, "score_return_alignment_label": "digital_adtech_event_cap_4B_guard", "current_profile_verdict": "current_profile_4B_too_late_if_digital_adtech_event_premium_not_capped"}
```

### 25.5 residual_contribution row

```jsonl
{"row_type": "residual_contribution", "round": "R8", "loop": "99", "large_sector_id": "L8_PLATFORM_CONTENT_SW_SECURITY", "canonical_archetype_id": "C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE", "fine_archetype_id": "COMMERCE_PLATFORM_GMV_AD_TAKE_RATE_OPERATING_LEVERAGE_BRIDGE_VS_SEARCH_PORTAL_AD_RECOVERY_FALSE_STAGE2_AND_DIGITAL_ADTECH_EVENT_CAP", "new_independent_case_count": 3, "reused_case_count": 0, "new_symbol_count": 3, "same_archetype_new_symbol_count": 3, "same_archetype_new_trigger_family_count": 3, "new_trigger_family_count": 3, "positive_case_count": 1, "counterexample_count": 2, "4B_case_count": 1, "4C_case_count": 0, "tested_existing_calibrated_axes": ["stage2_required_bridge", "local_4b_watch_guard", "platform_ad_revenue_operating_leverage_guardrail", "full_4b_requires_non_price_evidence", "price_only_blowoff_blocks_positive_stage", "high_MAE_guardrail"], "residual_error_types_found": ["platform_ad_revenue_operating_leverage_positive", "search_portal_false_stage2", "digital_adtech_event_cap_4B"], "loop_contribution_label": "priority1_canonical_archetype_rule_candidate", "do_not_propose_new_weight_delta": true, "source_proxy_only_count": 3, "evidence_url_pending_count": 3}
```

### 25.6 narrative_only row

```jsonl
{"row_type":"narrative_only","case_id":"none","symbol":"none","large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE","reason":"all selected rows have usable 180D stock-web windows; no narrative-only price row required","price_source":"Songdaiki/stock-web","usage":"not_weight_calibration"}
```

## 26. Deferred Coding Agent Handoff Prompt

### Purpose

You are now in the repository implementation phase. The attached Markdown files are v12 post-calibrated residual research outputs produced using the Songdaiki/stock-web OHLC atlas.

These MDs are not live candidate research. They are historical calibration research designed to extend the already-applied calibrated profile.

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
- C26 rows need explicit GMV or traffic conversion, ad/solution take-rate, advertiser or merchant retention, operating leverage, margin and revision bridge before positive promotion.
- In C26, bridge-missing platform/ad-revenue rows with low MFE or high/persistent MAE should route to 4B/watch, not Stage3.
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
10. Add tests that bridge-missing C26 platform ad-revenue operating-leverage rows cannot promote positive stages.

### Expected output

- Concise implementation summary.
- Rows accepted/rejected.
- New sector/canonical archetype coverage.
- Existing axis strengthened/weakened/kept.
- No investment recommendation language.

## 27. Next Selection State

```text
completed_round = R8
completed_loop = 99
completed_canonical_archetype_id = C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE
coverage_scheduler_status = coverage_index_first
next_selection_rule = re-read V12_Research_No_Repeat_Index.md Priority 1 and local supplements
round_schedule_status = valid
round_sector_consistency = pass
```

## 28. Source Notes

- Main execution prompt: Songdaiki/stock_agent docs/core/e2r_v12_prompt_round_scheduler_corrected.txt.
- No-repeat index: Songdaiki/stock_agent docs/core/V12_Research_No_Repeat_Index.md.
- Price atlas: Songdaiki/stock-web atlas/manifest.json and per-symbol tradable shards.
- This file contains no investment recommendation and no production scoring change.
