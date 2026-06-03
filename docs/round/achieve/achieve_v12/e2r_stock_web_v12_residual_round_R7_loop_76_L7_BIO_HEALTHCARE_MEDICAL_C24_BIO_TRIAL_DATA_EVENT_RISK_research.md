# E2R Stock-Web v12 Residual Research — R7 Loop 76 / L7 / C24

## Metadata

```json
{
  "research_session": "post_calibrated_sector_archetype_residual_research",
  "mode": "historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12",
  "scheduled_round": "R7",
  "scheduled_loop": 76,
  "round_schedule_status": "valid",
  "round_sector_consistency": "pass",
  "completed_round": "R7",
  "completed_loop": 76,
  "computed_next_round": "R8",
  "computed_next_loop": 76,
  "large_sector_id": "L7_BIO_HEALTHCARE_MEDICAL",
  "canonical_archetype_id": "C24_BIO_TRIAL_DATA_EVENT_RISK",
  "fine_archetype_id": "BISPECIFIC_ADC_ONCOLOGY_TRIAL_DATA_EVENT_BRIDGE_VS_CLINICAL_BETA_FADE",
  "loop_objective": [
    "coverage_gap_fill",
    "counterexample_mining",
    "4B_non_price_requirement_stress_test",
    "trial_data_event_risk_guardrail",
    "clinical_data_bridge_vs_bio_beta_fade",
    "sector_specific_rule_discovery",
    "canonical_archetype_compression",
    "source_repair_queue_creation",
    "corporate_action_validation_queue_creation"
  ],
  "price_source": "Songdaiki/stock-web",
  "price_basis": "tradable_raw",
  "price_adjustment_status": "raw_unadjusted_marcap",
  "stock_web_manifest_max_date": "2026-02-20",
  "production_scoring_changed": false,
  "shadow_weight_only": true,
  "handoff_prompt_executed_now": false,
  "do_not_propose_new_weight_delta": true
}
```

## Execution compliance note

This file is a standalone historical calibration / sector-archetype residual research Markdown artifact.  
It does not patch `stock_agent`, does not run live discovery, and does not propose immediate production scoring changes.

The execution used `Songdaiki/stock-web` as the sole price atlas:

```text
price_source = Songdaiki/stock-web
price_basis = tradable_raw
price_adjustment_status = raw_unadjusted_marcap
stock_web_manifest_max_date = 2026-02-20
production_scoring_changed = false
shadow_weight_only = true
handoff_prompt_executed_now = false
```

## Round / scope resolution

Previous completed state in this interactive run: R6 / loop 76.

Therefore:

```text
scheduled_round = R7
scheduled_loop = 76
allowed_large_sector = L7_BIO_HEALTHCARE_MEDICAL
selected_large_sector = L7_BIO_HEALTHCARE_MEDICAL
selected_canonical_archetype_id = C24_BIO_TRIAL_DATA_EVENT_RISK
computed_next_round = R8
computed_next_loop = 76
```

R7 was routed to C24 because loop 75 used C25 and C24 is thinner than C23.  
This file tests clinical/trial-data event risk rather than medical device export or approval-to-commercialization.

## No-Repeat / novelty check

No hard duplicate is intentionally reused.

Hard duplicate key checked conceptually:

```text
canonical_archetype_id + symbol + trigger_type + entry_date
```

No-Repeat shows C24 is concentrated in:

```text
000100, 028300, 009420, 039200, UNKNOWN_SYMBOL
```

This run uses three different symbols:

```text
298380 / 에이비엘바이오 / bispecific-ADC trial-data and partner-validation bridge
141080 / 리가켐바이오·레고켐바이오 / ADC platform trial-data post-CA bridge
215600 / 신라젠 / oncology trial-data beta fade after post-CA entry
```

Data-quality note:

```text
All three rows are stock-web calibration usable by profile-level corporate-action candidates.
All three rows are source_proxy_only=true / evidence_url_pending=true.
141080 and 215600 are deliberately measured after their 2024 corporate-action candidate dates.
141080 still requires corporate-action/share-count continuity validation before runtime promotion.
```

## Research thesis

C24 is not “bio stock went up.”

The mechanism must pass through:

```text
trial / clinical data event
→ endpoint quality and safety
→ regulatory path or partner validation
→ financing runway and commercialization bridge
→ durable rerating
```

A clinical headline is a lab door opening.  
The bridge is whether the data walks out with endpoints, safety, regulator path and funding attached.

---

## Case 1 — Positive with lifecycle 4B: 298380 / 에이비엘바이오

### Evidence status

```text
source_proxy_only = true
evidence_url_pending = true
source_repair_required = true
```

The source-repair task is bispecific / ADC oncology trial-data quality, partner validation, regulatory path and commercialization evidence.

