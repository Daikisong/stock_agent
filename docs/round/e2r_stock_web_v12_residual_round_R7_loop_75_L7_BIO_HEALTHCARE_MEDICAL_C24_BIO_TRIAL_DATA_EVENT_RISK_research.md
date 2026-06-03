# E2R Stock-Web Historical Calibration / Sector-Archetype Residual Research Round

## 0. Research Metadata

```yaml
mode: historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12
research_session: post_calibrated_sector_archetype_residual_research
scheduled_round: R7
scheduled_loop: 75
completed_round: R7
completed_loop: 75
large_sector_id: L7_BIO_HEALTHCARE_MEDICAL
canonical_archetype_id: C24_BIO_TRIAL_DATA_EVENT_RISK
fine_archetype_id: BIO_PLATFORM_LICENSEOUT_EVENT_QUALITY_AND_REGULATORY_REJECTION_GUARD
output_file: e2r_stock_web_v12_residual_round_R7_loop_75_L7_BIO_HEALTHCARE_MEDICAL_C24_BIO_TRIAL_DATA_EVENT_RISK_research.md
production_scoring_changed: false
shadow_weight_only: true
handoff_prompt_embedded: true
handoff_prompt_executed_now: false
stock_agent_code_access_allowed: false
stock_agent_code_patch_allowed: false
stock_web_price_atlas_access_required: true
```

This loop adds 4 new independent cases, 2 counterexamples, and 3 residual errors for R7/L7_BIO_HEALTHCARE_MEDICAL/C24_BIO_TRIAL_DATA_EVENT_RISK.

## 1. Current Calibrated Profile Assumption

```text
current_default_profile_proxy = e2r_2_1_stock_web_calibrated
previous_baseline_reference = e2r_2_0_baseline
stage2_actionable_evidence_bonus = +2.0
stage3_yellow_total_min = 75.0
stage3_green_total_min = 87.0
stage3_green_revision_min = 55.0
stage3_cross_evidence_green_buffer = +1.5
price_only_blowoff_blocks_positive_stage = true
full_4b_requires_non_price_evidence = true
hard_4c_thesis_break_routes_to_4c = true
```

## 2. Round / Large Sector / Canonical Archetype Scope

| field | value |
|---|---|
| scheduled_round | R7 |
| scheduled_loop | 75 |
| large_sector_id | L7_BIO_HEALTHCARE_MEDICAL |
| canonical_archetype_id | C24_BIO_TRIAL_DATA_EVENT_RISK |
| fine_archetype_id | BIO_PLATFORM_LICENSEOUT_EVENT_QUALITY_AND_REGULATORY_REJECTION_GUARD |
| loop_objective | sector_specific_rule_discovery; canonical_archetype_compression; counterexample_mining; 4C_thesis_break_timing_test; coverage_gap_fill |

## 3. Previous Coverage / Duplicate Avoidance Check

Local prior v12 R7 outputs in the working set show loop 71 covered C24 with `196170`, `087010`, `323990`, and reused `028300`; loop 72 covered C23 with `000100`, `039200`, `028300`, `140410`; loop 73 covered C23 with `196170`, `145020`, `302440`, `028300`; loop 74 covered C25 with `214150`, `338220`, `145720`, `100120`. This loop intentionally avoids those representative trigger groups and uses new C24 symbols: `298380`, `310210`, `397030`, `007390`; `141080` is recorded as narrative-only because of a corporate-action candidate inside the forward window.

| duplicate axis | status |
|---|---|
| same symbol + trigger date reuse | avoided for calibration rows |
| same C24 archetype reuse | allowed; new symbols/trigger families used |
| previous global axis repetition | avoided; only stress-tested and strengthened/kept |

## 4. Stock-Web OHLC Input / Price Source Validation

| manifest field | value |
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
| markets | ['KONEX', 'KOSDAQ', 'KOSDAQ GLOBAL', 'KOSPI'] |
| calibration_shard_root | atlas/ohlcv_tradable_by_symbol_year |
| raw_shard_root | atlas/ohlcv_raw_by_symbol_year |
| schema_path | atlas/schema.json |
| universe_path | atlas/universe/all_symbols.csv |

```text
price_basis = tradable_raw
price_adjustment_status = raw_unadjusted_marcap
calibration_shard_root = atlas/ohlcv_tradable_by_symbol_year
raw_shard_root = atlas/ohlcv_raw_by_symbol_year
stock_web_manifest_max_date = 2026-02-20
```

## 5. Historical Eligibility Gate

| case_id | symbol | entry_date in tradable shard | forward 180D available | corporate-action window | calibration_usable |
|---|---:|---|---|---|---|
| R7L75_C24_298380_ABL_SANOFI_LICENSEOUT_HIGH_MAE_SUCCESS | 298380 | yes | yes | clean_180D_window; corporate_action_candidate_count=0 | true |
| R7L75_C24_310210_BORONOI_CLINICAL_OPTIONALITY_SUCCESS | 310210 | yes | yes | clean_180D_window; corporate_action_candidate_count=0 | true |
| R7L75_C24_397030_APRILBIO_EVENT_SPIKE_FAILED_RERATING | 397030 | yes | yes | clean_180D_window after 2024 trigger; corporate candidates in 2023 only | true |
| R7L75_C24_007390_NATURECELL_JOINTSTEM_REJECTION_4C | 007390 | yes | yes | clean_180D_window; corporate candidates are old 1998-2009 only | true |
| R7L75_C24_141080_LIGACHEM_JNJ_LICENSEOUT_BLOCKED_CA | 141080 | yes | yes | blocked: profile has 2024-04-23 corporate-action candidate in forward window | false / narrative_only |

## 6. Canonical Archetype Compression Map

| canonical_archetype_id | fine_archetype_id | compression rule |
|---|---|---|
| C24_BIO_TRIAL_DATA_EVENT_RISK | BIO_PLATFORM_LICENSEOUT_EVENT_QUALITY_AND_REGULATORY_REJECTION_GUARD | C24 should separate (1) partner-quality/license-out or endpoint-clarity events that can structurally rerate, from (2) price-only clinical spikes and (3) hard regulatory rejection/thesis-break cases. The shadow rule uses non-price evidence gates plus high-MAE and hard-4C guards. |

## 7. Case Selection Summary

| case_id | symbol | company | role | trigger_family | current_profile_verdict |
|---|---:|---|---|---|---|
| R7L75_C24_298380_ABL_SANOFI_LICENSEOUT_HIGH_MAE_SUCCESS | 298380 | 에이비엘바이오 | high_mae_success / positive | large_licenseout_with_partner_quality_but_bear_regime_mae | current_profile_4B_too_late |
| R7L75_C24_310210_BORONOI_CLINICAL_OPTIONALITY_SUCCESS | 310210 | 보로노이 | structural_success / positive | clinical_data_optionality_to_rerating_with_clean_forward_window | current_profile_too_late |
| R7L75_C24_397030_APRILBIO_EVENT_SPIKE_FAILED_RERATING | 397030 | 에이프릴바이오 | failed_rerating / counterexample | clinical_event_spike_without_durable_commercial_bridge | current_profile_false_positive |
| R7L75_C24_007390_NATURECELL_JOINTSTEM_REJECTION_4C | 007390 | 네이처셀 | 4C_success / counterexample | regulatory_rejection_hard_4c_after_failed_approval_thesis | current_profile_4C_too_late |
| R7L75_C24_141080_LIGACHEM_JNJ_LICENSEOUT_BLOCKED_CA | 141080 | 리가켐바이오 | narrative_only | blocked corporate-action forward window | current_profile_data_insufficient |

