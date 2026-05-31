# E2R V12 No-Repeat Standalone Residual Research
## R8 / L8 / C28 — Software security contract-retention guard

metadata:
```text
selected_round: R8
scheduler_override_used: true
scheduled_round_inherited: false
large_sector_id: L8_PLATFORM_CONTENT_SW_SECURITY
canonical_archetype_id: C28_SOFTWARE_SECURITY_CONTRACT_RETENTION
fine_archetype_id: CYBERSECURITY_CONTRACT_RETENTION_RENEWAL_MARGIN_GUARD
loop_objective: coverage_gap_fill|new_symbol_expansion|counterexample_mining|positive_counterexample_balance|4B_non_price_requirement_stress_test|green_strictness_stress_test
price_source: Songdaiki/stock-web
stock_web_manifest_max_date: 2026-02-20
output_file: e2r_stock_web_v12_no_repeat_standalone_L8_PLATFORM_CONTENT_SW_SECURITY_C28_SOFTWARE_SECURITY_CONTRACT_RETENTION_cybersecurity_contract_retention_2023_research.md
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

This run avoids those top-covered C28 symbols and adds 067920, 203650, and 042510.  
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
067920 이글루: 2023 forward window clean; corporate-action candidate is 2014-04-24 and outside selected test window.
203650 드림시큐리티: 2023 forward window clean; corporate-action candidates are 2017-01-20 and 2019-11-26, outside selected test window.
042510 라온시큐어: selected 2023 forward window is before the 2023-12-18 corporate-action candidate; older corporate-action candidates are outside selected test window.
```

## 3. Research thesis

C28 should not treat every cybersecurity or digital-ID headline as durable software revenue. It should test whether security attention becomes retained contract economics:

```text
software/security attention
→ contract renewal and customer retention
→ maintenance or ARR-like revenue quality
→ project mix and delivery margin
→ margin and revision bridge
→ rerating
```

A security headline is an alarm bell. A retained contract is the monitoring subscription that keeps ringing every month. Stage2 can follow early evidence of retained security budgets, but Green should require renewal, backlog, maintenance mix and margin.

## 4. Case table

| case_id | symbol | role | entry | entry_price | peak | low_180d | MFE_30D | MFE_90D | MFE_180D | MAE_180D | post-peak DD |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| C28_067920_IGLOO_20230118_SECURITY_OPS_CONTRACT_RETENTION_STAGE2 | 067920 | positive_security_ops_contract_retention_stage2_success_with_later_4b | 2023-01-18 | 6260 | 9550 on 2023-02-10 | 5630 on 2023-10-31 | 52.56% | 52.56% | 52.56% | -10.06% | -41.05% |
| C28_203650_DREAMSECURITY_20230920_DIGITAL_ID_SECURITY_PRICE_PREMIUM_4B | 203650 | digital_id_security_theme_price_premium_counterexample | 2023-09-20 | 3855 | 4250 on 2023-09-20 | 3025 on 2023-10-30 | 10.25% | 10.25% | 10.25% | -21.53% | -28.82% |
| C28_042510_RAONSECURE_20230203_AUTH_SECURITY_FALSE_GREEN | 042510 | authentication_security_contract_retention_false_green_counterexample | 2023-02-03 | 2820 | 2935 on 2023-02-06 | 2105 on 2023-10-31 | 4.08% | 4.08% | 4.08% | -25.35% | -28.28% |

## 5. Stage evidence split

### Stage2 / Stage2-Actionable
- Security operations, public-sector cyber budgets and retained managed-security contracts can be valid Stage2 routes.
- 067920 is the positive anchor: early 2023 security-ops attention produced a large MFE with limited early MAE. The later drawdown shows why contract-retention evidence must be refreshed after a spike.

### Stage3 / Green
- C28 Green should require renewal rate, contract backlog, maintenance revenue quality, project mix, margin and revision confirmation.
- 042510 is the false-Green guard. Authentication/security attention and a short price confirmation were not enough when contract-retention and maintenance-margin evidence did not keep improving.

### 4B
- 203650 is the local 4B counterexample. Digital-ID/security premium had already moved by the trigger day; without renewed contract economics and margin/revision bridge, the following drawdown made the spike price-only.
- 067920 also required later 4B discipline after a valid Stage2 signal matured into a theme premium.

### 4C
- No hard contract cancellation or accounting break is asserted.
- The C28 break mode is retention disappointment: the security need remains real, but renewal, maintenance mix, project margin and revisions do not support the price already paid.

## 6. Raw component score breakdown

