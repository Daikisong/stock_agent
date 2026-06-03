# E2R Stock-Web v12 Residual Research — R9 Loop 75

```yaml
research_session: post_calibrated_sector_archetype_residual_research
mode: historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12
completed_round: R9
completed_loop: 75
next_round: R10
next_loop: 75
large_sector_id: L3_BATTERY_EV_GREEN_MOBILITY
canonical_archetype_id: C13_BATTERY_JV_UTILIZATION_AMPC_IRA
fine_archetype_id: COPPER_FOIL_CATHODE_ELECTROLYTE_UTILIZATION_IRA_AMPC_AND_HIGH_MAE_ROUTER
output_file: e2r_stock_web_v12_residual_round_R9_loop_75_L3_BATTERY_EV_GREEN_MOBILITY_C13_BATTERY_JV_UTILIZATION_AMPC_IRA_research.md
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
completed_loop  = 75
large_sector_id = L8_PLATFORM_CONTENT_SW_SECURITY
canonical_archetype_id = C27_CONTENT_IP_GLOBAL_MONETIZATION
```

Therefore:

```text
scheduled_round = R9
scheduled_loop  = 75
```

R9 permits:

```text
large_sector_id = L3_BATTERY_EV_GREEN_MOBILITY
or
large_sector_id = L9_CONSTRUCTION_REALESTATE_HOUSING
```

This run selects the L3 battery branch:

```text
large_sector_id = L3_BATTERY_EV_GREEN_MOBILITY
canonical_archetype_id = C13_BATTERY_JV_UTILIZATION_AMPC_IRA
fine_archetype_id = COPPER_FOIL_CATHODE_ELECTROLYTE_UTILIZATION_IRA_AMPC_AND_HIGH_MAE_ROUTER
```

This is a valid R9 pairing.

---

## 1. Why this R9/C13 run

The no-repeat ledger shows C13 is relatively thin and concentrated in large cell/JV names:

```text
C13_BATTERY_JV_UTILIZATION_AMPC_IRA:
  rows: 37
  symbols: 7
  date_range: 2022-05-25~2025-04-08
  good/bad S2: 8/9
  4B/4C: 7/2
  URL/proxy: 0/0
  top covered symbols: 373220(14), 006400(13), 096770(5), 003670(2), 005070(1), 020150(1)
```

This file avoids the most repeated battery cell/JV names and expands the C13 sample into second-tier materials and utilization-sensitive suppliers:

```text
020150 롯데에너지머티리얼즈
005070 코스모신소재
278280 천보
```

Research question:

```text
Can C13 separate usable battery material utilization / IRA-supply-chain rerating from material recovery labels where AMPC/IRA/JV relevance exists but customer volume, utilization, pass-through, and margin conversion are not repaired?
```

C13 is a utilization bridge. A subsidy or IRA label is the wind on the factory roof; the actual turbine is customer volume, utilization, conversion spread, and margin. Without that spinning turbine, the label can move the stock for a few weeks and still leave the entry exposed to severe MAE.

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
| `020150` | 롯데에너지머티리얼즈 | active_like / KOSPI | none listed | true |
| `005070` | 코스모신소재 | active_like / KOSPI | no 2024 overlap; latest listed candidate 2019-11-13 | true |
| `278280` | 천보 | active_like / KOSDAQ / KOSDAQ GLOBAL history | none listed | true |

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
The Stock-Web price path is fully validated, but company-level utilization, customer call-off risk, IRA/AMPC pass-through, JV or localization benefit, order visibility, inventory, working capital, ASP/spread, and gross-margin evidence still require later URL repair through filings, IR decks, customer data, subsidy disclosures, or sell-side reports before production weight promotion.
```

C13 interpretation used here:

```text
C13 is not simply “battery material stock bounced.”
It asks whether IRA/AMPC/JV/utilization relevance converts into:
- customer volume and call-off resistance,
- plant utilization and localization economics,
- order or shipment visibility,
- ASP/spread and input pass-through,
- working-capital and inventory quality,
- gross margin and cash-flow conversion,
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
020150 + C13_BATTERY_JV_UTILIZATION_AMPC_IRA -> no direct match found
005070 + C13_BATTERY_JV_UTILIZATION_AMPC_IRA -> no direct match found
278280 + C13_BATTERY_JV_UTILIZATION_AMPC_IRA -> no direct match found
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
| `R9L75_C13_020150_20240321` | `020150` 롯데에너지머티리얼즈 | copper foil / IRA supply-chain utilization rerating | positive-guarded high-MFE / later-MAE watch |
| `R9L75_C13_005070_20240213` | `005070` 코스모신소재 | cathode material IRA/AMPC supply-chain initial-MFE path | later hard-MAE counterexample |
| `R9L75_C13_278280_20240222` | `278280` 천보 | electrolyte additive utilization recovery | weak-MFE extreme-MAE counterexample |

