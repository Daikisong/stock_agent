# E2R Stock-Web v12 Residual Research — R1 Loop 75

```yaml
research_session: post_calibrated_sector_archetype_residual_research
mode: historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12
completed_round: R1
completed_loop: 75
next_round: R2
next_loop: 75
large_sector_id: L1_INDUSTRIALS_INFRA_DEFENSE_GRID
canonical_archetype_id: C02_POWER_GRID_DATACENTER_CAPEX
fine_archetype_id: SMALL_MID_TRANSFORMER_CABLE_SWITCHGEAR_GRID_DATACENTER_CAPEX_AND_THEME_SPIKE_ROUTER
output_file: e2r_stock_web_v12_residual_round_R1_loop_75_L1_INDUSTRIALS_INFRA_DEFENSE_GRID_C02_POWER_GRID_DATACENTER_CAPEX_research.md
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
completed_loop  = 74
large_sector_id = L10_POLICY_EVENT_CROSS_REDTEAM_MISC
canonical_archetype_id = R13_CROSS_ARCHETYPE_STAGE2_FALSE_POSITIVE_REVIEW
```

Therefore:

```text
scheduled_round = R1
scheduled_loop  = 75
```

R1 maps to:

```text
large_sector_id = L1_INDUSTRIALS_INFRA_DEFENSE_GRID
```

This run selects:

```text
canonical_archetype_id = C02_POWER_GRID_DATACENTER_CAPEX
fine_archetype_id = SMALL_MID_TRANSFORMER_CABLE_SWITCHGEAR_GRID_DATACENTER_CAPEX_AND_THEME_SPIKE_ROUTER
```

This is a valid R1/L1 pairing.

---

## 1. Why this R1/C02 run

The no-repeat ledger shows C02 is already well represented, but concentrated in the best-known transformer and grid-capex leaders:

```text
C02_POWER_GRID_DATACENTER_CAPEX:
  rows: 49
  symbols: 8
  date_range: 2023-01-27~2024-07-24
  good/bad S2: 24/1
  4B/4C: 15/0
  URL/proxy: 4/4
  top covered symbols: 010120(16), 267260(12), 298040(7), 006340(4), 103590(4), UNKNOWN_SYMBOL(3)
```

This file avoids those top-covered names and expands the C02 sample into smaller transformer / cable / switchgear names:

```text
033100 제룡전기
000500 가온전선
189860 서전기전
```

Research question:

```text
Can C02 separate real small/mid transformer and power-cable grid CAPEX winners from switchgear/grid theme spikes where the entry candle has already spent the upside and the order/margin bridge is missing?
```

C02 should work like a substation breaker. It must let through the names where grid/datacenter CAPEX becomes order backlog, customer quality, capacity utilization, and margin conversion. It must trip when the current is only a theme surge: a price spike without the load-bearing order bridge.

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
| `033100` | 제룡전기 | active_like / KOSDAQ | no 2024 overlap; latest listed candidate 2014-11-06 | true |
| `000500` | 가온전선 | active_like / KOSPI | 2024-11-11 and 2025-02-20 candidates are after the selected entry~D+180 window | true for 30D/90D/180D |
| `189860` | 서전기전 | active_like / KOSDAQ | no 2024 overlap; latest listed candidate 2018-11-16 | true |

Profile caveat:

```text
Stock-Web OHLC is raw/unadjusted marcap data.
These cases are calibration-safe for the selected 30D/90D/180D windows because no listed corporate-action candidate overlaps each entry~D+180 test window.
For 000500, 1Y/2Y would be contaminated_or_unavailable because later 2024-11-11 and 2025-02-20 candidates exist, but the 180D window used here remains usable.
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
The Stock-Web price path is fully validated, but company-level transformer/cable/switchgear order backlog, customer quality, export or datacenter demand bridge, capacity utilization, copper/pass-through, and gross-margin evidence still require later URL repair through filings, IR decks, contract disclosures, export data, or sell-side reports before production weight promotion.
```

C02 interpretation used here:

```text
C02 is not simply “grid stock rose.”
It asks whether grid/datacenter CAPEX converts into:
- order backlog,
- named or high-confidence customer demand,
- delivery schedule,
- capacity utilization,
- pass-through / input cost control,
- gross and operating margin conversion,
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
033100 + C02_POWER_GRID_DATACENTER_CAPEX -> no direct match found
000500 + C02_POWER_GRID_DATACENTER_CAPEX -> no direct match found
189860 + C02_POWER_GRID_DATACENTER_CAPEX -> no direct match found
```

Novelty accounting:

```json
{
  "new_symbol_count": 3,
  "minimum_new_symbol_count": 2,
  "positive_case_count": 2,
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
| `R1L75_C02_033100_20240305` | `033100` 제룡전기 | small/mid transformer grid/datacenter CAPEX order-margin rerating | positive anchor |
| `R1L75_C02_000500_20240306` | `000500` 가온전선 | power-cable grid/datacenter CAPEX low-MAE rerating | positive-guarded |
| `R1L75_C02_189860_20240529` | `189860` 서전기전 | switchgear/grid theme spike without order bridge | counterexample / 4B-4C high-MAE |

The intended residual:

```text
C02 should separate:
1. transformer and cable names where MFE expands and MAE remains contained;
2. delayed but durable grid-capex rerating where order/capacity evidence can later be repaired;
3. low-liquidity switchgear/grid theme spikes where the peak occurs at entry and high MAE follows quickly.
```

---

## 6. Stock-Web OHLC and backtest

### 6.1 `033100` 제룡전기 — small/mid transformer grid/datacenter CAPEX positive anchor

Trigger:

```text
trigger_date = 2024-03-04
trigger_type = Stage2-Actionable
trigger_family = small_mid_transformer_grid_datacenter_capex_order_margin_rerating
entry_date = 2024-03-05
entry_price = 27200.0
entry_price_type = next_tradable_open_after_transformer_capex_order_burst
```

Relevant Stock-Web rows:

```csv
d,o,h,l,c,v,a,mc,s,m
2024-03-04,21750.0,27200.0,21750.0,27200.0,5746788.0,149308673550.0,436897524800.0,16062409,KOSDAQ
2024-03-05,27200.0,27900.0,25700.0,27300.0,2574584.0,69485465450.0,438503765700.0,16062409,KOSDAQ
2024-03-08,30300.0,33850.0,30050.0,32550.0,3911304.0,125532485250.0,522831412950.0,16062409,KOSDAQ
2024-04-04,48550.0,55500.0,48400.0,53000.0,3370262.0,178441960050.0,851307677000.0,16062409,KOSDAQ
2024-05-13,75800.0,80700.0,68300.0,71500.0,3196414.0,236886628500.0,1148462243500.0,16062409,KOSDAQ
2024-06-21,72400.0,89400.0,71700.0,84500.0,5208004.0,423812403700.0,1357273560500.0,16062409,KOSDAQ
2024-07-11,98000.0,100700.0,94300.0,95900.0,810617.0,79154020100.0,1540385023100.0,16062409,KOSDAQ
2024-08-05,65700.0,68300.0,57700.0,62400.0,932399.0,59653534700.0,1002294321600.0,16062409,KOSDAQ
```

Backtest:

| window | peak/high | peak date | trough/low | trough date | MFE | MAE |
|---|---:|---|---:|---|---:|---:|
| 30 calendar days | 55500 | 2024-04-04 | 25700 | 2024-03-05 | +104.04% | -5.51% |
| 90 calendar days | 80700 | 2024-05-13 | 25700 | 2024-03-05 | +196.69% | -5.51% |
| 180 calendar days | 100700 | 2024-07-11 | 25700 | 2024-03-05 | +270.22% | -5.51% |

Interpretation:

```text
033100 is the clean C02 positive anchor.
The price path had very large MFE and only shallow early MAE, matching a real grid/datacenter transformer CAPEX rerating.
It can support Stage2-Actionable / Yellow after evidence repair, but Green still requires URL-repaired order backlog, customer quality, delivery, capacity, and margin evidence.
```

### 6.2 `000500` 가온전선 — power-cable grid/datacenter CAPEX low-MAE rerating

Trigger:

```text
trigger_date = 2024-03-05
trigger_type = Stage2-Actionable-Guarded
trigger_family = power_cable_grid_datacenter_capex_low_mae_rerating
entry_date = 2024-03-06
entry_price = 27000.0
entry_price_type = next_tradable_open_after_power_cable_grid_capex_burst
```

Relevant Stock-Web rows:

```csv
d,o,h,l,c,v,a,mc,s,m
2024-03-05,25200.0,29450.0,25100.0,27400.0,1471689.0,40901072100.0,201607720400.0,7357946,KOSPI
2024-03-06,27000.0,27600.0,26150.0,27150.0,409162.0,11033369250.0,199768233900.0,7357946,KOSPI
2024-04-05,31350.0,36650.0,30700.0,31800.0,4505449.0,152381531450.0,233982682800.0,7357946,KOSPI
2024-04-29,47100.0,54000.0,45600.0,49400.0,3555386.0,179668212950.0,363482532400.0,7357946,KOSPI
2024-05-13,66800.0,74500.0,64000.0,66300.0,3556501.0,246508101800.0,487831819800.0,7357946,KOSPI
2024-06-04,52200.0,52300.0,49000.0,49500.0,345023.0,17295227600.0,364218327000.0,7357946,KOSPI
2024-08-05,39500.0,39750.0,30900.0,32400.0,288299.0,10279731600.0,238397450400.0,7357946,KOSPI
2024-09-02,35400.0,35400.0,34600.0,35000.0,52523.0,1913136750.0,257528110000.0,7357946,KOSPI
```

Backtest:

| window | peak/high | peak date | trough/low | trough date | MFE | MAE |
|---|---:|---|---:|---|---:|---:|
| 30 calendar days | 36650 | 2024-04-05 | 26150 | 2024-03-06 | +35.74% | -3.15% |
| 90 calendar days | 74500 | 2024-05-13 | 26150 | 2024-03-06 | +175.93% | -3.15% |
| 180 calendar days | 74500 | 2024-05-13 | 26150 | 2024-03-06 | +175.93% | -3.15% |

Interpretation:

```text
000500 is the C02 power-cable positive-guarded case.
The forward path delivered large MFE with very contained MAE from the selected entry.
This should remain Stage2-Guarded / Yellow only after URL-repaired cable order, capacity, copper pass-through, and margin bridge evidence.
```

### 6.3 `189860` 서전기전 — switchgear/grid theme spike without order bridge

Trigger:

```text
trigger_date = 2024-05-28
trigger_type = Stage2-FalsePositive-Candidate
trigger_family = switchgear_grid_theme_spike_without_order_margin_bridge
entry_date = 2024-05-29
entry_price = 8440.0
entry_price_type = next_tradable_open_after_switchgear_grid_theme_spike
```

Relevant Stock-Web rows:

```csv
d,o,h,l,c,v,a,mc,s,m
2024-05-28,6000.0,7730.0,5890.0,7730.0,4518862.0,31274314530.0,74971569400.0,9698780,KOSDAQ
2024-05-29,8440.0,8450.0,7020.0,7020.0,4099236.0,31858595710.0,68085435600.0,9698780,KOSDAQ
2024-06-04,6560.0,6570.0,6190.0,6300.0,421143.0,2654555600.0,61102314000.0,9698780,KOSDAQ
2024-06-24,5800.0,5800.0,5550.0,5610.0,87048.0,492315720.0,54410155800.0,9698780,KOSDAQ
2024-08-05,5350.0,5350.0,4510.0,4805.0,175594.0,870204975.0,46602637900.0,9698780,KOSDAQ
2024-10-11,4110.0,4145.0,4005.0,4080.0,32619.0,132744140.0,39571022400.0,9698780,KOSDAQ
2024-11-25,4860.0,4860.0,4695.0,4770.0,37056.0,175790985.0,46263180600.0,9698780,KOSDAQ
```

Backtest:

| window | peak/high | peak date | trough/low | trough date | MFE | MAE |
|---|---:|---|---:|---|---:|---:|
| 30 calendar days | 8450 | 2024-05-29 | 5550 | 2024-06-24 | +0.12% | -34.24% |
| 90 calendar days | 8450 | 2024-05-29 | 4510 | 2024-08-05 | +0.12% | -46.56% |
| 180 calendar days | 8450 | 2024-05-29 | 4005 | 2024-10-11 | +0.12% | -52.55% |

Interpretation:

```text
189860 is the hard C02 counterexample.
The switchgear/grid theme candle had already spent the upside by entry. The next windows show almost no MFE and severe MAE.
This should block Stage2/Green and route to 4B/4C high-MAE watch unless real order backlog and margin bridge evidence existed before entry.
```

---

## 7. Machine-readable trigger JSONL

```jsonl
{"row_type":"trigger","research_id":"R1L75_C02_GRID_TRANSFORMER_CABLE_ROUTER","round":"R1","loop":75,"large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C02_POWER_GRID_DATACENTER_CAPEX","fine_archetype_id":"SMALL_MID_TRANSFORMER_CABLE_SWITCHGEAR_GRID_DATACENTER_CAPEX_AND_THEME_SPIKE_ROUTER","symbol":"033100","name":"제룡전기","trigger_type":"Stage2-Actionable","trigger_family":"small_mid_transformer_grid_datacenter_capex_order_margin_rerating","trigger_date":"2024-03-04","entry_date":"2024-03-05","entry_price":27200.0,"entry_price_type":"next_tradable_open_after_transformer_capex_order_burst","price_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","mfe_30d_pct":104.04,"mae_30d_pct":-5.51,"mfe_90d_pct":196.69,"mae_90d_pct":-5.51,"mfe_180d_pct":270.22,"mae_180d_pct":-5.51,"peak_price_180d":100700.0,"peak_date_180d":"2024-07-11","trough_price_180d":25700.0,"trough_date_180d":"2024-03-05","calibration_usable":true,"case_polarity":"positive_anchor_transformer_low_mae","evidence_url_pending":true,"source_proxy_only":true,"non_price_evidence_strength":"medium_pending_url_repair","price_only_blowoff":false,"expected_stage_current_profile":"Stage2-Actionable_to_Yellow_after_transformer_order_backlog_margin_bridge_repaired","residual_error_type":"positive_transformer_capex_path_requires_url_repaired_order_backlog_customer_margin_evidence_before_green"}
{"row_type":"trigger","research_id":"R1L75_C02_GRID_TRANSFORMER_CABLE_ROUTER","round":"R1","loop":75,"large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C02_POWER_GRID_DATACENTER_CAPEX","fine_archetype_id":"SMALL_MID_TRANSFORMER_CABLE_SWITCHGEAR_GRID_DATACENTER_CAPEX_AND_THEME_SPIKE_ROUTER","symbol":"000500","name":"가온전선","trigger_type":"Stage2-Actionable-Guarded","trigger_family":"power_cable_grid_datacenter_capex_low_mae_rerating","trigger_date":"2024-03-05","entry_date":"2024-03-06","entry_price":27000.0,"entry_price_type":"next_tradable_open_after_power_cable_grid_capex_burst","price_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","mfe_30d_pct":35.74,"mae_30d_pct":-3.15,"mfe_90d_pct":175.93,"mae_90d_pct":-3.15,"mfe_180d_pct":175.93,"mae_180d_pct":-3.15,"peak_price_180d":74500.0,"peak_date_180d":"2024-05-13","trough_price_180d":26150.0,"trough_date_180d":"2024-03-06","calibration_usable":true,"case_polarity":"positive_guarded_power_cable_low_mae","evidence_url_pending":true,"source_proxy_only":true,"non_price_evidence_strength":"medium_pending_url_repair","price_only_blowoff":false,"expected_stage_current_profile":"Stage2-Guarded_to_Yellow_if_power_cable_order_capacity_margin_bridge_repaired","residual_error_type":"positive_cable_capex_path_requires_url_repaired_order_capacity_pass_through_margin_bridge_before_green"}
{"row_type":"trigger","research_id":"R1L75_C02_GRID_TRANSFORMER_CABLE_ROUTER","round":"R1","loop":75,"large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C02_POWER_GRID_DATACENTER_CAPEX","fine_archetype_id":"SMALL_MID_TRANSFORMER_CABLE_SWITCHGEAR_GRID_DATACENTER_CAPEX_AND_THEME_SPIKE_ROUTER","symbol":"189860","name":"서전기전","trigger_type":"Stage2-FalsePositive-Candidate","trigger_family":"switchgear_grid_theme_spike_without_order_margin_bridge","trigger_date":"2024-05-28","entry_date":"2024-05-29","entry_price":8440.0,"entry_price_type":"next_tradable_open_after_switchgear_grid_theme_spike","price_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","mfe_30d_pct":0.12,"mae_30d_pct":-34.24,"mfe_90d_pct":0.12,"mae_90d_pct":-46.56,"mfe_180d_pct":0.12,"mae_180d_pct":-52.55,"peak_price_180d":8450.0,"peak_date_180d":"2024-05-29","trough_price_180d":4005.0,"trough_date_180d":"2024-10-11","calibration_usable":true,"case_polarity":"counterexample_theme_spike_extreme_mae","evidence_url_pending":true,"source_proxy_only":true,"non_price_evidence_strength":"low_pending_url_repair","price_only_blowoff":true,"expected_stage_current_profile":"blocked_Stage2_or_4B_4C_high_MAE_watch","residual_error_type":"switchgear_grid_theme_entry_spent_upside_on_entry_day_and_failed_without_order_backlog_margin_bridge"}
```

---

## 8. Score simulation and raw component breakdown

This is shadow-only and does not change production scoring.

| symbol | grid/datacenter CAPEX relevance | order backlog / customer bridge | capacity / delivery bridge | input pass-through | market mispricing | margin conversion | information confidence | shadow total | intended route |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| `033100` | 15 | 13 | 12 | 9 | 16 | 12 | 6 | 83 | Stage2/Yellow after transformer order and margin evidence repair |
| `000500` | 13 | 11 | 10 | 10 | 14 | 10 | 6 | 74 | Stage2-Guarded / Yellow after cable order/capacity/pass-through evidence repair |
| `189860` | 8 | 2 | 3 | 2 | 3 | 2 | 4 | 24 | blocked Stage2 / 4B-4C high-MAE watch |

### Current calibrated profile stress test

The current calibrated profile already blocks pure price-only blowoff.  
The remaining C02 issue is **small/mid grid equipment label without order-margin bridge**:

```text
C02 clean transformer/cable path:
  grid/datacenter CAPEX relevance
  + persistent MFE
  + contained MAE
  + URL-repaired order / delivery / capacity / margin evidence
  => Stage2-Actionable or Stage2-Guarded, then Yellow after evidence repair

