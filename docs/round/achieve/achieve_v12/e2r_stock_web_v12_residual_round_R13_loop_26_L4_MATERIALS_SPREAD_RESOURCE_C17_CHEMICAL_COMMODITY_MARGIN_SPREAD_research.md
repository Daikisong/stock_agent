# E2R Stock-Web Historical Calibration / Sector-Archetype Residual Research Round

## 0. Research Metadata

| round | loop | large_sector_id | canonical_archetype_id | fine_archetype_id | mode | research_session | production_scoring_changed | shadow_weight_only | stock_web_manifest_max_date |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| R13 | 26 | L4_MATERIALS_SPREAD_RESOURCE | C17_CHEMICAL_COMMODITY_MARGIN_SPREAD | SPREAD_SUPERCYCLE_VS_COMMODITY_PRICE_ONLY_CHEMICALS | historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12 | post_calibrated_sector_archetype_residual_research | False | True | 2026-02-20 |

## 1. Current Calibrated Profile Assumption

current_default_profile_proxy = `e2r_2_1_stock_web_calibrated_proxy`.

Applied global axes treated as already active, not re-proposed: `stage2_actionable_evidence_bonus=+2.0`, `stage3_yellow_total_min=75`, `stage3_green_total_min=87`, `stage3_green_revision_min=55`, `stage3_cross_evidence_green_buffer=+1.5`, `price_only_blowoff_blocks_positive_stage=true`, `full_4b_requires_non_price_evidence=true`, `hard_4c_thesis_break_routes_to_4c=true`.

This loop stress-tests whether **C17 chemical commodity-margin spread** needs an archetype-specific distinction between real spread-duration/margin-bridge evidence and generic commodity-price or naphtha/olefin recovery narratives.

## 2. Round / Large Sector / Canonical Archetype Scope

- round: `R13`
- loop: `26`
- large_sector_id: `L4_MATERIALS_SPREAD_RESOURCE`
- canonical_archetype_id: `C17_CHEMICAL_COMMODITY_MARGIN_SPREAD`
- fine_archetype_id: `SPREAD_SUPERCYCLE_VS_COMMODITY_PRICE_ONLY_CHEMICALS`
- loop_objective: `holdout_validation`, `residual_false_positive_mining`, `green_strictness_stress_test`, `stage2_actionable_bonus_stress_test`, `4B_non_price_requirement_stress_test`, `sector_specific_rule_discovery`, `canonical_archetype_compression`, `counterexample_mining`, `coverage_gap_fill`

## 3. Previous Coverage / Duplicate Avoidance Check

The allowed `stock_agent` research artifact check showed prior ingestion had 107 parsed result MDs, 1,940 validated trigger rows, and 1,376 representative aggregate rows across R1–R13 / loop 1–9. Local generated handoff files also already contain L5, L6, L7, L8, L9, and L10 examples. This loop therefore avoids another financial or consumer rerun and uses a new L4/C17 spread-cycle holdout set: `298020`, `011780`, `011170`, and `006650`.

new_independent_case_ratio = `1.00`.

## 4. Stock-Web OHLC Input / Price Source Validation

| source | source_url | manifest_path | schema_path | universe_path | manifest_max_date | price_basis | price_adjustment_status | calibration_shard_root | raw_shard_root | validation_status |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Songdaiki/stock-web | https://github.com/Songdaiki/stock-web | atlas/manifest.json | atlas/schema.json | atlas/universe/all_symbols.csv | 2026-02-20 | tradable_raw | raw_unadjusted_marcap | atlas/ohlcv_tradable_by_symbol_year | atlas/ohlcv_raw_by_symbol_year | usable_for_historical_calibration |

Manifest facts used: source_name `FinanceData/marcap`; price_adjustment_status `raw_unadjusted_marcap`; min_date `1995-05-02`; max_date `2026-02-20`; tradable_row_count `14354401`; raw_row_count `15214118`; symbol_count `5414`; active_like_symbol_count `2868`; inactive_or_delisted_like_symbol_count `2546`; markets `KONEX, KOSDAQ, KOSDAQ GLOBAL, KOSPI`; calibration_shard_root `atlas/ohlcv_tradable_by_symbol_year`; raw_shard_root `atlas/ohlcv_raw_by_symbol_year`.

## 5. Historical Eligibility Gate

| trigger_id | symbol | company_name | trigger_type | trigger_date | entry_date | entry_price | calibration_usable | forward_window_trading_days | corporate_action_window_status | calibration_block_reasons |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| R13L26_C17_001_T1_STAGE2_ACTIONABLE | 298020 | 효성티앤씨 | Stage2-Actionable | 2021-02-05 | 2021-02-05 | 479000 | True | 180 | clean_180D_window |  |
| R13L26_C17_001_T2_STAGE3_GREEN_LATE | 298020 | 효성티앤씨 | Stage3-Green | 2021-04-16 | 2021-04-16 | 700000 | True | 180 | clean_180D_window |  |
| R13L26_C17_001_T3_4B_VALUATION_OVERHEAT | 298020 | 효성티앤씨 | 4B-Overlay | 2021-07-16 | 2021-07-16 | 881000 | True | 180 | clean_180D_window |  |
| R13L26_C17_002_T1_STAGE2_ACTIONABLE | 011780 | 금호석유화학 | Stage2-Actionable | 2021-01-21 | 2021-01-21 | 186000 | True | 180 | clean_180D_window; profile corporate_action_candidate_dates=[2001-01-16], outside window |  |
| R13L26_C17_002_T2_STAGE3_GREEN_LATE | 011780 | 금호석유화학 | Stage3-Green | 2021-02-05 | 2021-02-05 | 276500 | True | 180 | clean_180D_window; profile corporate_action_candidate_dates=[2001-01-16], outside window |  |
| R13L26_C17_003_T1_STAGE2_YELLOW | 011170 | 롯데케미칼 | Stage2-Yellow | 2021-02-23 | 2021-02-23 | 326000 | True | 180 | clean_180D_window; profile corporate_action_candidate_dates=[2023-02-13], outside window |  |
| R13L26_C17_004_T1_STAGE2_YELLOW | 006650 | 대한유화 | Stage2-Yellow | 2021-02-10 | 2021-02-10 | 373500 | True | 180 | clean_180D_window; profile corporate_action_candidate_dates=[2010-07-13], outside window |  |

All representative and overlay rows have entry dates inside stock-web tradable shards and at least 180 trading days available before the manifest max date. 1Y/2Y fields are present in machine-readable rows but set to `null` in this loop because the proposed shadow weight is calibrated only on the explicitly verified 30D/90D/180D windows.

## 6. Canonical Archetype Compression Map

| fine_archetype_id | canonical_archetype_id | compression_rule |
| --- | --- | --- |
| SPREAD_SUPERCYCLE_VS_COMMODITY_PRICE_ONLY_CHEMICALS | C17_CHEMICAL_COMMODITY_MARGIN_SPREAD | Treat durable product-specific spread expansion plus utilization/customer/product-mix evidence as C17 positive; treat generic feedstock/naphtha/olefin recovery and commodity-price-only moves as guarded C17 until revision breadth and duration are visible. |

## 7. Case Selection Summary

| case_id | symbol | company_name | case_type | positive_or_counterexample | best_trigger | current_profile_verdict | calibration_usable | is_new_independent_case | notes |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| R13L26_C17_001 | 298020 | 효성티앤씨 | structural_success | positive | R13L26_C17_001_T1_STAGE2_ACTIONABLE | current_profile_missed_structural | True | True | Spandex spread supercycle where industry spread and utilization evidence moved before fully confirmed consensus revision; Green was useful confirmation but not the best first trigger. |
| R13L26_C17_002 | 011780 | 금호석유화학 | structural_success | positive | R13L26_C17_002_T1_STAGE2_ACTIONABLE | current_profile_correct | True | True | NB latex / synthetic-rubber spread and product-mix evidence created a clean Stage2 before later earnings confirmation. |
| R13L26_C17_003 | 011170 | 롯데케미칼 | failed_rerating | counterexample | R13L26_C17_003_T1_STAGE2_YELLOW | current_profile_false_positive | True | True | Naphtha/olefin recovery narrative did not convert into durable margin bridge; price path showed low MFE and deep MAE. |
| R13L26_C17_004 | 006650 | 대한유화 | failed_rerating | counterexample | R13L26_C17_004_T1_STAGE2_YELLOW | current_profile_false_positive | True | True | Commodity spread spike looked like C17 at the headline layer, but spread duration/customer-quality/revision breadth were insufficient; peak appeared before durable Stage3 evidence. |

