# E2R Stock-Web v12 Residual Research — R4 Loop 73

```yaml
research_session: post_calibrated_sector_archetype_residual_research
mode: historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12
completed_round: R4
completed_loop: 73
next_round: R5
next_loop: 73
large_sector_id: L4_MATERIALS_SPREAD_RESOURCE
canonical_archetype_id: C16_STRATEGIC_RESOURCE_POLICY_SUPPLY
fine_archetype_id: RARE_METAL_TITANIUM_RARE_EARTH_SUPPLY_POLICY_HIGH_MAE_ROUTER
output_file: e2r_stock_web_v12_residual_round_R4_loop_73_L4_MATERIALS_SPREAD_RESOURCE_C16_STRATEGIC_RESOURCE_POLICY_SUPPLY_research.md
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
completed_loop  = 73
large_sector_id = L3_BATTERY_EV_GREEN_MOBILITY
canonical_archetype_id = C11_BATTERY_ORDERBOOK_RERATING
```

Therefore:

```text
scheduled_round = R4
scheduled_loop  = 73
```

R4 maps to:

```text
large_sector_id = L4_MATERIALS_SPREAD_RESOURCE
```

This run selects:

```text
canonical_archetype_id = C16_STRATEGIC_RESOURCE_POLICY_SUPPLY
fine_archetype_id = RARE_METAL_TITANIUM_RARE_EARTH_SUPPLY_POLICY_HIGH_MAE_ROUTER
```

This is a valid R4/L4 pairing.

---

## 1. Why this R4/C16 run

The no-repeat ledger shows C16 is moderately covered, but still less saturated than C17 and several later consumer/financial archetypes:

```text
C16_STRATEGIC_RESOURCE_POLICY_SUPPLY:
  rows: 52
  symbols: 20
  date_range: 2019-05-20~2024-02-28
  good/bad S2: 14/5
  4B/4C: 17/0
  URL/proxy: 4/4
  top covered symbols: 001570(7), 005490(6), 000910(5), 005290(4), 075970(4), 009520(3)
```

This run avoids those top-covered C16 names and adds three less-repeated strategic-resource / rare-metal / rare-earth-adjacent names:

```text
012320 경동인베스트
047400 유니온머티리얼
081150 티플랙스
```

Research question:

```text
Can C16 separate a real strategic-resource policy/supply bottleneck from resource-theme spikes where the price candle arrives before the investable supply, offtake, license, mining economics, or margin bridge?
```

C16 is a supply-chain archetype. The market often reacts to the first smell of scarcity, but scarcity only becomes Stage2/Green when it flows through a company-specific bridge: resource ownership, extraction path, customer/offtake, pricing, and cash-flow conversion. Without that bridge, a strategic resource rally is a flare: bright, visible, and easy to mistake for firepower.

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
| `012320` | 경동인베스트 | active_like / KOSPI | no 2024 overlap; latest listed candidate 2017-08-25 | true |
| `047400` | 유니온머티리얼 | active_like / KOSPI | no 2024 overlap; latest listed candidate 2011-04-29 | true |
| `081150` | 티플랙스 | active_like / KOSDAQ | no 2024 overlap; latest listed candidate 2012-10-25 | true |

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
The Stock-Web price path is fully validated, but company-level resource ownership, mining/extraction approval, strategic-resource policy link, customer/offtake, pricing bridge, and margin/cash-flow conversion evidence still require later URL repair through filings, government documents, company IR, commodity data, or archived reports before production weight promotion.
```

C16 interpretation used here:

```text
C16 is not simply “resource stock rose.”
It asks whether strategic-resource scarcity is company-convertible:
- policy relevance,
- domestic or allied supply-chain role,
- resource ownership or processing capability,
- customer/offtake or demand channel,
- margin bridge,
- and low-MAE follow-through.
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
012320 + C16_STRATEGIC_RESOURCE_POLICY_SUPPLY -> no direct match found
047400 + C16_STRATEGIC_RESOURCE_POLICY_SUPPLY -> no direct match found
081150 + C16_STRATEGIC_RESOURCE_POLICY_SUPPLY -> no direct match found
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
| `R4L73_C16_081150_20241011` | `081150` 티플랙스 | rare-metal/stainless strategic resource policy rally with contained MAE | positive-guarded / low-MAE holdout |
| `R4L73_C16_012320_20240322` | `012320` 경동인베스트 | titanium/resource-development option spike | high-MFE / high-MAE counterexample |
| `R4L73_C16_047400_20240715` | `047400` 유니온머티리얼 | rare-earth / magnet-material policy-theme relief rally | low-MFE / high-MAE counterexample |