The intended residual:

```text
C13 should separate:
1. utilization-sensitive material paths with strong 30D/90D MFE but later MAE that still requires evidence repair;
2. cathode/material IRA labels where the initial MFE is real but 180D MAE blocks Yellow/Green;
3. electrolyte recovery labels where MFE never expands and MAE enters hard-failure territory.
```

---

## 6. Stock-Web OHLC and backtest

### 6.1 `020150` 롯데에너지머티리얼즈 — copper foil / IRA supply-chain utilization guarded path

Trigger:

```text
trigger_date = 2024-03-20
trigger_type = Stage2-Actionable-Guarded
trigger_family = copper_foil_ira_supply_chain_utilization_high_mfe_later_mae
entry_date = 2024-03-21
entry_price = 43000.0
entry_price_type = next_tradable_open_after_copper_foil_utilization_ira_supply_chain_burst
```

Relevant Stock-Web rows:

```csv
d,o,h,l,c,v,a,mc,s,m
2024-03-20,40350.0,43200.0,39950.0,42350.0,563283.0,23584920000.0,1952793862250.0,46110835,KOSPI
2024-03-21,43000.0,49200.0,42850.0,47050.0,2039716.0,95044578800.0,2169514786750.0,46110835,KOSPI
2024-03-27,49550.0,52400.0,49150.0,51000.0,528464.0,27023694750.0,2351652585000.0,46110835,KOSPI
2024-04-18,40650.0,42600.0,40400.0,42000.0,193288.0,8072944250.0,1936655070000.0,46110835,KOSPI
2024-05-16,47000.0,51000.0,46950.0,49550.0,797933.0,39416264900.0,2284791874250.0,46110835,KOSPI
2024-06-18,58000.0,59200.0,56700.0,57300.0,565460.0,32760920400.0,2642150845500.0,46110835,KOSPI
2024-08-05,36100.0,36750.0,30500.0,32200.0,468908.0,15821669100.0,1484768887000.0,46110835,KOSPI
2024-09-05,40050.0,45650.0,40050.0,43000.0,1121196.0,48476794250.0,1982765905000.0,46110835,KOSPI
```

Backtest:

| window | peak/high | peak date | trough/low | trough date | MFE | MAE |
|---|---:|---|---:|---|---:|---:|
| 30 calendar days | 52400 | 2024-03-27 | 40400 | 2024-04-18 | +21.86% | -6.05% |
| 90 calendar days | 59200 | 2024-06-18 | 40400 | 2024-04-18 | +37.67% | -6.05% |
| 180 calendar days | 59200 | 2024-06-18 | 30500 | 2024-08-05 | +37.67% | -29.07% |

Interpretation:

```text
020150 is the C13 positive-guarded holdout.
The 30D/90D MFE was strong enough to preserve a Stage2-Guarded route, but the 180D drawdown is too large for Yellow/Green while evidence remains source-proxy-only.
It should require URL-repaired utilization, customer volume, copper-foil supply-chain localization, and margin evidence.
```

### 6.2 `005070` 코스모신소재 — cathode material IRA/AMPC label with later hard MAE

Trigger:

```text
trigger_date = 2024-02-08
trigger_type = Stage2-Actionable-Guarded
trigger_family = cathode_material_ira_ampc_supply_chain_initial_mfe_later_hard_mae
entry_date = 2024-02-13
entry_price = 161600.0
entry_price_type = next_tradable_open_after_cathode_material_ira_supply_chain_burst
```

