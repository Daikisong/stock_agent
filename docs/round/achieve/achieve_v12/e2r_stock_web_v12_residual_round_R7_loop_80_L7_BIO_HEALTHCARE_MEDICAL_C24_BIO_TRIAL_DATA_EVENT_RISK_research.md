# E2R Stock-Web v12 Residual Research — R7 Loop 80 / L7 / C24

## Metadata

```json
{
  "research_session": "post_calibrated_sector_archetype_residual_research",
  "mode": "historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12",
  "scheduled_round": "R7",
  "scheduled_loop": 80,
  "round_schedule_status": "valid",
  "round_sector_consistency": "pass",
  "completed_round": "R7",
  "completed_loop": 80,
  "computed_next_round": "R8",
  "computed_next_loop": 80,
  "large_sector_id": "L7_BIO_HEALTHCARE_MEDICAL",
  "canonical_archetype_id": "C24_BIO_TRIAL_DATA_EVENT_RISK",
  "fine_archetype_id": "BIO_PLATFORM_TRIAL_DATA_LICENSE_MILESTONE_BRIDGE_VS_TRIAL_THEME_FADE",
  "loop_objective": [
    "coverage_gap_fill",
    "counterexample_mining",
    "4B_non_price_requirement_stress_test",
    "bio_trial_data_event_risk_guardrail",
    "platform_trial_data_license_milestone_commercialization_bridge",
    "trial_theme_MFE_fade_boundary",
    "post_corporate_action_name_change_validation_queue_creation",
    "sector_specific_rule_discovery",
    "canonical_archetype_compression",
    "source_repair_queue_creation"
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

Previous completed state in this interactive run: R6 / loop 80.

Therefore:

```text
scheduled_round = R7
scheduled_loop = 80
allowed_large_sector = L7_BIO_HEALTHCARE_MEDICAL
selected_large_sector = L7_BIO_HEALTHCARE_MEDICAL
selected_canonical_archetype_id = C24_BIO_TRIAL_DATA_EVENT_RISK
computed_next_round = R8
computed_next_loop = 80
```

R7 was routed to C24 because loop 79 R7 used C25.  
This file tests biotech platform trial-data / license-milestone bridges and trial-theme fade boundaries.

## No-Repeat / novelty check

No hard duplicate is intentionally reused.

Hard duplicate key checked conceptually:

```text
canonical_archetype_id + symbol + trigger_type + entry_date
```

No-Repeat shows C24 concentration in:

```text
000100, 028300, 009420, 039200, UNKNOWN_SYMBOL
```

This run uses three different symbols:

```text
298380 / 에이비엘바이오 / bioplatform trial-data and license-milestone bridge
141080 / 리가켐바이오 / post-CA ADC platform data-license bridge
323990 / 박셀바이오 / cell-therapy trial-theme fade
```

Data-quality note:

```text
All three rows are stock-web calibration usable by profile-level corporate-action candidates.
All three rows are source_proxy_only=true / evidence_url_pending=true.
141080 requires post-corporate-action and name-change continuity validation before runtime promotion.
```

## Research thesis

C24 is not “바이오가 올랐다.”

The mechanism must pass through:

```text
trial data or platform event
→ data quality and regulatory path
→ partner / license / milestone economics
→ cash runway and commercialization bridge
→ durable rerating
```

바이오 이벤트는 현미경 위의 빛이다.  
C24가 보려는 것은 그 빛이 실제 데이터, 파트너, 마일스톤, 현금 활주로, 상업화 길로 초점을 맺는지다.

---

## Case 1 — Bioplatform data/license positive: 298380 / 에이비엘바이오

### Evidence status

```text
source_proxy_only = true
evidence_url_pending = true
source_repair_required = true
```

The source-repair task is trial-data quality, partner/license economics, milestone runway, cash runway and commercialization bridge evidence.

```text
evidence_family = BIO_PLATFORM_TRIAL_DATA_PARTNER_LICENSE_MILESTONE_RUNWAY_COMMERCIALIZATION_BRIDGE
case_role = positive_bioplatform_data_license_with_later_4b_watch
trigger_date = 2024-01-31
entry_date = 2024-02-01
entry_price = 21,700
```

### Stock-Web price path

Observed rows from `atlas/ohlcv_tradable_by_symbol_year/298/298380/2024.csv`:

```text
2024-02-01,21700,22200,21350,21800
2024-02-08,20400,20400,18960,19900
2024-03-06,24550,28400,24350,27300
2024-03-13,29800,30500,26300,27900
2024-07-04,27200,29750,27000,29700
2024-10-17,42050,43300,39550,40350
2024-10-28,36900,37550,35800,36700
```

### Backtest

```text
MFE_30D  = +40.55%
MAE_30D  = -12.63%
MFE_90D  = +40.55%
MAE_90D  = -12.63%
MFE_180D = +99.54%
MAE_180D = -12.63%
peak_180 = 43,300 on 2024-10-17
trough_180 = 18,960 on 2024-02-08
peak_to_later_drawdown = -17.32%
```

### Interpretation

This is a C24 data/license positive candidate.  
The MFE expanded enough to justify protecting it after source repair, but not enough to accept price-only evidence.

Correct treatment:

```text
verified trial data / partner license / milestone / cash runway bridge → Stage2 possible
bridge stale after peak → lifecycle local 4B-watch
```

---

## Case 2 — Post-CA ADC-platform positive: 141080 / 리가켐바이오

### Evidence status

```text
source_proxy_only = true
evidence_url_pending = true
post_corporate_action_validation_required = true
name_change_validation_required = true
share_count_change_inside_window = true
source_repair_required = true
```

The source-repair task is ADC platform trial data, license economics, partner quality, milestone runway and commercialization bridge evidence.

```text
evidence_family = ADC_PLATFORM_TRIAL_DATA_LICENSE_MILESTONE_PIPELINE_COMMERCIALIZATION_BRIDGE_POST_CA
case_role = positive_post_CA_ADC_data_license_with_later_4b_watch
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
2024-07-09,81800,87200,80600,84100
2024-08-29,96900,99500,94300,94800
2024-10-22,130700,139600,127100,130700
2024-11-11,133700,143600,130800,140000
```

### Backtest

```text
MFE_30D  = +5.59%
MAE_30D  = -10.88%
MFE_90D  = +46.32%
MAE_90D  = -10.88%
MFE_180D = +111.18%
MAE_180D = -10.88%
peak_180 = 143,600 on 2024-11-11
trough_180 = 60,600 on 2024-05-30
peak_to_later_drawdown = -23.05%
```

### Interpretation

This is a strong C24 ADC-platform positive, but not a clean raw row.  
The 2024-04-23 corporate-action candidate and 2024-04-19 name change mean runtime ingestion must validate continuity.

Correct treatment:

```text
post-CA/name validation first
verified ADC data / license / milestone / partner bridge → Stage2 possible
bridge stale after peak → lifecycle local 4B-watch
```

---

## Case 3 — Counterexample / local 4B: 323990 / 박셀바이오

### Evidence status

```text
source_proxy_only = true
evidence_url_pending = true
source_repair_required = true
```

This row tests cell-therapy trial-theme beta without enough data/regulatory/partner/cash-runway bridge.

```text
evidence_family = CELL_THERAPY_TRIAL_THEME_WITH_WEAK_DATA_REGULATORY_PARTNER_CASH_RUNWAY_BRIDGE
case_role = counterexample_trial_theme_local4b
trigger_date = 2024-01-31
entry_date = 2024-02-01
entry_price = 18,800
```

### Stock-Web price path

Observed rows from `atlas/ohlcv_tradable_by_symbol_year/323/323990/2024.csv`:

```text
2024-02-01,18800,19240,18790,19160
2024-03-07,20250,22500,20250,21150
2024-03-25,21450,24250,21050,23350
2024-04-11,17900,17910,17650,17770
2024-08-05,15600,15690,13010,13670
2024-09-11,13940,14180,13500,13510
2024-10-25,12670,12670,12020,12200
```

### Backtest

```text
MFE_30D  = +19.68%
MAE_30D  = -0.05%
MFE_90D  = +28.99%
MAE_90D  = -6.12%
MFE_180D = +28.99%
MAE_180D = -36.06%
peak_180 = 24,250 on 2024-03-25
trough_180 = 12,020 on 2024-10-25
peak_to_later_drawdown = -50.43%
```

### Interpretation

This is the C24 trial-theme fade row.  
The early MFE was tradable, but durable Stage2 was not validated.

Correct treatment:

```text
cell-therapy trial theme beta
→ no verified data / regulatory / partner / cash runway bridge
→ local 4B-watch
```

---

## Cross-case residual finding

### What this strengthens

```text
stage2_required_bridge = strengthen
price_only_blowoff_blocks_positive_stage = strengthen
local_4b_watch_guard = strengthen
post_corporate_action_validation_guard = strengthen
name_change_validation_guard = strengthen
full_4b_requires_non_price_evidence = keep
```

### What this does not justify

```text
do_not_raise_generic_C24_bio_event_weight = true
do_not_treat_all_bio_MFE_as_Green = true
do_not_ingest_post_CA_or_name_change_rows_without_validation = true
do_not_convert_bio_drawdown_to_hard_4C_without_non_price_trial_failure_regulatory_rejection_or_financing_break = true
```

### Candidate canonical compression

Fine labels can compress into:

```text
BIO_PLATFORM_TRIAL_DATA_LICENSE_MILESTONE_BRIDGE_VS_TRIAL_THEME_FADE
```

This fine archetype covers:

```text
1. bioplatform trial-data / license bridge → Stage2 possible after source repair
2. ADC-platform post-CA data/license bridge → Stage2 possible after CA/name validation
3. cell-therapy trial theme without data/regulatory bridge → false Stage2 / local 4B
```

---

## Machine-readable rows

### price source validation row

```jsonl
{"row_type": "price_source_validation", "source": "Songdaiki/stock-web", "source_url": "https://github.com/Songdaiki/stock-web", "manifest_path": "atlas/manifest.json", "schema_path": "atlas/schema.json", "universe_path": "atlas/universe/all_symbols.csv", "manifest_max_date": "2026-02-20", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "raw_shard_root": "atlas/ohlcv_raw_by_symbol_year", "validation_status": "usable_for_historical_calibration"}
```

### case rows

```jsonl
{"row_type": "case", "case_id": "R7L80-C24-298380-ABL-BIO-BIOPLATFORM-DATA-LICENSE-MILESTONE", "symbol": "298380", "company_name": "에이비엘바이오", "round": "R7", "loop": "80", "large_sector_id": "L7_BIO_HEALTHCARE_MEDICAL", "canonical_archetype_id": "C24_BIO_TRIAL_DATA_EVENT_RISK", "fine_archetype_id": "BIO_PLATFORM_TRIAL_DATA_LICENSE_MILESTONE_BRIDGE_VS_TRIAL_THEME_FADE", "case_type": "bio_trial_data_event_risk", "positive_or_counterexample": "positive", "best_trigger": "Stage2-Actionable-BioPlatformTrialDataLicenseMilestoneBridgeWithLifecycle4B", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 0.5, "score_price_alignment": "C24 should protect platform-biotech positives only when trial data, partner/license economics, milestone runway, cash runway and commercialization path are visible. ABL Bio produced a strong MFE but still needs lifecycle 4B if the data/license bridge fades.", "current_profile_verdict": "source_repair_required_before_runtime_weight", "price_source": "Songdaiki/stock-web", "notes": "Stock-web path usable; non-proxy trial data, regulatory path, partner/license economics, milestone/cash runway and commercialization bridge evidence required before runtime promotion."}
{"row_type": "case", "case_id": "R7L80-C24-141080-LIGACHEM-ADC-POSTCA-DATA-LICENSE-MILESTONE", "symbol": "141080", "company_name": "리가켐바이오", "round": "R7", "loop": "80", "large_sector_id": "L7_BIO_HEALTHCARE_MEDICAL", "canonical_archetype_id": "C24_BIO_TRIAL_DATA_EVENT_RISK", "fine_archetype_id": "BIO_PLATFORM_TRIAL_DATA_LICENSE_MILESTONE_BRIDGE_VS_TRIAL_THEME_FADE", "case_type": "bio_trial_data_event_risk", "positive_or_counterexample": "positive", "best_trigger": "Stage2-Actionable-PostCAADCPlatformDataLicenseMilestoneBridgeWithLifecycle4B", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 0.5, "score_price_alignment": "C24 should allow ADC platform positives when post-CA continuity, trial data, license economics, milestone runway, partner quality and commercialization bridge are visible. LigaChem Bio produced a large post-CA MFE, but runtime ingestion requires post-CA/name-change validation.", "current_profile_verdict": "source_repair_required_before_runtime_weight", "price_source": "Songdaiki/stock-web", "notes": "Stock-web path usable; non-proxy trial data, regulatory path, partner/license economics, milestone/cash runway and commercialization bridge evidence required before runtime promotion."}
{"row_type": "case", "case_id": "R7L80-C24-323990-VAXCELL-TRIAL-THEME-FADE", "symbol": "323990", "company_name": "박셀바이오", "round": "R7", "loop": "80", "large_sector_id": "L7_BIO_HEALTHCARE_MEDICAL", "canonical_archetype_id": "C24_BIO_TRIAL_DATA_EVENT_RISK", "fine_archetype_id": "BIO_PLATFORM_TRIAL_DATA_LICENSE_MILESTONE_BRIDGE_VS_TRIAL_THEME_FADE", "case_type": "bio_trial_data_event_risk", "positive_or_counterexample": "counterexample", "best_trigger": "Stage2-FalsePositive / TrialThemeMFEFadeWithLocal4BWatch", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 0.5, "score_price_alignment": "C24 should not treat cell-therapy trial theme beta as durable Stage2 unless trial data quality, regulatory path, partner/commercial economics and cash runway are visible. VaxCell had a tradable MFE but then a high-MAE fade.", "current_profile_verdict": "source_repair_required_before_runtime_weight", "price_source": "Songdaiki/stock-web", "notes": "Stock-web path usable; non-proxy trial data, regulatory path, partner/license economics, milestone/cash runway and commercialization bridge evidence required before runtime promotion."}
```

### trigger rows

```jsonl
{"row_type": "trigger", "trigger_id": "TRG_R7L80-C24-298380-ABL-BIO-BIOPLATFORM-DATA-LICENSE-MILESTONE", "case_id": "R7L80-C24-298380-ABL-BIO-BIOPLATFORM-DATA-LICENSE-MILESTONE", "symbol": "298380", "company_name": "에이비엘바이오", "round": "R7", "loop": "80", "large_sector_id": "L7_BIO_HEALTHCARE_MEDICAL", "canonical_archetype_id": "C24_BIO_TRIAL_DATA_EVENT_RISK", "fine_archetype_id": "BIO_PLATFORM_TRIAL_DATA_LICENSE_MILESTONE_BRIDGE_VS_TRIAL_THEME_FADE", "loop_objective": "coverage_gap_fill|counterexample_mining|bio_trial_data_event_risk_guardrail", "trigger_type": "Stage2-Actionable-BioPlatformTrialDataLicenseMilestoneBridgeWithLifecycle4B", "trigger_date": "2024-01-31", "entry_date": "2024-02-01", "entry_price": 21700.0, "evidence_available_at_that_date": "BIO_PLATFORM_TRIAL_DATA_PARTNER_LICENSE_MILESTONE_RUNWAY_COMMERCIALIZATION_BRIDGE", "evidence_source": "source_proxy_manual_verification_required:ABL_BIO_2024_TRIAL_DATA_LICENSE_PARTNER_MILESTONE_CASH_RUNWAY_COMMERCIALIZATION_BRIDGE", "stage2_evidence_fields": ["trial_data_quality_candidate", "partner_license_or_milestone_candidate", "regulatory_commercialization_bridge_candidate"], "stage3_evidence_fields": ["relative_strength", "cash_runway_or_partner_quality_candidate"], "stage4b_evidence_fields": ["trial_theme_beta", "bridge_stale_or_absent", "MAE_widening", "post_peak_drawdown"], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/298/298380/2024.csv", "profile_path": "atlas/symbol_profiles/298/298380.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": 40.55, "MFE_90D_pct": 40.55, "MFE_180D_pct": 99.54, "MAE_30D_pct": -12.63, "MAE_90D_pct": -12.63, "MAE_180D_pct": -12.63, "peak_date": "2024-10-17", "peak_price": 43300.0, "drawdown_after_peak_pct": -17.32, "green_lateness_ratio": null, "four_b_local_peak_proximity": "local_4b_watch_after_bio_trial_peak_if_data_license_regulatory_or_cash_runway_bridge_fades", "four_b_full_window_peak_proximity": "full_4b_requires_non_price_trial_failure_regulatory_rejection_partner_loss_financing_or_cash_runway_break", "trigger_outcome_label": "positive_bioplatform_data_license_with_later_4b_watch", "current_profile_verdict": "C24 should protect platform-biotech positives only when trial data, partner/license economics, milestone runway, cash runway and commercialization path are visible. ABL Bio produced a strong MFE but still needs lifecycle 4B if the data/license bridge fades.", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window_by_profile_or_post_CA_validation_required", "share_count_change_inside_window": false, "same_entry_group_id": "C24_BIO_TRIAL_DATA_298380_2024-02-01", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 0.5, "do_not_count_as_new_case": false, "source_proxy_only": true, "evidence_url_pending": true}
{"row_type": "trigger", "trigger_id": "TRG_R7L80-C24-141080-LIGACHEM-ADC-POSTCA-DATA-LICENSE-MILESTONE", "case_id": "R7L80-C24-141080-LIGACHEM-ADC-POSTCA-DATA-LICENSE-MILESTONE", "symbol": "141080", "company_name": "리가켐바이오", "round": "R7", "loop": "80", "large_sector_id": "L7_BIO_HEALTHCARE_MEDICAL", "canonical_archetype_id": "C24_BIO_TRIAL_DATA_EVENT_RISK", "fine_archetype_id": "BIO_PLATFORM_TRIAL_DATA_LICENSE_MILESTONE_BRIDGE_VS_TRIAL_THEME_FADE", "loop_objective": "coverage_gap_fill|counterexample_mining|bio_trial_data_event_risk_guardrail", "trigger_type": "Stage2-Actionable-PostCAADCPlatformDataLicenseMilestoneBridgeWithLifecycle4B", "trigger_date": "2024-04-23", "entry_date": "2024-04-24", "entry_price": 68000.0, "evidence_available_at_that_date": "ADC_PLATFORM_TRIAL_DATA_LICENSE_MILESTONE_PIPELINE_COMMERCIALIZATION_BRIDGE_POST_CA", "evidence_source": "source_proxy_manual_verification_required:LIGACHEM_BIO_2024_ADC_PLATFORM_TRIAL_DATA_LICENSE_MILESTONE_PARTNER_COMMERCIALIZATION_BRIDGE_POST_CA", "stage2_evidence_fields": ["trial_data_quality_candidate", "partner_license_or_milestone_candidate", "regulatory_commercialization_bridge_candidate"], "stage3_evidence_fields": ["relative_strength", "cash_runway_or_partner_quality_candidate"], "stage4b_evidence_fields": ["trial_theme_beta", "bridge_stale_or_absent", "MAE_widening", "post_peak_drawdown"], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/141/141080/2024.csv", "profile_path": "atlas/symbol_profiles/141/141080.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": 5.59, "MFE_90D_pct": 46.32, "MFE_180D_pct": 111.18, "MAE_30D_pct": -10.88, "MAE_90D_pct": -10.88, "MAE_180D_pct": -10.88, "peak_date": "2024-11-11", "peak_price": 143600.0, "drawdown_after_peak_pct": -23.05, "green_lateness_ratio": null, "four_b_local_peak_proximity": "local_4b_watch_after_bio_trial_peak_if_data_license_regulatory_or_cash_runway_bridge_fades", "four_b_full_window_peak_proximity": "full_4b_requires_non_price_trial_failure_regulatory_rejection_partner_loss_financing_or_cash_runway_break", "trigger_outcome_label": "positive_post_CA_ADC_data_license_with_later_4b_watch", "current_profile_verdict": "C24 should allow ADC platform positives when post-CA continuity, trial data, license economics, milestone runway, partner quality and commercialization bridge are visible. LigaChem Bio produced a large post-CA MFE, but runtime ingestion requires post-CA/name-change validation.", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window_by_profile_or_post_CA_validation_required", "share_count_change_inside_window": true, "same_entry_group_id": "C24_BIO_TRIAL_DATA_141080_2024-04-24", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 0.5, "do_not_count_as_new_case": false, "source_proxy_only": true, "evidence_url_pending": true}
{"row_type": "trigger", "trigger_id": "TRG_R7L80-C24-323990-VAXCELL-TRIAL-THEME-FADE", "case_id": "R7L80-C24-323990-VAXCELL-TRIAL-THEME-FADE", "symbol": "323990", "company_name": "박셀바이오", "round": "R7", "loop": "80", "large_sector_id": "L7_BIO_HEALTHCARE_MEDICAL", "canonical_archetype_id": "C24_BIO_TRIAL_DATA_EVENT_RISK", "fine_archetype_id": "BIO_PLATFORM_TRIAL_DATA_LICENSE_MILESTONE_BRIDGE_VS_TRIAL_THEME_FADE", "loop_objective": "coverage_gap_fill|counterexample_mining|bio_trial_data_event_risk_guardrail", "trigger_type": "Stage2-FalsePositive / TrialThemeMFEFadeWithLocal4BWatch", "trigger_date": "2024-01-31", "entry_date": "2024-02-01", "entry_price": 18800.0, "evidence_available_at_that_date": "CELL_THERAPY_TRIAL_THEME_WITH_WEAK_DATA_REGULATORY_PARTNER_CASH_RUNWAY_BRIDGE", "evidence_source": "source_proxy_manual_verification_required:VAXCELL_BIO_2024_CELL_THERAPY_TRIAL_DATA_REGULATORY_PARTNER_CASH_RUNWAY_BRIDGE", "stage2_evidence_fields": ["trial_data_quality_candidate", "partner_license_or_milestone_candidate", "regulatory_commercialization_bridge_candidate"], "stage3_evidence_fields": ["relative_strength", "cash_runway_or_partner_quality_candidate"], "stage4b_evidence_fields": ["trial_theme_beta", "bridge_stale_or_absent", "MAE_widening", "post_peak_drawdown"], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/323/323990/2024.csv", "profile_path": "atlas/symbol_profiles/323/323990.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": 19.68, "MFE_90D_pct": 28.99, "MFE_180D_pct": 28.99, "MAE_30D_pct": -0.05, "MAE_90D_pct": -6.12, "MAE_180D_pct": -36.06, "peak_date": "2024-03-25", "peak_price": 24250.0, "drawdown_after_peak_pct": -50.43, "green_lateness_ratio": null, "four_b_local_peak_proximity": "local_4b_watch_after_bio_trial_peak_if_data_license_regulatory_or_cash_runway_bridge_fades", "four_b_full_window_peak_proximity": "full_4b_requires_non_price_trial_failure_regulatory_rejection_partner_loss_financing_or_cash_runway_break", "trigger_outcome_label": "counterexample_trial_theme_local4b", "current_profile_verdict": "C24 should not treat cell-therapy trial theme beta as durable Stage2 unless trial data quality, regulatory path, partner/commercial economics and cash runway are visible. VaxCell had a tradable MFE but then a high-MAE fade.", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window_by_profile_or_post_CA_validation_required", "share_count_change_inside_window": false, "same_entry_group_id": "C24_BIO_TRIAL_DATA_323990_2024-02-01", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 0.5, "do_not_count_as_new_case": false, "source_proxy_only": true, "evidence_url_pending": true}
```

### score simulation rows

```jsonl
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R7L80-C24-298380-ABL-BIO-BIOPLATFORM-DATA-LICENSE-MILESTONE", "trigger_id": "TRG_R7L80-C24-298380-ABL-BIO-BIOPLATFORM-DATA-LICENSE-MILESTONE", "symbol": "298380", "large_sector_id": "L7_BIO_HEALTHCARE_MEDICAL", "canonical_archetype_id": "C24_BIO_TRIAL_DATA_EVENT_RISK", "raw_component_scores_before": {"trial_data_quality_score": 14, "partner_license_score": 14, "milestone_cash_runway_score": 13, "regulatory_commercialization_bridge_score": 13, "relative_strength_score": 12, "validation_risk": 0, "execution_risk_score": 10, "source_confidence_score": 2}, "weighted_score_before": 78, "stage_label_before": "Stage2 candidate after source repair", "raw_component_scores_after": {"trial_data_quality_score": 16, "partner_license_score": 16, "milestone_cash_runway_score": 15, "regulatory_commercialization_bridge_score": 15, "relative_strength_score": 11, "validation_risk": 0, "execution_risk_score": 11, "source_confidence_score": 2}, "weighted_score_after": 84, "stage_label_after": "Stage2/Yellow after source repair + lifecycle 4B", "changed_components": ["trial_data_quality_score", "partner_license_score", "milestone_cash_runway_score", "regulatory_commercialization_bridge_score", "execution_risk_score"], "component_delta_explanation": "Reward only verified trial data, partner/license economics, milestone/cash runway and regulatory/commercialization bridge; cap trial-theme beta when bridge fails to refresh.", "MFE_90D_pct": 40.55, "MAE_90D_pct": -12.63, "score_return_alignment_label": "bio_trial_data_license_positive_with_lifecycle_4b", "current_profile_verdict": "C24 should protect platform-biotech positives only when trial data, partner/license economics, milestone runway, cash runway and commercialization path are visible. ABL Bio produced a strong MFE but still needs lifecycle 4B if the data/license bridge fades."}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R7L80-C24-141080-LIGACHEM-ADC-POSTCA-DATA-LICENSE-MILESTONE", "trigger_id": "TRG_R7L80-C24-141080-LIGACHEM-ADC-POSTCA-DATA-LICENSE-MILESTONE", "symbol": "141080", "large_sector_id": "L7_BIO_HEALTHCARE_MEDICAL", "canonical_archetype_id": "C24_BIO_TRIAL_DATA_EVENT_RISK", "raw_component_scores_before": {"trial_data_quality_score": 14, "partner_license_score": 14, "milestone_cash_runway_score": 13, "regulatory_commercialization_bridge_score": 13, "relative_strength_score": 12, "validation_risk": 10, "execution_risk_score": 10, "source_confidence_score": 2}, "weighted_score_before": 78, "stage_label_before": "Stage2 candidate after source repair", "raw_component_scores_after": {"trial_data_quality_score": 16, "partner_license_score": 16, "milestone_cash_runway_score": 15, "regulatory_commercialization_bridge_score": 15, "relative_strength_score": 11, "validation_risk": 12, "execution_risk_score": 11, "source_confidence_score": 2}, "weighted_score_after": 84, "stage_label_after": "Stage2/Yellow after source repair + lifecycle 4B", "changed_components": ["trial_data_quality_score", "partner_license_score", "milestone_cash_runway_score", "regulatory_commercialization_bridge_score", "execution_risk_score"], "component_delta_explanation": "Reward only verified trial data, partner/license economics, milestone/cash runway and regulatory/commercialization bridge; cap trial-theme beta when bridge fails to refresh.", "MFE_90D_pct": 46.32, "MAE_90D_pct": -10.88, "score_return_alignment_label": "bio_trial_data_license_positive_with_lifecycle_4b", "current_profile_verdict": "C24 should allow ADC platform positives when post-CA continuity, trial data, license economics, milestone runway, partner quality and commercialization bridge are visible. LigaChem Bio produced a large post-CA MFE, but runtime ingestion requires post-CA/name-change validation."}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R7L80-C24-323990-VAXCELL-TRIAL-THEME-FADE", "trigger_id": "TRG_R7L80-C24-323990-VAXCELL-TRIAL-THEME-FADE", "symbol": "323990", "large_sector_id": "L7_BIO_HEALTHCARE_MEDICAL", "canonical_archetype_id": "C24_BIO_TRIAL_DATA_EVENT_RISK", "raw_component_scores_before": {"trial_data_quality_score": 5, "partner_license_score": 3, "milestone_cash_runway_score": 3, "regulatory_commercialization_bridge_score": 2, "relative_strength_score": 5, "validation_risk": 0, "execution_risk_score": 22, "source_confidence_score": 2}, "weighted_score_before": 44, "stage_label_before": "Stage2-FalsePositive / local 4B-watch", "raw_component_scores_after": {"trial_data_quality_score": 3, "partner_license_score": 1, "milestone_cash_runway_score": 1, "regulatory_commercialization_bridge_score": 1, "relative_strength_score": 4, "validation_risk": 0, "execution_risk_score": 24, "source_confidence_score": 2}, "weighted_score_after": 33, "stage_label_after": "Stage4B-local-watch / no durable Green", "changed_components": ["trial_data_quality_score", "partner_license_score", "milestone_cash_runway_score", "regulatory_commercialization_bridge_score", "execution_risk_score"], "component_delta_explanation": "Reward only verified trial data, partner/license economics, milestone/cash runway and regulatory/commercialization bridge; cap trial-theme beta when bridge fails to refresh.", "MFE_90D_pct": 28.99, "MAE_90D_pct": -6.12, "score_return_alignment_label": "false_positive_trial_theme_bridge_gap", "current_profile_verdict": "C24 should not treat cell-therapy trial theme beta as durable Stage2 unless trial data quality, regulatory path, partner/commercial economics and cash runway are visible. VaxCell had a tradable MFE but then a high-MAE fade."}
```

### aggregate row

```jsonl
{"row_type": "aggregate", "round": "R7", "loop": 80, "large_sector_id": "L7_BIO_HEALTHCARE_MEDICAL", "canonical_archetype_id": "C24_BIO_TRIAL_DATA_EVENT_RISK", "fine_archetype_id": "BIO_PLATFORM_TRIAL_DATA_LICENSE_MILESTONE_BRIDGE_VS_TRIAL_THEME_FADE", "calibration_usable_case_count": 3, "calibration_usable_trigger_count": 3, "new_independent_case_count": 3, "reused_case_count": 0, "same_archetype_new_symbol_count": 3, "same_archetype_new_trigger_family_count": 3, "positive_case_count": 2, "counterexample_count": 1, "four_b_case_count": 3, "four_c_case_count": 0, "source_proxy_only_count": 3, "evidence_url_pending_count": 3, "share_count_change_inside_window_count": 1, "post_corporate_action_validation_count": 1, "name_change_validation_count": 1, "current_profile_error_count": 1, "diversity_score_summary": "+3 C24 bio trial/data symbols outside top-covered 000100/028300/009420/039200 set, +3 bioplatform/ADC/cell-therapy trigger families, +2 data-license positives, +1 trial-theme local-4B counterexample, no hard duplicate", "residual_contribution_label": "coverage_gap_fill_with_source_repair_CA_name_validation_needed"}
```

### shadow weight row

```jsonl
{"row_type": "shadow_weight", "round": "R7", "loop": 80, "large_sector_id": "L7_BIO_HEALTHCARE_MEDICAL", "canonical_archetype_id": "C24_BIO_TRIAL_DATA_EVENT_RISK", "axis": "bio_platform_trial_data_license_milestone_bridge_vs_trial_theme_fade", "decision": "hold_for_source_repair_and_more_evidence", "proposed_runtime_effect": "C24 should split verified trial-data/platform license milestone rerating from generic biotech trial-theme beta. Stage2 requires data quality, partner/license economics, milestone/cash runway, regulatory path and commercialization bridge. If MFE fades and MAE/post-peak drawdown opens without bridge refresh, route to local 4B-watch. Post-CA/name-change rows require continuity validation before runtime promotion.", "do_not_propose_new_weight_delta": true, "needs_more_evidence": true, "source_repair_required": ["298380", "141080", "323990"], "post_corporate_action_validation_required": ["141080"], "name_change_validation_required": ["141080"]}
```

### residual contribution row

```jsonl
{"row_type": "residual_contribution", "round": "R7", "loop": 80, "large_sector_id": "L7_BIO_HEALTHCARE_MEDICAL", "canonical_archetype_id": "C24_BIO_TRIAL_DATA_EVENT_RISK", "existing_axis_strengthened": ["stage2_required_bridge", "price_only_blowoff_blocks_positive_stage", "local_4b_watch_guard", "post_corporate_action_validation_guard", "name_change_validation_guard", "full_4b_requires_non_price_evidence"], "new_axis_proposed": null, "sector_specific_rule_candidate": true, "canonical_archetype_rule_candidate": true, "narrative_summary": "C24 needs trial data quality, partner/license economics, milestone/cash runway and regulatory/commercialization proof. ABL Bio and LigaChem Bio show data-license platform positives after source repair; VaxCell Bio shows trial-theme MFE fading into local 4B when data/regulatory/partner bridge is weak."}
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
  name = 에이비엘바이오
  corporate_action_candidate_dates = none
  selected window = 2024-02-01~D+180
  contamination = false

