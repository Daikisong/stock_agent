# E2R Stock-Web Historical Calibration / Sector-Archetype Residual Research Round

## 0. Research Metadata

```text
research_session = post_calibrated_sector_archetype_residual_research
mode = historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12
round = R7
loop = 27
large_sector_id = L7_BIO_HEALTHCARE_MEDICAL
canonical_archetype_id = C24_BIO_TRIAL_DATA_EVENT_RISK
fine_archetype_id = LUNG_CANCER_PIVOTAL_DATA_TO_APPROVAL_OPTIONALITY / CORE_PHASE3_FAILURE_4C / FAILED_DATA_WITH_RESCUE_FLOW_FALSE_BREAK
output_file = e2r_stock_web_v12_residual_round_R7_loop_27_L7_BIO_HEALTHCARE_MEDICAL_C24_BIO_TRIAL_DATA_EVENT_RISK_research.md
production_scoring_changed = false
shadow_weight_only = true
handoff_prompt_embedded = true
handoff_prompt_executed_now = false
```

This file is historical calibration research only. It is not a current candidate scan, not a live watchlist, not a trading recommendation, and not a repository patch.

## 1. Current Calibrated Profile Assumption

```text
current_default_profile_proxy = e2r_2_1_stock_web_calibrated_proxy
rollback_reference_profile_id = e2r_2_0_baseline_reference
stage2_actionable_evidence_bonus = +2.0
stage3_yellow_total_min = 75.0
stage3_green_total_min = 87.0
stage3_green_revision_min = 55.0
stage3_cross_evidence_green_buffer = +1.5
price_only_blowoff_blocks_positive_stage = true
full_4b_requires_non_price_evidence = true
hard_4c_thesis_break_routes_to_4c = true
```

The tested question is not whether early Stage2 is generally earlier than Green. That axis is already treated as applied. The new residual question is narrower: in `C24_BIO_TRIAL_DATA_EVENT_RISK`, does a pivotal clinical-data event need a different split between (1) efficacy data that opens an approval/commercialization route, (2) core phase-3 failure that breaks the asset thesis, and (3) failed data where financing/rescue-flow can create a temporary counter-rally even after the clinical thesis is impaired?

## 2. Round / Large Sector / Canonical Archetype Scope

| field | value |
|---|---|
| round | R7 |
| loop | 27 |
| large_sector_id | L7_BIO_HEALTHCARE_MEDICAL |
| canonical_archetype_id | C24_BIO_TRIAL_DATA_EVENT_RISK |
| loop_objective | coverage_gap_fill; counterexample_mining; 4C_thesis_break_timing_test; green_strictness_stress_test; canonical_archetype_compression |
| selection_mode | auto_coverage_gap_fill |
| auto_selected_coverage_gap | R7/C24 trial-data cases need positive and counterexample coverage separate from C23 approval/commercialization cases. |

## 3. Previous Coverage / Duplicate Avoidance Check

No `stock_agent/src/e2r` code was opened. Repository implementation files were not inspected. This loop deliberately avoids repeating the prior C23 approval/commercialization handoff. Two symbols overlap with broader bio research knowledge, but the trigger family is different: this loop uses trial-data events, not final approval or launch events.

Novelty handling:

| case_id | symbol | previous-overlap risk | novelty decision |
|---|---:|---|---|
| R7L27-C24-000100-MARIPOSA | 000100 | Yuhan may have appeared in C23 approval work | reused_symbol_possible, but new_trigger_family = pivotal phase-3 trial data; independent_evidence_weight = 0.5 |
| R7L27-C24-039200-MARIPOSA | 039200 | same drug ecosystem as Yuhan | new symbol for this loop, new equity sensitivity; independent_evidence_weight = 1.0 |
| R7L27-C24-215600-PHOCUS | 215600 | not reused in this loop | new hard 4C trial-futility case; independent_evidence_weight = 1.0 |
| R7L27-C24-084990-ENGENSIS | 084990 | not reused in this loop | new failed-data-with-rescue-flow counterexample; independent_evidence_weight = 1.0 |

## 4. Stock-Web OHLC Input / Price Source Validation

Stock-Web manifest was checked first.

```text
source = Songdaiki/stock-web
manifest_path = atlas/manifest.json
schema_path = atlas/schema.json
universe_path = atlas/universe/all_symbols.csv
source_name = FinanceData/marcap
source_repo_url = https://github.com/FinanceData/marcap
price_basis = tradable_raw
price_adjustment_status = raw_unadjusted_marcap
manifest_min_date = 1995-05-02
manifest_max_date = 2026-02-20
tradable_row_count = 14354401
raw_row_count = 15214118
symbol_count = 5414
active_like_symbol_count = 2868
inactive_or_delisted_like_symbol_count = 2546
markets = KONEX, KOSDAQ, KOSDAQ GLOBAL, KOSPI
calibration_shard_root = atlas/ohlcv_tradable_by_symbol_year
raw_shard_root = atlas/ohlcv_raw_by_symbol_year
```

The manifest explicitly states that OHLC is raw/unadjusted, zero-volume and zero-OHLC rows are excluded from calibration shards, and corporate-action-contaminated windows are blocked by default. Therefore all quantitative rows below use `tradable_raw` only.

## 5. Historical Eligibility Gate

| case_id | symbol | entry_date | 180D forward availability | corporate-action 180D overlap | calibration_usable | note |
|---|---:|---:|---|---|---|---|
| R7L27-C24-000100-MARIPOSA | 000100 | 2023-10-24 | yes | none in D+180 | true | 2020-04-08 corporate-action candidate is outside window. |
| R7L27-C24-039200-MARIPOSA | 039200 | 2023-10-24 | yes | none in D+180 | true | 2022-11-30 corporate-action candidate is outside window. |
| R7L27-C24-215600-PHOCUS | 215600 | 2019-08-02 | yes | none in D+180 | true | 2022-10-13 and 2024-07-09 corporate-action candidates are outside 2019/2020 window. |
| R7L27-C24-084990-ENGENSIS | 084990 | 2024-01-03 | yes | none in D+180 | true | 2019/2020/2021 corporate-action candidates are outside 2024 window. |

## 6. Canonical Archetype Compression Map

