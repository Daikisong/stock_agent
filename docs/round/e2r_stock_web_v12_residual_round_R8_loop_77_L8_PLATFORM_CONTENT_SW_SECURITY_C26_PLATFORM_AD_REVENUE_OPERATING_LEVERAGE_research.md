# E2R Stock-Web v12 Residual Research — R8 Loop 77 / L8 / C26

## Metadata

```json
{
  "research_session": "post_calibrated_sector_archetype_residual_research",
  "mode": "historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12",
  "scheduled_round": "R8",
  "scheduled_loop": 77,
  "round_schedule_status": "valid",
  "round_sector_consistency": "pass",
  "completed_round": "R8",
  "completed_loop": 77,
  "computed_next_round": "R9",
  "computed_next_loop": 77,
  "large_sector_id": "L8_PLATFORM_CONTENT_SW_SECURITY",
  "canonical_archetype_id": "C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE",
  "fine_archetype_id": "ADTECH_MEDIA_BUYING_PLATFORM_ROAS_BUDGET_OPERATING_LEVERAGE_BRIDGE_VS_AD_THEME_FADE",
  "loop_objective": [
    "coverage_gap_fill",
    "counterexample_mining",
    "4B_non_price_requirement_stress_test",
    "platform_ad_revenue_operating_leverage_guardrail",
    "adtech_budget_ROAS_margin_bridge_vs_theme_beta",
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

Previous completed state in this interactive run: R7 / loop 77.

Therefore:

```text
scheduled_round = R8
scheduled_loop = 77
allowed_large_sector = L8_PLATFORM_CONTENT_SW_SECURITY
selected_large_sector = L8_PLATFORM_CONTENT_SW_SECURITY
selected_canonical_archetype_id = C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE
computed_next_round = R9
computed_next_loop = 77
```

R8 was routed to C26 because loop 76 used C27 and C28 was already used in a recent prior R8 path.  
This file tests platform ad revenue / media-buying operating leverage rather than content IP monetization or software/security contract retention.

## No-Repeat / novelty check

No hard duplicate is intentionally reused.

Hard duplicate key checked conceptually:

```text
canonical_archetype_id + symbol + trigger_type + entry_date
```

No-Repeat shows C26 is concentrated in:

```text
067160, 035420, 035720, 089600, 216050
```

This run uses three different symbols:

```text
237820 / 플레이디 / adtech media-buying ROAS and operating-leverage bridge
273060 / 와이즈버즈 / ad-platform theme fade
363260 / 모비데이즈 / post-CA adtech theme fade
```

Data-quality note:

```text
All three rows are stock-web calibration usable by profile-level corporate-action candidates.
All three rows are source_proxy_only=true / evidence_url_pending=true.
363260 has a 2024-05-24 corporate-action candidate, so the selected trigger starts 2024-05-27 after that candidate date.
```

## Research thesis

C26 is not “광고 플랫폼주가 올랐다.”

The mechanism must pass through:

```text
advertiser budget recovery
→ ROAS / media-buying efficiency
→ repeat spend or client retention
→ platform revenue
→ margin / operating leverage
→ durable rerating
```

광고 플랫폼의 주가 급등은 전광판이 켜진 것일 수 있다.  
C26은 그 전광판 뒤에서 실제 광고 예산, 캠페인 효율, 반복 집행, 영업레버리지가 돌아가는지를 본다.

---

## Case 1 — Positive with lifecycle 4B: 237820 / 플레이디

### Evidence status

```text
source_proxy_only = true
evidence_url_pending = true
source_repair_required = true
```

The source-repair task is advertiser budget recovery, ROAS/media-buying efficiency, repeat spend, platform revenue and margin bridge evidence.

```text
evidence_family = ADTECH_MEDIA_BUYING_PLATFORM_ADVERTISER_BUDGET_ROAS_REVENUE_MARGIN_BRIDGE
case_role = positive_with_later_4b_watch
trigger_date = 2024-02-01
entry_date = 2024-02-02
entry_price = 5,600
```

### Stock-Web price path

Observed rows from `atlas/ohlcv_tradable_by_symbol_year/237/237820/2024.csv`:

```text
2024-02-02,5600,6820,5570,6820
2024-02-27,8740,10100,7920,8900
2024-03-06,10550,10660,9240,9800
2024-04-17,6680,7600,6530,6820
2024-07-26,7990,8380,7220,7730
2024-09-09,4730,4965,4690,4955
```

### Backtest

```text
MFE_30D  = +90.36%
MAE_30D  = -0.54%
MFE_90D  = +90.36%
MAE_90D  = -0.54%
MFE_180D = +90.36%
MAE_180D = -16.25%
peak_180 = 10,660 on 2024-03-06
trough_180 = 4,690 on 2024-09-09
peak_to_later_drawdown = -56.00%
```

### Interpretation

This is the usable C26 MFE candidate.  
The early path had strong relative strength and controlled entry-basis MAE.

Correct treatment:

```text
verified advertiser budget / ROAS / platform revenue / margin bridge → Stage2 possible
bridge stale after peak → lifecycle local 4B-watch
```

---

## Case 2 — Counterexample / local 4B: 273060 / 와이즈버즈

### Evidence status

```text
source_proxy_only = true
evidence_url_pending = true
source_repair_required = true
```

This row tests digital-ad / AI-ad platform theme beta without enough advertiser-budget, ROAS and margin bridge.

```text
evidence_family = AD_PLATFORM_AI_AD_TECH_THEME_WITH_WEAK_ADVERTISER_BUDGET_ROAS_MARGIN_BRIDGE
case_role = counterexample_ad_platform_beta_local4b
trigger_date = 2024-02-01
entry_date = 2024-02-02
entry_price = 1,407
```

### Stock-Web price path

Observed rows from `atlas/ohlcv_tradable_by_symbol_year/273/273060/2024.csv`:

```text
2024-02-02,1407,1468,1321,1392
2024-02-20,1400,1560,1388,1446
2024-03-06,1767,1834,1596,1621
2024-04-16,1180,1195,1148,1155
2024-04-24,1230,1591,1228,1580
2024-07-03,1132,1147,1118,1122
```

### Backtest

```text
MFE_30D  = +30.35%
MAE_30D  = -6.11%
MFE_90D  = +30.35%
MAE_90D  = -18.41%
MFE_180D = +30.35%
MAE_180D = -20.54%
peak_180 = 1,834 on 2024-03-06
trough_180 = 1,118 on 2024-07-03
peak_to_later_drawdown = -39.04%
```

### Interpretation

This is a C26 false-positive boundary.  
The first MFE was tradable, but it did not validate durable ad-platform operating leverage.

Correct treatment:

```text
ad-platform / AI-ad theme beta
→ no verified advertiser budget / ROAS / margin bridge
→ local 4B-watch
```

---

## Case 3 — Counterexample / post-CA local 4B: 363260 / 모비데이즈

### Evidence status

```text
source_proxy_only = true
evidence_url_pending = true
post_corporate_action_validation_required = true
source_repair_required = true
```

This row tests post-corporate-action adtech theme beta without enough advertiser-budget, ROAS, platform revenue retention and margin bridge.

```text
evidence_family = MOBILE_ADTECH_THEME_POST_CA_WITH_WEAK_ADVERTISER_BUDGET_ROAS_REVENUE_MARGIN_BRIDGE
case_role = counterexample_post_ca_adtech_theme_local4b
trigger_date = 2024-05-24
entry_date = 2024-05-27
entry_price = 2,885
```

### Stock-Web price path

Observed rows from `atlas/ohlcv_tradable_by_symbol_year/363/363260/2024.csv`:

```text
2024-05-24,2985,3160,2875,2875
2024-05-27,2885,2885,2510,2575
2024-05-29,2450,3200,2435,2705
2024-07-02,2155,2245,2150,2205
2024-08-05,2110,2125,1623,1774
2024-10-23,2475,2985,2120,2635
2024-11-15,1530,1583,1476,1516
```

### Backtest

```text
MFE_30D  = +10.92%
MAE_30D  = -25.48%
MFE_90D  = +10.92%
MAE_90D  = -43.74%
MFE_180D = +10.92%
MAE_180D = -48.84%
peak_180 = 3,200 on 2024-05-29
trough_180 = 1,476 on 2024-11-15
peak_to_later_drawdown = -53.88%
```

### Interpretation

This is not a clean C26 positive.  
Even after moving entry to the post-CA window, the path quickly became high-MAE.

Correct treatment:

```text
post-CA adtech theme beta
→ no advertiser budget / ROAS / retention / margin bridge
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
do_not_raise_generic_C26_adtech_theme_weight = true
do_not_treat_all_ad_platform_MFE_as_Green = true
do_not_convert_adtech_drawdown_to_hard_4C_without_non_price_budget_ROAS_client_or_margin_break = true
```

### Candidate canonical compression

Fine labels can compress into:

```text
ADTECH_MEDIA_BUYING_PLATFORM_ROAS_BUDGET_OPERATING_LEVERAGE_BRIDGE_VS_AD_THEME_FADE
```

This fine archetype covers:

```text
1. media-buying platform advertiser-budget / ROAS bridge → Stage2 possible after source repair
2. ad-platform / AI-ad theme without margin bridge → false Stage2 / local 4B
3. post-CA mobile adtech theme without revenue-retention bridge → false Stage2 / local 4B
```

---

## Machine-readable rows

### price source validation row

```jsonl
{"row_type": "price_source_validation", "source": "Songdaiki/stock-web", "source_url": "https://github.com/Songdaiki/stock-web", "manifest_path": "atlas/manifest.json", "schema_path": "atlas/schema.json", "universe_path": "atlas/universe/all_symbols.csv", "manifest_max_date": "2026-02-20", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "raw_shard_root": "atlas/ohlcv_raw_by_symbol_year", "validation_status": "usable_for_historical_calibration"}
```

### case rows

```jsonl
{"row_type": "case", "case_id": "R8L77-C26-237820-PLAYD-ADTECH-ROAS-BUDGET-OPERATING-LEVERAGE", "symbol": "237820", "company_name": "플레이디", "round": "R8", "loop": "77", "large_sector_id": "L8_PLATFORM_CONTENT_SW_SECURITY", "canonical_archetype_id": "C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE", "fine_archetype_id": "ADTECH_MEDIA_BUYING_PLATFORM_ROAS_BUDGET_OPERATING_LEVERAGE_BRIDGE_VS_AD_THEME_FADE", "case_type": "platform_ad_revenue_operating_leverage", "positive_or_counterexample": "positive", "best_trigger": "Stage2-Actionable-AdTechROASBudgetOperatingLeverageBridgeWithLifecycle4B", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 0.5, "score_price_alignment": "C26 should allow adtech/platform positives only when advertiser budget recovery, ROAS/performance evidence, media-buying platform revenue and operating leverage bridge are visible. PlayD produced very large MFE with controlled entry-basis MAE, but the later post-peak drawdown requires lifecycle local 4B if ad-budget/ROAS/margin evidence fades.", "current_profile_verdict": "source_repair_required_before_runtime_weight", "price_source": "Songdaiki/stock-web", "notes": "Stock-web path usable; non-proxy advertiser budget, ROAS, repeat spend, platform revenue retention and operating leverage evidence required before runtime promotion."}
{"row_type": "case", "case_id": "R8L77-C26-273060-WISEBIRDS-AD-PLATFORM-THEME-FADE", "symbol": "273060", "company_name": "와이즈버즈", "round": "R8", "loop": "77", "large_sector_id": "L8_PLATFORM_CONTENT_SW_SECURITY", "canonical_archetype_id": "C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE", "fine_archetype_id": "ADTECH_MEDIA_BUYING_PLATFORM_ROAS_BUDGET_OPERATING_LEVERAGE_BRIDGE_VS_AD_THEME_FADE", "case_type": "platform_ad_revenue_operating_leverage", "positive_or_counterexample": "counterexample", "best_trigger": "Stage2-FalsePositive / AdPlatformROASBudgetThemeFade", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 0.5, "score_price_alignment": "C26 should not treat digital-ad or AI-ad platform beta as durable Stage2 unless advertiser budget, ROAS, media buying efficiency, repeat spend and margin bridge refreshes. Wisebirds had a tradable MFE but then a deep post-peak fade, making it a local 4B-watch row rather than durable Green.", "current_profile_verdict": "source_repair_required_before_runtime_weight", "price_source": "Songdaiki/stock-web", "notes": "Stock-web path usable; non-proxy advertiser budget, ROAS, repeat spend, platform revenue retention and operating leverage evidence required before runtime promotion."}
{"row_type": "case", "case_id": "R8L77-C26-363260-MOBIDAYS-POST-CA-ADTECH-THEME-FADE", "symbol": "363260", "company_name": "모비데이즈", "round": "R8", "loop": "77", "large_sector_id": "L8_PLATFORM_CONTENT_SW_SECURITY", "canonical_archetype_id": "C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE", "fine_archetype_id": "ADTECH_MEDIA_BUYING_PLATFORM_ROAS_BUDGET_OPERATING_LEVERAGE_BRIDGE_VS_AD_THEME_FADE", "case_type": "platform_ad_revenue_operating_leverage", "positive_or_counterexample": "counterexample", "best_trigger": "Stage2-FalsePositive / PostCAAdTechThemeFade", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 0.5, "score_price_alignment": "C26 should not treat post-corporate-action adtech theme spikes as durable Stage2 unless advertiser budget, campaign ROAS, platform revenue retention and operating leverage bridge are verified. Mobidays was measured only after the 2024-05-24 corporate-action candidate; the post-entry path showed weak MFE and high MAE, so it is a post-CA local 4B boundary.", "current_profile_verdict": "source_repair_required_before_runtime_weight", "price_source": "Songdaiki/stock-web", "notes": "Stock-web path usable; non-proxy advertiser budget, ROAS, repeat spend, platform revenue retention and operating leverage evidence required before runtime promotion."}
```

### trigger rows

```jsonl
{"row_type": "trigger", "trigger_id": "TRG_R8L77-C26-237820-PLAYD-ADTECH-ROAS-BUDGET-OPERATING-LEVERAGE", "case_id": "R8L77-C26-237820-PLAYD-ADTECH-ROAS-BUDGET-OPERATING-LEVERAGE", "symbol": "237820", "company_name": "플레이디", "round": "R8", "loop": "77", "large_sector_id": "L8_PLATFORM_CONTENT_SW_SECURITY", "canonical_archetype_id": "C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE", "fine_archetype_id": "ADTECH_MEDIA_BUYING_PLATFORM_ROAS_BUDGET_OPERATING_LEVERAGE_BRIDGE_VS_AD_THEME_FADE", "loop_objective": "coverage_gap_fill|counterexample_mining|platform_ad_revenue_operating_leverage_guardrail", "trigger_type": "Stage2-Actionable-AdTechROASBudgetOperatingLeverageBridgeWithLifecycle4B", "trigger_date": "2024-02-01", "entry_date": "2024-02-02", "entry_price": 5600.0, "evidence_available_at_that_date": "ADTECH_MEDIA_BUYING_PLATFORM_ADVERTISER_BUDGET_ROAS_REVENUE_MARGIN_BRIDGE", "evidence_source": "source_proxy_manual_verification_required:PLAYD_2024_ADTECH_MEDIA_BUYING_ADVERTISER_BUDGET_ROAS_REVENUE_MARGIN_BRIDGE", "stage2_evidence_fields": ["advertiser_budget_recovery_candidate", "ROAS_or_media_buying_efficiency_candidate", "revenue_margin_bridge_candidate"], "stage3_evidence_fields": ["relative_strength", "repeat_spend_or_platform_retention_candidate"], "stage4b_evidence_fields": ["adtech_theme_beta", "bridge_stale_or_absent", "MAE_widening", "post_peak_drawdown"], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/237/237820/2024.csv", "profile_path": "atlas/symbol_profiles/237/237820.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": 90.36, "MFE_90D_pct": 90.36, "MFE_180D_pct": 90.36, "MAE_30D_pct": -0.54, "MAE_90D_pct": -0.54, "MAE_180D_pct": -16.25, "peak_date": "2024-03-06", "peak_price": 10660.0, "drawdown_after_peak_pct": -56.0, "green_lateness_ratio": null, "four_b_local_peak_proximity": "local_4b_watch_after_adtech_peak_if_budget_ROAS_or_margin_bridge_fades", "four_b_full_window_peak_proximity": "full_4b_requires_non_price_ad_budget_loss_ROAS_deterioration_client_churn_margin_or_financing_break", "trigger_outcome_label": "positive_with_later_4b_watch", "current_profile_verdict": "C26 should allow adtech/platform positives only when advertiser budget recovery, ROAS/performance evidence, media-buying platform revenue and operating leverage bridge are visible. PlayD produced very large MFE with controlled entry-basis MAE, but the later post-peak drawdown requires lifecycle local 4B if ad-budget/ROAS/margin evidence fades.", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window_by_profile_or_post_CA_entry", "share_count_change_inside_window": false, "same_entry_group_id": "C26_ADTECH_PLATFORM_237820_2024-02-02", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 0.5, "do_not_count_as_new_case": false, "source_proxy_only": true, "evidence_url_pending": true}
{"row_type": "trigger", "trigger_id": "TRG_R8L77-C26-273060-WISEBIRDS-AD-PLATFORM-THEME-FADE", "case_id": "R8L77-C26-273060-WISEBIRDS-AD-PLATFORM-THEME-FADE", "symbol": "273060", "company_name": "와이즈버즈", "round": "R8", "loop": "77", "large_sector_id": "L8_PLATFORM_CONTENT_SW_SECURITY", "canonical_archetype_id": "C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE", "fine_archetype_id": "ADTECH_MEDIA_BUYING_PLATFORM_ROAS_BUDGET_OPERATING_LEVERAGE_BRIDGE_VS_AD_THEME_FADE", "loop_objective": "coverage_gap_fill|counterexample_mining|platform_ad_revenue_operating_leverage_guardrail", "trigger_type": "Stage2-FalsePositive / AdPlatformROASBudgetThemeFade", "trigger_date": "2024-02-01", "entry_date": "2024-02-02", "entry_price": 1407.0, "evidence_available_at_that_date": "AD_PLATFORM_AI_AD_TECH_THEME_WITH_WEAK_ADVERTISER_BUDGET_ROAS_MARGIN_BRIDGE", "evidence_source": "source_proxy_manual_verification_required:WISEBIRDS_2024_AD_PLATFORM_AI_AD_TECH_ADVERTISER_BUDGET_ROAS_MARGIN_BRIDGE", "stage2_evidence_fields": ["advertiser_budget_recovery_candidate", "ROAS_or_media_buying_efficiency_candidate", "revenue_margin_bridge_candidate"], "stage3_evidence_fields": ["relative_strength", "repeat_spend_or_platform_retention_candidate"], "stage4b_evidence_fields": ["adtech_theme_beta", "bridge_stale_or_absent", "MAE_widening", "post_peak_drawdown"], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/273/273060/2024.csv", "profile_path": "atlas/symbol_profiles/273/273060.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": 30.35, "MFE_90D_pct": 30.35, "MFE_180D_pct": 30.35, "MAE_30D_pct": -6.11, "MAE_90D_pct": -18.41, "MAE_180D_pct": -20.54, "peak_date": "2024-03-06", "peak_price": 1834.0, "drawdown_after_peak_pct": -39.04, "green_lateness_ratio": null, "four_b_local_peak_proximity": "local_4b_watch_after_adtech_peak_if_budget_ROAS_or_margin_bridge_fades", "four_b_full_window_peak_proximity": "full_4b_requires_non_price_ad_budget_loss_ROAS_deterioration_client_churn_margin_or_financing_break", "trigger_outcome_label": "counterexample_ad_platform_beta_local4b", "current_profile_verdict": "C26 should not treat digital-ad or AI-ad platform beta as durable Stage2 unless advertiser budget, ROAS, media buying efficiency, repeat spend and margin bridge refreshes. Wisebirds had a tradable MFE but then a deep post-peak fade, making it a local 4B-watch row rather than durable Green.", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window_by_profile_or_post_CA_entry", "share_count_change_inside_window": false, "same_entry_group_id": "C26_ADTECH_PLATFORM_273060_2024-02-02", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 0.5, "do_not_count_as_new_case": false, "source_proxy_only": true, "evidence_url_pending": true}
{"row_type": "trigger", "trigger_id": "TRG_R8L77-C26-363260-MOBIDAYS-POST-CA-ADTECH-THEME-FADE", "case_id": "R8L77-C26-363260-MOBIDAYS-POST-CA-ADTECH-THEME-FADE", "symbol": "363260", "company_name": "모비데이즈", "round": "R8", "loop": "77", "large_sector_id": "L8_PLATFORM_CONTENT_SW_SECURITY", "canonical_archetype_id": "C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE", "fine_archetype_id": "ADTECH_MEDIA_BUYING_PLATFORM_ROAS_BUDGET_OPERATING_LEVERAGE_BRIDGE_VS_AD_THEME_FADE", "loop_objective": "coverage_gap_fill|counterexample_mining|platform_ad_revenue_operating_leverage_guardrail", "trigger_type": "Stage2-FalsePositive / PostCAAdTechThemeFade", "trigger_date": "2024-05-24", "entry_date": "2024-05-27", "entry_price": 2885.0, "evidence_available_at_that_date": "MOBILE_ADTECH_THEME_POST_CA_WITH_WEAK_ADVERTISER_BUDGET_ROAS_REVENUE_MARGIN_BRIDGE", "evidence_source": "source_proxy_manual_verification_required:MOBIDAYS_2024_POST_CA_ADTECH_ADVERTISER_BUDGET_ROAS_PLATFORM_REVENUE_MARGIN_BRIDGE", "stage2_evidence_fields": ["advertiser_budget_recovery_candidate", "ROAS_or_media_buying_efficiency_candidate", "revenue_margin_bridge_candidate"], "stage3_evidence_fields": ["relative_strength", "repeat_spend_or_platform_retention_candidate"], "stage4b_evidence_fields": ["adtech_theme_beta", "bridge_stale_or_absent", "MAE_widening", "post_peak_drawdown"], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/363/363260/2024.csv", "profile_path": "atlas/symbol_profiles/363/363260.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": 10.92, "MFE_90D_pct": 10.92, "MFE_180D_pct": 10.92, "MAE_30D_pct": -25.48, "MAE_90D_pct": -43.74, "MAE_180D_pct": -48.84, "peak_date": "2024-05-29", "peak_price": 3200.0, "drawdown_after_peak_pct": -53.88, "green_lateness_ratio": null, "four_b_local_peak_proximity": "local_4b_watch_after_adtech_peak_if_budget_ROAS_or_margin_bridge_fades", "four_b_full_window_peak_proximity": "full_4b_requires_non_price_ad_budget_loss_ROAS_deterioration_client_churn_margin_or_financing_break", "trigger_outcome_label": "counterexample_post_ca_adtech_theme_local4b", "current_profile_verdict": "C26 should not treat post-corporate-action adtech theme spikes as durable Stage2 unless advertiser budget, campaign ROAS, platform revenue retention and operating leverage bridge are verified. Mobidays was measured only after the 2024-05-24 corporate-action candidate; the post-entry path showed weak MFE and high MAE, so it is a post-CA local 4B boundary.", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window_by_profile_or_post_CA_entry", "share_count_change_inside_window": false, "same_entry_group_id": "C26_ADTECH_PLATFORM_363260_2024-05-27", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 0.5, "do_not_count_as_new_case": false, "source_proxy_only": true, "evidence_url_pending": true}
```

### score simulation rows

```jsonl
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R8L77-C26-237820-PLAYD-ADTECH-ROAS-BUDGET-OPERATING-LEVERAGE", "trigger_id": "TRG_R8L77-C26-237820-PLAYD-ADTECH-ROAS-BUDGET-OPERATING-LEVERAGE", "symbol": "237820", "large_sector_id": "L8_PLATFORM_CONTENT_SW_SECURITY", "canonical_archetype_id": "C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE", "raw_component_scores_before": {"platform_ad_revenue_score": 14, "advertiser_budget_score": 13, "ROAS_efficiency_score": 13, "repeat_spend_retention_score": 12, "operating_leverage_score": 13, "relative_strength_score": 14, "execution_risk_score": 8, "post_CA_validation_risk": 0, "source_confidence_score": 2}, "weighted_score_before": 80, "stage_label_before": "Stage2 candidate after source repair", "raw_component_scores_after": {"platform_ad_revenue_score": 16, "advertiser_budget_score": 15, "ROAS_efficiency_score": 15, "repeat_spend_retention_score": 14, "operating_leverage_score": 15, "relative_strength_score": 13, "execution_risk_score": 9, "post_CA_validation_risk": 0, "source_confidence_score": 2}, "weighted_score_after": 86, "stage_label_after": "Stage2/Yellow-Green after source repair + lifecycle 4B", "changed_components": ["advertiser_budget_score", "ROAS_efficiency_score", "repeat_spend_retention_score", "operating_leverage_score", "execution_risk_score"], "component_delta_explanation": "Reward only verified advertiser budget recovery, ROAS/media-buying efficiency, repeat spend, platform revenue retention and operating leverage; cap adtech theme beta when evidence fails to refresh.", "MFE_90D_pct": 90.36, "MAE_90D_pct": -0.54, "score_return_alignment_label": "adtech_operating_leverage_positive_with_lifecycle_4b", "current_profile_verdict": "C26 should allow adtech/platform positives only when advertiser budget recovery, ROAS/performance evidence, media-buying platform revenue and operating leverage bridge are visible. PlayD produced very large MFE with controlled entry-basis MAE, but the later post-peak drawdown requires lifecycle local 4B if ad-budget/ROAS/margin evidence fades."}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R8L77-C26-273060-WISEBIRDS-AD-PLATFORM-THEME-FADE", "trigger_id": "TRG_R8L77-C26-273060-WISEBIRDS-AD-PLATFORM-THEME-FADE", "symbol": "273060", "large_sector_id": "L8_PLATFORM_CONTENT_SW_SECURITY", "canonical_archetype_id": "C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE", "raw_component_scores_before": {"platform_ad_revenue_score": 5, "advertiser_budget_score": 3, "ROAS_efficiency_score": 2, "repeat_spend_retention_score": 2, "operating_leverage_score": 2, "relative_strength_score": 5, "execution_risk_score": 21, "post_CA_validation_risk": 0, "source_confidence_score": 2}, "weighted_score_before": 47, "stage_label_before": "Stage2-FalsePositive / local 4B-watch", "raw_component_scores_after": {"platform_ad_revenue_score": 3, "advertiser_budget_score": 1, "ROAS_efficiency_score": 1, "repeat_spend_retention_score": 1, "operating_leverage_score": 1, "relative_strength_score": 3, "execution_risk_score": 23, "post_CA_validation_risk": 0, "source_confidence_score": 2}, "weighted_score_after": 35, "stage_label_after": "Stage4B-local-watch / no durable Green", "changed_components": ["advertiser_budget_score", "ROAS_efficiency_score", "repeat_spend_retention_score", "operating_leverage_score", "execution_risk_score"], "component_delta_explanation": "Reward only verified advertiser budget recovery, ROAS/media-buying efficiency, repeat spend, platform revenue retention and operating leverage; cap adtech theme beta when evidence fails to refresh.", "MFE_90D_pct": 30.35, "MAE_90D_pct": -18.41, "score_return_alignment_label": "false_positive_adtech_theme_bridge_gap", "current_profile_verdict": "C26 should not treat digital-ad or AI-ad platform beta as durable Stage2 unless advertiser budget, ROAS, media buying efficiency, repeat spend and margin bridge refreshes. Wisebirds had a tradable MFE but then a deep post-peak fade, making it a local 4B-watch row rather than durable Green."}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R8L77-C26-363260-MOBIDAYS-POST-CA-ADTECH-THEME-FADE", "trigger_id": "TRG_R8L77-C26-363260-MOBIDAYS-POST-CA-ADTECH-THEME-FADE", "symbol": "363260", "large_sector_id": "L8_PLATFORM_CONTENT_SW_SECURITY", "canonical_archetype_id": "C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE", "raw_component_scores_before": {"platform_ad_revenue_score": 5, "advertiser_budget_score": 3, "ROAS_efficiency_score": 2, "repeat_spend_retention_score": 2, "operating_leverage_score": 2, "relative_strength_score": 5, "execution_risk_score": 21, "post_CA_validation_risk": 10, "source_confidence_score": 2}, "weighted_score_before": 47, "stage_label_before": "Stage2-FalsePositive / local 4B-watch", "raw_component_scores_after": {"platform_ad_revenue_score": 3, "advertiser_budget_score": 1, "ROAS_efficiency_score": 1, "repeat_spend_retention_score": 1, "operating_leverage_score": 1, "relative_strength_score": 3, "execution_risk_score": 23, "post_CA_validation_risk": 12, "source_confidence_score": 2}, "weighted_score_after": 35, "stage_label_after": "Stage4B-local-watch / no durable Green", "changed_components": ["advertiser_budget_score", "ROAS_efficiency_score", "repeat_spend_retention_score", "operating_leverage_score", "execution_risk_score"], "component_delta_explanation": "Reward only verified advertiser budget recovery, ROAS/media-buying efficiency, repeat spend, platform revenue retention and operating leverage; cap adtech theme beta when evidence fails to refresh.", "MFE_90D_pct": 10.92, "MAE_90D_pct": -43.74, "score_return_alignment_label": "false_positive_adtech_theme_bridge_gap", "current_profile_verdict": "C26 should not treat post-corporate-action adtech theme spikes as durable Stage2 unless advertiser budget, campaign ROAS, platform revenue retention and operating leverage bridge are verified. Mobidays was measured only after the 2024-05-24 corporate-action candidate; the post-entry path showed weak MFE and high MAE, so it is a post-CA local 4B boundary."}
```

### aggregate row

```jsonl
{"row_type": "aggregate", "round": "R8", "loop": 77, "large_sector_id": "L8_PLATFORM_CONTENT_SW_SECURITY", "canonical_archetype_id": "C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE", "fine_archetype_id": "ADTECH_MEDIA_BUYING_PLATFORM_ROAS_BUDGET_OPERATING_LEVERAGE_BRIDGE_VS_AD_THEME_FADE", "calibration_usable_case_count": 3, "calibration_usable_trigger_count": 3, "new_independent_case_count": 3, "reused_case_count": 0, "same_archetype_new_symbol_count": 3, "same_archetype_new_trigger_family_count": 3, "positive_case_count": 1, "counterexample_count": 2, "four_b_case_count": 3, "four_c_case_count": 0, "source_proxy_only_count": 3, "evidence_url_pending_count": 3, "share_count_change_inside_window_count": 0, "post_corporate_action_validation_count": 1, "current_profile_error_count": 2, "diversity_score_summary": "+3 C26 adtech/media-buying symbols outside top-covered SOOP/Naver/Kakao/Nasmedia/Incross set, +3 media-buying/ad-platform/post-CA-adtech trigger families, +1 adtech operating-leverage MFE candidate, +2 adtech theme local-4B counterexamples, no hard duplicate", "residual_contribution_label": "coverage_gap_fill_with_source_repair_and_post_CA_validation_needed"}
```

### shadow weight row

```jsonl
{"row_type": "shadow_weight", "round": "R8", "loop": 77, "large_sector_id": "L8_PLATFORM_CONTENT_SW_SECURITY", "canonical_archetype_id": "C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE", "axis": "adtech_media_buying_platform_ROAS_budget_operating_leverage_bridge_vs_ad_theme_fade", "decision": "hold_for_source_repair_and_more_evidence", "proposed_runtime_effect": "C26 should split verified platform ad-revenue operating leverage from generic adtech or AI-ad theme beta. Stage2 requires advertiser budget recovery, ROAS/media-buying efficiency, repeat spend/client retention, platform revenue and margin/operating leverage bridge. If MFE fades and MAE/post-peak drawdown opens without bridge refresh, route to local 4B-watch. Post-CA entries require validation before runtime promotion.", "do_not_propose_new_weight_delta": true, "needs_more_evidence": true, "source_repair_required": ["237820", "273060", "363260"], "post_corporate_action_validation_required": ["363260"]}
```

### residual contribution row

```jsonl
{"row_type": "residual_contribution", "round": "R8", "loop": 77, "large_sector_id": "L8_PLATFORM_CONTENT_SW_SECURITY", "canonical_archetype_id": "C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE", "existing_axis_strengthened": ["stage2_required_bridge", "price_only_blowoff_blocks_positive_stage", "local_4b_watch_guard", "full_4b_requires_non_price_evidence", "corporate_action_validation_guard"], "new_axis_proposed": null, "sector_specific_rule_candidate": true, "canonical_archetype_rule_candidate": true, "narrative_summary": "C26 needs advertiser-budget, ROAS and operating-leverage proof. PlayD shows an adtech/media-buying MFE candidate after source repair; Wisebirds and Mobidays show ad-platform theme beta fading into local 4B when budget, ROAS, retention and margin bridge are absent."}
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
237820:
  corporate_action_candidate_dates = none
  selected window = 2024-02-02~D+180
  contamination = false

