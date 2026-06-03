# E2R Stock-Web v12 Residual Research — R7 Loop 78 / L7 / C24

## Metadata

```json
{
  "research_session": "post_calibrated_sector_archetype_residual_research",
  "mode": "historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12",
  "scheduled_round": "R7",
  "scheduled_loop": 78,
  "round_schedule_status": "valid",
  "round_sector_consistency": "pass",
  "completed_round": "R7",
  "completed_loop": 78,
  "computed_next_round": "R8",
  "computed_next_loop": 78,
  "large_sector_id": "L7_BIO_HEALTHCARE_MEDICAL",
  "canonical_archetype_id": "C24_BIO_TRIAL_DATA_EVENT_RISK",
  "fine_archetype_id": "ADC_RADIOPHARMA_IMMUNO_ONCOLOGY_DATA_BRIDGE_VS_BIO_DATA_EVENT_FADE",
  "loop_objective": [
    "coverage_gap_fill",
    "counterexample_mining",
    "4B_non_price_requirement_stress_test",
    "bio_trial_data_event_guardrail",
    "clinical_data_partnering_commercialization_bridge",
    "binary_data_event_local4b_boundary",
    "source_repair_queue_creation",
    "share_count_validation_queue_creation",
    "post_corporate_action_validation_queue_creation"
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

Previous completed state in this interactive run: R6 / loop 78.

Therefore:

```text
scheduled_round = R7
scheduled_loop = 78
allowed_large_sector = L7_BIO_HEALTHCARE_MEDICAL
selected_large_sector = L7_BIO_HEALTHCARE_MEDICAL
selected_canonical_archetype_id = C24_BIO_TRIAL_DATA_EVENT_RISK
computed_next_round = R8
computed_next_loop = 78
```

R7 was routed to C24 because loop 77 used C25.  
This file tests bio trial-data / regulatory / partner-commercialization risk rather than medical-device export reimbursement.

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
141080 / 리가켐바이오 / post-CA ADC data-partnering lifecycle candidate
220100 / 퓨쳐켐 / radiopharma clinical-data lifecycle candidate
950220 / 네오이뮨텍 / immuno-oncology data-event fade
```

Data-quality note:

```text
All three rows are stock-web calibration usable by profile-level corporate-action candidates.
All three rows are source_proxy_only=true / evidence_url_pending=true.
141080 has a 2024-04-23 corporate-action candidate; selected entry starts 2024-04-24 after that date.
141080 also has share-count changes inside the selected window and requires coding-agent validation before runtime promotion.
```

## Research thesis

C24 is not “바이오 임상 뉴스가 떴다.”

The mechanism must pass through:

```text
clinical / trial / data event
→ endpoint quality and efficacy-safety read-through
→ regulatory or partner validation
→ financing runway
→ commercialization or milestone bridge
→ durable rerating
```

바이오 데이터는 불꽃이다.  
C24가 보려는 것은 그 불꽃이 실제 endpoint, 규제 경로, 파트너 검증, 자금 런웨이, 상업화 다리로 번지는지다.

---

## Case 1 — Positive after CA validation: 141080 / 리가켐바이오

### Evidence status

```text
source_proxy_only = true
evidence_url_pending = true
post_corporate_action_validation_required = true
share_count_validation_required = true
source_repair_required = true
```

The source-repair task is ADC trial-data quality, partner/program validation, milestone economics and financing runway evidence.

```text
evidence_family = ADC_PLATFORM_TRIAL_DATA_PARTNERING_PROGRAM_VISIBILITY_CASH_RUNWAY_BRIDGE_POST_CA
case_role = positive_with_post_CA_sharecount_validation_and_later_4b_watch
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
2024-06-20,68200,77400,67700,75500
2024-08-29,96900,99500,94300,94800
2024-10-22,130700,139600,127100,130700
2024-11-04,117400,133900,114600,130100
```

### Backtest

```text
MFE_30D  = +5.59%
MAE_30D  = -10.88%
MFE_90D  = +46.32%
MAE_90D  = -10.88%
MFE_180D = +105.29%
MAE_180D = -10.88%
peak_180 = 139,600 on 2024-10-22
trough_180 = 60,600 on 2024-05-30
peak_to_later_drawdown = -17.91%
```

### Interpretation

This is a C24 data/partnering lifecycle positive after validation.  
The price path validates a strong post-CA MFE candidate, but runtime promotion must wait for source repair and share-count continuity checks.

Correct treatment:

```text
verified endpoint / partner / milestone / financing bridge → Stage2 possible
post-CA and share-count validation first
bridge stale after peak → local 4B-watch
```