| fine_archetype_id | canonical_archetype_id | compression reason |
|---|---|---|
| LUNG_CANCER_PIVOTAL_DATA_TO_APPROVAL_OPTIONALITY | C24_BIO_TRIAL_DATA_EVENT_RISK | Pivotal PFS/OS/response data changes probability of regulatory and commercial path, but the trigger is trial data, not approval. |
| CORE_PHASE3_FAILURE_4C | C24_BIO_TRIAL_DATA_EVENT_RISK | Core asset failure or futility can immediately break the thesis. |
| FAILED_DATA_WITH_RESCUE_FLOW_FALSE_BREAK | C24_BIO_TRIAL_DATA_EVENT_RISK | Failed data may coexist with financing, acquisition, restructuring or speculative rescue flows; this is not the same as a clean hard-4C path. |

## 7. Case Selection Summary

| case_id | symbol | company_name | case_type | positive_or_counterexample | best_trigger | short thesis |
|---|---:|---|---|---|---|---|
| R7L27-C24-000100-MARIPOSA | 000100 | 유한양행 | structural_success | positive | trial_data_stage2_actionable | MARIPOSA-related lung-cancer data created durable approval/commercialization optionality. |
| R7L27-C24-039200-MARIPOSA | 039200 | 오스코텍 | high_mae_success | positive | trial_data_stage2_actionable | Same clinical data had higher equity beta and drawdown, but the data-to-optionality path remained valid. |
| R7L27-C24-215600-PHOCUS | 215600 | 신라젠 | 4C_success | counterexample | hard_4c_core_trial_futility | Core Pexa-Vec/PHOCUS thesis was broken by futility/termination-type event; price never recovered to entry in the window. |
| R7L27-C24-084990-ENGENSIS | 084990 | 헬릭스미스 | false_break | counterexample | failed_data_with_rescue_flow | Failed Engensis DPN data caused a thesis break, but post-failure rescue/speculative flow created a large counter-rally, showing hard-4C needs a rescue-flow guard. |

## 8. Positive vs Counterexample Balance

```text
positive_case_count = 2
counterexample_count = 2
4B_case_count = 1
4C_case_count = 2
calibration_usable_case_count = 4
new_independent_case_count = 4
reused_case_count = 0
```

This loop satisfies the minimum balance rule. It is not a positive-only bio rerating file. It contains two positive trial-data cases and two failed-data cases, including one clean hard-4C and one hard-4C false-break/rescue-flow stress case.

## 9. Evidence Source Map

| case_id | trigger_date | evidence_source | evidence_available_at_that_date | stage2_evidence_fields | stage3_evidence_fields | stage4b_evidence_fields | stage4c_evidence_fields |
|---|---:|---|---|---|---|---|---|
| R7L27-C24-000100-MARIPOSA | 2023-10-23 | MARIPOSA public trial data / later FDA evidence summary / medical press reporting | Public trial-data signal available by late Oct 2023; entry uses next-trading-day close due overseas conference/reporting timing uncertainty. | public_event_or_disclosure; customer_or_order_quality; policy_or_regulatory_optionality; early_revision_signal | multiple_public_sources; financial_visibility; durable_customer_confirmation | valuation_blowoff after 2024-08/10 run | [] |
| R7L27-C24-039200-MARIPOSA | 2023-10-23 | MARIPOSA public trial data and Korean partner sensitivity | Same trigger family as Yuhan but different equity beta and liquidity profile. | public_event_or_disclosure; relative_strength; policy_or_regulatory_optionality; early_revision_signal | multiple_public_sources; financial_visibility | valuation_blowoff; positioning_overheat | [] |
| R7L27-C24-215600-PHOCUS | 2019-08-02 | Pexa-Vec / PHOCUS phase-3 futility or termination-type public event | Treated as same-day market-actionable event because stock-web row shows immediate limit-down response. | [] | [] | [] | trial_failure; thesis_evidence_broken; forced_liquidation_or_crash |
| R7L27-C24-084990-ENGENSIS | 2024-01-03 | Engensis VM202-DPN phase-3 failure report | Same-day data-failure event; row shows immediate repricing. | [] | [] | positioning_overheat; rescue_flow_after_failure | trial_failure; thesis_evidence_broken |

Source-note caveat: the scoring rows intentionally use trial-data events as evidence families. Later approval events are not used to back-date the trigger labels. The positive cases are trial-data-to-optionality cases; the negative cases are data-failure or futility cases.

## 10. Price Data Source Map

| symbol | company_name | profile_path | price shard(s) used | profile status | corporate_action_window_status |
|---:|---|---|---|---|---|
| 000100 | 유한양행 | atlas/symbol_profiles/000/000100.json | atlas/ohlcv_tradable_by_symbol_year/000/000100/2023.csv; 2024.csv; 2025.csv | active_like | clean_180D_window |
| 039200 | 오스코텍 | atlas/symbol_profiles/039/039200.json | atlas/ohlcv_tradable_by_symbol_year/039/039200/2023.csv; 2024.csv | active_like | clean_180D_window |
| 215600 | 신라젠 | atlas/symbol_profiles/215/215600.json | atlas/ohlcv_tradable_by_symbol_year/215/215600/2019.csv; 2020.csv | active_like, but trading suspension history visible as missing 2021 tradable shard | clean_180D_window |
| 084990 | 헬릭스미스 | atlas/symbol_profiles/084/084990.json | atlas/ohlcv_tradable_by_symbol_year/084/084990/2024.csv | active_like | clean_180D_window |

## 11. Case-by-Case Trigger Grid

| trigger_id | case_id | trigger_type | trigger_date | entry_date | entry_price | trigger_outcome_label | current_profile_verdict | aggregate role |
|---|---|---|---:|---:|---:|---|---|---|
| R7L27-T001 | R7L27-C24-000100-MARIPOSA | Stage2-Actionable | 2023-10-23 | 2023-10-24 | 58000 | structural_success | current_profile_too_late | representative |
| R7L27-T002 | R7L27-C24-000100-MARIPOSA | Stage3-Green-comparison | 2024-08-26 | 2024-08-26 | 111600 | late_green_comparison | current_profile_too_late | label_comparison_only |
| R7L27-T003 | R7L27-C24-039200-MARIPOSA | Stage2-Actionable | 2023-10-23 | 2023-10-24 | 19670 | high_mae_success | current_profile_too_late | representative |
| R7L27-T004 | R7L27-C24-039200-MARIPOSA | Stage4B-overlay | 2024-10-15 | 2024-10-15 | 42250 | 4B_overlay_success | current_profile_correct | 4B_overlay_only |
| R7L27-T005 | R7L27-C24-215600-PHOCUS | 4C | 2019-08-02 | 2019-08-02 | 31200 | hard_4c_success | current_profile_correct | representative |
| R7L27-T006 | R7L27-C24-084990-ENGENSIS | 4C-watch | 2024-01-03 | 2024-01-03 | 4250 | failed_data_false_break | current_profile_4C_too_early | representative |
| R7L27-T007 | R7L27-C24-084990-ENGENSIS | Stage4B-overlay | 2024-02-06 | 2024-02-06 | 5850 | rescue_flow_4B_overlay | current_profile_correct | 4B_overlay_only |

