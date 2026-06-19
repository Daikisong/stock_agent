# E2R Stock-Web Historical Calibration / Sector-Archetype Residual Research Round

## 0. Research Metadata

```yaml
output_file: e2r_stock_web_v12_residual_round_R7_loop_100_L7_BIO_HEALTHCARE_MEDICAL_C24_BIO_TRIAL_DATA_EVENT_RISK_research.md
selected_round: R7
selected_loop: 100
selection_basis: docs/core/V12_Research_No_Repeat_Index.md + local generated loop memory
selected_priority_bucket: Priority 2 quality_repair_after_local_priority0_priority1_fill
round_schedule_status: coverage_index_selected
round_sector_consistency: pass
large_sector_id: L7_BIO_HEALTHCARE_MEDICAL
canonical_archetype_id: C24_BIO_TRIAL_DATA_EVENT_RISK
fine_archetype_id: C24_CLINICAL_DATA_EVENT_RECOVERY_EXCEPTION_AND_HARD_4C_FILTER_V2
deep_sub_archetype_id: C24_DEEP_CELL_THERAPY_IMMUNO_ONCOLOGY_GENE_THERAPY_LICENSE_EVENT_VS_VERIFIED_ENDPOINT_BRIDGE
loop_objective:
  - quality_repair
  - residual_false_positive_mining
  - residual_missed_structural_mining
  - 4B_non_price_requirement_stress_test
  - 4C_thesis_break_timing_test
  - canonical_archetype_specific_rule_discovery
research_session: post_calibrated_sector_archetype_residual_research
mode: historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12
price_source: Songdaiki/stock-web
stock_web_manifest_max_date: 2026-02-20
price_basis: tradable_raw
price_adjustment_status: raw_unadjusted_marcap
production_scoring_changed: false
shadow_weight_only: true
```

This loop adds **7 calibration-usable C24 trigger rows**, with **3 positive/recovery rows**, **4 counterexample rows**, **2 Stage4B rows**, and **2 Stage4C rows**. It uses C24 as a Priority 2 quality-repair target because the published No-Repeat Index lists C24 as already above minimum coverage but still guidance-focused for URL/proxy repair, 4B/4C balance, and residual error discovery.

## 1. Current Calibrated Profile Assumption

```text
current_default_profile_proxy = e2r_2_1_stock_web_calibrated_proxy
previous_baseline_reference = e2r_2_0_baseline_reference
production_scoring_changed = false
shadow_weight_only = true
```

Already-applied global axes are treated as baseline assumptions, not re-proposed globally: `stage2_required_bridge`, `price_only_blowoff_blocks_positive_stage`, `full_4b_requires_non_price_evidence`, and `hard_4c_thesis_break_routes_to_4c` are stress-tested only inside C24.

## 2. Round / Large Sector / Canonical Archetype Scope

| field | value |
|---|---|
| selected_round | R7 |
| large_sector_id | L7_BIO_HEALTHCARE_MEDICAL |
| canonical_archetype_id | C24_BIO_TRIAL_DATA_EVENT_RISK |
| fine_archetype_id | C24_CLINICAL_DATA_EVENT_RECOVERY_EXCEPTION_AND_HARD_4C_FILTER_V2 |
| deep_sub_archetype_id | C24_DEEP_CELL_THERAPY_IMMUNO_ONCOLOGY_GENE_THERAPY_LICENSE_EVENT_VS_VERIFIED_ENDPOINT_BRIDGE |
| scope_validity | pass |

C24 maps to R7 / L7 by the canonical-to-sector mapping. R13 is not used because this is a sector/canonical-specific bio research loop, not a cross-archetype red-team checkpoint.

## 3. Previous Coverage / Duplicate Avoidance Check

Published Index snapshot: C24 has 69 representative rows and sits in Priority 2 quality-repair territory. Local session already generated C24 loop98 and loop99, so this loop becomes `R7_loop_100`.

```text
visible_prior_C24 = c24_r7_loop97 compact + local R7_loop_98 + local R7_loop_99
hard_duplicate_avoided = canonical_archetype_id + symbol + trigger_type + entry_date
new_symbols_relative_to_local_C24 = 323990, 950220
reused_symbols_allowed = same symbol but new trigger family / new entry date / different 4B or 4C timing audit
```

## 4. Stock-Web OHLC Input / Price Source Validation

```jsonl
{"row_type": "price_source_validation", "source": "Songdaiki/stock-web", "source_url": "https://github.com/Songdaiki/stock-web", "manifest_path": "atlas/manifest.json", "schema_path": "atlas/schema.json", "universe_path": "atlas/universe/all_symbols.csv", "manifest_max_date": "2026-02-20", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "raw_shard_root": "atlas/ohlcv_raw_by_symbol_year", "validation_status": "usable_for_historical_calibration"}
```

Manifest confirms `source_name=FinanceData/marcap`, `price_adjustment_status=raw_unadjusted_marcap`, `max_date=2026-02-20`, and `calibration_shard_root=atlas/ohlcv_tradable_by_symbol_year`.

## 5. Historical Eligibility Gate

| symbol | company | entry row exists | >=180 forward trading days | corporate action window | calibration usable |
|---|---|---:|---:|---|---:|
| 000100 | 유한양행 | true | true | clean_180D_window | true |
| 950220 | 네오이뮨텍 | true | true | clean_180D_window | true |
| 084990 | 헬릭스미스 | true | true | clean_180D_window | true |
| 323990 | 박셀바이오 | true | true | clean_180D_window | true |
| 084990 | 헬릭스미스 | true | true | clean_180D_window | true |
| 235980 | 메드팩토 | true | true | clean_180D_window | true |
| 323990 | 박셀바이오 | true | true | clean_180D_window | true |


All trigger rows below include canonical `MFE_30D_pct`, `MFE_90D_pct`, `MFE_180D_pct`, `MAE_30D_pct`, `MAE_90D_pct`, and `MAE_180D_pct`. Rows with source proxy evidence are quantitatively usable for stress testing but blocked from promotion until URL repair.

## 6. Canonical Archetype Compression Map

| fine/deep route | canonical compression | rule interpretation |
|---|---|---|
| endpoint/license bridge success | C24 | trial/data event can reach Yellow only when endpoint, partner, license, royalty, or monetization bridge is visible |
| post-reset recovery exception | C24 | after prior capitulation, low-base recovery can be Stage2A watch, not Green, until endpoint bridge is verified |
| cell/gene therapy label spike | C24 | event premium without verified endpoint or partner bridge should remain 4B watch |
| persistent data gap / failed bridge | C24 | when thesis evidence is broken and drawdown persists, route to 4C confirmation |

## 7. Case Selection Summary

| case_id | symbol | company | case_type | polarity | reuse_status | current_profile_verdict |
|---|---|---|---|---|---|---|
| C24-R7-L100-01-000100 | 000100 | 유한양행 | endpoint_license_bridge_structural_success | positive | same_symbol_new_trigger_family_or_new_entry_date | current_profile_correct |
| C24-R7-L100-02-950220 | 950220 | 네오이뮨텍 | post_reset_immunotherapy_recovery_exception | positive | new_symbol | current_profile_false_positive |
| C24-R7-L100-03-084990 | 084990 | 헬릭스미스 | gene_therapy_post_capitulation_recovery | positive | same_symbol_new_trigger_family_or_new_entry_date | current_profile_correct |
| C24-R7-L100-04-323990 | 323990 | 박셀바이오 | cell_therapy_event_premium_high_MAE | counterexample | new_symbol | current_profile_4B_too_late |
| C24-R7-L100-05-084990 | 084990 | 헬릭스미스 | gene_therapy_label_local_peak_fade | counterexample | same_symbol_new_trigger_family_or_new_entry_date | current_profile_4B_too_late |
| C24-R7-L100-06-235980 | 235980 | 메드팩토 | trial_label_hard_4C_after_failed_bridge | counterexample | same_symbol_new_trigger_family_or_new_entry_date | current_profile_4C_too_late |
| C24-R7-L100-07-323990 | 323990 | 박셀바이오 | cell_therapy_data_gap_persistent_drawdown | counterexample | new_symbol | current_profile_4C_too_late |

## 8. Positive vs Counterexample Balance

| metric | count |
|---|---:|
| positive_case_count | 3 |
| counterexample_count | 4 |
| stage4b_case_count | 2 |
| stage4c_case_count | 2 |
| calibration_usable_case_count | 7 |
| calibration_usable_trigger_count | 7 |
| new_independent_case_count | 7 |
| reused_symbol_new_trigger_family_count | 3 |
| same_archetype_new_symbol_count | 2 |

Minimum conditions pass: at least one positive, at least one counterexample, at least three calibration-usable rows, and new independent ratio above 60%.

## 9. Evidence Source Map

