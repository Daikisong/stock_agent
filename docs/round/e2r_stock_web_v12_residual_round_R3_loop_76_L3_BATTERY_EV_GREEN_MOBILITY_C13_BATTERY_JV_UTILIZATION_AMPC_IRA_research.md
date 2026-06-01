# E2R Stock-Web v12 Residual Research — R3 Loop 76 / L3 / C13

## Metadata

```json
{
  "research_session": "post_calibrated_sector_archetype_residual_research",
  "mode": "historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12",
  "scheduled_round": "R3",
  "scheduled_loop": 76,
  "round_schedule_status": "valid",
  "round_sector_consistency": "pass",
  "completed_round": "R3",
  "completed_loop": 76,
  "computed_next_round": "R4",
  "computed_next_loop": 76,
  "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY",
  "canonical_archetype_id": "C13_BATTERY_JV_UTILIZATION_AMPC_IRA",
  "fine_archetype_id": "US_IRA_AMPC_ELECTROLYTE_CNT_LOCAL_SUPPLY_UTILIZATION_BRIDGE_VS_MATERIAL_UTILIZATION_FADE",
  "loop_objective": [
    "coverage_gap_fill",
    "counterexample_mining",
    "4B_non_price_requirement_stress_test",
    "battery_US_IRA_AMPC_utilization_guardrail",
    "sector_specific_rule_discovery",
    "canonical_archetype_compression",
    "source_repair_queue_creation",
    "share_count_validation_queue_creation"
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

Previous completed state in this interactive run: R2 / loop 76.

Therefore:

```text
scheduled_round = R3
scheduled_loop = 76
allowed_large_sector = L3_BATTERY_EV_GREEN_MOBILITY
selected_large_sector = L3_BATTERY_EV_GREEN_MOBILITY
selected_canonical_archetype_id = C13_BATTERY_JV_UTILIZATION_AMPC_IRA
computed_next_round = R4
computed_next_loop = 76
```

R3 was routed to C13 because loop 75 used C12 and C13 is concentrated in a small cellmaker set.  
This file tests battery material/local-supply utilization bridge behavior rather than generic battery orderbook or EV slowdown.

## No-Repeat / novelty check

No hard duplicate is intentionally reused.

Hard duplicate key checked conceptually:

```text
canonical_archetype_id + symbol + trigger_type + entry_date
```

No-Repeat shows C13 is concentrated in:

```text
006400, 373220, 096770
```

This run uses three different symbols:

```text
348370 / 엔켐 / US electrolyte local-supply IRA/AMPC lifecycle
121600 / 나노신소재 / CNT conductive additive US utilization bridge
278280 / 천보 / electrolyte-additive utilization fade
```

Data-quality note:

```text
All three rows are stock-web calibration usable by profile-level corporate-action candidates.
All three rows are source_proxy_only=true / evidence_url_pending=true.
348370 and 121600 show share-count changes inside the selected window and require coding-agent validation before runtime promotion.
```

## Research thesis

C13 is not “battery policy stock went up.”

The mechanism must pass through:

```text
US / IRA / AMPC / local-supply policy
→ customer qualification or ramp
→ call-off / utilization / capacity absorption
→ margin conversion
→ durable rerating
```

A US plant headline is a factory gate.  
C13 asks whether cells, electrolyte or conductive material actually flow through the gate at profitable utilization.

---

## Case 1 — Positive with lifecycle 4B: 348370 / 엔켐

### Evidence status

```text
source_proxy_only = true
evidence_url_pending = true
share_count_change_inside_window = true
source_repair_required = true
```

The source-repair task is US electrolyte local supply, customer qualification/ramp, utilization, AMPC/IRA benefit and margin bridge evidence.

```text
evidence_family = US_ELECTROLYTE_LOCAL_SUPPLY_IRA_AMPC_CUSTOMER_UTILIZATION_MARGIN_BRIDGE
case_role = positive_with_later_4b_watch_and_sharecount_validation
trigger_date = 2024-01-09
entry_date = 2024-01-10
entry_price = 91,000
```

### Stock-Web price path

Observed rows from `atlas/ohlcv_tradable_by_symbol_year/348/348370/2024.csv`:

```text
2024-01-10,91000,98600,86300,88200
2024-02-21,338000,358500,304500,326500
2024-04-08,360000,394500,342500,358000
2024-08-05,170000,173200,149000,156500
2024-09-06,176200,181100,165500,165500
```

### Backtest

```text
MFE_30D  = +293.96%
MAE_30D  = -5.16%
MFE_90D  = +333.52%
MAE_90D  = -5.16%
MFE_180D = +333.52%
MAE_180D = -5.16%
peak_180 = 394,500 on 2024-04-08
trough_180 = 86,300 on 2024-01-10
peak_to_later_drawdown = -62.23%
```

### Interpretation

This is a real C13 lifecycle winner.  
The price path validates tradability and possible local-supply/utilization bridge. But it also shows why high MFE cannot be permanent Green.

Correct treatment:

```text
source repair first
possible Stage2/Green
later local 4B if customer ramp/utilization/margin bridge fades
```

---

## Case 2 — Positive with lifecycle 4B: 121600 / 나노신소재

### Evidence status

```text
source_proxy_only = true
evidence_url_pending = true
share_count_change_inside_window = true
source_repair_required = true
```

The source-repair task is CNT conductive additive local supply, customer ramp, utilization, capacity absorption and margin bridge evidence.

```text
evidence_family = CNT_CONDUCTIVE_ADDITIVE_US_LOCAL_SUPPLY_CUSTOMER_RAMP_UTILIZATION_MARGIN_BRIDGE
case_role = positive_with_later_4b_watch_and_sharecount_validation
trigger_date = 2024-02-20
entry_date = 2024-02-21
entry_price = 105,000
```

### Stock-Web price path

Observed rows from `atlas/ohlcv_tradable_by_symbol_year/121/121600/2024.csv`:

```text
2024-02-21,105000,136300,104100,134000
2024-02-22,133100,157800,130600,138000
2024-06-11,122000,149800,121300,141500
2024-07-24,94200,97700,93500,93500
2024-08-05,87900,89700,68500,74900
```

### Backtest

```text
MFE_30D  = +50.29%
MAE_30D  = -0.86%
MFE_90D  = +50.29%
MAE_90D  = -3.90%
MFE_180D = +50.29%
MAE_180D = -34.76%
peak_180 = 157,800 on 2024-02-22
trough_180 = 68,500 on 2024-08-05
peak_to_later_drawdown = -56.59%
```

### Interpretation

This row shows a subtler C13 lifecycle pattern.  
The initial customer-ramp narrative could be real, but later utilization/demand pressure created a large MAE.

Correct treatment:

```text
Stage2 possible after source repair
lifecycle local 4B if utilization/margin bridge fades
```

---

## Case 3 — Counterexample / local 4B: 278280 / 천보

### Evidence status

```text
source_proxy_only = true
evidence_url_pending = true
source_repair_required = true
```

This row tests electrolyte-additive / IRA supply-chain beta without enough customer utilization and margin bridge.

```text
evidence_family = ELECTROLYTE_ADDITIVE_IRA_SUPPLY_BETA_WITH_WEAK_CUSTOMER_UTILIZATION_MARGIN_BRIDGE
case_role = counterexample_utilization_local4b
trigger_date = 2024-02-20
entry_date = 2024-02-21
entry_price = 90,800
```

### Stock-Web price path

Observed rows from `atlas/ohlcv_tradable_by_symbol_year/278/278280/2024.csv`:

```text
2024-02-21,90800,99800,90000,95600
2024-02-22,96500,98800,95100,97700
2024-05-29,73000,73600,71500,71600
2024-07-24,64000,65500,62500,62500
2024-08-05,60600,60800,49000,50400
```

### Backtest

```text
MFE_30D  = +9.91%
MAE_30D  = -5.07%
MFE_90D  = +9.91%
MAE_90D  = -21.70%
MFE_180D = +9.91%
MAE_180D = -46.04%
peak_180 = 99,800 on 2024-02-21
trough_180 = 49,000 on 2024-08-05
peak_to_later_drawdown = -50.90%
```

### Interpretation

This is the utilization-fade counterexample.  
A battery electrolyte/additive name can look policy-linked, but without customer utilization and margin bridge it should not become durable Stage2.

Correct treatment:

```text
false Stage2
local 4B-watch
no hard 4C without non-price break
```

---

## Cross-case residual finding

### What this strengthens

```text
stage2_required_bridge = strengthen
price_only_blowoff_blocks_positive_stage = strengthen
local_4b_watch_guard = strengthen
full_4b_requires_non_price_evidence = keep
share_count_validation_guard = strengthen
```

### What this does not justify

```text
do_not_raise_generic_C13_battery_policy_weight = true
do_not_treat_all_US_IRA_AMPC_MFE_as_Green = true
do_not_convert_battery_material_drawdown_to_hard_4C_without_non_price_break = true
```

### Candidate canonical compression

Fine labels can compress into:

```text
US_IRA_AMPC_ELECTROLYTE_CNT_LOCAL_SUPPLY_UTILIZATION_BRIDGE_VS_MATERIAL_UTILIZATION_FADE
```

This fine archetype covers:

```text
1. US electrolyte local-supply utilization bridge → Stage2 possible after source repair
2. CNT conductive additive customer-ramp utilization bridge → Stage2 possible, lifecycle-managed
3. electrolyte additive utilization fade → false Stage2 / local 4B
```

---

## Machine-readable rows

### price source validation row

```jsonl
{"row_type": "price_source_validation", "source": "Songdaiki/stock-web", "source_url": "https://github.com/Songdaiki/stock-web", "manifest_path": "atlas/manifest.json", "schema_path": "atlas/schema.json", "universe_path": "atlas/universe/all_symbols.csv", "manifest_max_date": "2026-02-20", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "raw_shard_root": "atlas/ohlcv_raw_by_symbol_year", "validation_status": "usable_for_historical_calibration"}
```

### case rows

```jsonl
{"row_type": "case", "case_id": "R3L76-C13-348370-ENCHEM-US-ELECTROLYTE-IRA-LOCAL-SUPPLY-LIFECYCLE", "symbol": "348370", "company_name": "엔켐", "round": "R3", "loop": "76", "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C13_BATTERY_JV_UTILIZATION_AMPC_IRA", "fine_archetype_id": "US_IRA_AMPC_ELECTROLYTE_CNT_LOCAL_SUPPLY_UTILIZATION_BRIDGE_VS_MATERIAL_UTILIZATION_FADE", "case_type": "battery_jv_utilization_ampc_ira", "positive_or_counterexample": "positive", "best_trigger": "Stage2-Actionable-USElectrolyteIRALocalSupplyBridgeWithLifecycle4B", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 0.5, "score_price_alignment": "C13 should allow Stage2 when US/IRA battery supply-chain attention connects to actual electrolyte local supply, customer qualification, utilization, AMPC or margin bridge. Enchem produced extreme MFE with controlled entry-basis MAE, but the post-peak drawdown and share-count changes require lifecycle local 4B and validation.", "current_profile_verdict": "source_repair_required_before_runtime_weight", "price_source": "Songdaiki/stock-web", "notes": "Stock-web path usable; non-proxy US/IRA/AMPC/local-supply, customer ramp, utilization, call-off and margin bridge evidence required before runtime promotion."}
{"row_type": "case", "case_id": "R3L76-C13-121600-NANOSIN-CNT-CONDUCTIVE-ADDITIVE-US-UTILIZATION", "symbol": "121600", "company_name": "나노신소재", "round": "R3", "loop": "76", "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C13_BATTERY_JV_UTILIZATION_AMPC_IRA", "fine_archetype_id": "US_IRA_AMPC_ELECTROLYTE_CNT_LOCAL_SUPPLY_UTILIZATION_BRIDGE_VS_MATERIAL_UTILIZATION_FADE", "case_type": "battery_jv_utilization_ampc_ira", "positive_or_counterexample": "positive", "best_trigger": "Stage2-Actionable-CNTConductiveAdditiveUSUtilizationBridgeWithLater4B", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 0.5, "score_price_alignment": "C13 should include CNT/conductive additive suppliers only when US/local supply, customer ramp, utilization and margin bridge is visible. Nano New Material produced strong early MFE, but the later utilization/demand drawdown means the signal must be lifecycle-managed and share-count validated.", "current_profile_verdict": "source_repair_required_before_runtime_weight", "price_source": "Songdaiki/stock-web", "notes": "Stock-web path usable; non-proxy US/IRA/AMPC/local-supply, customer ramp, utilization, call-off and margin bridge evidence required before runtime promotion."}
{"row_type": "case", "case_id": "R3L76-C13-278280-CHUNBO-ELECTROLYTE-ADDITIVE-UTILIZATION-FADE", "symbol": "278280", "company_name": "천보", "round": "R3", "loop": "76", "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C13_BATTERY_JV_UTILIZATION_AMPC_IRA", "fine_archetype_id": "US_IRA_AMPC_ELECTROLYTE_CNT_LOCAL_SUPPLY_UTILIZATION_BRIDGE_VS_MATERIAL_UTILIZATION_FADE", "case_type": "battery_jv_utilization_ampc_ira", "positive_or_counterexample": "counterexample", "best_trigger": "Stage2-FalsePositive / ElectrolyteAdditiveUtilizationFade", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 0.5, "score_price_alignment": "C13 should not treat electrolyte/additive or IRA supply-chain beta as durable Stage2 unless customer utilization, local supply, call-off and margin evidence refreshes. Chunbo had limited MFE and then a high-MAE utilization fade.", "current_profile_verdict": "source_repair_required_before_runtime_weight", "price_source": "Songdaiki/stock-web", "notes": "Stock-web path usable; non-proxy US/IRA/AMPC/local-supply, customer ramp, utilization, call-off and margin bridge evidence required before runtime promotion."}
```

### trigger rows

```jsonl
{"row_type": "trigger", "trigger_id": "TRG_R3L76-C13-348370-ENCHEM-US-ELECTROLYTE-IRA-LOCAL-SUPPLY-LIFECYCLE", "case_id": "R3L76-C13-348370-ENCHEM-US-ELECTROLYTE-IRA-LOCAL-SUPPLY-LIFECYCLE", "symbol": "348370", "company_name": "엔켐", "round": "R3", "loop": "76", "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C13_BATTERY_JV_UTILIZATION_AMPC_IRA", "fine_archetype_id": "US_IRA_AMPC_ELECTROLYTE_CNT_LOCAL_SUPPLY_UTILIZATION_BRIDGE_VS_MATERIAL_UTILIZATION_FADE", "loop_objective": "coverage_gap_fill|counterexample_mining|battery_US_IRA_AMPC_utilization_guardrail", "trigger_type": "Stage2-Actionable-USElectrolyteIRALocalSupplyBridgeWithLifecycle4B", "trigger_date": "2024-01-09", "entry_date": "2024-01-10", "entry_price": 91000.0, "evidence_available_at_that_date": "US_ELECTROLYTE_LOCAL_SUPPLY_IRA_AMPC_CUSTOMER_UTILIZATION_MARGIN_BRIDGE", "evidence_source": "source_proxy_manual_verification_required:ENCHEM_2024_US_ELECTROLYTE_IRA_AMPC_LOCAL_SUPPLY_CUSTOMER_UTILIZATION_MARGIN_BRIDGE", "stage2_evidence_fields": ["US_IRA_or_AMPC_supply_chain", "local_supply_or_customer_ramp_candidate", "utilization_or_margin_bridge_candidate"], "stage3_evidence_fields": ["relative_strength", "calloff_or_capacity_absorption_candidate"], "stage4b_evidence_fields": ["utilization_fade", "bridge_stale_or_absent", "MAE_widening", "post_peak_drawdown"], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/348/348370/2024.csv", "profile_path": "atlas/symbol_profiles/348/348370.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": 293.96, "MFE_90D_pct": 333.52, "MFE_180D_pct": 333.52, "MAE_30D_pct": -5.16, "MAE_90D_pct": -5.16, "MAE_180D_pct": -5.16, "peak_date": "2024-04-08", "peak_price": 394500.0, "drawdown_after_peak_pct": -62.23, "green_lateness_ratio": null, "four_b_local_peak_proximity": "local_4b_watch_after_US_IRA_AMPC_or_material_supply_peak_if_utilization_margin_bridge_fades", "four_b_full_window_peak_proximity": "full_4b_requires_non_price_customer_calloff_utilization_AMPC_margin_or_financing_break", "trigger_outcome_label": "positive_with_later_4b_watch_and_sharecount_validation", "current_profile_verdict": "C13 should allow Stage2 when US/IRA battery supply-chain attention connects to actual electrolyte local supply, customer qualification, utilization, AMPC or margin bridge. Enchem produced extreme MFE with controlled entry-basis MAE, but the post-peak drawdown and share-count changes require lifecycle local 4B and validation.", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window_by_profile", "share_count_change_inside_window": true, "same_entry_group_id": "C13_US_IRA_AMPC_UTIL_348370_2024-01-10", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 0.5, "do_not_count_as_new_case": false, "source_proxy_only": true, "evidence_url_pending": true}
{"row_type": "trigger", "trigger_id": "TRG_R3L76-C13-121600-NANOSIN-CNT-CONDUCTIVE-ADDITIVE-US-UTILIZATION", "case_id": "R3L76-C13-121600-NANOSIN-CNT-CONDUCTIVE-ADDITIVE-US-UTILIZATION", "symbol": "121600", "company_name": "나노신소재", "round": "R3", "loop": "76", "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C13_BATTERY_JV_UTILIZATION_AMPC_IRA", "fine_archetype_id": "US_IRA_AMPC_ELECTROLYTE_CNT_LOCAL_SUPPLY_UTILIZATION_BRIDGE_VS_MATERIAL_UTILIZATION_FADE", "loop_objective": "coverage_gap_fill|counterexample_mining|battery_US_IRA_AMPC_utilization_guardrail", "trigger_type": "Stage2-Actionable-CNTConductiveAdditiveUSUtilizationBridgeWithLater4B", "trigger_date": "2024-02-20", "entry_date": "2024-02-21", "entry_price": 105000.0, "evidence_available_at_that_date": "CNT_CONDUCTIVE_ADDITIVE_US_LOCAL_SUPPLY_CUSTOMER_RAMP_UTILIZATION_MARGIN_BRIDGE", "evidence_source": "source_proxy_manual_verification_required:NANOSIN_2024_CNT_CONDUCTIVE_ADDITIVE_US_LOCAL_SUPPLY_CUSTOMER_RAMP_UTILIZATION_MARGIN_BRIDGE", "stage2_evidence_fields": ["US_IRA_or_AMPC_supply_chain", "local_supply_or_customer_ramp_candidate", "utilization_or_margin_bridge_candidate"], "stage3_evidence_fields": ["relative_strength", "calloff_or_capacity_absorption_candidate"], "stage4b_evidence_fields": ["utilization_fade", "bridge_stale_or_absent", "MAE_widening", "post_peak_drawdown"], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/121/121600/2024.csv", "profile_path": "atlas/symbol_profiles/121/121600.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": 50.29, "MFE_90D_pct": 50.29, "MFE_180D_pct": 50.29, "MAE_30D_pct": -0.86, "MAE_90D_pct": -3.9, "MAE_180D_pct": -34.76, "peak_date": "2024-02-22", "peak_price": 157800.0, "drawdown_after_peak_pct": -56.59, "green_lateness_ratio": null, "four_b_local_peak_proximity": "local_4b_watch_after_US_IRA_AMPC_or_material_supply_peak_if_utilization_margin_bridge_fades", "four_b_full_window_peak_proximity": "full_4b_requires_non_price_customer_calloff_utilization_AMPC_margin_or_financing_break", "trigger_outcome_label": "positive_with_later_4b_watch_and_sharecount_validation", "current_profile_verdict": "C13 should include CNT/conductive additive suppliers only when US/local supply, customer ramp, utilization and margin bridge is visible. Nano New Material produced strong early MFE, but the later utilization/demand drawdown means the signal must be lifecycle-managed and share-count validated.", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window_by_profile", "share_count_change_inside_window": true, "same_entry_group_id": "C13_US_IRA_AMPC_UTIL_121600_2024-02-21", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 0.5, "do_not_count_as_new_case": false, "source_proxy_only": true, "evidence_url_pending": true}
{"row_type": "trigger", "trigger_id": "TRG_R3L76-C13-278280-CHUNBO-ELECTROLYTE-ADDITIVE-UTILIZATION-FADE", "case_id": "R3L76-C13-278280-CHUNBO-ELECTROLYTE-ADDITIVE-UTILIZATION-FADE", "symbol": "278280", "company_name": "천보", "round": "R3", "loop": "76", "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C13_BATTERY_JV_UTILIZATION_AMPC_IRA", "fine_archetype_id": "US_IRA_AMPC_ELECTROLYTE_CNT_LOCAL_SUPPLY_UTILIZATION_BRIDGE_VS_MATERIAL_UTILIZATION_FADE", "loop_objective": "coverage_gap_fill|counterexample_mining|battery_US_IRA_AMPC_utilization_guardrail", "trigger_type": "Stage2-FalsePositive / ElectrolyteAdditiveUtilizationFade", "trigger_date": "2024-02-20", "entry_date": "2024-02-21", "entry_price": 90800.0, "evidence_available_at_that_date": "ELECTROLYTE_ADDITIVE_IRA_SUPPLY_BETA_WITH_WEAK_CUSTOMER_UTILIZATION_MARGIN_BRIDGE", "evidence_source": "source_proxy_manual_verification_required:CHUNBO_2024_ELECTROLYTE_ADDITIVE_IRA_SUPPLY_CUSTOMER_UTILIZATION_MARGIN_BRIDGE", "stage2_evidence_fields": ["US_IRA_or_AMPC_supply_chain", "local_supply_or_customer_ramp_candidate", "utilization_or_margin_bridge_candidate"], "stage3_evidence_fields": ["relative_strength", "calloff_or_capacity_absorption_candidate"], "stage4b_evidence_fields": ["utilization_fade", "bridge_stale_or_absent", "MAE_widening", "post_peak_drawdown"], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/278/278280/2024.csv", "profile_path": "atlas/symbol_profiles/278/278280.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": 9.91, "MFE_90D_pct": 9.91, "MFE_180D_pct": 9.91, "MAE_30D_pct": -5.07, "MAE_90D_pct": -21.7, "MAE_180D_pct": -46.04, "peak_date": "2024-02-21", "peak_price": 99800.0, "drawdown_after_peak_pct": -50.9, "green_lateness_ratio": null, "four_b_local_peak_proximity": "local_4b_watch_after_US_IRA_AMPC_or_material_supply_peak_if_utilization_margin_bridge_fades", "four_b_full_window_peak_proximity": "full_4b_requires_non_price_customer_calloff_utilization_AMPC_margin_or_financing_break", "trigger_outcome_label": "counterexample_utilization_local4b", "current_profile_verdict": "C13 should not treat electrolyte/additive or IRA supply-chain beta as durable Stage2 unless customer utilization, local supply, call-off and margin evidence refreshes. Chunbo had limited MFE and then a high-MAE utilization fade.", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window_by_profile", "share_count_change_inside_window": false, "same_entry_group_id": "C13_US_IRA_AMPC_UTIL_278280_2024-02-21", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 0.5, "do_not_count_as_new_case": false, "source_proxy_only": true, "evidence_url_pending": true}
```

### score simulation rows

```jsonl
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R3L76-C13-348370-ENCHEM-US-ELECTROLYTE-IRA-LOCAL-SUPPLY-LIFECYCLE", "trigger_id": "TRG_R3L76-C13-348370-ENCHEM-US-ELECTROLYTE-IRA-LOCAL-SUPPLY-LIFECYCLE", "symbol": "348370", "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C13_BATTERY_JV_UTILIZATION_AMPC_IRA", "raw_component_scores_before": {"US_IRA_AMPC_policy_score": 12, "local_supply_score": 14, "customer_ramp_score": 14, "utilization_score": 13, "margin_bridge_score": 12, "relative_strength_score": 16, "execution_risk_score": 7, "dilution_or_sharecount_validation_risk": 8, "source_confidence_score": 2}, "weighted_score_before": 84, "stage_label_before": "Stage2-Actionable after source repair", "raw_component_scores_after": {"US_IRA_AMPC_policy_score": 9, "local_supply_score": 16, "customer_ramp_score": 16, "utilization_score": 15, "margin_bridge_score": 14, "relative_strength_score": 15, "execution_risk_score": 8, "dilution_or_sharecount_validation_risk": 10, "source_confidence_score": 2}, "weighted_score_after": 89, "stage_label_after": "Stage2/Yellow-Green candidate after source repair + lifecycle 4B", "changed_components": ["local_supply_score", "customer_ramp_score", "utilization_score", "margin_bridge_score", "execution_risk_score"], "component_delta_explanation": "Reward only verified US/IRA/AMPC local supply, customer ramp, utilization and margin bridge; cap material-supply beta when utilization/call-off evidence fails to refresh.", "MFE_90D_pct": 333.52, "MAE_90D_pct": -5.16, "score_return_alignment_label": "aligned_positive_with_lifecycle_4b", "current_profile_verdict": "C13 should allow Stage2 when US/IRA battery supply-chain attention connects to actual electrolyte local supply, customer qualification, utilization, AMPC or margin bridge. Enchem produced extreme MFE with controlled entry-basis MAE, but the post-peak drawdown and share-count changes require lifecycle local 4B and validation."}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R3L76-C13-121600-NANOSIN-CNT-CONDUCTIVE-ADDITIVE-US-UTILIZATION", "trigger_id": "TRG_R3L76-C13-121600-NANOSIN-CNT-CONDUCTIVE-ADDITIVE-US-UTILIZATION", "symbol": "121600", "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C13_BATTERY_JV_UTILIZATION_AMPC_IRA", "raw_component_scores_before": {"US_IRA_AMPC_policy_score": 12, "local_supply_score": 14, "customer_ramp_score": 14, "utilization_score": 13, "margin_bridge_score": 12, "relative_strength_score": 16, "execution_risk_score": 7, "dilution_or_sharecount_validation_risk": 8, "source_confidence_score": 2}, "weighted_score_before": 84, "stage_label_before": "Stage2-Actionable after source repair", "raw_component_scores_after": {"US_IRA_AMPC_policy_score": 9, "local_supply_score": 16, "customer_ramp_score": 16, "utilization_score": 15, "margin_bridge_score": 14, "relative_strength_score": 15, "execution_risk_score": 8, "dilution_or_sharecount_validation_risk": 10, "source_confidence_score": 2}, "weighted_score_after": 89, "stage_label_after": "Stage2/Yellow-Green candidate after source repair + lifecycle 4B", "changed_components": ["local_supply_score", "customer_ramp_score", "utilization_score", "margin_bridge_score", "execution_risk_score"], "component_delta_explanation": "Reward only verified US/IRA/AMPC local supply, customer ramp, utilization and margin bridge; cap material-supply beta when utilization/call-off evidence fails to refresh.", "MFE_90D_pct": 50.29, "MAE_90D_pct": -3.9, "score_return_alignment_label": "aligned_positive_with_lifecycle_4b", "current_profile_verdict": "C13 should include CNT/conductive additive suppliers only when US/local supply, customer ramp, utilization and margin bridge is visible. Nano New Material produced strong early MFE, but the later utilization/demand drawdown means the signal must be lifecycle-managed and share-count validated."}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R3L76-C13-278280-CHUNBO-ELECTROLYTE-ADDITIVE-UTILIZATION-FADE", "trigger_id": "TRG_R3L76-C13-278280-CHUNBO-ELECTROLYTE-ADDITIVE-UTILIZATION-FADE", "symbol": "278280", "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C13_BATTERY_JV_UTILIZATION_AMPC_IRA", "raw_component_scores_before": {"US_IRA_AMPC_policy_score": 12, "local_supply_score": 5, "customer_ramp_score": 4, "utilization_score": 3, "margin_bridge_score": 2, "relative_strength_score": 5, "execution_risk_score": 18, "dilution_or_sharecount_validation_risk": 0, "source_confidence_score": 2}, "weighted_score_before": 50, "stage_label_before": "Stage2-FalsePositive / local 4B-watch", "raw_component_scores_after": {"US_IRA_AMPC_policy_score": 9, "local_supply_score": 3, "customer_ramp_score": 2, "utilization_score": 1, "margin_bridge_score": 1, "relative_strength_score": 3, "execution_risk_score": 21, "dilution_or_sharecount_validation_risk": 0, "source_confidence_score": 2}, "weighted_score_after": 38, "stage_label_after": "Stage4B-local-watch / no durable Green", "changed_components": ["local_supply_score", "customer_ramp_score", "utilization_score", "margin_bridge_score", "execution_risk_score"], "component_delta_explanation": "Reward only verified US/IRA/AMPC local supply, customer ramp, utilization and margin bridge; cap material-supply beta when utilization/call-off evidence fails to refresh.", "MFE_90D_pct": 9.91, "MAE_90D_pct": -21.7, "score_return_alignment_label": "false_positive_utilization_bridge_gap", "current_profile_verdict": "C13 should not treat electrolyte/additive or IRA supply-chain beta as durable Stage2 unless customer utilization, local supply, call-off and margin evidence refreshes. Chunbo had limited MFE and then a high-MAE utilization fade."}
```

### aggregate row

```jsonl
{"row_type": "aggregate", "round": "R3", "loop": 76, "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C13_BATTERY_JV_UTILIZATION_AMPC_IRA", "fine_archetype_id": "US_IRA_AMPC_ELECTROLYTE_CNT_LOCAL_SUPPLY_UTILIZATION_BRIDGE_VS_MATERIAL_UTILIZATION_FADE", "calibration_usable_case_count": 3, "calibration_usable_trigger_count": 3, "new_independent_case_count": 3, "reused_case_count": 0, "same_archetype_new_symbol_count": 3, "same_archetype_new_trigger_family_count": 3, "positive_case_count": 2, "counterexample_count": 1, "four_b_case_count": 3, "four_c_case_count": 0, "source_proxy_only_count": 3, "evidence_url_pending_count": 3, "share_count_change_inside_window_count": 2, "current_profile_error_count": 1, "diversity_score_summary": "+3 C13 battery material/local-supply symbols outside top-covered cellmaker set, +3 electrolyte/CNT/electrolyte-additive utilization trigger families, +2 US/local-supply positives, +1 utilization-fade local-4B counterexample, no hard duplicate", "residual_contribution_label": "coverage_gap_fill_with_source_repair_and_sharecount_validation_needed"}
```

### shadow weight row

```jsonl
{"row_type": "shadow_weight", "round": "R3", "loop": 76, "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C13_BATTERY_JV_UTILIZATION_AMPC_IRA", "axis": "us_ira_ampc_electrolyte_cnt_local_supply_utilization_bridge_vs_material_utilization_fade", "decision": "hold_for_source_repair_and_more_evidence", "proposed_runtime_effect": "C13 should split verified US/IRA/AMPC local-supply utilization bridges from generic battery-material policy beta. Stage2 requires local supply, customer ramp, call-off/utilization, AMPC or margin bridge. If MFE fades and MAE/post-peak drawdown opens without bridge refresh, route to local 4B-watch. Share-count changes require validation before runtime promotion.", "do_not_propose_new_weight_delta": true, "needs_more_evidence": true, "source_repair_required": ["348370", "121600", "278280"], "share_count_validation_required": ["348370", "121600"]}
```

### residual contribution row

```jsonl
{"row_type": "residual_contribution", "round": "R3", "loop": 76, "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C13_BATTERY_JV_UTILIZATION_AMPC_IRA", "existing_axis_strengthened": ["stage2_required_bridge", "price_only_blowoff_blocks_positive_stage", "local_4b_watch_guard", "full_4b_requires_non_price_evidence", "share_count_validation_guard"], "new_axis_proposed": null, "sector_specific_rule_candidate": true, "canonical_archetype_rule_candidate": true, "narrative_summary": "C13 needs US/IRA/AMPC utilization proof. Enchem and Nano New Material show local-supply/CNT material positives after source repair; Chunbo shows electrolyte-additive utilization fading into local 4B when customer utilization and margin bridge are absent."}
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
348370:
  corporate_action_candidate_dates = none
  selected window = 2024-01-10~D+180
  contamination = false by profile
  share_count_change_inside_window = true → coding-agent validation required

