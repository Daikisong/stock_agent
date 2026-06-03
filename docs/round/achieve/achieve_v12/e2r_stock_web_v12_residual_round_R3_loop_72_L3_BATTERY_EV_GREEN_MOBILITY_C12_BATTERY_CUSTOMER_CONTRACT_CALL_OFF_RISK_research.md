# E2R Stock-Web v12 Residual Research — R3 Loop 72 / L3 / C12

## Metadata

```json
{
  "research_session": "post_calibrated_sector_archetype_residual_research",
  "mode": "historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12",
  "scheduled_round": "R3",
  "scheduled_loop": 72,
  "round_schedule_status": "valid",
  "round_sector_consistency": "pass",
  "completed_round": "R3",
  "completed_loop": 72,
  "computed_next_round": "R4",
  "computed_next_loop": 72,
  "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY",
  "canonical_archetype_id": "C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK",
  "fine_archetype_id": "OEM_EV_DEMAND_SLOWDOWN_CAPEX_CUT_CUSTOMER_CONTRACT_RISK_VS_AMPC_BASE_SUPPORT",
  "loop_objective": [
    "coverage_gap_fill",
    "counterexample_mining",
    "4B_non_price_requirement_stress_test",
    "sector_specific_rule_discovery",
    "canonical_archetype_compression",
    "risk_positive_vs_overbearish_false_positive_balance"
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

Previous completed state in this interactive run: R2 / loop 72.

Therefore:

```text
scheduled_round = R3
scheduled_loop = 72
allowed_large_sector = L3_BATTERY_EV_GREEN_MOBILITY
selected_large_sector = L3_BATTERY_EV_GREEN_MOBILITY
selected_canonical_archetype_id = C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK
computed_next_round = R4
computed_next_loop = 72
```

R3 was routed to C12 because C11/C13/C14 already contain many repeated LGES/SDI/EcoPro/POSCO-style battery cycle rows, while C12 still benefits from cleaner separation between:

```text
cell-maker customer/capex risk
material-supplier customer call-off risk
overbearish slow-demand headlines that should not become full 4B/4C
```

## No-Repeat / novelty check

No hard duplicate is intentionally reused.

Hard duplicate key checked conceptually:

```text
canonical_archetype_id + symbol + trigger_type + entry_date
```

Selected rows:

```text
373220 / LG에너지솔루션 / Stage2-RiskWatch / NotFull4B / 2024-04-25
006400 / 삼성SDI / Stage4B-Local-CustomerDemandRisk / 2024-06-28
003670 / 포스코퓨처엠 / Stage4B-Local-CathodeCustomerCallOffRisk / 2024-04-25
```

Data-quality note:

```text
003670 is stock-web calibration-usable but source_proxy_only=true / evidence_url_pending=true.
It should be treated as source-repair candidate before runtime promotion.
```

## Research thesis

C12 is not just “EV demand slowed.”

The correct mechanism is:

```text
OEM EV demand slowdown
→ cell-maker capex / customer order pacing changes
→ cathode/material supplier shipment and price pressure
→ MAE and drawdown widening
```

But the risk does not strike the whole chain equally.  
A cell maker with AMPC support and a wider customer base may survive as RiskWatch.  
An upstream material supplier has less cushion: if the customer taps the brake, the supplier feels the seatbelt first.

The residual split is:

```text
C12 RiskWatch:
  slow EV demand confirmed, but AMPC/customer base/contract mix buffers the equity path

C12 local 4B:
  customer demand cuts, capex delays, weak sales target, or material demand pressure
  plus large MAE or post-peak drawdown

C12 full 4B/4C:
  explicit contract cancellation, take-or-pay failure, confirmed order reduction,
  or customer-specific thesis break