Relevant Stock-Web rows:

```csv
d,o,h,l,c,v,a,mc,s,m
2024-02-08,156600.0,164200.0,155500.0,159900.0,399624.0,63981118600.0,5198469884400.0,32510756,KOSPI
2024-02-13,161600.0,161700.0,154300.0,157100.0,242920.0,38294076700.0,5107439767600.0,32510756,KOSPI
2024-02-21,185600.0,194300.0,182100.0,184500.0,570202.0,107192154500.0,5998234482000.0,32510756,KOSPI
2024-03-12,167600.0,175500.0,167600.0,175500.0,239597.0,41196170700.0,5705637678000.0,32510756,KOSPI
2024-04-08,149700.0,153800.0,147000.0,152200.0,181289.0,27265261700.0,4948137063200.0,32510756,KOSPI
2024-07-08,145800.0,160300.0,143000.0,149800.0,351768.0,52983946800.0,4870111248800.0,32510756,KOSPI
2024-08-05,124900.0,124900.0,100100.0,106800.0,482707.0,54265885300.0,3472148740800.0,32510756,KOSPI
2024-09-26,119800.0,132900.0,119300.0,132400.0,302414.0,38694939900.0,4304424094400.0,32510756,KOSPI
```

Backtest:

| window | peak/high | peak date | trough/low | trough date | MFE | MAE |
|---|---:|---|---:|---|---:|---:|
| 30 calendar days | 194300 | 2024-02-21 | 154200 | 2024-02-14 | +20.24% | -4.58% |
| 90 calendar days | 194300 | 2024-02-21 | 147000 | 2024-04-08 | +20.24% | -9.03% |
| 180 calendar days | 194300 | 2024-02-21 | 100100 | 2024-08-05 | +20.24% | -38.06% |

Interpretation:

```text
005070 is the initial-MFE / later hard-MAE counterexample.
The first 30D path looked acceptable, but the 180D window exposed a deep drawdown before utilization and margin evidence was repaired.
This should cap at Stage2-Guarded or local 4B/high-MAE watch, not Yellow/Green.
```

### 6.3 `278280` 천보 — electrolyte additive recovery label with weak MFE and extreme MAE

Trigger:

```text
trigger_date = 2024-02-21
trigger_type = Stage2-FalsePositive-Candidate
trigger_family = electrolyte_additive_utilization_recovery_weak_mfe_extreme_mae
entry_date = 2024-02-22
entry_price = 96500.0
entry_price_type = next_tradable_open_after_electrolyte_utilization_recovery_spike
```

Relevant Stock-Web rows:

```csv
d,o,h,l,c,v,a,mc,s,m
2024-02-21,90800.0,99800.0,90000.0,95600.0,164733.0,15846436600.0,956000000000.0,10000000,KOSDAQ GLOBAL
2024-02-22,96500.0,98800.0,95100.0,97700.0,102695.0,10006757900.0,977000000000.0,10000000,KOSDAQ GLOBAL
2024-03-15,89100.0,89200.0,86200.0,86400.0,63835.0,5550171500.0,864000000000.0,10000000,KOSDAQ GLOBAL
2024-04-19,72400.0,72800.0,71200.0,71700.0,24849.0,1782264100.0,717000000000.0,10000000,KOSDAQ GLOBAL
2024-06-12,79100.0,82200.0,77800.0,78000.0,66521.0,5289492600.0,780000000000.0,10000000,KOSDAQ GLOBAL
2024-08-05,60600.0,60800.0,49000.0,50400.0,99184.0,5352917450.0,504000000000.0,10000000,KOSDAQ
2024-10-07,62700.0,65500.0,62300.0,65300.0,42212.0,2727560900.0,653000000000.0,10000000,KOSDAQ
```

Backtest:

| window | peak/high | peak date | trough/low | trough date | MFE | MAE |
|---|---:|---|---:|---|---:|---:|
| 30 calendar days | 98800 | 2024-02-22 | 86200 | 2024-03-15 | +2.38% | -10.67% |
| 90 calendar days | 98800 | 2024-02-22 | 71200 | 2024-04-19 | +2.38% | -26.22% |
| 180 calendar days | 98800 | 2024-02-22 | 49000 | 2024-08-05 | +2.38% | -49.22% |

