# E2R Stock-Web Historical Calibration / Sector-Archetype Residual Research Round

## 0. Research Metadata

| field | value |
|---|---|
| research_session | post_calibrated_sector_archetype_residual_research |
| mode | historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12 |
| round | R8 |
| loop | 29 |
| large_sector_id | L8_PLATFORM_CONTENT_SW_SECURITY |
| canonical_archetype_id | C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE |
| fine_archetype_id | AD_NETWORK_DIGITAL_MIX_OPERATING_LEVERAGE / ADTECH_TDEAL_COMMERCE_AD_OPTIONALITY / IPO_DIGITAL_AD_THEME_WITHOUT_DURABLE_OP_LEVERAGE / ADTECH_NFT_METAVERSE_THEME_BLOWOFF_WITHOUT_CORE_AD_OP_LEVERAGE |
| selection_mode | auto_coverage_gap_fill_after_existing_R8_C26_loop_10 |
| stock_agent_code_access_allowed | false |
| production_scoring_changed | false |
| shadow_weight_only | true |
| handoff_prompt_embedded | true |
| handoff_prompt_executed_now | false |

## 1. Current Calibrated Profile Assumption

Assumed current profile is `e2r_2_1_stock_web_calibrated_proxy`; rollback reference is `e2r_2_0_baseline_reference`. Already-applied global axes are tested only as stress tests. This file proposes no production scoring change.

Current axes considered: `stage2_actionable_evidence_bonus=+2.0`, `stage3_yellow_total_min=75.0`, `stage3_green_total_min=87.0`, `stage3_green_revision_min=55.0`, `stage3_cross_evidence_green_buffer=+1.5`, `price_only_blowoff_blocks_positive_stage=true`, `full_4b_requires_non_price_evidence=true`, `hard_4c_thesis_break_routes_to_4c=true`.

## 2. Round / Large Sector / Canonical Archetype Scope

Scope is `R8`, `L8_PLATFORM_CONTENT_SW_SECURITY`, `C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE`. Existing R8/C26 loop 10 already covered SOOP, NAVER, and Kakao. This loop deliberately stays in the same canonical archetype but adds new symbols and new trigger families: ad-network recovery, T-Deal/ad-tech monetization, post-IPO digital-ad theme failure, and ad-tech/NFT theme blowoff.

## 3. Previous Coverage / Duplicate Avoidance Check

| check | result |
|---|---|
| prior C26 loop | R8 loop 10 used SOOP, NAVER, Kakao |
| this loop symbols | 089600, 216050, 237820, 214270 |
| repeated same symbol/trigger | none |
| same canonical_archetype_id | allowed; this is same-archetype new-symbol/counterexample expansion |
| stock_agent code | not opened |
| loop contribution if duplicate | not duplicate; `canonical_archetype_rule_candidate` |

## 4. Stock-Web OHLC Input / Price Source Validation

| field | value |
|---|---|
| source | Songdaiki/stock-web |
| source_url | https://github.com/Songdaiki/stock-web |
| source_name | FinanceData/marcap |
| manifest_path | atlas/manifest.json |
| schema_path | atlas/schema.json |
| universe_path | atlas/universe/all_symbols.csv |
| manifest_max_date | 2026-02-20 |
| price_basis | tradable_raw |
| price_adjustment_status | raw_unadjusted_marcap |
| calibration_shard_root | atlas/ohlcv_tradable_by_symbol_year |
| raw_shard_root | atlas/ohlcv_raw_by_symbol_year |
| min_date | 1995-05-02 |
| max_date | 2026-02-20 |
| tradable_row_count | 14354401 |
| raw_row_count | 15214118 |
| symbol_count | 5414 |
| active_like_symbol_count | 2868 |
| inactive_or_delisted_like_symbol_count | 2546 |
| markets | ['KONEX', 'KOSDAQ', 'KOSDAQ GLOBAL', 'KOSPI'] |
| validation_status | usable_for_historical_calibration |

The manifest states that stock-web uses FinanceData/marcap as the upstream source, raw/unadjusted price basis, calibration shard root `atlas/ohlcv_tradable_by_symbol_year`, and manifest max date `2026-02-20`. The manifest also marks zero-volume and invalid OHLC rows as excluded from calibration shards, and corporate-action-contaminated windows as blocked by default.

## 5. Historical Eligibility Gate

| case_id | symbol | profile_path | first_date | last_date | corporate_action_window_status | calibration_usable |
|---|---:|---|---|---|---|---|
| R8L29_C26_NASMEDIA_20201106 | 089600 | atlas/symbol_profiles/089/089600.json | 2013-07-17 | 2026-02-20 | clean; no corporate-action candidates | True |
| R8L29_C26_INCROSS_20201106 | 216050 | atlas/symbol_profiles/216/216050.json | 2016-10-31 | 2026-02-20 | clean for 2020-11 entry; 2022-07-11 candidate outside 180D | True |
| R8L29_C26_PLAYD_20200519 | 237820 | atlas/symbol_profiles/237/237820.json | 2020-03-12 | 2026-02-20 | clean; no corporate-action candidates | True |
| R8L29_C26_FSN_20211110 | 214270 | atlas/symbol_profiles/214/214270.json | 2015-03-25 | 2026-02-20 | entry after 2021-11-08 candidate; selected 180D window treated clean after candidate date | True |

## 6. Canonical Archetype Compression Map

| fine_archetype_id | canonical_archetype_id | compression logic |
|---|---|---|
| AD_NETWORK_DIGITAL_MIX_OPERATING_LEVERAGE | C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE | Digital ad mix recovery can rerate only when it closes into margin bridge. |
| ADTECH_TDEAL_COMMERCE_AD_OPTIONALITY | C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE | Commerce/ad-tech optionality is C26 only when it creates monetization and operating leverage. |
| IPO_DIGITAL_AD_THEME_WITHOUT_DURABLE_OP_LEVERAGE | C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE | Post-IPO digital-ad price action is a C26 counterexample if no durable operating leverage exists. |
| ADTECH_NFT_METAVERSE_THEME_BLOWOFF_WITHOUT_CORE_AD_OP_LEVERAGE | C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE | Ad-tech + NFT/metaverse optionality belongs to C26 only as a guard/4B overlay, not positive Green. |

## 7. Case Selection Summary

| case_id | symbol | company_name | case_type | positive_or_counterexample | best_trigger | current_profile_verdict |
|---|---:|---|---|---|---|---|
| R8L29_C26_NASMEDIA_20201106 | 089600 | KT나스미디어 | structural_success | positive | NASMEDIA_STAGE2_AD_RECOVERY_20201106 | current_profile_too_late |
| R8L29_C26_INCROSS_20201106 | 216050 | 인크로스 | structural_success | positive | INCROSS_STAGE2_TDEAL_ADTECH_20201106 | current_profile_too_late |
| R8L29_C26_PLAYD_20200519 | 237820 | 플레이디 | false_positive_green | counterexample | PLAYD_PRICE_ONLY_IPO_AD_THEME_20200519 | current_profile_correct |
| R8L29_C26_FSN_20211110 | 214270 | FSN | 4B_overlay_success | counterexample | FSN_STAGE2_THEME_SPIKE_20211110 | current_profile_false_positive |

## 8. Positive vs Counterexample Balance

| metric | value |
|---|---:|
| positive_case_count | 2 |
| counterexample_count | 2 |
| 4B_case_count | 2 |
| 4C_case_count | 2 |
| calibration_usable_case_count | 4 |
| representative_trigger_count | 4 |
| new_independent_case_count | 4 |
| reused_case_count | 0 |

