# E2R Stock-Web v12 Residual Research — R11 Loop 76

```yaml
research_session: post_calibrated_sector_archetype_residual_research
mode: historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12
completed_round: R11
completed_loop: 76
next_round: R12
next_loop: 76
large_sector_id: L10_POLICY_EVENT_CROSS_REDTEAM_MISC
canonical_archetype_id: C31_POLICY_SUBSIDY_LEGISLATION_EVENT
fine_archetype_id: KOREA_VALUEUP_HOLDING_COMPANY_CAPITAL_ALLOCATION_AND_WEAK_MFE_ROUTER
output_file: e2r_stock_web_v12_residual_round_R11_loop_76_L10_POLICY_EVENT_CROSS_REDTEAM_MISC_C31_POLICY_SUBSIDY_LEGISLATION_EVENT_research.md
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
completed_loop  = 76
large_sector_id = L9_CONSTRUCTION_REALESTATE_HOUSING
canonical_archetype_id = C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK
```

Therefore:

```text
scheduled_round = R11
scheduled_loop  = 76
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
fine_archetype_id = KOREA_VALUEUP_HOLDING_COMPANY_CAPITAL_ALLOCATION_AND_WEAK_MFE_ROUTER
```

This is a valid R11/L10 pairing.

---

## 1. Why this R11/C31 run

The no-repeat ledger shows C31 is wide and policy-event-heavy:

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

This file avoids those top-covered C31 names and adds a value-up fine subtype distinct from the previous R11 telecom/tobacco value-up run:

```text
Korea value-up holding company / capital allocation / discount-release router
```

Selected symbols:

```text
000150 두산
028260 삼성물산
003550 LG
034730 SK
```

Research question:

```text
Can C31 separate holding-company value-up rerating from policy-label cases where the Korea value-up event is real but company-specific capital allocation, shareholder return, discount release, and earnings-quality bridges are not repaired?
```

C31 policy events are a tide; holding companies are boats tied to different anchors. A value-up tide can lift one boat quickly when capital allocation and earnings quality loosen the anchor. Another boat can still sit low in the water if portfolio complexity, governance discount, capital burden, or weak shareholder-return execution keeps the chain tight.

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
| `000150` | 두산 | active_like / KOSPI | no 2024 overlap; latest listed candidate 1999-12-03 | true |
| `028260` | 삼성물산 | active_like / KOSPI | no 2024 overlap; 2015 merger/listing discontinuity outside window | true |
| `003550` | LG | active_like / KOSPI | no 2024 overlap; latest listed candidate 2004-08-05 | true |
| `034730` | SK | active_like / KOSPI | no 2024 overlap; latest listed candidate 2015-08-17 | true |

Profile caveat:

```text
Stock-Web OHLC is raw/unadjusted marcap data.
These cases are calibration-safe for the selected 2024 30D/90D/180D windows because no listed corporate-action candidate overlaps each entry~D+180 test window.
```

---

## 3. Event family and trigger discipline

### Event family

```text
event_family = Korea Corporate Value-Up Program / holding-company discount-release / capital-allocation repricing
trigger_date = 2024-02-26
entry_rule = next_tradable_open_to_avoid_same_day_lookahead
entry_date = 2024-02-27
canonical_archetype_id = C31_POLICY_SUBSIDY_LEGISLATION_EVENT
fine_archetype_id = KOREA_VALUEUP_HOLDING_COMPANY_CAPITAL_ALLOCATION_AND_WEAK_MFE_ROUTER
```

This artifact intentionally marks non-price evidence as conservative:

```text
evidence_url_pending = true
source_proxy_only = true
```

Reason:

```text
The Stock-Web price path is fully validated, but company-level capital allocation, shareholder-return execution, treasury-share policy, portfolio restructuring, NAV discount release, ROE/ROIC improvement, dividend/buyback capacity, earnings quality, and governance-discount evidence still require URL repair through filings, IR, exchange disclosures, or regulatory documents before production weight promotion.
```

---

## 4. No-repeat and novelty check

Hard duplicate key:

```text
canonical_archetype_id + symbol + trigger_type + entry_date
```

