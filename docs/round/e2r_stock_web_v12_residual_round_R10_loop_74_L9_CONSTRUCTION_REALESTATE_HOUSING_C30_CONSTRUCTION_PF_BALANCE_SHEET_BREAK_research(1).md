# E2R Stock-Web v12 Residual Research — R10 Loop 74

```yaml
research_session: post_calibrated_sector_archetype_residual_research
mode: historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12
completed_round: R10
completed_loop: 74
next_round: R11
next_loop: 74
large_sector_id: L9_CONSTRUCTION_REALESTATE_HOUSING
canonical_archetype_id: C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK
fine_archetype_id: MIDSMALL_CONSTRUCTION_PF_RELIEF_SPIKE_AND_WEAK_MFE_SLOW_FADE_ROUTER
output_file: e2r_stock_web_v12_residual_round_R10_loop_74_L9_CONSTRUCTION_REALESTATE_HOUSING_C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK_research.md
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
completed_round = R9
completed_loop  = 74
large_sector_id = L3_BATTERY_EV_GREEN_MOBILITY
canonical_archetype_id = C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE
```

Therefore:

```text
scheduled_round = R10
scheduled_loop  = 74
```

R10 maps to:

```text
large_sector_id = L9_CONSTRUCTION_REALESTATE_HOUSING
```

This run selects:

```text
canonical_archetype_id = C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK
fine_archetype_id = MIDSMALL_CONSTRUCTION_PF_RELIEF_SPIKE_AND_WEAK_MFE_SLOW_FADE_ROUTER
```

This is a valid R10/L9 pairing.

---

## 1. Why this R10/C30 run

The no-repeat ledger shows C30 is heavily covered but concentrated in the usual large-contractors and already-stressed names:

```text
C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK:
  rows: 113
  symbols: 34
  date_range: 2021-03-11~2024-09-30
  good/bad S2: 15/18
  4B/4C: 14/28
  URL/proxy: 0/0
  top covered symbols: 006360(13), UNKNOWN_SYMBOL(13), 294870(12), 047040(11), 000720(8), 375500(6)
```

This file avoids those top-covered names and adds four mid/small construction cases:

```text
003070 코오롱글로벌
004960 한신공영
001260 남광토건
005960 동부건설
```

Research question:

```text
Can C30 separate genuine construction/PF relief rerating from weak-MFE slow-fade candidates where the sector label is plausible but liquidity, refinancing, receivables, and working-capital evidence are not yet repaired?
```

C30 is a balance-sheet bridge archetype. A construction rally can look like the ground has stopped shaking, but the model still has to inspect the pilings: PF guarantees, maturity wall, receivables, unbilled construction revenue, unsold inventory, and cash-flow repair. Without those pilings, the first bounce is only scaffolding.

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
| `003070` | 코오롱글로벌 | active_like / KOSPI | no selected 2024 entry-window overlap; 2023-01-31 candidate before test window | true |
| `004960` | 한신공영 | active_like / KOSPI | no 2024 overlap; old candidates only | true |
| `001260` | 남광토건 | active_like / KOSPI | no 2024 overlap; latest listed candidate 2016-02-05 | true |
| `005960` | 동부건설 | active_like / KOSPI | no 2024 overlap; latest listed candidate 2016-11-04 | true |

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
The Stock-Web price path is fully validated, but company-level PF guarantee exposure, refinancing, maturity wall, receivables, unbilled construction revenue, unsold inventory, cash-flow repair, and covenant/liquidity evidence still require later URL repair through filings, credit reports, IR decks, or disclosures before production weight promotion.
```

C30 interpretation used here:

```text
C30 is not simply “construction stock bounced.”
It asks whether the balance-sheet bridge is actually repaired:
- PF guarantee / contingent-liability exposure,
- refinancing and maturity-wall control,
- receivables and working capital,
- unsold inventory and cost-overrun risk,
- cash-flow and covenant headroom,
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
001260 + C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK -> no direct match found
004960 + C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK -> no direct match found
005960 + C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK -> no direct match found
003070 + C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK -> no direct match found
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
| `R10L74_C30_003070_20240529` | `003070` 코오롱글로벌 | mid/small construction policy/PF relief spike | positive-guarded high-MFE holdout |
| `R10L74_C30_004960_20240129` | `004960` 한신공영 | low-PBR / PF repair contained-MAE path | positive-guarded contained-MAE |
| `R10L74_C30_001260_20240213` | `001260` 남광토건 | regional contractor PF relief, weak early MFE / delayed recovery | local 4B drawdown watch |
| `R10L74_C30_005960_20240202` | `005960` 동부건설 | PF/liquidity weak-MFE slow fade | weak-MFE counterexample |

