# E2R Stock-Web v12 Residual Research — R3 Loop 77

```yaml
research_session: post_calibrated_sector_archetype_residual_research
mode: historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12
completed_round: R3
completed_loop: 77
next_round: R4
next_loop: 77
large_sector_id: L3_BATTERY_EV_GREEN_MOBILITY
canonical_archetype_id: C13_BATTERY_JV_UTILIZATION_AMPC_IRA
fine_archetype_id: COPPER_FOIL_CATHODE_FOIL_UTILIZATION_AMPC_IRA_HIGH_MAE_ROUTER
output_file: e2r_stock_web_v12_residual_round_R3_loop_77_L3_BATTERY_EV_GREEN_MOBILITY_C13_BATTERY_JV_UTILIZATION_AMPC_IRA_research.md
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
completed_loop  = 77
large_sector_id = L2_AI_SEMICONDUCTOR_ELECTRONICS
canonical_archetype_id = C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF
```

Therefore:

```text
scheduled_round = R3
scheduled_loop  = 77
```

R3 maps to:

```text
large_sector_id = L3_BATTERY_EV_GREEN_MOBILITY
```

This run selects:

```text
canonical_archetype_id = C13_BATTERY_JV_UTILIZATION_AMPC_IRA
fine_archetype_id = COPPER_FOIL_CATHODE_FOIL_UTILIZATION_AMPC_IRA_HIGH_MAE_ROUTER
```

This is a valid R3/L3 pairing.

---

## 1. Why this R3/C13 run

The no-repeat ledger shows C13 is still relatively compact compared with C11/C12/C14:

```text
C13_BATTERY_JV_UTILIZATION_AMPC_IRA:
  rows: 43
  symbols: 11
  date_range: 2022-05-25~2025-04-08
  good/bad S2: 10/9
  4B/4C: 7/2
  URL/proxy: 6/6
  top covered symbols: 373220(14), 006400(13), 096770(5), 003670(2), 020150(2), 051910(2)
```

This file avoids the most repeated cell-level names and adds material-supply-chain utilization cases:

```text
011790 SKC
020150 롯데에너지머티리얼즈
005070 코스모신소재
006110 삼아알미늄
```

Research question:

```text
Can C13 separate a real IRA/AMPC/utilization rerating in battery materials from material/foil/cathode labels where the policy and utilization story exists, but customer call-off, actual utilization, spread/ASP, and margin conversion are not repaired?
```

C13 is a utilization bridge. IRA/AMPC is the power line, but the factory still needs the switch turned on: customer releases, operating rate, qualified capacity, spread, pass-through, and cash margin. If the switch is off, the policy line hums while the stock falls silent.

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
| `011790` | SKC | active_like / KOSPI | no 2024 overlap; old candidates only | true |
| `020150` | 롯데에너지머티리얼즈 | active_like / KOSPI | none listed | true |
| `005070` | 코스모신소재 | active_like / KOSPI | no 2024 overlap; latest listed candidate 2019-11-13 | true |
| `006110` | 삼아알미늄 | active_like / KOSPI | no 2024 overlap; latest listed candidate 2023-02-09 | true |

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
The Stock-Web price path is fully validated, but company-level customer call-off, actual utilization, qualified capacity, AMPC/IRA eligibility, JV economics, shipment volume, ASP/spread, input-cost pass-through, working capital, gross margin, and cash conversion evidence still require later URL repair through filings, IR decks, customer data, order disclosures, export data, or sell-side reports before production weight promotion.
```

C13 interpretation used here:

```text
C13 is not simply “battery material stock rose.”
It asks whether IRA/AMPC/JV/utilization relevance becomes company economics:
- customer call-off and release schedule,
- actual utilization / operating rate,
- qualified capacity and customer acceptance,
- AMPC/IRA eligibility and unit economics,
- ASP/spread and input-cost pass-through,
- working capital and cash conversion,
- and controlled MAE after the trigger.
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
011790 + C13_BATTERY_JV_UTILIZATION_AMPC_IRA -> no direct match found
005070 + C13_BATTERY_JV_UTILIZATION_AMPC_IRA -> no direct match found
006110 + C13_BATTERY_JV_UTILIZATION_AMPC_IRA -> no direct match found
020150 + C13_BATTERY_JV_UTILIZATION_AMPC_IRA -> no direct match found
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
| `R3L77_C13_011790_20240311` | `011790` SKC | copper foil IRA/AMPC utilization / customer-quality path | positive anchor |
| `R3L77_C13_020150_20240321` | `020150` 롯데에너지머티리얼즈 | copper foil utilization / first-window MFE later drawdown | positive-guarded |
| `R3L77_C13_005070_20240311` | `005070` 코스모신소재 | cathode material utilization / weak-MFE later high MAE | counterexample |
| `R3L77_C13_006110_20240308` | `006110` 삼아알미늄 | battery foil utilization label / near-zero MFE extreme MAE | hard counterexample |