## 8. Positive vs Counterexample Balance

- positive_structural_success: `2` (`298020`, `011780`)
- counterexample_or_failed_rerating: `2` (`011170`, `006650`)
- 4B_or_4C_case: `3` overlay / thesis-break rows (`298020` 4B, `011170` thesis-break fields, `006650` thesis-break fields)
- calibration_usable_case_count: `4`
- calibration_usable_trigger_count: `7`
- representative_trigger_count: `4`

## 9. Evidence Source Map

| case_id | symbol | stage2_evidence_fields | stage3_evidence_fields | stage4b_evidence_fields | stage4c_evidence_fields | evidence_source |
| --- | --- | --- | --- | --- | --- | --- |
| R13L26_C17_001 | 298020 | capacity_or_volume_route, early_revision_signal, public_event_or_disclosure, relative_strength | confirmed_revision, financial_visibility, low_red_team_risk, margin_bridge, multiple_public_sources | margin_or_backlog_slowdown, positioning_overheat, valuation_blowoff |  | public disclosure/news/research-note class; stock-web OHLC verified |
| R13L26_C17_002 | 011780 | capacity_or_volume_route, customer_or_order_quality, early_revision_signal, public_event_or_disclosure, relative_strength | confirmed_revision, financial_visibility, margin_bridge, multiple_public_sources |  |  | public disclosure/news/research-note class; stock-web OHLC verified |
| R13L26_C17_003 | 011170 | public_event_or_disclosure, relative_strength | multiple_public_sources | margin_or_backlog_slowdown | thesis_evidence_broken | public disclosure/news/research-note class; stock-web OHLC verified |
| R13L26_C17_004 | 006650 | public_event_or_disclosure, relative_strength | multiple_public_sources | price_only_local_peak, valuation_blowoff | thesis_evidence_broken | public disclosure/news/research-note class; stock-web OHLC verified |

Evidence is intentionally separated from price. Price rows only determine entry/MFE/MAE; they do not create Stage2/Stage3 evidence.

## 10. Price Data Source Map

| case_id | symbol | company_name | price_shard_path | profile_path | price_basis | price_adjustment_status | manifest_max_date |
| --- | --- | --- | --- | --- | --- | --- | --- |
| R13L26_C17_001 | 298020 | 효성티앤씨 | atlas/ohlcv_tradable_by_symbol_year/298/298020/2021.csv | atlas/symbol_profiles/298/298020.json | tradable_raw | raw_unadjusted_marcap | 2026-02-20 |
| R13L26_C17_002 | 011780 | 금호석유화학 | atlas/ohlcv_tradable_by_symbol_year/011/011780/2021.csv | atlas/symbol_profiles/011/011780.json | tradable_raw | raw_unadjusted_marcap | 2026-02-20 |
| R13L26_C17_003 | 011170 | 롯데케미칼 | atlas/ohlcv_tradable_by_symbol_year/011/011170/2021.csv | atlas/symbol_profiles/011/011170.json | tradable_raw | raw_unadjusted_marcap | 2026-02-20 |
| R13L26_C17_004 | 006650 | 대한유화 | atlas/ohlcv_tradable_by_symbol_year/006/006650/2021.csv | atlas/symbol_profiles/006/006650.json | tradable_raw | raw_unadjusted_marcap | 2026-02-20 |

## 11. Case-by-Case Trigger Grid

| trigger_id | case_id | symbol | company_name | trigger_type | trigger_date | entry_date | entry_price | dedupe_for_aggregate | aggregate_group_role | trigger_outcome_label | current_profile_verdict |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| R13L26_C17_001_T1_STAGE2_ACTIONABLE | R13L26_C17_001 | 298020 | 효성티앤씨 | Stage2-Actionable | 2021-02-05 | 2021-02-05 | 479000 | True | representative | structural_success_spread_to_revision | current_profile_missed_structural |
| R13L26_C17_001_T2_STAGE3_GREEN_LATE | R13L26_C17_001 | 298020 | 효성티앤씨 | Stage3-Green | 2021-04-16 | 2021-04-16 | 700000 | False | label_comparison_only | green_confirmation_after_large_move | current_profile_too_late |
| R13L26_C17_001_T3_4B_VALUATION_OVERHEAT | R13L26_C17_001 | 298020 | 효성티앤씨 | 4B-Overlay | 2021-07-16 | 2021-07-16 | 881000 | False | 4B_overlay_only | good_full_window_4B_timing_after_spread_blowoff | current_profile_correct |
| R13L26_C17_002_T1_STAGE2_ACTIONABLE | R13L26_C17_002 | 011780 | 금호석유화학 | Stage2-Actionable | 2021-01-21 | 2021-01-21 | 186000 | True | representative | structural_success_early_spread_route | current_profile_correct |
| R13L26_C17_002_T2_STAGE3_GREEN_LATE | R13L26_C17_002 | 011780 | 금호석유화학 | Stage3-Green | 2021-02-05 | 2021-02-05 | 276500 | False | label_comparison_only | green_too_late_after_major_spread_move | current_profile_too_late |
| R13L26_C17_003_T1_STAGE2_YELLOW | R13L26_C17_003 | 011170 | 롯데케미칼 | Stage2-Yellow | 2021-02-23 | 2021-02-23 | 326000 | True | representative | false_positive_low_mfe_deep_mae | current_profile_false_positive |
| R13L26_C17_004_T1_STAGE2_YELLOW | R13L26_C17_004 | 006650 | 대한유화 | Stage2-Yellow | 2021-02-10 | 2021-02-10 | 373500 | True | representative | false_positive_peak_before_durable_revision | current_profile_false_positive |

## 12. Trigger-Level OHLC Backtest Tables

| trigger_id | symbol | entry_date | entry_price | MFE_30D_pct | MFE_90D_pct | MFE_180D_pct | MFE_1Y_pct | MFE_2Y_pct | MAE_30D_pct | MAE_90D_pct | MAE_180D_pct | MAE_1Y_pct | below_entry_price_flag_30D | below_entry_price_flag_90D | peak_date | peak_price | drawdown_after_peak_pct |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| R13L26_C17_001_T1_STAGE2_ACTIONABLE | 298020 | 2021-02-05 | 479000 | 19.83 | 76.2 | 101.04 |  |  | -18.16 | -18.16 | -18.16 |  | True | True | 2021-07-16 | 963000 | -38.42 |
| R13L26_C17_001_T2_STAGE3_GREEN_LATE | 298020 | 2021-04-16 | 700000 | 15.71 | 37.57 | 37.57 |  |  | -5.29 | -5.29 | -15.29 |  | True | True | 2021-07-16 | 963000 | -38.42 |
| R13L26_C17_001_T3_4B_VALUATION_OVERHEAT | 298020 | 2021-07-16 | 881000 | 9.31 | 9.31 | 9.31 |  |  | -12.94 | -32.69 | -32.69 |  | True | True | 2021-07-16 | 963000 | -38.42 |
| R13L26_C17_002_T1_STAGE2_ACTIONABLE | 011780 | 2021-01-21 | 186000 | 57.8 | 60.48 | 60.48 |  |  | -2.15 | -2.15 | -3.49 |  | True | True | 2021-05-06 | 298500 | -39.87 |
| R13L26_C17_002_T2_STAGE3_GREEN_LATE | 011780 | 2021-02-05 | 276500 | 6.15 | 7.96 | 7.96 |  |  | -27.67 | -27.67 | -35.08 |  | True | True | 2021-05-06 | 298500 | -39.87 |
| R13L26_C17_003_T1_STAGE2_YELLOW | 011170 | 2021-02-23 | 326000 | 2.45 | 2.45 | 2.45 |  |  | -9.2 | -15.64 | -28.53 |  | True | True | 2021-03-08 | 334000 | -30.24 |
| R13L26_C17_004_T1_STAGE2_YELLOW | 006650 | 2021-02-10 | 373500 | 8.57 | 8.57 | 8.57 |  |  | -16.06 | -29.05 | -41.5 |  | True | True | 2021-02-17 | 405500 | -46.12 |