## 8. Positive vs Counterexample Balance

| positive_case_count | counterexample_count | 4B_case_count | 4C_case_count | calibration_usable_case_count |
|---:|---:|---:|---:|---:|
| 2 | 2 | 3 | 1 | 4 |

The usable set is balanced: two positive structural/high-MAE success cases (`298380`, `310210`) and two counterexamples (`397030`, `007390`).

## 9. Evidence Source Map

| trigger_id | evidence source status | Stage2 fields | Stage3 fields | 4B fields | 4C fields |
|---|---|---|---|---|---|
| T_R7L75_C24_298380_ABL_SANOFI_LICENSEOUT_HIGH_MAE_SUCCESS | Sanofi/ABL301 license-out event proxy; non-price partner-quality evidence at trigger, but the 2022 biotech beta path created deep MAE before durable rerating. | `public_event_or_disclosure,customer_or_order_quality,relative_strength,policy_or_regulatory_optionality` | `multiple_public_sources,durable_customer_confirmation,financial_visibility` | `valuation_blowoff,positioning_overheat,margin_or_backlog_slowdown` | `` |
| T_R7L75_C24_310210_BORONOI_CLINICAL_OPTIONALITY_SUCCESS | VRN/oncology clinical-data optionality and repeated relative strength proxy; stock-web rows show a clean low-MAE repricing path after the trigger. | `public_event_or_disclosure,relative_strength,policy_or_regulatory_optionality,early_revision_signal` | `multiple_public_sources,durable_customer_confirmation,low_red_team_risk,financial_visibility` | `valuation_blowoff,positioning_overheat` | `` |
| T_R7L75_C24_397030_APRILBIO_EVENT_SPIKE_FAILED_RERATING | APB/SAFA platform clinical-event spike proxy. The first reaction was large, but 90D/180D MAE shows the event lacked enough commercial/regulatory conversion quality for Green promotion. | `public_event_or_disclosure,relative_strength,policy_or_regulatory_optionality` | `` | `price_only_local_peak,valuation_blowoff,positioning_overheat` | `thesis_evidence_broken` |
| T_R7L75_C24_007390_NATURECELL_JOINTSTEM_REJECTION_4C | JointStem regulatory rejection/approval-failure proxy. The post-trigger path shows why C24 needs a hard 4C routing layer when the regulatory thesis breaks. | `public_event_or_disclosure,policy_or_regulatory_optionality` | `` | `price_only_local_peak,positioning_overheat` | `regulatory_rejection,thesis_evidence_broken` |

## 10. Price Data Source Map

| symbol | company | entry row source | profile_path | price_basis | adjustment |
|---:|---|---|---|---|---|
| 298380 | 에이비엘바이오 | `atlas/ohlcv_tradable_by_symbol_year/298/298380/2022.csv` | `atlas/symbol_profiles/298/298380.json` | tradable_raw | raw_unadjusted_marcap |
| 310210 | 보로노이 | `atlas/ohlcv_tradable_by_symbol_year/310/310210/2024.csv|atlas/ohlcv_tradable_by_symbol_year/310/310210/2025.csv` | `atlas/symbol_profiles/310/310210.json` | tradable_raw | raw_unadjusted_marcap |
| 397030 | 에이프릴바이오 | `atlas/ohlcv_tradable_by_symbol_year/397/397030/2024.csv|atlas/ohlcv_tradable_by_symbol_year/397/397030/2025.csv` | `atlas/symbol_profiles/397/397030.json` | tradable_raw | raw_unadjusted_marcap |
| 007390 | 네이처셀 | `atlas/ohlcv_tradable_by_symbol_year/007/007390/2023.csv` | `atlas/symbol_profiles/007/007390.json` | tradable_raw | raw_unadjusted_marcap |
| 141080 | 리가켐바이오 | `atlas/ohlcv_tradable_by_symbol_year/141/141080/2023.csv|atlas/ohlcv_tradable_by_symbol_year/141/141080/2024.csv` | `atlas/symbol_profiles/141/141080.json` | tradable_raw | raw_unadjusted_marcap |

## 11. Case-by-Case Trigger Grid

| trigger_id | symbol | company | trigger_type | trigger_date | entry_date | entry_price | MFE90 | MAE90 | peak_date | peak_price | drawdown_after_peak | current_profile_verdict | role |
|---|---:|---|---|---|---|---:|---:|---:|---|---:|---:|---|---|
| T_R7L75_C24_298380_ABL_SANOFI_LICENSEOUT_HIGH_MAE_SUCCESS | 298380 | 에이비엘바이오 | Stage2-Actionable | 2022-01-12 | 2022-01-12 | 26150 | 33.08% | -26.58% | 2022-01-21 | 34800 | -51.01% | current_profile_4B_too_late | representative |
| T_R7L75_C24_310210_BORONOI_CLINICAL_OPTIONALITY_SUCCESS | 310210 | 보로노이 | Stage2-Actionable | 2024-06-26 | 2024-06-26 | 49350 | 147.62% | -4.86% | 2025-03-10 | 153000 | -39.15% | current_profile_too_late | representative |
| T_R7L75_C24_397030_APRILBIO_EVENT_SPIKE_FAILED_RERATING | 397030 | 에이프릴바이오 | Stage2-Actionable | 2024-06-20 | 2024-06-20 | 19470 | 33.02% | -25.27% | 2024-10-15 | 25900 | -53.75% | current_profile_false_positive | representative |
| T_R7L75_C24_007390_NATURECELL_JOINTSTEM_REJECTION_4C | 007390 | 네이처셀 | Stage4C-ThesisBreak | 2023-04-07 | 2023-04-10 | 12110 | 5.04% | -41.95% | 2023-04-14 | 12720 | -44.73% | current_profile_4C_too_late | representative |

## 12. Trigger-Level OHLC Backtest Tables

| trigger_id | entry_price | MFE_30D | MAE_30D | MFE_90D | MAE_90D | MFE_180D | MAE_180D | MFE_1Y | MAE_1Y | MFE_2Y | peak_date | peak_price | drawdown_after_peak | below_entry_30D | below_entry_90D |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|---|---:|---:|---|---|
| T_R7L75_C24_298380_ABL_SANOFI_LICENSEOUT_HIGH_MAE_SUCCESS | 26150 | 33.08% | -8.99% | 33.08% | -26.58% | 33.08% | -34.80% | 33.08% | -34.80% | unavailable_by_2Y_window_or_not_required | 2022-01-21 | 34800 | -51.01% | true | true |
| T_R7L75_C24_310210_BORONOI_CLINICAL_OPTIONALITY_SUCCESS | 49350 | 70.21% | -4.86% | 147.62% | -4.86% | 210.03% | -4.86% | 210.03% | -39.15% | unavailable_by_2Y_window_or_not_required | 2025-03-10 | 153000 | -39.15% | true | true |
| T_R7L75_C24_397030_APRILBIO_EVENT_SPIKE_FAILED_RERATING | 19470 | 14.79% | -11.97% | 33.02% | -25.27% | 33.02% | -30.20% | 33.02% | -53.75% | unavailable_by_2Y_window_or_not_required | 2024-10-15 | 25900 | -53.75% | true | true |
| T_R7L75_C24_007390_NATURECELL_JOINTSTEM_REJECTION_4C | 12110 | 5.04% | -23.12% | 5.04% | -41.95% | 5.04% | -41.95% | 5.04% | -41.95% | unavailable_by_2Y_window_or_not_required | 2023-04-14 | 12720 | -44.73% | true | true |