Interpretation:

```text
278280 is the hard C13 false-positive branch.
The electrolyte utilization/recovery label had almost no forward MFE and then moved into severe MAE.
This should block Stage2 or route to 4B/4C high-MAE watch unless fresh customer-volume, utilization, and margin evidence appears before entry.
```

---

## 7. Machine-readable trigger JSONL

```jsonl
{"row_type":"trigger","research_id":"R9L75_C13_BATTERY_MATERIAL_UTILIZATION_ROUTER","round":"R9","loop":75,"large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C13_BATTERY_JV_UTILIZATION_AMPC_IRA","fine_archetype_id":"COPPER_FOIL_CATHODE_ELECTROLYTE_UTILIZATION_IRA_AMPC_AND_HIGH_MAE_ROUTER","symbol":"020150","name":"롯데에너지머티리얼즈","trigger_type":"Stage2-Actionable-Guarded","trigger_family":"copper_foil_ira_supply_chain_utilization_high_mfe_later_mae","trigger_date":"2024-03-20","entry_date":"2024-03-21","entry_price":43000.0,"entry_price_type":"next_tradable_open_after_copper_foil_utilization_ira_supply_chain_burst","price_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","mfe_30d_pct":21.86,"mae_30d_pct":-6.05,"mfe_90d_pct":37.67,"mae_90d_pct":-6.05,"mfe_180d_pct":37.67,"mae_180d_pct":-29.07,"peak_price_180d":59200.0,"peak_date_180d":"2024-06-18","trough_price_180d":30500.0,"trough_date_180d":"2024-08-05","calibration_usable":true,"case_polarity":"positive_guarded_high_mfe_later_mae","evidence_url_pending":true,"source_proxy_only":true,"non_price_evidence_strength":"medium_pending_url_repair","price_only_blowoff":false,"expected_stage_current_profile":"Stage2-Guarded_to_Yellow_only_if_utilization_customer_margin_bridge_repaired","residual_error_type":"copper_foil_utilization_ira_path_had_high_mfe_but_later_mae_requires_url_repaired_customer_supply_margin_bridge_before_green"}
{"row_type":"trigger","research_id":"R9L75_C13_BATTERY_MATERIAL_UTILIZATION_ROUTER","round":"R9","loop":75,"large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C13_BATTERY_JV_UTILIZATION_AMPC_IRA","fine_archetype_id":"COPPER_FOIL_CATHODE_ELECTROLYTE_UTILIZATION_IRA_AMPC_AND_HIGH_MAE_ROUTER","symbol":"005070","name":"코스모신소재","trigger_type":"Stage2-Actionable-Guarded","trigger_family":"cathode_material_ira_ampc_supply_chain_initial_mfe_later_hard_mae","trigger_date":"2024-02-08","entry_date":"2024-02-13","entry_price":161600.0,"entry_price_type":"next_tradable_open_after_cathode_material_ira_supply_chain_burst","price_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","mfe_30d_pct":20.24,"mae_30d_pct":-4.58,"mfe_90d_pct":20.24,"mae_90d_pct":-9.03,"mfe_180d_pct":20.24,"mae_180d_pct":-38.06,"peak_price_180d":194300.0,"peak_date_180d":"2024-02-21","trough_price_180d":100100.0,"trough_date_180d":"2024-08-05","calibration_usable":true,"case_polarity":"counterexample_initial_mfe_later_hard_mae","evidence_url_pending":true,"source_proxy_only":true,"non_price_evidence_strength":"medium_low_pending_url_repair","price_only_blowoff":false,"expected_stage_current_profile":"Stage2-Guarded_or_local_4B_high_MAE_watch_until_utilization_margin_bridge_repaired","residual_error_type":"cathode_material_ira_label_had_initial_mfe_but_180d_mae_blocks_yellow_green_without_utilization_customer_margin_bridge"}
{"row_type":"trigger","research_id":"R9L75_C13_BATTERY_MATERIAL_UTILIZATION_ROUTER","round":"R9","loop":75,"large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C13_BATTERY_JV_UTILIZATION_AMPC_IRA","fine_archetype_id":"COPPER_FOIL_CATHODE_ELECTROLYTE_UTILIZATION_IRA_AMPC_AND_HIGH_MAE_ROUTER","symbol":"278280","name":"천보","trigger_type":"Stage2-FalsePositive-Candidate","trigger_family":"electrolyte_additive_utilization_recovery_weak_mfe_extreme_mae","trigger_date":"2024-02-21","entry_date":"2024-02-22","entry_price":96500.0,"entry_price_type":"next_tradable_open_after_electrolyte_utilization_recovery_spike","price_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","mfe_30d_pct":2.38,"mae_30d_pct":-10.67,"mfe_90d_pct":2.38,"mae_90d_pct":-26.22,"mfe_180d_pct":2.38,"mae_180d_pct":-49.22,"peak_price_180d":98800.0,"peak_date_180d":"2024-02-22","trough_price_180d":49000.0,"trough_date_180d":"2024-08-05","calibration_usable":true,"case_polarity":"counterexample_weak_mfe_extreme_mae","evidence_url_pending":true,"source_proxy_only":true,"non_price_evidence_strength":"low_pending_url_repair","price_only_blowoff":false,"expected_stage_current_profile":"blocked_Stage2_or_4B_4C_high_MAE_watch","residual_error_type":"electrolyte_utilization_recovery_label_had_weak_mfe_and_extreme_mae_without_customer_volume_margin_bridge"}
```

