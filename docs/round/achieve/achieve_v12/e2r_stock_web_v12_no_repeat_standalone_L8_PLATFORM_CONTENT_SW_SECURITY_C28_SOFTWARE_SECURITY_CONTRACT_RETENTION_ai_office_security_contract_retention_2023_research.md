# E2R V12 No-Repeat Standalone Residual Research
## R8 / L8 / C28 — Software/security contract-retention guard

metadata:
```text
selected_round: R8
scheduler_override_used: true
scheduled_round_inherited: false
large_sector_id: L8_PLATFORM_CONTENT_SW_SECURITY
canonical_archetype_id: C28_SOFTWARE_SECURITY_CONTRACT_RETENTION
fine_archetype_id: AI_OFFICE_SECURITY_SCM_CONTRACT_RETENTION_GUARD
loop_objective: coverage_gap_fill|counterexample_mining|green_strictness_stress_test|4B_non_price_requirement_stress_test
price_source: Songdaiki/stock-web
stock_web_manifest_max_date: 2026-02-20
output_file: e2r_stock_web_v12_no_repeat_standalone_L8_PLATFORM_CONTENT_SW_SECURITY_C28_SOFTWARE_SECURITY_CONTRACT_RETENTION_ai_office_security_contract_retention_2023_research.md
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

This run avoids those top-covered C28 symbols and adds 058970, 041020, and 150900.  
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
058970 엠로: 2023 forward window clean; corporate-action candidates are 2022-01-17 and 2022-02-09.
041020 폴라리스오피스: 2023 forward window clean; corporate-action candidates are old, outside the test window.
150900 파수: corporate_action_candidate_count=0.
```

## 3. Research thesis

C28 should not be a generic software-theme bucket. It should test whether software/security attention becomes durable contracted revenue:

```text
software/security/AI-office attention
→ enterprise contract, partner route, ARR/RPO, or renewal evidence
→ retention and operating leverage
→ margin/revision bridge
→ rerating
```

The positive row shows that software contract visibility can create a real rerating window. The counterexamples show the guard: AI-office or security narrative heat without ARR/retention proof is a thin bridge; price can run across it, but the bridge may not hold.

## 4. Case table

| case_id | symbol | role | entry | entry_price | peak | low_180d | MFE_30D | MFE_90D | MFE_180D | MAE_180D | post-peak DD |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| C28_058970_EMRO_20230315_SCM_SAAS_CONTRACT_RERATING | 058970 | positive_structural_success_with_4b_guard | 2023-03-15 | 30200 | 97800 on 2023-07-20 | 30200 on 2023-03-15 | 102.98% | 223.84% | 223.84% | 0.0% | -45.81% |
| C28_041020_POLARISOFFICE_20230717_AI_OFFICE_PRICE_ONLY_FALSE_GREEN | 041020 | ai_software_price_premium_counterexample | 2023-07-17 | 4175 | 7450 on 2023-08-31 | 3860 on 2023-10-04 | 62.87% | 78.44% | 78.44% | -7.54% | -48.19% |
| C28_150900_FASOO_20230127_SECURITY_CONTRACT_RETENTION_FADE | 150900 | security_contract_retention_false_green_counterexample | 2023-01-27 | 10180 | 10550 on 2023-01-30 | 6480 on 2023-08-23 | 3.63% | 3.63% | 3.63% | -36.35% | -38.58% |

## 5. Stage evidence split

### Stage2 / Stage2-Actionable
- Software/security attention and relative strength are valid routing signals.
- 041020 shows that AI-office heat can produce a strong tradable path, but that is not the same as retention quality.

### Stage3 / Green
- C28 Green should require ARR/RPO, renewal retention, enterprise contract conversion, and margin/revision evidence.
- 058970 is the positive anchor because the price path is consistent with a real software contract/partner rerating, not just generic software beta.

### 4B
- 058970 and 041020 both require local 4B discipline after the market capitalizes the story.
- Full 4B should require non-price evidence that the contract/revision bridge has matured or saturated.

### 4C
- 150900 is a retention-gap counterexample: security software labels alone do not protect against drift if renewal, ARR/RPO, and operating leverage do not improve.
- The C28 break mode is softer than accounting failure: revenue quality, renewal visibility, or revision bridge simply fails to arrive.

## 6. Raw component score breakdown

