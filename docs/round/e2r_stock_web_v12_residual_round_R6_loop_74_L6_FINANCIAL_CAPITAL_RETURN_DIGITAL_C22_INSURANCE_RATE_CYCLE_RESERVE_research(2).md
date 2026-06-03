# E2R Stock-Web v12 Residual Research — R6 Loop 74

```yaml
research_session: post_calibrated_sector_archetype_residual_research
mode: historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12
completed_round: R6
completed_loop: 74
next_round: R7
next_loop: 74
large_sector_id: L6_FINANCIAL_CAPITAL_RETURN_DIGITAL
canonical_archetype_id: C22_INSURANCE_RATE_CYCLE_RESERVE
fine_archetype_id: NONBANK_INSURANCE_CSM_KICS_CAPITAL_RETURN_AND_MA_HIGH_MAE_ROUTER
output_file: e2r_stock_web_v12_residual_round_R6_loop_74_L6_FINANCIAL_CAPITAL_RETURN_DIGITAL_C22_INSURANCE_RATE_CYCLE_RESERVE_research.md
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
completed_loop  = 74
large_sector_id = L5_CONSUMER_BRAND_DISTRIBUTION
canonical_archetype_id = C18_CONSUMER_EXPORT_CHANNEL_REORDER
```

Therefore:

```text
scheduled_round = R6
scheduled_loop  = 74
```

R6 maps to:

```text
large_sector_id = L6_FINANCIAL_CAPITAL_RETURN_DIGITAL
```

This run selects:

```text
canonical_archetype_id = C22_INSURANCE_RATE_CYCLE_RESERVE
fine_archetype_id = NONBANK_INSURANCE_CSM_KICS_CAPITAL_RETURN_AND_MA_HIGH_MAE_ROUTER
```

This is a valid R6/L6 pairing.

---

## 1. Why this R6/C22 run

The no-repeat ledger shows C22 is heavily covered, but the most repeated cases are concentrated in large insurers:

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

This file avoids those top-covered names and adds:

```text
003690 코리안리
000370 한화손해보험
082640 동양생명
```

Research question:

```text
Can C22 separate stable insurance/reinsurance capital-return rerating from life-insurance M&A/value-up bursts where the first MFE is real but later MAE reveals execution, K-ICS, or deal-closure risk?
```

