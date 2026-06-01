# E2R Stock-Web v12 Residual Research — R11 Loop 71 / L10 / C31

## Metadata

```json
{
  "research_session": "post_calibrated_sector_archetype_residual_research",
  "mode": "historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12",
  "scheduled_round": "R11",
  "scheduled_loop": 71,
  "round_schedule_status": "valid",
  "round_sector_consistency": "pass",
  "completed_round": "R11",
  "completed_loop": 71,
  "computed_next_round": "R12",
  "computed_next_loop": 71,
  "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC",
  "canonical_archetype_id": "C31_POLICY_SUBSIDY_LEGISLATION_EVENT",
  "fine_archetype_id": "POLICY_EVENT_EXECUTION_BRIDGE_VS_PRICE_ONLY_THEME_BLOWOFF",
  "loop_objective": [
    "coverage_gap_fill",
    "counterexample_mining",
    "4B_non_price_requirement_stress_test",
    "sector_specific_rule_discovery",
    "canonical_archetype_compression",
    "residual_false_positive_mining"
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

This file is a standalone historical calibration / sector-archetype residual research Markdown artifact. It does not patch `stock_agent`, does not run live discovery, and does not propose immediate production scoring changes.

The execution used `Songdaiki/stock-web` as the sole price atlas with:

```text
price_source = Songdaiki/stock-web
price_basis = tradable_raw
price_adjustment_status = raw_unadjusted_marcap
stock_web_manifest_max_date = 2026-02-20
```

## Round / scope resolution

Previous completed state in this interactive run: R10 / loop 71.

Therefore:

```text
scheduled_round = R11
scheduled_loop = 71
allowed_large_sector = L10_POLICY_EVENT_CROSS_REDTEAM_MISC or L1 policy-defense linkage
selected_large_sector = L10_POLICY_EVENT_CROSS_REDTEAM_MISC
selected_canonical_archetype_id = C31_POLICY_SUBSIDY_LEGISLATION_EVENT
computed_next_round = R12
computed_next_loop = 71
```

R11 was not routed to L1 because this run is not a defense-policy framework case. It is a cross-policy event residual test: policy announcement, legislation, short-selling rule, tariff/project bridge, and price-only theme blowoff.

## No-Repeat / novelty check

No hard duplicate is intentionally reused.

Hard duplicate key checked conceptually:

```text
canonical_archetype_id + symbol + trigger_type + entry_date
```

Selected symbols are not among the high-repeat C31 top set in the No-Repeat index.

```text
C31 existing snapshot:
rows = 34
symbols = 14
good/bad Stage2 = 10/10
4B/4C = 1/0
top covered symbols = 112610, 034020, 336260, UNKNOWN_SYMBOL, 036460
```

This run adds:

```text
015760 / Korea Electric Power / named overseas nuclear project bridge
004090 / Korea Petroleum / East Sea oil-gas policy announcement price-only blowoff
247540 / EcoPro BM / market-wide short-selling ban policy squeeze
```

## Research thesis

C31 should not treat all policy events as one signal.

Policy headlines are like a match. Sometimes the match lights a furnace; sometimes it only burns paper.  
The separating mechanism is whether the policy event has a **cash-flow bridge**.

```text
Positive bridge:
named project / named contract route / tariff or budget mechanism / beneficiary operating leverage

