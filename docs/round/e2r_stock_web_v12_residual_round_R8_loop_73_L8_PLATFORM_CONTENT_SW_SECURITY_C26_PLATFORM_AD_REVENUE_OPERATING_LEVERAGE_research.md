# E2R Stock-Web v12 Residual Research — R8 Loop 73 / L8 / C26

## Metadata

```json
{
  "research_session": "post_calibrated_sector_archetype_residual_research",
  "mode": "historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12",
  "scheduled_round": "R8",
  "scheduled_loop": 73,
  "round_schedule_status": "valid",
  "round_sector_consistency": "pass",
  "completed_round": "R8",
  "completed_loop": 73,
  "computed_next_round": "R9",
  "computed_next_loop": 73,
  "large_sector_id": "L8_PLATFORM_CONTENT_SW_SECURITY",
  "canonical_archetype_id": "C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE",
  "fine_archetype_id": "SUBSCRIPTION_FANDOM_PLATFORM_AND_DIGITAL_AD_OPERATING_LEVERAGE_VS_PRICE_ONLY_ADTECH_BETA",
  "loop_objective": [
    "coverage_gap_fill",
    "counterexample_mining",
    "4B_non_price_requirement_stress_test",
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
```

## Round / scope resolution

Previous completed state in this interactive run: R7 / loop 73.

Therefore:

```text
scheduled_round = R8
scheduled_loop = 73
allowed_large_sector = L8_PLATFORM_CONTENT_SW_SECURITY
selected_large_sector = L8_PLATFORM_CONTENT_SW_SECURITY
selected_canonical_archetype_id = C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE
computed_next_round = R9
computed_next_loop = 73
```

R8 was routed to C26 because loop 71 already used C27 and loop 72 already used C28.  
This file tests platform/ad/subscription operating leverage rather than content IP or software security retention.

## No-Repeat / novelty check

No hard duplicate is intentionally reused.

Hard duplicate key checked conceptually:

```text
canonical_archetype_id + symbol + trigger_type + entry_date
```

No-Repeat shows C26 is concentrated in `067160`, `035420`, `035720`, `089600`, and `216050`.  
This run avoids those top-covered symbols and uses:

```text
376300 / 디어유 / subscription fandom platform operating leverage
214270 / FSN / digital adtech price-beta local 4B
214320 / 이노션 / ad-agency operating leverage riskwatch boundary
```

Data-quality note:

```text
All three rows are stock-web calibration usable.
All three rows are source_proxy_only=true / evidence_url_pending=true.
This file is a source-repair queue plus stock-web path calibration, not immediate runtime weight evidence.
```

## Research thesis

C26 is not “platform stock went up.”

The mechanism must go through recurring revenue:

```text
platform user / subscription / ad inventory / client budget
→ retention, take-rate, ARPU or campaign expansion
→ margin conversion
→ durable rerating
```

A platform is a turnstile.  
A user walking through once is traffic.  
A user paying again is leverage.

---

## Case 1 — Positive with later 4B-watch: 376300 / 디어유

### Evidence status

```text
source_proxy_only = true
evidence_url_pending = true
source_repair_required = true
```

The source-repair task is global artist expansion, paid-message/subscription user growth, ARPU and margin conversion evidence.

```text
evidence_family = FANDOM_SUBSCRIPTION_PLATFORM_USER_ARPU_GLOBAL_ARTIST_EXPANSION_OPERATING_LEVERAGE
case_role = positive_with_later_4b_watch
trigger_date = 2024-10-25
entry_date = 2024-10-28
entry_price = 24,100
```

### Stock-Web price path

Observed rows from `atlas/ohlcv_tradable_by_symbol_year/376/376300/2024.csv` and `2025.csv`:

```text
2024-10-28,24100,30700,24000,29800
2024-11-25,39000,41950,38300,39200
2025-02-20,49050,50300,45850,47700
2025-04-09,38350,38700,35350,35650
```

### Backtest

```text
MFE_30D  = +74.07%
MAE_30D  = -0.41%
MFE_90D  = +108.71%
MAE_90D  = -0.41%
MFE_180D = +108.71%
MAE_180D = -0.41%
peak_180 = 50,300 on 2025-02-20
trough_180 = 24,000 on 2024-10-28
peak_to_later_drawdown = -29.72%
```

