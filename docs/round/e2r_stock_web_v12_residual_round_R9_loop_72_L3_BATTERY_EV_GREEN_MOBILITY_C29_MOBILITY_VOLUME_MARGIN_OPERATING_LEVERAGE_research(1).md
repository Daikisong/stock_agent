# E2R Stock-Web Historical Calibration / Sector-Archetype Residual Research Round

## 0. Research Metadata

```text
research_session = post_calibrated_sector_archetype_residual_research
mode = historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12
scheduled_round = R9
scheduled_loop = 72
completed_round = R9
completed_loop = 72
large_sector_id = L3_BATTERY_EV_GREEN_MOBILITY
canonical_archetype_id = C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE
fine_archetype_id = TIRE_SPREAD_OPERATING_LEVERAGE_VS_SUPPLIER_THEME_SPILLOVER
output_file = e2r_stock_web_v12_residual_round_R9_loop_72_L3_BATTERY_EV_GREEN_MOBILITY_C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE_research.md
stock_agent_code_access_allowed = false
stock_agent_code_patch_allowed = false
stock_agent_live_scan_allowed = false
current_stock_discovery_allowed = false
auto_trading_allowed = false
brokerage_api_allowed = false
production_scoring_changed = false
shadow_weight_only = true
handoff_prompt_embedded = true
handoff_prompt_executed_now = false
```

This loop adds 4 new independent cases, 2 counterexamples, and 3 residual errors for R9/L3_BATTERY_EV_GREEN_MOBILITY/C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE.

## 1. Current Calibrated Profile Assumption

The current proxy is `e2r_2_1_stock_web_calibrated_proxy`; the rollback reference is `e2r_2_0_baseline_reference`.

This MD does not re-argue the already applied global Stage2 bonus or Green lateness rules. It stress-tests a C29-specific residual: in mobility/transport, a direct tire spread / ASP / utilization bridge behaved very differently from supplier-theme relative strength without independent margin or FCF conversion evidence.

| applied axis | status in this MD | finding |
|---|---|---|
| stage2_actionable_evidence_bonus | existing_axis_tested | Helpful only when a non-price margin/volume bridge exists. |
| stage3_yellow_total_min | existing_axis_kept | Threshold is acceptable; component composition needs C29 guardrails. |
| stage3_green_total_min / revision_min | existing_axis_kept | Green strictness is not weakened. |
| price_only_blowoff_blocks_positive_stage | existing_axis_strengthened | 한국무브넥스 shows price-only mobility blowoff can be severe. |
| full_4b_requires_non_price_evidence | existing_axis_strengthened | Tire peaks were usable only when valuation/positioning risk had non-price support. |
| hard_4c_thesis_break_routes_to_4c | existing_axis_strengthened | 한온시스템 is a thesis-break watch case when margin/FCF bridge fails. |

## 2. Round / Large Sector / Canonical Archetype Scope

| field | value |
|---|---|
| scheduled_round | R9 |
| scheduled_loop | 72 |
| large_sector_id | L3_BATTERY_EV_GREEN_MOBILITY |
| canonical_archetype_id | C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE |
| fine_archetype_id | TIRE_SPREAD_OPERATING_LEVERAGE_VS_SUPPLIER_THEME_SPILLOVER |
| round_sector_consistency | pass |
| loop_objective | residual_false_positive_mining; residual_missed_structural_mining; 4B_non_price_requirement_stress_test; 4C_thesis_break_timing_test; sector_specific_rule_discovery; canonical_archetype_compression; counterexample_mining; coverage_gap_fill |

R9 is treated as the mobility/transport residual round. This loop remains in `L3_BATTERY_EV_GREEN_MOBILITY` because the cases are tire, EV thermal, and mobility component names. The canonical scope is `C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE`.

## 3. Previous Coverage / Duplicate Avoidance Check

The immediately previous completed local output was R8 / Loop 72, whose next state was R9 / Loop 72. The only prior local R9 file in this workspace was R9 / Loop 71 and used Hyundai Motor, Kia, HL Mando, and Hyundai Wia. This loop avoids those exact symbols and entry families.

```text
scheduled_round = R9
scheduled_loop = 72
round_schedule_status = valid
round_sector_consistency = pass
new_independent_case_count = 4
reused_case_count = 0
new_symbol_count = 4
same_archetype_new_symbol_count = 4
same_archetype_new_trigger_family_count = 4
minimum_new_independent_case_ratio = 1.00
```

Duplicate-risk check:

| duplicate component | result |
|---|---|
| same canonical_archetype_id | allowed |
| same symbol + trigger_date + entry_date as R9 loop71 | not used |
| repeated evidence family from R9 loop71 | avoided: tire spread / thermal supplier / smallcap blowoff are new C29 subfamilies |
| schema rematerialization | no |

## 4. Stock-Web OHLC Input / Price Source Validation

The Stock-Web manifest was read for this run.

| field | value |
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

Price basis for all rows:

```text
price_data_source = Songdaiki/stock-web
price_basis = tradable_raw
price_adjustment_status = raw_unadjusted_marcap
stock_web_manifest_max_date = 2026-02-20
```

## 5. Historical Eligibility Gate

| symbol | company | profile_path | profile status | corporate action status | 180D usable |
|---:|---|---|---|---|---|
| 161390 | 한국타이어앤테크놀로지 | atlas/symbol_profiles/161/161390.json | tradable_ohlcv; active_like | corporate_action_candidate_count=0 | true |
| 073240 | 금호타이어 | atlas/symbol_profiles/073/073240.json | tradable_ohlcv; active_like | old candidates only: 2010, 2018; 2023/2024 window clean | true |
| 018880 | 한온시스템 | atlas/symbol_profiles/018/018880.json | tradable_ohlcv; active_like | 2025/2026 candidates outside 2024 180D window | true |
| 010100 | 한국무브넥스 | atlas/symbol_profiles/010/010100.json | tradable_ohlcv; active_like | old candidates only: 1996/2002/2004/2018; 2023/2024 window clean | true |

All representative entries exist in the tradable shard and have at least 180 trading days before the manifest max date. Corporate-action contaminated 180D windows were not used.

## 6. Canonical Archetype Compression Map

```text
canonical_archetype_id = C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE

fine_archetype compression:
- TIRE_RAW_MATERIAL_SPREAD_ASP_MARGIN_BRIDGE -> C29
- TIRE_TURNAROUND_UTILIZATION_EXPORT_REPAIR_MARGIN -> C29
- EV_THERMAL_SUPPLIER_THEME_WITHOUT_MARGIN_FCF_BRIDGE -> C29
- SMALLCAP_MOBILITY_NAMECHANGE_PRICE_ONLY_BLOWOFF -> C29
```

The compression thesis is simple: C29 should promote mobility names when the evidence bridge is `volume/mix/ASP/margin/FCF`, not when the only evidence is relative strength or general OEM-cycle sympathy.

## 7. Case Selection Summary

| case_id | symbol | company | role | trigger family | new independent | reason |
|---|---:|---|---|---|---|---|
| R9L72_C29_161390_20231101_TIRE_SPREAD_MARGIN_SUCCESS | 161390 | 한국타이어앤테크놀로지 | structural_success | tire spread + ASP/margin bridge | true | high MFE, shallow initial MAE |
| R9L72_C29_073240_20231101_TIRE_TURNAROUND_UTILIZATION_SUCCESS | 073240 | 금호타이어 | structural_success | utilization/export turnaround | true | high MFE, low early MAE |
| R9L72_C29_018880_20240126_THERMAL_SUPPLIER_MARGIN_FAIL | 018880 | 한온시스템 | failed_rerating | EV thermal supplier without margin/FCF bridge | true | low MFE, deep 90D/180D MAE |
| R9L72_C29_010100_20231101_SMALLCAP_MOBILITY_BLOWOFF_FAIL | 010100 | 한국무브넥스 | price_moved_without_evidence | smallcap mobility price-only blowoff | true | severe MAE after relative-strength trigger |

