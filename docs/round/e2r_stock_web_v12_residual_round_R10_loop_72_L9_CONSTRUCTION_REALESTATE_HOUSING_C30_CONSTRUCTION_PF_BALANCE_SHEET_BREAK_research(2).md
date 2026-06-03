# E2R Stock-Web v12 Residual Research — R10 Loop 72

```yaml
research_session: post_calibrated_sector_archetype_residual_research
mode: historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12
completed_round: R10
completed_loop: 72
next_round: R11
next_loop: 72
large_sector_id: L9_CONSTRUCTION_REALESTATE_HOUSING
canonical_archetype_id: C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK
fine_archetype_id: MID_SMALL_CONSTRUCTION_PF_RELIEF_RALLY_AND_LIQUIDITY_BREAK_GUARD
output_file: e2r_stock_web_v12_residual_round_R10_loop_72_L9_CONSTRUCTION_REALESTATE_HOUSING_C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK_research.md
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
must_include_current_calibrated_profile_stress_test = true
must_output_every_usable_trigger_as_jsonl = true
```

### Round resolution

The immediately preceding completed artifact in this automation chain was:

```text
completed_round = R9
completed_loop = 72
large_sector_id = L3_BATTERY_EV_GREEN_MOBILITY
canonical_archetype_id = C14_EV_DEMAND_SLOWDOWN_4B_4C
```

Therefore:

```text
scheduled_round = R10
scheduled_loop = 72
```

R10 maps to:

```text
large_sector_id = L9_CONSTRUCTION_REALESTATE_HOUSING
```

This run selects:

```text
canonical_archetype_id = C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK
```

This is a valid R10/L9 pairing.

---

## 1. Why this R10/C30 run

The no-repeat ledger shows C30 is already heavily covered, but the top symbols are concentrated in major contractors or already-stressed high-repeat names:

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

This run avoids those top-covered names and adds three mid/small construction balance-sheet cases:

```text
004960 한신공영
005960 동부건설
003070 코오롱글로벌
```

The residual question is:

```text
Can C30 distinguish a genuine PF/balance-sheet repair path from a relief rally that only reprices “survival optionality” before liquidity, PF exposure, or working-capital stress reappears?
```

C30 is a credit-risk-first archetype. A useful signal is often not “the stock rose,” but whether the move survived the next credit/liquidity check. The same price candle can behave like a raft or a trapdoor depending on whether PF exposure, refinancing, receivables, working capital, and unsold inventory are actually being repaired.

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
| `004960` | 한신공영 | active_like / KOSPI | no 2024 overlap; old 1998~2002 candidates only | true |
| `005960` | 동부건설 | active_like / KOSPI | no 2024 overlap; latest listed candidate 2016-11-04 | true |
| `003070` | 코오롱글로벌 | active_like / KOSPI | no selected-window overlap; 2023-01-31 and 2025-12-11 outside test window | true |

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
The Stock-Web price path is fully validated, but company-level PF exposure, refinancing, short-term borrowings, receivables, unbilled construction revenue, unsold inventory, cash-flow repair, and covenant/liquidity evidence still require later URL repair through filings, credit reports, IR, or disclosure data before any production weight promotion.
```

C30 interpretation used here:

```text
C30 is not simply “construction stock moved.”
It asks whether the balance sheet is breaking, stabilizing, or being repaired:
- PF guarantee / contingent-liability exposure,
- refinancing and maturity wall,
- receivables and working capital,
- unsold housing inventory,
- impairment or cost overrun risk,
- and liquidity/covenant headroom.
```

Therefore this run is useful as a C30 residual-shape and guardrail file, not as a positive production patch.

---

## 4. No-repeat and novelty check

Hard duplicate key:

```text
canonical_archetype_id + symbol + trigger_type + entry_date
```

Targeted repository searches before writing:

```text
004960 + C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK -> no direct match found
005960 + C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK -> no direct match found
003070 + C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK -> no direct match found
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
| `R10L72_C30_004960_20240708` | `004960` 한신공영 | mid-construction PF relief rally with contained MAE | guarded positive / low-MAE repair candidate |
| `R10L72_C30_005960_20240715` | `005960` 동부건설 | low-liquidity PF/balance-sheet fade after relief attempt | counterexample / delayed 4C watch |
| `R10L72_C30_003070_20240627` | `003070` 코오롱글로벌 | construction credit relief squeeze with severe drawdown | high-MAE counterexample / 4B then 4C watch |

