# E2R Stock-Web v12 Residual Research — R8 Loop 72

```yaml
research_session: post_calibrated_sector_archetype_residual_research
mode: historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12
completed_round: R8
completed_loop: 72
next_round: R9
next_loop: 72
large_sector_id: L8_PLATFORM_CONTENT_SW_SECURITY
canonical_archetype_id: C28_SOFTWARE_SECURITY_CONTRACT_RETENTION
fine_archetype_id: AI_SOFTWARE_ENTERPRISE_CONTRACT_MONETIZATION_AND_POST_SPIKE_MAE
output_file: e2r_stock_web_v12_residual_round_R8_loop_72_L8_PLATFORM_CONTENT_SW_SECURITY_C28_SOFTWARE_SECURITY_CONTRACT_RETENTION_research.md
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

The active prompt explicitly fixes the research mode:

```text
primary_price_source = Songdaiki/stock-web
price_basis = tradable_raw
price_adjustment_status = raw_unadjusted_marcap

production_scoring_changed = false
shadow_weight_only = true
must_use_actual_stock_web_1D_OHLC = true
must_output_every_usable_trigger_as_jsonl = true
```

### Round resolution

The immediately preceding completed scheduled artifact in this automation chain was:

```text
completed_round = R7
completed_loop = 72
large_sector_id = L7_BIO_HEALTHCARE_MEDICAL
canonical_archetype_id = C24_BIO_TRIAL_DATA_EVENT_RISK
```

Therefore:

```text
scheduled_round = R8
scheduled_loop = 72
```

R8 maps to:

```text
large_sector_id = L8_PLATFORM_CONTENT_SW_SECURITY
```

This run selects:

```text
canonical_archetype_id = C28_SOFTWARE_SECURITY_CONTRACT_RETENTION
```

This is a valid R8/L8 pairing.

---

## 1. Why this R8/C28 run

The no-repeat ledger shows C28 is meaningfully covered, but the top-covered names are concentrated in legacy security / support / enterprise software names:

```text
C28_SOFTWARE_SECURITY_CONTRACT_RETENTION:
  rows: 87
  symbols: 18
  date_range: 2019-05-27~2024-07-22
  good/bad S2: 26/6
  4B/4C: 21/3
  URL/proxy: 0/0
  top covered symbols: 012510(20), 053800(16), 263860(12), 030520(7), 131370(6), 042510(4)
```

This run avoids those high-repeat names and adds three less-repeated AI/software-enterprise cases:

```text
047560 이스트소프트
041020 폴라리스오피스
307950 현대오토에버
```

The residual question is:

```text
Can C28 separate AI/software narrative rerating from actual enterprise contract retention / recurring monetization?
```

C28 behaves like a subscription machine: the headline spark may light the wick, but durable value comes from renewal, retention, backlog, ARR-like visibility, enterprise spend, or embedded customer workflow. A one-time AI demo or theme rally can look like Stage2 for a few candles, then disappear like steam unless contract/revenue conversion arrives.

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
| `047560` | 이스트소프트 | KOSDAQ | active_like | none in 2024 window; old 2015 candidates only | true |
| `041020` | 폴라리스오피스 | KOSDAQ | active_like | none in 2024 window; old 2010/2017 candidates only | true |
| `307950` | 현대오토에버 | KOSPI | active_like | none in 2024 window; old 2021 candidate only | true |

Profile caveat:

```text
Stock-Web OHLC is raw/unadjusted marcap data. These cases are calibration-safe for the selected 2024 windows because no listed corporate-action candidate overlaps each entry~D+180 test window.
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
The Stock-Web price path is fully validated, but company-level contract renewal, enterprise customer win, ARR-like recurring revenue, security/enterprise retention, AI-product monetization, and margin conversion evidence still require later URL repair through filings, IR decks, product/customer disclosures, or reports before any production weight promotion.
```

C28 interpretation used here:

```text
C28 is not simply “software stock rose.”
It asks whether software/security enthusiasm is being converted into durable contract retention:
- recurring revenue or repeat enterprise demand,
- named customer or group-wide deployment,
- renewal/retention quality,
- RPO/backlog/order visibility,
- operating leverage,
- and information confidence.
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
047560 + C28_SOFTWARE_SECURITY_CONTRACT_RETENTION -> no direct match found
041020 + C28_SOFTWARE_SECURITY_CONTRACT_RETENTION -> no direct match found
307950 + C28_SOFTWARE_SECURITY_CONTRACT_RETENTION -> no direct match found
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
| `R8L72_C28_047560_20240108` | `047560` 이스트소프트 | AI software narrative breakout | high-MFE positive-guarded, later high-MAE warning |
| `R8L72_C28_041020_20240304` | `041020` 폴라리스오피스 | AI office/productivity second-spike | counterexample / weak follow-through + high MAE |
| `R8L72_C28_307950_20240613` | `307950` 현대오토에버 | enterprise IT / vehicle software monetization | contract-retention-style positive-guarded case |

