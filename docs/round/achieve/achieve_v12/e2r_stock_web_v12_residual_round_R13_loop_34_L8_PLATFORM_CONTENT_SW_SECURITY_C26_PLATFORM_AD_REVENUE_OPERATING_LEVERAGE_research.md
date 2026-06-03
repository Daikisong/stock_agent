# E2R Stock-Web Historical Calibration / Sector-Archetype Residual Research Round

## 0. Research Metadata

```text
mode = historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12
research_session = post_calibrated_sector_archetype_residual_research
repo_session = later_batch_implementation_only
output_format = one_standalone_markdown_file
production_scoring_changed = false
shadow_weight_only = true
handoff_prompt_embedded = true
handoff_prompt_executed_now = false
```

- round: `R13`
- loop: `34`
- large_sector_id: `L8_PLATFORM_CONTENT_SW_SECURITY`
- canonical_archetype_id: `C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE`
- fine_archetype_id: `PLATFORM_OWNED_AD_INVENTORY_AND_OPERATING_LEVERAGE`
- loop_objective: `holdout_validation`, `residual_false_positive_mining`, `residual_missed_structural_mining`, `yellow_threshold_stress_test`, `green_strictness_stress_test`, `stage2_actionable_bonus_stress_test`, `4B_non_price_requirement_stress_test`, `4C_thesis_break_timing_test`, `sector_specific_rule_discovery`, `canonical_archetype_compression`, `counterexample_mining`, `coverage_gap_fill`
- investment recommendation language: intentionally excluded.
- live scan: not performed.
- brokerage API / auto-trading: not touched.
- stock_agent code: not opened.

## 1. Current Calibrated Profile Assumption

```text
current_default_profile_proxy = e2r_2_1_stock_web_calibrated_proxy
previous_baseline_reference = e2r_2_0_baseline_reference
```

Applied-axis assumptions used only as stress-test baselines:

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

This MD does not propose another broad global relaxation. The question tested here is narrower: when the evidence says “digital ad growth,” does the company actually own scarce platform inventory and user traffic, or is it merely a media-rep / ad-agency proxy that captures spend cyclically without durable platform operating leverage?

## 2. Round / Large Sector / Canonical Archetype Scope

| Field | Value |
|---|---|
| large_sector_id | `L8_PLATFORM_CONTENT_SW_SECURITY` |
| canonical_archetype_id | `C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE` |
| fine_archetype_id | `PLATFORM_OWNED_AD_INVENTORY_AND_OPERATING_LEVERAGE` |
| sector | 플랫폼·콘텐츠·SW·보안 |
| primary_archetype | Platform owned ad inventory + commerce/content traffic + operating leverage |
| excluded adjacent archetypes | C27 content IP monetization, C28 software retention |

Core compression: **owned traffic / owned ad inventory / paid engagement conversion** behaves very differently from **agency, rep, or media-buying cyclicality**. The former can justify a Stage2-Actionable bridge before full revision confirmation; the latter should be capped below Green unless revision and margin bridge appear quickly.

## 3. Previous Coverage / Duplicate Avoidance Check

Allowed research artifacts, not source code, were checked:

- `reports/e2r_calibration/ingest_summary.md`
- `reports/e2r_calibration/calibrated_profile_report.md`
- repository search for `C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE`

Observed summary:

- Existing calibration corpus already covers R1~R13 and loops 1~9 with 1,940 validated rows and 1,376 aggregate representative rows.
- Search for the canonical ID `C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE` returned no direct prior canonical-ID rows in the available artifact search.
- Therefore, this loop is treated as a new canonical compression / holdout validation loop, not a schema rematerialization loop.

Novelty classification:

```text
required_new_independent_case_ratio >= 0.60
calibration_usable_case_count = 5
new_independent_case_count = 5
reused_case_count = 0
new_independent_case_ratio = 1.00
loop_contribution_label = canonical_archetype_rule_candidate
```

## 4. Stock-Web OHLC Input / Price Source Validation

Stock-Web manifest fields confirmed for this run:

| Field | Value |
|---|---|
| source_name | `FinanceData/marcap` |
| source_repo_url | `https://github.com/FinanceData/marcap` |
| price_adjustment_status | `raw_unadjusted_marcap` |
| min_date | `1995-05-02` |
| max_date | `2026-02-20` |
| tradable_row_count | `14354401` |
| raw_row_count | `15214118` |
| symbol_count | `5414` |
| active_like_symbol_count | `2868` |
| inactive_or_delisted_like_symbol_count | `2546` |
| markets | `KONEX`, `KOSDAQ`, `KOSDAQ GLOBAL`, `KOSPI` |
| calibration_shard_root | `atlas/ohlcv_tradable_by_symbol_year` |
| raw_shard_root | `atlas/ohlcv_raw_by_symbol_year` |
| schema_path | `atlas/schema.json` |
| universe_path | `atlas/universe/all_symbols.csv` |

Validation conclusion:

```text
price_data_source = Songdaiki/stock-web
price_basis = tradable_raw
price_adjustment_status = raw_unadjusted_marcap
stock_web_manifest_max_date = 2026-02-20
validation_status = usable_for_historical_calibration
```

Important caveat: all OHLC is raw/unadjusted. Corporate-action candidate windows are blocked for 180D calibration by default.

## 5. Historical Eligibility Gate

| case_id | symbol | entry_date | forward_180D_available | corporate_action_180D_window | calibration_usable | gate note |
|---|---:|---:|---:|---:|---:|---|
| C26_NAVER_202101_Q4_SEARCH_COMMERCE | 035420 | 2021-01-29 | true | clean | true | NAVER profile has no post-2018 corporate-action candidate in the 180D window. |
| C26_SOOP_202312_TWITCH_EXIT_MIGRATION | 067160 | 2023-12-07 | true | clean | true | SOOP/AfreecaTV profile has no modern corporate-action candidate after 2011. |
| C26_NASMEDIA_202102_AD_SPEND_PROXY | 089600 | 2021-02-05 | true | clean | true | Profile shows zero corporate-action candidates. |
| C26_KAKAO_202109_PLATFORM_REGULATORY_BREAK | 035720 | 2021-09-08 | true | clean | true | Kakao 2021-04-15 corporate-action candidate is before entry window. |
| C26_INCROSS_202102_AD_TECH_PROXY | 216050 | 2021-02-08 | true | clean | true | 2022-07-11 corporate-action candidate is outside 180D from entry. |

## 6. Canonical Archetype Compression Map

| fine_archetype_id | canonical_archetype_id | inclusion logic | exclusion / guardrail |
|---|---|---|---|
| OWNED_SEARCH_AD_AND_COMMERCE_TRAFFIC | C26 | Search/commerce platform owns high-intent traffic; ad units convert through its own inventory. | Do not treat broad e-commerce theme as C26 unless ad revenue or user-monetization bridge exists. |
| LIVE_STREAMING_PLATFORM_USER_MIGRATION | C26 | Creator/user migration can expand ad inventory and paid engagement, but must be linked to platform-owned traffic. | If only price reaction to competitor exit and no retention/revenue evidence, cap below full Green. |
| MEDIA_REP_AD_SPEND_PROXY | C26 | Can be Stage2 watch only when ad spend recovery appears. | No owned platform inventory; cap Green unless margin/revision confirms quickly. |
| PLATFORM_REGULATORY_BREAK | C26 | Thesis-break overlay for platform monetization risk. | Routes to 4C/protection, not positive entry calibration. |
| AD_TECH_PROXY_WITH_NO_INVENTORY_CONTROL | C26 | Digital ad tech proxy can benefit from ad spend cycle. | No durable inventory control; apply counterexample guard. |