```json
{
  "C28_042510_RAONSECURE_20230203_AUTH_SECURITY_FALSE_GREEN": {
    "bottleneck_pricing_power": 5,
    "capital_allocation": 2,
    "eps_fcf_explosion": 4,
    "information_confidence": 3,
    "market_mispricing": 5,
    "total": 26,
    "valuation_rerating_runway": 2,
    "visibility_quality": 5
  },
  "C28_067920_IGLOO_20230118_SECURITY_OPS_CONTRACT_RETENTION_STAGE2": {
    "bottleneck_pricing_power": 7,
    "capital_allocation": 2,
    "eps_fcf_explosion": 8,
    "information_confidence": 4,
    "market_mispricing": 10,
    "total": 49,
    "valuation_rerating_runway": 8,
    "visibility_quality": 10
  },
  "C28_203650_DREAMSECURITY_20230920_DIGITAL_ID_SECURITY_PRICE_PREMIUM_4B": {
    "bottleneck_pricing_power": 6,
    "capital_allocation": 2,
    "eps_fcf_explosion": 5,
    "information_confidence": 3,
    "market_mispricing": 4,
    "total": 27,
    "valuation_rerating_runway": 2,
    "visibility_quality": 5
  }
}
```

## 7. Current calibrated profile stress test

Suggested C28 guard:
```text
if security_contract_attention and renewal_maintenance_margin_bridge_visible:
    allow_stage2_actionable = true

if security_theme_price_premium and no renewal_retention_maintenance_margin_revision_bridge:
    block_stage3_green = true
    route_to_local_4B_watch = true

if post_peak_drawdown and retention_or_margin_bridge_fails:
    route_to_counterexample_or_4C_watch = true
```

Residual errors:
```text
current_profile_error_count = 2
- 203650 / 2023-09-20: digital-ID/security price premium can be over-promoted if the model treats theme heat as retained contract economics.
- 042510 / 2023-02-03: authentication/security claims can look like Green, but the later path argues for Yellow/counterexample unless renewal, maintenance mix and margin revisions close.
```

## 8. Machine-readable rows