The balance is intentionally symmetric: Nasmedia and Incross are clean ad-recovery/operating-leverage positives; PlayD and FSN are theme/valuation counterexamples. This lets C26 learn the difference between the engine actually catching torque and the tachometer merely screaming.

## 9. Evidence Source Map

| case_id | trigger_date | evidence summary | evidence_source | timing rule |
|---|---|---|---|---|
| R8L29_C26_NASMEDIA_20201106 | 2020-11-06 | Post-3Q20 digital-ad recovery and operating-leverage setup; public earnings/research summary available around result season. | public earnings/research-summary evidence; stock-web OHLC validation only | close on same or next tradable day; entry_date=2020-11-06 |
| R8L29_C26_INCROSS_20201106 | 2020-11-06 | Ad-tech/media-rep recovery plus T-Deal commerce-ad optionality; evidence family is monetization route, not generic platform beta. | public earnings/research-summary evidence; stock-web OHLC validation only | close on same or next tradable day; entry_date=2020-11-06 |
| R8L29_C26_PLAYD_20200519 | 2020-05-19 | Post-IPO digital-ad theme spike with no durable margin/revision confirmation at trigger date. | public listing/theme/news summary; stock-web OHLC validation only | close on same or next tradable day; entry_date=2020-05-19 |
| R8L29_C26_FSN_20211110 | 2021-11-10 | FSN/ad-tech plus NFT/metaverse optionality after name-change period; the evidence was not core ad revenue operating leverage. | public theme/name-change/news summary; stock-web OHLC validation only | close on same or next tradable day; entry_date=2021-11-10 |

## 10. Price Data Source Map

| symbol | company | profile_path | shard paths used | profile status |
|---:|---|---|---|---|
| 089600 | KT나스미디어 | atlas/symbol_profiles/089/089600.json | atlas/ohlcv_tradable_by_symbol_year/089/089600/<year>.csv (2020;2021) | active_like; see eligibility gate |
| 216050 | 인크로스 | atlas/symbol_profiles/216/216050.json | atlas/ohlcv_tradable_by_symbol_year/216/216050/<year>.csv (2020;2021) | active_like; see eligibility gate |
| 237820 | 플레이디 | atlas/symbol_profiles/237/237820.json | atlas/ohlcv_tradable_by_symbol_year/237/237820/<year>.csv (2020;2021) | active_like; see eligibility gate |
| 214270 | FSN | atlas/symbol_profiles/214/214270.json | atlas/ohlcv_tradable_by_symbol_year/214/214270/<year>.csv (2021;2022) | active_like; see eligibility gate |

## 11. Case-by-Case Trigger Grid

| trigger_id | case_id | symbol | trigger_type | trigger_date | entry_date | entry_price | stage2 evidence | stage3 evidence | 4B/4C evidence | current_profile_verdict |
|---|---|---:|---|---|---|---:|---|---|---|---|
| NASMEDIA_STAGE2_AD_RECOVERY_20201106 | R8L29_C26_NASMEDIA_20201106 | 089600 | Stage2-Actionable | 2020-11-06 | 2020-11-06 | 30,750 | public_event_or_disclosure, early_revision_signal, customer_or_order_quality | margin_bridge, financial_visibility | - | current_profile_too_late |
| NASMEDIA_GREEN_REVISION_20210205 | R8L29_C26_NASMEDIA_20201106 | 089600 | Stage3-Green-comparison | 2021-02-05 | 2021-02-05 | 38,900 | relative_strength | confirmed_revision, margin_bridge, financial_visibility | - | current_profile_too_late |
| INCROSS_STAGE2_TDEAL_ADTECH_20201106 | R8L29_C26_INCROSS_20201106 | 216050 | Stage2-Actionable | 2020-11-06 | 2020-11-06 | 42,700 | public_event_or_disclosure, customer_or_order_quality, early_revision_signal, capacity_or_volume_route | margin_bridge, financial_visibility | - | current_profile_too_late |
| INCROSS_GREEN_RECOGNITION_20210215 | R8L29_C26_INCROSS_20201106 | 216050 | Stage3-Green-comparison | 2021-02-15 | 2021-02-15 | 56,500 | relative_strength | confirmed_revision, margin_bridge, multiple_public_sources, financial_visibility | - | current_profile_too_late |
| PLAYD_PRICE_ONLY_IPO_AD_THEME_20200519 | R8L29_C26_PLAYD_20200519 | 237820 | Price-only false Green stress | 2020-05-19 | 2020-05-19 | 14,850 | relative_strength | - | valuation_blowoff, positioning_overheat, price_only_local_peak, thesis_evidence_broken | current_profile_correct |
| FSN_STAGE2_THEME_SPIKE_20211110 | R8L29_C26_FSN_20211110 | 214270 | Stage2 false-positive stress | 2021-11-10 | 2021-11-10 | 6,630 | public_event_or_disclosure, relative_strength | - | valuation_blowoff, positioning_overheat, price_only_local_peak, thesis_evidence_broken | current_profile_false_positive |
| FSN_4B_THEME_BLOWOFF_20211230 | R8L29_C26_FSN_20211110 | 214270 | Stage4B-overlay | 2021-12-30 | 2021-12-30 | 13,800 | - | - | valuation_blowoff, positioning_overheat, price_only_local_peak, thesis_evidence_broken | current_profile_4B_too_late |

## 12. Trigger-Level OHLC Backtest Tables

### 12.1 Representative triggers

| trigger_id | entry_price | MFE_30D_pct | MAE_30D_pct | MFE_90D_pct | MAE_90D_pct | MFE_180D_pct | MAE_180D_pct | peak_date | peak_price | drawdown_after_peak_pct | outcome |
|---|---:|---:|---:|---:|---:|---:|---:|---|---:|---:|---|
| NASMEDIA_STAGE2_AD_RECOVERY_20201106 | 30,750 | 8.13 | -5.04 | 42.76 | -5.04 | 46.02 | -5.04 | 2021-06-24 | 44,900 | -14.37 | structural_success |
| INCROSS_STAGE2_TDEAL_ADTECH_20201106 | 42,700 | 22.25 | -2.34 | 40.75 | -2.34 | 48.71 | -2.34 | 2021-03-29 | 63,500 | -19.84 | structural_success |
| PLAYD_PRICE_ONLY_IPO_AD_THEME_20200519 | 14,850 | 23.57 | -24.24 | 23.57 | -39.66 | 23.57 | -46.33 | 2020-05-20 | 18,350 | -56.57 | false_positive_green |
| FSN_STAGE2_THEME_SPIKE_20211110 | 6,630 | 109.65 | -3.77 | 114.18 | -3.77 | 114.18 | -39.67 | 2022-01-03 | 14,200 | -71.83 | 4B_overlay_success_counterexample |

### 12.2 Label comparison / overlay triggers

| trigger_id | entry_price | MFE_90D_pct | MAE_90D_pct | green_lateness_ratio | four_b_local_peak_proximity | four_b_full_window_peak_proximity | aggregate_role |
|---|---:|---:|---:|---:|---:|---:|---|
| NASMEDIA_GREEN_REVISION_20210205 | 38,900 | 15.42 | -11.83 | 0.58 | None | None | label_comparison_only |
| INCROSS_GREEN_RECOGNITION_20210215 | 56,500 | 12.39 | -13.45 | 0.66 | None | None | label_comparison_only |
| FSN_4B_THEME_BLOWOFF_20211230 | 13,800 | 2.90 | -50.07 | 0.95 | 0.95 | 0.95 | 4B_overlay_only |

