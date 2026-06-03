# E2R Stock-Web v12 Residual Research — R4 Loop 74

```yaml
research_session: post_calibrated_sector_archetype_residual_research
mode: historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12
completed_round: R4
completed_loop: 74
next_round: R5
next_loop: 74
large_sector_id: L4_MATERIALS_SPREAD_RESOURCE
canonical_archetype_id: C15_MATERIAL_SPREAD_SUPERCYCLE
fine_archetype_id: COPPER_NONFERROUS_SPREAD_PASS_THROUGH_AND_THEME_HIGH_MAE_ROUTER
output_file: e2r_stock_web_v12_residual_round_R4_loop_74_L4_MATERIALS_SPREAD_RESOURCE_C15_MATERIAL_SPREAD_SUPERCYCLE_research.md
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
completed_round = R3
completed_loop  = 74
large_sector_id = L3_BATTERY_EV_GREEN_MOBILITY
canonical_archetype_id = C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK
```

Therefore:

```text
scheduled_round = R4
scheduled_loop  = 74
```

R4 maps to:

```text
large_sector_id = L4_MATERIALS_SPREAD_RESOURCE
```

This run selects:

```text
canonical_archetype_id = C15_MATERIAL_SPREAD_SUPERCYCLE
fine_archetype_id = COPPER_NONFERROUS_SPREAD_PASS_THROUGH_AND_THEME_HIGH_MAE_ROUTER
```

This is a valid R4/L4 pairing.

---

## 1. Why this R4/C15 run

The no-repeat ledger shows C15 is moderately covered, with concentration in steel / major material-spread names:

```text
C15_MATERIAL_SPREAD_SUPERCYCLE:
  rows: 56
  symbols: 23
  date_range: 2020-08-10~2024-09-13
  good/bad S2: 20/3
  4B/4C: 15/0
  URL/proxy: 0/0
  top covered symbols: 005490(9), 004020(7), 001430(4), 018470(4), 001230(3), 011170(3)
```

This file avoids those top-covered names and adds three copper / brass / nonferrous processing names:

```text
025820 이구산업
012800 대창
021050 서원
```

Research question:

```text
Can C15 separate true nonferrous spread pass-through from copper/brass theme rallies where commodity price beta exists but inventory, cost pass-through, and margin conversion are not URL-repaired?
```

C15 is a spread archetype. The commodity price is the weather; company margin is the crop. A copper price storm can make every field look alive, but Stage2/Yellow should ask whether the company actually harvests better spread, inventory gains, and cash margin rather than simply moving with the futures tape.

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
| `025820` | 이구산업 | active_like / KOSPI | no 2024 overlap; old 1996/2007 candidates only | true |
| `012800` | 대창 | active_like / KOSPI | no 2024 overlap; old 1998/2008 candidates only | true |
| `021050` | 서원 | active_like / KOSPI | no 2024 overlap; latest listed candidate 2016-06-21 | true |

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
The Stock-Web price path is fully validated, but company-level copper/brass spread, inventory gains/losses, pass-through lag, volume, customer mix, and gross-margin bridge evidence still require later URL repair through filings, IR decks, commodity data, customs/export data, or sell-side reports before production weight promotion.
```

C15 interpretation used here:

```text
C15 is not simply “commodity-linked stock rose.”
It asks whether material spread becomes company margin:
- raw-material price / product price spread,
- inventory valuation and pass-through lag,
- volume and customer mix,
- operating leverage,
- working-capital burden,
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
025820 + C15_MATERIAL_SPREAD_SUPERCYCLE -> no direct match found
012800 + C15_MATERIAL_SPREAD_SUPERCYCLE -> no direct match found
021050 + C15_MATERIAL_SPREAD_SUPERCYCLE -> no direct match found
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
| `R4L74_C15_025820_20240315` | `025820` 이구산업 | copper rolling spread pass-through rerating | positive-guarded / low-MAE anchor |
| `R4L74_C15_012800_20240315` | `012800` 대창 | brass/copper spread theme high-MFE later drawdown | high-MFE / delayed-MAE counterexample |
| `R4L74_C15_021050_20240215` | `021050` 서원 | brass/copper theme spike without margin bridge | high-MAE counterexample |

The intended residual:

```text
C15 should separate:
1. nonferrous spread cases where MFE persists and MAE remains relatively controlled;
2. copper/brass theme rallies where high MFE arrives but the later path proves drawdown risk;
3. low-price commodity beta spikes where margin pass-through is not proven and MAE crosses the 4B/high-MAE guardrail.
```