```jsonl
{"MAE_180D_pct": -10.06, "MAE_30D_pct": -4.15, "MAE_90D_pct": -4.15, "MFE_180D_pct": 52.56, "MFE_30D_pct": 52.56, "MFE_90D_pct": 52.56, "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "calibration_usable": true, "canonical_archetype_id": "C28_SOFTWARE_SECURITY_CONTRACT_RETENTION", "case_id": "C28_067920_IGLOO_20230118_SECURITY_OPS_CONTRACT_RETENTION_STAGE2", "case_role": "positive_security_ops_contract_retention_stage2_success_with_later_4b", "company_name": "이글루", "corporate_action_window_status": "clean_2023_forward_window; corporate-action candidate is 2014-04-24 and outside selected test window", "current_profile_error": false, "current_profile_verdict": "Stage2 was useful when security-operations/managed-security contract retention and public-sector cyber-budget visibility could plausibly connect to revenue durability; Green still requires renewal rate, backlog, ARR-like maintenance mix, margin and revision bridge. After the February 2023 spike, the same evidence needed local 4B discipline.", "dedupe_for_aggregate": true, "do_not_count_as_new_case": false, "drawdown_after_peak_pct": -41.05, "entry_date": "2023-01-18", "entry_price": 6260, "evidence_family": "security_ops_recurring_contract_retention_public_sector_cyber_budget_stage2_route", "evidence_url_pending": false, "fine_archetype_id": "CYBERSECURITY_CONTRACT_RETENTION_RENEWAL_MARGIN_GUARD", "forward_window_trading_days": 180, "independent_evidence_weight": 1.0, "large_sector_id": "L8_PLATFORM_CONTENT_SW_SECURITY", "low_date_180d": "2023-10-31", "low_price_180d": 5630, "peak_date": "2023-02-10", "peak_price": 9550, "positive_or_counterexample": "positive", "price_adjustment_status": "raw_unadjusted_marcap", "price_basis": "tradable_raw", "price_data_source": "Songdaiki/stock-web", "profile_path": "atlas/symbol_profiles/067/067920.json", "raw_component_score_breakdown": {"bottleneck_pricing_power": 7, "capital_allocation": 2, "eps_fcf_explosion": 8, "information_confidence": 4, "market_mispricing": 10, "total": 49, "valuation_rerating_runway": 8, "visibility_quality": 10}, "reuse_reason": null, "same_entry_group_id": "C28_067920_IGLOO_20230118_SECURITY_OPS_CONTRACT_RETENTION_STAGE2", "schema_version": "v12_no_repeat_standalone_trigger_row_v1", "selected_round": "R8", "source_proxy_only": false, "stage2_evidence_fields": ["software_security_contract_attention", "renewal_or_retention_visibility", "maintenance_revenue_or_public_sector_cyber_budget_signal"], "stage3_evidence_fields": ["contract_renewal_rate_required", "maintenance_revenue_quality_and_backlog_required", "margin_or_revision_bridge_required"], "stage4b_evidence_fields": ["security_theme_or_contract_price_premium", "valuation_or_positioning_overheat", "post_peak_drawdown"], "stage4c_evidence_fields": ["renewal_or_retention_gap", "maintenance_margin_or_project_mix_disappointment", "revision_bridge_failure"], "symbol": "067920", "tradable_shard_path": "atlas/ohlcv_tradable_by_symbol_year/067/067920/2023.csv", "trigger_date": "2023-01-18", "trigger_type": "Stage2-Actionable", "upstream_source": "FinanceData/marcap"}
{"MAE_180D_pct": -21.53, "MAE_30D_pct": -21.53, "MAE_90D_pct": -21.53, "MFE_180D_pct": 10.25, "MFE_30D_pct": 10.25, "MFE_90D_pct": 10.25, "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "calibration_usable": true, "canonical_archetype_id": "C28_SOFTWARE_SECURITY_CONTRACT_RETENTION", "case_id": "C28_203650_DREAMSECURITY_20230920_DIGITAL_ID_SECURITY_PRICE_PREMIUM_4B", "case_role": "digital_id_security_theme_price_premium_counterexample", "company_name": "드림시큐리티", "corporate_action_window_status": "clean_2023_forward_window; corporate-action candidates are 2017-01-20 and 2019-11-26, outside selected test window", "current_profile_error": true, "current_profile_verdict": "Digital-ID/security theme price premium should route to local 4B or counterexample unless contracted customers, renewal/retention, maintenance revenue quality, margin and revision evidence keep expanding after the price spike.", "dedupe_for_aggregate": true, "do_not_count_as_new_case": false, "drawdown_after_peak_pct": -28.82, "entry_date": "2023-09-20", "entry_price": 3855, "evidence_family": "digital_identity_security_theme_price_premium_without_contract_retention_margin_revision_bridge", "evidence_url_pending": false, "fine_archetype_id": "CYBERSECURITY_CONTRACT_RETENTION_RENEWAL_MARGIN_GUARD", "forward_window_trading_days": 180, "independent_evidence_weight": 1.0, "large_sector_id": "L8_PLATFORM_CONTENT_SW_SECURITY", "low_date_180d": "2023-10-30", "low_price_180d": 3025, "peak_date": "2023-09-20", "peak_price": 4250, "positive_or_counterexample": "counterexample", "price_adjustment_status": "raw_unadjusted_marcap", "price_basis": "tradable_raw", "price_data_source": "Songdaiki/stock-web", "profile_path": "atlas/symbol_profiles/203/203650.json", "raw_component_score_breakdown": {"bottleneck_pricing_power": 6, "capital_allocation": 2, "eps_fcf_explosion": 5, "information_confidence": 3, "market_mispricing": 4, "total": 27, "valuation_rerating_runway": 2, "visibility_quality": 5}, "reuse_reason": null, "same_entry_group_id": "C28_203650_DREAMSECURITY_20230920_DIGITAL_ID_SECURITY_PRICE_PREMIUM_4B", "schema_version": "v12_no_repeat_standalone_trigger_row_v1", "selected_round": "R8", "source_proxy_only": false, "stage2_evidence_fields": ["software_security_contract_attention", "renewal_or_retention_visibility", "maintenance_revenue_or_public_sector_cyber_budget_signal"], "stage3_evidence_fields": ["contract_renewal_rate_required", "maintenance_revenue_quality_and_backlog_required", "margin_or_revision_bridge_required"], "stage4b_evidence_fields": ["security_theme_or_contract_price_premium", "valuation_or_positioning_overheat", "post_peak_drawdown"], "stage4c_evidence_fields": ["renewal_or_retention_gap", "maintenance_margin_or_project_mix_disappointment", "revision_bridge_failure"], "symbol": "203650", "tradable_shard_path": "atlas/ohlcv_tradable_by_symbol_year/203/203650/2023.csv", "trigger_date": "2023-09-20", "trigger_type": "4B-local-price-only", "upstream_source": "FinanceData/marcap"}
{"MAE_180D_pct": -25.35, "MAE_30D_pct": -15.43, "MAE_90D_pct": -20.74, "MFE_180D_pct": 4.08, "MFE_30D_pct": 4.08, "MFE_90D_pct": 4.08, "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "calibration_usable": true, "canonical_archetype_id": "C28_SOFTWARE_SECURITY_CONTRACT_RETENTION", "case_id": "C28_042510_RAONSECURE_20230203_AUTH_SECURITY_FALSE_GREEN", "case_role": "authentication_security_contract_retention_false_green_counterexample", "company_name": "라온시큐어", "corporate_action_window_status": "selected 2023 forward window is before 2023-12-18 corporate-action candidate; older candidates are outside selected test window", "current_profile_error": true, "current_profile_verdict": "Authentication/security contract claims should stay Yellow when renewal, maintenance revenue, enterprise/customer expansion, margin and revision evidence do not keep improving. Price confirmation alone was a false-Green risk.", "dedupe_for_aggregate": true, "do_not_count_as_new_case": false, "drawdown_after_peak_pct": -28.28, "entry_date": "2023-02-03", "entry_price": 2820, "evidence_family": "authentication_security_contract_claim_without_retention_maintenance_margin_revision_duration", "evidence_url_pending": false, "fine_archetype_id": "CYBERSECURITY_CONTRACT_RETENTION_RENEWAL_MARGIN_GUARD", "forward_window_trading_days": 180, "independent_evidence_weight": 1.0, "large_sector_id": "L8_PLATFORM_CONTENT_SW_SECURITY", "low_date_180d": "2023-10-31", "low_price_180d": 2105, "peak_date": "2023-02-06", "peak_price": 2935, "positive_or_counterexample": "counterexample", "price_adjustment_status": "raw_unadjusted_marcap", "price_basis": "tradable_raw", "price_data_source": "Songdaiki/stock-web", "profile_path": "atlas/symbol_profiles/042/042510.json", "raw_component_score_breakdown": {"bottleneck_pricing_power": 5, "capital_allocation": 2, "eps_fcf_explosion": 4, "information_confidence": 3, "market_mispricing": 5, "total": 26, "valuation_rerating_runway": 2, "visibility_quality": 5}, "reuse_reason": null, "same_entry_group_id": "C28_042510_RAONSECURE_20230203_AUTH_SECURITY_FALSE_GREEN", "schema_version": "v12_no_repeat_standalone_trigger_row_v1", "selected_round": "R8", "source_proxy_only": false, "stage2_evidence_fields": ["software_security_contract_attention", "renewal_or_retention_visibility", "maintenance_revenue_or_public_sector_cyber_budget_signal"], "stage3_evidence_fields": ["contract_renewal_rate_required", "maintenance_revenue_quality_and_backlog_required", "margin_or_revision_bridge_required"], "stage4b_evidence_fields": ["security_theme_or_contract_price_premium", "valuation_or_positioning_overheat", "post_peak_drawdown"], "stage4c_evidence_fields": ["renewal_or_retention_gap", "maintenance_margin_or_project_mix_disappointment", "revision_bridge_failure"], "symbol": "042510", "tradable_shard_path": "atlas/ohlcv_tradable_by_symbol_year/042/042510/2023.csv", "trigger_date": "2023-02-03", "trigger_type": "Stage3-Yellow", "upstream_source": "FinanceData/marcap"}
```

