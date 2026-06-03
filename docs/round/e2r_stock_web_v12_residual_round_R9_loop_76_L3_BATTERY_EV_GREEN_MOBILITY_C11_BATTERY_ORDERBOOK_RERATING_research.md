# E2R Stock-Web v12 Residual Research — R9 Loop 76

```yaml
research_session: post_calibrated_sector_archetype_residual_research
mode: historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12
completed_round: R9
completed_loop: 76
next_round: R10
next_loop: 76
large_sector_id: L3_BATTERY_EV_GREEN_MOBILITY
canonical_archetype_id: C11_BATTERY_ORDERBOOK_RERATING
fine_archetype_id: BATTERY_EQUIPMENT_ORDERBOOK_CUSTOMER_DELIVERY_AND_WEAK_MFE_HIGH_MAE_ROUTER
output_file: e2r_stock_web_v12_residual_round_R9_loop_76_L3_BATTERY_EV_GREEN_MOBILITY_C11_BATTERY_ORDERBOOK_RERATING_research.md
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
completed_round = R8
completed_loop  = 76
large_sector_id = L8_PLATFORM_CONTENT_SW_SECURITY
canonical_archetype_id = C28_SOFTWARE_SECURITY_CONTRACT_RETENTION
```

Therefore:

```text
scheduled_round = R9
scheduled_loop  = 76
```

R9 permits:

```text
large_sector_id = L3_BATTERY_EV_GREEN_MOBILITY
or
large_sector_id = L9_CONSTRUCTION_REALESTATE_HOUSING
```

This run selects the battery branch:

```text
large_sector_id = L3_BATTERY_EV_GREEN_MOBILITY
canonical_archetype_id = C11_BATTERY_ORDERBOOK_RERATING
fine_archetype_id = BATTERY_EQUIPMENT_ORDERBOOK_CUSTOMER_DELIVERY_AND_WEAK_MFE_HIGH_MAE_ROUTER
```

This is a valid R9/L3 pairing.

---

## 1. Why this R9/C11 run

The no-repeat ledger shows C11 remains a major battery-orderbook archetype, but recent coverage is concentrated in a few heavily repeated cell/material names:

```text
C11_BATTERY_ORDERBOOK_RERATING:
  rows: 79
  symbols: 21
  date_range: 2022-08-17~2024-07-22
  good/bad S2: 31/9
  4B/4C: 17/5
  URL/proxy: 12/12
  top covered symbols: 247540(11), 003670(8), 393890(8), 222080(6), 348370(6), 066970(5)
```

This file avoids those top-covered symbols and tests battery equipment / inspection / auxiliary-equipment orderbook cases:

```text
137400 피엔티
302430 이노메트리
299030 하나기술
290670 대보마그네틱
```

Research question:

```text
Can C11 separate a real equipment orderbook rerating from equipment-order labels where the customer/orderbook story exists, but delivery timing, customer acceptance, margin, cash collection, and capex call-off are not repaired?
```

C11 is an orderbook bridge. A battery-equipment order is the contract on the wall; Stage2 needs the machine shipped, accepted, invoiced, and converted into gross margin. If customer capex pauses or acceptance slips, the contract becomes a warehouse echo rather than revenue.

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
| `137400` | 피엔티 | active_like / KOSDAQ GLOBAL | no 2024 overlap; latest listed candidate 2019-05-30 | true |
| `302430` | 이노메트리 | active_like / KOSDAQ | no 2024 overlap; latest listed candidate 2020-01-21 | true |
| `299030` | 하나기술 | active_like / KOSDAQ | no 2024 overlap; latest listed candidate 2021-04-13 | true |
| `290670` | 대보마그네틱 | active_like / KOSDAQ | no 2024 overlap; latest listed candidate 2019-11-26 | true |

Profile caveat:

```text
Stock-Web OHLC is raw/unadjusted marcap data.
These cases are calibration-safe for the selected 2024 30D/90D/180D windows because no listed corporate-action candidate overlaps each entry~D+180 test window.
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
The Stock-Web price path is fully validated, but company-level customer identity, signed order size, delivery schedule, customer acceptance, revenue recognition, warranty/installation risk, backlog quality, gross margin, working capital, and cash collection evidence still require later URL repair through filings, IR decks, order disclosures, customer/capex data, or sell-side reports before production weight promotion.
```

C11 interpretation used here:

```text
C11 is not simply “battery equipment stock rose.”
It asks whether the orderbook becomes executable economics:
- customer quality and order size,
- delivery and acceptance schedule,
- revenue recognition and margin,
- installation / warranty risk,
- working capital and cash collection,
- customer capex call-off risk,
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
302430 + C11_BATTERY_ORDERBOOK_RERATING -> no direct match found
299030 + C11_BATTERY_ORDERBOOK_RERATING -> no direct match found
290670 + C11_BATTERY_ORDERBOOK_RERATING -> no direct match found
```

Novelty accounting:

```json
{
  "new_symbol_count": 4,
  "minimum_new_symbol_count": 2,
  "positive_guarded_case_count": 1,
  "counterexample_count": 3,
  "new_independent_case_ratio": 1.00,
  "duplicate_status": "pass",
  "data_quality_status": "source_proxy_only_non_price_evidence"
}
```

---

## 5. Case design

| case_id | symbol | trigger family | research role |
|---|---|---|---|
| `R9L76_C11_137400_20240529` | `137400` 피엔티 | battery equipment orderbook/customer delivery high-MFE path | positive-guarded |
| `R9L76_C11_302430_20240311` | `302430` 이노메트리 | battery inspection equipment orderbook first-window MFE / later high MAE | counterexample |
| `R9L76_C11_299030_20240311` | `299030` 하나기술 | battery formation/assembly equipment weak-MFE extreme-MAE path | counterexample |
| `R9L76_C11_290670_20240311` | `290670` 대보마그네틱 | battery auxiliary equipment recovery weak-MFE extreme-MAE path | counterexample |

The intended residual:

```text
C11 should separate:
1. equipment orderbook paths where MFE is large enough to preserve Stage2-Guarded;
2. inspection-equipment labels where first-window MFE appears but 180D MAE blocks Yellow/Green;
3. formation/assembly-equipment labels where MFE stays weak and extreme MAE follows;
4. auxiliary-equipment labels where the orderbook/recovery story fails without customer acceptance and margin evidence.
```

---

## 6. Stock-Web OHLC and backtest

### 6.1 `137400` 피엔티 — battery equipment orderbook/customer delivery high-MFE guarded path

Trigger:

```text
trigger_date = 2024-05-28
trigger_type = Stage2-Actionable-Guarded
trigger_family = battery_equipment_orderbook_customer_delivery_high_mfe_later_drawdown
entry_date = 2024-05-29
entry_price = 53600.0
entry_price_type = next_tradable_open_after_battery_equipment_orderbook_delivery_burst
```

Relevant Stock-Web rows:

```csv
d,o,h,l,c,v,a,mc,s,m
2024-05-28,50200.0,50300.0,48500.0,49000.0,364512.0,17970447800.0,1114318702000.0,22741198,KOSDAQ GLOBAL
2024-05-29,53600.0,62500.0,53000.0,60300.0,5484629.0,325084117200.0,1371294239400.0,22741198,KOSDAQ GLOBAL
2024-06-05,72000.0,78500.0,70600.0,74800.0,2451096.0,183718230600.0,1701041610400.0,22741198,KOSDAQ GLOBAL
2024-06-19,85100.0,89500.0,84000.0,84500.0,690736.0,59660038400.0,1921631231000.0,22741198,KOSDAQ GLOBAL
2024-08-05,51100.0,53400.0,45950.0,49200.0,837840.0,42067866100.0,1168159831200.0,23743086,KOSDAQ GLOBAL
2024-11-15,41850.0,42650.0,39750.0,41150.0,616771.0,25360281350.0,977027988900.0,23743086,KOSDAQ GLOBAL
```

Backtest:

| window | peak/high | peak date | trough/low | trough date | MFE | MAE |
|---|---:|---|---:|---|---:|---:|
| 30 calendar days | 89500 | 2024-06-19 | 53000 | 2024-05-29 | +66.98% | -1.12% |
| 90 calendar days | 89500 | 2024-06-19 | 45950 | 2024-08-05 | +66.98% | -14.27% |
| 180 calendar days | 89500 | 2024-06-19 | 39750 | 2024-11-15 | +66.98% | -25.84% |

Interpretation:

```text
137400 is the C11 positive-guarded holdout.
The equipment orderbook path produced large MFE, so the router should not blanket-block battery equipment.
However, later drawdown widened materially. Yellow/Green should require URL-repaired customer order, delivery, acceptance, revenue recognition, margin, and cash collection evidence.
```

