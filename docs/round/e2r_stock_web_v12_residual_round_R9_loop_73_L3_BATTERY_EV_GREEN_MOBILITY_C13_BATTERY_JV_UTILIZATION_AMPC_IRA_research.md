# E2R Stock-Web v12 Residual Research — R9 Loop 73

```yaml
research_session: post_calibrated_sector_archetype_residual_research
mode: historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12
completed_round: R9
completed_loop: 73
next_round: R10
next_loop: 73
large_sector_id: L3_BATTERY_EV_GREEN_MOBILITY
canonical_archetype_id: C13_BATTERY_JV_UTILIZATION_AMPC_IRA
fine_archetype_id: BATTERY_US_JV_AMPC_UTILIZATION_PARENT_SEPARATOR_COPPERFOIL_HIGH_MAE_ROUTER
output_file: e2r_stock_web_v12_residual_round_R9_loop_73_L3_BATTERY_EV_GREEN_MOBILITY_C13_BATTERY_JV_UTILIZATION_AMPC_IRA_research.md
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
completed_round = R8
completed_loop  = 73
large_sector_id = L8_PLATFORM_CONTENT_SW_SECURITY
canonical_archetype_id = C27_CONTENT_IP_GLOBAL_MONETIZATION
```

Therefore:

```text
scheduled_round = R9
scheduled_loop  = 73
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
canonical_archetype_id = C13_BATTERY_JV_UTILIZATION_AMPC_IRA
fine_archetype_id = BATTERY_US_JV_AMPC_UTILIZATION_PARENT_SEPARATOR_COPPERFOIL_HIGH_MAE_ROUTER
```

This is a valid R9 pairing.

---

## 1. Why this R9/C13 run

The no-repeat ledger shows C13 is less covered than C11/C12/C14 and concentrated in a few core cell/material names:

```text
C13_BATTERY_JV_UTILIZATION_AMPC_IRA:
  rows: 37
  symbols: 7
  date_range: 2022-05-25~2025-04-08
  good/bad S2: 8/9
  4B/4C: 7/2
  URL/proxy: 0/0
  top covered symbols: 373220(14), 006400(13), 096770(5), 003670(2), 005070(1), 020150(1)
```

This file deliberately avoids adding more rows to the top-covered cell names and tests adjacent / lower-repeat C13 cases:

```text
051910 LG화학
361610 SK아이이테크놀로지
020150 롯데에너지머티리얼즈
```

Research question:

```text
Can C13 distinguish real JV / AMPC / utilization repair from parent-company, separator, or copper-foil relief rallies that still fail because utilization, customer call-off, or margin conversion is not visible?
```