The intended residual:

```text
C30 should separate:
1. policy/PF relief spikes that actually hold the entry and produce large MFE;
2. contained-MAE low-PBR/PF repair paths that may stay Stage2-Guarded;
3. weak-MFE slow fades where the sector label exists but liquidity repair evidence is not enough for Stage2/Green.
```

---

## 6. Stock-Web OHLC and backtest

### 6.1 `003070` 코오롱글로벌 — mid/small construction PF relief high-MFE holdout

Trigger:

```text
trigger_date = 2024-05-28
trigger_type = Stage2-Actionable-Guarded
trigger_family = midsmall_construction_policy_pf_relief_high_mfe_low_mae
entry_date = 2024-05-29
entry_price = 9400.0
entry_price_type = next_tradable_open_after_construction_policy_relief_spike
```

Relevant Stock-Web rows:

```csv
d,o,h,l,c,v,a,mc,s,m
2024-05-28,8510.0,10860.0,8440.0,9610.0,2823746.0,28367987440.0,181943371930.0,18932713,KOSPI
2024-05-29,9400.0,9400.0,8910.0,9040.0,278178.0,2526668170.0,171151725520.0,18932713,KOSPI
2024-06-04,9270.0,12100.0,9030.0,10700.0,2464149.0,26763592240.0,202580029100.0,18932713,KOSPI
2024-06-13,13870.0,15240.0,12690.0,12800.0,8289926.0,117739699830.0,242338726400.0,18932713,KOSPI
2024-06-20,12400.0,15740.0,11750.0,15740.0,6422155.0,93402790790.0,298000902620.0,18932713,KOSPI
2024-06-21,15740.0,16110.0,14040.0,14090.0,3012333.0,45383959560.0,266761926170.0,18932713,KOSPI
2024-08-05,9610.0,9620.0,8500.0,8800.0,124324.0,1113766920.0,166607874400.0,18932713,KOSPI
2024-11-25,10450.0,10850.0,10130.0,10500.0,506265.0,5312107230.0,198793486500.0,18932713,KOSPI
```

Backtest:

| window | peak/high | peak date | trough/low | trough date | MFE | MAE |
|---|---:|---|---:|---|---:|---:|
| 30 calendar days | 16110 | 2024-06-21 | 8910 | 2024-05-29 | +71.38% | -5.21% |
| 90 calendar days | 16110 | 2024-06-21 | 8500 | 2024-08-05 | +71.38% | -9.57% |
| 180 calendar days | 16110 | 2024-06-21 | 8500 | 2024-08-05 | +71.38% | -9.57% |

Interpretation:

```text
003070 is the C30 high-MFE positive holdout.
Even though the move was theme-sensitive and volatile, the selected next-open entry had strong MFE and did not suffer deep MAE.
The case should remain Stage2-Guarded / Yellow only after PF-liquidity and cash-flow evidence repair; it prevents the C30 guardrail from overblocking every construction relief spike.
```

### 6.2 `004960` 한신공영 — low-PBR / PF repair contained-MAE path

Trigger:

```text
trigger_date = 2024-01-26
trigger_type = Stage2-Actionable-Guarded
trigger_family = midsmall_contractor_low_pbr_pf_repair_contained_mae
entry_date = 2024-01-29
entry_price = 7040.0
entry_price_type = next_tradable_open_after_low_pbr_pf_relief
```

Relevant Stock-Web rows:

```csv
d,o,h,l,c,v,a,mc,s,m
2024-01-29,7040.0,7380.0,6990.0,7350.0,64015.0,462924810.0,85044659700.0,11570702,KOSPI
2024-02-02,7810.0,7810.0,7500.0,7630.0,82528.0,628723100.0,88284456260.0,11570702,KOSPI
2024-02-27,7090.0,7210.0,6990.0,7090.0,42665.0,302463650.0,82036277180.0,11570702,KOSPI
2024-04-15,6320.0,6390.0,6240.0,6380.0,23183.0,146304340.0,73821078760.0,11570702,KOSPI
2024-04-17,6280.0,6350.0,6160.0,6160.0,42098.0,263770630.0,71275524320.0,11570702,KOSPI
2024-05-14,6630.0,7290.0,6620.0,6830.0,145318.0,1002376350.0,79027894660.0,11570702,KOSPI
2024-07-30,7190.0,7560.0,6890.0,7340.0,255573.0,1871437550.0,84928952680.0,11570702,KOSPI
```

Backtest:

| window | peak/high | peak date | trough/low | trough date | MFE | MAE |
|---|---:|---|---:|---|---:|---:|
| 30 calendar days | 7810 | 2024-02-02 | 6990 | 2024-02-27 | +10.94% | -0.71% |
| 90 calendar days | 7810 | 2024-02-02 | 6160 | 2024-04-17 | +10.94% | -12.50% |
| 180 calendar days | 7810 | 2024-02-02 | 6160 | 2024-04-17 | +10.94% | -12.50% |

Interpretation:

```text
004960 is a contained-MAE positive-guarded path.
The 30D path was orderly, but the 90D/180D drawdown still requires evidence repair before Yellow/Green.
This should be Stage2-Guarded, not Green from low-PBR or sector relief alone.
```

### 6.3 `001260` 남광토건 — regional contractor delayed recovery / drawdown watch

Trigger:

```text
trigger_date = 2024-02-08
trigger_type = Stage2-Actionable-Guarded
trigger_family = regional_contractor_pf_relief_delayed_mfe_drawdown_watch
entry_date = 2024-02-13
entry_price = 7290.0
entry_price_type = next_tradable_open_after_regional_contractor_relief
```

Relevant Stock-Web rows:

```csv
d,o,h,l,c,v,a,mc,s,m
2024-02-08,7180.0,7290.0,7150.0,7290.0,3969.0,28617610.0,71679449880.0,9832572,KOSPI
2024-02-13,7290.0,7500.0,7230.0,7490.0,15583.0,115138920.0,73645964280.0,9832572,KOSPI
2024-02-14,7460.0,7660.0,7410.0,7570.0,10403.0,78806560.0,74432570040.0,9832572,KOSPI
2024-03-11,6730.0,6820.0,6600.0,6690.0,7526.0,50336380.0,65779906680.0,9832572,KOSPI
2024-04-08,6150.0,6200.0,6020.0,6150.0,15235.0,92908020.0,60470317800.0,9832572,KOSPI
2024-07-30,6950.0,8550.0,6800.0,7580.0,549241.0,4339598530.0,74530895760.0,9832572,KOSPI
2024-08-05,7320.0,7320.0,6450.0,6530.0,58215.0,396229420.0,64206695160.0,9832572,KOSPI
```

Backtest:

| window | peak/high | peak date | trough/low | trough date | MFE | MAE |
|---|---:|---|---:|---|---:|---:|
| 30 calendar days | 7660 | 2024-02-14 | 6600 | 2024-03-11 | +5.08% | -9.47% |
| 90 calendar days | 7660 | 2024-02-14 | 6020 | 2024-04-08 | +5.08% | -17.42% |
| 180 calendar days | 8550 | 2024-07-30 | 6020 | 2024-04-08 | +17.28% | -17.42% |

