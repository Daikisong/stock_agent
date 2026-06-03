# E2R Stock-Web v12 Residual Research — R10 Loop 76

```yaml
research_session: post_calibrated_sector_archetype_residual_research
mode: historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12
completed_round: R10
completed_loop: 76
next_round: R11
next_loop: 76
large_sector_id: L9_CONSTRUCTION_REALESTATE_HOUSING
canonical_archetype_id: C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK
fine_archetype_id: REGIONAL_HOUSING_HOLDCO_PF_RELIEF_LOW_MAE_AND_POLITICAL_SPIKE_HIGH_MAE_ROUTER
output_file: e2r_stock_web_v12_residual_round_R10_loop_76_L9_CONSTRUCTION_REALESTATE_HOUSING_C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK_research.md
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
completed_loop  = 76
large_sector_id = L3_BATTERY_EV_GREEN_MOBILITY
canonical_archetype_id = C11_BATTERY_ORDERBOOK_RERATING
```

Therefore:

```text
scheduled_round = R10
scheduled_loop  = 76
```

R10 maps to:

```text
large_sector_id = L9_CONSTRUCTION_REALESTATE_HOUSING
```

This run selects:

```text
canonical_archetype_id = C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK
fine_archetype_id = REGIONAL_HOUSING_HOLDCO_PF_RELIEF_LOW_MAE_AND_POLITICAL_SPIKE_HIGH_MAE_ROUTER
```

This is a valid R10/L9 pairing.

---

## 1. Why this R10/C30 run

The no-repeat ledger shows C30 is broad, noisy, and PF/balance-sheet stress-heavy:

```text
C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK:
  rows: 159
  symbols: 29
  date_range: 2021-03-11~2024-09-30
  good/bad S2: 15/21
  4B/4C: 29/29
  URL/proxy: 42/42
  top covered symbols: 047040(15), 006360(13), UNKNOWN_SYMBOL(13), 294870(12), 005960(9), 000720(8)
```

This file avoids those top-covered C30 names and also avoids the previous loop-75 C30 symbols:

```text
013580 계룡건설
014790 HL D&I
013360 일성건설
002410 범양건영
```

Selected new symbols:

```text
012630 HDC
035890 서희건설
001470 삼부토건
002780 진흥기업
```

Research question:

```text
Can C30 separate low-MAE housing/PF relief rerating from construction labels that are really political/policy spikes or quiet PF slow fades?
```

C30 is a balance-sheet bridge archetype. A construction rally can look like a fresh coat of paint on a cracked wall. The model has to tap the concrete: PF exposure, refinancing, receivables, unsold inventory, project margin, cash conversion, covenant headroom, and working-capital repair. Without that, a policy candle is not a repaired building.

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
| `012630` | HDC | active_like / KOSPI | no 2024 overlap; latest listed candidate 2018-10-11 | true |
| `035890` | 서희건설 | active_like / KOSDAQ | no 2024 overlap; latest listed candidate 2012-07-12 | true |
| `001470` | 삼부토건 | active_like / KOSPI history | no 2024 overlap; latest listed candidate 2019-05-02 | true for selected 180D |
| `002780` | 진흥기업 | active_like / KOSPI | no 2024 overlap; latest listed candidate 2015-01-28 | true |

Profile caveat:

```text
Stock-Web OHLC is raw/unadjusted marcap data.
These cases are calibration-safe for the selected 2024 30D/90D/180D windows because no listed corporate-action candidate overlaps each entry~D+180 test window.
For 001470, later listing/trading-history complications are outside the selected 2024 180D window used here.
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
The Stock-Web price path is fully validated, but company-level PF guarantee exposure, refinancing, receivables, unbilled construction revenue, unsold inventory, project margin, working-capital repair, cash-flow conversion, and covenant/liquidity headroom evidence still require later URL repair through filings, credit reports, IR decks, project disclosures, or sell-side reports before production weight promotion.
```

C30 interpretation used here:

