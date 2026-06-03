# E2R Stock-Web v12 Residual Research — R2 Loop 72

```yaml
research_session: post_calibrated_sector_archetype_residual_research
mode: historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12
completed_round: R2
completed_loop: 72
next_round: R3
next_loop: 72
large_sector_id: L2_AI_SEMICONDUCTOR_ELECTRONICS
canonical_archetype_id: C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE
fine_archetype_id: MEMORY_CAPEX_RECOVERY_EQUIPMENT_AND_PROCESS_CONSUMABLES
output_file: e2r_stock_web_v12_residual_round_R2_loop_72_L2_AI_SEMICONDUCTOR_ELECTRONICS_C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE_research.md
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

The previous completed artifact in this automation chain was:

```text
completed_round = R1
completed_loop = 72
large_sector_id = L1_INDUSTRIALS_INFRA_DEFENSE_GRID
canonical_archetype_id = C01_ORDER_BACKLOG_MARGIN_BRIDGE
```

Therefore:

```text
scheduled_round = R2
scheduled_loop = 72
```

R2 maps to:

```text
large_sector_id = L2_AI_SEMICONDUCTOR_ELECTRONICS
```

This run selects:

```text
canonical_archetype_id = C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE
```

This is a valid R2/L2 pairing.

---

## 1. Why this R2/C10 run

The no-repeat ledger shows that C10 is relatively thinner than adjacent R2 HBM/socket/equipment archetypes:

```text
C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE:
  rows: 22
  symbols: 13
  date_range: 2023-03-17~2024-06-07
  good/bad S2: 9/4
  4B/4C: 2/0
  top covered symbols: 095610(4), 036930(3), 240810(3), 084370(2), 테스(2), 000660(1)
```

This run therefore adds three less-repeated C10 symbols:

```text
183300 코미코
281820 케이씨텍
319660 피에스케이
```

The research question is:

```text
Can C10 separate durable memory-capex recovery cases from equipment-cycle price spikes that later produce high MAE before verified order/earnings conversion?
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

| symbol | name | market | profile status | corporate-action contamination in tested 180D window | calibration usable |
|---|---|---|---|---|---|
| `183300` | 코미코 | KOSDAQ GLOBAL | active_like | none | true |
| `281820` | 케이씨텍 | KOSPI | active_like | none | true |
| `319660` | 피에스케이 | KOSDAQ GLOBAL | active_like | none in 2024 tested window; old 2022 events only | true |

Profile caveat:

```text
Stock-Web OHLC is raw/unadjusted marcap data. These cases are calibration-safe for the selected 2024 windows because no listed corporate-action candidate overlaps each entry~D+180 test window.
```

---

## 3. Evidence status and trigger discipline

The non-price evidence in this run is intentionally treated as `source_proxy_only = true` unless later batch implementation verifies exact DART/IR/report URLs.  
This keeps the run honest: the price path is fully validated through Stock-Web, but the order/earnings/revision evidence still needs URL-level repair before any production weight promotion.

Evidence proxy used:

```text
2024 memory-capex / semiconductor-equipment recovery regime,
visible in March~July 2024 through sector rotation, equipment/process-stock breakouts, and subsequent price confirmation.
```

C10 trigger interpretation:

```text
C10 does not require HBM-specific customer allocation like C06/C07.
It asks whether broad memory capex recovery is being translated into equipment/process-service revenue visibility.
```

This file therefore should be treated as:

```text
calibration_usable_price_path = true
non_price_evidence_needs_url_repair = true
promotion_blocker_until_url_repair = true
```

---

## 4. No-repeat and novelty check

Hard duplicate key:

```text
canonical_archetype_id + symbol + trigger_type + entry_date
```

Searches performed before writing:

