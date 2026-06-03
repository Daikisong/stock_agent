# E2R Stock-Web v12 Residual Research — R5 Loop 74

```yaml
research_session: post_calibrated_sector_archetype_residual_research
mode: historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12
completed_round: R5
completed_loop: 74
next_round: R6
next_loop: 74
large_sector_id: L5_CONSUMER_BRAND_DISTRIBUTION
canonical_archetype_id: C18_CONSUMER_EXPORT_CHANNEL_REORDER
fine_archetype_id: KFOOD_SNACK_CONFECTIONERY_EXPORT_CHANNEL_REORDER_AND_WEAK_MFE_ROUTER
output_file: e2r_stock_web_v12_residual_round_R5_loop_74_L5_CONSUMER_BRAND_DISTRIBUTION_C18_CONSUMER_EXPORT_CHANNEL_REORDER_research.md
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
completed_round = R4
completed_loop  = 74
large_sector_id = L4_MATERIALS_SPREAD_RESOURCE
canonical_archetype_id = C15_MATERIAL_SPREAD_SUPERCYCLE
```

Therefore:

```text
scheduled_round = R5
scheduled_loop  = 74
```

R5 maps to:

```text
large_sector_id = L5_CONSUMER_BRAND_DISTRIBUTION
```

This run selects:

```text
canonical_archetype_id = C18_CONSUMER_EXPORT_CHANNEL_REORDER
fine_archetype_id = KFOOD_SNACK_CONFECTIONERY_EXPORT_CHANNEL_REORDER_AND_WEAK_MFE_ROUTER
```

This is a valid R5/L5 pairing.

---

## 1. Why this R5/C18 run

The no-repeat ledger shows C18 is covered but concentrated in a small set of top food / consumer export names:

```text
C18_CONSUMER_EXPORT_CHANNEL_REORDER:
  rows: 108
  symbols: 18
  date_range: 2020-03-17~2024-12-16
  good/bad S2: 31/11
  4B/4C: 25/8
  URL/proxy: 0/0
  top covered symbols: 003230(20), 005180(14), 004370(13), 383220(8), 097950(6), 161890(6)
```

This file avoids those top-covered symbols and adds:

```text
001680 대상
280360 롯데웰푸드
271560 오리온
```

Research question:

```text
Can C18 separate real K-food / confectionery export-channel reorder rerating from an overseas-channel relief setup where the label is plausible but MFE remains weak?
```

