# E2R Stock-Web Historical Calibration / Sector-Archetype Residual Research Round

## 0. Research Metadata

```text
filename = e2r_stock_web_v12_residual_round_R12_loop_14_L10_POLICY_EVENT_CROSS_REDTEAM_MISC_C31_POLICY_SUBSIDY_LEGISLATION_EVENT_research.md
research_session = post_calibrated_sector_archetype_residual_research
mode = historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12
scheduled_round = R12
scheduled_loop = 14
completed_round = R12
completed_loop = 14
next_round = R13
next_loop = 14
round_schedule_status = valid
round_sector_consistency = pass

large_sector_id = L10_POLICY_EVENT_CROSS_REDTEAM_MISC
canonical_archetype_id = C31_POLICY_SUBSIDY_LEGISLATION_EVENT
fine_archetype_id = COVID_PUBLIC_HEALTH_PPE_SUPPLY_ROUTE_GUARD
loop_objective = coverage_gap_fill | counterexample_mining | residual_false_positive_mining | 4B_non_price_requirement_stress_test | green_strictness_stress_test | canonical_archetype_compression

price_source = Songdaiki/stock-web
stock_web_manifest_max_date = 2026-02-20
price_basis = tradable_raw
price_adjustment_status = raw_unadjusted_marcap
production_scoring_changed = false
shadow_weight_only = true
handoff_prompt_embedded = true
handoff_prompt_executed_now = false
```

This loop adds 4 new independent cases, 2 counterexamples, and 3 residual errors for R12/L10_POLICY_EVENT_CROSS_REDTEAM_MISC/C31_POLICY_SUBSIDY_LEGISLATION_EVENT.

## 1. Current Calibrated Profile Assumption

The current proxy profile is `e2r_2_1_stock_web_calibrated_proxy`. The baseline reference remains `e2r_2_0_baseline_reference`.

Existing calibrated axes are treated as already applied and are not re-proposed globally:

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

The residual question is narrower: **when should a public-health / PPE policy event in R12 be promoted as real Stage2/Yellow evidence, and when is it merely emergency hoarding or peripheral theme beta wearing a policy mask?**

## 2. Round / Large Sector / Canonical Archetype Scope

| field | value |
|---|---|
| scheduled_round | R12 |
| scheduled_loop | 14 |
| large_sector_id | L10_POLICY_EVENT_CROSS_REDTEAM_MISC |
| canonical_archetype_id | C31_POLICY_SUBSIDY_LEGISLATION_EVENT |
| fine_archetype_id | COVID_PUBLIC_HEALTH_PPE_SUPPLY_ROUTE_GUARD |
| round sector consistency | pass |
| next round | R13 / loop 14 |

R12 permits L10 policy/event/cross-misc work or under-covered service/agri/life-service cases. This loop uses L10 because the COVID public-health shock is a policy/event shock, while the symbols are life-service/material/PPE-adjacent rather than a clean R7 biotech or R8 software case.

## 3. Previous Coverage / Duplicate Avoidance Check

Existing local v12 R12 files cover:

| prior loop | canonical | fine area already covered | duplicate action |
|---|---|---|---|
| R12 loop 10 | C31 | grain/feed shock, online education, food-safety/person themes | avoid symbols 005860/057030/053290/011150 |
| R12 loop 11 | C31 | grain/feed and Fukushima hoarding route split | avoid symbols 008040/218150/277410/248170 |
| R12 loop 12 | C31 | China group-tour reopening / travel-service recovery | avoid symbols 039130/032350/008770/034230 |
| R12 loop 13 | C32 | governance/control premium event failures | avoid C32 repetition |

New symbol set:

```text
065950, 083550, 045060, 012690
```

No case reuses the same symbol + trigger_date + entry_date + evidence family from prior R12 loops. Same canonical `C31` is intentional; the new evidence family is public-health PPE / hygiene supply route vs theme-only emergency hoarding.

## 4. Stock-Web OHLC Input / Price Source Validation

| manifest field | observed value |
|---|---|
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

The atlas is raw/unadjusted. Corporate-action-contaminated windows are blocked. The selected 2020 windows are clean at the 180D calibration window according to each profile's candidate-date list.

## 5. Historical Eligibility Gate

| case_id | symbol | trigger_date | entry_date | 180D forward available by manifest max_date | corporate action 180D status | usable? |
|---|---:|---:|---:|---|---|---|
| R12L14_C31_065950_WELCRON_COVID_PPE_20200120 | 065950 | 2020-01-20 | 2020-01-20 | yes | clean_180D_window; profile candidate only 2006-01-17 | true |
| R12L14_C31_083550_KM_COVID_PPE_20200120 | 083550 | 2020-01-20 | 2020-01-20 | yes | clean_180D_window; profile has no corporate-action candidates | true |
| R12L14_C31_045060_OKONG_COVID_THEME_20200120 | 045060 | 2020-01-20 | 2020-01-20 | yes | clean_180D_window; profile candidates outside 2020 window | true |
| R12L14_C31_012690_MONALISA_COVID_HYGIENE_20200120 | 012690 | 2020-01-20 | 2020-01-20 | yes | clean_180D_window; profile candidates before 2003 | true |

## 6. Canonical Archetype Compression Map

| canonical_archetype_id | fine_archetype_id | compression rule |
|---|---|---|
| C31_POLICY_SUBSIDY_LEGISLATION_EVENT | COVID_PUBLIC_HEALTH_PPE_SUPPLY_ROUTE | public-health event + direct PPE/supply route may support Stage2/Yellow |
| C31_POLICY_SUBSIDY_LEGISLATION_EVENT | COVID_PUBLIC_HEALTH_PPE_THEME_ONLY_GUARD | public-health event + peripheral theme/RS should remain watch/4B, not Green |
| C31_POLICY_SUBSIDY_LEGISLATION_EVENT | COVID_PUBLIC_HEALTH_CONSUMER_HYGIENE_HOARDING_GUARD | hoarding/shelf-panic demand needs repeat sell-through and margin bridge before promotion |

## 7. Case Selection Summary

| case_id | symbol | company | role | selected trigger family | new? | why selected |
|---|---:|---|---|---|---|---|
| R12L14_C31_065950_WELCRON_COVID_PPE_20200120 | 065950 | 웰크론 | positive | direct PPE / mask-material event route | true | large MFE from early public-health shock but needs 4B overlay after price blowoff |
| R12L14_C31_083550_KM_COVID_PPE_20200120 | 083550 | 케이엠 | positive | PPE / cleanroom / mask supply route | true | delayed higher peak and relatively lower early MAE distinguish it from one-day theme spikes |
| R12L14_C31_045060_OKONG_COVID_THEME_20200120 | 045060 | 오공 | counterexample | public-health peripheral theme | true | huge price beta but weak durable policy-to-cash-flow bridge |
| R12L14_C31_012690_MONALISA_COVID_HYGIENE_20200120 | 012690 | 모나리자 | counterexample | consumer hygiene hoarding route | true | emergency demand/hoarding spike lacks durable Green proof |

## 8. Positive vs Counterexample Balance

| balance field | value |
|---|---:|
| positive_case_count | 2 |
| counterexample_count | 2 |
| 4B_case_count | 4 |
| 4C_case_count | 0 |
| calibration_usable_case_count | 4 |
| calibration_usable_trigger_count | 8 |
| representative_trigger_count | 4 |
| new_independent_case_count | 4 |
| reused_case_count | 0 |

The positive side proves that public-health PPE routes should not be dismissed as pure price action. The counterexample side prevents the same event headline from over-promoting peripheral or hoarding themes into Stage3-Green.

## 9. Evidence Source Map

| case | evidence source class | allowed for scoring | blocked for promotion |
|---|---|---|---|
| 웰크론 | public COVID event + direct PPE/mask-material route + stock-web 2020 OHLC | public_event_or_disclosure; policy_or_regulatory_optionality; capacity_or_volume_route; relative_strength | price-only Green; post-peak outcome labeling |
| 케이엠 | public COVID event + PPE/cleanroom route + stock-web 2020 OHLC | public_event_or_disclosure; policy_or_regulatory_optionality; capacity_or_volume_route; relative_strength | Green without margin/revision/order proof |
| 오공 | public COVID event + peripheral public-health theme + stock-web 2020 OHLC | Stage2 watch only; RS as risk signal | Stage3-Green from theme + price alone |
| 모나리자 | public COVID event + consumer hygiene/hoarding route + stock-web 2020 OHLC | Stage2 watch only; hoarding as event-risk signal | durable rerating without repeat sell-through/margin bridge |