```text
C30 is not simply “construction stock rose.”
It asks whether PF/balance-sheet stress is genuinely repaired:
- PF guarantee / contingent-liability exposure,
- refinancing and maturity-wall control,
- receivables and working-capital quality,
- unbilled construction revenue / cost-overrun control,
- unsold inventory,
- project margin and cash-flow repair,
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
012630 + C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK -> no direct match found
035890 + C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK -> no direct match found
001470 + C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK -> no direct match found
002780 + C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK -> no direct match found
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
| `R10L76_C30_012630_20240129` | `012630` HDC | housing holdco low-PBR/PF relief with low MAE | positive-guarded anchor |
| `R10L76_C30_035890_20240129` | `035890` 서희건설 | regional housing PF relief with contained MAE | positive-guarded slow-MFE |
| `R10L76_C30_001470_20240214` | `001470` 삼부토건 | small contractor political/reconstruction spike | high-MAE counterexample |
| `R10L76_C30_002780_20240227` | `002780` 진흥기업 | regional contractor PF relief weak-MFE slow fade | weak-MFE counterexample |

The intended residual:

```text
C30 should separate:
1. low-MAE housing/PF recovery routes that can remain Stage2-Guarded;
2. slow regional-contractor paths that preserve capital but lack enough MFE for Green;
3. political/policy construction spikes where MAE overwhelms the initial signal;
4. quiet regional-contractor slow fades where Stage2 fails because MFE never appears.
```

---

## 6. Stock-Web OHLC and backtest

### 6.1 `012630` HDC — housing holdco low-PBR / PF relief low-MAE rerating

Trigger:

```text
trigger_date = 2024-01-26
trigger_type = Stage2-Actionable-Guarded
trigger_family = housing_holdco_low_pbr_pf_relief_project_margin_low_mae_rerating
entry_date = 2024-01-29
entry_price = 6880.0
entry_price_type = next_tradable_open_after_housing_pf_low_pbr_relief_burst
```

Relevant Stock-Web rows:

```csv
d,o,h,l,c,v,a,mc,s,m
2024-01-26,6600.0,6830.0,6600.0,6830.0,134560.0,908541750.0,408035954430.0,59741721,KOSPI
2024-01-29,6880.0,7210.0,6770.0,7170.0,272079.0,1919873380.0,428348139570.0,59741721,KOSPI
2024-02-07,8650.0,8820.0,8410.0,8810.0,458707.0,3972111550.0,526324562010.0,59741721,KOSPI
2024-03-13,7800.0,7880.0,7620.0,7840.0,126827.0,981202850.0,468375092640.0,59741721,KOSPI
2024-07-26,8820.0,9710.0,8820.0,9650.0,835390.0,7899624570.0,576507607650.0,59741721,KOSPI
2024-08-05,9650.0,9800.0,8900.0,9280.0,621155.0,5789571020.0,554403170880.0,59741721,KOSPI
```

Backtest:

| window | peak/high | peak date | trough/low | trough date | MFE | MAE |
|---|---:|---|---:|---|---:|---:|
| 30 calendar days | 8820 | 2024-02-07 | 6770 | 2024-01-29 | +28.20% | -1.60% |
| 90 calendar days | 8820 | 2024-02-07 | 6770 | 2024-01-29 | +28.20% | -1.60% |
| 180 calendar days | 9710 | 2024-07-26 | 6770 | 2024-01-29 | +41.13% | -1.60% |

Interpretation:

```text
012630 is the C30 positive-guarded anchor in this run.
The housing holdco / PF relief path had persistent MFE and very low MAE.
It can support Stage2-Guarded / Yellow-after-repair, but Green still requires URL-repaired PF exposure, refinancing, project margin, working-capital, and cash-flow evidence.
```

### 6.2 `035890` 서희건설 — regional housing PF relief with contained MAE

Trigger:

```text
trigger_date = 2024-01-26
trigger_type = Stage2-Actionable-Guarded
trigger_family = regional_housing_pf_relief_contained_mae_slow_rerating
entry_date = 2024-01-29
entry_price = 1233.0
entry_price_type = next_tradable_open_after_regional_housing_pf_relief_burst
```

Relevant Stock-Web rows:

```csv
d,o,h,l,c,v,a,mc,s,m
2024-01-26,1223.0,1240.0,1217.0,1233.0,114349.0,140750418.0,283353827481.0,229808457,KOSDAQ
2024-01-29,1233.0,1260.0,1233.0,1259.0,265697.0,331568866.0,289328847363.0,229808457,KOSDAQ
2024-02-02,1305.0,1317.0,1295.0,1304.0,316587.0,412468995.0,299670227928.0,229808457,KOSDAQ
2024-02-27,1267.0,1267.0,1230.0,1235.0,190120.0,235616951.0,283813444395.0,229808457,KOSDAQ
2024-04-09,1366.0,1378.0,1366.0,1370.0,365291.0,500775902.0,314837586090.0,229808457,KOSDAQ
2024-08-05,1315.0,1318.0,1190.0,1227.0,375086.0,467526179.0,281974976739.0,229808457,KOSDAQ
```

Backtest:

| window | peak/high | peak date | trough/low | trough date | MFE | MAE |
|---|---:|---|---:|---|---:|---:|
| 30 calendar days | 1317 | 2024-02-02 | 1230 | 2024-02-27 | +6.81% | -0.24% |
| 90 calendar days | 1378 | 2024-04-09 | 1230 | 2024-02-27 | +11.76% | -0.24% |
| 180 calendar days | 1378 | 2024-04-09 | 1230 | 2024-02-27 | +11.76% | -0.24% |

Interpretation:

```text
035890 is a slow-MFE but low-MAE C30 holdout.
It should not be treated as Green-quality, but it also should not be forced into 4B.
The correct route is Stage2-Guarded only until regional PF/refinancing, project margin, and cash-flow evidence is repaired.
```

### 6.3 `001470` 삼부토건 — political/reconstruction construction spike with high MAE

Trigger:

```text
trigger_date = 2024-02-13
trigger_type = Stage2-FalsePositive-Candidate
trigger_family = small_contractor_political_reconstruction_pf_spike_high_mae
entry_date = 2024-02-14
entry_price = 2585.0
entry_price_type = next_tradable_open_after_small_contractor_policy_political_spike
```

Relevant Stock-Web rows:

```csv
d,o,h,l,c,v,a,mc,s,m
2024-02-13,2155.0,2630.0,2100.0,2585.0,71228864.0,176867053360.0,528010171590.0,204259254,KOSPI
2024-02-14,2585.0,2690.0,2410.0,2570.0,36708335.0,93719951850.0,524946282780.0,204259254,KOSPI
2024-03-13,2230.0,2650.0,2210.0,2400.0,30313060.0,75168457415.0,490222209600.0,204259254,KOSPI
2024-03-15,2565.0,2865.0,2430.0,2690.0,77629103.0,208864960205.0,549457393260.0,204259254,KOSPI
2024-04-08,1670.0,1836.0,1510.0,1540.0,27138794.0,43821880838.0,314559251160.0,204259254,KOSPI
2024-08-08,1162.0,1162.0,997.0,1014.0,24310605.0,25809434098.0,226742389536.0,223611824,KOSPI
```

Backtest:

| window | peak/high | peak date | trough/low | trough date | MFE | MAE |
|---|---:|---|---:|---|---:|---:|
| 30 calendar days | 2865 | 2024-03-15 | 2210 | 2024-03-13 | +10.83% | -14.51% |
| 90 calendar days | 2865 | 2024-03-15 | 1510 | 2024-04-08 | +10.83% | -41.59% |
| 180 calendar days | 2865 | 2024-03-15 | 997 | 2024-08-08 | +10.83% | -61.43% |

Interpretation:

```text
001470 is the high-MAE C30 counterexample.
The construction/policy/political label produced a short-lived window, but the entry rapidly became a severe drawdown path.
This should block Stage2 or route to 4B/4C high-MAE watch unless a later independent trigger repairs balance-sheet, liquidity, project, and cash-flow evidence.
```

### 6.4 `002780` 진흥기업 — regional contractor PF relief weak-MFE slow fade

Trigger:

```text
trigger_date = 2024-02-26
trigger_type = Stage2-FalsePositive-Candidate
trigger_family = regional_contractor_pf_relief_weak_mfe_slow_fade
entry_date = 2024-02-27
entry_price = 1053.0
entry_price_type = next_tradable_open_after_regional_contractor_pf_relief_spike
```

Relevant Stock-Web rows:

```csv
d,o,h,l,c,v,a,mc,s,m
2024-02-26,1062.0,1149.0,1050.0,1063.0,2183885.0,2391585629.0,154636464935.0,145471745,KOSPI
2024-02-27,1053.0,1058.0,1033.0,1037.0,417739.0,436858853.0,150854199565.0,145471745,KOSPI
2024-03-20,1005.0,1010.0,949.0,1005.0,296058.0,295489227.0,146199103725.0,145471745,KOSPI
2024-05-27,943.0,943.0,930.0,933.0,282197.0,263646377.0,135725138085.0,145471745,KOSPI
2024-08-05,890.0,893.0,797.0,820.0,1217575.0,1027442773.0,119286830900.0,145471745,KOSPI
2024-08-06,796.0,848.0,795.0,827.0,507225.0,417381675.0,120305133115.0,145471745,KOSPI
```

Backtest:

| window | peak/high | peak date | trough/low | trough date | MFE | MAE |
|---|---:|---|---:|---|---:|---:|
| 30 calendar days | 1058 | 2024-02-27 | 949 | 2024-03-20 | +0.47% | -9.88% |
| 90 calendar days | 1058 | 2024-02-27 | 930 | 2024-05-27 | +0.47% | -11.68% |
| 180 calendar days | 1058 | 2024-02-27 | 795 | 2024-08-06 | +0.47% | -24.50% |

Interpretation:

```text
002780 is the quiet slow-fade C30 counterexample.
It did not need a single dramatic event collapse; it simply never delivered MFE while MAE widened.
This is the C30 failure mode where PF relief relevance exists, but no balance-sheet/cash-flow repair bridge reaches the stock path.
```

---

## 7. Machine-readable trigger JSONL

```jsonl
{"row_type":"trigger","research_id":"R10L76_C30_REGIONAL_HOUSING_PF_ROUTER","round":"R10","loop":76,"large_sector_id":"L9_CONSTRUCTION_REALESTATE_HOUSING","canonical_archetype_id":"C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK","fine_archetype_id":"REGIONAL_HOUSING_HOLDCO_PF_RELIEF_LOW_MAE_AND_POLITICAL_SPIKE_HIGH_MAE_ROUTER","symbol":"012630","name":"HDC","trigger_type":"Stage2-Actionable-Guarded","trigger_family":"housing_holdco_low_pbr_pf_relief_project_margin_low_mae_rerating","trigger_date":"2024-01-26","entry_date":"2024-01-29","entry_price":6880.0,"entry_price_type":"next_tradable_open_after_housing_pf_low_pbr_relief_burst","price_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","mfe_30d_pct":28.2,"mae_30d_pct":-1.6,"mfe_90d_pct":28.2,"mae_90d_pct":-1.6,"mfe_180d_pct":41.13,"mae_180d_pct":-1.6,"peak_price_180d":9710.0,"peak_date_180d":"2024-07-26","trough_price_180d":6770.0,"trough_date_180d":"2024-01-29","calibration_usable":true,"case_polarity":"positive_guarded_low_mae_housing_holdco","evidence_url_pending":true,"source_proxy_only":true,"non_price_evidence_strength":"medium_low_pending_url_repair","price_only_blowoff":false,"expected_stage_current_profile":"Stage2-Guarded_to_Yellow_if_pf_liquidity_project_margin_cashflow_bridge_repaired","residual_error_type":"housing_holdco_low_pbr_pf_relief_path_had_low_mae_mfe_but_green_requires_url_repaired_balance_sheet_project_margin_bridge"}
{"row_type":"trigger","research_id":"R10L76_C30_REGIONAL_HOUSING_PF_ROUTER","round":"R10","loop":76,"large_sector_id":"L9_CONSTRUCTION_REALESTATE_HOUSING","canonical_archetype_id":"C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK","fine_archetype_id":"REGIONAL_HOUSING_HOLDCO_PF_RELIEF_LOW_MAE_AND_POLITICAL_SPIKE_HIGH_MAE_ROUTER","symbol":"035890","name":"서희건설","trigger_type":"Stage2-Actionable-Guarded","trigger_family":"regional_housing_pf_relief_contained_mae_slow_rerating","trigger_date":"2024-01-26","entry_date":"2024-01-29","entry_price":1233.0,"entry_price_type":"next_tradable_open_after_regional_housing_pf_relief_burst","price_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","mfe_30d_pct":6.81,"mae_30d_pct":-0.24,"mfe_90d_pct":11.76,"mae_90d_pct":-0.24,"mfe_180d_pct":11.76,"mae_180d_pct":-0.24,"peak_price_180d":1378.0,"peak_date_180d":"2024-04-09","trough_price_180d":1230.0,"trough_date_180d":"2024-02-27","calibration_usable":true,"case_polarity":"positive_guarded_slow_low_mae","evidence_url_pending":true,"source_proxy_only":true,"non_price_evidence_strength":"medium_low_pending_url_repair","price_only_blowoff":false,"expected_stage_current_profile":"Stage2-Guarded_only_until_pf_refinancing_working_capital_cashflow_bridge_repaired","residual_error_type":"regional_housing_pf_relief_path_preserved_mae_but_mfe_was_modest_without_repaired_project_cashflow_bridge"}
{"row_type":"trigger","research_id":"R10L76_C30_REGIONAL_HOUSING_PF_ROUTER","round":"R10","loop":76,"large_sector_id":"L9_CONSTRUCTION_REALESTATE_HOUSING","canonical_archetype_id":"C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK","fine_archetype_id":"REGIONAL_HOUSING_HOLDCO_PF_RELIEF_LOW_MAE_AND_POLITICAL_SPIKE_HIGH_MAE_ROUTER","symbol":"001470","name":"삼부토건","trigger_type":"Stage2-FalsePositive-Candidate","trigger_family":"small_contractor_political_reconstruction_pf_spike_high_mae","trigger_date":"2024-02-13","entry_date":"2024-02-14","entry_price":2585.0,"entry_price_type":"next_tradable_open_after_small_contractor_policy_political_spike","price_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","mfe_30d_pct":10.83,"mae_30d_pct":-14.51,"mfe_90d_pct":10.83,"mae_90d_pct":-41.59,"mfe_180d_pct":10.83,"mae_180d_pct":-61.43,"peak_price_180d":2865.0,"peak_date_180d":"2024-03-15","trough_price_180d":997.0,"trough_date_180d":"2024-08-08","calibration_usable":true,"case_polarity":"counterexample_policy_political_spike_high_mae","evidence_url_pending":true,"source_proxy_only":true,"non_price_evidence_strength":"low_pending_url_repair","price_only_blowoff":true,"expected_stage_current_profile":"blocked_Stage2_or_4B_4C_high_MAE_watch","residual_error_type":"small_contractor_policy_political_spike_had_limited_mfe_and_extreme_mae_without_pf_liquidity_cashflow_bridge"}
{"row_type":"trigger","research_id":"R10L76_C30_REGIONAL_HOUSING_PF_ROUTER","round":"R10","loop":76,"large_sector_id":"L9_CONSTRUCTION_REALESTATE_HOUSING","canonical_archetype_id":"C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK","fine_archetype_id":"REGIONAL_HOUSING_HOLDCO_PF_RELIEF_LOW_MAE_AND_POLITICAL_SPIKE_HIGH_MAE_ROUTER","symbol":"002780","name":"진흥기업","trigger_type":"Stage2-FalsePositive-Candidate","trigger_family":"regional_contractor_pf_relief_weak_mfe_slow_fade","trigger_date":"2024-02-26","entry_date":"2024-02-27","entry_price":1053.0,"entry_price_type":"next_tradable_open_after_regional_contractor_pf_relief_spike","price_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","mfe_30d_pct":0.47,"mae_30d_pct":-9.88,"mfe_90d_pct":0.47,"mae_90d_pct":-11.68,"mfe_180d_pct":0.47,"mae_180d_pct":-24.5,"peak_price_180d":1058.0,"peak_date_180d":"2024-02-27","trough_price_180d":795.0,"trough_date_180d":"2024-08-06","calibration_usable":true,"case_polarity":"counterexample_weak_mfe_slow_fade","evidence_url_pending":true,"source_proxy_only":true,"non_price_evidence_strength":"low_pending_url_repair","price_only_blowoff":false,"expected_stage_current_profile":"blocked_Stage2_or_local_4B_watch_until_pf_liquidity_project_margin_bridge_repaired","residual_error_type":"regional_contractor_pf_relief_label_had_almost_no_mfe_and_later_mae_without_balance_sheet_cashflow_bridge"}
```

---

## 8. Score simulation and raw component breakdown

This is shadow-only and does not change production scoring.

| symbol | PF/liquidity repair | refinancing / maturity wall | working-capital quality | project/order margin | market mispricing | cash-flow / covenant bridge | information confidence | shadow total | intended route |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| `012630` | 10 | 9 | 8 | 9 | 12 | 8 | 5 | 61 | Stage2-Guarded / Yellow after evidence repair |
| `035890` | 8 | 7 | 7 | 7 | 5 | 6 | 5 | 45 | Stage2-Guarded only until evidence repair |
| `001470` | 3 | 2 | 2 | 3 | 4 | 1 | 4 | 19 | blocked Stage2 / 4B-4C high-MAE watch |
| `002780` | 3 | 3 | 3 | 3 | 1 | 2 | 4 | 19 | blocked Stage2 / weak-MFE slow-fade watch |

### Current calibrated profile stress test

The current calibrated profile already blocks pure price-only blowoff.  
The remaining C30 issue is **construction/PF label without balance-sheet repair evidence**:

```text
C30 low-MAE housing/PF recovery path:
  low-PBR / PF relief relevance
  + MFE_90D >= +10%
  + MAE_90D > -8%
  + evidence remains source_proxy_only
  => Stage2-Guarded; Yellow only after PF/refinancing/cash-flow evidence repair