The intended residual:

```text
C16 should separate:
1. rare-metal policy/supply names with contained MAE that may remain Stage2-Guarded;
2. strategic-resource option spikes that generate large MFE but quickly lose the non-price bridge;
3. rare-earth / material theme relief rallies where MFE is small and drawdown dominates.
```

---

## 6. Stock-Web OHLC and backtest

### 6.1 `081150` 티플랙스 — rare-metal policy rally with contained MAE

Trigger:

```text
trigger_date = 2024-10-10
trigger_type = Stage2-Actionable-Guarded
trigger_family = rare_metal_stainless_policy_supply_rally_contained_mae
entry_date = 2024-10-11
entry_price = 3135.0
entry_price_type = next_tradable_open_after_theme_burst
```

Relevant Stock-Web rows:

```csv
d,o,h,l,c,v,a,mc,s,m
2024-10-10,2700.0,3290.0,2700.0,3180.0,11664995.0,36204097475.0,77173518360.0,24268402,KOSDAQ
2024-10-11,3135.0,3245.0,2955.0,3015.0,2134788.0,6617747580.0,73169232030.0,24268402,KOSDAQ
2024-10-16,3050.0,3270.0,2955.0,3030.0,3556547.0,11168972700.0,73533258060.0,24268402,KOSDAQ
2024-10-28,3100.0,3390.0,3045.0,3300.0,3616674.0,11713274100.0,80085726600.0,24268402,KOSDAQ
2024-11-15,3260.0,3425.0,2920.0,2920.0,7472884.0,23857638645.0,70863733840.0,24268402,KOSDAQ
2024-12-09,2850.0,2890.0,2645.0,2645.0,678769.0,1865390135.0,64189923290.0,24268402,KOSDAQ
2025-02-03,3185.0,3615.0,3075.0,3245.0,20986927.0,71629138410.0,78750964490.0,24268402,KOSDAQ
2025-04-16,3380.0,3675.0,3215.0,3230.0,933807.0,3095657627.0,80935120670.0,24268402,KOSDAQ
```

Backtest:

| window | peak/high | peak date | trough/low | trough date | MFE | MAE |
|---|---:|---|---:|---|---:|---:|
| 30 calendar days | 3390 | 2024-10-28 | 2950 | 2024-10-17 | +8.13% | -5.90% |
| 90 calendar days | 3470 | 2024-11-29 | 2645 | 2024-12-09 | +10.69% | -15.63% |
| 180 calendar days | 3675 | 2025-04-16 | 2645 | 2024-12-09 | +17.22% | -15.63% |

Interpretation:

```text
081150 is the holdout positive-guarded case.
The return profile was not explosive, but MAE stayed below the severe-failure zone and later MFE improved.
This is not Green; it is a C16 Stage2-Guarded case that still needs URL-repaired rare-metal policy, customer/offtake, and margin evidence.
```

### 6.2 `012320` 경동인베스트 — titanium/resource option spike with high MAE

Trigger:

```text
trigger_date = 2024-03-21
trigger_type = 4B-local-watch
trigger_family = titanium_resource_development_option_spike
entry_date = 2024-03-22
entry_price = 95500.0
entry_price_type = next_tradable_open_after_resource_spike
```

Relevant Stock-Web rows:

```csv
d,o,h,l,c,v,a,mc,s,m
2024-03-21,62200.0,80400.0,61900.0,80400.0,475485.0,36011404000.0,190147849200.0,2365023,KOSPI
2024-03-22,95500.0,104400.0,81800.0,101300.0,2284686.0,216543438700.0,239576829900.0,2365023,KOSPI
2024-03-25,102100.0,123900.0,96900.0,110000.0,1122746.0,128266596100.0,260152530000.0,2365023,KOSPI
2024-04-12,73400.0,74100.0,69500.0,69500.0,68416.0,4859730300.0,164369098500.0,2365023,KOSPI
2024-06-27,81500.0,82800.0,81500.0,82100.0,8363.0,687141100.0,194168388300.0,2365023,KOSPI
2024-08-05,78700.0,80000.0,67200.0,69300.0,68058.0,4954964400.0,163896093900.0,2365023,KOSPI
2024-08-29,86700.0,91800.0,86300.0,87300.0,53111.0,4730323300.0,206466507900.0,2365023,KOSPI
2024-09-13,79200.0,79200.0,76400.0,77200.0,26010.0,2017551100.0,182579775600.0,2365023,KOSPI
```

