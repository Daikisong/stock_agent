# E2R Stock-Web v12 Residual Research — R5 Loop 75

```yaml
research_session: post_calibrated_sector_archetype_residual_research
mode: historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12
completed_round: R5
completed_loop: 75
next_round: R6
next_loop: 75
large_sector_id: L5_CONSUMER_BRAND_DISTRIBUTION
canonical_archetype_id: C19_BRAND_RETAIL_INVENTORY_MARGIN
fine_archetype_id: APPAREL_ATHLEISURE_BRAND_INVENTORY_DESTOCK_MARGIN_AND_WEAK_MFE_ROUTER
output_file: e2r_stock_web_v12_residual_round_R5_loop_75_L5_CONSUMER_BRAND_DISTRIBUTION_C19_BRAND_RETAIL_INVENTORY_MARGIN_research.md
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
completed_loop  = 75
large_sector_id = L4_MATERIALS_SPREAD_RESOURCE
canonical_archetype_id = C16_STRATEGIC_RESOURCE_POLICY_SUPPLY
```

Therefore:

```text
scheduled_round = R5
scheduled_loop  = 75
```

R5 maps to:

```text
large_sector_id = L5_CONSUMER_BRAND_DISTRIBUTION
```

This run selects:

```text
canonical_archetype_id = C19_BRAND_RETAIL_INVENTORY_MARGIN
fine_archetype_id = APPAREL_ATHLEISURE_BRAND_INVENTORY_DESTOCK_MARGIN_AND_WEAK_MFE_ROUTER
```

This is a valid R5/L5 pairing.

---

## 1. Why this R5/C19 run

The no-repeat ledger shows C19 has materially fewer symbols than the broader C18/C20 consumer/export buckets:

```text
C19_BRAND_RETAIL_INVENTORY_MARGIN:
  rows: 68
  symbols: 13
  date_range: 2021-05-17~2024-10-16
  good/bad S2: 15/14
  4B/4C: 16/7
  URL/proxy: 0/4
  top covered symbols: 383220(9), 111770(8), UNKNOWN_SYMBOL(8), 036620(7), 081660(7), 298540(7)
```

This file avoids those top-covered symbols and adds three apparel/athleisure/premium-brand inventory-margin names:

```text
337930 브랜드엑스코퍼레이션/젝시믹스
093050 LF
020000 한섬
```

Research question:

```text
Can C19 separate real apparel / athleisure inventory-destock margin rerating from premium-apparel relief entries where inventory-margin relevance exists but sell-through and gross-margin evidence are not durable enough?
```

C19 is an inventory-margin archetype. Inventory is like water behind a dam: destocking can release margin pressure, but only if sell-through improves and price discipline holds. If the channel is still clogged, the first bounce is just water hitting the gate.

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
| `337930` | 브랜드엑스코퍼레이션/젝시믹스 | active_like / KOSDAQ | no 2024 overlap; latest listed candidate 2021-09-23 | true |
| `093050` | LF | active_like / KOSPI | none listed | true |
| `020000` | 한섬 | active_like / KOSPI | no 2024 overlap; latest listed candidate 2008-01-16 | true |

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
The Stock-Web price path is fully validated, but company-level inventory balance, sell-through, markdown pressure, online/offline channel mix, athleisure demand, product-cycle durability, gross margin, and operating leverage evidence still require later URL repair through filings, IR decks, channel data, or sell-side reports before production weight promotion.
```

C19 interpretation used here:

```text
C19 is not simply “apparel stock bounced.”
It asks whether brand retail inventory pressure converts into margin:
- inventory days and markdown risk,
- sell-through and channel inventory,
- product mix and ASP,
- online/offline channel efficiency,
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
093050 + C19_BRAND_RETAIL_INVENTORY_MARGIN -> no direct match found
020000 + C19_BRAND_RETAIL_INVENTORY_MARGIN -> no direct match found
337930 + C19_BRAND_RETAIL_INVENTORY_MARGIN -> no direct match found
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
| `R5L75_C19_337930_20240529` | `337930` 브랜드엑스코퍼레이션/젝시믹스 | athleisure brand inventory-destock / margin leverage | positive anchor |
| `R5L75_C19_093050_20240308` | `093050` LF | apparel brand inventory-destock / low-MAE margin rerating | positive-guarded |
| `R5L75_C19_020000_20240208` | `020000` 한섬 | premium apparel inventory-margin relief with weak MFE | weak-MFE drawdown counterexample |

