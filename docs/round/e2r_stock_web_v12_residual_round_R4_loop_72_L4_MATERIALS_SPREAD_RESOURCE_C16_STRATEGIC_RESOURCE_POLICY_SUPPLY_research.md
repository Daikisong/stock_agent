# E2R Stock-Web v12 Residual Research — R4 Loop 72 / L4 / C16

## Metadata

```json
{
  "research_session": "post_calibrated_sector_archetype_residual_research",
  "mode": "historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12",
  "scheduled_round": "R4",
  "scheduled_loop": 72,
  "round_schedule_status": "valid",
  "round_sector_consistency": "pass",
  "completed_round": "R4",
  "completed_loop": 72,
  "computed_next_round": "R5",
  "computed_next_loop": 72,
  "large_sector_id": "L4_MATERIALS_SPREAD_RESOURCE",
  "canonical_archetype_id": "C16_STRATEGIC_RESOURCE_POLICY_SUPPLY",
  "fine_archetype_id": "GRAPHITE_CRITICAL_MINERAL_EXPORT_CONTROL_AND_SMELTER_SUPPLY_SQUEEZE_VS_PRICE_ONLY_RESOURCE_BETA",
  "loop_objective": [
    "coverage_gap_fill",
    "counterexample_mining",
    "4B_non_price_requirement_stress_test",
    "sector_specific_rule_discovery",
    "canonical_archetype_compression",
    "strategic_resource_supply_policy_bridge_test"
  ],
  "price_source": "Songdaiki/stock-web",
  "price_basis": "tradable_raw",
  "price_adjustment_status": "raw_unadjusted_marcap",
  "stock_web_manifest_max_date": "2026-02-20",
  "production_scoring_changed": false,
  "shadow_weight_only": true,
  "handoff_prompt_executed_now": false,
  "do_not_propose_new_weight_delta": false
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

Previous completed state in this interactive run: R3 / loop 72.

Therefore:

```text
scheduled_round = R4
scheduled_loop = 72
allowed_large_sector = L4_MATERIALS_SPREAD_RESOURCE
selected_large_sector = L4_MATERIALS_SPREAD_RESOURCE
selected_canonical_archetype_id = C16_STRATEGIC_RESOURCE_POLICY_SUPPLY
computed_next_round = R5
computed_next_loop = 72
```

R4 was routed to C16 because loop 71 had already filled C15.  
No-Repeat coverage shows C16 is still relatively small versus C17, so this run targets strategic-resource policy/supply rather than another chemical spread case.

## No-Repeat / novelty check

No hard duplicate is intentionally reused.

Hard duplicate key checked conceptually:

```text
canonical_archetype_id + symbol + trigger_type + entry_date
```

Selected rows:

```text
005490 / POSCO홀딩스 / StrategicResourcePolicyWatch / 2023-10-23
003670 / 포스코퓨처엠 / Stage4B-Local-StrategicResourceSupplyRisk / 2023-10-23
010130 / 고려아연 / Stage2-Actionable / LaterLocal4B / 2024-04-11
```

## Research thesis

C16 is not “resource theme went up.”

A strategic-resource event only matters if it can cross the bridge:

```text
policy or supply shock
→ restricted physical availability or higher processing value
→ company-level supply, pricing, offtake, smelter charge, or margin bridge
→ durable return path
```

Without that bridge, the headline is a flare.  
With the bridge, it becomes a road.

---

## Case 1 — Counterexample: 005490 / POSCO홀딩스 / graphite export controls as generic resource beta

### Evidence

Reuters' critical-mineral export-control snapshot states that in October 2023 China began requiring export permits for some graphite products, while China is the top graphite producer/exporter and refines more than 90% of graphite used in EV battery anodes.

```text
evidence_family = CHINA_GRAPHITE_EXPORT_CONTROL_CRITICAL_MINERAL_POLICY_WITH_WEAK_COMPANY_CASHFLOW_BRIDGE
case_role = counterexample
trigger_date = 2023-10-20
entry_date = 2023-10-23
entry_price = 452,000
```

### Stock-Web price path

Observed rows from `atlas/ohlcv_tradable_by_symbol_year/005/005490/2023.csv` and `2024.csv`:

```text
2023-10-23,452000,457500,442500,453000
2023-11-06,471000,527000,462000,522000
2024-06-28,358500,365000,355000,363000
```

### Backtest

```text
MFE_30D  = +16.59%
MAE_30D  = -11.61%
MFE_90D  = +16.59%
MAE_90D  = -11.61%
MFE_180D = +16.59%
MAE_180D = -21.46%
peak_180 = 527,000 on 2023-11-06
trough_180 = 355,000 on 2024-06-28
peak_to_later_drawdown = -32.64%
```

### Interpretation

This is the generic-policy false positive.  
POSCO Holdings had strategic material exposure, but the graphite-control headline did not by itself create a durable company-level cash-flow bridge.

The C16 rule should not reward the word “critical mineral” unless the specific company receives pricing, supply, offtake, or margin conversion.

---

## Case 2 — Risk-positive: 003670 / 포스코퓨처엠 / graphite/anode supply-chain risk

### Evidence

The same graphite export-control event matters more directly for a battery material supplier.  
For POSCO Future M, the strategic-resource shock is not a diversified holding-company story; it is an anode/cathode supply-chain risk story.

```text
evidence_family = CHINA_GRAPHITE_EXPORT_CONTROL_ANODE_SUPPLY_CHAIN_POLICY_RISK
case_role = risk_positive
trigger_date = 2023-10-20
entry_date = 2023-10-23
entry_price = 298,500
```

### Stock-Web price path

Observed rows from `atlas/ohlcv_tradable_by_symbol_year/003/003670/2023.csv` and `2024.csv`:

```text
2023-10-23,298500,310500,296000,301500
2023-12-21,361000,382000,361000,368000
2024-07-24,229500,237500,227000,227500
```

### Backtest

```text
MFE_30D  = +20.94%
MAE_30D  = -22.45%
MFE_90D  = +27.97%
MAE_90D  = -22.45%
MFE_180D = +27.97%
MAE_180D = -23.95%
peak_180 = 382,000 on 2023-12-21
trough_180 = 227,000 on 2024-07-24
peak_to_later_drawdown = -40.58%
```

### Interpretation

This is not a clean positive.  
The policy shock created a tradable squeeze, but post-peak drawdown was large. For supplier-chain names, C16 should use local 4B-watch when the supply shock does not become durable pricing/order/margin evidence.

---

## Case 3 — Positive with later local 4B: 010130 / 고려아연 / zinc smelter supply squeeze

### Evidence

Reuters reported that benchmark zinc smelter treatment charges collapsed as zinc mine supply faltered. This is closer to a company-level C16 bridge because Korea Zinc is a smelter: the shock touches concentrate availability, smelter economics, and physical supply rather than merely the label “resource.”

```text
evidence_family = ZINC_MINE_SUPPLY_TIGHTNESS_SMELTER_TREATMENT_CHARGE_COLLAPSE
case_role = positive_with_later_4b_watch
trigger_date = 2024-04-09
entry_date = 2024-04-11
entry_price = 463,000
```

### Stock-Web price path

Observed rows from `atlas/ohlcv_tradable_by_symbol_year/010/010130/2024.csv`:

```text
2024-04-11,463000,474500,462000,472000
2024-08-05,478000,478000,445000,454500
2024-12-06,2124000,2407000,1736000,1813000
2024-12-20,1020000,1024000,990000,991000
```

### Backtest

```text
MFE_30D  = +17.93%
MAE_30D  = -2.70%
MFE_90D  = +20.30%
MAE_90D  = -3.89%
MFE_180D = +419.87%
MAE_180D = -3.89%
peak_180 = 2,407,000 on 2024-12-06
trough_180 = 445,000 on 2024-08-05
peak_to_later_drawdown = -58.87%
```

### Interpretation

This is the positive C16 anchor, but it also demonstrates contamination.  
The early physical supply bridge worked. Later, the price path became a governance/control-premium blowoff rather than a pure zinc supply read-through.

So the C16 lifecycle should be:

```text
physical supply bridge → Stage2-Actionable possible
governance/price blowoff contamination → later local 4B-watch
hard 4C only with non-price thesis break
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
do_not_raise_generic_C16_policy_weight = true
do_not_treat_critical_mineral_headline_as_Green = true
do_not_convert_resource_drawdown_to_4C_without_non_price_break = true
```

### Candidate canonical compression

Fine labels can compress into:

```text
GRAPHITE_CRITICAL_MINERAL_EXPORT_CONTROL_AND_SMELTER_SUPPLY_SQUEEZE_VS_PRICE_ONLY_RESOURCE_BETA
```

This fine archetype covers:

```text
1. generic critical-mineral policy exposure → RiskWatch / false positive risk
2. battery-material supplier exposure to export-control supply chain → local 4B-watch
3. physical smelter supply/treatment-charge bridge → Stage2 possible, later local 4B if blowoff contaminates
```

---

## Machine-readable rows

### trigger rows

```jsonl
{"row_type": "trigger", "round": "R4", "loop": 72, "large_sector_id": "L4_MATERIALS_SPREAD_RESOURCE", "canonical_archetype_id": "C16_STRATEGIC_RESOURCE_POLICY_SUPPLY", "fine_archetype_id": "GRAPHITE_CRITICAL_MINERAL_EXPORT_CONTROL_AND_SMELTER_SUPPLY_SQUEEZE_VS_PRICE_ONLY_RESOURCE_BETA", "case_id": "R4L72-C16-005490-POSCOHOLDINGS-CHINA-GRAPHITE-CONTROL-LITHIUM-BETA", "symbol": "005490", "company": "POSCO홀딩스", "trigger_type": "Stage2-FalsePositive / StrategicResourcePolicyWatch", "trigger_date": "2023-10-20", "entry_date": "2023-10-23", "entry_price": 452000.0, "mfe_30_pct": 16.59, "mae_30_pct": -11.61, "mfe_90_pct": 16.59, "mae_90_pct": -11.61, "mfe_180_pct": 16.59, "mae_180_pct": -21.46, "peak_price_180": 527000.0, "peak_date_180": "2023-11-06", "trough_price_180": 355000.0, "trough_date_180": "2024-06-28", "peak_to_later_drawdown_pct": -32.64, "case_role": "counterexample", "calibration_usable": true, "corporate_action_contaminated_180d": false, "evidence_family": "CHINA_GRAPHITE_EXPORT_CONTROL_CRITICAL_MINERAL_POLICY_WITH_WEAK_COMPANY_CASHFLOW_BRIDGE", "evidence_url": "https://www.reuters.com/world/china/chinas-curbs-exports-strategic-minerals-2025-02-04/", "source_proxy_only": false, "evidence_url_pending": false}
{"row_type": "trigger", "round": "R4", "loop": 72, "large_sector_id": "L4_MATERIALS_SPREAD_RESOURCE", "canonical_archetype_id": "C16_STRATEGIC_RESOURCE_POLICY_SUPPLY", "fine_archetype_id": "GRAPHITE_CRITICAL_MINERAL_EXPORT_CONTROL_AND_SMELTER_SUPPLY_SQUEEZE_VS_PRICE_ONLY_RESOURCE_BETA", "case_id": "R4L72-C16-003670-POSCOFUTUREM-GRAPHITE-ANODE-SUPPLY-RISK", "symbol": "003670", "company": "포스코퓨처엠", "trigger_type": "Stage4B-Local-StrategicResourceSupplyRisk", "trigger_date": "2023-10-20", "entry_date": "2023-10-23", "entry_price": 298500.0, "mfe_30_pct": 20.94, "mae_30_pct": -22.45, "mfe_90_pct": 27.97, "mae_90_pct": -22.45, "mfe_180_pct": 27.97, "mae_180_pct": -23.95, "peak_price_180": 382000.0, "peak_date_180": "2023-12-21", "trough_price_180": 227000.0, "trough_date_180": "2024-07-24", "peak_to_later_drawdown_pct": -40.58, "case_role": "risk_positive", "calibration_usable": true, "corporate_action_contaminated_180d": false, "evidence_family": "CHINA_GRAPHITE_EXPORT_CONTROL_ANODE_SUPPLY_CHAIN_POLICY_RISK", "evidence_url": "https://www.reuters.com/world/china/chinas-curbs-exports-strategic-minerals-2025-02-04/", "source_proxy_only": false, "evidence_url_pending": false}
{"row_type": "trigger", "round": "R4", "loop": 72, "large_sector_id": "L4_MATERIALS_SPREAD_RESOURCE", "canonical_archetype_id": "C16_STRATEGIC_RESOURCE_POLICY_SUPPLY", "fine_archetype_id": "GRAPHITE_CRITICAL_MINERAL_EXPORT_CONTROL_AND_SMELTER_SUPPLY_SQUEEZE_VS_PRICE_ONLY_RESOURCE_BETA", "case_id": "R4L72-C16-010130-KOREAZINC-ZINC-SMELTER-CHARGE-SUPPLY-SQUEEZE", "symbol": "010130", "company": "고려아연", "trigger_type": "Stage2-Actionable / LaterLocal4B", "trigger_date": "2024-04-09", "entry_date": "2024-04-11", "entry_price": 463000.0, "mfe_30_pct": 17.93, "mae_30_pct": -2.7, "mfe_90_pct": 20.3, "mae_90_pct": -3.89, "mfe_180_pct": 419.87, "mae_180_pct": -3.89, "peak_price_180": 2407000.0, "peak_date_180": "2024-12-06", "trough_price_180": 445000.0, "trough_date_180": "2024-08-05", "peak_to_later_drawdown_pct": -58.87, "case_role": "positive_with_later_4b_watch", "calibration_usable": true, "corporate_action_contaminated_180d": false, "evidence_family": "ZINC_MINE_SUPPLY_TIGHTNESS_SMELTER_TREATMENT_CHARGE_COLLAPSE", "evidence_url": "https://www.reuters.com/markets/commodities/smelter-charges-collapse-zinc-mine-supply-falters-2024-04-09/", "source_proxy_only": false, "evidence_url_pending": false}
```

### score simulation rows

```jsonl
{"row_type": "score_simulation", "case_id": "R4L72-C16-005490-POSCOHOLDINGS-CHINA-GRAPHITE-CONTROL-LITHIUM-BETA", "symbol": "005490", "baseline_current_proxy": "e2r_2_1_stock_web_calibrated", "raw_component_score_breakdown": {"eps_fcf_explosion": 4, "earnings_visibility": 5, "bottleneck_pricing_power": 8, "market_mispricing": 14, "valuation_rerating": 6, "capital_allocation": 2, "information_confidence": 4}, "diagnostic_flags": ["strategic_resource_policy_supply", "critical_mineral_or_smelter_supply", "generic_resource_policy_or_supplier_risk", "drawdown_watch"], "expected_current_profile_stage": "RiskWatch / local 4B-watch, not Green", "profile_stress_result": "C16 should not reward generic critical-mineral exposure unless the policy shock connects to company-level supply, pricing, offtake or margin evidence. POSCO Holdings had lithium/materials exposure, but the graphite-control headline did not create durable 180D rerating."}
{"row_type": "score_simulation", "case_id": "R4L72-C16-003670-POSCOFUTUREM-GRAPHITE-ANODE-SUPPLY-RISK", "symbol": "003670", "baseline_current_proxy": "e2r_2_1_stock_web_calibrated", "raw_component_score_breakdown": {"eps_fcf_explosion": 4, "earnings_visibility": 5, "bottleneck_pricing_power": 8, "market_mispricing": 14, "valuation_rerating": 6, "capital_allocation": 2, "information_confidence": 4}, "diagnostic_flags": ["strategic_resource_policy_supply", "critical_mineral_or_smelter_supply", "generic_resource_policy_or_supplier_risk", "local_4b_watch_after_peak_drawdown"], "expected_current_profile_stage": "RiskWatch / local 4B-watch, not Green", "profile_stress_result": "Battery-material suppliers should be more sensitive than diversified holding companies to graphite/anode supply policy shocks. The path had a tradable squeeze, but post-peak drawdown and later MAE argue for local 4B-watch rather than Green."}
{"row_type": "score_simulation", "case_id": "R4L72-C16-010130-KOREAZINC-ZINC-SMELTER-CHARGE-SUPPLY-SQUEEZE", "symbol": "010130", "baseline_current_proxy": "e2r_2_1_stock_web_calibrated", "raw_component_score_breakdown": {"eps_fcf_explosion": 13, "earnings_visibility": 12, "bottleneck_pricing_power": 17, "market_mispricing": 14, "valuation_rerating": 10, "capital_allocation": 2, "information_confidence": 4}, "diagnostic_flags": ["strategic_resource_policy_supply", "critical_mineral_or_smelter_supply", "company_level_supply_bridge_present", "local_4b_watch_after_peak_drawdown"], "expected_current_profile_stage": "Stage2-Actionable with later local 4B watch", "profile_stress_result": "C16 should reward strategic smelter supply squeeze only when physical concentrate/treatment-charge evidence exists. Korea Zinc had a clean commodity-supply bridge, but later governance/control-premium blowoff contaminated the same price path and requires local 4B-watch after peak."}
```

### aggregate row

```jsonl
{"row_type": "aggregate", "round": "R4", "loop": 72, "large_sector_id": "L4_MATERIALS_SPREAD_RESOURCE", "canonical_archetype_id": "C16_STRATEGIC_RESOURCE_POLICY_SUPPLY", "fine_archetype_id": "GRAPHITE_CRITICAL_MINERAL_EXPORT_CONTROL_AND_SMELTER_SUPPLY_SQUEEZE_VS_PRICE_ONLY_RESOURCE_BETA", "calibration_usable_case_count": 3, "calibration_usable_trigger_count": 3, "new_independent_case_count": 3, "reused_case_count": 0, "same_archetype_new_symbol_count": 3, "same_archetype_new_trigger_family_count": 3, "positive_case_count": 1, "counterexample_count": 1, "risk_positive_case_count": 1, "four_b_case_count": 2, "four_c_case_count": 0, "source_proxy_only_count": 0, "evidence_url_pending_count": 0, "current_profile_error_count": 2, "diversity_score_summary": "+3 C16 symbols, +2 critical-mineral policy/supply families, +1 smelter-supply positive, +1 resource-policy false positive, +1 supplier-chain local-4B risk, no hard duplicate", "residual_contribution_label": "canonical_archetype_rule_candidate"}
```

### shadow weight row

```jsonl
{"row_type": "shadow_weight", "round": "R4", "loop": 72, "large_sector_id": "L4_MATERIALS_SPREAD_RESOURCE", "canonical_archetype_id": "C16_STRATEGIC_RESOURCE_POLICY_SUPPLY", "axis": "graphite_critical_mineral_export_control_and_smelter_supply_squeeze_vs_price_only_resource_beta", "decision": "candidate_observe_more", "proposed_runtime_effect": "C16 should split generic critical-mineral policy headlines from company-level supply, pricing, concentrate, smelter-charge or offtake bridges. Strategic resource exposure without cashflow bridge should stay RiskWatch/local 4B, while physical supply squeeze with smelter economics can become Stage2-Actionable but needs later local 4B after governance or blowoff contamination.", "do_not_propose_new_weight_delta": false, "needs_more_evidence": true}
```

### residual contribution row

```jsonl
{"row_type": "residual_contribution", "round": "R4", "loop": 72, "large_sector_id": "L4_MATERIALS_SPREAD_RESOURCE", "canonical_archetype_id": "C16_STRATEGIC_RESOURCE_POLICY_SUPPLY", "existing_axis_strengthened": ["stage2_required_bridge", "price_only_blowoff_blocks_positive_stage", "local_4b_watch_guard"], "new_axis_proposed": null, "sector_specific_rule_candidate": true, "canonical_archetype_rule_candidate": true, "narrative_summary": "C16 needs to treat strategic-resource policy as a bridge test, not a theme label. Graphite export controls created supply-risk volatility but did not automatically rerate diversified resource names; supplier-chain names need local 4B-watch. Physical zinc concentrate/smelter charge evidence produced a real positive path, but later governance/price blowoff required a separate local 4B guard."}
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
005490:
  corporate_action_candidate_dates = none
  selected window = 2023-10-23~D+180
  contamination = false