---

## Case 2 — Positive with lifecycle 4B: 220100 / 퓨쳐켐

### Evidence status

```text
source_proxy_only = true
evidence_url_pending = true
source_repair_required = true
```

The source-repair task is radiopharma clinical-data quality, regulatory route, patient/enrollment progress, partner route and commercialization bridge evidence.

```text
evidence_family = RADIOPHARMA_CLINICAL_DATA_REGULATORY_PROGRAM_PARTNERING_COMMERCIALIZATION_BRIDGE
case_role = positive_with_later_4b_watch
trigger_date = 2024-01-31
entry_date = 2024-02-01
entry_price = 8,500
```

### Stock-Web price path

Observed rows from `atlas/ohlcv_tradable_by_symbol_year/220/220100/2024.csv`:

```text
2024-02-01,8500,8750,8250,8320
2024-02-06,8050,8880,7960,8230
2024-03-13,10420,10860,9970,10100
2024-05-30,15620,17270,15410,16990
2024-07-18,23450,25400,21300,21750
2024-10-16,30250,31250,29750,30200
2024-11-01,23100,24100,22000,22000
```

### Backtest

```text
MFE_30D  = +27.76%
MAE_30D  = -6.35%
MFE_90D  = +103.18%
MAE_90D  = -6.35%
MFE_180D = +267.65%
MAE_180D = -6.35%
peak_180 = 31,250 on 2024-10-16
trough_180 = 7,960 on 2024-02-06
peak_to_later_drawdown = -29.60%
```

### Interpretation

This is a C24 clinical-data positive.  
The MFE was explosive while the entry-basis MAE stayed controlled.

Correct treatment:

```text
verified clinical-data / regulatory / partner-commercial bridge → Stage2 possible
bridge stale after peak → lifecycle local 4B-watch
```

---

## Case 3 — Counterexample / local 4B: 950220 / 네오이뮨텍

### Evidence status

```text
source_proxy_only = true
evidence_url_pending = true
source_repair_required = true
```

This row tests immuno-oncology data-event beta without enough efficacy/safety, endpoint, financing and commercialization bridge.

```text
evidence_family = IMMUNO_ONCOLOGY_TRIAL_DATA_THEME_WITH_WEAK_EFFICACY_FINANCING_COMMERCIAL_BRIDGE
case_role = counterexample_immuno_oncology_data_local4b
trigger_date = 2024-01-31
entry_date = 2024-02-01
entry_price = 1,600
```

### Stock-Web price path

Observed rows from `atlas/ohlcv_tradable_by_symbol_year/950/950220/2024.csv`:

```text
2024-02-01,1600,1620,1568,1595
2024-02-28,1750,1806,1693,1708
2024-03-25,1879,1977,1811,1878
2024-04-09,1505,1505,1425,1447
2024-08-05,1443,1563,1200,1340
2024-09-09,1343,1745,1338,1745
2024-11-01,1425,1443,1370,1392
```

### Backtest

```text
MFE_30D  = +12.88%
MAE_30D  = -3.75%
MFE_90D  = +23.56%
MAE_90D  = -10.94%
MFE_180D = +23.56%
MAE_180D = -25.00%
peak_180 = 1,977 on 2024-03-25
trough_180 = 1,200 on 2024-08-05
peak_to_later_drawdown = -39.30%
```

### Interpretation

This is a C24 false-positive boundary.  
The first data-event MFE was tradable, but it did not become durable rerating.

Correct treatment:

```text
immuno-oncology data-event beta
→ no verified endpoint / financing / commercialization bridge
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
post_corporate_action_validation_guard = strengthen
share_count_validation_guard = strengthen
```

### What this does not justify

```text
do_not_raise_generic_C24_bio_data_event_weight = true
do_not_treat_all_bio_data_MFE_as_Green = true
do_not_convert_bio_data_drawdown_to_hard_4C_without_non_price_trial_regulatory_financing_or_safety_break = true
```

### Candidate canonical compression

Fine labels can compress into:

```text
ADC_RADIOPHARMA_IMMUNO_ONCOLOGY_DATA_BRIDGE_VS_BIO_DATA_EVENT_FADE
```

This fine archetype covers:

```text
1. ADC data/partnering bridge after CA validation → Stage2 possible after source repair
2. radiopharma clinical-data/commercial route bridge → Stage2 possible, lifecycle-managed
3. immuno-oncology data-event beta without endpoint/financing bridge → false Stage2 / local 4B
```

---

## Machine-readable rows

### price source validation row