Interpretation:

```text
001260 is the delayed-recovery / drawdown-watch branch.
The 180D MFE eventually improved, but the first 90D path showed weak MFE and material MAE.
This should cap at Stage2-Guarded or local 4B watch until PF exposure, refinancing, and working-capital evidence are repaired.
```

### 6.4 `005960` 동부건설 — weak-MFE PF/liquidity slow fade

Trigger:

```text
trigger_date = 2024-02-01
trigger_type = Stage2-FalsePositive-Candidate
trigger_family = construction_pf_liquidity_weak_mfe_slow_fade
entry_date = 2024-02-02
entry_price = 5370.0
entry_price_type = next_tradable_open_after_construction_pf_relief
```

Relevant Stock-Web rows:

```csv
d,o,h,l,c,v,a,mc,s,m
2024-02-01,5350.0,5470.0,5330.0,5430.0,50896.0,275609000.0,124210506090.0,22874863,KOSPI
2024-02-02,5370.0,5430.0,5290.0,5300.0,135844.0,723172820.0,121605547900.0,22944443,KOSPI
2024-02-19,5400.0,5500.0,5360.0,5430.0,46761.0,253612090.0,124588325490.0,22944443,KOSPI
2024-02-27,5270.0,5330.0,5200.0,5220.0,63463.0,333127740.0,119769992460.0,22944443,KOSPI
2024-04-15,4830.0,4910.0,4805.0,4880.0,15986.0,77506300.0,111968881840.0,22944443,KOSPI
2024-06-13,4950.0,4980.0,4750.0,4855.0,129757.0,624270220.0,111404504975.0,22946345,KOSPI
2024-07-31,4930.0,4985.0,4925.0,4950.0,38671.0,191866010.0,113584407750.0,22946345,KOSPI
```

Backtest:

| window | peak/high | peak date | trough/low | trough date | MFE | MAE |
|---|---:|---|---:|---|---:|---:|
| 30 calendar days | 5500 | 2024-02-19 | 5200 | 2024-02-27 | +2.42% | -3.17% |
| 90 calendar days | 5500 | 2024-02-19 | 4805 | 2024-04-15 | +2.42% | -10.52% |
| 180 calendar days | 5500 | 2024-02-19 | 4750 | 2024-06-13 | +2.42% | -11.55% |

Interpretation:

```text
005960 is the weak-MFE slow-fade counterexample.
The downside was not a violent 4C collapse, but the trigger never produced enough MFE to deserve positive-stage promotion.
C30 needs this kind of slow-fade guard because PF/liquidity risk can fail by not rerating, not only by crashing.
```

---

## 7. Machine-readable trigger JSONL