### 6.2 `302430` 이노메트리 — battery inspection equipment first-window MFE / later high-MAE branch

Trigger:

```text
trigger_date = 2024-03-08
trigger_type = Stage2-FalsePositive-Candidate
trigger_family = battery_inspection_equipment_orderbook_first_window_mfe_later_high_mae
entry_date = 2024-03-11
entry_price = 12750.0
entry_price_type = next_tradable_open_after_battery_inspection_equipment_orderbook_spike
```

Relevant Stock-Web rows:

```csv
d,o,h,l,c,v,a,mc,s,m
2024-03-08,10900.0,13850.0,10750.0,13010.0,2729445.0,35054163430.0,127930036080.0,9833208,KOSDAQ
2024-03-11,12750.0,12960.0,12050.0,12080.0,390761.0,4860967340.0,118785152640.0,9833208,KOSDAQ
2024-03-12,12120.0,15260.0,11940.0,13980.0,6039239.0,86643415290.0,137468247840.0,9833208,KOSDAQ
2024-04-09,11800.0,11890.0,11500.0,11560.0,38200.0,444341220.0,113671884480.0,9833208,KOSDAQ
2024-05-31,10690.0,10870.0,10400.0,10710.0,21834.0,233660290.0,105313657680.0,9833208,KOSDAQ
2024-08-06,7930.0,9620.0,7900.0,8720.0,54193.0,474780330.0,85745573760.0,9833208,KOSDAQ
```

Backtest:

| window | peak/high | peak date | trough/low | trough date | MFE | MAE |
|---|---:|---|---:|---|---:|---:|
| 30 calendar days | 15260 | 2024-03-12 | 11500 | 2024-04-09 | +19.69% | -9.80% |
| 90 calendar days | 15260 | 2024-03-12 | 10400 | 2024-05-31 | +19.69% | -18.43% |
| 180 calendar days | 15260 | 2024-03-12 | 7900 | 2024-08-06 | +19.69% | -38.04% |

Interpretation:

```text
302430 is the first-window-MFE / later-high-MAE warning.
Inspection-equipment orderbook relevance produced a near +20% MFE, but the 180D drawdown crossed a hard guardrail.
This should cap at Stage2-Guarded or local 4B watch until customer acceptance, delivery, revenue recognition, and margin evidence are repaired.
```

### 6.3 `299030` 하나기술 — battery formation/assembly equipment weak-MFE extreme-MAE path

Trigger:

```text
trigger_date = 2024-03-08
trigger_type = Stage2-FalsePositive-Candidate
trigger_family = battery_formation_assembly_equipment_orderbook_weak_mfe_extreme_mae
entry_date = 2024-03-11
entry_price = 67900.0
entry_price_type = next_tradable_open_after_battery_equipment_orderbook_spike
```

Relevant Stock-Web rows:

```csv
d,o,h,l,c,v,a,mc,s,m
2024-03-08,64000.0,73100.0,61400.0,67200.0,1377695.0,95170104800.0,548392790400.0,8160607,KOSDAQ
2024-03-11,67900.0,68200.0,65300.0,66000.0,230075.0,15362079200.0,538600062000.0,8160607,KOSDAQ
2024-03-12,66000.0,70400.0,66000.0,68100.0,336558.0,23072862300.0,555737336700.0,8160607,KOSDAQ
2024-04-09,57100.0,58400.0,56100.0,56300.0,47130.0,2680527300.0,459442174100.0,8160607,KOSDAQ
2024-05-31,54500.0,56800.0,52700.0,53000.0,198430.0,10750358100.0,432512171000.0,8160607,KOSDAQ
2024-08-05,30150.0,30550.0,24350.0,25450.0,167450.0,4567850200.0,207941591850.0,8170593,KOSDAQ
```

Backtest:

| window | peak/high | peak date | trough/low | trough date | MFE | MAE |
|---|---:|---|---:|---|---:|---:|
| 30 calendar days | 70400 | 2024-03-12 | 56100 | 2024-04-09 | +3.68% | -17.38% |
| 90 calendar days | 70400 | 2024-03-12 | 52700 | 2024-05-31 | +3.68% | -22.39% |
| 180 calendar days | 70400 | 2024-03-12 | 24350 | 2024-08-05 | +3.68% | -64.14% |

Interpretation:

```text
299030 is a hard C11 weak-MFE failure.
The orderbook/equipment label was already crowded by entry: forward MFE stayed below +4%, while 180D MAE reached -64.14%.
This should block Stage2 or route to 4B/4C high-MAE watch unless a fresh, later trigger repairs customer delivery, cash collection, and margin evidence before entry.
```

### 6.4 `290670` 대보마그네틱 — battery auxiliary equipment recovery weak-MFE extreme-MAE path

Trigger:

```text
trigger_date = 2024-03-08
trigger_type = Stage2-FalsePositive-Candidate
trigger_family = battery_magnetic_separator_orderbook_recovery_weak_mfe_extreme_mae
entry_date = 2024-03-11
entry_price = 31600.0
entry_price_type = next_tradable_open_after_battery_aux_equipment_orderbook_recovery_spike
```

Relevant Stock-Web rows:

```csv
d,o,h,l,c,v,a,mc,s,m
2024-03-08,30200.0,33200.0,30200.0,30850.0,244986.0,7789298850.0,242408811000.0,7857660,KOSDAQ
2024-03-11,31600.0,31600.0,30400.0,30950.0,58727.0,1810890100.0,243194577000.0,7857660,KOSDAQ
2024-03-12,31050.0,32600.0,31000.0,32350.0,132001.0,4238969900.0,254195301000.0,7857660,KOSDAQ
2024-04-09,27100.0,27700.0,27000.0,27000.0,19031.0,517850050.0,212156820000.0,7857660,KOSDAQ
2024-05-30,23350.0,23500.0,23000.0,23150.0,17214.0,398669500.0,181904829000.0,7857660,KOSDAQ
2024-08-05,19490.0,19490.0,15400.0,16010.0,90510.0,1549303020.0,125801136600.0,7857660,KOSDAQ
```

Backtest:

| window | peak/high | peak date | trough/low | trough date | MFE | MAE |
|---|---:|---|---:|---|---:|---:|
| 30 calendar days | 32600 | 2024-03-12 | 27000 | 2024-04-09 | +3.16% | -14.56% |
| 90 calendar days | 32600 | 2024-03-12 | 23000 | 2024-05-30 | +3.16% | -27.22% |
| 180 calendar days | 32600 | 2024-03-12 | 15400 | 2024-08-05 | +3.16% | -51.27% |

Interpretation:

```text
290670 is the auxiliary-equipment weak-MFE failure.
The battery equipment recovery label existed, but the price path never confirmed the orderbook story and later MAE became extreme.
This should block Stage2 or route to 4B/4C watch until customer acceptance, delivery schedule, margin, and cash conversion evidence is repaired.
```

---

## 7. Machine-readable trigger JSONL