```text
evidence_family = BISPECIFIC_ADC_ONCOLOGY_TRIAL_DATA_PARTNERING_PLATFORM_VALUE_BRIDGE
case_role = positive_with_lifecycle_4b_watch
trigger_date = 2024-02-22
entry_date = 2024-02-23
entry_price = 21,500
```

### Stock-Web price path

Observed rows from `atlas/ohlcv_tradable_by_symbol_year/298/298380/2024.csv`:

```text
2024-02-23,21500,23550,21450,22500
2024-03-06,24550,28400,24350,27300
2024-07-30,30250,31350,29650,31350
2024-10-17,42050,43300,39550,40350
2024-11-01,36900,37200,35250,35850
```

### Backtest

```text
MFE_30D  = +41.86%
MAE_30D  = -0.23%
MFE_90D  = +41.86%
MAE_90D  = -0.23%
MFE_180D = +101.40%
MAE_180D = -0.23%
peak_180 = 43,300 on 2024-10-17
trough_180 = 21,450 on 2024-02-23
peak_to_later_drawdown = -18.59%
```

### Interpretation

This is the clean C24 positive-shaped path.  
It has controlled entry-basis risk and a multi-month MFE path.

Correct treatment:

```text
trial data / partner validation / regulatory bridge verified → Stage2 possible
bridge stale after peak → lifecycle local 4B-watch
```

---

## Case 2 — Positive after CA validation: 141080 / 리가켐바이오·레고켐바이오

### Evidence status

```text
source_proxy_only = true
evidence_url_pending = true
share_count_change_inside_window = true
post_corporate_action_validation_required = true
source_repair_required = true
```

The source-repair task is ADC platform trial data, partner validation, pipeline value and commercialization bridge evidence.

```text
evidence_family = ADC_PLATFORM_TRIAL_DATA_PARTNERING_POST_CA_PIPELINE_VALUE_BRIDGE
case_role = positive_with_post_corporate_action_validation
trigger_date = 2024-04-23
entry_date = 2024-04-24
entry_price = 68,000
```

### Stock-Web price path

Observed rows from `atlas/ohlcv_tradable_by_symbol_year/141/141080/2024.csv`:

```text
2024-04-23,62800,69000,62300,67800
2024-04-24,68000,69000,67300,68200
2024-05-30,61300,65200,60600,64300
2024-08-26,94900,98700,94100,98000
2024-10-22,130700,139600,127100,130700
2024-11-01,126500,128900,119400,119400
```

### Backtest

```text
MFE_30D  = +5.88%
MAE_30D  = -4.41%
MFE_90D  = +45.44%
MAE_90D  = -10.88%
MFE_180D = +105.29%
MAE_180D = -10.88%
peak_180 = 139,600 on 2024-10-22
trough_180 = 60,600 on 2024-05-30
peak_to_later_drawdown = -14.47%
```

### Interpretation

This is a strong C24 positive, but only after corporate-action handling.  
The 2024-04-23 candidate means the model must not casually mix pre-CA and post-CA rows.

Correct treatment:

```text
post-CA validation first
then Stage2 possible after source repair
```

---

## Case 3 — Counterexample / local 4B: 215600 / 신라젠

### Evidence status

```text
source_proxy_only = true
evidence_url_pending = true
post_corporate_action_validation_required = true
source_repair_required = true
```

This row tests oncology-trial / financing / post-CA clinical beta without enough endpoint, regulatory and commercialization bridge.

```text
evidence_family = ONCOLOGY_TRIAL_DATA_FINANCING_POST_CA_BETA_WITH_WEAK_ENDPOINT_COMMERCIALIZATION_BRIDGE
case_role = counterexample_trial_beta_local4b_post_ca
trigger_date = 2024-07-09
entry_date = 2024-07-10
entry_price = 3,200
```

### Stock-Web price path

Observed rows from `atlas/ohlcv_tradable_by_symbol_year/215/215600/2024.csv`:

```text
2024-07-09,3190,3255,3145,3220
2024-07-10,3200,3225,3150,3170
2024-08-19,3190,3435,3165,3275
2024-09-06,2735,2780,2680,2700
2024-10-25,2395,2410,2340,2400
```

### Backtest

```text
MFE_30D  = +7.34%
MAE_30D  = -12.19%
MFE_90D  = +7.34%
MAE_90D  = -18.44%
MFE_180D = +7.34%
MAE_180D = -26.88%
peak_180 = 3,435 on 2024-08-19
trough_180 = 2,340 on 2024-10-25
peak_to_later_drawdown = -31.88%
```

### Interpretation

This is the C24 false-positive boundary.  
The post-CA entry avoided the corporate-action date, but price action did not validate a durable clinical rerating.

Correct treatment:

```text
clinical beta / financing beta
→ no endpoint / safety / regulatory / commercialization bridge
→ local 4B-watch
```

---

## Cross-case residual finding

### What this strengthens

