# E2R Stock-Web v12 Residual Research — R7 Loop 81 / L7 / C23

## Metadata

```json
{
  "research_session": "post_calibrated_sector_archetype_residual_research",
  "mode": "historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12",
  "scheduled_round": "R7",
  "scheduled_loop": 81,
  "round_schedule_status": "valid",
  "round_sector_consistency": "pass",
  "completed_round": "R7",
  "completed_loop": 81,
  "computed_next_round": "R8",
  "computed_next_loop": 81,
  "large_sector_id": "L7_BIO_HEALTHCARE_MEDICAL",
  "canonical_archetype_id": "C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION",
  "fine_archetype_id": "BIOSIMILAR_APPROVAL_PARTNER_COMMERCIALIZATION_BRIDGE_VS_VACCINE_PLATFORM_THEME_FADE",
  "loop_objective": [
    "coverage_gap_fill",
    "counterexample_mining",
    "4B_non_price_requirement_stress_test",
    "bio_regulatory_approval_commercialization_guardrail",
    "biosimilar_approval_partner_commercialization_revenue_margin_bridge",
    "vaccine_platform_commercialization_theme_fade_boundary",
    "post_corporate_action_validation_queue_creation",
    "share_count_validation_queue_creation",
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

Previous completed state in this interactive run: R6 / loop 81.

Therefore:

```text
scheduled_round = R7
scheduled_loop = 81
allowed_large_sector = L7_BIO_HEALTHCARE_MEDICAL
selected_large_sector = L7_BIO_HEALTHCARE_MEDICAL
selected_canonical_archetype_id = C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION
computed_next_round = R8
computed_next_loop = 81
```

R7 was routed to C23 because loop 80 R7 used C24 and loop 79 R7 used C25.  
This file tests regulatory approval / biosimilar commercialization / vaccine platform commercialization bridges.

## No-Repeat / novelty check

No hard duplicate is intentionally reused.

Hard duplicate key checked conceptually:

```text
canonical_archetype_id + symbol + trigger_type + entry_date
```

No-Repeat shows C23 concentration in:

```text
000100, 028300, UNKNOWN_SYMBOL, 145020, 196170
```

This run uses three different symbols:

```text
000250 / 삼천당제약 / biosimilar approval and partner commercialization bridge
068270 / 셀트리온 / biosimilar commercialization bridge with post-CA/share-count validation
302440 / SK바이오사이언스 / vaccine platform commercialization theme fade
```

Data-quality note:

```text
All three rows are stock-web calibration usable by profile-level corporate-action candidates.
All three rows are source_proxy_only=true / evidence_url_pending=true.
068270 requires post-corporate-action and share-count validation.
302440 requires share-count validation because the 2024 shard shows share-count changes despite no profile-level 2024 CA candidate.
```

## Research thesis

C23 is not “바이오 승인 뉴스가 떴다.”

The mechanism must pass through:

```text
regulatory approval / commercialization event
→ partner, license or procurement economics
→ supply or manufacturing readiness
→ launch timing and revenue conversion
→ margin bridge
→ durable rerating
```

승인 뉴스는 문을 여는 열쇠다.  
C23이 보려는 것은 문이 열린 뒤 실제 파트너 계약, 출하, 매출, 마진이 방 안으로 들어오는지다.

---

## Case 1 — Biosimilar approval / partner commercialization positive: 000250 / 삼천당제약

### Evidence status

```text
source_proxy_only = true
evidence_url_pending = true
source_repair_required = true
```

The source-repair task is biosimilar approval, partner/license economics, supply agreement, launch timing, revenue conversion and margin bridge evidence.

```text
evidence_family = BIOSIMILAR_APPROVAL_PARTNER_LICENSE_SUPPLY_COMMERCIALIZATION_REVENUE_MARGIN_BRIDGE
case_role = positive_biosimilar_approval_partner_commercialization_with_later_4b_watch
trigger_date = 2024-01-31
entry_date = 2024-02-01
entry_price = 63,900
```

### Stock-Web price path

Observed rows from `atlas/ohlcv_tradable_by_symbol_year/000/000250/2024.csv`:

```text
2024-02-01,63900,64800,61900,64200
2024-02-23,70200,76000,70100,73500
2024-03-18,79400,87700,77800,86500
2024-03-25,103000,111100,102700,111100
2024-03-26,118100,143400,117000,140400
2024-07-24,187000,189100,181000,185200
2024-08-05,172000,174900,145500,152600
2024-10-25,123700,130500,122300,125900
```

### Backtest

```text
MFE_30D  = +39.28%
MAE_30D  = -3.13%
MFE_90D  = +132.71%
MAE_90D  = -3.13%
MFE_180D = +195.93%
MAE_180D = -3.13%
peak_180 = 189,100 on 2024-07-24
trough_180 = 61,900 on 2024-02-01
peak_to_later_drawdown = -35.32%
```

### Interpretation

This is a strong C23 approval-commercialization positive.  
But it still cannot be promoted from price alone; approval, partner economics, supply and revenue/margin bridge must be source-repaired.

Correct treatment:

```text
verified approval / partner-license / supply / commercialization / margin bridge → Stage2 possible
bridge stale after peak → lifecycle local 4B-watch
```

---

## Case 2 — Bounded biosimilar commercialization positive: 068270 / 셀트리온

### Evidence status

```text
source_proxy_only = true
evidence_url_pending = true
post_corporate_action_validation_required = true
share_count_validation_required = true
source_repair_required = true
```

The source-repair task is biosimilar approval/switching, commercialization/export revenue and margin bridge evidence.

```text
evidence_family = BIOSIMILAR_APPROVAL_SWITCHING_COMMERCIALIZATION_EXPORT_REVENUE_MARGIN_BRIDGE_POST_CA
case_role = positive_bounded_biosimilar_commercialization_with_postCA_sharecount_validation
trigger_date = 2024-01-31
entry_date = 2024-02-01
entry_price = 177,700
```

### Stock-Web price path

Observed rows from `atlas/ohlcv_tradable_by_symbol_year/068/068270/2024.csv`:

```text
2024-02-01,177700,179800,173700,178700
2024-02-27,182000,191400,181300,190100
2024-03-29,184000,192800,184000,191200
2024-07-29,203000,210000,202000,209000
2024-08-05,188300,195300,173000,182500
2024-09-23,203000,211000,203000,205000
2024-10-31,187000,187500,182500,182500
```

### Backtest

```text
MFE_30D  = +8.83%
MAE_30D  = -2.25%
MFE_90D  = +8.83%
MAE_90D  = -2.25%
MFE_180D = +18.74%
MAE_180D = -2.64%
peak_180 = 211,000 on 2024-09-23
trough_180 = 173,000 on 2024-08-05
peak_to_later_drawdown = -13.51%
```

### Interpretation

This is not an explosive row, but it is also not a false-positive fade.  
The correct label is bounded commercialization candidate after post-CA/share-count validation.

Correct treatment:

```text
post-CA/share-count validation first
verified biosimilar commercialization / export revenue / margin bridge → Stage2-Yellow possible
no forced 4B while MAE is controlled and non-price break is absent
```

---

## Case 3 — Counterexample / local 4B: 302440 / SK바이오사이언스

### Evidence status

```text
source_proxy_only = true
evidence_url_pending = true
share_count_validation_required = true
source_repair_required = true
```

This row tests vaccine platform / commercialization theme beta without enough order/procurement, manufacturing utilization, revenue and margin bridge.

```text
evidence_family = VACCINE_PLATFORM_REGULATORY_COMMERCIALIZATION_THEME_WITH_WEAK_ORDER_REVENUE_MARGIN_BRIDGE
case_role = counterexample_vaccine_platform_commercialization_theme_local4b
trigger_date = 2024-01-31
entry_date = 2024-02-01
entry_price = 62,900
```

### Stock-Web price path

Observed rows from `atlas/ohlcv_tradable_by_symbol_year/302/302440/2024.csv`:

```text
2024-02-01,62900,64600,62700,64100
2024-02-07,64400,65400,63900,64800
2024-02-29,61800,62400,60800,61400
2024-04-03,60500,60600,59500,59500
2024-07-24,53700,55500,53600,54500
2024-08-05,55600,55600,48600,49350
2024-08-12,56400,61500,56300,58700
2024-10-25,56100,56100,52000,52300
```

### Backtest

```text
MFE_30D  = +3.97%
MAE_30D  = -3.34%
MFE_90D  = +3.97%
MAE_90D  = -7.95%
MFE_180D = +3.97%
MAE_180D = -22.73%
peak_180 = 65,400 on 2024-02-07
trough_180 = 48,600 on 2024-08-05
peak_to_later_drawdown = -25.69%
```

### Interpretation

This is a C23 vaccine/platform commercialization false-positive boundary.  
The price path did not validate durable procurement, revenue or manufacturing-utilization rerating.

Correct treatment:

```text
vaccine platform / commercialization theme beta
→ no verified procurement / order / utilization / revenue / margin bridge
→ local 4B-watch
```

---

## Cross-case residual finding

### What this strengthens

```text
stage2_required_bridge = strengthen
regulatory_approval_commercialization_bridge_required = strengthen
partner_license_revenue_margin_bridge_guard = strengthen
price_only_blowoff_blocks_positive_stage = strengthen
local_4b_watch_guard = strengthen
post_corporate_action_validation_guard = strengthen
share_count_validation_guard = strengthen
full_4b_requires_non_price_evidence = keep
```

### What this does not justify

```text
do_not_raise_generic_C23_bio_approval_theme_weight = true
do_not_treat_all_bio_approval_MFE_as_Green = true
do_not_ingest_post_CA_or_sharecount_changed_rows_without_validation = true
do_not_convert_bio_commercialization_drawdown_to_hard_4C_without_non_price_approval_procurement_partner_or_margin_break = true
```

### Candidate canonical compression

Fine labels can compress into:

```text
BIOSIMILAR_APPROVAL_PARTNER_COMMERCIALIZATION_BRIDGE_VS_VACCINE_PLATFORM_THEME_FADE
```

This fine archetype covers:

```text
1. biosimilar approval / partner-license commercialization bridge → Stage2 possible after source repair
2. large-cap biosimilar commercialization with controlled MAE → Stage2-Yellow after validation, no forced 4B
3. vaccine platform commercialization beta without procurement/revenue bridge → false Stage2 / local 4B
```

---

## Machine-readable rows

### price source validation row

```jsonl
{"row_type": "price_source_validation", "source": "Songdaiki/stock-web", "source_url": "https://github.com/Songdaiki/stock-web", "manifest_path": "atlas/manifest.json", "schema_path": "atlas/schema.json", "universe_path": "atlas/universe/all_symbols.csv", "manifest_max_date": "2026-02-20", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "raw_shard_root": "atlas/ohlcv_raw_by_symbol_year", "validation_status": "usable_for_historical_calibration"}
```

### case rows

```jsonl
{"row_type": "case", "case_id": "R7L81-C23-000250-SCD-BIOSIMILAR-APPROVAL-PARTNER-COMMERCIALIZATION", "symbol": "000250", "company_name": "삼천당제약", "round": "R7", "loop": "81", "large_sector_id": "L7_BIO_HEALTHCARE_MEDICAL", "canonical_archetype_id": "C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION", "fine_archetype_id": "BIOSIMILAR_APPROVAL_PARTNER_COMMERCIALIZATION_BRIDGE_VS_VACCINE_PLATFORM_THEME_FADE", "case_type": "bio_regulatory_approval_commercialization", "positive_or_counterexample": "positive", "best_trigger": "Stage2-Actionable-BiosimilarApprovalPartnerCommercializationBridgeWithLifecycle4B", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 0.5, "score_price_alignment": "C23 should protect regulatory/commercialization positives only when approval, partner/license economics, supply agreement, launch timing, revenue conversion and margin bridge are visible. Samchundang Pharm produced very large MFE with shallow early MAE, but post-peak drawdown requires lifecycle 4B if commercialization evidence fades.", "current_profile_verdict": "source_repair_required_before_runtime_weight", "price_source": "Songdaiki/stock-web", "notes": "Stock-web path usable; non-proxy product approval, partner/license economics, procurement/order visibility, supply/manufacturing, commercialization, revenue conversion and margin bridge evidence required before runtime promotion."}
{"row_type": "case", "case_id": "R7L81-C23-068270-CELLTRION-BIOSIMILAR-COMMERCIALIZATION-POSTCA", "symbol": "068270", "company_name": "셀트리온", "round": "R7", "loop": "81", "large_sector_id": "L7_BIO_HEALTHCARE_MEDICAL", "canonical_archetype_id": "C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION", "fine_archetype_id": "BIOSIMILAR_APPROVAL_PARTNER_COMMERCIALIZATION_BRIDGE_VS_VACCINE_PLATFORM_THEME_FADE", "case_type": "bio_regulatory_approval_commercialization", "positive_or_counterexample": "positive", "best_trigger": "Stage2-Yellow-BiosimilarCommercializationBridgeWithPostCAAndSharecountValidation", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 0.5, "score_price_alignment": "C23 should not overblock large-cap biosimilar commercialization rows when MAE is controlled and commercialization/export revenue bridge may be visible. Celltrion requires post-CA and share-count continuity validation because the profile flags a 2024-01-12 corporate-action candidate and the 2024 shard shows share-count changes.", "current_profile_verdict": "source_repair_required_before_runtime_weight", "price_source": "Songdaiki/stock-web", "notes": "Stock-web path usable; non-proxy product approval, partner/license economics, procurement/order visibility, supply/manufacturing, commercialization, revenue conversion and margin bridge evidence required before runtime promotion."}
{"row_type": "case", "case_id": "R7L81-C23-302440-SK-BIOSCIENCE-VACCINE-COMMERCIALIZATION-THEME-FADE", "symbol": "302440", "company_name": "SK바이오사이언스", "round": "R7", "loop": "81", "large_sector_id": "L7_BIO_HEALTHCARE_MEDICAL", "canonical_archetype_id": "C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION", "fine_archetype_id": "BIOSIMILAR_APPROVAL_PARTNER_COMMERCIALIZATION_BRIDGE_VS_VACCINE_PLATFORM_THEME_FADE", "case_type": "bio_regulatory_approval_commercialization", "positive_or_counterexample": "counterexample", "best_trigger": "Stage2-FalsePositive / VaccinePlatformCommercializationThemeFadeWithLocal4BWatch", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 0.5, "score_price_alignment": "C23 should not treat vaccine platform or regulatory commercialization theme beta as durable Stage2 unless product approval, procurement/order visibility, manufacturing utilization, revenue conversion and margin bridge are visible. SK Bioscience had tiny MFE and then a high-MAE fade.", "current_profile_verdict": "source_repair_required_before_runtime_weight", "price_source": "Songdaiki/stock-web", "notes": "Stock-web path usable; non-proxy product approval, partner/license economics, procurement/order visibility, supply/manufacturing, commercialization, revenue conversion and margin bridge evidence required before runtime promotion."}
```

### trigger rows

```jsonl
{"row_type": "trigger", "trigger_id": "TRG_R7L81-C23-000250-SCD-BIOSIMILAR-APPROVAL-PARTNER-COMMERCIALIZATION", "case_id": "R7L81-C23-000250-SCD-BIOSIMILAR-APPROVAL-PARTNER-COMMERCIALIZATION", "symbol": "000250", "company_name": "삼천당제약", "round": "R7", "loop": "81", "large_sector_id": "L7_BIO_HEALTHCARE_MEDICAL", "canonical_archetype_id": "C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION", "fine_archetype_id": "BIOSIMILAR_APPROVAL_PARTNER_COMMERCIALIZATION_BRIDGE_VS_VACCINE_PLATFORM_THEME_FADE", "loop_objective": "coverage_gap_fill|counterexample_mining|bio_regulatory_commercialization_guardrail", "trigger_type": "Stage2-Actionable-BiosimilarApprovalPartnerCommercializationBridgeWithLifecycle4B", "trigger_date": "2024-01-31", "entry_date": "2024-02-01", "entry_price": 63900.0, "evidence_available_at_that_date": "BIOSIMILAR_APPROVAL_PARTNER_LICENSE_SUPPLY_COMMERCIALIZATION_REVENUE_MARGIN_BRIDGE", "evidence_source": "source_proxy_manual_verification_required:SAMCHUNDANG_PHARM_2024_BIOSIMILAR_APPROVAL_PARTNER_LICENSE_SUPPLY_COMMERCIALIZATION_REVENUE_MARGIN_BRIDGE", "stage2_evidence_fields": ["approval_or_regulatory_event_candidate", "partner_license_or_procurement_candidate", "commercialization_revenue_margin_bridge_candidate"], "stage3_evidence_fields": ["relative_strength", "supply_manufacturing_or_export_candidate"], "stage4b_evidence_fields": ["bio_commercialization_theme_beta", "bridge_stale_or_absent", "MAE_widening", "post_peak_drawdown"], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/000/000250/2024.csv", "profile_path": "atlas/symbol_profiles/000/000250.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": 39.28, "MFE_90D_pct": 132.71, "MFE_180D_pct": 195.93, "MAE_30D_pct": -3.13, "MAE_90D_pct": -3.13, "MAE_180D_pct": -3.13, "peak_date": "2024-07-24", "peak_price": 189100.0, "drawdown_after_peak_pct": -35.32, "green_lateness_ratio": null, "four_b_local_peak_proximity": "local_4b_watch_after_bio_commercialization_peak_if_approval_partner_revenue_or_margin_bridge_fades", "four_b_full_window_peak_proximity": "full_4b_requires_non_price_approval_failure_procurement_failure_partner_loss_margin_or_financing_break", "trigger_outcome_label": "positive_biosimilar_approval_partner_commercialization_with_later_4b_watch", "current_profile_verdict": "C23 should protect regulatory/commercialization positives only when approval, partner/license economics, supply agreement, launch timing, revenue conversion and margin bridge are visible. Samchundang Pharm produced very large MFE with shallow early MAE, but post-peak drawdown requires lifecycle 4B if commercialization evidence fades.", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window_by_profile_or_post_CA_sharecount_validation_required", "share_count_change_inside_window": false, "same_entry_group_id": "C23_BIO_REGULATORY_COMMERCIALIZATION_000250_2024-02-01", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 0.5, "do_not_count_as_new_case": false, "source_proxy_only": true, "evidence_url_pending": true}
{"row_type": "trigger", "trigger_id": "TRG_R7L81-C23-068270-CELLTRION-BIOSIMILAR-COMMERCIALIZATION-POSTCA", "case_id": "R7L81-C23-068270-CELLTRION-BIOSIMILAR-COMMERCIALIZATION-POSTCA", "symbol": "068270", "company_name": "셀트리온", "round": "R7", "loop": "81", "large_sector_id": "L7_BIO_HEALTHCARE_MEDICAL", "canonical_archetype_id": "C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION", "fine_archetype_id": "BIOSIMILAR_APPROVAL_PARTNER_COMMERCIALIZATION_BRIDGE_VS_VACCINE_PLATFORM_THEME_FADE", "loop_objective": "coverage_gap_fill|counterexample_mining|bio_regulatory_commercialization_guardrail", "trigger_type": "Stage2-Yellow-BiosimilarCommercializationBridgeWithPostCAAndSharecountValidation", "trigger_date": "2024-01-31", "entry_date": "2024-02-01", "entry_price": 177700.0, "evidence_available_at_that_date": "BIOSIMILAR_APPROVAL_SWITCHING_COMMERCIALIZATION_EXPORT_REVENUE_MARGIN_BRIDGE_POST_CA", "evidence_source": "source_proxy_manual_verification_required:CELLTRION_2024_BIOSIMILAR_APPROVAL_SWITCHING_COMMERCIALIZATION_EXPORT_REVENUE_MARGIN_BRIDGE_POST_CA", "stage2_evidence_fields": ["approval_or_regulatory_event_candidate", "partner_license_or_procurement_candidate", "commercialization_revenue_margin_bridge_candidate"], "stage3_evidence_fields": ["relative_strength", "supply_manufacturing_or_export_candidate"], "stage4b_evidence_fields": ["bio_commercialization_theme_beta", "bridge_stale_or_absent", "MAE_widening", "post_peak_drawdown"], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/068/068270/2024.csv", "profile_path": "atlas/symbol_profiles/068/068270.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": 8.83, "MFE_90D_pct": 8.83, "MFE_180D_pct": 18.74, "MAE_30D_pct": -2.25, "MAE_90D_pct": -2.25, "MAE_180D_pct": -2.64, "peak_date": "2024-09-23", "peak_price": 211000.0, "drawdown_after_peak_pct": -13.51, "green_lateness_ratio": null, "four_b_local_peak_proximity": "local_4b_watch_after_bio_commercialization_peak_if_approval_partner_revenue_or_margin_bridge_fades", "four_b_full_window_peak_proximity": "full_4b_requires_non_price_approval_failure_procurement_failure_partner_loss_margin_or_financing_break", "trigger_outcome_label": "positive_bounded_biosimilar_commercialization_with_postCA_sharecount_validation", "current_profile_verdict": "C23 should not overblock large-cap biosimilar commercialization rows when MAE is controlled and commercialization/export revenue bridge may be visible. Celltrion requires post-CA and share-count continuity validation because the profile flags a 2024-01-12 corporate-action candidate and the 2024 shard shows share-count changes.", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window_by_profile_or_post_CA_sharecount_validation_required", "share_count_change_inside_window": true, "same_entry_group_id": "C23_BIO_REGULATORY_COMMERCIALIZATION_068270_2024-02-01", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 0.5, "do_not_count_as_new_case": false, "source_proxy_only": true, "evidence_url_pending": true}
{"row_type": "trigger", "trigger_id": "TRG_R7L81-C23-302440-SK-BIOSCIENCE-VACCINE-COMMERCIALIZATION-THEME-FADE", "case_id": "R7L81-C23-302440-SK-BIOSCIENCE-VACCINE-COMMERCIALIZATION-THEME-FADE", "symbol": "302440", "company_name": "SK바이오사이언스", "round": "R7", "loop": "81", "large_sector_id": "L7_BIO_HEALTHCARE_MEDICAL", "canonical_archetype_id": "C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION", "fine_archetype_id": "BIOSIMILAR_APPROVAL_PARTNER_COMMERCIALIZATION_BRIDGE_VS_VACCINE_PLATFORM_THEME_FADE", "loop_objective": "coverage_gap_fill|counterexample_mining|bio_regulatory_commercialization_guardrail", "trigger_type": "Stage2-FalsePositive / VaccinePlatformCommercializationThemeFadeWithLocal4BWatch", "trigger_date": "2024-01-31", "entry_date": "2024-02-01", "entry_price": 62900.0, "evidence_available_at_that_date": "VACCINE_PLATFORM_REGULATORY_COMMERCIALIZATION_THEME_WITH_WEAK_ORDER_REVENUE_MARGIN_BRIDGE", "evidence_source": "source_proxy_manual_verification_required:SK_BIOSCIENCE_2024_VACCINE_PLATFORM_APPROVAL_PROCUREMENT_MANUFACTURING_REVENUE_MARGIN_BRIDGE", "stage2_evidence_fields": ["approval_or_regulatory_event_candidate", "partner_license_or_procurement_candidate", "commercialization_revenue_margin_bridge_candidate"], "stage3_evidence_fields": ["relative_strength", "supply_manufacturing_or_export_candidate"], "stage4b_evidence_fields": ["bio_commercialization_theme_beta", "bridge_stale_or_absent", "MAE_widening", "post_peak_drawdown"], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/302/302440/2024.csv", "profile_path": "atlas/symbol_profiles/302/302440.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": 3.97, "MFE_90D_pct": 3.97, "MFE_180D_pct": 3.97, "MAE_30D_pct": -3.34, "MAE_90D_pct": -7.95, "MAE_180D_pct": -22.73, "peak_date": "2024-02-07", "peak_price": 65400.0, "drawdown_after_peak_pct": -25.69, "green_lateness_ratio": null, "four_b_local_peak_proximity": "local_4b_watch_after_bio_commercialization_peak_if_approval_partner_revenue_or_margin_bridge_fades", "four_b_full_window_peak_proximity": "full_4b_requires_non_price_approval_failure_procurement_failure_partner_loss_margin_or_financing_break", "trigger_outcome_label": "counterexample_vaccine_platform_commercialization_theme_local4b", "current_profile_verdict": "C23 should not treat vaccine platform or regulatory commercialization theme beta as durable Stage2 unless product approval, procurement/order visibility, manufacturing utilization, revenue conversion and margin bridge are visible. SK Bioscience had tiny MFE and then a high-MAE fade.", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window_by_profile_or_post_CA_sharecount_validation_required", "share_count_change_inside_window": true, "same_entry_group_id": "C23_BIO_REGULATORY_COMMERCIALIZATION_302440_2024-02-01", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 0.5, "do_not_count_as_new_case": false, "source_proxy_only": true, "evidence_url_pending": true}
```

### score simulation rows

```jsonl
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R7L81-C23-000250-SCD-BIOSIMILAR-APPROVAL-PARTNER-COMMERCIALIZATION", "trigger_id": "TRG_R7L81-C23-000250-SCD-BIOSIMILAR-APPROVAL-PARTNER-COMMERCIALIZATION", "symbol": "000250", "large_sector_id": "L7_BIO_HEALTHCARE_MEDICAL", "canonical_archetype_id": "C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION", "raw_component_scores_before": {"regulatory_approval_score": 14, "partner_license_or_procurement_score": 14, "commercialization_timing_score": 13, "revenue_conversion_score": 13, "margin_bridge_score": 13, "relative_strength_score": 14, "validation_risk": 0, "execution_risk_score": 10, "source_confidence_score": 2}, "weighted_score_before": 80, "stage_label_before": "Stage2/Yellow candidate after source repair", "raw_component_scores_after": {"regulatory_approval_score": 16, "partner_license_or_procurement_score": 16, "commercialization_timing_score": 15, "revenue_conversion_score": 15, "margin_bridge_score": 15, "relative_strength_score": 13, "validation_risk": 0, "execution_risk_score": 11, "source_confidence_score": 2}, "weighted_score_after": 86, "stage_label_after": "Stage2/Yellow after source repair + lifecycle 4B", "changed_components": ["regulatory_approval_score", "partner_license_or_procurement_score", "commercialization_timing_score", "revenue_conversion_score", "margin_bridge_score", "execution_risk_score"], "component_delta_explanation": "Reward only verified product approval, partner/license/procurement economics, launch or commercialization timing, revenue conversion and margin bridge; cap vaccine/platform commercialization theme beta when bridge fails to refresh.", "MFE_90D_pct": 132.71, "MAE_90D_pct": -3.13, "score_return_alignment_label": "bio_approval_commercialization_positive_with_lifecycle_4b", "current_profile_verdict": "C23 should protect regulatory/commercialization positives only when approval, partner/license economics, supply agreement, launch timing, revenue conversion and margin bridge are visible. Samchundang Pharm produced very large MFE with shallow early MAE, but post-peak drawdown requires lifecycle 4B if commercialization evidence fades."}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R7L81-C23-068270-CELLTRION-BIOSIMILAR-COMMERCIALIZATION-POSTCA", "trigger_id": "TRG_R7L81-C23-068270-CELLTRION-BIOSIMILAR-COMMERCIALIZATION-POSTCA", "symbol": "068270", "large_sector_id": "L7_BIO_HEALTHCARE_MEDICAL", "canonical_archetype_id": "C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION", "raw_component_scores_before": {"regulatory_approval_score": 14, "partner_license_or_procurement_score": 14, "commercialization_timing_score": 13, "revenue_conversion_score": 13, "margin_bridge_score": 13, "relative_strength_score": 4, "validation_risk": 10, "execution_risk_score": 10, "source_confidence_score": 2}, "weighted_score_before": 80, "stage_label_before": "Stage2/Yellow candidate after source repair", "raw_component_scores_after": {"regulatory_approval_score": 16, "partner_license_or_procurement_score": 16, "commercialization_timing_score": 15, "revenue_conversion_score": 15, "margin_bridge_score": 15, "relative_strength_score": 13, "validation_risk": 12, "execution_risk_score": 11, "source_confidence_score": 2}, "weighted_score_after": 86, "stage_label_after": "Stage2/Yellow after source repair + lifecycle 4B", "changed_components": ["regulatory_approval_score", "partner_license_or_procurement_score", "commercialization_timing_score", "revenue_conversion_score", "margin_bridge_score", "execution_risk_score"], "component_delta_explanation": "Reward only verified product approval, partner/license/procurement economics, launch or commercialization timing, revenue conversion and margin bridge; cap vaccine/platform commercialization theme beta when bridge fails to refresh.", "MFE_90D_pct": 8.83, "MAE_90D_pct": -2.25, "score_return_alignment_label": "bio_approval_commercialization_positive_with_lifecycle_4b", "current_profile_verdict": "C23 should not overblock large-cap biosimilar commercialization rows when MAE is controlled and commercialization/export revenue bridge may be visible. Celltrion requires post-CA and share-count continuity validation because the profile flags a 2024-01-12 corporate-action candidate and the 2024 shard shows share-count changes."}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R7L81-C23-302440-SK-BIOSCIENCE-VACCINE-COMMERCIALIZATION-THEME-FADE", "trigger_id": "TRG_R7L81-C23-302440-SK-BIOSCIENCE-VACCINE-COMMERCIALIZATION-THEME-FADE", "symbol": "302440", "large_sector_id": "L7_BIO_HEALTHCARE_MEDICAL", "canonical_archetype_id": "C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION", "raw_component_scores_before": {"regulatory_approval_score": 5, "partner_license_or_procurement_score": 3, "commercialization_timing_score": 3, "revenue_conversion_score": 2, "margin_bridge_score": 1, "relative_strength_score": 4, "validation_risk": 10, "execution_risk_score": 23, "source_confidence_score": 2}, "weighted_score_before": 43, "stage_label_before": "Stage2-FalsePositive / local 4B-watch", "raw_component_scores_after": {"regulatory_approval_score": 3, "partner_license_or_procurement_score": 1, "commercialization_timing_score": 1, "revenue_conversion_score": 1, "margin_bridge_score": 1, "relative_strength_score": 3, "validation_risk": 12, "execution_risk_score": 25, "source_confidence_score": 2}, "weighted_score_after": 32, "stage_label_after": "Stage4B-local-watch / no durable Green", "changed_components": ["regulatory_approval_score", "partner_license_or_procurement_score", "commercialization_timing_score", "revenue_conversion_score", "margin_bridge_score", "execution_risk_score"], "component_delta_explanation": "Reward only verified product approval, partner/license/procurement economics, launch or commercialization timing, revenue conversion and margin bridge; cap vaccine/platform commercialization theme beta when bridge fails to refresh.", "MFE_90D_pct": 3.97, "MAE_90D_pct": -7.95, "score_return_alignment_label": "false_positive_vaccine_platform_commercialization_bridge_gap", "current_profile_verdict": "C23 should not treat vaccine platform or regulatory commercialization theme beta as durable Stage2 unless product approval, procurement/order visibility, manufacturing utilization, revenue conversion and margin bridge are visible. SK Bioscience had tiny MFE and then a high-MAE fade."}
```

### aggregate row

```jsonl
{"row_type": "aggregate", "round": "R7", "loop": 81, "large_sector_id": "L7_BIO_HEALTHCARE_MEDICAL", "canonical_archetype_id": "C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION", "fine_archetype_id": "BIOSIMILAR_APPROVAL_PARTNER_COMMERCIALIZATION_BRIDGE_VS_VACCINE_PLATFORM_THEME_FADE", "calibration_usable_case_count": 3, "calibration_usable_trigger_count": 3, "new_independent_case_count": 3, "reused_case_count": 0, "same_archetype_new_symbol_count": 3, "same_archetype_new_trigger_family_count": 3, "positive_case_count": 2, "counterexample_count": 1, "four_b_case_count": 2, "four_c_case_count": 0, "source_proxy_only_count": 3, "evidence_url_pending_count": 3, "share_count_change_inside_window_count": 2, "post_corporate_action_validation_count": 1, "current_profile_error_count": 1, "diversity_score_summary": "+3 C23 symbols outside top-covered 000100/028300/145020/196170 set, +3 Samchundang/Celltrion/SK Bioscience trigger families, +2 approval-commercialization positives, +1 vaccine commercialization local-4B counterexample, no hard duplicate", "residual_contribution_label": "coverage_gap_fill_with_source_repair_postCA_and_sharecount_validation_needed"}
```

### shadow weight row

```jsonl
{"row_type": "shadow_weight", "round": "R7", "loop": 81, "large_sector_id": "L7_BIO_HEALTHCARE_MEDICAL", "canonical_archetype_id": "C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION", "axis": "biosimilar_approval_partner_commercialization_bridge_vs_vaccine_platform_theme_fade", "decision": "hold_for_source_repair_and_more_evidence", "proposed_runtime_effect": "C23 should split verified approval/commercialization and partner-license revenue-margin rerating from generic vaccine/platform commercialization theme beta. Stage2 requires product approval, partner/license or procurement economics, supply/manufacturing readiness, commercialization timing, revenue conversion and margin bridge. If MFE fades and MAE/post-peak drawdown opens without bridge refresh, route to local 4B-watch. Post-CA/share-count flags require validation before runtime promotion.", "do_not_propose_new_weight_delta": true, "needs_more_evidence": true, "source_repair_required": ["000250", "068270", "302440"], "post_corporate_action_validation_required": ["068270"], "share_count_validation_required": ["068270", "302440"]}
```

### residual contribution row

```jsonl
{"row_type": "residual_contribution", "round": "R7", "loop": 81, "large_sector_id": "L7_BIO_HEALTHCARE_MEDICAL", "canonical_archetype_id": "C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION", "existing_axis_strengthened": ["stage2_required_bridge", "regulatory_approval_commercialization_bridge_required", "partner_license_revenue_margin_bridge_guard", "price_only_blowoff_blocks_positive_stage", "local_4b_watch_guard", "post_corporate_action_validation_guard", "share_count_validation_guard", "full_4b_requires_non_price_evidence"], "new_axis_proposed": null, "sector_specific_rule_candidate": true, "canonical_archetype_rule_candidate": true, "narrative_summary": "C23 needs regulatory approval or commercialization events to map into partner/license economics, procurement/order visibility, supply/manufacturing, revenue conversion and margin proof. Samchundang Pharm and Celltrion show approval-commercialization positives after source repair and validation; SK Bioscience shows vaccine platform commercialization theme fading into local 4B."}
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
000250:
  name = 삼천당제약
  corporate_action_candidate_dates = 2002-04-22
  selected window = 2024-02-01~D+180
  contamination = false