```jsonl
{"row_type":"trigger","research_id":"R10L74_C30_MIDSMALL_CONSTRUCTION_PF_ROUTER","round":"R10","loop":74,"large_sector_id":"L9_CONSTRUCTION_REALESTATE_HOUSING","canonical_archetype_id":"C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK","fine_archetype_id":"MIDSMALL_CONSTRUCTION_PF_RELIEF_SPIKE_AND_WEAK_MFE_SLOW_FADE_ROUTER","symbol":"003070","name":"코오롱글로벌","trigger_type":"Stage2-Actionable-Guarded","trigger_family":"midsmall_construction_policy_pf_relief_high_mfe_low_mae","trigger_date":"2024-05-28","entry_date":"2024-05-29","entry_price":9400.0,"entry_price_type":"next_tradable_open_after_construction_policy_relief_spike","price_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","mfe_30d_pct":71.38,"mae_30d_pct":-5.21,"mfe_90d_pct":71.38,"mae_90d_pct":-9.57,"mfe_180d_pct":71.38,"mae_180d_pct":-9.57,"peak_price_180d":16110.0,"peak_date_180d":"2024-06-21","trough_price_180d":8500.0,"trough_date_180d":"2024-08-05","calibration_usable":true,"case_polarity":"positive_guarded_high_mfe_low_mae","evidence_url_pending":true,"source_proxy_only":true,"non_price_evidence_strength":"medium_pending_url_repair","price_only_blowoff":false,"expected_stage_current_profile":"Stage2-Guarded_to_Yellow_if_pf_liquidity_order_margin_bridge_repaired","residual_error_type":"positive_construction_policy_relief_path_requires_url_repaired_pf_liquidity_cashflow_bridge_before_green"}
{"row_type":"trigger","research_id":"R10L74_C30_MIDSMALL_CONSTRUCTION_PF_ROUTER","round":"R10","loop":74,"large_sector_id":"L9_CONSTRUCTION_REALESTATE_HOUSING","canonical_archetype_id":"C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK","fine_archetype_id":"MIDSMALL_CONSTRUCTION_PF_RELIEF_SPIKE_AND_WEAK_MFE_SLOW_FADE_ROUTER","symbol":"004960","name":"한신공영","trigger_type":"Stage2-Actionable-Guarded","trigger_family":"midsmall_contractor_low_pbr_pf_repair_contained_mae","trigger_date":"2024-01-26","entry_date":"2024-01-29","entry_price":7040.0,"entry_price_type":"next_tradable_open_after_low_pbr_pf_relief","price_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","mfe_30d_pct":10.94,"mae_30d_pct":-0.71,"mfe_90d_pct":10.94,"mae_90d_pct":-12.5,"mfe_180d_pct":10.94,"mae_180d_pct":-12.5,"peak_price_180d":7810.0,"peak_date_180d":"2024-02-02","trough_price_180d":6160.0,"trough_date_180d":"2024-04-17","calibration_usable":true,"case_polarity":"positive_guarded_contained_mae","evidence_url_pending":true,"source_proxy_only":true,"non_price_evidence_strength":"medium_low_pending_url_repair","price_only_blowoff":false,"expected_stage_current_profile":"Stage2-Guarded_until_pf_refinancing_working_capital_bridge_repaired","residual_error_type":"contained_mae_contractor_path_but_yellow_green_requires_balance_sheet_repair_evidence"}
{"row_type":"trigger","research_id":"R10L74_C30_MIDSMALL_CONSTRUCTION_PF_ROUTER","round":"R10","loop":74,"large_sector_id":"L9_CONSTRUCTION_REALESTATE_HOUSING","canonical_archetype_id":"C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK","fine_archetype_id":"MIDSMALL_CONSTRUCTION_PF_RELIEF_SPIKE_AND_WEAK_MFE_SLOW_FADE_ROUTER","symbol":"001260","name":"남광토건","trigger_type":"Stage2-Actionable-Guarded","trigger_family":"regional_contractor_pf_relief_delayed_mfe_drawdown_watch","trigger_date":"2024-02-08","entry_date":"2024-02-13","entry_price":7290.0,"entry_price_type":"next_tradable_open_after_regional_contractor_relief","price_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","mfe_30d_pct":5.08,"mae_30d_pct":-9.47,"mfe_90d_pct":5.08,"mae_90d_pct":-17.42,"mfe_180d_pct":17.28,"mae_180d_pct":-17.42,"peak_price_180d":8550.0,"peak_date_180d":"2024-07-30","trough_price_180d":6020.0,"trough_date_180d":"2024-04-08","calibration_usable":true,"case_polarity":"counterexample_delayed_mfe_drawdown_watch","evidence_url_pending":true,"source_proxy_only":true,"non_price_evidence_strength":"low_pending_url_repair","price_only_blowoff":false,"expected_stage_current_profile":"Stage2-Guarded_or_local_4B_watch_until_pf_cashflow_bridge_repaired","residual_error_type":"regional_contractor_relief_had_weak_early_mfe_and_drawdown_before_delayed_recovery"}
{"row_type":"trigger","research_id":"R10L74_C30_MIDSMALL_CONSTRUCTION_PF_ROUTER","round":"R10","loop":74,"large_sector_id":"L9_CONSTRUCTION_REALESTATE_HOUSING","canonical_archetype_id":"C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK","fine_archetype_id":"MIDSMALL_CONSTRUCTION_PF_RELIEF_SPIKE_AND_WEAK_MFE_SLOW_FADE_ROUTER","symbol":"005960","name":"동부건설","trigger_type":"Stage2-FalsePositive-Candidate","trigger_family":"construction_pf_liquidity_weak_mfe_slow_fade","trigger_date":"2024-02-01","entry_date":"2024-02-02","entry_price":5370.0,"entry_price_type":"next_tradable_open_after_construction_pf_relief","price_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","mfe_30d_pct":2.42,"mae_30d_pct":-3.17,"mfe_90d_pct":2.42,"mae_90d_pct":-10.52,"mfe_180d_pct":2.42,"mae_180d_pct":-11.55,"peak_price_180d":5500.0,"peak_date_180d":"2024-02-19","trough_price_180d":4750.0,"trough_date_180d":"2024-06-13","calibration_usable":true,"case_polarity":"counterexample_weak_mfe_slow_fade","evidence_url_pending":true,"source_proxy_only":true,"non_price_evidence_strength":"low_pending_url_repair","price_only_blowoff":false,"expected_stage_current_profile":"blocked_Stage2_or_Stage2_Guarded_only_until_pf_liquidity_repair_evidence","residual_error_type":"weak_mfe_construction_pf_relief_path_should_not_green_without_liquidity_bridge"}
```

