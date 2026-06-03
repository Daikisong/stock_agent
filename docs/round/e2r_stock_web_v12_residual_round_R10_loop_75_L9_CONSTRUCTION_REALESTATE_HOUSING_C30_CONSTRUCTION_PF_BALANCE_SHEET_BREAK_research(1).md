# E2R Stock-Web v12 Residual Research — R10 Loop 75

```yaml
research_session: post_calibrated_sector_archetype_residual_research
mode: historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12
completed_round: R10
completed_loop: 75
next_round: R11
next_loop: 75
large_sector_id: L9_CONSTRUCTION_REALESTATE_HOUSING
canonical_archetype_id: C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK
fine_archetype_id: REGIONAL_CONTRACTOR_LOW_PBR_PF_REPAIR_AND_WEAK_MFE_HIGH_MAE_ROUTER
output_file: e2r_stock_web_v12_residual_round_R10_loop_75_L9_CONSTRUCTION_REALESTATE_HOUSING_C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK_research.md
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
completed_loop  = 75
large_sector_id = L3_BATTERY_EV_GREEN_MOBILITY
canonical_archetype_id = C13_BATTERY_JV_UTILIZATION_AMPC_IRA
```

Therefore:

```text
scheduled_round = R10
scheduled_loop  = 75
```

R10 maps to:

```text
large_sector_id = L9_CONSTRUCTION_REALESTATE_HOUSING
```

This run selects:

```text
canonical_archetype_id = C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK
fine_archetype_id = REGIONAL_CONTRACTOR_LOW_PBR_PF_REPAIR_AND_WEAK_MFE_HIGH_MAE_ROUTER
```

This is a valid R10/L9 pairing.

---

## 1. Why this R10/C30 run

The no-repeat ledger shows C30 is heavily covered and noisy, with the most repeated symbols concentrated in large contractors / already-stressed PF names:

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

This file avoids those top-covered symbols and also avoids the prior loop-74 C30 names:

```text
003070 코오롱글로벌
004960 한신공영
001260 남광토건
005960 동부건설
```

Selected new symbols:

```text
013580 계룡건설
014790 HL D&I
013360 일성건설
002410 범양건영
```

Research question:

```text
Can C30 separate real low-PBR / PF-repair contractor rerating from small-contractor relief labels where the forward path has weak MFE, early high MAE, or slow-fade drawdown before balance-sheet repair evidence is URL-repaired?
```

C30 is a balance-sheet bridge archetype. In construction, a stock can rise on policy relief the way a cracked wall can look stable after paint. The model has to inspect the rebar: PF guarantees, refinancing, receivables, unbilled revenue, unsold inventory, working capital, cash-flow repair, and covenant headroom. Without that, a relief rally is just fresh paint over stress.

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
| `013580` | 계룡건설 | active_like / KOSPI | no 2024 overlap; latest listed candidate 1999-07-16 | true |
| `014790` | HL D&I | active_like / KOSPI | no 2024 overlap; latest listed candidate 2012-02-06 | true |
| `013360` | 일성건설 | active_like / KOSPI | no 2024 overlap; latest listed candidate 2017-05-18 | true |
| `002410` | 범양건영 | active_like / KOSPI | no 2024 overlap; latest listed candidate 2017-12-06 | true |

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
The Stock-Web price path is fully validated, but company-level PF guarantee exposure, maturity-wall refinancing, receivables, unbilled construction revenue, unsold inventory, project margin, working-capital repair, cash-flow conversion, and covenant/liquidity headroom evidence still require later URL repair through filings, credit reports, IR decks, project disclosures, or sell-side reports before production weight promotion.
```

C30 interpretation used here:

```text
C30 is not simply “small construction stock bounced.”
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
013580 + C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK -> no direct match found
014790 + C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK -> no direct match found
013360 + C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK -> no direct match found
002410 + C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK -> no direct match found
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
| `R10L75_C30_013580_20240129` | `013580` 계룡건설 | regional contractor low-PBR/PF repair contained-MAE path | positive-guarded |
| `R10L75_C30_014790_20240604` | `014790` HL D&I | mid/small contractor PF-policy relief high-MFE / low-MAE path | positive-guarded |
| `R10L75_C30_013360_20240411` | `013360` 일성건설 | small contractor policy/event spike with early high MAE | early high-MAE counterexample |
| `R10L75_C30_002410_20240202` | `002410` 범양건영 | small contractor low-PBR/PF relief weak-MFE slow fade | weak-MFE high-MAE counterexample |

