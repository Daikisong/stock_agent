# E2R Stock-Web v12 Residual Research — R11 Loop 73 / L10 / C31

## Metadata

```json
{
  "research_session": "post_calibrated_sector_archetype_residual_research",
  "mode": "historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12",
  "scheduled_round": "R11",
  "scheduled_loop": 73,
  "round_schedule_status": "valid",
  "round_sector_consistency": "pass",
  "completed_round": "R11",
  "completed_loop": 73,
  "computed_next_round": "R12",
  "computed_next_loop": 73,
  "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC",
  "canonical_archetype_id": "C31_POLICY_SUBSIDY_LEGISLATION_EVENT",
  "fine_archetype_id": "CZECH_NUCLEAR_PREFERRED_BIDDER_POLICY_CONTRACT_BRIDGE_VS_PROXY_HEADLINE_CHASE",
  "loop_objective": [
    "counterexample_mining",
    "residual_false_positive_mining",
    "4B_non_price_requirement_stress_test",
    "sector_specific_rule_discovery",
    "canonical_archetype_compression",
    "policy_contract_bridge_guardrail",
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

Previous completed state in this interactive run: R10 / loop 73.

Therefore:

```text
scheduled_round = R11
scheduled_loop = 73
allowed_large_sector = L10_POLICY_EVENT_CROSS_REDTEAM_MISC or L1 policy-defense linkage
selected_large_sector = L10_POLICY_EVENT_CROSS_REDTEAM_MISC
selected_canonical_archetype_id = C31_POLICY_SUBSIDY_LEGISLATION_EVENT
computed_next_round = R12
computed_next_loop = 73
```

R11 was routed to C31 because this is a policy-event / preferred-bidder / contract-bridge guardrail, not a normal industrial backlog run.

## No-Repeat / novelty check

No hard duplicate is intentionally reused.

Hard duplicate key checked conceptually:

```text
canonical_archetype_id + symbol + trigger_type + entry_date
```

No-Repeat shows C31 concentration in `112610`, `034020`, `336260`, `UNKNOWN_SYMBOL`, and `036460`.  
This file deliberately avoids those top-covered symbols and uses:

```text
052690 / 한전기술 / EPC-engineering proxy chase
051600 / 한전KPS / service-maintenance proxy RiskWatch
083650 / 비에이치아이 / nuclear-equipment delayed bridge
```

## Evidence event

Reuters reported on 2024-07-17 that South Korea's KHNP was selected by the Czech government as preferred bidder for two nuclear reactors, with contract details still to be finalized and a target to complete the deal later. This is a real policy/contract event, but not by itself a company-level cash-flow bridge for every Korean nuclear proxy.

```text
evidence_family = CZECH_NUCLEAR_KHNP_PREFERRED_BIDDER_POLICY_CONTRACT_EVENT
trigger_date = 2024-07-17
entry_date = 2024-07-18
```

## Research thesis

C31 should separate policy heat from contract plumbing.

```text
preferred bidder headline
→ named company scope or subcontract allocation
→ order/backlog/revenue timing
→ margin bridge
→ durable rerating
```

A preferred-bidder headline is the invitation to the construction site.  
A contract bridge is the work order with the company name on it.

Without that bridge, a price gap is just a crowd at the gate.

---

## Case 1 — Counterexample: 052690 / 한전기술

### Evidence status

```text
Reuters policy event = non-proxy
company-level contract/scope bridge = evidence_url_pending
```

```text
evidence_family = CZECH_NUCLEAR_KHNP_PREFERRED_BIDDER_EPC_ENGINEERING_PROXY_WITH_WEAK_DIRECT_CONTRACT_BRIDGE
case_role = counterexample
trigger_date = 2024-07-17
entry_date = 2024-07-18
entry_price = 95,000
```

### Stock-Web price path

Observed rows from `atlas/ohlcv_tradable_by_symbol_year/052/052690/2024.csv` and `2025.csv`:

```text
2024-07-18,95000,98100,80700,82000
2024-08-05,69800,70200,61600,63300
2025-02-14,70600,75900,69800,72000
2025-04-09,51100,52000,49800,49950
```

### Backtest

```text
MFE_30D  = +3.26%
MAE_30D  = -35.16%
MFE_90D  = +3.26%
MAE_90D  = -35.16%
MFE_180D = +3.26%
MAE_180D = -47.58%
peak_180 = 98,100 on 2024-07-18
trough_180 = 49,800 on 2025-04-09
peak_to_later_drawdown = -49.24%
```

### Interpretation

This is the C31 policy-headline chase failure.  
The market bought the EPC/engineering proxy at the gap, but the stock-web path says the direct company bridge was not ready.

For C31, the rule should require:

```text
named scope
subcontract allocation
revenue timing
or backlog bridge
```

before Stage2/Green.

---

## Case 2 — RiskWatch / no full 4B: 051600 / 한전KPS

### Evidence status

```text
Reuters policy event = non-proxy
company-level O&M/service scope bridge = evidence_url_pending
```

```text
evidence_family = CZECH_NUCLEAR_KHNP_PREFERRED_BIDDER_SERVICE_MAINTENANCE_PROXY_WITH_STABLE_BUFFER
case_role = overbearish_counterexample
trigger_date = 2024-07-17
entry_date = 2024-07-18
entry_price = 43,500
```

### Stock-Web price path

Observed rows from `atlas/ohlcv_tradable_by_symbol_year/051/051600/2024.csv` and `2025.csv`:

```text
2024-07-18,43500,47450,38550,38900
2024-08-05,38450,38850,35850,37000
2025-01-24,47300,48100,46850,47500
2025-04-09,38500,39100,38000,38200
```

### Backtest

```text
MFE_30D  = +9.08%
MAE_30D  = -17.59%
MFE_90D  = +9.08%
MAE_90D  = -17.59%
MFE_180D = +10.57%
MAE_180D = -17.59%
peak_180 = 48,100 on 2025-01-24
trough_180 = 35,850 on 2024-08-05
peak_to_later_drawdown = -20.99%
```

### Interpretation

This is not a positive Green row.  
But it is also not full 4B or hard 4C.

Service/O&M proxy exposure should be RiskWatch until actual service scope, O&M participation, or backlog bridge is visible. The bounded MAE and later recovery argue against overclassification.

---

## Case 3 — Delayed positive with early local 4B risk: 083650 / 비에이치아이

### Evidence status

```text
Reuters policy event = non-proxy
company-level equipment/order/backlog bridge = evidence_url_pending
```

```text
evidence_family = CZECH_NUCLEAR_POLICY_EQUIPMENT_BOILER_HRSG_ORDER_BACKLOG_BRIDGE_WITH_DELAYED_RERATING
case_role = delayed_positive_with_local4b_risk
trigger_date = 2024-07-17
entry_date = 2024-07-18
entry_price = 10,210
```

### Stock-Web price path

Observed rows from `atlas/ohlcv_tradable_by_symbol_year/083/083650/2024.csv` and `2025.csv`:

```text
2024-07-18,10210,10530,8760,8810
2024-08-05,8150,8190,7100,7400
2024-11-22,17340,19920,17230,19100
2025-02-14,22000,24800,21600,23000
2025-04-07,15910,16060,15270,15480
```

### Backtest

```text
MFE_30D  = +3.13%
MAE_30D  = -30.46%
MFE_90D  = +95.10%
MAE_90D  = -30.46%
MFE_180D = +142.90%
MAE_180D = -30.46%
peak_180 = 24,800 on 2025-02-14
trough_180 = 7,100 on 2024-08-05
peak_to_later_drawdown = -38.43%
```

### Interpretation

This is the most important R11 row.

It says two things at once:

```text
1. Blind policy-gap entry was bad because early MAE was severe.
2. The equipment/backlog bridge may still become real later.
```

So C31 should not simply block all nuclear equipment names.  
It should require non-proxy order/backlog evidence before positive Stage2, and also use local 4B-watch after the later peak if evidence stops refreshing.

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
do_not_raise_generic_C31_nuclear_policy_weight = true
do_not_treat_preferred_bidder_headline_as_Green_without_company_scope = true
do_not_overblock_true_equipment_backlog_winners_after_source_repair = true
do_not_convert_policy_proxy_drawdown_to_hard_4C_without_non_price_break = true
```