```text
319660 + C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE -> no direct match found
281820 + C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE -> no direct match found
183300 + C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE -> no direct match found
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
| `R2L72_C10_183300_20240320` | `183300` 코미코 | process cleaning/coating recovery | positive Stage2/Yellow path with later drawdown guard |
| `R2L72_C10_281820_20240227` | `281820` 케이씨텍 | memory/CMP process-equipment recovery | positive but high-MAE after peak |
| `R2L72_C10_319660_20240401` | `319660` 피에스케이 | equipment-cycle breakout without durable follow-through | counterexample / high-MAE guard |

The intended residual:

```text
C10 should not treat every equipment-cycle breakout as Green.
It needs a separate confirmation branch:
- low-MAE early trend + repeat demand/earnings visibility -> Stage2/Yellow, possible Green later
- high-MAE after equipment-cycle spike without verified customer/order bridge -> Stage2-Guarded or 4B/high-MAE watch
```

---

## 6. Stock-Web OHLC and backtest

### 6.1 `183300` 코미코 — process-service recovery positive with later drawdown guard

Trigger:

```text
trigger_date = 2024-03-19
trigger_type = Stage2-Actionable
trigger_family = memory_process_cleaning_coating_recovery
entry_date = 2024-03-20
entry_price = 66500.0
entry_price_type = next_tradable_open
```

Relevant Stock-Web rows:

```csv
d,o,h,l,c,v,a,mc,s,m
2024-03-19,65700.0,70600.0,62800.0,66800.0,1088141.0,72989447600.0,698773691200.0,10460684,KOSDAQ GLOBAL
2024-03-20,66500.0,72100.0,64300.0,71300.0,352403.0,23970107600.0,745846769200.0,10460684,KOSDAQ GLOBAL
2024-03-21,74000.0,75800.0,70900.0,73000.0,356051.0,26049307600.0,763629932000.0,10460684,KOSDAQ GLOBAL
2024-04-18,85100.0,91200.0,82600.0,89000.0,258563.0,22646978400.0,931000876000.0,10460684,KOSDAQ GLOBAL
2024-05-16,97000.0,98400.0,91600.0,94400.0,351619.0,33282108100.0,987488569600.0,10460684,KOSDAQ GLOBAL
2024-06-25,79500.0,80300.0,77900.0,79100.0,129511.0,10194927600.0,827440104400.0,10460684,KOSDAQ GLOBAL
2024-09-06,56000.0,56800.0,54700.0,56500.0,100351.0,5597547600.0,591028646000.0,10460684,KOSDAQ GLOBAL
```

Backtest:

| window | peak/high | peak date | trough/low | trough date | MFE | MAE |
|---|---:|---|---:|---|---:|---:|
| 30 calendar days | 91200 | 2024-04-18 | 64300 | 2024-03-20 | +37.14% | -3.31% |
| 90 calendar days | 98400 | 2024-05-16 | 64300 | 2024-03-20 | +47.97% | -3.31% |
| 180 calendar days | 98400 | 2024-05-16 | 54700 | 2024-09-06 | +47.97% | -17.74% |

Interpretation:

```text
183300 is a usable C10 positive path, but not a free Green.
The early low-MAE trend supports Stage2-Actionable / Stage3-Yellow,
while the later 180D drawdown warns that Green should still require verified earnings/order conversion.
```

### 6.2 `281820` 케이씨텍 — process-equipment recovery with stronger MFE but high-MAE after peak

Trigger:

```text
trigger_date = 2024-02-26
trigger_type = Stage2-Actionable
trigger_family = memory_CMP_process_equipment_recovery
entry_date = 2024-02-27
entry_price = 38050.0
entry_price_type = next_tradable_open
```

Relevant Stock-Web rows:

```csv
d,o,h,l,c,v,a,mc,s,m
2024-02-26,32550.0,36100.0,32300.0,36100.0,605352.0,21267105100.0,753102171600.0,20861556,KOSPI
2024-02-27,38050.0,44700.0,34500.0,39200.0,2215249.0,86773423600.0,817772995200.0,20861556,KOSPI
2024-03-08,46850.0,54100.0,46850.0,50500.0,1513524.0,76147859550.0,1053508578000.0,20861556,KOSPI
2024-05-14,33300.0,33550.0,32350.0,33350.0,214661.0,7051909100.0,695732892600.0,20861556,KOSPI
2024-06-20,46300.0,50000.0,46300.0,48150.0,744173.0,36183143200.0,1004483921400.0,20861556,KOSPI
2024-07-11,52000.0,59000.0,51900.0,56500.0,612449.0,34524875200.0,1178677914000.0,20861556,KOSPI
2024-08-05,36500.0,37800.0,31000.0,33150.0,232519.0,8238318150.0,691560581400.0,20861556,KOSPI
```

Backtest:

| window | peak/high | peak date | trough/low | trough date | MFE | MAE |
|---|---:|---|---:|---|---:|---:|
| 30 calendar days | 54100 | 2024-03-08 | 34500 | 2024-02-27 | +42.18% | -9.33% |
| 90 calendar days | 54100 | 2024-03-08 | 32350 | 2024-05-14 | +42.18% | -14.98% |
| 180 calendar days | 59000 | 2024-07-11 | 31000 | 2024-08-05 | +55.06% | -18.53% |

Interpretation:

```text
281820 generated large MFE, but the same trigger family also produced post-peak MAE near -19%.
This supports Stage2-Actionable / Stage3-Yellow, but Green should require earnings/order durability,
not just a memory-equipment beta squeeze.
```

### 6.3 `319660` 피에스케이 — equipment-cycle spike without durable follow-through

Trigger:

```text
trigger_date = 2024-03-29
trigger_type = Stage2-Actionable-Guarded
trigger_family = equipment_cycle_breakout_without_confirmed_durable_bridge
entry_date = 2024-04-01
entry_price = 30800.0
entry_price_type = next_tradable_open
```

Relevant Stock-Web rows:

```csv
d,o,h,l,c,v,a,mc,s,m
2024-03-29,28850.0,30800.0,28450.0,30200.0,1044308.0,31384591800.0,874794762800.0,28966714,KOSDAQ GLOBAL
2024-04-01,30800.0,31200.0,29750.0,30000.0,460956.0,14023391350.0,869001420000.0,28966714,KOSDAQ GLOBAL
2024-04-17,31650.0,33500.0,31200.0,32350.0,646080.0,21035948250.0,937073197900.0,28966714,KOSDAQ GLOBAL
2024-05-10,29150.0,29150.0,27500.0,27850.0,422064.0,11820821750.0,806722984900.0,28966714,KOSDAQ GLOBAL
2024-06-19,36750.0,37100.0,35050.0,35400.0,444832.0,16038798850.0,1025421675600.0,28966714,KOSDAQ GLOBAL
2024-07-11,38550.0,39100.0,38100.0,38600.0,214271.0,8266493650.0,1118115160400.0,28966714,KOSDAQ GLOBAL
2024-09-19,21700.0,21700.0,20500.0,21250.0,253781.0,5339479550.0,615542672500.0,28966714,KOSDAQ GLOBAL
```

Backtest:

| window | peak/high | peak date | trough/low | trough date | MFE | MAE |
|---|---:|---|---:|---|---:|---:|
| 30 calendar days | 33500 | 2024-04-17 | 28550 | 2024-04-30 | +8.77% | -7.31% |
| 90 calendar days | 37100 | 2024-06-19 | 27500 | 2024-05-10 | +20.45% | -10.71% |
| 180 calendar days | 39100 | 2024-07-11 | 20500 | 2024-09-19 | +26.95% | -33.44% |

Interpretation:

```text
319660 is the key counterexample. The equipment-cycle breakout delivered acceptable MFE,
but the 180D path carried a -33% MAE before any durable bridge was verified in this run.
C10 should not Green this pattern without verified order/customer/earnings conversion.
```

---

## 7. Machine-readable trigger JSONL

```jsonl
{"row_type":"trigger","research_id":"R2L72_C10_MEMORY_RECOVERY_EQUIPMENT","round":"R2","loop":72,"large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE","fine_archetype_id":"MEMORY_CAPEX_RECOVERY_EQUIPMENT_AND_PROCESS_CONSUMABLES","symbol":"183300","name":"코미코","trigger_type":"Stage2-Actionable","trigger_family":"memory_process_cleaning_coating_recovery","trigger_date":"2024-03-19","entry_date":"2024-03-20","entry_price":66500.0,"entry_price_type":"next_tradable_open","price_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","mfe_30d_pct":37.14,"mae_30d_pct":-3.31,"mfe_90d_pct":47.97,"mae_90d_pct":-3.31,"mfe_180d_pct":47.97,"mae_180d_pct":-17.74,"peak_price_180d":98400.0,"peak_date_180d":"2024-05-16","trough_price_180d":54700.0,"trough_date_180d":"2024-09-06","calibration_usable":true,"case_polarity":"positive_guarded","evidence_url_pending":true,"source_proxy_only":true,"non_price_evidence_strength":"medium_pending_url_repair","price_only_blowoff":false,"expected_stage_current_profile":"Stage2-Actionable_to_Stage3-Yellow_until_earnings_bridge_verified","residual_error_type":"green_requires_verified_memory_recovery_revenue_bridge"}
{"row_type":"trigger","research_id":"R2L72_C10_MEMORY_RECOVERY_EQUIPMENT","round":"R2","loop":72,"large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE","fine_archetype_id":"MEMORY_CAPEX_RECOVERY_EQUIPMENT_AND_PROCESS_CONSUMABLES","symbol":"281820","name":"케이씨텍","trigger_type":"Stage2-Actionable","trigger_family":"memory_CMP_process_equipment_recovery","trigger_date":"2024-02-26","entry_date":"2024-02-27","entry_price":38050.0,"entry_price_type":"next_tradable_open","price_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","mfe_30d_pct":42.18,"mae_30d_pct":-9.33,"mfe_90d_pct":42.18,"mae_90d_pct":-14.98,"mfe_180d_pct":55.06,"mae_180d_pct":-18.53,"peak_price_180d":59000.0,"peak_date_180d":"2024-07-11","trough_price_180d":31000.0,"trough_date_180d":"2024-08-05","calibration_usable":true,"case_polarity":"positive_guarded","evidence_url_pending":true,"source_proxy_only":true,"non_price_evidence_strength":"medium_pending_url_repair","price_only_blowoff":false,"expected_stage_current_profile":"Stage2-Actionable_to_Yellow_high_MAE_guard","residual_error_type":"large_MFE_but_green_requires_order_or_margin_conversion"}
{"row_type":"trigger","research_id":"R2L72_C10_MEMORY_RECOVERY_EQUIPMENT","round":"R2","loop":72,"large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE","fine_archetype_id":"MEMORY_CAPEX_RECOVERY_EQUIPMENT_AND_PROCESS_CONSUMABLES","symbol":"319660","name":"피에스케이","trigger_type":"Stage2-Actionable-Guarded","trigger_family":"equipment_cycle_breakout_without_confirmed_durable_bridge","trigger_date":"2024-03-29","entry_date":"2024-04-01","entry_price":30800.0,"entry_price_type":"next_tradable_open","price_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","mfe_30d_pct":8.77,"mae_30d_pct":-7.31,"mfe_90d_pct":20.45,"mae_90d_pct":-10.71,"mfe_180d_pct":26.95,"mae_180d_pct":-33.44,"peak_price_180d":39100.0,"peak_date_180d":"2024-07-11","trough_price_180d":20500.0,"trough_date_180d":"2024-09-19","calibration_usable":true,"case_polarity":"counterexample","evidence_url_pending":true,"source_proxy_only":true,"non_price_evidence_strength":"low_pending_url_repair","price_only_blowoff":false,"expected_stage_current_profile":"Stage2-Guarded_or_4B_high_MAE_watch","residual_error_type":"equipment_cycle_breakout_high_MAE_without_durable_bridge"}
```

---

## 8. Score simulation and raw component breakdown

This is shadow-only and does not change production scoring.

| symbol | EPS/FCF | earnings visibility | equipment/order visibility | market mispricing | valuation rerating | capital allocation | information confidence | shadow total | intended route |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| `183300` | 11 | 13 | 12 | 10 | 10 | 4 | 9 | 69 | Stage2/Yellow until verified revenue bridge |
| `281820` | 10 | 12 | 13 | 12 | 12 | 4 | 8 | 71 | Stage2/Yellow, high-MAE guard before Green |
| `319660` | 7 | 8 | 8 | 9 | 8 | 3 | 6 | 49 | Stage2-Guarded / 4B-watch; no Green |

### Current calibrated profile stress test

The current calibrated profile already blocks price-only blowoff.  
The remaining C10 risk is different: **non-price theme is plausible, but evidence can be too broad or proxy-like**.

```text
C10 false-positive mode:
  broad memory capex recovery narrative
  + equipment stock breakout
  + no verified order/customer/earnings bridge
  + 180D MAE worse than -20%
  => should not Green

