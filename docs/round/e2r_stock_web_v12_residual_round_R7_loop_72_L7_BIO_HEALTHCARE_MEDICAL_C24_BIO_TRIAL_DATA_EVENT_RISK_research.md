# E2R Stock-Web v12 Residual Research — R7 Loop 72

```yaml
research_session: post_calibrated_sector_archetype_residual_research
mode: historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12
completed_round: R7
completed_loop: 72
next_round: R8
next_loop: 72
large_sector_id: L7_BIO_HEALTHCARE_MEDICAL
canonical_archetype_id: C24_BIO_TRIAL_DATA_EVENT_RISK
fine_archetype_id: BIO_PLATFORM_TRIAL_OPTIONALITY_EVENT_AND_HIGH_MAE_GUARD
output_file: e2r_stock_web_v12_residual_round_R7_loop_72_L7_BIO_HEALTHCARE_MEDICAL_C24_BIO_TRIAL_DATA_EVENT_RISK_research.md
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
completed_round = R6
completed_loop = 72
large_sector_id = L6_FINANCIAL_CAPITAL_RETURN_DIGITAL
canonical_archetype_id = C22_INSURANCE_RATE_CYCLE_RESERVE
```

Therefore:

```text
scheduled_round = R7
scheduled_loop = 72
```

R7 maps to:

```text
large_sector_id = L7_BIO_HEALTHCARE_MEDICAL
```

This run selects:

```text
canonical_archetype_id = C24_BIO_TRIAL_DATA_EVENT_RISK
```

This is a valid R7/L7 pairing.

---

## 1. Why this R7/C24 run

The no-repeat ledger shows C24 still has a meaningful evidence-quality problem:

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

This run avoids those high-repeat symbols and adds:

```text
087010 펩트론
358570 지아이이노베이션
323990 박셀바이오
```

The residual question is:

```text
Can C24 separate bio-platform event optionality with strong follow-through from trial/data/event momentum that produces large early MFE but also high MAE?
```

This is especially important because C24 can easily overfit to headlines. In this archetype, the model must treat price as a flare, not as the proof. The proof has to come from trial data quality, endpoint clarity, partner validation, regulatory path, financing risk, and dilution control.

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
| `087010` | 펩트론 | KOSDAQ | active_like | none in 2024 test window; old 2018/2021 candidates only | true |
| `358570` | 지아이이노베이션 | KOSDAQ | active_like | Jan/Feb 2024 candidates are before the selected June 2024 entry window; no overlap with entry~D+180 | true |
| `323990` | 박셀바이오 | KOSDAQ | active_like | old 2021/2023 candidates only; no overlap with selected 2024 window | true |

Profile caveat:

```text
Stock-Web OHLC is raw/unadjusted marcap data. These cases are calibration-safe for the selected windows because no listed corporate-action candidate overlaps each entry~D+180 test window.
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
The Stock-Web price path is fully validated, but company-level clinical endpoint, data quality, partner validation, regulatory path, financing risk, and dilution risk evidence still require later URL repair through filings, company IR, trial registry, conference data, regulatory disclosure, or broker report evidence before any production weight promotion.
```

C24 interpretation used here:

