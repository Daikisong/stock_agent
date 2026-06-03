# E2R Stock-Web v12 Residual Research — R12 Loop 76

```yaml
research_session: post_calibrated_sector_archetype_residual_research
mode: historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12
completed_round: R12
completed_loop: 76
next_round: R13
next_loop: 76
large_sector_id: L10_POLICY_EVENT_CROSS_REDTEAM_MISC
canonical_archetype_id: C31_POLICY_SUBSIDY_LEGISLATION_EVENT
fine_archetype_id: MEDICAL_SCHOOL_QUOTA_PRIVATE_EDUCATION_POLICY_THEME_AND_HIGH_MAE_ROUTER
output_file: e2r_stock_web_v12_residual_round_R12_loop_76_L10_POLICY_EVENT_CROSS_REDTEAM_MISC_C31_POLICY_SUBSIDY_LEGISLATION_EVENT_research.md
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
completed_round = R11
completed_loop  = 76
large_sector_id = L10_POLICY_EVENT_CROSS_REDTEAM_MISC
canonical_archetype_id = C31_POLICY_SUBSIDY_LEGISLATION_EVENT
fine_archetype_id = KOREA_VALUEUP_HOLDING_COMPANY_CAPITAL_ALLOCATION_AND_WEAK_MFE_ROUTER
```

Therefore:

```text
scheduled_round = R12
scheduled_loop  = 76
```

R12 permits:

```text
large_sector_id = L10_POLICY_EVENT_CROSS_REDTEAM_MISC
or
under-covered service/agri/event sector
```

This run selects a policy-event / service fine subtype:

```text
large_sector_id = L10_POLICY_EVENT_CROSS_REDTEAM_MISC
canonical_archetype_id = C31_POLICY_SUBSIDY_LEGISLATION_EVENT
fine_archetype_id = MEDICAL_SCHOOL_QUOTA_PRIVATE_EDUCATION_POLICY_THEME_AND_HIGH_MAE_ROUTER
```

This is a valid R12/L10 pairing.

---

## 1. Why this R12/C31 run

The no-repeat ledger shows C31 is already wide, but it is deliberately broad and still benefits from fine-subtype red-team splits:

```text
C31_POLICY_SUBSIDY_LEGISLATION_EVENT:
  rows: 206
  symbols: 77
  date_range: 2020-01-20~2024-07-31
  good/bad S2: 41/38
  4B/4C: 43/0
  URL/proxy: 39/40
  top covered symbols: UNKNOWN_SYMBOL(15), 004090(8), 036460(8), 112610(7), 005860(6), 008970(6)
```

This file avoids the top-covered C31 names and avoids the immediately previous value-up fine subtypes:

```text
- defensive-yield / telecom / tobacco value-up
- low-birth / childcare policy
- holding-company / capital-allocation value-up
```

Selected fine subtype:

```text
medical school quota / private education / edtech policy theme
```

Selected symbols:

```text
100220 비상교육
057030 YBM넷
133750 메가엠디
289010 아이스크림에듀
```

Research question:

```text
Can C31 separate an education-policy theme that produces real MFE from private-education and edtech policy labels where policy relevance exists but student enrollment, paid conversion, course revenue, subscription retention, and margin conversion are not repaired?
```

C31 policy themes are like a school bell. Everyone hears the bell at the same time, but only some classrooms actually fill. Stage2 should ask whether the policy bell becomes students, paid enrollments, content sales, subscription retention, and operating leverage. Without that conversion, the first crowd in the hallway can turn into a long empty corridor.

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
| `100220` | 비상교육 | active_like / KOSPI | no 2024 overlap; latest listed candidate 2011-04-18 | true |
| `057030` | YBM넷 | active_like / KOSDAQ | no 2024 overlap; latest listed candidate 2010-01-25 | true |
| `133750` | 메가엠디 | active_like / KOSDAQ | none listed | true |
| `289010` | 아이스크림에듀 | active_like / KOSDAQ | none listed | true |

Profile caveat:

```text
Stock-Web OHLC is raw/unadjusted marcap data.
These cases are calibration-safe for the selected 2024 30D/90D/180D windows because no listed corporate-action candidate overlaps each entry~D+180 test window.
```

---

## 3. Event family and trigger discipline

### Event family