---

## 8. Score simulation and raw component breakdown

This is shadow-only and does not change production scoring.

| symbol | PF/liquidity repair | refinancing / maturity wall | working-capital quality | order/backlog quality | market mispricing | cash-flow / covenant bridge | information confidence | shadow total | intended route |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| `003070` | 10 | 8 | 7 | 8 | 14 | 6 | 5 | 58 | Stage2-Guarded; Yellow only after PF/cash-flow repair |
| `004960` | 9 | 8 | 7 | 8 | 8 | 6 | 5 | 51 | Stage2-Guarded until balance-sheet bridge repaired |
| `001260` | 5 | 4 | 4 | 5 | 7 | 3 | 4 | 32 | Stage2-Guarded or local 4B drawdown watch |
| `005960` | 3 | 3 | 3 | 4 | 3 | 2 | 4 | 22 | blocked Stage2 / weak-MFE slow fade |

### Current calibrated profile stress test

The current calibrated profile already blocks pure price-only blowoff.  
The remaining C30 issue is **construction relief without balance-sheet evidence**:

```text
C30 high-MFE but source-proxy path:
  construction/PF policy relief
  + strong MFE and survivable MAE
  + evidence still source_proxy_only
  => Stage2-Guarded; no Green until PF/cash-flow evidence repair

C30 contained-MAE repair path:
  low-PBR / contractor relief
  + 30D MAE is contained
  + 90D/180D drawdown remains below hard-failure zone
  => Stage2-Guarded, Yellow only after balance-sheet evidence repair

C30 weak-MFE slow fade:
  sector label exists
  + MFE_90D < +5%
  + no repaired liquidity/PF evidence
  => block Stage2 or keep local 4B watch
```

`003070` and `004960` prevent overblocking.  
`001260` shows that delayed MFE should not erase an early drawdown.  
`005960` shows that a construction PF candidate can fail quietly by never rerating.

---

## 9. Aggregate metrics