```text
C24 is not simply “bio stock rose after a clinical headline.”
It asks whether an event has credible, repeatable non-price validation:
- endpoint or biomarker quality,
- trial design and population clarity,
- partner or regulatory validation,
- monetization path,
- financing runway,
- and dilution risk control.
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
087010 + C24_BIO_TRIAL_DATA_EVENT_RISK -> no direct match found
358570 + C24_BIO_TRIAL_DATA_EVENT_RISK -> no direct match found
323990 + C24_BIO_TRIAL_DATA_EVENT_RISK -> no direct match found
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
| `R7L72_C24_087010_20240627` | `087010` 펩트론 | bio-platform optionality with strong follow-through | positive high-MFE / low-MAE anchor |
| `R7L72_C24_358570_20240604` | `358570` 지아이이노베이션 | immunology/bio-event optionality with high-MAE before recovery | guarded counterexample / delayed recovery |
| `R7L72_C24_323990_20240522` | `323990` 박셀바이오 | cell-therapy event momentum with severe same-window MAE | event-spike counterexample |

The intended residual:

```text
C24 needs an event-quality router.
A bio platform can produce enormous MFE, but C24 should not Green a case from price alone.
Conversely, many clinical/data-event spikes show same-day or same-window MAE severe enough to require a 4B/high-MAE guard even when the headline initially works.
```

---

## 6. Stock-Web OHLC and backtest

### 6.1 `087010` 펩트론 — bio-platform optionality positive, but evidence still pending

Trigger:

```text
trigger_date = 2024-06-26
trigger_type = Stage2-Actionable-Guarded
trigger_family = bio_platform_partner_optional_event_followthrough
entry_date = 2024-06-27
entry_price = 37500.0
entry_price_type = next_tradable_open
```

Relevant Stock-Web rows:

```csv
d,o,h,l,c,v,a,mc,s,m
2024-06-26,39100.0,40150.0,36500.0,37950.0,482229.0,18219810700.0,783946432500.0,20657350,KOSDAQ
2024-06-27,37500.0,48000.0,37150.0,46500.0,3883153.0,170534089850.0,960566775000.0,20657350,KOSDAQ
2024-06-28,46400.0,49500.0,44800.0,49350.0,2237146.0,105827234400.0,1019440222500.0,20657350,KOSDAQ
2024-07-10,68000.0,76800.0,67800.0,71200.0,2832629.0,205609443500.0,1470803320000.0,20657350,KOSDAQ
2024-07-22,82000.0,83800.0,78200.0,81300.0,1856795.0,150699289900.0,1679442555000.0,20657350,KOSDAQ
2024-08-05,62500.0,64900.0,46750.0,53700.0,1414819.0,81097465500.0,1109299695000.0,20657350,KOSDAQ
2024-10-17,98300.0,104500.0,97100.0,100600.0,2956243.0,297990301000.0,2078129410000.0,20657350,KOSDAQ
2024-11-18,129500.0,132000.0,120000.0,125700.0,1486597.0,188376644000.0,2596628895000.0,20657350,KOSDAQ
```

Backtest:

| window | peak/high | peak date | trough/low | trough date | MFE | MAE |
|---|---:|---|---:|---|---:|---:|
| 30 calendar days | 83800 | 2024-07-22 | 37150 | 2024-06-27 | +123.47% | -0.93% |
| 90 calendar days | 83800 | 2024-07-22 | 37150 | 2024-06-27 | +123.47% | -0.93% |
| 180 calendar days | 132000 | 2024-11-18 | 37150 | 2024-06-27 | +252.00% | -0.93% |

Interpretation:

```text
087010 is the positive C24 anchor in this run.
The price path shows rare high-MFE / low-MAE behavior.
However, because non-price evidence is still URL-pending in this artifact, the correct label is Stage2-Actionable-Guarded / Yellow candidate, not automatic Green.
Green requires repaired evidence for partner validation, clinical/platform durability, regulatory path, and monetization quality.
```

### 6.2 `358570` 지아이이노베이션 — delayed recovery after high-MAE bio-event setup

Trigger:

```text
trigger_date = 2024-06-03
trigger_type = Stage2-Actionable-Guarded
trigger_family = immunology_bio_event_optional_with_high_mae_before_recovery
entry_date = 2024-06-04
entry_price = 11740.0
entry_price_type = next_tradable_open
```

Relevant Stock-Web rows:

```csv
d,o,h,l,c,v,a,mc,s,m
2024-06-03,11800.0,12120.0,11630.0,11700.0,381179.0,4524359080.0,517102840800.0,44196824,KOSDAQ
2024-06-04,11740.0,12210.0,11190.0,11380.0,1311897.0,15510617610.0,502959857120.0,44196824,KOSDAQ
2024-06-25,10180.0,10500.0,9920.0,10320.0,344674.0,3509880610.0,456111223680.0,44196824,KOSDAQ
2024-08-05,9990.0,10240.0,8510.0,8970.0,717439.0,6793563580.0,396445511280.0,44196824,KOSDAQ
2024-08-30,13060.0,14500.0,12850.0,14290.0,2826956.0,39130792000.0,631872519190.0,44217811,KOSDAQ
2024-10-16,15230.0,16340.0,14930.0,15100.0,2129720.0,33156924930.0,667688946100.0,44217811,KOSDAQ
2024-11-18,10760.0,10830.0,10040.0,10310.0,826442.0,8517181210.0,456782477690.0,44304799,KOSDAQ
2024-11-29,12150.0,12530.0,11310.0,11600.0,650480.0,7778577940.0,513935668400.0,44304799,KOSDAQ
```

Backtest:

| window | peak/high | peak date | trough/low | trough date | MFE | MAE |
|---|---:|---|---:|---|---:|---:|
| 30 calendar days | 12210 | 2024-06-04 | 9920 | 2024-06-25 | +4.00% | -15.50% |
| 90 calendar days | 14500 | 2024-08-30 | 8510 | 2024-08-05 | +23.51% | -27.51% |
| 180 calendar days | 16340 | 2024-10-16 | 8510 | 2024-08-05 | +39.18% | -27.51% |

Interpretation:

```text
358570 is not a clean positive despite eventual recovery.
The 30D/90D MAE sequence is the key signal: the path broke down before later recovery.
This should be Stage2-Actionable-Guarded at most while evidence is URL-pending, and it should carry a high-MAE gate before any Green promotion.
```

### 6.3 `323990` 박셀바이오 — event spike with severe same-window MAE

Trigger:

```text
trigger_date = 2024-05-21
trigger_type = 4B-local-watch
trigger_family = cell_therapy_event_momentum_same_day_high_mae
entry_date = 2024-05-22
entry_price = 19400.0
entry_price_type = next_tradable_open_after_event_momentum
```

Relevant Stock-Web rows:

```csv
d,o,h,l,c,v,a,mc,s,m
2024-05-20,17240.0,19800.0,17020.0,19050.0,1548726.0,29064914580.0,438020460000.0,22993200,KOSDAQ
2024-05-21,19100.0,19800.0,18890.0,19390.0,504977.0,9759257950.0,445838148000.0,22993200,KOSDAQ
2024-05-22,19400.0,25200.0,15060.0,25200.0,5138210.0,112377075550.0,579428640000.0,22993200,KOSDAQ
2024-05-23,22700.0,23500.0,20500.0,20950.0,6360722.0,141270404650.0,481707540000.0,22993200,KOSDAQ
2024-05-29,19980.0,20800.0,17740.0,18470.0,3903943.0,74639999460.0,424684404000.0,22993200,KOSDAQ
2024-08-05,15600.0,15690.0,13010.0,13670.0,405423.0,5895078700.0,314317044000.0,22993200,KOSDAQ
2024-10-25,12670.0,12670.0,12020.0,12200.0,183655.0,2252621460.0,280517040000.0,22993200,KOSDAQ
2024-11-13,11490.0,11700.0,11110.0,11330.0,117106.0,1327647150.0,260512956000.0,22993200,KOSDAQ
```

Backtest:

| window | peak/high | peak date | trough/low | trough date | MFE | MAE |
|---|---:|---|---:|---|---:|---:|
| 30 calendar days | 25200 | 2024-05-22 | 15060 | 2024-05-22 | +29.90% | -22.37% |
| 90 calendar days | 25200 | 2024-05-22 | 13010 | 2024-08-05 | +29.90% | -32.94% |
| 180 calendar days | 25200 | 2024-05-22 | 11110 | 2024-11-13 | +29.90% | -42.73% |

Interpretation:

```text
323990 is the clean C24 counterexample.
The same row generated large MFE and severe MAE. That is exactly the event-risk trap C24 must guard against.
This should route to 4B-local-watch / high-MAE guard, not Stage2/Green.
```

---

## 7. Machine-readable trigger JSONL

```jsonl
{"row_type":"trigger","research_id":"R7L72_C24_BIO_EVENT_HIGH_MAE","round":"R7","loop":72,"large_sector_id":"L7_BIO_HEALTHCARE_MEDICAL","canonical_archetype_id":"C24_BIO_TRIAL_DATA_EVENT_RISK","fine_archetype_id":"BIO_PLATFORM_TRIAL_OPTIONALITY_EVENT_AND_HIGH_MAE_GUARD","symbol":"087010","name":"펩트론","trigger_type":"Stage2-Actionable-Guarded","trigger_family":"bio_platform_partner_optional_event_followthrough","trigger_date":"2024-06-26","entry_date":"2024-06-27","entry_price":37500.0,"entry_price_type":"next_tradable_open","price_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","mfe_30d_pct":123.47,"mae_30d_pct":-0.93,"mfe_90d_pct":123.47,"mae_90d_pct":-0.93,"mfe_180d_pct":252.00,"mae_180d_pct":-0.93,"peak_price_180d":132000.0,"peak_date_180d":"2024-11-18","trough_price_180d":37150.0,"trough_date_180d":"2024-06-27","calibration_usable":true,"case_polarity":"positive_high_mfe_low_mae","evidence_url_pending":true,"source_proxy_only":true,"non_price_evidence_strength":"medium_pending_url_repair","price_only_blowoff":false,"expected_stage_current_profile":"Stage2-Actionable-Guarded_to_Yellow_if_platform_partner_evidence_repaired","residual_error_type":"price_path_positive_but_green_requires_repaired_partner_clinical_regulatory_evidence"}
{"row_type":"trigger","research_id":"R7L72_C24_BIO_EVENT_HIGH_MAE","round":"R7","loop":72,"large_sector_id":"L7_BIO_HEALTHCARE_MEDICAL","canonical_archetype_id":"C24_BIO_TRIAL_DATA_EVENT_RISK","fine_archetype_id":"BIO_PLATFORM_TRIAL_OPTIONALITY_EVENT_AND_HIGH_MAE_GUARD","symbol":"358570","name":"지아이이노베이션","trigger_type":"Stage2-Actionable-Guarded","trigger_family":"immunology_bio_event_optional_with_high_mae_before_recovery","trigger_date":"2024-06-03","entry_date":"2024-06-04","entry_price":11740.0,"entry_price_type":"next_tradable_open","price_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","mfe_30d_pct":4.00,"mae_30d_pct":-15.50,"mfe_90d_pct":23.51,"mae_90d_pct":-27.51,"mfe_180d_pct":39.18,"mae_180d_pct":-27.51,"peak_price_180d":16340.0,"peak_date_180d":"2024-10-16","trough_price_180d":8510.0,"trough_date_180d":"2024-08-05","calibration_usable":true,"case_polarity":"counterexample_delayed_recovery","evidence_url_pending":true,"source_proxy_only":true,"non_price_evidence_strength":"low_pending_url_repair","price_only_blowoff":false,"expected_stage_current_profile":"Stage2-Guarded_or_4B_high_MAE_watch_until_trial_partner_evidence_repaired","residual_error_type":"delayed_recovery_after_high_mae_should_not_green"}
{"row_type":"trigger","research_id":"R7L72_C24_BIO_EVENT_HIGH_MAE","round":"R7","loop":72,"large_sector_id":"L7_BIO_HEALTHCARE_MEDICAL","canonical_archetype_id":"C24_BIO_TRIAL_DATA_EVENT_RISK","fine_archetype_id":"BIO_PLATFORM_TRIAL_OPTIONALITY_EVENT_AND_HIGH_MAE_GUARD","symbol":"323990","name":"박셀바이오","trigger_type":"4B-local-watch","trigger_family":"cell_therapy_event_momentum_same_day_high_mae","trigger_date":"2024-05-21","entry_date":"2024-05-22","entry_price":19400.0,"entry_price_type":"next_tradable_open_after_event_momentum","price_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","mfe_30d_pct":29.90,"mae_30d_pct":-22.37,"mfe_90d_pct":29.90,"mae_90d_pct":-32.94,"mfe_180d_pct":29.90,"mae_180d_pct":-42.73,"peak_price_180d":25200.0,"peak_date_180d":"2024-05-22","trough_price_180d":11110.0,"trough_date_180d":"2024-11-13","calibration_usable":true,"case_polarity":"counterexample_high_mae","evidence_url_pending":true,"source_proxy_only":true,"non_price_evidence_strength":"low_pending_url_repair","price_only_blowoff":false,"expected_stage_current_profile":"4B_local_watch_or_blocked_positive_stage","residual_error_type":"same_window_mfe_and_mae_event_spike_should_not_stage2_green"}
```

---

## 8. Score simulation and raw component breakdown

This is shadow-only and does not change production scoring.

| symbol | clinical/platform evidence | endpoint/regulatory clarity | partner/monetization validation | market mispricing | valuation rerating | financing/dilution risk control | information confidence | shadow total | intended route |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| `087010` | 13 | 9 | 14 | 16 | 18 | 7 | 6 | 83 | Stage2-Guarded / Yellow after evidence repair; no auto-Green |
| `358570` | 8 | 6 | 7 | 9 | 9 | 4 | 5 | 48 | Stage2-Guarded or high-MAE watch |
| `323990` | 6 | 5 | 4 | 10 | 8 | 3 | 4 | 40 | 4B-local-watch / event-risk counterexample |

### Current calibrated profile stress test

The current calibrated profile already blocks price-only blowoff.  
The remaining C24 problem is **event evidence quality plus MAE sequencing**:

```text
C24 cleaner positive path:
  high-MFE / low-MAE path
  + repaired platform/partner/regulatory evidence
  + no immediate financing/dilution deterioration
  => Stage2-Actionable / Yellow; Green only after evidence repair