```

---

## Case 1 — Overbearish counterexample: 373220 / LG에너지솔루션

### Evidence

Reuters reported on 2024-04-25 that LG Energy Solution planned to minimize capital expenditure due to slowing global EV demand after Q1 profit plunged. The same report noted customer exposure to Tesla, General Motors and Volkswagen, and that IRA tax credits were a major support factor.

```text
evidence_family = CUSTOMER_EV_DEMAND_SLOWDOWN_CAPEX_MINIMIZATION_WITH_AMPC_SUPPORT
case_role = overbearish_counterexample
trigger_date = 2024-04-25
entry_date = 2024-04-25
entry_price = 380,000
```

### Stock-Web price path

Observed rows from `atlas/ohlcv_tradable_by_symbol_year/373/373220/2024.csv`:

```text
2024-04-25,380000,381000,372000,372500
2024-07-25,315000,342500,313000,332500
2024-10-08,416500,444000,412000,436500
```

### Backtest

```text
MFE_30D  = +4.47%
MAE_30D  = -14.21%
MFE_90D  = +10.26%
MAE_90D  = -17.63%
MFE_180D = +16.84%
MAE_180D = -17.63%
peak_180 = 444,000 on 2024-10-08
trough_180 = 313,000 on 2024-07-25
peak_to_later_drawdown = -22.86%
```

### Interpretation

This is not a bullish row.  
It is a guardrail against over-bearish classification.

The slow EV-demand signal was real, but the stock did not confirm a full 4B/4C collapse. C12 should flag RiskWatch, but not automatically escalate a top-tier cell maker to hard deterioration when AMPC and customer-base support remain present.

---

## Case 2 — Risk-positive: 006400 / 삼성SDI

### Evidence

MarketWatch/WSJ Market Talk reported that analysts expected Samsung SDI's 2024 earnings to take a hit from sluggish EV battery demand, including likely weakness in cylindrical-battery shipments because U.S. customer Rivian had a conservative sales target. A separate Market Talk item noted European EV-demand softness and Samsung SDI's heavy exposure to European automaker clients.

```text
evidence_family = RIVIAN_EUROPE_CUSTOMER_SALES_TARGET_DOWN_REVENUE_CONCENTRATION_RISK
case_role = risk_positive
trigger_date = 2024-06-28
entry_date = 2024-06-28
entry_price = 359,000
```

### Stock-Web price path

Observed rows from `atlas/ohlcv_tradable_by_symbol_year/006/006400/2024.csv` and `2025.csv`:

```text
2024-06-28,359000,362500,351000,354000
2024-07-05,387500,390000,378500,382000
2025-03-14,199500,209500,189300,191400
```

### Backtest

```text
MFE_30D  = +8.64%
MAE_30D  = -17.97%
MFE_90D  = +8.64%
MAE_90D  = -17.97%
MFE_180D = +8.64%
MAE_180D = -47.27%
peak_180 = 390,000 on 2024-07-05
trough_180 = 189,300 on 2025-03-14
peak_to_later_drawdown = -51.46%
```

### Interpretation

This is the clean local 4B-watch row.

The early MFE was not enough to offset the customer-demand risk. The later MAE opened too widely. C12 should not need a full contract cancellation to mark this as local 4B risk, but it should still require stronger non-price evidence before calling it full 4B or 4C.

---

## Case 3 — Risk-positive with source repair: 003670 / 포스코퓨처엠

### Evidence status

```text
source_proxy_only = true
evidence_url_pending = true
source_repair_required = true
```

This row is included because the stock-web path is a clear cathode-material customer/capex risk path.  
The source-repair task is to attach company-level non-proxy evidence for cathode shipment/order risk, while the sector-level background comes from weak EV demand, LGES capex minimization, and battery-metal price weakness.

```text
evidence_family = CATHODE_MATERIAL_CUSTOMER_CAPEX_CUT_PRICE_AND_ORDER_RISK
case_role = risk_positive
trigger_date = 2024-04-25
entry_date = 2024-04-25
entry_price = 290,000
```

### Stock-Web price path

Observed rows from `atlas/ohlcv_tradable_by_symbol_year/003/003670/2024.csv`:

```text
2024-04-25,290000,296500,279500,280500
2024-08-05,224000,231500,195500,203000
2024-12-27,141200,146200,139500,142400
```

### Backtest

```text
MFE_30D  = +2.24%
MAE_30D  = -13.79%
MFE_90D  = +2.24%
MAE_90D  = -32.59%
MFE_180D = +2.24%
MAE_180D = -51.90%
peak_180 = 296,500 on 2024-04-25
trough_180 = 139,500 on 2024-12-27
peak_to_later_drawdown = -52.95%
```

### Interpretation

This is the sharper supplier-chain version of C12.  
The cell-maker row, LGES, stayed in RiskWatch. The cathode/material supplier row opened a much wider MAE and drawdown.

The rule should therefore distinguish:

```text
cell maker with AMPC / customer base support = RiskWatch unless non-price deterioration confirms
material supplier exposed to capex/order slowdown = stronger local 4B-watch
```

---

## Cross-case residual finding

### What this strengthens

```text
stage2_required_bridge = strengthen
local_4b_watch_guard = strengthen
hard_4c_confirmation = strengthen
```

### What this does not justify

```text
do_not_convert_all_slow_EV_demand_to_4C = true
do_not_treat_AMPC_supported_cell_maker_risk_as_automatic_full_4B = true
do_not_treat_material_supplier_drawdown_as_full_4B_without_order evidence = true
```

### Candidate canonical compression

Fine labels can compress into:

```text
OEM_EV_DEMAND_SLOWDOWN_CAPEX_CUT_CUSTOMER_CONTRACT_RISK_VS_AMPC_BASE_SUPPORT
```

This fine archetype covers:

```text
1. cell-maker slow-demand warning + AMPC/customer base support → RiskWatch / no full 4B
2. customer-concentrated battery maker demand risk → local 4B-watch
3. cathode/material supplier customer capex risk → stronger local 4B-watch, source repair required
```

---

## Machine-readable rows

### trigger rows

```jsonl
{"row_type": "trigger", "round": "R3", "loop": 72, "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK", "fine_archetype_id": "OEM_EV_DEMAND_SLOWDOWN_CAPEX_CUT_CUSTOMER_CONTRACT_RISK_VS_AMPC_BASE_SUPPORT", "case_id": "R3L72-C12-373220-LGES-Q1-SLOW-EV-DEMAND-CAPEX-CUT-NOT-4C", "symbol": "373220", "company": "LG에너지솔루션", "trigger_type": "Stage2-RiskWatch / NotFull4B", "trigger_date": "2024-04-25", "entry_date": "2024-04-25", "entry_price": 380000.0, "mfe_30_pct": 4.47, "mae_30_pct": -14.21, "mfe_90_pct": 10.26, "mae_90_pct": -17.63, "mfe_180_pct": 16.84, "mae_180_pct": -17.63, "peak_price_180": 444000.0, "peak_date_180": "2024-10-08", "trough_price_180": 313000.0, "trough_date_180": "2024-07-25", "peak_to_later_drawdown_pct": -22.86, "case_role": "overbearish_counterexample", "calibration_usable": true, "corporate_action_contaminated_180d": false, "evidence_family": "CUSTOMER_EV_DEMAND_SLOWDOWN_CAPEX_MINIMIZATION_WITH_AMPC_SUPPORT", "evidence_url": "https://www.reuters.com/technology/battery-firm-lg-energy-solution-q1-profit-plunges-weak-ev-sales-2024-04-25/", "source_proxy_only": false, "evidence_url_pending": false}
{"row_type": "trigger", "round": "R3", "loop": 72, "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK", "fine_archetype_id": "OEM_EV_DEMAND_SLOWDOWN_CAPEX_CUT_CUSTOMER_CONTRACT_RISK_VS_AMPC_BASE_SUPPORT", "case_id": "R3L72-C12-006400-SAMSUNGSDI-RIVIAN-EUROPE-SLOW-EV-DEMAND", "symbol": "006400", "company": "삼성SDI", "trigger_type": "Stage4B-Local-CustomerDemandRisk", "trigger_date": "2024-06-28", "entry_date": "2024-06-28", "entry_price": 359000.0, "mfe_30_pct": 8.64, "mae_30_pct": -17.97, "mfe_90_pct": 8.64, "mae_90_pct": -17.97, "mfe_180_pct": 8.64, "mae_180_pct": -47.27, "peak_price_180": 390000.0, "peak_date_180": "2024-07-05", "trough_price_180": 189300.0, "trough_date_180": "2025-03-14", "peak_to_later_drawdown_pct": -51.46, "case_role": "risk_positive", "calibration_usable": true, "corporate_action_contaminated_180d": false, "evidence_family": "RIVIAN_EUROPE_CUSTOMER_SALES_TARGET_DOWN_REVENUE_CONCENTRATION_RISK", "evidence_url": "https://www.marketwatch.com/story/samsung-sdi-s-2024-earnings-could-take-a-hit-from-sluggish-ev-battery-demand-market-talk-ceab3dde", "source_proxy_only": false, "evidence_url_pending": false}
{"row_type": "trigger", "round": "R3", "loop": 72, "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK", "fine_archetype_id": "OEM_EV_DEMAND_SLOWDOWN_CAPEX_CUT_CUSTOMER_CONTRACT_RISK_VS_AMPC_BASE_SUPPORT", "case_id": "R3L72-C12-003670-POSCOFUTUREM-CATHODE-CUSTOMER-CAPEX-CUT-RISK", "symbol": "003670", "company": "포스코퓨처엠", "trigger_type": "Stage4B-Local-CathodeCustomerCallOffRisk", "trigger_date": "2024-04-25", "entry_date": "2024-04-25", "entry_price": 290000.0, "mfe_30_pct": 2.24, "mae_30_pct": -13.79, "mfe_90_pct": 2.24, "mae_90_pct": -32.59, "mfe_180_pct": 2.24, "mae_180_pct": -51.9, "peak_price_180": 296500.0, "peak_date_180": "2024-04-25", "trough_price_180": 139500.0, "trough_date_180": "2024-12-27", "peak_to_later_drawdown_pct": -52.95, "case_role": "risk_positive", "calibration_usable": true, "corporate_action_contaminated_180d": false, "evidence_family": "CATHODE_MATERIAL_CUSTOMER_CAPEX_CUT_PRICE_AND_ORDER_RISK", "evidence_url": "source_proxy_manual_verification_required:POSCO_FUTURE_M_CATHODE_CUSTOMER_CAPEX_CUT_AND_BATTERY_METALS_WEAKNESS_2024", "source_proxy_only": true, "evidence_url_pending": true}
```

### score simulation rows

```jsonl
{"row_type": "score_simulation", "case_id": "R3L72-C12-373220-LGES-Q1-SLOW-EV-DEMAND-CAPEX-CUT-NOT-4C", "symbol": "373220", "baseline_current_proxy": "e2r_2_1_stock_web_calibrated", "raw_component_score_breakdown": {"eps_fcf_explosion": 4, "earnings_visibility": 6, "bottleneck_pricing_power": 4, "market_mispricing": 10, "valuation_rerating": 8, "capital_allocation": 2, "information_confidence": 4}, "diagnostic_flags": ["battery_customer_contract_call_off_risk", "slow_ev_demand", "capex_or_customer_order_risk", "overbearish_counterexample", "verified_external_evidence"], "expected_current_profile_stage": "Stage2-RiskWatch / no full 4B", "profile_stress_result": "C12 should flag customer demand/capex risk, but not auto-upgrade to full 4B/4C when AMPC support and customer mix keep the equity path from collapsing."}
{"row_type": "score_simulation", "case_id": "R3L72-C12-006400-SAMSUNGSDI-RIVIAN-EUROPE-SLOW-EV-DEMAND", "symbol": "006400", "baseline_current_proxy": "e2r_2_1_stock_web_calibrated", "raw_component_score_breakdown": {"eps_fcf_explosion": 2, "earnings_visibility": 3, "bottleneck_pricing_power": 2, "market_mispricing": 12, "valuation_rerating": 6, "capital_allocation": 2, "information_confidence": 4}, "diagnostic_flags": ["battery_customer_contract_call_off_risk", "slow_ev_demand", "capex_or_customer_order_risk", "risk_positive", "verified_external_evidence"], "expected_current_profile_stage": "Stage4B-local-watch", "profile_stress_result": "C12 should fire local 4B-watch when a battery maker has high exposure to weak EV customers/regions and the stock path opens large 180D MAE; however full 4B still needs non-price deterioration."}
{"row_type": "score_simulation", "case_id": "R3L72-C12-003670-POSCOFUTUREM-CATHODE-CUSTOMER-CAPEX-CUT-RISK", "symbol": "003670", "baseline_current_proxy": "e2r_2_1_stock_web_calibrated", "raw_component_score_breakdown": {"eps_fcf_explosion": 2, "earnings_visibility": 3, "bottleneck_pricing_power": 2, "market_mispricing": 12, "valuation_rerating": 6, "capital_allocation": 2, "information_confidence": 2}, "diagnostic_flags": ["battery_customer_contract_call_off_risk", "slow_ev_demand", "capex_or_customer_order_risk", "risk_positive", "source_proxy_only"], "expected_current_profile_stage": "Stage4B-local-watch", "profile_stress_result": "Cathode material makers need stronger customer-order bridge protection than cell makers. When the upstream customer cuts capex and battery metal prices weaken, C12 should treat the material supplier as a sharper local 4B risk."}
```

### aggregate row

```jsonl
{"row_type": "aggregate", "round": "R3", "loop": 72, "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK", "fine_archetype_id": "OEM_EV_DEMAND_SLOWDOWN_CAPEX_CUT_CUSTOMER_CONTRACT_RISK_VS_AMPC_BASE_SUPPORT", "calibration_usable_case_count": 3, "calibration_usable_trigger_count": 3, "new_independent_case_count": 3, "reused_case_count": 0, "same_archetype_new_symbol_count": 3, "same_archetype_new_trigger_family_count": 3, "risk_positive_case_count": 2, "overbearish_counterexample_count": 1, "four_b_case_count": 2, "four_c_case_count": 0, "source_proxy_only_count": 1, "evidence_url_pending_count": 1, "current_profile_error_count": 2, "diversity_score_summary": "+3 symbols in C12, +3 customer-demand/capex risk trigger families, +2 local-4B risk positives, +1 overbearish no-full-4B counterexample, no hard duplicate", "residual_contribution_label": "canonical_archetype_rule_candidate"}
```

### shadow weight row

```jsonl
{"row_type": "shadow_weight", "round": "R3", "loop": 72, "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK", "axis": "oem_ev_demand_slowdown_capex_cut_customer_contract_risk_vs_ampc_base_support", "decision": "candidate_observe_more", "proposed_runtime_effect": "C12 should split cell-maker demand risk with AMPC/customer-base support from upstream cathode/material supplier call-off risk. Local 4B-watch should be stronger for supplier chains when customer capex cuts and material price weakness open large MAE; full 4B/4C still requires non-price contract/order deterioration.", "do_not_propose_new_weight_delta": false, "needs_more_evidence": true, "source_repair_required": ["003670"]}
```

### residual contribution row

```jsonl
{"row_type": "residual_contribution", "round": "R3", "loop": 72, "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK", "existing_axis_strengthened": ["stage2_required_bridge", "local_4b_watch_guard", "hard_4c_confirmation"], "new_axis_proposed": null, "sector_specific_rule_candidate": true, "canonical_archetype_rule_candidate": true, "narrative_summary": "C12 should not simply punish all slow-EV-demand headlines. It needs a supplier-chain split: cell makers with AMPC/customer-base support can remain RiskWatch, while cathode/material suppliers and customer-concentrated battery makers with order/capex exposure should move to local 4B-watch when MAE and post-peak drawdown confirm the risk."}
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
373220:
  corporate_action_candidate_dates = none
  selected window = 2024-04-25~D+180
  contamination = false