141080:
  name = 리가켐바이오 from 2024-04-19, 레고켐바이오 before that
  corporate_action_candidate_dates = 2020-07-07, 2024-04-23
  selected entry starts 2024-04-24 after the 2024-04-23 candidate
  contamination = false after post-CA entry, but coding-agent validation required
  name_change_inside_window = true
  share_count_change_inside_window = true

323990:
  name = 박셀바이오
  corporate_action_candidate_dates = 2021-01-22, 2023-11-23, 2023-11-30
  selected window = 2024-02-01~D+180
  contamination = false
```

Data-quality caveat:

```text
All selected C24 rows are source_proxy_only / evidence_url_pending.
141080 requires post-corporate-action, name-change and share-count validation before runtime promotion.
This MD is useful for stock-web path calibration and C24 rule-shape discovery,
but coding-agent promotion requires non-proxy trial data, regulatory path, partner/license economics, milestone/cash runway and commercialization evidence.
```

---

## Deferred Coding Agent Handoff Prompt

Do not execute this now.

```text
You are the coding agent for Songdaiki/stock_agent.

Read this standalone v12 residual research MD and ingest machine-readable rows only after validation.

Do not patch production scoring blindly.
This R7/C24 artifact is marked do_not_propose_new_weight_delta=true because all rows need source repair and 141080 needs post-CA/name/share-count validation.

