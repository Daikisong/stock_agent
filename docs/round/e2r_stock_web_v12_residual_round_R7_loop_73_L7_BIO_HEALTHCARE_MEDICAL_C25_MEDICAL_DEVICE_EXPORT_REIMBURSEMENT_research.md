# E2R Stock-Web v12 Residual Research — R7 Loop 73

```yaml
research_session: post_calibrated_sector_archetype_residual_research
mode: historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12
completed_round: R7
completed_loop: 73
next_round: R8
next_loop: 73
large_sector_id: L7_BIO_HEALTHCARE_MEDICAL
canonical_archetype_id: C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT
fine_archetype_id: AESTHETIC_MEDICAL_DEVICE_EXPORT_COMMERCIALIZATION_AND_HIGH_MAE_ROUTER
output_file: e2r_stock_web_v12_residual_round_R7_loop_73_L7_BIO_HEALTHCARE_MEDICAL_C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT_research.md
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
completed_loop  = 73
large_sector_id = L6_FINANCIAL_CAPITAL_RETURN_DIGITAL
canonical_archetype_id = C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN
```

Therefore:

```text
scheduled_round = R7
scheduled_loop  = 73
```

R7 maps to:

```text
large_sector_id = L7_BIO_HEALTHCARE_MEDICAL
```

This run selects:

```text
canonical_archetype_id = C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT
fine_archetype_id = AESTHETIC_MEDICAL_DEVICE_EXPORT_COMMERCIALIZATION_AND_HIGH_MAE_ROUTER
```

This is a valid R7/L7 pairing.

---

## 1. Why this R7/C25 run

The no-repeat ledger shows C25 is covered but still has room outside the dominant medical-device / AI-diagnostic / dental names:

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

This file deliberately avoids the highest-covered symbols and adds:

```text
340570 티앤엘
336570 원텍
149980 하이로닉
```

Research question:

```text
Can C25 separate an actual export/commercialization medical-device rerating path from aesthetic-device relief spikes where the first MFE appears before repeat order, overseas distribution, utilization, reimbursement, or margin conversion is verified?
```