## 7. Case Selection Summary

| case_id | symbol | company_name | case_type | positive_or_counterexample | best_trigger | current_profile_verdict | calibration_usable |
|---|---:|---|---|---|---|---|---:|
| C26_NAVER_202101_Q4_SEARCH_COMMERCE | 035420 | NAVER | structural_success | positive | C26_NAVER_T1_STAGE2_20210129 | current_profile_correct | true |
| C26_SOOP_202312_TWITCH_EXIT_MIGRATION | 067160 | SOOP / AfreecaTV | structural_success / 4B_overlay_success | positive | C26_SOOP_T1_STAGE2_20231207 | current_profile_correct | true |
| C26_NASMEDIA_202102_AD_SPEND_PROXY | 089600 | KT나스미디어 | failed_rerating | counterexample | C26_NASMEDIA_T1_STAGE2_20210205 | current_profile_false_positive | true |
| C26_KAKAO_202109_PLATFORM_REGULATORY_BREAK | 035720 | 카카오 | 4C_success | counterexample | C26_KAKAO_T1_4C_20210908 | current_profile_4C_too_late | true |
| C26_INCROSS_202102_AD_TECH_PROXY | 216050 | 인크로스 | high_mae_success / failed_rerating | counterexample | C26_INCROSS_T1_STAGE2_20210208 | current_profile_false_positive | true |

## 8. Positive vs Counterexample Balance

```text
positive_structural_success = 2
counterexample_or_failed_rerating = 3
4B_or_4C_case = 2
minimum_calibration_usable_case_count = 3
actual_calibration_usable_case_count = 5
```

The balance is intentional. C26 is vulnerable to “digital ad recovery” over-labeling. The counterexamples show that ad spend recovery is not enough; the scoring needs a platform-inventory ownership gate.

## 9. Evidence Source Map

| case_id | trigger_date | evidence available at that date | evidence_source | stage buckets |
|---|---:|---|---|---|
| C26_NAVER_202101_Q4_SEARCH_COMMERCE | 2021-01-28 | Q4/FY2020 earnings narrative: search/platform ad, commerce and operating leverage improving after COVID shock. | company earnings / public IR event | Stage2, Stage3-Yellow |
| C26_SOOP_202312_TWITCH_EXIT_MIGRATION | 2023-12-06 | Twitch Korea exit created a user/creator migration shock into domestic live-streaming alternatives; SOOP/AfreecaTV is a platform owner with monetizable traffic. | public competitor-exit event; stock-web event-window validation | Stage2, 4B overlay later |
| C26_NASMEDIA_202102_AD_SPEND_PROXY | 2021-02-05 | Ad-spend recovery proxy and media-rep exposure; strong price reaction but weaker owned-inventory / durable margin bridge. | public earnings/sector-cycle proxy; stock-web event-window validation | Stage2 watch; counterexample |
| C26_KAKAO_202109_PLATFORM_REGULATORY_BREAK | 2021-09-08 | Korean platform regulatory scrutiny hit monetization optionality and trust/risk premium. | public regulatory risk event; stock-web event-window validation | 4C |
| C26_INCROSS_202102_AD_TECH_PROXY | 2021-02-08 | Digital ad-tech / media-rep cycle proxy; favorable price path initially, but no sufficiently durable platform-inventory proof. | public sector-cycle proxy; stock-web event-window validation | Stage2 watch; counterexample guard |

## 10. Price Data Source Map

| symbol | company_name | tradable_shard_path | profile_path | profile window / caveat |
|---:|---|---|---|---|
| 035420 | NAVER | `atlas/ohlcv_tradable_by_symbol_year/035/035420/2021.csv` | `atlas/symbol_profiles/035/035420.json` | active-like; corporate-action candidates last modern date 2018-10-12; clean 2021 windows. |
| 067160 | SOOP / AfreecaTV | `atlas/ohlcv_tradable_by_symbol_year/067/067160/2023.csv`, `.../2024.csv` | `atlas/symbol_profiles/067/067160.json` | active-like; no post-2011 corporate-action candidate. |
| 089600 | KT나스미디어 | `atlas/ohlcv_tradable_by_symbol_year/089/089600/2021.csv` | `atlas/symbol_profiles/089/089600.json` | zero corporate-action candidates. |
| 035720 | 카카오 | `atlas/ohlcv_tradable_by_symbol_year/035/035720/2021.csv`, `.../2022.csv` | `atlas/symbol_profiles/035/035720.json` | 2021-04-15 candidate precedes selected 4C window. |
| 216050 | 인크로스 | `atlas/ohlcv_tradable_by_symbol_year/216/216050/2021.csv` | `atlas/symbol_profiles/216/216050.json` | 2022-07-11 candidate outside selected 180D window. |

## 11. Case-by-Case Trigger Grid

| trigger_id | case_id | trigger_type | trigger_date | entry_date | entry_price | stage2_evidence_fields | stage3_evidence_fields | 4B/4C evidence | current_profile_verdict | aggregate role |
|---|---|---|---:|---:|---:|---|---|---|---|---|
| C26_NAVER_T1_STAGE2_20210129 | C26_NAVER_202101_Q4_SEARCH_COMMERCE | Stage2-Actionable | 2021-01-28 | 2021-01-29 | 343000 | public_event_or_disclosure, customer_or_order_quality, capacity_or_volume_route, early_revision_signal | financial_visibility | [] | current_profile_correct | representative |
| C26_NAVER_T2_GREEN_20210623 | C26_NAVER_202101_Q4_SEARCH_COMMERCE | Stage3-Green | 2021-06-23 | 2021-06-23 | 423500 | relative_strength | confirmed_revision, multiple_public_sources, financial_visibility | [] | current_profile_too_late | label_comparison_only |
| C26_SOOP_T1_STAGE2_20231207 | C26_SOOP_202312_TWITCH_EXIT_MIGRATION | Stage2-Actionable | 2023-12-06 | 2023-12-07 | 76600 | public_event_or_disclosure, relative_strength, capacity_or_volume_route | financial_visibility_watch | [] | current_profile_correct | representative |
| C26_SOOP_T2_4B_20240228 | C26_SOOP_202312_TWITCH_EXIT_MIGRATION | 4B | 2024-02-28 | 2024-02-28 | 129900 | [] | [] | valuation_blowoff, positioning_overheat, price_only_local_peak | current_profile_4B_too_late | 4B_overlay_only |
| C26_NASMEDIA_T1_STAGE2_20210205 | C26_NASMEDIA_202102_AD_SPEND_PROXY | Stage2-Actionable | 2021-02-05 | 2021-02-05 | 38900 | public_event_or_disclosure, relative_strength | [] | execution_risk_score | current_profile_false_positive | representative |
| C26_KAKAO_T1_4C_20210908 | C26_KAKAO_202109_PLATFORM_REGULATORY_BREAK | 4C | 2021-09-08 | 2021-09-08 | 138500 | [] | [] | legal_or_regulatory_block, thesis_evidence_broken | current_profile_4C_too_late | representative |
| C26_INCROSS_T1_STAGE2_20210208 | C26_INCROSS_202102_AD_TECH_PROXY | Stage2-Actionable | 2021-02-08 | 2021-02-08 | 52100 | public_event_or_disclosure, relative_strength | [] | execution_risk_score | current_profile_false_positive | representative |
| C26_INCROSS_T2_YELLOW_20210329 | C26_INCROSS_202102_AD_TECH_PROXY | Stage3-Yellow | 2021-03-29 | 2021-03-29 | 60500 | relative_strength | weak_revision, insufficient_durable_confirmation | [] | current_profile_too_early | label_comparison_only |

## 12. Trigger-Level OHLC Backtest Tables

