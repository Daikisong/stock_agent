# E2R Stock-Web v12 Residual Research — R11 Loop 75

```yaml
research_session: post_calibrated_sector_archetype_residual_research
mode: historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12
completed_round: R11
completed_loop: 75
next_round: R12
next_loop: 75
large_sector_id: L10_POLICY_EVENT_CROSS_REDTEAM_MISC
canonical_archetype_id: C31_POLICY_SUBSIDY_LEGISLATION_EVENT
fine_archetype_id: KOREA_VALUEUP_DEFENSIVE_YIELD_TELECOM_TOBACCO_CAPITAL_RETURN_AND_WEAK_MFE_ROUTER
output_file: e2r_stock_web_v12_residual_round_R11_loop_75_L10_POLICY_EVENT_CROSS_REDTEAM_MISC_C31_POLICY_SUBSIDY_LEGISLATION_EVENT_research.md
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
completed_round = R10
completed_loop  = 75
large_sector_id = L9_CONSTRUCTION_REALESTATE_HOUSING
canonical_archetype_id = C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK
```

Therefore:

```text
scheduled_round = R11
scheduled_loop  = 75
```

R11 permits:

```text
large_sector_id = L10_POLICY_EVENT_CROSS_REDTEAM_MISC
or
large_sector_id = L1_INDUSTRIALS_INFRA_DEFENSE_GRID when the case is defense/policy-linked
```

This run selects:

```text
large_sector_id = L10_POLICY_EVENT_CROSS_REDTEAM_MISC
canonical_archetype_id = C31_POLICY_SUBSIDY_LEGISLATION_EVENT
fine_archetype_id = KOREA_VALUEUP_DEFENSIVE_YIELD_TELECOM_TOBACCO_CAPITAL_RETURN_AND_WEAK_MFE_ROUTER
```

This is a valid R11/L10 pairing.

---

## 1. Why this R11/C31 run

The no-repeat ledger shows C31 is broad and policy-event-heavy:

```text
C31_POLICY_SUBSIDY_LEGISLATION_EVENT:
  rows: 155
  symbols: 63
  date_range: 2020-01-20~2024-07-31
  good/bad S2: 38/32
  4B/4C: 35/0
  URL/proxy: 0/7
  top covered symbols: UNKNOWN_SYMBOL(15), 036460(8), 112610(7), 005380(5), 005860(5), 218150(5)
```

This file avoids those top-covered symbols and adds defensive yield / telecom / tobacco value-up cases:

```text
033780 KT&G
017670 SK텔레콤
030200 KT
032640 LG유플러스
```

Research question:

```text
Can C31 separate defensive-yield value-up cases where policy relevance turns into shareholder-return rerating from telecom policy-label cases where MAE is contained but MFE is too weak for Stage2/Yellow without company-specific execution?
```

C31 policy events are like a tide. The tide can lift defensive-yield names, but the boat still needs its own engine: dividend/buyback execution, free cash flow, ARPU or pricing, regulatory clarity, and capital allocation. Without that engine, a policy tide creates low volatility but not necessarily a Stage2 rerating.

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
| `033780` | KT&G | active_like / KOSPI | none listed | true |
| `017670` | SK텔레콤 | active_like / KOSPI | no 2024 overlap; 2021-era discontinuity already outside window | true |
| `030200` | KT | active_like / KOSPI | none listed | true |
| `032640` | LG유플러스 | active_like / KOSPI | no 2024 overlap; latest listed candidate 2010-01-15 | true |

Profile caveat:

```text
Stock-Web OHLC is raw/unadjusted marcap data.
These cases are calibration-safe for the selected 2024 windows because no listed corporate-action candidate overlaps each entry~D+180 test window.
```

---

## 3. Event family and trigger discipline

### Event family

```text
event_family = Korea Corporate Value-Up Program policy announcement / defensive-yield capital-return repricing
trigger_date = 2024-02-26
entry_rule = next_tradable_open_to_avoid_same_day_lookahead
entry_date = 2024-02-27
canonical_archetype_id = C31_POLICY_SUBSIDY_LEGISLATION_EVENT
fine_archetype_id = KOREA_VALUEUP_DEFENSIVE_YIELD_TELECOM_TOBACCO_CAPITAL_RETURN_AND_WEAK_MFE_ROUTER
```

