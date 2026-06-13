# E2R Stock-Web v12 Residual Research — R7 loop 164 — C24 Bio Trial Data Event Risk

```text
completed_round = R7
completed_loop = 164
selection_basis = docs/core/V12_Research_No_Repeat_Index.md
selected_priority_bucket = Priority 2 quality-repair after session-aware P0/P1/thin-P2 clearing
round_schedule_status = coverage_index_selected_not_sequential
round_sector_consistency = pass
large_sector_id = L7_BIO_HEALTHCARE_MEDICAL
canonical_archetype_id = C24_BIO_TRIAL_DATA_EVENT_RISK
fine_archetype_id = mixed_c24_autoimmune_oncology_phase_data_value_capture_leaf_set
output_filename = e2r_stock_web_v12_residual_round_R7_loop_164_L7_BIO_HEALTHCARE_MEDICAL_C24_BIO_TRIAL_DATA_EVENT_RISK_research.md
```

## 1. Scope guard

This research follows the E2R Historical Calibration Prompt v12. It is not a live candidate scan, not a broker/API task, not a `stock_agent` code patch, and not a production scoring change. The only output is this standalone historical calibration Markdown file using actual `Songdaiki/stock-web` 1D OHLCV rows.

```text
production_scoring_changed = false
shadow_weight_only = true
stock_agent_code_patch_allowed = false
stock_agent_live_scan_allowed = false
must_use_actual_stock_web_1D_OHLC = true
must_include_complete_30_90_180_mfe_mae_in_every_trigger_row = true
```

## 2. Coverage-index selection rationale

The original No-Repeat Index places `C24_BIO_TRIAL_DATA_EVENT_RISK` in Priority 2 with 69 representative rows. After this session's P0/P1 clearing and the thin-P2 repairs for C08, C19, C25, C13, C22, and C03, C24 remains a natural quality-repair target because the existing corpus is still prone to two opposite errors:

1. over-promoting early Phase 1/2 vocabulary without partner, financing, endpoint durability, or value-capture bridge;
2. under-promoting late-stage or externally validated data that should become Stage2-Actionable before the later C23 approval/commercialization event.

```text
index_baseline_coverage_before = C24 rows 69
index_baseline_coverage_after_if_accepted = C24 rows 76
new_independent_case_count = 7
reused_case_count = 0
same_archetype_new_symbol_count = 6
same_archetype_new_trigger_family_count = 7
narrative_only_blocked_case_count = 2
loop_objective = coverage_gap_fill|counterexample_mining|4B_non_price_requirement_stress_test|4C_thesis_break_timing_test|canonical_archetype_compression|sector_specific_rule_discovery
```

## 3. Price source validation

```text
price_source = Songdaiki/stock-web
source_basis = FinanceData/marcap transformed into assistant-readable symbol-year CSV shards
price_basis = tradable_raw
price_adjustment_status = raw_unadjusted_marcap
calibration_shard_root = atlas/ohlcv_tradable_by_symbol_year
stock_web_manifest_max_date = 2026-02-20
entry_price_rule = entry_date close column c
MFE_MAE_rule = max high / min low after entry_date through 30/90/180 trading rows
```

Profile/corporate-action audit:

```text
009420 HanAll Biopharma: profile active_like; corporate-action candidate dates 1996-12-24, 2006-05-10, 2006-07-19, 2015-08-18; no overlap with 2023-12/2024-03 180D windows.
321550 TiumBio: profile active_like; corporate_action_candidate_count = 0.
298380 ABL Bio: profile active_like; corporate_action_candidate_count = 0.
358570 GI Innovation: profile active_like; corporate-action candidates 2024-01-19, 2024-02-15, 2025-04-10; selected 2024-06-03 180D window ends before 2025-04-10.
115180 Qurient: profile active_like; corporate-action candidates 2022-10-07, 2024-01-04, 2024-01-15; selected 2024-05 trigger occurs after those dates.
039200 Oscotec: profile active_like; last corporate-action candidate 2022-11-30; no overlap with selected 2024-01 trigger window.
288330 Bridge Biotherapeutics: corporate-action candidate dates contaminate the 2024-07 and 2025-04 trial rows; kept as narrative-only audit, not calibration usable.
```

## 4. Evidence and trigger summary

