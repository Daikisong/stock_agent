# E2R Stock-Web v12 Residual Research — R5 Loop 72

```yaml
research_session: post_calibrated_sector_archetype_residual_research
mode: historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12
completed_round: R5
completed_loop: 72
next_round: R6
next_loop: 72
large_sector_id: L5_CONSUMER_BRAND_DISTRIBUTION
canonical_archetype_id: C18_CONSUMER_EXPORT_CHANNEL_REORDER
fine_archetype_id: K_FOOD_GLOBAL_CHANNEL_REORDER_AND_POST_SPIKE_INVENTORY_RISK
output_file: e2r_stock_web_v12_residual_round_R5_loop_72_L5_CONSUMER_BRAND_DISTRIBUTION_C18_CONSUMER_EXPORT_CHANNEL_REORDER_research.md
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

### Round resolution

The immediately preceding completed scheduled artifact in this automation chain was:

```text
completed_round = R4
completed_loop = 72
large_sector_id = L4_MATERIALS_SPREAD_RESOURCE
canonical_archetype_id = C15_MATERIAL_SPREAD_SUPERCYCLE
```

Therefore:

```text
scheduled_round = R5
scheduled_loop = 72
```

R5 maps to:

```text
large_sector_id = L5_CONSUMER_BRAND_DISTRIBUTION
```

This run selects:

```text
canonical_archetype_id = C18_CONSUMER_EXPORT_CHANNEL_REORDER
```

This is a valid R5/L5 pairing.

---

## 1. Why this R5/C18 run

The no-repeat ledger shows C18 is already meaningfully covered, but the top symbols are concentrated in a few K-food/K-brand exporters:

```text
C18_CONSUMER_EXPORT_CHANNEL_REORDER:
  rows: 108
  symbols: 18
  date_range: 2020-03-17~2024-12-16
  good/bad S2: 31/11
  4B/4C: 25/8
  top covered symbols: 003230(20), 005180(14), 004370(13), 383220(8), 097950(6), 161890(6)