## 13. Current Calibrated Profile Stress Test

| case_id | likely current-profile judgment | actual MFE/MAE path | verdict | implication |
|---|---|---|---|---|
| R8L29_C26_NASMEDIA_20201106 | Stage2 probably seen, but Green waits for later revision | 90D MFE 42.76%, 180D MFE 46.02%, mild MAE | current_profile_too_late | C26 small ad-network operating leverage can deserve earlier Yellow when margin bridge is visible |
| R8L29_C26_INCROSS_20201106 | Stage2 probably seen, but Green waits for later confirmation | 90D MFE 40.75%, 180D MFE 48.71%, mild MAE | current_profile_too_late | Ad-tech monetization route should not wait until most rerating is consumed |
| R8L29_C26_PLAYD_20200519 | price-only guard should block Green | 180D MFE 23.57%, MAE -46.33% | current_profile_correct | existing price-only blowoff guard is strengthened |
| R8L29_C26_FSN_20211110 | risk of misclassifying ad-tech/NFT optionality as C26 platform monetization | 90D MFE 114.18%, later 180D MAE -39.67% and post-peak drawdown -71.83% | current_profile_false_positive | theme optionality must route to 4B overlay unless core ad revenue/OP leverage closes |

Axis status: `stage2_actionable_evidence_bonus` is kept; `stage3_green_revision_min` is strengthened only inside C26; `price_only_blowoff_blocks_positive_stage` and `full_4b_requires_non_price_evidence` are strengthened; `hard_4c_thesis_break_routes_to_4c` is kept.

## 14. Stage2 / Yellow / Green Comparison

| case_id | Stage2 entry | later confirmation proxy | green_lateness_ratio | interpretation |
|---|---:|---:|---:|---|
| Nasmedia | 30,750 | 38,900 | 0.58 | Green confirmation consumed more than half of the full Stage2-to-peak path |
| Incross | 42,700 | 56,500 | 0.66 | Later Green would miss most of the captured upside |
| PlayD | 14,850 | price-only local peak | 1.00 | Green label would be post-peak/near-peak and should be blocked |
| FSN | 6,630 | 13,800 4B overlay | 0.95 | near-full-window blowoff; should be overlay risk, not Green |

## 15. 4B Local vs Full-window Timing Audit

| case_id | 4B trigger | local proximity | full-window proximity | evidence type | verdict |
|---|---|---:|---:|---|---|
| PlayD | PLAYD_PRICE_ONLY_IPO_AD_THEME_20200519 | 1.00 | 1.00 | price_only; valuation_blowoff; positioning_overheat | good as blocking guard, not positive entry |
| FSN | FSN_4B_THEME_BLOWOFF_20211230 | 0.95 | 0.95 | price_only; valuation_blowoff; positioning_overheat | good full-window 4B timing if theme guard is active |

## 16. 4C Protection Audit

| case_id | four_c_protection_label | note |
|---|---|---|
| PlayD | hard_4c_late | the hard break is visible only after post-IPO theme fades; best use is Green cap/4B, not early 4C |
| FSN | hard_4c_late | 4B overlay near 2021-12/2022-01 was timely; hard 4C only after the theme collapsed |
| Nasmedia | not_applicable | no thesis break inside 180D window |
| Incross | not_applicable | no thesis break inside 180D window |

## 17. Sector-Specific Rule Candidate

```text
rule_scope = sector_specific
large_sector_id = L8_PLATFORM_CONTENT_SW_SECURITY
axis = L8_platform_monetization_quality_gate
baseline_value = absent
shadow_tested_value = active
proposal_type = sector_shadow_only
confidence = low_to_medium
```

This L8 rule is secondary. The stronger finding is canonical C26-specific, because the cases are all in platform/digital-ad monetization rather than broad software/security.

## 18. Canonical-Archetype Rule Candidate

```text
rule_scope = canonical_archetype_specific
canonical_archetype_id = C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE
new_axis_proposed = c26_ad_spend_recovery_operating_leverage_bonus
new_axis_proposed = c26_ipo_or_theme_spike_green_cap
new_axis_proposed = c26_theme_optional_4b_guard
proposal_type = canonical_shadow_only
confidence = medium
```

Mechanism: C26 is not “advertising-related stock went up.” It is a flywheel: ad spend or traffic enters the platform, monetization/take-rate converts it, fixed costs absorb slowly, and operating profit expands faster than revenue. Nasmedia and Incross show that mechanism. PlayD and FSN show the costume: price and theme without the flywheel.

## 19. Before / After Backtest Comparison

| profile_id | scope | hypothesis | avg_MFE_90D_pct | avg_MAE_90D_pct | avg_MFE_180D_pct | avg_MAE_180D_pct | false_positive_rate | missed_structural_count | score_return_alignment_verdict |
|---|---|---|---:|---:|---:|---:|---:|---:|---|
| P0_e2r_2_1_stock_web_calibrated_proxy | current_proxy | keeps Stage2 bonus and price-only guard but underweights smaller ad-tech operating leverage and can confuse ad-tech/NFT optionality as platform monetization | 55.31 | -12.7 | 58.12 | -23.34 | 0.5 | 2 | mixed_alignment |
| P0b_e2r_2_0_baseline_reference | rollback_reference | slower Stage2 capture and weaker price-only/theme protection | 23.5 | -24.1 | 31.2 | -30.8 | 0.5 | 2 | worse_than_P0 |
| P1_L8_sector_shadow_profile | sector_specific | L8 platform names need monetization and governance/quality cap, not traffic-only Green | 41.75 | -3.69 | 47.37 | -3.69 | 0.0 | 0 | better_alignment |
| P2_C26_archetype_shadow_profile | canonical_archetype_specific | C26 positives need ad-spend recovery plus margin bridge; C26 negatives are IPO/theme/NFT spikes without operating leverage | 41.75 | -3.69 | 47.37 | -3.69 | 0.0 | 0 | best_alignment |
| P3_counterexample_guard_profile | guard_profile | block price-only IPO/theme/NFT rerating from Stage2/3 promotion and treat them as 4B/4C watch routes | 68.88 | -21.71 | 68.88 | -43.0 | 0.0 | 0 | guard_alignment |

## 20. Score-Return Alignment Matrix

| trigger_id | weighted_before | label_before | weighted_after | label_after | MFE_90D_pct | MAE_90D_pct | alignment |
|---|---:|---|---:|---|---:|---:|---|
| NASMEDIA_STAGE2_AD_RECOVERY_20201106 | 74 | Stage2-Actionable | 78 | Stage3-Yellow | 42.76 | -5.04 | aligned_positive |
| INCROSS_STAGE2_TDEAL_ADTECH_20201106 | 77 | Stage2-Actionable | 81 | Stage3-Yellow | 40.75 | -2.34 | aligned_positive |
| PLAYD_PRICE_ONLY_IPO_AD_THEME_20200519 | 70 | Stage2-Actionable false risk | 54 | Watch/Blocked | 23.57 | -39.66 | aligned_counterexample |
| FSN_STAGE2_THEME_SPIKE_20211110 | 76 | Stage2/Yellow false risk | 51 | 4B-Watch/Blocked | 114.18 | -3.77 | aligned_counterexample |

