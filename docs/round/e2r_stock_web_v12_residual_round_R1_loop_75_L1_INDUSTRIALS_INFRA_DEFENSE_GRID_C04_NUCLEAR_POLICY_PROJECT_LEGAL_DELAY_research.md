# E2R Stock-Web v12 Residual Research — R1 Loop 75 / L1 / C04

## Metadata

```json
{
  "research_session": "post_calibrated_sector_archetype_residual_research",
  "mode": "historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12",
  "scheduled_round": "R1",
  "scheduled_loop": 75,
  "round_schedule_status": "valid",
  "round_sector_consistency": "pass",
  "completed_round": "R1",
  "completed_loop": 75,
  "computed_next_round": "R2",
  "computed_next_loop": 75,
  "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID",
  "canonical_archetype_id": "C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY",
  "fine_archetype_id": "NUCLEAR_SERVICE_CONTROL_INSTRUMENTATION_PROJECT_BRIDGE_VS_POLICY_PROXY_FADE",
  "loop_objective": [
    "coverage_gap_fill",
    "counterexample_mining",
    "4B_non_price_requirement_stress_test",
    "policy_project_contract_bridge_guardrail",
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

Previous completed state in this interactive run: R13 / loop 74.

Therefore:

```text
scheduled_round = R1
scheduled_loop = 75
allowed_large_sector = L1_INDUSTRIALS_INFRA_DEFENSE_GRID
selected_large_sector = L1_INDUSTRIALS_INFRA_DEFENSE_GRID
selected_canonical_archetype_id = C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY
computed_next_round = R2
computed_next_loop = 75
```

R1 was routed to C04 because loop 74 used C03 and C04 remains relatively thin.  
This file avoids the top-covered Czech-project names and tests service, control-system and instrumentation supplier paths.

## No-Repeat / novelty check

No hard duplicate is intentionally reused.

Hard duplicate key checked conceptually:

```text
canonical_archetype_id + symbol + trigger_type + entry_date
```

No-Repeat shows C04 is concentrated in:

```text
034020, 051600, 052690, 000720, 083650
```

This run uses three different symbols:

```text
130660 / 한전산업 / nuclear service/O&M project bridge
032820 / 우리기술 / nuclear control-system I&C project bridge
105840 / 우진 / nuclear instrumentation policy-proxy fade
```

Data-quality note:

```text
All three rows are stock-web calibration usable by profile-level corporate-action candidates.
All three rows are source_proxy_only=true / evidence_url_pending=true.
032820 shows share-count changes inside the selected window and requires coding-agent validation before runtime promotion.
```

## Research thesis

C04 is not “nuclear policy headline went up.”

The mechanism must pass through:

```text
policy / project event
→ named project scope or regulatory milestone
→ O&M / control system / instrumentation order
→ customer, delivery or margin bridge
→ durable rerating
```

A nuclear headline is the reactor dome on the skyline.  
The order bridge is the control room wiring.

---

## Case 1 — Positive with lifecycle 4B: 130660 / 한전산업

### Evidence status

```text
source_proxy_only = true
evidence_url_pending = true
source_repair_required = true
```

The source-repair task is nuclear service/O&M, project scope, customer/utility contract, delivery and margin bridge evidence.

```text
evidence_family = NUCLEAR_SERVICE_OPERATION_MAINTENANCE_POLICY_PROJECT_SCOPE_MARGIN_BRIDGE
case_role = positive_with_later_4b_watch
trigger_date = 2024-05-24
entry_date = 2024-05-27
entry_price = 8,800
```

### Stock-Web price path

Observed rows from `atlas/ohlcv_tradable_by_symbol_year/130/130660/2024.csv`:

```text
2024-05-27,8800,10930,8640,10330
2024-06-11,11950,14570,11580,12950
2024-07-18,19500,19500,17200,17740
2024-08-05,13910,14240,11920,12750
2024-12-09,9250,9380,8880,8890
```

### Backtest

```text
MFE_30D  = +65.57%
MAE_30D  = -1.82%
MFE_90D  = +121.59%
MAE_90D  = -1.82%
MFE_180D = +121.59%
MAE_180D = -1.82%
peak_180 = 19,500 on 2024-07-18
trough_180 = 8,640 on 2024-05-27
peak_to_later_drawdown = -54.46%
```

### Interpretation

This is a strong C04 positive-shaped path.  
The price path supports nuclear service/project bridge potential, but it should not become generic nuclear beta. Non-price project scope and service/margin evidence are required.

The post-peak drawdown says C04 needs lifecycle local 4B if evidence stops refreshing.

---

## Case 2 — Positive with share-count validation: 032820 / 우리기술

### Evidence status

```text
source_proxy_only = true
evidence_url_pending = true
share_count_change_inside_window = true
source_repair_required = true
```

The source-repair task is nuclear control/I&C system project order, customer validation, delivery and margin bridge evidence.

```text
evidence_family = NUCLEAR_CONTROL_SYSTEM_I_AND_C_PROJECT_ORDER_POLICY_SCOPE_BRIDGE
case_role = positive_with_later_4b_watch_and_sharecount_validation
trigger_date = 2024-05-10
entry_date = 2024-05-13
entry_price = 1,493
```

### Stock-Web price path

Observed rows from `atlas/ohlcv_tradable_by_symbol_year/032/032820/2024.csv`:

```text
2024-05-13,1493,1812,1488,1795
2024-05-28,2490,2650,2440,2650
2024-07-09,2430,2915,2420,2825
2024-08-05,2170,2175,1800,1968
2024-12-09,1741,1761,1650,1656
```

### Backtest

```text
MFE_30D  = +77.49%
MAE_30D  = -0.33%
MFE_90D  = +95.24%
MAE_90D  = -0.33%
MFE_180D = +95.24%
MAE_180D = -0.33%
peak_180 = 2,915 on 2024-07-09
trough_180 = 1,488 on 2024-05-13
peak_to_later_drawdown = -44.39%
```

### Interpretation

This is the control-system supplier version of C04.  
It shows why C04 should not only track EPC or plant-owner names. But the share-count changes and post-peak drawdown mean runtime promotion must wait for validation and source repair.

---

## Case 3 — Counterexample / local 4B: 105840 / 우진

### Evidence status

```text
source_proxy_only = true
evidence_url_pending = true
source_repair_required = true
```

This row tests nuclear instrumentation policy proxy beta without project/order/margin bridge.

```text
evidence_family = NUCLEAR_INSTRUMENTATION_POLICY_PROXY_WITH_WEAK_PROJECT_ORDER_MARGIN_BRIDGE
case_role = counterexample_policy_proxy_local4b
trigger_date = 2024-05-24
entry_date = 2024-05-27
entry_price = 9,580
```

### Stock-Web price path

Observed rows from `atlas/ohlcv_tradable_by_symbol_year/105/105840/2024.csv`:

```text
2024-05-27,9580,11200,9430,10260
2024-07-18,10800,10950,9300,9300
2024-08-05,7980,8000,7120,7140
2024-10-17,8640,8870,8180,8240
2024-12-09,6250,6250,5630,5820
```

### Backtest

```text
MFE_30D  = +16.91%
MAE_30D  = -7.10%
MFE_90D  = +16.91%
MAE_90D  = -25.68%
MFE_180D = +16.91%
MAE_180D = -41.23%
peak_180 = 11,200 on 2024-05-27
trough_180 = 5,630 on 2024-12-09
peak_to_later_drawdown = -49.73%
```

### Interpretation

This is the C04 policy-proxy fade.  
The first move was tradable, but the project/order bridge did not hold. Without non-price evidence, the correct label is:

```text
false Stage2 / local 4B-watch
```

not durable Green.

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
do_not_raise_generic_C04_nuclear_policy_weight = true
do_not_treat_all_nuclear_policy_MFE_as_Green = true
do_not_convert_nuclear_drawdown_to_hard_4C_without_non_price_project_break = true
```

