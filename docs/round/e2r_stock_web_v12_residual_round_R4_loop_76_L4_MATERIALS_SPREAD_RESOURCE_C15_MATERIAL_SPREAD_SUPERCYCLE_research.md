# E2R Stock-Web v12 Residual Research — R4 Loop 76

```yaml
research_session: post_calibrated_sector_archetype_residual_research
mode: historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12
completed_round: R4
completed_loop: 76
next_round: R5
next_loop: 76
large_sector_id: L4_MATERIALS_SPREAD_RESOURCE
canonical_archetype_id: C15_MATERIAL_SPREAD_SUPERCYCLE
fine_archetype_id: COPPER_STAINLESS_NICKEL_SPREAD_PASS_THROUGH_AND_WEAK_MFE_HIGH_MAE_ROUTER
output_file: e2r_stock_web_v12_residual_round_R4_loop_76_L4_MATERIALS_SPREAD_RESOURCE_C15_MATERIAL_SPREAD_SUPERCYCLE_research.md
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
completed_loop  = 76
large_sector_id = L3_BATTERY_EV_GREEN_MOBILITY
canonical_archetype_id = C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK
```

Therefore:

```text
scheduled_round = R4
scheduled_loop  = 76
```

R4 maps to:

```text
large_sector_id = L4_MATERIALS_SPREAD_RESOURCE
```

This run selects:

```text
canonical_archetype_id = C15_MATERIAL_SPREAD_SUPERCYCLE
fine_archetype_id = COPPER_STAINLESS_NICKEL_SPREAD_PASS_THROUGH_AND_WEAK_MFE_HIGH_MAE_ROUTER
```

This is a valid R4/L4 pairing.

---

## 1. Why this R4/C15 run

The no-repeat ledger shows C15 is moderately covered but concentrated in large steel/chemical spread names:

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

This file avoids those top-covered symbols and adds three copper/stainless/nickel-material spread cases:

```text
103140 풍산
004560 현대비앤지스틸
032560 황금에스티
```

Research question:

```text
Can C15 separate a true copper/material spread pass-through rerating from stainless/nickel/titanium spread labels where first-window MFE or theme relevance exists but inventory, pass-through, demand, and margin conversion evidence is not repaired?
```

