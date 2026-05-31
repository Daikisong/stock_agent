# E2R V12 No-Repeat Standalone Residual Research
## R8 / L8 / C28 — Software/security contract-retention guard

metadata:
```text
selected_round: R8
scheduler_override_used: true
scheduled_round_inherited: false
large_sector_id: L8_PLATFORM_CONTENT_SW_SECURITY
canonical_archetype_id: C28_SOFTWARE_SECURITY_CONTRACT_RETENTION
fine_archetype_id: SOFTWARE_SECURITY_CONTRACT_RETENTION_ARR_MAINTENANCE_GUARD
loop_objective: coverage_gap_fill|counterexample_mining|positive_counterexample_balance|4B_non_price_requirement_stress_test|green_strictness_stress_test
price_source: Songdaiki/stock-web
stock_web_manifest_max_date: 2026-02-20
output_file: e2r_stock_web_v12_no_repeat_standalone_L8_PLATFORM_CONTENT_SW_SECURITY_C28_SOFTWARE_SECURITY_CONTRACT_RETENTION_software_security_retention_guard_2020_2024_research.md
production_scoring_changed: false
shadow_weight_only: true
```

## 1. Prompt / no-repeat basis

This MD follows `docs/core/e2r_v12_prompt_round_scheduler_corrected.txt` as a standalone historical residual research artifact.  
`V12_Research_No_Repeat_Index.md` is used only for duplicate avoidance and coverage-gap selection.

No-Repeat selection:
```text
C28_SOFTWARE_SECURITY_CONTRACT_RETENTION current coverage:
rows=64, symbols=12, date range=2019-05-27~2024-04-29, good/bad S2=18/4, 4B/4C=9/2
top covered symbols: 012510(15), 053800(13), 263860(11), 131370(5), 030520(3)
```

This run avoids those top-covered C28 symbols and adds 150900, 067920, and 042510.  
Each row uses a new `C28 + symbol + trigger_type + entry_date` hard key.

## 2. Stock-Web source check

Manifest:
```text
source_name: FinanceData/marcap
price_adjustment_status: raw_unadjusted_marcap
min_date: 1995-05-02
max_date: 2026-02-20
tradable_row_count: 14354401
calibration_shard_root: atlas/ohlcv_tradable_by_symbol_year
raw_shard_root: atlas/ohlcv_raw_by_symbol_year
```

Selected profiles:
```text
150900 파수: corporate_action_candidate_count=0.
067920 이글루: 2023 forward window clean; corporate-action candidate is old, outside the selected test window.
042510 라온시큐어: 2024 selected window is after the 2023-12-18 corporate-action candidate; 2025 candidate is outside the selected window.
```

## 3. Research thesis

C28 should not be a generic "security/software theme" bucket. It should test whether security attention becomes retained software revenue:

```text
security / authentication / remote-work software attention
→ enterprise contract conversion
→ renewal quality and retention
→ ARR, maintenance, managed-service or subscription conversion
→ margin and revision bridge
→ rerating
```

The contract is the server. The headline is only the login screen. C28 should pay for the retained server load, not just the authentication flash.

## 4. Case table

| case_id | symbol | role | entry | entry_price | peak | low_180d | MFE_30D | MFE_90D | MFE_180D | MAE_180D | post-peak DD |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| C28_150900_FASOO_20200423_REMOTE_WORK_DATA_SECURITY_STAGE2 | 150900 | positive_security_contract_retention_stage2_success_with_later_4b | 2020-04-23 | 3890 | 8790 on 2020-10-06 | 3725 on 2020-04-23 | 26.99% | 46.27% | 125.96% | -4.24% | -37.2% |
| C28_067920_IGLOO_20230210_AI_SECURITY_MONITORING_PRICE_PREMIUM_FALSE_GREEN | 067920 | ai_security_monitoring_false_green_counterexample | 2023-02-10 | 8890 | 9550 on 2023-02-10 | 5650 on 2023-08-17 | 7.42% | 7.42% | 7.42% | -36.45% | -40.84% |
| C28_042510_RAONSECURE_20240722_DIGITAL_ID_SECURITY_LOCAL_4B | 042510 | digital_id_security_price_premium_counterexample | 2024-07-22 | 2210 | 2595 on 2024-08-30 | 1650 on 2024-12-09 | 15.38% | 17.42% | 17.42% | -25.34% | -36.42% |