Backtest:

| window | peak/high | peak date | trough/low | trough date | MFE | MAE |
|---|---:|---|---:|---|---:|---:|
| 30 calendar days | 123900 | 2024-03-25 | 69500 | 2024-04-12 | +29.74% | -27.23% |
| 90 calendar days | 123900 | 2024-03-25 | 69500 | 2024-04-12 | +29.74% | -27.23% |
| 180 calendar days | 123900 | 2024-03-25 | 67200 | 2024-08-05 | +29.74% | -29.63% |

Interpretation:

```text
012320 is a high-MFE/high-MAE C16 counterexample.
The first spike was real, but the drawdown quickly crossed the high-MAE zone.
This should remain local 4B/resource-option watch until resource economics, development path, licensing, offtake, and cash-flow bridge are repaired.
```

### 6.3 `047400` 유니온머티리얼 — rare-earth / magnet-material relief rally with low MFE and high MAE

Trigger:

```text
trigger_date = 2024-07-12
trigger_type = Stage2-FalsePositive-Candidate
trigger_family = rare_earth_magnet_material_policy_relief_rally
entry_date = 2024-07-15
entry_price = 2730.0
entry_price_type = next_tradable_open_after_theme_burst
```

Relevant Stock-Web rows:

```csv
d,o,h,l,c,v,a,mc,s,m
2024-07-12,2595.0,2595.0,2535.0,2550.0,109313.0,279114440.0,107100000000.0,42000000,KOSPI
2024-07-15,2730.0,2735.0,2625.0,2660.0,744663.0,1991532170.0,111720000000.0,42000000,KOSPI
2024-07-17,2910.0,2950.0,2680.0,2680.0,1861563.0,5263360175.0,112560000000.0,42000000,KOSPI
2024-08-05,2410.0,2470.0,2040.0,2095.0,630204.0,1414163045.0,87990000000.0,42000000,KOSPI
2024-09-09,1984.0,2045.0,1940.0,2035.0,89303.0,177663626.0,85470000000.0,42000000,KOSPI
2024-10-10,2195.0,2445.0,2195.0,2330.0,2686213.0,6267663475.0,97860000000.0,42000000,KOSPI
2025-01-09,2330.0,2420.0,2310.0,2415.0,562506.0,1333407785.0,101430000000.0,42000000,KOSPI
2025-01-17,2400.0,2460.0,2395.0,2460.0,457332.0,1114286595.0,103320000000.0,42000000,KOSPI
```

Backtest:

| window | peak/high | peak date | trough/low | trough date | MFE | MAE |
|---|---:|---|---:|---|---:|---:|
| 30 calendar days | 2950 | 2024-07-17 | 2040 | 2024-08-05 | +8.06% | -25.27% |
| 90 calendar days | 2950 | 2024-07-17 | 1940 | 2024-09-09 | +8.06% | -28.94% |
| 180 calendar days | 2950 | 2024-07-17 | 1940 | 2024-09-09 | +8.06% | -28.94% |

Interpretation:

```text
047400 is the clean low-MFE/high-MAE counterexample.
The rare-earth / magnet-material theme was plausible, but the price path offered little remaining upside after entry and quickly produced severe drawdown.
This should block Stage2/Green unless a company-specific supply-chain bridge appears before the move.
```

---

## 7. Machine-readable trigger JSONL

