# E2R Stock-Web Historical Calibration / Sector-Archetype Residual Research Round

## 0. Research Metadata

```yaml
research_session: post_calibrated_sector_archetype_residual_research
mode: historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12
scheduled_round: R13
scheduled_loop: 73
completed_round: R13
completed_loop: 73
next_round: R1
next_loop: 74
round_schedule_status: valid
round_sector_consistency: pass
large_sector_id: L10_POLICY_EVENT_CROSS_REDTEAM_MISC
canonical_archetype_id: R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL
fine_archetype_id: HIGH_MAE_THIN_EVIDENCE_VS_STRUCTURAL_ROUTE_GUARDRAIL
loop_objective: "4B_non_price_requirement_stress_test | 4C_thesis_break_timing_test | counterexample_mining | holdout_validation | residual_false_positive_mining | green_strictness_stress_test"
price_source: Songdaiki/stock-web
price_basis: tradable_raw
price_adjustment_status: raw_unadjusted_marcap
stock_web_manifest_max_date: 2026-02-20
stock_agent_code_access_allowed: false
stock_agent_code_patch_allowed: false
stock_agent_live_scan_allowed: false
current_stock_discovery_allowed: false
production_scoring_changed: false
shadow_weight_only: true
handoff_prompt_embedded: true
handoff_prompt_executed_now: false
```

This loop adds 0 new independent cases, 4 counterexamples, and 6 residual/profile-error observations for R13/L10_POLICY_EVENT_CROSS_REDTEAM_MISC/R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL.

R13 is a checkpoint, not a new sector round. The purpose is to ask one red-team question across already materialized R1~R12 holdout rows: **when a trigger later suffers large MAE, is the failure explained by thin evidence, price-only premium, binary event risk, or missing margin/direct-route bridge?** The answer is yes for the counterexamples and no for the structural controls. That distinction matters because high MAE itself is not a blunt axe; it is a smoke alarm. It only becomes a score guardrail when the room also contains thin evidence.

## 1. Current Calibrated Profile Assumption

```text
current_default_profile_proxy = e2r_2_1_stock_web_calibrated
previous_baseline_reference = e2r_2_0_baseline
```

Applied axes assumed active:

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

This MD does not propose a production scoring change. It stress-tests existing calibrated axes and prior sector/canonical shadow rules across a reused R13 holdout basket.

## 2. Round / Large Sector / Canonical Archetype Scope

- scheduled_round: `R13`
- scheduled_loop: `73`
- R13 sector route: `L10_POLICY_EVENT_CROSS_REDTEAM_MISC` only
- canonical scope: `R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL`
- fine_archetype_id: `HIGH_MAE_THIN_EVIDENCE_VS_STRUCTURAL_ROUTE_GUARDRAIL`
- round_sector_consistency: `pass`

R13 is intentionally not written as an L5/L6/L7/L8 sector-specific file. Source rows come from prior R1~R12 outputs, but this file's scope is the R13 high-MAE red-team checkpoint.

## 3. Previous Coverage / Duplicate Avoidance Check

Allowed research-artifact access was used only for schedule sanity and duplicate/coverage avoidance. No `src/e2r` code was opened. Local v12 artifacts show R1~R12 loop 73 coverage, and the immediately preceding local output completed `R12 / Loop 73`, so this execution resolves to `R13 / Loop 73`.

Novelty/reuse classification:

```text
same_canonical_archetype_research = not_applicable_R13_cross_checkpoint
same_symbol_same_trigger_date_research = reused_by_holdout_validation_only
new_independent_case_count = 0
reused_case_count = 8
new_symbol_count = 0
new_trigger_family_count = 0
minimum_new_independent_case_ratio = 0.00
R13_exception = holdout_validation_checkpoint
```

Because this is a reused cross-checkpoint, `do_not_propose_new_weight_delta = true`. The contribution is validation and guardrail stress, not new independent calibration evidence.

## 4. Stock-Web OHLC Input / Price Source Validation

| field | value |
| --- | --- |
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

Tradable shard columns used:

```text
d,o,h,l,c,v,a,mc,s,m
```

Schema formulas applied by the source artifacts:

```text
MFE_N_pct = (max high from entry_date through N tradable rows / entry_price - 1) * 100
MAE_N_pct = (min low from entry_date through N tradable rows / entry_price - 1) * 100
```

## 5. Historical Eligibility Gate

| symbol | profile_path | price_shard_path | entry_date | forward_window_trading_days | corporate_action_window_status | calibration_usable |
| --- | --- | --- | --- | --- | --- | --- |
| 196170 | atlas/symbol_profiles/196/196170.json | atlas/ohlcv_tradable_by_symbol_year/196/196170/2024.csv | 2024-02-23 | 180 | clean_180D_window | True |
| 003230 | atlas/symbol_profiles/003/003230.json | atlas/ohlcv_tradable_by_symbol_year/003/003230/2024.csv | 2024-05-17 | 180 | clean_180D_window | True |
| 138040 | atlas/symbol_profiles/138/138040.json | atlas/ohlcv_tradable_by_symbol_year/138/138040/2024.csv | 2024-02-08 | 180 | clean_180D_window | True |
| 112610 | atlas/symbol_profiles/112/112610.json | atlas/ohlcv_tradable_by_symbol_year/112/112610/2022.csv | 2022-07-29 | 180 | clean_180D_window_profile_candidates_outside_window | True |
| 053800 | atlas/symbol_profiles/053/053800.json | atlas/ohlcv_tradable_by_symbol_year/053/053800/2022.csv | 2022-03-23 | 180 | clean_180D_window | True |
| 247540 | atlas/symbol_profiles/247/247540.json | atlas/ohlcv_tradable_by_symbol_year/247/247540/2023.csv | 2023-12-04 | 180 | clean_180D_window | True |
| 028300 | atlas/symbol_profiles/028/028300.json | atlas/ohlcv_tradable_by_symbol_year/028/028300/2024.csv | 2024-04-22 | 180 | clean_180D_window | True |
| 006910 | atlas/symbol_profiles/006/006910.json | atlas/ohlcv_tradable_by_symbol_year/006/006910/2022.csv | 2022-03-10 | 180 | clean_180D_window | True |

All selected R13 holdout rows use prior v12 representative trigger rows with stock-web `tradable_raw` OHLC and a 180-trading-day forward window. They are reused for R13 validation and not counted as fresh independent evidence.

## 6. Canonical Archetype Compression Map

| source_round | source_large_sector_id | source_canonical_archetype_id | R13 compression bucket | mechanism |
| --- | --- | --- | --- | --- |
| R7 | L7_BIO_HEALTHCARE_MEDICAL | C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION | R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL | positive route control |
| R5 | L5_CONSUMER_BRAND_DISTRIBUTION | C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION | R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL | positive route control |
| R6 | L6_FINANCIAL_CAPITAL_RETURN_DIGITAL | C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN | R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL | positive route control |
| R12 | L10_POLICY_EVENT_CROSS_REDTEAM_MISC | C31_POLICY_SUBSIDY_LEGISLATION_EVENT | R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL | positive route control |
| R8 | L8_PLATFORM_CONTENT_SW_SECURITY | C28_SOFTWARE_SECURITY_CONTRACT_RETENTION | R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL | thin-evidence high-MAE counterexample |
| R3 | L3_BATTERY_EV_GREEN_MOBILITY | C11_BATTERY_ORDERBOOK_RERATING | R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL | thin-evidence high-MAE counterexample |
| R7 | L7_BIO_HEALTHCARE_MEDICAL | C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION | R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL | thin-evidence high-MAE counterexample |
| R1 | L1_INDUSTRIALS_INFRA_DEFENSE_GRID | C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY | R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL | thin-evidence high-MAE counterexample |

Compression rule: the source archetype remains the explanatory owner, but R13 tests whether several source-specific failures share one cross-archetype residual shape. Here the shared shape is not “high MAE is bad.” It is **high MAE after a score that leaned on price, headline, contract size, or binary anticipation without enough non-price conversion evidence.**

## 7. Case Selection Summary

| role | symbol | company | source_large_sector | source_canonical | trigger_type | entry_date | entry_price | MFE180 | MAE180 | current_profile_verdict |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| positive_control | 196170 | 알테오젠 | L7_BIO_HEALTHCARE_MEDICAL | C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION | Stage2-Actionable | 2024-02-23 | 131200 | 247.18 | -9.3 | current_profile_correct |
| positive_control | 003230 | 삼양식품 | L5_CONSUMER_BRAND_DISTRIBUTION | C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION | Stage2-Actionable | 2024-05-17 | 446500 | 85.44 | 0 | current_profile_missed_structural |
| positive_control | 138040 | 메리츠금융지주 | L6_FINANCIAL_CAPITAL_RETURN_DIGITAL | C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN | Stage2-Actionable | 2024-02-08 | 71800 | 49.3 | -2.79 | current_profile_too_late |
| positive_control | 112610 | 씨에스윈드 | L10_POLICY_EVENT_CROSS_REDTEAM_MISC | C31_POLICY_SUBSIDY_LEGISLATION_EVENT | Stage2-Actionable | 2022-07-29 | 55500 | 45.05 | -4.5 | current_profile_correct |
| counterexample | 053800 | 안랩 | L8_PLATFORM_CONTENT_SW_SECURITY | C28_SOFTWARE_SECURITY_CONTRACT_RETENTION | Stage2-WatchOnly | 2022-03-23 | 175800 | 24.29 | -66.5 | current_profile_false_positive |
| counterexample | 247540 | 에코프로비엠 | L3_BATTERY_EV_GREEN_MOBILITY | C11_BATTERY_ORDERBOOK_RERATING | Stage2-Actionable/Orderbook-Without-Margin-Guard | 2023-12-04 | 323000 | 9.6 | -53.97 | current_profile_false_positive |
| counterexample | 028300 | HLB | L7_BIO_HEALTHCARE_MEDICAL | C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION | Stage2-PreApprovalBinaryEvent | 2024-04-22 | 106300 | 7.53 | -55.79 | current_profile_false_positive |
| counterexample | 006910 | 보성파워텍 | L1_INDUSTRIALS_INFRA_DEFENSE_GRID | C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY | Stage2-Actionable | 2022-03-10 | 6840 | 32.31 | -37.94 | current_profile_false_positive |

Selection balance:

```text
positive_control_count = 4
counterexample_count = 4
calibration_usable_case_count = 8
calibration_usable_trigger_count = 8
current_profile_error_count = 6
```

## 8. Positive vs Counterexample Balance

| group | case_count | avg_MFE_90D | avg_MAE_90D | avg_MFE_180D | avg_MAE_180D | interpretation |
| --- | --- | --- | --- | --- | --- | --- |
| structural route controls | 4 | 64.09 | -4.15 | 106.74 | -4.15 | strong upside with controlled MAE; high-MAE guard must not block these |
| thin-evidence counters | 4 | 18.43 | -43.22 | 18.43 | -53.55 | some initial MFE, but drawdown dominates; promotion should be capped or routed to 4B/4C watch |
| all P0 replay rows | 8 | 41.26 | -23.69 | 62.59 | -28.85 | mixed profile: the same broad score layer needs evidence-quality separation |

## 9. Evidence Source Map