## 13. Current Calibrated Profile Stress Test

| case_id | P0 likely judgment | actual MFE/MAE alignment | current_profile_verdict | residual |
|---|---|---|---|---|
| R7L75_C24_298380_ABL_SANOFI_LICENSEOUT_HIGH_MAE_SUCCESS | Promotes license-out quality but lacks enough high-MAE/4B overlay during 2022 bear regime. | MFE180 33.08% / MAE180 -34.80% / drawdown -51.01% | current_profile_4B_too_late | C24 needs evidence-quality and hard rejection guards rather than a generic biotech event bonus. |
| R7L75_C24_310210_BORONOI_CLINICAL_OPTIONALITY_SUCCESS | Under-promotes until repeated confirmation despite clean low-MAE clinical optionality path. | MFE180 210.03% / MAE180 -4.86% / drawdown -39.15% | current_profile_too_late | C24 needs evidence-quality and hard rejection guards rather than a generic biotech event bonus. |
| R7L75_C24_397030_APRILBIO_EVENT_SPIKE_FAILED_RERATING | Can over-promote price/event spike without durable endpoint or commercialization bridge. | MFE180 33.02% / MAE180 -30.20% / drawdown -53.75% | current_profile_false_positive | C24 needs evidence-quality and hard rejection guards rather than a generic biotech event bonus. |
| R7L75_C24_007390_NATURECELL_JOINTSTEM_REJECTION_4C | Hard regulatory rejection should be routed directly to 4C; delayed routing fails protection. | MFE180 5.04% / MAE180 -41.95% / drawdown -44.73% | current_profile_4C_too_late | C24 needs evidence-quality and hard rejection guards rather than a generic biotech event bonus. |

```text
existing_axis_tested = stage2_actionable_evidence_bonus | price_only_blowoff_blocks_positive_stage | full_4b_requires_non_price_evidence | hard_4c_thesis_break_routes_to_4c
existing_axis_strengthened = price_only_blowoff_blocks_positive_stage | full_4b_requires_non_price_evidence | hard_4c_thesis_break_routes_to_4c
existing_axis_weakened = null
existing_axis_kept = stage3_yellow_total_min | stage3_green_total_min | stage3_green_revision_min | stage3_cross_evidence_green_buffer
new_axis_proposed = C24_clinical_event_quality_gate | C24_partner_quality_licenseout_bonus | C24_regulatory_rejection_hard_4c_guard | C24_high_mae_success_position_size_guard
```

## 14. Stage2 / Yellow / Green Comparison

| case_id | Stage2 Actionable entry | Stage3/Green issue | green_lateness_ratio | interpretation |
|---|---|---|---|---|
| R7L75_C24_298380_ABL_SANOFI_LICENSEOUT_HIGH_MAE_SUCCESS | 2022-01-12 @ 26150 | Stage3-Yellow+4B/MAE-Watch | 0.15 if Stage3 waits for Sanofi confirmation; not late on price, but risk overlay required | current_profile_4B_too_late |
| R7L75_C24_310210_BORONOI_CLINICAL_OPTIONALITY_SUCCESS | 2024-06-26 @ 49350 | Stage3-Green+4B-Watch | 0.40 if Green waits for Nov-2024 repeat confirmation; still acceptable but loses early convexity | current_profile_too_late |
| R7L75_C24_397030_APRILBIO_EVENT_SPIKE_FAILED_RERATING | 2024-06-20 @ 19470 | Stage2-Watch/4B-Guard | not_applicable:no_confirmed_Stage3_Green_trigger | current_profile_false_positive |
| R7L75_C24_007390_NATURECELL_JOINTSTEM_REJECTION_4C | 2023-04-10 @ 12110 | Stage4C-ThesisBreak | not_applicable:hard_4c_case | current_profile_4C_too_late |

## 15. 4B Local vs Full-window Timing Audit

| 4B/overlay trigger | symbol | Stage2 entry | overlay entry | full peak | local proximity | full-window proximity | evidence type | verdict |
|---|---:|---:|---:|---:|---:|---:|---|---|
| 4B_R7L75_C24_298380_ABL_SANOFI_LICENSEOUT_HIGH_MAE_SUCCESS | 298380 | 26150 | 33050 | 34800 | 0.76 | 0.76 | `valuation_blowoff,positioning_overheat,margin_or_backlog_slowdown` | good_full_window_4B_timing |
| 4B_R7L75_C24_310210_BORONOI_CLINICAL_OPTIONALITY_SUCCESS | 310210 | 49350 | 141900 | 153000 | 0.92 | 0.92 | `valuation_blowoff,positioning_overheat` | good_full_window_4B_timing |
| 4B_R7L75_C24_397030_APRILBIO_EVENT_SPIKE_FAILED_RERATING | 397030 | 19470 | 24450 | 25900 | 0.77 | 0.77 | `price_only_local_peak,valuation_blowoff,positioning_overheat` | price_only_or_regulatory_overlay_not_positive_stage |
| 4B_R7L75_C24_007390_NATURECELL_JOINTSTEM_REJECTION_4C | 007390 | 12110 | 24650 | 12720 | 0.98 | 0.98 | `price_only_local_peak,positioning_overheat` | price_only_or_regulatory_overlay_not_positive_stage |

## 16. 4C Protection Audit

| case_id | 4C protection label | thesis-break reading |
|---|---|---|
| R7L75_C24_298380_ABL_SANOFI_LICENSEOUT_HIGH_MAE_SUCCESS | not_applicable | positive_but_high_mae_licenseout_success_requires_size_guard |
| R7L75_C24_310210_BORONOI_CLINICAL_OPTIONALITY_SUCCESS | not_applicable | positive_structural_success_low_mae_clinical_optional_rerating |
| R7L75_C24_397030_APRILBIO_EVENT_SPIKE_FAILED_RERATING | thesis_break_watch_only | event_spike_failed_rerating_high_mae_counterexample |
| R7L75_C24_007390_NATURECELL_JOINTSTEM_REJECTION_4C | hard_4c_success | hard_4c_success_regulatory_rejection_protection |

## 17. Sector-Specific Rule Candidate

**Rule candidate: `l7_bio_event_quality_and_4c_guard`.** In L7, a biotech event should not be promoted by price reaction alone. Promotion requires one of: credible partner/license-out quality, clear endpoint/regulatory path, durable clinical optionality confirmed by multiple sources, or financial runway visibility. Clinical-event spikes without this bridge are capped at Stage2-Watch/4B-Watch. Regulatory rejection routes directly to hard 4C.

## 18. Canonical-Archetype Rule Candidate