C30 slow-MFE regional path:
  MAE stays controlled
  + MFE is modest
  + evidence remains source_proxy_only
  => Stage2-Guarded at most, no Green

C30 political/policy spike failure:
  policy or reconstruction label drives volume
  + MAE_90D <= -35%
  + no project/PF/cash-flow bridge
  => block Stage2 or 4B/4C high-MAE watch

C30 quiet slow fade:
  MFE_90D < +5%
  + MAE_180D <= -20%
  + no liquidity bridge
  => block Stage2 even without a single dramatic 4C candle
```

`012630` and `035890` prevent overblocking.  
`001470` shows why policy/political construction spikes need a hard high-MAE guard.  
`002780` adds the quiet failure mode: no MFE, steady PF/balance-sheet discount.

---

## 9. Aggregate metrics

```json
{
  "row_type": "aggregate",
  "research_id": "R10L76_C30_REGIONAL_HOUSING_PF_ROUTER",
  "round": "R10",
  "loop": 76,
  "large_sector_id": "L9_CONSTRUCTION_REALESTATE_HOUSING",
  "canonical_archetype_id": "C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK",
  "fine_archetype_id": "REGIONAL_HOUSING_HOLDCO_PF_RELIEF_LOW_MAE_AND_POLITICAL_SPIKE_HIGH_MAE_ROUTER",
  "case_count": 4,
  "calibration_usable_case_count": 4,
  "positive_guarded_case_count": 2,
  "counterexample_count": 2,
  "new_symbol_count": 4,
  "source_proxy_only_count": 4,
  "evidence_url_pending_count": 4,
  "avg_mfe_30d_pct": 11.58,
  "avg_mae_30d_pct": -6.56,
  "avg_mfe_90d_pct": 12.82,
  "avg_mae_90d_pct": -13.78,
  "avg_mfe_180d_pct": 16.05,
  "avg_mae_180d_pct": -21.94,
  "max_mfe_180d_pct": 41.13,
  "worst_mae_180d_pct": -61.43
}
```

---

## 10. 4B proximity split

```json
{
  "row_type": "4b_split",
  "research_id": "R10L76_C30_REGIONAL_HOUSING_PF_ROUTER",
  "stage2_guarded_or_yellow_candidate": [
    {
      "symbol": "012630",
      "reason": "housing/PF relief path had +41.13% 180D MFE with only -1.60% MAE"
    },
    {
      "symbol": "035890",
      "reason": "regional housing path preserved MAE, but MFE was modest; Stage2-Guarded only"
    }
  ],
  "blocked_stage2_or_4c_watch": [
    {
      "symbol": "001470",
      "reason": "policy/political construction spike had only +10.83% MFE and -61.43% 180D MAE"
    },
    {
      "symbol": "002780",
      "reason": "PF relief label had only +0.47% MFE and -24.50% 180D MAE"
    }
  ],
  "full_4b_or_green_requires_non_price_evidence": [
    "PF guarantee exposure reduction",
    "refinancing / maturity-wall repair",
    "receivables and working-capital quality",
    "unbilled construction revenue / cost-overrun control",
    "unsold inventory evidence",
    "project margin and cash-flow conversion",
    "covenant and liquidity headroom"
  ]
}
```

---

## 11. Shadow rule candidate

```yaml
row_type: canonical_archetype_rule_candidate
canonical_archetype_id: C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK
fine_archetype_id: REGIONAL_HOUSING_HOLDCO_PF_RELIEF_LOW_MAE_AND_POLITICAL_SPIKE_HIGH_MAE_ROUTER
rule_name: C30_regional_housing_pf_relief_low_mae_and_political_spike_high_mae_router
production_scoring_changed: false
shadow_weight_only: true
```

### Proposed routing logic

```text
For C30 housing holdco / regional contractor / small-contractor PF relief cases:

Tier A: low-MAE PF relief candidate
  Conditions:
    - PF/liquidity relief or low-PBR housing repair relevance is plausible
    - MFE_90D >= +10%
    - MAE_90D > -8%
    - evidence remains source_proxy_only
  Routing:
    - Stage2-Guarded allowed
    - Stage3-Yellow only after URL-repaired PF/refinancing/working-capital/cash-flow bridge
    - no Green while evidence is pending

Tier B: slow-MFE regional contractor
  Conditions:
    - MFE_180D >= +10%
    - MAE_180D > -8%
    - evidence remains source_proxy_only
  Routing:
    - Stage2-Guarded only
    - no Yellow/Green without balance-sheet repair evidence

Tier C: political / reconstruction / policy spike failure
  Conditions:
    - construction label is policy/political/event-heavy
    - MAE_90D <= -35% or MAE_180D <= -50%
    - no repaired project/PF/cash-flow bridge
  Routing:
    - block Stage2
    - route to 4B/4C high-MAE watch

Tier D: quiet PF slow fade
  Conditions:
    - MFE_90D < +5%
    - MAE_180D <= -20%
    - no repaired liquidity/balance-sheet bridge
  Routing:
    - block Stage2 or local 4B watch
    - count as counterexample
```

### Suggested shadow delta

```json
{
  "row_type": "shadow_weight",
  "axis": "c30_regional_housing_pf_relief_low_mae_and_political_spike_high_mae_router",
  "scope": "canonical_archetype_id:C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK",
  "proposal": {
    "source_proxy_only_green_allowed": false,
    "balance_sheet_liquidity_cashflow_bridge_required_for_yellow_green": true,
    "low_mae_pf_mfe90_threshold_pct": 10.0,
    "low_mae_pf_mae90_min_pct": -8.0,
    "slow_mfe_stage2_guarded_mfe180_threshold_pct": 10.0,
    "slow_mfe_stage2_guarded_mae180_min_pct": -8.0,
    "political_spike_mae90_threshold_pct": -35.0,
    "political_spike_mae180_threshold_pct": -50.0,
    "quiet_slow_fade_mfe90_threshold_pct": 5.0,
    "quiet_slow_fade_mae180_threshold_pct": -20.0,
    "positive_weight_blocked_until_url_repair": true
  },
  "confidence": "medium_low_until_url_repair",
  "apply_now": false,
  "reason": "Two non-top-covered low-MAE housing/regional PF holdouts and two high-MAE or weak-MFE construction failures show that C30 should require URL-repaired PF, refinancing, working-capital, project-margin, and cash-flow evidence before Yellow/Green."
}
```

---

## 12. Residual contribution summary

```json
{
  "row_type": "residual_contribution",
  "research_id": "R10L76_C30_REGIONAL_HOUSING_PF_ROUTER",
  "large_sector_id": "L9_CONSTRUCTION_REALESTATE_HOUSING",
  "canonical_archetype_id": "C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK",
  "contribution": "Adds four non-top-covered C30 housing holdco / regional construction / small-contractor PF relief cases and separates low-MAE housing/PF recovery from political construction spike and quiet PF slow-fade failures. C30 Yellow/Green should require URL-repaired PF exposure, refinancing, working capital, project margin, cash flow, covenant, and liquidity evidence.",
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
  "data_quality_blocker": "All four non-price construction/PF triggers require URL-level repair before positive weight promotion.",
  "guardrail_added": "C30 source_proxy_only political/policy construction spikes with MAE_90D <= -35% should block Stage2; quiet slow-fade cases with MFE_90D < +5% and MAE_180D <= -20% should block Stage2 or route to local 4B watch."
}
```

One-line contribution:

```text
This loop adds 4 new independent cases, 2 counterexamples, and 2 residual errors for R10/L9_CONSTRUCTION_REALESTATE_HOUSING/C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK.
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
    012630: false
    035890: false
    001470: false
    002780: false
  evidence_url_pending:
    012630: true
    035890: true
    001470: true
    002780: true
  source_proxy_only:
    012630: true
    035890: true
    001470: true
    002780: true
