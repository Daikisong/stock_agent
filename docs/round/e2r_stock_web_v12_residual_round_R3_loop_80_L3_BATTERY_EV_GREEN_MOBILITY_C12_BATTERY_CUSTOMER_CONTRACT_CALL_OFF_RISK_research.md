# E2R Stock-Web v12 Residual Research — R3 Loop 80 / L3 / C12

## Metadata

```json
{
  "research_session": "post_calibrated_sector_archetype_residual_research",
  "mode": "historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12",
  "scheduled_round": "R3",
  "scheduled_loop": 80,
  "round_schedule_status": "valid",
  "round_sector_consistency": "pass",
  "completed_round": "R3",
  "completed_loop": 80,
  "computed_next_round": "R4",
  "computed_next_loop": 80,
  "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY",
  "canonical_archetype_id": "C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK",
  "fine_archetype_id": "SEPARATOR_COPPERFOIL_PRECURSOR_CUSTOMER_CALLOFF_UTILIZATION_MARGIN_BRIDGE",
  "loop_objective": [
    "coverage_gap_fill",
    "counterexample_mining",
    "4B_non_price_requirement_stress_test",
    "battery_customer_contract_calloff_guardrail",
    "separator_copperfoil_precursor_customer_volume_utilization_margin_bridge",
    "post_corporate_action_validation_queue_creation",
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

Previous completed state in this interactive run: R2 / loop 80.

Therefore:

```text
scheduled_round = R3
scheduled_loop = 80
allowed_large_sector = L3_BATTERY_EV_GREEN_MOBILITY
selected_large_sector = L3_BATTERY_EV_GREEN_MOBILITY
selected_canonical_archetype_id = C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK
computed_next_round = R4
computed_next_loop = 80
```

R3 was routed to C12 because loop 79 R3 used C14 and C12 still has under-covered separator / copperfoil / precursor call-off risk residual space.

## No-Repeat / novelty check

No hard duplicate is intentionally reused.

Hard duplicate key checked conceptually:

```text
canonical_archetype_id + symbol + trigger_type + entry_date
```

No-Repeat shows C12 concentration in:

```text
UNKNOWN_SYMBOL, 247540, 278280, 003670, 005070
```

This run uses three different symbols:

```text
361610 / SK아이이테크놀로지 / separator customer call-off and utilization local 4B
336370 / 솔루스첨단소재 / post-CA copperfoil recovery vs call-off lifecycle
450080 / 에코프로머티 / precursor customer contract call-off fade
```

Data-quality note:

```text
All three rows are stock-web calibration usable by profile-level corporate-action candidates.
All three rows are source_proxy_only=true / evidence_url_pending=true.
336370 requires post-corporate-action validation because 2024-01-30 is a candidate date before entry.
450080 shows share-count changes later in the 2024 shard and requires validation before runtime promotion.
```

## Research thesis

C12 is not “배터리 소재가 빠졌다.”

The mechanism must pass through:

```text
customer contract or supply agreement
→ actual call-off / shipment volume
→ utilization and inventory absorption
→ pricing and margin bridge
→ either recovery Stage2 or local 4B
```

고객계약은 수도꼭지다.  
C12가 보려는 것은 계약이라는 수도꼭지가 실제 물량, 가동률, 재고 소진, 마진으로 물을 흘려보내는지다.

---

## Case 1 — Local 4B risk: 361610 / SK아이이테크놀로지

### Evidence status

```text
source_proxy_only = true
evidence_url_pending = true
source_repair_required = true
```

The source-repair task is separator customer call-off, utilization, volume, pricing and margin bridge evidence.

```text
evidence_family = BATTERY_SEPARATOR_CUSTOMER_CALLOFF_UTILIZATION_VOLUME_MARGIN_BRIDGE_WEAK
case_role = risk_positive_separator_calloff_local4b
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
2024-03-19,76000,77000,74300,76800
2024-08-05,36000,36200,30950,32000
2024-09-10,31750,32100,30050,30050
2024-10-25,31800,32300,30800,30800
```

### Backtest

```text
MFE_30D  = +10.08%
MAE_30D  = -11.31%
MFE_90D  = +10.08%
MAE_90D  = -18.80%
MFE_180D = +10.08%
MAE_180D = -59.06%
peak_180 = 80,800 on 2024-02-02
trough_180 = 30,050 on 2024-09-10
peak_to_later_drawdown = -62.81%
```

### Interpretation

This is a C12 local-4B risk row.  
The early bounce did not become durable customer-volume or utilization rerating.

Correct treatment:

```text
separator call-off / utilization risk
→ high MAE
→ local 4B-watch
→ no hard 4C without non-price customer loss, impairment, financing or margin break
```

---

## Case 2 — Post-CA recovery candidate: 336370 / 솔루스첨단소재

### Evidence status

```text
source_proxy_only = true
evidence_url_pending = true
post_corporate_action_validation_required = true
source_repair_required = true
```

The source-repair task is copperfoil customer volume, utilization, pricing, inventory and margin bridge evidence.

```text
evidence_family = BATTERY_COPPERFOIL_CUSTOMER_VOLUME_UTILIZATION_MARGIN_BRIDGE_POST_CA
case_role = positive_post_CA_recovery_with_later_4b_watch
trigger_date = 2024-01-31
entry_date = 2024-02-01
entry_price = 11,150
```

### Stock-Web price path

Observed rows from `atlas/ohlcv_tradable_by_symbol_year/336/336370/2024.csv`:

```text
2024-01-30,12310,12410,11620,11630
2024-02-01,11150,11300,11010,11160
2024-02-21,12890,13250,12560,13100
2024-04-11,20750,21650,18660,19900
2024-07-01,18480,23500,17650,23050
2024-08-05,14510,14530,11920,12590
2024-09-10,11480,11730,11200,11200
```

### Backtest

```text
MFE_30D  = +18.83%
MAE_30D  = -1.26%
MFE_90D  = +94.62%
MAE_90D  = -1.26%
MFE_180D = +110.76%
MAE_180D = -1.26%
peak_180 = 23,500 on 2024-07-01
trough_180 = 11,010 on 2024-02-01
peak_to_later_drawdown = -52.34%
```

### Interpretation

This is a recovery candidate, not a blanket EV-slowdown rejection.  
But the 2024-01-30 corporate-action candidate means runtime ingestion must validate post-CA continuity.

Correct treatment:

```text
post-CA validation first
verified customer volume / utilization / margin bridge → Stage2 possible
bridge stale after peak → lifecycle local 4B-watch
```

---

## Case 3 — Counterexample / local 4B: 450080 / 에코프로머티

### Evidence status

```text
source_proxy_only = true
evidence_url_pending = true
share_count_validation_required = true
source_repair_required = true
```

This row tests precursor / battery material contract beta without enough customer call-off, utilization and margin refresh.

```text
evidence_family = BATTERY_PRECURSOR_CUSTOMER_CONTRACT_VOLUME_CALLOFF_UTILIZATION_MARGIN_BRIDGE_WEAK
case_role = counterexample_precursor_contract_calloff_local4b
trigger_date = 2024-01-31
entry_date = 2024-02-01
entry_price = 147,000
```

### Stock-Web price path

Observed rows from `atlas/ohlcv_tradable_by_symbol_year/450/450080/2024.csv`:

```text
2024-02-01,147000,174000,144600,173600
2024-02-13,180000,209500,179300,209500
2024-03-28,139200,139900,133100,133600
2024-04-05,120600,125500,115900,117500
2024-08-05,82600,83800,70100,72300
2024-09-30,132300,144100,126300,134900
2024-10-25,114300,115400,110000,110000
```

### Backtest

```text
MFE_30D  = +42.52%
MAE_30D  = -0.68%
MFE_90D  = +42.52%
MAE_90D  = -23.74%
MFE_180D = +42.52%
MAE_180D = -52.31%
peak_180 = 209,500 on 2024-02-13
trough_180 = 70,100 on 2024-08-05
peak_to_later_drawdown = -66.54%
```

### Interpretation

This is a C12 false-positive boundary.  
The early MFE was tradable, but it did not validate durable contract call-off / utilization economics.

Correct treatment:

```text
precursor contract beta
→ no verified call-off / utilization / margin bridge
→ local 4B-watch
```

---

## Cross-case residual finding

### What this strengthens

```text
stage2_required_bridge = strengthen
customer_calloff_local_4b_guard = strengthen
post_corporate_action_validation_guard = strengthen
share_count_validation_guard = strengthen
blanket_EV_material_overbearish_guard = strengthen
full_4b_or_4c_requires_non_price_evidence = keep
```

### What this does not justify

```text
do_not_raise_generic_C12_battery_contract_weight = true
do_not_treat_all_battery_material_MFE_as_Green = true
do_not_force_4B_on_post_CA_recovery_without_validation = true
do_not_convert_calloff_drawdown_to_hard_4C_without_non_price_customer_loss_or_margin_break = true
```

### Candidate canonical compression

Fine labels can compress into:

```text
SEPARATOR_COPPERFOIL_PRECURSOR_CUSTOMER_CALLOFF_UTILIZATION_MARGIN_BRIDGE
```

This fine archetype covers:

```text
1. separator customer call-off / utilization weakness → local 4B-watch
2. copperfoil post-CA recovery with bounded MAE → Stage2 possible after validation and source repair
3. precursor contract beta without call-off/margin bridge → false Stage2 / local 4B
```

---

## Machine-readable rows

### price source validation row

```jsonl
{"row_type": "price_source_validation", "source": "Songdaiki/stock-web", "source_url": "https://github.com/Songdaiki/stock-web", "manifest_path": "atlas/manifest.json", "schema_path": "atlas/schema.json", "universe_path": "atlas/universe/all_symbols.csv", "manifest_max_date": "2026-02-20", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "raw_shard_root": "atlas/ohlcv_raw_by_symbol_year", "validation_status": "usable_for_historical_calibration"}
```

### case rows

```jsonl
{"row_type": "case", "case_id": "R3L80-C12-361610-SKIET-SEPARATOR-CALLOFF-UTILIZATION-LOCAL4B", "symbol": "361610", "company_name": "SK아이이테크놀로지", "round": "R3", "loop": "80", "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK", "fine_archetype_id": "SEPARATOR_COPPERFOIL_PRECURSOR_CUSTOMER_CALLOFF_UTILIZATION_MARGIN_BRIDGE", "case_type": "battery_customer_contract_call_off_risk", "positive_or_counterexample": "risk_positive", "best_trigger": "Stage4B-Local-SeparatorCustomerCalloffUtilizationHighMAE", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 0.5, "score_price_alignment": "C12 should flag separator/customer-calloff risk when customer volume, utilization, pricing and margin bridge weaken. SK IET produced only a small early MFE and then a deep high-MAE path.", "current_profile_verdict": "source_repair_required_before_runtime_weight", "price_source": "Songdaiki/stock-web", "notes": "Stock-web path usable; non-proxy customer call-off, contract volume, utilization, pricing, inventory and margin bridge evidence required before runtime promotion."}
{"row_type": "case", "case_id": "R3L80-C12-336370-SOLUS-COPPERFOIL-POSTCA-CALLOFF-LIFECYCLE", "symbol": "336370", "company_name": "솔루스첨단소재", "round": "R3", "loop": "80", "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK", "fine_archetype_id": "SEPARATOR_COPPERFOIL_PRECURSOR_CUSTOMER_CALLOFF_UTILIZATION_MARGIN_BRIDGE", "case_type": "battery_customer_contract_call_off_risk", "positive_or_counterexample": "positive", "best_trigger": "Stage2-Lifecycle-CopperfoilCustomerCalloffPostCABridgeWithLocal4B", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 0.5, "score_price_alignment": "C12 should not overblock post-CA copperfoil/material names when recovery MFE and bounded entry MAE are visible, but it still requires customer volume, utilization and margin evidence before Stage2 promotion.", "current_profile_verdict": "source_repair_required_before_runtime_weight", "price_source": "Songdaiki/stock-web", "notes": "Stock-web path usable; non-proxy customer call-off, contract volume, utilization, pricing, inventory and margin bridge evidence required before runtime promotion."}
{"row_type": "case", "case_id": "R3L80-C12-450080-ECOPRO-MATERIALS-PRECURSOR-CALLOFF-FADE", "symbol": "450080", "company_name": "에코프로머티", "round": "R3", "loop": "80", "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK", "fine_archetype_id": "SEPARATOR_COPPERFOIL_PRECURSOR_CUSTOMER_CALLOFF_UTILIZATION_MARGIN_BRIDGE", "case_type": "battery_customer_contract_call_off_risk", "positive_or_counterexample": "counterexample", "best_trigger": "Stage2-FalsePositive / PrecursorCustomerContractCalloffFade", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 0.5, "score_price_alignment": "C12 should not treat precursor/material contract beta as durable Stage2 unless customer call-off, volume visibility, utilization, pricing and margin bridge remain visible. Ecopro Materials had an early MFE but then opened a severe high-MAE drawdown path.", "current_profile_verdict": "source_repair_required_before_runtime_weight", "price_source": "Songdaiki/stock-web", "notes": "Stock-web path usable; non-proxy customer call-off, contract volume, utilization, pricing, inventory and margin bridge evidence required before runtime promotion."}
```

### trigger rows

```jsonl
{"row_type": "trigger", "trigger_id": "TRG_R3L80-C12-361610-SKIET-SEPARATOR-CALLOFF-UTILIZATION-LOCAL4B", "case_id": "R3L80-C12-361610-SKIET-SEPARATOR-CALLOFF-UTILIZATION-LOCAL4B", "symbol": "361610", "company_name": "SK아이이테크놀로지", "round": "R3", "loop": "80", "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK", "fine_archetype_id": "SEPARATOR_COPPERFOIL_PRECURSOR_CUSTOMER_CALLOFF_UTILIZATION_MARGIN_BRIDGE", "loop_objective": "coverage_gap_fill|counterexample_mining|battery_customer_contract_calloff_guardrail", "trigger_type": "Stage4B-Local-SeparatorCustomerCalloffUtilizationHighMAE", "trigger_date": "2024-01-31", "entry_date": "2024-02-01", "entry_price": 73400.0, "evidence_available_at_that_date": "BATTERY_SEPARATOR_CUSTOMER_CALLOFF_UTILIZATION_VOLUME_MARGIN_BRIDGE_WEAK", "evidence_source": "source_proxy_manual_verification_required:SK_IET_2024_SEPARATOR_CUSTOMER_CALLOFF_UTILIZATION_VOLUME_MARGIN_BRIDGE", "stage2_evidence_fields": ["customer_contract_or_calloff_candidate", "utilization_or_volume_candidate", "margin_bridge_candidate"], "stage3_evidence_fields": ["relative_strength", "pricing_inventory_or_customer_quality_candidate"], "stage4b_evidence_fields": ["customer_calloff_risk", "bridge_stale_or_absent", "MAE_widening", "post_peak_drawdown"], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/361/361610/2024.csv", "profile_path": "atlas/symbol_profiles/361/361610.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": 10.08, "MFE_90D_pct": 10.08, "MFE_180D_pct": 10.08, "MAE_30D_pct": -11.31, "MAE_90D_pct": -18.8, "MAE_180D_pct": -59.06, "peak_date": "2024-02-02", "peak_price": 80800.0, "drawdown_after_peak_pct": -62.81, "green_lateness_ratio": null, "four_b_local_peak_proximity": "local_4b_watch_after_battery_material_peak_if_customer_calloff_utilization_or_margin_bridge_fades", "four_b_full_window_peak_proximity": "full_4b_or_4c_requires_non_price_customer_loss_calloff_collapse_inventory_impairment_margin_or_financing_break", "trigger_outcome_label": "risk_positive_separator_calloff_local4b", "current_profile_verdict": "C12 should flag separator/customer-calloff risk when customer volume, utilization, pricing and margin bridge weaken. SK IET produced only a small early MFE and then a deep high-MAE path.", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window_by_profile_or_post_CA_validation_required", "share_count_change_inside_window": false, "same_entry_group_id": "C12_BATTERY_CALLOFF_361610_2024-02-01", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 0.5, "do_not_count_as_new_case": false, "source_proxy_only": true, "evidence_url_pending": true}
{"row_type": "trigger", "trigger_id": "TRG_R3L80-C12-336370-SOLUS-COPPERFOIL-POSTCA-CALLOFF-LIFECYCLE", "case_id": "R3L80-C12-336370-SOLUS-COPPERFOIL-POSTCA-CALLOFF-LIFECYCLE", "symbol": "336370", "company_name": "솔루스첨단소재", "round": "R3", "loop": "80", "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK", "fine_archetype_id": "SEPARATOR_COPPERFOIL_PRECURSOR_CUSTOMER_CALLOFF_UTILIZATION_MARGIN_BRIDGE", "loop_objective": "coverage_gap_fill|counterexample_mining|battery_customer_contract_calloff_guardrail", "trigger_type": "Stage2-Lifecycle-CopperfoilCustomerCalloffPostCABridgeWithLocal4B", "trigger_date": "2024-01-31", "entry_date": "2024-02-01", "entry_price": 11150.0, "evidence_available_at_that_date": "BATTERY_COPPERFOIL_CUSTOMER_VOLUME_UTILIZATION_MARGIN_BRIDGE_POST_CA", "evidence_source": "source_proxy_manual_verification_required:SOLUS_ADVANCED_MATERIALS_2024_COPPERFOIL_CUSTOMER_VOLUME_UTILIZATION_MARGIN_BRIDGE_POST_CA", "stage2_evidence_fields": ["customer_contract_or_calloff_candidate", "utilization_or_volume_candidate", "margin_bridge_candidate"], "stage3_evidence_fields": ["relative_strength", "pricing_inventory_or_customer_quality_candidate"], "stage4b_evidence_fields": ["customer_calloff_risk", "bridge_stale_or_absent", "MAE_widening", "post_peak_drawdown"], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/336/336370/2024.csv", "profile_path": "atlas/symbol_profiles/336/336370.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": 18.83, "MFE_90D_pct": 94.62, "MFE_180D_pct": 110.76, "MAE_30D_pct": -1.26, "MAE_90D_pct": -1.26, "MAE_180D_pct": -1.26, "peak_date": "2024-07-01", "peak_price": 23500.0, "drawdown_after_peak_pct": -52.34, "green_lateness_ratio": null, "four_b_local_peak_proximity": "local_4b_watch_after_battery_material_peak_if_customer_calloff_utilization_or_margin_bridge_fades", "four_b_full_window_peak_proximity": "full_4b_or_4c_requires_non_price_customer_loss_calloff_collapse_inventory_impairment_margin_or_financing_break", "trigger_outcome_label": "positive_post_CA_recovery_with_later_4b_watch", "current_profile_verdict": "C12 should not overblock post-CA copperfoil/material names when recovery MFE and bounded entry MAE are visible, but it still requires customer volume, utilization and margin evidence before Stage2 promotion.", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window_by_profile_or_post_CA_validation_required", "share_count_change_inside_window": false, "same_entry_group_id": "C12_BATTERY_CALLOFF_336370_2024-02-01", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 0.5, "do_not_count_as_new_case": false, "source_proxy_only": true, "evidence_url_pending": true}
{"row_type": "trigger", "trigger_id": "TRG_R3L80-C12-450080-ECOPRO-MATERIALS-PRECURSOR-CALLOFF-FADE", "case_id": "R3L80-C12-450080-ECOPRO-MATERIALS-PRECURSOR-CALLOFF-FADE", "symbol": "450080", "company_name": "에코프로머티", "round": "R3", "loop": "80", "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK", "fine_archetype_id": "SEPARATOR_COPPERFOIL_PRECURSOR_CUSTOMER_CALLOFF_UTILIZATION_MARGIN_BRIDGE", "loop_objective": "coverage_gap_fill|counterexample_mining|battery_customer_contract_calloff_guardrail", "trigger_type": "Stage2-FalsePositive / PrecursorCustomerContractCalloffFade", "trigger_date": "2024-01-31", "entry_date": "2024-02-01", "entry_price": 147000.0, "evidence_available_at_that_date": "BATTERY_PRECURSOR_CUSTOMER_CONTRACT_VOLUME_CALLOFF_UTILIZATION_MARGIN_BRIDGE_WEAK", "evidence_source": "source_proxy_manual_verification_required:ECOPRO_MATERIALS_2024_PRECURSOR_CUSTOMER_CONTRACT_VOLUME_CALLOFF_UTILIZATION_MARGIN_BRIDGE", "stage2_evidence_fields": ["customer_contract_or_calloff_candidate", "utilization_or_volume_candidate", "margin_bridge_candidate"], "stage3_evidence_fields": ["relative_strength", "pricing_inventory_or_customer_quality_candidate"], "stage4b_evidence_fields": ["customer_calloff_risk", "bridge_stale_or_absent", "MAE_widening", "post_peak_drawdown"], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/450/450080/2024.csv", "profile_path": "atlas/symbol_profiles/450/450080.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": 42.52, "MFE_90D_pct": 42.52, "MFE_180D_pct": 42.52, "MAE_30D_pct": -0.68, "MAE_90D_pct": -23.74, "MAE_180D_pct": -52.31, "peak_date": "2024-02-13", "peak_price": 209500.0, "drawdown_after_peak_pct": -66.54, "green_lateness_ratio": null, "four_b_local_peak_proximity": "local_4b_watch_after_battery_material_peak_if_customer_calloff_utilization_or_margin_bridge_fades", "four_b_full_window_peak_proximity": "full_4b_or_4c_requires_non_price_customer_loss_calloff_collapse_inventory_impairment_margin_or_financing_break", "trigger_outcome_label": "counterexample_precursor_contract_calloff_local4b", "current_profile_verdict": "C12 should not treat precursor/material contract beta as durable Stage2 unless customer call-off, volume visibility, utilization, pricing and margin bridge remain visible. Ecopro Materials had an early MFE but then opened a severe high-MAE drawdown path.", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window_by_profile_or_post_CA_validation_required", "share_count_change_inside_window": true, "same_entry_group_id": "C12_BATTERY_CALLOFF_450080_2024-02-01", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 0.5, "do_not_count_as_new_case": false, "source_proxy_only": true, "evidence_url_pending": true}
```

### score simulation rows

```jsonl
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R3L80-C12-361610-SKIET-SEPARATOR-CALLOFF-UTILIZATION-LOCAL4B", "trigger_id": "TRG_R3L80-C12-361610-SKIET-SEPARATOR-CALLOFF-UTILIZATION-LOCAL4B", "symbol": "361610", "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK", "raw_component_scores_before": {"customer_contract_score": 5, "calloff_risk_score": 18, "utilization_score": 4, "pricing_inventory_score": 4, "margin_bridge_score": 2, "relative_strength_score": 3, "execution_risk_score": 23, "validation_risk": 0, "source_confidence_score": 2}, "weighted_score_before": 31, "stage_label_before": "Stage4B-local-watch / no durable Green", "raw_component_scores_after": {"customer_contract_score": 3, "calloff_risk_score": 20, "utilization_score": 2, "pricing_inventory_score": 2, "margin_bridge_score": 1, "relative_strength_score": 2, "execution_risk_score": 25, "validation_risk": 0, "source_confidence_score": 2}, "weighted_score_after": 28, "stage_label_after": "Stage4B-local-watch / no durable Green", "changed_components": ["customer_contract_score", "calloff_risk_score", "utilization_score", "pricing_inventory_score", "margin_bridge_score", "execution_risk_score"], "component_delta_explanation": "Reward only verified customer contract/call-off visibility, utilization, pricing/inventory and margin bridge; route to local 4B when high MAE appears without bridge refresh.", "MFE_90D_pct": 10.08, "MAE_90D_pct": -18.8, "score_return_alignment_label": "battery_customer_calloff_local4b", "current_profile_verdict": "C12 should flag separator/customer-calloff risk when customer volume, utilization, pricing and margin bridge weaken. SK IET produced only a small early MFE and then a deep high-MAE path."}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R3L80-C12-336370-SOLUS-COPPERFOIL-POSTCA-CALLOFF-LIFECYCLE", "trigger_id": "TRG_R3L80-C12-336370-SOLUS-COPPERFOIL-POSTCA-CALLOFF-LIFECYCLE", "symbol": "336370", "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK", "raw_component_scores_before": {"customer_contract_score": 14, "calloff_risk_score": 8, "utilization_score": 14, "pricing_inventory_score": 12, "margin_bridge_score": 13, "relative_strength_score": 12, "execution_risk_score": 10, "validation_risk": 8, "source_confidence_score": 2}, "weighted_score_before": 78, "stage_label_before": "Stage2 candidate after source repair", "raw_component_scores_after": {"customer_contract_score": 16, "calloff_risk_score": 9, "utilization_score": 16, "pricing_inventory_score": 14, "margin_bridge_score": 15, "relative_strength_score": 11, "execution_risk_score": 11, "validation_risk": 10, "source_confidence_score": 2}, "weighted_score_after": 84, "stage_label_after": "Stage2/Yellow after source repair + lifecycle 4B", "changed_components": ["customer_contract_score", "calloff_risk_score", "utilization_score", "pricing_inventory_score", "margin_bridge_score", "execution_risk_score"], "component_delta_explanation": "Reward only verified customer contract/call-off visibility, utilization, pricing/inventory and margin bridge; route to local 4B when high MAE appears without bridge refresh.", "MFE_90D_pct": 94.62, "MAE_90D_pct": -1.26, "score_return_alignment_label": "battery_calloff_positive_with_lifecycle_4b", "current_profile_verdict": "C12 should not overblock post-CA copperfoil/material names when recovery MFE and bounded entry MAE are visible, but it still requires customer volume, utilization and margin evidence before Stage2 promotion."}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R3L80-C12-450080-ECOPRO-MATERIALS-PRECURSOR-CALLOFF-FADE", "trigger_id": "TRG_R3L80-C12-450080-ECOPRO-MATERIALS-PRECURSOR-CALLOFF-FADE", "symbol": "450080", "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK", "raw_component_scores_before": {"customer_contract_score": 5, "calloff_risk_score": 18, "utilization_score": 4, "pricing_inventory_score": 4, "margin_bridge_score": 2, "relative_strength_score": 12, "execution_risk_score": 23, "validation_risk": 8, "source_confidence_score": 2}, "weighted_score_before": 42, "stage_label_before": "Stage4B-local-watch / no durable Green", "raw_component_scores_after": {"customer_contract_score": 3, "calloff_risk_score": 20, "utilization_score": 2, "pricing_inventory_score": 2, "margin_bridge_score": 1, "relative_strength_score": 2, "execution_risk_score": 25, "validation_risk": 10, "source_confidence_score": 2}, "weighted_score_after": 33, "stage_label_after": "Stage4B-local-watch / no durable Green", "changed_components": ["customer_contract_score", "calloff_risk_score", "utilization_score", "pricing_inventory_score", "margin_bridge_score", "execution_risk_score"], "component_delta_explanation": "Reward only verified customer contract/call-off visibility, utilization, pricing/inventory and margin bridge; route to local 4B when high MAE appears without bridge refresh.", "MFE_90D_pct": 42.52, "MAE_90D_pct": -23.74, "score_return_alignment_label": "battery_customer_calloff_local4b", "current_profile_verdict": "C12 should not treat precursor/material contract beta as durable Stage2 unless customer call-off, volume visibility, utilization, pricing and margin bridge remain visible. Ecopro Materials had an early MFE but then opened a severe high-MAE drawdown path."}
```

### aggregate row

```jsonl
{"row_type": "aggregate", "round": "R3", "loop": 80, "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK", "fine_archetype_id": "SEPARATOR_COPPERFOIL_PRECURSOR_CUSTOMER_CALLOFF_UTILIZATION_MARGIN_BRIDGE", "calibration_usable_case_count": 3, "calibration_usable_trigger_count": 3, "new_independent_case_count": 3, "reused_case_count": 0, "same_archetype_new_symbol_count": 3, "same_archetype_new_trigger_family_count": 3, "positive_case_count": 1, "risk_positive_case_count": 1, "counterexample_count": 1, "four_b_case_count": 3, "four_c_case_count": 0, "source_proxy_only_count": 3, "evidence_url_pending_count": 3, "share_count_change_inside_window_count": 1, "post_corporate_action_validation_count": 1, "current_profile_error_count": 1, "diversity_score_summary": "+3 C12 battery separator/copperfoil/precursor symbols outside top-covered 247540/278280/003670 set, +3 separator/copperfoil/precursor trigger families, +1 post-CA recovery candidate, +2 customer calloff local-4B paths, no hard duplicate", "residual_contribution_label": "coverage_gap_fill_with_source_repair_CA_and_sharecount_validation_needed"}
```

### shadow weight row

```jsonl
{"row_type": "shadow_weight", "round": "R3", "loop": 80, "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK", "axis": "separator_copperfoil_precursor_customer_calloff_utilization_margin_bridge", "decision": "hold_for_source_repair_and_more_evidence", "proposed_runtime_effect": "C12 should split verified post-CA/customer-volume recovery from battery material call-off risk. Stage2 requires customer contract/call-off visibility, utilization, pricing/inventory and margin bridge. Local 4B triggers when customer call-off or utilization/margin bridge is weak and MAE_90D/180D or post-peak drawdown widens. CA/share-count flags require validation before runtime promotion.", "do_not_propose_new_weight_delta": true, "needs_more_evidence": true, "source_repair_required": ["361610", "336370", "450080"], "post_corporate_action_validation_required": ["336370"], "share_count_validation_required": ["450080"]}
```

### residual contribution row

```jsonl
{"row_type": "residual_contribution", "round": "R3", "loop": 80, "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK", "existing_axis_strengthened": ["stage2_required_bridge", "customer_calloff_local_4b_guard", "post_corporate_action_validation_guard", "share_count_validation_guard", "blanket_EV_material_overbearish_guard", "full_4b_or_4c_requires_non_price_evidence"], "new_axis_proposed": null, "sector_specific_rule_candidate": true, "canonical_archetype_rule_candidate": true, "narrative_summary": "C12 needs customer call-off, utilization, pricing/inventory and margin proof. SK IET and Ecopro Materials show high-MAE call-off local-4B paths; Solus Advanced Materials shows a post-CA recovery candidate that should not be overblocked before source repair and continuity validation."}
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
361610:
  name = SK아이이테크놀로지
  corporate_action_candidate_dates = none
  selected window = 2024-02-01~D+180
  contamination = false