```jsonl
{"row_type":"trigger","research_id":"R9L76_C11_BATTERY_EQUIPMENT_ORDERBOOK_ROUTER","round":"R9","loop":76,"large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C11_BATTERY_ORDERBOOK_RERATING","fine_archetype_id":"BATTERY_EQUIPMENT_ORDERBOOK_CUSTOMER_DELIVERY_AND_WEAK_MFE_HIGH_MAE_ROUTER","symbol":"137400","name":"피엔티","trigger_type":"Stage2-Actionable-Guarded","trigger_family":"battery_equipment_orderbook_customer_delivery_high_mfe_later_drawdown","trigger_date":"2024-05-28","entry_date":"2024-05-29","entry_price":53600.0,"entry_price_type":"next_tradable_open_after_battery_equipment_orderbook_delivery_burst","price_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","mfe_30d_pct":66.98,"mae_30d_pct":-1.12,"mfe_90d_pct":66.98,"mae_90d_pct":-14.27,"mfe_180d_pct":66.98,"mae_180d_pct":-25.84,"peak_price_180d":89500.0,"peak_date_180d":"2024-06-19","trough_price_180d":39750.0,"trough_date_180d":"2024-11-15","calibration_usable":true,"case_polarity":"positive_guarded_high_mfe_later_drawdown","evidence_url_pending":true,"source_proxy_only":true,"non_price_evidence_strength":"medium_pending_url_repair","price_only_blowoff":false,"expected_stage_current_profile":"Stage2-Guarded_to_Yellow_only_if_customer_order_delivery_margin_bridge_repaired","residual_error_type":"battery_equipment_orderbook_path_had_large_mfe_but_later_mae_requires_url_repaired_customer_delivery_and_margin_bridge_before_green"}
{"row_type":"trigger","research_id":"R9L76_C11_BATTERY_EQUIPMENT_ORDERBOOK_ROUTER","round":"R9","loop":76,"large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C11_BATTERY_ORDERBOOK_RERATING","fine_archetype_id":"BATTERY_EQUIPMENT_ORDERBOOK_CUSTOMER_DELIVERY_AND_WEAK_MFE_HIGH_MAE_ROUTER","symbol":"302430","name":"이노메트리","trigger_type":"Stage2-FalsePositive-Candidate","trigger_family":"battery_inspection_equipment_orderbook_first_window_mfe_later_high_mae","trigger_date":"2024-03-08","entry_date":"2024-03-11","entry_price":12750.0,"entry_price_type":"next_tradable_open_after_battery_inspection_equipment_orderbook_spike","price_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","mfe_30d_pct":19.69,"mae_30d_pct":-9.8,"mfe_90d_pct":19.69,"mae_90d_pct":-18.43,"mfe_180d_pct":19.69,"mae_180d_pct":-38.04,"peak_price_180d":15260.0,"peak_date_180d":"2024-03-12","trough_price_180d":7900.0,"trough_date_180d":"2024-08-06","calibration_usable":true,"case_polarity":"counterexample_first_window_mfe_later_high_mae","evidence_url_pending":true,"source_proxy_only":true,"non_price_evidence_strength":"low_pending_url_repair","price_only_blowoff":false,"expected_stage_current_profile":"Stage2-Guarded_or_local_4B_watch_until_customer_order_acceptance_margin_bridge_repaired","residual_error_type":"battery_inspection_equipment_orderbook_label_had_first_window_mfe_but_180d_mae_blocks_yellow_green_without_delivery_and_margin_bridge"}
{"row_type":"trigger","research_id":"R9L76_C11_BATTERY_EQUIPMENT_ORDERBOOK_ROUTER","round":"R9","loop":76,"large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C11_BATTERY_ORDERBOOK_RERATING","fine_archetype_id":"BATTERY_EQUIPMENT_ORDERBOOK_CUSTOMER_DELIVERY_AND_WEAK_MFE_HIGH_MAE_ROUTER","symbol":"299030","name":"하나기술","trigger_type":"Stage2-FalsePositive-Candidate","trigger_family":"battery_formation_assembly_equipment_orderbook_weak_mfe_extreme_mae","trigger_date":"2024-03-08","entry_date":"2024-03-11","entry_price":67900.0,"entry_price_type":"next_tradable_open_after_battery_equipment_orderbook_spike","price_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","mfe_30d_pct":3.68,"mae_30d_pct":-17.38,"mfe_90d_pct":3.68,"mae_90d_pct":-22.39,"mfe_180d_pct":3.68,"mae_180d_pct":-64.14,"peak_price_180d":70400.0,"peak_date_180d":"2024-03-12","trough_price_180d":24350.0,"trough_date_180d":"2024-08-05","calibration_usable":true,"case_polarity":"counterexample_weak_mfe_extreme_mae","evidence_url_pending":true,"source_proxy_only":true,"non_price_evidence_strength":"low_pending_url_repair","price_only_blowoff":false,"expected_stage_current_profile":"blocked_Stage2_or_4B_4C_high_MAE_watch_until_orderbook_delivery_cash_margin_bridge_repaired","residual_error_type":"battery_equipment_orderbook_label_had_weak_mfe_and_extreme_mae_without_customer_delivery_cash_margin_bridge"}
{"row_type":"trigger","research_id":"R9L76_C11_BATTERY_EQUIPMENT_ORDERBOOK_ROUTER","round":"R9","loop":76,"large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C11_BATTERY_ORDERBOOK_RERATING","fine_archetype_id":"BATTERY_EQUIPMENT_ORDERBOOK_CUSTOMER_DELIVERY_AND_WEAK_MFE_HIGH_MAE_ROUTER","symbol":"290670","name":"대보마그네틱","trigger_type":"Stage2-FalsePositive-Candidate","trigger_family":"battery_magnetic_separator_orderbook_recovery_weak_mfe_extreme_mae","trigger_date":"2024-03-08","entry_date":"2024-03-11","entry_price":31600.0,"entry_price_type":"next_tradable_open_after_battery_aux_equipment_orderbook_recovery_spike","price_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","mfe_30d_pct":3.16,"mae_30d_pct":-14.56,"mfe_90d_pct":3.16,"mae_90d_pct":-27.22,"mfe_180d_pct":3.16,"mae_180d_pct":-51.27,"peak_price_180d":32600.0,"peak_date_180d":"2024-03-12","trough_price_180d":15400.0,"trough_date_180d":"2024-08-05","calibration_usable":true,"case_polarity":"counterexample_weak_mfe_extreme_mae","evidence_url_pending":true,"source_proxy_only":true,"non_price_evidence_strength":"low_pending_url_repair","price_only_blowoff":false,"expected_stage_current_profile":"blocked_Stage2_or_4B_4C_high_MAE_watch_until_customer_acceptance_delivery_margin_bridge_repaired","residual_error_type":"battery_aux_equipment_orderbook_recovery_label_had_weak_mfe_and_extreme_mae_without_order_acceptance_delivery_margin_bridge"}
```