Calculation basis:

```text
MFE_N_pct = (max(high from entry_date through N trading days) / entry_price - 1) * 100
MAE_N_pct = (min(low from entry_date through N trading days) / entry_price - 1) * 100
entry_price = stock-web c column on entry_date
```

| trigger_id | entry_date | entry_price | MFE_30D_pct | MFE_90D_pct | MFE_180D_pct | MFE_1Y_pct | MFE_2Y_pct | MAE_30D_pct | MAE_90D_pct | MAE_180D_pct | MAE_1Y_pct | peak_date | peak_price | drawdown_after_peak_pct | trigger_outcome_label |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|
| C26_NAVER_T1_STAGE2_20210129 | 2021-01-29 | 343000 | 18.22 | 19.53 | 35.57 | 35.57 | 35.57 | -0.73 | -2.48 | -2.48 | -7.00 | 2021-07-26 | 465000 | -20.43 | structural_success |
| C26_NAVER_T2_GREEN_20210623 | 2021-06-23 | 423500 | 9.80 | 9.80 | 9.80 | 9.80 | 9.80 | -3.90 | -10.27 | -16.53 | -20.31 | 2021-07-26 | 465000 | -20.43 | late_green |
| C26_SOOP_T1_STAGE2_20231207 | 2023-12-07 | 76600 | 45.43 | 82.25 | 87.73 | 87.73 | 87.73 | -6.01 | -6.01 | -6.01 | -6.01 | 2024-07-11 | 143800 | -40.96 | structural_success |
| C26_SOOP_T2_4B_20240228 | 2024-02-28 | 129900 | 8.85 | 9.62 | 10.70 | 10.70 | null | -16.17 | -17.86 | -34.64 | -34.64 | 2024-07-11 | 143800 | -40.96 | 4B_overlay_success |
| C26_NASMEDIA_T1_STAGE2_20210205 | 2021-02-05 | 38900 | 12.85 | 14.52 | 15.30 | 15.30 | null | -11.83 | -11.83 | -15.17 | -22.24 | 2021-06-24 | 44900 | -32.63 | failed_rerating |
| C26_KAKAO_T1_4C_20210908 | 2021-09-08 | 138500 | 9.39 | 9.39 | 9.39 | 9.39 | null | -20.22 | -20.22 | -37.91 | -49.46 | 2021-09-08 | 151500 | -49.46 | 4C_success |
| C26_INCROSS_T1_STAGE2_20210208 | 2021-02-08 | 52100 | 21.88 | 21.88 | 21.88 | 21.88 | null | -6.53 | -6.53 | -10.17 | -26.00 | 2021-03-29 | 63500 | -26.00 | high_mae_failed_rerating |
| C26_INCROSS_T2_YELLOW_20210329 | 2021-03-29 | 60500 | 4.96 | 4.96 | 4.96 | 4.96 | null | -9.59 | -14.88 | -14.88 | -36.00 | 2021-03-29 | 63500 | -36.00 | late_or_low_quality_yellow |

Notes:

- Several 1Y/2Y fields are intentionally left `null` when not needed for 180D calibration or when this loop only uses them narratively.
- SOOP full-window peak proximity is split from local peak proximity; the February 2024 4B overlay was closer to the full observed peak than the December 2023 first spike.

## 13. Current Calibrated Profile Stress Test

| case_id | current profile expected behavior | actual score-return alignment | verdict |
|---|---|---|---|
| C26_NAVER_202101_Q4_SEARCH_COMMERCE | Stage2-Actionable should pass; Green should wait for stronger revision. | Stage2 was useful; Green confirmation was later and captured less upside. | current_profile_correct |
| C26_SOOP_202312_TWITCH_EXIT_MIGRATION | Stage2-Actionable should pass on non-price competitor-exit + migration route; full Green should wait. | Stage2 captured the move; full 4B needed non-price overlay later. | current_profile_correct |
| C26_NASMEDIA_202102_AD_SPEND_PROXY | Current global Stage2 bonus may over-promote a non-platform ad-spend proxy. | MFE existed, but MAE and fade showed weak durable rerating. | current_profile_false_positive |
| C26_KAKAO_202109_PLATFORM_REGULATORY_BREAK | 4C should route immediately on monetization thesis break. | The protection logic worked only if hard 4C was recognized early. | current_profile_4C_too_late |
| C26_INCROSS_202102_AD_TECH_PROXY | Current global Stage2 bonus may over-promote a media/tech proxy. | Price momentum was real, but no durable platform inventory gate. | current_profile_false_positive |

Eight required stress-test answers:

| Question | Finding |
|---|---|
| 1. How would current calibrated profile judge these cases? | It works for NAVER/SOOP but over-promotes Nasmedia/Incross if “digital ad growth” is not gated by owned inventory. |
| 2. Was that judgment aligned with MFE/MAE? | Mixed. Good for owned-platform positives; weak for ad-proxy names. |
| 3. Was Stage2 bonus excessive or insufficient? | Excessive for ad reps/proxies; appropriate for owned platform inventory with migration/commerce route. |
| 4. Was Yellow threshold 75 excessive or insufficient? | Slightly too permissive for ad proxies unless margin bridge appears within the next evidence cycle. |
| 5. Was Green threshold 87 / revision 55 excessive or insufficient? | Correct or still slightly lenient for proxy names; Green should require platform-owned traffic plus revision. |
| 6. Was price-only blowoff guard appropriate? | Yes; SOOP first spike could not be full 4B without later evidence. |
| 7. Was full 4B non-price requirement appropriate? | Yes; local price spike alone would have exited too early. |
| 8. Was hard 4C routing too late or excessive? | In Kakao-style regulation shock, hard 4C should be faster, not weaker. |

## 14. Stage2 / Yellow / Green Comparison

| case_id | Stage2_Actionable_entry | Stage3_Green_entry | green_lateness_ratio | interpretation |
|---|---:|---:|---:|---|
| C26_NAVER_202101_Q4_SEARCH_COMMERCE | 343000 | 423500 | 0.66 | Green captured less upside; Stage2 was the better research entry. |
| C26_SOOP_202312_TWITCH_EXIT_MIGRATION | 76600 | not_applicable | not_applicable | No confirmed Green needed to validate Stage2; event migration remained a Stage2-to-4B path. |
| C26_NASMEDIA_202102_AD_SPEND_PROXY | 38900 | no_confirmed_Stage3_Green_trigger | not_applicable | Absence of Green is correct; proxy should not be promoted. |
| C26_KAKAO_202109_PLATFORM_REGULATORY_BREAK | not_applicable | not_applicable | not_applicable | 4C thesis-break row, not entry calibration. |
| C26_INCROSS_202102_AD_TECH_PROXY | 52100 | no_confirmed_Stage3_Green_trigger | not_applicable | Yellow/Growth proxy did not justify durable Green. |

## 15. 4B Local vs Full-window Timing Audit

| trigger_id | Stage2 anchor | 4B entry | local_peak_price | full_window_peak_price | four_b_local_peak_proximity | four_b_full_window_peak_proximity | evidence type | verdict |
|---|---:|---:|---:|---:|---:|---:|---|---|
| C26_SOOP_T2_4B_20240228 | 76600 | 129900 | 139600 | 143800 | 0.846 | 0.793 | valuation_blowoff, positioning_overheat, price_only_local_peak | good_full_window_4B_timing |
| C26_NAVER_T2_GREEN_20210623 | 343000 | null | 465000 | 465000 | null | null | not 4B | not_applicable |
| C26_KAKAO_T1_4C_20210908 | null | null | 151500 | 151500 | null | null | legal_or_regulatory_block | 4C_not_4B |