### Candidate canonical compression

Fine labels can compress into:

```text
CZECH_NUCLEAR_PREFERRED_BIDDER_POLICY_CONTRACT_BRIDGE_VS_PROXY_HEADLINE_CHASE
```

This fine archetype covers:

```text
1. EPC/engineering proxy gap chase without direct scope bridge → false Stage2 / local 4B
2. service/O&M proxy with bounded MAE → RiskWatch / no full 4B
3. equipment/backlog beneficiary with delayed rerating → Stage2 only after source repair, later local 4B after peak
```

---

## Machine-readable rows

### price source validation row

```jsonl
{"row_type": "price_source_validation", "source": "Songdaiki/stock-web", "source_url": "https://github.com/Songdaiki/stock-web", "manifest_path": "atlas/manifest.json", "schema_path": "atlas/schema.json", "universe_path": "atlas/universe/all_symbols.csv", "manifest_max_date": "2026-02-20", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "raw_shard_root": "atlas/ohlcv_raw_by_symbol_year", "validation_status": "usable_for_historical_calibration"}
```

### case rows

```jsonl
{"row_type": "case", "case_id": "R11L73-C31-052690-KEPCO-ENC-CZECH-NUCLEAR-EPC-PROXY-CHASE", "symbol": "052690", "company_name": "한전기술", "round": "R11", "loop": "73", "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "C31_POLICY_SUBSIDY_LEGISLATION_EVENT", "fine_archetype_id": "CZECH_NUCLEAR_PREFERRED_BIDDER_POLICY_CONTRACT_BRIDGE_VS_PROXY_HEADLINE_CHASE", "case_type": "policy_subsidy_legislation_event_nuclear_contract_bridge", "positive_or_counterexample": "counterexample", "best_trigger": "Stage2-FalsePositive / NuclearEPCPolicyHeadlineChase", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 0.7, "score_price_alignment": "C31 should not treat the nuclear preferred-bidder headline as durable Stage2 for EPC/engineering proxies unless named scope, contract allocation, revenue timing, or backlog bridge is visible. KEPCO E&C gapped into the event but then opened severe MAE and drawdown.", "current_profile_verdict": "company_level_contract_bridge_source_repair_required", "price_source": "Songdaiki/stock-web", "notes": "Reuters policy event source is non-proxy, but company-level contract/scope/backlog bridge remains evidence_url_pending."}
{"row_type": "case", "case_id": "R11L73-C31-051600-KEPCO-KPS-CZECH-NUCLEAR-SERVICE-PROXY-RISKWATCH", "symbol": "051600", "company_name": "한전KPS", "round": "R11", "loop": "73", "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "C31_POLICY_SUBSIDY_LEGISLATION_EVENT", "fine_archetype_id": "CZECH_NUCLEAR_PREFERRED_BIDDER_POLICY_CONTRACT_BRIDGE_VS_PROXY_HEADLINE_CHASE", "case_type": "policy_subsidy_legislation_event_nuclear_contract_bridge", "positive_or_counterexample": "overbearish_counterexample", "best_trigger": "Stage2-RiskWatch / NuclearServiceProxyNoFull4B", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 0.7, "score_price_alignment": "C31 should flag nuclear service proxies as RiskWatch unless service scope, O&M participation, or backlog bridge is verified. KEPCO KPS had bounded MAE and later recovery, so it should not become full 4B or hard 4C from the policy headline alone.", "current_profile_verdict": "company_level_contract_bridge_source_repair_required", "price_source": "Songdaiki/stock-web", "notes": "Reuters policy event source is non-proxy, but company-level contract/scope/backlog bridge remains evidence_url_pending."}
{"row_type": "case", "case_id": "R11L73-C31-083650-BHI-CZECH-NUCLEAR-EQUIPMENT-DELAYED-BRIDGE", "symbol": "083650", "company_name": "비에이치아이", "round": "R11", "loop": "73", "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "C31_POLICY_SUBSIDY_LEGISLATION_EVENT", "fine_archetype_id": "CZECH_NUCLEAR_PREFERRED_BIDDER_POLICY_CONTRACT_BRIDGE_VS_PROXY_HEADLINE_CHASE", "case_type": "policy_subsidy_legislation_event_nuclear_contract_bridge", "positive_or_counterexample": "delayed_positive", "best_trigger": "Stage2-DelayedPositive / NuclearEquipmentBridgeWithEarlyMAE", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 0.7, "score_price_alignment": "C31 should not overblock true nuclear equipment/backlog beneficiaries, but the entry should not be a blind policy-headline chase. BHI had severe early MAE before later rerating; Stage2 requires non-proxy equipment order/backlog evidence and a lifecycle local 4B after peak.", "current_profile_verdict": "company_level_contract_bridge_source_repair_required", "price_source": "Songdaiki/stock-web", "notes": "Reuters policy event source is non-proxy, but company-level contract/scope/backlog bridge remains evidence_url_pending."}
```