```jsonl
{"row_type": "price_source_validation", "source": "Songdaiki/stock-web", "source_url": "https://github.com/Songdaiki/stock-web", "manifest_path": "atlas/manifest.json", "schema_path": "atlas/schema.json", "universe_path": "atlas/universe/all_symbols.csv", "manifest_max_date": "2026-02-20", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "raw_shard_root": "atlas/ohlcv_raw_by_symbol_year", "validation_status": "usable_for_historical_calibration"}
```

### case rows

```jsonl
{"row_type": "case", "case_id": "R7L78-C24-141080-LIGACHEM-ADC-DATA-PARTNERING-POST-CA", "symbol": "141080", "company_name": "리가켐바이오", "round": "R7", "loop": "78", "large_sector_id": "L7_BIO_HEALTHCARE_MEDICAL", "canonical_archetype_id": "C24_BIO_TRIAL_DATA_EVENT_RISK", "fine_archetype_id": "ADC_RADIOPHARMA_IMMUNO_ONCOLOGY_DATA_BRIDGE_VS_BIO_DATA_EVENT_FADE", "case_type": "bio_trial_data_event_risk", "positive_or_counterexample": "positive", "best_trigger": "Stage2-Actionable-PostCAADCDataPartneringBridgeWithLifecycle4B", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 0.5, "score_price_alignment": "C24 should allow ADC/platform positives only when trial-data quality, partner validation, named program visibility, milestone economics and cash runway bridge are visible. LigaChem Bio produced very large MFE after the 2024-04-23 corporate-action/share-count discontinuity; runtime promotion requires post-CA and share-count validation.", "current_profile_verdict": "source_repair_required_before_runtime_weight", "price_source": "Songdaiki/stock-web", "notes": "Stock-web path usable; non-proxy efficacy/safety, endpoint quality, regulatory route, partner/commercial bridge, financing runway and trial-data source evidence required before runtime promotion."}
{"row_type": "case", "case_id": "R7L78-C24-220100-FUTURECHEM-RADIOPHARMA-TRIAL-DATA", "symbol": "220100", "company_name": "퓨쳐켐", "round": "R7", "loop": "78", "large_sector_id": "L7_BIO_HEALTHCARE_MEDICAL", "canonical_archetype_id": "C24_BIO_TRIAL_DATA_EVENT_RISK", "fine_archetype_id": "ADC_RADIOPHARMA_IMMUNO_ONCOLOGY_DATA_BRIDGE_VS_BIO_DATA_EVENT_FADE", "case_type": "bio_trial_data_event_risk", "positive_or_counterexample": "positive", "best_trigger": "Stage2-Actionable-RadiopharmaTrialDataCommercialBridgeWithLifecycle4B", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 0.5, "score_price_alignment": "C24 should preserve radiopharma positives when clinical-data quality, regulatory path, patient enrollment, partner/commercial route and financing bridge are visible. FutureChem produced very large MFE with controlled entry-basis MAE, but post-peak volatility still requires lifecycle local 4B if data/commercial bridge decays.", "current_profile_verdict": "source_repair_required_before_runtime_weight", "price_source": "Songdaiki/stock-web", "notes": "Stock-web path usable; non-proxy efficacy/safety, endpoint quality, regulatory route, partner/commercial bridge, financing runway and trial-data source evidence required before runtime promotion."}
{"row_type": "case", "case_id": "R7L78-C24-950220-NEOIMMUNETECH-IMMUNO-ONCOLOGY-DATA-FADE", "symbol": "950220", "company_name": "네오이뮨텍", "round": "R7", "loop": "78", "large_sector_id": "L7_BIO_HEALTHCARE_MEDICAL", "canonical_archetype_id": "C24_BIO_TRIAL_DATA_EVENT_RISK", "fine_archetype_id": "ADC_RADIOPHARMA_IMMUNO_ONCOLOGY_DATA_BRIDGE_VS_BIO_DATA_EVENT_FADE", "case_type": "bio_trial_data_event_risk", "positive_or_counterexample": "counterexample", "best_trigger": "Stage2-FalsePositive / ImmunoOncologyDataEventFade", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 0.5, "score_price_alignment": "C24 should not treat immuno-oncology trial-data theme beta as durable Stage2 unless efficacy/safety, endpoint quality, regulatory path, financing runway and commercialization bridge are visible. NeoImmuneTech had a tradable spike but no durable rerating and then a broad drawdown path.", "current_profile_verdict": "source_repair_required_before_runtime_weight", "price_source": "Songdaiki/stock-web", "notes": "Stock-web path usable; non-proxy efficacy/safety, endpoint quality, regulatory route, partner/commercial bridge, financing runway and trial-data source evidence required before runtime promotion."}
```

