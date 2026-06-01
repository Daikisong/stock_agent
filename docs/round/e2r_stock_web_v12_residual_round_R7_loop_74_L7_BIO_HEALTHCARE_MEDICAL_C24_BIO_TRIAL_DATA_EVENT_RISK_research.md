# E2R Stock-Web v12 Residual Research — R7 Loop 74 / L7 / C24

## Metadata

```json
{
  "research_session": "post_calibrated_sector_archetype_residual_research",
  "mode": "historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12",
  "scheduled_round": "R7",
  "scheduled_loop": 74,
  "round_schedule_status": "valid",
  "round_sector_consistency": "pass",
  "completed_round": "R7",
  "completed_loop": 74,
  "computed_next_round": "R8",
  "computed_next_loop": 74,
  "large_sector_id": "L7_BIO_HEALTHCARE_MEDICAL",
  "canonical_archetype_id": "C24_BIO_TRIAL_DATA_EVENT_RISK",
  "fine_archetype_id": "ADC_BISPECIFIC_PLATFORM_DATA_DERISKING_VS_IMMUNOTHERAPY_TRIAL_HEADLINE_FADE",
  "loop_objective": [
    "coverage_gap_fill",
    "counterexample_mining",
    "4B_non_price_requirement_stress_test",
    "trial_data_event_timing_test",
    "sector_specific_rule_discovery",
    "canonical_archetype_compression",
    "source_repair_queue_creation",
    "share_count_validation_queue_creation"
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

Previous completed state in this interactive run: R6 / loop 74.

Therefore:

```text
scheduled_round = R7
scheduled_loop = 74
allowed_large_sector = L7_BIO_HEALTHCARE_MEDICAL
selected_large_sector = L7_BIO_HEALTHCARE_MEDICAL
selected_canonical_archetype_id = C24_BIO_TRIAL_DATA_EVENT_RISK
computed_next_round = R8
computed_next_loop = 74
```

R7 was routed to C24 because loop 73 used C23 and C24 has thinner coverage than C25.

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
141080 / 리가켐바이오 / ADC platform data derisking
298380 / 에이비엘바이오 / bispecific platform data rerating
950220 / 네오이뮨텍 / immunotherapy trial headline fade
```

Data-quality note:

```text
All three rows are stock-web calibration usable by profile-level corporate-action candidates.
All three rows are source_proxy_only=true / evidence_url_pending=true.
141080 uses a post-2024-04-23 corporate-action entry.
141080 and 298380 show share-count changes inside the selected window and need coding-agent validation.
```

## Research thesis

C24 is not “bio headline went up.”

The mechanism is:

```text
trial/platform event
→ endpoint quality or platform derisking
→ partner validation / regulatory or commercial path
→ durable rerating
```

A trial headline is a match.  
Endpoint durability is the candle staying lit.

---

## Case 1 — Delayed positive with lifecycle 4B: 141080 / 리가켐바이오

### Evidence status

```text
source_proxy_only = true
evidence_url_pending = true
post_corporate_action_entry = true
share_count_change_inside_window = true
source_repair_required = true
```

The source-repair task is ADC platform data, partner validation, derisking, and commercialization path evidence.

```text
evidence_family = ADC_PLATFORM_CLINICAL_DATA_PARTNER_VALIDATION_DERISKING_WITH_POST_CA_VALIDATION
case_role = delayed_positive_with_later_4b_watch_and_sharecount_validation
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
2024-11-11,133700,143600,130800,140000
2024-11-21,101400,101500,91300,97000
```

### Backtest

```text
MFE_30D  = +5.59%
MAE_30D  = -10.88%
MFE_90D  = +28.24%
MAE_90D  = -10.88%
MFE_180D = +111.18%
MAE_180D = -10.88%
peak_180 = 143,600 on 2024-11-11
trough_180 = 60,600 on 2024-05-30
peak_to_later_drawdown = -36.42%
```

### Interpretation

This is a delayed positive, not an immediate gap Green.  
The post-CA entry still had early MAE, but later platform-data/partner derisking may have become real.

C24 should therefore allow delayed Stage2 only after source repair, while keeping later local 4B-watch after the November peak.

---

## Case 2 — Delayed positive with share-count validation: 298380 / 에이비엘바이오

### Evidence status