003670:
  corporate_action_candidate_dates = 2015-05-04, 2021-02-03
  selected window = 2023-10-23~D+180
  contamination = false

010130:
  corporate_action_candidate_dates = none
  selected window = 2024-04-11~D+180
  contamination = false
```

---

## Deferred Coding Agent Handoff Prompt

Do not execute this now.

```text
You are the coding agent for Songdaiki/stock_agent.

Read this standalone v12 residual research MD and ingest machine-readable rows only after validation.

Do not patch production scoring blindly.

Candidate axis:
graphite_critical_mineral_export_control_and_smelter_supply_squeeze_vs_price_only_resource_beta

Required checks before implementation:
1. Validate all trigger rows against stock-web tradable_raw OHLC shards.
2. Confirm no hard duplicate key:
   canonical_archetype_id + symbol + trigger_type + entry_date.
3. Do not raise generic C16 resource-policy weight just because a headline mentions critical minerals.
4. Require company-level bridge:
   physical supply restriction,
   pricing/treatment-charge effect,
   offtake/customer linkage,
   smelter/refining economics,
   or margin conversion.
5. Use local 4B-watch when:
   strategic-resource headline produces MFE,
   but later drawdown exceeds roughly 35%,
   and company-level supply/margin evidence fails to refresh.
6. Separate governance/control-premium blowoff contamination from resource-supply Stage2.
7. Hard 4C still requires non-price thesis-break evidence.
8. Emit before/after diagnostics and reject if C16 becomes a generic commodity beta rule.
```

---

## Final round state

```text
completed_round = R4
completed_loop = 72
next_round = R5
next_loop = 72
round_schedule_status = valid
round_sector_consistency = pass
```