273060:
  name = 와이즈버즈 from 2020-08-05, NH SPAC 12 before that
  corporate_action_candidate_dates = 2020-08-05
  selected window = 2024-02-02~D+180
  contamination = false

363260:
  name = 모비데이즈 from 2022-06-08, 하나금융17호스팩 before that
  corporate_action_candidate_dates = 2022-06-08, 2024-05-24
  selected window starts 2024-05-27 after the 2024-05-24 candidate
  contamination = false after post-CA entry, but coding-agent validation required
```

Data-quality caveat:

```text
All selected C26 rows are source_proxy_only / evidence_url_pending.
363260 also requires post-corporate-action validation before runtime promotion.
This MD is useful for stock-web path calibration and C26 rule-shape discovery,
but coding-agent promotion requires non-proxy advertiser budget, ROAS, repeat spend/client retention, platform revenue and operating leverage evidence.
```

---

## Deferred Coding Agent Handoff Prompt

Do not execute this now.

```text
You are the coding agent for Songdaiki/stock_agent.

Read this standalone v12 residual research MD and ingest machine-readable rows only after validation.

Do not patch production scoring blindly.
This R8/C26 artifact is marked do_not_propose_new_weight_delta=true because all rows need source repair and 363260 needs post-CA validation.

Candidate axis:
adtech_media_buying_platform_ROAS_budget_operating_leverage_bridge_vs_ad_theme_fade

