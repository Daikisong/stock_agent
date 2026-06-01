# E2R Stock-Web v12 Residual Research — R3 Loop 75 / L3 / C12

## Metadata

```json
{
  "research_session": "post_calibrated_sector_archetype_residual_research",
  "mode": "historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12",
  "scheduled_round": "R3",
  "scheduled_loop": 75,
  "round_schedule_status": "valid",
  "round_sector_consistency": "pass",
  "completed_round": "R3",
  "completed_loop": 75,
  "computed_next_round": "R4",
  "computed_next_loop": 75,
  "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY",
  "canonical_archetype_id": "C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK",
  "fine_archetype_id": "COPPER_FOIL_SEPARATOR_AL_FOIL_CUSTOMER_CONTRACT_BRIDGE_VS_CALLOFF_BETA_FADE",
  "loop_objective": [
    "coverage_gap_fill",
    "counterexample_mining",
    "4B_non_price_requirement_stress_test",
    "customer_contract_calloff_guardrail",
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

Previous completed state in this interactive run: R2 / loop 75.

Therefore:

```text
scheduled_round = R3
scheduled_loop = 75
allowed_large_sector = L3_BATTERY_EV_GREEN_MOBILITY
selected_large_sector = L3_BATTERY_EV_GREEN_MOBILITY
selected_canonical_archetype_id = C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK
computed_next_round = R4
computed_next_loop = 75
```

R3 was routed to C12 because loop 74 used C11 and loop 73 used C14.  
This file tests customer contract / call-off cadence rather than generic battery orderbook or EV slowdown.

## No-Repeat / novelty check

No hard duplicate is intentionally reused.

Hard duplicate key checked conceptually:

```text
canonical_archetype_id + symbol + trigger_type + entry_date
```

No-Repeat shows C12 is concentrated in:

```text
UNKNOWN_SYMBOL, 247540, 278280, 003670, 005070
```

This run uses three different symbols:

```text
020150 / 롯데에너지머티리얼즈 / copper-foil customer contract bridge
361610 / SK아이이테크놀로지 / separator customer call-off risk
006110 / 삼아알미늄 / aluminum-foil contract beta fade
```

Data-quality note:

```text
All three rows are stock-web calibration usable by profile-level corporate-action candidates.
All three rows are source_proxy_only=true / evidence_url_pending=true.
No selected row has a profile-level 2024 corporate-action candidate.
```

## Research thesis

C12 is not “battery material stock went up.”

The mechanism is:

```text
customer contract
→ call-off cadence
→ utilization / delivery / ASP
→ margin conversion
→ durable rerating
```

A long-term contract is the umbrella.  
The call-off schedule is whether it actually rains revenue.

---

## Case 1 — Positive with lifecycle 4B: 020150 / 롯데에너지머티리얼즈

### Evidence status

```text
source_proxy_only = true
evidence_url_pending = true
source_repair_required = true
```

The source-repair task is copper-foil customer contract, capacity, call-off/delivery schedule and margin bridge evidence.

```text
evidence_family = COPPER_FOIL_CUSTOMER_LONG_TERM_CONTRACT_CAPACITY_DELIVERY_MARGIN_BRIDGE
case_role = positive_with_later_4b_watch
trigger_date = 2024-01-31
entry_date = 2024-02-01
entry_price = 31,250
```

### Stock-Web price path

Observed rows from `atlas/ohlcv_tradable_by_symbol_year/020/020150/2024.csv`:

```text
2024-02-01,31250,32850,31000,32700
2024-03-13,39950,40950,39400,39900
2024-03-21,43000,49200,42850,47050
2024-08-05,36100,36750,30500,32200
2024-09-05,40050,45650,40050,43000
2024-12-09,22100,22400,20900,21000
```

### Backtest

```text
MFE_30D  = +31.04%
MAE_30D  = -0.80%
MFE_90D  = +57.44%
MAE_90D  = -0.80%
MFE_180D = +57.44%
MAE_180D = -2.40%
peak_180 = 49,200 on 2024-03-21
trough_180 = 30,500 on 2024-08-05
peak_to_later_drawdown = -57.52%
```

### Interpretation

This is the C12 positive side.  
The initial path says a customer-contract and capacity bridge could be real. But the later collapse says a stale contract headline is not enough.

Correct treatment:

```text
verified call-off / utilization / margin bridge → Stage2 possible
bridge stale or call-off risk opens → lifecycle local 4B-watch
```

---

## Case 2 — Counterexample / local 4B: 361610 / SK아이이테크놀로지

### Evidence status

```text
source_proxy_only = true
evidence_url_pending = true
source_repair_required = true
```

This row tests separator customer call-off and utilization risk.

```text
evidence_family = SEPARATOR_CUSTOMER_CALLOFF_UTILIZATION_EV_SLOWDOWN_MARGIN_RISK
case_role = counterexample_calloff_local4b
trigger_date = 2024-01-31
entry_date = 2024-02-01
entry_price = 73,400
```

### Stock-Web price path

Observed rows from `atlas/ohlcv_tradable_by_symbol_year/361/361610/2024.csv`:

```text
2024-02-01,73400,74800,73400,74800
2024-02-02,75500,80800,74600,76000
2024-02-06,67200,68200,65100,65500
2024-08-05,36000,36200,30950,32000
2024-09-10,31750,32100,30050,30050
```

### Backtest

```text
MFE_30D  = +10.08%
MAE_30D  = -11.31%
MFE_90D  = +10.08%
MAE_90D  = -48.84%
MFE_180D = +10.08%
MAE_180D = -59.06%
peak_180 = 80,800 on 2024-02-02
trough_180 = 30,050 on 2024-09-10
peak_to_later_drawdown = -62.81%
```

### Interpretation

This is a clean call-off risk failure.  
The early rebound was small. The later drawdown says customer utilization and margin risk dominated.

C12 should classify this as:

```text
false Stage2 / local 4B-watch
```

unless non-price call-off and utilization evidence is repaired.

---

## Case 3 — Counterexample / local 4B: 006110 / 삼아알미늄

### Evidence status

```text
source_proxy_only = true
evidence_url_pending = true
source_repair_required = true
```

This row tests aluminum-foil contract beta without durable call-off, utilization and margin bridge.

```text
evidence_family = ALUMINUM_FOIL_BATTERY_CUSTOMER_CONTRACT_BETA_WITH_CALLOFF_AND_MARGIN_FADE
case_role = counterexample_calloff_local4b
trigger_date = 2024-01-31
entry_date = 2024-02-01
entry_price = 86,500
```

### Stock-Web price path

Observed rows from `atlas/ohlcv_tradable_by_symbol_year/006/006110/2024.csv`:

```text
2024-02-01,86500,88000,84800,86500
2024-02-16,95000,102400,93700,99500
2024-02-21,110600,116400,110000,110700
2024-08-05,48100,49000,39600,42000
2024-10-10,60000,61200,57700,58700
2024-12-20,36700,36900,34000,34550
```

### Backtest

```text
MFE_30D  = +34.57%
MAE_30D  = -7.28%
MFE_90D  = +34.57%
MAE_90D  = -28.67%
MFE_180D = +34.57%
MAE_180D = -54.22%
peak_180 = 116,400 on 2024-02-21
trough_180 = 39,600 on 2024-08-05
peak_to_later_drawdown = -70.79%
```

### Interpretation

This is the dangerous C12 shape: large MFE first, then severe call-off risk.  
The contract narrative can produce a tradable rally, but without call-off cadence and margin bridge it should not be durable Green.

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
do_not_raise_generic_C12_battery_material_weight = true
do_not_treat_all_customer_contract_MFE_as_Green = true
do_not_convert_battery_material_drawdown_to_hard_4C_without_non_price_customer_or_margin_break = true
```