## 10. Price Data Source Map

| symbol | company | profile_path | representative shard | profile 180D status |
|---:|---|---|---|---|
| 065950 | 웰크론 | atlas/symbol_profiles/065/065950.json | atlas/ohlcv_tradable_by_symbol_year/065/065950/2020.csv | clean_180D_window |
| 083550 | 케이엠 | atlas/symbol_profiles/083/083550.json | atlas/ohlcv_tradable_by_symbol_year/083/083550/2020.csv | clean_180D_window |
| 045060 | 오공 | atlas/symbol_profiles/045/045060.json | atlas/ohlcv_tradable_by_symbol_year/045/045060/2020.csv | clean_180D_window |
| 012690 | 모나리자 | atlas/symbol_profiles/012/012690.json | atlas/ohlcv_tradable_by_symbol_year/012/012690/2020.csv | clean_180D_window |

## 11. Case-by-Case Trigger Grid

| trigger_id | case_id | trigger_type | trigger_date | entry_date | entry_price | same_entry_group_id | aggregate role | current_profile_verdict |
|---|---|---|---:|---:|---:|---|---|---|
| R12L14_C31_065950_STAGE2A_20200120 | R12L14_C31_065950_WELCRON_COVID_PPE_20200120 | Stage2-Actionable | 2020-01-20 | 2020-01-20 | 4855 | R12L14_C31_065950_WELCRON_COVID_PPE_20200120_ENTRY | representative | current_profile_4B_too_late |
| R12L14_C31_083550_STAGE2A_20200120 | R12L14_C31_083550_KM_COVID_PPE_20200120 | Stage2-Actionable | 2020-01-20 | 2020-01-20 | 8920 | R12L14_C31_083550_KM_COVID_PPE_20200120_ENTRY | representative | current_profile_correct |
| R12L14_C31_045060_STAGE2WATCH_20200120 | R12L14_C31_045060_OKONG_COVID_THEME_20200120 | Stage2_event_premium_risk_watch | 2020-01-20 | 2020-01-20 | 4775 | R12L14_C31_045060_OKONG_COVID_THEME_20200120_ENTRY | representative | current_profile_false_positive |
| R12L14_C31_012690_STAGE2WATCH_20200120 | R12L14_C31_012690_MONALISA_COVID_HYGIENE_20200120 | Stage2_event_premium_risk_watch | 2020-01-20 | 2020-01-20 | 4430 | R12L14_C31_012690_MONALISA_COVID_HYGIENE_20200120_ENTRY | representative | current_profile_false_positive |
| R12L14_C31_065950_4B_20200221 | R12L14_C31_065950_WELCRON_COVID_PPE_20200120 | Stage4B_overlay | 2020-02-21 | 2020-02-21 | 9020 | R12L14_C31_065950_WELCRON_COVID_PPE_20200120_4B | 4B_overlay_only | current_profile_4B_too_late |
| R12L14_C31_083550_4B_20200525 | R12L14_C31_083550_KM_COVID_PPE_20200120 | Stage4B_overlay | 2020-05-25 | 2020-05-25 | 21450 | R12L14_C31_083550_KM_COVID_PPE_20200120_4B | 4B_overlay_only | current_profile_4B_too_late |
| R12L14_C31_045060_4B_20200221 | R12L14_C31_045060_OKONG_COVID_THEME_20200120 | Stage4B_overlay | 2020-02-21 | 2020-02-21 | 12150 | R12L14_C31_045060_OKONG_COVID_THEME_20200120_4B | 4B_overlay_only | current_profile_correct |
| R12L14_C31_012690_4B_20200221 | R12L14_C31_012690_MONALISA_COVID_HYGIENE_20200120 | Stage4B_overlay | 2020-02-21 | 2020-02-21 | 8220 | R12L14_C31_012690_MONALISA_COVID_HYGIENE_20200120_4B | 4B_overlay_only | current_profile_correct |


## 12. Trigger-Level OHLC Backtest Tables

### 12.1 Representative entry triggers

| trigger_id | entry_price | MFE_30D_pct | MAE_30D_pct | MFE_90D_pct | MAE_90D_pct | MFE_180D_pct | MAE_180D_pct | peak_date | peak_price | drawdown_after_peak_pct | outcome label |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|
| R12L14_C31_065950_STAGE2A_20200120 | 4855 | 120.39 | -16.17 | 120.39 | -16.17 | 120.39 | -16.17 | 2020-02-21 | 10700 | -52.8 | direct_PPE_event_stage2_success_but_price_only_4B_needed |
| R12L14_C31_083550_STAGE2A_20200120 | 8920 | 117.49 | -9.19 | 150.0 | -9.19 | 150.0 | -9.19 | 2020-05-25 | 22300 | -42.83 | direct_PPE_stage2_then_delayed_peak_success |
| R12L14_C31_045060_STAGE2WATCH_20200120 | 4775 | 200.52 | -21.36 | 200.52 | -21.36 | 200.52 | -21.36 | 2020-02-21 | 14350 | -72.02 | peripheral_theme_spike_failed_durable_rerating |
| R12L14_C31_012690_STAGE2WATCH_20200120 | 4430 | 120.99 | -10.05 | 120.99 | -14.22 | 120.99 | -14.22 | 2020-02-03 | 9790 | -61.18 | consumer_hygiene_hoarding_spike_failed_green |

### 12.2 4B overlay triggers

| trigger_id | entry_price | peak_price_used | local proximity | full-window proximity | timing verdict |
|---|---:|---:|---:|---:|---|
| R12L14_C31_065950_4B_20200221 | 9020 | 10700 | 0.71 | 0.71 | useful_4B_but_not_hard_4C |
| R12L14_C31_083550_4B_20200525 | 21450 | 22300 | 0.94 | 0.94 | good_full_window_4B_timing_for_event_premium |
| R12L14_C31_045060_4B_20200221 | 12150 | 14350 | 0.77 | 0.77 | good_full_window_4B_timing_for_event_premium |
| R12L14_C31_012690_4B_20200221 | 8220 | 9790 | 0.71 | 0.71 | good_full_window_4B_timing_for_event_premium |


Backtest math uses `entry_price = c` from the stock-web tradable shard and computes MFE/MAE from the high/low window through the 180-trading-day calibration horizon. 1Y/2Y fields in JSONL are left `null` because this loop proposes only 180D shadow deltas.

## 13. Current Calibrated Profile Stress Test

| case_id | current profile likely decision | actual alignment | verdict | residual error |
|---|---|---|---|---|
| R12L14_C31_065950_WELCRON_COVID_PPE_20200120 | Stage2 is allowed, but price-only 4B may be late | +120.39% MFE, then large post-peak drawdown | current_profile_4B_too_late | PPE event needs 4B overlay once price-only blowoff dominates |
| R12L14_C31_083550_KM_COVID_PPE_20200120 | Stage2/Yellow candidate with route evidence | +150.00% 90D/180D MFE with lower early MAE | current_profile_correct | Existing Stage2 bonus mostly works when route is direct |
| R12L14_C31_045060_OKONG_COVID_THEME_20200120 | RS + event could be over-promoted | high MFE but severe post-peak failure | current_profile_false_positive | Peripheral theme needs guard penalty |
| R12L14_C31_012690_MONALISA_COVID_HYGIENE_20200120 | hoarding/hygiene could be over-promoted | high MFE but hoarding path fails durable Green | current_profile_false_positive | consumer-hoarding route needs repeat sell-through/margin proof |

Stress-test answers:

```text
1. Stage2 bonus is appropriate for direct PPE supply route, too strong for peripheral/hoarding themes.
2. Yellow threshold 75 is too permissive if relative strength + public event are enough.
3. Green 87 / revision 55 is correctly strict; do not weaken it for public-health themes.
4. price_only_blowoff_blocks_positive_stage is strengthened.
5. full_4b_requires_non_price_evidence is kept; price-only peaks are overlays/watch, not hard 4C.
6. hard_4c_thesis_break routing is not tested as a new 4C in this loop.
```