```text
source_proxy_only = true
evidence_url_pending = true
share_count_change_inside_window = true
source_repair_required = true
```

The source-repair task is bispecific antibody platform data, CNS/BBB path, partner validation and clinical derisking evidence.

```text
evidence_family = BISPECIFIC_ANTIBODY_PLATFORM_CNS_BBB_CLINICAL_DATA_PARTNER_VALIDATION_BRIDGE
case_role = delayed_positive_with_sharecount_validation
trigger_date = 2024-03-05
entry_date = 2024-03-06
entry_price = 24,550
```

### Stock-Web price path

Observed rows from `atlas/ohlcv_tradable_by_symbol_year/298/298380/2024.csv`:

```text
2024-03-06,24550,28400,24350,27300
2024-03-13,29800,30500,26300,27900
2024-04-17,22100,22400,21500,21500
2024-07-05,29400,31000,28850,29550
2024-10-17,42050,43300,39550,40350
2024-11-21,28750,28950,26350,27650
```

### Backtest

```text
MFE_30D  = +24.24%
MAE_30D  = -10.39%
MFE_90D  = +26.27%
MAE_90D  = -12.42%
MFE_180D = +76.37%
MAE_180D = -12.42%
peak_180 = 43,300 on 2024-10-17
trough_180 = 21,500 on 2024-04-17
peak_to_later_drawdown = -39.15%
```

### Interpretation

This is the C24 platform-data derisking version.  
The path had an early squeeze, a drawdown, and then a larger delayed rerating. That is exactly why C24 should protect delayed positives after source repair while refusing to mark the initial event as risk-free Green.

---

## Case 3 — Counterexample / local 4B: 950220 / 네오이뮨텍

### Evidence status

```text
source_proxy_only = true
evidence_url_pending = true
source_repair_required = true
```

This row tests immunotherapy trial headline beta without enough durable endpoint, partner or commercialization bridge.

```text
evidence_family = IMMUNOTHERAPY_TRIAL_HEADLINE_WITH_WEAK_DURABLE_DATA_COMMERCIALIZATION_BRIDGE
case_role = counterexample
trigger_date = 2024-04-10
entry_date = 2024-04-11
entry_price = 1,447
```

### Stock-Web price path

Observed rows from `atlas/ohlcv_tradable_by_symbol_year/950/950220/2024.csv`:

```text
2024-04-11,1447,1725,1439,1558
2024-04-16,1431,1444,1299,1378
2024-04-25,1409,1818,1396,1651
2024-05-14,1935,2120,1905,1972
2024-11-13,1279,1280,1200,1210
2024-12-09,1100,1100,1009,1015
```

### Backtest

```text
MFE_30D  = +46.51%
MAE_30D  = -10.23%
MFE_90D  = +46.51%
MAE_90D  = -10.23%
MFE_180D = +46.51%
MAE_180D = -30.27%
peak_180 = 2,120 on 2024-05-14
trough_180 = 1,009 on 2024-12-09
peak_to_later_drawdown = -52.41%
```

### Interpretation

This is the C24 headline fade.  
The MFE was tradable, but the endpoint and durability bridge did not hold. Without non-proxy data-quality or partner evidence, this should be false Stage2 / local 4B-watch, not Green.

---

## Cross-case residual finding

### What this strengthens

```text
stage2_required_bridge = strengthen
price_only_blowoff_blocks_positive_stage = strengthen
local_4b_watch_guard = strengthen
delayed_positive_protection = strengthen
```

### What this does not justify

```text
do_not_raise_generic_C24_bio_headline_weight = true
do_not_treat_all_trial_data_spikes_as_Green = true
do_not_convert_bio_drawdown_to_hard_4C_without_non_price_break = true
do_not_overblock_delayed_platform_winners_after_source_repair = true
```

### Candidate canonical compression

Fine labels can compress into:

```text
ADC_BISPECIFIC_PLATFORM_DATA_DERISKING_VS_IMMUNOTHERAPY_TRIAL_HEADLINE_FADE
```

This fine archetype covers:

```text
1. ADC platform derisking + partner validation → delayed Stage2 possible after source repair
2. bispecific platform data rerating → delayed Stage2 possible, with share-count validation
3. immunotherapy trial headline without durable data bridge → false Stage2 / local 4B-watch
```

---

## Machine-readable rows

### price source validation row