## 8. Positive vs Counterexample Balance

```text
positive_case_count = 2
counterexample_count = 2
4B_case_count = 3
4C_case_count = 1
calibration_usable_case_count = 4
calibration_usable_trigger_count = 8
representative_trigger_count = 4
```

The two positive cases are not generic “auto upcycle” claims. They are tire-specific margin/turnaround cases. The two counterexamples stress the same C29 container from the opposite side: EV/supplier or smallcap mobility evidence was too weak without an independent bridge.

## 9. Evidence Source Map

| evidence family | positive tire cases | supplier / price-only counterexamples |
|---|---|---|
| public_event_or_disclosure | industry recovery, earnings/turnaround context | present, but not enough alone |
| relative_strength | secondary confirmation | dominant but fragile |
| capacity_or_volume_route | utilization/export/replacement tire channel | weak or not independently verified |
| margin_bridge | central evidence | missing or broken |
| financial_visibility | improving | insufficient |
| execution_risk | manageable at trigger | high |
| price-only local peak | not used for promotion | used as guard / 4B overlay |

## 10. Price Data Source Map

| symbol | tradable shard | profile |
|---:|---|---|
| 161390 | atlas/ohlcv_tradable_by_symbol_year/161/161390/2023.csv; atlas/ohlcv_tradable_by_symbol_year/161/161390/2024.csv | atlas/symbol_profiles/161/161390.json |
| 073240 | atlas/ohlcv_tradable_by_symbol_year/073/073240/2023.csv; atlas/ohlcv_tradable_by_symbol_year/073/073240/2024.csv | atlas/symbol_profiles/073/073240.json |
| 018880 | atlas/ohlcv_tradable_by_symbol_year/018/018880/2024.csv | atlas/symbol_profiles/018/018880.json |
| 010100 | atlas/ohlcv_tradable_by_symbol_year/010/010100/2023.csv; atlas/ohlcv_tradable_by_symbol_year/010/010100/2024.csv | atlas/symbol_profiles/010/010100.json |

## 11. Case-by-Case Trigger Grid

| case_id | symbol | company | role | entry | entry_price | MFE30 | MAE30 | MFE90 | MAE90 | MFE180 | MAE180 | peak | current verdict |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---|---|
| R9L72_C29_161390_20231101_TIRE_SPREAD_MARGIN_SUCCESS | 161390 | 한국타이어앤테크놀로지 | positive | 2023-11-01 | 38900 | 24.42 | -4.11 | 53.21 | -4.11 | 53.21 | -4.11 | 2024-02-23 59600 | current_profile_missed_structural |
| R9L72_C29_073240_20231101_TIRE_TURNAROUND_UTILIZATION_SUCCESS | 073240 | 금호타이어 | positive | 2023-11-01 | 4235 | 38.13 | -1.53 | 62.46 | -1.53 | 63.64 | -1.53 | 2024-06-26 6930 | current_profile_correct |
| R9L72_C29_018880_20240126_THERMAL_SUPPLIER_MARGIN_FAIL | 018880 | 한온시스템 | counterexample | 2024-01-26 | 6240 | 5.61 | -4.33 | 8.97 | -21.88 | 8.97 | -39.1 | 2024-05-07 6800 | current_profile_false_positive |
| R9L72_C29_010100_20231101_SMALLCAP_MOBILITY_BLOWOFF_FAIL | 010100 | 한국무브넥스 | counterexample | 2023-11-01 | 8910 | 4.6 | -31.43 | 7.52 | -39.84 | 7.52 | -48.26 | 2023-12-26 9580 | current_profile_false_positive |

## 12. Trigger-Level OHLC Backtest Tables

| trigger_id | symbol | aggregate role | entry_date | entry_price | MFE30 | MAE30 | MFE90 | MAE90 | MFE180 | MAE180 | peak_date | peak_price | drawdown_after_peak |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---|---:|---:|
| T_R9L72_161390_STAGE2_20231101 | 161390 | representative | 2023-11-01 | 38900 | 24.42 | -4.11 | 53.21 | -4.11 | 53.21 | -4.11 | 2024-02-23 | 59600 | -36.49 |
| T_R9L72_073240_STAGE2_20231101 | 073240 | representative | 2023-11-01 | 4235 | 38.13 | -1.53 | 62.46 | -1.53 | 63.64 | -1.53 | 2024-06-26 | 6930 | -38.24 |
| T_R9L72_018880_WATCH_20240126 | 018880 | representative | 2024-01-26 | 6240 | 5.61 | -4.33 | 8.97 | -21.88 | 8.97 | -39.1 | 2024-05-07 | 6800 | -44.12 |
| T_R9L72_010100_WATCH_20231101 | 010100 | representative | 2023-11-01 | 8910 | 4.6 | -31.43 | 7.52 | -39.84 | 7.52 | -48.26 | 2023-12-26 | 9580 | -51.88 |
| T_R9L72_161390_4B_20240223 | 161390 | overlay_only | 2024-02-23 | 58700 | n/a | n/a | n/a | n/a | n/a | n/a | 2024-02-23 | 59600 | -36.49 |
| T_R9L72_073240_4B_20240626 | 073240 | overlay_only | 2024-06-26 | 6860 | n/a | n/a | n/a | n/a | n/a | n/a | 2024-06-26 | 6930 | -38.24 |
| T_R9L72_018880_4C_WATCH_20240613 | 018880 | overlay_only | 2024-06-13 | 4725 | n/a | n/a | n/a | n/a | n/a | n/a | 2024-05-07 | 6800 | -44.12 |
| T_R9L72_010100_4B_20231114 | 010100 | overlay_only | 2023-11-14 | 6700 | n/a | n/a | n/a | n/a | n/a | n/a | 2023-12-26 | 9580 | -51.88 |

Representative rows are deduped into aggregate metrics. Overlay rows are included only for 4B/4C timing audit and do not count as new independent representative entries.

## 13. Current Calibrated Profile Stress Test

| case | current calibrated profile verdict | actual result | residual finding |
|---|---|---|---|
| 161390 한국타이어앤테크놀로지 | current_profile_missed_structural | MFE180 53.21 / MAE180 -4.11 | needs tire/margin bridge boost |
| 073240 금호타이어 | current_profile_correct | MFE180 63.64 / MAE180 -1.53 | needs tire/margin bridge boost |
| 018880 한온시스템 | current_profile_false_positive | MFE180 8.97 / MAE180 -39.1 | must be capped by supplier/price-only guard |
| 010100 한국무브넥스 | current_profile_false_positive | MFE180 7.52 / MAE180 -48.26 | must be capped by supplier/price-only guard |

The current profile is not globally wrong. Its residual problem is C29 composition. It can recognize mobility strength, but without a C29-specific bridge it can over-credit supplier-theme relative strength and under-credit tire spread/ASP evidence.

## 14. Stage2 / Yellow / Green Comparison

