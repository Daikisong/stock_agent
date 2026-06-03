# E2R Stock-Web v12 Residual Research — R3 Loop 74

```yaml
research_session: post_calibrated_sector_archetype_residual_research
mode: historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12
completed_round: R3
completed_loop: 74
next_round: R4
next_loop: 74
large_sector_id: L3_BATTERY_EV_GREEN_MOBILITY
canonical_archetype_id: C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK
fine_archetype_id: ANODE_CNT_SILICON_CAN_CUSTOMER_CONTRACT_CALLOFF_AND_HIGH_MAE_ROUTER
output_file: e2r_stock_web_v12_residual_round_R3_loop_74_L3_BATTERY_EV_GREEN_MOBILITY_C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK_research.md
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
completed_loop  = 74
large_sector_id = L2_AI_SEMICONDUCTOR_ELECTRONICS
canonical_archetype_id = C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE
```

Therefore:

```text
scheduled_round = R3
scheduled_loop  = 74
```

R3 maps to:

```text
large_sector_id = L3_BATTERY_EV_GREEN_MOBILITY
```

This run selects:

```text
canonical_archetype_id = C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK
fine_archetype_id = ANODE_CNT_SILICON_CAN_CUSTOMER_CONTRACT_CALLOFF_AND_HIGH_MAE_ROUTER
```

This is a valid R3/L3 pairing.

---

## 1. Why this R3/C12 run

The no-repeat ledger shows C12 is moderately covered but concentrated in a small set of battery-material and separator names:

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

This file avoids those top-covered names and adds three less-repeated customer-contract / call-off exposed battery names:

```text
078600 대주전자재료
121600 나노신소재
091580 상신이디피
```

Research question:

```text
Can C12 separate a real customer-conversion rerating from battery-material / battery-component rallies where customer qualification exists as a narrative but later call-off, utilization, or margin risk dominates the path?
```

C12 is a customer-pull-through archetype. A battery supplier can have a beautiful product story, but if the customer schedule slows or the contracted volume does not convert to margin, the order bridge becomes a drawbridge: it looks solid while raised, then disappears under the entry.

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
| `078600` | 대주전자재료 | active_like / KOSDAQ | none listed | true |
| `121600` | 나노신소재 | active_like / KOSDAQ | no 2024 overlap; latest listed candidate 2015-12-17 | true |
| `091580` | 상신이디피 | active_like / KOSDAQ | no 2024 overlap; latest listed candidate 2011-05-11 | true |

Profile caveat:

```text
Stock-Web OHLC is raw/unadjusted marcap data.
These cases are calibration-safe for the selected 2024 windows because no listed corporate-action candidate overlaps each entry~D+180 test window.
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
The Stock-Web price path is fully validated, but company-level customer contract, battery OEM qualification, volume schedule, call-off risk, utilization, ASP, and margin conversion evidence still require later URL repair through filings, IR decks, customer data, export data, or sell-side reports before production weight promotion.
```

C12 interpretation used here:

```text
C12 is not simply “battery material stock rose.”
It asks whether customer demand is actually contract-convertible:
- named or high-confidence customer bridge,
- qualification and mass-production schedule,
- call-off and delay risk,
- volume / utilization,
- ASP and margin conversion,
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
078600 + C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK -> no direct match found
121600 + C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK -> no direct match found
091580 + C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK -> no direct match found
```

Novelty accounting:

```json
{
  "new_symbol_count": 3,
  "minimum_new_symbol_count": 2,
  "positive_anchor_count": 1,
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
| `R3L74_C12_078600_20240312` | `078600` 대주전자재료 | silicon-anode customer conversion / low-MAE rerating | positive anchor |
| `R3L74_C12_121600_20240222` | `121600` 나노신소재 | CNT conductive additive customer-contract narrative | high-MAE counterexample |
| `R3L74_C12_091580_20240308` | `091580` 상신이디피 | battery-can customer demand relief | weak-MFE high-MAE counterexample |

The intended residual:

```text
C12 should separate:
1. customer-conversion paths where MFE persists and MAE stays low;
2. battery-material customer narratives that produce initial MFE but later collapse when call-off/utilization risk appears;
3. component-supplier relief entries where MFE is weak and high MAE should block Stage2/Green.
```

---

## 6. Stock-Web OHLC and backtest

### 6.1 `078600` 대주전자재료 — silicon-anode customer conversion low-MAE rerating

Trigger:

```text
trigger_date = 2024-03-11
trigger_type = Stage2-Actionable
trigger_family = silicon_anode_customer_conversion_low_mae_rerating
entry_date = 2024-03-12
entry_price = 86400.0
entry_price_type = next_tradable_open_after_silicon_anode_customer_rerating
```

Relevant Stock-Web rows:

```csv
d,o,h,l,c,v,a,mc,s,m
2024-03-11,80000.0,85600.0,77500.0,85200.0,586226.0,48633832700.0,1318946523600.0,15480593,KOSDAQ
2024-03-12,86400.0,95100.0,85400.0,94900.0,1144358.0,104711119200.0,1469108275700.0,15480593,KOSDAQ
2024-03-25,97000.0,102000.0,95200.0,102000.0,388838.0,38976415300.0,1579020486000.0,15480593,KOSDAQ
2024-03-26,101500.0,103200.0,96000.0,98500.0,444003.0,43900864500.0,1524838410500.0,15480593,KOSDAQ
2024-04-08,90000.0,90000.0,85000.0,88800.0,162941.0,14223802700.0,1374676658400.0,15480593,KOSDAQ
2024-05-30,105200.0,123000.0,105200.0,121300.0,2236997.0,264481416600.0,1877795930900.0,15480593,KOSDAQ
2024-06-12,154900.0,163400.0,152300.0,160000.0,1515428.0,240983991200.0,2476894880000.0,15480593,KOSDAQ
2024-09-06,100700.0,101800.0,92500.0,92900.0,421202.0,40051568800.0,1438147089700.0,15480593,KOSDAQ
```

Backtest:

| window | peak/high | peak date | trough/low | trough date | MFE | MAE |
|---|---:|---|---:|---|---:|---:|
| 30 calendar days | 103200 | 2024-03-26 | 85000 | 2024-04-08 | +19.44% | -1.62% |
| 90 calendar days | 128500 | 2024-06-10 | 85000 | 2024-04-08 | +48.73% | -1.62% |
| 180 calendar days | 163400 | 2024-06-12 | 85000 | 2024-04-08 | +89.12% | -1.62% |

Interpretation:

```text
078600 is the C12 positive anchor.
The price path had persistent MFE and very low MAE, which is exactly what a customer-conversion rerating should look like.
Green still requires URL-repaired customer contract / qualification / mass-production / margin evidence, but the path supports Stage2-Actionable / Yellow after repair.
```

### 6.2 `121600` 나노신소재 — CNT customer-contract narrative with later high MAE

Trigger:

```text
trigger_date = 2024-02-21
trigger_type = Stage2-Actionable-Guarded
trigger_family = cnt_conductive_additive_customer_contract_high_mae
entry_date = 2024-02-22
entry_price = 133100.0
entry_price_type = next_tradable_open_after_cnt_customer_theme_burst
```

Relevant Stock-Web rows:

```csv
d,o,h,l,c,v,a,mc,s,m
2024-02-21,105000.0,136300.0,104100.0,134000.0,1984511.0,251330823300.0,1629423652000.0,12159878,KOSDAQ
2024-02-22,133100.0,157800.0,130600.0,138000.0,1955332.0,281220563000.0,1678063164000.0,12159878,KOSDAQ
2024-03-06,129200.0,132300.0,125000.0,125700.0,266532.0,34090901300.0,1528496664600.0,12159878,KOSDAQ
2024-03-18,145700.0,151000.0,145300.0,147600.0,464253.0,68940481400.0,1794797992800.0,12159878,KOSDAQ
2024-04-08,121800.0,122500.0,116000.0,121000.0,149693.0,17761843600.0,1471345238000.0,12159878,KOSDAQ
2024-06-27,121300.0,127800.0,119500.0,121000.0,379007.0,46945231500.0,1475725438000.0,12196078,KOSDAQ
2024-08-05,87900.0,89700.0,68500.0,74900.0,264044.0,21196062100.0,913486242200.0,12196078,KOSDAQ
2024-09-06,87500.0,88200.0,81300.0,82800.0,70432.0,5914884400.0,1009835258400.0,12196078,KOSDAQ
```

Backtest:

| window | peak/high | peak date | trough/low | trough date | MFE | MAE |
|---|---:|---|---:|---|---:|---:|
| 30 calendar days | 157800 | 2024-02-22 | 125000 | 2024-03-06 | +18.56% | -6.09% |
| 90 calendar days | 157800 | 2024-02-22 | 116000 | 2024-04-08 | +18.56% | -12.85% |
| 180 calendar days | 157800 | 2024-02-22 | 68500 | 2024-08-05 | +18.56% | -48.54% |

Interpretation:

```text
121600 is the high-MAE C12 counterexample.
The customer/CNT narrative produced a real first-window rerating, but the 180D drawdown later overwhelmed it.
This should stay Stage2-Guarded or local 4B/high-MAE watch until customer schedule, call-off risk, utilization, ASP, and margin evidence are repaired.
```

### 6.3 `091580` 상신이디피 — battery-can customer demand relief with weak MFE and high MAE

Trigger:

```text
trigger_date = 2024-03-07
trigger_type = Stage2-FalsePositive-Candidate
trigger_family = battery_can_customer_demand_relief_weak_mfe_high_mae
entry_date = 2024-03-08
entry_price = 18790.0
entry_price_type = next_tradable_open_after_battery_can_customer_demand_spike
```

Relevant Stock-Web rows:

```csv
d,o,h,l,c,v,a,mc,s,m
2024-03-07,15950.0,19440.0,15810.0,18000.0,3526915.0,64200433390.0,245307942000.0,13628219,KOSDAQ
2024-03-08,18790.0,19320.0,17830.0,18390.0,1785418.0,33326694850.0,250622947410.0,13628219,KOSDAQ
2024-03-20,19180.0,20700.0,19070.0,19480.0,1377974.0,27512495350.0,265477706120.0,13628219,KOSDAQ
2024-04-05,17110.0,17290.0,16950.0,17000.0,134587.0,2294987370.0,228279723000.0,13428219,KOSDAQ
2024-05-24,15320.0,15540.0,15000.0,15160.0,70918.0,1078345170.0,363545820200.0,13428219,KOSDAQ
2024-06-26,15180.0,15920.0,15040.0,15150.0,160818.0,2488177310.0,203437517850.0,13428219,KOSDAQ
2024-08-05,12410.0,12450.0,10450.0,10760.0,217188.0,2454597590.0,144487636440.0,13428219,KOSDAQ
2024-09-04,11500.0,11510.0,11110.0,11310.0,62062.0,699364850.0,151873156890.0,13428219,KOSDAQ
```

Backtest:

| window | peak/high | peak date | trough/low | trough date | MFE | MAE |
|---|---:|---|---:|---|---:|---:|
| 30 calendar days | 20700 | 2024-03-20 | 16950 | 2024-04-05 | +10.16% | -9.79% |
| 90 calendar days | 20700 | 2024-03-20 | 15000 | 2024-05-24 | +10.16% | -20.17% |
| 180 calendar days | 20700 | 2024-03-20 | 10450 | 2024-08-05 | +10.16% | -44.39% |

Interpretation:

```text
091580 is the weak-MFE / high-MAE branch.
The entry had a battery-customer demand label, but the return/risk geometry failed: only +10.16% MFE against -44.39% 180D MAE.
This should block Stage2/Green unless hard customer contract, utilization, and margin evidence is repaired before entry.
```

---

## 7. Machine-readable trigger JSONL

```jsonl
{"row_type":"trigger","research_id":"R3L74_C12_ANODE_CNT_CUSTOMER_CALLOFF_ROUTER","round":"R3","loop":74,"large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK","fine_archetype_id":"ANODE_CNT_SILICON_CAN_CUSTOMER_CONTRACT_CALLOFF_AND_HIGH_MAE_ROUTER","symbol":"078600","name":"대주전자재료","trigger_type":"Stage2-Actionable","trigger_family":"silicon_anode_customer_conversion_low_mae_rerating","trigger_date":"2024-03-11","entry_date":"2024-03-12","entry_price":86400.0,"entry_price_type":"next_tradable_open_after_silicon_anode_customer_rerating","price_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","mfe_30d_pct":19.44,"mae_30d_pct":-1.62,"mfe_90d_pct":48.73,"mae_90d_pct":-1.62,"mfe_180d_pct":89.12,"mae_180d_pct":-1.62,"peak_price_180d":163400.0,"peak_date_180d":"2024-06-12","trough_price_180d":85000.0,"trough_date_180d":"2024-04-08","calibration_usable":true,"case_polarity":"positive_anchor_low_mae","evidence_url_pending":true,"source_proxy_only":true,"non_price_evidence_strength":"medium_pending_url_repair","price_only_blowoff":false,"expected_stage_current_profile":"Stage2-Actionable_to_Yellow_after_customer_contract_margin_bridge_repaired","residual_error_type":"positive_anchor_requires_url_repaired_customer_contract_volume_margin_bridge_before_green"}
{"row_type":"trigger","research_id":"R3L74_C12_ANODE_CNT_CUSTOMER_CALLOFF_ROUTER","round":"R3","loop":74,"large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK","fine_archetype_id":"ANODE_CNT_SILICON_CAN_CUSTOMER_CONTRACT_CALLOFF_AND_HIGH_MAE_ROUTER","symbol":"121600","name":"나노신소재","trigger_type":"Stage2-Actionable-Guarded","trigger_family":"cnt_conductive_additive_customer_contract_high_mae","trigger_date":"2024-02-21","entry_date":"2024-02-22","entry_price":133100.0,"entry_price_type":"next_tradable_open_after_cnt_customer_theme_burst","price_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","mfe_30d_pct":18.56,"mae_30d_pct":-6.09,"mfe_90d_pct":18.56,"mae_90d_pct":-12.85,"mfe_180d_pct":18.56,"mae_180d_pct":-48.54,"peak_price_180d":157800.0,"peak_date_180d":"2024-02-22","trough_price_180d":68500.0,"trough_date_180d":"2024-08-05","calibration_usable":true,"case_polarity":"counterexample_customer_contract_high_mae","evidence_url_pending":true,"source_proxy_only":true,"non_price_evidence_strength":"medium_low_pending_url_repair","price_only_blowoff":false,"expected_stage_current_profile":"Stage2-Guarded_or_4B_high_MAE_watch_until_customer_calloff_bridge_repaired","residual_error_type":"cnt_customer_contract_narrative_had_initial_mfe_but_later_calloff_mae_blocks_green"}
{"row_type":"trigger","research_id":"R3L74_C12_ANODE_CNT_CUSTOMER_CALLOFF_ROUTER","round":"R3","loop":74,"large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK","fine_archetype_id":"ANODE_CNT_SILICON_CAN_CUSTOMER_CONTRACT_CALLOFF_AND_HIGH_MAE_ROUTER","symbol":"091580","name":"상신이디피","trigger_type":"Stage2-FalsePositive-Candidate","trigger_family":"battery_can_customer_demand_relief_weak_mfe_high_mae","trigger_date":"2024-03-07","entry_date":"2024-03-08","entry_price":18790.0,"entry_price_type":"next_tradable_open_after_battery_can_customer_demand_spike","price_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","mfe_30d_pct":10.16,"mae_30d_pct":-9.79,"mfe_90d_pct":10.16,"mae_90d_pct":-20.17,"mfe_180d_pct":10.16,"mae_180d_pct":-44.39,"peak_price_180d":20700.0,"peak_date_180d":"2024-03-20","trough_price_180d":10450.0,"trough_date_180d":"2024-08-05","calibration_usable":true,"case_polarity":"counterexample_weak_mfe_high_mae","evidence_url_pending":true,"source_proxy_only":true,"non_price_evidence_strength":"low_pending_url_repair","price_only_blowoff":false,"expected_stage_current_profile":"blocked_Stage2_or_4B_4C_high_MAE_watch","residual_error_type":"battery_can_customer_demand_relief_entry_weak_mfe_extreme_mae_without_contract_bridge"}
```

---

## 8. Score simulation and raw component breakdown

This is shadow-only and does not change production scoring.

| symbol | customer/contract bridge | call-off risk control | utilization / volume bridge | market mispricing | valuation rerating | margin conversion | information confidence | shadow total | intended route |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| `078600` | 14 | 12 | 13 | 14 | 15 | 12 | 7 | 87 | Stage2/Yellow; Green only after customer-contract and margin evidence repair |
| `121600` | 9 | 4 | 6 | 11 | 10 | 4 | 5 | 49 | Stage2-Guarded or 4B/high-MAE watch |
| `091580` | 4 | 3 | 3 | 5 | 4 | 3 | 4 | 26 | blocked Stage2 / 4B-4C high-MAE watch |

### Current calibrated profile stress test

The current calibrated profile already blocks pure price-only blowoff.  
The remaining C12 issue is **customer narrative without pull-through**:

```text
C12 clean customer-conversion path:
  customer/qualification relevance
  + MFE persists across 90D/180D
  + MAE remains contained
  + URL-repaired volume/margin bridge
  => Stage2-Actionable / Yellow, possible Green after proof