**Canonical candidate: `c24_partner_quality_endpoint_clarity_guard`.** C24 gets a small positive shadow delta when partner quality or endpoint clarity is strong, but a stronger negative guard when the event is price-only, lacks endpoint/regulatory bridge, or becomes a hard rejection. High-MAE success is not disqualified, but it must carry a size/4B overlay rather than clean Green.

## 19. Before / After Backtest Comparison

| profile_id | profile_scope | profile_hypothesis | changed_axes | eligible_trigger_count | selected_entry_trigger_per_case | avg_MFE_90D_pct | avg_MAE_90D_pct | avg_MFE_180D_pct | avg_MAE_180D_pct | false_positive_rate | missed_structural_count | late_green_count | avg_four_b_local_peak_proximity | avg_four_b_full_window_peak_proximity | score_return_alignment_verdict |
|---|---|---|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|
| P0 | e2r_2_1_stock_web_calibrated_proxy | current global calibrated proxy | none | 4 | 298380|310210|397030|007390 | 54.69 | -24.66 | 70.29 | -27.95 | 0.50 | 0 | 1 | 0.86 | 0.86 | mixed: captures license-out optionality but over-promotes clinical spikes and routes rejection late |
| P0b | e2r_2_0_baseline_reference | rollback reference | pre-calibration | 4 | same | 54.69 | -24.66 | 70.29 | -27.95 | 0.50 | 1 | 1 | 0.86 | 0.86 | worse: less explicit 4C and no high-MAE license-out guard |
| P1 | sector_specific_candidate_profile | L7 clinical event quality gate | clinical_event_quality_gate; high_mae_guard | 4 | 298380|310210 positive; 397030 watch; 007390 4C | 90.35 | -15.72 | 121.56 | -19.83 | 0.00 | 0 | 0 | 0.84 | 0.84 | better positive/counter separation |
| P2 | canonical_archetype_candidate_profile | C24 partner-quality and endpoint-clarity compression | partner_quality_bonus; endpoint_clarity_guard | 4 | same as P1 | 90.35 | -15.72 | 121.56 | -19.83 | 0.00 | 0 | 0 | 0.84 | 0.84 | canonical rule candidate |
| P3 | counterexample_guard_profile | hard regulatory rejection and price-only spike guard | price_only_event_spike_cap; hard_4c_rejection_route | 4 | 397030 capped; 007390 4C | 19.03 | -33.61 | 19.03 | -36.08 | 0.00 | 0 | 0 | 0.88 | 0.88 | protects false positives |

## 20. Score-Return Alignment Matrix

| case_id | before score/stage | after score/stage | MFE90/MAE90 | alignment |
|---|---|---|---|---|
| R7L75_C24_298380_ABL_SANOFI_LICENSEOUT_HIGH_MAE_SUCCESS | 86 / Stage3-Yellow/Green-borderline | 84 / Stage3-Yellow+4B/MAE-Watch | 33.08% / -26.58% | positive_but_high_mae_licenseout_success_requires_size_guard |
| R7L75_C24_310210_BORONOI_CLINICAL_OPTIONALITY_SUCCESS | 82 / Stage3-Yellow | 90 / Stage3-Green+4B-Watch | 147.62% / -4.86% | positive_structural_success_low_mae_clinical_optional_rerating |
| R7L75_C24_397030_APRILBIO_EVENT_SPIKE_FAILED_RERATING | 78 / Stage3-Yellow false-promotion risk | 62 / Stage2-Watch/4B-Guard | 33.02% / -25.27% | event_spike_failed_rerating_high_mae_counterexample |
| R7L75_C24_007390_NATURECELL_JOINTSTEM_REJECTION_4C | 70 / Stage2/3 false-positive if rejection risk not routed | 32 / Stage4C-ThesisBreak | 5.04% / -41.95% | hard_4c_success_regulatory_rejection_protection |

## 21. Coverage Matrix

| large_sector_id | canonical_archetype_id | fine_archetype_id | positive_case_count | counterexample_count | 4B_case_count | 4C_case_count | new_independent_case_count | reused_case_count | calibration_usable_trigger_count | representative_trigger_count | current_profile_error_count | sector_rule_candidate | canonical_rule_candidate | coverage_gap_after_this_loop |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|---|---|
| L7_BIO_HEALTHCARE_MEDICAL | C24_BIO_TRIAL_DATA_EVENT_RISK | BIO_PLATFORM_LICENSEOUT_EVENT_QUALITY_AND_REGULATORY_REJECTION_GUARD | 2 | 2 | 3 | 1 | 4 | 0 | 4 | 4 | 3 | true | true | C24 now has additional non-HLB regulatory-rejection and non-Alteogen platform/license-out coverage; still needs overseas approval-to-sales holdout cases. |

## 22. Residual Contribution Summary

```text
new_independent_case_count: 4
reused_case_count: 0
reused_case_ids: []
new_symbol_count: 4
new_canonical_archetype_count: 0
new_fine_archetype_count: 1
new_trigger_family_count: 4
tested_existing_calibrated_axes: [stage2_actionable_evidence_bonus, price_only_blowoff_blocks_positive_stage, full_4b_requires_non_price_evidence, hard_4c_thesis_break_routes_to_4c]
residual_error_types_found: [clinical_event_spike_false_positive, high_mae_licenseout_success_needs_overlay, regulatory_rejection_4c_too_late, clinical_optionality_too_late]
new_axis_proposed: [C24_clinical_event_quality_gate, C24_partner_quality_licenseout_bonus, C24_regulatory_rejection_hard_4c_guard, C24_high_mae_success_position_size_guard]
existing_axis_strengthened: [price_only_blowoff_blocks_positive_stage, full_4b_requires_non_price_evidence, hard_4c_thesis_break_routes_to_4c]
existing_axis_weakened: null
existing_axis_kept: [stage2_actionable_evidence_bonus, stage3_yellow_total_min, stage3_green_total_min, stage3_green_revision_min, stage3_cross_evidence_green_buffer]
sector_specific_rule_candidate: true
canonical_archetype_rule_candidate: true
no_new_signal_reason: null
loop_contribution_label: canonical_archetype_rule_candidate
do_not_propose_new_weight_delta: false
```

## 23. Validation Scope / Non-Validation Scope

**Validation scope:** historical trigger-level OHLC using stock-web tradable shards; 30D/90D/180D MFE/MAE; C24 positive/counterexample balance; current calibrated profile stress test; 4B local/full-window split; 4C rejection guard.

**Non-validation scope:** no live stock discovery, no investment recommendation, no production scoring change, no `stock_agent` code access, no broker/API execution, no current watchlist.

## 24. Shadow Weight Calibration