C18 is a reorder archetype. A distributor order is not just a first shipment; it is a pulse that repeats. The model should reward the second heartbeat: channel sell-through, reorder, margin conversion, and operating leverage. A single export headline without reorder proof is only a sample box, not a route.

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
| `001680` | 대상 | active_like / KOSPI | no 2024 overlap; latest listed candidate 2005-08-05 | true |
| `280360` | 롯데웰푸드 | active_like / KOSPI | no 2024 overlap; latest listed candidate 2022-07-20 | true |
| `271560` | 오리온 | active_like / KOSPI | none listed | true |

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
The Stock-Web price path is fully validated, but company-level export shipment, distributor reorder, overseas sell-through, channel inventory, ASP, gross margin, and operating-leverage evidence still require later URL repair through filings, IR decks, customs/export data, channel data, or sell-side reports before production weight promotion.
```

C18 interpretation used here:

```text
C18 is not simply “K-food stock rose.”
It asks whether export demand is reorder-convertible:
- overseas channel expansion,
- distributor reorder,
- sell-through and channel inventory,
- ASP / mix,
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
001680 + C18_CONSUMER_EXPORT_CHANNEL_REORDER -> no direct match found
280360 + C18_CONSUMER_EXPORT_CHANNEL_REORDER -> no direct match found
271560 + C18_CONSUMER_EXPORT_CHANNEL_REORDER -> no direct match found
```

Novelty accounting:

```json
{
  "new_symbol_count": 3,
  "minimum_new_symbol_count": 2,
  "positive_case_count": 2,
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
| `R5L74_C18_280360_20240422` | `280360` 롯데웰푸드 | confectionery export-channel reorder / operating leverage rerating | positive anchor |
| `R5L74_C18_001680_20240422` | `001680` 대상 | K-food export-channel reorder / margin rerating | positive-guarded |
| `R5L74_C18_271560_20240611` | `271560` 오리온 | overseas-channel relief plateau with weak MFE | counterexample / weak-MFE guard |

The intended residual:

```text
C18 should separate:
1. export-channel reorder cases where MFE persists and MAE remains contained;
2. K-food margin paths that rerate after channel reorder but still need URL-repaired evidence before Green;
3. overseas-channel relief entries where the brand/channel label is plausible but MFE stays too weak to justify promotion.
```

---

## 6. Stock-Web OHLC and backtest

### 6.1 `280360` 롯데웰푸드 — confectionery export-channel reorder / operating leverage rerating

Trigger:

```text
trigger_date = 2024-04-19
trigger_type = Stage2-Actionable
trigger_family = confectionery_export_channel_reorder_operating_leverage_rerating
entry_date = 2024-04-22
entry_price = 128800.0
entry_price_type = next_tradable_open_after_confectionery_channel_burst
```

Relevant Stock-Web rows:

```csv
d,o,h,l,c,v,a,mc,s,m
2024-04-19,124000.0,129200.0,123100.0,127000.0,12211.0,1544943700.0,1198190898000.0,9434574,KOSPI
2024-04-22,128800.0,132100.0,126600.0,132100.0,22935.0,2996549400.0,1246307225400.0,9434574,KOSPI
2024-05-22,143500.0,150000.0,140800.0,149800.0,37472.0,5542141000.0,1413299185200.0,9434574,KOSPI
2024-06-10,159000.0,185500.0,159000.0,177900.0,157673.0,27717343200.0,1678410714600.0,9434574,KOSPI
2024-06-18,199800.0,208500.0,191100.0,193300.0,102305.0,19997474200.0,1823703154200.0,9434574,KOSPI
2024-08-05,159900.0,159900.0,143500.0,148500.0,51431.0,7751732900.0,1401034239000.0,9434574,KOSPI
2024-09-06,134300.0,134600.0,129000.0,129600.0,16207.0,2103376300.0,1222720790400.0,9434574,KOSPI
```

Backtest:

| window | peak/high | peak date | trough/low | trough date | MFE | MAE |
|---|---:|---|---:|---|---:|---:|
| 30 calendar days | 150000 | 2024-05-22 | 126600 | 2024-04-22 | +16.46% | -1.71% |
| 90 calendar days | 208500 | 2024-06-18 | 126600 | 2024-04-22 | +61.88% | -1.71% |
| 180 calendar days | 208500 | 2024-06-18 | 126600 | 2024-04-22 | +61.88% | -1.71% |

Interpretation:

```text
280360 is the clean C18 positive anchor.
The price path had strong MFE and very contained MAE, which is the signature of a channel-reorder rerating.
This supports Stage2-Actionable / Yellow after evidence repair. Green still requires URL-repaired export, reorder, ASP/mix, and margin evidence.
```

### 6.2 `001680` 대상 — K-food export-channel reorder / margin rerating

Trigger:

```text
trigger_date = 2024-04-19
trigger_type = Stage2-Actionable-Guarded
trigger_family = kfood_export_channel_reorder_margin_rerating
entry_date = 2024-04-22
entry_price = 21200.0
entry_price_type = next_tradable_open_after_kfood_export_channel_burst
```

Relevant Stock-Web rows:

```csv
d,o,h,l,c,v,a,mc,s,m
2024-04-19,20800.0,21100.0,20650.0,20900.0,180085.0,3763236950.0,724143722500.0,34648025,KOSPI
2024-04-22,21200.0,22000.0,21000.0,21900.0,408245.0,8863276150.0,758791747500.0,34648025,KOSPI
2024-05-22,22900.0,24400.0,22750.0,24000.0,1011139.0,24184986200.0,831552600000.0,34648025,KOSPI
2024-06-10,24400.0,26250.0,24050.0,26200.0,1334563.0,34244842000.0,907778255000.0,34648025,KOSPI
2024-06-17,30000.0,30900.0,29000.0,30200.0,1307784.0,39545075750.0,1046370355000.0,34648025,KOSPI
2024-08-05,23150.0,23150.0,21050.0,21500.0,304699.0,6703108400.0,744932537500.0,34648025,KOSPI
2024-09-09,19750.0,20500.0,19670.0,20350.0,101379.0,2035924040.0,705087308750.0,34648025,KOSPI
```

Backtest:

| window | peak/high | peak date | trough/low | trough date | MFE | MAE |
|---|---:|---|---:|---|---:|---:|
| 30 calendar days | 24400 | 2024-05-22 | 21000 | 2024-04-22 | +15.09% | -0.94% |
| 90 calendar days | 30900 | 2024-06-17 | 21000 | 2024-04-22 | +45.75% | -0.94% |
| 180 calendar days | 30900 | 2024-06-17 | 19670 | 2024-09-09 | +45.75% | -7.22% |

Interpretation:

```text
001680 is a positive-guarded C18 case.
The initial path was strong and low-MAE, then the later pullback remained below the hard-failure zone.
This is Stage2-Guarded / Yellow after evidence repair, not automatic Green from K-food theme relevance alone.
```

### 6.3 `271560` 오리온 — overseas-channel relief plateau with weak MFE

Trigger:

```text
trigger_date = 2024-06-10
trigger_type = Stage2-FalsePositive-Candidate
trigger_family = overseas_channel_reorder_plateau_weak_mfe_drawdown
entry_date = 2024-06-11
entry_price = 99000.0
entry_price_type = next_tradable_open_after_overseas_channel_relief
```

Relevant Stock-Web rows:

```csv
d,o,h,l,c,v,a,mc,s,m
2024-06-10,92100.0,100300.0,91700.0,97900.0,1591152.0,155392895400.0,3870587322800.0,39536132,KOSPI
2024-06-11,99000.0,102000.0,96500.0,97200.0,865201.0,85910891000.0,3842912030400.0,39536132,KOSPI
2024-06-18,105900.0,106700.0,99600.0,100900.0,568723.0,58029204400.0,3989195718800.0,39536132,KOSPI
2024-07-03,91200.0,91600.0,90100.0,90400.0,142004.0,12853062100.0,3574066332800.0,39536132,KOSPI
2024-08-05,88600.0,89300.0,81800.0,83900.0,368927.0,31458278000.0,3317081474800.0,39536132,KOSPI
2024-09-09,87000.0,89300.0,86400.0,88800.0,73460.0,6443557000.0,3510808521600.0,39536132,KOSPI
2024-11-20,98900.0,104600.0,98500.0,103400.0,399211.0,41026161600.0,4088036048800.0,39536132,KOSPI
```

Backtest:

| window | peak/high | peak date | trough/low | trough date | MFE | MAE |
|---|---:|---|---:|---|---:|---:|
| 30 calendar days | 106700 | 2024-06-18 | 90100 | 2024-07-03 | +7.78% | -8.99% |
| 90 calendar days | 106700 | 2024-06-18 | 81800 | 2024-08-05 | +7.78% | -17.37% |
| 180 calendar days | 106700 | 2024-06-18 | 81800 | 2024-08-05 | +7.78% | -17.37% |

Interpretation:

```text
271560 is the weak-MFE counterexample.
The overseas-channel label was plausible, but the entry failed to expand MFE and then produced a meaningful drawdown.
This should block Green and either block Stage2 or cap at Stage2-Guarded until reorder, channel inventory, and margin bridge evidence are repaired.
```

---

## 7. Machine-readable trigger JSONL

```jsonl
{"row_type":"trigger","research_id":"R5L74_C18_KFOOD_EXPORT_CHANNEL_ROUTER","round":"R5","loop":74,"large_sector_id":"L5_CONSUMER_BRAND_DISTRIBUTION","canonical_archetype_id":"C18_CONSUMER_EXPORT_CHANNEL_REORDER","fine_archetype_id":"KFOOD_SNACK_CONFECTIONERY_EXPORT_CHANNEL_REORDER_AND_WEAK_MFE_ROUTER","symbol":"001680","name":"대상","trigger_type":"Stage2-Actionable-Guarded","trigger_family":"kfood_export_channel_reorder_margin_rerating","trigger_date":"2024-04-19","entry_date":"2024-04-22","entry_price":21200.0,"entry_price_type":"next_tradable_open_after_kfood_export_channel_burst","price_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","mfe_30d_pct":15.09,"mae_30d_pct":-0.94,"mfe_90d_pct":45.75,"mae_90d_pct":-0.94,"mfe_180d_pct":45.75,"mae_180d_pct":-7.22,"peak_price_180d":30900.0,"peak_date_180d":"2024-06-17","trough_price_180d":19670.0,"trough_date_180d":"2024-09-09","calibration_usable":true,"case_polarity":"positive_guarded_export_channel","evidence_url_pending":true,"source_proxy_only":true,"non_price_evidence_strength":"medium_pending_url_repair","price_only_blowoff":false,"expected_stage_current_profile":"Stage2-Guarded_to_Yellow_if_export_reorder_margin_bridge_repaired","residual_error_type":"positive_kfood_export_channel_path_requires_url_repaired_reorder_margin_evidence_before_green"}
{"row_type":"trigger","research_id":"R5L74_C18_KFOOD_EXPORT_CHANNEL_ROUTER","round":"R5","loop":74,"large_sector_id":"L5_CONSUMER_BRAND_DISTRIBUTION","canonical_archetype_id":"C18_CONSUMER_EXPORT_CHANNEL_REORDER","fine_archetype_id":"KFOOD_SNACK_CONFECTIONERY_EXPORT_CHANNEL_REORDER_AND_WEAK_MFE_ROUTER","symbol":"280360","name":"롯데웰푸드","trigger_type":"Stage2-Actionable","trigger_family":"confectionery_export_channel_reorder_operating_leverage_rerating","trigger_date":"2024-04-19","entry_date":"2024-04-22","entry_price":128800.0,"entry_price_type":"next_tradable_open_after_confectionery_channel_burst","price_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","mfe_30d_pct":16.46,"mae_30d_pct":-1.71,"mfe_90d_pct":61.88,"mae_90d_pct":-1.71,"mfe_180d_pct":61.88,"mae_180d_pct":-1.71,"peak_price_180d":208500.0,"peak_date_180d":"2024-06-18","trough_price_180d":126600.0,"trough_date_180d":"2024-04-22","calibration_usable":true,"case_polarity":"positive_anchor_low_mae","evidence_url_pending":true,"source_proxy_only":true,"non_price_evidence_strength":"medium_pending_url_repair","price_only_blowoff":false,"expected_stage_current_profile":"Stage2-Actionable_to_Yellow_after_global_distribution_reorder_margin_bridge_repaired","residual_error_type":"positive_confectionery_export_distribution_path_requires_url_repaired_channel_reorder_margin_evidence_before_green"}
{"row_type":"trigger","research_id":"R5L74_C18_KFOOD_EXPORT_CHANNEL_ROUTER","round":"R5","loop":74,"large_sector_id":"L5_CONSUMER_BRAND_DISTRIBUTION","canonical_archetype_id":"C18_CONSUMER_EXPORT_CHANNEL_REORDER","fine_archetype_id":"KFOOD_SNACK_CONFECTIONERY_EXPORT_CHANNEL_REORDER_AND_WEAK_MFE_ROUTER","symbol":"271560","name":"오리온","trigger_type":"Stage2-FalsePositive-Candidate","trigger_family":"overseas_channel_reorder_plateau_weak_mfe_drawdown","trigger_date":"2024-06-10","entry_date":"2024-06-11","entry_price":99000.0,"entry_price_type":"next_tradable_open_after_overseas_channel_relief","price_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","mfe_30d_pct":7.78,"mae_30d_pct":-8.99,"mfe_90d_pct":7.78,"mae_90d_pct":-17.37,"mfe_180d_pct":7.78,"mae_180d_pct":-17.37,"peak_price_180d":106700.0,"peak_date_180d":"2024-06-18","trough_price_180d":81800.0,"trough_date_180d":"2024-08-05","calibration_usable":true,"case_polarity":"counterexample_weak_mfe_drawdown","evidence_url_pending":true,"source_proxy_only":true,"non_price_evidence_strength":"low_pending_url_repair","price_only_blowoff":false,"expected_stage_current_profile":"blocked_Stage2_or_Stage2_Guarded_until_overseas_reorder_margin_bridge_repaired","residual_error_type":"overseas_channel_label_with_weak_mfe_and_drawdown_should_not_green_without_reorder_bridge"}
```

---

## 8. Score simulation and raw component breakdown

This is shadow-only and does not change production scoring.

| symbol | export/channel relevance | reorder visibility | sell-through / inventory | market mispricing | valuation rerating | margin conversion | information confidence | shadow total | intended route |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| `280360` | 14 | 13 | 12 | 13 | 14 | 12 | 7 | 85 | Stage2/Yellow after channel reorder and margin evidence repair |
| `001680` | 13 | 11 | 10 | 12 | 11 | 10 | 6 | 73 | Stage2-Guarded / Yellow after export and margin bridge repair |
| `271560` | 10 | 4 | 5 | 5 | 4 | 5 | 5 | 38 | blocked Stage2 or guarded until reorder bridge repair |

### Current calibrated profile stress test

The current calibrated profile already blocks pure price-only blowoff.  
The remaining C18 issue is **export/channel label without reorder proof**:

```text
C18 clean reorder path:
  export/channel expansion relevance
  + MFE persists across 90D/180D
  + MAE remains contained
  + URL-repaired reorder / sell-through / margin evidence
  => Stage2-Actionable / Yellow, possible Green after proof

C18 positive-guarded path:
  K-food / snack export theme is plausible
  + MFE is strong
  + drawdown is manageable
  + evidence remains source_proxy_only
  => Stage2-Guarded at most until evidence repair

C18 weak-MFE channel plateau:
  channel label exists
  + MFE_30D < +10%
  + MAE_90D approaches -20%
  + no reorder proof
  => block Green, cap Stage2, or route to local 4B watch
```

`280360` and `001680` prevent overblocking.  
`271560` shows why a brand/channel label alone should not be promoted when post-entry MFE stays weak.

---

## 9. Aggregate metrics

```json
{
  "row_type": "aggregate",
  "research_id": "R5L74_C18_KFOOD_EXPORT_CHANNEL_ROUTER",
  "round": "R5",
  "loop": 74,
  "large_sector_id": "L5_CONSUMER_BRAND_DISTRIBUTION",
  "canonical_archetype_id": "C18_CONSUMER_EXPORT_CHANNEL_REORDER",
  "fine_archetype_id": "KFOOD_SNACK_CONFECTIONERY_EXPORT_CHANNEL_REORDER_AND_WEAK_MFE_ROUTER",
  "case_count": 3,
  "calibration_usable_case_count": 3,
  "positive_case_count": 2,
  "counterexample_count": 1,
  "new_symbol_count": 3,
  "source_proxy_only_count": 3,
  "evidence_url_pending_count": 3,
  "avg_mfe_30d_pct": 13.11,
  "avg_mae_30d_pct": -3.88,
  "avg_mfe_90d_pct": 38.47,
  "avg_mae_90d_pct": -6.67,
  "avg_mfe_180d_pct": 38.47,
  "avg_mae_180d_pct": -8.77,
  "max_mfe_180d_pct": 61.88,
  "worst_mae_180d_pct": -17.37
}
```

---

## 10. 4B proximity split

```json
{
  "row_type": "4b_split",
  "research_id": "R5L74_C18_KFOOD_EXPORT_CHANNEL_ROUTER",
  "stage2_positive_or_yellow_candidate": [
    {
      "symbol": "280360",
      "reason": "persistent +61.88% 180D MFE with only -1.71% MAE; requires export-channel reorder and margin evidence before Green"
    },
    {
      "symbol": "001680",
      "reason": "strong +45.75% 180D MFE with manageable -7.22% MAE; requires K-food export/reorder bridge repair"
    }
  ],
  "blocked_stage2_or_local_4b_watch": [
    {
      "symbol": "271560",
      "reason": "MFE stayed below +10% while 90D/180D MAE reached -17.37%; channel label did not convert into return/risk alignment"
    }
  ],
  "full_4b_or_green_requires_non_price_evidence": [
    "export shipment and channel expansion",
    "distributor reorder / repeat order",
    "sell-through and channel inventory",
    "ASP / product mix improvement",
    "gross margin / operating leverage conversion"
  ]
}
```

---

## 11. Shadow rule candidate

```yaml
row_type: canonical_archetype_rule_candidate
canonical_archetype_id: C18_CONSUMER_EXPORT_CHANNEL_REORDER
fine_archetype_id: KFOOD_SNACK_CONFECTIONERY_EXPORT_CHANNEL_REORDER_AND_WEAK_MFE_ROUTER
rule_name: C18_kfood_export_channel_reorder_and_weak_mfe_router
production_scoring_changed: false
shadow_weight_only: true
```

### Proposed routing logic

```text
For C18 consumer export / channel reorder cases:

Tier A: verified reorder-driven export winner
  Conditions:
    - export/channel relevance is clear
    - distributor reorder, sell-through, and margin evidence are URL-repaired
    - 30D/90D MAE remains contained
    - MFE persists beyond a single theme candle
  Routing:
    - Stage2-Actionable allowed
    - Stage3-Yellow allowed after evidence repair
    - Green only after reorder and margin conversion are verified

Tier B: source-proxy-only K-food export rerating
  Conditions:
    - K-food / confectionery export theme is plausible
    - price path has strong MFE and manageable MAE
    - evidence_url_pending or source_proxy_only remains true
  Routing:
    - Stage2-Actionable-Guarded at most
    - no Green
    - no production positive weight promotion

Tier C: weak-MFE overseas-channel plateau
  Conditions:
    - MFE_30D < +10%
    - MAE_90D <= -15%
    - reorder / sell-through / margin bridge is missing
  Routing:
    - block Green
    - block Stage2 or cap at Stage2-Guarded
    - local 4B watch if drawdown expands
```

### Suggested shadow delta

```json
{
  "row_type": "shadow_weight",
  "axis": "c18_kfood_export_channel_reorder_and_weak_mfe_router",
  "scope": "canonical_archetype_id:C18_CONSUMER_EXPORT_CHANNEL_REORDER",
  "proposal": {
    "source_proxy_only_green_allowed": false,
    "export_reorder_sellthrough_margin_bridge_required_for_green": true,
    "stage2_guarded_allowed_for_strong_mfe_contained_mae": true,
    "weak_mfe_threshold_30d_pct": 10.0,
    "weak_mfe_mae_watch_threshold_90d_pct": -15.0,
    "positive_weight_blocked_until_url_repair": true
  },
  "confidence": "medium_low_until_url_repair",
  "apply_now": false,
  "reason": "Two strong K-food/confectionery export-channel paths and one weak-MFE overseas-channel plateau show that C18 should preserve reorder-driven winners but require URL-repaired export/reorder/sell-through/margin evidence before Yellow/Green."
}
```

---

## 12. Residual contribution summary

```json
{
  "row_type": "residual_contribution",
  "research_id": "R5L74_C18_KFOOD_EXPORT_CHANNEL_ROUTER",
  "large_sector_id": "L5_CONSUMER_BRAND_DISTRIBUTION",
  "canonical_archetype_id": "C18_CONSUMER_EXPORT_CHANNEL_REORDER",
  "contribution": "Adds three non-top-covered C18 K-food / snack / confectionery export-channel cases and separates clean reorder-driven low-MAE rerating from weak-MFE overseas-channel plateau. C18 Green should require URL-repaired export shipment, distributor reorder, sell-through, channel inventory, ASP/mix, and margin evidence.",
  "positive_case_added": 2,
  "counterexample_case_added": 1,
  "new_symbol_count": 3,
  "data_quality_blocker": "All three non-price export/channel triggers require URL-level repair before positive weight promotion.",
  "guardrail_added": "C18 source_proxy_only cases with MFE_30D < +10% and MAE_90D <= -15% should block Green and either block Stage2 or remain Stage2-Guarded until reorder evidence is repaired."
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
    001680: false
    280360: false
    271560: false
  evidence_url_pending:
    001680: true
    280360: true
    271560: true
  source_proxy_only:
    001680: true
    280360: true
    271560: true
```

Limitations:

```text
- Price path is validated against Stock-Web tradable OHLC rows.
- Non-price evidence is not URL-repaired in this run.
- Therefore this artifact is useful for C18 consumer export/channel reorder residual shape and weak-MFE guardrail design, but should not promote positive weights until filings/IR/customs/channel/report data verifies export shipment, distributor reorder, sell-through, channel inventory, ASP/mix, and margin conversion.
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
2. Preserve R5 / loop 74 metadata.
3. Add the cases to C18_CONSUMER_EXPORT_CHANNEL_REORDER only if parser validation passes.
4. Treat all three non-price triggers as evidence_url_pending=true and source_proxy_only=true until URL-level evidence is repaired.
5. Do not use these rows for positive weight promotion until filings/IR/customs/channel/report data verifies export shipment, distributor reorder, sell-through, channel inventory, ASP/mix, and margin conversion.
6. Add a shadow-only rule candidate named C18_kfood_export_channel_reorder_and_weak_mfe_router.
7. Do not loosen Stage3-Green.
8. Add C18-specific guards:
   - source_proxy_only -> no Green
   - Green requires repaired export/reorder/sell-through/margin bridge
   - strong MFE with contained MAE may stay Stage2-Guarded until evidence repair
   - MFE_30D < +10% and MAE_90D <= -15% without reorder evidence -> block Green and cap or block Stage2
9. Keep production scoring unchanged unless later batch promotion logic independently marks this axis safe.
```

---

## 15. Next round state

```text
completed_round = R5
completed_loop = 74
next_round = R6
next_loop = 74
next_large_sector_hint = L6_FINANCIAL_CAPITAL_RETURN_DIGITAL
```
