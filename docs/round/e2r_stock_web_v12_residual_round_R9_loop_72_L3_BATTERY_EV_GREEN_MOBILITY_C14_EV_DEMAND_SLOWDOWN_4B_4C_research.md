# E2R Stock-Web v12 Residual Research — R9 Loop 72

```yaml
research_session: post_calibrated_sector_archetype_residual_research
mode: historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12
completed_round: R9
completed_loop: 72
next_round: R10
next_loop: 72
large_sector_id: L3_BATTERY_EV_GREEN_MOBILITY
canonical_archetype_id: C14_EV_DEMAND_SLOWDOWN_4B_4C
fine_archetype_id: BATTERY_MATERIAL_EQUIPMENT_RELIEF_RALLY_HIGH_MAE_GUARD
output_file: e2r_stock_web_v12_residual_round_R9_loop_72_L3_BATTERY_EV_GREEN_MOBILITY_C14_EV_DEMAND_SLOWDOWN_4B_4C_research.md
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

The active prompt fixes the research mode:

```text
primary_price_source = Songdaiki/stock-web
price_basis = tradable_raw
price_adjustment_status = raw_unadjusted_marcap

production_scoring_changed = false
shadow_weight_only = true
must_use_actual_stock_web_1D_OHLC = true
must_include_backtest_result = true
must_output_every_usable_trigger_as_jsonl = true
```

### Round resolution

The immediately preceding completed scheduled artifact in this automation chain was:

```text
completed_round = R8
completed_loop = 72
large_sector_id = L8_PLATFORM_CONTENT_SW_SECURITY
canonical_archetype_id = C28_SOFTWARE_SECURITY_CONTRACT_RETENTION
```

Therefore:

```text
scheduled_round = R9
scheduled_loop = 72
```

R9 permits:

```text
large_sector_id = L3_BATTERY_EV_GREEN_MOBILITY
or
large_sector_id = L9_CONSTRUCTION_REALESTATE_HOUSING
```

This run selects the L3 branch:

```text
large_sector_id = L3_BATTERY_EV_GREEN_MOBILITY
canonical_archetype_id = C14_EV_DEMAND_SLOWDOWN_4B_4C
```

This is a valid R9 pairing.

---

## 1. Why this R9/C14 run

The no-repeat ledger shows C14 is already heavily represented, but it is concentrated in the core cell/cathode names:

```text
C14_EV_DEMAND_SLOWDOWN_4B_4C:
  rows: 70
  symbols: 15
  date_range: 2023-02-22~2024-12-20
  good/bad S2: 0/0
  4B/4C: 29/32
  URL/proxy: 0/0
  top covered symbols: 247540(13), 003670(10), 066970(10), 373220(7), 361610(6), 011790(5)
```

This run avoids those top-covered names and tests less-repeated battery material/equipment adjacency:

```text
278280 천보
095500 미래나노텍
222080 씨아이에스
```

The residual question is:

```text
When EV/battery names produce a relief rally after a prior drawdown, can C14 prevent the model from mistaking reflexive MFE for real Stage2/Green recovery?
```

C14 is a protection archetype.  
Its “positive” contribution is often not a long-positive result; it is a guardrail-positive result: correctly blocking or downgrading apparent Stage2 when EV-demand/call-off pressure later creates severe MAE.

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
| `278280` | 천보 | active_like; KOSDAQ/KOSDAQ GLOBAL history | none listed | true |
| `095500` | 미래나노텍 | active_like; KOSDAQ | no 2024 overlap; only old 2007~2009 candidates | true |
| `222080` | 씨아이에스 | active_like; KOSDAQ | no 2024 overlap; old 2017 SPAC transition candidate only | true |

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
The Stock-Web price path is fully validated, but company-level EV-demand, customer call-off, electrolyte/additive pricing, lithium-processing margin, equipment order timing, utilization, and cancellation/delay evidence still require later URL repair through filings, IR, disclosures, customs data, or sell-side reports before any production weight promotion.
```

C14 interpretation used here:

```text
C14 is not just “battery stocks went down.”
It tests the model's ability to protect against a false recovery:
- relief rally after heavy drawdown,
- customer demand slowdown,
- order/capex delay,
- margin pressure,
- inventory correction,
- and 4B/4C timing.
```

Therefore this run is useful as a guardrail/residual artifact, not as a positive production patch.