## 13. Current Calibrated Profile Stress Test

| case_id | symbol | P0 expected behavior | actual path | verdict | stage2_bonus | yellow_threshold | green_threshold | price_only_guard | 4B_non_price_requirement | 4C_routing |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| R13L26_C17_001 | 298020 | May wait for stronger formal revision before Green; Stage2 can be under-weighted if spread evidence is treated as generic cyclicality. | Stage2 entry MFE_180D +101.04%; Green entry still positive but materially later. | current_profile_missed_structural | insufficient for durable spread duration | acceptable | too strict if revision must be fully confirmed first | kept | kept | not primary |
| R13L26_C17_002 | 011780 | Early product-specific spread + relative strength can be Stage2-Actionable. | Stage2 entry MFE_180D +60.48%; late Green MFE_180D only +7.96%. | current_profile_correct | appropriate | acceptable | too late if used as first entry | kept | kept | not primary |
| R13L26_C17_003 | 011170 | Generic naphtha/olefin recovery may be over-promoted as Stage2-Yellow. | MFE_180D +2.45%, MAE_180D -28.53%. | current_profile_false_positive | too generous without spread duration | too low for generic cyclicals | not relevant | kept but needs commodity guard | kept | watch |
| R13L26_C17_004 | 006650 | Headline ethylene/propylene spike may be promoted despite weak duration. | MFE_180D +8.57%, MAE_180D -41.50%. | current_profile_false_positive | too generous without revision breadth | too low for spike-only moves | not relevant | kept but needs commodity guard | kept | watch |

## 14. Stage2 / Yellow / Green Comparison

| case_id | Stage2_Actionable_entry | Stage3_Green_entry | peak_after_stage2 | green_lateness_ratio | interpretation |
| --- | --- | --- | --- | --- | --- |
| R13L26_C17_001 | 479000 | 700000 | 963000 | 0.457 | Green captured confirmation but gave up roughly 45.7% of the Stage2-to-peak upside. |
| R13L26_C17_002 | 186000 | 276500 | 298500 | 0.804 | Green was very late: about 80.4% of the Stage2-to-peak move had already occurred. |
| R13L26_C17_003 | not_applicable | none | 334000 | not_applicable | No valid Green; Yellow should be guarded due poor forward MFE/MAE. |
| R13L26_C17_004 | not_applicable | none | 405500 | not_applicable | No durable Green; early commodity spread spike peaked before thesis could mature. |

## 15. 4B Local vs Full-window Timing Audit

| trigger_id | symbol | entry_price | stage2_anchor | local_peak | full_window_peak | four_b_local_peak_proximity | four_b_full_window_peak_proximity | four_b_timing_verdict | four_b_evidence_type |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| R13L26_C17_001_T3_4B_VALUATION_OVERHEAT | 298020 | 881000 | 479000 | 963000 | 963000 | 0.831 | 0.831 | good_full_window_4B_timing | valuation_blowoff, positioning_overheat, margin_or_backlog_slowdown |
| R13L26_C17_003_T1_STAGE2_YELLOW | 011170 | 326000 | 326000 | 334000 | 334000 |  |  | not_full_4B; counterexample row | margin_or_backlog_slowdown |
| R13L26_C17_004_T1_STAGE2_YELLOW | 006650 | 373500 | 373500 | 405500 | 405500 |  |  | not_full_4B; counterexample row | valuation_blowoff, price_only_local_peak |

## 16. 4C Protection Audit

| case_id | symbol | 4C/Thesis-break label | prior_peak | representative_entry | max_drawdown_after_peak | protection_note |
| --- | --- | --- | --- | --- | --- | --- |
| R13L26_C17_001 | 298020 | thesis_break_watch_only | 963000 | 479000 | -38.42% | 4B overlay protects gains; hard 4C should wait for spread/revision break, not price alone. |
| R13L26_C17_003 | 011170 | hard_4c_success_partial | 334000 | 326000 | -30.24% | A guarded Yellow/Watch label avoids false positive promotion before deep MAE. |
| R13L26_C17_004 | 006650 | hard_4c_success_partial | 405500 | 373500 | -46.12% | Commodity-spike reversal argues for a C17 duration guard. |

## 17. Sector-Specific Rule Candidate

rule_scope = `sector_specific`

Candidate: `l4_spread_duration_margin_bridge_gate`.

Mechanism: in L4 chemical/material spread cycles, price often twitches first because commodity curves move daily. But not every twitch becomes an EPS bridge. The useful signal is when the spread has duration, product/customer specificity, and a visible margin bridge. Without that, the model is listening to thunder and calling it rain.

Proposed shadow behavior:
- Add `+1` to Stage2-Actionable only when spread duration + product/customer specificity + early revision route co-exist.
- Add a guard penalty when the evidence is generic feedstock/naphtha/commodity price recovery without margin bridge.
- Keep price-only blowoff as 4B overlay only.

## 18. Canonical-Archetype Rule Candidate

rule_scope = `canonical_archetype_specific`

Candidate: `c17_chemical_spread_bridge_vs_headline_recovery`.

C17 should compress multiple fine archetypes into two baskets:
1. **durable spread bridge**: spandex, NB latex, product-mix spread, capacity tightness, utilization, and revision visibility.
2. **headline recovery**: olefin/naphtha/ethylene/propylene rebound without duration, customer stickiness, or revision breadth.

Only the first basket can promote Stage2-Actionable. The second can remain Yellow/Watch until revision breadth confirms.

## 19. Before / After Backtest Comparison

| profile_id | profile_scope | profile_hypothesis | changed_axes | changed_thresholds | eligible_trigger_count | selected_entry_trigger_per_case | avg_MFE_90D_pct | avg_MAE_90D_pct | avg_MFE_180D_pct | avg_MAE_180D_pct | false_positive_rate | missed_structural_count | late_green_count | avg_green_lateness_ratio | avg_four_b_local_peak_proximity | avg_four_b_full_window_peak_proximity | score_return_alignment_verdict |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| P0 | current calibrated proxy | global calibrated axes only | none | existing calibrated thresholds | 4 | representative trigger per case | 36.92 | -16.25 | 43.13 | -22.92 | 50% | 1 | 0 | 0.63 | n/a | n/a | mixed: positives captured late; commodity false positives leak through |
| P0b | baseline reference | old E2R 2.0 rollback/reference | no v2.1 calibrated guards | looser | 4 | representative trigger per case | 36.92 | -16.25 | 43.13 | -22.92 | 50% | 2 | 1 | 0.63 | n/a | n/a | worse: too much generic cyclicality promoted |
| P1 | sector_specific_candidate_profile | L4 spread evidence must include duration/customer/product specificity | spread_duration_gate + commodity_price_guard | no production threshold change | 4 | representative trigger per case | 68.34 | -10.15 | 80.76 | -10.82 | 0% | 0 | 1 | 0.63 | 0.831 | 0.831 | better: excludes generic false positives |
| P2 | canonical_archetype_candidate_profile | C17 compression into durable spread bridge vs headline recovery | C17 spread-duration margin bridge + generic feedstock guard | no production threshold change | 4 | representative trigger per case | 68.34 | -10.15 | 80.76 | -10.82 | 0% | 0 | 1 | 0.63 | 0.831 | 0.831 | best candidate for batch ledger |
| P3 | counterexample_guard_profile | Only block generic commodity price-only rows; no positive promotion | generic_commodity_price_guard | no production threshold change | 4 | representative trigger per case | 36.92 | -16.25 | 43.13 | -22.92 | 0% | 1 | 1 | 0.63 | n/a | n/a | safe guard, weaker positive recall |

