# E2R Stock-Web v12 Residual Research — R4 Loop 77

```yaml
research_session: post_calibrated_sector_archetype_residual_research
mode: historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12
completed_round: R4
completed_loop: 77
next_round: R5
next_loop: 77
large_sector_id: L4_MATERIALS_SPREAD_RESOURCE
canonical_archetype_id: C16_STRATEGIC_RESOURCE_POLICY_SUPPLY
fine_archetype_id: EAST_SEA_GAS_OIL_RESOURCE_POLICY_SUPPLY_RIGHTS_AND_THEME_SPIKE_HIGH_MAE_ROUTER
output_file: e2r_stock_web_v12_residual_round_R4_loop_77_L4_MATERIALS_SPREAD_RESOURCE_C16_STRATEGIC_RESOURCE_POLICY_SUPPLY_research.md
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
completed_round = R3
completed_loop  = 77
large_sector_id = L3_BATTERY_EV_GREEN_MOBILITY
canonical_archetype_id = C13_BATTERY_JV_UTILIZATION_AMPC_IRA
```

Therefore:

```text
scheduled_round = R4
scheduled_loop  = 77
```

R4 maps to:

```text
large_sector_id = L4_MATERIALS_SPREAD_RESOURCE
```

This run selects:

```text
canonical_archetype_id = C16_STRATEGIC_RESOURCE_POLICY_SUPPLY
fine_archetype_id = EAST_SEA_GAS_OIL_RESOURCE_POLICY_SUPPLY_RIGHTS_AND_THEME_SPIKE_HIGH_MAE_ROUTER
```

This is a valid R4/L4 pairing.

---

## 1. Why this R4/C16 run

The no-repeat ledger shows C16 is moderately covered but concentrated in a small set of strategic-resource names:

```text
C16_STRATEGIC_RESOURCE_POLICY_SUPPLY:
  rows: 67
  symbols: 23
  date_range: 2019-05-20~2024-10-10
  good/bad S2: 17/7
  4B/4C: 19/0
  URL/proxy: 13/13
  top covered symbols: 001570(8), 005490(8), 000910(7), 075970(5), 005290(4), 081150(4)
```

This file avoids those top-covered symbols and adds four East Sea gas / petroleum / resource-policy supply cases:

```text
036460 한국가스공사
039610 화성밸브
024060 흥구석유
004090 한국석유
```

Research question:

```text
Can C16 separate state-backed resource-supply rerating from oil/gas/petroleum policy-theme spikes where the policy label is real but resource rights, procurement, order, volume, and margin bridges are not company-specific?
```

C16 is a resource-supply bridge. A government resource-policy announcement is the seismic pulse; Stage2 needs the drill bit, the concession, the capex plan, the procurement route, and the cash-flow map. Without those, the pulse becomes a theme wave that knocks late entries underwater.

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
| `036460` | 한국가스공사 | active_like / KOSPI | none listed | true |
| `039610` | 화성밸브 | active_like / KOSDAQ | no 2024 overlap; latest listed candidate 2019-02-18 | true |
| `024060` | 흥구석유 | active_like / KOSDAQ | no 2024 overlap; old 2008 candidates only | true |
| `004090` | 한국석유 | active_like / KOSPI | no 2024 overlap; latest listed candidates 2021 only | true |

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
The Stock-Web price path is fully validated, but company-level resource rights, exploration/development authority, state-backed execution, capex schedule, procurement route, pipe/valve order visibility, petroleum-volume linkage, tariff/spread/margin conversion, and cash-flow evidence still require later URL repair through filings, government policy documents, IR decks, procurement disclosures, or sell-side reports before production weight promotion.
```

C16 interpretation used here:

```text
C16 is not simply “resource policy stock rose.”
It asks whether a strategic-resource policy event becomes company economics:
- resource rights and execution authority,
- exploration / development / capex schedule,
- procurement and supply-chain route,
- order visibility for infrastructure suppliers,
- volume / tariff / spread linkage,
- gross margin and cash-flow conversion,
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
036460 + C16_STRATEGIC_RESOURCE_POLICY_SUPPLY -> no direct match found
024060 + C16_STRATEGIC_RESOURCE_POLICY_SUPPLY -> no direct match found
039610 + C16_STRATEGIC_RESOURCE_POLICY_SUPPLY -> no direct match found
004090 + C16_STRATEGIC_RESOURCE_POLICY_SUPPLY -> no direct match found
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
| `R4L77_C16_036460_20240604` | `036460` 한국가스공사 | East Sea gas resource policy / state-backed supply rights | positive-guarded anchor |
| `R4L77_C16_039610_20240604` | `039610` 화성밸브 | gas-valve infrastructure resource policy high-MFE/high-MAE | positive-guarded, high-MAE |
| `R4L77_C16_024060_20240604` | `024060` 흥구석유 | oil distributor resource-policy theme first-window MFE / later drawdown | counterexample |
| `R4L77_C16_004090_20240604` | `004090` 한국석유 | petroleum material resource-policy theme initial-MFE / high-MAE | counterexample |