The intended residual:

```text
C28 should separate:
1. enterprise software / workflow-embedded cases where contract retention and customer spending can support Stage2/Yellow; and
2. AI theme/software narrative spikes where price MFE appears before durable monetization evidence, then high MAE exposes the gap.
```

---

## 6. Stock-Web OHLC and backtest

### 6.1 `047560` 이스트소프트 — AI software narrative with large MFE and later high-MAE warning

Trigger:

```text
trigger_date = 2024-01-05
trigger_type = Stage2-Actionable-Guarded
trigger_family = ai_software_product_narrative_breakout
entry_date = 2024-01-08
entry_price = 23000.0
entry_price_type = next_tradable_open
```

Relevant Stock-Web rows:

```csv
d,o,h,l,c,v,a,mc,s,m
2024-01-05,15230.0,19740.0,15230.0,19740.0,4814096.0,89191932260.0,225192577680.0,11407932,KOSDAQ
2024-01-08,23000.0,25650.0,22100.0,25650.0,6325051.0,158425400910.0,292613455800.0,11407932,KOSDAQ
2024-01-19,31300.0,39100.0,30300.0,39100.0,4092225.0,140580045350.0,446050141200.0,11407932,KOSDAQ
2024-01-29,46100.0,49800.0,36500.0,41300.0,3100218.0,129853420800.0,471147591600.0,11407932,KOSDAQ
2024-05-09,27400.0,31500.0,27100.0,28000.0,5929429.0,173051485200.0,323941296000.0,11569332,KOSDAQ
2024-06-28,18200.0,18590.0,17770.0,18010.0,101308.0,1849838360.0,208941790320.0,11601432,KOSDAQ
2024-07-04,17520.0,17660.0,17180.0,17190.0,119426.0,2077311430.0,199428616080.0,11601432,KOSDAQ
2024-08-05,11630.0,11840.0,9950.0,10730.0,276969.0,2986632450.0,124508434160.0,11603992,KOSDAQ
```

Backtest:

| window | peak/high | peak date | trough/low | trough date | MFE | MAE |
|---|---:|---|---:|---|---:|---:|
| 30 calendar days | 49800 | 2024-01-29 | 22100 | 2024-01-08 | +116.52% | -3.91% |
| 90 calendar days | 49800 | 2024-01-29 | 22100 | 2024-01-08 | +116.52% | -3.91% |
| 180 calendar days | 49800 | 2024-01-29 | 17180 | 2024-07-04 | +116.52% | -25.30% |

Interpretation:

```text
047560 is a high-MFE C28 positive-guarded path, not an automatic Green.
The early price action was powerful, but the 180D path later printed -25.30% MAE.
This is the exact software/AI narrative trap: a product story can produce a fast rerating before contract retention, recurring revenue, and margin conversion are proven.
```

### 6.2 `041020` 폴라리스오피스 — AI office/productivity second-spike with weak follow-through

Trigger:

```text
trigger_date = 2024-02-29
trigger_type = Stage2-FalsePositive-Candidate
trigger_family = ai_office_productivity_second_spike_without_retention_bridge
entry_date = 2024-03-04
entry_price = 8350.0
entry_price_type = next_tradable_open_after_second_spike
```

Relevant Stock-Web rows:

```csv
d,o,h,l,c,v,a,mc,s,m
2024-02-29,6950.0,8230.0,6830.0,7940.0,39113326.0,303521212730.0,394820454120.0,49725498,KOSDAQ
2024-03-04,8350.0,8660.0,7860.0,8000.0,21699656.0,179288045740.0,397803984000.0,49725498,KOSDAQ
2024-03-06,8160.0,8960.0,7860.0,7970.0,24613916.0,207109203090.0,396312219060.0,49725498,KOSDAQ
2024-04-03,6350.0,6380.0,6100.0,6200.0,1203944.0,7484409140.0,308298087600.0,49725498,KOSDAQ
2024-04-11,5840.0,6090.0,5720.0,6060.0,676484.0,4029226510.0,301336517880.0,49725498,KOSDAQ
2024-05-14,9270.0,10550.0,8990.0,9030.0,51791776.0,513138639600.0,449021246940.0,49725498,KOSDAQ
2024-07-24,6560.0,6760.0,6520.0,6530.0,748218.0,4953341690.0,324707501940.0,49725498,KOSDAQ
2024-08-05,5950.0,5960.0,4500.0,4790.0,2576039.0,13333842845.0,238185135420.0,49725498,KOSDAQ
```

Backtest:

| window | peak/high | peak date | trough/low | trough date | MFE | MAE |
|---|---:|---|---:|---|---:|---:|
| 30 calendar days | 8960 | 2024-03-06 | 6100 | 2024-04-03 | +7.31% | -26.95% |
| 90 calendar days | 10550 | 2024-05-14 | 5720 | 2024-04-11 | +26.35% | -31.50% |
| 180 calendar days | 10550 | 2024-05-14 | 4500 | 2024-08-05 | +26.35% | -46.11% |

Interpretation:

```text
041020 is the clean C28 counterexample.
The second-spike entry had very weak 30D MFE and immediate high MAE.
Even after a later MFE recovery, the 180D path exposed severe drawdown.
This should be blocked from Stage3-Green unless URL-repaired evidence proves durable product monetization, enterprise retention, or repeat revenue.
```

### 6.3 `307950` 현대오토에버 — enterprise software / vehicle software positive-guarded case

Trigger:

```text
trigger_date = 2024-06-12
trigger_type = Stage2-Actionable-Guarded
trigger_family = enterprise_vehicle_software_group_contract_monetization
entry_date = 2024-06-13
entry_price = 148500.0
entry_price_type = next_tradable_open
```

Relevant Stock-Web rows:

```csv
d,o,h,l,c,v,a,mc,s,m
2024-06-12,147000.0,147500.0,146400.0,147300.0,36625.0,5379391100.0,4039552548600.0,27423982,KOSPI
2024-06-13,148500.0,153700.0,148000.0,152700.0,189125.0,28702680700.0,4187642051400.0,27423982,KOSPI
2024-06-18,157500.0,163000.0,156600.0,161700.0,388097.0,62102220400.0,4434457889400.0,27423982,KOSPI
2024-07-04,172600.0,178000.0,170500.0,174000.0,402884.0,70426365700.0,4771772868000.0,27423982,KOSPI
2024-07-11,177600.0,181900.0,175000.0,175000.0,168755.0,30102374000.0,4799196850000.0,27423982,KOSPI
2024-08-05,151100.0,154000.0,139700.0,144500.0,178185.0,26384993600.0,3962765399000.0,27423982,KOSPI
2024-11-19,144000.0,149800.0,142800.0,147900.0,246916.0,36282725000.0,4056006937800.0,27423982,KOSPI
2024-12-09,124100.0,128600.0,123800.0,124500.0,67183.0,8448124300.0,3414285759000.0,27423982,KOSPI
```

Backtest:

| window | peak/high | peak date | trough/low | trough date | MFE | MAE |
|---|---:|---|---:|---|---:|---:|
| 30 calendar days | 181900 | 2024-07-11 | 148000 | 2024-06-13 | +22.49% | -0.34% |
| 90 calendar days | 181900 | 2024-07-11 | 139700 | 2024-08-05 | +22.49% | -5.93% |
| 180 calendar days | 181900 | 2024-07-11 | 123800 | 2024-12-09 | +22.49% | -16.63% |

Interpretation:

```text
307950 is the contract-retention-style positive-guarded case in this run.
The path is less explosive than AI theme names, but its 30D/90D MAE profile is much more controlled.
That is what C28 should prefer: enterprise workflow embedding and recurring customer spend over one-shot narrative rerating.
Even here, Green still requires URL-repaired enterprise contract / margin / operating leverage evidence.
```

---

## 7. Machine-readable trigger JSONL