### trigger rows

```jsonl
{"row_type": "trigger", "trigger_id": "TRG_R11L73-C31-052690-KEPCO-ENC-CZECH-NUCLEAR-EPC-PROXY-CHASE", "case_id": "R11L73-C31-052690-KEPCO-ENC-CZECH-NUCLEAR-EPC-PROXY-CHASE", "symbol": "052690", "company_name": "한전기술", "round": "R11", "loop": "73", "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "C31_POLICY_SUBSIDY_LEGISLATION_EVENT", "fine_archetype_id": "CZECH_NUCLEAR_PREFERRED_BIDDER_POLICY_CONTRACT_BRIDGE_VS_PROXY_HEADLINE_CHASE", "loop_objective": "counterexample_mining|policy_contract_bridge_guardrail|4B_non_price_requirement_stress_test", "trigger_type": "Stage2-FalsePositive / NuclearEPCPolicyHeadlineChase", "trigger_date": "2024-07-17", "entry_date": "2024-07-18", "entry_price": 95000.0, "evidence_available_at_that_date": "CZECH_NUCLEAR_KHNP_PREFERRED_BIDDER_EPC_ENGINEERING_PROXY_WITH_WEAK_DIRECT_CONTRACT_BRIDGE", "evidence_source": "https://www.reuters.com/business/energy/south-koreas-winning-bid-czech-nuclear-power-project-2024-07-17/", "stage2_evidence_fields": ["policy_event", "preferred_bidder", "contract_bridge_candidate"], "stage3_evidence_fields": ["relative_strength", "scope_or_backlog_bridge_candidate"], "stage4b_evidence_fields": ["bridge_absent_or_stale", "MAE_widening", "post_peak_drawdown"], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/052/052690/2024.csv", "profile_path": "atlas/symbol_profiles/052/052690.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": 3.26, "MFE_90D_pct": 3.26, "MFE_180D_pct": 3.26, "MAE_30D_pct": -35.16, "MAE_90D_pct": -35.16, "MAE_180D_pct": -47.58, "peak_date": "2024-07-18", "peak_price": 98100.0, "drawdown_after_peak_pct": -49.24, "green_lateness_ratio": null, "four_b_local_peak_proximity": "local_4b_watch_after_policy_gap_or_contract_bridge_fades", "four_b_full_window_peak_proximity": "full_4b_requires_non_price_contract_failure_or_project_scope_break", "trigger_outcome_label": "counterexample", "current_profile_verdict": "C31 should not treat the nuclear preferred-bidder headline as durable Stage2 for EPC/engineering proxies unless named scope, contract allocation, revenue timing, or backlog bridge is visible. KEPCO E&C gapped into the event but then opened severe MAE and drawdown.", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window", "same_entry_group_id": "C31_CZECH_NUCLEAR_20240718_PROXY_GROUP", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 0.7, "do_not_count_as_new_case": false, "source_proxy_only": false, "evidence_url_pending": true}
{"row_type": "trigger", "trigger_id": "TRG_R11L73-C31-051600-KEPCO-KPS-CZECH-NUCLEAR-SERVICE-PROXY-RISKWATCH", "case_id": "R11L73-C31-051600-KEPCO-KPS-CZECH-NUCLEAR-SERVICE-PROXY-RISKWATCH", "symbol": "051600", "company_name": "한전KPS", "round": "R11", "loop": "73", "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "C31_POLICY_SUBSIDY_LEGISLATION_EVENT", "fine_archetype_id": "CZECH_NUCLEAR_PREFERRED_BIDDER_POLICY_CONTRACT_BRIDGE_VS_PROXY_HEADLINE_CHASE", "loop_objective": "counterexample_mining|policy_contract_bridge_guardrail|4B_non_price_requirement_stress_test", "trigger_type": "Stage2-RiskWatch / NuclearServiceProxyNoFull4B", "trigger_date": "2024-07-17", "entry_date": "2024-07-18", "entry_price": 43500.0, "evidence_available_at_that_date": "CZECH_NUCLEAR_KHNP_PREFERRED_BIDDER_SERVICE_MAINTENANCE_PROXY_WITH_STABLE_BUFFER", "evidence_source": "https://www.reuters.com/business/energy/south-koreas-winning-bid-czech-nuclear-power-project-2024-07-17/", "stage2_evidence_fields": ["policy_event", "preferred_bidder", "contract_bridge_candidate"], "stage3_evidence_fields": ["relative_strength", "scope_or_backlog_bridge_candidate"], "stage4b_evidence_fields": ["bridge_absent_or_stale", "MAE_widening", "post_peak_drawdown"], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/051/051600/2024.csv", "profile_path": "atlas/symbol_profiles/051/051600.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": 9.08, "MFE_90D_pct": 9.08, "MFE_180D_pct": 10.57, "MAE_30D_pct": -17.59, "MAE_90D_pct": -17.59, "MAE_180D_pct": -17.59, "peak_date": "2025-01-24", "peak_price": 48100.0, "drawdown_after_peak_pct": -20.99, "green_lateness_ratio": null, "four_b_local_peak_proximity": "local_4b_watch_after_policy_gap_or_contract_bridge_fades", "four_b_full_window_peak_proximity": "full_4b_requires_non_price_contract_failure_or_project_scope_break", "trigger_outcome_label": "overbearish_counterexample", "current_profile_verdict": "C31 should flag nuclear service proxies as RiskWatch unless service scope, O&M participation, or backlog bridge is verified. KEPCO KPS had bounded MAE and later recovery, so it should not become full 4B or hard 4C from the policy headline alone.", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window", "same_entry_group_id": "C31_CZECH_NUCLEAR_20240718_PROXY_GROUP", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 0.7, "do_not_count_as_new_case": false, "source_proxy_only": false, "evidence_url_pending": true}
{"row_type": "trigger", "trigger_id": "TRG_R11L73-C31-083650-BHI-CZECH-NUCLEAR-EQUIPMENT-DELAYED-BRIDGE", "case_id": "R11L73-C31-083650-BHI-CZECH-NUCLEAR-EQUIPMENT-DELAYED-BRIDGE", "symbol": "083650", "company_name": "비에이치아이", "round": "R11", "loop": "73", "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "C31_POLICY_SUBSIDY_LEGISLATION_EVENT", "fine_archetype_id": "CZECH_NUCLEAR_PREFERRED_BIDDER_POLICY_CONTRACT_BRIDGE_VS_PROXY_HEADLINE_CHASE", "loop_objective": "counterexample_mining|policy_contract_bridge_guardrail|4B_non_price_requirement_stress_test", "trigger_type": "Stage2-DelayedPositive / NuclearEquipmentBridgeWithEarlyMAE", "trigger_date": "2024-07-17", "entry_date": "2024-07-18", "entry_price": 10210.0, "evidence_available_at_that_date": "CZECH_NUCLEAR_POLICY_EQUIPMENT_BOILER_HRSG_ORDER_BACKLOG_BRIDGE_WITH_DELAYED_RERATING", "evidence_source": "https://www.reuters.com/business/energy/south-koreas-winning-bid-czech-nuclear-power-project-2024-07-17/", "stage2_evidence_fields": ["policy_event", "preferred_bidder", "contract_bridge_candidate"], "stage3_evidence_fields": ["relative_strength", "scope_or_backlog_bridge_candidate"], "stage4b_evidence_fields": ["bridge_absent_or_stale", "MAE_widening", "post_peak_drawdown"], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/083/083650/2024.csv", "profile_path": "atlas/symbol_profiles/083/083650.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": 3.13, "MFE_90D_pct": 95.1, "MFE_180D_pct": 142.9, "MAE_30D_pct": -30.46, "MAE_90D_pct": -30.46, "MAE_180D_pct": -30.46, "peak_date": "2025-02-14", "peak_price": 24800.0, "drawdown_after_peak_pct": -38.43, "green_lateness_ratio": null, "four_b_local_peak_proximity": "local_4b_watch_after_policy_gap_or_contract_bridge_fades", "four_b_full_window_peak_proximity": "full_4b_requires_non_price_contract_failure_or_project_scope_break", "trigger_outcome_label": "delayed_positive_with_local4b_risk", "current_profile_verdict": "C31 should not overblock true nuclear equipment/backlog beneficiaries, but the entry should not be a blind policy-headline chase. BHI had severe early MAE before later rerating; Stage2 requires non-proxy equipment order/backlog evidence and a lifecycle local 4B after peak.", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window", "same_entry_group_id": "C31_CZECH_NUCLEAR_20240718_PROXY_GROUP", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 0.7, "do_not_count_as_new_case": false, "source_proxy_only": false, "evidence_url_pending": true}
```

