# E2R Stock-Web v12 Residual Research — R2 Loop 74

```yaml
research_session: post_calibrated_sector_archetype_residual_research
mode: historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12
completed_round: R2
completed_loop: 74
next_round: R3
next_loop: 74
large_sector_id: L2_AI_SEMICONDUCTOR_ELECTRONICS
canonical_archetype_id: C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE
fine_archetype_id: CMP_ETCH_PARTS_MEMORY_RECOVERY_EQUIPMENT_CYCLE_AND_HIGH_MAE_ROUTER
output_file: e2r_stock_web_v12_residual_round_R2_loop_74_L2_AI_SEMICONDUCTOR_ELECTRONICS_C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE_research.md
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
completed_round = R1
completed_loop  = 74
large_sector_id = L1_INDUSTRIALS_INFRA_DEFENSE_GRID
canonical_archetype_id = C01_ORDER_BACKLOG_MARGIN_BRIDGE
```

Therefore:

```text
scheduled_round = R2
scheduled_loop  = 74
```

R2 maps to:

```text
large_sector_id = L2_AI_SEMICONDUCTOR_ELECTRONICS
```

This run selects:

```text
canonical_archetype_id = C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE
fine_archetype_id = CMP_ETCH_PARTS_MEMORY_RECOVERY_EQUIPMENT_CYCLE_AND_HIGH_MAE_ROUTER
```

This is a valid R2/L2 pairing.

---

## 1. Why this R2/C10 run

The no-repeat ledger shows C10 is relatively thin versus C07/C08/C09 and still small enough to benefit from non-top-covered expansion:

```text
C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE:
  rows: 22
  symbols: 13
  date_range: 2023-03-17~2024-06-07
  good/bad S2: 9/4
  4B/4C: 2/0
  URL/proxy: 0/0
  top covered symbols: 095610(4), 036930(3), 240810(3), 084370(2), 테스(2), 000660(1)
```

This file avoids those top-covered symbols and adds three less-repeated memory-recovery equipment / parts names:

```text
281820 케이씨텍
089970 브이엠
101160 월덱스
```

Research question:

```text
Can C10 separate real memory-recovery equipment rerating from equipment/parts cycle rallies where theme relevance exists but customer order, utilization, or margin bridge is not yet durable?
```

C10 is a cycle-recovery archetype. A memory cycle turn can lift many boats, but Stage2/Yellow should require a working engine under the boat: customer capex, order visibility, utilization, margin conversion, and contained drawdown. Otherwise the move is only the tide.

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
| `281820` | 케이씨텍 | active_like / KOSPI | none listed | true |
| `089970` | 브이엠 | active_like / KOSDAQ | none listed | true |
| `101160` | 월덱스 | active_like / KOSDAQ | no 2024 overlap; latest listed candidate 2014-11-03 | true |

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
The Stock-Web price path is fully validated, but company-level memory capex recovery, CMP/etch equipment orders, consumable-part utilization, customer qualification, order backlog, delivery schedule, and margin bridge evidence still require later URL repair through filings, IR decks, customer data, or sell-side reports before production weight promotion.
```

C10 interpretation used here:

```text
C10 is not simply “semiconductor equipment stock rose.”
It asks whether memory recovery is company-convertible:
- memory customer capex recovery,
- equipment or consumable order visibility,
- utilization / replacement cycle,
- customer quality,
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
281820 + C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE -> no direct match found
089970 + C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE -> no direct match found
101160 + C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE -> no direct match found
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
| `R2L74_C10_281820_20240227` | `281820` 케이씨텍 | CMP / memory recovery equipment cycle rerating | positive-guarded high-MFE |
| `R2L74_C10_089970_20240312` | `089970` 브이엠 | etch equipment memory recovery relief then high MAE | delayed high-MAE counterexample |
| `R2L74_C10_101160_20240321` | `101160` 월덱스 | consumable parts recovery cycle weak-MFE path | weak-MFE / later-MAE counterexample |

The intended residual:

```text
C10 should separate:
1. memory equipment rerating with strong MFE and survivable MAE;
2. etch/equipment theme rallies that later break into high MAE without order bridge repair;
3. consumable-part cycle relevance where MFE remains too weak to justify Green.
```

---

## 6. Stock-Web OHLC and backtest

