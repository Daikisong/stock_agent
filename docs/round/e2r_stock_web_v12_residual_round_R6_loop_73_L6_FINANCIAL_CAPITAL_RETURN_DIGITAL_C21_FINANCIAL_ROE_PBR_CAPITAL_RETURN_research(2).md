# E2R Stock-Web v12 Residual Research — R6 Loop 73

```yaml
research_session: post_calibrated_sector_archetype_residual_research
mode: historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12
completed_round: R6
completed_loop: 73
next_round: R7
next_loop: 73
large_sector_id: L6_FINANCIAL_CAPITAL_RETURN_DIGITAL
canonical_archetype_id: C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN
fine_archetype_id: BROKERAGE_VALUEUP_ROE_PBR_CAPITAL_RETURN_HIGH_MAE_ROUTER
output_file: e2r_stock_web_v12_residual_round_R6_loop_73_L6_FINANCIAL_CAPITAL_RETURN_DIGITAL_C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN_research.md
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
completed_loop  = 73
large_sector_id = L5_CONSUMER_BRAND_DISTRIBUTION
canonical_archetype_id = C19_BRAND_RETAIL_INVENTORY_MARGIN
```

Therefore:

```text
scheduled_round = R6
scheduled_loop  = 73
```

R6 maps to:

```text
large_sector_id = L6_FINANCIAL_CAPITAL_RETURN_DIGITAL
```

This run selects:

```text
canonical_archetype_id = C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN
fine_archetype_id = BROKERAGE_VALUEUP_ROE_PBR_CAPITAL_RETURN_HIGH_MAE_ROUTER
```

This is a valid R6/L6 pairing.

---

## 1. Why this R6/C21 run

The no-repeat ledger shows C21 is heavily covered, but the dominant rows are concentrated in banks and the most visible low-PBR financials:

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

This run deliberately avoids the top-covered bank-heavy set and expands into brokerage / non-bank financial capital-return rerating:

```text
016360 삼성증권
071050 한국금융지주
006800 미래에셋증권
```

Research question:

```text
Can C21 distinguish a brokerage value-up / ROE-PBR rerating path with clean low-MAE follow-through from a post-spike financial entry whose first rerating candle has already spent most of the upside?
```

C21 is a capital-return archetype, but for brokers the current runs through a different wire than banks. Banks rerate through CET1, buyback visibility, dividend policy, and NIM/credit cycle. Securities firms rerate through ROE recovery, market volume, IB/WM earnings, shareholder-return policy, and balance-sheet risk. When the market sees “low PBR + value-up,” it can paint all financials with one brush. This file tests where that brush smears.

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
| `016360` | 삼성증권 | active_like / KOSPI | no 2024 overlap; latest listed candidate 2001-07-10 | true |
| `071050` | 한국금융지주 | active_like / KOSPI | none listed | true |
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
The Stock-Web price path is fully validated, but company-level capital-return execution, dividend/buyback plan, ROE recovery, brokerage earnings mix, IB/WM contribution, balance-sheet risk, and regulatory value-up disclosure evidence still require later URL repair through filings, IR decks, exchange disclosures, or sell-side reports before production weight promotion.
```

C21 interpretation used here:

```text
C21 is not simply “financial stock went up.”
It asks whether the low-PBR / value-up rerating is supported by:
- ROE recovery,
- dividend/buyback or total shareholder return,
- capital adequacy / balance-sheet safety,
- earnings quality,
- valuation discount closure,
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
016360 + C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN -> no direct match found
071050 + C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN -> no direct match found
006800 + C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN -> no direct match found
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
| `R6L73_C21_071050_20240130` | `071050` 한국금융지주 | brokerage/holding ROE-PBR value-up rerating with low MAE | positive anchor |
| `R6L73_C21_016360_20240130` | `016360` 삼성증권 | shareholder-return / brokerage ROE rerating with contained MAE | positive-guarded |
| `R6L73_C21_006800_20240226` | `006800` 미래에셋증권 | post-spike brokerage value-up entry without fresh execution bridge | counterexample / high-MAE watch |

The intended residual:

```text
C21 should separate:
1. early low-PBR financial rerating entries with low MAE and persistent follow-through;
2. brokerage capital-return candidates whose price path remains constructive but still needs URL-repaired shareholder-return / ROE evidence;
3. post-spike entries where the value-up theme is real but the remaining upside is small and later MAE crosses the guardrail.
```