The intended residual:

```text
C30 should separate:
1. low-MAE contractor repair paths that can remain Stage2-Guarded;
2. high-MFE policy-relief paths that should not be overblocked;
3. event-spike paths where early MAE arrives before delayed MFE;
4. quiet PF slow fades where MFE never materializes.
```

---

## 6. Stock-Web OHLC and backtest

### 6.1 `013580` 계룡건설 — regional contractor low-PBR / PF repair contained-MAE path

Trigger:

```text
trigger_date = 2024-01-26
trigger_type = Stage2-Actionable-Guarded
trigger_family = regional_contractor_low_pbr_pf_repair_contained_mae
entry_date = 2024-01-29
entry_price = 13530.0
entry_price_type = next_tradable_open_after_low_pbr_construction_pf_repair
```

Relevant Stock-Web rows:

```csv
d,o,h,l,c,v,a,mc,s,m
2024-01-26,13370.0,13680.0,13350.0,13650.0,12069.0,163713570.0,121906880550.0,8930907,KOSPI
2024-01-29,13530.0,14110.0,13390.0,14080.0,24362.0,336589530.0,125747170560.0,8930907,KOSPI
2024-02-19,15190.0,15430.0,15110.0,15330.0,24809.0,379725250.0,136910804310.0,8930907,KOSPI
2024-04-19,12900.0,12900.0,12630.0,12770.0,14793.0,188285480.0,114047682390.0,8930907,KOSPI
2024-07-17,14210.0,15490.0,14210.0,15220.0,233961.0,3528811590.0,135928404540.0,8930907,KOSPI
2024-08-05,14500.0,14500.0,13210.0,13630.0,104755.0,1449499860.0,121728262410.0,8930907,KOSPI
```

Backtest:

| window | peak/high | peak date | trough/low | trough date | MFE | MAE |
|---|---:|---|---:|---|---:|---:|
| 30 calendar days | 15430 | 2024-02-19 | 13390 | 2024-01-29 | +14.04% | -1.03% |
| 90 calendar days | 15430 | 2024-02-19 | 12630 | 2024-04-19 | +14.04% | -6.65% |
| 180 calendar days | 15490 | 2024-07-17 | 12630 | 2024-04-19 | +14.49% | -6.65% |

Interpretation:

```text
013580 is a contained-MAE positive-guarded C30 case.
MFE was moderate rather than explosive, but drawdown stayed away from hard 4B/4C territory.
This can remain Stage2-Guarded and possibly Yellow after URL-repaired PF/refinancing/working-capital evidence, not Green from low-PBR construction relief alone.
```

### 6.2 `014790` HL D&I — mid/small contractor PF-policy relief high-MFE / low-MAE path

Trigger:

```text
trigger_date = 2024-06-03
trigger_type = Stage2-Actionable-Guarded
trigger_family = midsmall_contractor_pf_policy_relief_high_mfe_low_mae
entry_date = 2024-06-04
entry_price = 2025.0
entry_price_type = next_tradable_open_after_midsmall_construction_policy_relief
```

Relevant Stock-Web rows:

```csv
d,o,h,l,c,v,a,mc,s,m
2024-06-03,2010.0,2025.0,2010.0,2025.0,68223.0,137620175.0,76663667025.0,37858601,KOSPI
2024-06-04,2025.0,2390.0,2015.0,2105.0,1688164.0,3722706085.0,79692355105.0,37858601,KOSPI
2024-06-20,2285.0,2660.0,2250.0,2395.0,3475236.0,8673943680.0,90671349395.0,37858601,KOSPI
2024-07-19,2410.0,2645.0,2360.0,2540.0,905239.0,2288707345.0,96160846540.0,37858601,KOSPI
2024-08-05,2445.0,2465.0,2210.0,2250.0,295634.0,679151525.0,85181852250.0,37858601,KOSPI
2024-08-23,2645.0,2880.0,2625.0,2870.0,371789.0,1035857620.0,108654184870.0,37858601,KOSPI
2024-12-02,2360.0,2380.0,2270.0,2320.0,57024.0,131972885.0,87831954320.0,37858601,KOSPI
```

Backtest:

| window | peak/high | peak date | trough/low | trough date | MFE | MAE |
|---|---:|---|---:|---|---:|---:|
| 30 calendar days | 2660 | 2024-06-20 | 2015 | 2024-06-04 | +31.36% | -0.49% |
| 90 calendar days | 2880 | 2024-08-23 | 2015 | 2024-06-04 | +42.22% | -0.49% |
| 180 calendar days | 2880 | 2024-08-23 | 2015 | 2024-06-04 | +42.22% | -0.49% |

Interpretation:

```text
014790 is the high-MFE / low-MAE positive holdout.
This prevents the C30 router from becoming a blanket anti-construction filter: some mid/small contractor relief paths did rerate without early capital impairment.
Green still requires URL-repaired PF liquidity, project margin, working-capital, and cash-flow evidence.
```

### 6.3 `013360` 일성건설 — small contractor event spike with early high MAE

Trigger:

```text
trigger_date = 2024-04-09
trigger_type = Stage2-FalsePositive-Candidate
trigger_family = small_contractor_policy_event_spike_early_high_mae
entry_date = 2024-04-11
entry_price = 1395.0
entry_price_type = next_tradable_open_after_small_contractor_event_spike
```

Relevant Stock-Web rows:

```csv
d,o,h,l,c,v,a,mc,s,m
2024-04-09,1213.0,1484.0,1213.0,1380.0,5384678.0,7537323542.0,74554334400.0,54024880,KOSPI
2024-04-11,1395.0,1583.0,1285.0,1380.0,2434893.0,3473912568.0,74554334400.0,54024880,KOSPI
2024-04-19,1216.0,1216.0,1172.0,1186.0,178321.0,212722951.0,64073507680.0,54024880,KOSPI
2024-04-22,1255.0,1541.0,1216.0,1449.0,11756121.0,17311315849.0,78282051120.0,54024880,KOSPI
2024-06-24,1325.0,1330.0,1260.0,1260.0,137545.0,176077936.0,68071348800.0,54024880,KOSPI
2024-07-23,1464.0,1860.0,1464.0,1663.0,9542026.0,16343694298.0,89843375440.0,54024880,KOSPI
2024-08-05,1500.0,1500.0,1288.0,1340.0,561790.0,776998638.0,72393339200.0,54024880,KOSPI
```

Backtest:

| window | peak/high | peak date | trough/low | trough date | MFE | MAE |
|---|---:|---|---:|---|---:|---:|
| 30 calendar days | 1583 | 2024-04-11 | 1172 | 2024-04-19 | +13.48% | -15.99% |
| 90 calendar days | 1583 | 2024-04-11 | 1172 | 2024-04-19 | +13.48% | -15.99% |
| 180 calendar days | 1860 | 2024-07-23 | 1172 | 2024-04-19 | +33.33% | -15.99% |

Interpretation:

```text
013360 is the early-high-MAE / delayed-MFE warning.
The later peak made the full-window MFE look useful, but the entry first had to absorb a -15.99% MAE.
This should not become Yellow/Green until project/PF/cash-flow evidence is URL-repaired; it belongs at Stage2-Guarded or local 4B watch.
```

### 6.4 `002410` 범양건영 — weak-MFE small-contractor PF slow fade

Trigger:

```text
trigger_date = 2024-02-01
trigger_type = Stage2-FalsePositive-Candidate
trigger_family = small_contractor_low_pbr_pf_relief_weak_mfe_slow_fade
entry_date = 2024-02-02
entry_price = 1780.0
entry_price_type = next_tradable_open_after_small_contractor_low_pbr_pf_relief
```

Relevant Stock-Web rows:

```csv
d,o,h,l,c,v,a,mc,s,m
2024-02-01,1767.0,1784.0,1750.0,1767.0,36120.0,63933427.0,43878112194.0,24831982,KOSPI
2024-02-02,1780.0,1803.0,1767.0,1787.0,61197.0,109390158.0,44374751834.0,24831982,KOSPI
2024-02-28,1668.0,1721.0,1668.0,1721.0,67810.0,115183488.0,42735841022.0,24831982,KOSPI
2024-03-05,1701.0,1709.0,1667.0,1667.0,167138.0,283788467.0,41394913994.0,24831982,KOSPI
2024-04-08,1399.0,1432.0,1367.0,1421.0,168953.0,235660026.0,35286246422.0,24831982,KOSPI
2024-07-03,1259.0,1262.0,1192.0,1233.0,109604.0,133177832.0,30617833806.0,24831982,KOSPI
2024-07-30,1404.0,1572.0,1364.0,1376.0,1151067.0,1708707433.0,34168807232.0,24831982,KOSPI
2024-08-05,1323.0,1347.0,1198.0,1198.0,199593.0,254521880.0,29748714436.0,24831982,KOSPI
```

Backtest:

| window | peak/high | peak date | trough/low | trough date | MFE | MAE |
|---|---:|---|---:|---|---:|---:|
| 30 calendar days | 1803 | 2024-02-02 | 1668 | 2024-02-28 | +1.29% | -6.29% |
| 90 calendar days | 1803 | 2024-02-02 | 1367 | 2024-04-08 | +1.29% | -23.20% |
| 180 calendar days | 1803 | 2024-02-02 | 1192 | 2024-07-03 | +1.29% | -33.03% |

Interpretation:

```text
002410 is the quiet weak-MFE C30 failure.
It did not need a spectacular crash to fail Stage2; it simply never rerated while MAE widened over time.
This is important for C30 because PF/balance-sheet stress can fail as a slow fade, not only as a sudden 4C thesis break.
```

---

## 7. Machine-readable trigger JSONL