### 6.1 `281820` 케이씨텍 — CMP / memory equipment recovery positive-guarded case

Trigger:

```text
trigger_date = 2024-02-26
trigger_type = Stage2-Actionable-Guarded
trigger_family = cmp_memory_recovery_equipment_cycle_rerating
entry_date = 2024-02-27
entry_price = 38050.0
entry_price_type = next_tradable_open_after_memory_equipment_burst
```

Relevant Stock-Web rows:

```csv
d,o,h,l,c,v,a,mc,s,m
2024-02-26,32550.0,36100.0,32300.0,36100.0,605352.0,21267105100.0,753102171600.0,20861556,KOSPI
2024-02-27,38050.0,44700.0,34500.0,39200.0,2215249.0,86773423600.0,817772995200.0,20861556,KOSPI
2024-03-06,38250.0,49800.0,38250.0,47600.0,1602406.0,72067092750.0,993010065600.0,20861556,KOSPI
2024-03-08,46850.0,54100.0,46850.0,50500.0,1513524.0,76147859550.0,1053508578000.0,20861556,KOSPI
2024-04-11,36800.0,38350.0,36000.0,38100.0,189507.0,7076084950.0,794825283600.0,20861556,KOSPI
2024-05-14,33300.0,33550.0,32350.0,33350.0,214661.0,7051909100.0,695732892600.0,20861556,KOSPI
2024-07-11,52000.0,59000.0,51900.0,56500.0,612449.0,34524875200.0,1178677914000.0,20861556,KOSPI
2024-08-05,36500.0,37800.0,31000.0,33150.0,232519.0,8238318150.0,691560581400.0,20861556,KOSPI
```

Backtest:

| window | peak/high | peak date | trough/low | trough date | MFE | MAE |
|---|---:|---|---:|---|---:|---:|
| 30 calendar days | 54100 | 2024-03-08 | 34500 | 2024-02-27 | +42.18% | -9.33% |
| 90 calendar days | 54100 | 2024-03-08 | 32350 | 2024-05-14 | +42.18% | -14.98% |
| 180 calendar days | 59000 | 2024-07-11 | 31000 | 2024-08-05 | +55.06% | -18.53% |

Interpretation:

```text
281820 is the positive-guarded anchor.
The MFE was strong and persistent, but the entry itself was volatile and the 180D drawdown remained meaningful.
This supports Stage2-Actionable-Guarded / Yellow after URL repair, not automatic Green.
```

### 6.2 `089970` 브이엠 — etch equipment recovery label with delayed high MAE

Trigger:

```text
trigger_date = 2024-03-11
trigger_type = Stage2-FalsePositive-Candidate
trigger_family = etch_equipment_memory_recovery_relief_then_high_mae
entry_date = 2024-03-12
entry_price = 16000.0
entry_price_type = next_tradable_open_after_etch_equipment_burst
```

Relevant Stock-Web rows:

```csv
d,o,h,l,c,v,a,mc,s,m
2024-03-11,14240.0,15790.0,14040.0,15770.0,325665.0,4961110620.0,378173983150.0,23980595,KOSDAQ
2024-03-12,16000.0,16530.0,15330.0,16090.0,375878.0,6040150090.0,385847773550.0,23980595,KOSDAQ
2024-03-13,16120.0,17000.0,16120.0,16830.0,532257.0,8891035470.0,403593413850.0,23980595,KOSDAQ
2024-04-11,14010.0,16000.0,13950.0,14480.0,201406.0,3010686830.0,347239015600.0,23980595,KOSDAQ
2024-04-26,16800.0,17900.0,16800.0,17320.0,320145.0,5566167880.0,415343905400.0,23980595,KOSDAQ
2024-06-13,19870.0,20950.0,18610.0,19100.0,2289127.0,45360832200.0,459843864500.0,24075595,KOSDAQ
2024-08-05,10410.0,10580.0,8300.0,9890.0,267059.0,2708860170.0,238107634550.0,24075595,KOSDAQ
2024-09-06,9710.0,9810.0,9250.0,9350.0,55412.0,520379930.0,225106813250.0,24075595,KOSDAQ
```

Backtest:

| window | peak/high | peak date | trough/low | trough date | MFE | MAE |
|---|---:|---|---:|---|---:|---:|
| 30 calendar days | 17000 | 2024-03-13 | 13950 | 2024-04-11 | +6.25% | -12.81% |
| 90 calendar days | 17900 | 2024-04-26 | 13950 | 2024-04-11 | +11.88% | -12.81% |
| 180 calendar days | 20950 | 2024-06-13 | 8300 | 2024-08-05 | +30.94% | -48.13% |

Interpretation:

```text
089970 is the high-MAE counterexample.
The 180D MFE later looked useful, but it required enduring a collapse to -48.13% MAE.
This should be Stage2-Guarded at most, and more realistically local 4B/high-MAE watch until customer/order/margin evidence is repaired.
```

### 6.3 `101160` 월덱스 — consumable parts recovery with weak MFE and later MAE

Trigger:

```text
trigger_date = 2024-03-20
trigger_type = Stage2-Actionable-Guarded
trigger_family = consumable_parts_memory_recovery_cycle_weak_mfe_later_mae
entry_date = 2024-03-21
entry_price = 24600.0
entry_price_type = next_tradable_open_after_parts_cycle_burst
```

Relevant Stock-Web rows:

```csv
d,o,h,l,c,v,a,mc,s,m
2024-03-20,22800.0,23450.0,22700.0,23300.0,170715.0,3951636650.0,384706136900.0,16510993,KOSDAQ
2024-03-21,24600.0,25700.0,24250.0,25150.0,1375483.0,34624045800.0,415251473950.0,16510993,KOSDAQ
2024-04-02,25550.0,26150.0,24950.0,25700.0,659726.0,16920533000.0,424332520100.0,16510993,KOSDAQ
2024-05-31,22250.0,22450.0,21400.0,21450.0,295949.0,6432488500.0,354160799850.0,16510993,KOSDAQ
2024-06-03,21500.0,21800.0,21300.0,21700.0,129158.0,2787805950.0,358288548100.0,16510993,KOSDAQ
2024-08-05,21200.0,21350.0,18550.0,19050.0,396372.0,7968541920.0,314534416650.0,16510993,KOSDAQ
2024-08-20,25650.0,26050.0,25150.0,25900.0,334649.0,8608699350.0,427634718700.0,16510993,KOSDAQ
2024-09-06,20200.0,20350.0,19610.0,19690.0,386637.0,7647130800.0,325101452170.0,16510993,KOSDAQ
```

Backtest:

| window | peak/high | peak date | trough/low | trough date | MFE | MAE |
|---|---:|---|---:|---|---:|---:|
| 30 calendar days | 26150 | 2024-04-02 | 23450 | 2024-03-27 | +6.30% | -4.67% |
| 90 calendar days | 26150 | 2024-04-02 | 21300 | 2024-06-03 | +6.30% | -13.41% |
| 180 calendar days | 26150 | 2024-04-02 | 18550 | 2024-08-05 | +6.30% | -24.59% |

Interpretation:

```text
101160 is not a hard 4C failure, but it is a weak-MFE guardrail case.
The cycle relevance existed, yet the forward return never expanded beyond +6.30% while MAE worsened over time.
This should not be Green; it should stay Stage2-Guarded or local 4B watch until parts demand and margin bridge evidence is repaired.
```

---

## 7. Machine-readable trigger JSONL