## 12. Trigger-Level OHLC Backtest Tables

Representative rows below use actual stock-web `c`, `h`, and `l` values from tradable shards. Values are rounded to two decimals. For same-entry label-comparison rows, aggregate inclusion is false.

| trigger_id | symbol | entry_date | entry_price | MFE_30D_pct | MAE_30D_pct | MFE_90D_pct | MAE_90D_pct | MFE_180D_pct | MAE_180D_pct | MFE_1Y_pct | MAE_1Y_pct | peak_date | peak_price | drawdown_after_peak_pct |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| R7L27-T001 | 000100 | 2023-10-24 | 58000 | 10.69 | -5.34 | 23.45 | -5.34 | 73.10 | -5.34 | 187.76 | -5.34 | 2024-10-15 | 166900 | -39.19 |
| R7L27-T003 | 039200 | 2023-10-24 | 19670 | 9.81 | -8.49 | 52.52 | -8.49 | 128.27 | -8.49 | 128.27 | -8.49 | 2024-07-16 | 44900 | -51.67 |
| R7L27-T005 | 215600 | 2019-08-02 | 31200 | 0.00 | -71.15 | 0.00 | -74.94 | 0.00 | -74.94 | 0.00 | -74.94 | 2019-08-02 | 31200 | -74.94 |
| R7L27-T006 | 084990 | 2024-01-03 | 4250 | 75.06 | -23.06 | 75.06 | -23.53 | 75.06 | -23.53 | 75.06 | -23.53 | 2024-02-06 | 7440 | -56.05 |

Interpretation:

* `000100` and `039200` show that C24 can produce valid Stage2-Actionable signals before clean Green confirmation, but the equity path is volatile enough that Green should not be relaxed globally.
* `215600` is a clean hard-4C: core phase-3 failure/futility cut the thesis and there was no positive MFE after the entry close in the forward windows.
* `084990` is the residual counterexample: the clinical-data thesis failed, but a large rescue/speculative rally followed. Hard 4C should remain thesis-break routing, but C24 needs a `failed_data_with_rescue_flow_watch` guard before assuming immediate irreversible price protection.

## 13. Current Calibrated Profile Stress Test

| case_id | P0 expected action | actual path | verdict | axis implication |
|---|---|---|---|---|
| R7L27-C24-000100-MARIPOSA | Likely Yellow/Green delayed until regulatory/commercial confirmation because revision visibility was incomplete. | 180D MFE +73.10%; full-cycle peak far above Stage2 entry. | current_profile_too_late | C24 pivotal data with high-quality partner and endpoint strength can deserve Stage2-Actionable even before full revision score. |
| R7L27-C24-039200-MARIPOSA | Similar delay; higher small/mid-cap volatility may keep Green strict. | 180D MFE +128.27%, but MAE and later drawdown are large. | current_profile_too_late but high_mae_success | Do not lower global Green; add C24 Stage2 optionality bonus with MAE warning. |
| R7L27-C24-215600-PHOCUS | Hard 4C on core trial futility/failure. | No positive MFE; deep MAE. | current_profile_correct | Existing hard_4c_thesis_break route is strengthened for core asset failure. |
| R7L27-C24-084990-ENGENSIS | Hard 4C would likely fire on phase-3 failure. | 30D/90D MFE +75.06% before fading; failure did not immediately protect from a squeeze/restructuring rally. | current_profile_4C_too_early | Add C24 counterexample guard: failed-data 4C needs rescue-flow / financing / corporate-action watch label when rebound risk is visible. |

Axis answers:

```text
stage2_actionable_evidence_bonus: adequate globally, but C24 pivotal-data-to-approval-optionality needs +1 shadow support.
yellow_threshold_75: kept.
green_threshold_87/revision_55: kept globally; weakened only as C24-specific exception for pivotal endpoint data with strong partner/regulatory path.
price_only_blowoff_guard: strengthened.
full_4b_non_price_requirement: strengthened.
hard_4c_routing: strengthened for core failure; weakened only for failed-data-with-rescue-flow false-break path.
```

## 14. Stage2 / Yellow / Green Comparison

| case_id | Stage2_Actionable_entry | Stage3_Green_proxy_entry | peak_after_stage2 | green_lateness_ratio | interpretation |
|---|---:|---:|---:|---:|---|
| R7L27-C24-000100-MARIPOSA | 58000 | 111600 | 166900 | 0.49 | Green is not useless, but it captures the middle of the move rather than the early data inflection. |
| R7L27-C24-039200-MARIPOSA | 19670 | 37300 | 44900 | 0.70 | Green after a clean financial/consensus bridge would be late for this high-beta partner equity. |
| R7L27-C24-215600-PHOCUS | not_applicable | not_applicable | 31200 | not_applicable | Negative trial-data case; no Green audit. |
| R7L27-C24-084990-ENGENSIS | not_applicable | not_applicable | 7440 | not_applicable | Failed-data with rescue-flow case; this belongs to 4C/4B audit, not Green promotion. |

## 15. 4B Local vs Full-window Timing Audit

| trigger_id | case_id | 4B evidence type | local peak reference | full-window peak reference | four_b_local_peak_proximity | four_b_full_window_peak_proximity | verdict |
|---|---|---|---:|---:|---:|---:|---|
| R7L27-T004 | R7L27-C24-039200-MARIPOSA | valuation_blowoff; positioning_overheat | 44900 | 44900 | 0.91 | 0.91 | good_full_window_4B_timing; 2024-10 rally occurred after large data-driven rerating and preceded >50% drawdown from peak zone. |
| R7L27-T007 | R7L27-C24-084990-ENGENSIS | rescue_flow_after_failure; price_only | 7440 | 7440 | 0.73 | 0.73 | 4B overlay, not positive promotion; failed data cannot become Stage2/3 solely because price rebounded. |

## 16. 4C Protection Audit