| case | ticker | company | label | trigger | entry | MFE30/MAE30 | MFE90/MAE90 | MFE180/MAE180 | residual interpretation |
|---|---:|---|---|---|---:|---:|---:|---:|---|
| C24_009420_20231221_BATOCLIMAB_GRAVES_P2_INITIAL_DATA | 009420 | HanAll Biopharma | positive_with_high_beta_guard | Stage2-Actionable / 2023-12-21 | 2023-12-21 / 34,700 | 34.73/-17.72 | 34.73/-17.72 | 34.73/-17.87 | Clinical POC data mattered, but the entry carried a meaningful -17% drawdown; C24 should permit Stage2-Actionable while attaching a high-beta biotech trial-risk guard. |
| C24_009420_20240321_HANALL_FY2023_PIPELINE_UPDATE_LATE_FOLLOWUP | 009420 | HanAll Biopharma | counterexample_watch_late_followup | Stage2-Watch / 2024-03-21 | 2024-03-21 / 38,250 | 8.63/-17.78 | 8.63/-21.83 | 35.95/-25.49 | The same POC evidence resurfaced, but entry quality was worse: shallow early MFE, -21% 90D MAE, then delayed recovery. Follow-up reports need lower weight than first data release. |
| C24_321550_20240508_MERIGOLIX_ENDOMETRIOSIS_P2A_TOPLINE | 321550 | TiumBio | counterexample_positive_data_no_financing_or_partner_bridge | Stage2-FalsePositive / 2024-05-08 | 2024-05-08 / 7,640 | 4.71/-26.57 | 4.71/-29.97 | 4.71/-56.28 | The data headline was clinically positive, but the price path collapsed. C24 needs a financing/partner/next-trial bridge before treating small-cap Phase 2a data as Actionable. |
| C24_298380_20240603_ABL503_ASCO_P1_RESPONSE_DATA | 298380 | ABL Bio | positive_trial_data_platform_revaluation | Stage2-Actionable / 2024-06-03 | 2024-06-03 / 24,050 | 28.9/-11.85 | 80.04/-11.85 | 96.47/-11.85 | This was a strong C24 positive: ASCO clinical response data plus platform read-through produced large MFE with a manageable -12% MAE. |
| C24_358570_20240603_GI102_ASCO_P1_2A_PRELIMINARY_DATA | 358570 | GI Innovation | positive_with_high_MAE_guard | Stage2-Watch / 2024-06-03 | 2024-06-03 / 11,700 | 9.4/-15.21 | 39.66/-27.26 | 47.44/-35.98 | The row produced >40% 180D MFE but also suffered a -36% 180D MAE. Early IO data should be Watch until partner/cash or randomized expansion bridge is visible. |
| C24_115180_20240529_Q901_ASCO_FIRST_IN_HUMAN_DATA | 115180 | Qurient | positive_with_drawdown_guard | Stage2-Watch / 2024-05-29 | 2024-05-29 / 4,065 | 5.29/-20.91 | 23.99/-21.28 | 56.7/-21.28 | The path supports early Watch, not clean Actionable: 180D MFE was strong but 30D/90D MAE breached -20%. |
| C24_039200_20240119_LASER301_LAZERTINIB_PUBLISHED_DATA | 039200 | Oscotec | positive_late_stage_trial_data_royalty_readthrough | Stage2-Actionable / 2024-01-19 | 2024-01-19 / 20,100 | 28.61/-7.76 | 92.04/-7.76 | 128.11/-7.76 | This is the clean late-stage C24 positive: trial data were already de-risked enough to justify Stage2-Actionable before later regulatory/commercial C23 triggers. |

## 5. Evidence URL table

| ticker | case | evidence source | evidence family |
|---:|---|---|---|
| 009420 | C24_009420_20231221_BATOCLIMAB_GRAVES_P2_INITIAL_DATA | https://www.immunovant.com/investors/news-events/press-releases/detail/58/immunovant-reports-positive-initial-phase-2-results-for | partner_reported_phase2_data / response_rate / licensed_asset / clinical_POC |
| 009420 | C24_009420_20240321_HANALL_FY2023_PIPELINE_UPDATE_LATE_FOLLOWUP | https://hanall.com/board_view.php?bo_table=press&idx=88 | annual_results_pipeline_update / same_data_reiteration / late_entry |
| 321550 | C24_321550_20240508_MERIGOLIX_ENDOMETRIOSIS_P2A_TOPLINE | https://www.prnewswire.com/news-releases/tiumbio-announces-positive-topline-data-from-phase-2a-trial-of-merigolix-in-patients-with-moderate-to-severe-endometriosis-associated-pain-302139490.html | positive_phase2a_topline / small_sample / no_partner_or_cash_bridge / female_health |
| 298380 | C24_298380_20240603_ABL503_ASCO_P1_RESPONSE_DATA | https://www.ablbio.com/en/company/news/36 | ASCO_phase1_response_data / complete_response_partial_responses / platform_validation |
| 358570 | C24_358570_20240603_GI102_ASCO_P1_2A_PRELIMINARY_DATA | https://www.asco.org/abstracts-presentations/233987 | ASCO_preliminary_phase1_2a_data / orphan_designation / combination_optionality / cashburn_risk |
| 115180 | C24_115180_20240529_Q901_ASCO_FIRST_IN_HUMAN_DATA | https://ascopubs.org/doi/10.1200/JCO.2024.42.16_suppl.3078 | ASCO_first_in_human_data / biomarker_signal / early_dose_escalation / partnering_gap |
| 039200 | C24_039200_20240119_LASER301_LAZERTINIB_PUBLISHED_DATA | https://pubmed.ncbi.nlm.nih.gov/37379502/ | phase3_laser301_data / PFS_benefit / royalty_derivative / late_stage_validation |
| 288330 | C24_288330_20240730_BBT877_ENROLLMENT_COMPLETE_BLOCKED_BY_CORP_ACTION | https://www.prnewswire.com/news-releases/bridge-biotherapeutics-announces-completion-of-enrollment-in-the-phase-2a-clinical-study-of-bbt-877-for-the-treatment-of-idiopathic-pulmonary-fibrosis-302208799.html | corporate_action_contaminated_180D_window |
| 288330 | C24_288330_20250415_BBT877_P2_FAILURE_BLOCKED_BY_CORP_ACTION_BUT_THESIS_BREAK_CONFIRMED | https://www.koreabiomed.com/news/articleView.html?idxno=27276 | corporate_action_contaminated_180D_window |