### score simulation rows

```jsonl
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R11L73-C31-052690-KEPCO-ENC-CZECH-NUCLEAR-EPC-PROXY-CHASE", "trigger_id": "TRG_R11L73-C31-052690-KEPCO-ENC-CZECH-NUCLEAR-EPC-PROXY-CHASE", "symbol": "052690", "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "C31_POLICY_SUBSIDY_LEGISLATION_EVENT", "raw_component_scores_before": {"policy_or_regulatory_score": 16, "contract_score": 6, "backlog_visibility_score": 4, "margin_bridge_score": 2, "relative_strength_score": 5, "execution_risk_score": 12, "legal_or_contract_risk_score": 8, "customer_quality_score": 4, "source_confidence_score": 3}, "weighted_score_before": 65, "stage_label_before": "Stage2-Watch / policy headline beta", "raw_component_scores_after": {"policy_or_regulatory_score": 9, "contract_score": 2, "backlog_visibility_score": 1, "margin_bridge_score": 1, "relative_strength_score": 3, "execution_risk_score": 17, "legal_or_contract_risk_score": 10, "customer_quality_score": 2, "source_confidence_score": 3}, "weighted_score_after": 45, "stage_label_after": "Stage4B-local-watch / no durable Green", "changed_components": ["policy_or_regulatory_score", "contract_score", "backlog_visibility_score", "execution_risk_score"], "component_delta_explanation": "Cap preferred-bidder policy headline unless named company scope, contract allocation, revenue timing or backlog bridge is verified.", "MFE_90D_pct": 3.26, "MAE_90D_pct": -35.16, "score_return_alignment_label": "policy_headline_false_positive", "current_profile_verdict": "C31 should not treat the nuclear preferred-bidder headline as durable Stage2 for EPC/engineering proxies unless named scope, contract allocation, revenue timing, or backlog bridge is visible. KEPCO E&C gapped into the event but then opened severe MAE and drawdown."}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R11L73-C31-051600-KEPCO-KPS-CZECH-NUCLEAR-SERVICE-PROXY-RISKWATCH", "trigger_id": "TRG_R11L73-C31-051600-KEPCO-KPS-CZECH-NUCLEAR-SERVICE-PROXY-RISKWATCH", "symbol": "051600", "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "C31_POLICY_SUBSIDY_LEGISLATION_EVENT", "raw_component_scores_before": {"policy_or_regulatory_score": 16, "contract_score": 6, "backlog_visibility_score": 4, "margin_bridge_score": 2, "relative_strength_score": 5, "execution_risk_score": 12, "legal_or_contract_risk_score": 8, "customer_quality_score": 4, "source_confidence_score": 3}, "weighted_score_before": 65, "stage_label_before": "Stage2-Watch / policy headline beta", "raw_component_scores_after": {"policy_or_regulatory_score": 9, "contract_score": 2, "backlog_visibility_score": 1, "margin_bridge_score": 1, "relative_strength_score": 3, "execution_risk_score": 11, "legal_or_contract_risk_score": 10, "customer_quality_score": 2, "source_confidence_score": 3}, "weighted_score_after": 55, "stage_label_after": "RiskWatch / no full 4B", "changed_components": ["policy_or_regulatory_score", "contract_score", "backlog_visibility_score", "execution_risk_score"], "component_delta_explanation": "Cap preferred-bidder policy headline unless named company scope, contract allocation, revenue timing or backlog bridge is verified.", "MFE_90D_pct": 9.08, "MAE_90D_pct": -17.59, "score_return_alignment_label": "riskwatch_no_full4b", "current_profile_verdict": "C31 should flag nuclear service proxies as RiskWatch unless service scope, O&M participation, or backlog bridge is verified. KEPCO KPS had bounded MAE and later recovery, so it should not become full 4B or hard 4C from the policy headline alone."}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R11L73-C31-083650-BHI-CZECH-NUCLEAR-EQUIPMENT-DELAYED-BRIDGE", "trigger_id": "TRG_R11L73-C31-083650-BHI-CZECH-NUCLEAR-EQUIPMENT-DELAYED-BRIDGE", "symbol": "083650", "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "C31_POLICY_SUBSIDY_LEGISLATION_EVENT", "raw_component_scores_before": {"policy_or_regulatory_score": 16, "contract_score": 8, "backlog_visibility_score": 8, "margin_bridge_score": 6, "relative_strength_score": 10, "execution_risk_score": 12, "legal_or_contract_risk_score": 8, "customer_quality_score": 4, "source_confidence_score": 3}, "weighted_score_before": 74, "stage_label_before": "Stage2-Watch / policy headline beta", "raw_component_scores_after": {"policy_or_regulatory_score": 9, "contract_score": 6, "backlog_visibility_score": 7, "margin_bridge_score": 5, "relative_strength_score": 13, "execution_risk_score": 17, "legal_or_contract_risk_score": 10, "customer_quality_score": 2, "source_confidence_score": 3}, "weighted_score_after": 78, "stage_label_after": "Delayed Stage2 candidate after source repair + local 4B lifecycle", "changed_components": ["policy_or_regulatory_score", "contract_score", "backlog_visibility_score", "execution_risk_score"], "component_delta_explanation": "Cap preferred-bidder policy headline unless named company scope, contract allocation, revenue timing or backlog bridge is verified.", "MFE_90D_pct": 95.1, "MAE_90D_pct": -30.46, "score_return_alignment_label": "delayed_positive_after_early_mae", "current_profile_verdict": "C31 should not overblock true nuclear equipment/backlog beneficiaries, but the entry should not be a blind policy-headline chase. BHI had severe early MAE before later rerating; Stage2 requires non-proxy equipment order/backlog evidence and a lifecycle local 4B after peak."}
```