## 20. Score-Return Alignment Matrix

| trigger_id | symbol | trigger_type | current_profile_verdict | MFE_90D_pct | MAE_90D_pct | MFE_180D_pct | MAE_180D_pct | alignment |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| R13L26_C17_001_T1_STAGE2_ACTIONABLE | 298020 | Stage2-Actionable | current_profile_missed_structural | 76.2 | -18.16 | 101.04 | -18.16 | aligned |
| R13L26_C17_001_T2_STAGE3_GREEN_LATE | 298020 | Stage3-Green | current_profile_too_late | 37.57 | -5.29 | 37.57 | -15.29 | aligned |
| R13L26_C17_001_T3_4B_VALUATION_OVERHEAT | 298020 | 4B-Overlay | current_profile_correct | 9.31 | -32.69 | 9.31 | -32.69 | aligned |
| R13L26_C17_002_T1_STAGE2_ACTIONABLE | 011780 | Stage2-Actionable | current_profile_correct | 60.48 | -2.15 | 60.48 | -3.49 | aligned |
| R13L26_C17_002_T2_STAGE3_GREEN_LATE | 011780 | Stage3-Green | current_profile_too_late | 7.96 | -27.67 | 7.96 | -35.08 | aligned |
| R13L26_C17_003_T1_STAGE2_YELLOW | 011170 | Stage2-Yellow | current_profile_false_positive | 2.45 | -15.64 | 2.45 | -28.53 | misaligned |
| R13L26_C17_004_T1_STAGE2_YELLOW | 006650 | Stage2-Yellow | current_profile_false_positive | 8.57 | -29.05 | 8.57 | -41.5 | misaligned |

## 21. Coverage Matrix

| large_sector_id | canonical_archetype_id | fine_archetype_id | positive_case_count | counterexample_count | 4B_case_count | 4C_case_count | new_independent_case_count | reused_case_count | calibration_usable_trigger_count | representative_trigger_count | current_profile_error_count | sector_rule_candidate | canonical_rule_candidate | coverage_gap_after_this_loop |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| L4_MATERIALS_SPREAD_RESOURCE | C17_CHEMICAL_COMMODITY_MARGIN_SPREAD | SPREAD_SUPERCYCLE_VS_COMMODITY_PRICE_ONLY_CHEMICALS | 2 | 2 | 1 | 2 | 4 | 0 | 7 | 4 | 3 | True | True | C17 now has positive/counterexample balance for durable-spread vs headline-commodity distinction; more holdout in materials/resource C15/C16 still needed. |

## 22. Residual Contribution Summary

new_independent_case_count: `4`
reused_case_count: `0`
reused_case_ids: `[]`
new_symbol_count: `4`
new_canonical_archetype_count: `1`
new_fine_archetype_count: `4`
new_trigger_family_count: `4`
tested_existing_calibrated_axes: `stage2_actionable_evidence_bonus`, `stage3_green_revision_min`, `price_only_blowoff_blocks_positive_stage`, `full_4b_requires_non_price_evidence`
residual_error_types_found: `generic_commodity_price_false_positive`, `green_after_spread_move_lateness`, `spread_duration_missing_guard`
new_axis_proposed: `c17_spread_duration_margin_bridge_gate`, `c17_generic_feedstock_recovery_guard`
existing_axis_strengthened: `price_only_blowoff_blocks_positive_stage`, `full_4b_requires_non_price_evidence`
existing_axis_weakened: `null`
existing_axis_kept: `stage2_actionable_evidence_bonus`, `stage3_yellow_total_min`, `stage3_green_total_min`, `stage3_green_revision_min`, `stage3_cross_evidence_green_buffer`, `hard_4c_thesis_break_routes_to_4c`
sector_specific_rule_candidate: `true`
canonical_archetype_rule_candidate: `true`
no_new_signal_reason: `null`

loop_contribution_label: `canonical_archetype_rule_candidate`

## 23. Validation Scope / Non-Validation Scope

Validation scope:
- Historical trigger-level calibration only.
- Actual stock-web tradable OHLC rows for entry, peak, MFE, MAE, and drawdown.
- Clean 180D windows based on symbol profile corporate-action candidate dates.
- Shadow-only sector/canonical rule proposal.

Non-validation scope:
- No current/live candidate discovery.
- No investment recommendation.
- No `stock_agent` source code inspection.
- No production scoring change.
- No brokerage, auto-trading, or live scanner work.
- 1Y/2Y metrics are intentionally not used for the quantitative shadow delta in this MD.

## 24. Shadow Weight Calibration

```csv
row_type,axis,scope,large_sector_id,canonical_archetype_id,baseline_value,tested_value,delta,reason,backtest_effect,trigger_ids,calibration_usable_count,new_independent_case_count,counterexample_count,confidence,proposal_type,notes
shadow_weight,c17_spread_duration_margin_bridge_gate,canonical_archetype_specific,L4_MATERIALS_SPREAD_RESOURCE,C17_CHEMICAL_COMMODITY_MARGIN_SPREAD,0,1,+1,"Promote C17 only when spread duration plus product/customer specificity and margin bridge are present.","Improves separation between 298020/011780 positives and 011170/006650 false positives.","R13L26_C17_001_T1_STAGE2_ACTIONABLE|R13L26_C17_002_T1_STAGE2_ACTIONABLE|R13L26_C17_003_T1_STAGE2_YELLOW|R13L26_C17_004_T1_STAGE2_YELLOW",4,4,2,medium,canonical_shadow_only,"not production; post-calibrated residual"
shadow_weight,c17_generic_feedstock_recovery_guard,canonical_archetype_specific,L4_MATERIALS_SPREAD_RESOURCE,C17_CHEMICAL_COMMODITY_MARGIN_SPREAD,0,1,+1,"Guard generic olefin/naphtha/headline commodity recovery without revision breadth.","Blocks low-MFE/deep-MAE rows in 011170 and 006650.","R13L26_C17_003_T1_STAGE2_YELLOW|R13L26_C17_004_T1_STAGE2_YELLOW",2,2,2,medium,counterexample_guard,"not production; post-calibrated residual"
shadow_weight,c17_price_only_blowoff_4b_overlay,sector_specific,L4_MATERIALS_SPREAD_RESOURCE,C17_CHEMICAL_COMMODITY_MARGIN_SPREAD,0,1,+1,"Treat late price/valuation blowoff as 4B overlay, not positive-stage evidence.","Keeps 298020 late overheat row out of aggregate positive promotion.","R13L26_C17_001_T3_4B_VALUATION_OVERHEAT",1,1,0,low,sector_shadow_only,"not production; post-calibrated residual"
```

## 25. Machine-Readable Rows

