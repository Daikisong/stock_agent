# E2R Stock-Web v12 Residual Research — R7 Loop 74

```yaml
research_session: post_calibrated_sector_archetype_residual_research
mode: historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12
completed_round: R7
completed_loop: 74
next_round: R8
next_loop: 74
large_sector_id: L7_BIO_HEALTHCARE_MEDICAL
canonical_archetype_id: C24_BIO_TRIAL_DATA_EVENT_RISK
fine_archetype_id: CLINICAL_PLATFORM_DATA_MILESTONE_HIGH_MFE_VS_EVENT_RISK_ROUTER
output_file: e2r_stock_web_v12_residual_round_R7_loop_74_L7_BIO_HEALTHCARE_MEDICAL_C24_BIO_TRIAL_DATA_EVENT_RISK_research.md
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
completed_loop  = 74
large_sector_id = L6_FINANCIAL_CAPITAL_RETURN_DIGITAL
canonical_archetype_id = C22_INSURANCE_RATE_CYCLE_RESERVE
```

Therefore:

```text
scheduled_round = R7
scheduled_loop  = 74
```

R7 maps to:

```text
large_sector_id = L7_BIO_HEALTHCARE_MEDICAL
```

This run selects:

```text
canonical_archetype_id = C24_BIO_TRIAL_DATA_EVENT_RISK
fine_archetype_id = CLINICAL_PLATFORM_DATA_MILESTONE_HIGH_MFE_VS_EVENT_RISK_ROUTER
```

This is a valid R7/L7 pairing.

---

## 1. Why this R7/C24 run

The no-repeat ledger shows C24 is smaller than the heavily repeated C23 approval/commercialization set and has room for non-top-covered clinical-platform cases:

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

This file avoids those top-covered C24 symbols and adds:

```text
298380 에이비엘바이오
397030 에이프릴바이오
323990 박셀바이오
```

Research question:

```text
Can C24 separate clinical-platform / data-readthrough rerating with persistent MFE from clinical event spikes where the post-entry path shows weak MFE and severe MAE before durable regulatory or commercialization evidence appears?
```

C24 is a trial-data event-risk archetype. A clinical event is like a lab signal: it can be bright, but the signal must survive replication, regulatory interpretation, partner validation, and financing risk. A single bright readout should not become Green unless it travels the whole corridor from data to development path.

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
| `298380` | 에이비엘바이오 | active_like / KOSDAQ | none listed | true |
| `397030` | 에이프릴바이오 | active_like / KOSDAQ | no 2024 overlap; latest listed candidates 2023-10-31 / 2023-11-20 | true |
| `323990` | 박셀바이오 | active_like / KOSDAQ | no 2024 overlap; latest listed candidates 2023-11-23 / 2023-11-30 | true |

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
The Stock-Web price path is fully validated, but company-level clinical trial result, endpoint quality, partner validation, regulatory pathway, dose/safety durability, financing runway, milestone probability, and commercialization bridge evidence still require later URL repair through filings, IR decks, trial registries, conference abstracts, or regulatory documents before production weight promotion.
```

C24 interpretation used here:

```text
C24 is not simply “bio stock rose after a clinical headline.”
It asks whether trial/data event relevance is development-convertible:
- endpoint and safety quality,
- repeatability / durability of data,
- partner or licensing validation,
- regulatory path,
- financing runway and dilution risk,
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
397030 + C24_BIO_TRIAL_DATA_EVENT_RISK -> no direct match found
298380 + C24_BIO_TRIAL_DATA_EVENT_RISK -> no direct match found
323990 + C24_BIO_TRIAL_DATA_EVENT_RISK -> no direct match found
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
| `R7L74_C24_298380_20240306` | `298380` 에이비엘바이오 | bispecific antibody platform clinical data readthrough | positive-guarded / high-MFE |
| `R7L74_C24_397030_20240312` | `397030` 에이프릴바이오 | clinical pipeline / license milestone readthrough | positive-guarded / moderate-MAE |
| `R7L74_C24_323990_20240326` | `323990` 박셀바이오 | clinical data event spike without durable regulatory bridge | counterexample / high-MAE |

The intended residual:

```text
C24 should separate:
1. platform/data readthrough cases where MFE persists despite biotech volatility;
2. clinical pipeline reratings that remain useful but need evidence repair before Yellow/Green;
3. clinical event spikes where MFE is too weak and MAE crosses the 4B/4C guardrail.
```

