# E2R Stock-Web v12 Residual Research — R6 Loop 76

```yaml
research_session: post_calibrated_sector_archetype_residual_research
mode: historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12
completed_round: R6
completed_loop: 76
next_round: R7
next_loop: 76
large_sector_id: L6_FINANCIAL_CAPITAL_RETURN_DIGITAL
canonical_archetype_id: C22_INSURANCE_RATE_CYCLE_RESERVE
fine_archetype_id: NON_TOP_INSURER_VALUEUP_RATE_RESERVE_CAPITAL_AND_WEAK_MFE_ROUTER
output_file: e2r_stock_web_v12_residual_round_R6_loop_76_L6_FINANCIAL_CAPITAL_RETURN_DIGITAL_C22_INSURANCE_RATE_CYCLE_RESERVE_research.md
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
completed_round = R5
completed_loop  = 76
large_sector_id = L5_CONSUMER_BRAND_DISTRIBUTION
canonical_archetype_id = C18_CONSUMER_EXPORT_CHANNEL_REORDER
```

Therefore:

```text
scheduled_round = R6
scheduled_loop  = 76
```

R6 maps to:

```text
large_sector_id = L6_FINANCIAL_CAPITAL_RETURN_DIGITAL
```

This run selects:

```text
canonical_archetype_id = C22_INSURANCE_RATE_CYCLE_RESERVE
fine_archetype_id = NON_TOP_INSURER_VALUEUP_RATE_RESERVE_CAPITAL_AND_WEAK_MFE_ROUTER
```

This is a valid R6/L6 pairing.

---

## 1. Why this R6/C22 run

The no-repeat ledger shows C22 is heavily covered and concentrated in the top insurers:

```text
C22_INSURANCE_RATE_CYCLE_RESERVE:
  rows: 138
  symbols: 11
  date_range: 2023-05-15~2025-05-30
  good/bad S2: 45/20
  4B/4C: 22/5
  URL/proxy: 8/8
  top covered symbols: 000810(34), 005830(33), 088350(17), 001450(16), 000400(11), 032830(11)
```

This file avoids those top-covered names and tests smaller/non-top insurance and reinsurance paths:

```text
082640 동양생명
003690 코리안리
000370 한화손해보험
085620 미래에셋생명
```

Research question:

```text
Can C22 separate non-top insurer value-up / reserve / rate-cycle rerating from insurance policy labels where reserve-quality, capital-return execution, underwriting quality, and solvency evidence are not repaired and the path shows weak MFE or mid-window drawdown?
```

C22 is an insurance balance-sheet bridge. A value-up or rate-cycle label is only the headline premium. Stage2 needs the loss ratio, reserve confidence, CSM/earnings quality, solvency headroom, dividend/buyback policy, and capital-allocation proof. Without those, the policy label can float briefly and still leak risk through MAE.

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
| `082640` | 동양생명 | active_like / KOSPI | no 2024 overlap; latest listed candidate 2017-04-11 | true |
| `003690` | 코리안리 | active_like / KOSPI | no 2024 overlap; latest listed candidate 2004-07-20 | true |
| `000370` | 한화손해보험 | active_like / KOSPI | no 2024 overlap; latest listed candidate 2017-11-23 | true |
| `085620` | 미래에셋생명 | active_like / KOSPI | no 2024 overlap; latest listed candidate 2018-03-23 | true |

Profile caveat:

```text
Stock-Web OHLC is raw/unadjusted marcap data.
These cases are calibration-safe for the selected 2024 30D/90D/180D windows because no listed corporate-action candidate overlaps each entry~D+180 test window.
```

---

## 3. Event family and trigger discipline

### Event family

```text
event_family = Korea value-up / insurance rate-cycle / reserve-quality repricing
trigger_date = 2024-02-26
entry_rule = next_tradable_open_to_avoid_same_day_lookahead
entry_date = 2024-02-27
canonical_archetype_id = C22_INSURANCE_RATE_CYCLE_RESERVE
fine_archetype_id = NON_TOP_INSURER_VALUEUP_RATE_RESERVE_CAPITAL_AND_WEAK_MFE_ROUTER
```

This artifact intentionally marks non-price evidence as conservative:

```text
evidence_url_pending = true
source_proxy_only = true
```

Reason:

```text
The Stock-Web price path is fully validated, but company-level reserve adequacy, CSM/earnings quality, loss ratio, underwriting cycle, solvency ratio, shareholder-return policy, dividend/buyback execution, and capital-allocation evidence still require URL repair through filings, IR, actuarial/reserve disclosures, or sell-side reports before production weight promotion.
```

---

## 4. No-repeat and novelty check

Hard duplicate key:

```text
canonical_archetype_id + symbol + trigger_type + entry_date
```

Targeted repository searches before writing:

```text
000370 + C22_INSURANCE_RATE_CYCLE_RESERVE -> no direct match found
003690 + C22_INSURANCE_RATE_CYCLE_RESERVE -> no direct match found
082640 + C22_INSURANCE_RATE_CYCLE_RESERVE -> no direct match found
085620 + C22_INSURANCE_RATE_CYCLE_RESERVE -> no direct match found
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
| `R6L76_C22_082640_20240227` | `082640` 동양생명 | life insurer value-up / reserve / capital-policy high-MFE path | positive-guarded |
| `R6L76_C22_003690_20240227` | `003690` 코리안리 | reinsurance rate-cycle / capital-return low-MAE slow rerating | positive-guarded low-MAE |
| `R6L76_C22_000370_20240227` | `000370` 한화손해보험 | nonlife insurer reserve/rate value-up with mid-window drawdown | guarded counterexample |
| `R6L76_C22_085620_20240227` | `085620` 미래에셋생명 | life insurer value-up policy label with weak MFE/drawdown | weak-MFE counterexample |

The intended residual:

```text
C22 should separate:
1. non-top insurer cases where value-up/rate-cycle relevance becomes real MFE;
2. reinsurance low-MAE paths that are only Stage2-Guarded unless capital-return and underwriting evidence is repaired;
3. insurer policy labels that draw down before the reserve/capital bridge is proven;
4. weak-MFE life-insurance labels where policy relevance alone does not create Stage2 return alignment.
```

---

## 6. Stock-Web OHLC and backtest

### 6.1 `082640` 동양생명 — life insurer value-up / reserve high-MFE guarded path

Trigger:

```text
trigger_date = 2024-02-26
trigger_type = Stage2-Actionable-Guarded
trigger_family = life_insurance_valueup_rate_reserve_capital_policy_high_mfe_guarded
entry_date = 2024-02-27
entry_price = 5360.0
entry_price_type = next_tradable_open_after_insurance_valueup_rate_reserve_burst
```

Relevant Stock-Web rows:

```csv
d,o,h,l,c,v,a,mc,s,m
2024-02-26,5380.0,5480.0,5200.0,5360.0,548813.0,2914672910.0,864882015600.0,161358585,KOSPI
2024-02-27,5360.0,5420.0,5230.0,5300.0,346701.0,1850882920.0,855200500500.0,161358585,KOSPI
2024-03-08,6390.0,6500.0,6320.0,6350.0,472273.0,3030546620.0,1024627014750.0,161358585,KOSPI
2024-04-19,4930.0,4970.0,4830.0,4970.0,150983.0,739709400.0,801952167450.0,161358585,KOSPI
2024-06-28,7060.0,8220.0,7040.0,7820.0,7868539.0,60414969290.0,1261824134700.0,161358585,KOSPI
2024-07-31,7930.0,9440.0,7710.0,7970.0,2952682.0,25466445060.0,1286027922450.0,161358585,KOSPI
2024-08-05,8400.0,8460.0,7700.0,7920.0,710136.0,5738705380.0,1277959993200.0,161358585,KOSPI
2024-08-23,8290.0,8410.0,8180.0,8400.0,195186.0,1623960620.0,1355412114000.0,161358585,KOSPI
```

Backtest:

| window | peak/high | peak date | trough/low | trough date | MFE | MAE |
|---|---:|---|---:|---|---:|---:|
| 30 calendar days | 6500 | 2024-03-08 | 5230 | 2024-02-27 | +21.27% | -2.43% |
| 90 calendar days | 6500 | 2024-03-08 | 4830 | 2024-04-19 | +21.27% | -9.89% |
| 180 calendar days | 9440 | 2024-07-31 | 4830 | 2024-04-19 | +76.12% | -9.89% |

Interpretation:

```text
082640 is the non-top C22 positive holdout.
The value-up / insurance reserve-rate label produced real 180D MFE while staying just inside a manageable MAE band.
It can remain Stage2-Guarded / Yellow-after-repair, but Green still requires URL-repaired reserve, CSM/earnings, solvency, and shareholder-return evidence.
```

### 6.2 `003690` 코리안리 — reinsurance rate-cycle low-MAE slow rerating

Trigger:

```text
trigger_date = 2024-02-26
trigger_type = Stage2-Actionable-Guarded
trigger_family = reinsurance_rate_cycle_capital_return_low_mae_slow_rerating
entry_date = 2024-02-27
entry_price = 7900.0
entry_price_type = next_tradable_open_after_reinsurance_rate_cycle_valueup_burst
```

Relevant Stock-Web rows:

```csv
d,o,h,l,c,v,a,mc,s,m
2024-02-26,7970.0,8000.0,7850.0,7930.0,310946.0,2456701560.0,1311364481180.0,165367526,KOSPI
2024-02-27,7900.0,8030.0,7880.0,7910.0,277777.0,2214036630.0,1308057130660.0,165367526,KOSPI
2024-03-22,8360.0,8550.0,8340.0,8510.0,486073.0,4105826600.0,1407277646260.0,165367526,KOSPI
2024-04-15,7600.0,7650.0,7500.0,7630.0,349456.0,2653812270.0,1261754223380.0,165367526,KOSPI
2024-07-18,7980.0,8350.0,7920.0,8340.0,930436.0,7682142000.0,1379165166840.0,165367526,KOSPI
2024-08-20,8850.0,8960.0,8800.0,8890.0,253386.0,2257527400.0,1470117306140.0,165367526,KOSPI
2024-08-23,8830.0,8960.0,8800.0,8900.0,160446.0,1431003880.0,1471770981400.0,165367526,KOSPI
```

Backtest:

| window | peak/high | peak date | trough/low | trough date | MFE | MAE |
|---|---:|---|---:|---|---:|---:|
| 30 calendar days | 8550 | 2024-03-22 | 7870 | 2024-02-28 | +8.23% | -0.38% |
| 90 calendar days | 8550 | 2024-03-22 | 7500 | 2024-04-15 | +8.23% | -5.06% |
| 180 calendar days | 8960 | 2024-08-23 | 7500 | 2024-04-15 | +13.42% | -5.06% |

Interpretation:

```text
003690 is a low-MAE but modest-MFE C22 holdout.
It is not a Green-quality explosive case, but it preserves capital and eventually trends higher.
This supports Stage2-Guarded only until reinsurance pricing, reserve adequacy, underwriting margin, and capital-return evidence is repaired.
```

### 6.3 `000370` 한화손해보험 — nonlife reserve/rate value-up mid-window drawdown

Trigger:

```text
trigger_date = 2024-02-26
trigger_type = Stage2-Actionable-Guarded
trigger_family = nonlife_insurance_reserve_rate_valueup_drawdown_watch
entry_date = 2024-02-27
entry_price = 4880.0
entry_price_type = next_tradable_open_after_nonlife_insurance_valueup_rate_burst
```

Relevant Stock-Web rows:

```csv
d,o,h,l,c,v,a,mc,s,m
2024-02-26,5380.0,5410.0,4845.0,4930.0,3744870.0,18750371465.0,575522850950.0,116738915,KOSPI
2024-02-27,4880.0,4940.0,4650.0,4675.0,2145844.0,10166064440.0,545754427625.0,116738915,KOSPI
2024-03-15,5040.0,5260.0,4940.0,4945.0,1683507.0,8539991960.0,577273934675.0,116738915,KOSPI
2024-04-15,4105.0,4275.0,4085.0,4265.0,295165.0,1237150110.0,497891472475.0,116738915,KOSPI
2024-05-16,5070.0,5390.0,5070.0,5230.0,1056416.0,5537962640.0,610544525450.0,116738915,KOSPI
2024-07-31,5390.0,5720.0,5360.0,5650.0,1793708.0,10068154500.0,659574869750.0,116738915,KOSPI
2024-08-20,5840.0,6230.0,5810.0,6190.0,2000903.0,12168169080.0,722613883850.0,116738915,KOSPI
```

Backtest:

| window | peak/high | peak date | trough/low | trough date | MFE | MAE |
|---|---:|---|---:|---|---:|---:|
| 30 calendar days | 5260 | 2024-03-15 | 4510 | 2024-03-28 | +7.79% | -7.58% |
| 90 calendar days | 5390 | 2024-05-16 | 4085 | 2024-04-15 | +10.45% | -16.29% |
| 180 calendar days | 6230 | 2024-08-20 | 4085 | 2024-04-15 | +27.66% | -16.29% |

Interpretation:

```text
000370 is a guarded counterexample rather than a hard failure.
The later 180D MFE improved, but the path first absorbed a -16.29% drawdown.
C22 should cap this at Stage2-Guarded or local 4B watch until reserve adequacy, loss ratio, solvency, and capital-return execution evidence is repaired.
```

### 6.4 `085620` 미래에셋생명 — life-insurance value-up policy label with weak early MFE

Trigger:

```text
trigger_date = 2024-02-26
trigger_type = Stage2-FalsePositive-Candidate
trigger_family = life_insurance_valueup_policy_label_weak_mfe_drawdown
entry_date = 2024-02-27
entry_price = 5220.0
entry_price_type = next_tradable_open_after_life_insurance_valueup_policy_label
```

Relevant Stock-Web rows:

```csv
d,o,h,l,c,v,a,mc,s,m
2024-02-26,5250.0,5280.0,5100.0,5260.0,288254.0,1493994670.0,931105154140.0,177016189,KOSPI
2024-02-27,5220.0,5370.0,5040.0,5130.0,360644.0,1881375160.0,908093049570.0,177016189,KOSPI
2024-03-20,4550.0,4560.0,4500.0,4500.0,159661.0,721617945.0,796572850500.0,177016189,KOSPI
2024-04-02,4535.0,4535.0,4425.0,4490.0,124180.0,556531920.0,794802688610.0,177016189,KOSPI
2024-05-16,5320.0,5560.0,5260.0,5460.0,218842.0,1200160990.0,966508391940.0,177016189,KOSPI
2024-06-27,4910.0,6140.0,4855.0,5350.0,2767280.0,15163281775.0,947036611150.0,177016189,KOSPI
2024-08-05,5050.0,5090.0,4660.0,4950.0,444427.0,2196450515.0,876230135550.0,177016189,KOSPI
```

Backtest:

| window | peak/high | peak date | trough/low | trough date | MFE | MAE |
|---|---:|---|---:|---|---:|---:|
| 30 calendar days | 5370 | 2024-02-27 | 4470 | 2024-03-19 | +2.87% | -14.37% |
| 90 calendar days | 5560 | 2024-05-16 | 4425 | 2024-04-02 | +6.51% | -15.23% |
| 180 calendar days | 6140 | 2024-06-27 | 4425 | 2024-04-02 | +17.62% | -15.23% |

Interpretation:

```text
085620 is the weak-MFE C22 counterexample.
The value-up/insurance label existed, but the entry gave poor early MFE and a double-digit drawdown before any durable rerating.
This should block Green and usually block Stage2 unless a later independent trigger repairs capital-return, reserve quality, and earnings-quality evidence.
```

---

## 7. Machine-readable trigger JSONL

```jsonl
{"row_type":"trigger","research_id":"R6L76_C22_NON_TOP_INSURER_RATE_RESERVE_ROUTER","round":"R6","loop":76,"large_sector_id":"L6_FINANCIAL_CAPITAL_RETURN_DIGITAL","canonical_archetype_id":"C22_INSURANCE_RATE_CYCLE_RESERVE","fine_archetype_id":"NON_TOP_INSURER_VALUEUP_RATE_RESERVE_CAPITAL_AND_WEAK_MFE_ROUTER","symbol":"082640","name":"동양생명","trigger_type":"Stage2-Actionable-Guarded","trigger_family":"life_insurance_valueup_rate_reserve_capital_policy_high_mfe_guarded","trigger_date":"2024-02-26","entry_date":"2024-02-27","entry_price":5360.0,"entry_price_type":"next_tradable_open_after_insurance_valueup_rate_reserve_burst","price_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","mfe_30d_pct":21.27,"mae_30d_pct":-2.43,"mfe_90d_pct":21.27,"mae_90d_pct":-9.89,"mfe_180d_pct":76.12,"mae_180d_pct":-9.89,"peak_price_180d":9440.0,"peak_date_180d":"2024-07-31","trough_price_180d":4830.0,"trough_date_180d":"2024-04-19","calibration_usable":true,"case_polarity":"positive_guarded_life_insurance_high_mfe","evidence_url_pending":true,"source_proxy_only":true,"non_price_evidence_strength":"medium_pending_url_repair","price_only_blowoff":false,"expected_stage_current_profile":"Stage2-Guarded_to_Yellow_if_reserve_capital_return_earnings_quality_bridge_repaired","residual_error_type":"life_insurance_valueup_rate_reserve_path_had_high_mfe_but_green_requires_url_repaired_reserve_capital_and_shareholder_return_bridge"}
{"row_type":"trigger","research_id":"R6L76_C22_NON_TOP_INSURER_RATE_RESERVE_ROUTER","round":"R6","loop":76,"large_sector_id":"L6_FINANCIAL_CAPITAL_RETURN_DIGITAL","canonical_archetype_id":"C22_INSURANCE_RATE_CYCLE_RESERVE","fine_archetype_id":"NON_TOP_INSURER_VALUEUP_RATE_RESERVE_CAPITAL_AND_WEAK_MFE_ROUTER","symbol":"003690","name":"코리안리","trigger_type":"Stage2-Actionable-Guarded","trigger_family":"reinsurance_rate_cycle_capital_return_low_mae_slow_rerating","trigger_date":"2024-02-26","entry_date":"2024-02-27","entry_price":7900.0,"entry_price_type":"next_tradable_open_after_reinsurance_rate_cycle_valueup_burst","price_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","mfe_30d_pct":8.23,"mae_30d_pct":-0.38,"mfe_90d_pct":8.23,"mae_90d_pct":-5.06,"mfe_180d_pct":13.42,"mae_180d_pct":-5.06,"peak_price_180d":8960.0,"peak_date_180d":"2024-08-23","trough_price_180d":7500.0,"trough_date_180d":"2024-04-15","calibration_usable":true,"case_polarity":"positive_guarded_low_mae_reinsurance","evidence_url_pending":true,"source_proxy_only":true,"non_price_evidence_strength":"medium_low_pending_url_repair","price_only_blowoff":false,"expected_stage_current_profile":"Stage2-Guarded_only_until_reinsurance_rate_reserve_capital_return_bridge_repaired","residual_error_type":"reinsurance_rate_cycle_path_preserved_mae_but_mfe_was_modest_without_stronger_capital_return_and_underwriting_bridge"}
{"row_type":"trigger","research_id":"R6L76_C22_NON_TOP_INSURER_RATE_RESERVE_ROUTER","round":"R6","loop":76,"large_sector_id":"L6_FINANCIAL_CAPITAL_RETURN_DIGITAL","canonical_archetype_id":"C22_INSURANCE_RATE_CYCLE_RESERVE","fine_archetype_id":"NON_TOP_INSURER_VALUEUP_RATE_RESERVE_CAPITAL_AND_WEAK_MFE_ROUTER","symbol":"000370","name":"한화손해보험","trigger_type":"Stage2-Actionable-Guarded","trigger_family":"nonlife_insurance_reserve_rate_valueup_drawdown_watch","trigger_date":"2024-02-26","entry_date":"2024-02-27","entry_price":4880.0,"entry_price_type":"next_tradable_open_after_nonlife_insurance_valueup_rate_burst","price_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","mfe_30d_pct":7.79,"mae_30d_pct":-7.58,"mfe_90d_pct":10.45,"mae_90d_pct":-16.29,"mfe_180d_pct":27.66,"mae_180d_pct":-16.29,"peak_price_180d":6230.0,"peak_date_180d":"2024-08-20","trough_price_180d":4085.0,"trough_date_180d":"2024-04-15","calibration_usable":true,"case_polarity":"counterexample_guarded_mid_window_drawdown","evidence_url_pending":true,"source_proxy_only":true,"non_price_evidence_strength":"medium_low_pending_url_repair","price_only_blowoff":false,"expected_stage_current_profile":"Stage2-Guarded_or_local_4B_watch_until_reserve_capital_return_bridge_repaired","residual_error_type":"nonlife_insurance_valueup_label_had_mid_window_drawdown_before_later_mfe_without_repaired_reserve_capital_bridge"}
{"row_type":"trigger","research_id":"R6L76_C22_NON_TOP_INSURER_RATE_RESERVE_ROUTER","round":"R6","loop":76,"large_sector_id":"L6_FINANCIAL_CAPITAL_RETURN_DIGITAL","canonical_archetype_id":"C22_INSURANCE_RATE_CYCLE_RESERVE","fine_archetype_id":"NON_TOP_INSURER_VALUEUP_RATE_RESERVE_CAPITAL_AND_WEAK_MFE_ROUTER","symbol":"085620","name":"미래에셋생명","trigger_type":"Stage2-FalsePositive-Candidate","trigger_family":"life_insurance_valueup_policy_label_weak_mfe_drawdown","trigger_date":"2024-02-26","entry_date":"2024-02-27","entry_price":5220.0,"entry_price_type":"next_tradable_open_after_life_insurance_valueup_policy_label","price_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","mfe_30d_pct":2.87,"mae_30d_pct":-14.37,"mfe_90d_pct":6.51,"mae_90d_pct":-15.23,"mfe_180d_pct":17.62,"mae_180d_pct":-15.23,"peak_price_180d":6140.0,"peak_date_180d":"2024-06-27","trough_price_180d":4425.0,"trough_date_180d":"2024-04-02","calibration_usable":true,"case_polarity":"counterexample_weak_mfe_drawdown","evidence_url_pending":true,"source_proxy_only":true,"non_price_evidence_strength":"low_pending_url_repair","price_only_blowoff":false,"expected_stage_current_profile":"blocked_Stage2_or_Stage2_Guarded_until_reserve_capital_return_execution_bridge_repaired","residual_error_type":"life_insurance_valueup_policy_label_had_weak_early_mfe_and_drawdown_without_capital_return_or_reserve_quality_bridge"}
```

---

## 8. Score simulation and raw component breakdown

This is shadow-only and does not change production scoring.

| symbol | reserve / CSM quality | underwriting / loss ratio | rate-cycle leverage | solvency / capital headroom | market mispricing | shareholder return | information confidence | shadow total | intended route |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| `082640` | 10 | 8 | 10 | 9 | 13 | 8 | 6 | 64 | Stage2-Guarded / Yellow after evidence repair |
| `003690` | 9 | 9 | 8 | 8 | 6 | 6 | 6 | 52 | Stage2-Guarded only until evidence repair |
| `000370` | 7 | 6 | 7 | 5 | 7 | 4 | 5 | 41 | Stage2-Guarded or local 4B watch |
| `085620` | 5 | 4 | 5 | 4 | 3 | 3 | 5 | 29 | blocked Stage2 or guarded after fresh bridge |

### Current calibrated profile stress test

The current calibrated profile already blocks pure price-only blowoff.  
The remaining C22 issue is **insurance value-up/rate-cycle label without reserve/capital execution**:

```text
C22 high-MFE non-top insurer path:
  value-up / rate-cycle / reserve relevance
  + MFE_180D expands materially
  + 90D MAE remains better than -10%
  + evidence remains source_proxy_only
  => Stage2-Guarded; Yellow only after reserve/capital-return evidence repair