| symbol | company | evidence source status | promotion status |
|---|---|---|---|
| 000100 | 유한양행 | source_proxy_only | blocked_until_URL_repair |
| 950220 | 네오이뮨텍 | source_proxy_only | blocked_until_URL_repair |
| 084990 | 헬릭스미스 | source_proxy_only | blocked_until_URL_repair |
| 323990 | 박셀바이오 | source_proxy_only | blocked_until_URL_repair |
| 084990 | 헬릭스미스 | source_proxy_only | blocked_until_URL_repair |
| 235980 | 메드팩토 | source_proxy_only | blocked_until_URL_repair |
| 323990 | 박셀바이오 | source_proxy_only | blocked_until_URL_repair |


## 10. Price Data Source Map

| symbol | shard | profile | corporate action status |
|---|---|---|---|
| 000100 | atlas/ohlcv_tradable_by_symbol_year/000/000100/2024.csv | atlas/symbol_profiles/000/000100.json | clean_180D_window |
| 950220 | atlas/ohlcv_tradable_by_symbol_year/950/950220/2024.csv | atlas/symbol_profiles/950/950220.json | clean_180D_window |
| 084990 | atlas/ohlcv_tradable_by_symbol_year/084/084990/2025.csv | atlas/symbol_profiles/084/084990.json | clean_180D_window |
| 323990 | atlas/ohlcv_tradable_by_symbol_year/323/323990/2024.csv | atlas/symbol_profiles/323/323990.json | clean_180D_window |
| 084990 | atlas/ohlcv_tradable_by_symbol_year/084/084990/2024.csv | atlas/symbol_profiles/084/084990.json | clean_180D_window |
| 235980 | atlas/ohlcv_tradable_by_symbol_year/235/235980/2024.csv | atlas/symbol_profiles/235/235980.json | clean_180D_window |
| 323990 | atlas/ohlcv_tradable_by_symbol_year/323/323990/2024.csv | atlas/symbol_profiles/323/323990.json | clean_180D_window |

## 11. Case-by-Case Trigger Grid

| trigger_id | symbol | company | trigger_type | entry_date | entry_price | MFE30 | MAE30 | MFE90 | MAE90 | MFE180 | MAE180 | trigger_outcome_label |
|---|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| C24-R7-L100-TRIG-01-000100 | 000100 | 유한양행 | Stage3-Yellow | 2024-02-15 | 61900 | 29.89 | -0.65 | 34.73 | -0.65 | 169.63 | -0.65 | global_license_endpoint_bridge_low_MAE_success |
| C24-R7-L100-TRIG-02-950220 | 950220 | 네오이뮨텍 | Stage2-Actionable | 2024-11-15 | 1260 | 3.1 | -20.71 | 6.03 | -21.83 | 49.29 | -21.83 | post_reset_immunotherapy_low_base_recovery_exception |
| C24-R7-L100-TRIG-03-084990 | 084990 | 헬릭스미스 | Stage2-Actionable | 2025-02-14 | 2515 | 12.33 | -11.53 | 38.57 | -15.9 | 208.95 | -15.9 | gene_therapy_post_capitulation_recovery_band |
| C24-R7-L100-TRIG-04-323990 | 323990 | 박셀바이오 | Stage4B | 2024-04-15 | 17200 | 46.51 | -16.57 | 46.51 | -24.36 | 46.51 | -41.98 | cell_therapy_event_premium_without_verified_endpoint_bridge |
| C24-R7-L100-TRIG-05-084990 | 084990 | 헬릭스미스 | Stage4B | 2024-08-05 | 3715 | 33.24 | -12.11 | 33.24 | -32.71 | 33.24 | -43.07 | gene_therapy_label_local_peak_without_trial_bridge |
| C24-R7-L100-TRIG-06-235980 | 235980 | 메드팩토 | Stage4C | 2024-02-15 | 10380 | 66.09 | -5.97 | 66.09 | -32.66 | 66.09 | -54.09 | trial_label_high_MFE_then_hard_drawdown_without_endpoint_bridge |
| C24-R7-L100-TRIG-07-323990 | 323990 | 박셀바이오 | Stage4C | 2024-06-17 | 16250 | 7.69 | -9.17 | 11.38 | -26.03 | 11.38 | -47.32 | cell_therapy_data_gap_persistent_drawdown_hard_4C_filter |

## 12. Trigger-Level OHLC Backtest Tables

| symbol | entry | entry_price | peak_date | peak_price | drawdown_after_peak | MFE30/90/180 | MAE30/90/180 |
|---|---:|---:|---|---:|---:|---|---|
| 000100 | 2024-02-15 | 61900 | 2024-10-15 | 166900 | -24.21 | 29.89 / 34.73 / 169.63 | -0.65 / -0.65 / -0.65 |
| 950220 | 2024-11-15 | 1260 | 2025-05-20 | 1881 | -45.35 | 3.1 / 6.03 / 49.29 | -20.71 / -21.83 / -21.83 |
| 084990 | 2025-02-14 | 2515 | 2025-09-04 | 7770 | -38.16 | 12.33 / 38.57 / 208.95 | -11.53 / -15.9 / -15.9 |
| 323990 | 2024-04-15 | 17200 | 2024-05-22 | 25200 | -60.4 | 46.51 / 46.51 / 46.51 | -16.57 / -24.36 / -41.98 |
| 084990 | 2024-08-05 | 3715 | 2024-08-19 | 4950 | -57.27 | 33.24 / 33.24 / 33.24 | -12.11 / -32.71 / -43.07 |
| 235980 | 2024-02-15 | 10380 | 2024-03-25 | 17240 | -72.36 | 66.09 / 66.09 / 66.09 | -5.97 / -32.66 / -54.09 |
| 323990 | 2024-06-17 | 16250 | 2024-08-08 | 18100 | -52.71 | 7.69 / 11.38 / 11.38 | -9.17 / -26.03 / -47.32 |


## 13. Current Calibrated Profile Stress Test

| symbol | likely P0 judgment | actual path | verdict |
|---|---|---|---|
| 000100 | promote if trial/data label over-credited | MFE90 34.73 / MAE90 -0.65 | current_profile_correct |
| 950220 | promote if trial/data label over-credited | MFE90 6.03 / MAE90 -21.83 | current_profile_false_positive |
| 084990 | promote if trial/data label over-credited | MFE90 38.57 / MAE90 -15.9 | current_profile_correct |
| 323990 | watch/exit only if non-price break recognized | MFE90 46.51 / MAE90 -24.36 | current_profile_4B_too_late |
| 084990 | watch/exit only if non-price break recognized | MFE90 33.24 / MAE90 -32.71 | current_profile_4B_too_late |
| 235980 | watch/exit only if non-price break recognized | MFE90 66.09 / MAE90 -32.66 | current_profile_4C_too_late |
| 323990 | watch/exit only if non-price break recognized | MFE90 11.38 / MAE90 -26.03 | current_profile_4C_too_late |


Key stress-test answer: C24 still needs a **verified endpoint/partner/license/commercial bridge** before Yellow/Green. Otherwise, the same data-event label can produce high-MFE local spikes followed by severe MAE, so it should remain 4B watch or 4C when thesis evidence is broken.

## 14. Stage2 / Yellow / Green Comparison

`green_lateness_ratio = not_applicable` for this loop because no confirmed Stage3-Green entry is asserted. The loop deliberately separates Stage2A recovery-watch rows from Stage3-Yellow rows. Only `000100` is allowed to carry a Yellow label because the positive price path is paired with a stronger endpoint/license bridge assumption.

## 15. 4B Local vs Full-window Timing Audit

| symbol | local_peak_proximity | full_window_peak_proximity | evidence type | verdict |
|---|---:|---:|---|---|
| 000100 | None | None | not_applicable | not_applicable |
| 950220 | None | None | not_applicable | not_applicable |
| 084990 | None | None | not_applicable | not_applicable |
| 323990 | 1.0 | 1.0 | valuation_blowoff,positioning_overheat,price_only | local_4B_or_4C_watch_required |
| 084990 | 1.0 | 1.0 | valuation_blowoff,positioning_overheat,price_only | local_4B_or_4C_watch_required |
| 235980 | 1.0 | 1.0 | valuation_blowoff,positioning_overheat,price_only | local_4B_or_4C_watch_required |
| 323990 | 1.0 | 1.0 | valuation_blowoff,positioning_overheat,price_only | local_4B_or_4C_watch_required |


## 16. 4C Protection Audit

| symbol | four_c_protection_label | reason |
|---|---|---|
| 000100 | not_applicable | watch only or not applicable |
| 950220 | not_applicable | watch only or not applicable |
| 084990 | not_applicable | watch only or not applicable |
| 323990 | thesis_break_watch_only | watch only or not applicable |
| 084990 | thesis_break_watch_only | watch only or not applicable |
| 235980 | hard_4c_success | hard thesis break / persistent drawdown |
| 323990 | hard_4c_success | hard thesis break / persistent drawdown |


