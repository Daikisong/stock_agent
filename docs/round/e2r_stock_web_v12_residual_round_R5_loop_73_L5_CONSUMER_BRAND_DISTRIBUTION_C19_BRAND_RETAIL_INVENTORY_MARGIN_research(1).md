# E2R Stock-Web v12 Residual Research — R5 Loop 73

```yaml
research_session: post_calibrated_sector_archetype_residual_research
mode: historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12
completed_round: R5
completed_loop: 73
next_round: R6
next_loop: 73
large_sector_id: L5_CONSUMER_BRAND_DISTRIBUTION
canonical_archetype_id: C19_BRAND_RETAIL_INVENTORY_MARGIN
fine_archetype_id: RETAIL_MARGIN_RECOVERY_DUTYFREE_INVENTORY_AND_DEPARTMENT_STORE_HIGH_MAE_ROUTER
output_file: e2r_stock_web_v12_residual_round_R5_loop_73_L5_CONSUMER_BRAND_DISTRIBUTION_C19_BRAND_RETAIL_INVENTORY_MARGIN_research.md
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
completed_loop  = 73
large_sector_id = L4_MATERIALS_SPREAD_RESOURCE
canonical_archetype_id = C16_STRATEGIC_RESOURCE_POLICY_SUPPLY
```

Therefore:

```text
scheduled_round = R5
scheduled_loop  = 73
```

R5 maps to:

```text
large_sector_id = L5_CONSUMER_BRAND_DISTRIBUTION
```

This run selects:

```text
canonical_archetype_id = C19_BRAND_RETAIL_INVENTORY_MARGIN
fine_archetype_id = RETAIL_MARGIN_RECOVERY_DUTYFREE_INVENTORY_AND_DEPARTMENT_STORE_HIGH_MAE_ROUTER
```

This is a valid R5/L5 pairing.

---

## 1. Why this R5/C19 run

The no-repeat ledger shows C19 is already covered, but it is concentrated in a few brand and retail/inventory names:

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

This file deliberately avoids those top-covered names and adds three retail/distribution cases:

```text
282330 BGF리테일
008770 호텔신라
004170 신세계
```

Research question:

```text
Can C19 separate defensive retail-margin stabilization from duty-free / department-store relief rallies where inventory, traffic, mix, or China-spend assumptions fail to convert into durable margin?
```

C19 is a retail operating-leverage archetype. A retailer can look like a simple “same-store-sales recovery” chart, but the real engine is stock-to-sell-through-to-gross-margin conversion. If traffic improves but inventory or channel mix is wrong, the margin engine coughs. The model should hear that misfire before it gives Green.

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
| `282330` | BGF리테일 | active_like / KOSPI | none listed | true |
| `008770` | 호텔신라 | active_like / KOSPI | no 2024 overlap; old 1999 candidates only | true |
| `004170` | 신세계 | active_like / KOSPI | no 2024 overlap; old 1996/2004/2011 candidates only | true |

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
The Stock-Web price path is fully validated, but company-level same-store-sales, inventory quality, gross-margin, duty-free mix, tourist traffic, department-store transaction value, and operating-leverage evidence still require later URL repair through filings, IR decks, disclosure data, or sell-side reports before production weight promotion.
```

C19 interpretation used here:

```text
C19 is not simply “retail stock bounced.”
It asks whether brand/retail recovery is margin-convertible:
- inventory clearance or inventory quality,
- channel traffic and sell-through,
- gross margin and operating leverage,
- duty-free / department-store mix,
- and durable earnings bridge.
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
282330 + C19_BRAND_RETAIL_INVENTORY_MARGIN -> no direct match found
008770 + C19_BRAND_RETAIL_INVENTORY_MARGIN -> no direct match found
004170 + C19_BRAND_RETAIL_INVENTORY_MARGIN -> no direct match found
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
| `R5L73_C19_282330_20240401` | `282330` BGF리테일 | convenience-store defensive retail margin stabilization | positive-guarded / low-MAE early path |
| `R5L73_C19_008770_20240715` | `008770` 호텔신라 | duty-free / tourism retail margin fade | counterexample / low-MFE high-MAE path |
| `R5L73_C19_004170_20240927` | `004170` 신세계 | department-store / duty-free relief rally after stimulus/mix optimism | counterexample / delayed high-MAE path |

The intended residual:

```text
C19 should separate:
1. defensive retail-margin stabilization with contained early MAE;
2. duty-free or department-store relief rallies where traffic/mix assumptions do not convert into margin;
3. post-rally retail entries where low MFE and later MAE should block Stage2/Green.
```

