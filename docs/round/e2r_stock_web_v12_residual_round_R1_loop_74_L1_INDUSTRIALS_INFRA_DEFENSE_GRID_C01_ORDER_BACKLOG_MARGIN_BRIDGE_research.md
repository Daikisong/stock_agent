# E2R Stock-Web v12 Residual Research — R1 Loop 74

```yaml
research_session: post_calibrated_sector_archetype_residual_research
mode: historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12
completed_round: R1
completed_loop: 74
next_round: R2
next_loop: 74
large_sector_id: L1_INDUSTRIALS_INFRA_DEFENSE_GRID
canonical_archetype_id: C01_ORDER_BACKLOG_MARGIN_BRIDGE
fine_archetype_id: SHIP_ENGINE_LNG_EQUIPMENT_BACKLOG_MARGIN_BRIDGE_AND_OFFSHORE_WIND_SLOW_FADE_ROUTER
output_file: e2r_stock_web_v12_residual_round_R1_loop_74_L1_INDUSTRIALS_INFRA_DEFENSE_GRID_C01_ORDER_BACKLOG_MARGIN_BRIDGE_research.md
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
completed_loop  = 73
large_sector_id = L10_POLICY_EVENT_CROSS_REDTEAM_MISC
canonical_archetype_id = R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL
```

Therefore:

```text
scheduled_round = R1
scheduled_loop  = 74
```

R1 maps to:

```text
large_sector_id = L1_INDUSTRIALS_INFRA_DEFENSE_GRID
```

This run selects:

```text
canonical_archetype_id = C01_ORDER_BACKLOG_MARGIN_BRIDGE
fine_archetype_id = SHIP_ENGINE_LNG_EQUIPMENT_BACKLOG_MARGIN_BRIDGE_AND_OFFSHORE_WIND_SLOW_FADE_ROUTER
```

This is a valid R1/L1 pairing.

---

## 1. Why this R1/C01 run

The no-repeat ledger shows C01 is one of the thinnest canonical archetypes:

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

This file deliberately avoids those top-covered symbols and expands into ship-engine / LNG equipment / offshore-fabrication backlog cases:

```text
082740 한화엔진
071970 HD현대마린엔진
017960 한국카본
100090 SK오션플랜트
```

Research question:

```text
Can C01 separate real order-backlog / delivery / margin-bridge rerating from capital-goods relief rallies where orderbook relevance exists but margin conversion or project economics are not visible?
```