C02 theme-spike failure:
  switchgear/grid label exists
  + peak occurs at entry
  + MFE_30D < +5%
  + MAE_30D <= -30%
  + no order/margin bridge
  => block Stage2 and route to 4B/4C high-MAE watch
```

`033100` and `000500` prevent overblocking.  
`189860` shows why C02 should not let every grid-adjacent small-cap theme candle through the same breaker.

---

## 9. Aggregate metrics

```json
{
  "row_type": "aggregate",
  "research_id": "R1L75_C02_GRID_TRANSFORMER_CABLE_ROUTER",
  "round": "R1",
  "loop": 75,
  "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID",
  "canonical_archetype_id": "C02_POWER_GRID_DATACENTER_CAPEX",
  "fine_archetype_id": "SMALL_MID_TRANSFORMER_CABLE_SWITCHGEAR_GRID_DATACENTER_CAPEX_AND_THEME_SPIKE_ROUTER",
  "case_count": 3,
  "calibration_usable_case_count": 3,
  "positive_case_count": 2,
  "counterexample_count": 1,
  "new_symbol_count": 3,
  "source_proxy_only_count": 3,
  "evidence_url_pending_count": 3,
  "avg_mfe_30d_pct": 46.63,
  "avg_mae_30d_pct": -14.3,
  "avg_mfe_90d_pct": 124.25,
  "avg_mae_90d_pct": -18.41,
  "avg_mfe_180d_pct": 148.76,
  "avg_mae_180d_pct": -20.4,
  "max_mfe_180d_pct": 270.22,
  "worst_mae_180d_pct": -52.55
}
```

---

## 10. 4B proximity split

```json
{
  "row_type": "4b_split",
  "research_id": "R1L75_C02_GRID_TRANSFORMER_CABLE_ROUTER",
  "stage2_positive_or_yellow_candidate": [
    {
      "symbol": "033100",
      "reason": "transformer/grid CAPEX path had +270.22% 180D MFE with only -5.51% MAE"
    },
    {
      "symbol": "000500",
      "reason": "power-cable CAPEX path had +175.93% 180D MFE with only -3.15% MAE"
    }
  ],
  "blocked_stage2_or_4c_watch": [
    {
      "symbol": "189860",
      "reason": "entry-day peak with +0.12% MFE and -52.55% 180D MAE"
    }
  ],
  "full_4b_or_green_requires_non_price_evidence": [
    "transformer/cable/switchgear order backlog",
    "customer quality and delivery schedule",
    "datacenter or grid CAPEX pull-through",
    "capacity utilization",
    "input-cost pass-through",
    "gross margin / operating margin conversion"
  ]
}
```

---

## 11. Shadow rule candidate

```yaml
row_type: canonical_archetype_rule_candidate
canonical_archetype_id: C02_POWER_GRID_DATACENTER_CAPEX
fine_archetype_id: SMALL_MID_TRANSFORMER_CABLE_SWITCHGEAR_GRID_DATACENTER_CAPEX_AND_THEME_SPIKE_ROUTER
rule_name: C02_small_mid_grid_capex_order_bridge_vs_theme_spike_router
production_scoring_changed: false
shadow_weight_only: true
existing_axis_tested: price_only_blowoff_blocks_positive_stage
existing_axis_strengthened: true
```

### Proposed routing logic

```text
For C02 small/mid transformer, cable, and switchgear cases:

Tier A: verified transformer/cable CAPEX winner
  Conditions:
    - grid/datacenter CAPEX relevance is clear
    - order backlog, customer, delivery, and margin evidence are URL-repaired
    - MAE_30D remains better than -10%
    - MFE persists beyond the first event candle
  Routing:
    - Stage2-Actionable or Stage2-Guarded allowed
    - Stage3-Yellow allowed after evidence repair
    - Green only after order/capacity/margin bridge is verified

Tier B: source-proxy-only strong price path
  Conditions:
    - MFE_90D >= +50%
    - MAE_90D > -15%
    - evidence_url_pending or source_proxy_only remains true
  Routing:
    - Stage2-Guarded / Yellow watch
    - no Green until URL repair

Tier C: grid theme spike already spent
  Conditions:
    - MFE_30D < +5%
    - MAE_30D <= -30%
    - peak occurs on entry day or within first 5 trading days
    - no order/margin bridge
  Routing:
    - block Stage2
    - local 4B / 4C high-MAE watch
    - count as counterexample
```

### Suggested shadow delta

```json
{
  "row_type": "shadow_weight",
  "axis": "c02_small_mid_grid_capex_order_bridge_vs_theme_spike_router",
  "scope": "canonical_archetype_id:C02_POWER_GRID_DATACENTER_CAPEX",
  "proposal": {
    "source_proxy_only_green_allowed": false,
    "order_backlog_customer_capacity_margin_bridge_required_for_green": true,
    "strong_mfe90_threshold_pct": 50.0,
    "strong_path_mae90_min_pct": -15.0,
    "theme_spike_mfe30_threshold_pct": 5.0,
    "theme_spike_mae30_threshold_pct": -30.0,
    "entry_day_or_first5_peak_blocks_stage2_without_bridge": true,
    "positive_weight_blocked_until_url_repair": true
  },
  "confidence": "medium_low_until_url_repair",
  "apply_now": false,
  "reason": "Two non-top-covered transformer/cable winners and one switchgear theme-spike failure show that C02 should preserve low-MAE grid CAPEX winners while blocking small-cap grid theme spikes without order and margin bridge evidence."
}
```

---

## 12. Residual contribution summary

```json
{
  "row_type": "residual_contribution",
  "research_id": "R1L75_C02_GRID_TRANSFORMER_CABLE_ROUTER",
  "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID",
  "canonical_archetype_id": "C02_POWER_GRID_DATACENTER_CAPEX",
  "contribution": "Adds three non-top-covered C02 grid/datacenter CAPEX cases and separates low-MAE transformer/cable rerating from a hard switchgear/grid theme-spike false positive. C02 Green should require URL-repaired order backlog, customer quality, delivery schedule, capacity utilization, pass-through, and margin evidence.",
  "positive_case_added": 2,
  "counterexample_case_added": 1,
  "new_symbol_count": 3,
  "new_independent_case_count": 3,
  "reused_case_count": 0,
  "same_archetype_new_symbol_count": 3,
  "same_archetype_new_trigger_family_count": 3,
  "new_trigger_family_count": 3,
  "current_profile_error_count": 1,
  "diversity_score_summary": {
    "new_symbol_bonus": 9,
    "counterexample_gap_bonus": 4,
    "residual_error_bonus": 5,
    "wrong_round_penalty": 0,
    "repeated_same_symbol_penalty": 0,
    "net_interpretive_score": 18
  },
  "loop_contribution_label": "sector_specific_rule_candidate",
  "do_not_propose_new_weight_delta": false,
  "data_quality_blocker": "All three non-price grid/datacenter CAPEX triggers require URL-level repair before positive weight promotion.",
  "guardrail_added": "C02 source_proxy_only small-cap grid theme spikes with MFE_30D < +5% and MAE_30D <= -30% should block Stage2 or route to 4B/4C watch; strong transformer/cable paths can remain Stage2-Guarded until order/margin evidence is repaired."
}
```

One-line contribution:

```text
This loop adds 3 new independent cases, 1 counterexamples, and 1 residual errors for R1/L1_INDUSTRIALS_INFRA_DEFENSE_GRID/C02_POWER_GRID_DATACENTER_CAPEX.
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
    033100: false
    000500: false
    189860: false
  evidence_url_pending:
    033100: true
    000500: true
    189860: true
  source_proxy_only:
    033100: true
    000500: true
    189860: true
  special_handling:
    000500:
      note: "2024-11-11 and 2025-02-20 corporate-action candidates occur after the selected 2024-03-06 entry plus 180 calendar days. 30D/90D/180D are usable; 1Y/2Y would be contaminated_or_unavailable."