```text
event_family = medical school quota / private education / online education policy theme burst
trigger_date = 2024-02-06
entry_rule = next_tradable_open_to_avoid_same_day_lookahead
entry_date = 2024-02-07
canonical_archetype_id = C31_POLICY_SUBSIDY_LEGISLATION_EVENT
fine_archetype_id = MEDICAL_SCHOOL_QUOTA_PRIVATE_EDUCATION_POLICY_THEME_AND_HIGH_MAE_ROUTER
```

This artifact intentionally marks non-price evidence as conservative:

```text
evidence_url_pending = true
source_proxy_only = true
```

Reason:

```text
The Stock-Web price path is fully validated, but company-level policy execution, student enrollment, paid-course conversion, B2B/B2C channel demand, online platform retention, content sales, subscription revenue, gross margin, and operating leverage evidence still require later URL repair through filings, IR, policy documents, channel data, or sell-side reports before production weight promotion.
```

---

## 4. No-repeat and novelty check

Hard duplicate key:

```text
canonical_archetype_id + symbol + trigger_type + entry_date
```

Targeted repository searches before writing:

```text
100220 + C31_POLICY_SUBSIDY_LEGISLATION_EVENT -> no direct match found
057030 + C31_POLICY_SUBSIDY_LEGISLATION_EVENT -> no direct match found
133750 + C31_POLICY_SUBSIDY_LEGISLATION_EVENT -> no direct match found
289010 + C31_POLICY_SUBSIDY_LEGISLATION_EVENT -> no direct match found
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
| `R12L76_C31_100220_20240207` | `100220` 비상교육 | education policy / medical-school quota theme high-MFE later drawdown | positive-guarded holdout |
| `R12L76_C31_057030_20240207` | `057030` YBM넷 | online education policy theme initial-MFE later drawdown | first-window-MFE later-MAE counterexample |
| `R12L76_C31_133750_20240207` | `133750` 메가엠디 | medical education policy theme moderate-MFE extreme-MAE | high-MAE counterexample |
| `R12L76_C31_289010_20240207` | `289010` 아이스크림에듀 | edtech policy theme initial-MFE later-high-MAE | later-MAE counterexample |

The intended residual:

```text
C31 should separate:
1. education-policy themes where MFE is large enough to preserve Stage2-Guarded;
2. online/private education names where first-window MFE exists but later MAE blocks Yellow/Green;
3. medical education labels where MFE is only moderate and later MAE becomes extreme;
4. edtech labels where the policy theme fails without enrollment/subscription/margin evidence.
```

---

## 6. Stock-Web OHLC and backtest

### 6.1 `100220` 비상교육 — education policy / medical-school quota high-MFE later-drawdown holdout

Trigger:

```text
trigger_date = 2024-02-06
trigger_type = Stage2-Actionable-Guarded
trigger_family = education_policy_medical_quota_private_education_theme_high_mfe_later_drawdown
entry_date = 2024-02-07
entry_price = 5100.0
entry_price_type = next_tradable_open_after_medical_school_quota_private_education_policy_burst
```

Relevant Stock-Web rows:

```csv
d,o,h,l,c,v,a,mc,s,m
2024-02-06,5520.0,6450.0,5030.0,5060.0,8387452.0,50201733680.0,65763509460.0,12996741,KOSPI
2024-02-07,5100.0,5110.0,4835.0,4840.0,408457.0,2012305240.0,62904226440.0,12996741,KOSPI
2024-02-08,4780.0,4840.0,4580.0,4580.0,332071.0,1556528055.0,59525073780.0,12996741,KOSPI
2024-02-20,5270.0,7000.0,5180.0,7000.0,16263149.0,105353263580.0,90977187000.0,12996741,KOSPI
2024-02-21,7400.0,8420.0,7090.0,7360.0,17513420.0,138281669640.0,95656013760.0,12996741,KOSPI
2024-03-08,5790.0,5900.0,5630.0,5720.0,190235.0,1092031040.0,74341358520.0,12996741,KOSPI
2024-04-16,4920.0,5000.0,4690.0,4715.0,101092.0,485802530.0,61279633815.0,12996741,KOSPI
2024-08-05,4555.0,4565.0,3990.0,4125.0,116373.0,493826685.0,53611556625.0,12996741,KOSPI
```

Backtest:

| window | peak/high | peak date | trough/low | trough date | MFE | MAE |
|---|---:|---|---:|---|---:|---:|
| 30 calendar days | 8420 | 2024-02-21 | 4580 | 2024-02-08 | +65.10% | -10.20% |
| 90 calendar days | 8420 | 2024-02-21 | 4580 | 2024-02-08 | +65.10% | -10.20% |
| 180 calendar days | 8420 | 2024-02-21 | 3990 | 2024-08-05 | +65.10% | -21.76% |

Interpretation:

```text
100220 is the C31 education-policy positive-guarded holdout.
The policy theme produced real MFE, but the 180D drawdown shows why this cannot be Green while evidence remains source-proxy-only.
Yellow/Green should require URL-repaired student enrollment, paid-course conversion, policy execution, and margin evidence.
```

### 6.2 `057030` YBM넷 — online education policy theme initial-MFE / later-MAE branch

Trigger:

```text
trigger_date = 2024-02-06
trigger_type = Stage2-Actionable-Guarded
trigger_family = online_education_policy_theme_initial_mfe_later_drawdown
entry_date = 2024-02-07
entry_price = 4645.0
entry_price_type = next_tradable_open_after_private_education_policy_theme_burst
```

Relevant Stock-Web rows:

```csv
d,o,h,l,c,v,a,mc,s,m
2024-02-06,5060.0,5090.0,4645.0,4645.0,637402.0,3111828110.0,75772477565.0,16312697,KOSDAQ
2024-02-07,4645.0,4690.0,4580.0,4645.0,101323.0,469399630.0,75772477565.0,16312697,KOSDAQ
2024-02-16,4525.0,4610.0,4435.0,4610.0,154861.0,700319830.0,75201533170.0,16312697,KOSDAQ
2024-02-29,4525.0,5580.0,4460.0,4905.0,8068188.0,41946005145.0,80013778785.0,16312697,KOSDAQ
2024-03-14,4605.0,4670.0,4300.0,4400.0,284356.0,1254500505.0,71775866800.0,16312697,KOSDAQ
2024-04-05,4010.0,4025.0,3910.0,4000.0,44378.0,175055340.0,65250788000.0,16312697,KOSDAQ
2024-08-05,3445.0,3530.0,2960.0,3100.0,151208.0,486065565.0,50569360700.0,16312697,KOSDAQ
```

Backtest:

| window | peak/high | peak date | trough/low | trough date | MFE | MAE |
|---|---:|---|---:|---|---:|---:|
| 30 calendar days | 5580 | 2024-02-29 | 4435 | 2024-02-16 | +20.13% | -4.52% |
| 90 calendar days | 5580 | 2024-02-29 | 3910 | 2024-04-05 | +20.13% | -15.82% |
| 180 calendar days | 5580 | 2024-02-29 | 2960 | 2024-08-05 | +20.13% | -36.28% |

Interpretation:

```text
057030 is the first-window-MFE / later-high-MAE counterexample.
The initial policy theme was tradable, but 180D MAE crossed a hard drawdown zone.
C31 should cap this at Stage2-Guarded or local 4B watch until enrollment/platform revenue and margin evidence is repaired.
```

### 6.3 `133750` 메가엠디 — medical education policy theme moderate-MFE / extreme-MAE path

Trigger:

```text
trigger_date = 2024-02-06
trigger_type = Stage2-FalsePositive-Candidate
trigger_family = medical_education_policy_theme_moderate_mfe_extreme_mae
entry_date = 2024-02-07
entry_price = 3000.0
entry_price_type = next_tradable_open_after_medical_education_policy_theme_burst
```

Relevant Stock-Web rows:

```csv
d,o,h,l,c,v,a,mc,s,m
2024-02-06,3515.0,3670.0,2975.0,2995.0,22166019.0,75820537405.0,70104195615.0,23407077,KOSDAQ
2024-02-07,3000.0,3095.0,2850.0,2850.0,1956714.0,5764157155.0,66710169450.0,23407077,KOSDAQ
2024-02-14,2690.0,3130.0,2670.0,2895.0,5608190.0,16407991630.0,67763487915.0,23407077,KOSDAQ
2024-03-05,3315.0,3555.0,3205.0,3240.0,7937414.0,26751332380.0,75838929480.0,23407077,KOSDAQ
2024-04-19,2315.0,2315.0,2205.0,2280.0,181112.0,408062175.0,53368135560.0,23407077,KOSDAQ
2024-08-05,2005.0,2035.0,1647.0,1740.0,306837.0,573536733.0,40728313980.0,23407077,KOSDAQ
```

Backtest:

| window | peak/high | peak date | trough/low | trough date | MFE | MAE |
|---|---:|---|---:|---|---:|---:|
| 30 calendar days | 3555 | 2024-03-05 | 2670 | 2024-02-14 | +18.50% | -11.00% |
| 90 calendar days | 3555 | 2024-03-05 | 2205 | 2024-04-19 | +18.50% | -26.50% |
| 180 calendar days | 3555 | 2024-03-05 | 1647 | 2024-08-05 | +18.50% | -45.10% |

Interpretation:

```text
133750 is the hard medical-education policy-theme counterexample.
The event label created only moderate MFE, then 90D/180D drawdown became severe.
This should block Stage2 or route to 4B/4C watch unless a later independent trigger repairs policy-to-revenue conversion evidence.
```

### 6.4 `289010` 아이스크림에듀 — edtech policy theme initial-MFE / later-high-MAE path

Trigger:

```text
trigger_date = 2024-02-06
trigger_type = Stage2-FalsePositive-Candidate
trigger_family = edtech_policy_theme_initial_mfe_later_high_mae
entry_date = 2024-02-07
entry_price = 3845.0
entry_price_type = next_tradable_open_after_edtech_policy_theme_burst
```

Relevant Stock-Web rows:

```csv
d,o,h,l,c,v,a,mc,s,m
2024-02-06,4145.0,4695.0,3860.0,3890.0,14231024.0,62741098080.0,50041103930.0,12864037,KOSDAQ
2024-02-07,3845.0,3890.0,3740.0,3865.0,477797.0,1822762155.0,49719503005.0,12864037,KOSDAQ
2024-02-29,3875.0,4350.0,3855.0,4060.0,4361073.0,18043049490.0,52227990220.0,12864037,KOSDAQ
2024-03-04,4465.0,4600.0,4150.0,4150.0,3044849.0,13296281650.0,53385753550.0,12864037,KOSDAQ
2024-04-11,3570.0,3635.0,3550.0,3585.0,21833.0,78181115.0,46117572645.0,12864037,KOSDAQ
2024-08-05,2930.0,2930.0,2385.0,2530.0,66989.0,182569195.0,32546013610.0,12864037,KOSDAQ
```

Backtest:

| window | peak/high | peak date | trough/low | trough date | MFE | MAE |
|---|---:|---|---:|---|---:|---:|
| 30 calendar days | 4600 | 2024-03-04 | 3740 | 2024-02-07 | +19.64% | -2.73% |
| 90 calendar days | 4600 | 2024-03-04 | 3550 | 2024-04-11 | +19.64% | -7.67% |
| 180 calendar days | 4600 | 2024-03-04 | 2385 | 2024-08-05 | +19.64% | -37.97% |

Interpretation:

```text
289010 is the edtech first-window-MFE / later-high-MAE branch.
The first window looked controlled, but 180D MAE showed the policy theme did not convert into durable subscription/revenue economics.
This should cap at Stage2-Guarded or local 4B watch until subscription retention, B2B/B2C demand, and margin evidence is repaired.
```

---

## 7. Machine-readable trigger JSONL

```jsonl
{"row_type":"trigger","research_id":"R12L76_C31_EDUCATION_MEDSCHOOL_POLICY_ROUTER","round":"R12","loop":76,"large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"C31_POLICY_SUBSIDY_LEGISLATION_EVENT","fine_archetype_id":"MEDICAL_SCHOOL_QUOTA_PRIVATE_EDUCATION_POLICY_THEME_AND_HIGH_MAE_ROUTER","symbol":"100220","name":"비상교육","trigger_type":"Stage2-Actionable-Guarded","trigger_family":"education_policy_medical_quota_private_education_theme_high_mfe_later_drawdown","trigger_date":"2024-02-06","entry_date":"2024-02-07","entry_price":5100.0,"entry_price_type":"next_tradable_open_after_medical_school_quota_private_education_policy_burst","price_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","mfe_30d_pct":65.1,"mae_30d_pct":-10.2,"mfe_90d_pct":65.1,"mae_90d_pct":-10.2,"mfe_180d_pct":65.1,"mae_180d_pct":-21.76,"peak_price_180d":8420.0,"peak_date_180d":"2024-02-21","trough_price_180d":3990.0,"trough_date_180d":"2024-08-05","calibration_usable":true,"case_polarity":"positive_guarded_high_mfe_later_drawdown","evidence_url_pending":true,"source_proxy_only":true,"non_price_evidence_strength":"medium_low_pending_url_repair","price_only_blowoff":false,"expected_stage_current_profile":"Stage2-Guarded_to_Yellow_only_if_policy_execution_enrollment_revenue_margin_bridge_repaired","residual_error_type":"education_policy_theme_had_high_mfe_but_later_drawdown_requires_url_repaired_policy_execution_enrollment_revenue_margin_bridge_before_green"}
{"row_type":"trigger","research_id":"R12L76_C31_EDUCATION_MEDSCHOOL_POLICY_ROUTER","round":"R12","loop":76,"large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"C31_POLICY_SUBSIDY_LEGISLATION_EVENT","fine_archetype_id":"MEDICAL_SCHOOL_QUOTA_PRIVATE_EDUCATION_POLICY_THEME_AND_HIGH_MAE_ROUTER","symbol":"057030","name":"YBM넷","trigger_type":"Stage2-Actionable-Guarded","trigger_family":"online_education_policy_theme_initial_mfe_later_drawdown","trigger_date":"2024-02-06","entry_date":"2024-02-07","entry_price":4645.0,"entry_price_type":"next_tradable_open_after_private_education_policy_theme_burst","price_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","mfe_30d_pct":20.13,"mae_30d_pct":-4.52,"mfe_90d_pct":20.13,"mae_90d_pct":-15.82,"mfe_180d_pct":20.13,"mae_180d_pct":-36.28,"peak_price_180d":5580.0,"peak_date_180d":"2024-02-29","trough_price_180d":2960.0,"trough_date_180d":"2024-08-05","calibration_usable":true,"case_polarity":"counterexample_initial_mfe_later_high_mae","evidence_url_pending":true,"source_proxy_only":true,"non_price_evidence_strength":"low_pending_url_repair","price_only_blowoff":false,"expected_stage_current_profile":"Stage2-Guarded_or_local_4B_watch_until_enrollment_platform_revenue_bridge_repaired","residual_error_type":"online_education_policy_theme_had_initial_mfe_but_180d_high_mae_blocks_yellow_green_without_revenue_conversion_bridge"}
{"row_type":"trigger","research_id":"R12L76_C31_EDUCATION_MEDSCHOOL_POLICY_ROUTER","round":"R12","loop":76,"large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"C31_POLICY_SUBSIDY_LEGISLATION_EVENT","fine_archetype_id":"MEDICAL_SCHOOL_QUOTA_PRIVATE_EDUCATION_POLICY_THEME_AND_HIGH_MAE_ROUTER","symbol":"133750","name":"메가엠디","trigger_type":"Stage2-FalsePositive-Candidate","trigger_family":"medical_education_policy_theme_moderate_mfe_extreme_mae","trigger_date":"2024-02-06","entry_date":"2024-02-07","entry_price":3000.0,"entry_price_type":"next_tradable_open_after_medical_education_policy_theme_burst","price_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","mfe_30d_pct":18.5,"mae_30d_pct":-11.0,"mfe_90d_pct":18.5,"mae_90d_pct":-26.5,"mfe_180d_pct":18.5,"mae_180d_pct":-45.1,"peak_price_180d":3555.0,"peak_date_180d":"2024-03-05","trough_price_180d":1647.0,"trough_date_180d":"2024-08-05","calibration_usable":true,"case_polarity":"counterexample_moderate_mfe_extreme_mae","evidence_url_pending":true,"source_proxy_only":true,"non_price_evidence_strength":"low_pending_url_repair","price_only_blowoff":false,"expected_stage_current_profile":"blocked_Stage2_or_4B_4C_high_MAE_watch_until_medical_education_revenue_bridge_repaired","residual_error_type":"medical_education_policy_theme_had_only_moderate_mfe_and_extreme_mae_without_policy_to_revenue_bridge"}
{"row_type":"trigger","research_id":"R12L76_C31_EDUCATION_MEDSCHOOL_POLICY_ROUTER","round":"R12","loop":76,"large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"C31_POLICY_SUBSIDY_LEGISLATION_EVENT","fine_archetype_id":"MEDICAL_SCHOOL_QUOTA_PRIVATE_EDUCATION_POLICY_THEME_AND_HIGH_MAE_ROUTER","symbol":"289010","name":"아이스크림에듀","trigger_type":"Stage2-FalsePositive-Candidate","trigger_family":"edtech_policy_theme_initial_mfe_later_high_mae","trigger_date":"2024-02-06","entry_date":"2024-02-07","entry_price":3845.0,"entry_price_type":"next_tradable_open_after_edtech_policy_theme_burst","price_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","mfe_30d_pct":19.64,"mae_30d_pct":-2.73,"mfe_90d_pct":19.64,"mae_90d_pct":-7.67,"mfe_180d_pct":19.64,"mae_180d_pct":-37.97,"peak_price_180d":4600.0,"peak_date_180d":"2024-03-04","trough_price_180d":2385.0,"trough_date_180d":"2024-08-05","calibration_usable":true,"case_polarity":"counterexample_first_window_mfe_later_high_mae","evidence_url_pending":true,"source_proxy_only":true,"non_price_evidence_strength":"low_pending_url_repair","price_only_blowoff":false,"expected_stage_current_profile":"Stage2-Guarded_or_local_4B_watch_until_edtech_subscription_revenue_margin_bridge_repaired","residual_error_type":"edtech_policy_theme_had_first_window_mfe_but_180d_high_mae_without_subscription_revenue_or_margin_bridge"}
```

---

## 8. Score simulation and raw component breakdown

This is shadow-only and does not change production scoring.

| symbol | policy relevance | enrollment / paid conversion | platform / content demand | revenue bridge | market mispricing | margin / operating leverage | information confidence | shadow total | intended route |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| `100220` | 12 | 6 | 7 | 6 | 12 | 5 | 5 | 53 | Stage2-Guarded / Yellow only after evidence repair |
| `057030` | 10 | 4 | 5 | 4 | 6 | 3 | 5 | 37 | Stage2-Guarded or local 4B watch |
| `133750` | 10 | 3 | 3 | 3 | 4 | 2 | 4 | 29 | blocked Stage2 / 4B-4C high-MAE watch |
| `289010` | 9 | 3 | 4 | 3 | 5 | 2 | 4 | 30 | Stage2-Guarded at most / local 4B watch |

### Current calibrated profile stress test

The current calibrated profile already blocks pure price-only blowoff.  
The remaining C31 issue is **education policy relevance without enrollment/revenue conversion**:

```text
C31 high-MFE education policy path:
  policy relevance
  + MFE_30D >= +50%
  + later MAE_180D <= -20%
  + evidence remains source_proxy_only
  => Stage2-Guarded; Yellow only after policy/enrollment/revenue bridge repair

C31 first-window-MFE later-MAE path:
  education theme MFE appears
  + MAE_180D <= -35%
  + paid conversion / revenue bridge missing
  => Stage2-Guarded at most, local 4B watch, no Green

C31 moderate-MFE extreme-MAE path:
  MFE_30D < +20%
  + MAE_90D <= -25% or MAE_180D <= -40%
  + no policy-to-revenue evidence
  => block Stage2 or route to 4B/4C high-MAE watch

C31 edtech subscription path:
  first-window MFE exists
  + 180D drawdown becomes high
  + subscription / platform retention evidence missing
  => no Yellow/Green
```

`100220` prevents overblocking.  
`057030`, `133750`, and `289010` show why education-policy labels should not be promoted without enrollment, paid conversion, and margin evidence.

---

## 9. Aggregate metrics

```json
{
  "row_type": "aggregate",
  "research_id": "R12L76_C31_EDUCATION_MEDSCHOOL_POLICY_ROUTER",
  "round": "R12",
  "loop": 76,
  "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC",
  "canonical_archetype_id": "C31_POLICY_SUBSIDY_LEGISLATION_EVENT",
  "fine_archetype_id": "MEDICAL_SCHOOL_QUOTA_PRIVATE_EDUCATION_POLICY_THEME_AND_HIGH_MAE_ROUTER",
  "case_count": 4,
  "calibration_usable_case_count": 4,
  "positive_guarded_case_count": 1,
  "counterexample_count": 3,
  "new_symbol_count": 4,
  "source_proxy_only_count": 4,
  "evidence_url_pending_count": 4,
  "avg_mfe_30d_pct": 30.84,
  "avg_mae_30d_pct": -7.11,
  "avg_mfe_90d_pct": 30.84,
  "avg_mae_90d_pct": -15.05,
  "avg_mfe_180d_pct": 30.84,
  "avg_mae_180d_pct": -35.28,
  "max_mfe_180d_pct": 65.1,
  "worst_mae_180d_pct": -45.1
}
```

---

## 10. 4B proximity split

```json
{
  "row_type": "4b_split",
  "research_id": "R12L76_C31_EDUCATION_MEDSCHOOL_POLICY_ROUTER",
  "stage2_guarded_or_yellow_candidate": [
    {
      "symbol": "100220",
      "reason": "education policy path had +65.10% MFE, but 180D MAE reached -21.76%; requires policy/enrollment/revenue evidence repair"
    }
  ],
  "stage2_guarded_or_local_4b_watch": [
    {
      "symbol": "057030",
      "reason": "online education path had +20.13% first-window MFE but -36.28% 180D MAE"
    },
    {
      "symbol": "289010",
      "reason": "edtech policy path had +19.64% MFE but -37.97% 180D MAE"
    }
  ],
  "blocked_stage2_or_4c_watch": [
    {
      "symbol": "133750",
      "reason": "medical education policy path had only +18.50% MFE and -45.10% 180D MAE"
    }
  ],
  "full_4b_or_green_requires_non_price_evidence": [
    "actual policy execution and timing",
    "student enrollment / paid-course conversion",
    "B2B/B2C channel demand",
    "online platform retention and subscription revenue",
    "content sales and pricing",
    "gross margin and operating leverage conversion"
  ]
}
```

---

## 11. Shadow rule candidate

```yaml
row_type: canonical_archetype_rule_candidate
canonical_archetype_id: C31_POLICY_SUBSIDY_LEGISLATION_EVENT
fine_archetype_id: MEDICAL_SCHOOL_QUOTA_PRIVATE_EDUCATION_POLICY_THEME_AND_HIGH_MAE_ROUTER
rule_name: C31_medical_school_quota_private_education_policy_theme_and_high_mae_router
production_scoring_changed: false
shadow_weight_only: true
```

### Proposed routing logic

```text
For C31 medical-school quota / private education / edtech policy theme cases:

Tier A: high-MFE education policy holdout
  Conditions:
    - policy relevance is clear
    - MFE_30D >= +50%
    - evidence remains source_proxy_only
  Routing:
    - Stage2-Guarded allowed
    - Stage3-Yellow only after URL-repaired enrollment / paid conversion / revenue / margin bridge
    - no Green while evidence is pending

Tier B: first-window-MFE later-high-MAE education theme
  Conditions:
    - MFE_30D >= +15%
    - MAE_180D <= -35%
    - no repaired paid-conversion or subscription bridge
  Routing:
    - Stage2-Guarded at most
    - local 4B/high-MAE watch
    - no Yellow/Green

Tier C: moderate-MFE extreme-MAE education policy label
  Conditions:
    - MFE_30D < +20%
    - MAE_90D <= -25% or MAE_180D <= -40%
    - no policy-to-revenue bridge
  Routing:
    - block Stage2
    - route to 4B/4C high-MAE watch
```

### Suggested shadow delta

```json
{
  "row_type": "shadow_weight",
  "axis": "c31_medical_school_quota_private_education_policy_theme_and_high_mae_router",
  "scope": "canonical_archetype_id:C31_POLICY_SUBSIDY_LEGISLATION_EVENT",
  "proposal": {
    "source_proxy_only_green_allowed": false,
    "policy_relevance_alone_stage2_allowed": false,
    "education_policy_enrollment_revenue_margin_bridge_required_for_green": true,
    "high_mfe_education_policy_mfe30_threshold_pct": 50.0,
    "first_window_mfe_threshold_30d_pct": 15.0,
    "first_window_mfe_later_high_mae180_threshold_pct": -35.0,
    "moderate_mfe_threshold_30d_pct": 20.0,
    "moderate_mfe_mae90_threshold_pct": -25.0,
    "moderate_mfe_mae180_threshold_pct": -40.0,
    "positive_weight_blocked_until_url_repair": true
  },
  "confidence": "medium_low_until_url_repair",
  "apply_now": false,
  "reason": "One high-MFE education-policy holdout and three initial-MFE or moderate-MFE high-MAE failures show that C31 should not promote medical-school quota/private education policy relevance without URL-repaired enrollment, paid conversion, subscription, revenue, and margin evidence."
}
```

---

## 12. Residual contribution summary

```json
{
  "row_type": "residual_contribution",
  "research_id": "R12L76_C31_EDUCATION_MEDSCHOOL_POLICY_ROUTER",
  "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC",
  "canonical_archetype_id": "C31_POLICY_SUBSIDY_LEGISLATION_EVENT",
  "contribution": "Adds four non-top-covered C31 education / medical-school quota / private-education policy-event cases and separates one high-MFE education-policy holdout from online education, medical education, and edtech later-high-MAE failures. C31 Yellow/Green should require URL-repaired policy execution, enrollment, paid conversion, platform/subscription revenue, content demand, margin, and operating-leverage evidence.",
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
  "data_quality_blocker": "All four non-price education policy triggers require URL-level repair before positive weight promotion.",
  "guardrail_added": "C31 source_proxy_only education policy cases with MFE_30D >= +15% but MAE_180D <= -35% should cap at Stage2-Guarded; moderate-MFE education policy labels with MAE_90D <= -25% or MAE_180D <= -40% should block Stage2."
}
```

One-line contribution:

```text
This loop adds 4 new independent cases, 3 counterexamples, and 3 residual errors for R12/L10_POLICY_EVENT_CROSS_REDTEAM_MISC/C31_POLICY_SUBSIDY_LEGISLATION_EVENT.
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
    100220: false
    057030: false
    133750: false
    289010: false
  evidence_url_pending:
    100220: true
    057030: true
    133750: true
    289010: true
  source_proxy_only:
    100220: true
    057030: true
    133750: true
    289010: true
```

Limitations:

```text
- Price path is validated against Stock-Web tradable OHLC rows.
- Non-price evidence is not URL-repaired in this run.
- Therefore this artifact is useful for C31 education / medical-school quota / private-education policy residual shape and high-MAE guardrail design, but should not promote positive weights until filings, IR, policy documents, channel data, or reports verify policy execution, student enrollment, paid conversion, platform/subscription retention, revenue, and margin conversion.
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
2. Preserve R12 / loop 76 metadata.
3. Add the cases to C31_POLICY_SUBSIDY_LEGISLATION_EVENT only if parser validation passes.
4. Treat all four non-price triggers as evidence_url_pending=true and source_proxy_only=true until URL-level evidence is repaired.
5. Do not use these rows for positive weight promotion until filings/IR/policy-document/channel-data/report data verifies policy execution, student enrollment, paid-course conversion, B2B/B2C demand, platform/subscription retention, content revenue, gross margin, and operating leverage.
6. Add a shadow-only rule candidate named C31_medical_school_quota_private_education_policy_theme_and_high_mae_router.
7. Do not loosen Stage3-Green.
8. Add C31-specific guards:
   - source_proxy_only -> no Green
   - policy relevance alone -> no Stage2 promotion
   - Stage3-Yellow/Green requires company-specific education policy / enrollment / revenue / margin bridge
   - MFE_30D >= +50% may remain Stage2-Guarded until evidence repair
   - MFE_30D >= +15% and MAE_180D <= -35% -> Stage2-Guarded at most / local 4B watch
   - MFE_30D < +20% and MAE_90D <= -25% or MAE_180D <= -40% -> block Stage2 / 4B-4C watch
9. Keep production scoring unchanged unless later batch promotion logic independently marks this axis safe.
```

---

## 15. Next round state

```text
completed_round = R12
completed_loop = 76
next_round = R13
next_loop = 76
next_large_sector_hint = L10_POLICY_EVENT_CROSS_REDTEAM_MISC
next_allowed_scope = R13_CROSS_ARCHETYPE_STAGE2_FALSE_POSITIVE_REVIEW or R13_CROSS_ARCHETYPE_4B_4C_REDTEAM or R13_CROSS_ARCHETYPE_ACCOUNTING_TRUST_PRICE_VALIDATION or R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL
round_schedule_status = valid
round_sector_consistency = pass
```