C22 low-MAE slow rerating:
  rate-cycle relevance exists
  + MAE stays controlled
  + MFE is modest
  => Stage2-Guarded at most, no Green

C22 mid-window drawdown:
  later MFE appears
  + MAE_90D <= -15%
  + reserve/capital bridge remains unrepaired
  => Stage2-Guarded or local 4B watch

C22 weak early MFE:
  MFE_90D < +10%
  + MAE_30D <= -10%
  + no reserve/capital-return bridge
  => block Green and usually block Stage2
```

`082640` and `003690` prevent overblocking.  
`000370` shows why later MFE cannot erase a mid-window drawdown without evidence repair.  
`085620` shows why insurance value-up policy relevance alone cannot create Stage2 return alignment.

---

## 9. Aggregate metrics

```json
{
  "row_type": "aggregate",
  "research_id": "R6L76_C22_NON_TOP_INSURER_RATE_RESERVE_ROUTER",
  "round": "R6",
  "loop": 76,
  "large_sector_id": "L6_FINANCIAL_CAPITAL_RETURN_DIGITAL",
  "canonical_archetype_id": "C22_INSURANCE_RATE_CYCLE_RESERVE",
  "fine_archetype_id": "NON_TOP_INSURER_VALUEUP_RATE_RESERVE_CAPITAL_AND_WEAK_MFE_ROUTER",
  "case_count": 4,
  "calibration_usable_case_count": 4,
  "positive_guarded_case_count": 2,
  "counterexample_count": 2,
  "new_symbol_count": 4,
  "source_proxy_only_count": 4,
  "evidence_url_pending_count": 4,
  "avg_mfe_30d_pct": 10.04,
  "avg_mae_30d_pct": -6.19,
  "avg_mfe_90d_pct": 11.62,
  "avg_mae_90d_pct": -11.62,
  "avg_mfe_180d_pct": 33.71,
  "avg_mae_180d_pct": -11.62,
  "max_mfe_180d_pct": 76.12,
  "worst_mae_180d_pct": -16.29
}
```

---

## 10. 4B proximity split

```json
{
  "row_type": "4b_split",
  "research_id": "R6L76_C22_NON_TOP_INSURER_RATE_RESERVE_ROUTER",
  "stage2_guarded_or_yellow_candidate": [
    {
      "symbol": "082640",
      "reason": "non-top life insurer path had +76.12% 180D MFE with 90D MAE just inside -10%; requires reserve/capital bridge repair"
    },
    {
      "symbol": "003690",
      "reason": "reinsurance rate-cycle path had low MAE but modest MFE; suitable only as Stage2-Guarded pending evidence repair"
    }
  ],
  "stage2_guarded_or_local_4b_watch": [
    {
      "symbol": "000370",
      "reason": "later MFE improved, but 90D/180D MAE reached -16.29% before reserve/capital bridge repair"
    }
  ],
  "blocked_stage2_or_weak_mfe_watch": [
    {
      "symbol": "085620",
      "reason": "MFE_90D stayed only +6.51% while 30D MAE already reached -14.37%"
    }
  ],
  "full_4b_or_green_requires_non_price_evidence": [
    "reserve adequacy and CSM / earnings quality",
    "underwriting margin and loss-ratio trend",
    "rate-cycle leverage",
    "solvency ratio / capital headroom",
    "dividend / buyback / shareholder-return execution",
    "asset-liability and investment spread risk"
  ]
}
```

---

## 11. Shadow rule candidate

```yaml
row_type: canonical_archetype_rule_candidate
canonical_archetype_id: C22_INSURANCE_RATE_CYCLE_RESERVE
fine_archetype_id: NON_TOP_INSURER_VALUEUP_RATE_RESERVE_CAPITAL_AND_WEAK_MFE_ROUTER
rule_name: C22_non_top_insurer_rate_reserve_capital_and_weak_mfe_router
production_scoring_changed: false
shadow_weight_only: true
```

### Proposed routing logic

```text
For C22 non-top insurer / reinsurer value-up, reserve, and rate-cycle cases:

Tier A: verified non-top insurer rerating
  Conditions:
    - reserve adequacy, CSM/earnings quality, solvency, and shareholder-return evidence are URL-repaired
    - MFE_180D >= +30%
    - MAE_90D > -10%
  Routing:
    - Stage2-Guarded allowed
    - Stage3-Yellow allowed after evidence repair
    - Green only after reserve / capital / underwriting bridge is verified

Tier B: low-MAE slow rerating
  Conditions:
    - MFE_180D >= +10%
    - MAE_180D > -8%
    - evidence remains source_proxy_only
  Routing:
    - Stage2-Guarded at most
    - no Green until evidence repair

Tier C: later-MFE with mid-window drawdown
  Conditions:
    - MFE_180D >= +15%
    - MAE_90D <= -15%
    - reserve/capital evidence remains unrepaired
  Routing:
    - Stage2-Guarded or local 4B watch
    - no Yellow/Green

Tier D: weak-MFE insurance value-up label
  Conditions:
    - MFE_90D < +10%
    - MAE_30D <= -10%
    - no repaired reserve/capital-return bridge
  Routing:
    - block Green
    - block Stage2 or narrative-only until a later independent trigger appears
```

### Suggested shadow delta

```json
{
  "row_type": "shadow_weight",
  "axis": "c22_non_top_insurer_rate_reserve_capital_and_weak_mfe_router",
  "scope": "canonical_archetype_id:C22_INSURANCE_RATE_CYCLE_RESERVE",
  "proposal": {
    "source_proxy_only_green_allowed": false,
    "reserve_csm_solvency_shareholder_return_bridge_required_for_green": true,
    "verified_non_top_insurer_mfe180_threshold_pct": 30.0,
    "verified_non_top_insurer_mae90_min_pct": -10.0,
    "low_mae_slow_rerating_mfe180_threshold_pct": 10.0,
    "low_mae_slow_rerating_mae180_min_pct": -8.0,
    "mid_window_drawdown_mfe180_threshold_pct": 15.0,
    "mid_window_drawdown_mae90_threshold_pct": -15.0,
    "weak_mfe_threshold_90d_pct": 10.0,
    "weak_mfe_mae30_threshold_pct": -10.0,
    "positive_weight_blocked_until_url_repair": true
  },
  "confidence": "medium_low_until_url_repair",
  "apply_now": false,
  "reason": "Two non-top insurer/reinsurer holdouts and two weak-MFE or drawdown cases show that C22 should require URL-repaired reserve adequacy, CSM/earnings quality, solvency, underwriting margin, and shareholder-return evidence before Yellow/Green."
}
```

---

## 12. Residual contribution summary

```json
{
  "row_type": "residual_contribution",
  "research_id": "R6L76_C22_NON_TOP_INSURER_RATE_RESERVE_ROUTER",
  "large_sector_id": "L6_FINANCIAL_CAPITAL_RETURN_DIGITAL",
  "canonical_archetype_id": "C22_INSURANCE_RATE_CYCLE_RESERVE",
  "contribution": "Adds four non-top C22 insurer/reinsurer value-up/rate/reserve cases and separates high-MFE or low-MAE holdouts from mid-window-drawdown and weak-MFE insurance value-up label failures. C22 Yellow/Green should require URL-repaired reserve adequacy, CSM/earnings quality, underwriting margin, solvency, shareholder-return, and investment-spread evidence.",
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
  "data_quality_blocker": "All four non-price insurance/rate/reserve triggers require URL-level repair before positive weight promotion.",
  "guardrail_added": "C22 source_proxy_only cases with MFE_90D < +10% and MAE_30D <= -10% should block Green and usually block Stage2; later-MFE cases with MAE_90D <= -15% should cap at Stage2-Guarded or local 4B until reserve/capital evidence is repaired."
}
```

One-line contribution:

```text
This loop adds 4 new independent cases, 2 counterexamples, and 2 residual errors for R6/L6_FINANCIAL_CAPITAL_RETURN_DIGITAL/C22_INSURANCE_RATE_CYCLE_RESERVE.
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
    082640: false
    003690: false
    000370: false
    085620: false
  evidence_url_pending:
    082640: true
    003690: true
    000370: true
    085620: true
  source_proxy_only:
    082640: true
    003690: true
    000370: true
    085620: true