The intended residual:

```text
C19 should separate:
1. athleisure/brand cases where sell-through and margin leverage create persistent MFE;
2. apparel inventory-destock paths where MFE is moderate and MAE remains contained;
3. premium-apparel relief entries where the first spike is already capped and the forward path fails to rerate.
```

---

## 6. Stock-Web OHLC and backtest

### 6.1 `337930` 브랜드엑스코퍼레이션/젝시믹스 — athleisure inventory-destock / margin leverage rerating

Trigger:

```text
trigger_date = 2024-05-28
trigger_type = Stage2-Actionable
trigger_family = athleisure_brand_inventory_destock_margin_operating_leverage_rerating
entry_date = 2024-05-29
entry_price = 5120.0
entry_price_type = next_tradable_open_after_athleisure_brand_margin_burst
```

Relevant Stock-Web rows:

```csv
d,o,h,l,c,v,a,mc,s,m
2024-05-28,4985.0,5170.0,4985.0,5120.0,149762.0,762446685.0,149844935680.0,29266589,KOSDAQ
2024-05-29,5120.0,5840.0,5090.0,5750.0,1093903.0,6077965470.0,168282886750.0,29266589,KOSDAQ
2024-05-31,5680.0,6280.0,5660.0,5960.0,2018929.0,12213770740.0,174428870440.0,29266589,KOSDAQ
2024-06-24,5960.0,6900.0,5850.0,6330.0,6362602.0,41601048290.0,185257508370.0,29266589,KOSDAQ
2024-06-28,6800.0,7170.0,6700.0,6950.0,1150463.0,7997790830.0,203402793550.0,29266589,KOSDAQ
2024-07-10,8270.0,9140.0,8180.0,8520.0,3269645.0,28381894490.0,249734380440.0,29311547,KOSDAQ
2024-08-09,10820.0,12280.0,10780.0,11430.0,12992643.0,149626887540.0,335030982210.0,29311547,KOSDAQ
2024-10-07,12540.0,13380.0,11700.0,11880.0,2331468.0,29446166650.0,348221178360.0,29311547,KOSDAQ
```

Backtest:

| window | peak/high | peak date | trough/low | trough date | MFE | MAE |
|---|---:|---|---:|---|---:|---:|
| 30 calendar days | 7170 | 2024-06-28 | 5090 | 2024-05-29 | +40.04% | -0.59% |
| 90 calendar days | 12280 | 2024-08-09 | 5090 | 2024-05-29 | +139.84% | -0.59% |
| 180 calendar days | 13380 | 2024-10-07 | 5090 | 2024-05-29 | +161.33% | -0.59% |

Interpretation:

```text
337930 is the C19 positive anchor.
The forward path had large and persistent MFE with almost no MAE from the selected next-open entry.
It can support Stage2-Actionable / Yellow after evidence repair, but Green still requires URL-repaired inventory, sell-through, channel, and margin evidence.
```

### 6.2 `093050` LF — apparel inventory-destock / low-MAE margin rerating

Trigger:

```text
trigger_date = 2024-03-07
trigger_type = Stage2-Actionable-Guarded
trigger_family = apparel_brand_inventory_destock_margin_low_mae_rerating
entry_date = 2024-03-08
entry_price = 13650.0
entry_price_type = next_tradable_open_after_apparel_inventory_margin_burst
```

Relevant Stock-Web rows:

```csv
d,o,h,l,c,v,a,mc,s,m
2024-03-07,13150.0,13840.0,13120.0,13640.0,202428.0,2731199640.0,398833600000.0,29240000,KOSPI
2024-03-08,13650.0,14240.0,13530.0,14170.0,140730.0,1967116490.0,414330800000.0,29240000,KOSPI
2024-03-28,15600.0,15920.0,15350.0,15400.0,84677.0,1315191090.0,450296000000.0,29240000,KOSPI
2024-05-17,16400.0,16710.0,16360.0,16420.0,40843.0,675577820.0,480120800000.0,29240000,KOSPI
2024-06-25,14450.0,14450.0,13740.0,13860.0,161882.0,2267087000.0,405266400000.0,29240000,KOSPI
2024-08-05,14220.0,14220.0,13090.0,13180.0,118446.0,1600057190.0,385383200000.0,29240000,KOSPI
2024-09-09,14390.0,14940.0,14360.0,14940.0,109744.0,1610913160.0,436845600000.0,29240000,KOSPI
```

Backtest:

| window | peak/high | peak date | trough/low | trough date | MFE | MAE |
|---|---:|---|---:|---|---:|---:|
| 30 calendar days | 15920 | 2024-03-28 | 13530 | 2024-03-08 | +16.63% | -0.88% |
| 90 calendar days | 16710 | 2024-05-17 | 13530 | 2024-03-08 | +22.42% | -0.88% |
| 180 calendar days | 16710 | 2024-05-17 | 13090 | 2024-08-05 | +22.42% | -4.10% |

Interpretation:

```text
093050 is a positive-guarded apparel case.
The MFE was moderate rather than explosive, but the path stayed low-MAE.
This should remain Stage2-Guarded / Yellow candidate after inventory, channel sell-through, and margin bridge evidence is repaired.
```

### 6.3 `020000` 한섬 — premium apparel relief with weak MFE and drawdown

Trigger:

```text
trigger_date = 2024-02-07
trigger_type = Stage2-FalsePositive-Candidate
trigger_family = premium_apparel_inventory_margin_relief_weak_mfe_drawdown
entry_date = 2024-02-08
entry_price = 21550.0
entry_price_type = next_tradable_open_after_premium_apparel_relief
```

Relevant Stock-Web rows:

```csv
d,o,h,l,c,v,a,mc,s,m
2024-02-07,20100.0,21650.0,20050.0,21550.0,282915.0,5943063900.0,530776500000.0,24630000,KOSPI
2024-02-08,21550.0,21650.0,20750.0,20950.0,140411.0,2959049400.0,515998500000.0,24630000,KOSPI
2024-03-04,19110.0,19200.0,18810.0,18970.0,71832.0,1363215080.0,467231100000.0,24630000,KOSPI
2024-04-08,19080.0,19150.0,18880.0,18890.0,38454.0,729702360.0,441997665000.0,23398500,KOSPI
2024-06-25,17620.0,17690.0,17590.0,17590.0,45323.0,799735070.0,411579615000.0,23398500,KOSPI
2024-08-05,17100.0,17180.0,15640.0,16290.0,102686.0,1685526280.0,381161565000.0,23398500,KOSPI
2024-09-06,16220.0,16250.0,15820.0,15940.0,29816.0,474760760.0,372972090000.0,23398500,KOSPI
```

Backtest:

| window | peak/high | peak date | trough/low | trough date | MFE | MAE |
|---|---:|---|---:|---|---:|---:|
| 30 calendar days | 21650 | 2024-02-08 | 18810 | 2024-03-04 | +0.46% | -12.71% |
| 90 calendar days | 21650 | 2024-02-08 | 18810 | 2024-03-04 | +0.46% | -12.71% |
| 180 calendar days | 21650 | 2024-02-08 | 15640 | 2024-08-05 | +0.46% | -27.42% |

Interpretation:

```text
020000 is the weak-MFE C19 counterexample.
The premium-apparel relief label existed, but the selected next-open entry had almost no forward MFE and later drew down materially.
This should block Green and usually block Stage2 unless fresh inventory sell-through and gross-margin evidence appears before entry.
```

---

## 7. Machine-readable trigger JSONL

