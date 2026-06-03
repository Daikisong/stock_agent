# E2R Stock-Web v12 Residual Research — R3 Loop 75

```yaml
research_session: post_calibrated_sector_archetype_residual_research
mode: historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12
completed_round: R3
completed_loop: 75
next_round: R4
next_loop: 75
large_sector_id: L3_BATTERY_EV_GREEN_MOBILITY
canonical_archetype_id: C11_BATTERY_ORDERBOOK_RERATING
fine_archetype_id: SECOND_TIER_BATTERY_EQUIPMENT_ORDERBOOK_BRIDGE_AND_HIGH_MAE_ROUTER
output_file: e2r_stock_web_v12_residual_round_R3_loop_75_L3_BATTERY_EV_GREEN_MOBILITY_C11_BATTERY_ORDERBOOK_RERATING_research.md
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

The active execution prompt fixes the research mode:

```text
primary_price_source = Songdaiki/stock-web
source_basis = FinanceData/marcap transformed into assistant-readable symbol-year CSV shards
price_basis = tradable_raw
price_adjustment_status = raw_unadjusted_marcap

production_scoring_changed = false
shadow_weight_only = true
must_use_actual_stock_web_1D_OHLC = true
must_include_backtest_result = true
must_include_score_return_alignment = true
must_include_current_calibrated_profile_stress_test = true
must_include_positive_and_counterexample_balance = true
must_output_every_usable_trigger_as_jsonl = true
```

### Round resolution

The immediately preceding completed scheduled artifact in this automation chain was:

```text
completed_round = R2
completed_loop  = 75
large_sector_id = L2_AI_SEMICONDUCTOR_ELECTRONICS
canonical_archetype_id = C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF
```

Therefore:

```text
scheduled_round = R3
scheduled_loop  = 75
```

R3 maps to:

```text
large_sector_id = L3_BATTERY_EV_GREEN_MOBILITY
```

This run selects:

```text
canonical_archetype_id = C11_BATTERY_ORDERBOOK_RERATING
fine_archetype_id = SECOND_TIER_BATTERY_EQUIPMENT_ORDERBOOK_BRIDGE_AND_HIGH_MAE_ROUTER
```

This is a valid R3/L3 pairing.

---

## 1. Why this R3/C11 run

The no-repeat ledger shows C11 is moderately covered and concentrated in top battery-cell/material and major equipment names:

```text
C11_BATTERY_ORDERBOOK_RERATING:
  rows: 67
  symbols: 23
  date_range: 2022-08-17~2024-07-22
  good/bad S2: 24/5
  4B/4C: 17/5
  URL/proxy: 0/0
  top covered symbols: 247540(11), 003670(8), 393890(8), 348370(6), 066970(5), 222080(4)
