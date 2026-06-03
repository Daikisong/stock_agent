# E2R Stock-Web v12 Residual Research — R12 Loop 74

```yaml
research_session: post_calibrated_sector_archetype_residual_research
mode: historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12
completed_round: R12
completed_loop: 74
next_round: R13
next_loop: 74
large_sector_id: L10_POLICY_EVENT_CROSS_REDTEAM_MISC
canonical_archetype_id: C31_POLICY_SUBSIDY_LEGISLATION_EVENT
fine_archetype_id: KOREA_VALUEUP_HOLDING_DISCOUNT_CAPITAL_ALLOCATION_AND_WEAK_MFE_ROUTER
output_file: e2r_stock_web_v12_residual_round_R12_loop_74_L10_POLICY_EVENT_CROSS_REDTEAM_MISC_C31_POLICY_SUBSIDY_LEGISLATION_EVENT_research.md
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
completed_loop  = 74
large_sector_id = L10_POLICY_EVENT_CROSS_REDTEAM_MISC
canonical_archetype_id = C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP
```

Therefore:

```text
scheduled_round = R12
scheduled_loop  = 74
```

R12 permits:

```text
large_sector_id = L10_POLICY_EVENT_CROSS_REDTEAM_MISC
or
under-covered service/agri/event sector
```

This run selects:

```text
large_sector_id = L10_POLICY_EVENT_CROSS_REDTEAM_MISC
canonical_archetype_id = C31_POLICY_SUBSIDY_LEGISLATION_EVENT
fine_archetype_id = KOREA_VALUEUP_HOLDING_DISCOUNT_CAPITAL_ALLOCATION_AND_WEAK_MFE_ROUTER
```

This is a valid R12/L10 pairing.

---

## 1. Why this R12/C31 run

The no-repeat ledger shows C31 is broad and already covered, but the top-covered symbols are not the holding-company discount / capital-allocation set tested here:

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

This file deliberately tests a different C31 policy-event subtype from the prior auto value-up run:

```text
fine_archetype_id = KOREA_VALUEUP_HOLDING_DISCOUNT_CAPITAL_ALLOCATION_AND_WEAK_MFE_ROUTER
```

Selected symbols:

```text
001040 CJ
003550 LG
034730 SK
```

Research question:

```text
Can C31 separate Korea value-up / holding-company discount closure from holding-company policy-label rallies where the policy wind is real, but company-specific capital allocation, shareholder return, ROE, and discount-closure evidence are not yet repaired?
```

C31 policy events are like a tide. They lift many names at the same time, but the ship still needs its own hull. For holding companies, that hull is capital allocation, governance, shareholder return, NAV-discount closure, and cash-flow-through evidence. Without that, the policy event can lift the price for one tide and then strand it on the rocks.

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
| `001040` | CJ | active_like / KOSPI | no 2024 overlap; latest listed candidate 2008-01-22 | true |
| `003550` | LG | active_like / KOSPI | no 2024 overlap; latest listed candidate 2004-08-05 | true |
| `034730` | SK | active_like / KOSPI | no 2024 overlap; latest listed candidate 2015-08-17 | true |

Profile caveat:

```text
Stock-Web OHLC is raw/unadjusted marcap data.
These cases are calibration-safe for the selected 2024 windows because no listed corporate-action candidate overlaps each entry~D+180 test window.
```

---

## 3. Event family and trigger discipline

### Event family

```text
event_family = Korea Corporate Value-Up Program policy announcement / holding-company discount closure
trigger_date = 2024-02-26
entry_rule = next_tradable_open_to_avoid_same_day_lookahead
entry_date = 2024-02-27
canonical_archetype_id = C31_POLICY_SUBSIDY_LEGISLATION_EVENT
fine_archetype_id = KOREA_VALUEUP_HOLDING_DISCOUNT_CAPITAL_ALLOCATION_AND_WEAK_MFE_ROUTER
```

This artifact intentionally marks non-price evidence as conservative:

```text
evidence_url_pending = true
source_proxy_only = true
```

Reason:

```text
The Stock-Web price path is fully validated, but company-level value-up plan disclosure, shareholder-return policy, dividend/buyback execution, governance reform, NAV-discount closure, subsidiary cash-flow-through, and ROE bridge evidence still require URL repair through filings, company IR, exchange disclosures, or regulatory documents before production weight promotion.
```

C31 interpretation used here:

```text
C31 should not score all policy beneficiaries the same.
A policy event creates an option.
Company-specific capital allocation converts the option into Stage2/Yellow/Green.
```

---

## 4. No-repeat and novelty check

Hard duplicate key:

```text
canonical_archetype_id + symbol + trigger_type + entry_date
```

Targeted repository searches before writing:

```text
001040 + C31_POLICY_SUBSIDY_LEGISLATION_EVENT -> no direct match found
003550 + C31_POLICY_SUBSIDY_LEGISLATION_EVENT -> no direct match found
034730 + C31_POLICY_SUBSIDY_LEGISLATION_EVENT -> no direct match found
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
| `R12L74_C31_001040_20240227` | `001040` CJ | holding-company value-up / discount closure / capital allocation rerating | positive anchor |
| `R12L74_C31_003550_20240227` | `003550` LG | holding-company value-up policy label without execution bridge | weak-MFE high-MAE counterexample |
| `R12L74_C31_034730_20240227` | `034730` SK | holding-company value-up label with hard MAE | hard-MAE counterexample |

The intended residual:

```text
C31 should separate:
1. holding-company value-up paths where MFE expands and MAE remains contained;
2. holding-company policy-label cases where MFE remains weak and drawdown reopens the discount;
3. hard-MAE holding-company paths where policy relevance is not enough without capital allocation / ROE / shareholder-return evidence.
```

---

## 6. Stock-Web OHLC and backtest

### 6.1 `001040` CJ — holding-company value-up / discount closure rerating

Trigger:

```text
trigger_date = 2024-02-26
trigger_type = Stage2-Actionable
trigger_family = holding_company_valueup_discount_closure_capital_allocation_rerating
entry_date = 2024-02-27
entry_price = 94000.0
entry_price_type = next_tradable_open_after_korea_valueup_policy_event
```

Relevant Stock-Web rows:

```csv
d,o,h,l,c,v,a,mc,s,m
2024-02-26,100300.0,100400.0,92700.0,94300.0,235412.0,22409828500.0,2751390911400.0,29176998,KOSPI
2024-02-27,94000.0,94200.0,92100.0,93000.0,84642.0,7887174300.0,2713460814000.0,29176998,KOSPI
2024-03-15,96500.0,109200.0,95900.0,109200.0,688893.0,71770424800.0,3186128181600.0,29176998,KOSPI
2024-03-28,116900.0,124000.0,114000.0,122200.0,308463.0,37067135300.0,3565429155600.0,29176998,KOSPI
2024-04-05,132100.0,135500.0,127900.0,128600.0,203954.0,26583541700.0,3752161942800.0,29176998,KOSPI
2024-07-11,121100.0,123600.0,119000.0,122300.0,196597.0,23877703800.0,3568346855400.0,29176998,KOSPI
2024-08-01,130900.0,135000.0,128800.0,134900.0,101820.0,13551741600.0,3935977030200.0,29176998,KOSPI
2024-08-30,112900.0,113700.0,107000.0,111900.0,129870.0,14587244000.0,3264906076200.0,29176998,KOSPI
```

Backtest:

| window | peak/high | peak date | trough/low | trough date | MFE | MAE |
|---|---:|---|---:|---|---:|---:|
| 30 calendar days | 124000 | 2024-03-28 | 91100 | 2024-03-13 | +31.91% | -3.09% |
| 90 calendar days | 135500 | 2024-04-05 | 91100 | 2024-03-13 | +44.15% | -3.09% |
| 180 calendar days | 135500 | 2024-04-05 | 91100 | 2024-03-13 | +44.15% | -3.09% |

Interpretation:

```text
001040 is the C31 positive anchor.
The policy event was followed by persistent MFE and low MAE, which is the price shape of a real holding-discount closure rerating.
Green still requires URL-repaired value-up plan, shareholder return, capital allocation, ROE, and cash-flow-through evidence.
```

### 6.2 `003550` LG — holding-company policy label with weak MFE and high MAE

Trigger:

```text
trigger_date = 2024-02-26
trigger_type = Stage2-FalsePositive-Candidate
trigger_family = holding_company_valueup_policy_label_weak_mfe_discount_reopen
entry_date = 2024-02-27
entry_price = 94400.0
entry_price_type = next_tradable_open_after_korea_valueup_policy_event
```

Relevant Stock-Web rows:

```csv
d,o,h,l,c,v,a,mc,s,m
2024-02-26,100600.0,100600.0,92700.0,93900.0,604229.0,57485392100.0,14770563242700.0,157300993,KOSPI
2024-02-27,94400.0,94500.0,92200.0,93400.0,230955.0,21587830100.0,14691912746200.0,157300993,KOSPI
2024-03-14,100200.0,101500.0,98200.0,101400.0,443284.0,44565060300.0,15950320690200.0,157300993,KOSPI
2024-03-28,88700.0,88700.0,87600.0,87600.0,244326.0,21493775200.0,13779566986800.0,157300993,KOSPI
2024-04-18,76100.0,76800.0,73900.0,76200.0,457818.0,34661107479.0,11986335666600.0,157300993,KOSPI
2024-06-13,83200.0,85300.0,81400.0,81400.0,351352.0,29108184400.0,12804300830200.0,157300993,KOSPI
2024-08-05,83800.0,83800.0,77400.0,78100.0,242747.0,19353161300.0,12285207553300.0,157300993,KOSPI
2024-09-03,79700.0,85900.0,79500.0,85400.0,563126.0,47399268700.0,13433504802200.0,157300993,KOSPI
```

Backtest:

| window | peak/high | peak date | trough/low | trough date | MFE | MAE |
|---|---:|---|---:|---|---:|---:|
| 30 calendar days | 101500 | 2024-03-14 | 87600 | 2024-03-28 | +7.52% | -7.20% |
| 90 calendar days | 101500 | 2024-03-14 | 73900 | 2024-04-18 | +7.52% | -21.72% |
| 180 calendar days | 101500 | 2024-03-14 | 73900 | 2024-04-18 | +7.52% | -21.72% |

Interpretation:

```text
003550 is the weak-MFE/high-MAE C31 counterexample.
The value-up policy label was plausible, but post-entry upside remained below +10% and the 90D drawdown exceeded -20%.
This should block Green and either block Stage2 or cap at Stage2-Guarded until capital-allocation and shareholder-return evidence is repaired.
```

### 6.3 `034730` SK — holding-company policy label with hard MAE

Trigger:

```text
trigger_date = 2024-02-26
trigger_type = Stage2-FalsePositive-Candidate
trigger_family = holding_company_valueup_policy_label_weak_mfe_high_mae
entry_date = 2024-02-27
entry_price = 188800.0
entry_price_type = next_tradable_open_after_korea_valueup_policy_event
```

Relevant Stock-Web rows:

```csv
d,o,h,l,c,v,a,mc,s,m
2024-02-26,199800.0,199900.0,187200.0,190200.0,436018.0,83211567300.0,13922322175800.0,73198329,KOSPI
2024-02-27,188800.0,189300.0,181600.0,185500.0,253583.0,46848898900.0,13578290029500.0,73198329,KOSPI
2024-02-29,194500.0,196700.0,188800.0,191800.0,372756.0,71298040900.0,14039439502200.0,73198329,KOSPI
2024-03-12,186200.0,186200.0,178300.0,180400.0,254731.0,45982039500.0,13204978551600.0,73198329,KOSPI
2024-05-24,149300.0,151500.0,148500.0,148800.0,126956.0,18971376500.0,10891911355200.0,73198329,KOSPI
2024-06-10,184300.0,194700.0,180200.0,188600.0,1615800.0,306392365800.0,13805204849400.0,73198329,KOSPI
2024-08-05,142400.0,143000.0,128400.0,131300.0,347328.0,47025691500.0,9519604903900.0,72502703,KOSPI
2024-09-20,149600.0,156700.0,147500.0,154000.0,507998.0,78470567500.0,11165416262000.0,72502703,KOSPI
```

Backtest:

| window | peak/high | peak date | trough/low | trough date | MFE | MAE |
|---|---:|---|---:|---|---:|---:|
| 30 calendar days | 196700 | 2024-02-29 | 178300 | 2024-03-12 | +4.18% | -5.56% |
| 90 calendar days | 196700 | 2024-02-29 | 148500 | 2024-05-24 | +4.18% | -21.35% |
| 180 calendar days | 196700 | 2024-02-29 | 128400 | 2024-08-05 | +4.18% | -31.99% |

Interpretation:

```text
034730 is the hard-MAE C31 counterexample.
The policy label existed, but MFE was tiny and the 180D drawdown crossed -30%.
This should block Stage2 or route to local 4B/high-MAE watch unless a company-specific value-up, capital-return, ROE, and portfolio-discount bridge appears before entry.
```

---

## 7. Machine-readable trigger JSONL

```jsonl
{"row_type":"trigger","research_id":"R12L74_C31_HOLDCO_VALUEUP_ROUTER","round":"R12","loop":74,"large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"C31_POLICY_SUBSIDY_LEGISLATION_EVENT","fine_archetype_id":"KOREA_VALUEUP_HOLDING_DISCOUNT_CAPITAL_ALLOCATION_AND_WEAK_MFE_ROUTER","symbol":"001040","name":"CJ","trigger_type":"Stage2-Actionable","trigger_family":"holding_company_valueup_discount_closure_capital_allocation_rerating","trigger_date":"2024-02-26","entry_date":"2024-02-27","entry_price":94000.0,"entry_price_type":"next_tradable_open_after_korea_valueup_policy_event","price_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","mfe_30d_pct":31.91,"mae_30d_pct":-3.09,"mfe_90d_pct":44.15,"mae_90d_pct":-3.09,"mfe_180d_pct":44.15,"mae_180d_pct":-3.09,"peak_price_180d":135500.0,"peak_date_180d":"2024-04-05","trough_price_180d":91100.0,"trough_date_180d":"2024-03-13","calibration_usable":true,"case_polarity":"positive_anchor_low_mae_valueup","evidence_url_pending":true,"source_proxy_only":true,"non_price_evidence_strength":"medium_pending_url_repair","price_only_blowoff":false,"expected_stage_current_profile":"Stage2-Actionable_to_Yellow_after_capital_allocation_shareholder_return_bridge_repaired","residual_error_type":"positive_holding_discount_closure_path_requires_url_repaired_valueup_capital_allocation_and_roe_bridge_before_green"}
{"row_type":"trigger","research_id":"R12L74_C31_HOLDCO_VALUEUP_ROUTER","round":"R12","loop":74,"large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"C31_POLICY_SUBSIDY_LEGISLATION_EVENT","fine_archetype_id":"KOREA_VALUEUP_HOLDING_DISCOUNT_CAPITAL_ALLOCATION_AND_WEAK_MFE_ROUTER","symbol":"003550","name":"LG","trigger_type":"Stage2-FalsePositive-Candidate","trigger_family":"holding_company_valueup_policy_label_weak_mfe_discount_reopen","trigger_date":"2024-02-26","entry_date":"2024-02-27","entry_price":94400.0,"entry_price_type":"next_tradable_open_after_korea_valueup_policy_event","price_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","mfe_30d_pct":7.52,"mae_30d_pct":-7.2,"mfe_90d_pct":7.52,"mae_90d_pct":-21.72,"mfe_180d_pct":7.52,"mae_180d_pct":-21.72,"peak_price_180d":101500.0,"peak_date_180d":"2024-03-14","trough_price_180d":73900.0,"trough_date_180d":"2024-04-18","calibration_usable":true,"case_polarity":"counterexample_weak_mfe_high_mae","evidence_url_pending":true,"source_proxy_only":true,"non_price_evidence_strength":"low_pending_url_repair","price_only_blowoff":false,"expected_stage_current_profile":"blocked_Stage2_or_Stage2_Guarded_until_capital_allocation_bridge_repaired","residual_error_type":"valueup_policy_relevance_without_company_specific_capital_allocation_bridge_led_to_weak_mfe_and_high_mae"}
{"row_type":"trigger","research_id":"R12L74_C31_HOLDCO_VALUEUP_ROUTER","round":"R12","loop":74,"large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"C31_POLICY_SUBSIDY_LEGISLATION_EVENT","fine_archetype_id":"KOREA_VALUEUP_HOLDING_DISCOUNT_CAPITAL_ALLOCATION_AND_WEAK_MFE_ROUTER","symbol":"034730","name":"SK","trigger_type":"Stage2-FalsePositive-Candidate","trigger_family":"holding_company_valueup_policy_label_weak_mfe_high_mae","trigger_date":"2024-02-26","entry_date":"2024-02-27","entry_price":188800.0,"entry_price_type":"next_tradable_open_after_korea_valueup_policy_event","price_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","mfe_30d_pct":4.18,"mae_30d_pct":-5.56,"mfe_90d_pct":4.18,"mae_90d_pct":-21.35,"mfe_180d_pct":4.18,"mae_180d_pct":-31.99,"peak_price_180d":196700.0,"peak_date_180d":"2024-02-29","trough_price_180d":128400.0,"trough_date_180d":"2024-08-05","calibration_usable":true,"case_polarity":"counterexample_weak_mfe_hard_mae","evidence_url_pending":true,"source_proxy_only":true,"non_price_evidence_strength":"low_pending_url_repair","price_only_blowoff":false,"expected_stage_current_profile":"blocked_Stage2_or_4B_high_MAE_watch_until_shareholder_return_roe_bridge_repaired","residual_error_type":"holding_company_valueup_label_had_low_mfe_and_180d_hard_mae_without_repaired_capital_return_or_discount_closure_bridge"}
```

---

## 8. Score simulation and raw component breakdown

This is shadow-only and does not change production scoring.

| symbol | policy relevance | capital allocation / shareholder return | NAV discount closure | ROE / cash-flow-through bridge | market mispricing | execution confidence | information confidence | shadow total | intended route |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| `001040` | 13 | 11 | 12 | 10 | 13 | 9 | 6 | 74 | Stage2/Yellow after evidence repair |
| `003550` | 12 | 4 | 4 | 5 | 5 | 3 | 5 | 38 | blocked Stage2 or guarded until bridge repair |
| `034730` | 12 | 3 | 3 | 4 | 4 | 2 | 5 | 33 | blocked Stage2 / 4B high-MAE watch |

### Current calibrated profile stress test

The current calibrated profile already blocks pure price-only blowoff.  
The remaining C31 issue is **policy-event relevance without company-specific execution**:

```text
C31 clean holding-discount path:
  policy relevance
  + persistent MFE
  + contained MAE
  + URL-repaired value-up / capital-allocation / shareholder-return bridge
  => Stage2-Actionable / Stage3-Yellow, possible Green after proof

C31 holding-company policy-label false-positive:
  policy relevance exists
  + MFE_30D < +10%
  + MAE_90D <= -20%
  + no company-specific execution bridge
  => block Green and cap or block Stage2

C31 hard-MAE holding-company path:
  policy relevance exists
  + MFE_180D < +10%
  + MAE_180D <= -30%
  + bridge remains source_proxy_only
  => local 4B/high-MAE watch or blocked Stage2
```

`001040` prevents overblocking: some holding-company value-up cases became real low-MAE reratings.  
`003550` and `034730` show why the policy label cannot be used as a universal boost.

---

## 9. Aggregate metrics

```json
{
  "row_type": "aggregate",
  "research_id": "R12L74_C31_HOLDCO_VALUEUP_ROUTER",
  "round": "R12",
  "loop": 74,
  "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC",
  "canonical_archetype_id": "C31_POLICY_SUBSIDY_LEGISLATION_EVENT",
  "fine_archetype_id": "KOREA_VALUEUP_HOLDING_DISCOUNT_CAPITAL_ALLOCATION_AND_WEAK_MFE_ROUTER",
  "case_count": 3,
  "calibration_usable_case_count": 3,
  "positive_case_count": 1,
  "counterexample_count": 2,
  "new_symbol_count": 3,
  "source_proxy_only_count": 3,
  "evidence_url_pending_count": 3,
  "avg_mfe_30d_pct": 14.54,
  "avg_mae_30d_pct": -5.28,
  "avg_mfe_90d_pct": 18.62,
  "avg_mae_90d_pct": -15.39,
  "avg_mfe_180d_pct": 18.62,
  "avg_mae_180d_pct": -18.93,
  "max_mfe_180d_pct": 44.15,
  "worst_mae_180d_pct": -31.99
}
```

---

## 10. 4B proximity split

```json
{
  "row_type": "4b_split",
  "research_id": "R12L74_C31_HOLDCO_VALUEUP_ROUTER",
  "stage2_positive_or_yellow_candidate": [
    {
      "symbol": "001040",
      "reason": "persistent +44.15% 180D MFE with only -3.09% MAE; requires URL-repaired value-up / shareholder-return / capital-allocation evidence before Green"
    }
  ],
  "blocked_stage2_or_local_4b_watch": [
    {
      "symbol": "003550",
      "reason": "MFE stayed at +7.52% while 90D/180D MAE reached -21.72%; no repaired execution bridge"
    },
    {
      "symbol": "034730",
      "reason": "MFE stayed at +4.18% while 180D MAE reached -31.99%; hard-MAE holding-company policy-label counterexample"
    }
  ],
  "full_4b_or_green_requires_non_price_evidence": [
    "company-specific value-up plan",
    "dividend / buyback / total shareholder return execution",
    "capital allocation and portfolio restructuring plan",
    "NAV-discount closure mechanism",
    "ROE and subsidiary cash-flow-through bridge"
  ]
}
```

---

## 11. Shadow rule candidate

```yaml
row_type: canonical_archetype_rule_candidate
canonical_archetype_id: C31_POLICY_SUBSIDY_LEGISLATION_EVENT
fine_archetype_id: KOREA_VALUEUP_HOLDING_DISCOUNT_CAPITAL_ALLOCATION_AND_WEAK_MFE_ROUTER
rule_name: C31_valueup_holding_discount_execution_bridge_and_weak_mfe_router
production_scoring_changed: false
shadow_weight_only: true
```

### Proposed routing logic

```text
For C31 Korea value-up / holding-company discount cases:

Tier A: verified holding-discount closure winner
  Conditions:
    - policy relevance is clear
    - company-specific value-up / shareholder return / capital allocation evidence is URL-repaired
    - MFE_90D >= +25%
    - MAE_90D remains contained
  Routing:
    - Stage2-Actionable allowed
    - Stage3-Yellow allowed after evidence repair
    - Green only after capital allocation / shareholder return / ROE bridge is verified

Tier B: policy-label but weak-MFE holding-company path
  Conditions:
    - policy relevance exists
    - MFE_30D < +10%
    - MAE_90D <= -20%
    - evidence remains source_proxy_only
  Routing:
    - block Green
    - Stage2-Guarded at most
    - no positive weight promotion

Tier C: hard-MAE holding-company false-positive
  Conditions:
    - MFE_180D < +10%
    - MAE_180D <= -30%
    - no repaired capital-allocation / shareholder-return bridge
  Routing:
    - block Stage2 or route to local 4B/high-MAE watch
    - count as counterexample
```

### Suggested shadow delta

```json
{
  "row_type": "shadow_weight",
  "axis": "c31_valueup_holding_discount_execution_bridge_and_weak_mfe_router",
  "scope": "canonical_archetype_id:C31_POLICY_SUBSIDY_LEGISLATION_EVENT",
  "proposal": {
    "source_proxy_only_green_allowed": false,
    "policy_relevance_alone_green_allowed": false,
    "holding_company_capital_allocation_bridge_required_for_green": true,
    "positive_mfe90_threshold_pct": 25.0,
    "weak_mfe_threshold_30d_pct": 10.0,
    "weak_mfe_mae90_threshold_pct": -20.0,
    "hard_mae_threshold_180d_pct": -30.0,
    "positive_weight_blocked_until_url_repair": true
  },
  "confidence": "medium_low_until_url_repair",
  "apply_now": false,
  "reason": "One holding-company discount-closure winner and two weak-MFE/high-MAE holding-company policy-label failures show that C31 should not boost holding companies from value-up policy relevance alone. Green requires company-specific capital allocation, shareholder return, NAV-discount closure, ROE, and cash-flow-through evidence."
}
```

---

## 12. Residual contribution summary

```json
{
  "row_type": "residual_contribution",
  "research_id": "R12L74_C31_HOLDCO_VALUEUP_ROUTER",
  "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC",
  "canonical_archetype_id": "C31_POLICY_SUBSIDY_LEGISLATION_EVENT",
  "contribution": "Adds three C31 Korea value-up holding-company discount/capital-allocation cases and separates a clean low-MAE holding-discount closure path from two weak-MFE/high-MAE policy-label false positives. C31 Green should require URL-repaired company-specific value-up plan, shareholder return, capital allocation, NAV-discount closure, ROE, and cash-flow-through evidence.",
  "positive_case_added": 1,
  "counterexample_case_added": 2,
  "new_symbol_count": 3,
  "data_quality_blocker": "All three non-price value-up holding-company triggers require URL-level repair before positive weight promotion.",
  "guardrail_added": "C31 policy relevance alone cannot create Green; holding-company cases with MFE_30D < +10% and MAE_90D <= -20% should cap at Stage2-Guarded, while MFE_180D < +10% and MAE_180D <= -30% should block Stage2 or route to local 4B/high-MAE watch."
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
    001040: false
    003550: false
    034730: false
  evidence_url_pending:
    001040: true
    003550: true
    034730: true
  source_proxy_only:
    001040: true
    003550: true
    034730: true
```

Limitations:

```text
- Price path is validated against Stock-Web tradable OHLC rows.
- Non-price evidence is not URL-repaired in this run.
- Therefore this artifact is useful for C31 Korea value-up holding-company discount residual shape and weak-MFE/high-MAE guardrail design, but should not promote positive weights until filings, IR, exchange disclosures, or regulatory documents verify value-up plan, shareholder return, buybacks/dividends, capital allocation, NAV-discount closure, ROE, and cash-flow-through bridge.
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
2. Preserve R12 / loop 74 metadata.
3. Add the cases to C31_POLICY_SUBSIDY_LEGISLATION_EVENT only if parser validation passes.
4. Treat all three non-price triggers as evidence_url_pending=true and source_proxy_only=true until URL-level evidence is repaired.
5. Do not use these rows for positive weight promotion until filings/IR/exchange-disclosure/regulatory data verifies company-specific value-up plans, shareholder return, buyback/dividend execution, capital allocation, NAV-discount closure, ROE, and cash-flow-through bridge.
6. Add a shadow-only rule candidate named C31_valueup_holding_discount_execution_bridge_and_weak_mfe_router.
7. Do not loosen Stage3-Green.
8. Add C31-specific guards:
   - source_proxy_only -> no Green
   - policy relevance alone -> no Green
   - Stage3-Yellow/Green requires company-specific capital-allocation / shareholder-return bridge
   - MFE_30D < +10% and MAE_90D <= -20% -> Stage2-Guarded at most
   - MFE_180D < +10% and MAE_180D <= -30% -> block Stage2 or local 4B/high-MAE watch
9. Keep production scoring unchanged unless later batch promotion logic independently marks this axis safe.
```

---

## 15. Next round state

```text
completed_round = R12
completed_loop = 74
next_round = R13
next_loop = 74
next_large_sector_hint = L10_POLICY_EVENT_CROSS_REDTEAM_MISC
next_allowed_scope = R13_CROSS_ARCHETYPE_STAGE2_FALSE_POSITIVE_REVIEW or R13_CROSS_ARCHETYPE_4B_4C_REDTEAM or R13_CROSS_ARCHETYPE_ACCOUNTING_TRUST_PRICE_VALIDATION or R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL
round_schedule_status = valid
round_sector_consistency = pass
```
