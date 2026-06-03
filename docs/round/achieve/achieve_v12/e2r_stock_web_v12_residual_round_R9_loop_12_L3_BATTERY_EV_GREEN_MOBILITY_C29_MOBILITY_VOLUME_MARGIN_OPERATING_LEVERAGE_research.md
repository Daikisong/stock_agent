# E2R Stock-Web Historical Calibration / Sector-Archetype Residual Research Round

## 0. Research Metadata

| field | value |
|---|---|
| mode | historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12 |
| research_session | post_calibrated_sector_archetype_residual_research |
| round | R9 |
| loop | 12 |
| large_sector_id | L3_BATTERY_EV_GREEN_MOBILITY |
| canonical_archetype_id | C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE |
| fine_archetype_id | CONTAINER_FREIGHT_RATE_OPERATING_LEVERAGE; AUTO_LOGISTICS_CKD_PCC_VOLUME_MARGIN; LCC_REOPENING_VOLUME_WITH_FUEL_FX_COST_GAP |
| output_file | e2r_stock_web_v12_residual_round_R9_loop_12_L3_BATTERY_EV_GREEN_MOBILITY_C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE_research.md |
| production_scoring_changed | false |
| shadow_weight_only | true |
| live_candidate_mode | false |
| current_stock_discovery_allowed | false |
| stock_agent_code_access_allowed | false |
| stock_web_price_atlas_access_required | true |

This document is historical calibration research only. It is not a recommendation, a live watchlist, a trading signal, or a production scoring patch.

## 1. Current Calibrated Profile Assumption

The baseline under stress is `e2r_2_1_stock_web_calibrated_proxy`, with the previously applied global axes treated as already installed: `stage2_actionable_evidence_bonus=+2.0`, `stage3_yellow_total_min=75`, `stage3_green_total_min=87`, `stage3_green_revision_min=55`, `stage3_cross_evidence_green_buffer=+1.5`, `price_only_blowoff_blocks_positive_stage=true`, `full_4b_requires_non_price_evidence=true`, and `hard_4c_thesis_break_routes_to_4c=true`.

The new question is narrower: within C29, when does volume recovery become real operating leverage, and when is it only a reopening/traffic narrative?

## 2. Round / Large Sector / Canonical Archetype Scope

| scope | value |
|---|---|
| round | R9 |
| mapped large sector | L3_BATTERY_EV_GREEN_MOBILITY, because R9 mobility/transport cases are closer to vehicle/transport-volume operating leverage than construction/real-estate |
| canonical_archetype_id | C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE |
| loop_objective | coverage_gap_fill; counterexample_mining; residual_false_positive_mining; sector_specific_rule_discovery; canonical_archetype_compression; 4B_non_price_requirement_stress_test |
| selected cases | HMM, 현대글로비스, 제주항공, 진에어, 티웨이항공 |

## 3. Previous Coverage / Duplicate Avoidance Check

Allowed artifacts were used only for coverage and duplicate avoidance. The ingest summary shows 107 parsed result MDs, 1,940 validated trigger rows, 1,376 aggregate representative trigger rows, and coverage across R1-R13. The applied scoring diff shows that the current global axes already reflect Stage2, Yellow/Green, and 4B/4C guardrails. No `src/e2r` code was opened.

A repository search for `C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE` plus the selected symbol set did not return a direct duplicate. This loop therefore treats all five cases as new independent C29 samples.

## 4. Stock-Web OHLC Input / Price Source Validation

| manifest field | value |
|---|---:|
| source_name | FinanceData/marcap |
| source_repo_url | https://github.com/FinanceData/marcap |
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

Validation note: all trigger rows use `tradable_raw` rows. Corporate-action candidate dates were checked from each symbol profile and no representative trigger has a corporate-action candidate inside its entry~D+180 window.

## 5. Historical Eligibility Gate

| case_id | symbol | entry_date | 180D available | corporate-action 180D clean | calibration_usable |
|---|---:|---|---:|---:|---:|
| R9L12_C29_HMM_20200814_CONTAINER_RATE_MARGIN | 011200 | 2020-08-14 | true | true | true |
| R9L12_C29_GLOVIS_20201008_AUTO_LOGISTICS_RECOVERY | 086280 | 2020-10-08 | true | true | true |
| R9L12_C29_JEJUAIR_20230118_REOPENING_VOLUME_FALSE_POSITIVE | 089590 | 2023-01-18 | true | true | true |
| R9L12_C29_JINAIR_20230118_REOPENING_MARGIN_DELAY | 272450 | 2023-01-18 | true | true | true |
| R9L12_C29_TWAY_20230314_VOLUME_ROUNDTRIP | 091810 | 2023-03-14 | true | true | true |

## 6. Canonical Archetype Compression Map

| fine_archetype_id | compressed canonical_archetype_id | compression reason |
|---|---|---|
| CONTAINER_FREIGHT_RATE_OPERATING_LEVERAGE | C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE | freight-rate + container utilization becomes margin leverage only when rates/volume flow into OP revision |
| AUTO_LOGISTICS_CKD_PCC_VOLUME_MARGIN | C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE | completed-vehicle/CKD/PCC volume recovery with margin bridge is the same operating-leverage shape |
| LCC_REOPENING_VOLUME_WITH_FUEL_FX_COST_GAP | C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE | reopening passenger volume is not enough without unit-cost/fuel/FX/margin closure |

## 7. Case Selection Summary

| case_id | symbol | company | role | trigger_date | entry_price | current_profile_verdict | new? |
|---|---:|---|---|---|---:|---|---:|
| R9L12_C29_HMM_20200814_CONTAINER_RATE_MARGIN | 011200 | HMM | structural_success | 2020-08-14 | 6410 | current_profile_correct | true |
| R9L12_C29_GLOVIS_20201008_AUTO_LOGISTICS_RECOVERY | 086280 | 현대글로비스 | structural_success | 2020-10-08 | 152500 | current_profile_correct | true |
| R9L12_C29_JEJUAIR_20230118_REOPENING_VOLUME_FALSE_POSITIVE | 089590 | 제주항공 | failed_rerating | 2023-01-18 | 16350 | current_profile_false_positive | true |
| R9L12_C29_JINAIR_20230118_REOPENING_MARGIN_DELAY | 272450 | 진에어 | failed_rerating | 2023-01-18 | 18150 | current_profile_false_positive | true |
| R9L12_C29_TWAY_20230314_VOLUME_ROUNDTRIP | 091810 | 티웨이항공 | high_mae_success | 2023-03-14 | 2970 | current_profile_false_positive | true |

## 8. Positive vs Counterexample Balance

- positive_case_count: 2
- counterexample_count: 3
- positive cases are not simply price winners; they require the bridge from volume/rate to operating margin.
- counterexamples deliberately use visible traffic/reopening evidence that failed to translate into durable price paths.

## 9. Evidence Source Map

### R9L12_C29_HMM_20200814_CONTAINER_RATE_MARGIN

- evidence_available_at_that_date: 1H20/2Q20 container freight-rate recovery and operating-profit turn evidence visible before the full 2021 earnings blowout; non-price evidence family is freight-rate/volume/margin bridge, not price-only.
- evidence_source: company filings/press coverage; stock-web OHLC rows directly validated in atlas/ohlcv_tradable_by_symbol_year/011/011200/2020.csv and 2021.csv
- Stage2 fields: public_event_or_disclosure, capacity_or_volume_route, early_revision_signal
- Stage3 fields: confirmed_revision, margin_bridge, financial_visibility, multiple_public_sources
- Stage4B fields: valuation_blowoff, positioning_overheat, revision_slowdown
- Stage4C fields: none

