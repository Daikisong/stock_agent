# E2R Stock-Web v12 Residual Research — R1 Loop 76

```yaml
research_session: post_calibrated_sector_archetype_residual_research
mode: historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12
completed_round: R1
completed_loop: 76
next_round: R2
next_loop: 76
large_sector_id: L1_INDUSTRIALS_INFRA_DEFENSE_GRID
canonical_archetype_id: C01_ORDER_BACKLOG_MARGIN_BRIDGE
fine_archetype_id: SHIPBUILDING_ENGINE_BACKLOG_MARGIN_LOW_MAE_AND_WEAK_MFE_ROUTER
output_file: e2r_stock_web_v12_residual_round_R1_loop_76_L1_INDUSTRIALS_INFRA_DEFENSE_GRID_C01_ORDER_BACKLOG_MARGIN_BRIDGE_research.md
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
completed_round = R13
completed_loop  = 75
large_sector_id = L10_POLICY_EVENT_CROSS_REDTEAM_MISC
canonical_archetype_id = R13_CROSS_ARCHETYPE_STAGE2_FALSE_POSITIVE_REVIEW
```

Therefore:

```text
scheduled_round = R1
scheduled_loop  = 76
```

R1 maps to:

```text
large_sector_id = L1_INDUSTRIALS_INFRA_DEFENSE_GRID
```

This run selects:

```text
canonical_archetype_id = C01_ORDER_BACKLOG_MARGIN_BRIDGE
fine_archetype_id = SHIPBUILDING_ENGINE_BACKLOG_MARGIN_LOW_MAE_AND_WEAK_MFE_ROUTER
```

This is a valid R1/L1 pairing.

---

## 1. Why this R1/C01 run

The no-repeat ledger shows C01 is the thinnest L1-related canonical archetype:

```text
C01_ORDER_BACKLOG_MARGIN_BRIDGE:
  rows: 8
  symbols: 6
  date_range: 2023-01-04~2024-07-31
  good/bad S2: 5/1
  4B/4C: 2/0
  URL/proxy: 0/3
  top covered symbols: 009540(2), 010620(2), 001440(1), 010120(1), 010140(1), 267260(1)
```

This file avoids those top-covered symbols and expands the archetype into shipbuilding / engine backlog-to-margin cases:

```text
042660 한화오션
329180 HD현대중공업
077970 STX엔진
097230 HJ중공업
```

Research question:

```text
Can C01 separate real shipbuilding/engine backlog-to-margin rerating from small-shipbuilder backlog labels where forward MFE is weak and balance-sheet or margin risk creates high MAE?
```

C01 is an order-backlog margin bridge. A backlog is not just a pile of contracts; it is a production conveyor. The model should ask whether ship price, delivery schedule, mix, cost pass-through, and margin recognition turn that backlog into earnings. If the conveyor is heavy with balance-sheet or execution friction, the label alone can fail Stage2.

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
| `042660` | 한화오션 | active_like / KOSPI | no 2024 overlap; latest listed candidate 2023-11-28 | true |
| `329180` | HD현대중공업 | active_like / KOSPI | none listed | true |
| `077970` | STX엔진 | active_like / KOSPI | 2025-04-21 candidate after selected 180D window | true for 180D |
| `097230` | HJ중공업 | active_like / KOSPI | no 2024 overlap; latest listed candidate 2019-05-23 | true |

Profile caveat:

```text
Stock-Web OHLC is raw/unadjusted marcap data.
These cases are calibration-safe for the selected 2024 30D/90D/180D windows because no listed corporate-action candidate overlaps each entry~D+180 test window.
For 077970, 1Y/2Y fields would be contaminated_or_unavailable by the later 2025-04-21 corporate-action candidate, but the selected 180D window remains usable.
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
The Stock-Web price path is fully validated, but company-level order backlog quality, ship price / contract margin, engine delivery schedule, cost pass-through, labor and steel cost control, execution risk, working capital, and balance-sheet evidence still require later URL repair through filings, IR decks, order disclosures, industry data, or sell-side reports before production weight promotion.
```

C01 interpretation used here:

```text
C01 is not simply “shipbuilding stock rose.”
It asks whether backlog becomes earnings:
- backlog quality and customer mix,
- newbuilding price / contract margin,
- delivery schedule and production slot visibility,
- engine or component delivery leverage,
- cost pass-through and execution risk,
- working capital and balance-sheet trust,
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
042660 + C01_ORDER_BACKLOG_MARGIN_BRIDGE -> no direct match found
329180 + C01_ORDER_BACKLOG_MARGIN_BRIDGE -> no direct match found
077970 + C01_ORDER_BACKLOG_MARGIN_BRIDGE -> no direct match found
097230 + C01_ORDER_BACKLOG_MARGIN_BRIDGE -> no direct match found
```

Novelty accounting:

```json
{
  "new_symbol_count": 4,
  "minimum_new_symbol_count": 2,
  "positive_case_count": 3,
  "counterexample_count": 1,
  "new_independent_case_ratio": 1.00,
  "duplicate_status": "pass",
  "data_quality_status": "source_proxy_only_non_price_evidence"
}
```

---

## 5. Case design

| case_id | symbol | trigger family | research role |
|---|---|---|---|
| `R1L76_C01_042660_20240227` | `042660` 한화오션 | shipbuilding backlog / margin repair | positive-guarded |
| `R1L76_C01_329180_20240227` | `329180` HD현대중공업 | large shipbuilder backlog / delivery leverage | positive anchor |
| `R1L76_C01_077970_20240222` | `077970` STX엔진 | ship engine order / delivery late-MFE path | positive-guarded late-MFE |
| `R1L76_C01_097230_20240227` | `097230` HJ중공업 | small shipbuilder backlog label with balance-sheet drag | weak-MFE high-MAE counterexample |

The intended residual:

```text
C01 should separate:
1. large/quality shipbuilding backlog cases where MFE expands and MAE stays contained;
2. engine backlog cases where MFE arrives later but MAE remains controlled;
3. small-shipbuilder labels where backlog relevance is not enough and forward path shows weak MFE with high MAE.
```

---

## 6. Stock-Web OHLC and backtest

### 6.1 `042660` 한화오션 — shipbuilding backlog / margin repair low-MAE rerating

Trigger:

```text
trigger_date = 2024-02-26
trigger_type = Stage2-Actionable-Guarded
trigger_family = shipbuilding_order_backlog_margin_repair_low_mae_rerating
entry_date = 2024-02-27
entry_price = 23050.0
entry_price_type = next_tradable_open_after_shipbuilding_backlog_margin_burst
```

Relevant Stock-Web rows:

```csv
d,o,h,l,c,v,a,mc,s,m
2024-02-26,22000.0,22950.0,21800.0,22950.0,1106711.0,24903248550.0,7030936732050.0,306358899,KOSPI
2024-02-27,23050.0,24350.0,22550.0,24150.0,2288524.0,54331217100.0,7398567410850.0,306358899,KOSPI
2024-03-06,22500.0,22800.0,22250.0,22300.0,637436.0,14326323800.0,6831803447700.0,306358899,KOSPI
2024-03-22,30350.0,30900.0,29550.0,30700.0,1607646.0,48908602600.0,9405218199300.0,306358899,KOSPI
2024-04-24,35050.0,36400.0,34100.0,34450.0,5335817.0,187870371200.0,10554064070550.0,306358899,KOSPI
2024-08-05,30200.0,30200.0,25400.0,26950.0,3510391.0,99037942450.0,8257840968300.0,306413394,KOSPI
2024-08-21,32350.0,33800.0,32250.0,33200.0,2408540.0,79854790300.0,10172924680800.0,306413394,KOSPI
```

Backtest:

| window | peak/high | peak date | trough/low | trough date | MFE | MAE |
|---|---:|---|---:|---|---:|---:|
| 30 calendar days | 30900 | 2024-03-22 | 22250 | 2024-03-06 | +34.06% | -3.47% |
| 90 calendar days | 36400 | 2024-04-24 | 22250 | 2024-03-06 | +57.92% | -3.47% |
| 180 calendar days | 36400 | 2024-04-24 | 22250 | 2024-03-06 | +57.92% | -3.47% |

Interpretation:

```text
042660 is a positive-guarded C01 backlog/margin case.
The forward path expanded MFE across the first 90D while keeping MAE contained.
This can support Stage2-Guarded / Yellow-after-repair, but Green still requires URL-repaired order backlog, ship-price, delivery, cost, and margin evidence.
```

### 6.2 `329180` HD현대중공업 — large shipbuilder backlog / delivery leverage positive anchor

Trigger:

```text
trigger_date = 2024-02-26
trigger_type = Stage2-Actionable
trigger_family = large_shipbuilder_backlog_margin_delivery_leverage_rerating
entry_date = 2024-02-27
entry_price = 110400.0
entry_price_type = next_tradable_open_after_shipbuilding_backlog_margin_burst
```

Relevant Stock-Web rows:

```csv
d,o,h,l,c,v,a,mc,s,m
2024-02-26,110500.0,111400.0,109200.0,109700.0,107007.0,11779258900.0,9738410825200.0,88773116,KOSPI
2024-02-27,110400.0,115500.0,108800.0,114900.0,244823.0,27844907000.0,10200031028400.0,88773116,KOSPI
2024-03-20,122800.0,127800.0,122800.0,125800.0,172740.0,21722751500.0,11167657992800.0,88773116,KOSPI
2024-05-13,138400.0,146000.0,137200.0,143500.0,358025.0,51240585000.0,12738942146000.0,88773116,KOSPI
2024-07-26,184500.0,210000.0,183500.0,207500.0,1077171.0,214368171500.0,18420421570000.0,88773116,KOSPI
2024-08-09,221000.0,222500.0,208000.0,212000.0,323259.0,68988874000.0,18819900592000.0,88773116,KOSPI
2024-08-26,196200.0,197300.0,189200.0,191100.0,310304.0,59380385200.0,16964542467600.0,88773116,KOSPI
```

Backtest:

| window | peak/high | peak date | trough/low | trough date | MFE | MAE |
|---|---:|---|---:|---|---:|---:|
| 30 calendar days | 127800 | 2024-03-20 | 108800 | 2024-02-27 | +15.76% | -1.45% |
| 90 calendar days | 146000 | 2024-05-13 | 108800 | 2024-02-27 | +32.25% | -1.45% |
| 180 calendar days | 222500 | 2024-08-09 | 108800 | 2024-02-27 | +101.54% | -1.45% |

Interpretation:

```text
329180 is the C01 positive anchor.
The order-backlog/margin thesis became persistent price strength with minimal MAE.
The case is useful because it shows that C01 should not underweight high-quality backlog names; the guard is not against shipbuilding, but against backlog labels without delivery/margin conversion evidence.
```

### 6.3 `077970` STX엔진 — engine backlog late-MFE path

Trigger:

```text
trigger_date = 2024-02-21
trigger_type = Stage2-Actionable-Guarded
trigger_family = ship_engine_order_delivery_late_mfe_backlog_margin_rerating
entry_date = 2024-02-22
entry_price = 12900.0
entry_price_type = next_tradable_open_after_engine_backlog_delivery_burst
```

Relevant Stock-Web rows:

```csv
d,o,h,l,c,v,a,mc,s,m
2024-02-21,12490.0,12550.0,12300.0,12440.0,29967.0,376307350.0,286230765760.0,23008904,KOSPI
2024-02-22,12900.0,12960.0,12350.0,12900.0,78516.0,993915310.0,296814861600.0,23008904,KOSPI
2024-03-21,13850.0,13900.0,13310.0,13420.0,79711.0,1073599780.0,308779491680.0,23008904,KOSPI
2024-04-11,12700.0,12970.0,12310.0,12420.0,20894.0,260871350.0,285770587680.0,23008904,KOSPI
2024-04-24,14900.0,15730.0,14390.0,14860.0,711011.0,10810198880.0,341912313440.0,23008904,KOSPI
2024-08-05,15000.0,15050.0,12880.0,13690.0,263744.0,3655181240.0,314991895760.0,23008904,KOSPI
2024-08-19,22250.0,24400.0,21200.0,23000.0,4250385.0,93443077200.0,529204792000.0,23008904,KOSPI
```

Backtest:

| window | peak/high | peak date | trough/low | trough date | MFE | MAE |
|---|---:|---|---:|---|---:|---:|
| 30 calendar days | 13900 | 2024-03-21 | 12350 | 2024-02-22 | +7.75% | -4.26% |
| 90 calendar days | 15730 | 2024-04-24 | 12310 | 2024-04-11 | +21.94% | -4.57% |
| 180 calendar days | 24400 | 2024-08-19 | 12310 | 2024-04-11 | +89.15% | -4.57% |

Interpretation:

```text
077970 is a late-MFE positive-guarded case.
The first 30D window was not explosive, but MAE stayed controlled and the 180D window eventually captured large engine/order leverage.
C01 should preserve this path, but Yellow/Green still needs order, delivery schedule, engine margin, and customer evidence repair.
```

### 6.4 `097230` HJ중공업 — small shipbuilder backlog label with weak MFE and high MAE

Trigger:

```text
trigger_date = 2024-02-26
trigger_type = Stage2-FalsePositive-Candidate
trigger_family = small_shipbuilder_backlog_label_weak_mfe_balance_sheet_drag
entry_date = 2024-02-27
entry_price = 3600.0
entry_price_type = next_tradable_open_after_small_shipbuilder_backlog_label
```

Relevant Stock-Web rows:

```csv
d,o,h,l,c,v,a,mc,s,m
2024-02-26,3585.0,3600.0,3540.0,3600.0,21614.0,77036850.0,299787411600.0,83274281,KOSPI
2024-02-27,3600.0,3600.0,3520.0,3525.0,29246.0,103578590.0,293541840525.0,83274281,KOSPI
2024-03-13,3480.0,3720.0,3410.0,3420.0,46484.0,161034085.0,284798041020.0,83274281,KOSPI
2024-03-19,3335.0,3370.0,3250.0,3280.0,74737.0,245507685.0,273139641680.0,83274281,KOSPI
2024-04-16,3020.0,3045.0,2875.0,2890.0,129522.0,378794970.0,240662672090.0,83274281,KOSPI
2024-07-23,3590.0,3775.0,3500.0,3540.0,1125134.0,4080027505.0,294790954740.0,83274281,KOSPI
2024-08-05,3010.0,3100.0,2700.0,2790.0,305881.0,893896785.0,232335243990.0,83274281,KOSPI
```

Backtest:

| window | peak/high | peak date | trough/low | trough date | MFE | MAE |
|---|---:|---|---:|---|---:|---:|
| 30 calendar days | 3720 | 2024-03-13 | 3250 | 2024-03-19 | +3.33% | -9.72% |
| 90 calendar days | 3720 | 2024-03-13 | 2875 | 2024-04-16 | +3.33% | -20.14% |
| 180 calendar days | 3775 | 2024-07-23 | 2700 | 2024-08-05 | +4.86% | -25.00% |

Interpretation:

```text
097230 is the C01 counterexample.
The backlog/shipbuilding label existed, but forward MFE stayed weak while 90D/180D MAE widened.
This should block Green and usually block Stage2 unless a later, independent trigger repairs backlog quality, delivery, balance-sheet, and margin evidence.
```

---

## 7. Machine-readable trigger JSONL