### trigger rows

```jsonl
{"row_type": "trigger", "trigger_id": "TRG_R7L78-C24-141080-LIGACHEM-ADC-DATA-PARTNERING-POST-CA", "case_id": "R7L78-C24-141080-LIGACHEM-ADC-DATA-PARTNERING-POST-CA", "symbol": "141080", "company_name": "리가켐바이오", "round": "R7", "loop": "78", "large_sector_id": "L7_BIO_HEALTHCARE_MEDICAL", "canonical_archetype_id": "C24_BIO_TRIAL_DATA_EVENT_RISK", "fine_archetype_id": "ADC_RADIOPHARMA_IMMUNO_ONCOLOGY_DATA_BRIDGE_VS_BIO_DATA_EVENT_FADE", "loop_objective": "coverage_gap_fill|counterexample_mining|bio_trial_data_event_guardrail", "trigger_type": "Stage2-Actionable-PostCAADCDataPartneringBridgeWithLifecycle4B", "trigger_date": "2024-04-23", "entry_date": "2024-04-24", "entry_price": 68000.0, "evidence_available_at_that_date": "ADC_PLATFORM_TRIAL_DATA_PARTNERING_PROGRAM_VISIBILITY_CASH_RUNWAY_BRIDGE_POST_CA", "evidence_source": "source_proxy_manual_verification_required:LIGACHEM_BIO_2024_ADC_TRIAL_DATA_PARTNER_PROGRAM_MILESTONE_CASH_RUNWAY_BRIDGE_POST_CA", "stage2_evidence_fields": ["clinical_data_quality_candidate", "regulatory_or_partner_bridge_candidate", "financing_runway_candidate"], "stage3_evidence_fields": ["relative_strength", "commercialization_or_program_visibility_candidate"], "stage4b_evidence_fields": ["bio_data_event_beta", "bridge_stale_or_absent", "MAE_widening", "post_peak_drawdown"], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/141/141080/2024.csv", "profile_path": "atlas/symbol_profiles/141/141080.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": 5.59, "MFE_90D_pct": 46.32, "MFE_180D_pct": 105.29, "MAE_30D_pct": -10.88, "MAE_90D_pct": -10.88, "MAE_180D_pct": -10.88, "peak_date": "2024-10-22", "peak_price": 139600.0, "drawdown_after_peak_pct": -17.91, "green_lateness_ratio": null, "four_b_local_peak_proximity": "local_4b_watch_after_bio_data_peak_if_endpoint_regulatory_financing_or_commercial_bridge_fades", "four_b_full_window_peak_proximity": "full_4b_requires_non_price_trial_failure_regulatory_setback_financing_break_partner_loss_or_safety_signal", "trigger_outcome_label": "positive_with_post_CA_sharecount_validation_and_later_4b_watch", "current_profile_verdict": "C24 should allow ADC/platform positives only when trial-data quality, partner validation, named program visibility, milestone economics and cash runway bridge are visible. LigaChem Bio produced very large MFE after the 2024-04-23 corporate-action/share-count discontinuity; runtime promotion requires post-CA and share-count validation.", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_or_post_CA_validation_required", "share_count_change_inside_window": true, "same_entry_group_id": "C24_BIO_DATA_141080_2024-04-24", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 0.5, "do_not_count_as_new_case": false, "source_proxy_only": true, "evidence_url_pending": true}
{"row_type": "trigger", "trigger_id": "TRG_R7L78-C24-220100-FUTURECHEM-RADIOPHARMA-TRIAL-DATA", "case_id": "R7L78-C24-220100-FUTURECHEM-RADIOPHARMA-TRIAL-DATA", "symbol": "220100", "company_name": "퓨쳐켐", "round": "R7", "loop": "78", "large_sector_id": "L7_BIO_HEALTHCARE_MEDICAL", "canonical_archetype_id": "C24_BIO_TRIAL_DATA_EVENT_RISK", "fine_archetype_id": "ADC_RADIOPHARMA_IMMUNO_ONCOLOGY_DATA_BRIDGE_VS_BIO_DATA_EVENT_FADE", "loop_objective": "coverage_gap_fill|counterexample_mining|bio_trial_data_event_guardrail", "trigger_type": "Stage2-Actionable-RadiopharmaTrialDataCommercialBridgeWithLifecycle4B", "trigger_date": "2024-01-31", "entry_date": "2024-02-01", "entry_price": 8500.0, "evidence_available_at_that_date": "RADIOPHARMA_CLINICAL_DATA_REGULATORY_PROGRAM_PARTNERING_COMMERCIALIZATION_BRIDGE", "evidence_source": "source_proxy_manual_verification_required:FUTURECHEM_2024_RADIOPHARMA_TRIAL_DATA_REGULATORY_PARTNER_COMMERCIALIZATION_BRIDGE", "stage2_evidence_fields": ["clinical_data_quality_candidate", "regulatory_or_partner_bridge_candidate", "financing_runway_candidate"], "stage3_evidence_fields": ["relative_strength", "commercialization_or_program_visibility_candidate"], "stage4b_evidence_fields": ["bio_data_event_beta", "bridge_stale_or_absent", "MAE_widening", "post_peak_drawdown"], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/220/220100/2024.csv", "profile_path": "atlas/symbol_profiles/220/220100.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": 27.76, "MFE_90D_pct": 103.18, "MFE_180D_pct": 267.65, "MAE_30D_pct": -6.35, "MAE_90D_pct": -6.35, "MAE_180D_pct": -6.35, "peak_date": "2024-10-16", "peak_price": 31250.0, "drawdown_after_peak_pct": -29.6, "green_lateness_ratio": null, "four_b_local_peak_proximity": "local_4b_watch_after_bio_data_peak_if_endpoint_regulatory_financing_or_commercial_bridge_fades", "four_b_full_window_peak_proximity": "full_4b_requires_non_price_trial_failure_regulatory_setback_financing_break_partner_loss_or_safety_signal", "trigger_outcome_label": "positive_with_later_4b_watch", "current_profile_verdict": "C24 should preserve radiopharma positives when clinical-data quality, regulatory path, patient enrollment, partner/commercial route and financing bridge are visible. FutureChem produced very large MFE with controlled entry-basis MAE, but post-peak volatility still requires lifecycle local 4B if data/commercial bridge decays.", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_or_post_CA_validation_required", "share_count_change_inside_window": false, "same_entry_group_id": "C24_BIO_DATA_220100_2024-02-01", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 0.5, "do_not_count_as_new_case": false, "source_proxy_only": true, "evidence_url_pending": true}
{"row_type": "trigger", "trigger_id": "TRG_R7L78-C24-950220-NEOIMMUNETECH-IMMUNO-ONCOLOGY-DATA-FADE", "case_id": "R7L78-C24-950220-NEOIMMUNETECH-IMMUNO-ONCOLOGY-DATA-FADE", "symbol": "950220", "company_name": "네오이뮨텍", "round": "R7", "loop": "78", "large_sector_id": "L7_BIO_HEALTHCARE_MEDICAL", "canonical_archetype_id": "C24_BIO_TRIAL_DATA_EVENT_RISK", "fine_archetype_id": "ADC_RADIOPHARMA_IMMUNO_ONCOLOGY_DATA_BRIDGE_VS_BIO_DATA_EVENT_FADE", "loop_objective": "coverage_gap_fill|counterexample_mining|bio_trial_data_event_guardrail", "trigger_type": "Stage2-FalsePositive / ImmunoOncologyDataEventFade", "trigger_date": "2024-01-31", "entry_date": "2024-02-01", "entry_price": 1600.0, "evidence_available_at_that_date": "IMMUNO_ONCOLOGY_TRIAL_DATA_THEME_WITH_WEAK_EFFICACY_FINANCING_COMMERCIAL_BRIDGE", "evidence_source": "source_proxy_manual_verification_required:NEOIMMUNETECH_2024_IMMUNO_ONCOLOGY_TRIAL_DATA_EFFICACY_SAFETY_FINANCING_COMMERCIAL_BRIDGE", "stage2_evidence_fields": ["clinical_data_quality_candidate", "regulatory_or_partner_bridge_candidate", "financing_runway_candidate"], "stage3_evidence_fields": ["relative_strength", "commercialization_or_program_visibility_candidate"], "stage4b_evidence_fields": ["bio_data_event_beta", "bridge_stale_or_absent", "MAE_widening", "post_peak_drawdown"], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/950/950220/2024.csv", "profile_path": "atlas/symbol_profiles/950/950220.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": 12.88, "MFE_90D_pct": 23.56, "MFE_180D_pct": 23.56, "MAE_30D_pct": -3.75, "MAE_90D_pct": -10.94, "MAE_180D_pct": -25.0, "peak_date": "2024-03-25", "peak_price": 1977.0, "drawdown_after_peak_pct": -39.3, "green_lateness_ratio": null, "four_b_local_peak_proximity": "local_4b_watch_after_bio_data_peak_if_endpoint_regulatory_financing_or_commercial_bridge_fades", "four_b_full_window_peak_proximity": "full_4b_requires_non_price_trial_failure_regulatory_setback_financing_break_partner_loss_or_safety_signal", "trigger_outcome_label": "counterexample_immuno_oncology_data_local4b", "current_profile_verdict": "C24 should not treat immuno-oncology trial-data theme beta as durable Stage2 unless efficacy/safety, endpoint quality, regulatory path, financing runway and commercialization bridge are visible. NeoImmuneTech had a tradable spike but no durable rerating and then a broad drawdown path.", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_or_post_CA_validation_required", "share_count_change_inside_window": false, "same_entry_group_id": "C24_BIO_DATA_950220_2024-02-01", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 0.5, "do_not_count_as_new_case": false, "source_proxy_only": true, "evidence_url_pending": true}
```