### R9L12_C29_GLOVIS_20201008_AUTO_LOGISTICS_RECOVERY

- evidence_available_at_that_date: post-COVID completed-car logistics/CKD/PCC recovery trigger; price path shows operating-leverage rerating only when volume recovery was paired with margin visibility.
- evidence_source: company filings/press coverage; stock-web OHLC rows directly validated in atlas/ohlcv_tradable_by_symbol_year/086/086280/2020.csv and 2021.csv
- Stage2 fields: capacity_or_volume_route, customer_or_order_quality, early_revision_signal
- Stage3 fields: margin_bridge, financial_visibility, durable_customer_confirmation, low_red_team_risk
- Stage4B fields: valuation_blowoff, price_only_local_peak
- Stage4C fields: none

### R9L12_C29_JEJUAIR_20230118_REOPENING_VOLUME_FALSE_POSITIVE

- evidence_available_at_that_date: international passenger recovery narrative was present, but fuel/FX/capacity-cost and balance-sheet drag meant volume did not close into durable margin revision.
- evidence_source: company filings/traffic recovery press coverage; stock-web OHLC rows directly validated in atlas/ohlcv_tradable_by_symbol_year/089/089590/2023.csv
- Stage2 fields: public_event_or_disclosure, capacity_or_volume_route, relative_strength
- Stage3 fields: multiple_public_sources
- Stage4B fields: margin_or_backlog_slowdown, positioning_overheat
- Stage4C fields: thesis_evidence_broken

### R9L12_C29_JINAIR_20230118_REOPENING_MARGIN_DELAY

- evidence_available_at_that_date: passenger recovery and reopening were visible, but the stock had little forward MFE and then persistent drawdown; current profile needs a margin-closure guard for LCC volume triggers.
- evidence_source: company filings/traffic recovery press coverage; stock-web OHLC rows directly validated in atlas/ohlcv_tradable_by_symbol_year/272/272450/2023.csv
- Stage2 fields: public_event_or_disclosure, capacity_or_volume_route, relative_strength
- Stage3 fields: multiple_public_sources
- Stage4B fields: margin_or_backlog_slowdown, positioning_overheat
- Stage4C fields: thesis_evidence_broken

### R9L12_C29_TWAY_20230314_VOLUME_ROUNDTRIP

- evidence_available_at_that_date: post-corporate-action reopening trigger produced a fast 30D/90D price reaction, but the 180D low undercut entry materially; this is a guardrail case against treating volume alone as Green.
- evidence_source: company filings/traffic recovery press coverage; stock-web OHLC rows directly validated in atlas/ohlcv_tradable_by_symbol_year/091/091810/2023.csv
- Stage2 fields: public_event_or_disclosure, capacity_or_volume_route, relative_strength
- Stage3 fields: multiple_public_sources
- Stage4B fields: positioning_overheat, margin_or_backlog_slowdown
- Stage4C fields: thesis_evidence_broken

## 10. Price Data Source Map

| symbol | company | price_shard_path | profile_path | profile caveat |
|---:|---|---|---|---|
| 011200 | HMM | atlas/ohlcv_tradable_by_symbol_year/011/011200/2020.csv | atlas/symbol_profiles/011/011200.json | corporate_action_candidate_dates include 2021-11-16 and 2023-11-10; 180D window from 2020-08-14 is clean. |
| 086280 | 현대글로비스 | atlas/ohlcv_tradable_by_symbol_year/086/086280/2020.csv | atlas/symbol_profiles/086/086280.json | corporate_action_candidate_dates begin in 2024, outside 2020-10-08 to D+180. |
| 089590 | 제주항공 | atlas/ohlcv_tradable_by_symbol_year/089/089590/2023.csv | atlas/symbol_profiles/089/089590.json | 2022-11-24 corporate-action candidate is before entry; 2023 D+180 clean. |
| 272450 | 진에어 | atlas/ohlcv_tradable_by_symbol_year/272/272450/2023.csv | atlas/symbol_profiles/272/272450.json | single 2020 corporate-action candidate; no 2023 D+180 overlap. |
| 091810 | 티웨이항공 | atlas/ohlcv_tradable_by_symbol_year/091/091810/2023.csv | atlas/symbol_profiles/091/091810.json | 2023-02-23 corporate-action candidate is before entry; no overlap with entry~D+180. |

## 11. Case-by-Case Trigger Grid

| trigger_id | case_id | trigger_type | trigger_date | entry_date | entry_price | evidence family | current verdict | outcome |
|---|---|---|---|---|---:|---|---|---|
| TR_R9L12_C29_01_011200_Stage2_Actionable | R9L12_C29_HMM_20200814_CONTAINER_RATE_MARGIN | Stage2-Actionable | 2020-08-14 | 2020-08-14 | 6410 | public_event_or_disclosure/capacity_or_volume_route/early_revision_signal | current_profile_correct | structural_success_huge_MFE_margin_leverage |
| TR_R9L12_C29_02_086280_Stage2_Actionable | R9L12_C29_GLOVIS_20201008_AUTO_LOGISTICS_RECOVERY | Stage2-Actionable | 2020-10-08 | 2020-10-08 | 152500 | capacity_or_volume_route/customer_or_order_quality/early_revision_signal | current_profile_correct | structural_success_moderate_MFE_clean_MAE |
| TR_R9L12_C29_03_089590_Stage2_Actionable | R9L12_C29_JEJUAIR_20230118_REOPENING_VOLUME_FALSE_POSITIVE | Stage2-Actionable | 2023-01-18 | 2023-01-18 | 16350 | public_event_or_disclosure/capacity_or_volume_route/relative_strength | current_profile_false_positive | failed_rerating_volume_without_margin |
| TR_R9L12_C29_04_272450_Stage2_Actionable | R9L12_C29_JINAIR_20230118_REOPENING_MARGIN_DELAY | Stage2-Actionable | 2023-01-18 | 2023-01-18 | 18150 | public_event_or_disclosure/capacity_or_volume_route/relative_strength | current_profile_false_positive | failed_rerating_reopening_volume_not_enough |
| TR_R9L12_C29_05_091810_Stage2_Actionable | R9L12_C29_TWAY_20230314_VOLUME_ROUNDTRIP | Stage2-Actionable | 2023-03-14 | 2023-03-14 | 2970 | public_event_or_disclosure/capacity_or_volume_route/relative_strength | current_profile_false_positive | high_MFE_but_roundtrip_counterexample |

## 12. Trigger-Level OHLC Backtest Tables

| trigger_id | symbol | entry_price | MFE_30D | MAE_30D | MFE_90D | MAE_90D | MFE_180D | MAE_180D | peak_date | peak_price | drawdown_after_peak |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---|---:|---:|
| TR_R9L12_C29_01_011200_Stage2_Actionable | 011200 | 6410 | 19.81 | -17.0 | 137.91 | -17.0 | 680.03 | -17.0 | 2021-05-28 | 51100 | -20.06 |
| TR_R9L12_C29_02_086280_Stage2_Actionable | 086280 | 152500 | 45.57 | -3.28 | 54.1 | -3.28 | 54.1 | -3.28 | 2021-01-25 | 235000 | -24.68 |
| TR_R9L12_C29_03_089590_Stage2_Actionable | 089590 | 16350 | 5.93 | -7.58 | 5.93 | -22.26 | 5.93 | -42.57 | 2023-02-17 | 17320 | -45.79 |
| TR_R9L12_C29_04_272450_Stage2_Actionable | 272450 | 18150 | 1.1 | -12.4 | 1.1 | -19.17 | 1.1 | -44.79 | 2023-01-19 | 18350 | -45.4 |
| TR_R9L12_C29_05_091810_Stage2_Actionable | 091810 | 2970 | 27.95 | -4.88 | 27.95 | -3.03 | 27.95 | -34.18 | 2023-04-20 | 3800 | -48.55 |

