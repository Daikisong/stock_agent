# E2R Stock-Web v12 Residual Research — R5 Loop 76

```yaml
research_session: post_calibrated_sector_archetype_residual_research
mode: historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12
completed_round: R5
completed_loop: 76
next_round: R6
next_loop: 76
large_sector_id: L5_CONSUMER_BRAND_DISTRIBUTION
canonical_archetype_id: C18_CONSUMER_EXPORT_CHANNEL_REORDER
fine_archetype_id: KFOOD_SEAFOOD_PROCESSED_FOOD_EXPORT_REORDER_AND_LATE_SPIKE_HIGH_MAE_ROUTER
output_file: e2r_stock_web_v12_residual_round_R5_loop_76_L5_CONSUMER_BRAND_DISTRIBUTION_C18_CONSUMER_EXPORT_CHANNEL_REORDER_research.md
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
completed_loop  = 76
large_sector_id = L4_MATERIALS_SPREAD_RESOURCE
canonical_archetype_id = C15_MATERIAL_SPREAD_SUPERCYCLE
```

Therefore:

```text
scheduled_round = R5
scheduled_loop  = 76
```

R5 maps to:

```text
large_sector_id = L5_CONSUMER_BRAND_DISTRIBUTION
```

This run selects:

```text
canonical_archetype_id = C18_CONSUMER_EXPORT_CHANNEL_REORDER
fine_archetype_id = KFOOD_SEAFOOD_PROCESSED_FOOD_EXPORT_REORDER_AND_LATE_SPIKE_HIGH_MAE_ROUTER
```

This is a valid R5/L5 pairing.

---

## 1. Why this R5/C18 run

The no-repeat ledger shows C18 is moderately covered and concentrated in large/known consumer-export leaders:

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

This file avoids those top-covered symbols and adds four K-food / seafood / processed-food export-channel cases:

```text
003960 사조대림
014710 사조씨푸드
049770 동원F&B
011150 CJ씨푸드
```

Research question:

```text
Can C18 separate real K-food / seafood export-channel reorder rerating from late theme spikes where the export label is already crowded, MFE is weak, and high MAE follows without reorder, channel inventory, and margin evidence?
```

C18 is a reorder bridge. A viral export story is the first order; Stage2 needs the second order, distributor pull-through, channel inventory health, product mix, and margin conversion. Without reorder receipts, the theme candle is a supermarket sample tray: busy for a moment, but not proof of shelf velocity.

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
| `003960` | 사조대림 | active_like / KOSPI | no 2024 overlap; latest listed candidate 2019-06-26 | true |
| `014710` | 사조씨푸드 | active_like / KOSPI | none listed | true |
| `049770` | 동원F&B | inactive_or_delisted_like / KOSPI history | no 2024 overlap; 2023-04-19 candidate before selected window | true for selected 2024 windows |
| `011150` | CJ씨푸드 | active_like / KOSPI | no 2024 overlap; old 2002 candidate only | true |

Profile caveat:

```text
Stock-Web OHLC is raw/unadjusted marcap data.
These cases are calibration-safe for the selected 2024 30D/90D/180D windows because no listed corporate-action candidate overlaps each entry~D+180 test window.
For 049770, status is inferred as inactive_or_delisted_like because Stock-Web latest row ends in 2025; the selected 2024 calibration window is still usable.
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
The Stock-Web price path is fully validated, but company-level export orders, distributor reorder, channel inventory, overseas sell-through, product mix, FX, input-cost pass-through, gross margin, and operating leverage evidence still require later URL repair through filings, IR decks, export data, channel checks, customs data, or sell-side reports before production weight promotion.
```

C18 interpretation used here:

```text
C18 is not simply “food stock rose.”
It asks whether consumer-export demand is reorder-convertible:
- export order and distributor reorder,
- overseas channel inventory and sell-through,
- product mix and ASP,
- input-cost and FX pass-through,
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
003960 + C18_CONSUMER_EXPORT_CHANNEL_REORDER -> no direct match found
014710 + C18_CONSUMER_EXPORT_CHANNEL_REORDER -> no direct match found
049770 + C18_CONSUMER_EXPORT_CHANNEL_REORDER -> no direct match found
011150 + C18_CONSUMER_EXPORT_CHANNEL_REORDER -> no direct match found
```

