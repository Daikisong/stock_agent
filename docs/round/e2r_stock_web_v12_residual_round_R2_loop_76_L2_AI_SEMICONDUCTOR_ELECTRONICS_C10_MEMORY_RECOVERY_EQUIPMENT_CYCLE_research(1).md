# E2R Stock-Web v12 Residual Research — R2 Loop 76

```yaml
research_session: post_calibrated_sector_archetype_residual_research
mode: historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12
completed_round: R2
completed_loop: 76
next_round: R3
next_loop: 76
large_sector_id: L2_AI_SEMICONDUCTOR_ELECTRONICS
canonical_archetype_id: C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE
fine_archetype_id: MEMORY_TEST_CMP_SUBSYSTEM_RECOVERY_LOW_MAE_AND_HIGH_MAE_ROUTER
output_file: e2r_stock_web_v12_residual_round_R2_loop_76_L2_AI_SEMICONDUCTOR_ELECTRONICS_C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE_research.md
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
completed_loop  = 76
large_sector_id = L1_INDUSTRIALS_INFRA_DEFENSE_GRID
canonical_archetype_id = C01_ORDER_BACKLOG_MARGIN_BRIDGE
```

Therefore:

```text
scheduled_round = R2
scheduled_loop  = 76
```

R2 maps to:

```text
large_sector_id = L2_AI_SEMICONDUCTOR_ELECTRONICS
```

This run selects:

```text
canonical_archetype_id = C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE
fine_archetype_id = MEMORY_TEST_CMP_SUBSYSTEM_RECOVERY_LOW_MAE_AND_HIGH_MAE_ROUTER
```

This is a valid R2/L2 pairing.

---

## 1. Why this R2/C10 run

The no-repeat ledger shows C10 is still relatively thin compared with the other L2 semiconductor archetypes:

```text
C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE:
  rows: 22
  symbols: 13
  date_range: 2023-03-17~2024-06-07
  good/bad S2: 9/4
  4B/4C: 2/0
  URL/proxy: 0/0
  top covered symbols: 095610(4), 036930(3), 240810(3), 084370(2), 테스(2), 000660(1)
```

This file avoids those top-covered C10 names and adds four memory-cycle equipment / consumable cases:

```text
089030 테크윙
281820 케이씨텍
039440 에스티아이
101160 월덱스
```

Research question:

```text
Can C10 separate true memory-cycle equipment recovery, where MFE persists and MAE remains contained, from memory-equipment or consumable recovery labels where first-window MFE is not enough and later MAE or weak MFE blocks Yellow/Green?
```