### Candidate canonical compression

Fine labels can compress into:

```text
COPPER_FOIL_SEPARATOR_AL_FOIL_CUSTOMER_CONTRACT_BRIDGE_VS_CALLOFF_BETA_FADE
```

This fine archetype covers:

```text
1. copper-foil customer contract/capacity bridge → Stage2 possible after source repair
2. separator call-off/utilization risk → false Stage2 / local 4B
3. aluminum-foil contract beta without call-off/margin bridge → false Stage2 / local 4B
```

---

## Machine-readable rows

### price source validation row

```jsonl
{"row_type": "price_source_validation", "source": "Songdaiki/stock-web", "source_url": "https://github.com/Songdaiki/stock-web", "manifest_path": "atlas/manifest.json", "schema_path": "atlas/schema.json", "universe_path": "atlas/universe/all_symbols.csv", "manifest_max_date": "2026-02-20", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "raw_shard_root": "atlas/ohlcv_raw_by_symbol_year", "validation_status": "usable_for_historical_calibration"}
```

### case rows

```jsonl
{"row_type": "case", "case_id": "R3L75-C12-020150-LOTTE-ENERGY-MATERIALS-COPPER-FOIL-CONTRACT-BRIDGE", "symbol": "020150", "company_name": "롯데에너지머티리얼즈", "round": "R3", "loop": "75", "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK", "fine_archetype_id": "COPPER_FOIL_SEPARATOR_AL_FOIL_CUSTOMER_CONTRACT_BRIDGE_VS_CALLOFF_BETA_FADE", "case_type": "battery_customer_contract_calloff_risk", "positive_or_counterexample": "positive", "best_trigger": "Stage2-Actionable-CopperFoilCustomerContractBridgeWithLifecycle4B", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 0.5, "score_price_alignment": "C12 should allow Stage2 when copper-foil customer contracts, delivery schedule, capacity utilization and margin bridge are explicit. Lotte Energy Materials produced high MFE with low entry-basis MAE, but later drawdown shows lifecycle local 4B is needed if customer call-off or margin evidence fades.", "current_profile_verdict": "source_repair_required_before_runtime_weight", "price_source": "Songdaiki/stock-web", "notes": "Stock-web path usable; non-proxy customer contract, call-off cadence, utilization, capacity, delivery and margin evidence required before runtime promotion."}
{"row_type": "case", "case_id": "R3L75-C12-361610-SK-IET-SEPARATOR-CUSTOMER-CALLOFF-RISK", "symbol": "361610", "company_name": "SK아이이테크놀로지", "round": "R3", "loop": "75", "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK", "fine_archetype_id": "COPPER_FOIL_SEPARATOR_AL_FOIL_CUSTOMER_CONTRACT_BRIDGE_VS_CALLOFF_BETA_FADE", "case_type": "battery_customer_contract_calloff_risk", "positive_or_counterexample": "counterexample", "best_trigger": "Stage2-FalsePositive / SeparatorCustomerCalloffRisk", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 0.5, "score_price_alignment": "C12 should not treat separator beta as durable Stage2 unless customer call-off schedule, utilization, pricing and margin evidence refreshes. SK IET had a brief rebound but then opened severe MAE as EV demand and separator utilization risk dominated.", "current_profile_verdict": "source_repair_required_before_runtime_weight", "price_source": "Songdaiki/stock-web", "notes": "Stock-web path usable; non-proxy customer contract, call-off cadence, utilization, capacity, delivery and margin evidence required before runtime promotion."}
{"row_type": "case", "case_id": "R3L75-C12-006110-SAMA-ALUMINIUM-ALFOIL-CONTRACT-BETA-FADE", "symbol": "006110", "company_name": "삼아알미늄", "round": "R3", "loop": "75", "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK", "fine_archetype_id": "COPPER_FOIL_SEPARATOR_AL_FOIL_CUSTOMER_CONTRACT_BRIDGE_VS_CALLOFF_BETA_FADE", "case_type": "battery_customer_contract_calloff_risk", "positive_or_counterexample": "counterexample", "best_trigger": "Stage2-FalsePositive / AluminumFoilContractBetaFade", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 0.5, "score_price_alignment": "C12 should not treat aluminum-foil contract beta as durable Stage2 unless customer order, call-off cadence, utilization and margin bridge remain visible. Sama Aluminium had a strong early MFE but later collapsed, showing call-off and utilization risk.", "current_profile_verdict": "source_repair_required_before_runtime_weight", "price_source": "Songdaiki/stock-web", "notes": "Stock-web path usable; non-proxy customer contract, call-off cadence, utilization, capacity, delivery and margin evidence required before runtime promotion."}
```

