# E2R Stock-Web v12 Residual Research — R3 Loop 72

```yaml
research_session: post_calibrated_sector_archetype_residual_research
mode: historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12
completed_round: R3
completed_loop: 72
next_round: R4
next_loop: 72
large_sector_id: L3_BATTERY_EV_GREEN_MOBILITY
canonical_archetype_id: C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK
fine_archetype_id: BATTERY_EQUIPMENT_MATERIAL_CUSTOMER_CALLOFF_HIGH_MAE
output_file: e2r_stock_web_v12_residual_round_R3_loop_72_L3_BATTERY_EV_GREEN_MOBILITY_C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK_research.md
production_scoring_changed: false
shadow_weight_only: true
handoff_prompt_embedded: true
handoff_prompt_executed_now: false
```

## 0. Execution gate

This file follows the v12 historical calibration prompt as the execution procedure.  
`V12_Research_No_Repeat_Index.md` is used only as the duplicate-avoidance ledger.

This is not a live stock discovery run, not investment advice, not a trading instruction, and not a `stock_agent` code patch.  
The only output is a standalone historical calibration / sector-archetype residual Markdown artifact.

### Round resolution

The immediately preceding artifact in this automation chain was:

```text
completed_round = R2
completed_loop  = 72
large_sector_id = L2_AI_SEMICONDUCTOR_ELECTRONICS
canonical_archetype_id = C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE
```

Therefore:

```text
scheduled_round = R3
scheduled_loop  = 72
```

R3 maps to:

```text
large_sector_id = L3_BATTERY_EV_GREEN_MOBILITY
```

This run selects:

```text
canonical_archetype_id = C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK
```

This is a valid R3/L3 pairing.

---

## 1. Why this R3/C12 run

The no-repeat ledger shows C12 is already moderately covered, but the dominant set is concentrated in larger battery-cell/material names:

```text
C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK:
  rows: 53
  symbols: 17
  date range: 2023-01-26~2024-07-25
  good/bad S2: 13/2
  4B/4C: 10/5
  top covered symbols: 393890(9), 361610(7), 011790(5), 336370(5), 006110(4), UNKNOWN_SYMBOL(4)
```

This run adds three less-repeated R3/C12 symbols from battery equipment/material adjacency:

```text
137400 피엔티
121600 나노신소재
382840 원준
```

The research question is:

```text
Can C12 separate orderbook-resilient battery equipment cases from customer-calloff / EV-slowdown cases whose apparent Stage2 setup turns into high-MAE or failed follow-through?
```

---

## 2. Price atlas validation

### Stock-Web manifest snapshot

```json
{
  "price_atlas_repo": "Songdaiki/stock-web",
  "source_name": "FinanceData/marcap",
  "price_adjustment_status": "raw_unadjusted_marcap",
  "min_date": "1995-05-02",
  "max_date": "2026-02-20",
  "tradable_row_count": 14354401,
  "raw_row_count": 15214118,
  "symbol_count": 5414,
  "active_like_symbol_count": 2868,
  "inactive_or_delisted_like_symbol_count": 2546,
  "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year",
  "raw_shard_root": "atlas/ohlcv_raw_by_symbol_year",
  "schema_path": "atlas/schema.json",
  "research_pack_default_price_basis": "tradable_raw"
}
```

All price rows below use:

```text
price_source = Songdaiki/stock-web
upstream_source = FinanceData/marcap
price_basis = tradable_raw
price_adjustment_status = raw_unadjusted_marcap
```

### Candidate profile checks

| symbol | name | market | profile status | corporate-action candidate overlap with selected 180D window | calibration usable |
|---|---|---|---|---|---|
| `137400` | 피엔티 | KOSDAQ GLOBAL | active_like | none in 2024 test window; old 2012/2019 candidates only | true |
| `121600` | 나노신소재 | KOSDAQ | active_like | none in 2024 test window; old 2015 candidate only | true |
| `382840` | 원준 | KOSDAQ | active_like | none in 2024 test window; old 2022 candidates only | true |

Profile caveat:

```text
Stock-Web OHLC is raw/unadjusted marcap data. These cases are calibration-safe for the selected 2024 windows because no listed corporate-action candidate overlaps each entry~D+180 test window.
```

---

## 3. Evidence status and trigger discipline

This run intentionally treats non-price evidence as `source_proxy_only = true` and `evidence_url_pending = true`.

