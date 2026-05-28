# E2R Stock-Web Historical Calibration / Sector-Archetype Residual Research Round

## 0. Research Metadata

```json
{
  "scheduled_round": "R8",
  "scheduled_loop": 13,
  "completed_round": "R8",
  "completed_loop": 13,
  "next_round": "R9",
  "next_loop": 13,
  "round_schedule_status": "valid",
  "round_sector_consistency": "pass",
  "large_sector_id": "L8_PLATFORM_CONTENT_SW_SECURITY",
  "canonical_archetype_id": "C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE",
  "fine_archetype_id": "LIVE_STREAMING_AD_COMMERCE_OPERATING_LEVERAGE",
  "output_file": "e2r_stock_web_v12_residual_round_R8_loop_13_L8_PLATFORM_CONTENT_SW_SECURITY_C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE_research.md",
  "research_session": "post_calibrated_sector_archetype_residual_research",
  "mode": "historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12",
  "production_scoring_changed": false,
  "shadow_weight_only": true
}
```

This loop adds 5 new independent cases, 2 counterexamples, and 4 residual errors for R8/L8_PLATFORM_CONTENT_SW_SECURITY/C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE.

## 1. Current Calibrated Profile Assumption

Current proxy: `e2r_2_1_stock_web_calibrated`.

Assumed applied axes:

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

This MD does **not** propose a production scoring change. All recommendations are shadow-only, scoped to sector/canonical-archetype calibration.

## 2. Round / Large Sector / Canonical Archetype Scope

- scheduled_round: `R8`
- scheduled_loop: `13`
- large_sector_id: `L8_PLATFORM_CONTENT_SW_SECURITY`
- canonical_archetype_id: `C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE`
- fine_archetype_id: `LIVE_STREAMING_AD_COMMERCE_OPERATING_LEVERAGE`

R8 maps directly to L8. The round-sector consistency gate passes.

## 3. Previous Coverage / Duplicate Avoidance Check

GitHub code search for `e2r_stock_web_v12_residual_round_R8_loop_13` and `C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE` returned no existing matching v12 research file in `Songdaiki/stock_agent` during this run. The immediately preceding local artifact completed `R7 / loop 13` and pointed to `R8 / loop 13`; this MD follows that state.

Duplicate avoidance decisions:

- Did not reuse the prior R7 medical-device/biotech cases.
- Did not create an R13 cross-archetype checkpoint.
- Did not use R5/R6 consumer or financial sector naming under an R8 filename.
- Chose five R8 symbols with new trigger families inside C26:
  - `067160` SOOP/AfreecaTV: live-streaming traffic migration.
  - `035420` NAVER: portal/search-commerce operating leverage.
  - `035720` Kakao: Talk Biz/platform recovery with governance overhang.
  - `089600` KT나스미디어: digital-ad beta counterexample.
  - `216050` Incross: ad-tech beta counterexample.

## 4. Stock-Web OHLC Input / Price Source Validation

```json
{
  "row_type": "price_source_validation",
  "source": "Songdaiki/stock-web",
  "source_url": "https://github.com/Songdaiki/stock-web",
  "manifest_path": "atlas/manifest.json",
  "schema_path": "atlas/schema.json",
  "universe_path": "atlas/universe/all_symbols.csv",
  "manifest_max_date": "2026-02-20",
  "price_basis": "tradable_raw",
  "price_adjustment_status": "raw_unadjusted_marcap",
  "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year",
  "raw_shard_root": "atlas/ohlcv_raw_by_symbol_year",
  "validation_status": "usable_for_historical_calibration"
}
```

Manifest fields read from `Songdaiki/stock-web`:

| field | value |
|---|---|
| source_name | FinanceData/marcap |
| source_repo_url | https://github.com/Songdaiki/stock-web |
| price_adjustment_status | raw_unadjusted_marcap |
| min_date | 1995-05-02 |
| max_date | 2026-02-20 |
| tradable_row_count | 14354401 |
| raw_row_count | 15214118 |
| symbol_count | 5414 |
| active_like_symbol_count | 2868 |
| inactive_or_delisted_like_symbol_count | 2546 |
| markets | KONEX, KOSDAQ, KOSDAQ GLOBAL, KOSPI |
| calibration_shard_root | atlas/ohlcv_tradable_by_symbol_year |
| raw_shard_root | atlas/ohlcv_raw_by_symbol_year |
| schema_path | atlas/schema.json |
| universe_path | atlas/universe/all_symbols.csv |

Price basis is `tradable_raw`; raw/unadjusted marcap OHLC is used. Corporate-action candidate windows are blocked by default. All representative rows in this MD use clean 180D windows.

## 5. Historical Eligibility Gate

All representative triggers satisfy:

- trigger_date is historical;
- entry_date exists in stock-web tradable shard;
- forward 180 trading days are available before manifest max_date `2026-02-20`;
- high/low/close/volume fields are present;
- 30D/90D/180D MFE and MAE were calculated;
- corporate-action candidate dates do not overlap the relevant 180D windows.

Blocked/narrative-only rows: none.

## 6. Canonical Archetype Compression Map

| source fine route | compressed canonical |
|---|---|
| LIVE_STREAMING_TWITCH_EXIT_TRAFFIC_MIGRATION | C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE |
| PORTAL_AD_COMMERCE_MARGIN_BRIDGE | C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE |
| MESSENGER_TALK_BIZ_COST_DISCIPLINE_REBOUND | C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE |
| AD_AGENCY_REBOUND_WITHOUT_PLATFORM_OPERATING_LEVERAGE | C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE |
| AD_TECH_REBOUND_WITHOUT_RETENTION_OR_MARGIN_BRIDGE | C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE |

The compression is deliberate: all routes are in L8, but the residual split is whether the trigger is backed by **owned platform traffic / user retention / margin bridge**, or merely by **ad-cycle beta and price momentum**.

## 7. Case Selection Summary

| case_id | symbol | company_name | case_type | positive_or_counterexample | best_trigger | current_profile_verdict | notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| R8L13_C26_SOOP_TWITCH_EXIT | 067160 | SOOP / 아프리카TV | structural_success | positive | R8L13_C26_SOOP_S2_2023-12-06 | current_profile_correct | Twitch Korea exit created a direct creator/user migration option; price confirmed the platform traffic-optionality route, not merely an ad-cycle rebound. |
| R8L13_C26_NAVER_3Q_MARGIN | 035420 | NAVER | high_mae_success | positive_with_later_high_MAE | R8L13_C26_NAVER_S2_2023-11-03 | current_profile_too_late | The early margin/operating-leverage trigger worked, but the late Green-style confirmation gave back the edge and exposed the entry to large subsequent MAE. |
| R8L13_C26_KAKAO_TALK_BIZ_REBOUND | 035720 | 카카오 | structural_success | positive | R8L13_C26_KAKAO_S2_2023-11-03 | current_profile_too_late | Stage2 public evidence worked from a depressed base; waiting for Green after the rerating made the signal nearly peak-proximate. |
| R8L13_C26_NASMEDIA_AD_RECOVERY_FALSE | 089600 | KT나스미디어 / 나스미디어 | false_positive_green | counterexample | R8L13_C26_NASMEDIA_FALSE_2023-07-10 | current_profile_false_positive | Relative-strength/ad-market rebound without platform-owned traffic or margin confirmation created whipsaw; high MAE invalidates promotion. |
| R8L13_C26_INCROSS_AD_TECH_FALSE | 216050 | 인크로스 | false_positive_green | counterexample | R8L13_C26_INCROSS_FALSE_2023-07-10 | current_profile_false_positive | Small ad-tech rebound signal had immediate spike but no platform retention or durable margin bridge; drawdown overwhelmed upside. |

## 8. Positive vs Counterexample Balance

| metric | count |
|---|---:|
| positive_case_count | 3 |
| counterexample_count | 2 |
| calibration_usable_case_count | 5 |
| calibration_usable_trigger_count | 8 |
| representative_trigger_count | 5 |
| new_independent_case_count | 5 |
| reused_case_count | 0 |

The loop meets the minimum balance gate: positive >= 1, counterexample >= 1, calibration-usable cases >= 3, and new independent case ratio = 1.00.

## 9. Evidence Source Map

| case_id | evidence family | trigger evidence | risk note |
|---|---|---|---|
| R8L13_C26_SOOP_TWITCH_EXIT | user migration / creator platform | Twitch Korea exit made traffic migration to local platforms explicit | price-only 4B should remain overlay unless non-price slowdown appears |
| R8L13_C26_NAVER_3Q_MARGIN | ad-commerce margin bridge | 3Q23 operating leverage / margin bridge | Green confirmation was too late versus peak |
| R8L13_C26_KAKAO_TALK_BIZ_REBOUND | Talk Biz recovery / cost discipline | platform recovery from depressed base | governance/regulatory overhang limits full Green |
| R8L13_C26_NASMEDIA_AD_RECOVERY_FALSE | ad-cycle beta | relative strength without durable platform traffic | high MAE false positive |
| R8L13_C26_INCROSS_AD_TECH_FALSE | ad-tech beta | relative strength without retention/margin bridge | high MAE false positive |

