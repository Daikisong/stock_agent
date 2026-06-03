# E2R Stock-Web v12 Residual Research — R9 Loop 74

```yaml
research_session: post_calibrated_sector_archetype_residual_research
mode: historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12
completed_round: R9
completed_loop: 74
next_round: R10
next_loop: 74
large_sector_id: L3_BATTERY_EV_GREEN_MOBILITY
canonical_archetype_id: C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE
fine_archetype_id: AUTO_PARTS_VOLUME_MARGIN_LOW_MAE_AND_WEAK_MFE_HIGH_MAE_ROUTER
output_file: e2r_stock_web_v12_residual_round_R9_loop_74_L3_BATTERY_EV_GREEN_MOBILITY_C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE_research.md
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
completed_loop  = 74
large_sector_id = L8_PLATFORM_CONTENT_SW_SECURITY
canonical_archetype_id = C28_SOFTWARE_SECURITY_CONTRACT_RETENTION
```

Therefore:

```text
scheduled_round = R9
scheduled_loop  = 74
```

R9 permits:

```text
large_sector_id = L3_BATTERY_EV_GREEN_MOBILITY
or
large_sector_id = L9_CONSTRUCTION_REALESTATE_HOUSING
```

This run selects the L3 mobility branch:

```text
large_sector_id = L3_BATTERY_EV_GREEN_MOBILITY
canonical_archetype_id = C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE
fine_archetype_id = AUTO_PARTS_VOLUME_MARGIN_LOW_MAE_AND_WEAK_MFE_HIGH_MAE_ROUTER
```

This is a valid R9 pairing.

---

## 1. Why this R9/C29 run

The no-repeat ledger shows C29 is large and noisy, with many auto/mobility volume-margin cases already present:

```text
C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE:
  rows: 157
  symbols: 33
  date_range: 2020-08-14~2024-09-09
  good/bad S2: 51/40
  4B/4C: 30/10
  URL/proxy: 4/0
  top covered symbols: UNKNOWN_SYMBOL(20), 000270(19), 005380(12), 204320(10), 018880(8), 161390(8)
```

This file deliberately avoids those top-covered names and tests lower-repeat auto-parts / EV-body supplier paths:

```text
064960 SNT모티브
033530 세종공업/SJG세종
009900 명신산업
```

Research question:

```text
Can C29 separate stable auto-parts volume/margin rerating from supplier relief entries where auto-cycle relevance exists but MFE remains weak and later MAE exposes margin or customer-volume risk?
```

C29 is an operating-leverage archetype. Vehicle volume is the wind, but supplier margin is the sail. If customer mix, FX, pass-through, utilization, and fixed-cost leverage do not catch that wind, a supplier can look policy/cycle-linked while still leaking downside.

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
| `064960` | SNT모티브 | active_like / KOSPI | no 2024 overlap; latest future candidates 2025-01-24 and 2025-02-26 are outside window | true |
| `033530` | 세종공업/SJG세종 | active_like / KOSPI | no 2024 overlap; latest listed candidate 1999-11-29 | true |
| `009900` | 명신산업 | active_like / KOSPI | no 2024 overlap; latest listed candidate 2021-06-18 | true |

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
The Stock-Web price path is fully validated, but company-level customer volume, model mix, EV/ICE mix, pass-through, fixed-cost leverage, FX, order visibility, and margin conversion evidence still require later URL repair through filings, IR decks, customer data, or sell-side reports before production weight promotion.
```

C29 interpretation used here:

```text
C29 is not simply “auto part stock bounced.”
It asks whether mobility volume turns into operating leverage:
- customer production volume,
- model / EV / export mix,
- price pass-through and FX,
- utilization and fixed-cost absorption,
- operating margin bridge,
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
064960 + C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE -> no direct match found
033530 + C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE -> no direct match found
009900 + C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE -> no direct match found
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
| `R9L74_C29_064960_20240202` | `064960` SNT모티브 | auto motor parts volume/margin low-MAE rerating | positive-guarded low-MAE holdout |
| `R9L74_C29_033530_20240202` | `033530` 세종공업/SJG세종 | auto exhaust parts volume/margin relief with later drawdown | moderate-MFE later-drawdown watch |
| `R9L74_C29_009900_20240213` | `009900` 명신산업 | EV body-parts supplier relief with weak MFE and high MAE | hard weak-MFE / high-MAE counterexample |

The intended residual:

```text
C29 should separate:
1. low-MAE auto-parts paths that may stay Stage2-Guarded;
2. supplier relief paths where MFE is only moderate and later drawdown needs bridge repair;
3. EV/body supplier entries where the cycle label is plausible but MFE is weak and 180D MAE is severe.
```

---

## 6. Stock-Web OHLC and backtest

### 6.1 `064960` SNT모티브 — auto motor-parts low-MAE rerating

Trigger:

```text
trigger_date = 2024-02-01
trigger_type = Stage2-Actionable-Guarded
trigger_family = auto_motor_parts_volume_margin_low_mae_valueup_rerating
entry_date = 2024-02-02
entry_price = 44600.0
entry_price_type = next_tradable_open_after_auto_parts_valueup_burst
```

Relevant Stock-Web rows:

```csv
d,o,h,l,c,v,a,mc,s,m
2024-02-01,44400.0,45950.0,44000.0,44600.0,67205.0,3022485450.0,652191865600.0,14623136,KOSPI
2024-02-02,44600.0,46400.0,44000.0,45700.0,110242.0,4986202100.0,668277315200.0,14623136,KOSPI
2024-02-05,46350.0,47050.0,44950.0,45800.0,53049.0,2428178300.0,669739628800.0,14623136,KOSPI
2024-02-14,43000.0,44350.0,42850.0,43900.0,32645.0,1434618200.0,641955670400.0,14623136,KOSPI
2024-03-28,45300.0,45400.0,42400.0,44950.0,40688.0,1826104400.0,657309963200.0,14623136,KOSPI
2024-06-28,49950.0,50300.0,49350.0,49850.0,24152.0,1207455150.0,728963329600.0,14623136,KOSPI
2024-07-31,43300.0,43400.0,42850.0,43050.0,16953.0,730834250.0,629526004800.0,14623136,KOSPI
```

Backtest:

| window | peak/high | peak date | trough/low | trough date | MFE | MAE |
|---|---:|---|---:|---|---:|---:|
| 30 calendar days | 47050 | 2024-02-05 | 42850 | 2024-02-14 | +5.49% | -3.92% |
| 90 calendar days | 47050 | 2024-02-05 | 42400 | 2024-03-28 | +5.49% | -4.93% |
| 180 calendar days | 50300 | 2024-06-28 | 42400 | 2024-03-28 | +12.78% | -4.93% |

Interpretation:

```text
064960 is the low-MAE C29 holdout.
The return profile is not explosive, but the drawdown stayed contained and later MFE improved.
This is useful because some C29 mobility cases should be judged by stable operating leverage rather than blowoff strength. It can remain Stage2-Guarded / Yellow candidate after evidence repair.
```

### 6.2 `033530` 세종공업/SJG세종 — auto supplier relief with later drawdown

Trigger:

```text
trigger_date = 2024-02-01
trigger_type = Stage2-Actionable-Guarded
trigger_family = auto_exhaust_parts_volume_margin_relief_later_drawdown
entry_date = 2024-02-02
entry_price = 5940.0
entry_price_type = next_tradable_open_after_auto_supplier_relief
```

Relevant Stock-Web rows:

```csv
d,o,h,l,c,v,a,mc,s,m
2024-02-01,5530.0,5880.0,5530.0,5860.0,390712.0,2258371370.0,163030831460.0,27820961,KOSPI
2024-02-02,5940.0,6370.0,5880.0,6320.0,1383389.0,8590641770.0,175828473520.0,27820961,KOSPI
2024-02-14,6050.0,6640.0,6050.0,6380.0,1955047.0,12619255970.0,177497731180.0,27820961,KOSPI
2024-03-06,6240.0,6840.0,5970.0,5970.0,3387084.0,21795715550.0,166091137170.0,27820961,KOSPI
2024-03-12,5720.0,5780.0,5650.0,5700.0,100214.0,571752260.0,158579477700.0,27820961,KOSPI
2024-04-11,5740.0,5810.0,5650.0,5760.0,41401.0,236527120.0,160248735360.0,27820961,KOSPI
2024-07-25,4970.0,5030.0,4905.0,4970.0,49687.0,246446755.0,138270176170.0,27820961,KOSPI
2024-07-31,5100.0,5140.0,5050.0,5120.0,18721.0,95510670.0,142443320320.0,27820961,KOSPI
```

Backtest:

| window | peak/high | peak date | trough/low | trough date | MFE | MAE |
|---|---:|---|---:|---|---:|---:|
| 30 calendar days | 6640 | 2024-02-14 | 5840 | 2024-02-21 | +11.78% | -1.68% |
| 90 calendar days | 6840 | 2024-03-06 | 5650 | 2024-03-12 | +15.15% | -4.88% |
| 180 calendar days | 6840 | 2024-03-06 | 4905 | 2024-07-25 | +15.15% | -17.42% |

Interpretation:

```text
033530 is the middle branch.
The first windows were acceptable, but the 180D path drifted into a material drawdown.
This should remain Stage2-Guarded or local 4B watch until customer volume, model mix, pass-through, and operating-margin evidence are repaired.
```

### 6.3 `009900` 명신산업 — EV body-parts supplier relief with weak MFE and high MAE

Trigger:

```text
trigger_date = 2024-02-08
trigger_type = Stage2-FalsePositive-Candidate
trigger_family = ev_body_parts_volume_margin_relief_weak_mfe_high_mae
entry_date = 2024-02-13
entry_price = 17130.0
entry_price_type = next_tradable_open_after_ev_body_supplier_relief
```

Relevant Stock-Web rows:

```csv
d,o,h,l,c,v,a,mc,s,m
2024-02-08,17200.0,17250.0,17010.0,17010.0,162320.0,2774821270.0,892516962330.0,52470133,KOSPI
2024-02-13,17130.0,17410.0,17100.0,17260.0,169448.0,2926141270.0,905634495580.0,52470133,KOSPI
2024-02-15,17670.0,17670.0,17120.0,17150.0,200243.0,3450752490.0,899862780950.0,52470133,KOSPI
2024-03-07,15500.0,15540.0,15120.0,15160.0,268475.0,4086782040.0,795447216280.0,52470133,KOSPI
2024-04-08,14600.0,14700.0,14190.0,14200.0,273442.0,3917472110.0,745075888600.0,52470133,KOSPI
2024-07-03,14900.0,15400.0,14630.0,14690.0,852361.0,12840844390.0,770786253770.0,52470133,KOSPI
2024-08-05,12600.0,12640.0,10500.0,10770.0,505436.0,5809986540.0,565103332410.0,52470133,KOSPI
```

Backtest:

| window | peak/high | peak date | trough/low | trough date | MFE | MAE |
|---|---:|---|---:|---|---:|---:|
| 30 calendar days | 17670 | 2024-02-15 | 15120 | 2024-03-07 | +3.15% | -11.73% |
| 90 calendar days | 17670 | 2024-02-15 | 14190 | 2024-04-08 | +3.15% | -17.16% |
| 180 calendar days | 17670 | 2024-02-15 | 10500 | 2024-08-05 | +3.15% | -38.70% |

Interpretation:

```text
009900 is the hard C29 counterexample.
The mobility/EV-body supplier label existed, but the post-entry return geometry failed: MFE stayed near +3%, while 180D MAE reached -38.70%.
This should block Stage2/Green unless fresh customer volume and margin evidence appears before entry.
```

---

## 7. Machine-readable trigger JSONL