## 6. Residual diagnosis

C24 is not one signal; it is a ladder. A trial event only becomes investable when the baton is handed from clinical signal to value capture. In this loop, clinical vocabulary alone was insufficient for TiumBio, where positive Phase 2a topline data failed to protect the stock path without a partner/financing/next-trial bridge. In contrast, ABL Bio and Oscotec show that response data or late-stage Phase 3 data with platform/royalty read-through can reprice before an approval event.

```text
residual_false_positive = early Phase 1/2 or small-sample data treated like late-stage externally validated data
residual_too_late = late-stage/partner-validated trial data delayed until C23 approval/commercialization
residual_over_4C = trial enrollment/follow-up vocabulary used as hard 4C without endpoint failure
```

## 7. Proposed shadow rule candidate

```text
rule_id = C24_TRIAL_DATA_STAGE_AND_VALUE_CAPTURE_GATE_V1
large_sector_id = L7_BIO_HEALTHCARE_MEDICAL
canonical_archetype_id = C24_BIO_TRIAL_DATA_EVENT_RISK
production_scoring_changed = false
shadow_weight_only = true
```

Candidate rule:

```text
IF trial event is Phase 1 / early Phase 2 biomarker or dose-escalation data
AND no named partner, cash runway, next-trial funding, randomized endpoint, or out-licensing path exists
THEN cap at Stage2-Watch and attach high-MAE biotech trial-risk guard.

IF trial event is late-stage data, partner-reported data, externally validated ASCO/JCO data, or response data with platform read-through
AND there is a royalty, licensed asset, partner, or platform value-capture bridge
THEN allow Stage2-Actionable before later C23 approval/commercialization.

IF endpoint failure is confirmed
THEN allow 4C thesis-break only if the price window is not corporate-action contaminated and the failure is the asset's key value bridge.
```

## 8. Machine-readable trigger rows JSONL