C12 high-MAE customer narrative:
  material/component has plausible customer story
  + first-window MFE exists
  + 180D MAE <= -40%
  + source evidence remains URL-pending
  => Stage2-Guarded at most, local 4B/high-MAE watch, no Green

C12 weak-MFE component relief:
  MFE_90D near +10%
  + MAE_90D <= -20%
  + no customer call-off repair
  => block Stage2 or 4B/4C watch
```

`078600` prevents overblocking.  
`121600` shows that a real product/customer theme can still fail if later call-off/utilization risk appears.  
`091580` is the hard weak-MFE guardrail.

---

## 9. Aggregate metrics

```json
{
  "row_type": "aggregate",
  "research_id": "R3L74_C12_ANODE_CNT_CUSTOMER_CALLOFF_ROUTER",
  "round": "R3",
  "loop": 74,
  "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY",
  "canonical_archetype_id": "C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK",
  "fine_archetype_id": "ANODE_CNT_SILICON_CAN_CUSTOMER_CONTRACT_CALLOFF_AND_HIGH_MAE_ROUTER",
  "case_count": 3,
  "calibration_usable_case_count": 3,
  "positive_anchor_count": 1,
  "counterexample_count": 2,
  "new_symbol_count": 3,
  "source_proxy_only_count": 3,
  "evidence_url_pending_count": 3,
  "avg_mfe_30d_pct": 16.05,
  "avg_mae_30d_pct": -5.83,
  "avg_mfe_90d_pct": 25.82,
  "avg_mae_90d_pct": -11.55,
  "avg_mfe_180d_pct": 39.28,
  "avg_mae_180d_pct": -31.52,
  "max_mfe_180d_pct": 89.12,
  "worst_mae_180d_pct": -48.54
}
```

---

## 10. 4B proximity split

```json
{
  "row_type": "4b_split",
  "research_id": "R3L74_C12_ANODE_CNT_CUSTOMER_CALLOFF_ROUTER",
  "stage2_positive_or_yellow_candidate": [
    {
      "symbol": "078600",
      "reason": "persistent +89.12% 180D MFE with only -1.62% MAE; requires URL-repaired customer/volume/margin bridge before Green"
    }
  ],
  "local_4b_high_mae_watch": [
    {
      "symbol": "121600",
      "reason": "initial +18.56% MFE, but 180D MAE reached -48.54%; customer/CNT narrative needs call-off and margin repair"
    }
  ],
  "blocked_stage2_or_4c_watch": [
    {
      "symbol": "091580",
      "reason": "MFE stayed only +10.16% while 90D MAE crossed -20% and 180D MAE reached -44.39%"
    }
  ],
  "full_4b_or_green_requires_non_price_evidence": [
    "named or high-confidence customer bridge",
    "qualification and mass-production schedule",
    "call-off / delay risk reduction",
    "utilization and shipment volume",
    "ASP and margin conversion"
  ]
}
```

---

## 11. Shadow rule candidate

```yaml
row_type: canonical_archetype_rule_candidate
canonical_archetype_id: C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK
fine_archetype_id: ANODE_CNT_SILICON_CAN_CUSTOMER_CONTRACT_CALLOFF_AND_HIGH_MAE_ROUTER
rule_name: C12_customer_contract_calloff_high_mae_router
production_scoring_changed: false
shadow_weight_only: true
```

### Proposed routing logic

```text
For C12 battery customer contract / call-off risk cases:

Tier A: verified customer-conversion winner
  Conditions:
    - customer/qualification/volume evidence is URL-repaired
    - 30D/90D MAE remains contained
    - MFE persists beyond one event candle
    - margin conversion is visible or later confirmed
  Routing:
    - Stage2-Actionable allowed
    - Stage3-Yellow allowed after evidence repair
    - Green only after customer volume and margin bridge are verified

Tier B: product/customer narrative with later high MAE
  Conditions:
    - product or customer theme has initial MFE
    - evidence_url_pending or source_proxy_only remains true
    - 180D MAE <= -40%
  Routing:
    - Stage2-Actionable-Guarded at most
    - local 4B/high-MAE watch
    - no Green

Tier C: component relief with weak MFE and call-off risk
  Conditions:
    - MFE_90D <= +12%
    - MAE_90D <= -20%
    - no repaired customer schedule / utilization / margin bridge
  Routing:
    - block Stage2 or route to 4B/4C watch
    - count as counterexample
```

### Suggested shadow delta

```json
{
  "row_type": "shadow_weight",
  "axis": "c12_customer_contract_calloff_high_mae_router",
  "scope": "canonical_archetype_id:C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK",
  "proposal": {
    "source_proxy_only_green_allowed": false,
    "customer_volume_margin_bridge_required_for_green": true,
    "product_customer_narrative_stage2_cap": "guarded_only_until_url_repair",
    "high_mae_watch_threshold_180d_pct": -40.0,
    "weak_mfe_threshold_90d_pct": 12.0,
    "calloff_high_mae_threshold_90d_pct": -20.0,
    "positive_weight_blocked_until_url_repair": true
  },
  "confidence": "medium_low_until_url_repair",
  "apply_now": false,
  "reason": "One low-MAE customer-conversion winner and two high-MAE customer/call-off counterexamples show that C12 should require URL-repaired customer schedule, volume, utilization, and margin evidence before Yellow/Green."
}
```

---

## 12. Residual contribution summary

```json
{
  "row_type": "residual_contribution",
  "research_id": "R3L74_C12_ANODE_CNT_CUSTOMER_CALLOFF_ROUTER",
  "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY",
  "canonical_archetype_id": "C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK",
  "contribution": "Adds three non-top-covered C12 battery customer/call-off cases and separates a clean silicon-anode customer-conversion path from CNT/customer-narrative and battery-can weak-MFE high-MAE counterexamples. C12 Green should require URL-repaired customer schedule, qualification, call-off risk reduction, utilization, ASP, and margin conversion evidence.",
  "positive_case_added": 1,
  "counterexample_case_added": 2,
  "new_symbol_count": 3,
  "data_quality_blocker": "All three non-price customer/call-off triggers require URL-level repair before positive weight promotion.",
  "guardrail_added": "C12 source_proxy_only customer narratives with 180D MAE <= -40% should cap at Stage2-Guarded or 4B/high-MAE watch; weak-MFE component cases with MAE_90D <= -20% should block Stage2 or route to 4B/4C watch."
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
    078600: false
    121600: false
    091580: false
  evidence_url_pending:
    078600: true
    121600: true
    091580: true
  source_proxy_only:
    078600: true
    121600: true
    091580: true
```

Limitations:

```text
- Price path is validated against Stock-Web tradable OHLC rows.
- Non-price evidence is not URL-repaired in this run.
- Therefore this artifact is useful for C12 customer contract/call-off residual shape and high-MAE guardrail design, but should not promote positive weights until filings/IR/customer/export/report data verifies customer contracts, qualification, mass-production schedule, utilization, ASP, and margin conversion.
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
2. Preserve R3 / loop 74 metadata.
3. Add the cases to C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK only if parser validation passes.
4. Treat all three non-price triggers as evidence_url_pending=true and source_proxy_only=true until URL-level evidence is repaired.
5. Do not use these rows for positive weight promotion until filings/IR/customer/export/report data verifies customer contracts, qualification, mass-production schedule, call-off risk reduction, utilization, ASP, and margin conversion.
6. Add a shadow-only rule candidate named C12_customer_contract_calloff_high_mae_router.
7. Do not loosen Stage3-Green.
8. Add C12-specific guards:
   - source_proxy_only -> no Green
   - Green requires repaired customer/volume/margin bridge
   - 180D MAE <= -40% without bridge repair -> local 4B/high-MAE watch
   - MFE_90D <= +12% and MAE_90D <= -20% -> block Stage2 or route to 4B/4C watch
   - initial product/customer MFE does not override later call-off MAE
9. Keep production scoring unchanged unless later batch promotion logic independently marks this axis safe.
```

---

## 15. Next round state

```text
completed_round = R3
completed_loop = 74
next_round = R4
next_loop = 74
next_large_sector_hint = L4_MATERIALS_SPREAD_RESOURCE
```