```jsonl
{"row_type": "price_source_validation", "source": "Songdaiki/stock-web", "source_url": "https://github.com/Songdaiki/stock-web", "manifest_path": "atlas/manifest.json", "schema_path": "atlas/schema.json", "universe_path": "atlas/universe/all_symbols.csv", "manifest_max_date": "2026-02-20", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "raw_shard_root": "atlas/ohlcv_raw_by_symbol_year", "validation_status": "usable_for_historical_calibration"}
{"row_type": "case", "case_id": "R13L26_C17_001", "symbol": "298020", "company_name": "효성티앤씨", "round": "R13", "loop": "26", "large_sector_id": "L4_MATERIALS_SPREAD_RESOURCE", "canonical_archetype_id": "C17_CHEMICAL_COMMODITY_MARGIN_SPREAD", "fine_archetype_id": "SPREAD_SUPERCYCLE_VS_COMMODITY_PRICE_ONLY_CHEMICALS", "case_type": "structural_success", "positive_or_counterexample": "positive", "best_trigger": "R13L26_C17_001_T1_STAGE2_ACTIONABLE", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "aligned_positive", "current_profile_verdict": "current_profile_missed_structural", "price_source": "Songdaiki/stock-web", "notes": "Spandex spread supercycle where industry spread and utilization evidence moved before fully confirmed consensus revision; Green was useful confirmation but not the best first trigger."}
{"row_type": "case", "case_id": "R13L26_C17_002", "symbol": "011780", "company_name": "금호석유화학", "round": "R13", "loop": "26", "large_sector_id": "L4_MATERIALS_SPREAD_RESOURCE", "canonical_archetype_id": "C17_CHEMICAL_COMMODITY_MARGIN_SPREAD", "fine_archetype_id": "SPREAD_SUPERCYCLE_VS_COMMODITY_PRICE_ONLY_CHEMICALS", "case_type": "structural_success", "positive_or_counterexample": "positive", "best_trigger": "R13L26_C17_002_T1_STAGE2_ACTIONABLE", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "aligned_positive", "current_profile_verdict": "current_profile_correct", "price_source": "Songdaiki/stock-web", "notes": "NB latex / synthetic-rubber spread and product-mix evidence created a clean Stage2 before later earnings confirmation."}
{"row_type": "case", "case_id": "R13L26_C17_003", "symbol": "011170", "company_name": "롯데케미칼", "round": "R13", "loop": "26", "large_sector_id": "L4_MATERIALS_SPREAD_RESOURCE", "canonical_archetype_id": "C17_CHEMICAL_COMMODITY_MARGIN_SPREAD", "fine_archetype_id": "SPREAD_SUPERCYCLE_VS_COMMODITY_PRICE_ONLY_CHEMICALS", "case_type": "failed_rerating", "positive_or_counterexample": "counterexample", "best_trigger": "R13L26_C17_003_T1_STAGE2_YELLOW", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "false_positive_block_needed", "current_profile_verdict": "current_profile_false_positive", "price_source": "Songdaiki/stock-web", "notes": "Naphtha/olefin recovery narrative did not convert into durable margin bridge; price path showed low MFE and deep MAE."}
{"row_type": "case", "case_id": "R13L26_C17_004", "symbol": "006650", "company_name": "대한유화", "round": "R13", "loop": "26", "large_sector_id": "L4_MATERIALS_SPREAD_RESOURCE", "canonical_archetype_id": "C17_CHEMICAL_COMMODITY_MARGIN_SPREAD", "fine_archetype_id": "SPREAD_SUPERCYCLE_VS_COMMODITY_PRICE_ONLY_CHEMICALS", "case_type": "failed_rerating", "positive_or_counterexample": "counterexample", "best_trigger": "R13L26_C17_004_T1_STAGE2_YELLOW", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "false_positive_block_needed", "current_profile_verdict": "current_profile_false_positive", "price_source": "Songdaiki/stock-web", "notes": "Commodity spread spike looked like C17 at the headline layer, but spread duration/customer-quality/revision breadth were insufficient; peak appeared before durable Stage3 evidence."}
{"row_type": "trigger", "trigger_id": "R13L26_C17_001_T1_STAGE2_ACTIONABLE", "case_id": "R13L26_C17_001", "symbol": "298020", "company_name": "효성티앤씨", "round": "R13", "loop": "26", "large_sector_id": "L4_MATERIALS_SPREAD_RESOURCE", "canonical_archetype_id": "C17_CHEMICAL_COMMODITY_MARGIN_SPREAD", "fine_archetype_id": "SPREAD_SUPERCYCLE_VS_COMMODITY_PRICE_ONLY_CHEMICALS", "sector": "화학·섬유 소재", "primary_archetype": "spandex_spread_supercycle", "loop_objective": "sector_specific_rule_discovery|canonical_archetype_compression|counterexample_mining|4B_non_price_requirement_stress_test|coverage_gap_fill", "trigger_type": "Stage2-Actionable", "trigger_date": "2021-02-05", "evidence_available_at_that_date": "Spandex spread/utilization and earnings revision route available around early-Feb 2021; stock-web 2021 shard row shows entry close 479000.", "evidence_source": "public earnings/disclosure/news/research-note class; price verified by Songdaiki/stock-web shard", "stage2_evidence_fields": ["public_event_or_disclosure", "relative_strength", "capacity_or_volume_route", "early_revision_signal"], "stage3_evidence_fields": ["confirmed_revision", "margin_bridge", "financial_visibility", "multiple_public_sources"], "stage4b_evidence_fields": [], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/298/298020/2021.csv", "profile_path": "atlas/symbol_profiles/298/298020.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "entry_date": "2021-02-05", "entry_price": 479000, "MFE_30D_pct": 19.83, "MFE_90D_pct": 76.2, "MFE_180D_pct": 101.04, "MFE_1Y_pct": null, "MFE_2Y_pct": null, "MAE_30D_pct": -18.16, "MAE_90D_pct": -18.16, "MAE_180D_pct": -18.16, "MAE_1Y_pct": null, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2021-07-16", "peak_price": 963000, "drawdown_after_peak_pct": -38.42, "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": null, "four_b_full_window_peak_proximity": null, "four_b_timing_verdict": "not_4B_row", "four_b_evidence_type": [], "four_c_protection_label": null, "trigger_outcome_label": "structural_success_spread_to_revision", "current_profile_verdict": "current_profile_missed_structural", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window", "same_entry_group_id": "R13L26_C17_001_2021-02-05_479000", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false}
{"row_type": "trigger", "trigger_id": "R13L26_C17_001_T2_STAGE3_GREEN_LATE", "case_id": "R13L26_C17_001", "symbol": "298020", "company_name": "효성티앤씨", "round": "R13", "loop": "26", "large_sector_id": "L4_MATERIALS_SPREAD_RESOURCE", "canonical_archetype_id": "C17_CHEMICAL_COMMODITY_MARGIN_SPREAD", "fine_archetype_id": "SPREAD_SUPERCYCLE_VS_COMMODITY_PRICE_ONLY_CHEMICALS", "sector": "화학·섬유 소재", "primary_archetype": "spandex_spread_supercycle", "loop_objective": "sector_specific_rule_discovery|canonical_archetype_compression|counterexample_mining|4B_non_price_requirement_stress_test|coverage_gap_fill", "trigger_type": "Stage3-Green", "trigger_date": "2021-04-16", "evidence_available_at_that_date": "Formal earnings/revision confirmation after earlier spread move; used only for Green lateness comparison.", "evidence_source": "public earnings/disclosure/news/research-note class; price verified by Songdaiki/stock-web shard", "stage2_evidence_fields": ["relative_strength", "capacity_or_volume_route"], "stage3_evidence_fields": ["confirmed_revision", "margin_bridge", "financial_visibility", "low_red_team_risk"], "stage4b_evidence_fields": [], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/298/298020/2021.csv", "profile_path": "atlas/symbol_profiles/298/298020.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "entry_date": "2021-04-16", "entry_price": 700000, "MFE_30D_pct": 15.71, "MFE_90D_pct": 37.57, "MFE_180D_pct": 37.57, "MFE_1Y_pct": null, "MFE_2Y_pct": null, "MAE_30D_pct": -5.29, "MAE_90D_pct": -5.29, "MAE_180D_pct": -15.29, "MAE_1Y_pct": null, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2021-07-16", "peak_price": 963000, "drawdown_after_peak_pct": -38.42, "green_lateness_ratio": 0.457, "four_b_local_peak_proximity": null, "four_b_full_window_peak_proximity": null, "four_b_timing_verdict": "not_4B_row", "four_b_evidence_type": [], "four_c_protection_label": null, "trigger_outcome_label": "green_confirmation_after_large_move", "current_profile_verdict": "current_profile_too_late", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window", "same_entry_group_id": "R13L26_C17_001_2021-04-16_700000", "dedupe_for_aggregate": false, "aggregate_group_role": "label_comparison_only", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false}
{"row_type": "trigger", "trigger_id": "R13L26_C17_001_T3_4B_VALUATION_OVERHEAT", "case_id": "R13L26_C17_001", "symbol": "298020", "company_name": "효성티앤씨", "round": "R13", "loop": "26", "large_sector_id": "L4_MATERIALS_SPREAD_RESOURCE", "canonical_archetype_id": "C17_CHEMICAL_COMMODITY_MARGIN_SPREAD", "fine_archetype_id": "SPREAD_SUPERCYCLE_VS_COMMODITY_PRICE_ONLY_CHEMICALS", "sector": "화학·섬유 소재", "primary_archetype": "spandex_spread_supercycle", "loop_objective": "sector_specific_rule_discovery|canonical_archetype_compression|counterexample_mining|4B_non_price_requirement_stress_test|coverage_gap_fill", "trigger_type": "4B-Overlay", "trigger_date": "2021-07-16", "evidence_available_at_that_date": "Valuation/positioning overheat after full spread-rerating; not a positive-stage promotion row.", "evidence_source": "public earnings/disclosure/news/research-note class; price verified by Songdaiki/stock-web shard", "stage2_evidence_fields": [], "stage3_evidence_fields": [], "stage4b_evidence_fields": ["valuation_blowoff", "positioning_overheat", "margin_or_backlog_slowdown"], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/298/298020/2021.csv", "profile_path": "atlas/symbol_profiles/298/298020.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "entry_date": "2021-07-16", "entry_price": 881000, "MFE_30D_pct": 9.31, "MFE_90D_pct": 9.31, "MFE_180D_pct": 9.31, "MFE_1Y_pct": null, "MFE_2Y_pct": null, "MAE_30D_pct": -12.94, "MAE_90D_pct": -32.69, "MAE_180D_pct": -32.69, "MAE_1Y_pct": null, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2021-07-16", "peak_price": 963000, "drawdown_after_peak_pct": -38.42, "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": 0.831, "four_b_full_window_peak_proximity": 0.831, "four_b_timing_verdict": "good_full_window_4B_timing", "four_b_evidence_type": ["valuation_blowoff", "positioning_overheat", "margin_or_backlog_slowdown"], "four_c_protection_label": null, "trigger_outcome_label": "good_full_window_4B_timing_after_spread_blowoff", "current_profile_verdict": "current_profile_correct", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window", "same_entry_group_id": "R13L26_C17_001_2021-07-16_881000", "dedupe_for_aggregate": false, "aggregate_group_role": "4B_overlay_only", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false}
{"row_type": "trigger", "trigger_id": "R13L26_C17_002_T1_STAGE2_ACTIONABLE", "case_id": "R13L26_C17_002", "symbol": "011780", "company_name": "금호석유화학", "round": "R13", "loop": "26", "large_sector_id": "L4_MATERIALS_SPREAD_RESOURCE", "canonical_archetype_id": "C17_CHEMICAL_COMMODITY_MARGIN_SPREAD", "fine_archetype_id": "SPREAD_SUPERCYCLE_VS_COMMODITY_PRICE_ONLY_CHEMICALS", "sector": "화학·합성고무", "primary_archetype": "synthetic_rubber_nb_latex_spread", "loop_objective": "sector_specific_rule_discovery|canonical_archetype_compression|counterexample_mining|4B_non_price_requirement_stress_test|coverage_gap_fill", "trigger_type": "Stage2-Actionable", "trigger_date": "2021-01-21", "evidence_available_at_that_date": "NB latex / synthetic rubber spread route and relative strength were visible before later full revision confirmation.", "evidence_source": "public earnings/disclosure/news/research-note class; price verified by Songdaiki/stock-web shard", "stage2_evidence_fields": ["public_event_or_disclosure", "customer_or_order_quality", "relative_strength", "capacity_or_volume_route", "early_revision_signal"], "stage3_evidence_fields": ["confirmed_revision", "margin_bridge", "multiple_public_sources", "financial_visibility"], "stage4b_evidence_fields": [], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/011/011780/2021.csv", "profile_path": "atlas/symbol_profiles/011/011780.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "entry_date": "2021-01-21", "entry_price": 186000, "MFE_30D_pct": 57.8, "MFE_90D_pct": 60.48, "MFE_180D_pct": 60.48, "MFE_1Y_pct": null, "MFE_2Y_pct": null, "MAE_30D_pct": -2.15, "MAE_90D_pct": -2.15, "MAE_180D_pct": -3.49, "MAE_1Y_pct": null, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2021-05-06", "peak_price": 298500, "drawdown_after_peak_pct": -39.87, "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": null, "four_b_full_window_peak_proximity": null, "four_b_timing_verdict": "not_4B_row", "four_b_evidence_type": [], "four_c_protection_label": null, "trigger_outcome_label": "structural_success_early_spread_route", "current_profile_verdict": "current_profile_correct", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window; profile corporate_action_candidate_dates=[2001-01-16], outside window", "same_entry_group_id": "R13L26_C17_002_2021-01-21_186000", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false}
{"row_type": "trigger", "trigger_id": "R13L26_C17_002_T2_STAGE3_GREEN_LATE", "case_id": "R13L26_C17_002", "symbol": "011780", "company_name": "금호석유화학", "round": "R13", "loop": "26", "large_sector_id": "L4_MATERIALS_SPREAD_RESOURCE", "canonical_archetype_id": "C17_CHEMICAL_COMMODITY_MARGIN_SPREAD", "fine_archetype_id": "SPREAD_SUPERCYCLE_VS_COMMODITY_PRICE_ONLY_CHEMICALS", "sector": "화학·합성고무", "primary_archetype": "synthetic_rubber_nb_latex_spread", "loop_objective": "sector_specific_rule_discovery|canonical_archetype_compression|counterexample_mining|4B_non_price_requirement_stress_test|coverage_gap_fill", "trigger_type": "Stage3-Green", "trigger_date": "2021-02-05", "evidence_available_at_that_date": "Later confirmation row shows why C17 needs spread-duration evidence to count earlier than formal Green.", "evidence_source": "public earnings/disclosure/news/research-note class; price verified by Songdaiki/stock-web shard", "stage2_evidence_fields": ["public_event_or_disclosure", "relative_strength"], "stage3_evidence_fields": ["confirmed_revision", "margin_bridge", "financial_visibility"], "stage4b_evidence_fields": [], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/011/011780/2021.csv", "profile_path": "atlas/symbol_profiles/011/011780.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "entry_date": "2021-02-05", "entry_price": 276500, "MFE_30D_pct": 6.15, "MFE_90D_pct": 7.96, "MFE_180D_pct": 7.96, "MFE_1Y_pct": null, "MFE_2Y_pct": null, "MAE_30D_pct": -27.67, "MAE_90D_pct": -27.67, "MAE_180D_pct": -35.08, "MAE_1Y_pct": null, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2021-05-06", "peak_price": 298500, "drawdown_after_peak_pct": -39.87, "green_lateness_ratio": 0.804, "four_b_local_peak_proximity": null, "four_b_full_window_peak_proximity": null, "four_b_timing_verdict": "not_4B_row", "four_b_evidence_type": [], "four_c_protection_label": null, "trigger_outcome_label": "green_too_late_after_major_spread_move", "current_profile_verdict": "current_profile_too_late", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window; profile corporate_action_candidate_dates=[2001-01-16], outside window", "same_entry_group_id": "R13L26_C17_002_2021-02-05_276500", "dedupe_for_aggregate": false, "aggregate_group_role": "label_comparison_only", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false}
{"row_type": "trigger", "trigger_id": "R13L26_C17_003_T1_STAGE2_YELLOW", "case_id": "R13L26_C17_003", "symbol": "011170", "company_name": "롯데케미칼", "round": "R13", "loop": "26", "large_sector_id": "L4_MATERIALS_SPREAD_RESOURCE", "canonical_archetype_id": "C17_CHEMICAL_COMMODITY_MARGIN_SPREAD", "fine_archetype_id": "SPREAD_SUPERCYCLE_VS_COMMODITY_PRICE_ONLY_CHEMICALS", "sector": "화학·석유화학", "primary_archetype": "naphtha_olefin_spread_false_positive", "loop_objective": "sector_specific_rule_discovery|canonical_archetype_compression|counterexample_mining|4B_non_price_requirement_stress_test|coverage_gap_fill", "trigger_type": "Stage2-Yellow", "trigger_date": "2021-02-23", "evidence_available_at_that_date": "Olefin/naphtha recovery narrative without durable spread duration or revision breadth; subsequent OHLC showed poor alignment.", "evidence_source": "public earnings/disclosure/news/research-note class; price verified by Songdaiki/stock-web shard", "stage2_evidence_fields": ["public_event_or_disclosure", "relative_strength"], "stage3_evidence_fields": ["multiple_public_sources"], "stage4b_evidence_fields": ["margin_or_backlog_slowdown"], "stage4c_evidence_fields": ["thesis_evidence_broken"], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/011/011170/2021.csv", "profile_path": "atlas/symbol_profiles/011/011170.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "entry_date": "2021-02-23", "entry_price": 326000, "MFE_30D_pct": 2.45, "MFE_90D_pct": 2.45, "MFE_180D_pct": 2.45, "MFE_1Y_pct": null, "MFE_2Y_pct": null, "MAE_30D_pct": -9.2, "MAE_90D_pct": -15.64, "MAE_180D_pct": -28.53, "MAE_1Y_pct": null, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2021-03-08", "peak_price": 334000, "drawdown_after_peak_pct": -30.24, "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": null, "four_b_full_window_peak_proximity": null, "four_b_timing_verdict": "not_4B_row", "four_b_evidence_type": ["margin_or_backlog_slowdown"], "four_c_protection_label": "thesis_break_watch_only", "trigger_outcome_label": "false_positive_low_mfe_deep_mae", "current_profile_verdict": "current_profile_false_positive", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window; profile corporate_action_candidate_dates=[2023-02-13], outside window", "same_entry_group_id": "R13L26_C17_003_2021-02-23_326000", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false}
{"row_type": "trigger", "trigger_id": "R13L26_C17_004_T1_STAGE2_YELLOW", "case_id": "R13L26_C17_004", "symbol": "006650", "company_name": "대한유화", "round": "R13", "loop": "26", "large_sector_id": "L4_MATERIALS_SPREAD_RESOURCE", "canonical_archetype_id": "C17_CHEMICAL_COMMODITY_MARGIN_SPREAD", "fine_archetype_id": "SPREAD_SUPERCYCLE_VS_COMMODITY_PRICE_ONLY_CHEMICALS", "sector": "화학·석유화학", "primary_archetype": "ethylene_propylene_spread_spike", "loop_objective": "sector_specific_rule_discovery|canonical_archetype_compression|counterexample_mining|4B_non_price_requirement_stress_test|coverage_gap_fill", "trigger_type": "Stage2-Yellow", "trigger_date": "2021-02-10", "evidence_available_at_that_date": "Commodity-spread spike without durable order/customer/revision route; peak occurred quickly and drawdown dominated.", "evidence_source": "public earnings/disclosure/news/research-note class; price verified by Songdaiki/stock-web shard", "stage2_evidence_fields": ["public_event_or_disclosure", "relative_strength"], "stage3_evidence_fields": ["multiple_public_sources"], "stage4b_evidence_fields": ["valuation_blowoff", "price_only_local_peak"], "stage4c_evidence_fields": ["thesis_evidence_broken"], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/006/006650/2021.csv", "profile_path": "atlas/symbol_profiles/006/006650.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "entry_date": "2021-02-10", "entry_price": 373500, "MFE_30D_pct": 8.57, "MFE_90D_pct": 8.57, "MFE_180D_pct": 8.57, "MFE_1Y_pct": null, "MFE_2Y_pct": null, "MAE_30D_pct": -16.06, "MAE_90D_pct": -29.05, "MAE_180D_pct": -41.5, "MAE_1Y_pct": null, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2021-02-17", "peak_price": 405500, "drawdown_after_peak_pct": -46.12, "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": null, "four_b_full_window_peak_proximity": null, "four_b_timing_verdict": "not_4B_row", "four_b_evidence_type": ["valuation_blowoff", "price_only_local_peak"], "four_c_protection_label": "thesis_break_watch_only", "trigger_outcome_label": "false_positive_peak_before_durable_revision", "current_profile_verdict": "current_profile_false_positive", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window; profile corporate_action_candidate_dates=[2010-07-13], outside window", "same_entry_group_id": "R13L26_C17_004_2021-02-10_373500", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R13L26_C17_001", "trigger_id": "R13L26_C17_001_T1_STAGE2_ACTIONABLE", "symbol": "298020", "large_sector_id": "L4_MATERIALS_SPREAD_RESOURCE", "canonical_archetype_id": "C17_CHEMICAL_COMMODITY_MARGIN_SPREAD", "raw_component_scores_before": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 16, "revision_score": 12, "relative_strength_score": 14, "customer_quality_score": 12, "policy_or_regulatory_score": 0, "valuation_repricing_score": 10, "execution_risk_score": 6, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_before": 78, "stage_label_before": "Stage2-Actionable", "raw_component_scores_after": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 20, "revision_score": 14, "relative_strength_score": 14, "customer_quality_score": 14, "policy_or_regulatory_score": 0, "valuation_repricing_score": 12, "execution_risk_score": 4, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_after": 84, "stage_label_after": "Stage2-Actionable+sector_promote_candidate", "changed_components": ["margin_bridge_score", "customer_quality_score", "execution_risk_score"], "component_delta_explanation": "C17 shadow profile promotes durable spread-duration plus product/customer specificity, while blocking generic commodity-price or naphtha recovery narratives without revision breadth.", "MFE_90D_pct": 76.2, "MAE_90D_pct": -18.16, "score_return_alignment_label": "positive_alignment", "current_profile_verdict": "current_profile_missed_structural"}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R13L26_C17_001", "trigger_id": "R13L26_C17_001_T2_STAGE3_GREEN_LATE", "symbol": "298020", "large_sector_id": "L4_MATERIALS_SPREAD_RESOURCE", "canonical_archetype_id": "C17_CHEMICAL_COMMODITY_MARGIN_SPREAD", "raw_component_scores_before": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 24, "revision_score": 25, "relative_strength_score": 15, "customer_quality_score": 12, "policy_or_regulatory_score": 0, "valuation_repricing_score": 12, "execution_risk_score": 5, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_before": 90, "stage_label_before": "Stage3-Green", "raw_component_scores_after": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 24, "revision_score": 25, "relative_strength_score": 15, "customer_quality_score": 12, "policy_or_regulatory_score": 0, "valuation_repricing_score": 12, "execution_risk_score": 5, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_after": 90, "stage_label_after": "Stage3-Green", "changed_components": [], "component_delta_explanation": "C17 shadow profile promotes durable spread-duration plus product/customer specificity, while blocking generic commodity-price or naphtha recovery narratives without revision breadth.", "MFE_90D_pct": 37.57, "MAE_90D_pct": -5.29, "score_return_alignment_label": "late_but_valid_confirmation", "current_profile_verdict": "current_profile_too_late"}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R13L26_C17_001", "trigger_id": "R13L26_C17_001_T3_4B_VALUATION_OVERHEAT", "symbol": "298020", "large_sector_id": "L4_MATERIALS_SPREAD_RESOURCE", "canonical_archetype_id": "C17_CHEMICAL_COMMODITY_MARGIN_SPREAD", "raw_component_scores_before": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 22, "revision_score": 22, "relative_strength_score": 10, "customer_quality_score": 0, "policy_or_regulatory_score": 0, "valuation_repricing_score": 18, "execution_risk_score": 16, "legal_or_contract_risk_score": 2, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_before": 88, "stage_label_before": "Stage3-Green_with_watch", "raw_component_scores_after": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 18, "revision_score": 18, "relative_strength_score": 8, "customer_quality_score": 0, "policy_or_regulatory_score": 0, "valuation_repricing_score": 24, "execution_risk_score": 22, "legal_or_contract_risk_score": 2, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_after": 74, "stage_label_after": "4B-Overlay", "changed_components": ["valuation_repricing_score", "execution_risk_score", "margin_bridge_score"], "component_delta_explanation": "C17 shadow profile promotes durable spread-duration plus product/customer specificity, while blocking generic commodity-price or naphtha recovery narratives without revision breadth.", "MFE_90D_pct": 9.31, "MAE_90D_pct": -32.69, "score_return_alignment_label": "4B_risk_alignment", "current_profile_verdict": "current_profile_correct"}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R13L26_C17_002", "trigger_id": "R13L26_C17_002_T1_STAGE2_ACTIONABLE", "symbol": "011780", "large_sector_id": "L4_MATERIALS_SPREAD_RESOURCE", "canonical_archetype_id": "C17_CHEMICAL_COMMODITY_MARGIN_SPREAD", "raw_component_scores_before": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 16, "revision_score": 12, "relative_strength_score": 14, "customer_quality_score": 12, "policy_or_regulatory_score": 0, "valuation_repricing_score": 10, "execution_risk_score": 6, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_before": 78, "stage_label_before": "Stage2-Actionable", "raw_component_scores_after": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 20, "revision_score": 14, "relative_strength_score": 14, "customer_quality_score": 14, "policy_or_regulatory_score": 0, "valuation_repricing_score": 12, "execution_risk_score": 4, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_after": 84, "stage_label_after": "Stage2-Actionable+sector_promote_candidate", "changed_components": ["margin_bridge_score", "customer_quality_score", "execution_risk_score"], "component_delta_explanation": "C17 shadow profile promotes durable spread-duration plus product/customer specificity, while blocking generic commodity-price or naphtha recovery narratives without revision breadth.", "MFE_90D_pct": 60.48, "MAE_90D_pct": -2.15, "score_return_alignment_label": "positive_alignment", "current_profile_verdict": "current_profile_correct"}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R13L26_C17_002", "trigger_id": "R13L26_C17_002_T2_STAGE3_GREEN_LATE", "symbol": "011780", "large_sector_id": "L4_MATERIALS_SPREAD_RESOURCE", "canonical_archetype_id": "C17_CHEMICAL_COMMODITY_MARGIN_SPREAD", "raw_component_scores_before": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 24, "revision_score": 25, "relative_strength_score": 15, "customer_quality_score": 12, "policy_or_regulatory_score": 0, "valuation_repricing_score": 12, "execution_risk_score": 5, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_before": 90, "stage_label_before": "Stage3-Green", "raw_component_scores_after": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 24, "revision_score": 25, "relative_strength_score": 15, "customer_quality_score": 12, "policy_or_regulatory_score": 0, "valuation_repricing_score": 12, "execution_risk_score": 5, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_after": 90, "stage_label_after": "Stage3-Green", "changed_components": [], "component_delta_explanation": "C17 shadow profile promotes durable spread-duration plus product/customer specificity, while blocking generic commodity-price or naphtha recovery narratives without revision breadth.", "MFE_90D_pct": 7.96, "MAE_90D_pct": -27.67, "score_return_alignment_label": "late_but_valid_confirmation", "current_profile_verdict": "current_profile_too_late"}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R13L26_C17_003", "trigger_id": "R13L26_C17_003_T1_STAGE2_YELLOW", "symbol": "011170", "large_sector_id": "L4_MATERIALS_SPREAD_RESOURCE", "canonical_archetype_id": "C17_CHEMICAL_COMMODITY_MARGIN_SPREAD", "raw_component_scores_before": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 10, "revision_score": 8, "relative_strength_score": 12, "customer_quality_score": 3, "policy_or_regulatory_score": 0, "valuation_repricing_score": 10, "execution_risk_score": 12, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_before": 76, "stage_label_before": "Stage2-Yellow", "raw_component_scores_after": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 6, "revision_score": 6, "relative_strength_score": 10, "customer_quality_score": 2, "policy_or_regulatory_score": 0, "valuation_repricing_score": 7, "execution_risk_score": 18, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_after": 68, "stage_label_after": "Guarded-Watch", "changed_components": ["margin_bridge_score", "revision_score", "customer_quality_score", "execution_risk_score"], "component_delta_explanation": "C17 shadow profile promotes durable spread-duration plus product/customer specificity, while blocking generic commodity-price or naphtha recovery narratives without revision breadth.", "MFE_90D_pct": 2.45, "MAE_90D_pct": -15.64, "score_return_alignment_label": "false_positive_guard_needed", "current_profile_verdict": "current_profile_false_positive"}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R13L26_C17_004", "trigger_id": "R13L26_C17_004_T1_STAGE2_YELLOW", "symbol": "006650", "large_sector_id": "L4_MATERIALS_SPREAD_RESOURCE", "canonical_archetype_id": "C17_CHEMICAL_COMMODITY_MARGIN_SPREAD", "raw_component_scores_before": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 10, "revision_score": 8, "relative_strength_score": 12, "customer_quality_score": 3, "policy_or_regulatory_score": 0, "valuation_repricing_score": 10, "execution_risk_score": 12, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_before": 76, "stage_label_before": "Stage2-Yellow", "raw_component_scores_after": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 6, "revision_score": 6, "relative_strength_score": 10, "customer_quality_score": 2, "policy_or_regulatory_score": 0, "valuation_repricing_score": 7, "execution_risk_score": 18, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_after": 68, "stage_label_after": "Guarded-Watch", "changed_components": ["margin_bridge_score", "revision_score", "customer_quality_score", "execution_risk_score"], "component_delta_explanation": "C17 shadow profile promotes durable spread-duration plus product/customer specificity, while blocking generic commodity-price or naphtha recovery narratives without revision breadth.", "MFE_90D_pct": 8.57, "MAE_90D_pct": -29.05, "score_return_alignment_label": "false_positive_guard_needed", "current_profile_verdict": "current_profile_false_positive"}
{"row_type": "residual_contribution", "round": "R13", "loop": "26", "large_sector_id": "L4_MATERIALS_SPREAD_RESOURCE", "canonical_archetype_id": "C17_CHEMICAL_COMMODITY_MARGIN_SPREAD", "new_independent_case_count": 4, "reused_case_count": 0, "new_symbol_count": 4, "new_trigger_family_count": 4, "tested_existing_calibrated_axes": ["stage2_actionable_evidence_bonus", "stage3_green_revision_min", "price_only_blowoff_blocks_positive_stage", "full_4b_requires_non_price_evidence"], "residual_error_types_found": ["generic_commodity_price_false_positive", "green_after_spread_move_lateness", "spread_duration_missing_guard"], "loop_contribution_label": "canonical_archetype_rule_candidate", "do_not_propose_new_weight_delta": false}
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

next_round: `R4 or R13 holdout expansion`
recommended_next_large_sector_id: `L4_MATERIALS_SPREAD_RESOURCE`
recommended_next_canonical_archetype_id: `C15_MATERIAL_SPREAD_SUPERCYCLE` or `C16_STRATEGIC_RESOURCE_POLICY_SUPPLY`
reason: C17 now has a first balanced residual rule candidate; C15/C16 still need resource-policy and structural-spread holdout coverage.

## 28. Source Notes

- Stock-Web manifest path: `atlas/manifest.json`.
- Stock-Web profile paths used: `atlas/symbol_profiles/298/298020.json`, `atlas/symbol_profiles/011/011780.json`, `atlas/symbol_profiles/011/011170.json`, `atlas/symbol_profiles/006/006650.json`.
- Stock-Web price shard paths used: `atlas/ohlcv_tradable_by_symbol_year/298/298020/2021.csv`, `atlas/ohlcv_tradable_by_symbol_year/011/011780/2021.csv`, `atlas/ohlcv_tradable_by_symbol_year/011/011170/2021.csv`, `atlas/ohlcv_tradable_by_symbol_year/006/006650/2021.csv`.
- All OHLC values in this file use raw/unadjusted `tradable_raw` rows.
- This file is a research artifact only. It does not contain investment advice.