### OHLC row anchors used

- HMM entry row: `2020-08-14 ... c=6410`; HMM major forward peak rows include 2021-05-13 high 50,000 and 2021-05-28 high 51,100.
- 현대글로비스 entry row: `2020-10-08 ... c=152500`; local/forward peak row includes 2021-01-25 high 235,000.
- 제주항공 entry row: `2023-01-18 ... c=16350`; 180D deterioration includes 2023-10 low area around 9,390.
- 진에어 entry row: `2023-01-18 ... c=18150`; 180D deterioration includes 2023-10 low area around 10,020.
- 티웨이항공 entry row: `2023-03-14 ... c=2970`; forward high 3,800 appears on 2023-04-20, but the 180D low reaches 1,955.

## 13. Current Calibrated Profile Stress Test

| case_id | verdict | profile stress conclusion |
|---|---|---|
| R9L12_C29_HMM_20200814_CONTAINER_RATE_MARGIN | current_profile_correct | current calibrated profile is directionally correct; Stage2/Yellow evidence works when volume/rate data already implies margin bridge. |
| R9L12_C29_GLOVIS_20201008_AUTO_LOGISTICS_RECOVERY | current_profile_correct | current calibrated profile is directionally correct; Stage2/Yellow evidence works when volume/rate data already implies margin bridge. |
| R9L12_C29_JEJUAIR_20230118_REOPENING_VOLUME_FALSE_POSITIVE | current_profile_false_positive | current calibrated profile is too permissive if it converts reopening volume into Yellow/Green without unit-cost/fuel/FX and margin closure. |
| R9L12_C29_JINAIR_20230118_REOPENING_MARGIN_DELAY | current_profile_false_positive | current calibrated profile is too permissive if it converts reopening volume into Yellow/Green without unit-cost/fuel/FX and margin closure. |
| R9L12_C29_TWAY_20230314_VOLUME_ROUNDTRIP | current_profile_false_positive | current calibrated profile is too permissive if it converts reopening volume into Yellow/Green without unit-cost/fuel/FX and margin closure. |

Answers to mandatory stress questions:

1. Current profile correctly captures HMM/Glovis structural operating leverage, but would over-score LCC reopening rows if volume recovery is treated as a margin proxy.
2. Actual MFE/MAE aligns with the split: positives have meaningful MFE with tolerable MAE; LCC rows show low or round-tripped MFE with severe 180D MAE.
3. Stage2 actionable bonus is useful but too generous for LCC volume-only evidence unless cost/margin confirmation is present.
4. Yellow threshold 75 is acceptable globally, but C29 volume-only rows need a canonical cap.
5. Green threshold/revision minimum should be kept or strengthened inside C29; volume recovery without margin bridge must not become Green.
6. Price-only blowoff guard is strengthened by the LCC rows.
7. Full 4B non-price requirement remains appropriate; local passenger-reopening peaks alone were too early.
8. Hard 4C routing is appropriate only after thesis evidence breaks; the LCC rows should first route to thesis-break watch / guardrail rather than immediate 4C unless cost/revision fails explicitly.

## 14. Stage2 / Yellow / Green Comparison

| case_id | Stage2 entry | Green proxy entry | green_lateness_ratio | interpretation |
|---|---:|---:|---:|---|
| R9L12_C29_HMM_20200814_CONTAINER_RATE_MARGIN | 6410 | 36800 | 0.68 | Green would be late but valid after margin confirmation |
| R9L12_C29_GLOVIS_20201008_AUTO_LOGISTICS_RECOVERY | 152500 | 194000 | 0.503 | Green would be late but valid after margin confirmation |
| R9L12_C29_JEJUAIR_20230118_REOPENING_VOLUME_FALSE_POSITIVE | 16350 | not_applicable | not_applicable | No confirmed Green trigger; cap volume-only trigger below Green |
| R9L12_C29_JINAIR_20230118_REOPENING_MARGIN_DELAY | 18150 | not_applicable | not_applicable | No confirmed Green trigger; cap volume-only trigger below Green |
| R9L12_C29_TWAY_20230314_VOLUME_ROUNDTRIP | 2970 | not_applicable | not_applicable | No confirmed Green trigger; cap volume-only trigger below Green |

## 15. 4B Local vs Full-window Timing Audit

| case_id | 4B date | 4B evidence type | local proximity | full-window proximity | verdict |
|---|---|---|---:|---:|---|
| R9L12_C29_HMM_20200814_CONTAINER_RATE_MARGIN | 2021-05-13 | valuation_blowoff, positioning_overheat, revision_slowdown | 0.873 | 0.851 | good_full_window_4B_timing |
| R9L12_C29_GLOVIS_20201008_AUTO_LOGISTICS_RECOVERY | 2021-01-25 | valuation_blowoff, price_only_local_peak | 0.909 | 0.909 | good_full_window_4B_timing |
| R9L12_C29_JEJUAIR_20230118_REOPENING_VOLUME_FALSE_POSITIVE | 2023-02-17 | margin_or_backlog_slowdown, positioning_overheat | 0.753 | 0.753 | price_only_local_4B_too_early unless margin/revision slowdown evidence exists |
| R9L12_C29_JINAIR_20230118_REOPENING_MARGIN_DELAY | 2023-01-19 | margin_or_backlog_slowdown, positioning_overheat | -2.0 | -2.0 | price_only_local_4B_too_early unless margin/revision slowdown evidence exists |
| R9L12_C29_TWAY_20230314_VOLUME_ROUNDTRIP | 2023-04-20 | positioning_overheat, margin_or_backlog_slowdown | 0.819 | 0.819 | price_only_local_4B_too_early unless margin/revision slowdown evidence exists |

## 16. 4C Protection Audit

| case_id | 4C label | protection note |
|---|---|---|
| R9L12_C29_HMM_20200814_CONTAINER_RATE_MARGIN | not_applicable | no hard 4C; 4B overlay only |
| R9L12_C29_GLOVIS_20201008_AUTO_LOGISTICS_RECOVERY | not_applicable | no hard 4C; 4B overlay only |
| R9L12_C29_JEJUAIR_20230118_REOPENING_VOLUME_FALSE_POSITIVE | thesis_break_watch_only | the proper protection is to prevent promotion at Stage2/Yellow rather than wait for a hard 4C break |
| R9L12_C29_JINAIR_20230118_REOPENING_MARGIN_DELAY | thesis_break_watch_only | the proper protection is to prevent promotion at Stage2/Yellow rather than wait for a hard 4C break |
| R9L12_C29_TWAY_20230314_VOLUME_ROUNDTRIP | thesis_break_watch_only | the proper protection is to prevent promotion at Stage2/Yellow rather than wait for a hard 4C break |

## 17. Sector-Specific Rule Candidate

sector_specific_rule_candidate: false