```json
{
  "row_type": "aggregate",
  "research_id": "R10L74_C30_MIDSMALL_CONSTRUCTION_PF_ROUTER",
  "round": "R10",
  "loop": 74,
  "large_sector_id": "L9_CONSTRUCTION_REALESTATE_HOUSING",
  "canonical_archetype_id": "C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK",
  "fine_archetype_id": "MIDSMALL_CONSTRUCTION_PF_RELIEF_SPIKE_AND_WEAK_MFE_SLOW_FADE_ROUTER",
  "case_count": 4,
  "calibration_usable_case_count": 4,
  "positive_guarded_case_count": 2,
  "counterexample_count": 2,
  "new_symbol_count": 4,
  "source_proxy_only_count": 4,
  "evidence_url_pending_count": 4,
  "avg_mfe_30d_pct": 22.46,
  "avg_mae_30d_pct": -4.64,
  "avg_mfe_90d_pct": 22.46,
  "avg_mae_90d_pct": -12.5,
  "avg_mfe_180d_pct": 25.51,
  "avg_mae_180d_pct": -12.76,
  "max_mfe_180d_pct": 71.38,
  "worst_mae_180d_pct": -17.42
}
```

---

## 10. 4B proximity split

```json
{
  "row_type": "4b_split",
  "research_id": "R10L74_C30_MIDSMALL_CONSTRUCTION_PF_ROUTER",
  "stage2_guarded_or_yellow_candidate": [
    {
      "symbol": "003070",
      "reason": "high +71.38% MFE with only -9.57% 180D MAE; requires PF/liquidity/cash-flow evidence before Green"
    },
    {
      "symbol": "004960",
      "reason": "contained 30D path and non-hard-failure 180D drawdown; requires refinancing and working-capital bridge repair"
    }
  ],
  "local_4b_watch": [
    {
      "symbol": "001260",
      "reason": "weak 30D/90D MFE with -17.42% MAE before delayed 180D recovery"
    }
  ],
  "blocked_stage2_or_weak_mfe_fade": [
    {
      "symbol": "005960",
      "reason": "MFE never exceeded +2.42%, while 90D/180D MAE widened into a slow-fade profile"
    }
  ],
  "full_4b_or_green_requires_non_price_evidence": [
    "PF guarantee exposure reduction",
    "refinancing / maturity wall repair",
    "receivables and working-capital repair",
    "unbilled construction revenue / cost-overrun control",
    "unsold inventory evidence",
    "cash-flow and covenant headroom"
  ]
}
```

---

## 11. Shadow rule candidate

```yaml
row_type: canonical_archetype_rule_candidate
canonical_archetype_id: C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK
fine_archetype_id: MIDSMALL_CONSTRUCTION_PF_RELIEF_SPIKE_AND_WEAK_MFE_SLOW_FADE_ROUTER
rule_name: C30_midsmall_pf_relief_spike_and_weak_mfe_slow_fade_router
production_scoring_changed: false
shadow_weight_only: true
```

### Proposed routing logic

```text
For C30 construction PF / balance-sheet repair cases:

Tier A: high-MFE construction relief holdout
  Conditions:
    - construction/PF policy or liquidity relief relevance is plausible
    - MFE_30D >= +40%
    - MAE_90D > -15%
    - evidence remains source_proxy_only
  Routing:
    - Stage2-Guarded allowed
    - no Green
    - Yellow only after PF/liquidity/cash-flow evidence repair

Tier B: contained-MAE low-PBR contractor repair
  Conditions:
    - MFE_30D >= +8%
    - MAE_30D > -5%
    - 180D MAE remains better than -20%
  Routing:
    - Stage2-Guarded allowed
    - no production positive weight until evidence repair

Tier C: weak-MFE slow-fade
  Conditions:
    - MFE_90D < +5%
    - evidence_url_pending or source_proxy_only remains true
    - PF/liquidity bridge is missing
  Routing:
    - block Stage2 or local 4B watch
    - count as weak-MFE counterexample
```

### Suggested shadow delta