C13 is a bridge-quality archetype. It should not simply say “IRA/AMPC exposure exists.” The bridge must carry weight: U.S. JV production ramp, utilization, customer pull-through, tax-credit capture, margin conversion, and reduced call-off risk. Otherwise the market is standing on a painted bridge: the shape is there, but the load-bearing structure is not.

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
| `051910` | LG화학 | active_like / KOSPI | none listed | true |
| `361610` | SK아이이테크놀로지 | active_like / KOSPI | none listed | true |
| `020150` | 롯데에너지머티리얼즈 | active_like / KOSPI | none listed | true |

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
The Stock-Web price path is fully validated, but company-level U.S. JV ramp, AMPC capture, separator/copper-foil utilization, customer call-off, delivery schedule, margin conversion, and IRA-policy linkage still require later URL repair through filings, IR decks, JV disclosures, regulatory/tax-credit data, or sell-side reports before production weight promotion.
```

C13 interpretation used here:

```text
C13 is not simply “battery stock bounced.”
It asks whether a battery name has a concrete JV / utilization / AMPC bridge:
- U.S. plant or JV ramp quality,
- AMPC tax-credit capture visibility,
- customer demand and call-off control,
- separator/copper-foil utilization,
- margin conversion,
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
051910 + C13_BATTERY_JV_UTILIZATION_AMPC_IRA -> no direct match found
361610 + C13_BATTERY_JV_UTILIZATION_AMPC_IRA -> no direct match found
020150 + C13_BATTERY_JV_UTILIZATION_AMPC_IRA -> no direct match found
```

Novelty accounting:

```json
{
  "new_symbol_count": 2,
  "reused_low_frequency_symbol_count": 1,
  "minimum_new_symbol_count": 2,
  "positive_guarded_case_count": 1,
  "counterexample_count": 2,
  "new_independent_case_ratio": 1.00,
  "duplicate_status": "pass",
  "data_quality_status": "source_proxy_only_non_price_evidence"
}
```

`020150` appears once in the no-repeat ledger, but is not a high-repeat C13 symbol. It is included as a copper-foil utilization/call-off case because it is directly useful for this fine-archetype.

---

## 5. Case design

| case_id | symbol | trigger family | research role |
|---|---|---|---|
| `R9L73_C13_051910_20240202` | `051910` LG화학 | parent-company battery/JV/AMPC proxy rerating | positive-guarded early path, later high-MAE watch |
| `R9L73_C13_361610_20240627` | `361610` SK아이이테크놀로지 | separator utilization / customer call-off stress | low-MFE high-MAE counterexample |
| `R9L73_C13_020150_20240627` | `020150` 롯데에너지머티리얼즈 | copper-foil utilization / call-off relief failure | low-MFE extreme-MAE counterexample |

The intended residual:

```text
C13 should separate:
1. early battery/JV proxy rerating that may deserve Stage2-Guarded when MAE is initially contained;
2. separator/copper-foil utilization cases where weak MFE and large MAE show that the utilization bridge is still broken;
3. any source-proxy-only AMPC/JV narrative that lacks customer demand and margin conversion evidence.
```

---

## 6. Stock-Web OHLC and backtest

### 6.1 `051910` LG화학 — parent-company JV/AMPC proxy rerating, later high-MAE watch

Trigger:

```text
trigger_date = 2024-02-01
trigger_type = Stage2-Actionable-Guarded
trigger_family = parent_company_battery_jv_ampc_proxy_rerating
entry_date = 2024-02-02
entry_price = 451000.0
entry_price_type = next_tradable_open
```

Relevant Stock-Web rows:

```csv
d,o,h,l,c,v,a,mc,s,m
2024-02-01,426500.0,433000.0,417000.0,430000.0,312842.0,133027513500.0,30354707490000.0,70592343,KOSPI
2024-02-02,451000.0,468500.0,433000.0,461000.0,679677.0,309922167500.0,32543070123000.0,70592343,KOSPI
2024-02-16,489000.0,515000.0,488000.0,504000.0,587439.0,296430643000.0,35578540872000.0,70592343,KOSPI
2024-02-19,508000.0,520000.0,504000.0,508000.0,358152.0,183685798148.0,35860910244000.0,70592343,KOSPI
2024-04-19,374500.0,374500.0,366000.0,370500.0,348850.0,128602043000.0,26154463081500.0,70592343,KOSPI
2024-05-30,365000.0,368000.0,350000.0,350500.0,634361.0,225640556090.0,24742616221500.0,70592343,KOSPI
2024-07-19,332500.0,333500.0,326000.0,333500.0,303750.0,100240468500.0,23542546390500.0,70592343,KOSPI
2024-07-22,332500.0,339000.0,330000.0,333000.0,229970.0,76580677500.0,23507250219000.0,70592343,KOSPI
```

Backtest:

| window | peak/high | peak date | trough/low | trough date | MFE | MAE |
|---|---:|---|---:|---|---:|---:|
| 30 calendar days | 520000 | 2024-02-19 | 433000 | 2024-02-02 | +15.30% | -3.99% |
| 90 calendar days | 520000 | 2024-02-19 | 366000 | 2024-04-19 | +15.30% | -18.85% |
| 180 calendar days | 520000 | 2024-02-19 | 326000 | 2024-07-19 | +15.30% | -27.72% |

Interpretation:

```text
051910 is the positive-guarded holdout, not a Green case.
The first month showed a usable Stage2-like path: moderate MFE and contained MAE.
But the 180D drawdown crossed -25%, so any C13 positive route must require URL-repaired JV/AMPC/utilization/margin evidence before Yellow/Green.
```

### 6.2 `361610` SK아이이테크놀로지 — separator utilization / call-off stress

Trigger:

```text
trigger_date = 2024-06-26
trigger_type = Stage2-FalsePositive-Candidate
trigger_family = separator_utilization_calloff_stress_relief_rally
entry_date = 2024-06-27
entry_price = 44500.0
entry_price_type = next_tradable_open
```

Relevant Stock-Web rows:

```csv
d,o,h,l,c,v,a,mc,s,m
2024-06-26,43800.0,44750.0,43250.0,43900.0,164274.0,7231729750.0,3129964288800.0,71297592,KOSPI
2024-06-27,44500.0,44500.0,43300.0,43850.0,142241.0,6233686150.0,3126399409200.0,71297592,KOSPI
2024-07-02,45300.0,45450.0,43800.0,44100.0,173201.0,7663845600.0,3144223807200.0,71297592,KOSPI
2024-07-25,37300.0,38100.0,36550.0,37600.0,163688.0,6110042050.0,2680789459200.0,71297592,KOSPI
2024-08-05,36000.0,36200.0,30950.0,32000.0,341460.0,11406412450.0,2281522944000.0,71297592,KOSPI
2024-09-10,31750.0,32100.0,30050.0,30050.0,354268.0,10841296050.0,2142492639600.0,71297592,KOSPI
2024-11-15,25650.0,25750.0,24350.0,25150.0,424173.0,10594077550.0,1793134438800.0,71297592,KOSPI
2024-12-09,24050.0,24100.0,22650.0,22800.0,266446.0,6130032250.0,1625585097600.0,71297592,KOSPI
```

Backtest:

| window | peak/high | peak date | trough/low | trough date | MFE | MAE |
|---|---:|---|---:|---|---:|---:|
| 30 calendar days | 45450 | 2024-07-02 | 36550 | 2024-07-25 | +2.13% | -17.87% |
| 90 calendar days | 45450 | 2024-07-02 | 30050 | 2024-09-10 | +2.13% | -32.47% |
| 180 calendar days | 45450 | 2024-07-02 | 22650 | 2024-12-09 | +2.13% | -49.10% |

Interpretation:

```text
361610 is a clean C13 false-positive branch.
The entry had almost no MFE and quickly transitioned into high MAE.
This is exactly the kind of separator/utilization case where AMPC or IRA relevance cannot substitute for actual customer pull-through and utilization repair.
```

### 6.3 `020150` 롯데에너지머티리얼즈 — copper-foil utilization / call-off relief failure

Trigger:

```text
trigger_date = 2024-06-26
trigger_type = Stage2-FalsePositive-Candidate
trigger_family = copperfoil_utilization_customer_calloff_relief_failure
entry_date = 2024-06-27
entry_price = 53100.0
entry_price_type = next_tradable_open
```

Relevant Stock-Web rows:

```csv
d,o,h,l,c,v,a,mc,s,m
2024-06-26,53100.0,55100.0,53100.0,53300.0,315190.0,17005953500.0,2457707505500.0,46110835,KOSPI
2024-06-27,53100.0,54100.0,51700.0,52000.0,267020.0,14086406500.0,2397763420000.0,46110835,KOSPI
2024-07-03,54900.0,56100.0,52100.0,52900.0,344462.0,18519786300.0,2439263171500.0,46110835,KOSPI
2024-07-26,37450.0,37750.0,36300.0,36800.0,237532.0,8718396300.0,1696878728000.0,46110835,KOSPI
2024-08-05,36100.0,36750.0,30500.0,32200.0,468908.0,15821669100.0,1484768887000.0,46110835,KOSPI
2024-09-05,40050.0,45650.0,40050.0,43000.0,1121196.0,48476794250.0,1982765905000.0,46110835,KOSPI
2024-11-14,30300.0,30650.0,28100.0,28100.0,332305.0,9635744550.0,1295714463500.0,46110835,KOSPI
2024-12-09,22100.0,22400.0,20900.0,21000.0,212907.0,4555484550.0,968327535000.0,46110835,KOSPI
```

Backtest:

| window | peak/high | peak date | trough/low | trough date | MFE | MAE |
|---|---:|---|---:|---|---:|---:|
| 30 calendar days | 56100 | 2024-07-03 | 36300 | 2024-07-26 | +5.65% | -31.64% |
| 90 calendar days | 56100 | 2024-07-03 | 30500 | 2024-08-05 | +5.65% | -42.56% |
| 180 calendar days | 56100 | 2024-07-03 | 20900 | 2024-12-09 | +5.65% | -60.64% |

Interpretation:

```text
020150 is the hard C13 counterexample.
The copper-foil / utilization relief attempt created only small MFE and then extreme MAE.
This should be blocked from Stage2/Green unless hard customer, utilization, and margin repair evidence appears before the trigger.
```

---

## 7. Machine-readable trigger JSONL

```jsonl
{"row_type":"trigger","research_id":"R9L73_C13_BATTERY_JV_UTILIZATION_ROUTER","round":"R9","loop":73,"large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C13_BATTERY_JV_UTILIZATION_AMPC_IRA","fine_archetype_id":"BATTERY_US_JV_AMPC_UTILIZATION_PARENT_SEPARATOR_COPPERFOIL_HIGH_MAE_ROUTER","symbol":"051910","name":"LG화학","trigger_type":"Stage2-Actionable-Guarded","trigger_family":"parent_company_battery_jv_ampc_proxy_rerating","trigger_date":"2024-02-01","entry_date":"2024-02-02","entry_price":451000.0,"entry_price_type":"next_tradable_open","price_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","mfe_30d_pct":15.30,"mae_30d_pct":-3.99,"mfe_90d_pct":15.30,"mae_90d_pct":-18.85,"mfe_180d_pct":15.30,"mae_180d_pct":-27.72,"peak_price_180d":520000.0,"peak_date_180d":"2024-02-19","trough_price_180d":326000.0,"trough_date_180d":"2024-07-19","calibration_usable":true,"case_polarity":"positive_guarded_high_mae_later","evidence_url_pending":true,"source_proxy_only":true,"non_price_evidence_strength":"medium_pending_url_repair","price_only_blowoff":false,"expected_stage_current_profile":"Stage2-Guarded_to_Yellow_only_if_jv_ampc_utilization_margin_bridge_repaired","residual_error_type":"early_parent_proxy_rerating_but_180d_mae_requires_url_repaired_battery_bridge_before_green"}
{"row_type":"trigger","research_id":"R9L73_C13_BATTERY_JV_UTILIZATION_ROUTER","round":"R9","loop":73,"large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C13_BATTERY_JV_UTILIZATION_AMPC_IRA","fine_archetype_id":"BATTERY_US_JV_AMPC_UTILIZATION_PARENT_SEPARATOR_COPPERFOIL_HIGH_MAE_ROUTER","symbol":"361610","name":"SK아이이테크놀로지","trigger_type":"Stage2-FalsePositive-Candidate","trigger_family":"separator_utilization_calloff_stress_relief_rally","trigger_date":"2024-06-26","entry_date":"2024-06-27","entry_price":44500.0,"entry_price_type":"next_tradable_open","price_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","mfe_30d_pct":2.13,"mae_30d_pct":-17.87,"mfe_90d_pct":2.13,"mae_90d_pct":-32.47,"mfe_180d_pct":2.13,"mae_180d_pct":-49.10,"peak_price_180d":45450.0,"peak_date_180d":"2024-07-02","trough_price_180d":22650.0,"trough_date_180d":"2024-12-09","calibration_usable":true,"case_polarity":"counterexample_low_mfe_high_mae","evidence_url_pending":true,"source_proxy_only":true,"non_price_evidence_strength":"low_pending_url_repair","price_only_blowoff":false,"expected_stage_current_profile":"blocked_Stage2_or_4B_4C_high_MAE_watch","residual_error_type":"separator_utilization_relevance_without_customer_pullthrough_low_mfe_extreme_mae"}
{"row_type":"trigger","research_id":"R9L73_C13_BATTERY_JV_UTILIZATION_ROUTER","round":"R9","loop":73,"large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C13_BATTERY_JV_UTILIZATION_AMPC_IRA","fine_archetype_id":"BATTERY_US_JV_AMPC_UTILIZATION_PARENT_SEPARATOR_COPPERFOIL_HIGH_MAE_ROUTER","symbol":"020150","name":"롯데에너지머티리얼즈","trigger_type":"Stage2-FalsePositive-Candidate","trigger_family":"copperfoil_utilization_customer_calloff_relief_failure","trigger_date":"2024-06-26","entry_date":"2024-06-27","entry_price":53100.0,"entry_price_type":"next_tradable_open","price_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","mfe_30d_pct":5.65,"mae_30d_pct":-31.64,"mfe_90d_pct":5.65,"mae_90d_pct":-42.56,"mfe_180d_pct":5.65,"mae_180d_pct":-60.64,"peak_price_180d":56100.0,"peak_date_180d":"2024-07-03","trough_price_180d":20900.0,"trough_date_180d":"2024-12-09","calibration_usable":true,"case_polarity":"counterexample_extreme_mae","evidence_url_pending":true,"source_proxy_only":true,"non_price_evidence_strength":"low_pending_url_repair","price_only_blowoff":false,"expected_stage_current_profile":"blocked_Stage2_or_4C_high_MAE_watch_until_utilization_customer_margin_bridge_repaired","residual_error_type":"copperfoil_utilization_relief_entry_low_mfe_extreme_mae"}
```

---

## 8. Score simulation and raw component breakdown

This is shadow-only and does not change production scoring.

| symbol | JV / AMPC relevance | utilization bridge | customer / call-off control | market mispricing | valuation rerating | margin conversion | information confidence | shadow total | intended route |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| `051910` | 13 | 8 | 8 | 9 | 8 | 7 | 6 | 59 | Stage2-Guarded / Yellow only after bridge repair |
| `361610` | 7 | 3 | 2 | 4 | 3 | 2 | 5 | 26 | blocked Stage2 / 4B-4C high-MAE watch |
| `020150` | 7 | 3 | 2 | 5 | 4 | 2 | 4 | 27 | blocked Stage2 / 4C high-MAE watch |

### Current calibrated profile stress test

The current calibrated profile already blocks pure price-only blowoff.  
The remaining C13 risk is **policy/JV exposure without utilization conversion**:

```text
C13 guarded positive path:
  JV / AMPC / IRA relevance is plausible
  + early MAE is contained
  + source evidence is later URL-repaired
  + utilization and margin bridge are visible
  => Stage2-Actionable-Guarded / Yellow only after repair

