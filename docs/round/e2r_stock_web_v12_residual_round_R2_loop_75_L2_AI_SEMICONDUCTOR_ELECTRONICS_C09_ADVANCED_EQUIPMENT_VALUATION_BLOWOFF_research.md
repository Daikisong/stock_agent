# E2R Stock-Web v12 Residual Research — R2 Loop 75

```yaml
research_session: post_calibrated_sector_archetype_residual_research
mode: historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12
completed_round: R2
completed_loop: 75
next_round: R3
next_loop: 75
large_sector_id: L2_AI_SEMICONDUCTOR_ELECTRONICS
canonical_archetype_id: C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF
fine_archetype_id: ADVANCED_METROLOGY_INSPECTION_ORDER_BRIDGE_AND_VALUATION_BLOWOFF_ROUTER
output_file: e2r_stock_web_v12_residual_round_R2_loop_75_L2_AI_SEMICONDUCTOR_ELECTRONICS_C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF_research.md
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
completed_loop  = 75
large_sector_id = L1_INDUSTRIALS_INFRA_DEFENSE_GRID
canonical_archetype_id = C02_POWER_GRID_DATACENTER_CAPEX
```

Therefore:

```text
scheduled_round = R2
scheduled_loop  = 75
```

R2 maps to:

```text
large_sector_id = L2_AI_SEMICONDUCTOR_ELECTRONICS
```

This run selects:

```text
canonical_archetype_id = C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF
fine_archetype_id = ADVANCED_METROLOGY_INSPECTION_ORDER_BRIDGE_AND_VALUATION_BLOWOFF_ROUTER
```

This is a valid R2/L2 pairing.

---

## 1. Why this R2/C09 run

The no-repeat ledger shows C09 is covered, but its top repeated names are concentrated in the already-tested advanced equipment / HBM equipment cluster:

```text
C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF:
  rows: 50
  symbols: 21
  date_range: 2024-01-19~2024-07-11
  good/bad S2: 6/0
  4B/4C: 19/2
  URL/proxy: 0/0
  top covered symbols: 240810(6), 036930(5), 039030(4), 003160(3), 042700(3), 095340(3)
```

This file avoids those top-covered symbols and tests advanced metrology / inspection names:

```text
140860 파크시스템스
322310 오로스테크놀로지
348210 넥스틴
```

Research question:

```text
Can C09 preserve a high-quality advanced metrology holdout while blocking entry-day or delayed high-MAE inspection/metrology spikes where valuation and equipment-label relevance are not enough without customer order and margin evidence?
```

C09 is a valuation-blowoff archetype, not a blanket rejection rule. A precision metrology company can rerate after a reset when the customer/order bridge is durable. But the same sector can also produce a lens-flare: the chart flashes, the peak is already in, and the next visible object is drawdown. The router has to separate the microscope from the mirror.

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
| `140860` | 파크시스템스 | active_like / KOSDAQ | none listed | true |
| `322310` | 오로스테크놀로지 | active_like / KOSDAQ | none listed | true |
| `348210` | 넥스틴 | active_like / KOSDAQ GLOBAL | no 2024 overlap; listed 2021 candidates only | true |

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
The Stock-Web price path is fully validated, but company-level metrology/inspection customer order, qualification, delivery schedule, advanced-node exposure, HBM/advanced packaging pull-through, backlog, gross margin, and operating leverage evidence still require later URL repair through filings, IR decks, customer data, or sell-side reports before production weight promotion.
```

C09 interpretation used here:

```text
C09 is not simply “advanced semiconductor equipment rose.”
It asks whether valuation expansion is backed by a real bridge:
- customer order / qualification,
- advanced-node or packaging demand,
- delivery and backlog visibility,
- gross margin and operating leverage,
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
140860 + C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF -> no direct match found
322310 + C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF -> no direct match found
348210 + C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF -> no direct match found
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
| `R2L75_C09_140860_20240429` | `140860` 파크시스템스 | advanced metrology quality / order bridge after reset | positive-guarded holdout |
| `R2L75_C09_322310_20240227` | `322310` 오로스테크놀로지 | overlay metrology theme spike without order bridge | entry-day peak high-MAE counterexample |
| `R2L75_C09_348210_20240228` | `348210` 넥스틴 | inspection equipment recovery label with delayed high MAE | delayed high-MAE counterexample |

The intended residual:

```text
C09 should separate:
1. quality advanced-equipment rerating after reset, where MAE remains contained;
2. event/theme spikes that peak at entry and then collapse;
3. equipment-recovery labels that show first-window MFE but fail later without customer/order/margin bridge repair.
```