```jsonl
{"row_type":"trigger","research_id":"R2L74_C10_MEMORY_EQUIPMENT_ROUTER","round":"R2","loop":74,"large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE","fine_archetype_id":"CMP_ETCH_PARTS_MEMORY_RECOVERY_EQUIPMENT_CYCLE_AND_HIGH_MAE_ROUTER","symbol":"281820","name":"케이씨텍","trigger_type":"Stage2-Actionable-Guarded","trigger_family":"cmp_memory_recovery_equipment_cycle_rerating","trigger_date":"2024-02-26","entry_date":"2024-02-27","entry_price":38050.0,"entry_price_type":"next_tradable_open_after_memory_equipment_burst","price_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","mfe_30d_pct":42.18,"mae_30d_pct":-9.33,"mfe_90d_pct":42.18,"mae_90d_pct":-14.98,"mfe_180d_pct":55.06,"mae_180d_pct":-18.53,"peak_price_180d":59000.0,"peak_date_180d":"2024-07-11","trough_price_180d":31000.0,"trough_date_180d":"2024-08-05","calibration_usable":true,"case_polarity":"positive_guarded_high_mfe","evidence_url_pending":true,"source_proxy_only":true,"non_price_evidence_strength":"medium_pending_url_repair","price_only_blowoff":false,"expected_stage_current_profile":"Stage2-Guarded_to_Yellow_if_memory_recovery_order_margin_bridge_repaired","residual_error_type":"strong_memory_equipment_mfe_but_green_requires_customer_order_margin_evidence"}
{"row_type":"trigger","research_id":"R2L74_C10_MEMORY_EQUIPMENT_ROUTER","round":"R2","loop":74,"large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE","fine_archetype_id":"CMP_ETCH_PARTS_MEMORY_RECOVERY_EQUIPMENT_CYCLE_AND_HIGH_MAE_ROUTER","symbol":"089970","name":"브이엠","trigger_type":"Stage2-FalsePositive-Candidate","trigger_family":"etch_equipment_memory_recovery_relief_then_high_mae","trigger_date":"2024-03-11","entry_date":"2024-03-12","entry_price":16000.0,"entry_price_type":"next_tradable_open_after_etch_equipment_burst","price_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","mfe_30d_pct":6.25,"mae_30d_pct":-12.81,"mfe_90d_pct":11.88,"mae_90d_pct":-12.81,"mfe_180d_pct":30.94,"mae_180d_pct":-48.13,"peak_price_180d":20950.0,"peak_date_180d":"2024-06-13","trough_price_180d":8300.0,"trough_date_180d":"2024-08-05","calibration_usable":true,"case_polarity":"counterexample_delayed_high_mae","evidence_url_pending":true,"source_proxy_only":true,"non_price_evidence_strength":"low_pending_url_repair","price_only_blowoff":false,"expected_stage_current_profile":"Stage2-Guarded_or_4B_high_MAE_watch_until_etch_order_bridge_repaired","residual_error_type":"memory_equipment_recovery_label_had_later_high_mae_without_customer_order_bridge"}
{"row_type":"trigger","research_id":"R2L74_C10_MEMORY_EQUIPMENT_ROUTER","round":"R2","loop":74,"large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE","fine_archetype_id":"CMP_ETCH_PARTS_MEMORY_RECOVERY_EQUIPMENT_CYCLE_AND_HIGH_MAE_ROUTER","symbol":"101160","name":"월덱스","trigger_type":"Stage2-Actionable-Guarded","trigger_family":"consumable_parts_memory_recovery_cycle_weak_mfe_later_mae","trigger_date":"2024-03-20","entry_date":"2024-03-21","entry_price":24600.0,"entry_price_type":"next_tradable_open_after_parts_cycle_burst","price_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","mfe_30d_pct":6.3,"mae_30d_pct":-4.67,"mfe_90d_pct":6.3,"mae_90d_pct":-13.41,"mfe_180d_pct":6.3,"mae_180d_pct":-24.59,"peak_price_180d":26150.0,"peak_date_180d":"2024-04-02","trough_price_180d":18550.0,"trough_date_180d":"2024-08-05","calibration_usable":true,"case_polarity":"counterexample_weak_mfe_later_mae","evidence_url_pending":true,"source_proxy_only":true,"non_price_evidence_strength":"low_pending_url_repair","price_only_blowoff":false,"expected_stage_current_profile":"Stage2-Guarded_or_local_4B_watch_until_parts_demand_margin_bridge_repaired","residual_error_type":"consumable_parts_cycle_relevance_with_weak_mfe_and_later_mae_should_not_green"}
```

---

## 8. Score simulation and raw component breakdown

This is shadow-only and does not change production scoring.

| symbol | memory recovery relevance | customer/order bridge | utilization / replacement cycle | market mispricing | valuation rerating | margin conversion | information confidence | shadow total | intended route |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| `281820` | 14 | 11 | 10 | 13 | 13 | 9 | 7 | 77 | Stage2-Guarded / Yellow after evidence repair |
| `089970` | 10 | 5 | 5 | 8 | 7 | 3 | 5 | 43 | Stage2-Guarded or 4B/high-MAE watch |
| `101160` | 9 | 5 | 6 | 5 | 4 | 4 | 5 | 38 | Stage2-Guarded or local 4B watch |

### Current calibrated profile stress test

The current calibrated profile already blocks pure price-only blowoff.  
The remaining C10 issue is **cycle relevance without customer/order/margin bridge**:

```text
C10 cleaner path:
  memory recovery equipment exposure
  + strong MFE
  + MAE remains survivable
  + URL-repaired customer/order/margin evidence
  => Stage2-Actionable-Guarded / Yellow, possible Green after proof

C10 high-MAE trap:
  equipment recovery label exists
  + MFE eventually appears
  + 180D MAE <= -40%
  + evidence remains source_proxy_only
  => no Green; local 4B/high-MAE watch

C10 weak-MFE cycle path:
  cycle relevance exists
  + MFE_90D < +10%
  + MAE keeps expanding
  + bridge evidence missing
  => Stage2-Guarded only or local 4B watch
```

`281820` prevents overblocking.  
`089970` shows why later MFE cannot rescue a path that first exposes a near-half drawdown.  
`101160` shows that a weak-MFE parts cycle should not be promoted from theme relevance alone.

---

## 9. Aggregate metrics

```json
{
  "row_type": "aggregate",
  "research_id": "R2L74_C10_MEMORY_EQUIPMENT_ROUTER",
  "round": "R2",
  "loop": 74,
  "large_sector_id": "L2_AI_SEMICONDUCTOR_ELECTRONICS",
  "canonical_archetype_id": "C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE",
  "fine_archetype_id": "CMP_ETCH_PARTS_MEMORY_RECOVERY_EQUIPMENT_CYCLE_AND_HIGH_MAE_ROUTER",
  "case_count": 3,
  "calibration_usable_case_count": 3,
  "positive_guarded_case_count": 1,
  "counterexample_count": 2,
  "new_symbol_count": 3,
  "source_proxy_only_count": 3,
  "evidence_url_pending_count": 3,
  "avg_mfe_30d_pct": 18.24,
  "avg_mae_30d_pct": -8.94,
  "avg_mfe_90d_pct": 20.12,
  "avg_mae_90d_pct": -13.73,
  "avg_mfe_180d_pct": 30.77,
  "avg_mae_180d_pct": -30.42,
  "max_mfe_180d_pct": 55.06,
  "worst_mae_180d_pct": -48.13
}
```

---

## 10. 4B proximity split

```json
{
  "row_type": "4b_split",
  "research_id": "R2L74_C10_MEMORY_EQUIPMENT_ROUTER",
  "stage2_guarded_or_yellow_candidate": [
    {
      "symbol": "281820",
      "reason": "strong 30D/180D MFE with survivable but non-trivial MAE; requires memory equipment customer/order/margin evidence before Green"
    }
  ],
  "local_4b_high_mae_watch": [
    {
      "symbol": "089970",
      "reason": "180D MFE reached +30.94%, but 180D MAE reached -48.13%; later MFE does not validate initial Green"
    },
    {
      "symbol": "101160",
      "reason": "MFE stayed weak at +6.30% while 180D MAE widened to -24.59%"
    }
  ],
  "full_4b_or_green_requires_non_price_evidence": [
    "memory customer capex/order visibility",
    "equipment or consumable replacement cycle",
    "customer qualification and repeat order",
    "utilization recovery",
    "gross margin / operating margin conversion"
  ]
}
```

---

## 11. Shadow rule candidate

```yaml
row_type: canonical_archetype_rule_candidate
canonical_archetype_id: C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE
fine_archetype_id: CMP_ETCH_PARTS_MEMORY_RECOVERY_EQUIPMENT_CYCLE_AND_HIGH_MAE_ROUTER
rule_name: C10_memory_recovery_equipment_bridge_and_high_mae_router
production_scoring_changed: false
shadow_weight_only: true
```

### Proposed routing logic

```text
For C10 memory recovery equipment/parts cases:

Tier A: verified memory equipment recovery
  Conditions:
    - memory customer capex/order evidence is URL-repaired
    - equipment or parts utilization/replacement cycle is visible
    - 30D/90D MAE remains survivable
    - MFE persists beyond one event candle
  Routing:
    - Stage2-Actionable-Guarded allowed
    - Stage3-Yellow allowed after evidence repair
    - Green only after customer/order/margin bridge is verified

Tier B: later-MFE / high-MAE trap
  Conditions:
    - MFE eventually becomes meaningful
    - MAE_180D <= -40%
    - bridge evidence remains source_proxy_only
  Routing:
    - local 4B/high-MAE watch
    - no Green
    - no production positive weight promotion

Tier C: weak-MFE cycle relevance
  Conditions:
    - MFE_90D < +10%
    - MAE_180D <= -20%
    - customer/order/margin bridge is missing
  Routing:
    - Stage2-Guarded at most
    - local 4B watch
    - count as counterexample if evidence remains unrepaired
```