---

## 6. Stock-Web OHLC and backtest

### 6.1 `282330` BGF리테일 — defensive retail-margin stabilization

Trigger:

```text
trigger_date = 2024-03-29
trigger_type = Stage2-Actionable-Guarded
trigger_family = convenience_store_defensive_margin_stabilization
entry_date = 2024-04-01
entry_price = 118500.0
entry_price_type = next_tradable_open
```

Relevant Stock-Web rows:

```csv
d,o,h,l,c,v,a,mc,s,m
2024-04-01,118500.0,121900.0,117700.0,121900.0,64407.0,7754230000.0,2106908141400.0,17283906,KOSPI
2024-04-18,121400.0,125600.0,120000.0,125600.0,146496.0,18180778600.0,2170858593600.0,17283906,KOSPI
2024-04-30,130200.0,132900.0,127600.0,131100.0,78005.0,10268357768.0,2265920076600.0,17283906,KOSPI
2024-05-08,134100.0,136200.0,131300.0,136200.0,33728.0,4517217700.0,2354067997200.0,17283906,KOSPI
2024-06-25,110400.0,110400.0,107600.0,108000.0,60696.0,6571437552.0,1866661848000.0,17283906,KOSPI
2024-06-28,104100.0,104400.0,101700.0,103300.0,86796.0,8914484900.0,1785427489800.0,17283906,KOSPI
2024-07-05,101500.0,101700.0,99000.0,99900.0,132549.0,13291305200.0,1726662209400.0,17283906,KOSPI
2024-09-24,121100.0,123600.0,119500.0,123300.0,87364.0,10664518600.0,2131105609800.0,17283906,KOSPI
```

Backtest:

| window | peak/high | peak date | trough/low | trough date | MFE | MAE |
|---|---:|---|---:|---|---:|---:|
| 30 calendar days | 132900 | 2024-04-30 | 117700 | 2024-04-01 | +12.15% | -0.68% |
| 90 calendar days | 136200 | 2024-05-08 | 101700 | 2024-06-28 | +14.94% | -14.18% |
| 180 calendar days | 136200 | 2024-05-08 | 99000 | 2024-07-05 | +14.94% | -16.46% |

Interpretation:

```text
282330 is the positive-guarded anchor.
It did not deliver explosive MFE, but the early path was orderly and the drawdown stayed below the severe-failure zone.
This is a C19 Stage2-Guarded candidate, not Green. Green would require URL-repaired same-store-sales, gross-margin, and operating-leverage evidence.
```

### 6.2 `008770` 호텔신라 — duty-free / tourism retail margin fade

Trigger:

```text
trigger_date = 2024-07-12
trigger_type = Stage2-FalsePositive-Candidate
trigger_family = dutyfree_tourism_retail_margin_fade
entry_date = 2024-07-15
entry_price = 53900.0
entry_price_type = next_tradable_open_after_relief
```

Relevant Stock-Web rows:

```csv
d,o,h,l,c,v,a,mc,s,m
2024-07-12,53500.0,54000.0,53500.0,53900.0,101495.0,5455529400.0,2115473721900.0,39248121,KOSPI
2024-07-15,53900.0,54000.0,53000.0,53000.0,95635.0,5094431500.0,2080150413000.0,39248121,KOSPI
2024-08-05,49400.0,49400.0,44750.0,46050.0,416605.0,19458801100.0,1807375972050.0,39248121,KOSPI
2024-09-09,44800.0,45450.0,44250.0,45350.0,95838.0,4294309850.0,1779902287350.0,39248121,KOSPI
2024-09-27,47950.0,49450.0,47900.0,48850.0,303742.0,14855845950.0,1917270710850.0,39248121,KOSPI
2024-11-04,42400.0,42400.0,40500.0,41050.0,591653.0,24245384400.0,1611135367050.0,39248121,KOSPI
2024-12-09,37900.0,37900.0,35900.0,35900.0,208405.0,7595821900.0,1409007543900.0,39248121,KOSPI
2025-01-10,39050.0,39400.0,38450.0,38900.0,100342.0,3898423000.0,1526751906900.0,39248121,KOSPI
```

Backtest:

| window | peak/high | peak date | trough/low | trough date | MFE | MAE |
|---|---:|---|---:|---|---:|---:|
| 30 calendar days | 54000 | 2024-07-15 | 44750 | 2024-08-05 | +0.19% | -16.98% |
| 90 calendar days | 54000 | 2024-07-15 | 44250 | 2024-09-09 | +0.19% | -17.90% |
| 180 calendar days | 54000 | 2024-07-15 | 35900 | 2024-12-09 | +0.19% | -33.40% |

Interpretation:

```text
008770 is the clean C19 counterexample.
The relief entry had almost no remaining upside, while duty-free / tourism margin assumptions failed to protect the downside.
This should block Stage2/Green unless a hard mix, traffic, inventory, or margin bridge is repaired before entry.
```

### 6.3 `004170` 신세계 — department-store / duty-free relief rally that later failed

Trigger:

```text
trigger_date = 2024-09-26
trigger_type = Stage2-Actionable-Guarded
trigger_family = department_store_dutyfree_relief_rally_after_policy_stimulus
entry_date = 2024-09-27
entry_price = 160900.0
entry_price_type = next_tradable_open_after_relief
```

Relevant Stock-Web rows:

```csv
d,o,h,l,c,v,a,mc,s,m
2024-09-26,158000.0,160200.0,156500.0,160000.0,24278.0,3861812500.0,1575228960000.0,9845181,KOSPI
2024-09-27,160900.0,164600.0,160000.0,162300.0,64429.0,10518077300.0,1597872876300.0,9845181,KOSPI
2024-09-30,164900.0,164900.0,159000.0,159100.0,23005.0,3696562800.0,1566368297100.0,9845181,KOSPI
2024-10-21,151800.0,151800.0,145400.0,145600.0,44794.0,6601137200.0,1433458353600.0,9845181,KOSPI
2024-11-13,133200.0,133800.0,127500.0,127700.0,52574.0,6804103500.0,1257229613700.0,9845181,KOSPI
2024-12-09,130000.0,130000.0,125000.0,125900.0,40146.0,5076794100.0,1239508287900.0,9845181,KOSPI
2025-02-20,141500.0,149200.0,141500.0,148800.0,81232.0,11905473300.0,1464962932800.0,9845181,KOSPI
2025-03-07,153000.0,162200.0,152200.0,160500.0,109493.0,17428801300.0,1580151550500.0,9845181,KOSPI
```

Backtest:

| window | peak/high | peak date | trough/low | trough date | MFE | MAE |
|---|---:|---|---:|---|---:|---:|
| 30 calendar days | 164900 | 2024-09-30 | 145000 | 2024-10-22 | +2.49% | -9.88% |
| 90 calendar days | 164900 | 2024-09-30 | 125000 | 2024-12-09 | +2.49% | -22.31% |
| 180 calendar days | 164900 | 2024-09-30 | 125000 | 2024-12-09 | +2.49% | -22.31% |

Interpretation:

```text
004170 is a delayed high-MAE counterexample.
The policy/stimulus and retail-recovery framing produced a short relief window, but the 90D path broke below the high-MAE threshold.
This should remain Stage2-Guarded or local 4B watch until department-store transaction value, duty-free mix, inventory, and margin evidence are repaired.
```

---

## 7. Machine-readable trigger JSONL