Novelty accounting:

```json
{
  "new_symbol_count": 4,
  "minimum_new_symbol_count": 2,
  "positive_case_count": 3,
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
| `R5L76_C18_003960_20240517` | `003960` 사조대림 | K-food processed seafood export-channel reorder | positive anchor |
| `R5L76_C18_014710_20240517` | `014710` 사조씨푸드 | seafood export-channel high-MFE low-MAE path | positive-guarded |
| `R5L76_C18_049770_20240517` | `049770` 동원F&B | processed-food export reorder moderate-MFE later drawdown | positive-guarded / later-drawdown watch |
| `R5L76_C18_011150_20240617` | `011150` CJ씨푸드 | late seafood export theme spike with weak MFE and extreme MAE | counterexample / 4B-4C watch |

The intended residual:

```text
C18 should separate:
1. export-channel reorder paths where MFE compounds before MAE becomes material;
2. high-MFE seafood export paths with low early drawdown;
3. moderate-MFE large food names where later drawdown caps Yellow/Green until evidence repair;
4. late crowded seafood theme spikes where the entry peak is already spent and MAE becomes extreme.
```

---

## 6. Stock-Web OHLC and backtest

### 6.1 `003960` 사조대림 — K-food / processed seafood export-channel reorder positive anchor

Trigger:

```text
trigger_date = 2024-05-16
trigger_type = Stage2-Actionable
trigger_family = kfood_processed_seafood_export_channel_reorder_low_mae_rerating
entry_date = 2024-05-17
entry_price = 43850.0
entry_price_type = next_tradable_open_after_kfood_export_reorder_burst
```

Relevant Stock-Web rows:

```csv
d,o,h,l,c,v,a,mc,s,m
2024-05-16,42450.0,45200.0,41800.0,44000.0,137202.0,6016431900.0,403236548000.0,9164467,KOSPI
2024-05-17,43850.0,47800.0,43450.0,44800.0,188049.0,8630451600.0,410568121600.0,9164467,KOSPI
2024-06-07,42950.0,42950.0,41500.0,42350.0,34328.0,1443935800.0,388115177450.0,9164467,KOSPI
2024-06-14,47450.0,61600.0,46750.0,61600.0,984182.0,55960562550.0,564531167200.0,9164467,KOSPI
2024-06-28,79600.0,94300.0,74200.0,90900.0,866950.0,74330788100.0,833050050300.0,9164467,KOSPI
2024-07-09,108500.0,109900.0,97700.0,99500.0,1307373.0,136290793500.0,911864466500.0,9164467,KOSPI
2024-08-05,62200.0,62700.0,52800.0,57700.0,283449.0,16514106100.0,528789745900.0,9164467,KOSPI
2024-11-13,39050.0,39700.0,38300.0,38300.0,31686.0,1230424200.0,350999086100.0,9164467,KOSPI
```

Backtest:

| window | peak/high | peak date | trough/low | trough date | MFE | MAE |
|---|---:|---|---:|---|---:|---:|
| 30 calendar days | 61600 | 2024-06-14 | 41500 | 2024-06-07 | +40.48% | -5.36% |
| 90 calendar days | 109900 | 2024-07-09 | 41500 | 2024-06-07 | +150.63% | -5.36% |
| 180 calendar days | 109900 | 2024-07-09 | 38300 | 2024-11-13 | +150.63% | -12.66% |

Interpretation:

```text
003960 is the C18 positive anchor.
The K-food / processed seafood export-channel path delivered very large MFE with controlled early MAE.
It supports Stage2-Actionable / Yellow after evidence repair, but Green still requires URL-repaired export reorder, channel inventory, sell-through, product mix, and margin evidence.
```

### 6.2 `014710` 사조씨푸드 — seafood export-channel high-MFE low-MAE path

Trigger:

```text
trigger_date = 2024-05-16
trigger_type = Stage2-Actionable-Guarded
trigger_family = seafood_export_channel_theme_high_mfe_low_mae_rerating
entry_date = 2024-05-17
entry_price = 4150.0
entry_price_type = next_tradable_open_after_seafood_export_channel_burst
```

Relevant Stock-Web rows:

```csv
d,o,h,l,c,v,a,mc,s,m
2024-05-16,3545.0,4420.0,3545.0,3935.0,5102357.0,20852022475.0,67754966705.0,17218543,KOSPI
2024-05-17,4150.0,5050.0,3995.0,4420.0,12412401.0,58997470945.0,76105960060.0,17218543,KOSPI
2024-06-05,4340.0,4340.0,3990.0,4210.0,175060.0,733523645.0,72490066030.0,17218543,KOSPI
2024-06-14,4780.0,6090.0,4610.0,6090.0,10217009.0,58353633215.0,104860926870.0,17218543,KOSPI
2024-07-09,8860.0,8950.0,8020.0,8190.0,6866858.0,58138855770.0,141019867170.0,17218543,KOSPI
2024-08-05,6380.0,6640.0,6010.0,6350.0,554667.0,3551342020.0,109337748050.0,17218543,KOSPI
2024-11-13,5170.0,5210.0,5060.0,5090.0,87190.0,446286720.0,87642383870.0,17218543,KOSPI
```

Backtest:

| window | peak/high | peak date | trough/low | trough date | MFE | MAE |
|---|---:|---|---:|---|---:|---:|
| 30 calendar days | 6090 | 2024-06-14 | 3990 | 2024-06-05 | +46.75% | -3.86% |
| 90 calendar days | 8950 | 2024-07-09 | 3990 | 2024-06-05 | +115.66% | -3.86% |
| 180 calendar days | 8950 | 2024-07-09 | 3990 | 2024-06-05 | +115.66% | -3.86% |

Interpretation:

```text
014710 is a strong positive-guarded seafood export-channel case.
MFE expanded through the first 90D while MAE stayed shallow.
This should remain Stage2-Guarded / Yellow-after-repair, not Green while non-price export reorder and margin evidence remains source-proxy-only.
```

### 6.3 `049770` 동원F&B — processed-food export-channel moderate-MFE later drawdown

Trigger:

```text
trigger_date = 2024-05-16
trigger_type = Stage2-Actionable-Guarded
trigger_family = processed_food_export_channel_reorder_moderate_mfe_later_drawdown
entry_date = 2024-05-17
entry_price = 38300.0
entry_price_type = next_tradable_open_after_processed_food_export_reorder_burst
```

Relevant Stock-Web rows:

```csv
d,o,h,l,c,v,a,mc,s,m
2024-05-16,38400.0,38400.0,37100.0,37150.0,29154.0,1094246700.0,716832283000.0,19295620,KOSPI
2024-05-17,38300.0,41600.0,37700.0,39500.0,286823.0,11464643700.0,762176990000.0,19295620,KOSPI
2024-06-14,42800.0,48350.0,42550.0,46100.0,580134.0,26777149950.0,889528082000.0,19295620,KOSPI
2024-06-17,46750.0,48900.0,45200.0,46700.0,346614.0,16324846000.0,901105454000.0,19295620,KOSPI
2024-08-05,36050.0,36600.0,33000.0,33900.0,94338.0,3263939100.0,654121518000.0,19295620,KOSPI
2024-11-13,30800.0,31900.0,30650.0,30650.0,25498.0,792664500.0,591410753000.0,19295620,KOSPI
```

Backtest:

| window | peak/high | peak date | trough/low | trough date | MFE | MAE |
|---|---:|---|---:|---|---:|---:|
| 30 calendar days | 48350 | 2024-06-14 | 37700 | 2024-05-17 | +26.24% | -1.57% |
| 90 calendar days | 48900 | 2024-06-17 | 33000 | 2024-08-05 | +27.68% | -13.84% |
| 180 calendar days | 48900 | 2024-06-17 | 30650 | 2024-11-13 | +27.68% | -19.97% |

Interpretation:

```text
049770 is the moderate-MFE / later-drawdown branch.
The first 30D showed a workable export-channel rerating, but later drawdown widened enough to block Yellow/Green while evidence remains unrepaired.
This belongs at Stage2-Guarded until export reorder, channel inventory, pricing, and margin evidence is URL-repaired.
```

### 6.4 `011150` CJ씨푸드 — late seafood export theme spike with weak MFE and extreme MAE

Trigger:

```text
trigger_date = 2024-06-14
trigger_type = Stage2-FalsePositive-Candidate
trigger_family = late_seafood_export_theme_spike_weak_mfe_extreme_mae
entry_date = 2024-06-17
entry_price = 6290.0
entry_price_type = next_tradable_open_after_late_seafood_export_theme_spike
```

Relevant Stock-Web rows:

```csv
d,o,h,l,c,v,a,mc,s,m
2024-06-14,5140.0,6460.0,4920.0,6320.0,71598499.0,425627690990.0,227082485360.0,35930773,KOSPI
2024-06-17,6290.0,6490.0,5740.0,6040.0,22421670.0,137179192910.0,217021868920.0,35930773,KOSPI
2024-07-05,4555.0,4615.0,4460.0,4475.0,970527.0,4392922265.0,160790209175.0,35930773,KOSPI
2024-08-05,3760.0,3795.0,3270.0,3420.0,1067423.0,3803931580.0,122883243660.0,35930773,KOSPI
2024-11-13,2815.0,2900.0,2780.0,2790.0,354438.0,998486810.0,100246856670.0,35930773,KOSPI
2024-12-09,2700.0,2740.0,2530.0,2725.0,577683.0,1525563970.0,97911356425.0,35930773,KOSPI
```

Backtest:

| window | peak/high | peak date | trough/low | trough date | MFE | MAE |
|---|---:|---|---:|---|---:|---:|
| 30 calendar days | 6490 | 2024-06-17 | 4460 | 2024-07-05 | +3.18% | -29.09% |
| 90 calendar days | 6490 | 2024-06-17 | 3270 | 2024-08-05 | +3.18% | -48.01% |
| 180 calendar days | 6490 | 2024-06-17 | 2530 | 2024-12-09 | +3.18% | -59.78% |

Interpretation:

```text
011150 is the hard C18 counterexample.
The late seafood export theme entry peaked immediately, produced almost no MFE, and then suffered extreme MAE.
This should block Stage2 or route to 4B/4C high-MAE watch unless a new independent trigger later repairs reorder, channel, and margin evidence.
```

---

## 7. Machine-readable trigger JSONL

```jsonl
{"row_type":"trigger","research_id":"R5L76_C18_KFOOD_SEAFOOD_EXPORT_ROUTER","round":"R5","loop":76,"large_sector_id":"L5_CONSUMER_BRAND_DISTRIBUTION","canonical_archetype_id":"C18_CONSUMER_EXPORT_CHANNEL_REORDER","fine_archetype_id":"KFOOD_SEAFOOD_PROCESSED_FOOD_EXPORT_REORDER_AND_LATE_SPIKE_HIGH_MAE_ROUTER","symbol":"003960","name":"사조대림","trigger_type":"Stage2-Actionable","trigger_family":"kfood_processed_seafood_export_channel_reorder_low_mae_rerating","trigger_date":"2024-05-16","entry_date":"2024-05-17","entry_price":43850.0,"entry_price_type":"next_tradable_open_after_kfood_export_reorder_burst","price_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","mfe_30d_pct":40.48,"mae_30d_pct":-5.36,"mfe_90d_pct":150.63,"mae_90d_pct":-5.36,"mfe_180d_pct":150.63,"mae_180d_pct":-12.66,"peak_price_180d":109900.0,"peak_date_180d":"2024-07-09","trough_price_180d":38300.0,"trough_date_180d":"2024-11-13","calibration_usable":true,"case_polarity":"positive_anchor_kfood_export_low_mae","evidence_url_pending":true,"source_proxy_only":true,"non_price_evidence_strength":"medium_pending_url_repair","price_only_blowoff":false,"expected_stage_current_profile":"Stage2-Actionable_to_Yellow_after_export_reorder_channel_margin_bridge_repaired","residual_error_type":"kfood_processed_seafood_export_path_supports_positive_route_but_green_requires_url_repaired_reorder_channel_inventory_margin_bridge"}
{"row_type":"trigger","research_id":"R5L76_C18_KFOOD_SEAFOOD_EXPORT_ROUTER","round":"R5","loop":76,"large_sector_id":"L5_CONSUMER_BRAND_DISTRIBUTION","canonical_archetype_id":"C18_CONSUMER_EXPORT_CHANNEL_REORDER","fine_archetype_id":"KFOOD_SEAFOOD_PROCESSED_FOOD_EXPORT_REORDER_AND_LATE_SPIKE_HIGH_MAE_ROUTER","symbol":"014710","name":"사조씨푸드","trigger_type":"Stage2-Actionable-Guarded","trigger_family":"seafood_export_channel_theme_high_mfe_low_mae_rerating","trigger_date":"2024-05-16","entry_date":"2024-05-17","entry_price":4150.0,"entry_price_type":"next_tradable_open_after_seafood_export_channel_burst","price_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","mfe_30d_pct":46.75,"mae_30d_pct":-3.86,"mfe_90d_pct":115.66,"mae_90d_pct":-3.86,"mfe_180d_pct":115.66,"mae_180d_pct":-3.86,"peak_price_180d":8950.0,"peak_date_180d":"2024-07-09","trough_price_180d":3990.0,"trough_date_180d":"2024-06-05","calibration_usable":true,"case_polarity":"positive_guarded_seafood_export_low_mae","evidence_url_pending":true,"source_proxy_only":true,"non_price_evidence_strength":"medium_low_pending_url_repair","price_only_blowoff":false,"expected_stage_current_profile":"Stage2-Guarded_to_Yellow_if_export_channel_reorder_margin_bridge_repaired","residual_error_type":"seafood_export_channel_path_had_high_mfe_and_low_mae_but_green_requires_url_repaired_reorder_margin_evidence"}
{"row_type":"trigger","research_id":"R5L76_C18_KFOOD_SEAFOOD_EXPORT_ROUTER","round":"R5","loop":76,"large_sector_id":"L5_CONSUMER_BRAND_DISTRIBUTION","canonical_archetype_id":"C18_CONSUMER_EXPORT_CHANNEL_REORDER","fine_archetype_id":"KFOOD_SEAFOOD_PROCESSED_FOOD_EXPORT_REORDER_AND_LATE_SPIKE_HIGH_MAE_ROUTER","symbol":"049770","name":"동원F&B","trigger_type":"Stage2-Actionable-Guarded","trigger_family":"processed_food_export_channel_reorder_moderate_mfe_later_drawdown","trigger_date":"2024-05-16","entry_date":"2024-05-17","entry_price":38300.0,"entry_price_type":"next_tradable_open_after_processed_food_export_reorder_burst","price_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","mfe_30d_pct":26.24,"mae_30d_pct":-1.57,"mfe_90d_pct":27.68,"mae_90d_pct":-13.84,"mfe_180d_pct":27.68,"mae_180d_pct":-19.97,"peak_price_180d":48900.0,"peak_date_180d":"2024-06-17","trough_price_180d":30650.0,"trough_date_180d":"2024-11-13","calibration_usable":true,"case_polarity":"positive_guarded_moderate_mfe_later_drawdown","evidence_url_pending":true,"source_proxy_only":true,"non_price_evidence_strength":"medium_low_pending_url_repair","price_only_blowoff":false,"expected_stage_current_profile":"Stage2-Guarded_only_until_export_reorder_margin_channel_bridge_repaired","residual_error_type":"processed_food_export_reorder_path_had_moderate_mfe_but_later_drawdown_requires_url_repaired_channel_margin_bridge_before_yellow_green"}
{"row_type":"trigger","research_id":"R5L76_C18_KFOOD_SEAFOOD_EXPORT_ROUTER","round":"R5","loop":76,"large_sector_id":"L5_CONSUMER_BRAND_DISTRIBUTION","canonical_archetype_id":"C18_CONSUMER_EXPORT_CHANNEL_REORDER","fine_archetype_id":"KFOOD_SEAFOOD_PROCESSED_FOOD_EXPORT_REORDER_AND_LATE_SPIKE_HIGH_MAE_ROUTER","symbol":"011150","name":"CJ씨푸드","trigger_type":"Stage2-FalsePositive-Candidate","trigger_family":"late_seafood_export_theme_spike_weak_mfe_extreme_mae","trigger_date":"2024-06-14","entry_date":"2024-06-17","entry_price":6290.0,"entry_price_type":"next_tradable_open_after_late_seafood_export_theme_spike","price_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","mfe_30d_pct":3.18,"mae_30d_pct":-29.09,"mfe_90d_pct":3.18,"mae_90d_pct":-48.01,"mfe_180d_pct":3.18,"mae_180d_pct":-59.78,"peak_price_180d":6490.0,"peak_date_180d":"2024-06-17","trough_price_180d":2530.0,"trough_date_180d":"2024-12-09","calibration_usable":true,"case_polarity":"counterexample_late_spike_weak_mfe_extreme_mae","evidence_url_pending":true,"source_proxy_only":true,"non_price_evidence_strength":"low_pending_url_repair","price_only_blowoff":true,"expected_stage_current_profile":"blocked_Stage2_or_4B_4C_high_MAE_watch","residual_error_type":"late_seafood_export_theme_spike_had_entry_peak_weak_mfe_and_extreme_mae_without_reorder_channel_margin_bridge"}
```

---

## 8. Score simulation and raw component breakdown

This is shadow-only and does not change production scoring.

| symbol | export/reorder relevance | channel sell-through | inventory / channel health | product mix / ASP | market mispricing | margin / operating leverage | information confidence | shadow total | intended route |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| `003960` | 14 | 11 | 10 | 10 | 15 | 10 | 6 | 76 | Stage2/Yellow after evidence repair |
| `014710` | 12 | 9 | 8 | 7 | 13 | 7 | 5 | 61 | Stage2-Guarded / Yellow after evidence repair |
| `049770` | 10 | 8 | 7 | 7 | 8 | 6 | 5 | 51 | Stage2-Guarded only until evidence repair |
| `011150` | 7 | 2 | 2 | 3 | 1 | 1 | 4 | 20 | blocked Stage2 / 4B-4C high-MAE watch |

### Current calibrated profile stress test

The current calibrated profile already blocks pure price-only blowoff.  
The remaining C18 issue is **export-channel label without reorder and margin conversion**:

```text
C18 clean K-food export path:
  export/reorder relevance
  + persistent MFE
  + contained early MAE
  + URL-repaired channel inventory / sell-through / margin evidence
  => Stage2-Actionable / Yellow candidate, possible Green after proof