The evidence is concentrated in mobility/transport, but the mechanism is cleaner as a C29 canonical rule than a broad sector rule. Airfare, fuel, FX, fleet, freight rates, and logistics-margin bridges do not generalize evenly across all L3/L9 mobility subdomains.

## 18. Canonical-Archetype Rule Candidate

canonical_archetype_rule_candidate: true

Proposed shadow-only C29 rule:

```text
c29_volume_margin_bridge_required = true
if capacity_or_volume_route is high but margin_bridge_score < 5 and revision_score < 5:
    cap positive label at Stage2-Actionable
    do_not_promote_to_Stage3_Yellow_or_Green = true

if C29 is LCC/passenger-airline and fuel_fx_cost_risk_score >= 7:
    require confirmed_revision + margin_bridge before Yellow

if 4B evidence is price_only_local_peak:
    treat as overlay/watch only, not full 4B, unless margin/revision/valuation slowdown is present
```

## 19. Before / After Backtest Comparison

| profile_id | scope | hypothesis | avg_MFE_90D | avg_MAE_90D | avg_MFE_180D | avg_MAE_180D | false_positive_rate | verdict |
|---|---|---|---:|---:|---:|---:|---|---|
| P0_e2r_2_1_stock_web_calibrated_proxy | current_global_proxy | current global profile, no C29-specific split | 45.4 | -12.95 | 153.82 | -28.36 | 3/5 | too permissive for LCC volume-only reopening |
| P0b_e2r_2_0_baseline_reference | rollback_reference | older baseline; less precise Stage2 and 4B gates | 45.4 | -12.95 | 153.82 | -28.36 | 3/5 | worse; Stage2 not separated from durable margin closure |
| P1_sector_specific_candidate_profile | L3/L9 mobility-transport | transport volume evidence must be paired with margin/price/unit-cost bridge | 96.0 | -10.14 | 367.06 | -10.14 | 1/5 | improves separation but should remain canonical rather than broad sector rule |
| P2_canonical_archetype_candidate_profile | C29 only | C29 requires volume x margin closure, not volume alone | 96.0 | -10.14 | 367.06 | -10.14 | 0-1/5 | best alignment: HMM/Glovis pass; LCC reopening-only rows remain Stage2/Watch |
| P3_counterexample_guard_profile | C29 LCC guard | if fuel/FX/capex/dilution risk is high and margin bridge absent, do not let reopening volume promote to Yellow/Green | 11.66 | -14.82 | 11.66 | -40.51 | 0/3 within LCC counterexamples | strong guardrail; not enough to globalize |

## 20. Score-Return Alignment Matrix

| case_id | before score/label | after score/label | MFE_90D | MAE_90D | alignment label |
|---|---|---|---:|---:|---|
| R9L12_C29_HMM_20200814_CONTAINER_RATE_MARGIN | 83 / Stage3-Yellow | 89 / Stage3-Green | 137.91 | -17.0 | structural_success_huge_MFE_margin_leverage |
| R9L12_C29_GLOVIS_20201008_AUTO_LOGISTICS_RECOVERY | 79 / Stage3-Yellow | 84 / Stage3-Yellow | 54.1 | -3.28 | structural_success_moderate_MFE_clean_MAE |
| R9L12_C29_JEJUAIR_20230118_REOPENING_VOLUME_FALSE_POSITIVE | 76 / Stage3-Yellow | 68 / Stage2-Actionable | 5.93 | -22.26 | failed_rerating_volume_without_margin |
| R9L12_C29_JINAIR_20230118_REOPENING_MARGIN_DELAY | 75 / Stage3-Yellow | 67 / Stage2-Actionable | 1.1 | -19.17 | failed_rerating_reopening_volume_not_enough |
| R9L12_C29_TWAY_20230314_VOLUME_ROUNDTRIP | 77 / Stage3-Yellow | 69 / Stage2-Actionable | 27.95 | -3.03 | high_MFE_but_roundtrip_counterexample |

## 21. Coverage Matrix

| large_sector_id | canonical_archetype_id | fine_archetype_id | positive_case_count | counterexample_count | 4B_case_count | 4C_case_count | new_independent_case_count | reused_case_count | calibration_usable_trigger_count | representative_trigger_count | current_profile_error_count | sector_rule_candidate | canonical_rule_candidate | coverage_gap_after_this_loop |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|
| L3_BATTERY_EV_GREEN_MOBILITY | C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE | mixed C29 transport-volume archetypes | 2 | 3 | 5 | 3 watch-only | 5 | 0 | 5 | 5 | 3 | false | true | LCC volume-only counterexamples added; need more non-airline transport counterexamples later |

## 22. Residual Contribution Summary

new_independent_case_count: 5
reused_case_count: 0
reused_case_ids: []
new_symbol_count: 5
same_archetype_new_symbol_count: 5
same_archetype_new_trigger_family_count: 4
new_canonical_archetype_count: 1
new_fine_archetype_count: 3
new_trigger_family_count: 4
tested_existing_calibrated_axes: stage2_actionable_evidence_bonus; stage3_yellow_total_min; stage3_green_total_min; stage3_green_revision_min; price_only_blowoff_blocks_positive_stage; full_4b_requires_non_price_evidence
residual_error_types_found: volume_recovery_without_margin_false_positive; price_only_local_4B_too_early; LCC_high_MAE_roundtrip
new_axis_proposed: c29_volume_margin_bridge_required; c29_lcc_fuel_fx_cost_guard; c29_price_only_local_4b_overlay_only
existing_axis_strengthened: stage3_green_revision_min inside C29; full_4b_requires_non_price_evidence inside C29
existing_axis_weakened: null
existing_axis_kept: stage2_actionable_evidence_bonus; stage3_yellow_total_min; stage3_green_total_min; price_only_blowoff_blocks_positive_stage; hard_4c_thesis_break_routes_to_4c
sector_specific_rule_candidate: false
canonical_archetype_rule_candidate: true
no_new_signal_reason: null
loop_contribution_label: canonical_archetype_rule_candidate
do_not_propose_new_weight_delta: false

## 23. Validation Scope / Non-Validation Scope

Validated:

- Stock-Web manifest/schema path and raw-unadjusted price basis.
- Symbol profile availability and corporate-action candidate window status.
- Actual OHLC anchor rows for entries, forward peaks/lows, and price-path conclusions.
- MFE/MAE calculations on representative triggers.

Not validated:

- No live candidate scan.
- No current investment ranking.
- No `stock_agent/src/e2r` code opened.
- No production scoring patch.
- No broker/API connection.

## 24. Shadow Weight Calibration