The intended residual:

```text
C16 should separate:
1. state-backed resource-supply paths where MFE expands and MAE is not catastrophic;
2. infrastructure supplier paths where MFE can be large but early MAE requires an order/procurement bridge;
3. oil distributor / petroleum theme paths where MFE appears but high MAE blocks Yellow/Green;
4. resource-policy labels that lack company-specific rights, volume, tariff/spread, or margin evidence.
```

---

## 6. Stock-Web OHLC and backtest

### 6.1 `036460` 한국가스공사 — East Sea gas resource policy positive-guarded anchor

Trigger:

```text
trigger_date = 2024-06-03
trigger_type = Stage2-Actionable-Guarded
trigger_family = east_sea_gas_resource_policy_supply_rights_state_backed_low_mae_high_mfe
entry_date = 2024-06-04
entry_price = 40800.0
entry_price_type = next_tradable_open_after_east_sea_gas_resource_policy_burst
```

Relevant Stock-Web rows:

```csv
d,o,h,l,c,v,a,mc,s,m
2024-06-03,29800.0,38700.0,29700.0,38700.0,13412864.0,498113399650.0,3572513100000.0,92313000,KOSPI
2024-06-04,40800.0,49350.0,38750.0,39400.0,33946477.0,1494925644300.0,3637132200000.0,92313000,KOSPI
2024-06-05,39000.0,44650.0,37350.0,43700.0,23475149.0,968111636450.0,4034078100000.0,92313000,KOSPI
2024-06-20,59200.0,64500.0,56500.0,63500.0,12497795.0,748090305700.0,5861875500000.0,92313000,KOSPI
2024-08-05,40350.0,40950.0,36500.0,37950.0,2254302.0,87875721600.0,3503278350000.0,92313000,KOSPI
2024-09-20,47700.0,52300.0,46700.0,50800.0,4763427.0,239643215650.0,4689500400000.0,92313000,KOSPI
2024-11-25,47250.0,48150.0,46550.0,47650.0,1305560.0,61802235200.0,4398714450000.0,92313000,KOSPI
```

Backtest:

| window | peak/high | peak date | trough/low | trough date | MFE | MAE |
|---|---:|---|---:|---|---:|---:|
| 30 calendar days | 64500 | 2024-06-20 | 37350 | 2024-06-05 | +58.09% | -8.46% |
| 90 calendar days | 64500 | 2024-06-20 | 36500 | 2024-08-05 | +58.09% | -10.54% |
| 180 calendar days | 64500 | 2024-06-20 | 36500 | 2024-08-05 | +58.09% | -10.54% |

Interpretation:

```text
036460 is the C16 positive-guarded anchor.
The state-backed resource-policy path produced large MFE and did not become a deep high-MAE failure.
However, Green still requires URL-repaired evidence for resource rights, execution authority, capex schedule, tariff/spread linkage, and cash-flow conversion.
```

### 6.2 `039610` 화성밸브 — gas-valve infrastructure resource policy high-MFE/high-MAE branch

Trigger:

```text
trigger_date = 2024-06-03
trigger_type = Stage2-Actionable-Guarded
trigger_family = gas_valve_infrastructure_resource_policy_high_mfe_high_mae_guarded
entry_date = 2024-06-04
entry_price = 8630.0
entry_price_type = next_tradable_open_after_gas_valve_resource_infrastructure_policy_burst
```

Relevant Stock-Web rows:

```csv
d,o,h,l,c,v,a,mc,s,m
2024-06-03,5150.0,6640.0,5140.0,6640.0,3557446.0,22292106990.0,69125056000.0,10410400,KOSDAQ
2024-06-04,8630.0,8630.0,8310.0,8630.0,3942431.0,33930835030.0,89841752000.0,10410400,KOSDAQ
2024-06-05,8330.0,11080.0,7800.0,9870.0,50911410.0,487972385270.0,102750648000.0,10410400,KOSDAQ
2024-07-03,7020.0,7170.0,6800.0,7120.0,285052.0,1984515320.0,74122048000.0,10410400,KOSDAQ
2024-07-23,9550.0,12070.0,9350.0,10990.0,18551212.0,204863833830.0,114410296000.0,10410400,KOSDAQ
2024-08-20,12200.0,13470.0,11640.0,11790.0,13989254.0,179128302580.0,122738616000.0,10410400,KOSDAQ
2024-12-09,12560.0,12650.0,11950.0,12040.0,434668.0,5273057380.0,180600000000.0,15000000,KOSDAQ
```

Backtest:

| window | peak/high | peak date | trough/low | trough date | MFE | MAE |
|---|---:|---|---:|---|---:|---:|
| 30 calendar days | 11080 | 2024-06-05 | 6800 | 2024-07-03 | +28.39% | -21.21% |
| 90 calendar days | 13470 | 2024-08-20 | 6800 | 2024-07-03 | +56.08% | -21.21% |
| 180 calendar days | 13470 | 2024-08-20 | 6800 | 2024-07-03 | +56.08% | -21.21% |

Interpretation:

```text
039610 is a high-MFE but high-MAE C16 branch.
The path eventually produced large MFE, so it should not be blanket-blocked.
But because early MAE exceeded -20%, this should remain Stage2-Guarded only until gas valve procurement/order, project linkage, delivery, and margin evidence is URL-repaired.
```

### 6.3 `024060` 흥구석유 — oil distributor resource-policy theme first-window MFE / later drawdown

Trigger:

```text
trigger_date = 2024-06-03
trigger_type = Stage2-FalsePositive-Candidate
trigger_family = oil_distributor_resource_policy_theme_first_window_mfe_later_drawdown
entry_date = 2024-06-04
entry_price = 17520.0
entry_price_type = next_tradable_open_after_oil_resource_policy_theme_burst
```

Relevant Stock-Web rows:

```csv
d,o,h,l,c,v,a,mc,s,m
2024-06-03,12510.0,16250.0,12510.0,16250.0,15726169.0,241831929270.0,243750000000.0,15000000,KOSDAQ
2024-06-04,17520.0,20950.0,17510.0,19240.0,24948825.0,489654197180.0,288600000000.0,15000000,KOSDAQ
2024-06-18,14150.0,15930.0,14010.0,14360.0,6886969.0,104048824260.0,215400000000.0,15000000,KOSDAQ
2024-07-26,12680.0,12830.0,12360.0,12670.0,206087.0,2600717580.0,190050000000.0,15000000,KOSDAQ
2024-08-13,21650.0,21900.0,19940.0,20300.0,7288331.0,151025565150.0,304500000000.0,15000000,KOSDAQ
2024-10-04,20500.0,23000.0,19970.0,21800.0,20683974.0,443512936820.0,327000000000.0,15000000,KOSDAQ
2024-11-27,15030.0,15040.0,14060.0,14080.0,578902.0,8350484390.0,211200000000.0,15000000,KOSDAQ
```

Backtest:

| window | peak/high | peak date | trough/low | trough date | MFE | MAE |
|---|---:|---|---:|---|---:|---:|
| 30 calendar days | 20950 | 2024-06-04 | 14010 | 2024-06-18 | +19.58% | -20.03% |
| 90 calendar days | 21900 | 2024-08-13 | 12360 | 2024-07-26 | +25.00% | -29.45% |
| 180 calendar days | 23000 | 2024-10-04 | 12360 | 2024-07-26 | +31.28% | -29.45% |

Interpretation:

```text
024060 is a first-window-MFE / high-MAE C16 counterexample.
The oil/resource policy theme was tradable, but drawdown reached a local high-MAE band before any company-specific resource-supply economics were visible.
This should cap at Stage2-Guarded or route to local 4B watch until volume, tariff/spread, or margin evidence is repaired.
```

### 6.4 `004090` 한국석유 — petroleum material resource-policy theme initial-MFE / high-MAE path

Trigger:

```text
trigger_date = 2024-06-03
trigger_type = Stage2-FalsePositive-Candidate
trigger_family = petroleum_material_resource_policy_theme_initial_mfe_high_mae
entry_date = 2024-06-04
entry_price = 21650.0
entry_price_type = next_tradable_open_after_petroleum_resource_policy_theme_burst
```