---

## 6. Stock-Web OHLC and backtest

### 6.1 `025820` 이구산업 — copper rolling spread pass-through rerating

Trigger:

```text
trigger_date = 2024-03-14
trigger_type = Stage2-Actionable-Guarded
trigger_family = copper_rolling_spread_pass_through_rerating_low_initial_mae
entry_date = 2024-03-15
entry_price = 4265.0
entry_price_type = next_tradable_open_after_copper_spread_burst
```

Relevant Stock-Web rows:

```csv
d,o,h,l,c,v,a,mc,s,m
2024-03-14,4400.0,4825.0,4185.0,4220.0,25017428.0,115472800550.0,141125240000.0,33442000,KOSPI
2024-03-15,4265.0,4760.0,4165.0,4545.0,15961509.0,72578851935.0,151993890000.0,33442000,KOSPI
2024-04-12,5690.0,6090.0,5460.0,5700.0,15223035.0,89166441390.0,190619400000.0,33442000,KOSPI
2024-04-19,6640.0,7310.0,6410.0,6790.0,47804175.0,332468400980.0,227071180000.0,33442000,KOSPI
2024-05-20,7700.0,8420.0,7400.0,7880.0,47603058.0,381542856790.0,263522960000.0,33442000,KOSPI
2024-06-05,5620.0,5680.0,5450.0,5510.0,1483416.0,8231931900.0,184265420000.0,33442000,KOSPI
2024-08-05,4365.0,4430.0,3795.0,3930.0,805374.0,3285423220.0,131427060000.0,33442000,KOSPI
2024-09-06,4080.0,4100.0,3975.0,3990.0,143785.0,577027540.0,133433580000.0,33442000,KOSPI
```

Backtest:

| window | peak/high | peak date | trough/low | trough date | MFE | MAE |
|---|---:|---|---:|---|---:|---:|
| 30 calendar days | 6090 | 2024-04-12 | 4165 | 2024-03-15 | +42.79% | -2.34% |
| 90 calendar days | 8420 | 2024-05-20 | 4165 | 2024-03-15 | +97.42% | -2.34% |
| 180 calendar days | 8420 | 2024-05-20 | 3795 | 2024-08-05 | +97.42% | -11.02% |

Interpretation:

```text
025820 is the C15 positive-guarded anchor.
The path generated strong MFE with relatively controlled MAE, which is the shape C15 should keep open.
It still should not become Green without URL-repaired evidence that copper price beta actually converted into inventory gain, spread, and margin.
```

### 6.2 `012800` 대창 — brass/copper spread theme with delayed drawdown

Trigger:

```text
trigger_date = 2024-03-14
trigger_type = Stage2-Actionable-Guarded
trigger_family = brass_copper_spread_theme_high_mfe_later_drawdown
entry_date = 2024-03-15
entry_price = 1399.0
entry_price_type = next_tradable_open_after_nonferrous_theme_burst
```

Relevant Stock-Web rows:

```csv
d,o,h,l,c,v,a,mc,s,m
2024-03-14,1433.0,1544.0,1388.0,1400.0,12005543.0,17470586152.0,127596698600.0,91140499,KOSPI
2024-03-15,1399.0,1483.0,1365.0,1469.0,7117854.0,10275464332.0,133885393031.0,91140499,KOSPI
2024-04-12,1470.0,1575.0,1450.0,1543.0,9904736.0,15110419383.0,140629789957.0,91140499,KOSPI
2024-05-16,1621.0,1785.0,1610.0,1678.0,19312953.0,33041334611.0,152933757322.0,91140499,KOSPI
2024-05-21,2185.0,2320.0,2080.0,2175.0,69505626.0,152388771765.0,198230585325.0,91140499,KOSPI
2024-06-05,1527.0,1529.0,1470.0,1478.0,2377342.0,3535804427.0,134705657522.0,91140499,KOSPI
2024-08-05,1277.0,1283.0,1100.0,1161.0,1724372.0,2078029050.0,105814119339.0,91140499,KOSPI
2024-09-11,1201.0,1218.0,1195.0,1197.0,175040.0,210983248.0,109095177303.0,91140499,KOSPI
```

Backtest:

| window | peak/high | peak date | trough/low | trough date | MFE | MAE |
|---|---:|---|---:|---|---:|---:|
| 30 calendar days | 1575 | 2024-04-12 | 1322 | 2024-03-28 | +12.58% | -5.50% |
| 90 calendar days | 2320 | 2024-05-21 | 1322 | 2024-03-28 | +65.83% | -5.50% |
| 180 calendar days | 2320 | 2024-05-21 | 1100 | 2024-08-05 | +65.83% | -21.37% |

Interpretation:

```text
012800 is a high-MFE / delayed-MAE C15 warning.
The copper/brass theme produced a large MFE window, but the later drawdown crossed a material guardrail.
This is not a hard false positive, but it should cap at Stage2-Guarded until spread pass-through, inventory, and margin evidence are URL-repaired.
```

### 6.3 `021050` 서원 — brass/copper theme spike without margin bridge

Trigger:

```text
trigger_date = 2024-02-14
trigger_type = Stage2-FalsePositive-Candidate
trigger_family = brass_copper_theme_spike_high_mae_without_margin_bridge
entry_date = 2024-02-15
entry_price = 1482.0
entry_price_type = next_tradable_open_after_brass_copper_spike
```

Relevant Stock-Web rows:

```csv
d,o,h,l,c,v,a,mc,s,m
2024-02-14,1330.0,1481.0,1310.0,1452.0,5786533.0,8201524360.0,68933104680.0,47474590,KOSPI
2024-02-15,1482.0,1790.0,1460.0,1690.0,28567663.0,47901572826.0,80232057100.0,47474590,KOSPI
2024-03-05,1320.0,1320.0,1235.0,1281.0,724258.0,928056205.0,60814949790.0,47474590,KOSPI
2024-04-15,1328.0,1410.0,1326.0,1359.0,3352222.0,4586724353.0,64517967810.0,47474590,KOSPI
2024-05-20,1674.0,1999.0,1630.0,1916.0,33435296.0,62636646061.0,90961314440.0,47474590,KOSPI
2024-05-21,2000.0,2005.0,1700.0,1815.0,8640685.0,16204835453.0,86166380850.0,47474590,KOSPI
2024-08-05,1229.0,1229.0,1074.0,1090.0,907251.0,1046554301.0,51747303100.0,47474590,KOSPI
2024-09-11,1216.0,1225.0,1197.0,1205.0,112235.0,135086685.0,57206880950.0,47474590,KOSPI
```

Backtest:

| window | peak/high | peak date | trough/low | trough date | MFE | MAE |
|---|---:|---|---:|---|---:|---:|
| 30 calendar days | 1790 | 2024-02-15 | 1235 | 2024-03-05 | +20.78% | -16.67% |
| 90 calendar days | 1790 | 2024-02-15 | 1235 | 2024-03-05 | +20.78% | -16.67% |
| 180 calendar days | 2005 | 2024-05-21 | 1074 | 2024-08-05 | +35.29% | -27.53% |

Interpretation:

```text
021050 is the hard C15 counterexample in this file.
The entry had immediate theme MFE but also deep early MAE, and the later full-window MAE exceeded -25%.
This should not be Stage2/Green without company-specific spread, inventory, and margin bridge evidence.
```

---

## 7. Machine-readable trigger JSONL