---

## 8. Score simulation and raw component breakdown

This is shadow-only and does not change production scoring.

| symbol | IRA/AMPC/JV relevance | customer volume bridge | utilization / localization | call-off risk control | market mispricing | margin / cash conversion | information confidence | shadow total | intended route |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| `020150` | 12 | 9 | 10 | 5 | 11 | 6 | 6 | 59 | Stage2-Guarded; Yellow only after evidence repair |
| `005070` | 10 | 6 | 6 | 3 | 8 | 4 | 5 | 42 | Stage2-Guarded or local 4B watch |
| `278280` | 7 | 3 | 3 | 2 | 2 | 2 | 4 | 23 | blocked Stage2 / 4B-4C high-MAE watch |

### Current calibrated profile stress test

The current calibrated profile already blocks pure price-only blowoff.  
The remaining C13 issue is **battery utilization / IRA label without customer-volume and margin conversion**:

```text
C13 high-MFE guarded path:
  utilization / IRA supply-chain relevance
  + 30D/90D MFE expands
  + evidence remains source_proxy_only
  + 180D MAE worsens beyond -25%
  => Stage2-Guarded only; Yellow/Green require repaired utilization/customer/margin bridge

C13 initial-MFE later-MAE path:
  first-window MFE exists
  + MAE_180D <= -35%
  + bridge evidence remains unrepaired
  => Stage2-Guarded at most, local 4B watch

C13 weak-MFE high-MAE path:
  MFE_30D < +5%
  + MAE_90D <= -25% or MAE_180D <= -45%
  + no utilization/customer/margin bridge
  => block Stage2 or route to 4B/4C high-MAE watch
```

`020150` prevents overblocking: not every materials utilization setup should be rejected.  
`005070` and `278280` show why IRA/AMPC/JV labels cannot bypass MAE and customer-volume guards.

---

## 9. Aggregate metrics

```json
{
  "row_type": "aggregate",
  "research_id": "R9L75_C13_BATTERY_MATERIAL_UTILIZATION_ROUTER",
  "round": "R9",
  "loop": 75,
  "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY",
  "canonical_archetype_id": "C13_BATTERY_JV_UTILIZATION_AMPC_IRA",
  "fine_archetype_id": "COPPER_FOIL_CATHODE_ELECTROLYTE_UTILIZATION_IRA_AMPC_AND_HIGH_MAE_ROUTER",
  "case_count": 3,
  "calibration_usable_case_count": 3,
  "positive_guarded_case_count": 1,
  "counterexample_count": 2,
  "new_symbol_count": 3,
  "source_proxy_only_count": 3,
  "evidence_url_pending_count": 3,
  "avg_mfe_30d_pct": 14.83,
  "avg_mae_30d_pct": -7.1,
  "avg_mfe_90d_pct": 20.1,
  "avg_mae_90d_pct": -13.77,
  "avg_mfe_180d_pct": 20.1,
  "avg_mae_180d_pct": -38.78,
  "max_mfe_180d_pct": 37.67,
  "worst_mae_180d_pct": -49.22
}
```