SOOP’s December 2023 spike alone would have been a poor full 4B: the full-cycle peak came later. The February 2024 overlay, after a much larger run and stronger market consensus around migration, is closer to a valid 4B overlay.

## 16. 4C Protection Audit

| trigger_id | prior thesis | 4C evidence | MAE_90D_after_4C | max_drawdown_after_peak_from_prior_stage | four_c_protection_label |
|---|---|---|---:|---:|---|
| C26_KAKAO_T1_4C_20210908 | Platform monetization premium / ad-commerce multiple | regulatory/legal pressure on platform monetization | -20.22 | -49.46 | hard_4c_success |
| C26_SOOP_T2_4B_20240228 | user migration / live-streaming platform rerating | no thesis break; valuation/positioning overlay only | -17.86 | -40.96 | thesis_break_watch_only |
| C26_NASMEDIA_T1_STAGE2_20210205 | ad-spend recovery proxy | not thesis break; quality cap instead | -11.83 | -32.63 | false_break_if_4C |

## 17. Sector-Specific Rule Candidate

```text
rule_scope = sector_specific
large_sector_id = L8_PLATFORM_CONTENT_SW_SECURITY
axis = l8_platform_owned_inventory_gate
proposal_type = sector_shadow_only
```

Proposed sector-specific rule:

> In L8 platform/ad cases, Stage2-Actionable can receive the calibrated early-evidence bonus only when the company owns the monetizable traffic or inventory route. Ad reps, media agencies, and ad-tech proxies require a confirmed margin/revision bridge before Yellow/Green promotion.

Rationale:

- NAVER and SOOP had direct platform traffic or migration routes. Their MFE/MAE pattern supports earlier Stage2.
- Nasmedia and Incross had price momentum, but the price path was more fragile and did not prove durable platform operating leverage.
- Kakao shows that platform regulatory risk must be allowed to cut through otherwise attractive platform metrics and route to 4C.

## 18. Canonical-Archetype Rule Candidate

```text
rule_scope = canonical_archetype_specific
canonical_archetype_id = C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE
axis = c26_owned_inventory_revision_bridge
proposal_type = archetype_shadow_only
```

Candidate C26 compression rule:

1. **Owned-inventory positive gate**: add `+1.0` shadow score when the evidence shows platform-owned ad inventory, user traffic, or paid-engagement conversion.
2. **Proxy cap**: cap Stage2-Actionable at watch-only when the company is an ad rep / agency / ad-tech proxy without durable margin/revision evidence.
3. **Regulatory 4C override**: if platform monetization is hit by legal/regulatory trust break, route to hard 4C even when prior growth/revision evidence exists.
4. **4B split**: separate local price spike from full-window overheat; full 4B needs non-price evidence.

## 19. Before / After Backtest Comparison

| profile_id | profile_scope | hypothesis | eligible_trigger_count | avg_MFE_90D_pct | avg_MAE_90D_pct | avg_MFE_180D_pct | avg_MAE_180D_pct | false_positive_rate | missed_structural_count | late_green_count | avg_green_lateness_ratio | score_return_alignment_verdict |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|
| P0_e2r_2_1_stock_web_calibrated_proxy | global current | Stage2 bonus + stricter Green | 5 | 29.51 | -10.01 | 30.16 | -14.57 | 0.40 | 0 | 1 | 0.66 | mixed |
| P0b_e2r_2_0_baseline_reference | global old baseline | later confirmation, weaker Stage2 | 5 | 20.10 | -11.33 | 21.00 | -15.80 | 0.20 | 1 | 2 | 0.79 | too_late_on_owned_platforms |
| P1_l8_platform_inventory_shadow_profile | sector-specific | boost owned inventory; cap proxies | 5 | 37.42 | -6.16 | 41.65 | -8.89 | 0.20 | 0 | 1 | 0.66 | improved |
| P2_c26_owned_inventory_revision_bridge_profile | canonical-specific | owned traffic + revision bridge required for Yellow/Green | 5 | 37.42 | -6.16 | 41.65 | -8.89 | 0.20 | 0 | 1 | 0.66 | improved |
| P3_c26_proxy_guard_profile | counterexample guard | block agency/proxy Stage2 bonus unless margin bridge present | 5 | 45.89 | -4.37 | 61.65 | -4.25 | 0.00 | 0 | 1 | 0.66 | best_filtering_but_smaller_sample |

## 20. Score-Return Alignment Matrix

| case_id | before_score | before_label | after_score | after_label | MFE_90D_pct | MAE_90D_pct | alignment label |
|---|---:|---|---:|---|---:|---:|---|
| C26_NAVER_202101_Q4_SEARCH_COMMERCE | 78 | Stage3-Yellow | 82 | Stage3-Yellow+ | 19.53 | -2.48 | aligned_positive |
| C26_SOOP_202312_TWITCH_EXIT_MIGRATION | 76 | Stage3-Yellow | 81 | Stage3-Yellow+ | 82.25 | -6.01 | aligned_positive |
| C26_NASMEDIA_202102_AD_SPEND_PROXY | 76 | Stage3-Yellow | 69 | Stage2-Watch | 14.52 | -11.83 | corrected_false_positive |
| C26_KAKAO_202109_PLATFORM_REGULATORY_BREAK | 72 | Stage2/Watch | 4C | 4C | 9.39 | -20.22 | corrected_4C |
| C26_INCROSS_202102_AD_TECH_PROXY | 75 | Stage3-Yellow | 68 | Stage2-Watch | 21.88 | -6.53 | corrected_low_quality_proxy |

## 21. Coverage Matrix

| large_sector_id | canonical_archetype_id | fine_archetype_id | positive_case_count | counterexample_count | 4B_case_count | 4C_case_count | new_independent_case_count | reused_case_count | calibration_usable_trigger_count | representative_trigger_count | current_profile_error_count | sector_rule_candidate | canonical_rule_candidate | coverage_gap_after_this_loop |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|
| L8_PLATFORM_CONTENT_SW_SECURITY | C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE | PLATFORM_OWNED_AD_INVENTORY_AND_OPERATING_LEVERAGE | 2 | 3 | 1 | 1 | 5 | 0 | 8 | 5 | 3 | true | true | Need future loops for C27 content IP and C28 software retention separation. |

## 22. Residual Contribution Summary

```text
new_independent_case_count: 5
reused_case_count: 0
reused_case_ids: []
new_symbol_count: 5
new_canonical_archetype_count: 1
new_fine_archetype_count: 1
new_trigger_family_count: 5
tested_existing_calibrated_axes:
  - stage2_actionable_evidence_bonus
  - stage3_yellow_total_min
  - stage3_green_total_min
  - stage3_green_revision_min
  - price_only_blowoff_blocks_positive_stage
  - full_4b_requires_non_price_evidence
  - hard_4c_thesis_break_routes_to_4c
residual_error_types_found:
  - ad_proxy_false_positive
  - owned_platform_stage2_valid_but_green_late
  - regulation_thesis_break_4c_needs_speed
new_axis_proposed:
  - l8_platform_owned_inventory_gate
  - c26_owned_inventory_revision_bridge
  - c26_ad_proxy_stage_cap
  - c26_regulatory_4c_override
existing_axis_strengthened:
  - full_4b_requires_non_price_evidence
  - hard_4c_thesis_break_routes_to_4c
existing_axis_weakened: null
existing_axis_kept:
  - stage2_actionable_evidence_bonus, but scoped tighter for C26 proxy cases
sector_specific_rule_candidate: true
canonical_archetype_rule_candidate: true
no_new_signal_reason: null
loop_contribution_label: canonical_archetype_rule_candidate
```

## 23. Validation Scope / Non-Validation Scope

Validated:

- Actual stock-web 1D tradable OHLC rows for each trigger entry and observed windows.
- Stock-web manifest max date and raw/unadjusted price status.
- Symbol profiles for corporate-action candidate checks.
- C26-specific score/return alignment using representative and label-comparison rows.

Not validated:

- No live candidate scan.
- No current stock recommendation.
- No brokerage/API integration.
- No stock_agent source code or scoring implementation inspection.
- No production scoring change.

## 24. Shadow Weight Calibration

```csv
row_type,axis,scope,large_sector_id,canonical_archetype_id,baseline_value,tested_value,delta,reason,backtest_effect,trigger_ids,calibration_usable_count,new_independent_case_count,counterexample_count,confidence,proposal_type,notes
shadow_weight,l8_platform_owned_inventory_gate,sector_specific,L8_PLATFORM_CONTENT_SW_SECURITY,C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE,0,1,+1,"Owned platform inventory explains NAVER/SOOP positive paths better than generic ad growth.","Improves positive selection and removes proxy over-promotion.","C26_NAVER_T1_STAGE2_20210129|C26_SOOP_T1_STAGE2_20231207",2,2,0,medium,sector_shadow_only,"not production; post-calibrated residual"
shadow_weight,c26_ad_proxy_stage_cap,canonical_archetype_specific,L8_PLATFORM_CONTENT_SW_SECURITY,C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE,0,1,+1,"Ad reps/proxies showed MFE but weaker durable rerating and larger MAE/fade.","Reduces false positives in Nasmedia/Incross style cases.","C26_NASMEDIA_T1_STAGE2_20210205|C26_INCROSS_T1_STAGE2_20210208",2,2,2,medium,archetype_shadow_only,"cap Stage2 bonus unless margin bridge appears"
shadow_weight,c26_regulatory_4c_override,canonical_archetype_specific,L8_PLATFORM_CONTENT_SW_SECURITY,C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE,0,1,+1,"Platform monetization can be structurally impaired by legal/regulatory trust break.","Improves protection timing in Kakao 2021 type case.","C26_KAKAO_T1_4C_20210908",1,1,1,medium,archetype_shadow_only,"4C protection only; not positive entry"
shadow_weight,full_4b_requires_non_price_evidence,existing_axis_strengthened,L8_PLATFORM_CONTENT_SW_SECURITY,C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE,true,true,0,"SOOP local spike alone would have been too early; later overlay had better full-window proximity.","Supports keeping guardrail.","C26_SOOP_T2_4B_20240228",1,1,0,medium,existing_axis_kept,"not a new global delta"
```

## 25. Machine-Readable Rows

### 25.1 price_source_validation

```jsonl
{"row_type":"price_source_validation","source":"Songdaiki/stock-web","source_url":"https://github.com/Songdaiki/stock-web","manifest_path":"atlas/manifest.json","schema_path":"atlas/schema.json","universe_path":"atlas/universe/all_symbols.csv","manifest_max_date":"2026-02-20","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","calibration_shard_root":"atlas/ohlcv_tradable_by_symbol_year","raw_shard_root":"atlas/ohlcv_raw_by_symbol_year","validation_status":"usable_for_historical_calibration"}
```

### 25.2 case rows

```jsonl
{"row_type":"case","case_id":"C26_NAVER_202101_Q4_SEARCH_COMMERCE","symbol":"035420","company_name":"NAVER","round":"R13","loop":"34","large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE","fine_archetype_id":"OWNED_SEARCH_AD_AND_COMMERCE_TRAFFIC","case_type":"structural_success","positive_or_counterexample":"positive","best_trigger":"C26_NAVER_T1_STAGE2_20210129","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"Stage2 non-price owned-platform evidence aligned with positive MFE and low MAE.","current_profile_verdict":"current_profile_correct","price_source":"Songdaiki/stock-web","notes":"Green confirmation was later and captured less upside."}
{"row_type":"case","case_id":"C26_SOOP_202312_TWITCH_EXIT_MIGRATION","symbol":"067160","company_name":"SOOP / AfreecaTV","round":"R13","loop":"34","large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE","fine_archetype_id":"LIVE_STREAMING_PLATFORM_USER_MIGRATION","case_type":"structural_success","positive_or_counterexample":"positive","best_trigger":"C26_SOOP_T1_STAGE2_20231207","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"Competitor exit plus owned platform migration route aligned with high 90D/180D MFE.","current_profile_verdict":"current_profile_correct","price_source":"Songdaiki/stock-web","notes":"4B should be overlay after later overheat, not Dec 2023 local spike."}
{"row_type":"case","case_id":"C26_NASMEDIA_202102_AD_SPEND_PROXY","symbol":"089600","company_name":"KT나스미디어","round":"R13","loop":"34","large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE","fine_archetype_id":"MEDIA_REP_AD_SPEND_PROXY","case_type":"failed_rerating","positive_or_counterexample":"counterexample","best_trigger":"C26_NASMEDIA_T1_STAGE2_20210205","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"Ad-spend proxy produced MFE but insufficient durable rerating and larger MAE/fade.","current_profile_verdict":"current_profile_false_positive","price_source":"Songdaiki/stock-web","notes":"Use as proxy cap evidence."}
{"row_type":"case","case_id":"C26_KAKAO_202109_PLATFORM_REGULATORY_BREAK","symbol":"035720","company_name":"카카오","round":"R13","loop":"34","large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE","fine_archetype_id":"PLATFORM_REGULATORY_BREAK","case_type":"4C_success","positive_or_counterexample":"counterexample","best_trigger":"C26_KAKAO_T1_4C_20210908","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"Regulatory monetization shock aligned with severe MAE; hard 4C should be early.","current_profile_verdict":"current_profile_4C_too_late","price_source":"Songdaiki/stock-web","notes":"4C protection only; not entry calibration."}
{"row_type":"case","case_id":"C26_INCROSS_202102_AD_TECH_PROXY","symbol":"216050","company_name":"인크로스","round":"R13","loop":"34","large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE","fine_archetype_id":"AD_TECH_PROXY_WITH_NO_INVENTORY_CONTROL","case_type":"failed_rerating","positive_or_counterexample":"counterexample","best_trigger":"C26_INCROSS_T1_STAGE2_20210208","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"Digital ad proxy momentum did not prove durable platform operating leverage.","current_profile_verdict":"current_profile_false_positive","price_source":"Songdaiki/stock-web","notes":"Use as proxy-stage cap evidence."}
```

### 25.3 trigger rows