| symbol | Stage2 evidence family | Stage3 evidence family | 4B evidence family | 4C evidence family |
| --- | --- | --- | --- | --- |
| 196170 | public_event_or_disclosure,customer_or_order_quality,relative_strength,policy_or_regulatory_optionality | durable_customer_confirmation,multiple_public_sources,financial_visibility | valuation_blowoff,positioning_overheat,price_only_local_peak |  |
| 003230 | public_event_or_disclosure,customer_or_order_quality,capacity_or_volume_route,early_revision_signal | confirmed_revision,margin_bridge,financial_visibility,repeat_order_or_conversion |  |  |
| 138040 | public_event_or_disclosure,policy_or_regulatory_optionality,backlog_or_delivery_visibility | confirmed_revision,financial_visibility,multiple_public_sources,low_red_team_risk |  |  |
| 112610 | public_event_or_disclosure,policy_or_regulatory_optionality,customer_or_order_quality,relative_strength | repeat_order_or_conversion,financial_visibility,multiple_public_sources | valuation_blowoff,positioning_overheat |  |
| 053800 | relative_strength |  | price_only_local_peak,positioning_overheat | thesis_evidence_broken |
| 247540 | public_event_or_disclosure,customer_or_order_quality,backlog_or_delivery_visibility | multiple_public_sources | valuation_blowoff,positioning_overheat,margin_or_backlog_slowdown | thesis_evidence_broken |
| 028300 | public_event_or_disclosure,relative_strength,policy_or_regulatory_optionality |  | positioning_overheat,explicit_event_cap | regulatory_rejection,thesis_evidence_broken |
| 006910 | public_event_or_disclosure,policy_or_regulatory_optionality,relative_strength |  | price_only_local_peak,positioning_overheat |  |

The four counterexamples all had a visible trigger, but the trigger did not mature into a durable non-price route before the drawdown. The four positive controls had a route: partner/commercialization, export-margin/reorder, capital-return ROE/PBR, or direct policy manufacturing/order visibility.

## 10. Price Data Source Map

| symbol | company | price_shard_path | profile_path | entry_date | entry_price | peak_date | peak_price |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 196170 | 알테오젠 | atlas/ohlcv_tradable_by_symbol_year/196/196170/2024.csv | atlas/symbol_profiles/196/196170.json | 2024-02-23 | 131200 | 2024-11-11 | 455500 |
| 003230 | 삼양식품 | atlas/ohlcv_tradable_by_symbol_year/003/003230/2024.csv | atlas/symbol_profiles/003/003230.json | 2024-05-17 | 446500 | 2025-03-19 | 958000 |
| 138040 | 메리츠금융지주 | atlas/ohlcv_tradable_by_symbol_year/138/138040/2024.csv | atlas/symbol_profiles/138/138040.json | 2024-02-08 | 71800 | 2024-10-21 | 107200 |
| 112610 | 씨에스윈드 | atlas/ohlcv_tradable_by_symbol_year/112/112610/2022.csv | atlas/symbol_profiles/112/112610.json | 2022-07-29 | 55500 | 2022-11-28 | 80500 |
| 053800 | 안랩 | atlas/ohlcv_tradable_by_symbol_year/053/053800/2022.csv | atlas/symbol_profiles/053/053800.json | 2022-03-23 | 175800 | 2022-03-24 | 218500 |
| 247540 | 에코프로비엠 | atlas/ohlcv_tradable_by_symbol_year/247/247540/2023.csv | atlas/symbol_profiles/247/247540.json | 2023-12-04 | 323000 | 2023-12-04 | 354000 |
| 028300 | HLB | atlas/ohlcv_tradable_by_symbol_year/028/028300/2024.csv | atlas/symbol_profiles/028/028300.json | 2024-04-22 | 106300 | 2024-04-30 | 114300 |
| 006910 | 보성파워텍 | atlas/ohlcv_tradable_by_symbol_year/006/006910/2022.csv | atlas/symbol_profiles/006/006910.json | 2022-03-10 | 6840 | 2022-03-25 | 9050 |

## 11. Case-by-Case Trigger Grid

| trigger_id | symbol | entry_date | entry_price | MFE30 | MFE90 | MFE180 | MAE30 | MAE90 | MAE180 | peak_date | peak_price | outcome |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| TRG_R7L73_ALT_20240223_S2A | 196170 | 2024-02-23 | 131200 | 71.88 | 127.52 | 247.18 | -9.3 | -9.3 | -9.3 | 2024-11-11 | 455500 | structural_success |
| T_C20_SAMYANG_STAGE2_20240517 | 003230 | 2024-05-17 | 446500 | 60.81 | 60.81 | 85.44 | 0 | 0 | 0 | 2025-03-19 | 958000 | structural_success |
| R6L73_C21_138040_20240208_stage2_actionable_payout_program | 138040 | 2024-02-08 | 71800 | 22.98 | 22.98 | 49.3 | -2.79 | -2.79 | -2.79 | 2024-10-21 | 107200 | structural_success |
| R12L73_C31_112610_T1_STAGE2_IRA_WIND_TOWER_VISIBILITY | 112610 | 2022-07-29 | 55500 | 27.93 | 45.05 | 45.05 | -4.5 | -4.5 | -4.5 | 2022-11-28 | 80500 | policy_direct_path_structural_success |
| R8L73_C28_053800_T1_STAGE2_PRICE_ONLY_POLITICAL_SECURITY_THEME | 053800 | 2022-03-23 | 175800 | 24.29 | 24.29 | 24.29 | -46.59 | -53.92 | -66.5 | 2022-03-24 | 218500 | price_only_theme_high_MAE_counterexample |
| TRG_247540_20231204_FAILED_RERATING | 247540 | 2023-12-04 | 323000 | 9.6 | 9.6 | 9.6 | -13 | -34.67 | -53.97 | 2023-12-04 | 354000 | contract_size_false_positive_without_margin_bridge |
| TRG_R7L73_HLB_20240422_PREPDUFA | 028300 | 2024-04-22 | 106300 | 7.53 | 7.53 | 7.53 | -55.79 | -55.79 | -55.79 | 2024-04-30 | 114300 | false_positive_green |
| R1L73_T006910_20220310_STAGE2A_HOLDOUT | 006910 | 2022-03-10 | 6840 | 32.31 | 32.31 | 32.31 | -6.87 | -28.51 | -37.94 | 2022-03-25 | 9050 | policy_only_false_positive_holdout |

## 12. Trigger-Level OHLC Backtest Tables

### Representative holdout trigger backtest

| symbol | entry | MFE_30D | MAE_30D | MFE_90D | MAE_90D | MFE_180D | MAE_180D | below_entry_30D | below_entry_90D | current_verdict |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 196170 | 2024-02-23 @ 131200 | 71.88 | -9.3 | 127.52 | -9.3 | 247.18 | -9.3 | True | True | current_profile_correct |
| 003230 | 2024-05-17 @ 446500 | 60.81 | 0 | 60.81 | 0 | 85.44 | 0 | False | False | current_profile_missed_structural |
| 138040 | 2024-02-08 @ 71800 | 22.98 | -2.79 | 22.98 | -2.79 | 49.3 | -2.79 | True | True | current_profile_too_late |
| 112610 | 2022-07-29 @ 55500 | 27.93 | -4.5 | 45.05 | -4.5 | 45.05 | -4.5 | True | True | current_profile_correct |
| 053800 | 2022-03-23 @ 175800 | 24.29 | -46.59 | 24.29 | -53.92 | 24.29 | -66.5 | True | True | current_profile_false_positive |
| 247540 | 2023-12-04 @ 323000 | 9.6 | -13 | 9.6 | -34.67 | 9.6 | -53.97 | True | True | current_profile_false_positive |
| 028300 | 2024-04-22 @ 106300 | 7.53 | -55.79 | 7.53 | -55.79 | 7.53 | -55.79 | True | True | current_profile_false_positive |
| 006910 | 2022-03-10 @ 6840 | 32.31 | -6.87 | 32.31 | -28.51 | 32.31 | -37.94 | True | True | current_profile_false_positive |

### Aggregate diagnostic

The red-team split is sharp:

```text
avg_positive_MFE_180D = 106.74%
avg_positive_MAE_180D = -4.15%
avg_counterexample_MFE_180D = 18.43%
avg_counterexample_MAE_180D = -53.55%
```

High MAE is therefore not a universal kill-switch. It is a metal detector: it becomes useful when it rings exactly where the evidence is thin.

## 13. Current Calibrated Profile Stress Test

| question | answer |
| --- | --- |
| 1. How would current profile judge these cases? | P0/source profiles correctly kept two positives, but missed/timed late two structural positives and over-accepted four high-MAE counterexamples. |
| 2. Did that match MFE/MAE? | It matched 196170 and 112610, was too late for 003230/138040, and false-positive for 053800/247540/028300/006910. |
| 3. Was Stage2 bonus too high? | Too high only when Stage2 rested on price/headline/binary anticipation without a route. Too low or late for route-backed positives. |
| 4. Was Yellow 75 too high/low? | Yellow remains acceptable if evidence quality is clean. It is too easy for theme-only and pre-decision binary triggers. |
| 5. Was Green 87/revision 55 too high/low? | Kept. The error is not global Green strictness; it is evidence qualification before promotion. |
| 6. Was price-only blowoff guard appropriate? | Yes; R13 strengthens it. AhnLab and Bosung show price-only/event-premium peaks near the full observed peak but bad MAE. |
| 7. Was full 4B non-price requirement appropriate? | Yes; EcoProBM shows non-price margin/slowdown evidence makes 4B/4C useful, while price-only alone should remain watch-only. |
| 8. Was hard 4C routing too late or too aggressive? | It was useful for HLB/EcoProBM after thesis break. For price-only theme cases, 4C should not pretend to be fundamental; the better fix is blocking promotion. |

Current profile verdict distribution:

```text
current_profile_correct = 2
current_profile_false_positive = 4
current_profile_missed_or_too_late = 2
current_profile_error_count = 6
```

## 14. Stage2 / Yellow / Green Comparison

| symbol | source trigger | source stage tendency | green_lateness_ratio | R13 verdict |
| --- | --- | --- | --- | --- |
| 196170 | Stage2-Actionable | Stage3-Yellow | 0.42 | keep as structural control |
| 003230 | Stage2-Actionable | Stage3-Yellow | 0.86 | keep as structural control |
| 138040 | Stage2-Actionable | Stage3-Yellow | 0.31 | keep as structural control |
| 112610 | Stage2-Actionable | Stage3-Yellow | 0.43 | keep as structural control |
| 053800 | Stage2-WatchOnly | Stage3-Yellow | null | cap or route to watch/4C before Green |
| 247540 | Stage2-Actionable/Orderbook-Without-Margin-Guard | Stage3-Green-false-positive-risk | not_applicable | cap or route to watch/4C before Green |
| 028300 | Stage2-PreApprovalBinaryEvent | Stage3-Yellow | null | cap or route to watch/4C before Green |
| 006910 | Stage2-Actionable | Stage2-Actionable | not_applicable | cap or route to watch/4C before Green |

The R13 conclusion is not “make Green easier” or “make Stage2 impossible.” It is to require the bridge that connects the headline to earnings. Without that bridge, a trigger is a flare on a dark road: bright, visible, and gone.