Relevant Stock-Web rows:

```csv
d,o,h,l,c,v,a,mc,s,m
2024-06-03,13890.0,17950.0,13850.0,17950.0,7056561.0,122108449660.0,227859454000.0,12694120,KOSPI
2024-06-04,21650.0,23300.0,21500.0,23300.0,11398794.0,258647366250.0,295772996000.0,12694120,KOSPI
2024-06-05,23650.0,28100.0,21600.0,23300.0,18062960.0,435703215800.0,295772996000.0,12694120,KOSPI
2024-06-26,17710.0,17860.0,17040.0,17200.0,704359.0,12185880340.0,218338864000.0,12694120,KOSPI
2024-07-25,16140.0,16600.0,15540.0,15660.0,375320.0,6025508920.0,198789919200.0,12694120,KOSPI
2024-08-05,23900.0,24950.0,20150.0,22600.0,8496027.0,199712989400.0,286887112000.0,12694120,KOSPI
2024-11-29,14660.0,14680.0,14180.0,14260.0,101490.0,1454471770.0,181018151200.0,12694120,KOSPI
```

Backtest:

| window | peak/high | peak date | trough/low | trough date | MFE | MAE |
|---|---:|---|---:|---|---:|---:|
| 30 calendar days | 28100 | 2024-06-05 | 17040 | 2024-06-26 | +29.79% | -21.29% |
| 90 calendar days | 28100 | 2024-06-05 | 15540 | 2024-07-25 | +29.79% | -28.22% |
| 180 calendar days | 28100 | 2024-06-05 | 14180 | 2024-11-29 | +29.79% | -34.50% |

Interpretation:

```text
004090 is the petroleum-policy initial-MFE / high-MAE counterexample.
The first spike looked powerful, but the drawdown kept widening while company-specific resource rights or supply economics remained unrepaired.
This should not become Yellow/Green from price movement alone.
```

---

## 7. Machine-readable trigger JSONL

