# E2R Stock-Web v12 Residual Research — R6 Loop 72

```yaml
research_session: post_calibrated_sector_archetype_residual_research
mode: historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12
completed_round: R6
completed_loop: 72
next_round: R7
next_loop: 72
large_sector_id: L6_FINANCIAL_CAPITAL_RETURN_DIGITAL
canonical_archetype_id: C22_INSURANCE_RATE_CYCLE_RESERVE
fine_archetype_id: INSURANCE_VALUEUP_RESERVE_RATE_CYCLE_AND_POST_SPIKE_MAE
output_file: e2r_stock_web_v12_residual_round_R6_loop_72_L6_FINANCIAL_CAPITAL_RETURN_DIGITAL_C22_INSURANCE_RATE_CYCLE_RESERVE_research.md
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

### Round resolution

The immediately preceding completed scheduled artifact in this automation chain was:

```text
completed_round = R5
completed_loop = 72
large_sector_id = L5_CONSUMER_BRAND_DISTRIBUTION
canonical_archetype_id = C18_CONSUMER_EXPORT_CHANNEL_REORDER
```

Therefore:

```text
scheduled_round = R6
scheduled_loop = 72
```

R6 maps to:

```text
large_sector_id = L6_FINANCIAL_CAPITAL_RETURN_DIGITAL
```

This run selects:

```text
canonical_archetype_id = C22_INSURANCE_RATE_CYCLE_RESERVE
```

This is a valid R6/L6 pairing.

---

## 1. Why this R6/C22 run

The no-repeat ledger shows C22 is covered but still has a data-quality warning because URL/proxy repair remains non-trivial:

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

This run avoids the highest-covered C22 symbols and adds:

```text
003690 코리안리
082640 동양생명
000370 한화손해보험
```

The residual question is:

```text
Can C22 separate low-MAE insurance reserve/rate-cycle rerating from late-entry insurance value-up overheat that turns into high-MAE?
```

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

| symbol | name | market | profile status | corporate-action candidate overlap with selected 180D window | calibration usable |
|---|---|---|---|---|---|
| `003690` | 코리안리 | KOSPI | active_like | none in 2024 test window; old 1997/2004 candidates only | true |
| `082640` | 동양생명 | KOSPI | active_like | none in 2024 test window; old 2017 candidate only | true |
| `000370` | 한화손해보험 | KOSPI | active_like | none in 2024 test window; latest listed candidate is 2017-11-23 | true |

Profile caveat:

```text
Stock-Web OHLC is raw/unadjusted marcap data. These cases are calibration-safe for the selected 2024 windows because no listed corporate-action candidate overlaps each entry~D+180 test window.
```

---

## 3. Evidence status and trigger discipline

This artifact intentionally uses conservative evidence flags:

```text
evidence_url_pending = true
source_proxy_only = true
```

Reason:

```text
The Stock-Web price path is fully validated, but company-level CSM, reserve quality, IFRS17 assumptions, loss ratio, shareholder-return plan, and rate-cycle evidence still require later URL repair through filings, IR decks, reports, or regulatory data before any production weight promotion.
```

C22 interpretation used here:

```text
C22 is not simply “insurance stock rose.”
It asks whether the rerating is supported by:
- reserve quality,
- rate cycle / loss ratio,
- CSM or earnings visibility,
- ROE/PBR gap closure,
- and capital-return execution.
```

Therefore this run is safe as residual research, but should not become a positive weight patch until URL-level non-price evidence is repaired.

---

## 4. No-repeat and novelty check

Hard duplicate key:

```text
canonical_archetype_id + symbol + trigger_type + entry_date
```

Searches performed before writing:

```text
003690 + C22_INSURANCE_RATE_CYCLE_RESERVE -> no direct match found
082640 + C22_INSURANCE_RATE_CYCLE_RESERVE -> no direct match found
000370 + C22_INSURANCE_RATE_CYCLE_RESERVE -> no direct match found
```

Novelty accounting:

```json
{
  "new_symbol_count": 3,
  "minimum_new_symbol_count": 2,
  "minimum_positive_case_count": 1,
  "minimum_counterexample_count": 1,
  "new_independent_case_ratio": 1.00,
  "duplicate_status": "pass",
  "data_quality_status": "source_proxy_only_non_price_evidence"
}
```

---

## 5. Case design

| case_id | symbol | trigger family | research role |
|---|---|---|---|
| `R6L72_C22_003690_20240130` | `003690` 코리안리 | reinsurer reserve/rate-cycle rerating | stable positive / low-MAE anchor |
| `R6L72_C22_082640_20240130` | `082640` 동양생명 | life-insurer low-PBR / reserve-cycle rerating | high-MFE positive but evidence repair required |
| `R6L72_C22_000370_20240214` | `000370` 한화손해보험 | post-value-up insurance overheat / 4B local watch | counterexample / high-MAE guardrail |

The intended residual:

```text
C22 should allow Stage2/Yellow for low-PBR insurance rerating only when reserve/rate/capital-return evidence is repaired.
It should block Green or route to 4B/high-MAE watch when the entry occurs after the first insurance value-up spike and MAE expands before fresh non-price confirmation.
```

---

## 6. Stock-Web OHLC and backtest

### 6.1 `003690` 코리안리 — stable reinsurer positive anchor

Trigger:

```text
trigger_date = 2024-01-29
trigger_type = Stage2-Actionable
trigger_family = reinsurer_reserve_rate_cycle_low_pbr_rerating
entry_date = 2024-01-30
entry_price = 7410.0
entry_price_type = next_tradable_open
```

Relevant Stock-Web rows:

```csv
d,o,h,l,c,v,a,mc,s,m
2024-01-29,7230.0,7410.0,7180.0,7400.0,399538.0,2933656470.0,1223719692400.0,165367526,KOSPI
2024-01-30,7410.0,7480.0,7360.0,7380.0,496052.0,3681963670.0,1220412341880.0,165367526,KOSPI
2024-02-01,7580.0,7960.0,7470.0,7810.0,1308385.0,10268194140.0,1291520378060.0,165367526,KOSPI
2024-02-19,8010.0,8330.0,8010.0,8190.0,969875.0,7929746500.0,1354360037940.0,165367526,KOSPI
2024-03-07,8130.0,8420.0,8080.0,8350.0,976201.0,8148942580.0,1380818842100.0,165367526,KOSPI
2024-03-22,8360.0,8550.0,8340.0,8510.0,486073.0,4105826600.0,1407277646260.0,165367526,KOSPI
2024-07-18,7980.0,8350.0,7920.0,8340.0,930436.0,7682142000.0,1379165166840.0,165367526,KOSPI
2024-07-30,8220.0,8500.0,8200.0,8440.0,543290.0,4575376080.0,1395701919440.0,165367526,KOSPI
```

Backtest:

| window | peak/high | peak date | trough/low | trough date | MFE | MAE |
|---|---:|---|---:|---|---:|---:|
| 30 calendar days | 8330 | 2024-02-19 | 7360 | 2024-01-30 | +12.42% | -0.67% |
| 90 calendar days | 8550 | 2024-03-22 | 7360 | 2024-01-30 | +15.38% | -0.67% |
| 180 calendar days | 8550 | 2024-03-22 | 7360 | 2024-01-30 | +15.38% | -0.67% |

Interpretation:

```text
003690 is a clean low-MAE C22 positive-stable anchor.
The MFE was not explosive, but the drawdown profile was unusually controlled.
This is a Stage2/Yellow candidate only after reserve/rate-cycle evidence is repaired, not a Green-by-price case.
```

### 6.2 `082640` 동양생명 — life-insurer rerating with very strong MFE

Trigger:

```text
trigger_date = 2024-01-29
trigger_type = Stage2-Actionable
trigger_family = life_insurer_low_pbr_reserve_cycle_rerating
entry_date = 2024-01-30
entry_price = 4630.0
entry_price_type = next_tradable_open
```

Relevant Stock-Web rows:

```csv
d,o,h,l,c,v,a,mc,s,m
2024-01-29,4510.0,4640.0,4485.0,4630.0,218194.0,1002507445.0,747090248550.0,161358585,KOSPI
2024-01-30,4630.0,4940.0,4595.0,4850.0,795896.0,3824153210.0,782589137250.0,161358585,KOSPI
2024-02-01,4925.0,5480.0,4810.0,5380.0,1864697.0,9849106980.0,868109187300.0,161358585,KOSPI
2024-02-29,5550.0,5850.0,5540.0,5820.0,1081813.0,6246823460.0,939106964700.0,161358585,KOSPI
2024-03-04,5850.0,6150.0,5790.0,6140.0,834302.0,5024421630.0,990741711900.0,161358585,KOSPI
2024-06-18,5240.0,6810.0,5140.0,6500.0,9631424.0,61158634090.0,1048830802500.0,161358585,KOSPI
2024-06-28,7060.0,8220.0,7040.0,7820.0,7868539.0,60414969290.0,1261824134700.0,161358585,KOSPI
2024-07-02,7660.0,9340.0,7640.0,8450.0,10225276.0,89993017340.0,1363480043250.0,161358585,KOSPI
```

Backtest:

| window | peak/high | peak date | trough/low | trough date | MFE | MAE |
|---|---:|---|---:|---|---:|---:|
| 30 calendar days | 5850 | 2024-02-29 | 4595 | 2024-01-30 | +26.35% | -0.76% |
| 90 calendar days | 6150 | 2024-03-04 | 4595 | 2024-01-30 | +32.83% | -0.76% |
| 180 calendar days | 9340 | 2024-07-02 | 4595 | 2024-01-30 | +101.73% | -0.76% |

Interpretation:

```text
082640 is a high-MFE C22 positive, but it is not safe for production promotion while evidence remains proxy-only.
The price path is excellent, yet the model should require reserve quality, CSM/earnings visibility, and capital-return evidence before Green.
```

### 6.3 `000370` 한화손해보험 — post-spike 4B/high-MAE counterexample

Trigger:

```text
trigger_date = 2024-02-13
trigger_type = 4B-local-watch
trigger_family = post_valueup_insurance_overheat_high_mae
entry_date = 2024-02-14
entry_price = 5370.0
entry_price_type = next_tradable_open_after_overheat
```

Relevant Stock-Web rows:

```csv
d,o,h,l,c,v,a,mc,s,m
2024-01-30,4040.0,4365.0,4040.0,4325.0,1845725.0,7825374970.0,504895807375.0,116738915,KOSPI
2024-02-01,4320.0,5640.0,4150.0,5120.0,31984623.0,167160468105.0,597703244800.0,116738915,KOSPI
2024-02-13,5590.0,6170.0,5380.0,5520.0,22178568.0,129162465550.0,644398810800.0,116738915,KOSPI
2024-02-14,5370.0,5700.0,5240.0,5310.0,3592090.0,19516157450.0,619883638650.0,116738915,KOSPI
2024-02-28,4570.0,4790.0,4500.0,4725.0,1735197.0,8016707510.0,551591373375.0,116738915,KOSPI
2024-04-11,4310.0,4375.0,4205.0,4285.0,323628.0,1384160425.0,500226250775.0,116738915,KOSPI
2024-07-31,5390.0,5720.0,5360.0,5650.0,1793708.0,10068154500.0,659574869750.0,116738915,KOSPI
2024-08-09,5310.0,6100.0,5230.0,5830.0,3154140.0,18060829110.0,680587874450.0,116738915,KOSPI
```

Backtest:

| window | peak/high | peak date | trough/low | trough date | MFE | MAE |
|---|---:|---|---:|---|---:|---:|
| 30 calendar days | 5700 | 2024-02-14 | 4500 | 2024-02-28 | +6.15% | -16.20% |
| 90 calendar days | 5700 | 2024-02-14 | 4205 | 2024-04-11 | +6.15% | -21.69% |
| 180 calendar days | 6100 | 2024-08-09 | 4205 | 2024-04-11 | +13.59% | -21.69% |

Interpretation:

```text
000370 is the counterexample branch.
The early value-up/insurance spike had already moved before the entry date.
After the overheat entry, MFE was small and MAE crossed -20%.
This should route to local 4B/high-MAE watch, not Stage2/Green.
```

---

## 7. Machine-readable trigger JSONL

```jsonl
{"row_type":"trigger","research_id":"R6L72_C22_INSURANCE_VALUEUP_RESERVE","round":"R6","loop":72,"large_sector_id":"L6_FINANCIAL_CAPITAL_RETURN_DIGITAL","canonical_archetype_id":"C22_INSURANCE_RATE_CYCLE_RESERVE","fine_archetype_id":"INSURANCE_VALUEUP_RESERVE_RATE_CYCLE_AND_POST_SPIKE_MAE","symbol":"003690","name":"코리안리","trigger_type":"Stage2-Actionable","trigger_family":"reinsurer_reserve_rate_cycle_low_pbr_rerating","trigger_date":"2024-01-29","entry_date":"2024-01-30","entry_price":7410.0,"entry_price_type":"next_tradable_open","price_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","mfe_30d_pct":12.42,"mae_30d_pct":-0.67,"mfe_90d_pct":15.38,"mae_90d_pct":-0.67,"mfe_180d_pct":15.38,"mae_180d_pct":-0.67,"peak_price_180d":8550.0,"peak_date_180d":"2024-03-22","trough_price_180d":7360.0,"trough_date_180d":"2024-01-30","calibration_usable":true,"case_polarity":"positive_stable","evidence_url_pending":true,"source_proxy_only":true,"non_price_evidence_strength":"medium_pending_url_repair","price_only_blowoff":false,"expected_stage_current_profile":"Stage2-Actionable_to_Yellow_if_reserve_rate_cycle_verified","residual_error_type":"low_MAE_stable_insurance_positive_but_green_requires_reserve_quality_proof"}
{"row_type":"trigger","research_id":"R6L72_C22_INSURANCE_VALUEUP_RESERVE","round":"R6","loop":72,"large_sector_id":"L6_FINANCIAL_CAPITAL_RETURN_DIGITAL","canonical_archetype_id":"C22_INSURANCE_RATE_CYCLE_RESERVE","fine_archetype_id":"INSURANCE_VALUEUP_RESERVE_RATE_CYCLE_AND_POST_SPIKE_MAE","symbol":"082640","name":"동양생명","trigger_type":"Stage2-Actionable","trigger_family":"life_insurer_low_pbr_reserve_cycle_rerating","trigger_date":"2024-01-29","entry_date":"2024-01-30","entry_price":4630.0,"entry_price_type":"next_tradable_open","price_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","mfe_30d_pct":26.35,"mae_30d_pct":-0.76,"mfe_90d_pct":32.83,"mae_90d_pct":-0.76,"mfe_180d_pct":101.73,"mae_180d_pct":-0.76,"peak_price_180d":9340.0,"peak_date_180d":"2024-07-02","trough_price_180d":4595.0,"trough_date_180d":"2024-01-30","calibration_usable":true,"case_polarity":"positive_high_mfe","evidence_url_pending":true,"source_proxy_only":true,"non_price_evidence_strength":"medium_pending_url_repair","price_only_blowoff":false,"expected_stage_current_profile":"Stage2-Actionable_to_Yellow_or_4B_watch_until_reserve_capital_return_verified","residual_error_type":"high_MFE_insurance_rerating_requires_reserve_CSM_capital_return_evidence_before_green"}
{"row_type":"trigger","research_id":"R6L72_C22_INSURANCE_VALUEUP_RESERVE","round":"R6","loop":72,"large_sector_id":"L6_FINANCIAL_CAPITAL_RETURN_DIGITAL","canonical_archetype_id":"C22_INSURANCE_RATE_CYCLE_RESERVE","fine_archetype_id":"INSURANCE_VALUEUP_RESERVE_RATE_CYCLE_AND_POST_SPIKE_MAE","symbol":"000370","name":"한화손해보험","trigger_type":"4B-local-watch","trigger_family":"post_valueup_insurance_overheat_high_mae","trigger_date":"2024-02-13","entry_date":"2024-02-14","entry_price":5370.0,"entry_price_type":"next_tradable_open_after_overheat","price_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","mfe_30d_pct":6.15,"mae_30d_pct":-16.20,"mfe_90d_pct":6.15,"mae_90d_pct":-21.69,"mfe_180d_pct":13.59,"mae_180d_pct":-21.69,"peak_price_180d":6100.0,"peak_date_180d":"2024-08-09","trough_price_180d":4205.0,"trough_date_180d":"2024-04-11","calibration_usable":true,"case_polarity":"counterexample_high_mae","evidence_url_pending":true,"source_proxy_only":true,"non_price_evidence_strength":"low_pending_url_repair","price_only_blowoff":false,"expected_stage_current_profile":"4B_local_watch_or_blocked_positive_stage","residual_error_type":"post_spike_insurance_entry_small_MFE_high_MAE"}
```

---

## 8. Score simulation and raw component breakdown

This is shadow-only and does not change production scoring.

| symbol | EPS/FCF | reserve/CSM quality | rate-cycle visibility | ROE/PBR mispricing | capital return | valuation rerating | information confidence | shadow total | intended route |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| `003690` | 7 | 12 | 13 | 10 | 6 | 8 | 7 | 63 | Stage2/Yellow only after reserve/rate evidence repair |
| `082640` | 9 | 11 | 10 | 15 | 7 | 16 | 6 | 74 | Stage2/Yellow, possible 4B watch; no Green until evidence repair |
| `000370` | 7 | 7 | 8 | 13 | 5 | 12 | 5 | 57 | local 4B/high-MAE watch; no positive promotion |

### Current calibrated profile stress test

The current calibrated profile already blocks price-only blowoff.  
The remaining C22 problem is **timing and evidence quality**:

```text
C22 stable positive path:
  low-PBR insurance rerating
  + low MAE
  + reserve/rate/capital-return evidence repaired
  => Stage2-Actionable / Stage3-Yellow