```jsonl
{"row_type":"trigger","research_id":"R4L74_C15_COPPER_SPREAD_ROUTER","round":"R4","loop":74,"large_sector_id":"L4_MATERIALS_SPREAD_RESOURCE","canonical_archetype_id":"C15_MATERIAL_SPREAD_SUPERCYCLE","fine_archetype_id":"COPPER_NONFERROUS_SPREAD_PASS_THROUGH_AND_THEME_HIGH_MAE_ROUTER","symbol":"025820","name":"이구산업","trigger_type":"Stage2-Actionable-Guarded","trigger_family":"copper_rolling_spread_pass_through_rerating_low_initial_mae","trigger_date":"2024-03-14","entry_date":"2024-03-15","entry_price":4265.0,"entry_price_type":"next_tradable_open_after_copper_spread_burst","price_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","mfe_30d_pct":42.79,"mae_30d_pct":-2.34,"mfe_90d_pct":97.42,"mae_90d_pct":-2.34,"mfe_180d_pct":97.42,"mae_180d_pct":-11.02,"peak_price_180d":8420.0,"peak_date_180d":"2024-05-20","trough_price_180d":3795.0,"trough_date_180d":"2024-08-05","calibration_usable":true,"case_polarity":"positive_guarded_low_mae","evidence_url_pending":true,"source_proxy_only":true,"non_price_evidence_strength":"medium_pending_url_repair","price_only_blowoff":false,"expected_stage_current_profile":"Stage2-Guarded_to_Yellow_if_copper_spread_inventory_margin_bridge_repaired","residual_error_type":"positive_copper_spread_path_requires_url_repaired_pass_through_inventory_margin_bridge_before_green"}
{"row_type":"trigger","research_id":"R4L74_C15_COPPER_SPREAD_ROUTER","round":"R4","loop":74,"large_sector_id":"L4_MATERIALS_SPREAD_RESOURCE","canonical_archetype_id":"C15_MATERIAL_SPREAD_SUPERCYCLE","fine_archetype_id":"COPPER_NONFERROUS_SPREAD_PASS_THROUGH_AND_THEME_HIGH_MAE_ROUTER","symbol":"012800","name":"대창","trigger_type":"Stage2-Actionable-Guarded","trigger_family":"brass_copper_spread_theme_high_mfe_later_drawdown","trigger_date":"2024-03-14","entry_date":"2024-03-15","entry_price":1399.0,"entry_price_type":"next_tradable_open_after_nonferrous_theme_burst","price_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","mfe_30d_pct":12.58,"mae_30d_pct":-5.5,"mfe_90d_pct":65.83,"mae_90d_pct":-5.5,"mfe_180d_pct":65.83,"mae_180d_pct":-21.37,"peak_price_180d":2320.0,"peak_date_180d":"2024-05-21","trough_price_180d":1100.0,"trough_date_180d":"2024-08-05","calibration_usable":true,"case_polarity":"counterexample_high_mfe_delayed_mae","evidence_url_pending":true,"source_proxy_only":true,"non_price_evidence_strength":"low_pending_url_repair","price_only_blowoff":false,"expected_stage_current_profile":"Stage2-Guarded_or_4B_watch_until_spread_margin_bridge_repaired","residual_error_type":"nonferrous_theme_had_high_mfe_but_later_drawdown_requires_spread_margin_bridge_before_green"}
{"row_type":"trigger","research_id":"R4L74_C15_COPPER_SPREAD_ROUTER","round":"R4","loop":74,"large_sector_id":"L4_MATERIALS_SPREAD_RESOURCE","canonical_archetype_id":"C15_MATERIAL_SPREAD_SUPERCYCLE","fine_archetype_id":"COPPER_NONFERROUS_SPREAD_PASS_THROUGH_AND_THEME_HIGH_MAE_ROUTER","symbol":"021050","name":"서원","trigger_type":"Stage2-FalsePositive-Candidate","trigger_family":"brass_copper_theme_spike_high_mae_without_margin_bridge","trigger_date":"2024-02-14","entry_date":"2024-02-15","entry_price":1482.0,"entry_price_type":"next_tradable_open_after_brass_copper_spike","price_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","mfe_30d_pct":20.78,"mae_30d_pct":-16.67,"mfe_90d_pct":20.78,"mae_90d_pct":-16.67,"mfe_180d_pct":35.29,"mae_180d_pct":-27.53,"peak_price_180d":2005.0,"peak_date_180d":"2024-05-21","trough_price_180d":1074.0,"trough_date_180d":"2024-08-05","calibration_usable":true,"case_polarity":"counterexample_high_mae","evidence_url_pending":true,"source_proxy_only":true,"non_price_evidence_strength":"low_pending_url_repair","price_only_blowoff":false,"expected_stage_current_profile":"blocked_Stage2_or_4B_high_MAE_watch_until_margin_pass_through_repaired","residual_error_type":"copper_brass_theme_entry_had_mae_over_25pct_without_company_margin_bridge"}
```

---

## 8. Score simulation and raw component breakdown

This is shadow-only and does not change production scoring.

| symbol | commodity/spread relevance | pass-through bridge | inventory / working capital | market mispricing | valuation rerating | margin conversion | information confidence | shadow total | intended route |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| `025820` | 13 | 10 | 9 | 13 | 12 | 9 | 6 | 72 | Stage2-Guarded / Yellow after spread-margin evidence repair |
| `012800` | 11 | 6 | 5 | 12 | 10 | 4 | 5 | 53 | Stage2-Guarded or local 4B watch |
| `021050` | 9 | 4 | 3 | 8 | 6 | 3 | 4 | 37 | blocked Stage2 or 4B/high-MAE watch |

### Current calibrated profile stress test

The current calibrated profile already blocks pure price-only blowoff.  
The remaining C15 issue is **commodity beta without company spread conversion**:

```text
C15 clean spread path:
  commodity/spread relevance
  + persistent MFE
  + controlled MAE
  + URL-repaired inventory / pass-through / margin bridge
  => Stage2-Actionable-Guarded / Yellow, possible Green after proof

C15 high-MFE delayed-MAE path:
  commodity beta creates large MFE
  + later MAE crosses -20%
  + evidence remains source_proxy_only
  => Stage2-Guarded at most, local 4B watch, no Green

C15 theme-spike high-MAE path:
  entry follows copper/brass spike
  + 30D MAE <= -15%
  + 180D MAE <= -25%
  + no margin bridge
  => block Stage2 or route to 4B/high-MAE watch
```

`025820` prevents overblocking.  
`012800` shows why high MFE needs a later drawdown guard.  
`021050` shows that copper/brass theme beta can fail the Stage2 capital-preservation test even when commodity relevance is real.

---

## 9. Aggregate metrics

```json
{
  "row_type": "aggregate",
  "research_id": "R4L74_C15_COPPER_SPREAD_ROUTER",
  "round": "R4",
  "loop": 74,
  "large_sector_id": "L4_MATERIALS_SPREAD_RESOURCE",
  "canonical_archetype_id": "C15_MATERIAL_SPREAD_SUPERCYCLE",
  "fine_archetype_id": "COPPER_NONFERROUS_SPREAD_PASS_THROUGH_AND_THEME_HIGH_MAE_ROUTER",
  "case_count": 3,
  "calibration_usable_case_count": 3,
  "positive_guarded_case_count": 1,
  "counterexample_count": 2,
  "new_symbol_count": 3,
  "source_proxy_only_count": 3,
  "evidence_url_pending_count": 3,
  "avg_mfe_30d_pct": 25.38,
  "avg_mae_30d_pct": -8.17,
  "avg_mfe_90d_pct": 61.34,
  "avg_mae_90d_pct": -8.17,
  "avg_mfe_180d_pct": 66.18,
  "avg_mae_180d_pct": -19.97,
  "max_mfe_180d_pct": 97.42,
  "worst_mae_180d_pct": -27.53
}
```

---

## 10. 4B proximity split

```json
{
  "row_type": "4b_split",
  "research_id": "R4L74_C15_COPPER_SPREAD_ROUTER",
  "stage2_guarded_or_yellow_candidate": [
    {
      "symbol": "025820",
      "reason": "strong 90D/180D MFE with 180D MAE only -11.02%; requires spread/pass-through/margin evidence before Green"
    }
  ],
  "local_4b_watch": [
    {
      "symbol": "012800",
      "reason": "large +65.83% MFE but 180D MAE reached -21.37%; high-MFE copper theme needs margin bridge repair"
    },
    {
      "symbol": "021050",
      "reason": "theme entry had -16.67% 30D MAE and -27.53% 180D MAE; should block positive stage without spread evidence"
    }
  ],
  "full_4b_or_green_requires_non_price_evidence": [
    "copper/brass product spread",
    "inventory gain/loss and working-capital burden",
    "price pass-through lag",
    "customer mix and volume",
    "gross margin / operating margin conversion"
  ]
}
```

---

## 11. Shadow rule candidate

```yaml
row_type: canonical_archetype_rule_candidate
canonical_archetype_id: C15_MATERIAL_SPREAD_SUPERCYCLE
fine_archetype_id: COPPER_NONFERROUS_SPREAD_PASS_THROUGH_AND_THEME_HIGH_MAE_ROUTER
rule_name: C15_copper_nonferrous_spread_pass_through_and_high_mae_router
production_scoring_changed: false
shadow_weight_only: true
```

### Proposed routing logic

```text
For C15 copper / nonferrous material-spread cases:

Tier A: verified spread pass-through winner
  Conditions:
    - commodity/spread relevance is clear
    - inventory / pass-through / margin evidence is URL-repaired
    - 30D/90D MAE remains contained
    - MFE persists beyond one theme candle
  Routing:
    - Stage2-Actionable-Guarded allowed
    - Stage3-Yellow allowed after evidence repair
    - Green only after spread and margin conversion are verified

Tier B: high-MFE delayed drawdown
  Conditions:
    - MFE_90D >= +40%
    - MAE_180D <= -20%
    - bridge evidence remains source_proxy_only
  Routing:
    - Stage2-Guarded at most
    - local 4B watch
    - no Green

Tier C: commodity theme spike without company margin bridge
  Conditions:
    - MAE_30D <= -15%
    - MAE_180D <= -25%
    - no repaired margin/pass-through evidence
  Routing:
    - block Stage2
    - local 4B/high-MAE watch
    - count as false-positive counterexample
```