Stage2-Actionable worked when a tire spread and utilization bridge existed. Yellow/Green strictness is not weakened. The proposed C29 rule only changes what evidence is allowed to carry the score.

```text
green_lateness_ratio = not_applicable
reason = no separately verified Stage3-Green trigger date used in this MD
```

Positive path:

```text
Stage2-Actionable + margin_bridge + utilization/export evidence
    -> permit Stage3-Yellow if raw score >= 75 and red-team risk low
```

Counterexample path:

```text
relative_strength + general OEM/EV theme only
    -> cap at Stage2-WatchOnly
    -> if price expands without evidence, attach 4B/4C watch overlay
```

## 15. 4B Local vs Full-window Timing Audit

| trigger_id | symbol | evidence type | local peak proximity | full-window proximity | verdict |
|---|---:|---|---:|---:|---|
| T_R9L72_161390_4B_20240223 | 161390 | valuation_blowoff, positioning_overheat | 0.96 | 0.96 | good_full_window_4B_timing |
| T_R9L72_073240_4B_20240626 | 073240 | valuation_blowoff, positioning_overheat | 0.97 | 0.97 | good_full_window_4B_timing |
| T_R9L72_018880_4C_WATCH_20240613 | 018880 | margin_or_backlog_slowdown, thesis_evidence_broken | -2.71 | -2.71 | 4C watch after bridge failure |
| T_R9L72_010100_4B_20231114 | 010100 | price_only_local_peak, positioning_overheat | -3.3 | -3.3 | price-only blowoff; do not promote |

The C29 distinction is visible: tire positives generated usable 4B timing after non-price evidence; price-only smallcap mobility had negative/invalid proximity because the “risk signal” came after entry had already failed, so it should never have been promoted.

## 16. 4C Protection Audit

No hard 4C production rule is proposed from this loop alone.

| symbol | label | reason |
|---:|---|---|
| 018880 | thesis_break_watch_only | margin/FCF bridge failure led to -39.10% 180D MAE from the representative trigger. |
| 010100 | price_only_false_break_watch | price-only mobility blowoff had -48.26% 180D MAE; the correct behavior is watch/guard, not positive promotion. |

## 17. Sector-Specific Rule Candidate

```text
rule_scope = sector_specific
axis = L3_C29_supplier_theme_requires_independent_margin_or_FCF_bridge
candidate = true
```

For L3 mobility names, general OEM/EV sympathy should not promote a supplier unless at least one independent bridge is present:

```text
- confirmed margin expansion
- ASP/raw-material spread improvement
- utilization or volume route tied to that company
- FCF conversion
- direct order/customer quality evidence
```

## 18. Canonical-Archetype Rule Candidate

```text
rule_scope = canonical_archetype_specific
axis = C29_operating_leverage_bridge_required_for_promotion
candidate = true
```

C29 should compress into this archetype rule:

```text
Promotion allowed:
    mobility evidence + margin/volume/ASP/FCF bridge + clean 180D price window

Promotion capped:
    relative strength + OEM/EV theme only
    smallcap mobility name-change or theme-only rerating
    supplier evidence without independent margin bridge
```

## 19. Before / After Backtest Comparison

| profile_id | scope | hypothesis | eligible triggers | selected entries | avg MFE90 | avg MAE90 | avg MFE180 | avg MAE180 | false_positive_rate | missed_structural_count | late_green_count | avg 4B local prox | avg 4B full prox | alignment |
|---|---|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|
| P0 e2r_2_1_stock_web_calibrated_proxy | current proxy | treats supplier relative strength and direct tire margin bridge too similarly | 4 | all representative rows | 33.04 | -16.84 | 33.34 | -23.25 | 50% | 1 | 1 | 0.49 | 0.49 | mixed |
| P0b e2r_2_0_baseline_reference | rollback | slower Stage2 capture; less likely to promote false positives | 2 | 161390,073240 | 57.84 | -2.82 | 58.42 | -2.82 | 0% | 1 | 2 | n/a | n/a | conservative but misses tire turnaround speed |
| P1 sector_specific_candidate_profile | L3 mobility | add tire-spread/margin bridge and supplier-theme guard | 2 | 161390,073240 | 57.84 | -2.82 | 58.42 | -2.82 | 0% | 0 | 1 | 0.97 | 0.97 | improved |
| P2 canonical_archetype_candidate_profile | C29 | require independent margin/FCF bridge for supplier promotion | 2 | 161390,073240 | 57.84 | -2.82 | 58.42 | -2.82 | 0% | 0 | 1 | 0.97 | 0.97 | best |
| P3 counterexample_guard_profile | C29 guard | block price-only smallcap mobility blowoff and EV supplier without margin bridge | 2 | 161390,073240 | 57.84 | -2.82 | 58.42 | -2.82 | 0% | 0 | 1 | 0.97 | 0.97 | best drawdown control |


## 20. Score-Return Alignment Matrix

| symbol | before stage | after shadow stage | MFE180 / MAE180 | alignment |
|---:|---|---|---|---|
| 161390 | Stage2-Actionable | Stage3-Yellow | 53.21 / -4.11 | after better captures missed tire spread structural |
| 073240 | Stage3-Yellow | Stage3-Yellow | 63.64 / -1.53 | kept; score composition improved |
| 018880 | Stage3-Yellow | Stage2-WatchOnly | 8.97 / -39.1 | after blocks high-MAE supplier false positive |
| 010100 | Stage2-Actionable | Stage2-WatchOnly | 7.52 / -48.26 | after blocks price-only blowoff |

## 21. Coverage Matrix

| large_sector_id | canonical_archetype_id | fine_archetype_id | positive_case_count | counterexample_count | 4B_case_count | 4C_case_count | new_independent_case_count | reused_case_count | calibration_usable_trigger_count | representative_trigger_count | current_profile_error_count | sector_rule_candidate | canonical_rule_candidate | coverage_gap_after_this_loop |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|---|---|
| L3_BATTERY_EV_GREEN_MOBILITY | C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE | TIRE_SPREAD_OPERATING_LEVERAGE_VS_SUPPLIER_THEME_SPILLOVER | 2 | 2 | 3 | 1 | 4 | 0 | 8 | 4 | 3 | true | true | partially closed: tire spread positives and supplier spillover counterexamples added |


## 22. Residual Contribution Summary

```text
new_independent_case_count: 4
reused_case_count: 0
reused_case_ids: []
new_symbol_count: 4
new_canonical_archetype_count: 0
new_fine_archetype_count: 4
new_trigger_family_count: 4
tested_existing_calibrated_axes:
  - stage2_actionable_evidence_bonus
  - price_only_blowoff_blocks_positive_stage
  - full_4b_requires_non_price_evidence
  - hard_4c_thesis_break_routes_to_4c
residual_error_types_found:
  - residual_missed_structural_mining
  - residual_false_positive_mining
  - 4B_price_only_too_early
  - 4C_thesis_break_watch
new_axis_proposed:
  - C29_tire_spread_margin_bridge_bonus
  - C29_supplier_theme_without_margin_bridge_penalty
  - C29_price_only_mobility_blowoff_guard
existing_axis_strengthened:
  - price_only_blowoff_blocks_positive_stage
  - full_4b_requires_non_price_evidence
  - hard_4c_thesis_break_routes_to_4c
existing_axis_weakened: null
existing_axis_kept:
  - stage3_yellow_total_min
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
- stock-web manifest max_date and price basis
- ticker profile availability
- clean 180D calibration windows
- entry_date and entry_price from tradable shards
- MFE/MAE 30D/90D/180D using actual OHLC values observed in stock-web rows
- representative-row dedupe logic
- positive/counterexample balance
- C29-specific rule candidate scope
```