Counterexample:
headline-only policy / market-structure squeeze / geological or legislative uncertainty / no beneficiary-level earnings bridge
```

The residual rule candidate is therefore:

```text
C31 generic policy-event score should stay capped unless the case has a named execution bridge.
If policy-event MFE is large but bridge evidence remains absent, route to local 4B watch rather than durable Stage2/Green.
```

---

## Case 1 — Positive bridge: 015760 / 한국전력 / Czech nuclear preferred bidder

### Evidence

Reuters reported that Korea Hydro & Nuclear Power, a subsidiary of KEPCO, was selected as the preferred bidder for two Czech nuclear reactors, with final contract negotiation still pending and completion targeted later. This is not merely a macro policy headline; it names the project, the bidder, and the parent utility route.

```text
evidence_family = CZECH_NUCLEAR_PREFERRED_BIDDER_POLICY_PROJECT_BRIDGE
case_role = positive
trigger_date = 2024-07-17
entry_date = 2024-07-18
entry_price = 20,050
```

### Stock-Web price path

Observed rows from `atlas/ohlcv_tradable_by_symbol_year/015/015760/2024.csv`:

```text
2024-07-18,20050,20400,19550,19610
2024-08-05,19600,19610,18190,18400
2024-11-26,23800,24600,23800,24400
```

### Backtest

```text
MFE_30D  = +14.46%
MAE_30D  = -9.28%
MFE_90D  = +22.69%
MAE_90D  = -9.28%
MFE_180D = +22.69%
MAE_180D = -9.28%
peak_180 = 24,600 on 2024-11-26
trough_180 = 18,190 on 2024-08-05
peak_to_later_drawdown = -26.06%
```

### Interpretation

This is the one case in this run where policy evidence can support Stage2-Actionable.  
However, it is not because “government supports nuclear” in the abstract. It is because the policy event has a project bridge: named overseas project, named preferred bidder, and identifiable parent utility route.

The current profile could underweight this if C31 is treated as generic policy headline risk. The positive rule is narrow:

```text
C31 positive scoring requires a named execution bridge.
```

---

## Case 2 — Counterexample: 004090 / 한국석유 / East Sea oil-gas announcement

### Evidence

Reuters reported that President Yoon approved exploratory drilling after citing the possibility of large oil and gas resources off South Korea's east coast. The same report emphasized that drilling was still exploratory and that reserves remained to be confirmed.

```text
evidence_family = EAST_SEA_OIL_GAS_EXPLORATION_POLICY_ANNOUNCEMENT_PRICE_ONLY
case_role = counterexample
trigger_date = 2024-06-03
entry_date = 2024-06-04
entry_price = 21,650
```

### Stock-Web price path

Observed rows from `atlas/ohlcv_tradable_by_symbol_year/004/004090/2024.csv`:

```text
2024-06-04,21650,23300,21500,23300
2024-06-05,23650,28100,21600,23300
2024-11-15,14350,14800,14350,14770
```

### Backtest

```text
MFE_30D  = +29.79%
MAE_30D  = -23.23%
MFE_90D  = +29.79%
MAE_90D  = -29.52%
MFE_180D = +29.79%
MAE_180D = -33.72%
peak_180 = 28,100 on 2024-06-05
trough_180 = 14,350 on 2024-11-15
peak_to_later_drawdown = -48.93%
```

### Interpretation

This is the classic policy-event trap.  
The MFE is real. The tradable spike is real. But the evidence is not yet a business bridge. It is an exploratory policy announcement with geological uncertainty and no confirmed cash-flow path for the listed proxy.

Current global rule should block durable positive Stage2/Green.  
The residual is more precise:

```text
Large policy-event MFE without execution bridge should create local 4B-watch quickly after blowoff,
not wait for a full non-price thesis break.
```

---

## Case 3 — Counterexample: 247540 / 에코프로비엠 / short-selling ban squeeze

### Evidence

Reuters reported that Korea's market-wide short-selling ban was imposed in November 2023 and later extended, with authorities citing illegal/naked short-selling detection and market fairness concerns. This is a market-structure policy event rather than a company-level earnings bridge.

```text
evidence_family = MARKET_WIDE_SHORT_SELLING_BAN_POLICY_SQUEEZE
case_role = counterexample
trigger_date = 2023-11-06
entry_date = 2023-11-06
entry_price = 270,500
```

### Stock-Web price path

Observed rows from `atlas/ohlcv_tradable_by_symbol_year/247/247540/2023.csv` and `2024.csv`:

```text
2023-11-06,270500,299000,260500,299000
2023-12-04,320000,354000,307500,323000
2024-06-28,178000,186000,175200,183000
```

### Backtest

```text
MFE_30D  = +30.87%
MAE_30D  = -16.82%
MFE_90D  = +30.87%
MAE_90D  = -21.07%
MFE_180D = +30.87%
MAE_180D = -35.23%
peak_180 = 354,000 on 2023-12-04
trough_180 = 175,200 on 2024-06-28
peak_to_later_drawdown = -50.51%
```

### Interpretation

The policy changed market mechanics, not company economics.  
This creates a very strong short-run MFE, but the later drawdown shows why C31 must separate **liquidity/policy squeeze** from **fundamental rerating**.

This is not a new positive weight candidate.  
It is a local 4B timing candidate:

```text
If policy squeeze MFE > +25% within 30D and no earnings/order/customer bridge appears,
downgrade to local 4B-watch even if full non-price 4B evidence is not yet available.
```

---

## Cross-case residual finding

### What repeated global rules already get right

```text
price_only_blowoff_blocks_positive_stage = useful
full_4b_requires_non_price_evidence = useful for full 4B
hard_4c_thesis_break_routes_to_4c = not directly tested here
```

### What remains unresolved

For C31, the remaining error is not whether policy events can move prices. They obviously can.

The unresolved issue is timing:

```text
Policy-event blowoffs often peak before a clean non-price thesis break appears.
Waiting for full 4B evidence can be too slow.
Generic positive Stage2 is too generous.
```

### Candidate canonical compression

Fine labels can compress into one C31 sub-rule:

```text
POLICY_EVENT_EXECUTION_BRIDGE_VS_PRICE_ONLY_THEME_BLOWOFF
```

This fine archetype covers:

```text
1. named project / contract / tariff bridge → Stage2-Actionable possible
2. market-structure squeeze → local 4B-watch, no positive Stage2
3. geological / subsidy / legislation headline without execution bridge → local 4B-watch, no positive Stage2
```

---

## Machine-readable rows

### trigger rows

```jsonl
{"row_type": "trigger", "round": "R11", "loop": 71, "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "C31_POLICY_SUBSIDY_LEGISLATION_EVENT", "fine_archetype_id": "POLICY_EVENT_EXECUTION_BRIDGE_VS_PRICE_ONLY_THEME_BLOWOFF", "case_id": "R11L71-C31-015760-CZECH-KHNP-PREFERRED-BIDDER-BRIDGE", "symbol": "015760", "company": "한국전력", "trigger_type": "Stage2-Actionable", "trigger_date": "2024-07-17", "entry_date": "2024-07-18", "entry_price": 20050.0, "mfe_30_pct": 14.46, "mae_30_pct": -9.28, "mfe_90_pct": 22.69, "mae_90_pct": -9.28, "mfe_180_pct": 22.69, "mae_180_pct": -9.28, "peak_price_180": 24600.0, "peak_date_180": "2024-11-26", "trough_price_180": 18190.0, "trough_date_180": "2024-08-05", "peak_to_later_drawdown_pct": -26.06, "case_role": "positive", "calibration_usable": true, "corporate_action_contaminated_180d": false, "evidence_family": "CZECH_NUCLEAR_PREFERRED_BIDDER_POLICY_PROJECT_BRIDGE", "evidence_url": "https://www.reuters.com/business/energy/south-koreas-winning-bid-czech-nuclear-power-project-2024-07-17/", "source_proxy_only": false, "evidence_url_pending": false}
{"row_type": "trigger", "round": "R11", "loop": 71, "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "C31_POLICY_SUBSIDY_LEGISLATION_EVENT", "fine_archetype_id": "POLICY_EVENT_EXECUTION_BRIDGE_VS_PRICE_ONLY_THEME_BLOWOFF", "case_id": "R11L71-C31-004090-EAST-SEA-OIL-GAS-ANNOUNCEMENT", "symbol": "004090", "company": "한국석유", "trigger_type": "Stage4B-Local-PriceOnly-PolicyTheme", "trigger_date": "2024-06-03", "entry_date": "2024-06-04", "entry_price": 21650.0, "mfe_30_pct": 29.79, "mae_30_pct": -23.23, "mfe_90_pct": 29.79, "mae_90_pct": -29.52, "mfe_180_pct": 29.79, "mae_180_pct": -33.72, "peak_price_180": 28100.0, "peak_date_180": "2024-06-05", "trough_price_180": 14350.0, "trough_date_180": "2024-11-15", "peak_to_later_drawdown_pct": -48.93, "case_role": "counterexample", "calibration_usable": true, "corporate_action_contaminated_180d": false, "evidence_family": "EAST_SEA_OIL_GAS_EXPLORATION_POLICY_ANNOUNCEMENT_PRICE_ONLY", "evidence_url": "https://www.reuters.com/world/asia-pacific/skoreas-yoon-says-vast-amount-oil-gas-reserve-possible-off-east-coast-2024-06-03/", "source_proxy_only": false, "evidence_url_pending": false}
{"row_type": "trigger", "round": "R11", "loop": 71, "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "C31_POLICY_SUBSIDY_LEGISLATION_EVENT", "fine_archetype_id": "POLICY_EVENT_EXECUTION_BRIDGE_VS_PRICE_ONLY_THEME_BLOWOFF", "case_id": "R11L71-C31-247540-SHORT-SELLING-BAN-SQUEEZE", "symbol": "247540", "company": "에코프로비엠", "trigger_type": "Stage4B-Local-PriceOnly-PolicySqueeze", "trigger_date": "2023-11-06", "entry_date": "2023-11-06", "entry_price": 270500.0, "mfe_30_pct": 30.87, "mae_30_pct": -16.82, "mfe_90_pct": 30.87, "mae_90_pct": -21.07, "mfe_180_pct": 30.87, "mae_180_pct": -35.23, "peak_price_180": 354000.0, "peak_date_180": "2023-12-04", "trough_price_180": 175200.0, "trough_date_180": "2024-06-28", "peak_to_later_drawdown_pct": -50.51, "case_role": "counterexample", "calibration_usable": true, "corporate_action_contaminated_180d": false, "evidence_family": "MARKET_WIDE_SHORT_SELLING_BAN_POLICY_SQUEEZE", "evidence_url": "https://www.reuters.com/world/asia-pacific/south-korea-extend-short-selling-ban-now-2024-06-13/", "source_proxy_only": false, "evidence_url_pending": false}
```

### score simulation rows

```jsonl
{"row_type": "score_simulation", "case_id": "R11L71-C31-015760-CZECH-KHNP-PREFERRED-BIDDER-BRIDGE", "symbol": "015760", "baseline_current_proxy": "e2r_2_1_stock_web_calibrated", "raw_component_score_breakdown": {"eps_fcf_explosion": 10, "earnings_visibility": 13, "bottleneck_pricing_power": 11, "market_mispricing": 12, "valuation_rerating": 11, "capital_allocation": 3, "information_confidence": 4}, "diagnostic_flags": ["policy_event", "named_project_execution_bridge", "non_price_bridge_present"], "expected_current_profile_stage": "Stage2-Actionable", "profile_stress_result": "policy event becomes actionable only because it has a named preferred bidder, named KEPCO subsidiary KHNP, and project/contract bridge; generic policy headline alone should remain capped"}
{"row_type": "score_simulation", "case_id": "R11L71-C31-004090-EAST-SEA-OIL-GAS-ANNOUNCEMENT", "symbol": "004090", "baseline_current_proxy": "e2r_2_1_stock_web_calibrated", "raw_component_score_breakdown": {"eps_fcf_explosion": 6, "earnings_visibility": 7, "bottleneck_pricing_power": 5, "market_mispricing": 14, "valuation_rerating": 9, "capital_allocation": 2, "information_confidence": 2}, "diagnostic_flags": ["policy_event", "price_only_blowoff", "non_price_bridge_absent_or_unconfirmed"], "expected_current_profile_stage": "Stage4B-local-watch / no positive Stage2", "profile_stress_result": "policy announcement with uncertain resource confirmation can create explosive MFE but should not be treated as durable Stage2/Green; local 4B watch should fire after blowoff without waiting for full thesis-break evidence"}
{"row_type": "score_simulation", "case_id": "R11L71-C31-247540-SHORT-SELLING-BAN-SQUEEZE", "symbol": "247540", "baseline_current_proxy": "e2r_2_1_stock_web_calibrated", "raw_component_score_breakdown": {"eps_fcf_explosion": 6, "earnings_visibility": 7, "bottleneck_pricing_power": 5, "market_mispricing": 14, "valuation_rerating": 9, "capital_allocation": 2, "information_confidence": 2}, "diagnostic_flags": ["policy_event", "price_only_blowoff", "non_price_bridge_absent_or_unconfirmed"], "expected_current_profile_stage": "Stage4B-local-watch / no positive Stage2", "profile_stress_result": "market-structure policy can create squeeze MFE, but without earnings/order/customer bridge it should stay outside durable positive Stage2; the residual is a need for local blowoff timing, not a new positive weight"}
```

### aggregate row

```jsonl
{"row_type": "aggregate", "round": "R11", "loop": 71, "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "C31_POLICY_SUBSIDY_LEGISLATION_EVENT", "fine_archetype_id": "POLICY_EVENT_EXECUTION_BRIDGE_VS_PRICE_ONLY_THEME_BLOWOFF", "calibration_usable_case_count": 3, "calibration_usable_trigger_count": 3, "new_independent_case_count": 3, "reused_case_count": 0, "same_archetype_new_symbol_count": 3, "same_archetype_new_trigger_family_count": 3, "positive_case_count": 1, "counterexample_count": 2, "four_b_case_count": 2, "four_c_case_count": 0, "current_profile_error_count": 2, "diversity_score_summary": "+3 new symbols, +3 trigger families, +2 policy-price-only 4B local guards, +1 named-project bridge positive, no hard duplicate", "residual_contribution_label": "canonical_archetype_rule_candidate"}
```

### shadow weight row

```jsonl
{"row_type": "shadow_weight", "round": "R11", "loop": 71, "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "C31_POLICY_SUBSIDY_LEGISLATION_EVENT", "axis": "policy_event_execution_bridge_vs_price_only_blowoff", "decision": "candidate_observe_more", "proposed_runtime_effect": "Do not raise generic C31 policy-event score. Add/strengthen local 4B-watch when policy-event MFE is unsupported by named budget/order/tariff/project bridge; allow Stage2 only when policy has explicit cashflow or project execution bridge.", "do_not_propose_new_weight_delta": false, "needs_more_evidence": true}
```

### residual contribution row

```jsonl
{"row_type": "residual_contribution", "round": "R11", "loop": 71, "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "C31_POLICY_SUBSIDY_LEGISLATION_EVENT", "existing_axis_strengthened": ["price_only_blowoff_blocks_positive_stage", "full_4b_requires_non_price_evidence"], "new_axis_proposed": null, "sector_specific_rule_candidate": true, "canonical_archetype_rule_candidate": true, "narrative_summary": "C31 policy-event evidence bifurcates into (1) named-project/tariff/cashflow bridge cases that can become Stage2-Actionable and (2) price-only policy-squeeze/geology-announcement cases that produce high MFE but require local 4B watch rather than durable Green treatment."}
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
selected_windows_corporate_action_contaminated = false
production_scoring_changed = false
shadow_weight_only = true
```

Profile checks:

```text
015760: corporate_action_candidate_count = 0 → 180D window usable
004090: corporate action candidates = 1997-08-07, 2021-04-15, 2021-05-07 → 2024 window usable
247540: corporate action candidates = 2022-06-27, 2022-07-15 → 2023-11~2024-06 window usable
```

---

## Deferred Coding Agent Handoff Prompt

Do not execute this now.

```text
You are the coding agent for Songdaiki/stock_agent.

Read this standalone v12 residual research MD and ingest only machine-readable rows.

Do not patch production scoring blindly.
Use the rows to evaluate whether C31_POLICY_SUBSIDY_LEGISLATION_EVENT needs a scoped local-4B watch guard:

candidate_axis = policy_event_execution_bridge_vs_price_only_blowoff

Required checks before implementation:
1. Validate all trigger rows against stock-web tradable_raw OHLC shards.
2. Confirm no hard duplicate key:
   canonical_archetype_id + symbol + trigger_type + entry_date.
3. Keep generic C31 positive weight unchanged unless more named-execution-bridge positives appear.
4. Consider adding a C31 local-4B-watch diagnostic:
   if policy_event_mfe_30d >= 25%
   and no named execution bridge is present
   and no EPS/order/customer/tariff cash-flow bridge is present
   then label Stage4B-local-watch, not Stage2/Green.
5. Do not apply full 4B unless existing non-price 4B evidence rule is satisfied.
6. Emit before/after diagnostics and reject if cross-sector false positives increase.
```

---

## Final round state

```text
completed_round = R11
completed_loop = 71
next_round = R12
next_loop = 71
round_schedule_status = valid
round_sector_consistency = pass
```