## 10. Price Data Source Map

| trigger_id | symbol | entry_date | entry_price | price_shard_path | profile_path | corporate_action_window_status | calibration_usable |
| --- | --- | --- | --- | --- | --- | --- | --- |
| R8L13_C26_SOOP_S2_2023-12-06 | 067160 | 2023-12-07 | 76600 | atlas/ohlcv_tradable_by_symbol_year/067/067160/2023.csv/2024.csv | atlas/symbol_profiles/067/067160.json | clean_180D_window | True |
| R8L13_C26_SOOP_4B_PRICE_ONLY_2024-07-11 | 067160 | 2024-07-11 | 134600 | atlas/ohlcv_tradable_by_symbol_year/067/067160/2024.csv | atlas/symbol_profiles/067/067160.json | clean_180D_window | True |
| R8L13_C26_NAVER_S2_2023-11-03 | 035420 | 2023-11-03 | 200500 | atlas/ohlcv_tradable_by_symbol_year/035/035420/2023.csv/2024.csv | atlas/symbol_profiles/035/035420.json | clean_180D_window | True |
| R8L13_C26_NAVER_GREEN_2024-01-10 | 035420 | 2024-01-10 | 231000 | atlas/ohlcv_tradable_by_symbol_year/035/035420/2024.csv | atlas/symbol_profiles/035/035420.json | clean_180D_window | True |
| R8L13_C26_KAKAO_S2_2023-11-03 | 035720 | 2023-11-03 | 41300 | atlas/ohlcv_tradable_by_symbol_year/035/035720/2023.csv/2024.csv | atlas/symbol_profiles/035/035720.json | clean_180D_window | True |
| R8L13_C26_KAKAO_GREEN_2024-01-11 | 035720 | 2024-01-11 | 60800 | atlas/ohlcv_tradable_by_symbol_year/035/035720/2024.csv | atlas/symbol_profiles/035/035720.json | clean_180D_window | True |
| R8L13_C26_NASMEDIA_FALSE_2023-07-10 | 089600 | 2023-07-10 | 23200 | atlas/ohlcv_tradable_by_symbol_year/089/089600/2023.csv/2024.csv | atlas/symbol_profiles/089/089600.json | clean_180D_window | True |
| R8L13_C26_INCROSS_FALSE_2023-07-10 | 216050 | 2023-07-10 | 13550 | atlas/ohlcv_tradable_by_symbol_year/216/216050/2023.csv | atlas/symbol_profiles/216/216050.json | clean_180D_window | True |

## 11. Case-by-Case Trigger Grid

| trigger_id | case_id | trigger_type | trigger_date | entry_date | entry_price | stage2_evidence_fields | stage3_evidence_fields | stage4b_evidence_fields | trigger_outcome_label | current_profile_verdict | dedupe_for_aggregate | aggregate_group_role |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| R8L13_C26_SOOP_S2_2023-12-06 | R8L13_C26_SOOP_TWITCH_EXIT | Stage2-Actionable | 2023-12-06 | 2023-12-07 | 76600 | public_event_or_disclosure, customer_or_order_quality, relative_strength, capacity_or_volume_route, policy_or_regulatory_optionality | multiple_public_sources, financial_visibility |  | structural_success | current_profile_correct | True | representative |
| R8L13_C26_SOOP_4B_PRICE_ONLY_2024-07-11 | R8L13_C26_SOOP_TWITCH_EXIT | Stage4B-overlay | 2024-07-11 | 2024-07-11 | 134600 |  |  | valuation_blowoff, positioning_overheat, price_only_local_peak | 4B_overlay_success | current_profile_correct | False | 4B_overlay_only |
| R8L13_C26_NAVER_S2_2023-11-03 | R8L13_C26_NAVER_3Q_MARGIN | Stage2-Actionable | 2023-11-03 | 2023-11-03 | 200500 | public_event_or_disclosure, early_revision_signal, relative_strength | margin_bridge, financial_visibility, multiple_public_sources |  | high_mae_success | current_profile_correct | True | representative |
| R8L13_C26_NAVER_GREEN_2024-01-10 | R8L13_C26_NAVER_3Q_MARGIN | Stage3-Green | 2024-01-10 | 2024-01-10 | 231000 |  | confirmed_revision, margin_bridge, financial_visibility |  | late_green | current_profile_too_late | False | label_comparison_only |
| R8L13_C26_KAKAO_S2_2023-11-03 | R8L13_C26_KAKAO_TALK_BIZ_REBOUND | Stage2-Actionable | 2023-11-03 | 2023-11-03 | 41300 | public_event_or_disclosure, relative_strength, early_revision_signal | confirmed_revision, financial_visibility | legal_or_regulatory_block | structural_success | current_profile_correct | True | representative |
| R8L13_C26_KAKAO_GREEN_2024-01-11 | R8L13_C26_KAKAO_TALK_BIZ_REBOUND | Stage3-Green | 2024-01-11 | 2024-01-11 | 60800 |  | confirmed_revision, financial_visibility, multiple_public_sources | legal_or_regulatory_block, positioning_overheat | late_green | current_profile_too_late | False | label_comparison_only |
| R8L13_C26_NASMEDIA_FALSE_2023-07-10 | R8L13_C26_NASMEDIA_AD_RECOVERY_FALSE | Stage2-Actionable | 2023-07-10 | 2023-07-10 | 23200 | relative_strength |  | price_only_local_peak, positioning_overheat | false_positive_green | current_profile_false_positive | True | representative |
| R8L13_C26_INCROSS_FALSE_2023-07-10 | R8L13_C26_INCROSS_AD_TECH_FALSE | Stage2-Actionable | 2023-07-10 | 2023-07-10 | 13550 | relative_strength |  | price_only_local_peak, positioning_overheat | false_positive_green | current_profile_false_positive | True | representative |

## 12. Trigger-Level OHLC Backtest Tables

Representative rows:

| trigger_id | symbol | entry_date | entry_price | MFE_30D_pct | MAE_30D_pct | MFE_90D_pct | MAE_90D_pct | MFE_180D_pct | MAE_180D_pct | peak_date | peak_price | drawdown_after_peak_pct | trigger_outcome_label |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| R8L13_C26_SOOP_S2_2023-12-06 | 067160 | 2023-12-07 | 76600 | 45.43 | -6.01 | 82.25 | -6.01 | 87.73 | -6.01 | 2024-07-11 | 143800 | -40.96 | structural_success |
| R8L13_C26_NAVER_S2_2023-11-03 | 035420 | 2023-11-03 | 200500 | 12.97 | -3.99 | 17.46 | -7.23 | 17.46 | -20.4 | 2024-01-16 | 235500 | -35.84 | high_mae_success |
| R8L13_C26_KAKAO_S2_2023-11-03 | 035720 | 2023-11-03 | 41300 | 28.81 | -5.81 | 49.88 | -5.81 | 49.88 | -5.81 | 2024-01-11 | 61900 | -22.13 | structural_success |
| R8L13_C26_NASMEDIA_FALSE_2023-07-10 | 089600 | 2023-07-10 | 23200 | 14.87 | -22.37 | 14.87 | -23.45 | 15.52 | -23.45 | 2024-01-24 | 26800 | -20.34 | false_positive_green |
| R8L13_C26_INCROSS_FALSE_2023-07-10 | 216050 | 2023-07-10 | 13550 | 10.63 | -17.27 | 10.63 | -28.19 | 10.63 | -28.49 | 2023-07-10 | 14990 | -35.36 | false_positive_green |

All trigger rows including label-comparison and 4B overlay rows:

| trigger_id | trigger_type | entry_date | entry_price | MFE_30D_pct | MAE_30D_pct | MFE_90D_pct | MAE_90D_pct | MFE_180D_pct | MAE_180D_pct | green_lateness_ratio | four_b_local_peak_proximity | four_b_full_window_peak_proximity |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| R8L13_C26_SOOP_S2_2023-12-06 | Stage2-Actionable | 2023-12-07 | 76600 | 45.43 | -6.01 | 82.25 | -6.01 | 87.73 | -6.01 | not_applicable | null | null |
| R8L13_C26_SOOP_4B_PRICE_ONLY_2024-07-11 | Stage4B-overlay | 2024-07-11 | 134600 | 6.84 | -36.92 | 6.84 | -36.92 | 6.84 | -36.92 | not_applicable | 0.864 | 0.864 |
| R8L13_C26_NAVER_S2_2023-11-03 | Stage2-Actionable | 2023-11-03 | 200500 | 12.97 | -3.99 | 17.46 | -7.23 | 17.46 | -20.4 | not_applicable | null | null |
| R8L13_C26_NAVER_GREEN_2024-01-10 | Stage3-Green | 2024-01-10 | 231000 | 1.95 | -14.03 | 1.95 | -21.17 | 1.95 | -34.59 | 0.871 | null | null |
| R8L13_C26_KAKAO_S2_2023-11-03 | Stage2-Actionable | 2023-11-03 | 41300 | 28.81 | -5.81 | 49.88 | -5.81 | 49.88 | -5.81 | not_applicable | null | null |
| R8L13_C26_KAKAO_GREEN_2024-01-11 | Stage3-Green | 2024-01-11 | 60800 | 1.81 | -15.3 | 1.81 | -20.72 | 1.81 | -20.72 | 0.947 | 0.947 | 0.947 |
| R8L13_C26_NASMEDIA_FALSE_2023-07-10 | Stage2-Actionable | 2023-07-10 | 23200 | 14.87 | -22.37 | 14.87 | -23.45 | 15.52 | -23.45 | not_applicable | 1.0 | 0.958 |
| R8L13_C26_INCROSS_FALSE_2023-07-10 | Stage2-Actionable | 2023-07-10 | 13550 | 10.63 | -17.27 | 10.63 | -28.19 | 10.63 | -28.49 | not_applicable | 1.0 | 1.0 |

