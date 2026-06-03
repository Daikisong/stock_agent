# E2R Stock-Web v12 Residual Research — R4 Loop 75 / L4 / C16

## Metadata

```json
{
  "research_session": "post_calibrated_sector_archetype_residual_research",
  "mode": "historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12",
  "scheduled_round": "R4",
  "scheduled_loop": 75,
  "round_schedule_status": "valid",
  "round_sector_consistency": "pass",
  "completed_round": "R4",
  "completed_loop": 75,
  "computed_next_round": "R5",
  "computed_next_loop": 75,
  "large_sector_id": "L4_MATERIALS_SPREAD_RESOURCE",
  "canonical_archetype_id": "C16_STRATEGIC_RESOURCE_POLICY_SUPPLY",
  "fine_archetype_id": "RARE_METAL_PROCESSING_DIRECT_SUPPLY_BRIDGE_VS_RESOURCE_POLICY_PROXY_BETA_FADE",
  "loop_objective": [
    "coverage_gap_fill",
    "counterexample_mining",
    "4B_non_price_requirement_stress_test",
    "strategic_resource_policy_supply_guardrail",
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

Previous completed state in this interactive run: R3 / loop 75.

Therefore:

```text
scheduled_round = R4
scheduled_loop = 75
allowed_large_sector = L4_MATERIALS_SPREAD_RESOURCE
selected_large_sector = L4_MATERIALS_SPREAD_RESOURCE
selected_canonical_archetype_id = C16_STRATEGIC_RESOURCE_POLICY_SUPPLY
computed_next_round = R5
computed_next_loop = 75
```

R4 was routed to C16 because loop 74 used C15 and loop 73 used C17.  
C16 is thin and old-dated in the No-Repeat table, so this run tests fresh 2024 strategic-resource proxy vs direct-supply bridge behavior.

## No-Repeat / novelty check

No hard duplicate is intentionally reused.

Hard duplicate key checked conceptually:

```text
canonical_archetype_id + symbol + trigger_type + entry_date
```

No-Repeat shows C16 is concentrated in:

```text
005290, 027580, 047400, 093370
```

This run uses three different symbols:

```text
081150 / 티플랙스 / rare-metal processing supply bridge
000910 / 유니온 / rare-earth policy proxy fade
011810 / STX / resource-trading policy beta fade
```

Data-quality note:

```text
All three rows are stock-web calibration usable by profile-level corporate-action candidates or post-CA entry.
All three rows are source_proxy_only=true / evidence_url_pending=true.
011810 has a 2024-01-05 corporate-action candidate, but the selected entry is 2024-02-16 after that event.
```

## Research thesis

C16 is not “strategic resource headline went up.”

The mechanism must be:

```text
strategic resource policy / supply shock
→ direct resource supply, processing capacity or offtake
→ customer / inventory / delivery visibility
→ margin conversion
→ durable rerating
```

A resource headline is a map with a red circle.  
The bridge is the mine, processor, offtake and margin actually connected.

---

## Case 1 — Positive candidate: 081150 / 티플랙스

### Evidence status

```text
source_proxy_only = true
evidence_url_pending = true
source_repair_required = true
```

The source-repair task is rare-metal/stainless/nickel processing, direct supply, customer demand and margin evidence.

```text
evidence_family = RARE_METAL_STAINLESS_NICKEL_PROCESSING_DIRECT_SUPPLY_CUSTOMER_MARGIN_BRIDGE
case_role = positive_with_low_MAE_source_repair
trigger_date = 2024-10-09
entry_date = 2024-10-10
entry_price = 2,700
```

### Stock-Web price path

Observed rows from `atlas/ohlcv_tradable_by_symbol_year/081/081150/2024.csv` and `2025.csv`:

```text
2024-10-10,2700,3290,2700,3180
2024-11-15,3260,3425,2920,2920
2024-12-09,2850,2890,2645,2645
2025-02-03,3185,3615,3075,3245
2025-04-16,3380,3675,3215,3230
2025-05-23,3160,3160,3050,3065
```

### Backtest

```text
MFE_30D  = +26.85%
MAE_30D  = -1.85%
MFE_90D  = +33.89%
MAE_90D  = -2.04%
MFE_180D = +36.11%
MAE_180D = -2.04%
peak_180 = 3,675 on 2025-04-16
trough_180 = 2,645 on 2024-12-09
peak_to_later_drawdown = -17.01%
```

### Interpretation

This is the positive side of C16.  
The price path is not a one-day policy spike. MAE stayed controlled and follow-through continued into 2025.

But runtime promotion still requires source repair:

```text
direct processing capacity
customer/offtake
inventory/supply evidence
margin bridge
```

---

## Case 2 — Counterexample / local 4B: 000910 / 유니온

### Evidence status

```text
source_proxy_only = true
evidence_url_pending = true
source_repair_required = true
```

This row tests rare-earth policy proxy beta without direct supply, processing or margin bridge.

```text
evidence_family = RARE_EARTH_RESOURCE_POLICY_PROXY_WITH_WEAK_DIRECT_SUPPLY_MARGIN_BRIDGE
case_role = counterexample_policy_proxy_local4b
trigger_date = 2024-01-04
entry_date = 2024-01-05
entry_price = 6,100
```

### Stock-Web price path

Observed rows from `atlas/ohlcv_tradable_by_symbol_year/000/000910/2024.csv`:

```text
2024-01-05,6100,6110,5650,5650
2024-01-10,6290,6580,5820,5840
2024-02-01,5400,5490,5370,5420
2024-04-01,5120,5180,5100,5160
2024-08-05,4705,4750,3360,4100
```

### Backtest

```text
MFE_30D  = +7.87%
MAE_30D  = -11.97%
MFE_90D  = +7.87%
MAE_90D  = -16.07%
MFE_180D = +7.87%
MAE_180D = -44.92%
peak_180 = 6,580 on 2024-01-10
trough_180 = 3,360 on 2024-08-05
peak_to_later_drawdown = -48.94%
```

### Interpretation

This is the policy-proxy failure.  
The first move was too small and the later drawdown too large.

C16 should not call rare-earth proxy exposure Green unless actual supply, processing, customer or margin bridge exists.

---

## Case 3 — Counterexample / local 4B: 011810 / STX

### Evidence status

```text
source_proxy_only = true
evidence_url_pending = true
source_repair_required = true
```

This row tests nickel/lithium/resource-trading policy beta without named offtake, supply or margin bridge.

```text
evidence_family = NICKEL_LITHIUM_RESOURCE_TRADING_POLICY_BETA_WITH_WEAK_OFFTAKE_SUPPLY_MARGIN_BRIDGE
case_role = counterexample_resource_trading_local4b
trigger_date = 2024-02-15
entry_date = 2024-02-16
entry_price = 10,470
```

### Stock-Web price path

Observed rows from `atlas/ohlcv_tradable_by_symbol_year/011/011810/2024.csv`:

```text
2024-02-16,10470,11900,10470,10950
2024-03-11,8510,8750,8370,8540
2024-04-18,7070,8330,7070,7640
2024-06-04,8140,9080,7850,7920
2024-08-05,6230,6230,5000,5380
2024-10-25,4835,4940,4700,4940
2024-12-09,4030,4150,3945,3945
```

### Backtest

```text
MFE_30D  = +13.66%
MAE_30D  = -20.06%
MFE_90D  = +13.66%
MAE_90D  = -32.47%
MFE_180D = +13.66%
MAE_180D = -55.11%
peak_180 = 11,900 on 2024-02-16
trough_180 = 4,700 on 2024-10-25
peak_to_later_drawdown = -66.85%
```

### Interpretation

This is resource-trading beta fade.  
The price path says policy/resource heat did not become a durable offtake or margin rerating.

Correct treatment:

```text
false Stage2 / local 4B-watch
```

not hard 4C, unless non-price financing, supply-chain, offtake or margin-break evidence appears.

---

## Cross-case residual finding

### What this strengthens

```text
stage2_required_bridge = strengthen
price_only_blowoff_blocks_positive_stage = strengthen
local_4b_watch_guard = strengthen
full_4b_requires_non_price_evidence = keep
```

### What this does not justify

```text
do_not_raise_generic_C16_resource_policy_weight = true
do_not_treat_all_rare_earth_or_resource_policy_beta_as_Green = true
do_not_convert_resource_proxy_drawdown_to_hard_4C_without_non_price_break = true
```

### Candidate canonical compression

Fine labels can compress into:

```text
RARE_METAL_PROCESSING_DIRECT_SUPPLY_BRIDGE_VS_RESOURCE_POLICY_PROXY_BETA_FADE
```

This fine archetype covers:

```text
1. rare-metal processing/direct supply bridge → Stage2 possible after source repair
2. rare-earth policy proxy without supply/margin bridge → false Stage2 / local 4B
3. resource-trading/of-take policy beta without direct bridge → false Stage2 / local 4B
```

---

## Machine-readable rows

### price source validation row

```jsonl
{"row_type": "price_source_validation", "source": "Songdaiki/stock-web", "source_url": "https://github.com/Songdaiki/stock-web", "manifest_path": "atlas/manifest.json", "schema_path": "atlas/schema.json", "universe_path": "atlas/universe/all_symbols.csv", "manifest_max_date": "2026-02-20", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "raw_shard_root": "atlas/ohlcv_raw_by_symbol_year", "validation_status": "usable_for_historical_calibration"}
```

### case rows

```jsonl
{"row_type": "case", "case_id": "R4L75-C16-081150-TFLEX-RARE-METAL-PROCESSING-SUPPLY-BRIDGE", "symbol": "081150", "company_name": "티플랙스", "round": "R4", "loop": "75", "large_sector_id": "L4_MATERIALS_SPREAD_RESOURCE", "canonical_archetype_id": "C16_STRATEGIC_RESOURCE_POLICY_SUPPLY", "fine_archetype_id": "RARE_METAL_PROCESSING_DIRECT_SUPPLY_BRIDGE_VS_RESOURCE_POLICY_PROXY_BETA_FADE", "case_type": "strategic_resource_policy_supply", "positive_or_counterexample": "positive", "best_trigger": "Stage2-Actionable-RareMetalProcessingSupplyBridge", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 0.5, "score_price_alignment": "C16 should allow Stage2 when strategic-resource policy heat connects to real rare-metal processing, customer demand, inventory/supply and margin bridge. T-Flex produced controlled-MAE follow-through and later 2025 highs, but runtime promotion still requires non-proxy customer/supply evidence.", "current_profile_verdict": "source_repair_required_before_runtime_weight", "price_source": "Songdaiki/stock-web", "notes": "Stock-web path usable; non-proxy resource supply, processing capacity, offtake/customer, inventory and margin evidence required before runtime promotion."}
{"row_type": "case", "case_id": "R4L75-C16-000910-UNION-RARE-EARTH-POLICY-PROXY-FADE", "symbol": "000910", "company_name": "유니온", "round": "R4", "loop": "75", "large_sector_id": "L4_MATERIALS_SPREAD_RESOURCE", "canonical_archetype_id": "C16_STRATEGIC_RESOURCE_POLICY_SUPPLY", "fine_archetype_id": "RARE_METAL_PROCESSING_DIRECT_SUPPLY_BRIDGE_VS_RESOURCE_POLICY_PROXY_BETA_FADE", "case_type": "strategic_resource_policy_supply", "positive_or_counterexample": "counterexample", "best_trigger": "Stage2-FalsePositive / RareEarthPolicyProxyFade", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 0.5, "score_price_alignment": "C16 should not treat rare-earth or resource policy proxy beta as durable Stage2 unless direct resource supply, processing capacity, customer contract or margin bridge is visible. Union had only modest MFE and later deep MAE/drawdown.", "current_profile_verdict": "source_repair_required_before_runtime_weight", "price_source": "Songdaiki/stock-web", "notes": "Stock-web path usable; non-proxy resource supply, processing capacity, offtake/customer, inventory and margin evidence required before runtime promotion."}
{"row_type": "case", "case_id": "R4L75-C16-011810-STX-RESOURCE-TRADING-POLICY-BETA-FADE", "symbol": "011810", "company_name": "STX", "round": "R4", "loop": "75", "large_sector_id": "L4_MATERIALS_SPREAD_RESOURCE", "canonical_archetype_id": "C16_STRATEGIC_RESOURCE_POLICY_SUPPLY", "fine_archetype_id": "RARE_METAL_PROCESSING_DIRECT_SUPPLY_BRIDGE_VS_RESOURCE_POLICY_PROXY_BETA_FADE", "case_type": "strategic_resource_policy_supply", "positive_or_counterexample": "counterexample", "best_trigger": "Stage2-FalsePositive / ResourceTradingPolicyBetaFade", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 0.5, "score_price_alignment": "C16 should not treat resource trading or offtake-policy beta as durable Stage2 unless named supply/offtake, inventory, customer and margin bridge is visible. STX had a short spike but then opened a long high-MAE drawdown path.", "current_profile_verdict": "source_repair_required_before_runtime_weight", "price_source": "Songdaiki/stock-web", "notes": "Stock-web path usable; non-proxy resource supply, processing capacity, offtake/customer, inventory and margin evidence required before runtime promotion."}
```

### trigger rows

```jsonl
{"row_type": "trigger", "trigger_id": "TRG_R4L75-C16-081150-TFLEX-RARE-METAL-PROCESSING-SUPPLY-BRIDGE", "case_id": "R4L75-C16-081150-TFLEX-RARE-METAL-PROCESSING-SUPPLY-BRIDGE", "symbol": "081150", "company_name": "티플랙스", "round": "R4", "loop": "75", "large_sector_id": "L4_MATERIALS_SPREAD_RESOURCE", "canonical_archetype_id": "C16_STRATEGIC_RESOURCE_POLICY_SUPPLY", "fine_archetype_id": "RARE_METAL_PROCESSING_DIRECT_SUPPLY_BRIDGE_VS_RESOURCE_POLICY_PROXY_BETA_FADE", "loop_objective": "coverage_gap_fill|counterexample_mining|strategic_resource_policy_supply_guardrail", "trigger_type": "Stage2-Actionable-RareMetalProcessingSupplyBridge", "trigger_date": "2024-10-09", "entry_date": "2024-10-10", "entry_price": 2700.0, "evidence_available_at_that_date": "RARE_METAL_STAINLESS_NICKEL_PROCESSING_DIRECT_SUPPLY_CUSTOMER_MARGIN_BRIDGE", "evidence_source": "source_proxy_manual_verification_required:TFLEX_2024_RARE_METAL_PROCESSING_NICKEL_STAINLESS_CUSTOMER_SUPPLY_MARGIN_BRIDGE", "stage2_evidence_fields": ["strategic_resource_policy", "direct_supply_or_processing_candidate", "offtake_customer_margin_bridge_candidate"], "stage3_evidence_fields": ["relative_strength", "inventory_supply_or_margin_conversion_candidate"], "stage4b_evidence_fields": ["policy_proxy_beta", "bridge_stale_or_absent", "MAE_widening", "post_peak_drawdown"], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/081/081150/2024.csv", "profile_path": "atlas/symbol_profiles/081/081150.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": 26.85, "MFE_90D_pct": 33.89, "MFE_180D_pct": 36.11, "MAE_30D_pct": -1.85, "MAE_90D_pct": -2.04, "MAE_180D_pct": -2.04, "peak_date": "2025-04-16", "peak_price": 3675.0, "drawdown_after_peak_pct": -17.01, "green_lateness_ratio": null, "four_b_local_peak_proximity": "local_4b_watch_after_resource_policy_or_supply_peak_if_bridge_fades", "four_b_full_window_peak_proximity": "full_4b_requires_non_price_offtake_supply_customer_inventory_or_margin_break", "trigger_outcome_label": "positive_with_low_MAE_source_repair", "current_profile_verdict": "C16 should allow Stage2 when strategic-resource policy heat connects to real rare-metal processing, customer demand, inventory/supply and margin bridge. T-Flex produced controlled-MAE follow-through and later 2025 highs, but runtime promotion still requires non-proxy customer/supply evidence.", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window_by_profile_or_after_CA", "share_count_change_inside_window": false, "same_entry_group_id": "C16_STRATEGIC_RESOURCE_081150_2024-10-10", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 0.5, "do_not_count_as_new_case": false, "source_proxy_only": true, "evidence_url_pending": true}
{"row_type": "trigger", "trigger_id": "TRG_R4L75-C16-000910-UNION-RARE-EARTH-POLICY-PROXY-FADE", "case_id": "R4L75-C16-000910-UNION-RARE-EARTH-POLICY-PROXY-FADE", "symbol": "000910", "company_name": "유니온", "round": "R4", "loop": "75", "large_sector_id": "L4_MATERIALS_SPREAD_RESOURCE", "canonical_archetype_id": "C16_STRATEGIC_RESOURCE_POLICY_SUPPLY", "fine_archetype_id": "RARE_METAL_PROCESSING_DIRECT_SUPPLY_BRIDGE_VS_RESOURCE_POLICY_PROXY_BETA_FADE", "loop_objective": "coverage_gap_fill|counterexample_mining|strategic_resource_policy_supply_guardrail", "trigger_type": "Stage2-FalsePositive / RareEarthPolicyProxyFade", "trigger_date": "2024-01-04", "entry_date": "2024-01-05", "entry_price": 6100.0, "evidence_available_at_that_date": "RARE_EARTH_RESOURCE_POLICY_PROXY_WITH_WEAK_DIRECT_SUPPLY_MARGIN_BRIDGE", "evidence_source": "source_proxy_manual_verification_required:UNION_2024_RARE_EARTH_RESOURCE_POLICY_DIRECT_SUPPLY_PROCESSING_MARGIN_BRIDGE", "stage2_evidence_fields": ["strategic_resource_policy", "direct_supply_or_processing_candidate", "offtake_customer_margin_bridge_candidate"], "stage3_evidence_fields": ["relative_strength", "inventory_supply_or_margin_conversion_candidate"], "stage4b_evidence_fields": ["policy_proxy_beta", "bridge_stale_or_absent", "MAE_widening", "post_peak_drawdown"], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/000/000910/2024.csv", "profile_path": "atlas/symbol_profiles/000/000910.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": 7.87, "MFE_90D_pct": 7.87, "MFE_180D_pct": 7.87, "MAE_30D_pct": -11.97, "MAE_90D_pct": -16.07, "MAE_180D_pct": -44.92, "peak_date": "2024-01-10", "peak_price": 6580.0, "drawdown_after_peak_pct": -48.94, "green_lateness_ratio": null, "four_b_local_peak_proximity": "local_4b_watch_after_resource_policy_or_supply_peak_if_bridge_fades", "four_b_full_window_peak_proximity": "full_4b_requires_non_price_offtake_supply_customer_inventory_or_margin_break", "trigger_outcome_label": "counterexample_policy_proxy_local4b", "current_profile_verdict": "C16 should not treat rare-earth or resource policy proxy beta as durable Stage2 unless direct resource supply, processing capacity, customer contract or margin bridge is visible. Union had only modest MFE and later deep MAE/drawdown.", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window_by_profile_or_after_CA", "share_count_change_inside_window": false, "same_entry_group_id": "C16_STRATEGIC_RESOURCE_000910_2024-01-05", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 0.5, "do_not_count_as_new_case": false, "source_proxy_only": true, "evidence_url_pending": true}
{"row_type": "trigger", "trigger_id": "TRG_R4L75-C16-011810-STX-RESOURCE-TRADING-POLICY-BETA-FADE", "case_id": "R4L75-C16-011810-STX-RESOURCE-TRADING-POLICY-BETA-FADE", "symbol": "011810", "company_name": "STX", "round": "R4", "loop": "75", "large_sector_id": "L4_MATERIALS_SPREAD_RESOURCE", "canonical_archetype_id": "C16_STRATEGIC_RESOURCE_POLICY_SUPPLY", "fine_archetype_id": "RARE_METAL_PROCESSING_DIRECT_SUPPLY_BRIDGE_VS_RESOURCE_POLICY_PROXY_BETA_FADE", "loop_objective": "coverage_gap_fill|counterexample_mining|strategic_resource_policy_supply_guardrail", "trigger_type": "Stage2-FalsePositive / ResourceTradingPolicyBetaFade", "trigger_date": "2024-02-15", "entry_date": "2024-02-16", "entry_price": 10470.0, "evidence_available_at_that_date": "NICKEL_LITHIUM_RESOURCE_TRADING_POLICY_BETA_WITH_WEAK_OFFTAKE_SUPPLY_MARGIN_BRIDGE", "evidence_source": "source_proxy_manual_verification_required:STX_2024_NICKEL_LITHIUM_RESOURCE_TRADING_OFFTAKE_SUPPLY_MARGIN_BRIDGE", "stage2_evidence_fields": ["strategic_resource_policy", "direct_supply_or_processing_candidate", "offtake_customer_margin_bridge_candidate"], "stage3_evidence_fields": ["relative_strength", "inventory_supply_or_margin_conversion_candidate"], "stage4b_evidence_fields": ["policy_proxy_beta", "bridge_stale_or_absent", "MAE_widening", "post_peak_drawdown"], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/011/011810/2024.csv", "profile_path": "atlas/symbol_profiles/011/011810.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": 13.66, "MFE_90D_pct": 13.66, "MFE_180D_pct": 13.66, "MAE_30D_pct": -20.06, "MAE_90D_pct": -32.47, "MAE_180D_pct": -55.11, "peak_date": "2024-02-16", "peak_price": 11900.0, "drawdown_after_peak_pct": -66.85, "green_lateness_ratio": null, "four_b_local_peak_proximity": "local_4b_watch_after_resource_policy_or_supply_peak_if_bridge_fades", "four_b_full_window_peak_proximity": "full_4b_requires_non_price_offtake_supply_customer_inventory_or_margin_break", "trigger_outcome_label": "counterexample_resource_trading_local4b", "current_profile_verdict": "C16 should not treat resource trading or offtake-policy beta as durable Stage2 unless named supply/offtake, inventory, customer and margin bridge is visible. STX had a short spike but then opened a long high-MAE drawdown path.", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window_by_profile_or_after_CA", "share_count_change_inside_window": false, "same_entry_group_id": "C16_STRATEGIC_RESOURCE_011810_2024-02-16", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 0.5, "do_not_count_as_new_case": false, "source_proxy_only": true, "evidence_url_pending": true}
```

### score simulation rows

```jsonl
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R4L75-C16-081150-TFLEX-RARE-METAL-PROCESSING-SUPPLY-BRIDGE", "trigger_id": "TRG_R4L75-C16-081150-TFLEX-RARE-METAL-PROCESSING-SUPPLY-BRIDGE", "symbol": "081150", "large_sector_id": "L4_MATERIALS_SPREAD_RESOURCE", "canonical_archetype_id": "C16_STRATEGIC_RESOURCE_POLICY_SUPPLY", "raw_component_scores_before": {"policy_or_regulatory_score": 12, "direct_supply_processing_score": 13, "offtake_customer_score": 11, "inventory_supply_chain_score": 10, "margin_bridge_score": 11, "relative_strength_score": 13, "execution_risk_score": 6, "source_confidence_score": 2}, "weighted_score_before": 80, "stage_label_before": "Stage2-Actionable after source repair", "raw_component_scores_after": {"policy_or_regulatory_score": 8, "direct_supply_processing_score": 15, "offtake_customer_score": 13, "inventory_supply_chain_score": 12, "margin_bridge_score": 13, "relative_strength_score": 13, "execution_risk_score": 6, "source_confidence_score": 2}, "weighted_score_after": 86, "stage_label_after": "Stage2/Yellow candidate after source repair", "changed_components": ["policy_or_regulatory_score", "direct_supply_processing_score", "offtake_customer_score", "margin_bridge_score", "execution_risk_score"], "component_delta_explanation": "Reward only verified strategic-resource direct supply, processing capacity, offtake/customer and margin bridge; cap policy-proxy beta when bridge evidence fails to refresh.", "MFE_90D_pct": 33.89, "MAE_90D_pct": -2.04, "score_return_alignment_label": "aligned_positive_with_source_repair", "current_profile_verdict": "C16 should allow Stage2 when strategic-resource policy heat connects to real rare-metal processing, customer demand, inventory/supply and margin bridge. T-Flex produced controlled-MAE follow-through and later 2025 highs, but runtime promotion still requires non-proxy customer/supply evidence."}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R4L75-C16-000910-UNION-RARE-EARTH-POLICY-PROXY-FADE", "trigger_id": "TRG_R4L75-C16-000910-UNION-RARE-EARTH-POLICY-PROXY-FADE", "symbol": "000910", "large_sector_id": "L4_MATERIALS_SPREAD_RESOURCE", "canonical_archetype_id": "C16_STRATEGIC_RESOURCE_POLICY_SUPPLY", "raw_component_scores_before": {"policy_or_regulatory_score": 12, "direct_supply_processing_score": 4, "offtake_customer_score": 2, "inventory_supply_chain_score": 3, "margin_bridge_score": 2, "relative_strength_score": 5, "execution_risk_score": 18, "source_confidence_score": 2}, "weighted_score_before": 50, "stage_label_before": "Stage2-FalsePositive / local 4B-watch", "raw_component_scores_after": {"policy_or_regulatory_score": 8, "direct_supply_processing_score": 2, "offtake_customer_score": 1, "inventory_supply_chain_score": 2, "margin_bridge_score": 1, "relative_strength_score": 3, "execution_risk_score": 20, "source_confidence_score": 2}, "weighted_score_after": 39, "stage_label_after": "Stage4B-local-watch / no durable Green", "changed_components": ["policy_or_regulatory_score", "direct_supply_processing_score", "offtake_customer_score", "margin_bridge_score", "execution_risk_score"], "component_delta_explanation": "Reward only verified strategic-resource direct supply, processing capacity, offtake/customer and margin bridge; cap policy-proxy beta when bridge evidence fails to refresh.", "MFE_90D_pct": 7.87, "MAE_90D_pct": -16.07, "score_return_alignment_label": "false_positive_resource_policy_proxy_bridge_gap", "current_profile_verdict": "C16 should not treat rare-earth or resource policy proxy beta as durable Stage2 unless direct resource supply, processing capacity, customer contract or margin bridge is visible. Union had only modest MFE and later deep MAE/drawdown."}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R4L75-C16-011810-STX-RESOURCE-TRADING-POLICY-BETA-FADE", "trigger_id": "TRG_R4L75-C16-011810-STX-RESOURCE-TRADING-POLICY-BETA-FADE", "symbol": "011810", "large_sector_id": "L4_MATERIALS_SPREAD_RESOURCE", "canonical_archetype_id": "C16_STRATEGIC_RESOURCE_POLICY_SUPPLY", "raw_component_scores_before": {"policy_or_regulatory_score": 12, "direct_supply_processing_score": 4, "offtake_customer_score": 2, "inventory_supply_chain_score": 3, "margin_bridge_score": 2, "relative_strength_score": 5, "execution_risk_score": 18, "source_confidence_score": 2}, "weighted_score_before": 50, "stage_label_before": "Stage2-FalsePositive / local 4B-watch", "raw_component_scores_after": {"policy_or_regulatory_score": 8, "direct_supply_processing_score": 2, "offtake_customer_score": 1, "inventory_supply_chain_score": 2, "margin_bridge_score": 1, "relative_strength_score": 3, "execution_risk_score": 20, "source_confidence_score": 2}, "weighted_score_after": 39, "stage_label_after": "Stage4B-local-watch / no durable Green", "changed_components": ["policy_or_regulatory_score", "direct_supply_processing_score", "offtake_customer_score", "margin_bridge_score", "execution_risk_score"], "component_delta_explanation": "Reward only verified strategic-resource direct supply, processing capacity, offtake/customer and margin bridge; cap policy-proxy beta when bridge evidence fails to refresh.", "MFE_90D_pct": 13.66, "MAE_90D_pct": -32.47, "score_return_alignment_label": "false_positive_resource_policy_proxy_bridge_gap", "current_profile_verdict": "C16 should not treat resource trading or offtake-policy beta as durable Stage2 unless named supply/offtake, inventory, customer and margin bridge is visible. STX had a short spike but then opened a long high-MAE drawdown path."}
```

### aggregate row

```jsonl
{"row_type": "aggregate", "round": "R4", "loop": 75, "large_sector_id": "L4_MATERIALS_SPREAD_RESOURCE", "canonical_archetype_id": "C16_STRATEGIC_RESOURCE_POLICY_SUPPLY", "fine_archetype_id": "RARE_METAL_PROCESSING_DIRECT_SUPPLY_BRIDGE_VS_RESOURCE_POLICY_PROXY_BETA_FADE", "calibration_usable_case_count": 3, "calibration_usable_trigger_count": 3, "new_independent_case_count": 3, "reused_case_count": 0, "same_archetype_new_symbol_count": 3, "same_archetype_new_trigger_family_count": 3, "positive_case_count": 1, "counterexample_count": 2, "four_b_case_count": 2, "four_c_case_count": 0, "source_proxy_only_count": 3, "evidence_url_pending_count": 3, "share_count_change_inside_window_count": 0, "current_profile_error_count": 2, "diversity_score_summary": "+3 underused C16 strategic-resource symbols outside top-covered set, +3 rare-metal/rare-earth/resource-trading trigger families, +1 low-MAE processing-supply positive, +2 policy-proxy beta fade local-4B counterexamples, no hard duplicate", "residual_contribution_label": "coverage_gap_fill_with_source_repair_needed"}
```

### shadow weight row

```jsonl
{"row_type": "shadow_weight", "round": "R4", "loop": 75, "large_sector_id": "L4_MATERIALS_SPREAD_RESOURCE", "canonical_archetype_id": "C16_STRATEGIC_RESOURCE_POLICY_SUPPLY", "axis": "rare_metal_processing_direct_supply_bridge_vs_resource_policy_proxy_beta_fade", "decision": "hold_for_source_repair_and_more_evidence", "proposed_runtime_effect": "C16 should split verified strategic-resource direct supply/processing/offtake bridge from rare-earth or resource-policy proxy beta. Stage2 requires direct supply, processing capacity, customer/offtake, inventory or margin bridge. If MFE fades and MAE/post-peak drawdown opens without bridge refresh, route to local 4B-watch.", "do_not_propose_new_weight_delta": true, "needs_more_evidence": true, "source_repair_required": ["081150", "000910", "011810"]}
```

### residual contribution row

```jsonl
{"row_type": "residual_contribution", "round": "R4", "loop": 75, "large_sector_id": "L4_MATERIALS_SPREAD_RESOURCE", "canonical_archetype_id": "C16_STRATEGIC_RESOURCE_POLICY_SUPPLY", "existing_axis_strengthened": ["stage2_required_bridge", "price_only_blowoff_blocks_positive_stage", "local_4b_watch_guard", "full_4b_requires_non_price_evidence"], "new_axis_proposed": null, "sector_specific_rule_candidate": true, "canonical_archetype_rule_candidate": true, "narrative_summary": "C16 needs direct strategic-resource supply proof. T-Flex shows a controlled-MAE rare-metal processing candidate after source repair; Union and STX show rare-earth/resource-trading policy proxy beta fading into local 4B when direct supply/offtake/margin bridge is absent."}
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
081150:
  corporate_action_candidate_dates = 2012-10-04, 2012-10-25
  selected window = 2024-10-10~D+180
  contamination = false