### aggregate row

```jsonl
{"row_type": "aggregate", "round": "R11", "loop": 73, "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "C31_POLICY_SUBSIDY_LEGISLATION_EVENT", "fine_archetype_id": "CZECH_NUCLEAR_PREFERRED_BIDDER_POLICY_CONTRACT_BRIDGE_VS_PROXY_HEADLINE_CHASE", "calibration_usable_case_count": 3, "calibration_usable_trigger_count": 3, "new_independent_case_count": 3, "reused_case_count": 0, "same_archetype_new_symbol_count": 3, "same_archetype_new_trigger_family_count": 1, "positive_case_count": 1, "counterexample_count": 1, "overbearish_counterexample_count": 1, "four_b_case_count": 2, "four_c_case_count": 0, "source_proxy_only_count": 0, "evidence_url_pending_count": 3, "current_profile_error_count": 2, "diversity_score_summary": "+3 underused C31 nuclear-policy symbols, +1 Czech nuclear preferred-bidder trigger family, +1 delayed equipment positive, +1 EPC headline false positive, +1 service no-full-4B boundary, no hard duplicate", "residual_contribution_label": "canonical_archetype_rule_candidate_with_company_bridge_source_repair"}
```

### shadow weight row

```jsonl
{"row_type": "shadow_weight", "round": "R11", "loop": 73, "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "C31_POLICY_SUBSIDY_LEGISLATION_EVENT", "axis": "czech_nuclear_preferred_bidder_policy_contract_bridge_vs_proxy_headline_chase", "decision": "hold_for_source_repair_and_more_evidence", "proposed_runtime_effect": "C31 should cap nuclear-policy preferred-bidder proxy scores unless the event creates named company scope, contract allocation, revenue timing, supply order, or backlog bridge. Gap-up EPC/service proxy chases should route to local 4B/RiskWatch if MAE opens. Equipment names can become delayed Stage2 only after non-proxy order/backlog evidence is verified.", "do_not_propose_new_weight_delta": true, "needs_more_evidence": true, "source_repair_required": ["052690", "051600", "083650"]}
```