---

## 6. Stock-Web OHLC and backtest

### 6.1 `298380` 에이비엘바이오 — bispecific antibody platform data readthrough

Trigger:

```text
trigger_date = 2024-03-05
trigger_type = Stage2-Actionable-Guarded
trigger_family = bispecific_antibody_platform_clinical_data_readthrough
entry_date = 2024-03-06
entry_price = 24550.0
entry_price_type = next_tradable_open_after_bio_platform_data_burst
```

Relevant Stock-Web rows:

```csv
d,o,h,l,c,v,a,mc,s,m
2024-03-05,23050.0,24200.0,22900.0,23950.0,972516.0,23182901150.0,1147026309050.0,47892539,KOSDAQ
2024-03-06,24550.0,28400.0,24350.0,27300.0,8136384.0,218893876800.0,1307466314700.0,47892539,KOSDAQ
2024-03-13,29800.0,30500.0,26300.0,27900.0,4377989.0,125411174800.0,1336201838100.0,47892539,KOSDAQ
2024-04-08,23550.0,23550.0,22000.0,22550.0,981641.0,22109245350.0,1079976754450.0,47892539,KOSDAQ
2024-07-04,27200.0,29750.0,27000.0,29700.0,8698482.0,251226019300.0,1427019333300.0,48047789,KOSDAQ
2024-08-29,34500.0,38500.0,32800.0,33950.0,15995123.0,569637037750.0,1631222436550.0,48047789,KOSDAQ
```

Backtest:

| window | peak/high | peak date | trough/low | trough date | MFE | MAE |
|---|---:|---|---:|---|---:|---:|
| 30 calendar days | 30500 | 2024-03-13 | 23200 | 2024-04-05 | +24.24% | -5.50% |
| 90 calendar days | 30500 | 2024-03-13 | 22000 | 2024-04-08 | +24.24% | -10.39% |
| 180 calendar days | 38500 | 2024-08-29 | 22000 | 2024-04-08 | +56.82% | -10.39% |

Interpretation:

```text
298380 is a positive-guarded C24 case.
The platform/data readthrough path survived the first biotech drawdown and later expanded to a strong 180D MFE.
This supports Stage2-Guarded / Yellow after evidence repair, not automatic Green.
```

### 6.2 `397030` 에이프릴바이오 — clinical pipeline / license milestone rerating

Trigger:

```text
trigger_date = 2024-03-11
trigger_type = Stage2-Actionable-Guarded
trigger_family = clinical_pipeline_license_data_milestone_rerating
entry_date = 2024-03-12
entry_price = 15790.0
entry_price_type = next_tradable_open_after_clinical_pipeline_data_burst
```

Relevant Stock-Web rows:

```csv
d,o,h,l,c,v,a,mc,s,m
2024-03-11,16000.0,17500.0,15150.0,15310.0,3424506.0,55566723440.0,331042465300.0,21622630,KOSDAQ
2024-03-12,15790.0,18230.0,15500.0,16680.0,5707052.0,96684683850.0,360665468400.0,21622630,KOSDAQ
2024-03-15,16200.0,19150.0,15710.0,17050.0,5266488.0,94197509050.0,368665841500.0,21622630,KOSDAQ
2024-04-11,13710.0,14140.0,13710.0,14000.0,154837.0,2154541710.0,302716820000.0,21622630,KOSDAQ
2024-06-26,20550.0,20800.0,18910.0,19290.0,2592274.0,51297160200.0,419010628500.0,21721650,KOSDAQ
2024-08-26,21850.0,25550.0,21400.0,24450.0,8078029.0,193397944750.0,535871041200.0,21917016,KOSDAQ
```

Backtest:

| window | peak/high | peak date | trough/low | trough date | MFE | MAE |
|---|---:|---|---:|---|---:|---:|
| 30 calendar days | 19150 | 2024-03-15 | 13710 | 2024-04-11 | +21.28% | -13.17% |
| 90 calendar days | 20800 | 2024-06-26 | 13710 | 2024-04-11 | +31.73% | -13.17% |
| 180 calendar days | 25550 | 2024-08-26 | 13710 | 2024-04-11 | +61.81% | -13.17% |

Interpretation:

```text
397030 is also positive-guarded, but with more biotech volatility than 298380.
It can be Stage2-Guarded / Yellow after URL repair, but the -13.17% MAE means Green should wait for stronger clinical, licensing, regulatory, and financing evidence.
```

### 6.3 `323990` 박셀바이오 — clinical event spike without durable bridge

Trigger:

```text
trigger_date = 2024-03-25
trigger_type = Stage2-FalsePositive-Candidate
trigger_family = clinical_data_event_spike_without_durable_regulatory_bridge
entry_date = 2024-03-26
entry_price = 23100.0
entry_price_type = next_tradable_open_after_clinical_event_spike
```

Relevant Stock-Web rows:

```csv
d,o,h,l,c,v,a,mc,s,m
2024-03-25,21450.0,24250.0,21050.0,23350.0,2889412.0,67053589950.0,536891220000.0,22993200,KOSDAQ
2024-03-26,23100.0,23200.0,22300.0,22550.0,574490.0,13038683650.0,518496660000.0,22993200,KOSDAQ
2024-03-27,23100.0,23600.0,21450.0,21450.0,1043408.0,23287366500.0,493204140000.0,22993200,KOSDAQ
2024-04-02,20050.0,20350.0,17510.0,18870.0,1888013.0,34849898710.0,433881684000.0,22993200,KOSDAQ
2024-06-26,15230.0,15370.0,15100.0,15140.0,130606.0,1983699200.0,348117048000.0,22993200,KOSDAQ
2024-08-05,15600.0,15690.0,13010.0,13670.0,405423.0,5895078700.0,314317044000.0,22993200,KOSDAQ
2024-09-11,13940.0,14180.0,13500.0,13510.0,103496.0,1424632950.0,310638132000.0,22993200,KOSDAQ
```

Backtest:

| window | peak/high | peak date | trough/low | trough date | MFE | MAE |
|---|---:|---|---:|---|---:|---:|
| 30 calendar days | 23600 | 2024-03-27 | 17650 | 2024-04-11 | +2.16% | -23.59% |
| 90 calendar days | 23600 | 2024-03-27 | 15100 | 2024-06-26 | +2.16% | -34.63% |
| 180 calendar days | 23600 | 2024-03-27 | 13010 | 2024-08-05 | +2.16% | -43.68% |

Interpretation:

```text
323990 is the hard C24 counterexample.
The clinical event spike was already spent by entry: MFE stayed near +2%, while MAE quickly crossed the high-MAE guardrail.
This should block Stage2/Green and route to 4B/4C watch until durable clinical/regulatory evidence is repaired.
```

---

## 7. Machine-readable trigger JSONL