```jsonl
{"row_type":"trigger","research_id":"R5L73_C19_RETAIL_MARGIN_ROUTER","round":"R5","loop":73,"large_sector_id":"L5_CONSUMER_BRAND_DISTRIBUTION","canonical_archetype_id":"C19_BRAND_RETAIL_INVENTORY_MARGIN","fine_archetype_id":"RETAIL_MARGIN_RECOVERY_DUTYFREE_INVENTORY_AND_DEPARTMENT_STORE_HIGH_MAE_ROUTER","symbol":"282330","name":"BGF리테일","trigger_type":"Stage2-Actionable-Guarded","trigger_family":"convenience_store_defensive_margin_stabilization","trigger_date":"2024-03-29","entry_date":"2024-04-01","entry_price":118500.0,"entry_price_type":"next_tradable_open","price_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","mfe_30d_pct":12.15,"mae_30d_pct":-0.68,"mfe_90d_pct":14.94,"mae_90d_pct":-14.18,"mfe_180d_pct":14.94,"mae_180d_pct":-16.46,"peak_price_180d":136200.0,"peak_date_180d":"2024-05-08","trough_price_180d":99000.0,"trough_date_180d":"2024-07-05","calibration_usable":true,"case_polarity":"positive_guarded","evidence_url_pending":true,"source_proxy_only":true,"non_price_evidence_strength":"medium_pending_url_repair","price_only_blowoff":false,"expected_stage_current_profile":"Stage2-Guarded_to_Yellow_if_retail_margin_bridge_repaired","residual_error_type":"defensive_retail_margin_stabilization_requires_url_repaired_sss_inventory_margin_evidence_before_green"}
{"row_type":"trigger","research_id":"R5L73_C19_RETAIL_MARGIN_ROUTER","round":"R5","loop":73,"large_sector_id":"L5_CONSUMER_BRAND_DISTRIBUTION","canonical_archetype_id":"C19_BRAND_RETAIL_INVENTORY_MARGIN","fine_archetype_id":"RETAIL_MARGIN_RECOVERY_DUTYFREE_INVENTORY_AND_DEPARTMENT_STORE_HIGH_MAE_ROUTER","symbol":"008770","name":"호텔신라","trigger_type":"Stage2-FalsePositive-Candidate","trigger_family":"dutyfree_tourism_retail_margin_fade","trigger_date":"2024-07-12","entry_date":"2024-07-15","entry_price":53900.0,"entry_price_type":"next_tradable_open_after_relief","price_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","mfe_30d_pct":0.19,"mae_30d_pct":-16.98,"mfe_90d_pct":0.19,"mae_90d_pct":-17.90,"mfe_180d_pct":0.19,"mae_180d_pct":-33.40,"peak_price_180d":54000.0,"peak_date_180d":"2024-07-15","trough_price_180d":35900.0,"trough_date_180d":"2024-12-09","calibration_usable":true,"case_polarity":"counterexample_low_mfe_high_mae","evidence_url_pending":true,"source_proxy_only":true,"non_price_evidence_strength":"low_pending_url_repair","price_only_blowoff":false,"expected_stage_current_profile":"blocked_Stage2_or_4B_high_MAE_watch","residual_error_type":"dutyfree_relief_entry_had_no_mfe_and_later_inventory_mix_margin_fade"}
{"row_type":"trigger","research_id":"R5L73_C19_RETAIL_MARGIN_ROUTER","round":"R5","loop":73,"large_sector_id":"L5_CONSUMER_BRAND_DISTRIBUTION","canonical_archetype_id":"C19_BRAND_RETAIL_INVENTORY_MARGIN","fine_archetype_id":"RETAIL_MARGIN_RECOVERY_DUTYFREE_INVENTORY_AND_DEPARTMENT_STORE_HIGH_MAE_ROUTER","symbol":"004170","name":"신세계","trigger_type":"Stage2-Actionable-Guarded","trigger_family":"department_store_dutyfree_relief_rally_after_policy_stimulus","trigger_date":"2024-09-26","entry_date":"2024-09-27","entry_price":160900.0,"entry_price_type":"next_tradable_open_after_relief","price_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","mfe_30d_pct":2.49,"mae_30d_pct":-9.88,"mfe_90d_pct":2.49,"mae_90d_pct":-22.31,"mfe_180d_pct":2.49,"mae_180d_pct":-22.31,"peak_price_180d":164900.0,"peak_date_180d":"2024-09-30","trough_price_180d":125000.0,"trough_date_180d":"2024-12-09","calibration_usable":true,"case_polarity":"counterexample_delayed_high_mae","evidence_url_pending":true,"source_proxy_only":true,"non_price_evidence_strength":"medium_low_pending_url_repair","price_only_blowoff":false,"expected_stage_current_profile":"Stage2-Guarded_or_4B_high_MAE_watch_until_margin_mix_bridge_repaired","residual_error_type":"department_store_dutyfree_relief_low_mfe_then_high_mae"}
```

---

## 8. Score simulation and raw component breakdown

This is shadow-only and does not change production scoring.

| symbol | retail/inventory quality | traffic/sell-through visibility | margin bridge | market mispricing | valuation rerating | operating leverage | information confidence | shadow total | intended route |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| `282330` | 12 | 11 | 10 | 8 | 7 | 9 | 7 | 64 | Stage2-Guarded / Yellow after retail margin evidence repair |
| `008770` | 4 | 5 | 2 | 4 | 3 | 2 | 5 | 25 | blocked Stage2 / high-MAE watch |
| `004170` | 6 | 7 | 4 | 6 | 5 | 4 | 5 | 37 | Stage2-Guarded or 4B watch until mix/margin evidence repair |

### Current calibrated profile stress test

The current calibrated profile already blocks pure price-only blowoff.  
The remaining C19 risk is **retail recovery without margin conversion**:

```text
C19 cleaner path:
  defensive retail traffic / store network
  + contained early MAE
  + URL-repaired same-store-sales, inventory, and margin bridge
  => Stage2-Actionable-Guarded / Yellow, possible Green after proof

C19 duty-free / department-store false-positive path:
  relief rally on tourism, China consumption, or stimulus assumptions
  + source_proxy_only evidence
  + weak MFE or 90D/180D MAE <= -20%
  => Stage2-Guarded, 4B/high-MAE watch, or blocked Stage2

C19 hard-fade path:
  MFE_30D near zero
  + duty-free / inventory / mix assumptions fail
  + 180D MAE worse than -30%
  => block Stage2
```

`282330` prevents overblocking: a lower-volatility retail margin case can still remain a Stage2-Guarded candidate.  
`008770` and `004170` show why duty-free / department-store relief rallies should not be promoted without actual mix and margin proof.

---

## 9. Aggregate metrics

```json
{
  "row_type": "aggregate",
  "research_id": "R5L73_C19_RETAIL_MARGIN_ROUTER",
  "round": "R5",
  "loop": 73,
  "large_sector_id": "L5_CONSUMER_BRAND_DISTRIBUTION",
  "canonical_archetype_id": "C19_BRAND_RETAIL_INVENTORY_MARGIN",
  "fine_archetype_id": "RETAIL_MARGIN_RECOVERY_DUTYFREE_INVENTORY_AND_DEPARTMENT_STORE_HIGH_MAE_ROUTER",
  "case_count": 3,
  "calibration_usable_case_count": 3,
  "positive_guarded_case_count": 1,
  "counterexample_count": 2,
  "new_symbol_count": 3,
  "source_proxy_only_count": 3,
  "evidence_url_pending_count": 3,
  "avg_mfe_30d_pct": 4.94,
  "avg_mae_30d_pct": -9.18,
  "avg_mfe_90d_pct": 5.87,
  "avg_mae_90d_pct": -18.13,
  "avg_mfe_180d_pct": 5.87,
  "avg_mae_180d_pct": -24.06,
  "max_mfe_180d_pct": 14.94,
  "worst_mae_180d_pct": -33.40
}
```

---

## 10. 4B proximity split

```json
{
  "row_type": "4b_split",
  "research_id": "R5L73_C19_RETAIL_MARGIN_ROUTER",
  "stage2_guarded_or_yellow_candidate": [
    {
      "symbol": "282330",
      "reason": "contained early MAE and moderate MFE; requires URL-repaired same-store-sales/inventory/margin bridge before Yellow/Green"
    }
  ],
  "local_4b_watch": [
    {
      "symbol": "004170",
      "reason": "policy/stimulus relief had only +2.49% MFE and 90D MAE reached -22.31%"
    }
  ],
  "blocked_stage2_or_hard_fade": [
    {
      "symbol": "008770",
      "reason": "relief entry had only +0.19% MFE and 180D MAE reached -33.40%"
    }
  ],
  "full_4b_or_green_requires_non_price_evidence": [
    "same-store-sales or transaction value",
    "inventory quality / markdown pressure",
    "gross margin bridge",
    "duty-free mix and tourist traffic bridge",
    "operating leverage conversion"
  ]
}
```

---

## 11. Shadow rule candidate

```yaml
row_type: canonical_archetype_rule_candidate
canonical_archetype_id: C19_BRAND_RETAIL_INVENTORY_MARGIN
fine_archetype_id: RETAIL_MARGIN_RECOVERY_DUTYFREE_INVENTORY_AND_DEPARTMENT_STORE_HIGH_MAE_ROUTER
rule_name: C19_retail_margin_inventory_bridge_and_high_mae_router
production_scoring_changed: false
shadow_weight_only: true
```

### Proposed routing logic

```text
For C19 brand/retail/inventory-margin cases:

Tier A: verified defensive retail margin stabilization
  Conditions:
    - traffic or same-store-sales evidence is URL-repaired
    - inventory markdown risk is controlled
    - margin bridge is visible
    - 30D/90D MAE remains contained
  Routing:
    - Stage2-Actionable-Guarded allowed
    - Stage3-Yellow allowed after evidence repair
    - Green only after inventory and margin conversion are verified

Tier B: relief rally without margin bridge
  Conditions:
    - retailer or duty-free stock bounces on traffic / stimulus / China-spend assumptions
    - source_proxy_only or evidence_url_pending remains true
    - MFE is weak or short-lived
  Routing:
    - Stage2-Guarded at most
    - local 4B/high-MAE watch
    - no Green

Tier C: duty-free / department-store hard fade
  Conditions:
    - MFE_30D < +5%
    - MAE_90D <= -20% or MAE_180D <= -30%
    - mix/inventory/margin bridge is missing
  Routing:
    - block Stage2
    - count as false-positive counterexample
```