```jsonl
{"row_type":"trigger","research_id":"R1L76_C01_SHIPBUILDING_BACKLOG_MARGIN_ROUTER","round":"R1","loop":76,"large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C01_ORDER_BACKLOG_MARGIN_BRIDGE","fine_archetype_id":"SHIPBUILDING_ENGINE_BACKLOG_MARGIN_LOW_MAE_AND_WEAK_MFE_ROUTER","symbol":"042660","name":"한화오션","trigger_type":"Stage2-Actionable-Guarded","trigger_family":"shipbuilding_order_backlog_margin_repair_low_mae_rerating","trigger_date":"2024-02-26","entry_date":"2024-02-27","entry_price":23050.0,"entry_price_type":"next_tradable_open_after_shipbuilding_backlog_margin_burst","price_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","mfe_30d_pct":34.06,"mae_30d_pct":-3.47,"mfe_90d_pct":57.92,"mae_90d_pct":-3.47,"mfe_180d_pct":57.92,"mae_180d_pct":-3.47,"peak_price_180d":36400.0,"peak_date_180d":"2024-04-24","trough_price_180d":22250.0,"trough_date_180d":"2024-03-06","calibration_usable":true,"case_polarity":"positive_guarded_shipbuilding_low_mae","evidence_url_pending":true,"source_proxy_only":true,"non_price_evidence_strength":"medium_pending_url_repair","price_only_blowoff":false,"expected_stage_current_profile":"Stage2-Guarded_to_Yellow_if_order_backlog_ship_price_margin_bridge_repaired","residual_error_type":"shipbuilding_order_backlog_path_had_persistent_mfe_but_green_requires_url_repaired_backlog_delivery_margin_bridge"}
{"row_type":"trigger","research_id":"R1L76_C01_SHIPBUILDING_BACKLOG_MARGIN_ROUTER","round":"R1","loop":76,"large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C01_ORDER_BACKLOG_MARGIN_BRIDGE","fine_archetype_id":"SHIPBUILDING_ENGINE_BACKLOG_MARGIN_LOW_MAE_AND_WEAK_MFE_ROUTER","symbol":"329180","name":"HD현대중공업","trigger_type":"Stage2-Actionable","trigger_family":"large_shipbuilder_backlog_margin_delivery_leverage_rerating","trigger_date":"2024-02-26","entry_date":"2024-02-27","entry_price":110400.0,"entry_price_type":"next_tradable_open_after_shipbuilding_backlog_margin_burst","price_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","mfe_30d_pct":15.76,"mae_30d_pct":-1.45,"mfe_90d_pct":32.25,"mae_90d_pct":-1.45,"mfe_180d_pct":101.54,"mae_180d_pct":-1.45,"peak_price_180d":222500.0,"peak_date_180d":"2024-08-09","trough_price_180d":108800.0,"trough_date_180d":"2024-02-27","calibration_usable":true,"case_polarity":"positive_anchor_large_shipbuilder_low_mae","evidence_url_pending":true,"source_proxy_only":true,"non_price_evidence_strength":"medium_pending_url_repair","price_only_blowoff":false,"expected_stage_current_profile":"Stage2-Actionable_to_Yellow_after_order_backlog_delivery_margin_bridge_repaired","residual_error_type":"large_shipbuilder_backlog_margin_path_supports_positive_route_but_green_requires_url_repaired_margin_delivery_evidence"}
{"row_type":"trigger","research_id":"R1L76_C01_SHIPBUILDING_BACKLOG_MARGIN_ROUTER","round":"R1","loop":76,"large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C01_ORDER_BACKLOG_MARGIN_BRIDGE","fine_archetype_id":"SHIPBUILDING_ENGINE_BACKLOG_MARGIN_LOW_MAE_AND_WEAK_MFE_ROUTER","symbol":"077970","name":"STX엔진","trigger_type":"Stage2-Actionable-Guarded","trigger_family":"ship_engine_order_delivery_late_mfe_backlog_margin_rerating","trigger_date":"2024-02-21","entry_date":"2024-02-22","entry_price":12900.0,"entry_price_type":"next_tradable_open_after_engine_backlog_delivery_burst","price_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","mfe_30d_pct":7.75,"mae_30d_pct":-4.26,"mfe_90d_pct":21.94,"mae_90d_pct":-4.57,"mfe_180d_pct":89.15,"mae_180d_pct":-4.57,"peak_price_180d":24400.0,"peak_date_180d":"2024-08-19","trough_price_180d":12310.0,"trough_date_180d":"2024-04-11","calibration_usable":true,"case_polarity":"positive_guarded_late_mfe_engine_backlog","evidence_url_pending":true,"source_proxy_only":true,"non_price_evidence_strength":"medium_low_pending_url_repair","price_only_blowoff":false,"expected_stage_current_profile":"Stage2-Guarded_to_Yellow_if_engine_order_delivery_margin_bridge_repaired","residual_error_type":"engine_backlog_late_mfe_path_should_not_be_overblocked_but_green_requires_url_repaired_order_delivery_margin_bridge"}
{"row_type":"trigger","research_id":"R1L76_C01_SHIPBUILDING_BACKLOG_MARGIN_ROUTER","round":"R1","loop":76,"large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C01_ORDER_BACKLOG_MARGIN_BRIDGE","fine_archetype_id":"SHIPBUILDING_ENGINE_BACKLOG_MARGIN_LOW_MAE_AND_WEAK_MFE_ROUTER","symbol":"097230","name":"HJ중공업","trigger_type":"Stage2-FalsePositive-Candidate","trigger_family":"small_shipbuilder_backlog_label_weak_mfe_balance_sheet_drag","trigger_date":"2024-02-26","entry_date":"2024-02-27","entry_price":3600.0,"entry_price_type":"next_tradable_open_after_small_shipbuilder_backlog_label","price_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","mfe_30d_pct":3.33,"mae_30d_pct":-9.72,"mfe_90d_pct":3.33,"mae_90d_pct":-20.14,"mfe_180d_pct":4.86,"mae_180d_pct":-25.0,"peak_price_180d":3775.0,"peak_date_180d":"2024-07-23","trough_price_180d":2700.0,"trough_date_180d":"2024-08-05","calibration_usable":true,"case_polarity":"counterexample_weak_mfe_high_mae","evidence_url_pending":true,"source_proxy_only":true,"non_price_evidence_strength":"low_pending_url_repair","price_only_blowoff":false,"expected_stage_current_profile":"blocked_Stage2_or_local_4B_watch_until_balance_sheet_margin_bridge_repaired","residual_error_type":"small_shipbuilder_backlog_label_had_weak_mfe_and_high_mae_without_backlog_delivery_balance_sheet_margin_bridge"}
```