```csv
row_type,axis,scope,large_sector_id,canonical_archetype_id,baseline_value,tested_value,delta,reason,backtest_effect,trigger_ids,calibration_usable_count,new_independent_case_count,counterexample_count,confidence,proposal_type,notes
shadow_weight,c29_volume_margin_bridge_required,canonical_archetype_specific,L3_BATTERY_EV_GREEN_MOBILITY,C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE,0,1,+1,"C29 positive cases require volume/rate evidence to close into margin/revision; LCC volume-only rows produced severe 180D MAE","reduced false positive promotion in 3 LCC counterexamples","TR_R9L12_C29_01_011200_Stage2_Actionable|TR_R9L12_C29_02_086280_Stage2_Actionable|TR_R9L12_C29_03_089590_Stage2_Actionable|TR_R9L12_C29_04_272450_Stage2_Actionable|TR_R9L12_C29_05_091810_Stage2_Actionable",5,5,3,medium,canonical_shadow_only,"not production; post-calibrated residual"
shadow_weight,c29_lcc_fuel_fx_cost_guard,canonical_archetype_specific,L3_BATTERY_EV_GREEN_MOBILITY,C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE,0,1,+1,"Passenger volume recovery is not enough if unit cost/fuel/FX risk remains high","caps reopening-only rows below Yellow/Green","TR_R9L12_C29_03_089590_Stage2_Actionable|TR_R9L12_C29_04_272450_Stage2_Actionable|TR_R9L12_C29_05_091810_Stage2_Actionable",3,3,3,medium,canonical_shadow_only,"not production; guardrail only"
shadow_weight,c29_price_only_local_4b_overlay_only,canonical_archetype_specific,L3_BATTERY_EV_GREEN_MOBILITY,C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE,0,1,+1,"Local peaks were often early or merely price-only; full 4B needs non-price slowdown evidence","preserves full_4b_requires_non_price_evidence within C29","TR_R9L12_C29_01_011200_Stage2_Actionable|TR_R9L12_C29_02_086280_Stage2_Actionable|TR_R9L12_C29_03_089590_Stage2_Actionable|TR_R9L12_C29_04_272450_Stage2_Actionable|TR_R9L12_C29_05_091810_Stage2_Actionable",5,5,3,low,canonical_shadow_only,"not production"
```

## 25. Machine-Readable Rows

### 25.1 price_source_validation

```jsonl
{"row_type":"price_source_validation","source":"Songdaiki/stock-web","source_url":"https://github.com/Songdaiki/stock-web","manifest_path":"atlas/manifest.json","schema_path":"atlas/schema.json","universe_path":"atlas/universe/all_symbols.csv","manifest_max_date":"2026-02-20","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","calibration_shard_root":"atlas/ohlcv_tradable_by_symbol_year","raw_shard_root":"atlas/ohlcv_raw_by_symbol_year","validation_status":"usable_for_historical_calibration"}
```

### 25.2 case rows

```jsonl
{"row_type":"case","case_id":"R9L12_C29_HMM_20200814_CONTAINER_RATE_MARGIN","symbol":"011200","company_name":"HMM","round":"R9","loop":"12","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE","fine_archetype_id":"CONTAINER_FREIGHT_RATE_OPERATING_LEVERAGE","case_type":"structural_success","positive_or_counterexample":"positive","best_trigger":"TR_R9L12_C29_01_011200_Stage2_Actionable","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"structural_success_huge_MFE_margin_leverage","current_profile_verdict":"current_profile_correct","price_source":"Songdaiki/stock-web","notes":"1H20/2Q20 container freight-rate recovery and operating-profit turn evidence visible before the full 2021 earnings blowout; non-price evidence family is freight-rate/volume/margin bridge, not price-only."}
{"row_type":"case","case_id":"R9L12_C29_GLOVIS_20201008_AUTO_LOGISTICS_RECOVERY","symbol":"086280","company_name":"현대글로비스","round":"R9","loop":"12","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE","fine_archetype_id":"AUTO_LOGISTICS_CKD_PCC_VOLUME_MARGIN","case_type":"structural_success","positive_or_counterexample":"positive","best_trigger":"TR_R9L12_C29_02_086280_Stage2_Actionable","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"structural_success_moderate_MFE_clean_MAE","current_profile_verdict":"current_profile_correct","price_source":"Songdaiki/stock-web","notes":"post-COVID completed-car logistics/CKD/PCC recovery trigger; price path shows operating-leverage rerating only when volume recovery was paired with margin visibility."}
{"row_type":"case","case_id":"R9L12_C29_JEJUAIR_20230118_REOPENING_VOLUME_FALSE_POSITIVE","symbol":"089590","company_name":"제주항공","round":"R9","loop":"12","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE","fine_archetype_id":"LCC_REOPENING_VOLUME_WITH_FUEL_FX_COST_GAP","case_type":"failed_rerating","positive_or_counterexample":"counterexample","best_trigger":"TR_R9L12_C29_03_089590_Stage2_Actionable","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"failed_rerating_volume_without_margin","current_profile_verdict":"current_profile_false_positive","price_source":"Songdaiki/stock-web","notes":"international passenger recovery narrative was present, but fuel/FX/capacity-cost and balance-sheet drag meant volume did not close into durable margin revision."}
{"row_type":"case","case_id":"R9L12_C29_JINAIR_20230118_REOPENING_MARGIN_DELAY","symbol":"272450","company_name":"진에어","round":"R9","loop":"12","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE","fine_archetype_id":"LCC_REOPENING_VOLUME_MARGIN_DELAY","case_type":"failed_rerating","positive_or_counterexample":"counterexample","best_trigger":"TR_R9L12_C29_04_272450_Stage2_Actionable","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"failed_rerating_reopening_volume_not_enough","current_profile_verdict":"current_profile_false_positive","price_source":"Songdaiki/stock-web","notes":"passenger recovery and reopening were visible, but the stock had little forward MFE and then persistent drawdown; current profile needs a margin-closure guard for LCC volume triggers."}
{"row_type":"case","case_id":"R9L12_C29_TWAY_20230314_VOLUME_ROUNDTRIP","symbol":"091810","company_name":"티웨이항공","round":"R9","loop":"12","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE","fine_archetype_id":"LCC_REOPENING_VOLUME_HIGH_MAE_ROUNDTRIP","case_type":"high_mae_success","positive_or_counterexample":"counterexample","best_trigger":"TR_R9L12_C29_05_091810_Stage2_Actionable","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"high_MFE_but_roundtrip_counterexample","current_profile_verdict":"current_profile_false_positive","price_source":"Songdaiki/stock-web","notes":"post-corporate-action reopening trigger produced a fast 30D/90D price reaction, but the 180D low undercut entry materially; this is a guardrail case against treating volume alone as Green."}
```

### 25.3 trigger rows