### Suggested shadow delta

```json
{
  "row_type": "shadow_weight",
  "axis": "c10_memory_recovery_equipment_bridge_and_high_mae_router",
  "scope": "canonical_archetype_id:C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE",
  "proposal": {
    "source_proxy_only_green_allowed": false,
    "memory_customer_order_margin_bridge_required_for_green": true,
    "stage2_guarded_allowed_for_survivable_mae_high_mfe": true,
    "high_mae_watch_threshold_180d_pct": -40.0,
    "weak_mfe_threshold_90d_pct": 10.0,
    "weak_mfe_later_mae_watch_threshold_180d_pct": -20.0,
    "positive_weight_blocked_until_url_repair": true
  },
  "confidence": "medium_low_until_url_repair",
  "apply_now": false,
  "reason": "One high-MFE memory equipment case and two equipment/parts high-MAE or weak-MFE cases show that C10 should require URL-repaired customer/order/utilization/margin evidence before Yellow/Green."
}
```

---

## 12. Residual contribution summary

```json
{
  "row_type": "residual_contribution",
  "research_id": "R2L74_C10_MEMORY_EQUIPMENT_ROUTER",
  "large_sector_id": "L2_AI_SEMICONDUCTOR_ELECTRONICS",
  "canonical_archetype_id": "C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE",
  "contribution": "Adds three non-top-covered C10 memory recovery equipment/parts cases and separates a strong CMP equipment rerating path from later-MFE/high-MAE and weak-MFE parts-cycle counterexamples. C10 Green should require URL-repaired memory customer order, utilization, replacement-cycle, and margin evidence.",
  "positive_guarded_case_added": 1,
  "counterexample_case_added": 2,
  "new_symbol_count": 3,
  "data_quality_blocker": "All three non-price memory equipment/cycle triggers require URL-level repair before positive weight promotion.",
  "guardrail_added": "C10 source_proxy_only cases with MAE_180D <= -40% should route to 4B/high-MAE watch; weak-MFE cases with MFE_90D < +10% and MAE_180D <= -20% should cap at Stage2-Guarded."
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
    281820: false
    089970: false
    101160: false
  evidence_url_pending:
    281820: true
    089970: true
    101160: true
  source_proxy_only:
    281820: true
    089970: true
    101160: true
```

Limitations:

```text
- Price path is validated against Stock-Web tradable OHLC rows.
- Non-price evidence is not URL-repaired in this run.
- Therefore this artifact is useful for C10 memory recovery equipment-cycle residual shape and high-MAE guardrail design, but should not promote positive weights until filings/IR/customer/report data verifies memory customer capex, equipment orders, consumable utilization, replacement cycle, and margin conversion.
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
2. Preserve R2 / loop 74 metadata.
3. Add the cases to C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE only if parser validation passes.
4. Treat all three non-price triggers as evidence_url_pending=true and source_proxy_only=true until URL-level evidence is repaired.
5. Do not use these rows for positive weight promotion until filings/IR/customer/report data verifies memory customer capex, equipment order visibility, utilization, replacement cycle, and margin conversion.
6. Add a shadow-only rule candidate named C10_memory_recovery_equipment_bridge_and_high_mae_router.
7. Do not loosen Stage3-Green.
8. Add C10-specific guards:
   - source_proxy_only -> no Green
   - Green requires repaired memory customer/order/utilization/margin bridge
   - MAE_180D <= -40% without bridge repair -> local 4B/high-MAE watch
   - MFE_90D < +10% and MAE_180D <= -20% -> Stage2-Guarded at most
   - later MFE after extreme MAE does not validate initial Green
9. Keep production scoring unchanged unless later batch promotion logic independently marks this axis safe.
```

---

## 15. Next round state

```text
completed_round = R2
completed_loop = 74
next_round = R3
next_loop = 74
next_large_sector_hint = L3_BATTERY_EV_GREEN_MOBILITY
```