121600:
  corporate_action_candidate_dates = 2015-12-17
  selected window = 2024-02-21~D+180
  contamination = false
  share_count_change_inside_window = true → coding-agent validation required

278280:
  corporate_action_candidate_dates = none
  selected window = 2024-02-21~D+180
  contamination = false
```

Data-quality caveat:

```text
All selected C13 rows are source_proxy_only / evidence_url_pending.
348370 and 121600 also require share-count validation before runtime promotion.
This MD is useful for stock-web path calibration and C13 rule-shape discovery,
but coding-agent promotion requires non-proxy US/IRA/AMPC/local-supply, customer ramp, utilization, call-off and margin evidence.
```

---

## Deferred Coding Agent Handoff Prompt

Do not execute this now.

```text
You are the coding agent for Songdaiki/stock_agent.

Read this standalone v12 residual research MD and ingest machine-readable rows only after validation.

Do not patch production scoring blindly.
This R3/C13 artifact is marked do_not_propose_new_weight_delta=true because all rows need source repair and two rows need share-count validation.

Candidate axis:
us_ira_ampc_electrolyte_cnt_local_supply_utilization_bridge_vs_material_utilization_fade

Required checks before implementation:
1. Validate all trigger rows against stock-web tradable_raw OHLC shards.
2. Confirm no hard duplicate key:
   canonical_archetype_id + symbol + trigger_type + entry_date.
3. Verify non-proxy source URLs for 348370, 121600 and 278280.
4. Validate 348370 and 121600 share-count changes inside the selected window.
5. Keep generic C13 battery-policy weight unchanged until source repair is complete.
6. Consider Stage2 only when:
   - US/IRA/AMPC or local-supply exposure is explicit,
   - customer ramp or qualification is visible,
   - utilization / call-off / capacity absorption evidence exists,
   - margin bridge is credible,
   - MAE remains controlled or the signal is lifecycle-managed.
7. Consider local 4B-watch when:
   - the trigger is battery-material or IRA beta only,
   - utilization/call-off/margin evidence is weak or stale,
   - MAE_90D <= -20% or MAE_180D <= -25%,
   - post-peak drawdown <= -35%.
8. Do not convert local 4B-watch into full 4B/4C without non-price customer loss, utilization collapse, AMPC policy break, margin collapse, financing or liquidity evidence.
9. Emit before/after diagnostics and reject if verified US/local-supply utilization positives are overblocked.
```

---

## Final round state

```text
completed_round = R3
completed_loop = 76
next_round = R4
next_loop = 76
round_schedule_status = valid
round_sector_consistency = pass
```