---

## 8. Score simulation and raw component breakdown

This is shadow-only and does not change production scoring.

| symbol | orderbook quality | customer / call-off risk | delivery / acceptance | revenue recognition | market mispricing | margin / cash conversion | information confidence | shadow total | intended route |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| `137400` | 12 | 7 | 8 | 7 | 13 | 6 | 6 | 59 | Stage2-Guarded / Yellow only after evidence repair |
| `302430` | 7 | 4 | 4 | 4 | 5 | 3 | 4 | 31 | Stage2-Guarded at most / local 4B watch |
| `299030` | 5 | 2 | 2 | 2 | 1 | 1 | 4 | 17 | blocked Stage2 / 4B-4C high-MAE watch |
| `290670` | 5 | 2 | 2 | 2 | 1 | 1 | 4 | 17 | blocked Stage2 / 4B-4C high-MAE watch |

### Current calibrated profile stress test

The current calibrated profile already blocks pure price-only blowoff.  
The remaining C11 issue is **battery equipment orderbook label without delivery, acceptance, and cash-margin conversion**:

```text
C11 high-MFE equipment path:
  battery equipment orderbook relevance
  + MFE_30D >= +50%
  + later MAE_180D widens beyond -20%
  + evidence remains source_proxy_only
  => Stage2-Guarded, Yellow only after order/delivery/margin evidence repair

C11 first-window-MFE later-MAE path:
  inspection/equipment relevance
  + MFE_30D >= +15%
  + MAE_180D <= -35%
  + customer acceptance bridge missing
  => Stage2-Guarded at most, local 4B watch, no Green

C11 weak-MFE extreme-MAE path:
  orderbook/equipment label exists
  + MFE_90D < +5%
  + MAE_90D <= -20% or MAE_180D <= -50%
  + no repaired delivery/cash/margin bridge
  => block Stage2 or route to 4B/4C high-MAE watch
```

`137400` prevents overblocking.  
`302430` shows why first-window MFE is not enough.  
`299030` and `290670` show why a battery-equipment orderbook label should not be promoted when forward MFE is weak and MAE becomes extreme.

---

## 9. Aggregate metrics

```json
{
  "row_type": "aggregate",
  "research_id": "R9L76_C11_BATTERY_EQUIPMENT_ORDERBOOK_ROUTER",
  "round": "R9",
  "loop": 76,
  "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY",
  "canonical_archetype_id": "C11_BATTERY_ORDERBOOK_RERATING",
  "fine_archetype_id": "BATTERY_EQUIPMENT_ORDERBOOK_CUSTOMER_DELIVERY_AND_WEAK_MFE_HIGH_MAE_ROUTER",
  "case_count": 4,
  "calibration_usable_case_count": 4,
  "positive_guarded_case_count": 1,
  "counterexample_count": 3,
  "new_symbol_count": 4,
  "source_proxy_only_count": 4,
  "evidence_url_pending_count": 4,
  "avg_mfe_30d_pct": 23.38,
  "avg_mae_30d_pct": -10.72,
  "avg_mfe_90d_pct": 23.38,
  "avg_mae_90d_pct": -20.58,
  "avg_mfe_180d_pct": 23.38,
  "avg_mae_180d_pct": -44.82,
  "max_mfe_180d_pct": 66.98,
  "worst_mae_180d_pct": -64.14
}
```

---

## 10. 4B proximity split