### trigger rows

```jsonl
{"row_type": "trigger", "trigger_id": "TRG_R3L75-C12-020150-LOTTE-ENERGY-MATERIALS-COPPER-FOIL-CONTRACT-BRIDGE", "case_id": "R3L75-C12-020150-LOTTE-ENERGY-MATERIALS-COPPER-FOIL-CONTRACT-BRIDGE", "symbol": "020150", "company_name": "롯데에너지머티리얼즈", "round": "R3", "loop": "75", "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK", "fine_archetype_id": "COPPER_FOIL_SEPARATOR_AL_FOIL_CUSTOMER_CONTRACT_BRIDGE_VS_CALLOFF_BETA_FADE", "loop_objective": "coverage_gap_fill|counterexample_mining|customer_contract_calloff_guardrail", "trigger_type": "Stage2-Actionable-CopperFoilCustomerContractBridgeWithLifecycle4B", "trigger_date": "2024-01-31", "entry_date": "2024-02-01", "entry_price": 31250.0, "evidence_available_at_that_date": "COPPER_FOIL_CUSTOMER_LONG_TERM_CONTRACT_CAPACITY_DELIVERY_MARGIN_BRIDGE", "evidence_source": "source_proxy_manual_verification_required:LOTTE_ENERGY_MATERIALS_2024_COPPER_FOIL_CUSTOMER_CONTRACT_CAPACITY_DELIVERY_MARGIN_BRIDGE", "stage2_evidence_fields": ["customer_contract_candidate", "calloff_schedule_candidate", "capacity_utilization_or_delivery_bridge_candidate"], "stage3_evidence_fields": ["relative_strength", "margin_or_ASP_bridge_candidate"], "stage4b_evidence_fields": ["calloff_or_utilization_risk", "bridge_stale_or_absent", "MAE_widening", "post_peak_drawdown"], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/020/020150/2024.csv", "profile_path": "atlas/symbol_profiles/020/020150.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": 31.04, "MFE_90D_pct": 57.44, "MFE_180D_pct": 57.44, "MAE_30D_pct": -0.8, "MAE_90D_pct": -0.8, "MAE_180D_pct": -2.4, "peak_date": "2024-03-21", "peak_price": 49200.0, "drawdown_after_peak_pct": -57.52, "green_lateness_ratio": null, "four_b_local_peak_proximity": "local_4b_watch_after_contract_or_customer_calloff_peak_if_bridge_fades", "four_b_full_window_peak_proximity": "full_4b_requires_non_price_customer_cancellation_calloff_utilization_or_margin_break", "trigger_outcome_label": "positive_with_later_4b_watch", "current_profile_verdict": "C12 should allow Stage2 when copper-foil customer contracts, delivery schedule, capacity utilization and margin bridge are explicit. Lotte Energy Materials produced high MFE with low entry-basis MAE, but later drawdown shows lifecycle local 4B is needed if customer call-off or margin evidence fades.", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window_by_profile", "share_count_change_inside_window": false, "same_entry_group_id": "C12_BATTERY_CALLOFF_020150_2024-02-01", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 0.5, "do_not_count_as_new_case": false, "source_proxy_only": true, "evidence_url_pending": true}
{"row_type": "trigger", "trigger_id": "TRG_R3L75-C12-361610-SK-IET-SEPARATOR-CUSTOMER-CALLOFF-RISK", "case_id": "R3L75-C12-361610-SK-IET-SEPARATOR-CUSTOMER-CALLOFF-RISK", "symbol": "361610", "company_name": "SK아이이테크놀로지", "round": "R3", "loop": "75", "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK", "fine_archetype_id": "COPPER_FOIL_SEPARATOR_AL_FOIL_CUSTOMER_CONTRACT_BRIDGE_VS_CALLOFF_BETA_FADE", "loop_objective": "coverage_gap_fill|counterexample_mining|customer_contract_calloff_guardrail", "trigger_type": "Stage2-FalsePositive / SeparatorCustomerCalloffRisk", "trigger_date": "2024-01-31", "entry_date": "2024-02-01", "entry_price": 73400.0, "evidence_available_at_that_date": "SEPARATOR_CUSTOMER_CALLOFF_UTILIZATION_EV_SLOWDOWN_MARGIN_RISK", "evidence_source": "source_proxy_manual_verification_required:SK_IET_2024_SEPARATOR_CUSTOMER_CALLOFF_UTILIZATION_MARGIN_RISK", "stage2_evidence_fields": ["customer_contract_candidate", "calloff_schedule_candidate", "capacity_utilization_or_delivery_bridge_candidate"], "stage3_evidence_fields": ["relative_strength", "margin_or_ASP_bridge_candidate"], "stage4b_evidence_fields": ["calloff_or_utilization_risk", "bridge_stale_or_absent", "MAE_widening", "post_peak_drawdown"], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/361/361610/2024.csv", "profile_path": "atlas/symbol_profiles/361/361610.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": 10.08, "MFE_90D_pct": 10.08, "MFE_180D_pct": 10.08, "MAE_30D_pct": -11.31, "MAE_90D_pct": -48.84, "MAE_180D_pct": -59.06, "peak_date": "2024-02-02", "peak_price": 80800.0, "drawdown_after_peak_pct": -62.81, "green_lateness_ratio": null, "four_b_local_peak_proximity": "local_4b_watch_after_contract_or_customer_calloff_peak_if_bridge_fades", "four_b_full_window_peak_proximity": "full_4b_requires_non_price_customer_cancellation_calloff_utilization_or_margin_break", "trigger_outcome_label": "counterexample_calloff_local4b", "current_profile_verdict": "C12 should not treat separator beta as durable Stage2 unless customer call-off schedule, utilization, pricing and margin evidence refreshes. SK IET had a brief rebound but then opened severe MAE as EV demand and separator utilization risk dominated.", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window_by_profile", "share_count_change_inside_window": false, "same_entry_group_id": "C12_BATTERY_CALLOFF_361610_2024-02-01", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 0.5, "do_not_count_as_new_case": false, "source_proxy_only": true, "evidence_url_pending": true}
{"row_type": "trigger", "trigger_id": "TRG_R3L75-C12-006110-SAMA-ALUMINIUM-ALFOIL-CONTRACT-BETA-FADE", "case_id": "R3L75-C12-006110-SAMA-ALUMINIUM-ALFOIL-CONTRACT-BETA-FADE", "symbol": "006110", "company_name": "삼아알미늄", "round": "R3", "loop": "75", "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK", "fine_archetype_id": "COPPER_FOIL_SEPARATOR_AL_FOIL_CUSTOMER_CONTRACT_BRIDGE_VS_CALLOFF_BETA_FADE", "loop_objective": "coverage_gap_fill|counterexample_mining|customer_contract_calloff_guardrail", "trigger_type": "Stage2-FalsePositive / AluminumFoilContractBetaFade", "trigger_date": "2024-01-31", "entry_date": "2024-02-01", "entry_price": 86500.0, "evidence_available_at_that_date": "ALUMINUM_FOIL_BATTERY_CUSTOMER_CONTRACT_BETA_WITH_CALLOFF_AND_MARGIN_FADE", "evidence_source": "source_proxy_manual_verification_required:SAMA_ALUMINIUM_2024_BATTERY_AL_FOIL_CUSTOMER_CONTRACT_CALLOFF_MARGIN_BRIDGE", "stage2_evidence_fields": ["customer_contract_candidate", "calloff_schedule_candidate", "capacity_utilization_or_delivery_bridge_candidate"], "stage3_evidence_fields": ["relative_strength", "margin_or_ASP_bridge_candidate"], "stage4b_evidence_fields": ["calloff_or_utilization_risk", "bridge_stale_or_absent", "MAE_widening", "post_peak_drawdown"], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/006/006110/2024.csv", "profile_path": "atlas/symbol_profiles/006/006110.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": 34.57, "MFE_90D_pct": 34.57, "MFE_180D_pct": 34.57, "MAE_30D_pct": -7.28, "MAE_90D_pct": -28.67, "MAE_180D_pct": -54.22, "peak_date": "2024-02-21", "peak_price": 116400.0, "drawdown_after_peak_pct": -70.79, "green_lateness_ratio": null, "four_b_local_peak_proximity": "local_4b_watch_after_contract_or_customer_calloff_peak_if_bridge_fades", "four_b_full_window_peak_proximity": "full_4b_requires_non_price_customer_cancellation_calloff_utilization_or_margin_break", "trigger_outcome_label": "counterexample_calloff_local4b", "current_profile_verdict": "C12 should not treat aluminum-foil contract beta as durable Stage2 unless customer order, call-off cadence, utilization and margin bridge remain visible. Sama Aluminium had a strong early MFE but later collapsed, showing call-off and utilization risk.", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window_by_profile", "share_count_change_inside_window": false, "same_entry_group_id": "C12_BATTERY_CALLOFF_006110_2024-02-01", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 0.5, "do_not_count_as_new_case": false, "source_proxy_only": true, "evidence_url_pending": true}
```

