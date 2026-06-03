# E2R Stock-Web v12 Residual Research — R6 Loop 75

```yaml
research_session: post_calibrated_sector_archetype_residual_research
mode: historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12
completed_round: R6
completed_loop: 75
next_round: R7
next_loop: 75
large_sector_id: L6_FINANCIAL_CAPITAL_RETURN_DIGITAL
canonical_archetype_id: C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN
fine_archetype_id: BROKERAGE_CAPITAL_RETURN_ROE_VALUEUP_AND_WEAK_MFE_BALANCE_SHEET_ROUTER
output_file: e2r_stock_web_v12_residual_round_R6_loop_75_L6_FINANCIAL_CAPITAL_RETURN_DIGITAL_C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN_research.md
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
completed_loop  = 75
large_sector_id = L5_CONSUMER_BRAND_DISTRIBUTION
canonical_archetype_id = C19_BRAND_RETAIL_INVENTORY_MARGIN
```

Therefore:

```text
scheduled_round = R6
scheduled_loop  = 75
```

R6 maps to:

```text
large_sector_id = L6_FINANCIAL_CAPITAL_RETURN_DIGITAL
```

This run selects:

```text
canonical_archetype_id = C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN
fine_archetype_id = BROKERAGE_CAPITAL_RETURN_ROE_VALUEUP_AND_WEAK_MFE_BALANCE_SHEET_ROUTER
```

This is a valid R6/L6 pairing.

---

## 1. Why this R6/C21 run

The no-repeat ledger shows C21 is heavily covered and bank-heavy:

```text
C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN:
  rows: 209
  symbols: 26
  date_range: 2021-08-06~2025-05-26
  good/bad S2: 73/20
  4B/4C: 29/5
  URL/proxy: 0/0
  top covered symbols: 105560(56), 323410(31), 086790(26), UNKNOWN_SYMBOL(21), 006220(16), 055550(9)
```

This file avoids those top-covered bank symbols and tests brokerage / securities-holdco value-up paths:

```text
039490 키움증권
071050 한국금융지주
016360 삼성증권
006800 미래에셋증권
```

Research question:

```text
Can C21 separate brokerage ROE / capital-return rerating from brokerage value-up labels where the post-entry path has only weak MFE unless ROE, shareholder-return, and balance-sheet evidence are repaired?
```