The intended residual:

```text
C30 should separate:
1. contained-MAE relief rallies that may deserve Stage2-Actionable-Guarded only after liquidity/PF evidence repair; and
2. relief rallies that rapidly produce 30D/90D MAE worse than -20%, which should route to 4B/4C watch regardless of short-term MFE.
```

---

## 6. Stock-Web OHLC and backtest

### 6.1 `004960` 한신공영 — contained-MAE PF relief candidate

Trigger:

```text
trigger_date = 2024-07-05
trigger_type = Stage2-Actionable-Guarded
trigger_family = mid_construction_pf_relief_contained_mae
entry_date = 2024-07-08
entry_price = 6400.0
entry_price_type = next_tradable_open
```

Relevant Stock-Web rows:

```csv
d,o,h,l,c,v,a,mc,s,m
2024-07-05,6430.0,6490.0,6430.0,6470.0,6893.0,44465190.0,74862441940.0,11570702,KOSPI
2024-07-08,6400.0,7030.0,6310.0,6390.0,256035.0,1698851760.0,73936785780.0,11570702,KOSPI
2024-07-30,7190.0,7560.0,6890.0,7340.0,255573.0,1871437550.0,84928952680.0,11570702,KOSPI
2024-07-31,7200.0,7560.0,7080.0,7360.0,196628.0,1448339040.0,85160366720.0,11570702,KOSPI
2024-08-05,6970.0,6970.0,6160.0,6300.0,108376.0,710455290.0,72895422600.0,11570702,KOSPI
2024-11-12,6670.0,7970.0,6550.0,7110.0,1509551.0,11130948860.0,82267691220.0,11570702,KOSPI
2024-12-09,6490.0,6600.0,6140.0,6140.0,91651.0,572498540.0,71044110280.0,11570702,KOSPI
```

Backtest:

| window | peak/high | peak date | trough/low | trough date | MFE | MAE |
|---|---:|---|---:|---|---:|---:|
| 30 calendar days | 7560 | 2024-07-30 | 6160 | 2024-08-05 | +18.13% | -3.75% |
| 90 calendar days | 7560 | 2024-07-30 | 6160 | 2024-08-05 | +18.13% | -3.75% |
| 180 calendar days | 7970 | 2024-11-12 | 6140 | 2024-12-09 | +24.53% | -4.06% |

Interpretation:

```text
004960 is the guarded positive case in this file.
The key is not huge upside; it is the contained drawdown profile. The price path suggests a possible survival/repair rally with manageable MAE.
However, because PF/liquidity evidence is still URL-pending, the correct route is Stage2-Actionable-Guarded / Yellow candidate only after balance-sheet evidence repair, not Green.
```

### 6.2 `005960` 동부건설 — low-liquidity PF/balance-sheet fade after relief attempt

Trigger:

```text
trigger_date = 2024-07-12
trigger_type = Stage2-FalsePositive-Candidate
trigger_family = construction_pf_relief_attempt_delayed_liquidity_fade
entry_date = 2024-07-15
entry_price = 4800.0
entry_price_type = next_tradable_open
```

Relevant Stock-Web rows:

```csv
d,o,h,l,c,v,a,mc,s,m
2024-07-12,4800.0,4840.0,4770.0,4800.0,30157.0,145075030.0,110142456000.0,22946345,KOSPI
2024-07-15,4800.0,4900.0,4800.0,4895.0,41762.0,203730395.0,112322358775.0,22946345,KOSPI
2024-07-31,4930.0,4985.0,4925.0,4950.0,38671.0,191866010.0,113584407750.0,22946345,KOSPI
2024-08-01,4975.0,4980.0,4950.0,4960.0,10301.0,51153475.0,113813871200.0,22946345,KOSPI
2024-08-05,4840.0,4845.0,4365.0,4435.0,61091.0,281950580.0,101767040075.0,22946345,KOSPI
2024-10-11,4230.0,4270.0,4185.0,4190.0,20943.0,88000000.0,96145185550.0,22946345,KOSPI
2024-11-13,3915.0,3965.0,3750.0,3775.0,40027.0,154157055.0,86622452375.0,22946345,KOSPI
2024-12-09,3700.0,3710.0,3570.0,3580.0,45054.0,163866975.0,82147915100.0,22946345,KOSPI
```