C18 moderate-MFE later-drawdown path:
  export label and first-window MFE exist
  + MAE_90D <= -10% or MAE_180D <= -15%
  + evidence remains source_proxy_only
  => Stage2-Guarded at most, no Green

C18 late crowded theme spike:
  entry peak occurs immediately
  + MFE_30D < +5%
  + MAE_30D <= -25%
  + no reorder/channel evidence
  => block Stage2 or route to 4B/4C high-MAE watch
```

`003960`, `014710`, and `049770` prevent overblocking.  
`011150` shows why late seafood/K-food theme spikes need an entry-peak and high-MAE guard.

---

## 9. Aggregate metrics

```json
{
  "row_type": "aggregate",
  "research_id": "R5L76_C18_KFOOD_SEAFOOD_EXPORT_ROUTER",
  "round": "R5",
  "loop": 76,
  "large_sector_id": "L5_CONSUMER_BRAND_DISTRIBUTION",
  "canonical_archetype_id": "C18_CONSUMER_EXPORT_CHANNEL_REORDER",
  "fine_archetype_id": "KFOOD_SEAFOOD_PROCESSED_FOOD_EXPORT_REORDER_AND_LATE_SPIKE_HIGH_MAE_ROUTER",
  "case_count": 4,
  "calibration_usable_case_count": 4,
  "positive_case_count": 3,
  "counterexample_count": 1,
  "new_symbol_count": 4,
  "source_proxy_only_count": 4,
  "evidence_url_pending_count": 4,
  "avg_mfe_30d_pct": 29.16,
  "avg_mae_30d_pct": -9.97,
  "avg_mfe_90d_pct": 74.29,
  "avg_mae_90d_pct": -17.77,
  "avg_mfe_180d_pct": 74.29,
  "avg_mae_180d_pct": -24.07,
  "max_mfe_180d_pct": 150.63,
  "worst_mae_180d_pct": -59.78
}
```

---

## 10. 4B proximity split

```json
{
  "row_type": "4b_split",
  "research_id": "R5L76_C18_KFOOD_SEAFOOD_EXPORT_ROUTER",
  "stage2_positive_or_yellow_candidate": [
    {
      "symbol": "003960",
      "reason": "processed seafood/K-food export path had +150.63% 180D MFE with initially controlled MAE"
    },
    {
      "symbol": "014710",
      "reason": "seafood export-channel path had +115.66% 180D MFE with only -3.86% MAE"
    }
  ],
  "stage2_guarded_or_later_drawdown_watch": [
    {
      "symbol": "049770",
      "reason": "processed-food export path had +27.68% MFE but 180D MAE reached -19.97%"
    }
  ],
  "blocked_stage2_or_4c_watch": [
    {
      "symbol": "011150",
      "reason": "late seafood export theme entry had only +3.18% MFE and -59.78% 180D MAE"
    }
  ],
  "full_4b_or_green_requires_non_price_evidence": [
    "export order and distributor reorder",
    "overseas channel sell-through",
    "channel inventory health",
    "product mix and ASP",
    "input-cost and FX pass-through",
    "gross margin and operating leverage conversion"
  ]
}
```

---

## 11. Shadow rule candidate

```yaml
row_type: canonical_archetype_rule_candidate
canonical_archetype_id: C18_CONSUMER_EXPORT_CHANNEL_REORDER
fine_archetype_id: KFOOD_SEAFOOD_PROCESSED_FOOD_EXPORT_REORDER_AND_LATE_SPIKE_HIGH_MAE_ROUTER
rule_name: C18_kfood_seafood_export_reorder_and_late_spike_high_mae_router
production_scoring_changed: false
shadow_weight_only: true
```

### Proposed routing logic

```text
For C18 K-food / seafood / processed-food export-channel cases:

Tier A: verified export-reorder winner
  Conditions:
    - export order, distributor reorder, channel inventory, sell-through, and margin evidence are URL-repaired
    - MFE_90D >= +40%
    - MAE_90D > -10%
    - MFE persists beyond the first event candle
  Routing:
    - Stage2-Actionable allowed
    - Stage3-Yellow allowed after evidence repair
    - Green only after reorder / channel / margin bridge is verified

Tier B: moderate-MFE later-drawdown food export path
  Conditions:
    - MFE_30D >= +20%
    - MAE_90D <= -10% or MAE_180D <= -15%
    - evidence_url_pending or source_proxy_only remains true
  Routing:
    - Stage2-Guarded at most
    - no Green until evidence repair

Tier C: late crowded seafood/K-food theme spike
  Conditions:
    - peak occurs on entry day or first 5 trading days
    - MFE_30D < +5%
    - MAE_30D <= -25% or MAE_90D <= -40%
    - no repaired reorder/channel evidence
  Routing:
    - block Stage2
    - route to 4B/4C high-MAE watch
```

### Suggested shadow delta

```json
{
  "row_type": "shadow_weight",
  "axis": "c18_kfood_seafood_export_reorder_and_late_spike_high_mae_router",
  "scope": "canonical_archetype_id:C18_CONSUMER_EXPORT_CHANNEL_REORDER",
  "proposal": {
    "source_proxy_only_green_allowed": false,
    "export_reorder_channel_margin_bridge_required_for_green": true,
    "verified_export_winner_mfe90_threshold_pct": 40.0,
    "verified_export_winner_mae90_min_pct": -10.0,
    "moderate_mfe_threshold_30d_pct": 20.0,
    "later_drawdown_mae90_threshold_pct": -10.0,
    "later_drawdown_mae180_threshold_pct": -15.0,
    "late_spike_weak_mfe_threshold_30d_pct": 5.0,
    "late_spike_mae30_threshold_pct": -25.0,
    "late_spike_mae90_threshold_pct": -40.0,
    "entry_day_or_first5_peak_blocks_stage2_without_bridge": true,
    "positive_weight_blocked_until_url_repair": true
  },
  "confidence": "medium_low_until_url_repair",
  "apply_now": false,
  "reason": "Three non-top-covered K-food/seafood export-channel winners and one late-spike extreme-MAE failure show that C18 should require URL-repaired export reorder, channel sell-through, inventory, product mix, and margin evidence before Yellow/Green."
}
```

---

## 12. Residual contribution summary

```json
{
  "row_type": "residual_contribution",
  "research_id": "R5L76_C18_KFOOD_SEAFOOD_EXPORT_ROUTER",
  "large_sector_id": "L5_CONSUMER_BRAND_DISTRIBUTION",
  "canonical_archetype_id": "C18_CONSUMER_EXPORT_CHANNEL_REORDER",
  "contribution": "Adds four non-top-covered C18 K-food/seafood/processed-food export-channel cases and separates real reorder-like high-MFE paths from a late seafood theme spike with weak MFE and extreme MAE. C18 Yellow/Green should require URL-repaired export orders, distributor reorder, overseas sell-through, channel inventory, product mix, input-cost/FX pass-through, and margin conversion evidence.",
  "positive_case_added": 3,
  "counterexample_case_added": 1,
  "new_symbol_count": 4,
  "new_independent_case_count": 4,
  "reused_case_count": 0,
  "same_archetype_new_symbol_count": 4,
  "same_archetype_new_trigger_family_count": 4,
  "new_trigger_family_count": 4,
  "current_profile_error_count": 1,
  "diversity_score_summary": {
    "new_symbol_bonus": 12,
    "counterexample_gap_bonus": 4,
    "residual_error_bonus": 5,
    "wrong_round_penalty": 0,
    "repeated_same_symbol_penalty": 0,
    "net_interpretive_score": 21
  },
  "loop_contribution_label": "canonical_archetype_rule_candidate",
  "do_not_propose_new_weight_delta": false,
  "data_quality_blocker": "All four non-price food/export-channel triggers require URL-level repair before positive weight promotion.",
  "guardrail_added": "C18 source_proxy_only late theme spikes with MFE_30D < +5% and MAE_30D <= -25% should block Stage2; moderate-MFE food export cases with later MAE should cap at Stage2-Guarded until reorder/channel/margin evidence is repaired."
}
```

One-line contribution:

```text
This loop adds 4 new independent cases, 1 counterexample, and 1 residual error for R5/L5_CONSUMER_BRAND_DISTRIBUTION/C18_CONSUMER_EXPORT_CHANNEL_REORDER.
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
    003960: false
    014710: false
    049770: false
    011150: false
  evidence_url_pending:
    003960: true
    014710: true
    049770: true
    011150: true
  source_proxy_only:
    003960: true
    014710: true
    049770: true
    011150: true
  special_handling:
    049770:
      status_inferred: inactive_or_delisted_like
      note: "Stock-Web latest row ends after the selected 2024 test window. The selected 2024 30D/90D/180D windows are still calibration-usable because no corporate-action candidate overlaps."