```jsonl
{"row_type":"trigger","research_id":"R4L77_C16_EAST_SEA_GAS_RESOURCE_POLICY_ROUTER","round":"R4","loop":77,"large_sector_id":"L4_MATERIALS_SPREAD_RESOURCE","canonical_archetype_id":"C16_STRATEGIC_RESOURCE_POLICY_SUPPLY","fine_archetype_id":"EAST_SEA_GAS_OIL_RESOURCE_POLICY_SUPPLY_RIGHTS_AND_THEME_SPIKE_HIGH_MAE_ROUTER","symbol":"036460","name":"한국가스공사","trigger_type":"Stage2-Actionable-Guarded","trigger_family":"east_sea_gas_resource_policy_supply_rights_state_backed_low_mae_high_mfe","trigger_date":"2024-06-03","entry_date":"2024-06-04","entry_price":40800.0,"entry_price_type":"next_tradable_open_after_east_sea_gas_resource_policy_burst","price_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","mfe_30d_pct":58.09,"mae_30d_pct":-8.46,"mfe_90d_pct":58.09,"mae_90d_pct":-10.54,"mfe_180d_pct":58.09,"mae_180d_pct":-10.54,"peak_price_180d":64500.0,"peak_date_180d":"2024-06-20","trough_price_180d":36500.0,"trough_date_180d":"2024-08-05","calibration_usable":true,"case_polarity":"positive_guarded_state_backed_resource_supply","evidence_url_pending":true,"source_proxy_only":true,"non_price_evidence_strength":"medium_pending_url_repair","price_only_blowoff":false,"expected_stage_current_profile":"Stage2-Guarded_to_Yellow_if_exploration_rights_government_execution_capex_cashflow_bridge_repaired","residual_error_type":"state_backed_resource_policy_supply_path_had_high_mfe_but_green_requires_url_repaired_resource_rights_execution_capex_and_cashflow_bridge"}
{"row_type":"trigger","research_id":"R4L77_C16_EAST_SEA_GAS_RESOURCE_POLICY_ROUTER","round":"R4","loop":77,"large_sector_id":"L4_MATERIALS_SPREAD_RESOURCE","canonical_archetype_id":"C16_STRATEGIC_RESOURCE_POLICY_SUPPLY","fine_archetype_id":"EAST_SEA_GAS_OIL_RESOURCE_POLICY_SUPPLY_RIGHTS_AND_THEME_SPIKE_HIGH_MAE_ROUTER","symbol":"039610","name":"화성밸브","trigger_type":"Stage2-Actionable-Guarded","trigger_family":"gas_valve_infrastructure_resource_policy_high_mfe_high_mae_guarded","trigger_date":"2024-06-03","entry_date":"2024-06-04","entry_price":8630.0,"entry_price_type":"next_tradable_open_after_gas_valve_resource_infrastructure_policy_burst","price_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","mfe_30d_pct":28.39,"mae_30d_pct":-21.21,"mfe_90d_pct":56.08,"mae_90d_pct":-21.21,"mfe_180d_pct":56.08,"mae_180d_pct":-21.21,"peak_price_180d":13470.0,"peak_date_180d":"2024-08-20","trough_price_180d":6800.0,"trough_date_180d":"2024-07-03","calibration_usable":true,"case_polarity":"positive_guarded_high_mfe_high_mae_resource_infra","evidence_url_pending":true,"source_proxy_only":true,"non_price_evidence_strength":"medium_low_pending_url_repair","price_only_blowoff":false,"expected_stage_current_profile":"Stage2-Guarded_only_until_pipeline_valve_order_procurement_margin_bridge_repaired","residual_error_type":"gas_valve_resource_policy_path_had_high_mfe_but_early_high_mae_requires_url_repaired_order_procurement_margin_bridge_before_yellow_green"}
{"row_type":"trigger","research_id":"R4L77_C16_EAST_SEA_GAS_RESOURCE_POLICY_ROUTER","round":"R4","loop":77,"large_sector_id":"L4_MATERIALS_SPREAD_RESOURCE","canonical_archetype_id":"C16_STRATEGIC_RESOURCE_POLICY_SUPPLY","fine_archetype_id":"EAST_SEA_GAS_OIL_RESOURCE_POLICY_SUPPLY_RIGHTS_AND_THEME_SPIKE_HIGH_MAE_ROUTER","symbol":"024060","name":"흥구석유","trigger_type":"Stage2-FalsePositive-Candidate","trigger_family":"oil_distributor_resource_policy_theme_first_window_mfe_later_drawdown","trigger_date":"2024-06-03","entry_date":"2024-06-04","entry_price":17520.0,"entry_price_type":"next_tradable_open_after_oil_resource_policy_theme_burst","price_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","mfe_30d_pct":19.58,"mae_30d_pct":-20.03,"mfe_90d_pct":25.0,"mae_90d_pct":-29.45,"mfe_180d_pct":31.28,"mae_180d_pct":-29.45,"peak_price_180d":23000.0,"peak_date_180d":"2024-10-04","trough_price_180d":12360.0,"trough_date_180d":"2024-07-26","calibration_usable":true,"case_polarity":"counterexample_theme_first_window_mfe_later_high_mae","evidence_url_pending":true,"source_proxy_only":true,"non_price_evidence_strength":"low_pending_url_repair","price_only_blowoff":false,"expected_stage_current_profile":"Stage2-Guarded_or_local_4B_watch_until_resource_rights_margin_volume_bridge_repaired","residual_error_type":"oil_distributor_resource_policy_theme_had_mfe_but_early_and_90d_high_mae_blocks_yellow_green_without_resource_supply_margin_bridge"}
{"row_type":"trigger","research_id":"R4L77_C16_EAST_SEA_GAS_RESOURCE_POLICY_ROUTER","round":"R4","loop":77,"large_sector_id":"L4_MATERIALS_SPREAD_RESOURCE","canonical_archetype_id":"C16_STRATEGIC_RESOURCE_POLICY_SUPPLY","fine_archetype_id":"EAST_SEA_GAS_OIL_RESOURCE_POLICY_SUPPLY_RIGHTS_AND_THEME_SPIKE_HIGH_MAE_ROUTER","symbol":"004090","name":"한국석유","trigger_type":"Stage2-FalsePositive-Candidate","trigger_family":"petroleum_material_resource_policy_theme_initial_mfe_high_mae","trigger_date":"2024-06-03","entry_date":"2024-06-04","entry_price":21650.0,"entry_price_type":"next_tradable_open_after_petroleum_resource_policy_theme_burst","price_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","mfe_30d_pct":29.79,"mae_30d_pct":-21.29,"mfe_90d_pct":29.79,"mae_90d_pct":-28.22,"mfe_180d_pct":29.79,"mae_180d_pct":-34.5,"peak_price_180d":28100.0,"peak_date_180d":"2024-06-05","trough_price_180d":14180.0,"trough_date_180d":"2024-11-29","calibration_usable":true,"case_polarity":"counterexample_initial_mfe_high_mae_policy_theme","evidence_url_pending":true,"source_proxy_only":true,"non_price_evidence_strength":"low_pending_url_repair","price_only_blowoff":false,"expected_stage_current_profile":"Stage2-Guarded_at_most_or_local_4B_watch_until_resource_policy_to_revenue_margin_bridge_repaired","residual_error_type":"petroleum_resource_policy_theme_had_initial_mfe_but_high_mae_without_company_specific_supply_rights_revenue_margin_bridge"}
```