```jsonl
{"row_type": "price_source_validation", "source": "Songdaiki/stock-web", "source_url": "https://github.com/Songdaiki/stock-web", "manifest_path": "atlas/manifest.json", "schema_path": "atlas/schema.json", "universe_path": "atlas/universe/all_symbols.csv", "manifest_max_date": "2026-02-20", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "raw_shard_root": "atlas/ohlcv_raw_by_symbol_year", "validation_status": "usable_for_historical_calibration"}
```

### case rows

```jsonl
{"row_type": "case", "case_id": "R7L74-C24-141080-LCB-ADC-PLATFORM-DATA-DERISKING", "symbol": "141080", "company_name": "리가켐바이오", "round": "R7", "loop": "74", "large_sector_id": "L7_BIO_HEALTHCARE_MEDICAL", "canonical_archetype_id": "C24_BIO_TRIAL_DATA_EVENT_RISK", "fine_archetype_id": "ADC_BISPECIFIC_PLATFORM_DATA_DERISKING_VS_IMMUNOTHERAPY_TRIAL_HEADLINE_FADE", "case_type": "bio_trial_data_event_risk", "positive_or_counterexample": "delayed_positive", "best_trigger": "Stage2-DelayedPositive-ADCPlatformDataDeriskingPostCA", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 0.5, "score_price_alignment": "C24 should not treat a biotech data/platform event as instant Green at the first gap, but it should allow delayed Stage2 when clinical/platform derisking and partner validation become real. LigaChem Bio required post-CA validation and later lifecycle 4B after the November peak.", "current_profile_verdict": "source_repair_required_before_runtime_weight", "price_source": "Songdaiki/stock-web", "notes": "Stock-web path usable; non-proxy trial data, endpoint durability, partner validation, commercialization and share-count validation required before runtime promotion."}
{"row_type": "case", "case_id": "R7L74-C24-298380-ABL-BISPECIFIC-PLATFORM-DATA-RERATING", "symbol": "298380", "company_name": "에이비엘바이오", "round": "R7", "loop": "74", "large_sector_id": "L7_BIO_HEALTHCARE_MEDICAL", "canonical_archetype_id": "C24_BIO_TRIAL_DATA_EVENT_RISK", "fine_archetype_id": "ADC_BISPECIFIC_PLATFORM_DATA_DERISKING_VS_IMMUNOTHERAPY_TRIAL_HEADLINE_FADE", "case_type": "bio_trial_data_event_risk", "positive_or_counterexample": "delayed_positive", "best_trigger": "Stage2-DelayedPositive-BispecificPlatformDataRerating", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 0.5, "score_price_alignment": "C24 should distinguish platform-data derisking from simple biotech beta. ABL Bio had an early tradable MFE, then later re-accelerated into a larger 180D MFE; however later drawdown and share-count change require lifecycle and validation controls.", "current_profile_verdict": "source_repair_required_before_runtime_weight", "price_source": "Songdaiki/stock-web", "notes": "Stock-web path usable; non-proxy trial data, endpoint durability, partner validation, commercialization and share-count validation required before runtime promotion."}
{"row_type": "case", "case_id": "R7L74-C24-950220-NEOIMMUNETECH-IMMUNOTHERAPY-TRIAL-HEADLINE-FADE", "symbol": "950220", "company_name": "네오이뮨텍", "round": "R7", "loop": "74", "large_sector_id": "L7_BIO_HEALTHCARE_MEDICAL", "canonical_archetype_id": "C24_BIO_TRIAL_DATA_EVENT_RISK", "fine_archetype_id": "ADC_BISPECIFIC_PLATFORM_DATA_DERISKING_VS_IMMUNOTHERAPY_TRIAL_HEADLINE_FADE", "case_type": "bio_trial_data_event_risk", "positive_or_counterexample": "counterexample", "best_trigger": "Stage2-FalsePositive / ImmunotherapyTrialHeadlineFade", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 0.5, "score_price_alignment": "C24 should not treat immunotherapy trial/headline spikes as durable Stage2 unless data quality, endpoint durability, partner path or commercialization bridge is visible. NeoImmuneTech had large MFE but later collapsed into high MAE and post-peak drawdown.", "current_profile_verdict": "source_repair_required_before_runtime_weight", "price_source": "Songdaiki/stock-web", "notes": "Stock-web path usable; non-proxy trial data, endpoint durability, partner validation, commercialization and share-count validation required before runtime promotion."}
```

