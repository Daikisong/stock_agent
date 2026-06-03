# E2R Stock-Web v12 Residual Research — R11 Loop 76 / L10 / C31

## Metadata

```json
{
  "research_session": "post_calibrated_sector_archetype_residual_research",
  "mode": "historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12",
  "scheduled_round": "R11",
  "scheduled_loop": 76,
  "round_schedule_status": "valid",
  "round_sector_consistency": "pass",
  "completed_round": "R11",
  "completed_loop": 76,
  "computed_next_round": "R12",
  "computed_next_loop": 76,
  "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC",
  "canonical_archetype_id": "C31_POLICY_SUBSIDY_LEGISLATION_EVENT",
  "fine_archetype_id": "EAST_SEA_GAS_FIELD_PIPE_VALVE_INFRA_POLICY_EVENT_BRIDGE_VS_RESOURCE_THEME_FADE",
  "loop_objective": [
    "coverage_gap_fill",
    "counterexample_mining",
    "policy_event_bridge_guardrail",
    "4B_non_price_requirement_stress_test",
    "resource_policy_direct_beneficiary_mapping",
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

Previous completed state in this interactive run: R10 / loop 76.

Therefore:

```text
scheduled_round = R11
scheduled_loop = 76
allowed_large_sector = L10_POLICY_EVENT_CROSS_REDTEAM_MISC or L1 policy-defense linkage
selected_large_sector = L10_POLICY_EVENT_CROSS_REDTEAM_MISC
selected_canonical_archetype_id = C31_POLICY_SUBSIDY_LEGISLATION_EVENT
computed_next_round = R12
computed_next_loop = 76
```

R11 was routed to C31 because this is a resource-development policy event bridge guardrail, not a normal materials or construction operating-leverage round.

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

This run uses three different symbols:

```text
039610 / 화성밸브 / East Sea gas-field policy valve direct-beneficiary lifecycle
008970 / 동양철관 / East Sea gas-field pipe policy beta fade
071090 / 하이스틸 / East Sea gas-field steel-pipe policy beta fade
```

Data-quality note:

```text
All three rows are stock-web calibration usable by profile-level corporate-action candidates.
All three rows are source_proxy_only=true / evidence_url_pending=true.
008970 shows share-count changes inside the selected window and requires coding-agent validation before runtime promotion.
```

## Research thesis

C31 is not “policy headline went up.”

For resource-development policy rows, the bridge must pass through:

```text
policy / exploration / resource-development announcement
→ direct beneficiary mapping
→ project order / delivery schedule
→ revenue / margin bridge
→ durable rerating
```

A policy headline is a flare in the dark.  
The investment bridge is whether a purchase order, delivery slot and margin actually follow the flare.

---

## Case 1 — Policy lifecycle candidate: 039610 / 화성밸브

### Evidence status

```text
source_proxy_only = true
evidence_url_pending = true
source_repair_required = true
```

The source-repair task is direct valve/pipeline beneficiary mapping, actual project order, delivery schedule, revenue and margin bridge evidence.

```text
evidence_family = EAST_SEA_GAS_FIELD_POLICY_VALVE_PIPELINE_INFRA_ORDER_REVENUE_MARGIN_BRIDGE_CANDIDATE
case_role = policy_lifecycle_positive_with_later_4b_watch
trigger_date = 2024-06-03
entry_date = 2024-06-04
entry_price = 8,630
```

### Stock-Web price path

Observed rows from `atlas/ohlcv_tradable_by_symbol_year/039/039610/2024.csv`:

```text
2024-06-03,5150,6640,5140,6640
2024-06-04,8630,8630,8310,8630
2024-06-05,8330,11080,7800,9870
2024-07-23,9550,12070,9350,10990
2024-08-23,13410,15420,13400,14110
2024-12-04,8990,9420,7490,7500
```

### Backtest

```text
MFE_30D  = +39.86%
MAE_30D  = -18.31%
MFE_90D  = +78.68%
MAE_90D  = -18.31%
MFE_180D = +78.68%
MAE_180D = -18.31%
peak_180 = 15,420 on 2024-08-23
trough_180 = 7,050 on 2024-07-01
peak_to_later_drawdown = -51.43%
```

### Interpretation

This is the policy lifecycle winner.  
The policy shock created real tradable MFE. But it cannot become permanent Green unless order/revenue/margin bridge is repaired.

Correct treatment:

```text
source repair first
possible policy lifecycle Stage2-Yellow
later local 4B if direct-order/revenue bridge fades
```

---

## Case 2 — Counterexample / local 4B: 008970 / 동양철관

### Evidence status

```text
source_proxy_only = true
evidence_url_pending = true
share_count_change_inside_window = true
source_repair_required = true
```

This row tests East Sea gas-field / pipeline policy beta without enough actual order and revenue bridge.

```text
evidence_family = EAST_SEA_GAS_FIELD_POLICY_PIPELINE_THEME_WITH_WEAK_ACTUAL_ORDER_REVENUE_MARGIN_BRIDGE
case_role = counterexample_policy_proxy_local4b_with_sharecount_validation
trigger_date = 2024-06-03
entry_date = 2024-06-04
entry_price = 1,175
```

### Stock-Web price path

Observed rows from `atlas/ohlcv_tradable_by_symbol_year/008/008970/2024.csv`:

```text
2024-06-03,697,904,697,904
2024-06-04,1175,1175,1175,1175
2024-06-05,1414,1527,1351,1527
2024-06-07,1610,1678,1285,1411
2024-07-02,1072,1136,997,1000
2024-08-05,985,987,826,890
```

### Backtest

```text
MFE_30D  = +42.81%
MAE_30D  = -14.30%
MFE_90D  = +42.81%
MAE_90D  = -29.70%
MFE_180D = +42.81%
MAE_180D = -29.70%
peak_180 = 1,678 on 2024-06-07
trough_180 = 826 on 2024-08-05
peak_to_later_drawdown = -50.77%
```

### Interpretation

This is a policy-proxy false positive.  
The entry had strong MFE, but the later MAE and share-count changes make runtime promotion unsafe.

Correct treatment:

```text
pipeline policy beta
→ no confirmed order/revenue/margin bridge
→ local 4B-watch
```

---

## Case 3 — Counterexample / local 4B: 071090 / 하이스틸

### Evidence status

```text
source_proxy_only = true
evidence_url_pending = true
source_repair_required = true
```

This row tests steel-pipe / resource-development policy beta without enough project order and margin bridge.

```text
evidence_family = EAST_SEA_GAS_FIELD_POLICY_STEEL_PIPE_THEME_WITH_WEAK_PROJECT_ORDER_MARGIN_BRIDGE
case_role = counterexample_policy_proxy_local4b
trigger_date = 2024-06-03
entry_date = 2024-06-04
entry_price = 4,500
```

### Stock-Web price path

Observed rows from `atlas/ohlcv_tradable_by_symbol_year/071/071090/2024.csv`:

```text
2024-06-03,3480,4345,3480,4185
2024-06-04,4500,4945,4120,4235
2024-06-05,4160,5330,4005,4800
2024-06-19,3960,4635,3845,4165
2024-07-12,3540,3570,3500,3500
2024-08-05,3405,3460,2880,2995
```

### Backtest

```text
MFE_30D  = +18.44%
MAE_30D  = -16.67%
MFE_90D  = +18.44%
MAE_90D  = -36.00%
MFE_180D = +18.44%
MAE_180D = -36.00%
peak_180 = 5,330 on 2024-06-05
trough_180 = 2,880 on 2024-08-05
peak_to_later_drawdown = -45.97%
```

### Interpretation

This is the steel-pipe policy beta fade.  
The first move was not enough to validate Stage2, and the MAE opened quickly.

Correct treatment:

```text
resource-development headline
→ no direct project order / margin bridge
→ local 4B-watch
```

---

## Cross-case residual finding

### What this strengthens

```text
price_only_blowoff_blocks_positive_stage = strengthen
local_4b_watch_guard = strengthen
stage2_required_bridge = strengthen
full_4b_requires_non_price_evidence = keep
share_count_validation_guard = strengthen
```

### What this does not justify

```text
do_not_raise_generic_C31_resource_policy_weight = true
do_not_treat_East_Sea_gas_field_headline_as_Green_without_order_bridge = true
do_not_convert_policy_proxy_drawdown_to_hard_4C_without_non_price_project_failure_or_margin_break = true
```

### Candidate canonical compression

Fine labels can compress into:

```text
EAST_SEA_GAS_FIELD_PIPE_VALVE_INFRA_POLICY_EVENT_BRIDGE_VS_RESOURCE_THEME_FADE
```

This fine archetype covers:

```text
1. valve / pipeline direct-beneficiary policy MFE → policy lifecycle candidate after source repair
2. pipe policy proxy without order/revenue bridge → false Stage2 / local 4B
3. steel-pipe resource-policy beta without project-order bridge → false Stage2 / local 4B
```

---

## Machine-readable rows

### price source validation row

```jsonl
{"row_type": "price_source_validation", "source": "Songdaiki/stock-web", "source_url": "https://github.com/Songdaiki/stock-web", "manifest_path": "atlas/manifest.json", "schema_path": "atlas/schema.json", "universe_path": "atlas/universe/all_symbols.csv", "manifest_max_date": "2026-02-20", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "raw_shard_root": "atlas/ohlcv_raw_by_symbol_year", "validation_status": "usable_for_historical_calibration"}
```

### case rows

```jsonl
{"row_type": "case", "case_id": "R11L76-C31-039610-HWASEONG-VALVE-EASTSEA-GAS-POLICY-LIFECYCLE", "symbol": "039610", "company_name": "화성밸브", "round": "R11", "loop": "76", "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "C31_POLICY_SUBSIDY_LEGISLATION_EVENT", "fine_archetype_id": "EAST_SEA_GAS_FIELD_PIPE_VALVE_INFRA_POLICY_EVENT_BRIDGE_VS_RESOURCE_THEME_FADE", "case_type": "policy_subsidy_legislation_event_resource_infra", "positive_or_counterexample": "policy_lifecycle_positive", "best_trigger": "Stage2-PolicyLifecycle-EastSeaGasFieldValveDirectBeneficiaryBridge", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 0.5, "score_price_alignment": "C31 can allow a policy-event lifecycle candidate when a gas-field/resource-development policy shock maps to a direct valve/pipeline beneficiary and then to actual order, project schedule, revenue and margin bridge. Hwaseong Valve produced large MFE, but post-peak drawdown requires lifecycle local 4B if the policy-to-order bridge fades.", "current_profile_verdict": "source_repair_required_before_runtime_weight", "price_source": "Songdaiki/stock-web", "notes": "Stock-web path usable; non-proxy policy event, direct beneficiary mapping, actual project order, revenue, delivery schedule and margin bridge required before runtime promotion."}
{"row_type": "case", "case_id": "R11L76-C31-008970-DONGYANG-STEEL-PIPE-EASTSEA-GAS-POLICY-PIPE-BETA-FADE", "symbol": "008970", "company_name": "동양철관", "round": "R11", "loop": "76", "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "C31_POLICY_SUBSIDY_LEGISLATION_EVENT", "fine_archetype_id": "EAST_SEA_GAS_FIELD_PIPE_VALVE_INFRA_POLICY_EVENT_BRIDGE_VS_RESOURCE_THEME_FADE", "case_type": "policy_subsidy_legislation_event_resource_infra", "positive_or_counterexample": "counterexample", "best_trigger": "Stage2-FalsePositive / EastSeaGasFieldPipePolicyBetaFade", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 0.5, "score_price_alignment": "C31 should not treat gas-field / pipeline policy beta as durable Stage2 unless direct beneficiary mapping, confirmed order, project schedule, revenue and margin bridge are visible. Dongyang Steel Pipe had a tradable MFE but then high MAE and repeated share-count movement, making it local 4B rather than Green.", "current_profile_verdict": "source_repair_required_before_runtime_weight", "price_source": "Songdaiki/stock-web", "notes": "Stock-web path usable; non-proxy policy event, direct beneficiary mapping, actual project order, revenue, delivery schedule and margin bridge required before runtime promotion."}
{"row_type": "case", "case_id": "R11L76-C31-071090-HISTEEL-EASTSEA-GAS-POLICY-PIPE-BETA-FADE", "symbol": "071090", "company_name": "하이스틸", "round": "R11", "loop": "76", "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "C31_POLICY_SUBSIDY_LEGISLATION_EVENT", "fine_archetype_id": "EAST_SEA_GAS_FIELD_PIPE_VALVE_INFRA_POLICY_EVENT_BRIDGE_VS_RESOURCE_THEME_FADE", "case_type": "policy_subsidy_legislation_event_resource_infra", "positive_or_counterexample": "counterexample", "best_trigger": "Stage2-FalsePositive / EastSeaGasFieldSteelPipePolicyBetaFade", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 0.5, "score_price_alignment": "C31 should not treat steel-pipe/resource-policy beta as durable Stage2 unless actual project order, customer, delivery schedule and margin bridge is visible. Hi Steel produced a small MFE and then a large MAE drawdown, making it a policy-proxy local 4B row.", "current_profile_verdict": "source_repair_required_before_runtime_weight", "price_source": "Songdaiki/stock-web", "notes": "Stock-web path usable; non-proxy policy event, direct beneficiary mapping, actual project order, revenue, delivery schedule and margin bridge required before runtime promotion."}
```

### trigger rows

```jsonl
{"row_type": "trigger", "trigger_id": "TRG_R11L76-C31-039610-HWASEONG-VALVE-EASTSEA-GAS-POLICY-LIFECYCLE", "case_id": "R11L76-C31-039610-HWASEONG-VALVE-EASTSEA-GAS-POLICY-LIFECYCLE", "symbol": "039610", "company_name": "화성밸브", "round": "R11", "loop": "76", "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "C31_POLICY_SUBSIDY_LEGISLATION_EVENT", "fine_archetype_id": "EAST_SEA_GAS_FIELD_PIPE_VALVE_INFRA_POLICY_EVENT_BRIDGE_VS_RESOURCE_THEME_FADE", "loop_objective": "coverage_gap_fill|counterexample_mining|policy_event_bridge_guardrail", "trigger_type": "Stage2-PolicyLifecycle-EastSeaGasFieldValveDirectBeneficiaryBridge", "trigger_date": "2024-06-03", "entry_date": "2024-06-04", "entry_price": 8630.0, "evidence_available_at_that_date": "EAST_SEA_GAS_FIELD_POLICY_VALVE_PIPELINE_INFRA_ORDER_REVENUE_MARGIN_BRIDGE_CANDIDATE", "evidence_source": "source_proxy_manual_verification_required:HWASEONG_VALVE_2024_EAST_SEA_GAS_FIELD_POLICY_VALVE_PIPELINE_ORDER_REVENUE_MARGIN_BRIDGE", "stage2_evidence_fields": ["policy_event", "direct_beneficiary_mapping_candidate", "project_order_revenue_margin_bridge_candidate"], "stage3_evidence_fields": ["relative_strength", "delivery_schedule_or_customer_bridge_candidate"], "stage4b_evidence_fields": ["policy_proxy_beta", "bridge_stale_or_absent", "MAE_widening", "post_peak_drawdown"], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/039/039610/2024.csv", "profile_path": "atlas/symbol_profiles/039/039610.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": 39.86, "MFE_90D_pct": 78.68, "MFE_180D_pct": 78.68, "MAE_30D_pct": -18.31, "MAE_90D_pct": -18.31, "MAE_180D_pct": -18.31, "peak_date": "2024-08-23", "peak_price": 15420.0, "drawdown_after_peak_pct": -51.43, "green_lateness_ratio": null, "four_b_local_peak_proximity": "local_4b_watch_after_policy_infra_peak_if_direct_order_or_revenue_bridge_fades", "four_b_full_window_peak_proximity": "full_4b_requires_non_price_project_cancellation_order_failure_revenue_margin_or_financing_break", "trigger_outcome_label": "policy_lifecycle_positive_with_later_4b_watch", "current_profile_verdict": "C31 can allow a policy-event lifecycle candidate when a gas-field/resource-development policy shock maps to a direct valve/pipeline beneficiary and then to actual order, project schedule, revenue and margin bridge. Hwaseong Valve produced large MFE, but post-peak drawdown requires lifecycle local 4B if the policy-to-order bridge fades.", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window_by_profile", "share_count_change_inside_window": false, "same_entry_group_id": "C31_EAST_SEA_GAS_FIELD_POLICY_20240604_GROUP", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 0.5, "do_not_count_as_new_case": false, "source_proxy_only": true, "evidence_url_pending": true}
{"row_type": "trigger", "trigger_id": "TRG_R11L76-C31-008970-DONGYANG-STEEL-PIPE-EASTSEA-GAS-POLICY-PIPE-BETA-FADE", "case_id": "R11L76-C31-008970-DONGYANG-STEEL-PIPE-EASTSEA-GAS-POLICY-PIPE-BETA-FADE", "symbol": "008970", "company_name": "동양철관", "round": "R11", "loop": "76", "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "C31_POLICY_SUBSIDY_LEGISLATION_EVENT", "fine_archetype_id": "EAST_SEA_GAS_FIELD_PIPE_VALVE_INFRA_POLICY_EVENT_BRIDGE_VS_RESOURCE_THEME_FADE", "loop_objective": "coverage_gap_fill|counterexample_mining|policy_event_bridge_guardrail", "trigger_type": "Stage2-FalsePositive / EastSeaGasFieldPipePolicyBetaFade", "trigger_date": "2024-06-03", "entry_date": "2024-06-04", "entry_price": 1175.0, "evidence_available_at_that_date": "EAST_SEA_GAS_FIELD_POLICY_PIPELINE_THEME_WITH_WEAK_ACTUAL_ORDER_REVENUE_MARGIN_BRIDGE", "evidence_source": "source_proxy_manual_verification_required:DONGYANG_STEEL_PIPE_2024_EAST_SEA_GAS_FIELD_POLICY_PIPELINE_ORDER_REVENUE_MARGIN_BRIDGE", "stage2_evidence_fields": ["policy_event", "direct_beneficiary_mapping_candidate", "project_order_revenue_margin_bridge_candidate"], "stage3_evidence_fields": ["relative_strength", "delivery_schedule_or_customer_bridge_candidate"], "stage4b_evidence_fields": ["policy_proxy_beta", "bridge_stale_or_absent", "MAE_widening", "post_peak_drawdown"], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/008/008970/2024.csv", "profile_path": "atlas/symbol_profiles/008/008970.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": 42.81, "MFE_90D_pct": 42.81, "MFE_180D_pct": 42.81, "MAE_30D_pct": -14.3, "MAE_90D_pct": -29.7, "MAE_180D_pct": -29.7, "peak_date": "2024-06-07", "peak_price": 1678.0, "drawdown_after_peak_pct": -50.77, "green_lateness_ratio": null, "four_b_local_peak_proximity": "local_4b_watch_after_policy_infra_peak_if_direct_order_or_revenue_bridge_fades", "four_b_full_window_peak_proximity": "full_4b_requires_non_price_project_cancellation_order_failure_revenue_margin_or_financing_break", "trigger_outcome_label": "counterexample_policy_proxy_local4b_with_sharecount_validation", "current_profile_verdict": "C31 should not treat gas-field / pipeline policy beta as durable Stage2 unless direct beneficiary mapping, confirmed order, project schedule, revenue and margin bridge are visible. Dongyang Steel Pipe had a tradable MFE but then high MAE and repeated share-count movement, making it local 4B rather than Green.", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window_by_profile", "share_count_change_inside_window": true, "same_entry_group_id": "C31_EAST_SEA_GAS_FIELD_POLICY_20240604_GROUP", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 0.5, "do_not_count_as_new_case": false, "source_proxy_only": true, "evidence_url_pending": true}
{"row_type": "trigger", "trigger_id": "TRG_R11L76-C31-071090-HISTEEL-EASTSEA-GAS-POLICY-PIPE-BETA-FADE", "case_id": "R11L76-C31-071090-HISTEEL-EASTSEA-GAS-POLICY-PIPE-BETA-FADE", "symbol": "071090", "company_name": "하이스틸", "round": "R11", "loop": "76", "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "C31_POLICY_SUBSIDY_LEGISLATION_EVENT", "fine_archetype_id": "EAST_SEA_GAS_FIELD_PIPE_VALVE_INFRA_POLICY_EVENT_BRIDGE_VS_RESOURCE_THEME_FADE", "loop_objective": "coverage_gap_fill|counterexample_mining|policy_event_bridge_guardrail", "trigger_type": "Stage2-FalsePositive / EastSeaGasFieldSteelPipePolicyBetaFade", "trigger_date": "2024-06-03", "entry_date": "2024-06-04", "entry_price": 4500.0, "evidence_available_at_that_date": "EAST_SEA_GAS_FIELD_POLICY_STEEL_PIPE_THEME_WITH_WEAK_PROJECT_ORDER_MARGIN_BRIDGE", "evidence_source": "source_proxy_manual_verification_required:HISTEEL_2024_EAST_SEA_GAS_FIELD_POLICY_STEEL_PIPE_PROJECT_ORDER_MARGIN_BRIDGE", "stage2_evidence_fields": ["policy_event", "direct_beneficiary_mapping_candidate", "project_order_revenue_margin_bridge_candidate"], "stage3_evidence_fields": ["relative_strength", "delivery_schedule_or_customer_bridge_candidate"], "stage4b_evidence_fields": ["policy_proxy_beta", "bridge_stale_or_absent", "MAE_widening", "post_peak_drawdown"], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/071/071090/2024.csv", "profile_path": "atlas/symbol_profiles/071/071090.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": 18.44, "MFE_90D_pct": 18.44, "MFE_180D_pct": 18.44, "MAE_30D_pct": -16.67, "MAE_90D_pct": -36.0, "MAE_180D_pct": -36.0, "peak_date": "2024-06-05", "peak_price": 5330.0, "drawdown_after_peak_pct": -45.97, "green_lateness_ratio": null, "four_b_local_peak_proximity": "local_4b_watch_after_policy_infra_peak_if_direct_order_or_revenue_bridge_fades", "four_b_full_window_peak_proximity": "full_4b_requires_non_price_project_cancellation_order_failure_revenue_margin_or_financing_break", "trigger_outcome_label": "counterexample_policy_proxy_local4b", "current_profile_verdict": "C31 should not treat steel-pipe/resource-policy beta as durable Stage2 unless actual project order, customer, delivery schedule and margin bridge is visible. Hi Steel produced a small MFE and then a large MAE drawdown, making it a policy-proxy local 4B row.", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window_by_profile", "share_count_change_inside_window": false, "same_entry_group_id": "C31_EAST_SEA_GAS_FIELD_POLICY_20240604_GROUP", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 0.5, "do_not_count_as_new_case": false, "source_proxy_only": true, "evidence_url_pending": true}
```

### score simulation rows

```jsonl
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R11L76-C31-039610-HWASEONG-VALVE-EASTSEA-GAS-POLICY-LIFECYCLE", "trigger_id": "TRG_R11L76-C31-039610-HWASEONG-VALVE-EASTSEA-GAS-POLICY-LIFECYCLE", "symbol": "039610", "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "C31_POLICY_SUBSIDY_LEGISLATION_EVENT", "raw_component_scores_before": {"policy_or_regulatory_score": 15, "direct_beneficiary_mapping_score": 12, "actual_order_score": 10, "revenue_bridge_score": 10, "margin_bridge_score": 9, "relative_strength_score": 14, "execution_risk_score": 11, "dilution_or_sharecount_validation_risk": 0, "source_confidence_score": 2}, "weighted_score_before": 70, "stage_label_before": "Policy lifecycle candidate after source repair", "raw_component_scores_after": {"policy_or_regulatory_score": 9, "direct_beneficiary_mapping_score": 15, "actual_order_score": 14, "revenue_bridge_score": 13, "margin_bridge_score": 12, "relative_strength_score": 12, "execution_risk_score": 12, "dilution_or_sharecount_validation_risk": 0, "source_confidence_score": 2}, "weighted_score_after": 76, "stage_label_after": "Policy lifecycle Stage2-Yellow after source repair + local 4B", "changed_components": ["policy_or_regulatory_score", "direct_beneficiary_mapping_score", "actual_order_score", "revenue_bridge_score", "execution_risk_score"], "component_delta_explanation": "Cap policy/event scores unless the resource-development headline maps to direct beneficiary economics, actual project order, revenue and margin bridge.", "MFE_90D_pct": 78.68, "MAE_90D_pct": -18.31, "score_return_alignment_label": "policy_lifecycle_with_later_4b", "current_profile_verdict": "C31 can allow a policy-event lifecycle candidate when a gas-field/resource-development policy shock maps to a direct valve/pipeline beneficiary and then to actual order, project schedule, revenue and margin bridge. Hwaseong Valve produced large MFE, but post-peak drawdown requires lifecycle local 4B if the policy-to-order bridge fades."}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R11L76-C31-008970-DONGYANG-STEEL-PIPE-EASTSEA-GAS-POLICY-PIPE-BETA-FADE", "trigger_id": "TRG_R11L76-C31-008970-DONGYANG-STEEL-PIPE-EASTSEA-GAS-POLICY-PIPE-BETA-FADE", "symbol": "008970", "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "C31_POLICY_SUBSIDY_LEGISLATION_EVENT", "raw_component_scores_before": {"policy_or_regulatory_score": 15, "direct_beneficiary_mapping_score": 4, "actual_order_score": 2, "revenue_bridge_score": 2, "margin_bridge_score": 1, "relative_strength_score": 14, "execution_risk_score": 20, "dilution_or_sharecount_validation_risk": 9, "source_confidence_score": 2}, "weighted_score_before": 50, "stage_label_before": "Stage2-FalsePositive / local 4B-watch", "raw_component_scores_after": {"policy_or_regulatory_score": 9, "direct_beneficiary_mapping_score": 2, "actual_order_score": 1, "revenue_bridge_score": 1, "margin_bridge_score": 1, "relative_strength_score": 4, "execution_risk_score": 22, "dilution_or_sharecount_validation_risk": 11, "source_confidence_score": 2}, "weighted_score_after": 37, "stage_label_after": "Stage4B-local-watch / no durable Green", "changed_components": ["policy_or_regulatory_score", "direct_beneficiary_mapping_score", "actual_order_score", "revenue_bridge_score", "execution_risk_score"], "component_delta_explanation": "Cap policy/event scores unless the resource-development headline maps to direct beneficiary economics, actual project order, revenue and margin bridge.", "MFE_90D_pct": 42.81, "MAE_90D_pct": -29.7, "score_return_alignment_label": "policy_proxy_false_positive_bridge_gap", "current_profile_verdict": "C31 should not treat gas-field / pipeline policy beta as durable Stage2 unless direct beneficiary mapping, confirmed order, project schedule, revenue and margin bridge are visible. Dongyang Steel Pipe had a tradable MFE but then high MAE and repeated share-count movement, making it local 4B rather than Green."}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R11L76-C31-071090-HISTEEL-EASTSEA-GAS-POLICY-PIPE-BETA-FADE", "trigger_id": "TRG_R11L76-C31-071090-HISTEEL-EASTSEA-GAS-POLICY-PIPE-BETA-FADE", "symbol": "071090", "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "C31_POLICY_SUBSIDY_LEGISLATION_EVENT", "raw_component_scores_before": {"policy_or_regulatory_score": 15, "direct_beneficiary_mapping_score": 4, "actual_order_score": 2, "revenue_bridge_score": 2, "margin_bridge_score": 1, "relative_strength_score": 7, "execution_risk_score": 20, "dilution_or_sharecount_validation_risk": 0, "source_confidence_score": 2}, "weighted_score_before": 50, "stage_label_before": "Stage2-FalsePositive / local 4B-watch", "raw_component_scores_after": {"policy_or_regulatory_score": 9, "direct_beneficiary_mapping_score": 2, "actual_order_score": 1, "revenue_bridge_score": 1, "margin_bridge_score": 1, "relative_strength_score": 4, "execution_risk_score": 22, "dilution_or_sharecount_validation_risk": 0, "source_confidence_score": 2}, "weighted_score_after": 37, "stage_label_after": "Stage4B-local-watch / no durable Green", "changed_components": ["policy_or_regulatory_score", "direct_beneficiary_mapping_score", "actual_order_score", "revenue_bridge_score", "execution_risk_score"], "component_delta_explanation": "Cap policy/event scores unless the resource-development headline maps to direct beneficiary economics, actual project order, revenue and margin bridge.", "MFE_90D_pct": 18.44, "MAE_90D_pct": -36.0, "score_return_alignment_label": "policy_proxy_false_positive_bridge_gap", "current_profile_verdict": "C31 should not treat steel-pipe/resource-policy beta as durable Stage2 unless actual project order, customer, delivery schedule and margin bridge is visible. Hi Steel produced a small MFE and then a large MAE drawdown, making it a policy-proxy local 4B row."}
```

### aggregate row

```jsonl
{"row_type": "aggregate", "round": "R11", "loop": 76, "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "C31_POLICY_SUBSIDY_LEGISLATION_EVENT", "fine_archetype_id": "EAST_SEA_GAS_FIELD_PIPE_VALVE_INFRA_POLICY_EVENT_BRIDGE_VS_RESOURCE_THEME_FADE", "calibration_usable_case_count": 3, "calibration_usable_trigger_count": 3, "new_independent_case_count": 3, "reused_case_count": 0, "same_archetype_new_symbol_count": 3, "same_archetype_new_trigger_family_count": 1, "positive_case_count": 1, "counterexample_count": 2, "four_b_case_count": 3, "four_c_case_count": 0, "source_proxy_only_count": 3, "evidence_url_pending_count": 3, "share_count_change_inside_window_count": 1, "current_profile_error_count": 2, "diversity_score_summary": "+3 underused C31 resource-policy infrastructure symbols outside top-covered C31 set, +1 East Sea gas-field policy trigger family, +1 valve policy lifecycle MFE winner, +2 pipe policy-proxy local-4B counterexamples, no hard duplicate", "residual_contribution_label": "policy_event_bridge_guardrail_with_source_repair_and_sharecount_validation_needed"}
```

### shadow weight row

```jsonl
{"row_type": "shadow_weight", "round": "R11", "loop": 76, "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "C31_POLICY_SUBSIDY_LEGISLATION_EVENT", "axis": "east_sea_gas_field_pipe_valve_infra_policy_event_bridge_vs_resource_theme_fade", "decision": "hold_for_source_repair_and_more_evidence", "proposed_runtime_effect": "C31 should split resource policy-event beneficiary bridges from pipe/valve theme beta. Stage2 requires explicit policy event plus direct beneficiary mapping, project order, delivery schedule, revenue and margin bridge. If MFE fades and MAE/post-peak drawdown opens without bridge refresh, route to local 4B-watch. Share-count changes require validation before runtime promotion.", "do_not_propose_new_weight_delta": true, "needs_more_evidence": true, "source_repair_required": ["039610", "008970", "071090"], "share_count_validation_required": ["008970"]}
```

### residual contribution row

```jsonl
{"row_type": "residual_contribution", "round": "R11", "loop": 76, "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "C31_POLICY_SUBSIDY_LEGISLATION_EVENT", "existing_axis_strengthened": ["price_only_blowoff_blocks_positive_stage", "local_4b_watch_guard", "stage2_required_bridge", "full_4b_requires_non_price_evidence", "share_count_validation_guard"], "new_axis_proposed": null, "sector_specific_rule_candidate": true, "canonical_archetype_rule_candidate": true, "narrative_summary": "C31 resource policy events need direct-order/revenue proof. Hwaseong Valve shows an East Sea gas-field policy lifecycle MFE winner; Dongyang Steel Pipe and Hi Steel show pipe policy beta fading into local 4B when direct order, revenue and margin bridge are absent."}
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
039610:
  corporate_action_candidate_dates = 2001-12-17, 2002-07-15, 2004-01-12, 2004-03-26, 2019-02-18
  selected window = 2024-06-04~D+180
  contamination = false

008970:
  name = 동양철관 in 2024, KBI동양철관 after 2025-09-12
  corporate_action_candidate_dates = 1997-01-03, 1997-09-02, 1999-03-24, 1999-03-30, 2001-08-27, 2001-10-04, 2018-12-27, 2025-09-12, 2025-12-26
  selected window = 2024-06-04~D+180
  contamination = false by profile
  share_count_change_inside_window = true → coding-agent validation required

071090:
  corporate_action_candidate_dates = 2012-11-27, 2021-04-05
  selected window = 2024-06-04~D+180
  contamination = false
```

Data-quality caveat:

```text
All selected C31 rows are source_proxy_only / evidence_url_pending.
008970 also requires share-count validation before runtime promotion.
This MD is useful for stock-web path calibration and C31 rule-shape discovery,
but coding-agent promotion requires non-proxy policy event, direct beneficiary mapping, actual project order, delivery schedule, revenue and margin evidence.
```

---

## Deferred Coding Agent Handoff Prompt

Do not execute this now.

```text
You are the coding agent for Songdaiki/stock_agent.

Read this standalone v12 residual research MD and ingest machine-readable rows only after validation.

Do not patch production scoring blindly.
This R11/C31 artifact is marked do_not_propose_new_weight_delta=true because all rows need source repair and 008970 needs share-count validation.

Candidate axis:
east_sea_gas_field_pipe_valve_infra_policy_event_bridge_vs_resource_theme_fade

Required checks before implementation:
1. Validate all trigger rows against stock-web tradable_raw OHLC shards.
2. Confirm no hard duplicate key:
   canonical_archetype_id + symbol + trigger_type + entry_date.
3. Verify non-proxy source URLs for 039610, 008970 and 071090.
4. Validate 008970 share-count changes inside the selected window.
5. Keep generic C31 policy-event weight unchanged until source repair is complete.
6. Consider Stage2 only when:
   - policy/resource-development event is explicit,
   - direct beneficiary mapping is visible,
   - actual order, project schedule, delivery or customer bridge exists,
   - revenue and margin bridge is credible,
   - MAE remains controlled or the signal is lifecycle-managed.
7. Consider local 4B-watch when:
   - the trigger is policy/resource theme beta only,
   - order/revenue/margin bridge is absent or stale,
   - MAE_90D <= -20% or MAE_180D <= -25%,
   - post-peak drawdown <= -35%.
8. Do not convert local 4B-watch into full 4B/4C without non-price project cancellation, order failure, policy reversal, revenue/margin break, financing or liquidity evidence.
9. Emit before/after diagnostics and reject if verified direct-beneficiary policy lifecycle positives are overblocked.
```

---

## Final round state

```text
completed_round = R11
completed_loop = 76
next_round = R12
next_loop = 76
round_schedule_status = valid
round_sector_consistency = pass
```

