# E2R Stock-Web v12 Residual Research — R4 Loop 75

```yaml
research_session: post_calibrated_sector_archetype_residual_research
mode: historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12
completed_round: R4
completed_loop: 75
next_round: R5
next_loop: 75
large_sector_id: L4_MATERIALS_SPREAD_RESOURCE
canonical_archetype_id: C16_STRATEGIC_RESOURCE_POLICY_SUPPLY
fine_archetype_id: RARE_EARTH_NICKEL_RESOURCE_POLICY_SUPPLY_AND_THEME_SPIKE_HIGH_MAE_ROUTER
output_file: e2r_stock_web_v12_residual_round_R4_loop_75_L4_MATERIALS_SPREAD_RESOURCE_C16_STRATEGIC_RESOURCE_POLICY_SUPPLY_research.md
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
completed_loop  = 75
large_sector_id = L3_BATTERY_EV_GREEN_MOBILITY
canonical_archetype_id = C11_BATTERY_ORDERBOOK_RERATING
```

Therefore:

```text
scheduled_round = R4
scheduled_loop  = 75
```

R4 maps to:

```text
large_sector_id = L4_MATERIALS_SPREAD_RESOURCE
```

This run selects:

```text
canonical_archetype_id = C16_STRATEGIC_RESOURCE_POLICY_SUPPLY
fine_archetype_id = RARE_EARTH_NICKEL_RESOURCE_POLICY_SUPPLY_AND_THEME_SPIKE_HIGH_MAE_ROUTER
```

This is a valid R4/L4 pairing.

---

## 1. Why this R4/C16 run

The no-repeat ledger shows C16 is moderately covered but still not as over-dense as the broad chemical spread or consumer/export archetypes:

```text
C16_STRATEGIC_RESOURCE_POLICY_SUPPLY:
  rows: 52
  symbols: 20
  date_range: 2019-05-20~2024-02-28
  good/bad S2: 14/5
  4B/4C: 17/0
  URL/proxy: 4/4
  top covered symbols: 001570(7), 005490(6), 000910(5), 005290(4), 075970(4), 009520(3)
```

This file avoids those top-covered symbols and adds three lower-repeat strategic-resource policy/supply candidates:

```text
081150 티플랙스
047400 유니온머티리얼
011810 STX
```

Research question:

```text
Can C16 separate a usable rare-metal supply-policy rerating from rare-earth/resource trading theme spikes where policy relevance exists but company-specific supply contract, inventory, volume, and margin conversion are not visible?
```

C16 should behave like a supply-chain customs gate. It should let through resource cases where policy pressure converts into supply, customers, volume, and margin. It should stop the cargo when the bill of lading is only a headline: critical-mineral language, no verified company bridge, then high MAE.

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
| `081150` | 티플랙스 | active_like / KOSDAQ | no 2024 overlap; old 2012 candidates only | true |
| `047400` | 유니온머티리얼 | active_like / KOSPI | no 2024 overlap; old 2011 candidate only | true |
| `011810` | STX | active_like / KOSPI | 2024-01-05 candidate is before selected 2024-02-16 entry | true for selected 30D/90D/180D window |

Profile caveat:

```text
Stock-Web OHLC is raw/unadjusted marcap data.
These cases are calibration-safe for the selected 2024 windows because no listed corporate-action candidate overlaps each entry~D+180 test window.
For 011810, the 2024-01-05 corporate-action candidate is before the selected entry and is not inside the tested forward window.
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
The Stock-Web price path is fully validated, but company-level rare-metal sourcing, rare-earth/permanent-magnet exposure, inventory position, customer contracts, trading volume, supply-security policy linkage, pass-through, and margin conversion evidence still require later URL repair through filings, IR decks, customs/export data, contract disclosures, or sell-side reports before production weight promotion.
```

C16 interpretation used here:

```text
C16 is not simply “strategic resource stock rose.”
It asks whether policy supply relevance becomes company economics:
- strategic resource / rare-earth / nickel exposure,
- supply contract or trading volume,
- inventory and working-capital control,
- customer quality,
- policy-linked procurement or reshoring demand,
- margin and cash conversion,
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
081150 + C16_STRATEGIC_RESOURCE_POLICY_SUPPLY -> no direct match found
047400 + C16_STRATEGIC_RESOURCE_POLICY_SUPPLY -> no direct match found
011810 + C16_STRATEGIC_RESOURCE_POLICY_SUPPLY -> no direct match found
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
| `R4L75_C16_081150_20240419` | `081150` 티플랙스 | rare-metal / nickel policy supply rerating | positive-guarded drawdown watch |
| `R4L75_C16_047400_20240422` | `047400` 유니온머티리얼 | rare-earth / permanent-magnet policy label weak-MFE path | weak-MFE high-MAE counterexample |
| `R4L75_C16_011810_20240216` | `011810` STX | strategic resource trading / lithium-nickel policy spike | extreme-MAE counterexample |

The intended residual:

```text
C16 should separate:
1. rare-metal supply paths with usable MFE and initially contained drawdown;
2. rare-earth/permanent-magnet policy labels where MFE remains weak and drawdown becomes hard;
3. resource-trading policy spikes where first-window MFE is overwhelmed by 90D/180D MAE.
```

---

## 6. Stock-Web OHLC and backtest

### 6.1 `081150` 티플랙스 — rare-metal / nickel supply-policy guarded case

Trigger:

```text
trigger_date = 2024-04-18
trigger_type = Stage2-Actionable-Guarded
trigger_family = rare_metal_nickel_policy_supply_low_mae_to_drawdown_watch
entry_date = 2024-04-19
entry_price = 2805.0
entry_price_type = next_tradable_open_after_rare_metal_policy_supply_burst
```

Relevant Stock-Web rows:

```csv
d,o,h,l,c,v,a,mc,s,m
2024-04-18,2735.0,2980.0,2735.0,2825.0,394323.0,1125322590.0,68558235650.0,24268402,KOSDAQ
2024-04-19,2805.0,3115.0,2805.0,2975.0,4380708.0,13138113210.0,72198495950.0,24268402,KOSDAQ
2024-05-20,3030.0,3370.0,2970.0,3180.0,8794348.0,28175249455.0,77173518360.0,24268402,KOSDAQ
2024-07-09,3080.0,3160.0,3040.0,3140.0,402475.0,1254736990.0,76202782280.0,24268402,KOSDAQ
2024-08-05,2660.0,2720.0,2310.0,2450.0,313241.0,799820165.0,59457584900.0,24268402,KOSDAQ
2024-10-10,2700.0,3290.0,2700.0,3180.0,11664995.0,36204097475.0,77173518360.0,24268402,KOSDAQ
2024-10-28,3100.0,3390.0,3045.0,3300.0,3616674.0,11713274100.0,80085726600.0,24268402,KOSDAQ
```

Backtest:

| window | peak/high | peak date | trough/low | trough date | MFE | MAE |
|---|---:|---|---:|---|---:|---:|
| 30 calendar days | 3115 | 2024-04-19 | 2805 | 2024-04-19 | +11.05% | +0.00% |
| 90 calendar days | 3370 | 2024-05-20 | 2805 | 2024-04-19 | +20.14% | +0.00% |
| 180 calendar days | 3370 | 2024-05-20 | 2310 | 2024-08-05 | +20.14% | -17.65% |

Interpretation:

```text
081150 is the guarded positive holdout.
The first 90 days did not break capital preservation, and MFE was usable. The 180D drawdown, however, argues against Green while evidence remains source-proxy-only.
C16 should keep this as Stage2-Guarded / Yellow-after-repair, not as automatic strategic-resource Green.
```

### 6.2 `047400` 유니온머티리얼 — rare-earth / permanent-magnet weak-MFE high-MAE path

Trigger:

```text
trigger_date = 2024-04-19
trigger_type = Stage2-FalsePositive-Candidate
trigger_family = rare_earth_permanent_magnet_policy_label_weak_mfe_high_mae
entry_date = 2024-04-22
entry_price = 2995.0
entry_price_type = next_tradable_open_after_rare_earth_theme_spike
```

Relevant Stock-Web rows:

```csv
d,o,h,l,c,v,a,mc,s,m
2024-04-18,2750.0,2820.0,2695.0,2785.0,1275433.0,3539359110.0,116970000000.0,42000000,KOSPI
2024-04-19,2880.0,3050.0,2800.0,3050.0,4258902.0,12450232950.0,128100000000.0,42000000,KOSPI
2024-04-22,2995.0,2995.0,2830.0,2875.0,1368853.0,3988346930.0,120750000000.0,42000000,KOSPI
2024-05-07,2780.0,2800.0,2655.0,2715.0,532281.0,1440204905.0,114030000000.0,42000000,KOSPI
2024-05-17,2910.0,3085.0,2840.0,2905.0,1777501.0,5261177260.0,122010000000.0,42000000,KOSPI
2024-06-28,2500.0,2540.0,2460.0,2495.0,211715.0,527321180.0,104790000000.0,42000000,KOSPI
2024-09-09,1984.0,2045.0,1940.0,2035.0,89303.0,177663626.0,85470000000.0,42000000,KOSPI
2024-10-16,2345.0,2600.0,2300.0,2360.0,3672058.0,9108094120.0,99120000000.0,42000000,KOSPI
```

Backtest:

| window | peak/high | peak date | trough/low | trough date | MFE | MAE |
|---|---:|---|---:|---|---:|---:|
| 30 calendar days | 3085 | 2024-05-17 | 2655 | 2024-05-07 | +3.01% | -11.35% |
| 90 calendar days | 3085 | 2024-05-17 | 2460 | 2024-06-28 | +3.01% | -17.86% |
| 180 calendar days | 3085 | 2024-05-17 | 1940 | 2024-09-09 | +3.01% | -35.23% |

Interpretation:

```text
047400 is the weak-MFE high-MAE C16 counterexample.
The rare-earth/permanent-magnet policy label was plausible, but post-entry MFE never expanded beyond +3.01%, while 180D MAE crossed -35%.
This should block Stage2 or route to local 4B/high-MAE watch until company-specific supply/customer/margin evidence is repaired.
```

### 6.3 `011810` STX — strategic resource trading spike with extreme MAE

Trigger:

```text
trigger_date = 2024-02-15
trigger_type = Stage2-FalsePositive-Candidate
trigger_family = strategic_resource_trading_lithium_nickel_policy_spike_high_mae
entry_date = 2024-02-16
entry_price = 10470.0
entry_price_type = next_tradable_open_after_resource_trading_policy_spike
```

Relevant Stock-Web rows:

```csv
d,o,h,l,c,v,a,mc,s,m
2024-02-15,10000.0,10460.0,9800.0,10410.0,1396453.0,14267716890.0,322896620070.0,31017927,KOSPI
2024-02-16,10470.0,11900.0,10470.0,10950.0,5696858.0,64474234560.0,339646300650.0,31017927,KOSPI
2024-03-11,8510.0,8750.0,8370.0,8540.0,302917.0,2600630260.0,264893096580.0,31017927,KOSPI
2024-04-17,7210.0,7350.0,7160.0,7160.0,178772.0,1290755580.0,222088357320.0,31017927,KOSPI
2024-05-22,8370.0,8900.0,8080.0,8200.0,2031676.0,17300027340.0,254347001400.0,31017927,KOSPI
2024-06-04,8140.0,9080.0,7850.0,7920.0,3397921.0,28898195000.0,245661981840.0,31017927,KOSPI
2024-08-05,6230.0,6230.0,5000.0,5380.0,410405.0,2333162810.0,166876447260.0,31017927,KOSPI
2024-08-14,6010.0,6350.0,6010.0,6170.0,250001.0,1545424340.0,191380609590.0,31017927,KOSPI
```

Backtest:

| window | peak/high | peak date | trough/low | trough date | MFE | MAE |
|---|---:|---|---:|---|---:|---:|
| 30 calendar days | 11900 | 2024-02-16 | 8370 | 2024-03-11 | +13.66% | -20.06% |
| 90 calendar days | 11900 | 2024-02-16 | 7160 | 2024-04-17 | +13.66% | -31.61% |
| 180 calendar days | 11900 | 2024-02-16 | 5000 | 2024-08-05 | +13.66% | -52.24% |

Interpretation:

```text
011810 is the extreme-MAE resource-trading counterexample.
The first window had some MFE, but the peak came on entry day and the forward MAE rapidly moved into 4B/4C territory.
C16 should not promote resource-trading or critical-mineral optionality without supply contracts, inventory control, customer quality, and margin evidence.
```

---

## 7. Machine-readable trigger JSONL

```jsonl
{"row_type":"trigger","research_id":"R4L75_C16_RARE_METAL_RESOURCE_ROUTER","round":"R4","loop":75,"large_sector_id":"L4_MATERIALS_SPREAD_RESOURCE","canonical_archetype_id":"C16_STRATEGIC_RESOURCE_POLICY_SUPPLY","fine_archetype_id":"RARE_EARTH_NICKEL_RESOURCE_POLICY_SUPPLY_AND_THEME_SPIKE_HIGH_MAE_ROUTER","symbol":"081150","name":"티플랙스","trigger_type":"Stage2-Actionable-Guarded","trigger_family":"rare_metal_nickel_policy_supply_low_mae_to_drawdown_watch","trigger_date":"2024-04-18","entry_date":"2024-04-19","entry_price":2805.0,"entry_price_type":"next_tradable_open_after_rare_metal_policy_supply_burst","price_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","mfe_30d_pct":11.05,"mae_30d_pct":0.0,"mfe_90d_pct":20.14,"mae_90d_pct":0.0,"mfe_180d_pct":20.14,"mae_180d_pct":-17.65,"peak_price_180d":3370.0,"peak_date_180d":"2024-05-20","trough_price_180d":2310.0,"trough_date_180d":"2024-08-05","calibration_usable":true,"case_polarity":"positive_guarded_drawdown_watch","evidence_url_pending":true,"source_proxy_only":true,"non_price_evidence_strength":"medium_low_pending_url_repair","price_only_blowoff":false,"expected_stage_current_profile":"Stage2-Guarded_to_Yellow_only_if_resource_supply_customer_margin_bridge_repaired","residual_error_type":"rare_metal_supply_path_had_usable_mfe_but_180d_drawdown_requires_url_repaired_resource_customer_margin_bridge_before_green"}
{"row_type":"trigger","research_id":"R4L75_C16_RARE_METAL_RESOURCE_ROUTER","round":"R4","loop":75,"large_sector_id":"L4_MATERIALS_SPREAD_RESOURCE","canonical_archetype_id":"C16_STRATEGIC_RESOURCE_POLICY_SUPPLY","fine_archetype_id":"RARE_EARTH_NICKEL_RESOURCE_POLICY_SUPPLY_AND_THEME_SPIKE_HIGH_MAE_ROUTER","symbol":"047400","name":"유니온머티리얼","trigger_type":"Stage2-FalsePositive-Candidate","trigger_family":"rare_earth_permanent_magnet_policy_label_weak_mfe_high_mae","trigger_date":"2024-04-19","entry_date":"2024-04-22","entry_price":2995.0,"entry_price_type":"next_tradable_open_after_rare_earth_theme_spike","price_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","mfe_30d_pct":3.01,"mae_30d_pct":-11.35,"mfe_90d_pct":3.01,"mae_90d_pct":-17.86,"mfe_180d_pct":3.01,"mae_180d_pct":-35.23,"peak_price_180d":3085.0,"peak_date_180d":"2024-05-17","trough_price_180d":1940.0,"trough_date_180d":"2024-09-09","calibration_usable":true,"case_polarity":"counterexample_weak_mfe_high_mae","evidence_url_pending":true,"source_proxy_only":true,"non_price_evidence_strength":"low_pending_url_repair","price_only_blowoff":false,"expected_stage_current_profile":"blocked_Stage2_or_4B_high_MAE_watch_until_customer_supply_margin_bridge_repaired","residual_error_type":"rare_earth_policy_label_had_weak_mfe_and_hard_180d_mae_without_company_specific_supply_margin_bridge"}
{"row_type":"trigger","research_id":"R4L75_C16_RARE_METAL_RESOURCE_ROUTER","round":"R4","loop":75,"large_sector_id":"L4_MATERIALS_SPREAD_RESOURCE","canonical_archetype_id":"C16_STRATEGIC_RESOURCE_POLICY_SUPPLY","fine_archetype_id":"RARE_EARTH_NICKEL_RESOURCE_POLICY_SUPPLY_AND_THEME_SPIKE_HIGH_MAE_ROUTER","symbol":"011810","name":"STX","trigger_type":"Stage2-FalsePositive-Candidate","trigger_family":"strategic_resource_trading_lithium_nickel_policy_spike_high_mae","trigger_date":"2024-02-15","entry_date":"2024-02-16","entry_price":10470.0,"entry_price_type":"next_tradable_open_after_resource_trading_policy_spike","price_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","mfe_30d_pct":13.66,"mae_30d_pct":-20.06,"mfe_90d_pct":13.66,"mae_90d_pct":-31.61,"mfe_180d_pct":13.66,"mae_180d_pct":-52.24,"peak_price_180d":11900.0,"peak_date_180d":"2024-02-16","trough_price_180d":5000.0,"trough_date_180d":"2024-08-05","calibration_usable":true,"case_polarity":"counterexample_resource_trading_spike_extreme_mae","evidence_url_pending":true,"source_proxy_only":true,"non_price_evidence_strength":"low_pending_url_repair","price_only_blowoff":false,"expected_stage_current_profile":"blocked_Stage2_or_4B_4C_high_MAE_watch","residual_error_type":"resource_trading_policy_spike_had_first_window_mfe_but_90d_180d_mae_blocks_positive_stage_without_supply_contract_margin_bridge"}
```

---

## 8. Score simulation and raw component breakdown

This is shadow-only and does not change production scoring.

| symbol | policy/supply relevance | resource exposure bridge | customer / contract bridge | inventory / working capital | market mispricing | margin conversion | information confidence | shadow total | intended route |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| `081150` | 11 | 9 | 6 | 6 | 8 | 5 | 5 | 50 | Stage2-Guarded / Yellow only after evidence repair |
| `047400` | 9 | 5 | 3 | 3 | 3 | 2 | 4 | 29 | blocked Stage2 or local 4B/high-MAE watch |
| `011810` | 10 | 4 | 3 | 2 | 5 | 2 | 4 | 30 | blocked Stage2 / 4B-4C high-MAE watch |

### Current calibrated profile stress test

The current calibrated profile already blocks pure price-only blowoff.  
The remaining C16 issue is **strategic-resource label without company economics**:

```text
C16 guarded positive path:
  strategic resource / rare-metal relevance
  + first 90D MFE is usable
  + MAE is initially contained
  + evidence is still source_proxy_only
  => Stage2-Guarded, no Green until URL-repaired evidence

