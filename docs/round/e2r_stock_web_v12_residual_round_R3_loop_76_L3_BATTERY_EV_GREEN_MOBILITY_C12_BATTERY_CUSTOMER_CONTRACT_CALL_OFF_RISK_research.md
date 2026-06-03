# E2R Stock-Web v12 Residual Research — R3 Loop 76

```yaml
research_session: post_calibrated_sector_archetype_residual_research
mode: historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12
completed_round: R3
completed_loop: 76
next_round: R4
next_loop: 76
large_sector_id: L3_BATTERY_EV_GREEN_MOBILITY
canonical_archetype_id: C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK
fine_archetype_id: ELECTROLYTE_CNT_CAN_CUSTOMER_CONTRACT_LOCALIZATION_AND_CALL_OFF_HIGH_MAE_ROUTER
output_file: e2r_stock_web_v12_residual_round_R3_loop_76_L3_BATTERY_EV_GREEN_MOBILITY_C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK_research.md
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
completed_round = R2
completed_loop  = 76
large_sector_id = L2_AI_SEMICONDUCTOR_ELECTRONICS
canonical_archetype_id = C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE
```

Therefore:

```text
scheduled_round = R3
scheduled_loop  = 76
```

R3 maps to:

```text
large_sector_id = L3_BATTERY_EV_GREEN_MOBILITY
```

This run selects:

```text
canonical_archetype_id = C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK
fine_archetype_id = ELECTROLYTE_CNT_CAN_CUSTOMER_CONTRACT_LOCALIZATION_AND_CALL_OFF_HIGH_MAE_ROUTER
```

This is a valid R3/L3 pairing.

---

## 1. Why this R3/C12 run

The no-repeat ledger shows C12 is already covered, but top coverage is concentrated in separator / copper-foil / known customer-risk names:

```text
C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK:
  rows: 53
  symbols: 17
  date_range: 2023-01-26~2024-07-25
  good/bad S2: 13/2
  4B/4C: 10/5
  URL/proxy: 0/0
  top covered symbols: 393890(9), 361610(7), 011790(5), 336370(5), 006110(4), UNKNOWN_SYMBOL(4)
```

This file avoids those top-covered C12 symbols and adds customer-contract / call-off risk cases from electrolyte, CNT/conductive additive, and battery-can supply chains:

```text
348370 엔켐
121600 나노신소재
091580 상신이디피
```

Research question:

```text
Can C12 separate true battery customer-contract/localization rerating from customer-expansion labels where first-window MFE is real but later call-off, utilization, volume, and margin risk dominates?
```

C12 is a customer-contract bridge. A contract headline is the purchase order; Stage2 needs the shipment, the call-off schedule, the localization economics, margin conversion, and cash collection. If the customer slows releases, the first candle is only a promise, not a conveyor belt.

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
| `348370` | 엔켐 | active_like / KOSDAQ | none listed | true |
| `121600` | 나노신소재 | active_like / KOSDAQ | no 2024 overlap; latest listed candidate 2015-12-17 | true |
| `091580` | 상신이디피 | active_like / KOSDAQ | no 2024 overlap; latest listed candidate 2011-05-11 | true |

Profile caveat:

```text
Stock-Web OHLC is raw/unadjusted marcap data.
These cases are calibration-safe for the selected 2024 30D/90D/180D windows because no listed corporate-action candidate overlaps each entry~D+180 test window.
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
The Stock-Web price path is fully validated, but company-level customer contract quality, shipment/call-off schedule, localization benefit, electrolyte/CNT/can utilization, ASP/pass-through, inventory, working-capital, gross margin, and cash conversion evidence still require later URL repair through filings, IR decks, order disclosures, customer data, export data, or sell-side reports before production weight promotion.
```

C12 interpretation used here:

```text
C12 is not simply “battery supplier stock rose.”
It asks whether the customer contract is actually convertible:
- customer quality and contract duration,
- shipment and call-off schedule,
- localization or IRA/customer procurement relevance,
- utilization and volume pull-through,
- ASP/spread and input-cost pass-through,
- inventory / working-capital control,
- gross margin and cash-flow conversion,
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
348370 + C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK -> no direct match found
121600 + C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK -> no direct match found
091580 + C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK -> no direct match found
```