| case_id | 4C event | MAE_90D_after_4C | max_drawdown_after_prior_peak | four_c_protection_label | explanation |
|---|---|---:|---:|---|---|
| R7L27-C24-215600-PHOCUS | Core pivotal trial futility/failure | -74.94 | -74.94 | hard_4c_success | Thesis and price both broke; no positive-stage rescue label is justified. |
| R7L27-C24-084990-ENGENSIS | Engensis DPN phase-3 failure | -23.53 | -56.05 after rescue peak | thesis_break_watch_only | Thesis break is real, but immediate hard-4C as a price-protection signal was too early because a squeeze/rescue rally followed. |

## 17. Sector-Specific Rule Candidate

```text
sector_specific_rule_candidate = false
reason = all cases are within L7 only and specifically map to C24; no cross-sector generalization is proposed.
```

## 18. Canonical-Archetype Rule Candidate

```text
canonical_archetype_rule_candidate = true
scope = C24_BIO_TRIAL_DATA_EVENT_RISK
```

Proposed C24 shadow-only rules:

1. `c24_pivotal_data_to_optionality_stage2_bonus = +1.0`
   * Eligible only when trial data is pivotal or near-pivotal, endpoint quality is material, partner/regulatory route is credible, and the event is not merely abstract mechanism news.
   * Evidence fields: `public_event_or_disclosure`, `policy_or_regulatory_optionality`, `customer_or_order_quality`, `early_revision_signal`.
   * Effect: catches Yuhan/Oskotec-type trial-data inflection earlier without lowering global Green.

2. `c24_core_phase3_failure_hard_4c = strengthen_existing_axis`
   * Eligible when the asset is central to valuation and the data event is futility, trial failure, regulatory-data insufficiency, or endpoint failure.
   * Evidence fields: `trial_failure`, `thesis_evidence_broken`, `forced_liquidation_or_crash`.
   * Effect: reinforces SillaJen-type hard 4C.

3. `c24_failed_data_rescue_flow_guard = +1 risk overlay, not positive-stage promotion`
   * If data fails but rescue-flow, financing optionality, acquisition/restructuring speculation, or squeezed float dominates the next window, label as `thesis_break_watch_only` or `failed_data_with_rescue_flow`, not as clean hard-4C price protection.
   * Effect: prevents Helixmith-type false confidence where clinical 4C is correct but immediate price-protection timing is too early.

## 19. Before / After Backtest Comparison

| profile_id | profile_scope | changed_axes | eligible_trigger_count | selected_entry_trigger_per_case | avg_MFE_90D_pct | avg_MAE_90D_pct | avg_MFE_180D_pct | avg_MAE_180D_pct | false_positive_rate | missed_structural_count | late_green_count | avg_green_lateness_ratio | score_return_alignment_verdict |
|---|---|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| P0_e2r_2_1_stock_web_calibrated_proxy | global current | none | 4 | strict Green/4C | 43.01 | -28.08 | 69.11 | -29.06 | 0.25 | 2 | 2 | 0.60 | partially aligned; too late on trial-data positives; too early as price-protection on rescue-flow failure. |
| P0b_e2r_2_0_baseline_reference | rollback reference | looser Green, weaker 4C | 4 | mixed | 43.01 | -28.08 | 69.11 | -29.06 | 0.50 | 1 | 1 | 0.45 | worse; more likely to misread failed-data rebounds as positive. |
| P1_sector_specific_candidate_profile | L7 | no sector-wide rule | 4 | no sector promotion | 43.01 | -28.08 | 69.11 | -29.06 | 0.25 | 2 | 2 | 0.60 | not selected; sector is too broad. |
| P2_c24_archetype_candidate_profile | C24 | +1 pivotal-data Stage2; strengthen core 4C; rescue-flow guard | 4 | event-family-aware | 43.01 | -28.08 | 69.11 | -29.06 | 0.00 | 0 | 1 | 0.60 | best alignment; keeps global Green strict while catching pivotal-data option value. |
| P3_counterexample_guard_profile | C24 risk overlay | rescue-flow guard only | 2 failed-data rows | 4C/watch split | 37.53 | -49.24 | 37.53 | -49.24 | 0.00 | 0 | n/a | n/a | good for failed-data risk, incomplete for positives. |

## 20. Score-Return Alignment Matrix

### Raw component proxy scores

| case_id | contract | backlog_visibility | margin_bridge | revision | relative_strength | customer_quality | policy_regulatory | valuation_repricing | execution_risk | legal_contract_risk | dilution_cb_risk | accounting_trust_risk | supplemental |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|
| R7L27-C24-000100-MARIPOSA | 35 | 20 | 25 | 45 | 40 | 70 | 80 | 55 | 25 | 10 | 0 | 0 | trial_endpoint_quality_score=85; commercialization_optionality_score=75 |
| R7L27-C24-039200-MARIPOSA | 20 | 15 | 15 | 35 | 60 | 65 | 75 | 70 | 40 | 10 | 0 | 0 | trial_endpoint_quality_score=85; partner_beta_score=80 |
| R7L27-C24-215600-PHOCUS | 0 | 0 | 0 | 0 | 0 | 20 | 0 | 0 | 95 | 35 | 20 | 20 | thesis_break_score=100; forced_liquidation_score=90 |
| R7L27-C24-084990-ENGENSIS | 0 | 0 | 0 | 0 | 20 | 15 | 0 | 30 | 90 | 20 | 40 | 15 | thesis_break_score=85; rescue_flow_score=80 |

### Score simulation rows

| trigger_id | profile_before | weighted_score_before | stage_label_before | profile_after | weighted_score_after | stage_label_after | component_delta_explanation | score_return_alignment_label |
|---|---|---:|---|---|---:|---|---|---|
| R7L27-T001 | P0 | 73 | Stage2-Watch / below Yellow | P2 | 77 | Stage2-Actionable / C24 Yellow-Watch | pivotal data quality and regulatory optionality add C24 bonus without full revision relaxation | aligned_positive |
| R7L27-T003 | P0 | 72 | Stage2-Watch | P2 | 76 | Stage2-Actionable / high-MAE C24 | same data, smaller equity, higher beta; add C24 optionality but retain volatility warning | aligned_high_mae_positive |
| R7L27-T005 | P0 | 18 | 4C | P2 | 10 | hard_4C | core trial failure increases thesis_break penalty | aligned_4C |
| R7L27-T006 | P0 | 16 | hard_4C | P3 | 20 | thesis_break_watch_only + rescue_flow_guard | clinical thesis broken, but rescue-flow flag blocks overconfident immediate price-protection label | aligned_counterexample_guard |

## 21. Coverage Matrix

