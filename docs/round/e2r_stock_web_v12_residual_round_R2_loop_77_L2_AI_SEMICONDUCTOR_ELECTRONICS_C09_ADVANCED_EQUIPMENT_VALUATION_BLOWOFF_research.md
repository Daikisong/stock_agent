# E2R Stock-Web v12 Residual Research — R2 Loop 77

```yaml
research_session: post_calibrated_sector_archetype_residual_research
mode: historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12
completed_round: R2
completed_loop: 77
next_round: R3
next_loop: 77
large_sector_id: L2_AI_SEMICONDUCTOR_ELECTRONICS
canonical_archetype_id: C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF
fine_archetype_id: METROLOGY_INSPECTION_DRY_PROCESS_EQUIPMENT_MFE_AND_HIGH_MAE_ROUTER
output_file: e2r_stock_web_v12_residual_round_R2_loop_77_L2_AI_SEMICONDUCTOR_ELECTRONICS_C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF_research.md
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
completed_round = R1
completed_loop  = 77
large_sector_id = L1_INDUSTRIALS_INFRA_DEFENSE_GRID
canonical_archetype_id = C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG
```

Therefore:

```text
scheduled_round = R2
scheduled_loop  = 77
```

R2 maps to:

```text
large_sector_id = L2_AI_SEMICONDUCTOR_ELECTRONICS
```

This run selects:

```text
canonical_archetype_id = C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF
fine_archetype_id = METROLOGY_INSPECTION_DRY_PROCESS_EQUIPMENT_MFE_AND_HIGH_MAE_ROUTER
```

This is a valid R2/L2 pairing.

---

## 1. Why this R2/C09 run

The no-repeat ledger shows C09 is moderately covered and concentrated in prior advanced-equipment names:

```text
C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF:
  rows: 56
  symbols: 17
  date_range: 2024-01-19~2024-07-11
  good/bad S2: 7/0
  4B/4C: 19/2
  URL/proxy: 6/6
  top covered symbols: 240810(8), 036930(7), 039030(4), 403870(4), 003160(3), 042700(3)
```

This file avoids those top-covered symbols and expands C09 into metrology / inspection / dry-process semicap cases:

```text
319660 피에스케이
140860 파크시스템스
348210 넥스틴
064290 인텍플러스
```

Research question:

```text
Can C09 separate real advanced-equipment order/customer-quality rerating from advanced-equipment labels where a first event candle exists but customer orders, delivery, acceptance, and margin conversion are not visible?
```

C09 is the sharp end of semiconductor capex. A tool can look like a precision scalpel, but the stock only deserves Stage2 if the tool is actually being bought, delivered, qualified, and recognized into margin. Without that bridge, the same scalpel becomes a price spike that cuts the entry.

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
| `319660` | 피에스케이 | active_like / KOSDAQ GLOBAL | no 2024 overlap; 2022 candidates outside window | true |
| `140860` | 파크시스템스 | active_like / KOSDAQ/KOSDAQ GLOBAL history | none listed | true |
| `348210` | 넥스틴 | active_like / KOSDAQ GLOBAL | no 2024 overlap; 2021 candidates outside window | true |
| `064290` | 인텍플러스 | active_like / KOSDAQ | none listed | true |

Profile caveat:

```text
Stock-Web OHLC is raw/unadjusted marcap data.
These cases are calibration-safe for the selected 2024/2025 forward windows because no listed corporate-action candidate overlaps each entry~D+180 test window.
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
The Stock-Web price path is fully validated, but company-level order quality, customer qualification, delivery schedule, tool acceptance, memory/foundry node exposure, advanced packaging or metrology pull-through, gross margin, and cash-flow conversion evidence still require later URL repair through filings, IR decks, customer data, order disclosures, or sell-side reports before production weight promotion.
```

C09 interpretation used here:

```text
C09 is not simply “semicap equipment stock rose.”
It asks whether advanced-equipment relevance becomes executable economics:
- customer order and qualification,
- delivery and tool acceptance,
- node / HBM / advanced-packaging / foundry bridge,
- backlog and revenue recognition,
- gross margin and operating leverage,
- and controlled MAE after the trigger.
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
140860 + C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF -> no direct match found
319660 + C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF -> no direct match found
348210 + C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF -> no direct match found
064290 + C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF -> no direct match found
```