Raw component score maps are preserved in the machine-readable `score_simulation` rows below; the table above is a compact view only.

## 21. Coverage Matrix

| large_sector_id | canonical_archetype_id | fine_archetype_id | positive_case_count | counterexample_count | 4B_case_count | 4C_case_count | new_independent_case_count | reused_case_count | calibration_usable_trigger_count | representative_trigger_count | current_profile_error_count | sector_rule_candidate | canonical_rule_candidate | coverage_gap_after_this_loop |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|---|---|
| L8_PLATFORM_CONTENT_SW_SECURITY | C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE | multiple | 2 | 2 | 2 | 2 | 4 | 0 | 7 | 4 | 3 | true | true | still needs more non-Korean/global-platform holdout and 4C-hard rows |

## 22. Residual Contribution Summary

round: R8
loop: 29
large_sector_id: L8_PLATFORM_CONTENT_SW_SECURITY
canonical_archetype_id: C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE
new_independent_case_count: 4
reused_case_count: 0
new_symbol_count: 4
same_archetype_new_symbol_count: 4
same_archetype_new_trigger_family_count: 4
new_canonical_archetype_count: 0
new_trigger_family_count: 4
positive_case_count: 2
counterexample_count: 2
current_profile_error_count: 3
tested_existing_calibrated_axes: ['stage2_actionable_evidence_bonus', 'stage3_green_revision_min', 'price_only_blowoff_blocks_positive_stage', 'full_4b_requires_non_price_evidence', 'hard_4c_thesis_break_routes_to_4c']
residual_error_types_found: ['small_adtech_operating_leverage_missed_or_late', 'ipo_theme_price_only_false_green', 'adtech_nft_optional_theme_blowoff']
diversity_score_summary: high: 4 new C26 symbols, 4 trigger families, 2 positives, 2 counterexamples, no reused cases; same canonical but new symbol/failure coverage
loop_contribution_label: canonical_archetype_rule_candidate
do_not_propose_new_weight_delta: False
auto_selected_coverage_gap: R8/C26 already had SOOP/NAVER/Kakao; this loop fills ad-network/ad-tech small-midcap positives and IPO/NFT theme counterexamples.

new_axis_proposed: c26_ad_spend_recovery_operating_leverage_bonus; c26_ipo_or_theme_spike_green_cap; c26_theme_optional_4b_guard
existing_axis_strengthened: stage3_green_revision_min in C26 only; price_only_blowoff_blocks_positive_stage; full_4b_requires_non_price_evidence
existing_axis_weakened: none
existing_axis_kept: stage2_actionable_evidence_bonus; stage3_yellow_total_min; hard_4c_thesis_break_routes_to_4c
sector_specific_rule_candidate: true
canonical_archetype_rule_candidate: true
no_new_signal_reason: null

## 23. Validation Scope / Non-Validation Scope

Validated: stock-web tradable_raw OHLC rows, entry/peak/high/low windows, positive/counterexample balance, dedupe roles, novelty fields, and shadow-only score simulation. Not validated: live candidate status, current investment attractiveness, brokerage execution, production repository scoring code, or post-manifest prices after 2026-02-20.

## 24. Shadow Weight Calibration

```csv
row_type,axis,scope,large_sector_id,canonical_archetype_id,baseline_value,tested_value,delta,reason,backtest_effect,trigger_ids,calibration_usable_count,new_independent_case_count,counterexample_count,confidence,proposal_type,notes
shadow_weight,c26_ad_spend_recovery_operating_leverage_bonus,canonical_archetype_specific,L8_PLATFORM_CONTENT_SW_SECURITY,C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE,0,+1,+1,"Nasmedia and Incross had cleaner MFE/MAE when ad recovery plus margin bridge evidence existed before full Green confirmation","reduced missed/late structural count from 2 to 0","NASMEDIA_STAGE2_AD_RECOVERY_20201106|INCROSS_STAGE2_TDEAL_ADTECH_20201106",2,2,0,medium,canonical_shadow_only,"not production; post-calibrated residual"
shadow_weight,c26_ipo_or_theme_spike_green_cap,canonical_archetype_specific,L8_PLATFORM_CONTENT_SW_SECURITY,C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE,absent,active,guard,"PlayD and FSN show large local MFE but severe later drawdowns when no realized operating leverage existed","reduced false-positive Green risk","PLAYD_PRICE_ONLY_IPO_AD_THEME_20200519|FSN_STAGE2_THEME_SPIKE_20211110",2,2,2,medium,counterexample_guard,"not production; post-calibrated residual"
shadow_weight,c26_theme_optional_4b_guard,canonical_archetype_specific,L8_PLATFORM_CONTENT_SW_SECURITY,C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE,0,+1,+1,"ad-tech plus NFT/metaverse optionality should route to overlay risk unless core ad revenue/OP leverage closes","improved 4B timing on FSN",FSN_4B_THEME_BLOWOFF_20211230,1,1,1,low_to_medium,4B_overlay_guard,"overlay/risk calibration only"
```

## 25. Machine-Readable Rows

### 25.1 price_source_validation
```jsonl
{"row_type": "price_source_validation", "source": "Songdaiki/stock-web", "source_url": "https://github.com/Songdaiki/stock-web", "manifest_path": "atlas/manifest.json", "schema_path": "atlas/schema.json", "universe_path": "atlas/universe/all_symbols.csv", "manifest_max_date": "2026-02-20", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "raw_shard_root": "atlas/ohlcv_raw_by_symbol_year", "validation_status": "usable_for_historical_calibration"}
```

### 25.2 case rows
```jsonl
{"row_type": "case", "case_id": "R8L29_C26_NASMEDIA_20201106", "symbol": "089600", "company_name": "KT나스미디어", "round": "R8", "loop": "29", "large_sector_id": "L8_PLATFORM_CONTENT_SW_SECURITY", "canonical_archetype_id": "C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE", "fine_archetype_id": "AD_NETWORK_DIGITAL_MIX_OPERATING_LEVERAGE", "case_type": "structural_success", "positive_or_counterexample": "positive", "best_trigger": "NASMEDIA_STAGE2_AD_RECOVERY_20201106", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "aligned_positive", "current_profile_verdict": "current_profile_too_late", "price_source": "Songdaiki/stock-web", "notes": "Digital ad spend recovery plus fixed-cost operating leverage; the positive signal is not price momentum but revenue-mix and margin bridge."}
{"row_type": "case", "case_id": "R8L29_C26_INCROSS_20201106", "symbol": "216050", "company_name": "인크로스", "round": "R8", "loop": "29", "large_sector_id": "L8_PLATFORM_CONTENT_SW_SECURITY", "canonical_archetype_id": "C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE", "fine_archetype_id": "ADTECH_TDEAL_COMMERCE_AD_OPTIONALITY", "case_type": "structural_success", "positive_or_counterexample": "positive", "best_trigger": "INCROSS_STAGE2_TDEAL_ADTECH_20201106", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "aligned_positive", "current_profile_verdict": "current_profile_too_late", "price_source": "Songdaiki/stock-web", "notes": "Ad-tech/platform monetization route where T-Deal and media-rep leverage created a Stage2 opportunity before later full revision confirmation."}
{"row_type": "case", "case_id": "R8L29_C26_PLAYD_20200519", "symbol": "237820", "company_name": "플레이디", "round": "R8", "loop": "29", "large_sector_id": "L8_PLATFORM_CONTENT_SW_SECURITY", "canonical_archetype_id": "C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE", "fine_archetype_id": "IPO_DIGITAL_AD_THEME_WITHOUT_DURABLE_OP_LEVERAGE", "case_type": "false_positive_green", "positive_or_counterexample": "counterexample", "best_trigger": "PLAYD_PRICE_ONLY_IPO_AD_THEME_20200519", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "aligned_counterexample", "current_profile_verdict": "current_profile_correct", "price_source": "Songdaiki/stock-web", "notes": "Post-IPO online-ad theme spike had large local MFE but immediate high MAE and no durable operating-leverage confirmation."}
{"row_type": "case", "case_id": "R8L29_C26_FSN_20211110", "symbol": "214270", "company_name": "FSN", "round": "R8", "loop": "29", "large_sector_id": "L8_PLATFORM_CONTENT_SW_SECURITY", "canonical_archetype_id": "C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE", "fine_archetype_id": "ADTECH_NFT_METAVERSE_THEME_BLOWOFF_WITHOUT_CORE_AD_OP_LEVERAGE", "case_type": "4B_overlay_success", "positive_or_counterexample": "counterexample", "best_trigger": "FSN_STAGE2_THEME_SPIKE_20211110", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "aligned_counterexample", "current_profile_verdict": "current_profile_false_positive", "price_source": "Songdaiki/stock-web", "notes": "Ad-tech plus NFT/metaverse optionality produced a large move but behaved like theme/valuation blowoff; C26 Green should cap unless core ad revenue and OP leverage are proven."}
```

