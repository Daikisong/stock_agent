# E2R Stock-Web v12 Residual Research — R8 Loop 81 / L8 / C26

## Metadata

```json
{
  "research_session": "post_calibrated_sector_archetype_residual_research",
  "mode": "historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12",
  "scheduled_round": "R8",
  "scheduled_loop": 81,
  "round_schedule_status": "valid",
  "round_sector_consistency": "pass",
  "completed_round": "R8",
  "completed_loop": 81,
  "computed_next_round": "R9",
  "computed_next_loop": 81,
  "large_sector_id": "L8_PLATFORM_CONTENT_SW_SECURITY",
  "canonical_archetype_id": "C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE",
  "fine_archetype_id": "PERFORMANCE_AD_REWARD_AD_AGENCY_REVENUE_MARGIN_BRIDGE_VS_ADTECH_THEME_FADE",
  "loop_objective": [
    "coverage_gap_fill",
    "counterexample_mining",
    "4B_non_price_requirement_stress_test",
    "platform_ad_revenue_operating_leverage_guardrail",
    "performance_ad_reward_ad_agency_revenue_margin_bridge",
    "adtech_theme_fade_boundary",
    "bounded_ad_agency_no_forced4B_guard",
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

Previous completed state in this interactive run: R7 / loop 81.

Therefore:

```text
scheduled_round = R8
scheduled_loop = 81
allowed_large_sector = L8_PLATFORM_CONTENT_SW_SECURITY
selected_large_sector = L8_PLATFORM_CONTENT_SW_SECURITY
selected_canonical_archetype_id = C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE
computed_next_round = R9
computed_next_loop = 81
```

R8 was routed to C26 because loop 80 R8 used C27 and loop 79 R8 used C28.  
This file tests platform/adtech revenue operating leverage instead of game/content IP monetization or software/security retention.

## No-Repeat / novelty check

No hard duplicate is intentionally reused.

Hard duplicate key checked conceptually:

```text
canonical_archetype_id + symbol + trigger_type + entry_date
```

No-Repeat shows C26 concentration in:

```text
067160, 035420, 035720, 089600, 216050
```

This run uses three different symbols:

```text
237820 / 플레이디 / performance-ad AI marketing revenue lifecycle
236810 / 엔비티 / reward-ad platform theme fade
030000 / 제일기획 / bounded large ad-agency RiskWatch / no forced 4B
```

Data-quality note:

```text
All three rows are stock-web calibration usable by profile-level corporate-action candidates.
All three rows are source_proxy_only=true / evidence_url_pending=true.
No selected row has a profile-level 2024 corporate-action candidate inside the selected 180D window.
```

## Research thesis

C26 is not “AI 광고 / 플랫폼 광고가 올랐다.”

The mechanism must pass through:

```text
platform / adtech / ad-agency attention
→ advertiser or client budget
→ user, retention or conversion metrics
→ recurring ad spend and revenue conversion
→ operating leverage and margin bridge
→ durable rerating
```

광고 플랫폼은 전광판의 불빛이 아니다.  
C26이 보려는 것은 그 불빛이 실제 광고주 예산, 전환율, 반복 집행, 매출, 마진으로 전류를 보내는지다.

---

## Case 1 — Performance-ad lifecycle candidate: 237820 / 플레이디

### Evidence status

```text
source_proxy_only = true
evidence_url_pending = true
source_repair_required = true
```

The source-repair task is performance-ad / AI marketing client budget, conversion metrics, recurring advertiser spend, revenue conversion and margin bridge evidence.

```text
evidence_family = PERFORMANCE_AD_DIGITAL_MARKETING_AI_AD_TECH_CLIENT_BUDGET_REVENUE_MARGIN_BRIDGE
case_role = positive_performance_ad_revenue_leverage_with_later_4b_watch
trigger_date = 2024-01-31
entry_date = 2024-02-01
entry_price = 5,340
```

### Stock-Web price path

Observed rows from `atlas/ohlcv_tradable_by_symbol_year/237/237820/2024.csv`:

```text
2024-02-01,5340,5350,5140,5250
2024-02-02,5600,6820,5570,6820
2024-02-23,6720,8000,6570,8000
2024-03-05,8310,10100,7920,10100
2024-03-06,10550,10660,9240,9800
2024-07-25,5600,7350,5480,7270
2024-08-05,6180,6310,5130,5330
2024-09-09,4730,4965,4690,4955
2024-10-24,6080,7150,5850,6640
```

### Backtest

```text
MFE_30D  = +99.63%
MAE_30D  = -3.75%
MFE_90D  = +99.63%
MAE_90D  = -3.75%
MFE_180D = +99.63%
MAE_180D = -12.17%
peak_180 = 10,660 on 2024-03-06
trough_180 = 4,690 on 2024-09-09
peak_to_later_drawdown = -56.00%
```

### Interpretation

This is a C26 performance-ad / adtech lifecycle candidate.  
The MFE was real, but it cannot become durable Green without ad-budget, conversion and margin proof.

Correct treatment:

```text
verified client budget / conversion metrics / recurring ad revenue / margin bridge → Stage2-Yellow possible
bridge stale after peak → local 4B-watch
```

---

## Case 2 — Counterexample / local 4B: 236810 / 엔비티

### Evidence status

```text
source_proxy_only = true
evidence_url_pending = true
source_repair_required = true
```

This row tests reward-ad / mobile-ad platform theme beta without enough advertiser budget, conversion and margin bridge.

```text
evidence_family = REWARD_AD_MOBILE_AD_PLATFORM_THEME_WITH_WEAK_CLIENT_BUDGET_REVENUE_MARGIN_BRIDGE
case_role = counterexample_reward_ad_platform_theme_local4b
trigger_date = 2024-01-31
entry_date = 2024-02-01
entry_price = 7,550
```

### Stock-Web price path

Observed rows from `atlas/ohlcv_tradable_by_symbol_year/236/236810/2024.csv`:

```text
2024-02-01,7550,7790,7250,7400
2024-02-05,7580,7700,6960,7100
2024-02-20,8120,9160,8120,8620
2024-03-12,7200,7370,7040,7370
2024-08-05,4460,4470,3670,4015
2024-09-09,3350,3445,3225,3440
2024-09-27,4015,4415,3905,3905
2024-10-25,3600,3660,3560,3590
```

### Backtest

```text
MFE_30D  = +21.32%
MAE_30D  = -7.81%
MFE_90D  = +21.32%
MAE_90D  = -18.15%
MFE_180D = +21.32%
MAE_180D = -57.28%
peak_180 = 9,160 on 2024-02-20
trough_180 = 3,225 on 2024-09-09
peak_to_later_drawdown = -64.79%
```

### Interpretation

This is a C26 false-positive / local-4B boundary.  
The reward-ad platform theme did not validate durable advertiser-budget and revenue-margin rerating.

Correct treatment:

```text
reward-ad / mobile-ad platform theme beta
→ no verified advertiser budget / conversion / margin bridge
→ local 4B-watch
```

---

## Case 3 — Bounded no-forced-4B boundary: 030000 / 제일기획

### Evidence status

```text
source_proxy_only = true
evidence_url_pending = true
source_repair_required = true
```

This row tests a large ad-agency recovery / value-up watch with bounded MAE but incomplete rerating bridge.

```text
evidence_family = GLOBAL_AD_AGENCY_CLIENT_BUDGET_OPERATING_LEVERAGE_MARGIN_WITH_BOUNDED_MAE_AND_WEAK_RERATING_BRIDGE
case_role = overbearish_counterexample_bounded_ad_agency_no_forced4b
trigger_date = 2024-01-31
entry_date = 2024-02-01
entry_price = 18,370
```

### Stock-Web price path

Observed rows from `atlas/ohlcv_tradable_by_symbol_year/030/030000/2024.csv`:

```text
2024-02-01,18370,18790,18320,18420
2024-02-22,18820,18840,18600,18810
2024-03-28,18620,18930,18590,18670
2024-04-02,19170,19340,19100,19170
2024-07-24,17620,17730,17450,17590
2024-08-05,17590,17590,16400,16600
2024-09-05,18510,18830,18500,18710
2024-10-31,18340,18480,18050,18440
```

### Backtest

```text
MFE_30D  = +2.50%
MAE_30D  = -1.09%
MFE_90D  = +5.28%
MAE_90D  = -2.29%
MFE_180D = +5.28%
MAE_180D = -10.72%
peak_180 = 19,340 on 2024-04-02
trough_180 = 16,400 on 2024-08-05
peak_to_later_drawdown = -15.20%
```

### Interpretation

This is not durable Stage2, but it is also not forced local 4B.  
The path is too bounded for a price-only bearish escalation.

Correct treatment:

```text
large ad-agency revenue/margin watch
bounded MAE
→ no durable Stage2 without client-budget / operating-leverage / margin bridge
→ no forced 4B without non-price deterioration
```

---

## Cross-case residual finding

### What this strengthens

```text
stage2_required_bridge = strengthen
platform_ad_revenue_bridge_required = strengthen
price_only_blowoff_blocks_positive_stage = strengthen
local_4b_watch_guard = strengthen
bounded_MAE_no_forced_4B_guard = strengthen
full_4b_requires_non_price_evidence = keep
```

### What this does not justify

```text
do_not_raise_generic_C26_AI_ad_platform_weight = true
do_not_treat_all_adtech_MFE_as_Green = true
do_not_force_4B_on_bounded_large_ad_agency_rows = true
do_not_convert_adtech_drawdown_to_hard_4C_without_non_price_client_budget_platform_churn_or_margin_break = true
```

### Candidate canonical compression

Fine labels can compress into:

```text
PERFORMANCE_AD_REWARD_AD_AGENCY_REVENUE_MARGIN_BRIDGE_VS_ADTECH_THEME_FADE
```

This fine archetype covers:

```text
1. performance-ad / AI marketing client-budget bridge → Stage2-Yellow possible after source repair
2. reward-ad platform beta without ad-budget and margin bridge → false Stage2 / local 4B
3. bounded large ad-agency recovery watch → RiskWatch / no durable Stage2 / no forced 4B
```

---

## Machine-readable rows

### price source validation row

```jsonl
{"row_type": "price_source_validation", "source": "Songdaiki/stock-web", "source_url": "https://github.com/Songdaiki/stock-web", "manifest_path": "atlas/manifest.json", "schema_path": "atlas/schema.json", "universe_path": "atlas/universe/all_symbols.csv", "manifest_max_date": "2026-02-20", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "raw_shard_root": "atlas/ohlcv_raw_by_symbol_year", "validation_status": "usable_for_historical_calibration"}
```

### case rows

```jsonl
{"row_type": "case", "case_id": "R8L81-C26-237820-PLAYD-PERFORMANCE-AD-AI-MARKETING-LIFECYCLE", "symbol": "237820", "company_name": "플레이디", "round": "R8", "loop": "81", "large_sector_id": "L8_PLATFORM_CONTENT_SW_SECURITY", "canonical_archetype_id": "C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE", "fine_archetype_id": "PERFORMANCE_AD_REWARD_AD_AGENCY_REVENUE_MARGIN_BRIDGE_VS_ADTECH_THEME_FADE", "case_type": "platform_ad_revenue_operating_leverage", "positive_or_counterexample": "positive", "best_trigger": "Stage2-Lifecycle-PerformanceAdAIMarketingRevenueMarginBridgeWithLocal4B", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 0.5, "score_price_alignment": "C26 should allow adtech/performance-marketing positives only when AI/digital ad attention maps to client budget, conversion metrics, recurring advertiser spend, revenue conversion and margin bridge. PlayD produced a very large MFE but later post-peak drawdown demands lifecycle 4B if the bridge fades.", "current_profile_verdict": "source_repair_required_before_runtime_weight", "price_source": "Songdaiki/stock-web", "notes": "Stock-web path usable; non-proxy advertiser/client budget, ad spend recovery, user/conversion metrics, recurring ad revenue, operating leverage and margin bridge evidence required before runtime promotion."}
{"row_type": "case", "case_id": "R8L81-C26-236810-NBT-REWARD-AD-PLATFORM-THEME-FADE", "symbol": "236810", "company_name": "엔비티", "round": "R8", "loop": "81", "large_sector_id": "L8_PLATFORM_CONTENT_SW_SECURITY", "canonical_archetype_id": "C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE", "fine_archetype_id": "PERFORMANCE_AD_REWARD_AD_AGENCY_REVENUE_MARGIN_BRIDGE_VS_ADTECH_THEME_FADE", "case_type": "platform_ad_revenue_operating_leverage", "positive_or_counterexample": "counterexample", "best_trigger": "Stage2-FalsePositive / RewardAdPlatformThemeFadeWithLocal4BWatch", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 0.5, "score_price_alignment": "C26 should not treat reward-ad or mobile-ad platform theme beta as durable Stage2 unless advertiser budget, DAU/MAU or conversion metrics, retention, revenue conversion and margin bridge are visible. NBT had a small/medium MFE and then a severe high-MAE fade.", "current_profile_verdict": "source_repair_required_before_runtime_weight", "price_source": "Songdaiki/stock-web", "notes": "Stock-web path usable; non-proxy advertiser/client budget, ad spend recovery, user/conversion metrics, recurring ad revenue, operating leverage and margin bridge evidence required before runtime promotion."}
{"row_type": "case", "case_id": "R8L81-C26-030000-CHEIL-WORLDWIDE-AD-AGENCY-BOUNDED-RISKWATCH", "symbol": "030000", "company_name": "제일기획", "round": "R8", "loop": "81", "large_sector_id": "L8_PLATFORM_CONTENT_SW_SECURITY", "canonical_archetype_id": "C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE", "fine_archetype_id": "PERFORMANCE_AD_REWARD_AD_AGENCY_REVENUE_MARGIN_BRIDGE_VS_ADTECH_THEME_FADE", "case_type": "platform_ad_revenue_operating_leverage", "positive_or_counterexample": "overbearish_counterexample", "best_trigger": "RiskWatch-BoundedAdAgencyRevenueMarginNoDurableStage2NoForced4B", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 0.5, "score_price_alignment": "C26 should not force stable large ad-agency rows into 4B when MAE is bounded and no client-budget or margin break is confirmed, but it also should not call durable Stage2 without verified ad spend recovery, client budget, operating leverage and margin bridge.", "current_profile_verdict": "source_repair_required_before_runtime_weight", "price_source": "Songdaiki/stock-web", "notes": "Stock-web path usable; non-proxy advertiser/client budget, ad spend recovery, user/conversion metrics, recurring ad revenue, operating leverage and margin bridge evidence required before runtime promotion."}
```

### trigger rows

```jsonl
{"row_type": "trigger", "trigger_id": "TRG_R8L81-C26-237820-PLAYD-PERFORMANCE-AD-AI-MARKETING-LIFECYCLE", "case_id": "R8L81-C26-237820-PLAYD-PERFORMANCE-AD-AI-MARKETING-LIFECYCLE", "symbol": "237820", "company_name": "플레이디", "round": "R8", "loop": "81", "large_sector_id": "L8_PLATFORM_CONTENT_SW_SECURITY", "canonical_archetype_id": "C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE", "fine_archetype_id": "PERFORMANCE_AD_REWARD_AD_AGENCY_REVENUE_MARGIN_BRIDGE_VS_ADTECH_THEME_FADE", "loop_objective": "coverage_gap_fill|counterexample_mining|platform_ad_revenue_operating_leverage_guardrail", "trigger_type": "Stage2-Lifecycle-PerformanceAdAIMarketingRevenueMarginBridgeWithLocal4B", "trigger_date": "2024-01-31", "entry_date": "2024-02-01", "entry_price": 5340.0, "evidence_available_at_that_date": "PERFORMANCE_AD_DIGITAL_MARKETING_AI_AD_TECH_CLIENT_BUDGET_REVENUE_MARGIN_BRIDGE", "evidence_source": "source_proxy_manual_verification_required:PLAYD_2024_PERFORMANCE_AD_AI_MARKETING_CLIENT_BUDGET_REVENUE_MARGIN_BRIDGE", "stage2_evidence_fields": ["advertiser_or_client_budget_candidate", "ad_spend_or_conversion_metric_candidate", "revenue_margin_bridge_candidate"], "stage3_evidence_fields": ["relative_strength", "operating_leverage_or_recurring_ad_spend_candidate"], "stage4b_evidence_fields": ["adtech_theme_beta", "bridge_stale_or_absent", "MAE_widening", "post_peak_drawdown"], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/237/237820/2024.csv", "profile_path": "atlas/symbol_profiles/237/237820.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": 99.63, "MFE_90D_pct": 99.63, "MFE_180D_pct": 99.63, "MAE_30D_pct": -3.75, "MAE_90D_pct": -3.75, "MAE_180D_pct": -12.17, "peak_date": "2024-03-06", "peak_price": 10660.0, "drawdown_after_peak_pct": -56.0, "green_lateness_ratio": null, "four_b_local_peak_proximity": "local_4b_watch_after_adtech_peak_if_advertiser_budget_conversion_revenue_or_margin_bridge_fades", "four_b_full_window_peak_proximity": "full_4b_requires_non_price_client_budget_loss_ad_spend_contraction_platform_churn_margin_or_financing_break", "trigger_outcome_label": "positive_performance_ad_revenue_leverage_with_later_4b_watch", "current_profile_verdict": "C26 should allow adtech/performance-marketing positives only when AI/digital ad attention maps to client budget, conversion metrics, recurring advertiser spend, revenue conversion and margin bridge. PlayD produced a very large MFE but later post-peak drawdown demands lifecycle 4B if the bridge fades.", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window_by_profile", "share_count_change_inside_window": false, "same_entry_group_id": "C26_PLATFORM_AD_REVENUE_237820_2024-02-01", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 0.5, "do_not_count_as_new_case": false, "source_proxy_only": true, "evidence_url_pending": true}
{"row_type": "trigger", "trigger_id": "TRG_R8L81-C26-236810-NBT-REWARD-AD-PLATFORM-THEME-FADE", "case_id": "R8L81-C26-236810-NBT-REWARD-AD-PLATFORM-THEME-FADE", "symbol": "236810", "company_name": "엔비티", "round": "R8", "loop": "81", "large_sector_id": "L8_PLATFORM_CONTENT_SW_SECURITY", "canonical_archetype_id": "C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE", "fine_archetype_id": "PERFORMANCE_AD_REWARD_AD_AGENCY_REVENUE_MARGIN_BRIDGE_VS_ADTECH_THEME_FADE", "loop_objective": "coverage_gap_fill|counterexample_mining|platform_ad_revenue_operating_leverage_guardrail", "trigger_type": "Stage2-FalsePositive / RewardAdPlatformThemeFadeWithLocal4BWatch", "trigger_date": "2024-01-31", "entry_date": "2024-02-01", "entry_price": 7550.0, "evidence_available_at_that_date": "REWARD_AD_MOBILE_AD_PLATFORM_THEME_WITH_WEAK_CLIENT_BUDGET_REVENUE_MARGIN_BRIDGE", "evidence_source": "source_proxy_manual_verification_required:NBT_2024_REWARD_AD_PLATFORM_ADVERTISER_BUDGET_CONVERSION_REVENUE_MARGIN_BRIDGE", "stage2_evidence_fields": ["advertiser_or_client_budget_candidate", "ad_spend_or_conversion_metric_candidate", "revenue_margin_bridge_candidate"], "stage3_evidence_fields": ["relative_strength", "operating_leverage_or_recurring_ad_spend_candidate"], "stage4b_evidence_fields": ["adtech_theme_beta", "bridge_stale_or_absent", "MAE_widening", "post_peak_drawdown"], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/236/236810/2024.csv", "profile_path": "atlas/symbol_profiles/236/236810.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": 21.32, "MFE_90D_pct": 21.32, "MFE_180D_pct": 21.32, "MAE_30D_pct": -7.81, "MAE_90D_pct": -18.15, "MAE_180D_pct": -57.28, "peak_date": "2024-02-20", "peak_price": 9160.0, "drawdown_after_peak_pct": -64.79, "green_lateness_ratio": null, "four_b_local_peak_proximity": "local_4b_watch_after_adtech_peak_if_advertiser_budget_conversion_revenue_or_margin_bridge_fades", "four_b_full_window_peak_proximity": "full_4b_requires_non_price_client_budget_loss_ad_spend_contraction_platform_churn_margin_or_financing_break", "trigger_outcome_label": "counterexample_reward_ad_platform_theme_local4b", "current_profile_verdict": "C26 should not treat reward-ad or mobile-ad platform theme beta as durable Stage2 unless advertiser budget, DAU/MAU or conversion metrics, retention, revenue conversion and margin bridge are visible. NBT had a small/medium MFE and then a severe high-MAE fade.", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window_by_profile", "share_count_change_inside_window": false, "same_entry_group_id": "C26_PLATFORM_AD_REVENUE_236810_2024-02-01", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 0.5, "do_not_count_as_new_case": false, "source_proxy_only": true, "evidence_url_pending": true}
{"row_type": "trigger", "trigger_id": "TRG_R8L81-C26-030000-CHEIL-WORLDWIDE-AD-AGENCY-BOUNDED-RISKWATCH", "case_id": "R8L81-C26-030000-CHEIL-WORLDWIDE-AD-AGENCY-BOUNDED-RISKWATCH", "symbol": "030000", "company_name": "제일기획", "round": "R8", "loop": "81", "large_sector_id": "L8_PLATFORM_CONTENT_SW_SECURITY", "canonical_archetype_id": "C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE", "fine_archetype_id": "PERFORMANCE_AD_REWARD_AD_AGENCY_REVENUE_MARGIN_BRIDGE_VS_ADTECH_THEME_FADE", "loop_objective": "coverage_gap_fill|counterexample_mining|platform_ad_revenue_operating_leverage_guardrail", "trigger_type": "RiskWatch-BoundedAdAgencyRevenueMarginNoDurableStage2NoForced4B", "trigger_date": "2024-01-31", "entry_date": "2024-02-01", "entry_price": 18370.0, "evidence_available_at_that_date": "GLOBAL_AD_AGENCY_CLIENT_BUDGET_OPERATING_LEVERAGE_MARGIN_WITH_BOUNDED_MAE_AND_WEAK_RERATING_BRIDGE", "evidence_source": "source_proxy_manual_verification_required:CHEIL_WORLDWIDE_2024_AD_AGENCY_CLIENT_BUDGET_OPERATING_LEVERAGE_REVENUE_MARGIN_BRIDGE", "stage2_evidence_fields": ["advertiser_or_client_budget_candidate", "ad_spend_or_conversion_metric_candidate", "revenue_margin_bridge_candidate"], "stage3_evidence_fields": ["relative_strength", "operating_leverage_or_recurring_ad_spend_candidate"], "stage4b_evidence_fields": ["adtech_theme_beta", "bridge_stale_or_absent", "MAE_widening", "post_peak_drawdown"], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/030/030000/2024.csv", "profile_path": "atlas/symbol_profiles/030/030000.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": 2.5, "MFE_90D_pct": 5.28, "MFE_180D_pct": 5.28, "MAE_30D_pct": -1.09, "MAE_90D_pct": -2.29, "MAE_180D_pct": -10.72, "peak_date": "2024-04-02", "peak_price": 19340.0, "drawdown_after_peak_pct": -15.2, "green_lateness_ratio": null, "four_b_local_peak_proximity": "local_4b_watch_after_adtech_peak_if_advertiser_budget_conversion_revenue_or_margin_bridge_fades", "four_b_full_window_peak_proximity": "full_4b_requires_non_price_client_budget_loss_ad_spend_contraction_platform_churn_margin_or_financing_break", "trigger_outcome_label": "overbearish_counterexample_bounded_ad_agency_no_forced4b", "current_profile_verdict": "C26 should not force stable large ad-agency rows into 4B when MAE is bounded and no client-budget or margin break is confirmed, but it also should not call durable Stage2 without verified ad spend recovery, client budget, operating leverage and margin bridge.", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window_by_profile", "share_count_change_inside_window": false, "same_entry_group_id": "C26_PLATFORM_AD_REVENUE_030000_2024-02-01", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 0.5, "do_not_count_as_new_case": false, "source_proxy_only": true, "evidence_url_pending": true}
```

### score simulation rows

```jsonl
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R8L81-C26-237820-PLAYD-PERFORMANCE-AD-AI-MARKETING-LIFECYCLE", "trigger_id": "TRG_R8L81-C26-237820-PLAYD-PERFORMANCE-AD-AI-MARKETING-LIFECYCLE", "symbol": "237820", "large_sector_id": "L8_PLATFORM_CONTENT_SW_SECURITY", "canonical_archetype_id": "C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE", "raw_component_scores_before": {"advertiser_budget_score": 14, "user_conversion_metric_score": 13, "ad_revenue_score": 13, "operating_leverage_score": 12, "margin_bridge_score": 13, "relative_strength_score": 12, "execution_risk_score": 11, "source_confidence_score": 2}, "weighted_score_before": 76, "stage_label_before": "Stage2/Yellow candidate after source repair", "raw_component_scores_after": {"advertiser_budget_score": 16, "user_conversion_metric_score": 15, "ad_revenue_score": 15, "operating_leverage_score": 14, "margin_bridge_score": 15, "relative_strength_score": 11, "execution_risk_score": 12, "source_confidence_score": 2}, "weighted_score_after": 82, "stage_label_after": "Stage2/Yellow after source repair + lifecycle 4B", "changed_components": ["advertiser_budget_score", "user_conversion_metric_score", "ad_revenue_score", "operating_leverage_score", "margin_bridge_score", "execution_risk_score"], "component_delta_explanation": "Reward only verified advertiser/client budget, conversion metrics, recurring ad revenue, operating leverage and margin bridge; cap adtech theme beta when bridge fails to refresh while protecting bounded ad-agency rows from forced 4B.", "MFE_90D_pct": 99.63, "MAE_90D_pct": -3.75, "score_return_alignment_label": "platform_ad_revenue_positive_with_lifecycle_4b", "current_profile_verdict": "C26 should allow adtech/performance-marketing positives only when AI/digital ad attention maps to client budget, conversion metrics, recurring advertiser spend, revenue conversion and margin bridge. PlayD produced a very large MFE but later post-peak drawdown demands lifecycle 4B if the bridge fades."}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R8L81-C26-236810-NBT-REWARD-AD-PLATFORM-THEME-FADE", "trigger_id": "TRG_R8L81-C26-236810-NBT-REWARD-AD-PLATFORM-THEME-FADE", "symbol": "236810", "large_sector_id": "L8_PLATFORM_CONTENT_SW_SECURITY", "canonical_archetype_id": "C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE", "raw_component_scores_before": {"advertiser_budget_score": 4, "user_conversion_metric_score": 3, "ad_revenue_score": 2, "operating_leverage_score": 2, "margin_bridge_score": 1, "relative_strength_score": 3, "execution_risk_score": 24, "source_confidence_score": 2}, "weighted_score_before": 42, "stage_label_before": "Stage2-FalsePositive / local 4B-watch", "raw_component_scores_after": {"advertiser_budget_score": 3, "user_conversion_metric_score": 1, "ad_revenue_score": 1, "operating_leverage_score": 1, "margin_bridge_score": 1, "relative_strength_score": 3, "execution_risk_score": 26, "source_confidence_score": 2}, "weighted_score_after": 31, "stage_label_after": "Stage4B-local-watch / no durable Green", "changed_components": ["advertiser_budget_score", "user_conversion_metric_score", "ad_revenue_score", "operating_leverage_score", "margin_bridge_score", "execution_risk_score"], "component_delta_explanation": "Reward only verified advertiser/client budget, conversion metrics, recurring ad revenue, operating leverage and margin bridge; cap adtech theme beta when bridge fails to refresh while protecting bounded ad-agency rows from forced 4B.", "MFE_90D_pct": 21.32, "MAE_90D_pct": -18.15, "score_return_alignment_label": "false_positive_adtech_bridge_gap", "current_profile_verdict": "C26 should not treat reward-ad or mobile-ad platform theme beta as durable Stage2 unless advertiser budget, DAU/MAU or conversion metrics, retention, revenue conversion and margin bridge are visible. NBT had a small/medium MFE and then a severe high-MAE fade."}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R8L81-C26-030000-CHEIL-WORLDWIDE-AD-AGENCY-BOUNDED-RISKWATCH", "trigger_id": "TRG_R8L81-C26-030000-CHEIL-WORLDWIDE-AD-AGENCY-BOUNDED-RISKWATCH", "symbol": "030000", "large_sector_id": "L8_PLATFORM_CONTENT_SW_SECURITY", "canonical_archetype_id": "C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE", "raw_component_scores_before": {"advertiser_budget_score": 7, "user_conversion_metric_score": 6, "ad_revenue_score": 5, "operating_leverage_score": 5, "margin_bridge_score": 4, "relative_strength_score": 3, "execution_risk_score": 8, "source_confidence_score": 2}, "weighted_score_before": 58, "stage_label_before": "RiskWatch / no forced 4B", "raw_component_scores_after": {"advertiser_budget_score": 6, "user_conversion_metric_score": 5, "ad_revenue_score": 4, "operating_leverage_score": 4, "margin_bridge_score": 3, "relative_strength_score": 3, "execution_risk_score": 7, "source_confidence_score": 2}, "weighted_score_after": 60, "stage_label_after": "RiskWatch / no durable Stage2 and no forced 4B", "changed_components": ["advertiser_budget_score", "user_conversion_metric_score", "ad_revenue_score", "operating_leverage_score", "margin_bridge_score", "execution_risk_score"], "component_delta_explanation": "Reward only verified advertiser/client budget, conversion metrics, recurring ad revenue, operating leverage and margin bridge; cap adtech theme beta when bridge fails to refresh while protecting bounded ad-agency rows from forced 4B.", "MFE_90D_pct": 5.28, "MAE_90D_pct": -2.29, "score_return_alignment_label": "bounded_ad_agency_no_forced4b", "current_profile_verdict": "C26 should not force stable large ad-agency rows into 4B when MAE is bounded and no client-budget or margin break is confirmed, but it also should not call durable Stage2 without verified ad spend recovery, client budget, operating leverage and margin bridge."}
```

### aggregate row

```jsonl
{"row_type": "aggregate", "round": "R8", "loop": 81, "large_sector_id": "L8_PLATFORM_CONTENT_SW_SECURITY", "canonical_archetype_id": "C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE", "fine_archetype_id": "PERFORMANCE_AD_REWARD_AD_AGENCY_REVENUE_MARGIN_BRIDGE_VS_ADTECH_THEME_FADE", "calibration_usable_case_count": 3, "calibration_usable_trigger_count": 3, "new_independent_case_count": 3, "reused_case_count": 0, "same_archetype_new_symbol_count": 3, "same_archetype_new_trigger_family_count": 3, "positive_case_count": 1, "counterexample_count": 1, "overbearish_counterexample_count": 1, "four_b_case_count": 2, "four_c_case_count": 0, "source_proxy_only_count": 3, "evidence_url_pending_count": 3, "share_count_change_inside_window_count": 0, "current_profile_error_count": 1, "diversity_score_summary": "+3 C26 ad/platform symbols outside top-covered 067160/035420/035720/089600/216050 set, +3 performance-ad/reward-ad/large-ad-agency trigger families, +1 adtech lifecycle positive, +1 reward-ad local-4B counterexample, +1 bounded ad-agency no-forced-4B boundary, no hard duplicate", "residual_contribution_label": "coverage_gap_fill_with_source_repair_needed"}
```

### shadow weight row

```jsonl
{"row_type": "shadow_weight", "round": "R8", "loop": 81, "large_sector_id": "L8_PLATFORM_CONTENT_SW_SECURITY", "canonical_archetype_id": "C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE", "axis": "performance_ad_reward_ad_agency_revenue_margin_bridge_vs_adtech_theme_fade", "decision": "hold_for_source_repair_and_more_evidence", "proposed_runtime_effect": "C26 should split verified platform/adtech revenue operating leverage from generic AI advertising or ad platform theme beta. Stage2 requires advertiser/client budget, user or conversion metrics, recurring ad spend, revenue conversion, operating leverage and margin bridge. If MFE fades and MAE/post-peak drawdown opens without bridge refresh, route to local 4B-watch. Bounded large-agency rows should remain RiskWatch/no durable Stage2, not forced 4B.", "do_not_propose_new_weight_delta": true, "needs_more_evidence": true, "source_repair_required": ["237820", "236810", "030000"]}
```

### residual contribution row

```jsonl
{"row_type": "residual_contribution", "round": "R8", "loop": 81, "large_sector_id": "L8_PLATFORM_CONTENT_SW_SECURITY", "canonical_archetype_id": "C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE", "existing_axis_strengthened": ["stage2_required_bridge", "platform_ad_revenue_bridge_required", "price_only_blowoff_blocks_positive_stage", "local_4b_watch_guard", "bounded_MAE_no_forced_4B_guard", "full_4b_requires_non_price_evidence"], "new_axis_proposed": null, "sector_specific_rule_candidate": true, "canonical_archetype_rule_candidate": true, "narrative_summary": "C26 needs adtech/platform attention to map into advertiser budget, user/conversion metrics, recurring ad spend, revenue conversion and margin proof. PlayD shows a performance-ad lifecycle candidate after source repair; NBT shows reward-ad platform theme fading into local 4B; Cheil Worldwide shows a bounded large-agency RiskWatch row where forced 4B would be too harsh."}
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
  name = 플레이디
  corporate_action_candidate_dates = none
  selected window = 2024-02-01~D+180
  contamination = false