## 15. 4B Local vs Full-window Timing Audit

| symbol | 4B evidence type | local proximity | full-window proximity | timing verdict |
| --- | --- | --- | --- | --- |
| 196170 | price_only,valuation_blowoff,positioning_overheat | 0.97 | 0.97 | price_only_local_4B_too_early |
| 003230 |  | null | null | None |
| 138040 |  | null | null | not_applicable_for_representative_entry |
| 112610 | valuation_blowoff,positioning_overheat | 0.93 | 0.93 | good_full_window_4B_timing |
| 053800 | price_only,positioning_overheat,control_premium_or_event_premium | 1 | 1 | price_only_theme_full_window_peak_not_positive_stage |
| 247540 | valuation_blowoff,positioning_overheat,margin_or_backlog_slowdown | 0.98 | 0.98 | good_full_window_4B_timing_with_non_price_margin_guard |
| 028300 |  | null | null | None |
| 006910 | price_only,positioning_overheat | null | null | price_only_blowoff_should_not_promote_stage3 |

The split matters. In structural positives, 4B can be an overlay near a true cycle peak. In event/theme counters, price-only 4B often arrives right at the visible peak, but it is not a positive-stage signal and should not rescue an earlier bad promotion.

## 16. 4C Protection Audit

| symbol | 4C label | outcome | drawdown_after_peak_pct |
| --- | --- | --- | --- |
| 196170 | None | structural_success | -38.75 |
| 003230 | thesis_break_watch_only | structural_success | -18.68 |
| 138040 | not_applicable | structural_success | -6.16 |
| 112610 | thesis_break_watch_only | policy_direct_path_structural_success | -23.23 |
| 053800 | false_break_price_theme_only_not_fundamental_4C | price_only_theme_high_MAE_counterexample | -73.04 |
| 247540 | hard_4c_success_after_margin_bridge_break | contract_size_false_positive_without_margin_bridge | -58.0 |
| 028300 | hard_4c_success | false_positive_green | -58.88 |
| 006910 | false_break | policy_only_false_positive_holdout | -53.09 |

HLB and EcoProBM show hard 4C utility when thesis evidence breaks. AhnLab and Bosung show a different pathology: the original evidence never deserved fundamental promotion, so 4C is less a protection tool than a reminder that the Stage2/Yellow gate should have capped the row earlier.

## 17. Sector-Specific Rule Candidate

```text
sector_specific_rule_candidate = false
reason = R13 is cross-archetype redteam, not a new sector round.
```

No L5/L6/L7/L8 sector-specific rule is proposed from this R13 file. Source sector rules remain in their original sector artifacts.

## 18. Canonical-Archetype Rule Candidate

```text
canonical_archetype_rule_candidate = false
new_axis_proposed = null
```

R13 does not create a new production or canonical rule. It strengthens a shared interpretation for existing shadow rules:

```text
high_MAE_guardrail should be conditional, not blunt:
- thin non-price evidence + high MAE => demotion/watch/4C path,
- route-backed structural evidence + temporary MAE => do not block,
- price-only full-window peak => never a positive-stage evidence source,
- binary-event anticipation => hold below Green until decision/conversion.
```

## 19. Before / After Backtest Comparison

| profile | profile_id | hypothesis | changed_axes | eligible_trigger_count | selected_entry_trigger_per_case | avg_MFE_90D | avg_MAE_90D | avg_MFE_180D | avg_MAE_180D | false_positive_rate | missed_structural_count | late_green_count | avg_green_lateness | avg_4B_local | avg_4B_full | score_return_alignment_verdict |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| P0 | e2r_2_1_stock_web_calibrated_proxy | current profile as replayed across selected source artifacts | none | 8 | keeps all historical source decisions | 41.26 | -23.69 | 62.59 | -28.85 | 50% false-positive block need + 25% too-late positives | 0 | 2 | 0.51 | 0.87 | 0.89 | mixed: high-MFE successes coexist with high-MAE theme/binary failures |
| P0b | e2r_2_0_baseline_reference | rollback reference; no v12 guard assumption | older thresholds / weaker blowoff routing | 8 | would keep or delay most decisions | 41.26 | -23.69 | 62.59 | -28.85 | same or worse | 0 | 2 | 0.51 | 0.87 | 0.89 | inferior because price-only/binary failures stay too promotable |
| P1 | cross_archetype_high_MAE_guard_profile | thin-evidence high-MAE guardrail | cap promotion when no route + high drawdown signature | 8 | keeps positives; demotes four counters to watch/4C | 64.09 | -4.15 | 106.74 | -4.15 | 0% inside selected holdout | 0 | 1 | 0.51 | 0.91 | 0.94 | best MAE control; holdout only |
| P2 | archetype_specific_existing_guards_kept | no new canonical profile; preserve source-specific shadow rules | C04/C11/C23/C28/C31 source guards kept | 8 | use each source archetype rule, no global delta | 64.09 | -4.15 | 106.74 | -4.15 | 0% if source guards are active | 0 | 1 | 0.51 | 0.91 | 0.94 | supports keeping existing source-specific guards rather than one crude global rule |
| P3 | counterexample_guard_profile | 4B/4C protection overlay | non-price 4B/4C required; price-only not positive | 8 | counters remain watch/4C; positives not auto-blocked | 64.09 | -4.15 | 106.74 | -4.15 | 0% on selected counters | 0 | 1 | 0.51 | 0.91 | 0.94 | redteam passed; no production delta proposed |

## 20. Score-Return Alignment Matrix

| symbol | score_before | stage_before | score_after | stage_after | MFE_180D | MAE_180D | alignment |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 196170 | 86.0 | Stage3-Yellow | 89.0 | Stage3-Green | 247.18 | -9.3 | positive_control_kept |
| 003230 | 84 | Stage3-Yellow | 90 | Stage3-Green | 85.44 | 0 | positive_control_kept |
| 138040 | 81 | Stage3-Yellow | 88 | Stage3-Green | 49.3 | -2.79 | positive_control_kept |
| 112610 | 82.0 | Stage3-Yellow | 86.0 | Stage3-Yellow_near_green | 45.05 | -4.5 | positive_control_kept |
| 053800 | 79 | Stage3-Yellow | 56 | Stage2-Watch | 24.29 | -66.5 | counterexample_guardrail_needed |
| 247540 | 83 | Stage3-Green-false-positive-risk | 70 | Stage4B/4C-watch-positive-blocked | 9.6 | -53.97 | counterexample_guardrail_needed |
| 028300 | 76.0 | Stage3-Yellow | 62.0 | Stage2-Watch_until_decision_or_4C_after_CRL | 7.53 | -55.79 | counterexample_guardrail_needed |
| 006910 | 73 | Stage2-Actionable | 55 | Stage2-Watch | 32.31 | -37.94 | counterexample_guardrail_needed |

Mechanism summary: a score is a door hinge. The same door can open smoothly when it is bolted to revenue, margin, customer quality, or regulatory conversion; it rips out of the frame when it is attached only to price heat.

## 21. Coverage Matrix

| large_sector_id | canonical_archetype_id | fine_archetype_id | positive_case_count | counterexample_count | 4B_case_count | 4C_case_count | new_independent_case_count | reused_case_count | calibration_usable_trigger_count | representative_trigger_count | current_profile_error_count | sector_rule_candidate | canonical_rule_candidate | coverage_gap_after_this_loop |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| L10_POLICY_EVENT_CROSS_REDTEAM_MISC | R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL | HIGH_MAE_THIN_EVIDENCE_VS_STRUCTURAL_ROUTE_GUARDRAIL | 4 | 4 | 5 | 3 | 0 | 8 | 8 | 8 | 6 | False | False | R13 checkpoint: use as guardrail validation only; next gap is multi-loop confirmation with fresh holdout rows |

## 22. Residual Contribution Summary

```yaml
new_independent_case_count: 0
reused_case_count: 8
reused_case_ids: ['R7L73_C23_ALT_196170_20240223', 'C20_POS_SAMYANG_20240517', 'R6L73_C21_138040_MERITZ_20240208', 'R12L73_C31_POS_112610_IRA_WIND_TOWER', 'R8L73_C28_053800_AHNLAB_POLITICAL_SECURITY_THEME', 'R3L73_C11_247540_20231204_ORDERBOOK_COUNTER', 'R7L73_C23_HLB_028300_20240422', 'R1L73_C04_006910_BOSUNG_20220310_POLICY_ONLY_HOLDOUT']
new_symbol_count: 0
new_canonical_archetype_count: 0
new_fine_archetype_count: 1
new_trigger_family_count: 0
tested_existing_calibrated_axes:
  - price_only_blowoff_blocks_positive_stage
  - full_4b_requires_non_price_evidence
  - hard_4c_thesis_break_routes_to_4c
  - stage3_green_revision_min
  - stage3_yellow_total_min
residual_error_types_found:
  - cross_archetype_high_MAE_false_positive
  - thin_non_price_evidence_with_large_drawdown
  - binary_event_predecision_green_false_positive
  - price_only_event_premium_full_window_peak
  - missed_structural_positive_control
new_axis_proposed: null
existing_axis_strengthened:
  - price_only_blowoff_blocks_positive_stage
  - full_4b_requires_non_price_evidence
  - hard_4c_thesis_break_routes_to_4c
existing_axis_weakened: null
existing_axis_kept:
  - stage2_actionable_evidence_bonus
  - stage3_yellow_total_min
  - stage3_green_total_min
  - stage3_green_revision_min
  - stage3_cross_evidence_green_buffer
sector_specific_rule_candidate: false
canonical_archetype_rule_candidate: false
no_new_signal_reason: R13 holdout validation uses reused prior v12 rows; no fresh calibration weight delta.
loop_contribution_label: holdout_validation_passed
do_not_propose_new_weight_delta: true
```

## 23. Validation Scope / Non-Validation Scope

Validation scope:

```text
- historical OHLC rows only from Songdaiki/stock-web,
- prior v12 research artifact trigger rows only,
- R13 high-MAE guardrail stress test,
- no current/live discovery,
- no production scoring update,
- no stock_agent code inspection.
```

Non-validation scope:

```text
- no investment recommendation,
- no live watchlist,
- no broker/API/autotrading,
- no claim that this single R13 file alone justifies a global scoring change,
- no new sector-specific positive/counterexample discovery.
```

## 24. Shadow Weight Calibration

```csv
row_type,axis,scope,large_sector_id,canonical_archetype_id,baseline_value,tested_value,delta,reason,backtest_effect,trigger_ids,calibration_usable_count,new_independent_case_count,counterexample_count,confidence,proposal_type,notes
shadow_weight,R13_high_MAE_thin_evidence_guardrail,cross_archetype_redteam_holdout,L10_POLICY_EVENT_CROSS_REDTEAM_MISC,R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL,0,0,0,"High MAE alone is not a universal demotion; it becomes a guardrail when paired with thin non-price evidence, binary-event failure, price-only premium, or missing margin/direct-route bridge","Holdout separates four positives avg_MFE180=106.74/avg_MAE180=-4.15 from four counters avg_MFE180=18.43/avg_MAE180=-53.55; no production delta proposed","TRG_R7L73_ALT_20240223_S2A|T_C20_SAMYANG_STAGE2_20240517|R6L73_C21_138040_20240208_stage2_actionable_payout_program|R12L73_C31_112610_T1_STAGE2_IRA_WIND_TOWER_VISIBILITY|R8L73_C28_053800_T1_STAGE2_PRICE_ONLY_POLITICAL_SECURITY_THEME|TRG_247540_20231204_FAILED_RERATING|TRG_R7L73_HLB_20240422_PREPDUFA|R1L73_T006910_20220310_STAGE2A_HOLDOUT",8,0,4,medium,redteam_checkpoint_only,"not production; reused prior v12 rows for R13 checkpoint"
```

