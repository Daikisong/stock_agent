# E2R Stock-Web v12 Residual Research — R1 Loop 73

```yaml
research_session: post_calibrated_sector_archetype_residual_research
mode: historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12
completed_round: R1
completed_loop: 73
next_round: R2
next_loop: 73
large_sector_id: L1_INDUSTRIALS_INFRA_DEFENSE_GRID
canonical_archetype_id: C02_POWER_GRID_DATACENTER_CAPEX
fine_archetype_id: SECOND_TIER_POWER_EQUIPMENT_GRID_CAPEX_AND_DATACENTER_RELIEF_RALLY_GUARD
output_file: e2r_stock_web_v12_residual_round_R1_loop_73_L1_INDUSTRIALS_INFRA_DEFENSE_GRID_C02_POWER_GRID_DATACENTER_CAPEX_research.md
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
completed_round = R13
completed_loop  = 72
large_sector_id = L10_POLICY_EVENT_CROSS_REDTEAM_MISC
canonical_archetype_id = R13_CROSS_ARCHETYPE_STAGE2_FALSE_POSITIVE_REVIEW
```

Therefore:

```text
scheduled_round = R1
scheduled_loop  = 73
```

R1 maps to:

```text
large_sector_id = L1_INDUSTRIALS_INFRA_DEFENSE_GRID
```

This run selects:

```text
canonical_archetype_id = C02_POWER_GRID_DATACENTER_CAPEX
fine_archetype_id = SECOND_TIER_POWER_EQUIPMENT_GRID_CAPEX_AND_DATACENTER_RELIEF_RALLY_GUARD
```

This is a valid R1/L1 pairing.

---

## 1. Why this R1/C02 run

The no-repeat ledger shows C02 is already meaningfully covered, but concentrated in a small group of primary grid-capex names:

```text
C02_POWER_GRID_DATACENTER_CAPEX:
  rows: 49
  symbols: 8
  date_range: 2023-01-27~2024-07-24
  good/bad S2: 24/1
  4B/4C: 15/0
  URL/proxy: 4/4
  top covered symbols: 010120(16), 267260(12), 298040(7), 006340(4), 103590(4), UNKNOWN_SYMBOL(3)
```

This run deliberately avoids the dominant large-cap / already-covered transformer winners and tests second-tier electrical equipment names:

```text
033100 제룡전기
199820 제일일렉트릭
017040 광명전기
```

Research question:

```text
Can C02 separate true grid/datacenter capex bottleneck winners from second-tier power-equipment/theme rallies that look like Stage2 but later carry high MAE?
```

The mechanism is like a power grid itself. The primary transformer bottleneck is the substation transformer: if demand is real and orders are visible, current flows cleanly. Second-tier electrical equipment names can also light up, but some are more like a loose wire: the first spark is visible, while order quality and margin conversion may not carry the load.

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
| `033100` | 제룡전기 | active_like / KOSDAQ | no 2024 overlap; latest listed candidate 2014-11-06 | true |
| `199820` | 제일일렉트릭 | active_like / KOSDAQ | 2024-05-21 and 2024-06-11 candidates are before the selected 2024-06-27 entry; no forward-window overlap | true after 2024-06-11 |
| `017040` | 광명전기 | active_like / KOSPI | no 2024 overlap; old 2000/2001 candidates only | true |

Profile caveat:

```text
Stock-Web OHLC is raw/unadjusted marcap data. These cases are calibration-safe for the selected windows because no listed corporate-action candidate overlaps each entry~D+180 test window.
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
The Stock-Web price path is fully validated, but company-level transformer/electrical-equipment order backlog, export customer, datacenter/grid capex linkage, margin conversion, and lead-time/pricing evidence still require later URL repair through filings, IR decks, export data, contracts, or reports before any production weight promotion.
```

C02 interpretation used here:

```text
C02 is not simply “electric equipment stock rose.”
It asks whether power-grid/datacenter capex creates durable non-price evidence:
- backlog / order visibility,
- transformer or electrical-equipment bottleneck,
- export and customer quality,
- margin conversion,
- and low-MAE follow-through.
```

This file is useful as residual research and guardrail design, but should not be promoted as positive weight until URL-level evidence is repaired.

---

## 4. No-repeat and novelty check

Hard duplicate key:

```text
canonical_archetype_id + symbol + trigger_type + entry_date
```

Targeted repository searches before writing:

```text
033100 + C02_POWER_GRID_DATACENTER_CAPEX -> no direct match found
199820 + C02_POWER_GRID_DATACENTER_CAPEX -> no direct match found
017040 + C02_POWER_GRID_DATACENTER_CAPEX -> no direct match found
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
| `R1L73_C02_033100_20240304` | `033100` 제룡전기 | transformer/grid capex bottleneck breakout | clean positive / low-MAE anchor |
| `R1L73_C02_199820_20240627` | `199820` 제일일렉트릭 | post-adjustment second-tier electrical equipment relief rally | counterexample / high-MAE guard |
| `R1L73_C02_017040_20240507` | `017040` 광명전기 | low-price electrical equipment theme spike | counterexample / 4B-to-4C guard |

The intended residual:

```text
C02 should separate:
1. true bottleneck transformer/grid-capex winners with low MAE and persistent MFE;
2. second-tier electrical-equipment relays where initial MFE is real but 90D/180D MAE becomes severe;
3. low-price theme spikes where price moves before durable order/margin evidence.
```

---

## 6. Stock-Web OHLC and backtest

### 6.1 `033100` 제룡전기 — clean grid-capex bottleneck positive

Trigger:

```text
trigger_date = 2024-03-01
trigger_type = Stage2-Actionable
trigger_family = transformer_grid_capex_bottleneck_breakout
entry_date = 2024-03-04
entry_price = 21750.0
entry_price_type = next_tradable_open
```

Relevant Stock-Web rows:

```csv
d,o,h,l,c,v,a,mc,s,m
2024-03-04,21750.0,27200.0,21750.0,27200.0,5746788.0,149308673550.0,436897524800.0,16062409,KOSDAQ
2024-03-08,30300.0,33850.0,30050.0,32550.0,3911304.0,125532485250.0,522831412950.0,16062409,KOSDAQ
2024-03-29,41300.0,49450.0,40200.0,43700.0,9717004.0,438128627800.0,701927273300.0,16062409,KOSDAQ
2024-04-03,47800.0,51300.0,46250.0,47950.0,2146074.0,105296393500.0,770192511550.0,16062409,KOSDAQ
2024-05-13,75800.0,80700.0,68300.0,71500.0,3196414.0,236886628500.0,1148462243500.0,16062409,KOSDAQ
2024-06-27,79400.0,91800.0,78100.0,90900.0,2743612.0,239039356600.0,1460072978100.0,16062409,KOSDAQ
2024-07-11,98000.0,100700.0,94300.0,95900.0,810617.0,79154020100.0,1540385023100.0,16062409,KOSDAQ
2024-08-05,65700.0,68300.0,57700.0,62400.0,932399.0,59653534700.0,1002294321600.0,16062409,KOSDAQ
```

Backtest:

| window | peak/high | peak date | trough/low | trough date | MFE | MAE |
|---|---:|---|---:|---|---:|---:|
| 30 calendar days | 51300 | 2024-04-03 | 21750 | 2024-03-04 | +135.86% | +0.00% |
| 90 calendar days | 80700 | 2024-05-13 | 21750 | 2024-03-04 | +271.03% | +0.00% |
| 180 calendar days | 100700 | 2024-07-11 | 21750 | 2024-03-04 | +362.99% | +0.00% |

Interpretation:

```text
033100 is the clean positive anchor. The entry carried immediate, persistent, low-MAE follow-through.
This is the C02 pattern the model should reward once non-price evidence is URL-repaired:
bottleneck exposure + sustained MFE + no meaningful early drawdown.
```

### 6.2 `199820` 제일일렉트릭 — second-tier electrical equipment relief rally with high-MAE risk

Trigger:

```text
trigger_date = 2024-06-26
trigger_type = Stage2-Actionable-Guarded
trigger_family = post_adjustment_second_tier_electrical_equipment_relief_rally
entry_date = 2024-06-27
entry_price = 8740.0
entry_price_type = next_tradable_open_after_corporate_action_window
```

Relevant Stock-Web rows:

```csv
d,o,h,l,c,v,a,mc,s,m
2024-06-26,8680.0,9140.0,8600.0,8740.0,783582.0,6953087900.0,194202800000.0,22220000,KOSDAQ
2024-06-27,8740.0,9880.0,8510.0,9250.0,5145573.0,49012737610.0,205535000000.0,22220000,KOSDAQ
2024-06-28,9400.0,10840.0,9350.0,10050.0,11875241.0,123079928770.0,223311000000.0,22220000,KOSDAQ
2024-07-26,7650.0,7810.0,7590.0,7620.0,265728.0,2039825700.0,169316400000.0,22220000,KOSDAQ
2024-08-05,6710.0,6960.0,5700.0,6010.0,590962.0,3739788200.0,133542200000.0,22220000,KOSDAQ
2024-09-27,10820.0,11000.0,9670.0,9700.0,5622592.0,58722445340.0,215534000000.0,22220000,KOSDAQ
2024-11-14,10190.0,11940.0,10180.0,11220.0,15914628.0,181068118750.0,249308400000.0,22220000,KOSDAQ
2024-12-09,8040.0,8210.0,7840.0,7860.0,580139.0,4618139280.0,174649200000.0,22220000,KOSDAQ
```

Backtest:

| window | peak/high | peak date | trough/low | trough date | MFE | MAE |
|---|---:|---|---:|---|---:|---:|
| 30 calendar days | 10840 | 2024-06-28 | 7590 | 2024-07-26 | +24.03% | -13.16% |
| 90 calendar days | 10840 | 2024-06-28 | 5700 | 2024-08-05 | +24.03% | -34.78% |
| 180 calendar days | 11940 | 2024-11-14 | 5700 | 2024-08-05 | +36.61% | -34.78% |

Interpretation:

```text
199820 is not a clean positive even though it produced useful MFE.
The 90D/180D MAE was severe, and the later MFE required enduring a deep drawdown first.
This should be Stage2-Actionable-Guarded or local 4B/high-MAE watch until backlog/customer/order evidence is repaired.
```

### 6.3 `017040` 광명전기 — low-price electrical equipment theme spike, then 4B/4C drawdown

Trigger:

```text
trigger_date = 2024-05-03
trigger_type = 4B-local-watch
trigger_family = low_price_power_equipment_theme_spike_without_order_bridge
entry_date = 2024-05-07
entry_price = 2685.0
entry_price_type = next_tradable_open
```

Relevant Stock-Web rows:

```csv
d,o,h,l,c,v,a,mc,s,m
2024-05-03,2735.0,2735.0,2655.0,2660.0,1421432.0,3814490845.0,115278055900.0,43337615,KOSPI
2024-05-07,2685.0,3270.0,2670.0,3185.0,43351466.0,133598176775.0,138030303775.0,43337615,KOSPI
2024-05-08,3090.0,3320.0,3020.0,3060.0,15800256.0,49840216860.0,132613101900.0,43337615,KOSPI
2024-05-13,2495.0,3030.0,2400.0,2670.0,26914087.0,73195203245.0,115711432050.0,43337615,KOSPI
2024-06-05,2240.0,2255.0,2185.0,2205.0,640390.0,1417008300.0,95559441075.0,43337615,KOSPI
2024-08-05,1935.0,1999.0,1614.0,1744.0,1349197.0,2463892933.0,75580800560.0,43337615,KOSPI
2024-10-25,1452.0,1464.0,1390.0,1391.0,651453.0,925115812.0,60282622465.0,43337615,KOSPI
2024-10-31,1338.0,1415.0,1250.0,1368.0,1534948.0,2041411136.0,59285857320.0,43337615,KOSPI
```

Backtest:

| window | peak/high | peak date | trough/low | trough date | MFE | MAE |
|---|---:|---|---:|---|---:|---:|
| 30 calendar days | 3320 | 2024-05-08 | 2185 | 2024-06-05 | +23.65% | -18.62% |
| 90 calendar days | 3320 | 2024-05-08 | 1614 | 2024-08-05 | +23.65% | -39.89% |
| 180 calendar days | 3320 | 2024-05-08 | 1250 | 2024-10-31 | +23.65% | -53.45% |

Interpretation:

```text
017040 is the clean counterexample. The first spark was bright, but the wire could not carry the load.
Without order/backlog/customer/margin bridge evidence, this should not be Stage2/Green.
It should route to 4B-local-watch and then 4C/high-MAE guard.
```

---

## 7. Machine-readable trigger JSONL

```jsonl
{"row_type":"trigger","research_id":"R1L73_C02_POWER_GRID_SECOND_TIER","round":"R1","loop":73,"large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C02_POWER_GRID_DATACENTER_CAPEX","fine_archetype_id":"SECOND_TIER_POWER_EQUIPMENT_GRID_CAPEX_AND_DATACENTER_RELIEF_RALLY_GUARD","symbol":"033100","name":"제룡전기","trigger_type":"Stage2-Actionable","trigger_family":"transformer_grid_capex_bottleneck_breakout","trigger_date":"2024-03-01","entry_date":"2024-03-04","entry_price":21750.0,"entry_price_type":"next_tradable_open","price_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","mfe_30d_pct":135.86,"mae_30d_pct":0.00,"mfe_90d_pct":271.03,"mae_90d_pct":0.00,"mfe_180d_pct":362.99,"mae_180d_pct":0.00,"peak_price_180d":100700.0,"peak_date_180d":"2024-07-11","trough_price_180d":21750.0,"trough_date_180d":"2024-03-04","calibration_usable":true,"case_polarity":"positive_anchor","evidence_url_pending":true,"source_proxy_only":true,"non_price_evidence_strength":"medium_pending_url_repair","price_only_blowoff":false,"expected_stage_current_profile":"Stage2-Actionable_to_Yellow_or_Green_after_order_margin_bridge_repaired","residual_error_type":"positive_anchor_requires_url_repaired_backlog_customer_margin_evidence_before_green"}
{"row_type":"trigger","research_id":"R1L73_C02_POWER_GRID_SECOND_TIER","round":"R1","loop":73,"large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C02_POWER_GRID_DATACENTER_CAPEX","fine_archetype_id":"SECOND_TIER_POWER_EQUIPMENT_GRID_CAPEX_AND_DATACENTER_RELIEF_RALLY_GUARD","symbol":"199820","name":"제일일렉트릭","trigger_type":"Stage2-Actionable-Guarded","trigger_family":"post_adjustment_second_tier_electrical_equipment_relief_rally","trigger_date":"2024-06-26","entry_date":"2024-06-27","entry_price":8740.0,"entry_price_type":"next_tradable_open_after_corporate_action_window","price_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","mfe_30d_pct":24.03,"mae_30d_pct":-13.16,"mfe_90d_pct":24.03,"mae_90d_pct":-34.78,"mfe_180d_pct":36.61,"mae_180d_pct":-34.78,"peak_price_180d":11940.0,"peak_date_180d":"2024-11-14","trough_price_180d":5700.0,"trough_date_180d":"2024-08-05","calibration_usable":true,"case_polarity":"counterexample_high_mae","evidence_url_pending":true,"source_proxy_only":true,"non_price_evidence_strength":"low_pending_url_repair","price_only_blowoff":false,"expected_stage_current_profile":"Stage2_Guarded_or_4B_high_MAE_watch_until_order_bridge_repaired","residual_error_type":"second_tier_grid_relief_rally_high_mae_without_verified_backlog_bridge"}
{"row_type":"trigger","research_id":"R1L73_C02_POWER_GRID_SECOND_TIER","round":"R1","loop":73,"large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C02_POWER_GRID_DATACENTER_CAPEX","fine_archetype_id":"SECOND_TIER_POWER_EQUIPMENT_GRID_CAPEX_AND_DATACENTER_RELIEF_RALLY_GUARD","symbol":"017040","name":"광명전기","trigger_type":"4B-local-watch","trigger_family":"low_price_power_equipment_theme_spike_without_order_bridge","trigger_date":"2024-05-03","entry_date":"2024-05-07","entry_price":2685.0,"entry_price_type":"next_tradable_open","price_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","mfe_30d_pct":23.65,"mae_30d_pct":-18.62,"mfe_90d_pct":23.65,"mae_90d_pct":-39.89,"mfe_180d_pct":23.65,"mae_180d_pct":-53.45,"peak_price_180d":3320.0,"peak_date_180d":"2024-05-08","trough_price_180d":1250.0,"trough_date_180d":"2024-10-31","calibration_usable":true,"case_polarity":"counterexample_theme_blowoff","evidence_url_pending":true,"source_proxy_only":true,"non_price_evidence_strength":"low_pending_url_repair","price_only_blowoff":true,"expected_stage_current_profile":"4B_local_watch_or_4C_high_MAE_guard","residual_error_type":"low_price_grid_theme_spike_low_mfe_extreme_mae_should_block_stage2_green"}
```

---

## 8. Score simulation and raw component breakdown

This is shadow-only and does not change production scoring.

| symbol | grid/datacenter relevance | order/backlog visibility | bottleneck/pricing quality | market mispricing | valuation rerating | capital allocation | information confidence | shadow total | intended route |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| `033100` | 17 | 14 | 17 | 15 | 18 | 5 | 7 | 93 | Stage2/Yellow; Green only after order/margin evidence repair |
| `199820` | 11 | 6 | 8 | 9 | 8 | 4 | 5 | 51 | Stage2-Guarded or high-MAE watch |
| `017040` | 8 | 3 | 5 | 8 | 6 | 3 | 4 | 37 | 4B-local-watch / 4C high-MAE guard |

### Current calibrated profile stress test

The current calibrated profile already blocks pure price-only blowoff.  
The remaining C02 problem is more nuanced:

```text
C02 clean bottleneck path:
  transformer/grid capex exposure
  + low MAE
  + persistent MFE
  + later repaired order/backlog/customer/margin evidence
  => Stage2-Actionable / Yellow, possible Green