### Candidate canonical compression

Fine labels can compress into:

```text
NUCLEAR_SERVICE_CONTROL_INSTRUMENTATION_PROJECT_BRIDGE_VS_POLICY_PROXY_FADE
```

This fine archetype covers:

```text
1. nuclear service/O&M project bridge → Stage2 possible after source repair
2. nuclear control/I&C project bridge → Stage2 possible, with share-count validation
3. nuclear instrumentation policy proxy without project/order bridge → false Stage2 / local 4B-watch
```

---

## Machine-readable rows

### price source validation row

```jsonl
{"row_type": "price_source_validation", "source": "Songdaiki/stock-web", "source_url": "https://github.com/Songdaiki/stock-web", "manifest_path": "atlas/manifest.json", "schema_path": "atlas/schema.json", "universe_path": "atlas/universe/all_symbols.csv", "manifest_max_date": "2026-02-20", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "raw_shard_root": "atlas/ohlcv_raw_by_symbol_year", "validation_status": "usable_for_historical_calibration"}
```

### case rows

```jsonl
{"row_type": "case", "case_id": "R1L75-C04-130660-KEPCO-INDUSTRIAL-NUCLEAR-SERVICE-PROJECT-BRIDGE", "symbol": "130660", "company_name": "한전산업", "round": "R1", "loop": "75", "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "canonical_archetype_id": "C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY", "fine_archetype_id": "NUCLEAR_SERVICE_CONTROL_INSTRUMENTATION_PROJECT_BRIDGE_VS_POLICY_PROXY_FADE", "case_type": "nuclear_policy_project_legal_delay", "positive_or_counterexample": "positive", "best_trigger": "Stage2-Actionable-NuclearServiceProjectBridge", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 0.5, "score_price_alignment": "C04 should allow Stage2 when nuclear policy attention is tied to actual service/O&M/project scope, operating contract visibility and margin bridge. KEPCO Industrial produced very high MFE with controlled entry-basis MAE, but post-peak drawdown requires lifecycle local 4B if project-scope evidence fades.", "current_profile_verdict": "source_repair_required_before_runtime_weight", "price_source": "Songdaiki/stock-web", "notes": "Stock-web path usable; non-proxy project scope, order/customer, O&M, I&C/instrumentation, contract and margin evidence required before runtime promotion."}
{"row_type": "case", "case_id": "R1L75-C04-032820-WOORI-TECH-NUCLEAR-CONTROL-SYSTEM-BRIDGE", "symbol": "032820", "company_name": "우리기술", "round": "R1", "loop": "75", "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "canonical_archetype_id": "C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY", "fine_archetype_id": "NUCLEAR_SERVICE_CONTROL_INSTRUMENTATION_PROJECT_BRIDGE_VS_POLICY_PROXY_FADE", "case_type": "nuclear_policy_project_legal_delay", "positive_or_counterexample": "positive", "best_trigger": "Stage2-Actionable-NuclearControlSystemProjectBridge", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 0.5, "score_price_alignment": "C04 should include nuclear control/I&C suppliers when policy/project attention converts into project scope, order or customer validation. Woori Technology produced very high MFE and no entry-basis negative MAE, but share-count changes and later drawdown require validation and lifecycle local 4B.", "current_profile_verdict": "source_repair_required_before_runtime_weight", "price_source": "Songdaiki/stock-web", "notes": "Stock-web path usable; non-proxy project scope, order/customer, O&M, I&C/instrumentation, contract and margin evidence required before runtime promotion."}
{"row_type": "case", "case_id": "R1L75-C04-105840-WOOJIN-INSTRUMENTATION-POLICY-PROXY-FADE", "symbol": "105840", "company_name": "우진", "round": "R1", "loop": "75", "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "canonical_archetype_id": "C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY", "fine_archetype_id": "NUCLEAR_SERVICE_CONTROL_INSTRUMENTATION_PROJECT_BRIDGE_VS_POLICY_PROXY_FADE", "case_type": "nuclear_policy_project_legal_delay", "positive_or_counterexample": "counterexample", "best_trigger": "Stage2-FalsePositive / NuclearInstrumentationPolicyProxyFade", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 0.5, "score_price_alignment": "C04 should not treat nuclear instrumentation or policy proxy beta as durable Stage2 unless project scope, order, customer, safety instrumentation, replacement cycle or margin bridge is verified. Woojin produced an early pop but later opened severe MAE and post-peak drawdown.", "current_profile_verdict": "source_repair_required_before_runtime_weight", "price_source": "Songdaiki/stock-web", "notes": "Stock-web path usable; non-proxy project scope, order/customer, O&M, I&C/instrumentation, contract and margin evidence required before runtime promotion."}
```

