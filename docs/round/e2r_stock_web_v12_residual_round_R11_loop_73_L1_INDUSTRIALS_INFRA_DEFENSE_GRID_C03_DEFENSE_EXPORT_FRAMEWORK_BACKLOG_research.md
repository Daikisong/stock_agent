# E2R Stock-Web Historical Calibration / Sector-Archetype Residual Research Round

## 0. Research Metadata

```yaml
research_session: post_calibrated_sector_archetype_residual_research
mode: historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12
repo_session: later_batch_implementation_only
output_file: e2r_stock_web_v12_residual_round_R11_loop_73_L1_INDUSTRIALS_INFRA_DEFENSE_GRID_C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG_research.md
scheduled_round: R11
scheduled_loop: 73
completed_round: R11
completed_loop: 73
large_sector_id: L1_INDUSTRIALS_INFRA_DEFENSE_GRID
canonical_archetype_id: C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG
fine_archetype_id: POLAND_DEFENSE_EXPORT_FRAMEWORK_VS_GEOPOLITICAL_THEME_GUARD
loop_objective:
  - residual_false_positive_mining
  - residual_missed_structural_mining
  - stage2_actionable_bonus_stress_test
  - 4B_non_price_requirement_stress_test
  - sector_specific_rule_discovery
  - canonical_archetype_compression
  - counterexample_mining
  - coverage_gap_fill
stock_agent_code_access_allowed: false
stock_agent_code_patch_allowed: false
stock_agent_live_scan_allowed: false
production_scoring_changed: false
shadow_weight_only: true
handoff_prompt_embedded: true
handoff_prompt_executed_now: false
price_source: Songdaiki/stock-web
price_basis: tradable_raw
price_adjustment_status: raw_unadjusted_marcap
stock_web_manifest_max_date: 2026-02-20
round_schedule_status: valid
round_sector_consistency: pass
```

This loop adds 4 new independent cases, 2 counterexamples, and 2 residual errors for R11/L1_INDUSTRIALS_INFRA_DEFENSE_GRID/C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG.

## 1. Current Calibrated Profile Assumption

The current default proxy is `e2r_2_1_stock_web_calibrated_proxy`; the rollback reference is `e2r_2_0_baseline_reference`.

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

This MD does not re-propose those axes globally. It stress-tests them inside a policy-defense R11 route and proposes shadow-only C03/L1 rules.

## 2. Round / Large Sector / Canonical Archetype Scope

| field | value |
|---|---|
| scheduled_round | R11 |
| scheduled_loop | 73 |
| selected large_sector_id | L1_INDUSTRIALS_INFRA_DEFENSE_GRID |
| selected canonical_archetype_id | C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG |
| fine_archetype_id | POLAND_DEFENSE_EXPORT_FRAMEWORK_VS_GEOPOLITICAL_THEME_GUARD |
| R11 sector consistency | R11 permits L10 policy-event cross-checks or L1 when policy-defense linkage is the mechanism; this file uses L1/C03 because the tested path is defense export framework vs. geopolitical defense theme. |

## 3. Previous Coverage / Duplicate Avoidance Check

GitHub code search for `e2r_stock_web_v12_residual_round_R11_loop_73 C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG` returned no matching prior R11/Loop73/C03 file. Local v12 outputs already contain R11/Loop71-72 C31 policy-event nuclear/demographic files, so this run intentionally shifts to a policy-defense R11 route without opening `stock_agent/src/e2r`.

```text
hard_duplicate_key = canonical_archetype_id + symbol + trigger_date + entry_date + trigger_family
minimum_new_independent_case_ratio = 1.00
new_symbol_count = 4
reused_case_count = 0
```

## 4. Stock-Web OHLC Input / Price Source Validation