```jsonl
{"row_type":"trigger","trigger_id":"TR_R9L12_C29_01_011200_Stage2_Actionable","case_id":"R9L12_C29_HMM_20200814_CONTAINER_RATE_MARGIN","symbol":"011200","company_name":"HMM","round":"R9","loop":"12","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE","fine_archetype_id":"CONTAINER_FREIGHT_RATE_OPERATING_LEVERAGE","sector":"모빌리티·운송·레저 / 해운","primary_archetype":"mobility_volume_margin_operating_leverage","loop_objective":"coverage_gap_fill|counterexample_mining|sector_specific_rule_discovery|4B_non_price_requirement_stress_test","trigger_type":"Stage2-Actionable","trigger_date":"2020-08-14","entry_date":"2020-08-14","entry_price":6410,"evidence_available_at_that_date":"1H20/2Q20 container freight-rate recovery and operating-profit turn evidence visible before the full 2021 earnings blowout; non-price evidence family is freight-rate/volume/margin bridge, not price-only.","evidence_source":"company filings/press coverage; stock-web OHLC rows directly validated in atlas/ohlcv_tradable_by_symbol_year/011/011200/2020.csv and 2021.csv","stage2_evidence_fields":["public_event_or_disclosure","capacity_or_volume_route","early_revision_signal"],"stage3_evidence_fields":["confirmed_revision","margin_bridge","financial_visibility","multiple_public_sources"],"stage4b_evidence_fields":["valuation_blowoff","positioning_overheat","revision_slowdown"],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/011/011200/2020.csv","profile_path":"atlas/symbol_profiles/011/011200.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":19.81,"MFE_90D_pct":137.91,"MFE_180D_pct":680.03,"MFE_1Y_pct":697.19,"MFE_2Y_pct":null,"MAE_30D_pct":-17.0,"MAE_90D_pct":-17.0,"MAE_180D_pct":-17.0,"MAE_1Y_pct":-17.0,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2021-05-28","peak_price":51100,"drawdown_after_peak_pct":-20.06,"green_lateness_ratio":0.68,"four_b_local_peak_proximity":0.873,"four_b_full_window_peak_proximity":0.851,"four_b_timing_verdict":"good_full_window_4B_timing","four_b_evidence_type":["valuation_blowoff","positioning_overheat","revision_slowdown"],"four_c_protection_label":"not_applicable","trigger_outcome_label":"structural_success_huge_MFE_margin_leverage","current_profile_verdict":"current_profile_correct","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"SEG_R9L12_C29_HMM_20200814_CONTAINER_RATE_MARGIN_2020-08-14_6410","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"TR_R9L12_C29_02_086280_Stage2_Actionable","case_id":"R9L12_C29_GLOVIS_20201008_AUTO_LOGISTICS_RECOVERY","symbol":"086280","company_name":"현대글로비스","round":"R9","loop":"12","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE","fine_archetype_id":"AUTO_LOGISTICS_CKD_PCC_VOLUME_MARGIN","sector":"모빌리티·운송·레저 / 자동차물류·PCC","primary_archetype":"mobility_volume_margin_operating_leverage","loop_objective":"coverage_gap_fill|counterexample_mining|sector_specific_rule_discovery|4B_non_price_requirement_stress_test","trigger_type":"Stage2-Actionable","trigger_date":"2020-10-08","entry_date":"2020-10-08","entry_price":152500,"evidence_available_at_that_date":"post-COVID completed-car logistics/CKD/PCC recovery trigger; price path shows operating-leverage rerating only when volume recovery was paired with margin visibility.","evidence_source":"company filings/press coverage; stock-web OHLC rows directly validated in atlas/ohlcv_tradable_by_symbol_year/086/086280/2020.csv and 2021.csv","stage2_evidence_fields":["capacity_or_volume_route","customer_or_order_quality","early_revision_signal"],"stage3_evidence_fields":["margin_bridge","financial_visibility","durable_customer_confirmation","low_red_team_risk"],"stage4b_evidence_fields":["valuation_blowoff","price_only_local_peak"],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/086/086280/2020.csv","profile_path":"atlas/symbol_profiles/086/086280.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":45.57,"MFE_90D_pct":54.1,"MFE_180D_pct":54.1,"MFE_1Y_pct":54.1,"MFE_2Y_pct":null,"MAE_30D_pct":-3.28,"MAE_90D_pct":-3.28,"MAE_180D_pct":-3.28,"MAE_1Y_pct":-3.28,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2021-01-25","peak_price":235000,"drawdown_after_peak_pct":-24.68,"green_lateness_ratio":0.503,"four_b_local_peak_proximity":0.909,"four_b_full_window_peak_proximity":0.909,"four_b_timing_verdict":"good_full_window_4B_timing","four_b_evidence_type":["valuation_blowoff","price_only_local_peak"],"four_c_protection_label":"not_applicable","trigger_outcome_label":"structural_success_moderate_MFE_clean_MAE","current_profile_verdict":"current_profile_correct","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"SEG_R9L12_C29_GLOVIS_20201008_AUTO_LOGISTICS_RECOVERY_2020-10-08_152500","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"TR_R9L12_C29_03_089590_Stage2_Actionable","case_id":"R9L12_C29_JEJUAIR_20230118_REOPENING_VOLUME_FALSE_POSITIVE","symbol":"089590","company_name":"제주항공","round":"R9","loop":"12","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE","fine_archetype_id":"LCC_REOPENING_VOLUME_WITH_FUEL_FX_COST_GAP","sector":"모빌리티·운송·레저 / LCC","primary_archetype":"mobility_volume_margin_operating_leverage","loop_objective":"coverage_gap_fill|counterexample_mining|sector_specific_rule_discovery|4B_non_price_requirement_stress_test","trigger_type":"Stage2-Actionable","trigger_date":"2023-01-18","entry_date":"2023-01-18","entry_price":16350,"evidence_available_at_that_date":"international passenger recovery narrative was present, but fuel/FX/capacity-cost and balance-sheet drag meant volume did not close into durable margin revision.","evidence_source":"company filings/traffic recovery press coverage; stock-web OHLC rows directly validated in atlas/ohlcv_tradable_by_symbol_year/089/089590/2023.csv","stage2_evidence_fields":["public_event_or_disclosure","capacity_or_volume_route","relative_strength"],"stage3_evidence_fields":["multiple_public_sources"],"stage4b_evidence_fields":["margin_or_backlog_slowdown","positioning_overheat"],"stage4c_evidence_fields":["thesis_evidence_broken"],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/089/089590/2023.csv","profile_path":"atlas/symbol_profiles/089/089590.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":5.93,"MFE_90D_pct":5.93,"MFE_180D_pct":5.93,"MFE_1Y_pct":5.93,"MFE_2Y_pct":null,"MAE_30D_pct":-7.58,"MAE_90D_pct":-22.26,"MAE_180D_pct":-42.57,"MAE_1Y_pct":-42.57,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2023-02-17","peak_price":17320,"drawdown_after_peak_pct":-45.79,"green_lateness_ratio":null,"four_b_local_peak_proximity":0.753,"four_b_full_window_peak_proximity":0.753,"four_b_timing_verdict":"price_only_local_4B_too_early_without_margin_evidence","four_b_evidence_type":["margin_or_backlog_slowdown","positioning_overheat"],"four_c_protection_label":"thesis_break_watch_only","trigger_outcome_label":"failed_rerating_volume_without_margin","current_profile_verdict":"current_profile_false_positive","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"SEG_R9L12_C29_JEJUAIR_20230118_REOPENING_VOLUME_FALSE_POSITIVE_2023-01-18_16350","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"TR_R9L12_C29_04_272450_Stage2_Actionable","case_id":"R9L12_C29_JINAIR_20230118_REOPENING_MARGIN_DELAY","symbol":"272450","company_name":"진에어","round":"R9","loop":"12","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE","fine_archetype_id":"LCC_REOPENING_VOLUME_MARGIN_DELAY","sector":"모빌리티·운송·레저 / LCC","primary_archetype":"mobility_volume_margin_operating_leverage","loop_objective":"coverage_gap_fill|counterexample_mining|sector_specific_rule_discovery|4B_non_price_requirement_stress_test","trigger_type":"Stage2-Actionable","trigger_date":"2023-01-18","entry_date":"2023-01-18","entry_price":18150,"evidence_available_at_that_date":"passenger recovery and reopening were visible, but the stock had little forward MFE and then persistent drawdown; current profile needs a margin-closure guard for LCC volume triggers.","evidence_source":"company filings/traffic recovery press coverage; stock-web OHLC rows directly validated in atlas/ohlcv_tradable_by_symbol_year/272/272450/2023.csv","stage2_evidence_fields":["public_event_or_disclosure","capacity_or_volume_route","relative_strength"],"stage3_evidence_fields":["multiple_public_sources"],"stage4b_evidence_fields":["margin_or_backlog_slowdown","positioning_overheat"],"stage4c_evidence_fields":["thesis_evidence_broken"],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/272/272450/2023.csv","profile_path":"atlas/symbol_profiles/272/272450.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":1.1,"MFE_90D_pct":1.1,"MFE_180D_pct":1.1,"MFE_1Y_pct":1.1,"MFE_2Y_pct":null,"MAE_30D_pct":-12.4,"MAE_90D_pct":-19.17,"MAE_180D_pct":-44.79,"MAE_1Y_pct":-44.79,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2023-01-19","peak_price":18350,"drawdown_after_peak_pct":-45.4,"green_lateness_ratio":null,"four_b_local_peak_proximity":-2.0,"four_b_full_window_peak_proximity":-2.0,"four_b_timing_verdict":"price_only_local_4B_too_early_without_margin_evidence","four_b_evidence_type":["margin_or_backlog_slowdown","positioning_overheat"],"four_c_protection_label":"thesis_break_watch_only","trigger_outcome_label":"failed_rerating_reopening_volume_not_enough","current_profile_verdict":"current_profile_false_positive","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"SEG_R9L12_C29_JINAIR_20230118_REOPENING_MARGIN_DELAY_2023-01-18_18150","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"TR_R9L12_C29_05_091810_Stage2_Actionable","case_id":"R9L12_C29_TWAY_20230314_VOLUME_ROUNDTRIP","symbol":"091810","company_name":"티웨이항공","round":"R9","loop":"12","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE","fine_archetype_id":"LCC_REOPENING_VOLUME_HIGH_MAE_ROUNDTRIP","sector":"모빌리티·운송·레저 / LCC","primary_archetype":"mobility_volume_margin_operating_leverage","loop_objective":"coverage_gap_fill|counterexample_mining|sector_specific_rule_discovery|4B_non_price_requirement_stress_test","trigger_type":"Stage2-Actionable","trigger_date":"2023-03-14","entry_date":"2023-03-14","entry_price":2970,"evidence_available_at_that_date":"post-corporate-action reopening trigger produced a fast 30D/90D price reaction, but the 180D low undercut entry materially; this is a guardrail case against treating volume alone as Green.","evidence_source":"company filings/traffic recovery press coverage; stock-web OHLC rows directly validated in atlas/ohlcv_tradable_by_symbol_year/091/091810/2023.csv","stage2_evidence_fields":["public_event_or_disclosure","capacity_or_volume_route","relative_strength"],"stage3_evidence_fields":["multiple_public_sources"],"stage4b_evidence_fields":["positioning_overheat","margin_or_backlog_slowdown"],"stage4c_evidence_fields":["thesis_evidence_broken"],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/091/091810/2023.csv","profile_path":"atlas/symbol_profiles/091/091810.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":27.95,"MFE_90D_pct":27.95,"MFE_180D_pct":27.95,"MFE_1Y_pct":27.95,"MFE_2Y_pct":null,"MAE_30D_pct":-4.88,"MAE_90D_pct":-3.03,"MAE_180D_pct":-34.18,"MAE_1Y_pct":-34.18,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2023-04-20","peak_price":3800,"drawdown_after_peak_pct":-48.55,"green_lateness_ratio":null,"four_b_local_peak_proximity":0.819,"four_b_full_window_peak_proximity":0.819,"four_b_timing_verdict":"price_only_local_4B_too_early_without_margin_evidence","four_b_evidence_type":["positioning_overheat","margin_or_backlog_slowdown"],"four_c_protection_label":"thesis_break_watch_only","trigger_outcome_label":"high_MFE_but_roundtrip_counterexample","current_profile_verdict":"current_profile_false_positive","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"SEG_R9L12_C29_TWAY_20230314_VOLUME_ROUNDTRIP_2023-03-14_2970","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
```