### trigger rows

```jsonl
{"row_type": "trigger", "trigger_id": "TRG_R1L75-C04-130660-KEPCO-INDUSTRIAL-NUCLEAR-SERVICE-PROJECT-BRIDGE", "case_id": "R1L75-C04-130660-KEPCO-INDUSTRIAL-NUCLEAR-SERVICE-PROJECT-BRIDGE", "symbol": "130660", "company_name": "한전산업", "round": "R1", "loop": "75", "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "canonical_archetype_id": "C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY", "fine_archetype_id": "NUCLEAR_SERVICE_CONTROL_INSTRUMENTATION_PROJECT_BRIDGE_VS_POLICY_PROXY_FADE", "loop_objective": "coverage_gap_fill|counterexample_mining|policy_project_contract_bridge_guardrail", "trigger_type": "Stage2-Actionable-NuclearServiceProjectBridge", "trigger_date": "2024-05-24", "entry_date": "2024-05-27", "entry_price": 8800.0, "evidence_available_at_that_date": "NUCLEAR_SERVICE_OPERATION_MAINTENANCE_POLICY_PROJECT_SCOPE_MARGIN_BRIDGE", "evidence_source": "source_proxy_manual_verification_required:KEPCO_INDUSTRIAL_2024_NUCLEAR_SERVICE_O_AND_M_PROJECT_SCOPE_MARGIN_BRIDGE", "stage2_evidence_fields": ["nuclear_policy_event", "project_scope_or_order_candidate", "margin_bridge_candidate"], "stage3_evidence_fields": ["relative_strength", "contract_or_customer_bridge_candidate"], "stage4b_evidence_fields": ["bridge_stale_or_absent", "MAE_widening", "post_peak_drawdown"], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/130/130660/2024.csv", "profile_path": "atlas/symbol_profiles/130/130660.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": 65.57, "MFE_90D_pct": 121.59, "MFE_180D_pct": 121.59, "MAE_30D_pct": -1.82, "MAE_90D_pct": -1.82, "MAE_180D_pct": -1.82, "peak_date": "2024-07-18", "peak_price": 19500.0, "drawdown_after_peak_pct": -54.46, "green_lateness_ratio": null, "four_b_local_peak_proximity": "local_4b_watch_after_nuclear_policy_or_project_peak_if_bridge_fades", "four_b_full_window_peak_proximity": "full_4b_requires_non_price_project_delay_contract_loss_regulatory_or_margin_break", "trigger_outcome_label": "positive_with_later_4b_watch", "current_profile_verdict": "C04 should allow Stage2 when nuclear policy attention is tied to actual service/O&M/project scope, operating contract visibility and margin bridge. KEPCO Industrial produced very high MFE with controlled entry-basis MAE, but post-peak drawdown requires lifecycle local 4B if project-scope evidence fades.", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window_by_profile", "share_count_change_inside_window": false, "same_entry_group_id": "C04_NUCLEAR_PROJECT_130660_2024-05-27", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 0.5, "do_not_count_as_new_case": false, "source_proxy_only": true, "evidence_url_pending": true}
{"row_type": "trigger", "trigger_id": "TRG_R1L75-C04-032820-WOORI-TECH-NUCLEAR-CONTROL-SYSTEM-BRIDGE", "case_id": "R1L75-C04-032820-WOORI-TECH-NUCLEAR-CONTROL-SYSTEM-BRIDGE", "symbol": "032820", "company_name": "우리기술", "round": "R1", "loop": "75", "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "canonical_archetype_id": "C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY", "fine_archetype_id": "NUCLEAR_SERVICE_CONTROL_INSTRUMENTATION_PROJECT_BRIDGE_VS_POLICY_PROXY_FADE", "loop_objective": "coverage_gap_fill|counterexample_mining|policy_project_contract_bridge_guardrail", "trigger_type": "Stage2-Actionable-NuclearControlSystemProjectBridge", "trigger_date": "2024-05-10", "entry_date": "2024-05-13", "entry_price": 1493.0, "evidence_available_at_that_date": "NUCLEAR_CONTROL_SYSTEM_I_AND_C_PROJECT_ORDER_POLICY_SCOPE_BRIDGE", "evidence_source": "source_proxy_manual_verification_required:WOORI_TECH_2024_NUCLEAR_CONTROL_I_AND_C_PROJECT_ORDER_POLICY_SCOPE_BRIDGE", "stage2_evidence_fields": ["nuclear_policy_event", "project_scope_or_order_candidate", "margin_bridge_candidate"], "stage3_evidence_fields": ["relative_strength", "contract_or_customer_bridge_candidate"], "stage4b_evidence_fields": ["bridge_stale_or_absent", "MAE_widening", "post_peak_drawdown"], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/032/032820/2024.csv", "profile_path": "atlas/symbol_profiles/032/032820.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": 77.49, "MFE_90D_pct": 95.24, "MFE_180D_pct": 95.24, "MAE_30D_pct": -0.33, "MAE_90D_pct": -0.33, "MAE_180D_pct": -0.33, "peak_date": "2024-07-09", "peak_price": 2915.0, "drawdown_after_peak_pct": -44.39, "green_lateness_ratio": null, "four_b_local_peak_proximity": "local_4b_watch_after_nuclear_policy_or_project_peak_if_bridge_fades", "four_b_full_window_peak_proximity": "full_4b_requires_non_price_project_delay_contract_loss_regulatory_or_margin_break", "trigger_outcome_label": "positive_with_later_4b_watch_and_sharecount_validation", "current_profile_verdict": "C04 should include nuclear control/I&C suppliers when policy/project attention converts into project scope, order or customer validation. Woori Technology produced very high MFE and no entry-basis negative MAE, but share-count changes and later drawdown require validation and lifecycle local 4B.", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window_by_profile", "share_count_change_inside_window": true, "same_entry_group_id": "C04_NUCLEAR_PROJECT_032820_2024-05-13", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 0.5, "do_not_count_as_new_case": false, "source_proxy_only": true, "evidence_url_pending": true}
{"row_type": "trigger", "trigger_id": "TRG_R1L75-C04-105840-WOOJIN-INSTRUMENTATION-POLICY-PROXY-FADE", "case_id": "R1L75-C04-105840-WOOJIN-INSTRUMENTATION-POLICY-PROXY-FADE", "symbol": "105840", "company_name": "우진", "round": "R1", "loop": "75", "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "canonical_archetype_id": "C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY", "fine_archetype_id": "NUCLEAR_SERVICE_CONTROL_INSTRUMENTATION_PROJECT_BRIDGE_VS_POLICY_PROXY_FADE", "loop_objective": "coverage_gap_fill|counterexample_mining|policy_project_contract_bridge_guardrail", "trigger_type": "Stage2-FalsePositive / NuclearInstrumentationPolicyProxyFade", "trigger_date": "2024-05-24", "entry_date": "2024-05-27", "entry_price": 9580.0, "evidence_available_at_that_date": "NUCLEAR_INSTRUMENTATION_POLICY_PROXY_WITH_WEAK_PROJECT_ORDER_MARGIN_BRIDGE", "evidence_source": "source_proxy_manual_verification_required:WOOJIN_2024_NUCLEAR_INSTRUMENTATION_PROJECT_ORDER_MARGIN_BRIDGE", "stage2_evidence_fields": ["nuclear_policy_event", "project_scope_or_order_candidate", "margin_bridge_candidate"], "stage3_evidence_fields": ["relative_strength", "contract_or_customer_bridge_candidate"], "stage4b_evidence_fields": ["bridge_stale_or_absent", "MAE_widening", "post_peak_drawdown"], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/105/105840/2024.csv", "profile_path": "atlas/symbol_profiles/105/105840.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": 16.91, "MFE_90D_pct": 16.91, "MFE_180D_pct": 16.91, "MAE_30D_pct": -7.1, "MAE_90D_pct": -25.68, "MAE_180D_pct": -41.23, "peak_date": "2024-05-27", "peak_price": 11200.0, "drawdown_after_peak_pct": -49.73, "green_lateness_ratio": null, "four_b_local_peak_proximity": "local_4b_watch_after_nuclear_policy_or_project_peak_if_bridge_fades", "four_b_full_window_peak_proximity": "full_4b_requires_non_price_project_delay_contract_loss_regulatory_or_margin_break", "trigger_outcome_label": "counterexample_policy_proxy_local4b", "current_profile_verdict": "C04 should not treat nuclear instrumentation or policy proxy beta as durable Stage2 unless project scope, order, customer, safety instrumentation, replacement cycle or margin bridge is verified. Woojin produced an early pop but later opened severe MAE and post-peak drawdown.", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window_by_profile", "share_count_change_inside_window": false, "same_entry_group_id": "C04_NUCLEAR_PROJECT_105840_2024-05-27", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 0.5, "do_not_count_as_new_case": false, "source_proxy_only": true, "evidence_url_pending": true}
```