## 25. Machine-Readable Rows

```jsonl
{"row_type": "price_source_validation", "source": "Songdaiki/stock-web", "source_url": "https://github.com/Songdaiki/stock-web", "manifest_path": "atlas/manifest.json", "schema_path": "atlas/schema.json", "universe_path": "atlas/universe/all_symbols.csv", "manifest_max_date": "2026-02-20", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "raw_shard_root": "atlas/ohlcv_raw_by_symbol_year", "validation_status": "usable_for_historical_calibration"}
{"row_type": "case", "case_id": "R13L73_HMAE_POS_196170", "source_case_id": "R7L73_C23_ALT_196170_20240223", "source_trigger_id": "TRG_R7L73_ALT_20240223_S2A", "symbol": "196170", "company_name": "알테오젠", "round": "R13", "loop": "73", "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL", "fine_archetype_id": "HIGH_MAE_THIN_EVIDENCE_VS_STRUCTURAL_ROUTE_GUARDRAIL", "source_round": "R7", "source_large_sector_id": "L7_BIO_HEALTHCARE_MEDICAL", "source_canonical_archetype_id": "C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION", "case_type": "structural_control_positive", "positive_or_counterexample": "positive", "best_trigger": "Stage2-Actionable", "calibration_usable": true, "is_new_independent_case": false, "reuse_reason": "R13 cross-archetype holdout validation using prior v12 representative trigger; not a new sector-specific sample.", "independent_evidence_weight": 0.25, "do_not_count_as_new_case": false, "score_price_alignment": "aligned_positive_control", "current_profile_verdict": "current_profile_correct", "price_source": "Songdaiki/stock-web", "notes": "R13 validates whether high MAE is explained by thin evidence, binary-event failure, price-only premium, or missing margin/direct-route bridge."}
{"row_type": "case", "case_id": "R13L73_HMAE_POS_003230", "source_case_id": "C20_POS_SAMYANG_20240517", "source_trigger_id": "T_C20_SAMYANG_STAGE2_20240517", "symbol": "003230", "company_name": "삼양식품", "round": "R13", "loop": "73", "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL", "fine_archetype_id": "HIGH_MAE_THIN_EVIDENCE_VS_STRUCTURAL_ROUTE_GUARDRAIL", "source_round": "R5", "source_large_sector_id": "L5_CONSUMER_BRAND_DISTRIBUTION", "source_canonical_archetype_id": "C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION", "case_type": "structural_control_positive", "positive_or_counterexample": "positive", "best_trigger": "Stage2-Actionable", "calibration_usable": true, "is_new_independent_case": false, "reuse_reason": "R13 cross-archetype holdout validation using prior v12 representative trigger; not a new sector-specific sample.", "independent_evidence_weight": 0.25, "do_not_count_as_new_case": false, "score_price_alignment": "aligned_positive_control", "current_profile_verdict": "current_profile_missed_structural", "price_source": "Songdaiki/stock-web", "notes": "R13 validates whether high MAE is explained by thin evidence, binary-event failure, price-only premium, or missing margin/direct-route bridge."}
{"row_type": "case", "case_id": "R13L73_HMAE_POS_138040", "source_case_id": "R6L73_C21_138040_MERITZ_20240208", "source_trigger_id": "R6L73_C21_138040_20240208_stage2_actionable_payout_program", "symbol": "138040", "company_name": "메리츠금융지주", "round": "R13", "loop": "73", "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL", "fine_archetype_id": "HIGH_MAE_THIN_EVIDENCE_VS_STRUCTURAL_ROUTE_GUARDRAIL", "source_round": "R6", "source_large_sector_id": "L6_FINANCIAL_CAPITAL_RETURN_DIGITAL", "source_canonical_archetype_id": "C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN", "case_type": "structural_control_positive", "positive_or_counterexample": "positive", "best_trigger": "Stage2-Actionable", "calibration_usable": true, "is_new_independent_case": false, "reuse_reason": "R13 cross-archetype holdout validation using prior v12 representative trigger; not a new sector-specific sample.", "independent_evidence_weight": 0.25, "do_not_count_as_new_case": false, "score_price_alignment": "aligned_positive_control", "current_profile_verdict": "current_profile_too_late", "price_source": "Songdaiki/stock-web", "notes": "R13 validates whether high MAE is explained by thin evidence, binary-event failure, price-only premium, or missing margin/direct-route bridge."}
{"row_type": "case", "case_id": "R13L73_HMAE_POS_112610", "source_case_id": "R12L73_C31_POS_112610_IRA_WIND_TOWER", "source_trigger_id": "R12L73_C31_112610_T1_STAGE2_IRA_WIND_TOWER_VISIBILITY", "symbol": "112610", "company_name": "씨에스윈드", "round": "R13", "loop": "73", "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL", "fine_archetype_id": "HIGH_MAE_THIN_EVIDENCE_VS_STRUCTURAL_ROUTE_GUARDRAIL", "source_round": "R12", "source_large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "source_canonical_archetype_id": "C31_POLICY_SUBSIDY_LEGISLATION_EVENT", "case_type": "structural_control_positive", "positive_or_counterexample": "positive", "best_trigger": "Stage2-Actionable", "calibration_usable": true, "is_new_independent_case": false, "reuse_reason": "R13 cross-archetype holdout validation using prior v12 representative trigger; not a new sector-specific sample.", "independent_evidence_weight": 0.25, "do_not_count_as_new_case": false, "score_price_alignment": "aligned_positive_control", "current_profile_verdict": "current_profile_correct", "price_source": "Songdaiki/stock-web", "notes": "R13 validates whether high MAE is explained by thin evidence, binary-event failure, price-only premium, or missing margin/direct-route bridge."}
{"row_type": "case", "case_id": "R13L73_HMAE_CEX_053800", "source_case_id": "R8L73_C28_053800_AHNLAB_POLITICAL_SECURITY_THEME", "source_trigger_id": "R8L73_C28_053800_T1_STAGE2_PRICE_ONLY_POLITICAL_SECURITY_THEME", "symbol": "053800", "company_name": "안랩", "round": "R13", "loop": "73", "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL", "fine_archetype_id": "HIGH_MAE_THIN_EVIDENCE_VS_STRUCTURAL_ROUTE_GUARDRAIL", "source_round": "R8", "source_large_sector_id": "L8_PLATFORM_CONTENT_SW_SECURITY", "source_canonical_archetype_id": "C28_SOFTWARE_SECURITY_CONTRACT_RETENTION", "case_type": "high_mae_counterexample", "positive_or_counterexample": "counterexample", "best_trigger": "Stage2-WatchOnly", "calibration_usable": true, "is_new_independent_case": false, "reuse_reason": "R13 cross-archetype holdout validation using prior v12 representative trigger; not a new sector-specific sample.", "independent_evidence_weight": 0.25, "do_not_count_as_new_case": false, "score_price_alignment": "high_mae_guardrail_counterexample", "current_profile_verdict": "current_profile_false_positive", "price_source": "Songdaiki/stock-web", "notes": "R13 validates whether high MAE is explained by thin evidence, binary-event failure, price-only premium, or missing margin/direct-route bridge."}
{"row_type": "case", "case_id": "R13L73_HMAE_CEX_247540", "source_case_id": "R3L73_C11_247540_20231204_ORDERBOOK_COUNTER", "source_trigger_id": "TRG_247540_20231204_FAILED_RERATING", "symbol": "247540", "company_name": "에코프로비엠", "round": "R13", "loop": "73", "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL", "fine_archetype_id": "HIGH_MAE_THIN_EVIDENCE_VS_STRUCTURAL_ROUTE_GUARDRAIL", "source_round": "R3", "source_large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "source_canonical_archetype_id": "C11_BATTERY_ORDERBOOK_RERATING", "case_type": "high_mae_counterexample", "positive_or_counterexample": "counterexample", "best_trigger": "Stage2-Actionable/Orderbook-Without-Margin-Guard", "calibration_usable": true, "is_new_independent_case": false, "reuse_reason": "R13 cross-archetype holdout validation using prior v12 representative trigger; not a new sector-specific sample.", "independent_evidence_weight": 0.25, "do_not_count_as_new_case": false, "score_price_alignment": "high_mae_guardrail_counterexample", "current_profile_verdict": "current_profile_false_positive", "price_source": "Songdaiki/stock-web", "notes": "R13 validates whether high MAE is explained by thin evidence, binary-event failure, price-only premium, or missing margin/direct-route bridge."}
{"row_type": "case", "case_id": "R13L73_HMAE_CEX_028300", "source_case_id": "R7L73_C23_HLB_028300_20240422", "source_trigger_id": "TRG_R7L73_HLB_20240422_PREPDUFA", "symbol": "028300", "company_name": "HLB", "round": "R13", "loop": "73", "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL", "fine_archetype_id": "HIGH_MAE_THIN_EVIDENCE_VS_STRUCTURAL_ROUTE_GUARDRAIL", "source_round": "R7", "source_large_sector_id": "L7_BIO_HEALTHCARE_MEDICAL", "source_canonical_archetype_id": "C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION", "case_type": "high_mae_counterexample", "positive_or_counterexample": "counterexample", "best_trigger": "Stage2-PreApprovalBinaryEvent", "calibration_usable": true, "is_new_independent_case": false, "reuse_reason": "R13 cross-archetype holdout validation using prior v12 representative trigger; not a new sector-specific sample.", "independent_evidence_weight": 0.25, "do_not_count_as_new_case": false, "score_price_alignment": "high_mae_guardrail_counterexample", "current_profile_verdict": "current_profile_false_positive", "price_source": "Songdaiki/stock-web", "notes": "R13 validates whether high MAE is explained by thin evidence, binary-event failure, price-only premium, or missing margin/direct-route bridge."}
{"row_type": "case", "case_id": "R13L73_HMAE_CEX_006910", "source_case_id": "R1L73_C04_006910_BOSUNG_20220310_POLICY_ONLY_HOLDOUT", "source_trigger_id": "R1L73_T006910_20220310_STAGE2A_HOLDOUT", "symbol": "006910", "company_name": "보성파워텍", "round": "R13", "loop": "73", "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL", "fine_archetype_id": "HIGH_MAE_THIN_EVIDENCE_VS_STRUCTURAL_ROUTE_GUARDRAIL", "source_round": "R1", "source_large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "source_canonical_archetype_id": "C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY", "case_type": "high_mae_counterexample", "positive_or_counterexample": "counterexample", "best_trigger": "Stage2-Actionable", "calibration_usable": true, "is_new_independent_case": false, "reuse_reason": "R13 cross-archetype holdout validation using prior v12 representative trigger; not a new sector-specific sample.", "independent_evidence_weight": 0.25, "do_not_count_as_new_case": false, "score_price_alignment": "high_mae_guardrail_counterexample", "current_profile_verdict": "current_profile_false_positive", "price_source": "Songdaiki/stock-web", "notes": "R13 validates whether high MAE is explained by thin evidence, binary-event failure, price-only premium, or missing margin/direct-route bridge."}
{"row_type": "trigger", "trigger_id": "R13L73_HMAE_REUSED_TRG_R7L73_ALT_20240223_S2A", "case_id": "R13L73_HMAE_POS_196170", "symbol": "196170", "company_name": "알테오젠", "round": "R13", "loop": "73", "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL", "fine_archetype_id": "HIGH_MAE_THIN_EVIDENCE_VS_STRUCTURAL_ROUTE_GUARDRAIL", "sector": "bio_healthcare_medical", "primary_archetype": "regulatory_approval_to_commercialization", "loop_objective": "4B_non_price_requirement_stress_test | 4C_thesis_break_timing_test | counterexample_mining | holdout_validation | residual_false_positive_mining | green_strictness_stress_test", "trigger_type": "Stage2-Actionable", "trigger_date": "2024-02-22", "entry_date": "2024-02-23", "entry_price": 131200, "evidence_available_at_that_date": "ALT-B4/SC formulation commercialization route repricing after public partner-route licensing amendment; follow-on Merck/Keytruda SC disclosure context later reinforced route.", "evidence_source": "public company/disclosure/news flow; Reuters later confirmed Merck's SC Keytruda uses an Alteogen-developed enzyme.", "stage2_evidence_fields": ["public_event_or_disclosure", "customer_or_order_quality", "relative_strength", "policy_or_regulatory_optionality"], "stage3_evidence_fields": ["durable_customer_confirmation", "multiple_public_sources", "financial_visibility"], "stage4b_evidence_fields": ["valuation_blowoff", "positioning_overheat", "price_only_local_peak"], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/196/196170/2024.csv", "profile_path": "atlas/symbol_profiles/196/196170.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": 71.88, "MFE_90D_pct": 127.52, "MFE_180D_pct": 247.18, "MFE_1Y_pct": null, "MFE_2Y_pct": null, "MAE_30D_pct": -9.3, "MAE_90D_pct": -9.3, "MAE_180D_pct": -9.3, "MAE_1Y_pct": null, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2024-11-11", "peak_price": 455500, "drawdown_after_peak_pct": -38.75, "green_lateness_ratio": 0.425, "four_b_local_peak_proximity": 0.969, "four_b_full_window_peak_proximity": 0.969, "four_b_timing_verdict": "price_only_local_4B_too_early", "four_b_evidence_type": ["price_only", "valuation_blowoff", "positioning_overheat"], "four_c_protection_label": null, "trigger_outcome_label": "structural_success", "current_profile_verdict": "current_profile_correct", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window", "same_entry_group_id": "R13L73_HMAE_196170_2024-02-23_131200", "dedupe_for_aggregate": true, "aggregate_group_role": "representative_holdout", "is_new_independent_case": false, "reuse_reason": "R13 cross-archetype holdout validation; source OHLC/MFE/MAE row copied from prior v12 artifact and re-aggregated only for redteam guardrail review.", "independent_evidence_weight": 0.25, "do_not_count_as_new_case": false, "source_round": "R7", "source_large_sector_id": "L7_BIO_HEALTHCARE_MEDICAL", "source_canonical_archetype_id": "C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION", "source_trigger_id": "TRG_R7L73_ALT_20240223_S2A"}
{"row_type": "trigger", "trigger_id": "R13L73_HMAE_REUSED_T_C20_SAMYANG_STAGE2_20240517", "case_id": "R13L73_HMAE_POS_003230", "symbol": "003230", "company_name": "삼양식품", "round": "R13", "loop": "73", "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL", "fine_archetype_id": "HIGH_MAE_THIN_EVIDENCE_VS_STRUCTURAL_ROUTE_GUARDRAIL", "sector": "consumer_food_export", "primary_archetype": "food_export_reorder_margin_bridge", "loop_objective": "4B_non_price_requirement_stress_test | 4C_thesis_break_timing_test | counterexample_mining | holdout_validation | residual_false_positive_mining | green_strictness_stress_test", "trigger_type": "Stage2-Actionable", "trigger_date": "2024-05-16", "entry_date": "2024-05-17", "entry_price": 446500, "evidence_available_at_that_date": "export-led earnings surprise and channel reorder narrative", "evidence_source": "historical public earnings/disclosure/news category label", "stage2_evidence_fields": ["public_event_or_disclosure", "customer_or_order_quality", "capacity_or_volume_route", "early_revision_signal"], "stage3_evidence_fields": ["confirmed_revision", "margin_bridge", "financial_visibility", "repeat_order_or_conversion"], "stage4b_evidence_fields": [], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/003/003230/2024.csv", "profile_path": "atlas/symbol_profiles/003/003230.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": 60.81, "MFE_90D_pct": 60.81, "MFE_180D_pct": 85.44, "MFE_1Y_pct": 114.56, "MFE_2Y_pct": null, "MAE_30D_pct": 0.0, "MAE_90D_pct": 0.0, "MAE_180D_pct": 0.0, "MAE_1Y_pct": 0.0, "below_entry_price_flag_30D": false, "below_entry_price_flag_90D": false, "peak_date": "2025-03-19", "peak_price": 958000, "drawdown_after_peak_pct": -18.68, "green_lateness_ratio": 0.86, "four_b_local_peak_proximity": null, "four_b_full_window_peak_proximity": null, "four_b_timing_verdict": null, "four_b_evidence_type": [], "four_c_protection_label": "thesis_break_watch_only", "trigger_outcome_label": "structural_success", "current_profile_verdict": "current_profile_missed_structural", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window", "same_entry_group_id": "R13L73_HMAE_003230_2024-05-17_446500", "dedupe_for_aggregate": true, "aggregate_group_role": "representative_holdout", "is_new_independent_case": false, "reuse_reason": "R13 cross-archetype holdout validation; source OHLC/MFE/MAE row copied from prior v12 artifact and re-aggregated only for redteam guardrail review.", "independent_evidence_weight": 0.25, "do_not_count_as_new_case": false, "source_round": "R5", "source_large_sector_id": "L5_CONSUMER_BRAND_DISTRIBUTION", "source_canonical_archetype_id": "C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION", "source_trigger_id": "T_C20_SAMYANG_STAGE2_20240517"}
{"row_type": "trigger", "trigger_id": "R13L73_HMAE_REUSED_R6L73_C21_138040_20240208_stage2_actionable_payout_program", "case_id": "R13L73_HMAE_POS_138040", "symbol": "138040", "company_name": "메리츠금융지주", "round": "R13", "loop": "73", "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL", "fine_archetype_id": "HIGH_MAE_THIN_EVIDENCE_VS_STRUCTURAL_ROUTE_GUARDRAIL", "sector": "financial_capital_return_digital", "primary_archetype": "ROE/PBR capital return rerating", "loop_objective": "4B_non_price_requirement_stress_test | 4C_thesis_break_timing_test | counterexample_mining | holdout_validation | residual_false_positive_mining | green_strictness_stress_test", "trigger_type": "Stage2-Actionable", "trigger_date": "2024-02-07", "evidence_available_at_that_date": "지주 체제 전환 이후 일관된 자사주 매입·소각/총주주환원율 커뮤니케이션이 ROE·PBR 재평가 경로와 결합된 case.", "evidence_source": "historical public disclosure / earnings / market evidence map; price rows from stock-web", "stage2_evidence_fields": ["public_event_or_disclosure", "policy_or_regulatory_optionality", "backlog_or_delivery_visibility"], "stage3_evidence_fields": ["confirmed_revision", "financial_visibility", "multiple_public_sources", "low_red_team_risk"], "stage4b_evidence_fields": [], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/138/138040/2024.csv", "profile_path": "atlas/symbol_profiles/138/138040.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "entry_date": "2024-02-08", "entry_price": 71800, "MFE_30D_pct": 22.98, "MFE_90D_pct": 22.98, "MFE_180D_pct": 49.3, "MFE_1Y_pct": 49.3, "MFE_2Y_pct": null, "MAE_30D_pct": -2.79, "MAE_90D_pct": -2.79, "MAE_180D_pct": -2.79, "MAE_1Y_pct": -2.79, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2024-10-21", "peak_price": 107200, "drawdown_after_peak_pct": -6.16, "green_lateness_ratio": 0.31, "four_b_local_peak_proximity": null, "four_b_full_window_peak_proximity": null, "four_b_timing_verdict": "not_applicable_for_representative_entry", "four_b_evidence_type": [], "four_c_protection_label": "not_applicable", "trigger_outcome_label": "structural_success", "current_profile_verdict": "current_profile_too_late", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window", "same_entry_group_id": "R13L73_HMAE_138040_2024-02-08_71800", "dedupe_for_aggregate": true, "aggregate_group_role": "representative_holdout", "is_new_independent_case": false, "reuse_reason": "R13 cross-archetype holdout validation; source OHLC/MFE/MAE row copied from prior v12 artifact and re-aggregated only for redteam guardrail review.", "independent_evidence_weight": 0.25, "do_not_count_as_new_case": false, "source_round": "R6", "source_large_sector_id": "L6_FINANCIAL_CAPITAL_RETURN_DIGITAL", "source_canonical_archetype_id": "C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN", "source_trigger_id": "R6L73_C21_138040_20240208_stage2_actionable_payout_program"}
{"row_type": "trigger", "trigger_id": "R13L73_HMAE_REUSED_R12L73_C31_112610_T1_STAGE2_IRA_WIND_TOWER_VISIBILITY", "case_id": "R13L73_HMAE_POS_112610", "symbol": "112610", "company_name": "씨에스윈드", "round": "R13", "loop": "73", "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL", "fine_archetype_id": "HIGH_MAE_THIN_EVIDENCE_VS_STRUCTURAL_ROUTE_GUARDRAIL", "sector": "policy-linked wind equipment manufacturing", "primary_archetype": "direct renewable manufacturing/order route", "loop_objective": "4B_non_price_requirement_stress_test | 4C_thesis_break_timing_test | counterexample_mining | holdout_validation | residual_false_positive_mining | green_strictness_stress_test", "trigger_type": "Stage2-Actionable", "trigger_date": "2022-07-28", "evidence_available_at_that_date": "Policy package was not only a theme headline; wind-tower manufacturing exposure gave a concrete route from subsidy/renewable capex to order and margin visibility.", "evidence_source": "public_policy_event: U.S. Inflation Reduction Act Senate agreement / bill text family; company exposure classified from historical business mix, not live discovery", "stage2_evidence_fields": ["public_event_or_disclosure", "policy_or_regulatory_optionality", "customer_or_order_quality", "relative_strength"], "stage3_evidence_fields": ["repeat_order_or_conversion", "financial_visibility", "multiple_public_sources"], "stage4b_evidence_fields": ["valuation_blowoff", "positioning_overheat"], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/112/112610/2022.csv", "profile_path": "atlas/symbol_profiles/112/112610.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "entry_date": "2022-07-29", "entry_price": 55500, "MFE_30D_pct": 27.93, "MFE_90D_pct": 45.05, "MFE_180D_pct": 45.05, "MFE_1Y_pct": null, "MFE_2Y_pct": null, "MAE_30D_pct": -4.5, "MAE_90D_pct": -4.5, "MAE_180D_pct": -4.5, "MAE_1Y_pct": null, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2022-11-28", "peak_price": 80500, "drawdown_after_peak_pct": -23.23, "green_lateness_ratio": 0.43, "four_b_local_peak_proximity": 0.93, "four_b_full_window_peak_proximity": 0.93, "four_b_timing_verdict": "good_full_window_4B_timing", "four_b_evidence_type": ["valuation_blowoff", "positioning_overheat"], "four_c_protection_label": "thesis_break_watch_only", "trigger_outcome_label": "policy_direct_path_structural_success", "current_profile_verdict": "current_profile_correct", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window_profile_candidates_outside_window", "same_entry_group_id": "R13L73_HMAE_112610_2022-07-29_55500", "dedupe_for_aggregate": true, "aggregate_group_role": "representative_holdout", "is_new_independent_case": false, "reuse_reason": "R13 cross-archetype holdout validation; source OHLC/MFE/MAE row copied from prior v12 artifact and re-aggregated only for redteam guardrail review.", "independent_evidence_weight": 0.25, "do_not_count_as_new_case": false, "source_round": "R12", "source_large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "source_canonical_archetype_id": "C31_POLICY_SUBSIDY_LEGISLATION_EVENT", "source_trigger_id": "R12L73_C31_112610_T1_STAGE2_IRA_WIND_TOWER_VISIBILITY"}
{"row_type": "trigger", "trigger_id": "R13L73_HMAE_REUSED_R8L73_C28_053800_T1_STAGE2_PRICE_ONLY_POLITICAL_SECURITY_THEME", "case_id": "R13L73_HMAE_CEX_053800", "symbol": "053800", "company_name": "안랩", "round": "R13", "loop": "73", "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL", "fine_archetype_id": "HIGH_MAE_THIN_EVIDENCE_VS_STRUCTURAL_ROUTE_GUARDRAIL", "sector": "security_software", "primary_archetype": "political_event_premium_not_contract_retention", "loop_objective": "4B_non_price_requirement_stress_test | 4C_thesis_break_timing_test | counterexample_mining | holdout_validation | residual_false_positive_mining | green_strictness_stress_test", "trigger_type": "Stage2-WatchOnly", "trigger_date": "2022-03-23", "evidence_available_at_that_date": "안랩 2022년 3월 움직임은 보안 제품·계약 유지율·갱신율·수주잔고가 아니라 정치/인물 프리미엄과 price-only blowoff에 가까웠다. C28에서는 security ticker라는 이유만으로 software contract retention score를 주면 안 된다는 대표 반례다.", "evidence_source": "stock-web rows show 2022-03-23 close 175,800, 2022-03-24 high 218,500, and 2022-10-21 low 58,900; profile CA candidate is 2005 only.", "stage2_evidence_fields": ["relative_strength"], "stage3_evidence_fields": [], "stage4b_evidence_fields": ["price_only_local_peak", "positioning_overheat"], "stage4c_evidence_fields": ["thesis_evidence_broken"], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/053/053800/2022.csv", "profile_path": "atlas/symbol_profiles/053/053800.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "entry_date": "2022-03-23", "entry_price": 175800, "MFE_30D_pct": 24.29, "MFE_90D_pct": 24.29, "MFE_180D_pct": 24.29, "MFE_1Y_pct": null, "MFE_2Y_pct": null, "MAE_30D_pct": -46.59, "MAE_90D_pct": -53.92, "MAE_180D_pct": -66.5, "MAE_1Y_pct": null, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2022-03-24", "peak_price": 218500, "drawdown_after_peak_pct": -73.04, "green_lateness_ratio": null, "four_b_local_peak_proximity": 1.0, "four_b_full_window_peak_proximity": 1.0, "four_b_timing_verdict": "price_only_theme_full_window_peak_not_positive_stage", "four_b_evidence_type": ["price_only", "positioning_overheat", "control_premium_or_event_premium"], "four_c_protection_label": "false_break_price_theme_only_not_fundamental_4C", "trigger_outcome_label": "price_only_theme_high_MAE_counterexample", "current_profile_verdict": "current_profile_false_positive", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window", "same_entry_group_id": "R13L73_HMAE_053800_2022-03-23_175800", "dedupe_for_aggregate": true, "aggregate_group_role": "representative_holdout", "is_new_independent_case": false, "reuse_reason": "R13 cross-archetype holdout validation; source OHLC/MFE/MAE row copied from prior v12 artifact and re-aggregated only for redteam guardrail review.", "independent_evidence_weight": 0.25, "do_not_count_as_new_case": false, "source_round": "R8", "source_large_sector_id": "L8_PLATFORM_CONTENT_SW_SECURITY", "source_canonical_archetype_id": "C28_SOFTWARE_SECURITY_CONTRACT_RETENTION", "source_trigger_id": "R8L73_C28_053800_T1_STAGE2_PRICE_ONLY_POLITICAL_SECURITY_THEME"}
{"row_type": "trigger", "trigger_id": "R13L73_HMAE_REUSED_TRG_247540_20231204_FAILED_RERATING", "case_id": "R13L73_HMAE_CEX_247540", "symbol": "247540", "company_name": "에코프로비엠", "round": "R13", "loop": "73", "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL", "fine_archetype_id": "HIGH_MAE_THIN_EVIDENCE_VS_STRUCTURAL_ROUTE_GUARDRAIL", "sector": "battery_ev_green_mobility", "primary_archetype": "battery long-term supply orderbook rerating with margin/customer guard", "loop_objective": "4B_non_price_requirement_stress_test | 4C_thesis_break_timing_test | counterexample_mining | holdout_validation | residual_false_positive_mining | green_strictness_stress_test", "trigger_type": "Stage2-Actionable/Orderbook-Without-Margin-Guard", "trigger_date": "2023-12-01", "entry_date": "2023-12-04", "entry_price": 323000, "evidence_available_at_that_date": "Long-term supply contract/orderbook was visible, but it arrived after a prior sector blowoff and before the ASP/margin/utilization bridge repaired; the current profile can over-promote if contract size is scored without spread and demand guards.", "evidence_source": "historical disclosure/news narrative cross-checked against stock-web price rows; see Source Notes", "stage2_evidence_fields": ["public_event_or_disclosure", "customer_or_order_quality", "backlog_or_delivery_visibility"], "stage3_evidence_fields": ["multiple_public_sources"], "stage4b_evidence_fields": ["valuation_blowoff", "positioning_overheat", "margin_or_backlog_slowdown"], "stage4c_evidence_fields": ["thesis_evidence_broken"], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/247/247540/2023.csv", "profile_path": "atlas/symbol_profiles/247/247540.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": 9.6, "MFE_90D_pct": 9.6, "MFE_180D_pct": 9.6, "MFE_1Y_pct": null, "MFE_2Y_pct": null, "MAE_30D_pct": -13.0, "MAE_90D_pct": -34.67, "MAE_180D_pct": -53.97, "MAE_1Y_pct": null, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2023-12-04", "peak_price": 354000, "drawdown_after_peak_pct": -58.0, "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": 0.98, "four_b_full_window_peak_proximity": 0.98, "four_b_timing_verdict": "good_full_window_4B_timing_with_non_price_margin_guard", "four_b_evidence_type": ["valuation_blowoff", "positioning_overheat", "margin_or_backlog_slowdown"], "four_c_protection_label": "hard_4c_success_after_margin_bridge_break", "trigger_outcome_label": "contract_size_false_positive_without_margin_bridge", "current_profile_verdict": "current_profile_false_positive", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window", "same_entry_group_id": "R13L73_HMAE_247540_2023-12-04_323000", "dedupe_for_aggregate": true, "aggregate_group_role": "representative_holdout", "is_new_independent_case": false, "reuse_reason": "R13 cross-archetype holdout validation; source OHLC/MFE/MAE row copied from prior v12 artifact and re-aggregated only for redteam guardrail review.", "independent_evidence_weight": 0.25, "do_not_count_as_new_case": false, "source_round": "R3", "source_large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "source_canonical_archetype_id": "C11_BATTERY_ORDERBOOK_RERATING", "source_trigger_id": "TRG_247540_20231204_FAILED_RERATING"}
{"row_type": "trigger", "trigger_id": "R13L73_HMAE_REUSED_TRG_R7L73_HLB_20240422_PREPDUFA", "case_id": "R13L73_HMAE_CEX_028300", "symbol": "028300", "company_name": "HLB", "round": "R13", "loop": "73", "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL", "fine_archetype_id": "HIGH_MAE_THIN_EVIDENCE_VS_STRUCTURAL_ROUTE_GUARDRAIL", "sector": "bio_healthcare_medical", "primary_archetype": "regulatory_approval_to_commercialization", "loop_objective": "4B_non_price_requirement_stress_test | 4C_thesis_break_timing_test | counterexample_mining | holdout_validation | residual_false_positive_mining | green_strictness_stress_test", "trigger_type": "Stage2-PreApprovalBinaryEvent", "trigger_date": "2024-04-22", "entry_date": "2024-04-22", "entry_price": 106300, "evidence_available_at_that_date": "Pre-PDUFA/regulatory approval expectation priced before decision; FDA Complete Response Letter then triggered hard thesis-break path.", "evidence_source": "public regulatory-event/news flow around HLB/Elevar liver cancer application and May 2024 CRL; later source normalization required.", "stage2_evidence_fields": ["public_event_or_disclosure", "relative_strength", "policy_or_regulatory_optionality"], "stage3_evidence_fields": [], "stage4b_evidence_fields": ["positioning_overheat", "explicit_event_cap"], "stage4c_evidence_fields": ["regulatory_rejection", "thesis_evidence_broken"], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/028/028300/2024.csv", "profile_path": "atlas/symbol_profiles/028/028300.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": 7.53, "MFE_90D_pct": 7.53, "MFE_180D_pct": 7.53, "MFE_1Y_pct": null, "MFE_2Y_pct": null, "MAE_30D_pct": -55.79, "MAE_90D_pct": -55.79, "MAE_180D_pct": -55.79, "MAE_1Y_pct": null, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2024-04-30", "peak_price": 114300, "drawdown_after_peak_pct": -58.88, "green_lateness_ratio": null, "four_b_local_peak_proximity": null, "four_b_full_window_peak_proximity": null, "four_b_timing_verdict": null, "four_b_evidence_type": [], "four_c_protection_label": "hard_4c_success", "trigger_outcome_label": "false_positive_green", "current_profile_verdict": "current_profile_false_positive", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window", "same_entry_group_id": "R13L73_HMAE_028300_2024-04-22_106300", "dedupe_for_aggregate": true, "aggregate_group_role": "representative_holdout", "is_new_independent_case": false, "reuse_reason": "R13 cross-archetype holdout validation; source OHLC/MFE/MAE row copied from prior v12 artifact and re-aggregated only for redteam guardrail review.", "independent_evidence_weight": 0.25, "do_not_count_as_new_case": false, "source_round": "R7", "source_large_sector_id": "L7_BIO_HEALTHCARE_MEDICAL", "source_canonical_archetype_id": "C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION", "source_trigger_id": "TRG_R7L73_HLB_20240422_PREPDUFA"}
{"trigger_id": "R13L73_HMAE_REUSED_R1L73_T006910_20220310_STAGE2A_HOLDOUT", "case_id": "R13L73_HMAE_CEX_006910", "symbol": "006910", "company_name": "보성파워텍", "trigger_type": "Stage2-Actionable", "trigger_date": "2022-03-10", "entry_date": "2022-03-10", "entry_price": 6840, "evidence_available_at_that_date": "Yoon election nuclear-policy inflection headline; no company-specific contract/order/revision bridge at trigger date", "evidence_source": "prior allowed C04/C31 holdout row; stock-web 006910 profile and shard path validated", "stage2_evidence_fields": ["public_event_or_disclosure", "policy_or_regulatory_optionality", "relative_strength"], "stage3_evidence_fields": [], "stage4b_evidence_fields": ["price_only_local_peak", "positioning_overheat"], "stage4c_evidence_fields": [], "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/006/006910/2022.csv", "profile_path": "atlas/symbol_profiles/006/006910.json", "MFE_30D_pct": 32.31, "MFE_90D_pct": 32.31, "MFE_180D_pct": 32.31, "MFE_1Y_pct": 32.31, "MFE_2Y_pct": null, "MAE_30D_pct": -6.87, "MAE_90D_pct": -28.51, "MAE_180D_pct": -37.94, "MAE_1Y_pct": -53.09, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2022-03-25", "peak_price": 9050, "drawdown_after_peak_pct": -53.09, "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": null, "four_b_full_window_peak_proximity": null, "four_b_timing_verdict": "price_only_blowoff_should_not_promote_stage3", "four_b_evidence_type": ["price_only", "positioning_overheat"], "four_c_protection_label": "false_break", "trigger_outcome_label": "policy_only_false_positive_holdout", "current_profile_verdict": "current_profile_false_positive", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window", "row_type": "trigger", "round": "R13", "loop": "73", "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL", "fine_archetype_id": "HIGH_MAE_THIN_EVIDENCE_VS_STRUCTURAL_ROUTE_GUARDRAIL", "sector": "nuclear_theme_supplier", "primary_archetype": "policy-only nuclear theme without company conversion bridge", "loop_objective": "4B_non_price_requirement_stress_test | 4C_thesis_break_timing_test | counterexample_mining | holdout_validation | residual_false_positive_mining | green_strictness_stress_test", "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "same_entry_group_id": "R13L73_HMAE_006910_2022-03-10_6840", "dedupe_for_aggregate": true, "aggregate_group_role": "representative_holdout", "is_new_independent_case": false, "reuse_reason": "R13 cross-archetype holdout validation; source OHLC/MFE/MAE row copied from prior v12 artifact and re-aggregated only for redteam guardrail review.", "independent_evidence_weight": 0.25, "do_not_count_as_new_case": false, "source_round": "R1", "source_large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "source_canonical_archetype_id": "C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY", "source_trigger_id": "R1L73_T006910_20220310_STAGE2A_HOLDOUT"}
{"row_type": "score_simulation", "profile_id": "R13_cross_archetype_high_MAE_guardrail_holdout", "case_id": "R13L73_HMAE_POS_196170", "trigger_id": "R13L73_HMAE_REUSED_TRG_R7L73_ALT_20240223_S2A", "source_trigger_id": "TRG_R7L73_ALT_20240223_S2A", "symbol": "196170", "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL", "source_large_sector_id": "L7_BIO_HEALTHCARE_MEDICAL", "source_canonical_archetype_id": "C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION", "raw_component_scores_before": {"contract_score": 8, "backlog_visibility_score": 0, "margin_bridge_score": 2, "revision_score": 5, "relative_strength_score": 9, "customer_quality_score": 8, "policy_or_regulatory_score": 6, "valuation_repricing_score": 7, "execution_risk_score": 3, "legal_or_contract_risk_score": 2, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_before": 86.0, "stage_label_before": "Stage3-Yellow", "raw_component_scores_after": {"contract_score": 9, "backlog_visibility_score": 0, "margin_bridge_score": 2, "revision_score": 6, "relative_strength_score": 9, "customer_quality_score": 9, "policy_or_regulatory_score": 7, "valuation_repricing_score": 7, "execution_risk_score": 3, "legal_or_contract_risk_score": 2, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_after": 89.0, "stage_label_after": "Stage3-Green", "changed_components": ["policy_or_regulatory_score", "customer_quality_score", "revision_score", "relative_strength_score", "execution_risk_score"], "component_delta_explanation": "R13 holdout reuse: C23 route bonus upgrades identified global-partner commercialization optionality; 4B remains overlay-only near peak. Cross-guardrail interpretation: high MAE is accepted only as a risk flag; it becomes score-demotion evidence when paired with thin non-price evidence, price-only premium, binary event failure, or missing margin/direct-route bridge.", "MFE_90D_pct": 127.52, "MAE_90D_pct": -9.3, "score_return_alignment_label": "positive_control_kept", "current_profile_verdict": "current_profile_correct"}
{"row_type": "score_simulation", "profile_id": "R13_cross_archetype_high_MAE_guardrail_holdout", "case_id": "R13L73_HMAE_POS_003230", "trigger_id": "R13L73_HMAE_REUSED_T_C20_SAMYANG_STAGE2_20240517", "source_trigger_id": "T_C20_SAMYANG_STAGE2_20240517", "symbol": "003230", "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL", "source_large_sector_id": "L5_CONSUMER_BRAND_DISTRIBUTION", "source_canonical_archetype_id": "C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION", "raw_component_scores_before": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 12, "revision_score": 14, "relative_strength_score": 10, "customer_quality_score": 8, "policy_or_regulatory_score": 0, "valuation_repricing_score": 6, "execution_risk_score": 3, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0, "channel_reorder_score": 13, "inventory_overhang_score": 1}, "weighted_score_before": 84, "stage_label_before": "Stage3-Yellow", "raw_component_scores_after": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 12, "revision_score": 14, "relative_strength_score": 10, "customer_quality_score": 8, "policy_or_regulatory_score": 0, "valuation_repricing_score": 6, "execution_risk_score": 3, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0, "channel_reorder_score": 13, "inventory_overhang_score": 1}, "weighted_score_after": 90, "stage_label_after": "Stage3-Green", "changed_components": ["channel_reorder_score", "margin_bridge_score"], "component_delta_explanation": "R13 holdout reuse: C20 reorder + margin bridge bonus Cross-guardrail interpretation: high MAE is accepted only as a risk flag; it becomes score-demotion evidence when paired with thin non-price evidence, price-only premium, binary event failure, or missing margin/direct-route bridge.", "MFE_90D_pct": 60.81, "MAE_90D_pct": 0.0, "score_return_alignment_label": "positive_control_kept", "current_profile_verdict": "current_profile_missed_structural"}
{"row_type": "score_simulation", "profile_id": "R13_cross_archetype_high_MAE_guardrail_holdout", "case_id": "R13L73_HMAE_POS_138040", "trigger_id": "R13L73_HMAE_REUSED_R6L73_C21_138040_20240208_stage2_actionable_payout_program", "source_trigger_id": "R6L73_C21_138040_20240208_stage2_actionable_payout_program", "symbol": "138040", "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL", "source_large_sector_id": "L6_FINANCIAL_CAPITAL_RETURN_DIGITAL", "source_canonical_archetype_id": "C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN", "raw_component_scores_before": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 0, "revision_score": 12, "relative_strength_score": 13, "customer_quality_score": 0, "policy_or_regulatory_score": 13, "valuation_repricing_score": 15, "execution_risk_score": 2, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_before": 81, "stage_label_before": "Stage3-Yellow", "raw_component_scores_after": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 0, "revision_score": 12, "relative_strength_score": 13, "customer_quality_score": 0, "policy_or_regulatory_score": 16, "valuation_repricing_score": 18, "execution_risk_score": 1, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_after": 88, "stage_label_after": "Stage3-Green", "changed_components": ["policy_or_regulatory_score", "valuation_repricing_score", "execution_risk_score"], "component_delta_explanation": "R13 holdout reuse: C21 shadow profile rewards explicit recurring payout/ROE-PBR evidence, but penalizes theme-only bank rerating and digital-bank multiple without hard capital-return disclosure. Cross-guardrail interpretation: high MAE is accepted only as a risk flag; it becomes score-demotion evidence when paired with thin non-price evidence, price-only premium, binary event failure, or missing margin/direct-route bridge.", "MFE_90D_pct": 22.98, "MAE_90D_pct": -2.79, "score_return_alignment_label": "positive_control_kept", "current_profile_verdict": "current_profile_too_late"}
{"row_type": "score_simulation", "profile_id": "R13_cross_archetype_high_MAE_guardrail_holdout", "case_id": "R13L73_HMAE_POS_112610", "trigger_id": "R13L73_HMAE_REUSED_R12L73_C31_112610_T1_STAGE2_IRA_WIND_TOWER_VISIBILITY", "source_trigger_id": "R12L73_C31_112610_T1_STAGE2_IRA_WIND_TOWER_VISIBILITY", "symbol": "112610", "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL", "source_large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "source_canonical_archetype_id": "C31_POLICY_SUBSIDY_LEGISLATION_EVENT", "raw_component_scores_before": {"contract_score": 3, "backlog_visibility_score": 8, "margin_bridge_score": 8, "revision_score": 8, "relative_strength_score": 17, "customer_quality_score": 10, "policy_or_regulatory_score": 18, "valuation_repricing_score": 9, "execution_risk_score": -3, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0, "capacity_or_shipment_score": 11, "subsidy_directness_score": 11}, "weighted_score_before": 82.0, "stage_label_before": "Stage3-Yellow", "raw_component_scores_after": {"contract_score": 4, "backlog_visibility_score": 10, "margin_bridge_score": 9, "revision_score": 9, "relative_strength_score": 17, "customer_quality_score": 10, "policy_or_regulatory_score": 20, "valuation_repricing_score": 9, "execution_risk_score": -3, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0, "capacity_or_shipment_score": 14, "subsidy_directness_score": 15}, "weighted_score_after": 86.0, "stage_label_after": "Stage3-Yellow_near_green", "changed_components": ["policy_or_regulatory_score", "subsidy_directness_score", "capacity_or_shipment_score", "relative_strength_score", "execution_risk_score"], "component_delta_explanation": "R13 holdout reuse: C31 shadow profile separates direct subsidy/capacity/order route from policy-label-only relative strength; not a production score. Cross-guardrail interpretation: high MAE is accepted only as a risk flag; it becomes score-demotion evidence when paired with thin non-price evidence, price-only premium, binary event failure, or missing margin/direct-route bridge.", "MFE_90D_pct": 45.05, "MAE_90D_pct": -4.5, "score_return_alignment_label": "positive_control_kept", "current_profile_verdict": "current_profile_correct"}
{"row_type": "score_simulation", "profile_id": "R13_cross_archetype_high_MAE_guardrail_holdout", "case_id": "R13L73_HMAE_CEX_053800", "trigger_id": "R13L73_HMAE_REUSED_R8L73_C28_053800_T1_STAGE2_PRICE_ONLY_POLITICAL_SECURITY_THEME", "source_trigger_id": "R8L73_C28_053800_T1_STAGE2_PRICE_ONLY_POLITICAL_SECURITY_THEME", "symbol": "053800", "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL", "source_large_sector_id": "L8_PLATFORM_CONTENT_SW_SECURITY", "source_canonical_archetype_id": "C28_SOFTWARE_SECURITY_CONTRACT_RETENTION", "raw_component_scores_before": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 0, "revision_score": 0, "relative_strength_score": 20, "customer_quality_score": 3, "policy_or_regulatory_score": 0, "valuation_repricing_score": 15, "execution_risk_score": 18, "legal_or_contract_risk_score": 4, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_before": 79, "stage_label_before": "Stage3-Yellow", "raw_component_scores_after": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 0, "revision_score": 0, "relative_strength_score": 12, "customer_quality_score": 0, "policy_or_regulatory_score": 0, "valuation_repricing_score": 8, "execution_risk_score": 24, "legal_or_contract_risk_score": 4, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_after": 56, "stage_label_after": "Stage2-Watch", "changed_components": ["contract_score", "customer_quality_score", "valuation_repricing_score", "execution_risk_score"], "component_delta_explanation": "R13 holdout reuse: C28 shadow separates recurring contract/retention bridge from security/software theme premium. Price-only or AI/political optionality is capped; contract retention and renewal evidence can promote. Cross-guardrail interpretation: high MAE is accepted only as a risk flag; it becomes score-demotion evidence when paired with thin non-price evidence, price-only premium, binary event failure, or missing margin/direct-route bridge.", "MFE_90D_pct": 24.29, "MAE_90D_pct": -53.92, "score_return_alignment_label": "counterexample_guardrail_needed", "current_profile_verdict": "current_profile_false_positive"}
{"row_type": "score_simulation", "profile_id": "R13_cross_archetype_high_MAE_guardrail_holdout", "case_id": "R13L73_HMAE_CEX_247540", "trigger_id": "R13L73_HMAE_REUSED_TRG_247540_20231204_FAILED_RERATING", "source_trigger_id": "TRG_247540_20231204_FAILED_RERATING", "symbol": "247540", "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL", "source_large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "source_canonical_archetype_id": "C11_BATTERY_ORDERBOOK_RERATING", "raw_component_scores_before": {"contract_score": 82, "backlog_visibility_score": 85, "margin_bridge_score": 25, "revision_score": 25, "relative_strength_score": 25, "customer_quality_score": 65, "policy_or_regulatory_score": 35, "valuation_repricing_score": 65, "execution_risk_score": 55, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0, "capacity_or_shipment_score": 60, "asp_or_spread_score": 20, "utilization_score": 25, "positioning_overheat_score": 75, "thesis_break_score": 35}, "weighted_score_before": 83, "stage_label_before": "Stage3-Green-false-positive-risk", "raw_component_scores_after": {"contract_score": 72, "backlog_visibility_score": 65, "margin_bridge_score": 15, "revision_score": 15, "relative_strength_score": 20, "customer_quality_score": 55, "policy_or_regulatory_score": 30, "valuation_repricing_score": 55, "execution_risk_score": 70, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0, "capacity_or_shipment_score": 50, "asp_or_spread_score": 10, "utilization_score": 20, "positioning_overheat_score": 85, "thesis_break_score": 65}, "weighted_score_after": 70, "stage_label_after": "Stage4B/4C-watch-positive-blocked", "changed_components": ["contract_score", "backlog_visibility_score", "margin_bridge_score", "asp_or_spread_score", "utilization_score", "positioning_overheat_score", "thesis_break_score"], "component_delta_explanation": "R13 holdout reuse: C11 shadow split promotes named customer/orderbook with margin/customer quality, but caps contract-size-only or capacity-theme rerating when spread/utilization/relative strength are weak. Cross-guardrail interpretation: high MAE is accepted only as a risk flag; it becomes score-demotion evidence when paired with thin non-price evidence, price-only premium, binary event failure, or missing margin/direct-route bridge.", "MFE_90D_pct": 9.6, "MAE_90D_pct": -34.67, "score_return_alignment_label": "counterexample_guardrail_needed", "current_profile_verdict": "current_profile_false_positive"}
{"row_type": "score_simulation", "profile_id": "R13_cross_archetype_high_MAE_guardrail_holdout", "case_id": "R13L73_HMAE_CEX_028300", "trigger_id": "R13L73_HMAE_REUSED_TRG_R7L73_HLB_20240422_PREPDUFA", "source_trigger_id": "TRG_R7L73_HLB_20240422_PREPDUFA", "symbol": "028300", "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL", "source_large_sector_id": "L7_BIO_HEALTHCARE_MEDICAL", "source_canonical_archetype_id": "C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION", "raw_component_scores_before": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 0, "revision_score": 1, "relative_strength_score": 8, "customer_quality_score": 2, "policy_or_regulatory_score": 8, "valuation_repricing_score": 8, "execution_risk_score": 8, "legal_or_contract_risk_score": 7, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_before": 76.0, "stage_label_before": "Stage3-Yellow", "raw_component_scores_after": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 0, "revision_score": 0, "relative_strength_score": 4, "customer_quality_score": 1, "policy_or_regulatory_score": 5, "valuation_repricing_score": 3, "execution_risk_score": 10, "legal_or_contract_risk_score": 10, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_after": 62.0, "stage_label_after": "Stage2-Watch_until_decision_or_4C_after_CRL", "changed_components": ["policy_or_regulatory_score", "customer_quality_score", "revision_score", "relative_strength_score", "execution_risk_score"], "component_delta_explanation": "R13 holdout reuse: Pre-approval binary events are not allowed to become Green without actual approval plus commercial conversion; CRL routes to hard 4C. Cross-guardrail interpretation: high MAE is accepted only as a risk flag; it becomes score-demotion evidence when paired with thin non-price evidence, price-only premium, binary event failure, or missing margin/direct-route bridge.", "MFE_90D_pct": 7.53, "MAE_90D_pct": -55.79, "score_return_alignment_label": "counterexample_guardrail_needed", "current_profile_verdict": "current_profile_false_positive"}
{"row_type": "score_simulation", "profile_id": "R13_cross_archetype_high_MAE_guardrail_holdout", "case_id": "R13L73_HMAE_CEX_006910", "trigger_id": "R13L73_HMAE_REUSED_R1L73_T006910_20220310_STAGE2A_HOLDOUT", "source_trigger_id": "R1L73_T006910_20220310_STAGE2A_HOLDOUT", "symbol": "006910", "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL", "source_large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "source_canonical_archetype_id": "C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY", "raw_component_scores_before": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 0, "revision_score": 0, "relative_strength_score": 20, "customer_quality_score": 0, "policy_or_regulatory_score": 22, "valuation_repricing_score": 10, "execution_risk_score": 15, "legal_or_contract_risk_score": 4, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_before": 73, "stage_label_before": "Stage2-Actionable", "raw_component_scores_after": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 0, "revision_score": 0, "relative_strength_score": 14, "customer_quality_score": 0, "policy_or_regulatory_score": 13, "valuation_repricing_score": 6, "execution_risk_score": 21, "legal_or_contract_risk_score": 8, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_after": 55, "stage_label_after": "Stage2-Watch", "changed_components": ["policy_or_regulatory_score", "customer_quality_score", "backlog_visibility_score", "legal_or_contract_risk_score", "theme_only_stage_cap"], "component_delta_explanation": "R13 holdout reuse: Shadow-only C04 adjustment: add limited supplier/legal-de-risking bridge when IP/legal blocker clears and company has identifiable nuclear equipment route; cap policy-only theme blowoffs without contract/customer/revision bridge. Cross-guardrail interpretation: high MAE is accepted only as a risk flag; it becomes score-demotion evidence when paired with thin non-price evidence, price-only premium, binary event failure, or missing margin/direct-route bridge.", "MFE_90D_pct": 32.31, "MAE_90D_pct": -28.51, "score_return_alignment_label": "counterexample_guardrail_needed", "current_profile_verdict": "current_profile_false_positive"}
{"row_type": "residual_contribution", "round": "R13", "loop": "73", "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL", "new_independent_case_count": 0, "reused_case_count": 8, "new_symbol_count": 0, "new_trigger_family_count": 0, "tested_existing_calibrated_axes": ["price_only_blowoff_blocks_positive_stage", "full_4b_requires_non_price_evidence", "hard_4c_thesis_break_routes_to_4c", "stage3_green_revision_min", "stage3_yellow_total_min"], "residual_error_types_found": ["cross_archetype_high_MAE_false_positive", "thin_non_price_evidence_with_large_drawdown", "binary_event_predecision_green_false_positive", "price_only_event_premium_full_window_peak", "missed_structural_positive_control"], "loop_contribution_label": "holdout_validation_passed", "do_not_propose_new_weight_delta": true}
```