### trigger rows

```jsonl
{"row_type": "trigger", "trigger_id": "TRG_R7L74-C24-141080-LCB-ADC-PLATFORM-DATA-DERISKING", "case_id": "R7L74-C24-141080-LCB-ADC-PLATFORM-DATA-DERISKING", "symbol": "141080", "company_name": "리가켐바이오", "round": "R7", "loop": "74", "large_sector_id": "L7_BIO_HEALTHCARE_MEDICAL", "canonical_archetype_id": "C24_BIO_TRIAL_DATA_EVENT_RISK", "fine_archetype_id": "ADC_BISPECIFIC_PLATFORM_DATA_DERISKING_VS_IMMUNOTHERAPY_TRIAL_HEADLINE_FADE", "loop_objective": "coverage_gap_fill|counterexample_mining|trial_data_event_timing_test", "trigger_type": "Stage2-DelayedPositive-ADCPlatformDataDeriskingPostCA", "trigger_date": "2024-04-23", "entry_date": "2024-04-24", "entry_price": 68000.0, "evidence_available_at_that_date": "ADC_PLATFORM_CLINICAL_DATA_PARTNER_VALIDATION_DERISKING_WITH_POST_CA_VALIDATION", "evidence_source": "source_proxy_manual_verification_required:LIGACHEM_BIO_2024_ADC_PLATFORM_CLINICAL_DATA_PARTNER_VALIDATION_DERISKING", "stage2_evidence_fields": ["trial_or_platform_data_candidate", "partner_validation_candidate", "endpoint_or_derisking_bridge_candidate"], "stage3_evidence_fields": ["relative_strength", "data_quality_or_partner_bridge_candidate"], "stage4b_evidence_fields": ["bridge_stale_or_absent", "MAE_widening", "post_peak_drawdown"], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/141/141080/2024.csv", "profile_path": "atlas/symbol_profiles/141/141080.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": 5.59, "MFE_90D_pct": 28.24, "MFE_180D_pct": 111.18, "MAE_30D_pct": -10.88, "MAE_90D_pct": -10.88, "MAE_180D_pct": -10.88, "peak_date": "2024-11-11", "peak_price": 143600.0, "drawdown_after_peak_pct": -36.42, "green_lateness_ratio": null, "four_b_local_peak_proximity": "local_4b_watch_after_trial_data_or_platform_peak_if_bridge_fades", "four_b_full_window_peak_proximity": "full_4b_requires_non_price_clinical_failure_endpoint_or_partner_break", "trigger_outcome_label": "delayed_positive_with_later_4b_watch_and_sharecount_validation", "current_profile_verdict": "C24 should not treat a biotech data/platform event as instant Green at the first gap, but it should allow delayed Stage2 when clinical/platform derisking and partner validation become real. LigaChem Bio required post-CA validation and later lifecycle 4B after the November peak.", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window_by_profile", "post_corporate_action_entry": true, "share_count_change_inside_window": true, "same_entry_group_id": "C24_BIO_DATA_141080_2024-04-24", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 0.5, "do_not_count_as_new_case": false, "source_proxy_only": true, "evidence_url_pending": true}
{"row_type": "trigger", "trigger_id": "TRG_R7L74-C24-298380-ABL-BISPECIFIC-PLATFORM-DATA-RERATING", "case_id": "R7L74-C24-298380-ABL-BISPECIFIC-PLATFORM-DATA-RERATING", "symbol": "298380", "company_name": "에이비엘바이오", "round": "R7", "loop": "74", "large_sector_id": "L7_BIO_HEALTHCARE_MEDICAL", "canonical_archetype_id": "C24_BIO_TRIAL_DATA_EVENT_RISK", "fine_archetype_id": "ADC_BISPECIFIC_PLATFORM_DATA_DERISKING_VS_IMMUNOTHERAPY_TRIAL_HEADLINE_FADE", "loop_objective": "coverage_gap_fill|counterexample_mining|trial_data_event_timing_test", "trigger_type": "Stage2-DelayedPositive-BispecificPlatformDataRerating", "trigger_date": "2024-03-05", "entry_date": "2024-03-06", "entry_price": 24550.0, "evidence_available_at_that_date": "BISPECIFIC_ANTIBODY_PLATFORM_CNS_BBB_CLINICAL_DATA_PARTNER_VALIDATION_BRIDGE", "evidence_source": "source_proxy_manual_verification_required:ABL_BIO_2024_BISPECIFIC_CNS_BBB_PLATFORM_CLINICAL_DATA_PARTNER_VALIDATION", "stage2_evidence_fields": ["trial_or_platform_data_candidate", "partner_validation_candidate", "endpoint_or_derisking_bridge_candidate"], "stage3_evidence_fields": ["relative_strength", "data_quality_or_partner_bridge_candidate"], "stage4b_evidence_fields": ["bridge_stale_or_absent", "MAE_widening", "post_peak_drawdown"], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/298/298380/2024.csv", "profile_path": "atlas/symbol_profiles/298/298380.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": 24.24, "MFE_90D_pct": 26.27, "MFE_180D_pct": 76.37, "MAE_30D_pct": -10.39, "MAE_90D_pct": -12.42, "MAE_180D_pct": -12.42, "peak_date": "2024-10-17", "peak_price": 43300.0, "drawdown_after_peak_pct": -39.15, "green_lateness_ratio": null, "four_b_local_peak_proximity": "local_4b_watch_after_trial_data_or_platform_peak_if_bridge_fades", "four_b_full_window_peak_proximity": "full_4b_requires_non_price_clinical_failure_endpoint_or_partner_break", "trigger_outcome_label": "delayed_positive_with_sharecount_validation", "current_profile_verdict": "C24 should distinguish platform-data derisking from simple biotech beta. ABL Bio had an early tradable MFE, then later re-accelerated into a larger 180D MFE; however later drawdown and share-count change require lifecycle and validation controls.", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window_by_profile", "post_corporate_action_entry": false, "share_count_change_inside_window": true, "same_entry_group_id": "C24_BIO_DATA_298380_2024-03-06", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 0.5, "do_not_count_as_new_case": false, "source_proxy_only": true, "evidence_url_pending": true}
{"row_type": "trigger", "trigger_id": "TRG_R7L74-C24-950220-NEOIMMUNETECH-IMMUNOTHERAPY-TRIAL-HEADLINE-FADE", "case_id": "R7L74-C24-950220-NEOIMMUNETECH-IMMUNOTHERAPY-TRIAL-HEADLINE-FADE", "symbol": "950220", "company_name": "네오이뮨텍", "round": "R7", "loop": "74", "large_sector_id": "L7_BIO_HEALTHCARE_MEDICAL", "canonical_archetype_id": "C24_BIO_TRIAL_DATA_EVENT_RISK", "fine_archetype_id": "ADC_BISPECIFIC_PLATFORM_DATA_DERISKING_VS_IMMUNOTHERAPY_TRIAL_HEADLINE_FADE", "loop_objective": "coverage_gap_fill|counterexample_mining|trial_data_event_timing_test", "trigger_type": "Stage2-FalsePositive / ImmunotherapyTrialHeadlineFade", "trigger_date": "2024-04-10", "entry_date": "2024-04-11", "entry_price": 1447.0, "evidence_available_at_that_date": "IMMUNOTHERAPY_TRIAL_HEADLINE_WITH_WEAK_DURABLE_DATA_COMMERCIALIZATION_BRIDGE", "evidence_source": "source_proxy_manual_verification_required:NEOIMMUNETECH_2024_IMMUNOTHERAPY_TRIAL_HEADLINE_ENDPOINT_DURABILITY_PARTNER_BRIDGE", "stage2_evidence_fields": ["trial_or_platform_data_candidate", "partner_validation_candidate", "endpoint_or_derisking_bridge_candidate"], "stage3_evidence_fields": ["relative_strength", "data_quality_or_partner_bridge_candidate"], "stage4b_evidence_fields": ["bridge_stale_or_absent", "MAE_widening", "post_peak_drawdown"], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/950/950220/2024.csv", "profile_path": "atlas/symbol_profiles/950/950220.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": 46.51, "MFE_90D_pct": 46.51, "MFE_180D_pct": 46.51, "MAE_30D_pct": -10.23, "MAE_90D_pct": -10.23, "MAE_180D_pct": -30.27, "peak_date": "2024-05-14", "peak_price": 2120.0, "drawdown_after_peak_pct": -52.41, "green_lateness_ratio": null, "four_b_local_peak_proximity": "local_4b_watch_after_trial_data_or_platform_peak_if_bridge_fades", "four_b_full_window_peak_proximity": "full_4b_requires_non_price_clinical_failure_endpoint_or_partner_break", "trigger_outcome_label": "counterexample", "current_profile_verdict": "C24 should not treat immunotherapy trial/headline spikes as durable Stage2 unless data quality, endpoint durability, partner path or commercialization bridge is visible. NeoImmuneTech had large MFE but later collapsed into high MAE and post-peak drawdown.", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window_by_profile", "post_corporate_action_entry": false, "share_count_change_inside_window": false, "same_entry_group_id": "C24_BIO_DATA_950220_2024-04-11", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 0.5, "do_not_count_as_new_case": false, "source_proxy_only": true, "evidence_url_pending": true}
```