Novelty accounting:

```json
{
  "new_symbol_count": 3,
  "minimum_new_symbol_count": 2,
  "positive_guarded_case_count": 1,
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
| `R3L76_C12_348370_20240124` | `348370` 엔켐 | electrolyte customer localization / contract rerating | positive-guarded high-MFE |
| `R3L76_C12_121600_20240221` | `121600` 나노신소재 | CNT conductive-additive customer expansion / later call-off drawdown | first-window-MFE later-MAE counterexample |
| `R3L76_C12_091580_20240308` | `091580` 상신이디피 | battery-can customer relief / weak-MFE high-MAE | weak-MFE high-MAE counterexample |

The intended residual:

```text
C12 should separate:
1. electrolyte/localization paths where MFE becomes very large but still needs call-off and margin proof;
2. CNT/customer-expansion paths where early MFE is real yet later MAE shows call-off/utilization risk;
3. battery-can customer-contract relief paths where MFE stays weak and drawdown becomes severe.
```

---

## 6. Stock-Web OHLC and backtest

### 6.1 `348370` 엔켐 — electrolyte customer localization high-MFE guarded path

Trigger:

```text
trigger_date = 2024-01-23
trigger_type = Stage2-Actionable-Guarded
trigger_family = electrolyte_customer_contract_localization_high_mfe_guarded
entry_date = 2024-01-24
entry_price = 125000.0
entry_price_type = next_tradable_open_after_electrolyte_customer_localization_burst
```

Relevant Stock-Web rows:

```csv
d,o,h,l,c,v,a,mc,s,m
2024-01-23,102000.0,119400.0,101200.0,119400.0,2629550.0,296941820400.0,1983055019400.0,16608501,KOSDAQ
2024-01-24,125000.0,128300.0,110800.0,118500.0,2376486.0,282594418700.0,1968107368500.0,16608501,KOSDAQ
2024-01-26,110900.0,136800.0,107300.0,135500.0,2478208.0,312609828300.0,2250451885500.0,16608501,KOSDAQ
2024-02-21,338000.0,358500.0,304500.0,326500.0,1192247.0,397268428500.0,5608659445000.0,17178130,KOSDAQ
2024-04-08,360000.0,394500.0,342500.0,358000.0,2413652.0,904208343500.0,6586650470000.0,18398465,KOSDAQ
2024-06-26,227500.0,228000.0,208500.0,215500.0,691507.0,149167912500.0,4381232878500.0,20330547,KOSDAQ
2024-08-05,170000.0,173200.0,149000.0,156500.0,429529.0,69264417000.0,3248126826000.0,20754804,KOSDAQ
```

Backtest:

| window | peak/high | peak date | trough/low | trough date | MFE | MAE |
|---|---:|---|---:|---|---:|---:|
| 30 calendar days | 358500 | 2024-02-21 | 107300 | 2024-01-26 | +186.80% | -14.16% |
| 90 calendar days | 394500 | 2024-04-08 | 107300 | 2024-01-26 | +215.60% | -14.16% |
| 180 calendar days | 394500 | 2024-04-08 | 107300 | 2024-01-26 | +215.60% | -14.16% |

Interpretation:

```text
348370 is the C12 high-MFE holdout.
The electrolyte/localization story produced a very large price path, so C12 should not block this subtype.
However, the entry also carried double-digit MAE; Green still requires URL-repaired customer contract quality, call-off schedule, localization, utilization, and margin evidence.
```

### 6.2 `121600` 나노신소재 — CNT customer expansion first-window-MFE / later-MAE warning

Trigger:

```text
trigger_date = 2024-02-20
trigger_type = Stage2-Actionable-Guarded
trigger_family = cnt_conductive_additive_customer_expansion_initial_mfe_later_call_off_drawdown
entry_date = 2024-02-21
entry_price = 105000.0
entry_price_type = next_tradable_open_after_cnt_customer_expansion_burst
```

Relevant Stock-Web rows:

```csv
d,o,h,l,c,v,a,mc,s,m
2024-02-20,103100.0,106000.0,100000.0,104900.0,112286.0,11622260100.0,1275571202200.0,12159878,KOSDAQ
2024-02-21,105000.0,136300.0,104100.0,134000.0,1984511.0,251330823300.0,1629423652000.0,12159878,KOSDAQ
2024-02-22,133100.0,157800.0,130600.0,138000.0,1955332.0,281220563000.0,1678063164000.0,12159878,KOSDAQ
2024-03-18,145700.0,151000.0,145300.0,147600.0,464253.0,68940481400.0,1794797992800.0,12159878,KOSDAQ
2024-05-21,109500.0,110400.0,107100.0,108500.0,76785.0,8295633600.0,1323274463000.0,12196078,KOSDAQ
2024-08-05,87900.0,89700.0,68500.0,74900.0,264044.0,21196062100.0,913486242200.0,12196078,KOSDAQ
2024-09-02,91200.0,96100.0,90800.0,95500.0,209806.0,19778185000.0,1164725449000.0,12196078,KOSDAQ
```

Backtest:

| window | peak/high | peak date | trough/low | trough date | MFE | MAE |
|---|---:|---|---:|---|---:|---:|
| 30 calendar days | 157800 | 2024-02-22 | 104100 | 2024-02-21 | +50.29% | -0.86% |
| 90 calendar days | 157800 | 2024-02-22 | 104100 | 2024-02-21 | +50.29% | -0.86% |
| 180 calendar days | 157800 | 2024-02-22 | 68500 | 2024-08-05 | +50.29% | -34.76% |

Interpretation:

```text
121600 is the first-window-MFE / later-MAE branch.
The first month looked strong, but the 180D path shows why C12 needs a call-off and customer-volume guard.
This should remain Stage2-Guarded or local 4B watch until customer release schedule, CNT volume, utilization, and margin evidence are repaired.
```

### 6.3 `091580` 상신이디피 — battery-can customer-contract relief weak-MFE / high-MAE counterexample

Trigger:

```text
trigger_date = 2024-03-07
trigger_type = Stage2-FalsePositive-Candidate
trigger_family = battery_can_customer_contract_relief_weak_mfe_high_mae
entry_date = 2024-03-08
entry_price = 18790.0
entry_price_type = next_tradable_open_after_battery_can_customer_relief_spike
```

Relevant Stock-Web rows:

```csv
d,o,h,l,c,v,a,mc,s,m
2024-03-07,15950.0,19440.0,15810.0,18000.0,3526915.0,64200433390.0,245307942000.0,13628219,KOSDAQ
2024-03-08,18790.0,19320.0,17830.0,18390.0,1785418.0,33326694850.0,250622947410.0,13628219,KOSDAQ
2024-03-20,19180.0,20700.0,19070.0,19480.0,1377974.0,27512495350.0,265477706120.0,13628219,KOSDAQ
2024-05-30,14500.0,14710.0,14000.0,14550.0,94453.0,1363412030.0,195380586450.0,13428219,KOSDAQ
2024-08-05,12410.0,12450.0,10450.0,10760.0,217188.0,2454597590.0,144487636440.0,13428219,KOSDAQ
2024-09-04,11500.0,11510.0,11110.0,11310.0,62062.0,699364850.0,151873156890.0,13428219,KOSDAQ
```

Backtest:

| window | peak/high | peak date | trough/low | trough date | MFE | MAE |
|---|---:|---|---:|---|---:|---:|
| 30 calendar days | 20700 | 2024-03-20 | 16950 | 2024-04-05 | +10.16% | -9.79% |
| 90 calendar days | 20700 | 2024-03-20 | 14000 | 2024-05-30 | +10.16% | -25.49% |
| 180 calendar days | 20700 | 2024-03-20 | 10450 | 2024-08-05 | +10.16% | -44.39% |

Interpretation:

```text
091580 is the weak-MFE high-MAE C12 counterexample.
The battery-can/customer relief label was plausible, but MFE never expanded beyond +10.16% and 180D MAE reached -44.39%.
This should block Stage2 or route to 4B/4C watch unless a fresh customer-volume and margin bridge is visible before entry.
```

---

## 7. Machine-readable trigger JSONL

```jsonl
{"row_type":"trigger","research_id":"R3L76_C12_BATTERY_CUSTOMER_CONTRACT_ROUTER","round":"R3","loop":76,"large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK","fine_archetype_id":"ELECTROLYTE_CNT_CAN_CUSTOMER_CONTRACT_LOCALIZATION_AND_CALL_OFF_HIGH_MAE_ROUTER","symbol":"348370","name":"엔켐","trigger_type":"Stage2-Actionable-Guarded","trigger_family":"electrolyte_customer_contract_localization_high_mfe_guarded","trigger_date":"2024-01-23","entry_date":"2024-01-24","entry_price":125000.0,"entry_price_type":"next_tradable_open_after_electrolyte_customer_localization_burst","price_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","mfe_30d_pct":186.8,"mae_30d_pct":-14.16,"mfe_90d_pct":215.6,"mae_90d_pct":-14.16,"mfe_180d_pct":215.6,"mae_180d_pct":-14.16,"peak_price_180d":394500.0,"peak_date_180d":"2024-04-08","trough_price_180d":107300.0,"trough_date_180d":"2024-01-26","calibration_usable":true,"case_polarity":"positive_guarded_high_mfe_customer_localization","evidence_url_pending":true,"source_proxy_only":true,"non_price_evidence_strength":"medium_pending_url_repair","price_only_blowoff":false,"expected_stage_current_profile":"Stage2-Guarded_to_Yellow_only_if_customer_contract_localization_volume_margin_bridge_repaired","residual_error_type":"huge_mfe_electrolyte_customer_localization_path_requires_call_off_and_margin_bridge_before_green"}
{"row_type":"trigger","research_id":"R3L76_C12_BATTERY_CUSTOMER_CONTRACT_ROUTER","round":"R3","loop":76,"large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK","fine_archetype_id":"ELECTROLYTE_CNT_CAN_CUSTOMER_CONTRACT_LOCALIZATION_AND_CALL_OFF_HIGH_MAE_ROUTER","symbol":"121600","name":"나노신소재","trigger_type":"Stage2-Actionable-Guarded","trigger_family":"cnt_conductive_additive_customer_expansion_initial_mfe_later_call_off_drawdown","trigger_date":"2024-02-20","entry_date":"2024-02-21","entry_price":105000.0,"entry_price_type":"next_tradable_open_after_cnt_customer_expansion_burst","price_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","mfe_30d_pct":50.29,"mae_30d_pct":-0.86,"mfe_90d_pct":50.29,"mae_90d_pct":-0.86,"mfe_180d_pct":50.29,"mae_180d_pct":-34.76,"peak_price_180d":157800.0,"peak_date_180d":"2024-02-22","trough_price_180d":68500.0,"trough_date_180d":"2024-08-05","calibration_usable":true,"case_polarity":"counterexample_initial_mfe_later_hard_mae","evidence_url_pending":true,"source_proxy_only":true,"non_price_evidence_strength":"medium_low_pending_url_repair","price_only_blowoff":false,"expected_stage_current_profile":"Stage2-Guarded_or_local_4B_high_MAE_watch_until_customer_volume_call_off_margin_bridge_repaired","residual_error_type":"cnt_customer_expansion_label_had_first_window_mfe_but_180d_call_off_mae_blocks_yellow_green_without_volume_margin_bridge"}
{"row_type":"trigger","research_id":"R3L76_C12_BATTERY_CUSTOMER_CONTRACT_ROUTER","round":"R3","loop":76,"large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK","fine_archetype_id":"ELECTROLYTE_CNT_CAN_CUSTOMER_CONTRACT_LOCALIZATION_AND_CALL_OFF_HIGH_MAE_ROUTER","symbol":"091580","name":"상신이디피","trigger_type":"Stage2-FalsePositive-Candidate","trigger_family":"battery_can_customer_contract_relief_weak_mfe_high_mae","trigger_date":"2024-03-07","entry_date":"2024-03-08","entry_price":18790.0,"entry_price_type":"next_tradable_open_after_battery_can_customer_relief_spike","price_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","mfe_30d_pct":10.16,"mae_30d_pct":-9.79,"mfe_90d_pct":10.16,"mae_90d_pct":-25.49,"mfe_180d_pct":10.16,"mae_180d_pct":-44.39,"peak_price_180d":20700.0,"peak_date_180d":"2024-03-20","trough_price_180d":10450.0,"trough_date_180d":"2024-08-05","calibration_usable":true,"case_polarity":"counterexample_weak_mfe_high_mae","evidence_url_pending":true,"source_proxy_only":true,"non_price_evidence_strength":"low_pending_url_repair","price_only_blowoff":false,"expected_stage_current_profile":"blocked_Stage2_or_4B_4C_high_MAE_watch_until_customer_contract_volume_margin_bridge_repaired","residual_error_type":"battery_can_customer_contract_relief_had_weak_mfe_and_high_mae_without_volume_margin_and_call_off_bridge"}
```

---

## 8. Score simulation and raw component breakdown

This is shadow-only and does not change production scoring.

| symbol | customer contract quality | call-off / release schedule | localization / procurement bridge | utilization / volume | market mispricing | margin / cash conversion | information confidence | shadow total | intended route |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| `348370` | 12 | 8 | 12 | 10 | 17 | 7 | 6 | 72 | Stage2-Guarded / Yellow only after evidence repair |
| `121600` | 10 | 4 | 7 | 6 | 10 | 4 | 5 | 46 | Stage2-Guarded or local 4B watch |
| `091580` | 5 | 2 | 3 | 3 | 3 | 2 | 4 | 22 | blocked Stage2 / 4B-4C high-MAE watch |

### Current calibrated profile stress test

The current calibrated profile already blocks pure price-only blowoff.  
The remaining C12 issue is **customer-contract label without call-off and margin conversion**:

```text
C12 high-MFE contract/localization path:
  customer/localization relevance
  + very large MFE
  + evidence still source_proxy_only
  + double-digit MAE
  => Stage2-Guarded, Yellow only after contract/call-off/margin evidence repair