006400:
  corporate_action_candidate_dates = 1996-01-03, 1998-11-03, 2014-07-15
  selected window = 2024-06-28~D+180
  contamination = false

003670:
  corporate_action_candidate_dates = 2015-05-04, 2021-02-03
  selected window = 2024-04-25~D+180
  contamination = false
```

Data-quality caveat:

```text
003670 source URL is proxy/pending.
It should be treated as source-repair candidate before coding-agent promotion.
```

---

## Deferred Coding Agent Handoff Prompt

Do not execute this now.

```text
You are the coding agent for Songdaiki/stock_agent.

Read this standalone v12 residual research MD and ingest machine-readable rows only after validation.

Do not patch production scoring blindly.

Candidate axis:
oem_ev_demand_slowdown_capex_cut_customer_contract_risk_vs_ampc_base_support

Required checks before implementation:
1. Validate all trigger rows against stock-web tradable_raw OHLC shards.
2. Confirm no hard duplicate key:
   canonical_archetype_id + symbol + trigger_type + entry_date.
3. Verify non-proxy source URL for 003670.
4. Do not auto-convert all slow-EV-demand headlines into full 4B/4C.
5. Consider C12 RiskWatch if:
   - slow EV demand or capex cut is confirmed,
   - but AMPC/customer-base support remains,
   - MAE_180D is not severe and no explicit order cancellation exists.
6. Consider local 4B-watch if:
   - customer concentration, regional EV slowdown, or downbeat customer sales target is present,
   - MAE_180D <= -25% or peak_to_later_drawdown <= -35%,
   - order/capex bridge is weak or deteriorating.
7. Consider stronger supplier-chain local 4B when:
   - upstream cathode/material supplier depends on cell-maker/OEM capex,
   - battery metals or shipment visibility deteriorates,
   - stock-web MAE opens materially wider than the cell-maker anchor.
8. Full 4B/4C still requires non-price contract/order cancellation, take-or-pay failure, or explicit customer thesis break.
9. Emit before/after diagnostics and reject if C12 overblocks AMPC-supported cell-maker cases.
```

---

## Final round state

```text
completed_round = R3
completed_loop = 72
next_round = R4
next_loop = 72
round_schedule_status = valid
round_sector_consistency = pass
```