```json
{
  "row_type": "4b_split",
  "research_id": "R9L76_C11_BATTERY_EQUIPMENT_ORDERBOOK_ROUTER",
  "stage2_guarded_or_yellow_candidate": [
    {
      "symbol": "137400",
      "reason": "battery equipment orderbook path had +66.98% MFE, but 180D MAE reached -25.84%; requires order/delivery/margin evidence repair"
    }
  ],
  "stage2_guarded_or_local_4b_watch": [
    {
      "symbol": "302430",
      "reason": "inspection-equipment path had +19.69% first-window MFE but -38.04% 180D MAE"
    }
  ],
  "blocked_stage2_or_4c_watch": [
    {
      "symbol": "299030",
      "reason": "MFE stayed only +3.68%, while 180D MAE reached -64.14%"
    },
    {
      "symbol": "290670",
      "reason": "MFE stayed only +3.16%, while 180D MAE reached -51.27%"
    }
  ],
  "full_4b_or_green_requires_non_price_evidence": [
    "customer quality and order size",
    "delivery and customer acceptance schedule",
    "revenue recognition and installation risk",
    "warranty / commissioning risk",
    "working capital and cash collection",
    "gross margin and operating leverage conversion"
  ]
}
```

---

## 11. Shadow rule candidate

```yaml
row_type: canonical_archetype_rule_candidate
canonical_archetype_id: C11_BATTERY_ORDERBOOK_RERATING
fine_archetype_id: BATTERY_EQUIPMENT_ORDERBOOK_CUSTOMER_DELIVERY_AND_WEAK_MFE_HIGH_MAE_ROUTER
rule_name: C11_battery_equipment_orderbook_delivery_acceptance_and_weak_mfe_high_mae_router
production_scoring_changed: false
shadow_weight_only: true
```

### Proposed routing logic

```text
For C11 battery equipment / inspection / auxiliary-equipment orderbook cases:

Tier A: verified orderbook-to-delivery winner
  Conditions:
    - order size, customer quality, delivery schedule, acceptance, revenue recognition, and margin evidence are URL-repaired
    - MFE_90D >= +30%
    - MAE_90D > -12%
  Routing:
    - Stage2-Actionable or Stage2-Guarded allowed
    - Stage3-Yellow allowed after evidence repair
    - Green only after delivery / acceptance / margin bridge is verified

Tier B: high-MFE source-proxy equipment path with later drawdown
  Conditions:
    - MFE_30D >= +50%
    - MAE_180D <= -20%
    - evidence_url_pending or source_proxy_only remains true
  Routing:
    - Stage2-Guarded at most
    - no Green until evidence repair

Tier C: first-window-MFE / later-high-MAE inspection-equipment path
  Conditions:
    - MFE_30D >= +15%
    - MAE_180D <= -35%
    - no repaired delivery / customer acceptance / margin bridge
  Routing:
    - local 4B/high-MAE watch
    - no Yellow/Green

Tier D: weak-MFE extreme-MAE equipment label
  Conditions:
    - MFE_90D < +5%
    - MAE_90D <= -20% or MAE_180D <= -50%
    - bridge evidence remains unrepaired
  Routing:
    - block Stage2
    - route to 4B/4C high-MAE watch
```

### Suggested shadow delta

```json
{
  "row_type": "shadow_weight",
  "axis": "c11_battery_equipment_orderbook_delivery_acceptance_and_weak_mfe_high_mae_router",
  "scope": "canonical_archetype_id:C11_BATTERY_ORDERBOOK_RERATING",
  "proposal": {
    "source_proxy_only_green_allowed": false,
    "order_delivery_acceptance_margin_bridge_required_for_green": true,
    "verified_orderbook_mfe90_threshold_pct": 30.0,
    "verified_orderbook_mae90_min_pct": -12.0,
    "high_mfe_source_proxy_mfe30_threshold_pct": 50.0,
    "high_mfe_later_mae180_threshold_pct": -20.0,
    "first_window_mfe_threshold_30d_pct": 15.0,
    "later_high_mae_threshold_180d_pct": -35.0,
    "weak_mfe_threshold_90d_pct": 5.0,
    "weak_mfe_mae90_threshold_pct": -20.0,
    "weak_mfe_extreme_mae180_threshold_pct": -50.0,
    "positive_weight_blocked_until_url_repair": true
  },
  "confidence": "medium_low_until_url_repair",
  "apply_now": false,
  "reason": "One battery equipment high-MFE holdout and three inspection/formation/aux-equipment high-MAE failures show that C11 should require URL-repaired customer order, delivery, acceptance, revenue recognition, cash collection, and margin evidence before Yellow/Green."
}
```

---

## 12. Residual contribution summary