C10 is a memory-cycle recovery archetype. A memory upcycle is the rising tide, but equipment stocks need their own propeller: customer orders, qualification, delivery timing, installed-base demand, utilization, margin, and cash conversion. Without that propeller, the stock can catch the first wave and still drift back.

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
| `089030` | 테크윙 | active_like / KOSDAQ | no 2024 overlap; latest listed candidate 2022-08-23 | true |
| `281820` | 케이씨텍 | active_like / KOSPI | none listed | true |
| `039440` | 에스티아이 | active_like / KOSDAQ | no 2024 overlap; latest listed candidate 2018-04-20 | true |
| `101160` | 월덱스 | active_like / KOSDAQ | no 2024 overlap; latest listed candidate 2014-11-03 | true |

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
The Stock-Web price path is fully validated, but company-level customer order, qualification, delivery schedule, memory-node exposure, HBM or advanced-memory pull-through, consumable replacement demand, backlog, gross margin, and operating leverage evidence still require later URL repair through filings, IR decks, customer data, order disclosures, or sell-side reports before production weight promotion.
```

C10 interpretation used here:

```text
C10 is not simply “memory equipment stock rose.”
It asks whether memory-cycle recovery becomes company economics:
- customer order / qualification,
- delivery schedule and backlog,
- HBM / DRAM / NAND / advanced-memory demand bridge,
- installed-base or consumable pull-through,
- gross margin / operating leverage,
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
089030 + C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE -> no direct match found
281820 + C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE -> no direct match found
101160 + C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE -> no direct match found
039440 + C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE -> no direct match found
```

Novelty accounting:

```json
{
  "new_symbol_count": 4,
  "minimum_new_symbol_count": 2,
  "positive_case_count": 2,
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
| `R2L76_C10_089030_20240312` | `089030` 테크윙 | memory test handler / HBM cycle | positive anchor |
| `R2L76_C10_281820_20240227` | `281820` 케이씨텍 | memory CMP equipment recovery / high MFE later drawdown | positive-guarded |
| `R2L76_C10_039440_20240311` | `039440` 에스티아이 | memory subsystem equipment event / later hard MAE | first-window-MFE later-MAE counterexample |
| `R2L76_C10_101160_20240321` | `101160` 월덱스 | memory consumable recovery label / weak MFE slow fade | weak-MFE counterexample |

The intended residual:

```text
C10 should separate:
1. low-MAE memory test/equipment winners where MFE expands persistently;
2. high-MFE equipment recovery cases where later MAE still prevents Green without evidence repair;
3. first-window-MFE cases where 180D MAE overwhelms the recovery label;
4. memory consumable labels where MFE never expands enough for Stage2.
```

---

## 6. Stock-Web OHLC and backtest

### 6.1 `089030` 테크윙 — memory test handler / HBM cycle positive anchor

Trigger:

```text
trigger_date = 2024-03-11
trigger_type = Stage2-Actionable
trigger_family = memory_test_handler_hbm_cycle_low_mae_persistent_mfe
entry_date = 2024-03-12
entry_price = 26000.0
entry_price_type = next_tradable_open_after_memory_test_handler_cycle_burst
```

Relevant Stock-Web rows:

```csv
d,o,h,l,c,v,a,mc,s,m
2024-03-11,23350.0,24100.0,21850.0,23900.0,984145.0,22708974600.0,892752115500.0,37353645,KOSDAQ
2024-03-12,26000.0,28000.0,25200.0,26850.0,3360798.0,90473580250.0,1002945368250.0,37353645,KOSDAQ
2024-04-11,33650.0,39100.0,33350.0,38700.0,2637442.0,97864810200.0,1445586061500.0,37353645,KOSDAQ
2024-05-28,40900.0,45200.0,40550.0,43500.0,1916853.0,83046502300.0,1624883557500.0,37353645,KOSDAQ
2024-07-11,67800.0,70800.0,67200.0,68700.0,874088.0,60222114100.0,2566195411500.0,37353645,KOSDAQ
2024-08-05,41450.0,43700.0,37200.0,39150.0,2515253.0,103307240150.0,1462395201750.0,37353645,KOSDAQ
2024-09-06,32700.0,33000.0,30900.0,31700.0,1027687.0,32730488750.0,1184110546500.0,37353645,KOSDAQ
```

Backtest:

| window | peak/high | peak date | trough/low | trough date | MFE | MAE |
|---|---:|---|---:|---|---:|---:|
| 30 calendar days | 39100 | 2024-04-11 | 25200 | 2024-03-12 | +50.38% | -3.08% |
| 90 calendar days | 45200 | 2024-05-28 | 25200 | 2024-03-12 | +73.85% | -3.08% |
| 180 calendar days | 70800 | 2024-07-11 | 25200 | 2024-03-12 | +172.31% | -3.08% |

Interpretation:

```text
089030 is the C10 positive anchor.
The test-handler / HBM-cycle path produced persistent MFE with very limited MAE.
It supports Stage2-Actionable / Yellow after evidence repair, but Green still requires URL-repaired customer order, qualification, delivery, and margin evidence.
```

### 6.2 `281820` 케이씨텍 — memory CMP equipment high-MFE later-drawdown path

Trigger:

```text
trigger_date = 2024-02-26
trigger_type = Stage2-Actionable-Guarded
trigger_family = memory_cmp_equipment_cycle_high_mfe_later_drawdown
entry_date = 2024-02-27
entry_price = 38050.0
entry_price_type = next_tradable_open_after_memory_cmp_equipment_cycle_burst
```

Relevant Stock-Web rows:

```csv
d,o,h,l,c,v,a,mc,s,m
2024-02-26,32550.0,36100.0,32300.0,36100.0,605352.0,21267105100.0,753102171600.0,20861556,KOSPI
2024-02-27,38050.0,44700.0,34500.0,39200.0,2215249.0,86773423600.0,817772995200.0,20861556,KOSPI
2024-03-08,46850.0,54100.0,46850.0,50500.0,1513524.0,76147859550.0,1053508578000.0,20861556,KOSPI
2024-05-14,33300.0,33550.0,32350.0,33350.0,214661.0,7051909100.0,695732892600.0,20861556,KOSPI
2024-07-11,52000.0,59000.0,51900.0,56500.0,612449.0,34524875200.0,1178677914000.0,20861556,KOSPI
2024-08-05,36500.0,37800.0,31000.0,33150.0,232519.0,8238318150.0,691560581400.0,20861556,KOSPI
```

Backtest:

| window | peak/high | peak date | trough/low | trough date | MFE | MAE |
|---|---:|---|---:|---|---:|---:|
| 30 calendar days | 54100 | 2024-03-08 | 34500 | 2024-02-27 | +42.18% | -9.33% |
| 90 calendar days | 54100 | 2024-03-08 | 32350 | 2024-05-14 | +42.18% | -14.98% |
| 180 calendar days | 59000 | 2024-07-11 | 31000 | 2024-08-05 | +55.06% | -18.53% |

Interpretation:

```text
281820 is the high-MFE but later-drawdown branch.
The 30D/180D MFE was large, yet the 90D/180D MAE was too wide for Green while evidence remains source-proxy-only.
This should remain Stage2-Guarded or Yellow-watch only after customer/order/margin evidence repair.
```

### 6.3 `039440` 에스티아이 — memory subsystem event with later hard MAE

Trigger:

```text
trigger_date = 2024-03-08
trigger_type = Stage2-FalsePositive-Candidate
trigger_family = memory_subsystem_equipment_event_mfe_later_hard_mae
entry_date = 2024-03-11
entry_price = 35600.0
entry_price_type = next_tradable_open_after_memory_subsystem_equipment_spike
```

Relevant Stock-Web rows:

```csv
d,o,h,l,c,v,a,mc,s,m
2024-03-08,36400.0,39550.0,35700.0,37000.0,2502464.0,94342914350.0,585710000000.0,15830000,KOSDAQ
2024-03-11,35600.0,41200.0,34550.0,38400.0,2960083.0,114112042350.0,607872000000.0,15830000,KOSDAQ
2024-03-13,40100.0,43250.0,38750.0,38750.0,2438199.0,99405111200.0,613412500000.0,15830000,KOSDAQ
2024-04-11,31200.0,33450.0,31100.0,33350.0,334044.0,10932590700.0,527930500000.0,15830000,KOSDAQ
2024-04-18,36100.0,42600.0,35650.0,42000.0,4000134.0,161030472100.0,664860000000.0,15830000,KOSDAQ
2024-08-05,23500.0,23700.0,20000.0,21100.0,517792.0,11552154550.0,334013000000.0,15830000,KOSDAQ
2024-09-06,20000.0,20150.0,19200.0,19400.0,281427.0,5483560740.0,307102000000.0,15830000,KOSDAQ
```

Backtest:

| window | peak/high | peak date | trough/low | trough date | MFE | MAE |
|---|---:|---|---:|---|---:|---:|
| 30 calendar days | 43250 | 2024-03-13 | 32050 | 2024-04-09 | +21.49% | -9.97% |
| 90 calendar days | 43250 | 2024-03-13 | 31500 | 2024-05-31 | +21.49% | -11.52% |
| 180 calendar days | 43250 | 2024-03-13 | 19200 | 2024-09-06 | +21.49% | -46.07% |

Interpretation:

```text
039440 is the first-window-MFE / later-hard-MAE counterexample.
The initial equipment-event MFE was real, but the 180D drawdown crossed a hard high-MAE zone.
This should cap at Stage2-Guarded or route to local 4B/high-MAE watch until order, customer, delivery, and margin evidence are repaired.
```

### 6.4 `101160` 월덱스 — memory consumable recovery weak-MFE slow fade

Trigger:

```text
trigger_date = 2024-03-20
trigger_type = Stage2-FalsePositive-Candidate
trigger_family = memory_consumable_recovery_label_weak_mfe_slow_fade
entry_date = 2024-03-21
entry_price = 24600.0
entry_price_type = next_tradable_open_after_memory_consumable_recovery_label_burst
```

Relevant Stock-Web rows:

```csv
d,o,h,l,c,v,a,mc,s,m
2024-03-20,22800.0,23450.0,22700.0,23300.0,170715.0,3951636650.0,384706136900.0,16510993,KOSDAQ
2024-03-21,24600.0,25700.0,24250.0,25150.0,1375483.0,34624045800.0,415251473950.0,16510993,KOSDAQ
2024-04-02,25550.0,26150.0,24950.0,25700.0,659726.0,16920533000.0,424332520100.0,16510993,KOSDAQ
2024-05-31,22250.0,22450.0,21400.0,21450.0,295949.0,6432488500.0,354160799850.0,16510993,KOSDAQ
2024-08-05,21200.0,21350.0,18550.0,19050.0,396372.0,7968541920.0,314534416650.0,16510993,KOSDAQ
2024-09-06,20200.0,20350.0,19610.0,19690.0,386637.0,7647130800.0,325101452170.0,16510993,KOSDAQ
```

Backtest:

| window | peak/high | peak date | trough/low | trough date | MFE | MAE |
|---|---:|---|---:|---|---:|---:|
| 30 calendar days | 26150 | 2024-04-02 | 23500 | 2024-04-19 | +6.30% | -4.47% |
| 90 calendar days | 26150 | 2024-04-02 | 21300 | 2024-06-03 | +6.30% | -13.41% |
| 180 calendar days | 26150 | 2024-04-02 | 18550 | 2024-08-05 | +6.30% | -24.59% |

Interpretation:

```text
101160 is the weak-MFE slow-fade branch.
The memory consumable recovery label existed, but MFE never expanded past +6.30% while 90D/180D drawdown widened.
This should block Green and usually block Stage2 unless a later independent trigger repairs customer volume, replacement demand, and margin evidence.
```

---

## 7. Machine-readable trigger JSONL

```jsonl
{"row_type":"trigger","research_id":"R2L76_C10_MEMORY_EQUIPMENT_RECOVERY_ROUTER","round":"R2","loop":76,"large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE","fine_archetype_id":"MEMORY_TEST_CMP_SUBSYSTEM_RECOVERY_LOW_MAE_AND_HIGH_MAE_ROUTER","symbol":"089030","name":"테크윙","trigger_type":"Stage2-Actionable","trigger_family":"memory_test_handler_hbm_cycle_low_mae_persistent_mfe","trigger_date":"2024-03-11","entry_date":"2024-03-12","entry_price":26000.0,"entry_price_type":"next_tradable_open_after_memory_test_handler_cycle_burst","price_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","mfe_30d_pct":50.38,"mae_30d_pct":-3.08,"mfe_90d_pct":73.85,"mae_90d_pct":-3.08,"mfe_180d_pct":172.31,"mae_180d_pct":-3.08,"peak_price_180d":70800.0,"peak_date_180d":"2024-07-11","trough_price_180d":25200.0,"trough_date_180d":"2024-03-12","calibration_usable":true,"case_polarity":"positive_anchor_low_mae_memory_test_handler","evidence_url_pending":true,"source_proxy_only":true,"non_price_evidence_strength":"medium_pending_url_repair","price_only_blowoff":false,"expected_stage_current_profile":"Stage2-Actionable_to_Yellow_after_customer_order_delivery_margin_bridge_repaired","residual_error_type":"memory_test_handler_cycle_path_supports_positive_route_but_green_requires_url_repaired_order_customer_margin_bridge"}
{"row_type":"trigger","research_id":"R2L76_C10_MEMORY_EQUIPMENT_RECOVERY_ROUTER","round":"R2","loop":76,"large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE","fine_archetype_id":"MEMORY_TEST_CMP_SUBSYSTEM_RECOVERY_LOW_MAE_AND_HIGH_MAE_ROUTER","symbol":"281820","name":"케이씨텍","trigger_type":"Stage2-Actionable-Guarded","trigger_family":"memory_cmp_equipment_cycle_high_mfe_later_drawdown","trigger_date":"2024-02-26","entry_date":"2024-02-27","entry_price":38050.0,"entry_price_type":"next_tradable_open_after_memory_cmp_equipment_cycle_burst","price_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","mfe_30d_pct":42.18,"mae_30d_pct":-9.33,"mfe_90d_pct":42.18,"mae_90d_pct":-14.98,"mfe_180d_pct":55.06,"mae_180d_pct":-18.53,"peak_price_180d":59000.0,"peak_date_180d":"2024-07-11","trough_price_180d":31000.0,"trough_date_180d":"2024-08-05","calibration_usable":true,"case_polarity":"positive_guarded_high_mfe_later_drawdown","evidence_url_pending":true,"source_proxy_only":true,"non_price_evidence_strength":"medium_low_pending_url_repair","price_only_blowoff":false,"expected_stage_current_profile":"Stage2-Guarded_to_Yellow_only_if_cmp_order_memory_customer_margin_bridge_repaired","residual_error_type":"memory_cmp_cycle_had_high_mfe_but_later_mae_requires_url_repaired_customer_order_margin_bridge_before_yellow_green"}
{"row_type":"trigger","research_id":"R2L76_C10_MEMORY_EQUIPMENT_RECOVERY_ROUTER","round":"R2","loop":76,"large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE","fine_archetype_id":"MEMORY_TEST_CMP_SUBSYSTEM_RECOVERY_LOW_MAE_AND_HIGH_MAE_ROUTER","symbol":"039440","name":"에스티아이","trigger_type":"Stage2-FalsePositive-Candidate","trigger_family":"memory_subsystem_equipment_event_mfe_later_hard_mae","trigger_date":"2024-03-08","entry_date":"2024-03-11","entry_price":35600.0,"entry_price_type":"next_tradable_open_after_memory_subsystem_equipment_spike","price_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","mfe_30d_pct":21.49,"mae_30d_pct":-9.97,"mfe_90d_pct":21.49,"mae_90d_pct":-11.52,"mfe_180d_pct":21.49,"mae_180d_pct":-46.07,"peak_price_180d":43250.0,"peak_date_180d":"2024-03-13","trough_price_180d":19200.0,"trough_date_180d":"2024-09-06","calibration_usable":true,"case_polarity":"counterexample_first_window_mfe_later_hard_mae","evidence_url_pending":true,"source_proxy_only":true,"non_price_evidence_strength":"low_pending_url_repair","price_only_blowoff":false,"expected_stage_current_profile":"Stage2-Guarded_or_local_4B_high_MAE_watch_until_customer_order_margin_bridge_repaired","residual_error_type":"memory_equipment_label_had_first_window_mfe_but_180d_hard_mae_blocks_yellow_green_without_order_margin_bridge"}
{"row_type":"trigger","research_id":"R2L76_C10_MEMORY_EQUIPMENT_RECOVERY_ROUTER","round":"R2","loop":76,"large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE","fine_archetype_id":"MEMORY_TEST_CMP_SUBSYSTEM_RECOVERY_LOW_MAE_AND_HIGH_MAE_ROUTER","symbol":"101160","name":"월덱스","trigger_type":"Stage2-FalsePositive-Candidate","trigger_family":"memory_consumable_recovery_label_weak_mfe_slow_fade","trigger_date":"2024-03-20","entry_date":"2024-03-21","entry_price":24600.0,"entry_price_type":"next_tradable_open_after_memory_consumable_recovery_label_burst","price_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","mfe_30d_pct":6.3,"mae_30d_pct":-4.47,"mfe_90d_pct":6.3,"mae_90d_pct":-13.41,"mfe_180d_pct":6.3,"mae_180d_pct":-24.59,"peak_price_180d":26150.0,"peak_date_180d":"2024-04-02","trough_price_180d":18550.0,"trough_date_180d":"2024-08-05","calibration_usable":true,"case_polarity":"counterexample_weak_mfe_slow_fade","evidence_url_pending":true,"source_proxy_only":true,"non_price_evidence_strength":"low_pending_url_repair","price_only_blowoff":false,"expected_stage_current_profile":"blocked_Stage2_or_local_4B_watch_until_customer_cycle_margin_bridge_repaired","residual_error_type":"memory_consumable_recovery_label_had_weak_mfe_and_mid_window_drawdown_without_customer_volume_margin_bridge"}
```

---

## 8. Score simulation and raw component breakdown

This is shadow-only and does not change production scoring.

| symbol | memory-cycle relevance | customer/order bridge | delivery / qualification | installed-base or consumable pull-through | market mispricing | margin / operating leverage | information confidence | shadow total | intended route |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| `089030` | 14 | 12 | 12 | 10 | 16 | 12 | 6 | 82 | Stage2/Yellow after evidence repair |
| `281820` | 11 | 8 | 8 | 6 | 11 | 6 | 5 | 55 | Stage2-Guarded / Yellow-watch after bridge repair |
| `039440` | 9 | 4 | 4 | 4 | 6 | 3 | 4 | 34 | Stage2-Guarded at most / local 4B watch |
| `101160` | 8 | 3 | 3 | 4 | 2 | 2 | 4 | 26 | blocked Stage2 / weak-MFE watch |

### Current calibrated profile stress test

The current calibrated profile already blocks pure price-only blowoff.  
The remaining C10 issue is **memory-cycle label without order/customer/margin conversion**:

```text
C10 clean memory equipment path:
  memory-cycle / HBM or advanced-memory relevance
  + persistent MFE
  + contained MAE
  + URL-repaired customer/order/qualification/margin bridge
  => Stage2-Actionable / Yellow, possible Green after proof

C10 high-MFE later-drawdown path:
  equipment recovery relevance
  + MFE_30D >= +30%
  + MAE_90D <= -12%
  + source_proxy_only evidence
  => Stage2-Guarded at most until bridge repair

C10 first-window-MFE later-hard-MAE path:
  first-window MFE exists
  + MAE_180D <= -40%
  + customer/order bridge missing
  => no Yellow/Green, local 4B watch

C10 weak-MFE slow fade:
  MFE_90D < +10%
  + MAE_180D <= -20%
  + no customer-volume / margin bridge
  => block Stage2 or local 4B watch
```

`089030` prevents overblocking.  
`281820` shows why strong MFE still needs a later-drawdown cap.  
`039440` and `101160` show why memory recovery labels should not be promoted without customer/order/margin evidence.

---

## 9. Aggregate metrics

```json
{
  "row_type": "aggregate",
  "research_id": "R2L76_C10_MEMORY_EQUIPMENT_RECOVERY_ROUTER",
  "round": "R2",
  "loop": 76,
  "large_sector_id": "L2_AI_SEMICONDUCTOR_ELECTRONICS",
  "canonical_archetype_id": "C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE",
  "fine_archetype_id": "MEMORY_TEST_CMP_SUBSYSTEM_RECOVERY_LOW_MAE_AND_HIGH_MAE_ROUTER",
  "case_count": 4,
  "calibration_usable_case_count": 4,
  "positive_case_count": 2,
  "counterexample_count": 2,
  "new_symbol_count": 4,
  "source_proxy_only_count": 4,
  "evidence_url_pending_count": 4,
  "avg_mfe_30d_pct": 30.09,
  "avg_mae_30d_pct": -6.71,
  "avg_mfe_90d_pct": 35.95,
  "avg_mae_90d_pct": -10.75,
  "avg_mfe_180d_pct": 63.79,
  "avg_mae_180d_pct": -23.07,
  "max_mfe_180d_pct": 172.31,
  "worst_mae_180d_pct": -46.07
}
```

---

## 10. 4B proximity split

```json
{
  "row_type": "4b_split",
  "research_id": "R2L76_C10_MEMORY_EQUIPMENT_RECOVERY_ROUTER",
  "stage2_positive_or_yellow_candidate": [
    {
      "symbol": "089030",
      "reason": "memory test-handler path had +172.31% 180D MFE with only -3.08% MAE"
    }
  ],
  "stage2_guarded_or_yellow_watch": [
    {
      "symbol": "281820",
      "reason": "memory CMP equipment path had +55.06% MFE but -18.53% 180D MAE; requires order/margin evidence repair"
    }
  ],
  "local_4b_high_mae_watch": [
    {
      "symbol": "039440",
      "reason": "first-window MFE existed, but 180D MAE reached -46.07%"
    }
  ],
  "blocked_stage2_or_weak_mfe_watch": [
    {
      "symbol": "101160",
      "reason": "MFE stayed only +6.30%, while 180D MAE reached -24.59%"
    }
  ],
  "full_4b_or_green_requires_non_price_evidence": [
    "customer order and qualification",
    "memory-node / HBM / DRAM / NAND demand bridge",
    "delivery schedule and backlog",
    "installed-base or consumable replacement demand",
    "gross margin and operating leverage",
    "cash-flow conversion"
  ]
}
```

---

## 11. Shadow rule candidate

```yaml
row_type: canonical_archetype_rule_candidate
canonical_archetype_id: C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE
fine_archetype_id: MEMORY_TEST_CMP_SUBSYSTEM_RECOVERY_LOW_MAE_AND_HIGH_MAE_ROUTER
rule_name: C10_memory_equipment_cycle_customer_order_margin_and_high_mae_router
production_scoring_changed: false
shadow_weight_only: true
```

### Proposed routing logic

```text
For C10 memory recovery equipment / consumable cases:

Tier A: verified memory equipment winner
  Conditions:
    - memory-cycle relevance is backed by URL-repaired customer/order/qualification/margin evidence
    - MFE_90D >= +30%
    - MAE_90D > -8%
    - MFE persists beyond one event candle
  Routing:
    - Stage2-Actionable allowed
    - Stage3-Yellow allowed after evidence repair
    - Green only after customer/order/margin bridge is verified

Tier B: source-proxy high-MFE later-drawdown case
  Conditions:
    - MFE_30D >= +30%
    - MAE_90D <= -12%
    - evidence_url_pending or source_proxy_only remains true
  Routing:
    - Stage2-Guarded at most
    - no Green until evidence repair

Tier C: first-window-MFE / later-hard-MAE case
  Conditions:
    - MFE_30D >= +15%
    - MAE_180D <= -40%
    - no repaired customer/order/margin bridge
  Routing:
    - local 4B/high-MAE watch
    - no Yellow/Green

Tier D: weak-MFE slow-fade memory label
  Conditions:
    - MFE_90D < +10%
    - MAE_180D <= -20%
    - bridge evidence remains unrepaired
  Routing:
    - block Stage2 or local 4B watch
    - count as counterexample
```

### Suggested shadow delta

```json
{
  "row_type": "shadow_weight",
  "axis": "c10_memory_equipment_cycle_customer_order_margin_and_high_mae_router",
  "scope": "canonical_archetype_id:C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE",
  "proposal": {
    "source_proxy_only_green_allowed": false,
    "customer_order_qualification_margin_bridge_required_for_green": true,
    "verified_memory_equipment_mfe90_threshold_pct": 30.0,
    "verified_memory_equipment_mae90_min_pct": -8.0,
    "high_mfe_threshold_30d_pct": 30.0,
    "high_mfe_later_drawdown_mae90_threshold_pct": -12.0,
    "first_window_mfe_threshold_30d_pct": 15.0,
    "later_hard_mae_threshold_180d_pct": -40.0,
    "weak_mfe_threshold_90d_pct": 10.0,
    "weak_mfe_mae180_threshold_pct": -20.0,
    "positive_weight_blocked_until_url_repair": true
  },
  "confidence": "medium_low_until_url_repair",
  "apply_now": false,
  "reason": "One clean memory test-handler winner, one high-MFE later-drawdown equipment case, and two high-MAE or weak-MFE recovery-label failures show that C10 should require URL-repaired customer order, qualification, delivery, and margin evidence before Yellow/Green."
}
```

---

## 12. Residual contribution summary

```json
{
  "row_type": "residual_contribution",
  "research_id": "R2L76_C10_MEMORY_EQUIPMENT_RECOVERY_ROUTER",
  "large_sector_id": "L2_AI_SEMICONDUCTOR_ELECTRONICS",
  "canonical_archetype_id": "C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE",
  "contribution": "Adds four non-top-covered C10 memory recovery equipment/consumable cases and separates a clean low-MAE test-handler winner from high-MFE later-drawdown, first-window-MFE later-hard-MAE, and weak-MFE slow-fade failures. C10 Yellow/Green should require URL-repaired customer order, qualification, delivery, memory-node demand, installed-base/consumable pull-through, and margin evidence.",
  "positive_case_added": 2,
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
  "data_quality_blocker": "All four non-price memory equipment/recovery triggers require URL-level repair before positive weight promotion.",
  "guardrail_added": "C10 source_proxy_only cases with MFE_30D >= +30% but MAE_90D <= -12% should cap at Stage2-Guarded; first-window-MFE cases with MAE_180D <= -40% should route to 4B watch; weak-MFE cases with MFE_90D < +10% and MAE_180D <= -20% should block Stage2."
}
```

One-line contribution:

```text
This loop adds 4 new independent cases, 2 counterexamples, and 2 residual errors for R2/L2_AI_SEMICONDUCTOR_ELECTRONICS/C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE.
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
    089030: false
    281820: false
    039440: false
    101160: false
  evidence_url_pending:
    089030: true
    281820: true
    039440: true
    101160: true
  source_proxy_only:
    089030: true
    281820: true
    039440: true
    101160: true
```

Limitations:

```text
- Price path is validated against Stock-Web tradable OHLC rows.
- Non-price evidence is not URL-repaired in this run.
- Therefore this artifact is useful for C10 memory recovery equipment/consumable residual shape and high-MAE/weak-MFE guardrail design, but should not promote positive weights until filings, IR, customer/order data, order disclosures, or reports verify customer order, qualification, delivery, memory-node demand, installed-base/consumable pull-through, margin, and cash-flow conversion.
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
2. Preserve R2 / loop 76 metadata.
3. Add the cases to C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE only if parser validation passes.
4. Treat all four non-price triggers as evidence_url_pending=true and source_proxy_only=true until URL-level evidence is repaired.
5. Do not use these rows for positive weight promotion until filings/IR/customer-order/order-disclosure/report data verifies customer order, qualification, delivery, memory-node demand, installed-base/consumable pull-through, margin, and cash-flow conversion.
6. Add a shadow-only rule candidate named C10_memory_equipment_cycle_customer_order_margin_and_high_mae_router.
7. Do not loosen Stage3-Green.
8. Add C10-specific guards:
   - source_proxy_only -> no Green
   - Green requires repaired customer/order/qualification/margin bridge
   - MFE_90D >= +30% and MAE_90D > -8% may remain Stage2-Actionable / Yellow watch after evidence repair
   - MFE_30D >= +30% but MAE_90D <= -12% -> Stage2-Guarded at most until evidence repair
   - MFE_30D >= +15% and MAE_180D <= -40% -> local 4B/high-MAE watch; no Yellow/Green
   - MFE_90D < +10% and MAE_180D <= -20% -> block Stage2 or local 4B watch
9. Keep production scoring unchanged unless later batch promotion logic independently marks this axis safe.
```

---

## 15. Next round state

```text
completed_round = R2
completed_loop = 76
next_round = R3
next_loop = 76
next_large_sector_hint = L3_BATTERY_EV_GREEN_MOBILITY
round_schedule_status = valid
round_sector_consistency = pass
```
