# E2R Stock-Web v12 Residual Research — R10 Loop 73

```yaml
research_session: post_calibrated_sector_archetype_residual_research
mode: historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12
completed_round: R10
completed_loop: 73
next_round: R11
next_loop: 73
large_sector_id: L9_CONSTRUCTION_REALESTATE_HOUSING
canonical_archetype_id: C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK
fine_archetype_id: REGIONAL_CONSTRUCTION_PF_LIQUIDITY_REPAIR_AND_SLOW_FADE_ROUTER
output_file: e2r_stock_web_v12_residual_round_R10_loop_73_L9_CONSTRUCTION_REALESTATE_HOUSING_C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK_research.md
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
completed_round = R9
completed_loop  = 73
large_sector_id = L3_BATTERY_EV_GREEN_MOBILITY
canonical_archetype_id = C13_BATTERY_JV_UTILIZATION_AMPC_IRA
```

Therefore:

```text
scheduled_round = R10
scheduled_loop  = 73
```

R10 maps to:

```text
large_sector_id = L9_CONSTRUCTION_REALESTATE_HOUSING
```

This run selects:

```text
canonical_archetype_id = C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK
fine_archetype_id = REGIONAL_CONSTRUCTION_PF_LIQUIDITY_REPAIR_AND_SLOW_FADE_ROUTER
```

This is a valid R10/L9 pairing.

---

## 1. Why this R10/C30 run

The no-repeat ledger shows C30 is heavily covered but concentrated in large contractors and already-stressed top repeat names:

```text
C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK:
  rows: 113
  symbols: 34
  date_range: 2021-03-11~2024-09-30
  good/bad S2: 15/18
  4B/4C: 14/28
  URL/proxy: 0/0
  top covered symbols: 006360(13), UNKNOWN_SYMBOL(13), 294870(12), 047040(11), 000720(8), 375500(6)
```

This run avoids those top-covered construction names and uses regional / mid-small construction balance-sheet cases:

```text
035890 서희건설
013580 계룡건설
002990 금호건설
```

Research question:

```text
Can C30 distinguish a contained-MAE regional construction repair path from a slow PF/liquidity fade whose first bounce is too weak to become Stage2?
```