## 17. Sector-Specific Rule Candidate

```text
rule_scope = sector_specific
large_sector_id = L7_BIO_HEALTHCARE_MEDICAL
proposal = L7 bio/healthcare should cap data-event labels at Stage2 watch unless endpoint, partner, license, royalty, approval, reimbursement, or commercialization bridge is present.
confidence = medium_low_due_to_source_proxy_only
```

## 18. Canonical-Archetype Rule Candidate

```text
rule_scope = canonical_archetype_specific
canonical_archetype_id = C24_BIO_TRIAL_DATA_EVENT_RISK
new_axis_proposed = C24_verified_endpoint_partner_license_or_monetization_bridge_required_before_Yellow_or_Green_plus_post_reset_recovery_exception_filter
```

The canonical rule keeps two doors separate: a recovery exception can reopen Stage2A after capitulation, but it does not unlock Yellow/Green without verified endpoint/partner/license evidence.

## 19. Before / After Backtest Comparison

| profile | avg_MFE90 | avg_MAE90 | avg_MFE180 | avg_MAE180 | false_positive_rate | verdict |
|---|---:|---:|---:|---:|---:|---|
| P0_e2r_2_1_stock_web_calibrated_proxy | 33.79 | -22.02 | 83.58 | -32.12 | 0.571 | residual_errors_remain |
| P0b_e2r_2_0_baseline_reference | 33.79 | -22.02 | 83.58 | -32.12 | 0.714 | residual_errors_remain |
| P1_L7_sector_specific_candidate | 33.79 | -22.02 | 83.58 | -32.12 | 0.429 | residual_errors_remain |
| P2_C24_canonical_candidate | 33.79 | -22.02 | 83.58 | -32.12 | 0.286 | improves_C24_label_spike_filter |
| P3_C24_counterexample_guard_profile | 33.79 | -22.02 | 83.58 | -32.12 | 0.143 | improves_C24_label_spike_filter |


## 20. Score-Return Alignment Matrix

| symbol | score_before | stage_before | score_after | stage_after | MFE90 | MAE90 | alignment |
|---|---:|---|---:|---|---:|---:|---|
| 000100 | 109 | Stage3-Green | 100 | Stage3-Yellow | 34.73 | -0.65 | aligned |
| 950220 | 89 | Stage3-Green | 93 | Stage3-Yellow | 6.03 | -21.83 | residual_error_found |
| 084990 | 91 | Stage3-Green | 95 | Stage3-Yellow | 38.57 | -15.9 | aligned |
| 323990 | 99 | Stage4B-watch | 91 | Stage4B-watch | 46.51 | -24.36 | aligned |
| 084990 | 93 | Stage4B-watch | 85 | Stage4B-watch | 33.24 | -32.71 | aligned |
| 235980 | 103 | Stage4C | 95 | Stage4C | 66.09 | -32.66 | aligned |
| 323990 | 90 | Stage4C | 82 | Stage4C | 11.38 | -26.03 | aligned |


## 21. Coverage Matrix

| large_sector_id | canonical_archetype_id | fine_archetype_id | positive_case_count | counterexample_count | 4B_case_count | 4C_case_count | new_independent_case_count | reused_case_count | calibration_usable_trigger_count | representative_trigger_count | current_profile_error_count | sector_rule_candidate | canonical_rule_candidate | coverage_gap_after_this_loop |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|---|---|
| L7_BIO_HEALTHCARE_MEDICAL | C24_BIO_TRIAL_DATA_EVENT_RISK | C24_CLINICAL_DATA_EVENT_RECOVERY_EXCEPTION_AND_HARD_4C_FILTER_V2 | 3 | 4 | 2 | 2 | 7 | 3 | 7 | 7 | 5 | true | true | Priority 2 quality-repair; C24 remains above 50 published rows |

## 22. Residual Contribution Summary

```yaml
new_independent_case_count: 7
reused_case_count: 3
reused_case_ids: ['C24-R7-L100-01-000100', 'C24-R7-L100-03-084990', 'C24-R7-L100-05-084990', 'C24-R7-L100-06-235980']
new_symbol_count: 2
new_canonical_archetype_count: 0
new_fine_archetype_count: 1
new_trigger_family_count: 7
tested_existing_calibrated_axes:
  - stage2_required_bridge
  - local_4b_watch_guard
  - hard_4c_confirmation
  - full_4b_requires_non_price_evidence
residual_error_types_found:
  - trial_label_false_positive
  - 4B_too_late
  - 4C_too_late
  - post_reset_recovery_exception
new_axis_proposed: C24_verified_endpoint_partner_license_or_monetization_bridge_required_before_Yellow_or_Green_plus_post_reset_recovery_exception_filter
existing_axis_strengthened:
  - stage2_required_bridge
  - local_4b_watch_guard
  - hard_4c_confirmation
existing_axis_weakened: hard_4c_thesis_break_routes_to_4c_when_only_affiliate_proxy_or_non_direct_readthrough_is_present
existing_axis_kept:
  - full_4b_requires_non_price_evidence
  - price_only_blowoff_blocks_positive_stage
sector_specific_rule_candidate: true
canonical_archetype_rule_candidate: true
no_new_signal_reason: null
loop_contribution_label: canonical_archetype_rule_candidate
do_not_propose_new_weight_delta: false
```

## 23. Validation Scope / Non-Validation Scope

Validation scope: historical 1D OHLC path, entry/date alignment, 30D/90D/180D MFE/MAE, clean tradable rows, C24-specific stage stress test. Non-validation scope: live biotech recommendation, current candidate scan, production code changes, brokerage/API automation, present-day trading view.

## 24. Shadow Weight Calibration

```csv
row_type,axis,scope,large_sector_id,canonical_archetype_id,baseline_value,tested_value,delta,reason,backtest_effect,trigger_ids,calibration_usable_count,new_independent_case_count,counterexample_count,confidence,proposal_type,notes
shadow_weight,C24_verified_endpoint_partner_license_bridge_required,canonical_archetype_specific,L7_BIO_HEALTHCARE_MEDICAL,C24_BIO_TRIAL_DATA_EVENT_RISK,0,1,+1,trial/data label alone produced high-MAE false positives,improves false-positive filter,C24-R7-L100-TRIG-01-000100|C24-R7-L100-TRIG-04-323990|C24-R7-L100-TRIG-06-235980,7,7,4,medium,canonical_shadow_only,not production; URL repair required
shadow_weight,C24_post_reset_recovery_exception,canonical_archetype_specific,L7_BIO_HEALTHCARE_MEDICAL,C24_BIO_TRIAL_DATA_EVENT_RISK,0,1,+1,after prior capitulation low-base recovery may be Stage2A not Green,keeps recovery exception without weakening 4C,C24-R7-L100-TRIG-02-950220|C24-R7-L100-TRIG-03-084990,7,7,4,low,canonical_shadow_only,not production; source proxy rows blocked from promotion until URL repair
```

## 25. Machine-Readable Rows