---

## 6. Stock-Web OHLC and backtest

### 6.1 `140860` 파크시스템스 — advanced metrology quality holdout

Trigger:

```text
trigger_date = 2024-04-26
trigger_type = Stage2-Actionable-Guarded
trigger_family = advanced_metrology_quality_order_bridge_post_reset_rerating
entry_date = 2024-04-29
entry_price = 151600.0
entry_price_type = next_tradable_open_after_metrology_order_quality_reset
```

Relevant Stock-Web rows:

```csv
d,o,h,l,c,v,a,mc,s,m
2024-04-26,151200.0,153500.0,148800.0,150100.0,19756.0,2988383400.0,1046701185900.0,6973359,KOSDAQ
2024-04-29,151600.0,153700.0,145600.0,148200.0,40395.0,5974738400.0,1033451803800.0,6973359,KOSDAQ
2024-05-23,178900.0,180400.0,176000.0,180400.0,40835.0,7337714900.0,1258444963600.0,6975859,KOSDAQ
2024-06-04,180000.0,189500.0,179200.0,187600.0,75744.0,14116322600.0,1308671148400.0,6975859,KOSDAQ
2024-07-04,195800.0,198600.0,193600.0,198400.0,24612.0,4838187400.0,1384942905600.0,6980559,KOSDAQ
2024-08-05,158700.0,161400.0,149500.0,153800.0,60127.0,9312526900.0,1073609974200.0,6980559,KOSDAQ
2024-10-04,197400.0,201500.0,193500.0,199900.0,32535.0,6485431600.0,1396023439100.0,6983609,KOSDAQ
```

Backtest:

| window | peak/high | peak date | trough/low | trough date | MFE | MAE |
|---|---:|---|---:|---|---:|---:|
| 30 calendar days | 180400 | 2024-05-23 | 145600 | 2024-04-29 | +19.00% | -3.96% |
| 90 calendar days | 198600 | 2024-07-04 | 145600 | 2024-04-29 | +31.00% | -3.96% |
| 180 calendar days | 201500 | 2024-10-04 | 145600 | 2024-04-29 | +32.92% | -3.96% |

Interpretation:

```text
140860 is the C09 positive-guarded holdout.
The return was not a single blowoff candle; MFE built over time while MAE stayed contained.
This should stay open as Stage2-Guarded / Yellow after URL-repaired customer order, advanced-node demand, and margin evidence. It is not automatic Green while evidence is source-proxy-only.
```

### 6.2 `322310` 오로스테크놀로지 — overlay metrology entry-day peak / high-MAE counterexample

Trigger:

```text
trigger_date = 2024-02-26
trigger_type = Stage2-FalsePositive-Candidate
trigger_family = overlay_metrology_equipment_theme_spike_without_order_bridge
entry_date = 2024-02-27
entry_price = 36100.0
entry_price_type = next_tradable_open_after_overlay_metrology_theme_burst
```

Relevant Stock-Web rows:

```csv
d,o,h,l,c,v,a,mc,s,m
2024-02-26,34200.0,36900.0,33000.0,35450.0,372773.0,13275844750.0,332043913900.0,9366542,KOSDAQ
2024-02-27,36100.0,40750.0,34050.0,37200.0,1848333.0,70098981500.0,348435362400.0,9366542,KOSDAQ
2024-03-14,33700.0,33700.0,32300.0,32850.0,141358.0,4630580600.0,307690904700.0,9366542,KOSDAQ
2024-04-23,28200.0,28400.0,27000.0,27000.0,159341.0,4390267450.0,252896634000.0,9366542,KOSDAQ
2024-05-27,24700.0,25050.0,23750.0,24400.0,150441.0,3642403950.0,228543624800.0,9366542,KOSDAQ
2024-07-04,22500.0,27050.0,22400.0,26600.0,931713.0,23726250100.0,249150017200.0,9366542,KOSDAQ
2024-08-05,19950.0,19980.0,16300.0,16860.0,178735.0,3261903150.0,157919898120.0,9366542,KOSDAQ
```

Backtest:

| window | peak/high | peak date | trough/low | trough date | MFE | MAE |
|---|---:|---|---:|---|---:|---:|
| 30 calendar days | 40750 | 2024-02-27 | 32300 | 2024-03-14 | +12.88% | -10.53% |
| 90 calendar days | 40750 | 2024-02-27 | 23750 | 2024-05-27 | +12.88% | -34.21% |
| 180 calendar days | 40750 | 2024-02-27 | 16300 | 2024-08-05 | +12.88% | -54.85% |