C12 first-window-MFE later-MAE path:
  first-window MFE is strong
  + 180D MAE <= -30%
  + release schedule and volume bridge missing
  => Stage2-Guarded at most, local 4B watch, no Green

C12 weak-MFE high-MAE path:
  customer relief label exists
  + MFE_90D <= +12%
  + MAE_90D <= -20% or MAE_180D <= -40%
  + no contract/call-off evidence
  => block Stage2 or route to 4B/4C
```

`348370` prevents overblocking.  
`121600` shows why early MFE cannot become Green without call-off evidence.  
`091580` shows why customer-contract relevance must be tied to volume, margin, and cash conversion.

---

## 9. Aggregate metrics

```json
{
  "row_type": "aggregate",
  "research_id": "R3L76_C12_BATTERY_CUSTOMER_CONTRACT_ROUTER",
  "round": "R3",
  "loop": 76,
  "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY",
  "canonical_archetype_id": "C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK",
  "fine_archetype_id": "ELECTROLYTE_CNT_CAN_CUSTOMER_CONTRACT_LOCALIZATION_AND_CALL_OFF_HIGH_MAE_ROUTER",
  "case_count": 3,
  "calibration_usable_case_count": 3,
  "positive_guarded_case_count": 1,
  "counterexample_count": 2,
  "new_symbol_count": 3,
  "source_proxy_only_count": 3,
  "evidence_url_pending_count": 3,
  "avg_mfe_30d_pct": 82.42,
  "avg_mae_30d_pct": -8.27,
  "avg_mfe_90d_pct": 92.02,
  "avg_mae_90d_pct": -13.5,
  "avg_mfe_180d_pct": 92.02,
  "avg_mae_180d_pct": -31.1,
  "max_mfe_180d_pct": 215.6,
  "worst_mae_180d_pct": -44.39
}
```

---

## 10. 4B proximity split

```json
{
  "row_type": "4b_split",
  "research_id": "R3L76_C12_BATTERY_CUSTOMER_CONTRACT_ROUTER",
  "stage2_guarded_or_yellow_candidate": [
    {
      "symbol": "348370",
      "reason": "electrolyte/customer localization path had +215.60% 180D MFE, but double-digit MAE and source-proxy evidence require bridge repair"
    }
  ],
  "stage2_guarded_or_local_4b_watch": [
    {
      "symbol": "121600",
      "reason": "CNT customer-expansion path had +50.29% MFE but 180D MAE reached -34.76%"
    }
  ],
  "blocked_stage2_or_4c_watch": [
    {
      "symbol": "091580",
      "reason": "battery-can customer relief path had only +10.16% MFE and -44.39% 180D MAE"
    }
  ],
  "full_4b_or_green_requires_non_price_evidence": [
    "customer contract quality and duration",
    "shipment / call-off / release schedule",
    "localization or IRA/procurement linkage",
    "utilization and customer volume pull-through",
    "ASP/spread and input-cost pass-through",
    "inventory and working-capital control",
    "gross margin and cash-flow conversion"
  ]
}
```

---

## 11. Shadow rule candidate

```yaml
row_type: canonical_archetype_rule_candidate
canonical_archetype_id: C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK
fine_archetype_id: ELECTROLYTE_CNT_CAN_CUSTOMER_CONTRACT_LOCALIZATION_AND_CALL_OFF_HIGH_MAE_ROUTER
rule_name: C12_customer_contract_calloff_localization_and_high_mae_router
production_scoring_changed: false
shadow_weight_only: true
```

### Proposed routing logic

```text
For C12 battery customer-contract / call-off risk cases:

Tier A: high-MFE customer/localization path
  Conditions:
    - customer/localization relevance is plausible
    - MFE_90D >= +50%
    - evidence remains source_proxy_only
  Routing:
    - Stage2-Guarded allowed
    - Stage3-Yellow only after URL-repaired contract, call-off, localization, and margin bridge
    - no Green while evidence is pending

Tier B: first-window-MFE / later-MAE path
  Conditions:
    - MFE_30D >= +30%
    - MAE_180D <= -30%
    - no repaired customer-volume or release-schedule bridge
  Routing:
    - Stage2-Guarded at most
    - local 4B/high-MAE watch
    - no Yellow/Green

Tier C: weak-MFE high-MAE customer label
  Conditions:
    - MFE_90D <= +12%
    - MAE_90D <= -20% or MAE_180D <= -40%
    - bridge evidence remains unrepaired
  Routing:
    - block Stage2
    - route to 4B/4C high-MAE watch
```

### Suggested shadow delta

```json
{
  "row_type": "shadow_weight",
  "axis": "c12_customer_contract_calloff_localization_and_high_mae_router",
  "scope": "canonical_archetype_id:C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK",
  "proposal": {
    "source_proxy_only_green_allowed": false,
    "customer_contract_calloff_margin_bridge_required_for_green": true,
    "high_mfe_customer_path_mfe90_threshold_pct": 50.0,
    "first_window_mfe_threshold_30d_pct": 30.0,
    "later_mae_watch_threshold_180d_pct": -30.0,
    "weak_mfe_threshold_90d_pct": 12.0,
    "weak_mfe_mae90_threshold_pct": -20.0,
    "weak_mfe_hard_mae180_threshold_pct": -40.0,
    "positive_weight_blocked_until_url_repair": true
  },
  "confidence": "medium_low_until_url_repair",
  "apply_now": false,
  "reason": "One very high-MFE electrolyte/localization case and two call-off/customer-volume high-MAE failures show that C12 should require URL-repaired customer contract, release schedule, utilization, and margin evidence before Yellow/Green."
}
```

---

## 12. Residual contribution summary

```json
{
  "row_type": "residual_contribution",
  "research_id": "R3L76_C12_BATTERY_CUSTOMER_CONTRACT_ROUTER",
  "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY",
  "canonical_archetype_id": "C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK",
  "contribution": "Adds three non-top-covered C12 electrolyte/CNT/battery-can customer-contract cases and separates a huge-MFE electrolyte localization holdout from first-window-MFE/later-call-off drawdown and weak-MFE high-MAE customer-relief failures. C12 Yellow/Green should require URL-repaired customer contract quality, call-off schedule, localization/procurement linkage, utilization, volume, pass-through, working-capital, and margin evidence.",
  "positive_guarded_case_added": 1,
  "counterexample_case_added": 2,
  "new_symbol_count": 3,
  "new_independent_case_count": 3,
  "reused_case_count": 0,
  "same_archetype_new_symbol_count": 3,
  "same_archetype_new_trigger_family_count": 3,
  "new_trigger_family_count": 3,
  "current_profile_error_count": 2,
  "diversity_score_summary": {
    "new_symbol_bonus": 9,
    "counterexample_gap_bonus": 4,
    "residual_error_bonus": 10,
    "wrong_round_penalty": 0,
    "repeated_same_symbol_penalty": 0,
    "net_interpretive_score": 23
  },
  "loop_contribution_label": "canonical_archetype_rule_candidate",
  "do_not_propose_new_weight_delta": false,
  "data_quality_blocker": "All three non-price battery customer-contract triggers require URL-level repair before positive weight promotion.",
  "guardrail_added": "C12 source_proxy_only cases with MFE_30D >= +30% but MAE_180D <= -30% should cap at Stage2-Guarded; weak-MFE cases with MFE_90D <= +12% and MAE_90D <= -20% or MAE_180D <= -40% should block Stage2 or route to 4B/4C watch."
}
```

One-line contribution:

```text
This loop adds 3 new independent cases, 2 counterexamples, and 2 residual errors for R3/L3_BATTERY_EV_GREEN_MOBILITY/C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK.
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
    348370: false
    121600: false
    091580: false
  evidence_url_pending:
    348370: true
    121600: true
    091580: true
  source_proxy_only:
    348370: true
    121600: true
    091580: true