Required checks before implementation:
1. Validate all trigger rows against stock-web tradable_raw OHLC shards.
2. Confirm no hard duplicate key:
   canonical_archetype_id + symbol + trigger_type + entry_date.
3. Verify non-proxy source URLs for 237820, 273060 and 363260.
4. Validate 363260 post-CA continuity after the 2024-05-24 corporate-action candidate.
5. Keep generic C26 platform/ad weight unchanged until source repair is complete.
6. Consider Stage2 only when:
   - advertiser budget recovery is explicit,
   - ROAS or media-buying efficiency is visible,
   - repeat spend, client retention or platform revenue retention exists,
   - margin / operating leverage bridge is credible,
   - MAE remains controlled or the signal is lifecycle-managed.
7. Consider local 4B-watch when:
   - the trigger is adtech/platform theme beta only,
   - budget/ROAS/revenue/margin evidence is weak or stale,
   - MAE_90D <= -20% or MAE_180D <= -25%,
   - post-peak drawdown <= -35%.
8. Do not convert local 4B-watch into full 4B/4C without non-price advertiser-budget loss, ROAS deterioration, client churn, platform revenue contraction, financing or margin break.
9. Emit before/after diagnostics and reject if verified adtech operating-leverage positives are overblocked.
```

---

## Final round state

```text
completed_round = R8
completed_loop = 77
next_round = R9
next_loop = 77
round_schedule_status = valid
round_sector_consistency = pass
```