### score simulation rows

```jsonl
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R7L78-C24-141080-LIGACHEM-ADC-DATA-PARTNERING-POST-CA", "trigger_id": "TRG_R7L78-C24-141080-LIGACHEM-ADC-DATA-PARTNERING-POST-CA", "symbol": "141080", "large_sector_id": "L7_BIO_HEALTHCARE_MEDICAL", "canonical_archetype_id": "C24_BIO_TRIAL_DATA_EVENT_RISK", "raw_component_scores_before": {"clinical_data_quality_score": 15, "endpoint_regulatory_score": 14, "partner_or_commercial_bridge_score": 13, "financing_runway_score": 12, "relative_strength_score": 15, "execution_risk_score": 9, "post_CA_or_sharecount_validation_risk": 10, "source_confidence_score": 2}, "weighted_score_before": 80, "stage_label_before": "Stage2 candidate after source repair", "raw_component_scores_after": {"clinical_data_quality_score": 17, "endpoint_regulatory_score": 16, "partner_or_commercial_bridge_score": 15, "financing_runway_score": 14, "relative_strength_score": 14, "execution_risk_score": 10, "post_CA_or_sharecount_validation_risk": 12, "source_confidence_score": 2}, "weighted_score_after": 86, "stage_label_after": "Stage2/Yellow-Green after source repair + lifecycle 4B", "changed_components": ["clinical_data_quality_score", "endpoint_regulatory_score", "partner_or_commercial_bridge_score", "financing_runway_score", "execution_risk_score"], "component_delta_explanation": "Reward only verified clinical data quality, endpoint/regulatory path, partner or commercial bridge and financing runway; cap bio data-event beta when evidence fails to refresh.", "MFE_90D_pct": 46.32, "MAE_90D_pct": -10.88, "score_return_alignment_label": "bio_trial_data_positive_with_lifecycle_4b", "current_profile_verdict": "C24 should allow ADC/platform positives only when trial-data quality, partner validation, named program visibility, milestone economics and cash runway bridge are visible. LigaChem Bio produced very large MFE after the 2024-04-23 corporate-action/share-count discontinuity; runtime promotion requires post-CA and share-count validation."}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R7L78-C24-220100-FUTURECHEM-RADIOPHARMA-TRIAL-DATA", "trigger_id": "TRG_R7L78-C24-220100-FUTURECHEM-RADIOPHARMA-TRIAL-DATA", "symbol": "220100", "large_sector_id": "L7_BIO_HEALTHCARE_MEDICAL", "canonical_archetype_id": "C24_BIO_TRIAL_DATA_EVENT_RISK", "raw_component_scores_before": {"clinical_data_quality_score": 15, "endpoint_regulatory_score": 14, "partner_or_commercial_bridge_score": 13, "financing_runway_score": 12, "relative_strength_score": 15, "execution_risk_score": 9, "post_CA_or_sharecount_validation_risk": 0, "source_confidence_score": 2}, "weighted_score_before": 80, "stage_label_before": "Stage2 candidate after source repair", "raw_component_scores_after": {"clinical_data_quality_score": 17, "endpoint_regulatory_score": 16, "partner_or_commercial_bridge_score": 15, "financing_runway_score": 14, "relative_strength_score": 14, "execution_risk_score": 10, "post_CA_or_sharecount_validation_risk": 0, "source_confidence_score": 2}, "weighted_score_after": 86, "stage_label_after": "Stage2/Yellow-Green after source repair + lifecycle 4B", "changed_components": ["clinical_data_quality_score", "endpoint_regulatory_score", "partner_or_commercial_bridge_score", "financing_runway_score", "execution_risk_score"], "component_delta_explanation": "Reward only verified clinical data quality, endpoint/regulatory path, partner or commercial bridge and financing runway; cap bio data-event beta when evidence fails to refresh.", "MFE_90D_pct": 103.18, "MAE_90D_pct": -6.35, "score_return_alignment_label": "bio_trial_data_positive_with_lifecycle_4b", "current_profile_verdict": "C24 should preserve radiopharma positives when clinical-data quality, regulatory path, patient enrollment, partner/commercial route and financing bridge are visible. FutureChem produced very large MFE with controlled entry-basis MAE, but post-peak volatility still requires lifecycle local 4B if data/commercial bridge decays."}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R7L78-C24-950220-NEOIMMUNETECH-IMMUNO-ONCOLOGY-DATA-FADE", "trigger_id": "TRG_R7L78-C24-950220-NEOIMMUNETECH-IMMUNO-ONCOLOGY-DATA-FADE", "symbol": "950220", "large_sector_id": "L7_BIO_HEALTHCARE_MEDICAL", "canonical_archetype_id": "C24_BIO_TRIAL_DATA_EVENT_RISK", "raw_component_scores_before": {"clinical_data_quality_score": 5, "endpoint_regulatory_score": 3, "partner_or_commercial_bridge_score": 2, "financing_runway_score": 2, "relative_strength_score": 5, "execution_risk_score": 22, "post_CA_or_sharecount_validation_risk": 0, "source_confidence_score": 2}, "weighted_score_before": 46, "stage_label_before": "Stage2-FalsePositive / local 4B-watch", "raw_component_scores_after": {"clinical_data_quality_score": 3, "endpoint_regulatory_score": 1, "partner_or_commercial_bridge_score": 1, "financing_runway_score": 1, "relative_strength_score": 3, "execution_risk_score": 24, "post_CA_or_sharecount_validation_risk": 0, "source_confidence_score": 2}, "weighted_score_after": 34, "stage_label_after": "Stage4B-local-watch / no durable Green", "changed_components": ["clinical_data_quality_score", "endpoint_regulatory_score", "partner_or_commercial_bridge_score", "financing_runway_score", "execution_risk_score"], "component_delta_explanation": "Reward only verified clinical data quality, endpoint/regulatory path, partner or commercial bridge and financing runway; cap bio data-event beta when evidence fails to refresh.", "MFE_90D_pct": 23.56, "MAE_90D_pct": -10.94, "score_return_alignment_label": "false_positive_bio_data_bridge_gap", "current_profile_verdict": "C24 should not treat immuno-oncology trial-data theme beta as durable Stage2 unless efficacy/safety, endpoint quality, regulatory path, financing runway and commercialization bridge are visible. NeoImmuneTech had a tradable spike but no durable rerating and then a broad drawdown path."}
```

