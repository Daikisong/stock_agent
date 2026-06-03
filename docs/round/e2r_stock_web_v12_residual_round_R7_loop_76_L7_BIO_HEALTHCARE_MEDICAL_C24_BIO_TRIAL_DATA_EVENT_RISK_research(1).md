# E2R Stock-Web v12 Residual Research — R7 Loop 76

```yaml
research_session: post_calibrated_sector_archetype_residual_research
mode: historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12
completed_round: R7
completed_loop: 76
next_round: R8
next_loop: 76
large_sector_id: L7_BIO_HEALTHCARE_MEDICAL
canonical_archetype_id: C24_BIO_TRIAL_DATA_EVENT_RISK
fine_archetype_id: ADC_RNA_VACCINE_TRIAL_PLATFORM_EVENT_MFE_AND_HIGH_MAE_ROUTER
output_file: e2r_stock_web_v12_residual_round_R7_loop_76_L7_BIO_HEALTHCARE_MEDICAL_C24_BIO_TRIAL_DATA_EVENT_RISK_research.md
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
completed_loop  = 76
large_sector_id = L6_FINANCIAL_CAPITAL_RETURN_DIGITAL
canonical_archetype_id = C22_INSURANCE_RATE_CYCLE_RESERVE
```

Therefore:

```text
scheduled_round = R7
scheduled_loop  = 76
```

R7 maps to:

```text
large_sector_id = L7_BIO_HEALTHCARE_MEDICAL
```

This run selects:

```text
canonical_archetype_id = C24_BIO_TRIAL_DATA_EVENT_RISK
fine_archetype_id = ADC_RNA_VACCINE_TRIAL_PLATFORM_EVENT_MFE_AND_HIGH_MAE_ROUTER
```

This is a valid R7/L7 pairing.

---

## 1. Why this R7/C24 run

The no-repeat ledger shows C24 is meaningfully covered but still not as dense as C23, and top coverage is concentrated in a handful of prior drug-trial names:

```text
C24_BIO_TRIAL_DATA_EVENT_RISK:
  rows: 62
  symbols: 17
  date_range: 2019-08-01~2024-11-20
  good/bad S2: 22/3
  4B/4C: 6/18
  URL/proxy: 0/7
  top covered symbols: 000100(8), 009420(8), 215600(8), 028300(7), 039200(7), 019170(4)
```

This file avoids those top-covered symbols and adds four platform / RNA / vaccine / clinical-event cases:

```text
226950 올릭스
298380 에이비엘바이오
206650 유바이오로직스
293780 압타바이오
```

Research question:

```text
Can C24 separate real bio platform / trial-event rerating from clinical-event cases where first-window MFE is not enough, because the entry must first absorb high MAE or later drawdown before trial data, partnering, cash runway, and commercialization bridges are repaired?
```

C24 is a trial-event risk archetype. A clinical event is not a factory order; it is a probability gate. The stock can run when the gate opens, but Stage2 should ask whether the bridge behind that gate exists: data quality, endpoint credibility, partner economics, next readout timing, regulatory path, and cash runway. Without the bridge, the event candle is a door with no floor behind it.

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
| `226950` | 올릭스 | active_like / KOSDAQ | no 2024 overlap; latest listed candidates 2020 only | true |
| `298380` | 에이비엘바이오 | active_like / KOSDAQ | none listed | true |
| `206650` | 유바이오로직스 | active_like / KOSDAQ | none listed | true |
| `293780` | 압타바이오 | active_like / KOSDAQ | no 2024 overlap; latest listed candidates 2021 only | true |

Profile caveat:

```text
Stock-Web OHLC is raw/unadjusted marcap data.
These cases are calibration-safe for the selected 2024 30D/90D/180D windows because no listed corporate-action candidate overlaps each entry~D+180 test window.
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
The Stock-Web price path is fully validated, but company-level trial data quality, endpoint credibility, partner economics, licensing economics, next-readout timing, regulatory path, cash runway, dilution risk, and commercialization bridge evidence still require later URL repair through filings, IR decks, clinical registry data, conference abstracts, license disclosures, or sell-side reports before production weight promotion.
```

C24 interpretation used here:

```text
C24 is not simply “bio stock rose.”
It asks whether a trial/platform event is probability-convertible:
- data quality and endpoint credibility,
- regulatory and next-readout path,
- partner/license economics,
- cash runway and dilution risk,
- commercialization or reimbursement bridge where relevant,
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
298380 + C24_BIO_TRIAL_DATA_EVENT_RISK -> no direct match found
226950 + C24_BIO_TRIAL_DATA_EVENT_RISK -> no direct match found
206650 + C24_BIO_TRIAL_DATA_EVENT_RISK -> no direct match found
293780 + C24_BIO_TRIAL_DATA_EVENT_RISK -> no direct match found
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
| `R7L76_C24_226950_20240711` | `226950` 올릭스 | RNA therapeutics platform / trial-event low-MAE persistent-MFE path | positive-guarded anchor |
| `R7L76_C24_298380_20240306` | `298380` 에이비엘바이오 | bispecific/ADC platform event with high MFE and later drawdown | positive-guarded |
| `R7L76_C24_206650_20240216` | `206650` 유바이오로직스 | vaccine pipeline / approval label with modest MFE and later MAE | counterexample |
| `R7L76_C24_293780_20240229` | `293780` 압타바이오 | clinical-event failure gapdown / delayed MFE after high MAE | early-high-MAE counterexample |

The intended residual:

```text
C24 should separate:
1. platform/trial-event paths where MFE persists and MAE remains controlled;
2. bio platform paths where MFE is large but Green still needs partner/data/cash evidence;
3. vaccine/approval labels where MFE is modest and later drawdown blocks Yellow/Green;
4. clinical-event cases where later MFE cannot erase the fact that entry first absorbed high MAE.
```

---

## 6. Stock-Web OHLC and backtest

### 6.1 `226950` 올릭스 — RNA therapeutics trial-platform low-MAE persistent-MFE path

Trigger:

```text
trigger_date = 2024-07-10
trigger_type = Stage2-Actionable-Guarded
trigger_family = rna_therapeutics_trial_platform_event_low_mae_persistent_mfe
entry_date = 2024-07-11
entry_price = 9300.0
entry_price_type = next_tradable_open_after_rna_therapeutics_trial_platform_event_burst
```

Relevant Stock-Web rows:

```csv
d,o,h,l,c,v,a,mc,s,m
2024-07-10,9370.0,9600.0,9150.0,9280.0,46951.0,435963080.0,154384474240.0,16636258,KOSDAQ
2024-07-11,9300.0,10760.0,9250.0,10410.0,236563.0,2413168640.0,173183445780.0,16636258,KOSDAQ
2024-07-22,13860.0,17300.0,13700.0,16070.0,3376252.0,53188049670.0,267344666060.0,16636258,KOSDAQ
2024-08-05,14510.0,15460.0,13060.0,13980.0,332037.0,4800417480.0,232677094620.0,16643569,KOSDAQ
2024-09-13,18100.0,19130.0,16720.0,18890.0,615363.0,11235310970.0,320635025330.0,16973797,KOSDAQ
2024-10-08,18300.0,21950.0,18300.0,21600.0,1733336.0,35854806320.0,366634015200.0,16973797,KOSDAQ
2024-10-24,30300.0,32750.0,28950.0,30100.0,843190.0,25943220450.0,518870512300.0,17238223,KOSDAQ
2025-01-07,19130.0,19130.0,17300.0,17410.0,575914.0,10258916450.0,321381165930.0,18459573,KOSDAQ
```

Backtest:

| window | peak/high | peak date | trough/low | trough date | MFE | MAE |
|---|---:|---|---:|---|---:|---:|
| 30 calendar days | 17300 | 2024-07-22 | 9250 | 2024-07-11 | +86.02% | -0.54% |
| 90 calendar days | 21950 | 2024-10-08 | 9250 | 2024-07-11 | +136.02% | -0.54% |
| 180 calendar days | 32750 | 2024-10-24 | 9250 | 2024-07-11 | +252.15% | -0.54% |

Interpretation:

```text
226950 is the C24 positive holdout.
The RNA/platform event path showed persistent MFE with almost no MAE.
This prevents C24 from becoming a blanket anti-bio filter. It can support Stage2-Guarded / Yellow-after-repair, but Green still requires URL-repaired trial data, partner economics, next-readout, regulatory, and cash-runway evidence.
```

### 6.2 `298380` 에이비엘바이오 — bispecific/ADC platform event high-MFE later-drawdown path

Trigger:

```text
trigger_date = 2024-03-05
trigger_type = Stage2-Actionable-Guarded
trigger_family = bispecific_adc_platform_trial_partnering_high_mfe_later_drawdown
entry_date = 2024-03-06
entry_price = 24550.0
entry_price_type = next_tradable_open_after_bispecific_adc_platform_event_burst
```

Relevant Stock-Web rows:

```csv
d,o,h,l,c,v,a,mc,s,m
2024-03-05,23050.0,24200.0,22900.0,23950.0,972516.0,23182901150.0,1147026309050.0,47892539,KOSDAQ
2024-03-06,24550.0,28400.0,24350.0,27300.0,8136384.0,218893876800.0,1307466314700.0,47892539,KOSDAQ
2024-03-13,29800.0,30500.0,26300.0,27900.0,4377989.0,125411174800.0,1336201838100.0,47892539,KOSDAQ
2024-04-17,22100.0,22400.0,21500.0,21500.0,401888.0,8760825550.0,1029689588500.0,47892539,KOSDAQ
2024-06-17,21950.0,22100.0,21200.0,21500.0,461110.0,9907717300.0,1033027463500.0,48047789,KOSDAQ
2024-07-04,27200.0,29750.0,27000.0,29700.0,8698482.0,251226019300.0,1427019333300.0,48047789,KOSDAQ
2024-08-29,34500.0,38500.0,32800.0,33950.0,15995123.0,569637037750.0,1631222436550.0,48047789,KOSDAQ
2024-09-06,27050.0,29600.0,26300.0,28900.0,2775895.0,78095203250.0,1388581102100.0,48047789,KOSDAQ
```

Backtest:

| window | peak/high | peak date | trough/low | trough date | MFE | MAE |
|---|---:|---|---:|---|---:|---:|
| 30 calendar days | 30500 | 2024-03-13 | 23200 | 2024-04-05 | +24.24% | -5.50% |
| 90 calendar days | 30500 | 2024-03-13 | 21500 | 2024-04-17 | +24.24% | -12.42% |
| 180 calendar days | 38500 | 2024-08-29 | 21200 | 2024-06-17 | +56.82% | -13.65% |

Interpretation:

```text
298380 is a positive-guarded C24 platform path.
The MFE became meaningful, but 90D/180D drawdown was not trivial.
This should remain Stage2-Guarded or Yellow-watch only after data quality, partnering, next-readout, and cash-runway evidence is URL-repaired.
```

### 6.3 `206650` 유바이오로직스 — vaccine pipeline / approval label with later MAE

Trigger:

```text
trigger_date = 2024-02-15
trigger_type = Stage2-FalsePositive-Candidate
trigger_family = vaccine_pipeline_trial_approval_label_initial_mfe_later_mae
entry_date = 2024-02-16
entry_price = 12230.0
entry_price_type = next_tradable_open_after_vaccine_pipeline_trial_approval_spike
```

Relevant Stock-Web rows:

```csv
d,o,h,l,c,v,a,mc,s,m
2024-02-15,11360.0,12440.0,11200.0,12350.0,1455541.0,17512770300.0,450216866450.0,36454807,KOSDAQ
2024-02-16,12230.0,12880.0,11600.0,12350.0,1031585.0,12612841130.0,450216866450.0,36454807,KOSDAQ
2024-03-11,13250.0,13500.0,12740.0,12760.0,414162.0,5396858950.0,465163337320.0,36454807,KOSDAQ
2024-04-08,12120.0,14500.0,11700.0,11980.0,1990423.0,25637192640.0,436728587860.0,36454807,KOSDAQ
2024-06-28,12040.0,12110.0,11760.0,12000.0,328029.0,3920312110.0,437811684000.0,36484307,KOSDAQ
2024-08-05,10950.0,11050.0,9350.0,9890.0,381446.0,3907106790.0,360829796230.0,36484307,KOSDAQ
2024-08-19,11500.0,12640.0,11490.0,12410.0,681801.0,8344223840.0,452770249870.0,36484307,KOSDAQ
```

Backtest:

| window | peak/high | peak date | trough/low | trough date | MFE | MAE |
|---|---:|---|---:|---|---:|---:|
| 30 calendar days | 13500 | 2024-03-11 | 11600 | 2024-02-16 | +10.38% | -5.15% |
| 90 calendar days | 14500 | 2024-04-08 | 11490 | 2024-04-09 | +18.56% | -6.05% |
| 180 calendar days | 14500 | 2024-04-08 | 9350 | 2024-08-05 | +18.56% | -23.55% |

Interpretation:

```text
206650 is the modest-MFE / later-MAE counterexample.
The vaccine pipeline / approval label created some upside, but not enough to justify Yellow/Green once 180D MAE reached -23.55%.
C24 should cap or block this route until approval, revenue, procurement, and cash-runway evidence is repaired.
```

### 6.4 `293780` 압타바이오 — clinical-event gapdown, delayed-MFE after early high MAE

Trigger:

```text
trigger_date = 2024-02-28
trigger_type = Stage2-FalsePositive-Candidate
trigger_family = clinical_event_failure_gapdown_then_delayed_mfe_high_mae
entry_date = 2024-02-29
entry_price = 6810.0
entry_price_type = next_tradable_open_after_clinical_event_risk_gapdown
```

Relevant Stock-Web rows:

```csv
d,o,h,l,c,v,a,mc,s,m
2024-02-28,6810.0,6920.0,6770.0,6890.0,45668.0,311924880.0,153639186740.0,22298866,KOSDAQ
2024-02-29,6810.0,6850.0,4935.0,5290.0,2732136.0,14869059380.0,117961001140.0,22298866,KOSDAQ
2024-03-28,6750.0,7530.0,6730.0,7110.0,470186.0,3397292890.0,158544937260.0,22298866,KOSDAQ
2024-05-27,5300.0,5370.0,4930.0,5220.0,69263.0,358262525.0,116400080520.0,22298866,KOSDAQ
2024-07-11,12150.0,15490.0,11910.0,14600.0,4010937.0,57976859390.0,325563443600.0,22298866,KOSDAQ
2024-08-05,9980.0,9990.0,8500.0,9050.0,751207.0,6993512200.0,201804737300.0,22298866,KOSDAQ
2024-08-19,8850.0,9020.0,7400.0,8360.0,1111681.0,9103598340.0,186418519760.0,22298866,KOSDAQ
2024-08-27,8400.0,8550.0,8150.0,8240.0,111160.0,926826540.0,183742655840.0,22298866,KOSDAQ
```

Backtest:

| window | peak/high | peak date | trough/low | trough date | MFE | MAE |
|---|---:|---|---:|---|---:|---:|
| 30 calendar days | 7530 | 2024-03-28 | 4935 | 2024-02-29 | +10.57% | -27.53% |
| 90 calendar days | 7530 | 2024-03-28 | 4930 | 2024-05-27 | +10.57% | -27.61% |
| 180 calendar days | 15490 | 2024-07-11 | 4930 | 2024-05-27 | +127.46% | -27.61% |

Interpretation:

```text
293780 is the early-high-MAE / delayed-MFE C24 warning.
The later 180D MFE looks large, but the selected entry first absorbed a -27% drawdown.
C24 should not treat delayed MFE as clean Stage2 return alignment unless the clinical-data thesis is repaired before or during the drawdown window.
```

---

## 7. Machine-readable trigger JSONL

```jsonl
{"row_type":"trigger","research_id":"R7L76_C24_BIO_PLATFORM_TRIAL_EVENT_ROUTER","round":"R7","loop":76,"large_sector_id":"L7_BIO_HEALTHCARE_MEDICAL","canonical_archetype_id":"C24_BIO_TRIAL_DATA_EVENT_RISK","fine_archetype_id":"ADC_RNA_VACCINE_TRIAL_PLATFORM_EVENT_MFE_AND_HIGH_MAE_ROUTER","symbol":"226950","name":"올릭스","trigger_type":"Stage2-Actionable-Guarded","trigger_family":"rna_therapeutics_trial_platform_event_low_mae_persistent_mfe","trigger_date":"2024-07-10","entry_date":"2024-07-11","entry_price":9300.0,"entry_price_type":"next_tradable_open_after_rna_therapeutics_trial_platform_event_burst","price_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","mfe_30d_pct":86.02,"mae_30d_pct":-0.54,"mfe_90d_pct":136.02,"mae_90d_pct":-0.54,"mfe_180d_pct":252.15,"mae_180d_pct":-0.54,"peak_price_180d":32750.0,"peak_date_180d":"2024-10-24","trough_price_180d":9250.0,"trough_date_180d":"2024-07-11","calibration_usable":true,"case_polarity":"positive_guarded_rna_platform_low_mae","evidence_url_pending":true,"source_proxy_only":true,"non_price_evidence_strength":"medium_pending_url_repair","price_only_blowoff":false,"expected_stage_current_profile":"Stage2-Guarded_to_Yellow_if_trial_data_partnering_cash_runway_bridge_repaired","residual_error_type":"rna_trial_platform_event_path_supports_positive_route_but_green_requires_url_repaired_trial_data_partnering_cash_runway_bridge"}
{"row_type":"trigger","research_id":"R7L76_C24_BIO_PLATFORM_TRIAL_EVENT_ROUTER","round":"R7","loop":76,"large_sector_id":"L7_BIO_HEALTHCARE_MEDICAL","canonical_archetype_id":"C24_BIO_TRIAL_DATA_EVENT_RISK","fine_archetype_id":"ADC_RNA_VACCINE_TRIAL_PLATFORM_EVENT_MFE_AND_HIGH_MAE_ROUTER","symbol":"298380","name":"에이비엘바이오","trigger_type":"Stage2-Actionable-Guarded","trigger_family":"bispecific_adc_platform_trial_partnering_high_mfe_later_drawdown","trigger_date":"2024-03-05","entry_date":"2024-03-06","entry_price":24550.0,"entry_price_type":"next_tradable_open_after_bispecific_adc_platform_event_burst","price_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","mfe_30d_pct":24.24,"mae_30d_pct":-5.5,"mfe_90d_pct":24.24,"mae_90d_pct":-12.42,"mfe_180d_pct":56.82,"mae_180d_pct":-13.65,"peak_price_180d":38500.0,"peak_date_180d":"2024-08-29","trough_price_180d":21200.0,"trough_date_180d":"2024-06-17","calibration_usable":true,"case_polarity":"positive_guarded_platform_mfe_later_drawdown","evidence_url_pending":true,"source_proxy_only":true,"non_price_evidence_strength":"medium_low_pending_url_repair","price_only_blowoff":false,"expected_stage_current_profile":"Stage2-Guarded_to_Yellow_only_if_platform_partnering_trial_quality_cash_bridge_repaired","residual_error_type":"adc_bispecific_platform_event_had_high_mfe_but_later_drawdown_requires_url_repaired_partnering_trial_and_cash_bridge_before_green"}
{"row_type":"trigger","research_id":"R7L76_C24_BIO_PLATFORM_TRIAL_EVENT_ROUTER","round":"R7","loop":76,"large_sector_id":"L7_BIO_HEALTHCARE_MEDICAL","canonical_archetype_id":"C24_BIO_TRIAL_DATA_EVENT_RISK","fine_archetype_id":"ADC_RNA_VACCINE_TRIAL_PLATFORM_EVENT_MFE_AND_HIGH_MAE_ROUTER","symbol":"206650","name":"유바이오로직스","trigger_type":"Stage2-FalsePositive-Candidate","trigger_family":"vaccine_pipeline_trial_approval_label_initial_mfe_later_mae","trigger_date":"2024-02-15","entry_date":"2024-02-16","entry_price":12230.0,"entry_price_type":"next_tradable_open_after_vaccine_pipeline_trial_approval_spike","price_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","mfe_30d_pct":10.38,"mae_30d_pct":-5.15,"mfe_90d_pct":18.56,"mae_90d_pct":-6.05,"mfe_180d_pct":18.56,"mae_180d_pct":-23.55,"peak_price_180d":14500.0,"peak_date_180d":"2024-04-08","trough_price_180d":9350.0,"trough_date_180d":"2024-08-05","calibration_usable":true,"case_polarity":"counterexample_initial_mfe_later_drawdown","evidence_url_pending":true,"source_proxy_only":true,"non_price_evidence_strength":"low_pending_url_repair","price_only_blowoff":false,"expected_stage_current_profile":"Stage2-Guarded_or_local_4B_watch_until_trial_approval_revenue_cash_bridge_repaired","residual_error_type":"vaccine_pipeline_event_had_modest_mfe_but_later_mae_blocks_yellow_green_without_approval_revenue_cash_bridge"}
{"row_type":"trigger","research_id":"R7L76_C24_BIO_PLATFORM_TRIAL_EVENT_ROUTER","round":"R7","loop":76,"large_sector_id":"L7_BIO_HEALTHCARE_MEDICAL","canonical_archetype_id":"C24_BIO_TRIAL_DATA_EVENT_RISK","fine_archetype_id":"ADC_RNA_VACCINE_TRIAL_PLATFORM_EVENT_MFE_AND_HIGH_MAE_ROUTER","symbol":"293780","name":"압타바이오","trigger_type":"Stage2-FalsePositive-Candidate","trigger_family":"clinical_event_failure_gapdown_then_delayed_mfe_high_mae","trigger_date":"2024-02-28","entry_date":"2024-02-29","entry_price":6810.0,"entry_price_type":"next_tradable_open_after_clinical_event_risk_gapdown","price_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","mfe_30d_pct":10.57,"mae_30d_pct":-27.53,"mfe_90d_pct":10.57,"mae_90d_pct":-27.61,"mfe_180d_pct":127.46,"mae_180d_pct":-27.61,"peak_price_180d":15490.0,"peak_date_180d":"2024-07-11","trough_price_180d":4930.0,"trough_date_180d":"2024-05-27","calibration_usable":true,"case_polarity":"counterexample_early_high_mae_delayed_mfe","evidence_url_pending":true,"source_proxy_only":true,"non_price_evidence_strength":"low_pending_url_repair","price_only_blowoff":false,"expected_stage_current_profile":"local_4B_watch_even_if_later_mfe_until_trial_data_thesis_repaired","residual_error_type":"clinical_event_risk_case_had_delayed_mfe_but_entry_first_absorbed_high_mae_and_requires_trial_data_repair_before_positive_stage"}
```

---

## 8. Score simulation and raw component breakdown

This is shadow-only and does not change production scoring.

| symbol | data / endpoint credibility | platform / partner quality | regulatory / next-readout path | cash runway / dilution risk | market mispricing | MAE risk control | information confidence | shadow total | intended route |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| `226950` | 10 | 10 | 9 | 7 | 15 | 15 | 5 | 71 | Stage2-Guarded / Yellow after evidence repair |
| `298380` | 10 | 9 | 8 | 6 | 10 | 8 | 5 | 56 | Stage2-Guarded / Yellow-watch after bridge repair |
| `206650` | 5 | 4 | 5 | 4 | 5 | 4 | 4 | 31 | Stage2-Guarded at most / local 4B watch |
| `293780` | 3 | 3 | 3 | 3 | 9 | 0 | 4 | 25 | local 4B watch despite delayed MFE |

### Current calibrated profile stress test

The current calibrated profile already blocks pure price-only blowoff.  
The remaining C24 issue is **bio event label without trial-data and cash-runway bridge**:

```text
C24 clean platform-event path:
  trial/platform relevance
  + persistent MFE
  + controlled MAE
  + URL-repaired data/partner/regulatory/cash bridge
  => Stage2-Guarded / Yellow, possible Green after proof