---

## 8. Score simulation and raw component breakdown

This is shadow-only and does not change production scoring.

| symbol | resource rights / authority | policy execution bridge | procurement / order visibility | volume / tariff / spread bridge | market mispricing | MAE risk control | information confidence | shadow total | intended route |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| `036460` | 12 | 10 | 8 | 8 | 13 | 9 | 6 | 66 | Stage2-Guarded / Yellow after evidence repair |
| `039610` | 6 | 5 | 6 | 5 | 11 | 3 | 5 | 41 | Stage2-Guarded only until procurement/order bridge repair |
| `024060` | 3 | 3 | 2 | 3 | 5 | 1 | 4 | 21 | Stage2-Guarded at most / local 4B watch |
| `004090` | 3 | 3 | 2 | 3 | 5 | 0 | 4 | 20 | blocked Stage2 or local 4B high-MAE watch |

### Current calibrated profile stress test

The current calibrated profile already blocks pure price-only blowoff.  
The remaining C16 issue is **resource-policy label without company-specific resource-supply bridge**:

```text
C16 state-backed supply-rights path:
  policy relevance
  + state-backed execution relevance
  + MFE_90D >= +50%
  + MAE_90D around -10%
  + evidence remains source_proxy_only
  => Stage2-Guarded; Yellow only after rights/execution/capex/cash-flow evidence repair

C16 infrastructure supplier high-MFE/high-MAE path:
  gas infrastructure relevance
  + MFE_90D >= +50%
  + MAE_30D <= -20%
  + no order/procurement evidence
  => Stage2-Guarded at most, no Green

C16 oil/petroleum theme high-MAE path:
  policy theme produces first-window MFE
  + MAE_30D <= -20% or MAE_90D <= -25%
  + no company-specific rights/volume/margin bridge
  => cap at local 4B watch or block Stage2

C16 initial-MFE widening-MAE path:
  early MFE exists
  + MAE_180D <= -30%
  + evidence remains source_proxy_only
  => no Yellow/Green
```

`036460` prevents overblocking of real strategic-resource policy paths.  
`039610` shows that infrastructure suppliers can have high MFE but need an early-MAE guard.  
`024060` and `004090` show why oil/petroleum theme labels need company-specific volume, supply, spread, and margin evidence.

---

## 9. Aggregate metrics

```json
{
  "row_type": "aggregate",
  "research_id": "R4L77_C16_EAST_SEA_GAS_RESOURCE_POLICY_ROUTER",
  "round": "R4",
  "loop": 77,
  "large_sector_id": "L4_MATERIALS_SPREAD_RESOURCE",
  "canonical_archetype_id": "C16_STRATEGIC_RESOURCE_POLICY_SUPPLY",
  "fine_archetype_id": "EAST_SEA_GAS_OIL_RESOURCE_POLICY_SUPPLY_RIGHTS_AND_THEME_SPIKE_HIGH_MAE_ROUTER",
  "case_count": 4,
  "calibration_usable_case_count": 4,
  "positive_guarded_case_count": 2,
  "counterexample_count": 2,
  "new_symbol_count": 4,
  "source_proxy_only_count": 4,
  "evidence_url_pending_count": 4,
  "avg_mfe_30d_pct": 33.96,
  "avg_mae_30d_pct": -17.75,
  "avg_mfe_90d_pct": 42.24,
  "avg_mae_90d_pct": -22.36,
  "avg_mfe_180d_pct": 43.81,
  "avg_mae_180d_pct": -23.93,
  "max_mfe_180d_pct": 58.09,
  "worst_mae_180d_pct": -34.5
}
```

---

## 10. 4B proximity split