C01 should behave like a bridge inspector. A backlog headline is the bridge deck; the model still has to inspect the beams: delivery schedule, customer quality, pass-through pricing, cost inflation, and margin conversion. If the beams are missing, the price can bounce and still collapse under load.

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
| `082740` | 한화엔진 | active_like / KOSPI | no 2024 overlap; latest listed candidate 2022-08-25 | true |
| `071970` | HD현대마린엔진 | active_like / KOSPI | no 2024 overlap; old 2013~2018 candidates only | true |
| `017960` | 한국카본 | active_like / KOSPI | no 2024 overlap; latest listed candidate 2012-12-27 | true |
| `100090` | SK오션플랜트 | active_like / KOSPI | no 2024 overlap; latest listed candidate 2022-09-16 | true |

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
The Stock-Web price path is fully validated, but company-level order backlog, delivery schedule, engine/LNG material customer quality, offshore-wind project economics, cost pass-through, and margin conversion evidence still require later URL repair through filings, IR decks, contract disclosures, shipyard/customer data, or sell-side reports before production weight promotion.
```

C01 interpretation used here:

```text
C01 is not simply “capital goods stock rose.”
It asks whether order/backlog visibility converts into:
- delivery schedule,
- revenue recognition,
- customer quality,
- pricing/cost pass-through,
- gross margin and operating margin bridge,
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
082740 + C01_ORDER_BACKLOG_MARGIN_BRIDGE -> no direct match found
071970 + C01_ORDER_BACKLOG_MARGIN_BRIDGE -> no direct match found
017960 + C01_ORDER_BACKLOG_MARGIN_BRIDGE -> no direct match found
100090 + C01_ORDER_BACKLOG_MARGIN_BRIDGE -> no direct match found
```

Novelty accounting:

```json
{
  "new_symbol_count": 4,
  "minimum_new_symbol_count": 2,
  "positive_guarded_case_count": 3,
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
| `R1L74_C01_082740_20240315` | `082740` 한화엔진 | ship-engine backlog / delayed margin bridge rerating | positive-guarded / delayed rerating |
| `R1L74_C01_071970_20240716` | `071970` HD현대마린엔진 | marine-engine backlog repricing after group integration theme | positive-guarded high-MFE |
| `R1L74_C01_017960_20240724` | `017960` 한국카본 | LNG insulation / materials order backlog and margin bridge | positive-guarded low-MAE |
| `R1L74_C01_100090_20240605` | `100090` SK오션플랜트 | offshore-wind fabrication orderbook relief slow fade | counterexample / high-MAE guard |

The intended residual:

```text
C01 should separate:
1. engine/LNG equipment backlog cases where MFE persists and MAE remains controlled;
2. delayed-rerating cases where 30D is weak but 90D/180D proves the order bridge;
3. offshore-wind / capital-goods relief spikes where project economics and margin bridge fail to hold the path.
```

---

## 6. Stock-Web OHLC and backtest

### 6.1 `082740` 한화엔진 — ship-engine backlog / delayed rerating

Trigger:

```text
trigger_date = 2024-03-14
trigger_type = Stage2-Actionable-Guarded
trigger_family = ship_engine_backlog_margin_bridge_delayed_rerating
entry_date = 2024-03-15
entry_price = 9670.0
entry_price_type = next_tradable_open_after_engine_backlog_burst
```

Relevant Stock-Web rows:

```csv
d,o,h,l,c,v,a,mc,s,m
2024-03-14,8770.0,9750.0,8770.0,9570.0,1753653.0,16518463490.0,684676022580.0,71543994,KOSPI
2024-03-15,9670.0,9910.0,9320.0,9500.0,1058960.0,10165497710.0,679667943000.0,71543994,KOSPI
2024-03-22,10130.0,10220.0,9910.0,10150.0,492442.0,4984215460.0,846988491300.0,83447142,KOSPI
2024-04-11,9500.0,9550.0,9270.0,9480.0,288274.0,2706494420.0,791078906160.0,83447142,KOSPI
2024-04-24,12710.0,13890.0,12410.0,12450.0,14705861.0,192824678030.0,1038916917900.0,83447142,KOSPI
2024-06-25,16030.0,16990.0,15500.0,15820.0,3149498.0,51615270420.0,1320133786440.0,83447142,KOSPI
2024-07-24,16900.0,17160.0,15880.0,15880.0,2372324.0,39414357710.0,1325140614960.0,83447142,KOSPI
2024-09-06,12010.0,12090.0,11510.0,11960.0,634660.0,7496186670.0,998027818320.0,83447142,KOSPI
```

Backtest:

| window | peak/high | peak date | trough/low | trough date | MFE | MAE |
|---|---:|---|---:|---|---:|---:|
| 30 calendar days | 10220 | 2024-03-22 | 9270 | 2024-04-11 | +5.69% | -4.14% |
| 90 calendar days | 13890 | 2024-04-24 | 9270 | 2024-04-11 | +43.64% | -4.14% |
| 180 calendar days | 17160 | 2024-07-24 | 9270 | 2024-04-11 | +77.46% | -4.14% |

Interpretation:

```text
082740 is a delayed positive-guarded case.
The first 30 calendar days were not impressive, but the 90D/180D path became a strong low-MAE rerating.
C01 should allow this kind of delayed Stage2-Guarded path, but Green still requires URL-repaired order backlog, delivery, pricing, and margin evidence.
```

### 6.2 `071970` HD현대마린엔진 — marine-engine backlog repricing

Trigger:

```text
trigger_date = 2024-07-15
trigger_type = Stage2-Actionable-Guarded
trigger_family = marine_engine_backlog_repricing_after_group_integration_theme
entry_date = 2024-07-16
entry_price = 17730.0
entry_price_type = next_tradable_open_after_engine_theme_burst
```

Relevant Stock-Web rows:

```csv
d,o,h,l,c,v,a,mc,s,m
2024-07-15,18920.0,19980.0,17060.0,17480.0,1671261.0,30603647780.0,499100654120.0,28552669,KOSPI
2024-07-16,17730.0,21400.0,17580.0,19100.0,4903961.0,96147653030.0,545355977900.0,28552669,KOSPI
2024-07-31,23700.0,24850.0,22700.0,23050.0,1281933.0,30665929100.0,658139020450.0,28552669,KOSPI
2024-08-05,22400.0,22550.0,17910.0,20100.0,2062846.0,42235989120.0,573908646900.0,28552669,KOSPI
2024-09-06,16320.0,16360.0,15660.0,16260.0,472699.0,7590544990.0,551495932140.0,33917339,KOSPI
2025-01-03,26300.0,26700.0,24300.0,24600.0,1018200.0,25696224100.0,834468777000.0,33921495,KOSPI
2025-01-10,26000.0,27350.0,25550.0,27000.0,1654398.0,43094399850.0,915880365000.0,33921495,KOSPI
```

Backtest:

| window | peak/high | peak date | trough/low | trough date | MFE | MAE |
|---|---:|---|---:|---|---:|---:|
| 30 calendar days | 24850 | 2024-07-31 | 17580 | 2024-07-16 | +40.16% | -0.85% |
| 90 calendar days | 24850 | 2024-07-31 | 15660 | 2024-09-06 | +40.16% | -11.68% |
| 180 calendar days | 27350 | 2025-01-10 | 15660 | 2024-09-06 | +54.26% | -11.68% |

Interpretation:

```text
071970 is a high-MFE positive-guarded case.
The entry had immediate upside and later recovered to a new forward-window high after a mid-window drawdown.
This is Stage2-Guarded / Yellow after evidence repair, not Green by price alone.
```

### 6.3 `017960` 한국카본 — LNG insulation / material backlog low-MAE candidate

Trigger:

```text
trigger_date = 2024-07-23
trigger_type = Stage2-Actionable-Guarded
trigger_family = lng_insulation_material_order_backlog_margin_bridge
entry_date = 2024-07-24
entry_price = 11350.0
entry_price_type = next_tradable_open_after_lng_material_burst
```

Relevant Stock-Web rows:

```csv
d,o,h,l,c,v,a,mc,s,m
2024-07-23,11100.0,11240.0,10930.0,11220.0,291034.0,3242045730.0,582412831440.0,51908452,KOSPI
2024-07-24,11350.0,12540.0,11300.0,12180.0,4825454.0,58958943760.0,632244945360.0,51908452,KOSPI
2024-08-05,11730.0,11770.0,10230.0,10700.0,990790.0,10934570030.0,555420436400.0,51908452,KOSPI
2024-08-20,12740.0,13350.0,12600.0,13350.0,1293013.0,16920509870.0,692977834200.0,51908452,KOSPI
2024-09-05,11280.0,11290.0,10750.0,10840.0,346633.0,3795885710.0,562687619680.0,51908452,KOSPI
2025-01-15,12480.0,12760.0,12430.0,12700.0,680875.0,8587630810.0,659237340400.0,51908452,KOSPI
2025-01-20,13440.0,13500.0,13200.0,13470.0,620802.0,8300131290.0,699206848440.0,51908452,KOSPI
```

Backtest:

| window | peak/high | peak date | trough/low | trough date | MFE | MAE |
|---|---:|---|---:|---|---:|---:|
| 30 calendar days | 13350 | 2024-08-20 | 10230 | 2024-08-05 | +17.62% | -9.87% |
| 90 calendar days | 13350 | 2024-08-20 | 10230 | 2024-08-05 | +17.62% | -9.87% |
| 180 calendar days | 13500 | 2025-01-20 | 10230 | 2024-08-05 | +18.94% | -9.87% |

Interpretation:

```text
017960 is a contained-MAE positive-guarded case.
The return was not explosive, but the drawdown stayed below the severe-failure zone.
This should stay Stage2-Guarded until LNG material backlog, delivery schedule, cost pass-through, and margin evidence are repaired.
```

### 6.4 `100090` SK오션플랜트 — offshore-wind fabrication relief slow fade

Trigger:

```text
trigger_date = 2024-06-04
trigger_type = Stage2-FalsePositive-Candidate
trigger_family = offshore_wind_fabrication_orderbook_relief_slow_fade
entry_date = 2024-06-05
entry_price = 15020.0
entry_price_type = next_tradable_open_after_offshore_wind_relief_spike
```

Relevant Stock-Web rows:

```csv
d,o,h,l,c,v,a,mc,s,m
2024-06-04,16310.0,17730.0,14820.0,14850.0,8035492.0,133649724280.0,879054184800.0,59195568,KOSPI
2024-06-05,15020.0,16180.0,14460.0,15470.0,3024498.0,46908760690.0,915755436960.0,59195568,KOSPI
2024-06-21,13540.0,15550.0,13340.0,14650.0,4383420.0,64900318990.0,867215071200.0,59195568,KOSPI
2024-08-05,12350.0,12400.0,10300.0,10880.0,450975.0,5194585920.0,644047779840.0,59195568,KOSPI
2024-08-27,15120.0,15410.0,14690.0,14900.0,469607.0,7115643180.0,882013963200.0,59195568,KOSPI
2024-09-24,15520.0,16200.0,15520.0,16050.0,467884.0,7483958080.0,950088866400.0,59195568,KOSPI
2024-11-15,12350.0,12680.0,11370.0,11760.0,879694.0,10462032350.0,696139879680.0,59195568,KOSPI
2024-12-02,11570.0,11760.0,11110.0,11260.0,124906.0,1420749140.0,666542095680.0,59195568,KOSPI
```

Backtest:

| window | peak/high | peak date | trough/low | trough date | MFE | MAE |
|---|---:|---|---:|---|---:|---:|
| 30 calendar days | 16180 | 2024-06-05 | 13340 | 2024-06-21 | +7.72% | -11.19% |
| 90 calendar days | 16180 | 2024-06-05 | 10300 | 2024-08-05 | +7.72% | -31.42% |
| 180 calendar days | 16200 | 2024-09-24 | 10300 | 2024-08-05 | +7.86% | -31.42% |

Interpretation:

```text
100090 is the C01 counterexample.
Offshore-wind fabrication/orderbook relevance existed, but after the spike the remaining MFE was weak and the 90D/180D MAE crossed -30%.
This should block Stage2 or route to local 4B/high-MAE watch until project economics and margin bridge are repaired.
```

---

## 7. Machine-readable trigger JSONL

```jsonl
{"row_type":"trigger","research_id":"R1L74_C01_SHIP_ENGINE_LNG_BACKLOG_ROUTER","round":"R1","loop":74,"large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C01_ORDER_BACKLOG_MARGIN_BRIDGE","fine_archetype_id":"SHIP_ENGINE_LNG_EQUIPMENT_BACKLOG_MARGIN_BRIDGE_AND_OFFSHORE_WIND_SLOW_FADE_ROUTER","symbol":"082740","name":"한화엔진","trigger_type":"Stage2-Actionable-Guarded","trigger_family":"ship_engine_backlog_margin_bridge_delayed_rerating","trigger_date":"2024-03-14","entry_date":"2024-03-15","entry_price":9670.0,"entry_price_type":"next_tradable_open_after_engine_backlog_burst","price_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","mfe_30d_pct":5.69,"mae_30d_pct":-4.14,"mfe_90d_pct":43.64,"mae_90d_pct":-4.14,"mfe_180d_pct":77.46,"mae_180d_pct":-4.14,"peak_price_180d":17160.0,"peak_date_180d":"2024-07-24","trough_price_180d":9270.0,"trough_date_180d":"2024-04-11","calibration_usable":true,"case_polarity":"positive_guarded_delayed_rerating","evidence_url_pending":true,"source_proxy_only":true,"non_price_evidence_strength":"medium_pending_url_repair","price_only_blowoff":false,"expected_stage_current_profile":"Stage2-Guarded_to_Yellow_if_backlog_margin_delivery_bridge_repaired","residual_error_type":"delayed_rerating_requires_url_repaired_order_backlog_and_margin_bridge_before_green"}
{"row_type":"trigger","research_id":"R1L74_C01_SHIP_ENGINE_LNG_BACKLOG_ROUTER","round":"R1","loop":74,"large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C01_ORDER_BACKLOG_MARGIN_BRIDGE","fine_archetype_id":"SHIP_ENGINE_LNG_EQUIPMENT_BACKLOG_MARGIN_BRIDGE_AND_OFFSHORE_WIND_SLOW_FADE_ROUTER","symbol":"071970","name":"HD현대마린엔진","trigger_type":"Stage2-Actionable-Guarded","trigger_family":"marine_engine_backlog_repricing_after_group_integration_theme","trigger_date":"2024-07-15","entry_date":"2024-07-16","entry_price":17730.0,"entry_price_type":"next_tradable_open_after_engine_theme_burst","price_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","mfe_30d_pct":40.16,"mae_30d_pct":-0.85,"mfe_90d_pct":40.16,"mae_90d_pct":-11.68,"mfe_180d_pct":54.26,"mae_180d_pct":-11.68,"peak_price_180d":27350.0,"peak_date_180d":"2025-01-10","trough_price_180d":15660.0,"trough_date_180d":"2024-09-06","calibration_usable":true,"case_polarity":"positive_guarded_high_mfe","evidence_url_pending":true,"source_proxy_only":true,"non_price_evidence_strength":"medium_pending_url_repair","price_only_blowoff":false,"expected_stage_current_profile":"Stage2-Guarded_to_Yellow_if_engine_order_delivery_margin_bridge_repaired","residual_error_type":"high_mfe_engine_repricing_still_requires_order_margin_bridge_before_green"}
{"row_type":"trigger","research_id":"R1L74_C01_SHIP_ENGINE_LNG_BACKLOG_ROUTER","round":"R1","loop":74,"large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C01_ORDER_BACKLOG_MARGIN_BRIDGE","fine_archetype_id":"SHIP_ENGINE_LNG_EQUIPMENT_BACKLOG_MARGIN_BRIDGE_AND_OFFSHORE_WIND_SLOW_FADE_ROUTER","symbol":"017960","name":"한국카본","trigger_type":"Stage2-Actionable-Guarded","trigger_family":"lng_insulation_material_order_backlog_margin_bridge","trigger_date":"2024-07-23","entry_date":"2024-07-24","entry_price":11350.0,"entry_price_type":"next_tradable_open_after_lng_material_burst","price_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","mfe_30d_pct":17.62,"mae_30d_pct":-9.87,"mfe_90d_pct":17.62,"mae_90d_pct":-9.87,"mfe_180d_pct":18.94,"mae_180d_pct":-9.87,"peak_price_180d":13500.0,"peak_date_180d":"2025-01-20","trough_price_180d":10230.0,"trough_date_180d":"2024-08-05","calibration_usable":true,"case_polarity":"positive_guarded_low_mae","evidence_url_pending":true,"source_proxy_only":true,"non_price_evidence_strength":"medium_low_pending_url_repair","price_only_blowoff":false,"expected_stage_current_profile":"Stage2-Guarded_until_lng_order_margin_bridge_repaired","residual_error_type":"contained_mae_lng_backlog_case_but_green_requires_margin_and_delivery_evidence"}
{"row_type":"trigger","research_id":"R1L74_C01_SHIP_ENGINE_LNG_BACKLOG_ROUTER","round":"R1","loop":74,"large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C01_ORDER_BACKLOG_MARGIN_BRIDGE","fine_archetype_id":"SHIP_ENGINE_LNG_EQUIPMENT_BACKLOG_MARGIN_BRIDGE_AND_OFFSHORE_WIND_SLOW_FADE_ROUTER","symbol":"100090","name":"SK오션플랜트","trigger_type":"Stage2-FalsePositive-Candidate","trigger_family":"offshore_wind_fabrication_orderbook_relief_slow_fade","trigger_date":"2024-06-04","entry_date":"2024-06-05","entry_price":15020.0,"entry_price_type":"next_tradable_open_after_offshore_wind_relief_spike","price_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","mfe_30d_pct":7.72,"mae_30d_pct":-11.19,"mfe_90d_pct":7.72,"mae_90d_pct":-31.42,"mfe_180d_pct":7.86,"mae_180d_pct":-31.42,"peak_price_180d":16200.0,"peak_date_180d":"2024-09-24","trough_price_180d":10300.0,"trough_date_180d":"2024-08-05","calibration_usable":true,"case_polarity":"counterexample_slow_fade_high_mae","evidence_url_pending":true,"source_proxy_only":true,"non_price_evidence_strength":"low_pending_url_repair","price_only_blowoff":false,"expected_stage_current_profile":"blocked_Stage2_or_4B_high_MAE_watch_until_order_margin_bridge_repaired","residual_error_type":"offshore_wind_fabrication_relief_spike_low_mfe_high_mae_without_margin_bridge"}
```

---

## 8. Score simulation and raw component breakdown

This is shadow-only and does not change production scoring.

| symbol | order/backlog visibility | delivery schedule | customer quality | margin bridge | market mispricing | execution / cost risk control | information confidence | shadow total | intended route |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| `082740` | 13 | 10 | 11 | 9 | 12 | 7 | 6 | 68 | Stage2-Guarded / Yellow after engine backlog and margin evidence repair |
| `071970` | 12 | 10 | 10 | 8 | 13 | 6 | 6 | 65 | Stage2-Guarded / Yellow after order and margin bridge repair |
| `017960` | 10 | 9 | 9 | 8 | 8 | 7 | 6 | 57 | Stage2-Guarded until LNG backlog/margin bridge repaired |
| `100090` | 6 | 5 | 5 | 2 | 5 | 2 | 4 | 29 | blocked Stage2 or 4B/high-MAE watch |

### Current calibrated profile stress test

The current calibrated profile already blocks pure price-only blowoff.  
The remaining C01 risk is **orderbook relevance without margin conversion**:

```text
C01 clean / guarded path:
  backlog or capital-goods cycle relevance
  + MFE persists beyond first event candle
  + MAE remains contained
  + URL-repaired delivery / customer / margin bridge
  => Stage2-Actionable-Guarded, then Yellow after evidence repair

C01 delayed rerating path:
  30D MFE is weak
  + 90D/180D MFE becomes strong
  + MAE remains contained
  => do not overblock; allow Stage2-Guarded while requiring evidence repair

C01 false-positive path:
  orderbook or project theme appears
  + MFE_30D < +10%
  + MAE_90D <= -30%
  + margin bridge is source-proxy-only
  => block Stage2 or route to local 4B/high-MAE watch
```

`082740`, `071970`, and `017960` prevent overblocking.  
`100090` shows why orderbook labels must not be promoted without project economics and margin conversion.

---

## 9. Aggregate metrics

```json
{
  "row_type": "aggregate",
  "research_id": "R1L74_C01_SHIP_ENGINE_LNG_BACKLOG_ROUTER",
  "round": "R1",
  "loop": 74,
  "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID",
  "canonical_archetype_id": "C01_ORDER_BACKLOG_MARGIN_BRIDGE",
  "fine_archetype_id": "SHIP_ENGINE_LNG_EQUIPMENT_BACKLOG_MARGIN_BRIDGE_AND_OFFSHORE_WIND_SLOW_FADE_ROUTER",
  "case_count": 4,
  "calibration_usable_case_count": 4,
  "positive_guarded_case_count": 3,
  "counterexample_count": 1,
  "new_symbol_count": 4,
  "source_proxy_only_count": 4,
  "evidence_url_pending_count": 4,
  "avg_mfe_30d_pct": 17.8,
  "avg_mae_30d_pct": -6.51,
  "avg_mfe_90d_pct": 27.29,
  "avg_mae_90d_pct": -14.28,
  "avg_mfe_180d_pct": 39.63,
  "avg_mae_180d_pct": -14.28,
  "max_mfe_180d_pct": 77.46,
  "worst_mae_180d_pct": -31.42
}
```

---

## 10. 4B proximity split

```json
{
  "row_type": "4b_split",
  "research_id": "R1L74_C01_SHIP_ENGINE_LNG_BACKLOG_ROUTER",
  "stage2_guarded_or_yellow_candidate": [
    {
      "symbol": "082740",
      "reason": "delayed but strong 90D/180D MFE with only -4.14% MAE; requires engine backlog/delivery/margin evidence repair"
    },
    {
      "symbol": "071970",
      "reason": "high MFE and acceptable forward MAE; requires order/customer/margin evidence repair before Green"
    },
    {
      "symbol": "017960",
      "reason": "moderate MFE with contained drawdown; requires LNG material backlog and cost-pass-through evidence"
    }
  ],
  "blocked_stage2_or_local_4b_watch": [
    {
      "symbol": "100090",
      "reason": "MFE was below +10% while 90D/180D MAE reached -31.42%; offshore-wind fabrication bridge was not proven"
    }
  ],
  "full_4b_or_green_requires_non_price_evidence": [
    "order backlog and customer quality",
    "delivery schedule / revenue conversion",
    "cost pass-through and margin bridge",
    "project economics and execution risk control",
    "cash-flow conversion"
  ]
}
```

---

## 11. Shadow rule candidate

```yaml
row_type: canonical_archetype_rule_candidate
canonical_archetype_id: C01_ORDER_BACKLOG_MARGIN_BRIDGE
fine_archetype_id: SHIP_ENGINE_LNG_EQUIPMENT_BACKLOG_MARGIN_BRIDGE_AND_OFFSHORE_WIND_SLOW_FADE_ROUTER
rule_name: C01_backlog_margin_bridge_delayed_positive_and_slow_fade_router
production_scoring_changed: false
shadow_weight_only: true
```

### Proposed routing logic

```text
For C01 order backlog / margin bridge cases:

Tier A: verified backlog-margin bridge
  Conditions:
    - order backlog, customer, delivery schedule, and margin evidence are URL-repaired
    - 30D/90D MAE remains contained
    - MFE persists beyond the first event candle
  Routing:
    - Stage2-Actionable or Stage2-Guarded allowed
    - Stage3-Yellow allowed after evidence repair
    - Green only after delivery and margin conversion are verified

Tier B: delayed rerating with contained MAE
  Conditions:
    - MFE_30D is weak or moderate
    - MFE_90D or MFE_180D becomes strong
    - MAE_90D remains better than -15%
    - evidence remains URL-pending
  Routing:
    - Stage2-Guarded allowed
    - no Green until evidence repair

Tier C: weak-MFE slow fade
  Conditions:
    - MFE_30D < +10%
    - MAE_90D <= -30%
    - margin / project-economics bridge is missing
  Routing:
    - block Stage2
    - local 4B/high-MAE watch
    - count as counterexample
```

### Suggested shadow delta

```json
{
  "row_type": "shadow_weight",
  "axis": "c01_backlog_margin_bridge_delayed_positive_and_slow_fade_router",
  "scope": "canonical_archetype_id:C01_ORDER_BACKLOG_MARGIN_BRIDGE",
  "proposal": {
    "source_proxy_only_green_allowed": false,
    "order_backlog_delivery_margin_bridge_required_for_green": true,
    "delayed_rerating_stage2_guarded_allowed": true,
    "delayed_rerating_mae90_min_pct": -15.0,
    "weak_mfe_threshold_30d_pct": 10.0,
    "slow_fade_high_mae_threshold_90d_pct": -30.0,
    "positive_weight_blocked_until_url_repair": true
  },
  "confidence": "medium_low_until_url_repair",
  "apply_now": false,
  "reason": "Three ship-engine/LNG equipment paths show valid C01 guarded positives, while one offshore-wind fabrication path shows a weak-MFE/high-MAE slow fade. C01 should preserve delayed low-MAE positives but require URL-repaired delivery and margin evidence before Green."
}
```

---

## 12. Residual contribution summary

```json
{
  "row_type": "residual_contribution",
  "research_id": "R1L74_C01_SHIP_ENGINE_LNG_BACKLOG_ROUTER",
  "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID",
  "canonical_archetype_id": "C01_ORDER_BACKLOG_MARGIN_BRIDGE",
  "contribution": "Adds four new C01 capital-goods/order-backlog cases in ship engines, LNG materials, and offshore fabrication. The run separates delayed low-MAE backlog rerating from a weak-MFE/high-MAE offshore-wind fabrication slow fade. C01 Green should require URL-repaired order backlog, delivery schedule, customer quality, cost pass-through, and margin conversion evidence.",
  "positive_guarded_case_added": 3,
  "counterexample_case_added": 1,
  "new_symbol_count": 4,
  "data_quality_blocker": "All four non-price order/backlog/margin triggers require URL-level repair before positive weight promotion.",
  "guardrail_added": "C01 weak-MFE entries with MFE_30D < +10% and MAE_90D <= -30% should block Stage2 or route to local 4B/high-MAE watch; delayed low-MAE reratings may remain Stage2-Guarded until evidence repair."
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
    082740: false
    071970: false
    017960: false
    100090: false
  evidence_url_pending:
    082740: true
    071970: true
    017960: true
    100090: true
  source_proxy_only:
    082740: true
    071970: true
    017960: true
    100090: true
```

Limitations:

```text
- Price path is validated against Stock-Web tradable OHLC rows.
- Non-price evidence is not URL-repaired in this run.
- Therefore this artifact is useful for C01 order-backlog/margin-bridge residual shape and slow-fade guardrail design, but should not promote positive weights until filings, IR, contract disclosures, customer/project data, or reports verify backlog, delivery, customer quality, cost pass-through, project economics, and margin conversion.
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
2. Preserve R1 / loop 74 metadata.
3. Add the cases to C01_ORDER_BACKLOG_MARGIN_BRIDGE only if parser validation passes.
4. Treat all four non-price triggers as evidence_url_pending=true and source_proxy_only=true until URL-level evidence is repaired.
5. Do not use these rows for positive weight promotion until filings/IR/contract-disclosure/customer-project/report data verifies order backlog, delivery schedule, customer quality, cost pass-through, project economics, and margin conversion.
6. Add a shadow-only rule candidate named C01_backlog_margin_bridge_delayed_positive_and_slow_fade_router.
7. Do not loosen Stage3-Green.
8. Add C01-specific guards:
   - source_proxy_only -> no Green
   - delayed low-MAE rerating may stay Stage2-Guarded until evidence repair
   - Green requires repaired order/delivery/customer/margin bridge
   - MFE_30D < +10% and MAE_90D <= -30% without margin bridge -> block Stage2 or local 4B/high-MAE watch
9. Keep production scoring unchanged unless later batch promotion logic independently marks this axis safe.
```

---

## 15. Next round state

```text
completed_round = R1
completed_loop = 74
next_round = R2
next_loop = 74
next_large_sector_hint = L2_AI_SEMICONDUCTOR_ELECTRONICS
```