C22 high-MFE but proxy-only path:
  strong price response
  + evidence still proxy-only
  + possible event/valuation overlay
  => Stage2-Guarded / Yellow at most; no Green

C22 post-spike high-MAE path:
  entry after first value-up/insurance spike
  + small remaining MFE
  + MAE worse than -20%
  => local 4B/high-MAE watch or blocked positive stage
```

The important distinction is that `003690` and `082640` have low early MAE, while the late `000370` entry shows the “chase-after-spike” failure mode.

---

## 9. Aggregate metrics

```json
{
  "row_type": "aggregate",
  "research_id": "R6L72_C22_INSURANCE_VALUEUP_RESERVE",
  "round": "R6",
  "loop": 72,
  "large_sector_id": "L6_FINANCIAL_CAPITAL_RETURN_DIGITAL",
  "canonical_archetype_id": "C22_INSURANCE_RATE_CYCLE_RESERVE",
  "fine_archetype_id": "INSURANCE_VALUEUP_RESERVE_RATE_CYCLE_AND_POST_SPIKE_MAE",
  "case_count": 3,
  "calibration_usable_case_count": 3,
  "positive_stable_case_count": 1,
  "positive_high_mfe_case_count": 1,
  "counterexample_count": 1,
  "new_symbol_count": 3,
  "source_proxy_only_count": 3,
  "evidence_url_pending_count": 3,
  "avg_mfe_30d_pct": 14.97,
  "avg_mae_30d_pct": -5.88,
  "avg_mfe_90d_pct": 18.12,
  "avg_mae_90d_pct": -7.71,
  "avg_mfe_180d_pct": 43.57,
  "avg_mae_180d_pct": -7.71,
  "worst_mae_180d_pct": -21.69
}
```

---

## 10. Shadow rule candidate

```yaml
row_type: canonical_archetype_rule_candidate
canonical_archetype_id: C22_INSURANCE_RATE_CYCLE_RESERVE
fine_archetype_id: INSURANCE_VALUEUP_RESERVE_RATE_CYCLE_AND_POST_SPIKE_MAE
rule_name: C22_insurance_reserve_rate_cycle_evidence_and_high_mae_router
production_scoring_changed: false
shadow_weight_only: true
```

### Proposed routing logic

```text
For C22 insurance reserve/rate-cycle cases:

Tier A: verified reserve/rate/capital-return rerating
  Conditions:
    - low-PBR insurance rerating
    - reserve quality / CSM / loss-ratio / rate-cycle evidence is URL-repaired
    - 30D/90D MAE remains contained
  Routing:
    - Stage2-Actionable allowed
    - Stage3-Yellow allowed
    - Green only after reserve quality and capital-return evidence are verified

Tier B: high-MFE but source-proxy-only insurance rerating
  Conditions:
    - price path is strong
    - evidence is not URL-repaired
    - possible valuation or event overlay exists
  Routing:
    - Stage2-Actionable-Guarded or Yellow at most
    - no production weight promotion
    - no Green

Tier C: post-spike high-MAE insurance chase
  Conditions:
    - trigger/entry occurs after first value-up/insurance rerating spike
    - 90D or 180D MAE worse than -20%
    - no fresh reserve/capital-return evidence
  Routing:
    - local 4B/high-MAE watch
    - block positive Stage2/Green promotion
    - count as counterexample
```

### Suggested shadow delta

```json
{
  "row_type": "shadow_weight",
  "axis": "c22_insurance_reserve_rate_cycle_evidence_and_high_mae_router",
  "scope": "canonical_archetype_id:C22_INSURANCE_RATE_CYCLE_RESERVE",
  "proposal": {
    "source_proxy_only_green_allowed": false,
    "reserve_csm_capital_return_required_for_green": true,
    "stage2_guarded_allowed_when_30d_mae_contained": true,
    "post_spike_high_mae_watch_threshold_pct": -20.0,
    "positive_weight_blocked_until_url_repair": true
  },
  "confidence": "medium_low_until_url_repair",
  "apply_now": false,
  "reason": "Three new C22 insurance cases show useful separation between low-MAE rerating paths and a post-spike high-MAE entry. However all non-price evidence remains URL-pending, so this is a guardrail candidate rather than a positive promotion candidate."
}
```

---

## 11. Residual contribution summary

```json
{
  "row_type": "residual_contribution",
  "research_id": "R6L72_C22_INSURANCE_VALUEUP_RESERVE",
  "large_sector_id": "L6_FINANCIAL_CAPITAL_RETURN_DIGITAL",
  "canonical_archetype_id": "C22_INSURANCE_RATE_CYCLE_RESERVE",
  "contribution": "Adds three less-repeated C22 insurance cases and separates stable low-MAE reserve/rate-cycle rerating from post-value-up overheat entries that produce small remaining MFE and high MAE.",
  "positive_case_added": 2,
  "counterexample_case_added": 1,
  "new_symbol_count": 3,
  "data_quality_blocker": "All three non-price insurance triggers require URL-level repair before positive weight promotion.",
  "guardrail_added": "C22 Green requires verified reserve/CSM/rate-cycle/capital-return evidence; post-spike insurance entries with MAE worse than -20% should route to local 4B/high-MAE watch or blocked positive stage."
}
```

---

## 12. Validation scope

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
    082640: false
    000370: false
  evidence_url_pending:
    003690: true
    082640: true
    000370: true
  source_proxy_only:
    003690: true
    082640: true
    000370: true
```