`Songdaiki/stock-web` manifest validation:

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
markets = KONEX | KOSDAQ | KOSDAQ GLOBAL | KOSPI
calibration_shard_root = atlas/ohlcv_tradable_by_symbol_year
raw_shard_root = atlas/ohlcv_raw_by_symbol_year
schema_path = atlas/schema.json
universe_path = atlas/universe/all_symbols.csv
```

The manifest confirms raw/unadjusted OHLC, zero-volume and invalid OHLC rows excluded from calibration shards, and corporate-action-contaminated windows blocked by default.

## 5. Historical Eligibility Gate

| case_id | symbol | profile path | entry_date | 180D forward window | corporate action window status | calibration_usable |
|---|---:|---|---|---:|---|---|
| R11L73_C03_012450_20220728_POLAND_K9_FRAMEWORK_BACKLOG | 012450 | atlas/symbol_profiles/012/012450.json | 2022-07-28 | 180 | clean_180D_window | true |
| R11L73_C03_064350_20220728_POLAND_K2_FRAMEWORK_BACKLOG | 064350 | atlas/symbol_profiles/064/064350.json | 2022-07-28 | 180 | clean_180D_window | true |
| R11L73_C03_065450_20221004_NK_MISSILE_GEOPOLITICAL_THEME | 065450 | atlas/symbol_profiles/065/065450.json | 2022-10-04 | 180 | clean_180D_window | true |
| R11L73_C03_010820_20221004_NK_MISSILE_PRICE_ONLY_HIGH_MAE | 010820 | atlas/symbol_profiles/010/010820.json | 2022-10-04 | 180 | clean_180D_window | true |

All four representative triggers are historical, have tradable entry rows, have at least 180 forward trading days by `2026-02-20`, and have no corporate-action candidate inside the entry~D+180 window.

## 6. Canonical Archetype Compression Map

| fine_archetype_id | canonical_archetype_id | included symbols | compression note |
|---|---|---|---|
| POLAND_DEFENSE_EXPORT_FRAMEWORK_BACKLOG | C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG | 012450, 064350 | buyer/platform/quantity/delivery or executive-contract path makes policy-defense event economically convertible |
| GEOPOLITICAL_DEFENSE_THEME_GUARD | C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG | 065450, 010820 | geopolitical shock/relative strength alone is theme beta and should not promote above watch without company-specific order evidence |

## 7. Case Selection Summary

| case_id | symbol | company_name | case_type | positive_or_counterexample | trigger_type | trigger_date | entry_date | entry_price |
|---|---:|---|---|---|---|---|---|---:|
| R11L73_C03_012450_20220728_POLAND_K9_FRAMEWORK_BACKLOG | 012450 | 한화에어로스페이스 | structural_success | positive | Stage2-Actionable | 2022-07-27 | 2022-07-28 | 53,700 |
| R11L73_C03_064350_20220728_POLAND_K2_FRAMEWORK_BACKLOG | 064350 | 현대로템 | structural_success | positive | Stage2-Actionable | 2022-07-27 | 2022-07-28 | 24,950 |
| R11L73_C03_065450_20221004_NK_MISSILE_GEOPOLITICAL_THEME | 065450 | 빅텍 | price_moved_without_evidence | counterexample | Stage2-Theme / not Stage2-Actionable | 2022-10-04 | 2022-10-04 | 5,700 |
| R11L73_C03_010820_20221004_NK_MISSILE_PRICE_ONLY_HIGH_MAE | 010820 | 퍼스텍 | high_mae_success | counterexample | Stage2-Theme / high-MAE guard | 2022-10-04 | 2022-10-04 | 3,150 |

## 8. Positive vs Counterexample Balance

```text
positive_case_count = 2
counterexample_count = 2
4B_case_count = 4
4C_case_count = 2
calibration_usable_case_count = 4
minimum_positive_case_count = pass
minimum_counterexample_count = pass
minimum_calibration_usable_case_count = pass
```

The positive pair has a named sovereign buyer, platform path, and delivery/backlog route. The counterexample pair only has geopolitical air-raid siren energy: it can move the tape, but it does not put a purchase order into the backlog.

## 9. Evidence Source Map

| trigger_id | evidence_available_at_that_date | evidence source | stage evidence classification |
|---|---|---|---|
| R11L73_T012450_20220728_STAGE2A | Poland-Hanwha K9 framework agreement created a visible export/backlog bridge rather than a pure war-news sympathy trade; later executive-contract path made the policy/export spark economically convertible. | Reuters 2025 Poland/Hanwha references 2022 arms framework; K9 Thunder export records list 2022-07-27 framework and 2022-08-26 executive contract; stock-web rows validated from 012450 2022/2023 shards. | Stage2=public_event_or_disclosure,customer_or_order_quality,policy_or_regulatory_optionality,backlog_or_delivery_visibility,relative_strength; Stage3=multiple_public_sources,financial_visibility,durable_customer_confirmation,repeat_order_or_conversion |
| R11L73_T064350_20220728_STAGE2A | Poland-Hyundai Rotem K2 framework agreement provided buyer identity, platform quantity, delivery/local-production option, and a later executive-contract path. This is qualitatively different from generic defense-theme beta. | Reuters 2025 K2 follow-up references the 2022 Hyundai Rotem agreement; K2 Black Panther export records list 2022-07-27 framework and 2022-08-26 executive agreement; stock-web rows validated from 064350 2022/2023 shards. | Stage2=public_event_or_disclosure,customer_or_order_quality,policy_or_regulatory_optionality,backlog_or_delivery_visibility,relative_strength; Stage3=multiple_public_sources,financial_visibility,durable_customer_confirmation,repeat_order_or_conversion |
| R11L73_T065450_20221004_STAGE2_THEME | North Korea missile/geopolitical shock produced defense-theme relative strength, but no named export order, buyer quality, backlog visibility, or margin bridge was visible for the company at trigger date. | Reuters/Nikkei style historical coverage of North Korea missile over Japan, 2022-10-04; stock-web rows validated from 065450 2022/2023 shards. | Stage2=public_event_or_disclosure,relative_strength,policy_or_regulatory_optionality; Stage3=none |
| R11L73_T010820_20221004_STAGE2_THEME | The same geopolitical shock created intermittent MFE but also high MAE and no firm export/backlog bridge. It tests whether C03 should distinguish tradable volatility from investable export-framework evidence. | Historical North Korea missile headline family, 2022-10-04; stock-web rows validated from 010820 2022/2023 shards. | Stage2=public_event_or_disclosure,relative_strength,policy_or_regulatory_optionality; Stage3=none |

## 10. Price Data Source Map

| symbol | company_name | tradable shard(s) used | profile path | price basis | stock_web_manifest_max_date |
|---:|---|---|---|---|---|
| 012450 | 한화에어로스페이스 | atlas/ohlcv_tradable_by_symbol_year/012/012450/2022.csv|atlas/ohlcv_tradable_by_symbol_year/012/012450/2023.csv | atlas/symbol_profiles/012/012450.json | tradable_raw | 2026-02-20 |
| 064350 | 현대로템 | atlas/ohlcv_tradable_by_symbol_year/064/064350/2022.csv|atlas/ohlcv_tradable_by_symbol_year/064/064350/2023.csv | atlas/symbol_profiles/064/064350.json | tradable_raw | 2026-02-20 |
| 065450 | 빅텍 | atlas/ohlcv_tradable_by_symbol_year/065/065450/2022.csv|atlas/ohlcv_tradable_by_symbol_year/065/065450/2023.csv | atlas/symbol_profiles/065/065450.json | tradable_raw | 2026-02-20 |
| 010820 | 퍼스텍 | atlas/ohlcv_tradable_by_symbol_year/010/010820/2022.csv|atlas/ohlcv_tradable_by_symbol_year/010/010820/2023.csv | atlas/symbol_profiles/010/010820.json | tradable_raw | 2026-02-20 |

## 11. Case-by-Case Trigger Grid

| case_id | Stage2 evidence | Stage3 evidence | 4B evidence | 4C evidence | current_profile_verdict |
|---|---|---|---|---|---|
| R11L73_C03_012450_20220728_POLAND_K9_FRAMEWORK_BACKLOG | public_event_or_disclosure, customer_or_order_quality, policy_or_regulatory_optionality, backlog_or_delivery_visibility, relative_strength | multiple_public_sources, financial_visibility, durable_customer_confirmation, repeat_order_or_conversion | valuation_blowoff, positioning_overheat | - | current_profile_correct |
| R11L73_C03_064350_20220728_POLAND_K2_FRAMEWORK_BACKLOG | public_event_or_disclosure, customer_or_order_quality, policy_or_regulatory_optionality, backlog_or_delivery_visibility, relative_strength | multiple_public_sources, financial_visibility, durable_customer_confirmation, repeat_order_or_conversion | valuation_blowoff, positioning_overheat | - | current_profile_correct |
| R11L73_C03_065450_20221004_NK_MISSILE_GEOPOLITICAL_THEME | public_event_or_disclosure, relative_strength, policy_or_regulatory_optionality | - | price_only_local_peak, positioning_overheat | thesis_evidence_broken | current_profile_false_positive |
| R11L73_C03_010820_20221004_NK_MISSILE_PRICE_ONLY_HIGH_MAE | public_event_or_disclosure, relative_strength, policy_or_regulatory_optionality | - | price_only_local_peak, positioning_overheat | thesis_evidence_broken | current_profile_false_positive |

## 12. Trigger-Level OHLC Backtest Tables

| trigger_id | symbol | entry_date | entry_price | MFE_30D_pct | MAE_30D_pct | MFE_90D_pct | MAE_90D_pct | MFE_180D_pct | MAE_180D_pct | peak_date | peak_price | drawdown_after_peak_pct | calibration_usable |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---|---:|---:|---|
| R11L73_T012450_20220728_STAGE2A | 012450 | 2022-07-28 | 53,700 | 61.64 | -3.17 | 61.64 | -3.17 | 123.65 | -3.17 | 2023-04-11 | 120,100 | -15.57 | true |
| R11L73_T064350_20220728_STAGE2A | 064350 | 2022-07-28 | 24,950 | 31.66 | -3.61 | 31.66 | -7.62 | 31.66 | -7.62 | 2022-08-26 | 32,850 | -29.83 | true |
| R11L73_T065450_20221004_STAGE2_THEME | 065450 | 2022-10-04 | 5,700 | 28.77 | -7.72 | 28.77 | -8.07 | 28.77 | -14.91 | 2022-11-03 | 7,340 | -33.92 | true |
| R11L73_T010820_20221004_STAGE2_THEME | 010820 | 2022-10-04 | 3,150 | 11.75 | -17.3 | 20.79 | -17.3 | 25.08 | -17.3 | 2023-04-06 | 3,940 | -13.45 | true |

## 13. Current Calibrated Profile Stress Test

| case_id | current calibrated profile likely action | actual MFE/MAE alignment | verdict |
|---|---|---|---|
| R11L73_C03_012450_20220728_POLAND_K9_FRAMEWORK_BACKLOG | promote as Stage2-Actionable/Yellow because named export framework and backlog route exist | strong 30D/90D/180D MFE with modest early MAE | current_profile_correct |
| R11L73_C03_064350_20220728_POLAND_K2_FRAMEWORK_BACKLOG | promote as Stage2-Actionable/Yellow because named buyer/platform/quantity path exists | positive MFE but local 4B overlay needed after Aug 2022 peak | current_profile_correct |
| R11L73_C03_065450_20221004_NK_MISSILE_GEOPOLITICAL_THEME | risk of false Stage2-Actionable if policy/geopolitical relative strength is over-weighted | MFE exists, but no backlog bridge and drawdown after peak is severe | current_profile_false_positive |
| R11L73_C03_010820_20221004_NK_MISSILE_PRICE_ONLY_HIGH_MAE | risk of false Stage2-Actionable from price-only defense theme | intermittent MFE but high MAE and no export conversion | current_profile_false_positive |

Existing axis treatment:

```text
stage2_actionable_evidence_bonus = existing_axis_tested
stage3_yellow_total_min = existing_axis_tested
price_only_blowoff_blocks_positive_stage = existing_axis_strengthened
full_4b_requires_non_price_evidence = existing_axis_strengthened
hard_4c_thesis_break_routes_to_4c = existing_axis_kept
```

## 14. Stage2 / Yellow / Green Comparison

Stage2-Actionable is useful in C03 only when the evidence has a conversion bridge. The difference is not “defense went up” but “defense headline became contract/backlog visibility.”

```text
C03_export_framework_entry = Stage2-Actionable allowed
C03_geopolitical_theme_entry = Stage2-Watch only
Stage3-Yellow requires named buyer + platform/quantity + delivery/backlog visibility
Stage3-Green requires revision/margin/backlog conversion, not just theme liquidity
```

`green_lateness_ratio` is not calculated here because the selected representative rows are Stage2-Actionable and no separate confirmed Stage3-Green trigger date is used for aggregate inclusion.

## 15. 4B Local vs Full-window Timing Audit

| case_id | four_b_local_peak_proximity | four_b_full_window_peak_proximity | four_b_evidence_type | verdict |
|---|---:|---:|---|---|
| R11L73_C03_012450_20220728_POLAND_K9_FRAMEWORK_BACKLOG | 0.68 | 0.68 | valuation_blowoff, positioning_overheat | not full 4B until non-price overheat/revision slowdown appears |
| R11L73_C03_064350_20220728_POLAND_K2_FRAMEWORK_BACKLOG | 1.00 | 1.00 | valuation_blowoff, positioning_overheat | local peak timing good; still overlay-only without non-price 4B evidence |
| R11L73_C03_065450_20221004_NK_MISSILE_GEOPOLITICAL_THEME | 1.00 | 1.00 | price_only, positioning_overheat | price-only 4B watch, not positive-stage evidence |
| R11L73_C03_010820_20221004_NK_MISSILE_PRICE_ONLY_HIGH_MAE | 0.47 | 0.47 | price_only, positioning_overheat | early local 4B can be too early vs. later price-only spike |

## 16. 4C Protection Audit

No hard 4C is proposed for the export-framework positives. For theme rows, the correct handling is `thesis_break_watch_only` unless a company-specific contract cancellation, export failure, accounting/trust break, or explicit customer/order loss appears.

```text
065450 = thesis_break_watch_only
010820 = thesis_break_watch_only
hard_4c_routing = existing_axis_kept
```

## 17. Sector-Specific Rule Candidate

```text
rule_scope = sector_specific
rule_id = L1_C03_defense_export_framework_quality_gate
candidate = true
```

Rule candidate:

```text
If large_sector_id == L1 and canonical_archetype_id == C03:
    promote policy-defense event above Stage2-Watch only when:
        named_buyer_or_sovereign_customer == true
        and platform_or_quantity_or_contract_size_visible == true
        and delivery_or_backlog_or_follow-on_conversion_path == true
    else:
        cap to Stage2-Watch / theme-only watch even if relative_strength_score is high