Backtest:

| window | peak/high | peak date | trough/low | trough date | MFE | MAE |
|---|---:|---|---:|---|---:|---:|
| 30 calendar days | 4985 | 2024-08-01 | 4365 | 2024-08-05 | +3.85% | -9.06% |
| 90 calendar days | 4985 | 2024-08-01 | 4185 | 2024-10-11 | +3.85% | -12.81% |
| 180 calendar days | 4985 | 2024-08-01 | 3570 | 2024-12-09 | +3.85% | -25.63% |

Interpretation:

```text
005960 is the slow-fade C30 counterexample.
The initial 30D path did not collapse immediately, but it never produced meaningful MFE and the 180D path crossed -25% MAE.
This should not be Stage2/Green. It belongs in 4B/high-MAE watch or 4C watch until liquidity and PF exposure repair is verified.
```

### 6.3 `003070` 코오롱글로벌 — credit relief squeeze with severe drawdown

Trigger:

```text
trigger_date = 2024-06-26
trigger_type = 4B-local-watch
trigger_family = construction_credit_relief_squeeze_high_mae
entry_date = 2024-06-27
entry_price = 14150.0
entry_price_type = next_tradable_open_after_squeeze
```

Relevant Stock-Web rows:

```csv
d,o,h,l,c,v,a,mc,s,m
2024-06-26,13810.0,14500.0,13220.0,13630.0,529069.0,7320671250.0,258052878190.0,18932713,KOSPI
2024-06-27,14150.0,15200.0,13600.0,13630.0,2062450.0,30126741120.0,258052878190.0,18932713,KOSPI
2024-07-03,12840.0,12900.0,11680.0,11730.0,297984.0,3593070830.0,222080723490.0,18932713,KOSPI
2024-07-12,11550.0,13640.0,11230.0,11620.0,1630186.0,20711709200.0,219998125060.0,18932713,KOSPI
2024-07-25,10310.0,10370.0,10010.0,10320.0,129417.0,1320545600.0,195385598160.0,18932713,KOSPI
2024-08-05,9610.0,9620.0,8500.0,8800.0,124324.0,1113766920.0,166607874400.0,18932713,KOSPI
2024-11-12,9100.0,11970.0,8770.0,10850.0,2751981.0,30735571850.0,205419936050.0,18932713,KOSPI
2024-12-09,8550.0,8560.0,7920.0,7960.0,100042.0,808168200.0,150704395480.0,18932713,KOSPI
```

Backtest:

| window | peak/high | peak date | trough/low | trough date | MFE | MAE |
|---|---:|---|---:|---|---:|---:|
| 30 calendar days | 15200 | 2024-06-27 | 10010 | 2024-07-25 | +7.42% | -29.26% |
| 90 calendar days | 15200 | 2024-06-27 | 8500 | 2024-08-05 | +7.42% | -39.93% |
| 180 calendar days | 15200 | 2024-06-27 | 7920 | 2024-12-09 | +7.42% | -44.03% |

Interpretation:

```text
003070 is the clean high-MAE C30 counterexample.
The price already carried a relief-squeeze shape at entry, but remaining upside was small and drawdown arrived quickly.
This is not Stage2. It should route to local 4B / high-MAE watch and then 4C watch unless hard balance-sheet repair evidence appears.
```

---

## 7. Machine-readable trigger JSONL

