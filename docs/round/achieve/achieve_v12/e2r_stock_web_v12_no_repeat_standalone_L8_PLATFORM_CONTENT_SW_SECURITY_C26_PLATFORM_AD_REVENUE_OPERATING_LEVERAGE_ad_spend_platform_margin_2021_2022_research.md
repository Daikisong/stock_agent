# E2R V12 No-Repeat Standalone Residual Research
## R8 / L8 / C26 — Platform/ad revenue operating-leverage guard

metadata:
```text
selected_round: R8
scheduler_override_used: true
scheduled_round_inherited: false
large_sector_id: L8_PLATFORM_CONTENT_SW_SECURITY
canonical_archetype_id: C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE
fine_archetype_id: AD_SPEND_PLATFORM_MARGIN_REVISION_GUARD
loop_objective: coverage_gap_fill|counterexample_mining|positive_counterexample_balance|4B_non_price_requirement_stress_test|green_strictness_stress_test
price_source: Songdaiki/stock-web
stock_web_manifest_max_date: 2026-02-20
output_file: e2r_stock_web_v12_no_repeat_standalone_L8_PLATFORM_CONTENT_SW_SECURITY_C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE_ad_spend_platform_margin_2021_2022_research.md
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

This run avoids those top-covered C26 symbols and adds 030000, 214320, and 214270.  
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
030000 제일기획: 2021 forward window clean; corporate-action candidates are old, outside the selected test window.
214320 이노션: 2022 forward window clean; corporate-action candidates are in late 2023, outside the selected test window.
214270 FSN: 2022 forward window is after the 2021-11-08 corporate-action candidate; calibration caveat noted but selected window uses post-event tradable rows.
```

## 3. Research thesis

C26 should not treat every ad/platform headline as operating leverage. It should test whether ad attention becomes retained, high-quality revenue:

```text
platform / ad-spend / adtech attention
→ retained advertiser budget
→ digital or project mix quality
→ take-rate or margin expansion
→ revision confirmation
→ rerating
```

The useful distinction is between a campaign and a contract rhythm. A campaign can flare for one quarter; operating leverage needs the budget to return, the mix to improve, and the margin to stay on the books.

## 4. Case table

| case_id | symbol | role | entry | entry_price | peak | low_180d | MFE_30D | MFE_90D | MFE_180D | MAE_180D | post-peak DD |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| C26_030000_CHEIL_20210312_AD_SPEND_REOPENING_OPERATING_LEVERAGE_STAGE2 | 030000 | positive_ad_spend_operating_leverage_stage2_success | 2021-03-12 | 21250 | 26500 on 2021-07-01 | 20700 on 2021-03-23 | 5.88% | 24.71% | 24.71% | -2.59% | -16.6% |
| C26_214320_INNOCEAN_20220331_AUTO_AD_RECOVERY_FALSE_GREEN | 214320 | auto_ad_recovery_false_green_counterexample | 2022-03-31 | 50300 | 50700 on 2022-04-05 | 40800 on 2022-09-28 | 0.8% | 0.8% | 0.8% | -18.89% | -19.53% |
| C26_214270_FSN_20220103_DIGITAL_ADTECH_PRICE_PREMIUM_4B | 214270 | digital_adtech_theme_price_premium_counterexample | 2022-01-03 | 13800 | 14200 on 2022-01-03 | 3180 on 2022-09-28 | 2.9% | 2.9% | 2.9% | -76.96% | -77.61% |

## 5. Stage evidence split

### Stage2 / Stage2-Actionable
- Ad-spend recovery, digital mix improvement, and platform-ad operating leverage can be valid Stage2 routes.
- 030000 is the positive anchor: reopening ad budgets and operating-leverage expectations produced a low-MAE forward MFE.

### Stage3 / Green
- C26 Green should require retained advertiser budget, digital/project mix quality, take-rate or agency margin, and revision confirmation.
- 214320 shows the false-Green risk: auto-ad recovery language was plausible, but the later path argues for Yellow when budget cadence and margin revisions do not continue.

### 4B
- 214270 is the local 4B guard. Digital adtech/platform premium had already moved before retained revenue and margin evidence could support it.
- Price-only adtech premiums should not be treated as fresh Green unless retained revenue, take-rate quality and revision bridge are visible.

### 4C
- No hard accounting break is asserted.
- The C26 break mode is retained-revenue failure: the ad market exists, but advertiser budget, take-rate, project mix, margin and revisions do not carry the valuation.

## 6. Raw component score breakdown