```jsonl
{"row_type":"trigger","research_id":"R9L74_C29_AUTO_PARTS_VOLUME_MARGIN_ROUTER","round":"R9","loop":74,"large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE","fine_archetype_id":"AUTO_PARTS_VOLUME_MARGIN_LOW_MAE_AND_WEAK_MFE_HIGH_MAE_ROUTER","symbol":"064960","name":"SNT모티브","trigger_type":"Stage2-Actionable-Guarded","trigger_family":"auto_motor_parts_volume_margin_low_mae_valueup_rerating","trigger_date":"2024-02-01","entry_date":"2024-02-02","entry_price":44600.0,"entry_price_type":"next_tradable_open_after_auto_parts_valueup_burst","price_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","mfe_30d_pct":5.49,"mae_30d_pct":-3.92,"mfe_90d_pct":5.49,"mae_90d_pct":-4.93,"mfe_180d_pct":12.78,"mae_180d_pct":-4.93,"peak_price_180d":50300.0,"peak_date_180d":"2024-06-28","trough_price_180d":42400.0,"trough_date_180d":"2024-03-28","calibration_usable":true,"case_polarity":"positive_guarded_low_mae","evidence_url_pending":true,"source_proxy_only":true,"non_price_evidence_strength":"medium_low_pending_url_repair","price_only_blowoff":false,"expected_stage_current_profile":"Stage2-Guarded_to_Yellow_if_volume_margin_capital_return_bridge_repaired","residual_error_type":"low_mae_auto_parts_volume_margin_path_requires_url_repaired_customer_volume_margin_bridge_before_green"}
{"row_type":"trigger","research_id":"R9L74_C29_AUTO_PARTS_VOLUME_MARGIN_ROUTER","round":"R9","loop":74,"large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE","fine_archetype_id":"AUTO_PARTS_VOLUME_MARGIN_LOW_MAE_AND_WEAK_MFE_HIGH_MAE_ROUTER","symbol":"033530","name":"세종공업/SJG세종","trigger_type":"Stage2-Actionable-Guarded","trigger_family":"auto_exhaust_parts_volume_margin_relief_later_drawdown","trigger_date":"2024-02-01","entry_date":"2024-02-02","entry_price":5940.0,"entry_price_type":"next_tradable_open_after_auto_supplier_relief","price_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","mfe_30d_pct":11.78,"mae_30d_pct":-1.68,"mfe_90d_pct":15.15,"mae_90d_pct":-4.88,"mfe_180d_pct":15.15,"mae_180d_pct":-17.42,"peak_price_180d":6840.0,"peak_date_180d":"2024-03-06","trough_price_180d":4905.0,"trough_date_180d":"2024-07-25","calibration_usable":true,"case_polarity":"counterexample_moderate_mfe_later_drawdown_watch","evidence_url_pending":true,"source_proxy_only":true,"non_price_evidence_strength":"medium_low_pending_url_repair","price_only_blowoff":false,"expected_stage_current_profile":"Stage2-Guarded_or_local_4B_watch_until_auto_supplier_margin_bridge_repaired","residual_error_type":"auto_supplier_relief_mfe_was_moderate_but_later_drawdown_needs_customer_margin_bridge"}
{"row_type":"trigger","research_id":"R9L74_C29_AUTO_PARTS_VOLUME_MARGIN_ROUTER","round":"R9","loop":74,"large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE","fine_archetype_id":"AUTO_PARTS_VOLUME_MARGIN_LOW_MAE_AND_WEAK_MFE_HIGH_MAE_ROUTER","symbol":"009900","name":"명신산업","trigger_type":"Stage2-FalsePositive-Candidate","trigger_family":"ev_body_parts_volume_margin_relief_weak_mfe_high_mae","trigger_date":"2024-02-08","entry_date":"2024-02-13","entry_price":17130.0,"entry_price_type":"next_tradable_open_after_ev_body_supplier_relief","price_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","mfe_30d_pct":3.15,"mae_30d_pct":-11.73,"mfe_90d_pct":3.15,"mae_90d_pct":-17.16,"mfe_180d_pct":3.15,"mae_180d_pct":-38.7,"peak_price_180d":17670.0,"peak_date_180d":"2024-02-15","trough_price_180d":10500.0,"trough_date_180d":"2024-08-05","calibration_usable":true,"case_polarity":"counterexample_weak_mfe_high_mae","evidence_url_pending":true,"source_proxy_only":true,"non_price_evidence_strength":"low_pending_url_repair","price_only_blowoff":false,"expected_stage_current_profile":"blocked_Stage2_or_4B_4C_high_MAE_watch","residual_error_type":"ev_body_supplier_relief_had_weak_mfe_and_high_mae_without_volume_margin_bridge"}
```

---

## 8. Score simulation and raw component breakdown

This is shadow-only and does not change production scoring.

| symbol | customer volume bridge | model / EV mix | pass-through / FX | operating leverage | market mispricing | margin conversion | information confidence | shadow total | intended route |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| `064960` | 8 | 7 | 8 | 8 | 6 | 8 | 6 | 51 | Stage2-Guarded / Yellow after volume-margin evidence repair |
| `033530` | 7 | 6 | 5 | 6 | 7 | 4 | 5 | 40 | Stage2-Guarded or local 4B watch |
| `009900` | 3 | 4 | 2 | 2 | 3 | 2 | 4 | 20 | blocked Stage2 / 4B-4C high-MAE watch |

### Current calibrated profile stress test

The current calibrated profile already blocks pure price-only blowoff.  
The remaining C29 issue is **mobility label without operating-leverage conversion**:

```text
C29 low-MAE supplier path:
  auto/mobility supplier relevance
  + MAE remains contained
  + later MFE improves
  + URL-repaired customer-volume and margin bridge
  => Stage2-Guarded / Yellow candidate

C29 moderate-MFE drawdown path:
  supplier relief creates acceptable first-window MFE
  + 180D MAE approaches -20%
  + evidence remains source_proxy_only
  => Stage2-Guarded at most, local 4B watch

C29 weak-MFE high-MAE path:
  EV/auto supplier label exists
  + MFE_30D < +5%
  + MAE_180D <= -35%
  + no customer-volume / margin bridge
  => block Stage2 or route to 4B/4C high-MAE watch
```

`064960` prevents overblocking.  
`033530` shows why moderate supplier rerating should stay guarded.  
`009900` shows why a mobility label alone cannot rescue a weak-MFE, high-MAE path.

---

## 9. Aggregate metrics

```json
{
  "row_type": "aggregate",
  "research_id": "R9L74_C29_AUTO_PARTS_VOLUME_MARGIN_ROUTER",
  "round": "R9",
  "loop": 74,
  "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY",
  "canonical_archetype_id": "C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE",
  "fine_archetype_id": "AUTO_PARTS_VOLUME_MARGIN_LOW_MAE_AND_WEAK_MFE_HIGH_MAE_ROUTER",
  "case_count": 3,
  "calibration_usable_case_count": 3,
  "positive_guarded_case_count": 1,
  "counterexample_count": 2,
  "new_symbol_count": 3,
  "source_proxy_only_count": 3,
  "evidence_url_pending_count": 3,
  "avg_mfe_30d_pct": 6.81,
  "avg_mae_30d_pct": -5.78,
  "avg_mfe_90d_pct": 7.93,
  "avg_mae_90d_pct": -8.99,
  "avg_mfe_180d_pct": 10.36,
  "avg_mae_180d_pct": -20.35,
  "max_mfe_180d_pct": 15.15,
  "worst_mae_180d_pct": -38.7
}
```

---

## 10. 4B proximity split

```json
{
  "row_type": "4b_split",
  "research_id": "R9L74_C29_AUTO_PARTS_VOLUME_MARGIN_ROUTER",
  "stage2_guarded_or_yellow_candidate": [
    {
      "symbol": "064960",
      "reason": "low-MAE path with improving 180D MFE; requires customer volume and operating-margin evidence before Yellow/Green"
    }
  ],
  "local_4b_watch": [
    {
      "symbol": "033530",
      "reason": "first windows were acceptable, but 180D MAE reached -17.42%; needs pass-through and margin bridge repair"
    }
  ],
  "blocked_stage2_or_4c_watch": [
    {
      "symbol": "009900",
      "reason": "MFE stayed only +3.15%, while 180D MAE reached -38.70%; weak-MFE high-MAE supplier relief"
    }
  ],
  "full_4b_or_green_requires_non_price_evidence": [
    "customer production volume",
    "model / EV / export mix",
    "price pass-through and FX",
    "utilization and fixed-cost absorption",
    "operating margin and cash-flow conversion"
  ]
}
```

---

## 11. Shadow rule candidate

```yaml
row_type: canonical_archetype_rule_candidate
canonical_archetype_id: C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE
fine_archetype_id: AUTO_PARTS_VOLUME_MARGIN_LOW_MAE_AND_WEAK_MFE_HIGH_MAE_ROUTER
rule_name: C29_auto_parts_volume_margin_low_mae_and_weak_mfe_high_mae_router
production_scoring_changed: false
shadow_weight_only: true
```

### Proposed routing logic

```text
For C29 mobility / auto-parts volume-margin cases:

Tier A: verified low-MAE operating-leverage path
  Conditions:
    - customer volume, model mix, pass-through, and margin evidence are URL-repaired
    - 30D/90D MAE remains contained
    - MFE improves beyond one event candle
  Routing:
    - Stage2-Actionable-Guarded allowed
    - Stage3-Yellow allowed after evidence repair
    - Green only after customer volume and margin bridge are verified

Tier B: moderate-MFE supplier relief with later drawdown
  Conditions:
    - MFE_90D >= +10%
    - MAE_180D <= -15%
    - bridge evidence remains source_proxy_only
  Routing:
    - Stage2-Guarded at most
    - local 4B watch
    - no Green

Tier C: weak-MFE high-MAE supplier relief
  Conditions:
    - MFE_30D < +5%
    - MAE_180D <= -35%
    - no customer-volume or margin bridge
  Routing:
    - block Stage2
    - route to 4B/4C high-MAE watch
    - count as counterexample
```