```jsonl
{"MAE_180D_pct": -17.87, "MAE_30D_pct": -17.72, "MAE_90D_pct": -17.72, "MFE_180D_pct": 34.73, "MFE_30D_pct": 34.73, "MFE_90D_pct": 34.73, "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "calibration_usable": true, "canonical_archetype_id": "C24_BIO_TRIAL_DATA_EVENT_RISK", "case_id": "C24_009420_20231221_BATOCLIMAB_GRAVES_P2_INITIAL_DATA", "company_name": "HanAll Biopharma", "component_score_breakdown": {"biotech_trial_risk_penalty": -3, "bottleneck_pricing_power": 6, "capital_allocation": 3, "earnings_visibility": 12, "eps_fcf_explosion": 10, "information_confidence": 24, "market_mispricing": 14, "valuation_rerating": 10}, "corporate_action_window_status": "clean_180D_or_no_candidate_overlap", "current_profile_error": false, "dedupe_key": "C24_BIO_TRIAL_DATA_EVENT_RISK|009420|Stage2-Actionable|2023-12-21", "entry_date": "2023-12-21", "entry_price": 34700.0, "entry_price_source": "entry_date close c from stock-web tradable shard", "evidence_family": "partner_reported_phase2_data|response_rate|licensed_asset|clinical_POC", "evidence_summary": "Immunovant reported positive initial Phase 2 proof-of-concept data for batoclimab in Graves disease, with response rates meaningfully above 50%; HanAll has the licensed-partner exposure.", "fine_archetype_id": "C24_AUTOIMMUNE_PARTNER_TRIAL_DATA_VALUE_CAPTURE", "interpretation": "Clinical POC data mattered, but the entry carried a meaningful -17% drawdown; C24 should permit Stage2-Actionable while attaching a high-beta biotech trial-risk guard.", "label": "positive_with_high_beta_guard", "large_sector_id": "L7_BIO_HEALTHCARE_MEDICAL", "loop_id": 164, "peak_180D_date": "2023-12-27", "peak_30D_date": "2023-12-27", "peak_90D_date": "2023-12-27", "price_adjustment_status": "raw_unadjusted_marcap", "price_basis": "tradable_raw", "price_source": "Songdaiki/stock-web", "profile_expected_error": "current_profile_too_late_if_partner_trial_data_is_ignored_but_needs_high_beta_MAE_guard", "representative": true, "round_id": "R7", "row_type": "trigger", "source_url": "https://www.immunovant.com/investors/news-events/press-releases/detail/58/immunovant-reports-positive-initial-phase-2-results-for", "stock_web_manifest_max_date": "2026-02-20", "ticker": "009420", "trigger_date": "2023-12-21", "trigger_type": "Stage2-Actionable", "trough_180D_date": "2024-08-05", "trough_30D_date": "2024-02-01", "trough_90D_date": "2024-02-01", "validation_scope": "30D_90D_180D_complete", "window_180D_end_date": "2024-09-19", "window_30D_end_date": "2024-02-06", "window_90D_end_date": "2024-05-08"}
{"MAE_180D_pct": -25.49, "MAE_30D_pct": -17.78, "MAE_90D_pct": -21.83, "MFE_180D_pct": 35.95, "MFE_30D_pct": 8.63, "MFE_90D_pct": 8.63, "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "calibration_usable": true, "canonical_archetype_id": "C24_BIO_TRIAL_DATA_EVENT_RISK", "case_id": "C24_009420_20240321_HANALL_FY2023_PIPELINE_UPDATE_LATE_FOLLOWUP", "company_name": "HanAll Biopharma", "component_score_breakdown": {"biotech_trial_risk_penalty": -8, "bottleneck_pricing_power": 3, "capital_allocation": 3, "earnings_visibility": 6, "eps_fcf_explosion": 4, "information_confidence": 15, "market_mispricing": 8, "valuation_rerating": 10}, "corporate_action_window_status": "clean_180D_or_no_candidate_overlap", "current_profile_error": true, "dedupe_key": "C24_BIO_TRIAL_DATA_EVENT_RISK|009420|Stage2-Watch|2024-03-21", "entry_date": "2024-03-21", "entry_price": 38250.0, "entry_price_source": "entry_date close c from stock-web tradable shard", "evidence_family": "annual_results_pipeline_update|same_data_reiteration|late_entry", "evidence_summary": "HanAll reiterated the partner-reported positive Phase 2 proof-of-concept Graves disease data in its FY2023 update.", "fine_archetype_id": "C24_AUTOIMMUNE_TRIAL_DATA_FOLLOWUP_LATE_ENTRY", "interpretation": "The same POC evidence resurfaced, but entry quality was worse: shallow early MFE, -21% 90D MAE, then delayed recovery. Follow-up reports need lower weight than first data release.", "label": "counterexample_watch_late_followup", "large_sector_id": "L7_BIO_HEALTHCARE_MEDICAL", "loop_id": 164, "peak_180D_date": "2024-10-22", "peak_30D_date": "2024-03-26", "peak_90D_date": "2024-03-26", "price_adjustment_status": "raw_unadjusted_marcap", "price_basis": "tradable_raw", "price_source": "Songdaiki/stock-web", "profile_expected_error": "current_profile_false_positive_if_reiterated_trial_data_gets_same_weight_as_initial_data", "representative": true, "round_id": "R7", "row_type": "trigger", "source_url": "https://hanall.com/board_view.php?bo_table=press&idx=88", "stock_web_manifest_max_date": "2026-02-20", "ticker": "009420", "trigger_date": "2024-03-21", "trigger_type": "Stage2-Watch", "trough_180D_date": "2024-08-05", "trough_30D_date": "2024-04-11", "trough_90D_date": "2024-05-31", "validation_scope": "30D_90D_180D_complete", "window_180D_end_date": "2024-12-16", "window_30D_end_date": "2024-05-07", "window_90D_end_date": "2024-08-01"}
{"MAE_180D_pct": -56.28, "MAE_30D_pct": -26.57, "MAE_90D_pct": -29.97, "MFE_180D_pct": 4.71, "MFE_30D_pct": 4.71, "MFE_90D_pct": 4.71, "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "calibration_usable": true, "canonical_archetype_id": "C24_BIO_TRIAL_DATA_EVENT_RISK", "case_id": "C24_321550_20240508_MERIGOLIX_ENDOMETRIOSIS_P2A_TOPLINE", "company_name": "TiumBio", "component_score_breakdown": {"biotech_trial_risk_penalty": -8, "bottleneck_pricing_power": 3, "capital_allocation": 3, "earnings_visibility": 6, "eps_fcf_explosion": 4, "information_confidence": 15, "market_mispricing": 8, "valuation_rerating": 5}, "corporate_action_window_status": "clean_180D_or_no_candidate_overlap", "current_profile_error": true, "dedupe_key": "C24_BIO_TRIAL_DATA_EVENT_RISK|321550|Stage2-FalsePositive|2024-05-08", "entry_date": "2024-05-08", "entry_price": 7640.0, "entry_price_source": "entry_date close c from stock-web tradable shard", "evidence_family": "positive_phase2a_topline|small_sample|no_partner_or_cash_bridge|female_health", "evidence_summary": "TiumBio announced positive Phase 2a topline merigolix data in endometriosis pain, including statistically significant efficacy versus placebo and safety language.", "fine_archetype_id": "C24_SMALLCAP_P2_TOPLINE_WITH_CASH_PARTNER_GAP", "interpretation": "The data headline was clinically positive, but the price path collapsed. C24 needs a financing/partner/next-trial bridge before treating small-cap Phase 2a data as Actionable.", "label": "counterexample_positive_data_no_financing_or_partner_bridge", "large_sector_id": "L7_BIO_HEALTHCARE_MEDICAL", "loop_id": 164, "peak_180D_date": "2024-05-08", "peak_30D_date": "2024-05-08", "peak_90D_date": "2024-05-08", "price_adjustment_status": "raw_unadjusted_marcap", "price_basis": "tradable_raw", "price_source": "Songdaiki/stock-web", "profile_expected_error": "current_profile_false_positive_if_positive_smallcap_trial_data_is_promoted_without_cash_partner_path", "representative": true, "round_id": "R7", "row_type": "trigger", "source_url": "https://www.prnewswire.com/news-releases/tiumbio-announces-positive-topline-data-from-phase-2a-trial-of-merigolix-in-patients-with-moderate-to-severe-endometriosis-associated-pain-302139490.html", "stock_web_manifest_max_date": "2026-02-20", "ticker": "321550", "trigger_date": "2024-05-08", "trigger_type": "Stage2-FalsePositive", "trough_180D_date": "2025-02-03", "trough_30D_date": "2024-06-21", "trough_90D_date": "2024-08-05", "validation_scope": "30D_90D_180D_complete", "window_180D_end_date": "2025-02-06", "window_30D_end_date": "2024-06-21", "window_90D_end_date": "2024-09-19"}
{"MAE_180D_pct": -11.85, "MAE_30D_pct": -11.85, "MAE_90D_pct": -11.85, "MFE_180D_pct": 96.47, "MFE_30D_pct": 28.9, "MFE_90D_pct": 80.04, "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "calibration_usable": true, "canonical_archetype_id": "C24_BIO_TRIAL_DATA_EVENT_RISK", "case_id": "C24_298380_20240603_ABL503_ASCO_P1_RESPONSE_DATA", "company_name": "ABL Bio", "component_score_breakdown": {"biotech_trial_risk_penalty": -3, "bottleneck_pricing_power": 6, "capital_allocation": 3, "earnings_visibility": 12, "eps_fcf_explosion": 10, "information_confidence": 15, "market_mispricing": 14, "valuation_rerating": 10}, "corporate_action_window_status": "clean_180D_or_no_candidate_overlap", "current_profile_error": false, "dedupe_key": "C24_BIO_TRIAL_DATA_EVENT_RISK|298380|Stage2-Actionable|2024-06-03", "entry_date": "2024-06-03", "entry_price": 24050.0, "entry_price_source": "entry_date close c from stock-web tradable shard", "evidence_family": "ASCO_phase1_response_data|complete_response_partial_responses|platform_validation", "evidence_summary": "ABL Bio highlighted promising Phase 1 ABL503 data presented at ASCO 2024 for its PD-L1 x 4-1BB bispecific antibody program.", "fine_archetype_id": "C24_ONCOLOGY_BISPECIFIC_ASCO_P1_RESPONSE_PLATFORM", "interpretation": "This was a strong C24 positive: ASCO clinical response data plus platform read-through produced large MFE with a manageable -12% MAE.", "label": "positive_trial_data_platform_revaluation", "large_sector_id": "L7_BIO_HEALTHCARE_MEDICAL", "loop_id": 164, "peak_180D_date": "2025-02-18", "peak_30D_date": "2024-07-05", "peak_90D_date": "2024-10-17", "price_adjustment_status": "raw_unadjusted_marcap", "price_basis": "tradable_raw", "price_source": "Songdaiki/stock-web", "profile_expected_error": "current_profile_too_late_if_ASCO_response_data_and_platform_validation_are_seen_only_after_partnering", "representative": true, "round_id": "R7", "row_type": "trigger", "source_url": "https://www.ablbio.com/en/company/news/36", "stock_web_manifest_max_date": "2026-02-20", "ticker": "298380", "trigger_date": "2024-06-03", "trigger_type": "Stage2-Actionable", "trough_180D_date": "2024-06-17", "trough_30D_date": "2024-06-17", "trough_90D_date": "2024-06-17", "validation_scope": "30D_90D_180D_complete", "window_180D_end_date": "2025-03-04", "window_30D_end_date": "2024-07-16", "window_90D_end_date": "2024-10-17"}
{"MAE_180D_pct": -35.98, "MAE_30D_pct": -15.21, "MAE_90D_pct": -27.26, "MFE_180D_pct": 47.44, "MFE_30D_pct": 9.4, "MFE_90D_pct": 39.66, "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "calibration_usable": true, "canonical_archetype_id": "C24_BIO_TRIAL_DATA_EVENT_RISK", "case_id": "C24_358570_20240603_GI102_ASCO_P1_2A_PRELIMINARY_DATA", "company_name": "GI Innovation", "component_score_breakdown": {"biotech_trial_risk_penalty": -8, "bottleneck_pricing_power": 6, "capital_allocation": 3, "earnings_visibility": 12, "eps_fcf_explosion": 10, "information_confidence": 15, "market_mispricing": 14, "valuation_rerating": 10}, "corporate_action_window_status": "clean_180D_or_no_candidate_overlap", "current_profile_error": true, "dedupe_key": "C24_BIO_TRIAL_DATA_EVENT_RISK|358570|Stage2-Watch|2024-06-03", "entry_date": "2024-06-03", "entry_price": 11700.0, "entry_price_source": "entry_date close c from stock-web tradable shard", "evidence_family": "ASCO_preliminary_phase1_2a_data|orphan_designation|combination_optionality|cashburn_risk", "evidence_summary": "ASCO 2024 included preliminary safety and efficacy data from the first-in-human Phase 1/2a GI-102 study in metastatic solid tumors.", "fine_archetype_id": "C24_IMMUNO_ONCOLOGY_EARLY_DATA_HIGH_MAE", "interpretation": "The row produced >40% 180D MFE but also suffered a -36% 180D MAE. Early IO data should be Watch until partner/cash or randomized expansion bridge is visible.", "label": "positive_with_high_MAE_guard", "large_sector_id": "L7_BIO_HEALTHCARE_MEDICAL", "loop_id": 164, "peak_180D_date": "2025-02-27", "peak_30D_date": "2024-07-09", "peak_90D_date": "2024-10-16", "price_adjustment_status": "raw_unadjusted_marcap", "price_basis": "tradable_raw", "price_source": "Songdaiki/stock-web", "profile_expected_error": "current_profile_correct_to_watch_but_wrong_if_promoted_to_actionable_without_cash_partner_confirmation", "representative": true, "round_id": "R7", "row_type": "trigger", "source_url": "https://www.asco.org/abstracts-presentations/233987", "stock_web_manifest_max_date": "2026-02-20", "ticker": "358570", "trigger_date": "2024-06-03", "trigger_type": "Stage2-Watch", "trough_180D_date": "2024-12-23", "trough_30D_date": "2024-06-25", "trough_90D_date": "2024-08-05", "validation_scope": "30D_90D_180D_complete", "window_180D_end_date": "2025-03-04", "window_30D_end_date": "2024-07-16", "window_90D_end_date": "2024-10-17"}
{"MAE_180D_pct": -21.28, "MAE_30D_pct": -20.91, "MAE_90D_pct": -21.28, "MFE_180D_pct": 56.7, "MFE_30D_pct": 5.29, "MFE_90D_pct": 23.99, "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "calibration_usable": true, "canonical_archetype_id": "C24_BIO_TRIAL_DATA_EVENT_RISK", "case_id": "C24_115180_20240529_Q901_ASCO_FIRST_IN_HUMAN_DATA", "company_name": "Qurient", "component_score_breakdown": {"biotech_trial_risk_penalty": -8, "bottleneck_pricing_power": 6, "capital_allocation": 3, "earnings_visibility": 12, "eps_fcf_explosion": 10, "information_confidence": 15, "market_mispricing": 14, "valuation_rerating": 10}, "corporate_action_window_status": "clean_180D_or_no_candidate_overlap", "current_profile_error": true, "dedupe_key": "C24_BIO_TRIAL_DATA_EVENT_RISK|115180|Stage2-Watch|2024-05-29", "entry_date": "2024-05-29", "entry_price": 4065.0, "entry_price_source": "entry_date close c from stock-web tradable shard", "evidence_family": "ASCO_first_in_human_data|biomarker_signal|early_dose_escalation|partnering_gap", "evidence_summary": "The ASCO 2024 Q901 first-in-human abstract reported early dose-level results and pharmacodynamic/biomarker framing for Qurient’s selective CDK7 inhibitor.", "fine_archetype_id": "C24_FIRST_IN_HUMAN_CDK7_BIOMARKER_DATA", "interpretation": "The path supports early Watch, not clean Actionable: 180D MFE was strong but 30D/90D MAE breached -20%.", "label": "positive_with_drawdown_guard", "large_sector_id": "L7_BIO_HEALTHCARE_MEDICAL", "loop_id": 164, "peak_180D_date": "2025-02-25", "peak_30D_date": "2024-05-31", "peak_90D_date": "2024-08-19", "price_adjustment_status": "raw_unadjusted_marcap", "price_basis": "tradable_raw", "price_source": "Songdaiki/stock-web", "profile_expected_error": "current_profile_too_binary_if_it_rejects_early_biomarker_data_or_promotes_it_without_MAE_guard", "representative": true, "round_id": "R7", "row_type": "trigger", "source_url": "https://ascopubs.org/doi/10.1200/JCO.2024.42.16_suppl.3078", "stock_web_manifest_max_date": "2026-02-20", "ticker": "115180", "trigger_date": "2024-05-29", "trigger_type": "Stage2-Watch", "trough_180D_date": "2024-08-05", "trough_30D_date": "2024-07-05", "trough_90D_date": "2024-08-05", "validation_scope": "30D_90D_180D_complete", "window_180D_end_date": "2025-02-26", "window_30D_end_date": "2024-07-11", "window_90D_end_date": "2024-10-14"}
{"MAE_180D_pct": -7.76, "MAE_30D_pct": -7.76, "MAE_90D_pct": -7.76, "MFE_180D_pct": 128.11, "MFE_30D_pct": 28.61, "MFE_90D_pct": 92.04, "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "calibration_usable": true, "canonical_archetype_id": "C24_BIO_TRIAL_DATA_EVENT_RISK", "case_id": "C24_039200_20240119_LASER301_LAZERTINIB_PUBLISHED_DATA", "company_name": "Oscotec", "component_score_breakdown": {"biotech_trial_risk_penalty": -3, "bottleneck_pricing_power": 6, "capital_allocation": 3, "earnings_visibility": 12, "eps_fcf_explosion": 10, "information_confidence": 24, "market_mispricing": 14, "valuation_rerating": 10}, "corporate_action_window_status": "clean_180D_or_no_candidate_overlap", "current_profile_error": false, "dedupe_key": "C24_BIO_TRIAL_DATA_EVENT_RISK|039200|Stage2-Actionable|2024-01-19", "entry_date": "2024-01-19", "entry_price": 20100.0, "entry_price_source": "entry_date close c from stock-web tradable shard", "evidence_family": "phase3_laser301_data|PFS_benefit|royalty_derivative|late_stage_validation", "evidence_summary": "The LASER301 publication reported that lazertinib significantly improved efficacy versus gefitinib in EGFR-mutated advanced NSCLC with a manageable safety profile.", "fine_archetype_id": "C24_LATE_STAGE_ONCOLOGY_DATA_ROYALTY_READTHROUGH", "interpretation": "This is the clean late-stage C24 positive: trial data were already de-risked enough to justify Stage2-Actionable before later regulatory/commercial C23 triggers.", "label": "positive_late_stage_trial_data_royalty_readthrough", "large_sector_id": "L7_BIO_HEALTHCARE_MEDICAL", "loop_id": 164, "peak_180D_date": "2024-08-21", "peak_30D_date": "2024-03-06", "peak_90D_date": "2024-06-03", "price_adjustment_status": "raw_unadjusted_marcap", "price_basis": "tradable_raw", "price_source": "Songdaiki/stock-web", "profile_expected_error": "current_profile_too_late_if_late_stage_trial_data_readthrough_waits_for_approval_only", "representative": true, "round_id": "R7", "row_type": "trigger", "source_url": "https://pubmed.ncbi.nlm.nih.gov/37379502/", "stock_web_manifest_max_date": "2026-02-20", "ticker": "039200", "trigger_date": "2024-01-19", "trigger_type": "Stage2-Actionable", "trough_180D_date": "2024-02-01", "trough_30D_date": "2024-02-01", "trough_90D_date": "2024-02-01", "validation_scope": "30D_90D_180D_complete", "window_180D_end_date": "2024-10-18", "window_30D_end_date": "2024-03-06", "window_90D_end_date": "2024-06-04"}
```