The intended residual:

```text
C13 should separate:
1. copper-foil utilization paths where MFE compounds and MAE remains controlled;
2. copper-foil paths where first-window MFE is real but later MAE caps Yellow/Green;
3. cathode/material names where utilization policy relevance exists but MFE is weak;
4. foil/utilization labels where the entry is effectively the peak and 180D MAE becomes extreme.
```

---

## 6. Stock-Web OHLC and backtest

### 6.1 `011790` SKC — copper-foil IRA/AMPC utilization positive anchor

Trigger:

```text
trigger_date = 2024-03-08
trigger_type = Stage2-Actionable
trigger_family = copper_foil_ira_ampc_utilization_customer_quality_high_mfe_low_mae_rerating
entry_date = 2024-03-11
entry_price = 104500.0
entry_price_type = next_tradable_open_after_copper_foil_ira_ampc_utilization_burst
```

Relevant Stock-Web rows:

```csv
d,o,h,l,c,v,a,mc,s,m
2024-03-08,97800.0,105400.0,97000.0,103700.0,817210.0,83265709200.0,3926942502600.0,37868298,KOSPI
2024-03-11,104500.0,109700.0,101000.0,106300.0,692892.0,73707559000.0,4025400077400.0,37868298,KOSPI
2024-04-09,140900.0,149700.0,134900.0,135500.0,1290419.0,182236641700.0,5131154379000.0,37868298,KOSPI
2024-05-17,110100.0,110100.0,101300.0,101300.0,630583.0,65148220900.0,3836058587400.0,37868298,KOSPI
2024-06-07,149900.0,156300.0,146200.0,149200.0,734425.0,110598601100.0,5649950061600.0,37868298,KOSPI
2024-06-18,189100.0,200000.0,172900.0,182000.0,1381511.0,260576363300.0,6892030236000.0,37868298,KOSPI
2024-08-05,123100.0,125000.0,107600.0,114100.0,606740.0,71690324400.0,4320772801800.0,37868298,KOSPI
2024-09-06,116300.0,117200.0,108500.0,109100.0,363314.0,40450742400.0,4131431311800.0,37868298,KOSPI
```

Backtest:

| window | peak/high | peak date | trough/low | trough date | MFE | MAE |
|---|---:|---|---:|---|---:|---:|
| 30 calendar days | 149700 | 2024-04-09 | 101000 | 2024-03-11 | +43.25% | -3.35% |
| 90 calendar days | 156300 | 2024-06-07 | 101000 | 2024-03-11 | +49.57% | -3.35% |
| 180 calendar days | 200000 | 2024-06-18 | 101000 | 2024-03-11 | +91.39% | -3.35% |

Interpretation:

```text
011790 is the C13 positive anchor.
The copper-foil / IRA-AMPC / utilization route produced persistent MFE while MAE stayed contained.
It can support Stage2-Actionable / Yellow after evidence repair, but Green still requires URL-repaired customer call-off, utilization, shipment volume, spread, and margin evidence.
```

### 6.2 `020150` 롯데에너지머티리얼즈 — copper-foil utilization first-window MFE / later-drawdown path

Trigger:

```text
trigger_date = 2024-03-20
trigger_type = Stage2-Actionable-Guarded
trigger_family = copper_foil_utilization_ira_ampc_first_window_mfe_later_drawdown
entry_date = 2024-03-21
entry_price = 43000.0
entry_price_type = next_tradable_open_after_copper_foil_utilization_ira_ampc_burst
```

Relevant Stock-Web rows:

```csv
d,o,h,l,c,v,a,mc,s,m
2024-03-20,40350.0,43200.0,39950.0,42350.0,563283.0,23584920000.0,1952793862250.0,46110835,KOSPI
2024-03-21,43000.0,49200.0,42850.0,47050.0,2039716.0,95044578800.0,2169514786750.0,46110835,KOSPI
2024-03-27,49550.0,52400.0,49150.0,51000.0,528464.0,27023694750.0,2351652585000.0,46110835,KOSPI
2024-04-18,40650.0,42600.0,40400.0,42000.0,193288.0,8072944250.0,1936655070000.0,46110835,KOSPI
2024-06-18,58000.0,59200.0,56700.0,57300.0,565460.0,32760920400.0,2642150845500.0,46110835,KOSPI
2024-08-05,36100.0,36750.0,30500.0,32200.0,468908.0,15821669100.0,1484768887000.0,46110835,KOSPI
2024-09-05,40050.0,45650.0,40050.0,43000.0,1121196.0,48476794250.0,1982765905000.0,46110835,KOSPI
```

Backtest:

| window | peak/high | peak date | trough/low | trough date | MFE | MAE |
|---|---:|---|---:|---|---:|---:|
| 30 calendar days | 52400 | 2024-03-27 | 40400 | 2024-04-18 | +21.86% | -6.05% |
| 90 calendar days | 59200 | 2024-06-18 | 40400 | 2024-04-18 | +37.67% | -6.05% |
| 180 calendar days | 59200 | 2024-06-18 | 30500 | 2024-08-05 | +37.67% | -29.07% |

Interpretation:

```text
020150 is the first-window-MFE / later-drawdown C13 branch.
The copper-foil utilization thesis was tradable, but 180D MAE widened enough to block Green while evidence remains source-proxy-only.
This should remain Stage2-Guarded until customer volume, utilization, ASP/spread, and margin evidence is repaired.
```

### 6.3 `005070` 코스모신소재 — cathode material utilization weak-MFE / high-MAE path

Trigger:

```text
trigger_date = 2024-03-08
trigger_type = Stage2-FalsePositive-Candidate
trigger_family = cathode_material_utilization_ira_ampc_weak_mfe_later_high_mae
entry_date = 2024-03-11
entry_price = 165500.0
entry_price_type = next_tradable_open_after_cathode_material_utilization_policy_rebound
```

Relevant Stock-Web rows:

```csv
d,o,h,l,c,v,a,mc,s,m
2024-03-08,171100.0,174900.0,165000.0,166900.0,251888.0,42260212100.0,5426045176400.0,32510756,KOSPI
2024-03-11,165500.0,169100.0,164000.0,167600.0,116274.0,19465645000.0,5448802705600.0,32510756,KOSPI
2024-03-15,173700.0,181000.0,172000.0,177200.0,244436.0,43317104000.0,5760905963200.0,32510756,KOSPI
2024-04-08,149700.0,153800.0,147000.0,152200.0,181289.0,27265261700.0,4948137063200.0,32510756,KOSPI
2024-05-24,139100.0,139200.0,136800.0,137000.0,148929.0,20467908800.0,4453973572000.0,32510756,KOSPI
2024-08-05,124900.0,124900.0,100100.0,106800.0,482707.0,54265885300.0,3472148740800.0,32510756,KOSPI
2024-09-06,111100.0,113200.0,102800.0,103400.0,219139.0,23285829700.0,3361612170400.0,32510756,KOSPI
```

Backtest:

| window | peak/high | peak date | trough/low | trough date | MFE | MAE |
|---|---:|---|---:|---|---:|---:|
| 30 calendar days | 181000 | 2024-03-15 | 147000 | 2024-04-08 | +9.37% | -11.18% |
| 90 calendar days | 181000 | 2024-03-15 | 136800 | 2024-05-24 | +9.37% | -17.34% |
| 180 calendar days | 181000 | 2024-03-15 | 100100 | 2024-08-05 | +9.37% | -39.52% |

Interpretation:

```text
005070 is the weak-MFE high-MAE C13 counterexample.
The utilization/policy rebound label existed, but forward MFE stayed below +10% and 180D MAE widened to almost -40%.
This should block Stage2 unless a later independent trigger repairs customer volume, qualified capacity, and margin evidence.
```