068270:
  name = 셀트리온 from 2008-08-29, 오알켐 before that
  corporate_action_candidate_dates = 2006-10-13, 2008-06-10, 2008-09-24, 2012-06-29, 2013-03-22, 2024-01-12
  selected entry starts 2024-02-01 after the 2024-01-12 candidate
  contamination = false after post-CA entry, but coding-agent validation required
  share_count_change_inside_window = true

302440:
  name = SK바이오사이언스
  corporate_action_candidate_dates = none
  selected window = 2024-02-01~D+180
  contamination = false by profile
  share_count_change_inside_window = true → coding-agent validation required
```

Data-quality caveat:

```text
All selected C23 rows are source_proxy_only / evidence_url_pending.
068270 requires post-corporate-action and share-count validation.
302440 requires share-count validation before runtime promotion.
This MD is useful for stock-web path calibration and C23 regulatory/commercialization rule-shape discovery,
but coding-agent promotion requires non-proxy product approval, partner/license economics, procurement/order visibility, supply/manufacturing, revenue conversion and margin evidence.
```

---

## Deferred Coding Agent Handoff Prompt

Do not execute this now.

```text
You are the coding agent for Songdaiki/stock_agent.

Read this standalone v12 residual research MD and ingest machine-readable rows only after validation.

Do not patch production scoring blindly.
This R7/C23 artifact is marked do_not_propose_new_weight_delta=true because all rows need source repair and 068270/302440 need validation.