Candidate axis:
bio_platform_trial_data_license_milestone_bridge_vs_trial_theme_fade

Required checks before implementation:
1. Validate all trigger rows against stock-web tradable_raw OHLC shards.
2. Confirm no hard duplicate key:
   canonical_archetype_id + symbol + trigger_type + entry_date.
3. Verify non-proxy source URLs for 298380, 141080 and 323990.
4. Validate 141080 continuity after the 2024-04-19 name change and 2024-04-23 corporate-action candidate.
5. Keep generic C24 bio-event weight unchanged until source repair is complete.
6. Consider Stage2 only when:
   - trial data quality is explicit,
   - regulatory path is credible,
   - partner / license / milestone economics exist,
   - cash runway and commercialization bridge are visible,
   - MAE remains controlled or the signal is lifecycle-managed.
7. Consider local 4B-watch when:
   - the trigger is bio/trial theme beta only,
   - data/regulatory/partner/cash-runway evidence is weak or stale,
   - MAE_90D <= -20% or MAE_180D <= -25%,
   - post-peak drawdown <= -35%.
8. Do not convert local 4B-watch into full 4B/4C without non-price trial failure, regulatory rejection, partner loss, financing break or cash-runway break.
9. Emit before/after diagnostics and reject if verified data-license positives are overblocked.
```

---

## Final round state

```text
completed_round = R7
completed_loop = 80
next_round = R8
next_loop = 80
round_schedule_status = valid
round_sector_consistency = pass
```