---

## 8. Score simulation and raw component breakdown

This is shadow-only and does not change production scoring.

| symbol | backlog quality | delivery visibility | contract margin | cost / pass-through control | market mispricing | balance-sheet trust | information confidence | shadow total | intended route |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| `329180` | 14 | 13 | 12 | 10 | 14 | 10 | 6 | 79 | Stage2/Yellow after evidence repair |
| `042660` | 12 | 10 | 9 | 8 | 12 | 7 | 6 | 64 | Stage2-Guarded / Yellow after evidence repair |
| `077970` | 10 | 8 | 8 | 7 | 12 | 6 | 5 | 56 | Stage2-Guarded; late-MFE holdout |
| `097230` | 5 | 4 | 3 | 3 | 2 | 2 | 4 | 23 | blocked Stage2 / local 4B watch |

### Current calibrated profile stress test

The current calibrated profile already blocks pure price-only blowoff.  
The remaining C01 issue is **backlog label without margin/delivery conversion**:

```text
C01 high-quality backlog path:
  order backlog / delivery leverage
  + MFE expands across 90D/180D
  + MAE remains contained
  + URL-repaired backlog quality, delivery schedule, cost and margin evidence
  => Stage2-Actionable / Yellow candidate, possible Green after proof

C01 late-MFE engine path:
  engine/backlog label initially modest
  + MAE remains contained
  + later MFE expands strongly
  => Stage2-Guarded, no Green until order/delivery/margin evidence repair

C01 weak-MFE small shipbuilder path:
  shipbuilding/backlog label exists
  + MFE_90D < +5%
  + MAE_90D <= -20%
  + balance-sheet / margin bridge missing
  => block Stage2 or local 4B watch
```

`329180`, `042660`, and `077970` prevent overblocking.  
`097230` shows why C01 must demand margin/delivery/balance-sheet proof rather than promoting every backlog-adjacent shipbuilding label.

---

## 9. Aggregate metrics

```json
{
  "row_type": "aggregate",
  "research_id": "R1L76_C01_SHIPBUILDING_BACKLOG_MARGIN_ROUTER",
  "round": "R1",
  "loop": 76,
  "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID",
  "canonical_archetype_id": "C01_ORDER_BACKLOG_MARGIN_BRIDGE",
  "fine_archetype_id": "SHIPBUILDING_ENGINE_BACKLOG_MARGIN_LOW_MAE_AND_WEAK_MFE_ROUTER",
  "case_count": 4,
  "calibration_usable_case_count": 4,
  "positive_case_count": 3,
  "counterexample_count": 1,
  "new_symbol_count": 4,
  "source_proxy_only_count": 4,
  "evidence_url_pending_count": 4,
  "avg_mfe_30d_pct": 15.23,
  "avg_mae_30d_pct": -4.73,
  "avg_mfe_90d_pct": 28.86,
  "avg_mae_90d_pct": -7.41,
  "avg_mfe_180d_pct": 63.37,
  "avg_mae_180d_pct": -8.62,
  "max_mfe_180d_pct": 101.54,
  "worst_mae_180d_pct": -25.0
}
```

---

## 10. 4B proximity split