## 5. Stage evidence split

### Stage2 / Stage2-Actionable
- Remote-work security, data-security, managed-security and authentication attention can be valid Stage2 routes.
- 150900 is the positive anchor: the early remote-work/data-security route created a large MFE, but the later peak still required 4B discipline.

### Stage3 / Green
- C28 Green should require renewal quality, contract retention, ARR/maintenance conversion, managed-service durability, margin and revision confirmation.
- 067920 and 042510 show why security labels alone should not become Green. AI/security monitoring and digital-ID themes can move first, then fade if retained contract evidence does not follow.

### 4B
- 042510 is the local 4B guard: the digital-ID/authentication price premium created a tradable burst, then rolled over hard.
- 067920 also behaves like a security-theme price premium rather than a confirmed retained-software rerating.

### 4C
- No hard accounting break is asserted.
- The C28 break mode is retention failure: the security problem remains real, but enterprise contract conversion, ARR, maintenance revenue, margin and revision do not carry the valuation.

## 6. Raw component score breakdown

```json
{
  "C28_042510_RAONSECURE_20240722_DIGITAL_ID_SECURITY_LOCAL_4B": {
    "bottleneck_pricing_power": 6,
    "capital_allocation": 2,
    "eps_fcf_explosion": 4,
    "information_confidence": 3,
    "market_mispricing": 4,
    "total": 26,
    "valuation_rerating_runway": 2,
    "visibility_quality": 5
  },
  "C28_067920_IGLOO_20230210_AI_SECURITY_MONITORING_PRICE_PREMIUM_FALSE_GREEN": {
    "bottleneck_pricing_power": 6,
    "capital_allocation": 2,
    "eps_fcf_explosion": 5,
    "information_confidence": 3,
    "market_mispricing": 5,
    "total": 29,
    "valuation_rerating_runway": 3,
    "visibility_quality": 5
  },
  "C28_150900_FASOO_20200423_REMOTE_WORK_DATA_SECURITY_STAGE2": {
    "bottleneck_pricing_power": 9,
    "capital_allocation": 2,
    "eps_fcf_explosion": 10,
    "information_confidence": 4,
    "market_mispricing": 11,
    "total": 56,
    "valuation_rerating_runway": 9,
    "visibility_quality": 11
  }
}
```

## 7. Current calibrated profile stress test

Suggested C28 guard:
```text
if software_security_attention and contract_retention_or_arr_route_visible:
    allow_stage2_actionable = true

if security_theme_price_premium and no renewal_arr_maintenance_margin_revision_bridge:
    block_stage3_green = true
    route_to_local_4B_watch = true

if post_peak_drawdown and retained_contract_bridge_fails:
    route_to_counterexample_or_4C_watch = true
```

Residual errors:
```text
current_profile_error_count = 2
- 067920 / 2023-02-10: AI/security monitoring theme heat can be over-promoted if the model does not demand retained contract and ARR/maintenance evidence.
- 042510 / 2024-07-22: digital-ID/authentication premium can become price-only when enterprise contract conversion and revision proof do not arrive.
```

## 8. Machine-readable rows