## 9. Aggregate row

```json
{
  "calibration_usable_case_count": 3,
  "canonical_archetype_id": "C28_SOFTWARE_SECURITY_CONTRACT_RETENTION",
  "counterexample_count": 2,
  "current_profile_error_count": 2,
  "evidence_url_pending_count": 0,
  "fine_archetype_id": "CYBERSECURITY_CONTRACT_RETENTION_RENEWAL_MARGIN_GUARD",
  "hard_duplicate_avoided": true,
  "index_update_needed": true,
  "large_sector_id": "L8_PLATFORM_CONTENT_SW_SECURITY",
  "loop_contribution_label": "software_security_contract_retention_new_symbols_and_theme_price_premium_counterexamples",
  "new_independent_case_count": 3,
  "positive_case_count": 1,
  "reused_case_count": 0,
  "schema_version": "v12_no_repeat_standalone_aggregate_v1",
  "selected_round": "R8",
  "shadow_rule_candidate": "C28 software/security contract-retention rows should allow Stage2 when security-contract renewal, maintenance revenue quality and public-sector/enterprise cyber budget visibility appear before the theme is priced, but Stage3 Green requires renewal rate, backlog, retention, maintenance margin, project mix and revision bridge; security theme price premium without retention proof should route to local 4B or counterexample.",
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
3. Add C28-specific security contract / renewal / maintenance revenue / margin-revision guard only as a shadow candidate until more rows exist.

Candidate rule:
- C28_STAGE2_ALLOWED_ON_RENEWAL_MAINTENANCE_MARGIN_BRIDGE
- C28_GREEN_REQUIRES_RENEWAL_RATE_BACKLOG_MAINTENANCE_REVENUE_MARGIN_REVISION
- C28_SECURITY_THEME_PRICE_PREMIUM_LOCAL_4B
- C28_CONTRACT_RETENTION_WITHOUT_MARGIN_REVISION_COUNTEREXAMPLE

Do not lower global Stage3 Green thresholds.
Do not treat this single MD as production-ready.
```

## 11. Final contribution line

This loop adds 3 new independent cases, 2 counterexamples, and 2 current-profile residual errors for R8/L8_PLATFORM_CONTENT_SW_SECURITY/C28_SOFTWARE_SECURITY_CONTRACT_RETENTION.

