# E2R Stock-Web v12 Residual Research — R8 Loop 76

```yaml
research_session: post_calibrated_sector_archetype_residual_research
mode: historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12
completed_round: R8
completed_loop: 76
next_round: R9
next_loop: 76
large_sector_id: L8_PLATFORM_CONTENT_SW_SECURITY
canonical_archetype_id: C28_SOFTWARE_SECURITY_CONTRACT_RETENTION
fine_archetype_id: ENTERPRISE_SOFTWARE_DIGITAL_ID_SECURITY_CONTRACT_RETENTION_AND_WEAK_MFE_ROUTER
output_file: e2r_stock_web_v12_residual_round_R8_loop_76_L8_PLATFORM_CONTENT_SW_SECURITY_C28_SOFTWARE_SECURITY_CONTRACT_RETENTION_research.md
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
completed_round = R7
completed_loop  = 76
large_sector_id = L7_BIO_HEALTHCARE_MEDICAL
canonical_archetype_id = C24_BIO_TRIAL_DATA_EVENT_RISK
```

Therefore:

```text
scheduled_round = R8
scheduled_loop  = 76
```

R8 maps to:

```text
large_sector_id = L8_PLATFORM_CONTENT_SW_SECURITY
```

This run selects:

```text
canonical_archetype_id = C28_SOFTWARE_SECURITY_CONTRACT_RETENTION
fine_archetype_id = ENTERPRISE_SOFTWARE_DIGITAL_ID_SECURITY_CONTRACT_RETENTION_AND_WEAK_MFE_ROUTER
```

This is a valid R8/L8 pairing.

---

## 1. Why this R8/C28 run

The no-repeat ledger shows C28 is covered, but the top coverage is concentrated in a handful of security/software names:

```text
C28_SOFTWARE_SECURITY_CONTRACT_RETENTION:
  rows: 102
  symbols: 22
  date_range: 2019-05-27~2024-08-13
  good/bad S2: 28/6
  4B/4C: 20/2
  URL/proxy: 15/15
  top covered symbols: 012510(20), 053800(16), 263860(12), 030520(7), 131370(6), 136540(6)
```

This file avoids those top-covered symbols and adds four enterprise software / digital ID / security cases:

```text
307950 현대오토에버
058970 엠로
042510 라온시큐어
053300 한국정보인증
```

Research question:

```text
Can C28 separate enterprise software contract-retention rerating from digital ID / security event labels where contract retention, recurring revenue, deployment, and margin conversion are not visible and the path shows weak MFE or high MAE?
```

C28 is a software-retention bridge. A demo, policy headline, or security event is only the login screen. Stage2 needs the paid seat, the renewal, the deployment, the margin, and the customer reference. Without those, the password works once and the session expires.

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
| `307950` | 현대오토에버 | active_like / KOSPI | no 2024 overlap; latest listed candidate 2021-04-14 | true |
| `058970` | 엠로 | active_like / KOSDAQ | no 2024 overlap; latest listed candidates 2022 only | true |
| `042510` | 라온시큐어 | active_like / KOSDAQ | 2023-12-18 before selected entry, 2025-05-07 after selected 180D window | true for selected 180D |
| `053300` | 한국정보인증 | active_like / KOSDAQ | no 2024 overlap; latest listed candidate 2021-10-05 | true |

Profile caveat:

```text
Stock-Web OHLC is raw/unadjusted marcap data.
These cases are calibration-safe for the selected 2024 30D/90D/180D windows because no listed corporate-action candidate overlaps each entry~D+180 test window.
For 042510, the 2025-05-07 corporate-action candidate is after the selected 180D window and is not used here.
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
The Stock-Web price path is fully validated, but company-level contract renewal, ARR/recurring revenue, backlog, deployment schedule, customer concentration, churn, gross margin, security subscription conversion, digital ID policy execution, and cash-flow evidence still require later URL repair through filings, IR decks, contract disclosures, procurement data, customer references, or sell-side reports before production weight promotion.
```

C28 interpretation used here:

```text
C28 is not simply “software/security stock rose.”
It asks whether software or security relevance becomes contract economics:
- contract renewal and retention,
- ARR / recurring revenue / backlog,
- customer deployment and referenceability,
- churn and seat expansion,
- security subscription or identity transaction monetization,
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
307950 + C28_SOFTWARE_SECURITY_CONTRACT_RETENTION -> no direct match found
058970 + C28_SOFTWARE_SECURITY_CONTRACT_RETENTION -> no direct match found
042510 + C28_SOFTWARE_SECURITY_CONTRACT_RETENTION -> no direct match found
053300 + C28_SOFTWARE_SECURITY_CONTRACT_RETENTION -> no direct match found
```

Novelty accounting:

```json
{
  "new_symbol_count": 4,
  "minimum_new_symbol_count": 2,
  "positive_guarded_case_count": 1,
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
| `R8L76_C28_307950_20240424` | `307950` 현대오토에버 | enterprise/vehicle software contract retention low-MAE rerating | positive-guarded |
| `R8L76_C28_058970_20240321` | `058970` 엠로 | procurement SaaS / AI contract MFE with later high MAE | high-MFE later-MAE counterexample |
| `R8L76_C28_042510_20240828` | `042510` 라온시큐어 | digital ID/security event weak-MFE high-MAE | weak-MFE high-MAE counterexample |
| `R8L76_C28_053300_20240904` | `053300` 한국정보인증 | digital certificate/security event with early drawdown and delayed MFE | early drawdown / delayed-MFE counterexample |

The intended residual:

```text
C28 should separate:
1. enterprise software contract paths where MFE is moderate but MAE is very controlled;
2. enterprise SaaS paths where first-window MFE is real but 180D drawdown blocks Green;
3. security/digital-ID event labels where MFE is weak and MAE becomes high;
4. identity/certificate cases where delayed MFE should not erase early drawdown without contract revenue evidence.
```

---

## 6. Stock-Web OHLC and backtest

### 6.1 `307950` 현대오토에버 — enterprise/vehicle software contract-retention low-MAE rerating

Trigger:

```text
trigger_date = 2024-04-23
trigger_type = Stage2-Actionable-Guarded
trigger_family = enterprise_vehicle_software_contract_retention_low_mae_rerating
entry_date = 2024-04-24
entry_price = 143200.0
entry_price_type = next_tradable_open_after_enterprise_vehicle_software_contract_burst
```

Relevant Stock-Web rows:

```csv
d,o,h,l,c,v,a,mc,s,m
2024-04-23,142000.0,143100.0,139700.0,140200.0,57161.0,8062720200.0,3844842276400.0,27423982,KOSPI
2024-04-24,143200.0,154700.0,142500.0,154200.0,413460.0,62441203600.0,4228778024400.0,27423982,KOSPI
2024-04-30,170000.0,173500.0,154000.0,154000.0,1092422.0,180095160500.0,4223293228000.0,27423982,KOSPI
2024-07-11,177600.0,181900.0,175000.0,175000.0,168755.0,30102374000.0,4799196850000.0,27423982,KOSPI
2024-08-05,151100.0,154000.0,139700.0,144500.0,178185.0,26384993600.0,3962765399000.0,27423982,KOSPI
2024-09-20,166000.0,168800.0,163700.0,165300.0,106855.0,17781638000.0,4533184224600.0,27423982,KOSPI
```

Backtest:

| window | peak/high | peak date | trough/low | trough date | MFE | MAE |
|---|---:|---|---:|---|---:|---:|
| 30 calendar days | 173500 | 2024-04-30 | 142500 | 2024-04-24 | +21.16% | -0.49% |
| 90 calendar days | 181900 | 2024-07-11 | 142500 | 2024-04-24 | +27.03% | -0.49% |
| 180 calendar days | 181900 | 2024-07-11 | 139700 | 2024-08-05 | +27.03% | -2.44% |

Interpretation:

```text
307950 is the C28 positive-guarded holdout.
The path was not explosive like a small-cap theme, but MFE was persistent and MAE was very controlled.
This should remain Stage2-Guarded / Yellow-after-repair, not Green while contract retention, recurring revenue, deployment, and margin evidence remains source-proxy-only.
```

### 6.2 `058970` 엠로 — procurement SaaS / AI contract MFE with later high MAE

Trigger:

```text
trigger_date = 2024-03-20
trigger_type = Stage2-Actionable-Guarded
trigger_family = enterprise_procurement_saas_ai_contract_mfe_later_high_mae
entry_date = 2024-03-21
entry_price = 59500.0
entry_price_type = next_tradable_open_after_procurement_saas_ai_contract_burst
```

Relevant Stock-Web rows:

```csv
d,o,h,l,c,v,a,mc,s,m
2024-03-20,57300.0,59300.0,57300.0,59000.0,67411.0,3929357300.0,661515080000.0,11212120,KOSDAQ
2024-03-21,59500.0,63600.0,59000.0,63600.0,220197.0,13591344900.0,713090832000.0,11212120,KOSDAQ
2024-03-27,70000.0,72000.0,65800.0,68000.0,422348.0,29263914300.0,762424160000.0,11212120,KOSDAQ
2024-05-31,74500.0,76300.0,72900.0,75100.0,171030.0,12784147600.0,842030212000.0,11212120,KOSDAQ
2024-08-05,46000.0,46700.0,39000.0,39700.0,311711.0,13142396350.0,445121164000.0,11212120,KOSDAQ
2024-08-08,39650.0,40300.0,37900.0,39300.0,131141.0,5114698750.0,440636316000.0,11212120,KOSDAQ
2024-09-20,48300.0,51900.0,48300.0,51500.0,106782.0,5392504900.0,610466477000.0,11853718,KOSDAQ
```

Backtest:

| window | peak/high | peak date | trough/low | trough date | MFE | MAE |
|---|---:|---|---:|---|---:|---:|
| 30 calendar days | 72000 | 2024-03-27 | 56200 | 2024-04-16 | +21.01% | -5.55% |
| 90 calendar days | 76300 | 2024-05-31 | 56200 | 2024-04-16 | +28.24% | -5.55% |
| 180 calendar days | 76300 | 2024-05-31 | 37900 | 2024-08-08 | +28.24% | -36.30% |

Interpretation:

```text
058970 is the C28 high-MFE / later-high-MAE warning.
The first 90D path looked like a real SaaS/AI contract rerating, but 180D MAE crossed a hard guardrail.
This should cap at Stage2-Guarded or local 4B watch until ARR, contract retention, deployment, customer expansion, and margin evidence are URL-repaired.
```

### 6.3 `042510` 라온시큐어 — digital ID/security event weak-MFE high-MAE

Trigger:

```text
trigger_date = 2024-08-27
trigger_type = Stage2-FalsePositive-Candidate
trigger_family = digital_id_security_event_weak_mfe_high_mae
entry_date = 2024-08-28
entry_price = 2280.0
entry_price_type = next_tradable_open_after_digital_id_security_theme_burst
```

Relevant Stock-Web rows:

```csv
d,o,h,l,c,v,a,mc,s,m
2024-08-27,2040.0,2325.0,1990.0,2245.0,11356269.0,25197442308.0,125778080395.0,56025871,KOSDAQ
2024-08-28,2280.0,2560.0,2175.0,2180.0,16744546.0,40330866795.0,122136398780.0,56025871,KOSDAQ
2024-08-30,2210.0,2595.0,2190.0,2390.0,30595329.0,75731726580.0,133901831690.0,56025871,KOSDAQ
2024-09-11,2060.0,2105.0,1989.0,2105.0,820789.0,1677535041.0,117934458455.0,56025871,KOSDAQ
2024-11-15,1655.0,1739.0,1655.0,1737.0,108981.0,186823806.0,97316937927.0,56025871,KOSDAQ
2024-12-09,1711.0,1744.0,1650.0,1652.0,364245.0,612141065.0,92554738892.0,56025871,KOSDAQ
2025-02-04,2080.0,2465.0,2080.0,2175.0,11016216.0,25359042160.0,121856269425.0,56025871,KOSDAQ
```

Backtest:

| window | peak/high | peak date | trough/low | trough date | MFE | MAE |
|---|---:|---|---:|---|---:|---:|
| 30 calendar days | 2595 | 2024-08-30 | 1989 | 2024-09-11 | +13.82% | -12.76% |
| 90 calendar days | 2595 | 2024-08-30 | 1655 | 2024-11-15 | +13.82% | -27.41% |
| 180 calendar days | 2595 | 2024-08-30 | 1650 | 2024-12-09 | +13.82% | -27.63% |

Interpretation:

```text
042510 is the digital-ID/security false-positive branch.
The event label was plausible, but MFE stayed too weak and MAE widened quickly.
This should block Green and usually block Stage2 unless a later independent trigger repairs security-contract revenue, recurring subscription, digital-ID monetization, and margin evidence.
```

### 6.4 `053300` 한국정보인증 — digital certificate/security event with early drawdown and delayed MFE

Trigger:

```text
trigger_date = 2024-09-03
trigger_type = Stage2-FalsePositive-Candidate
trigger_family = digital_certificate_identity_security_delayed_mfe_drawdown
entry_date = 2024-09-04
entry_price = 4605.0
entry_price_type = next_tradable_open_after_digital_certificate_identity_security_burst
```

Relevant Stock-Web rows:

```csv
d,o,h,l,c,v,a,mc,s,m
2024-09-03,3905.0,4665.0,3905.0,4585.0,8511616.0,38154547940.0,194593640185.0,42441361,KOSDAQ
2024-09-04,4605.0,4795.0,4200.0,4330.0,4404547.0,20169339570.0,183771093130.0,42441361,KOSDAQ
2024-09-19,3855.0,3865.0,3710.0,3830.0,144797.0,548368335.0,162550412630.0,42441361,KOSDAQ
2025-01-06,4360.0,5420.0,4310.0,5030.0,16742349.0,84613992905.0,213480045830.0,42441361,KOSDAQ
2025-01-07,4930.0,5510.0,4890.0,5100.0,7405147.0,38734023790.0,216450941100.0,42441361,KOSDAQ
2025-02-28,4600.0,4650.0,4510.0,4535.0,188168.0,857104105.0,192471572135.0,42441361,KOSDAQ
```

Backtest:

| window | peak/high | peak date | trough/low | trough date | MFE | MAE |
|---|---:|---|---:|---|---:|---:|
| 30 calendar days | 4795 | 2024-09-04 | 3710 | 2024-09-19 | +4.13% | -19.44% |
| 90 calendar days | 4795 | 2024-09-04 | 3710 | 2024-09-19 | +4.13% | -19.44% |
| 180 calendar days | 5510 | 2025-01-07 | 3710 | 2024-09-19 | +19.65% | -19.44% |

Interpretation:

```text
053300 is the early-drawdown / delayed-MFE counterexample.
The delayed January 2025 MFE should not erase the first 30D/90D failure pattern.
C28 should cap this at Stage2-Guarded or local 4B watch until digital-certificate contract revenue, identity transaction monetization, customer retention, and margin evidence are repaired.
```

---

## 7. Machine-readable trigger JSONL

```jsonl
{"row_type":"trigger","research_id":"R8L76_C28_SOFTWARE_SECURITY_CONTRACT_ROUTER","round":"R8","loop":76,"large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C28_SOFTWARE_SECURITY_CONTRACT_RETENTION","fine_archetype_id":"ENTERPRISE_SOFTWARE_DIGITAL_ID_SECURITY_CONTRACT_RETENTION_AND_WEAK_MFE_ROUTER","symbol":"307950","name":"현대오토에버","trigger_type":"Stage2-Actionable-Guarded","trigger_family":"enterprise_vehicle_software_contract_retention_low_mae_rerating","trigger_date":"2024-04-23","entry_date":"2024-04-24","entry_price":143200.0,"entry_price_type":"next_tradable_open_after_enterprise_vehicle_software_contract_burst","price_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","mfe_30d_pct":21.16,"mae_30d_pct":-0.49,"mfe_90d_pct":27.03,"mae_90d_pct":-0.49,"mfe_180d_pct":27.03,"mae_180d_pct":-2.44,"peak_price_180d":181900.0,"peak_date_180d":"2024-07-11","trough_price_180d":139700.0,"trough_date_180d":"2024-08-05","calibration_usable":true,"case_polarity":"positive_guarded_enterprise_software_low_mae","evidence_url_pending":true,"source_proxy_only":true,"non_price_evidence_strength":"medium_pending_url_repair","price_only_blowoff":false,"expected_stage_current_profile":"Stage2-Guarded_to_Yellow_if_contract_retention_margin_and_recurring_revenue_bridge_repaired","residual_error_type":"enterprise_software_contract_retention_path_had_low_mae_but_green_requires_url_repaired_contract_retention_recurring_revenue_margin_bridge"}
{"row_type":"trigger","research_id":"R8L76_C28_SOFTWARE_SECURITY_CONTRACT_ROUTER","round":"R8","loop":76,"large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C28_SOFTWARE_SECURITY_CONTRACT_RETENTION","fine_archetype_id":"ENTERPRISE_SOFTWARE_DIGITAL_ID_SECURITY_CONTRACT_RETENTION_AND_WEAK_MFE_ROUTER","symbol":"058970","name":"엠로","trigger_type":"Stage2-Actionable-Guarded","trigger_family":"enterprise_procurement_saas_ai_contract_mfe_later_high_mae","trigger_date":"2024-03-20","entry_date":"2024-03-21","entry_price":59500.0,"entry_price_type":"next_tradable_open_after_procurement_saas_ai_contract_burst","price_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","mfe_30d_pct":21.01,"mae_30d_pct":-5.55,"mfe_90d_pct":28.24,"mae_90d_pct":-5.55,"mfe_180d_pct":28.24,"mae_180d_pct":-36.3,"peak_price_180d":76300.0,"peak_date_180d":"2024-05-31","trough_price_180d":37900.0,"trough_date_180d":"2024-08-08","calibration_usable":true,"case_polarity":"counterexample_mfe_later_high_mae","evidence_url_pending":true,"source_proxy_only":true,"non_price_evidence_strength":"medium_low_pending_url_repair","price_only_blowoff":false,"expected_stage_current_profile":"Stage2-Guarded_or_local_4B_watch_until_saas_backlog_retention_margin_bridge_repaired","residual_error_type":"enterprise_procurement_saas_ai_label_had_mfe_but_180d_mae_blocks_yellow_green_without_contract_retention_margin_bridge"}
{"row_type":"trigger","research_id":"R8L76_C28_SOFTWARE_SECURITY_CONTRACT_ROUTER","round":"R8","loop":76,"large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C28_SOFTWARE_SECURITY_CONTRACT_RETENTION","fine_archetype_id":"ENTERPRISE_SOFTWARE_DIGITAL_ID_SECURITY_CONTRACT_RETENTION_AND_WEAK_MFE_ROUTER","symbol":"042510","name":"라온시큐어","trigger_type":"Stage2-FalsePositive-Candidate","trigger_family":"digital_id_security_event_weak_mfe_high_mae","trigger_date":"2024-08-27","entry_date":"2024-08-28","entry_price":2280.0,"entry_price_type":"next_tradable_open_after_digital_id_security_theme_burst","price_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","mfe_30d_pct":13.82,"mae_30d_pct":-12.76,"mfe_90d_pct":13.82,"mae_90d_pct":-27.41,"mfe_180d_pct":13.82,"mae_180d_pct":-27.63,"peak_price_180d":2595.0,"peak_date_180d":"2024-08-30","trough_price_180d":1650.0,"trough_date_180d":"2024-12-09","calibration_usable":true,"case_polarity":"counterexample_security_event_weak_mfe_high_mae","evidence_url_pending":true,"source_proxy_only":true,"non_price_evidence_strength":"low_pending_url_repair","price_only_blowoff":false,"expected_stage_current_profile":"blocked_Stage2_or_local_4B_high_MAE_watch_until_security_contract_revenue_bridge_repaired","residual_error_type":"digital_id_security_theme_had_weak_mfe_and_high_mae_without_contract_retention_or_margin_bridge"}
{"row_type":"trigger","research_id":"R8L76_C28_SOFTWARE_SECURITY_CONTRACT_ROUTER","round":"R8","loop":76,"large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C28_SOFTWARE_SECURITY_CONTRACT_RETENTION","fine_archetype_id":"ENTERPRISE_SOFTWARE_DIGITAL_ID_SECURITY_CONTRACT_RETENTION_AND_WEAK_MFE_ROUTER","symbol":"053300","name":"한국정보인증","trigger_type":"Stage2-FalsePositive-Candidate","trigger_family":"digital_certificate_identity_security_delayed_mfe_drawdown","trigger_date":"2024-09-03","entry_date":"2024-09-04","entry_price":4605.0,"entry_price_type":"next_tradable_open_after_digital_certificate_identity_security_burst","price_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","mfe_30d_pct":4.13,"mae_30d_pct":-19.44,"mfe_90d_pct":4.13,"mae_90d_pct":-19.44,"mfe_180d_pct":19.65,"mae_180d_pct":-19.44,"peak_price_180d":5510.0,"peak_date_180d":"2025-01-07","trough_price_180d":3710.0,"trough_date_180d":"2024-09-19","calibration_usable":true,"case_polarity":"counterexample_early_drawdown_delayed_mfe","evidence_url_pending":true,"source_proxy_only":true,"non_price_evidence_strength":"low_pending_url_repair","price_only_blowoff":false,"expected_stage_current_profile":"Stage2-Guarded_at_most_or_local_4B_watch_until_identity_security_contract_revenue_bridge_repaired","residual_error_type":"digital_certificate_identity_event_had_weak_30d_90d_mfe_and_early_high_mae_before_delayed_mfe_without_contract_revenue_bridge"}
```

---

## 8. Score simulation and raw component breakdown

This is shadow-only and does not change production scoring.

| symbol | contract retention | recurring / transaction revenue | deployment / customer bridge | churn / renewal risk | market mispricing | margin conversion | information confidence | shadow total | intended route |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| `307950` | 12 | 10 | 11 | 9 | 8 | 9 | 6 | 65 | Stage2-Guarded / Yellow after evidence repair |
| `058970` | 9 | 7 | 7 | 4 | 8 | 4 | 5 | 44 | Stage2-Guarded or local 4B watch |
| `042510` | 4 | 3 | 3 | 2 | 3 | 2 | 4 | 21 | blocked Stage2 / high-MAE watch |
| `053300` | 5 | 4 | 3 | 3 | 4 | 3 | 4 | 26 | Stage2-Guarded at most / local 4B watch |

### Current calibrated profile stress test

The current calibrated profile already blocks pure price-only blowoff.  
The remaining C28 issue is **software/security label without contract-retention conversion**:

```text
C28 low-MAE enterprise software path:
  contract/deployment relevance
  + moderate persistent MFE
  + very controlled MAE
  + URL-repaired recurring revenue, retention, deployment, and margin bridge
  => Stage2-Guarded / Yellow, possible Green after proof