```

Limitations:

```text
- Price path is validated against Stock-Web tradable OHLC rows.
- Non-price evidence is not URL-repaired in this run.
- Therefore this artifact is useful for C18 K-food/seafood/processed-food export-channel residual shape and late-spike high-MAE guardrail design, but should not promote positive weights until filings, IR, export data, channel checks, customs data, or reports verify export orders, distributor reorder, overseas sell-through, channel inventory, product mix, and margin conversion.
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
2. Preserve R5 / loop 76 metadata.
3. Add the cases to C18_CONSUMER_EXPORT_CHANNEL_REORDER only if parser validation passes.
4. Treat all four non-price triggers as evidence_url_pending=true and source_proxy_only=true until URL-level evidence is repaired.
5. Do not use these rows for positive weight promotion until filings/IR/export-data/channel-check/customs-data/report data verifies export orders, distributor reorder, overseas sell-through, channel inventory, product mix, input-cost/FX pass-through, and margin conversion.
6. Add a shadow-only rule candidate named C18_kfood_seafood_export_reorder_and_late_spike_high_mae_router.
7. Do not loosen Stage3-Green.
8. Add C18-specific guards:
   - source_proxy_only -> no Green
   - Green requires repaired export reorder / channel / margin bridge
   - MFE_90D >= +40% and MAE_90D > -10% may remain Stage2-Actionable / Yellow watch after evidence repair
   - MFE_30D >= +20% but MAE_90D <= -10% or MAE_180D <= -15% -> Stage2-Guarded at most until evidence repair
   - entry-day or first-5-day peak with MFE_30D < +5% and MAE_30D <= -25% or MAE_90D <= -40% -> block Stage2 / 4B-4C watch
9. Keep production scoring unchanged unless later batch promotion logic independently marks this axis safe.
```

---

## 15. Next round state

```text
completed_round = R5
completed_loop = 76
next_round = R6
next_loop = 76
next_large_sector_hint = L6_FINANCIAL_CAPITAL_RETURN_DIGITAL
round_schedule_status = valid
round_sector_consistency = pass
```