### score simulation rows

```jsonl
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R1L75-C04-130660-KEPCO-INDUSTRIAL-NUCLEAR-SERVICE-PROJECT-BRIDGE", "trigger_id": "TRG_R1L75-C04-130660-KEPCO-INDUSTRIAL-NUCLEAR-SERVICE-PROJECT-BRIDGE", "symbol": "130660", "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "canonical_archetype_id": "C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY", "raw_component_scores_before": {"policy_or_regulatory_score": 13, "contract_score": 8, "backlog_visibility_score": 9, "margin_bridge_score": 10, "revision_score": 8, "relative_strength_score": 15, "customer_quality_score": 9, "execution_risk_score": 6, "legal_or_contract_risk_score": 7, "dilution_or_sharecount_risk_score": 0}, "weighted_score_before": 82, "stage_label_before": "Stage2-Actionable after source repair", "raw_component_scores_after": {"policy_or_regulatory_score": 8, "contract_score": 11, "backlog_visibility_score": 11, "margin_bridge_score": 12, "revision_score": 9, "relative_strength_score": 15, "customer_quality_score": 10, "execution_risk_score": 7, "legal_or_contract_risk_score": 8, "dilution_or_sharecount_risk_score": 0}, "weighted_score_after": 88, "stage_label_after": "Stage2/Green candidate after source repair + lifecycle 4B", "changed_components": ["policy_or_regulatory_score", "contract_score", "backlog_visibility_score", "margin_bridge_score", "execution_risk_score"], "component_delta_explanation": "Reward only verified nuclear project scope, O&M/I&C/instrumentation order and margin bridge; cap policy proxy beta when project/order bridge fails to refresh.", "MFE_90D_pct": 121.59, "MAE_90D_pct": -1.82, "score_return_alignment_label": "aligned_positive_with_lifecycle_4b", "current_profile_verdict": "C04 should allow Stage2 when nuclear policy attention is tied to actual service/O&M/project scope, operating contract visibility and margin bridge. KEPCO Industrial produced very high MFE with controlled entry-basis MAE, but post-peak drawdown requires lifecycle local 4B if project-scope evidence fades."}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R1L75-C04-032820-WOORI-TECH-NUCLEAR-CONTROL-SYSTEM-BRIDGE", "trigger_id": "TRG_R1L75-C04-032820-WOORI-TECH-NUCLEAR-CONTROL-SYSTEM-BRIDGE", "symbol": "032820", "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "canonical_archetype_id": "C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY", "raw_component_scores_before": {"policy_or_regulatory_score": 13, "contract_score": 8, "backlog_visibility_score": 9, "margin_bridge_score": 10, "revision_score": 8, "relative_strength_score": 15, "customer_quality_score": 9, "execution_risk_score": 6, "legal_or_contract_risk_score": 7, "dilution_or_sharecount_risk_score": 8}, "weighted_score_before": 82, "stage_label_before": "Stage2-Actionable after source repair", "raw_component_scores_after": {"policy_or_regulatory_score": 8, "contract_score": 11, "backlog_visibility_score": 11, "margin_bridge_score": 12, "revision_score": 9, "relative_strength_score": 15, "customer_quality_score": 10, "execution_risk_score": 7, "legal_or_contract_risk_score": 8, "dilution_or_sharecount_risk_score": 10}, "weighted_score_after": 88, "stage_label_after": "Stage2/Green candidate after source repair + lifecycle 4B", "changed_components": ["policy_or_regulatory_score", "contract_score", "backlog_visibility_score", "margin_bridge_score", "execution_risk_score"], "component_delta_explanation": "Reward only verified nuclear project scope, O&M/I&C/instrumentation order and margin bridge; cap policy proxy beta when project/order bridge fails to refresh.", "MFE_90D_pct": 95.24, "MAE_90D_pct": -0.33, "score_return_alignment_label": "aligned_positive_with_lifecycle_4b", "current_profile_verdict": "C04 should include nuclear control/I&C suppliers when policy/project attention converts into project scope, order or customer validation. Woori Technology produced very high MFE and no entry-basis negative MAE, but share-count changes and later drawdown require validation and lifecycle local 4B."}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R1L75-C04-105840-WOOJIN-INSTRUMENTATION-POLICY-PROXY-FADE", "trigger_id": "TRG_R1L75-C04-105840-WOOJIN-INSTRUMENTATION-POLICY-PROXY-FADE", "symbol": "105840", "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "canonical_archetype_id": "C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY", "raw_component_scores_before": {"policy_or_regulatory_score": 13, "contract_score": 3, "backlog_visibility_score": 3, "margin_bridge_score": 2, "revision_score": 2, "relative_strength_score": 7, "customer_quality_score": 3, "execution_risk_score": 16, "legal_or_contract_risk_score": 7, "dilution_or_sharecount_risk_score": 0}, "weighted_score_before": 53, "stage_label_before": "Stage2-FalsePositive / local 4B-watch", "raw_component_scores_after": {"policy_or_regulatory_score": 8, "contract_score": 2, "backlog_visibility_score": 1, "margin_bridge_score": 1, "revision_score": 1, "relative_strength_score": 4, "customer_quality_score": 2, "execution_risk_score": 19, "legal_or_contract_risk_score": 8, "dilution_or_sharecount_risk_score": 0}, "weighted_score_after": 42, "stage_label_after": "Stage4B-local-watch / no durable Green", "changed_components": ["policy_or_regulatory_score", "contract_score", "backlog_visibility_score", "margin_bridge_score", "execution_risk_score"], "component_delta_explanation": "Reward only verified nuclear project scope, O&M/I&C/instrumentation order and margin bridge; cap policy proxy beta when project/order bridge fails to refresh.", "MFE_90D_pct": 16.91, "MAE_90D_pct": -25.68, "score_return_alignment_label": "false_positive_nuclear_policy_proxy_bridge_gap", "current_profile_verdict": "C04 should not treat nuclear instrumentation or policy proxy beta as durable Stage2 unless project scope, order, customer, safety instrumentation, replacement cycle or margin bridge is verified. Woojin produced an early pop but later opened severe MAE and post-peak drawdown."}
```