```jsonl
{"MAE_180D_pct": -4.24, "MAE_30D_pct": -4.24, "MAE_90D_pct": -4.24, "MFE_180D_pct": 125.96, "MFE_30D_pct": 26.99, "MFE_90D_pct": 46.27, "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "calibration_usable": true, "canonical_archetype_id": "C28_SOFTWARE_SECURITY_CONTRACT_RETENTION", "case_id": "C28_150900_FASOO_20200423_REMOTE_WORK_DATA_SECURITY_STAGE2", "case_role": "positive_security_contract_retention_stage2_success_with_later_4b", "company_name": "파수", "corporate_action_window_status": "clean_forward_window; corporate-action candidates old or outside selected test window where present", "current_profile_error": false, "current_profile_verdict": "Stage2 was useful when remote-work and data-security contract attention produced a recurring-revenue route, but Green still requires renewal quality, ARR/maintenance conversion, margin and revision durability.", "dedupe_for_aggregate": true, "do_not_count_as_new_case": false, "drawdown_after_peak_pct": -37.2, "entry_date": "2020-04-23", "entry_price": 3890, "evidence_family": "remote_work_data_security_drm_contract_retention_stage2_route", "evidence_url_pending": false, "fine_archetype_id": "SOFTWARE_SECURITY_CONTRACT_RETENTION_ARR_MAINTENANCE_GUARD", "forward_window_trading_days": 180, "independent_evidence_weight": 1.0, "large_sector_id": "L8_PLATFORM_CONTENT_SW_SECURITY", "low_date_180d": "2020-04-23", "low_price_180d": 3725, "peak_date": "2020-10-06", "peak_price": 8790, "positive_or_counterexample": "positive", "price_adjustment_status": "raw_unadjusted_marcap", "price_basis": "tradable_raw", "price_data_source": "Songdaiki/stock-web", "profile_path": "atlas/symbol_profiles/150/150900.json", "raw_component_score_breakdown": {"bottleneck_pricing_power": 9, "capital_allocation": 2, "eps_fcf_explosion": 10, "information_confidence": 4, "market_mispricing": 11, "total": 56, "valuation_rerating_runway": 9, "visibility_quality": 11}, "reuse_reason": null, "same_entry_group_id": "C28_150900_FASOO_20200423_REMOTE_WORK_DATA_SECURITY_STAGE2", "schema_version": "v12_no_repeat_standalone_trigger_row_v1", "selected_round": "R8", "source_proxy_only": false, "stage2_evidence_fields": ["software_security_or_authentication_attention", "contract_retention_or_managed_security_claim", "ARR_or_maintenance_revenue_route"], "stage3_evidence_fields": ["renewal_quality_and_contract_retention_required", "ARR_maintenance_or_subscription_conversion_required", "margin_or_revision_bridge_required"], "stage4b_evidence_fields": ["software_security_price_premium", "valuation_or_positioning_overheat", "post_peak_drawdown"], "stage4c_evidence_fields": ["contract_retention_gap", "ARR_or_maintenance_conversion_failure", "margin_or_revision_bridge_failure"], "symbol": "150900", "tradable_shard_path": "atlas/ohlcv_tradable_by_symbol_year/150/150900/2020.csv", "trigger_date": "2020-04-23", "trigger_type": "Stage2-Actionable", "upstream_source": "FinanceData/marcap"}
{"MAE_180D_pct": -36.45, "MAE_30D_pct": -17.77, "MAE_90D_pct": -23.85, "MFE_180D_pct": 7.42, "MFE_30D_pct": 7.42, "MFE_90D_pct": 7.42, "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "calibration_usable": true, "canonical_archetype_id": "C28_SOFTWARE_SECURITY_CONTRACT_RETENTION", "case_id": "C28_067920_IGLOO_20230210_AI_SECURITY_MONITORING_PRICE_PREMIUM_FALSE_GREEN", "case_role": "ai_security_monitoring_false_green_counterexample", "company_name": "이글루", "corporate_action_window_status": "clean_forward_window; corporate-action candidates old or outside selected test window where present", "current_profile_error": true, "current_profile_verdict": "AI/security monitoring price premium should stay Yellow or local 4B unless retained contracts, managed-security backlog, ARR/maintenance quality, margin and revision bridge are visible.", "dedupe_for_aggregate": true, "do_not_count_as_new_case": false, "drawdown_after_peak_pct": -40.84, "entry_date": "2023-02-10", "entry_price": 8890, "evidence_family": "ai_security_monitoring_theme_without_contract_retention_arr_revision_bridge", "evidence_url_pending": false, "fine_archetype_id": "SOFTWARE_SECURITY_CONTRACT_RETENTION_ARR_MAINTENANCE_GUARD", "forward_window_trading_days": 180, "independent_evidence_weight": 1.0, "large_sector_id": "L8_PLATFORM_CONTENT_SW_SECURITY", "low_date_180d": "2023-08-17", "low_price_180d": 5650, "peak_date": "2023-02-10", "peak_price": 9550, "positive_or_counterexample": "counterexample", "price_adjustment_status": "raw_unadjusted_marcap", "price_basis": "tradable_raw", "price_data_source": "Songdaiki/stock-web", "profile_path": "atlas/symbol_profiles/067/067920.json", "raw_component_score_breakdown": {"bottleneck_pricing_power": 6, "capital_allocation": 2, "eps_fcf_explosion": 5, "information_confidence": 3, "market_mispricing": 5, "total": 29, "valuation_rerating_runway": 3, "visibility_quality": 5}, "reuse_reason": null, "same_entry_group_id": "C28_067920_IGLOO_20230210_AI_SECURITY_MONITORING_PRICE_PREMIUM_FALSE_GREEN", "schema_version": "v12_no_repeat_standalone_trigger_row_v1", "selected_round": "R8", "source_proxy_only": false, "stage2_evidence_fields": ["software_security_or_authentication_attention", "contract_retention_or_managed_security_claim", "ARR_or_maintenance_revenue_route"], "stage3_evidence_fields": ["renewal_quality_and_contract_retention_required", "ARR_maintenance_or_subscription_conversion_required", "margin_or_revision_bridge_required"], "stage4b_evidence_fields": ["software_security_price_premium", "valuation_or_positioning_overheat", "post_peak_drawdown"], "stage4c_evidence_fields": ["contract_retention_gap", "ARR_or_maintenance_conversion_failure", "margin_or_revision_bridge_failure"], "symbol": "067920", "tradable_shard_path": "atlas/ohlcv_tradable_by_symbol_year/067/067920/2023.csv", "trigger_date": "2023-02-10", "trigger_type": "Stage3-Yellow", "upstream_source": "FinanceData/marcap"}
{"MAE_180D_pct": -25.34, "MAE_30D_pct": -23.57, "MAE_90D_pct": -23.57, "MFE_180D_pct": 17.42, "MFE_30D_pct": 15.38, "MFE_90D_pct": 17.42, "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "calibration_usable": true, "canonical_archetype_id": "C28_SOFTWARE_SECURITY_CONTRACT_RETENTION", "case_id": "C28_042510_RAONSECURE_20240722_DIGITAL_ID_SECURITY_LOCAL_4B", "case_role": "digital_id_security_price_premium_counterexample", "company_name": "라온시큐어", "corporate_action_window_status": "clean_forward_window; corporate-action candidates old or outside selected test window where present", "current_profile_error": true, "current_profile_verdict": "Digital-ID/authentication security premium should route to local 4B or Yellow unless enterprise contract conversion, retained maintenance revenue, margin and revision evidence close.", "dedupe_for_aggregate": true, "do_not_count_as_new_case": false, "drawdown_after_peak_pct": -36.42, "entry_date": "2024-07-22", "entry_price": 2210, "evidence_family": "digital_id_authentication_security_price_premium_without_enterprise_contract_retention_bridge", "evidence_url_pending": false, "fine_archetype_id": "SOFTWARE_SECURITY_CONTRACT_RETENTION_ARR_MAINTENANCE_GUARD", "forward_window_trading_days": 180, "independent_evidence_weight": 1.0, "large_sector_id": "L8_PLATFORM_CONTENT_SW_SECURITY", "low_date_180d": "2024-12-09", "low_price_180d": 1650, "peak_date": "2024-08-30", "peak_price": 2595, "positive_or_counterexample": "counterexample", "price_adjustment_status": "raw_unadjusted_marcap", "price_basis": "tradable_raw", "price_data_source": "Songdaiki/stock-web", "profile_path": "atlas/symbol_profiles/042/042510.json", "raw_component_score_breakdown": {"bottleneck_pricing_power": 6, "capital_allocation": 2, "eps_fcf_explosion": 4, "information_confidence": 3, "market_mispricing": 4, "total": 26, "valuation_rerating_runway": 2, "visibility_quality": 5}, "reuse_reason": null, "same_entry_group_id": "C28_042510_RAONSECURE_20240722_DIGITAL_ID_SECURITY_LOCAL_4B", "schema_version": "v12_no_repeat_standalone_trigger_row_v1", "selected_round": "R8", "source_proxy_only": false, "stage2_evidence_fields": ["software_security_or_authentication_attention", "contract_retention_or_managed_security_claim", "ARR_or_maintenance_revenue_route"], "stage3_evidence_fields": ["renewal_quality_and_contract_retention_required", "ARR_maintenance_or_subscription_conversion_required", "margin_or_revision_bridge_required"], "stage4b_evidence_fields": ["software_security_price_premium", "valuation_or_positioning_overheat", "post_peak_drawdown"], "stage4c_evidence_fields": ["contract_retention_gap", "ARR_or_maintenance_conversion_failure", "margin_or_revision_bridge_failure"], "symbol": "042510", "tradable_shard_path": "atlas/ohlcv_tradable_by_symbol_year/042/042510/2024.csv", "trigger_date": "2024-07-22", "trigger_type": "4B-local-price-only", "upstream_source": "FinanceData/marcap"}
```