```

This file avoids those top-covered names and tests second-tier battery equipment / inspection / formation names:

```text
137400 피엔티
217820 원익피앤이
302430 이노메트리
```

Research question:

```text
Can C11 separate real equipment orderbook rerating from second-tier battery equipment relief spikes where orderbook relevance exists but customer delivery, margin conversion, and call-off resistance are not URL-repaired?
```

C11 is an orderbook archetype. An orderbook is not just a headline pile of contracts; it is a conveyor belt. Stage2 should ask whether backlog turns into delivery, revenue recognition, margin, and cash. If the conveyor slows, the first rally becomes inventory sitting on the floor.

---

## 2. Price atlas validation

### Stock-Web manifest snapshot

```json
{
  "price_atlas_repo": "Songdaiki/stock-web",
  "source_name": "FinanceData/marcap",
  "source_repo_url": "https://github.com/FinanceData/marcap",
  "price_adjustment_status": "raw_unadjusted_marcap",
  "min_date": "1995-05-02",
  "max_date": "2026-02-20",
  "tradable_row_count": 14354401,
  "raw_row_count": 15214118,
  "symbol_count": 5414,
  "active_like_symbol_count": 2868,
  "inactive_or_delisted_like_symbol_count": 2546,
  "markets": ["KONEX", "KOSDAQ", "KOSDAQ GLOBAL", "KOSPI"],
  "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year",
  "raw_shard_root": "atlas/ohlcv_raw_by_symbol_year",
  "schema_path": "atlas/schema.json",
  "universe_path": "atlas/universe/all_symbols.csv",
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

| symbol | name | market/profile status | corporate-action candidate overlap with selected 180D window | calibration usable |
|---|---|---|---|---|
| `137400` | 피엔티 | active_like / KOSDAQ GLOBAL | no 2024 overlap; old 2012/2019 candidates only | true |
| `217820` | 원익피앤이 | active_like / KOSDAQ | no 2024 overlap; latest listed candidate 2022-11-29 | true |
| `302430` | 이노메트리 | active_like / KOSDAQ | no 2024 overlap; latest listed candidate 2020-01-21 | true |

Profile caveat:

```text
Stock-Web OHLC is raw/unadjusted marcap data.
These cases are calibration-safe for the selected 2024 windows because no listed corporate-action candidate overlaps each entry~D+180 test window.
```

---

## 3. Evidence status and trigger discipline

This artifact intentionally uses conservative non-price evidence flags:

```text
evidence_url_pending = true
source_proxy_only = true
```

Reason:

```text
The Stock-Web price path is fully validated, but company-level order backlog, customer quality, delivery schedule, customer call-off risk, revenue recognition, gross margin, working capital, and cash conversion evidence still require later URL repair through filings, IR decks, order disclosures, customer data, or sell-side reports before production weight promotion.
```

C11 interpretation used here:

```text
C11 is not simply “battery equipment stock rose.”
It asks whether equipment orders become operating leverage:
- customer/order quality,
- backlog and delivery schedule,
- call-off or delay resistance,
- revenue recognition,
- margin conversion,
- working-capital and cash-flow quality,
- and contained MAE after the trigger.
```

This file is therefore a residual/guardrail artifact, not a positive production patch.

---

## 4. No-repeat and novelty check

Hard duplicate key:

```text
canonical_archetype_id + symbol + trigger_type + entry_date
```

Targeted repository searches before writing:

```text
137400 + C11_BATTERY_ORDERBOOK_RERATING -> no direct match found
217820 + C11_BATTERY_ORDERBOOK_RERATING -> no direct match found
302430 + C11_BATTERY_ORDERBOOK_RERATING -> no direct match found
```

Novelty accounting:

```json
{
  "new_symbol_count": 3,
  "minimum_new_symbol_count": 2,
  "positive_guarded_case_count": 1,
  "counterexample_count": 2,
  "new_independent_case_ratio": 1.00,
  "duplicate_status": "pass",
  "data_quality_status": "source_proxy_only_non_price_evidence"
}
```

---

## 5. Case design

| case_id | symbol | trigger family | research role |
|---|---|---|---|
| `R3L75_C11_137400_20240529` | `137400` 피엔티 | battery roll-to-roll equipment orderbook rerating | positive-guarded high-MFE / later-MAE watch |
| `R3L75_C11_217820_20240215` | `217820` 원익피앤이 | formation equipment relief spike | weak-MFE extreme-MAE counterexample |
| `R3L75_C11_302430_20240311` | `302430` 이노메트리 | X-ray inspection equipment spike | first-window MFE / later-MAE counterexample |

The intended residual:

```text
C11 should separate:
1. battery equipment orderbook rerating where MFE is large and early MAE is controlled;
2. formation-equipment relief where the first spike is not enough and 180D MAE becomes extreme;
3. inspection-equipment names where first-window MFE exists but later high MAE blocks Yellow/Green.
```

---

## 6. Stock-Web OHLC and backtest

### 6.1 `137400` 피엔티 — battery roll-to-roll equipment orderbook high-MFE case

Trigger:

```text
trigger_date = 2024-05-28
trigger_type = Stage2-Actionable-Guarded
trigger_family = battery_roll_to_roll_equipment_orderbook_high_mfe_later_mae
entry_date = 2024-05-29
entry_price = 53600.0
entry_price_type = next_tradable_open_after_battery_equipment_orderbook_burst
```

Relevant Stock-Web rows:

```csv
d,o,h,l,c,v,a,mc,s,m
2024-05-28,50200.0,50300.0,48500.0,49000.0,364512.0,17970447800.0,1114318702000.0,22741198,KOSDAQ GLOBAL
2024-05-29,53600.0,62500.0,53000.0,60300.0,5484629.0,325084117200.0,1371294239400.0,22741198,KOSDAQ GLOBAL
2024-06-04,66000.0,71400.0,65600.0,69400.0,1145358.0,79519670500.0,1578239141200.0,22741198,KOSDAQ GLOBAL
2024-06-19,85100.0,89500.0,84000.0,84500.0,690736.0,59660038400.0,1921631231000.0,22741198,KOSDAQ GLOBAL
2024-08-05,51100.0,53400.0,45950.0,49200.0,837840.0,42067866100.0,1168159831200.0,23743086,KOSDAQ GLOBAL
2024-09-09,46050.0,49350.0,46000.0,48600.0,263074.0,12577201150.0,1153913979600.0,23743086,KOSDAQ GLOBAL
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
137400 is the positive-guarded holdout.
The first 30D/90D path produced strong MFE, but the 180D drawdown means it should not become Green without evidence repair.
C11 should preserve this as Stage2-Guarded / Yellow-after-repair, not as automatic Green.
```

### 6.2 `217820` 원익피앤이 — formation equipment relief spike with extreme MAE

Trigger:

```text
trigger_date = 2024-02-14
trigger_type = Stage2-FalsePositive-Candidate
trigger_family = battery_formation_equipment_orderbook_relief_weak_mfe_high_mae
entry_date = 2024-02-15
entry_price = 6680.0
entry_price_type = next_tradable_open_after_formation_equipment_relief_spike
```

Relevant Stock-Web rows:

```csv
d,o,h,l,c,v,a,mc,s,m
2024-02-14,6200.0,6630.0,6200.0,6580.0,1172900.0,7639943920.0,312250998220.0,47454559,KOSDAQ
2024-02-15,6680.0,7300.0,6580.0,6870.0,4446465.0,31202272170.0,326012820330.0,47454559,KOSDAQ
2024-03-05,5740.0,5810.0,5650.0,5710.0,274357.0,1561530240.0,270965531890.0,47454559,KOSDAQ
2024-05-14,5030.0,5120.0,5010.0,5050.0,98743.0,498114510.0,239645522950.0,47454559,KOSDAQ
2024-06-18,4720.0,4780.0,4530.0,4530.0,314776.0,1453316600.0,214969152270.0,47454559,KOSDAQ
2024-08-05,3650.0,3650.0,2890.0,3045.0,303407.0,991845210.0,144499132155.0,47454559,KOSDAQ
2024-09-06,3025.0,3045.0,2935.0,2945.0,82552.0,244391215.0,139753676255.0,47454559,KOSDAQ
```

Backtest:

| window | peak/high | peak date | trough/low | trough date | MFE | MAE |
|---|---:|---|---:|---|---:|---:|
| 30 calendar days | 7300 | 2024-02-15 | 5650 | 2024-03-05 | +9.28% | -15.42% |
| 90 calendar days | 7300 | 2024-02-15 | 5010 | 2024-05-14 | +9.28% | -25.00% |
| 180 calendar days | 7300 | 2024-02-15 | 2890 | 2024-08-05 | +9.28% | -56.74% |

Interpretation:

```text
217820 is a clean C11 false-positive branch.
The orderbook/equipment label was plausible, but MFE stayed below +10% and 180D MAE became extreme.
This should block Stage2 or route to 4B/4C high-MAE watch unless customer delivery and margin evidence were repaired before the trigger.
```

### 6.3 `302430` 이노메트리 — X-ray inspection equipment spike with later high MAE

Trigger:

```text
trigger_date = 2024-03-08
trigger_type = Stage2-FalsePositive-Candidate
trigger_family = battery_xray_inspection_equipment_spike_later_high_mae
entry_date = 2024-03-11
entry_price = 12750.0
entry_price_type = next_tradable_open_after_xray_inspection_equipment_spike
```

Relevant Stock-Web rows:

```csv
d,o,h,l,c,v,a,mc,s,m
2024-03-08,10900.0,13850.0,10750.0,13010.0,2729445.0,35054163430.0,127930036080.0,9833208,KOSDAQ
2024-03-11,12750.0,12960.0,12050.0,12080.0,390761.0,4860967340.0,118785152640.0,9833208,KOSDAQ
2024-03-12,12120.0,15260.0,11940.0,13980.0,6039239.0,86643415290.0,137468247840.0,9833208,KOSDAQ
2024-04-09,11800.0,11890.0,11500.0,11560.0,38200.0,444341220.0,113671884480.0,9833208,KOSDAQ
2024-05-31,10690.0,10870.0,10400.0,10710.0,21834.0,233660290.0,105313657680.0,9833208,KOSDAQ
2024-07-23,9090.0,10890.0,9090.0,9240.0,819009.0,8383516120.0,90858841920.0,9833208,KOSDAQ
2024-08-05,9050.0,9110.0,8000.0,8140.0,85094.0,728408810.0,80042313120.0,9833208,KOSDAQ
```

Backtest:

| window | peak/high | peak date | trough/low | trough date | MFE | MAE |
|---|---:|---|---:|---|---:|---:|
| 30 calendar days | 15260 | 2024-03-12 | 11500 | 2024-04-09 | +19.69% | -9.80% |
| 90 calendar days | 15260 | 2024-03-12 | 10400 | 2024-05-31 | +19.69% | -18.43% |
| 180 calendar days | 15260 | 2024-03-12 | 8000 | 2024-08-05 | +19.69% | -37.25% |

Interpretation:

```text
302430 is the first-window-MFE / later-MAE warning.
The first month was not a pure failure, but the 180D drawdown crossed the hard guardrail.
C11 should cap this at Stage2-Guarded or local 4B watch until inspection-equipment order backlog, customer quality, delivery, and margin evidence are repaired.
```

---

## 7. Machine-readable trigger JSONL

```jsonl
{"row_type":"trigger","research_id":"R3L75_C11_BATTERY_EQUIPMENT_ORDERBOOK_ROUTER","round":"R3","loop":75,"large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C11_BATTERY_ORDERBOOK_RERATING","fine_archetype_id":"SECOND_TIER_BATTERY_EQUIPMENT_ORDERBOOK_BRIDGE_AND_HIGH_MAE_ROUTER","symbol":"137400","name":"피엔티","trigger_type":"Stage2-Actionable-Guarded","trigger_family":"battery_roll_to_roll_equipment_orderbook_high_mfe_later_mae","trigger_date":"2024-05-28","entry_date":"2024-05-29","entry_price":53600.0,"entry_price_type":"next_tradable_open_after_battery_equipment_orderbook_burst","price_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","mfe_30d_pct":66.98,"mae_30d_pct":-1.12,"mfe_90d_pct":66.98,"mae_90d_pct":-14.27,"mfe_180d_pct":66.98,"mae_180d_pct":-25.84,"peak_price_180d":89500.0,"peak_date_180d":"2024-06-19","trough_price_180d":39750.0,"trough_date_180d":"2024-11-15","calibration_usable":true,"case_polarity":"positive_guarded_high_mfe_later_mae","evidence_url_pending":true,"source_proxy_only":true,"non_price_evidence_strength":"medium_pending_url_repair","price_only_blowoff":false,"expected_stage_current_profile":"Stage2-Guarded_to_Yellow_only_if_order_backlog_customer_delivery_margin_bridge_repaired","residual_error_type":"high_mfe_orderbook_equipment_path_requires_later_mae_guard_and_url_repaired_customer_order_margin_bridge_before_green"}
{"row_type":"trigger","research_id":"R3L75_C11_BATTERY_EQUIPMENT_ORDERBOOK_ROUTER","round":"R3","loop":75,"large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C11_BATTERY_ORDERBOOK_RERATING","fine_archetype_id":"SECOND_TIER_BATTERY_EQUIPMENT_ORDERBOOK_BRIDGE_AND_HIGH_MAE_ROUTER","symbol":"217820","name":"원익피앤이","trigger_type":"Stage2-FalsePositive-Candidate","trigger_family":"battery_formation_equipment_orderbook_relief_weak_mfe_high_mae","trigger_date":"2024-02-14","entry_date":"2024-02-15","entry_price":6680.0,"entry_price_type":"next_tradable_open_after_formation_equipment_relief_spike","price_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","mfe_30d_pct":9.28,"mae_30d_pct":-15.42,"mfe_90d_pct":9.28,"mae_90d_pct":-25.0,"mfe_180d_pct":9.28,"mae_180d_pct":-56.74,"peak_price_180d":7300.0,"peak_date_180d":"2024-02-15","trough_price_180d":2890.0,"trough_date_180d":"2024-08-05","calibration_usable":true,"case_polarity":"counterexample_weak_mfe_extreme_mae","evidence_url_pending":true,"source_proxy_only":true,"non_price_evidence_strength":"low_pending_url_repair","price_only_blowoff":false,"expected_stage_current_profile":"blocked_Stage2_or_4B_4C_high_MAE_watch_until_customer_order_margin_bridge_repaired","residual_error_type":"formation_equipment_orderbook_relief_had_weak_mfe_and_extreme_mae_without_customer_delivery_margin_bridge"}
{"row_type":"trigger","research_id":"R3L75_C11_BATTERY_EQUIPMENT_ORDERBOOK_ROUTER","round":"R3","loop":75,"large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C11_BATTERY_ORDERBOOK_RERATING","fine_archetype_id":"SECOND_TIER_BATTERY_EQUIPMENT_ORDERBOOK_BRIDGE_AND_HIGH_MAE_ROUTER","symbol":"302430","name":"이노메트리","trigger_type":"Stage2-FalsePositive-Candidate","trigger_family":"battery_xray_inspection_equipment_spike_later_high_mae","trigger_date":"2024-03-08","entry_date":"2024-03-11","entry_price":12750.0,"entry_price_type":"next_tradable_open_after_xray_inspection_equipment_spike","price_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","mfe_30d_pct":19.69,"mae_30d_pct":-9.8,"mfe_90d_pct":19.69,"mae_90d_pct":-18.43,"mfe_180d_pct":19.69,"mae_180d_pct":-37.25,"peak_price_180d":15260.0,"peak_date_180d":"2024-03-12","trough_price_180d":8000.0,"trough_date_180d":"2024-08-05","calibration_usable":true,"case_polarity":"counterexample_later_high_mae","evidence_url_pending":true,"source_proxy_only":true,"non_price_evidence_strength":"low_pending_url_repair","price_only_blowoff":false,"expected_stage_current_profile":"Stage2-Guarded_or_local_4B_high_MAE_watch_until_inspection_order_backlog_bridge_repaired","residual_error_type":"inspection_equipment_spike_had_first_window_mfe_but_later_mae_blocks_yellow_green_without_order_backlog_bridge"}
```

---

## 8. Score simulation and raw component breakdown

This is shadow-only and does not change production scoring.

| symbol | orderbook visibility | customer quality | delivery / revenue conversion | call-off risk control | market mispricing | margin conversion | information confidence | shadow total | intended route |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| `137400` | 12 | 10 | 9 | 6 | 13 | 7 | 6 | 63 | Stage2-Guarded / Yellow only after evidence repair |
| `217820` | 4 | 3 | 3 | 2 | 3 | 2 | 4 | 21 | blocked Stage2 / 4B-4C high-MAE watch |
| `302430` | 5 | 4 | 4 | 3 | 6 | 3 | 4 | 29 | Stage2-Guarded at most / local 4B watch |

### Current calibrated profile stress test

The current calibrated profile already blocks pure price-only blowoff.  
The remaining C11 issue is **battery orderbook label without delivery/margin conversion**:

```text
C11 high-MFE equipment path:
  battery equipment orderbook relevance
  + high 30D/90D MFE
  + source evidence still pending
  + 180D MAE worse than -25%
  => Stage2-Guarded, Yellow only after evidence repair, no Green

C11 weak-MFE high-MAE path:
  equipment/orderbook label exists
  + MFE_30D < +10%
  + MAE_90D <= -20% or MAE_180D <= -50%
  => block Stage2 or route to 4B/4C high-MAE watch

C11 first-window-MFE later-MAE path:
  MFE_30D >= +15%
  + MAE_180D <= -35%
  + customer/order bridge unrepaired
  => Stage2-Guarded at most, no Yellow/Green
```

`137400` prevents overblocking: second-tier equipment can still generate real MFE.  
`217820` and `302430` show why C11 needs delivery/margin and high-MAE routing before promotion.

---

## 9. Aggregate metrics

```json
{
  "row_type": "aggregate",
  "research_id": "R3L75_C11_BATTERY_EQUIPMENT_ORDERBOOK_ROUTER",
  "round": "R3",
  "loop": 75,
  "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY",
  "canonical_archetype_id": "C11_BATTERY_ORDERBOOK_RERATING",
  "fine_archetype_id": "SECOND_TIER_BATTERY_EQUIPMENT_ORDERBOOK_BRIDGE_AND_HIGH_MAE_ROUTER",
  "case_count": 3,
  "calibration_usable_case_count": 3,
  "positive_guarded_case_count": 1,
  "counterexample_count": 2,
  "new_symbol_count": 3,
  "source_proxy_only_count": 3,
  "evidence_url_pending_count": 3,
  "avg_mfe_30d_pct": 31.98,
  "avg_mae_30d_pct": -8.78,
  "avg_mfe_90d_pct": 31.98,
  "avg_mae_90d_pct": -19.23,
  "avg_mfe_180d_pct": 31.98,
  "avg_mae_180d_pct": -39.94,
  "max_mfe_180d_pct": 66.98,
  "worst_mae_180d_pct": -56.74
}
```

---

## 10. 4B proximity split

```json
{
  "row_type": "4b_split",
  "research_id": "R3L75_C11_BATTERY_EQUIPMENT_ORDERBOOK_ROUTER",
  "stage2_guarded_or_yellow_candidate": [
    {
      "symbol": "137400",
      "reason": "strong +66.98% MFE, but 180D MAE reached -25.84%; Yellow/Green requires order/customer/margin evidence repair"
    }
  ],
  "blocked_stage2_or_4c_watch": [
    {
      "symbol": "217820",
      "reason": "MFE stayed below +10% while 180D MAE reached -56.74%"
    }
  ],
  "local_4b_high_mae_watch": [
    {
      "symbol": "302430",
      "reason": "first-window MFE existed, but 180D MAE reached -37.25%"
    }
  ],
  "full_4b_or_green_requires_non_price_evidence": [
    "order backlog and customer quality",
    "delivery schedule / revenue recognition",
    "customer call-off and delay risk reduction",
    "working-capital and cash-flow conversion",
    "gross margin / operating margin bridge"
  ]
}
```

---

## 11. Shadow rule candidate

```yaml
row_type: canonical_archetype_rule_candidate
canonical_archetype_id: C11_BATTERY_ORDERBOOK_RERATING
fine_archetype_id: SECOND_TIER_BATTERY_EQUIPMENT_ORDERBOOK_BRIDGE_AND_HIGH_MAE_ROUTER
rule_name: C11_second_tier_battery_equipment_orderbook_bridge_and_high_mae_router
production_scoring_changed: false
shadow_weight_only: true
```

### Proposed routing logic

```text
For C11 second-tier battery equipment / inspection / formation cases:

Tier A: high-MFE equipment orderbook path
  Conditions:
    - battery equipment orderbook relevance is clear
    - MFE_30D >= +40%
    - MAE_90D > -15%
    - evidence remains source_proxy_only
  Routing:
    - Stage2-Guarded allowed
    - Stage3-Yellow only after URL-repaired order/customer/delivery/margin bridge
    - no Green while evidence is pending

Tier B: weak-MFE high-MAE equipment relief
  Conditions:
    - MFE_30D < +10%
    - MAE_90D <= -20% or MAE_180D <= -50%
    - no repaired customer/order bridge
  Routing:
    - block Stage2
    - route to 4B/4C high-MAE watch
    - count as counterexample

Tier C: first-window-MFE / later-MAE inspection equipment
  Conditions:
    - MFE_30D >= +15%
    - MAE_180D <= -35%
    - evidence_url_pending or source_proxy_only remains true
  Routing:
    - Stage2-Guarded at most
    - local 4B/high-MAE watch
    - no Yellow/Green
```

### Suggested shadow delta

```json
{
  "row_type": "shadow_weight",
  "axis": "c11_second_tier_battery_equipment_orderbook_bridge_and_high_mae_router",
  "scope": "canonical_archetype_id:C11_BATTERY_ORDERBOOK_RERATING",
  "proposal": {
    "source_proxy_only_green_allowed": false,
    "order_customer_delivery_margin_bridge_required_for_green": true,
    "high_mfe_equipment_stage2_guarded_allowed": true,
    "high_mfe_threshold_30d_pct": 40.0,
    "high_mfe_path_mae90_min_pct": -15.0,
    "weak_mfe_threshold_30d_pct": 10.0,
    "weak_mfe_mae90_threshold_pct": -20.0,
    "hard_mae_threshold_180d_pct": -50.0,
    "later_mae_watch_threshold_180d_pct": -35.0,
    "positive_weight_blocked_until_url_repair": true
  },
  "confidence": "medium_low_until_url_repair",
  "apply_now": false,
  "reason": "One second-tier battery equipment high-MFE guarded case and two high-MAE counterexamples show that C11 should require URL-repaired order/customer/delivery/margin evidence before Yellow/Green."
}
```

---

## 12. Residual contribution summary

```json
{
  "row_type": "residual_contribution",
  "research_id": "R3L75_C11_BATTERY_EQUIPMENT_ORDERBOOK_ROUTER",
  "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY",
  "canonical_archetype_id": "C11_BATTERY_ORDERBOOK_RERATING",
  "contribution": "Adds three non-top-covered C11 second-tier battery equipment/inspection cases and separates a high-MFE roll-to-roll equipment rerating from weak-MFE and first-window-MFE high-MAE counterexamples. C11 Yellow/Green should require URL-repaired order backlog, customer quality, delivery schedule, call-off risk reduction, working-capital, cash-flow, and margin evidence.",
  "positive_guarded_case_added": 1,
  "counterexample_case_added": 2,
  "new_symbol_count": 3,
  "new_independent_case_count": 3,
  "reused_case_count": 0,
  "same_archetype_new_symbol_count": 3,
  "same_archetype_new_trigger_family_count": 3,
  "new_trigger_family_count": 3,
  "current_profile_error_count": 2,
  "diversity_score_summary": {
    "new_symbol_bonus": 9,
    "counterexample_gap_bonus": 4,
    "residual_error_bonus": 10,
    "wrong_round_penalty": 0,
    "repeated_same_symbol_penalty": 0,
    "net_interpretive_score": 23
  },
  "loop_contribution_label": "canonical_archetype_rule_candidate",
  "do_not_propose_new_weight_delta": false,
  "data_quality_blocker": "All three non-price battery equipment/orderbook triggers require URL-level repair before positive weight promotion.",
  "guardrail_added": "C11 source_proxy_only second-tier equipment cases with MFE_30D < +10% and MAE_90D <= -20% should block Stage2; cases with MFE_30D >= +15% but MAE_180D <= -35% should cap at Stage2-Guarded or 4B watch until order/customer/margin evidence is repaired."
}
```

One-line contribution:

```text
This loop adds 3 new independent cases, 2 counterexamples, and 2 residual errors for R3/L3_BATTERY_EV_GREEN_MOBILITY/C11_BATTERY_ORDERBOOK_RERATING.
```

---

## 13. Validation scope

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
    217820: false
    302430: false
  evidence_url_pending:
    137400: true
    217820: true
    302430: true
  source_proxy_only:
    137400: true
    217820: true
    302430: true
```

Limitations:

```text
- Price path is validated against Stock-Web tradable OHLC rows.
- Non-price evidence is not URL-repaired in this run.
- Therefore this artifact is useful for C11 second-tier battery equipment orderbook residual shape and high-MAE guardrail design, but should not promote positive weights until filings, IR, order disclosures, customer data, or reports verify order backlog, customer quality, delivery, revenue recognition, working capital, and margin conversion.
- It should not be read as a current investment view.
```

---

## 14. Deferred Coding Agent Handoff Prompt

Do not execute this prompt in the current research run.

```text
You are the later batch implementation agent for Songdaiki/stock_agent.

Read this MD as one v12 historical residual research artifact.

Task:
1. Ingest the machine-readable trigger rows.
2. Preserve R3 / loop 75 metadata.
3. Add the cases to C11_BATTERY_ORDERBOOK_RERATING only if parser validation passes.
4. Treat all three non-price triggers as evidence_url_pending=true and source_proxy_only=true until URL-level evidence is repaired.
5. Do not use these rows for positive weight promotion until filings/IR/order-disclosure/customer/report data verifies order backlog, customer quality, delivery schedule, revenue recognition, working capital, cash-flow, and margin conversion.
6. Add a shadow-only rule candidate named C11_second_tier_battery_equipment_orderbook_bridge_and_high_mae_router.
7. Do not loosen Stage3-Green.
8. Add C11-specific guards:
   - source_proxy_only -> no Green
   - Green requires repaired order/customer/delivery/margin bridge
   - MFE_30D >= +40% and MAE_90D > -15% may remain Stage2-Guarded until evidence repair
   - MFE_30D < +10% and MAE_90D <= -20% -> block Stage2 / 4B-4C watch
   - MFE_30D >= +15% but MAE_180D <= -35% -> Stage2-Guarded at most / local 4B watch
9. Keep production scoring unchanged unless later batch promotion logic independently marks this axis safe.
```

---

## 15. Next round state

```text
completed_round = R3
completed_loop = 75
next_round = R4
next_loop = 75
next_large_sector_hint = L4_MATERIALS_SPREAD_RESOURCE
round_schedule_status = valid
round_sector_consistency = pass
```