```jsonl
{"row_type":"trigger","research_id":"R10L72_C30_PF_BALANCE_SHEET_RELIEF_GUARD","round":"R10","loop":72,"large_sector_id":"L9_CONSTRUCTION_REALESTATE_HOUSING","canonical_archetype_id":"C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK","fine_archetype_id":"MID_SMALL_CONSTRUCTION_PF_RELIEF_RALLY_AND_LIQUIDITY_BREAK_GUARD","symbol":"004960","name":"한신공영","trigger_type":"Stage2-Actionable-Guarded","trigger_family":"mid_construction_pf_relief_contained_mae","trigger_date":"2024-07-05","entry_date":"2024-07-08","entry_price":6400.0,"entry_price_type":"next_tradable_open","price_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","mfe_30d_pct":18.13,"mae_30d_pct":-3.75,"mfe_90d_pct":18.13,"mae_90d_pct":-3.75,"mfe_180d_pct":24.53,"mae_180d_pct":-4.06,"peak_price_180d":7970.0,"peak_date_180d":"2024-11-12","trough_price_180d":6140.0,"trough_date_180d":"2024-12-09","calibration_usable":true,"case_polarity":"positive_guarded","evidence_url_pending":true,"source_proxy_only":true,"non_price_evidence_strength":"medium_pending_url_repair","price_only_blowoff":false,"expected_stage_current_profile":"Stage2_Actionable_Guarded_to_Yellow_if_pf_liquidity_repair_verified","residual_error_type":"contained_mae_relief_rally_requires_balance_sheet_repair_evidence_before_green"}
{"row_type":"trigger","research_id":"R10L72_C30_PF_BALANCE_SHEET_RELIEF_GUARD","round":"R10","loop":72,"large_sector_id":"L9_CONSTRUCTION_REALESTATE_HOUSING","canonical_archetype_id":"C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK","fine_archetype_id":"MID_SMALL_CONSTRUCTION_PF_RELIEF_RALLY_AND_LIQUIDITY_BREAK_GUARD","symbol":"005960","name":"동부건설","trigger_type":"Stage2-FalsePositive-Candidate","trigger_family":"construction_pf_relief_attempt_delayed_liquidity_fade","trigger_date":"2024-07-12","entry_date":"2024-07-15","entry_price":4800.0,"entry_price_type":"next_tradable_open","price_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","mfe_30d_pct":3.85,"mae_30d_pct":-9.06,"mfe_90d_pct":3.85,"mae_90d_pct":-12.81,"mfe_180d_pct":3.85,"mae_180d_pct":-25.63,"peak_price_180d":4985.0,"peak_date_180d":"2024-08-01","trough_price_180d":3570.0,"trough_date_180d":"2024-12-09","calibration_usable":true,"case_polarity":"counterexample_delayed_high_mae","evidence_url_pending":true,"source_proxy_only":true,"non_price_evidence_strength":"low_pending_url_repair","price_only_blowoff":false,"expected_stage_current_profile":"blocked_stage2_or_4B_high_MAE_watch","residual_error_type":"low_mfe_delayed_pf_liquidity_fade_should_not_stage2_green"}
{"row_type":"trigger","research_id":"R10L72_C30_PF_BALANCE_SHEET_RELIEF_GUARD","round":"R10","loop":72,"large_sector_id":"L9_CONSTRUCTION_REALESTATE_HOUSING","canonical_archetype_id":"C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK","fine_archetype_id":"MID_SMALL_CONSTRUCTION_PF_RELIEF_RALLY_AND_LIQUIDITY_BREAK_GUARD","symbol":"003070","name":"코오롱글로벌","trigger_type":"4B-local-watch","trigger_family":"construction_credit_relief_squeeze_high_mae","trigger_date":"2024-06-26","entry_date":"2024-06-27","entry_price":14150.0,"entry_price_type":"next_tradable_open_after_squeeze","price_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","mfe_30d_pct":7.42,"mae_30d_pct":-29.26,"mfe_90d_pct":7.42,"mae_90d_pct":-39.93,"mfe_180d_pct":7.42,"mae_180d_pct":-44.03,"peak_price_180d":15200.0,"peak_date_180d":"2024-06-27","trough_price_180d":7920.0,"trough_date_180d":"2024-12-09","calibration_usable":true,"case_polarity":"counterexample_high_mae","evidence_url_pending":true,"source_proxy_only":true,"non_price_evidence_strength":"low_pending_url_repair","price_only_blowoff":false,"expected_stage_current_profile":"4B_local_watch_or_4C_watch_until_balance_sheet_repair_verified","residual_error_type":"relief_squeeze_small_mfe_extreme_mae_should_route_to_4b_4c"}
```