Novelty accounting:

```json
{
  "new_symbol_count": 4,
  "minimum_new_symbol_count": 2,
  "positive_guarded_case_count": 2,
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
| `R2L77_C09_319660_20240304` | `319660` 피에스케이 | dry-process semicap equipment recovery / order cycle | positive-guarded |
| `R2L77_C09_140860_20240924` | `140860` 파크시스템스 | advanced metrology customer-quality late-MFE path | positive-guarded late-MFE |
| `R2L77_C09_348210_20240229` | `348210` 넥스틴 | advanced inspection event weak-MFE / high-MAE | weak-MFE counterexample |
| `R2L77_C09_064290_20240221` | `064290` 인텍플러스 | advanced inspection theme weak-MFE / extreme-MAE | hard counterexample |

The intended residual:

```text
C09 should separate:
1. semicap equipment paths where MFE compounds and MAE remains controlled;
2. advanced metrology paths where MFE arrives late but still respects a local MAE guard;
3. advanced inspection names where event relevance fails because MFE is weak and drawdown widens;
4. inspection-theme spikes where the absence of order quality and delivery evidence turns into extreme MAE.
```

---

## 6. Stock-Web OHLC and backtest

### 6.1 `319660` 피에스케이 — dry-process semicap equipment recovery positive-guarded path

Trigger:

```text
trigger_date = 2024-02-29
trigger_type = Stage2-Actionable-Guarded
trigger_family = dry_process_semicap_equipment_recovery_order_cycle_low_mae_rerating
entry_date = 2024-03-04
entry_price = 25850.0
entry_price_type = next_tradable_open_after_semicap_equipment_cycle_burst
```

Relevant Stock-Web rows:

```csv
d,o,h,l,c,v,a,mc,s,m
2024-02-29,22750.0,26150.0,22600.0,25400.0,1841557.0,45263787600.0,735754535600.0,28966714,KOSDAQ GLOBAL
2024-03-04,25850.0,26500.0,25300.0,26300.0,977588.0,25301826800.0,761824578200.0,28966714,KOSDAQ GLOBAL
2024-03-11,25200.0,25800.0,25200.0,25400.0,297810.0,7560717900.0,735754535600.0,28966714,KOSDAQ GLOBAL
2024-04-02,30600.0,31600.0,30400.0,31100.0,713290.0,22214201150.0,900864805400.0,28966714,KOSDAQ GLOBAL
2024-04-17,31650.0,33500.0,31200.0,32350.0,646080.0,21035948250.0,937073197900.0,28966714,KOSDAQ GLOBAL
2024-06-18,33900.0,36400.0,33900.0,36100.0,762778.0,27125838200.0,1045698375400.0,28966714,KOSDAQ GLOBAL
2024-07-11,38550.0,39100.0,38100.0,38600.0,214271.0,8266493650.0,1118115160400.0,28966714,KOSDAQ GLOBAL
2024-08-05,27050.0,27900.0,24000.0,25900.0,492071.0,13057771400.0,750237892600.0,28966714,KOSDAQ GLOBAL
```

Backtest:

| window | peak/high | peak date | trough/low | trough date | MFE | MAE |
|---|---:|---|---:|---|---:|---:|
| 30 calendar days | 31600 | 2024-04-02 | 25200 | 2024-03-11 | +22.24% | -2.51% |
| 90 calendar days | 33500 | 2024-04-17 | 25200 | 2024-03-11 | +29.59% | -2.51% |
| 180 calendar days | 39100 | 2024-07-11 | 24000 | 2024-08-05 | +51.26% | -7.16% |

Interpretation:

```text
319660 is a positive-guarded C09 equipment-cycle path.
The MFE expanded across 30D/90D/180D while MAE remained within a controlled band.
This can support Stage2-Guarded / Yellow-after-repair, but Green still requires URL-repaired customer order, delivery, qualification, and margin evidence.
```

### 6.2 `140860` 파크시스템스 — advanced metrology late-MFE low-MAE path

Trigger:

```text
trigger_date = 2024-09-23
trigger_type = Stage2-Actionable-Guarded
trigger_family = advanced_metrology_customer_quality_late_mfe_low_mae_rerating
entry_date = 2024-09-24
entry_price = 184700.0
entry_price_type = next_tradable_open_after_advanced_metrology_recovery_burst
```

Relevant Stock-Web rows:

```csv
d,o,h,l,c,v,a,mc,s,m
2024-09-23,174300.0,188500.0,174300.0,184700.0,46458.0,8593284300.0,1289872582300.0,6983609,KOSDAQ
2024-09-24,184700.0,192200.0,184700.0,192200.0,34662.0,6606044300.0,1342249649800.0,6983609,KOSDAQ
2024-10-11,184700.0,184800.0,181700.0,182000.0,19721.0,3606260800.0,1271016838000.0,6983609,KOSDAQ
2024-10-24,207000.0,219500.0,203000.0,207000.0,39879.0,8422852000.0,1445607063000.0,6983609,KOSDAQ
2024-11-07,208000.0,224000.0,208000.0,214500.0,41428.0,9030058500.0,1497984130500.0,6983609,KOSDAQ
2024-11-18,189000.0,191500.0,167000.0,173200.0,105354.0,18535575400.0,1209561078800.0,6983609,KOSDAQ
2025-01-22,248500.0,250000.0,237500.0,245500.0,16309.0,3982745500.0,1715450153500.0,6987577,KOSDAQ
2025-03-21,202500.0,218750.0,202500.0,214500.0,42044.0,8954090000.0,1499028316500.0,6988477,KOSDAQ
```

Backtest:

| window | peak/high | peak date | trough/low | trough date | MFE | MAE |
|---|---:|---|---:|---|---:|---:|
| 30 calendar days | 219500 | 2024-10-24 | 181700 | 2024-10-11 | +18.84% | -1.62% |
| 90 calendar days | 224000 | 2024-11-07 | 167000 | 2024-11-18 | +21.28% | -9.58% |
| 180 calendar days | 250000 | 2025-01-22 | 167000 | 2024-11-18 | +35.35% | -9.58% |

Interpretation:

```text
140860 is a late-MFE positive-guarded C09 case.
It prevents overblocking of high-quality metrology names: MFE arrived over a longer window while MAE stayed just inside a usable guardrail.
The case still should not become Green without URL-repaired customer mix, tool adoption, order backlog, and margin evidence.
```

### 6.3 `348210` 넥스틴 — advanced inspection weak-MFE high-MAE counterexample

Trigger:

```text
trigger_date = 2024-02-28
trigger_type = Stage2-FalsePositive-Candidate
trigger_family = advanced_inspection_equipment_event_weak_mfe_later_high_mae
entry_date = 2024-02-29
entry_price = 74300.0
entry_price_type = next_tradable_open_after_advanced_inspection_equipment_event
```

Relevant Stock-Web rows:

```csv
d,o,h,l,c,v,a,mc,s,m
2024-02-28,68900.0,76800.0,68700.0,74800.0,390433.0,29170757400.0,768819233600.0,10278332,KOSDAQ GLOBAL
2024-02-29,74300.0,76700.0,72700.0,76200.0,161009.0,12100616400.0,783208898400.0,10278332,KOSDAQ GLOBAL
2024-03-04,77800.0,77900.0,75300.0,76200.0,160323.0,12241646700.0,783208898400.0,10278332,KOSDAQ GLOBAL
2024-03-15,69900.0,71300.0,69300.0,70800.0,98621.0,6909999800.0,727705905600.0,10278332,KOSDAQ GLOBAL
2024-04-22,59300.0,60500.0,55500.0,56700.0,232134.0,13276495700.0,582781424400.0,10278332,KOSDAQ GLOBAL
2024-06-20,71900.0,76500.0,71600.0,74600.0,262019.0,19524337300.0,772659056000.0,10357360,KOSDAQ GLOBAL
2024-08-05,53400.0,53700.0,44900.0,45000.0,221835.0,10811232150.0,466081200000.0,10357360,KOSDAQ GLOBAL
```

Backtest:

| window | peak/high | peak date | trough/low | trough date | MFE | MAE |
|---|---:|---|---:|---|---:|---:|
| 30 calendar days | 77900 | 2024-03-04 | 69300 | 2024-03-15 | +4.85% | -6.73% |
| 90 calendar days | 77900 | 2024-03-04 | 55500 | 2024-04-22 | +4.85% | -25.30% |
| 180 calendar days | 77900 | 2024-03-04 | 44900 | 2024-08-05 | +4.85% | -39.57% |

Interpretation:

```text
348210 is the weak-MFE high-MAE inspection-equipment counterexample.
The advanced-equipment label existed, but forward MFE never expanded and the 90D/180D drawdown widened.
This should block Green and usually block Stage2 until customer order, qualification, delivery, and margin evidence is repaired.
```

### 6.4 `064290` 인텍플러스 — advanced inspection theme weak-MFE extreme-MAE branch

Trigger:

```text
trigger_date = 2024-02-20
trigger_type = Stage2-FalsePositive-Candidate
trigger_family = advanced_inspection_equipment_entry_theme_weak_mfe_extreme_mae
entry_date = 2024-02-21
entry_price = 36100.0
entry_price_type = next_tradable_open_after_advanced_inspection_equipment_theme_burst
```

Relevant Stock-Web rows:

```csv
d,o,h,l,c,v,a,mc,s,m
2024-02-20,31650.0,37300.0,31650.0,35750.0,2916729.0,103919044850.0,458885641500.0,12835962,KOSDAQ
2024-02-21,36100.0,38200.0,35050.0,36500.0,2037212.0,75062339300.0,468512613000.0,12835962,KOSDAQ
2024-03-07,40500.0,40900.0,37200.0,37500.0,664450.0,25565433350.0,481348575000.0,12835962,KOSDAQ
2024-03-14,36300.0,36450.0,34000.0,34300.0,553063.0,19090545400.0,440342096600.0,12837962,KOSDAQ
2024-04-23,30400.0,30600.0,29300.0,29300.0,140702.0,4190385500.0,376152286600.0,12837962,KOSDAQ
2024-05-21,26550.0,26950.0,25600.0,26150.0,223278.0,5806671700.0,336392606300.0,12863962,KOSDAQ
2024-08-05,17860.0,18140.0,14810.0,15150.0,248502.0,4024372280.0,194889024300.0,12863962,KOSDAQ
```

Backtest:

| window | peak/high | peak date | trough/low | trough date | MFE | MAE |
|---|---:|---|---:|---|---:|---:|
| 30 calendar days | 40900 | 2024-03-07 | 34000 | 2024-03-14 | +13.30% | -5.82% |
| 90 calendar days | 40900 | 2024-03-07 | 25600 | 2024-05-21 | +13.30% | -29.09% |
| 180 calendar days | 40900 | 2024-03-07 | 14810 | 2024-08-05 | +13.30% | -58.98% |

Interpretation:

```text
064290 is the hard C09 high-MAE counterexample.
Initial MFE existed, but it was not enough to compensate for the later collapse.
This should route to local 4B/4C high-MAE watch unless a later independent trigger repairs order quality, tool acceptance, delivery, and margin evidence.
```

---

## 7. Machine-readable trigger JSONL

```jsonl
{"row_type":"trigger","research_id":"R2L77_C09_ADVANCED_EQUIPMENT_ROUTER","round":"R2","loop":77,"large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF","fine_archetype_id":"METROLOGY_INSPECTION_DRY_PROCESS_EQUIPMENT_MFE_AND_HIGH_MAE_ROUTER","symbol":"319660","name":"피에스케이","trigger_type":"Stage2-Actionable-Guarded","trigger_family":"dry_process_semicap_equipment_recovery_order_cycle_low_mae_rerating","trigger_date":"2024-02-29","entry_date":"2024-03-04","entry_price":25850.0,"entry_price_type":"next_tradable_open_after_semicap_equipment_cycle_burst","price_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","mfe_30d_pct":22.24,"mae_30d_pct":-2.51,"mfe_90d_pct":29.59,"mae_90d_pct":-2.51,"mfe_180d_pct":51.26,"mae_180d_pct":-7.16,"peak_price_180d":39100.0,"peak_date_180d":"2024-07-11","trough_price_180d":24000.0,"trough_date_180d":"2024-08-05","calibration_usable":true,"case_polarity":"positive_guarded_low_mae_semicap_equipment","evidence_url_pending":true,"source_proxy_only":true,"non_price_evidence_strength":"medium_pending_url_repair","price_only_blowoff":false,"expected_stage_current_profile":"Stage2-Guarded_to_Yellow_if_customer_order_delivery_margin_bridge_repaired","residual_error_type":"semicap_equipment_cycle_path_had_persistent_mfe_and_controlled_mae_but_green_requires_url_repaired_customer_order_delivery_margin_bridge"}
{"row_type":"trigger","research_id":"R2L77_C09_ADVANCED_EQUIPMENT_ROUTER","round":"R2","loop":77,"large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF","fine_archetype_id":"METROLOGY_INSPECTION_DRY_PROCESS_EQUIPMENT_MFE_AND_HIGH_MAE_ROUTER","symbol":"140860","name":"파크시스템스","trigger_type":"Stage2-Actionable-Guarded","trigger_family":"advanced_metrology_customer_quality_late_mfe_low_mae_rerating","trigger_date":"2024-09-23","entry_date":"2024-09-24","entry_price":184700.0,"entry_price_type":"next_tradable_open_after_advanced_metrology_recovery_burst","price_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","mfe_30d_pct":18.84,"mae_30d_pct":-1.62,"mfe_90d_pct":21.28,"mae_90d_pct":-9.58,"mfe_180d_pct":35.35,"mae_180d_pct":-9.58,"peak_price_180d":250000.0,"peak_date_180d":"2025-01-22","trough_price_180d":167000.0,"trough_date_180d":"2024-11-18","calibration_usable":true,"case_polarity":"positive_guarded_advanced_metrology_late_mfe","evidence_url_pending":true,"source_proxy_only":true,"non_price_evidence_strength":"medium_low_pending_url_repair","price_only_blowoff":false,"expected_stage_current_profile":"Stage2-Guarded_to_Yellow_if_metrology_customer_mix_order_margin_bridge_repaired","residual_error_type":"advanced_metrology_late_mfe_path_should_not_be_overblocked_but_green_requires_url_repaired_customer_quality_order_margin_bridge"}
{"row_type":"trigger","research_id":"R2L77_C09_ADVANCED_EQUIPMENT_ROUTER","round":"R2","loop":77,"large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF","fine_archetype_id":"METROLOGY_INSPECTION_DRY_PROCESS_EQUIPMENT_MFE_AND_HIGH_MAE_ROUTER","symbol":"348210","name":"넥스틴","trigger_type":"Stage2-FalsePositive-Candidate","trigger_family":"advanced_inspection_equipment_event_weak_mfe_later_high_mae","trigger_date":"2024-02-28","entry_date":"2024-02-29","entry_price":74300.0,"entry_price_type":"next_tradable_open_after_advanced_inspection_equipment_event","price_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","mfe_30d_pct":4.85,"mae_30d_pct":-6.73,"mfe_90d_pct":4.85,"mae_90d_pct":-25.3,"mfe_180d_pct":4.85,"mae_180d_pct":-39.57,"peak_price_180d":77900.0,"peak_date_180d":"2024-03-04","trough_price_180d":44900.0,"trough_date_180d":"2024-08-05","calibration_usable":true,"case_polarity":"counterexample_weak_mfe_high_mae","evidence_url_pending":true,"source_proxy_only":true,"non_price_evidence_strength":"low_pending_url_repair","price_only_blowoff":false,"expected_stage_current_profile":"blocked_Stage2_or_local_4B_high_MAE_watch_until_customer_order_acceptance_margin_bridge_repaired","residual_error_type":"advanced_inspection_equipment_label_had_weak_mfe_and_high_mae_without_customer_order_delivery_margin_bridge"}
{"row_type":"trigger","research_id":"R2L77_C09_ADVANCED_EQUIPMENT_ROUTER","round":"R2","loop":77,"large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF","fine_archetype_id":"METROLOGY_INSPECTION_DRY_PROCESS_EQUIPMENT_MFE_AND_HIGH_MAE_ROUTER","symbol":"064290","name":"인텍플러스","trigger_type":"Stage2-FalsePositive-Candidate","trigger_family":"advanced_inspection_equipment_entry_theme_weak_mfe_extreme_mae","trigger_date":"2024-02-20","entry_date":"2024-02-21","entry_price":36100.0,"entry_price_type":"next_tradable_open_after_advanced_inspection_equipment_theme_burst","price_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","mfe_30d_pct":13.3,"mae_30d_pct":-5.82,"mfe_90d_pct":13.3,"mae_90d_pct":-29.09,"mfe_180d_pct":13.3,"mae_180d_pct":-58.98,"peak_price_180d":40900.0,"peak_date_180d":"2024-03-07","trough_price_180d":14810.0,"trough_date_180d":"2024-08-05","calibration_usable":true,"case_polarity":"counterexample_weak_mfe_extreme_mae","evidence_url_pending":true,"source_proxy_only":true,"non_price_evidence_strength":"low_pending_url_repair","price_only_blowoff":false,"expected_stage_current_profile":"blocked_Stage2_or_4B_4C_high_MAE_watch_until_order_quality_delivery_margin_bridge_repaired","residual_error_type":"advanced_inspection_theme_had_limited_mfe_and_extreme_mae_without_order_quality_delivery_margin_bridge"}
```

---

## 8. Score simulation and raw component breakdown

This is shadow-only and does not change production scoring.

| symbol | advanced-equipment relevance | customer/order bridge | qualification / delivery | node or HBM/foundry pull-through | market mispricing | margin / operating leverage | information confidence | shadow total | intended route |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| `319660` | 12 | 9 | 8 | 8 | 11 | 8 | 5 | 61 | Stage2-Guarded / Yellow after evidence repair |
| `140860` | 12 | 8 | 8 | 9 | 8 | 7 | 5 | 57 | Stage2-Guarded / late-MFE Yellow watch after bridge repair |
| `348210` | 8 | 3 | 3 | 4 | 2 | 2 | 4 | 26 | blocked Stage2 / local 4B watch |
| `064290` | 8 | 2 | 2 | 4 | 3 | 1 | 4 | 24 | blocked Stage2 / 4B-4C high-MAE watch |

### Current calibrated profile stress test

The current calibrated profile already blocks pure price-only blowoff.  
The remaining C09 issue is **advanced equipment relevance without customer/order/qualification conversion**:

```text
C09 clean semicap equipment path:
  advanced equipment / semicap relevance
  + MFE_90D >= +20%
  + MAE_90D > -8%
  + evidence remains source_proxy_only
  => Stage2-Guarded, Yellow only after order/delivery/margin evidence repair