---

## 6. Stock-Web OHLC and backtest

### 6.1 `071050` 한국금융지주 — brokerage/holding value-up positive anchor

Trigger:

```text
trigger_date = 2024-01-29
trigger_type = Stage2-Actionable
trigger_family = brokerage_holding_company_roe_pbr_valueup_rerating
entry_date = 2024-01-30
entry_price = 58700.0
entry_price_type = next_tradable_open
```

Relevant Stock-Web rows:

```csv
d,o,h,l,c,v,a,mc,s,m
2024-01-29,58800.0,59500.0,57400.0,58700.0,93784.0,5516968800.0,3271115730400.0,55725992,KOSPI
2024-01-30,58700.0,62000.0,58700.0,61400.0,215559.0,13219680400.0,3421575908800.0,55725992,KOSPI
2024-02-01,61000.0,66700.0,60500.0,66200.0,461141.0,29946987000.0,3689060670400.0,55725992,KOSPI
2024-02-19,69200.0,71200.0,69200.0,70900.0,269231.0,18918334200.0,3950972832800.0,55725992,KOSPI
2024-02-23,70400.0,72000.0,70300.0,71000.0,158095.0,11253508400.0,3956545432000.0,55725992,KOSPI
2024-03-05,74000.0,75200.0,73300.0,74100.0,188756.0,14019563300.0,4129296007200.0,55725992,KOSPI
2024-07-17,73300.0,77700.0,72700.0,75200.0,471821.0,35916444200.0,4190594598400.0,55725992,KOSPI
2024-08-05,69100.0,69300.0,62900.0,63700.0,245906.0,16044493200.0,3549745690400.0,55725992,KOSPI
```

Backtest:

| window | peak/high | peak date | trough/low | trough date | MFE | MAE |
|---|---:|---|---:|---|---:|---:|
| 30 calendar days | 72000 | 2024-02-23 | 58700 | 2024-01-30 | +22.66% | +0.00% |
| 90 calendar days | 75200 | 2024-03-05 | 58700 | 2024-01-30 | +28.11% | +0.00% |
| 180 calendar days | 77700 | 2024-07-17 | 58700 | 2024-01-30 | +32.37% | +0.00% |

Interpretation:

```text
071050 is the clean C21 brokerage/holding positive anchor.
The price path had persistent MFE and no adverse excursion from the selected entry.
This is the case C21 should keep as Stage2-Actionable / Yellow candidate after URL repair.
Green still requires shareholder-return execution, ROE recovery, and capital-risk evidence.
```

### 6.2 `016360` 삼성증권 — shareholder-return brokerage rerating with contained MAE

Trigger:

```text
trigger_date = 2024-01-29
trigger_type = Stage2-Actionable
trigger_family = brokerage_shareholder_return_roe_pbr_rerating
entry_date = 2024-01-30
entry_price = 37100.0
entry_price_type = next_tradable_open
```

Relevant Stock-Web rows:

```csv
d,o,h,l,c,v,a,mc,s,m
2024-01-29,36500.0,37250.0,36200.0,36950.0,214774.0,7920764100.0,3299635000000.0,89300000,KOSPI
2024-01-30,37100.0,37950.0,37050.0,37250.0,250706.0,9386395200.0,3326425000000.0,89300000,KOSPI
2024-02-01,37500.0,39850.0,37450.0,39550.0,855788.0,33352507750.0,3531815000000.0,89300000,KOSPI
2024-02-19,40950.0,42250.0,40800.0,41700.0,509159.0,21223242150.0,3723810000000.0,89300000,KOSPI
2024-02-23,40850.0,42750.0,40750.0,41800.0,615953.0,25902633050.0,3732740000000.0,89300000,KOSPI
2024-04-19,35800.0,36050.0,35350.0,35900.0,258816.0,9247343650.0,3205870000000.0,89300000,KOSPI
2024-07-17,45700.0,46150.0,45150.0,45400.0,404780.0,18483681150.0,4054220000000.0,89300000,KOSPI
2024-08-20,45850.0,47800.0,45800.0,47800.0,726013.0,34300890700.0,4268540000000.0,89300000,KOSPI
```

Backtest:

| window | peak/high | peak date | trough/low | trough date | MFE | MAE |
|---|---:|---|---:|---|---:|---:|
| 30 calendar days | 42750 | 2024-02-23 | 37050 | 2024-01-30 | +15.23% | -0.13% |
| 90 calendar days | 42750 | 2024-02-23 | 35350 | 2024-04-19 | +15.23% | -4.72% |
| 180 calendar days | 46150 | 2024-07-17 | 35350 | 2024-04-19 | +24.39% | -4.72% |

Interpretation:

```text
016360 is a constructive C21 positive-guarded case.
The path was less explosive than 071050 but remained aligned: MFE was persistent and MAE stayed contained.
This supports Stage2-Actionable / Stage3-Yellow after evidence repair, not automatic Green.
```

### 6.3 `006800` 미래에셋증권 — post-spike value-up entry with weak remaining MFE

Trigger:

```text
trigger_date = 2024-02-23
trigger_type = Stage2-FalsePositive-Candidate
trigger_family = brokerage_valueup_post_spike_without_fresh_capital_return_bridge
entry_date = 2024-02-26
entry_price = 8950.0
entry_price_type = next_tradable_open_after_valueup_spike
```

Relevant Stock-Web rows:

```csv
d,o,h,l,c,v,a,mc,s,m
2024-02-23,9080.0,9200.0,8900.0,8950.0,2057313.0,18576938770.0,5417581851600.0,605316408,KOSPI
2024-02-26,8950.0,8980.0,8550.0,8680.0,1147724.0,10030148820.0,5254146421440.0,605316408,KOSPI
2024-02-29,9100.0,9160.0,8940.0,9020.0,1509894.0,13637120760.0,5459954000160.0,605316408,KOSPI
2024-03-12,8000.0,8050.0,7750.0,7820.0,1485635.0,11663968410.0,4733574310560.0,605316408,KOSPI
2024-04-19,7250.0,7320.0,7050.0,7150.0,583741.0,4178671930.0,4256512317200.0,595316408,KOSPI
2024-06-11,7200.0,7240.0,7060.0,7070.0,569363.0,4052524830.0,4208887004560.0,595316408,KOSPI
2024-07-29,7650.0,7950.0,7570.0,7800.0,892921.0,6975550380.0,4643467982400.0,595316408,KOSPI
2024-08-05,7250.0,7250.0,6600.0,6660.0,1967971.0,13520077360.0,3964807277280.0,595316408,KOSPI
```

Backtest:

| window | peak/high | peak date | trough/low | trough date | MFE | MAE |
|---|---:|---|---:|---|---:|---:|
| 30 calendar days | 9160 | 2024-02-29 | 7750 | 2024-03-12 | +2.35% | -13.41% |
| 90 calendar days | 9160 | 2024-02-29 | 7050 | 2024-04-19 | +2.35% | -21.23% |
| 180 calendar days | 9160 | 2024-02-29 | 6600 | 2024-08-05 | +2.35% | -26.26% |

Interpretation:

```text
006800 is the counterexample branch.
The broader C21 theme was real, but this post-spike entry had already spent the rerating candle.
A model that treats every brokerage value-up move as fresh Stage2 would over-score this case.
The right route is local 4B/high-MAE watch or blocked Stage2 until a fresh capital-return / ROE bridge appears.
```

---

## 7. Machine-readable trigger JSONL