C25 is not simply “medical device stock went up.”  
A medical-device move is durable only when the device turns into a repeatable commercial engine: regulatory clearance, distributor channel, hospital/clinic adoption, reimbursement or procedure volume, repeat consumable demand, and margin conversion. If that engine is not visible, the first candle can be a flash from a surgical lamp rather than a real operating result.

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
| `340570` | 티앤엘 | active_like / KOSDAQ | no 2024 overlap; old 2021 candidates only | true |
| `336570` | 원텍 | active_like / KOSDAQ | no 2024 overlap; 2022 SPAC/name-transition candidate outside tested window | true |
| `149980` | 하이로닉 | active_like / KOSDAQ | no 2024 overlap; old 2014/2015 candidates only | true |

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
The Stock-Web price path is fully validated, but company-level export shipment, FDA/CE/KFDA approval, distributor channel, reimbursement, clinic utilization, consumable repeat demand, and margin bridge evidence still require later URL repair through filings, IR decks, regulatory databases, export data, or sell-side reports before production weight promotion.
```

C25 interpretation used here:

```text
C25 asks whether a medical-device thesis has a commercial bridge:
- regulatory clearance or reimbursement path,
- export channel / distributor visibility,
- repeat procedures or consumable demand,
- customer adoption,
- gross margin / operating leverage conversion,
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
149980 + C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT -> no direct match found
```

Novelty accounting:

```json
{
  "new_symbol_count": 3,
  "minimum_new_symbol_count": 2,
  "positive_case_count": 1,
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
| `R7L73_C25_340570_20240319` | `340570` 티앤엘 | wound-care / medical consumable export-commercialization rerating | positive anchor / low-MAE commercial bridge candidate |
| `R7L73_C25_336570_20240325` | `336570` 원텍 | aesthetic-device export/commercialization rerating with later high MAE | high-MFE/high-MAE counterexample |
| `R7L73_C25_149980_20240627` | `149980` 하이로닉 | aesthetic-device theme spike with weak follow-through | low-MFE/high-MAE counterexample |

The intended residual:

```text
C25 should separate:
1. medical-device / consumable export paths where MFE persists and MAE stays contained;
2. aesthetic-device rerating paths where early MFE is real but later drawdown shows the commercial bridge is not yet durable;
3. post-spike relief entries where the trigger has almost no remaining MFE and quickly becomes 4B/high-MAE.
```

---

## 6. Stock-Web OHLC and backtest

### 6.1 `340570` 티앤엘 — medical consumable export-commercialization positive anchor

Trigger:

```text
trigger_date = 2024-03-18
trigger_type = Stage2-Actionable
trigger_family = woundcare_medical_consumable_export_commercialization
entry_date = 2024-03-19
entry_price = 50500.0
entry_price_type = next_tradable_open
```

Relevant Stock-Web rows:

```csv
d,o,h,l,c,v,a,mc,s,m
2024-03-18,47600.0,48200.0,46600.0,47350.0,61407.0,2920744300.0,384860800000.0,8128000,KOSDAQ
2024-03-19,50500.0,52700.0,49850.0,51300.0,450689.0,23133609850.0,416966400000.0,8128000,KOSDAQ
2024-04-11,61000.0,63500.0,58000.0,59900.0,346955.0,21133689100.0,486867200000.0,8128000,KOSDAQ
2024-05-16,65300.0,71600.0,64100.0,70800.0,658584.0,45076416300.0,575462400000.0,8128000,KOSDAQ
2024-06-24,70000.0,74100.0,69500.0,71600.0,236914.0,17075471300.0,581964800000.0,8128000,KOSDAQ
2024-08-20,74000.0,76500.0,72100.0,75600.0,285883.0,21380733700.0,614476800000.0,8128000,KOSDAQ
2024-09-04,66500.0,68600.0,65500.0,67200.0,70468.0,4744636500.0,546201600000.0,8128000,KOSDAQ
2024-09-23,73000.0,75800.0,72700.0,74000.0,237492.0,17549749500.0,601472000000.0,8128000,KOSDAQ
```

Backtest:

| window | peak/high | peak date | trough/low | trough date | MFE | MAE |
|---|---:|---|---:|---|---:|---:|
| 30 calendar days | 63500 | 2024-04-11 | 49850 | 2024-03-19 | +25.74% | -1.29% |
| 90 calendar days | 71600 | 2024-05-16 | 49850 | 2024-03-19 | +41.78% | -1.29% |
| 180 calendar days | 77000 | 2024-08-21 | 49850 | 2024-03-19 | +52.48% | -1.29% |

Interpretation:

```text
340570 is the positive anchor.
The path produced persistent MFE while keeping MAE close to zero.
This is the C25 pattern that can remain Stage2-Actionable / Stage3-Yellow after evidence repair.
Green still requires URL-repaired export channel, repeat demand, regulatory/reimbursement, and margin conversion evidence.
```

### 6.2 `336570` 원텍 — aesthetic-device rerating with later high MAE

Trigger:

```text
trigger_date = 2024-03-22
trigger_type = Stage2-Actionable-Guarded
trigger_family = aesthetic_device_export_commercialization_rerating_high_mae
entry_date = 2024-03-25
entry_price = 8400.0
entry_price_type = next_tradable_open_after_device_theme_burst
```

Relevant Stock-Web rows:

```csv
d,o,h,l,c,v,a,mc,s,m
2024-03-22,8330.0,8410.0,8180.0,8340.0,562327.0,4660024140.0,735370451100.0,88173915,KOSDAQ
2024-03-25,8400.0,9990.0,8360.0,9890.0,15405837.0,148066600290.0,872040019350.0,88173915,KOSDAQ
2024-04-03,9940.0,11200.0,9890.0,10850.0,8944330.0,96283291650.0,956686977750.0,88173915,KOSDAQ
2024-04-19,11160.0,11850.0,11000.0,11570.0,4459962.0,51094829020.0,1020172196550.0,88173915,KOSDAQ
2024-04-22,11580.0,12000.0,10690.0,10860.0,4213557.0,48057138740.0,957568716900.0,88173915,KOSDAQ
2024-06-05,7500.0,7500.0,7270.0,7350.0,749995.0,5517804640.0,656653549650.0,89340619,KOSDAQ
2024-08-26,5670.0,5730.0,5560.0,5650.0,402990.0,2269781090.0,504774497350.0,89340619,KOSDAQ
2024-09-19,6880.0,7250.0,6730.0,7200.0,1943699.0,13694649400.0,643252456800.0,89340619,KOSDAQ
```

Backtest:

| window | peak/high | peak date | trough/low | trough date | MFE | MAE |
|---|---:|---|---:|---|---:|---:|
| 30 calendar days | 12000 | 2024-04-22 | 8360 | 2024-03-25 | +42.86% | -0.48% |
| 90 calendar days | 12000 | 2024-04-22 | 7270 | 2024-06-05 | +42.86% | -13.45% |
| 180 calendar days | 12000 | 2024-04-22 | 5560 | 2024-08-26 | +42.86% | -33.81% |

Interpretation:

```text
336570 is the high-MFE/high-MAE counterexample.
The first-month price path looked excellent, but the 180D drawdown later crossed -30%.
The lesson is not to block all aesthetic-device names. The lesson is to require export/distributor utilization and margin conversion proof before Green.
```

### 6.3 `149980` 하이로닉 — aesthetic-device spike with weak follow-through

Trigger:

```text
trigger_date = 2024-06-26
trigger_type = Stage2-FalsePositive-Candidate
trigger_family = aesthetic_device_theme_spike_weak_followthrough
entry_date = 2024-06-27
entry_price = 10810.0
entry_price_type = next_tradable_open_after_theme_spike
```

Relevant Stock-Web rows:

```csv
d,o,h,l,c,v,a,mc,s,m
2024-06-26,9190.0,11250.0,9170.0,10510.0,13305769.0,141345208930.0,195395225130.0,18591363,KOSDAQ
2024-06-27,10810.0,10950.0,10010.0,10230.0,3297875.0,34411113750.0,190189643490.0,18591363,KOSDAQ
2024-07-26,9060.0,9350.0,8410.0,8610.0,486263.0,4217401920.0,160071635430.0,18591363,KOSDAQ
2024-08-05,7460.0,7520.0,6450.0,6770.0,680779.0,4822642880.0,125863527510.0,18591363,KOSDAQ
2024-09-09,10050.0,10640.0,8280.0,8280.0,7028504.0,66456185330.0,153936485640.0,18591363,KOSDAQ
2024-10-16,6700.0,8710.0,6600.0,7400.0,9022074.0,70914685460.0,137576086200.0,18591363,KOSDAQ
2024-11-13,6060.0,6210.0,5920.0,5920.0,123620.0,746915490.0,110078628960.0,18594363,KOSDAQ
2024-12-09,5780.0,6020.0,5300.0,5310.0,222108.0,1217213060.0,98736067530.0,18594363,KOSDAQ
```

Backtest:

| window | peak/high | peak date | trough/low | trough date | MFE | MAE |
|---|---:|---|---:|---|---:|---:|
| 30 calendar days | 10950 | 2024-06-27 | 8410 | 2024-07-26 | +1.30% | -22.20% |
| 90 calendar days | 10950 | 2024-06-27 | 6450 | 2024-08-05 | +1.30% | -40.33% |
| 180 calendar days | 10950 | 2024-06-27 | 5300 | 2024-12-09 | +1.30% | -50.97% |

Interpretation:

```text
149980 is the clean false-positive branch.
The event candle itself had already spent the upside, and the next windows delivered severe MAE.
This should block Stage2/Green unless fresh regulatory, export, distributor, utilization, or margin evidence appears before entry.
```

---

## 7. Machine-readable trigger JSONL

```jsonl
{"row_type":"trigger","research_id":"R7L73_C25_MEDICAL_DEVICE_EXPORT_ROUTER","round":"R7","loop":73,"large_sector_id":"L7_BIO_HEALTHCARE_MEDICAL","canonical_archetype_id":"C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT","fine_archetype_id":"AESTHETIC_MEDICAL_DEVICE_EXPORT_COMMERCIALIZATION_AND_HIGH_MAE_ROUTER","symbol":"340570","name":"티앤엘","trigger_type":"Stage2-Actionable","trigger_family":"woundcare_medical_consumable_export_commercialization","trigger_date":"2024-03-18","entry_date":"2024-03-19","entry_price":50500.0,"entry_price_type":"next_tradable_open","price_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","mfe_30d_pct":25.74,"mae_30d_pct":-1.29,"mfe_90d_pct":41.78,"mae_90d_pct":-1.29,"mfe_180d_pct":52.48,"mae_180d_pct":-1.29,"peak_price_180d":77000.0,"peak_date_180d":"2024-08-21","trough_price_180d":49850.0,"trough_date_180d":"2024-03-19","calibration_usable":true,"case_polarity":"positive_anchor","evidence_url_pending":true,"source_proxy_only":true,"non_price_evidence_strength":"medium_pending_url_repair","price_only_blowoff":false,"expected_stage_current_profile":"Stage2-Actionable_to_Yellow_after_export_reimbursement_margin_bridge_repaired","residual_error_type":"positive_anchor_requires_url_repaired_export_regulatory_repeat_demand_margin_evidence_before_green"}
{"row_type":"trigger","research_id":"R7L73_C25_MEDICAL_DEVICE_EXPORT_ROUTER","round":"R7","loop":73,"large_sector_id":"L7_BIO_HEALTHCARE_MEDICAL","canonical_archetype_id":"C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT","fine_archetype_id":"AESTHETIC_MEDICAL_DEVICE_EXPORT_COMMERCIALIZATION_AND_HIGH_MAE_ROUTER","symbol":"336570","name":"원텍","trigger_type":"Stage2-Actionable-Guarded","trigger_family":"aesthetic_device_export_commercialization_rerating_high_mae","trigger_date":"2024-03-22","entry_date":"2024-03-25","entry_price":8400.0,"entry_price_type":"next_tradable_open_after_device_theme_burst","price_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","mfe_30d_pct":42.86,"mae_30d_pct":-0.48,"mfe_90d_pct":42.86,"mae_90d_pct":-13.45,"mfe_180d_pct":42.86,"mae_180d_pct":-33.81,"peak_price_180d":12000.0,"peak_date_180d":"2024-04-22","trough_price_180d":5560.0,"trough_date_180d":"2024-08-26","calibration_usable":true,"case_polarity":"counterexample_high_mfe_high_mae","evidence_url_pending":true,"source_proxy_only":true,"non_price_evidence_strength":"medium_low_pending_url_repair","price_only_blowoff":false,"expected_stage_current_profile":"Stage2-Guarded_or_4B_high_MAE_watch_until_export_utilization_margin_bridge_repaired","residual_error_type":"first_month_mfe_overwhelmed_by_180d_high_mae_without_durable_commercial_bridge"}
{"row_type":"trigger","research_id":"R7L73_C25_MEDICAL_DEVICE_EXPORT_ROUTER","round":"R7","loop":73,"large_sector_id":"L7_BIO_HEALTHCARE_MEDICAL","canonical_archetype_id":"C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT","fine_archetype_id":"AESTHETIC_MEDICAL_DEVICE_EXPORT_COMMERCIALIZATION_AND_HIGH_MAE_ROUTER","symbol":"149980","name":"하이로닉","trigger_type":"Stage2-FalsePositive-Candidate","trigger_family":"aesthetic_device_theme_spike_weak_followthrough","trigger_date":"2024-06-26","entry_date":"2024-06-27","entry_price":10810.0,"entry_price_type":"next_tradable_open_after_theme_spike","price_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","mfe_30d_pct":1.30,"mae_30d_pct":-22.20,"mfe_90d_pct":1.30,"mae_90d_pct":-40.33,"mfe_180d_pct":1.30,"mae_180d_pct":-50.97,"peak_price_180d":10950.0,"peak_date_180d":"2024-06-27","trough_price_180d":5300.0,"trough_date_180d":"2024-12-09","calibration_usable":true,"case_polarity":"counterexample_low_mfe_high_mae","evidence_url_pending":true,"source_proxy_only":true,"non_price_evidence_strength":"low_pending_url_repair","price_only_blowoff":false,"expected_stage_current_profile":"blocked_Stage2_or_4B_4C_high_MAE_watch","residual_error_type":"post_spike_medical_device_entry_low_mfe_extreme_mae_without_fresh_commercial_bridge"}
```

---

## 8. Score simulation and raw component breakdown

This is shadow-only and does not change production scoring.

| symbol | regulatory/reimbursement bridge | export/distribution visibility | repeat demand/utilization | market mispricing | valuation rerating | margin conversion | information confidence | shadow total | intended route |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| `340570` | 10 | 13 | 14 | 12 | 12 | 13 | 7 | 81 | Stage2/Yellow after export-commercialization evidence repair |
| `336570` | 8 | 10 | 7 | 14 | 13 | 6 | 6 | 64 | Stage2-Guarded or 4B/high-MAE watch |
| `149980` | 4 | 5 | 3 | 4 | 4 | 3 | 4 | 27 | blocked Stage2 / 4B-to-4C high-MAE watch |

### Current calibrated profile stress test

The current calibrated profile already blocks pure price-only blowoff.  
The remaining C25 risk is **commercial bridge durability**:

```text
C25 clean path:
  medical device / consumable has export or reimbursement relevance
  + MFE is persistent
  + MAE remains contained
  + regulatory, distributor, repeat-demand, and margin evidence is URL-repaired
  => Stage2-Actionable / Yellow, possible Green after proof

C25 aesthetic-device high-MFE trap:
  device theme has strong first-month MFE
  + evidence remains source_proxy_only
  + 180D MAE <= -30%
  => Stage2-Guarded or 4B/high-MAE watch, no Green

C25 post-spike false-positive:
  entry follows theme spike
  + MFE_30D < +5%
  + MAE_30D <= -20%
  + no fresh commercial bridge
  => block Stage2 and route to 4B/4C watch
```

`340570` prevents overblocking.  
`336570` shows why excellent first-month MFE is not enough.  
`149980` is the hard false-positive: the event candle became the ceiling, not the start of a commercial rerating.

---

## 9. Aggregate metrics

```json
{
  "row_type": "aggregate",
  "research_id": "R7L73_C25_MEDICAL_DEVICE_EXPORT_ROUTER",
  "round": "R7",
  "loop": 73,
  "large_sector_id": "L7_BIO_HEALTHCARE_MEDICAL",
  "canonical_archetype_id": "C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT",
  "fine_archetype_id": "AESTHETIC_MEDICAL_DEVICE_EXPORT_COMMERCIALIZATION_AND_HIGH_MAE_ROUTER",
  "case_count": 3,
  "calibration_usable_case_count": 3,
  "positive_case_count": 1,
  "counterexample_count": 2,
  "new_symbol_count": 3,
  "source_proxy_only_count": 3,
  "evidence_url_pending_count": 3,
  "avg_mfe_30d_pct": 23.30,
  "avg_mae_30d_pct": -7.99,
  "avg_mfe_90d_pct": 28.65,
  "avg_mae_90d_pct": -18.36,
  "avg_mfe_180d_pct": 32.21,
  "avg_mae_180d_pct": -28.69,
  "max_mfe_180d_pct": 52.48,
  "worst_mae_180d_pct": -50.97
}
```

---

## 10. 4B proximity split

```json
{
  "row_type": "4b_split",
  "research_id": "R7L73_C25_MEDICAL_DEVICE_EXPORT_ROUTER",
  "stage2_positive_or_yellow_candidate": [
    {
      "symbol": "340570",
      "reason": "persistent 180D MFE of +52.48% with only -1.29% MAE; still requires URL-repaired export/repeat-demand/margin evidence before Green"
    }
  ],
  "local_4b_watch": [
    {
      "symbol": "336570",
      "reason": "first-month MFE was strong, but 180D MAE reached -33.81%; requires commercial bridge repair before promotion"
    }
  ],
  "blocked_stage2_or_4c_watch": [
    {
      "symbol": "149980",
      "reason": "entry-day MFE was only +1.30% and 180D MAE reached -50.97%; post-spike false-positive"
    }
  ],
  "full_4b_or_green_requires_non_price_evidence": [
    "regulatory clearance / reimbursement path",
    "export distributor or named customer channel",
    "repeat consumable or procedure-volume demand",
    "clinic/hospital utilization evidence",
    "gross margin / operating leverage conversion"
  ]
}
```

---

## 11. Shadow rule candidate

```yaml
row_type: canonical_archetype_rule_candidate
canonical_archetype_id: C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT
fine_archetype_id: AESTHETIC_MEDICAL_DEVICE_EXPORT_COMMERCIALIZATION_AND_HIGH_MAE_ROUTER
rule_name: C25_medical_device_commercial_bridge_and_high_mae_router
production_scoring_changed: false
shadow_weight_only: true
```

### Proposed routing logic

```text
For C25 medical-device export / reimbursement / commercialization cases:

Tier A: verified medical-device commercial bridge
  Conditions:
    - regulatory/reimbursement/export/distributor evidence is URL-repaired
    - repeat demand, utilization, or consumable attach-rate is visible
    - 30D/90D MAE is contained
    - MFE persists beyond the first event candle
  Routing:
    - Stage2-Actionable allowed
    - Stage3-Yellow allowed after evidence repair
    - Green only after commercial bridge and margin conversion are verified

Tier B: aesthetic-device high-MFE but source-proxy bridge
  Conditions:
    - first-month MFE is strong
    - source_proxy_only or evidence_url_pending remains true
    - 180D MAE <= -30%
  Routing:
    - Stage2-Actionable-Guarded at most
    - local 4B/high-MAE watch
    - no Green

Tier C: post-spike weak follow-through
  Conditions:
    - MFE_30D < +5%
    - MAE_30D <= -20%
    - no fresh regulatory/export/utilization/margin evidence
  Routing:
    - block Stage2
    - route to 4B/4C high-MAE watch
    - count as false-positive counterexample
```

### Suggested shadow delta

```json
{
  "row_type": "shadow_weight",
  "axis": "c25_medical_device_commercial_bridge_and_high_mae_router",
  "scope": "canonical_archetype_id:C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT",
  "proposal": {
    "source_proxy_only_green_allowed": false,
    "commercial_bridge_required_for_green": true,
    "regulatory_export_reimbursement_bridge_required": true,
    "aesthetic_device_high_mfe_stage2_cap": "guarded_only_until_url_repair",
    "high_mae_watch_threshold_180d_pct": -30.0,
    "post_spike_weak_mfe_threshold_30d_pct": 5.0,
    "post_spike_high_mae_threshold_30d_pct": -20.0,
    "positive_weight_blocked_until_url_repair": true
  },
  "confidence": "medium_low_until_url_repair",
  "apply_now": false,
  "reason": "One clean medical consumable export-commercialization positive and two aesthetic-device high-MAE counterexamples show that C25 should require regulatory/export/repeat-demand/margin evidence before Green, especially after first-candle device-theme spikes."
}
```

---

## 12. Residual contribution summary

```json
{
  "row_type": "residual_contribution",
  "research_id": "R7L73_C25_MEDICAL_DEVICE_EXPORT_ROUTER",
  "large_sector_id": "L7_BIO_HEALTHCARE_MEDICAL",
  "canonical_archetype_id": "C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT",
  "contribution": "Adds three non-top-covered C25 medical-device / aesthetic-device cases and separates a clean low-MAE medical consumable export-commercialization path from high-MFE/high-MAE and low-MFE/high-MAE aesthetic-device false positives. C25 Green should require URL-repaired regulatory, export, distributor, repeat-demand, utilization, and margin evidence.",
  "positive_case_added": 1,
  "counterexample_case_added": 2,
  "new_symbol_count": 3,
  "data_quality_blocker": "All three non-price medical-device commercialization triggers require URL-level repair before positive weight promotion.",
  "guardrail_added": "C25 source_proxy_only aesthetic-device cases with 180D MAE <= -30% should route to Stage2-Guarded or 4B/high-MAE watch; post-spike entries with MFE_30D < +5% and MAE_30D <= -20% should block Stage2."
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
    340570: false
    336570: false
    149980: false
  evidence_url_pending:
    340570: true
    336570: true
    149980: true
  source_proxy_only:
    340570: true
    336570: true
    149980: true
```

Limitations:

```text
- Price path is validated against Stock-Web tradable OHLC rows.
- Non-price evidence is not URL-repaired in this run.
- Therefore this artifact is useful for C25 medical-device residual shape and high-MAE guardrail design, but should not promote positive weights until filings/IR/regulatory/export/report data verifies regulatory clearance, reimbursement, distributor channel, repeat demand, procedure utilization, and margin conversion.
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
2. Preserve R7 / loop 73 metadata.
3. Add the cases to C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT only if parser validation passes.
4. Treat all three non-price triggers as evidence_url_pending=true and source_proxy_only=true until URL-level evidence is repaired.
5. Do not use these rows for positive weight promotion until filings/IR/regulatory/export/report data verifies regulatory clearance, reimbursement, distributor channel, repeat demand, procedure utilization, and margin conversion.
6. Add a shadow-only rule candidate named C25_medical_device_commercial_bridge_and_high_mae_router.
7. Do not loosen Stage3-Green.
8. Add C25-specific guards:
   - source_proxy_only -> no Green
   - aesthetic-device high-MFE case with 180D MAE <= -30% -> Stage2-Guarded or local 4B/high-MAE watch
   - post-spike entry with MFE_30D < +5% and MAE_30D <= -20% -> block Stage2
   - Green requires repaired regulatory/export/reimbursement/repeat-demand/margin bridge
9. Keep production scoring unchanged unless later batch promotion logic independently marks this axis safe.
```

---

## 15. Next round state

```text
completed_round = R7
completed_loop = 73
next_round = R8
next_loop = 73
next_large_sector_hint = L8_PLATFORM_CONTENT_SW_SECURITY
```