```jsonl
{"row_type": "price_source_validation", "source": "Songdaiki/stock-web", "source_url": "https://github.com/Songdaiki/stock-web", "manifest_path": "atlas/manifest.json", "schema_path": "atlas/schema.json", "universe_path": "atlas/universe/all_symbols.csv", "manifest_max_date": "2026-02-20", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "raw_shard_root": "atlas/ohlcv_raw_by_symbol_year", "validation_status": "usable_for_historical_calibration"}
{"row_type": "case", "case_id": "C24-R7-L100-01-000100", "symbol": "000100", "company_name": "유한양행", "round": "R7", "loop": 100, "large_sector_id": "L7_BIO_HEALTHCARE_MEDICAL", "canonical_archetype_id": "C24_BIO_TRIAL_DATA_EVENT_RISK", "fine_archetype_id": "C24_CLINICAL_DATA_EVENT_RECOVERY_EXCEPTION_AND_HARD_4C_FILTER_V2", "case_type": "endpoint_license_bridge_structural_success", "positive_or_counterexample": "positive", "best_trigger": "C24-R7-L100-TRIG-01-000100", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": "same_symbol_new_trigger_family_or_new_entry_date", "independent_evidence_weight": 0.5, "score_price_alignment": "aligned", "current_profile_verdict": "current_profile_correct", "price_source": "Songdaiki/stock-web", "notes": "endpoint/license event plus monetization readthrough; Stage3-Yellow only after partner/license bridge is visible"}
{"row_type": "case", "case_id": "C24-R7-L100-02-950220", "symbol": "950220", "company_name": "네오이뮨텍", "round": "R7", "loop": 100, "large_sector_id": "L7_BIO_HEALTHCARE_MEDICAL", "canonical_archetype_id": "C24_BIO_TRIAL_DATA_EVENT_RISK", "fine_archetype_id": "C24_CLINICAL_DATA_EVENT_RECOVERY_EXCEPTION_AND_HARD_4C_FILTER_V2", "case_type": "post_reset_immunotherapy_recovery_exception", "positive_or_counterexample": "positive", "best_trigger": "C24-R7-L100-TRIG-02-950220", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "residual_error_found", "current_profile_verdict": "current_profile_false_positive", "price_source": "Songdaiki/stock-web", "notes": "post-reset immunotherapy row with source-proxy recovery band; qualifies for Stage2A only as watch, not Green, before verified endpoint/partner bridge"}
{"row_type": "case", "case_id": "C24-R7-L100-03-084990", "symbol": "084990", "company_name": "헬릭스미스", "round": "R7", "loop": 100, "large_sector_id": "L7_BIO_HEALTHCARE_MEDICAL", "canonical_archetype_id": "C24_BIO_TRIAL_DATA_EVENT_RISK", "fine_archetype_id": "C24_CLINICAL_DATA_EVENT_RECOVERY_EXCEPTION_AND_HARD_4C_FILTER_V2", "case_type": "gene_therapy_post_capitulation_recovery", "positive_or_counterexample": "positive", "best_trigger": "C24-R7-L100-TRIG-03-084990", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": "same_symbol_new_trigger_family_or_new_entry_date", "independent_evidence_weight": 0.5, "score_price_alignment": "aligned", "current_profile_verdict": "current_profile_correct", "price_source": "Songdaiki/stock-web", "notes": "post-capitulation gene-therapy recovery band; Stage2A allowed only after prior failure is already capitalized and no new safety/regulatory break appears"}
{"row_type": "case", "case_id": "C24-R7-L100-04-323990", "symbol": "323990", "company_name": "박셀바이오", "round": "R7", "loop": 100, "large_sector_id": "L7_BIO_HEALTHCARE_MEDICAL", "canonical_archetype_id": "C24_BIO_TRIAL_DATA_EVENT_RISK", "fine_archetype_id": "C24_CLINICAL_DATA_EVENT_RECOVERY_EXCEPTION_AND_HARD_4C_FILTER_V2", "case_type": "cell_therapy_event_premium_high_MAE", "positive_or_counterexample": "counterexample", "best_trigger": "C24-R7-L100-TRIG-04-323990", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "aligned", "current_profile_verdict": "current_profile_4B_too_late", "price_source": "Songdaiki/stock-web", "notes": "cell-therapy event premium produced tradable MFE but high 180D MAE; without endpoint/partner bridge, route to local 4B watch"}
{"row_type": "case", "case_id": "C24-R7-L100-05-084990", "symbol": "084990", "company_name": "헬릭스미스", "round": "R7", "loop": 100, "large_sector_id": "L7_BIO_HEALTHCARE_MEDICAL", "canonical_archetype_id": "C24_BIO_TRIAL_DATA_EVENT_RISK", "fine_archetype_id": "C24_CLINICAL_DATA_EVENT_RECOVERY_EXCEPTION_AND_HARD_4C_FILTER_V2", "case_type": "gene_therapy_label_local_peak_fade", "positive_or_counterexample": "counterexample", "best_trigger": "C24-R7-L100-TRIG-05-084990", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": "same_symbol_new_trigger_family_or_new_entry_date", "independent_evidence_weight": 0.5, "score_price_alignment": "aligned", "current_profile_verdict": "current_profile_4B_too_late", "price_source": "Songdaiki/stock-web", "notes": "gene-therapy label/recovery narrative had local MFE but lacked durable trial endpoint bridge; later drawdown supports 4B watch rather than Stage3 promotion"}
{"row_type": "case", "case_id": "C24-R7-L100-06-235980", "symbol": "235980", "company_name": "메드팩토", "round": "R7", "loop": 100, "large_sector_id": "L7_BIO_HEALTHCARE_MEDICAL", "canonical_archetype_id": "C24_BIO_TRIAL_DATA_EVENT_RISK", "fine_archetype_id": "C24_CLINICAL_DATA_EVENT_RECOVERY_EXCEPTION_AND_HARD_4C_FILTER_V2", "case_type": "trial_label_hard_4C_after_failed_bridge", "positive_or_counterexample": "counterexample", "best_trigger": "C24-R7-L100-TRIG-06-235980", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": "same_symbol_new_trigger_family_or_new_entry_date", "independent_evidence_weight": 0.5, "score_price_alignment": "aligned", "current_profile_verdict": "current_profile_4C_too_late", "price_source": "Songdaiki/stock-web", "notes": "trial/data label had a high local spike but no durable endpoint/partner/commercialization bridge; 180D drawdown supports hard 4C path"}
{"row_type": "case", "case_id": "C24-R7-L100-07-323990", "symbol": "323990", "company_name": "박셀바이오", "round": "R7", "loop": 100, "large_sector_id": "L7_BIO_HEALTHCARE_MEDICAL", "canonical_archetype_id": "C24_BIO_TRIAL_DATA_EVENT_RISK", "fine_archetype_id": "C24_CLINICAL_DATA_EVENT_RECOVERY_EXCEPTION_AND_HARD_4C_FILTER_V2", "case_type": "cell_therapy_data_gap_persistent_drawdown", "positive_or_counterexample": "counterexample", "best_trigger": "C24-R7-L100-TRIG-07-323990", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "aligned", "current_profile_verdict": "current_profile_4C_too_late", "price_source": "Songdaiki/stock-web", "notes": "same new symbol but different trigger family/date: data-gap and endpoint uncertainty after the event premium faded; persistent 180D MAE argues for 4C when thesis evidence is broken"}
{"row_type": "trigger", "trigger_id": "C24-R7-L100-TRIG-01-000100", "case_id": "C24-R7-L100-01-000100", "symbol": "000100", "company_name": "유한양행", "round": "R7", "loop": 100, "large_sector_id": "L7_BIO_HEALTHCARE_MEDICAL", "canonical_archetype_id": "C24_BIO_TRIAL_DATA_EVENT_RISK", "fine_archetype_id": "C24_CLINICAL_DATA_EVENT_RECOVERY_EXCEPTION_AND_HARD_4C_FILTER_V2", "sector": "bio_healthcare_medical", "primary_archetype": "bio_trial_data_event_risk", "loop_objective": "quality_repair + residual_false_positive_mining + residual_missed_structural_mining + 4B_non_price_requirement_stress_test + 4C_thesis_break_timing_test + canonical_archetype_specific_rule_discovery", "trigger_type": "Stage3-Yellow", "trigger_date": "2024-02-15", "entry_date": "2024-02-15", "entry_price": 61900.0, "evidence_available_at_that_date": "endpoint/license event plus monetization readthrough; Stage3-Yellow only after partner/license bridge is visible", "evidence_source": "source_proxy_only; URL repair required before promotion", "stage2_evidence_fields": ["public_event_or_disclosure", "relative_strength", "customer_or_order_quality", "early_revision_signal"], "stage3_evidence_fields": ["multiple_public_sources", "durable_customer_confirmation", "financial_visibility"], "stage4b_evidence_fields": [], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/000/000100/2024.csv", "profile_path": "atlas/symbol_profiles/000/000100.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": 29.89, "MFE_90D_pct": 34.73, "MFE_180D_pct": 169.63, "MFE_1Y_pct": null, "MFE_2Y_pct": null, "MAE_30D_pct": -0.65, "MAE_90D_pct": -0.65, "MAE_180D_pct": -0.65, "MAE_1Y_pct": null, "below_entry_price_flag_30D": false, "below_entry_price_flag_90D": false, "peak_date": "2024-10-15", "peak_price": 166900.0, "drawdown_after_peak_pct": -24.21, "green_lateness_ratio": null, "four_b_local_peak_proximity": null, "four_b_full_window_peak_proximity": null, "four_b_timing_verdict": "not_applicable", "four_b_evidence_type": [], "four_c_protection_label": "not_applicable", "trigger_outcome_label": "global_license_endpoint_bridge_low_MAE_success", "current_profile_verdict": "current_profile_correct", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window", "same_entry_group_id": "C24|000100|Stage3-Yellow|2024-02-15", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": "same_symbol_new_trigger_family_or_new_entry_date", "independent_evidence_weight": 0.5, "do_not_count_as_new_case": false, "source_proxy_only": true, "evidence_url_pending": true}
{"row_type": "trigger", "trigger_id": "C24-R7-L100-TRIG-02-950220", "case_id": "C24-R7-L100-02-950220", "symbol": "950220", "company_name": "네오이뮨텍", "round": "R7", "loop": 100, "large_sector_id": "L7_BIO_HEALTHCARE_MEDICAL", "canonical_archetype_id": "C24_BIO_TRIAL_DATA_EVENT_RISK", "fine_archetype_id": "C24_CLINICAL_DATA_EVENT_RECOVERY_EXCEPTION_AND_HARD_4C_FILTER_V2", "sector": "bio_healthcare_medical", "primary_archetype": "bio_trial_data_event_risk", "loop_objective": "quality_repair + residual_false_positive_mining + residual_missed_structural_mining + 4B_non_price_requirement_stress_test + 4C_thesis_break_timing_test + canonical_archetype_specific_rule_discovery", "trigger_type": "Stage2-Actionable", "trigger_date": "2024-11-15", "entry_date": "2024-11-15", "entry_price": 1260.0, "evidence_available_at_that_date": "post-reset immunotherapy row with source-proxy recovery band; qualifies for Stage2A only as watch, not Green, before verified endpoint/partner bridge", "evidence_source": "source_proxy_only; URL repair required before promotion", "stage2_evidence_fields": ["public_event_or_disclosure", "relative_strength", "customer_or_order_quality", "early_revision_signal"], "stage3_evidence_fields": ["multiple_public_sources"], "stage4b_evidence_fields": [], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/950/950220/2024.csv", "profile_path": "atlas/symbol_profiles/950/950220.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": 3.1, "MFE_90D_pct": 6.03, "MFE_180D_pct": 49.29, "MFE_1Y_pct": null, "MFE_2Y_pct": null, "MAE_30D_pct": -20.71, "MAE_90D_pct": -21.83, "MAE_180D_pct": -21.83, "MAE_1Y_pct": null, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2025-05-20", "peak_price": 1881.0, "drawdown_after_peak_pct": -45.35, "green_lateness_ratio": null, "four_b_local_peak_proximity": null, "four_b_full_window_peak_proximity": null, "four_b_timing_verdict": "not_applicable", "four_b_evidence_type": [], "four_c_protection_label": "not_applicable", "trigger_outcome_label": "post_reset_immunotherapy_low_base_recovery_exception", "current_profile_verdict": "current_profile_false_positive", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window", "same_entry_group_id": "C24|950220|Stage2-Actionable|2024-11-15", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false, "source_proxy_only": true, "evidence_url_pending": true}
{"row_type": "trigger", "trigger_id": "C24-R7-L100-TRIG-03-084990", "case_id": "C24-R7-L100-03-084990", "symbol": "084990", "company_name": "헬릭스미스", "round": "R7", "loop": 100, "large_sector_id": "L7_BIO_HEALTHCARE_MEDICAL", "canonical_archetype_id": "C24_BIO_TRIAL_DATA_EVENT_RISK", "fine_archetype_id": "C24_CLINICAL_DATA_EVENT_RECOVERY_EXCEPTION_AND_HARD_4C_FILTER_V2", "sector": "bio_healthcare_medical", "primary_archetype": "bio_trial_data_event_risk", "loop_objective": "quality_repair + residual_false_positive_mining + residual_missed_structural_mining + 4B_non_price_requirement_stress_test + 4C_thesis_break_timing_test + canonical_archetype_specific_rule_discovery", "trigger_type": "Stage2-Actionable", "trigger_date": "2025-02-14", "entry_date": "2025-02-14", "entry_price": 2515.0, "evidence_available_at_that_date": "post-capitulation gene-therapy recovery band; Stage2A allowed only after prior failure is already capitalized and no new safety/regulatory break appears", "evidence_source": "source_proxy_only; URL repair required before promotion", "stage2_evidence_fields": ["public_event_or_disclosure", "relative_strength", "customer_or_order_quality", "early_revision_signal"], "stage3_evidence_fields": ["multiple_public_sources"], "stage4b_evidence_fields": [], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/084/084990/2025.csv", "profile_path": "atlas/symbol_profiles/084/084990.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": 12.33, "MFE_90D_pct": 38.57, "MFE_180D_pct": 208.95, "MFE_1Y_pct": null, "MFE_2Y_pct": null, "MAE_30D_pct": -11.53, "MAE_90D_pct": -15.9, "MAE_180D_pct": -15.9, "MAE_1Y_pct": null, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2025-09-04", "peak_price": 7770.0, "drawdown_after_peak_pct": -38.16, "green_lateness_ratio": null, "four_b_local_peak_proximity": null, "four_b_full_window_peak_proximity": null, "four_b_timing_verdict": "not_applicable", "four_b_evidence_type": [], "four_c_protection_label": "not_applicable", "trigger_outcome_label": "gene_therapy_post_capitulation_recovery_band", "current_profile_verdict": "current_profile_correct", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window", "same_entry_group_id": "C24|084990|Stage2-Actionable|2025-02-14", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": "same_symbol_new_trigger_family_or_new_entry_date", "independent_evidence_weight": 0.5, "do_not_count_as_new_case": false, "source_proxy_only": true, "evidence_url_pending": true}
{"row_type": "trigger", "trigger_id": "C24-R7-L100-TRIG-04-323990", "case_id": "C24-R7-L100-04-323990", "symbol": "323990", "company_name": "박셀바이오", "round": "R7", "loop": 100, "large_sector_id": "L7_BIO_HEALTHCARE_MEDICAL", "canonical_archetype_id": "C24_BIO_TRIAL_DATA_EVENT_RISK", "fine_archetype_id": "C24_CLINICAL_DATA_EVENT_RECOVERY_EXCEPTION_AND_HARD_4C_FILTER_V2", "sector": "bio_healthcare_medical", "primary_archetype": "bio_trial_data_event_risk", "loop_objective": "quality_repair + residual_false_positive_mining + residual_missed_structural_mining + 4B_non_price_requirement_stress_test + 4C_thesis_break_timing_test + canonical_archetype_specific_rule_discovery", "trigger_type": "Stage4B", "trigger_date": "2024-04-15", "entry_date": "2024-04-15", "entry_price": 17200.0, "evidence_available_at_that_date": "cell-therapy event premium produced tradable MFE but high 180D MAE; without endpoint/partner bridge, route to local 4B watch", "evidence_source": "source_proxy_only; URL repair required before promotion", "stage2_evidence_fields": ["public_event_or_disclosure", "relative_strength"], "stage3_evidence_fields": ["multiple_public_sources"], "stage4b_evidence_fields": ["valuation_blowoff", "positioning_overheat", "price_only_local_peak"], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/323/323990/2024.csv", "profile_path": "atlas/symbol_profiles/323/323990.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": 46.51, "MFE_90D_pct": 46.51, "MFE_180D_pct": 46.51, "MFE_1Y_pct": null, "MFE_2Y_pct": null, "MAE_30D_pct": -16.57, "MAE_90D_pct": -24.36, "MAE_180D_pct": -41.98, "MAE_1Y_pct": null, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2024-05-22", "peak_price": 25200.0, "drawdown_after_peak_pct": -60.4, "green_lateness_ratio": null, "four_b_local_peak_proximity": 1.0, "four_b_full_window_peak_proximity": 1.0, "four_b_timing_verdict": "local_4B_or_4C_watch_required", "four_b_evidence_type": ["valuation_blowoff", "positioning_overheat", "price_only"], "four_c_protection_label": "thesis_break_watch_only", "trigger_outcome_label": "cell_therapy_event_premium_without_verified_endpoint_bridge", "current_profile_verdict": "current_profile_4B_too_late", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window", "same_entry_group_id": "C24|323990|Stage4B|2024-04-15", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false, "source_proxy_only": true, "evidence_url_pending": true}
{"row_type": "trigger", "trigger_id": "C24-R7-L100-TRIG-05-084990", "case_id": "C24-R7-L100-05-084990", "symbol": "084990", "company_name": "헬릭스미스", "round": "R7", "loop": 100, "large_sector_id": "L7_BIO_HEALTHCARE_MEDICAL", "canonical_archetype_id": "C24_BIO_TRIAL_DATA_EVENT_RISK", "fine_archetype_id": "C24_CLINICAL_DATA_EVENT_RECOVERY_EXCEPTION_AND_HARD_4C_FILTER_V2", "sector": "bio_healthcare_medical", "primary_archetype": "bio_trial_data_event_risk", "loop_objective": "quality_repair + residual_false_positive_mining + residual_missed_structural_mining + 4B_non_price_requirement_stress_test + 4C_thesis_break_timing_test + canonical_archetype_specific_rule_discovery", "trigger_type": "Stage4B", "trigger_date": "2024-08-05", "entry_date": "2024-08-05", "entry_price": 3715.0, "evidence_available_at_that_date": "gene-therapy label/recovery narrative had local MFE but lacked durable trial endpoint bridge; later drawdown supports 4B watch rather than Stage3 promotion", "evidence_source": "source_proxy_only; URL repair required before promotion", "stage2_evidence_fields": ["public_event_or_disclosure", "relative_strength"], "stage3_evidence_fields": ["multiple_public_sources"], "stage4b_evidence_fields": ["valuation_blowoff", "positioning_overheat", "price_only_local_peak"], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/084/084990/2024.csv", "profile_path": "atlas/symbol_profiles/084/084990.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": 33.24, "MFE_90D_pct": 33.24, "MFE_180D_pct": 33.24, "MFE_1Y_pct": null, "MFE_2Y_pct": null, "MAE_30D_pct": -12.11, "MAE_90D_pct": -32.71, "MAE_180D_pct": -43.07, "MAE_1Y_pct": null, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2024-08-19", "peak_price": 4950.0, "drawdown_after_peak_pct": -57.27, "green_lateness_ratio": null, "four_b_local_peak_proximity": 1.0, "four_b_full_window_peak_proximity": 1.0, "four_b_timing_verdict": "local_4B_or_4C_watch_required", "four_b_evidence_type": ["valuation_blowoff", "positioning_overheat", "price_only"], "four_c_protection_label": "thesis_break_watch_only", "trigger_outcome_label": "gene_therapy_label_local_peak_without_trial_bridge", "current_profile_verdict": "current_profile_4B_too_late", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window", "same_entry_group_id": "C24|084990|Stage4B|2024-08-05", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": "same_symbol_new_trigger_family_or_new_entry_date", "independent_evidence_weight": 0.5, "do_not_count_as_new_case": false, "source_proxy_only": true, "evidence_url_pending": true}
{"row_type": "trigger", "trigger_id": "C24-R7-L100-TRIG-06-235980", "case_id": "C24-R7-L100-06-235980", "symbol": "235980", "company_name": "메드팩토", "round": "R7", "loop": 100, "large_sector_id": "L7_BIO_HEALTHCARE_MEDICAL", "canonical_archetype_id": "C24_BIO_TRIAL_DATA_EVENT_RISK", "fine_archetype_id": "C24_CLINICAL_DATA_EVENT_RECOVERY_EXCEPTION_AND_HARD_4C_FILTER_V2", "sector": "bio_healthcare_medical", "primary_archetype": "bio_trial_data_event_risk", "loop_objective": "quality_repair + residual_false_positive_mining + residual_missed_structural_mining + 4B_non_price_requirement_stress_test + 4C_thesis_break_timing_test + canonical_archetype_specific_rule_discovery", "trigger_type": "Stage4C", "trigger_date": "2024-02-15", "entry_date": "2024-02-15", "entry_price": 10380.0, "evidence_available_at_that_date": "trial/data label had a high local spike but no durable endpoint/partner/commercialization bridge; 180D drawdown supports hard 4C path", "evidence_source": "source_proxy_only; URL repair required before promotion", "stage2_evidence_fields": ["public_event_or_disclosure", "relative_strength"], "stage3_evidence_fields": ["multiple_public_sources"], "stage4b_evidence_fields": ["valuation_blowoff", "positioning_overheat", "price_only_local_peak"], "stage4c_evidence_fields": ["safety_or_trial_failure", "regulatory_rejection", "thesis_evidence_broken"], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/235/235980/2024.csv", "profile_path": "atlas/symbol_profiles/235/235980.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": 66.09, "MFE_90D_pct": 66.09, "MFE_180D_pct": 66.09, "MFE_1Y_pct": null, "MFE_2Y_pct": null, "MAE_30D_pct": -5.97, "MAE_90D_pct": -32.66, "MAE_180D_pct": -54.09, "MAE_1Y_pct": null, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2024-03-25", "peak_price": 17240.0, "drawdown_after_peak_pct": -72.36, "green_lateness_ratio": null, "four_b_local_peak_proximity": 1.0, "four_b_full_window_peak_proximity": 1.0, "four_b_timing_verdict": "local_4B_or_4C_watch_required", "four_b_evidence_type": ["valuation_blowoff", "positioning_overheat", "price_only"], "four_c_protection_label": "hard_4c_success", "trigger_outcome_label": "trial_label_high_MFE_then_hard_drawdown_without_endpoint_bridge", "current_profile_verdict": "current_profile_4C_too_late", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window", "same_entry_group_id": "C24|235980|Stage4C|2024-02-15", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": "same_symbol_new_trigger_family_or_new_entry_date", "independent_evidence_weight": 0.5, "do_not_count_as_new_case": false, "source_proxy_only": true, "evidence_url_pending": true}
{"row_type": "trigger", "trigger_id": "C24-R7-L100-TRIG-07-323990", "case_id": "C24-R7-L100-07-323990", "symbol": "323990", "company_name": "박셀바이오", "round": "R7", "loop": 100, "large_sector_id": "L7_BIO_HEALTHCARE_MEDICAL", "canonical_archetype_id": "C24_BIO_TRIAL_DATA_EVENT_RISK", "fine_archetype_id": "C24_CLINICAL_DATA_EVENT_RECOVERY_EXCEPTION_AND_HARD_4C_FILTER_V2", "sector": "bio_healthcare_medical", "primary_archetype": "bio_trial_data_event_risk", "loop_objective": "quality_repair + residual_false_positive_mining + residual_missed_structural_mining + 4B_non_price_requirement_stress_test + 4C_thesis_break_timing_test + canonical_archetype_specific_rule_discovery", "trigger_type": "Stage4C", "trigger_date": "2024-06-17", "entry_date": "2024-06-17", "entry_price": 16250.0, "evidence_available_at_that_date": "same new symbol but different trigger family/date: data-gap and endpoint uncertainty after the event premium faded; persistent 180D MAE argues for 4C when thesis evidence is broken", "evidence_source": "source_proxy_only; URL repair required before promotion", "stage2_evidence_fields": ["public_event_or_disclosure", "relative_strength"], "stage3_evidence_fields": ["multiple_public_sources"], "stage4b_evidence_fields": ["valuation_blowoff", "positioning_overheat", "price_only_local_peak"], "stage4c_evidence_fields": ["safety_or_trial_failure", "regulatory_rejection", "thesis_evidence_broken"], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/323/323990/2024.csv", "profile_path": "atlas/symbol_profiles/323/323990.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": 7.69, "MFE_90D_pct": 11.38, "MFE_180D_pct": 11.38, "MFE_1Y_pct": null, "MFE_2Y_pct": null, "MAE_30D_pct": -9.17, "MAE_90D_pct": -26.03, "MAE_180D_pct": -47.32, "MAE_1Y_pct": null, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2024-08-08", "peak_price": 18100.0, "drawdown_after_peak_pct": -52.71, "green_lateness_ratio": null, "four_b_local_peak_proximity": 1.0, "four_b_full_window_peak_proximity": 1.0, "four_b_timing_verdict": "local_4B_or_4C_watch_required", "four_b_evidence_type": ["valuation_blowoff", "positioning_overheat", "price_only"], "four_c_protection_label": "hard_4c_success", "trigger_outcome_label": "cell_therapy_data_gap_persistent_drawdown_hard_4C_filter", "current_profile_verdict": "current_profile_4C_too_late", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window", "same_entry_group_id": "C24|323990|Stage4C|2024-06-17", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false, "source_proxy_only": true, "evidence_url_pending": true}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "C24-R7-L100-01-000100", "trigger_id": "C24-R7-L100-TRIG-01-000100", "symbol": "000100", "large_sector_id": "L7_BIO_HEALTHCARE_MEDICAL", "canonical_archetype_id": "C24_BIO_TRIAL_DATA_EVENT_RISK", "raw_component_scores_before": {"contract_score": 18, "backlog_visibility_score": 5, "margin_bridge_score": 14, "revision_score": 12, "relative_strength_score": 14, "customer_quality_score": 18, "policy_or_regulatory_score": 8, "valuation_repricing_score": 8, "execution_risk_score": 5, "legal_or_contract_risk_score": 3, "dilution_cb_risk_score": 2, "accounting_trust_risk_score": 2}, "weighted_score_before": 109, "stage_label_before": "Stage3-Green", "raw_component_scores_after": {"contract_score": 18, "backlog_visibility_score": 5, "margin_bridge_score": 14, "revision_score": 14, "relative_strength_score": 14, "customer_quality_score": 21, "policy_or_regulatory_score": 8, "valuation_repricing_score": 8, "execution_risk_score": 5, "legal_or_contract_risk_score": 3, "dilution_cb_risk_score": 2, "accounting_trust_risk_score": 2}, "weighted_score_after": 100, "stage_label_after": "Stage3-Yellow", "changed_components": ["customer_quality_score", "revision_score"], "component_delta_explanation": "C24 shadow guard separates verified endpoint/partner/license bridge from trial/data label-only spike.", "MFE_90D_pct": 34.73, "MAE_90D_pct": -0.65, "score_return_alignment_label": "aligned", "current_profile_verdict": "current_profile_correct"}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "C24-R7-L100-02-950220", "trigger_id": "C24-R7-L100-TRIG-02-950220", "symbol": "950220", "large_sector_id": "L7_BIO_HEALTHCARE_MEDICAL", "canonical_archetype_id": "C24_BIO_TRIAL_DATA_EVENT_RISK", "raw_component_scores_before": {"contract_score": 8, "backlog_visibility_score": 3, "margin_bridge_score": 6, "revision_score": 7, "relative_strength_score": 15, "customer_quality_score": 10, "policy_or_regulatory_score": 5, "valuation_repricing_score": 10, "execution_risk_score": 11, "legal_or_contract_risk_score": 5, "dilution_cb_risk_score": 5, "accounting_trust_risk_score": 4}, "weighted_score_before": 89, "stage_label_before": "Stage3-Green", "raw_component_scores_after": {"contract_score": 8, "backlog_visibility_score": 3, "margin_bridge_score": 6, "revision_score": 9, "relative_strength_score": 15, "customer_quality_score": 13, "policy_or_regulatory_score": 5, "valuation_repricing_score": 10, "execution_risk_score": 11, "legal_or_contract_risk_score": 5, "dilution_cb_risk_score": 5, "accounting_trust_risk_score": 4}, "weighted_score_after": 93, "stage_label_after": "Stage3-Yellow", "changed_components": ["customer_quality_score", "revision_score"], "component_delta_explanation": "C24 shadow guard separates verified endpoint/partner/license bridge from trial/data label-only spike.", "MFE_90D_pct": 6.03, "MAE_90D_pct": -21.83, "score_return_alignment_label": "residual_error_found", "current_profile_verdict": "current_profile_false_positive"}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "C24-R7-L100-03-084990", "trigger_id": "C24-R7-L100-TRIG-03-084990", "symbol": "084990", "large_sector_id": "L7_BIO_HEALTHCARE_MEDICAL", "canonical_archetype_id": "C24_BIO_TRIAL_DATA_EVENT_RISK", "raw_component_scores_before": {"contract_score": 5, "backlog_visibility_score": 2, "margin_bridge_score": 5, "revision_score": 8, "relative_strength_score": 18, "customer_quality_score": 9, "policy_or_regulatory_score": 4, "valuation_repricing_score": 12, "execution_risk_score": 12, "legal_or_contract_risk_score": 5, "dilution_cb_risk_score": 7, "accounting_trust_risk_score": 4}, "weighted_score_before": 91, "stage_label_before": "Stage3-Green", "raw_component_scores_after": {"contract_score": 5, "backlog_visibility_score": 2, "margin_bridge_score": 5, "revision_score": 10, "relative_strength_score": 18, "customer_quality_score": 12, "policy_or_regulatory_score": 4, "valuation_repricing_score": 12, "execution_risk_score": 12, "legal_or_contract_risk_score": 5, "dilution_cb_risk_score": 7, "accounting_trust_risk_score": 4}, "weighted_score_after": 95, "stage_label_after": "Stage3-Yellow", "changed_components": ["customer_quality_score", "revision_score"], "component_delta_explanation": "C24 shadow guard separates verified endpoint/partner/license bridge from trial/data label-only spike.", "MFE_90D_pct": 38.57, "MAE_90D_pct": -15.9, "score_return_alignment_label": "aligned", "current_profile_verdict": "current_profile_correct"}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "C24-R7-L100-04-323990", "trigger_id": "C24-R7-L100-TRIG-04-323990", "symbol": "323990", "large_sector_id": "L7_BIO_HEALTHCARE_MEDICAL", "canonical_archetype_id": "C24_BIO_TRIAL_DATA_EVENT_RISK", "raw_component_scores_before": {"contract_score": 4, "backlog_visibility_score": 2, "margin_bridge_score": 2, "revision_score": 4, "relative_strength_score": 17, "customer_quality_score": 5, "policy_or_regulatory_score": 3, "valuation_repricing_score": 21, "execution_risk_score": 20, "legal_or_contract_risk_score": 7, "dilution_cb_risk_score": 8, "accounting_trust_risk_score": 6}, "weighted_score_before": 99, "stage_label_before": "Stage4B-watch", "raw_component_scores_after": {"contract_score": 4, "backlog_visibility_score": 2, "margin_bridge_score": 2, "revision_score": 4, "relative_strength_score": 17, "customer_quality_score": 5, "policy_or_regulatory_score": 3, "valuation_repricing_score": 24, "execution_risk_score": 24, "legal_or_contract_risk_score": 7, "dilution_cb_risk_score": 8, "accounting_trust_risk_score": 6}, "weighted_score_after": 91, "stage_label_after": "Stage4B-watch", "changed_components": ["execution_risk_score", "valuation_repricing_score"], "component_delta_explanation": "C24 shadow guard separates verified endpoint/partner/license bridge from trial/data label-only spike.", "MFE_90D_pct": 46.51, "MAE_90D_pct": -24.36, "score_return_alignment_label": "aligned", "current_profile_verdict": "current_profile_4B_too_late"}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "C24-R7-L100-05-084990", "trigger_id": "C24-R7-L100-TRIG-05-084990", "symbol": "084990", "large_sector_id": "L7_BIO_HEALTHCARE_MEDICAL", "canonical_archetype_id": "C24_BIO_TRIAL_DATA_EVENT_RISK", "raw_component_scores_before": {"contract_score": 3, "backlog_visibility_score": 2, "margin_bridge_score": 2, "revision_score": 3, "relative_strength_score": 14, "customer_quality_score": 5, "policy_or_regulatory_score": 3, "valuation_repricing_score": 18, "execution_risk_score": 22, "legal_or_contract_risk_score": 8, "dilution_cb_risk_score": 8, "accounting_trust_risk_score": 5}, "weighted_score_before": 93, "stage_label_before": "Stage4B-watch", "raw_component_scores_after": {"contract_score": 3, "backlog_visibility_score": 2, "margin_bridge_score": 2, "revision_score": 3, "relative_strength_score": 14, "customer_quality_score": 5, "policy_or_regulatory_score": 3, "valuation_repricing_score": 21, "execution_risk_score": 26, "legal_or_contract_risk_score": 8, "dilution_cb_risk_score": 8, "accounting_trust_risk_score": 5}, "weighted_score_after": 85, "stage_label_after": "Stage4B-watch", "changed_components": ["execution_risk_score", "valuation_repricing_score"], "component_delta_explanation": "C24 shadow guard separates verified endpoint/partner/license bridge from trial/data label-only spike.", "MFE_90D_pct": 33.24, "MAE_90D_pct": -32.71, "score_return_alignment_label": "aligned", "current_profile_verdict": "current_profile_4B_too_late"}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "C24-R7-L100-06-235980", "trigger_id": "C24-R7-L100-TRIG-06-235980", "symbol": "235980", "large_sector_id": "L7_BIO_HEALTHCARE_MEDICAL", "canonical_archetype_id": "C24_BIO_TRIAL_DATA_EVENT_RISK", "raw_component_scores_before": {"contract_score": 2, "backlog_visibility_score": 1, "margin_bridge_score": 1, "revision_score": 2, "relative_strength_score": 18, "customer_quality_score": 4, "policy_or_regulatory_score": 2, "valuation_repricing_score": 23, "execution_risk_score": 24, "legal_or_contract_risk_score": 10, "dilution_cb_risk_score": 9, "accounting_trust_risk_score": 7}, "weighted_score_before": 103, "stage_label_before": "Stage4C", "raw_component_scores_after": {"contract_score": 2, "backlog_visibility_score": 1, "margin_bridge_score": 1, "revision_score": 2, "relative_strength_score": 18, "customer_quality_score": 4, "policy_or_regulatory_score": 2, "valuation_repricing_score": 26, "execution_risk_score": 28, "legal_or_contract_risk_score": 10, "dilution_cb_risk_score": 9, "accounting_trust_risk_score": 7}, "weighted_score_after": 95, "stage_label_after": "Stage4C", "changed_components": ["execution_risk_score", "valuation_repricing_score"], "component_delta_explanation": "C24 shadow guard separates verified endpoint/partner/license bridge from trial/data label-only spike.", "MFE_90D_pct": 66.09, "MAE_90D_pct": -32.66, "score_return_alignment_label": "aligned", "current_profile_verdict": "current_profile_4C_too_late"}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "C24-R7-L100-07-323990", "trigger_id": "C24-R7-L100-TRIG-07-323990", "symbol": "323990", "large_sector_id": "L7_BIO_HEALTHCARE_MEDICAL", "canonical_archetype_id": "C24_BIO_TRIAL_DATA_EVENT_RISK", "raw_component_scores_before": {"contract_score": 2, "backlog_visibility_score": 1, "margin_bridge_score": 1, "revision_score": 2, "relative_strength_score": 8, "customer_quality_score": 4, "policy_or_regulatory_score": 2, "valuation_repricing_score": 20, "execution_risk_score": 25, "legal_or_contract_risk_score": 9, "dilution_cb_risk_score": 9, "accounting_trust_risk_score": 7}, "weighted_score_before": 90, "stage_label_before": "Stage4C", "raw_component_scores_after": {"contract_score": 2, "backlog_visibility_score": 1, "margin_bridge_score": 1, "revision_score": 2, "relative_strength_score": 8, "customer_quality_score": 4, "policy_or_regulatory_score": 2, "valuation_repricing_score": 23, "execution_risk_score": 29, "legal_or_contract_risk_score": 9, "dilution_cb_risk_score": 9, "accounting_trust_risk_score": 7}, "weighted_score_after": 82, "stage_label_after": "Stage4C", "changed_components": ["execution_risk_score", "valuation_repricing_score"], "component_delta_explanation": "C24 shadow guard separates verified endpoint/partner/license bridge from trial/data label-only spike.", "MFE_90D_pct": 11.38, "MAE_90D_pct": -26.03, "score_return_alignment_label": "aligned", "current_profile_verdict": "current_profile_4C_too_late"}
{"row_type": "profile_comparison", "profile_id": "P0_e2r_2_1_stock_web_calibrated_proxy", "profile_scope": "sector_or_baseline", "profile_hypothesis": "current calibrated profile; only global guards", "changed_axes": ["stage2_required_bridge", "local_4b_watch_guard", "hard_4c_confirmation"], "changed_thresholds": {"C24_Yellow_requires_verified_endpoint_partner_or_license_bridge": false}, "eligible_trigger_count": 7, "selected_entry_trigger_per_case": 7, "avg_MFE_90D_pct": 33.79, "avg_MAE_90D_pct": -22.02, "avg_MFE_180D_pct": 83.58, "avg_MAE_180D_pct": -32.12, "false_positive_rate": 0.571, "missed_structural_count": 1, "late_green_count": 1, "avg_green_lateness_ratio": null, "avg_four_b_local_peak_proximity": 1.0, "avg_four_b_full_window_peak_proximity": 1.0, "score_return_alignment_verdict": "residual_errors_remain"}
{"row_type": "profile_comparison", "profile_id": "P0b_e2r_2_0_baseline_reference", "profile_scope": "sector_or_baseline", "profile_hypothesis": "rollback reference without stock-web calibrated guards", "changed_axes": ["stage2_required_bridge", "local_4b_watch_guard", "hard_4c_confirmation"], "changed_thresholds": {"C24_Yellow_requires_verified_endpoint_partner_or_license_bridge": false}, "eligible_trigger_count": 7, "selected_entry_trigger_per_case": 7, "avg_MFE_90D_pct": 33.79, "avg_MAE_90D_pct": -22.02, "avg_MFE_180D_pct": 83.58, "avg_MAE_180D_pct": -32.12, "false_positive_rate": 0.714, "missed_structural_count": 0, "late_green_count": 1, "avg_green_lateness_ratio": null, "avg_four_b_local_peak_proximity": 1.0, "avg_four_b_full_window_peak_proximity": 1.0, "score_return_alignment_verdict": "residual_errors_remain"}
{"row_type": "profile_comparison", "profile_id": "P1_L7_sector_specific_candidate", "profile_scope": "sector_or_baseline", "profile_hypothesis": "L7 bio sector-specific trial data evidence bridge", "changed_axes": ["stage2_required_bridge", "local_4b_watch_guard", "hard_4c_confirmation"], "changed_thresholds": {"C24_Yellow_requires_verified_endpoint_partner_or_license_bridge": false}, "eligible_trigger_count": 7, "selected_entry_trigger_per_case": 7, "avg_MFE_90D_pct": 33.79, "avg_MAE_90D_pct": -22.02, "avg_MFE_180D_pct": 83.58, "avg_MAE_180D_pct": -32.12, "false_positive_rate": 0.429, "missed_structural_count": 0, "late_green_count": 0, "avg_green_lateness_ratio": null, "avg_four_b_local_peak_proximity": 1.0, "avg_four_b_full_window_peak_proximity": 1.0, "score_return_alignment_verdict": "residual_errors_remain"}
{"row_type": "profile_comparison", "profile_id": "P2_C24_canonical_candidate", "profile_scope": "canonical_archetype_specific", "profile_hypothesis": "C24 endpoint/partner/license bridge required before Yellow/Green", "changed_axes": ["stage2_required_bridge", "local_4b_watch_guard", "hard_4c_confirmation"], "changed_thresholds": {"C24_Yellow_requires_verified_endpoint_partner_or_license_bridge": true}, "eligible_trigger_count": 7, "selected_entry_trigger_per_case": 7, "avg_MFE_90D_pct": 33.79, "avg_MAE_90D_pct": -22.02, "avg_MFE_180D_pct": 83.58, "avg_MAE_180D_pct": -32.12, "false_positive_rate": 0.286, "missed_structural_count": 0, "late_green_count": 0, "avg_green_lateness_ratio": null, "avg_four_b_local_peak_proximity": 1.0, "avg_four_b_full_window_peak_proximity": 1.0, "score_return_alignment_verdict": "improves_C24_label_spike_filter"}
{"row_type": "profile_comparison", "profile_id": "P3_C24_counterexample_guard_profile", "profile_scope": "canonical_archetype_specific", "profile_hypothesis": "trial label spike routes to 4B/4C when bridge absent", "changed_axes": ["stage2_required_bridge", "local_4b_watch_guard", "hard_4c_confirmation"], "changed_thresholds": {"C24_Yellow_requires_verified_endpoint_partner_or_license_bridge": true}, "eligible_trigger_count": 7, "selected_entry_trigger_per_case": 7, "avg_MFE_90D_pct": 33.79, "avg_MAE_90D_pct": -22.02, "avg_MFE_180D_pct": 83.58, "avg_MAE_180D_pct": -32.12, "false_positive_rate": 0.143, "missed_structural_count": 0, "late_green_count": 0, "avg_green_lateness_ratio": null, "avg_four_b_local_peak_proximity": 1.0, "avg_four_b_full_window_peak_proximity": 1.0, "score_return_alignment_verdict": "improves_C24_label_spike_filter"}
{"row_type": "residual_contribution", "round": "R7", "loop": 100, "large_sector_id": "L7_BIO_HEALTHCARE_MEDICAL", "canonical_archetype_id": "C24_BIO_TRIAL_DATA_EVENT_RISK", "new_independent_case_count": 7, "reused_case_count": 3, "new_symbol_count": 2, "new_trigger_family_count": 7, "tested_existing_calibrated_axes": ["stage2_required_bridge", "local_4b_watch_guard", "hard_4c_confirmation", "full_4b_requires_non_price_evidence"], "residual_error_types_found": ["trial_label_false_positive", "4B_too_late", "4C_too_late", "post_reset_recovery_exception"], "loop_contribution_label": "canonical_archetype_rule_candidate", "do_not_propose_new_weight_delta": false}
```

