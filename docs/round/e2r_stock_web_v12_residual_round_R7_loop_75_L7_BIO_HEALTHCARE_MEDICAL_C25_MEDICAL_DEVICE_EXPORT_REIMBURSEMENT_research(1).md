# E2R Stock-Web v12 Residual Research — R7 Loop 75

```yaml
research_session: post_calibrated_sector_archetype_residual_research
mode: historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12
completed_round: R7
completed_loop: 75
next_round: R8
next_loop: 75
large_sector_id: L7_BIO_HEALTHCARE_MEDICAL
canonical_archetype_id: C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT
fine_archetype_id: AESTHETIC_DEVICE_WOUNDCARE_XRAY_EXPORT_REIMBURSEMENT_AND_HIGH_MAE_ROUTER
output_file: e2r_stock_web_v12_residual_round_R7_loop_75_L7_BIO_HEALTHCARE_MEDICAL_C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT_research.md
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
completed_round = R6
completed_loop  = 75
large_sector_id = L6_FINANCIAL_CAPITAL_RETURN_DIGITAL
canonical_archetype_id = C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN
```

Therefore:

```text
scheduled_round = R7
scheduled_loop  = 75
```

R7 maps to:

```text
large_sector_id = L7_BIO_HEALTHCARE_MEDICAL
```

This run selects:

```text
canonical_archetype_id = C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT
fine_archetype_id = AESTHETIC_DEVICE_WOUNDCARE_XRAY_EXPORT_REIMBURSEMENT_AND_HIGH_MAE_ROUTER
```

This is a valid R7/L7 pairing.

---

## 1. Why this R7/C25 run

The no-repeat ledger shows C25 is covered but still materially smaller than C23 and less concentrated than the broad consumer/financial buckets:

```text
C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT:
  rows: 83
  symbols: 17
  date_range: 2022-05-11~2024-05-09
  good/bad S2: 35/8
  4B/4C: 15/4
  URL/proxy: 0/0
  top covered symbols: 338220(17), 214150(14), 145720(8), 099190(6), 228670(6), 335890(5)
```

This file avoids those top-covered names and expands the C25 sample into:

```text
340570 티앤엘
336570 원텍
214680 디알텍
263690 디알젬
```

Research question:

```text
Can C25 separate true medical consumable export/reorder rerating from aesthetic-device and X-ray-device export labels where first-window MFE exists, but later MAE shows customer reorder, reimbursement, export-order, and margin evidence was not yet durable?
```