```text
stage2_required_bridge = strengthen
price_only_blowoff_blocks_positive_stage = strengthen
local_4b_watch_guard = strengthen
full_4b_requires_non_price_evidence = keep
corporate_action_validation_guard = strengthen
```

### What this does not justify

```text
do_not_raise_generic_C24_bio_trial_beta_weight = true
do_not_treat_all_clinical_event_MFE_as_Green = true
do_not_convert_bio_drawdown_to_hard_4C_without_endpoint_safety_regulatory_or_financing_break = true
```

### Candidate canonical compression

Fine labels can compress into:

```text
BISPECIFIC_ADC_ONCOLOGY_TRIAL_DATA_EVENT_BRIDGE_VS_CLINICAL_BETA_FADE
```

This fine archetype covers:

```text
1. bispecific / ADC trial-data plus partner validation → Stage2 possible after source repair
2. ADC platform post-CA trial-data path → Stage2 possible after CA validation
3. oncology clinical beta without endpoint/regulatory bridge → false Stage2 / local 4B
```

---

## Machine-readable rows

### price source validation row

```jsonl
{"row_type": "price_source_validation", "source": "Songdaiki/stock-web", "source_url": "https://github.com/Songdaiki/stock-web", "manifest_path": "atlas/manifest.json", "schema_path": "atlas/schema.json", "universe_path": "atlas/universe/all_symbols.csv", "manifest_max_date": "2026-02-20", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "raw_shard_root": "atlas/ohlcv_raw_by_symbol_year", "validation_status": "usable_for_historical_calibration"}
```

### case rows

```jsonl
{"row_type": "case", "case_id": "R7L76-C24-298380-ABL-BIO-BISPECIFIC-ADC-TRIAL-DATA-BRIDGE", "symbol": "298380", "company_name": "에이비엘바이오", "round": "R7", "loop": "76", "large_sector_id": "L7_BIO_HEALTHCARE_MEDICAL", "canonical_archetype_id": "C24_BIO_TRIAL_DATA_EVENT_RISK", "fine_archetype_id": "BISPECIFIC_ADC_ONCOLOGY_TRIAL_DATA_EVENT_BRIDGE_VS_CLINICAL_BETA_FADE", "case_type": "bio_trial_data_event_risk", "positive_or_counterexample": "positive", "best_trigger": "Stage2-Actionable-BispecificADCTrialDataPartneringBridge", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 0.5, "score_price_alignment": "C24 should allow a trial-data/platform-event Stage2 when clinical data, partner validation, differentiated modality and downstream commercialization bridge are visible. ABL Bio produced high MFE with almost no entry-basis MAE, but later post-peak fading still requires lifecycle local 4B if clinical/partner bridge evidence goes stale.", "current_profile_verdict": "source_repair_required_before_runtime_weight", "price_source": "Songdaiki/stock-web", "notes": "Stock-web path usable; non-proxy endpoint quality, safety, regulatory path, partner validation, financing runway and commercialization evidence required before runtime promotion."}
{"row_type": "case", "case_id": "R7L76-C24-141080-LIGACHEM-ADC-TRIAL-DATA-POST-CA-LIFECYCLE", "symbol": "141080", "company_name": "리가켐바이오/레고켐바이오", "round": "R7", "loop": "76", "large_sector_id": "L7_BIO_HEALTHCARE_MEDICAL", "canonical_archetype_id": "C24_BIO_TRIAL_DATA_EVENT_RISK", "fine_archetype_id": "BISPECIFIC_ADC_ONCOLOGY_TRIAL_DATA_EVENT_BRIDGE_VS_CLINICAL_BETA_FADE", "case_type": "bio_trial_data_event_risk", "positive_or_counterexample": "positive", "best_trigger": "Stage2-Actionable-ADCPipelineTrialDataPostCABridge", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 0.5, "score_price_alignment": "C24 should allow ADC-platform trial-data / partner-validation positives only after corporate-action windows are handled. LigaChem Bio had a 2024-04-23 corporate-action candidate, so the post-CA entry is deliberately 2024-04-24; the post-entry path produced very large MFE, but requires source repair and CA validation before runtime promotion.", "current_profile_verdict": "source_repair_required_before_runtime_weight", "price_source": "Songdaiki/stock-web", "notes": "Stock-web path usable; non-proxy endpoint quality, safety, regulatory path, partner validation, financing runway and commercialization evidence required before runtime promotion."}
{"row_type": "case", "case_id": "R7L76-C24-215600-SILLAJEN-ONCOLOGY-TRIAL-DATA-POST-CA-BETA-FADE", "symbol": "215600", "company_name": "신라젠", "round": "R7", "loop": "76", "large_sector_id": "L7_BIO_HEALTHCARE_MEDICAL", "canonical_archetype_id": "C24_BIO_TRIAL_DATA_EVENT_RISK", "fine_archetype_id": "BISPECIFIC_ADC_ONCOLOGY_TRIAL_DATA_EVENT_BRIDGE_VS_CLINICAL_BETA_FADE", "case_type": "bio_trial_data_event_risk", "positive_or_counterexample": "counterexample", "best_trigger": "Stage2-FalsePositive / OncologyTrialDataPostCABetaFade", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 0.5, "score_price_alignment": "C24 should not treat oncology-trial or financing/post-CA bio beta as durable Stage2 unless endpoint quality, safety, regulatory path, financing runway and commercialization bridge are visible. SillaJen had only a small MFE after the post-CA entry and then opened a high-MAE decline.", "current_profile_verdict": "source_repair_required_before_runtime_weight", "price_source": "Songdaiki/stock-web", "notes": "Stock-web path usable; non-proxy endpoint quality, safety, regulatory path, partner validation, financing runway and commercialization evidence required before runtime promotion."}
```