C28 high-MFE later-high-MAE SaaS path:
  SaaS/AI procurement relevance
  + 30D/90D MFE is real
  + MAE_180D <= -30%
  + evidence remains source_proxy_only
  => Stage2-Guarded at most, local 4B watch, no Green

C28 digital ID / certificate event path:
  security or identity policy/event relevance exists
  + MFE_90D < +15%
  + MAE_90D <= -15% or MAE_180D <= -25%
  + no contract revenue bridge
  => block Green and usually block Stage2

C28 delayed-MFE after early drawdown:
  delayed MFE appears after first-window failure
  + MAE_30D <= -15%
  + contract evidence unrepaired
  => delayed MFE does not override early high MAE
```

`307950` prevents overblocking.  
`058970` shows why real software MFE still needs later-MAE and retention guards.  
`042510` and `053300` show why digital ID/security labels should not be promoted without contract revenue and margin evidence.

---

## 9. Aggregate metrics

```json
{
  "row_type": "aggregate",
  "research_id": "R8L76_C28_SOFTWARE_SECURITY_CONTRACT_ROUTER",
  "round": "R8",
  "loop": 76,
  "large_sector_id": "L8_PLATFORM_CONTENT_SW_SECURITY",
  "canonical_archetype_id": "C28_SOFTWARE_SECURITY_CONTRACT_RETENTION",
  "fine_archetype_id": "ENTERPRISE_SOFTWARE_DIGITAL_ID_SECURITY_CONTRACT_RETENTION_AND_WEAK_MFE_ROUTER",
  "case_count": 4,
  "calibration_usable_case_count": 4,
  "positive_guarded_case_count": 1,
  "counterexample_count": 3,
  "new_symbol_count": 4,
  "source_proxy_only_count": 4,
  "evidence_url_pending_count": 4,
  "avg_mfe_30d_pct": 15.03,
  "avg_mae_30d_pct": -9.56,
  "avg_mfe_90d_pct": 18.31,
  "avg_mae_90d_pct": -13.22,
  "avg_mfe_180d_pct": 22.19,
  "avg_mae_180d_pct": -21.45,
  "max_mfe_180d_pct": 28.24,
  "worst_mae_180d_pct": -36.3
}
```

---

## 10. 4B proximity split

```json
{
  "row_type": "4b_split",
  "research_id": "R8L76_C28_SOFTWARE_SECURITY_CONTRACT_ROUTER",
  "stage2_guarded_or_yellow_candidate": [
    {
      "symbol": "307950",
      "reason": "enterprise software path had +27.03% 180D MFE with only -2.44% MAE"
    }
  ],
  "stage2_guarded_or_local_4b_watch": [
    {
      "symbol": "058970",
      "reason": "SaaS/procurement AI path had +28.24% MFE, but 180D MAE reached -36.30%"
    },
    {
      "symbol": "053300",
      "reason": "delayed MFE appeared, but first 30D/90D had weak MFE and -19.44% MAE"
    }
  ],
  "blocked_stage2_or_local_4b_watch": [
    {
      "symbol": "042510",
      "reason": "digital ID/security event had only +13.82% MFE and -27.63% 180D MAE"
    }
  ],
  "full_4b_or_green_requires_non_price_evidence": [
    "contract renewal and retention",
    "ARR / recurring revenue / transaction revenue",
    "backlog and deployment schedule",
    "customer concentration and churn",
    "security subscription or digital-ID monetization",
    "gross margin and operating leverage"
  ]
}
```

---

## 11. Shadow rule candidate

```yaml
row_type: canonical_archetype_rule_candidate
canonical_archetype_id: C28_SOFTWARE_SECURITY_CONTRACT_RETENTION
fine_archetype_id: ENTERPRISE_SOFTWARE_DIGITAL_ID_SECURITY_CONTRACT_RETENTION_AND_WEAK_MFE_ROUTER
rule_name: C28_enterprise_software_digital_id_security_contract_retention_and_weak_mfe_router
production_scoring_changed: false
shadow_weight_only: true
```

### Proposed routing logic

```text
For C28 enterprise software / security / digital ID cases:

Tier A: verified enterprise software contract-retention winner
  Conditions:
    - contract retention, ARR/recurring revenue, deployment, and margin evidence are URL-repaired
    - MFE_90D >= +20%
    - MAE_90D > -8%
  Routing:
    - Stage2-Guarded allowed
    - Stage3-Yellow allowed after evidence repair
    - Green only after contract-retention / revenue / margin bridge is verified

Tier B: high-MFE later-high-MAE SaaS/software case
  Conditions:
    - MFE_90D >= +20%
    - MAE_180D <= -30%
    - evidence_url_pending or source_proxy_only remains true
  Routing:
    - Stage2-Guarded at most
    - local 4B/high-MAE watch
    - no Yellow/Green

Tier C: weak-MFE security/digital identity event
  Conditions:
    - MFE_90D < +15%
    - MAE_90D <= -15% or MAE_180D <= -25%
    - no repaired contract revenue bridge
  Routing:
    - block Green
    - block Stage2 or local 4B watch

Tier D: delayed-MFE after early drawdown
  Conditions:
    - MFE_30D < +10%
    - MAE_30D <= -15%
    - delayed MFE appears only later
    - evidence remains source_proxy_only
  Routing:
    - Stage2-Guarded at most
    - no Yellow/Green from delayed MFE alone