```json
{
  "C28_041020_POLARISOFFICE_20230717_AI_OFFICE_PRICE_ONLY_FALSE_GREEN": {
    "bottleneck_pricing_power": 6,
    "capital_allocation": 1,
    "eps_fcf_explosion": 5,
    "information_confidence": 3,
    "market_mispricing": 6,
    "total": 29,
    "valuation_rerating_runway": 3,
    "visibility_quality": 5
  },
  "C28_058970_EMRO_20230315_SCM_SAAS_CONTRACT_RERATING": {
    "bottleneck_pricing_power": 11,
    "capital_allocation": 2,
    "eps_fcf_explosion": 13,
    "information_confidence": 4,
    "market_mispricing": 12,
    "total": 66,
    "valuation_rerating_runway": 10,
    "visibility_quality": 14
  },
  "C28_150900_FASOO_20230127_SECURITY_CONTRACT_RETENTION_FADE": {
    "bottleneck_pricing_power": 5,
    "capital_allocation": 2,
    "eps_fcf_explosion": 5,
    "information_confidence": 3,
    "market_mispricing": 6,
    "total": 31,
    "valuation_rerating_runway": 4,
    "visibility_quality": 6
  }
}
```

## 7. Current calibrated profile stress test

Suggested C28 guard:
```text
if software_security_attention and no arr_rpo_retention_bridge:
    cap_stage = Stage2-Actionable or Stage3-Yellow
    block_stage3_green = true

if ai_office_or_software_theme_price_run and no enterprise_contract_conversion:
    route_to_local_4B_watch = true

if post_peak_drawdown and retention_revision_bridge_fails:
    route_to_counterexample_or_4C_watch = true
```

Residual errors:
```text
current_profile_error_count = 2
- 041020 / 2023-07-17: AI-office price premium can be over-promoted if ARR/retention and enterprise contract gates are not required.
- 150900 / 2023-01-27: security-contract narrative can fade when renewal/ARR and margin evidence are missing.
```

## 8. Machine-readable rows