### 6.4 `006110` 삼아알미늄 — battery foil utilization label with near-zero MFE and extreme MAE

Trigger:

```text
trigger_date = 2024-03-07
trigger_type = Stage2-FalsePositive-Candidate
trigger_family = battery_foil_utilization_ira_ampc_weak_mfe_extreme_mae
entry_date = 2024-03-08
entry_price = 98000.0
entry_price_type = next_tradable_open_after_battery_foil_utilization_policy_spike
```

Relevant Stock-Web rows:

```csv
d,o,h,l,c,v,a,mc,s,m
2024-03-07,93500.0,98000.0,93100.0,96400.0,60975.0,5846241500.0,1418228702400.0,14711916,KOSPI
2024-03-08,98000.0,98100.0,92500.0,92500.0,84043.0,7937085300.0,1360852230000.0,14711916,KOSPI
2024-04-05,82000.0,82600.0,80600.0,81000.0,44323.0,3598741800.0,1191665196000.0,14711916,KOSPI
2024-05-24,67500.0,74800.0,66000.0,72700.0,245274.0,17220521100.0,1069556293200.0,14711916,KOSPI
2024-08-05,48100.0,49000.0,39600.0,42000.0,132511.0,5799648700.0,617900472000.0,14711916,KOSPI
2024-09-06,47000.0,47000.0,42350.0,42700.0,57607.0,2509395000.0,628198813200.0,14711916,KOSPI
```

Backtest:

| window | peak/high | peak date | trough/low | trough date | MFE | MAE |
|---|---:|---|---:|---|---:|---:|
| 30 calendar days | 98100 | 2024-03-08 | 80600 | 2024-04-05 | +0.10% | -17.76% |
| 90 calendar days | 98100 | 2024-03-08 | 66000 | 2024-05-24 | +0.10% | -32.65% |
| 180 calendar days | 98100 | 2024-03-08 | 39600 | 2024-08-05 | +0.10% | -59.59% |

Interpretation:

```text
006110 is the hard C13 extreme-MAE counterexample.
The battery-foil utilization label peaked at entry and never delivered forward MFE.
This should block Stage2 or route to 4B/4C high-MAE watch until customer call-off, utilization, shipment, spread, and margin evidence is repaired.
```

---

## 7. Machine-readable trigger JSONL