```

### Suggested shadow delta

```json
{
  "row_type": "shadow_weight",
  "axis": "c28_enterprise_software_digital_id_security_contract_retention_and_weak_mfe_router",
  "scope": "canonical_archetype_id:C28_SOFTWARE_SECURITY_CONTRACT_RETENTION",
  "proposal": {
    "source_proxy_only_green_allowed": false,
    "contract_retention_recurring_revenue_margin_bridge_required_for_green": true,
    "verified_contract_retention_mfe90_threshold_pct": 20.0,
    "verified_contract_retention_mae90_min_pct": -8.0,
    "high_mfe_later_mae_mfe90_threshold_pct": 20.0,
    "high_mfe_later_mae180_threshold_pct": -30.0,
    "weak_mfe_security_threshold_90d_pct": 15.0,
    "weak_mfe_security_mae90_threshold_pct": -15.0,
    "weak_mfe_security_mae180_threshold_pct": -25.0,
    "early_drawdown_mae30_threshold_pct": -15.0,
    "delayed_mfe_does_not_override_early_drawdown_without_contract_bridge": true,
    "positive_weight_blocked_until_url_repair": true
  },
  "confidence": "medium_low_until_url_repair",
  "apply_now": false,
  "reason": "One low-MAE enterprise software holdout and three SaaS/security/digital-ID weak-MFE or high-MAE cases show that C28 should require URL-repaired contract retention, recurring revenue, deployment, security subscription/transaction monetization, and margin evidence before Yellow/Green."
}
```

---

## 12. Residual contribution summary

```json
{
  "row_type": "residual_contribution",
  "research_id": "R8L76_C28_SOFTWARE_SECURITY_CONTRACT_ROUTER",
  "large_sector_id": "L8_PLATFORM_CONTENT_SW_SECURITY",
  "canonical_archetype_id": "C28_SOFTWARE_SECURITY_CONTRACT_RETENTION",
  "contribution": "Adds four non-top-covered C28 enterprise software / digital ID / security contract-retention cases and separates a low-MAE enterprise software holdout from high-MFE later-high-MAE SaaS and weak-MFE digital-ID/security failures. C28 Yellow/Green should require URL-repaired contract retention, recurring/transaction revenue, deployment, customer renewal/churn, security subscription or identity monetization, and margin evidence.",
  "positive_guarded_case_added": 1,
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
  "data_quality_blocker": "All four non-price software/security triggers require URL-level repair before positive weight promotion.",
  "guardrail_added": "C28 source_proxy_only cases with MFE_90D < +15% and MAE_90D <= -15% or MAE_180D <= -25% should block Green and usually block Stage2; high-MFE software cases with MAE_180D <= -30% should cap at Stage2-Guarded until contract-retention evidence is repaired."
}
```

One-line contribution:

```text
This loop adds 4 new independent cases, 3 counterexamples, and 3 residual errors for R8/L8_PLATFORM_CONTENT_SW_SECURITY/C28_SOFTWARE_SECURITY_CONTRACT_RETENTION.
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
    307950: false
    058970: false
    042510: false
    053300: false
  evidence_url_pending:
    307950: true
    058970: true
    042510: true
    053300: true
  source_proxy_only:
    307950: true
    058970: true
    042510: true
    053300: true
  special_handling:
    042510:
      corporate_action_candidate_date_after_window: "2025-05-07"
      note: "The selected 2024-08-28 entry plus 180D window ends before this corporate-action candidate."