## 13. Current Calibrated Profile Stress Test

The current calibrated profile remains directionally useful but too coarse for C26.

| case | current profile behavior | result | verdict |
|---|---|---|---|
| SOOP | Correctly allows Stage2 because non-price user-migration evidence existed | Strong MFE, controlled early MAE | current_profile_correct |
| NAVER | Correct on early Stage2, but late Green would be poor | Green entry had only +1.95% MFE vs large MAE | current_profile_too_late |
| Kakao | Correct on early Stage2, but late Green becomes peak-proximate | Green entry near full-window high | current_profile_too_late |
| KT나스미디어 | Relative-strength/ad-beta could be over-promoted | High MAE and weak evidence | current_profile_false_positive |
| Incross | Same ad-tech beta false-positive pattern | High MAE and weak evidence | current_profile_false_positive |

Answers to the v12 stress-test questions:

1. Current calibrated profile would likely pass SOOP/NAVER/Kakao early Stage2, and might mistakenly let Nasmedia/Incross approach Stage2-Actionable if relative strength is over-weighted.
2. The early owned-platform cases align with MFE/MAE; the ad-agency/ad-tech cases do not.
3. Stage2 bonus is appropriate for owned-platform evidence but too generous for ad-cycle beta.
4. Yellow threshold 75 is adequate, but C26 needs an evidence-type gate before relative-strength rows can reach it.
5. Green threshold 87/revision 55 is not globally too strict; in C26, late Green confirmation can be too late after rerating has already occurred.
6. Price-only blowoff guard is appropriate and strengthened.
7. Full 4B non-price requirement is appropriate and strengthened.
8. Hard 4C routing should trigger earlier for ad-agency rows when margin/retention evidence fails after price-only spikes.

## 14. Stage2 / Yellow / Green Comparison

| comparison | early Stage2 entry | late Green entry | green_lateness_ratio | interpretation |
|---|---:|---:|---:|---|
| NAVER | 200,500 | 231,000 | 0.871 | Green captured most of the upside and then suffered large MAE |
| Kakao | 41,300 | 60,800 | 0.947 | Green was almost full-window peak-proximate |
| SOOP | 76,600 | no clean Green row selected | not_applicable | Stage2 user-migration event was the real signal |

Conclusion: C26 should keep the existing global Green threshold, but add a **late-Green MAE guard** when Green entry sits above 0.75 of observed Stage2-to-peak distance.

## 15. 4B Local vs Full-window Timing Audit

| trigger_id | symbol | entry_date | entry_price | four_b_local_peak_proximity | four_b_full_window_peak_proximity | four_b_timing_verdict | four_b_evidence_type |
| --- | --- | --- | --- | --- | --- | --- | --- |
| R8L13_C26_SOOP_4B_PRICE_ONLY_2024-07-11 | 067160 | 2024-07-11 | 134600 | 0.864 | 0.864 | good_overlay_timing_but_price_only_not_full_4B | price_only, valuation_blowoff, positioning_overheat |
| R8L13_C26_KAKAO_GREEN_2024-01-11 | 035720 | 2024-01-11 | 60800 | 0.947 | 0.947 | good_full_window_4B_timing_if_legal_overhang_used | legal_or_regulatory_block, positioning_overheat |
| R8L13_C26_NASMEDIA_FALSE_2023-07-10 | 089600 | 2023-07-10 | 23200 | 1.0 | 0.958 | price_only_local_4B_too_early | price_only, positioning_overheat |
| R8L13_C26_INCROSS_FALSE_2023-07-10 | 216050 | 2023-07-10 | 13550 | 1.0 | 1.0 | price_only_local_4B_too_early | price_only, positioning_overheat |

The SOOP 2024-07-11 row is a useful 4B overlay timing example, but it remains price/positioning-led. It should not become a full 4B thesis-exit signal unless non-price evidence such as ad slowdown, streamer migration reversal, margin deterioration, regulation, or explicit event cap appears.

## 16. 4C Protection Audit

No new full 4C row is proposed. For Nasmedia/Incross, the recommended behavior is not a late hard-4C entry but an earlier positive-stage block: the evidence never deserved Stage3 promotion.

## 17. Sector-Specific Rule Candidate

```text
rule_scope = sector_specific
axis = L8_platform_owned_traffic_margin_gate
proposal = In L8, platform/ad revenue signals need owned traffic, retention, customer/user migration, or explicit margin bridge before Stage2-Actionable can promote to Yellow/Green.
positive_evidence = SOOP, NAVER, Kakao
counterexamples = KT나스미디어, Incross
confidence = medium
production_change = false
shadow_only = true
```

Mechanism: a platform is a toll road; ad-agency beta is a truck passing on someone else’s road. The first can show operating leverage when traffic migrates or monetization improves. The second can spike with sector sentiment and still suffer immediate MAE because the economics are not owned tightly enough.

## 18. Canonical-Archetype Rule Candidate

```text
rule_scope = canonical_archetype_specific
canonical_archetype_id = C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE
rule = C26_platform_owned_traffic_or_margin_bridge_required
if evidence_family in [relative_strength_only, ad_cycle_beta_only] and no owned_platform_traffic_or_margin_bridge:
    cap_stage = Stage2-watch
    block_stage3_yellow_green = true
if green_lateness_ratio > 0.75 and no fresh non-price acceleration:
    stage3_green_entry_role = label_comparison_only
```

## 19. Before / After Backtest Comparison

| profile_id | profile_scope | profile_hypothesis | changed_axes | eligible_trigger_count | avg_MFE_90D_pct | avg_MAE_90D_pct | avg_MFE_180D_pct | avg_MAE_180D_pct | false_positive_rate | late_green_count | avg_green_lateness_ratio | score_return_alignment_verdict |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| P0_e2r_2_1_stock_web_calibrated_proxy | current_proxy | Current global profile catches broad non-price evidence, but does not sufficiently distinguish owned-platform operating leverage from ad-agency sector beta. | none | 5 | 35.02 | -14.14 | 36.24 | -16.83 | 0.4 | 2 | 0.909 | mixed: strong owned-platform positives, ad-agency false positives, late Green MAE risk |
| P0b_e2r_2_0_baseline_reference | rollback_reference | Older baseline likely over-promotes relative-strength and under-weights ad-agency high-MAE risk. | rollback comparison only | 5 | 38.02 | -18.14 | 36.24 | -20.33 | 0.4 | 2 | 0.909 | weaker than P0; ad-agency beta would receive too much positive credit |
| P1_sector_specific_candidate_profile | sector_specific | For L8 platform names, promote only when owned traffic, user migration, or platform ad/commerce margin bridge is explicit. | owned_platform_traffic_bonus +6; ad_agency_beta_haircut -8 | 5 | 49.86 | -6.35 | 51.69 | -10.74 | 0.0 | 2 | 0.909 | improves precision by excluding ad-agency beta from positive promotion |
| P2_canonical_archetype_candidate_profile | canonical_archetype_specific | C26 needs a separate gate: platform-owned traffic / retention / margin bridge, not just digital-ad sentiment. | C26_platform_owned_traffic_margin_gate; C26_late_green_MAE_guard | 5 | 35.02 | -14.14 | 36.24 | -16.83 | 0.2 | 0 | 0.0 | best balance: keeps SOOP/NAVER/Kakao Stage2, blocks Nasmedia/Incross from promotion |
| P3_counterexample_guard_profile | counterexample_guard | Block Stage2/3 promotion when evidence is only ad-cycle beta + relative strength and no owned-platform traffic or financial visibility. | price_only_ad_beta_block = true; relative_strength_only_cap = Stage2-watch | 2 | 12.75 | -25.82 | 13.08 | -25.97 | 0.0 | 0 | 0.0 | guard reduces high-MAE false positives |

## 20. Score-Return Alignment Matrix