```jsonl
{"row_type":"trigger","research_id":"R6L73_C21_BROKERAGE_VALUEUP_CAPITAL_RETURN","round":"R6","loop":73,"large_sector_id":"L6_FINANCIAL_CAPITAL_RETURN_DIGITAL","canonical_archetype_id":"C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN","fine_archetype_id":"BROKERAGE_VALUEUP_ROE_PBR_CAPITAL_RETURN_HIGH_MAE_ROUTER","symbol":"071050","name":"한국금융지주","trigger_type":"Stage2-Actionable","trigger_family":"brokerage_holding_company_roe_pbr_valueup_rerating","trigger_date":"2024-01-29","entry_date":"2024-01-30","entry_price":58700.0,"entry_price_type":"next_tradable_open","price_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","mfe_30d_pct":22.66,"mae_30d_pct":0.00,"mfe_90d_pct":28.11,"mae_90d_pct":0.00,"mfe_180d_pct":32.37,"mae_180d_pct":0.00,"peak_price_180d":77700.0,"peak_date_180d":"2024-07-17","trough_price_180d":58700.0,"trough_date_180d":"2024-01-30","calibration_usable":true,"case_polarity":"positive_anchor","evidence_url_pending":true,"source_proxy_only":true,"non_price_evidence_strength":"medium_pending_url_repair","price_only_blowoff":false,"expected_stage_current_profile":"Stage2-Actionable_to_Yellow_after_roe_capital_return_bridge_repaired","residual_error_type":"positive_anchor_requires_url_repaired_roe_shareholder_return_evidence_before_green"}
{"row_type":"trigger","research_id":"R6L73_C21_BROKERAGE_VALUEUP_CAPITAL_RETURN","round":"R6","loop":73,"large_sector_id":"L6_FINANCIAL_CAPITAL_RETURN_DIGITAL","canonical_archetype_id":"C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN","fine_archetype_id":"BROKERAGE_VALUEUP_ROE_PBR_CAPITAL_RETURN_HIGH_MAE_ROUTER","symbol":"016360","name":"삼성증권","trigger_type":"Stage2-Actionable","trigger_family":"brokerage_shareholder_return_roe_pbr_rerating","trigger_date":"2024-01-29","entry_date":"2024-01-30","entry_price":37100.0,"entry_price_type":"next_tradable_open","price_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","mfe_30d_pct":15.23,"mae_30d_pct":-0.13,"mfe_90d_pct":15.23,"mae_90d_pct":-4.72,"mfe_180d_pct":24.39,"mae_180d_pct":-4.72,"peak_price_180d":46150.0,"peak_date_180d":"2024-07-17","trough_price_180d":35350.0,"trough_date_180d":"2024-04-19","calibration_usable":true,"case_polarity":"positive_guarded","evidence_url_pending":true,"source_proxy_only":true,"non_price_evidence_strength":"medium_pending_url_repair","price_only_blowoff":false,"expected_stage_current_profile":"Stage2-Actionable_to_Yellow_if_capital_return_roe_bridge_repaired","residual_error_type":"constructive_path_but_green_requires_shareholder_return_and_earnings_quality_bridge"}
{"row_type":"trigger","research_id":"R6L73_C21_BROKERAGE_VALUEUP_CAPITAL_RETURN","round":"R6","loop":73,"large_sector_id":"L6_FINANCIAL_CAPITAL_RETURN_DIGITAL","canonical_archetype_id":"C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN","fine_archetype_id":"BROKERAGE_VALUEUP_ROE_PBR_CAPITAL_RETURN_HIGH_MAE_ROUTER","symbol":"006800","name":"미래에셋증권","trigger_type":"Stage2-FalsePositive-Candidate","trigger_family":"brokerage_valueup_post_spike_without_fresh_capital_return_bridge","trigger_date":"2024-02-23","entry_date":"2024-02-26","entry_price":8950.0,"entry_price_type":"next_tradable_open_after_valueup_spike","price_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","mfe_30d_pct":2.35,"mae_30d_pct":-13.41,"mfe_90d_pct":2.35,"mae_90d_pct":-21.23,"mfe_180d_pct":2.35,"mae_180d_pct":-26.26,"peak_price_180d":9160.0,"peak_date_180d":"2024-02-29","trough_price_180d":6600.0,"trough_date_180d":"2024-08-05","calibration_usable":true,"case_polarity":"counterexample_post_spike_high_mae","evidence_url_pending":true,"source_proxy_only":true,"non_price_evidence_strength":"low_pending_url_repair","price_only_blowoff":false,"expected_stage_current_profile":"blocked_Stage2_or_4B_high_MAE_watch","residual_error_type":"post_spike_brokerage_valueup_entry_low_mfe_high_mae_without_fresh_execution_bridge"}
```

---

## 8. Score simulation and raw component breakdown

This is shadow-only and does not change production scoring.

| symbol | ROE recovery | capital-return visibility | balance-sheet / risk control | market mispricing | valuation rerating | earnings quality | information confidence | shadow total | intended route |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| `071050` | 13 | 11 | 10 | 13 | 13 | 11 | 7 | 78 | Stage2/Yellow after ROE and shareholder-return evidence repair |
| `016360` | 12 | 13 | 11 | 10 | 10 | 10 | 7 | 73 | Stage2/Yellow after capital-return evidence repair |
| `006800` | 8 | 7 | 7 | 5 | 5 | 7 | 5 | 44 | blocked Stage2 or 4B/high-MAE watch |

### Current calibrated profile stress test