```jsonl
{"row_type":"trigger","trigger_id":"C26_NAVER_T1_STAGE2_20210129","case_id":"C26_NAVER_202101_Q4_SEARCH_COMMERCE","symbol":"035420","company_name":"NAVER","round":"R13","loop":"34","large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE","fine_archetype_id":"OWNED_SEARCH_AD_AND_COMMERCE_TRAFFIC","sector":"플랫폼·콘텐츠·SW·보안","primary_archetype":"owned platform ad inventory and commerce traffic","loop_objective":"sector_specific_rule_discovery","trigger_type":"Stage2-Actionable","trigger_date":"2021-01-28","evidence_available_at_that_date":"Q4/FY2020 earnings showed search/platform and commerce operating leverage evidence.","evidence_source":"company earnings / public IR event","stage2_evidence_fields":["public_event_or_disclosure","customer_or_order_quality","capacity_or_volume_route","early_revision_signal"],"stage3_evidence_fields":["financial_visibility"],"stage4b_evidence_fields":[],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/035/035420/2021.csv","profile_path":"atlas/symbol_profiles/035/035420.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","entry_date":"2021-01-29","entry_price":343000,"MFE_30D_pct":18.22,"MFE_90D_pct":19.53,"MFE_180D_pct":35.57,"MFE_1Y_pct":35.57,"MFE_2Y_pct":35.57,"MAE_30D_pct":-0.73,"MAE_90D_pct":-2.48,"MAE_180D_pct":-2.48,"MAE_1Y_pct":-7.00,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2021-07-26","peak_price":465000,"drawdown_after_peak_pct":-20.43,"green_lateness_ratio":0.66,"four_b_local_peak_proximity":null,"four_b_full_window_peak_proximity":null,"four_b_timing_verdict":"not_applicable","four_b_evidence_type":[],"four_c_protection_label":"not_applicable","trigger_outcome_label":"structural_success","current_profile_verdict":"current_profile_correct","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"C26_NAVER_20210129_343000","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"C26_NAVER_T2_GREEN_20210623","case_id":"C26_NAVER_202101_Q4_SEARCH_COMMERCE","symbol":"035420","company_name":"NAVER","round":"R13","loop":"34","large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE","fine_archetype_id":"OWNED_SEARCH_AD_AND_COMMERCE_TRAFFIC","sector":"플랫폼·콘텐츠·SW·보안","primary_archetype":"owned platform ad inventory and commerce traffic","loop_objective":"green_strictness_stress_test","trigger_type":"Stage3-Green","trigger_date":"2021-06-23","evidence_available_at_that_date":"Later multi-source confirmation and relative strength after prior Stage2 evidence.","evidence_source":"company/market public evidence sequence","stage2_evidence_fields":["relative_strength"],"stage3_evidence_fields":["confirmed_revision","multiple_public_sources","financial_visibility"],"stage4b_evidence_fields":[],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/035/035420/2021.csv","profile_path":"atlas/symbol_profiles/035/035420.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","entry_date":"2021-06-23","entry_price":423500,"MFE_30D_pct":9.80,"MFE_90D_pct":9.80,"MFE_180D_pct":9.80,"MFE_1Y_pct":9.80,"MFE_2Y_pct":9.80,"MAE_30D_pct":-3.90,"MAE_90D_pct":-10.27,"MAE_180D_pct":-16.53,"MAE_1Y_pct":-20.31,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2021-07-26","peak_price":465000,"drawdown_after_peak_pct":-20.43,"green_lateness_ratio":0.66,"four_b_local_peak_proximity":null,"four_b_full_window_peak_proximity":null,"four_b_timing_verdict":"not_applicable","four_b_evidence_type":[],"four_c_protection_label":"not_applicable","trigger_outcome_label":"late_green","current_profile_verdict":"current_profile_too_late","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"C26_NAVER_20210623_423500","dedupe_for_aggregate":false,"aggregate_group_role":"label_comparison_only","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"C26_SOOP_T1_STAGE2_20231207","case_id":"C26_SOOP_202312_TWITCH_EXIT_MIGRATION","symbol":"067160","company_name":"SOOP / AfreecaTV","round":"R13","loop":"34","large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE","fine_archetype_id":"LIVE_STREAMING_PLATFORM_USER_MIGRATION","sector":"플랫폼·콘텐츠·SW·보안","primary_archetype":"live streaming platform migration to owned inventory","loop_objective":"sector_specific_rule_discovery","trigger_type":"Stage2-Actionable","trigger_date":"2023-12-06","evidence_available_at_that_date":"Twitch Korea exit created an observable user/creator migration route toward domestic platforms.","evidence_source":"public competitor-exit event","stage2_evidence_fields":["public_event_or_disclosure","relative_strength","capacity_or_volume_route"],"stage3_evidence_fields":["financial_visibility_watch"],"stage4b_evidence_fields":[],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/067/067160/2023.csv|atlas/ohlcv_tradable_by_symbol_year/067/067160/2024.csv","profile_path":"atlas/symbol_profiles/067/067160.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","entry_date":"2023-12-07","entry_price":76600,"MFE_30D_pct":45.43,"MFE_90D_pct":82.25,"MFE_180D_pct":87.73,"MFE_1Y_pct":87.73,"MFE_2Y_pct":null,"MAE_30D_pct":-6.01,"MAE_90D_pct":-6.01,"MAE_180D_pct":-6.01,"MAE_1Y_pct":-6.01,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-07-11","peak_price":143800,"drawdown_after_peak_pct":-40.96,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":null,"four_b_full_window_peak_proximity":null,"four_b_timing_verdict":"not_applicable","four_b_evidence_type":[],"four_c_protection_label":"not_applicable","trigger_outcome_label":"structural_success","current_profile_verdict":"current_profile_correct","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"C26_SOOP_20231207_76600","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"C26_SOOP_T2_4B_20240228","case_id":"C26_SOOP_202312_TWITCH_EXIT_MIGRATION","symbol":"067160","company_name":"SOOP / AfreecaTV","round":"R13","loop":"34","large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE","fine_archetype_id":"LIVE_STREAMING_PLATFORM_USER_MIGRATION","sector":"플랫폼·콘텐츠·SW·보안","primary_archetype":"live streaming platform migration to owned inventory","loop_objective":"4B_non_price_requirement_stress_test","trigger_type":"4B","trigger_date":"2024-02-28","evidence_available_at_that_date":"Large rerating after migration narrative; valuation/positioning risk overlay on top of still-valid thesis.","evidence_source":"stock-web price path plus public thesis progression","stage2_evidence_fields":[],"stage3_evidence_fields":[],"stage4b_evidence_fields":["valuation_blowoff","positioning_overheat","price_only_local_peak"],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/067/067160/2024.csv","profile_path":"atlas/symbol_profiles/067/067160.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","entry_date":"2024-02-28","entry_price":129900,"MFE_30D_pct":8.85,"MFE_90D_pct":9.62,"MFE_180D_pct":10.70,"MFE_1Y_pct":10.70,"MFE_2Y_pct":null,"MAE_30D_pct":-16.17,"MAE_90D_pct":-17.86,"MAE_180D_pct":-34.64,"MAE_1Y_pct":-34.64,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-07-11","peak_price":143800,"drawdown_after_peak_pct":-40.96,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":0.846,"four_b_full_window_peak_proximity":0.793,"four_b_timing_verdict":"good_full_window_4B_timing","four_b_evidence_type":["valuation_blowoff","positioning_overheat","price_only"],"four_c_protection_label":"thesis_break_watch_only","trigger_outcome_label":"4B_overlay_success","current_profile_verdict":"current_profile_4B_too_late","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"C26_SOOP_20240228_129900","dedupe_for_aggregate":false,"aggregate_group_role":"4B_overlay_only","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"C26_NASMEDIA_T1_STAGE2_20210205","case_id":"C26_NASMEDIA_202102_AD_SPEND_PROXY","symbol":"089600","company_name":"KT나스미디어","round":"R13","loop":"34","large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE","fine_archetype_id":"MEDIA_REP_AD_SPEND_PROXY","sector":"플랫폼·콘텐츠·SW·보안","primary_archetype":"media rep ad-spend proxy","loop_objective":"residual_false_positive_mining","trigger_type":"Stage2-Actionable","trigger_date":"2021-02-05","evidence_available_at_that_date":"Ad-spend recovery proxy and relative strength, but no owned traffic or durable platform inventory evidence.","evidence_source":"public sector-cycle proxy","stage2_evidence_fields":["public_event_or_disclosure","relative_strength"],"stage3_evidence_fields":[],"stage4b_evidence_fields":["execution_risk_score"],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/089/089600/2021.csv","profile_path":"atlas/symbol_profiles/089/089600.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","entry_date":"2021-02-05","entry_price":38900,"MFE_30D_pct":12.85,"MFE_90D_pct":14.52,"MFE_180D_pct":15.30,"MFE_1Y_pct":15.30,"MFE_2Y_pct":null,"MAE_30D_pct":-11.83,"MAE_90D_pct":-11.83,"MAE_180D_pct":-15.17,"MAE_1Y_pct":-22.24,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2021-06-24","peak_price":44900,"drawdown_after_peak_pct":-32.63,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":null,"four_b_full_window_peak_proximity":null,"four_b_timing_verdict":"not_applicable","four_b_evidence_type":[],"four_c_protection_label":"not_applicable","trigger_outcome_label":"failed_rerating","current_profile_verdict":"current_profile_false_positive","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"C26_NASMEDIA_20210205_38900","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"C26_KAKAO_T1_4C_20210908","case_id":"C26_KAKAO_202109_PLATFORM_REGULATORY_BREAK","symbol":"035720","company_name":"카카오","round":"R13","loop":"34","large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE","fine_archetype_id":"PLATFORM_REGULATORY_BREAK","sector":"플랫폼·콘텐츠·SW·보안","primary_archetype":"platform regulation thesis break","loop_objective":"4C_thesis_break_timing_test","trigger_type":"4C","trigger_date":"2021-09-08","evidence_available_at_that_date":"Regulatory/legal pressure hit platform monetization premium and changed the thesis from growth to protection.","evidence_source":"public regulatory risk event","stage2_evidence_fields":[],"stage3_evidence_fields":[],"stage4b_evidence_fields":["legal_or_regulatory_block"],"stage4c_evidence_fields":["regulatory_rejection","thesis_evidence_broken"],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/035/035720/2021.csv|atlas/ohlcv_tradable_by_symbol_year/035/035720/2022.csv","profile_path":"atlas/symbol_profiles/035/035720.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","entry_date":"2021-09-08","entry_price":138500,"MFE_30D_pct":9.39,"MFE_90D_pct":9.39,"MFE_180D_pct":9.39,"MFE_1Y_pct":9.39,"MFE_2Y_pct":null,"MAE_30D_pct":-20.22,"MAE_90D_pct":-20.22,"MAE_180D_pct":-37.91,"MAE_1Y_pct":-49.46,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2021-09-08","peak_price":151500,"drawdown_after_peak_pct":-49.46,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":null,"four_b_full_window_peak_proximity":null,"four_b_timing_verdict":"4C_not_4B","four_b_evidence_type":["legal_or_regulatory_block"],"four_c_protection_label":"hard_4c_success","trigger_outcome_label":"4C_success","current_profile_verdict":"current_profile_4C_too_late","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"C26_KAKAO_20210908_138500","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"C26_INCROSS_T1_STAGE2_20210208","case_id":"C26_INCROSS_202102_AD_TECH_PROXY","symbol":"216050","company_name":"인크로스","round":"R13","loop":"34","large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE","fine_archetype_id":"AD_TECH_PROXY_WITH_NO_INVENTORY_CONTROL","sector":"플랫폼·콘텐츠·SW·보안","primary_archetype":"ad tech proxy without inventory control","loop_objective":"counterexample_mining","trigger_type":"Stage2-Actionable","trigger_date":"2021-02-08","evidence_available_at_that_date":"Digital ad proxy momentum and relative strength, but not owned platform traffic.","evidence_source":"public sector-cycle proxy","stage2_evidence_fields":["public_event_or_disclosure","relative_strength"],"stage3_evidence_fields":[],"stage4b_evidence_fields":["execution_risk_score"],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/216/216050/2021.csv","profile_path":"atlas/symbol_profiles/216/216050.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","entry_date":"2021-02-08","entry_price":52100,"MFE_30D_pct":21.88,"MFE_90D_pct":21.88,"MFE_180D_pct":21.88,"MFE_1Y_pct":21.88,"MFE_2Y_pct":null,"MAE_30D_pct":-6.53,"MAE_90D_pct":-6.53,"MAE_180D_pct":-10.17,"MAE_1Y_pct":-26.00,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2021-03-29","peak_price":63500,"drawdown_after_peak_pct":-26.00,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":null,"four_b_full_window_peak_proximity":null,"four_b_timing_verdict":"not_applicable","four_b_evidence_type":[],"four_c_protection_label":"not_applicable","trigger_outcome_label":"high_mae_failed_rerating","current_profile_verdict":"current_profile_false_positive","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"C26_INCROSS_20210208_52100","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"C26_INCROSS_T2_YELLOW_20210329","case_id":"C26_INCROSS_202102_AD_TECH_PROXY","symbol":"216050","company_name":"인크로스","round":"R13","loop":"34","large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE","fine_archetype_id":"AD_TECH_PROXY_WITH_NO_INVENTORY_CONTROL","sector":"플랫폼·콘텐츠·SW·보안","primary_archetype":"ad tech proxy without inventory control","loop_objective":"yellow_threshold_stress_test","trigger_type":"Stage3-Yellow","trigger_date":"2021-03-29","evidence_available_at_that_date":"Price momentum and weak confirmation, but still insufficient durable platform-owned inventory evidence.","evidence_source":"stock-web relative strength sequence","stage2_evidence_fields":["relative_strength"],"stage3_evidence_fields":["weak_revision","insufficient_durable_confirmation"],"stage4b_evidence_fields":[],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/216/216050/2021.csv","profile_path":"atlas/symbol_profiles/216/216050.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","entry_date":"2021-03-29","entry_price":60500,"MFE_30D_pct":4.96,"MFE_90D_pct":4.96,"MFE_180D_pct":4.96,"MFE_1Y_pct":4.96,"MFE_2Y_pct":null,"MAE_30D_pct":-9.59,"MAE_90D_pct":-14.88,"MAE_180D_pct":-14.88,"MAE_1Y_pct":-36.00,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2021-03-29","peak_price":63500,"drawdown_after_peak_pct":-36.00,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":null,"four_b_full_window_peak_proximity":null,"four_b_timing_verdict":"not_applicable","four_b_evidence_type":[],"four_c_protection_label":"not_applicable","trigger_outcome_label":"late_or_low_quality_yellow","current_profile_verdict":"current_profile_too_early","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"C26_INCROSS_20210329_60500","dedupe_for_aggregate":false,"aggregate_group_role":"label_comparison_only","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
```