```jsonl
{"row_type":"trigger","research_id":"R8L72_C28_AI_SOFTWARE_CONTRACT_RETENTION","round":"R8","loop":72,"large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C28_SOFTWARE_SECURITY_CONTRACT_RETENTION","fine_archetype_id":"AI_SOFTWARE_ENTERPRISE_CONTRACT_MONETIZATION_AND_POST_SPIKE_MAE","symbol":"047560","name":"이스트소프트","trigger_type":"Stage2-Actionable-Guarded","trigger_family":"ai_software_product_narrative_breakout","trigger_date":"2024-01-05","entry_date":"2024-01-08","entry_price":23000.0,"entry_price_type":"next_tradable_open","price_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","mfe_30d_pct":116.52,"mae_30d_pct":-3.91,"mfe_90d_pct":116.52,"mae_90d_pct":-3.91,"mfe_180d_pct":116.52,"mae_180d_pct":-25.30,"peak_price_180d":49800.0,"peak_date_180d":"2024-01-29","trough_price_180d":17180.0,"trough_date_180d":"2024-07-04","calibration_usable":true,"case_polarity":"positive_guarded_high_mfe_high_mae","evidence_url_pending":true,"source_proxy_only":true,"non_price_evidence_strength":"medium_pending_url_repair","price_only_blowoff":false,"expected_stage_current_profile":"Stage2-Actionable-Guarded_or_4B_watch_until_contract_monetization_repaired","residual_error_type":"ai_software_narrative_high_mfe_later_high_mae_requires_contract_retention_proof"}
{"row_type":"trigger","research_id":"R8L72_C28_AI_SOFTWARE_CONTRACT_RETENTION","round":"R8","loop":72,"large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C28_SOFTWARE_SECURITY_CONTRACT_RETENTION","fine_archetype_id":"AI_SOFTWARE_ENTERPRISE_CONTRACT_MONETIZATION_AND_POST_SPIKE_MAE","symbol":"041020","name":"폴라리스오피스","trigger_type":"Stage2-FalsePositive-Candidate","trigger_family":"ai_office_productivity_second_spike_without_retention_bridge","trigger_date":"2024-02-29","entry_date":"2024-03-04","entry_price":8350.0,"entry_price_type":"next_tradable_open_after_second_spike","price_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","mfe_30d_pct":7.31,"mae_30d_pct":-26.95,"mfe_90d_pct":26.35,"mae_90d_pct":-31.50,"mfe_180d_pct":26.35,"mae_180d_pct":-46.11,"peak_price_180d":10550.0,"peak_date_180d":"2024-05-14","trough_price_180d":4500.0,"trough_date_180d":"2024-08-05","calibration_usable":true,"case_polarity":"counterexample_high_mae","evidence_url_pending":true,"source_proxy_only":true,"non_price_evidence_strength":"low_pending_url_repair","price_only_blowoff":false,"expected_stage_current_profile":"blocked_Stage2_or_4B_high_MAE_watch","residual_error_type":"second_spike_ai_office_entry_weak_30d_mfe_extreme_mae_without_retention_bridge"}
{"row_type":"trigger","research_id":"R8L72_C28_AI_SOFTWARE_CONTRACT_RETENTION","round":"R8","loop":72,"large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C28_SOFTWARE_SECURITY_CONTRACT_RETENTION","fine_archetype_id":"AI_SOFTWARE_ENTERPRISE_CONTRACT_MONETIZATION_AND_POST_SPIKE_MAE","symbol":"307950","name":"현대오토에버","trigger_type":"Stage2-Actionable-Guarded","trigger_family":"enterprise_vehicle_software_group_contract_monetization","trigger_date":"2024-06-12","entry_date":"2024-06-13","entry_price":148500.0,"entry_price_type":"next_tradable_open","price_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","mfe_30d_pct":22.49,"mae_30d_pct":-0.34,"mfe_90d_pct":22.49,"mae_90d_pct":-5.93,"mfe_180d_pct":22.49,"mae_180d_pct":-16.63,"peak_price_180d":181900.0,"peak_date_180d":"2024-07-11","trough_price_180d":123800.0,"trough_date_180d":"2024-12-09","calibration_usable":true,"case_polarity":"positive_guarded_enterprise_software","evidence_url_pending":true,"source_proxy_only":true,"non_price_evidence_strength":"medium_pending_url_repair","price_only_blowoff":false,"expected_stage_current_profile":"Stage2-Actionable_to_Yellow_if_enterprise_contract_margin_bridge_repaired","residual_error_type":"enterprise_software_path_better_mae_but_green_requires_retention_and_margin_evidence"}
```