Reason:

```text
The price path is fully validated with Stock-Web OHLC rows, but the customer-level orderbook/call-off details require later URL-level repair through DART, company IR, report, or disclosure evidence before any production weight promotion.
```

This keeps the artifact useful but conservative:

```text
price_path_calibration_usable = true
positive_weight_promotion_allowed_now = false
reason = source_proxy_only_non_price_evidence
```

C12 interpretation used here:

```text
C12 is not just “battery stock fell.”
It tests whether the model can distinguish:
1. equipment/orderbook cases that still have enough non-price resilience to remain Stage2-Actionable guarded,
2. material/equipment cases whose customer-demand or EV-slowdown exposure turns a Stage2-looking setup into high-MAE or 4B/4C watch.
```

---

## 4. No-repeat and novelty check

Hard duplicate key:

```text
canonical_archetype_id + symbol + trigger_type + entry_date
```

Searches performed before writing:

```text
137400 + C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK -> no direct match found
121600 + C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK -> no direct match found
382840 + C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK -> no direct match found
```

Novelty accounting:

```json
{
  "new_symbol_count": 3,
  "minimum_new_symbol_count": 2,
  "minimum_positive_case_count": 1,
  "minimum_counterexample_count": 1,
  "new_independent_case_ratio": 1.00,
  "duplicate_status": "pass",
  "data_quality_status": "source_proxy_only_non_price_evidence"
}
```

---

## 5. Case design

| case_id | symbol | trigger family | research role |
|---|---|---|---|
| `R3L72_C12_137400_20240529` | `137400` 피엔티 | battery-equipment orderbook resilience vs later call-off risk | positive-guarded Stage2 / later high-MAE watch |
| `R3L72_C12_121600_20240702` | `121600` 나노신소재 | CNT/battery material EV-slowdown call-off sensitivity | counterexample / failed Stage2 follow-through |
| `R3L72_C12_382840_20240702` | `382840` 원준 | battery equipment/capex slowdown exposure | counterexample / persistent high-MAE path |

The intended residual:

```text
C12 should not score battery-equipment/material names by price momentum alone.
It needs a customer-demand bridge:
- confirmed backlog/orderbook resilience can stay Stage2-Actionable-Guarded,
- customer call-off / EV slowdown exposure with high MAE should route to 4B/4C watch or false-positive counterexample.
```

---

## 6. Stock-Web OHLC and backtest

### 6.1 `137400` 피엔티 — orderbook-resilient positive, but later high-MAE guard

Trigger:

```text
trigger_date = 2024-05-28
trigger_type = Stage2-Actionable-Guarded
trigger_family = battery_equipment_orderbook_resilience_vs_customer_calloff_risk
entry_date = 2024-05-29
entry_price = 53600.0
entry_price_type = next_tradable_open
```

Relevant Stock-Web rows:

```csv
d,o,h,l,c,v,a,mc,s,m
2024-05-27,47500.0,50000.0,46950.0,49500.0,878799.0,43033579350.0,1125689301000.0,22741198,KOSDAQ GLOBAL
2024-05-28,50200.0,50300.0,48500.0,49000.0,364512.0,17970447800.0,1114318702000.0,22741198,KOSDAQ GLOBAL
2024-05-29,53600.0,62500.0,53000.0,60300.0,5484629.0,325084117200.0,1371294239400.0,22741198,KOSDAQ GLOBAL
2024-06-05,72000.0,78500.0,70600.0,74800.0,2451096.0,183718230600.0,1701041610400.0,22741198,KOSDAQ GLOBAL
2024-06-19,85100.0,89500.0,84000.0,84500.0,690736.0,59660038400.0,1921631231000.0,22741198,KOSDAQ GLOBAL
2024-08-05,51100.0,53400.0,45950.0,49200.0,837840.0,42067866100.0,1168159831200.0,23743086,KOSDAQ GLOBAL
2024-11-15,41850.0,42650.0,39750.0,41150.0,616771.0,25360281350.0,977027988900.0,23743086,KOSDAQ GLOBAL
2024-11-25,47600.0,48300.0,47200.0,48150.0,183323.0,8783071300.0,1143229590900.0,23743086,KOSDAQ GLOBAL
```

Backtest:

| window | peak/high | peak date | trough/low | trough date | MFE | MAE |
|---|---:|---|---:|---|---:|---:|
| 30 calendar days | 89500 | 2024-06-19 | 53000 | 2024-05-29 | +66.98% | -1.12% |
| 90 calendar days | 89500 | 2024-06-19 | 45950 | 2024-08-05 | +66.98% | -14.27% |
| 180 calendar days | 89500 | 2024-06-19 | 39750 | 2024-11-15 | +66.98% | -25.84% |

Interpretation:

```text
137400 is a positive-but-guarded C12 case.
The early price path was strong and low-MAE, consistent with orderbook resilience.
However, the 180D path eventually printed -25.84% MAE, so the model should not turn early MFE into Green unless customer/orderbook conversion remains verified.
```

### 6.2 `121600` 나노신소재 — material exposure failed Stage2 follow-through

Trigger:

```text
trigger_date = 2024-07-01
trigger_type = Stage2-FalsePositive-Candidate
trigger_family = battery_material_customer_demand_slowdown_calloff
entry_date = 2024-07-02
entry_price = 117500.0
entry_price_type = next_tradable_open
```

Relevant Stock-Web rows:

```csv
d,o,h,l,c,v,a,mc,s,m
2024-07-01,117000.0,118700.0,112600.0,116300.0,208729.0,24137659300.0,1418403871400.0,12196078,KOSDAQ
2024-07-02,117500.0,118900.0,110800.0,111000.0,183414.0,20839980200.0,1353764658000.0,12196078,KOSDAQ
2024-07-04,121600.0,121700.0,116000.0,116400.0,125955.0,14843293600.0,1419623479200.0,12196078,KOSDAQ
2024-07-24,94200.0,97700.0,93500.0,93500.0,93412.0,8867233100.0,1140333293000.0,12196078,KOSDAQ
2024-08-05,87900.0,89700.0,68500.0,74900.0,264044.0,21196062100.0,913486242200.0,12196078,KOSDAQ
2024-09-27,97500.0,97700.0,94200.0,94900.0,110233.0,10568336700.0,1157407802200.0,12196078,KOSDAQ
2024-11-15,65200.0,65800.0,59300.0,63700.0,317938.0,19710158700.0,776890168600.0,12196078,KOSDAQ
2024-12-27,59500.0,60000.0,57800.0,59400.0,64293.0,3783923600.0,724447033200.0,12196078,KOSDAQ
```

Backtest:

| window | peak/high | peak date | trough/low | trough date | MFE | MAE |
|---|---:|---|---:|---|---:|---:|
| 30 calendar days | 121700 | 2024-07-04 | 90000 | 2024-07-31 | +3.57% | -23.40% |
| 90 calendar days | 121700 | 2024-07-04 | 68500 | 2024-08-05 | +3.57% | -41.70% |
| 180 calendar days | 121700 | 2024-07-04 | 57800 | 2024-12-27 | +3.57% | -50.81% |

Interpretation:

```text
121600 is a clean C12 counterexample.
It had only small upside after the selected trigger but extremely large MAE.
This should not be Stage2-Actionable unless customer/orderbook evidence is explicitly repaired and verified.
```

### 6.3 `382840` 원준 — battery equipment/capex slowdown exposure

Trigger:

```text
trigger_date = 2024-07-01
trigger_type = Stage2-FalsePositive-Candidate
trigger_family = battery_equipment_capex_slowdown_calloff
entry_date = 2024-07-02
entry_price = 13910.0
entry_price_type = next_tradable_open
```

Relevant Stock-Web rows:

```csv
d,o,h,l,c,v,a,mc,s,m
2024-07-01,13790.0,14070.0,13760.0,13880.0,33316.0,464101270.0,211969544280.0,15271581,KOSDAQ
2024-07-02,13910.0,13970.0,13410.0,13430.0,54283.0,738985310.0,205097332830.0,15271581,KOSDAQ
2024-07-12,13900.0,14120.0,13170.0,13240.0,174062.0,2354626190.0,202195732440.0,15271581,KOSDAQ
2024-07-31,10950.0,11000.0,10700.0,10890.0,48331.0,522171820.0,166307517090.0,15271581,KOSDAQ
2024-08-05,10680.0,10680.0,8600.0,8790.0,209927.0,1992591740.0,134237196990.0,15271581,KOSDAQ
2024-10-25,14440.0,15970.0,14020.0,14020.0,1020653.0,15322151710.0,214107565620.0,15271581,KOSDAQ
2024-11-05,14310.0,16140.0,14070.0,14740.0,2329836.0,35877332050.0,225103103940.0,15271581,KOSDAQ
2024-12-09,9390.0,9390.0,8750.0,8850.0,161304.0,1446177770.0,135153491850.0,15271581,KOSDAQ
```