### score simulation rows

```jsonl
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R7L74-C24-141080-LCB-ADC-PLATFORM-DATA-DERISKING", "trigger_id": "TRG_R7L74-C24-141080-LCB-ADC-PLATFORM-DATA-DERISKING", "symbol": "141080", "large_sector_id": "L7_BIO_HEALTHCARE_MEDICAL", "canonical_archetype_id": "C24_BIO_TRIAL_DATA_EVENT_RISK", "raw_component_scores_before": {"trial_data_quality_score": 14, "endpoint_durability_score": 12, "partner_validation_score": 13, "commercialization_bridge_score": 7, "relative_strength_score": 14, "execution_risk_score": 6, "dilution_or_sharecount_risk_score": 8, "source_confidence_score": 2}, "weighted_score_before": 80, "stage_label_before": "Delayed Stage2 candidate after source repair", "raw_component_scores_after": {"trial_data_quality_score": 16, "endpoint_durability_score": 14, "partner_validation_score": 15, "commercialization_bridge_score": 8, "relative_strength_score": 13, "execution_risk_score": 7, "dilution_or_sharecount_risk_score": 10, "source_confidence_score": 2}, "weighted_score_after": 86, "stage_label_after": "Delayed Stage2/Yellow candidate after source repair + lifecycle 4B", "changed_components": ["trial_data_quality_score", "partner_validation_score", "execution_risk_score", "dilution_or_sharecount_risk_score"], "component_delta_explanation": "Reward trial/platform data only when data quality, endpoint durability, partner validation and commercialization bridge are verified; cap headline spikes that later open MAE and drawdown.", "MFE_90D_pct": 28.24, "MAE_90D_pct": -10.88, "score_return_alignment_label": "delayed_positive_with_lifecycle_4b", "current_profile_verdict": "C24 should not treat a biotech data/platform event as instant Green at the first gap, but it should allow delayed Stage2 when clinical/platform derisking and partner validation become real. LigaChem Bio required post-CA validation and later lifecycle 4B after the November peak."}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R7L74-C24-298380-ABL-BISPECIFIC-PLATFORM-DATA-RERATING", "trigger_id": "TRG_R7L74-C24-298380-ABL-BISPECIFIC-PLATFORM-DATA-RERATING", "symbol": "298380", "large_sector_id": "L7_BIO_HEALTHCARE_MEDICAL", "canonical_archetype_id": "C24_BIO_TRIAL_DATA_EVENT_RISK", "raw_component_scores_before": {"trial_data_quality_score": 14, "endpoint_durability_score": 12, "partner_validation_score": 13, "commercialization_bridge_score": 7, "relative_strength_score": 14, "execution_risk_score": 6, "dilution_or_sharecount_risk_score": 8, "source_confidence_score": 2}, "weighted_score_before": 80, "stage_label_before": "Delayed Stage2 candidate after source repair", "raw_component_scores_after": {"trial_data_quality_score": 16, "endpoint_durability_score": 14, "partner_validation_score": 15, "commercialization_bridge_score": 8, "relative_strength_score": 13, "execution_risk_score": 7, "dilution_or_sharecount_risk_score": 10, "source_confidence_score": 2}, "weighted_score_after": 86, "stage_label_after": "Delayed Stage2/Yellow candidate after source repair + lifecycle 4B", "changed_components": ["trial_data_quality_score", "partner_validation_score", "execution_risk_score", "dilution_or_sharecount_risk_score"], "component_delta_explanation": "Reward trial/platform data only when data quality, endpoint durability, partner validation and commercialization bridge are verified; cap headline spikes that later open MAE and drawdown.", "MFE_90D_pct": 26.27, "MAE_90D_pct": -12.42, "score_return_alignment_label": "delayed_positive_with_lifecycle_4b", "current_profile_verdict": "C24 should distinguish platform-data derisking from simple biotech beta. ABL Bio had an early tradable MFE, then later re-accelerated into a larger 180D MFE; however later drawdown and share-count change require lifecycle and validation controls."}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R7L74-C24-950220-NEOIMMUNETECH-IMMUNOTHERAPY-TRIAL-HEADLINE-FADE", "trigger_id": "TRG_R7L74-C24-950220-NEOIMMUNETECH-IMMUNOTHERAPY-TRIAL-HEADLINE-FADE", "symbol": "950220", "large_sector_id": "L7_BIO_HEALTHCARE_MEDICAL", "canonical_archetype_id": "C24_BIO_TRIAL_DATA_EVENT_RISK", "raw_component_scores_before": {"trial_data_quality_score": 5, "endpoint_durability_score": 3, "partner_validation_score": 2, "commercialization_bridge_score": 1, "relative_strength_score": 8, "execution_risk_score": 16, "dilution_or_sharecount_risk_score": 0, "source_confidence_score": 2}, "weighted_score_before": 54, "stage_label_before": "Stage2-FalsePositive / local 4B-watch", "raw_component_scores_after": {"trial_data_quality_score": 3, "endpoint_durability_score": 2, "partner_validation_score": 1, "commercialization_bridge_score": 1, "relative_strength_score": 5, "execution_risk_score": 18, "dilution_or_sharecount_risk_score": 0, "source_confidence_score": 2}, "weighted_score_after": 43, "stage_label_after": "Stage4B-local-watch / no durable Green", "changed_components": ["trial_data_quality_score", "partner_validation_score", "execution_risk_score", "dilution_or_sharecount_risk_score"], "component_delta_explanation": "Reward trial/platform data only when data quality, endpoint durability, partner validation and commercialization bridge are verified; cap headline spikes that later open MAE and drawdown.", "MFE_90D_pct": 46.51, "MAE_90D_pct": -10.23, "score_return_alignment_label": "false_positive_trial_headline_bridge_gap", "current_profile_verdict": "C24 should not treat immunotherapy trial/headline spikes as durable Stage2 unless data quality, endpoint durability, partner path or commercialization bridge is visible. NeoImmuneTech had large MFE but later collapsed into high MAE and post-peak drawdown."}
```