### aggregate row

```jsonl
{"row_type": "aggregate", "round": "R1", "loop": 75, "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "canonical_archetype_id": "C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY", "fine_archetype_id": "NUCLEAR_SERVICE_CONTROL_INSTRUMENTATION_PROJECT_BRIDGE_VS_POLICY_PROXY_FADE", "calibration_usable_case_count": 3, "calibration_usable_trigger_count": 3, "new_independent_case_count": 3, "reused_case_count": 0, "same_archetype_new_symbol_count": 3, "same_archetype_new_trigger_family_count": 3, "positive_case_count": 2, "counterexample_count": 1, "four_b_case_count": 3, "four_c_case_count": 0, "source_proxy_only_count": 3, "evidence_url_pending_count": 3, "share_count_change_inside_window_count": 1, "current_profile_error_count": 1, "diversity_score_summary": "+3 underused/new C04 nuclear policy symbols outside top-covered Czech/nuclear set, +3 service/control/instrumentation trigger families, +2 project-bridge positives, +1 instrumentation policy-proxy local-4B counterexample, no hard duplicate", "residual_contribution_label": "coverage_gap_fill_with_source_repair_and_sharecount_validation_needed"}
```

### shadow weight row

```jsonl
{"row_type": "shadow_weight", "round": "R1", "loop": 75, "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "canonical_archetype_id": "C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY", "axis": "nuclear_service_control_instrumentation_project_bridge_vs_policy_proxy_fade", "decision": "hold_for_source_repair_and_more_evidence", "proposed_runtime_effect": "C04 should split verified nuclear project/O&M/I&C/control-system order bridge from policy proxy beta. Stage2 requires project scope, service/O&M contract, customer/order, regulatory milestone, delivery or margin bridge. If MFE fades and MAE/post-peak drawdown opens without bridge refresh, route to local 4B-watch. Share-count changes require validation before runtime promotion.", "do_not_propose_new_weight_delta": true, "needs_more_evidence": true, "source_repair_required": ["130660", "032820", "105840"], "share_count_validation_required": ["032820"]}
```