Backtest:

| window | peak/high | peak date | trough/low | trough date | MFE | MAE |
|---|---:|---|---:|---|---:|---:|
| 30 calendar days | 14120 | 2024-07-12 | 10700 | 2024-07-31 | +1.51% | -23.08% |
| 90 calendar days | 14120 | 2024-07-12 | 8600 | 2024-08-05 | +1.51% | -38.17% |
| 180 calendar days | 16140 | 2024-11-05 | 8600 | 2024-08-05 | +16.03% | -38.17% |

Interpretation:

```text
382840 is a second C12 counterexample.
The later 180D MFE recovered somewhat, but only after a deep -38.17% MAE.
This is not a clean Stage2 setup; it should route to 4B/high-MAE watch or false-positive review until order/capex timing is repaired with hard evidence.
```

---

## 7. Machine-readable trigger JSONL

```jsonl
{"row_type":"trigger","research_id":"R3L72_C12_BATTERY_CALLOFF_HIGH_MAE","round":"R3","loop":72,"large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK","fine_archetype_id":"BATTERY_EQUIPMENT_MATERIAL_CUSTOMER_CALLOFF_HIGH_MAE","symbol":"137400","name":"피엔티","trigger_type":"Stage2-Actionable-Guarded","trigger_family":"battery_equipment_orderbook_resilience_vs_customer_calloff_risk","trigger_date":"2024-05-28","entry_date":"2024-05-29","entry_price":53600.0,"entry_price_type":"next_tradable_open","price_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","mfe_30d_pct":66.98,"mae_30d_pct":-1.12,"mfe_90d_pct":66.98,"mae_90d_pct":-14.27,"mfe_180d_pct":66.98,"mae_180d_pct":-25.84,"peak_price_180d":89500.0,"peak_date_180d":"2024-06-19","trough_price_180d":39750.0,"trough_date_180d":"2024-11-15","calibration_usable":true,"case_polarity":"positive_guarded","evidence_url_pending":true,"source_proxy_only":true,"non_price_evidence_strength":"medium_pending_url_repair","price_only_blowoff":false,"expected_stage_current_profile":"Stage2-Actionable-Guarded_to_Yellow_if_orderbook_bridge_verified","residual_error_type":"early_low_MAE_positive_but_green_requires_customer_orderbook_conversion"}
{"row_type":"trigger","research_id":"R3L72_C12_BATTERY_CALLOFF_HIGH_MAE","round":"R3","loop":72,"large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK","fine_archetype_id":"BATTERY_EQUIPMENT_MATERIAL_CUSTOMER_CALLOFF_HIGH_MAE","symbol":"121600","name":"나노신소재","trigger_type":"Stage2-FalsePositive-Candidate","trigger_family":"battery_material_customer_demand_slowdown_calloff","trigger_date":"2024-07-01","entry_date":"2024-07-02","entry_price":117500.0,"entry_price_type":"next_tradable_open","price_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","mfe_30d_pct":3.57,"mae_30d_pct":-23.40,"mfe_90d_pct":3.57,"mae_90d_pct":-41.70,"mfe_180d_pct":3.57,"mae_180d_pct":-50.81,"peak_price_180d":121700.0,"peak_date_180d":"2024-07-04","trough_price_180d":57800.0,"trough_date_180d":"2024-12-27","calibration_usable":true,"case_polarity":"counterexample","evidence_url_pending":true,"source_proxy_only":true,"non_price_evidence_strength":"low_pending_url_repair","price_only_blowoff":false,"expected_stage_current_profile":"blocked_Stage2_or_4B_high_MAE_watch","residual_error_type":"small_MFE_large_MAE_battery_material_calloff_false_positive"}
{"row_type":"trigger","research_id":"R3L72_C12_BATTERY_CALLOFF_HIGH_MAE","round":"R3","loop":72,"large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK","fine_archetype_id":"BATTERY_EQUIPMENT_MATERIAL_CUSTOMER_CALLOFF_HIGH_MAE","symbol":"382840","name":"원준","trigger_type":"Stage2-FalsePositive-Candidate","trigger_family":"battery_equipment_capex_slowdown_calloff","trigger_date":"2024-07-01","entry_date":"2024-07-02","entry_price":13910.0,"entry_price_type":"next_tradable_open","price_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","mfe_30d_pct":1.51,"mae_30d_pct":-23.08,"mfe_90d_pct":1.51,"mae_90d_pct":-38.17,"mfe_180d_pct":16.03,"mae_180d_pct":-38.17,"peak_price_180d":16140.0,"peak_date_180d":"2024-11-05","trough_price_180d":8600.0,"trough_date_180d":"2024-08-05","calibration_usable":true,"case_polarity":"counterexample","evidence_url_pending":true,"source_proxy_only":true,"non_price_evidence_strength":"low_pending_url_repair","price_only_blowoff":false,"expected_stage_current_profile":"blocked_Stage2_or_4B_high_MAE_watch","residual_error_type":"equipment_capex_calloff_high_MAE_before_any_recovery"}
```