C02 second-tier relief path:
  electrical-equipment exposure
  + initial MFE
  + evidence still source-proxy-only
  + 90D/180D MAE worse than -30%
  => Stage2-Guarded or 4B/high-MAE watch; no Green

C02 low-price theme path:
  power-equipment theme spike
  + no verified order bridge
  + 180D MAE worse than -50%
  => blocked Stage2 / 4B-to-4C guard
```

`033100` proves that C02 should not be overblocked.  
`199820` and `017040` show that second-tier power-equipment rallies need stricter order/margin validation than the primary transformer winners.

---

## 9. Aggregate metrics

```json
{
  "row_type": "aggregate",
  "research_id": "R1L73_C02_POWER_GRID_SECOND_TIER",
  "round": "R1",
  "loop": 73,
  "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID",
  "canonical_archetype_id": "C02_POWER_GRID_DATACENTER_CAPEX",
  "fine_archetype_id": "SECOND_TIER_POWER_EQUIPMENT_GRID_CAPEX_AND_DATACENTER_RELIEF_RALLY_GUARD",
  "case_count": 3,
  "calibration_usable_case_count": 3,
  "positive_anchor_count": 1,
  "counterexample_count": 2,
  "new_symbol_count": 3,
  "source_proxy_only_count": 3,
  "evidence_url_pending_count": 3,
  "avg_mfe_30d_pct": 61.18,
  "avg_mae_30d_pct": -10.59,
  "avg_mfe_90d_pct": 106.24,
  "avg_mae_90d_pct": -24.89,
  "avg_mfe_180d_pct": 141.08,
  "avg_mae_180d_pct": -29.41,
  "max_mfe_180d_pct": 362.99,
  "worst_mae_180d_pct": -53.45
}
```

---

## 10. 4B proximity split

```json
{
  "row_type": "4b_split",
  "research_id": "R1L73_C02_POWER_GRID_SECOND_TIER",
  "stage2_positive_or_yellow_candidate": [
    {
      "symbol": "033100",
      "reason": "persistent MFE and no early MAE; requires URL-repaired backlog/customer/margin evidence before Green"
    }
  ],
  "local_4b_watch": [
    {
      "symbol": "199820",
      "reason": "useful MFE, but 90D/180D MAE reached -34.78%; second-tier rally needs order bridge repair"
    },
    {
      "symbol": "017040",
      "reason": "theme spike followed by -53.45% 180D MAE; should route to 4B/4C watch"
    }
  ],
  "full_4b_or_green_requires_non_price_evidence": [
    "named grid/datacenter/customer order",
    "backlog conversion",
    "margin bridge",
    "pricing/lead-time bottleneck evidence",
    "repeat export/customer visibility"
  ]
}
```

---

## 11. Shadow rule candidate

```yaml
row_type: canonical_archetype_rule_candidate
canonical_archetype_id: C02_POWER_GRID_DATACENTER_CAPEX
fine_archetype_id: SECOND_TIER_POWER_EQUIPMENT_GRID_CAPEX_AND_DATACENTER_RELIEF_RALLY_GUARD
rule_name: C02_second_tier_grid_capex_order_bridge_and_high_mae_router
production_scoring_changed: false
shadow_weight_only: true
```

### Proposed routing logic

```text
For C02 power-grid / datacenter capex cases:

Tier A: verified transformer/grid bottleneck winner
  Conditions:
    - direct transformer/grid/datacenter capex exposure
    - company-level order, backlog, export customer, or margin bridge is URL-repaired
    - 30D/90D MAE is contained
    - MFE is persistent beyond one event candle
  Routing:
    - Stage2-Actionable allowed
    - Stage3-Yellow allowed after evidence repair
    - Green only after order/backlog/margin conversion is verified

Tier B: second-tier electrical equipment rally
  Conditions:
    - electrical-equipment exposure is plausible
    - evidence remains source_proxy_only
    - 90D or 180D MAE <= -30%
  Routing:
    - Stage2-Actionable-Guarded at most
    - no Green
    - local 4B/high-MAE watch until order bridge is repaired

Tier C: low-price power theme spike
  Conditions:
    - low-price / theme stock
    - no verified order/backlog bridge
    - 180D MAE <= -40%
  Routing:
    - block Stage2
    - local 4B-to-4C watch
    - count as counterexample
```

### Suggested shadow delta

```json
{
  "row_type": "shadow_weight",
  "axis": "c02_second_tier_grid_capex_order_bridge_and_high_mae_router",
  "scope": "canonical_archetype_id:C02_POWER_GRID_DATACENTER_CAPEX",
  "proposal": {
    "source_proxy_only_green_allowed": false,
    "grid_order_backlog_margin_bridge_required_for_green": true,
    "second_tier_equipment_stage2_cap": "guarded_only_until_url_repair",
    "second_tier_high_mae_watch_threshold_pct": -30.0,
    "low_price_theme_high_mae_block_stage2_threshold_pct": -40.0,
    "positive_weight_blocked_until_url_repair": true
  },
  "confidence": "medium_low_until_url_repair",
  "apply_now": false,
  "reason": "One clean bottleneck positive and two second-tier high-MAE cases show that C02 should reward persistent low-MAE transformer winners but require stricter order/backlog/margin evidence for second-tier electrical-equipment rallies."
}
```

---

## 12. Residual contribution summary

```json
{
  "row_type": "residual_contribution",
  "research_id": "R1L73_C02_POWER_GRID_SECOND_TIER",
  "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID",
  "canonical_archetype_id": "C02_POWER_GRID_DATACENTER_CAPEX",
  "contribution": "Adds three non-top-covered C02 power-grid/electrical-equipment cases and separates a clean transformer/grid-capex bottleneck path from second-tier electrical-equipment rallies that later suffer severe MAE. C02 Green should require URL-repaired order/backlog/customer/margin bridge, especially for second-tier or low-price theme names.",
  "positive_case_added": 1,
  "counterexample_case_added": 2,
  "new_symbol_count": 3,
  "data_quality_blocker": "All three non-price grid/datacenter capex triggers require URL-level repair before positive weight promotion.",
  "guardrail_added": "C02 source_proxy_only second-tier rallies with 90D/180D MAE worse than -30% should route to Stage2-Guarded or 4B/high-MAE watch; low-price theme names with 180D MAE worse than -40% should block Stage2."
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
    033100: false
    199820: false
    017040: false
  evidence_url_pending:
    033100: true
    199820: true
    017040: true
  source_proxy_only:
    033100: true
    199820: true
    017040: true
```

Limitations:

```text
- Price path is validated against Stock-Web tradable OHLC rows.
- Non-price evidence is not URL-repaired in this run.
- Therefore this artifact is useful for C02 second-tier power-equipment residual shape and high-MAE guardrail design, but should not promote positive weights until filings/IR/export/customer/report data verifies order backlog, grid/datacenter customer exposure, pricing/lead-time bottleneck, and margin conversion.
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
2. Preserve R1 / loop 73 metadata.
3. Add the cases to C02_POWER_GRID_DATACENTER_CAPEX only if parser validation passes.
4. Treat all three non-price triggers as evidence_url_pending=true and source_proxy_only=true until URL-level evidence is repaired.
5. Do not use these rows for positive weight promotion until filings/IR/export/customer/report data verifies order backlog, grid/datacenter exposure, pricing/lead-time bottleneck, and margin conversion.
6. Add a shadow-only rule candidate named C02_second_tier_grid_capex_order_bridge_and_high_mae_router.
7. Do not loosen Stage3-Green.
8. Add C02-specific guards:
   - source_proxy_only -> no Green
   - second-tier electrical equipment -> Stage2-Guarded at most until URL repair
   - 90D/180D MAE <= -30% without order bridge -> local 4B/high-MAE watch
   - low-price theme with 180D MAE <= -40% -> block Stage2
   - Green requires repaired order/backlog/customer/margin bridge
9. Keep production scoring unchanged unless later batch promotion logic independently marks this axis safe.
```

---

## 15. Next round state

```text
completed_round = R1
completed_loop = 73
next_round = R2
next_loop = 73
next_large_sector_hint = L2_AI_SEMICONDUCTOR_ELECTRONICS
```