---

## 8. Score simulation and raw component breakdown

This is shadow-only and does not change production scoring.

| symbol | recurring/contract visibility | enterprise/customer retention | product monetization | market mispricing | valuation rerating | operating leverage | information confidence | shadow total | intended route |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| `047560` | 6 | 5 | 10 | 18 | 18 | 6 | 5 | 68 | Stage2-Guarded / local 4B watch until monetization proof |
| `041020` | 4 | 4 | 7 | 10 | 9 | 4 | 4 | 42 | blocked Stage2 or high-MAE watch |
| `307950` | 12 | 14 | 11 | 9 | 8 | 9 | 8 | 71 | Stage2/Yellow after contract/margin evidence repair |

### Current calibrated profile stress test

The current calibrated profile already blocks pure price-only blowoff.  
The remaining C28 risk is more specific:

```text
C28 false-positive mode:
  AI software narrative
  + strong early MFE
  + no repaired enterprise contract / recurring revenue / retention evidence
  + 180D MAE worse than -25%
  => no Green, no positive weight promotion

C28 cleaner positive mode:
  enterprise workflow / group IT / vehicle software spend
  + contained 30D/90D MAE
  + contract or margin conversion evidence repaired
  => Stage2-Actionable / Yellow, then Green only after retention and operating leverage evidence
```

The useful diagnostic is not “software rose.”  
It is whether the stock behaves like a recurring contract engine or like a fireworks candle. `307950` looks closer to the contract engine; `041020` is the clean false-positive; `047560` is the ambiguous high-MFE case whose later MAE demands evidence repair before promotion.

---

## 9. Aggregate metrics

```json
{
  "row_type": "aggregate",
  "research_id": "R8L72_C28_AI_SOFTWARE_CONTRACT_RETENTION",
  "round": "R8",
  "loop": 72,
  "large_sector_id": "L8_PLATFORM_CONTENT_SW_SECURITY",
  "canonical_archetype_id": "C28_SOFTWARE_SECURITY_CONTRACT_RETENTION",
  "fine_archetype_id": "AI_SOFTWARE_ENTERPRISE_CONTRACT_MONETIZATION_AND_POST_SPIKE_MAE",
  "case_count": 3,
  "calibration_usable_case_count": 3,
  "positive_guarded_case_count": 2,
  "counterexample_count": 1,
  "new_symbol_count": 3,
  "source_proxy_only_count": 3,
  "evidence_url_pending_count": 3,
  "avg_mfe_30d_pct": 48.77,
  "avg_mae_30d_pct": -10.40,
  "avg_mfe_90d_pct": 55.12,
  "avg_mae_90d_pct": -13.78,
  "avg_mfe_180d_pct": 55.12,
  "avg_mae_180d_pct": -29.35,
  "worst_mae_180d_pct": -46.11
}
```

---

## 10. Shadow rule candidate

```yaml
row_type: canonical_archetype_rule_candidate
canonical_archetype_id: C28_SOFTWARE_SECURITY_CONTRACT_RETENTION
fine_archetype_id: AI_SOFTWARE_ENTERPRISE_CONTRACT_MONETIZATION_AND_POST_SPIKE_MAE
rule_name: C28_ai_software_contract_retention_and_high_mae_router
production_scoring_changed: false
shadow_weight_only: true
```

### Proposed routing logic

```text
For C28 software/security/contract-retention cases:

Tier A: verified enterprise contract-retention software
  Conditions:
    - named enterprise customer, renewal, group-wide deployment, recurring revenue, RPO, or contract backlog evidence
    - 30D/90D MAE remains contained
    - margin or operating leverage bridge is visible
  Routing:
    - Stage2-Actionable allowed
    - Stage3-Yellow allowed after evidence repair
    - Green only after retention, recurring revenue, and margin conversion evidence are repaired

Tier B: AI software/product narrative without contract proof
  Conditions:
    - product or AI narrative produces large early MFE
    - evidence_url_pending or source_proxy_only remains true
    - contract/retention/ARR-like evidence is missing
  Routing:
    - Stage2-Actionable-Guarded at most
    - local 4B watch if early MFE is large
    - no Green
    - no production positive weight promotion

Tier C: second-spike / post-theme high-MAE entry
  Conditions:
    - entry follows an already extended AI/software theme move
    - 30D or 90D MAE <= -20%
    - no repaired enterprise monetization evidence
  Routing:
    - blocked Stage2 or high-MAE watch
    - count as counterexample
```