### residual contribution row

```jsonl
{"row_type": "residual_contribution", "round": "R1", "loop": 75, "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "canonical_archetype_id": "C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY", "existing_axis_strengthened": ["stage2_required_bridge", "price_only_blowoff_blocks_positive_stage", "local_4b_watch_guard", "full_4b_requires_non_price_evidence"], "new_axis_proposed": null, "sector_specific_rule_candidate": true, "canonical_archetype_rule_candidate": true, "narrative_summary": "C04 needs project bridge proof. KEPCO Industrial and Woori Technology show service/control-system project positives after source repair; Woojin shows nuclear instrumentation policy beta fading into local 4B when order/margin bridge is absent."}
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
130660:
  corporate_action_candidate_dates = none
  selected window = 2024-05-27~D+180
  contamination = false

032820:
  corporate_action_candidate_dates = 2003-10-28, 2005-06-07, 2007-07-03, 2007-07-31, 2009-07-29
  selected window = 2024-05-13~D+180
  contamination = false by profile
  share_count_change_inside_window = true → coding-agent validation required

105840:
  corporate_action_candidate_dates = 2012-11-19, 2012-12-11
  selected window = 2024-05-27~D+180
  contamination = false
```

Data-quality caveat:

```text
All selected C04 rows are source_proxy_only / evidence_url_pending.
032820 also requires share-count validation before runtime promotion.
This MD is useful for stock-web path calibration and C04 rule-shape discovery,
but coding-agent promotion requires non-proxy nuclear project scope, O&M, control-system, instrumentation, order/customer and margin evidence.
```