```jsonl
{"row_type":"trigger","research_id":"R3L77_C13_BATTERY_MATERIAL_UTILIZATION_ROUTER","round":"R3","loop":77,"large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C13_BATTERY_JV_UTILIZATION_AMPC_IRA","fine_archetype_id":"COPPER_FOIL_CATHODE_FOIL_UTILIZATION_AMPC_IRA_HIGH_MAE_ROUTER","symbol":"011790","name":"SKC","trigger_type":"Stage2-Actionable","trigger_family":"copper_foil_ira_ampc_utilization_customer_quality_high_mfe_low_mae_rerating","trigger_date":"2024-03-08","entry_date":"2024-03-11","entry_price":104500.0,"entry_price_type":"next_tradable_open_after_copper_foil_ira_ampc_utilization_burst","price_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","mfe_30d_pct":43.25,"mae_30d_pct":-3.35,"mfe_90d_pct":49.57,"mae_90d_pct":-3.35,"mfe_180d_pct":91.39,"mae_180d_pct":-3.35,"peak_price_180d":200000.0,"peak_date_180d":"2024-06-18","trough_price_180d":101000.0,"trough_date_180d":"2024-03-11","calibration_usable":true,"case_polarity":"positive_anchor_copper_foil_utilization_low_mae","evidence_url_pending":true,"source_proxy_only":true,"non_price_evidence_strength":"medium_pending_url_repair","price_only_blowoff":false,"expected_stage_current_profile":"Stage2-Actionable_to_Yellow_after_customer_calloff_utilization_margin_bridge_repaired","residual_error_type":"copper_foil_ira_ampc_utilization_path_supports_positive_route_but_green_requires_url_repaired_customer_calloff_utilization_margin_bridge"}
{"row_type":"trigger","research_id":"R3L77_C13_BATTERY_MATERIAL_UTILIZATION_ROUTER","round":"R3","loop":77,"large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C13_BATTERY_JV_UTILIZATION_AMPC_IRA","fine_archetype_id":"COPPER_FOIL_CATHODE_FOIL_UTILIZATION_AMPC_IRA_HIGH_MAE_ROUTER","symbol":"020150","name":"롯데에너지머티리얼즈","trigger_type":"Stage2-Actionable-Guarded","trigger_family":"copper_foil_utilization_ira_ampc_first_window_mfe_later_drawdown","trigger_date":"2024-03-20","entry_date":"2024-03-21","entry_price":43000.0,"entry_price_type":"next_tradable_open_after_copper_foil_utilization_ira_ampc_burst","price_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","mfe_30d_pct":21.86,"mae_30d_pct":-6.05,"mfe_90d_pct":37.67,"mae_90d_pct":-6.05,"mfe_180d_pct":37.67,"mae_180d_pct":-29.07,"peak_price_180d":59200.0,"peak_date_180d":"2024-06-18","trough_price_180d":30500.0,"trough_date_180d":"2024-08-05","calibration_usable":true,"case_polarity":"positive_guarded_first_window_mfe_later_drawdown","evidence_url_pending":true,"source_proxy_only":true,"non_price_evidence_strength":"medium_low_pending_url_repair","price_only_blowoff":false,"expected_stage_current_profile":"Stage2-Guarded_to_Yellow_only_if_copper_foil_customer_volume_spread_margin_bridge_repaired","residual_error_type":"copper_foil_utilization_had_mfe_but_later_mae_requires_url_repaired_customer_volume_spread_margin_bridge_before_yellow_green"}
{"row_type":"trigger","research_id":"R3L77_C13_BATTERY_MATERIAL_UTILIZATION_ROUTER","round":"R3","loop":77,"large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C13_BATTERY_JV_UTILIZATION_AMPC_IRA","fine_archetype_id":"COPPER_FOIL_CATHODE_FOIL_UTILIZATION_AMPC_IRA_HIGH_MAE_ROUTER","symbol":"005070","name":"코스모신소재","trigger_type":"Stage2-FalsePositive-Candidate","trigger_family":"cathode_material_utilization_ira_ampc_weak_mfe_later_high_mae","trigger_date":"2024-03-08","entry_date":"2024-03-11","entry_price":165500.0,"entry_price_type":"next_tradable_open_after_cathode_material_utilization_policy_rebound","price_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","mfe_30d_pct":9.37,"mae_30d_pct":-11.18,"mfe_90d_pct":9.37,"mae_90d_pct":-17.34,"mfe_180d_pct":9.37,"mae_180d_pct":-39.52,"peak_price_180d":181000.0,"peak_date_180d":"2024-03-15","trough_price_180d":100100.0,"trough_date_180d":"2024-08-05","calibration_usable":true,"case_polarity":"counterexample_weak_mfe_high_mae","evidence_url_pending":true,"source_proxy_only":true,"non_price_evidence_strength":"low_pending_url_repair","price_only_blowoff":false,"expected_stage_current_profile":"blocked_Stage2_or_local_4B_high_MAE_watch_until_utilization_customer_volume_margin_bridge_repaired","residual_error_type":"cathode_material_utilization_policy_rebound_had_weak_mfe_and_high_mae_without_customer_volume_margin_bridge"}
{"row_type":"trigger","research_id":"R3L77_C13_BATTERY_MATERIAL_UTILIZATION_ROUTER","round":"R3","loop":77,"large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C13_BATTERY_JV_UTILIZATION_AMPC_IRA","fine_archetype_id":"COPPER_FOIL_CATHODE_FOIL_UTILIZATION_AMPC_IRA_HIGH_MAE_ROUTER","symbol":"006110","name":"삼아알미늄","trigger_type":"Stage2-FalsePositive-Candidate","trigger_family":"battery_foil_utilization_ira_ampc_weak_mfe_extreme_mae","trigger_date":"2024-03-07","entry_date":"2024-03-08","entry_price":98000.0,"entry_price_type":"next_tradable_open_after_battery_foil_utilization_policy_spike","price_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","mfe_30d_pct":0.1,"mae_30d_pct":-17.76,"mfe_90d_pct":0.1,"mae_90d_pct":-32.65,"mfe_180d_pct":0.1,"mae_180d_pct":-59.59,"peak_price_180d":98100.0,"peak_date_180d":"2024-03-08","trough_price_180d":39600.0,"trough_date_180d":"2024-08-05","calibration_usable":true,"case_polarity":"counterexample_weak_mfe_extreme_mae","evidence_url_pending":true,"source_proxy_only":true,"non_price_evidence_strength":"low_pending_url_repair","price_only_blowoff":true,"expected_stage_current_profile":"blocked_Stage2_or_4B_4C_high_MAE_watch_until_customer_calloff_utilization_margin_bridge_repaired","residual_error_type":"battery_foil_utilization_label_had_entry_peak_near_zero_mfe_and_extreme_mae_without_calloff_utilization_margin_bridge"}
```