### Suggested shadow delta

```json
{
  "row_type": "shadow_weight",
  "axis": "c19_retail_margin_inventory_bridge_and_high_mae_router",
  "scope": "canonical_archetype_id:C19_BRAND_RETAIL_INVENTORY_MARGIN",
  "proposal": {
    "source_proxy_only_green_allowed": false,
    "inventory_margin_bridge_required_for_green": true,
    "retail_relief_stage2_cap": "guarded_only_until_url_repair",
    "weak_mfe_threshold_30d_pct": 5.0,
    "high_mae_watch_threshold_90d_pct": -20.0,
    "hard_fade_threshold_180d_pct": -30.0,
    "positive_weight_blocked_until_url_repair": true
  },
  "confidence": "medium_low_until_url_repair",
  "apply_now": false,
  "reason": "One defensive convenience-store case and two duty-free/department-store high-MAE cases show that C19 should reward contained-MAE margin stabilization only after inventory and margin evidence is repaired, while weak-MFE retail relief rallies should be capped or blocked."
}
```

---

## 12. Residual contribution summary

```json
{
  "row_type": "residual_contribution",
  "research_id": "R5L73_C19_RETAIL_MARGIN_ROUTER",
  "large_sector_id": "L5_CONSUMER_BRAND_DISTRIBUTION",
  "canonical_archetype_id": "C19_BRAND_RETAIL_INVENTORY_MARGIN",
  "contribution": "Adds three non-top-covered C19 retail/inventory-margin cases and separates a defensive convenience-store margin-stabilization path from duty-free and department-store relief rallies that later suffer high MAE. C19 Green should require URL-repaired same-store-sales, inventory, mix, and margin evidence.",
  "positive_guarded_case_added": 1,
  "counterexample_case_added": 2,
  "new_symbol_count": 3,
  "data_quality_blocker": "All three non-price retail-margin triggers require URL-level repair before positive weight promotion.",
  "guardrail_added": "C19 source_proxy_only retail relief rallies with MFE_30D < +5% and MAE_90D <= -20% or MAE_180D <= -30% should block Stage2 or route to 4B/high-MAE watch."
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
    282330: false
    008770: false
    004170: false
  evidence_url_pending:
    282330: true
    008770: true
    004170: true
  source_proxy_only:
    282330: true
    008770: true
    004170: true
```

Limitations:

```text
- Price path is validated against Stock-Web tradable OHLC rows.
- Non-price evidence is not URL-repaired in this run.
- Therefore this artifact is useful for C19 residual shape and high-MAE guardrail design, but should not promote positive weights until filings/IR/disclosure/report data verifies same-store-sales, inventory quality, duty-free mix, tourist traffic, gross margin, and operating leverage.
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
2. Preserve R5 / loop 73 metadata.
3. Add the cases to C19_BRAND_RETAIL_INVENTORY_MARGIN only if parser validation passes.
4. Treat all three non-price triggers as evidence_url_pending=true and source_proxy_only=true until URL-level evidence is repaired.
5. Do not use these rows for positive weight promotion until filings/IR/disclosure/report data verifies same-store-sales, inventory quality, duty-free mix, tourist traffic, gross margin, and operating leverage.
6. Add a shadow-only rule candidate named C19_retail_margin_inventory_bridge_and_high_mae_router.
7. Do not loosen Stage3-Green.
8. Add C19-specific guards:
   - source_proxy_only -> no Green
   - retail relief without inventory/margin bridge -> Stage2-Guarded at most
   - MFE_30D < +5% and MAE_90D <= -20% -> block Stage2 or local 4B/high-MAE watch
   - MAE_180D <= -30% without margin bridge -> hard-fade counterexample
   - Green requires repaired inventory/mix/margin/operating-leverage bridge
9. Keep production scoring unchanged unless later batch promotion logic independently marks this axis safe.
```

---

## 15. Next round state

```text
completed_round = R5
completed_loop = 73
next_round = R6
next_loop = 73
next_large_sector_hint = L6_FINANCIAL_CAPITAL_RETURN_DIGITAL
```