---

## 10. 4B proximity split

```json
{
  "row_type": "4b_split",
  "research_id": "R9L75_C13_BATTERY_MATERIAL_UTILIZATION_ROUTER",
  "stage2_guarded_or_yellow_candidate": [
    {
      "symbol": "020150",
      "reason": "30D/90D MFE was strong, but 180D MAE reached -29.07%; Yellow/Green requires utilization/customer/margin evidence repair"
    }
  ],
  "stage2_guarded_or_local_4b_watch": [
    {
      "symbol": "005070",
      "reason": "initial +20.24% MFE was real, but 180D MAE reached -38.06%"
    }
  ],
  "blocked_stage2_or_4c_watch": [
    {
      "symbol": "278280",
      "reason": "MFE stayed only +2.38%, while 90D MAE reached -26.22% and 180D MAE reached -49.22%"
    }
  ],
  "full_4b_or_green_requires_non_price_evidence": [
    "customer volume and call-off resistance",
    "plant utilization and localization economics",
    "IRA/AMPC or JV benefit pass-through",
    "order / shipment visibility",
    "ASP, spread, and input-cost pass-through",
    "working-capital and inventory quality",
    "gross margin and cash-flow conversion"
  ]
}
```

---

## 11. Shadow rule candidate

```yaml
row_type: canonical_archetype_rule_candidate
canonical_archetype_id: C13_BATTERY_JV_UTILIZATION_AMPC_IRA
fine_archetype_id: COPPER_FOIL_CATHODE_ELECTROLYTE_UTILIZATION_IRA_AMPC_AND_HIGH_MAE_ROUTER
rule_name: C13_material_utilization_ira_ampc_customer_volume_and_high_mae_router
production_scoring_changed: false
shadow_weight_only: true
```

### Proposed routing logic

```text
For C13 battery JV / utilization / AMPC / IRA cases:

Tier A: high-MFE utilization path
  Conditions:
    - IRA/AMPC/JV/utilization relevance is plausible
    - MFE_90D >= +25%
    - MAE_90D > -10%
    - evidence remains source_proxy_only
  Routing:
    - Stage2-Guarded allowed
    - Stage3-Yellow only after URL-repaired utilization/customer/margin bridge
    - no Green while evidence is pending

Tier B: initial-MFE / later hard-MAE material path
  Conditions:
    - MFE_30D >= +15%
    - MAE_180D <= -35%
    - no repaired customer-volume or margin bridge
  Routing:
    - Stage2-Guarded at most
    - local 4B/high-MAE watch
    - no Yellow/Green

Tier C: weak-MFE utilization recovery label
  Conditions:
    - MFE_30D < +5%
    - MAE_90D <= -25% or MAE_180D <= -45%
    - bridge evidence remains unrepaired
  Routing:
    - block Stage2
    - route to 4B/4C high-MAE watch
```

### Suggested shadow delta

```json
{
  "row_type": "shadow_weight",
  "axis": "c13_material_utilization_ira_ampc_customer_volume_and_high_mae_router",
  "scope": "canonical_archetype_id:C13_BATTERY_JV_UTILIZATION_AMPC_IRA",
  "proposal": {
    "source_proxy_only_green_allowed": false,
    "utilization_customer_margin_bridge_required_for_green": true,
    "high_mfe_utilization_stage2_guarded_allowed": true,
    "high_mfe_threshold_90d_pct": 25.0,
    "high_mfe_mae90_min_pct": -10.0,
    "initial_mfe_threshold_30d_pct": 15.0,
    "later_hard_mae_threshold_180d_pct": -35.0,
    "weak_mfe_threshold_30d_pct": 5.0,
    "weak_mfe_mae90_threshold_pct": -25.0,
    "weak_mfe_hard_mae180_threshold_pct": -45.0,
    "positive_weight_blocked_until_url_repair": true
  },
  "confidence": "medium_low_until_url_repair",
  "apply_now": false,
  "reason": "One utilization-sensitive high-MFE path and two material/electrolyte high-MAE failures show that C13 should require URL-repaired customer-volume, utilization, IRA/AMPC pass-through, working-capital, and margin evidence before Yellow/Green."
}
```