### residual contribution row

```jsonl
{"row_type": "residual_contribution", "round": "R11", "loop": 73, "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "C31_POLICY_SUBSIDY_LEGISLATION_EVENT", "existing_axis_strengthened": ["price_only_blowoff_blocks_positive_stage", "full_4b_requires_non_price_evidence", "local_4b_watch_guard", "stage2_required_bridge"], "new_axis_proposed": null, "sector_specific_rule_candidate": true, "canonical_archetype_rule_candidate": true, "narrative_summary": "C31 nuclear-policy events need contract bridge proof. KEPCO E&C shows policy headline chase failure, KEPCO KPS is service-proxy RiskWatch/no-full-4B, and BHI is a delayed equipment winner that still suffered severe early MAE and needs non-proxy backlog evidence."}
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
052690:
  corporate_action_candidate_dates = none
  selected window = 2024-07-18~D+180
  contamination = false

051600:
  corporate_action_candidate_dates = none
  selected window = 2024-07-18~D+180
  contamination = false

083650:
  corporate_action_candidate_dates = 2006-06-16, 2006-07-12, 2015-04-10, 2015-05-12
  selected window = 2024-07-18~D+180
  contamination = false
```

Data-quality caveat:

```text
The Czech nuclear policy event source is non-proxy Reuters evidence.
The company-level contract/scope/order/backlog bridge remains evidence_url_pending for all three rows.
This MD is useful for stock-web path calibration and C31 rule-shape discovery,
but coding-agent promotion requires non-proxy company-level contract allocation, revenue timing, order or backlog evidence.
```