000910:
  corporate_action_candidate_dates = 1997-01-03, 2008-05-07
  selected window = 2024-01-05~D+180
  contamination = false

011810:
  corporate_action_candidate_dates includes 2024-01-05
  selected window = 2024-02-16~D+180, after 2024-01-05 action
  contamination = false by selected post-CA entry
```

Data-quality caveat:

```text
All selected C16 rows are source_proxy_only / evidence_url_pending.
This MD is useful for stock-web path calibration and C16 rule-shape discovery,
but coding-agent promotion requires non-proxy direct supply, processing capacity, offtake/customer, inventory and margin evidence.
```

---

## Deferred Coding Agent Handoff Prompt

Do not execute this now.

```text
You are the coding agent for Songdaiki/stock_agent.

Read this standalone v12 residual research MD and ingest machine-readable rows only after validation.

Do not patch production scoring blindly.
This R4/C16 artifact is marked do_not_propose_new_weight_delta=true because all rows need source repair.

Candidate axis:
rare_metal_processing_direct_supply_bridge_vs_resource_policy_proxy_beta_fade

Required checks before implementation:
1. Validate all trigger rows against stock-web tradable_raw OHLC shards.
2. Confirm no hard duplicate key:
   canonical_archetype_id + symbol + trigger_type + entry_date.
3. Verify non-proxy source URLs for 081150, 000910 and 011810.
4. Validate 011810 entry is treated after the 2024-01-05 corporate-action candidate.
5. Keep generic C16 strategic-resource policy weight unchanged until source repair is complete.
6. Consider Stage2 only when:
   - strategic-resource policy/supply shock is explicit,
   - direct supply, processing capacity or offtake bridge is visible,
   - customer, inventory, delivery or margin bridge exists,
   - MAE remains controlled or the signal is lifecycle-managed.
7. Consider local 4B-watch when:
   - the trigger is rare-earth/resource policy proxy beta only,
   - supply/offtake/customer/margin bridge is weak or stale,
   - MAE_90D <= -20% or MAE_180D <= -25%,
   - post-peak drawdown <= -35%.
8. Do not convert local 4B-watch into full 4B/4C without non-price supply-chain break, offtake loss, financing/liquidity break, inventory impairment or margin collapse.
9. Emit before/after diagnostics and reject if verified rare-metal processing positives are overblocked.
```

---

## Final round state

```text
completed_round = R4
completed_loop = 75
next_round = R5
next_loop = 75
round_schedule_status = valid
round_sector_consistency = pass
```