C15 is a spread bridge. A commodity price rising is only the wind; the company needs a sail: inventory position, pass-through timing, customer demand, product mix, and margin capture. If the sail is torn, the first gust can move the stock and still leave the entry exposed to later MAE.

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
| `103140` | 풍산 | active_like / KOSPI | none listed | true |
| `004560` | 현대비앤지스틸 | active_like / KOSPI | no 2024 overlap; latest listed candidate 2003-11-27 | true |
| `032560` | 황금에스티 | active_like / KOSPI | no 2024 overlap; latest listed candidate 2010-02-24 | true |

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
The Stock-Web price path is fully validated, but company-level copper/stainless/nickel/titanium inventory position, ASP pass-through, customer demand, product mix, raw-material cost timing, hedging, export/defense demand, gross margin, and operating leverage evidence still require later URL repair through filings, IR decks, commodity spread data, order disclosures, export data, or sell-side reports before production weight promotion.
```

C15 interpretation used here:

```text
C15 is not simply “material stock rose.”
It asks whether spread conditions become company economics:
- commodity spread / ASP movement,
- inventory and raw-material cost timing,
- pass-through ability,
- customer demand and product mix,
- export / defense / industrial end-market bridge,
- gross margin and operating leverage,
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
103140 + C15_MATERIAL_SPREAD_SUPERCYCLE -> no direct match found
004560 + C15_MATERIAL_SPREAD_SUPERCYCLE -> no direct match found
032560 + C15_MATERIAL_SPREAD_SUPERCYCLE -> no direct match found
```

Novelty accounting:

```json
{
  "new_symbol_count": 3,
  "minimum_new_symbol_count": 2,
  "positive_case_count": 1,
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
| `R4L76_C15_103140_20240308` | `103140` 풍산 | copper spread / defense-ammo material pass-through | positive anchor |
| `R4L76_C15_004560_20240312` | `004560` 현대비앤지스틸 | stainless/nickel spread theme initial-MFE / later high MAE | first-window-MFE later-MAE counterexample |
| `R4L76_C15_032560_20240521` | `032560` 황금에스티 | stainless/titanium material-spread weak-MFE slow fade | weak-MFE high-MAE counterexample |

The intended residual:

```text
C15 should separate:
1. copper/material spread paths where MFE expands and MAE remains contained;
2. stainless/nickel theme paths where first-window MFE appears but later MAE blocks Yellow/Green;
3. low-liquidity stainless/titanium material labels where MFE never expands and drawdown widens.
```

---

## 6. Stock-Web OHLC and backtest

### 6.1 `103140` 풍산 — copper spread / defense-ammo material pass-through positive anchor

Trigger:

```text
trigger_date = 2024-03-07
trigger_type = Stage2-Actionable
trigger_family = copper_spread_defense_ammo_material_pass_through_low_mae_rerating
entry_date = 2024-03-08
entry_price = 46400.0
entry_price_type = next_tradable_open_after_copper_spread_defense_material_burst
```

Relevant Stock-Web rows:

```csv
d,o,h,l,c,v,a,mc,s,m
2024-03-07,45000.0,51300.0,44900.0,46100.0,1930617.0,92592720500.0,1291919215800.0,28024278,KOSPI
2024-03-08,46400.0,48700.0,46350.0,48400.0,765449.0,36607460450.0,1356375055200.0,28024278,KOSPI
2024-03-13,45300.0,45750.0,44300.0,44450.0,407219.0,18216155800.0,1245679157100.0,28024278,KOSPI
2024-04-05,53200.0,53800.0,51500.0,51700.0,341662.0,17935563600.0,1448855172600.0,28024278,KOSPI
2024-04-12,60200.0,67500.0,59600.0,61600.0,2301877.0,145094424100.0,1726295524800.0,28024278,KOSPI
2024-05-14,78100.0,78900.0,75600.0,76300.0,625384.0,48386189700.0,2138252411400.0,28024278,KOSPI
2024-08-05,53300.0,54100.0,47000.0,49400.0,499656.0,25562625600.0,1384399333200.0,28024278,KOSPI
2024-09-04,63600.0,65300.0,62200.0,64100.0,304688.0,19624025100.0,1796356219800.0,28024278,KOSPI
```

Backtest:

| window | peak/high | peak date | trough/low | trough date | MFE | MAE |
|---|---:|---|---:|---|---:|---:|
| 30 calendar days | 53800 | 2024-04-05 | 44300 | 2024-03-13 | +15.95% | -4.53% |
| 90 calendar days | 78900 | 2024-05-14 | 44300 | 2024-03-13 | +70.04% | -4.53% |
| 180 calendar days | 78900 | 2024-05-14 | 44300 | 2024-03-13 | +70.04% | -4.53% |

Interpretation:

```text
103140 is the C15 positive anchor.
The copper/material spread path generated persistent MFE and kept MAE contained.
It supports Stage2-Actionable / Yellow after evidence repair, but Green still requires URL-repaired inventory, pass-through, customer demand, export/defense demand, and margin evidence.
```

### 6.2 `004560` 현대비앤지스틸 — stainless/nickel spread initial-MFE / later high-MAE branch

Trigger:

```text
trigger_date = 2024-03-11
trigger_type = Stage2-Actionable-Guarded
trigger_family = stainless_nickel_spread_theme_initial_mfe_later_high_mae
entry_date = 2024-03-12
entry_price = 18100.0
entry_price_type = next_tradable_open_after_stainless_nickel_spread_spike
```

Relevant Stock-Web rows:

```csv
d,o,h,l,c,v,a,mc,s,m
2024-03-11,17890.0,18030.0,17460.0,17970.0,99187.0,1752416810.0,270966233670.0,15078811,KOSPI
2024-03-12,18100.0,21950.0,17990.0,20900.0,3249524.0,65481785810.0,315147149900.0,15078811,KOSPI
2024-03-28,21000.0,22400.0,20850.0,22200.0,714850.0,15707896450.0,334749604200.0,15078811,KOSPI
2024-05-29,22200.0,23150.0,21850.0,22800.0,259904.0,5862429400.0,343796890800.0,15078811,KOSPI
2024-06-26,17700.0,18130.0,16670.0,16890.0,256291.0,4378456450.0,254681117790.0,15078811,KOSPI
2024-08-05,14450.0,14450.0,12200.0,12580.0,305076.0,4030111960.0,189691442380.0,15078811,KOSPI
2024-09-06,13440.0,13440.0,12700.0,12760.0,76017.0,978734250.0,192405628360.0,15078811,KOSPI
```

Backtest:

| window | peak/high | peak date | trough/low | trough date | MFE | MAE |
|---|---:|---|---:|---|---:|---:|
| 30 calendar days | 22400 | 2024-03-28 | 17990 | 2024-03-12 | +23.76% | -0.61% |
| 90 calendar days | 23150 | 2024-05-29 | 17990 | 2024-03-12 | +27.90% | -0.61% |
| 180 calendar days | 23150 | 2024-05-29 | 12200 | 2024-08-05 | +27.90% | -32.60% |

Interpretation:

```text
004560 is the first-window-MFE / later-high-MAE warning.
The initial stainless/nickel spread rally looked tradable for 30D/90D, but the 180D drawdown crossed a hard guardrail.
C15 should cap this at Stage2-Guarded or local 4B watch until inventory, pass-through, demand, and margin bridge evidence is repaired.
```

### 6.3 `032560` 황금에스티 — stainless/titanium material-spread weak-MFE slow fade

Trigger:

```text
trigger_date = 2024-05-20
trigger_type = Stage2-FalsePositive-Candidate
trigger_family = stainless_titanium_spread_theme_weak_mfe_slow_fade
entry_date = 2024-05-21
entry_price = 7120.0
entry_price_type = next_tradable_open_after_stainless_titanium_material_spread_burst
```

Relevant Stock-Web rows:

```csv
d,o,h,l,c,v,a,mc,s,m
2024-05-20,7040.0,7740.0,6920.0,7070.0,2731424.0,20100471980.0,120190000000.0,17000000,KOSPI
2024-05-21,7120.0,7360.0,6940.0,6980.0,335089.0,2397995000.0,118660000000.0,17000000,KOSPI
2024-06-20,6450.0,6520.0,6410.0,6520.0,23707.0,152880150.0,110840000000.0,17000000,KOSPI
2024-08-05,5960.0,5960.0,5340.0,5340.0,71403.0,398313250.0,90780000000.0,17000000,KOSPI
2024-11-15,4850.0,4945.0,4800.0,4945.0,15079.0,73185325.0,84065000000.0,17000000,KOSPI
```

Backtest:

| window | peak/high | peak date | trough/low | trough date | MFE | MAE |
|---|---:|---|---:|---|---:|---:|
| 30 calendar days | 7360 | 2024-05-21 | 6410 | 2024-06-20 | +3.37% | -9.97% |
| 90 calendar days | 7360 | 2024-05-21 | 5280 | 2024-08-06 | +3.37% | -25.84% |
| 180 calendar days | 7360 | 2024-05-21 | 4800 | 2024-11-15 | +3.37% | -32.58% |

Interpretation:

```text
032560 is the weak-MFE high-MAE C15 counterexample.
The material-spread label existed, but post-entry MFE never expanded and the forward path became a slow fade.
This should block Stage2 or route to local 4B/high-MAE watch unless a later independent trigger repairs inventory, pass-through, and margin evidence.
```

---

## 7. Machine-readable trigger JSONL

```jsonl
{"row_type":"trigger","research_id":"R4L76_C15_COPPER_STAINLESS_SPREAD_ROUTER","round":"R4","loop":76,"large_sector_id":"L4_MATERIALS_SPREAD_RESOURCE","canonical_archetype_id":"C15_MATERIAL_SPREAD_SUPERCYCLE","fine_archetype_id":"COPPER_STAINLESS_NICKEL_SPREAD_PASS_THROUGH_AND_WEAK_MFE_HIGH_MAE_ROUTER","symbol":"103140","name":"풍산","trigger_type":"Stage2-Actionable","trigger_family":"copper_spread_defense_ammo_material_pass_through_low_mae_rerating","trigger_date":"2024-03-07","entry_date":"2024-03-08","entry_price":46400.0,"entry_price_type":"next_tradable_open_after_copper_spread_defense_material_burst","price_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","mfe_30d_pct":15.95,"mae_30d_pct":-4.53,"mfe_90d_pct":70.04,"mae_90d_pct":-4.53,"mfe_180d_pct":70.04,"mae_180d_pct":-4.53,"peak_price_180d":78900.0,"peak_date_180d":"2024-05-14","trough_price_180d":44300.0,"trough_date_180d":"2024-03-13","calibration_usable":true,"case_polarity":"positive_anchor_copper_spread_low_mae","evidence_url_pending":true,"source_proxy_only":true,"non_price_evidence_strength":"medium_pending_url_repair","price_only_blowoff":false,"expected_stage_current_profile":"Stage2-Actionable_to_Yellow_after_copper_spread_inventory_pass_through_margin_bridge_repaired","residual_error_type":"copper_spread_path_supports_positive_route_but_green_requires_url_repaired_inventory_pass_through_customer_margin_bridge"}
{"row_type":"trigger","research_id":"R4L76_C15_COPPER_STAINLESS_SPREAD_ROUTER","round":"R4","loop":76,"large_sector_id":"L4_MATERIALS_SPREAD_RESOURCE","canonical_archetype_id":"C15_MATERIAL_SPREAD_SUPERCYCLE","fine_archetype_id":"COPPER_STAINLESS_NICKEL_SPREAD_PASS_THROUGH_AND_WEAK_MFE_HIGH_MAE_ROUTER","symbol":"004560","name":"현대비앤지스틸","trigger_type":"Stage2-Actionable-Guarded","trigger_family":"stainless_nickel_spread_theme_initial_mfe_later_high_mae","trigger_date":"2024-03-11","entry_date":"2024-03-12","entry_price":18100.0,"entry_price_type":"next_tradable_open_after_stainless_nickel_spread_spike","price_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","mfe_30d_pct":23.76,"mae_30d_pct":-0.61,"mfe_90d_pct":27.9,"mae_90d_pct":-0.61,"mfe_180d_pct":27.9,"mae_180d_pct":-32.6,"peak_price_180d":23150.0,"peak_date_180d":"2024-05-29","trough_price_180d":12200.0,"trough_date_180d":"2024-08-05","calibration_usable":true,"case_polarity":"counterexample_initial_mfe_later_high_mae","evidence_url_pending":true,"source_proxy_only":true,"non_price_evidence_strength":"medium_low_pending_url_repair","price_only_blowoff":false,"expected_stage_current_profile":"Stage2-Guarded_or_local_4B_watch_until_stainless_nickel_inventory_margin_bridge_repaired","residual_error_type":"stainless_nickel_spread_label_had_initial_mfe_but_180d_mae_blocks_yellow_green_without_inventory_margin_bridge"}
{"row_type":"trigger","research_id":"R4L76_C15_COPPER_STAINLESS_SPREAD_ROUTER","round":"R4","loop":76,"large_sector_id":"L4_MATERIALS_SPREAD_RESOURCE","canonical_archetype_id":"C15_MATERIAL_SPREAD_SUPERCYCLE","fine_archetype_id":"COPPER_STAINLESS_NICKEL_SPREAD_PASS_THROUGH_AND_WEAK_MFE_HIGH_MAE_ROUTER","symbol":"032560","name":"황금에스티","trigger_type":"Stage2-FalsePositive-Candidate","trigger_family":"stainless_titanium_spread_theme_weak_mfe_slow_fade","trigger_date":"2024-05-20","entry_date":"2024-05-21","entry_price":7120.0,"entry_price_type":"next_tradable_open_after_stainless_titanium_material_spread_burst","price_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","mfe_30d_pct":3.37,"mae_30d_pct":-9.97,"mfe_90d_pct":3.37,"mae_90d_pct":-25.84,"mfe_180d_pct":3.37,"mae_180d_pct":-32.58,"peak_price_180d":7360.0,"peak_date_180d":"2024-05-21","trough_price_180d":4800.0,"trough_date_180d":"2024-11-15","calibration_usable":true,"case_polarity":"counterexample_weak_mfe_slow_fade_high_mae","evidence_url_pending":true,"source_proxy_only":true,"non_price_evidence_strength":"low_pending_url_repair","price_only_blowoff":false,"expected_stage_current_profile":"blocked_Stage2_or_local_4B_high_MAE_watch_until_spread_inventory_margin_bridge_repaired","residual_error_type":"stainless_titanium_material_spread_label_had_weak_mfe_and_later_high_mae_without_inventory_pass_through_margin_bridge"}
```

---

## 8. Score simulation and raw component breakdown

This is shadow-only and does not change production scoring.

| symbol | spread relevance | inventory / cost timing | pass-through ability | customer demand / mix | market mispricing | margin conversion | information confidence | shadow total | intended route |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| `103140` | 14 | 11 | 11 | 10 | 13 | 10 | 6 | 75 | Stage2/Yellow after evidence repair |
| `004560` | 9 | 5 | 5 | 4 | 7 | 3 | 5 | 38 | Stage2-Guarded or local 4B watch |
| `032560` | 6 | 3 | 3 | 2 | 2 | 2 | 4 | 22 | blocked Stage2 / weak-MFE high-MAE watch |

### Current calibrated profile stress test

The current calibrated profile already blocks pure price-only blowoff.  
The remaining C15 issue is **commodity-spread label without pass-through and margin conversion**:

```text
C15 clean spread path:
  copper/material spread relevance
  + persistent MFE
  + contained MAE
  + URL-repaired inventory, pass-through, demand, and margin evidence
  => Stage2-Actionable / Yellow, possible Green after proof

C15 first-window-MFE later-MAE path:
  stainless/nickel spread label creates MFE
  + MAE_180D <= -30%
  + evidence remains source_proxy_only
  => Stage2-Guarded at most, local 4B watch, no Yellow/Green

C15 weak-MFE slow-fade path:
  material-spread label exists
  + MFE_90D < +5%
  + MAE_90D <= -25% or MAE_180D <= -30%
  + no inventory/pass-through bridge
  => block Stage2 or local 4B/high-MAE watch
```

`103140` prevents overblocking.  
`004560` shows why initial spread MFE cannot become Green without later MAE control.  
`032560` shows why low-liquidity material-spread labels need a weak-MFE brake.

---

## 9. Aggregate metrics

```json
{
  "row_type": "aggregate",
  "research_id": "R4L76_C15_COPPER_STAINLESS_SPREAD_ROUTER",
  "round": "R4",
  "loop": 76,
  "large_sector_id": "L4_MATERIALS_SPREAD_RESOURCE",
  "canonical_archetype_id": "C15_MATERIAL_SPREAD_SUPERCYCLE",
  "fine_archetype_id": "COPPER_STAINLESS_NICKEL_SPREAD_PASS_THROUGH_AND_WEAK_MFE_HIGH_MAE_ROUTER",
  "case_count": 3,
  "calibration_usable_case_count": 3,
  "positive_case_count": 1,
  "counterexample_count": 2,
  "new_symbol_count": 3,
  "source_proxy_only_count": 3,
  "evidence_url_pending_count": 3,
  "avg_mfe_30d_pct": 14.36,
  "avg_mae_30d_pct": -5.04,
  "avg_mfe_90d_pct": 33.77,
  "avg_mae_90d_pct": -10.33,
  "avg_mfe_180d_pct": 33.77,
  "avg_mae_180d_pct": -23.24,
  "max_mfe_180d_pct": 70.04,
  "worst_mae_180d_pct": -32.6
}
```

---

## 10. 4B proximity split

```json
{
  "row_type": "4b_split",
  "research_id": "R4L76_C15_COPPER_STAINLESS_SPREAD_ROUTER",
  "stage2_positive_or_yellow_candidate": [
    {
      "symbol": "103140",
      "reason": "copper/material spread path had +70.04% 180D MFE with only -4.53% MAE"
    }
  ],
  "stage2_guarded_or_local_4b_watch": [
    {
      "symbol": "004560",
      "reason": "first-window MFE existed, but 180D MAE reached -32.60%"
    }
  ],
  "blocked_stage2_or_local_4b_watch": [
    {
      "symbol": "032560",
      "reason": "MFE stayed only +3.37%, while 90D MAE reached -25.84% and 180D MAE reached -32.58%"
    }
  ],
  "full_4b_or_green_requires_non_price_evidence": [
    "commodity spread / ASP movement",
    "inventory and raw-material cost timing",
    "pass-through ability",
    "customer demand and product mix",
    "export / defense / industrial end-market bridge",
    "gross margin and operating leverage conversion"
  ]
}
```

---

## 11. Shadow rule candidate

```yaml
row_type: canonical_archetype_rule_candidate
canonical_archetype_id: C15_MATERIAL_SPREAD_SUPERCYCLE
fine_archetype_id: COPPER_STAINLESS_NICKEL_SPREAD_PASS_THROUGH_AND_WEAK_MFE_HIGH_MAE_ROUTER
rule_name: C15_copper_stainless_nickel_spread_pass_through_and_weak_mfe_high_mae_router
production_scoring_changed: false
shadow_weight_only: true
```

### Proposed routing logic

```text
For C15 copper/stainless/nickel/titanium material-spread cases:

Tier A: verified material-spread winner
  Conditions:
    - commodity spread / ASP relevance is clear
    - inventory, pass-through, demand, and margin evidence are URL-repaired
    - MFE_90D >= +25%
    - MAE_90D > -10%
  Routing:
    - Stage2-Actionable allowed
    - Stage3-Yellow allowed after evidence repair
    - Green only after spread-to-margin bridge is verified

Tier B: source-proxy first-window MFE / later high MAE
  Conditions:
    - MFE_30D >= +15%
    - MAE_180D <= -30%
    - evidence_url_pending or source_proxy_only remains true
  Routing:
    - Stage2-Guarded at most
    - local 4B/high-MAE watch
    - no Yellow/Green

Tier C: weak-MFE material-spread label
  Conditions:
    - MFE_90D < +5%
    - MAE_90D <= -25% or MAE_180D <= -30%
    - no repaired inventory/pass-through/margin bridge
  Routing:
    - block Stage2
    - local 4B/high-MAE watch
    - count as counterexample
```

### Suggested shadow delta

```json
{
  "row_type": "shadow_weight",
  "axis": "c15_copper_stainless_nickel_spread_pass_through_and_weak_mfe_high_mae_router",
  "scope": "canonical_archetype_id:C15_MATERIAL_SPREAD_SUPERCYCLE",
  "proposal": {
    "source_proxy_only_green_allowed": false,
    "inventory_pass_through_margin_bridge_required_for_green": true,
    "verified_spread_winner_mfe90_threshold_pct": 25.0,
    "verified_spread_winner_mae90_min_pct": -10.0,
    "first_window_mfe_threshold_30d_pct": 15.0,
    "later_high_mae_threshold_180d_pct": -30.0,
    "weak_mfe_threshold_90d_pct": 5.0,
    "weak_mfe_mae90_threshold_pct": -25.0,
    "weak_mfe_hard_mae180_threshold_pct": -30.0,
    "positive_weight_blocked_until_url_repair": true
  },
  "confidence": "medium_low_until_url_repair",
  "apply_now": false,
  "reason": "One copper/material spread winner and two stainless/nickel/titanium weak-MFE or later-MAE failures show that C15 should require URL-repaired inventory, pass-through, demand, and margin evidence before Yellow/Green."
}
```

---

## 12. Residual contribution summary

```json
{
  "row_type": "residual_contribution",
  "research_id": "R4L76_C15_COPPER_STAINLESS_SPREAD_ROUTER",
  "large_sector_id": "L4_MATERIALS_SPREAD_RESOURCE",
  "canonical_archetype_id": "C15_MATERIAL_SPREAD_SUPERCYCLE",
  "contribution": "Adds three non-top-covered C15 copper/stainless/nickel/titanium material-spread cases and separates a low-MAE copper spread winner from first-window-MFE later-high-MAE and weak-MFE material-spread failures. C15 Yellow/Green should require URL-repaired commodity spread, inventory timing, pass-through, demand, product mix, and margin conversion evidence.",
  "positive_case_added": 1,
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
  "data_quality_blocker": "All three non-price material-spread triggers require URL-level repair before positive weight promotion.",
  "guardrail_added": "C15 source_proxy_only cases with MFE_30D >= +15% but MAE_180D <= -30% should cap at Stage2-Guarded; weak-MFE cases with MFE_90D < +5% and MAE_90D <= -25% or MAE_180D <= -30% should block Stage2."
}
```

One-line contribution:

```text
This loop adds 3 new independent cases, 2 counterexamples, and 2 residual errors for R4/L4_MATERIALS_SPREAD_RESOURCE/C15_MATERIAL_SPREAD_SUPERCYCLE.
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
    103140: false
    004560: false
    032560: false
  evidence_url_pending:
    103140: true
    004560: true
    032560: true
  source_proxy_only:
    103140: true
    004560: true
    032560: true
```

Limitations:

```text
- Price path is validated against Stock-Web tradable OHLC rows.
- Non-price evidence is not URL-repaired in this run.
- Therefore this artifact is useful for C15 copper/stainless/nickel/titanium material-spread residual shape and high-MAE/weak-MFE guardrail design, but should not promote positive weights until filings, IR, commodity spread data, customer/order data, export data, or reports verify inventory, pass-through, demand, product mix, and margin conversion.
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
2. Preserve R4 / loop 76 metadata.
3. Add the cases to C15_MATERIAL_SPREAD_SUPERCYCLE only if parser validation passes.
4. Treat all three non-price triggers as evidence_url_pending=true and source_proxy_only=true until URL-level evidence is repaired.
5. Do not use these rows for positive weight promotion until filings/IR/commodity-spread/customer-order/export-data/report data verifies inventory, pass-through, customer demand, product mix, raw-material cost timing, and margin conversion.
6. Add a shadow-only rule candidate named C15_copper_stainless_nickel_spread_pass_through_and_weak_mfe_high_mae_router.
7. Do not loosen Stage3-Green.
8. Add C15-specific guards:
   - source_proxy_only -> no Green
   - Green requires repaired inventory / pass-through / margin bridge
   - MFE_90D >= +25% and MAE_90D > -10% may remain Stage2-Actionable / Yellow watch after evidence repair
   - MFE_30D >= +15% and MAE_180D <= -30% -> Stage2-Guarded at most / local 4B watch
   - MFE_90D < +5% and MAE_90D <= -25% or MAE_180D <= -30% -> block Stage2 / local 4B watch
9. Keep production scoring unchanged unless later batch promotion logic independently marks this axis safe.
```

---

## 15. Next round state

```text
completed_round = R4
completed_loop = 76
next_round = R5
next_loop = 76
next_large_sector_hint = L5_CONSUMER_BRAND_DISTRIBUTION
round_schedule_status = valid
round_sector_consistency = pass
```