Limitations:

```text
- Price path is validated against Stock-Web tradable OHLC rows.
- Non-price evidence is not URL-repaired in this run.
- Therefore this artifact is useful for C22 residual shape and high-MAE guardrail design, but should not promote positive weights until filings/IR/report data verifies reserve quality, CSM, rate-cycle, loss-ratio, ROE/PBR, or capital-return execution.
- It should not be read as a current investment view.
```

---

## 13. Deferred Coding Agent Handoff Prompt

Do not execute this prompt in the current research run.

```text
You are the later batch implementation agent for Songdaiki/stock_agent.

Read this MD as one v12 historical residual research artifact.

Task:
1. Ingest the machine-readable trigger rows.
2. Preserve R6 / loop 72 metadata.
3. Add the cases to C22_INSURANCE_RATE_CYCLE_RESERVE only if parser validation passes.
4. Treat all three non-price triggers as evidence_url_pending=true and source_proxy_only=true until URL-level evidence is repaired.
5. Do not use these rows for positive weight promotion until filings/IR/report data verifies reserve quality, CSM, loss-ratio, rate-cycle, ROE/PBR, or capital-return execution.
6. Add a shadow-only rule candidate named C22_insurance_reserve_rate_cycle_evidence_and_high_mae_router.
7. Do not loosen Stage3-Green.
8. Add C22-specific guards:
   - source_proxy_only -> no Green
   - post-spike entry with 90D/180D MAE <= -20% -> local 4B/high-MAE watch or blocked positive stage
   - Green requires reserve/CSM/capital-return evidence repair
9. Keep production scoring unchanged unless later batch promotion logic independently marks this axis safe.
```

---

## 14. Next round state

```text
completed_round = R6
completed_loop = 72
next_round = R7
next_loop = 72
next_large_sector_hint = L7_BIO_HEALTHCARE_MEDICAL
```