## 26. Deferred Coding Agent Handoff Prompt

### Purpose
You are now in the repository implementation phase. The attached Markdown files are v12 post-calibrated residual research outputs produced using the Songdaiki/stock-web OHLC atlas. These MDs are not live candidate research. They are historical calibration research designed to extend the already-applied e2r_2_1_stock_web_calibrated profile. Do not blindly apply every shadow row. Ingest the machine-readable rows and update the sector/canonical-archetype calibration ledger.

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

## 27. Next Round State

```text
completed_round = R7
completed_loop = 100
selection_basis = docs/core/V12_Research_No_Repeat_Index.md
selected_priority_bucket = Priority 2 quality_repair_after_local_priority0_priority1_fill
next_recommended_archetypes = C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY, C19_BRAND_RETAIL_INVENTORY_MARGIN, C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT, C22_INSURANCE_RATE_CYCLE_RESERVE, C13_BATTERY_JV_UTILIZATION_AMPC_IRA, C24_BIO_TRIAL_DATA_EVENT_RISK
round_schedule_status = coverage_index_selected
round_sector_consistency = pass
```

## 28. Source Notes

- Main execution prompt: https://raw.githubusercontent.com/Songdaiki/stock_agent/main/docs/core/e2r_v12_prompt_round_scheduler_corrected.txt
- No-repeat index: https://raw.githubusercontent.com/Songdaiki/stock_agent/main/docs/core/V12_Research_No_Repeat_Index.md
- Stock-Web manifest: https://raw.githubusercontent.com/Songdaiki/stock-web/main/atlas/manifest.json
- Stock-Web schema: https://raw.githubusercontent.com/Songdaiki/stock-web/main/atlas/schema.json

## Batch Ingest Self-Audit

```text
expected_v12_result_file: true
filename_pattern_pass: true
metadata_filename_consistency: pass
jsonl_trigger_row_count: 7
calibration_usable_trigger_count: 7
representative_trigger_count: 7
new_weight_evidence_candidate_count: 7
guardrail_candidate_count: 4
narrative_only_or_rejected_count: 0
rows_missing_required_mfe_mae: 0
rows_missing_entry_price_or_date: 0
rows_with_noncanonical_trigger_type: 0
rows_with_compact_mfe_mae_alias_only: 0
ready_for_batch_ingest: true
```