```jsonl
{"MAE_180D_pct": 0.0, "MAE_30D_pct": 0.0, "MAE_90D_pct": 0.0, "MFE_180D_pct": 223.84, "MFE_30D_pct": 102.98, "MFE_90D_pct": 223.84, "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "calibration_usable": true, "canonical_archetype_id": "C28_SOFTWARE_SECURITY_CONTRACT_RETENTION", "case_id": "C28_058970_EMRO_20230315_SCM_SAAS_CONTRACT_RERATING", "case_role": "positive_structural_success_with_4b_guard", "company_name": "엠로", "corporate_action_window_status": "clean_180d_by_profile_or_outside_candidate_dates", "current_profile_error": false, "current_profile_verdict": "Green can be justified only when software contract/partner evidence closes into recurring revenue, retention, and revision bridge; after the rerating peak, local 4B discipline is still needed.", "dedupe_for_aggregate": true, "do_not_count_as_new_case": false, "drawdown_after_peak_pct": -45.81, "entry_date": "2023-03-15", "entry_price": 30200, "evidence_family": "supply_chain_management_software_contract_partner_retention_rerating", "evidence_url_pending": false, "fine_archetype_id": "AI_OFFICE_SECURITY_SCM_CONTRACT_RETENTION_GUARD", "forward_window_trading_days": 180, "independent_evidence_weight": 1.0, "large_sector_id": "L8_PLATFORM_CONTENT_SW_SECURITY", "low_date_180d": "2023-03-15", "low_price_180d": 30200, "peak_date": "2023-07-20", "peak_price": 97800, "positive_or_counterexample": "positive", "price_adjustment_status": "raw_unadjusted_marcap", "price_basis": "tradable_raw", "price_data_source": "Songdaiki/stock-web", "profile_path": "atlas/symbol_profiles/058/058970.json", "raw_component_score_breakdown": {"bottleneck_pricing_power": 11, "capital_allocation": 2, "eps_fcf_explosion": 13, "information_confidence": 4, "market_mispricing": 12, "total": 66, "valuation_rerating_runway": 10, "visibility_quality": 14}, "reuse_reason": null, "same_entry_group_id": "C28_058970_EMRO_20230315_SCM_SAAS_CONTRACT_RERATING", "schema_version": "v12_no_repeat_standalone_trigger_row_v1", "selected_round": "R8", "source_proxy_only": false, "stage2_evidence_fields": ["software_or_security_attention", "contract_or_partner_visibility_claim", "relative_strength"], "stage3_evidence_fields": ["arr_or_rpo_confirmation_required", "retention_or_renewal_visibility_required", "margin_or_revision_bridge_required"], "stage4b_evidence_fields": ["software_theme_or_ai_premium_blowoff", "valuation_or_positioning_overheat", "post_peak_drawdown"], "stage4c_evidence_fields": ["arr_retention_gap", "enterprise_contract_conversion_failure", "revision_or_operating_leverage_break"], "symbol": "058970", "tradable_shard_path": "atlas/ohlcv_tradable_by_symbol_year/058/058970/2023.csv", "trigger_date": "2023-03-15", "trigger_type": "Stage3-Green", "upstream_source": "FinanceData/marcap"}
{"MAE_180D_pct": -7.54, "MAE_30D_pct": -6.95, "MAE_90D_pct": -7.54, "MFE_180D_pct": 78.44, "MFE_30D_pct": 62.87, "MFE_90D_pct": 78.44, "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "calibration_usable": true, "canonical_archetype_id": "C28_SOFTWARE_SECURITY_CONTRACT_RETENTION", "case_id": "C28_041020_POLARISOFFICE_20230717_AI_OFFICE_PRICE_ONLY_FALSE_GREEN", "case_role": "ai_software_price_premium_counterexample", "company_name": "폴라리스오피스", "corporate_action_window_status": "clean_180d_by_profile_or_outside_candidate_dates", "current_profile_error": true, "current_profile_verdict": "AI office price premium should remain Stage2/EventPremium or local 4B unless ARR, paying-seat retention, enterprise contract, and revision evidence close.", "dedupe_for_aggregate": true, "do_not_count_as_new_case": false, "drawdown_after_peak_pct": -48.19, "entry_date": "2023-07-17", "entry_price": 4175, "evidence_family": "ai_office_software_theme_price_premium_without_arr_retention_bridge", "evidence_url_pending": false, "fine_archetype_id": "AI_OFFICE_SECURITY_SCM_CONTRACT_RETENTION_GUARD", "forward_window_trading_days": 180, "independent_evidence_weight": 1.0, "large_sector_id": "L8_PLATFORM_CONTENT_SW_SECURITY", "low_date_180d": "2023-10-04", "low_price_180d": 3860, "peak_date": "2023-08-31", "peak_price": 7450, "positive_or_counterexample": "counterexample", "price_adjustment_status": "raw_unadjusted_marcap", "price_basis": "tradable_raw", "price_data_source": "Songdaiki/stock-web", "profile_path": "atlas/symbol_profiles/041/041020.json", "raw_component_score_breakdown": {"bottleneck_pricing_power": 6, "capital_allocation": 1, "eps_fcf_explosion": 5, "information_confidence": 3, "market_mispricing": 6, "total": 29, "valuation_rerating_runway": 3, "visibility_quality": 5}, "reuse_reason": null, "same_entry_group_id": "C28_041020_POLARISOFFICE_20230717_AI_OFFICE_PRICE_ONLY_FALSE_GREEN", "schema_version": "v12_no_repeat_standalone_trigger_row_v1", "selected_round": "R8", "source_proxy_only": false, "stage2_evidence_fields": ["software_or_security_attention", "contract_or_partner_visibility_claim", "relative_strength"], "stage3_evidence_fields": ["arr_or_rpo_confirmation_required", "retention_or_renewal_visibility_required", "margin_or_revision_bridge_required"], "stage4b_evidence_fields": ["software_theme_or_ai_premium_blowoff", "valuation_or_positioning_overheat", "post_peak_drawdown"], "stage4c_evidence_fields": ["arr_retention_gap", "enterprise_contract_conversion_failure", "revision_or_operating_leverage_break"], "symbol": "041020", "tradable_shard_path": "atlas/ohlcv_tradable_by_symbol_year/041/041020/2023.csv", "trigger_date": "2023-07-17", "trigger_type": "Stage2-EventPremium", "upstream_source": "FinanceData/marcap"}
{"MAE_180D_pct": -36.35, "MAE_30D_pct": -12.57, "MAE_90D_pct": -26.82, "MFE_180D_pct": 3.63, "MFE_30D_pct": 3.63, "MFE_90D_pct": 3.63, "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "calibration_usable": true, "canonical_archetype_id": "C28_SOFTWARE_SECURITY_CONTRACT_RETENTION", "case_id": "C28_150900_FASOO_20230127_SECURITY_CONTRACT_RETENTION_FADE", "case_role": "security_contract_retention_false_green_counterexample", "company_name": "파수", "corporate_action_window_status": "clean_180d_by_profile_or_outside_candidate_dates", "current_profile_error": true, "current_profile_verdict": "Security contract/retention stories should not become Green unless renewal retention, ARR/RPO, operating leverage, and revision bridge are visible.", "dedupe_for_aggregate": true, "do_not_count_as_new_case": false, "drawdown_after_peak_pct": -38.58, "entry_date": "2023-01-27", "entry_price": 10180, "evidence_family": "security_contract_theme_without_retention_arr_margin_bridge", "evidence_url_pending": false, "fine_archetype_id": "AI_OFFICE_SECURITY_SCM_CONTRACT_RETENTION_GUARD", "forward_window_trading_days": 180, "independent_evidence_weight": 1.0, "large_sector_id": "L8_PLATFORM_CONTENT_SW_SECURITY", "low_date_180d": "2023-08-23", "low_price_180d": 6480, "peak_date": "2023-01-30", "peak_price": 10550, "positive_or_counterexample": "counterexample", "price_adjustment_status": "raw_unadjusted_marcap", "price_basis": "tradable_raw", "price_data_source": "Songdaiki/stock-web", "profile_path": "atlas/symbol_profiles/150/150900.json", "raw_component_score_breakdown": {"bottleneck_pricing_power": 5, "capital_allocation": 2, "eps_fcf_explosion": 5, "information_confidence": 3, "market_mispricing": 6, "total": 31, "valuation_rerating_runway": 4, "visibility_quality": 6}, "reuse_reason": null, "same_entry_group_id": "C28_150900_FASOO_20230127_SECURITY_CONTRACT_RETENTION_FADE", "schema_version": "v12_no_repeat_standalone_trigger_row_v1", "selected_round": "R8", "source_proxy_only": false, "stage2_evidence_fields": ["software_or_security_attention", "contract_or_partner_visibility_claim", "relative_strength"], "stage3_evidence_fields": ["arr_or_rpo_confirmation_required", "retention_or_renewal_visibility_required", "margin_or_revision_bridge_required"], "stage4b_evidence_fields": ["software_theme_or_ai_premium_blowoff", "valuation_or_positioning_overheat", "post_peak_drawdown"], "stage4c_evidence_fields": ["arr_retention_gap", "enterprise_contract_conversion_failure", "revision_or_operating_leverage_break"], "symbol": "150900", "tradable_shard_path": "atlas/ohlcv_tradable_by_symbol_year/150/150900/2023.csv", "trigger_date": "2023-01-27", "trigger_type": "Stage3-Yellow", "upstream_source": "FinanceData/marcap"}
```