```jsonl
{"row_type":"trigger","research_id":"R5L75_C19_APPAREL_INVENTORY_MARGIN_ROUTER","round":"R5","loop":75,"large_sector_id":"L5_CONSUMER_BRAND_DISTRIBUTION","canonical_archetype_id":"C19_BRAND_RETAIL_INVENTORY_MARGIN","fine_archetype_id":"APPAREL_ATHLEISURE_BRAND_INVENTORY_DESTOCK_MARGIN_AND_WEAK_MFE_ROUTER","symbol":"337930","name":"브랜드엑스코퍼레이션/젝시믹스","trigger_type":"Stage2-Actionable","trigger_family":"athleisure_brand_inventory_destock_margin_operating_leverage_rerating","trigger_date":"2024-05-28","entry_date":"2024-05-29","entry_price":5120.0,"entry_price_type":"next_tradable_open_after_athleisure_brand_margin_burst","price_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","mfe_30d_pct":40.04,"mae_30d_pct":-0.59,"mfe_90d_pct":139.84,"mae_90d_pct":-0.59,"mfe_180d_pct":161.33,"mae_180d_pct":-0.59,"peak_price_180d":13380.0,"peak_date_180d":"2024-10-07","trough_price_180d":5090.0,"trough_date_180d":"2024-05-29","calibration_usable":true,"case_polarity":"positive_anchor_low_mae_brand_margin","evidence_url_pending":true,"source_proxy_only":true,"non_price_evidence_strength":"medium_pending_url_repair","price_only_blowoff":false,"expected_stage_current_profile":"Stage2-Actionable_to_Yellow_after_inventory_destock_sellthrough_margin_bridge_repaired","residual_error_type":"positive_athleisure_brand_margin_path_requires_url_repaired_inventory_sellthrough_channel_margin_bridge_before_green"}
{"row_type":"trigger","research_id":"R5L75_C19_APPAREL_INVENTORY_MARGIN_ROUTER","round":"R5","loop":75,"large_sector_id":"L5_CONSUMER_BRAND_DISTRIBUTION","canonical_archetype_id":"C19_BRAND_RETAIL_INVENTORY_MARGIN","fine_archetype_id":"APPAREL_ATHLEISURE_BRAND_INVENTORY_DESTOCK_MARGIN_AND_WEAK_MFE_ROUTER","symbol":"093050","name":"LF","trigger_type":"Stage2-Actionable-Guarded","trigger_family":"apparel_brand_inventory_destock_margin_low_mae_rerating","trigger_date":"2024-03-07","entry_date":"2024-03-08","entry_price":13650.0,"entry_price_type":"next_tradable_open_after_apparel_inventory_margin_burst","price_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","mfe_30d_pct":16.63,"mae_30d_pct":-0.88,"mfe_90d_pct":22.42,"mae_90d_pct":-0.88,"mfe_180d_pct":22.42,"mae_180d_pct":-4.1,"peak_price_180d":16710.0,"peak_date_180d":"2024-05-17","trough_price_180d":13090.0,"trough_date_180d":"2024-08-05","calibration_usable":true,"case_polarity":"positive_guarded_low_mae","evidence_url_pending":true,"source_proxy_only":true,"non_price_evidence_strength":"medium_low_pending_url_repair","price_only_blowoff":false,"expected_stage_current_profile":"Stage2-Guarded_to_Yellow_if_inventory_margin_and_channel_sellthrough_bridge_repaired","residual_error_type":"apparel_destock_margin_path_worked_but_green_requires_inventory_sellthrough_and_margin_evidence"}
{"row_type":"trigger","research_id":"R5L75_C19_APPAREL_INVENTORY_MARGIN_ROUTER","round":"R5","loop":75,"large_sector_id":"L5_CONSUMER_BRAND_DISTRIBUTION","canonical_archetype_id":"C19_BRAND_RETAIL_INVENTORY_MARGIN","fine_archetype_id":"APPAREL_ATHLEISURE_BRAND_INVENTORY_DESTOCK_MARGIN_AND_WEAK_MFE_ROUTER","symbol":"020000","name":"한섬","trigger_type":"Stage2-FalsePositive-Candidate","trigger_family":"premium_apparel_inventory_margin_relief_weak_mfe_drawdown","trigger_date":"2024-02-07","entry_date":"2024-02-08","entry_price":21550.0,"entry_price_type":"next_tradable_open_after_premium_apparel_relief","price_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","mfe_30d_pct":0.46,"mae_30d_pct":-12.71,"mfe_90d_pct":0.46,"mae_90d_pct":-12.71,"mfe_180d_pct":0.46,"mae_180d_pct":-27.42,"peak_price_180d":21650.0,"peak_date_180d":"2024-02-08","trough_price_180d":15640.0,"trough_date_180d":"2024-08-05","calibration_usable":true,"case_polarity":"counterexample_weak_mfe_drawdown","evidence_url_pending":true,"source_proxy_only":true,"non_price_evidence_strength":"low_pending_url_repair","price_only_blowoff":false,"expected_stage_current_profile":"blocked_Stage2_or_Stage2_Guarded_until_inventory_margin_bridge_repaired","residual_error_type":"premium_apparel_inventory_margin_label_had_almost_no_mfe_and_180d_drawdown_without_sellthrough_margin_bridge"}
```