336370:
  name = 솔루스첨단소재 from 2020-12-24, 두산솔루스 before that
  corporate_action_candidate_dates = 2024-01-08, 2024-01-30
  selected entry starts 2024-02-01 after the 2024-01-30 candidate
  contamination = false after post-CA entry, but coding-agent validation required

450080:
  name = 에코프로머티
  corporate_action_candidate_dates = none
  selected window = 2024-02-01~D+180
  contamination = false by profile
  share_count_change_inside_window = true → coding-agent validation required
```

Data-quality caveat:

```text
All selected C12 rows are source_proxy_only / evidence_url_pending.
336370 requires post-corporate-action validation.
450080 requires share-count validation before runtime promotion.
This MD is useful for stock-web path calibration and C12 rule-shape discovery,
but coding-agent promotion requires non-proxy customer call-off, contract volume, utilization, pricing, inventory and margin evidence.
```

---

## Deferred Coding Agent Handoff Prompt

Do not execute this now.

```text
You are the coding agent for Songdaiki/stock_agent.

Read this standalone v12 residual research MD and ingest machine-readable rows only after validation.

Do not patch production scoring blindly.
This R3/C12 artifact is marked do_not_propose_new_weight_delta=true because all rows need source repair, 336370 needs post-CA validation, and 450080 needs share-count validation.