---

## 4. No-repeat and novelty check

Hard duplicate key:

```text
canonical_archetype_id + symbol + trigger_type + entry_date
```

Searches performed before writing:

```text
278280 + C14_EV_DEMAND_SLOWDOWN_4B_4C -> no direct match found
095500 + C14_EV_DEMAND_SLOWDOWN_4B_4C -> no direct match found
222080 + C14_EV_DEMAND_SLOWDOWN_4B_4C -> no direct match found
```

Novelty accounting:

```json
{
  "new_symbol_count": 3,
  "minimum_new_symbol_count": 2,
  "guardrail_positive_case_count": 1,
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
| `R9L72_C14_278280_20240611` | `278280` 천보 | electrolyte/material relief rally into EV demand weakness | guardrail-positive C14 block / 4B-4C watch |
| `R9L72_C14_095500_20240214` | `095500` 미래나노텍 | battery-material/lithium-processing squeeze before later demand fade | high-MFE / high-MAE false recovery counterexample |
| `R9L72_C14_222080_20240305` | `222080` 씨아이에스 | equipment-order relief rally before capex/demand slowdown | delayed high-MAE counterexample |

The intended residual:

```text
C14 should separate:
1. clean recovery with verified demand/order/margin repair; and
2. reflexive relief rallies where MFE appears first, but customer demand, margin, or capex slowdown later dominates the path.
```

No case in this file should be treated as Stage3-Green without URL-repaired non-price evidence.

---

## 6. Stock-Web OHLC and backtest

### 6.1 `278280` 천보 — electrolyte/material relief rally that should be blocked from Green

Trigger:

```text
trigger_date = 2024-06-10
trigger_type = 4B-4C-watch
trigger_family = electrolyte_material_relief_rally_ev_slowdown_guard
entry_date = 2024-06-11
entry_price = 74700.0
entry_price_type = next_tradable_open
```

Relevant Stock-Web rows:

```csv
d,o,h,l,c,v,a,mc,s,m
2024-06-10,76000.0,76300.0,74600.0,75000.0,21490.0,1618239800.0,750000000000.0,10000000,KOSDAQ GLOBAL
2024-06-11,74700.0,81200.0,74600.0,79100.0,104506.0,8284875100.0,791000000000.0,10000000,KOSDAQ GLOBAL
2024-06-12,79100.0,82200.0,77800.0,78000.0,66521.0,5289492600.0,780000000000.0,10000000,KOSDAQ GLOBAL
2024-06-25,71400.0,72500.0,71000.0,71200.0,18383.0,1313847600.0,712000000000.0,10000000,KOSDAQ
2024-07-08,77200.0,81500.0,76400.0,78100.0,82140.0,6504102700.0,781000000000.0,10000000,KOSDAQ
2024-07-17,69700.0,72000.0,67600.0,67600.0,61245.0,4205234100.0,676000000000.0,10000000,KOSDAQ
2024-08-05,60600.0,60800.0,49000.0,50400.0,99184.0,5352917450.0,504000000000.0,10000000,KOSDAQ
2024-10-07,62700.0,65500.0,62300.0,65300.0,42212.0,2727560900.0,653000000000.0,10000000,KOSDAQ
```

Backtest:

| window | peak/high | peak date | trough/low | trough date | MFE | MAE |
|---|---:|---|---:|---|---:|---:|
| 30 calendar days | 82200 | 2024-06-12 | 71000 | 2024-06-25 | +10.04% | -4.95% |
| 90 calendar days | 82200 | 2024-06-12 | 49000 | 2024-08-05 | +10.04% | -34.40% |
| 180 calendar days | 82200 | 2024-06-12 | 49000 | 2024-08-05 | +10.04% | -34.40% |

Interpretation:

```text
278280 is a guardrail-positive C14 case.
The 30D path looked only modestly positive and later converted into severe MAE.
This is exactly the case where C14 should prevent a relief rally from becoming Stage2/Green without confirmed EV-demand and margin repair.
```

### 6.2 `095500` 미래나노텍 — high-MFE material squeeze that later becomes high-MAE

Trigger:

```text
trigger_date = 2024-02-13
trigger_type = Stage2-FalsePositive-Candidate
trigger_family = battery_material_lithium_processing_squeeze_before_demand_fade
entry_date = 2024-02-14
entry_price = 14000.0
entry_price_type = next_tradable_open
```

Relevant Stock-Web rows:

```csv
d,o,h,l,c,v,a,mc,s,m
2024-02-13,14040.0,14400.0,14020.0,14110.0,194393.0,2750706490.0,437551085890.0,31009999,KOSDAQ
2024-02-14,14000.0,17140.0,13880.0,16080.0,5898345.0,96519749510.0,498640783920.0,31009999,KOSDAQ
2024-02-20,18140.0,20550.0,17610.0,19380.0,11414121.0,222497908050.0,600973780620.0,31009999,KOSDAQ
2024-02-28,19460.0,23000.0,19120.0,22100.0,15530428.0,332588920480.0,685320977900.0,31009999,KOSDAQ
2024-03-07,22750.0,25250.0,22050.0,22600.0,3702148.0,88029933900.0,700825977400.0,31009999,KOSDAQ
2024-04-05,16680.0,16910.0,16260.0,16280.0,498058.0,8223162590.0,504842783720.0,31009999,KOSDAQ
2024-08-05,11430.0,11450.0,9100.0,9710.0,538739.0,5542281790.0,301107090290.0,31009999,KOSDAQ
2024-09-10,10050.0,10280.0,9720.0,9720.0,167295.0,1659603570.0,301417190280.0,31009999,KOSDAQ
```

Backtest:

| window | peak/high | peak date | trough/low | trough date | MFE | MAE |
|---|---:|---|---:|---|---:|---:|
| 30 calendar days | 25250 | 2024-03-07 | 13880 | 2024-02-14 | +80.36% | -0.86% |
| 90 calendar days | 25250 | 2024-03-07 | 13880 | 2024-02-14 | +80.36% | -0.86% |
| 180 calendar days | 25250 | 2024-03-07 | 9100 | 2024-08-05 | +80.36% | -35.00% |

Interpretation:

```text
095500 is the strongest high-MFE / high-MAE false-recovery example.
A model that only looks at 30D MFE would over-reward this setup.
C14 should instead mark it as a 4B/4C watch unless there is hard evidence of demand, price, volume, and margin repair.
```

### 6.3 `222080` 씨아이에스 — equipment-order relief rally before delayed high-MAE

Trigger:

```text
trigger_date = 2024-03-04
trigger_type = Stage2-Actionable-Guarded
trigger_family = battery_equipment_order_relief_rally_before_capex_slowdown
entry_date = 2024-03-05
entry_price = 10820.0
entry_price_type = next_tradable_open
```

Relevant Stock-Web rows:

```csv
d,o,h,l,c,v,a,mc,s,m
2024-03-04,11120.0,11210.0,10940.0,10990.0,345462.0,3807509720.0,772131155880.0,70257612,KOSDAQ
2024-03-05,10820.0,13800.0,10820.0,13150.0,14218962.0,181676790090.0,923887597800.0,70257612,KOSDAQ
2024-03-11,13750.0,15110.0,13750.0,14300.0,13951166.0,202474876820.0,1004683851600.0,70257612,KOSDAQ
2024-04-17,10410.0,10590.0,10330.0,10340.0,432795.0,4520284780.0,738698657840.0,71440876,KOSDAQ
2024-06-10,11650.0,12700.0,11520.0,11840.0,3770117.0,45618141480.0,845859971840.0,71440876,KOSDAQ
2024-07-22,9650.0,9670.0,9270.0,9270.0,428159.0,4011317990.0,664930861290.0,71729327,KOSDAQ
2024-08-05,9100.0,9190.0,7800.0,8000.0,956215.0,8113943820.0,573834616000.0,71729327,KOSDAQ
2024-08-20,10870.0,12230.0,10760.0,11470.0,13882361.0,160427467170.0,822735380690.0,71729327,KOSDAQ
```

Backtest:

| window | peak/high | peak date | trough/low | trough date | MFE | MAE |
|---|---:|---|---:|---|---:|---:|
| 30 calendar days | 15110 | 2024-03-11 | 10820 | 2024-03-05 | +39.65% | +0.00% |
| 90 calendar days | 15110 | 2024-03-11 | 10330 | 2024-04-17 | +39.65% | -4.53% |
| 180 calendar days | 15110 | 2024-03-11 | 7800 | 2024-08-05 | +39.65% | -27.91% |

Interpretation:

```text
222080 looks healthier than 278280 or 095500 in the first 30/90 days.
But the 180D path still carries a large delayed MAE.
The correct C14 route is Stage2-Actionable-Guarded or local 4B watch until equipment order durability, customer capex timing, and margin conversion are URL-repaired.
```

---

## 7. Machine-readable trigger JSONL

```jsonl
{"row_type":"trigger","research_id":"R9L72_C14_EV_SLOWDOWN_RELIEF_RALLY_GUARD","round":"R9","loop":72,"large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C14_EV_DEMAND_SLOWDOWN_4B_4C","fine_archetype_id":"BATTERY_MATERIAL_EQUIPMENT_RELIEF_RALLY_HIGH_MAE_GUARD","symbol":"278280","name":"천보","trigger_type":"4B-4C-watch","trigger_family":"electrolyte_material_relief_rally_ev_slowdown_guard","trigger_date":"2024-06-10","entry_date":"2024-06-11","entry_price":74700.0,"entry_price_type":"next_tradable_open","price_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","mfe_30d_pct":10.04,"mae_30d_pct":-4.95,"mfe_90d_pct":10.04,"mae_90d_pct":-34.40,"mfe_180d_pct":10.04,"mae_180d_pct":-34.40,"peak_price_180d":82200.0,"peak_date_180d":"2024-06-12","trough_price_180d":49000.0,"trough_date_180d":"2024-08-05","calibration_usable":true,"case_polarity":"guardrail_positive","evidence_url_pending":true,"source_proxy_only":true,"non_price_evidence_strength":"low_pending_url_repair","price_only_blowoff":false,"expected_stage_current_profile":"4B_4C_watch_or_blocked_positive_stage","residual_error_type":"relief_rally_low_mfe_severe_mae_should_block_stage2_green"}
{"row_type":"trigger","research_id":"R9L72_C14_EV_SLOWDOWN_RELIEF_RALLY_GUARD","round":"R9","loop":72,"large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C14_EV_DEMAND_SLOWDOWN_4B_4C","fine_archetype_id":"BATTERY_MATERIAL_EQUIPMENT_RELIEF_RALLY_HIGH_MAE_GUARD","symbol":"095500","name":"미래나노텍","trigger_type":"Stage2-FalsePositive-Candidate","trigger_family":"battery_material_lithium_processing_squeeze_before_demand_fade","trigger_date":"2024-02-13","entry_date":"2024-02-14","entry_price":14000.0,"entry_price_type":"next_tradable_open","price_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","mfe_30d_pct":80.36,"mae_30d_pct":-0.86,"mfe_90d_pct":80.36,"mae_90d_pct":-0.86,"mfe_180d_pct":80.36,"mae_180d_pct":-35.00,"peak_price_180d":25250.0,"peak_date_180d":"2024-03-07","trough_price_180d":9100.0,"trough_date_180d":"2024-08-05","calibration_usable":true,"case_polarity":"counterexample_high_mfe_high_mae","evidence_url_pending":true,"source_proxy_only":true,"non_price_evidence_strength":"low_pending_url_repair","price_only_blowoff":false,"expected_stage_current_profile":"local_4B_watch_then_4C_risk_if_demand_bridge_not_repaired","residual_error_type":"early_high_mfe_later_high_mae_false_recovery"}
{"row_type":"trigger","research_id":"R9L72_C14_EV_SLOWDOWN_RELIEF_RALLY_GUARD","round":"R9","loop":72,"large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C14_EV_DEMAND_SLOWDOWN_4B_4C","fine_archetype_id":"BATTERY_MATERIAL_EQUIPMENT_RELIEF_RALLY_HIGH_MAE_GUARD","symbol":"222080","name":"씨아이에스","trigger_type":"Stage2-Actionable-Guarded","trigger_family":"battery_equipment_order_relief_rally_before_capex_slowdown","trigger_date":"2024-03-04","entry_date":"2024-03-05","entry_price":10820.0,"entry_price_type":"next_tradable_open","price_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","mfe_30d_pct":39.65,"mae_30d_pct":0.00,"mfe_90d_pct":39.65,"mae_90d_pct":-4.53,"mfe_180d_pct":39.65,"mae_180d_pct":-27.91,"peak_price_180d":15110.0,"peak_date_180d":"2024-03-11","trough_price_180d":7800.0,"trough_date_180d":"2024-08-05","calibration_usable":true,"case_polarity":"counterexample_delayed_high_mae","evidence_url_pending":true,"source_proxy_only":true,"non_price_evidence_strength":"medium_low_pending_url_repair","price_only_blowoff":false,"expected_stage_current_profile":"Stage2_Actionable_Guarded_or_4B_watch_until_order_capex_bridge_repaired","residual_error_type":"equipment_relief_rally_needs_order_capex_margin_confirmation_before_green"}
```

---

## 8. Score simulation and raw component breakdown

This is shadow-only and does not change production scoring.

| symbol | demand/order repair | margin/price repair | call-off/capex risk control | market mispricing | valuation rerating | balance/financing risk | information confidence | shadow total | intended route |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| `278280` | 3 | 4 | 2 | 5 | 4 | 5 | 4 | 27 | blocked positive stage / 4B-4C watch |
| `095500` | 5 | 5 | 3 | 14 | 13 | 4 | 5 | 49 | local 4B watch; no Green |
| `222080` | 8 | 7 | 5 | 11 | 9 | 5 | 6 | 51 | Stage2-Guarded only after order/capex bridge repair |

### Current calibrated profile stress test

The current calibrated profile already blocks price-only blowoff.  
The remaining C14 problem is more dangerous: **a relief rally can look fundamentally plausible even when the EV-demand bridge is still broken.**

```text
C14 false-recovery mode:
  battery material/equipment name
  + large MFE in 30D
  + source_proxy_only evidence
  + no repaired customer/order/capex/margin bridge
  + 180D MAE worse than -25%
  => block Green; route to 4B/4C watch