```jsonl
{"row_type":"trigger","research_id":"R10L75_C30_MIDSMALL_PF_REPAIR_ROUTER","round":"R10","loop":75,"large_sector_id":"L9_CONSTRUCTION_REALESTATE_HOUSING","canonical_archetype_id":"C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK","fine_archetype_id":"REGIONAL_CONTRACTOR_LOW_PBR_PF_REPAIR_AND_WEAK_MFE_HIGH_MAE_ROUTER","symbol":"013580","name":"계룡건설","trigger_type":"Stage2-Actionable-Guarded","trigger_family":"regional_contractor_low_pbr_pf_repair_contained_mae","trigger_date":"2024-01-26","entry_date":"2024-01-29","entry_price":13530.0,"entry_price_type":"next_tradable_open_after_low_pbr_construction_pf_repair","price_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","mfe_30d_pct":14.04,"mae_30d_pct":-1.03,"mfe_90d_pct":14.04,"mae_90d_pct":-6.65,"mfe_180d_pct":14.49,"mae_180d_pct":-6.65,"peak_price_180d":15490.0,"peak_date_180d":"2024-07-17","trough_price_180d":12630.0,"trough_date_180d":"2024-04-19","calibration_usable":true,"case_polarity":"positive_guarded_contained_mae","evidence_url_pending":true,"source_proxy_only":true,"non_price_evidence_strength":"medium_low_pending_url_repair","price_only_blowoff":false,"expected_stage_current_profile":"Stage2-Guarded_to_Yellow_if_pf_refinancing_working_capital_order_margin_bridge_repaired","residual_error_type":"contained_mae_regional_contractor_path_requires_url_repaired_balance_sheet_liquidity_bridge_before_yellow_green"}
{"row_type":"trigger","research_id":"R10L75_C30_MIDSMALL_PF_REPAIR_ROUTER","round":"R10","loop":75,"large_sector_id":"L9_CONSTRUCTION_REALESTATE_HOUSING","canonical_archetype_id":"C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK","fine_archetype_id":"REGIONAL_CONTRACTOR_LOW_PBR_PF_REPAIR_AND_WEAK_MFE_HIGH_MAE_ROUTER","symbol":"014790","name":"HL D&I","trigger_type":"Stage2-Actionable-Guarded","trigger_family":"midsmall_contractor_pf_policy_relief_high_mfe_low_mae","trigger_date":"2024-06-03","entry_date":"2024-06-04","entry_price":2025.0,"entry_price_type":"next_tradable_open_after_midsmall_construction_policy_relief","price_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","mfe_30d_pct":31.36,"mae_30d_pct":-0.49,"mfe_90d_pct":42.22,"mae_90d_pct":-0.49,"mfe_180d_pct":42.22,"mae_180d_pct":-0.49,"peak_price_180d":2880.0,"peak_date_180d":"2024-08-23","trough_price_180d":2015.0,"trough_date_180d":"2024-06-04","calibration_usable":true,"case_polarity":"positive_guarded_high_mfe_low_mae","evidence_url_pending":true,"source_proxy_only":true,"non_price_evidence_strength":"medium_low_pending_url_repair","price_only_blowoff":false,"expected_stage_current_profile":"Stage2-Guarded_to_Yellow_if_pf_liquidity_project_margin_cashflow_bridge_repaired","residual_error_type":"policy_relief_high_mfe_low_mae_path_should_not_be_overblocked_but_green_requires_balance_sheet_project_margin_bridge"}
{"row_type":"trigger","research_id":"R10L75_C30_MIDSMALL_PF_REPAIR_ROUTER","round":"R10","loop":75,"large_sector_id":"L9_CONSTRUCTION_REALESTATE_HOUSING","canonical_archetype_id":"C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK","fine_archetype_id":"REGIONAL_CONTRACTOR_LOW_PBR_PF_REPAIR_AND_WEAK_MFE_HIGH_MAE_ROUTER","symbol":"013360","name":"일성건설","trigger_type":"Stage2-FalsePositive-Candidate","trigger_family":"small_contractor_policy_event_spike_early_high_mae","trigger_date":"2024-04-09","entry_date":"2024-04-11","entry_price":1395.0,"entry_price_type":"next_tradable_open_after_small_contractor_event_spike","price_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","mfe_30d_pct":13.48,"mae_30d_pct":-15.99,"mfe_90d_pct":13.48,"mae_90d_pct":-15.99,"mfe_180d_pct":33.33,"mae_180d_pct":-15.99,"peak_price_180d":1860.0,"peak_date_180d":"2024-07-23","trough_price_180d":1172.0,"trough_date_180d":"2024-04-19","calibration_usable":true,"case_polarity":"counterexample_early_high_mae_then_delayed_mfe","evidence_url_pending":true,"source_proxy_only":true,"non_price_evidence_strength":"low_pending_url_repair","price_only_blowoff":false,"expected_stage_current_profile":"Stage2-Guarded_or_local_4B_watch_until_pf_cashflow_project_bridge_repaired","residual_error_type":"small_contractor_event_entry_had_early_high_mae_before_delayed_mfe_without_balance_sheet_bridge"}
{"row_type":"trigger","research_id":"R10L75_C30_MIDSMALL_PF_REPAIR_ROUTER","round":"R10","loop":75,"large_sector_id":"L9_CONSTRUCTION_REALESTATE_HOUSING","canonical_archetype_id":"C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK","fine_archetype_id":"REGIONAL_CONTRACTOR_LOW_PBR_PF_REPAIR_AND_WEAK_MFE_HIGH_MAE_ROUTER","symbol":"002410","name":"범양건영","trigger_type":"Stage2-FalsePositive-Candidate","trigger_family":"small_contractor_low_pbr_pf_relief_weak_mfe_slow_fade","trigger_date":"2024-02-01","entry_date":"2024-02-02","entry_price":1780.0,"entry_price_type":"next_tradable_open_after_small_contractor_low_pbr_pf_relief","price_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","mfe_30d_pct":1.29,"mae_30d_pct":-6.29,"mfe_90d_pct":1.29,"mae_90d_pct":-23.2,"mfe_180d_pct":1.29,"mae_180d_pct":-33.03,"peak_price_180d":1803.0,"peak_date_180d":"2024-02-02","trough_price_180d":1192.0,"trough_date_180d":"2024-07-03","calibration_usable":true,"case_polarity":"counterexample_weak_mfe_slow_fade_high_mae","evidence_url_pending":true,"source_proxy_only":true,"non_price_evidence_strength":"low_pending_url_repair","price_only_blowoff":false,"expected_stage_current_profile":"blocked_Stage2_or_local_4B_high_MAE_watch","residual_error_type":"small_contractor_pf_relief_label_had_almost_no_mfe_and_later_high_mae_without_liquidity_repair_bridge"}
```