### aggregate row

```jsonl
{"row_type": "aggregate", "round": "R7", "loop": 74, "large_sector_id": "L7_BIO_HEALTHCARE_MEDICAL", "canonical_archetype_id": "C24_BIO_TRIAL_DATA_EVENT_RISK", "fine_archetype_id": "ADC_BISPECIFIC_PLATFORM_DATA_DERISKING_VS_IMMUNOTHERAPY_TRIAL_HEADLINE_FADE", "calibration_usable_case_count": 3, "calibration_usable_trigger_count": 3, "new_independent_case_count": 3, "reused_case_count": 0, "same_archetype_new_symbol_count": 3, "same_archetype_new_trigger_family_count": 3, "positive_case_count": 2, "counterexample_count": 1, "four_b_case_count": 3, "four_c_case_count": 0, "source_proxy_only_count": 3, "evidence_url_pending_count": 3, "share_count_change_inside_window_count": 2, "post_corporate_action_entry_count": 1, "current_profile_error_count": 1, "diversity_score_summary": "+3 underused C24 symbols outside top-covered set, +3 ADC/bispecific/immunotherapy trigger families, +2 delayed platform-data positives, +1 immunotherapy headline fade counterexample, no hard duplicate", "residual_contribution_label": "coverage_gap_fill_with_source_repair_and_sharecount_validation_needed"}
```