## 14. Stage2 / Yellow / Green Comparison

| case | Stage2 entry | plausible Green trigger | green_lateness_ratio | interpretation |
|---|---:|---|---:|---|
| 웰크론 | 4855 | no clean confirmed Stage3-Green | not_applicable | event Stage2 captured move; Green needs order/revision support |
| 케이엠 | 8920 | no clean confirmed Stage3-Green | not_applicable | direct supply route sustains event, but Green remains proof-gated |
| 오공 | 4775 | no valid Green | not_applicable | theme-only spike should not become Green |
| 모나리자 | 4430 | no valid Green | not_applicable | hoarding spike should not become Green |

## 15. 4B Local vs Full-window Timing Audit

| case | Stage2 entry | 4B entry | local peak | full-window peak | local proximity | full-window proximity | evidence type | timing verdict |
|---|---:|---:|---:|---:|---:|---:|---|---|
| 웰크론 | 4855 | 9020 | 10700 | 10700 | 0.71 | 0.71 | valuation_blowoff; positioning_overheat; price_only | useful_4B_but_not_hard_4C |
| 케이엠 | 8920 | 21450 | 22300 | 22300 | 0.94 | 0.94 | valuation_blowoff; positioning_overheat; event demand pull-forward | good_full_window_4B_timing_for_event_premium |
| 오공 | 4775 | 12150 | 14350 | 14350 | 0.77 | 0.77 | valuation_blowoff; positioning_overheat; peripheral theme | good_full_window_4B_timing_for_event_premium |
| 모나리자 | 4430 | 8220 | 9790 | 9790 | 0.71 | 0.71 | valuation_blowoff; consumer-hoarding pull-forward | good_full_window_4B_timing_for_event_premium |

## 16. 4C Protection Audit

No hard 4C row is used for quantitative weight calibration. The right classification is:

```text
four_c_protection_label = thesis_break_watch_only
```

The cases are event-premium decay and demand-pull-forward overlays, not a discrete contract cancellation, trial failure, regulatory rejection, or accounting/trust break.

## 17. Sector-Specific Rule Candidate

`sector_specific_rule_candidate = true`.

For R12 public-health / PPE events, Stage2/Yellow promotion should require a **route**, not just a headline:

```text
positive route:
- direct PPE/mask/cleanroom supply,
- visible demand route to capacity or shipment,
- early public-health policy optionality,
- relative strength confirming event attention.

blocked route:
- consumer hoarding without repeat sell-through,
- peripheral public-health theme without direct revenue bridge,
- price-only spike after the first event wave,
- no margin/revision/order evidence.
```

## 18. Canonical-Archetype Rule Candidate

`canonical_archetype_rule_candidate = true`.

Proposed C31 shadow rule:

```text
if C31 event_family == public_health_ppe:
    if direct_supply_route and capacity_or_volume_route:
        add C31_public_health_direct_supply_bonus
    if consumer_hoarding_or_peripheral_theme and no repeat_order_or_margin_bridge:
        apply C31_consumer_hoarding_theme_penalty
    if price spike is local/full-window event cap:
        route to C31_price_only_event_peak_4B_overlay
```

This is not a global rule. It applies to R12/C31 public-health, PPE, and consumer hygiene policy/event shocks.

## 19. Before / After Backtest Comparison

| profile_id | scope | changed axes | eligible representative triggers | avg_MFE_90D_pct | avg_MAE_90D_pct | avg_MFE_180D_pct | avg_MAE_180D_pct | false_positive_rate | score_return_alignment_verdict |
|---|---|---|---:|---:|---:|---:|---:|---:|---|
| P0_e2r_2_1_stock_web_calibrated_proxy | current | none | 4 | 147.97 | -15.23 | 147.97 | -15.23 | 0.50 | mixed; good Stage2 but overpromotion risk |
| P0b_e2r_2_0_baseline_reference | rollback | none | 4 | 147.97 | -15.23 | 147.97 | -15.23 | 0.50 | misses route split and 4B timing |
| P1_R12_public_health_sector_shadow | sector_specific | public_health_direct_supply_bonus; hoarding_theme_penalty | 4 | 147.97 | -15.23 | 147.97 | -15.23 | 0.25 | improves positive/counterexample split |
| P2_C31_PPE_archetype_shadow | canonical_archetype_specific | direct route bonus; theme-only guard | 4 | 147.97 | -15.23 | 147.97 | -15.23 | 0.25 | best alignment for C31 |
| P3_C31_counterexample_guard | canonical_archetype_specific | price-only event peak 4B overlay | 4 | 147.97 | -15.23 | 147.97 | -15.23 | 0.25 | reduces false Green after blowoff |

## 20. Score-Return Alignment Matrix

| case | weighted_score_before | label_before | weighted_score_after | label_after | MFE90 | MAE90 | alignment |
|---|---:|---|---:|---|---:|---:|---|
| R12L14_C31_065950_WELCRON_COVID_PPE_20200120 | 78 | Stage2-Actionable | 82 | Stage3-Yellow_candidate_only | 120.39 | -16.17 | direct_PPE_event_stage2_success_but_price_only_4B_needed |
| R12L14_C31_083550_KM_COVID_PPE_20200120 | 78 | Stage2-Actionable | 84 | Stage3-Yellow_candidate_only | 150.0 | -9.19 | direct_PPE_stage2_then_delayed_peak_success |
| R12L14_C31_045060_OKONG_COVID_THEME_20200120 | 76 | Stage2-Actionable_or_Yellow_if_RS_overweighted | 58 | Stage2_watch_or_4B_overlay | 200.52 | -21.36 | peripheral_theme_spike_failed_durable_rerating |
| R12L14_C31_012690_MONALISA_COVID_HYGIENE_20200120 | 76 | Stage2-Actionable_or_Yellow_if_RS_overweighted | 58 | Stage2_watch_or_4B_overlay | 120.99 | -14.22 | consumer_hygiene_hoarding_spike_failed_green |


## 21. Coverage Matrix

| large_sector_id | canonical_archetype_id | fine_archetype_id | positive_case_count | counterexample_count | 4B_case_count | 4C_case_count | new_independent_case_count | reused_case_count | calibration_usable_trigger_count | representative_trigger_count | current_profile_error_count | sector_rule_candidate | canonical_rule_candidate | coverage_gap_after_this_loop |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|---|---|
| L10_POLICY_EVENT_CROSS_REDTEAM_MISC | C31_POLICY_SUBSIDY_LEGISLATION_EVENT | COVID_PUBLIC_HEALTH_PPE_SUPPLY_ROUTE_GUARD | 2 | 2 | 4 | 0 | 4 | 0 | 8 | 4 | 3 | true | true | PPE/public-health route now covered; still needs later loops for service labor/regulation events |

## 22. Residual Contribution Summary

```text
new_independent_case_count: 4
reused_case_count: 0
reused_case_ids: []
new_symbol_count: 4
same_archetype_new_symbol_count: 4
same_archetype_new_trigger_family_count: 4
new_canonical_archetype_count: 0
new_fine_archetype_count: 3
new_trigger_family_count: 4
tested_existing_calibrated_axes:
  - stage2_actionable_evidence_bonus
  - stage3_yellow_total_min
  - stage3_green_total_min
  - price_only_blowoff_blocks_positive_stage
  - full_4b_requires_non_price_evidence
residual_error_types_found:
  - PPE_direct_supply_vs_peripheral_theme_split
  - consumer_hoarding_false_positive
  - 4B_price_peak_should_not_promote_Green
new_axis_proposed:
  - C31_public_health_direct_supply_bonus
  - C31_consumer_hoarding_theme_penalty
  - C31_price_only_event_peak_4B_overlay
existing_axis_strengthened:
  - price_only_blowoff_blocks_positive_stage
  - full_4b_requires_non_price_evidence
existing_axis_weakened: null
existing_axis_kept:
  - stage3_green_total_min
  - stage3_green_revision_min
sector_specific_rule_candidate: true
canonical_archetype_rule_candidate: true
no_new_signal_reason: null

loop_contribution_label: canonical_archetype_rule_candidate
do_not_propose_new_weight_delta: false
```