This artifact intentionally marks non-price evidence as conservative:

```text
evidence_url_pending = true
source_proxy_only = true
```

Reason:

```text
The Stock-Web price path is fully validated, but company-level value-up plan, dividend/buyback execution, free cash flow, ROE/ROIC, regulatory clarity, ARPU/pricing, capex discipline, and capital-allocation bridge evidence still require URL repair through filings, IR, exchange disclosures, or regulatory documents before production weight promotion.
```

---

## 4. No-repeat and novelty check

Hard duplicate key:

```text
canonical_archetype_id + symbol + trigger_type + entry_date
```

Targeted repository searches before writing:

```text
033780 + C31_POLICY_SUBSIDY_LEGISLATION_EVENT -> no direct match found
017670 + C31_POLICY_SUBSIDY_LEGISLATION_EVENT -> no direct match found
030200 + C31_POLICY_SUBSIDY_LEGISLATION_EVENT -> no direct match found
032640 + C31_POLICY_SUBSIDY_LEGISLATION_EVENT -> no direct match found
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
| `R11L75_C31_033780_20240227` | `033780` KT&G | defensive-yield value-up / shareholder-return later rerating | positive-guarded |
| `R11L75_C31_017670_20240227` | `017670` SK텔레콤 | telecom defensive yield / capital return low-MAE path | positive-guarded low-MAE |
| `R11L75_C31_030200_20240227` | `030200` KT | telecom value-up policy label with weak MFE / drawdown | weak-MFE drawdown counterexample |
| `R11L75_C31_032640_20240227` | `032640` LG유플러스 | telecom value-up policy label with low MFE / slow fade | low-MFE counterexample |

The intended residual:

```text
C31 should separate:
1. defensive-yield names where shareholder-return / cash-flow evidence can convert policy relevance into delayed MFE;
2. telecom names where low MAE alone is not enough if MFE never expands;
3. policy-label cases where company-specific capital-return, ARPU, regulatory, and FCF evidence must be repaired before Stage2/Yellow.
```

---

## 6. Stock-Web OHLC and backtest

### 6.1 `033780` KT&G — defensive yield / shareholder-return later rerating

Trigger:

```text
trigger_date = 2024-02-26
trigger_type = Stage2-Actionable-Guarded
trigger_family = defensive_yield_valueup_shareholder_return_later_rerating
entry_date = 2024-02-27
entry_price = 92100.0
entry_price_type = next_tradable_open_after_korea_valueup_defensive_yield_event
```

Relevant Stock-Web rows:

```csv
d,o,h,l,c,v,a,mc,s,m
2024-02-26,93300.0,93300.0,91400.0,92100.0,187749.0,17309336560.0,12325051973700.0,133822497,KOSPI
2024-02-27,92100.0,92500.0,91600.0,91800.0,261875.0,24077061345.0,12284905224600.0,133822497,KOSPI
2024-03-14,94200.0,96000.0,93900.0,95200.0,389450.0,37060693600.0,12406701714400.0,130322497,KOSPI
2024-04-12,89600.0,89700.0,88000.0,88300.0,298018.0,26406019000.0,11507476485100.0,130322497,KOSPI
2024-05-29,85500.0,86000.0,85500.0,85600.0,195308.0,16730153800.0,11155605743200.0,130322497,KOSPI
2024-08-09,95000.0,101500.0,94300.0,100600.0,1372172.0,136142362500.0,13110443198200.0,130322497,KOSPI
2024-08-23,104300.0,108300.0,104100.0,107300.0,524108.0,56330203300.0,13983603928100.0,130322497,KOSPI
```

Backtest:

| window | peak/high | peak date | trough/low | trough date | MFE | MAE |
|---|---:|---|---:|---|---:|---:|
| 30 calendar days | 96000 | 2024-03-14 | 91000 | 2024-03-20 | +4.23% | -1.19% |
| 90 calendar days | 96000 | 2024-03-14 | 86100 | 2024-05-28 | +4.23% | -6.51% |
| 180 calendar days | 108300 | 2024-08-23 | 85500 | 2024-05-29 | +17.59% | -7.17% |

Interpretation:

```text
033780 is a delayed-MFE positive-guarded C31 case.
The first 90D path was not explosive, but the 180D path improved while MAE stayed controlled.
This should remain Stage2-Guarded / Yellow-after-repair, not Green from defensive-yield policy relevance alone.
```

### 6.2 `017670` SK텔레콤 — telecom defensive yield / capital-return low-MAE path

Trigger:

```text
trigger_date = 2024-02-26
trigger_type = Stage2-Actionable-Guarded
trigger_family = telecom_valueup_defensive_yield_capital_return_low_mae
entry_date = 2024-02-27
entry_price = 53000.0
entry_price_type = next_tradable_open_after_korea_valueup_telecom_yield_event
```

Relevant Stock-Web rows:

```csv
d,o,h,l,c,v,a,mc,s,m
2024-02-26,52700.0,52900.0,52200.0,52900.0,399359.0,21003768425.0,11362393803700.0,214790053,KOSPI
2024-02-27,53000.0,53000.0,52100.0,52300.0,396312.0,20777924364.0,11233519771900.0,214790053,KOSPI
2024-03-14,53400.0,55200.0,53200.0,54000.0,1174756.0,63696446400.0,11598662862000.0,214790053,KOSPI
2024-04-19,50300.0,50700.0,50000.0,50100.0,515479.0,25886732700.0,10760981655300.0,214790053,KOSPI
2024-07-25,53800.0,54700.0,53700.0,54100.0,1018590.0,55382390400.0,11620141867300.0,214790053,KOSPI
2024-08-23,55500.0,56500.0,55400.0,56100.0,725559.0,40732535600.0,12049721973300.0,214790053,KOSPI
```

Backtest:

| window | peak/high | peak date | trough/low | trough date | MFE | MAE |
|---|---:|---|---:|---|---:|---:|
| 30 calendar days | 55200 | 2024-03-14 | 52000 | 2024-03-04 | +4.15% | -1.89% |
| 90 calendar days | 55200 | 2024-03-14 | 50000 | 2024-04-19 | +4.15% | -5.66% |
| 180 calendar days | 56500 | 2024-08-23 | 50000 | 2024-04-19 | +6.60% | -5.66% |

Interpretation:

```text
017670 is a low-MAE but modest-MFE holdout.
The route can stay Stage2-Guarded only because capital preservation was strong; it does not justify Yellow/Green unless dividend/buyback, FCF, ARPU, and regulatory evidence are repaired.
```

### 6.3 `030200` KT — telecom value-up policy label with weak MFE / drawdown

Trigger:

```text
trigger_date = 2024-02-26
trigger_type = Stage2-FalsePositive-Candidate
trigger_family = telecom_valueup_policy_label_weak_mfe_drawdown
entry_date = 2024-02-27
entry_price = 38800.0
entry_price_type = next_tradable_open_after_korea_valueup_telecom_event
```

Relevant Stock-Web rows:

```csv
d,o,h,l,c,v,a,mc,s,m
2024-02-26,39750.0,39800.0,38500.0,38700.0,591319.0,23013690000.0,9979211412000.0,257860760,KOSPI
2024-02-27,38800.0,39100.0,37650.0,38100.0,716616.0,27338435850.0,9824494956000.0,257860760,KOSPI
2024-03-04,39250.0,39750.0,38600.0,38600.0,591873.0,23092081950.0,9953425336000.0,257860760,KOSPI
2024-04-19,33350.0,33650.0,33000.0,33300.0,773900.0,25745232827.0,8563594000500.0,257164985,KOSPI
2024-07-31,39100.0,39900.0,38900.0,39850.0,772348.0,30610587513.0,10043064147250.0,252021685,KOSPI
2024-08-01,39500.0,40000.0,38650.0,38750.0,727234.0,28315495000.0,9765840293750.0,252021685,KOSPI
```

Backtest:

| window | peak/high | peak date | trough/low | trough date | MFE | MAE |
|---|---:|---|---:|---|---:|---:|
| 30 calendar days | 39750 | 2024-03-04 | 37150 | 2024-03-20 | +2.45% | -4.25% |
| 90 calendar days | 39750 | 2024-03-04 | 33000 | 2024-04-19 | +2.45% | -14.95% |
| 180 calendar days | 40000 | 2024-08-01 | 33000 | 2024-04-19 | +3.09% | -14.95% |

Interpretation:

```text
030200 is a weak-MFE / drawdown C31 counterexample.
The telecom policy label was plausible, but the selected entry produced little MFE and a meaningful mid-window drawdown.
This should block Green and either block Stage2 or remain Stage2-Guarded only if later evidence repairs the capital-return / regulatory / cash-flow bridge.
```

### 6.4 `032640` LG유플러스 — telecom value-up policy label with low MFE / slow fade

Trigger:

```text
trigger_date = 2024-02-26
trigger_type = Stage2-FalsePositive-Candidate
trigger_family = telecom_valueup_policy_label_low_mfe_slow_fade
entry_date = 2024-02-27
entry_price = 10210.0
entry_price_type = next_tradable_open_after_korea_valueup_telecom_event
```

Relevant Stock-Web rows:

```csv
d,o,h,l,c,v,a,mc,s,m
2024-02-26,10310.0,10390.0,10120.0,10210.0,1099966.0,11267123920.0,4457801995810.0,436611361,KOSPI
2024-02-27,10210.0,10280.0,10150.0,10150.0,599457.0,6113841540.0,4431605314150.0,436611361,KOSPI
2024-02-29,10200.0,10320.0,10200.0,10320.0,2606703.0,26778102360.0,4505829245520.0,436611361,KOSPI
2024-03-19,9980.0,9990.0,9920.0,9920.0,1275709.0,12699212810.0,4331184701120.0,436611361,KOSPI
2024-04-16,9530.0,9560.0,9510.0,9510.0,828383.0,7888882470.0,4152174043110.0,436611361,KOSPI
2024-07-30,9950.0,10080.0,9950.0,10080.0,1417269.0,14222070580.0,4401042518880.0,436611361,KOSPI
```

Backtest:

| window | peak/high | peak date | trough/low | trough date | MFE | MAE |
|---|---:|---|---:|---|---:|---:|
| 30 calendar days | 10320 | 2024-02-29 | 9920 | 2024-03-19 | +1.08% | -2.84% |
| 90 calendar days | 10320 | 2024-02-29 | 9510 | 2024-04-16 | +1.08% | -6.86% |
| 180 calendar days | 10320 | 2024-02-29 | 9510 | 2024-04-16 | +1.08% | -6.86% |

Interpretation:

```text
032640 is a low-MFE slow-fade case.
MAE was not catastrophic, but Stage2 still fails if there is no MFE and no repaired execution bridge.
C31 should avoid counting low-volatility policy relevance as positive return alignment by itself.
```

---

## 7. Machine-readable trigger JSONL

```jsonl
{"row_type":"trigger","research_id":"R11L75_C31_DEFENSIVE_VALUEUP_ROUTER","round":"R11","loop":75,"large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"C31_POLICY_SUBSIDY_LEGISLATION_EVENT","fine_archetype_id":"KOREA_VALUEUP_DEFENSIVE_YIELD_TELECOM_TOBACCO_CAPITAL_RETURN_AND_WEAK_MFE_ROUTER","symbol":"033780","name":"KT&G","trigger_type":"Stage2-Actionable-Guarded","trigger_family":"defensive_yield_valueup_shareholder_return_later_rerating","trigger_date":"2024-02-26","entry_date":"2024-02-27","entry_price":92100.0,"entry_price_type":"next_tradable_open_after_korea_valueup_defensive_yield_event","price_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","mfe_30d_pct":4.23,"mae_30d_pct":-1.19,"mfe_90d_pct":4.23,"mae_90d_pct":-6.51,"mfe_180d_pct":17.59,"mae_180d_pct":-7.17,"peak_price_180d":108300.0,"peak_date_180d":"2024-08-23","trough_price_180d":85500.0,"trough_date_180d":"2024-05-29","calibration_usable":true,"case_polarity":"positive_guarded_defensive_yield_later_rerating","evidence_url_pending":true,"source_proxy_only":true,"non_price_evidence_strength":"medium_low_pending_url_repair","price_only_blowoff":false,"expected_stage_current_profile":"Stage2-Guarded_to_Yellow_if_shareholder_return_capital_allocation_bridge_repaired","residual_error_type":"defensive_yield_valueup_path_had_later_mfe_but_yellow_green_requires_url_repaired_shareholder_return_and_cashflow_bridge"}
{"row_type":"trigger","research_id":"R11L75_C31_DEFENSIVE_VALUEUP_ROUTER","round":"R11","loop":75,"large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"C31_POLICY_SUBSIDY_LEGISLATION_EVENT","fine_archetype_id":"KOREA_VALUEUP_DEFENSIVE_YIELD_TELECOM_TOBACCO_CAPITAL_RETURN_AND_WEAK_MFE_ROUTER","symbol":"017670","name":"SK텔레콤","trigger_type":"Stage2-Actionable-Guarded","trigger_family":"telecom_valueup_defensive_yield_capital_return_low_mae","trigger_date":"2024-02-26","entry_date":"2024-02-27","entry_price":53000.0,"entry_price_type":"next_tradable_open_after_korea_valueup_telecom_yield_event","price_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","mfe_30d_pct":4.15,"mae_30d_pct":-1.89,"mfe_90d_pct":4.15,"mae_90d_pct":-5.66,"mfe_180d_pct":6.6,"mae_180d_pct":-5.66,"peak_price_180d":56500.0,"peak_date_180d":"2024-08-23","trough_price_180d":50000.0,"trough_date_180d":"2024-04-19","calibration_usable":true,"case_polarity":"positive_guarded_low_mae_telecom_yield","evidence_url_pending":true,"source_proxy_only":true,"non_price_evidence_strength":"medium_low_pending_url_repair","price_only_blowoff":false,"expected_stage_current_profile":"Stage2-Guarded_only_until_dividend_buyback_cashflow_bridge_repaired","residual_error_type":"telecom_yield_valueup_path_preserved_mae_but_mfe_was_modest_without_stronger_capital_return_bridge"}
{"row_type":"trigger","research_id":"R11L75_C31_DEFENSIVE_VALUEUP_ROUTER","round":"R11","loop":75,"large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"C31_POLICY_SUBSIDY_LEGISLATION_EVENT","fine_archetype_id":"KOREA_VALUEUP_DEFENSIVE_YIELD_TELECOM_TOBACCO_CAPITAL_RETURN_AND_WEAK_MFE_ROUTER","symbol":"030200","name":"KT","trigger_type":"Stage2-FalsePositive-Candidate","trigger_family":"telecom_valueup_policy_label_weak_mfe_drawdown","trigger_date":"2024-02-26","entry_date":"2024-02-27","entry_price":38800.0,"entry_price_type":"next_tradable_open_after_korea_valueup_telecom_event","price_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","mfe_30d_pct":2.45,"mae_30d_pct":-4.25,"mfe_90d_pct":2.45,"mae_90d_pct":-14.95,"mfe_180d_pct":3.09,"mae_180d_pct":-14.95,"peak_price_180d":40000.0,"peak_date_180d":"2024-08-01","trough_price_180d":33000.0,"trough_date_180d":"2024-04-19","calibration_usable":true,"case_polarity":"counterexample_weak_mfe_drawdown","evidence_url_pending":true,"source_proxy_only":true,"non_price_evidence_strength":"low_pending_url_repair","price_only_blowoff":false,"expected_stage_current_profile":"blocked_Stage2_or_Stage2_Guarded_until_capital_return_regulatory_cashflow_bridge_repaired","residual_error_type":"telecom_valueup_policy_label_had_weak_mfe_and_mid_window_drawdown_without_company_specific_execution_bridge"}
{"row_type":"trigger","research_id":"R11L75_C31_DEFENSIVE_VALUEUP_ROUTER","round":"R11","loop":75,"large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"C31_POLICY_SUBSIDY_LEGISLATION_EVENT","fine_archetype_id":"KOREA_VALUEUP_DEFENSIVE_YIELD_TELECOM_TOBACCO_CAPITAL_RETURN_AND_WEAK_MFE_ROUTER","symbol":"032640","name":"LG유플러스","trigger_type":"Stage2-FalsePositive-Candidate","trigger_family":"telecom_valueup_policy_label_low_mfe_slow_fade","trigger_date":"2024-02-26","entry_date":"2024-02-27","entry_price":10210.0,"entry_price_type":"next_tradable_open_after_korea_valueup_telecom_event","price_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","mfe_30d_pct":1.08,"mae_30d_pct":-2.84,"mfe_90d_pct":1.08,"mae_90d_pct":-6.86,"mfe_180d_pct":1.08,"mae_180d_pct":-6.86,"peak_price_180d":10320.0,"peak_date_180d":"2024-02-29","trough_price_180d":9510.0,"trough_date_180d":"2024-04-16","calibration_usable":true,"case_polarity":"counterexample_low_mfe_slow_fade","evidence_url_pending":true,"source_proxy_only":true,"non_price_evidence_strength":"low_pending_url_repair","price_only_blowoff":false,"expected_stage_current_profile":"blocked_Stage2_or_narrative_only_until_capital_return_arpu_regulatory_bridge_repaired","residual_error_type":"telecom_valueup_policy_relevance_had_low_mae_but_almost_no_mfe_without_execution_bridge"}
```

---

## 8. Score simulation and raw component breakdown

This is shadow-only and does not change production scoring.

| symbol | policy relevance | shareholder-return bridge | FCF / cash-flow quality | regulatory / ARPU clarity | market mispricing | execution confidence | information confidence | shadow total | intended route |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| `033780` | 11 | 10 | 10 | 7 | 8 | 8 | 6 | 60 | Stage2-Guarded / Yellow after evidence repair |
| `017670` | 11 | 9 | 9 | 7 | 5 | 7 | 6 | 54 | Stage2-Guarded only until evidence repair |
| `030200` | 10 | 5 | 6 | 5 | 3 | 3 | 5 | 37 | blocked Stage2 or guarded after bridge repair |
| `032640` | 9 | 4 | 5 | 4 | 2 | 3 | 5 | 32 | narrative-only or blocked Stage2 until execution bridge |

### Current calibrated profile stress test

The current calibrated profile already blocks pure price-only blowoff.  
The remaining C31 issue is **policy relevance without return-aligned execution**:

```text
C31 defensive-yield holdout:
  value-up / capital-return relevance
  + MAE remains contained
  + delayed MFE appears
  + URL-repaired shareholder-return and cash-flow evidence
  => Stage2-Guarded / Yellow candidate

C31 telecom low-MAE but weak-MFE path:
  policy relevance exists
  + MAE is not severe
  + MFE_90D < +5%
  + evidence remains source_proxy_only
  => no Green and no automatic Stage2

C31 telecom drawdown path:
  policy relevance exists
  + MFE_90D < +5%
  + MAE_90D <= -10%
  + no capital-return / regulatory / FCF bridge
  => block Green and cap or block Stage2
```

`033780` and `017670` prevent overblocking.  
`030200` and `032640` show why policy relevance and low volatility do not automatically equal Stage2 return alignment.

---

## 9. Aggregate metrics

```json
{
  "row_type": "aggregate",
  "research_id": "R11L75_C31_DEFENSIVE_VALUEUP_ROUTER",
  "round": "R11",
  "loop": 75,
  "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC",
  "canonical_archetype_id": "C31_POLICY_SUBSIDY_LEGISLATION_EVENT",
  "fine_archetype_id": "KOREA_VALUEUP_DEFENSIVE_YIELD_TELECOM_TOBACCO_CAPITAL_RETURN_AND_WEAK_MFE_ROUTER",
  "case_count": 4,
  "calibration_usable_case_count": 4,
  "positive_guarded_case_count": 2,
  "counterexample_count": 2,
  "new_symbol_count": 4,
  "source_proxy_only_count": 4,
  "evidence_url_pending_count": 4,
  "avg_mfe_30d_pct": 2.98,
  "avg_mae_30d_pct": -2.54,
  "avg_mfe_90d_pct": 2.98,
  "avg_mae_90d_pct": -8.5,
  "avg_mfe_180d_pct": 7.09,
  "avg_mae_180d_pct": -8.66,
  "max_mfe_180d_pct": 17.59,
  "worst_mae_180d_pct": -14.95
}
```

---

## 10. 4B proximity split

```json
{
  "row_type": "4b_split",
  "research_id": "R11L75_C31_DEFENSIVE_VALUEUP_ROUTER",
  "stage2_guarded_or_yellow_candidate": [
    {
      "symbol": "033780",
      "reason": "defensive-yield path had delayed +17.59% 180D MFE with controlled -7.17% MAE"
    },
    {
      "symbol": "017670",
      "reason": "telecom-yield path had low MAE but modest MFE; suitable only as Stage2-Guarded pending evidence repair"
    }
  ],
  "blocked_stage2_or_stage2_guarded_review": [
    {
      "symbol": "030200",
      "reason": "MFE stayed below +5% while 90D/180D MAE reached -14.95%"
    },
    {
      "symbol": "032640",
      "reason": "MFE stayed near +1% despite contained MAE; policy label lacked return alignment"
    }
  ],
  "full_4b_or_green_requires_non_price_evidence": [
    "company-specific value-up plan",
    "dividend / buyback / total shareholder return execution",
    "free-cash-flow and payout capacity",
    "ARPU / pricing and regulatory clarity",
    "capex discipline",
    "ROE / ROIC and capital-allocation bridge"
  ]
}
```

---

## 11. Shadow rule candidate

```yaml
row_type: canonical_archetype_rule_candidate
canonical_archetype_id: C31_POLICY_SUBSIDY_LEGISLATION_EVENT
fine_archetype_id: KOREA_VALUEUP_DEFENSIVE_YIELD_TELECOM_TOBACCO_CAPITAL_RETURN_AND_WEAK_MFE_ROUTER
rule_name: C31_defensive_yield_valueup_execution_bridge_and_weak_mfe_router
production_scoring_changed: false
shadow_weight_only: true
```

### Proposed routing logic

```text
For C31 defensive-yield / telecom / tobacco value-up policy cases:

Tier A: verified defensive-yield rerating
  Conditions:
    - policy relevance is clear
    - shareholder-return / FCF / capital-allocation evidence is URL-repaired
    - MAE_90D > -8%
    - MFE_180D >= +12%
  Routing:
    - Stage2-Guarded allowed
    - Stage3-Yellow allowed after evidence repair
    - Green only after shareholder-return / FCF / capital-allocation bridge is verified

Tier B: low-MAE but weak-MFE telecom value-up path
  Conditions:
    - MFE_90D < +5%
    - MAE_90D > -10%
    - evidence remains source_proxy_only
  Routing:
    - no Green
    - narrative-only or Stage2-Guarded at most
    - require evidence repair for any positive promotion

Tier C: weak-MFE drawdown telecom policy label
  Conditions:
    - MFE_90D < +5%
    - MAE_90D <= -10%
    - no repaired dividend/buyback/ARPU/regulatory bridge
  Routing:
    - block Green
    - block Stage2 or local 4B watch
    - count as counterexample
```

### Suggested shadow delta

```json
{
  "row_type": "shadow_weight",
  "axis": "c31_defensive_yield_valueup_execution_bridge_and_weak_mfe_router",
  "scope": "canonical_archetype_id:C31_POLICY_SUBSIDY_LEGISLATION_EVENT",
  "proposal": {
    "source_proxy_only_green_allowed": false,
    "policy_relevance_alone_stage2_allowed": false,
    "shareholder_return_fcf_capital_allocation_bridge_required_for_green": true,
    "defensive_yield_mfe180_threshold_pct": 12.0,
    "defensive_yield_mae90_min_pct": -8.0,
    "weak_mfe_threshold_90d_pct": 5.0,
    "weak_mfe_drawdown_threshold_90d_pct": -10.0,
    "low_mae_weak_mfe_positive_promotion_allowed": false,
    "positive_weight_blocked_until_url_repair": true
  },
  "confidence": "medium_low_until_url_repair",
  "apply_now": false,
  "reason": "Two defensive-yield low-MAE holdouts and two telecom weak-MFE policy-label counterexamples show that C31 should not promote policy relevance alone. Yellow/Green requires URL-repaired shareholder-return, FCF, ARPU/regulatory, ROE/ROIC, and capital-allocation evidence."
}
```

---

## 12. Residual contribution summary

```json
{
  "row_type": "residual_contribution",
  "research_id": "R11L75_C31_DEFENSIVE_VALUEUP_ROUTER",
  "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC",
  "canonical_archetype_id": "C31_POLICY_SUBSIDY_LEGISLATION_EVENT",
  "contribution": "Adds four non-top-covered C31 defensive-yield / telecom / tobacco value-up cases and separates low-MAE defensive-yield holdouts from weak-MFE telecom policy-label failures. C31 Yellow/Green should require URL-repaired shareholder return, free-cash-flow, ARPU/regulatory, capex discipline, ROE/ROIC, and capital-allocation evidence.",
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
  "data_quality_blocker": "All four non-price value-up defensive-yield triggers require URL-level repair before positive weight promotion.",
  "guardrail_added": "C31 source_proxy_only defensive-yield cases with MFE_90D < +5% should not be promoted from policy relevance alone; MFE_90D < +5% and MAE_90D <= -10% should block Green and usually block Stage2."
}
```

One-line contribution:

```text
This loop adds 4 new independent cases, 2 counterexamples, and 2 residual errors for R11/L10_POLICY_EVENT_CROSS_REDTEAM_MISC/C31_POLICY_SUBSIDY_LEGISLATION_EVENT.
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
    033780: false
    017670: false
    030200: false
    032640: false
  evidence_url_pending:
    033780: true
    017670: true
    030200: true
    032640: true
  source_proxy_only:
    033780: true
    017670: true
    030200: true
    032640: true
```

Limitations:

```text
- Price path is validated against Stock-Web tradable OHLC rows.
- Non-price evidence is not URL-repaired in this run.
- Therefore this artifact is useful for C31 policy/value-up defensive-yield residual shape and weak-MFE guardrail design, but should not promote positive weights until filings, IR, exchange disclosures, or regulatory documents verify shareholder return, FCF, ARPU/pricing, regulatory clarity, capex discipline, ROE/ROIC, and capital allocation.
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
2. Preserve R11 / loop 75 metadata.
3. Add the cases to C31_POLICY_SUBSIDY_LEGISLATION_EVENT only if parser validation passes.
4. Treat all four non-price triggers as evidence_url_pending=true and source_proxy_only=true until URL-level evidence is repaired.
5. Do not use these rows for positive weight promotion until filings/IR/exchange-disclosure/regulatory data verifies company-specific value-up plans, shareholder return, free cash flow, ARPU/pricing, regulatory clarity, capex discipline, ROE/ROIC, and capital allocation.
6. Add a shadow-only rule candidate named C31_defensive_yield_valueup_execution_bridge_and_weak_mfe_router.
7. Do not loosen Stage3-Green.
8. Add C31-specific guards:
   - source_proxy_only -> no Green
   - policy relevance alone -> no Stage2 promotion
   - Stage3-Yellow/Green requires company-specific shareholder-return / FCF / capital-allocation bridge
   - MFE_180D >= +12% and MAE_90D > -8% may remain Stage2-Guarded until evidence repair
   - MFE_90D < +5% and MAE_90D > -10% -> narrative-only or Stage2-Guarded at most
   - MFE_90D < +5% and MAE_90D <= -10% -> block Green and often block Stage2 / local 4B watch
9. Keep production scoring unchanged unless later batch promotion logic independently marks this axis safe.
```

---

## 15. Next round state

```text
completed_round = R11
completed_loop = 75
next_round = R12
next_loop = 75
next_large_sector_hint = L10_POLICY_EVENT_CROSS_REDTEAM_MISC
round_schedule_status = valid
round_sector_consistency = pass
```