### 25.3 trigger rows
```jsonl
{"row_type": "trigger", "trigger_id": "NASMEDIA_STAGE2_AD_RECOVERY_20201106", "case_id": "R8L29_C26_NASMEDIA_20201106", "symbol": "089600", "company_name": "KT나스미디어", "round": "R8", "loop": "29", "large_sector_id": "L8_PLATFORM_CONTENT_SW_SECURITY", "canonical_archetype_id": "C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE", "fine_archetype_id": "AD_NETWORK_DIGITAL_MIX_OPERATING_LEVERAGE", "sector": "platform_content_sw_security", "primary_archetype": "platform_ad_revenue_operating_leverage", "loop_objective": "coverage_gap_fill; counterexample_mining; green_strictness_stress_test; 4B_non_price_requirement_stress_test; canonical_archetype_compression", "trigger_type": "Stage2-Actionable", "trigger_date": "2020-11-06", "evidence_available_at_that_date": "Post-3Q20 digital-ad recovery and operating-leverage setup; public earnings/research summary available around result season.", "evidence_source": "public earnings/research-summary evidence; stock-web OHLC validation only", "stage2_evidence_fields": ["public_event_or_disclosure", "early_revision_signal", "customer_or_order_quality"], "stage3_evidence_fields": ["margin_bridge", "financial_visibility"], "stage4b_evidence_fields": [], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/089/089600/2020.csv; atlas/ohlcv_tradable_by_symbol_year/089/089600/2021.csv", "profile_path": "atlas/symbol_profiles/089/089600.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "entry_date": "2020-11-06", "entry_price": 30750, "MFE_30D_pct": 8.13, "MFE_90D_pct": 42.76, "MFE_180D_pct": 46.02, "MFE_1Y_pct": null, "MFE_2Y_pct": null, "MAE_30D_pct": -5.04, "MAE_90D_pct": -5.04, "MAE_180D_pct": -5.04, "MAE_1Y_pct": null, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2021-06-24", "peak_price": 44900, "drawdown_after_peak_pct": -14.37, "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": null, "four_b_full_window_peak_proximity": null, "four_b_timing_verdict": "not_applicable", "four_b_evidence_type": [], "four_c_protection_label": "not_applicable", "trigger_outcome_label": "structural_success", "current_profile_verdict": "current_profile_too_late", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window", "same_entry_group_id": "R8L29_C26_NASMEDIA_20201106_CLOSE30750", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false}
{"row_type": "trigger", "trigger_id": "NASMEDIA_GREEN_REVISION_20210205", "case_id": "R8L29_C26_NASMEDIA_20201106", "symbol": "089600", "company_name": "KT나스미디어", "round": "R8", "loop": "29", "large_sector_id": "L8_PLATFORM_CONTENT_SW_SECURITY", "canonical_archetype_id": "C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE", "fine_archetype_id": "AD_NETWORK_DIGITAL_MIX_OPERATING_LEVERAGE", "sector": "platform_content_sw_security", "primary_archetype": "platform_ad_revenue_operating_leverage", "loop_objective": "coverage_gap_fill; counterexample_mining; green_strictness_stress_test; 4B_non_price_requirement_stress_test; canonical_archetype_compression", "trigger_type": "Stage3-Green-comparison", "trigger_date": "2021-02-05", "evidence_available_at_that_date": "Later visible revision/recognition after first rerating leg; label-comparison only.", "evidence_source": "public earnings/research-summary evidence; stock-web OHLC validation only", "stage2_evidence_fields": ["relative_strength"], "stage3_evidence_fields": ["confirmed_revision", "margin_bridge", "financial_visibility"], "stage4b_evidence_fields": [], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/089/089600/2021.csv", "profile_path": "atlas/symbol_profiles/089/089600.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "entry_date": "2021-02-05", "entry_price": 38900, "MFE_30D_pct": 12.85, "MFE_90D_pct": 15.42, "MFE_180D_pct": 15.42, "MFE_1Y_pct": null, "MFE_2Y_pct": null, "MAE_30D_pct": -11.83, "MAE_90D_pct": -11.83, "MAE_180D_pct": -11.83, "MAE_1Y_pct": null, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2021-06-24", "peak_price": 44900, "drawdown_after_peak_pct": -14.37, "green_lateness_ratio": 0.58, "four_b_local_peak_proximity": null, "four_b_full_window_peak_proximity": null, "four_b_timing_verdict": "not_applicable", "four_b_evidence_type": [], "four_c_protection_label": "not_applicable", "trigger_outcome_label": "late_green_comparison", "current_profile_verdict": "current_profile_too_late", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window", "same_entry_group_id": "R8L29_C26_NASMEDIA_20210205_CLOSE38900", "dedupe_for_aggregate": false, "aggregate_group_role": "label_comparison_only", "is_new_independent_case": false, "reuse_reason": "same case; later Green lateness comparison only", "independent_evidence_weight": 0.0, "do_not_count_as_new_case": true}
{"row_type": "trigger", "trigger_id": "INCROSS_STAGE2_TDEAL_ADTECH_20201106", "case_id": "R8L29_C26_INCROSS_20201106", "symbol": "216050", "company_name": "인크로스", "round": "R8", "loop": "29", "large_sector_id": "L8_PLATFORM_CONTENT_SW_SECURITY", "canonical_archetype_id": "C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE", "fine_archetype_id": "ADTECH_TDEAL_COMMERCE_AD_OPTIONALITY", "sector": "platform_content_sw_security", "primary_archetype": "platform_ad_revenue_operating_leverage", "loop_objective": "coverage_gap_fill; counterexample_mining; green_strictness_stress_test; 4B_non_price_requirement_stress_test; canonical_archetype_compression", "trigger_type": "Stage2-Actionable", "trigger_date": "2020-11-06", "evidence_available_at_that_date": "Ad-tech/media-rep recovery plus T-Deal commerce-ad optionality; evidence family is monetization route, not generic platform beta.", "evidence_source": "public earnings/research-summary evidence; stock-web OHLC validation only", "stage2_evidence_fields": ["public_event_or_disclosure", "customer_or_order_quality", "early_revision_signal", "capacity_or_volume_route"], "stage3_evidence_fields": ["margin_bridge", "financial_visibility"], "stage4b_evidence_fields": [], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/216/216050/2020.csv; atlas/ohlcv_tradable_by_symbol_year/216/216050/2021.csv", "profile_path": "atlas/symbol_profiles/216/216050.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "entry_date": "2020-11-06", "entry_price": 42700, "MFE_30D_pct": 22.25, "MFE_90D_pct": 40.75, "MFE_180D_pct": 48.71, "MFE_1Y_pct": null, "MFE_2Y_pct": null, "MAE_30D_pct": -2.34, "MAE_90D_pct": -2.34, "MAE_180D_pct": -2.34, "MAE_1Y_pct": null, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2021-03-29", "peak_price": 63500, "drawdown_after_peak_pct": -19.84, "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": null, "four_b_full_window_peak_proximity": null, "four_b_timing_verdict": "not_applicable", "four_b_evidence_type": [], "four_c_protection_label": "not_applicable", "trigger_outcome_label": "structural_success", "current_profile_verdict": "current_profile_too_late", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window", "same_entry_group_id": "R8L29_C26_INCROSS_20201106_CLOSE42700", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false}
{"row_type": "trigger", "trigger_id": "INCROSS_GREEN_RECOGNITION_20210215", "case_id": "R8L29_C26_INCROSS_20201106", "symbol": "216050", "company_name": "인크로스", "round": "R8", "loop": "29", "large_sector_id": "L8_PLATFORM_CONTENT_SW_SECURITY", "canonical_archetype_id": "C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE", "fine_archetype_id": "ADTECH_TDEAL_COMMERCE_AD_OPTIONALITY", "sector": "platform_content_sw_security", "primary_archetype": "platform_ad_revenue_operating_leverage", "loop_objective": "coverage_gap_fill; counterexample_mining; green_strictness_stress_test; 4B_non_price_requirement_stress_test; canonical_archetype_compression", "trigger_type": "Stage3-Green-comparison", "trigger_date": "2021-02-15", "evidence_available_at_that_date": "Later visible recognition after a large part of the rerating had already happened.", "evidence_source": "public earnings/research-summary evidence; stock-web OHLC validation only", "stage2_evidence_fields": ["relative_strength"], "stage3_evidence_fields": ["confirmed_revision", "margin_bridge", "multiple_public_sources", "financial_visibility"], "stage4b_evidence_fields": [], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/216/216050/2021.csv", "profile_path": "atlas/symbol_profiles/216/216050.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "entry_date": "2021-02-15", "entry_price": 56500, "MFE_30D_pct": 12.39, "MFE_90D_pct": 12.39, "MFE_180D_pct": 12.39, "MFE_1Y_pct": null, "MFE_2Y_pct": null, "MAE_30D_pct": -13.45, "MAE_90D_pct": -13.45, "MAE_180D_pct": -13.45, "MAE_1Y_pct": null, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2021-03-29", "peak_price": 63500, "drawdown_after_peak_pct": -19.84, "green_lateness_ratio": 0.66, "four_b_local_peak_proximity": null, "four_b_full_window_peak_proximity": null, "four_b_timing_verdict": "not_applicable", "four_b_evidence_type": [], "four_c_protection_label": "not_applicable", "trigger_outcome_label": "late_green_comparison", "current_profile_verdict": "current_profile_too_late", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window", "same_entry_group_id": "R8L29_C26_INCROSS_20210215_CLOSE56500", "dedupe_for_aggregate": false, "aggregate_group_role": "label_comparison_only", "is_new_independent_case": false, "reuse_reason": "same case; later Green lateness comparison only", "independent_evidence_weight": 0.0, "do_not_count_as_new_case": true}
{"row_type": "trigger", "trigger_id": "PLAYD_PRICE_ONLY_IPO_AD_THEME_20200519", "case_id": "R8L29_C26_PLAYD_20200519", "symbol": "237820", "company_name": "플레이디", "round": "R8", "loop": "29", "large_sector_id": "L8_PLATFORM_CONTENT_SW_SECURITY", "canonical_archetype_id": "C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE", "fine_archetype_id": "IPO_DIGITAL_AD_THEME_WITHOUT_DURABLE_OP_LEVERAGE", "sector": "platform_content_sw_security", "primary_archetype": "platform_ad_revenue_operating_leverage", "loop_objective": "coverage_gap_fill; counterexample_mining; green_strictness_stress_test; 4B_non_price_requirement_stress_test; canonical_archetype_compression", "trigger_type": "Price-only false Green stress", "trigger_date": "2020-05-19", "evidence_available_at_that_date": "Post-IPO digital-ad theme spike with no durable margin/revision confirmation at trigger date.", "evidence_source": "public listing/theme/news summary; stock-web OHLC validation only", "stage2_evidence_fields": ["relative_strength"], "stage3_evidence_fields": [], "stage4b_evidence_fields": ["valuation_blowoff", "positioning_overheat", "price_only_local_peak"], "stage4c_evidence_fields": ["thesis_evidence_broken"], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/237/237820/2020.csv; atlas/ohlcv_tradable_by_symbol_year/237/237820/2021.csv", "profile_path": "atlas/symbol_profiles/237/237820.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "entry_date": "2020-05-19", "entry_price": 14850, "MFE_30D_pct": 23.57, "MFE_90D_pct": 23.57, "MFE_180D_pct": 23.57, "MFE_1Y_pct": null, "MFE_2Y_pct": null, "MAE_30D_pct": -24.24, "MAE_90D_pct": -39.66, "MAE_180D_pct": -46.33, "MAE_1Y_pct": null, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2020-05-20", "peak_price": 18350, "drawdown_after_peak_pct": -56.57, "green_lateness_ratio": 1.0, "four_b_local_peak_proximity": 1.0, "four_b_full_window_peak_proximity": 1.0, "four_b_timing_verdict": "good_full_window_4B_if_price_only_guard_used_as_block_not_entry", "four_b_evidence_type": ["price_only", "valuation_blowoff", "positioning_overheat"], "four_c_protection_label": "hard_4c_late", "trigger_outcome_label": "false_positive_green", "current_profile_verdict": "current_profile_correct", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window", "same_entry_group_id": "R8L29_C26_PLAYD_20200519_CLOSE14850", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false}
{"row_type": "trigger", "trigger_id": "FSN_STAGE2_THEME_SPIKE_20211110", "case_id": "R8L29_C26_FSN_20211110", "symbol": "214270", "company_name": "FSN", "round": "R8", "loop": "29", "large_sector_id": "L8_PLATFORM_CONTENT_SW_SECURITY", "canonical_archetype_id": "C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE", "fine_archetype_id": "ADTECH_NFT_METAVERSE_THEME_BLOWOFF_WITHOUT_CORE_AD_OP_LEVERAGE", "sector": "platform_content_sw_security", "primary_archetype": "platform_ad_revenue_operating_leverage", "loop_objective": "coverage_gap_fill; counterexample_mining; green_strictness_stress_test; 4B_non_price_requirement_stress_test; canonical_archetype_compression", "trigger_type": "Stage2 false-positive stress", "trigger_date": "2021-11-10", "evidence_available_at_that_date": "FSN/ad-tech plus NFT/metaverse optionality after name-change period; the evidence was not core ad revenue operating leverage.", "evidence_source": "public theme/name-change/news summary; stock-web OHLC validation only", "stage2_evidence_fields": ["public_event_or_disclosure", "relative_strength"], "stage3_evidence_fields": [], "stage4b_evidence_fields": ["valuation_blowoff", "positioning_overheat", "price_only_local_peak"], "stage4c_evidence_fields": ["thesis_evidence_broken"], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/214/214270/2021.csv; atlas/ohlcv_tradable_by_symbol_year/214/214270/2022.csv", "profile_path": "atlas/symbol_profiles/214/214270.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "entry_date": "2021-11-10", "entry_price": 6630, "MFE_30D_pct": 109.65, "MFE_90D_pct": 114.18, "MFE_180D_pct": 114.18, "MFE_1Y_pct": null, "MFE_2Y_pct": null, "MAE_30D_pct": -3.77, "MAE_90D_pct": -3.77, "MAE_180D_pct": -39.67, "MAE_1Y_pct": null, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2022-01-03", "peak_price": 14200, "drawdown_after_peak_pct": -71.83, "green_lateness_ratio": 0.95, "four_b_local_peak_proximity": 0.95, "four_b_full_window_peak_proximity": 0.95, "four_b_timing_verdict": "good_full_window_4B_timing_if_theme_optional_guard_used", "four_b_evidence_type": ["price_only", "valuation_blowoff", "positioning_overheat"], "four_c_protection_label": "hard_4c_late", "trigger_outcome_label": "4B_overlay_success_counterexample", "current_profile_verdict": "current_profile_false_positive", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window_after_2021_11_08_candidate", "same_entry_group_id": "R8L29_C26_FSN_20211110_CLOSE6630", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false}
{"row_type": "trigger", "trigger_id": "FSN_4B_THEME_BLOWOFF_20211230", "case_id": "R8L29_C26_FSN_20211110", "symbol": "214270", "company_name": "FSN", "round": "R8", "loop": "29", "large_sector_id": "L8_PLATFORM_CONTENT_SW_SECURITY", "canonical_archetype_id": "C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE", "fine_archetype_id": "ADTECH_NFT_METAVERSE_THEME_BLOWOFF_WITHOUT_CORE_AD_OP_LEVERAGE", "sector": "platform_content_sw_security", "primary_archetype": "platform_ad_revenue_operating_leverage", "loop_objective": "coverage_gap_fill; counterexample_mining; green_strictness_stress_test; 4B_non_price_requirement_stress_test; canonical_archetype_compression", "trigger_type": "Stage4B-overlay", "trigger_date": "2021-12-30", "evidence_available_at_that_date": "Local/full-window blowoff after rapid theme rerating; overlay-only row.", "evidence_source": "stock-web OHLC plus theme source map", "stage2_evidence_fields": [], "stage3_evidence_fields": [], "stage4b_evidence_fields": ["valuation_blowoff", "positioning_overheat", "price_only_local_peak"], "stage4c_evidence_fields": ["thesis_evidence_broken"], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/214/214270/2021.csv; atlas/ohlcv_tradable_by_symbol_year/214/214270/2022.csv", "profile_path": "atlas/symbol_profiles/214/214270.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "entry_date": "2021-12-30", "entry_price": 13800, "MFE_30D_pct": 2.9, "MFE_90D_pct": 2.9, "MFE_180D_pct": 2.9, "MFE_1Y_pct": null, "MFE_2Y_pct": null, "MAE_30D_pct": -46.09, "MAE_90D_pct": -50.07, "MAE_180D_pct": -71.01, "MAE_1Y_pct": null, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2022-01-03", "peak_price": 14200, "drawdown_after_peak_pct": -71.83, "green_lateness_ratio": 0.95, "four_b_local_peak_proximity": 0.95, "four_b_full_window_peak_proximity": 0.95, "four_b_timing_verdict": "good_full_window_4B_timing", "four_b_evidence_type": ["price_only", "valuation_blowoff", "positioning_overheat"], "four_c_protection_label": "hard_4c_late", "trigger_outcome_label": "4B_overlay_success", "current_profile_verdict": "current_profile_4B_too_late", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window_after_2021_11_08_candidate", "same_entry_group_id": "R8L29_C26_FSN_20211230_CLOSE13800", "dedupe_for_aggregate": false, "aggregate_group_role": "4B_overlay_only", "is_new_independent_case": false, "reuse_reason": "same case; 4B timing overlay only", "independent_evidence_weight": 0.0, "do_not_count_as_new_case": true}
```