C25 is a reimbursement/export bridge archetype. A device or consumable can sell abroad, but Stage2 only becomes sturdy when the sale repeats, reimbursement or distributor access sticks, customer quality improves, and gross margin converts. A one-time device headline is a catalog page; a rerating needs reorder receipts.

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
| `340570` | 티앤엘 | active_like / KOSDAQ | no 2024 overlap; listed candidates were 2021 only | true |
| `336570` | 원텍 | active_like / KOSDAQ | no 2024 overlap; 2022-06-30 candidate before selected window | true |
| `214680` | 디알텍 | active_like / KOSDAQ | no 2024 overlap; 2016-12-05 candidate before selected window | true |
| `263690` | 디알젬 | active_like / KOSDAQ | none listed | true |

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
The Stock-Web price path is fully validated, but company-level export order, distributor reorder, reimbursement access, installed-base expansion, customer quality, device consumable pull-through, ASP, gross margin, and operating leverage evidence still require later URL repair through filings, IR decks, export data, contract disclosures, or sell-side reports before production weight promotion.
```

C25 interpretation used here:

```text
C25 is not simply “medical device stock rose.”
It asks whether medical-device or consumable demand is export/reimbursement-convertible:
- export order / distributor reorder,
- reimbursement or clinical-channel access,
- installed-base and repeat consumable demand,
- customer quality,
- ASP and product mix,
- gross margin and operating leverage,
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
340570 + C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT -> no direct match found
336570 + C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT -> no direct match found
214680 + C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT -> no direct match found
263690 + C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT -> no direct match found
```

Novelty accounting:

```json
{
  "new_symbol_count": 4,
  "minimum_new_symbol_count": 2,
  "positive_case_count": 1,
  "counterexample_count": 3,
  "new_independent_case_ratio": 1.00,
  "duplicate_status": "pass",
  "data_quality_status": "source_proxy_only_non_price_evidence"
}
```

---

## 5. Case design

| case_id | symbol | trigger family | research role |
|---|---|---|---|
| `R7L75_C25_340570_20240319` | `340570` 티앤엘 | wound-care medical consumable export/reorder margin rerating | positive anchor |
| `R7L75_C25_336570_20240326` | `336570` 원텍 | aesthetic laser export growth with initial MFE / later high MAE | guarded high-MAE counterexample |
| `R7L75_C25_214680_20240716` | `214680` 디알텍 | digital X-ray detector export theme spike | weak-MFE extreme-MAE counterexample |
| `R7L75_C25_263690_20240510` | `263690` 디알젬 | medical X-ray export/reimbursement label | weak-MFE slow-fade counterexample |

The intended residual:

```text
C25 should separate:
1. consumable export/reorder paths where MFE persists and MAE remains low;
2. aesthetic-device paths where first-window MFE exists but later MAE blocks Green;
3. medical imaging/X-ray labels where the device export story produces weak MFE and high MAE without export-order or reimbursement bridge repair.
```

---

## 6. Stock-Web OHLC and backtest

### 6.1 `340570` 티앤엘 — wound-care consumable export/reorder positive anchor

Trigger:

```text
trigger_date = 2024-03-18
trigger_type = Stage2-Actionable
trigger_family = woundcare_medical_consumable_export_reorder_margin_rerating
entry_date = 2024-03-19
entry_price = 50500.0
entry_price_type = next_tradable_open_after_woundcare_export_reorder_burst
```

Relevant Stock-Web rows:

```csv
d,o,h,l,c,v,a,mc,s,m
2024-03-18,47600.0,48200.0,46600.0,47350.0,61407.0,2920744300.0,384860800000.0,8128000,KOSDAQ
2024-03-19,50500.0,52700.0,49850.0,51300.0,450689.0,23133609850.0,416966400000.0,8128000,KOSDAQ
2024-03-29,52200.0,54100.0,51600.0,53600.0,121466.0,6468531400.0,435660800000.0,8128000,KOSDAQ
2024-04-11,61000.0,63500.0,58000.0,59900.0,346955.0,21133689100.0,486867200000.0,8128000,KOSDAQ
2024-05-16,65300.0,71600.0,64100.0,70800.0,658584.0,45076416300.0,575462400000.0,8128000,KOSDAQ
2024-06-24,70000.0,74100.0,69500.0,71600.0,236914.0,17075471300.0,581964800000.0,8128000,KOSDAQ
2024-08-05,56700.0,57000.0,50400.0,53500.0,230099.0,12438957400.0,434848000000.0,8128000,KOSDAQ
2024-08-21,75800.0,77000.0,73000.0,74500.0,215649.0,16126146100.0,605536000000.0,8128000,KOSDAQ
2024-09-13,65500.0,66900.0,64900.0,66500.0,54617.0,3600090100.0,540512000000.0,8128000,KOSDAQ
```

Backtest:

| window | peak/high | peak date | trough/low | trough date | MFE | MAE |
|---|---:|---|---:|---|---:|---:|
| 30 calendar days | 63500 | 2024-04-11 | 49850 | 2024-03-19 | +25.74% | -1.29% |
| 90 calendar days | 71600 | 2024-05-16 | 49850 | 2024-03-19 | +41.78% | -1.29% |
| 180 calendar days | 77000 | 2024-08-21 | 49850 | 2024-03-19 | +52.48% | -1.29% |

Interpretation:

```text
340570 is the C25 positive anchor.
The path had persistent MFE and almost no MAE, which is the correct geometry for a medical consumable export/reorder rerating.
It can support Stage2-Actionable / Yellow after evidence repair. Green still requires URL-repaired export reorder, customer, distributor, reimbursement/channel, and margin evidence.
```

### 6.2 `336570` 원텍 — aesthetic laser device initial-MFE / later high-MAE branch

Trigger:

```text
trigger_date = 2024-03-25
trigger_type = Stage2-Actionable-Guarded
trigger_family = aesthetic_laser_device_export_growth_initial_mfe_later_high_mae
entry_date = 2024-03-26
entry_price = 9800.0
entry_price_type = next_tradable_open_after_aesthetic_device_export_burst
```

Relevant Stock-Web rows:

```csv
d,o,h,l,c,v,a,mc,s,m
2024-03-25,8400.0,9990.0,8360.0,9890.0,15405837.0,148066600290.0,872040019350.0,88173915,KOSDAQ
2024-03-26,9800.0,9920.0,9510.0,9580.0,4042711.0,39294363620.0,844706105700.0,88173915,KOSDAQ
2024-03-28,9310.0,9810.0,9260.0,9720.0,3510884.0,33936366030.0,857050453800.0,88173915,KOSDAQ
2024-04-19,11160.0,11850.0,11000.0,11570.0,4459962.0,51094829020.0,1020172196550.0,88173915,KOSDAQ
2024-04-22,11580.0,12000.0,10690.0,10860.0,4213557.0,48057138740.0,957568716900.0,88173915,KOSDAQ
2024-05-29,8030.0,8030.0,7350.0,7540.0,2977239.0,22648148410.0,673628267260.0,89340619,KOSDAQ
2024-06-05,7500.0,7500.0,7270.0,7350.0,749995.0,5517804640.0,656653549650.0,89340619,KOSDAQ
2024-08-05,6400.0,6410.0,5690.0,5940.0,1839225.0,11271665020.0,530683276860.0,89340619,KOSDAQ
2024-08-26,5670.0,5730.0,5560.0,5650.0,402990.0,2269781090.0,504774497350.0,89340619,KOSDAQ
```

Backtest:

| window | peak/high | peak date | trough/low | trough date | MFE | MAE |
|---|---:|---|---:|---|---:|---:|
| 30 calendar days | 12000 | 2024-04-22 | 9260 | 2024-03-28 | +22.45% | -5.51% |
| 90 calendar days | 12000 | 2024-04-22 | 7270 | 2024-06-05 | +22.45% | -25.82% |
| 180 calendar days | 12000 | 2024-04-22 | 5560 | 2024-08-26 | +22.45% | -43.27% |

Interpretation:

```text
336570 is the C25 first-window-MFE / later-MAE warning.
The first window looked investable, but 90D and 180D drawdown crossed high-MAE guardrails.
This should stay Stage2-Guarded or local 4B/high-MAE watch until aesthetic-device export, reorder, consumable pull-through, and margin evidence are repaired.
```

### 6.3 `214680` 디알텍 — digital X-ray detector export-theme spike

Trigger:

```text
trigger_date = 2024-07-15
trigger_type = Stage2-FalsePositive-Candidate
trigger_family = digital_xray_detector_export_theme_spike_high_mae
entry_date = 2024-07-16
entry_price = 4290.0
entry_price_type = next_tradable_open_after_xray_detector_export_theme_spike
```

Relevant Stock-Web rows:

```csv
d,o,h,l,c,v,a,mc,s,m
2024-07-15,3965.0,4465.0,3855.0,4145.0,26550964.0,111571474250.0,305598862660.0,73727108,KOSDAQ
2024-07-16,4290.0,4290.0,4100.0,4130.0,7161123.0,29945926175.0,304492956040.0,73727108,KOSDAQ
2024-07-19,4480.0,4550.0,3860.0,3860.0,11516003.0,49089894245.0,284586636880.0,73727108,KOSDAQ
2024-08-05,3490.0,3490.0,2840.0,2975.0,3216798.0,10205988105.0,219338146300.0,73727108,KOSDAQ
2024-09-09,2670.0,2880.0,2655.0,2805.0,770384.0,2099520025.0,206804537940.0,73727108,KOSDAQ
2024-10-07,3080.0,3460.0,3020.0,3275.0,22808670.0,75762110650.0,241456278700.0,73727108,KOSDAQ
2024-12-09,2115.0,2170.0,1997.0,1997.0,1588998.0,3226046034.0,147796480238.0,74009254,KOSDAQ
2025-01-10,2415.0,2415.0,2345.0,2355.0,314371.0,744059275.0,174305923170.0,74015254,KOSDAQ
```

Backtest:

| window | peak/high | peak date | trough/low | trough date | MFE | MAE |
|---|---:|---|---:|---|---:|---:|
| 30 calendar days | 4550 | 2024-07-19 | 2840 | 2024-08-05 | +6.06% | -33.80% |
| 90 calendar days | 4550 | 2024-07-19 | 2655 | 2024-09-09 | +6.06% | -38.11% |
| 180 calendar days | 4550 | 2024-07-19 | 1997 | 2024-12-09 | +6.06% | -53.45% |

Interpretation:

```text
214680 is the hard X-ray detector false positive.
The device/export theme had a large event candle, but the forward path delivered only +6.06% MFE against -53.45% 180D MAE.
This should block Stage2 or route to 4B/4C high-MAE watch unless export order, customer quality, reimbursement/channel access, and margin evidence were repaired before entry.
```

### 6.4 `263690` 디알젬 — medical X-ray export/reimbursement weak-MFE slow fade

Trigger:

```text
trigger_date = 2024-05-09
trigger_type = Stage2-FalsePositive-Candidate
trigger_family = medical_xray_export_reimbursement_label_weak_mfe_slow_fade
entry_date = 2024-05-10
entry_price = 9710.0
entry_price_type = next_tradable_open_after_medical_xray_export_label_spike
```

Relevant Stock-Web rows:

```csv
d,o,h,l,c,v,a,mc,s,m
2024-05-09,10070.0,11240.0,9700.0,9700.0,171885.0,1788130880.0,109858417000.0,11325610,KOSDAQ
2024-05-10,9710.0,9920.0,9700.0,9830.0,10408.0,101896880.0,111330746300.0,11325610,KOSDAQ
2024-05-14,9890.0,10000.0,9760.0,10000.0,9717.0,96336880.0,113256100000.0,11325610,KOSDAQ
2024-06-04,9200.0,9200.0,8940.0,8970.0,21716.0,195860900.0,101590721700.0,11325610,KOSDAQ
2024-08-05,7930.0,7930.0,7170.0,7280.0,63642.0,478454600.0,82450440800.0,11325610,KOSDAQ
2024-10-23,7450.0,7450.0,7100.0,7130.0,8698.0,62324180.0,80751599300.0,11325610,KOSDAQ
2024-11-04,6790.0,6790.0,6600.0,6700.0,3406.0,22658030.0,75881587000.0,11325610,KOSDAQ
```

Backtest:

| window | peak/high | peak date | trough/low | trough date | MFE | MAE |
|---|---:|---|---:|---|---:|---:|
| 30 calendar days | 10000 | 2024-05-14 | 8940 | 2024-06-04 | +2.99% | -7.93% |
| 90 calendar days | 10000 | 2024-05-14 | 7170 | 2024-08-05 | +2.99% | -26.16% |
| 180 calendar days | 10000 | 2024-05-14 | 6600 | 2024-11-04 | +2.99% | -32.03% |

Interpretation:

```text
263690 is the weak-MFE slow-fade branch.
The X-ray medical device label existed, but post-entry MFE stayed below +3% while 90D/180D MAE crossed severe watch thresholds.
This should block Green and generally block Stage2 unless a fresh export-order/reimbursement bridge appears before entry.
```

---

## 7. Machine-readable trigger JSONL

```jsonl
{"row_type":"trigger","research_id":"R7L75_C25_MEDTECH_EXPORT_DEVICE_ROUTER","round":"R7","loop":75,"large_sector_id":"L7_BIO_HEALTHCARE_MEDICAL","canonical_archetype_id":"C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT","fine_archetype_id":"AESTHETIC_DEVICE_WOUNDCARE_XRAY_EXPORT_REIMBURSEMENT_AND_HIGH_MAE_ROUTER","symbol":"340570","name":"티앤엘","trigger_type":"Stage2-Actionable","trigger_family":"woundcare_medical_consumable_export_reorder_margin_rerating","trigger_date":"2024-03-18","entry_date":"2024-03-19","entry_price":50500.0,"entry_price_type":"next_tradable_open_after_woundcare_export_reorder_burst","price_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","mfe_30d_pct":25.74,"mae_30d_pct":-1.29,"mfe_90d_pct":41.78,"mae_90d_pct":-1.29,"mfe_180d_pct":52.48,"mae_180d_pct":-1.29,"peak_price_180d":77000.0,"peak_date_180d":"2024-08-21","trough_price_180d":49850.0,"trough_date_180d":"2024-03-19","calibration_usable":true,"case_polarity":"positive_anchor_low_mae_medical_consumable_export","evidence_url_pending":true,"source_proxy_only":true,"non_price_evidence_strength":"medium_pending_url_repair","price_only_blowoff":false,"expected_stage_current_profile":"Stage2-Actionable_to_Yellow_after_export_reorder_margin_bridge_repaired","residual_error_type":"positive_woundcare_consumable_export_path_requires_url_repaired_export_reorder_customer_margin_evidence_before_green"}
{"row_type":"trigger","research_id":"R7L75_C25_MEDTECH_EXPORT_DEVICE_ROUTER","round":"R7","loop":75,"large_sector_id":"L7_BIO_HEALTHCARE_MEDICAL","canonical_archetype_id":"C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT","fine_archetype_id":"AESTHETIC_DEVICE_WOUNDCARE_XRAY_EXPORT_REIMBURSEMENT_AND_HIGH_MAE_ROUTER","symbol":"336570","name":"원텍","trigger_type":"Stage2-Actionable-Guarded","trigger_family":"aesthetic_laser_device_export_growth_initial_mfe_later_high_mae","trigger_date":"2024-03-25","entry_date":"2024-03-26","entry_price":9800.0,"entry_price_type":"next_tradable_open_after_aesthetic_device_export_burst","price_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","mfe_30d_pct":22.45,"mae_30d_pct":-5.51,"mfe_90d_pct":22.45,"mae_90d_pct":-25.82,"mfe_180d_pct":22.45,"mae_180d_pct":-43.27,"peak_price_180d":12000.0,"peak_date_180d":"2024-04-22","trough_price_180d":5560.0,"trough_date_180d":"2024-08-26","calibration_usable":true,"case_polarity":"counterexample_initial_mfe_later_high_mae","evidence_url_pending":true,"source_proxy_only":true,"non_price_evidence_strength":"medium_low_pending_url_repair","price_only_blowoff":false,"expected_stage_current_profile":"Stage2-Guarded_or_local_4B_high_MAE_watch_until_export_reorder_margin_bridge_repaired","residual_error_type":"aesthetic_device_export_label_had_first_window_mfe_but_later_mae_blocks_yellow_green_without_customer_reorder_margin_bridge"}
{"row_type":"trigger","research_id":"R7L75_C25_MEDTECH_EXPORT_DEVICE_ROUTER","round":"R7","loop":75,"large_sector_id":"L7_BIO_HEALTHCARE_MEDICAL","canonical_archetype_id":"C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT","fine_archetype_id":"AESTHETIC_DEVICE_WOUNDCARE_XRAY_EXPORT_REIMBURSEMENT_AND_HIGH_MAE_ROUTER","symbol":"214680","name":"디알텍","trigger_type":"Stage2-FalsePositive-Candidate","trigger_family":"digital_xray_detector_export_theme_spike_high_mae","trigger_date":"2024-07-15","entry_date":"2024-07-16","entry_price":4290.0,"entry_price_type":"next_tradable_open_after_xray_detector_export_theme_spike","price_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","mfe_30d_pct":6.06,"mae_30d_pct":-33.8,"mfe_90d_pct":6.06,"mae_90d_pct":-38.11,"mfe_180d_pct":6.06,"mae_180d_pct":-53.45,"peak_price_180d":4550.0,"peak_date_180d":"2024-07-19","trough_price_180d":1997.0,"trough_date_180d":"2024-12-09","calibration_usable":true,"case_polarity":"counterexample_weak_mfe_extreme_mae","evidence_url_pending":true,"source_proxy_only":true,"non_price_evidence_strength":"low_pending_url_repair","price_only_blowoff":false,"expected_stage_current_profile":"blocked_Stage2_or_4B_4C_high_MAE_watch","residual_error_type":"xray_detector_export_theme_spike_had_weak_mfe_and_extreme_mae_without_export_order_margin_bridge"}
{"row_type":"trigger","research_id":"R7L75_C25_MEDTECH_EXPORT_DEVICE_ROUTER","round":"R7","loop":75,"large_sector_id":"L7_BIO_HEALTHCARE_MEDICAL","canonical_archetype_id":"C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT","fine_archetype_id":"AESTHETIC_DEVICE_WOUNDCARE_XRAY_EXPORT_REIMBURSEMENT_AND_HIGH_MAE_ROUTER","symbol":"263690","name":"디알젬","trigger_type":"Stage2-FalsePositive-Candidate","trigger_family":"medical_xray_export_reimbursement_label_weak_mfe_slow_fade","trigger_date":"2024-05-09","entry_date":"2024-05-10","entry_price":9710.0,"entry_price_type":"next_tradable_open_after_medical_xray_export_label_spike","price_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","mfe_30d_pct":2.99,"mae_30d_pct":-7.93,"mfe_90d_pct":2.99,"mae_90d_pct":-26.16,"mfe_180d_pct":2.99,"mae_180d_pct":-32.03,"peak_price_180d":10000.0,"peak_date_180d":"2024-05-14","trough_price_180d":6600.0,"trough_date_180d":"2024-11-04","calibration_usable":true,"case_polarity":"counterexample_weak_mfe_slow_fade","evidence_url_pending":true,"source_proxy_only":true,"non_price_evidence_strength":"low_pending_url_repair","price_only_blowoff":false,"expected_stage_current_profile":"blocked_Stage2_or_local_4B_watch_until_xray_export_order_bridge_repaired","residual_error_type":"medical_xray_export_label_had_almost_no_mfe_and_later_mae_without_export_order_reimbursement_margin_bridge"}
```

---

## 8. Score simulation and raw component breakdown

This is shadow-only and does not change production scoring.

| symbol | export/reorder bridge | reimbursement/channel access | customer quality | installed-base / consumable pull-through | market mispricing | margin conversion | information confidence | shadow total | intended route |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| `340570` | 13 | 9 | 11 | 12 | 12 | 11 | 6 | 74 | Stage2/Yellow after export-reorder and margin evidence repair |
| `336570` | 8 | 5 | 6 | 4 | 8 | 4 | 5 | 40 | Stage2-Guarded or local 4B/high-MAE watch |
| `214680` | 4 | 3 | 3 | 2 | 3 | 2 | 4 | 21 | blocked Stage2 / 4B-4C high-MAE watch |
| `263690` | 3 | 3 | 4 | 2 | 2 | 2 | 4 | 20 | blocked Stage2 / weak-MFE local 4B watch |

### Current calibrated profile stress test

The current calibrated profile already blocks pure price-only blowoff.  
The remaining C25 issue is **medical-device/export label without reorder or reimbursement conversion**:

```text
C25 clean consumable export path:
  export/reorder relevance
  + persistent MFE
  + contained MAE
  + URL-repaired distributor/customer/margin bridge
  => Stage2-Actionable / Yellow, possible Green after proof