```json
{
  "row_type": "4b_split",
  "research_id": "R1L76_C01_SHIPBUILDING_BACKLOG_MARGIN_ROUTER",
  "stage2_positive_or_yellow_candidate": [
    {
      "symbol": "329180",
      "reason": "large shipbuilder backlog path had +101.54% 180D MFE with only -1.45% MAE"
    },
    {
      "symbol": "042660",
      "reason": "shipbuilding margin-repair path had +57.92% MFE with only -3.47% MAE"
    },
    {
      "symbol": "077970",
      "reason": "engine backlog path had late +89.15% MFE with only -4.57% 180D MAE"
    }
  ],
  "blocked_stage2_or_local_4b_watch": [
    {
      "symbol": "097230",
      "reason": "MFE stayed only +4.86% while 90D MAE reached -20.14% and 180D MAE reached -25.00%"
    }
  ],
  "full_4b_or_green_requires_non_price_evidence": [
    "order backlog quality and customer mix",
    "newbuilding price / contract margin",
    "delivery schedule and production slot visibility",
    "engine or component delivery leverage",
    "steel/labor/input-cost pass-through",
    "working capital and balance-sheet trust"
  ]
}
```

---

## 11. Shadow rule candidate

```yaml
row_type: canonical_archetype_rule_candidate
canonical_archetype_id: C01_ORDER_BACKLOG_MARGIN_BRIDGE
fine_archetype_id: SHIPBUILDING_ENGINE_BACKLOG_MARGIN_LOW_MAE_AND_WEAK_MFE_ROUTER
rule_name: C01_shipbuilding_engine_backlog_margin_low_mae_and_weak_mfe_router
production_scoring_changed: false
shadow_weight_only: true
```

### Proposed routing logic

```text
For C01 shipbuilding / engine backlog-to-margin cases:

Tier A: verified backlog-to-margin winner
  Conditions:
    - backlog quality, delivery schedule, contract margin, and cost/pass-through evidence are URL-repaired
    - MFE_90D >= +25%
    - MAE_90D > -8%
    - MFE persists beyond one event candle
  Routing:
    - Stage2-Actionable allowed
    - Stage3-Yellow allowed after evidence repair
    - Green only after backlog/delivery/margin bridge is verified

Tier B: source-proxy-only low-MAE backlog path
  Conditions:
    - MFE_90D >= +20%
    - MAE_90D > -10%
    - evidence_url_pending or source_proxy_only remains true
  Routing:
    - Stage2-Guarded allowed
    - no Green until evidence repair

Tier C: late-MFE engine/order path
  Conditions:
    - MFE_180D >= +50%
    - MAE_180D > -10%
    - MFE_30D is modest but not negative
    - bridge evidence remains pending
  Routing:
    - Stage2-Guarded / Yellow watch
    - require order/delivery/margin evidence before promotion

Tier D: weak-MFE backlog-label failure
  Conditions:
    - MFE_90D < +5%
    - MAE_90D <= -20% or MAE_180D <= -25%
    - balance-sheet or margin bridge missing
  Routing:
    - block Stage2 or local 4B watch
    - count as counterexample
```

### Suggested shadow delta

```json
{
  "row_type": "shadow_weight",
  "axis": "c01_shipbuilding_engine_backlog_margin_low_mae_and_weak_mfe_router",
  "scope": "canonical_archetype_id:C01_ORDER_BACKLOG_MARGIN_BRIDGE",
  "proposal": {
    "source_proxy_only_green_allowed": false,
    "backlog_delivery_margin_bridge_required_for_green": true,
    "verified_backlog_mfe90_threshold_pct": 25.0,
    "verified_backlog_mae90_min_pct": -8.0,
    "source_proxy_low_mae_mfe90_threshold_pct": 20.0,
    "source_proxy_low_mae_mae90_min_pct": -10.0,
    "late_mfe_engine_mfe180_threshold_pct": 50.0,
    "late_mfe_engine_mae180_min_pct": -10.0,
    "weak_mfe_threshold_90d_pct": 5.0,
    "weak_mfe_mae90_threshold_pct": -20.0,
    "weak_mfe_mae180_threshold_pct": -25.0,
    "positive_weight_blocked_until_url_repair": true
  },
  "confidence": "medium_low_until_url_repair",
  "apply_now": false,
  "reason": "Three non-top-covered shipbuilding/engine backlog positives and one small-shipbuilder weak-MFE/high-MAE counterexample show that C01 should require URL-repaired backlog, delivery, cost/pass-through, margin, and balance-sheet evidence before Yellow/Green."
}
```

---

## 12. Residual contribution summary