### trigger rows

```jsonl
{"row_type": "trigger", "trigger_id": "TRG_R7L76-C24-298380-ABL-BIO-BISPECIFIC-ADC-TRIAL-DATA-BRIDGE", "case_id": "R7L76-C24-298380-ABL-BIO-BISPECIFIC-ADC-TRIAL-DATA-BRIDGE", "symbol": "298380", "company_name": "에이비엘바이오", "round": "R7", "loop": "76", "large_sector_id": "L7_BIO_HEALTHCARE_MEDICAL", "canonical_archetype_id": "C24_BIO_TRIAL_DATA_EVENT_RISK", "fine_archetype_id": "BISPECIFIC_ADC_ONCOLOGY_TRIAL_DATA_EVENT_BRIDGE_VS_CLINICAL_BETA_FADE", "loop_objective": "coverage_gap_fill|counterexample_mining|trial_data_event_risk_guardrail", "trigger_type": "Stage2-Actionable-BispecificADCTrialDataPartneringBridge", "trigger_date": "2024-02-22", "entry_date": "2024-02-23", "entry_price": 21500.0, "evidence_available_at_that_date": "BISPECIFIC_ADC_ONCOLOGY_TRIAL_DATA_PARTNERING_PLATFORM_VALUE_BRIDGE", "evidence_source": "source_proxy_manual_verification_required:ABL_BIO_2024_BISPECIFIC_ADC_ONCOLOGY_TRIAL_DATA_PARTNER_PLATFORM_VALUE_BRIDGE", "stage2_evidence_fields": ["trial_data_event", "endpoint_safety_or_partner_validation_candidate", "regulatory_or_commercialization_bridge_candidate"], "stage3_evidence_fields": ["relative_strength", "financing_runway_or_pipeline_value_bridge_candidate"], "stage4b_evidence_fields": ["clinical_beta", "bridge_stale_or_absent", "MAE_widening", "post_peak_drawdown"], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/298/298380/2024.csv", "profile_path": "atlas/symbol_profiles/298/298380.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": 41.86, "MFE_90D_pct": 41.86, "MFE_180D_pct": 101.4, "MAE_30D_pct": -0.23, "MAE_90D_pct": -0.23, "MAE_180D_pct": -0.23, "peak_date": "2024-10-17", "peak_price": 43300.0, "drawdown_after_peak_pct": -18.59, "green_lateness_ratio": null, "four_b_local_peak_proximity": "local_4b_watch_after_trial_data_or_platform_peak_if_endpoint_partner_or_regulatory_bridge_fades", "four_b_full_window_peak_proximity": "full_4b_requires_non_price_endpoint_failure_safety_signal_regulatory_rejection_financing_or_commercialization_break", "trigger_outcome_label": "positive_with_lifecycle_4b_watch", "current_profile_verdict": "C24 should allow a trial-data/platform-event Stage2 when clinical data, partner validation, differentiated modality and downstream commercialization bridge are visible. ABL Bio produced high MFE with almost no entry-basis MAE, but later post-peak fading still requires lifecycle local 4B if clinical/partner bridge evidence goes stale.", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window_by_profile_or_post_CA_entry", "share_count_change_inside_window": false, "same_entry_group_id": "C24_BIO_TRIAL_298380_2024-02-23", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 0.5, "do_not_count_as_new_case": false, "source_proxy_only": true, "evidence_url_pending": true}
{"row_type": "trigger", "trigger_id": "TRG_R7L76-C24-141080-LIGACHEM-ADC-TRIAL-DATA-POST-CA-LIFECYCLE", "case_id": "R7L76-C24-141080-LIGACHEM-ADC-TRIAL-DATA-POST-CA-LIFECYCLE", "symbol": "141080", "company_name": "리가켐바이오/레고켐바이오", "round": "R7", "loop": "76", "large_sector_id": "L7_BIO_HEALTHCARE_MEDICAL", "canonical_archetype_id": "C24_BIO_TRIAL_DATA_EVENT_RISK", "fine_archetype_id": "BISPECIFIC_ADC_ONCOLOGY_TRIAL_DATA_EVENT_BRIDGE_VS_CLINICAL_BETA_FADE", "loop_objective": "coverage_gap_fill|counterexample_mining|trial_data_event_risk_guardrail", "trigger_type": "Stage2-Actionable-ADCPipelineTrialDataPostCABridge", "trigger_date": "2024-04-23", "entry_date": "2024-04-24", "entry_price": 68000.0, "evidence_available_at_that_date": "ADC_PLATFORM_TRIAL_DATA_PARTNERING_POST_CA_PIPELINE_VALUE_BRIDGE", "evidence_source": "source_proxy_manual_verification_required:LIGACHEM_BIO_LEGOCHEM_2024_ADC_TRIAL_DATA_PARTNERING_PIPELINE_VALUE_POST_CA_BRIDGE", "stage2_evidence_fields": ["trial_data_event", "endpoint_safety_or_partner_validation_candidate", "regulatory_or_commercialization_bridge_candidate"], "stage3_evidence_fields": ["relative_strength", "financing_runway_or_pipeline_value_bridge_candidate"], "stage4b_evidence_fields": ["clinical_beta", "bridge_stale_or_absent", "MAE_widening", "post_peak_drawdown"], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/141/141080/2024.csv", "profile_path": "atlas/symbol_profiles/141/141080.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": 5.88, "MFE_90D_pct": 45.44, "MFE_180D_pct": 105.29, "MAE_30D_pct": -4.41, "MAE_90D_pct": -10.88, "MAE_180D_pct": -10.88, "peak_date": "2024-10-22", "peak_price": 139600.0, "drawdown_after_peak_pct": -14.47, "green_lateness_ratio": null, "four_b_local_peak_proximity": "local_4b_watch_after_trial_data_or_platform_peak_if_endpoint_partner_or_regulatory_bridge_fades", "four_b_full_window_peak_proximity": "full_4b_requires_non_price_endpoint_failure_safety_signal_regulatory_rejection_financing_or_commercialization_break", "trigger_outcome_label": "positive_with_post_corporate_action_validation", "current_profile_verdict": "C24 should allow ADC-platform trial-data / partner-validation positives only after corporate-action windows are handled. LigaChem Bio had a 2024-04-23 corporate-action candidate, so the post-CA entry is deliberately 2024-04-24; the post-entry path produced very large MFE, but requires source repair and CA validation before runtime promotion.", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window_by_profile_or_post_CA_entry", "share_count_change_inside_window": true, "same_entry_group_id": "C24_BIO_TRIAL_141080_2024-04-24", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 0.5, "do_not_count_as_new_case": false, "source_proxy_only": true, "evidence_url_pending": true}
{"row_type": "trigger", "trigger_id": "TRG_R7L76-C24-215600-SILLAJEN-ONCOLOGY-TRIAL-DATA-POST-CA-BETA-FADE", "case_id": "R7L76-C24-215600-SILLAJEN-ONCOLOGY-TRIAL-DATA-POST-CA-BETA-FADE", "symbol": "215600", "company_name": "신라젠", "round": "R7", "loop": "76", "large_sector_id": "L7_BIO_HEALTHCARE_MEDICAL", "canonical_archetype_id": "C24_BIO_TRIAL_DATA_EVENT_RISK", "fine_archetype_id": "BISPECIFIC_ADC_ONCOLOGY_TRIAL_DATA_EVENT_BRIDGE_VS_CLINICAL_BETA_FADE", "loop_objective": "coverage_gap_fill|counterexample_mining|trial_data_event_risk_guardrail", "trigger_type": "Stage2-FalsePositive / OncologyTrialDataPostCABetaFade", "trigger_date": "2024-07-09", "entry_date": "2024-07-10", "entry_price": 3200.0, "evidence_available_at_that_date": "ONCOLOGY_TRIAL_DATA_FINANCING_POST_CA_BETA_WITH_WEAK_ENDPOINT_COMMERCIALIZATION_BRIDGE", "evidence_source": "source_proxy_manual_verification_required:SILLAJEN_2024_ONCOLOGY_TRIAL_DATA_FINANCING_POST_CA_ENDPOINT_SAFETY_REGULATORY_COMMERCIALIZATION_BRIDGE", "stage2_evidence_fields": ["trial_data_event", "endpoint_safety_or_partner_validation_candidate", "regulatory_or_commercialization_bridge_candidate"], "stage3_evidence_fields": ["relative_strength", "financing_runway_or_pipeline_value_bridge_candidate"], "stage4b_evidence_fields": ["clinical_beta", "bridge_stale_or_absent", "MAE_widening", "post_peak_drawdown"], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/215/215600/2024.csv", "profile_path": "atlas/symbol_profiles/215/215600.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": 7.34, "MFE_90D_pct": 7.34, "MFE_180D_pct": 7.34, "MAE_30D_pct": -12.19, "MAE_90D_pct": -18.44, "MAE_180D_pct": -26.88, "peak_date": "2024-08-19", "peak_price": 3435.0, "drawdown_after_peak_pct": -31.88, "green_lateness_ratio": null, "four_b_local_peak_proximity": "local_4b_watch_after_trial_data_or_platform_peak_if_endpoint_partner_or_regulatory_bridge_fades", "four_b_full_window_peak_proximity": "full_4b_requires_non_price_endpoint_failure_safety_signal_regulatory_rejection_financing_or_commercialization_break", "trigger_outcome_label": "counterexample_trial_beta_local4b_post_ca", "current_profile_verdict": "C24 should not treat oncology-trial or financing/post-CA bio beta as durable Stage2 unless endpoint quality, safety, regulatory path, financing runway and commercialization bridge are visible. SillaJen had only a small MFE after the post-CA entry and then opened a high-MAE decline.", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window_by_profile_or_post_CA_entry", "share_count_change_inside_window": false, "same_entry_group_id": "C24_BIO_TRIAL_215600_2024-07-10", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 0.5, "do_not_count_as_new_case": false, "source_proxy_only": true, "evidence_url_pending": true}
```