C24 high-MAE path:
  clinical/data/event headline
  + same-window or early-window MAE worse than -20%
  + source-proxy-only evidence
  => 4B-local-watch, high-MAE watch, or blocked positive stage
```

The key diagnostic is not MFE alone.  
`323990` shows that a single event candle can contain both the bull case and the red flag.  
`358570` shows that delayed recovery after a drawdown should not be treated like a clean positive.  
`087010` shows that the strongest C24 path still needs evidence repair before Green.

---

## 9. Aggregate metrics

```json
{
  "row_type": "aggregate",
  "research_id": "R7L72_C24_BIO_EVENT_HIGH_MAE",
  "round": "R7",
  "loop": 72,
  "large_sector_id": "L7_BIO_HEALTHCARE_MEDICAL",
  "canonical_archetype_id": "C24_BIO_TRIAL_DATA_EVENT_RISK",
  "fine_archetype_id": "BIO_PLATFORM_TRIAL_OPTIONALITY_EVENT_AND_HIGH_MAE_GUARD",
  "case_count": 3,
  "calibration_usable_case_count": 3,
  "positive_high_mfe_low_mae_case_count": 1,
  "counterexample_count": 2,
  "new_symbol_count": 3,
  "source_proxy_only_count": 3,
  "evidence_url_pending_count": 3,
  "avg_mfe_30d_pct": 52.46,
  "avg_mae_30d_pct": -12.93,
  "avg_mfe_90d_pct": 58.96,
  "avg_mae_90d_pct": -20.46,
  "avg_mfe_180d_pct": 107.03,
  "avg_mae_180d_pct": -23.72,
  "worst_mae_180d_pct": -42.73
}
```

---

## 10. Shadow rule candidate

```yaml
row_type: canonical_archetype_rule_candidate
canonical_archetype_id: C24_BIO_TRIAL_DATA_EVENT_RISK
fine_archetype_id: BIO_PLATFORM_TRIAL_OPTIONALITY_EVENT_AND_HIGH_MAE_GUARD
rule_name: C24_bio_event_evidence_repair_and_high_mae_router
production_scoring_changed: false
shadow_weight_only: true
```

### Proposed routing logic

```text
For C24 bio trial/data/event-risk cases:

Tier A: repaired high-quality platform/trial event
  Conditions:
    - high-MFE / low-MAE path
    - trial endpoint, platform, partner, regulatory, or monetization evidence is URL-repaired
    - financing/dilution risk is not deteriorating
  Routing:
    - Stage2-Actionable allowed
    - Stage3-Yellow allowed after evidence repair
    - Green only after repaired evidence and information confidence pass threshold

Tier B: source-proxy-only bio event
  Conditions:
    - event optionality exists
    - price response is strong
    - evidence_url_pending or source_proxy_only remains true
  Routing:
    - Stage2-Actionable-Guarded at most
    - no Green
    - no positive weight promotion

Tier C: high-MAE event spike
  Conditions:
    - 30D or 90D MAE <= -20%
    - same-window event candle or early drawdown dominates
    - evidence is not repaired
  Routing:
    - local 4B/high-MAE watch
    - count as counterexample
    - block positive stage promotion
```

### Suggested shadow delta

```json
{
  "row_type": "shadow_weight",
  "axis": "c24_bio_event_evidence_repair_and_high_mae_router",
  "scope": "canonical_archetype_id:C24_BIO_TRIAL_DATA_EVENT_RISK",
  "proposal": {
    "source_proxy_only_green_allowed": false,
    "evidence_url_pending_positive_weight_blocked": true,
    "green_requires_repaired_trial_partner_regulatory_evidence": true,
    "high_mae_watch_threshold_pct": -20.0,
    "same_window_mfe_mae_event_candle_blocks_stage2_green": true
  },
  "confidence": "medium_low_until_url_repair",
  "apply_now": false,
  "reason": "Three new C24 bio-event cases show that high-MFE/low-MAE platform optionality and high-MAE event spikes need separate routing. However all non-price evidence remains URL-pending, so this is a guardrail candidate rather than a positive promotion candidate."
}
```

---

## 11. Residual contribution summary

```json
{
  "row_type": "residual_contribution",
  "research_id": "R7L72_C24_BIO_EVENT_HIGH_MAE",
  "large_sector_id": "L7_BIO_HEALTHCARE_MEDICAL",
  "canonical_archetype_id": "C24_BIO_TRIAL_DATA_EVENT_RISK",
  "contribution": "Adds three less-repeated C24 bio-event cases and separates a high-MFE/low-MAE platform optionality path from high-MAE event-spike and delayed-recovery counterexamples.",
  "positive_case_added": 1,
  "counterexample_case_added": 2,
  "new_symbol_count": 3,
  "data_quality_blocker": "All three non-price bio-event triggers require URL-level repair before positive weight promotion.",
  "guardrail_added": "C24 Green requires repaired trial/platform/partner/regulatory evidence; source_proxy_only plus 30D/90D MAE worse than -20% should route to local 4B/high-MAE watch or blocked positive stage."
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
    087010: false
    358570: false
    323990: false
  evidence_url_pending:
    087010: true
    358570: true
    323990: true
  source_proxy_only:
    087010: true
    358570: true
    323990: true
```

Limitations:

```text
- Price path is validated against Stock-Web tradable OHLC rows.
- Non-price evidence is not URL-repaired in this run.
- Therefore this artifact is useful for C24 residual shape and high-MAE guardrail design, but should not promote positive weights until filings/IR/trial-registry/report data verifies trial quality, platform durability, partner validation, regulatory path, monetization, financing runway, and dilution risk.
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
2. Preserve R7 / loop 72 metadata.
3. Add the cases to C24_BIO_TRIAL_DATA_EVENT_RISK only if parser validation passes.
4. Treat all three non-price triggers as evidence_url_pending=true and source_proxy_only=true until URL-level evidence is repaired.
5. Do not use these rows for positive weight promotion until filings/IR/trial-registry/report data verifies trial quality, platform durability, partner validation, regulatory path, monetization, financing runway, and dilution risk.
6. Add a shadow-only rule candidate named C24_bio_event_evidence_repair_and_high_mae_router.
7. Do not loosen Stage3-Green.
8. Add C24-specific guards:
   - source_proxy_only -> no Green
   - 30D/90D MAE <= -20% without repaired evidence -> local 4B/high-MAE watch or blocked positive stage
   - same-window MFE/MAE event candle -> no Stage2/Green promotion without repaired evidence
   - Green requires repaired trial/platform/partner/regulatory evidence
9. Keep production scoring unchanged unless later batch promotion logic independently marks this axis safe.
```

---

## 14. Next round state

```text
completed_round = R7
completed_loop = 72
next_round = R8
next_loop = 72
next_large_sector_hint = L8_PLATFORM_CONTENT_SW_SECURITY
```