Targeted repository searches before writing:

```text
000150 + C31_POLICY_SUBSIDY_LEGISLATION_EVENT -> no direct match found
028260 + C31_POLICY_SUBSIDY_LEGISLATION_EVENT -> no direct match found
003550 + C31_POLICY_SUBSIDY_LEGISLATION_EVENT -> no direct match found
034730 + C31_POLICY_SUBSIDY_LEGISLATION_EVENT -> no direct match found
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
| `R11L76_C31_000150_20240227` | `000150` 두산 | value-up holdco / capital allocation / AI-industrial repricing | positive anchor |
| `R11L76_C31_028260_20240227` | `028260` 삼성물산 | value-up governance holdco discount release / moderate-MFE later drawdown | positive-guarded |
| `R11L76_C31_003550_20240227` | `003550` LG | value-up holdco policy label with weak MFE / drawdown | counterexample |
| `R11L76_C31_034730_20240227` | `034730` SK | value-up holdco policy label with weak MFE / high MAE | counterexample |

The intended residual:

```text
C31 should separate:
1. holding-company value-up paths where policy relevance compounds with company-specific capital allocation or earnings-quality catalysts;
2. governance-discount release paths that are only Stage2-Guarded unless shareholder-return evidence is repaired;
3. policy-label holdcos where MFE stays weak and drawdown widens;
4. portfolio-complexity holdcos where value-up relevance alone does not overcome structural discount.
```

---

## 6. Stock-Web OHLC and backtest

### 6.1 `000150` 두산 — holding-company value-up / capital-allocation positive anchor

Trigger:

```text
trigger_date = 2024-02-26
trigger_type = Stage2-Actionable
trigger_family = korea_valueup_holding_company_capital_allocation_ai_industrial_repricing_low_mae
entry_date = 2024-02-27
entry_price = 95100.0
entry_price_type = next_tradable_open_after_korea_valueup_holding_company_policy_burst
```

Relevant Stock-Web rows:

```csv
d,o,h,l,c,v,a,mc,s,m
2024-02-26,99300.0,102300.0,95700.0,95900.0,164838.0,16109125728.0,1584635776500.0,16523835,KOSPI
2024-02-27,95100.0,96300.0,90200.0,90600.0,129340.0,11931220400.0,1497059451000.0,16523835,KOSPI
2024-02-28,90600.0,92400.0,89600.0,91700.0,88864.0,8068719600.0,1515235669500.0,16523835,KOSPI
2024-03-18,144300.0,163400.0,143700.0,162000.0,602761.0,93052813500.0,2676861270000.0,16523835,KOSPI
2024-05-27,208500.0,218500.0,202000.0,206500.0,315232.0,65739517300.0,3412171927500.0,16523835,KOSPI
2024-07-12,263500.0,263500.0,221000.0,237000.0,626925.0,150539605500.0,3916148895000.0,16523835,KOSPI
2024-08-05,142200.0,143000.0,122000.0,128100.0,502710.0,66626020800.0,2116703263500.0,16523835,KOSPI
```

Backtest:

| window | peak/high | peak date | trough/low | trough date | MFE | MAE |
|---|---:|---|---:|---|---:|---:|
| 30 calendar days | 163400 | 2024-03-18 | 89600 | 2024-02-28 | +71.82% | -5.78% |
| 90 calendar days | 218500 | 2024-05-27 | 89600 | 2024-02-28 | +129.76% | -5.78% |
| 180 calendar days | 263500 | 2024-07-12 | 89600 | 2024-02-28 | +177.08% | -5.78% |

Interpretation:

```text
000150 is the C31 value-up holdco positive anchor.
The policy event aligned with a company-specific repricing path: MFE compounded through 90D/180D while MAE stayed contained.
This can support Stage2-Actionable / Yellow after evidence repair, but Green still requires URL-repaired capital allocation, earnings-quality, shareholder-return, and NAV discount-release evidence.
```

### 6.2 `028260` 삼성물산 — governance holdco discount release with moderate MFE and later drawdown

Trigger:

```text
trigger_date = 2024-02-26
trigger_type = Stage2-Actionable-Guarded
trigger_family = korea_valueup_governance_holdco_discount_release_moderate_mfe_later_drawdown
entry_date = 2024-02-27
entry_price = 151000.0
entry_price_type = next_tradable_open_after_korea_valueup_governance_holdco_policy_burst
```

Relevant Stock-Web rows:

```csv
d,o,h,l,c,v,a,mc,s,m
2024-02-26,157500.0,157600.0,147500.0,152300.0,1019655.0,155228817300.0,28265611341000.0,185591670,KOSPI
2024-02-27,151000.0,151700.0,147100.0,147400.0,609664.0,90549242600.0,27356212158000.0,185591670,KOSPI
2024-02-28,147700.0,157500.0,147000.0,155700.0,638228.0,97755578600.0,28896623019000.0,185591670,KOSPI
2024-03-14,167100.0,170800.0,164200.0,170800.0,884935.0,149705307900.0,31699057236000.0,185591670,KOSPI
2024-04-19,137300.0,139500.0,136600.0,138200.0,289202.0,39875080600.0,25648768794000.0,185591670,KOSPI
2024-08-05,144200.0,144200.0,132800.0,135300.0,372457.0,51374483100.0,24054189677100.0,177784107,KOSPI
```

Backtest:

| window | peak/high | peak date | trough/low | trough date | MFE | MAE |
|---|---:|---|---:|---|---:|---:|
| 30 calendar days | 170800 | 2024-03-14 | 147000 | 2024-02-28 | +13.11% | -2.65% |
| 90 calendar days | 170800 | 2024-03-14 | 136600 | 2024-04-19 | +13.11% | -9.54% |
| 180 calendar days | 170800 | 2024-03-14 | 132800 | 2024-08-05 | +13.11% | -12.05% |

Interpretation:

```text
028260 is a positive-guarded, not Green, value-up case.
MFE was real but moderate, and later drawdown widened. It should stay Stage2-Guarded until governance, capital-return, earnings-quality, and discount-release evidence is repaired.
```

### 6.3 `003550` LG — value-up holding-company policy label with weak MFE and drawdown

Trigger:

```text
trigger_date = 2024-02-26
trigger_type = Stage2-FalsePositive-Candidate
trigger_family = korea_valueup_holding_company_policy_label_weak_mfe_drawdown
entry_date = 2024-02-27
entry_price = 94400.0
entry_price_type = next_tradable_open_after_korea_valueup_holdco_policy_label
```

Relevant Stock-Web rows:

```csv
d,o,h,l,c,v,a,mc,s,m
2024-02-26,100600.0,100600.0,92700.0,93900.0,604229.0,57485392100.0,14770563242700.0,157300993,KOSPI
2024-02-27,94400.0,94500.0,92200.0,93400.0,230955.0,21587830100.0,14691912746200.0,157300993,KOSPI
2024-03-14,100200.0,101500.0,98200.0,101400.0,443284.0,44565060300.0,15950320690200.0,157300993,KOSPI
2024-03-28,88700.0,88700.0,87600.0,87600.0,244326.0,21493775200.0,13779566986800.0,157300993,KOSPI
2024-04-18,76100.0,76800.0,73900.0,76200.0,457818.0,34661107479.0,11986335666600.0,157300993,KOSPI
2024-08-05,83800.0,83800.0,77400.0,78100.0,242747.0,19353161300.0,12285207553300.0,157300993,KOSPI
```

Backtest:

| window | peak/high | peak date | trough/low | trough date | MFE | MAE |
|---|---:|---|---:|---|---:|---:|
| 30 calendar days | 101500 | 2024-03-14 | 87600 | 2024-03-28 | +7.52% | -7.20% |
| 90 calendar days | 101500 | 2024-03-14 | 73900 | 2024-04-18 | +7.52% | -21.72% |
| 180 calendar days | 101500 | 2024-03-14 | 73900 | 2024-04-18 | +7.52% | -21.72% |

Interpretation:

```text
003550 is the weak-MFE value-up counterexample.
Policy relevance existed, but MFE did not expand enough and the 90D drawdown crossed a local high-MAE zone.
C31 should not promote a holding-company policy label without company-specific capital-return and discount-release evidence.
```

### 6.4 `034730` SK — value-up holding-company policy label with weak MFE and high MAE

Trigger:

```text
trigger_date = 2024-02-26
trigger_type = Stage2-FalsePositive-Candidate
trigger_family = korea_valueup_holding_company_policy_label_weak_mfe_high_mae
entry_date = 2024-02-27
entry_price = 188800.0
entry_price_type = next_tradable_open_after_korea_valueup_holdco_policy_label
```

Relevant Stock-Web rows:

```csv
d,o,h,l,c,v,a,mc,s,m
2024-02-26,199800.0,199900.0,187200.0,190200.0,436018.0,83211567300.0,13922322175800.0,73198329,KOSPI
2024-02-27,188800.0,189300.0,181600.0,185500.0,253583.0,46848898900.0,13578290029500.0,73198329,KOSPI
2024-02-29,194500.0,196700.0,188800.0,191800.0,372756.0,71298040900.0,14039439502200.0,73198329,KOSPI
2024-04-19,155100.0,157500.0,153400.0,155500.0,118931.0,18435400800.0,11382340159500.0,73198329,KOSPI
2024-05-24,149300.0,151500.0,148500.0,148800.0,126956.0,18971376500.0,10891911355200.0,73198329,KOSPI
2024-08-05,142400.0,143000.0,128400.0,131300.0,347328.0,47025691500.0,9519604903900.0,72502703,KOSPI
```

Backtest:

| window | peak/high | peak date | trough/low | trough date | MFE | MAE |
|---|---:|---|---:|---|---:|---:|
| 30 calendar days | 196700 | 2024-02-29 | 178300 | 2024-03-12 | +4.18% | -5.56% |
| 90 calendar days | 196700 | 2024-02-29 | 148500 | 2024-05-24 | +4.18% | -21.35% |
| 180 calendar days | 196700 | 2024-02-29 | 128400 | 2024-08-05 | +4.18% | -31.99% |

Interpretation:

```text
034730 is the hard weak-MFE / high-MAE value-up counterexample.
The holding-company policy label peaked almost immediately, then the path became drawdown-heavy.
This should block Stage2 or route to local 4B/high-MAE watch until portfolio restructuring, shareholder return, and capital-allocation evidence is repaired.
```

---

## 7. Machine-readable trigger JSONL

```jsonl
{"row_type":"trigger","research_id":"R11L76_C31_VALUEUP_HOLDCO_ROUTER","round":"R11","loop":76,"large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"C31_POLICY_SUBSIDY_LEGISLATION_EVENT","fine_archetype_id":"KOREA_VALUEUP_HOLDING_COMPANY_CAPITAL_ALLOCATION_AND_WEAK_MFE_ROUTER","symbol":"000150","name":"두산","trigger_type":"Stage2-Actionable","trigger_family":"korea_valueup_holding_company_capital_allocation_ai_industrial_repricing_low_mae","trigger_date":"2024-02-26","entry_date":"2024-02-27","entry_price":95100.0,"entry_price_type":"next_tradable_open_after_korea_valueup_holding_company_policy_burst","price_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","mfe_30d_pct":71.82,"mae_30d_pct":-5.78,"mfe_90d_pct":129.76,"mae_90d_pct":-5.78,"mfe_180d_pct":177.08,"mae_180d_pct":-5.78,"peak_price_180d":263500.0,"peak_date_180d":"2024-07-12","trough_price_180d":89600.0,"trough_date_180d":"2024-02-28","calibration_usable":true,"case_polarity":"positive_anchor_valueup_holdco_low_mae","evidence_url_pending":true,"source_proxy_only":true,"non_price_evidence_strength":"medium_pending_url_repair","price_only_blowoff":false,"expected_stage_current_profile":"Stage2-Actionable_to_Yellow_after_capital_allocation_earnings_quality_shareholder_return_bridge_repaired","residual_error_type":"holding_company_valueup_path_supports_positive_route_but_green_requires_url_repaired_capital_allocation_earnings_and_shareholder_return_bridge"}
{"row_type":"trigger","research_id":"R11L76_C31_VALUEUP_HOLDCO_ROUTER","round":"R11","loop":76,"large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"C31_POLICY_SUBSIDY_LEGISLATION_EVENT","fine_archetype_id":"KOREA_VALUEUP_HOLDING_COMPANY_CAPITAL_ALLOCATION_AND_WEAK_MFE_ROUTER","symbol":"028260","name":"삼성물산","trigger_type":"Stage2-Actionable-Guarded","trigger_family":"korea_valueup_governance_holdco_discount_release_moderate_mfe_later_drawdown","trigger_date":"2024-02-26","entry_date":"2024-02-27","entry_price":151000.0,"entry_price_type":"next_tradable_open_after_korea_valueup_governance_holdco_policy_burst","price_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","mfe_30d_pct":13.11,"mae_30d_pct":-2.65,"mfe_90d_pct":13.11,"mae_90d_pct":-9.54,"mfe_180d_pct":13.11,"mae_180d_pct":-12.05,"peak_price_180d":170800.0,"peak_date_180d":"2024-03-14","trough_price_180d":132800.0,"trough_date_180d":"2024-08-05","calibration_usable":true,"case_polarity":"positive_guarded_moderate_mfe_later_drawdown","evidence_url_pending":true,"source_proxy_only":true,"non_price_evidence_strength":"medium_low_pending_url_repair","price_only_blowoff":false,"expected_stage_current_profile":"Stage2-Guarded_only_until_governance_capital_return_earnings_quality_bridge_repaired","residual_error_type":"holdco_valueup_governance_path_had_moderate_mfe_but_later_drawdown_requires_url_repaired_capital_return_and_discount_release_bridge"}
{"row_type":"trigger","research_id":"R11L76_C31_VALUEUP_HOLDCO_ROUTER","round":"R11","loop":76,"large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"C31_POLICY_SUBSIDY_LEGISLATION_EVENT","fine_archetype_id":"KOREA_VALUEUP_HOLDING_COMPANY_CAPITAL_ALLOCATION_AND_WEAK_MFE_ROUTER","symbol":"003550","name":"LG","trigger_type":"Stage2-FalsePositive-Candidate","trigger_family":"korea_valueup_holding_company_policy_label_weak_mfe_drawdown","trigger_date":"2024-02-26","entry_date":"2024-02-27","entry_price":94400.0,"entry_price_type":"next_tradable_open_after_korea_valueup_holdco_policy_label","price_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","mfe_30d_pct":7.52,"mae_30d_pct":-7.2,"mfe_90d_pct":7.52,"mae_90d_pct":-21.72,"mfe_180d_pct":7.52,"mae_180d_pct":-21.72,"peak_price_180d":101500.0,"peak_date_180d":"2024-03-14","trough_price_180d":73900.0,"trough_date_180d":"2024-04-18","calibration_usable":true,"case_polarity":"counterexample_weak_mfe_drawdown","evidence_url_pending":true,"source_proxy_only":true,"non_price_evidence_strength":"low_pending_url_repair","price_only_blowoff":false,"expected_stage_current_profile":"blocked_Stage2_or_narrative_only_until_capital_allocation_discount_release_bridge_repaired","residual_error_type":"holding_company_valueup_policy_label_had_weak_mfe_and_90d_drawdown_without_company_specific_capital_return_bridge"}
{"row_type":"trigger","research_id":"R11L76_C31_VALUEUP_HOLDCO_ROUTER","round":"R11","loop":76,"large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"C31_POLICY_SUBSIDY_LEGISLATION_EVENT","fine_archetype_id":"KOREA_VALUEUP_HOLDING_COMPANY_CAPITAL_ALLOCATION_AND_WEAK_MFE_ROUTER","symbol":"034730","name":"SK","trigger_type":"Stage2-FalsePositive-Candidate","trigger_family":"korea_valueup_holding_company_policy_label_weak_mfe_high_mae","trigger_date":"2024-02-26","entry_date":"2024-02-27","entry_price":188800.0,"entry_price_type":"next_tradable_open_after_korea_valueup_holdco_policy_label","price_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","mfe_30d_pct":4.18,"mae_30d_pct":-5.56,"mfe_90d_pct":4.18,"mae_90d_pct":-21.35,"mfe_180d_pct":4.18,"mae_180d_pct":-31.99,"peak_price_180d":196700.0,"peak_date_180d":"2024-02-29","trough_price_180d":128400.0,"trough_date_180d":"2024-08-05","calibration_usable":true,"case_polarity":"counterexample_weak_mfe_high_mae","evidence_url_pending":true,"source_proxy_only":true,"non_price_evidence_strength":"low_pending_url_repair","price_only_blowoff":false,"expected_stage_current_profile":"blocked_Stage2_or_local_4B_high_MAE_watch_until_portfolio_restructuring_capital_return_bridge_repaired","residual_error_type":"holding_company_valueup_policy_label_had_weak_mfe_and_180d_high_mae_without_capital_allocation_and_discount_release_bridge"}
```

---

## 8. Score simulation and raw component breakdown

This is shadow-only and does not change production scoring.

| symbol | policy relevance | capital allocation bridge | shareholder return | NAV / discount release | earnings quality | market mispricing | information confidence | shadow total | intended route |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| `000150` | 12 | 12 | 9 | 10 | 11 | 16 | 6 | 76 | Stage2/Yellow after evidence repair |
| `028260` | 11 | 8 | 7 | 8 | 7 | 7 | 5 | 53 | Stage2-Guarded only until evidence repair |
| `003550` | 10 | 4 | 4 | 4 | 4 | 2 | 5 | 33 | blocked Stage2 or narrative-only |
| `034730` | 10 | 3 | 3 | 3 | 3 | 1 | 5 | 28 | blocked Stage2 / local 4B high-MAE watch |

### Current calibrated profile stress test

The current calibrated profile already blocks pure price-only blowoff.  
The remaining C31 issue is **policy relevance without company-specific capital-allocation execution**:

```text
C31 value-up holdco winner:
  value-up policy relevance
  + company-specific capital allocation / earnings-quality catalyst
  + MFE_90D >= +40%
  + MAE_90D > -10%
  => Stage2-Actionable / Yellow after evidence repair

C31 moderate-MFE governance discount path:
  value-up/governance relevance
  + MFE_90D >= +10%
  + MAE_90D near or below -10%
  + evidence remains source_proxy_only
  => Stage2-Guarded at most, no Green

C31 weak-MFE holdco policy label:
  MFE_90D < +10%
  + MAE_90D <= -20%
  + no capital-return/NAV discount-release bridge
  => block Stage2 or narrative-only

C31 weak-MFE high-MAE holdco:
  MFE_90D < +5%
  + MAE_180D <= -30%
  + no portfolio restructuring / shareholder-return bridge
  => block Stage2 or local 4B/high-MAE watch
```

`000150` prevents overblocking.  
`028260` shows why a moderate value-up path can remain Stage2-Guarded.  
`003550` and `034730` show why policy relevance alone should not become Stage2 or Green.

---

## 9. Aggregate metrics

```json
{
  "row_type": "aggregate",
  "research_id": "R11L76_C31_VALUEUP_HOLDCO_ROUTER",
  "round": "R11",
  "loop": 76,
  "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC",
  "canonical_archetype_id": "C31_POLICY_SUBSIDY_LEGISLATION_EVENT",
  "fine_archetype_id": "KOREA_VALUEUP_HOLDING_COMPANY_CAPITAL_ALLOCATION_AND_WEAK_MFE_ROUTER",
  "case_count": 4,
  "calibration_usable_case_count": 4,
  "positive_case_count": 2,
  "counterexample_count": 2,
  "new_symbol_count": 4,
  "source_proxy_only_count": 4,
  "evidence_url_pending_count": 4,
  "avg_mfe_30d_pct": 24.16,
  "avg_mae_30d_pct": -5.3,
  "avg_mfe_90d_pct": 38.64,
  "avg_mae_90d_pct": -14.6,
  "avg_mfe_180d_pct": 50.47,
  "avg_mae_180d_pct": -17.89,
  "max_mfe_180d_pct": 177.08,
  "worst_mae_180d_pct": -31.99
}
```

---

## 10. 4B proximity split

```json
{
  "row_type": "4b_split",
  "research_id": "R11L76_C31_VALUEUP_HOLDCO_ROUTER",
  "stage2_positive_or_yellow_candidate": [
    {
      "symbol": "000150",
      "reason": "holding-company value-up path had +177.08% 180D MFE with only -5.78% MAE"
    }
  ],
  "stage2_guarded_or_yellow_watch": [
    {
      "symbol": "028260",
      "reason": "governance/value-up path had +13.11% MFE but 180D MAE reached -12.05%; needs capital-return evidence repair"
    }
  ],
  "blocked_stage2_or_narrative_only": [
    {
      "symbol": "003550",
      "reason": "holding-company policy label had only +7.52% MFE and -21.72% 90D/180D MAE"
    }
  ],
  "blocked_stage2_or_local_4b_watch": [
    {
      "symbol": "034730",
      "reason": "holding-company policy label had only +4.18% MFE and -31.99% 180D MAE"
    }
  ],
  "full_4b_or_green_requires_non_price_evidence": [
    "company-specific value-up plan",
    "capital allocation and portfolio restructuring",
    "dividend / buyback / treasury-share policy",
    "NAV discount-release mechanism",
    "ROE / ROIC and earnings-quality improvement",
    "governance-discount repair"
  ]
}
```

---

## 11. Shadow rule candidate

```yaml
row_type: canonical_archetype_rule_candidate
canonical_archetype_id: C31_POLICY_SUBSIDY_LEGISLATION_EVENT
fine_archetype_id: KOREA_VALUEUP_HOLDING_COMPANY_CAPITAL_ALLOCATION_AND_WEAK_MFE_ROUTER
rule_name: C31_korea_valueup_holding_company_capital_allocation_and_weak_mfe_router
production_scoring_changed: false
shadow_weight_only: true
```

### Proposed routing logic

```text
For C31 Korea value-up holding-company cases:

Tier A: verified value-up holdco winner
  Conditions:
    - capital allocation, shareholder return, NAV discount-release, and earnings-quality evidence are URL-repaired
    - MFE_90D >= +40%
    - MAE_90D > -10%
  Routing:
    - Stage2-Actionable allowed
    - Stage3-Yellow allowed after evidence repair
    - Green only after company-specific execution bridge is verified

Tier B: moderate-MFE governance discount path
  Conditions:
    - MFE_90D >= +10%
    - MAE_90D <= -8% or evidence remains source_proxy_only
  Routing:
    - Stage2-Guarded at most
    - no Green until evidence repair

Tier C: weak-MFE holdco policy label
  Conditions:
    - MFE_90D < +10%
    - MAE_90D <= -20%
    - no repaired capital-return / NAV discount-release bridge
  Routing:
    - block Stage2 or narrative-only
    - count as counterexample

Tier D: weak-MFE high-MAE holdco
  Conditions:
    - MFE_90D < +5%
    - MAE_180D <= -30%
    - no portfolio restructuring / shareholder-return bridge
  Routing:
    - block Stage2
    - local 4B/high-MAE watch
```

### Suggested shadow delta

```json
{
  "row_type": "shadow_weight",
  "axis": "c31_korea_valueup_holding_company_capital_allocation_and_weak_mfe_router",
  "scope": "canonical_archetype_id:C31_POLICY_SUBSIDY_LEGISLATION_EVENT",
  "proposal": {
    "source_proxy_only_green_allowed": false,
    "policy_relevance_alone_stage2_allowed": false,
    "capital_allocation_shareholder_return_nav_discount_bridge_required_for_green": true,
    "verified_holdco_winner_mfe90_threshold_pct": 40.0,
    "verified_holdco_winner_mae90_min_pct": -10.0,
    "moderate_mfe_threshold_90d_pct": 10.0,
    "moderate_path_mae90_watch_pct": -8.0,
    "weak_mfe_threshold_90d_pct": 10.0,
    "weak_mfe_mae90_threshold_pct": -20.0,
    "weak_mfe_high_mae_mfe90_threshold_pct": 5.0,
    "weak_mfe_high_mae180_threshold_pct": -30.0,
    "positive_weight_blocked_until_url_repair": true
  },
  "confidence": "medium_low_until_url_repair",
  "apply_now": false,
  "reason": "One value-up holdco winner, one moderate guarded case, and two weak-MFE holdco policy-label failures show that C31 should not promote Korea value-up relevance without URL-repaired capital allocation, shareholder return, NAV discount-release, earnings-quality, and governance evidence."
}
```

---

## 12. Residual contribution summary

```json
{
  "row_type": "residual_contribution",
  "research_id": "R11L76_C31_VALUEUP_HOLDCO_ROUTER",
  "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC",
  "canonical_archetype_id": "C31_POLICY_SUBSIDY_LEGISLATION_EVENT",
  "contribution": "Adds four non-top-covered C31 Korea value-up holding-company cases and separates a true capital-allocation rerating from moderate-MFE governance-discount and weak-MFE/high-MAE policy-label failures. C31 Yellow/Green should require URL-repaired capital allocation, shareholder return, treasury-share policy, portfolio restructuring, NAV discount release, ROE/ROIC and earnings-quality evidence.",
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
  "data_quality_blocker": "All four non-price Korea value-up holding-company triggers require URL-level repair before positive weight promotion.",
  "guardrail_added": "C31 source_proxy_only holdco value-up cases with MFE_90D < +10% and MAE_90D <= -20% should block Stage2; MFE_90D < +5% and MAE_180D <= -30% should route to local 4B/high-MAE watch."
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
    000150: false
    028260: false
    003550: false
    034730: false
  evidence_url_pending:
    000150: true
    028260: true
    003550: true
    034730: true
  source_proxy_only:
    000150: true
    028260: true
    003550: true
    034730: true
```

Limitations:

```text
- Price path is validated against Stock-Web tradable OHLC rows.
- Non-price evidence is not URL-repaired in this run.
- Therefore this artifact is useful for C31 Korea value-up holding-company residual shape and weak-MFE/high-MAE guardrail design, but should not promote positive weights until filings, IR, exchange disclosures, or regulatory/company documents verify capital allocation, shareholder return, treasury-share policy, portfolio restructuring, NAV discount release, earnings quality, and governance-discount repair.
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
2. Preserve R11 / loop 76 metadata.
3. Add the cases to C31_POLICY_SUBSIDY_LEGISLATION_EVENT only if parser validation passes.
4. Treat all four non-price triggers as evidence_url_pending=true and source_proxy_only=true until URL-level evidence is repaired.
5. Do not use these rows for positive weight promotion until filings/IR/exchange-disclosure/company-document data verifies capital allocation, shareholder return, treasury-share policy, portfolio restructuring, NAV discount release, earnings quality, and governance-discount repair.
6. Add a shadow-only rule candidate named C31_korea_valueup_holding_company_capital_allocation_and_weak_mfe_router.
7. Do not loosen Stage3-Green.
8. Add C31-specific guards:
   - source_proxy_only -> no Green
   - policy relevance alone -> no Stage2 promotion
   - Stage3-Yellow/Green requires company-specific capital-allocation / shareholder-return / NAV-discount bridge
   - MFE_90D >= +40% and MAE_90D > -10% may remain Stage2-Actionable / Yellow watch after evidence repair
   - MFE_90D >= +10% but MAE_90D <= -8% -> Stage2-Guarded at most until evidence repair
   - MFE_90D < +10% and MAE_90D <= -20% -> block Stage2 or narrative-only
   - MFE_90D < +5% and MAE_180D <= -30% -> block Stage2 / local 4B high-MAE watch
9. Keep production scoring unchanged unless later batch promotion logic independently marks this axis safe.
```

---

## 15. Next round state

```text
completed_round = R11
completed_loop = 76
next_round = R12
next_loop = 76
next_large_sector_hint = L10_POLICY_EVENT_CROSS_REDTEAM_MISC
round_schedule_status = valid
round_sector_consistency = pass
```