---

## 12. Residual contribution summary

```json
{
  "row_type": "residual_contribution",
  "research_id": "R9L75_C13_BATTERY_MATERIAL_UTILIZATION_ROUTER",
  "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY",
  "canonical_archetype_id": "C13_BATTERY_JV_UTILIZATION_AMPC_IRA",
  "contribution": "Adds three non-top-covered or low-repeat C13 battery material utilization/IRA cases and separates a high-MFE copper-foil guarded path from cathode and electrolyte high-MAE failures. C13 Yellow/Green should require URL-repaired customer volume, plant utilization, IRA/AMPC pass-through, order visibility, working capital, and margin conversion evidence.",
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
  "data_quality_blocker": "All three non-price battery utilization/IRA triggers require URL-level repair before positive weight promotion.",
  "guardrail_added": "C13 source_proxy_only cases with MFE_30D < +5% and MAE_90D <= -25% or MAE_180D <= -45% should block Stage2; first-window-MFE cases with MAE_180D <= -35% should cap at Stage2-Guarded or 4B watch until customer/utilization/margin evidence is repaired."
}
```

One-line contribution:

```text
This loop adds 3 new independent cases, 2 counterexamples, and 2 residual errors for R9/L3_BATTERY_EV_GREEN_MOBILITY/C13_BATTERY_JV_UTILIZATION_AMPC_IRA.
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
    020150: false
    005070: false
    278280: false
  evidence_url_pending:
    020150: true
    005070: true
    278280: true
  source_proxy_only:
    020150: true
    005070: true
    278280: true
```

Limitations:

```text
- Price path is validated against Stock-Web tradable OHLC rows.
- Non-price evidence is not URL-repaired in this run.
- Therefore this artifact is useful for C13 battery utilization / IRA / AMPC residual shape and high-MAE guardrail design, but should not promote positive weights until filings, IR, customer data, subsidy disclosures, or reports verify customer volume, utilization, localization economics, IRA/AMPC pass-through, order visibility, working capital, and margin conversion.
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
2. Preserve R9 / loop 75 metadata.
3. Add the cases to C13_BATTERY_JV_UTILIZATION_AMPC_IRA only if parser validation passes.
4. Treat all three non-price triggers as evidence_url_pending=true and source_proxy_only=true until URL-level evidence is repaired.
5. Do not use these rows for positive weight promotion until filings/IR/customer/subsidy-disclosure/report data verifies customer volume, utilization, localization economics, IRA/AMPC pass-through, order visibility, working capital, and margin conversion.
6. Add a shadow-only rule candidate named C13_material_utilization_ira_ampc_customer_volume_and_high_mae_router.
7. Do not loosen Stage3-Green.
8. Add C13-specific guards:
   - source_proxy_only -> no Green
   - Green requires repaired utilization / customer volume / margin bridge
   - MFE_90D >= +25% and MAE_90D > -10% may remain Stage2-Guarded until evidence repair
   - MFE_30D >= +15% and MAE_180D <= -35% -> Stage2-Guarded at most / local 4B watch
   - MFE_30D < +5% and MAE_90D <= -25% or MAE_180D <= -45% -> block Stage2 / 4B-4C watch
9. Keep production scoring unchanged unless later batch promotion logic independently marks this axis safe.
```

---

## 15. Next round state

```text
completed_round = R9
completed_loop = 75
next_round = R10
next_loop = 75
next_large_sector_hint = L9_CONSTRUCTION_REALESTATE_HOUSING
round_schedule_status = valid
round_sector_consistency = pass
```