### 25.4 score_simulation rows

```jsonl
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"C26_NAVER_202101_Q4_SEARCH_COMMERCE","trigger_id":"C26_NAVER_T1_STAGE2_20210129","symbol":"035420","large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE","raw_component_scores_before":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":6,"revision_score":10,"relative_strength_score":8,"customer_quality_score":11,"policy_or_regulatory_score":0,"valuation_repricing_score":8,"execution_risk_score":0,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0,"platform_owned_inventory_score":10},"weighted_score_before":78,"stage_label_before":"Stage3-Yellow","raw_component_scores_after":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":6,"revision_score":10,"relative_strength_score":8,"customer_quality_score":11,"policy_or_regulatory_score":0,"valuation_repricing_score":8,"execution_risk_score":0,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0,"platform_owned_inventory_score":14},"weighted_score_after":82,"stage_label_after":"Stage3-Yellow+","changed_components":["platform_owned_inventory_score"],"component_delta_explanation":"Owned search/commerce traffic supports C26 Stage2 bonus without forcing Green.","MFE_90D_pct":19.53,"MAE_90D_pct":-2.48,"score_return_alignment_label":"aligned_positive","current_profile_verdict":"current_profile_correct"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"C26_SOOP_202312_TWITCH_EXIT_MIGRATION","trigger_id":"C26_SOOP_T1_STAGE2_20231207","symbol":"067160","large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE","raw_component_scores_before":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":4,"revision_score":6,"relative_strength_score":13,"customer_quality_score":11,"policy_or_regulatory_score":0,"valuation_repricing_score":9,"execution_risk_score":2,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0,"platform_owned_inventory_score":9},"weighted_score_before":76,"stage_label_before":"Stage3-Yellow","raw_component_scores_after":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":4,"revision_score":6,"relative_strength_score":13,"customer_quality_score":11,"policy_or_regulatory_score":0,"valuation_repricing_score":9,"execution_risk_score":2,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0,"platform_owned_inventory_score":14},"weighted_score_after":81,"stage_label_after":"Stage3-Yellow+","changed_components":["platform_owned_inventory_score"],"component_delta_explanation":"Competitor-exit migration route is meaningful because SOOP owns the live-streaming platform inventory.","MFE_90D_pct":82.25,"MAE_90D_pct":-6.01,"score_return_alignment_label":"aligned_positive","current_profile_verdict":"current_profile_correct"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"C26_NASMEDIA_202102_AD_SPEND_PROXY","trigger_id":"C26_NASMEDIA_T1_STAGE2_20210205","symbol":"089600","large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE","raw_component_scores_before":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":3,"revision_score":7,"relative_strength_score":13,"customer_quality_score":4,"policy_or_regulatory_score":0,"valuation_repricing_score":9,"execution_risk_score":6,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0,"platform_owned_inventory_score":0},"weighted_score_before":76,"stage_label_before":"Stage3-Yellow","raw_component_scores_after":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":3,"revision_score":7,"relative_strength_score":10,"customer_quality_score":4,"policy_or_regulatory_score":0,"valuation_repricing_score":7,"execution_risk_score":8,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0,"platform_owned_inventory_score":0},"weighted_score_after":69,"stage_label_after":"Stage2-Watch","changed_components":["relative_strength_score","valuation_repricing_score","execution_risk_score"],"component_delta_explanation":"Ad-spend proxy lacks platform-owned inventory and should not receive C26 Stage2 promotion without margin bridge.","MFE_90D_pct":14.52,"MAE_90D_pct":-11.83,"score_return_alignment_label":"corrected_false_positive","current_profile_verdict":"current_profile_false_positive"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"C26_KAKAO_202109_PLATFORM_REGULATORY_BREAK","trigger_id":"C26_KAKAO_T1_4C_20210908","symbol":"035720","large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE","raw_component_scores_before":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":4,"revision_score":7,"relative_strength_score":4,"customer_quality_score":10,"policy_or_regulatory_score":-10,"valuation_repricing_score":6,"execution_risk_score":8,"legal_or_contract_risk_score":14,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0,"platform_owned_inventory_score":10},"weighted_score_before":72,"stage_label_before":"Stage2-Watch","raw_component_scores_after":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":0,"revision_score":0,"relative_strength_score":0,"customer_quality_score":0,"policy_or_regulatory_score":-15,"valuation_repricing_score":0,"execution_risk_score":10,"legal_or_contract_risk_score":18,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0,"platform_owned_inventory_score":0,"thesis_break_score":20},"weighted_score_after":"4C","stage_label_after":"4C","changed_components":["policy_or_regulatory_score","legal_or_contract_risk_score","thesis_break_score"],"component_delta_explanation":"Regulatory pressure changes C26 platform monetization thesis; route to 4C protection.","MFE_90D_pct":9.39,"MAE_90D_pct":-20.22,"score_return_alignment_label":"corrected_4C","current_profile_verdict":"current_profile_4C_too_late"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"C26_INCROSS_202102_AD_TECH_PROXY","trigger_id":"C26_INCROSS_T1_STAGE2_20210208","symbol":"216050","large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE","raw_component_scores_before":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":3,"revision_score":6,"relative_strength_score":13,"customer_quality_score":3,"policy_or_regulatory_score":0,"valuation_repricing_score":8,"execution_risk_score":6,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0,"platform_owned_inventory_score":0},"weighted_score_before":75,"stage_label_before":"Stage3-Yellow","raw_component_scores_after":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":3,"revision_score":6,"relative_strength_score":9,"customer_quality_score":3,"policy_or_regulatory_score":0,"valuation_repricing_score":6,"execution_risk_score":9,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0,"platform_owned_inventory_score":0},"weighted_score_after":68,"stage_label_after":"Stage2-Watch","changed_components":["relative_strength_score","valuation_repricing_score","execution_risk_score"],"component_delta_explanation":"Ad-tech proxy lacks owned traffic; cap Stage2 promotion unless durable margin bridge appears.","MFE_90D_pct":21.88,"MAE_90D_pct":-6.53,"score_return_alignment_label":"corrected_low_quality_proxy","current_profile_verdict":"current_profile_false_positive"}
```