C25 first-window MFE / later-MAE device path:
  aesthetic device export label exists
  + MFE_30D >= +20%
  + MAE_90D <= -25%
  + no repaired reorder/margin bridge
  => Stage2-Guarded at most, local 4B watch, no Yellow/Green

C25 weak-MFE imaging device path:
  X-ray or imaging device export label exists
  + MFE_30D < +10%
  + MAE_90D <= -25%
  + no export-order/reimbursement bridge
  => block Stage2 or 4B/4C high-MAE watch
```

`340570` prevents overblocking.  
`336570` shows that first-window aesthetic-device MFE can still become a high-MAE trap.  
`214680` and `263690` show why X-ray/export labels require actual export order, reimbursement/channel, and margin evidence.

---

## 9. Aggregate metrics

```json
{
  "row_type": "aggregate",
  "research_id": "R7L75_C25_MEDTECH_EXPORT_DEVICE_ROUTER",
  "round": "R7",
  "loop": 75,
  "large_sector_id": "L7_BIO_HEALTHCARE_MEDICAL",
  "canonical_archetype_id": "C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT",
  "fine_archetype_id": "AESTHETIC_DEVICE_WOUNDCARE_XRAY_EXPORT_REIMBURSEMENT_AND_HIGH_MAE_ROUTER",
  "case_count": 4,
  "calibration_usable_case_count": 4,
  "positive_case_count": 1,
  "counterexample_count": 3,
  "new_symbol_count": 4,
  "source_proxy_only_count": 4,
  "evidence_url_pending_count": 4,
  "avg_mfe_30d_pct": 14.31,
  "avg_mae_30d_pct": -12.13,
  "avg_mfe_90d_pct": 18.32,
  "avg_mae_90d_pct": -22.85,
  "avg_mfe_180d_pct": 21.0,
  "avg_mae_180d_pct": -32.51,
  "max_mfe_180d_pct": 52.48,
  "worst_mae_180d_pct": -53.45
}
```

---

## 10. 4B proximity split

```json
{
  "row_type": "4b_split",
  "research_id": "R7L75_C25_MEDTECH_EXPORT_DEVICE_ROUTER",
  "stage2_positive_or_yellow_candidate": [
    {
      "symbol": "340570",
      "reason": "persistent +52.48% 180D MFE with only -1.29% MAE; requires export reorder / distributor / margin evidence before Green"
    }
  ],
  "stage2_guarded_or_local_4b_watch": [
    {
      "symbol": "336570",
      "reason": "first 30D MFE was +22.45%, but 90D MAE reached -25.82% and 180D MAE reached -43.27%"
    }
  ],
  "blocked_stage2_or_4c_watch": [
    {
      "symbol": "214680",
      "reason": "MFE stayed only +6.06%, while 180D MAE reached -53.45%"
    },
    {
      "symbol": "263690",
      "reason": "MFE stayed only +2.99%, while 90D MAE reached -26.16% and 180D MAE reached -32.03%"
    }
  ],
  "full_4b_or_green_requires_non_price_evidence": [
    "export order and distributor reorder",
    "reimbursement / clinical-channel access",
    "customer quality and installed-base expansion",
    "repeat consumable demand or device utilization",
    "ASP / product mix",
    "gross margin and operating leverage conversion"
  ]
}
```

---

## 11. Shadow rule candidate

```yaml
row_type: canonical_archetype_rule_candidate
canonical_archetype_id: C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT
fine_archetype_id: AESTHETIC_DEVICE_WOUNDCARE_XRAY_EXPORT_REIMBURSEMENT_AND_HIGH_MAE_ROUTER
rule_name: C25_medtech_export_reorder_reimbursement_and_high_mae_router
production_scoring_changed: false
shadow_weight_only: true
```

### Proposed routing logic

```text
For C25 medical-device / consumable export / reimbursement cases:

Tier A: verified export-reorder winner
  Conditions:
    - export order, distributor reorder, reimbursement/channel access, and margin evidence are URL-repaired
    - MFE_90D >= +30%
    - MAE_90D > -10%
    - MFE persists beyond one event candle
  Routing:
    - Stage2-Actionable allowed
    - Stage3-Yellow allowed after evidence repair
    - Green only after export/reorder/reimbursement/margin bridge is verified

Tier B: first-window MFE but later high MAE
  Conditions:
    - MFE_30D >= +20%
    - MAE_90D <= -25% or MAE_180D <= -40%
    - evidence_url_pending or source_proxy_only remains true
  Routing:
    - Stage2-Guarded at most
    - local 4B/high-MAE watch
    - no Yellow/Green

Tier C: weak-MFE imaging-device export label
  Conditions:
    - MFE_30D < +10%
    - MAE_90D <= -25% or MAE_180D <= -30%
    - no export-order or reimbursement bridge
  Routing:
    - block Stage2 or route to 4B/4C watch
    - count as counterexample
```

### Suggested shadow delta

```json
{
  "row_type": "shadow_weight",
  "axis": "c25_medtech_export_reorder_reimbursement_and_high_mae_router",
  "scope": "canonical_archetype_id:C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT",
  "proposal": {
    "source_proxy_only_green_allowed": false,
    "export_reorder_reimbursement_margin_bridge_required_for_green": true,
    "verified_export_winner_mfe90_threshold_pct": 30.0,
    "verified_export_winner_mae90_min_pct": -10.0,
    "first_window_mfe_threshold_30d_pct": 20.0,
    "later_mae_watch_threshold_90d_pct": -25.0,
    "later_hard_mae_threshold_180d_pct": -40.0,
    "weak_mfe_threshold_30d_pct": 10.0,
    "weak_mfe_mae90_threshold_pct": -25.0,
    "weak_mfe_hard_mae180_threshold_pct": -30.0,
    "positive_weight_blocked_until_url_repair": true
  },
  "confidence": "medium_low_until_url_repair",
  "apply_now": false,
  "reason": "One clean medical consumable export winner and three aesthetic/X-ray device high-MAE or weak-MFE cases show that C25 should require URL-repaired export reorder, reimbursement/channel, customer quality, and margin evidence before Yellow/Green."
}
```

---

## 12. Residual contribution summary

```json
{
  "row_type": "residual_contribution",
  "research_id": "R7L75_C25_MEDTECH_EXPORT_DEVICE_ROUTER",
  "large_sector_id": "L7_BIO_HEALTHCARE_MEDICAL",
  "canonical_archetype_id": "C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT",
  "contribution": "Adds four non-top-covered C25 medical-device/consumable export-reimbursement cases and separates a clean low-MAE wound-care consumable export/reorder winner from aesthetic-device and X-ray imaging weak-MFE/high-MAE failures. C25 Yellow/Green should require URL-repaired export order, distributor reorder, reimbursement/channel access, customer quality, installed-base utilization, ASP/product mix, and margin evidence.",
  "positive_case_added": 1,
  "counterexample_case_added": 3,
  "new_symbol_count": 4,
  "new_independent_case_count": 4,
  "reused_case_count": 0,
  "same_archetype_new_symbol_count": 4,
  "same_archetype_new_trigger_family_count": 4,
  "new_trigger_family_count": 4,
  "current_profile_error_count": 3,
  "diversity_score_summary": {
    "new_symbol_bonus": 12,
    "counterexample_gap_bonus": 6,
    "residual_error_bonus": 15,
    "wrong_round_penalty": 0,
    "repeated_same_symbol_penalty": 0,
    "net_interpretive_score": 33
  },
  "loop_contribution_label": "canonical_archetype_rule_candidate",
  "do_not_propose_new_weight_delta": false,
  "data_quality_blocker": "All four non-price medical-device/export triggers require URL-level repair before positive weight promotion.",
  "guardrail_added": "C25 source_proxy_only device cases with first-window MFE but MAE_90D <= -25% should cap at Stage2-Guarded; weak-MFE imaging-device cases with MFE_30D < +10% and MAE_90D <= -25% or MAE_180D <= -30% should block Stage2 or route to 4B/4C watch."
}
```

One-line contribution:

```text
This loop adds 4 new independent cases, 3 counterexamples, and 3 residual errors for R7/L7_BIO_HEALTHCARE_MEDICAL/C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT.
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
    340570: false
    336570: false
    214680: false
    263690: false
  evidence_url_pending:
    340570: true
    336570: true
    214680: true
    263690: true
  source_proxy_only:
    340570: true
    336570: true
    214680: true
    263690: true