```csv
row_type,axis,scope,large_sector_id,canonical_archetype_id,baseline_value,tested_value,delta,reason,backtest_effect,trigger_ids,calibration_usable_count,new_independent_case_count,counterexample_count,confidence,proposal_type,notes

shadow_weight,C24_clinical_event_quality_gate,canonical_archetype_specific,L7_BIO_HEALTHCARE_MEDICAL,C24_BIO_TRIAL_DATA_EVENT_RISK,0,1,+1,"require endpoint/regulatory clarity before Stage3 promotion","separates 310210 positive from 397030 spike",T_R7L75_C24_298380_ABL_SANOFI_LICENSEOUT_HIGH_MAE_SUCCESS|T_R7L75_C24_310210_BORONOI_CLINICAL_OPTIONALITY_SUCCESS|T_R7L75_C24_397030_APRILBIO_EVENT_SPIKE_FAILED_RERATING|T_R7L75_C24_007390_NATURECELL_JOINTSTEM_REJECTION_4C,4,4,2,medium,canonical_shadow_only,"not production; post-calibrated residual"

shadow_weight,C24_regulatory_rejection_hard_4c_guard,canonical_archetype_specific,L7_BIO_HEALTHCARE_MEDICAL,C24_BIO_TRIAL_DATA_EVENT_RISK,0,1,+1,"route explicit regulatory rejection to 4C","protects 007390 rejection path",T_R7L75_C24_007390_NATURECELL_JOINTSTEM_REJECTION_4C,4,4,2,medium,canonical_shadow_only,"not production; hard 4C guard"

```

## 25. Machine-Readable Rows