---

## 8. Score simulation and raw component breakdown

This is shadow-only and does not change production scoring.

| symbol | PF/liquidity repair | refinancing / maturity wall | working-capital quality | project/order margin | market mispricing | cash-flow / covenant bridge | information confidence | shadow total | intended route |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| `014790` | 9 | 8 | 7 | 8 | 12 | 7 | 5 | 56 | Stage2-Guarded / Yellow after evidence repair |
| `013580` | 8 | 8 | 7 | 8 | 8 | 6 | 5 | 50 | Stage2-Guarded until balance-sheet bridge repaired |
| `013360` | 5 | 4 | 4 | 5 | 8 | 3 | 4 | 33 | Stage2-Guarded or local 4B watch |
| `002410` | 3 | 3 | 3 | 3 | 2 | 2 | 4 | 20 | blocked Stage2 / weak-MFE high-MAE watch |

### Current calibrated profile stress test

The current calibrated profile already blocks pure price-only blowoff.  
The remaining C30 issue is **construction/PF label without balance-sheet repair evidence**:

```text
C30 low-MAE repair path:
  contractor relief / low-PBR setup
  + MFE is moderate or high
  + MAE remains contained
  + URL-repaired PF/refinancing/working-capital bridge
  => Stage2-Guarded, possible Yellow after proof

C30 early-high-MAE delayed-MFE path:
  policy/event spike creates MFE
  + MAE_30D <= -15%
  + later MFE arrives only after high drawdown
  => Stage2-Guarded at most, local 4B watch, no Green

C30 weak-MFE slow fade:
  small-contractor/PF label exists
  + MFE_90D < +5%
  + MAE_90D <= -20% or MAE_180D <= -30%
  + bridge evidence remains unrepaired
  => block Stage2 or route to weak-MFE 4B watch
```

`014790` and `013580` prevent overblocking.  
`013360` shows why delayed MFE cannot erase early high MAE.  
`002410` adds the quiet failure mode: no MFE, widening PF/balance-sheet discount.

---

## 9. Aggregate metrics

```json
{
  "row_type": "aggregate",
  "research_id": "R10L75_C30_MIDSMALL_PF_REPAIR_ROUTER",
  "round": "R10",
  "loop": 75,
  "large_sector_id": "L9_CONSTRUCTION_REALESTATE_HOUSING",
  "canonical_archetype_id": "C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK",
  "fine_archetype_id": "REGIONAL_CONTRACTOR_LOW_PBR_PF_REPAIR_AND_WEAK_MFE_HIGH_MAE_ROUTER",
  "case_count": 4,
  "calibration_usable_case_count": 4,
  "positive_guarded_case_count": 2,
  "counterexample_count": 2,
  "new_symbol_count": 4,
  "source_proxy_only_count": 4,
  "evidence_url_pending_count": 4,
  "avg_mfe_30d_pct": 15.04,
  "avg_mae_30d_pct": -5.95,
  "avg_mfe_90d_pct": 17.76,
  "avg_mae_90d_pct": -11.58,
  "avg_mfe_180d_pct": 22.83,
  "avg_mae_180d_pct": -14.04,
  "max_mfe_180d_pct": 42.22,
  "worst_mae_180d_pct": -33.03
}
```