C30 is a credit-risk archetype. A construction stock can look cheap, and a short relief rally can look like “balance-sheet repair.” But the actual bridge has to be made of liquidity, receivable conversion, PF exposure reduction, refinancing, unsold inventory control, and working-capital repair. If that bridge is not present, the stock can stand still for a few weeks and then quietly sink.

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
| `035890` | 서희건설 | active_like / KOSDAQ | no 2024 overlap; latest listed candidate 2012-07-12 | true |
| `013580` | 계룡건설 | active_like / KOSPI | no 2024 overlap; old 1999 candidate only | true |
| `002990` | 금호건설 | active_like / KOSPI | no 2024 overlap; latest listed candidate 2013-11-07 | true |

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
The Stock-Web price path is fully validated, but company-level PF guarantee exposure, refinancing, short-term borrowings, receivables, unbilled construction revenue, unsold inventory, cash-flow repair, and covenant/liquidity evidence still require later URL repair through filings, credit reports, IR, or disclosure data before any production weight promotion.
```

C30 interpretation used here:

```text
C30 is not simply “construction stock bounced.”
It asks whether the balance sheet is actually stabilizing:
- PF guarantee / contingent-liability exposure,
- refinancing and maturity wall,
- working capital and receivables,
- unsold inventory,
- impairment/cost-overrun risk,
- and liquidity/covenant headroom.
```

This run is useful as a C30 residual-shape and guardrail file, not as a positive production patch.

---

## 4. No-repeat and novelty check

Hard duplicate key:

```text
canonical_archetype_id + symbol + trigger_type + entry_date
```

Targeted repository searches before writing:

```text
035890 + C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK -> no direct match found
013580 + C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK -> no direct match found
002990 + C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK -> no direct match found
```

Novelty accounting:

```json
{
  "new_symbol_count": 3,
  "minimum_new_symbol_count": 2,
  "positive_guarded_case_count": 2,
  "counterexample_count": 1,
  "new_independent_case_ratio": 1.00,
  "duplicate_status": "pass",
  "data_quality_status": "source_proxy_only_non_price_evidence"
}
```

---

## 5. Case design

| case_id | symbol | trigger family | research role |
|---|---|---|---|
| `R10L73_C30_035890_20240821` | `035890` 서희건설 | regional housing / PF repair rally with contained MAE | positive-guarded / low-MAE holdout |
| `R10L73_C30_013580_20240715` | `013580` 계룡건설 | regional contractor low-PBR / order backlog relief | positive-guarded / later drawdown watch |
| `R10L73_C30_002990_20240315` | `002990` 금호건설 | PF/liquidity slow fade after weak relief | counterexample / Stage2 false-positive |

The intended residual:

```text
C30 should separate:
1. construction/PF relief paths where MAE remains contained and the stock can stay Stage2-Guarded;
2. regional contractor low-PBR relief where Yellow still requires balance-sheet evidence repair;
3. weak relief entries where MFE is tiny and 90D/180D MAE exposes a slow liquidity fade.
```

---

## 6. Stock-Web OHLC and backtest

### 6.1 `035890` 서희건설 — regional PF/housing repair rally with contained MAE

Trigger:

```text
trigger_date = 2024-08-20
trigger_type = Stage2-Actionable-Guarded
trigger_family = regional_housing_pf_repair_contained_mae
entry_date = 2024-08-21
entry_price = 1411.0
entry_price_type = next_tradable_open
```

Relevant Stock-Web rows:

```csv
d,o,h,l,c,v,a,mc,s,m
2024-08-20,1390.0,1407.0,1379.0,1405.0,738954.0,1030266452.0,322880882085.0,229808457,KOSDAQ
2024-08-21,1411.0,1459.0,1409.0,1458.0,1237833.0,1786212463.0,335060730306.0,229808457,KOSDAQ
2024-09-20,1515.0,1525.0,1481.0,1481.0,571900.0,854201043.0,340346324817.0,229808457,KOSDAQ
2024-10-10,1561.0,1621.0,1561.0,1577.0,1218702.0,1930076202.0,362407936689.0,229808457,KOSDAQ
2024-11-12,1396.0,1675.0,1391.0,1427.0,5913267.0,9016676282.0,327936668139.0,229808457,KOSDAQ
2024-11-14,1375.0,1426.0,1357.0,1399.0,854272.0,1185262293.0,321502031343.0,229808457,KOSDAQ
2025-01-14,1645.0,1664.0,1636.0,1648.0,548002.0,903451968.0,378724337136.0,229808457,KOSDAQ
2025-02-04,1520.0,1520.0,1482.0,1488.0,313947.0,469227497.0,341954984016.0,229808457,KOSDAQ
```

Backtest:

| window | peak/high | peak date | trough/low | trough date | MFE | MAE |
|---|---:|---|---:|---|---:|---:|
| 30 calendar days | 1525 | 2024-09-20 | 1405 | 2024-08-22 | +8.08% | -0.43% |
| 90 calendar days | 1675 | 2024-11-12 | 1357 | 2024-11-14 | +18.71% | -3.83% |
| 180 calendar days | 1675 | 2024-11-12 | 1357 | 2024-11-14 | +18.71% | -3.83% |

Interpretation:

```text
035890 is the clean positive-guarded C30 holdout.
The upside was not huge, but the path had unusually contained MAE for a construction/PF-sensitive name.
This can remain Stage2-Guarded / Yellow candidate after balance-sheet evidence repair, but it is still not Green while non-price evidence is URL-pending.
```

### 6.2 `013580` 계룡건설 — regional contractor low-PBR / order-backlog relief

Trigger:

```text
trigger_date = 2024-07-12
trigger_type = Stage2-Actionable-Guarded
trigger_family = regional_contractor_low_pbr_order_backlog_relief
entry_date = 2024-07-15
entry_price = 13780.0
entry_price_type = next_tradable_open
```

Relevant Stock-Web rows:

```csv
d,o,h,l,c,v,a,mc,s,m
2024-07-12,13690.0,14060.0,13670.0,13730.0,26848.0,372339000.0,122621353110.0,8930907,KOSPI
2024-07-15,13780.0,14210.0,13740.0,14210.0,41992.0,587488490.0,126908188470.0,8930907,KOSPI
2024-07-17,14210.0,15490.0,14210.0,15220.0,233961.0,3528811590.0,135928404540.0,8930907,KOSPI
2024-08-05,14500.0,14500.0,13210.0,13630.0,104755.0,1449499860.0,121728262410.0,8930907,KOSPI
2024-08-21,15140.0,15580.0,14980.0,15470.0,89247.0,1375497370.0,138161131290.0,8930907,KOSPI
2024-09-20,14240.0,14480.0,14240.0,14470.0,11189.0,160620350.0,129230224290.0,8930907,KOSPI
2025-01-09,12820.0,12850.0,12480.0,12630.0,64065.0,804609310.0,112797355410.0,8930907,KOSPI
2025-02-19,13010.0,13350.0,12900.0,13260.0,52489.0,692053380.0,118423826820.0,8930907,KOSPI
```

Backtest:

| window | peak/high | peak date | trough/low | trough date | MFE | MAE |
|---|---:|---|---:|---|---:|---:|
| 30 calendar days | 15490 | 2024-07-17 | 13210 | 2024-08-05 | +12.41% | -4.14% |
| 90 calendar days | 15580 | 2024-08-21 | 13210 | 2024-08-05 | +13.06% | -4.14% |
| 180 calendar days | 15580 | 2024-08-21 | 12480 | 2025-01-09 | +13.06% | -9.43% |

Interpretation:

```text
013580 is a second positive-guarded case.
The path is not explosive, but it does not behave like a PF-break false positive either.
For C30, this should remain Stage2-Guarded until order backlog, receivables, PF exposure, and working-capital evidence are repaired.
```

### 6.3 `002990` 금호건설 — weak relief followed by PF/liquidity slow fade

Trigger:

```text
trigger_date = 2024-03-14
trigger_type = Stage2-FalsePositive-Candidate
trigger_family = pf_liquidity_slow_fade_after_weak_relief
entry_date = 2024-03-15
entry_price = 4710.0
entry_price_type = next_tradable_open_after_breakdown
```

Relevant Stock-Web rows:

```csv
d,o,h,l,c,v,a,mc,s,m
2024-03-14,4800.0,4810.0,4710.0,4710.0,120001.0,569468095.0,174051432450.0,36953595,KOSPI
2024-03-15,4710.0,4735.0,4615.0,4615.0,125657.0,584903845.0,170540840925.0,36953595,KOSPI
2024-04-12,4290.0,4340.0,4285.0,4300.0,9109.0,39148860.0,158900458500.0,36953595,KOSPI
2024-06-13,3890.0,3890.0,3645.0,3710.0,194257.0,721596615.0,137097837450.0,36953595,KOSPI
2024-08-05,3580.0,3595.0,3205.0,3205.0,125435.0,426734035.0,118436271975.0,36953595,KOSPI
2024-09-11,3260.0,3265.0,3200.0,3230.0,20647.0,66693795.0,119360111850.0,36953595,KOSPI
2024-11-12,2780.0,3280.0,2685.0,2920.0,338250.0,1013151250.0,107904497400.0,36953595,KOSPI
2024-12-09,2655.0,2695.0,2530.0,2530.0,114003.0,294921330.0,93492595350.0,36953595,KOSPI
```

Backtest:

| window | peak/high | peak date | trough/low | trough date | MFE | MAE |
|---|---:|---|---:|---|---:|---:|
| 30 calendar days | 4735 | 2024-03-15 | 4285 | 2024-04-12 | +0.53% | -9.02% |
| 90 calendar days | 4735 | 2024-03-15 | 3645 | 2024-06-13 | +0.53% | -22.61% |
| 180 calendar days | 4735 | 2024-03-15 | 3200 | 2024-09-11 | +0.53% | -32.06% |

Interpretation:

```text
002990 is the clean C30 false-positive branch.
The trigger had almost no remaining MFE and then slowly leaked into large MAE.
This is the “quiet PF/liquidity fade” pattern: it may not explode downward on day one, but it fails the capital-preservation test. It should block Stage2/Green until hard liquidity repair evidence appears.
```

---

## 7. Machine-readable trigger JSONL

```jsonl
{"row_type":"trigger","research_id":"R10L73_C30_REGIONAL_PF_ROUTER","round":"R10","loop":73,"large_sector_id":"L9_CONSTRUCTION_REALESTATE_HOUSING","canonical_archetype_id":"C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK","fine_archetype_id":"REGIONAL_CONSTRUCTION_PF_LIQUIDITY_REPAIR_AND_SLOW_FADE_ROUTER","symbol":"035890","name":"서희건설","trigger_type":"Stage2-Actionable-Guarded","trigger_family":"regional_housing_pf_repair_contained_mae","trigger_date":"2024-08-20","entry_date":"2024-08-21","entry_price":1411.0,"entry_price_type":"next_tradable_open","price_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","mfe_30d_pct":8.08,"mae_30d_pct":-0.43,"mfe_90d_pct":18.71,"mae_90d_pct":-3.83,"mfe_180d_pct":18.71,"mae_180d_pct":-3.83,"peak_price_180d":1675.0,"peak_date_180d":"2024-11-12","trough_price_180d":1357.0,"trough_date_180d":"2024-11-14","calibration_usable":true,"case_polarity":"positive_guarded_low_mae","evidence_url_pending":true,"source_proxy_only":true,"non_price_evidence_strength":"medium_pending_url_repair","price_only_blowoff":false,"expected_stage_current_profile":"Stage2-Guarded_to_Yellow_if_pf_liquidity_working_capital_bridge_repaired","residual_error_type":"contained_mae_regional_repair_case_but_green_requires_balance_sheet_evidence"}
{"row_type":"trigger","research_id":"R10L73_C30_REGIONAL_PF_ROUTER","round":"R10","loop":73,"large_sector_id":"L9_CONSTRUCTION_REALESTATE_HOUSING","canonical_archetype_id":"C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK","fine_archetype_id":"REGIONAL_CONSTRUCTION_PF_LIQUIDITY_REPAIR_AND_SLOW_FADE_ROUTER","symbol":"013580","name":"계룡건설","trigger_type":"Stage2-Actionable-Guarded","trigger_family":"regional_contractor_low_pbr_order_backlog_relief","trigger_date":"2024-07-12","entry_date":"2024-07-15","entry_price":13780.0,"entry_price_type":"next_tradable_open","price_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","mfe_30d_pct":12.41,"mae_30d_pct":-4.14,"mfe_90d_pct":13.06,"mae_90d_pct":-4.14,"mfe_180d_pct":13.06,"mae_180d_pct":-9.43,"peak_price_180d":15580.0,"peak_date_180d":"2024-08-21","trough_price_180d":12480.0,"trough_date_180d":"2025-01-09","calibration_usable":true,"case_polarity":"positive_guarded","evidence_url_pending":true,"source_proxy_only":true,"non_price_evidence_strength":"medium_low_pending_url_repair","price_only_blowoff":false,"expected_stage_current_profile":"Stage2-Guarded_until_order_backlog_pf_receivable_bridge_repaired","residual_error_type":"regional_contractor_relief_is_usable_but_green_requires_credit_and_working_capital_repair"}
{"row_type":"trigger","research_id":"R10L73_C30_REGIONAL_PF_ROUTER","round":"R10","loop":73,"large_sector_id":"L9_CONSTRUCTION_REALESTATE_HOUSING","canonical_archetype_id":"C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK","fine_archetype_id":"REGIONAL_CONSTRUCTION_PF_LIQUIDITY_REPAIR_AND_SLOW_FADE_ROUTER","symbol":"002990","name":"금호건설","trigger_type":"Stage2-FalsePositive-Candidate","trigger_family":"pf_liquidity_slow_fade_after_weak_relief","trigger_date":"2024-03-14","entry_date":"2024-03-15","entry_price":4710.0,"entry_price_type":"next_tradable_open_after_breakdown","price_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","mfe_30d_pct":0.53,"mae_30d_pct":-9.02,"mfe_90d_pct":0.53,"mae_90d_pct":-22.61,"mfe_180d_pct":0.53,"mae_180d_pct":-32.06,"peak_price_180d":4735.0,"peak_date_180d":"2024-03-15","trough_price_180d":3200.0,"trough_date_180d":"2024-09-11","calibration_usable":true,"case_polarity":"counterexample_slow_fade","evidence_url_pending":true,"source_proxy_only":true,"non_price_evidence_strength":"low_pending_url_repair","price_only_blowoff":false,"expected_stage_current_profile":"blocked_Stage2_or_4B_4C_high_MAE_watch","residual_error_type":"weak_relief_mfe_then_pf_liquidity_slow_fade_high_mae"}
```

---

## 8. Score simulation and raw component breakdown

This is shadow-only and does not change production scoring.

| symbol | liquidity/PF repair | balance-sheet visibility | working-capital quality | order/backlog quality | market mispricing | refinancing risk control | information confidence | shadow total | intended route |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| `035890` | 10 | 9 | 8 | 9 | 9 | 8 | 6 | 59 | Stage2-Guarded / Yellow after PF-liquidity evidence repair |
| `013580` | 9 | 8 | 7 | 10 | 8 | 7 | 6 | 55 | Stage2-Guarded until order/PF bridge repaired |
| `002990` | 3 | 3 | 3 | 4 | 3 | 2 | 4 | 22 | blocked Stage2 / 4B-4C high-MAE watch |

### Current calibrated profile stress test

The current calibrated profile already blocks pure price-only blowoff.  
The remaining C30 issue is more specific: **a construction balance-sheet repair candidate can be legitimate only if MAE stays contained and the credit bridge can later be repaired.**

```text
C30 contained repair path:
  regional construction/PF relief
  + 30D/90D MAE is contained
  + source evidence can be repaired for PF, receivables, refinancing, and working capital
  => Stage2-Guarded first; Yellow only after evidence repair