## 9. Machine-readable score simulation rows JSONL

```jsonl
{"case_id": "C24_009420_20231221_BATOCLIMAB_GRAVES_P2_INITIAL_DATA", "component_score_breakdown": {"biotech_trial_risk_penalty": -3, "bottleneck_pricing_power": 6, "capital_allocation": 3, "earnings_visibility": 12, "eps_fcf_explosion": 10, "information_confidence": 24, "market_mispricing": 14, "valuation_rerating": 10}, "current_profile_error": false, "ticker": "009420"}
{"case_id": "C24_009420_20240321_HANALL_FY2023_PIPELINE_UPDATE_LATE_FOLLOWUP", "component_score_breakdown": {"biotech_trial_risk_penalty": -8, "bottleneck_pricing_power": 3, "capital_allocation": 3, "earnings_visibility": 6, "eps_fcf_explosion": 4, "information_confidence": 15, "market_mispricing": 8, "valuation_rerating": 10}, "current_profile_error": true, "ticker": "009420"}
{"case_id": "C24_321550_20240508_MERIGOLIX_ENDOMETRIOSIS_P2A_TOPLINE", "component_score_breakdown": {"biotech_trial_risk_penalty": -8, "bottleneck_pricing_power": 3, "capital_allocation": 3, "earnings_visibility": 6, "eps_fcf_explosion": 4, "information_confidence": 15, "market_mispricing": 8, "valuation_rerating": 5}, "current_profile_error": true, "ticker": "321550"}
{"case_id": "C24_298380_20240603_ABL503_ASCO_P1_RESPONSE_DATA", "component_score_breakdown": {"biotech_trial_risk_penalty": -3, "bottleneck_pricing_power": 6, "capital_allocation": 3, "earnings_visibility": 12, "eps_fcf_explosion": 10, "information_confidence": 15, "market_mispricing": 14, "valuation_rerating": 10}, "current_profile_error": false, "ticker": "298380"}
{"case_id": "C24_358570_20240603_GI102_ASCO_P1_2A_PRELIMINARY_DATA", "component_score_breakdown": {"biotech_trial_risk_penalty": -8, "bottleneck_pricing_power": 6, "capital_allocation": 3, "earnings_visibility": 12, "eps_fcf_explosion": 10, "information_confidence": 15, "market_mispricing": 14, "valuation_rerating": 10}, "current_profile_error": true, "ticker": "358570"}
{"case_id": "C24_115180_20240529_Q901_ASCO_FIRST_IN_HUMAN_DATA", "component_score_breakdown": {"biotech_trial_risk_penalty": -8, "bottleneck_pricing_power": 6, "capital_allocation": 3, "earnings_visibility": 12, "eps_fcf_explosion": 10, "information_confidence": 15, "market_mispricing": 14, "valuation_rerating": 10}, "current_profile_error": true, "ticker": "115180"}
{"case_id": "C24_039200_20240119_LASER301_LAZERTINIB_PUBLISHED_DATA", "component_score_breakdown": {"biotech_trial_risk_penalty": -3, "bottleneck_pricing_power": 6, "capital_allocation": 3, "earnings_visibility": 12, "eps_fcf_explosion": 10, "information_confidence": 24, "market_mispricing": 14, "valuation_rerating": 10}, "current_profile_error": false, "ticker": "039200"}
```

