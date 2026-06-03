# E2R Stock-Web v12 Residual Research — R11 Loop 74 / L10 / C31

## Metadata

```json
{
  "research_session": "post_calibrated_sector_archetype_residual_research",
  "mode": "historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12",
  "scheduled_round": "R11",
  "scheduled_loop": 74,
  "round_schedule_status": "valid",
  "round_sector_consistency": "pass",
  "completed_round": "R11",
  "completed_loop": 74,
  "computed_next_round": "R12",
  "computed_next_loop": 74,
  "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC",
  "canonical_archetype_id": "C31_POLICY_SUBSIDY_LEGISLATION_EVENT",
  "fine_archetype_id": "EAST_SEA_DEEPSEA_GAS_POLICY_RESOURCE_INFRA_CONTRACT_BRIDGE_VS_PROXY_HEADLINE_CHASE",
  "loop_objective": [
    "coverage_gap_fill",
    "counterexample_mining",
    "policy_contract_bridge_guardrail",
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
production_scoring_changed = false
shadow_weight_only = true
handoff_prompt_executed_now = false
```

## Round / scope resolution

Previous completed state in this interactive run: R10 / loop 74.

Therefore:

```text
scheduled_round = R11
scheduled_loop = 74
allowed_large_sector = L10_POLICY_EVENT_CROSS_REDTEAM_MISC or L1 policy-defense linkage
selected_large_sector = L10_POLICY_EVENT_CROSS_REDTEAM_MISC
selected_canonical_archetype_id = C31_POLICY_SUBSIDY_LEGISLATION_EVENT
computed_next_round = R12
computed_next_loop = 74
```