```json
{
  "row_type": "residual_contribution",
  "research_id": "R1L76_C01_SHIPBUILDING_BACKLOG_MARGIN_ROUTER",
  "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID",
  "canonical_archetype_id": "C01_ORDER_BACKLOG_MARGIN_BRIDGE",
  "contribution": "Adds four non-top-covered C01 shipbuilding/engine backlog-to-margin cases and separates high-quality low-MAE backlog rerating from small-shipbuilder weak-MFE balance-sheet/margin failure. C01 Yellow/Green should require URL-repaired backlog quality, delivery schedule, contract margin, cost pass-through, working-capital, and balance-sheet trust evidence.",
  "positive_case_added": 3,
  "counterexample_case_added": 1,
  "new_symbol_count": 4,
  "new_independent_case_count": 4,
  "reused_case_count": 0,
  "same_archetype_new_symbol_count": 4,
  "same_archetype_new_trigger_family_count": 4,
  "new_trigger_family_count": 4,
  "current_profile_error_count": 1,
  "diversity_score_summary": {
    "new_symbol_bonus": 12,
    "counterexample_gap_bonus": 4,
    "residual_error_bonus": 5,
    "wrong_round_penalty": 0,
    "repeated_same_symbol_penalty": 0,
    "net_interpretive_score": 21
  },
  "loop_contribution_label": "canonical_archetype_rule_candidate",
  "do_not_propose_new_weight_delta": false,
  "data_quality_blocker": "All four non-price backlog/margin triggers require URL-level repair before positive weight promotion.",
  "guardrail_added": "C01 source_proxy_only backlog-label cases with MFE_90D < +5% and MAE_90D <= -20% should block Stage2 or route to local 4B watch; low-MAE high-MFE shipbuilding/engine paths may remain Stage2-Guarded until backlog/delivery/margin evidence is repaired."
}
```

One-line contribution:

```text
This loop adds 4 new independent cases, 1 counterexample, and 1 residual error for R1/L1_INDUSTRIALS_INFRA_DEFENSE_GRID/C01_ORDER_BACKLOG_MARGIN_BRIDGE.
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
    042660: false
    329180: false
    077970: false
    097230: false
  evidence_url_pending:
    042660: true
    329180: true
    077970: true
    097230: true
  source_proxy_only:
    042660: true
    329180: true
    077970: true
    097230: true
  special_handling:
    077970:
      corporate_action_candidate_date: "2025-04-21"
      note: "Candidate date is after selected entry~D+180 window; 1Y/2Y fields would be contaminated_or_unavailable."
```

Limitations:

```text
- Price path is validated against Stock-Web tradable OHLC rows.
- Non-price evidence is not URL-repaired in this run.
- Therefore this artifact is useful for C01 shipbuilding/engine backlog-to-margin residual shape and weak-MFE guardrail design, but should not promote positive weights until filings, IR, order disclosures, industry data, or reports verify backlog quality, delivery schedule, contract margin, cost/pass-through, working capital, and balance-sheet trust.
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
2. Preserve R1 / loop 76 metadata.
3. Add the cases to C01_ORDER_BACKLOG_MARGIN_BRIDGE only if parser validation passes.
4. Treat all four non-price triggers as evidence_url_pending=true and source_proxy_only=true until URL-level evidence is repaired.
5. Do not use these rows for positive weight promotion until filings/IR/order-disclosure/industry-data/report data verifies backlog quality, customer mix, delivery schedule, contract margin, cost pass-through, working capital, and balance-sheet trust.
6. Add a shadow-only rule candidate named C01_shipbuilding_engine_backlog_margin_low_mae_and_weak_mfe_router.
7. Do not loosen Stage3-Green.
8. Add C01-specific guards:
   - source_proxy_only -> no Green
   - Green requires repaired backlog / delivery / margin bridge
   - MFE_90D >= +25% and MAE_90D > -8% may remain Stage2-Actionable / Yellow watch after evidence repair
   - MFE_90D >= +20% and MAE_90D > -10% may remain Stage2-Guarded while evidence is pending
   - MFE_180D >= +50% and MAE_180D > -10% may remain late-MFE engine/order holdout
   - MFE_90D < +5% and MAE_90D <= -20% or MAE_180D <= -25% -> block Stage2 or local 4B watch
9. Keep production scoring unchanged unless later batch promotion logic independently marks this axis safe.
```

---

## 15. Next round state

```text
completed_round = R1
completed_loop = 76
next_round = R2
next_loop = 76
next_large_sector_hint = L2_AI_SEMICONDUCTOR_ELECTRONICS
round_schedule_status = valid
round_sector_consistency = pass
```