```json
{
  "row_type": "4b_split",
  "research_id": "R4L77_C16_EAST_SEA_GAS_RESOURCE_POLICY_ROUTER",
  "stage2_guarded_or_yellow_candidate": [
    {
      "symbol": "036460",
      "reason": "state-backed gas resource policy path had +58.09% MFE and did not cross deep high-MAE; requires rights/execution/capex bridge repair"
    }
  ],
  "stage2_guarded_or_local_4b_watch": [
    {
      "symbol": "039610",
      "reason": "gas-valve policy path had +56.08% 180D MFE but early MAE reached -21.21%"
    },
    {
      "symbol": "024060",
      "reason": "oil distributor policy theme had +31.28% 180D MFE but 90D/180D MAE reached -29.45%"
    }
  ],
  "blocked_stage2_or_local_4b_watch": [
    {
      "symbol": "004090",
      "reason": "petroleum policy theme had +29.79% MFE but 180D MAE reached -34.50% without resource-supply bridge"
    }
  ],
  "full_4b_or_green_requires_non_price_evidence": [
    "resource rights and execution authority",
    "exploration / development / capex schedule",
    "procurement and supply-chain route",
    "pipe / valve order visibility for infrastructure suppliers",
    "volume / tariff / spread linkage",
    "gross margin and cash-flow conversion"
  ]
}
```

---

## 11. Shadow rule candidate

```yaml
row_type: canonical_archetype_rule_candidate
canonical_archetype_id: C16_STRATEGIC_RESOURCE_POLICY_SUPPLY
fine_archetype_id: EAST_SEA_GAS_OIL_RESOURCE_POLICY_SUPPLY_RIGHTS_AND_THEME_SPIKE_HIGH_MAE_ROUTER
rule_name: C16_east_sea_gas_oil_resource_policy_supply_rights_and_theme_spike_high_mae_router
production_scoring_changed: false
shadow_weight_only: true
```

### Proposed routing logic

```text
For C16 East Sea gas / oil / resource-policy supply cases:

Tier A: state-backed supply-rights candidate
  Conditions:
    - resource rights, execution authority, capex schedule, and cash-flow bridge are URL-repaired
    - MFE_90D >= +40%
    - MAE_90D > -12%
  Routing:
    - Stage2-Guarded allowed
    - Stage3-Yellow allowed after evidence repair
    - Green only after rights / execution / capex / cash-flow bridge is verified

Tier B: high-MFE infrastructure supplier with early high MAE
  Conditions:
    - MFE_90D >= +40%
    - MAE_30D <= -20%
    - evidence_url_pending or source_proxy_only remains true
  Routing:
    - Stage2-Guarded at most
    - no Green until order/procurement/margin evidence repair

Tier C: oil/petroleum resource-policy theme high-MAE path
  Conditions:
    - MFE_30D >= +15%
    - MAE_30D <= -20% or MAE_90D <= -25%
    - no company-specific resource-rights / volume / margin bridge
  Routing:
    - local 4B watch
    - no Yellow/Green

Tier D: widening-MAE policy theme
  Conditions:
    - MFE_180D < +35%
    - MAE_180D <= -30%
    - bridge evidence remains unrepaired
  Routing:
    - block Stage2 or local 4B/high-MAE watch
```

### Suggested shadow delta

```json
{
  "row_type": "shadow_weight",
  "axis": "c16_east_sea_gas_oil_resource_policy_supply_rights_and_theme_spike_high_mae_router",
  "scope": "canonical_archetype_id:C16_STRATEGIC_RESOURCE_POLICY_SUPPLY",
  "proposal": {
    "source_proxy_only_green_allowed": false,
    "resource_policy_label_alone_stage2_allowed": false,
    "resource_rights_execution_capex_cashflow_bridge_required_for_green": true,
    "verified_state_backed_mfe90_threshold_pct": 40.0,
    "verified_state_backed_mae90_min_pct": -12.0,
    "infrastructure_high_mfe_threshold_90d_pct": 40.0,
    "infrastructure_high_mae30_threshold_pct": -20.0,
    "theme_mfe30_threshold_pct": 15.0,
    "theme_mae30_threshold_pct": -20.0,
    "theme_mae90_threshold_pct": -25.0,
    "widening_mae_mfe180_threshold_pct": 35.0,
    "widening_mae180_threshold_pct": -30.0,
    "positive_weight_blocked_until_url_repair": true
  },
  "confidence": "medium_low_until_url_repair",
  "apply_now": false,
  "reason": "One state-backed gas-resource holdout, one gas-infrastructure high-MFE/high-MAE path, and two oil/petroleum theme high-MAE failures show that C16 should require URL-repaired resource rights, execution authority, procurement/order, volume, tariff/spread, and cash-flow evidence before Yellow/Green."
}
```