Not validated:

```text
- live current candidate status
- production stock_agent scoring code
- broker/API data
- adjusted-price performance
- intraday evidence timing
- exact production score implementation
```

## 24. Shadow Weight Calibration

```csv
row_type,axis,scope,large_sector_id,canonical_archetype_id,baseline_value,tested_value,delta,reason,backtest_effect,trigger_ids,calibration_usable_count,new_independent_case_count,counterexample_count,confidence,proposal_type,notes
shadow_weight,C29_tire_spread_margin_bridge_bonus,canonical_archetype_specific,L3_BATTERY_EV_GREEN_MOBILITY,C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE,0,1,+1,"Tire cases with ASP/raw-material spread + utilization + revision bridge had high MFE and low initial MAE","keeps 161390/073240 promotable; does not affect price-only rows","T_R9L72_161390_STAGE2_20231101|T_R9L72_073240_STAGE2_20231101",4,4,2,medium,canonical_shadow_only,"not production; post-calibrated residual"
shadow_weight,C29_supplier_theme_without_margin_bridge_penalty,canonical_archetype_specific,L3_BATTERY_EV_GREEN_MOBILITY,C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE,0,-2,-2,"Supplier theme/relative strength without independent margin or FCF bridge produced high MAE false positives","blocks 018880 and 010100 from Stage2/3 promotion","T_R9L72_018880_WATCH_20240126|T_R9L72_010100_WATCH_20231101",4,4,2,medium,canonical_shadow_only,"not production; post-calibrated residual"
shadow_weight,C29_price_only_mobility_blowoff_guard,sector_specific,L3_BATTERY_EV_GREEN_MOBILITY,C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE,0,1,+1,"Smallcap mobility price-only moves should be 4B/watch, not positive promotion","reduces high-MAE price-only entries","T_R9L72_010100_WATCH_20231101|T_R9L72_010100_4B_20231114",4,4,2,medium,sector_shadow_only,"strengthens existing price-only blowoff guard in C29 context"
```

These are shadow-only candidates. No production scoring is changed.

## 25. Machine-Readable Rows

### 25.1 price_source_validation
```jsonl
{"row_type": "price_source_validation", "source": "Songdaiki/stock-web", "source_url": "https://github.com/Songdaiki/stock-web", "manifest_path": "atlas/manifest.json", "schema_path": "atlas/schema.json", "universe_path": "atlas/universe/all_symbols.csv", "manifest_max_date": "2026-02-20", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "raw_shard_root": "atlas/ohlcv_raw_by_symbol_year", "validation_status": "usable_for_historical_calibration"}
```

### 25.2 case rows
```jsonl
{"row_type": "case", "case_id": "R9L72_C29_161390_20231101_TIRE_SPREAD_MARGIN_SUCCESS", "symbol": "161390", "company_name": "한국타이어앤테크놀로지", "round": "R9", "loop": "72", "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE", "fine_archetype_id": "TIRE_RAW_MATERIAL_SPREAD_ASP_MARGIN_BRIDGE", "case_type": "structural_success", "positive_or_counterexample": "positive", "best_trigger": "T_R9L72_161390_STAGE2_20231101", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "aligned", "current_profile_verdict": "current_profile_missed_structural", "price_source": "Songdaiki/stock-web", "notes": "Profile has zero corporate-action candidates; 180D window clean."}
{"row_type": "case", "case_id": "R9L72_C29_073240_20231101_TIRE_TURNAROUND_UTILIZATION_SUCCESS", "symbol": "073240", "company_name": "금호타이어", "round": "R9", "loop": "72", "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE", "fine_archetype_id": "TIRE_TURNAROUND_UTILIZATION_EXPORT_REPAIR_MARGIN", "case_type": "structural_success", "positive_or_counterexample": "positive", "best_trigger": "T_R9L72_073240_STAGE2_20231101", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "aligned", "current_profile_verdict": "current_profile_correct", "price_source": "Songdaiki/stock-web", "notes": "Profile corporate-action candidates are old 2010/2018 dates; 2023-11 to 2024-07 180D window clean."}
{"row_type": "case", "case_id": "R9L72_C29_018880_20240126_THERMAL_SUPPLIER_MARGIN_FAIL", "symbol": "018880", "company_name": "한온시스템", "round": "R9", "loop": "72", "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE", "fine_archetype_id": "EV_THERMAL_SUPPLIER_THEME_WITHOUT_MARGIN_FCF_BRIDGE", "case_type": "failed_rerating", "positive_or_counterexample": "counterexample", "best_trigger": "T_R9L72_018880_WATCH_20240126", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "misaligned_current_profile", "current_profile_verdict": "current_profile_false_positive", "price_source": "Songdaiki/stock-web", "notes": "Profile has corporate-action candidates in 2025/2026, outside the 2024 180D calibration window."}
{"row_type": "case", "case_id": "R9L72_C29_010100_20231101_SMALLCAP_MOBILITY_BLOWOFF_FAIL", "symbol": "010100", "company_name": "한국무브넥스", "round": "R9", "loop": "72", "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE", "fine_archetype_id": "SMALLCAP_MOBILITY_NAMECHANGE_PRICE_ONLY_BLOWOFF", "case_type": "price_moved_without_evidence", "positive_or_counterexample": "counterexample", "best_trigger": "T_R9L72_010100_WATCH_20231101", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "misaligned_current_profile", "current_profile_verdict": "current_profile_false_positive", "price_source": "Songdaiki/stock-web", "notes": "Profile corporate-action candidates are old 1996/2002/2004/2018 dates; 2023-11 to 2024-07 window clean."}
```