C24 high-MFE later-drawdown path:
  platform MFE is real
  + MAE_90D <= -10%
  + evidence remains source_proxy_only
  => Stage2-Guarded at most until evidence repair

C24 modest-MFE later-MAE path:
  MFE_180D < +25%
  + MAE_180D <= -20%
  + no approval/revenue/cash bridge
  => local 4B watch or blocked Stage2

C24 early-high-MAE delayed-MFE path:
  MAE_30D <= -20%
  + later MFE appears only after clinical-event risk
  + data thesis remains unrepaired
  => do not promote Yellow/Green from final-window MFE alone
```

`226950` and `298380` prevent overblocking.  
`206650` and `293780` show why C24 must care about early MAE and non-price evidence repair, not only final-window MFE.

---

## 9. Aggregate metrics

```json
{
  "row_type": "aggregate",
  "research_id": "R7L76_C24_BIO_PLATFORM_TRIAL_EVENT_ROUTER",
  "round": "R7",
  "loop": 76,
  "large_sector_id": "L7_BIO_HEALTHCARE_MEDICAL",
  "canonical_archetype_id": "C24_BIO_TRIAL_DATA_EVENT_RISK",
  "fine_archetype_id": "ADC_RNA_VACCINE_TRIAL_PLATFORM_EVENT_MFE_AND_HIGH_MAE_ROUTER",
  "case_count": 4,
  "calibration_usable_case_count": 4,
  "positive_guarded_case_count": 2,
  "counterexample_count": 2,
  "new_symbol_count": 4,
  "source_proxy_only_count": 4,
  "evidence_url_pending_count": 4,
  "avg_mfe_30d_pct": 32.8,
  "avg_mae_30d_pct": -9.68,
  "avg_mfe_90d_pct": 47.35,
  "avg_mae_90d_pct": -11.66,
  "avg_mfe_180d_pct": 113.75,
  "avg_mae_180d_pct": -16.34,
  "max_mfe_180d_pct": 252.15,
  "worst_mae_180d_pct": -27.61
}
```

---

## 10. 4B proximity split

```json
{
  "row_type": "4b_split",
  "research_id": "R7L76_C24_BIO_PLATFORM_TRIAL_EVENT_ROUTER",
  "stage2_guarded_or_yellow_candidate": [
    {
      "symbol": "226950",
      "reason": "RNA/platform event path had +252.15% 180D MFE with only -0.54% MAE"
    },
    {
      "symbol": "298380",
      "reason": "bispecific/ADC platform event had +56.82% 180D MFE, but 90D/180D MAE requires evidence repair"
    }
  ],
  "stage2_guarded_or_local_4b_watch": [
    {
      "symbol": "206650",
      "reason": "vaccine pipeline label had only +18.56% 180D MFE and -23.55% 180D MAE"
    },
    {
      "symbol": "293780",
      "reason": "clinical-event entry first absorbed -27.53% 30D MAE before delayed MFE arrived"
    }
  ],
  "full_4b_or_green_requires_non_price_evidence": [
    "trial data quality and endpoint credibility",
    "regulatory path and next readout timing",
    "partner / license economics",
    "cash runway and dilution risk",
    "approval / revenue bridge where relevant",
    "commercialization or reimbursement path"
  ]
}
```

---

## 11. Shadow rule candidate

```yaml
row_type: canonical_archetype_rule_candidate
canonical_archetype_id: C24_BIO_TRIAL_DATA_EVENT_RISK
fine_archetype_id: ADC_RNA_VACCINE_TRIAL_PLATFORM_EVENT_MFE_AND_HIGH_MAE_ROUTER
rule_name: C24_bio_platform_trial_event_mfe_and_high_mae_router
production_scoring_changed: false
shadow_weight_only: true
```

### Proposed routing logic

```text
For C24 bio trial / platform / clinical data event cases:

Tier A: verified platform-event winner
  Conditions:
    - trial data, endpoint, partner/license, regulatory, and cash-runway evidence are URL-repaired
    - MFE_90D >= +40%
    - MAE_90D > -10%
    - MFE persists beyond one event candle
  Routing:
    - Stage2-Guarded allowed
    - Stage3-Yellow allowed after evidence repair
    - Green only after data / partner / regulatory / cash bridge is verified

Tier B: high-MFE but later-drawdown platform case
  Conditions:
    - MFE_180D >= +50%
    - MAE_90D <= -10%
    - evidence_url_pending or source_proxy_only remains true
  Routing:
    - Stage2-Guarded at most
    - no Green until evidence repair

Tier C: modest-MFE later-MAE bio label
  Conditions:
    - MFE_180D < +25%
    - MAE_180D <= -20%
    - no repaired approval / revenue / cash bridge
  Routing:
    - local 4B watch or blocked Stage2
    - count as counterexample

Tier D: early-high-MAE delayed-MFE clinical event
  Conditions:
    - MAE_30D <= -20%
    - later MFE appears
    - trial-data thesis is unrepaired during the drawdown window
  Routing:
    - local 4B watch
    - no Yellow/Green from final-window MFE alone
```

### Suggested shadow delta

```json
{
  "row_type": "shadow_weight",
  "axis": "c24_bio_platform_trial_event_mfe_and_high_mae_router",
  "scope": "canonical_archetype_id:C24_BIO_TRIAL_DATA_EVENT_RISK",
  "proposal": {
    "source_proxy_only_green_allowed": false,
    "trial_data_partner_regulatory_cash_bridge_required_for_green": true,
    "verified_platform_winner_mfe90_threshold_pct": 40.0,
    "verified_platform_winner_mae90_min_pct": -10.0,
    "high_mfe_later_drawdown_mfe180_threshold_pct": 50.0,
    "high_mfe_later_drawdown_mae90_threshold_pct": -10.0,
    "modest_mfe_threshold_180d_pct": 25.0,
    "modest_mfe_later_mae_threshold_180d_pct": -20.0,
    "early_high_mae_threshold_30d_pct": -20.0,
    "delayed_mfe_does_not_override_early_high_mae_without_data_repair": true,
    "positive_weight_blocked_until_url_repair": true
  },
  "confidence": "medium_low_until_url_repair",
  "apply_now": false,
  "reason": "Two platform/trial event MFE holdouts and two high-MAE or modest-MFE bio event cases show that C24 should require URL-repaired trial data, endpoint, partner/license, regulatory, and cash-runway evidence before Yellow/Green."
}
```

---

## 12. Residual contribution summary

```json
{
  "row_type": "residual_contribution",
  "research_id": "R7L76_C24_BIO_PLATFORM_TRIAL_EVENT_ROUTER",
  "large_sector_id": "L7_BIO_HEALTHCARE_MEDICAL",
  "canonical_archetype_id": "C24_BIO_TRIAL_DATA_EVENT_RISK",
  "contribution": "Adds four non-top-covered C24 bio platform/trial-event cases and separates persistent-MFE RNA/ADC-platform holdouts from vaccine/modest-MFE and clinical-event early-high-MAE failures. C24 Yellow/Green should require URL-repaired trial data quality, endpoint credibility, partner/license economics, regulatory path, cash runway, dilution risk, and approval/revenue bridge evidence.",
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
  "data_quality_blocker": "All four non-price bio trial/platform triggers require URL-level repair before positive weight promotion.",
  "guardrail_added": "C24 source_proxy_only cases with MAE_30D <= -20% should route to local 4B watch even if delayed MFE appears; modest-MFE bio event cases with MFE_180D < +25% and MAE_180D <= -20% should block Yellow/Green."
}
```

One-line contribution:

```text
This loop adds 4 new independent cases, 2 counterexamples, and 2 residual errors for R7/L7_BIO_HEALTHCARE_MEDICAL/C24_BIO_TRIAL_DATA_EVENT_RISK.
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
    226950: false
    298380: false
    206650: false
    293780: false
  evidence_url_pending:
    226950: true
    298380: true
    206650: true
    293780: true
  source_proxy_only:
    226950: true
    298380: true
    206650: true
    293780: true