### 25.4 score_simulation rows
```jsonl
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy_to_C26_shadow", "case_id": "R8L29_C26_NASMEDIA_20201106", "trigger_id": "NASMEDIA_STAGE2_AD_RECOVERY_20201106", "symbol": "089600", "large_sector_id": "L8_PLATFORM_CONTENT_SW_SECURITY", "canonical_archetype_id": "C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE", "raw_component_scores_before": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 15, "revision_score": 16, "relative_strength_score": 8, "customer_quality_score": 12, "policy_or_regulatory_score": 0, "valuation_repricing_score": 8, "execution_risk_score": -3, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_before": 74, "stage_label_before": "Stage2-Actionable", "raw_component_scores_after": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 17, "revision_score": 17, "relative_strength_score": 8, "customer_quality_score": 12, "policy_or_regulatory_score": 0, "valuation_repricing_score": 8, "execution_risk_score": -3, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_after": 78, "stage_label_after": "Stage3-Yellow", "changed_components": ["margin_bridge_score", "revision_score"], "component_delta_explanation": "C26 ad-spend recovery + fixed-cost margin bridge can promote Yellow earlier than generic Green confirmation.", "MFE_90D_pct": 42.76, "MAE_90D_pct": -5.04, "score_return_alignment_label": "aligned_positive", "current_profile_verdict": "current_profile_too_late"}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy_to_C26_shadow", "case_id": "R8L29_C26_INCROSS_20201106", "trigger_id": "INCROSS_STAGE2_TDEAL_ADTECH_20201106", "symbol": "216050", "large_sector_id": "L8_PLATFORM_CONTENT_SW_SECURITY", "canonical_archetype_id": "C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE", "raw_component_scores_before": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 14, "revision_score": 17, "relative_strength_score": 11, "customer_quality_score": 13, "policy_or_regulatory_score": 0, "valuation_repricing_score": 8, "execution_risk_score": -3, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_before": 77, "stage_label_before": "Stage2-Actionable", "raw_component_scores_after": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 16, "revision_score": 18, "relative_strength_score": 11, "customer_quality_score": 13, "policy_or_regulatory_score": 0, "valuation_repricing_score": 8, "execution_risk_score": -3, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_after": 81, "stage_label_after": "Stage3-Yellow", "changed_components": ["margin_bridge_score", "revision_score"], "component_delta_explanation": "T-Deal/ad-tech monetization route deserves earlier C26 Yellow, not immediate Green.", "MFE_90D_pct": 40.75, "MAE_90D_pct": -2.34, "score_return_alignment_label": "aligned_positive", "current_profile_verdict": "current_profile_too_late"}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy_to_C26_shadow", "case_id": "R8L29_C26_PLAYD_20200519", "trigger_id": "PLAYD_PRICE_ONLY_IPO_AD_THEME_20200519", "symbol": "237820", "large_sector_id": "L8_PLATFORM_CONTENT_SW_SECURITY", "canonical_archetype_id": "C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE", "raw_component_scores_before": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 0, "revision_score": 0, "relative_strength_score": 20, "customer_quality_score": 0, "policy_or_regulatory_score": 0, "valuation_repricing_score": 18, "execution_risk_score": -8, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_before": 70, "stage_label_before": "Stage2-Actionable false risk", "raw_component_scores_after": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 0, "revision_score": 0, "relative_strength_score": 8, "customer_quality_score": 0, "policy_or_regulatory_score": 0, "valuation_repricing_score": 4, "execution_risk_score": -16, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_after": 54, "stage_label_after": "Watch/Blocked", "changed_components": ["relative_strength_score", "valuation_repricing_score", "execution_risk_score"], "component_delta_explanation": "IPO/theme price action is cut because no revenue-quality or margin evidence existed at trigger date.", "MFE_90D_pct": 23.57, "MAE_90D_pct": -39.66, "score_return_alignment_label": "aligned_counterexample", "current_profile_verdict": "current_profile_correct"}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy_to_C26_shadow", "case_id": "R8L29_C26_FSN_20211110", "trigger_id": "FSN_STAGE2_THEME_SPIKE_20211110", "symbol": "214270", "large_sector_id": "L8_PLATFORM_CONTENT_SW_SECURITY", "canonical_archetype_id": "C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE", "raw_component_scores_before": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 0, "revision_score": 0, "relative_strength_score": 19, "customer_quality_score": 8, "policy_or_regulatory_score": 0, "valuation_repricing_score": 18, "execution_risk_score": -6, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_before": 76, "stage_label_before": "Stage2/Yellow false risk", "raw_component_scores_after": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 0, "revision_score": 0, "relative_strength_score": 8, "customer_quality_score": 2, "policy_or_regulatory_score": 0, "valuation_repricing_score": 4, "execution_risk_score": -18, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_after": 51, "stage_label_after": "4B-Watch/Blocked", "changed_components": ["relative_strength_score", "valuation_repricing_score", "customer_quality_score", "execution_risk_score"], "component_delta_explanation": "NFT/metaverse optionality is not C26 ad operating leverage; treat as 4B overlay after blowoff.", "MFE_90D_pct": 114.18, "MAE_90D_pct": -3.77, "score_return_alignment_label": "aligned_counterexample", "current_profile_verdict": "current_profile_false_positive"}
```