```jsonl
{"row_type":"trigger","research_id":"R4L73_C16_RARE_METAL_RESOURCE_POLICY","round":"R4","loop":73,"large_sector_id":"L4_MATERIALS_SPREAD_RESOURCE","canonical_archetype_id":"C16_STRATEGIC_RESOURCE_POLICY_SUPPLY","fine_archetype_id":"RARE_METAL_TITANIUM_RARE_EARTH_SUPPLY_POLICY_HIGH_MAE_ROUTER","symbol":"081150","name":"티플랙스","trigger_type":"Stage2-Actionable-Guarded","trigger_family":"rare_metal_stainless_policy_supply_rally_contained_mae","trigger_date":"2024-10-10","entry_date":"2024-10-11","entry_price":3135.0,"entry_price_type":"next_tradable_open_after_theme_burst","price_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","mfe_30d_pct":8.13,"mae_30d_pct":-5.90,"mfe_90d_pct":10.69,"mae_90d_pct":-15.63,"mfe_180d_pct":17.22,"mae_180d_pct":-15.63,"peak_price_180d":3675.0,"peak_date_180d":"2025-04-16","trough_price_180d":2645.0,"trough_date_180d":"2024-12-09","calibration_usable":true,"case_polarity":"positive_guarded_low_mae_holdout","evidence_url_pending":true,"source_proxy_only":true,"non_price_evidence_strength":"medium_low_pending_url_repair","price_only_blowoff":false,"expected_stage_current_profile":"Stage2-Guarded_only_until_rare_metal_policy_offtake_margin_bridge_repaired","residual_error_type":"contained_mae_policy_supply_case_but_green_requires_company_specific_bridge"}
{"row_type":"trigger","research_id":"R4L73_C16_RARE_METAL_RESOURCE_POLICY","round":"R4","loop":73,"large_sector_id":"L4_MATERIALS_SPREAD_RESOURCE","canonical_archetype_id":"C16_STRATEGIC_RESOURCE_POLICY_SUPPLY","fine_archetype_id":"RARE_METAL_TITANIUM_RARE_EARTH_SUPPLY_POLICY_HIGH_MAE_ROUTER","symbol":"012320","name":"경동인베스트","trigger_type":"4B-local-watch","trigger_family":"titanium_resource_development_option_spike","trigger_date":"2024-03-21","entry_date":"2024-03-22","entry_price":95500.0,"entry_price_type":"next_tradable_open_after_resource_spike","price_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","mfe_30d_pct":29.74,"mae_30d_pct":-27.23,"mfe_90d_pct":29.74,"mae_90d_pct":-27.23,"mfe_180d_pct":29.74,"mae_180d_pct":-29.63,"peak_price_180d":123900.0,"peak_date_180d":"2024-03-25","trough_price_180d":67200.0,"trough_date_180d":"2024-08-05","calibration_usable":true,"case_polarity":"counterexample_high_mfe_high_mae","evidence_url_pending":true,"source_proxy_only":true,"non_price_evidence_strength":"low_pending_url_repair","price_only_blowoff":false,"expected_stage_current_profile":"4B_local_watch_until_resource_economics_offtake_cashflow_bridge_repaired","residual_error_type":"resource_option_spike_large_mfe_but_high_mae_blocks_green"}
{"row_type":"trigger","research_id":"R4L73_C16_RARE_METAL_RESOURCE_POLICY","round":"R4","loop":73,"large_sector_id":"L4_MATERIALS_SPREAD_RESOURCE","canonical_archetype_id":"C16_STRATEGIC_RESOURCE_POLICY_SUPPLY","fine_archetype_id":"RARE_METAL_TITANIUM_RARE_EARTH_SUPPLY_POLICY_HIGH_MAE_ROUTER","symbol":"047400","name":"유니온머티리얼","trigger_type":"Stage2-FalsePositive-Candidate","trigger_family":"rare_earth_magnet_material_policy_relief_rally","trigger_date":"2024-07-12","entry_date":"2024-07-15","entry_price":2730.0,"entry_price_type":"next_tradable_open_after_theme_burst","price_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","mfe_30d_pct":8.06,"mae_30d_pct":-25.27,"mfe_90d_pct":8.06,"mae_90d_pct":-28.94,"mfe_180d_pct":8.06,"mae_180d_pct":-28.94,"peak_price_180d":2950.0,"peak_date_180d":"2024-07-17","trough_price_180d":1940.0,"trough_date_180d":"2024-09-09","calibration_usable":true,"case_polarity":"counterexample_low_mfe_high_mae","evidence_url_pending":true,"source_proxy_only":true,"non_price_evidence_strength":"low_pending_url_repair","price_only_blowoff":true,"expected_stage_current_profile":"blocked_Stage2_or_4B_high_MAE_watch","residual_error_type":"rare_earth_theme_relief_entry_low_mfe_high_mae_without_company_bridge"}
```

---

## 8. Score simulation and raw component breakdown

This is shadow-only and does not change production scoring.

| symbol | policy/supply relevance | resource/processing bridge | customer/offtake visibility | market mispricing | valuation rerating | project/cash-flow risk control | information confidence | shadow total | intended route |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| `081150` | 10 | 8 | 6 | 7 | 6 | 7 | 6 | 50 | Stage2-Guarded holdout; no Green until bridge repair |
| `012320` | 13 | 6 | 3 | 14 | 12 | 2 | 5 | 55 | local 4B/resource-option watch |
| `047400` | 10 | 4 | 3 | 6 | 5 | 3 | 4 | 35 | blocked Stage2 / 4B high-MAE watch |