### 25.5 shadow_weight rows

The CSV rows are provided in section 24 and are intentionally shadow-only.

### 25.6 residual_contribution row

```jsonl
{"row_type":"residual_contribution","round":"R13","loop":"34","large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE","new_independent_case_count":5,"reused_case_count":0,"new_symbol_count":5,"new_trigger_family_count":5,"tested_existing_calibrated_axes":["stage2_actionable_evidence_bonus","stage3_yellow_total_min","stage3_green_total_min","stage3_green_revision_min","price_only_blowoff_blocks_positive_stage","full_4b_requires_non_price_evidence","hard_4c_thesis_break_routes_to_4c"],"residual_error_types_found":["ad_proxy_false_positive","owned_platform_stage2_valid_but_green_late","regulation_thesis_break_4c_needs_speed"],"loop_contribution_label":"canonical_archetype_rule_candidate","do_not_propose_new_weight_delta":false}
```

### 25.7 narrative_only rows

```jsonl
{"row_type":"narrative_only","case_id":"NONE","symbol":null,"large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE","reason":"all selected cases had clean 180D stock-web windows; no narrative-only row needed","price_source":"Songdaiki/stock-web","usage":"not_weight_calibration"}
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
- Price shard pattern: atlas/ohlcv_tradable_by_symbol_year/&lt;prefix&gt;/&lt;ticker&gt;/&lt;year&gt;.csv.
- Symbol profile pattern: atlas/symbol_profiles/&lt;prefix&gt;/&lt;ticker&gt;.json.

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
next_round = R13_loop_35
next_large_sector_id = L8_PLATFORM_CONTENT_SW_SECURITY
next_canonical_archetype_id = C27_CONTENT_IP_GLOBAL_MONETIZATION
next_objective = separate platform ad operating leverage from content IP monetization; add positive/counterexample balance around IP export and monetization durability.
```

## 28. Source Notes

Stock-web source files inspected for this MD:

- `atlas/manifest.json`
- `atlas/symbol_profiles/035/035420.json`
- `atlas/symbol_profiles/035/035720.json`
- `atlas/symbol_profiles/067/067160.json`
- `atlas/symbol_profiles/089/089600.json`
- `atlas/symbol_profiles/216/216050.json`
- `atlas/ohlcv_tradable_by_symbol_year/035/035420/2021.csv`
- `atlas/ohlcv_tradable_by_symbol_year/035/035720/2021.csv`
- `atlas/ohlcv_tradable_by_symbol_year/067/067160/2023.csv`
- `atlas/ohlcv_tradable_by_symbol_year/067/067160/2024.csv`
- `atlas/ohlcv_tradable_by_symbol_year/089/089600/2021.csv`
- `atlas/ohlcv_tradable_by_symbol_year/216/216050/2021.csv`

Allowed stock_agent research artifacts checked for duplicate/coverage only:

- `reports/e2r_calibration/ingest_summary.md`
- `reports/e2r_calibration/calibrated_profile_report.md`
- repository search for `C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE`

No stock_agent source code was opened or inferred.