```

Limitations:

```text
- Price path is validated against Stock-Web tradable OHLC rows.
- Non-price evidence is not URL-repaired in this run.
- Therefore this artifact is useful for C28 enterprise software / security / digital ID residual shape and weak-MFE/high-MAE guardrail design, but should not promote positive weights until filings, IR, contract disclosures, procurement/customer data, or reports verify contract retention, ARR/recurring revenue, deployment, churn, digital-ID monetization, security subscription conversion, margin, and cash-flow conversion.
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
2. Preserve R8 / loop 76 metadata.
3. Add the cases to C28_SOFTWARE_SECURITY_CONTRACT_RETENTION only if parser validation passes.
4. Treat all four non-price triggers as evidence_url_pending=true and source_proxy_only=true until URL-level evidence is repaired.
5. Do not use these rows for positive weight promotion until filings/IR/contract-disclosure/procurement-customer/report data verifies contract retention, ARR/recurring revenue, deployment, churn, digital-ID monetization, security subscription conversion, margin, and cash-flow conversion.
6. Add a shadow-only rule candidate named C28_enterprise_software_digital_id_security_contract_retention_and_weak_mfe_router.
7. Do not loosen Stage3-Green.
8. Add C28-specific guards:
   - source_proxy_only -> no Green
   - Green requires repaired contract retention / recurring revenue / deployment / margin bridge
   - MFE_90D >= +20% and MAE_90D > -8% may remain Stage2-Guarded / Yellow watch after evidence repair
   - MFE_90D >= +20% but MAE_180D <= -30% -> Stage2-Guarded at most / local 4B watch
   - MFE_90D < +15% and MAE_90D <= -15% or MAE_180D <= -25% -> block Green and usually block Stage2
   - MFE_30D < +10% and MAE_30D <= -15% -> delayed MFE does not override early drawdown without contract bridge
9. Keep production scoring unchanged unless later batch promotion logic independently marks this axis safe.
```

---

## 15. Next round state

```text
completed_round = R8
completed_loop = 76
next_round = R9
next_loop = 76
next_large_sector_hint = L3_BATTERY_EV_GREEN_MOBILITY or L9_CONSTRUCTION_REALESTATE_HOUSING
round_schedule_status = valid
round_sector_consistency = pass
```