```jsonl
{"row_type":"trigger","research_id":"R7L74_C24_BIO_TRIAL_DATA_ROUTER","round":"R7","loop":74,"large_sector_id":"L7_BIO_HEALTHCARE_MEDICAL","canonical_archetype_id":"C24_BIO_TRIAL_DATA_EVENT_RISK","fine_archetype_id":"CLINICAL_PLATFORM_DATA_MILESTONE_HIGH_MFE_VS_EVENT_RISK_ROUTER","symbol":"298380","name":"에이비엘바이오","trigger_type":"Stage2-Actionable-Guarded","trigger_family":"bispecific_antibody_platform_clinical_data_readthrough","trigger_date":"2024-03-05","entry_date":"2024-03-06","entry_price":24550.0,"entry_price_type":"next_tradable_open_after_bio_platform_data_burst","price_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","mfe_30d_pct":24.24,"mae_30d_pct":-5.5,"mfe_90d_pct":24.24,"mae_90d_pct":-10.39,"mfe_180d_pct":56.82,"mae_180d_pct":-10.39,"peak_price_180d":38500.0,"peak_date_180d":"2024-08-29","trough_price_180d":22000.0,"trough_date_180d":"2024-04-08","calibration_usable":true,"case_polarity":"positive_guarded_high_mfe","evidence_url_pending":true,"source_proxy_only":true,"non_price_evidence_strength":"medium_pending_url_repair","price_only_blowoff":false,"expected_stage_current_profile":"Stage2-Guarded_to_Yellow_if_trial_data_partnering_regulatory_bridge_repaired","residual_error_type":"positive_platform_data_path_requires_url_repaired_trial_data_partnering_commercialization_bridge_before_green"}
{"row_type":"trigger","research_id":"R7L74_C24_BIO_TRIAL_DATA_ROUTER","round":"R7","loop":74,"large_sector_id":"L7_BIO_HEALTHCARE_MEDICAL","canonical_archetype_id":"C24_BIO_TRIAL_DATA_EVENT_RISK","fine_archetype_id":"CLINICAL_PLATFORM_DATA_MILESTONE_HIGH_MFE_VS_EVENT_RISK_ROUTER","symbol":"397030","name":"에이프릴바이오","trigger_type":"Stage2-Actionable-Guarded","trigger_family":"clinical_pipeline_license_data_milestone_rerating","trigger_date":"2024-03-11","entry_date":"2024-03-12","entry_price":15790.0,"entry_price_type":"next_tradable_open_after_clinical_pipeline_data_burst","price_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","mfe_30d_pct":21.28,"mae_30d_pct":-13.17,"mfe_90d_pct":31.73,"mae_90d_pct":-13.17,"mfe_180d_pct":61.81,"mae_180d_pct":-13.17,"peak_price_180d":25550.0,"peak_date_180d":"2024-08-26","trough_price_180d":13710.0,"trough_date_180d":"2024-04-11","calibration_usable":true,"case_polarity":"positive_guarded_high_mfe_moderate_mae","evidence_url_pending":true,"source_proxy_only":true,"non_price_evidence_strength":"medium_pending_url_repair","price_only_blowoff":false,"expected_stage_current_profile":"Stage2-Guarded_to_Yellow_after_license_clinical_data_bridge_repaired","residual_error_type":"clinical_pipeline_mfe_was_persistent_but_green_requires_data_license_regulatory_evidence_repair"}
{"row_type":"trigger","research_id":"R7L74_C24_BIO_TRIAL_DATA_ROUTER","round":"R7","loop":74,"large_sector_id":"L7_BIO_HEALTHCARE_MEDICAL","canonical_archetype_id":"C24_BIO_TRIAL_DATA_EVENT_RISK","fine_archetype_id":"CLINICAL_PLATFORM_DATA_MILESTONE_HIGH_MFE_VS_EVENT_RISK_ROUTER","symbol":"323990","name":"박셀바이오","trigger_type":"Stage2-FalsePositive-Candidate","trigger_family":"clinical_data_event_spike_without_durable_regulatory_bridge","trigger_date":"2024-03-25","entry_date":"2024-03-26","entry_price":23100.0,"entry_price_type":"next_tradable_open_after_clinical_event_spike","price_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","mfe_30d_pct":2.16,"mae_30d_pct":-23.59,"mfe_90d_pct":2.16,"mae_90d_pct":-34.63,"mfe_180d_pct":2.16,"mae_180d_pct":-43.68,"peak_price_180d":23600.0,"peak_date_180d":"2024-03-27","trough_price_180d":13010.0,"trough_date_180d":"2024-08-05","calibration_usable":true,"case_polarity":"counterexample_clinical_event_high_mae","evidence_url_pending":true,"source_proxy_only":true,"non_price_evidence_strength":"low_pending_url_repair","price_only_blowoff":false,"expected_stage_current_profile":"blocked_Stage2_or_4B_4C_high_MAE_watch","residual_error_type":"clinical_event_entry_had_weak_mfe_and_large_mae_without_durable_data_regulatory_bridge"}
```

---

## 8. Score simulation and raw component breakdown

This is shadow-only and does not change production scoring.

| symbol | clinical data quality | partner / license validation | regulatory path | financing / dilution risk control | market mispricing | milestone conversion | information confidence | shadow total | intended route |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| `298380` | 12 | 11 | 9 | 7 | 12 | 10 | 6 | 67 | Stage2-Guarded / Yellow after evidence repair |
| `397030` | 11 | 10 | 8 | 6 | 11 | 10 | 6 | 62 | Stage2-Guarded; no Green until clinical/license bridge repair |
| `323990` | 3 | 2 | 2 | 1 | 3 | 2 | 4 | 17 | blocked Stage2 / 4B-4C high-MAE watch |

### Current calibrated profile stress test

The current calibrated profile already blocks pure price-only blowoff.  
The remaining C24 issue is **clinical event relevance without durable data/regulatory conversion**:

```text
C24 positive-guarded path:
  clinical platform/data event relevance
  + MFE expands across 90D/180D
  + MAE stays survivable
  + URL-repaired partner / regulatory / financing bridge
  => Stage2-Guarded / Yellow candidate

C24 clinical-event false-positive path:
  entry follows clinical event spike
  + MFE_30D < +5%
  + MAE_30D <= -20%
  + no durable data/regulatory bridge
  => block Stage2 and route to 4B/4C high-MAE watch
```

`298380` and `397030` prevent overblocking.  
`323990` shows why trial/data headlines must be routed through a high-MAE guard when the entry occurs after the event candle has already spent the upside.

---

## 9. Aggregate metrics

```json
{
  "row_type": "aggregate",
  "research_id": "R7L74_C24_BIO_TRIAL_DATA_ROUTER",
  "round": "R7",
  "loop": 74,
  "large_sector_id": "L7_BIO_HEALTHCARE_MEDICAL",
  "canonical_archetype_id": "C24_BIO_TRIAL_DATA_EVENT_RISK",
  "fine_archetype_id": "CLINICAL_PLATFORM_DATA_MILESTONE_HIGH_MFE_VS_EVENT_RISK_ROUTER",
  "case_count": 3,
  "calibration_usable_case_count": 3,
  "positive_guarded_case_count": 2,
  "counterexample_count": 1,
  "new_symbol_count": 3,
  "source_proxy_only_count": 3,
  "evidence_url_pending_count": 3,
  "avg_mfe_30d_pct": 15.89,
  "avg_mae_30d_pct": -14.09,
  "avg_mfe_90d_pct": 19.38,
  "avg_mae_90d_pct": -19.4,
  "avg_mfe_180d_pct": 40.26,
  "avg_mae_180d_pct": -22.41,
  "max_mfe_180d_pct": 61.81,
  "worst_mae_180d_pct": -43.68
}
```

---

## 10. 4B proximity split

```json
{
  "row_type": "4b_split",
  "research_id": "R7L74_C24_BIO_TRIAL_DATA_ROUTER",
  "stage2_guarded_or_yellow_candidate": [
    {
      "symbol": "298380",
      "reason": "persistent +56.82% 180D MFE with survivable -10.39% MAE; requires clinical/partner/regulatory evidence repair before Green"
    },
    {
      "symbol": "397030",
      "reason": "persistent +61.81% 180D MFE but -13.17% MAE; requires license/data/financing bridge repair before Yellow/Green"
    }
  ],
  "blocked_stage2_or_4c_watch": [
    {
      "symbol": "323990",
      "reason": "MFE stayed only +2.16%, while 30D MAE reached -23.59% and 180D MAE reached -43.68%"
    }
  ],
  "full_4b_or_green_requires_non_price_evidence": [
    "trial endpoint and safety durability",
    "partner / licensing validation",
    "regulatory pathway clarity",
    "financing runway and dilution risk control",
    "milestone-to-commercialization bridge"
  ]
}
```

---

## 11. Shadow rule candidate

```yaml
row_type: canonical_archetype_rule_candidate
canonical_archetype_id: C24_BIO_TRIAL_DATA_EVENT_RISK
fine_archetype_id: CLINICAL_PLATFORM_DATA_MILESTONE_HIGH_MFE_VS_EVENT_RISK_ROUTER
rule_name: C24_trial_data_milestone_high_mfe_vs_event_spike_mae_router
production_scoring_changed: false
shadow_weight_only: true
```

### Proposed routing logic

```text
For C24 bio trial/data event-risk cases:

Tier A: validated clinical-platform rerating
  Conditions:
    - clinical data / partner / regulatory evidence is URL-repaired
    - MFE expands across 90D or 180D
    - MAE remains survivable
    - financing or dilution risk is controlled
  Routing:
    - Stage2-Actionable-Guarded allowed
    - Stage3-Yellow allowed after evidence repair
    - Green only after trial data, regulatory, partner, and financing bridge are verified

Tier B: positive but volatile data milestone
  Conditions:
    - MFE_180D >= +40%
    - MAE_180D > -20%
    - evidence_url_pending or source_proxy_only remains true
  Routing:
    - Stage2-Guarded at most
    - no Green until evidence repair

Tier C: event spike already spent
  Conditions:
    - MFE_30D < +5%
    - MAE_30D <= -20%
    - no durable data/regulatory bridge
  Routing:
    - block Stage2
    - local 4B / 4C high-MAE watch
    - count as counterexample
```