### Current calibrated profile stress test

The current calibrated profile already blocks price-only blowoff.  
The remaining C16 risk is **theme-to-company bridge quality**:

```text
C16 cleaner path:
  strategic-resource policy relevance
  + contained MAE
  + company-specific processing/offtake/margin bridge
  => Stage2-Actionable-Guarded first, then Yellow only after evidence repair

C16 resource-option spike:
  resource scarcity or development option
  + high MFE
  + MAE <= -25%
  + source_proxy_only evidence
  => local 4B/high-MAE watch, not Green

C16 rare-earth/magnet theme false-positive:
  plausible policy theme
  + low post-entry MFE
  + 30D/90D MAE <= -25%
  + no company-specific bridge
  => block Stage2 and route to 4B watch
```

`081150` prevents overblocking because its path was relatively contained.  
`012320` shows why even large MFE must be discounted when the resource economics bridge is missing.  
`047400` is the clean false-positive case: policy theme present, but post-entry return/risk alignment failed.

---

## 9. Aggregate metrics

```json
{
  "row_type": "aggregate",
  "research_id": "R4L73_C16_RARE_METAL_RESOURCE_POLICY",
  "round": "R4",
  "loop": 73,
  "large_sector_id": "L4_MATERIALS_SPREAD_RESOURCE",
  "canonical_archetype_id": "C16_STRATEGIC_RESOURCE_POLICY_SUPPLY",
  "fine_archetype_id": "RARE_METAL_TITANIUM_RARE_EARTH_SUPPLY_POLICY_HIGH_MAE_ROUTER",
  "case_count": 3,
  "calibration_usable_case_count": 3,
  "positive_guarded_case_count": 1,
  "counterexample_count": 2,
  "new_symbol_count": 3,
  "source_proxy_only_count": 3,
  "evidence_url_pending_count": 3,
  "avg_mfe_30d_pct": 15.31,
  "avg_mae_30d_pct": -19.47,
  "avg_mfe_90d_pct": 16.16,
  "avg_mae_90d_pct": -23.93,
  "avg_mfe_180d_pct": 18.34,
  "avg_mae_180d_pct": -24.73,
  "max_mfe_180d_pct": 29.74,
  "worst_mae_180d_pct": -29.63
}
```

---

## 10. 4B proximity split

```json
{
  "row_type": "4b_split",
  "research_id": "R4L73_C16_RARE_METAL_RESOURCE_POLICY",
  "stage2_guarded_holdout": [
    {
      "symbol": "081150",
      "reason": "resource-policy theme had modest MFE but contained MAE; requires URL-repaired processing/offtake/margin bridge before Yellow/Green"
    }
  ],
  "local_4b_watch": [
    {
      "symbol": "012320",
      "reason": "titanium/resource option spike had +29.74% MFE but -29.63% 180D MAE"
    },
    {
      "symbol": "047400",
      "reason": "rare-earth/magnet material relief entry had only +8.06% MFE and -28.94% MAE"
    }
  ],
  "full_4b_or_green_requires_non_price_evidence": [
    "resource ownership or processing capacity",
    "license / development path",
    "customer or offtake bridge",
    "commodity pricing-to-margin bridge",
    "cash-flow or earnings conversion"
  ]
}
```

---

## 11. Shadow rule candidate

```yaml
row_type: canonical_archetype_rule_candidate
canonical_archetype_id: C16_STRATEGIC_RESOURCE_POLICY_SUPPLY
fine_archetype_id: RARE_METAL_TITANIUM_RARE_EARTH_SUPPLY_POLICY_HIGH_MAE_ROUTER
rule_name: C16_strategic_resource_company_bridge_and_high_mae_router
production_scoring_changed: false
shadow_weight_only: true
```

### Proposed routing logic