### aggregate row

```jsonl
{"row_type": "aggregate", "round": "R7", "loop": 78, "large_sector_id": "L7_BIO_HEALTHCARE_MEDICAL", "canonical_archetype_id": "C24_BIO_TRIAL_DATA_EVENT_RISK", "fine_archetype_id": "ADC_RADIOPHARMA_IMMUNO_ONCOLOGY_DATA_BRIDGE_VS_BIO_DATA_EVENT_FADE", "calibration_usable_case_count": 3, "calibration_usable_trigger_count": 3, "new_independent_case_count": 3, "reused_case_count": 0, "same_archetype_new_symbol_count": 3, "same_archetype_new_trigger_family_count": 3, "positive_case_count": 2, "counterexample_count": 1, "four_b_case_count": 3, "four_c_case_count": 0, "source_proxy_only_count": 3, "evidence_url_pending_count": 3, "share_count_change_inside_window_count": 1, "post_corporate_action_validation_count": 1, "current_profile_error_count": 1, "diversity_score_summary": "+3 C24 bio trial/data symbols outside top-covered 000100/028300/009420/039200 set, +3 ADC/radiopharma/immuno-oncology trigger families, +2 clinical-data lifecycle positives, +1 immuno-oncology data-event local-4B counterexample, no hard duplicate", "residual_contribution_label": "coverage_gap_fill_with_source_repair_and_post_CA_validation_needed"}
```