---

## 10. 4B proximity split

```json
{
  "row_type": "4b_split",
  "research_id": "R10L75_C30_MIDSMALL_PF_REPAIR_ROUTER",
  "stage2_guarded_or_yellow_candidate": [
    {
      "symbol": "014790",
      "reason": "high +42.22% 180D MFE with only -0.49% MAE; requires PF/project/cash-flow evidence before Green"
    },
    {
      "symbol": "013580",
      "reason": "contained-MAE contractor repair path; MFE moderate but drawdown remained controlled"
    }
  ],
  "local_4b_watch": [
    {
      "symbol": "013360",
      "reason": "later MFE improved, but 30D/90D MAE was already -15.99% before evidence repair"
    }
  ],
  "blocked_stage2_or_weak_mfe_fade": [
    {
      "symbol": "002410",
      "reason": "MFE stayed only +1.29%, while 90D MAE reached -23.20% and 180D MAE reached -33.03%"
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
fine_archetype_id: REGIONAL_CONTRACTOR_LOW_PBR_PF_REPAIR_AND_WEAK_MFE_HIGH_MAE_ROUTER
rule_name: C30_regional_contractor_pf_repair_low_mae_and_weak_mfe_high_mae_router
production_scoring_changed: false
shadow_weight_only: true
```

### Proposed routing logic

```text
For C30 regional/mid-small construction PF repair cases:

Tier A: contained-MAE PF repair candidate
  Conditions:
    - PF/liquidity relief or low-PBR contractor repair relevance is plausible
    - MFE_90D >= +10%
    - MAE_90D > -10%
    - evidence remains source_proxy_only
  Routing:
    - Stage2-Guarded allowed
    - Stage3-Yellow only after URL-repaired PF/refinancing/working-capital evidence
    - no Green while evidence is pending

Tier B: high-MFE policy-relief holdout
  Conditions:
    - MFE_90D >= +30%
    - MAE_90D > -5%
    - evidence_url_pending or source_proxy_only remains true
  Routing:
    - Stage2-Guarded allowed
    - no Green until project margin / cash-flow bridge is repaired

Tier C: early-high-MAE delayed-MFE
  Conditions:
    - MAE_30D <= -15%
    - later MFE improves
    - no repaired PF/cash-flow evidence
  Routing:
    - Stage2-Guarded at most
    - local 4B watch
    - no Yellow/Green

Tier D: weak-MFE PF slow fade
  Conditions:
    - MFE_90D < +5%
    - MAE_90D <= -20% or MAE_180D <= -30%
    - no repaired liquidity/balance-sheet bridge
  Routing:
    - block Stage2 or local 4B/high-MAE watch
    - count as counterexample
```

### Suggested shadow delta

```json
{
  "row_type": "shadow_weight",
  "axis": "c30_regional_contractor_pf_repair_low_mae_and_weak_mfe_high_mae_router",
  "scope": "canonical_archetype_id:C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK",
  "proposal": {
    "source_proxy_only_green_allowed": false,
    "balance_sheet_liquidity_cashflow_bridge_required_for_yellow_green": true,
    "contained_mae_mfe90_threshold_pct": 10.0,
    "contained_mae90_min_pct": -10.0,
    "high_mfe_policy_relief_threshold_90d_pct": 30.0,
    "high_mfe_policy_relief_mae90_min_pct": -5.0,
    "early_high_mae_threshold_30d_pct": -15.0,
    "weak_mfe_threshold_90d_pct": 5.0,
    "weak_mfe_mae90_threshold_pct": -20.0,
    "weak_mfe_hard_mae180_threshold_pct": -30.0,
    "positive_weight_blocked_until_url_repair": true
  },
  "confidence": "medium_low_until_url_repair",
  "apply_now": false,
  "reason": "Two non-top-covered contractor low-MAE positives and two small-contractor high-MAE or weak-MFE failures show that C30 should require URL-repaired PF, refinancing, working-capital, project-margin, and cash-flow evidence before Yellow/Green."
}
```