### 25.3 trigger rows
```jsonl
{"row_type": "trigger", "trigger_id": "T_R9L72_161390_STAGE2_20231101", "case_id": "R9L72_C29_161390_20231101_TIRE_SPREAD_MARGIN_SUCCESS", "symbol": "161390", "company_name": "한국타이어앤테크놀로지", "round": "R9", "loop": "72", "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE", "fine_archetype_id": "TIRE_RAW_MATERIAL_SPREAD_ASP_MARGIN_BRIDGE", "sector": "tire_mobility_supplier", "primary_archetype": "tire_spread_operating_leverage", "loop_objective": "sector_specific_rule_discovery|canonical_archetype_compression|counterexample_mining|coverage_gap_fill", "trigger_type": "Stage2-Actionable", "trigger_date": "2023-11-01", "evidence_available_at_that_date": "2023년 말 타이어 원재료비 안정, ASP/mix, 수출·교체용 수요 회복, 실적 가시성이 함께 관찰된 구간. 단순 완성차 테마가 아니라 margin bridge가 있었다.", "evidence_source": "public historical evidence proxy + stock-web OHLC rows in atlas/ohlcv_tradable_by_symbol_year/161/161390/2023.csv|atlas/ohlcv_tradable_by_symbol_year/161/161390/2024.csv", "stage2_evidence_fields": ["public_event_or_disclosure", "relative_strength", "early_revision_signal"], "stage3_evidence_fields": ["confirmed_revision", "margin_bridge", "financial_visibility"], "stage4b_evidence_fields": ["valuation_blowoff", "positioning_overheat"], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/161/161390/2023.csv|atlas/ohlcv_tradable_by_symbol_year/161/161390/2024.csv", "profile_path": "atlas/symbol_profiles/161/161390.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "entry_date": "2023-11-01", "entry_price": 38900, "MFE_30D_pct": 24.42, "MFE_90D_pct": 53.21, "MFE_180D_pct": 53.21, "MFE_1Y_pct": null, "MFE_2Y_pct": null, "MAE_30D_pct": -4.11, "MAE_90D_pct": -4.11, "MAE_180D_pct": -4.11, "MAE_1Y_pct": null, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2024-02-23", "peak_price": 59600, "drawdown_after_peak_pct": -36.49, "green_lateness_ratio": "not_applicable:no_confirmed_Stage3_Green_trigger", "four_b_local_peak_proximity": null, "four_b_full_window_peak_proximity": null, "four_b_timing_verdict": "not_primary_4B_row", "four_b_evidence_type": ["valuation_blowoff", "positioning_overheat"], "four_c_protection_label": "not_applicable", "trigger_outcome_label": "structural_success_margin_bridge", "current_profile_verdict": "current_profile_missed_structural", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window", "same_entry_group_id": "161390_2023-11-01_38900", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false}
{"row_type": "trigger", "trigger_id": "T_R9L72_073240_STAGE2_20231101", "case_id": "R9L72_C29_073240_20231101_TIRE_TURNAROUND_UTILIZATION_SUCCESS", "symbol": "073240", "company_name": "금호타이어", "round": "R9", "loop": "72", "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE", "fine_archetype_id": "TIRE_TURNAROUND_UTILIZATION_EXPORT_REPAIR_MARGIN", "sector": "tire_mobility_supplier", "primary_archetype": "tire_turnaround_operating_leverage", "loop_objective": "sector_specific_rule_discovery|canonical_archetype_compression|counterexample_mining|coverage_gap_fill", "trigger_type": "Stage2-Actionable", "trigger_date": "2023-11-01", "evidence_available_at_that_date": "회복형 타이어 케이스. 가동률/수출/스프레드 회복이 함께 붙어 단순 테마보다 영업레버리지 성격이 강했다.", "evidence_source": "public historical evidence proxy + stock-web OHLC rows in atlas/ohlcv_tradable_by_symbol_year/073/073240/2023.csv|atlas/ohlcv_tradable_by_symbol_year/073/073240/2024.csv", "stage2_evidence_fields": ["public_event_or_disclosure", "relative_strength", "capacity_or_volume_route", "early_revision_signal"], "stage3_evidence_fields": ["confirmed_revision", "margin_bridge", "financial_visibility"], "stage4b_evidence_fields": ["valuation_blowoff", "positioning_overheat"], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/073/073240/2023.csv|atlas/ohlcv_tradable_by_symbol_year/073/073240/2024.csv", "profile_path": "atlas/symbol_profiles/073/073240.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "entry_date": "2023-11-01", "entry_price": 4235, "MFE_30D_pct": 38.13, "MFE_90D_pct": 62.46, "MFE_180D_pct": 63.64, "MFE_1Y_pct": null, "MFE_2Y_pct": null, "MAE_30D_pct": -1.53, "MAE_90D_pct": -1.53, "MAE_180D_pct": -1.53, "MAE_1Y_pct": null, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2024-06-26", "peak_price": 6930, "drawdown_after_peak_pct": -38.24, "green_lateness_ratio": "not_applicable:no_confirmed_Stage3_Green_trigger", "four_b_local_peak_proximity": null, "four_b_full_window_peak_proximity": null, "four_b_timing_verdict": "not_primary_4B_row", "four_b_evidence_type": ["valuation_blowoff", "positioning_overheat"], "four_c_protection_label": "not_applicable", "trigger_outcome_label": "structural_success_high_MFE_low_initial_MAE", "current_profile_verdict": "current_profile_correct", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window", "same_entry_group_id": "073240_2023-11-01_4235", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false}
{"row_type": "trigger", "trigger_id": "T_R9L72_018880_WATCH_20240126", "case_id": "R9L72_C29_018880_20240126_THERMAL_SUPPLIER_MARGIN_FAIL", "symbol": "018880", "company_name": "한온시스템", "round": "R9", "loop": "72", "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE", "fine_archetype_id": "EV_THERMAL_SUPPLIER_THEME_WITHOUT_MARGIN_FCF_BRIDGE", "sector": "thermal_mobility_supplier", "primary_archetype": "supplier_spillover_without_margin_bridge", "loop_objective": "sector_specific_rule_discovery|canonical_archetype_compression|counterexample_mining|coverage_gap_fill", "trigger_type": "Stage2-WatchOnly", "trigger_date": "2024-01-26", "evidence_available_at_that_date": "EV 열관리/대형 부품주라는 서사는 있었지만, trigger 시점에는 독립적 margin bridge, FCF 전환, 레버리지 개선 증거가 약했다.", "evidence_source": "public historical evidence proxy + stock-web OHLC rows in atlas/ohlcv_tradable_by_symbol_year/018/018880/2024.csv", "stage2_evidence_fields": ["public_event_or_disclosure", "relative_strength"], "stage3_evidence_fields": [], "stage4b_evidence_fields": ["margin_or_backlog_slowdown", "positioning_overheat"], "stage4c_evidence_fields": ["thesis_evidence_broken"], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/018/018880/2024.csv", "profile_path": "atlas/symbol_profiles/018/018880.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "entry_date": "2024-01-26", "entry_price": 6240, "MFE_30D_pct": 5.61, "MFE_90D_pct": 8.97, "MFE_180D_pct": 8.97, "MFE_1Y_pct": null, "MFE_2Y_pct": null, "MAE_30D_pct": -4.33, "MAE_90D_pct": -21.88, "MAE_180D_pct": -39.1, "MAE_1Y_pct": null, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2024-05-07", "peak_price": 6800, "drawdown_after_peak_pct": -44.12, "green_lateness_ratio": "not_applicable:no_confirmed_Stage3_Green_trigger", "four_b_local_peak_proximity": null, "four_b_full_window_peak_proximity": null, "four_b_timing_verdict": "not_primary_4B_row", "four_b_evidence_type": ["margin_or_backlog_slowdown", "positioning_overheat"], "four_c_protection_label": "thesis_break_watch_only", "trigger_outcome_label": "failed_rerating_high_MAE", "current_profile_verdict": "current_profile_false_positive", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window", "same_entry_group_id": "018880_2024-01-26_6240", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false}
{"row_type": "trigger", "trigger_id": "T_R9L72_010100_WATCH_20231101", "case_id": "R9L72_C29_010100_20231101_SMALLCAP_MOBILITY_BLOWOFF_FAIL", "symbol": "010100", "company_name": "한국무브넥스", "round": "R9", "loop": "72", "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE", "fine_archetype_id": "SMALLCAP_MOBILITY_NAMECHANGE_PRICE_ONLY_BLOWOFF", "sector": "smallcap_mobility_supplier", "primary_archetype": "price_only_mobility_supplier_blowoff", "loop_objective": "sector_specific_rule_discovery|canonical_archetype_compression|counterexample_mining|coverage_gap_fill", "trigger_type": "Stage2-WatchOnly", "trigger_date": "2023-11-01", "evidence_available_at_that_date": "모빌리티 명칭/소형 부품주 상대강도는 있었지만, 독립적 수주·마진·FCF 브리지가 약했다. 가격만 먼저 달린 케이스.", "evidence_source": "public historical evidence proxy + stock-web OHLC rows in atlas/ohlcv_tradable_by_symbol_year/010/010100/2023.csv|atlas/ohlcv_tradable_by_symbol_year/010/010100/2024.csv", "stage2_evidence_fields": ["relative_strength", "public_event_or_disclosure"], "stage3_evidence_fields": [], "stage4b_evidence_fields": ["price_only_local_peak", "positioning_overheat"], "stage4c_evidence_fields": ["thesis_evidence_broken"], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/010/010100/2023.csv|atlas/ohlcv_tradable_by_symbol_year/010/010100/2024.csv", "profile_path": "atlas/symbol_profiles/010/010100.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "entry_date": "2023-11-01", "entry_price": 8910, "MFE_30D_pct": 4.6, "MFE_90D_pct": 7.52, "MFE_180D_pct": 7.52, "MFE_1Y_pct": null, "MFE_2Y_pct": null, "MAE_30D_pct": -31.43, "MAE_90D_pct": -39.84, "MAE_180D_pct": -48.26, "MAE_1Y_pct": null, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2023-12-26", "peak_price": 9580, "drawdown_after_peak_pct": -51.88, "green_lateness_ratio": "not_applicable:no_confirmed_Stage3_Green_trigger", "four_b_local_peak_proximity": null, "four_b_full_window_peak_proximity": null, "four_b_timing_verdict": "not_primary_4B_row", "four_b_evidence_type": ["price_only_local_peak", "positioning_overheat"], "four_c_protection_label": "thesis_break_watch_only", "trigger_outcome_label": "price_only_false_positive_high_MAE", "current_profile_verdict": "current_profile_false_positive", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window", "same_entry_group_id": "010100_2023-11-01_8910", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false}
{"row_type": "trigger", "trigger_id": "T_R9L72_161390_4B_20240223", "case_id": "R9L72_C29_161390_20231101_TIRE_SPREAD_MARGIN_SUCCESS", "symbol": "161390", "company_name": "한국타이어앤테크놀로지", "round": "R9", "loop": "72", "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE", "fine_archetype_id": "TIRE_RAW_MATERIAL_SPREAD_ASP_MARGIN_BRIDGE", "sector": "tire_mobility_supplier", "primary_archetype": "tire_spread_operating_leverage", "loop_objective": "4B_non_price_requirement_stress_test|4C_thesis_break_timing_test", "trigger_type": "Stage4B-Overlay", "trigger_date": "2024-02-23", "evidence_available_at_that_date": "risk overlay row; not representative for aggregate entry performance", "evidence_source": "stock-web OHLC rows in atlas/ohlcv_tradable_by_symbol_year/161/161390/2023.csv|atlas/ohlcv_tradable_by_symbol_year/161/161390/2024.csv plus historical risk evidence proxy", "stage2_evidence_fields": [], "stage3_evidence_fields": [], "stage4b_evidence_fields": ["valuation_blowoff", "positioning_overheat"], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/161/161390/2023.csv|atlas/ohlcv_tradable_by_symbol_year/161/161390/2024.csv", "profile_path": "atlas/symbol_profiles/161/161390.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "entry_date": "2024-02-23", "entry_price": 58700, "MFE_30D_pct": null, "MFE_90D_pct": null, "MFE_180D_pct": null, "MFE_1Y_pct": null, "MFE_2Y_pct": null, "MAE_30D_pct": null, "MAE_90D_pct": null, "MAE_180D_pct": null, "MAE_1Y_pct": null, "below_entry_price_flag_30D": null, "below_entry_price_flag_90D": null, "peak_date": "2024-02-23", "peak_price": 59600, "drawdown_after_peak_pct": -36.49, "green_lateness_ratio": "not_applicable:overlay_only", "four_b_local_peak_proximity": 0.96, "four_b_full_window_peak_proximity": 0.96, "four_b_timing_verdict": "good_full_window_4B_timing", "four_b_evidence_type": ["valuation_blowoff", "positioning_overheat"], "four_c_protection_label": "not_applicable", "trigger_outcome_label": "risk_overlay_only", "current_profile_verdict": "current_profile_missed_structural", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window", "same_entry_group_id": "161390_2024-02-23_58700", "dedupe_for_aggregate": false, "aggregate_group_role": "4B_overlay_only", "is_new_independent_case": false, "reuse_reason": "overlay_row_for_timing_audit", "independent_evidence_weight": 0.0, "do_not_count_as_new_case": true}
{"row_type": "trigger", "trigger_id": "T_R9L72_073240_4B_20240626", "case_id": "R9L72_C29_073240_20231101_TIRE_TURNAROUND_UTILIZATION_SUCCESS", "symbol": "073240", "company_name": "금호타이어", "round": "R9", "loop": "72", "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE", "fine_archetype_id": "TIRE_TURNAROUND_UTILIZATION_EXPORT_REPAIR_MARGIN", "sector": "tire_mobility_supplier", "primary_archetype": "tire_turnaround_operating_leverage", "loop_objective": "4B_non_price_requirement_stress_test|4C_thesis_break_timing_test", "trigger_type": "Stage4B-Overlay", "trigger_date": "2024-06-26", "evidence_available_at_that_date": "risk overlay row; not representative for aggregate entry performance", "evidence_source": "stock-web OHLC rows in atlas/ohlcv_tradable_by_symbol_year/073/073240/2023.csv|atlas/ohlcv_tradable_by_symbol_year/073/073240/2024.csv plus historical risk evidence proxy", "stage2_evidence_fields": [], "stage3_evidence_fields": [], "stage4b_evidence_fields": ["valuation_blowoff", "positioning_overheat"], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/073/073240/2023.csv|atlas/ohlcv_tradable_by_symbol_year/073/073240/2024.csv", "profile_path": "atlas/symbol_profiles/073/073240.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "entry_date": "2024-06-26", "entry_price": 6860, "MFE_30D_pct": null, "MFE_90D_pct": null, "MFE_180D_pct": null, "MFE_1Y_pct": null, "MFE_2Y_pct": null, "MAE_30D_pct": null, "MAE_90D_pct": null, "MAE_180D_pct": null, "MAE_1Y_pct": null, "below_entry_price_flag_30D": null, "below_entry_price_flag_90D": null, "peak_date": "2024-06-26", "peak_price": 6930, "drawdown_after_peak_pct": -38.24, "green_lateness_ratio": "not_applicable:overlay_only", "four_b_local_peak_proximity": 0.97, "four_b_full_window_peak_proximity": 0.97, "four_b_timing_verdict": "good_full_window_4B_timing", "four_b_evidence_type": ["valuation_blowoff", "positioning_overheat"], "four_c_protection_label": "not_applicable", "trigger_outcome_label": "risk_overlay_only", "current_profile_verdict": "current_profile_correct", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window", "same_entry_group_id": "073240_2024-06-26_6860", "dedupe_for_aggregate": false, "aggregate_group_role": "4B_overlay_only", "is_new_independent_case": false, "reuse_reason": "overlay_row_for_timing_audit", "independent_evidence_weight": 0.0, "do_not_count_as_new_case": true}
{"row_type": "trigger", "trigger_id": "T_R9L72_018880_4C_WATCH_20240613", "case_id": "R9L72_C29_018880_20240126_THERMAL_SUPPLIER_MARGIN_FAIL", "symbol": "018880", "company_name": "한온시스템", "round": "R9", "loop": "72", "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE", "fine_archetype_id": "EV_THERMAL_SUPPLIER_THEME_WITHOUT_MARGIN_FCF_BRIDGE", "sector": "thermal_mobility_supplier", "primary_archetype": "supplier_spillover_without_margin_bridge", "loop_objective": "4B_non_price_requirement_stress_test|4C_thesis_break_timing_test", "trigger_type": "Stage4C-Watch", "trigger_date": "2024-06-13", "evidence_available_at_that_date": "risk overlay row; not representative for aggregate entry performance", "evidence_source": "stock-web OHLC rows in atlas/ohlcv_tradable_by_symbol_year/018/018880/2024.csv plus historical risk evidence proxy", "stage2_evidence_fields": [], "stage3_evidence_fields": [], "stage4b_evidence_fields": ["margin_or_backlog_slowdown", "thesis_evidence_broken"], "stage4c_evidence_fields": ["thesis_evidence_broken"], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/018/018880/2024.csv", "profile_path": "atlas/symbol_profiles/018/018880.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "entry_date": "2024-06-13", "entry_price": 4725, "MFE_30D_pct": null, "MFE_90D_pct": null, "MFE_180D_pct": null, "MFE_1Y_pct": null, "MFE_2Y_pct": null, "MAE_30D_pct": null, "MAE_90D_pct": null, "MAE_180D_pct": null, "MAE_1Y_pct": null, "below_entry_price_flag_30D": null, "below_entry_price_flag_90D": null, "peak_date": "2024-05-07", "peak_price": 6800, "drawdown_after_peak_pct": -44.12, "green_lateness_ratio": "not_applicable:overlay_only", "four_b_local_peak_proximity": -2.71, "four_b_full_window_peak_proximity": -2.71, "four_b_timing_verdict": "4C_watch_after_bridge_failure", "four_b_evidence_type": ["margin_or_backlog_slowdown", "thesis_evidence_broken"], "four_c_protection_label": "thesis_break_watch_only", "trigger_outcome_label": "risk_overlay_only", "current_profile_verdict": "current_profile_false_positive", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window", "same_entry_group_id": "018880_2024-06-13_4725", "dedupe_for_aggregate": false, "aggregate_group_role": "4C_overlay_only", "is_new_independent_case": false, "reuse_reason": "overlay_row_for_timing_audit", "independent_evidence_weight": 0.0, "do_not_count_as_new_case": true}
{"row_type": "trigger", "trigger_id": "T_R9L72_010100_4B_20231114", "case_id": "R9L72_C29_010100_20231101_SMALLCAP_MOBILITY_BLOWOFF_FAIL", "symbol": "010100", "company_name": "한국무브넥스", "round": "R9", "loop": "72", "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE", "fine_archetype_id": "SMALLCAP_MOBILITY_NAMECHANGE_PRICE_ONLY_BLOWOFF", "sector": "smallcap_mobility_supplier", "primary_archetype": "price_only_mobility_supplier_blowoff", "loop_objective": "4B_non_price_requirement_stress_test|4C_thesis_break_timing_test", "trigger_type": "Stage4B-Overlay", "trigger_date": "2023-11-14", "evidence_available_at_that_date": "risk overlay row; not representative for aggregate entry performance", "evidence_source": "stock-web OHLC rows in atlas/ohlcv_tradable_by_symbol_year/010/010100/2023.csv|atlas/ohlcv_tradable_by_symbol_year/010/010100/2024.csv plus historical risk evidence proxy", "stage2_evidence_fields": [], "stage3_evidence_fields": [], "stage4b_evidence_fields": ["price_only_local_peak", "positioning_overheat"], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/010/010100/2023.csv|atlas/ohlcv_tradable_by_symbol_year/010/010100/2024.csv", "profile_path": "atlas/symbol_profiles/010/010100.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "entry_date": "2023-11-14", "entry_price": 6700, "MFE_30D_pct": null, "MFE_90D_pct": null, "MFE_180D_pct": null, "MFE_1Y_pct": null, "MFE_2Y_pct": null, "MAE_30D_pct": null, "MAE_90D_pct": null, "MAE_180D_pct": null, "MAE_1Y_pct": null, "below_entry_price_flag_30D": null, "below_entry_price_flag_90D": null, "peak_date": "2023-12-26", "peak_price": 9580, "drawdown_after_peak_pct": -51.88, "green_lateness_ratio": "not_applicable:overlay_only", "four_b_local_peak_proximity": -3.3, "four_b_full_window_peak_proximity": -3.3, "four_b_timing_verdict": "price_only_blowoff_do_not_promote", "four_b_evidence_type": ["price_only_local_peak", "positioning_overheat"], "four_c_protection_label": "not_applicable", "trigger_outcome_label": "risk_overlay_only", "current_profile_verdict": "current_profile_false_positive", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window", "same_entry_group_id": "010100_2023-11-14_6700", "dedupe_for_aggregate": false, "aggregate_group_role": "4B_overlay_only", "is_new_independent_case": false, "reuse_reason": "overlay_row_for_timing_audit", "independent_evidence_weight": 0.0, "do_not_count_as_new_case": true}
```