C09 late-MFE metrology path:
  advanced metrology relevance
  + MFE_180D >= +30%
  + MAE_180D > -10%
  + evidence remains source_proxy_only
  => Stage2-Guarded / Yellow watch, no Green

C09 weak-MFE high-MAE inspection path:
  equipment label exists
  + MFE_90D < +10%
  + MAE_90D <= -20% or MAE_180D <= -35%
  + no customer/order/margin bridge
  => block Stage2 or local 4B watch

C09 initial-MFE extreme-MAE path:
  first-window MFE exists
  + MAE_180D <= -50%
  + bridge evidence remains unrepaired
  => block Stage2 and route to 4B/4C high-MAE watch
```

`319660` and `140860` prevent overblocking.  
`348210` and `064290` show why advanced equipment labels should not be promoted without customer/order, qualification, delivery, and margin evidence.

---

## 9. Aggregate metrics

```json
{
  "row_type": "aggregate",
  "research_id": "R2L77_C09_ADVANCED_EQUIPMENT_ROUTER",
  "round": "R2",
  "loop": 77,
  "large_sector_id": "L2_AI_SEMICONDUCTOR_ELECTRONICS",
  "canonical_archetype_id": "C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF",
  "fine_archetype_id": "METROLOGY_INSPECTION_DRY_PROCESS_EQUIPMENT_MFE_AND_HIGH_MAE_ROUTER",
  "case_count": 4,
  "calibration_usable_case_count": 4,
  "positive_guarded_case_count": 2,
  "counterexample_count": 2,
  "new_symbol_count": 4,
  "source_proxy_only_count": 4,
  "evidence_url_pending_count": 4,
  "avg_mfe_30d_pct": 14.81,
  "avg_mae_30d_pct": -4.17,
  "avg_mfe_90d_pct": 17.25,
  "avg_mae_90d_pct": -16.62,
  "avg_mfe_180d_pct": 26.19,
  "avg_mae_180d_pct": -28.82,
  "max_mfe_180d_pct": 51.26,
  "worst_mae_180d_pct": -58.98
}
```

---

## 10. 4B proximity split

```json
{
  "row_type": "4b_split",
  "research_id": "R2L77_C09_ADVANCED_EQUIPMENT_ROUTER",
  "stage2_guarded_or_yellow_candidate": [
    {
      "symbol": "319660",
      "reason": "dry-process equipment path had +51.26% 180D MFE with only -7.16% MAE"
    },
    {
      "symbol": "140860",
      "reason": "advanced metrology path had +35.35% 180D MFE with -9.58% MAE"
    }
  ],
  "blocked_stage2_or_local_4b_watch": [
    {
      "symbol": "348210",
      "reason": "advanced inspection event had only +4.85% MFE and -39.57% 180D MAE"
    }
  ],
  "blocked_stage2_or_4c_watch": [
    {
      "symbol": "064290",
      "reason": "advanced inspection theme had only +13.30% MFE and -58.98% 180D MAE"
    }
  ],
  "full_4b_or_green_requires_non_price_evidence": [
    "customer order and qualification",
    "delivery schedule and tool acceptance",
    "node / HBM / foundry demand bridge",
    "backlog and revenue recognition",
    "gross margin and operating leverage",
    "cash-flow conversion"
  ]
}
```

---

## 11. Shadow rule candidate

```yaml
row_type: canonical_archetype_rule_candidate
canonical_archetype_id: C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF
fine_archetype_id: METROLOGY_INSPECTION_DRY_PROCESS_EQUIPMENT_MFE_AND_HIGH_MAE_ROUTER
rule_name: C09_metrology_inspection_dry_process_equipment_mfe_and_high_mae_router
production_scoring_changed: false
shadow_weight_only: true
```

### Proposed routing logic

```text
For C09 metrology / inspection / dry-process semicap equipment cases:

Tier A: verified advanced-equipment winner
  Conditions:
    - customer order, qualification, delivery, acceptance, and margin evidence are URL-repaired
    - MFE_90D >= +20%
    - MAE_90D > -8%
  Routing:
    - Stage2-Guarded allowed
    - Stage3-Yellow allowed after evidence repair
    - Green only after customer/order/qualification/margin bridge is verified

Tier B: late-MFE metrology path
  Conditions:
    - MFE_180D >= +30%
    - MAE_180D > -10%
    - evidence remains source_proxy_only
  Routing:
    - Stage2-Guarded / Yellow watch
    - no Green until evidence repair

Tier C: weak-MFE high-MAE equipment label
  Conditions:
    - MFE_90D < +10%
    - MAE_90D <= -20% or MAE_180D <= -35%
    - no repaired order/delivery/margin bridge
  Routing:
    - block Stage2
    - local 4B/high-MAE watch

Tier D: initial-MFE extreme-MAE equipment theme
  Conditions:
    - MFE_30D >= +10%
    - MAE_180D <= -50%
    - evidence remains source_proxy_only
  Routing:
    - block Stage2
    - route to 4B/4C high-MAE watch
```

### Suggested shadow delta

```json
{
  "row_type": "shadow_weight",
  "axis": "c09_metrology_inspection_dry_process_equipment_mfe_and_high_mae_router",
  "scope": "canonical_archetype_id:C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF",
  "proposal": {
    "source_proxy_only_green_allowed": false,
    "advanced_equipment_label_alone_stage2_allowed": false,
    "customer_order_qualification_margin_bridge_required_for_green": true,
    "verified_equipment_winner_mfe90_threshold_pct": 20.0,
    "verified_equipment_winner_mae90_min_pct": -8.0,
    "late_mfe_metrology_mfe180_threshold_pct": 30.0,
    "late_mfe_metrology_mae180_min_pct": -10.0,
    "weak_mfe_threshold_90d_pct": 10.0,
    "weak_mfe_mae90_threshold_pct": -20.0,
    "weak_mfe_hard_mae180_threshold_pct": -35.0,
    "extreme_mae180_threshold_pct": -50.0,
    "positive_weight_blocked_until_url_repair": true
  },
  "confidence": "medium_low_until_url_repair",
  "apply_now": false,
  "reason": "Two non-top-covered advanced equipment holdouts and two weak-MFE/high-MAE inspection-equipment failures show that C09 should require URL-repaired customer order, qualification, delivery, acceptance, and margin evidence before Yellow/Green."
}
```

---

## 12. Residual contribution summary

```json
{
  "row_type": "residual_contribution",
  "research_id": "R2L77_C09_ADVANCED_EQUIPMENT_ROUTER",
  "large_sector_id": "L2_AI_SEMICONDUCTOR_ELECTRONICS",
  "canonical_archetype_id": "C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF",
  "contribution": "Adds four non-top-covered C09 metrology / inspection / dry-process semicap equipment cases and separates low-MAE/late-MFE advanced-equipment holdouts from weak-MFE and extreme-MAE equipment-label failures. C09 Yellow/Green should require URL-repaired customer order, qualification, delivery, tool acceptance, node/HBM/foundry bridge, margin, and cash-flow evidence.",
  "positive_guarded_case_added": 2,
  "counterexample_case_added": 2,
  "new_symbol_count": 4,
  "new_independent_case_count": 4,
  "reused_case_count": 0,
  "same_archetype_new_symbol_count": 4,
  "same_archetype_new_trigger_family_count": 4,
  "new_trigger_family_count": 4,
  "current_profile_error_count": 2,
  "diversity_score_summary": {
    "new_symbol_bonus": 12,
    "counterexample_gap_bonus": 4,
    "residual_error_bonus": 10,
    "wrong_round_penalty": 0,
    "repeated_same_symbol_penalty": 0,
    "net_interpretive_score": 26
  },
  "loop_contribution_label": "canonical_archetype_rule_candidate",
  "do_not_propose_new_weight_delta": false,
  "data_quality_blocker": "All four non-price advanced-equipment triggers require URL-level repair before positive weight promotion.",
  "guardrail_added": "C09 source_proxy_only cases with MFE_90D < +10% and MAE_90D <= -20% or MAE_180D <= -35% should block Stage2; initial-MFE equipment themes with MAE_180D <= -50% should route to 4B/4C high-MAE watch."
}
```

One-line contribution:

```text
This loop adds 4 new independent cases, 2 counterexamples, and 2 residual errors for R2/L2_AI_SEMICONDUCTOR_ELECTRONICS/C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF.
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
    319660: false
    140860: false
    348210: false
    064290: false
  evidence_url_pending:
    319660: true
    140860: true
    348210: true
    064290: true
  source_proxy_only:
    319660: true
    140860: true
    348210: true
    064290: true