### score simulation rows

```jsonl
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R7L76-C24-298380-ABL-BIO-BISPECIFIC-ADC-TRIAL-DATA-BRIDGE", "trigger_id": "TRG_R7L76-C24-298380-ABL-BIO-BISPECIFIC-ADC-TRIAL-DATA-BRIDGE", "symbol": "298380", "large_sector_id": "L7_BIO_HEALTHCARE_MEDICAL", "canonical_archetype_id": "C24_BIO_TRIAL_DATA_EVENT_RISK", "raw_component_scores_before": {"trial_data_quality_score": 14, "endpoint_safety_score": 12, "partner_validation_score": 14, "regulatory_path_score": 11, "commercialization_bridge_score": 10, "relative_strength_score": 15, "corporate_action_or_financing_risk": 0, "execution_risk_score": 8, "source_confidence_score": 2}, "weighted_score_before": 78, "stage_label_before": "Stage2 candidate after source repair and CA validation", "raw_component_scores_after": {"trial_data_quality_score": 16, "endpoint_safety_score": 14, "partner_validation_score": 16, "regulatory_path_score": 13, "commercialization_bridge_score": 12, "relative_strength_score": 14, "corporate_action_or_financing_risk": 0, "execution_risk_score": 9, "source_confidence_score": 2}, "weighted_score_after": 84, "stage_label_after": "Stage2/Yellow candidate after source repair + lifecycle 4B", "changed_components": ["trial_data_quality_score", "endpoint_safety_score", "partner_validation_score", "regulatory_path_score", "execution_risk_score"], "component_delta_explanation": "Reward only verified clinical endpoint/safety, partner validation, regulatory path and commercialization bridge; cap bio clinical beta when endpoint/regulatory/financing bridge is weak or stale.", "MFE_90D_pct": 41.86, "MAE_90D_pct": -0.23, "score_return_alignment_label": "trial_data_platform_positive_with_lifecycle_4b", "current_profile_verdict": "C24 should allow a trial-data/platform-event Stage2 when clinical data, partner validation, differentiated modality and downstream commercialization bridge are visible. ABL Bio produced high MFE with almost no entry-basis MAE, but later post-peak fading still requires lifecycle local 4B if clinical/partner bridge evidence goes stale."}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R7L76-C24-141080-LIGACHEM-ADC-TRIAL-DATA-POST-CA-LIFECYCLE", "trigger_id": "TRG_R7L76-C24-141080-LIGACHEM-ADC-TRIAL-DATA-POST-CA-LIFECYCLE", "symbol": "141080", "large_sector_id": "L7_BIO_HEALTHCARE_MEDICAL", "canonical_archetype_id": "C24_BIO_TRIAL_DATA_EVENT_RISK", "raw_component_scores_before": {"trial_data_quality_score": 14, "endpoint_safety_score": 12, "partner_validation_score": 14, "regulatory_path_score": 11, "commercialization_bridge_score": 10, "relative_strength_score": 15, "corporate_action_or_financing_risk": 10, "execution_risk_score": 8, "source_confidence_score": 2}, "weighted_score_before": 78, "stage_label_before": "Stage2 candidate after source repair and CA validation", "raw_component_scores_after": {"trial_data_quality_score": 16, "endpoint_safety_score": 14, "partner_validation_score": 16, "regulatory_path_score": 13, "commercialization_bridge_score": 12, "relative_strength_score": 14, "corporate_action_or_financing_risk": 12, "execution_risk_score": 9, "source_confidence_score": 2}, "weighted_score_after": 84, "stage_label_after": "Stage2/Yellow candidate after source repair + lifecycle 4B", "changed_components": ["trial_data_quality_score", "endpoint_safety_score", "partner_validation_score", "regulatory_path_score", "execution_risk_score"], "component_delta_explanation": "Reward only verified clinical endpoint/safety, partner validation, regulatory path and commercialization bridge; cap bio clinical beta when endpoint/regulatory/financing bridge is weak or stale.", "MFE_90D_pct": 45.44, "MAE_90D_pct": -10.88, "score_return_alignment_label": "trial_data_platform_positive_with_lifecycle_4b", "current_profile_verdict": "C24 should allow ADC-platform trial-data / partner-validation positives only after corporate-action windows are handled. LigaChem Bio had a 2024-04-23 corporate-action candidate, so the post-CA entry is deliberately 2024-04-24; the post-entry path produced very large MFE, but requires source repair and CA validation before runtime promotion."}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R7L76-C24-215600-SILLAJEN-ONCOLOGY-TRIAL-DATA-POST-CA-BETA-FADE", "trigger_id": "TRG_R7L76-C24-215600-SILLAJEN-ONCOLOGY-TRIAL-DATA-POST-CA-BETA-FADE", "symbol": "215600", "large_sector_id": "L7_BIO_HEALTHCARE_MEDICAL", "canonical_archetype_id": "C24_BIO_TRIAL_DATA_EVENT_RISK", "raw_component_scores_before": {"trial_data_quality_score": 4, "endpoint_safety_score": 3, "partner_validation_score": 2, "regulatory_path_score": 2, "commercialization_bridge_score": 1, "relative_strength_score": 5, "corporate_action_or_financing_risk": 10, "execution_risk_score": 20, "source_confidence_score": 2}, "weighted_score_before": 48, "stage_label_before": "Stage2-FalsePositive / local 4B-watch", "raw_component_scores_after": {"trial_data_quality_score": 2, "endpoint_safety_score": 1, "partner_validation_score": 1, "regulatory_path_score": 1, "commercialization_bridge_score": 1, "relative_strength_score": 3, "corporate_action_or_financing_risk": 12, "execution_risk_score": 22, "source_confidence_score": 2}, "weighted_score_after": 36, "stage_label_after": "Stage4B-local-watch / no durable Green", "changed_components": ["trial_data_quality_score", "endpoint_safety_score", "partner_validation_score", "regulatory_path_score", "execution_risk_score"], "component_delta_explanation": "Reward only verified clinical endpoint/safety, partner validation, regulatory path and commercialization bridge; cap bio clinical beta when endpoint/regulatory/financing bridge is weak or stale.", "MFE_90D_pct": 7.34, "MAE_90D_pct": -18.44, "score_return_alignment_label": "false_positive_clinical_beta_bridge_gap", "current_profile_verdict": "C24 should not treat oncology-trial or financing/post-CA bio beta as durable Stage2 unless endpoint quality, safety, regulatory path, financing runway and commercialization bridge are visible. SillaJen had only a small MFE after the post-CA entry and then opened a high-MAE decline."}
```