```

## 18. Canonical-Archetype Rule Candidate

```text
rule_scope = canonical_archetype_specific
rule_id = C03_export_backlog_bridge_vs_geopolitical_theme_cap
candidate = true
```

This compresses the C03 distinction into one canonical rule: export framework + backlog visibility is evidence; geopolitical theme beta is a siren, not a shipment schedule.

## 19. Before / After Backtest Comparison

| profile_id | profile_scope | eligible_trigger_count | selected_entry_trigger_per_case | avg_MFE_90D_pct | avg_MAE_90D_pct | avg_MFE_180D_pct | avg_MAE_180D_pct | false_positive_rate | score_return_alignment_verdict |
|---|---|---:|---|---:|---:|---:|---:|---:|---|
| P0/e2r_2_1_stock_web_calibrated_proxy | current | 4 | all four triggers | 35.72 | -9.04 | 52.29 | -10.75 | 0.5 | mixed; positives have true export/backlog bridge, counterexamples are policy/geopolitical price-only rows |
| P0b/e2r_2_0_baseline_reference | rollback_reference | 4 | all four triggers but with lower positive confidence | 35.72 | -9.04 | 52.29 | -10.75 | 0.25 | safer but too blunt; does not separate export framework from theme beta |
| P1/sector_specific_candidate_profile | sector_specific | 2 | 012450 and 064350 only | 46.65 | -5.39 | 77.66 | -5.39 | 0.0 | improves alignment by keeping export-framework positives and blocking price-only theme rows |
| P2/canonical_archetype_candidate_profile | canonical_archetype_specific | 2 | C03 export-framework rows only | 46.65 | -5.39 | 77.66 | -5.39 | 0.0 | canonical shadow candidate retained |
| P3/counterexample_guard_profile | guardrail | 0 | 065450 and 010820 are demoted; no positive entry selected | None | None | None | None | 0.0 | guard stops two policy/geopolitical theme false positives |

## 20. Score-Return Alignment Matrix

| case_id | before score/label | after score/label | alignment note |
|---|---|---|---|
| R11L73_C03_012450_20220728_POLAND_K9_FRAMEWORK_BACKLOG | 84 / Stage3-Yellow / strong Stage2-Actionable | 88 / Stage3-Green-shadow / export framework backlog quality | C03 shadow rule gives a narrow positive bridge only when a policy/war-driven event is tied to named buyer, framework size, and order/backlog conversion path. |
| R11L73_C03_064350_20220728_POLAND_K2_FRAMEWORK_BACKLOG | 82 / Stage3-Yellow / export framework visible | 87 / Stage3-Green-shadow / export framework backlog quality | C03 export-framework positive should score above theme-only defense names only when buyer/platform/quantity/delivery path are explicit. |
| R11L73_C03_065450_20221004_NK_MISSILE_GEOPOLITICAL_THEME | 76 / Stage3-Yellow false positive if relative strength + policy shock over-weighted | 56 / Stage2-Watch / defense theme cap | Defense geopolitical theme rows must be capped at watch/actionable watch unless they gain buyer/order/backlog/revision evidence. |
| R11L73_C03_010820_20221004_NK_MISSILE_PRICE_ONLY_HIGH_MAE | 74 / Stage2-Actionable false positive if price-only theme is promoted | 54 / Stage2-Watch / high-MAE defense theme guard | High-MAE defense theme MFE should not be mistaken for structural C03 rerating. Require export-framework/backlog evidence for positive promotion. |

## 21. Coverage Matrix

| large_sector_id | canonical_archetype_id | fine_archetype_id | positive_case_count | counterexample_count | 4B_case_count | 4C_case_count | new_independent_case_count | reused_case_count | calibration_usable_trigger_count | representative_trigger_count | current_profile_error_count | sector_rule_candidate | canonical_rule_candidate | coverage_gap_after_this_loop |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|---|---|
| L1_INDUSTRIALS_INFRA_DEFENSE_GRID | C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG | POLAND_DEFENSE_EXPORT_FRAMEWORK_VS_GEOPOLITICAL_THEME_GUARD | 2 | 2 | 4 | 2 | 4 | 0 | 4 | 4 | 2 | true | true | export-framework vs theme split improved; still needs non-Korea and second-cycle validation |

## 22. Residual Contribution Summary

```text
new_independent_case_count: 4
reused_case_count: 0
reused_case_ids: []
new_symbol_count: 4
new_canonical_archetype_count: 0
new_fine_archetype_count: 2
new_trigger_family_count: 2
tested_existing_calibrated_axes:
  - stage2_actionable_evidence_bonus
  - stage3_yellow_total_min
  - price_only_blowoff_blocks_positive_stage
  - full_4b_requires_non_price_evidence
residual_error_types_found:
  - defense_geopolitical_theme_false_positive
  - price_only_local_4B_overlay_not_full_4B
  - export_framework_backlog_quality_undercompression
new_axis_proposed:
  - C03_export_framework_backlog_quality_bonus
  - C03_geopolitical_theme_stage_cap
existing_axis_strengthened:
  - price_only_blowoff_blocks_positive_stage
  - full_4b_requires_non_price_evidence
existing_axis_weakened: null
existing_axis_kept:
  - hard_4c_thesis_break_routes_to_4c