### 25.5 shadow_weight rows
```csv
row_type,axis,scope,large_sector_id,canonical_archetype_id,baseline_value,tested_value,delta,reason,backtest_effect,trigger_ids,calibration_usable_count,new_independent_case_count,counterexample_count,confidence,proposal_type,notes
shadow_weight,c26_ad_spend_recovery_operating_leverage_bonus,canonical_archetype_specific,L8_PLATFORM_CONTENT_SW_SECURITY,C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE,0,+1,+1,"Nasmedia and Incross had cleaner MFE/MAE when ad recovery plus margin bridge evidence existed before full Green confirmation","reduced missed/late structural count from 2 to 0","NASMEDIA_STAGE2_AD_RECOVERY_20201106|INCROSS_STAGE2_TDEAL_ADTECH_20201106",2,2,0,medium,canonical_shadow_only,"not production; post-calibrated residual"
shadow_weight,c26_ipo_or_theme_spike_green_cap,canonical_archetype_specific,L8_PLATFORM_CONTENT_SW_SECURITY,C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE,absent,active,guard,"PlayD and FSN show large local MFE but severe later drawdowns when no realized operating leverage existed","reduced false-positive Green risk","PLAYD_PRICE_ONLY_IPO_AD_THEME_20200519|FSN_STAGE2_THEME_SPIKE_20211110",2,2,2,medium,counterexample_guard,"not production; post-calibrated residual"
shadow_weight,c26_theme_optional_4b_guard,canonical_archetype_specific,L8_PLATFORM_CONTENT_SW_SECURITY,C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE,0,+1,+1,"ad-tech plus NFT/metaverse optionality should route to overlay risk unless core ad revenue/OP leverage closes","improved 4B timing on FSN",FSN_4B_THEME_BLOWOFF_20211230,1,1,1,low_to_medium,4B_overlay_guard,"overlay/risk calibration only"
```