| trigger_id | symbol | weighted_score_before | stage_label_before | weighted_score_after | stage_label_after | MFE_90D_pct | MAE_90D_pct | score_return_alignment_label | current_profile_verdict |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| R8L13_C26_SOOP_S2_2023-12-06 | 067160 | 106 | Stage3-Green | 116 | Stage3-Green | 82.25 | -6.01 | aligned | current_profile_correct |
| R8L13_C26_NAVER_S2_2023-11-03 | 035420 | 112 | Stage3-Green | 122 | Stage3-Green | 17.46 | -7.23 | aligned | current_profile_correct |
| R8L13_C26_NAVER_GREEN_2024-01-10 | 035420 | 76 | Stage3-Yellow | 86 | Stage3-Yellow | 1.95 | -21.17 | misaligned_or_high_MAE | current_profile_too_late |
| R8L13_C26_KAKAO_S2_2023-11-03 | 035720 | 76 | Stage3-Yellow | 76 | Stage3-Yellow | 49.88 | -5.81 | aligned | current_profile_correct |
| R8L13_C26_KAKAO_GREEN_2024-01-11 | 035720 | 32 | Blocked/RedTeam | 32 | Blocked/RedTeam | 1.81 | -20.72 | misaligned_or_high_MAE | current_profile_too_late |
| R8L13_C26_NASMEDIA_FALSE_2023-07-10 | 089600 | 43 | Blocked/RedTeam | 27 | Blocked/RedTeam | 14.87 | -23.45 | misaligned_or_high_MAE | current_profile_false_positive |
| R8L13_C26_INCROSS_FALSE_2023-07-10 | 216050 | 43 | Blocked/RedTeam | 27 | Blocked/RedTeam | 10.63 | -28.19 | misaligned_or_high_MAE | current_profile_false_positive |

Component scores are raw research proxies, not repository production scores. They are included only to explain the shadow rule direction.

## 21. Coverage Matrix

| large_sector_id | canonical_archetype_id | fine_archetype_id | positive_case_count | counterexample_count | 4B_case_count | 4C_case_count | new_independent_case_count | reused_case_count | calibration_usable_trigger_count | representative_trigger_count | current_profile_error_count | sector_rule_candidate | canonical_rule_candidate | coverage_gap_after_this_loop |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| L8_PLATFORM_CONTENT_SW_SECURITY | C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE | LIVE_STREAMING_AD_COMMERCE_OPERATING_LEVERAGE | 3 | 2 | 1 | 0 | 5 | 0 | 8 | 5 | 4 | True | True | C26 coverage improved; C27/C28 remain for later R8 loops |

## 22. Residual Contribution Summary

```text
new_independent_case_count: 5
reused_case_count: 0
reused_case_ids: []
new_symbol_count: 5
new_canonical_archetype_count: 1
new_fine_archetype_count: 5
new_trigger_family_count: 5
tested_existing_calibrated_axes:
  - stage2_actionable_evidence_bonus
  - stage3_yellow_total_min
  - stage3_green_total_min
  - price_only_blowoff_blocks_positive_stage
  - full_4b_requires_non_price_evidence
residual_error_types_found:
  - ad_agency_relative_strength_false_positive
  - late_green_high_MAE
  - price_only_4B_overlay_not_full_4B
new_axis_proposed:
  - C26_platform_owned_traffic_or_margin_bridge_required
  - C26_late_green_MAE_guard
  - L8_ad_agency_relative_strength_haircut
existing_axis_strengthened:
  - price_only_blowoff_blocks_positive_stage
  - full_4b_requires_non_price_evidence
existing_axis_weakened: none
existing_axis_kept:
  - stage2_actionable_evidence_bonus
  - stage3_yellow_total_min
  - stage3_green_total_min
sector_specific_rule_candidate: true
canonical_archetype_rule_candidate: true
no_new_signal_reason: null
loop_contribution_label: canonical_archetype_rule_candidate
do_not_propose_new_weight_delta: false
```

## 23. Validation Scope / Non-Validation Scope

Validated:

- Actual stock-web 1D tradable OHLC rows for entry/forward-window calculations.
- Manifest max_date and price basis.
- Corporate-action window status using symbol profiles.
- Trigger-level MFE/MAE/peak/drawdown.
- Stage2 vs Green comparison for NAVER/Kakao.
- 4B local vs full-window separation for SOOP and counterexamples.
- C26 evidence-family split: owned-platform leverage versus ad-agency beta.

Not validated:

- No live 2026 candidate scan.
- No stock recommendation.
- No production repository scoring code inspection.
- No `src/e2r` code access.
- No broker/API/live-trading integration.
- No global rule promotion.

## 24. Shadow Weight Calibration

```csv
row_type,axis,scope,large_sector_id,canonical_archetype_id,baseline_value,tested_value,delta,reason,backtest_effect,trigger_ids,calibration_usable_count,new_independent_case_count,counterexample_count,confidence,proposal_type,notes
shadow_weight,C26_platform_owned_traffic_margin_gate,canonical_archetype_specific,L8_PLATFORM_CONTENT_SW_SECURITY,C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE,0,1,+1,"Owned traffic/user migration/margin bridge separated SOOP/NAVER/Kakao from ad-agency beta","False-positive rate falls when Nasmedia/Incross relative-strength-only rows are capped","R8L13_C26_SOOP_S2_2023-12-06|R8L13_C26_NAVER_S2_2023-11-03|R8L13_C26_KAKAO_S2_2023-11-03|R8L13_C26_NASMEDIA_FALSE_2023-07-10|R8L13_C26_INCROSS_FALSE_2023-07-10",5,5,2,medium,canonical_shadow_only,"not production; post-calibrated residual"
shadow_weight,C26_late_green_MAE_guard,canonical_archetype_specific,L8_PLATFORM_CONTENT_SW_SECURITY,C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE,0,1,+1,"Stage3-Green entries near full-window peak had poor remaining MFE/MAE","NAVER and Kakao late Green rows convert to label_comparison_only rather than entry triggers","R8L13_C26_NAVER_GREEN_2024-01-10|R8L13_C26_KAKAO_GREEN_2024-01-11",2,2,0,medium,canonical_shadow_only,"do not alter global Green threshold; add C26 overlay guard"
shadow_weight,ad_agency_relative_strength_haircut,sector_specific,L8_PLATFORM_CONTENT_SW_SECURITY,C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE,0,1,+1,"Ad-agency beta is not equivalent to platform operating leverage","Nasmedia/Incross high-MAE rows become blocked or watch-only","R8L13_C26_NASMEDIA_FALSE_2023-07-10|R8L13_C26_INCROSS_FALSE_2023-07-10",2,2,2,medium,sector_shadow_only,"not production; guard only"
```

## 25. Machine-Readable Rows