C16 weak-MFE resource label:
  rare-earth / magnet / resource label exists
  + MFE_30D < +5%
  + MAE_180D <= -30%
  + no customer/supply/margin bridge
  => block Stage2 or local 4B/high-MAE watch

C16 resource-trading spike:
  MFE appears on entry day
  + MAE_90D <= -30%
  + MAE_180D <= -50%
  + bridge remains unrepaired
  => 4B/4C high-MAE watch, no positive-stage promotion
```

`081150` prevents overblocking: not every strategic-resource case should be rejected if the early path is contained.  
`047400` and `011810` show why C16 needs a company-specific supply/margin bridge, not only a policy label.

---

## 9. Aggregate metrics

```json
{
  "row_type": "aggregate",
  "research_id": "R4L75_C16_RARE_METAL_RESOURCE_ROUTER",
  "round": "R4",
  "loop": 75,
  "large_sector_id": "L4_MATERIALS_SPREAD_RESOURCE",
  "canonical_archetype_id": "C16_STRATEGIC_RESOURCE_POLICY_SUPPLY",
  "fine_archetype_id": "RARE_EARTH_NICKEL_RESOURCE_POLICY_SUPPLY_AND_THEME_SPIKE_HIGH_MAE_ROUTER",
  "case_count": 3,
  "calibration_usable_case_count": 3,
  "positive_guarded_case_count": 1,
  "counterexample_count": 2,
  "new_symbol_count": 3,
  "source_proxy_only_count": 3,
  "evidence_url_pending_count": 3,
  "avg_mfe_30d_pct": 9.24,
  "avg_mae_30d_pct": -10.47,
  "avg_mfe_90d_pct": 12.27,
  "avg_mae_90d_pct": -16.49,
  "avg_mfe_180d_pct": 12.27,
  "avg_mae_180d_pct": -35.04,
  "max_mfe_180d_pct": 20.14,
  "worst_mae_180d_pct": -52.24
}
```

---

## 10. 4B proximity split

```json
{
  "row_type": "4b_split",
  "research_id": "R4L75_C16_RARE_METAL_RESOURCE_ROUTER",
  "stage2_guarded_or_yellow_candidate": [
    {
      "symbol": "081150",
      "reason": "90D path had +20.14% MFE and no MAE; 180D MAE later reached -17.65%, so Yellow/Green requires evidence repair"
    }
  ],
  "blocked_stage2_or_local_4b_watch": [
    {
      "symbol": "047400",
      "reason": "MFE stayed only +3.01% while 180D MAE reached -35.23%; policy label lacked company-specific bridge"
    }
  ],
  "blocked_stage2_or_4c_watch": [
    {
      "symbol": "011810",
      "reason": "resource-trading spike had entry-day peak and 180D MAE reached -52.24%"
    }
  ],
  "full_4b_or_green_requires_non_price_evidence": [
    "strategic resource / rare-earth / nickel exposure quality",
    "supply contract or trading volume",
    "inventory and working-capital control",
    "customer quality and policy-linked procurement",
    "gross margin / operating margin conversion"
  ]
}
```

---

## 11. Shadow rule candidate

```yaml
row_type: canonical_archetype_rule_candidate
canonical_archetype_id: C16_STRATEGIC_RESOURCE_POLICY_SUPPLY
fine_archetype_id: RARE_EARTH_NICKEL_RESOURCE_POLICY_SUPPLY_AND_THEME_SPIKE_HIGH_MAE_ROUTER
rule_name: C16_rare_metal_resource_policy_supply_vs_theme_spike_high_mae_router
production_scoring_changed: false
shadow_weight_only: true
```

### Proposed routing logic

```text
For C16 strategic resource / policy supply cases:

Tier A: guarded strategic-resource supply path
  Conditions:
    - strategic resource or rare-metal exposure is plausible
    - 90D MFE >= +15%
    - 90D MAE remains better than -10%
    - evidence_url_pending or source_proxy_only remains true
  Routing:
    - Stage2-Guarded allowed
    - Yellow only after URL-repaired supply/customer/inventory/margin bridge
    - no Green while evidence remains pending

Tier B: weak-MFE policy label
  Conditions:
    - MFE_30D < +5%
    - MAE_180D <= -30%
    - no company-specific supply/customer/margin bridge
  Routing:
    - block Stage2 or local 4B/high-MAE watch
    - count as false-positive counterexample

Tier C: resource-trading entry-day spike
  Conditions:
    - peak occurs on entry day or first 5 trading days
    - MAE_90D <= -30% or MAE_180D <= -50%
    - bridge evidence remains source_proxy_only
  Routing:
    - block Stage2
    - route to 4B/4C high-MAE watch
    - no positive weight promotion
```

### Suggested shadow delta

```json
{
  "row_type": "shadow_weight",
  "axis": "c16_rare_metal_resource_policy_supply_vs_theme_spike_high_mae_router",
  "scope": "canonical_archetype_id:C16_STRATEGIC_RESOURCE_POLICY_SUPPLY",
  "proposal": {
    "source_proxy_only_green_allowed": false,
    "supply_customer_inventory_margin_bridge_required_for_green": true,
    "guarded_resource_path_mfe90_threshold_pct": 15.0,
    "guarded_resource_path_mae90_min_pct": -10.0,
    "weak_mfe_threshold_30d_pct": 5.0,
    "weak_mfe_hard_mae_threshold_180d_pct": -30.0,
    "resource_trading_spike_mae90_threshold_pct": -30.0,
    "resource_trading_spike_hard_mae180_threshold_pct": -50.0,
    "entry_day_or_first5_peak_blocks_stage2_without_bridge": true,
    "positive_weight_blocked_until_url_repair": true
  },
  "confidence": "medium_low_until_url_repair",
  "apply_now": false,
  "reason": "One guarded rare-metal resource path and two rare-earth/resource-trading high-MAE counterexamples show that C16 should require URL-repaired supply/customer/inventory/margin evidence before Yellow/Green."
}
```

---

## 12. Residual contribution summary

```json
{
  "row_type": "residual_contribution",
  "research_id": "R4L75_C16_RARE_METAL_RESOURCE_ROUTER",
  "large_sector_id": "L4_MATERIALS_SPREAD_RESOURCE",
  "canonical_archetype_id": "C16_STRATEGIC_RESOURCE_POLICY_SUPPLY",
  "contribution": "Adds three non-top-covered C16 strategic resource / rare-metal policy-supply cases and separates a guarded rare-metal supply path from weak-MFE and resource-trading high-MAE counterexamples. C16 Yellow/Green should require URL-repaired strategic-resource exposure, supply/customer contracts, inventory control, working-capital quality, and margin conversion evidence.",
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
  "data_quality_blocker": "All three non-price strategic-resource triggers require URL-level repair before positive weight promotion.",
  "guardrail_added": "C16 source_proxy_only cases with MFE_30D < +5% and MAE_180D <= -30% should block Stage2; resource-trading spikes with MAE_90D <= -30% or MAE_180D <= -50% should route to 4B/4C high-MAE watch."
}
```

One-line contribution:

```text
This loop adds 3 new independent cases, 2 counterexamples, and 2 residual errors for R4/L4_MATERIALS_SPREAD_RESOURCE/C16_STRATEGIC_RESOURCE_POLICY_SUPPLY.
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
    081150: false
    047400: false
    011810: false
  evidence_url_pending:
    081150: true
    047400: true
    011810: true
  source_proxy_only:
    081150: true
    047400: true
    011810: true
  special_handling:
    011810:
      corporate_action_candidate_date: "2024-01-05"
      note: "Candidate date is before selected 2024-02-16 entry; entry~D+180 window is after this candidate."