### Suggested shadow delta

```json
{
  "row_type": "shadow_weight",
  "axis": "c15_copper_nonferrous_spread_pass_through_and_high_mae_router",
  "scope": "canonical_archetype_id:C15_MATERIAL_SPREAD_SUPERCYCLE",
  "proposal": {
    "source_proxy_only_green_allowed": false,
    "spread_inventory_margin_bridge_required_for_green": true,
    "high_mfe_delayed_mae_stage2_cap": "guarded_only_until_url_repair",
    "high_mfe_threshold_90d_pct": 40.0,
    "delayed_mae_watch_threshold_180d_pct": -20.0,
    "theme_spike_high_mae_threshold_30d_pct": -15.0,
    "theme_spike_hard_mae_threshold_180d_pct": -25.0,
    "positive_weight_blocked_until_url_repair": true
  },
  "confidence": "medium_low_until_url_repair",
  "apply_now": false,
  "reason": "One strong low-MAE copper rolling case and two copper/brass theme high-MAE cases show that C15 should require URL-repaired spread, inventory, pass-through, and margin evidence before Yellow/Green."
}
```

---

## 12. Residual contribution summary

```json
{
  "row_type": "residual_contribution",
  "research_id": "R4L74_C15_COPPER_SPREAD_ROUTER",
  "large_sector_id": "L4_MATERIALS_SPREAD_RESOURCE",
  "canonical_archetype_id": "C15_MATERIAL_SPREAD_SUPERCYCLE",
  "contribution": "Adds three non-top-covered C15 copper/brass/nonferrous processing cases and separates a strong low-MAE copper rolling spread path from high-MFE delayed-MAE and hard high-MAE copper theme counterexamples. C15 Green should require URL-repaired commodity spread, inventory, pass-through, working-capital, and margin conversion evidence.",
  "positive_guarded_case_added": 1,
  "counterexample_case_added": 2,
  "new_symbol_count": 3,
  "data_quality_blocker": "All three non-price copper/nonferrous spread triggers require URL-level repair before positive weight promotion.",
  "guardrail_added": "C15 source_proxy_only copper/brass theme cases with MAE_180D <= -20% should cap at Stage2-Guarded or local 4B; MAE_30D <= -15% plus MAE_180D <= -25% should block Stage2 without margin bridge repair."
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
    025820: false
    012800: false
    021050: false
  evidence_url_pending:
    025820: true
    012800: true
    021050: true
  source_proxy_only:
    025820: true
    012800: true
    021050: true
```

Limitations:

```text
- Price path is validated against Stock-Web tradable OHLC rows.
- Non-price evidence is not URL-repaired in this run.
- Therefore this artifact is useful for C15 copper/nonferrous material-spread residual shape and high-MAE guardrail design, but should not promote positive weights until filings/IR/commodity/customs/report data verifies spread, inventory, pass-through, volume, working-capital, and margin conversion.
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
2. Preserve R4 / loop 74 metadata.
3. Add the cases to C15_MATERIAL_SPREAD_SUPERCYCLE only if parser validation passes.
4. Treat all three non-price triggers as evidence_url_pending=true and source_proxy_only=true until URL-level evidence is repaired.
5. Do not use these rows for positive weight promotion until filings/IR/commodity/customs/report data verifies copper/brass spread, inventory, pass-through, customer volume, working capital, and margin conversion.
6. Add a shadow-only rule candidate named C15_copper_nonferrous_spread_pass_through_and_high_mae_router.
7. Do not loosen Stage3-Green.
8. Add C15-specific guards:
   - source_proxy_only -> no Green
   - Green requires repaired spread/inventory/pass-through/margin bridge
   - MFE_90D >= +40% and MAE_180D <= -20% without evidence repair -> Stage2-Guarded at most
   - MAE_30D <= -15% and MAE_180D <= -25% without company margin bridge -> block Stage2 or local 4B/high-MAE watch
9. Keep production scoring unchanged unless later batch promotion logic independently marks this axis safe.
```

---

## 15. Next round state

```text
completed_round = R4
completed_loop = 74
next_round = R5
next_loop = 74
next_large_sector_hint = L5_CONSUMER_BRAND_DISTRIBUTION
```