Interpretation:

```text
322310 is the hard C09 entry-day-peak counterexample.
The highest price of the forward windows occurred on the entry day; the rest of the path was drawdown.
This should block Stage2/Green and route to 4B/4C high-MAE watch unless a verified order/customer/margin bridge existed before entry.
```

### 6.3 `348210` 넥스틴 — inspection equipment recovery label with delayed high MAE

Trigger:

```text
trigger_date = 2024-02-27
trigger_type = Stage2-Actionable-Guarded
trigger_family = inspection_equipment_recovery_label_delayed_high_mae
entry_date = 2024-02-28
entry_price = 68900.0
entry_price_type = next_tradable_open_after_inspection_equipment_recovery_burst
```

Relevant Stock-Web rows:

```csv
d,o,h,l,c,v,a,mc,s,m
2024-02-27,70400.0,70400.0,68200.0,69000.0,84762.0,5854162500.0,709204908000.0,10278332,KOSDAQ GLOBAL
2024-02-28,68900.0,76800.0,68700.0,74800.0,390433.0,29170757400.0,768819233600.0,10278332,KOSDAQ GLOBAL
2024-03-04,77800.0,77900.0,75300.0,76200.0,160323.0,12241646700.0,783208898400.0,10278332,KOSDAQ GLOBAL
2024-04-22,59300.0,60500.0,55500.0,56700.0,232134.0,13276495700.0,582781424400.0,10278332,KOSDAQ GLOBAL
2024-05-23,71600.0,72300.0,69900.0,70800.0,92515.0,6579738400.0,727705905600.0,10278332,KOSDAQ GLOBAL
2024-06-21,73700.0,77500.0,67300.0,70300.0,499734.0,37006777700.0,728122408000.0,10357360,KOSDAQ GLOBAL
2024-08-05,53400.0,53700.0,44900.0,45000.0,221835.0,10811232150.0,466081200000.0,10357360,KOSDAQ GLOBAL
2024-08-26,50900.0,51700.0,49250.0,49800.0,37352.0,1872263550.0,515796528000.0,10357360,KOSDAQ GLOBAL
```

Backtest:

| window | peak/high | peak date | trough/low | trough date | MFE | MAE |
|---|---:|---|---:|---|---:|---:|
| 30 calendar days | 77900 | 2024-03-04 | 68700 | 2024-02-28 | +13.06% | -0.29% |
| 90 calendar days | 77900 | 2024-03-04 | 55500 | 2024-04-22 | +13.06% | -19.45% |
| 180 calendar days | 77900 | 2024-03-04 | 44900 | 2024-08-05 | +13.06% | -34.83% |

Interpretation:

```text
348210 is the delayed high-MAE branch.
The first 30D window looked acceptable, but 90D and 180D exposed a drawdown that should block Yellow/Green while evidence remains source-proxy-only.
This should cap at Stage2-Guarded or local 4B watch until inspection-order, customer, and margin evidence are repaired.
```

---

## 7. Machine-readable trigger JSONL