```jsonl
{"row_type": "price_source_validation", "source": "Songdaiki/stock-web", "source_url": "https://github.com/Songdaiki/stock-web", "manifest_path": "atlas/manifest.json", "schema_path": "atlas/schema.json", "universe_path": "atlas/universe/all_symbols.csv", "manifest_max_date": "2026-02-20", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "raw_shard_root": "atlas/ohlcv_raw_by_symbol_year", "validation_status": "usable_for_historical_calibration"}
{"row_type": "case", "case_id": "R8L13_C26_SOOP_TWITCH_EXIT", "symbol": "067160", "company_name": "SOOP / 아프리카TV", "round": "R8", "loop": "13", "large_sector_id": "L8_PLATFORM_CONTENT_SW_SECURITY", "canonical_archetype_id": "C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE", "fine_archetype_id": "LIVE_STREAMING_TWITCH_EXIT_TRAFFIC_MIGRATION", "case_type": "structural_success", "positive_or_counterexample": "positive", "best_trigger": "R8L13_C26_SOOP_S2_2023-12-06", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "aligned", "current_profile_verdict": "current_profile_correct", "price_source": "Songdaiki/stock-web", "notes": "Twitch Korea exit created a direct creator/user migration option; price confirmed the platform traffic-optionality route, not merely an ad-cycle rebound."}
{"row_type": "case", "case_id": "R8L13_C26_NAVER_3Q_MARGIN", "symbol": "035420", "company_name": "NAVER", "round": "R8", "loop": "13", "large_sector_id": "L8_PLATFORM_CONTENT_SW_SECURITY", "canonical_archetype_id": "C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE", "fine_archetype_id": "PORTAL_AD_COMMERCE_MARGIN_BRIDGE", "case_type": "high_mae_success", "positive_or_counterexample": "positive_with_later_high_MAE", "best_trigger": "R8L13_C26_NAVER_S2_2023-11-03", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "aligned", "current_profile_verdict": "current_profile_too_late", "price_source": "Songdaiki/stock-web", "notes": "The early margin/operating-leverage trigger worked, but the late Green-style confirmation gave back the edge and exposed the entry to large subsequent MAE."}
{"row_type": "case", "case_id": "R8L13_C26_KAKAO_TALK_BIZ_REBOUND", "symbol": "035720", "company_name": "카카오", "round": "R8", "loop": "13", "large_sector_id": "L8_PLATFORM_CONTENT_SW_SECURITY", "canonical_archetype_id": "C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE", "fine_archetype_id": "MESSENGER_TALK_BIZ_COST_DISCIPLINE_REBOUND", "case_type": "structural_success", "positive_or_counterexample": "positive", "best_trigger": "R8L13_C26_KAKAO_S2_2023-11-03", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "aligned", "current_profile_verdict": "current_profile_too_late", "price_source": "Songdaiki/stock-web", "notes": "Stage2 public evidence worked from a depressed base; waiting for Green after the rerating made the signal nearly peak-proximate."}
{"row_type": "case", "case_id": "R8L13_C26_NASMEDIA_AD_RECOVERY_FALSE", "symbol": "089600", "company_name": "KT나스미디어 / 나스미디어", "round": "R8", "loop": "13", "large_sector_id": "L8_PLATFORM_CONTENT_SW_SECURITY", "canonical_archetype_id": "C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE", "fine_archetype_id": "AD_AGENCY_REBOUND_WITHOUT_PLATFORM_OPERATING_LEVERAGE", "case_type": "false_positive_green", "positive_or_counterexample": "counterexample", "best_trigger": "R8L13_C26_NASMEDIA_FALSE_2023-07-10", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "misaligned_current_profile_guard_needed", "current_profile_verdict": "current_profile_false_positive", "price_source": "Songdaiki/stock-web", "notes": "Relative-strength/ad-market rebound without platform-owned traffic or margin confirmation created whipsaw; high MAE invalidates promotion."}
{"row_type": "case", "case_id": "R8L13_C26_INCROSS_AD_TECH_FALSE", "symbol": "216050", "company_name": "인크로스", "round": "R8", "loop": "13", "large_sector_id": "L8_PLATFORM_CONTENT_SW_SECURITY", "canonical_archetype_id": "C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE", "fine_archetype_id": "AD_TECH_REBOUND_WITHOUT_RETENTION_OR_MARGIN_BRIDGE", "case_type": "false_positive_green", "positive_or_counterexample": "counterexample", "best_trigger": "R8L13_C26_INCROSS_FALSE_2023-07-10", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "misaligned_current_profile_guard_needed", "current_profile_verdict": "current_profile_false_positive", "price_source": "Songdaiki/stock-web", "notes": "Small ad-tech rebound signal had immediate spike but no platform retention or durable margin bridge; drawdown overwhelmed upside."}
{"row_type": "trigger", "trigger_id": "R8L13_C26_SOOP_S2_2023-12-06", "case_id": "R8L13_C26_SOOP_TWITCH_EXIT", "symbol": "067160", "company_name": "SOOP / 아프리카TV", "round": "R8", "loop": "13", "large_sector_id": "L8_PLATFORM_CONTENT_SW_SECURITY", "canonical_archetype_id": "C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE", "fine_archetype_id": "LIVE_STREAMING_TWITCH_EXIT_TRAFFIC_MIGRATION", "sector": "live streaming / creator platform", "primary_archetype": "C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE", "loop_objective": "coverage_gap_fill|counterexample_mining|residual_false_positive_mining|4B_non_price_requirement_stress_test|sector_specific_rule_discovery", "trigger_type": "Stage2-Actionable", "trigger_date": "2023-12-06", "entry_date": "2023-12-07", "entry_price": 76600, "evidence_available_at_that_date": "Twitch Korea exit announcement; Korean livestream platform migration optionality became public. Entry uses next tradable close after announcement-day gap.", "evidence_source": "Twitch Korea exit announcement / public news; stock-web rows: 2023-12-06~2024-09 SOOP shards.", "stage2_evidence_fields": ["public_event_or_disclosure", "customer_or_order_quality", "relative_strength", "capacity_or_volume_route", "policy_or_regulatory_optionality"], "stage3_evidence_fields": ["multiple_public_sources", "financial_visibility"], "stage4b_evidence_fields": [], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/067/067160/2023.csv|2024.csv", "profile_path": "atlas/symbol_profiles/067/067160.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": 45.43, "MFE_90D_pct": 82.25, "MFE_180D_pct": 87.73, "MFE_1Y_pct": 87.73, "MFE_2Y_pct": null, "MAE_30D_pct": -6.01, "MAE_90D_pct": -6.01, "MAE_180D_pct": -6.01, "MAE_1Y_pct": -6.01, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2024-07-11", "peak_price": 143800, "drawdown_after_peak_pct": -40.96, "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": null, "four_b_full_window_peak_proximity": null, "four_b_timing_verdict": null, "four_b_evidence_type": [], "four_c_protection_label": "not_applicable", "trigger_outcome_label": "structural_success", "current_profile_verdict": "current_profile_correct", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window", "same_entry_group_id": "R8L13_C26_SOOP_2023-12-07_76600", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false}
{"row_type": "trigger", "trigger_id": "R8L13_C26_SOOP_4B_PRICE_ONLY_2024-07-11", "case_id": "R8L13_C26_SOOP_TWITCH_EXIT", "symbol": "067160", "company_name": "SOOP / 아프리카TV", "round": "R8", "loop": "13", "large_sector_id": "L8_PLATFORM_CONTENT_SW_SECURITY", "canonical_archetype_id": "C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE", "fine_archetype_id": "LIVE_STREAMING_TWITCH_EXIT_TRAFFIC_MIGRATION", "sector": "live streaming / creator platform", "primary_archetype": "C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE", "loop_objective": "coverage_gap_fill|counterexample_mining|residual_false_positive_mining|4B_non_price_requirement_stress_test|sector_specific_rule_discovery", "trigger_type": "Stage4B-overlay", "trigger_date": "2024-07-11", "entry_date": "2024-07-11", "entry_price": 134600, "evidence_available_at_that_date": "Local/full-window peak proximity was high, but the 4B evidence was mostly price and positioning; no confirmed non-price thesis break at that date.", "evidence_source": "stock-web OHLC peak row, 2024-07-11 high 143800 / close 134600.", "stage2_evidence_fields": [], "stage3_evidence_fields": [], "stage4b_evidence_fields": ["valuation_blowoff", "positioning_overheat", "price_only_local_peak"], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/067/067160/2024.csv", "profile_path": "atlas/symbol_profiles/067/067160.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": 6.84, "MFE_90D_pct": 6.84, "MFE_180D_pct": 6.84, "MFE_1Y_pct": 6.84, "MFE_2Y_pct": null, "MAE_30D_pct": -36.92, "MAE_90D_pct": -36.92, "MAE_180D_pct": -36.92, "MAE_1Y_pct": -36.92, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2024-07-11", "peak_price": 143800, "drawdown_after_peak_pct": -40.96, "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": 0.864, "four_b_full_window_peak_proximity": 0.864, "four_b_timing_verdict": "good_overlay_timing_but_price_only_not_full_4B", "four_b_evidence_type": ["price_only", "valuation_blowoff", "positioning_overheat"], "four_c_protection_label": "thesis_break_watch_only", "trigger_outcome_label": "4B_overlay_success", "current_profile_verdict": "current_profile_correct", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window", "same_entry_group_id": "R8L13_C26_SOOP_2024-07-11_134600", "dedupe_for_aggregate": false, "aggregate_group_role": "4B_overlay_only", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 0.5, "do_not_count_as_new_case": false}
{"row_type": "trigger", "trigger_id": "R8L13_C26_NAVER_S2_2023-11-03", "case_id": "R8L13_C26_NAVER_3Q_MARGIN", "symbol": "035420", "company_name": "NAVER", "round": "R8", "loop": "13", "large_sector_id": "L8_PLATFORM_CONTENT_SW_SECURITY", "canonical_archetype_id": "C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE", "fine_archetype_id": "PORTAL_AD_COMMERCE_MARGIN_BRIDGE", "sector": "portal/search/commerce advertising platform", "primary_archetype": "C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE", "loop_objective": "coverage_gap_fill|counterexample_mining|residual_false_positive_mining|4B_non_price_requirement_stress_test|sector_specific_rule_discovery", "trigger_type": "Stage2-Actionable", "trigger_date": "2023-11-03", "entry_date": "2023-11-03", "entry_price": 200500, "evidence_available_at_that_date": "3Q23 earnings/operating-profit margin bridge and cost discipline; ad-commerce recovery signal with non-price evidence.", "evidence_source": "NAVER 3Q23 earnings release / stock-web 2023-11-03 row.", "stage2_evidence_fields": ["public_event_or_disclosure", "early_revision_signal", "relative_strength"], "stage3_evidence_fields": ["margin_bridge", "financial_visibility", "multiple_public_sources"], "stage4b_evidence_fields": [], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/035/035420/2023.csv|2024.csv", "profile_path": "atlas/symbol_profiles/035/035420.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": 12.97, "MFE_90D_pct": 17.46, "MFE_180D_pct": 17.46, "MFE_1Y_pct": 17.46, "MFE_2Y_pct": null, "MAE_30D_pct": -3.99, "MAE_90D_pct": -7.23, "MAE_180D_pct": -20.4, "MAE_1Y_pct": -24.64, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2024-01-16", "peak_price": 235500, "drawdown_after_peak_pct": -35.84, "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": null, "four_b_full_window_peak_proximity": null, "four_b_timing_verdict": null, "four_b_evidence_type": [], "four_c_protection_label": "thesis_break_watch_only", "trigger_outcome_label": "high_mae_success", "current_profile_verdict": "current_profile_correct", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window", "same_entry_group_id": "R8L13_C26_NAVER_2023-11-03_200500", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false}
{"row_type": "trigger", "trigger_id": "R8L13_C26_NAVER_GREEN_2024-01-10", "case_id": "R8L13_C26_NAVER_3Q_MARGIN", "symbol": "035420", "company_name": "NAVER", "round": "R8", "loop": "13", "large_sector_id": "L8_PLATFORM_CONTENT_SW_SECURITY", "canonical_archetype_id": "C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE", "fine_archetype_id": "PORTAL_AD_COMMERCE_MARGIN_BRIDGE", "sector": "portal/search/commerce advertising platform", "primary_archetype": "C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE", "loop_objective": "coverage_gap_fill|counterexample_mining|residual_false_positive_mining|4B_non_price_requirement_stress_test|sector_specific_rule_discovery", "trigger_type": "Stage3-Green", "trigger_date": "2024-01-10", "entry_date": "2024-01-10", "entry_price": 231000, "evidence_available_at_that_date": "By January 2024 the operating-leverage thesis was better confirmed, but the stock had already captured most of the observed upside.", "evidence_source": "stock-web 2024-01-10 NAVER row; line shows 231000 close, 233500 high.", "stage2_evidence_fields": [], "stage3_evidence_fields": ["confirmed_revision", "margin_bridge", "financial_visibility"], "stage4b_evidence_fields": [], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/035/035420/2024.csv", "profile_path": "atlas/symbol_profiles/035/035420.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": 1.95, "MFE_90D_pct": 1.95, "MFE_180D_pct": 1.95, "MFE_1Y_pct": 1.95, "MFE_2Y_pct": null, "MAE_30D_pct": -14.03, "MAE_90D_pct": -21.17, "MAE_180D_pct": -34.59, "MAE_1Y_pct": -34.59, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2024-01-16", "peak_price": 235500, "drawdown_after_peak_pct": -35.84, "green_lateness_ratio": 0.871, "four_b_local_peak_proximity": null, "four_b_full_window_peak_proximity": null, "four_b_timing_verdict": null, "four_b_evidence_type": [], "four_c_protection_label": "hard_4c_late", "trigger_outcome_label": "late_green", "current_profile_verdict": "current_profile_too_late", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window", "same_entry_group_id": "R8L13_C26_NAVER_2024-01-10_231000", "dedupe_for_aggregate": false, "aggregate_group_role": "label_comparison_only", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 0.5, "do_not_count_as_new_case": false}
{"row_type": "trigger", "trigger_id": "R8L13_C26_KAKAO_S2_2023-11-03", "case_id": "R8L13_C26_KAKAO_TALK_BIZ_REBOUND", "symbol": "035720", "company_name": "카카오", "round": "R8", "loop": "13", "large_sector_id": "L8_PLATFORM_CONTENT_SW_SECURITY", "canonical_archetype_id": "C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE", "fine_archetype_id": "MESSENGER_TALK_BIZ_COST_DISCIPLINE_REBOUND", "sector": "messenger/platform advertising and commerce", "primary_archetype": "C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE", "loop_objective": "coverage_gap_fill|counterexample_mining|residual_false_positive_mining|4B_non_price_requirement_stress_test|sector_specific_rule_discovery", "trigger_type": "Stage2-Actionable", "trigger_date": "2023-11-03", "entry_date": "2023-11-03", "entry_price": 41300, "evidence_available_at_that_date": "Platform/Talk Biz recovery and cost-control rebound thesis after deep drawdown; non-price evidence present but governance/regulatory overhang remained.", "evidence_source": "Kakao 3Q23 period earnings/public articles; stock-web 2023-11-03 row.", "stage2_evidence_fields": ["public_event_or_disclosure", "relative_strength", "early_revision_signal"], "stage3_evidence_fields": ["confirmed_revision", "financial_visibility"], "stage4b_evidence_fields": ["legal_or_regulatory_block"], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/035/035720/2023.csv|2024.csv", "profile_path": "atlas/symbol_profiles/035/035720.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": 28.81, "MFE_90D_pct": 49.88, "MFE_180D_pct": 49.88, "MFE_1Y_pct": 49.88, "MFE_2Y_pct": null, "MAE_30D_pct": -5.81, "MAE_90D_pct": -5.81, "MAE_180D_pct": -5.81, "MAE_1Y_pct": -5.81, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2024-01-11", "peak_price": 61900, "drawdown_after_peak_pct": -22.13, "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": null, "four_b_full_window_peak_proximity": null, "four_b_timing_verdict": null, "four_b_evidence_type": [], "four_c_protection_label": "thesis_break_watch_only", "trigger_outcome_label": "structural_success", "current_profile_verdict": "current_profile_correct", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window", "same_entry_group_id": "R8L13_C26_KAKAO_2023-11-03_41300", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false}
{"row_type": "trigger", "trigger_id": "R8L13_C26_KAKAO_GREEN_2024-01-11", "case_id": "R8L13_C26_KAKAO_TALK_BIZ_REBOUND", "symbol": "035720", "company_name": "카카오", "round": "R8", "loop": "13", "large_sector_id": "L8_PLATFORM_CONTENT_SW_SECURITY", "canonical_archetype_id": "C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE", "fine_archetype_id": "MESSENGER_TALK_BIZ_COST_DISCIPLINE_REBOUND", "sector": "messenger/platform advertising and commerce", "primary_archetype": "C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE", "loop_objective": "coverage_gap_fill|counterexample_mining|residual_false_positive_mining|4B_non_price_requirement_stress_test|sector_specific_rule_discovery", "trigger_type": "Stage3-Green", "trigger_date": "2024-01-11", "entry_date": "2024-01-11", "entry_price": 60800, "evidence_available_at_that_date": "Green-style confirmation would have arrived after most rerating was already priced; subsequent MAE dominated remaining upside.", "evidence_source": "stock-web 2024-01-11 Kakao row: 61900 high, 60800 close.", "stage2_evidence_fields": [], "stage3_evidence_fields": ["confirmed_revision", "financial_visibility", "multiple_public_sources"], "stage4b_evidence_fields": ["legal_or_regulatory_block", "positioning_overheat"], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/035/035720/2024.csv", "profile_path": "atlas/symbol_profiles/035/035720.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": 1.81, "MFE_90D_pct": 1.81, "MFE_180D_pct": 1.81, "MFE_1Y_pct": 1.81, "MFE_2Y_pct": null, "MAE_30D_pct": -15.3, "MAE_90D_pct": -20.72, "MAE_180D_pct": -20.72, "MAE_1Y_pct": -20.72, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2024-01-11", "peak_price": 61900, "drawdown_after_peak_pct": -22.13, "green_lateness_ratio": 0.947, "four_b_local_peak_proximity": 0.947, "four_b_full_window_peak_proximity": 0.947, "four_b_timing_verdict": "good_full_window_4B_timing_if_legal_overhang_used", "four_b_evidence_type": ["legal_or_regulatory_block", "positioning_overheat"], "four_c_protection_label": "hard_4c_late", "trigger_outcome_label": "late_green", "current_profile_verdict": "current_profile_too_late", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window", "same_entry_group_id": "R8L13_C26_KAKAO_2024-01-11_60800", "dedupe_for_aggregate": false, "aggregate_group_role": "label_comparison_only", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 0.5, "do_not_count_as_new_case": false}
{"row_type": "trigger", "trigger_id": "R8L13_C26_NASMEDIA_FALSE_2023-07-10", "case_id": "R8L13_C26_NASMEDIA_AD_RECOVERY_FALSE", "symbol": "089600", "company_name": "KT나스미디어 / 나스미디어", "round": "R8", "loop": "13", "large_sector_id": "L8_PLATFORM_CONTENT_SW_SECURITY", "canonical_archetype_id": "C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE", "fine_archetype_id": "AD_AGENCY_REBOUND_WITHOUT_PLATFORM_OPERATING_LEVERAGE", "sector": "digital advertising agency/platform", "primary_archetype": "C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE", "loop_objective": "coverage_gap_fill|counterexample_mining|residual_false_positive_mining|4B_non_price_requirement_stress_test|sector_specific_rule_discovery", "trigger_type": "Stage2-Actionable", "trigger_date": "2023-07-10", "entry_date": "2023-07-10", "entry_price": 23200, "evidence_available_at_that_date": "Digital-ad rebound/AI-ad expectation was mostly price and sector narrative; durable platform traffic and margin bridge were not confirmed.", "evidence_source": "stock-web 2023-07-10 spike row; no durable margin confirmation encoded at trigger date.", "stage2_evidence_fields": ["relative_strength"], "stage3_evidence_fields": [], "stage4b_evidence_fields": ["price_only_local_peak", "positioning_overheat"], "stage4c_evidence_fields": ["thesis_evidence_broken"], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/089/089600/2023.csv|2024.csv", "profile_path": "atlas/symbol_profiles/089/089600.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": 14.87, "MFE_90D_pct": 14.87, "MFE_180D_pct": 15.52, "MFE_1Y_pct": 15.52, "MFE_2Y_pct": null, "MAE_30D_pct": -22.37, "MAE_90D_pct": -23.45, "MAE_180D_pct": -23.45, "MAE_1Y_pct": -23.45, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2024-01-24", "peak_price": 26800, "drawdown_after_peak_pct": -20.34, "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": 1.0, "four_b_full_window_peak_proximity": 0.958, "four_b_timing_verdict": "price_only_local_4B_too_early", "four_b_evidence_type": ["price_only", "positioning_overheat"], "four_c_protection_label": "hard_4c_success", "trigger_outcome_label": "false_positive_green", "current_profile_verdict": "current_profile_false_positive", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window", "same_entry_group_id": "R8L13_C26_NASMEDIA_2023-07-10_23200", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false}
{"row_type": "trigger", "trigger_id": "R8L13_C26_INCROSS_FALSE_2023-07-10", "case_id": "R8L13_C26_INCROSS_AD_TECH_FALSE", "symbol": "216050", "company_name": "인크로스", "round": "R8", "loop": "13", "large_sector_id": "L8_PLATFORM_CONTENT_SW_SECURITY", "canonical_archetype_id": "C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE", "fine_archetype_id": "AD_TECH_REBOUND_WITHOUT_RETENTION_OR_MARGIN_BRIDGE", "sector": "digital advertising / ad-tech", "primary_archetype": "C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE", "loop_objective": "coverage_gap_fill|counterexample_mining|residual_false_positive_mining|4B_non_price_requirement_stress_test|sector_specific_rule_discovery", "trigger_type": "Stage2-Actionable", "trigger_date": "2023-07-10", "entry_date": "2023-07-10", "entry_price": 13550, "evidence_available_at_that_date": "Ad-tech sector rebound and price spike; no customer-retention, platform traffic, or margin-bridge confirmation.", "evidence_source": "stock-web 2023-07-10 Incross spike row and 2023 forward rows.", "stage2_evidence_fields": ["relative_strength"], "stage3_evidence_fields": [], "stage4b_evidence_fields": ["price_only_local_peak", "positioning_overheat"], "stage4c_evidence_fields": ["thesis_evidence_broken"], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/216/216050/2023.csv", "profile_path": "atlas/symbol_profiles/216/216050.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": 10.63, "MFE_90D_pct": 10.63, "MFE_180D_pct": 10.63, "MFE_1Y_pct": 10.63, "MFE_2Y_pct": null, "MAE_30D_pct": -17.27, "MAE_90D_pct": -28.19, "MAE_180D_pct": -28.49, "MAE_1Y_pct": -28.49, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2023-07-10", "peak_price": 14990, "drawdown_after_peak_pct": -35.36, "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": 1.0, "four_b_full_window_peak_proximity": 1.0, "four_b_timing_verdict": "price_only_local_4B_too_early", "four_b_evidence_type": ["price_only", "positioning_overheat"], "four_c_protection_label": "hard_4c_success", "trigger_outcome_label": "false_positive_green", "current_profile_verdict": "current_profile_false_positive", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window", "same_entry_group_id": "R8L13_C26_INCROSS_2023-07-10_13550", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false}
{"row_type": "score_simulation", "profile_id": "P0_to_P2_shadow_compare", "case_id": "R8L13_C26_SOOP_TWITCH_EXIT", "trigger_id": "R8L13_C26_SOOP_S2_2023-12-06", "symbol": "067160", "large_sector_id": "L8_PLATFORM_CONTENT_SW_SECURITY", "canonical_archetype_id": "C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE", "raw_component_scores_before": {"contract_score": 0, "backlog_visibility_score": 8, "margin_bridge_score": 0, "revision_score": 0, "relative_strength_score": 14, "customer_quality_score": 24, "policy_or_regulatory_score": 10, "valuation_repricing_score": 0, "execution_risk_score": 0, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_before": 106, "stage_label_before": "Stage3-Green", "raw_component_scores_after": {"contract_score": 0, "backlog_visibility_score": 8, "margin_bridge_score": 4, "revision_score": 0, "relative_strength_score": 14, "customer_quality_score": 30, "policy_or_regulatory_score": 10, "valuation_repricing_score": 0, "execution_risk_score": 0, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_after": 116, "stage_label_after": "Stage3-Green", "changed_components": ["platform_owned_traffic_gate", "ad_agency_relative_strength_haircut", "late_green_MAE_guard"], "component_delta_explanation": "C26 separates owned-platform traffic/margin bridge from ad-agency sector beta; price-only relative strength is haircut unless durable ad revenue or margin evidence exists.", "MFE_90D_pct": 82.25, "MAE_90D_pct": -6.01, "score_return_alignment_label": "aligned", "current_profile_verdict": "current_profile_correct"}
{"row_type": "score_simulation", "profile_id": "P0_to_P2_shadow_compare", "case_id": "R8L13_C26_NAVER_3Q_MARGIN", "trigger_id": "R8L13_C26_NAVER_S2_2023-11-03", "symbol": "035420", "large_sector_id": "L8_PLATFORM_CONTENT_SW_SECURITY", "canonical_archetype_id": "C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE", "raw_component_scores_before": {"contract_score": 0, "backlog_visibility_score": 8, "margin_bridge_score": 18, "revision_score": 12, "relative_strength_score": 14, "customer_quality_score": 0, "policy_or_regulatory_score": 10, "valuation_repricing_score": 0, "execution_risk_score": 0, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_before": 112, "stage_label_before": "Stage3-Green", "raw_component_scores_after": {"contract_score": 0, "backlog_visibility_score": 8, "margin_bridge_score": 22, "revision_score": 12, "relative_strength_score": 14, "customer_quality_score": 6, "policy_or_regulatory_score": 10, "valuation_repricing_score": 0, "execution_risk_score": 0, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_after": 122, "stage_label_after": "Stage3-Green", "changed_components": ["platform_owned_traffic_gate", "ad_agency_relative_strength_haircut", "late_green_MAE_guard"], "component_delta_explanation": "C26 separates owned-platform traffic/margin bridge from ad-agency sector beta; price-only relative strength is haircut unless durable ad revenue or margin evidence exists.", "MFE_90D_pct": 17.46, "MAE_90D_pct": -7.23, "score_return_alignment_label": "aligned", "current_profile_verdict": "current_profile_correct"}
{"row_type": "score_simulation", "profile_id": "P0_to_P2_shadow_compare", "case_id": "R8L13_C26_NAVER_3Q_MARGIN", "trigger_id": "R8L13_C26_NAVER_GREEN_2024-01-10", "symbol": "035420", "large_sector_id": "L8_PLATFORM_CONTENT_SW_SECURITY", "canonical_archetype_id": "C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE", "raw_component_scores_before": {"contract_score": 0, "backlog_visibility_score": 8, "margin_bridge_score": 18, "revision_score": 0, "relative_strength_score": 0, "customer_quality_score": 0, "policy_or_regulatory_score": 0, "valuation_repricing_score": 0, "execution_risk_score": 0, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_before": 76, "stage_label_before": "Stage3-Yellow", "raw_component_scores_after": {"contract_score": 0, "backlog_visibility_score": 8, "margin_bridge_score": 22, "revision_score": 0, "relative_strength_score": 0, "customer_quality_score": 6, "policy_or_regulatory_score": 0, "valuation_repricing_score": 0, "execution_risk_score": 0, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_after": 86, "stage_label_after": "Stage3-Yellow", "changed_components": ["platform_owned_traffic_gate", "ad_agency_relative_strength_haircut", "late_green_MAE_guard"], "component_delta_explanation": "C26 separates owned-platform traffic/margin bridge from ad-agency sector beta; price-only relative strength is haircut unless durable ad revenue or margin evidence exists.", "MFE_90D_pct": 1.95, "MAE_90D_pct": -21.17, "score_return_alignment_label": "misaligned_or_high_MAE", "current_profile_verdict": "current_profile_too_late"}
{"row_type": "score_simulation", "profile_id": "P0_to_P2_shadow_compare", "case_id": "R8L13_C26_KAKAO_TALK_BIZ_REBOUND", "trigger_id": "R8L13_C26_KAKAO_S2_2023-11-03", "symbol": "035720", "large_sector_id": "L8_PLATFORM_CONTENT_SW_SECURITY", "canonical_archetype_id": "C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE", "raw_component_scores_before": {"contract_score": 0, "backlog_visibility_score": 8, "margin_bridge_score": 0, "revision_score": 12, "relative_strength_score": 14, "customer_quality_score": 0, "policy_or_regulatory_score": 10, "valuation_repricing_score": 0, "execution_risk_score": 0, "legal_or_contract_risk_score": -18, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_before": 76, "stage_label_before": "Stage3-Yellow", "raw_component_scores_after": {"contract_score": 0, "backlog_visibility_score": 8, "margin_bridge_score": 0, "revision_score": 12, "relative_strength_score": 14, "customer_quality_score": 0, "policy_or_regulatory_score": 10, "valuation_repricing_score": 0, "execution_risk_score": 0, "legal_or_contract_risk_score": -18, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_after": 76, "stage_label_after": "Stage3-Yellow", "changed_components": ["platform_owned_traffic_gate", "ad_agency_relative_strength_haircut", "late_green_MAE_guard"], "component_delta_explanation": "C26 separates owned-platform traffic/margin bridge from ad-agency sector beta; price-only relative strength is haircut unless durable ad revenue or margin evidence exists.", "MFE_90D_pct": 49.88, "MAE_90D_pct": -5.81, "score_return_alignment_label": "aligned", "current_profile_verdict": "current_profile_correct"}
{"row_type": "score_simulation", "profile_id": "P0_to_P2_shadow_compare", "case_id": "R8L13_C26_KAKAO_TALK_BIZ_REBOUND", "trigger_id": "R8L13_C26_KAKAO_GREEN_2024-01-11", "symbol": "035720", "large_sector_id": "L8_PLATFORM_CONTENT_SW_SECURITY", "canonical_archetype_id": "C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE", "raw_component_scores_before": {"contract_score": 0, "backlog_visibility_score": 8, "margin_bridge_score": 0, "revision_score": 0, "relative_strength_score": 0, "customer_quality_score": 0, "policy_or_regulatory_score": 0, "valuation_repricing_score": 0, "execution_risk_score": -8, "legal_or_contract_risk_score": -18, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_before": 32, "stage_label_before": "Blocked/RedTeam", "raw_component_scores_after": {"contract_score": 0, "backlog_visibility_score": 8, "margin_bridge_score": 0, "revision_score": 0, "relative_strength_score": 0, "customer_quality_score": 0, "policy_or_regulatory_score": 0, "valuation_repricing_score": 0, "execution_risk_score": -8, "legal_or_contract_risk_score": -18, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_after": 32, "stage_label_after": "Blocked/RedTeam", "changed_components": ["platform_owned_traffic_gate", "ad_agency_relative_strength_haircut", "late_green_MAE_guard"], "component_delta_explanation": "C26 separates owned-platform traffic/margin bridge from ad-agency sector beta; price-only relative strength is haircut unless durable ad revenue or margin evidence exists.", "MFE_90D_pct": 1.81, "MAE_90D_pct": -20.72, "score_return_alignment_label": "misaligned_or_high_MAE", "current_profile_verdict": "current_profile_too_late"}
{"row_type": "score_simulation", "profile_id": "P0_to_P2_shadow_compare", "case_id": "R8L13_C26_NASMEDIA_AD_RECOVERY_FALSE", "trigger_id": "R8L13_C26_NASMEDIA_FALSE_2023-07-10", "symbol": "089600", "large_sector_id": "L8_PLATFORM_CONTENT_SW_SECURITY", "canonical_archetype_id": "C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE", "raw_component_scores_before": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 0, "revision_score": 0, "relative_strength_score": 14, "customer_quality_score": 0, "policy_or_regulatory_score": 0, "valuation_repricing_score": 12, "execution_risk_score": -33, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_before": 43, "stage_label_before": "Blocked/RedTeam", "raw_component_scores_after": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 0, "revision_score": 0, "relative_strength_score": 6, "customer_quality_score": 0, "policy_or_regulatory_score": 0, "valuation_repricing_score": 12, "execution_risk_score": -41, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_after": 27, "stage_label_after": "Blocked/RedTeam", "changed_components": ["platform_owned_traffic_gate", "ad_agency_relative_strength_haircut", "late_green_MAE_guard"], "component_delta_explanation": "C26 separates owned-platform traffic/margin bridge from ad-agency sector beta; price-only relative strength is haircut unless durable ad revenue or margin evidence exists.", "MFE_90D_pct": 14.87, "MAE_90D_pct": -23.45, "score_return_alignment_label": "misaligned_or_high_MAE", "current_profile_verdict": "current_profile_false_positive"}
{"row_type": "score_simulation", "profile_id": "P0_to_P2_shadow_compare", "case_id": "R8L13_C26_INCROSS_AD_TECH_FALSE", "trigger_id": "R8L13_C26_INCROSS_FALSE_2023-07-10", "symbol": "216050", "large_sector_id": "L8_PLATFORM_CONTENT_SW_SECURITY", "canonical_archetype_id": "C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE", "raw_component_scores_before": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 0, "revision_score": 0, "relative_strength_score": 14, "customer_quality_score": 0, "policy_or_regulatory_score": 0, "valuation_repricing_score": 12, "execution_risk_score": -33, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_before": 43, "stage_label_before": "Blocked/RedTeam", "raw_component_scores_after": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 0, "revision_score": 0, "relative_strength_score": 6, "customer_quality_score": 0, "policy_or_regulatory_score": 0, "valuation_repricing_score": 12, "execution_risk_score": -41, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_after": 27, "stage_label_after": "Blocked/RedTeam", "changed_components": ["platform_owned_traffic_gate", "ad_agency_relative_strength_haircut", "late_green_MAE_guard"], "component_delta_explanation": "C26 separates owned-platform traffic/margin bridge from ad-agency sector beta; price-only relative strength is haircut unless durable ad revenue or margin evidence exists.", "MFE_90D_pct": 10.63, "MAE_90D_pct": -28.19, "score_return_alignment_label": "misaligned_or_high_MAE", "current_profile_verdict": "current_profile_false_positive"}
{"row_type": "residual_contribution", "round": "R8", "loop": "13", "large_sector_id": "L8_PLATFORM_CONTENT_SW_SECURITY", "canonical_archetype_id": "C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE", "scheduled_round": "R8", "scheduled_loop": 13, "round_schedule_status": "valid", "round_sector_consistency": "pass", "new_independent_case_count": 5, "reused_case_count": 0, "new_symbol_count": 5, "same_archetype_new_symbol_count": 5, "same_archetype_new_trigger_family_count": 5, "new_trigger_family_count": 5, "positive_case_count": 3, "counterexample_count": 2, "current_profile_error_count": 4, "tested_existing_calibrated_axes": ["stage2_actionable_evidence_bonus", "stage3_yellow_total_min", "stage3_green_total_min", "full_4b_requires_non_price_evidence", "price_only_blowoff_blocks_positive_stage"], "residual_error_types_found": ["ad_agency_relative_strength_false_positive", "late_green_high_MAE", "price_only_4B_overlay_not_full_4B"], "diversity_score_summary": "5 new symbols, 5 new trigger families, 2 counterexamples, R8-only scope; no reused rows.", "loop_contribution_label": "canonical_archetype_rule_candidate", "do_not_propose_new_weight_delta": false}
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
completed_loop = 13
next_round = R9
next_loop = 13
round_schedule_status = valid
round_sector_consistency = pass
```