```

This run avoids the highest-repeated symbols and adds:

```text
280360 롯데웰푸드
271560 오리온
001680 대상
```

The residual question is:

```text
Can C18 separate durable global-channel/reorder paths from K-food channel excitement that spikes first and then suffers deep inventory/valuation mean reversion?
```

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

| symbol | name | market | profile status | corporate-action candidate overlap with selected 180D window | calibration usable |
|---|---|---|---|---|---|
| `280360` | 롯데웰푸드 | KOSPI | active_like | none in 2024 test window; old 2019/2022 candidates only | true |
| `271560` | 오리온 | KOSPI | active_like | none listed | true |
| `001680` | 대상 | KOSPI | active_like | none in 2024 test window; old 1996~2005 candidates only | true |

Profile caveat:

```text
Stock-Web OHLC is raw/unadjusted marcap data. These cases are calibration-safe for the selected 2024 windows because no listed corporate-action candidate overlaps each entry~D+180 test window.
```

---

## 3. Evidence status and trigger discipline

This artifact uses conservative non-price evidence flags:

```text
evidence_url_pending = true
source_proxy_only = true
```

Reason:

```text
The Stock-Web price path is fully validated, but company-level export shipment, channel expansion, reorder, sell-through, inventory, and margin evidence still require later URL repair through DART, company IR, customs/export data, or sell-side reports before any production weight promotion.
```

C18 interpretation:

```text
C18 is not just “consumer stocks rallied.”
It asks whether export/channel expansion created reorder visibility:
- repeated foreign-channel sales,
- sell-through rather than channel stuffing,
- inventory and margin durability,
- and EPS/OP conversion.
```

This run is therefore useful for C18 residual shape and high-MAE guard design, but should not be promoted as positive weight until URL-level non-price evidence is repaired.

---

## 4. No-repeat and novelty check

Hard duplicate key:

```text
canonical_archetype_id + symbol + trigger_type + entry_date
```

Searches performed before writing:

```text
280360 + C18_CONSUMER_EXPORT_CHANNEL_REORDER -> no direct match found
271560 + C18_CONSUMER_EXPORT_CHANNEL_REORDER -> no direct match found
001680 + C18_CONSUMER_EXPORT_CHANNEL_REORDER -> no direct match found
```

Novelty accounting:

```json
{
  "new_symbol_count": 3,
  "minimum_new_symbol_count": 2,
  "minimum_positive_case_count": 1,
  "minimum_counterexample_count": 1,
  "new_independent_case_ratio": 1.00,
  "duplicate_status": "pass",
  "data_quality_status": "source_proxy_only_non_price_evidence"
}
```

---

## 5. Case design

| case_id | symbol | trigger family | research role |
|---|---|---|---|
| `R5L72_C18_271560_20240610` | `271560` 오리온 | global food channel stable reorder | positive-stable / low-MAE anchor |
| `R5L72_C18_001680_20240610` | `001680` 대상 | K-food export/channel acceleration | positive-guarded with later high-MAE |
| `R5L72_C18_280360_20240604` | `280360` 롯데웰푸드 | K-snack/global channel excitement and post-spike inventory/valuation risk | high-MFE but high-MAE counterexample |

The intended residual:

```text
C18 should not map early consumer-export price momentum directly to Green.
It should require channel reorder and sell-through proof, especially after rapid K-food/K-snack rerating.
```

---

## 6. Stock-Web OHLC and backtest

### 6.1 `271560` 오리온 — stable global-channel reorder anchor

Trigger:

```text
trigger_date = 2024-06-07
trigger_type = Stage2-Actionable
trigger_family = global_food_channel_stable_reorder
entry_date = 2024-06-10
entry_price = 92100.0
entry_price_type = next_tradable_open
```

Relevant Stock-Web rows:

```csv
d,o,h,l,c,v,a,mc,s,m
2024-06-07,93000.0,94300.0,92400.0,92400.0,177253.0,16496462100.0,3653138596800.0,39536132,KOSPI
2024-06-10,92100.0,100300.0,91700.0,97900.0,1591152.0,155392895400.0,3870587322800.0,39536132,KOSPI
2024-06-17,101300.0,105600.0,100300.0,104400.0,862812.0,89296982200.0,4127572180800.0,39536132,KOSPI
2024-06-18,105900.0,106700.0,99600.0,100900.0,568723.0,58029204400.0,3989195718800.0,39536132,KOSPI
2024-07-03,91200.0,91600.0,90100.0,90400.0,142004.0,12853062100.0,3574066332800.0,39536132,KOSPI
2024-08-13,89500.0,92600.0,89500.0,92000.0,388844.0,35718270700.0,3637324144000.0,39536132,KOSPI
2024-09-09,87000.0,89300.0,86400.0,88800.0,73460.0,6443557000.0,3510808521600.0,39536132,KOSPI
2024-10-11,101600.0,102900.0,98500.0,99000.0,216655.0,21641545200.0,3914077068000.0,39536132,KOSPI
```

Backtest:

| window | peak/high | peak date | trough/low | trough date | MFE | MAE |
|---|---:|---|---:|---|---:|---:|
| 30 calendar days | 106700 | 2024-06-18 | 90100 | 2024-07-03 | +15.85% | -2.17% |
| 90 calendar days | 106700 | 2024-06-18 | 86700 | 2024-07-30 | +15.85% | -5.86% |
| 180 calendar days | 106700 | 2024-06-18 | 86400 | 2024-09-09 | +15.85% | -6.19% |

Interpretation:

```text
271560 is a lower-volatility C18 positive-stable anchor.
The MFE is not explosive, but the low MAE supports the idea that mature global-channel consumer exporters can behave like stable Stage2/Yellow candidates rather than blowoff cases.
```

### 6.2 `001680` 대상 — export/channel acceleration with later high-MAE

Trigger:

```text
trigger_date = 2024-06-07
trigger_type = Stage2-Actionable-Guarded
trigger_family = k_food_export_channel_acceleration
entry_date = 2024-06-10
entry_price = 24400.0
entry_price_type = next_tradable_open
```

Relevant Stock-Web rows:

```csv
d,o,h,l,c,v,a,mc,s,m
2024-06-07,23150.0,24650.0,23150.0,24400.0,487372.0,11788128650.0,845411810000.0,34648025,KOSPI
2024-06-10,24400.0,26250.0,24050.0,26200.0,1334563.0,34244842000.0,907778255000.0,34648025,KOSPI
2024-06-12,26150.0,28400.0,26050.0,28400.0,1876686.0,51707211100.0,984003910000.0,34648025,KOSPI
2024-06-17,30000.0,30900.0,29000.0,30200.0,1307784.0,39545075750.0,1046370355000.0,34648025,KOSPI
2024-07-03,26300.0,26300.0,25000.0,25500.0,357177.0,9113251650.0,883524637500.0,34648025,KOSPI
2024-08-05,23150.0,23150.0,21050.0,21500.0,304699.0,6703108400.0,744932537500.0,34648025,KOSPI
2024-09-06,20400.0,20450.0,20000.0,20100.0,93713.0,1886854250.0,696425302500.0,34648025,KOSPI
2024-11-13,19000.0,19110.0,18750.0,18750.0,99825.0,1884155060.0,649650468750.0,34648025,KOSPI
```

Backtest:

| window | peak/high | peak date | trough/low | trough date | MFE | MAE |
|---|---:|---|---:|---|---:|---:|
| 30 calendar days | 30900 | 2024-06-17 | 24050 | 2024-06-10 | +26.64% | -1.43% |
| 90 calendar days | 30900 | 2024-06-17 | 20000 | 2024-09-06 | +26.64% | -18.03% |
| 180 calendar days | 30900 | 2024-06-17 | 18750 | 2024-11-13 | +26.64% | -23.16% |

Interpretation:

```text
001680 is a C18 positive-guarded case.
The early path is strong enough for Stage2-Actionable, but the later MAE shows that export/channel acceleration alone should not be Green unless sell-through and margin conversion are verified.
```

### 6.3 `280360` 롯데웰푸드 — high-MFE K-snack/channel excitement with later deep reversal

Trigger:

```text
trigger_date = 2024-06-03
trigger_type = Stage2-Actionable-Guarded
trigger_family = k_snack_global_channel_rerating_post_spike_inventory_risk
entry_date = 2024-06-04
entry_price = 151300.0
entry_price_type = next_tradable_open
```

Relevant Stock-Web rows:

```csv
d,o,h,l,c,v,a,mc,s,m
2024-06-03,146300.0,149000.0,144000.0,147600.0,17494.0,2564512100.0,1392543122400.0,9434574,KOSPI
2024-06-04,151300.0,161900.0,150200.0,156900.0,104639.0,16421311100.0,1480284660600.0,9434574,KOSPI
2024-06-10,159000.0,185500.0,159000.0,177900.0,157673.0,27717343200.0,1678410714600.0,9434574,KOSPI
2024-06-18,199800.0,208500.0,191100.0,193300.0,102305.0,19997474200.0,1823703154200.0,9434574,KOSPI
2024-07-01,182000.0,182000.0,168000.0,170500.0,49835.0,8699189000.0,1608594867000.0,9434574,KOSPI
2024-08-29,146900.0,146900.0,137400.0,138300.0,32610.0,4557001200.0,1304801584200.0,9434574,KOSPI
2024-09-02,140500.0,141500.0,136800.0,139900.0,12964.0,1794329600.0,1319896902600.0,9434574,KOSPI
2024-11-15,106200.0,107800.0,103000.0,106300.0,28394.0,2975841800.0,1002895216200.0,9434574,KOSPI
```

Backtest:

| window | peak/high | peak date | trough/low | trough date | MFE | MAE |
|---|---:|---|---:|---|---:|---:|
| 30 calendar days | 208500 | 2024-06-18 | 150200 | 2024-06-04 | +37.81% | -0.73% |
| 90 calendar days | 208500 | 2024-06-18 | 136800 | 2024-09-02 | +37.81% | -9.58% |
| 180 calendar days | 208500 | 2024-06-18 | 103000 | 2024-11-15 | +37.81% | -31.92% |

Interpretation:

```text
280360 is the key C18 counterexample/high-MAE residual.
The early MFE was excellent and the first-month drawdown was tiny, but the 180D path shows a full valuation/inventory mean-reversion risk.
This should remain Stage2-Actionable-Guarded or local 4B watch until channel reorder, sell-through, and margin conversion are verified.
```

---

## 7. Machine-readable trigger JSONL

```jsonl
{"row_type":"trigger","research_id":"R5L72_C18_K_FOOD_CHANNEL_REORDER","round":"R5","loop":72,"large_sector_id":"L5_CONSUMER_BRAND_DISTRIBUTION","canonical_archetype_id":"C18_CONSUMER_EXPORT_CHANNEL_REORDER","fine_archetype_id":"K_FOOD_GLOBAL_CHANNEL_REORDER_AND_POST_SPIKE_INVENTORY_RISK","symbol":"271560","name":"오리온","trigger_type":"Stage2-Actionable","trigger_family":"global_food_channel_stable_reorder","trigger_date":"2024-06-07","entry_date":"2024-06-10","entry_price":92100.0,"entry_price_type":"next_tradable_open","price_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","mfe_30d_pct":15.85,"mae_30d_pct":-2.17,"mfe_90d_pct":15.85,"mae_90d_pct":-5.86,"mfe_180d_pct":15.85,"mae_180d_pct":-6.19,"peak_price_180d":106700.0,"peak_date_180d":"2024-06-18","trough_price_180d":86400.0,"trough_date_180d":"2024-09-09","calibration_usable":true,"case_polarity":"positive_stable","evidence_url_pending":true,"source_proxy_only":true,"non_price_evidence_strength":"medium_pending_url_repair","price_only_blowoff":false,"expected_stage_current_profile":"Stage2-Actionable_to_Yellow_if_channel_reorder_verified","residual_error_type":"low_MAE_stable_channel_positive_but_green_requires_reorder_proof"}
{"row_type":"trigger","research_id":"R5L72_C18_K_FOOD_CHANNEL_REORDER","round":"R5","loop":72,"large_sector_id":"L5_CONSUMER_BRAND_DISTRIBUTION","canonical_archetype_id":"C18_CONSUMER_EXPORT_CHANNEL_REORDER","fine_archetype_id":"K_FOOD_GLOBAL_CHANNEL_REORDER_AND_POST_SPIKE_INVENTORY_RISK","symbol":"001680","name":"대상","trigger_type":"Stage2-Actionable-Guarded","trigger_family":"k_food_export_channel_acceleration","trigger_date":"2024-06-07","entry_date":"2024-06-10","entry_price":24400.0,"entry_price_type":"next_tradable_open","price_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","mfe_30d_pct":26.64,"mae_30d_pct":-1.43,"mfe_90d_pct":26.64,"mae_90d_pct":-18.03,"mfe_180d_pct":26.64,"mae_180d_pct":-23.16,"peak_price_180d":30900.0,"peak_date_180d":"2024-06-17","trough_price_180d":18750.0,"trough_date_180d":"2024-11-13","calibration_usable":true,"case_polarity":"positive_guarded","evidence_url_pending":true,"source_proxy_only":true,"non_price_evidence_strength":"medium_pending_url_repair","price_only_blowoff":false,"expected_stage_current_profile":"Stage2-Actionable-Guarded_until_sellthrough_margin_verified","residual_error_type":"strong_30d_MFE_but_later_high_MAE_requires_channel_reorder_proof"}
{"row_type":"trigger","research_id":"R5L72_C18_K_FOOD_CHANNEL_REORDER","round":"R5","loop":72,"large_sector_id":"L5_CONSUMER_BRAND_DISTRIBUTION","canonical_archetype_id":"C18_CONSUMER_EXPORT_CHANNEL_REORDER","fine_archetype_id":"K_FOOD_GLOBAL_CHANNEL_REORDER_AND_POST_SPIKE_INVENTORY_RISK","symbol":"280360","name":"롯데웰푸드","trigger_type":"Stage2-Actionable-Guarded","trigger_family":"k_snack_global_channel_rerating_post_spike_inventory_risk","trigger_date":"2024-06-03","entry_date":"2024-06-04","entry_price":151300.0,"entry_price_type":"next_tradable_open","price_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","mfe_30d_pct":37.81,"mae_30d_pct":-0.73,"mfe_90d_pct":37.81,"mae_90d_pct":-9.58,"mfe_180d_pct":37.81,"mae_180d_pct":-31.92,"peak_price_180d":208500.0,"peak_date_180d":"2024-06-18","trough_price_180d":103000.0,"trough_date_180d":"2024-11-15","calibration_usable":true,"case_polarity":"counterexample_high_mfe_high_mae","evidence_url_pending":true,"source_proxy_only":true,"non_price_evidence_strength":"medium_pending_url_repair","price_only_blowoff":false,"expected_stage_current_profile":"Stage2-Guarded_or_4B_high_MAE_watch","residual_error_type":"post_spike_consumer_channel_mean_reversion_without_verified_reorder"}
```

---

## 8. Score simulation and raw component breakdown

This is shadow-only and does not change production scoring.

| symbol | EPS/FCF | channel/reorder visibility | sell-through/inventory quality | market mispricing | valuation rerating | capital allocation | information confidence | shadow total | intended route |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| `271560` | 8 | 12 | 11 | 7 | 6 | 5 | 8 | 57 | Stage2/Yellow only after URL-repaired reorder proof |
| `001680` | 9 | 11 | 7 | 10 | 9 | 4 | 7 | 57 | Stage2-Guarded; high-MAE watch if sell-through weak |
| `280360` | 8 | 12 | 5 | 13 | 12 | 4 | 6 | 60 | Stage2-Guarded or local 4B; no Green without reorder/margin proof |

### Current calibrated profile stress test

The current calibrated profile already blocks pure price-only blowoff.  
The remaining C18 risk is subtler:

```text
C18 stable positive path:
  global food/channel exposure
  + low MAE
  + verified reorder/sell-through
  => Stage2-Actionable / Yellow, then Green only after margin/EPS conversion