### Interpretation

This is the strongest C26 positive path in this set.  
The price path looks like platform operating leverage: very high MFE, nearly no entry-basis MAE.

But the rule should still be lifecycle-aware:

```text
subscription/user/ARPU bridge verified → Stage2/Green possible
post-peak bridge stale → local 4B-watch
```

---

## Case 2 — Counterexample / local 4B: 214270 / FSN

### Evidence status

```text
source_proxy_only = true
evidence_url_pending = true
source_repair_required = true
```

This row tests digital-adtech/platform theme beta without recurring revenue, client retention or margin bridge.

```text
evidence_family = DIGITAL_ADTECH_PLATFORM_THEME_BETA_WITH_WEAK_RECURRING_REVENUE_AND_MARGIN_BRIDGE
case_role = counterexample
trigger_date = 2024-01-31
entry_date = 2024-02-01
entry_price = 2,830
```

### Stock-Web price path

Observed rows from `atlas/ohlcv_tradable_by_symbol_year/214/214270/2024.csv`:

```text
2024-02-01,2830,3400,2820,3245
2024-02-02,3595,3775,3185,3255
2024-08-06,1550,1750,1550,1728
2024-12-09,1710,1729,1553,1578
```

### Backtest

```text
MFE_30D  = +33.39%
MAE_30D  = -4.59%
MFE_90D  = +33.39%
MAE_90D  = -22.97%
MFE_180D = +33.39%
MAE_180D = -45.23%
peak_180 = 3,775 on 2024-02-02
trough_180 = 1,550 on 2024-08-06
peak_to_later_drawdown = -58.94%
```

### Interpretation

This is the C26 false-positive shape.  
The MFE was real, but the bridge was not.

A price-only adtech/platform beta should not become durable Stage2 unless recurring revenue, client retention, take-rate or margin conversion evidence is verified.

---

## Case 3 — RiskWatch boundary: 214320 / 이노션

### Evidence status

```text
source_proxy_only = true
evidence_url_pending = true
source_repair_required = true
```

This row tests an ad-agency operating leverage narrative without enough digital mix or client-budget revision evidence.

```text
evidence_family = GLOBAL_AD_AGENCY_AUTO_CLIENT_CAMPAIGN_OPERATING_LEVERAGE_WITH_WEAK_REVISION_BRIDGE
case_role = riskwatch_boundary_case
trigger_date = 2024-01-31
entry_date = 2024-02-01
entry_price = 21,800
```

### Stock-Web price path

Observed rows from `atlas/ohlcv_tradable_by_symbol_year/214/214320/2024.csv`:

```text
2024-02-01,21800,22150,21650,22100
2024-02-26,22100,22800,22100,22450
2024-07-22,20050,20100,19670,19710
2024-08-05,19680,19700,18200,18700
```

### Backtest

```text
MFE_30D  = +4.59%
MAE_30D  = -2.98%
MFE_90D  = +4.59%
MAE_90D  = -2.98%
MFE_180D = +4.59%
MAE_180D = -16.51%
peak_180 = 22,800 on 2024-02-26
trough_180 = 18,200 on 2024-08-05
peak_to_later_drawdown = -20.18%
```

### Interpretation

This is not hard 4B.  
It is a boundary case: campaign stability and ad-agency beta are not the same as platform operating leverage.

The correct C26 treatment is:

```text
RiskWatch / no durable Green
unless client budget, digital mix, retention and margin bridge are verified.
```

---

## Cross-case residual finding

### What this strengthens

```text
stage2_required_bridge = strengthen
price_only_blowoff_blocks_positive_stage = strengthen
local_4b_watch_guard = strengthen
```

### What this does not justify

```text
do_not_raise_generic_C26_platform_weight = true
do_not_treat_adtech_or_agency_beta_as_Green_without_recurring_revenue_bridge = true
do_not_convert_platform_drawdown_to_hard_4C_without_non_price_break = true
```

### Candidate canonical compression

Fine labels can compress into:

```text
SUBSCRIPTION_FANDOM_PLATFORM_AND_DIGITAL_AD_OPERATING_LEVERAGE_VS_PRICE_ONLY_ADTECH_BETA
```

This fine archetype covers:

```text
1. subscription/fandom platform user and ARPU expansion → Stage2 possible after source repair
2. digital adtech price beta without recurring revenue/margin bridge → false Stage2 / local 4B
3. ad-agency campaign beta without platform-like retention bridge → RiskWatch boundary
```

---

## Machine-readable rows

### price source validation row

```jsonl
{"row_type": "price_source_validation", "source": "Songdaiki/stock-web", "source_url": "https://github.com/Songdaiki/stock-web", "manifest_path": "atlas/manifest.json", "schema_path": "atlas/schema.json", "universe_path": "atlas/universe/all_symbols.csv", "manifest_max_date": "2026-02-20", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "raw_shard_root": "atlas/ohlcv_raw_by_symbol_year", "validation_status": "usable_for_historical_calibration"}
```

### case rows

```jsonl
{"row_type": "case", "case_id": "R8L73-C26-376300-DEARU-SUBSCRIPTION-PLATFORM-OPERATING-LEVERAGE", "symbol": "376300", "company_name": "디어유", "round": "R8", "loop": "73", "large_sector_id": "L8_PLATFORM_CONTENT_SW_SECURITY", "canonical_archetype_id": "C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE", "fine_archetype_id": "SUBSCRIPTION_FANDOM_PLATFORM_AND_DIGITAL_AD_OPERATING_LEVERAGE_VS_PRICE_ONLY_ADTECH_BETA", "case_type": "platform_ad_revenue_operating_leverage", "positive_or_counterexample": "positive", "best_trigger": "Stage2-Actionable-SubscriptionPlatformOperatingLeverage", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 0.5, "score_price_alignment": "C26 should allow Stage2 when a platform has subscription/user or ARPU expansion that can convert into operating leverage. DearU produced very high MFE with almost no entry-basis MAE, but later local 4B-watch is still needed if subscriber/artist expansion evidence stops refreshing after the peak.", "current_profile_verdict": "source_repair_required_before_runtime_weight", "price_source": "Songdaiki/stock-web", "notes": "Stock-web path usable; non-proxy subscription/user/ARR/ad-revenue/client-retention/margin evidence must be attached before runtime promotion."}
{"row_type": "case", "case_id": "R8L73-C26-214270-FSN-DIGITAL-ADTECH-PRICE-BETA-LOCAL4B", "symbol": "214270", "company_name": "FSN", "round": "R8", "loop": "73", "large_sector_id": "L8_PLATFORM_CONTENT_SW_SECURITY", "canonical_archetype_id": "C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE", "fine_archetype_id": "SUBSCRIPTION_FANDOM_PLATFORM_AND_DIGITAL_AD_OPERATING_LEVERAGE_VS_PRICE_ONLY_ADTECH_BETA", "case_type": "platform_ad_revenue_operating_leverage", "positive_or_counterexample": "counterexample", "best_trigger": "Stage2-FalsePositive / DigitalAdTechPriceBetaLocal4B", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 0.5, "score_price_alignment": "C26 should not treat digital-adtech or platform theme MFE as durable Stage2 unless recurring ad revenue, take-rate, client retention and margin conversion are visible. FSN had a sharp MFE but later severe MAE and post-peak drawdown.", "current_profile_verdict": "source_repair_required_before_runtime_weight", "price_source": "Songdaiki/stock-web", "notes": "Stock-web path usable; non-proxy subscription/user/ARR/ad-revenue/client-retention/margin evidence must be attached before runtime promotion."}
{"row_type": "case", "case_id": "R8L73-C26-214320-INNOCEAN-AD-AGENCY-OPERATING-LEVERAGE-WEAK", "symbol": "214320", "company_name": "이노션", "round": "R8", "loop": "73", "large_sector_id": "L8_PLATFORM_CONTENT_SW_SECURITY", "canonical_archetype_id": "C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE", "fine_archetype_id": "SUBSCRIPTION_FANDOM_PLATFORM_AND_DIGITAL_AD_OPERATING_LEVERAGE_VS_PRICE_ONLY_ADTECH_BETA", "case_type": "platform_ad_revenue_operating_leverage", "positive_or_counterexample": "riskwatch_boundary", "best_trigger": "Stage2-FalsePositive / AdAgencyOperatingLeverageWeak", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 0.5, "score_price_alignment": "C26 should distinguish ad-agency campaign stability from true platform operating leverage. Innocean had limited MFE and later MAE; without client-budget, digital mix or margin revision evidence it should remain RiskWatch / no durable Green rather than Stage2.", "current_profile_verdict": "source_repair_required_before_runtime_weight", "price_source": "Songdaiki/stock-web", "notes": "Stock-web path usable; non-proxy subscription/user/ARR/ad-revenue/client-retention/margin evidence must be attached before runtime promotion."}
```