| large_sector_id | canonical_archetype_id | fine_archetype_id | positive_case_count | counterexample_count | 4B_case_count | 4C_case_count | new_independent_case_count | reused_case_count | calibration_usable_trigger_count | representative_trigger_count | current_profile_error_count | sector_rule_candidate | canonical_rule_candidate | coverage_gap_after_this_loop |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|---|---|
| L7_BIO_HEALTHCARE_MEDICAL | C24_BIO_TRIAL_DATA_EVENT_RISK | mixed | 2 | 2 | 2 | 2 | 4 | 0 | 7 | 4 | 3 | false | true | C24 now has positive pivotal data, core trial failure, and failed-data rescue-flow counterexample coverage. Needs later expansion to non-oncology and medical-device trial data. |

## 22. Residual Contribution Summary

```text
new_independent_case_count: 4
reused_case_count: 0
reused_case_ids: []
new_symbol_count: 4
same_archetype_new_symbol_count: 4
same_archetype_new_trigger_family_count: 3
new_canonical_archetype_count: 0
new_fine_archetype_count: 3
new_trigger_family_count: 3
positive_case_count: 2
counterexample_count: 2
current_profile_error_count: 3
calibration_usable_case_count: 4
calibration_usable_trigger_count: 7
tested_existing_calibrated_axes: [stage3_green_revision_min, price_only_blowoff_blocks_positive_stage, full_4b_requires_non_price_evidence, hard_4c_thesis_break_routes_to_4c]
residual_error_types_found: [current_profile_too_late_on_pivotal_trial_data, current_profile_4C_too_early_when_failed_data_has_rescue_flow]
new_axis_proposed: [c24_pivotal_data_to_optionality_stage2_bonus, c24_failed_data_rescue_flow_guard]
existing_axis_strengthened: [hard_4c_thesis_break_routes_to_4c, price_only_blowoff_blocks_positive_stage, full_4b_requires_non_price_evidence]
existing_axis_weakened: [stage3_green_revision_min only as C24-specific exception, not global]
existing_axis_kept: [stage3_yellow_total_min, stage3_green_total_min]
sector_specific_rule_candidate: false
canonical_archetype_rule_candidate: true
no_new_signal_reason: null
loop_contribution_label: residual_error_found; canonical_archetype_rule_candidate
do_not_propose_new_weight_delta: false
auto_selected_coverage_gap: R7/C24 trial-data event risk lacked balanced positive/counterexample coverage.
diversity_score_summary: high: 4 symbols, 3 trigger families, 2 positives, 2 counterexamples, and one rescue-flow false-break residual.
```

## 23. Validation Scope / Non-Validation Scope

Validated:

* Stock-Web manifest and symbol profiles were checked.
* Tradable OHLC rows were used for entry prices and forward MFE/MAE.
* 180D windows were checked against manifest/profile max date.
* Corporate-action candidate dates were checked for 180D overlap.
* Same-entry representative rows were deduplicated for aggregate use.

Not validated:

* No live candidate scan was run.
* No broker or trading API was used.
* No `stock_agent/src/e2r` production code was opened.
* The proposed scores are research proxy scores, not production scores.
* Some primary evidence-source URLs should be re-expanded during repository ingestion; the calibration value here rests on historical event classification plus stock-web OHLC rows.

## 24. Shadow Weight Calibration

```csv
row_type,axis,scope,large_sector_id,canonical_archetype_id,baseline_value,tested_value,delta,reason,backtest_effect,trigger_ids,calibration_usable_count,new_independent_case_count,counterexample_count,confidence,proposal_type,notes
shadow_weight,c24_pivotal_data_to_optionality_stage2_bonus,canonical_archetype_specific,L7_BIO_HEALTHCARE_MEDICAL,C24_BIO_TRIAL_DATA_EVENT_RISK,0,+1,+1,"pivotal data with clear regulatory/commercial optionality captured positive cases earlier without relaxing global Green","reduced missed_structural_count from 2 to 0 on positive rows",R7L27-T001|R7L27-T003,2,2,0,medium,canonical_shadow_only,"not production; requires batch ledger aggregation"
shadow_weight,c24_core_phase3_failure_hard_4c,canonical_archetype_specific,L7_BIO_HEALTHCARE_MEDICAL,C24_BIO_TRIAL_DATA_EVENT_RISK,existing,strengthen,0,"core pivotal failure/futility had clean negative path in SillaJen","strengthens hard_4c_thesis_break axis for core asset failure",R7L27-T005,1,1,1,medium,canonical_shadow_only,"strengthening existing axis, not a new global rule"
shadow_weight,c24_failed_data_rescue_flow_guard,canonical_archetype_specific,L7_BIO_HEALTHCARE_MEDICAL,C24_BIO_TRIAL_DATA_EVENT_RISK,0,+1,+1,"failed data can rally on rescue/speculative flow; do not treat every data failure as immediate clean price-protection 4C","reduced current_profile_4C_too_early error",R7L27-T006|R7L27-T007,1,1,1,low,canonical_shadow_only,"guard label, not positive promotion"
```

## 25. Machine-Readable Rows