## 10. Narrative-only / blocked rows JSONL

```jsonl
{"blocked_reason": "corporate_action_contaminated_180D_window", "calibration_usable": false, "canonical_archetype_id": "C24_BIO_TRIAL_DATA_EVENT_RISK", "case_id": "C24_288330_20240730_BBT877_ENROLLMENT_COMPLETE_BLOCKED_BY_CORP_ACTION", "company_name": "Bridge Biotherapeutics", "evidence_summary": "Bridge Biotherapeutics announced BBT-877 Phase 2 enrollment completion and expected topline in 1H25.", "large_sector_id": "L7_BIO_HEALTHCARE_MEDICAL", "profile_note": "288330 profile has corporate_action_candidate_date 2024-08-08 inside the forward window.", "row_type": "narrative_only_audit", "source_url": "https://www.prnewswire.com/news-releases/bridge-biotherapeutics-announces-completion-of-enrollment-in-the-phase-2a-clinical-study-of-bbt-877-for-the-treatment-of-idiopathic-pulmonary-fibrosis-302208799.html", "ticker": "288330", "trigger_date": "2024-07-30", "trigger_type": "Stage2-Watch"}
{"blocked_reason": "corporate_action_contaminated_180D_window", "calibration_usable": false, "canonical_archetype_id": "C24_BIO_TRIAL_DATA_EVENT_RISK", "case_id": "C24_288330_20250415_BBT877_P2_FAILURE_BLOCKED_BY_CORP_ACTION_BUT_THESIS_BREAK_CONFIRMED", "company_name": "Bridge Biotherapeutics", "evidence_summary": "BBT-877 failed to meet the Phase 2 primary endpoint, FVC change at 24 weeks, in 129 IPF patients.", "large_sector_id": "L7_BIO_HEALTHCARE_MEDICAL", "profile_note": "288330 profile has corporate_action_candidate_dates 2025-07-16 and 2026-01-09 inside/near the forward window.", "row_type": "narrative_only_audit", "source_url": "https://www.koreabiomed.com/news/articleView.html?idxno=27276", "ticker": "288330", "trigger_date": "2025-04-15", "trigger_type": "4C"}
```