```

Limitations:

```text
- Price path is validated against Stock-Web tradable OHLC rows.
- Non-price evidence is not URL-repaired in this run.
- Therefore this artifact is useful for C09 advanced-equipment residual shape and high-MAE guardrail design, but should not promote positive weights until filings, IR, customer/order data, tool-qualification data, order disclosures, or reports verify customer order, qualification, delivery, tool acceptance, node/HBM/foundry demand, margin, and cash-flow conversion.
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
2. Preserve R2 / loop 77 metadata.
3. Add the cases to C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF only if parser validation passes.
4. Treat all four non-price triggers as evidence_url_pending=true and source_proxy_only=true until URL-level evidence is repaired.
5. Do not use these rows for positive weight promotion until filings/IR/customer-order/tool-qualification/order-disclosure/report data verifies customer order, qualification, delivery, tool acceptance, node/HBM/foundry demand, margin, and cash-flow conversion.
6. Add a shadow-only rule candidate named C09_metrology_inspection_dry_process_equipment_mfe_and_high_mae_router.
7. Do not loosen Stage3-Green.
8. Add C09-specific guards:
   - source_proxy_only -> no Green
   - advanced equipment label alone -> no Stage2 promotion
   - Green requires repaired customer/order/qualification/margin bridge
   - MFE_90D >= +20% and MAE_90D > -8% may remain Stage2-Guarded / Yellow watch after evidence repair
   - MFE_180D >= +30% and MAE_180D > -10% may remain late-MFE Stage2-Guarded while evidence is pending
   - MFE_90D < +10% and MAE_90D <= -20% or MAE_180D <= -35% -> block Stage2 / local 4B watch
   - MFE_30D >= +10% and MAE_180D <= -50% -> block Stage2 / 4B-4C high-MAE watch
9. Keep production scoring unchanged unless later batch promotion logic independently marks this axis safe.
```

---

## 15. Next round state

```text
completed_round = R2
completed_loop = 77
next_round = R3
next_loop = 77
next_large_sector_hint = L3_BATTERY_EV_GREEN_MOBILITY
round_schedule_status = valid
round_sector_consistency = pass
```