```

Limitations:

```text
- Price path is validated against Stock-Web tradable OHLC rows.
- Non-price evidence is not URL-repaired in this run.
- Therefore this artifact is useful for C02 small/mid grid/datacenter CAPEX residual shape and theme-spike guardrail design, but should not promote positive weights until filings, IR, contract disclosures, export data, or reports verify order backlog, customer quality, delivery, capacity, pass-through, and margin conversion.
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
2. Preserve R1 / loop 75 metadata.
3. Add the cases to C02_POWER_GRID_DATACENTER_CAPEX only if parser validation passes.
4. Treat all three non-price triggers as evidence_url_pending=true and source_proxy_only=true until URL-level evidence is repaired.
5. Do not use these rows for positive weight promotion until filings/IR/contract-disclosure/export-data/report data verifies transformer/cable/switchgear order backlog, customer quality, delivery schedule, capacity utilization, input pass-through, and margin conversion.
6. Add a shadow-only rule candidate named C02_small_mid_grid_capex_order_bridge_vs_theme_spike_router.
7. Do not loosen Stage3-Green.
8. Add C02-specific guards:
   - source_proxy_only -> no Green
   - Green requires repaired order backlog / customer / capacity / margin bridge
   - MFE_90D >= +50% and MAE_90D > -15% may remain Stage2-Guarded / Yellow watch until evidence repair
   - MFE_30D < +5% and MAE_30D <= -30% with entry-day or first-5-day peak -> block Stage2 / 4B-4C watch
9. Keep production scoring unchanged unless later batch promotion logic independently marks this axis safe.
```

---

## 15. Next round state

```text
completed_round = R1
completed_loop = 75
next_round = R2
next_loop = 75
next_large_sector_hint = L2_AI_SEMICONDUCTOR_ELECTRONICS
round_schedule_status = valid
round_sector_consistency = pass
```