### aggregate row

```jsonl
{"row_type": "aggregate", "round": "R7", "loop": 76, "large_sector_id": "L7_BIO_HEALTHCARE_MEDICAL", "canonical_archetype_id": "C24_BIO_TRIAL_DATA_EVENT_RISK", "fine_archetype_id": "BISPECIFIC_ADC_ONCOLOGY_TRIAL_DATA_EVENT_BRIDGE_VS_CLINICAL_BETA_FADE", "calibration_usable_case_count": 3, "calibration_usable_trigger_count": 3, "new_independent_case_count": 3, "reused_case_count": 0, "same_archetype_new_symbol_count": 3, "same_archetype_new_trigger_family_count": 3, "positive_case_count": 2, "counterexample_count": 1, "four_b_case_count": 3, "four_c_case_count": 0, "source_proxy_only_count": 3, "evidence_url_pending_count": 3, "share_count_change_inside_window_count": 1, "corporate_action_post_entry_validation_count": 2, "current_profile_error_count": 1, "diversity_score_summary": "+3 C24 biotech symbols outside top-covered 000100/028300/009420/039200 set, +3 bispecific/ADC/oncology trial-data trigger families, +2 platform-data positives, +1 post-CA clinical beta fade counterexample, no hard duplicate", "residual_contribution_label": "coverage_gap_fill_with_source_repair_and_corporate_action_validation_needed"}
```