### score simulation rows

```jsonl
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R3L75-C12-020150-LOTTE-ENERGY-MATERIALS-COPPER-FOIL-CONTRACT-BRIDGE", "trigger_id": "TRG_R3L75-C12-020150-LOTTE-ENERGY-MATERIALS-COPPER-FOIL-CONTRACT-BRIDGE", "symbol": "020150", "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK", "raw_component_scores_before": {"customer_contract_score": 14, "calloff_schedule_score": 12, "capacity_utilization_score": 12, "margin_bridge_score": 12, "relative_strength_score": 14, "customer_quality_score": 11, "execution_risk_score": 6, "source_confidence_score": 2}, "weighted_score_before": 82, "stage_label_before": "Stage2-Actionable after source repair", "raw_component_scores_after": {"customer_contract_score": 16, "calloff_schedule_score": 14, "capacity_utilization_score": 13, "margin_bridge_score": 14, "relative_strength_score": 13, "customer_quality_score": 12, "execution_risk_score": 6, "source_confidence_score": 2}, "weighted_score_after": 88, "stage_label_after": "Stage2/Yellow candidate after source repair + lifecycle 4B", "changed_components": ["customer_contract_score", "calloff_schedule_score", "capacity_utilization_score", "margin_bridge_score", "execution_risk_score"], "component_delta_explanation": "Reward only verified customer contract/call-off, utilization, delivery and margin bridge; cap battery material beta when call-off or utilization evidence fails to refresh.", "MFE_90D_pct": 57.44, "MAE_90D_pct": -0.8, "score_return_alignment_label": "aligned_positive_with_lifecycle_4b", "current_profile_verdict": "C12 should allow Stage2 when copper-foil customer contracts, delivery schedule, capacity utilization and margin bridge are explicit. Lotte Energy Materials produced high MFE with low entry-basis MAE, but later drawdown shows lifecycle local 4B is needed if customer call-off or margin evidence fades."}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R3L75-C12-361610-SK-IET-SEPARATOR-CUSTOMER-CALLOFF-RISK", "trigger_id": "TRG_R3L75-C12-361610-SK-IET-SEPARATOR-CUSTOMER-CALLOFF-RISK", "symbol": "361610", "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK", "raw_component_scores_before": {"customer_contract_score": 5, "calloff_schedule_score": 3, "capacity_utilization_score": 3, "margin_bridge_score": 2, "relative_strength_score": 7, "customer_quality_score": 4, "execution_risk_score": 18, "source_confidence_score": 2}, "weighted_score_before": 50, "stage_label_before": "Stage2-FalsePositive / local 4B-watch", "raw_component_scores_after": {"customer_contract_score": 3, "calloff_schedule_score": 1, "capacity_utilization_score": 1, "margin_bridge_score": 1, "relative_strength_score": 4, "customer_quality_score": 3, "execution_risk_score": 20, "source_confidence_score": 2}, "weighted_score_after": 39, "stage_label_after": "Stage4B-local-watch / no durable Green", "changed_components": ["customer_contract_score", "calloff_schedule_score", "capacity_utilization_score", "margin_bridge_score", "execution_risk_score"], "component_delta_explanation": "Reward only verified customer contract/call-off, utilization, delivery and margin bridge; cap battery material beta when call-off or utilization evidence fails to refresh.", "MFE_90D_pct": 10.08, "MAE_90D_pct": -48.84, "score_return_alignment_label": "false_positive_calloff_bridge_gap", "current_profile_verdict": "C12 should not treat separator beta as durable Stage2 unless customer call-off schedule, utilization, pricing and margin evidence refreshes. SK IET had a brief rebound but then opened severe MAE as EV demand and separator utilization risk dominated."}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R3L75-C12-006110-SAMA-ALUMINIUM-ALFOIL-CONTRACT-BETA-FADE", "trigger_id": "TRG_R3L75-C12-006110-SAMA-ALUMINIUM-ALFOIL-CONTRACT-BETA-FADE", "symbol": "006110", "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK", "raw_component_scores_before": {"customer_contract_score": 5, "calloff_schedule_score": 3, "capacity_utilization_score": 3, "margin_bridge_score": 2, "relative_strength_score": 7, "customer_quality_score": 4, "execution_risk_score": 18, "source_confidence_score": 2}, "weighted_score_before": 50, "stage_label_before": "Stage2-FalsePositive / local 4B-watch", "raw_component_scores_after": {"customer_contract_score": 3, "calloff_schedule_score": 1, "capacity_utilization_score": 1, "margin_bridge_score": 1, "relative_strength_score": 4, "customer_quality_score": 3, "execution_risk_score": 20, "source_confidence_score": 2}, "weighted_score_after": 39, "stage_label_after": "Stage4B-local-watch / no durable Green", "changed_components": ["customer_contract_score", "calloff_schedule_score", "capacity_utilization_score", "margin_bridge_score", "execution_risk_score"], "component_delta_explanation": "Reward only verified customer contract/call-off, utilization, delivery and margin bridge; cap battery material beta when call-off or utilization evidence fails to refresh.", "MFE_90D_pct": 34.57, "MAE_90D_pct": -28.67, "score_return_alignment_label": "false_positive_calloff_bridge_gap", "current_profile_verdict": "C12 should not treat aluminum-foil contract beta as durable Stage2 unless customer order, call-off cadence, utilization and margin bridge remain visible. Sama Aluminium had a strong early MFE but later collapsed, showing call-off and utilization risk."}
```