---

## Deferred Coding Agent Handoff Prompt

Do not execute this now.

```text
You are the coding agent for Songdaiki/stock_agent.

Read this standalone v12 residual research MD and ingest machine-readable rows only after validation.

Do not patch production scoring blindly.
This R1/C04 artifact is marked do_not_propose_new_weight_delta=true because all rows need source repair.

Candidate axis:
nuclear_service_control_instrumentation_project_bridge_vs_policy_proxy_fade

Required checks before implementation:
1. Validate all trigger rows against stock-web tradable_raw OHLC shards.
2. Confirm no hard duplicate key:
   canonical_archetype_id + symbol + trigger_type + entry_date.
3. Verify non-proxy source URLs for 130660, 032820 and 105840.
4. Validate 032820 share-count changes inside the selected window.
5. Keep generic C04 nuclear-policy weight unchanged until source repair is complete.
6. Consider Stage2 only when:
   - policy/project event is explicit,
   - project scope, O&M, control/I&C, instrumentation, order or customer bridge is visible,
   - delivery or margin bridge exists,
   - MAE remains controlled or the signal is treated as lifecycle Stage2.
7. Consider local 4B-watch when:
   - the trigger is nuclear policy proxy beta only,
   - project/order/margin bridge is weak or stale,
   - MAE_90D <= -20% or MAE_180D <= -25%,
   - post-peak drawdown <= -35%.
8. Do not convert local 4B-watch into full 4B/4C without non-price project delay, contract loss, regulatory halt, customer loss, financing or margin-break evidence.
9. Emit before/after diagnostics and reject if verified project/O&M/control-system positives are overblocked.
```

---

## Final round state

```text
completed_round = R1
completed_loop = 75
next_round = R2
next_loop = 75
round_schedule_status = valid
round_sector_consistency = pass
```