```jsonl
{"row_type":"trigger","research_id":"R2L75_C09_ADVANCED_METROLOGY_INSPECTION_ROUTER","round":"R2","loop":75,"large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF","fine_archetype_id":"ADVANCED_METROLOGY_INSPECTION_ORDER_BRIDGE_AND_VALUATION_BLOWOFF_ROUTER","symbol":"140860","name":"파크시스템스","trigger_type":"Stage2-Actionable-Guarded","trigger_family":"advanced_metrology_quality_order_bridge_post_reset_rerating","trigger_date":"2024-04-26","entry_date":"2024-04-29","entry_price":151600.0,"entry_price_type":"next_tradable_open_after_metrology_order_quality_reset","price_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","mfe_30d_pct":19.0,"mae_30d_pct":-3.96,"mfe_90d_pct":31.0,"mae_90d_pct":-3.96,"mfe_180d_pct":32.92,"mae_180d_pct":-3.96,"peak_price_180d":201500.0,"peak_date_180d":"2024-10-04","trough_price_180d":145600.0,"trough_date_180d":"2024-04-29","calibration_usable":true,"case_polarity":"positive_guarded_quality_holdout","evidence_url_pending":true,"source_proxy_only":true,"non_price_evidence_strength":"medium_pending_url_repair","price_only_blowoff":false,"expected_stage_current_profile":"Stage2-Guarded_to_Yellow_if_customer_order_quality_margin_bridge_repaired","residual_error_type":"quality_metrology_rerating_should_not_be_overblocked_but_green_requires_url_repaired_customer_order_margin_bridge"}
{"row_type":"trigger","research_id":"R2L75_C09_ADVANCED_METROLOGY_INSPECTION_ROUTER","round":"R2","loop":75,"large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF","fine_archetype_id":"ADVANCED_METROLOGY_INSPECTION_ORDER_BRIDGE_AND_VALUATION_BLOWOFF_ROUTER","symbol":"322310","name":"오로스테크놀로지","trigger_type":"Stage2-FalsePositive-Candidate","trigger_family":"overlay_metrology_equipment_theme_spike_without_order_bridge","trigger_date":"2024-02-26","entry_date":"2024-02-27","entry_price":36100.0,"entry_price_type":"next_tradable_open_after_overlay_metrology_theme_burst","price_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","mfe_30d_pct":12.88,"mae_30d_pct":-10.53,"mfe_90d_pct":12.88,"mae_90d_pct":-34.21,"mfe_180d_pct":12.88,"mae_180d_pct":-54.85,"peak_price_180d":40750.0,"peak_date_180d":"2024-02-27","trough_price_180d":16300.0,"trough_date_180d":"2024-08-05","calibration_usable":true,"case_polarity":"counterexample_entry_day_peak_high_mae","evidence_url_pending":true,"source_proxy_only":true,"non_price_evidence_strength":"low_pending_url_repair","price_only_blowoff":true,"expected_stage_current_profile":"blocked_Stage2_or_4B_4C_high_MAE_watch","residual_error_type":"overlay_metrology_theme_spike_peaked_on_entry_day_and_failed_without_order_customer_margin_bridge"}
{"row_type":"trigger","research_id":"R2L75_C09_ADVANCED_METROLOGY_INSPECTION_ROUTER","round":"R2","loop":75,"large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF","fine_archetype_id":"ADVANCED_METROLOGY_INSPECTION_ORDER_BRIDGE_AND_VALUATION_BLOWOFF_ROUTER","symbol":"348210","name":"넥스틴","trigger_type":"Stage2-Actionable-Guarded","trigger_family":"inspection_equipment_recovery_label_delayed_high_mae","trigger_date":"2024-02-27","entry_date":"2024-02-28","entry_price":68900.0,"entry_price_type":"next_tradable_open_after_inspection_equipment_recovery_burst","price_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","mfe_30d_pct":13.06,"mae_30d_pct":-0.29,"mfe_90d_pct":13.06,"mae_90d_pct":-19.45,"mfe_180d_pct":13.06,"mae_180d_pct":-34.83,"peak_price_180d":77900.0,"peak_date_180d":"2024-03-04","trough_price_180d":44900.0,"trough_date_180d":"2024-08-05","calibration_usable":true,"case_polarity":"counterexample_delayed_high_mae","evidence_url_pending":true,"source_proxy_only":true,"non_price_evidence_strength":"medium_low_pending_url_repair","price_only_blowoff":false,"expected_stage_current_profile":"Stage2-Guarded_or_local_4B_watch_until_inspection_order_margin_bridge_repaired","residual_error_type":"inspection_equipment_label_had_initial_mfe_but_later_mae_blocks_yellow_green_without_customer_order_bridge"}
```

---

## 8. Score simulation and raw component breakdown

This is shadow-only and does not change production scoring.

| symbol | advanced equipment relevance | customer/order bridge | valuation reset quality | market mispricing | margin conversion | MAE risk control | information confidence | shadow total | intended route |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| `140860` | 13 | 9 | 11 | 10 | 9 | 13 | 6 | 71 | Stage2-Guarded / Yellow after evidence repair |
| `322310` | 9 | 3 | 2 | 5 | 2 | 0 | 4 | 25 | blocked Stage2 / 4B-4C high-MAE watch |
| `348210` | 10 | 5 | 5 | 6 | 4 | 3 | 5 | 38 | Stage2-Guarded or local 4B watch |

### Current calibrated profile stress test

The current calibrated profile already blocks pure price-only blowoff.  
The remaining C09 issue is **advanced-equipment label without customer/order bridge**:

```text
C09 quality holdout:
  advanced metrology relevance
  + post-reset entry
  + persistent 90D/180D MFE
  + MAE remains contained
  + URL-repaired customer/order/margin evidence
  => Stage2-Guarded / Yellow candidate, no automatic Green

C09 entry-day peak failure:
  advanced equipment theme spike
  + peak occurs at entry
  + MAE_90D <= -30%
  + no order bridge
  => block Stage2 and route to 4B/4C high-MAE watch

C09 delayed high-MAE branch:
  inspection equipment recovery label
  + first-window MFE exists
  + MAE_180D <= -30%
  + bridge evidence remains source-proxy-only
  => Stage2-Guarded at most, no Yellow/Green
```

`140860` prevents overblocking: not every advanced equipment rerating is a blowoff.  
`322310` and `348210` show why C09 needs both entry-day peak detection and delayed-MAE detection.

---

## 9. Aggregate metrics

```json
{
  "row_type": "aggregate",
  "research_id": "R2L75_C09_ADVANCED_METROLOGY_INSPECTION_ROUTER",
  "round": "R2",
  "loop": 75,
  "large_sector_id": "L2_AI_SEMICONDUCTOR_ELECTRONICS",
  "canonical_archetype_id": "C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF",
  "fine_archetype_id": "ADVANCED_METROLOGY_INSPECTION_ORDER_BRIDGE_AND_VALUATION_BLOWOFF_ROUTER",
  "case_count": 3,
  "calibration_usable_case_count": 3,
  "positive_guarded_case_count": 1,
  "counterexample_count": 2,
  "new_symbol_count": 3,
  "source_proxy_only_count": 3,
  "evidence_url_pending_count": 3,
  "avg_mfe_30d_pct": 14.98,
  "avg_mae_30d_pct": -4.93,
  "avg_mfe_90d_pct": 18.98,
  "avg_mae_90d_pct": -19.21,
  "avg_mfe_180d_pct": 19.62,
  "avg_mae_180d_pct": -31.21,
  "max_mfe_180d_pct": 32.92,
  "worst_mae_180d_pct": -54.85
}
```

---

## 10. 4B proximity split

```json
{
  "row_type": "4b_split",
  "research_id": "R2L75_C09_ADVANCED_METROLOGY_INSPECTION_ROUTER",
  "stage2_guarded_or_yellow_candidate": [
    {
      "symbol": "140860",
      "reason": "post-reset advanced metrology path had +32.92% 180D MFE with only -3.96% MAE; requires customer/order/margin evidence before Green"
    }
  ],
  "stage2_guarded_or_local_4b_watch": [
    {
      "symbol": "348210",
      "reason": "first 30D path looked acceptable, but 180D MAE reached -34.83%; requires inspection order and customer bridge repair"
    }
  ],
  "blocked_stage2_or_4c_watch": [
    {
      "symbol": "322310",
      "reason": "entry-day peak with +12.88% MFE but -54.85% 180D MAE"
    }
  ],
  "full_4b_or_green_requires_non_price_evidence": [
    "customer order and qualification",
    "advanced-node / advanced-packaging demand bridge",
    "delivery schedule and backlog visibility",
    "gross margin / operating leverage",
    "valuation reset quality after the first spike"
  ]
}
```

---

## 11. Shadow rule candidate

```yaml
row_type: canonical_archetype_rule_candidate
canonical_archetype_id: C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF
fine_archetype_id: ADVANCED_METROLOGY_INSPECTION_ORDER_BRIDGE_AND_VALUATION_BLOWOFF_ROUTER
rule_name: C09_advanced_metrology_order_bridge_vs_entry_peak_high_mae_router
production_scoring_changed: false
shadow_weight_only: true
existing_axis_tested: price_only_blowoff_blocks_positive_stage
existing_axis_strengthened: true
```

### Proposed routing logic

```text
For C09 advanced equipment / metrology / inspection cases:

Tier A: verified post-reset quality holdout
  Conditions:
    - advanced equipment relevance is backed by URL-repaired customer/order/margin evidence
    - MFE_90D >= +25%
    - MAE_90D > -10%
    - peak does not occur only on the entry day
  Routing:
    - Stage2-Actionable-Guarded allowed
    - Stage3-Yellow allowed after evidence repair
    - Green only after customer/order/margin bridge is verified

Tier B: delayed high-MAE inspection/equipment branch
  Conditions:
    - first 30D MFE is positive
    - MAE_180D <= -30%
    - evidence remains source_proxy_only
  Routing:
    - Stage2-Guarded at most
    - local 4B watch
    - no Yellow/Green

Tier C: entry-day advanced equipment spike
  Conditions:
    - peak occurs on entry day or within first 5 trading days
    - MAE_90D <= -30%
    - no repaired customer/order/margin bridge
  Routing:
    - block Stage2
    - local 4B / 4C high-MAE watch
    - count as counterexample
```