### aggregate row

```jsonl
{"row_type": "aggregate", "round": "R3", "loop": 75, "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK", "fine_archetype_id": "COPPER_FOIL_SEPARATOR_AL_FOIL_CUSTOMER_CONTRACT_BRIDGE_VS_CALLOFF_BETA_FADE", "calibration_usable_case_count": 3, "calibration_usable_trigger_count": 3, "new_independent_case_count": 3, "reused_case_count": 0, "same_archetype_new_symbol_count": 3, "same_archetype_new_trigger_family_count": 3, "positive_case_count": 1, "counterexample_count": 2, "four_b_case_count": 3, "four_c_case_count": 0, "source_proxy_only_count": 3, "evidence_url_pending_count": 3, "share_count_change_inside_window_count": 0, "current_profile_error_count": 2, "diversity_score_summary": "+3 underused/new C12 battery material/component symbols, +3 copper-foil/separator/al-foil call-off trigger families, +1 customer-contract bridge positive, +2 call-off beta fade local-4B counterexamples, no hard duplicate", "residual_contribution_label": "coverage_gap_fill_with_source_repair_needed"}
```

### shadow weight row

```jsonl
{"row_type": "shadow_weight", "round": "R3", "loop": 75, "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK", "axis": "copper_foil_separator_al_foil_customer_contract_bridge_vs_calloff_beta_fade", "decision": "hold_for_source_repair_and_more_evidence", "proposed_runtime_effect": "C12 should split verified battery customer contract/call-off bridges from generic material beta. Stage2 requires customer contract, call-off cadence, utilization, delivery schedule, ASP or margin bridge. If MFE fades and MAE/post-peak drawdown opens without bridge refresh, route to local 4B-watch.", "do_not_propose_new_weight_delta": true, "needs_more_evidence": true, "source_repair_required": ["020150", "361610", "006110"]}
```