### shadow weight row

```jsonl
{"row_type": "shadow_weight", "round": "R7", "loop": 78, "large_sector_id": "L7_BIO_HEALTHCARE_MEDICAL", "canonical_archetype_id": "C24_BIO_TRIAL_DATA_EVENT_RISK", "axis": "ADC_radiopharma_immuno_oncology_data_bridge_vs_bio_data_event_fade", "decision": "hold_for_source_repair_and_more_evidence", "proposed_runtime_effect": "C24 should split verified bio trial-data / regulatory / partner-commercial bridges from generic bio data-event beta. Stage2 requires efficacy/safety quality, endpoint relevance, regulatory path, partner/commercial bridge and financing runway. If MFE fades and MAE/post-peak drawdown opens without bridge refresh, route to local 4B-watch. Post-CA/share-count rows require validation before runtime promotion.", "do_not_propose_new_weight_delta": true, "needs_more_evidence": true, "source_repair_required": ["141080", "220100", "950220"], "post_corporate_action_validation_required": ["141080"], "share_count_validation_required": ["141080"]}
```

### residual contribution row

```jsonl
{"row_type": "residual_contribution", "round": "R7", "loop": 78, "large_sector_id": "L7_BIO_HEALTHCARE_MEDICAL", "canonical_archetype_id": "C24_BIO_TRIAL_DATA_EVENT_RISK", "existing_axis_strengthened": ["stage2_required_bridge", "price_only_blowoff_blocks_positive_stage", "local_4b_watch_guard", "full_4b_requires_non_price_evidence", "post_corporate_action_validation_guard", "share_count_validation_guard"], "new_axis_proposed": null, "sector_specific_rule_candidate": true, "canonical_archetype_rule_candidate": true, "narrative_summary": "C24 needs clinical-data, endpoint, regulatory, partner/commercial and financing proof. LigaChem Bio and FutureChem show data-event lifecycle MFE candidates after source repair; NeoImmuneTech shows immuno-oncology data-event beta fading into local 4B when efficacy, financing and commercialization bridge are weak."}
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
141080:
  name = 리가켐바이오 from 2024-04-19, 레고켐바이오 before that
  corporate_action_candidate_dates = 2020-07-07, 2024-04-23
  selected window starts 2024-04-24 after the 2024-04-23 candidate
  contamination = false after post-CA entry, but coding-agent validation required
  share_count_change_inside_window = true → coding-agent validation required

220100:
  name = 퓨쳐켐
  corporate_action_candidate_dates = 2015-09-02, 2016-08-26, 2016-12-01, 2020-08-18, 2022-11-03, 2022-11-11
  selected window = 2024-02-01~D+180
  contamination = false

950220:
  name = 네오이뮨텍 from 2022-03-16, 네오이뮨텍(Reg.S) before that
  corporate_action_candidate_dates = 2025-09-30
  selected window = 2024-02-01~D+180
  contamination = false
```