---

## 12. Residual contribution summary

```json
{
  "row_type": "residual_contribution",
  "research_id": "R10L75_C30_MIDSMALL_PF_REPAIR_ROUTER",
  "large_sector_id": "L9_CONSTRUCTION_REALESTATE_HOUSING",
  "canonical_archetype_id": "C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK",
  "contribution": "Adds four non-top-covered C30 regional/mid-small construction cases and separates contained-MAE PF repair and high-MFE policy-relief holdouts from early-high-MAE delayed-MFE and weak-MFE slow-fade failures. C30 Yellow/Green should require URL-repaired PF exposure, refinancing, working capital, project margin, cash flow, covenant, and liquidity evidence.",
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
  "guardrail_added": "C30 source_proxy_only cases with MFE_90D < +5% and MAE_90D <= -20% or MAE_180D <= -30% should block Stage2; early-high-MAE cases with MAE_30D <= -15% should cap at Stage2-Guarded until balance-sheet evidence is repaired."
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
    013580: false
    014790: false
    013360: false
    002410: false
  evidence_url_pending:
    013580: true
    014790: true
    013360: true
    002410: true
  source_proxy_only:
    013580: true
    014790: true
    013360: true
    002410: true
```

Limitations:

```text
- Price path is validated against Stock-Web tradable OHLC rows.
- Non-price evidence is not URL-repaired in this run.
- Therefore this artifact is useful for C30 regional/mid-small construction PF residual shape and weak-MFE/high-MAE guardrail design, but should not promote positive weights until filings, credit reports, IR, project disclosures, or reports verify PF exposure, refinancing, receivables, working capital, unsold inventory, project margin, cash-flow conversion, and covenant/liquidity headroom.
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
2. Preserve R10 / loop 75 metadata.
3. Add the cases to C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK only if parser validation passes.
4. Treat all four non-price triggers as evidence_url_pending=true and source_proxy_only=true until URL-level evidence is repaired.
5. Do not use these rows for positive weight promotion until filings/credit-report/IR/project-disclosure/report data verifies PF exposure, refinancing, receivables, working capital, unsold inventory, project margin, cash-flow conversion, and covenant/liquidity headroom.
6. Add a shadow-only rule candidate named C30_regional_contractor_pf_repair_low_mae_and_weak_mfe_high_mae_router.
7. Do not loosen Stage3-Green.
8. Add C30-specific guards:
   - source_proxy_only -> no Green
   - Stage3-Yellow/Green requires repaired PF / refinancing / working-capital / cash-flow bridge
   - MFE_90D >= +10% and MAE_90D > -10% may remain Stage2-Guarded until evidence repair
   - MFE_90D >= +30% and MAE_90D > -5% may remain high-MFE policy-relief holdout
   - MAE_30D <= -15% before evidence repair -> Stage2-Guarded at most / local 4B watch
   - MFE_90D < +5% and MAE_90D <= -20% or MAE_180D <= -30% -> block Stage2 or local 4B/high-MAE watch
9. Keep production scoring unchanged unless later batch promotion logic independently marks this axis safe.
```

---

## 15. Next round state

```text
completed_round = R10
completed_loop = 75
next_round = R11
next_loop = 75
next_large_sector_hint = L10_POLICY_EVENT_CROSS_REDTEAM_MISC or L1 defense-linked policy event
round_schedule_status = valid
round_sector_consistency = pass
```