```csv
row_type,axis,scope,large_sector_id,canonical_archetype_id,baseline_value,tested_value,delta,reason,backtest_effect,trigger_ids,calibration_usable_count,new_independent_case_count,counterexample_count,confidence,proposal_type,notes
shadow_weight,R13_high_MAE_thin_evidence_guardrail,cross_archetype_redteam_holdout,L10_POLICY_EVENT_CROSS_REDTEAM_MISC,R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL,0,0,0,"High MAE alone is not a universal demotion; it becomes a guardrail when paired with thin non-price evidence, binary-event failure, price-only premium, or missing margin/direct-route bridge","Holdout separates four positives avg_MFE180=106.74/avg_MAE180=-4.15 from four counters avg_MFE180=18.43/avg_MAE180=-53.55; no production delta proposed","TRG_R7L73_ALT_20240223_S2A|T_C20_SAMYANG_STAGE2_20240517|R6L73_C21_138040_20240208_stage2_actionable_payout_program|R12L73_C31_112610_T1_STAGE2_IRA_WIND_TOWER_VISIBILITY|R8L73_C28_053800_T1_STAGE2_PRICE_ONLY_POLITICAL_SECURITY_THEME|TRG_247540_20231204_FAILED_RERATING|TRG_R7L73_HLB_20240422_PREPDUFA|R1L73_T006910_20220310_STAGE2A_HOLDOUT",8,0,4,medium,redteam_checkpoint_only,"not production; reused prior v12 rows for R13 checkpoint"
```

## 26. Deferred Coding Agent Handoff Prompt

### Purpose

You are now in the repository implementation phase. The attached Markdown files are v12 post-calibrated residual research outputs produced using the Songdaiki/stock-web OHLC atlas.

These MDs are not live candidate research. They are historical calibration research designed to extend the already-applied e2r_2_1_stock_web_calibrated profile.

Do not blindly apply every shadow row.
Ingest the machine-readable rows and update the sector/canonical-archetype calibration ledger.

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
completed_round = R13
completed_loop = 73
next_round = R1
next_loop = 74
round_schedule_status = valid
round_sector_consistency = pass
```

## 28. Source Notes

- Stock-Web manifest and schema were checked for this run; `manifest.max_date = 2026-02-20`.
- Price source fields used in machine-readable rows point to `Songdaiki/stock-web` tradable shards and profiles.
- All selected trigger metrics are reused from prior v12 local research artifact rows and are explicitly marked as R13 holdout validation.
- This MD contains no stock_agent source-code inspection and no production scoring patch.