Data-quality caveat:

```text
All selected C24 rows are source_proxy_only / evidence_url_pending.
141080 also requires post-corporate-action and share-count validation before runtime promotion.
This MD is useful for stock-web path calibration and C24 rule-shape discovery,
but coding-agent promotion requires non-proxy clinical-data quality, endpoint relevance, regulatory path, partner/commercial bridge and financing runway evidence.
```

---

## Deferred Coding Agent Handoff Prompt

Do not execute this now.

```text
You are the coding agent for Songdaiki/stock_agent.

Read this standalone v12 residual research MD and ingest machine-readable rows only after validation.

Do not patch production scoring blindly.
This R7/C24 artifact is marked do_not_propose_new_weight_delta=true because all rows need source repair and 141080 needs post-CA/share-count validation.

Candidate axis:
ADC_radiopharma_immuno_oncology_data_bridge_vs_bio_data_event_fade

Required checks before implementation:
1. Validate all trigger rows against stock-web tradable_raw OHLC shards.
2. Confirm no hard duplicate key:
   canonical_archetype_id + symbol + trigger_type + entry_date.
3. Verify non-proxy source URLs for 141080, 220100 and 950220.
4. Validate 141080 post-CA continuity and share-count changes inside the selected window.
5. Keep generic C24 bio-data-event weight unchanged until source repair is complete.
6. Consider Stage2 only when:
   - clinical/trial data event is explicit,
   - efficacy/safety and endpoint quality are visible,
   - regulatory or partner validation exists,
   - financing runway is credible,
   - commercialization or milestone bridge is credible,
   - MAE remains controlled or the signal is lifecycle-managed.
7. Consider local 4B-watch when:
   - the trigger is bio data-event beta only,
   - data/regulatory/financing/commercial bridge is weak or stale,
   - MAE_90D <= -20% or MAE_180D <= -25%,
   - post-peak drawdown <= -35%.
8. Do not convert local 4B-watch into full 4B/4C without non-price trial failure, regulatory setback, financing break, partner loss, safety signal or commercialization failure.
9. Emit before/after diagnostics and reject if verified low-MAE clinical-data positives are overblocked.
```

---

## Final round state

```text
completed_round = R7
completed_loop = 78
next_round = R8
next_loop = 78
round_schedule_status = valid
round_sector_consistency = pass
```