Candidate axis:
separator_copperfoil_precursor_customer_calloff_utilization_margin_bridge

Required checks before implementation:
1. Validate all trigger rows against stock-web tradable_raw OHLC shards.
2. Confirm no hard duplicate key:
   canonical_archetype_id + symbol + trigger_type + entry_date.
3. Verify non-proxy source URLs for 361610, 336370 and 450080.
4. Validate 336370 post-CA continuity after 2024-01-30.
5. Validate 450080 share-count changes inside the selected window.
6. Keep generic C12 customer-contract/call-off weight unchanged until source repair is complete.
7. Consider Stage2 only when:
   - customer contract or supply agreement is explicit,
   - actual call-off / shipment volume is visible,
   - utilization or inventory absorption is visible,
   - pricing and margin bridge are credible,
   - MAE remains controlled or the signal is lifecycle-managed.
8. Consider local 4B-watch when:
   - customer call-off or utilization risk is visible,
   - margin evidence is weak or stale,
   - MAE_90D <= -20% or MAE_180D <= -25%,
   - post-peak drawdown <= -35%.
9. Do not convert local 4B-watch into full 4B/4C without non-price customer loss, call-off collapse, inventory impairment, financing or margin break.
10. Emit before/after diagnostics and reject if verified post-CA recovery rows are overblocked.
```

---

## Final round state

```text
completed_round = R3
completed_loop = 80
next_round = R4
next_loop = 80
round_schedule_status = valid
round_sector_consistency = pass
```