### Suggested shadow delta

```json
{
  "row_type": "shadow_weight",
  "axis": "c29_auto_parts_volume_margin_low_mae_and_weak_mfe_high_mae_router",
  "scope": "canonical_archetype_id:C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE",
  "proposal": {
    "source_proxy_only_green_allowed": false,
    "customer_volume_operating_margin_bridge_required_for_green": true,
    "low_mae_supplier_stage2_guarded_allowed": true,
    "moderate_mfe_threshold_90d_pct": 10.0,
    "later_drawdown_watch_threshold_180d_pct": -15.0,
    "weak_mfe_threshold_30d_pct": 5.0,
    "weak_mfe_hard_mae_threshold_180d_pct": -35.0,
    "positive_weight_blocked_until_url_repair": true
  },
  "confidence": "medium_low_until_url_repair",
  "apply_now": false,
  "reason": "One low-MAE auto-parts holdout, one moderate-MFE later-drawdown supplier, and one weak-MFE high-MAE EV/body supplier case show that C29 should require URL-repaired customer-volume and operating-margin evidence before Yellow/Green."
}
```

---

## 12. Residual contribution summary

```json
{
  "row_type": "residual_contribution",
  "research_id": "R9L74_C29_AUTO_PARTS_VOLUME_MARGIN_ROUTER",
  "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY",
  "canonical_archetype_id": "C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE",
  "contribution": "Adds three non-top-covered C29 auto-parts / EV-body supplier cases and separates a low-MAE operating-leverage holdout from moderate-MFE later-drawdown and weak-MFE high-MAE counterexamples. C29 Green should require URL-repaired customer production volume, model/EV/export mix, pass-through, utilization, operating-margin, and cash-flow evidence.",
  "positive_guarded_case_added": 1,
  "counterexample_case_added": 2,
  "new_symbol_count": 3,
  "data_quality_blocker": "All three non-price mobility volume/margin triggers require URL-level repair before positive weight promotion.",
  "guardrail_added": "C29 source_proxy_only supplier cases with MFE_30D < +5% and MAE_180D <= -35% should block Stage2 or route to 4B/4C high-MAE watch; moderate-MFE cases with MAE_180D <= -15% should cap at Stage2-Guarded until evidence repair."
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
    064960: false
    033530: false
    009900: false
  evidence_url_pending:
    064960: true
    033530: true
    009900: true
  source_proxy_only:
    064960: true
    033530: true
    009900: true
```

Limitations:

```text
- Price path is validated against Stock-Web tradable OHLC rows.
- Non-price evidence is not URL-repaired in this run.
- Therefore this artifact is useful for C29 mobility/auto-parts volume-margin residual shape and high-MAE guardrail design, but should not promote positive weights until filings, IR, customer data, or reports verify customer production volume, model mix, pass-through, utilization, operating margin, and cash-flow conversion.
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
2. Preserve R9 / loop 74 metadata.
3. Add the cases to C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE only if parser validation passes.
4. Treat all three non-price triggers as evidence_url_pending=true and source_proxy_only=true until URL-level evidence is repaired.
5. Do not use these rows for positive weight promotion until filings/IR/customer/report data verifies customer production volume, model mix, EV/export mix, pass-through, utilization, operating margin, and cash-flow conversion.
6. Add a shadow-only rule candidate named C29_auto_parts_volume_margin_low_mae_and_weak_mfe_high_mae_router.
7. Do not loosen Stage3-Green.
8. Add C29-specific guards:
   - source_proxy_only -> no Green
   - Green requires repaired customer-volume / operating-margin bridge
   - low-MAE supplier paths may remain Stage2-Guarded until evidence repair
   - MFE_90D >= +10% and MAE_180D <= -15% without bridge repair -> Stage2-Guarded at most / local 4B watch
   - MFE_30D < +5% and MAE_180D <= -35% -> block Stage2 or route to 4B/4C high-MAE watch
9. Keep production scoring unchanged unless later batch promotion logic independently marks this axis safe.
```

---

## 15. Next round state

```text
completed_round = R9
completed_loop = 74
next_round = R10
next_loop = 74
next_large_sector_hint = L9_CONSTRUCTION_REALESTATE_HOUSING
round_schedule_status = valid
round_sector_consistency = pass
```