sector_specific_rule_candidate: true
canonical_archetype_rule_candidate: true
no_new_signal_reason: null
loop_contribution_label: canonical_archetype_rule_candidate
do_not_propose_new_weight_delta: false
```

## 23. Validation Scope / Non-Validation Scope

Validated:

```text
- Scheduled R11 / Loop 73 state.
- R11 sector consistency for policy-defense L1 route.
- Stock-web manifest max_date = 2026-02-20.
- Actual stock-web tradable OHLC entry rows and observed highs/lows from 2022/2023 shards.
- Corporate-action candidate windows checked from symbol profiles.
- Trigger-level MFE/MAE for 30D/90D/180D.
- Same-entry dedupe: one representative trigger per case.
```

Not validated:

```text
- No live/current stock discovery.
- No brokerage or auto-trading path.
- No stock_agent source code inspection.
- No production scoring patch.
- No claim that these are current investment candidates.
```

## 24. Shadow Weight Calibration

```csv
row_type,axis,scope,large_sector_id,canonical_archetype_id,baseline_value,tested_value,delta,reason,backtest_effect,trigger_ids,calibration_usable_count,new_independent_case_count,counterexample_count,confidence,proposal_type,notes
shadow_weight,C03_export_framework_backlog_quality_bonus,canonical_archetype_specific,L1_INDUSTRIALS_INFRA_DEFENSE_GRID,C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG,0,1,+1,"Named sovereign buyer + platform/quantity + delivery/backlog route should receive positive C03 shadow support.","Keeps 012450/064350 positives and separates them from theme beta.","R11L73_T012450_20220728_STAGE2A|R11L73_T064350_20220728_STAGE2A",4,4,2,medium,canonical_shadow_only,"not production; post-calibrated residual"
shadow_weight,C03_geopolitical_theme_stage_cap,canonical_archetype_specific,L1_INDUSTRIALS_INFRA_DEFENSE_GRID,C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG,0,1,+1,"Defense geopolitical headline and relative strength without order/backlog/customer bridge must be capped.","Blocks 065450/010820 false-positive promotion while allowing theme-watch labeling.","R11L73_T065450_20221004_STAGE2_THEME|R11L73_T010820_20221004_STAGE2_THEME",4,4,2,medium,canonical_shadow_only,"not production; post-calibrated residual"
```

## 25. Machine-Readable Rows

```jsonl
{"row_type": "price_source_validation", "source": "Songdaiki/stock-web", "source_url": "https://github.com/Songdaiki/stock-web", "manifest_path": "atlas/manifest.json", "schema_path": "atlas/schema.json", "universe_path": "atlas/universe/all_symbols.csv", "manifest_max_date": "2026-02-20", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "raw_shard_root": "atlas/ohlcv_raw_by_symbol_year", "validation_status": "usable_for_historical_calibration"}
{"row_type": "case", "case_id": "R11L73_C03_012450_20220728_POLAND_K9_FRAMEWORK_BACKLOG", "symbol": "012450", "company_name": "한화에어로스페이스", "round": "R11", "loop": "73", "scheduled_round": "R11", "scheduled_loop": "73", "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "canonical_archetype_id": "C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG", "fine_archetype_id": "POLAND_DEFENSE_EXPORT_FRAMEWORK_VS_GEOPOLITICAL_THEME_GUARD", "case_type": "structural_success", "positive_or_counterexample": "positive", "best_trigger": "R11L73_T012450_20220728_STAGE2A", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "export_framework_backlog_structural_success", "current_profile_verdict": "current_profile_correct", "price_source": "Songdaiki/stock-web", "notes": "Poland-Hanwha K9 framework agreement created a visible export/backlog bridge rather than a pure war-news sympathy trade; later executive-contract path made the policy/export spark economically convertible."}
{"row_type": "case", "case_id": "R11L73_C03_064350_20220728_POLAND_K2_FRAMEWORK_BACKLOG", "symbol": "064350", "company_name": "현대로템", "round": "R11", "loop": "73", "scheduled_round": "R11", "scheduled_loop": "73", "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "canonical_archetype_id": "C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG", "fine_archetype_id": "POLAND_DEFENSE_EXPORT_FRAMEWORK_VS_GEOPOLITICAL_THEME_GUARD", "case_type": "structural_success", "positive_or_counterexample": "positive", "best_trigger": "R11L73_T064350_20220728_STAGE2A", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "defense_export_framework_success_with_local_peak_drawdown", "current_profile_verdict": "current_profile_correct", "price_source": "Songdaiki/stock-web", "notes": "Poland-Hyundai Rotem K2 framework agreement provided buyer identity, platform quantity, delivery/local-production option, and a later executive-contract path. This is qualitatively different from generic defense-theme beta."}
{"row_type": "case", "case_id": "R11L73_C03_065450_20221004_NK_MISSILE_GEOPOLITICAL_THEME", "symbol": "065450", "company_name": "빅텍", "round": "R11", "loop": "73", "scheduled_round": "R11", "scheduled_loop": "73", "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "canonical_archetype_id": "C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG", "fine_archetype_id": "POLAND_DEFENSE_EXPORT_FRAMEWORK_VS_GEOPOLITICAL_THEME_GUARD", "case_type": "price_moved_without_evidence", "positive_or_counterexample": "counterexample", "best_trigger": "R11L73_T065450_20221004_STAGE2_THEME", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "geopolitical_theme_price_pop_without_export_backlog", "current_profile_verdict": "current_profile_false_positive", "price_source": "Songdaiki/stock-web", "notes": "North Korea missile/geopolitical shock produced defense-theme relative strength, but no named export order, buyer quality, backlog visibility, or margin bridge was visible for the company at trigger date."}
{"row_type": "case", "case_id": "R11L73_C03_010820_20221004_NK_MISSILE_PRICE_ONLY_HIGH_MAE", "symbol": "010820", "company_name": "퍼스텍", "round": "R11", "loop": "73", "scheduled_round": "R11", "scheduled_loop": "73", "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "canonical_archetype_id": "C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG", "fine_archetype_id": "POLAND_DEFENSE_EXPORT_FRAMEWORK_VS_GEOPOLITICAL_THEME_GUARD", "case_type": "high_mae_success", "positive_or_counterexample": "counterexample", "best_trigger": "R11L73_T010820_20221004_STAGE2_THEME", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "intermittent_MFE_but_high_MAE_without_export_backlog", "current_profile_verdict": "current_profile_false_positive", "price_source": "Songdaiki/stock-web", "notes": "The same geopolitical shock created intermittent MFE but also high MAE and no firm export/backlog bridge. It tests whether C03 should distinguish tradable volatility from investable export-framework evidence."}
{"row_type": "trigger", "trigger_id": "R11L73_T012450_20220728_STAGE2A", "case_id": "R11L73_C03_012450_20220728_POLAND_K9_FRAMEWORK_BACKLOG", "symbol": "012450", "company_name": "한화에어로스페이스", "round": "R11", "loop": "73", "scheduled_round": "R11", "scheduled_loop": "73", "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "canonical_archetype_id": "C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG", "fine_archetype_id": "POLAND_DEFENSE_EXPORT_FRAMEWORK_VS_GEOPOLITICAL_THEME_GUARD", "sector": "defense_aerospace", "primary_archetype": "defense_export_framework_backlog", "loop_objective": "residual_false_positive_mining|residual_missed_structural_mining|stage2_actionable_bonus_stress_test|4B_non_price_requirement_stress_test|sector_specific_rule_discovery|canonical_archetype_compression|counterexample_mining|coverage_gap_fill", "trigger_type": "Stage2-Actionable", "trigger_date": "2022-07-27", "entry_date": "2022-07-28", "entry_price": 53700, "evidence_available_at_that_date": "Poland-Hanwha K9 framework agreement created a visible export/backlog bridge rather than a pure war-news sympathy trade; later executive-contract path made the policy/export spark economically convertible.", "evidence_source": "Reuters 2025 Poland/Hanwha references 2022 arms framework; K9 Thunder export records list 2022-07-27 framework and 2022-08-26 executive contract; stock-web rows validated from 012450 2022/2023 shards.", "stage2_evidence_fields": ["public_event_or_disclosure", "customer_or_order_quality", "policy_or_regulatory_optionality", "backlog_or_delivery_visibility", "relative_strength"], "stage3_evidence_fields": ["multiple_public_sources", "financial_visibility", "durable_customer_confirmation", "repeat_order_or_conversion"], "stage4b_evidence_fields": ["valuation_blowoff", "positioning_overheat"], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/012/012450/2022.csv|atlas/ohlcv_tradable_by_symbol_year/012/012450/2023.csv", "profile_path": "atlas/symbol_profiles/012/012450.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": 61.64, "MFE_90D_pct": 61.64, "MFE_180D_pct": 123.65, "MFE_1Y_pct": null, "MFE_2Y_pct": null, "MAE_30D_pct": -3.17, "MAE_90D_pct": -3.17, "MAE_180D_pct": -3.17, "MAE_1Y_pct": null, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2023-04-11", "peak_price": 120100, "drawdown_after_peak_pct": -15.57, "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": 0.68, "four_b_full_window_peak_proximity": 0.68, "four_b_timing_verdict": "non_price_export_backlog_needed_before_full_4B", "four_b_evidence_type": ["valuation_blowoff", "positioning_overheat"], "four_c_protection_label": "not_applicable", "trigger_outcome_label": "export_framework_backlog_structural_success", "current_profile_verdict": "current_profile_correct", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window", "same_entry_group_id": "R11L73_C03_012450_20220728_POLAND_K9_FRAMEWORK_BACKLOG::2022-07-28::53700", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false}
{"row_type": "trigger", "trigger_id": "R11L73_T064350_20220728_STAGE2A", "case_id": "R11L73_C03_064350_20220728_POLAND_K2_FRAMEWORK_BACKLOG", "symbol": "064350", "company_name": "현대로템", "round": "R11", "loop": "73", "scheduled_round": "R11", "scheduled_loop": "73", "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "canonical_archetype_id": "C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG", "fine_archetype_id": "POLAND_DEFENSE_EXPORT_FRAMEWORK_VS_GEOPOLITICAL_THEME_GUARD", "sector": "defense_ground_systems", "primary_archetype": "defense_export_framework_backlog", "loop_objective": "residual_false_positive_mining|residual_missed_structural_mining|stage2_actionable_bonus_stress_test|4B_non_price_requirement_stress_test|sector_specific_rule_discovery|canonical_archetype_compression|counterexample_mining|coverage_gap_fill", "trigger_type": "Stage2-Actionable", "trigger_date": "2022-07-27", "entry_date": "2022-07-28", "entry_price": 24950, "evidence_available_at_that_date": "Poland-Hyundai Rotem K2 framework agreement provided buyer identity, platform quantity, delivery/local-production option, and a later executive-contract path. This is qualitatively different from generic defense-theme beta.", "evidence_source": "Reuters 2025 K2 follow-up references the 2022 Hyundai Rotem agreement; K2 Black Panther export records list 2022-07-27 framework and 2022-08-26 executive agreement; stock-web rows validated from 064350 2022/2023 shards.", "stage2_evidence_fields": ["public_event_or_disclosure", "customer_or_order_quality", "policy_or_regulatory_optionality", "backlog_or_delivery_visibility", "relative_strength"], "stage3_evidence_fields": ["multiple_public_sources", "financial_visibility", "durable_customer_confirmation", "repeat_order_or_conversion"], "stage4b_evidence_fields": ["valuation_blowoff", "positioning_overheat"], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/064/064350/2022.csv|atlas/ohlcv_tradable_by_symbol_year/064/064350/2023.csv", "profile_path": "atlas/symbol_profiles/064/064350.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": 31.66, "MFE_90D_pct": 31.66, "MFE_180D_pct": 31.66, "MFE_1Y_pct": null, "MFE_2Y_pct": null, "MAE_30D_pct": -3.61, "MAE_90D_pct": -7.62, "MAE_180D_pct": -7.62, "MAE_1Y_pct": null, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2022-08-26", "peak_price": 32850, "drawdown_after_peak_pct": -29.83, "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": 1.0, "four_b_full_window_peak_proximity": 1.0, "four_b_timing_verdict": "good_local_4B_timing_but_full_4B_requires_non_price_overheat", "four_b_evidence_type": ["valuation_blowoff", "positioning_overheat"], "four_c_protection_label": "not_applicable", "trigger_outcome_label": "defense_export_framework_success_with_local_peak_drawdown", "current_profile_verdict": "current_profile_correct", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window", "same_entry_group_id": "R11L73_C03_064350_20220728_POLAND_K2_FRAMEWORK_BACKLOG::2022-07-28::24950", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false}
{"row_type": "trigger", "trigger_id": "R11L73_T065450_20221004_STAGE2_THEME", "case_id": "R11L73_C03_065450_20221004_NK_MISSILE_GEOPOLITICAL_THEME", "symbol": "065450", "company_name": "빅텍", "round": "R11", "loop": "73", "scheduled_round": "R11", "scheduled_loop": "73", "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "canonical_archetype_id": "C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG", "fine_archetype_id": "POLAND_DEFENSE_EXPORT_FRAMEWORK_VS_GEOPOLITICAL_THEME_GUARD", "sector": "defense_electronics_theme", "primary_archetype": "geopolitical_defense_theme_no_backlog", "loop_objective": "residual_false_positive_mining|residual_missed_structural_mining|stage2_actionable_bonus_stress_test|4B_non_price_requirement_stress_test|sector_specific_rule_discovery|canonical_archetype_compression|counterexample_mining|coverage_gap_fill", "trigger_type": "Stage2-Theme / not Stage2-Actionable", "trigger_date": "2022-10-04", "entry_date": "2022-10-04", "entry_price": 5700, "evidence_available_at_that_date": "North Korea missile/geopolitical shock produced defense-theme relative strength, but no named export order, buyer quality, backlog visibility, or margin bridge was visible for the company at trigger date.", "evidence_source": "Reuters/Nikkei style historical coverage of North Korea missile over Japan, 2022-10-04; stock-web rows validated from 065450 2022/2023 shards.", "stage2_evidence_fields": ["public_event_or_disclosure", "relative_strength", "policy_or_regulatory_optionality"], "stage3_evidence_fields": [], "stage4b_evidence_fields": ["price_only_local_peak", "positioning_overheat"], "stage4c_evidence_fields": ["thesis_evidence_broken"], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/065/065450/2022.csv|atlas/ohlcv_tradable_by_symbol_year/065/065450/2023.csv", "profile_path": "atlas/symbol_profiles/065/065450.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": 28.77, "MFE_90D_pct": 28.77, "MFE_180D_pct": 28.77, "MFE_1Y_pct": null, "MFE_2Y_pct": null, "MAE_30D_pct": -7.72, "MAE_90D_pct": -8.07, "MAE_180D_pct": -14.91, "MAE_1Y_pct": null, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2022-11-03", "peak_price": 7340, "drawdown_after_peak_pct": -33.92, "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": 1.0, "four_b_full_window_peak_proximity": 1.0, "four_b_timing_verdict": "price_only_local_4B_not_full_4B_without_non_price_evidence", "four_b_evidence_type": ["price_only", "positioning_overheat"], "four_c_protection_label": "thesis_break_watch_only", "trigger_outcome_label": "geopolitical_theme_price_pop_without_export_backlog", "current_profile_verdict": "current_profile_false_positive", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window", "same_entry_group_id": "R11L73_C03_065450_20221004_NK_MISSILE_GEOPOLITICAL_THEME::2022-10-04::5700", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false}
{"row_type": "trigger", "trigger_id": "R11L73_T010820_20221004_STAGE2_THEME", "case_id": "R11L73_C03_010820_20221004_NK_MISSILE_PRICE_ONLY_HIGH_MAE", "symbol": "010820", "company_name": "퍼스텍", "round": "R11", "loop": "73", "scheduled_round": "R11", "scheduled_loop": "73", "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "canonical_archetype_id": "C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG", "fine_archetype_id": "POLAND_DEFENSE_EXPORT_FRAMEWORK_VS_GEOPOLITICAL_THEME_GUARD", "sector": "defense_theme", "primary_archetype": "geopolitical_defense_theme_high_MAE", "loop_objective": "residual_false_positive_mining|residual_missed_structural_mining|stage2_actionable_bonus_stress_test|4B_non_price_requirement_stress_test|sector_specific_rule_discovery|canonical_archetype_compression|counterexample_mining|coverage_gap_fill", "trigger_type": "Stage2-Theme / high-MAE guard", "trigger_date": "2022-10-04", "entry_date": "2022-10-04", "entry_price": 3150, "evidence_available_at_that_date": "The same geopolitical shock created intermittent MFE but also high MAE and no firm export/backlog bridge. It tests whether C03 should distinguish tradable volatility from investable export-framework evidence.", "evidence_source": "Historical North Korea missile headline family, 2022-10-04; stock-web rows validated from 010820 2022/2023 shards.", "stage2_evidence_fields": ["public_event_or_disclosure", "relative_strength", "policy_or_regulatory_optionality"], "stage3_evidence_fields": [], "stage4b_evidence_fields": ["price_only_local_peak", "positioning_overheat"], "stage4c_evidence_fields": ["thesis_evidence_broken"], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/010/010820/2022.csv|atlas/ohlcv_tradable_by_symbol_year/010/010820/2023.csv", "profile_path": "atlas/symbol_profiles/010/010820.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": 11.75, "MFE_90D_pct": 20.79, "MFE_180D_pct": 25.08, "MFE_1Y_pct": null, "MFE_2Y_pct": null, "MAE_30D_pct": -17.3, "MAE_90D_pct": -17.3, "MAE_180D_pct": -17.3, "MAE_1Y_pct": null, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2023-04-06", "peak_price": 3940, "drawdown_after_peak_pct": -13.45, "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": 0.47, "four_b_full_window_peak_proximity": 0.47, "four_b_timing_verdict": "price_only_local_4B_too_early_vs_full_window_spike", "four_b_evidence_type": ["price_only", "positioning_overheat"], "four_c_protection_label": "thesis_break_watch_only", "trigger_outcome_label": "intermittent_MFE_but_high_MAE_without_export_backlog", "current_profile_verdict": "current_profile_false_positive", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window", "same_entry_group_id": "R11L73_C03_010820_20221004_NK_MISSILE_PRICE_ONLY_HIGH_MAE::2022-10-04::3150", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R11L73_C03_012450_20220728_POLAND_K9_FRAMEWORK_BACKLOG", "trigger_id": "R11L73_T012450_20220728_STAGE2A", "symbol": "012450", "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "canonical_archetype_id": "C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG", "raw_component_scores_before": {"contract_score": 13, "backlog_visibility_score": 16, "margin_bridge_score": 6, "revision_score": 12, "relative_strength_score": 14, "customer_quality_score": 14, "policy_or_regulatory_score": 13, "valuation_repricing_score": 2, "execution_risk_score": 4, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_before": 84, "stage_label_before": "Stage3-Yellow / strong Stage2-Actionable", "raw_component_scores_after": {"contract_score": 13, "backlog_visibility_score": 16, "margin_bridge_score": 6, "revision_score": 12, "relative_strength_score": 14, "customer_quality_score": 14, "policy_or_regulatory_score": 13, "valuation_repricing_score": 2, "execution_risk_score": 4, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_after": 84, "stage_label_after": "Stage3-Yellow / strong Stage2-Actionable", "changed_components": ["contract_score", "backlog_visibility_score", "customer_quality_score", "relative_strength_score", "policy_or_regulatory_score", "execution_risk_score"], "component_delta_explanation": "C03 shadow rule gives a narrow positive bridge only when a policy/war-driven event is tied to named buyer, framework size, and order/backlog conversion path.", "MFE_90D_pct": 61.64, "MAE_90D_pct": -3.17, "score_return_alignment_label": "export_framework_backlog_structural_success", "current_profile_verdict": "current_profile_correct"}
{"row_type": "score_simulation", "profile_id": "e2r_2_0_baseline_reference", "case_id": "R11L73_C03_012450_20220728_POLAND_K9_FRAMEWORK_BACKLOG", "trigger_id": "R11L73_T012450_20220728_STAGE2A", "symbol": "012450", "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "canonical_archetype_id": "C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG", "raw_component_scores_before": {"contract_score": 13, "backlog_visibility_score": 16, "margin_bridge_score": 6, "revision_score": 12, "relative_strength_score": 14, "customer_quality_score": 14, "policy_or_regulatory_score": 13, "valuation_repricing_score": 2, "execution_risk_score": 4, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_before": 84, "stage_label_before": "Stage3-Yellow / strong Stage2-Actionable", "raw_component_scores_after": {"contract_score": 13, "backlog_visibility_score": 16, "margin_bridge_score": 6, "revision_score": 12, "relative_strength_score": 14, "customer_quality_score": 14, "policy_or_regulatory_score": 13, "valuation_repricing_score": 2, "execution_risk_score": 4, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_after": 79, "stage_label_after": "Stage2-Actionable / strong Stage2-Actionable", "changed_components": ["contract_score", "backlog_visibility_score", "customer_quality_score", "relative_strength_score", "policy_or_regulatory_score", "execution_risk_score"], "component_delta_explanation": "C03 shadow rule gives a narrow positive bridge only when a policy/war-driven event is tied to named buyer, framework size, and order/backlog conversion path.", "MFE_90D_pct": 61.64, "MAE_90D_pct": -3.17, "score_return_alignment_label": "export_framework_backlog_structural_success", "current_profile_verdict": "current_profile_correct"}
{"row_type": "score_simulation", "profile_id": "sector_specific_candidate_profile", "case_id": "R11L73_C03_012450_20220728_POLAND_K9_FRAMEWORK_BACKLOG", "trigger_id": "R11L73_T012450_20220728_STAGE2A", "symbol": "012450", "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "canonical_archetype_id": "C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG", "raw_component_scores_before": {"contract_score": 13, "backlog_visibility_score": 16, "margin_bridge_score": 6, "revision_score": 12, "relative_strength_score": 14, "customer_quality_score": 14, "policy_or_regulatory_score": 13, "valuation_repricing_score": 2, "execution_risk_score": 4, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_before": 84, "stage_label_before": "Stage3-Yellow / strong Stage2-Actionable", "raw_component_scores_after": {"contract_score": 16, "backlog_visibility_score": 20, "margin_bridge_score": 8, "revision_score": 12, "relative_strength_score": 13, "customer_quality_score": 16, "policy_or_regulatory_score": 12, "valuation_repricing_score": 2, "execution_risk_score": 3, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_after": 88, "stage_label_after": "Stage3-Green-shadow / export framework backlog quality", "changed_components": ["contract_score", "backlog_visibility_score", "customer_quality_score", "relative_strength_score", "policy_or_regulatory_score", "execution_risk_score"], "component_delta_explanation": "C03 shadow rule gives a narrow positive bridge only when a policy/war-driven event is tied to named buyer, framework size, and order/backlog conversion path.", "MFE_90D_pct": 61.64, "MAE_90D_pct": -3.17, "score_return_alignment_label": "export_framework_backlog_structural_success", "current_profile_verdict": "current_profile_correct"}
{"row_type": "score_simulation", "profile_id": "canonical_archetype_candidate_profile", "case_id": "R11L73_C03_012450_20220728_POLAND_K9_FRAMEWORK_BACKLOG", "trigger_id": "R11L73_T012450_20220728_STAGE2A", "symbol": "012450", "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "canonical_archetype_id": "C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG", "raw_component_scores_before": {"contract_score": 13, "backlog_visibility_score": 16, "margin_bridge_score": 6, "revision_score": 12, "relative_strength_score": 14, "customer_quality_score": 14, "policy_or_regulatory_score": 13, "valuation_repricing_score": 2, "execution_risk_score": 4, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_before": 84, "stage_label_before": "Stage3-Yellow / strong Stage2-Actionable", "raw_component_scores_after": {"contract_score": 16, "backlog_visibility_score": 20, "margin_bridge_score": 8, "revision_score": 12, "relative_strength_score": 13, "customer_quality_score": 16, "policy_or_regulatory_score": 12, "valuation_repricing_score": 2, "execution_risk_score": 3, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_after": 88, "stage_label_after": "Stage3-Green-shadow / export framework backlog quality", "changed_components": ["contract_score", "backlog_visibility_score", "customer_quality_score", "relative_strength_score", "policy_or_regulatory_score", "execution_risk_score"], "component_delta_explanation": "C03 shadow rule gives a narrow positive bridge only when a policy/war-driven event is tied to named buyer, framework size, and order/backlog conversion path.", "MFE_90D_pct": 61.64, "MAE_90D_pct": -3.17, "score_return_alignment_label": "export_framework_backlog_structural_success", "current_profile_verdict": "current_profile_correct"}
{"row_type": "score_simulation", "profile_id": "counterexample_guard_profile", "case_id": "R11L73_C03_012450_20220728_POLAND_K9_FRAMEWORK_BACKLOG", "trigger_id": "R11L73_T012450_20220728_STAGE2A", "symbol": "012450", "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "canonical_archetype_id": "C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG", "raw_component_scores_before": {"contract_score": 13, "backlog_visibility_score": 16, "margin_bridge_score": 6, "revision_score": 12, "relative_strength_score": 14, "customer_quality_score": 14, "policy_or_regulatory_score": 13, "valuation_repricing_score": 2, "execution_risk_score": 4, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_before": 84, "stage_label_before": "Stage3-Yellow / strong Stage2-Actionable", "raw_component_scores_after": {"contract_score": 16, "backlog_visibility_score": 20, "margin_bridge_score": 8, "revision_score": 12, "relative_strength_score": 13, "customer_quality_score": 16, "policy_or_regulatory_score": 12, "valuation_repricing_score": 2, "execution_risk_score": 3, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_after": 88, "stage_label_after": "Stage3-Green-shadow / export framework backlog quality", "changed_components": ["contract_score", "backlog_visibility_score", "customer_quality_score", "relative_strength_score", "policy_or_regulatory_score", "execution_risk_score"], "component_delta_explanation": "C03 shadow rule gives a narrow positive bridge only when a policy/war-driven event is tied to named buyer, framework size, and order/backlog conversion path.", "MFE_90D_pct": 61.64, "MAE_90D_pct": -3.17, "score_return_alignment_label": "export_framework_backlog_structural_success", "current_profile_verdict": "current_profile_correct"}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R11L73_C03_064350_20220728_POLAND_K2_FRAMEWORK_BACKLOG", "trigger_id": "R11L73_T064350_20220728_STAGE2A", "symbol": "064350", "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "canonical_archetype_id": "C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG", "raw_component_scores_before": {"contract_score": 12, "backlog_visibility_score": 15, "margin_bridge_score": 4, "revision_score": 10, "relative_strength_score": 15, "customer_quality_score": 14, "policy_or_regulatory_score": 12, "valuation_repricing_score": 2, "execution_risk_score": 5, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_before": 82, "stage_label_before": "Stage3-Yellow / export framework visible", "raw_component_scores_after": {"contract_score": 12, "backlog_visibility_score": 15, "margin_bridge_score": 4, "revision_score": 10, "relative_strength_score": 15, "customer_quality_score": 14, "policy_or_regulatory_score": 12, "valuation_repricing_score": 2, "execution_risk_score": 5, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_after": 82, "stage_label_after": "Stage3-Yellow / export framework visible", "changed_components": ["contract_score", "backlog_visibility_score", "customer_quality_score", "relative_strength_score", "policy_or_regulatory_score", "execution_risk_score"], "component_delta_explanation": "C03 export-framework positive should score above theme-only defense names only when buyer/platform/quantity/delivery path are explicit.", "MFE_90D_pct": 31.66, "MAE_90D_pct": -7.62, "score_return_alignment_label": "defense_export_framework_success_with_local_peak_drawdown", "current_profile_verdict": "current_profile_correct"}
{"row_type": "score_simulation", "profile_id": "e2r_2_0_baseline_reference", "case_id": "R11L73_C03_064350_20220728_POLAND_K2_FRAMEWORK_BACKLOG", "trigger_id": "R11L73_T064350_20220728_STAGE2A", "symbol": "064350", "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "canonical_archetype_id": "C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG", "raw_component_scores_before": {"contract_score": 12, "backlog_visibility_score": 15, "margin_bridge_score": 4, "revision_score": 10, "relative_strength_score": 15, "customer_quality_score": 14, "policy_or_regulatory_score": 12, "valuation_repricing_score": 2, "execution_risk_score": 5, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_before": 82, "stage_label_before": "Stage3-Yellow / export framework visible", "raw_component_scores_after": {"contract_score": 12, "backlog_visibility_score": 15, "margin_bridge_score": 4, "revision_score": 10, "relative_strength_score": 15, "customer_quality_score": 14, "policy_or_regulatory_score": 12, "valuation_repricing_score": 2, "execution_risk_score": 5, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_after": 77, "stage_label_after": "Stage2-Actionable / export framework visible", "changed_components": ["contract_score", "backlog_visibility_score", "customer_quality_score", "relative_strength_score", "policy_or_regulatory_score", "execution_risk_score"], "component_delta_explanation": "C03 export-framework positive should score above theme-only defense names only when buyer/platform/quantity/delivery path are explicit.", "MFE_90D_pct": 31.66, "MAE_90D_pct": -7.62, "score_return_alignment_label": "defense_export_framework_success_with_local_peak_drawdown", "current_profile_verdict": "current_profile_correct"}
{"row_type": "score_simulation", "profile_id": "sector_specific_candidate_profile", "case_id": "R11L73_C03_064350_20220728_POLAND_K2_FRAMEWORK_BACKLOG", "trigger_id": "R11L73_T064350_20220728_STAGE2A", "symbol": "064350", "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "canonical_archetype_id": "C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG", "raw_component_scores_before": {"contract_score": 12, "backlog_visibility_score": 15, "margin_bridge_score": 4, "revision_score": 10, "relative_strength_score": 15, "customer_quality_score": 14, "policy_or_regulatory_score": 12, "valuation_repricing_score": 2, "execution_risk_score": 5, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_before": 82, "stage_label_before": "Stage3-Yellow / export framework visible", "raw_component_scores_after": {"contract_score": 15, "backlog_visibility_score": 18, "margin_bridge_score": 5, "revision_score": 10, "relative_strength_score": 14, "customer_quality_score": 16, "policy_or_regulatory_score": 12, "valuation_repricing_score": 2, "execution_risk_score": 4, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_after": 87, "stage_label_after": "Stage3-Green-shadow / export framework backlog quality", "changed_components": ["contract_score", "backlog_visibility_score", "customer_quality_score", "relative_strength_score", "policy_or_regulatory_score", "execution_risk_score"], "component_delta_explanation": "C03 export-framework positive should score above theme-only defense names only when buyer/platform/quantity/delivery path are explicit.", "MFE_90D_pct": 31.66, "MAE_90D_pct": -7.62, "score_return_alignment_label": "defense_export_framework_success_with_local_peak_drawdown", "current_profile_verdict": "current_profile_correct"}
{"row_type": "score_simulation", "profile_id": "canonical_archetype_candidate_profile", "case_id": "R11L73_C03_064350_20220728_POLAND_K2_FRAMEWORK_BACKLOG", "trigger_id": "R11L73_T064350_20220728_STAGE2A", "symbol": "064350", "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "canonical_archetype_id": "C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG", "raw_component_scores_before": {"contract_score": 12, "backlog_visibility_score": 15, "margin_bridge_score": 4, "revision_score": 10, "relative_strength_score": 15, "customer_quality_score": 14, "policy_or_regulatory_score": 12, "valuation_repricing_score": 2, "execution_risk_score": 5, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_before": 82, "stage_label_before": "Stage3-Yellow / export framework visible", "raw_component_scores_after": {"contract_score": 15, "backlog_visibility_score": 18, "margin_bridge_score": 5, "revision_score": 10, "relative_strength_score": 14, "customer_quality_score": 16, "policy_or_regulatory_score": 12, "valuation_repricing_score": 2, "execution_risk_score": 4, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_after": 87, "stage_label_after": "Stage3-Green-shadow / export framework backlog quality", "changed_components": ["contract_score", "backlog_visibility_score", "customer_quality_score", "relative_strength_score", "policy_or_regulatory_score", "execution_risk_score"], "component_delta_explanation": "C03 export-framework positive should score above theme-only defense names only when buyer/platform/quantity/delivery path are explicit.", "MFE_90D_pct": 31.66, "MAE_90D_pct": -7.62, "score_return_alignment_label": "defense_export_framework_success_with_local_peak_drawdown", "current_profile_verdict": "current_profile_correct"}
{"row_type": "score_simulation", "profile_id": "counterexample_guard_profile", "case_id": "R11L73_C03_064350_20220728_POLAND_K2_FRAMEWORK_BACKLOG", "trigger_id": "R11L73_T064350_20220728_STAGE2A", "symbol": "064350", "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "canonical_archetype_id": "C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG", "raw_component_scores_before": {"contract_score": 12, "backlog_visibility_score": 15, "margin_bridge_score": 4, "revision_score": 10, "relative_strength_score": 15, "customer_quality_score": 14, "policy_or_regulatory_score": 12, "valuation_repricing_score": 2, "execution_risk_score": 5, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_before": 82, "stage_label_before": "Stage3-Yellow / export framework visible", "raw_component_scores_after": {"contract_score": 15, "backlog_visibility_score": 18, "margin_bridge_score": 5, "revision_score": 10, "relative_strength_score": 14, "customer_quality_score": 16, "policy_or_regulatory_score": 12, "valuation_repricing_score": 2, "execution_risk_score": 4, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_after": 87, "stage_label_after": "Stage3-Green-shadow / export framework backlog quality", "changed_components": ["contract_score", "backlog_visibility_score", "customer_quality_score", "relative_strength_score", "policy_or_regulatory_score", "execution_risk_score"], "component_delta_explanation": "C03 export-framework positive should score above theme-only defense names only when buyer/platform/quantity/delivery path are explicit.", "MFE_90D_pct": 31.66, "MAE_90D_pct": -7.62, "score_return_alignment_label": "defense_export_framework_success_with_local_peak_drawdown", "current_profile_verdict": "current_profile_correct"}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R11L73_C03_065450_20221004_NK_MISSILE_GEOPOLITICAL_THEME", "trigger_id": "R11L73_T065450_20221004_STAGE2_THEME", "symbol": "065450", "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "canonical_archetype_id": "C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG", "raw_component_scores_before": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 0, "revision_score": 0, "relative_strength_score": 22, "customer_quality_score": 0, "policy_or_regulatory_score": 18, "valuation_repricing_score": 10, "execution_risk_score": 14, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_before": 76, "stage_label_before": "Stage3-Yellow false positive if relative strength + policy shock over-weighted", "raw_component_scores_after": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 0, "revision_score": 0, "relative_strength_score": 22, "customer_quality_score": 0, "policy_or_regulatory_score": 18, "valuation_repricing_score": 10, "execution_risk_score": 14, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_after": 76, "stage_label_after": "Stage3-Yellow false positive if relative strength + policy shock over-weighted", "changed_components": ["contract_score", "backlog_visibility_score", "customer_quality_score", "relative_strength_score", "policy_or_regulatory_score", "execution_risk_score"], "component_delta_explanation": "Defense geopolitical theme rows must be capped at watch/actionable watch unless they gain buyer/order/backlog/revision evidence.", "MFE_90D_pct": 28.77, "MAE_90D_pct": -8.07, "score_return_alignment_label": "geopolitical_theme_price_pop_without_export_backlog", "current_profile_verdict": "current_profile_false_positive"}
{"row_type": "score_simulation", "profile_id": "e2r_2_0_baseline_reference", "case_id": "R11L73_C03_065450_20221004_NK_MISSILE_GEOPOLITICAL_THEME", "trigger_id": "R11L73_T065450_20221004_STAGE2_THEME", "symbol": "065450", "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "canonical_archetype_id": "C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG", "raw_component_scores_before": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 0, "revision_score": 0, "relative_strength_score": 22, "customer_quality_score": 0, "policy_or_regulatory_score": 18, "valuation_repricing_score": 10, "execution_risk_score": 14, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_before": 76, "stage_label_before": "Stage3-Yellow false positive if relative strength + policy shock over-weighted", "raw_component_scores_after": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 0, "revision_score": 0, "relative_strength_score": 22, "customer_quality_score": 0, "policy_or_regulatory_score": 18, "valuation_repricing_score": 10, "execution_risk_score": 14, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_after": 71, "stage_label_after": "Stage2-Actionable false positive if relative strength + policy shock over-weighted", "changed_components": ["contract_score", "backlog_visibility_score", "customer_quality_score", "relative_strength_score", "policy_or_regulatory_score", "execution_risk_score"], "component_delta_explanation": "Defense geopolitical theme rows must be capped at watch/actionable watch unless they gain buyer/order/backlog/revision evidence.", "MFE_90D_pct": 28.77, "MAE_90D_pct": -8.07, "score_return_alignment_label": "geopolitical_theme_price_pop_without_export_backlog", "current_profile_verdict": "current_profile_false_positive"}
{"row_type": "score_simulation", "profile_id": "sector_specific_candidate_profile", "case_id": "R11L73_C03_065450_20221004_NK_MISSILE_GEOPOLITICAL_THEME", "trigger_id": "R11L73_T065450_20221004_STAGE2_THEME", "symbol": "065450", "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "canonical_archetype_id": "C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG", "raw_component_scores_before": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 0, "revision_score": 0, "relative_strength_score": 22, "customer_quality_score": 0, "policy_or_regulatory_score": 18, "valuation_repricing_score": 10, "execution_risk_score": 14, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_before": 76, "stage_label_before": "Stage3-Yellow false positive if relative strength + policy shock over-weighted", "raw_component_scores_after": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 0, "revision_score": 0, "relative_strength_score": 14, "customer_quality_score": 0, "policy_or_regulatory_score": 10, "valuation_repricing_score": 6, "execution_risk_score": 20, "legal_or_contract_risk_score": 4, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_after": 56, "stage_label_after": "Stage2-Watch / defense theme cap", "changed_components": ["contract_score", "backlog_visibility_score", "customer_quality_score", "relative_strength_score", "policy_or_regulatory_score", "execution_risk_score"], "component_delta_explanation": "Defense geopolitical theme rows must be capped at watch/actionable watch unless they gain buyer/order/backlog/revision evidence.", "MFE_90D_pct": 28.77, "MAE_90D_pct": -8.07, "score_return_alignment_label": "geopolitical_theme_price_pop_without_export_backlog", "current_profile_verdict": "current_profile_false_positive"}
{"row_type": "score_simulation", "profile_id": "canonical_archetype_candidate_profile", "case_id": "R11L73_C03_065450_20221004_NK_MISSILE_GEOPOLITICAL_THEME", "trigger_id": "R11L73_T065450_20221004_STAGE2_THEME", "symbol": "065450", "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "canonical_archetype_id": "C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG", "raw_component_scores_before": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 0, "revision_score": 0, "relative_strength_score": 22, "customer_quality_score": 0, "policy_or_regulatory_score": 18, "valuation_repricing_score": 10, "execution_risk_score": 14, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_before": 76, "stage_label_before": "Stage3-Yellow false positive if relative strength + policy shock over-weighted", "raw_component_scores_after": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 0, "revision_score": 0, "relative_strength_score": 14, "customer_quality_score": 0, "policy_or_regulatory_score": 10, "valuation_repricing_score": 6, "execution_risk_score": 20, "legal_or_contract_risk_score": 4, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_after": 56, "stage_label_after": "Stage2-Watch / defense theme cap", "changed_components": ["contract_score", "backlog_visibility_score", "customer_quality_score", "relative_strength_score", "policy_or_regulatory_score", "execution_risk_score"], "component_delta_explanation": "Defense geopolitical theme rows must be capped at watch/actionable watch unless they gain buyer/order/backlog/revision evidence.", "MFE_90D_pct": 28.77, "MAE_90D_pct": -8.07, "score_return_alignment_label": "geopolitical_theme_price_pop_without_export_backlog", "current_profile_verdict": "current_profile_false_positive"}
{"row_type": "score_simulation", "profile_id": "counterexample_guard_profile", "case_id": "R11L73_C03_065450_20221004_NK_MISSILE_GEOPOLITICAL_THEME", "trigger_id": "R11L73_T065450_20221004_STAGE2_THEME", "symbol": "065450", "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "canonical_archetype_id": "C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG", "raw_component_scores_before": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 0, "revision_score": 0, "relative_strength_score": 22, "customer_quality_score": 0, "policy_or_regulatory_score": 18, "valuation_repricing_score": 10, "execution_risk_score": 14, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_before": 76, "stage_label_before": "Stage3-Yellow false positive if relative strength + policy shock over-weighted", "raw_component_scores_after": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 0, "revision_score": 0, "relative_strength_score": 14, "customer_quality_score": 0, "policy_or_regulatory_score": 10, "valuation_repricing_score": 6, "execution_risk_score": 20, "legal_or_contract_risk_score": 4, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_after": 56, "stage_label_after": "Stage2-Watch / defense theme cap", "changed_components": ["contract_score", "backlog_visibility_score", "customer_quality_score", "relative_strength_score", "policy_or_regulatory_score", "execution_risk_score"], "component_delta_explanation": "Defense geopolitical theme rows must be capped at watch/actionable watch unless they gain buyer/order/backlog/revision evidence.", "MFE_90D_pct": 28.77, "MAE_90D_pct": -8.07, "score_return_alignment_label": "geopolitical_theme_price_pop_without_export_backlog", "current_profile_verdict": "current_profile_false_positive"}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R11L73_C03_010820_20221004_NK_MISSILE_PRICE_ONLY_HIGH_MAE", "trigger_id": "R11L73_T010820_20221004_STAGE2_THEME", "symbol": "010820", "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "canonical_archetype_id": "C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG", "raw_component_scores_before": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 0, "revision_score": 0, "relative_strength_score": 20, "customer_quality_score": 0, "policy_or_regulatory_score": 17, "valuation_repricing_score": 9, "execution_risk_score": 15, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_before": 74, "stage_label_before": "Stage2-Actionable false positive if price-only theme is promoted", "raw_component_scores_after": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 0, "revision_score": 0, "relative_strength_score": 20, "customer_quality_score": 0, "policy_or_regulatory_score": 17, "valuation_repricing_score": 9, "execution_risk_score": 15, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_after": 74, "stage_label_after": "Stage2-Actionable false positive if price-only theme is promoted", "changed_components": ["contract_score", "backlog_visibility_score", "customer_quality_score", "relative_strength_score", "policy_or_regulatory_score", "execution_risk_score"], "component_delta_explanation": "High-MAE defense theme MFE should not be mistaken for structural C03 rerating. Require export-framework/backlog evidence for positive promotion.", "MFE_90D_pct": 20.79, "MAE_90D_pct": -17.3, "score_return_alignment_label": "intermittent_MFE_but_high_MAE_without_export_backlog", "current_profile_verdict": "current_profile_false_positive"}
{"row_type": "score_simulation", "profile_id": "e2r_2_0_baseline_reference", "case_id": "R11L73_C03_010820_20221004_NK_MISSILE_PRICE_ONLY_HIGH_MAE", "trigger_id": "R11L73_T010820_20221004_STAGE2_THEME", "symbol": "010820", "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "canonical_archetype_id": "C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG", "raw_component_scores_before": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 0, "revision_score": 0, "relative_strength_score": 20, "customer_quality_score": 0, "policy_or_regulatory_score": 17, "valuation_repricing_score": 9, "execution_risk_score": 15, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_before": 74, "stage_label_before": "Stage2-Actionable false positive if price-only theme is promoted", "raw_component_scores_after": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 0, "revision_score": 0, "relative_strength_score": 20, "customer_quality_score": 0, "policy_or_regulatory_score": 17, "valuation_repricing_score": 9, "execution_risk_score": 15, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_after": 69, "stage_label_after": "Stage2-Actionable false positive if price-only theme is promoted", "changed_components": ["contract_score", "backlog_visibility_score", "customer_quality_score", "relative_strength_score", "policy_or_regulatory_score", "execution_risk_score"], "component_delta_explanation": "High-MAE defense theme MFE should not be mistaken for structural C03 rerating. Require export-framework/backlog evidence for positive promotion.", "MFE_90D_pct": 20.79, "MAE_90D_pct": -17.3, "score_return_alignment_label": "intermittent_MFE_but_high_MAE_without_export_backlog", "current_profile_verdict": "current_profile_false_positive"}
{"row_type": "score_simulation", "profile_id": "sector_specific_candidate_profile", "case_id": "R11L73_C03_010820_20221004_NK_MISSILE_PRICE_ONLY_HIGH_MAE", "trigger_id": "R11L73_T010820_20221004_STAGE2_THEME", "symbol": "010820", "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "canonical_archetype_id": "C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG", "raw_component_scores_before": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 0, "revision_score": 0, "relative_strength_score": 20, "customer_quality_score": 0, "policy_or_regulatory_score": 17, "valuation_repricing_score": 9, "execution_risk_score": 15, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_before": 74, "stage_label_before": "Stage2-Actionable false positive if price-only theme is promoted", "raw_component_scores_after": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 0, "revision_score": 0, "relative_strength_score": 12, "customer_quality_score": 0, "policy_or_regulatory_score": 9, "valuation_repricing_score": 5, "execution_risk_score": 22, "legal_or_contract_risk_score": 5, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_after": 54, "stage_label_after": "Stage2-Watch / high-MAE defense theme guard", "changed_components": ["contract_score", "backlog_visibility_score", "customer_quality_score", "relative_strength_score", "policy_or_regulatory_score", "execution_risk_score"], "component_delta_explanation": "High-MAE defense theme MFE should not be mistaken for structural C03 rerating. Require export-framework/backlog evidence for positive promotion.", "MFE_90D_pct": 20.79, "MAE_90D_pct": -17.3, "score_return_alignment_label": "intermittent_MFE_but_high_MAE_without_export_backlog", "current_profile_verdict": "current_profile_false_positive"}
{"row_type": "score_simulation", "profile_id": "canonical_archetype_candidate_profile", "case_id": "R11L73_C03_010820_20221004_NK_MISSILE_PRICE_ONLY_HIGH_MAE", "trigger_id": "R11L73_T010820_20221004_STAGE2_THEME", "symbol": "010820", "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "canonical_archetype_id": "C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG", "raw_component_scores_before": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 0, "revision_score": 0, "relative_strength_score": 20, "customer_quality_score": 0, "policy_or_regulatory_score": 17, "valuation_repricing_score": 9, "execution_risk_score": 15, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_before": 74, "stage_label_before": "Stage2-Actionable false positive if price-only theme is promoted", "raw_component_scores_after": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 0, "revision_score": 0, "relative_strength_score": 12, "customer_quality_score": 0, "policy_or_regulatory_score": 9, "valuation_repricing_score": 5, "execution_risk_score": 22, "legal_or_contract_risk_score": 5, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_after": 54, "stage_label_after": "Stage2-Watch / high-MAE defense theme guard", "changed_components": ["contract_score", "backlog_visibility_score", "customer_quality_score", "relative_strength_score", "policy_or_regulatory_score", "execution_risk_score"], "component_delta_explanation": "High-MAE defense theme MFE should not be mistaken for structural C03 rerating. Require export-framework/backlog evidence for positive promotion.", "MFE_90D_pct": 20.79, "MAE_90D_pct": -17.3, "score_return_alignment_label": "intermittent_MFE_but_high_MAE_without_export_backlog", "current_profile_verdict": "current_profile_false_positive"}
{"row_type": "score_simulation", "profile_id": "counterexample_guard_profile", "case_id": "R11L73_C03_010820_20221004_NK_MISSILE_PRICE_ONLY_HIGH_MAE", "trigger_id": "R11L73_T010820_20221004_STAGE2_THEME", "symbol": "010820", "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "canonical_archetype_id": "C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG", "raw_component_scores_before": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 0, "revision_score": 0, "relative_strength_score": 20, "customer_quality_score": 0, "policy_or_regulatory_score": 17, "valuation_repricing_score": 9, "execution_risk_score": 15, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_before": 74, "stage_label_before": "Stage2-Actionable false positive if price-only theme is promoted", "raw_component_scores_after": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 0, "revision_score": 0, "relative_strength_score": 12, "customer_quality_score": 0, "policy_or_regulatory_score": 9, "valuation_repricing_score": 5, "execution_risk_score": 22, "legal_or_contract_risk_score": 5, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_after": 54, "stage_label_after": "Stage2-Watch / high-MAE defense theme guard", "changed_components": ["contract_score", "backlog_visibility_score", "customer_quality_score", "relative_strength_score", "policy_or_regulatory_score", "execution_risk_score"], "component_delta_explanation": "High-MAE defense theme MFE should not be mistaken for structural C03 rerating. Require export-framework/backlog evidence for positive promotion.", "MFE_90D_pct": 20.79, "MAE_90D_pct": -17.3, "score_return_alignment_label": "intermittent_MFE_but_high_MAE_without_export_backlog", "current_profile_verdict": "current_profile_false_positive"}
{"row_type": "residual_contribution", "round": "R11", "loop": "73", "scheduled_round": "R11", "scheduled_loop": "73", "round_schedule_status": "valid", "round_sector_consistency": "pass", "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "canonical_archetype_id": "C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG", "new_independent_case_count": 4, "reused_case_count": 0, "new_symbol_count": 4, "same_archetype_new_symbol_count": 4, "same_archetype_new_trigger_family_count": 2, "new_trigger_family_count": 2, "positive_case_count": 2, "counterexample_count": 2, "current_profile_error_count": 2, "diversity_score_summary": "new_symbols=4; new_trigger_families=2; positives=2; counterexamples=2; residual_errors=2; wrong_round_penalty=0; duplicate_key_conflict=0", "tested_existing_calibrated_axes": ["stage2_actionable_evidence_bonus", "stage3_yellow_total_min", "price_only_blowoff_blocks_positive_stage", "full_4b_requires_non_price_evidence"], "residual_error_types_found": ["defense_geopolitical_theme_false_positive", "price_only_local_4B_overlay_not_full_4B", "export_framework_backlog_quality_undercompression"], "loop_contribution_label": "canonical_archetype_rule_candidate", "do_not_propose_new_weight_delta": false}
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
completed_round = R11
completed_loop = 73
next_round = R12
next_loop = 73
round_schedule_status = valid
round_sector_consistency = pass
```

## 28. Source Notes

```text
stock_web_manifest = atlas/manifest.json
stock_web_rows_checked:
  - atlas/ohlcv_tradable_by_symbol_year/012/012450/2022.csv
  - atlas/ohlcv_tradable_by_symbol_year/012/012450/2023.csv
  - atlas/ohlcv_tradable_by_symbol_year/064/064350/2022.csv
  - atlas/ohlcv_tradable_by_symbol_year/064/064350/2023.csv
  - atlas/ohlcv_tradable_by_symbol_year/065/065450/2022.csv
  - atlas/ohlcv_tradable_by_symbol_year/065/065450/2023.csv
  - atlas/ohlcv_tradable_by_symbol_year/010/010820/2022.csv
  - atlas/ohlcv_tradable_by_symbol_year/010/010820/2023.csv
profile_rows_checked:
  - atlas/symbol_profiles/012/012450.json
  - atlas/symbol_profiles/064/064350.json
  - atlas/symbol_profiles/065/065450.json
  - atlas/symbol_profiles/010/010820.json
evidence_sources_used_for_trigger_labels:
  - Reuters, 2025 follow-up articles referencing Poland's 2022 South Korea arms agreements and later Hanwha/Hyundai Rotem follow-on agreements.
  - Public K2/K9/FA-50 export chronology records for the July-August 2022 Poland framework/executive agreements.
  - Historical October 4, 2022 North Korea missile/geopolitical headline family for price-only defense-theme counterexamples.
```

