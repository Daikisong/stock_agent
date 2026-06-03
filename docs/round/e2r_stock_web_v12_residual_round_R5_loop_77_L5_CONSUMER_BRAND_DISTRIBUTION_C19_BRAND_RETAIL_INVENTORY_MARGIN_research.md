# E2R Stock-Web v12 Residual Research — R5 Loop 77

```yaml
research_session: post_calibrated_sector_archetype_residual_research
mode: historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12
completed_round: R5
completed_loop: 77
next_round: R6
next_loop: 77
large_sector_id: L5_CONSUMER_BRAND_DISTRIBUTION
canonical_archetype_id: C19_BRAND_RETAIL_INVENTORY_MARGIN
fine_archetype_id: CONVENIENCE_DEPARTMENT_DISCOUNT_STORE_INVENTORY_MARGIN_LOW_MAE_AND_WEAK_MFE_ROUTER
output_file: e2r_stock_web_v12_residual_round_R5_loop_77_L5_CONSUMER_BRAND_DISTRIBUTION_C19_BRAND_RETAIL_INVENTORY_MARGIN_research.md
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
completed_round = R4
completed_loop  = 77
large_sector_id = L4_MATERIALS_SPREAD_RESOURCE
canonical_archetype_id = C16_STRATEGIC_RESOURCE_POLICY_SUPPLY
```

Therefore:

```text
scheduled_round = R5
scheduled_loop  = 77
```

R5 maps to:

```text
large_sector_id = L5_CONSUMER_BRAND_DISTRIBUTION
```

This run selects:

```text
canonical_archetype_id = C19_BRAND_RETAIL_INVENTORY_MARGIN
fine_archetype_id = CONVENIENCE_DEPARTMENT_DISCOUNT_STORE_INVENTORY_MARGIN_LOW_MAE_AND_WEAK_MFE_ROUTER
```

This is a valid R5/L5 pairing.

---

## 1. Why this R5/C19 run

The no-repeat ledger shows C19 is less dense than the major C18/C20/C21 consumer-financial clusters:

```text
C19_BRAND_RETAIL_INVENTORY_MARGIN:
  rows: 89
  symbols: 17
  date_range: 2021-05-17~2024-10-16
  good/bad S2: 17/14
  4B/4C: 18/7
  URL/proxy: 21/25
  top covered symbols: 111770(11), 081660(10), 383220(9), UNKNOWN_SYMBOL(8), 020000(7), 036620(7)
```

This file avoids those top-covered symbols and focuses on domestic retail / department store / discount-store inventory and margin cases:

```text
007070 GS리테일
004170 신세계
282330 BGF리테일
139480 이마트
```

Research question:

```text
Can C19 separate retail-margin recovery paths with controlled MAE from retail/value-up/inventory-turnaround labels where same-store sales, inventory turnover, asset restructuring, and margin conversion are not visible?
```

C19 is a shelf economics archetype. A retailer can polish the storefront, but Stage2 lives in the back room: inventory turns, gross margin, same-store traffic, promotion intensity, store mix, duty-free recovery, and cash conversion. If the shelves move slowly, the label becomes a warehouse cost, not a rerating.

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
| `007070` | GS리테일 | active_like / KOSPI | 2024-12-23 candidate after selected 180D window | true for selected 180D |
| `004170` | 신세계 | active_like / KOSPI | old candidates only; none in 2024 window | true |
| `282330` | BGF리테일 | active_like / KOSPI | none listed | true |
| `139480` | 이마트 | active_like / KOSPI | none listed | true |

Profile caveat:

```text
Stock-Web OHLC is raw/unadjusted marcap data.
These cases are calibration-safe for the selected 2024 30D/90D/180D windows because no listed corporate-action candidate overlaps each entry~D+180 test window.
For 007070, the 2024-12-23 candidate is after the selected 2024-04-18~2024-10-15 test window and is not used here.
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
The Stock-Web price path is fully validated, but company-level same-store sales, store traffic, inventory turnover, promotion intensity, gross margin, duty-free recovery, online/offline mix, asset restructuring, working capital, and cash-flow conversion evidence still require later URL repair through filings, IR decks, channel data, retail sales data, or sell-side reports before production weight promotion.
```

C19 interpretation used here:

```text
C19 is not simply “retail stock rose.”
It asks whether retail/brand relevance becomes shelf economics:
- same-store sales and traffic,
- inventory turnover and markdown risk,
- gross margin and promotion intensity,
- store mix and channel mix,
- duty-free or department-store recovery where relevant,
- asset restructuring and working capital,
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
139480 + C19_BRAND_RETAIL_INVENTORY_MARGIN -> no direct match found
282330 + C19_BRAND_RETAIL_INVENTORY_MARGIN -> no direct match found
007070 + C19_BRAND_RETAIL_INVENTORY_MARGIN -> not in top-covered C19 symbols
004170 + C19_BRAND_RETAIL_INVENTORY_MARGIN -> not in top-covered C19 symbols
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
| `R5L77_C19_007070_20240418` | `007070` GS리테일 | convenience-store margin recovery / inventory normalization | positive-guarded low-MAE |
| `R5L77_C19_004170_20240418` | `004170` 신세계 | department store / duty-free inventory-margin recovery | positive-guarded, later drawdown |
| `R5L77_C19_282330_20240227` | `282330` BGF리테일 | convenience-store value-up / margin label with weak MFE | weak-MFE slow-drawdown counterexample |
| `R5L77_C19_139480_20240227` | `139480` 이마트 | discount-store inventory-margin turnaround label with weak MFE | weak-MFE high-MAE counterexample |

The intended residual:

```text
C19 should separate:
1. retail-margin recovery paths where MAE remains contained;
2. department/duty-free recovery paths where first-window MFE exists but later drawdown caps Green;
3. convenience-store value-up/margin labels where forward MFE never confirms the thesis;
4. discount-store turnaround labels where inventory/asset-margin repair is not visible and drawdown widens.
```

---

## 6. Stock-Web OHLC and backtest

### 6.1 `007070` GS리테일 — convenience-store margin recovery low-MAE route

Trigger:

```text
trigger_date = 2024-04-17
trigger_type = Stage2-Actionable-Guarded
trigger_family = convenience_store_margin_recovery_inventory_normalization_low_mae_rerating
entry_date = 2024-04-18
entry_price = 18810.0
entry_price_type = next_tradable_open_after_retail_margin_recovery_inventory_normalization_burst
```

Relevant Stock-Web rows:

```csv
d,o,h,l,c,v,a,mc,s,m
2024-04-17,18570.0,18800.0,18510.0,18600.0,176258.0,3291479270.0,1947753349200.0,104717922,KOSPI
2024-04-18,18810.0,19100.0,18630.0,19070.0,153170.0,2908008380.0,1996970772540.0,104717922,KOSPI
2024-05-10,20650.0,21400.0,20500.0,21050.0,444654.0,9389716900.0,2204312258100.0,104717922,KOSPI
2024-07-15,21600.0,21650.0,21200.0,21200.0,175022.0,3741311650.0,2220019946400.0,104717922,KOSPI
2024-08-05,22650.0,23200.0,20800.0,21350.0,1068621.0,23801051050.0,2235727634700.0,104717922,KOSPI
2024-10-04,21050.0,21100.0,20600.0,20700.0,142831.0,2964497300.0,2167660985400.0,104717922,KOSPI
```

Backtest:

| window | peak/high | peak date | trough/low | trough date | MFE | MAE |
|---|---:|---|---:|---|---:|---:|
| 30 calendar days | 21400 | 2024-05-10 | 18630 | 2024-04-18 | +13.77% | -0.96% |
| 90 calendar days | 21650 | 2024-07-15 | 18630 | 2024-04-18 | +15.10% | -0.96% |
| 180 calendar days | 23200 | 2024-08-05 | 18630 | 2024-04-18 | +23.34% | -0.96% |

Interpretation:

```text
007070 is the C19 low-MAE positive-guarded route.
The MFE is not explosive, but the path is return-aligned because MAE stays extremely contained while the stock grinds upward.
It can remain Stage2-Guarded / Yellow-after-repair, but Green still requires URL-repaired same-store sales, traffic, inventory, and margin evidence.
```

### 6.2 `004170` 신세계 — department-store / duty-free inventory-margin recovery with later drawdown

Trigger:

```text
trigger_date = 2024-04-17
trigger_type = Stage2-Actionable-Guarded
trigger_family = department_store_dutyfree_inventory_margin_recovery_first_window_mfe_later_drawdown
entry_date = 2024-04-18
entry_price = 159900.0
entry_price_type = next_tradable_open_after_department_store_margin_inventory_recovery_burst
```

Relevant Stock-Web rows:

```csv
d,o,h,l,c,v,a,mc,s,m
2024-04-17,160100.0,161700.0,159400.0,160800.0,36927.0,5934118200.0,1583105104800.0,9845181,KOSPI
2024-04-18,159900.0,162700.0,159100.0,161200.0,42562.0,6826538100.0,1587043177200.0,9845181,KOSPI
2024-05-09,177400.0,181000.0,174300.0,177100.0,167814.0,29943422400.0,1743581555100.0,9845181,KOSPI
2024-07-03,157300.0,158000.0,154500.0,155600.0,44152.0,6866309200.0,1531910163600.0,9845181,KOSPI
2024-08-05,151600.0,152100.0,138800.0,142100.0,73033.0,10503417900.0,1399000220100.0,9845181,KOSPI
2024-09-27,160900.0,164600.0,160000.0,162300.0,64429.0,10518077300.0,1597872876300.0,9845181,KOSPI
```

Backtest:

| window | peak/high | peak date | trough/low | trough date | MFE | MAE |
|---|---:|---|---:|---|---:|---:|
| 30 calendar days | 181000 | 2024-05-09 | 157900 | 2024-04-19 | +13.20% | -1.25% |
| 90 calendar days | 181000 | 2024-05-09 | 154500 | 2024-07-03 | +13.20% | -3.38% |
| 180 calendar days | 181000 | 2024-05-09 | 138800 | 2024-08-05 | +13.20% | -13.20% |

Interpretation:

```text
004170 is a positive-guarded but not Green-quality C19 path.
The first-window MFE and initially shallow MAE preserve Stage2-Guarded status, but the later -13.20% 180D MAE blocks Yellow/Green while the margin and inventory bridge remains unrepaired.
```

### 6.3 `282330` BGF리테일 — convenience-store value-up/margin label weak-MFE slow drawdown

Trigger:

```text
trigger_date = 2024-02-26
trigger_type = Stage2-FalsePositive-Candidate
trigger_family = convenience_store_valueup_margin_label_weak_mfe_slow_drawdown
entry_date = 2024-02-27
entry_price = 131800.0
entry_price_type = next_tradable_open_after_retail_valueup_margin_label
```

Relevant Stock-Web rows:

```csv
d,o,h,l,c,v,a,mc,s,m
2024-02-26,133500.0,133500.0,130400.0,131200.0,30192.0,3975691100.0,2267648467200.0,17283906,KOSPI
2024-02-27,131800.0,131800.0,129900.0,130000.0,31489.0,4107064600.0,2246907780000.0,17283906,KOSPI
2024-02-28,130200.0,134100.0,130100.0,133900.0,56163.0,7478963200.0,2314315013400.0,17283906,KOSPI
2024-03-22,117600.0,118600.0,116500.0,118600.0,74330.0,8750447900.0,2049871251600.0,17283906,KOSPI
2024-04-16,112000.0,117100.0,111300.0,117100.0,67490.0,7727244500.0,2023945392600.0,17283906,KOSPI
2024-05-08,134100.0,136200.0,131300.0,136200.0,33728.0,4517217700.0,2354067997200.0,17283906,KOSPI
2024-07-05,101500.0,101700.0,99000.0,99900.0,132549.0,13291305200.0,1726662209400.0,17283906,KOSPI
```

Backtest:

| window | peak/high | peak date | trough/low | trough date | MFE | MAE |
|---|---:|---|---:|---|---:|---:|
| 30 calendar days | 134100 | 2024-02-28 | 116500 | 2024-03-22 | +1.75% | -11.61% |
| 90 calendar days | 136200 | 2024-05-08 | 111300 | 2024-04-16 | +3.34% | -15.55% |
| 180 calendar days | 136200 | 2024-05-08 | 99000 | 2024-07-05 | +3.34% | -24.89% |

Interpretation:

```text
282330 is the C19 weak-MFE slow-drawdown counterexample.
The retail margin/value-up label existed, but MFE never confirmed the thesis and the 180D drawdown widened.
This should block Green and usually block Stage2 unless a fresh trigger repairs same-store sales, store traffic, inventory, and margin evidence.
```

### 6.4 `139480` 이마트 — discount-store inventory-margin turnaround label weak-MFE high-MAE path

Trigger:

```text
trigger_date = 2024-02-26
trigger_type = Stage2-FalsePositive-Candidate
trigger_family = discount_store_inventory_margin_turnaround_label_weak_mfe_high_mae
entry_date = 2024-02-27
entry_price = 72800.0
entry_price_type = next_tradable_open_after_discount_store_turnaround_valueup_margin_label
```

Relevant Stock-Web rows:

```csv
d,o,h,l,c,v,a,mc,s,m
2024-02-26,75200.0,75300.0,72500.0,73100.0,224698.0,16449331200.0,2037722368900.0,27875819,KOSPI
2024-02-27,72800.0,74700.0,72700.0,73200.0,125949.0,9288099200.0,2040509950800.0,27875819,KOSPI
2024-02-28,73300.0,75500.0,73300.0,74900.0,101979.0,7620271500.0,2087898843100.0,27875819,KOSPI
2024-03-28,68600.0,68900.0,68300.0,68300.0,133388.0,9136369100.0,1903918437700.0,27875819,KOSPI
2024-04-16,60100.0,60400.0,59500.0,60200.0,205811.0,12342710400.0,1678124303800.0,27875819,KOSPI
2024-06-27,55400.0,57000.0,54800.0,55700.0,201478.0,11198644000.0,1552683118300.0,27875819,KOSPI
2024-08-05,61200.0,61300.0,55400.0,56700.0,360083.0,20938948200.0,1580558937300.0,27875819,KOSPI
```

Backtest:

| window | peak/high | peak date | trough/low | trough date | MFE | MAE |
|---|---:|---|---:|---|---:|---:|
| 30 calendar days | 75500 | 2024-02-28 | 68300 | 2024-03-28 | +3.71% | -6.18% |
| 90 calendar days | 75500 | 2024-02-28 | 59500 | 2024-04-16 | +3.71% | -18.27% |
| 180 calendar days | 75500 | 2024-02-28 | 54800 | 2024-06-27 | +3.71% | -24.73% |

Interpretation:

```text
139480 is the discount-store weak-MFE/high-MAE counterexample.
The turnaround/value-up/inventory-margin label did not become return alignment.
C19 should block Stage2 until inventory turnover, promotion intensity, asset restructuring, working capital, and store-margin evidence is repaired.
```

---

## 7. Machine-readable trigger JSONL

```jsonl
{"row_type":"trigger","research_id":"R5L77_C19_RETAIL_INVENTORY_MARGIN_ROUTER","round":"R5","loop":77,"large_sector_id":"L5_CONSUMER_BRAND_DISTRIBUTION","canonical_archetype_id":"C19_BRAND_RETAIL_INVENTORY_MARGIN","fine_archetype_id":"CONVENIENCE_DEPARTMENT_DISCOUNT_STORE_INVENTORY_MARGIN_LOW_MAE_AND_WEAK_MFE_ROUTER","symbol":"007070","name":"GS리테일","trigger_type":"Stage2-Actionable-Guarded","trigger_family":"convenience_store_margin_recovery_inventory_normalization_low_mae_rerating","trigger_date":"2024-04-17","entry_date":"2024-04-18","entry_price":18810.0,"entry_price_type":"next_tradable_open_after_retail_margin_recovery_inventory_normalization_burst","price_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","mfe_30d_pct":13.77,"mae_30d_pct":-0.96,"mfe_90d_pct":15.1,"mae_90d_pct":-0.96,"mfe_180d_pct":23.34,"mae_180d_pct":-0.96,"peak_price_180d":23200.0,"peak_date_180d":"2024-08-05","trough_price_180d":18630.0,"trough_date_180d":"2024-04-18","calibration_usable":true,"case_polarity":"positive_guarded_low_mae_retail_margin","evidence_url_pending":true,"source_proxy_only":true,"non_price_evidence_strength":"medium_low_pending_url_repair","price_only_blowoff":false,"expected_stage_current_profile":"Stage2-Guarded_to_Yellow_if_same_store_sales_inventory_margin_bridge_repaired","residual_error_type":"retail_margin_recovery_path_had_controlled_mae_and_moderate_mfe_but_green_requires_url_repaired_same_store_inventory_margin_bridge"}
{"row_type":"trigger","research_id":"R5L77_C19_RETAIL_INVENTORY_MARGIN_ROUTER","round":"R5","loop":77,"large_sector_id":"L5_CONSUMER_BRAND_DISTRIBUTION","canonical_archetype_id":"C19_BRAND_RETAIL_INVENTORY_MARGIN","fine_archetype_id":"CONVENIENCE_DEPARTMENT_DISCOUNT_STORE_INVENTORY_MARGIN_LOW_MAE_AND_WEAK_MFE_ROUTER","symbol":"004170","name":"신세계","trigger_type":"Stage2-Actionable-Guarded","trigger_family":"department_store_dutyfree_inventory_margin_recovery_first_window_mfe_later_drawdown","trigger_date":"2024-04-17","entry_date":"2024-04-18","entry_price":159900.0,"entry_price_type":"next_tradable_open_after_department_store_margin_inventory_recovery_burst","price_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","mfe_30d_pct":13.2,"mae_30d_pct":-1.25,"mfe_90d_pct":13.2,"mae_90d_pct":-3.38,"mfe_180d_pct":13.2,"mae_180d_pct":-13.2,"peak_price_180d":181000.0,"peak_date_180d":"2024-05-09","trough_price_180d":138800.0,"trough_date_180d":"2024-08-05","calibration_usable":true,"case_polarity":"positive_guarded_first_window_mfe_later_drawdown","evidence_url_pending":true,"source_proxy_only":true,"non_price_evidence_strength":"medium_low_pending_url_repair","price_only_blowoff":false,"expected_stage_current_profile":"Stage2-Guarded_only_until_department_store_dutyfree_inventory_margin_bridge_repaired","residual_error_type":"department_store_inventory_margin_recovery_had_first_window_mfe_but_later_drawdown_requires_url_repaired_inventory_turnover_margin_and_dutyfree_bridge_before_yellow_green"}
{"row_type":"trigger","research_id":"R5L77_C19_RETAIL_INVENTORY_MARGIN_ROUTER","round":"R5","loop":77,"large_sector_id":"L5_CONSUMER_BRAND_DISTRIBUTION","canonical_archetype_id":"C19_BRAND_RETAIL_INVENTORY_MARGIN","fine_archetype_id":"CONVENIENCE_DEPARTMENT_DISCOUNT_STORE_INVENTORY_MARGIN_LOW_MAE_AND_WEAK_MFE_ROUTER","symbol":"282330","name":"BGF리테일","trigger_type":"Stage2-FalsePositive-Candidate","trigger_family":"convenience_store_valueup_margin_label_weak_mfe_slow_drawdown","trigger_date":"2024-02-26","entry_date":"2024-02-27","entry_price":131800.0,"entry_price_type":"next_tradable_open_after_retail_valueup_margin_label","price_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","mfe_30d_pct":1.75,"mae_30d_pct":-11.61,"mfe_90d_pct":3.34,"mae_90d_pct":-15.55,"mfe_180d_pct":3.34,"mae_180d_pct":-24.89,"peak_price_180d":136200.0,"peak_date_180d":"2024-05-08","trough_price_180d":99000.0,"trough_date_180d":"2024-07-05","calibration_usable":true,"case_polarity":"counterexample_weak_mfe_slow_drawdown","evidence_url_pending":true,"source_proxy_only":true,"non_price_evidence_strength":"low_pending_url_repair","price_only_blowoff":false,"expected_stage_current_profile":"blocked_Stage2_or_local_4B_watch_until_store_traffic_margin_inventory_bridge_repaired","residual_error_type":"convenience_store_margin_label_had_weak_mfe_and_later_mae_without_same_store_sales_inventory_margin_bridge"}
{"row_type":"trigger","research_id":"R5L77_C19_RETAIL_INVENTORY_MARGIN_ROUTER","round":"R5","loop":77,"large_sector_id":"L5_CONSUMER_BRAND_DISTRIBUTION","canonical_archetype_id":"C19_BRAND_RETAIL_INVENTORY_MARGIN","fine_archetype_id":"CONVENIENCE_DEPARTMENT_DISCOUNT_STORE_INVENTORY_MARGIN_LOW_MAE_AND_WEAK_MFE_ROUTER","symbol":"139480","name":"이마트","trigger_type":"Stage2-FalsePositive-Candidate","trigger_family":"discount_store_inventory_margin_turnaround_label_weak_mfe_high_mae","trigger_date":"2024-02-26","entry_date":"2024-02-27","entry_price":72800.0,"entry_price_type":"next_tradable_open_after_discount_store_turnaround_valueup_margin_label","price_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","mfe_30d_pct":3.71,"mae_30d_pct":-6.18,"mfe_90d_pct":3.71,"mae_90d_pct":-18.27,"mfe_180d_pct":3.71,"mae_180d_pct":-24.73,"peak_price_180d":75500.0,"peak_date_180d":"2024-02-28","trough_price_180d":54800.0,"trough_date_180d":"2024-06-27","calibration_usable":true,"case_polarity":"counterexample_weak_mfe_high_mae","evidence_url_pending":true,"source_proxy_only":true,"non_price_evidence_strength":"low_pending_url_repair","price_only_blowoff":false,"expected_stage_current_profile":"blocked_Stage2_or_local_4B_watch_until_inventory_turnover_store_margin_asset_restructuring_bridge_repaired","residual_error_type":"discount_store_turnaround_label_had_weak_mfe_and_high_mae_without_inventory_margin_asset_restructuring_bridge"}
```

---

## 8. Score simulation and raw component breakdown

This is shadow-only and does not change production scoring.

| symbol | retail margin relevance | same-store / traffic bridge | inventory turnover | channel / store mix | market mispricing | cash / working-capital conversion | information confidence | shadow total | intended route |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| `007070` | 10 | 8 | 8 | 8 | 8 | 8 | 5 | 55 | Stage2-Guarded / Yellow after evidence repair |
| `004170` | 9 | 6 | 6 | 6 | 7 | 5 | 5 | 44 | Stage2-Guarded only until evidence repair |
| `282330` | 7 | 3 | 3 | 5 | 1 | 3 | 4 | 26 | blocked Stage2 / local 4B watch |
| `139480` | 7 | 3 | 2 | 4 | 1 | 2 | 4 | 23 | blocked Stage2 / local 4B watch |

### Current calibrated profile stress test

The current calibrated profile already blocks pure price-only blowoff.  
The remaining C19 issue is **retail margin / value-up label without same-store and inventory conversion**:

```text
C19 low-MAE retail-margin path:
  same-store / inventory / margin relevance
  + MFE_90D >= +10%
  + MAE_90D > -5%
  + evidence remains source_proxy_only
  => Stage2-Guarded; Yellow only after store-traffic / inventory / margin evidence repair