Candidate axis:
biosimilar_approval_partner_commercialization_bridge_vs_vaccine_platform_theme_fade

Required checks before implementation:
1. Validate all trigger rows against stock-web tradable_raw OHLC shards.
2. Confirm no hard duplicate key:
   canonical_archetype_id + symbol + trigger_type + entry_date.
3. Verify non-proxy source URLs for 000250, 068270 and 302440.
4. Validate 068270 post-CA continuity after 2024-01-12 and share-count changes inside the selected window.
5. Validate 302440 share-count changes inside the selected window.
6. Keep generic C23 bio-approval/commercialization weight unchanged until source repair is complete.
7. Consider Stage2 only when:
   - product approval or regulatory event is explicit,
   - partner/license/procurement economics are visible,
   - supply/manufacturing readiness is visible,
   - commercialization timing and revenue conversion exist,
   - margin bridge is credible,
   - MAE remains controlled or the signal is lifecycle-managed.
8. Consider local 4B-watch when:
   - the trigger is bio approval/commercialization theme beta only,
   - approval/procurement/partner/revenue/margin evidence is weak or stale,
   - MAE_90D <= -20% or MAE_180D <= -25%,
   - post-peak drawdown <= -35%.
9. Do not convert local 4B-watch into full 4B/4C without non-price approval failure, procurement failure, partner loss, financing or margin break.
10. Emit before/after diagnostics and reject if verified approval-commercialization positives or bounded large-cap rows are overblocked.
```

---

## Final round state

```text
completed_round = R7
completed_loop = 81
next_round = R8
next_loop = 81
round_schedule_status = valid
round_sector_consistency = pass
```

