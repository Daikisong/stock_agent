# E2R Stock-Web v12 Residual Research — R2 Loop 73

```yaml
research_session: post_calibrated_sector_archetype_residual_research
mode: historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12
completed_round: R2
completed_loop: 73
next_round: R3
next_loop: 73
large_sector_id: L2_AI_SEMICONDUCTOR_ELECTRONICS
canonical_archetype_id: C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY
fine_archetype_id: HBM_TEST_OSAT_SECOND_TIER_CUSTOMER_QUALITY_AND_HIGH_MAE_ROUTER
output_file: e2r_stock_web_v12_residual_round_R2_loop_73_L2_AI_SEMICONDUCTOR_ELECTRONICS_C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY_research.md
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

The active prompt fixes the research mode:

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
completed_loop  = 73
large_sector_id = L1_INDUSTRIALS_INFRA_DEFENSE_GRID
canonical_archetype_id = C02_POWER_GRID_DATACENTER_CAPEX
```

Therefore:

```text
scheduled_round = R2
scheduled_loop  = 73
```

R2 maps to:

```text
large_sector_id = L2_AI_SEMICONDUCTOR_ELECTRONICS
```

This run selects:

```text
canonical_archetype_id = C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY
fine_archetype_id = HBM_TEST_OSAT_SECOND_TIER_CUSTOMER_QUALITY_AND_HIGH_MAE_ROUTER
```

This is a valid R2/L2 pairing.

---

## 1. Why this R2/C08 run

The no-repeat ledger shows C08 is already reasonably covered, but the top symbols are concentrated in socket / interface / test-quality names:

```text
C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY:
  rows: 66
  symbols: 14
  date_range: 2023-03-30~2024-09-26
  good/bad S2: 21/7
  4B/4C: 16/1
  URL/proxy: 0/0
  top covered symbols: 098120(11), 058470(8), 080580(7), 095340(7), 131290(7), 219130(6)
```

This file deliberately adds three less-repeated or non-top-covered test / OSAT / test-equipment names:

```text
089030 테크윙
067310 하나마이크론
092870 엑시콘
```

The residual question is:

```text
Can C08 separate a true HBM/test-equipment quality winner from OSAT/test-equipment beta rallies that initially look like Stage2 but later carry severe MAE without verified customer-quality evidence?
```

C08 is a customer-quality archetype. It should not only ask whether a stock is “near HBM” or “near semiconductor test.” It should ask whether the customer bridge is strong enough to hold the weight: qualification, repeat order, customer mix, utilization, and margin conversion. A test socket or handler story is like a probe card: the market may touch the pad, but the signal only counts if the electrical contact is clean.

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
| `089030` | 테크윙 | active_like / KOSDAQ | no 2024 overlap; latest listed candidates are 2022-08-01 and 2022-08-23 | true |
| `067310` | 하나마이크론 | active_like / KOSDAQ/KOSDAQ GLOBAL history | no 2024 overlap; latest listed candidate 2021-12-29 | true |
| `092870` | 엑시콘 | active_like / KOSDAQ | 2024-07-31 candidate exists; this file uses a post-candidate 2024-08-01 entry, so entry~D+180 is treated as usable | true after corporate-action window |

Profile caveat:

```text
Stock-Web OHLC is raw/unadjusted marcap data.
092870 has a 2024-07-31 corporate-action candidate, so this file deliberately avoids pre-2024-07-31 entries and uses 2024-08-01 as a post-window trigger.
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
The Stock-Web price path is fully validated, but company-level test handler / burn-in / OSAT / test-equipment customer qualification, HBM customer bridge, utilization, backlog, repeat order, margin conversion, and customer concentration evidence still require later URL repair through filings, IR decks, customer disclosures, export data, or sell-side reports before any production weight promotion.
```

C08 interpretation used here:

```text
C08 is not simply “semiconductor test stock went up.”
It asks whether the test/socket/equipment company is attached to a high-quality customer bridge:
- customer qualification,
- repeat order visibility,
- HBM or advanced packaging demand,
- utilization and margin conversion,
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
089030 + C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY -> no direct match found
067310 + C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY -> no direct match found
092870 + C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY -> no direct match found
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
| `R2L73_C08_089030_20240213` | `089030` 테크윙 | HBM/test-handler customer-quality breakout | positive anchor / low-MAE persistent rerating |
| `R2L73_C08_067310_20240327` | `067310` 하나마이크론 | OSAT/advanced packaging beta rally before utilization fade | counterexample / high-MAE after early MFE |
| `R2L73_C08_092870_20240801` | `092870` 엑시콘 | post-corporate-action test-equipment relief rally failure | counterexample / immediate high-MAE guard |

The intended residual:

```text
C08 should separate:
1. true test-handler/socket customer-quality winners with persistent MFE and contained MAE;
2. OSAT or test-equipment beta rallies that have early MFE but later collapse without verified customer/utilization bridge;
3. post-adjustment relief attempts where corporate-action-safe entry still fails to produce MFE.
```

---

## 6. Stock-Web OHLC and backtest

### 6.1 `089030` 테크윙 — HBM/test-handler customer-quality positive anchor

Trigger:

```text
trigger_date = 2024-02-08
trigger_type = Stage2-Actionable
trigger_family = HBM_test_handler_customer_quality_breakout
entry_date = 2024-02-13
entry_price = 18200.0
entry_price_type = next_tradable_open
```

Relevant Stock-Web rows:

```csv
d,o,h,l,c,v,a,mc,s,m
2024-02-08,15490.0,17640.0,15490.0,17400.0,3200495.0,53478356970.0,649953423000.0,37353645,KOSDAQ
2024-02-13,18200.0,19970.0,18090.0,18690.0,5859501.0,111737150520.0,698139625050.0,37353645,KOSDAQ
2024-02-19,18210.0,21800.0,18070.0,21550.0,7745873.0,159588823220.0,804971049750.0,37353645,KOSDAQ
2024-03-15,28600.0,30850.0,27800.0,30300.0,1230532.0,35920895300.0,1131815443500.0,37353645,KOSDAQ
2024-04-11,33650.0,39100.0,33350.0,38700.0,2637442.0,97864810200.0,1445586061500.0,37353645,KOSDAQ
2024-05-28,40900.0,45200.0,40550.0,43500.0,1916853.0,83046502300.0,1624883557500.0,37353645,KOSDAQ
2024-06-27,54000.0,59800.0,53300.0,59100.0,1324663.0,76380432400.0,2207600419500.0,37353645,KOSDAQ
2024-07-11,67800.0,70800.0,67200.0,68700.0,874088.0,60222114100.0,2566195411500.0,37353645,KOSDAQ
```

Backtest:

| window | peak/high | peak date | trough/low | trough date | MFE | MAE |
|---|---:|---|---:|---|---:|---:|
| 30 calendar days | 29500 | 2024-03-14 | 17560 | 2024-02-14 | +62.09% | -3.52% |
| 90 calendar days | 39100 | 2024-04-11 | 17560 | 2024-02-14 | +114.84% | -3.52% |
| 180 calendar days | 70800 | 2024-07-11 | 17560 | 2024-02-14 | +289.01% | -3.52% |

Interpretation:

```text
089030 is the clean positive anchor.
The price path was not only high-MFE; it was low-MAE and persistent.
This is the C08 pattern worth rewarding after URL repair: customer-quality story + test-equipment bottleneck + sustained relative strength.
```

### 6.2 `067310` 하나마이크론 — OSAT/advanced-packaging beta with later high-MAE

Trigger:

```text
trigger_date = 2024-03-26
trigger_type = Stage2-Actionable-Guarded
trigger_family = OSAT_advanced_packaging_beta_rally_without_verified_utilization_bridge
entry_date = 2024-03-27
entry_price = 25500.0
entry_price_type = next_tradable_open
```

Relevant Stock-Web rows:

```csv
d,o,h,l,c,v,a,mc,s,m
2024-03-27,25500.0,29750.0,25350.0,28150.0,15731208.0,448550276950.0,1353287435100.0,48074154,KOSDAQ GLOBAL
2024-03-29,29200.0,29600.0,28100.0,28650.0,7785025.0,219228491967.0,1493710008750.0,52136475,KOSDAQ GLOBAL
2024-04-04,28300.0,34500.0,28200.0,33300.0,29965507.0,971845642900.0,1736144617500.0,52136475,KOSDAQ GLOBAL
2024-04-19,28650.0,28750.0,26400.0,27150.0,4084715.0,111924417600.0,1415505296250.0,52136475,KOSDAQ GLOBAL
2024-05-20,22950.0,23600.0,22500.0,22850.0,4319869.0,99237638700.0,1192072503750.0,52169475,KOSDAQ GLOBAL
2024-06-25,20850.0,21150.0,20350.0,20550.0,624400.0,12882449350.0,1072082711250.0,52169475,KOSDAQ
2024-09-11,10930.0,11160.0,10690.0,10900.0,504025.0,5478105090.0,716619366400.0,65744896,KOSDAQ
2024-09-26,12280.0,12300.0,11970.0,12130.0,989826.0,12011494920.0,797485588480.0,65744896,KOSDAQ
```

Backtest:

| window | peak/high | peak date | trough/low | trough date | MFE | MAE |
|---|---:|---|---:|---|---:|---:|
| 30 calendar days | 34500 | 2024-04-04 | 25350 | 2024-03-27 | +35.29% | -0.59% |
| 90 calendar days | 34500 | 2024-04-04 | 20350 | 2024-06-25 | +35.29% | -20.20% |
| 180 calendar days | 34500 | 2024-04-04 | 10690 | 2024-09-11 | +35.29% | -58.08% |

Interpretation:

```text
067310 is the high-MFE/high-MAE counterexample.
The first month looked like Stage2: big MFE and almost no early MAE.
But the 90D/180D path exposed the missing bridge: without verified utilization, customer quality, and margin conversion, OSAT beta can unwind violently.
```

### 6.3 `092870` 엑시콘 — post-corporate-action test-equipment relief attempt that failed

Trigger:

```text
trigger_date = 2024-07-31
trigger_type = 4B-local-watch
trigger_family = post_corporate_action_test_equipment_relief_failure
entry_date = 2024-08-01
entry_price = 19150.0
entry_price_type = next_tradable_open_after_corporate_action_candidate
corporate_action_handling = post_2024_07_31_entry_only
```

Relevant Stock-Web rows:

```csv
d,o,h,l,c,v,a,mc,s,m
2024-07-31,17840.0,18600.0,17270.0,18350.0,814284.0,14715587880.0,239482124950.0,13050797,KOSDAQ
2024-08-01,19150.0,19190.0,17730.0,17840.0,551630.0,10142362420.0,232826218480.0,13050797,KOSDAQ
2024-08-05,15400.0,15490.0,11250.0,13050.0,941204.0,13086706400.0,170312900850.0,13050797,KOSDAQ
2024-08-29,12430.0,12610.0,12220.0,12500.0,214484.0,2652623220.0,163134962500.0,13050797,KOSDAQ
2024-09-09,10010.0,10910.0,10000.0,10880.0,198576.0,2079801500.0,141992671360.0,13050797,KOSDAQ
2024-09-26,12420.0,14660.0,12110.0,13810.0,6890008.0,93928741010.0,180231506570.0,13050797,KOSDAQ
2024-10-31,11410.0,13640.0,11220.0,12390.0,4396604.0,56618388570.0,161699374830.0,13050797,KOSDAQ
2025-01-20,13330.0,13900.0,13150.0,13870.0,343926.0,4701182430.0,181014554390.0,13050797,KOSDAQ
```

Backtest:

| window | peak/high | peak date | trough/low | trough date | MFE | MAE |
|---|---:|---|---:|---|---:|---:|
| 30 calendar days | 19190 | 2024-08-01 | 12220 | 2024-08-29 | +0.21% | -36.19% |
| 90 calendar days | 19190 | 2024-08-01 | 10000 | 2024-09-09 | +0.21% | -47.78% |
| 180 calendar days | 19190 | 2024-08-01 | 10000 | 2024-09-09 | +0.21% | -47.78% |

Interpretation:

```text
092870 is the clean post-adjustment failure case.
Even after avoiding the 2024-07-31 corporate-action candidate window, the post-window trigger had almost no upside and severe MAE.
This should be 4B/local-watch or blocked Stage2 until a hard order/customer bridge is repaired.
```

---

## 7. Machine-readable trigger JSONL

```jsonl
{"row_type":"trigger","research_id":"R2L73_C08_HBM_TEST_OSAT_QUALITY","round":"R2","loop":73,"large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY","fine_archetype_id":"HBM_TEST_OSAT_SECOND_TIER_CUSTOMER_QUALITY_AND_HIGH_MAE_ROUTER","symbol":"089030","name":"테크윙","trigger_type":"Stage2-Actionable","trigger_family":"HBM_test_handler_customer_quality_breakout","trigger_date":"2024-02-08","entry_date":"2024-02-13","entry_price":18200.0,"entry_price_type":"next_tradable_open","price_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","mfe_30d_pct":62.09,"mae_30d_pct":-3.52,"mfe_90d_pct":114.84,"mae_90d_pct":-3.52,"mfe_180d_pct":289.01,"mae_180d_pct":-3.52,"peak_price_180d":70800.0,"peak_date_180d":"2024-07-11","trough_price_180d":17560.0,"trough_date_180d":"2024-02-14","calibration_usable":true,"case_polarity":"positive_anchor","evidence_url_pending":true,"source_proxy_only":true,"non_price_evidence_strength":"medium_pending_url_repair","price_only_blowoff":false,"expected_stage_current_profile":"Stage2-Actionable_to_Yellow_or_Green_after_customer_quality_evidence_repaired","residual_error_type":"positive_anchor_requires_url_repaired_customer_order_margin_bridge_before_green"}
{"row_type":"trigger","research_id":"R2L73_C08_HBM_TEST_OSAT_QUALITY","round":"R2","loop":73,"large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY","fine_archetype_id":"HBM_TEST_OSAT_SECOND_TIER_CUSTOMER_QUALITY_AND_HIGH_MAE_ROUTER","symbol":"067310","name":"하나마이크론","trigger_type":"Stage2-Actionable-Guarded","trigger_family":"OSAT_advanced_packaging_beta_rally_without_verified_utilization_bridge","trigger_date":"2024-03-26","entry_date":"2024-03-27","entry_price":25500.0,"entry_price_type":"next_tradable_open","price_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","mfe_30d_pct":35.29,"mae_30d_pct":-0.59,"mfe_90d_pct":35.29,"mae_90d_pct":-20.20,"mfe_180d_pct":35.29,"mae_180d_pct":-58.08,"peak_price_180d":34500.0,"peak_date_180d":"2024-04-04","trough_price_180d":10690.0,"trough_date_180d":"2024-09-11","calibration_usable":true,"case_polarity":"counterexample_high_mfe_high_mae","evidence_url_pending":true,"source_proxy_only":true,"non_price_evidence_strength":"low_pending_url_repair","price_only_blowoff":false,"expected_stage_current_profile":"Stage2_Guarded_or_4B_high_MAE_watch_until_utilization_customer_bridge_repaired","residual_error_type":"early_osat_mfe_was_overwhelmed_by_later_high_mae_without_verified_customer_quality"}
{"row_type":"trigger","research_id":"R2L73_C08_HBM_TEST_OSAT_QUALITY","round":"R2","loop":73,"large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY","fine_archetype_id":"HBM_TEST_OSAT_SECOND_TIER_CUSTOMER_QUALITY_AND_HIGH_MAE_ROUTER","symbol":"092870","name":"엑시콘","trigger_type":"4B-local-watch","trigger_family":"post_corporate_action_test_equipment_relief_failure","trigger_date":"2024-07-31","entry_date":"2024-08-01","entry_price":19150.0,"entry_price_type":"next_tradable_open_after_corporate_action_candidate","price_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","mfe_30d_pct":0.21,"mae_30d_pct":-36.19,"mfe_90d_pct":0.21,"mae_90d_pct":-47.78,"mfe_180d_pct":0.21,"mae_180d_pct":-47.78,"peak_price_180d":19190.0,"peak_date_180d":"2024-08-01","trough_price_180d":10000.0,"trough_date_180d":"2024-09-09","calibration_usable":true,"case_polarity":"counterexample_post_adjustment_failure","evidence_url_pending":true,"source_proxy_only":true,"non_price_evidence_strength":"low_pending_url_repair","price_only_blowoff":false,"expected_stage_current_profile":"4B_local_watch_or_blocked_positive_stage","residual_error_type":"post_corporate_action_test_equipment_relief_attempt_low_mfe_extreme_mae"}
```

---

## 8. Score simulation and raw component breakdown

This is shadow-only and does not change production scoring.

| symbol | customer-quality bridge | test/socket bottleneck | order/utilization visibility | market mispricing | valuation rerating | capital allocation | information confidence | shadow total | intended route |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| `089030` | 15 | 17 | 14 | 15 | 18 | 5 | 7 | 91 | Stage2/Yellow; Green only after customer-quality evidence repair |
| `067310` | 7 | 7 | 5 | 11 | 10 | 4 | 5 | 49 | Stage2-Guarded or 4B/high-MAE watch |
| `092870` | 4 | 6 | 3 | 4 | 3 | 3 | 4 | 27 | 4B-local-watch / blocked Stage2 |

### Current calibrated profile stress test

The current calibrated profile already blocks pure price-only blowoff.  
The remaining C08 problem is more subtle:

```text
C08 clean positive path:
  test/socket/customer-quality exposure
  + persistent MFE
  + contained MAE
  + repaired customer/order/margin evidence
  => Stage2-Actionable / Yellow, possible Green