## 11. Aggregate / shadow weight / residual contribution JSONL

```jsonl
{"avg_MAE_180D_pct": -25.22, "avg_MAE_90D_pct": -19.67, "avg_MFE_180D_pct": 57.73, "avg_MFE_90D_pct": 40.54, "canonical_archetype_id": "C24_BIO_TRIAL_DATA_EVENT_RISK", "counterexample_count": 2, "current_profile_error_count": 4, "index_baseline_coverage_after_if_accepted": "C24 rows 76", "index_baseline_coverage_before": "C24 rows 69", "large_sector_id": "L7_BIO_HEALTHCARE_MEDICAL", "loop_id": 164, "narrative_only_blocked_count": 2, "positive_case_count": 5, "representative_trigger_count": 7, "round_id": "R7", "row_type": "aggregate", "stage2_watch_or_guard_count": 4, "usable_trigger_row_count": 7}
{"candidate_axis": "C24_TRIAL_DATA_STAGE_AND_VALUE_CAPTURE_GATE_V1", "canonical_archetype_id": "C24_BIO_TRIAL_DATA_EVENT_RISK", "do_not_propose_new_weight_delta": false, "expected_effect": "Reduce small-cap Phase2a false positives while preserving late-stage/externally validated trial-data positives.", "large_sector_id": "L7_BIO_HEALTHCARE_MEDICAL", "loop_id": 164, "proposed_rule": "Promote C24 only when trial data stage, external validation, effect size, and value-capture bridge are all present; otherwise keep early data at Watch and add MAE/cash/partner guard.", "round_id": "R7", "row_type": "shadow_weight_candidate"}
{"current_profile_error_count": 4, "existing_axis_strengthened": "price_only_blowoff_blocks_positive_stage|full_4b_requires_non_price_evidence|hard_4c_thesis_break_routes_to_4c", "existing_axis_weakened": "hard_4c_should_not_fire_on_trial_enrollment_or_followup_vocabulary_without_endpoint_result", "new_axis_proposed": "c24_trial_data_stage_and_value_capture_gate", "note": "C24 needs a ladder: early biomarker/Phase1 -> Watch; Phase2a small sample without partner/cash -> false-positive guard; late-stage/partner-validated data -> Actionable.", "residual_label": "bio_trial_data_value_capture_vs_trial_event_volatility", "row_type": "residual_contribution"}
```