---

## 12. Residual contribution summary

```json
{
  "row_type": "residual_contribution",
  "research_id": "R4L77_C16_EAST_SEA_GAS_RESOURCE_POLICY_ROUTER",
  "large_sector_id": "L4_MATERIALS_SPREAD_RESOURCE",
  "canonical_archetype_id": "C16_STRATEGIC_RESOURCE_POLICY_SUPPLY",
  "contribution": "Adds four non-top-covered C16 East Sea gas / oil / petroleum / gas-valve resource-policy cases and separates state-backed resource-supply rerating from high-MAE policy-theme paths. C16 Yellow/Green should require URL-repaired resource rights, execution authority, exploration/development capex, procurement/order visibility, volume/tariff/spread linkage, margin, and cash-flow conversion evidence.",
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
  "data_quality_blocker": "All four non-price resource-policy triggers require URL-level repair before positive weight promotion.",
  "guardrail_added": "C16 source_proxy_only oil/petroleum/resource-policy theme cases with MAE_30D <= -20% or MAE_90D <= -25% should cap at Stage2-Guarded/local 4B; cases with MFE_180D < +35% and MAE_180D <= -30% should block Stage2 or route to high-MAE watch."
}
```

One-line contribution:

```text
This loop adds 4 new independent cases, 2 counterexamples, and 2 residual errors for R4/L4_MATERIALS_SPREAD_RESOURCE/C16_STRATEGIC_RESOURCE_POLICY_SUPPLY.
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
    036460: false
    039610: false
    024060: false
    004090: false
  evidence_url_pending:
    036460: true
    039610: true
    024060: true
    004090: true
  source_proxy_only:
    036460: true
    039610: true
    024060: true
    004090: true
```

Limitations:

```text
- Price path is validated against Stock-Web tradable OHLC rows.
- Non-price evidence is not URL-repaired in this run.
- Therefore this artifact is useful for C16 East Sea gas / oil / strategic resource policy residual shape and high-MAE guardrail design, but should not promote positive weights until filings, government policy documents, IR, procurement/order disclosures, or reports verify resource rights, execution authority, capex schedule, procurement, order visibility, volume/tariff/spread linkage, margin, and cash-flow conversion.
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
2. Preserve R4 / loop 77 metadata.
3. Add the cases to C16_STRATEGIC_RESOURCE_POLICY_SUPPLY only if parser validation passes.
4. Treat all four non-price triggers as evidence_url_pending=true and source_proxy_only=true until URL-level evidence is repaired.
5. Do not use these rows for positive weight promotion until filings/government-policy-document/IR/procurement-order/report data verifies resource rights, execution authority, capex schedule, procurement route, pipe/valve order visibility, volume/tariff/spread linkage, gross margin, and cash-flow conversion.
6. Add a shadow-only rule candidate named C16_east_sea_gas_oil_resource_policy_supply_rights_and_theme_spike_high_mae_router.
7. Do not loosen Stage3-Green.
8. Add C16-specific guards:
   - source_proxy_only -> no Green
   - resource policy label alone -> no Stage2 promotion
   - Green requires repaired resource rights / execution / capex / cash-flow bridge
   - MFE_90D >= +40% and MAE_90D > -12% may remain Stage2-Guarded / Yellow watch after evidence repair
   - MFE_90D >= +40% but MAE_30D <= -20% -> Stage2-Guarded at most until order/procurement/margin evidence repair
   - MFE_30D >= +15% and MAE_30D <= -20% or MAE_90D <= -25% -> local 4B watch / no Yellow-Green
   - MFE_180D < +35% and MAE_180D <= -30% -> block Stage2 or local high-MAE watch
9. Keep production scoring unchanged unless later batch promotion logic independently marks this axis safe.
```

---

## 15. Next round state

```text
completed_round = R4
completed_loop = 77
next_round = R5
next_loop = 77
next_large_sector_hint = L5_CONSUMER_BRAND_DISTRIBUTION
round_schedule_status = valid
round_sector_consistency = pass
```