236810:
  name = 엔비티
  corporate_action_candidate_dates = 2022-05-30, 2022-06-21
  selected window = 2024-02-01~D+180
  contamination = false

030000:
  name = 제일기획
  corporate_action_candidate_dates = 1999-02-01, 2010-05-10
  selected window = 2024-02-01~D+180
  contamination = false
```

Data-quality caveat:

```text
All selected C26 rows are source_proxy_only / evidence_url_pending.
This MD is useful for stock-web path calibration and C26 platform/ad revenue rule-shape discovery,
but coding-agent promotion requires non-proxy advertiser/client budget, ad spend recovery, user/conversion metrics, recurring ad revenue, operating leverage and margin bridge evidence.
```

---

## Deferred Coding Agent Handoff Prompt

Do not execute this now.

```text
You are the coding agent for Songdaiki/stock_agent.

Read this standalone v12 residual research MD and ingest machine-readable rows only after validation.

Do not patch production scoring blindly.
This R8/C26 artifact is marked do_not_propose_new_weight_delta=true because all rows need source repair.

Candidate axis:
performance_ad_reward_ad_agency_revenue_margin_bridge_vs_adtech_theme_fade

Required checks before implementation:
1. Validate all trigger rows against stock-web tradable_raw OHLC shards.
2. Confirm no hard duplicate key:
   canonical_archetype_id + symbol + trigger_type + entry_date.
3. Verify non-proxy source URLs for 237820, 236810 and 030000.
4. Keep generic C26 platform/ad revenue weight unchanged until source repair is complete.
5. Consider Stage2 only when:
   - advertiser or client budget is explicit,
   - user, retention or conversion metrics are visible,
   - recurring ad spend and revenue conversion exist,
   - operating leverage and margin bridge are credible,
   - MAE remains controlled or the signal is lifecycle-managed.
6. Consider local 4B-watch when:
   - the trigger is adtech/platform advertising theme beta only,
   - advertiser budget / conversion / revenue / margin evidence is weak or stale,
   - MAE_90D <= -20% or MAE_180D <= -25%,
   - post-peak drawdown <= -35%.
7. Do not force local 4B when bounded large ad-agency rows have controlled MAE and no confirmed non-price bridge break.
8. Do not convert local 4B-watch into full 4B/4C without non-price client-budget loss, ad-spend contraction, platform churn, financing or margin break.
9. Emit before/after diagnostics and reject if verified platform-ad positives or bounded ad-agency rows are overblocked.
```

---

## Final round state

```text
completed_round = R8
completed_loop = 81
next_round = R9
next_loop = 81
round_schedule_status = valid
round_sector_consistency = pass
```