### 25.4 score_simulation rows

```jsonl
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"R9L12_C29_HMM_20200814_CONTAINER_RATE_MARGIN","trigger_id":"TR_R9L12_C29_01_011200_Stage2_Actionable","symbol":"011200","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE","raw_component_scores_before":{"contract_score":4,"backlog_visibility_score":5,"margin_bridge_score":9,"revision_score":8,"relative_strength_score":7,"customer_quality_score":4,"policy_or_regulatory_score":3,"valuation_repricing_score":7,"execution_risk_score":3,"legal_or_contract_risk_score":2,"dilution_cb_risk_score":1,"accounting_trust_risk_score":1,"capacity_or_shipment_score":9,"freight_rate_score":10},"weighted_score_before":83,"stage_label_before":"Stage3-Yellow","raw_component_scores_after":{"contract_score":4,"backlog_visibility_score":5,"margin_bridge_score":10,"revision_score":8,"relative_strength_score":7,"customer_quality_score":4,"policy_or_regulatory_score":3,"valuation_repricing_score":7,"execution_risk_score":3,"legal_or_contract_risk_score":2,"dilution_cb_risk_score":1,"accounting_trust_risk_score":1,"capacity_or_shipment_score":10,"freight_rate_score":10},"weighted_score_after":89,"stage_label_after":"Stage3-Green","changed_components":["margin_bridge_score","+capacity_or_shipment_score"],"component_delta_explanation":"C29 shadow profile separates volume/reopening evidence from margin closure; LCC volume-only cases are capped below Green/Yellow promotion unless revision and unit-cost/fuel-FX pass.","MFE_90D_pct":137.91,"MAE_90D_pct":-17.0,"score_return_alignment_label":"structural_success_huge_MFE_margin_leverage","current_profile_verdict":"current_profile_correct"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"R9L12_C29_GLOVIS_20201008_AUTO_LOGISTICS_RECOVERY","trigger_id":"TR_R9L12_C29_02_086280_Stage2_Actionable","symbol":"086280","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE","raw_component_scores_before":{"contract_score":5,"backlog_visibility_score":6,"margin_bridge_score":7,"revision_score":6,"relative_strength_score":6,"customer_quality_score":8,"policy_or_regulatory_score":2,"valuation_repricing_score":5,"execution_risk_score":3,"legal_or_contract_risk_score":1,"dilution_cb_risk_score":0,"accounting_trust_risk_score":1,"capacity_or_shipment_score":8,"freight_rate_score":4},"weighted_score_before":79,"stage_label_before":"Stage3-Yellow","raw_component_scores_after":{"contract_score":5,"backlog_visibility_score":6,"margin_bridge_score":8,"revision_score":6,"relative_strength_score":6,"customer_quality_score":8,"policy_or_regulatory_score":2,"valuation_repricing_score":5,"execution_risk_score":3,"legal_or_contract_risk_score":1,"dilution_cb_risk_score":0,"accounting_trust_risk_score":1,"capacity_or_shipment_score":9,"freight_rate_score":4},"weighted_score_after":84,"stage_label_after":"Stage3-Yellow","changed_components":["margin_bridge_score","+capacity_or_shipment_score"],"component_delta_explanation":"C29 shadow profile separates volume/reopening evidence from margin closure; LCC volume-only cases are capped below Green/Yellow promotion unless revision and unit-cost/fuel-FX pass.","MFE_90D_pct":54.1,"MAE_90D_pct":-3.28,"score_return_alignment_label":"structural_success_moderate_MFE_clean_MAE","current_profile_verdict":"current_profile_correct"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"R9L12_C29_JEJUAIR_20230118_REOPENING_VOLUME_FALSE_POSITIVE","trigger_id":"TR_R9L12_C29_03_089590_Stage2_Actionable","symbol":"089590","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE","raw_component_scores_before":{"contract_score":1,"backlog_visibility_score":2,"margin_bridge_score":2,"revision_score":2,"relative_strength_score":5,"customer_quality_score":3,"policy_or_regulatory_score":4,"valuation_repricing_score":5,"execution_risk_score":7,"legal_or_contract_risk_score":2,"dilution_cb_risk_score":3,"accounting_trust_risk_score":1,"capacity_or_shipment_score":8,"fuel_fx_cost_risk_score":8},"weighted_score_before":76,"stage_label_before":"Stage3-Yellow","raw_component_scores_after":{"contract_score":1,"backlog_visibility_score":2,"margin_bridge_score":1,"revision_score":2,"relative_strength_score":5,"customer_quality_score":3,"policy_or_regulatory_score":4,"valuation_repricing_score":5,"execution_risk_score":8,"legal_or_contract_risk_score":2,"dilution_cb_risk_score":3,"accounting_trust_risk_score":1,"capacity_or_shipment_score":8,"fuel_fx_cost_risk_score":8},"weighted_score_after":68,"stage_label_after":"Stage2-Actionable","changed_components":["margin_bridge_score_cap","execution_risk_score"],"component_delta_explanation":"C29 shadow profile separates volume/reopening evidence from margin closure; LCC volume-only cases are capped below Green/Yellow promotion unless revision and unit-cost/fuel-FX pass.","MFE_90D_pct":5.93,"MAE_90D_pct":-22.26,"score_return_alignment_label":"failed_rerating_volume_without_margin","current_profile_verdict":"current_profile_false_positive"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"R9L12_C29_JINAIR_20230118_REOPENING_MARGIN_DELAY","trigger_id":"TR_R9L12_C29_04_272450_Stage2_Actionable","symbol":"272450","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE","raw_component_scores_before":{"contract_score":1,"backlog_visibility_score":2,"margin_bridge_score":2,"revision_score":2,"relative_strength_score":6,"customer_quality_score":3,"policy_or_regulatory_score":4,"valuation_repricing_score":5,"execution_risk_score":7,"legal_or_contract_risk_score":1,"dilution_cb_risk_score":2,"accounting_trust_risk_score":1,"capacity_or_shipment_score":8,"fuel_fx_cost_risk_score":7},"weighted_score_before":75,"stage_label_before":"Stage3-Yellow","raw_component_scores_after":{"contract_score":1,"backlog_visibility_score":2,"margin_bridge_score":1,"revision_score":2,"relative_strength_score":6,"customer_quality_score":3,"policy_or_regulatory_score":4,"valuation_repricing_score":5,"execution_risk_score":8,"legal_or_contract_risk_score":1,"dilution_cb_risk_score":2,"accounting_trust_risk_score":1,"capacity_or_shipment_score":8,"fuel_fx_cost_risk_score":7},"weighted_score_after":67,"stage_label_after":"Stage2-Actionable","changed_components":["margin_bridge_score_cap","execution_risk_score"],"component_delta_explanation":"C29 shadow profile separates volume/reopening evidence from margin closure; LCC volume-only cases are capped below Green/Yellow promotion unless revision and unit-cost/fuel-FX pass.","MFE_90D_pct":1.1,"MAE_90D_pct":-19.17,"score_return_alignment_label":"failed_rerating_reopening_volume_not_enough","current_profile_verdict":"current_profile_false_positive"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"R9L12_C29_TWAY_20230314_VOLUME_ROUNDTRIP","trigger_id":"TR_R9L12_C29_05_091810_Stage2_Actionable","symbol":"091810","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE","raw_component_scores_before":{"contract_score":1,"backlog_visibility_score":2,"margin_bridge_score":3,"revision_score":3,"relative_strength_score":7,"customer_quality_score":3,"policy_or_regulatory_score":4,"valuation_repricing_score":6,"execution_risk_score":7,"legal_or_contract_risk_score":1,"dilution_cb_risk_score":5,"accounting_trust_risk_score":1,"capacity_or_shipment_score":8,"fuel_fx_cost_risk_score":7},"weighted_score_before":77,"stage_label_before":"Stage3-Yellow","raw_component_scores_after":{"contract_score":1,"backlog_visibility_score":2,"margin_bridge_score":2,"revision_score":3,"relative_strength_score":7,"customer_quality_score":3,"policy_or_regulatory_score":4,"valuation_repricing_score":6,"execution_risk_score":8,"legal_or_contract_risk_score":1,"dilution_cb_risk_score":5,"accounting_trust_risk_score":1,"capacity_or_shipment_score":8,"fuel_fx_cost_risk_score":7},"weighted_score_after":69,"stage_label_after":"Stage2-Actionable","changed_components":["margin_bridge_score_cap","execution_risk_score"],"component_delta_explanation":"C29 shadow profile separates volume/reopening evidence from margin closure; LCC volume-only cases are capped below Green/Yellow promotion unless revision and unit-cost/fuel-FX pass.","MFE_90D_pct":27.95,"MAE_90D_pct":-3.03,"score_return_alignment_label":"high_MFE_but_roundtrip_counterexample","current_profile_verdict":"current_profile_false_positive"}
```