---

## 8. Score simulation and raw component breakdown

This is shadow-only and does not change production scoring.

| symbol | inventory destock | sell-through / channel | brand demand | market mispricing | valuation rerating | gross / operating margin bridge | information confidence | shadow total | intended route |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| `337930` | 14 | 13 | 13 | 15 | 15 | 13 | 6 | 89 | Stage2/Yellow after evidence repair; Green only after hard bridge |
| `093050` | 11 | 9 | 8 | 9 | 9 | 8 | 6 | 60 | Stage2-Guarded / Yellow after sell-through and margin evidence repair |
| `020000` | 4 | 3 | 5 | 2 | 2 | 3 | 5 | 24 | blocked Stage2 or Stage2-Guarded only after fresh bridge |

### Current calibrated profile stress test

The current calibrated profile already blocks pure price-only blowoff.  
The remaining C19 issue is **inventory-margin label without sell-through conversion**:

```text
C19 clean brand-margin path:
  inventory destock / margin relevance
  + MFE expands across 90D/180D
  + MAE remains contained
  + URL-repaired sell-through / channel / margin bridge
  => Stage2-Actionable / Yellow, possible Green after proof

C19 positive-guarded apparel path:
  inventory-margin setup is plausible
  + MFE is moderate
  + MAE remains low
  + evidence remains source_proxy_only
  => Stage2-Guarded, no Green

C19 weak-MFE premium apparel path:
  inventory-margin label exists
  + MFE_30D < +5%
  + MAE_180D <= -25%
  + no sell-through / gross-margin bridge
  => block Green and usually block Stage2
```

`337930` and `093050` prevent overblocking.  
`020000` shows why apparel inventory-margin relevance alone cannot create positive-stage promotion.

---

## 9. Aggregate metrics

```json
{
  "row_type": "aggregate",
  "research_id": "R5L75_C19_APPAREL_INVENTORY_MARGIN_ROUTER",
  "round": "R5",
  "loop": 75,
  "large_sector_id": "L5_CONSUMER_BRAND_DISTRIBUTION",
  "canonical_archetype_id": "C19_BRAND_RETAIL_INVENTORY_MARGIN",
  "fine_archetype_id": "APPAREL_ATHLEISURE_BRAND_INVENTORY_DESTOCK_MARGIN_AND_WEAK_MFE_ROUTER",
  "case_count": 3,
  "calibration_usable_case_count": 3,
  "positive_case_count": 2,
  "counterexample_count": 1,
  "new_symbol_count": 3,
  "source_proxy_only_count": 3,
  "evidence_url_pending_count": 3,
  "avg_mfe_30d_pct": 19.04,
  "avg_mae_30d_pct": -4.73,
  "avg_mfe_90d_pct": 54.24,
  "avg_mae_90d_pct": -4.73,
  "avg_mfe_180d_pct": 61.4,
  "avg_mae_180d_pct": -10.7,
  "max_mfe_180d_pct": 161.33,
  "worst_mae_180d_pct": -27.42
}
```