### Suggested shadow delta

```json
{
  "row_type": "shadow_weight",
  "axis": "c09_advanced_metrology_order_bridge_vs_entry_peak_high_mae_router",
  "scope": "canonical_archetype_id:C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF",
  "proposal": {
    "source_proxy_only_green_allowed": false,
    "customer_order_margin_bridge_required_for_green": true,
    "post_reset_holdout_stage2_guarded_allowed": true,
    "holdout_mfe90_threshold_pct": 25.0,
    "holdout_mae90_min_pct": -10.0,
    "delayed_high_mae_threshold_180d_pct": -30.0,
    "entry_peak_high_mae_threshold_90d_pct": -30.0,
    "entry_day_or_first5_peak_blocks_stage2_without_bridge": true,
    "positive_weight_blocked_until_url_repair": true
  },
  "confidence": "medium_low_until_url_repair",
  "apply_now": false,
  "reason": "One quality metrology holdout and two metrology/inspection high-MAE failures show that C09 should preserve post-reset low-MAE winners but block entry-day or delayed high-MAE equipment spikes without customer/order/margin evidence."
}
```

---

## 12. Residual contribution summary

```json
{
  "row_type": "residual_contribution",
  "research_id": "R2L75_C09_ADVANCED_METROLOGY_INSPECTION_ROUTER",
  "large_sector_id": "L2_AI_SEMICONDUCTOR_ELECTRONICS",
  "canonical_archetype_id": "C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF",
  "contribution": "Adds three non-top-covered C09 advanced metrology/inspection cases and separates a post-reset quality holdout from entry-day peak and delayed high-MAE equipment-label failures. C09 Green should require URL-repaired customer order, qualification, advanced-node demand, delivery/backlog, and margin evidence.",
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
  "data_quality_blocker": "All three non-price advanced equipment triggers require URL-level repair before positive weight promotion.",
  "guardrail_added": "C09 source_proxy_only cases with entry-day peak and MAE_90D <= -30% should block Stage2; delayed high-MAE cases with MAE_180D <= -30% should cap at Stage2-Guarded or local 4B until customer/order evidence is repaired."
}
```

One-line contribution:

```text
This loop adds 3 new independent cases, 2 counterexamples, and 2 residual errors for R2/L2_AI_SEMICONDUCTOR_ELECTRONICS/C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF.
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
    140860: false
    322310: false
    348210: false
  evidence_url_pending:
    140860: true
    322310: true
    348210: true
  source_proxy_only:
    140860: true
    322310: true
    348210: true
```

Limitations:

```text
- Price path is validated against Stock-Web tradable OHLC rows.
- Non-price evidence is not URL-repaired in this run.
- Therefore this artifact is useful for C09 advanced equipment / metrology / inspection residual shape and high-MAE guardrail design, but should not promote positive weights until filings, IR, customer/order data, or reports verify customer qualification, delivery/backlog, advanced-node demand, and margin conversion.
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
2. Preserve R2 / loop 75 metadata.
3. Add the cases to C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF only if parser validation passes.
4. Treat all three non-price triggers as evidence_url_pending=true and source_proxy_only=true until URL-level evidence is repaired.
5. Do not use these rows for positive weight promotion until filings/IR/customer-order/report data verifies customer qualification, order/backlog, delivery, advanced-node demand, and margin conversion.
6. Add a shadow-only rule candidate named C09_advanced_metrology_order_bridge_vs_entry_peak_high_mae_router.
7. Do not loosen Stage3-Green.
8. Add C09-specific guards:
   - source_proxy_only -> no Green
   - Green requires repaired customer/order/margin bridge
   - MFE_90D >= +25% and MAE_90D > -10% may remain Stage2-Guarded / Yellow watch after reset
   - MAE_180D <= -30% without bridge repair -> Stage2-Guarded at most / local 4B watch
   - entry-day or first-5-day peak with MAE_90D <= -30% -> block Stage2 / 4B-4C watch
9. Keep production scoring unchanged unless later batch promotion logic independently marks this axis safe.
```

---

## 15. Next round state

```text
completed_round = R2
completed_loop = 75
next_round = R3
next_loop = 75
next_large_sector_hint = L3_BATTERY_EV_GREEN_MOBILITY
round_schedule_status = valid
round_sector_consistency = pass
```