```

Limitations:

```text
- Price path is validated against Stock-Web tradable OHLC rows.
- Non-price evidence is not URL-repaired in this run.
- Therefore this artifact is useful for C25 medical-device/export/reimbursement residual shape and high-MAE guardrail design, but should not promote positive weights until filings, IR, export data, distributor/channel data, reimbursement documents, or reports verify export orders, reorder, reimbursement/channel access, customer quality, installed-base utilization, ASP/product mix, and margin conversion.
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
2. Preserve R7 / loop 75 metadata.
3. Add the cases to C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT only if parser validation passes.
4. Treat all four non-price triggers as evidence_url_pending=true and source_proxy_only=true until URL-level evidence is repaired.
5. Do not use these rows for positive weight promotion until filings/IR/export-data/distributor-channel/reimbursement/report data verifies export orders, reorder, reimbursement/channel access, customer quality, installed-base utilization, ASP/product mix, and margin conversion.
6. Add a shadow-only rule candidate named C25_medtech_export_reorder_reimbursement_and_high_mae_router.
7. Do not loosen Stage3-Green.
8. Add C25-specific guards:
   - source_proxy_only -> no Green
   - Green requires repaired export/reorder/reimbursement/margin bridge
   - MFE_90D >= +30% and MAE_90D > -10% may remain Stage2-Actionable / Yellow watch after evidence repair
   - MFE_30D >= +20% but MAE_90D <= -25% or MAE_180D <= -40% -> Stage2-Guarded at most / local 4B watch
   - MFE_30D < +10% and MAE_90D <= -25% or MAE_180D <= -30% -> block Stage2 or 4B/4C watch
9. Keep production scoring unchanged unless later batch promotion logic independently marks this axis safe.
```

---

## 15. Next round state

```text
completed_round = R7
completed_loop = 75
next_round = R8
next_loop = 75
next_large_sector_hint = L8_PLATFORM_CONTENT_SW_SECURITY
round_schedule_status = valid
round_sector_consistency = pass
```