## 9. Aggregate row

```json
{
  "calibration_usable_case_count": 3,
  "canonical_archetype_id": "C28_SOFTWARE_SECURITY_CONTRACT_RETENTION",
  "counterexample_count": 2,
  "current_profile_error_count": 2,
  "evidence_url_pending_count": 0,
  "fine_archetype_id": "SOFTWARE_SECURITY_CONTRACT_RETENTION_ARR_MAINTENANCE_GUARD",
  "hard_duplicate_avoided": true,
  "index_update_needed": true,
  "large_sector_id": "L8_PLATFORM_CONTENT_SW_SECURITY",
  "loop_contribution_label": "software_security_contract_retention_new_symbols_and_counterexamples",
  "new_independent_case_count": 3,
  "positive_case_count": 1,
  "reused_case_count": 0,
  "schema_version": "v12_no_repeat_standalone_aggregate_v1",
  "selected_round": "R8",
  "shadow_rule_candidate": "C28 software/security rows should allow Stage2 on early contract-retention, remote-work, data-security or managed-security attention, but Stage3 Green requires renewal quality, ARR/maintenance conversion, enterprise-contract retention, margin and revision bridge; security price premium without retention proof should route to local 4B or counterexample.",
  "source_proxy_only_count": 0
}
```

## 10. Deferred Coding Agent Handoff Prompt

Do not execute this handoff inside the research session.

```text
Read this standalone v12 residual research MD.
Before batch apply:
1. Verify all OHLC rows again from Songdaiki/stock-web tradable shards.
2. Check no hard duplicate exists for C28 + symbol + trigger_type + entry_date.
3. Add C28-specific contract-retention / ARR-maintenance / renewal-quality guard only as a shadow candidate until more rows exist.

Candidate rule:
- C28_STAGE2_ALLOWED_ON_SECURITY_CONTRACT_RETENTION_ATTENTION
- C28_GREEN_REQUIRES_RENEWAL_ARR_MAINTENANCE_MARGIN_REVISION
- C28_SECURITY_THEME_PRICE_PREMIUM_LOCAL_4B
- C28_DIGITAL_ID_OR_AI_SECURITY_WITHOUT_CONTRACT_RETENTION_COUNTEREXAMPLE

Do not lower global Stage3 Green thresholds.
Do not treat this single MD as production-ready.
```

## 11. Final contribution line

This loop adds 3 new independent cases, 2 counterexamples, and 2 current-profile residual errors for R8/L8_PLATFORM_CONTENT_SW_SECURITY/C28_SOFTWARE_SECURITY_CONTRACT_RETENTION.