C22 is a balance-sheet and reserve-quality archetype. The price can respond to value-up policy, CSM, K-ICS, rate-cycle, or M&A optionality, but Stage2/Yellow should require the actuarial engine to keep turning: reserve quality, solvency headroom, capital-return execution, and earnings durability. If the engine is only a headline, the first rally can become a trap door.

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
| `003690` | 코리안리 | active_like / KOSPI | no 2024 overlap; latest listed candidate 2004-07-20 | true |
| `000370` | 한화손해보험 | active_like / KOSPI | no 2024 overlap; latest listed candidate 2017-11-23 | true |
| `082640` | 동양생명 | active_like / KOSPI | no 2024 overlap; latest listed candidate 2017-04-11 | true |

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
The Stock-Web price path is fully validated, but company-level CSM quality, reserve adequacy, K-ICS solvency, rate-cycle benefit, dividend/buyback policy, M&A finalization, and capital-return execution evidence still require later URL repair through filings, IR decks, insurance solvency disclosures, exchange filings, or sell-side reports before production weight promotion.
```

C22 interpretation used here:

```text
C22 is not simply “insurance stock rose.”
It asks whether insurance rerating is balance-sheet-convertible:
- CSM quality and reserve adequacy,
- K-ICS / solvency headroom,
- rate-cycle or reinsurance pricing benefit,
- capital-return execution,
- M&A / ownership event finality,
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
000370 + C22_INSURANCE_RATE_CYCLE_RESERVE -> no direct match found
003690 + C22_INSURANCE_RATE_CYCLE_RESERVE -> no direct match found
082640 + C22_INSURANCE_RATE_CYCLE_RESERVE -> no direct match found
```

Novelty accounting:

```json
{
  "new_symbol_count": 3,
  "minimum_new_symbol_count": 2,
  "positive_guarded_case_count": 2,
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
| `R6L74_C22_003690_20240202` | `003690` 코리안리 | reinsurance rate-cycle / CSM / capital-return low-MAE rerating | positive-guarded low-MAE holdout |
| `R6L74_C22_000370_20240202` | `000370` 한화손해보험 | non-life value-up / CSM / K-ICS capital-return rerating | positive-guarded but drawdown watch |
| `R6L74_C22_082640_20240627` | `082640` 동양생명 | life-insurance M&A / capital-return optionality burst | high-MFE / high-MAE counterexample |

The intended residual:

```text
C22 should separate:
1. low-MAE insurance/reinsurance paths where capital-return / rate-cycle evidence can later be repaired;
2. non-life value-up paths where MFE is real but drawdown still requires solvency and capital-return proof;
3. life-insurance M&A/value-up bursts where first-window MFE is overwhelmed by later MAE when deal or capital-return execution is unresolved.
```

---

## 6. Stock-Web OHLC and backtest

### 6.1 `003690` 코리안리 — reinsurance rate-cycle / low-MAE CSM rerating

Trigger:

```text
trigger_date = 2024-02-01
trigger_type = Stage2-Actionable-Guarded
trigger_family = reinsurance_rate_cycle_csm_capital_return_low_mae_rerating
entry_date = 2024-02-02
entry_price = 7820.0
entry_price_type = next_tradable_open_after_insurance_valueup_rate_cycle_burst
```

Relevant Stock-Web rows:

```csv
d,o,h,l,c,v,a,mc,s,m
2024-02-01,7580.0,7960.0,7470.0,7810.0,1308385.0,10268194140.0,1291520378060.0,165367526,KOSPI
2024-02-02,7820.0,7960.0,7490.0,7820.0,1344311.0,10421661320.0,1293174053320.0,165367526,KOSPI
2024-02-19,8010.0,8330.0,8010.0,8190.0,969875.0,7929746500.0,1354360037940.0,165367526,KOSPI
2024-03-22,8360.0,8550.0,8340.0,8510.0,486073.0,4105826600.0,1407277646260.0,165367526,KOSPI
2024-04-02,7820.0,8170.0,7820.0,8140.0,1299839.0,10477041850.0,1346091661640.0,165367526,KOSPI
2024-07-30,8220.0,8500.0,8200.0,8440.0,543290.0,4575376080.0,1395701919440.0,165367526,KOSPI
2024-08-05,8100.0,8100.0,7800.0,7880.0,839149.0,6666125540.0,1303096104880.0,165367526,KOSPI
```

Backtest:

| window | peak/high | peak date | trough/low | trough date | MFE | MAE |
|---|---:|---|---:|---|---:|---:|
| 30 calendar days | 8330 | 2024-02-19 | 7490 | 2024-02-02 | +6.52% | -4.22% |
| 90 calendar days | 8550 | 2024-03-22 | 7490 | 2024-02-02 | +9.34% | -4.22% |
| 180 calendar days | 8550 | 2024-03-22 | 7490 | 2024-02-02 | +9.34% | -4.22% |

Interpretation:

```text
003690 is a low-MAE positive-guarded holdout.
The MFE was modest, but the risk path was clean. This is useful for C22 because not every valid insurance rerating has to be explosive.
It can stay Stage2-Guarded / Yellow candidate after CSM, rate-cycle, solvency, and capital-return evidence repair.
```

### 6.2 `000370` 한화손해보험 — non-life value-up / CSM / K-ICS rerating with drawdown watch

Trigger:

```text
trigger_date = 2024-02-01
trigger_type = Stage2-Actionable-Guarded
trigger_family = nonlife_insurance_valueup_csm_kics_capital_return_rerating
entry_date = 2024-02-02
entry_price = 5000.0
entry_price_type = next_tradable_open_after_nonlife_insurance_valueup_burst
```

Relevant Stock-Web rows:

```csv
d,o,h,l,c,v,a,mc,s,m
2024-02-01,4320.0,5640.0,4150.0,5120.0,31984623.0,167160468105.0,597703244800.0,116738915,KOSPI
2024-02-02,5000.0,5430.0,4790.0,5320.0,11917018.0,61275461515.0,621051027800.0,116738915,KOSPI
2024-02-13,5590.0,6170.0,5380.0,5520.0,22178568.0,129162465550.0,644398810800.0,116738915,KOSPI
2024-02-28,4570.0,4790.0,4500.0,4725.0,1735197.0,8016707510.0,551591373375.0,116738915,KOSPI
2024-04-15,4105.0,4275.0,4085.0,4265.0,295165.0,1237150110.0,497891472475.0,116738915,KOSPI
2024-05-21,5290.0,5390.0,5260.0,5310.0,572910.0,3062184760.0,619883638650.0,116738915,KOSPI
2024-07-31,5390.0,5720.0,5360.0,5650.0,1793708.0,10068154500.0,659574869750.0,116738915,KOSPI
```

Backtest:

| window | peak/high | peak date | trough/low | trough date | MFE | MAE |
|---|---:|---|---:|---|---:|---:|
| 30 calendar days | 6170 | 2024-02-13 | 4500 | 2024-02-28 | +23.40% | -10.00% |
| 90 calendar days | 6170 | 2024-02-13 | 4085 | 2024-04-15 | +23.40% | -18.30% |
| 180 calendar days | 6170 | 2024-02-13 | 4085 | 2024-04-15 | +23.40% | -18.30% |

Interpretation:

```text
000370 is positive but guarded.
The first-window MFE was real, but the subsequent MAE was large enough to block Green without company-specific solvency, reserve, CSM, and capital-return proof.
This is not a hard false positive; it is a Stage2-Guarded insurance rerating with evidence repair required.
```

### 6.3 `082640` 동양생명 — life-insurance M&A/value-up burst with high MAE

Trigger:

```text
trigger_date = 2024-06-26
trigger_type = Stage2-FalsePositive-Candidate
trigger_family = life_insurance_ma_capital_return_rumor_high_mfe_high_mae
entry_date = 2024-06-27
entry_price = 7340.0
entry_price_type = next_tradable_open_after_life_insurance_ma_valueup_burst
```

Relevant Stock-Web rows:

```csv
d,o,h,l,c,v,a,mc,s,m
2024-06-26,6710.0,7500.0,6630.0,7000.0,4510201.0,32145098140.0,1129510095000.0,161358585,KOSPI
2024-06-27,7340.0,7340.0,6680.0,7200.0,2301850.0,16286708830.0,1161781812000.0,161358585,KOSPI
2024-07-02,7660.0,9340.0,7640.0,8450.0,10225276.0,89993017340.0,1363480043250.0,161358585,KOSPI
2024-07-31,7930.0,9440.0,7710.0,7970.0,2952682.0,25466445060.0,1286027922450.0,161358585,KOSPI
2024-08-28,8500.0,8900.0,6900.0,6980.0,3254686.0,24367211630.0,1126282923300.0,161358585,KOSPI
2024-09-25,5620.0,5650.0,5450.0,5450.0,303118.0,1671772110.0,879404288250.0,161358585,KOSPI
2024-12-17,5440.0,5510.0,4615.0,4640.0,4351260.0,21010908480.0,748703834400.0,161358585,KOSPI
2024-12-19,4580.0,4685.0,4575.0,4585.0,633035.0,2914009675.0,739829112225.0,161358585,KOSPI
```

Backtest:

| window | peak/high | peak date | trough/low | trough date | MFE | MAE |
|---|---:|---|---:|---|---:|---:|
| 30 calendar days | 9340 | 2024-07-02 | 6680 | 2024-06-27 | +27.25% | -8.99% |
| 90 calendar days | 9440 | 2024-07-31 | 5450 | 2024-09-25 | +28.61% | -25.75% |
| 180 calendar days | 9440 | 2024-07-31 | 4575 | 2024-12-19 | +28.61% | -37.67% |

Interpretation:

```text
082640 is the high-MFE / high-MAE counterexample.
The M&A/value-up optionality created real upside, but the later 90D/180D path crossed high-MAE guardrails.
C22 should cap this at Stage2-Guarded or local 4B/high-MAE watch until deal finality, K-ICS, CSM, and capital-return execution are repaired.
```

---

## 7. Machine-readable trigger JSONL

```jsonl
{"row_type":"trigger","research_id":"R6L74_C22_INSURANCE_RATE_CSM_ROUTER","round":"R6","loop":74,"large_sector_id":"L6_FINANCIAL_CAPITAL_RETURN_DIGITAL","canonical_archetype_id":"C22_INSURANCE_RATE_CYCLE_RESERVE","fine_archetype_id":"NONBANK_INSURANCE_CSM_KICS_CAPITAL_RETURN_AND_MA_HIGH_MAE_ROUTER","symbol":"003690","name":"코리안리","trigger_type":"Stage2-Actionable-Guarded","trigger_family":"reinsurance_rate_cycle_csm_capital_return_low_mae_rerating","trigger_date":"2024-02-01","entry_date":"2024-02-02","entry_price":7820.0,"entry_price_type":"next_tradable_open_after_insurance_valueup_rate_cycle_burst","price_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","mfe_30d_pct":6.52,"mae_30d_pct":-4.22,"mfe_90d_pct":9.34,"mae_90d_pct":-4.22,"mfe_180d_pct":9.34,"mae_180d_pct":-4.22,"peak_price_180d":8550.0,"peak_date_180d":"2024-03-22","trough_price_180d":7490.0,"trough_date_180d":"2024-02-02","calibration_usable":true,"case_polarity":"positive_guarded_low_mae","evidence_url_pending":true,"source_proxy_only":true,"non_price_evidence_strength":"medium_pending_url_repair","price_only_blowoff":false,"expected_stage_current_profile":"Stage2-Guarded_to_Yellow_if_reinsurance_rate_csm_capital_return_bridge_repaired","residual_error_type":"low_mae_reinsurance_rate_cycle_path_requires_url_repaired_csm_kics_capital_return_bridge_before_green"}
{"row_type":"trigger","research_id":"R6L74_C22_INSURANCE_RATE_CSM_ROUTER","round":"R6","loop":74,"large_sector_id":"L6_FINANCIAL_CAPITAL_RETURN_DIGITAL","canonical_archetype_id":"C22_INSURANCE_RATE_CYCLE_RESERVE","fine_archetype_id":"NONBANK_INSURANCE_CSM_KICS_CAPITAL_RETURN_AND_MA_HIGH_MAE_ROUTER","symbol":"000370","name":"한화손해보험","trigger_type":"Stage2-Actionable-Guarded","trigger_family":"nonlife_insurance_valueup_csm_kics_capital_return_rerating","trigger_date":"2024-02-01","entry_date":"2024-02-02","entry_price":5000.0,"entry_price_type":"next_tradable_open_after_nonlife_insurance_valueup_burst","price_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","mfe_30d_pct":23.4,"mae_30d_pct":-10.0,"mfe_90d_pct":23.4,"mae_90d_pct":-18.3,"mfe_180d_pct":23.4,"mae_180d_pct":-18.3,"peak_price_180d":6170.0,"peak_date_180d":"2024-02-13","trough_price_180d":4085.0,"trough_date_180d":"2024-04-15","calibration_usable":true,"case_polarity":"positive_guarded_high_mfe_drawdown_watch","evidence_url_pending":true,"source_proxy_only":true,"non_price_evidence_strength":"medium_low_pending_url_repair","price_only_blowoff":false,"expected_stage_current_profile":"Stage2-Guarded_only_until_csm_kics_capital_return_evidence_repaired","residual_error_type":"nonlife_valueup_mfe_was_real_but_drawdown_requires_csm_kics_capital_return_bridge_before_yellow_green"}
{"row_type":"trigger","research_id":"R6L74_C22_INSURANCE_RATE_CSM_ROUTER","round":"R6","loop":74,"large_sector_id":"L6_FINANCIAL_CAPITAL_RETURN_DIGITAL","canonical_archetype_id":"C22_INSURANCE_RATE_CYCLE_RESERVE","fine_archetype_id":"NONBANK_INSURANCE_CSM_KICS_CAPITAL_RETURN_AND_MA_HIGH_MAE_ROUTER","symbol":"082640","name":"동양생명","trigger_type":"Stage2-FalsePositive-Candidate","trigger_family":"life_insurance_ma_capital_return_rumor_high_mfe_high_mae","trigger_date":"2024-06-26","entry_date":"2024-06-27","entry_price":7340.0,"entry_price_type":"next_tradable_open_after_life_insurance_ma_valueup_burst","price_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","mfe_30d_pct":27.25,"mae_30d_pct":-8.99,"mfe_90d_pct":28.61,"mae_90d_pct":-25.75,"mfe_180d_pct":28.61,"mae_180d_pct":-37.67,"peak_price_180d":9440.0,"peak_date_180d":"2024-07-31","trough_price_180d":4575.0,"trough_date_180d":"2024-12-19","calibration_usable":true,"case_polarity":"counterexample_high_mfe_high_mae","evidence_url_pending":true,"source_proxy_only":true,"non_price_evidence_strength":"low_pending_url_repair","price_only_blowoff":false,"expected_stage_current_profile":"Stage2-Guarded_or_4B_high_MAE_watch_until_ma_capital_return_kics_bridge_repaired","residual_error_type":"life_insurance_ma_valueup_mfe_overwhelmed_by_90d_180d_high_mae_without_final_execution_bridge"}
```

---

## 8. Score simulation and raw component breakdown

This is shadow-only and does not change production scoring.

| symbol | CSM / reserve quality | K-ICS / solvency bridge | rate-cycle / pricing benefit | capital-return visibility | market mispricing | execution / event risk control | information confidence | shadow total | intended route |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| `003690` | 10 | 9 | 12 | 8 | 7 | 10 | 6 | 62 | Stage2-Guarded / Yellow after evidence repair |
| `000370` | 10 | 7 | 8 | 9 | 12 | 5 | 5 | 56 | Stage2-Guarded; drawdown watch until CSM/K-ICS bridge repaired |
| `082640` | 6 | 4 | 5 | 7 | 13 | 2 | 4 | 41 | Stage2-Guarded or 4B/high-MAE watch |

### Current calibrated profile stress test

The current calibrated profile already blocks pure price-only blowoff.  
The remaining C22 issue is **insurance value-up or M&A optionality without solvency/capital-return execution**:

```text
C22 low-MAE insurance path:
  rate-cycle / CSM / capital-return relevance
  + MAE remains contained
  + URL-repaired solvency and capital-return bridge
  => Stage2-Guarded / Yellow candidate

C22 high-MFE drawdown path:
  value-up or non-life rerating produces MFE
  + MAE approaches -20%
  + evidence remains source_proxy_only
  => Stage2-Guarded only, no Green

C22 M&A/value-up high-MAE trap:
  life-insurance event optionality produces MFE
  + 90D MAE <= -25% or 180D MAE <= -35%
  + final execution bridge missing
  => local 4B/high-MAE watch, no Green
```

`003690` prevents overblocking.  
`000370` shows why real insurance rerating still needs drawdown-aware evidence repair.  
`082640` shows that first-window MFE from M&A/value-up optionality is not enough when the later path carries severe MAE.

---

## 9. Aggregate metrics

```json
{
  "row_type": "aggregate",
  "research_id": "R6L74_C22_INSURANCE_RATE_CSM_ROUTER",
  "round": "R6",
  "loop": 74,
  "large_sector_id": "L6_FINANCIAL_CAPITAL_RETURN_DIGITAL",
  "canonical_archetype_id": "C22_INSURANCE_RATE_CYCLE_RESERVE",
  "fine_archetype_id": "NONBANK_INSURANCE_CSM_KICS_CAPITAL_RETURN_AND_MA_HIGH_MAE_ROUTER",
  "case_count": 3,
  "calibration_usable_case_count": 3,
  "positive_guarded_case_count": 2,
  "counterexample_count": 1,
  "new_symbol_count": 3,
  "source_proxy_only_count": 3,
  "evidence_url_pending_count": 3,
  "avg_mfe_30d_pct": 19.06,
  "avg_mae_30d_pct": -7.74,
  "avg_mfe_90d_pct": 20.45,
  "avg_mae_90d_pct": -16.09,
  "avg_mfe_180d_pct": 20.45,
  "avg_mae_180d_pct": -20.06,
  "max_mfe_180d_pct": 28.61,
  "worst_mae_180d_pct": -37.67
}
```

---

## 10. 4B proximity split

```json
{
  "row_type": "4b_split",
  "research_id": "R6L74_C22_INSURANCE_RATE_CSM_ROUTER",
  "stage2_guarded_or_yellow_candidate": [
    {
      "symbol": "003690",
      "reason": "low-MAE reinsurance/rate-cycle path; MFE is modest but capital preservation is strong"
    },
    {
      "symbol": "000370",
      "reason": "real +23.40% MFE but -18.30% 90D/180D MAE; requires CSM/K-ICS/capital-return evidence before Yellow/Green"
    }
  ],
  "local_4b_high_mae_watch": [
    {
      "symbol": "082640",
      "reason": "M&A/value-up MFE was real, but MAE_90D reached -25.75% and MAE_180D reached -37.67%"
    }
  ],
  "full_4b_or_green_requires_non_price_evidence": [
    "CSM quality and reserve adequacy",
    "K-ICS / solvency headroom",
    "rate-cycle or pricing benefit",
    "dividend / buyback / total shareholder return execution",
    "M&A finality and ownership-event resolution",
    "earnings durability and capital policy"
  ]
}
```

---

## 11. Shadow rule candidate

```yaml
row_type: canonical_archetype_rule_candidate
canonical_archetype_id: C22_INSURANCE_RATE_CYCLE_RESERVE
fine_archetype_id: NONBANK_INSURANCE_CSM_KICS_CAPITAL_RETURN_AND_MA_HIGH_MAE_ROUTER
rule_name: C22_insurance_csm_kics_capital_return_and_ma_high_mae_router
production_scoring_changed: false
shadow_weight_only: true
```

### Proposed routing logic

```text
For C22 insurance rate-cycle / reserve / CSM / capital-return cases:

Tier A: verified insurance rerating with solvency bridge
  Conditions:
    - CSM / reserve quality / K-ICS evidence is URL-repaired
    - capital-return policy is visible or later executed
    - 30D/90D MAE remains contained
    - MFE persists beyond one value-up candle
  Routing:
    - Stage2-Actionable-Guarded allowed
    - Stage3-Yellow allowed after evidence repair
    - Green only after solvency and capital-return bridge are verified

Tier B: high-MFE insurance rerating with drawdown watch
  Conditions:
    - MFE_30D >= +20%
    - MAE_90D <= -15%
    - bridge evidence remains source_proxy_only
  Routing:
    - Stage2-Guarded at most
    - no Green
    - require URL repair before positive weight promotion

Tier C: M&A / value-up event high-MAE trap
  Conditions:
    - event optionality produces MFE
    - MAE_90D <= -25% or MAE_180D <= -35%
    - M&A finality / capital-return / solvency bridge is missing
  Routing:
    - local 4B/high-MAE watch
    - block Green
    - count as counterexample
```

### Suggested shadow delta

```json
{
  "row_type": "shadow_weight",
  "axis": "c22_insurance_csm_kics_capital_return_and_ma_high_mae_router",
  "scope": "canonical_archetype_id:C22_INSURANCE_RATE_CYCLE_RESERVE",
  "proposal": {
    "source_proxy_only_green_allowed": false,
    "csm_kics_capital_return_bridge_required_for_green": true,
    "low_mae_reinsurance_stage2_guarded_allowed": true,
    "high_mfe_threshold_30d_pct": 20.0,
    "drawdown_watch_threshold_90d_pct": -15.0,
    "ma_event_high_mae_threshold_90d_pct": -25.0,
    "ma_event_hard_mae_threshold_180d_pct": -35.0,
    "positive_weight_blocked_until_url_repair": true
  },
  "confidence": "medium_low_until_url_repair",
  "apply_now": false,
  "reason": "Two non-top-covered insurance/reinsurance guarded cases and one life-insurance M&A high-MAE counterexample show that C22 should require URL-repaired CSM, K-ICS, reserve, capital-return, and event-finality evidence before Yellow/Green."
}
```

---

## 12. Residual contribution summary

```json
{
  "row_type": "residual_contribution",
  "research_id": "R6L74_C22_INSURANCE_RATE_CSM_ROUTER",
  "large_sector_id": "L6_FINANCIAL_CAPITAL_RETURN_DIGITAL",
  "canonical_archetype_id": "C22_INSURANCE_RATE_CYCLE_RESERVE",
  "contribution": "Adds three non-top-covered C22 insurance/reinsurance cases and separates low-MAE reinsurance/rate-cycle rerating from non-life drawdown-watch and life-insurance M&A/value-up high-MAE event risk. C22 Green should require URL-repaired CSM quality, reserve adequacy, K-ICS solvency, capital-return execution, and M&A/event finality evidence.",
  "positive_guarded_case_added": 2,
  "counterexample_case_added": 1,
  "new_symbol_count": 3,
  "data_quality_blocker": "All three non-price insurance/rate/CSM triggers require URL-level repair before positive weight promotion.",
  "guardrail_added": "C22 source_proxy_only cases with MFE_30D >= +20% and MAE_90D <= -15% should cap at Stage2-Guarded; M&A/value-up cases with MAE_90D <= -25% or MAE_180D <= -35% should route to local 4B/high-MAE watch."
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
    003690: false
    000370: false
    082640: false
  evidence_url_pending:
    003690: true
    000370: true
    082640: true
  source_proxy_only:
    003690: true
    000370: true
    082640: true
```

Limitations:

```text
- Price path is validated against Stock-Web tradable OHLC rows.
- Non-price evidence is not URL-repaired in this run.
- Therefore this artifact is useful for C22 insurance CSM/K-ICS/capital-return residual shape and high-MAE event guardrail design, but should not promote positive weights until filings, IR, solvency disclosures, exchange disclosures, or reports verify CSM quality, reserve adequacy, K-ICS, capital-return execution, and M&A/event finality.
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
2. Preserve R6 / loop 74 metadata.
3. Add the cases to C22_INSURANCE_RATE_CYCLE_RESERVE only if parser validation passes.
4. Treat all three non-price triggers as evidence_url_pending=true and source_proxy_only=true until URL-level evidence is repaired.
5. Do not use these rows for positive weight promotion until filings/IR/solvency-disclosure/exchange-disclosure/report data verifies CSM quality, reserve adequacy, K-ICS solvency, capital-return policy/execution, and M&A/event finality.
6. Add a shadow-only rule candidate named C22_insurance_csm_kics_capital_return_and_ma_high_mae_router.
7. Do not loosen Stage3-Green.
8. Add C22-specific guards:
   - source_proxy_only -> no Green
   - Green requires repaired CSM/K-ICS/reserve/capital-return bridge
   - MFE_30D >= +20% and MAE_90D <= -15% without evidence repair -> Stage2-Guarded at most
   - M&A/value-up event with MAE_90D <= -25% or MAE_180D <= -35% -> local 4B/high-MAE watch
   - low-MAE reinsurance/rate-cycle cases may remain Stage2-Guarded until evidence repair
9. Keep production scoring unchanged unless later batch promotion logic independently marks this axis safe.
```

---

## 15. Next round state

```text
completed_round = R6
completed_loop = 74
next_round = R7
next_loop = 74
next_large_sector_hint = L7_BIO_HEALTHCARE_MEDICAL
```