### trigger rows

```jsonl
{"row_type": "trigger", "trigger_id": "TRG_R8L73-C26-376300-DEARU-SUBSCRIPTION-PLATFORM-OPERATING-LEVERAGE", "case_id": "R8L73-C26-376300-DEARU-SUBSCRIPTION-PLATFORM-OPERATING-LEVERAGE", "symbol": "376300", "company_name": "디어유", "round": "R8", "loop": "73", "large_sector_id": "L8_PLATFORM_CONTENT_SW_SECURITY", "canonical_archetype_id": "C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE", "fine_archetype_id": "SUBSCRIPTION_FANDOM_PLATFORM_AND_DIGITAL_AD_OPERATING_LEVERAGE_VS_PRICE_ONLY_ADTECH_BETA", "loop_objective": "coverage_gap_fill|counterexample_mining|sector_specific_rule_discovery", "trigger_type": "Stage2-Actionable-SubscriptionPlatformOperatingLeverage", "trigger_date": "2024-10-25", "entry_date": "2024-10-28", "entry_price": 24100.0, "evidence_available_at_that_date": "FANDOM_SUBSCRIPTION_PLATFORM_USER_ARPU_GLOBAL_ARTIST_EXPANSION_OPERATING_LEVERAGE", "evidence_source": "source_proxy_manual_verification_required:DEARU_2024_FANDOM_SUBSCRIPTION_PLATFORM_GLOBAL_ARTIST_USER_ARPU_OPERATING_LEVERAGE", "stage2_evidence_fields": ["platform_or_ad_revenue", "operating_leverage_candidate", "subscription_or_client_retention_candidate"], "stage3_evidence_fields": ["relative_strength", "margin_or_recurring_revenue_candidate"], "stage4b_evidence_fields": ["later_local_4b_after_platform_peak_if_bridge_stale"], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/376/376300/2024.csv", "profile_path": "atlas/symbol_profiles/376/376300.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": 74.07, "MFE_90D_pct": 108.71, "MFE_180D_pct": 108.71, "MAE_30D_pct": -0.41, "MAE_90D_pct": -0.41, "MAE_180D_pct": -0.41, "peak_date": "2025-02-20", "peak_price": 50300.0, "drawdown_after_peak_pct": -29.72, "green_lateness_ratio": null, "four_b_local_peak_proximity": "local_4b_watch_after_platform_or_ad_revenue_peak_if_bridge_fades", "four_b_full_window_peak_proximity": "full_4b_requires_non_price_recurring_revenue_or_margin_break", "trigger_outcome_label": "positive_with_later_4b_watch", "current_profile_verdict": "C26 should allow Stage2 when a platform has subscription/user or ARPU expansion that can convert into operating leverage. DearU produced very high MFE with almost no entry-basis MAE, but later local 4B-watch is still needed if subscriber/artist expansion evidence stops refreshing after the peak.", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window", "same_entry_group_id": "C26_PLATFORM_AD_376300_2024-10-28", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 0.5, "do_not_count_as_new_case": false, "source_proxy_only": true, "evidence_url_pending": true}
{"row_type": "trigger", "trigger_id": "TRG_R8L73-C26-214270-FSN-DIGITAL-ADTECH-PRICE-BETA-LOCAL4B", "case_id": "R8L73-C26-214270-FSN-DIGITAL-ADTECH-PRICE-BETA-LOCAL4B", "symbol": "214270", "company_name": "FSN", "round": "R8", "loop": "73", "large_sector_id": "L8_PLATFORM_CONTENT_SW_SECURITY", "canonical_archetype_id": "C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE", "fine_archetype_id": "SUBSCRIPTION_FANDOM_PLATFORM_AND_DIGITAL_AD_OPERATING_LEVERAGE_VS_PRICE_ONLY_ADTECH_BETA", "loop_objective": "coverage_gap_fill|counterexample_mining|sector_specific_rule_discovery", "trigger_type": "Stage2-FalsePositive / DigitalAdTechPriceBetaLocal4B", "trigger_date": "2024-01-31", "entry_date": "2024-02-01", "entry_price": 2830.0, "evidence_available_at_that_date": "DIGITAL_ADTECH_PLATFORM_THEME_BETA_WITH_WEAK_RECURRING_REVENUE_AND_MARGIN_BRIDGE", "evidence_source": "source_proxy_manual_verification_required:FSN_2024_DIGITAL_ADTECH_PLATFORM_RECURRING_REVENUE_CLIENT_RETENTION_MARGIN_BRIDGE", "stage2_evidence_fields": ["platform_or_ad_revenue", "operating_leverage_candidate", "subscription_or_client_retention_candidate"], "stage3_evidence_fields": ["relative_strength", "margin_or_recurring_revenue_candidate"], "stage4b_evidence_fields": ["bridge_stale_or_absent", "post_peak_drawdown"], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/214/214270/2024.csv", "profile_path": "atlas/symbol_profiles/214/214270.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": 33.39, "MFE_90D_pct": 33.39, "MFE_180D_pct": 33.39, "MAE_30D_pct": -4.59, "MAE_90D_pct": -22.97, "MAE_180D_pct": -45.23, "peak_date": "2024-02-02", "peak_price": 3775.0, "drawdown_after_peak_pct": -58.94, "green_lateness_ratio": null, "four_b_local_peak_proximity": "local_4b_watch_after_platform_or_ad_revenue_peak_if_bridge_fades", "four_b_full_window_peak_proximity": "full_4b_requires_non_price_recurring_revenue_or_margin_break", "trigger_outcome_label": "counterexample", "current_profile_verdict": "C26 should not treat digital-adtech or platform theme MFE as durable Stage2 unless recurring ad revenue, take-rate, client retention and margin conversion are visible. FSN had a sharp MFE but later severe MAE and post-peak drawdown.", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window", "same_entry_group_id": "C26_PLATFORM_AD_214270_2024-02-01", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 0.5, "do_not_count_as_new_case": false, "source_proxy_only": true, "evidence_url_pending": true}
{"row_type": "trigger", "trigger_id": "TRG_R8L73-C26-214320-INNOCEAN-AD-AGENCY-OPERATING-LEVERAGE-WEAK", "case_id": "R8L73-C26-214320-INNOCEAN-AD-AGENCY-OPERATING-LEVERAGE-WEAK", "symbol": "214320", "company_name": "이노션", "round": "R8", "loop": "73", "large_sector_id": "L8_PLATFORM_CONTENT_SW_SECURITY", "canonical_archetype_id": "C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE", "fine_archetype_id": "SUBSCRIPTION_FANDOM_PLATFORM_AND_DIGITAL_AD_OPERATING_LEVERAGE_VS_PRICE_ONLY_ADTECH_BETA", "loop_objective": "coverage_gap_fill|counterexample_mining|sector_specific_rule_discovery", "trigger_type": "Stage2-FalsePositive / AdAgencyOperatingLeverageWeak", "trigger_date": "2024-01-31", "entry_date": "2024-02-01", "entry_price": 21800.0, "evidence_available_at_that_date": "GLOBAL_AD_AGENCY_AUTO_CLIENT_CAMPAIGN_OPERATING_LEVERAGE_WITH_WEAK_REVISION_BRIDGE", "evidence_source": "source_proxy_manual_verification_required:INNOCEAN_2024_GLOBAL_AD_AGENCY_CLIENT_BUDGET_DIGITAL_MIX_OPERATING_LEVERAGE", "stage2_evidence_fields": ["platform_or_ad_revenue", "operating_leverage_candidate", "subscription_or_client_retention_candidate"], "stage3_evidence_fields": ["relative_strength", "margin_or_recurring_revenue_candidate"], "stage4b_evidence_fields": ["bridge_stale_or_absent", "post_peak_drawdown"], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/214/214320/2024.csv", "profile_path": "atlas/symbol_profiles/214/214320.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": 4.59, "MFE_90D_pct": 4.59, "MFE_180D_pct": 4.59, "MAE_30D_pct": -2.98, "MAE_90D_pct": -2.98, "MAE_180D_pct": -16.51, "peak_date": "2024-02-26", "peak_price": 22800.0, "drawdown_after_peak_pct": -20.18, "green_lateness_ratio": null, "four_b_local_peak_proximity": "local_4b_watch_after_platform_or_ad_revenue_peak_if_bridge_fades", "four_b_full_window_peak_proximity": "full_4b_requires_non_price_recurring_revenue_or_margin_break", "trigger_outcome_label": "riskwatch_boundary_case", "current_profile_verdict": "C26 should distinguish ad-agency campaign stability from true platform operating leverage. Innocean had limited MFE and later MAE; without client-budget, digital mix or margin revision evidence it should remain RiskWatch / no durable Green rather than Stage2.", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window", "same_entry_group_id": "C26_PLATFORM_AD_214320_2024-02-01", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 0.5, "do_not_count_as_new_case": false, "source_proxy_only": true, "evidence_url_pending": true}
```