```json
{
  "C26_030000_CHEIL_20210312_AD_SPEND_REOPENING_OPERATING_LEVERAGE_STAGE2": {
    "bottleneck_pricing_power": 8,
    "capital_allocation": 3,
    "eps_fcf_explosion": 10,
    "information_confidence": 4,
    "market_mispricing": 10,
    "total": 54,
    "valuation_rerating_runway": 8,
    "visibility_quality": 11
  },
  "C26_214270_FSN_20220103_DIGITAL_ADTECH_PRICE_PREMIUM_4B": {
    "bottleneck_pricing_power": 5,
    "capital_allocation": 1,
    "eps_fcf_explosion": 4,
    "information_confidence": 3,
    "market_mispricing": 4,
    "total": 22,
    "valuation_rerating_runway": 1,
    "visibility_quality": 4
  },
  "C26_214320_INNOCEAN_20220331_AUTO_AD_RECOVERY_FALSE_GREEN": {
    "bottleneck_pricing_power": 5,
    "capital_allocation": 3,
    "eps_fcf_explosion": 5,
    "information_confidence": 3,
    "market_mispricing": 5,
    "total": 30,
    "valuation_rerating_runway": 3,
    "visibility_quality": 6
  }
}
```

## 7. Current calibrated profile stress test

Suggested C26 guard:
```text
if ad_spend_recovery and digital_mix_margin_bridge_visible:
    allow_stage2_actionable = true

if adtech_or_platform_ad_price_premium and no retained_revenue_margin_revision_bridge:
    block_stage3_green = true
    route_to_local_4B_watch = true

if post_peak_drawdown and advertiser_budget_or_take_rate_bridge_fails:
    route_to_counterexample_or_4C_watch = true
```

Residual errors:
```text
current_profile_error_count = 2
- 214320 / 2022-03-31: auto-ad recovery can be over-promoted if the model does not require budget cadence and margin/revision durability.
- 214270 / 2022-01-03: digital adtech premium can become price-only when retained ad revenue and take-rate/margin proof do not arrive.
```

## 8. Machine-readable rows