C21 is a financial capital-return archetype. The policy wind can lift financials, but the actual hull is ROE, excess capital, shareholder-return policy, earnings quality, risk assets, and balance-sheet trust. If the hull is heavy, a low-PBR label floats only briefly.

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
| `039490` | 키움증권 | active_like / KOSPI | no 2024 overlap; old 2008 candidate only | true |
| `071050` | 한국금융지주 | active_like / KOSPI | none listed | true |
| `016360` | 삼성증권 | active_like / KOSPI | no 2024 overlap; old 1997~2001 candidates only | true |
| `006800` | 미래에셋증권 | active_like / KOSPI | no 2024 overlap; latest listed candidate 2017-01-20 | true |

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
The Stock-Web price path is fully validated, but company-level ROE durability, shareholder-return policy, dividend/buyback execution, excess capital, brokerage commission cycle, IB/PF exposure, ELS or overseas-risk asset drag, and balance-sheet quality evidence still require later URL repair through filings, IR decks, capital policy disclosures, or sell-side reports before production weight promotion.
```

C21 interpretation used here:

```text
C21 is not simply “financial stock rose.”
It asks whether financial rerating is capital-return convertible:
- ROE and earnings quality,
- capital adequacy and excess capital,
- dividend / buyback / total shareholder return,
- valuation discount closure,
- risk-asset and balance-sheet trust,
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
039490 + C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN -> no direct match found
071050 + C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN -> no direct match found
016360 + C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN -> no direct match found
006800 + C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN -> no direct match found
```

Novelty accounting:

```json
{
  "new_symbol_count": 4,
  "minimum_new_symbol_count": 2,
  "positive_case_count": 2,
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
| `R6L75_C21_039490_20240202` | `039490` 키움증권 | brokerage value-up / ROE / capital-return rerating | positive anchor |
| `R6L75_C21_071050_20240202` | `071050` 한국금융지주 | securities-holdco discount closure / low-MAE rerating | positive-guarded |
| `R6L75_C21_016360_20240202` | `016360` 삼성증권 | brokerage dividend/value-up weak early MFE and drawdown watch | guarded counterexample |
| `R6L75_C21_006800_20240202` | `006800` 미래에셋증권 | large-brokerage value-up label with weak MFE / balance-sheet drag | weak-MFE counterexample |

The intended residual:

```text
C21 should separate:
1. brokerage ROE/capital-return paths with persistent low-MAE MFE;
2. securities-holdco discount closure paths that work but still require capital-allocation proof;
3. brokerage value-up labels that need evidence repair because MFE is weak or drawdown widens before the bridge is proven.
```

---

## 6. Stock-Web OHLC and backtest

### 6.1 `039490` 키움증권 — brokerage value-up / ROE capital-return rerating

Trigger:

```text
trigger_date = 2024-02-01
trigger_type = Stage2-Actionable
trigger_family = brokerage_valueup_roe_capital_return_low_mae_rerating
entry_date = 2024-02-02
entry_price = 107300.0
entry_price_type = next_tradable_open_after_financial_valueup_brokerage_burst
```

Relevant Stock-Web rows:

```csv
d,o,h,l,c,v,a,mc,s,m
2024-02-01,96100.0,108200.0,96100.0,107600.0,300681.0,31664789100.0,2821993565600.0,26226706,KOSPI
2024-02-02,107300.0,113800.0,105500.0,112200.0,197312.0,21719104200.0,2942636413200.0,26226706,KOSPI
2024-02-23,122700.0,127500.0,121200.0,126400.0,158770.0,20017684200.0,3315055638400.0,26226706,KOSPI
2024-03-05,130100.0,135900.0,130000.0,134800.0,113712.0,15282958400.0,3535359968800.0,26226706,KOSPI
2024-03-15,133800.0,136600.0,129600.0,131300.0,107076.0,14162349900.0,3443566497800.0,26226706,KOSPI
2024-07-11,139900.0,146200.0,138100.0,144600.0,143375.0,20650017600.0,3691161687600.0,25526706,KOSPI
2024-08-05,123500.0,124000.0,115200.0,118500.0,107170.0,12829777600.0,3024914661000.0,25526706,KOSPI
```

Backtest:

| window | peak/high | peak date | trough/low | trough date | MFE | MAE |
|---|---:|---|---:|---|---:|---:|
| 30 calendar days | 127500 | 2024-02-23 | 105500 | 2024-02-02 | +18.83% | -1.68% |
| 90 calendar days | 136600 | 2024-03-15 | 105500 | 2024-02-02 | +27.31% | -1.68% |
| 180 calendar days | 146200 | 2024-07-11 | 105500 | 2024-02-02 | +36.25% | -1.68% |

Interpretation:

```text
039490 is the C21 positive anchor.
The MFE persisted from 30D through 180D and the MAE stayed tiny. That is the correct price geometry for a brokerage ROE / capital-return rerating.
Green still requires URL-repaired ROE, shareholder-return, capital adequacy, and earnings-quality evidence.
```

### 6.2 `071050` 한국금융지주 — securities-holdco discount closure low-MAE case

Trigger:

```text
trigger_date = 2024-02-01
trigger_type = Stage2-Actionable-Guarded
trigger_family = securities_holdco_valueup_roe_discount_closure_low_mae
entry_date = 2024-02-02
entry_price = 65800.0
entry_price_type = next_tradable_open_after_securities_holdco_valueup_burst
```

Relevant Stock-Web rows:

```csv
d,o,h,l,c,v,a,mc,s,m
2024-02-01,61000.0,66700.0,60500.0,66200.0,461141.0,29946987000.0,3689060670400.0,55725992,KOSPI
2024-02-02,65800.0,67100.0,64500.0,66300.0,341473.0,22507223259.0,3694633269600.0,55725992,KOSPI
2024-02-05,66700.0,67000.0,62800.0,64600.0,217490.0,14025399400.0,3599899083200.0,55725992,KOSPI
2024-02-23,70400.0,72000.0,70300.0,71000.0,158095.0,11253508400.0,3956545432000.0,55725992,KOSPI
2024-03-05,74000.0,75200.0,73300.0,74100.0,188756.0,14019563300.0,4129296007200.0,55725992,KOSPI
2024-07-17,73300.0,77700.0,72700.0,75200.0,471821.0,35916444200.0,4190594598400.0,55725992,KOSPI
2024-08-05,69100.0,69300.0,62900.0,63700.0,245906.0,16044493200.0,3549745690400.0,55725992,KOSPI
```

Backtest:

| window | peak/high | peak date | trough/low | trough date | MFE | MAE |
|---|---:|---|---:|---|---:|---:|
| 30 calendar days | 72000 | 2024-02-23 | 62800 | 2024-02-05 | +9.42% | -4.56% |
| 90 calendar days | 75200 | 2024-03-05 | 62800 | 2024-02-05 | +14.29% | -4.56% |
| 180 calendar days | 77700 | 2024-07-17 | 62800 | 2024-02-05 | +18.09% | -4.56% |

Interpretation:

```text
071050 is a positive-guarded C21 case.
The rerating was less explosive than 039490, but the path preserved capital and improved through 180D.
This should stay Stage2-Guarded / Yellow-after-repair, not Green from value-up policy alone.
```

### 6.3 `016360` 삼성증권 — brokerage dividend/value-up weak-MFE drawdown watch

Trigger:

```text
trigger_date = 2024-02-01
trigger_type = Stage2-Actionable-Guarded
trigger_family = brokerage_dividend_valueup_weak_mfe_drawdown_watch
entry_date = 2024-02-02
entry_price = 39750.0
entry_price_type = next_tradable_open_after_financial_valueup_brokerage_burst
```

Relevant Stock-Web rows:

```csv
d,o,h,l,c,v,a,mc,s,m
2024-02-01,37500.0,39850.0,37450.0,39550.0,855788.0,33352507750.0,3531815000000.0,89300000,KOSPI
2024-02-02,39750.0,40700.0,38900.0,40550.0,712196.0,28467339900.0,3621115000000.0,89300000,KOSPI
2024-02-23,40850.0,42750.0,40750.0,41800.0,615953.0,25902633050.0,3732740000000.0,89300000,KOSPI
2024-04-19,35800.0,36050.0,35350.0,35900.0,258816.0,9247343650.0,3205870000000.0,89300000,KOSPI
2024-06-28,38400.0,39850.0,38350.0,39800.0,815565.0,32180155050.0,3554140000000.0,89300000,KOSPI
2024-07-17,45700.0,46150.0,45150.0,45400.0,404780.0,18483681150.0,4054220000000.0,89300000,KOSPI
2024-08-05,42100.0,42300.0,39500.0,40300.0,489974.0,20072168300.0,3598790000000.0,89300000,KOSPI
```

Backtest:

| window | peak/high | peak date | trough/low | trough date | MFE | MAE |
|---|---:|---|---:|---|---:|---:|
| 30 calendar days | 42750 | 2024-02-23 | 38050 | 2024-02-15 | +7.55% | -4.28% |
| 90 calendar days | 42750 | 2024-02-23 | 35350 | 2024-04-19 | +7.55% | -11.07% |
| 180 calendar days | 46150 | 2024-07-17 | 35350 | 2024-04-19 | +16.10% | -11.07% |

Interpretation:

```text
016360 is the guarded weak-MFE branch.
The later 180D MFE improved, but the first 90D path had weak MFE and double-digit drawdown.
This should cap at Stage2-Guarded until dividend, ROE, earnings-quality, and balance-sheet evidence is repaired.
```

### 6.4 `006800` 미래에셋증권 — large brokerage value-up weak-MFE slow fade

Trigger:

```text
trigger_date = 2024-02-01
trigger_type = Stage2-FalsePositive-Candidate
trigger_family = large_brokerage_valueup_weak_mfe_balance_sheet_drag
entry_date = 2024-02-02
entry_price = 8350.0
entry_price_type = next_tradable_open_after_brokerage_valueup_burst
```

Relevant Stock-Web rows:

```csv
d,o,h,l,c,v,a,mc,s,m
2024-02-01,7830.0,8300.0,7830.0,8290.0,2665240.0,21780894250.0,5018073022320.0,605316408,KOSPI
2024-02-02,8350.0,8700.0,8150.0,8620.0,2296779.0,19485963280.0,5217827436960.0,605316408,KOSPI
2024-02-23,9080.0,9200.0,8900.0,8950.0,2057313.0,18576938770.0,5417581851600.0,605316408,KOSPI
2024-03-12,8000.0,8050.0,7750.0,7820.0,1485635.0,11663968410.0,4733574310560.0,605316408,KOSPI
2024-04-19,7250.0,7320.0,7050.0,7150.0,583741.0,4178671930.0,4256512317200.0,595316408,KOSPI
2024-06-14,7080.0,7080.0,6930.0,6990.0,626915.0,4379011300.0,4161261691920.0,595316408,KOSPI
2024-07-31,7720.0,7750.0,7650.0,7750.0,346550.0,2672966060.0,4613702162000.0,595316408,KOSPI
2024-08-05,7250.0,7250.0,6600.0,6660.0,1967971.0,13520077360.0,3964807277280.0,595316408,KOSPI
```

Backtest:

| window | peak/high | peak date | trough/low | trough date | MFE | MAE |
|---|---:|---|---:|---|---:|---:|
| 30 calendar days | 9200 | 2024-02-23 | 8150 | 2024-02-02 | +10.18% | -2.40% |
| 90 calendar days | 9200 | 2024-02-23 | 7050 | 2024-04-19 | +10.18% | -15.57% |
| 180 calendar days | 9200 | 2024-02-23 | 6930 | 2024-06-14 | +10.18% | -17.01% |

Interpretation:

```text
006800 is the C21 weak-MFE slow-fade counterexample.
The value-up label created an early bounce, but MFE stalled near +10% and mid-window drawdown widened before any durable ROE/capital-return bridge was URL-repaired.
This should block Green and either block Stage2 or keep it Stage2-Guarded only after fresh evidence.
```

---

## 7. Machine-readable trigger JSONL

```jsonl
{"row_type":"trigger","research_id":"R6L75_C21_BROKERAGE_VALUEUP_ROE_ROUTER","round":"R6","loop":75,"large_sector_id":"L6_FINANCIAL_CAPITAL_RETURN_DIGITAL","canonical_archetype_id":"C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN","fine_archetype_id":"BROKERAGE_CAPITAL_RETURN_ROE_VALUEUP_AND_WEAK_MFE_BALANCE_SHEET_ROUTER","symbol":"039490","name":"키움증권","trigger_type":"Stage2-Actionable","trigger_family":"brokerage_valueup_roe_capital_return_low_mae_rerating","trigger_date":"2024-02-01","entry_date":"2024-02-02","entry_price":107300.0,"entry_price_type":"next_tradable_open_after_financial_valueup_brokerage_burst","price_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","mfe_30d_pct":18.83,"mae_30d_pct":-1.68,"mfe_90d_pct":27.31,"mae_90d_pct":-1.68,"mfe_180d_pct":36.25,"mae_180d_pct":-1.68,"peak_price_180d":146200.0,"peak_date_180d":"2024-07-11","trough_price_180d":105500.0,"trough_date_180d":"2024-02-02","calibration_usable":true,"case_polarity":"positive_anchor_low_mae_brokerage_valueup","evidence_url_pending":true,"source_proxy_only":true,"non_price_evidence_strength":"medium_pending_url_repair","price_only_blowoff":false,"expected_stage_current_profile":"Stage2-Actionable_to_Yellow_after_roe_capital_return_earnings_quality_bridge_repaired","residual_error_type":"positive_brokerage_valueup_path_requires_url_repaired_roe_shareholder_return_and_earnings_quality_bridge_before_green"}
{"row_type":"trigger","research_id":"R6L75_C21_BROKERAGE_VALUEUP_ROE_ROUTER","round":"R6","loop":75,"large_sector_id":"L6_FINANCIAL_CAPITAL_RETURN_DIGITAL","canonical_archetype_id":"C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN","fine_archetype_id":"BROKERAGE_CAPITAL_RETURN_ROE_VALUEUP_AND_WEAK_MFE_BALANCE_SHEET_ROUTER","symbol":"071050","name":"한국금융지주","trigger_type":"Stage2-Actionable-Guarded","trigger_family":"securities_holdco_valueup_roe_discount_closure_low_mae","trigger_date":"2024-02-01","entry_date":"2024-02-02","entry_price":65800.0,"entry_price_type":"next_tradable_open_after_securities_holdco_valueup_burst","price_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","mfe_30d_pct":9.42,"mae_30d_pct":-4.56,"mfe_90d_pct":14.29,"mae_90d_pct":-4.56,"mfe_180d_pct":18.09,"mae_180d_pct":-4.56,"peak_price_180d":77700.0,"peak_date_180d":"2024-07-17","trough_price_180d":62800.0,"trough_date_180d":"2024-02-05","calibration_usable":true,"case_polarity":"positive_guarded_low_mae_discount_closure","evidence_url_pending":true,"source_proxy_only":true,"non_price_evidence_strength":"medium_low_pending_url_repair","price_only_blowoff":false,"expected_stage_current_profile":"Stage2-Guarded_to_Yellow_if_roe_capital_allocation_brokerage_cycle_bridge_repaired","residual_error_type":"securities_holdco_discount_closure_path_requires_url_repaired_capital_allocation_and_roe_bridge_before_green"}
{"row_type":"trigger","research_id":"R6L75_C21_BROKERAGE_VALUEUP_ROE_ROUTER","round":"R6","loop":75,"large_sector_id":"L6_FINANCIAL_CAPITAL_RETURN_DIGITAL","canonical_archetype_id":"C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN","fine_archetype_id":"BROKERAGE_CAPITAL_RETURN_ROE_VALUEUP_AND_WEAK_MFE_BALANCE_SHEET_ROUTER","symbol":"016360","name":"삼성증권","trigger_type":"Stage2-Actionable-Guarded","trigger_family":"brokerage_dividend_valueup_weak_mfe_drawdown_watch","trigger_date":"2024-02-01","entry_date":"2024-02-02","entry_price":39750.0,"entry_price_type":"next_tradable_open_after_financial_valueup_brokerage_burst","price_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","mfe_30d_pct":7.55,"mae_30d_pct":-4.28,"mfe_90d_pct":7.55,"mae_90d_pct":-11.07,"mfe_180d_pct":16.1,"mae_180d_pct":-11.07,"peak_price_180d":46150.0,"peak_date_180d":"2024-07-17","trough_price_180d":35350.0,"trough_date_180d":"2024-04-19","calibration_usable":true,"case_polarity":"counterexample_guarded_weak_mfe_drawdown","evidence_url_pending":true,"source_proxy_only":true,"non_price_evidence_strength":"medium_low_pending_url_repair","price_only_blowoff":false,"expected_stage_current_profile":"Stage2-Guarded_only_until_dividend_roe_earnings_bridge_repaired","residual_error_type":"brokerage_dividend_valueup_label_had_weak_early_mfe_and_drawdown_without_repaired_roe_earnings_quality_bridge"}
{"row_type":"trigger","research_id":"R6L75_C21_BROKERAGE_VALUEUP_ROE_ROUTER","round":"R6","loop":75,"large_sector_id":"L6_FINANCIAL_CAPITAL_RETURN_DIGITAL","canonical_archetype_id":"C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN","fine_archetype_id":"BROKERAGE_CAPITAL_RETURN_ROE_VALUEUP_AND_WEAK_MFE_BALANCE_SHEET_ROUTER","symbol":"006800","name":"미래에셋증권","trigger_type":"Stage2-FalsePositive-Candidate","trigger_family":"large_brokerage_valueup_weak_mfe_balance_sheet_drag","trigger_date":"2024-02-01","entry_date":"2024-02-02","entry_price":8350.0,"entry_price_type":"next_tradable_open_after_brokerage_valueup_burst","price_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","mfe_30d_pct":10.18,"mae_30d_pct":-2.4,"mfe_90d_pct":10.18,"mae_90d_pct":-15.57,"mfe_180d_pct":10.18,"mae_180d_pct":-17.01,"peak_price_180d":9200.0,"peak_date_180d":"2024-02-23","trough_price_180d":6930.0,"trough_date_180d":"2024-06-14","calibration_usable":true,"case_polarity":"counterexample_weak_mfe_slow_fade","evidence_url_pending":true,"source_proxy_only":true,"non_price_evidence_strength":"low_pending_url_repair","price_only_blowoff":false,"expected_stage_current_profile":"blocked_Stage2_or_Stage2_Guarded_until_shareholder_return_roe_bridge_repaired","residual_error_type":"large_brokerage_valueup_label_had_only_small_mfe_and_mid_window_drawdown_without_capital_return_roe_bridge"}
```

---

## 8. Score simulation and raw component breakdown

This is shadow-only and does not change production scoring.

| symbol | ROE / earnings quality | shareholder return | capital adequacy | risk-asset trust | market mispricing | valuation discount closure | information confidence | shadow total | intended route |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| `039490` | 13 | 11 | 10 | 9 | 13 | 12 | 6 | 74 | Stage2/Yellow after ROE and capital-return bridge repair |
| `071050` | 11 | 9 | 9 | 8 | 10 | 9 | 6 | 62 | Stage2-Guarded / Yellow after evidence repair |
| `016360` | 9 | 8 | 9 | 6 | 6 | 6 | 5 | 49 | Stage2-Guarded only until evidence repair |
| `006800` | 6 | 5 | 6 | 3 | 4 | 3 | 5 | 32 | blocked Stage2 or guarded after fresh bridge |

### Current calibrated profile stress test

The current calibrated profile already blocks pure price-only blowoff.  
The remaining C21 issue is **financial value-up label without company-specific ROE / capital-return conversion**:

```text
C21 clean brokerage path:
  value-up / ROE / shareholder-return relevance
  + persistent MFE
  + contained MAE
  + URL-repaired ROE, dividend/buyback, and risk-asset evidence
  => Stage2-Actionable / Yellow, possible Green after proof

C21 guarded brokerage path:
  capital-return label exists
  + 180D MFE improves
  + 90D drawdown is non-trivial
  + evidence remains source_proxy_only
  => Stage2-Guarded at most, no Green

C21 weak-MFE slow fade:
  value-up label exists
  + MFE_90D near +10%
  + MAE_90D <= -15%
  + no ROE / shareholder-return bridge
  => block Green and usually block Stage2
```

`039490` and `071050` prevent overblocking.  
`016360` shows why weak early MFE should cap the route.  
`006800` shows that a large brokerage value-up label can fail quietly through a slow-fade, not only through a hard 4C crash.

---

## 9. Aggregate metrics

```json
{
  "row_type": "aggregate",
  "research_id": "R6L75_C21_BROKERAGE_VALUEUP_ROE_ROUTER",
  "round": "R6",
  "loop": 75,
  "large_sector_id": "L6_FINANCIAL_CAPITAL_RETURN_DIGITAL",
  "canonical_archetype_id": "C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN",
  "fine_archetype_id": "BROKERAGE_CAPITAL_RETURN_ROE_VALUEUP_AND_WEAK_MFE_BALANCE_SHEET_ROUTER",
  "case_count": 4,
  "calibration_usable_case_count": 4,
  "positive_case_count": 2,
  "counterexample_count": 2,
  "new_symbol_count": 4,
  "source_proxy_only_count": 4,
  "evidence_url_pending_count": 4,
  "avg_mfe_30d_pct": 11.5,
  "avg_mae_30d_pct": -3.23,
  "avg_mfe_90d_pct": 14.83,
  "avg_mae_90d_pct": -8.22,
  "avg_mfe_180d_pct": 20.16,
  "avg_mae_180d_pct": -8.58,
  "max_mfe_180d_pct": 36.25,
  "worst_mae_180d_pct": -17.01
}
```

---

## 10. 4B proximity split

```json
{
  "row_type": "4b_split",
  "research_id": "R6L75_C21_BROKERAGE_VALUEUP_ROE_ROUTER",
  "stage2_positive_or_yellow_candidate": [
    {
      "symbol": "039490",
      "reason": "brokerage value-up path had +36.25% 180D MFE with only -1.68% MAE"
    },
    {
      "symbol": "071050",
      "reason": "securities-holdco path had +18.09% 180D MFE with only -4.56% MAE"
    }
  ],
  "stage2_guarded_or_local_4b_watch": [
    {
      "symbol": "016360",
      "reason": "first 90D MFE was only +7.55% while MAE reached -11.07%; later recovery needs evidence repair"
    }
  ],
  "blocked_stage2_or_weak_mfe_fade": [
    {
      "symbol": "006800",
      "reason": "MFE stayed near +10.18% while 90D/180D drawdown widened; no repaired capital-return / ROE bridge"
    }
  ],
  "full_4b_or_green_requires_non_price_evidence": [
    "ROE durability and earnings quality",
    "dividend / buyback / total shareholder return execution",
    "capital adequacy and excess-capital policy",
    "IB/PF / ELS / overseas risk-asset trust",
    "brokerage commission and wealth-management cycle",
    "valuation discount closure"
  ]
}
```

---

## 11. Shadow rule candidate

```yaml
row_type: canonical_archetype_rule_candidate
canonical_archetype_id: C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN
fine_archetype_id: BROKERAGE_CAPITAL_RETURN_ROE_VALUEUP_AND_WEAK_MFE_BALANCE_SHEET_ROUTER
rule_name: C21_brokerage_valueup_roe_capital_return_and_weak_mfe_router
production_scoring_changed: false
shadow_weight_only: true
```

### Proposed routing logic

```text
For C21 brokerage / securities-holdco ROE / capital-return cases:

Tier A: verified brokerage capital-return rerating
  Conditions:
    - ROE, shareholder-return, capital adequacy, and earnings-quality evidence are URL-repaired
    - MFE_90D >= +20%
    - MAE_90D > -8%
    - MFE persists beyond one policy candle
  Routing:
    - Stage2-Actionable allowed
    - Stage3-Yellow allowed after evidence repair
    - Green only after ROE / capital-return / risk-asset evidence is verified

Tier B: guarded brokerage value-up path
  Conditions:
    - MFE_180D improves above +15%
    - MAE_90D <= -10%
    - evidence remains source_proxy_only
  Routing:
    - Stage2-Guarded at most
    - no Green until evidence repair

Tier C: weak-MFE slow-fade financial label
  Conditions:
    - MFE_90D <= +12%
    - MAE_90D <= -15%
    - no repaired ROE / shareholder-return bridge
  Routing:
    - block Green
    - block Stage2 or local 4B watch
    - count as counterexample
```

### Suggested shadow delta

```json
{
  "row_type": "shadow_weight",
  "axis": "c21_brokerage_valueup_roe_capital_return_and_weak_mfe_router",
  "scope": "canonical_archetype_id:C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN",
  "proposal": {
    "source_proxy_only_green_allowed": false,
    "roe_shareholder_return_risk_asset_bridge_required_for_green": true,
    "verified_brokerage_mfe90_threshold_pct": 20.0,
    "verified_brokerage_mae90_min_pct": -8.0,
    "guarded_recovery_mfe180_threshold_pct": 15.0,
    "guarded_drawdown_mae90_threshold_pct": -10.0,
    "weak_mfe_threshold_90d_pct": 12.0,
    "weak_mfe_drawdown_threshold_90d_pct": -15.0,
    "positive_weight_blocked_until_url_repair": true
  },
  "confidence": "medium_low_until_url_repair",
  "apply_now": false,
  "reason": "Two brokerage/securities-holdco positive paths and two weak-MFE brokerage value-up paths show that C21 should require URL-repaired ROE, shareholder-return, capital adequacy, earnings-quality, and risk-asset evidence before Yellow/Green."
}
```

---

## 12. Residual contribution summary

```json
{
  "row_type": "residual_contribution",
  "research_id": "R6L75_C21_BROKERAGE_VALUEUP_ROE_ROUTER",
  "large_sector_id": "L6_FINANCIAL_CAPITAL_RETURN_DIGITAL",
  "canonical_archetype_id": "C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN",
  "contribution": "Adds four non-top-covered C21 brokerage / securities-holdco financial value-up cases and separates low-MAE ROE/capital-return rerating from weak-MFE brokerage value-up slow fades. C21 Yellow/Green should require URL-repaired ROE durability, shareholder return, capital adequacy, risk-asset trust, earnings quality, and valuation-discount closure evidence.",
  "positive_case_added": 2,
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
  "data_quality_blocker": "All four non-price brokerage/financial value-up triggers require URL-level repair before positive weight promotion.",
  "guardrail_added": "C21 source_proxy_only brokerage cases with MFE_90D <= +12% and MAE_90D <= -15% should block Green and often Stage2; cases with later MFE recovery but early weak MFE should cap at Stage2-Guarded until ROE/shareholder-return evidence is repaired."
}
```

One-line contribution:

```text
This loop adds 4 new independent cases, 2 counterexamples, and 2 residual errors for R6/L6_FINANCIAL_CAPITAL_RETURN_DIGITAL/C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN.
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
    039490: false
    071050: false
    016360: false
    006800: false
  evidence_url_pending:
    039490: true
    071050: true
    016360: true
    006800: true
  source_proxy_only:
    039490: true
    071050: true
    016360: true
    006800: true
```

Limitations:

```text
- Price path is validated against Stock-Web tradable OHLC rows.
- Non-price evidence is not URL-repaired in this run.
- Therefore this artifact is useful for C21 brokerage / financial value-up residual shape and weak-MFE guardrail design, but should not promote positive weights until filings, IR, capital-policy disclosure, or reports verify ROE, shareholder return, capital adequacy, earnings quality, and risk-asset trust.
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
2. Preserve R6 / loop 75 metadata.
3. Add the cases to C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN only if parser validation passes.
4. Treat all four non-price triggers as evidence_url_pending=true and source_proxy_only=true until URL-level evidence is repaired.
5. Do not use these rows for positive weight promotion until filings/IR/capital-policy/report data verifies ROE durability, earnings quality, shareholder return, capital adequacy, risk-asset trust, and valuation-discount closure.
6. Add a shadow-only rule candidate named C21_brokerage_valueup_roe_capital_return_and_weak_mfe_router.
7. Do not loosen Stage3-Green.
8. Add C21-specific guards:
   - source_proxy_only -> no Green
   - Green requires repaired ROE / shareholder-return / risk-asset evidence
   - MFE_90D >= +20% and MAE_90D > -8% may remain Stage2-Actionable / Yellow watch after evidence repair
   - MFE_180D > +15% but MAE_90D <= -10% -> Stage2-Guarded at most while evidence is pending
   - MFE_90D <= +12% and MAE_90D <= -15% -> block Green and often block Stage2 / local 4B watch
9. Keep production scoring unchanged unless later batch promotion logic independently marks this axis safe.
```

---

## 15. Next round state

```text
completed_round = R6
completed_loop = 75
next_round = R7
next_loop = 75
next_large_sector_hint = L7_BIO_HEALTHCARE_MEDICAL
round_schedule_status = valid
round_sector_consistency = pass
```