### Suggested shadow delta

```json
{
  "row_type": "shadow_weight",
  "axis": "c28_ai_software_contract_retention_and_high_mae_router",
  "scope": "canonical_archetype_id:C28_SOFTWARE_SECURITY_CONTRACT_RETENTION",
  "proposal": {
    "source_proxy_only_green_allowed": false,
    "contract_retention_required_for_green": true,
    "recurring_revenue_or_enterprise_customer_bridge_required": true,
    "stage2_guarded_allowed_when_30d_mae_contained": true,
    "post_spike_high_mae_watch_threshold_pct": -20.0,
    "positive_weight_blocked_until_url_repair": true
  },
  "confidence": "medium_low_until_url_repair",
  "apply_now": false,
  "reason": "Three new C28 software cases show that AI/product narratives and enterprise software contract-retention paths have different MAE signatures. However all non-price evidence remains URL-pending, so this is a guardrail candidate rather than a positive promotion candidate."
}
```

---

## 11. Residual contribution summary

```json
{
  "row_type": "residual_contribution",
  "research_id": "R8L72_C28_AI_SOFTWARE_CONTRACT_RETENTION",
  "large_sector_id": "L8_PLATFORM_CONTENT_SW_SECURITY",
  "canonical_archetype_id": "C28_SOFTWARE_SECURITY_CONTRACT_RETENTION",
  "contribution": "Adds three less-repeated C28 software cases and separates AI software narrative rerating from enterprise contract-retention style monetization. Strong early MFE is not enough for Green; recurring revenue, customer retention, contract backlog, and margin conversion evidence must be repaired.",
  "positive_case_added": 2,
  "counterexample_case_added": 1,
  "new_symbol_count": 3,
  "data_quality_blocker": "All three non-price software triggers require URL-level repair before positive weight promotion.",
  "guardrail_added": "C28 Green requires repaired contract-retention/recurring-revenue/evidence; source_proxy_only plus 30D/90D MAE worse than -20% should route to local 4B/high-MAE watch or blocked positive stage."
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
    047560: false
    041020: false
    307950: false
  evidence_url_pending:
    047560: true
    041020: true
    307950: true
  source_proxy_only:
    047560: true
    041020: true
    307950: true
```

Limitations:

```text
- Price path is validated against Stock-Web tradable OHLC rows.
- Non-price evidence is not URL-repaired in this run.
- Therefore this artifact is useful for C28 residual shape and high-MAE guardrail design, but should not promote positive weights until filings/IR/product/customer/report data verifies enterprise customer wins, contract retention, recurring revenue, RPO/backlog, operating leverage, or margin conversion.
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
2. Preserve R8 / loop 72 metadata.
3. Add the cases to C28_SOFTWARE_SECURITY_CONTRACT_RETENTION only if parser validation passes.
4. Treat all three non-price triggers as evidence_url_pending=true and source_proxy_only=true until URL-level evidence is repaired.
5. Do not use these rows for positive weight promotion until filings/IR/product/customer/report data verifies enterprise contract retention, recurring revenue, renewal quality, RPO/backlog, operating leverage, or margin conversion.
6. Add a shadow-only rule candidate named C28_ai_software_contract_retention_and_high_mae_router.
7. Do not loosen Stage3-Green.
8. Add C28-specific guards:
   - source_proxy_only -> no Green
   - 30D/90D MAE <= -20% without repaired evidence -> local 4B/high-MAE watch or blocked positive stage
   - AI software narrative alone -> Stage2-Guarded at most
   - Green requires repaired contract-retention / recurring-revenue / enterprise-customer evidence
9. Keep production scoring unchanged unless later batch promotion logic independently marks this axis safe.
```

---

## 14. Next round state

```text
completed_round = R8
completed_loop = 72
next_round = R9
next_loop = 72
next_large_sector_hint = L3_BATTERY_EV_GREEN_MOBILITY or L9_CONSTRUCTION_REALESTATE_HOUSING
```