---

## 8. Score simulation and raw component breakdown

This is shadow-only and does not change production scoring.

| symbol | IRA/AMPC/JV relevance | customer call-off | utilization / qualified capacity | ASP/spread / pass-through | market mispricing | margin / cash conversion | information confidence | shadow total | intended route |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| `011790` | 12 | 9 | 10 | 9 | 14 | 8 | 6 | 68 | Stage2/Yellow after evidence repair |
| `020150` | 11 | 6 | 7 | 6 | 9 | 5 | 5 | 49 | Stage2-Guarded only until evidence repair |
| `005070` | 8 | 3 | 3 | 3 | 2 | 2 | 4 | 25 | blocked Stage2 / local 4B watch |
| `006110` | 7 | 2 | 2 | 2 | 0 | 1 | 4 | 18 | blocked Stage2 / 4B-4C high-MAE watch |

### Current calibrated profile stress test

The current calibrated profile already blocks pure price-only blowoff.  
The remaining C13 issue is **IRA/AMPC/utilization label without customer call-off and margin conversion**:

```text
C13 clean utilization path:
  IRA/AMPC/JV/utilization relevance
  + MFE_90D >= +35%
  + MAE_90D > -8%
  + evidence remains source_proxy_only
  => Stage2-Actionable / Yellow watch after evidence repair

C13 first-window-MFE later-drawdown path:
  copper-foil utilization MFE appears
  + MAE_180D <= -25%
  + customer volume and spread bridge missing
  => Stage2-Guarded at most, no Green

C13 weak-MFE high-MAE material path:
  material/utilization label exists
  + MFE_90D < +10%
  + MAE_180D <= -35%
  + no customer volume / margin evidence
  => block Stage2 or local 4B watch

C13 entry-peak extreme-MAE foil path:
  peak occurs at entry
  + MFE_30D < +3%
  + MAE_180D <= -50%
  + evidence remains source_proxy_only
  => block Stage2 and route to 4B/4C high-MAE watch
```

`011790` and `020150` prevent overblocking.  
`005070` and `006110` show why utilization labels should not be promoted without customer releases, actual operating rate, spread, and margin evidence.

---

## 9. Aggregate metrics

```json
{
  "row_type": "aggregate",
  "research_id": "R3L77_C13_BATTERY_MATERIAL_UTILIZATION_ROUTER",
  "round": "R3",
  "loop": 77,
  "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY",
  "canonical_archetype_id": "C13_BATTERY_JV_UTILIZATION_AMPC_IRA",
  "fine_archetype_id": "COPPER_FOIL_CATHODE_FOIL_UTILIZATION_AMPC_IRA_HIGH_MAE_ROUTER",
  "case_count": 4,
  "calibration_usable_case_count": 4,
  "positive_case_count": 2,
  "counterexample_count": 2,
  "new_symbol_count": 4,
  "source_proxy_only_count": 4,
  "evidence_url_pending_count": 4,
  "avg_mfe_30d_pct": 18.65,
  "avg_mae_30d_pct": -9.58,
  "avg_mfe_90d_pct": 24.18,
  "avg_mae_90d_pct": -14.85,
  "avg_mfe_180d_pct": 34.63,
  "avg_mae_180d_pct": -32.88,
  "max_mfe_180d_pct": 91.39,
  "worst_mae_180d_pct": -59.59
}
```

---

## 10. 4B proximity split