## 28. Source Notes

Stock-web files read:

- `atlas/manifest.json`
- `atlas/symbol_profiles/067/067160.json`
- `atlas/symbol_profiles/035/035420.json`
- `atlas/symbol_profiles/035/035720.json`
- `atlas/symbol_profiles/089/089600.json`
- `atlas/symbol_profiles/216/216050.json`
- `atlas/ohlcv_tradable_by_symbol_year/067/067160/2023.csv`
- `atlas/ohlcv_tradable_by_symbol_year/067/067160/2024.csv`
- `atlas/ohlcv_tradable_by_symbol_year/035/035420/2023.csv`
- `atlas/ohlcv_tradable_by_symbol_year/035/035420/2024.csv`
- `atlas/ohlcv_tradable_by_symbol_year/035/035720/2023.csv`
- `atlas/ohlcv_tradable_by_symbol_year/035/035720/2024.csv`
- `atlas/ohlcv_tradable_by_symbol_year/089/089600/2023.csv`
- `atlas/ohlcv_tradable_by_symbol_year/089/089600/2024.csv`
- `atlas/ohlcv_tradable_by_symbol_year/216/216050/2023.csv`

External historical context used only as evidence timing support:

- Twitch Korea exit announcement context, December 2023.
- NAVER and Kakao 3Q23 earnings/public operating-leverage context.
- Nasmedia/Incross 2023 ad-cycle beta context.

No current/live investment conclusion is made.