C30 slow-fade false-positive path:
  weak relief entry
  + MFE_30D < +5%
  + MAE_90D <= -20% or MAE_180D <= -30%
  + no repaired liquidity/PF evidence
  => block Stage2 and route to local 4B/4C watch
```

`035890` and `013580` prevent overblocking.  
`002990` shows why C30 needs a slow-fade detector, not only a crash detector. A construction stock can fail by dripping lower through the maturity wall, not only by breaking in one day.

---

## 9. Aggregate metrics

```json
{
  "row_type": "aggregate",
  "research_id": "R10L73_C30_REGIONAL_PF_ROUTER",
  "round": "R10",
  "loop": 73,
  "large_sector_id": "L9_CONSTRUCTION_REALESTATE_HOUSING",
  "canonical_archetype_id": "C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK",
  "fine_archetype_id": "REGIONAL_CONSTRUCTION_PF_LIQUIDITY_REPAIR_AND_SLOW_FADE_ROUTER",
  "case_count": 3,
  "calibration_usable_case_count": 3,
  "positive_guarded_case_count": 2,
  "counterexample_count": 1,
  "new_symbol_count": 3,
  "source_proxy_only_count": 3,
  "evidence_url_pending_count": 3,
  "avg_mfe_30d_pct": 7.01,
  "avg_mae_30d_pct": -4.53,
  "avg_mfe_90d_pct": 10.77,
  "avg_mae_90d_pct": -10.19,
  "avg_mfe_180d_pct": 10.77,
  "avg_mae_180d_pct": -15.11,
  "max_mfe_180d_pct": 18.71,
  "worst_mae_180d_pct": -32.06
}
```

---

## 10. 4B proximity split

```json
{
  "row_type": "4b_split",
  "research_id": "R10L73_C30_REGIONAL_PF_ROUTER",
  "stage2_guarded_or_yellow_candidate": [
    {
      "symbol": "035890",
      "reason": "30D/90D/180D MAE stayed contained; requires URL-repaired PF/liquidity/working-capital bridge before Yellow or Green"
    },
    {
      "symbol": "013580",
      "reason": "regional contractor path had moderate MFE and sub-10% 180D MAE; still source-proxy-only until order/backlog and PF evidence are repaired"
    }
  ],
  "blocked_stage2_or_4b_4c_watch": [
    {
      "symbol": "002990",
      "reason": "MFE_30D was only +0.53%, while MAE_90D reached -22.61% and MAE_180D reached -32.06%"
    }
  ],
  "full_4b_or_green_requires_non_price_evidence": [
    "PF guarantee exposure reduction",
    "refinancing / maturity wall repair",
    "receivables and working-capital repair",
    "unbilled construction revenue / cost-overrun control",
    "unsold inventory evidence",
    "cash-flow and covenant headroom"
  ]
}
```

---

## 11. Shadow rule candidate

```yaml
row_type: canonical_archetype_rule_candidate
canonical_archetype_id: C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK
fine_archetype_id: REGIONAL_CONSTRUCTION_PF_LIQUIDITY_REPAIR_AND_SLOW_FADE_ROUTER
rule_name: C30_regional_pf_repair_and_slow_fade_router
production_scoring_changed: false
shadow_weight_only: true
```

### Proposed routing logic

```text
For C30 construction PF / balance-sheet break cases:

Tier A: contained-MAE regional repair candidate
  Conditions:
    - regional construction/PF or low-PBR contractor relief exists
    - 30D/90D MAE remains contained
    - non-price evidence can be URL-repaired for PF exposure, refinancing, receivables, and working capital
  Routing:
    - Stage2-Actionable-Guarded allowed
    - Stage3-Yellow only after evidence repair
    - Green only after liquidity and balance-sheet repair are verified

Tier B: source-proxy-only construction relief
  Conditions:
    - price path is constructive but evidence_url_pending or source_proxy_only remains true
  Routing:
    - Stage2-Guarded at most
    - no Green
    - no production positive weight promotion

Tier C: weak-relief slow fade
  Conditions:
    - MFE_30D < +5%
    - MAE_90D <= -20% or MAE_180D <= -30%
    - no repaired liquidity/PF evidence
  Routing:
    - block Stage2
    - local 4B/high-MAE watch or 4C watch
    - count as false-positive counterexample
```

### Suggested shadow delta

```json
{
  "row_type": "shadow_weight",
  "axis": "c30_regional_pf_repair_and_slow_fade_router",
  "scope": "canonical_archetype_id:C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK",
  "proposal": {
    "source_proxy_only_green_allowed": false,
    "balance_sheet_liquidity_bridge_required_for_yellow_green": true,
    "contained_mae_regional_repair_stage2_guarded_allowed": true,
    "weak_mfe_threshold_30d_pct": 5.0,
    "slow_fade_high_mae_threshold_90d_pct": -20.0,
    "slow_fade_hard_failure_threshold_180d_pct": -30.0,
    "positive_weight_blocked_until_url_repair": true
  },
  "confidence": "medium_low_until_url_repair",
  "apply_now": false,
  "reason": "Two regional construction contained-MAE candidates and one weak-relief slow-fade counterexample show that C30 needs both a repair-candidate route and a slow-fade false-positive guard."
}
```

---

## 12. Residual contribution summary

```json
{
  "row_type": "residual_contribution",
  "research_id": "R10L73_C30_REGIONAL_PF_ROUTER",
  "large_sector_id": "L9_CONSTRUCTION_REALESTATE_HOUSING",
  "canonical_archetype_id": "C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK",
  "contribution": "Adds three non-top-covered C30 regional/mid-small construction cases and separates contained-MAE PF repair candidates from a weak-relief slow-fade false positive. C30 Green should require URL-repaired PF exposure, refinancing, receivables, working capital, inventory, cash-flow, and covenant evidence.",
  "positive_guarded_case_added": 2,
  "counterexample_case_added": 1,
  "new_symbol_count": 3,
  "data_quality_blocker": "All three non-price construction/PF triggers require URL-level repair before positive weight promotion.",
  "guardrail_added": "C30 weak-relief entries with MFE_30D < +5% and MAE_90D <= -20% or MAE_180D <= -30% should block Stage2 or route to 4B/4C high-MAE watch."
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
    035890: false
    013580: false
    002990: false
  evidence_url_pending:
    035890: true
    013580: true
    002990: true
  source_proxy_only:
    035890: true
    013580: true
    002990: true
```

Limitations:

```text
- Price path is validated against Stock-Web tradable OHLC rows.
- Non-price evidence is not URL-repaired in this run.
- Therefore this artifact is useful for C30 regional construction PF/liquidity residual shape and high-MAE guardrail design, but should not promote positive weights until filings, credit reports, IR, or disclosures verify PF exposure, refinancing, working capital, receivables, cash-flow, and unsold inventory repair.
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
2. Preserve R10 / loop 73 metadata.
3. Add the cases to C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK only if parser validation passes.
4. Treat all three non-price triggers as evidence_url_pending=true and source_proxy_only=true until URL-level evidence is repaired.
5. Do not use these rows for positive weight promotion until filings/IR/credit-report/disclosure data verifies PF exposure, refinancing, receivables, working capital, cash-flow, and unsold-inventory repair.
6. Add a shadow-only rule candidate named C30_regional_pf_repair_and_slow_fade_router.
7. Do not loosen Stage3-Green.
8. Add C30-specific guards:
   - source_proxy_only -> no Green
   - contained-MAE regional repair path -> Stage2-Guarded only until evidence repair
   - Stage3-Yellow/Green requires repaired balance-sheet and liquidity evidence
   - MFE_30D < +5% and MAE_90D <= -20% -> block Stage2 or local 4B/high-MAE watch
   - MAE_180D <= -30% without repaired evidence -> 4C watch or hard-fade counterexample
9. Keep production scoring unchanged unless later batch promotion logic independently marks this axis safe.
```

---

## 15. Next round state

```text
completed_round = R10
completed_loop = 73
next_round = R11
next_loop = 73
next_large_sector_hint = L10_POLICY_EVENT_CROSS_REDTEAM_MISC or L1 defense-linked policy event
```