### score simulation rows

```jsonl
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R8L73-C26-376300-DEARU-SUBSCRIPTION-PLATFORM-OPERATING-LEVERAGE", "trigger_id": "TRG_R8L73-C26-376300-DEARU-SUBSCRIPTION-PLATFORM-OPERATING-LEVERAGE", "symbol": "376300", "large_sector_id": "L8_PLATFORM_CONTENT_SW_SECURITY", "canonical_archetype_id": "C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE", "raw_component_scores_before": {"recurring_revenue_score": 15, "ad_revenue_score": 4, "subscription_user_score": 15, "client_retention_score": 4, "margin_bridge_score": 13, "relative_strength_score": 16, "valuation_repricing_score": 12, "execution_risk_score": 4, "source_confidence_score": 2}, "weighted_score_before": 84, "stage_label_before": "Stage2-Actionable after source repair", "raw_component_scores_after": {"recurring_revenue_score": 17, "ad_revenue_score": 3, "subscription_user_score": 17, "client_retention_score": 3, "margin_bridge_score": 15, "relative_strength_score": 16, "valuation_repricing_score": 11, "execution_risk_score": 4, "source_confidence_score": 2}, "weighted_score_after": 89, "stage_label_after": "Stage3-Yellow/Green candidate after source repair", "changed_components": ["recurring_revenue_score", "subscription_user_score", "margin_bridge_score", "execution_risk_score", "relative_strength_score"], "component_delta_explanation": "Reward only verified subscription/user/ad-revenue/client-retention and margin bridge; cap price-only adtech or campaign beta when bridge evidence fails to refresh.", "MFE_90D_pct": 108.71, "MAE_90D_pct": -0.41, "score_return_alignment_label": "aligned_positive_or_lifecycle_positive", "current_profile_verdict": "C26 should allow Stage2 when a platform has subscription/user or ARPU expansion that can convert into operating leverage. DearU produced very high MFE with almost no entry-basis MAE, but later local 4B-watch is still needed if subscriber/artist expansion evidence stops refreshing after the peak."}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R8L73-C26-214270-FSN-DIGITAL-ADTECH-PRICE-BETA-LOCAL4B", "trigger_id": "TRG_R8L73-C26-214270-FSN-DIGITAL-ADTECH-PRICE-BETA-LOCAL4B", "symbol": "214270", "large_sector_id": "L8_PLATFORM_CONTENT_SW_SECURITY", "canonical_archetype_id": "C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE", "raw_component_scores_before": {"recurring_revenue_score": 4, "ad_revenue_score": 10, "subscription_user_score": 2, "client_retention_score": 4, "margin_bridge_score": 3, "relative_strength_score": 8, "valuation_repricing_score": 7, "execution_risk_score": 15, "source_confidence_score": 2}, "weighted_score_before": 54, "stage_label_before": "Stage2-FalsePositive / RiskWatch", "raw_component_scores_after": {"recurring_revenue_score": 2, "ad_revenue_score": 8, "subscription_user_score": 1, "client_retention_score": 3, "margin_bridge_score": 2, "relative_strength_score": 4, "valuation_repricing_score": 5, "execution_risk_score": 18, "source_confidence_score": 2}, "weighted_score_after": 42, "stage_label_after": "Stage4B-local-watch / no durable Green", "changed_components": ["recurring_revenue_score", "subscription_user_score", "margin_bridge_score", "execution_risk_score", "relative_strength_score"], "component_delta_explanation": "Reward only verified subscription/user/ad-revenue/client-retention and margin bridge; cap price-only adtech or campaign beta when bridge evidence fails to refresh.", "MFE_90D_pct": 33.39, "MAE_90D_pct": -22.97, "score_return_alignment_label": "false_positive_platform_bridge_gap", "current_profile_verdict": "C26 should not treat digital-adtech or platform theme MFE as durable Stage2 unless recurring ad revenue, take-rate, client retention and margin conversion are visible. FSN had a sharp MFE but later severe MAE and post-peak drawdown."}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R8L73-C26-214320-INNOCEAN-AD-AGENCY-OPERATING-LEVERAGE-WEAK", "trigger_id": "TRG_R8L73-C26-214320-INNOCEAN-AD-AGENCY-OPERATING-LEVERAGE-WEAK", "symbol": "214320", "large_sector_id": "L8_PLATFORM_CONTENT_SW_SECURITY", "canonical_archetype_id": "C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE", "raw_component_scores_before": {"recurring_revenue_score": 4, "ad_revenue_score": 10, "subscription_user_score": 2, "client_retention_score": 8, "margin_bridge_score": 3, "relative_strength_score": 8, "valuation_repricing_score": 7, "execution_risk_score": 15, "source_confidence_score": 2}, "weighted_score_before": 54, "stage_label_before": "Stage2-FalsePositive / RiskWatch", "raw_component_scores_after": {"recurring_revenue_score": 2, "ad_revenue_score": 8, "subscription_user_score": 1, "client_retention_score": 8, "margin_bridge_score": 2, "relative_strength_score": 4, "valuation_repricing_score": 5, "execution_risk_score": 18, "source_confidence_score": 2}, "weighted_score_after": 42, "stage_label_after": "Stage4B-local-watch / no durable Green", "changed_components": ["recurring_revenue_score", "subscription_user_score", "margin_bridge_score", "execution_risk_score", "relative_strength_score"], "component_delta_explanation": "Reward only verified subscription/user/ad-revenue/client-retention and margin bridge; cap price-only adtech or campaign beta when bridge evidence fails to refresh.", "MFE_90D_pct": 4.59, "MAE_90D_pct": -2.98, "score_return_alignment_label": "false_positive_platform_bridge_gap", "current_profile_verdict": "C26 should distinguish ad-agency campaign stability from true platform operating leverage. Innocean had limited MFE and later MAE; without client-budget, digital mix or margin revision evidence it should remain RiskWatch / no durable Green rather than Stage2."}
```