C18 post-spike risk path:
  K-food/K-snack channel excitement
  + strong early MFE
  + later high MAE
  + no verified reorder or sell-through repair
  => Stage2-Guarded or 4B/high-MAE watch; no Green
```

The key diagnostic is not simply MFE size.  
It is the shape of the path:

```text
271560: lower MFE, low MAE -> stable channel candidate
001680: good MFE, later high MAE -> guarded
280360: excellent early MFE, severe 180D MAE -> post-spike counterexample
```

---

## 9. Aggregate metrics

```json
{
  "row_type": "aggregate",
  "research_id": "R5L72_C18_K_FOOD_CHANNEL_REORDER",
  "round": "R5",
  "loop": 72,
  "large_sector_id": "L5_CONSUMER_BRAND_DISTRIBUTION",
  "canonical_archetype_id": "C18_CONSUMER_EXPORT_CHANNEL_REORDER",
  "fine_archetype_id": "K_FOOD_GLOBAL_CHANNEL_REORDER_AND_POST_SPIKE_INVENTORY_RISK",
  "case_count": 3,
  "calibration_usable_case_count": 3,
  "positive_stable_case_count": 1,
  "positive_guarded_case_count": 1,
  "counterexample_count": 1,
  "new_symbol_count": 3,
  "source_proxy_only_count": 3,
  "evidence_url_pending_count": 3,
  "avg_mfe_30d_pct": 26.77,
  "avg_mae_30d_pct": -1.44,
  "avg_mfe_90d_pct": 26.77,
  "avg_mae_90d_pct": -11.16,
  "avg_mfe_180d_pct": 26.77,
  "avg_mae_180d_pct": -20.42,
  "worst_mae_180d_pct": -31.92
}
```

---

## 10. Shadow rule candidate

```yaml
row_type: canonical_archetype_rule_candidate
canonical_archetype_id: C18_CONSUMER_EXPORT_CHANNEL_REORDER
fine_archetype_id: K_FOOD_GLOBAL_CHANNEL_REORDER_AND_POST_SPIKE_INVENTORY_RISK
rule_name: C18_channel_reorder_sellthrough_and_high_mae_router
production_scoring_changed: false
shadow_weight_only: true
```

### Proposed routing logic

```text
For C18 consumer export/channel reorder cases:

Tier A: stable reorder candidate
  Conditions:
    - global/export channel is plausible
    - 30D/90D MAE is contained
    - reorder/sell-through evidence is URL-repaired
  Routing:
    - Stage2-Actionable allowed
    - Stage3-Yellow allowed
    - Green only after margin/EPS conversion or repeated channel data

Tier B: strong early MFE but source-proxy-only evidence
  Conditions:
    - early MFE is strong
    - non-price evidence is not URL-repaired
    - sell-through / inventory quality is not verified
  Routing:
    - Stage2-Actionable-Guarded
    - no Green
    - no positive weight promotion until evidence repair

Tier C: post-spike inventory/valuation risk
  Conditions:
    - 180D MAE worse than -25%
    - early MFE was mainly rerating
    - no verified reorder/sell-through bridge
  Routing:
    - local 4B/high-MAE watch
    - count as counterexample
    - block Green
```

### Suggested shadow delta

```json
{
  "row_type": "shadow_weight",
  "axis": "c18_channel_reorder_sellthrough_and_high_mae_router",
  "scope": "canonical_archetype_id:C18_CONSUMER_EXPORT_CHANNEL_REORDER",
  "proposal": {
    "source_proxy_only_green_allowed": false,
    "reorder_sellthrough_required_for_green": true,
    "post_spike_high_mae_watch_threshold_pct": -25.0,
    "stage2_guarded_allowed_when_30d_mae_contained": true,
    "positive_weight_blocked_until_url_repair": true
  },
  "confidence": "medium_low_until_url_repair",
  "apply_now": false,
  "reason": "Three new C18 consumer-export/channel cases show that early low-MAE MFE can be useful, but post-spike consumer rerating without verified reorder/sell-through can generate severe 180D MAE."
}
```

---

## 11. Residual contribution summary

```json
{
  "row_type": "residual_contribution",
  "research_id": "R5L72_C18_K_FOOD_CHANNEL_REORDER",
  "large_sector_id": "L5_CONSUMER_BRAND_DISTRIBUTION",
  "canonical_archetype_id": "C18_CONSUMER_EXPORT_CHANNEL_REORDER",
  "contribution": "Adds three less-repeated C18 K-food/global-channel examples and separates stable low-MAE channel candidates from high-MFE post-spike cases that later suffer inventory/valuation mean reversion.",
  "positive_case_added": 2,
  "counterexample_case_added": 1,
  "new_symbol_count": 3,
  "data_quality_blocker": "All three non-price channel/reorder triggers require URL-level repair before positive weight promotion.",
  "guardrail_added": "C18 Green requires verified reorder/sell-through/margin bridge; source_proxy_only plus 180D MAE worse than -25% should route to high-MAE watch or 4B local watch."
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
    271560: false
    001680: false
    280360: false
  evidence_url_pending:
    271560: true
    001680: true
    280360: true
  source_proxy_only:
    271560: true
    001680: true
    280360: true
```

Limitations:

```text
- Price path is validated against Stock-Web tradable OHLC rows.
- Non-price evidence is not URL-repaired in this run.
- Therefore this artifact is useful for C18 channel/reorder residual shape and high-MAE guardrail design, but should not promote positive weights until DART/IR/export/report evidence verifies reorder, sell-through, inventory quality, or margin conversion.
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
2. Preserve R5 / loop 72 metadata.
3. Add the cases to C18_CONSUMER_EXPORT_CHANNEL_REORDER only if parser validation passes.
4. Treat all three non-price triggers as evidence_url_pending=true and source_proxy_only=true until URL-level evidence is repaired.
5. Do not use these rows for positive weight promotion until DART/IR/export/report URLs verify channel reorder, sell-through, inventory quality, or margin conversion.
6. Add a shadow-only rule candidate named C18_channel_reorder_sellthrough_and_high_mae_router.
7. Do not loosen Stage3-Green.
8. Add C18-specific guards:
   - source_proxy_only -> no Green
   - 180D MAE <= -25% without verified reorder/sell-through -> route to high-MAE watch or local 4B
   - early MFE alone does not imply Green
9. Keep production scoring unchanged unless later batch promotion logic independently marks this axis safe.
```

---

## 14. Next round state

```text
completed_round = R5
completed_loop = 72
next_round = R6
next_loop = 72
next_large_sector_hint = L6_FINANCIAL_CAPITAL_RETURN_DIGITAL
```