C14 clean recovery mode:
  verified orderbook stabilization
  + customer call-off risk reduced
  + utilization/margin bridge repaired
  + contained 90D/180D MAE
  => only then consider Stage2/Yellow recovery
```

This file does not contain a clean recovery case.  
That is intentional because C14 is mainly a drawdown-thesis-break archetype. The “positive” result is the guardrail itself: `278280` shows the profile should block a weak relief rally before it becomes a false Stage2.

---

## 9. Aggregate metrics

```json
{
  "row_type": "aggregate",
  "research_id": "R9L72_C14_EV_SLOWDOWN_RELIEF_RALLY_GUARD",
  "round": "R9",
  "loop": 72,
  "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY",
  "canonical_archetype_id": "C14_EV_DEMAND_SLOWDOWN_4B_4C",
  "fine_archetype_id": "BATTERY_MATERIAL_EQUIPMENT_RELIEF_RALLY_HIGH_MAE_GUARD",
  "case_count": 3,
  "calibration_usable_case_count": 3,
  "guardrail_positive_case_count": 1,
  "counterexample_count": 2,
  "new_symbol_count": 3,
  "source_proxy_only_count": 3,
  "evidence_url_pending_count": 3,
  "avg_mfe_30d_pct": 43.35,
  "avg_mae_30d_pct": -1.94,
  "avg_mfe_90d_pct": 43.35,
  "avg_mae_90d_pct": -13.26,
  "avg_mfe_180d_pct": 43.35,
  "avg_mae_180d_pct": -32.44,
  "worst_mae_180d_pct": -35.00
}
```

---

## 10. Shadow rule candidate

```yaml
row_type: canonical_archetype_rule_candidate
canonical_archetype_id: C14_EV_DEMAND_SLOWDOWN_4B_4C
fine_archetype_id: BATTERY_MATERIAL_EQUIPMENT_RELIEF_RALLY_HIGH_MAE_GUARD
rule_name: C14_ev_slowdown_relief_rally_and_high_mae_router
production_scoring_changed: false
shadow_weight_only: true
```

### Proposed routing logic

```text
For C14 EV-demand slowdown / 4B-4C cases:

Tier A: verified recovery bridge
  Conditions:
    - customer call-off risk is reduced
    - order/capex schedule is repaired
    - margin/utilization evidence is URL-repaired
    - 90D/180D MAE remains contained
  Routing:
    - Stage2-Actionable recovery may be considered
    - Stage3-Yellow only after evidence repair
    - Green remains blocked until durable demand/margin repair is verified

Tier B: source-proxy-only relief rally
  Conditions:
    - MFE appears after heavy drawdown
    - non-price evidence remains source-proxy-only
    - EV-demand/capex bridge is not repaired
  Routing:
    - 4B-local-watch or Stage2-Guarded at most
    - no Green
    - no positive weight promotion

Tier C: high-MFE/high-MAE false recovery
  Conditions:
    - 30D MFE is large
    - 180D MAE <= -25%
    - customer/order/margin repair is not URL-repaired
  Routing:
    - count as false recovery counterexample
    - local 4B then 4C watch
    - block positive Stage2/Green promotion
```

### Suggested shadow delta

```json
{
  "row_type": "shadow_weight",
  "axis": "c14_ev_slowdown_relief_rally_and_high_mae_router",
  "scope": "canonical_archetype_id:C14_EV_DEMAND_SLOWDOWN_4B_4C",
  "proposal": {
    "source_proxy_only_green_allowed": false,
    "ev_demand_order_margin_bridge_required_for_recovery": true,
    "relief_rally_stage2_cap": "guarded_only",
    "high_mae_watch_threshold_pct": -25.0,
    "same_recovery_wave_high_mfe_high_mae_counts_as_false_recovery": true,
    "positive_weight_blocked_until_url_repair": true
  },
  "confidence": "medium_low_until_url_repair",
  "apply_now": false,
  "reason": "Three new C14 battery material/equipment adjacency cases show that relief rallies can produce large 30D MFE while later 180D MAE exceeds -25%. Because non-price evidence remains URL-pending, this is a guardrail candidate rather than a positive recovery candidate."
}
```

---

## 11. Residual contribution summary

```json
{
  "row_type": "residual_contribution",
  "research_id": "R9L72_C14_EV_SLOWDOWN_RELIEF_RALLY_GUARD",
  "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY",
  "canonical_archetype_id": "C14_EV_DEMAND_SLOWDOWN_4B_4C",
  "contribution": "Adds three less-repeated C14 battery material/equipment adjacency cases and shows that relief rallies can produce high MFE before later EV-demand/capex slowdown MAE dominates the path. C14 should treat these as guarded recovery or 4B/4C watch until order, demand, utilization, and margin repair evidence is URL-repaired.",
  "guardrail_positive_case_added": 1,
  "counterexample_case_added": 2,
  "new_symbol_count": 3,
  "data_quality_blocker": "All three non-price EV demand/capex/margin triggers require URL-level repair before positive recovery promotion.",
  "guardrail_added": "C14 Green is blocked when source_proxy_only=true and 180D MAE is worse than -25%, even if 30D MFE is large."
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
    278280: false
    095500: false
    222080: false
  evidence_url_pending:
    278280: true
    095500: true
    222080: true
  source_proxy_only:
    278280: true
    095500: true
    222080: true
```

Limitations:

```text
- Price path is validated against Stock-Web tradable OHLC rows.
- Non-price evidence is not URL-repaired in this run.
- Therefore this artifact is useful for C14 relief-rally/high-MAE guardrail design, but should not promote positive recovery weights until filings/IR/report data verifies customer demand, orderbook durability, capex timing, utilization, margin repair, and financing risk.
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
2. Preserve R9 / loop 72 metadata.
3. Add the cases to C14_EV_DEMAND_SLOWDOWN_4B_4C only if parser validation passes.
4. Treat all three non-price triggers as evidence_url_pending=true and source_proxy_only=true until URL-level evidence is repaired.
5. Do not use these rows for positive weight promotion until filings/IR/report data verifies EV demand, customer orderbook, capex timing, utilization, margin repair, and financing risk.
6. Add a shadow-only rule candidate named C14_ev_slowdown_relief_rally_and_high_mae_router.
7. Do not loosen Stage3-Green.
8. Add C14-specific guards:
   - source_proxy_only -> no Green
   - 180D MAE <= -25% without repaired demand/order/margin evidence -> local 4B/high-MAE watch or 4C watch
   - large 30D MFE does not override later EV slowdown MAE
   - Green requires repaired demand/order/margin bridge
9. Keep production scoring unchanged unless later batch promotion logic independently marks this axis safe.
```

---

## 14. Next round state

```text
completed_round = R9
completed_loop = 72
next_round = R10
next_loop = 72
next_large_sector_hint = L9_CONSTRUCTION_REALESTATE_HOUSING
```