C19 first-window MFE / later drawdown path:
  department-store or duty-free margin recovery appears
  + MFE_30D >= +10%
  + MAE_180D <= -10%
  + evidence remains source_proxy_only
  => Stage2-Guarded at most, no Green

C19 weak-MFE retail label:
  MFE_90D < +5%
  + MAE_90D <= -15% or MAE_180D <= -20%
  + no repaired inventory / margin bridge
  => block Stage2 or local 4B watch
```

`007070` and `004170` prevent overblocking of retail-margin recovery.  
`282330` and `139480` show why C19 must require same-store sales, inventory turnover, asset restructuring, and margin evidence before promotion.

---

## 9. Aggregate metrics

```json
{
  "row_type": "aggregate",
  "research_id": "R5L77_C19_RETAIL_INVENTORY_MARGIN_ROUTER",
  "round": "R5",
  "loop": 77,
  "large_sector_id": "L5_CONSUMER_BRAND_DISTRIBUTION",
  "canonical_archetype_id": "C19_BRAND_RETAIL_INVENTORY_MARGIN",
  "fine_archetype_id": "CONVENIENCE_DEPARTMENT_DISCOUNT_STORE_INVENTORY_MARGIN_LOW_MAE_AND_WEAK_MFE_ROUTER",
  "case_count": 4,
  "calibration_usable_case_count": 4,
  "positive_guarded_case_count": 2,
  "counterexample_count": 2,
  "new_symbol_count": 4,
  "source_proxy_only_count": 4,
  "evidence_url_pending_count": 4,
  "avg_mfe_30d_pct": 8.11,
  "avg_mae_30d_pct": -4.99,
  "avg_mfe_90d_pct": 8.84,
  "avg_mae_90d_pct": -9.54,
  "avg_mfe_180d_pct": 10.9,
  "avg_mae_180d_pct": -15.7,
  "max_mfe_180d_pct": 23.34,
  "worst_mae_180d_pct": -24.89
}
```

---

## 10. 4B proximity split

```json
{
  "row_type": "4b_split",
  "research_id": "R5L77_C19_RETAIL_INVENTORY_MARGIN_ROUTER",
  "stage2_guarded_or_yellow_candidate": [
    {
      "symbol": "007070",
      "reason": "retail-margin recovery path had +23.34% 180D MFE with only -0.96% MAE"
    },
    {
      "symbol": "004170",
      "reason": "department-store path had +13.20% first-window MFE but later drawdown caps at Stage2-Guarded"
    }
  ],
  "blocked_stage2_or_local_4b_watch": [
    {
      "symbol": "282330",
      "reason": "convenience-store margin label had only +3.34% 180D MFE and -24.89% 180D MAE"
    },
    {
      "symbol": "139480",
      "reason": "discount-store turnaround label had only +3.71% MFE and -24.73% 180D MAE"
    }
  ],
  "full_4b_or_green_requires_non_price_evidence": [
    "same-store sales and store traffic",
    "inventory turnover and markdown risk",
    "gross margin and promotion intensity",
    "store mix and channel mix",
    "duty-free / department-store recovery where relevant",
    "asset restructuring and working-capital conversion"
  ]
}
```

---

## 11. Shadow rule candidate

```yaml
row_type: canonical_archetype_rule_candidate
canonical_archetype_id: C19_BRAND_RETAIL_INVENTORY_MARGIN
fine_archetype_id: CONVENIENCE_DEPARTMENT_DISCOUNT_STORE_INVENTORY_MARGIN_LOW_MAE_AND_WEAK_MFE_ROUTER
rule_name: C19_convenience_department_discount_store_inventory_margin_low_mae_and_weak_mfe_router
production_scoring_changed: false
shadow_weight_only: true
```

### Proposed routing logic

```text
For C19 convenience-store / department-store / discount-store retail-margin cases:

Tier A: verified low-MAE retail-margin winner
  Conditions:
    - same-store sales, traffic, inventory turnover, gross margin, and working-capital evidence are URL-repaired
    - MFE_90D >= +10%
    - MAE_90D > -5%
  Routing:
    - Stage2-Guarded allowed
    - Stage3-Yellow allowed after evidence repair
    - Green only after store-traffic / inventory / margin bridge is verified

Tier B: first-window MFE with later drawdown
  Conditions:
    - MFE_30D >= +10%
    - MAE_180D <= -10%
    - evidence_url_pending or source_proxy_only remains true
  Routing:
    - Stage2-Guarded at most
    - no Green until evidence repair

Tier C: weak-MFE retail/value-up/inventory label
  Conditions:
    - MFE_90D < +5%
    - MAE_90D <= -15% or MAE_180D <= -20%
    - no repaired same-store / inventory / margin bridge
  Routing:
    - block Stage2
    - local 4B/high-MAE watch
```

### Suggested shadow delta

```json
{
  "row_type": "shadow_weight",
  "axis": "c19_convenience_department_discount_store_inventory_margin_low_mae_and_weak_mfe_router",
  "scope": "canonical_archetype_id:C19_BRAND_RETAIL_INVENTORY_MARGIN",
  "proposal": {
    "source_proxy_only_green_allowed": false,
    "retail_margin_label_alone_stage2_allowed": false,
    "same_store_inventory_margin_bridge_required_for_green": true,
    "verified_low_mae_retail_mfe90_threshold_pct": 10.0,
    "verified_low_mae_retail_mae90_min_pct": -5.0,
    "first_window_mfe_threshold_30d_pct": 10.0,
    "later_drawdown_mae180_threshold_pct": -10.0,
    "weak_mfe_threshold_90d_pct": 5.0,
    "weak_mfe_mae90_threshold_pct": -15.0,
    "weak_mfe_mae180_threshold_pct": -20.0,
    "positive_weight_blocked_until_url_repair": true
  },
  "confidence": "medium_low_until_url_repair",
  "apply_now": false,
  "reason": "Two retail-margin recovery holdouts and two weak-MFE retail/value-up/inventory-label failures show that C19 should require URL-repaired same-store sales, traffic, inventory turnover, gross margin, promotion intensity, and working-capital evidence before Yellow/Green."
}
```

---

## 12. Residual contribution summary

```json
{
  "row_type": "residual_contribution",
  "research_id": "R5L77_C19_RETAIL_INVENTORY_MARGIN_ROUTER",
  "large_sector_id": "L5_CONSUMER_BRAND_DISTRIBUTION",
  "canonical_archetype_id": "C19_BRAND_RETAIL_INVENTORY_MARGIN",
  "contribution": "Adds four non-top-covered C19 convenience-store / department-store / discount-store retail inventory-margin cases and separates low-MAE retail-margin recovery from weak-MFE retail/value-up/inventory-turnaround labels. C19 Yellow/Green should require URL-repaired same-store sales, traffic, inventory turnover, markdown risk, gross margin, promotion intensity, store/channel mix, asset restructuring, working capital, and cash-flow evidence.",
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
  "data_quality_blocker": "All four non-price retail/inventory-margin triggers require URL-level repair before positive weight promotion.",
  "guardrail_added": "C19 source_proxy_only retail labels with MFE_90D < +5% and MAE_90D <= -15% or MAE_180D <= -20% should block Stage2; low-MAE retail-margin recovery paths may remain Stage2-Guarded until same-store/inventory/margin evidence is repaired."
}
```

One-line contribution:

```text
This loop adds 4 new independent cases, 2 counterexamples, and 2 residual errors for R5/L5_CONSUMER_BRAND_DISTRIBUTION/C19_BRAND_RETAIL_INVENTORY_MARGIN.
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
    007070: false
    004170: false
    282330: false
    139480: false
  evidence_url_pending:
    007070: true
    004170: true
    282330: true
    139480: true
  source_proxy_only:
    007070: true
    004170: true
    282330: true
    139480: true
  special_handling:
    007070:
      corporate_action_candidate_after_window: "2024-12-23"
      note: "Selected 2024-04-18 entry plus 180D window ends before this candidate."
