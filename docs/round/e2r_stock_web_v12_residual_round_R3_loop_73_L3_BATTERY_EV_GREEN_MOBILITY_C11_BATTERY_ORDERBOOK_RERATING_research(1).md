# E2R Stock-Web v12 Residual Research — R3 Loop 73

```yaml
research_session: post_calibrated_sector_archetype_residual_research
mode: historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12
completed_round: R3
completed_loop: 73
next_round: R4
next_loop: 73
large_sector_id: L3_BATTERY_EV_GREEN_MOBILITY
canonical_archetype_id: C11_BATTERY_ORDERBOOK_RERATING
fine_archetype_id: BATTERY_EQUIPMENT_ORDERBOOK_RERATING_AND_HIGH_MAE_ROUTER
output_file: e2r_stock_web_v12_residual_round_R3_loop_73_L3_BATTERY_EV_GREEN_MOBILITY_C11_BATTERY_ORDERBOOK_RERATING_research.md
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
completed_loop  = 73
large_sector_id = L2_AI_SEMICONDUCTOR_ELECTRONICS
canonical_archetype_id = C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY
```

Therefore:

```text
scheduled_round = R3
scheduled_loop  = 73
```

R3 maps to:

```text
large_sector_id = L3_BATTERY_EV_GREEN_MOBILITY
```

This run selects:

```text
canonical_archetype_id = C11_BATTERY_ORDERBOOK_RERATING
fine_archetype_id = BATTERY_EQUIPMENT_ORDERBOOK_RERATING_AND_HIGH_MAE_ROUTER
```

This is a valid R3/L3 pairing.

---

## 1. Why this R3/C11 run

The no-repeat ledger shows C11 is meaningful but concentrated in large cell/material winners and a handful of already-covered names:

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

This file deliberately adds battery-equipment/orderbook names outside the top-covered C11 set:

```text
137400 피엔티
299030 하나기술
372170 윤성에프앤씨
```

Research question:

```text
Can C11 separate real equipment orderbook rerating from equipment-relief rallies whose first MFE is not supported by durable customer/order/margin evidence?
```

C11 is an orderbook archetype. A headline or theme can give the market a purchase order-shaped shadow, but Stage2/Green should require the actual paper: backlog, customer quality, repeat order, delivery schedule, and margin conversion.

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

| symbol | name | market/profile status | corporate-action candidate overlap with selected 180D window | calibration usable |
|---|---|---|---|---|
| `137400` | 피엔티 | active_like / KOSDAQ GLOBAL | no 2024 overlap; latest listed candidate 2019-05-30 | true |
| `299030` | 하나기술 | active_like / KOSDAQ | no 2024 overlap; old 2021 candidates only | true |
| `372170` | 윤성에프앤씨 | active_like / KOSDAQ | none listed | true |

Profile caveat:

```text
Stock-Web OHLC is raw/unadjusted marcap data. These cases are calibration-safe for the selected windows because no listed corporate-action candidate overlaps each entry~D+180 test window.
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
The Stock-Web price path is fully validated, but company-level equipment orderbook, customer call-off, delivery schedule, backlog conversion, and margin bridge evidence still require later URL repair through filings, IR decks, disclosures, customer data, or sell-side reports before production weight promotion.
```

C11 interpretation used here:

```text
C11 is not simply “battery equipment stock rallied.”
It asks whether the market is rerating a real orderbook:
- named or high-confidence customer orders,
- repeat equipment demand,
- delivery schedule and backlog conversion,
- customer call-off risk,
- and margin conversion.
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
299030 + C11_BATTERY_ORDERBOOK_RERATING -> no direct match found
372170 + C11_BATTERY_ORDERBOOK_RERATING -> no direct match found
```

Novelty accounting:

```json
{
  "new_symbol_count": 3,
  "minimum_new_symbol_count": 2,
  "positive_case_count": 1,
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
| `R3L73_C11_137400_20240529` | `137400` 피엔티 | battery equipment orderbook rerating with strong early MFE | positive-guarded / later high-MAE watch |
| `R3L73_C11_372170_20240531` | `372170` 윤성에프앤씨 | battery mixing-equipment orderbook relief rally | high-MFE then high-MAE counterexample |
| `R3L73_C11_299030_20240621` | `299030` 하나기술 | equipment orderbook thesis break / relief failure | false-positive / high-MAE counterexample |

The intended residual:

```text
C11 should separate:
1. orderbook rerating with strong early MFE and low early MAE;
2. equipment rallies where first-month MFE is useful but later MAE reveals orderbook fragility;
3. thesis-break setups where a relief attempt has limited MFE and severe drawdown.
```

---

## 6. Stock-Web OHLC and backtest

### 6.1 `137400` 피엔티 — orderbook rerating positive-guarded anchor

Trigger:

```text
trigger_date = 2024-05-28
trigger_type = Stage2-Actionable-Guarded
trigger_family = battery_equipment_orderbook_rerating_low_initial_mae
entry_date = 2024-05-29
entry_price = 53600.0
entry_price_type = next_tradable_open
```

Relevant Stock-Web rows:

```csv
d,o,h,l,c,v,a,mc,s,m
2024-05-28,50200.0,50300.0,48500.0,49000.0,364512.0,17970447800.0,1114318702000.0,22741198,KOSDAQ GLOBAL
2024-05-29,53600.0,62500.0,53000.0,60300.0,5484629.0,325084117200.0,1371294239400.0,22741198,KOSDAQ GLOBAL
2024-06-05,72000.0,78500.0,70600.0,74800.0,2451096.0,183718230600.0,1701041610400.0,22741198,KOSDAQ GLOBAL
2024-06-19,85100.0,89500.0,84000.0,84500.0,690736.0,59660038400.0,1921631231000.0,22741198,KOSDAQ GLOBAL
2024-07-22,53800.0,53800.0,51600.0,52000.0,381382.0,19898542800.0,1234640472000.0,23743086,KOSDAQ GLOBAL
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
137400 is the positive-guarded anchor.
The first month had strong MFE and nearly no MAE, so C11 Stage2-Actionable is reasonable.
However, the 180D drawdown crossed -25%, so Green still requires repaired orderbook/customer/margin evidence.
```

### 6.2 `372170` 윤성에프앤씨 — high-MFE equipment rally that later turned into high-MAE

Trigger:

```text
trigger_date = 2024-05-30
trigger_type = Stage2-Actionable-Guarded
trigger_family = battery_mixing_equipment_orderbook_relief_rally
entry_date = 2024-05-31
entry_price = 65400.0
entry_price_type = next_tradable_open
```

Relevant Stock-Web rows:

```csv
d,o,h,l,c,v,a,mc,s,m
2024-05-29,63600.0,68500.0,62500.0,65500.0,76223.0,4957079300.0,522627644000.0,7979048,KOSDAQ
2024-05-31,65400.0,75700.0,65400.0,69500.0,325364.0,23195473600.0,554543836000.0,7979048,KOSDAQ
2024-06-04,74000.0,84400.0,72900.0,81400.0,280207.0,22642841200.0,649494507200.0,7979048,KOSDAQ
2024-06-11,85400.0,91500.0,84500.0,88900.0,148588.0,13222781600.0,709337367200.0,7979048,KOSDAQ
2024-06-24,73900.0,75000.0,71500.0,71800.0,44877.0,3239253700.0,572895646400.0,7979048,KOSDAQ
2024-08-05,55000.0,55000.0,44800.0,46200.0,89321.0,4420626900.0,368632017600.0,7979048,KOSDAQ
2024-11-15,42550.0,43800.0,38650.0,40800.0,97090.0,3908884550.0,325545158400.0,7979048,KOSDAQ
2024-11-27,44750.0,44750.0,42800.0,42800.0,17628.0,767442500.0,341503254400.0,7979048,KOSDAQ
```

Backtest:

| window | peak/high | peak date | trough/low | trough date | MFE | MAE |
|---|---:|---|---:|---|---:|---:|
| 30 calendar days | 91500 | 2024-06-11 | 65400 | 2024-05-31 | +39.91% | +0.00% |
| 90 calendar days | 91500 | 2024-06-11 | 44800 | 2024-08-05 | +39.91% | -31.50% |
| 180 calendar days | 91500 | 2024-06-11 | 38650 | 2024-11-15 | +39.91% | -40.90% |

Interpretation:

```text
372170 is the classic C11 high-MFE/high-MAE trap.
The first month looks usable, but the 90D/180D path shows that the orderbook thesis was not yet durable enough to hold.
Without verified customer/order/backlog conversion, this should be Stage2-Guarded or 4B/high-MAE watch, not Green.
```

### 6.3 `299030` 하나기술 — orderbook thesis break / relief failure

Trigger:

```text
trigger_date = 2024-06-20
trigger_type = Stage2-FalsePositive-Candidate
trigger_family = battery_equipment_orderbook_thesis_break_relief_failure
entry_date = 2024-06-21
entry_price = 48350.0
entry_price_type = next_tradable_open_after_gap_down
```

Relevant Stock-Web rows:

```csv
d,o,h,l,c,v,a,mc,s,m
2024-06-20,57400.0,57800.0,56000.0,56000.0,103236.0,5728279000.0,456993992000.0,8160607,KOSDAQ
2024-06-21,48350.0,53800.0,48350.0,50700.0,590368.0,30018518200.0,413742774900.0,8160607,KOSDAQ
2024-06-24,49050.0,49600.0,40550.0,41150.0,800557.0,35003545750.0,335808978050.0,8160607,KOSDAQ
2024-07-19,30800.0,31550.0,30500.0,31550.0,56577.0,1748527350.0,257782209150.0,8170593,KOSDAQ
2024-08-05,30150.0,30550.0,24350.0,25450.0,167450.0,4567850200.0,207941591850.0,8170593,KOSDAQ
2024-11-15,20300.0,21800.0,18500.0,20600.0,102683.0,2077357750.0,164695146000.0,7994910,KOSDAQ
2024-12-09,17760.0,18500.0,16760.0,16860.0,57836.0,1000907410.0,134794182600.0,7994910,KOSDAQ
2024-12-18,18820.0,19540.0,18820.0,19400.0,22777.0,438988660.0,155101254000.0,7994910,KOSDAQ
```

Backtest:

| window | peak/high | peak date | trough/low | trough date | MFE | MAE |
|---|---:|---|---:|---|---:|---:|
| 30 calendar days | 53800 | 2024-06-21 | 30500 | 2024-07-19 | +11.27% | -36.92% |
| 90 calendar days | 53800 | 2024-06-21 | 24350 | 2024-08-05 | +11.27% | -49.64% |
| 180 calendar days | 53800 | 2024-06-21 | 16760 | 2024-12-09 | +11.27% | -65.34% |

Interpretation:

```text
299030 is the clean false-positive / thesis-break case.
The entry was a relief attempt after a sharp break, but remaining MFE was small and MAE became extreme.
This should not be Stage2/Green; it belongs in 4B/high-MAE watch or 4C review unless hard orderbook repair evidence arrives.
```

---

## 7. Machine-readable trigger JSONL

```jsonl
{"row_type":"trigger","research_id":"R3L73_C11_BATTERY_ORDERBOOK_ROUTER","round":"R3","loop":73,"large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C11_BATTERY_ORDERBOOK_RERATING","fine_archetype_id":"BATTERY_EQUIPMENT_ORDERBOOK_RERATING_AND_HIGH_MAE_ROUTER","symbol":"137400","name":"피엔티","trigger_type":"Stage2-Actionable-Guarded","trigger_family":"battery_equipment_orderbook_rerating_low_initial_mae","trigger_date":"2024-05-28","entry_date":"2024-05-29","entry_price":53600.0,"entry_price_type":"next_tradable_open","price_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","mfe_30d_pct":66.98,"mae_30d_pct":-1.12,"mfe_90d_pct":66.98,"mae_90d_pct":-14.27,"mfe_180d_pct":66.98,"mae_180d_pct":-25.84,"peak_price_180d":89500.0,"peak_date_180d":"2024-06-19","trough_price_180d":39750.0,"trough_date_180d":"2024-11-15","calibration_usable":true,"case_polarity":"positive_guarded","evidence_url_pending":true,"source_proxy_only":true,"non_price_evidence_strength":"medium_pending_url_repair","price_only_blowoff":false,"expected_stage_current_profile":"Stage2-Actionable-Guarded_to_Yellow_if_orderbook_bridge_repaired","residual_error_type":"strong_early_mfe_low_mae_but_green_requires_backlog_customer_margin_bridge"}
{"row_type":"trigger","research_id":"R3L73_C11_BATTERY_ORDERBOOK_ROUTER","round":"R3","loop":73,"large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C11_BATTERY_ORDERBOOK_RERATING","fine_archetype_id":"BATTERY_EQUIPMENT_ORDERBOOK_RERATING_AND_HIGH_MAE_ROUTER","symbol":"372170","name":"윤성에프앤씨","trigger_type":"Stage2-Actionable-Guarded","trigger_family":"battery_mixing_equipment_orderbook_relief_rally","trigger_date":"2024-05-30","entry_date":"2024-05-31","entry_price":65400.0,"entry_price_type":"next_tradable_open","price_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","mfe_30d_pct":39.91,"mae_30d_pct":0.00,"mfe_90d_pct":39.91,"mae_90d_pct":-31.50,"mfe_180d_pct":39.91,"mae_180d_pct":-40.90,"peak_price_180d":91500.0,"peak_date_180d":"2024-06-11","trough_price_180d":38650.0,"trough_date_180d":"2024-11-15","calibration_usable":true,"case_polarity":"counterexample_high_mfe_high_mae","evidence_url_pending":true,"source_proxy_only":true,"non_price_evidence_strength":"low_pending_url_repair","price_only_blowoff":false,"expected_stage_current_profile":"Stage2-Guarded_or_4B_high_MAE_watch_until_orderbook_bridge_repaired","residual_error_type":"first_month_mfe_overwhelmed_by_90d_180d_mae_without_durable_orderbook_bridge"}
{"row_type":"trigger","research_id":"R3L73_C11_BATTERY_ORDERBOOK_ROUTER","round":"R3","loop":73,"large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C11_BATTERY_ORDERBOOK_RERATING","fine_archetype_id":"BATTERY_EQUIPMENT_ORDERBOOK_RERATING_AND_HIGH_MAE_ROUTER","symbol":"299030","name":"하나기술","trigger_type":"Stage2-FalsePositive-Candidate","trigger_family":"battery_equipment_orderbook_thesis_break_relief_failure","trigger_date":"2024-06-20","entry_date":"2024-06-21","entry_price":48350.0,"entry_price_type":"next_tradable_open_after_gap_down","price_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","mfe_30d_pct":11.27,"mae_30d_pct":-36.92,"mfe_90d_pct":11.27,"mae_90d_pct":-49.64,"mfe_180d_pct":11.27,"mae_180d_pct":-65.34,"peak_price_180d":53800.0,"peak_date_180d":"2024-06-21","trough_price_180d":16760.0,"trough_date_180d":"2024-12-09","calibration_usable":true,"case_polarity":"counterexample_thesis_break","evidence_url_pending":true,"source_proxy_only":true,"non_price_evidence_strength":"low_pending_url_repair","price_only_blowoff":false,"expected_stage_current_profile":"blocked_Stage2_or_4B_4C_high_MAE_watch","residual_error_type":"relief_attempt_after_orderbook_thesis_break_had_low_mfe_extreme_mae"}
```

---

## 8. Score simulation and raw component breakdown

This is shadow-only and does not change production scoring.

| symbol | orderbook quality | customer visibility | delivery/margin bridge | market mispricing | valuation rerating | call-off risk control | information confidence | shadow total | intended route |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| `137400` | 14 | 12 | 10 | 13 | 12 | 8 | 7 | 76 | Stage2-Guarded / Yellow after orderbook evidence repair |
| `372170` | 9 | 7 | 5 | 11 | 10 | 3 | 5 | 50 | Stage2-Guarded or 4B/high-MAE watch |
| `299030` | 4 | 4 | 2 | 5 | 4 | 1 | 4 | 24 | blocked Stage2 / 4B-to-4C watch |

### Current calibrated profile stress test

The current calibrated profile already blocks pure price-only blowoff.  
The remaining C11 risk is **orderbook bridge quality**:

```text
C11 cleaner path:
  battery-equipment exposure
  + strong MFE
  + low early MAE
  + URL-repaired backlog/customer/delivery/margin bridge
  => Stage2-Actionable / Stage3-Yellow, possible Green after proof