The current calibrated profile already blocks pure price-only blowoff.  
The remaining C21 risk is **post-spike financial-theme over-scoring**:

```text
C21 clean brokerage path:
  low-PBR / value-up relevance
  + low MAE
  + persistent MFE
  + URL-repaired ROE and capital-return bridge
  => Stage2-Actionable / Stage3-Yellow, possible Green after proof

C21 post-spike false-positive path:
  financial value-up theme is real
  + entry occurs after first rerating burst
  + MFE_30D < +5%
  + MAE_90D <= -20%
  + no fresh execution evidence
  => block Stage2 or route to local 4B/high-MAE watch
```

`071050` and `016360` prevent overblocking.  
`006800` shows why the model should not treat a brokerage value-up candle as infinitely reusable. Once the rerating spark has already fired, the next entry needs a new ROE/capital-return bridge, not just the old policy label.

---

## 9. Aggregate metrics

```json
{
  "row_type": "aggregate",
  "research_id": "R6L73_C21_BROKERAGE_VALUEUP_CAPITAL_RETURN",
  "round": "R6",
  "loop": 73,
  "large_sector_id": "L6_FINANCIAL_CAPITAL_RETURN_DIGITAL",
  "canonical_archetype_id": "C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN",
  "fine_archetype_id": "BROKERAGE_VALUEUP_ROE_PBR_CAPITAL_RETURN_HIGH_MAE_ROUTER",
  "case_count": 3,
  "calibration_usable_case_count": 3,
  "positive_case_count": 2,
  "counterexample_count": 1,
  "new_symbol_count": 3,
  "source_proxy_only_count": 3,
  "evidence_url_pending_count": 3,
  "avg_mfe_30d_pct": 13.41,
  "avg_mae_30d_pct": -4.51,
  "avg_mfe_90d_pct": 15.23,
  "avg_mae_90d_pct": -8.65,
  "avg_mfe_180d_pct": 19.70,
  "avg_mae_180d_pct": -10.33,
  "max_mfe_180d_pct": 32.37,
  "worst_mae_180d_pct": -26.26
}
```

---

## 10. 4B proximity split

```json
{
  "row_type": "4b_split",
  "research_id": "R6L73_C21_BROKERAGE_VALUEUP_CAPITAL_RETURN",
  "stage2_positive_or_yellow_candidate": [
    {
      "symbol": "071050",
      "reason": "persistent MFE and no adverse excursion; requires URL-repaired ROE/shareholder-return bridge before Green"
    },
    {
      "symbol": "016360",
      "reason": "contained MAE and constructive 180D path; requires capital-return and earnings-quality bridge before Green"
    }
  ],
  "local_4b_watch": [
    {
      "symbol": "006800",
      "reason": "post-spike entry had only +2.35% MFE and MAE_90D reached -21.23%, with MAE_180D at -26.26%"
    }
  ],
  "full_4b_or_green_requires_non_price_evidence": [
    "explicit shareholder-return plan",
    "dividend / buyback / total shareholder return execution",
    "ROE recovery evidence",
    "brokerage earnings mix quality",
    "capital or balance-sheet risk control"
  ]
}
```

---

## 11. Shadow rule candidate

```yaml
row_type: canonical_archetype_rule_candidate
canonical_archetype_id: C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN
fine_archetype_id: BROKERAGE_VALUEUP_ROE_PBR_CAPITAL_RETURN_HIGH_MAE_ROUTER
rule_name: C21_brokerage_valueup_capital_return_post_spike_router
production_scoring_changed: false
shadow_weight_only: true
```

### Proposed routing logic

```text
For C21 brokerage / non-bank financial value-up cases:

Tier A: verified ROE-PBR rerating with capital-return bridge
  Conditions:
    - low-PBR / value-up relevance is clear
    - shareholder-return or ROE recovery evidence is URL-repaired
    - 30D/90D MAE is contained
    - MFE persists beyond first rerating candle
  Routing:
    - Stage2-Actionable allowed
    - Stage3-Yellow allowed after evidence repair
    - Green only after capital-return and earnings-quality evidence is verified

Tier B: source-proxy-only brokerage value-up rally
  Conditions:
    - financial value-up theme is plausible
    - evidence_url_pending or source_proxy_only remains true
    - MAE is contained
  Routing:
    - Stage2-Actionable-Guarded at most
    - no Green until evidence repair

Tier C: post-spike brokerage false-positive
  Conditions:
    - entry follows first rerating burst
    - MFE_30D < +5%
    - MAE_90D <= -20% or MAE_180D <= -25%
    - no fresh shareholder-return / ROE bridge
  Routing:
    - block Stage2
    - local 4B/high-MAE watch
    - count as counterexample
```