```jsonl
{"row_type":"price_source_validation","source":"Songdaiki/stock-web","source_url":"https://github.com/Songdaiki/stock-web","manifest_path":"atlas/manifest.json","schema_path":"atlas/schema.json","universe_path":"atlas/universe/all_symbols.csv","manifest_max_date":"2026-02-20","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","calibration_shard_root":"atlas/ohlcv_tradable_by_symbol_year","raw_shard_root":"atlas/ohlcv_raw_by_symbol_year","validation_status":"usable_for_historical_calibration"}
{"row_type":"case","case_id":"R7L27-C24-000100-MARIPOSA","symbol":"000100","company_name":"유한양행","round":"R7","loop":"27","large_sector_id":"L7_BIO_HEALTHCARE_MEDICAL","canonical_archetype_id":"C24_BIO_TRIAL_DATA_EVENT_RISK","fine_archetype_id":"LUNG_CANCER_PIVOTAL_DATA_TO_APPROVAL_OPTIONALITY","case_type":"structural_success","positive_or_counterexample":"positive","best_trigger":"R7L27-T001","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":"possible_prior_symbol_but_new_trigger_family_trial_data_not_approval","independent_evidence_weight":0.5,"score_price_alignment":"aligned_positive","current_profile_verdict":"current_profile_too_late","price_source":"Songdaiki/stock-web","notes":"pivotal trial-data optionality case; do not reclassify as C23 approval trigger"}
{"row_type":"case","case_id":"R7L27-C24-039200-MARIPOSA","symbol":"039200","company_name":"오스코텍","round":"R7","loop":"27","large_sector_id":"L7_BIO_HEALTHCARE_MEDICAL","canonical_archetype_id":"C24_BIO_TRIAL_DATA_EVENT_RISK","fine_archetype_id":"LUNG_CANCER_PIVOTAL_DATA_TO_APPROVAL_OPTIONALITY","case_type":"high_mae_success","positive_or_counterexample":"positive","best_trigger":"R7L27-T003","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"aligned_high_mae_positive","current_profile_verdict":"current_profile_too_late","price_source":"Songdaiki/stock-web","notes":"same data family, higher beta partner equity"}
{"row_type":"case","case_id":"R7L27-C24-215600-PHOCUS","symbol":"215600","company_name":"신라젠","round":"R7","loop":"27","large_sector_id":"L7_BIO_HEALTHCARE_MEDICAL","canonical_archetype_id":"C24_BIO_TRIAL_DATA_EVENT_RISK","fine_archetype_id":"CORE_PHASE3_FAILURE_4C","case_type":"4C_success","positive_or_counterexample":"counterexample","best_trigger":"R7L27-T005","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"aligned_4C","current_profile_verdict":"current_profile_correct","price_source":"Songdaiki/stock-web","notes":"clean core trial-futility hard 4C"}
{"row_type":"case","case_id":"R7L27-C24-084990-ENGENSIS","symbol":"084990","company_name":"헬릭스미스","round":"R7","loop":"27","large_sector_id":"L7_BIO_HEALTHCARE_MEDICAL","canonical_archetype_id":"C24_BIO_TRIAL_DATA_EVENT_RISK","fine_archetype_id":"FAILED_DATA_WITH_RESCUE_FLOW_FALSE_BREAK","case_type":"false_break","positive_or_counterexample":"counterexample","best_trigger":"R7L27-T006","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"counterexample_guard_needed","current_profile_verdict":"current_profile_4C_too_early","price_source":"Songdaiki/stock-web","notes":"failed data but rescue-flow rally; 4C price-protection timing should be guarded"}
{"row_type":"trigger","trigger_id":"R7L27-T001","case_id":"R7L27-C24-000100-MARIPOSA","symbol":"000100","company_name":"유한양행","round":"R7","loop":"27","large_sector_id":"L7_BIO_HEALTHCARE_MEDICAL","canonical_archetype_id":"C24_BIO_TRIAL_DATA_EVENT_RISK","fine_archetype_id":"LUNG_CANCER_PIVOTAL_DATA_TO_APPROVAL_OPTIONALITY","sector":"bio_healthcare_medical","primary_archetype":"pivotal_trial_data_to_regulatory_optionality","loop_objective":"coverage_gap_fill|green_strictness_stress_test","trigger_type":"Stage2-Actionable","trigger_date":"2023-10-23","evidence_available_at_that_date":"MARIPOSA pivotal trial data public by late Oct 2023; next-trading-day entry used for timing conservatism","evidence_source":"public clinical data / later FDA evidence summary / medical press","stage2_evidence_fields":["public_event_or_disclosure","policy_or_regulatory_optionality","customer_or_order_quality","early_revision_signal"],"stage3_evidence_fields":["multiple_public_sources","financial_visibility","durable_customer_confirmation"],"stage4b_evidence_fields":["valuation_blowoff"],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/000/000100/2023.csv","profile_path":"atlas/symbol_profiles/000/000100.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","entry_date":"2023-10-24","entry_price":58000,"MFE_30D_pct":10.69,"MFE_90D_pct":23.45,"MFE_180D_pct":73.10,"MFE_1Y_pct":187.76,"MFE_2Y_pct":187.76,"MAE_30D_pct":-5.34,"MAE_90D_pct":-5.34,"MAE_180D_pct":-5.34,"MAE_1Y_pct":-5.34,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-10-15","peak_price":166900,"drawdown_after_peak_pct":-39.19,"green_lateness_ratio":0.49,"four_b_local_peak_proximity":null,"four_b_full_window_peak_proximity":null,"four_b_timing_verdict":null,"four_b_evidence_type":[],"four_c_protection_label":null,"trigger_outcome_label":"structural_success","current_profile_verdict":"current_profile_too_late","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"R7L27-C24-000100-2023-10-24-58000","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":"possible_prior_symbol_but_new_trigger_family_trial_data_not_approval","independent_evidence_weight":0.5,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"R7L27-T003","case_id":"R7L27-C24-039200-MARIPOSA","symbol":"039200","company_name":"오스코텍","round":"R7","loop":"27","large_sector_id":"L7_BIO_HEALTHCARE_MEDICAL","canonical_archetype_id":"C24_BIO_TRIAL_DATA_EVENT_RISK","fine_archetype_id":"LUNG_CANCER_PIVOTAL_DATA_TO_APPROVAL_OPTIONALITY","sector":"bio_healthcare_medical","primary_archetype":"pivotal_trial_data_to_regulatory_optionality_partner_beta","loop_objective":"coverage_gap_fill|green_strictness_stress_test","trigger_type":"Stage2-Actionable","trigger_date":"2023-10-23","evidence_available_at_that_date":"same pivotal clinical-data family; next-trading-day entry used","evidence_source":"public clinical data / partner sensitivity","stage2_evidence_fields":["public_event_or_disclosure","relative_strength","policy_or_regulatory_optionality","early_revision_signal"],"stage3_evidence_fields":["multiple_public_sources","financial_visibility"],"stage4b_evidence_fields":["valuation_blowoff","positioning_overheat"],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/039/039200/2023.csv","profile_path":"atlas/symbol_profiles/039/039200.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","entry_date":"2023-10-24","entry_price":19670,"MFE_30D_pct":9.81,"MFE_90D_pct":52.52,"MFE_180D_pct":128.27,"MFE_1Y_pct":128.27,"MFE_2Y_pct":128.27,"MAE_30D_pct":-8.49,"MAE_90D_pct":-8.49,"MAE_180D_pct":-8.49,"MAE_1Y_pct":-8.49,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-07-16","peak_price":44900,"drawdown_after_peak_pct":-51.67,"green_lateness_ratio":0.70,"four_b_local_peak_proximity":null,"four_b_full_window_peak_proximity":null,"four_b_timing_verdict":null,"four_b_evidence_type":[],"four_c_protection_label":null,"trigger_outcome_label":"high_mae_success","current_profile_verdict":"current_profile_too_late","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"R7L27-C24-039200-2023-10-24-19670","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"R7L27-T005","case_id":"R7L27-C24-215600-PHOCUS","symbol":"215600","company_name":"신라젠","round":"R7","loop":"27","large_sector_id":"L7_BIO_HEALTHCARE_MEDICAL","canonical_archetype_id":"C24_BIO_TRIAL_DATA_EVENT_RISK","fine_archetype_id":"CORE_PHASE3_FAILURE_4C","sector":"bio_healthcare_medical","primary_archetype":"core_phase3_failure_hard_4c","loop_objective":"counterexample_mining|4C_thesis_break_timing_test","trigger_type":"4C","trigger_date":"2019-08-02","evidence_available_at_that_date":"core phase-3 futility/failure event market-actionable same day","evidence_source":"public trial-futility/termination event classification; stock-web immediate repricing row","stage2_evidence_fields":[],"stage3_evidence_fields":[],"stage4b_evidence_fields":[],"stage4c_evidence_fields":["trial_failure","thesis_evidence_broken","forced_liquidation_or_crash"],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/215/215600/2019.csv","profile_path":"atlas/symbol_profiles/215/215600.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","entry_date":"2019-08-02","entry_price":31200,"MFE_30D_pct":0.00,"MFE_90D_pct":0.00,"MFE_180D_pct":0.00,"MFE_1Y_pct":0.00,"MFE_2Y_pct":0.00,"MAE_30D_pct":-71.15,"MAE_90D_pct":-74.94,"MAE_180D_pct":-74.94,"MAE_1Y_pct":-74.94,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2019-08-02","peak_price":31200,"drawdown_after_peak_pct":-74.94,"green_lateness_ratio":null,"four_b_local_peak_proximity":null,"four_b_full_window_peak_proximity":null,"four_b_timing_verdict":null,"four_b_evidence_type":[],"four_c_protection_label":"hard_4c_success","trigger_outcome_label":"hard_4c_success","current_profile_verdict":"current_profile_correct","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"R7L27-C24-215600-2019-08-02-31200","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"R7L27-T006","case_id":"R7L27-C24-084990-ENGENSIS","symbol":"084990","company_name":"헬릭스미스","round":"R7","loop":"27","large_sector_id":"L7_BIO_HEALTHCARE_MEDICAL","canonical_archetype_id":"C24_BIO_TRIAL_DATA_EVENT_RISK","fine_archetype_id":"FAILED_DATA_WITH_RESCUE_FLOW_FALSE_BREAK","sector":"bio_healthcare_medical","primary_archetype":"failed_data_with_rescue_flow_false_break","loop_objective":"counterexample_mining|4C_thesis_break_timing_test","trigger_type":"4C-watch","trigger_date":"2024-01-03","evidence_available_at_that_date":"Engensis DPN phase-3 failure reported; same-day entry uses close after repricing","evidence_source":"public failed trial-data report; stock-web immediate repricing row","stage2_evidence_fields":[],"stage3_evidence_fields":[],"stage4b_evidence_fields":["positioning_overheat","price_only_local_peak"],"stage4c_evidence_fields":["trial_failure","thesis_evidence_broken"],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/084/084990/2024.csv","profile_path":"atlas/symbol_profiles/084/084990.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","entry_date":"2024-01-03","entry_price":4250,"MFE_30D_pct":75.06,"MFE_90D_pct":75.06,"MFE_180D_pct":75.06,"MFE_1Y_pct":75.06,"MFE_2Y_pct":75.06,"MAE_30D_pct":-23.06,"MAE_90D_pct":-23.53,"MAE_180D_pct":-23.53,"MAE_1Y_pct":-23.53,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-02-06","peak_price":7440,"drawdown_after_peak_pct":-56.05,"green_lateness_ratio":null,"four_b_local_peak_proximity":0.73,"four_b_full_window_peak_proximity":0.73,"four_b_timing_verdict":"rescue_flow_4B_overlay_not_positive_promotion","four_b_evidence_type":["price_only","positioning_overheat"],"four_c_protection_label":"thesis_break_watch_only","trigger_outcome_label":"failed_data_false_break","current_profile_verdict":"current_profile_4C_too_early","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"R7L27-C24-084990-2024-01-03-4250","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"R7L27-C24-000100-MARIPOSA","trigger_id":"R7L27-T001","symbol":"000100","large_sector_id":"L7_BIO_HEALTHCARE_MEDICAL","canonical_archetype_id":"C24_BIO_TRIAL_DATA_EVENT_RISK","raw_component_scores_before":{"contract_score":35,"backlog_visibility_score":20,"margin_bridge_score":25,"revision_score":45,"relative_strength_score":40,"customer_quality_score":70,"policy_or_regulatory_score":80,"valuation_repricing_score":55,"execution_risk_score":25,"legal_or_contract_risk_score":10,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0,"trial_endpoint_quality_score":85,"commercialization_optionality_score":75},"weighted_score_before":73,"stage_label_before":"Stage2-Watch","raw_component_scores_after":{"contract_score":35,"backlog_visibility_score":20,"margin_bridge_score":25,"revision_score":45,"relative_strength_score":40,"customer_quality_score":70,"policy_or_regulatory_score":80,"valuation_repricing_score":55,"execution_risk_score":25,"legal_or_contract_risk_score":10,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0,"trial_endpoint_quality_score":85,"commercialization_optionality_score":75},"weighted_score_after":77,"stage_label_after":"Stage2-Actionable_C24_YellowWatch","changed_components":["c24_pivotal_data_to_optionality_stage2_bonus"],"component_delta_explanation":"pivotal endpoint quality and credible regulatory path support earlier Stage2 without full Green relaxation","MFE_90D_pct":23.45,"MAE_90D_pct":-5.34,"score_return_alignment_label":"aligned_positive","current_profile_verdict":"current_profile_too_late"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"R7L27-C24-039200-MARIPOSA","trigger_id":"R7L27-T003","symbol":"039200","large_sector_id":"L7_BIO_HEALTHCARE_MEDICAL","canonical_archetype_id":"C24_BIO_TRIAL_DATA_EVENT_RISK","raw_component_scores_before":{"contract_score":20,"backlog_visibility_score":15,"margin_bridge_score":15,"revision_score":35,"relative_strength_score":60,"customer_quality_score":65,"policy_or_regulatory_score":75,"valuation_repricing_score":70,"execution_risk_score":40,"legal_or_contract_risk_score":10,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0,"trial_endpoint_quality_score":85,"partner_beta_score":80},"weighted_score_before":72,"stage_label_before":"Stage2-Watch","raw_component_scores_after":{"contract_score":20,"backlog_visibility_score":15,"margin_bridge_score":15,"revision_score":35,"relative_strength_score":60,"customer_quality_score":65,"policy_or_regulatory_score":75,"valuation_repricing_score":70,"execution_risk_score":40,"legal_or_contract_risk_score":10,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0,"trial_endpoint_quality_score":85,"partner_beta_score":80},"weighted_score_after":76,"stage_label_after":"Stage2-Actionable_C24_highMAE","changed_components":["c24_pivotal_data_to_optionality_stage2_bonus","high_mae_warning"],"component_delta_explanation":"same data path but higher equity beta and drawdown risk","MFE_90D_pct":52.52,"MAE_90D_pct":-8.49,"score_return_alignment_label":"aligned_high_mae_positive","current_profile_verdict":"current_profile_too_late"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"R7L27-C24-215600-PHOCUS","trigger_id":"R7L27-T005","symbol":"215600","large_sector_id":"L7_BIO_HEALTHCARE_MEDICAL","canonical_archetype_id":"C24_BIO_TRIAL_DATA_EVENT_RISK","raw_component_scores_before":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":0,"revision_score":0,"relative_strength_score":0,"customer_quality_score":20,"policy_or_regulatory_score":0,"valuation_repricing_score":0,"execution_risk_score":95,"legal_or_contract_risk_score":35,"dilution_cb_risk_score":20,"accounting_trust_risk_score":20,"thesis_break_score":100,"forced_liquidation_score":90},"weighted_score_before":18,"stage_label_before":"4C","raw_component_scores_after":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":0,"revision_score":0,"relative_strength_score":0,"customer_quality_score":20,"policy_or_regulatory_score":0,"valuation_repricing_score":0,"execution_risk_score":100,"legal_or_contract_risk_score":35,"dilution_cb_risk_score":20,"accounting_trust_risk_score":20,"thesis_break_score":100,"forced_liquidation_score":90},"weighted_score_after":10,"stage_label_after":"hard_4C_core_trial_failure","changed_components":["c24_core_phase3_failure_hard_4c"],"component_delta_explanation":"core pivotal failure strengthens thesis-break routing","MFE_90D_pct":0.00,"MAE_90D_pct":-74.94,"score_return_alignment_label":"aligned_4C","current_profile_verdict":"current_profile_correct"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"R7L27-C24-084990-ENGENSIS","trigger_id":"R7L27-T006","symbol":"084990","large_sector_id":"L7_BIO_HEALTHCARE_MEDICAL","canonical_archetype_id":"C24_BIO_TRIAL_DATA_EVENT_RISK","raw_component_scores_before":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":0,"revision_score":0,"relative_strength_score":20,"customer_quality_score":15,"policy_or_regulatory_score":0,"valuation_repricing_score":30,"execution_risk_score":90,"legal_or_contract_risk_score":20,"dilution_cb_risk_score":40,"accounting_trust_risk_score":15,"thesis_break_score":85,"rescue_flow_score":80},"weighted_score_before":16,"stage_label_before":"hard_4C","raw_component_scores_after":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":0,"revision_score":0,"relative_strength_score":20,"customer_quality_score":15,"policy_or_regulatory_score":0,"valuation_repricing_score":30,"execution_risk_score":90,"legal_or_contract_risk_score":20,"dilution_cb_risk_score":40,"accounting_trust_risk_score":15,"thesis_break_score":85,"rescue_flow_score":80},"weighted_score_after":20,"stage_label_after":"thesis_break_watch_only_with_rescue_flow_guard","changed_components":["c24_failed_data_rescue_flow_guard"],"component_delta_explanation":"clinical thesis failure remains, but immediate price-protection 4C is too early when rescue flow dominates","MFE_90D_pct":75.06,"MAE_90D_pct":-23.53,"score_return_alignment_label":"counterexample_guard_needed","current_profile_verdict":"current_profile_4C_too_early"}
{"row_type":"residual_contribution","round":"R7","loop":"27","large_sector_id":"L7_BIO_HEALTHCARE_MEDICAL","canonical_archetype_id":"C24_BIO_TRIAL_DATA_EVENT_RISK","new_independent_case_count":4,"reused_case_count":0,"new_symbol_count":4,"same_archetype_new_symbol_count":4,"same_archetype_new_trigger_family_count":3,"new_canonical_archetype_count":0,"new_trigger_family_count":3,"positive_case_count":2,"counterexample_count":2,"current_profile_error_count":3,"tested_existing_calibrated_axes":["stage3_green_revision_min","price_only_blowoff_blocks_positive_stage","full_4b_requires_non_price_evidence","hard_4c_thesis_break_routes_to_4c"],"residual_error_types_found":["current_profile_too_late_on_pivotal_trial_data","current_profile_4C_too_early_when_failed_data_has_rescue_flow"],"loop_contribution_label":"residual_error_found;canonical_archetype_rule_candidate","do_not_propose_new_weight_delta":false,"auto_selected_coverage_gap":"R7/C24 trial-data event risk positive/counterexample balance"}
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
- Price-only rows cannot promote Stage2/Stage3.
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
suggested_next_round = R7
suggested_next_canonical_archetype_id = C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT
suggested_objective = reimbursement/export evidence vs trial-data false positive separation
carry_forward_watch = C24 needs more non-oncology trial data and more failed-data-with-financing counterexamples.
```

## 28. Source Notes

Stock-Web source notes:

* `atlas/manifest.json` confirms `source_name=FinanceData/marcap`, `max_date=2026-02-20`, `price_adjustment_status=raw_unadjusted_marcap`, and `calibration_shard_root=atlas/ohlcv_tradable_by_symbol_year`.
* `atlas/symbol_profiles/000/000100.json`, `039/039200.json`, `215/215600.json`, and `084/084990.json` were checked for availability, row counts, markets, corporate-action candidate dates, and caveats.
* OHLC rows were read from stock-web tradable shards only. Raw shards were not used for calibration.

Evidence source notes:

* MARIPOSA/lazertinib-amivantamab was treated as a pivotal-data-to-optionality family, not as a final approval trigger.
* Engensis/VM202-DPN was treated as failed phase-3 data with rescue-flow stress behavior.
* SillaJen/Pexa-Vec was treated as core pivotal trial futility/failure hard-4C behavior.
* During repository ingestion, primary regulatory/disclosure URLs should be re-expanded and attached to the evidence ledger; this MD is a calibration research artifact, not a legal-source packet.