### residual contribution row

```jsonl
{"row_type": "residual_contribution", "round": "R3", "loop": 75, "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK", "existing_axis_strengthened": ["stage2_required_bridge", "price_only_blowoff_blocks_positive_stage", "local_4b_watch_guard", "full_4b_requires_non_price_evidence"], "new_axis_proposed": null, "sector_specific_rule_candidate": true, "canonical_archetype_rule_candidate": true, "narrative_summary": "C12 needs customer contract/call-off proof. Lotte Energy Materials shows a copper-foil bridge positive after source repair; SK IET and Sama Aluminium show separator/al-foil contract beta fading into local 4B when call-off, utilization and margin bridge fails."}
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
020150:
  corporate_action_candidate_dates = none
  selected window = 2024-02-01~D+180
  contamination = false

361610:
  corporate_action_candidate_dates = none
  selected window = 2024-02-01~D+180
  contamination = false

006110:
  corporate_action_candidate_dates = 2000-10-16, 2000-11-14, 2007-05-04, 2011-04-26, 2023-02-09
  selected window = 2024-02-01~D+180
  contamination = false
```

Data-quality caveat:

```text
All selected C12 rows are source_proxy_only / evidence_url_pending.
This MD is useful for stock-web path calibration and C12 rule-shape discovery,
but coding-agent promotion requires non-proxy customer contract, call-off cadence, utilization, capacity, delivery, ASP and margin evidence.
```