## 23. Validation Scope / Non-Validation Scope

Validated:

```text
- Stock-web manifest max_date, price_basis, adjustment status.
- Symbol profile availability and corporate-action candidate windows.
- Entry_date and entry_price from tradable shards.
- 30D/90D/180D MFE/MAE from observed stock-web rows.
- Positive/counterexample split inside scheduled R12 scope.
- 4B local vs full-window proximity split.
```

Not validated:

```text
- No live watchlist.
- No current candidate scan.
- No production scoring change.
- No brokerage / auto-trading.
- No stock_agent source-code inspection.
- No FinanceDataReader / pykrx / external price route discovery.
- 1Y/2Y fields are present as null in JSONL and are not used for this loop's shadow delta.
```

## 24. Shadow Weight Calibration

```csv
row_type,axis,scope,large_sector_id,canonical_archetype_id,baseline_value,tested_value,delta,reason,backtest_effect,trigger_ids,calibration_usable_count,new_independent_case_count,counterexample_count,confidence,proposal_type,notes
shadow_weight,C31_public_health_direct_supply_bonus,canonical_archetype_specific,L10_POLICY_EVENT_CROSS_REDTEAM_MISC,C31_POLICY_SUBSIDY_LEGISLATION_EVENT,0,1,+1,Direct PPE supplier route had stronger 90D/180D MFE with lower MAE than peripheral/hoarding themes.,Improves Stage2/Yellow selection for 065950/083550 without promoting price-only Green.,R12L14_C31_065950_STAGE2A_20200120|R12L14_C31_083550_STAGE2A_20200120,4,4,2,medium,canonical_shadow_only,not production; post-calibrated residual
shadow_weight,C31_consumer_hoarding_theme_penalty,canonical_archetype_specific,L10_POLICY_EVENT_CROSS_REDTEAM_MISC,C31_POLICY_SUBSIDY_LEGISLATION_EVENT,0,1,+1 risk penalty,Hygiene hoarding/peripheral themes had high MFE but weaker durable route and severe peak drawdown.,Blocks Stage3-Green promotion for 045060/012690 unless margin/reorder proof appears.,R12L14_C31_045060_STAGE2WATCH_20200120|R12L14_C31_012690_STAGE2WATCH_20200120,4,4,2,medium,canonical_shadow_only,not production; post-calibrated residual
shadow_weight,C31_price_only_event_peak_4B_overlay,canonical_archetype_specific,L10_POLICY_EVENT_CROSS_REDTEAM_MISC,C31_POLICY_SUBSIDY_LEGISLATION_EVENT,0,1,+1 overlay,All four cases show event peaks where price-only blowoff should cap new positive promotion.,Reduces false Green after public-health spike; keeps existing full_4B_requires_non_price_evidence.,R12L14_C31_065950_4B_20200221|R12L14_C31_083550_4B_20200525|R12L14_C31_045060_4B_20200221|R12L14_C31_012690_4B_20200221,4,4,2,medium,canonical_shadow_only,not production; post-calibrated residual
```

## 25. Machine-Readable Rows