### aggregate row

```jsonl
{"row_type": "aggregate", "round": "R8", "loop": 73, "large_sector_id": "L8_PLATFORM_CONTENT_SW_SECURITY", "canonical_archetype_id": "C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE", "fine_archetype_id": "SUBSCRIPTION_FANDOM_PLATFORM_AND_DIGITAL_AD_OPERATING_LEVERAGE_VS_PRICE_ONLY_ADTECH_BETA", "calibration_usable_case_count": 3, "calibration_usable_trigger_count": 3, "new_independent_case_count": 3, "reused_case_count": 0, "same_archetype_new_symbol_count": 3, "same_archetype_new_trigger_family_count": 3, "positive_case_count": 1, "counterexample_count": 1, "riskwatch_boundary_case_count": 1, "four_b_case_count": 2, "four_c_case_count": 0, "source_proxy_only_count": 3, "evidence_url_pending_count": 3, "current_profile_error_count": 2, "diversity_score_summary": "+3 underused C26 symbols, +3 platform/ad operating-leverage trigger families, +1 subscription-platform positive, +1 adtech beta local-4B, +1 agency riskwatch boundary, no hard duplicate", "residual_contribution_label": "coverage_gap_fill_with_source_repair_needed"}
```

### shadow weight row

```jsonl
{"row_type": "shadow_weight", "round": "R8", "loop": 73, "large_sector_id": "L8_PLATFORM_CONTENT_SW_SECURITY", "canonical_archetype_id": "C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE", "axis": "subscription_fandom_platform_and_digital_ad_operating_leverage_vs_price_only_adtech_beta", "decision": "hold_for_source_repair_and_more_evidence", "proposed_runtime_effect": "C26 should split verified recurring subscription/ad revenue operating leverage from price-only adtech or agency beta. Stage2 requires subscriber/user/ARPU, client retention, ad-budget recovery, take-rate or margin conversion evidence. If MFE is followed by stale bridge evidence and post-peak drawdown, route to local 4B-watch.", "do_not_propose_new_weight_delta": true, "needs_more_evidence": true, "source_repair_required": ["376300", "214270", "214320"]}
```