```json
{
  "row_type": "4b_split",
  "research_id": "R3L77_C13_BATTERY_MATERIAL_UTILIZATION_ROUTER",
  "stage2_positive_or_yellow_candidate": [
    {
      "symbol": "011790",
      "reason": "copper-foil utilization path had +91.39% 180D MFE with only -3.35% MAE"
    }
  ],
  "stage2_guarded_or_local_4b_watch": [
    {
      "symbol": "020150",
      "reason": "copper-foil path had +37.67% MFE but 180D MAE reached -29.07%; requires customer-volume/spread bridge repair"
    }
  ],
  "blocked_stage2_or_local_4b_watch": [
    {
      "symbol": "005070",
      "reason": "cathode material path had only +9.37% MFE and -39.52% 180D MAE"
    }
  ],
  "blocked_stage2_or_4c_watch": [
    {
      "symbol": "006110",
      "reason": "battery foil path had only +0.10% MFE and -59.59% 180D MAE"
    }
  ],
  "full_4b_or_green_requires_non_price_evidence": [
    "customer call-off and release schedule",
    "actual utilization / operating-rate proof",
    "qualified capacity and customer acceptance",
    "IRA/AMPC eligibility and unit economics",
    "ASP/spread and input-cost pass-through",
    "working capital and cash-flow conversion"
  ]
}
```

---

## 11. Shadow rule candidate

```yaml
row_type: canonical_archetype_rule_candidate
canonical_archetype_id: C13_BATTERY_JV_UTILIZATION_AMPC_IRA
fine_archetype_id: COPPER_FOIL_CATHODE_FOIL_UTILIZATION_AMPC_IRA_HIGH_MAE_ROUTER
rule_name: C13_copper_foil_cathode_foil_utilization_ampc_ira_high_mae_router
production_scoring_changed: false
shadow_weight_only: true
```

### Proposed routing logic

```text
For C13 copper foil / cathode / battery foil utilization and IRA-AMPC cases:

Tier A: verified utilization winner
  Conditions:
    - customer call-off, utilization, qualified capacity, spread, and margin evidence are URL-repaired
    - MFE_90D >= +35%
    - MAE_90D > -8%
  Routing:
    - Stage2-Actionable allowed
    - Stage3-Yellow allowed after evidence repair
    - Green only after call-off / utilization / margin bridge is verified

Tier B: first-window-MFE later-drawdown utilization case
  Conditions:
    - MFE_90D >= +25%
    - MAE_180D <= -25%
    - evidence_url_pending or source_proxy_only remains true
  Routing:
    - Stage2-Guarded at most
    - no Green until evidence repair

Tier C: weak-MFE high-MAE material utilization label
  Conditions:
    - MFE_90D < +10%
    - MAE_180D <= -35%
    - no repaired customer-volume / margin bridge
  Routing:
    - block Stage2
    - local 4B/high-MAE watch

Tier D: entry-peak extreme-MAE foil label
  Conditions:
    - MFE_30D < +3%
    - MAE_180D <= -50%
    - no repaired utilization / call-off bridge
  Routing:
    - block Stage2
    - route to 4B/4C high-MAE watch
```

### Suggested shadow delta

```json
{
  "row_type": "shadow_weight",
  "axis": "c13_copper_foil_cathode_foil_utilization_ampc_ira_high_mae_router",
  "scope": "canonical_archetype_id:C13_BATTERY_JV_UTILIZATION_AMPC_IRA",
  "proposal": {
    "source_proxy_only_green_allowed": false,
    "ira_ampc_utilization_label_alone_stage2_allowed": false,
    "customer_calloff_utilization_margin_bridge_required_for_green": true,
    "verified_utilization_winner_mfe90_threshold_pct": 35.0,
    "verified_utilization_winner_mae90_min_pct": -8.0,
    "first_window_mfe_threshold_90d_pct": 25.0,
    "later_drawdown_mae180_threshold_pct": -25.0,
    "weak_mfe_threshold_90d_pct": 10.0,
    "weak_mfe_high_mae180_threshold_pct": -35.0,
    "entry_peak_mfe30_threshold_pct": 3.0,
    "entry_peak_extreme_mae180_threshold_pct": -50.0,
    "positive_weight_blocked_until_url_repair": true
  },
  "confidence": "medium_low_until_url_repair",
  "apply_now": false,
  "reason": "Two copper-foil utilization holdouts and two cathode/foil weak-MFE high-MAE failures show that C13 should require URL-repaired customer call-off, actual utilization, qualified capacity, spread, and margin evidence before Yellow/Green."
}
```

