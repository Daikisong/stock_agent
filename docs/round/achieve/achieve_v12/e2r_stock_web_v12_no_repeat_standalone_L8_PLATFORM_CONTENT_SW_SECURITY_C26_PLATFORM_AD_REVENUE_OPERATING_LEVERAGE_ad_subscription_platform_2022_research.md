# E2R V12 No-Repeat Standalone Residual Research
## R8 / L8 / C26 — Platform/ad revenue operating-leverage guard

metadata:
```text
selected_round: R8
scheduler_override_used: true
scheduled_round_inherited: false
large_sector_id: L8_PLATFORM_CONTENT_SW_SECURITY
canonical_archetype_id: C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE
fine_archetype_id: AD_SUBSCRIPTION_PLATFORM_OPERATING_LEVERAGE_GUARD
loop_objective: coverage_gap_fill|counterexample_mining|green_strictness_stress_test|4B_non_price_requirement_stress_test
price_source: Songdaiki/stock-web
stock_web_manifest_max_date: 2026-02-20
output_file: e2r_stock_web_v12_no_repeat_standalone_L8_PLATFORM_CONTENT_SW_SECURITY_C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE_ad_subscription_platform_2022_research.md
production_scoring_changed: false
shadow_weight_only: true
```

## 1. Prompt / no-repeat basis

This MD follows `docs/core/e2r_v12_prompt_round_scheduler_corrected.txt` as a standalone historical residual research artifact.  
`V12_Research_No_Repeat_Index.md` is used only for duplicate avoidance and coverage-gap selection.

No-Repeat selection:
```text
C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE current coverage:
rows=65, symbols=10, date range=2020-04-27~2024-07-11, good/bad S2=28/6, 4B/4C=7/1
top covered symbols: 067160(11), 035420(7), 035720(7), 089600(6), 216050(5)
```

This run avoids those top-covered C26 symbols and adds 030000, 376300, and 214320.  
Each row uses a new `C26 + symbol + trigger_type + entry_date` hard key.

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
030000 제일기획: 2022 forward window clean; corporate-action candidates are old, outside the test window.
376300 디어유: corporate_action_candidate_count=0.
214320 이노션: 2022 forward window clean; corporate-action candidates are in 2023, outside the test window.
```

## 3. Research thesis

C26 should not be a generic platform or ad-theme bucket. It should test whether attention becomes operating leverage:

```text
platform / subscriber / ad-budget attention
→ ARPU, ad-revenue mix, or paying-user quality
→ retention or budget durability
→ operating leverage
→ margin/revision bridge
→ rerating
```

The residual failure mode is that the market often prices a platform symbol before the revenue engine has enough torque. A high-multiple subscription or ad-recovery story can run first, then roll over if ARPU, retention, budget durability, and revision do not arrive.

## 4. Case table

| case_id | symbol | role | entry | entry_price | peak | low_180d | MFE_30D | MFE_90D | MFE_180D | MAE_180D | post-peak DD |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| C26_030000_CHEIL_20220715_AD_AGENCY_OPERATING_LEVERAGE_STAGE2 | 030000 | positive_stage2_operating_leverage_recovery | 2022-07-15 | 21750 | 24950 on 2022-10-27 | 21200 on 2022-07-15 | 8.97% | 14.71% | 14.71% | -2.53% | -9.62% |
| C26_376300_DEARU_20211116_SUBSCRIPTION_PLATFORM_PRICE_ONLY_4B | 376300 | subscription_platform_blowoff_counterexample | 2021-11-16 | 90100 | 99100 on 2021-11-16 | 30200 on 2022-07-04 | 9.99% | 9.99% | 9.99% | -66.48% | -69.53% |
| C26_214320_INNOCEAN_20220511_AD_REVENUE_STAGE3_YELLOW_FADE | 214320 | ad_budget_operating_leverage_false_green | 2022-05-11 | 51500 | 52500 on 2022-05-11 | 37450 on 2022-10-21 | 1.94% | 1.94% | 1.94% | -27.28% | -28.67% |

## 5. Stage evidence split

### Stage2 / Stage2-Actionable
- Platform/subscriber attention and ad-budget recovery can be valid routing signals.
- 030000 is the positive anchor: the price path supported a Stage2 recovery after the July 2022 low, but the signal was not strong enough for automatic Green.

### Stage3 / Green
- C26 Green should require ARPU or ad-revenue mix, retention/budget durability, and margin/revision bridge.
- 376300 and 214320 show why price confirmation alone should not be treated as operating leverage.

### 4B
- 376300 is the clearest local 4B row: the subscription-platform premium expanded violently, then gave back most of the move.
- Full-window 4B should require non-price evidence of saturation or revision deceleration, while local 4B can activate on peak-proximity and price-premium stress.

### 4C
- No hard accounting break is asserted.
- The C26 break mode is softer: subscriber retention, ad-budget durability, ARPU, or margin leverage fails to validate the valuation already priced in.

## 6. Raw component score breakdown

```json
{
  "C26_030000_CHEIL_20220715_AD_AGENCY_OPERATING_LEVERAGE_STAGE2": {
    "bottleneck_pricing_power": 6,
    "capital_allocation": 3,
    "eps_fcf_explosion": 9,
    "information_confidence": 4,
    "market_mispricing": 9,
    "total": 49,
    "valuation_rerating_runway": 8,
    "visibility_quality": 10
  },
  "C26_214320_INNOCEAN_20220511_AD_REVENUE_STAGE3_YELLOW_FADE": {
    "bottleneck_pricing_power": 5,
    "capital_allocation": 3,
    "eps_fcf_explosion": 5,
    "information_confidence": 3,
    "market_mispricing": 6,
    "total": 32,
    "valuation_rerating_runway": 4,
    "visibility_quality": 6
  },
  "C26_376300_DEARU_20211116_SUBSCRIPTION_PLATFORM_PRICE_ONLY_4B": {
    "bottleneck_pricing_power": 6,
    "capital_allocation": 1,
    "eps_fcf_explosion": 5,
    "information_confidence": 3,
    "market_mispricing": 4,
    "total": 26,
    "valuation_rerating_runway": 2,
    "visibility_quality": 5
  }
}
```

## 7. Current calibrated profile stress test

Suggested C26 guard:
```text
if platform_ad_attention and no arpu_retention_budget_margin_revision_bridge:
    cap_stage = Stage2-Actionable or Stage3-Yellow
    block_stage3_green = true