### 25.4 score_simulation rows
```jsonl
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R9L72_C29_161390_20231101_TIRE_SPREAD_MARGIN_SUCCESS", "trigger_id": "T_R9L72_161390_STAGE2_20231101", "symbol": "161390", "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE", "raw_component_scores_before": {"contract_score": 1, "backlog_visibility_score": 1, "margin_bridge_score": 6, "revision_score": 5, "relative_strength_score": 5, "customer_quality_score": 2, "policy_or_regulatory_score": 0, "valuation_repricing_score": 3, "execution_risk_score": 2, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_before": 74, "stage_label_before": "Stage2-Actionable", "raw_component_scores_after": {"contract_score": 1, "backlog_visibility_score": 1, "margin_bridge_score": 8, "revision_score": 7, "relative_strength_score": 5, "customer_quality_score": 2, "policy_or_regulatory_score": 0, "valuation_repricing_score": 3, "execution_risk_score": 1, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0, "tire_spread_score": 8, "fcf_conversion_score": 6}, "weighted_score_after": 84, "stage_label_after": "Stage3-Yellow", "changed_components": ["margin_bridge_score", "revision_score", "execution_risk_score", "tire_spread_score", "fcf_conversion_score"], "component_delta_explanation": "Add tire spread / utilization / FCF conversion bridge.", "MFE_90D_pct": 53.21, "MAE_90D_pct": -4.11, "score_return_alignment_label": "improved_positive_capture", "current_profile_verdict": "current_profile_missed_structural"}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R9L72_C29_073240_20231101_TIRE_TURNAROUND_UTILIZATION_SUCCESS", "trigger_id": "T_R9L72_073240_STAGE2_20231101", "symbol": "073240", "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE", "raw_component_scores_before": {"contract_score": 0, "backlog_visibility_score": 1, "margin_bridge_score": 5, "revision_score": 4, "relative_strength_score": 6, "customer_quality_score": 2, "policy_or_regulatory_score": 0, "valuation_repricing_score": 4, "execution_risk_score": 3, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_before": 76, "stage_label_before": "Stage3-Yellow", "raw_component_scores_after": {"contract_score": 0, "backlog_visibility_score": 1, "margin_bridge_score": 8, "revision_score": 6, "relative_strength_score": 6, "customer_quality_score": 2, "policy_or_regulatory_score": 0, "valuation_repricing_score": 4, "execution_risk_score": 2, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0, "tire_turnaround_score": 8, "utilization_score": 7}, "weighted_score_after": 84, "stage_label_after": "Stage3-Yellow", "changed_components": ["margin_bridge_score", "revision_score", "execution_risk_score", "tire_turnaround_score", "utilization_score"], "component_delta_explanation": "Add tire spread / utilization / FCF conversion bridge.", "MFE_90D_pct": 62.46, "MAE_90D_pct": -1.53, "score_return_alignment_label": "improved_positive_capture", "current_profile_verdict": "current_profile_correct"}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R9L72_C29_018880_20240126_THERMAL_SUPPLIER_MARGIN_FAIL", "trigger_id": "T_R9L72_018880_WATCH_20240126", "symbol": "018880", "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE", "raw_component_scores_before": {"contract_score": 1, "backlog_visibility_score": 2, "margin_bridge_score": 2, "revision_score": 2, "relative_strength_score": 5, "customer_quality_score": 4, "policy_or_regulatory_score": 1, "valuation_repricing_score": 3, "execution_risk_score": 5, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_before": 76, "stage_label_before": "Stage3-Yellow", "raw_component_scores_after": {"contract_score": 1, "backlog_visibility_score": 2, "margin_bridge_score": 1, "revision_score": 1, "relative_strength_score": 4, "customer_quality_score": 4, "policy_or_regulatory_score": 1, "valuation_repricing_score": 2, "execution_risk_score": 8, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0, "fcf_conversion_score": 1, "thermal_margin_failure_penalty": 7}, "weighted_score_after": 61, "stage_label_after": "Stage2-WatchOnly", "changed_components": ["margin_bridge_score", "revision_score", "relative_strength_score", "valuation_repricing_score", "execution_risk_score", "fcf_conversion_score", "thermal_margin_failure_penalty"], "component_delta_explanation": "Penalize supplier theme or price-only relative strength without independent margin/FCF bridge.", "MFE_90D_pct": 8.97, "MAE_90D_pct": -21.88, "score_return_alignment_label": "reduced_false_positive", "current_profile_verdict": "current_profile_false_positive"}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R9L72_C29_010100_20231101_SMALLCAP_MOBILITY_BLOWOFF_FAIL", "trigger_id": "T_R9L72_010100_WATCH_20231101", "symbol": "010100", "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE", "raw_component_scores_before": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 1, "revision_score": 1, "relative_strength_score": 8, "customer_quality_score": 1, "policy_or_regulatory_score": 0, "valuation_repricing_score": 4, "execution_risk_score": 5, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_before": 77, "stage_label_before": "Stage2-Actionable", "raw_component_scores_after": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 0, "revision_score": 0, "relative_strength_score": 5, "customer_quality_score": 1, "policy_or_regulatory_score": 0, "valuation_repricing_score": 2, "execution_risk_score": 9, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0, "price_only_blowoff_penalty": 9}, "weighted_score_after": 54, "stage_label_after": "Stage2-WatchOnly", "changed_components": ["margin_bridge_score", "revision_score", "relative_strength_score", "valuation_repricing_score", "execution_risk_score", "price_only_blowoff_penalty"], "component_delta_explanation": "Penalize supplier theme or price-only relative strength without independent margin/FCF bridge.", "MFE_90D_pct": 7.52, "MAE_90D_pct": -39.84, "score_return_alignment_label": "reduced_false_positive", "current_profile_verdict": "current_profile_false_positive"}
```