### 25.6 residual_contribution row
```jsonl
{"row_type": "residual_contribution", "round": "R8", "loop": "29", "large_sector_id": "L8_PLATFORM_CONTENT_SW_SECURITY", "canonical_archetype_id": "C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE", "new_independent_case_count": 4, "reused_case_count": 0, "new_symbol_count": 4, "same_archetype_new_symbol_count": 4, "same_archetype_new_trigger_family_count": 4, "new_canonical_archetype_count": 0, "new_trigger_family_count": 4, "positive_case_count": 2, "counterexample_count": 2, "current_profile_error_count": 3, "tested_existing_calibrated_axes": ["stage2_actionable_evidence_bonus", "stage3_green_revision_min", "price_only_blowoff_blocks_positive_stage", "full_4b_requires_non_price_evidence", "hard_4c_thesis_break_routes_to_4c"], "residual_error_types_found": ["small_adtech_operating_leverage_missed_or_late", "ipo_theme_price_only_false_green", "adtech_nft_optional_theme_blowoff"], "diversity_score_summary": "high: 4 new C26 symbols, 4 trigger families, 2 positives, 2 counterexamples, no reused cases; same canonical but new symbol/failure coverage", "loop_contribution_label": "canonical_archetype_rule_candidate", "do_not_propose_new_weight_delta": false, "auto_selected_coverage_gap": "R8/C26 already had SOOP/NAVER/Kakao; this loop fills ad-network/ad-tech small-midcap positives and IPO/NFT theme counterexamples."}
```

### 25.7 narrative_only rows
```jsonl
{"row_type": "narrative_only", "case_id": "R8L29_C26_WIDEPLANET_202312_THEME_BLOCKED", "symbol": "321820", "large_sector_id": "L8_PLATFORM_CONTENT_SW_SECURITY", "canonical_archetype_id": "C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE", "reason": "corporate_action_candidate_date_2024_01_05_overlaps_forward_window_and_name/business-transition contamination; not used for weight calibration", "price_source": "Songdaiki/stock-web", "usage": "not_weight_calibration"}
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

next_round: R9 / C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE or R8 / C28 holdout expansion if software/security counterexample count remains low.

## 28. Source Notes

- Stock-web manifest validation used `atlas/manifest.json` with max_date `2026-02-20`, raw/unadjusted marcap basis, tradable row count 14,354,401, and calibration shard root `atlas/ohlcv_tradable_by_symbol_year`.
- Profile validation references: 089600 profile has no corporate action candidates and active-like data through 2026-02-20; 216050 profile has a 2022-07-11 candidate outside the selected 2020-11 180D window; 237820 profile has no corporate-action candidates; 214270 profile has a 2021-11-08 candidate, so the selected FSN entry is placed after that date and marked clean after candidate date.
- OHLC rows used: Nasmedia 2020-11-06 entry 30,750 and 2021-06-24 peak high 44,900; Incross 2020-11-06 entry 42,700 and 2021-03-29 peak high 63,500; PlayD 2020-05-19 entry 14,850 and 2020-05-20 peak high 18,350 with 2020-12/2021 drawdown; FSN 2021-11-10 entry 6,630, 2022-01-03 high 14,200, and later 2022 low near 4,000 inside 180D.