---

## 8. Score simulation and raw component breakdown

This is shadow-only and does not change production scoring.

| symbol | EPS/FCF | customer/order visibility | call-off risk control | market mispricing | valuation rerating | capital allocation | information confidence | shadow total | intended route |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| `137400` | 10 | 12 | 8 | 13 | 11 | 4 | 7 | 65 | Stage2-Actionable-Guarded; Yellow only after URL-repaired backlog bridge |
| `121600` | 5 | 5 | 2 | 5 | 4 | 3 | 5 | 29 | blocked Stage2 / high-MAE watch |
| `382840` | 4 | 5 | 2 | 5 | 4 | 3 | 5 | 28 | blocked Stage2 / high-MAE watch |

### Current calibrated profile stress test

The current calibrated profile already blocks price-only blowoff.  
The remaining C12 risk is **source-quality plus MAE sequencing**.

```text
C12 positive-guarded path:
  equipment/orderbook resilience is plausible
  + strong MFE and low 30D MAE
  + but source evidence is not URL-repaired
  => Stage2-Actionable-Guarded only; no Green

C12 false-positive path:
  customer/EV-slowdown exposure
  + weak MFE
  + 30D/90D MAE worse than -20%
  + no verified orderbook bridge
  => blocked Stage2 or 4B/high-MAE watch
```

---

## 9. Aggregate metrics

```json
{
  "row_type": "aggregate",
  "research_id": "R3L72_C12_BATTERY_CALLOFF_HIGH_MAE",
  "round": "R3",
  "loop": 72,
  "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY",
  "canonical_archetype_id": "C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK",
  "fine_archetype_id": "BATTERY_EQUIPMENT_MATERIAL_CUSTOMER_CALLOFF_HIGH_MAE",
  "case_count": 3,
  "calibration_usable_case_count": 3,
  "positive_guarded_case_count": 1,
  "counterexample_count": 2,
  "new_symbol_count": 3,
  "source_proxy_only_count": 3,
  "evidence_url_pending_count": 3,
  "avg_mfe_30d_pct": 24.02,
  "avg_mae_30d_pct": -15.87,
  "avg_mfe_90d_pct": 24.02,
  "avg_mae_90d_pct": -31.38,
  "avg_mfe_180d_pct": 28.86,
  "avg_mae_180d_pct": -38.27,
  "worst_mae_180d_pct": -50.81
}
```

---

## 10. Shadow rule candidate

```yaml
row_type: canonical_archetype_rule_candidate
canonical_archetype_id: C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK
fine_archetype_id: BATTERY_EQUIPMENT_MATERIAL_CUSTOMER_CALLOFF_HIGH_MAE
rule_name: C12_customer_calloff_bridge_and_mae_router
production_scoring_changed: false
shadow_weight_only: true
```

### Proposed routing logic

```text
For C12 battery customer contract / call-off risk cases:

Tier A: orderbook-resilient equipment case
  Conditions:
    - company has plausible equipment/orderbook linkage
    - MFE is strong
    - 30D MAE is contained
    - customer/orderbook evidence is URL-repaired
  Routing:
    - Stage2-Actionable allowed
    - Stage3-Yellow allowed after verification
    - Green only after customer/orderbook conversion or margin bridge is verified

Tier B: source-proxy-only orderbook narrative
  Conditions:
    - price path is positive but evidence is not URL-repaired
  Routing:
    - Stage2-Actionable-Guarded
    - no positive weight promotion
    - no Green

Tier C: call-off / EV-slowdown false-positive path
  Conditions:
    - 30D or 90D MAE worse than -20%
    - MFE weak or delayed
    - customer/orderbook bridge missing
  Routing:
    - blocked Stage2 or 4B/high-MAE watch
    - count as counterexample
```