---

## 8. Score simulation and raw component breakdown

This is shadow-only and does not change production scoring.

| symbol | liquidity/PF repair | balance-sheet visibility | working-capital quality | market mispricing | valuation rerating | refinancing risk control | information confidence | shadow total | intended route |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| `004960` | 9 | 8 | 7 | 9 | 8 | 8 | 6 | 55 | Stage2-Guarded / Yellow only after PF-liquidity repair evidence |
| `005960` | 4 | 4 | 4 | 5 | 4 | 3 | 4 | 28 | blocked Stage2 / delayed high-MAE watch |
| `003070` | 5 | 4 | 3 | 8 | 6 | 3 | 4 | 33 | local 4B then 4C watch; no Green |

### Current calibrated profile stress test

The current calibrated profile already blocks price-only blowoff.  
The remaining C30 risk is more specific: **a construction credit-relief rally can contain real credit optionality and still fail if balance-sheet repair is not verified.**

```text
C30 guarded repair mode:
  construction/PF relief rally
  + contained 30D/90D MAE
  + source evidence repaired for liquidity, PF guarantees, refinancing, receivables, and unsold inventory
  => Stage2-Actionable-Guarded; Yellow only after repair evidence

C30 false repair mode:
  relief rally or credit squeeze
  + MFE is small or short-lived
  + 30D/90D MAE worse than -20% or 180D MAE worse than -25%
  + no repaired balance-sheet evidence
  => blocked Stage2, local 4B, high-MAE watch, or 4C watch
```

`004960` behaves like a possible raft because the drawdown profile remained contained.  
`005960` behaves like a slow leak.  
`003070` behaves like a trapdoor: the event move was already spent, and the follow-through immediately became a credit-risk drawdown.

---

## 9. Aggregate metrics

```json
{
  "row_type": "aggregate",
  "research_id": "R10L72_C30_PF_BALANCE_SHEET_RELIEF_GUARD",
  "round": "R10",
  "loop": 72,
  "large_sector_id": "L9_CONSTRUCTION_REALESTATE_HOUSING",
  "canonical_archetype_id": "C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK",
  "fine_archetype_id": "MID_SMALL_CONSTRUCTION_PF_RELIEF_RALLY_AND_LIQUIDITY_BREAK_GUARD",
  "case_count": 3,
  "calibration_usable_case_count": 3,
  "positive_guarded_case_count": 1,
  "counterexample_count": 2,
  "new_symbol_count": 3,
  "source_proxy_only_count": 3,
  "evidence_url_pending_count": 3,
  "avg_mfe_30d_pct": 9.80,
  "avg_mae_30d_pct": -14.02,
  "avg_mfe_90d_pct": 9.80,
  "avg_mae_90d_pct": -18.83,
  "avg_mfe_180d_pct": 11.93,
  "avg_mae_180d_pct": -24.57,
  "worst_mae_180d_pct": -44.03
}
```

---

## 10. Shadow rule candidate

```yaml
row_type: canonical_archetype_rule_candidate
canonical_archetype_id: C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK
fine_archetype_id: MID_SMALL_CONSTRUCTION_PF_RELIEF_RALLY_AND_LIQUIDITY_BREAK_GUARD
rule_name: C30_pf_relief_rally_balance_sheet_repair_and_high_mae_router
production_scoring_changed: false
shadow_weight_only: true
```

### Proposed routing logic

```text
For C30 construction PF / balance-sheet break cases:

Tier A: verified PF/liquidity repair
  Conditions:
    - PF guarantee, refinancing, maturity wall, receivables, working capital, and unsold inventory evidence is URL-repaired
    - 30D/90D MAE remains contained
    - MFE is not just one-day relief squeeze
  Routing:
    - Stage2-Actionable-Guarded allowed
    - Stage3-Yellow allowed only after evidence repair
    - Green remains blocked until cash-flow and balance-sheet repair is verified

Tier B: source-proxy-only relief rally
  Conditions:
    - price bounces on construction/PF relief sentiment
    - evidence_url_pending or source_proxy_only remains true
    - balance-sheet repair is not verified
  Routing:
    - Stage2-Guarded at most
    - no Green
    - no production positive weight promotion

Tier C: high-MAE credit squeeze / false repair
  Conditions:
    - 30D or 90D MAE <= -20%, or 180D MAE <= -25%
    - no repaired liquidity/PF evidence
    - MFE is small or short-lived
  Routing:
    - local 4B/high-MAE watch
    - 4C watch if drawdown persists
    - count as counterexample
```