C11 false-positive path:
  equipment name has early MFE
  + source-proxy-only orderbook evidence
  + 90D MAE <= -30% or 180D MAE <= -40%
  => Stage2-Guarded or 4B/high-MAE watch; no Green

C11 thesis-break path:
  gap-down or relief attempt
  + weak MFE
  + 30D MAE <= -30%
  => block Stage2 and route to 4C watch unless hard repair evidence arrives
```

`137400` prevents overblocking.  
`372170` proves that first-month MFE alone is not enough.  
`299030` is the hard guardrail case: once the orderbook thesis is breaking, a relief candle should not be treated as a fresh Stage2.

---

## 9. Aggregate metrics

```json
{
  "row_type": "aggregate",
  "research_id": "R3L73_C11_BATTERY_ORDERBOOK_ROUTER",
  "round": "R3",
  "loop": 73,
  "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY",
  "canonical_archetype_id": "C11_BATTERY_ORDERBOOK_RERATING",
  "fine_archetype_id": "BATTERY_EQUIPMENT_ORDERBOOK_RERATING_AND_HIGH_MAE_ROUTER",
  "case_count": 3,
  "calibration_usable_case_count": 3,
  "positive_guarded_case_count": 1,
  "counterexample_count": 2,
  "new_symbol_count": 3,
  "source_proxy_only_count": 3,
  "evidence_url_pending_count": 3,
  "avg_mfe_30d_pct": 39.39,
  "avg_mae_30d_pct": -12.68,
  "avg_mfe_90d_pct": 39.39,
  "avg_mae_90d_pct": -31.80,
  "avg_mfe_180d_pct": 39.39,
  "avg_mae_180d_pct": -44.03,
  "max_mfe_180d_pct": 66.98,
  "worst_mae_180d_pct": -65.34
}
```

---

## 10. 4B proximity split

```json
{
  "row_type": "4b_split",
  "research_id": "R3L73_C11_BATTERY_ORDERBOOK_ROUTER",
  "stage2_positive_or_yellow_candidate": [
    {
      "symbol": "137400",
      "reason": "strong early MFE and contained 30D/90D MAE; Green still requires URL-repaired orderbook/customer/margin evidence"
    }
  ],
  "local_4b_watch": [
    {
      "symbol": "372170",
      "reason": "first-month MFE was strong, but 90D MAE reached -31.50% and 180D MAE reached -40.90%"
    },
    {
      "symbol": "299030",
      "reason": "relief attempt had only +11.27% MFE and -65.34% 180D MAE"
    }
  ],
  "full_4b_or_green_requires_non_price_evidence": [
    "named battery equipment customer",
    "order backlog or repeat order disclosure",
    "delivery schedule visibility",
    "call-off risk reduction",
    "gross margin / operating margin conversion"
  ]
}
```

---

## 11. Shadow rule candidate

```yaml
row_type: canonical_archetype_rule_candidate
canonical_archetype_id: C11_BATTERY_ORDERBOOK_RERATING
fine_archetype_id: BATTERY_EQUIPMENT_ORDERBOOK_RERATING_AND_HIGH_MAE_ROUTER
rule_name: C11_battery_equipment_orderbook_bridge_and_high_mae_router
production_scoring_changed: false
shadow_weight_only: true
```

### Proposed routing logic

```text
For C11 battery orderbook rerating cases:

Tier A: verified orderbook rerating
  Conditions:
    - orderbook / customer / delivery schedule evidence is URL-repaired
    - 30D/90D MAE is contained
    - MFE is not just one event candle
    - margin bridge is visible or later confirmed
  Routing:
    - Stage2-Actionable allowed
    - Stage3-Yellow allowed after evidence repair
    - Green only after orderbook and margin conversion evidence is verified

Tier B: equipment rally without durable bridge
  Conditions:
    - battery equipment exposure is plausible
    - early MFE is positive
    - evidence_url_pending or source_proxy_only remains true
    - 90D MAE <= -30% or 180D MAE <= -40%
  Routing:
    - Stage2-Actionable-Guarded at most
    - local 4B/high-MAE watch
    - no Green

Tier C: thesis-break relief attempt
  Conditions:
    - entry follows sharp gap-down or thesis break
    - MFE_30D < +15%
    - MAE_30D <= -30%
    - no repaired orderbook evidence
  Routing:
    - block Stage2
    - route to 4B/4C watch
    - count as counterexample
```

### Suggested shadow delta

```json
{
  "row_type": "shadow_weight",
  "axis": "c11_battery_equipment_orderbook_bridge_and_high_mae_router",
  "scope": "canonical_archetype_id:C11_BATTERY_ORDERBOOK_RERATING",
  "proposal": {
    "source_proxy_only_green_allowed": false,
    "orderbook_customer_margin_bridge_required_for_green": true,
    "equipment_rally_stage2_cap": "guarded_only_until_url_repair",
    "high_mae_watch_threshold_90d_pct": -30.0,
    "high_mae_watch_threshold_180d_pct": -40.0,
    "thesis_break_relief_blocks_stage2_if_mfe30_lt_15_and_mae30_lte_minus30": true,
    "positive_weight_blocked_until_url_repair": true
  },
  "confidence": "medium_low_until_url_repair",
  "apply_now": false,
  "reason": "One positive-guarded equipment orderbook case and two high-MAE counterexamples show that C11 should reward early low-MAE orderbook rerating only after URL-repaired backlog/customer/margin evidence, while blocking thesis-break relief attempts."
}
```

---

## 12. Residual contribution summary

```json
{
  "row_type": "residual_contribution",
  "research_id": "R3L73_C11_BATTERY_ORDERBOOK_ROUTER",
  "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY",
  "canonical_archetype_id": "C11_BATTERY_ORDERBOOK_RERATING",
  "contribution": "Adds three non-top-covered C11 battery-equipment/orderbook cases and separates a positive-guarded orderbook rerating path from equipment relief rallies and thesis-break cases with severe MAE. C11 Green should require URL-repaired orderbook, customer, delivery-schedule, and margin bridge evidence.",
  "positive_case_added": 1,
  "counterexample_case_added": 2,
  "new_symbol_count": 3,
  "data_quality_blocker": "All three non-price orderbook triggers require URL-level repair before positive weight promotion.",
  "guardrail_added": "C11 source_proxy_only equipment rallies with 90D MAE <= -30% or 180D MAE <= -40% should route to Stage2-Guarded or 4B/high-MAE watch; thesis-break relief attempts with weak MFE and large MAE should block Stage2."
}
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
    372170: false
    299030: false
  evidence_url_pending:
    137400: true
    372170: true
    299030: true
  source_proxy_only:
    137400: true
    372170: true
    299030: true