### Suggested shadow delta

```json
{
  "row_type": "shadow_weight",
  "axis": "c12_customer_calloff_bridge_and_mae_router",
  "scope": "canonical_archetype_id:C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK",
  "proposal": {
    "source_proxy_only_green_allowed": false,
    "evidence_url_pending_positive_weight_blocked": true,
    "stage2_guarded_allowed_when_30d_mae_contained": true,
    "calloff_high_mae_watch_threshold_pct": -20.0,
    "green_requires_customer_orderbook_or_margin_bridge": true
  },
  "confidence": "medium_low_until_url_repair",
  "apply_now": false,
  "reason": "Three new C12 symbols show sharp separation between early low-MAE equipment resilience and weak-MFE/high-MAE material/equipment false positives, but all non-price evidence remains URL-pending."
}
```

---

## 11. Residual contribution summary

```json
{
  "row_type": "residual_contribution",
  "research_id": "R3L72_C12_BATTERY_CALLOFF_HIGH_MAE",
  "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY",
  "canonical_archetype_id": "C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK",
  "contribution": "Adds three less-repeated C12 battery equipment/material cases and highlights that customer-calloff risk should be routed through MAE and source-quality guards. Strong MFE with low initial MAE can remain Stage2-Guarded, but weak MFE with 30D/90D MAE worse than -20% should be blocked or routed to 4B/high-MAE watch.",
  "positive_case_added": 1,
  "counterexample_case_added": 2,
  "new_symbol_count": 3,
  "data_quality_blocker": "All three non-price evidence triggers require URL-level repair before positive weight promotion.",
  "guardrail_added": "C12 Green requires verified customer/orderbook or margin bridge; source_proxy_only plus high MAE blocks Green."
}
```

---

## 12. Validation scope

```yaml
validation_scope:
  price_source: Songdaiki/stock-web
  price_basis: tradable_raw
  price_adjustment_status: raw_unadjusted_marcap
  manifest_max_date: 2026-02-20
  forward_window_required: 180_calendar_days
  forward_window_available: true
  raw_shard_used_for_weight_calibration: false
  corporate_action_contaminated_180D_window:
    137400: false
    121600: false
    382840: false
  evidence_url_pending:
    137400: true
    121600: true
    382840: true
  source_proxy_only:
    137400: true
    121600: true
    382840: true
```

Limitations:

```text
- Price path is validated against Stock-Web tradable OHLC rows.
- Non-price evidence is not URL-repaired in this run.
- Therefore this artifact is useful for C12 residual shape and high-MAE guardrail design, but should not promote positive weights until DART/IR/report URLs verify customer/orderbook or margin bridge evidence.
- It should not be read as a current investment view.
```

---

## 13. Deferred Coding Agent Handoff Prompt

Do not execute this prompt in the current research run.

```text
You are the later batch implementation agent for Songdaiki/stock_agent.

Read this MD as one v12 historical residual research artifact.

Task:
1. Ingest the machine-readable trigger rows.
2. Preserve R3 / loop 72 metadata.
3. Add the cases to C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK only if parser validation passes.
4. Treat all three non-price triggers as evidence_url_pending=true and source_proxy_only=true until URL-level evidence is repaired.
5. Do not use these rows for positive weight promotion until DART/IR/report URLs verify customer orderbook, call-off, margin bridge, or demand exposure.
6. Add a shadow-only rule candidate named C12_customer_calloff_bridge_and_mae_router.
7. Do not loosen Stage3-Green.
8. Add high-MAE guards:
   - if 30D/90D MAE <= -20% and customer/orderbook bridge is missing, block Stage2 and Green.
   - if source_proxy_only=true, allow only Stage2-Actionable-Guarded, not Green.
9. Keep production scoring unchanged unless later batch promotion logic independently marks this axis safe.
```

---

## 14. Next round state

```text
completed_round = R3
completed_loop = 72
next_round = R4
next_loop = 72
next_large_sector_hint = L4_MATERIALS_SPREAD_RESOURCE
```