---

## Deferred Coding Agent Handoff Prompt

Do not execute this now.

```text
You are the coding agent for Songdaiki/stock_agent.

Read this standalone v12 residual research MD and ingest machine-readable rows only after validation.

Do not patch production scoring blindly.
This R11/C31 artifact is marked do_not_propose_new_weight_delta=true because company-level bridge evidence needs source repair.

Candidate axis:
czech_nuclear_preferred_bidder_policy_contract_bridge_vs_proxy_headline_chase

Required checks before implementation:
1. Validate all trigger rows against stock-web tradable_raw OHLC shards.
2. Confirm no hard duplicate key:
   canonical_archetype_id + symbol + trigger_type + entry_date.
3. Verify non-proxy company-level source URLs for 052690, 051600 and 083650.
4. Keep generic C31 nuclear-policy weight unchanged until source repair is complete.
5. Consider Stage2 only when:
   - preferred bidder or policy event is explicit,
   - named company scope or subcontract allocation is visible,
   - revenue timing, order, backlog or margin bridge exists,
   - MAE remains controlled or the entry is not a pure policy-gap chase.
6. Consider local 4B-watch when:
   - the trigger is policy/proxy headline only,
   - company-level bridge is absent or stale,
   - MAE_30D or MAE_90D opens sharply,
   - post-peak drawdown <= -35%.
7. Keep RiskWatch/no-full-4B when:
   - service/O&M exposure has stable buffer,
   - direct scope is unconfirmed,
   - price drawdown exists but no non-price break is confirmed.
8. Do not convert local 4B-watch into hard 4C without non-price contract failure, project cancellation, legal break, or insolvency evidence.
9. Emit before/after diagnostics and reject if verified nuclear equipment/backlog positives are overblocked.
```

---

## Final round state

```text
completed_round = R11
completed_loop = 73
next_round = R12
next_loop = 73
round_schedule_status = valid
round_sector_consistency = pass
```