### JSONL
```jsonl
{"row_type":"price_source_validation","source":"Songdaiki/stock-web","source_url":"https://github.com/Songdaiki/stock-web","manifest_path":"atlas/manifest.json","schema_path":"atlas/schema.json","universe_path":"atlas/universe/all_symbols.csv","manifest_max_date":"2026-02-20","source_name":"FinanceData/marcap","source_repo_url":"https://github.com/FinanceData/marcap","tradable_row_count":14354401,"raw_row_count":15214118,"symbol_count":5414,"active_like_symbol_count":2868,"inactive_or_delisted_like_symbol_count":2546,"markets":["KONEX","KOSDAQ","KOSDAQ GLOBAL","KOSPI"],"price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","calibration_shard_root":"atlas/ohlcv_tradable_by_symbol_year","raw_shard_root":"atlas/ohlcv_raw_by_symbol_year","validation_status":"usable_for_historical_calibration"}
{"row_type":"case","case_id":"R7L75_C24_298380_ABL_SANOFI_LICENSEOUT_HIGH_MAE_SUCCESS","symbol":"298380","company_name":"에이비엘바이오","round":"R7","loop":"75","large_sector_id":"L7_BIO_HEALTHCARE_MEDICAL","canonical_archetype_id":"C24_BIO_TRIAL_DATA_EVENT_RISK","fine_archetype_id":"BIO_PLATFORM_LICENSEOUT_EVENT_QUALITY_AND_REGULATORY_REJECTION_GUARD","case_type":"high_mae_success","positive_or_counterexample":"positive","best_trigger":"T_R7L75_C24_298380_ABL_SANOFI_LICENSEOUT_HIGH_MAE_SUCCESS","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"positive_but_high_mae_licenseout_success_requires_size_guard","current_profile_verdict":"current_profile_4B_too_late","price_source":"Songdaiki/stock-web","notes":"Sanofi/ABL301 license-out event proxy; non-price partner-quality evidence at trigger, but the 2022 biotech beta path created deep MAE before durable rerating."}
{"row_type":"case","case_id":"R7L75_C24_310210_BORONOI_CLINICAL_OPTIONALITY_SUCCESS","symbol":"310210","company_name":"보로노이","round":"R7","loop":"75","large_sector_id":"L7_BIO_HEALTHCARE_MEDICAL","canonical_archetype_id":"C24_BIO_TRIAL_DATA_EVENT_RISK","fine_archetype_id":"BIO_PLATFORM_LICENSEOUT_EVENT_QUALITY_AND_REGULATORY_REJECTION_GUARD","case_type":"structural_success","positive_or_counterexample":"positive","best_trigger":"T_R7L75_C24_310210_BORONOI_CLINICAL_OPTIONALITY_SUCCESS","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"positive_structural_success_low_mae_clinical_optional_rerating","current_profile_verdict":"current_profile_too_late","price_source":"Songdaiki/stock-web","notes":"VRN/oncology clinical-data optionality and repeated relative strength proxy; stock-web rows show a clean low-MAE repricing path after the trigger."}
{"row_type":"case","case_id":"R7L75_C24_397030_APRILBIO_EVENT_SPIKE_FAILED_RERATING","symbol":"397030","company_name":"에이프릴바이오","round":"R7","loop":"75","large_sector_id":"L7_BIO_HEALTHCARE_MEDICAL","canonical_archetype_id":"C24_BIO_TRIAL_DATA_EVENT_RISK","fine_archetype_id":"BIO_PLATFORM_LICENSEOUT_EVENT_QUALITY_AND_REGULATORY_REJECTION_GUARD","case_type":"failed_rerating","positive_or_counterexample":"counterexample","best_trigger":"T_R7L75_C24_397030_APRILBIO_EVENT_SPIKE_FAILED_RERATING","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"event_spike_failed_rerating_high_mae_counterexample","current_profile_verdict":"current_profile_false_positive","price_source":"Songdaiki/stock-web","notes":"APB/SAFA platform clinical-event spike proxy. The first reaction was large, but 90D/180D MAE shows the event lacked enough commercial/regulatory conversion quality for Green promotion."}
{"row_type":"case","case_id":"R7L75_C24_007390_NATURECELL_JOINTSTEM_REJECTION_4C","symbol":"007390","company_name":"네이처셀","round":"R7","loop":"75","large_sector_id":"L7_BIO_HEALTHCARE_MEDICAL","canonical_archetype_id":"C24_BIO_TRIAL_DATA_EVENT_RISK","fine_archetype_id":"BIO_PLATFORM_LICENSEOUT_EVENT_QUALITY_AND_REGULATORY_REJECTION_GUARD","case_type":"4C_success","positive_or_counterexample":"counterexample","best_trigger":"T_R7L75_C24_007390_NATURECELL_JOINTSTEM_REJECTION_4C","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"hard_4c_success_regulatory_rejection_protection","current_profile_verdict":"current_profile_4C_too_late","price_source":"Songdaiki/stock-web","notes":"JointStem regulatory rejection/approval-failure proxy. The post-trigger path shows why C24 needs a hard 4C routing layer when the regulatory thesis breaks."}
{"row_type":"trigger","trigger_id":"T_R7L75_C24_298380_ABL_SANOFI_LICENSEOUT_HIGH_MAE_SUCCESS","case_id":"R7L75_C24_298380_ABL_SANOFI_LICENSEOUT_HIGH_MAE_SUCCESS","symbol":"298380","company_name":"에이비엘바이오","round":"R7","loop":"75","scheduled_round":"R7","scheduled_loop":"75","round_schedule_status":"valid","round_sector_consistency":"pass","large_sector_id":"L7_BIO_HEALTHCARE_MEDICAL","canonical_archetype_id":"C24_BIO_TRIAL_DATA_EVENT_RISK","fine_archetype_id":"BIO_PLATFORM_LICENSEOUT_EVENT_QUALITY_AND_REGULATORY_REJECTION_GUARD","sector":"bio_healthcare_medical","primary_archetype":"bio trial / regulatory event risk / platform license-out quality","loop_objective":"sector_specific_rule_discovery|canonical_archetype_compression|counterexample_mining|4C_thesis_break_timing_test|coverage_gap_fill","trigger_type":"Stage2-Actionable","trigger_date":"2022-01-12","entry_date":"2022-01-12","entry_price":26150,"evidence_available_at_that_date":"Sanofi/ABL301 license-out event proxy; non-price partner-quality evidence at trigger, but the 2022 biotech beta path created deep MAE before durable rerating.","evidence_source":"source_proxy: public disclosure/news/IR around trigger date; URL verification deferred to implementation batch","stage2_evidence_fields":["public_event_or_disclosure","customer_or_order_quality","relative_strength","policy_or_regulatory_optionality"],"stage3_evidence_fields":["multiple_public_sources","durable_customer_confirmation","financial_visibility"],"stage4b_evidence_fields":["valuation_blowoff","positioning_overheat","margin_or_backlog_slowdown"],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/298/298380/2022.csv","profile_path":"atlas/symbol_profiles/298/298380.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":33.08,"MFE_90D_pct":33.08,"MFE_180D_pct":33.08,"MFE_1Y_pct":33.08,"MFE_2Y_pct":null,"MAE_30D_pct":-8.99,"MAE_90D_pct":-26.58,"MAE_180D_pct":-34.8,"MAE_1Y_pct":-34.8,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2022-01-21","peak_price":34800,"drawdown_after_peak_pct":-51.01,"green_lateness_ratio":"0.15 if Stage3 waits for Sanofi confirmation; not late on price, but risk overlay required","four_b_local_peak_proximity":0.76,"four_b_full_window_peak_proximity":0.76,"four_b_timing_verdict":"good_full_window_4B_timing","four_b_evidence_type":"valuation_blowoff|positioning_overheat","four_c_protection_label":"not_applicable","trigger_outcome_label":"positive_but_high_mae_licenseout_success_requires_size_guard","current_profile_verdict":"current_profile_4B_too_late","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window; corporate_action_candidate_count=0","same_entry_group_id":"SEG_R7L75_C24_298380_ABL_SANOFI_LICENSEOUT_HIGH_MAE_SUCCESS_2022-01-12","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"T_R7L75_C24_310210_BORONOI_CLINICAL_OPTIONALITY_SUCCESS","case_id":"R7L75_C24_310210_BORONOI_CLINICAL_OPTIONALITY_SUCCESS","symbol":"310210","company_name":"보로노이","round":"R7","loop":"75","scheduled_round":"R7","scheduled_loop":"75","round_schedule_status":"valid","round_sector_consistency":"pass","large_sector_id":"L7_BIO_HEALTHCARE_MEDICAL","canonical_archetype_id":"C24_BIO_TRIAL_DATA_EVENT_RISK","fine_archetype_id":"BIO_PLATFORM_LICENSEOUT_EVENT_QUALITY_AND_REGULATORY_REJECTION_GUARD","sector":"bio_healthcare_medical","primary_archetype":"bio trial / regulatory event risk / platform license-out quality","loop_objective":"sector_specific_rule_discovery|canonical_archetype_compression|counterexample_mining|4C_thesis_break_timing_test|coverage_gap_fill","trigger_type":"Stage2-Actionable","trigger_date":"2024-06-26","entry_date":"2024-06-26","entry_price":49350,"evidence_available_at_that_date":"VRN/oncology clinical-data optionality and repeated relative strength proxy; stock-web rows show a clean low-MAE repricing path after the trigger.","evidence_source":"source_proxy: public disclosure/news/IR around trigger date; URL verification deferred to implementation batch","stage2_evidence_fields":["public_event_or_disclosure","relative_strength","policy_or_regulatory_optionality","early_revision_signal"],"stage3_evidence_fields":["multiple_public_sources","durable_customer_confirmation","low_red_team_risk","financial_visibility"],"stage4b_evidence_fields":["valuation_blowoff","positioning_overheat"],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/310/310210/2024.csv|atlas/ohlcv_tradable_by_symbol_year/310/310210/2025.csv","profile_path":"atlas/symbol_profiles/310/310210.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":70.21,"MFE_90D_pct":147.62,"MFE_180D_pct":210.03,"MFE_1Y_pct":210.03,"MFE_2Y_pct":null,"MAE_30D_pct":-4.86,"MAE_90D_pct":-4.86,"MAE_180D_pct":-4.86,"MAE_1Y_pct":-39.15,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2025-03-10","peak_price":153000,"drawdown_after_peak_pct":-39.15,"green_lateness_ratio":"0.40 if Green waits for Nov-2024 repeat confirmation; still acceptable but loses early convexity","four_b_local_peak_proximity":0.92,"four_b_full_window_peak_proximity":0.92,"four_b_timing_verdict":"good_full_window_4B_timing","four_b_evidence_type":"valuation_blowoff|positioning_overheat","four_c_protection_label":"not_applicable","trigger_outcome_label":"positive_structural_success_low_mae_clinical_optional_rerating","current_profile_verdict":"current_profile_too_late","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window; corporate_action_candidate_count=0","same_entry_group_id":"SEG_R7L75_C24_310210_BORONOI_CLINICAL_OPTIONALITY_SUCCESS_2024-06-26","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"T_R7L75_C24_397030_APRILBIO_EVENT_SPIKE_FAILED_RERATING","case_id":"R7L75_C24_397030_APRILBIO_EVENT_SPIKE_FAILED_RERATING","symbol":"397030","company_name":"에이프릴바이오","round":"R7","loop":"75","scheduled_round":"R7","scheduled_loop":"75","round_schedule_status":"valid","round_sector_consistency":"pass","large_sector_id":"L7_BIO_HEALTHCARE_MEDICAL","canonical_archetype_id":"C24_BIO_TRIAL_DATA_EVENT_RISK","fine_archetype_id":"BIO_PLATFORM_LICENSEOUT_EVENT_QUALITY_AND_REGULATORY_REJECTION_GUARD","sector":"bio_healthcare_medical","primary_archetype":"bio trial / regulatory event risk / platform license-out quality","loop_objective":"sector_specific_rule_discovery|canonical_archetype_compression|counterexample_mining|4C_thesis_break_timing_test|coverage_gap_fill","trigger_type":"Stage2-Actionable","trigger_date":"2024-06-20","entry_date":"2024-06-20","entry_price":19470,"evidence_available_at_that_date":"APB/SAFA platform clinical-event spike proxy. The first reaction was large, but 90D/180D MAE shows the event lacked enough commercial/regulatory conversion quality for Green promotion.","evidence_source":"source_proxy: public disclosure/news/IR around trigger date; URL verification deferred to implementation batch","stage2_evidence_fields":["public_event_or_disclosure","relative_strength","policy_or_regulatory_optionality"],"stage3_evidence_fields":[],"stage4b_evidence_fields":["price_only_local_peak","valuation_blowoff","positioning_overheat"],"stage4c_evidence_fields":["thesis_evidence_broken"],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/397/397030/2024.csv|atlas/ohlcv_tradable_by_symbol_year/397/397030/2025.csv","profile_path":"atlas/symbol_profiles/397/397030.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":14.79,"MFE_90D_pct":33.02,"MFE_180D_pct":33.02,"MFE_1Y_pct":33.02,"MFE_2Y_pct":null,"MAE_30D_pct":-11.97,"MAE_90D_pct":-25.27,"MAE_180D_pct":-30.2,"MAE_1Y_pct":-53.75,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-10-15","peak_price":25900,"drawdown_after_peak_pct":-53.75,"green_lateness_ratio":"not_applicable:no_confirmed_Stage3_Green_trigger","four_b_local_peak_proximity":0.77,"four_b_full_window_peak_proximity":0.77,"four_b_timing_verdict":"price_only_local_4B_watch_or_hard_4C","four_b_evidence_type":"price_only|regulatory_or_event_risk","four_c_protection_label":"thesis_break_watch_only","trigger_outcome_label":"event_spike_failed_rerating_high_mae_counterexample","current_profile_verdict":"current_profile_false_positive","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window after 2024 trigger; corporate candidates in 2023 only","same_entry_group_id":"SEG_R7L75_C24_397030_APRILBIO_EVENT_SPIKE_FAILED_RERATING_2024-06-20","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"T_R7L75_C24_007390_NATURECELL_JOINTSTEM_REJECTION_4C","case_id":"R7L75_C24_007390_NATURECELL_JOINTSTEM_REJECTION_4C","symbol":"007390","company_name":"네이처셀","round":"R7","loop":"75","scheduled_round":"R7","scheduled_loop":"75","round_schedule_status":"valid","round_sector_consistency":"pass","large_sector_id":"L7_BIO_HEALTHCARE_MEDICAL","canonical_archetype_id":"C24_BIO_TRIAL_DATA_EVENT_RISK","fine_archetype_id":"BIO_PLATFORM_LICENSEOUT_EVENT_QUALITY_AND_REGULATORY_REJECTION_GUARD","sector":"bio_healthcare_medical","primary_archetype":"bio trial / regulatory event risk / platform license-out quality","loop_objective":"sector_specific_rule_discovery|canonical_archetype_compression|counterexample_mining|4C_thesis_break_timing_test|coverage_gap_fill","trigger_type":"Stage4C-ThesisBreak","trigger_date":"2023-04-07","entry_date":"2023-04-10","entry_price":12110,"evidence_available_at_that_date":"JointStem regulatory rejection/approval-failure proxy. The post-trigger path shows why C24 needs a hard 4C routing layer when the regulatory thesis breaks.","evidence_source":"source_proxy: public disclosure/news/IR around trigger date; URL verification deferred to implementation batch","stage2_evidence_fields":["public_event_or_disclosure","policy_or_regulatory_optionality"],"stage3_evidence_fields":[],"stage4b_evidence_fields":["price_only_local_peak","positioning_overheat"],"stage4c_evidence_fields":["regulatory_rejection","thesis_evidence_broken"],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/007/007390/2023.csv","profile_path":"atlas/symbol_profiles/007/007390.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":5.04,"MFE_90D_pct":5.04,"MFE_180D_pct":5.04,"MFE_1Y_pct":5.04,"MFE_2Y_pct":null,"MAE_30D_pct":-23.12,"MAE_90D_pct":-41.95,"MAE_180D_pct":-41.95,"MAE_1Y_pct":-41.95,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2023-04-14","peak_price":12720,"drawdown_after_peak_pct":-44.73,"green_lateness_ratio":"not_applicable:hard_4c_case","four_b_local_peak_proximity":0.98,"four_b_full_window_peak_proximity":0.98,"four_b_timing_verdict":"price_only_local_4B_watch_or_hard_4C","four_b_evidence_type":"price_only|regulatory_or_event_risk","four_c_protection_label":"hard_4c_success","trigger_outcome_label":"hard_4c_success_regulatory_rejection_protection","current_profile_verdict":"current_profile_4C_too_late","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window; corporate candidates are old 1998-2009 only","same_entry_group_id":"SEG_R7L75_C24_007390_NATURECELL_JOINTSTEM_REJECTION_4C_2023-04-10","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"R7L75_C24_298380_ABL_SANOFI_LICENSEOUT_HIGH_MAE_SUCCESS","trigger_id":"T_R7L75_C24_298380_ABL_SANOFI_LICENSEOUT_HIGH_MAE_SUCCESS","symbol":"298380","large_sector_id":"L7_BIO_HEALTHCARE_MEDICAL","canonical_archetype_id":"C24_BIO_TRIAL_DATA_EVENT_RISK","raw_component_scores_before":{"contract_score":12,"backlog_visibility_score":3,"margin_bridge_score":2,"revision_score":6,"relative_strength_score":9,"customer_quality_score":13,"policy_or_regulatory_score":8,"valuation_repricing_score":9,"execution_risk_score":-8,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0,"clinical_event_quality_score":8,"partner_quality_score":14,"endpoint_or_regulatory_clarity_score":3,"cash_runway_score":6},"weighted_score_before":86,"stage_label_before":"Stage3-Yellow/Green-borderline","raw_component_scores_after":{"contract_score":12,"backlog_visibility_score":3,"margin_bridge_score":2,"revision_score":6,"relative_strength_score":9,"customer_quality_score":13,"policy_or_regulatory_score":8,"valuation_repricing_score":9,"execution_risk_score":-8,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0,"clinical_event_quality_score":11,"partner_quality_score":16,"endpoint_or_regulatory_clarity_score":3,"cash_runway_score":6},"weighted_score_after":84,"stage_label_after":"Stage3-Yellow+4B/MAE-Watch","changed_components":["clinical_event_quality_score","partner_quality_score","endpoint_or_regulatory_clarity_score","execution_risk_score"],"component_delta_explanation":"C24 shadow separates partner-quality/platform license-out or clear clinical optionality from price-only clinical-event spikes and hard regulatory rejection. Positive promotion requires non-price clinical/regulatory bridge; rejection routes to hard 4C.","MFE_90D_pct":33.08,"MAE_90D_pct":-26.58,"score_return_alignment_label":"positive_but_high_mae_licenseout_success_requires_size_guard","current_profile_verdict":"current_profile_4B_too_late"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"R7L75_C24_310210_BORONOI_CLINICAL_OPTIONALITY_SUCCESS","trigger_id":"T_R7L75_C24_310210_BORONOI_CLINICAL_OPTIONALITY_SUCCESS","symbol":"310210","large_sector_id":"L7_BIO_HEALTHCARE_MEDICAL","canonical_archetype_id":"C24_BIO_TRIAL_DATA_EVENT_RISK","raw_component_scores_before":{"contract_score":1,"backlog_visibility_score":0,"margin_bridge_score":2,"revision_score":9,"relative_strength_score":14,"customer_quality_score":7,"policy_or_regulatory_score":12,"valuation_repricing_score":10,"execution_risk_score":-3,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0,"clinical_event_quality_score":14,"partner_quality_score":6,"endpoint_or_regulatory_clarity_score":9,"cash_runway_score":5},"weighted_score_before":82,"stage_label_before":"Stage3-Yellow","raw_component_scores_after":{"contract_score":1,"backlog_visibility_score":0,"margin_bridge_score":2,"revision_score":9,"relative_strength_score":14,"customer_quality_score":7,"policy_or_regulatory_score":12,"valuation_repricing_score":10,"execution_risk_score":-3,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0,"clinical_event_quality_score":17,"partner_quality_score":8,"endpoint_or_regulatory_clarity_score":9,"cash_runway_score":5},"weighted_score_after":90,"stage_label_after":"Stage3-Green+4B-Watch","changed_components":["clinical_event_quality_score","partner_quality_score","endpoint_or_regulatory_clarity_score","execution_risk_score"],"component_delta_explanation":"C24 shadow separates partner-quality/platform license-out or clear clinical optionality from price-only clinical-event spikes and hard regulatory rejection. Positive promotion requires non-price clinical/regulatory bridge; rejection routes to hard 4C.","MFE_90D_pct":147.62,"MAE_90D_pct":-4.86,"score_return_alignment_label":"positive_structural_success_low_mae_clinical_optional_rerating","current_profile_verdict":"current_profile_too_late"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"R7L75_C24_397030_APRILBIO_EVENT_SPIKE_FAILED_RERATING","trigger_id":"T_R7L75_C24_397030_APRILBIO_EVENT_SPIKE_FAILED_RERATING","symbol":"397030","large_sector_id":"L7_BIO_HEALTHCARE_MEDICAL","canonical_archetype_id":"C24_BIO_TRIAL_DATA_EVENT_RISK","raw_component_scores_before":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":0,"revision_score":4,"relative_strength_score":11,"customer_quality_score":4,"policy_or_regulatory_score":9,"valuation_repricing_score":9,"execution_risk_score":-10,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0,"clinical_event_quality_score":5,"partner_quality_score":3,"endpoint_or_regulatory_clarity_score":4,"cash_runway_score":1},"weighted_score_before":78,"stage_label_before":"Stage3-Yellow false-promotion risk","raw_component_scores_after":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":0,"revision_score":4,"relative_strength_score":11,"customer_quality_score":4,"policy_or_regulatory_score":9,"valuation_repricing_score":9,"execution_risk_score":-10,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0,"clinical_event_quality_score":0,"partner_quality_score":3,"endpoint_or_regulatory_clarity_score":-2,"cash_runway_score":1},"weighted_score_after":62,"stage_label_after":"Stage2-Watch/4B-Guard","changed_components":["clinical_event_quality_score","partner_quality_score","endpoint_or_regulatory_clarity_score","execution_risk_score"],"component_delta_explanation":"C24 shadow separates partner-quality/platform license-out or clear clinical optionality from price-only clinical-event spikes and hard regulatory rejection. Positive promotion requires non-price clinical/regulatory bridge; rejection routes to hard 4C.","MFE_90D_pct":33.02,"MAE_90D_pct":-25.27,"score_return_alignment_label":"event_spike_failed_rerating_high_mae_counterexample","current_profile_verdict":"current_profile_false_positive"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"R7L75_C24_007390_NATURECELL_JOINTSTEM_REJECTION_4C","trigger_id":"T_R7L75_C24_007390_NATURECELL_JOINTSTEM_REJECTION_4C","symbol":"007390","large_sector_id":"L7_BIO_HEALTHCARE_MEDICAL","canonical_archetype_id":"C24_BIO_TRIAL_DATA_EVENT_RISK","raw_component_scores_before":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":0,"revision_score":-6,"relative_strength_score":-5,"customer_quality_score":0,"policy_or_regulatory_score":-18,"valuation_repricing_score":-4,"execution_risk_score":-15,"legal_or_contract_risk_score":-12,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0,"clinical_event_quality_score":-18,"partner_quality_score":0,"endpoint_or_regulatory_clarity_score":-18,"cash_runway_score":-4},"weighted_score_before":70,"stage_label_before":"Stage2/3 false-positive if rejection risk not routed","raw_component_scores_after":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":0,"revision_score":-6,"relative_strength_score":-5,"customer_quality_score":0,"policy_or_regulatory_score":-18,"valuation_repricing_score":-4,"execution_risk_score":-15,"legal_or_contract_risk_score":-12,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0,"clinical_event_quality_score":-23,"partner_quality_score":0,"endpoint_or_regulatory_clarity_score":-24,"cash_runway_score":-4},"weighted_score_after":32,"stage_label_after":"Stage4C-ThesisBreak","changed_components":["clinical_event_quality_score","partner_quality_score","endpoint_or_regulatory_clarity_score","execution_risk_score"],"component_delta_explanation":"C24 shadow separates partner-quality/platform license-out or clear clinical optionality from price-only clinical-event spikes and hard regulatory rejection. Positive promotion requires non-price clinical/regulatory bridge; rejection routes to hard 4C.","MFE_90D_pct":5.04,"MAE_90D_pct":-41.95,"score_return_alignment_label":"hard_4c_success_regulatory_rejection_protection","current_profile_verdict":"current_profile_4C_too_late"}
{"row_type":"residual_contribution","round":"R7","loop":"75","scheduled_round":"R7","scheduled_loop":"75","round_schedule_status":"valid","round_sector_consistency":"pass","large_sector_id":"L7_BIO_HEALTHCARE_MEDICAL","canonical_archetype_id":"C24_BIO_TRIAL_DATA_EVENT_RISK","new_independent_case_count":4,"reused_case_count":0,"new_symbol_count":4,"same_archetype_new_symbol_count":4,"same_archetype_new_trigger_family_count":4,"new_trigger_family_count":4,"positive_case_count":2,"counterexample_count":2,"current_profile_error_count":3,"tested_existing_calibrated_axes":["stage2_actionable_evidence_bonus","price_only_blowoff_blocks_positive_stage","full_4b_requires_non_price_evidence","hard_4c_thesis_break_routes_to_4c"],"residual_error_types_found":["clinical_event_spike_false_positive","high_mae_licenseout_success_needs_overlay","regulatory_rejection_4c_too_late","clinical_optionality_too_late"],"loop_contribution_label":"canonical_archetype_rule_candidate","do_not_propose_new_weight_delta":false,"diversity_score_summary":"new_symbols=4; new_trigger_families=4; counterexamples=2; residual_errors=3; wrong_round_penalty=0"}
{"row_type":"narrative_only","case_id":"R7L75_C24_141080_LIGACHEM_JNJ_LICENSEOUT_BLOCKED_CA","symbol":"141080","company_name":"리가켐바이오","large_sector_id":"L7_BIO_HEALTHCARE_MEDICAL","canonical_archetype_id":"C24_BIO_TRIAL_DATA_EVENT_RISK","reason":"license-out event is useful narrative evidence, but stock-web profile flags a 2024-04-23 corporate-action candidate inside the 180D forward window from late-2023/early-2024 trigger, so it is not used for weight calibration.","price_source":"Songdaiki/stock-web","usage":"not_weight_calibration","calibration_usable":false,"calibration_block_reasons":["corporate_action_contaminated_180D_window"],"do_not_count_as_new_case":true}
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
completed_round = R7
completed_loop = 75
next_round = R8
next_loop = 75
round_schedule_status = valid
round_sector_consistency = pass
```

## 28. Source Notes

Stock-Web manifest and profile checks were read from `Songdaiki/stock-web`: manifest max_date `2026-02-20`, `price_adjustment_status=raw_unadjusted_marcap`, calibration shard root `atlas/ohlcv_tradable_by_symbol_year`. Case-level price rows were selected from the listed tradable shards; raw shards were not used for weight calibration. Evidence sources are recorded as historical public disclosure/news/IR proxies and should be URL-verified during the later batch implementation phase.