```

Limitations:

```text
- Price path is validated against Stock-Web tradable OHLC rows.
- Non-price evidence is not URL-repaired in this run.
- Therefore this artifact is useful for C12 battery customer-contract / call-off residual shape and high-MAE guardrail design, but should not promote positive weights until filings, IR, order disclosures, customer data, export data, or reports verify customer contract quality, shipment/call-off schedule, localization, utilization, volume, pass-through, working capital, and margin conversion.
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
2. Preserve R3 / loop 76 metadata.
3. Add the cases to C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK only if parser validation passes.
4. Treat all three non-price triggers as evidence_url_pending=true and source_proxy_only=true until URL-level evidence is repaired.
5. Do not use these rows for positive weight promotion until filings/IR/order-disclosure/customer/export-data/report data verifies customer contract quality, shipment/call-off schedule, localization/procurement linkage, utilization, volume, pass-through, working capital, and margin conversion.
6. Add a shadow-only rule candidate named C12_customer_contract_calloff_localization_and_high_mae_router.
7. Do not loosen Stage3-Green.
8. Add C12-specific guards:
   - source_proxy_only -> no Green
   - Green requires repaired customer contract / call-off / margin bridge
   - MFE_90D >= +50% may remain Stage2-Guarded until evidence repair
   - MFE_30D >= +30% and MAE_180D <= -30% -> Stage2-Guarded at most / local 4B watch
   - MFE_90D <= +12% and MAE_90D <= -20% or MAE_180D <= -40% -> block Stage2 / 4B-4C watch
9. Keep production scoring unchanged unless later batch promotion logic independently marks this axis safe.
```

---

## 15. Next round state

```text
completed_round = R3
completed_loop = 76
next_round = R4
next_loop = 76
next_large_sector_hint = L4_MATERIALS_SPREAD_RESOURCE
round_schedule_status = valid
round_sector_consistency = pass
```