### Suggested shadow delta

```json
{
  "row_type": "shadow_weight",
  "axis": "c24_trial_data_milestone_high_mfe_vs_event_spike_mae_router",
  "scope": "canonical_archetype_id:C24_BIO_TRIAL_DATA_EVENT_RISK",
  "proposal": {
    "source_proxy_only_green_allowed": false,
    "trial_data_partner_regulatory_bridge_required_for_green": true,
    "positive_mfe180_threshold_pct": 40.0,
    "survivable_mae180_threshold_pct": -20.0,
    "event_spike_weak_mfe_threshold_30d_pct": 5.0,
    "event_spike_high_mae_threshold_30d_pct": -20.0,
    "positive_weight_blocked_until_url_repair": true
  },
  "confidence": "medium_low_until_url_repair",
  "apply_now": false,
  "reason": "Two clinical-platform positive paths and one clinical event-spike high-MAE counterexample show that C24 should preserve persistent MFE data-readthrough winners while blocking entries where the event candle has already spent the upside."
}
```

---

## 12. Residual contribution summary

```json
{
  "row_type": "residual_contribution",
  "research_id": "R7L74_C24_BIO_TRIAL_DATA_ROUTER",
  "large_sector_id": "L7_BIO_HEALTHCARE_MEDICAL",
  "canonical_archetype_id": "C24_BIO_TRIAL_DATA_EVENT_RISK",
  "contribution": "Adds three non-top-covered C24 bio trial/data event-risk cases and separates persistent clinical-platform data readthrough from a clinical event-spike false positive. C24 Green should require URL-repaired trial endpoint quality, partner/licensing validation, regulatory path, financing runway, and milestone-to-commercialization bridge evidence.",
  "positive_guarded_case_added": 2,
  "counterexample_case_added": 1,
  "new_symbol_count": 3,
  "data_quality_blocker": "All three non-price bio trial/data triggers require URL-level repair before positive weight promotion.",
  "guardrail_added": "C24 event-spike cases with MFE_30D < +5% and MAE_30D <= -20% should block Stage2 or route to 4B/4C high-MAE watch; persistent high-MFE cases remain Stage2-Guarded until evidence repair."
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
    298380: false
    397030: false
    323990: false
  evidence_url_pending:
    298380: true
    397030: true
    323990: true
  source_proxy_only:
    298380: true
    397030: true
    323990: true
```

Limitations:

```text
- Price path is validated against Stock-Web tradable OHLC rows.
- Non-price evidence is not URL-repaired in this run.
- Therefore this artifact is useful for C24 trial/data event-risk residual shape and high-MAE guardrail design, but should not promote positive weights until filings, IR, trial registry, conference, or regulatory documents verify endpoint quality, partner validation, regulatory path, financing runway, and milestone bridge.
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
2. Preserve R7 / loop 74 metadata.
3. Add the cases to C24_BIO_TRIAL_DATA_EVENT_RISK only if parser validation passes.
4. Treat all three non-price triggers as evidence_url_pending=true and source_proxy_only=true until URL-level evidence is repaired.
5. Do not use these rows for positive weight promotion until filings/IR/trial-registry/conference/regulatory data verifies endpoint quality, safety durability, partner/licensing validation, regulatory path, financing runway, and milestone-to-commercialization bridge.
6. Add a shadow-only rule candidate named C24_trial_data_milestone_high_mfe_vs_event_spike_mae_router.
7. Do not loosen Stage3-Green.
8. Add C24-specific guards:
   - source_proxy_only -> no Green
   - Green requires repaired trial-data / partner / regulatory / financing bridge
   - MFE_180D >= +40% and MAE_180D > -20% may remain Stage2-Guarded until evidence repair
   - MFE_30D < +5% and MAE_30D <= -20% without durable evidence -> block Stage2 or 4B/4C high-MAE watch
9. Keep production scoring unchanged unless later batch promotion logic independently marks this axis safe.
```

---

## 15. Next round state

```text
completed_round = R7
completed_loop = 74
next_round = R8
next_loop = 74
next_large_sector_hint = L8_PLATFORM_CONTENT_SW_SECURITY
round_schedule_status = valid
round_sector_consistency = pass
```