```jsonl
{"MAE_180D_pct": -2.59, "MAE_30D_pct": -2.59, "MAE_90D_pct": -2.59, "MFE_180D_pct": 24.71, "MFE_30D_pct": 5.88, "MFE_90D_pct": 24.71, "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "calibration_usable": true, "canonical_archetype_id": "C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE", "case_id": "C26_030000_CHEIL_20210312_AD_SPEND_REOPENING_OPERATING_LEVERAGE_STAGE2", "case_role": "positive_ad_spend_operating_leverage_stage2_success", "company_name": "제일기획", "corporate_action_window_status": "clean_forward_window; corporate-action candidates old or outside selected test window where present", "current_profile_error": false, "current_profile_verdict": "Stage2 was useful when ad-spend reopening, digital mix, and operating leverage were visible; Green still requires retained advertiser budgets, digital/platform mix, margin and revision bridge.", "dedupe_for_aggregate": true, "do_not_count_as_new_case": false, "drawdown_after_peak_pct": -16.6, "entry_date": "2021-03-12", "entry_price": 21250, "evidence_family": "global_ad_spend_reopening_digital_mix_margin_operating_leverage", "evidence_url_pending": false, "fine_archetype_id": "AD_SPEND_PLATFORM_MARGIN_REVISION_GUARD", "forward_window_trading_days": 180, "independent_evidence_weight": 1.0, "large_sector_id": "L8_PLATFORM_CONTENT_SW_SECURITY", "low_date_180d": "2021-03-23", "low_price_180d": 20700, "peak_date": "2021-07-01", "peak_price": 26500, "positive_or_counterexample": "positive", "price_adjustment_status": "raw_unadjusted_marcap", "price_basis": "tradable_raw", "price_data_source": "Songdaiki/stock-web", "profile_path": "atlas/symbol_profiles/030/030000.json", "raw_component_score_breakdown": {"bottleneck_pricing_power": 8, "capital_allocation": 3, "eps_fcf_explosion": 10, "information_confidence": 4, "market_mispricing": 10, "total": 54, "valuation_rerating_runway": 8, "visibility_quality": 11}, "reuse_reason": null, "same_entry_group_id": "C26_030000_CHEIL_20210312_AD_SPEND_REOPENING_OPERATING_LEVERAGE_STAGE2", "schema_version": "v12_no_repeat_standalone_trigger_row_v1", "selected_round": "R8", "source_proxy_only": false, "stage2_evidence_fields": ["platform_or_ad_spend_attention", "retained_advertiser_budget_or_digital_mix_claim", "operating_leverage_or_margin_signal"], "stage3_evidence_fields": ["advertiser_budget_retention_required", "take_rate_or_project_mix_quality_required", "margin_or_revision_bridge_required"], "stage4b_evidence_fields": ["adtech_or_ad_spend_price_premium", "valuation_or_positioning_overheat", "post_peak_drawdown"], "stage4c_evidence_fields": ["ad_budget_cadence_gap", "retained_revenue_or_take_rate_failure", "margin_revision_bridge_failure"], "symbol": "030000", "tradable_shard_path": "atlas/ohlcv_tradable_by_symbol_year/030/030000/2021.csv", "trigger_date": "2021-03-12", "trigger_type": "Stage2-Actionable", "upstream_source": "FinanceData/marcap"}
{"MAE_180D_pct": -18.89, "MAE_30D_pct": -2.88, "MAE_90D_pct": -10.54, "MFE_180D_pct": 0.8, "MFE_30D_pct": 0.8, "MFE_90D_pct": 0.8, "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "calibration_usable": true, "canonical_archetype_id": "C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE", "case_id": "C26_214320_INNOCEAN_20220331_AUTO_AD_RECOVERY_FALSE_GREEN", "case_role": "auto_ad_recovery_false_green_counterexample", "company_name": "이노션", "corporate_action_window_status": "clean_forward_window; corporate-action candidates old or outside selected test window where present", "current_profile_error": true, "current_profile_verdict": "Auto-ad recovery language should stay Yellow when advertiser budget cadence, project mix, overseas agency margin and revision bridge are not improving after the price run.", "dedupe_for_aggregate": true, "do_not_count_as_new_case": false, "drawdown_after_peak_pct": -19.53, "entry_date": "2022-03-31", "entry_price": 50300, "evidence_family": "auto_ad_spend_recovery_headline_without_sustained_budget_margin_revision_bridge", "evidence_url_pending": false, "fine_archetype_id": "AD_SPEND_PLATFORM_MARGIN_REVISION_GUARD", "forward_window_trading_days": 180, "independent_evidence_weight": 1.0, "large_sector_id": "L8_PLATFORM_CONTENT_SW_SECURITY", "low_date_180d": "2022-09-28", "low_price_180d": 40800, "peak_date": "2022-04-05", "peak_price": 50700, "positive_or_counterexample": "counterexample", "price_adjustment_status": "raw_unadjusted_marcap", "price_basis": "tradable_raw", "price_data_source": "Songdaiki/stock-web", "profile_path": "atlas/symbol_profiles/214/214320.json", "raw_component_score_breakdown": {"bottleneck_pricing_power": 5, "capital_allocation": 3, "eps_fcf_explosion": 5, "information_confidence": 3, "market_mispricing": 5, "total": 30, "valuation_rerating_runway": 3, "visibility_quality": 6}, "reuse_reason": null, "same_entry_group_id": "C26_214320_INNOCEAN_20220331_AUTO_AD_RECOVERY_FALSE_GREEN", "schema_version": "v12_no_repeat_standalone_trigger_row_v1", "selected_round": "R8", "source_proxy_only": false, "stage2_evidence_fields": ["platform_or_ad_spend_attention", "retained_advertiser_budget_or_digital_mix_claim", "operating_leverage_or_margin_signal"], "stage3_evidence_fields": ["advertiser_budget_retention_required", "take_rate_or_project_mix_quality_required", "margin_or_revision_bridge_required"], "stage4b_evidence_fields": ["adtech_or_ad_spend_price_premium", "valuation_or_positioning_overheat", "post_peak_drawdown"], "stage4c_evidence_fields": ["ad_budget_cadence_gap", "retained_revenue_or_take_rate_failure", "margin_revision_bridge_failure"], "symbol": "214320", "tradable_shard_path": "atlas/ohlcv_tradable_by_symbol_year/214/214320/2022.csv", "trigger_date": "2022-03-31", "trigger_type": "Stage3-Yellow", "upstream_source": "FinanceData/marcap"}
{"MAE_180D_pct": -76.96, "MAE_30D_pct": -46.09, "MAE_90D_pct": -49.28, "MFE_180D_pct": 2.9, "MFE_30D_pct": 2.9, "MFE_90D_pct": 2.9, "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "calibration_usable": true, "canonical_archetype_id": "C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE", "case_id": "C26_214270_FSN_20220103_DIGITAL_ADTECH_PRICE_PREMIUM_4B", "case_role": "digital_adtech_theme_price_premium_counterexample", "company_name": "FSN", "corporate_action_window_status": "clean_forward_window; corporate-action candidates old or outside selected test window where present", "current_profile_error": true, "current_profile_verdict": "Digital adtech/platform premium should route to local 4B or counterexample unless retained advertiser revenue, take-rate quality, margin and revision evidence remain visible.", "dedupe_for_aggregate": true, "do_not_count_as_new_case": false, "drawdown_after_peak_pct": -77.61, "entry_date": "2022-01-03", "entry_price": 13800, "evidence_family": "digital_adtech_platform_price_premium_without_retained_ad_revenue_margin_bridge", "evidence_url_pending": false, "fine_archetype_id": "AD_SPEND_PLATFORM_MARGIN_REVISION_GUARD", "forward_window_trading_days": 180, "independent_evidence_weight": 1.0, "large_sector_id": "L8_PLATFORM_CONTENT_SW_SECURITY", "low_date_180d": "2022-09-28", "low_price_180d": 3180, "peak_date": "2022-01-03", "peak_price": 14200, "positive_or_counterexample": "counterexample", "price_adjustment_status": "raw_unadjusted_marcap", "price_basis": "tradable_raw", "price_data_source": "Songdaiki/stock-web", "profile_path": "atlas/symbol_profiles/214/214270.json", "raw_component_score_breakdown": {"bottleneck_pricing_power": 5, "capital_allocation": 1, "eps_fcf_explosion": 4, "information_confidence": 3, "market_mispricing": 4, "total": 22, "valuation_rerating_runway": 1, "visibility_quality": 4}, "reuse_reason": null, "same_entry_group_id": "C26_214270_FSN_20220103_DIGITAL_ADTECH_PRICE_PREMIUM_4B", "schema_version": "v12_no_repeat_standalone_trigger_row_v1", "selected_round": "R8", "source_proxy_only": false, "stage2_evidence_fields": ["platform_or_ad_spend_attention", "retained_advertiser_budget_or_digital_mix_claim", "operating_leverage_or_margin_signal"], "stage3_evidence_fields": ["advertiser_budget_retention_required", "take_rate_or_project_mix_quality_required", "margin_or_revision_bridge_required"], "stage4b_evidence_fields": ["adtech_or_ad_spend_price_premium", "valuation_or_positioning_overheat", "post_peak_drawdown"], "stage4c_evidence_fields": ["ad_budget_cadence_gap", "retained_revenue_or_take_rate_failure", "margin_revision_bridge_failure"], "symbol": "214270", "tradable_shard_path": "atlas/ohlcv_tradable_by_symbol_year/214/214270/2022.csv", "trigger_date": "2022-01-03", "trigger_type": "4B-local-price-only", "upstream_source": "FinanceData/marcap"}
```