### Suggested shadow delta

```json
{
  "row_type": "shadow_weight",
  "axis": "c30_pf_relief_rally_balance_sheet_repair_and_high_mae_router",
  "scope": "canonical_archetype_id:C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK",
  "proposal": {
    "source_proxy_only_green_allowed": false,
    "balance_sheet_repair_required_for_yellow_green": true,
    "stage2_guarded_allowed_when_90d_mae_contained": true,
    "high_mae_watch_threshold_30d_or_90d_pct": -20.0,
    "high_mae_watch_threshold_180d_pct": -25.0,
    "positive_weight_blocked_until_url_repair": true
  },
  "confidence": "medium_low_until_url_repair",
  "apply_now": false,
  "reason": "Three new C30 mid/small construction cases show one contained-MAE relief path and two false repair paths. Because non-price evidence remains URL-pending, the result is a guardrail candidate rather than a positive promotion candidate."
}
```

---

## 11. Residual contribution summary

```json
{
  "row_type": "residual_contribution",
  "research_id": "R10L72_C30_PF_BALANCE_SHEET_RELIEF_GUARD",
  "large_sector_id": "L9_CONSTRUCTION_REALESTATE_HOUSING",
  "canonical_archetype_id": "C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK",
  "contribution": "Adds three less-repeated C30 mid/small construction cases and separates contained-MAE PF relief from low-MFE/high-MAE false repair paths. C30 should require URL-repaired liquidity, PF exposure, refinancing, receivables, working-capital, and unsold-inventory evidence before allowing Yellow/Green.",
  "positive_case_added": 1,
  "counterexample_case_added": 2,
  "new_symbol_count": 3,
  "data_quality_blocker": "All three non-price construction/PF triggers require URL-level repair before positive weight promotion.",
  "guardrail_added": "C30 Green is blocked when source_proxy_only=true; 30D/90D MAE <= -20% or 180D MAE <= -25% without repaired balance-sheet evidence should route to high-MAE watch or 4C watch."
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
    004960: false
    005960: false
    003070: false
  evidence_url_pending:
    004960: true
    005960: true
    003070: true
  source_proxy_only:
    004960: true
    005960: true
    003070: true
```

Limitations:

```text
- Price path is validated against Stock-Web tradable OHLC rows.
- Non-price evidence is not URL-repaired in this run.
- Therefore this artifact is useful for C30 PF-relief/high-MAE guardrail design, but should not promote positive weights until filings, credit reports, IR, or disclosures verify PF exposure, refinancing, working capital, cash-flow, receivables, and unsold inventory repair.
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
2. Preserve R10 / loop 72 metadata.
3. Add the cases to C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK only if parser validation passes.
4. Treat all three non-price triggers as evidence_url_pending=true and source_proxy_only=true until URL-level evidence is repaired.
5. Do not use these rows for positive weight promotion until filings/IR/credit-report/disclosure data verifies PF exposure, refinancing, receivables, working capital, cash-flow, and unsold-inventory repair.
6. Add a shadow-only rule candidate named C30_pf_relief_rally_balance_sheet_repair_and_high_mae_router.
7. Do not loosen Stage3-Green.
8. Add C30-specific guards:
   - source_proxy_only -> no Green
   - Stage3-Yellow/Green requires repaired balance-sheet and liquidity evidence
   - 30D/90D MAE <= -20% or 180D MAE <= -25% without repaired evidence -> local 4B/high-MAE watch or 4C watch
   - short-lived relief rally does not override PF/balance-sheet risk
9. Keep production scoring unchanged unless later batch promotion logic independently marks this axis safe.
```

---

## 14. Next round state

```text
completed_round = R10
completed_loop = 72
next_round = R11
next_loop = 72
next_large_sector_hint = L10_POLICY_EVENT_CROSS_REDTEAM_MISC or L1 defense-linked policy event
```