---

## 10. 4B proximity split

```json
{
  "row_type": "4b_split",
  "research_id": "R5L75_C19_APPAREL_INVENTORY_MARGIN_ROUTER",
  "stage2_positive_or_yellow_candidate": [
    {
      "symbol": "337930",
      "reason": "athleisure brand path had +161.33% 180D MFE with only -0.59% MAE"
    },
    {
      "symbol": "093050",
      "reason": "apparel inventory-destock path had +22.42% 180D MFE with only -4.10% MAE"
    }
  ],
  "blocked_stage2_or_local_4b_watch": [
    {
      "symbol": "020000",
      "reason": "premium-apparel relief entry had only +0.46% MFE and -27.42% 180D MAE"
    }
  ],
  "full_4b_or_green_requires_non_price_evidence": [
    "inventory days and markdown-risk reduction",
    "sell-through and channel inventory",
    "brand demand and product mix",
    "online/offline channel efficiency",
    "gross margin and operating leverage conversion"
  ]
}
```

---

## 11. Shadow rule candidate

```yaml
row_type: canonical_archetype_rule_candidate
canonical_archetype_id: C19_BRAND_RETAIL_INVENTORY_MARGIN
fine_archetype_id: APPAREL_ATHLEISURE_BRAND_INVENTORY_DESTOCK_MARGIN_AND_WEAK_MFE_ROUTER
rule_name: C19_apparel_athleisure_inventory_margin_sellthrough_and_weak_mfe_router
production_scoring_changed: false
shadow_weight_only: true
```

### Proposed routing logic

```text
For C19 apparel / brand retail / athleisure inventory-margin cases:

Tier A: verified brand inventory-margin winner
  Conditions:
    - inventory destock, sell-through, channel inventory, and gross-margin evidence are URL-repaired
    - MFE_90D >= +25%
    - MAE_90D > -10%
    - MFE persists beyond one earnings/theme candle
  Routing:
    - Stage2-Actionable allowed
    - Stage3-Yellow allowed after evidence repair
    - Green only after inventory and margin bridge are verified

Tier B: low-MAE apparel margin repair
  Conditions:
    - MFE_90D >= +15%
    - MAE_180D > -10%
    - evidence_url_pending or source_proxy_only remains true
  Routing:
    - Stage2-Guarded allowed
    - no Green until evidence repair

Tier C: weak-MFE premium apparel relief
  Conditions:
    - MFE_30D < +5%
    - MAE_180D <= -25%
    - no repaired sell-through / margin evidence
  Routing:
    - block Green
    - block Stage2 or local 4B watch
    - count as counterexample
```

### Suggested shadow delta

```json
{
  "row_type": "shadow_weight",
  "axis": "c19_apparel_athleisure_inventory_margin_sellthrough_and_weak_mfe_router",
  "scope": "canonical_archetype_id:C19_BRAND_RETAIL_INVENTORY_MARGIN",
  "proposal": {
    "source_proxy_only_green_allowed": false,
    "inventory_sellthrough_margin_bridge_required_for_green": true,
    "verified_brand_winner_mfe90_threshold_pct": 25.0,
    "verified_brand_winner_mae90_min_pct": -10.0,
    "low_mae_guarded_mfe90_threshold_pct": 15.0,
    "low_mae_guarded_mae180_min_pct": -10.0,
    "weak_mfe_threshold_30d_pct": 5.0,
    "weak_mfe_hard_mae_threshold_180d_pct": -25.0,
    "positive_weight_blocked_until_url_repair": true
  },
  "confidence": "medium_low_until_url_repair",
  "apply_now": false,
  "reason": "Two non-top-covered apparel/athleisure low-MAE winners and one premium-apparel weak-MFE drawdown counterexample show that C19 should require URL-repaired inventory, sell-through, channel, and margin evidence before Yellow/Green."
}
```

---

## 12. Residual contribution summary