```

Limitations:

```text
- Price path is validated against Stock-Web tradable OHLC rows.
- Non-price evidence is not URL-repaired in this run.
- Therefore this artifact is useful for C30 housing/PF residual shape and weak-MFE/high-MAE guardrail design, but should not promote positive weights until filings, credit reports, IR, project disclosures, or reports verify PF exposure, refinancing, receivables, working capital, unsold inventory, project margin, cash-flow conversion, and covenant/liquidity headroom.
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
2. Preserve R10 / loop 76 metadata.
3. Add the cases to C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK only if parser validation passes.
4. Treat all four non-price triggers as evidence_url_pending=true and source_proxy_only=true until URL-level evidence is repaired.
5. Do not use these rows for positive weight promotion until filings/credit-report/IR/project-disclosure/report data verifies PF exposure, refinancing, receivables, working capital, unsold inventory, project margin, cash-flow conversion, and covenant/liquidity headroom.
6. Add a shadow-only rule candidate named C30_regional_housing_pf_relief_low_mae_and_political_spike_high_mae_router.
7. Do not loosen Stage3-Green.
8. Add C30-specific guards:
   - source_proxy_only -> no Green
   - Stage3-Yellow/Green requires repaired PF / refinancing / working-capital / cash-flow bridge
   - MFE_90D >= +10% and MAE_90D > -8% may remain Stage2-Guarded until evidence repair
   - MFE_180D >= +10% and MAE_180D > -8% may remain Stage2-Guarded only
   - policy/political construction spikes with MAE_90D <= -35% or MAE_180D <= -50% -> block Stage2 / 4B-4C watch
   - MFE_90D < +5% and MAE_180D <= -20% -> block Stage2 or local 4B watch
9. Keep production scoring unchanged unless later batch promotion logic independently marks this axis safe.
```

---

## 15. Next round state

```text
completed_round = R10
completed_loop = 76
next_round = R11
next_loop = 76
next_large_sector_hint = L10_POLICY_EVENT_CROSS_REDTEAM_MISC or L1 defense-linked policy event
round_schedule_status = valid
round_sector_consistency = pass
```