### 25.5 shadow_weight rows
```csv
row_type,axis,scope,large_sector_id,canonical_archetype_id,baseline_value,tested_value,delta,reason,backtest_effect,trigger_ids,calibration_usable_count,new_independent_case_count,counterexample_count,confidence,proposal_type,notes
shadow_weight,C29_tire_spread_margin_bridge_bonus,canonical_archetype_specific,L3_BATTERY_EV_GREEN_MOBILITY,C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE,0,1,+1,"Tire cases with ASP/raw-material spread + utilization + revision bridge had high MFE and low initial MAE","keeps 161390/073240 promotable; does not affect price-only rows","T_R9L72_161390_STAGE2_20231101|T_R9L72_073240_STAGE2_20231101",4,4,2,medium,canonical_shadow_only,"not production; post-calibrated residual"
shadow_weight,C29_supplier_theme_without_margin_bridge_penalty,canonical_archetype_specific,L3_BATTERY_EV_GREEN_MOBILITY,C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE,0,-2,-2,"Supplier theme/relative strength without independent margin or FCF bridge produced high MAE false positives","blocks 018880 and 010100 from Stage2/3 promotion","T_R9L72_018880_WATCH_20240126|T_R9L72_010100_WATCH_20231101",4,4,2,medium,canonical_shadow_only,"not production; post-calibrated residual"
shadow_weight,C29_price_only_mobility_blowoff_guard,sector_specific,L3_BATTERY_EV_GREEN_MOBILITY,C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE,0,1,+1,"Smallcap mobility price-only moves should be 4B/watch, not positive promotion","reduces high-MAE price-only entries","T_R9L72_010100_WATCH_20231101|T_R9L72_010100_4B_20231114",4,4,2,medium,sector_shadow_only,"strengthens existing price-only blowoff guard in C29 context"
```