### Suggested shadow delta

```json
{
  "row_type": "shadow_weight",
  "axis": "c21_brokerage_valueup_capital_return_post_spike_router",
  "scope": "canonical_archetype_id:C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN",
  "proposal": {
    "source_proxy_only_green_allowed": false,
    "roe_capital_return_bridge_required_for_green": true,
    "brokerage_valueup_stage2_cap": "guarded_only_until_url_repair",
    "post_spike_mfe30_threshold_pct": 5.0,
    "post_spike_high_mae_watch_threshold_90d_pct": -20.0,
    "post_spike_hard_fade_threshold_180d_pct": -25.0,
    "positive_weight_blocked_until_url_repair": true
  },
  "confidence": "medium_low_until_url_repair",
  "apply_now": false,
  "reason": "Two clean brokerage/holding positive paths and one post-spike false-positive show that C21 should reward low-MAE brokerage value-up entries only when ROE and shareholder-return evidence are repaired, while blocking stale post-spike entries with weak MFE and high MAE."
}
```

---

## 12. Residual contribution summary

```json
{
  "row_type": "residual_contribution",
  "research_id": "R6L73_C21_BROKERAGE_VALUEUP_CAPITAL_RETURN",
  "large_sector_id": "L6_FINANCIAL_CAPITAL_RETURN_DIGITAL",
  "canonical_archetype_id": "C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN",
  "contribution": "Adds three non-top-covered C21 brokerage/non-bank financial cases and separates clean low-MAE value-up rerating from a post-spike brokerage entry with weak MFE and high MAE. C21 Green should require URL-repaired ROE recovery, shareholder-return execution, earnings-quality, and capital-risk evidence.",
  "positive_case_added": 2,
  "counterexample_case_added": 1,
  "new_symbol_count": 3,
  "data_quality_blocker": "All three non-price brokerage value-up triggers require URL-level repair before positive weight promotion.",
  "guardrail_added": "C21 post-spike brokerage value-up entries with MFE_30D < +5% and MAE_90D <= -20% or MAE_180D <= -25% should block Stage2 or route to local 4B/high-MAE watch."
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
    071050: false
    016360: false
    006800: false
  evidence_url_pending:
    071050: true
    016360: true
    006800: true
  source_proxy_only:
    071050: true
    016360: true
    006800: true
```

Limitations:

```text
- Price path is validated against Stock-Web tradable OHLC rows.
- Non-price evidence is not URL-repaired in this run.
- Therefore this artifact is useful for C21 brokerage value-up residual shape and post-spike high-MAE guardrail design, but should not promote positive weights until filings/IR/exchange-disclosure/report data verifies ROE recovery, shareholder return, buyback/dividend execution, earnings quality, and balance-sheet risk.
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
2. Preserve R6 / loop 73 metadata.
3. Add the cases to C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN only if parser validation passes.
4. Treat all three non-price triggers as evidence_url_pending=true and source_proxy_only=true until URL-level evidence is repaired.
5. Do not use these rows for positive weight promotion until filings/IR/exchange-disclosure/report data verifies ROE recovery, shareholder-return policy, buyback/dividend execution, brokerage earnings quality, and balance-sheet risk control.
6. Add a shadow-only rule candidate named C21_brokerage_valueup_capital_return_post_spike_router.
7. Do not loosen Stage3-Green.
8. Add C21-specific guards:
   - source_proxy_only -> no Green
   - brokerage value-up rally without repaired ROE/capital-return bridge -> Stage2-Guarded at most
   - post-spike entry with MFE_30D < +5% and MAE_90D <= -20% -> block Stage2 or local 4B/high-MAE watch
   - MAE_180D <= -25% without fresh execution bridge -> hard-fade counterexample
   - Green requires repaired ROE/shareholder-return/earnings-quality bridge
9. Keep production scoring unchanged unless later batch promotion logic independently marks this axis safe.
```

---

## 15. Next round state

```text
completed_round = R6
completed_loop = 73
next_round = R7
next_loop = 73
next_large_sector_hint = L7_BIO_HEALTHCARE_MEDICAL
```