C10 cleaner positive mode:
  process/equipment recovery
  + low early MAE
  + subsequent MFE
  + later verified revenue/OP bridge
  => Stage2/Yellow, then Green only after verification
```

---

## 9. Aggregate metrics

```json
{
  "row_type": "aggregate",
  "research_id": "R2L72_C10_MEMORY_RECOVERY_EQUIPMENT",
  "round": "R2",
  "loop": 72,
  "large_sector_id": "L2_AI_SEMICONDUCTOR_ELECTRONICS",
  "canonical_archetype_id": "C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE",
  "fine_archetype_id": "MEMORY_CAPEX_RECOVERY_EQUIPMENT_AND_PROCESS_CONSUMABLES",
  "case_count": 3,
  "calibration_usable_case_count": 3,
  "positive_guarded_case_count": 2,
  "counterexample_count": 1,
  "new_symbol_count": 3,
  "source_proxy_only_count": 3,
  "evidence_url_pending_count": 3,
  "avg_mfe_30d_pct": 29.36,
  "avg_mae_30d_pct": -6.65,
  "avg_mfe_90d_pct": 36.87,
  "avg_mae_90d_pct": -9.67,
  "avg_mfe_180d_pct": 43.33,
  "avg_mae_180d_pct": -23.24,
  "worst_mae_180d_pct": -33.44
}
```

---

## 10. Shadow rule candidate

```yaml
row_type: canonical_archetype_rule_candidate
canonical_archetype_id: C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE
fine_archetype_id: MEMORY_CAPEX_RECOVERY_EQUIPMENT_AND_PROCESS_CONSUMABLES
rule_name: C10_memory_recovery_bridge_and_mae_router
production_scoring_changed: false
shadow_weight_only: true
```

### Proposed routing logic

```text
For C10 memory recovery equipment-cycle cases:

Tier A: verified recovery bridge
  Conditions:
    - memory capex recovery narrative is supported by company-level order, customer, revenue, or margin evidence
    - 30D/90D MAE remains contained
    - MFE is not purely one-day price beta
  Routing:
    - Stage2-Actionable allowed
    - Stage3-Yellow allowed
    - Green only after verified bridge / repeat evidence

Tier B: proxy-only recovery narrative
  Conditions:
    - sector memory recovery is plausible
    - symbol has equipment/process exposure
    - but evidence URL or direct order/earnings bridge is missing
  Routing:
    - Stage2-Actionable-Guarded
    - no Green
    - mark evidence_url_pending / source_proxy_only

Tier C: high-MAE equipment-cycle spike
  Conditions:
    - 180D MAE <= -20%
    - no verified durable bridge
  Routing:
    - 4B/high-MAE watch or false-positive counterexample
    - do not propose positive weight delta
```

### Suggested shadow delta

```json
{
  "row_type": "shadow_weight",
  "axis": "c10_memory_recovery_bridge_and_mae_router",
  "scope": "canonical_archetype_id:C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE",
  "proposal": {
    "verified_recovery_bridge_stage2_bonus": 1.0,
    "source_proxy_only_green_allowed": false,
    "evidence_url_pending_positive_weight_blocked": true,
    "high_mae_watch_threshold_pct": -20.0,
    "green_requires_order_customer_or_margin_bridge": true
  },
  "confidence": "medium_low_until_url_repair",
  "apply_now": false,
  "reason": "Three new C10 symbols show that memory recovery equipment-cycle rallies can produce useful MFE, but proxy-only evidence and high 180D MAE should block Green until direct company-level bridge evidence is verified."
}
```

---

## 11. Residual contribution summary

```json
{
  "row_type": "residual_contribution",
  "research_id": "R2L72_C10_MEMORY_RECOVERY_EQUIPMENT",
  "large_sector_id": "L2_AI_SEMICONDUCTOR_ELECTRONICS",
  "canonical_archetype_id": "C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE",
  "contribution": "Adds three less-repeated C10 memory recovery equipment/process cases and highlights that C10 should route source-proxy recovery narratives through Stage2-Guarded/Yellow rather than Green until direct order, customer, revenue, or margin bridge evidence is verified.",
  "positive_case_added": 2,
  "counterexample_case_added": 1,
  "new_symbol_count": 3,
  "data_quality_blocker": "All three non-price evidence triggers require URL-level repair before positive weight promotion.",
  "guardrail_added": "C10 Green requires verified company-level bridge; 180D MAE worse than -20% without verified bridge should route to high-MAE watch."
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
    183300: false
    281820: false
    319660: false
  evidence_url_pending:
    183300: true
    281820: true
    319660: true
  source_proxy_only:
    183300: true
    281820: true
    319660: true
```

Limitations:

```text
- Price path is validated against Stock-Web tradable OHLC rows.
- Non-price evidence is not URL-repaired in this run.
- Therefore this artifact is useful for C10 residual shape and high-MAE guardrail design, but should not promote positive weights until later DART/IR/report URLs are attached.
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
2. Preserve R2 / loop 72 metadata.
3. Add the cases to C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE only if parser validation passes.
4. Treat all three non-price triggers as evidence_url_pending=true and source_proxy_only=true until URL-level evidence is repaired.
5. Do not use these rows for positive weight promotion until DART/IR/report URLs verify company-level order, customer, revenue, or margin bridge evidence.
6. Add a shadow-only rule candidate named C10_memory_recovery_bridge_and_mae_router.
7. Do not loosen Stage3-Green.
8. Add the high-MAE guard:
   - if 180D MAE <= -20% and evidence is proxy-only, block Green and route to Stage2-Guarded or 4B/high-MAE watch.
9. Keep production scoring unchanged unless later batch promotion logic independently marks this axis safe.
```

---

## 14. Next round state

```text
completed_round = R2
completed_loop = 72
next_round = R3
next_loop = 72
next_large_sector_hint = L3_BATTERY_EV_GREEN_MOBILITY
```