C08 OSAT/test-equipment beta path:
  semiconductor test/packaging exposure
  + early MFE
  + evidence still source-proxy-only
  + 90D MAE <= -20% or 180D MAE <= -40%
  => Stage2-Guarded or 4B/high-MAE watch; no Green

C08 post-adjustment failure path:
  corporate-action-safe post-window entry
  + no follow-through MFE
  + severe MAE
  => block Stage2 / local 4B watch
```

`089030` prevents overblocking.  
`067310` shows why early MFE is insufficient.  
`092870` shows that even a corporate-action-safe post-window entry can fail if the customer/order bridge is absent.

---

## 9. Aggregate metrics

```json
{
  "row_type": "aggregate",
  "research_id": "R2L73_C08_HBM_TEST_OSAT_QUALITY",
  "round": "R2",
  "loop": 73,
  "large_sector_id": "L2_AI_SEMICONDUCTOR_ELECTRONICS",
  "canonical_archetype_id": "C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY",
  "fine_archetype_id": "HBM_TEST_OSAT_SECOND_TIER_CUSTOMER_QUALITY_AND_HIGH_MAE_ROUTER",
  "case_count": 3,
  "calibration_usable_case_count": 3,
  "positive_anchor_count": 1,
  "counterexample_count": 2,
  "new_symbol_count": 3,
  "source_proxy_only_count": 3,
  "evidence_url_pending_count": 3,
  "avg_mfe_30d_pct": 32.53,
  "avg_mae_30d_pct": -13.43,
  "avg_mfe_90d_pct": 50.11,
  "avg_mae_90d_pct": -23.83,
  "avg_mfe_180d_pct": 108.17,
  "avg_mae_180d_pct": -36.46,
  "max_mfe_180d_pct": 289.01,
  "worst_mae_180d_pct": -58.08
}
```

---

## 10. 4B proximity split

```json
{
  "row_type": "4b_split",
  "research_id": "R2L73_C08_HBM_TEST_OSAT_QUALITY",
  "stage2_positive_or_yellow_candidate": [
    {
      "symbol": "089030",
      "reason": "persistent MFE and contained MAE; requires URL-repaired customer/order/margin bridge before Green"
    }
  ],
  "local_4b_watch": [
    {
      "symbol": "067310",
      "reason": "early MFE was useful, but 90D MAE crossed -20% and 180D MAE reached -58.08%"
    },
    {
      "symbol": "092870",
      "reason": "post-corporate-action-safe entry had only +0.21% MFE and -47.78% MAE"
    }
  ],
  "full_4b_or_green_requires_non_price_evidence": [
    "named customer or customer-quality evidence",
    "test handler / socket / burn-in equipment order bridge",
    "OSAT utilization improvement",
    "repeat order or backlog conversion",
    "margin bridge after customer qualification"
  ]
}
```

---

## 11. Shadow rule candidate

```yaml
row_type: canonical_archetype_rule_candidate
canonical_archetype_id: C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY
fine_archetype_id: HBM_TEST_OSAT_SECOND_TIER_CUSTOMER_QUALITY_AND_HIGH_MAE_ROUTER
rule_name: C08_hbm_test_osat_customer_quality_and_high_mae_router
production_scoring_changed: false
shadow_weight_only: true
```

### Proposed routing logic

```text
For C08 semi test/socket/customer-quality cases:

Tier A: verified customer-quality test/socket winner
  Conditions:
    - direct test/socket/test-handler/customer qualification evidence
    - order/backlog/utilization or margin bridge is URL-repaired
    - 30D/90D MAE is contained
    - MFE persists beyond the first spike
  Routing:
    - Stage2-Actionable allowed
    - Stage3-Yellow allowed after evidence repair
    - Green only after customer-quality and margin bridge evidence is verified

Tier B: OSAT/test-equipment beta without verified bridge
  Conditions:
    - semiconductor packaging/test exposure is plausible
    - early MFE is positive
    - source_proxy_only or evidence_url_pending remains true
    - 90D MAE <= -20% or 180D MAE <= -40%
  Routing:
    - Stage2-Actionable-Guarded at most
    - local 4B/high-MAE watch
    - no Green

Tier C: post-adjustment or post-theme relief failure
  Conditions:
    - corporate-action-safe entry exists
    - MFE is weak
    - MAE is severe
    - no repaired customer/order bridge
  Routing:
    - block Stage2
    - count as counterexample
```

### Suggested shadow delta

```json
{
  "row_type": "shadow_weight",
  "axis": "c08_hbm_test_osat_customer_quality_and_high_mae_router",
  "scope": "canonical_archetype_id:C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY",
  "proposal": {
    "source_proxy_only_green_allowed": false,
    "customer_quality_order_margin_bridge_required_for_green": true,
    "osat_beta_stage2_cap": "guarded_only_until_url_repair",
    "high_mae_watch_threshold_90d_pct": -20.0,
    "high_mae_watch_threshold_180d_pct": -40.0,
    "post_adjustment_weak_mfe_blocks_stage2": true,
    "positive_weight_blocked_until_url_repair": true
  },
  "confidence": "medium_low_until_url_repair",
  "apply_now": false,
  "reason": "One clean test-handler positive and two OSAT/test-equipment high-MAE counterexamples show that C08 should reward persistent low-MAE customer-quality paths but require stricter bridge evidence for beta rallies and post-adjustment relief attempts."
}
```

---

## 12. Residual contribution summary

```json
{
  "row_type": "residual_contribution",
  "research_id": "R2L73_C08_HBM_TEST_OSAT_QUALITY",
  "large_sector_id": "L2_AI_SEMICONDUCTOR_ELECTRONICS",
  "canonical_archetype_id": "C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY",
  "contribution": "Adds three non-top-covered C08 semi test/OSAT cases and separates a clean HBM test-handler customer-quality winner from OSAT/test-equipment beta rallies that later suffer severe MAE. C08 Green should require URL-repaired customer-quality, order, utilization, and margin bridge evidence.",
  "positive_case_added": 1,
  "counterexample_case_added": 2,
  "new_symbol_count": 3,
  "data_quality_blocker": "All three non-price test/customer-quality triggers require URL-level repair before positive weight promotion.",
  "guardrail_added": "C08 source_proxy_only OSAT/test-equipment beta rallies with 90D MAE <= -20% or 180D MAE <= -40% should route to Stage2-Guarded or 4B/high-MAE watch; post-adjustment weak-MFE entries should block Stage2."
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
    089030: false
    067310: false
    092870: false
  evidence_url_pending:
    089030: true
    067310: true
    092870: true
  source_proxy_only:
    089030: true
    067310: true
    092870: true
  special_handling:
    092870:
      corporate_action_candidate_date: "2024-07-31"
      selected_entry_date: "2024-08-01"
      reason: "Entry is deliberately after the candidate window; pre-2024-07-31 triggers are not used."
```

Limitations:

```text
- Price path is validated against Stock-Web tradable OHLC rows.
- Non-price evidence is not URL-repaired in this run.
- Therefore this artifact is useful for C08 residual shape and high-MAE guardrail design, but should not promote positive weights until filings/IR/customer/report data verifies customer qualification, repeat orders, test equipment backlog, OSAT utilization, and margin conversion.
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
2. Preserve R2 / loop 73 metadata.
3. Add the cases to C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY only if parser validation passes.
4. Treat all three non-price triggers as evidence_url_pending=true and source_proxy_only=true until URL-level evidence is repaired.
5. Preserve 092870's special handling: use only the post-2024-07-31 entry window for this artifact.
6. Do not use these rows for positive weight promotion until filings/IR/customer/report data verifies customer qualification, repeat orders, test-equipment backlog, OSAT utilization, and margin conversion.
7. Add a shadow-only rule candidate named C08_hbm_test_osat_customer_quality_and_high_mae_router.
8. Do not loosen Stage3-Green.
9. Add C08-specific guards:
   - source_proxy_only -> no Green
   - OSAT/test-equipment beta -> Stage2-Guarded at most until URL repair
   - 90D MAE <= -20% or 180D MAE <= -40% without repaired customer bridge -> local 4B/high-MAE watch
   - post-adjustment weak-MFE entry -> block Stage2
   - Green requires repaired customer-quality/order/utilization/margin bridge
10. Keep production scoring unchanged unless later batch promotion logic independently marks this axis safe.
```

---

## 15. Next round state

```text
completed_round = R2
completed_loop = 73
next_round = R3
next_loop = 73
next_large_sector_hint = L3_BATTERY_EV_GREEN_MOBILITY
```