R11 was routed to C31 because this is a policy-event / project-scope / contract-bridge guardrail, not a normal resource or industrial spread run.

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
039610 / 화성밸브 / gas valve policy lifecycle candidate
008970 / KBI동양철관 / steel-pipeline policy proxy fade
004090 / 한국석유 / oil-product policy theme beta fade
```

Data-quality note:

```text
All three rows are stock-web calibration usable by profile-level corporate-action candidates.
All three rows are source_proxy_only=true / evidence_url_pending=true.
008970 shows share-count changes inside the 2024 window and requires coding-agent validation before runtime promotion.
```

## Research thesis

C31 is not “policy headline went up.”

The mechanism must pass through:

```text
policy event
→ named project scope
→ concession / procurement / EPC / supply bridge
→ direct revenue or margin bridge
→ durable rerating
```

A policy headline is a survey flag in a field.  
A contract bridge is the road actually being built.

---

## Case 1 — Policy lifecycle candidate: 039610 / 화성밸브

### Evidence status

```text
source_proxy_only = true
evidence_url_pending = true
source_repair_required = true
```

The source-repair task is valve/infrastructure order, EPC, utility/offshore project scope and revenue bridge evidence.

```text
evidence_family = EAST_SEA_DEEPSEA_GAS_POLICY_VALVE_INFRA_ORDER_CONTRACT_BRIDGE_CANDIDATE
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
2024-07-03,7020,7170,6800,7120
2024-09-25,13880,14300,11920,12000
2024-12-09,8050,8200,6980,7050
```

### Backtest

```text
MFE_30D  = +28.39%
MAE_30D  = -21.21%
MFE_90D  = +65.70%
MAE_90D  = -21.21%
MFE_180D = +65.70%
MAE_180D = -21.21%
peak_180 = 14,300 on 2024-09-25
trough_180 = 6,800 on 2024-07-03
peak_to_later_drawdown = -51.19%
```

### Interpretation

This is not a clean immediate Green.  
The early MAE was already large. But the later secondary high says a policy lifecycle candidate should not be permanently overblocked if actual order or infrastructure bridge becomes visible.

Correct treatment:

```text
source repair first
then possible Stage2 lifecycle
later local 4B if contract bridge fades
```

---

## Case 2 — Counterexample / local 4B: 008970 / KBI동양철관

### Evidence status

```text
source_proxy_only = true
evidence_url_pending = true
share_count_change_inside_window = true
source_repair_required = true
```

The source-repair task is steel-pipeline procurement, EPC participation, order/backlog and direct revenue bridge evidence.

```text
evidence_family = EAST_SEA_DEEPSEA_GAS_POLICY_STEEL_PIPELINE_PROXY_WITH_WEAK_DIRECT_CONTRACT_BRIDGE
case_role = counterexample_policy_proxy_local4b
trigger_date = 2024-06-03
entry_date = 2024-06-04
entry_price = 1,175
```

### Stock-Web price path

Observed rows from `atlas/ohlcv_tradable_by_symbol_year/008/008970/2024.csv`:

```text
2024-06-03,697,904,697,904
2024-06-04,1175,1175,1175,1175
2024-06-07,1610,1678,1285,1411
2024-08-05,985,987,826,890
2024-10-21,821,870,805,805
2024-12-10,582,637,580,630
```

### Backtest

```text
MFE_30D  = +42.81%
MAE_30D  = -21.62%
MFE_90D  = +42.81%
MAE_90D  = -31.49%
MFE_180D = +42.81%
MAE_180D = -50.64%
peak_180 = 1,678 on 2024-06-07
trough_180 = 580 on 2024-12-10
peak_to_later_drawdown = -65.44%
```

### Interpretation

This is the classic C31 policy-proxy trap.  
The first move was strong, but the direct contract bridge did not hold.

The right label is:

```text
false Stage2 / local 4B-watch
```

not durable Green.

---

## Case 3 — Counterexample / local 4B: 004090 / 한국석유

### Evidence status

```text
source_proxy_only = true
evidence_url_pending = true
source_repair_required = true
```

The source-repair task is direct concession, product supply, infrastructure procurement or earnings bridge evidence.

```text
evidence_family = EAST_SEA_DEEPSEA_GAS_POLICY_OIL_PRODUCT_THEME_BETA_WITH_WEAK_REVENUE_BRIDGE
case_role = counterexample_policy_theme_beta
trigger_date = 2024-06-03
entry_date = 2024-06-04
entry_price = 21,650
```

### Stock-Web price path

Observed rows from `atlas/ohlcv_tradable_by_symbol_year/004/004090/2024.csv`:

```text
2024-06-03,13890,17950,13850,17950
2024-06-04,21650,23300,21500,23300
2024-06-05,23650,28100,21600,23300
2024-07-15,17570,17650,16770,16810
2024-08-02,20850,23850,20600,23000
2024-12-09,12500,13000,12240,12260
```

### Backtest

```text
MFE_30D  = +29.79%
MAE_30D  = -22.54%
MFE_90D  = +29.79%
MAE_90D  = -28.22%
MFE_180D = +29.79%
MAE_180D = -43.46%
peak_180 = 28,100 on 2024-06-05
trough_180 = 12,240 on 2024-12-09
peak_to_later_drawdown = -56.44%
```

### Interpretation

This is an oil/gas policy-theme beta fade.  
The company can move with the event, but C31 should not call it Stage2 unless the policy connects to direct earnings, supply, infrastructure or procurement.

---

## Cross-case residual finding

### What this strengthens

```text
price_only_blowoff_blocks_positive_stage = strengthen
full_4b_requires_non_price_evidence = keep
local_4b_watch_guard = strengthen
stage2_required_bridge = strengthen
```

### What this does not justify

```text
do_not_raise_generic_C31_resource_policy_weight = true
do_not_treat_policy_proxy_gap_as_Green_without_project_scope = true
do_not_convert_policy_proxy_drawdown_to_hard_4C_without_non_price_break = true
do_not_overblock_lifecycle_winner_after_contract_bridge_source_repair = true
```

### Candidate canonical compression

Fine labels can compress into:

```text
EAST_SEA_DEEPSEA_GAS_POLICY_RESOURCE_INFRA_CONTRACT_BRIDGE_VS_PROXY_HEADLINE_CHASE
```

This fine archetype covers:

```text
1. valve/infrastructure policy lifecycle candidate → possible only after source repair
2. steel-pipeline policy proxy without order bridge → false Stage2 / local 4B
3. oil-product policy theme beta without direct revenue bridge → false Stage2 / local 4B
```

---

## Machine-readable rows

### price source validation row

```jsonl
{"row_type": "price_source_validation", "source": "Songdaiki/stock-web", "source_url": "https://github.com/Songdaiki/stock-web", "manifest_path": "atlas/manifest.json", "schema_path": "atlas/schema.json", "universe_path": "atlas/universe/all_symbols.csv", "manifest_max_date": "2026-02-20", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "raw_shard_root": "atlas/ohlcv_raw_by_symbol_year", "validation_status": "usable_for_historical_calibration"}
```

### case rows

```jsonl
{"row_type": "case", "case_id": "R11L74-C31-039610-HWASUNG-VALVE-GAS-POLICY-CONTRACT-BRIDGE", "symbol": "039610", "company_name": "화성밸브", "round": "R11", "loop": "74", "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "C31_POLICY_SUBSIDY_LEGISLATION_EVENT", "fine_archetype_id": "EAST_SEA_DEEPSEA_GAS_POLICY_RESOURCE_INFRA_CONTRACT_BRIDGE_VS_PROXY_HEADLINE_CHASE", "case_type": "policy_subsidy_legislation_event_resource_infra_contract_bridge", "positive_or_counterexample": "policy_lifecycle_positive", "best_trigger": "Stage2-PolicyLifecycle / GasValveContractBridgeCandidate", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 0.5, "score_price_alignment": "C31 can allow a policy-event lifecycle candidate when a valve or pipeline-infra name later connects to named procurement, order, EPC, utility or offshore infrastructure bridge. Hwasung Valve had a large MFE and later secondary peak, but still needs source repair and lifecycle local 4B after the peak.", "current_profile_verdict": "source_repair_required_before_runtime_weight", "price_source": "Songdaiki/stock-web", "notes": "Stock-web path usable; non-proxy policy, project scope, procurement, EPC, concession, order and revenue bridge evidence required before runtime promotion."}
{"row_type": "case", "case_id": "R11L74-C31-008970-DONGYANG-PIPELINE-POLICY-PROXY-FADE", "symbol": "008970", "company_name": "KBI동양철관", "round": "R11", "loop": "74", "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "C31_POLICY_SUBSIDY_LEGISLATION_EVENT", "fine_archetype_id": "EAST_SEA_DEEPSEA_GAS_POLICY_RESOURCE_INFRA_CONTRACT_BRIDGE_VS_PROXY_HEADLINE_CHASE", "case_type": "policy_subsidy_legislation_event_resource_infra_contract_bridge", "positive_or_counterexample": "counterexample", "best_trigger": "Stage2-FalsePositive / PipelinePolicyProxyFade", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 0.5, "score_price_alignment": "C31 should not convert a pipeline/steel-pipe policy proxy into durable Stage2 unless project ownership, procurement scope, actual order, EPC participation or revenue timing is visible. KBI Dongyang Steel Pipe had a large initial MFE but then deep MAE and post-peak drawdown.", "current_profile_verdict": "source_repair_required_before_runtime_weight", "price_source": "Songdaiki/stock-web", "notes": "Stock-web path usable; non-proxy policy, project scope, procurement, EPC, concession, order and revenue bridge evidence required before runtime promotion."}
{"row_type": "case", "case_id": "R11L74-C31-004090-KOREA-PETROLEUM-POLICY-THEME-BETA-FADE", "symbol": "004090", "company_name": "한국석유", "round": "R11", "loop": "74", "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "C31_POLICY_SUBSIDY_LEGISLATION_EVENT", "fine_archetype_id": "EAST_SEA_DEEPSEA_GAS_POLICY_RESOURCE_INFRA_CONTRACT_BRIDGE_VS_PROXY_HEADLINE_CHASE", "case_type": "policy_subsidy_legislation_event_resource_infra_contract_bridge", "positive_or_counterexample": "counterexample", "best_trigger": "Stage2-FalsePositive / OilGasPolicyThemeBetaFade", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 0.5, "score_price_alignment": "C31 should not treat oil/gas policy attention as a durable Stage2 signal for an oil-product proxy without direct concession, supply, infrastructure, procurement or earnings bridge. Korea Petroleum produced strong event MFE but later opened high MAE and a large post-peak drawdown.", "current_profile_verdict": "source_repair_required_before_runtime_weight", "price_source": "Songdaiki/stock-web", "notes": "Stock-web path usable; non-proxy policy, project scope, procurement, EPC, concession, order and revenue bridge evidence required before runtime promotion."}
```

### trigger rows

```jsonl
{"row_type": "trigger", "trigger_id": "TRG_R11L74-C31-039610-HWASUNG-VALVE-GAS-POLICY-CONTRACT-BRIDGE", "case_id": "R11L74-C31-039610-HWASUNG-VALVE-GAS-POLICY-CONTRACT-BRIDGE", "symbol": "039610", "company_name": "화성밸브", "round": "R11", "loop": "74", "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "C31_POLICY_SUBSIDY_LEGISLATION_EVENT", "fine_archetype_id": "EAST_SEA_DEEPSEA_GAS_POLICY_RESOURCE_INFRA_CONTRACT_BRIDGE_VS_PROXY_HEADLINE_CHASE", "loop_objective": "counterexample_mining|policy_contract_bridge_guardrail|4B_non_price_requirement_stress_test", "trigger_type": "Stage2-PolicyLifecycle / GasValveContractBridgeCandidate", "trigger_date": "2024-06-03", "entry_date": "2024-06-04", "entry_price": 8630.0, "evidence_available_at_that_date": "EAST_SEA_DEEPSEA_GAS_POLICY_VALVE_INFRA_ORDER_CONTRACT_BRIDGE_CANDIDATE", "evidence_source": "source_proxy_manual_verification_required:EAST_SEA_DEEPSEA_GAS_POLICY_HWASUNG_VALVE_ORDER_EPC_INFRA_CONTRACT_BRIDGE", "stage2_evidence_fields": ["policy_event", "resource_or_infra_proxy", "contract_bridge_candidate"], "stage3_evidence_fields": ["relative_strength", "procurement_or_revenue_bridge_candidate"], "stage4b_evidence_fields": ["bridge_absent_or_stale", "MAE_widening", "post_peak_drawdown"], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/039/039610/2024.csv", "profile_path": "atlas/symbol_profiles/039/039610.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": 28.39, "MFE_90D_pct": 65.7, "MFE_180D_pct": 65.7, "MAE_30D_pct": -21.21, "MAE_90D_pct": -21.21, "MAE_180D_pct": -21.21, "peak_date": "2024-09-25", "peak_price": 14300.0, "drawdown_after_peak_pct": -51.19, "green_lateness_ratio": null, "four_b_local_peak_proximity": "local_4b_watch_after_policy_proxy_peak_if_contract_bridge_fades", "four_b_full_window_peak_proximity": "full_4b_requires_non_price_contract_failure_project_cancellation_or_direct_revenue_break", "trigger_outcome_label": "policy_lifecycle_positive_with_later_4b_watch", "current_profile_verdict": "C31 can allow a policy-event lifecycle candidate when a valve or pipeline-infra name later connects to named procurement, order, EPC, utility or offshore infrastructure bridge. Hwasung Valve had a large MFE and later secondary peak, but still needs source repair and lifecycle local 4B after the peak.", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window_by_profile", "share_count_change_inside_window": false, "same_entry_group_id": "C31_EAST_SEA_DEEPSEA_GAS_POLICY_20240604_GROUP", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 0.5, "do_not_count_as_new_case": false, "source_proxy_only": true, "evidence_url_pending": true}
{"row_type": "trigger", "trigger_id": "TRG_R11L74-C31-008970-DONGYANG-PIPELINE-POLICY-PROXY-FADE", "case_id": "R11L74-C31-008970-DONGYANG-PIPELINE-POLICY-PROXY-FADE", "symbol": "008970", "company_name": "KBI동양철관", "round": "R11", "loop": "74", "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "C31_POLICY_SUBSIDY_LEGISLATION_EVENT", "fine_archetype_id": "EAST_SEA_DEEPSEA_GAS_POLICY_RESOURCE_INFRA_CONTRACT_BRIDGE_VS_PROXY_HEADLINE_CHASE", "loop_objective": "counterexample_mining|policy_contract_bridge_guardrail|4B_non_price_requirement_stress_test", "trigger_type": "Stage2-FalsePositive / PipelinePolicyProxyFade", "trigger_date": "2024-06-03", "entry_date": "2024-06-04", "entry_price": 1175.0, "evidence_available_at_that_date": "EAST_SEA_DEEPSEA_GAS_POLICY_STEEL_PIPELINE_PROXY_WITH_WEAK_DIRECT_CONTRACT_BRIDGE", "evidence_source": "source_proxy_manual_verification_required:EAST_SEA_DEEPSEA_GAS_POLICY_DONGYANG_PIPELINE_STEEL_PIPE_ORDER_EPC_BRIDGE", "stage2_evidence_fields": ["policy_event", "resource_or_infra_proxy", "contract_bridge_candidate"], "stage3_evidence_fields": ["relative_strength", "procurement_or_revenue_bridge_candidate"], "stage4b_evidence_fields": ["bridge_absent_or_stale", "MAE_widening", "post_peak_drawdown"], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/008/008970/2024.csv", "profile_path": "atlas/symbol_profiles/008/008970.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": 42.81, "MFE_90D_pct": 42.81, "MFE_180D_pct": 42.81, "MAE_30D_pct": -21.62, "MAE_90D_pct": -31.49, "MAE_180D_pct": -50.64, "peak_date": "2024-06-07", "peak_price": 1678.0, "drawdown_after_peak_pct": -65.44, "green_lateness_ratio": null, "four_b_local_peak_proximity": "local_4b_watch_after_policy_proxy_peak_if_contract_bridge_fades", "four_b_full_window_peak_proximity": "full_4b_requires_non_price_contract_failure_project_cancellation_or_direct_revenue_break", "trigger_outcome_label": "counterexample_policy_proxy_local4b", "current_profile_verdict": "C31 should not convert a pipeline/steel-pipe policy proxy into durable Stage2 unless project ownership, procurement scope, actual order, EPC participation or revenue timing is visible. KBI Dongyang Steel Pipe had a large initial MFE but then deep MAE and post-peak drawdown.", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window_by_profile", "share_count_change_inside_window": true, "same_entry_group_id": "C31_EAST_SEA_DEEPSEA_GAS_POLICY_20240604_GROUP", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 0.5, "do_not_count_as_new_case": false, "source_proxy_only": true, "evidence_url_pending": true}
{"row_type": "trigger", "trigger_id": "TRG_R11L74-C31-004090-KOREA-PETROLEUM-POLICY-THEME-BETA-FADE", "case_id": "R11L74-C31-004090-KOREA-PETROLEUM-POLICY-THEME-BETA-FADE", "symbol": "004090", "company_name": "한국석유", "round": "R11", "loop": "74", "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "C31_POLICY_SUBSIDY_LEGISLATION_EVENT", "fine_archetype_id": "EAST_SEA_DEEPSEA_GAS_POLICY_RESOURCE_INFRA_CONTRACT_BRIDGE_VS_PROXY_HEADLINE_CHASE", "loop_objective": "counterexample_mining|policy_contract_bridge_guardrail|4B_non_price_requirement_stress_test", "trigger_type": "Stage2-FalsePositive / OilGasPolicyThemeBetaFade", "trigger_date": "2024-06-03", "entry_date": "2024-06-04", "entry_price": 21650.0, "evidence_available_at_that_date": "EAST_SEA_DEEPSEA_GAS_POLICY_OIL_PRODUCT_THEME_BETA_WITH_WEAK_REVENUE_BRIDGE", "evidence_source": "source_proxy_manual_verification_required:EAST_SEA_DEEPSEA_GAS_POLICY_KOREA_PETROLEUM_DIRECT_REVENUE_SUPPLY_BRIDGE", "stage2_evidence_fields": ["policy_event", "resource_or_infra_proxy", "contract_bridge_candidate"], "stage3_evidence_fields": ["relative_strength", "procurement_or_revenue_bridge_candidate"], "stage4b_evidence_fields": ["bridge_absent_or_stale", "MAE_widening", "post_peak_drawdown"], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/004/004090/2024.csv", "profile_path": "atlas/symbol_profiles/004/004090.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": 29.79, "MFE_90D_pct": 29.79, "MFE_180D_pct": 29.79, "MAE_30D_pct": -22.54, "MAE_90D_pct": -28.22, "MAE_180D_pct": -43.46, "peak_date": "2024-06-05", "peak_price": 28100.0, "drawdown_after_peak_pct": -56.44, "green_lateness_ratio": null, "four_b_local_peak_proximity": "local_4b_watch_after_policy_proxy_peak_if_contract_bridge_fades", "four_b_full_window_peak_proximity": "full_4b_requires_non_price_contract_failure_project_cancellation_or_direct_revenue_break", "trigger_outcome_label": "counterexample_policy_theme_beta", "current_profile_verdict": "C31 should not treat oil/gas policy attention as a durable Stage2 signal for an oil-product proxy without direct concession, supply, infrastructure, procurement or earnings bridge. Korea Petroleum produced strong event MFE but later opened high MAE and a large post-peak drawdown.", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window_by_profile", "share_count_change_inside_window": false, "same_entry_group_id": "C31_EAST_SEA_DEEPSEA_GAS_POLICY_20240604_GROUP", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 0.5, "do_not_count_as_new_case": false, "source_proxy_only": true, "evidence_url_pending": true}
```

### score simulation rows

```jsonl
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R11L74-C31-039610-HWASUNG-VALVE-GAS-POLICY-CONTRACT-BRIDGE", "trigger_id": "TRG_R11L74-C31-039610-HWASUNG-VALVE-GAS-POLICY-CONTRACT-BRIDGE", "symbol": "039610", "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "C31_POLICY_SUBSIDY_LEGISLATION_EVENT", "raw_component_scores_before": {"policy_or_regulatory_score": 16, "project_scope_score": 4, "contract_or_procurement_score": 3, "direct_revenue_bridge_score": 2, "relative_strength_score": 12, "execution_risk_score": 16, "theme_proxy_risk_score": 11, "dilution_or_sharecount_risk_score": 0, "source_confidence_score": 2}, "weighted_score_before": 68, "stage_label_before": "Stage2-Watch / policy proxy beta", "raw_component_scores_after": {"policy_or_regulatory_score": 9, "project_scope_score": 2, "contract_or_procurement_score": 1, "direct_revenue_bridge_score": 1, "relative_strength_score": 9, "execution_risk_score": 15, "theme_proxy_risk_score": 14, "dilution_or_sharecount_risk_score": 0, "source_confidence_score": 2}, "weighted_score_after": 61, "stage_label_after": "Policy lifecycle candidate after source repair + local 4B", "changed_components": ["policy_or_regulatory_score", "contract_or_procurement_score", "direct_revenue_bridge_score", "execution_risk_score", "theme_proxy_risk_score"], "component_delta_explanation": "Cap policy-event proxy scores unless project scope, procurement/EPC, concession, supply, order or revenue bridge is verified.", "MFE_90D_pct": 65.7, "MAE_90D_pct": -21.21, "score_return_alignment_label": "policy_lifecycle_with_later_4b", "current_profile_verdict": "C31 can allow a policy-event lifecycle candidate when a valve or pipeline-infra name later connects to named procurement, order, EPC, utility or offshore infrastructure bridge. Hwasung Valve had a large MFE and later secondary peak, but still needs source repair and lifecycle local 4B after the peak."}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R11L74-C31-008970-DONGYANG-PIPELINE-POLICY-PROXY-FADE", "trigger_id": "TRG_R11L74-C31-008970-DONGYANG-PIPELINE-POLICY-PROXY-FADE", "symbol": "008970", "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "C31_POLICY_SUBSIDY_LEGISLATION_EVENT", "raw_component_scores_before": {"policy_or_regulatory_score": 16, "project_scope_score": 4, "contract_or_procurement_score": 3, "direct_revenue_bridge_score": 2, "relative_strength_score": 12, "execution_risk_score": 16, "theme_proxy_risk_score": 16, "dilution_or_sharecount_risk_score": 6, "source_confidence_score": 2}, "weighted_score_before": 58, "stage_label_before": "Stage2-Watch / policy proxy beta", "raw_component_scores_after": {"policy_or_regulatory_score": 9, "project_scope_score": 2, "contract_or_procurement_score": 1, "direct_revenue_bridge_score": 1, "relative_strength_score": 5, "execution_risk_score": 19, "theme_proxy_risk_score": 19, "dilution_or_sharecount_risk_score": 9, "source_confidence_score": 2}, "weighted_score_after": 41, "stage_label_after": "Stage4B-local-watch / no durable Green", "changed_components": ["policy_or_regulatory_score", "contract_or_procurement_score", "direct_revenue_bridge_score", "execution_risk_score", "theme_proxy_risk_score"], "component_delta_explanation": "Cap policy-event proxy scores unless project scope, procurement/EPC, concession, supply, order or revenue bridge is verified.", "MFE_90D_pct": 42.81, "MAE_90D_pct": -31.49, "score_return_alignment_label": "policy_proxy_false_positive_bridge_gap", "current_profile_verdict": "C31 should not convert a pipeline/steel-pipe policy proxy into durable Stage2 unless project ownership, procurement scope, actual order, EPC participation or revenue timing is visible. KBI Dongyang Steel Pipe had a large initial MFE but then deep MAE and post-peak drawdown."}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R11L74-C31-004090-KOREA-PETROLEUM-POLICY-THEME-BETA-FADE", "trigger_id": "TRG_R11L74-C31-004090-KOREA-PETROLEUM-POLICY-THEME-BETA-FADE", "symbol": "004090", "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "C31_POLICY_SUBSIDY_LEGISLATION_EVENT", "raw_component_scores_before": {"policy_or_regulatory_score": 16, "project_scope_score": 4, "contract_or_procurement_score": 3, "direct_revenue_bridge_score": 2, "relative_strength_score": 8, "execution_risk_score": 16, "theme_proxy_risk_score": 16, "dilution_or_sharecount_risk_score": 0, "source_confidence_score": 2}, "weighted_score_before": 58, "stage_label_before": "Stage2-Watch / policy proxy beta", "raw_component_scores_after": {"policy_or_regulatory_score": 9, "project_scope_score": 2, "contract_or_procurement_score": 1, "direct_revenue_bridge_score": 1, "relative_strength_score": 5, "execution_risk_score": 19, "theme_proxy_risk_score": 19, "dilution_or_sharecount_risk_score": 0, "source_confidence_score": 2}, "weighted_score_after": 41, "stage_label_after": "Stage4B-local-watch / no durable Green", "changed_components": ["policy_or_regulatory_score", "contract_or_procurement_score", "direct_revenue_bridge_score", "execution_risk_score", "theme_proxy_risk_score"], "component_delta_explanation": "Cap policy-event proxy scores unless project scope, procurement/EPC, concession, supply, order or revenue bridge is verified.", "MFE_90D_pct": 29.79, "MAE_90D_pct": -28.22, "score_return_alignment_label": "policy_proxy_false_positive_bridge_gap", "current_profile_verdict": "C31 should not treat oil/gas policy attention as a durable Stage2 signal for an oil-product proxy without direct concession, supply, infrastructure, procurement or earnings bridge. Korea Petroleum produced strong event MFE but later opened high MAE and a large post-peak drawdown."}
```

### aggregate row

```jsonl
{"row_type": "aggregate", "round": "R11", "loop": 74, "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "C31_POLICY_SUBSIDY_LEGISLATION_EVENT", "fine_archetype_id": "EAST_SEA_DEEPSEA_GAS_POLICY_RESOURCE_INFRA_CONTRACT_BRIDGE_VS_PROXY_HEADLINE_CHASE", "calibration_usable_case_count": 3, "calibration_usable_trigger_count": 3, "new_independent_case_count": 3, "reused_case_count": 0, "same_archetype_new_symbol_count": 3, "same_archetype_new_trigger_family_count": 1, "positive_case_count": 1, "counterexample_count": 2, "four_b_case_count": 3, "four_c_case_count": 0, "source_proxy_only_count": 3, "evidence_url_pending_count": 3, "share_count_change_inside_window_count": 1, "current_profile_error_count": 2, "diversity_score_summary": "+3 underused C31 resource-policy proxy symbols, +1 East Sea deepsea gas trigger family, +1 valve lifecycle candidate, +2 policy-proxy false positives/local-4B, no hard duplicate", "residual_contribution_label": "policy_contract_bridge_guardrail_with_source_repair_needed"}
```

### shadow weight row

```jsonl
{"row_type": "shadow_weight", "round": "R11", "loop": 74, "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "C31_POLICY_SUBSIDY_LEGISLATION_EVENT", "axis": "east_sea_deepsea_gas_policy_resource_infra_contract_bridge_vs_proxy_headline_chase", "decision": "hold_for_source_repair_and_more_evidence", "proposed_runtime_effect": "C31 should split resource-policy proxy spikes from verified project/contract bridge. Stage2 requires named concession, project scope, procurement/EPC, order, supply, infrastructure or direct revenue evidence. Pipeline, valve and oil-product proxies with high MAE or post-peak drawdown should route to local 4B-watch unless bridge evidence refreshes.", "do_not_propose_new_weight_delta": true, "needs_more_evidence": true, "source_repair_required": ["039610", "008970", "004090"], "share_count_validation_required": ["008970"]}
```

### residual contribution row

```jsonl
{"row_type": "residual_contribution", "round": "R11", "loop": 74, "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "C31_POLICY_SUBSIDY_LEGISLATION_EVENT", "existing_axis_strengthened": ["price_only_blowoff_blocks_positive_stage", "full_4b_requires_non_price_evidence", "local_4b_watch_guard", "stage2_required_bridge"], "new_axis_proposed": null, "sector_specific_rule_candidate": true, "canonical_archetype_rule_candidate": true, "narrative_summary": "C31 resource-policy events need project and contract bridge proof. Hwasung Valve is a policy lifecycle candidate after source repair; KBI Dongyang Steel Pipe and Korea Petroleum are policy-proxy false positives/local 4B when contract or direct revenue bridge is absent."}
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
  corporate_action_candidate_dates = 1997-01-03, 1997-09-02, 1999-03-24, 1999-03-30, 2001-08-27, 2001-10-04, 2018-12-27, 2025-09-12, 2025-12-26
  selected window = 2024-06-04~D+180
  contamination = false by profile
  share_count_change_inside_window = true → coding-agent validation required

004090:
  corporate_action_candidate_dates = 1997-08-07, 2021-04-15, 2021-05-07
  selected window = 2024-06-04~D+180
  contamination = false
```

Data-quality caveat:

```text
All selected C31 rows are source_proxy_only / evidence_url_pending.
008970 also requires share-count validation before runtime promotion.
This MD is useful for stock-web path calibration and C31 rule-shape discovery,
but coding-agent promotion requires non-proxy policy, project scope, procurement/EPC, concession, order, supply and direct revenue evidence.
```

---

## Deferred Coding Agent Handoff Prompt

Do not execute this now.

```text
You are the coding agent for Songdaiki/stock_agent.

Read this standalone v12 residual research MD and ingest machine-readable rows only after validation.

Do not patch production scoring blindly.
This R11/C31 artifact is marked do_not_propose_new_weight_delta=true because all rows need source repair.

Candidate axis:
east_sea_deepsea_gas_policy_resource_infra_contract_bridge_vs_proxy_headline_chase

Required checks before implementation:
1. Validate all trigger rows against stock-web tradable_raw OHLC shards.
2. Confirm no hard duplicate key:
   canonical_archetype_id + symbol + trigger_type + entry_date.
3. Verify non-proxy source URLs for 039610, 008970 and 004090.
4. Validate 008970 share-count changes inside the selected window.
5. Keep generic C31 policy-event weight unchanged until source repair is complete.
6. Consider Stage2 only when:
   - policy event is explicit,
   - project scope or named concession is visible,
   - procurement/EPC/order/supply/direct revenue bridge exists,
   - MAE remains controlled or the signal is deliberately treated as lifecycle rather than immediate Green.
7. Consider local 4B-watch when:
   - the trigger is policy proxy headline only,
   - contract or direct revenue bridge is absent/stale,
   - MAE_90D <= -20% or MAE_180D <= -25%,
   - post-peak drawdown <= -35%.
8. Do not convert local 4B-watch into hard 4C without non-price project cancellation, contract failure, concession failure, financing/liquidity break, or insolvency evidence.
9. Emit before/after diagnostics and reject if verified project-contract lifecycle positives are overblocked.
```

---

## Final round state

```text
completed_round = R11
completed_loop = 74
next_round = R12
next_loop = 74
round_schedule_status = valid
round_sector_consistency = pass
```