if subscription_platform_or_ad_revenue_price_premium and no durable_non_price_bridge:
    route_to_local_4B_watch = true

if post_peak_drawdown and revision_or_operating_leverage_bridge_fails:
    route_to_counterexample_or_4C_watch = true
```

Residual errors:
```text
current_profile_error_count = 2
- 376300 / 2021-11-16: subscription-platform premium can be over-promoted if retention/ARPU and revision evidence are not required.
- 214320 / 2022-05-11: ad-budget recovery labels can become false Green if operating leverage and revision durability are weak.
```

## 8. Machine-readable rows

```jsonl
{"MAE_180D_pct": -2.53, "MAE_30D_pct": -2.53, "MAE_90D_pct": -2.53, "MFE_180D_pct": 14.71, "MFE_30D_pct": 8.97, "MFE_90D_pct": 14.71, "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "calibration_usable": true, "canonical_archetype_id": "C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE", "case_id": "C26_030000_CHEIL_20220715_AD_AGENCY_OPERATING_LEVERAGE_STAGE2", "case_role": "positive_stage2_operating_leverage_recovery", "company_name": "제일기획", "corporate_action_window_status": "clean_180d_by_profile_or_outside_candidate_dates", "current_profile_error": false, "current_profile_verdict": "Stage2 was useful when ad-budget recovery and operating leverage were plausible, but Green should still require revenue mix, margin, and revision bridge.", "dedupe_for_aggregate": true, "do_not_count_as_new_case": false, "drawdown_after_peak_pct": -9.62, "entry_date": "2022-07-15", "entry_price": 21750, "evidence_family": "advertising_revenue_recovery_operating_leverage_with_budget_visibility", "evidence_url_pending": false, "fine_archetype_id": "AD_SUBSCRIPTION_PLATFORM_OPERATING_LEVERAGE_GUARD", "forward_window_trading_days": 180, "independent_evidence_weight": 1.0, "large_sector_id": "L8_PLATFORM_CONTENT_SW_SECURITY", "low_date_180d": "2022-07-15", "low_price_180d": 21200, "peak_date": "2022-10-27", "peak_price": 24950, "positive_or_counterexample": "positive", "price_adjustment_status": "raw_unadjusted_marcap", "price_basis": "tradable_raw", "price_data_source": "Songdaiki/stock-web", "profile_path": "atlas/symbol_profiles/030/030000.json", "raw_component_score_breakdown": {"bottleneck_pricing_power": 6, "capital_allocation": 3, "eps_fcf_explosion": 9, "information_confidence": 4, "market_mispricing": 9, "total": 49, "valuation_rerating_runway": 8, "visibility_quality": 10}, "reuse_reason": null, "same_entry_group_id": "C26_030000_CHEIL_20220715_AD_AGENCY_OPERATING_LEVERAGE_STAGE2", "schema_version": "v12_no_repeat_standalone_trigger_row_v1", "selected_round": "R8", "source_proxy_only": false, "stage2_evidence_fields": ["platform_or_ad_revenue_attention", "subscriber_or_ad_budget_visibility_claim", "relative_strength"], "stage3_evidence_fields": ["arpu_or_ad_revenue_mix_required", "retention_or_budget_durability_required", "operating_leverage_and_revision_bridge_required"], "stage4b_evidence_fields": ["platform_or_ad_revenue_price_premium", "valuation_or_positioning_overheat", "post_peak_drawdown"], "stage4c_evidence_fields": ["subscriber_retention_or_budget_fade", "arpu_margin_bridge_gap", "revision_or_operating_leverage_break"], "symbol": "030000", "tradable_shard_path": "atlas/ohlcv_tradable_by_symbol_year/030/030000/2022.csv", "trigger_date": "2022-07-15", "trigger_type": "Stage2-Actionable", "upstream_source": "FinanceData/marcap"}
{"MAE_180D_pct": -66.48, "MAE_30D_pct": -32.19, "MAE_90D_pct": -55.05, "MFE_180D_pct": 9.99, "MFE_30D_pct": 9.99, "MFE_90D_pct": 9.99, "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "calibration_usable": true, "canonical_archetype_id": "C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE", "case_id": "C26_376300_DEARU_20211116_SUBSCRIPTION_PLATFORM_PRICE_ONLY_4B", "case_role": "subscription_platform_blowoff_counterexample", "company_name": "디어유", "corporate_action_window_status": "clean_180d_by_profile_or_outside_candidate_dates", "current_profile_error": true, "current_profile_verdict": "Subscription-platform price premium should not become Green without paying-user retention, ARPU, platform take-rate, and revision evidence.", "dedupe_for_aggregate": true, "do_not_count_as_new_case": false, "drawdown_after_peak_pct": -69.53, "entry_date": "2021-11-16", "entry_price": 90100, "evidence_family": "fan_platform_subscription_premium_without_arr_retention_revision_bridge", "evidence_url_pending": false, "fine_archetype_id": "AD_SUBSCRIPTION_PLATFORM_OPERATING_LEVERAGE_GUARD", "forward_window_trading_days": 180, "independent_evidence_weight": 1.0, "large_sector_id": "L8_PLATFORM_CONTENT_SW_SECURITY", "low_date_180d": "2022-07-04", "low_price_180d": 30200, "peak_date": "2021-11-16", "peak_price": 99100, "positive_or_counterexample": "counterexample", "price_adjustment_status": "raw_unadjusted_marcap", "price_basis": "tradable_raw", "price_data_source": "Songdaiki/stock-web", "profile_path": "atlas/symbol_profiles/376/376300.json", "raw_component_score_breakdown": {"bottleneck_pricing_power": 6, "capital_allocation": 1, "eps_fcf_explosion": 5, "information_confidence": 3, "market_mispricing": 4, "total": 26, "valuation_rerating_runway": 2, "visibility_quality": 5}, "reuse_reason": null, "same_entry_group_id": "C26_376300_DEARU_20211116_SUBSCRIPTION_PLATFORM_PRICE_ONLY_4B", "schema_version": "v12_no_repeat_standalone_trigger_row_v1", "selected_round": "R8", "source_proxy_only": false, "stage2_evidence_fields": ["platform_or_ad_revenue_attention", "subscriber_or_ad_budget_visibility_claim", "relative_strength"], "stage3_evidence_fields": ["arpu_or_ad_revenue_mix_required", "retention_or_budget_durability_required", "operating_leverage_and_revision_bridge_required"], "stage4b_evidence_fields": ["platform_or_ad_revenue_price_premium", "valuation_or_positioning_overheat", "post_peak_drawdown"], "stage4c_evidence_fields": ["subscriber_retention_or_budget_fade", "arpu_margin_bridge_gap", "revision_or_operating_leverage_break"], "symbol": "376300", "tradable_shard_path": "atlas/ohlcv_tradable_by_symbol_year/376/376300/2021.csv", "trigger_date": "2021-11-16", "trigger_type": "4B-local-price-only", "upstream_source": "FinanceData/marcap"}
{"MAE_180D_pct": -27.28, "MAE_30D_pct": -14.85, "MAE_90D_pct": -14.85, "MFE_180D_pct": 1.94, "MFE_30D_pct": 1.94, "MFE_90D_pct": 1.94, "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "calibration_usable": true, "canonical_archetype_id": "C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE", "case_id": "C26_214320_INNOCEAN_20220511_AD_REVENUE_STAGE3_YELLOW_FADE", "case_role": "ad_budget_operating_leverage_false_green", "company_name": "이노션", "corporate_action_window_status": "clean_180d_by_profile_or_outside_candidate_dates", "current_profile_error": true, "current_profile_verdict": "Ad-budget recovery labels should remain Yellow when operating leverage and revision confirmation are weak; price confirmation alone creates false-Green risk.", "dedupe_for_aggregate": true, "do_not_count_as_new_case": false, "drawdown_after_peak_pct": -28.67, "entry_date": "2022-05-11", "entry_price": 51500, "evidence_family": "ad_agency_revenue_reopening_without_durable_margin_revision_bridge", "evidence_url_pending": false, "fine_archetype_id": "AD_SUBSCRIPTION_PLATFORM_OPERATING_LEVERAGE_GUARD", "forward_window_trading_days": 180, "independent_evidence_weight": 1.0, "large_sector_id": "L8_PLATFORM_CONTENT_SW_SECURITY", "low_date_180d": "2022-10-21", "low_price_180d": 37450, "peak_date": "2022-05-11", "peak_price": 52500, "positive_or_counterexample": "counterexample", "price_adjustment_status": "raw_unadjusted_marcap", "price_basis": "tradable_raw", "price_data_source": "Songdaiki/stock-web", "profile_path": "atlas/symbol_profiles/214/214320.json", "raw_component_score_breakdown": {"bottleneck_pricing_power": 5, "capital_allocation": 3, "eps_fcf_explosion": 5, "information_confidence": 3, "market_mispricing": 6, "total": 32, "valuation_rerating_runway": 4, "visibility_quality": 6}, "reuse_reason": null, "same_entry_group_id": "C26_214320_INNOCEAN_20220511_AD_REVENUE_STAGE3_YELLOW_FADE", "schema_version": "v12_no_repeat_standalone_trigger_row_v1", "selected_round": "R8", "source_proxy_only": false, "stage2_evidence_fields": ["platform_or_ad_revenue_attention", "subscriber_or_ad_budget_visibility_claim", "relative_strength"], "stage3_evidence_fields": ["arpu_or_ad_revenue_mix_required", "retention_or_budget_durability_required", "operating_leverage_and_revision_bridge_required"], "stage4b_evidence_fields": ["platform_or_ad_revenue_price_premium", "valuation_or_positioning_overheat", "post_peak_drawdown"], "stage4c_evidence_fields": ["subscriber_retention_or_budget_fade", "arpu_margin_bridge_gap", "revision_or_operating_leverage_break"], "symbol": "214320", "tradable_shard_path": "atlas/ohlcv_tradable_by_symbol_year/214/214320/2022.csv", "trigger_date": "2022-05-11", "trigger_type": "Stage3-Yellow", "upstream_source": "FinanceData/marcap"}
```

## 9. Aggregate row

```json
{
  "calibration_usable_case_count": 3,
  "canonical_archetype_id": "C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE",
  "counterexample_count": 2,
  "current_profile_error_count": 2,
  "evidence_url_pending_count": 0,
  "fine_archetype_id": "AD_SUBSCRIPTION_PLATFORM_OPERATING_LEVERAGE_GUARD",
  "hard_duplicate_avoided": true,
  "index_update_needed": true,
  "large_sector_id": "L8_PLATFORM_CONTENT_SW_SECURITY",
  "loop_contribution_label": "platform_ad_revenue_operating_leverage_counterexample_added",
  "new_independent_case_count": 3,
  "positive_case_count": 1,
  "reused_case_count": 0,
  "schema_version": "v12_no_repeat_standalone_aggregate_v1",
  "selected_round": "R8",
  "shadow_rule_candidate": "C26 platform/ad-revenue rerating should permit Stage2 on subscriber/ad-budget attention, but Stage3 Green requires ARPU or ad-revenue mix, retention/budget durability, operating leverage, and revision bridge; IPO/subscription-platform price premium without retention proof should route to local 4B or counterexample.",
  "source_proxy_only_count": 0
}
```

## 10. Deferred Coding Agent Handoff Prompt

Do not execute this handoff inside the research session.

```text
Read this standalone v12 residual research MD.
Before batch apply:
1. Verify all OHLC rows again from Songdaiki/stock-web tradable shards.
2. Check no hard duplicate exists for C26 + symbol + trigger_type + entry_date.
3. Add C26-specific ARPU/ad-mix/retention/budget-durability operating-leverage guard only as a shadow candidate until more rows exist.

Candidate rule:
- C26_GREEN_REQUIRES_ARPU_ADMIX_RETENTION_MARGIN_REVISION
- C26_SUBSCRIPTION_PLATFORM_PRICE_PREMIUM_LOCAL_4B
- C26_AD_BUDGET_RECOVERY_WITHOUT_OPERATING_LEVERAGE_COUNTEREXAMPLE

Do not lower global Stage3 Green thresholds.
Do not treat this single MD as production-ready.
```

## 11. Final contribution line

This loop adds 3 new independent cases, 2 counterexamples, and 2 current-profile residual errors for R8/L8_PLATFORM_CONTENT_SW_SECURITY/C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE.