```

Limitations:

```text
- Price path is validated against Stock-Web tradable OHLC rows.
- Non-price evidence is not URL-repaired in this run.
- Therefore this artifact is useful for C11 residual shape and high-MAE guardrail design, but should not promote positive weights until filings/IR/disclosure/report data verifies orderbook durability, customer quality, delivery schedule, call-off risk, and margin conversion.
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
2. Preserve R3 / loop 73 metadata.
3. Add the cases to C11_BATTERY_ORDERBOOK_RERATING only if parser validation passes.
4. Treat all three non-price triggers as evidence_url_pending=true and source_proxy_only=true until URL-level evidence is repaired.
5. Do not use these rows for positive weight promotion until filings/IR/disclosure/report data verifies orderbook durability, customer quality, delivery schedule, call-off risk, and margin conversion.
6. Add a shadow-only rule candidate named C11_battery_equipment_orderbook_bridge_and_high_mae_router.
7. Do not loosen Stage3-Green.
8. Add C11-specific guards:
   - source_proxy_only -> no Green
   - equipment rally without repaired bridge -> Stage2-Guarded at most
   - 90D MAE <= -30% or 180D MAE <= -40% without repaired bridge -> local 4B/high-MAE watch
   - thesis-break relief attempt with MFE_30D < +15% and MAE_30D <= -30% -> block Stage2
   - Green requires repaired orderbook/customer/delivery/margin evidence
9. Keep production scoring unchanged unless later batch promotion logic independently marks this axis safe.
```

---

## 15. Next round state

```text
completed_round = R3
completed_loop = 73
next_round = R4
next_loop = 73
next_large_sector_hint = L4_MATERIALS_SPREAD_RESOURCE
```