### shadow weight row

```jsonl
{"row_type": "shadow_weight", "round": "R7", "loop": 76, "large_sector_id": "L7_BIO_HEALTHCARE_MEDICAL", "canonical_archetype_id": "C24_BIO_TRIAL_DATA_EVENT_RISK", "axis": "bispecific_adc_oncology_trial_data_event_bridge_vs_clinical_beta_fade", "decision": "hold_for_source_repair_and_more_evidence", "proposed_runtime_effect": "C24 should split verified trial-data / platform-event positives from generic clinical beta. Stage2 requires endpoint quality, safety, partner validation, regulatory path, financing runway or commercialization bridge. Post-CA entries require explicit validation. If MAE widens or post-peak drawdown opens without bridge refresh, route to local 4B-watch.", "do_not_propose_new_weight_delta": true, "needs_more_evidence": true, "source_repair_required": ["298380", "141080", "215600"], "corporate_action_validation_required": ["141080", "215600"]}
```

### residual contribution row

```jsonl
{"row_type": "residual_contribution", "round": "R7", "loop": 76, "large_sector_id": "L7_BIO_HEALTHCARE_MEDICAL", "canonical_archetype_id": "C24_BIO_TRIAL_DATA_EVENT_RISK", "existing_axis_strengthened": ["stage2_required_bridge", "price_only_blowoff_blocks_positive_stage", "local_4b_watch_guard", "full_4b_requires_non_price_evidence", "corporate_action_validation_guard"], "new_axis_proposed": null, "sector_specific_rule_candidate": true, "canonical_archetype_rule_candidate": true, "narrative_summary": "C24 needs trial-data and regulatory/commercial bridge proof. ABL Bio and LigaChem Bio show bispecific/ADC platform positives after source repair; SillaJen shows oncology clinical beta fading into local 4B when endpoint/regulatory/financing bridge is absent."}
```