C13 separator/copper-foil false-positive path:
  battery supply-chain relevance exists
  + MFE is weak or short-lived
  + 90D MAE <= -30% or 180D MAE <= -45%
  + no repaired customer/utilization/margin bridge
  => block Stage2 or route to 4B/4C high-MAE watch
```

`051910` prevents overblocking because the first-month path was acceptable.  
`361610` and `020150` show why source-proxy IRA/JV/utilization narratives must be capped when actual demand and margin conversion are not visible.

---

## 9. Aggregate metrics

```json
{
  "row_type": "aggregate",
  "research_id": "R9L73_C13_BATTERY_JV_UTILIZATION_ROUTER",
  "round": "R9",
  "loop": 73,
  "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY",
  "canonical_archetype_id": "C13_BATTERY_JV_UTILIZATION_AMPC_IRA",
  "fine_archetype_id": "BATTERY_US_JV_AMPC_UTILIZATION_PARENT_SEPARATOR_COPPERFOIL_HIGH_MAE_ROUTER",
  "case_count": 3,
  "calibration_usable_case_count": 3,
  "positive_guarded_case_count": 1,
  "counterexample_count": 2,
  "new_symbol_count": 2,
  "low_frequency_symbol_count": 1,
  "source_proxy_only_count": 3,
  "evidence_url_pending_count": 3,
  "avg_mfe_30d_pct": 7.69,
  "avg_mae_30d_pct": -17.83,
  "avg_mfe_90d_pct": 7.69,
  "avg_mae_90d_pct": -31.29,
  "avg_mfe_180d_pct": 7.69,
  "avg_mae_180d_pct": -45.82,
  "max_mfe_180d_pct": 15.30,
  "worst_mae_180d_pct": -60.64
}
```

---

## 10. 4B proximity split

```json
{
  "row_type": "4b_split",
  "research_id": "R9L73_C13_BATTERY_JV_UTILIZATION_ROUTER",
  "stage2_guarded_or_yellow_candidate": [
    {
      "symbol": "051910",
      "reason": "30D MFE was +15.30% with MAE only -3.99%, but 180D MAE reached -27.72%; Yellow/Green requires URL-repaired JV/AMPC/utilization/margin bridge"
    }
  ],
  "blocked_stage2_or_4b_4c_watch": [
    {
      "symbol": "361610",
      "reason": "MFE was only +2.13%, while 90D MAE reached -32.47% and 180D MAE reached -49.10%"
    },
    {
      "symbol": "020150",
      "reason": "MFE was only +5.65%, while 30D MAE already reached -31.64% and 180D MAE reached -60.64%"
    }
  ],
  "full_4b_or_green_requires_non_price_evidence": [
    "U.S. JV production ramp or AMPC capture",
    "customer demand / call-off reduction",
    "separator or copper-foil utilization repair",
    "delivery schedule and order durability",
    "gross margin / operating margin conversion"
  ]
}
```

---

## 11. Shadow rule candidate

```yaml
row_type: canonical_archetype_rule_candidate
canonical_archetype_id: C13_BATTERY_JV_UTILIZATION_AMPC_IRA
fine_archetype_id: BATTERY_US_JV_AMPC_UTILIZATION_PARENT_SEPARATOR_COPPERFOIL_HIGH_MAE_ROUTER
rule_name: C13_battery_jv_ampc_utilization_and_high_mae_router
production_scoring_changed: false
shadow_weight_only: true
```

### Proposed routing logic

```text
For C13 battery JV / utilization / AMPC / IRA cases:

Tier A: verified JV / AMPC / utilization repair
  Conditions:
    - U.S. JV ramp or AMPC capture is URL-repaired
    - customer call-off risk is reduced
    - utilization and margin conversion are visible
    - 30D/90D MAE is contained
  Routing:
    - Stage2-Actionable-Guarded allowed
    - Stage3-Yellow allowed after evidence repair
    - Green only after utilization and margin bridge are verified

Tier B: source-proxy-only parent/JV exposure
  Conditions:
    - parent or supply-chain name has plausible JV/IRA/AMPC exposure
    - evidence_url_pending or source_proxy_only remains true
    - 180D MAE <= -25%
  Routing:
    - Stage2-Guarded at most
    - no Green
    - no production positive weight promotion

Tier C: separator/copper-foil utilization false recovery
  Conditions:
    - MFE_30D < +10%
    - MAE_30D <= -20% or MAE_90D <= -30%
    - utilization/customer/margin bridge is missing
  Routing:
    - block Stage2
    - local 4B/high-MAE watch or 4C watch
    - count as counterexample
```

### Suggested shadow delta

```json
{
  "row_type": "shadow_weight",
  "axis": "c13_battery_jv_ampc_utilization_and_high_mae_router",
  "scope": "canonical_archetype_id:C13_BATTERY_JV_UTILIZATION_AMPC_IRA",
  "proposal": {
    "source_proxy_only_green_allowed": false,
    "jv_ampc_utilization_margin_bridge_required_for_green": true,
    "parent_proxy_stage2_cap": "guarded_only_until_url_repair",
    "parent_proxy_high_mae_watch_threshold_180d_pct": -25.0,
    "weak_mfe_threshold_30d_pct": 10.0,
    "separator_copperfoil_high_mae_threshold_30d_pct": -20.0,
    "utilization_failure_high_mae_threshold_90d_pct": -30.0,
    "positive_weight_blocked_until_url_repair": true
  },
  "confidence": "medium_low_until_url_repair",
  "apply_now": false,
  "reason": "One parent-company positive-guarded case and two separator/copper-foil high-MAE counterexamples show that C13 should require verified JV/AMPC/utilization/customer/margin evidence before Yellow/Green."
}
```

---

## 12. Residual contribution summary

```json
{
  "row_type": "residual_contribution",
  "research_id": "R9L73_C13_BATTERY_JV_UTILIZATION_ROUTER",
  "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY",
  "canonical_archetype_id": "C13_BATTERY_JV_UTILIZATION_AMPC_IRA",
  "contribution": "Adds C13 parent/JV proxy, separator, and copper-foil utilization cases outside the dominant cell-name cluster. The run separates a first-month acceptable parent proxy rerating from separator/copper-foil false recoveries with weak MFE and severe MAE. C13 Green should require URL-repaired JV ramp, AMPC capture, utilization, customer call-off reduction, and margin conversion evidence.",
  "positive_guarded_case_added": 1,
  "counterexample_case_added": 2,
  "new_symbol_count": 2,
  "low_frequency_symbol_added": 1,
  "data_quality_blocker": "All three non-price JV/utilization/AMPC triggers require URL-level repair before positive weight promotion.",
  "guardrail_added": "C13 source_proxy_only cases with weak MFE and 30D/90D high MAE should block Stage2 or route to 4B/4C high-MAE watch; parent-proxy cases with 180D MAE worse than -25% should not Green."
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
    051910: false
    361610: false
    020150: false
  evidence_url_pending:
    051910: true
    361610: true
    020150: true
  source_proxy_only:
    051910: true
    361610: true
    020150: true
```

Limitations:

```text
- Price path is validated against Stock-Web tradable OHLC rows.
- Non-price evidence is not URL-repaired in this run.
- Therefore this artifact is useful for C13 JV/utilization/AMPC residual shape and high-MAE guardrail design, but should not promote positive weights until filings/IR/JV-disclosure/regulatory/report data verifies U.S. JV ramp, AMPC capture, utilization, customer call-off, and margin conversion.
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
2. Preserve R9 / loop 73 metadata.
3. Add the cases to C13_BATTERY_JV_UTILIZATION_AMPC_IRA only if parser validation passes.
4. Treat all three non-price triggers as evidence_url_pending=true and source_proxy_only=true until URL-level evidence is repaired.
5. Do not use these rows for positive weight promotion until filings/IR/JV-disclosure/regulatory/report data verifies U.S. JV ramp, AMPC capture, utilization, customer call-off reduction, and margin conversion.
6. Add a shadow-only rule candidate named C13_battery_jv_ampc_utilization_and_high_mae_router.
7. Do not loosen Stage3-Green.
8. Add C13-specific guards:
   - source_proxy_only -> no Green
   - parent-proxy cases with 180D MAE <= -25% -> Stage2-Guarded at most
   - separator/copper-foil cases with MFE_30D < +10% and MAE_30D <= -20% -> block Stage2
   - MAE_90D <= -30% without utilization bridge -> 4B/4C high-MAE watch
   - Green requires repaired JV/AMPC/utilization/customer/margin bridge
9. Keep production scoring unchanged unless later batch promotion logic independently marks this axis safe.
```

---

## 15. Next round state

```text
completed_round = R9
completed_loop = 73
next_round = R10
next_loop = 73
next_large_sector_hint = L9_CONSTRUCTION_REALESTATE_HOUSING
```