## 12. Validation scope

```text
all_usable_trigger_rows_have_entry_date = true
all_usable_trigger_rows_have_entry_price = true
all_usable_trigger_rows_have_trigger_type = true
all_usable_trigger_rows_have_large_sector_id = true
all_usable_trigger_rows_have_canonical_archetype_id = true
all_usable_trigger_rows_have_complete_30_90_180_MFE_MAE = true
corporate_action_contaminated_rows_used_for_calibration = false
narrative_only_rows_kept_out_of_aggregate = true
standard_v12_filename = true
compact_filename_used = false
```

## 13. Deferred Coding Agent Handoff Prompt

```text
Do not execute during this research session.

Later batch implementation task:
1. Ingest this MD together with other v12 residual research files.
2. Validate every trigger row for required fields, stock-web 30/90/180D MFE/MAE, dedupe key, and corporate-action contamination.
3. Map all fine_archetype_id values back to C24_BIO_TRIAL_DATA_EVENT_RISK.
4. Evaluate the shadow rule candidate C24_TRIAL_DATA_STAGE_AND_VALUE_CAPTURE_GATE_V1.
5. If accepted, add a scoped C24 guard that distinguishes early biomarker/Phase1/Phase2a vocabulary from externally validated late-stage or partner-validated data.
6. Do not loosen Stage3-Green. Prefer Stage2-Watch / Stage2-Actionable boundary repair and 4B/high-MAE guard improvement.
7. Keep production profile changes safe, small, explainable, and reversible.
```

## 14. Next research state

```text
completed_round = R7
completed_loop = 164
selection_basis = docs/core/V12_Research_No_Repeat_Index.md
selected_priority_bucket = Priority 2 quality-repair after session-aware P0/P1/thin-P2 clearing
next_recommended_archetypes = C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY|C17_CHEMICAL_COMMODITY_MARGIN_SPREAD|C15_MATERIAL_SPREAD_SUPERCYCLE|C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION|C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN
round_schedule_status = coverage_index_selected_not_sequential
round_sector_consistency = pass
```
