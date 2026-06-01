# E2R Stock-Web v12 Residual Research — R12 Loop 81 / L10 / C31

## Metadata

```json
{
  "research_session": "post_calibrated_sector_archetype_residual_research",
  "mode": "historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12",
  "scheduled_round": "R12",
  "scheduled_loop": 81,
  "round_schedule_status": "valid",
  "round_sector_consistency": "pass",
  "completed_round": "R12",
  "completed_loop": 81,
  "computed_next_round": "R13",
  "computed_next_loop": 81,
  "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC",
  "canonical_archetype_id": "C31_POLICY_SUBSIDY_LEGISLATION_EVENT",
  "fine_archetype_id": "FOOD_SECURITY_FEED_SEED_AGRI_POLICY_DIRECT_BENEFICIARY_BRIDGE_VS_AGRI_THEME_FADE",
  "loop_objective": [
    "coverage_gap_fill",
    "counterexample_mining",
    "policy_event_bridge_guardrail",
    "4B_non_price_requirement_stress_test",
    "food_security_feed_seed_agri_policy_direct_beneficiary_mapping",
    "agri_food_policy_theme_beta_boundary",
    "under_covered_agri_service_sector_expansion",
    "bounded_no_forced4B_guard",
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

Previous completed state in this interactive run: R11 / loop 81.

Therefore:

```text
scheduled_round = R12
scheduled_loop = 81
allowed_large_sector = L10_POLICY_EVENT_CROSS_REDTEAM_MISC or relevant under-covered service/agri sector
selected_large_sector = L10_POLICY_EVENT_CROSS_REDTEAM_MISC
selected_canonical_archetype_id = C31_POLICY_SUBSIDY_LEGISLATION_EVENT
computed_next_round = R13
computed_next_loop = 81
```

R12 was routed to C31 because this is an under-covered agri/food-security policy event bridge guardrail, not a normal consumer, materials, or mobility round.  
This file deliberately avoids loop-80 education-policy names and loop-81 childcare-policy names.

## No-Repeat / novelty check

No hard duplicate is intentionally reused.

Hard duplicate key checked conceptually:

```text
canonical_archetype_id + symbol + trigger_type + entry_date
```

No-Repeat shows C31 concentration in:

```text
112610, 034020, 336260, UNKNOWN_SYMBOL, 036460
```

This run uses three different agri/food-security symbols outside that top-covered set:

```text
005860 / 한일사료 / food-security feed direct-beneficiary lifecycle
027710 / 팜스토리 / feed and food-security theme fade
054050 / 농우바이오 / seed/agri policy bounded no-forced-4B boundary
```

Data-quality note:

```text
All three rows are stock-web calibration usable by profile-level corporate-action candidates.
All three rows are source_proxy_only=true / evidence_url_pending=true.
No selected row has a profile-level 2024 corporate-action candidate inside the selected window.
```

## Research thesis

C31 is not “식량안보 정책 테마가 올랐다.”

For food-security / agri rows, the bridge must pass through:

```text
policy / food-security / grain-price headline
→ direct beneficiary mapping
→ feed, seed or agri-input demand
→ input-cost pass-through or channel demand
→ revenue conversion and margin bridge
→ durable rerating
```

식량안보 headline은 곡물창고의 문패다.  
C31이 보려는 것은 문패가 아니라 실제 사료 수요, 종자 수요, 원가 전가, 매출, 마진이라는 곡식이 창고에 쌓이는지다.

---

## Case 1 — Policy lifecycle candidate: 005860 / 한일사료

### Evidence status

```text
source_proxy_only = true
evidence_url_pending = true
source_repair_required = true
```

The source-repair task is food-security / feed policy, grain-price pass-through, direct feed demand, customer volume, revenue conversion and margin bridge evidence.

```text
evidence_family = FOOD_SECURITY_FEED_GRAIN_PRICE_POLICY_DIRECT_BENEFICIARY_VOLUME_REVENUE_MARGIN_BRIDGE_CANDIDATE
case_role = policy_lifecycle_positive_feed_food_security_with_later_4b_watch
trigger_date = 2024-01-31
entry_date = 2024-02-01
entry_price = 4,515
```

### Stock-Web price path

Observed rows from `atlas/ohlcv_tradable_by_symbol_year/005/005860/2024.csv`:

```text
2024-02-01,4515,4610,4495,4530
2024-02-14,4760,4890,4655,4680
2024-03-13,4370,4680,4345,4520
2024-03-19,4485,4770,4485,4655
2024-03-25,4695,5880,4695,5880
2024-08-05,4770,4930,3990,4320
2024-09-09,3840,4000,3830,3985
2024-10-25,4120,4215,4005,4060
```

### Backtest

```text
MFE_30D  = +30.23%
MAE_30D  = -4.65%
MFE_90D  = +30.23%
MAE_90D  = -11.30%
MFE_180D = +30.23%
MAE_180D = -15.17%
peak_180 = 5,880 on 2024-03-25
trough_180 = 3,830 on 2024-09-09
peak_to_later_drawdown = -34.86%
```

### Interpretation

This is a C31 food-security/feed policy lifecycle candidate, not durable Green.  
The MFE was tradable, but the later drawdown means direct-demand and margin evidence must refresh.

Correct treatment:

```text
verified food-security policy / direct feed demand / input-cost pass-through / margin bridge → Stage2-Yellow possible
bridge stale after peak → local 4B-watch
```

---

## Case 2 — Counterexample / local 4B: 027710 / 팜스토리

### Evidence status

```text
source_proxy_only = true
evidence_url_pending = true
source_repair_required = true
```

This row tests feed/food-security policy beta without enough direct volume, revenue and margin bridge.

```text
evidence_family = FOOD_SECURITY_FEED_MEAT_SUPPLY_THEME_WITH_WEAK_DIRECT_VOLUME_REVENUE_MARGIN_BRIDGE
case_role = counterexample_feed_food_security_theme_local4b
trigger_date = 2024-01-31
entry_date = 2024-02-01
entry_price = 1,610
```

### Stock-Web price path

Observed rows from `atlas/ohlcv_tradable_by_symbol_year/027/027710/2024.csv`:

```text
2024-02-01,1610,1635,1610,1622
2024-02-05,1641,1655,1635,1650
2024-03-25,1582,1675,1582,1657
2024-07-25,1504,1504,1455,1462
2024-08-05,1496,1496,1277,1308
2024-09-09,1300,1331,1280,1322
2024-10-15,1341,1545,1341,1403
2024-10-31,1292,1313,1290,1304
```

### Backtest

```text
MFE_30D  = +4.04%
MAE_30D  = -2.24%
MFE_90D  = +4.04%
MAE_90D  = -9.69%
MFE_180D = +4.04%
MAE_180D = -20.68%
peak_180 = 1,675 on 2024-03-25
trough_180 = 1,277 on 2024-08-05
peak_to_later_drawdown = -23.76%
```

### Interpretation

This is a C31 feed/food-security theme-fade boundary.  
The post-entry MFE was weak and the path turned into persistent drawdown.

Correct treatment:

```text
feed / food-security theme beta
→ no verified direct volume / revenue / margin bridge
→ local 4B-watch, not durable Stage2
```

---

## Case 3 — Bounded no-forced-4B boundary: 054050 / 농우바이오

### Evidence status

```text
source_proxy_only = true
evidence_url_pending = true
source_repair_required = true
```

This row tests seed/agri policy beta with bounded MAE but incomplete direct-beneficiary economics.

```text
evidence_family = SEED_AGRI_POLICY_FOOD_SECURITY_THEME_WITH_BOUNDED_MAE_AND_WEAK_DIRECT_REVENUE_MARGIN_BRIDGE
case_role = overbearish_counterexample_bounded_seed_agri_policy_no_forced4b
trigger_date = 2024-01-31
entry_date = 2024-02-01
entry_price = 8,000
```

### Stock-Web price path

Observed rows from `atlas/ohlcv_tradable_by_symbol_year/054/054050/2024.csv`:

```text
2024-02-01,8000,8150,8000,8050
2024-02-19,8200,8480,8110,8480
2024-02-21,8490,8820,8400,8470
2024-04-15,7960,7960,7870,7900
2024-08-05,7780,7850,7330,7420
2024-09-09,7100,7100,6990,7060
2024-10-14,7410,7530,7400,7500
2024-10-31,7240,7250,7190,7240
```

### Backtest

```text
MFE_30D  = +10.25%
MAE_30D  = +0.00%
MFE_90D  = +10.25%
MAE_90D  = -1.63%
MFE_180D = +10.25%
MAE_180D = -12.63%
peak_180 = 8,820 on 2024-02-21
trough_180 = 6,990 on 2024-09-09
peak_to_later_drawdown = -20.75%
```

### Interpretation

This is not durable Stage2, but it is also not forced local 4B.  
The correct result is RiskWatch until seed demand and margin bridge are source-repaired.

Correct treatment:

```text
seed/agri policy watch
bounded MAE
→ no durable Stage2 without seed demand / revenue / margin bridge
→ no forced 4B without non-price deterioration
```

---

## Cross-case residual finding

### What this strengthens

```text
price_only_blowoff_blocks_positive_stage = strengthen
local_4b_watch_guard = strengthen
stage2_required_bridge = strengthen
direct_beneficiary_mapping_required = strengthen
undercovered_agri_food_policy_guard = strengthen
bounded_MAE_no_forced_4B_guard = strengthen
full_4b_requires_non_price_evidence = keep
```

### What this does not justify

```text
do_not_raise_generic_C31_food_security_theme_weight = true
do_not_treat_food_security_or_agri_policy_headline_as_Green_without_direct_revenue_bridge = true
do_not_force_4B_on_bounded_seed_agri_rows_without_non_price_break = true
do_not_convert_policy_theme_drawdown_to_hard_4C_without_non_price_policy_reversal_demand_failure_or_margin_break = true
```

### Candidate canonical compression

Fine labels can compress into:

```text
FOOD_SECURITY_FEED_SEED_AGRI_POLICY_DIRECT_BENEFICIARY_BRIDGE_VS_AGRI_THEME_FADE
```

This fine archetype covers:

```text
1. feed/food-security direct-beneficiary candidate → policy lifecycle Stage2-Yellow only after source repair
2. feed/food-security beta without direct volume/revenue bridge → false Stage2 / local 4B
3. seed/agri policy beta with bounded MAE → RiskWatch / no durable Stage2 / no forced 4B
```

---

## Machine-readable rows

### price source validation row

```jsonl
{"row_type": "price_source_validation", "source": "Songdaiki/stock-web", "source_url": "https://github.com/Songdaiki/stock-web", "manifest_path": "atlas/manifest.json", "schema_path": "atlas/schema.json", "universe_path": "atlas/universe/all_symbols.csv", "manifest_max_date": "2026-02-20", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "raw_shard_root": "atlas/ohlcv_raw_by_symbol_year", "validation_status": "usable_for_historical_calibration"}
```

### case rows

```jsonl
{"row_type": "case", "case_id": "R12L81-C31-005860-HANIL-FEED-FOOD-SECURITY-LIFECYCLE", "symbol": "005860", "company_name": "한일사료", "round": "R12", "loop": "81", "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "C31_POLICY_SUBSIDY_LEGISLATION_EVENT", "fine_archetype_id": "FOOD_SECURITY_FEED_SEED_AGRI_POLICY_DIRECT_BENEFICIARY_BRIDGE_VS_AGRI_THEME_FADE", "case_type": "policy_subsidy_legislation_event_agri_food_security", "positive_or_counterexample": "policy_lifecycle_positive", "best_trigger": "PolicyLifecycle-FoodSecurityFeedDirectBeneficiaryRevenueMarginBridgeWithLocal4B", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 0.5, "score_price_alignment": "C31 should allow food-security/feed policy positives only when policy or grain-price attention maps to direct feed demand, purchase cost pass-through, customer volume, revenue conversion and margin bridge. Hanil Feed produced tradable MFE but later drawdown requires lifecycle 4B if direct-economics evidence fades.", "current_profile_verdict": "source_repair_required_before_runtime_weight", "price_source": "Songdaiki/stock-web", "notes": "Stock-web path usable; non-proxy food-security/agri policy event, direct beneficiary mapping, feed/seed demand, input-cost pass-through, revenue and margin bridge evidence required before runtime promotion."}
{"row_type": "case", "case_id": "R12L81-C31-027710-FARMSTORY-FEED-FOOD-SECURITY-THEME-FADE", "symbol": "027710", "company_name": "팜스토리", "round": "R12", "loop": "81", "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "C31_POLICY_SUBSIDY_LEGISLATION_EVENT", "fine_archetype_id": "FOOD_SECURITY_FEED_SEED_AGRI_POLICY_DIRECT_BENEFICIARY_BRIDGE_VS_AGRI_THEME_FADE", "case_type": "policy_subsidy_legislation_event_agri_food_security", "positive_or_counterexample": "counterexample", "best_trigger": "Stage2-FalsePositive / FeedFoodSecurityPolicyThemeFadeWithLocal4BWatch", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 0.5, "score_price_alignment": "C31 should not treat feed/food-security policy beta as durable Stage2 unless direct feed/meat demand, input cost pass-through, customer volume, revenue and margin bridge are visible. FarmStory had almost no post-entry MFE and then a persistent MAE path.", "current_profile_verdict": "source_repair_required_before_runtime_weight", "price_source": "Songdaiki/stock-web", "notes": "Stock-web path usable; non-proxy food-security/agri policy event, direct beneficiary mapping, feed/seed demand, input-cost pass-through, revenue and margin bridge evidence required before runtime promotion."}
{"row_type": "case", "case_id": "R12L81-C31-054050-NONGWOO-BIO-SEED-AGRI-POLICY-BOUNDED", "symbol": "054050", "company_name": "농우바이오", "round": "R12", "loop": "81", "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "C31_POLICY_SUBSIDY_LEGISLATION_EVENT", "fine_archetype_id": "FOOD_SECURITY_FEED_SEED_AGRI_POLICY_DIRECT_BENEFICIARY_BRIDGE_VS_AGRI_THEME_FADE", "case_type": "policy_subsidy_legislation_event_agri_food_security", "positive_or_counterexample": "overbearish_counterexample", "best_trigger": "RiskWatch-BoundedSeedAgriPolicyNoDurableStage2NoForced4B", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 0.5, "score_price_alignment": "C31 should keep seed/agri policy monitoring active, but should not force local 4B when MAE is bounded and no non-price demand or margin break is confirmed. Nongwoo Bio is a RiskWatch/no durable Stage2/no forced 4B boundary.", "current_profile_verdict": "source_repair_required_before_runtime_weight", "price_source": "Songdaiki/stock-web", "notes": "Stock-web path usable; non-proxy food-security/agri policy event, direct beneficiary mapping, feed/seed demand, input-cost pass-through, revenue and margin bridge evidence required before runtime promotion."}
```

### trigger rows

```jsonl
{"row_type": "trigger", "trigger_id": "TRG_R12L81-C31-005860-HANIL-FEED-FOOD-SECURITY-LIFECYCLE", "case_id": "R12L81-C31-005860-HANIL-FEED-FOOD-SECURITY-LIFECYCLE", "symbol": "005860", "company_name": "한일사료", "round": "R12", "loop": "81", "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "C31_POLICY_SUBSIDY_LEGISLATION_EVENT", "fine_archetype_id": "FOOD_SECURITY_FEED_SEED_AGRI_POLICY_DIRECT_BENEFICIARY_BRIDGE_VS_AGRI_THEME_FADE", "loop_objective": "coverage_gap_fill|counterexample_mining|policy_event_bridge_guardrail|undercovered_agri_food_axis", "trigger_type": "PolicyLifecycle-FoodSecurityFeedDirectBeneficiaryRevenueMarginBridgeWithLocal4B", "trigger_date": "2024-01-31", "entry_date": "2024-02-01", "entry_price": 4515.0, "evidence_available_at_that_date": "FOOD_SECURITY_FEED_GRAIN_PRICE_POLICY_DIRECT_BENEFICIARY_VOLUME_REVENUE_MARGIN_BRIDGE_CANDIDATE", "evidence_source": "source_proxy_manual_verification_required:HANIL_FEED_2024_FOOD_SECURITY_FEED_GRAIN_PRICE_DIRECT_DEMAND_REVENUE_MARGIN_BRIDGE", "stage2_evidence_fields": ["policy_or_food_security_event", "direct_beneficiary_mapping_candidate", "feed_seed_demand_revenue_margin_bridge_candidate"], "stage3_evidence_fields": ["relative_strength", "input_cost_pass_through_or_channel_demand_candidate"], "stage4b_evidence_fields": ["agri_food_policy_theme_beta", "bridge_stale_or_absent", "MAE_widening", "post_peak_drawdown"], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/005/005860/2024.csv", "profile_path": "atlas/symbol_profiles/005/005860.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": 30.23, "MFE_90D_pct": 30.23, "MFE_180D_pct": 30.23, "MAE_30D_pct": -4.65, "MAE_90D_pct": -11.3, "MAE_180D_pct": -15.17, "peak_date": "2024-03-25", "peak_price": 5880.0, "drawdown_after_peak_pct": -34.86, "green_lateness_ratio": null, "four_b_local_peak_proximity": "local_4b_watch_after_food_security_policy_peak_if_direct_demand_revenue_or_margin_bridge_fades", "four_b_full_window_peak_proximity": "full_4b_requires_non_price_policy_reversal_demand_failure_input_cost_shock_revenue_or_margin_break", "trigger_outcome_label": "policy_lifecycle_positive_feed_food_security_with_later_4b_watch", "current_profile_verdict": "C31 should allow food-security/feed policy positives only when policy or grain-price attention maps to direct feed demand, purchase cost pass-through, customer volume, revenue conversion and margin bridge. Hanil Feed produced tradable MFE but later drawdown requires lifecycle 4B if direct-economics evidence fades.", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window_by_profile", "share_count_change_inside_window": false, "same_entry_group_id": "C31_AGRI_FOOD_POLICY_005860_2024-02-01", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 0.5, "do_not_count_as_new_case": false, "source_proxy_only": true, "evidence_url_pending": true}
{"row_type": "trigger", "trigger_id": "TRG_R12L81-C31-027710-FARMSTORY-FEED-FOOD-SECURITY-THEME-FADE", "case_id": "R12L81-C31-027710-FARMSTORY-FEED-FOOD-SECURITY-THEME-FADE", "symbol": "027710", "company_name": "팜스토리", "round": "R12", "loop": "81", "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "C31_POLICY_SUBSIDY_LEGISLATION_EVENT", "fine_archetype_id": "FOOD_SECURITY_FEED_SEED_AGRI_POLICY_DIRECT_BENEFICIARY_BRIDGE_VS_AGRI_THEME_FADE", "loop_objective": "coverage_gap_fill|counterexample_mining|policy_event_bridge_guardrail|undercovered_agri_food_axis", "trigger_type": "Stage2-FalsePositive / FeedFoodSecurityPolicyThemeFadeWithLocal4BWatch", "trigger_date": "2024-01-31", "entry_date": "2024-02-01", "entry_price": 1610.0, "evidence_available_at_that_date": "FOOD_SECURITY_FEED_MEAT_SUPPLY_THEME_WITH_WEAK_DIRECT_VOLUME_REVENUE_MARGIN_BRIDGE", "evidence_source": "source_proxy_manual_verification_required:FARMSTORY_2024_FOOD_SECURITY_FEED_MEAT_SUPPLY_DIRECT_VOLUME_REVENUE_MARGIN_BRIDGE", "stage2_evidence_fields": ["policy_or_food_security_event", "direct_beneficiary_mapping_candidate", "feed_seed_demand_revenue_margin_bridge_candidate"], "stage3_evidence_fields": ["relative_strength", "input_cost_pass_through_or_channel_demand_candidate"], "stage4b_evidence_fields": ["agri_food_policy_theme_beta", "bridge_stale_or_absent", "MAE_widening", "post_peak_drawdown"], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/027/027710/2024.csv", "profile_path": "atlas/symbol_profiles/027/027710.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": 4.04, "MFE_90D_pct": 4.04, "MFE_180D_pct": 4.04, "MAE_30D_pct": -2.24, "MAE_90D_pct": -9.69, "MAE_180D_pct": -20.68, "peak_date": "2024-03-25", "peak_price": 1675.0, "drawdown_after_peak_pct": -23.76, "green_lateness_ratio": null, "four_b_local_peak_proximity": "local_4b_watch_after_food_security_policy_peak_if_direct_demand_revenue_or_margin_bridge_fades", "four_b_full_window_peak_proximity": "full_4b_requires_non_price_policy_reversal_demand_failure_input_cost_shock_revenue_or_margin_break", "trigger_outcome_label": "counterexample_feed_food_security_theme_local4b", "current_profile_verdict": "C31 should not treat feed/food-security policy beta as durable Stage2 unless direct feed/meat demand, input cost pass-through, customer volume, revenue and margin bridge are visible. FarmStory had almost no post-entry MFE and then a persistent MAE path.", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window_by_profile", "share_count_change_inside_window": false, "same_entry_group_id": "C31_AGRI_FOOD_POLICY_027710_2024-02-01", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 0.5, "do_not_count_as_new_case": false, "source_proxy_only": true, "evidence_url_pending": true}
{"row_type": "trigger", "trigger_id": "TRG_R12L81-C31-054050-NONGWOO-BIO-SEED-AGRI-POLICY-BOUNDED", "case_id": "R12L81-C31-054050-NONGWOO-BIO-SEED-AGRI-POLICY-BOUNDED", "symbol": "054050", "company_name": "농우바이오", "round": "R12", "loop": "81", "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "C31_POLICY_SUBSIDY_LEGISLATION_EVENT", "fine_archetype_id": "FOOD_SECURITY_FEED_SEED_AGRI_POLICY_DIRECT_BENEFICIARY_BRIDGE_VS_AGRI_THEME_FADE", "loop_objective": "coverage_gap_fill|counterexample_mining|policy_event_bridge_guardrail|undercovered_agri_food_axis", "trigger_type": "RiskWatch-BoundedSeedAgriPolicyNoDurableStage2NoForced4B", "trigger_date": "2024-01-31", "entry_date": "2024-02-01", "entry_price": 8000.0, "evidence_available_at_that_date": "SEED_AGRI_POLICY_FOOD_SECURITY_THEME_WITH_BOUNDED_MAE_AND_WEAK_DIRECT_REVENUE_MARGIN_BRIDGE", "evidence_source": "source_proxy_manual_verification_required:NONGWOO_BIO_2024_SEED_AGRI_POLICY_FOOD_SECURITY_DIRECT_DEMAND_REVENUE_MARGIN_BRIDGE", "stage2_evidence_fields": ["policy_or_food_security_event", "direct_beneficiary_mapping_candidate", "feed_seed_demand_revenue_margin_bridge_candidate"], "stage3_evidence_fields": ["relative_strength", "input_cost_pass_through_or_channel_demand_candidate"], "stage4b_evidence_fields": ["agri_food_policy_theme_beta", "bridge_stale_or_absent", "MAE_widening", "post_peak_drawdown"], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/054/054050/2024.csv", "profile_path": "atlas/symbol_profiles/054/054050.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": 10.25, "MFE_90D_pct": 10.25, "MFE_180D_pct": 10.25, "MAE_30D_pct": 0.0, "MAE_90D_pct": -1.62, "MAE_180D_pct": -12.62, "peak_date": "2024-02-21", "peak_price": 8820.0, "drawdown_after_peak_pct": -20.75, "green_lateness_ratio": null, "four_b_local_peak_proximity": "local_4b_watch_after_food_security_policy_peak_if_direct_demand_revenue_or_margin_bridge_fades", "four_b_full_window_peak_proximity": "full_4b_requires_non_price_policy_reversal_demand_failure_input_cost_shock_revenue_or_margin_break", "trigger_outcome_label": "overbearish_counterexample_bounded_seed_agri_policy_no_forced4b", "current_profile_verdict": "C31 should keep seed/agri policy monitoring active, but should not force local 4B when MAE is bounded and no non-price demand or margin break is confirmed. Nongwoo Bio is a RiskWatch/no durable Stage2/no forced 4B boundary.", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window_by_profile", "share_count_change_inside_window": false, "same_entry_group_id": "C31_AGRI_FOOD_POLICY_054050_2024-02-01", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 0.5, "do_not_count_as_new_case": false, "source_proxy_only": true, "evidence_url_pending": true}
```

### score simulation rows

```jsonl
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R12L81-C31-005860-HANIL-FEED-FOOD-SECURITY-LIFECYCLE", "trigger_id": "TRG_R12L81-C31-005860-HANIL-FEED-FOOD-SECURITY-LIFECYCLE", "symbol": "005860", "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "C31_POLICY_SUBSIDY_LEGISLATION_EVENT", "raw_component_scores_before": {"policy_event_score": 13, "direct_beneficiary_mapping_score": 13, "feed_seed_demand_score": 12, "input_cost_pass_through_score": 11, "revenue_margin_bridge_score": 12, "relative_strength_score": 9, "execution_risk_score": 12, "source_confidence_score": 2}, "weighted_score_before": 72, "stage_label_before": "Policy lifecycle candidate after source repair", "raw_component_scores_after": {"policy_event_score": 9, "direct_beneficiary_mapping_score": 15, "feed_seed_demand_score": 14, "input_cost_pass_through_score": 13, "revenue_margin_bridge_score": 14, "relative_strength_score": 8, "execution_risk_score": 13, "source_confidence_score": 2}, "weighted_score_after": 78, "stage_label_after": "Policy lifecycle Stage2-Yellow after source repair + local 4B", "changed_components": ["policy_event_score", "direct_beneficiary_mapping_score", "feed_seed_demand_score", "input_cost_pass_through_score", "revenue_margin_bridge_score", "execution_risk_score"], "component_delta_explanation": "Cap policy-event score unless food-security/agri policy maps to direct beneficiary economics, feed/seed demand, input-cost pass-through, revenue conversion and margin bridge.", "MFE_90D_pct": 30.23, "MAE_90D_pct": -11.3, "score_return_alignment_label": "food_security_policy_lifecycle_with_later_4b", "current_profile_verdict": "C31 should allow food-security/feed policy positives only when policy or grain-price attention maps to direct feed demand, purchase cost pass-through, customer volume, revenue conversion and margin bridge. Hanil Feed produced tradable MFE but later drawdown requires lifecycle 4B if direct-economics evidence fades."}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R12L81-C31-027710-FARMSTORY-FEED-FOOD-SECURITY-THEME-FADE", "trigger_id": "TRG_R12L81-C31-027710-FARMSTORY-FEED-FOOD-SECURITY-THEME-FADE", "symbol": "027710", "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "C31_POLICY_SUBSIDY_LEGISLATION_EVENT", "raw_component_scores_before": {"policy_event_score": 13, "direct_beneficiary_mapping_score": 4, "feed_seed_demand_score": 3, "input_cost_pass_through_score": 2, "revenue_margin_bridge_score": 1, "relative_strength_score": 4, "execution_risk_score": 24, "source_confidence_score": 2}, "weighted_score_before": 42, "stage_label_before": "Stage2-FalsePositive / local 4B-watch", "raw_component_scores_after": {"policy_event_score": 9, "direct_beneficiary_mapping_score": 2, "feed_seed_demand_score": 1, "input_cost_pass_through_score": 1, "revenue_margin_bridge_score": 1, "relative_strength_score": 3, "execution_risk_score": 26, "source_confidence_score": 2}, "weighted_score_after": 31, "stage_label_after": "Stage4B-local-watch / no durable Green", "changed_components": ["policy_event_score", "direct_beneficiary_mapping_score", "feed_seed_demand_score", "input_cost_pass_through_score", "revenue_margin_bridge_score", "execution_risk_score"], "component_delta_explanation": "Cap policy-event score unless food-security/agri policy maps to direct beneficiary economics, feed/seed demand, input-cost pass-through, revenue conversion and margin bridge.", "MFE_90D_pct": 4.04, "MAE_90D_pct": -9.69, "score_return_alignment_label": "food_security_policy_theme_false_positive_direct_economics_gap", "current_profile_verdict": "C31 should not treat feed/food-security policy beta as durable Stage2 unless direct feed/meat demand, input cost pass-through, customer volume, revenue and margin bridge are visible. FarmStory had almost no post-entry MFE and then a persistent MAE path."}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R12L81-C31-054050-NONGWOO-BIO-SEED-AGRI-POLICY-BOUNDED", "trigger_id": "TRG_R12L81-C31-054050-NONGWOO-BIO-SEED-AGRI-POLICY-BOUNDED", "symbol": "054050", "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "C31_POLICY_SUBSIDY_LEGISLATION_EVENT", "raw_component_scores_before": {"policy_event_score": 13, "direct_beneficiary_mapping_score": 6, "feed_seed_demand_score": 6, "input_cost_pass_through_score": 5, "revenue_margin_bridge_score": 4, "relative_strength_score": 4, "execution_risk_score": 8, "source_confidence_score": 2}, "weighted_score_before": 58, "stage_label_before": "RiskWatch / no forced 4B", "raw_component_scores_after": {"policy_event_score": 9, "direct_beneficiary_mapping_score": 5, "feed_seed_demand_score": 5, "input_cost_pass_through_score": 4, "revenue_margin_bridge_score": 3, "relative_strength_score": 4, "execution_risk_score": 7, "source_confidence_score": 2}, "weighted_score_after": 60, "stage_label_after": "RiskWatch / no durable Stage2 and no forced 4B", "changed_components": ["policy_event_score", "direct_beneficiary_mapping_score", "feed_seed_demand_score", "input_cost_pass_through_score", "revenue_margin_bridge_score", "execution_risk_score"], "component_delta_explanation": "Cap policy-event score unless food-security/agri policy maps to direct beneficiary economics, feed/seed demand, input-cost pass-through, revenue conversion and margin bridge.", "MFE_90D_pct": 10.25, "MAE_90D_pct": -1.62, "score_return_alignment_label": "bounded_seed_policy_no_forced4b", "current_profile_verdict": "C31 should keep seed/agri policy monitoring active, but should not force local 4B when MAE is bounded and no non-price demand or margin break is confirmed. Nongwoo Bio is a RiskWatch/no durable Stage2/no forced 4B boundary."}
```

### aggregate row

```jsonl
{"row_type": "aggregate", "round": "R12", "loop": 81, "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "C31_POLICY_SUBSIDY_LEGISLATION_EVENT", "fine_archetype_id": "FOOD_SECURITY_FEED_SEED_AGRI_POLICY_DIRECT_BENEFICIARY_BRIDGE_VS_AGRI_THEME_FADE", "calibration_usable_case_count": 3, "calibration_usable_trigger_count": 3, "new_independent_case_count": 3, "reused_case_count": 0, "same_archetype_new_symbol_count": 3, "same_archetype_new_trigger_family_count": 3, "positive_case_count": 1, "counterexample_count": 1, "overbearish_counterexample_count": 1, "four_b_case_count": 2, "four_c_case_count": 0, "source_proxy_only_count": 3, "evidence_url_pending_count": 3, "share_count_change_inside_window_count": 0, "current_profile_error_count": 1, "diversity_score_summary": "+3 C31 agri/food-security policy symbols outside top-covered 112610/034020/336260/036460 set and outside loop-80 education + loop-81 childcare names, +3 feed/food-security/seed trigger families, +1 policy lifecycle MFE candidate, +1 feed theme local-4B counterexample, +1 bounded seed/agri no-forced-4B boundary, no hard duplicate", "residual_contribution_label": "policy_event_bridge_guardrail_with_undercovered_agri_food_source_repair_needed"}
```

### shadow weight row

```jsonl
{"row_type": "shadow_weight", "round": "R12", "loop": 81, "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "C31_POLICY_SUBSIDY_LEGISLATION_EVENT", "axis": "food_security_feed_seed_agri_policy_direct_beneficiary_bridge_vs_agri_theme_fade", "decision": "hold_for_source_repair_and_more_evidence", "proposed_runtime_effect": "C31 should split food-security/feed/seed policy direct-beneficiary lifecycle trades from generic agri-food policy theme beta. Stage2 requires explicit policy/food-security event plus direct beneficiary mapping, feed/seed demand, input-cost pass-through, revenue conversion and margin bridge. If MFE fades and MAE/post-peak drawdown opens without bridge refresh, route to local 4B-watch. Bounded seed/agri rows should not be forced into 4B without non-price demand or margin break evidence.", "do_not_propose_new_weight_delta": true, "needs_more_evidence": true, "source_repair_required": ["005860", "027710", "054050"]}
```

### residual contribution row

```jsonl
{"row_type": "residual_contribution", "round": "R12", "loop": 81, "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "C31_POLICY_SUBSIDY_LEGISLATION_EVENT", "existing_axis_strengthened": ["price_only_blowoff_blocks_positive_stage", "local_4b_watch_guard", "stage2_required_bridge", "direct_beneficiary_mapping_required", "undercovered_agri_food_policy_guard", "bounded_MAE_no_forced_4B_guard", "full_4b_requires_non_price_evidence"], "new_axis_proposed": null, "sector_specific_rule_candidate": true, "canonical_archetype_rule_candidate": true, "narrative_summary": "C31 food-security/agri policy events need direct-beneficiary proof. Hanil Feed shows a tradable feed/food-security policy lifecycle candidate after source repair; FarmStory shows feed/food-security beta fading into local 4B; Nongwoo Bio shows a bounded seed/agri RiskWatch row where forced 4B would be too harsh."}
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
005860:
  name = 한일사료
  corporate_action_candidate_dates = 1997-01-30, 1997-02-13, 1999-07-14, 1999-10-11, 2000-01-10, 2016-12-22
  selected window = 2024-02-01~D+180
  contamination = false

027710:
  name = 팜스토리 from 2012-05-08, legacy names before that
  corporate_action_candidate_dates = 1999-10-25, 2000-05-26, 2000-06-09, 2005-10-25, 2011-01-21, 2019-12-13
  selected window = 2024-02-01~D+180
  contamination = false

054050:
  name = 농우바이오
  corporate_action_candidate_dates = none
  selected window = 2024-02-01~D+180
  contamination = false
```

Data-quality caveat:

```text
All selected C31 rows are source_proxy_only / evidence_url_pending.
This MD is useful for stock-web path calibration and C31 agri/food-security policy rule-shape discovery,
but coding-agent promotion requires non-proxy food-security/agri policy evidence, direct beneficiary mapping, feed/seed demand, input-cost pass-through, revenue conversion and margin evidence.
```

---

## Deferred Coding Agent Handoff Prompt

Do not execute this now.

```text
You are the coding agent for Songdaiki/stock_agent.

Read this standalone v12 residual research MD and ingest machine-readable rows only after validation.

Do not patch production scoring blindly.
This R12/C31 artifact is marked do_not_propose_new_weight_delta=true because all rows need source repair.

Candidate axis:
food_security_feed_seed_agri_policy_direct_beneficiary_bridge_vs_agri_theme_fade

Required checks before implementation:
1. Validate all trigger rows against stock-web tradable_raw OHLC shards.
2. Confirm no hard duplicate key:
   canonical_archetype_id + symbol + trigger_type + entry_date.
3. Verify non-proxy source URLs for 005860, 027710 and 054050.
4. Keep generic C31 policy-event weight unchanged until source repair is complete.
5. Consider Stage2 only when:
   - food-security / agri policy event is explicit,
   - direct beneficiary mapping is visible,
   - feed, seed or agri-input demand is visible,
   - input-cost pass-through or channel demand exists,
   - revenue conversion and margin bridge are credible,
   - MAE remains controlled or the signal is lifecycle-managed.
6. Consider local 4B-watch when:
   - the trigger is food-security/agri policy theme beta only,
   - direct demand / revenue / margin bridge is absent or stale,
   - MAE_90D <= -20% or MAE_180D <= -25%,
   - post-peak drawdown <= -35%.
7. Do not force local 4B when bounded seed/agri rows have controlled MAE and no confirmed non-price bridge break.
8. Do not convert local 4B-watch into full 4B/4C without non-price policy reversal, demand failure, input-cost shock, revenue deterioration or margin break evidence.
9. Emit before/after diagnostics and reject if verified direct-beneficiary food-security positives or bounded seed/agri rows are overblocked.
```

---

## Final round state

```text
completed_round = R12
completed_loop = 81
next_round = R13
next_loop = 81
round_schedule_status = valid
round_sector_consistency = pass
```