### 25.6 residual_contribution row
```jsonl
{"row_type": "residual_contribution", "round": "R9", "loop": "72", "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE", "scheduled_round": "R9", "scheduled_loop": 72, "round_schedule_status": "valid", "round_sector_consistency": "pass", "new_independent_case_count": 4, "reused_case_count": 0, "new_symbol_count": 4, "same_archetype_new_symbol_count": 4, "same_archetype_new_trigger_family_count": 4, "new_trigger_family_count": 4, "positive_case_count": 2, "counterexample_count": 2, "current_profile_error_count": 3, "tested_existing_calibrated_axes": ["stage2_actionable_evidence_bonus", "price_only_blowoff_blocks_positive_stage", "full_4b_requires_non_price_evidence", "hard_4c_thesis_break_routes_to_4c"], "residual_error_types_found": ["residual_missed_structural_mining", "residual_false_positive_mining", "4B_price_only_too_early", "4C_thesis_break_watch"], "loop_contribution_label": "canonical_archetype_rule_candidate", "do_not_propose_new_weight_delta": false, "diversity_score_summary": "new_symbols=4; new_trigger_family=4; counterexamples=2; residual_errors=3; wrong_round_penalty=0; new_independent_case_ratio=1.00"}
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
completed_round = R9
completed_loop = 72
next_round = R10
next_loop = 72
round_schedule_status = valid
round_sector_consistency = pass
```

## 28. Source Notes

Stock-Web files consulted during this run:

```text
atlas/manifest.json
atlas/symbol_profiles/161/161390.json
atlas/symbol_profiles/073/073240.json
atlas/symbol_profiles/018/018880.json
atlas/symbol_profiles/010/010100.json
atlas/ohlcv_tradable_by_symbol_year/161/161390/2023.csv
atlas/ohlcv_tradable_by_symbol_year/161/161390/2024.csv
atlas/ohlcv_tradable_by_symbol_year/073/073240/2023.csv
atlas/ohlcv_tradable_by_symbol_year/073/073240/2024.csv
atlas/ohlcv_tradable_by_symbol_year/018/018880/2024.csv
atlas/ohlcv_tradable_by_symbol_year/010/010100/2023.csv
atlas/ohlcv_tradable_by_symbol_year/010/010100/2024.csv
```

The research uses raw/unadjusted tradable OHLC from Songdaiki/stock-web. It is not an investment recommendation and does not alter production scoring.