### shadow weight row

```jsonl
{"row_type": "shadow_weight", "round": "R7", "loop": 74, "large_sector_id": "L7_BIO_HEALTHCARE_MEDICAL", "canonical_archetype_id": "C24_BIO_TRIAL_DATA_EVENT_RISK", "axis": "adc_bispecific_platform_data_derisking_vs_immunotherapy_trial_headline_fade", "decision": "hold_for_source_repair_and_more_evidence", "proposed_runtime_effect": "C24 should split verified platform/trial data derisking from headline-only trial spikes. Stage2 requires data quality, endpoint durability, partner validation or commercialization bridge. If the initial gap opens MAE or later drawdown without bridge refresh, route to local 4B-watch. Delayed winners should survive only after source repair and share-count validation.", "do_not_propose_new_weight_delta": true, "needs_more_evidence": true, "source_repair_required": ["141080", "298380", "950220"], "share_count_validation_required": ["141080", "298380"]}
```

### residual contribution row

```jsonl
{"row_type": "residual_contribution", "round": "R7", "loop": 74, "large_sector_id": "L7_BIO_HEALTHCARE_MEDICAL", "canonical_archetype_id": "C24_BIO_TRIAL_DATA_EVENT_RISK", "existing_axis_strengthened": ["stage2_required_bridge", "price_only_blowoff_blocks_positive_stage", "local_4b_watch_guard", "delayed_positive_protection"], "new_axis_proposed": null, "sector_specific_rule_candidate": true, "canonical_archetype_rule_candidate": true, "narrative_summary": "C24 needs trial/platform data proof. LigaChem Bio and ABL Bio show delayed platform-data positives with lifecycle local 4B; NeoImmuneTech shows immunotherapy trial headline fade into local 4B when endpoint/partner/commercial bridge fails to refresh."}
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
  corporate_action_candidate_dates = 2020-07-07, 2024-04-23
  selected window = 2024-04-24~D+180
  contamination = false because entry is after the 2024-04-23 candidate
  share_count_change_inside_window = true → coding-agent validation required

298380:
  corporate_action_candidate_dates = none
  selected window = 2024-03-06~D+180
  contamination = false
  share_count_change_inside_window = true → coding-agent validation required

950220:
  corporate_action_candidate_dates = 2025-09-30
  selected window = 2024-04-11~D+180
  contamination = false
```