### residual contribution row

```jsonl
{"row_type": "residual_contribution", "round": "R8", "loop": 73, "large_sector_id": "L8_PLATFORM_CONTENT_SW_SECURITY", "canonical_archetype_id": "C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE", "existing_axis_strengthened": ["stage2_required_bridge", "price_only_blowoff_blocks_positive_stage", "local_4b_watch_guard"], "new_axis_proposed": null, "sector_specific_rule_candidate": true, "canonical_archetype_rule_candidate": true, "narrative_summary": "C26 needs platform revenue proof. 디어유 shows subscription-platform operating leverage after source repair; FSN shows adtech price beta collapsing without recurring revenue/margin bridge; 이노션 shows stable agency beta that should remain RiskWatch without stronger digital/ad-budget operating leverage."}
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
376300:
  corporate_action_candidate_dates = none
  selected window = 2024-10-28~D+180
  contamination = false

214270:
  corporate_action_candidate_dates = 2016-10-05, 2018-03-05, 2021-11-08
  selected window = 2024-02-01~D+180
  contamination = false

214320:
  corporate_action_candidate_dates = 2023-11-29, 2023-12-21
  selected window = 2024-02-01~D+180
  contamination = false
```

Data-quality caveat:

```text
All selected C26 rows are source_proxy_only / evidence_url_pending.
This MD is useful for stock-web path calibration and C26 rule-shape discovery,
but coding-agent promotion requires non-proxy subscription/user/ARPU/ad-revenue/client-retention/margin evidence.
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
subscription_fandom_platform_and_digital_ad_operating_leverage_vs_price_only_adtech_beta

Required checks before implementation:
1. Validate all trigger rows against stock-web tradable_raw OHLC shards.
2. Confirm no hard duplicate key:
   canonical_archetype_id + symbol + trigger_type + entry_date.
3. Verify non-proxy source URLs for 376300, 214270 and 214320.
4. Keep generic C26 platform/ad weight unchanged until source repair is complete.
5. Consider Stage2 only when:
   - subscriber/user/ARPU, ad revenue, client retention or campaign expansion is explicit,
   - recurring revenue or take-rate bridge exists,
   - margin conversion or operating leverage is visible,
   - MAE remains controlled.
6. Consider local 4B-watch when:
   - the trigger is price-only platform/adtech/agency beta,
   - recurring revenue or margin evidence fails to refresh,
   - MAE_90D <= -20% or MAE_180D <= -25%,
   - post-peak drawdown <= -35%.
7. Do not convert local 4B-watch into full 4B/4C without non-price deterioration evidence.
8. Emit before/after diagnostics and reject if verified platform operating-leverage positives are overblocked.
```

---

## Final round state

```text
completed_round = R8
completed_loop = 73
next_round = R9
next_loop = 73
round_schedule_status = valid
round_sector_consistency = pass
```