---

## Deferred Coding Agent Handoff Prompt

Do not execute this now.

```text
You are the coding agent for Songdaiki/stock_agent.

Read this standalone v12 residual research MD and ingest machine-readable rows only after validation.

Do not patch production scoring blindly.
This R3/C12 artifact is marked do_not_propose_new_weight_delta=true because all rows need source repair.

Candidate axis:
copper_foil_separator_al_foil_customer_contract_bridge_vs_calloff_beta_fade

Required checks before implementation:
1. Validate all trigger rows against stock-web tradable_raw OHLC shards.
2. Confirm no hard duplicate key:
   canonical_archetype_id + symbol + trigger_type + entry_date.
3. Verify non-proxy source URLs for 020150, 361610 and 006110.
4. Keep generic C12 battery-material weight unchanged until source repair is complete.
5. Consider Stage2 only when:
   - customer contract is explicit,
   - call-off cadence or delivery schedule is visible,
   - utilization / capacity absorption / ASP bridge exists,
   - margin/revision bridge is credible,
   - MAE remains controlled or the signal is lifecycle-managed.
6. Consider local 4B-watch when:
   - the trigger is battery material/component contract beta only,
   - call-off or utilization evidence is weak/stale,
   - MAE_90D <= -20% or MAE_180D <= -25%,
   - post-peak drawdown <= -35%.
7. Do not convert local 4B-watch into full 4B/4C without non-price customer cancellation, call-off collapse, utilization break, ASP/margin collapse, covenant or financing evidence.
8. Emit before/after diagnostics and reject if verified copper-foil contract positives are overblocked.
```

---

## Final round state

```text
completed_round = R3
completed_loop = 75
next_round = R4
next_loop = 75
round_schedule_status = valid
round_sector_consistency = pass
```