```

Limitations:

```text
- Price path is validated against Stock-Web tradable OHLC rows.
- Non-price evidence is not URL-repaired in this run.
- Therefore this artifact is useful for C22 non-top insurer/reinsurer residual shape and weak-MFE/drawdown guardrail design, but should not promote positive weights until filings, IR, actuarial/reserve disclosures, capital-policy disclosures, or reports verify reserve adequacy, CSM/earnings quality, underwriting margin, solvency, shareholder return, and investment-spread risk.
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
2. Preserve R6 / loop 76 metadata.
3. Add the cases to C22_INSURANCE_RATE_CYCLE_RESERVE only if parser validation passes.
4. Treat all four non-price triggers as evidence_url_pending=true and source_proxy_only=true until URL-level evidence is repaired.
5. Do not use these rows for positive weight promotion until filings/IR/actuarial-reserve/capital-policy/report data verifies reserve adequacy, CSM/earnings quality, underwriting margin, solvency, shareholder return, and investment-spread risk.
6. Add a shadow-only rule candidate named C22_non_top_insurer_rate_reserve_capital_and_weak_mfe_router.
7. Do not loosen Stage3-Green.
8. Add C22-specific guards:
   - source_proxy_only -> no Green
   - Green requires repaired reserve / CSM / solvency / shareholder-return bridge
   - MFE_180D >= +30% and MAE_90D > -10% may remain Stage2-Guarded / Yellow watch after evidence repair
   - MFE_180D >= +10% and MAE_180D > -8% may remain Stage2-Guarded only
   - MFE_180D >= +15% and MAE_90D <= -15% -> Stage2-Guarded or local 4B watch; no Yellow/Green
   - MFE_90D < +10% and MAE_30D <= -10% -> block Green and usually block Stage2 unless a later independent trigger repairs evidence
9. Keep production scoring unchanged unless later batch promotion logic independently marks this axis safe.
```

---

## 15. Next round state

```text
completed_round = R6
completed_loop = 76
next_round = R7
next_loop = 76
next_large_sector_hint = L7_BIO_HEALTHCARE_MEDICAL
round_schedule_status = valid
round_sector_consistency = pass
```