```

Limitations:

```text
- Price path is validated against Stock-Web tradable OHLC rows.
- Non-price evidence is not URL-repaired in this run.
- Therefore this artifact is useful for C24 bio platform / trial-event residual shape and high-MAE guardrail design, but should not promote positive weights until filings, IR, clinical registry data, conference abstracts, license disclosures, or reports verify trial data quality, endpoint credibility, partner/license economics, regulatory path, cash runway, and approval/revenue bridge.
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
2. Preserve R7 / loop 76 metadata.
3. Add the cases to C24_BIO_TRIAL_DATA_EVENT_RISK only if parser validation passes.
4. Treat all four non-price triggers as evidence_url_pending=true and source_proxy_only=true until URL-level evidence is repaired.
5. Do not use these rows for positive weight promotion until filings/IR/clinical-registry/conference-abstract/license-disclosure/report data verifies trial data quality, endpoint credibility, partner/license economics, regulatory path, cash runway, dilution risk, and approval/revenue bridge.
6. Add a shadow-only rule candidate named C24_bio_platform_trial_event_mfe_and_high_mae_router.
7. Do not loosen Stage3-Green.
8. Add C24-specific guards:
   - source_proxy_only -> no Green
   - Green requires repaired trial data / partner / regulatory / cash bridge
   - MFE_90D >= +40% and MAE_90D > -10% may remain Stage2-Guarded / Yellow watch after evidence repair
   - MFE_180D >= +50% but MAE_90D <= -10% -> Stage2-Guarded at most until evidence repair
   - MFE_180D < +25% and MAE_180D <= -20% -> local 4B watch or blocked Stage2
   - MAE_30D <= -20% -> local 4B watch; delayed MFE does not override early high MAE unless data thesis is repaired
9. Keep production scoring unchanged unless later batch promotion logic independently marks this axis safe.
```

---

## 15. Next round state

```text
completed_round = R7
completed_loop = 76
next_round = R8
next_loop = 76
next_large_sector_hint = L8_PLATFORM_CONTENT_SW_SECURITY
round_schedule_status = valid
round_sector_consistency = pass
```