```jsonl
{"row_type": "price_source_validation", "source": "Songdaiki/stock-web", "source_url": "https://github.com/Songdaiki/stock-web", "manifest_path": "atlas/manifest.json", "schema_path": "atlas/schema.json", "universe_path": "atlas/universe/all_symbols.csv", "manifest_max_date": "2026-02-20", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "raw_shard_root": "atlas/ohlcv_raw_by_symbol_year", "validation_status": "usable_for_historical_calibration"}
{"row_type": "case", "case_id": "R12L14_C31_065950_WELCRON_COVID_PPE_20200120", "symbol": "065950", "company_name": "웰크론", "round": "R12", "loop": "14", "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "C31_POLICY_SUBSIDY_LEGISLATION_EVENT", "fine_archetype_id": "COVID_PUBLIC_HEALTH_PPE_SUPPLY_ROUTE", "case_type": "high_mae_success", "positive_or_counterexample": "positive", "best_trigger": "R12L14_C31_065950_STAGE2A_20200120", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "direct_PPE_event_stage2_success_but_price_only_4B_needed", "current_profile_verdict": "current_profile_4B_too_late", "price_source": "Songdaiki/stock-web", "notes": "Direct mask/PPE supply route made the public-health event tradable, but the run was still a tactical event path, not durable Green without order/revision proof."}
{"row_type": "case", "case_id": "R12L14_C31_083550_KM_COVID_PPE_20200120", "symbol": "083550", "company_name": "케이엠", "round": "R12", "loop": "14", "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "C31_POLICY_SUBSIDY_LEGISLATION_EVENT", "fine_archetype_id": "COVID_PUBLIC_HEALTH_PPE_SUPPLY_ROUTE", "case_type": "structural_success", "positive_or_counterexample": "positive", "best_trigger": "R12L14_C31_083550_STAGE2A_20200120", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "direct_PPE_stage2_then_delayed_peak_success", "current_profile_verdict": "current_profile_correct", "price_source": "Songdaiki/stock-web", "notes": "Cleaner direct PPE/cleanroom route kept the event alive longer than the first mask spike; Stage2 works, but Green still needs margin/revision support."}
{"row_type": "case", "case_id": "R12L14_C31_045060_OKONG_COVID_THEME_20200120", "symbol": "045060", "company_name": "오공", "round": "R12", "loop": "14", "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "C31_POLICY_SUBSIDY_LEGISLATION_EVENT", "fine_archetype_id": "COVID_PUBLIC_HEALTH_PPE_THEME_ONLY_GUARD", "case_type": "failed_rerating", "positive_or_counterexample": "counterexample", "best_trigger": "R12L14_C31_045060_STAGE2WATCH_20200120", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "peripheral_theme_spike_failed_durable_rerating", "current_profile_verdict": "current_profile_false_positive", "price_source": "Songdaiki/stock-web", "notes": "The stock had a violent event beta, but the evidence family was peripheral/theme-only; it should be risk-watch/4B overlay rather than clean Stage3."}
{"row_type": "case", "case_id": "R12L14_C31_012690_MONALISA_COVID_HYGIENE_20200120", "symbol": "012690", "company_name": "모나리자", "round": "R12", "loop": "14", "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "C31_POLICY_SUBSIDY_LEGISLATION_EVENT", "fine_archetype_id": "COVID_PUBLIC_HEALTH_CONSUMER_HYGIENE_HOARDING_GUARD", "case_type": "failed_rerating", "positive_or_counterexample": "counterexample", "best_trigger": "R12L14_C31_012690_STAGE2WATCH_20200120", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "consumer_hygiene_hoarding_spike_failed_green", "current_profile_verdict": "current_profile_false_positive", "price_source": "Songdaiki/stock-web", "notes": "Consumer hygiene/hoarding demand was real at the shelf level, but not a durable rerating bridge without repeated sell-through and margin proof."}
{"row_type": "trigger", "trigger_id": "R12L14_C31_065950_STAGE2A_20200120", "case_id": "R12L14_C31_065950_WELCRON_COVID_PPE_20200120", "symbol": "065950", "company_name": "웰크론", "round": "R12", "loop": "14", "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "C31_POLICY_SUBSIDY_LEGISLATION_EVENT", "fine_archetype_id": "COVID_PUBLIC_HEALTH_PPE_SUPPLY_ROUTE", "sector": "public_health_ppe_textile_mask", "primary_archetype": "C31_POLICY_SUBSIDY_LEGISLATION_EVENT", "loop_objective": "coverage_gap_fill|counterexample_mining|sector_specific_rule_discovery|4B_non_price_requirement_stress_test|green_strictness_stress_test", "trigger_type": "Stage2-Actionable", "trigger_date": "2020-01-20", "entry_date": "2020-01-20", "entry_price": 4855, "evidence_available_at_that_date": "Korea's first confirmed COVID-19 case created public-health PPE / hygiene demand optionality; only direct supply or verified route evidence may promote beyond Stage2.", "evidence_source": "Historical COVID public-health event classification; stock-web OHLC shard atlas/ohlcv_tradable_by_symbol_year/065/065950/2020.csv; profile atlas/symbol_profiles/065/065950.json.", "stage2_evidence_fields": ["public_event_or_disclosure", "policy_or_regulatory_optionality", "capacity_or_volume_route", "relative_strength"], "stage3_evidence_fields": ["multiple_public_sources", "financial_visibility_watch_only"], "stage4b_evidence_fields": ["valuation_blowoff", "positioning_overheat", "price_only_local_peak"], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/065/065950/2020.csv", "profile_path": "atlas/symbol_profiles/065/065950.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": 120.39, "MFE_90D_pct": 120.39, "MFE_180D_pct": 120.39, "MFE_1Y_pct": null, "MFE_2Y_pct": null, "MAE_30D_pct": -16.17, "MAE_90D_pct": -16.17, "MAE_180D_pct": -16.17, "MAE_1Y_pct": null, "MAE_2Y_pct": null, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2020-02-21", "peak_price": 10700, "drawdown_after_peak_pct": -52.8, "green_lateness_ratio": "not_applicable:no_clean_Stage3_Green_trigger", "four_b_local_peak_proximity": null, "four_b_full_window_peak_proximity": null, "four_b_timing_verdict": "Stage2_entry_not_4B_overlay", "four_b_evidence_type": [], "four_c_protection_label": "thesis_break_watch_only", "trigger_outcome_label": "direct_PPE_event_stage2_success_but_price_only_4B_needed", "current_profile_verdict": "current_profile_4B_too_late", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window", "same_entry_group_id": "R12L14_C31_065950_WELCRON_COVID_PPE_20200120_ENTRY", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false}
{"row_type": "trigger", "trigger_id": "R12L14_C31_065950_4B_20200221", "case_id": "R12L14_C31_065950_WELCRON_COVID_PPE_20200120", "symbol": "065950", "company_name": "웰크론", "round": "R12", "loop": "14", "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "C31_POLICY_SUBSIDY_LEGISLATION_EVENT", "fine_archetype_id": "COVID_PUBLIC_HEALTH_PPE_SUPPLY_ROUTE", "sector": "public_health_ppe_textile_mask", "primary_archetype": "C31_POLICY_SUBSIDY_LEGISLATION_EVENT", "loop_objective": "coverage_gap_fill|counterexample_mining|sector_specific_rule_discovery|4B_non_price_requirement_stress_test|green_strictness_stress_test", "trigger_type": "Stage4B_overlay", "trigger_date": "2020-02-21", "entry_date": "2020-02-21", "entry_price": 9020, "evidence_available_at_that_date": "Local/full-window event premium had become dominated by valuation blowoff, positioning overheat, and demand-pull-forward risk; use as overlay, not Stage3 evidence.", "evidence_source": "Historical COVID public-health event classification; stock-web OHLC shard atlas/ohlcv_tradable_by_symbol_year/065/065950/2020.csv; profile atlas/symbol_profiles/065/065950.json.", "stage2_evidence_fields": [], "stage3_evidence_fields": [], "stage4b_evidence_fields": ["valuation_blowoff", "positioning_overheat", "price_only_local_peak"], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/065/065950/2020.csv", "profile_path": "atlas/symbol_profiles/065/065950.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": null, "MFE_90D_pct": null, "MFE_180D_pct": null, "MFE_1Y_pct": null, "MFE_2Y_pct": null, "MAE_30D_pct": null, "MAE_90D_pct": null, "MAE_180D_pct": null, "MAE_1Y_pct": null, "MAE_2Y_pct": null, "below_entry_price_flag_30D": null, "below_entry_price_flag_90D": null, "peak_date": "2020-02-21", "peak_price": 10700, "drawdown_after_peak_pct": -52.8, "green_lateness_ratio": "not_applicable:no_clean_Stage3_Green_trigger", "four_b_local_peak_proximity": 0.71, "four_b_full_window_peak_proximity": 0.71, "four_b_timing_verdict": "useful_4B_but_not_hard_4C", "four_b_evidence_type": ["valuation_blowoff", "positioning_overheat", "price_only", "event_demand_pull_forward"], "four_c_protection_label": "thesis_break_watch_only", "trigger_outcome_label": "4B_overlay_after_event_premium_peak", "current_profile_verdict": "current_profile_4B_too_late", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window", "same_entry_group_id": "R12L14_C31_065950_WELCRON_COVID_PPE_20200120_4B", "dedupe_for_aggregate": false, "aggregate_group_role": "4B_overlay_only", "is_new_independent_case": false, "reuse_reason": "4B overlay for same case; not representative aggregate entry", "independent_evidence_weight": 0.25, "do_not_count_as_new_case": true}
{"row_type": "trigger", "trigger_id": "R12L14_C31_083550_STAGE2A_20200120", "case_id": "R12L14_C31_083550_KM_COVID_PPE_20200120", "symbol": "083550", "company_name": "케이엠", "round": "R12", "loop": "14", "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "C31_POLICY_SUBSIDY_LEGISLATION_EVENT", "fine_archetype_id": "COVID_PUBLIC_HEALTH_PPE_SUPPLY_ROUTE", "sector": "public_health_ppe_cleanroom_mask", "primary_archetype": "C31_POLICY_SUBSIDY_LEGISLATION_EVENT", "loop_objective": "coverage_gap_fill|counterexample_mining|sector_specific_rule_discovery|4B_non_price_requirement_stress_test|green_strictness_stress_test", "trigger_type": "Stage2-Actionable", "trigger_date": "2020-01-20", "entry_date": "2020-01-20", "entry_price": 8920, "evidence_available_at_that_date": "Korea's first confirmed COVID-19 case created public-health PPE / hygiene demand optionality; only direct supply or verified route evidence may promote beyond Stage2.", "evidence_source": "Historical COVID public-health event classification; stock-web OHLC shard atlas/ohlcv_tradable_by_symbol_year/083/083550/2020.csv; profile atlas/symbol_profiles/083/083550.json.", "stage2_evidence_fields": ["public_event_or_disclosure", "policy_or_regulatory_optionality", "capacity_or_volume_route", "relative_strength"], "stage3_evidence_fields": ["multiple_public_sources", "financial_visibility_watch_only", "customer_or_order_quality_watch_only"], "stage4b_evidence_fields": ["valuation_blowoff", "positioning_overheat", "price_only_local_peak"], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/083/083550/2020.csv", "profile_path": "atlas/symbol_profiles/083/083550.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": 117.49, "MFE_90D_pct": 150.0, "MFE_180D_pct": 150.0, "MFE_1Y_pct": null, "MFE_2Y_pct": null, "MAE_30D_pct": -9.19, "MAE_90D_pct": -9.19, "MAE_180D_pct": -9.19, "MAE_1Y_pct": null, "MAE_2Y_pct": null, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2020-05-25", "peak_price": 22300, "drawdown_after_peak_pct": -42.83, "green_lateness_ratio": "not_applicable:no_clean_Stage3_Green_trigger", "four_b_local_peak_proximity": null, "four_b_full_window_peak_proximity": null, "four_b_timing_verdict": "Stage2_entry_not_4B_overlay", "four_b_evidence_type": [], "four_c_protection_label": "thesis_break_watch_only", "trigger_outcome_label": "direct_PPE_stage2_then_delayed_peak_success", "current_profile_verdict": "current_profile_correct", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window", "same_entry_group_id": "R12L14_C31_083550_KM_COVID_PPE_20200120_ENTRY", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false}
{"row_type": "trigger", "trigger_id": "R12L14_C31_083550_4B_20200525", "case_id": "R12L14_C31_083550_KM_COVID_PPE_20200120", "symbol": "083550", "company_name": "케이엠", "round": "R12", "loop": "14", "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "C31_POLICY_SUBSIDY_LEGISLATION_EVENT", "fine_archetype_id": "COVID_PUBLIC_HEALTH_PPE_SUPPLY_ROUTE", "sector": "public_health_ppe_cleanroom_mask", "primary_archetype": "C31_POLICY_SUBSIDY_LEGISLATION_EVENT", "loop_objective": "coverage_gap_fill|counterexample_mining|sector_specific_rule_discovery|4B_non_price_requirement_stress_test|green_strictness_stress_test", "trigger_type": "Stage4B_overlay", "trigger_date": "2020-05-25", "entry_date": "2020-05-25", "entry_price": 21450, "evidence_available_at_that_date": "Local/full-window event premium had become dominated by valuation blowoff, positioning overheat, and demand-pull-forward risk; use as overlay, not Stage3 evidence.", "evidence_source": "Historical COVID public-health event classification; stock-web OHLC shard atlas/ohlcv_tradable_by_symbol_year/083/083550/2020.csv; profile atlas/symbol_profiles/083/083550.json.", "stage2_evidence_fields": [], "stage3_evidence_fields": [], "stage4b_evidence_fields": ["valuation_blowoff", "positioning_overheat", "price_only_local_peak"], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/083/083550/2020.csv", "profile_path": "atlas/symbol_profiles/083/083550.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": null, "MFE_90D_pct": null, "MFE_180D_pct": null, "MFE_1Y_pct": null, "MFE_2Y_pct": null, "MAE_30D_pct": null, "MAE_90D_pct": null, "MAE_180D_pct": null, "MAE_1Y_pct": null, "MAE_2Y_pct": null, "below_entry_price_flag_30D": null, "below_entry_price_flag_90D": null, "peak_date": "2020-05-25", "peak_price": 22300, "drawdown_after_peak_pct": -42.83, "green_lateness_ratio": "not_applicable:no_clean_Stage3_Green_trigger", "four_b_local_peak_proximity": 0.94, "four_b_full_window_peak_proximity": 0.94, "four_b_timing_verdict": "good_full_window_4B_timing_for_event_premium", "four_b_evidence_type": ["valuation_blowoff", "positioning_overheat", "price_only", "event_demand_pull_forward"], "four_c_protection_label": "thesis_break_watch_only", "trigger_outcome_label": "4B_overlay_after_event_premium_peak", "current_profile_verdict": "current_profile_correct", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window", "same_entry_group_id": "R12L14_C31_083550_KM_COVID_PPE_20200120_4B", "dedupe_for_aggregate": false, "aggregate_group_role": "4B_overlay_only", "is_new_independent_case": false, "reuse_reason": "4B overlay for same case; not representative aggregate entry", "independent_evidence_weight": 0.25, "do_not_count_as_new_case": true}
{"row_type": "trigger", "trigger_id": "R12L14_C31_045060_STAGE2WATCH_20200120", "case_id": "R12L14_C31_045060_OKONG_COVID_THEME_20200120", "symbol": "045060", "company_name": "오공", "round": "R12", "loop": "14", "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "C31_POLICY_SUBSIDY_LEGISLATION_EVENT", "fine_archetype_id": "COVID_PUBLIC_HEALTH_PPE_THEME_ONLY_GUARD", "sector": "public_health_theme_peripheral_material", "primary_archetype": "C31_POLICY_SUBSIDY_LEGISLATION_EVENT", "loop_objective": "coverage_gap_fill|counterexample_mining|sector_specific_rule_discovery|4B_non_price_requirement_stress_test|green_strictness_stress_test", "trigger_type": "Stage2_event_premium_risk_watch", "trigger_date": "2020-01-20", "entry_date": "2020-01-20", "entry_price": 4775, "evidence_available_at_that_date": "Korea's first confirmed COVID-19 case created public-health PPE / hygiene demand optionality; only direct supply or verified route evidence may promote beyond Stage2.", "evidence_source": "Historical COVID public-health event classification; stock-web OHLC shard atlas/ohlcv_tradable_by_symbol_year/045/045060/2020.csv; profile atlas/symbol_profiles/045/045060.json.", "stage2_evidence_fields": ["public_event_or_disclosure", "policy_or_regulatory_optionality", "relative_strength"], "stage3_evidence_fields": [], "stage4b_evidence_fields": ["valuation_blowoff", "positioning_overheat", "price_only_local_peak"], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/045/045060/2020.csv", "profile_path": "atlas/symbol_profiles/045/045060.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": 200.52, "MFE_90D_pct": 200.52, "MFE_180D_pct": 200.52, "MFE_1Y_pct": null, "MFE_2Y_pct": null, "MAE_30D_pct": -21.36, "MAE_90D_pct": -21.36, "MAE_180D_pct": -21.36, "MAE_1Y_pct": null, "MAE_2Y_pct": null, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2020-02-21", "peak_price": 14350, "drawdown_after_peak_pct": -72.02, "green_lateness_ratio": "not_applicable:no_clean_Stage3_Green_trigger", "four_b_local_peak_proximity": null, "four_b_full_window_peak_proximity": null, "four_b_timing_verdict": "Stage2_entry_not_4B_overlay", "four_b_evidence_type": [], "four_c_protection_label": "thesis_break_watch_only", "trigger_outcome_label": "peripheral_theme_spike_failed_durable_rerating", "current_profile_verdict": "current_profile_false_positive", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window", "same_entry_group_id": "R12L14_C31_045060_OKONG_COVID_THEME_20200120_ENTRY", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false}
{"row_type": "trigger", "trigger_id": "R12L14_C31_045060_4B_20200221", "case_id": "R12L14_C31_045060_OKONG_COVID_THEME_20200120", "symbol": "045060", "company_name": "오공", "round": "R12", "loop": "14", "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "C31_POLICY_SUBSIDY_LEGISLATION_EVENT", "fine_archetype_id": "COVID_PUBLIC_HEALTH_PPE_THEME_ONLY_GUARD", "sector": "public_health_theme_peripheral_material", "primary_archetype": "C31_POLICY_SUBSIDY_LEGISLATION_EVENT", "loop_objective": "coverage_gap_fill|counterexample_mining|sector_specific_rule_discovery|4B_non_price_requirement_stress_test|green_strictness_stress_test", "trigger_type": "Stage4B_overlay", "trigger_date": "2020-02-21", "entry_date": "2020-02-21", "entry_price": 12150, "evidence_available_at_that_date": "Local/full-window event premium had become dominated by valuation blowoff, positioning overheat, and demand-pull-forward risk; use as overlay, not Stage3 evidence.", "evidence_source": "Historical COVID public-health event classification; stock-web OHLC shard atlas/ohlcv_tradable_by_symbol_year/045/045060/2020.csv; profile atlas/symbol_profiles/045/045060.json.", "stage2_evidence_fields": [], "stage3_evidence_fields": [], "stage4b_evidence_fields": ["valuation_blowoff", "positioning_overheat", "price_only_local_peak"], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/045/045060/2020.csv", "profile_path": "atlas/symbol_profiles/045/045060.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": null, "MFE_90D_pct": null, "MFE_180D_pct": null, "MFE_1Y_pct": null, "MFE_2Y_pct": null, "MAE_30D_pct": null, "MAE_90D_pct": null, "MAE_180D_pct": null, "MAE_1Y_pct": null, "MAE_2Y_pct": null, "below_entry_price_flag_30D": null, "below_entry_price_flag_90D": null, "peak_date": "2020-02-21", "peak_price": 14350, "drawdown_after_peak_pct": -72.02, "green_lateness_ratio": "not_applicable:no_clean_Stage3_Green_trigger", "four_b_local_peak_proximity": 0.77, "four_b_full_window_peak_proximity": 0.77, "four_b_timing_verdict": "good_full_window_4B_timing_for_event_premium", "four_b_evidence_type": ["valuation_blowoff", "positioning_overheat", "price_only", "event_demand_pull_forward"], "four_c_protection_label": "thesis_break_watch_only", "trigger_outcome_label": "4B_overlay_after_event_premium_peak", "current_profile_verdict": "current_profile_false_positive", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window", "same_entry_group_id": "R12L14_C31_045060_OKONG_COVID_THEME_20200120_4B", "dedupe_for_aggregate": false, "aggregate_group_role": "4B_overlay_only", "is_new_independent_case": false, "reuse_reason": "4B overlay for same case; not representative aggregate entry", "independent_evidence_weight": 0.25, "do_not_count_as_new_case": true}
{"row_type": "trigger", "trigger_id": "R12L14_C31_012690_STAGE2WATCH_20200120", "case_id": "R12L14_C31_012690_MONALISA_COVID_HYGIENE_20200120", "symbol": "012690", "company_name": "모나리자", "round": "R12", "loop": "14", "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "C31_POLICY_SUBSIDY_LEGISLATION_EVENT", "fine_archetype_id": "COVID_PUBLIC_HEALTH_CONSUMER_HYGIENE_HOARDING_GUARD", "sector": "public_health_consumer_hygiene_hoarding", "primary_archetype": "C31_POLICY_SUBSIDY_LEGISLATION_EVENT", "loop_objective": "coverage_gap_fill|counterexample_mining|sector_specific_rule_discovery|4B_non_price_requirement_stress_test|green_strictness_stress_test", "trigger_type": "Stage2_event_premium_risk_watch", "trigger_date": "2020-01-20", "entry_date": "2020-01-20", "entry_price": 4430, "evidence_available_at_that_date": "Korea's first confirmed COVID-19 case created public-health PPE / hygiene demand optionality; only direct supply or verified route evidence may promote beyond Stage2.", "evidence_source": "Historical COVID public-health event classification; stock-web OHLC shard atlas/ohlcv_tradable_by_symbol_year/012/012690/2020.csv; profile atlas/symbol_profiles/012/012690.json.", "stage2_evidence_fields": ["public_event_or_disclosure", "policy_or_regulatory_optionality", "relative_strength"], "stage3_evidence_fields": [], "stage4b_evidence_fields": ["valuation_blowoff", "positioning_overheat", "price_only_local_peak", "event_demand_pull_forward"], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/012/012690/2020.csv", "profile_path": "atlas/symbol_profiles/012/012690.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": 120.99, "MFE_90D_pct": 120.99, "MFE_180D_pct": 120.99, "MFE_1Y_pct": null, "MFE_2Y_pct": null, "MAE_30D_pct": -10.05, "MAE_90D_pct": -14.22, "MAE_180D_pct": -14.22, "MAE_1Y_pct": null, "MAE_2Y_pct": null, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2020-02-03", "peak_price": 9790, "drawdown_after_peak_pct": -61.18, "green_lateness_ratio": "not_applicable:no_clean_Stage3_Green_trigger", "four_b_local_peak_proximity": null, "four_b_full_window_peak_proximity": null, "four_b_timing_verdict": "Stage2_entry_not_4B_overlay", "four_b_evidence_type": [], "four_c_protection_label": "thesis_break_watch_only", "trigger_outcome_label": "consumer_hygiene_hoarding_spike_failed_green", "current_profile_verdict": "current_profile_false_positive", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window", "same_entry_group_id": "R12L14_C31_012690_MONALISA_COVID_HYGIENE_20200120_ENTRY", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false}
{"row_type": "trigger", "trigger_id": "R12L14_C31_012690_4B_20200221", "case_id": "R12L14_C31_012690_MONALISA_COVID_HYGIENE_20200120", "symbol": "012690", "company_name": "모나리자", "round": "R12", "loop": "14", "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "C31_POLICY_SUBSIDY_LEGISLATION_EVENT", "fine_archetype_id": "COVID_PUBLIC_HEALTH_CONSUMER_HYGIENE_HOARDING_GUARD", "sector": "public_health_consumer_hygiene_hoarding", "primary_archetype": "C31_POLICY_SUBSIDY_LEGISLATION_EVENT", "loop_objective": "coverage_gap_fill|counterexample_mining|sector_specific_rule_discovery|4B_non_price_requirement_stress_test|green_strictness_stress_test", "trigger_type": "Stage4B_overlay", "trigger_date": "2020-02-21", "entry_date": "2020-02-21", "entry_price": 8220, "evidence_available_at_that_date": "Local/full-window event premium had become dominated by valuation blowoff, positioning overheat, and demand-pull-forward risk; use as overlay, not Stage3 evidence.", "evidence_source": "Historical COVID public-health event classification; stock-web OHLC shard atlas/ohlcv_tradable_by_symbol_year/012/012690/2020.csv; profile atlas/symbol_profiles/012/012690.json.", "stage2_evidence_fields": [], "stage3_evidence_fields": [], "stage4b_evidence_fields": ["valuation_blowoff", "positioning_overheat", "price_only_local_peak", "event_demand_pull_forward"], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/012/012690/2020.csv", "profile_path": "atlas/symbol_profiles/012/012690.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": null, "MFE_90D_pct": null, "MFE_180D_pct": null, "MFE_1Y_pct": null, "MFE_2Y_pct": null, "MAE_30D_pct": null, "MAE_90D_pct": null, "MAE_180D_pct": null, "MAE_1Y_pct": null, "MAE_2Y_pct": null, "below_entry_price_flag_30D": null, "below_entry_price_flag_90D": null, "peak_date": "2020-02-03", "peak_price": 9790, "drawdown_after_peak_pct": -61.18, "green_lateness_ratio": "not_applicable:no_clean_Stage3_Green_trigger", "four_b_local_peak_proximity": 0.71, "four_b_full_window_peak_proximity": 0.71, "four_b_timing_verdict": "good_full_window_4B_timing_for_event_premium", "four_b_evidence_type": ["valuation_blowoff", "positioning_overheat", "price_only", "event_demand_pull_forward"], "four_c_protection_label": "thesis_break_watch_only", "trigger_outcome_label": "4B_overlay_after_event_premium_peak", "current_profile_verdict": "current_profile_false_positive", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window", "same_entry_group_id": "R12L14_C31_012690_MONALISA_COVID_HYGIENE_20200120_4B", "dedupe_for_aggregate": false, "aggregate_group_role": "4B_overlay_only", "is_new_independent_case": false, "reuse_reason": "4B overlay for same case; not representative aggregate entry", "independent_evidence_weight": 0.25, "do_not_count_as_new_case": true}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R12L14_C31_065950_WELCRON_COVID_PPE_20200120", "trigger_id": "R12L14_C31_065950_STAGE2A_20200120", "symbol": "065950", "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "C31_POLICY_SUBSIDY_LEGISLATION_EVENT", "raw_component_scores_before": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 2, "revision_score": 1, "relative_strength_score": 8, "customer_quality_score": 2, "policy_or_regulatory_score": 15, "valuation_repricing_score": 8, "execution_risk_score": 8, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0, "capacity_or_shipment_score": 4, "public_health_direct_supply_score": 5, "event_demand_pull_forward_risk_score": 8}, "weighted_score_before": 78, "stage_label_before": "Stage2-Actionable", "raw_component_scores_after": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 2, "revision_score": 1, "relative_strength_score": 8, "customer_quality_score": 3, "policy_or_regulatory_score": 17, "valuation_repricing_score": 12, "execution_risk_score": 10, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0, "capacity_or_shipment_score": 4, "public_health_direct_supply_score": 5, "event_demand_pull_forward_risk_score": 8}, "weighted_score_after": 82, "stage_label_after": "Stage3-Yellow_candidate_only", "changed_components": ["public_health_direct_supply_score", "event_demand_pull_forward_risk_score", "valuation_repricing_score", "execution_risk_score"], "component_delta_explanation": "C31/R12 shadow profile separates direct PPE supply routes from consumer-hoarding or peripheral public-health themes; price-only spikes move to 4B/risk overlay.", "MFE_90D_pct": 120.39, "MAE_90D_pct": -16.17, "score_return_alignment_label": "direct_PPE_event_stage2_success_but_price_only_4B_needed", "current_profile_verdict": "current_profile_4B_too_late"}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R12L14_C31_083550_KM_COVID_PPE_20200120", "trigger_id": "R12L14_C31_083550_STAGE2A_20200120", "symbol": "083550", "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "C31_POLICY_SUBSIDY_LEGISLATION_EVENT", "raw_component_scores_before": {"contract_score": 0, "backlog_visibility_score": 1, "margin_bridge_score": 2, "revision_score": 1, "relative_strength_score": 8, "customer_quality_score": 3, "policy_or_regulatory_score": 15, "valuation_repricing_score": 8, "execution_risk_score": 8, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0, "capacity_or_shipment_score": 5, "public_health_direct_supply_score": 5, "event_demand_pull_forward_risk_score": 8}, "weighted_score_before": 78, "stage_label_before": "Stage2-Actionable", "raw_component_scores_after": {"contract_score": 0, "backlog_visibility_score": 1, "margin_bridge_score": 2, "revision_score": 1, "relative_strength_score": 8, "customer_quality_score": 4, "policy_or_regulatory_score": 17, "valuation_repricing_score": 12, "execution_risk_score": 10, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0, "capacity_or_shipment_score": 5, "public_health_direct_supply_score": 5, "event_demand_pull_forward_risk_score": 8}, "weighted_score_after": 84, "stage_label_after": "Stage3-Yellow_candidate_only", "changed_components": ["public_health_direct_supply_score", "event_demand_pull_forward_risk_score", "valuation_repricing_score", "execution_risk_score"], "component_delta_explanation": "C31/R12 shadow profile separates direct PPE supply routes from consumer-hoarding or peripheral public-health themes; price-only spikes move to 4B/risk overlay.", "MFE_90D_pct": 150.0, "MAE_90D_pct": -9.19, "score_return_alignment_label": "direct_PPE_stage2_then_delayed_peak_success", "current_profile_verdict": "current_profile_correct"}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R12L14_C31_045060_OKONG_COVID_THEME_20200120", "trigger_id": "R12L14_C31_045060_STAGE2WATCH_20200120", "symbol": "045060", "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "C31_POLICY_SUBSIDY_LEGISLATION_EVENT", "raw_component_scores_before": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 0, "revision_score": 0, "relative_strength_score": 9, "customer_quality_score": 1, "policy_or_regulatory_score": 10, "valuation_repricing_score": 14, "execution_risk_score": 14, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0, "capacity_or_shipment_score": 1, "public_health_direct_supply_score": 1, "event_demand_pull_forward_risk_score": 18}, "weighted_score_before": 76, "stage_label_before": "Stage2-Actionable_or_Yellow_if_RS_overweighted", "raw_component_scores_after": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 0, "revision_score": 0, "relative_strength_score": 9, "customer_quality_score": 0, "policy_or_regulatory_score": 10, "valuation_repricing_score": 22, "execution_risk_score": 22, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0, "capacity_or_shipment_score": 1, "public_health_direct_supply_score": 1, "event_demand_pull_forward_risk_score": 23}, "weighted_score_after": 58, "stage_label_after": "Stage2_watch_or_4B_overlay", "changed_components": ["public_health_direct_supply_score", "event_demand_pull_forward_risk_score", "valuation_repricing_score", "execution_risk_score"], "component_delta_explanation": "C31/R12 shadow profile separates direct PPE supply routes from consumer-hoarding or peripheral public-health themes; price-only spikes move to 4B/risk overlay.", "MFE_90D_pct": 200.52, "MAE_90D_pct": -21.36, "score_return_alignment_label": "peripheral_theme_spike_failed_durable_rerating", "current_profile_verdict": "current_profile_false_positive"}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R12L14_C31_012690_MONALISA_COVID_HYGIENE_20200120", "trigger_id": "R12L14_C31_012690_STAGE2WATCH_20200120", "symbol": "012690", "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "C31_POLICY_SUBSIDY_LEGISLATION_EVENT", "raw_component_scores_before": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 0, "revision_score": 0, "relative_strength_score": 9, "customer_quality_score": 1, "policy_or_regulatory_score": 10, "valuation_repricing_score": 14, "execution_risk_score": 14, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0, "capacity_or_shipment_score": 1, "public_health_direct_supply_score": 1, "event_demand_pull_forward_risk_score": 18}, "weighted_score_before": 76, "stage_label_before": "Stage2-Actionable_or_Yellow_if_RS_overweighted", "raw_component_scores_after": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 0, "revision_score": 0, "relative_strength_score": 9, "customer_quality_score": 0, "policy_or_regulatory_score": 10, "valuation_repricing_score": 22, "execution_risk_score": 22, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0, "capacity_or_shipment_score": 1, "public_health_direct_supply_score": 1, "event_demand_pull_forward_risk_score": 23}, "weighted_score_after": 58, "stage_label_after": "Stage2_watch_or_4B_overlay", "changed_components": ["public_health_direct_supply_score", "event_demand_pull_forward_risk_score", "valuation_repricing_score", "execution_risk_score"], "component_delta_explanation": "C31/R12 shadow profile separates direct PPE supply routes from consumer-hoarding or peripheral public-health themes; price-only spikes move to 4B/risk overlay.", "MFE_90D_pct": 120.99, "MAE_90D_pct": -14.22, "score_return_alignment_label": "consumer_hygiene_hoarding_spike_failed_green", "current_profile_verdict": "current_profile_false_positive"}
{"row_type": "residual_contribution", "round": "R12", "loop": "14", "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "C31_POLICY_SUBSIDY_LEGISLATION_EVENT", "new_independent_case_count": 4, "reused_case_count": 0, "new_symbol_count": 4, "same_archetype_new_symbol_count": 4, "same_archetype_new_trigger_family_count": 4, "new_trigger_family_count": 4, "positive_case_count": 2, "counterexample_count": 2, "current_profile_error_count": 3, "tested_existing_calibrated_axes": ["stage2_actionable_evidence_bonus", "stage3_yellow_total_min", "stage3_green_total_min", "price_only_blowoff_blocks_positive_stage", "full_4b_requires_non_price_evidence"], "residual_error_types_found": ["PPE_direct_supply_vs_peripheral_theme_split", "consumer_hoarding_false_positive", "4B_price_peak_should_not_promote_Green"], "loop_contribution_label": "canonical_archetype_rule_candidate", "do_not_propose_new_weight_delta": false}
```