Data-quality caveat:

```text
All selected C24 rows are source_proxy_only / evidence_url_pending.
141080 and 298380 also require share-count validation before runtime promotion.
This MD is useful for stock-web path calibration and C24 rule-shape discovery,
but coding-agent promotion requires non-proxy trial data, endpoint durability, partner validation, regulatory or commercialization evidence.
```

---

## Deferred Coding Agent Handoff Prompt

Do not execute this now.

```text
You are the coding agent for Songdaiki/stock_agent.

Read this standalone v12 residual research MD and ingest machine-readable rows only after validation.

Do not patch production scoring blindly.
This R7/C24 artifact is marked do_not_propose_new_weight_delta=true because all rows need source repair.

Candidate axis:
adc_bispecific_platform_data_derisking_vs_immunotherapy_trial_headline_fade

Required checks before implementation:
1. Validate all trigger rows against stock-web tradable_raw OHLC shards.
2. Confirm no hard duplicate key:
   canonical_archetype_id + symbol + trigger_type + entry_date.
3. Verify non-proxy source URLs for 141080, 298380 and 950220.
4. Validate 141080 post-corporate-action basis and share-count changes.
5. Validate 298380 share-count changes inside the selected window.
6. Keep generic C24 bio-headline weight unchanged until source repair is complete.
7. Consider Stage2 only when:
   - clinical/platform data quality is explicit,
   - endpoint durability or response quality is visible,
   - partner validation, regulatory path or commercialization bridge exists,
   - MAE remains controlled or the signal is deliberately delayed after early drawdown.
8. Consider local 4B-watch when:
   - the trigger is trial/data headline only,
   - endpoint or partner evidence is weak/stale,
   - MAE_90D <= -20% or MAE_180D <= -25%,
   - post-peak drawdown <= -35%.
9. Do not convert local 4B-watch into full 4B/4C without non-price clinical failure, regulatory halt, endpoint miss, partnership break, financing or solvency evidence.
10. Emit before/after diagnostics and reject if verified delayed platform-data positives are overblocked.
```

---

## Final round state

```text
completed_round = R7
completed_loop = 74
next_round = R8
next_loop = 74
round_schedule_status = valid
round_sector_consistency = pass
```