```json
{
  "row_type": "shadow_weight",
  "axis": "c30_midsmall_pf_relief_spike_and_weak_mfe_slow_fade_router",
  "scope": "canonical_archetype_id:C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK",
  "proposal": {
    "source_proxy_only_green_allowed": false,
    "balance_sheet_liquidity_bridge_required_for_yellow_green": true,
    "high_mfe_relief_stage2_guarded_allowed": true,
    "high_mfe_relief_threshold_30d_pct": 40.0,
    "high_mfe_relief_mae90_min_pct": -15.0,
    "contained_mae_stage2_guarded_allowed": true,
    "weak_mfe_threshold_90d_pct": 5.0,
    "weak_mfe_pf_relief_blocks_green": true,
    "positive_weight_blocked_until_url_repair": true
  },
  "confidence": "medium_low_until_url_repair",
  "apply_now": false,
  "reason": "Two mid/small construction guarded positives and two weak-MFE or delayed-drawdown cases show that C30 should preserve real relief reratings while blocking quiet PF slow-fades without balance-sheet evidence."
}
```

---

## 12. Residual contribution summary

```json
{
  "row_type": "residual_contribution",
  "research_id": "R10L74_C30_MIDSMALL_CONSTRUCTION_PF_ROUTER",
  "large_sector_id": "L9_CONSTRUCTION_REALESTATE_HOUSING",
  "canonical_archetype_id": "C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK",
  "contribution": "Adds four non-top-covered C30 mid/small construction cases and separates high-MFE relief and contained-MAE low-PBR repair paths from weak-MFE PF slow-fade candidates. C30 Yellow/Green should require URL-repaired PF exposure, refinancing, maturity wall, receivables, working capital, inventory, cash-flow, and covenant evidence.",
  "positive_guarded_case_added": 2,
  "counterexample_case_added": 2,
  "new_symbol_count": 4,
  "data_quality_blocker": "All four non-price construction/PF triggers require URL-level repair before positive weight promotion.",
  "guardrail_added": "C30 source_proxy_only cases with MFE_90D < +5% should block Green and often Stage2; high-MFE relief cases may remain Stage2-Guarded only while PF/liquidity evidence is pending."
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
    003070: false
    004960: false
    001260: false
    005960: false
  evidence_url_pending:
    003070: true
    004960: true
    001260: true
    005960: true
  source_proxy_only:
    003070: true
    004960: true
    001260: true
    005960: true
```

Limitations:

```text
- Price path is validated against Stock-Web tradable OHLC rows.
- Non-price evidence is not URL-repaired in this run.
- Therefore this artifact is useful for C30 mid/small construction PF residual shape and weak-MFE slow-fade guardrail design, but should not promote positive weights until filings, credit reports, IR, or disclosures verify PF exposure, refinancing, receivables, working capital, cash-flow, and unsold-inventory repair.
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
2. Preserve R10 / loop 74 metadata.
3. Add the cases to C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK only if parser validation passes.
4. Treat all four non-price triggers as evidence_url_pending=true and source_proxy_only=true until URL-level evidence is repaired.
5. Do not use these rows for positive weight promotion until filings/IR/credit-report/disclosure data verifies PF exposure, refinancing, receivables, working capital, cash-flow, and unsold-inventory repair.
6. Add a shadow-only rule candidate named C30_midsmall_pf_relief_spike_and_weak_mfe_slow_fade_router.
7. Do not loosen Stage3-Green.
8. Add C30-specific guards:
   - source_proxy_only -> no Green
   - Stage3-Yellow/Green requires repaired balance-sheet and liquidity evidence
   - MFE_30D >= +40% and MAE_90D > -15% may remain Stage2-Guarded while evidence is pending
   - MFE_90D < +5% without PF/liquidity bridge -> block Green and often Stage2
   - weak-MFE slow-fade cases should route to local 4B watch or counterexample bucket
9. Keep production scoring unchanged unless later batch promotion logic independently marks this axis safe.
```

---

## 15. Next round state

```text
completed_round = R10
completed_loop = 74
next_round = R11
next_loop = 74
next_large_sector_hint = L10_POLICY_EVENT_CROSS_REDTEAM_MISC or L1 defense-linked policy event
round_schedule_status = valid
round_sector_consistency = pass
```