## 9. Aggregate row

```json
{
  "calibration_usable_case_count": 3,
  "canonical_archetype_id": "C28_SOFTWARE_SECURITY_CONTRACT_RETENTION",
  "counterexample_count": 2,
  "current_profile_error_count": 2,
  "evidence_url_pending_count": 0,
  "fine_archetype_id": "AI_OFFICE_SECURITY_SCM_CONTRACT_RETENTION_GUARD",
  "hard_duplicate_avoided": true,
  "index_update_needed": true,
  "large_sector_id": "L8_PLATFORM_CONTENT_SW_SECURITY",
  "loop_contribution_label": "software_security_contract_retention_counterexample_added",
  "new_independent_case_count": 3,
  "positive_case_count": 1,
  "reused_case_count": 0,
  "schema_version": "v12_no_repeat_standalone_aggregate_v1",
  "selected_round": "R8",
  "shadow_rule_candidate": "C28 software/security rerating should permit Stage2/Green only when ARR/RPO, retention/renewal, enterprise-contract conversion, operating leverage, and revision bridge close; AI/software price premium without retention proof should route to Stage2 cap or local 4B.",
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
3. Add C28-specific ARR/RPO/retention/enterprise-contract logic only as a shadow candidate until more rows exist.

Candidate rule:
- C28_GREEN_REQUIRES_ARR_RPO_RETENTION_CONTRACT_REVISION
- C28_AI_OFFICE_PRICE_PREMIUM_STAGE2_CAP
- C28_SECURITY_CONTRACT_WITHOUT_RETENTION_COUNTEREXAMPLE

Do not lower global Stage3 Green thresholds.
Do not treat this single MD as production-ready.
```

## 11. Final contribution line

This loop adds 3 new independent cases, 2 counterexamples, and 2 current-profile residual errors for R8/L8_PLATFORM_CONTENT_SW_SECURITY/C28_SOFTWARE_SECURITY_CONTRACT_RETENTION.