---

## Validation scope

```text
price_source = Songdaiki/stock-web
price_basis = tradable_raw
price_adjustment_status = raw_unadjusted_marcap
manifest_max_date = 2026-02-20
forward_window_basis = stock_web_manifest_max_date
all_selected_entry_dates_present_in_tradable_shards = true
all_selected_180D_windows_available = true
production_scoring_changed = false
shadow_weight_only = true
```

Profile checks:

```text
298380:
  corporate_action_candidate_dates = none
  selected window = 2024-02-23~D+180
  contamination = false

141080:
  name = 레고켐바이오 until 2024-04-18, 리가켐바이오 from 2024-04-19
  corporate_action_candidate_dates = 2020-07-07, 2024-04-23
  selected window starts 2024-04-24 after 2024-04-23 candidate
  contamination = false after post-CA entry, but coding-agent validation required

215600:
  corporate_action_candidate_dates = 2022-10-13, 2024-07-09
  selected window starts 2024-07-10 after 2024-07-09 candidate
  contamination = false after post-CA entry
```

Data-quality caveat:

```text
All selected C24 rows are source_proxy_only / evidence_url_pending.
141080 and 215600 also require explicit post-corporate-action validation before runtime promotion.
This MD is useful for stock-web path calibration and C24 rule-shape discovery,
but coding-agent promotion requires non-proxy endpoint quality, safety, regulatory path, partner validation, financing runway and commercialization evidence.
```

---

## Deferred Coding Agent Handoff Prompt

Do not execute this now.

```text
You are the coding agent for Songdaiki/stock_agent.

Read this standalone v12 residual research MD and ingest machine-readable rows only after validation.

Do not patch production scoring blindly.
This R7/C24 artifact is marked do_not_propose_new_weight_delta=true because all rows need source repair and two rows require post-CA validation.

Candidate axis:
bispecific_adc_oncology_trial_data_event_bridge_vs_clinical_beta_fade

Required checks before implementation:
1. Validate all trigger rows against stock-web tradable_raw OHLC shards.
2. Confirm no hard duplicate key:
   canonical_archetype_id + symbol + trigger_type + entry_date.
3. Verify non-proxy source URLs for 298380, 141080 and 215600.
4. Validate post-CA continuity for 141080 and 215600.
5. Keep generic C24 bio-trial beta weight unchanged until source repair is complete.
6. Consider Stage2 only when:
   - clinical/trial data event is explicit,
   - endpoint quality and safety are visible,
   - partner validation, regulatory path or commercialization bridge exists,
   - financing runway is sufficient,
   - MAE remains controlled or the signal is lifecycle-managed.
7. Consider local 4B-watch when:
   - the trigger is clinical/trial-data beta only,
   - endpoint/regulatory/commercial bridge is weak or stale,
   - MAE_90D <= -20% or MAE_180D <= -25%,
   - post-peak drawdown <= -30~35%.
8. Do not convert local 4B-watch into full 4B/4C without non-price endpoint failure, safety signal, regulatory rejection, funding failure, trial halt or commercialization break.
9. Emit before/after diagnostics and reject if verified endpoint/partner-validation positives are overblocked.
```

---

## Final round state

```text
completed_round = R7
completed_loop = 76
next_round = R8
next_loop = 76
round_schedule_status = valid
round_sector_consistency = pass
```