```

Limitations:

```text
- Price path is validated against Stock-Web tradable OHLC rows.
- Non-price evidence is not URL-repaired in this run.
- Therefore this artifact is useful for C16 strategic resource / rare-metal policy-supply residual shape and high-MAE guardrail design, but should not promote positive weights until filings, IR, customs/export data, contract disclosures, or reports verify resource exposure, supply/customer contracts, inventory, working capital, and margin conversion.
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
2. Preserve R4 / loop 75 metadata.
3. Add the cases to C16_STRATEGIC_RESOURCE_POLICY_SUPPLY only if parser validation passes.
4. Treat all three non-price triggers as evidence_url_pending=true and source_proxy_only=true until URL-level evidence is repaired.
5. Do not use these rows for positive weight promotion until filings/IR/customs-export/contract-disclosure/report data verifies strategic resource exposure, supply contracts, customer quality, inventory, working-capital, and margin conversion.
6. Add a shadow-only rule candidate named C16_rare_metal_resource_policy_supply_vs_theme_spike_high_mae_router.
7. Do not loosen Stage3-Green.
8. Add C16-specific guards:
   - source_proxy_only -> no Green
   - Green requires repaired supply/customer/inventory/margin bridge
   - MFE_90D >= +15% and MAE_90D > -10% may remain Stage2-Guarded until evidence repair
   - MFE_30D < +5% and MAE_180D <= -30% -> block Stage2 or local 4B/high-MAE watch
   - entry-day or first-5-day peak with MAE_90D <= -30% or MAE_180D <= -50% -> block Stage2 / 4B-4C watch
9. Keep production scoring unchanged unless later batch promotion logic independently marks this axis safe.
```

---

## 15. Next round state

```text
completed_round = R4
completed_loop = 75
next_round = R5
next_loop = 75
next_large_sector_hint = L5_CONSUMER_BRAND_DISTRIBUTION
round_schedule_status = valid
round_sector_consistency = pass
```