```json
{
  "row_type": "residual_contribution",
  "research_id": "R5L75_C19_APPAREL_INVENTORY_MARGIN_ROUTER",
  "large_sector_id": "L5_CONSUMER_BRAND_DISTRIBUTION",
  "canonical_archetype_id": "C19_BRAND_RETAIL_INVENTORY_MARGIN",
  "contribution": "Adds three non-top-covered C19 apparel/athleisure/premium-brand inventory-margin cases and separates strong low-MAE brand-margin rerating from weak-MFE premium-apparel relief failure. C19 Yellow/Green should require URL-repaired inventory destock, sell-through, channel inventory, markdown-risk, product mix, and gross/operating-margin evidence.",
  "positive_case_added": 2,
  "counterexample_case_added": 1,
  "new_symbol_count": 3,
  "new_independent_case_count": 3,
  "reused_case_count": 0,
  "same_archetype_new_symbol_count": 3,
  "same_archetype_new_trigger_family_count": 3,
  "new_trigger_family_count": 3,
  "current_profile_error_count": 1,
  "diversity_score_summary": {
    "new_symbol_bonus": 9,
    "counterexample_gap_bonus": 4,
    "residual_error_bonus": 5,
    "wrong_round_penalty": 0,
    "repeated_same_symbol_penalty": 0,
    "net_interpretive_score": 18
  },
  "loop_contribution_label": "canonical_archetype_rule_candidate",
  "do_not_propose_new_weight_delta": false,
  "data_quality_blocker": "All three non-price apparel/brand inventory-margin triggers require URL-level repair before positive weight promotion.",
  "guardrail_added": "C19 source_proxy_only apparel cases with MFE_30D < +5% and MAE_180D <= -25% should block Green and usually block Stage2; low-MAE MFE paths may remain Stage2-Guarded until inventory/sell-through/margin evidence is repaired."
}
```

One-line contribution:

```text
This loop adds 3 new independent cases, 1 counterexamples, and 1 residual errors for R5/L5_CONSUMER_BRAND_DISTRIBUTION/C19_BRAND_RETAIL_INVENTORY_MARGIN.
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
    337930: false
    093050: false
    020000: false
  evidence_url_pending:
    337930: true
    093050: true
    020000: true
  source_proxy_only:
    337930: true
    093050: true
    020000: true
```

Limitations:

```text
- Price path is validated against Stock-Web tradable OHLC rows.
- Non-price evidence is not URL-repaired in this run.
- Therefore this artifact is useful for C19 apparel/brand retail inventory-margin residual shape and weak-MFE guardrail design, but should not promote positive weights until filings, IR, channel data, or reports verify inventory, sell-through, markdown pressure, channel mix, product mix, and margin conversion.
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
2. Preserve R5 / loop 75 metadata.
3. Add the cases to C19_BRAND_RETAIL_INVENTORY_MARGIN only if parser validation passes.
4. Treat all three non-price triggers as evidence_url_pending=true and source_proxy_only=true until URL-level evidence is repaired.
5. Do not use these rows for positive weight promotion until filings/IR/channel-data/report data verifies inventory destock, sell-through, channel inventory, markdown risk, product mix, gross margin, and operating leverage.
6. Add a shadow-only rule candidate named C19_apparel_athleisure_inventory_margin_sellthrough_and_weak_mfe_router.
7. Do not loosen Stage3-Green.
8. Add C19-specific guards:
   - source_proxy_only -> no Green
   - Green requires repaired inventory / sell-through / channel / margin bridge
   - MFE_90D >= +25% and MAE_90D > -10% may remain Stage2-Actionable/Yellow watch after evidence repair
   - MFE_90D >= +15% and MAE_180D > -10% may remain Stage2-Guarded while evidence is pending
   - MFE_30D < +5% and MAE_180D <= -25% -> block Green and usually block Stage2 / local 4B watch
9. Keep production scoring unchanged unless later batch promotion logic independently marks this axis safe.
```

---

## 15. Next round state

```text
completed_round = R5
completed_loop = 75
next_round = R6
next_loop = 75
next_large_sector_hint = L6_FINANCIAL_CAPITAL_RETURN_DIGITAL
round_schedule_status = valid
round_sector_consistency = pass
```