```text
For C16 strategic-resource policy/supply cases:

Tier A: verified company-convertible strategic resource
  Conditions:
    - resource/policy relevance is clear
    - company-specific ownership, processing, offtake, customer, or margin bridge is URL-repaired
    - 30D/90D MAE remains contained
  Routing:
    - Stage2-Actionable-Guarded allowed
    - Stage3-Yellow allowed after evidence repair
    - Green only after resource economics and margin/cash-flow bridge are verified

Tier B: resource-option spike without economics bridge
  Conditions:
    - resource scarcity/development theme creates MFE
    - source_proxy_only or evidence_url_pending remains true
    - 30D or 180D MAE <= -25%
  Routing:
    - local 4B/high-MAE watch
    - no Green
    - no production positive weight promotion

Tier C: low-MFE policy-theme relief rally
  Conditions:
    - policy theme is plausible
    - MFE_30D < +10%
    - MAE_30D <= -20%
    - company-specific bridge missing
  Routing:
    - block Stage2
    - count as false-positive counterexample
```

### Suggested shadow delta

```json
{
  "row_type": "shadow_weight",
  "axis": "c16_strategic_resource_company_bridge_and_high_mae_router",
  "scope": "canonical_archetype_id:C16_STRATEGIC_RESOURCE_POLICY_SUPPLY",
  "proposal": {
    "source_proxy_only_green_allowed": false,
    "company_specific_resource_offtake_margin_bridge_required_for_green": true,
    "resource_option_spike_stage2_cap": "local_4b_until_url_repair",
    "high_mae_watch_threshold_pct": -25.0,
    "low_mfe_theme_relief_blocks_stage2": true,
    "positive_weight_blocked_until_url_repair": true
  },
  "confidence": "medium_low_until_url_repair",
  "apply_now": false,
  "reason": "One contained-MAE rare-metal holdout and two resource-theme high-MAE counterexamples show that C16 should not promote strategic-resource policy relevance without a company-specific processing/offtake/margin bridge."
}
```

---

## 12. Residual contribution summary

```json
{
  "row_type": "residual_contribution",
  "research_id": "R4L73_C16_RARE_METAL_RESOURCE_POLICY",
  "large_sector_id": "L4_MATERIALS_SPREAD_RESOURCE",
  "canonical_archetype_id": "C16_STRATEGIC_RESOURCE_POLICY_SUPPLY",
  "contribution": "Adds three non-top-covered C16 strategic-resource / rare-metal cases and separates a contained-MAE policy-supply holdout from titanium/resource-option and rare-earth/magnet-theme counterexamples. C16 Green should require URL-repaired company-specific resource ownership, processing/offtake, margin, and cash-flow bridge evidence.",
  "positive_guarded_case_added": 1,
  "counterexample_case_added": 2,
  "new_symbol_count": 3,
  "data_quality_blocker": "All three non-price strategic-resource triggers require URL-level repair before positive weight promotion.",
  "guardrail_added": "C16 source_proxy_only resource-option spikes with MAE worse than -25% should route to local 4B/high-MAE watch; low-MFE policy-theme relief entries should block Stage2."
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
    081150: false
    012320: false
    047400: false
  evidence_url_pending:
    081150: true
    012320: true
    047400: true
  source_proxy_only:
    081150: true
    012320: true
    047400: true
```

Limitations:

```text
- Price path is validated against Stock-Web tradable OHLC rows.
- Non-price evidence is not URL-repaired in this run.
- Therefore this artifact is useful for C16 residual shape and high-MAE guardrail design, but should not promote positive weights until filings/IR/government-document/commodity/report data verifies resource ownership, processing capability, licensing, offtake, pricing, margin, and cash-flow conversion.
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
2. Preserve R4 / loop 73 metadata.
3. Add the cases to C16_STRATEGIC_RESOURCE_POLICY_SUPPLY only if parser validation passes.
4. Treat all three non-price triggers as evidence_url_pending=true and source_proxy_only=true until URL-level evidence is repaired.
5. Do not use these rows for positive weight promotion until filings/IR/government-document/commodity/report data verifies resource ownership, processing capability, licensing/development path, offtake, pricing, margin, and cash-flow conversion.
6. Add a shadow-only rule candidate named C16_strategic_resource_company_bridge_and_high_mae_router.
7. Do not loosen Stage3-Green.
8. Add C16-specific guards:
   - source_proxy_only -> no Green
   - resource-option spike with MAE <= -25% -> local 4B/high-MAE watch
   - MFE_30D < +10% and MAE_30D <= -20% without company bridge -> block Stage2
   - Green requires repaired company-specific resource/offtake/margin/cash-flow bridge
9. Keep production scoring unchanged unless later batch promotion logic independently marks this axis safe.
```

---

## 15. Next round state

```text
completed_round = R4
completed_loop = 73
next_round = R5
next_loop = 73
next_large_sector_hint = L5_CONSUMER_BRAND_DISTRIBUTION
```