### 25.5 shadow_weight rows

See CSV block in section 24.

### 25.6 residual_contribution row

```jsonl
{"row_type":"residual_contribution","round":"R9","loop":"12","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE","new_independent_case_count":5,"reused_case_count":0,"new_symbol_count":5,"same_archetype_new_symbol_count":5,"same_archetype_new_trigger_family_count":4,"new_canonical_archetype_count":1,"new_trigger_family_count":4,"positive_case_count":2,"counterexample_count":3,"current_profile_error_count":3,"tested_existing_calibrated_axes":["stage2_actionable_evidence_bonus","stage3_yellow_total_min","stage3_green_total_min","stage3_green_revision_min","price_only_blowoff_blocks_positive_stage","full_4b_requires_non_price_evidence"],"residual_error_types_found":["volume_recovery_without_margin_false_positive","price_only_local_4B_too_early","LCC_high_MAE_roundtrip"],"loop_contribution_label":"canonical_archetype_rule_candidate","do_not_propose_new_weight_delta":false}
```

### 25.7 narrative_only rows

```jsonl
{"row_type":"narrative_only","case_id":"NONE","symbol":"000000","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE","reason":"all selected representative triggers were calibration_usable","price_source":"Songdaiki/stock-web","usage":"not_weight_calibration"}
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

next_round: R10_C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK

Rationale: after C29 transport-volume operating leverage, the next undercovered large-sector/trigger-family block should stress-test balance-sheet/PF-break counterexamples where volume or backlog evidence is invalidated by financing structure.

## 28. Source Notes

- Stock-Web manifest: `atlas/manifest.json`, generated at 2026-05-21T16:28:39Z, max_date 2026-02-20.
- Stock-Web schema: `atlas/schema.json`, MFE/MAE definitions and calibration usability rules.
- Symbol profiles checked: 011200, 086280, 089590, 091810, 272450.
- Price shards checked: 011/011200/2020.csv, 011/011200/2021.csv, 086/086280/2020.csv, 086/086280/2021.csv, 089/089590/2023.csv, 091/091810/2023.csv, 272/272450/2023.csv.
- External historical evidence notes in this MD are narrative support only; quantitative calibration uses stock-web OHLC rows.
- No investment recommendation is implied.