---

## 12. Residual contribution summary

```json
{
  "row_type": "residual_contribution",
  "research_id": "R3L77_C13_BATTERY_MATERIAL_UTILIZATION_ROUTER",
  "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY",
  "canonical_archetype_id": "C13_BATTERY_JV_UTILIZATION_AMPC_IRA",
  "contribution": "Adds four C13 battery material / copper-foil / foil utilization cases and separates a clean low-MAE copper-foil utilization winner from first-window-MFE later-drawdown and weak-MFE high-MAE material-label failures. C13 Yellow/Green should require URL-repaired customer call-off, utilization, qualified capacity, IRA/AMPC unit economics, ASP/spread, pass-through, working-capital, and cash-margin evidence.",
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
  "data_quality_blocker": "All four non-price battery material/utilization triggers require URL-level repair before positive weight promotion.",
  "guardrail_added": "C13 source_proxy_only cases with MFE_90D < +10% and MAE_180D <= -35% should block Stage2; entry-peak foil cases with MFE_30D < +3% and MAE_180D <= -50% should route to 4B/4C high-MAE watch."
}
```

One-line contribution:

```text
This loop adds 4 new independent cases, 2 counterexamples, and 2 residual errors for R3/L3_BATTERY_EV_GREEN_MOBILITY/C13_BATTERY_JV_UTILIZATION_AMPC_IRA.
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
    011790: false
    020150: false
    005070: false
    006110: false
  evidence_url_pending:
    011790: true
    020150: true
    005070: true
    006110: true
  source_proxy_only:
    011790: true
    020150: true
    005070: true
    006110: true
```

Limitations:

```text
- Price path is validated against Stock-Web tradable OHLC rows.
- Non-price evidence is not URL-repaired in this run.
- Therefore this artifact is useful for C13 battery material utilization / IRA-AMPC residual shape and high-MAE guardrail design, but should not promote positive weights until filings, IR, customer/call-off data, utilization disclosures, order disclosures, export data, or reports verify customer releases, qualified capacity, actual utilization, ASP/spread, pass-through, working capital, and cash-margin conversion.
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
2. Preserve R3 / loop 77 metadata.
3. Add the cases to C13_BATTERY_JV_UTILIZATION_AMPC_IRA only if parser validation passes.
4. Treat all four non-price triggers as evidence_url_pending=true and source_proxy_only=true until URL-level evidence is repaired.
5. Do not use these rows for positive weight promotion until filings/IR/customer-calloff/utilization/order-disclosure/export-data/report data verifies customer releases, qualified capacity, actual utilization, IRA/AMPC unit economics, ASP/spread, pass-through, working capital, and cash-margin conversion.
6. Add a shadow-only rule candidate named C13_copper_foil_cathode_foil_utilization_ampc_ira_high_mae_router.
7. Do not loosen Stage3-Green.
8. Add C13-specific guards:
   - source_proxy_only -> no Green
   - IRA/AMPC/utilization label alone -> no Stage2 promotion
   - Green requires repaired customer call-off / utilization / margin bridge
   - MFE_90D >= +35% and MAE_90D > -8% may remain Stage2-Actionable / Yellow watch after evidence repair
   - MFE_90D >= +25% but MAE_180D <= -25% -> Stage2-Guarded at most until evidence repair
   - MFE_90D < +10% and MAE_180D <= -35% -> block Stage2 / local 4B watch
   - MFE_30D < +3% and MAE_180D <= -50% -> block Stage2 / 4B-4C high-MAE watch
9. Keep production scoring unchanged unless later batch promotion logic independently marks this axis safe.
```

---

## 15. Next round state

```text
completed_round = R3
completed_loop = 77
next_round = R4
next_loop = 77
next_large_sector_hint = L4_MATERIALS_SPREAD_RESOURCE
round_schedule_status = valid
round_sector_consistency = pass
```