## 9. Aggregate row

```json
{
  "calibration_usable_case_count": 3,
  "canonical_archetype_id": "C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE",
  "counterexample_count": 2,
  "current_profile_error_count": 2,
  "evidence_url_pending_count": 0,
  "fine_archetype_id": "AD_SPEND_PLATFORM_MARGIN_REVISION_GUARD",
  "hard_duplicate_avoided": true,
  "index_update_needed": true,
  "large_sector_id": "L8_PLATFORM_CONTENT_SW_SECURITY",
  "loop_contribution_label": "platform_ad_revenue_adspend_operating_leverage_new_symbols_added",
  "new_independent_case_count": 3,
  "positive_case_count": 1,
  "reused_case_count": 0,
  "schema_version": "v12_no_repeat_standalone_aggregate_v1",
  "selected_round": "R8",
  "shadow_rule_candidate": "C26 platform/ad-revenue operating-leverage rows should allow Stage2 on early ad-spend recovery and digital mix evidence, but Stage3 Green requires retained advertiser budget, take-rate/project mix quality, margin and revision bridge; adtech price premium without retained revenue proof should route to local 4B or counterexample.",
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
3. Add C26-specific ad-spend / platform-ad / retained-revenue / margin-revision guard only as a shadow candidate until more rows exist.

Candidate rule:
- C26_STAGE2_ALLOWED_ON_AD_SPEND_RECOVERY_DIGITAL_MIX
- C26_GREEN_REQUIRES_RETAINED_ADVERTISER_BUDGET_TAKE_RATE_MARGIN_REVISION
- C26_ADTECH_PLATFORM_PRICE_PREMIUM_LOCAL_4B
- C26_AD_RECOVERY_WITHOUT_BUDGET_CADENCE_COUNTEREXAMPLE

Do not lower global Stage3 Green thresholds.
Do not treat this single MD as production-ready.
```

## 11. Final contribution line

This loop adds 3 new independent cases, 2 counterexamples, and 2 current-profile residual errors for R8/L8_PLATFORM_CONTENT_SW_SECURITY/C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE.