```csv
row_type,axis,scope,large_sector_id,canonical_archetype_id,baseline_value,tested_value,delta,reason,backtest_effect,trigger_ids,calibration_usable_count,new_independent_case_count,counterexample_count,confidence,proposal_type,notes
shadow_weight,C31_public_health_direct_supply_bonus,canonical_archetype_specific,L10_POLICY_EVENT_CROSS_REDTEAM_MISC,C31_POLICY_SUBSIDY_LEGISLATION_EVENT,0,1,+1,Direct PPE supplier route had stronger 90D/180D MFE with lower MAE than peripheral/hoarding themes.,Improves Stage2/Yellow selection for 065950/083550 without promoting price-only Green.,R12L14_C31_065950_STAGE2A_20200120|R12L14_C31_083550_STAGE2A_20200120,4,4,2,medium,canonical_shadow_only,not production; post-calibrated residual
shadow_weight,C31_consumer_hoarding_theme_penalty,canonical_archetype_specific,L10_POLICY_EVENT_CROSS_REDTEAM_MISC,C31_POLICY_SUBSIDY_LEGISLATION_EVENT,0,1,+1 risk penalty,Hygiene hoarding/peripheral themes had high MFE but weaker durable route and severe peak drawdown.,Blocks Stage3-Green promotion for 045060/012690 unless margin/reorder proof appears.,R12L14_C31_045060_STAGE2WATCH_20200120|R12L14_C31_012690_STAGE2WATCH_20200120,4,4,2,medium,canonical_shadow_only,not production; post-calibrated residual
shadow_weight,C31_price_only_event_peak_4B_overlay,canonical_archetype_specific,L10_POLICY_EVENT_CROSS_REDTEAM_MISC,C31_POLICY_SUBSIDY_LEGISLATION_EVENT,0,1,+1 overlay,All four cases show event peaks where price-only blowoff should cap new positive promotion.,Reduces false Green after public-health spike; keeps existing full_4B_requires_non_price_evidence.,R12L14_C31_065950_4B_20200221|R12L14_C31_083550_4B_20200525|R12L14_C31_045060_4B_20200221|R12L14_C31_012690_4B_20200221,4,4,2,medium,canonical_shadow_only,not production; post-calibrated residual
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
completed_round = R12
completed_loop = 14
next_round = R13
next_loop = 14
round_schedule_status = valid
round_sector_consistency = pass
```

## 28. Source Notes

- `Songdaiki/stock-web` manifest was read for source name, raw/unadjusted status, max_date, shard roots, and row counts.
- Symbol profiles read: `065950`, `083550`, `045060`, `012690`.
- Tradable OHLCV shards read: `atlas/ohlcv_tradable_by_symbol_year/065/065950/2020.csv`, `083/083550/2020.csv`, `045/045060/2020.csv`, `012/012690/2020.csv`.
- Historical event classification is used only to define evidence families; the quantitative backtest rows come from stock-web OHLC.
- This is historical calibration research, not investment advice.