```json
{
  "row_type": "residual_contribution",
  "research_id": "R9L76_C11_BATTERY_EQUIPMENT_ORDERBOOK_ROUTER",
  "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY",
  "canonical_archetype_id": "C11_BATTERY_ORDERBOOK_RERATING",
  "contribution": "Adds four non-top-covered C11 battery equipment/inspection/auxiliary-equipment orderbook cases and separates a high-MFE equipment orderbook holdout from first-window-MFE later-high-MAE and weak-MFE extreme-MAE equipment-label failures. C11 Yellow/Green should require URL-repaired customer order, delivery, acceptance, revenue-recognition, working-capital, cash-collection, and margin-conversion evidence.",
  "positive_guarded_case_added": 1,
  "counterexample_case_added": 3,
  "new_symbol_count": 4,
  "new_independent_case_count": 4,
  "reused_case_count": 0,
  "same_archetype_new_symbol_count": 4,
  "same_archetype_new_trigger_family_count": 4,
  "new_trigger_family_count": 4,
  "current_profile_error_count": 3,
  "diversity_score_summary": {
    "new_symbol_bonus": 12,
    "counterexample_gap_bonus": 6,
    "residual_error_bonus": 15,
    "wrong_round_penalty": 0,
    "repeated_same_symbol_penalty": 0,
    "net_interpretive_score": 33
  },
  "loop_contribution_label": "canonical_archetype_rule_candidate",
  "do_not_propose_new_weight_delta": false,
  "data_quality_blocker": "All four non-price battery equipment orderbook triggers require URL-level repair before positive weight promotion.",
  "guardrail_added": "C11 source_proxy_only cases with MFE_90D < +5% and MAE_90D <= -20% or MAE_180D <= -50% should block Stage2; first-window-MFE cases with MAE_180D <= -35% should route to local 4B/high-MAE watch until delivery/acceptance/margin evidence is repaired."
}
```

One-line contribution:

```text
This loop adds 4 new independent cases, 3 counterexamples, and 3 residual errors for R9/L3_BATTERY_EV_GREEN_MOBILITY/C11_BATTERY_ORDERBOOK_RERATING.
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
    302430: false
    299030: false
    290670: false
  evidence_url_pending:
    137400: true
    302430: true
    299030: true
    290670: true
  source_proxy_only:
    137400: true
    302430: true
    299030: true
    290670: true
```

Limitations:

```text
- Price path is validated against Stock-Web tradable OHLC rows.
- Non-price evidence is not URL-repaired in this run.
- Therefore this artifact is useful for C11 battery equipment orderbook residual shape and weak-MFE/high-MAE guardrail design, but should not promote positive weights until filings, IR, order disclosures, customer/capex data, or reports verify order size, delivery schedule, acceptance, revenue recognition, cash collection, and margin conversion.
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
2. Preserve R9 / loop 76 metadata.
3. Add the cases to C11_BATTERY_ORDERBOOK_RERATING only if parser validation passes.
4. Treat all four non-price triggers as evidence_url_pending=true and source_proxy_only=true until URL-level evidence is repaired.
5. Do not use these rows for positive weight promotion until filings/IR/order-disclosure/customer-capex/report data verifies customer order size, delivery schedule, customer acceptance, revenue recognition, installation risk, working capital, cash collection, and margin conversion.
6. Add a shadow-only rule candidate named C11_battery_equipment_orderbook_delivery_acceptance_and_weak_mfe_high_mae_router.
7. Do not loosen Stage3-Green.
8. Add C11-specific guards:
   - source_proxy_only -> no Green
   - Green requires repaired customer order / delivery / acceptance / margin bridge
   - MFE_90D >= +30% and MAE_90D > -12% may remain Stage2-Actionable / Yellow watch after evidence repair
   - MFE_30D >= +50% and MAE_180D <= -20% -> Stage2-Guarded at most until evidence repair
   - MFE_30D >= +15% and MAE_180D <= -35% -> local 4B/high-MAE watch; no Yellow/Green
   - MFE_90D < +5% and MAE_90D <= -20% or MAE_180D <= -50% -> block Stage2 / 4B-4C watch
9. Keep production scoring unchanged unless later batch promotion logic independently marks this axis safe.
```

---

## 15. Next round state

```text
completed_round = R9
completed_loop = 76
next_round = R10
next_loop = 76
next_large_sector_hint = L9_CONSTRUCTION_REALESTATE_HOUSING
round_schedule_status = valid
round_sector_consistency = pass
```