```

Limitations:

```text
- Price path is validated against Stock-Web tradable OHLC rows.
- Non-price evidence is not URL-repaired in this run.
- Therefore this artifact is useful for C19 retail inventory-margin residual shape and weak-MFE/high-MAE guardrail design, but should not promote positive weights until filings, IR, channel/retail sales data, or reports verify same-store sales, traffic, inventory turnover, markdown risk, gross margin, channel mix, asset restructuring, working capital, and cash-flow conversion.
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
2. Preserve R5 / loop 77 metadata.
3. Add the cases to C19_BRAND_RETAIL_INVENTORY_MARGIN only if parser validation passes.
4. Treat all four non-price triggers as evidence_url_pending=true and source_proxy_only=true until URL-level evidence is repaired.
5. Do not use these rows for positive weight promotion until filings/IR/channel-data/retail-sales/report data verifies same-store sales, store traffic, inventory turnover, markdown risk, gross margin, promotion intensity, store/channel mix, asset restructuring, working capital, and cash-flow conversion.
6. Add a shadow-only rule candidate named C19_convenience_department_discount_store_inventory_margin_low_mae_and_weak_mfe_router.
7. Do not loosen Stage3-Green.
8. Add C19-specific guards:
   - source_proxy_only -> no Green
   - retail margin label alone -> no Stage2 promotion
   - Green requires repaired same-store / inventory / margin bridge
   - MFE_90D >= +10% and MAE_90D > -5% may remain Stage2-Guarded / Yellow watch after evidence repair
   - MFE_30D >= +10% and MAE_180D <= -10% -> Stage2-Guarded at most until evidence repair
   - MFE_90D < +5% and MAE_90D <= -15% or MAE_180D <= -20% -> block Stage2 / local 4B watch
9. Keep production scoring unchanged unless later batch promotion logic independently marks this axis safe.
```

---

## 15. Next round state

```text
completed_round = R5
completed_loop = 77
next_round = R6
next_loop = 77
next_large_sector_hint = L6_FINANCIAL_CAPITAL_RETURN_DIGITAL
round_schedule_status = valid
round_sector_consistency = pass
```
