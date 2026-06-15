# E2R Stock-Web v12 Residual Research — R2 / L2_AI_SEMICONDUCTOR_ELECTRONICS / C06_HBM_MEMORY_CUSTOMER_CAPACITY

```yaml
output_file: e2r_stock_web_v12_residual_round_R2_loop_122_L2_AI_SEMICONDUCTOR_ELECTRONICS_C06_HBM_MEMORY_CUSTOMER_CAPACITY_research.md
selected_round: R2
selected_loop: 122
selection_basis: docs/core/V12_Research_No_Repeat_Index.md
selected_priority_bucket: Priority 0 / under 30 representative rows
round_schedule_status: coverage_index_selected
round_sector_consistency: pass
large_sector_id: L2_AI_SEMICONDUCTOR_ELECTRONICS
canonical_archetype_id: C06_HBM_MEMORY_CUSTOMER_CAPACITY
fine_archetype_id: HBM_CUSTOMER_CAPACITY_LOCK_VOLUME_QUALIFICATION_REOPEN_DECAY
mode: historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12
loop_objective:
  - coverage_gap_fill
  - sector_specific_rule_discovery
  - canonical_archetype_compression
  - counterexample_mining
  - 4B_non_price_requirement_stress_test
  - 4C_thesis_break_timing_test
price_source: Songdaiki/stock-web
price_basis: tradable_raw
price_adjustment_status: raw_unadjusted_marcap
stock_web_manifest_min_date: 1995-05-02
stock_web_manifest_max_date: 2026-02-20
production_scoring_changed: false
shadow_weight_only: true
investment_recommendation: false
```

## 0. Execution scope

This standalone MD follows `E2R Historical Calibration Prompt v12` for post-calibrated historical residual research. It does not scan live candidates, does not patch `stock_agent`, does not alter production scoring, and does not create a watchlist. The only output is this historical calibration artifact.

The selected canonical is `C06_HBM_MEMORY_CUSTOMER_CAPACITY` because the no-repeat index lists it as Priority 0 with 17 representative rows and a `need_to_30` of 13. The immediately preceding completed sessions covered C02, C09, C14, and C10, so this run advances to the next Priority 0 shortage bucket instead of re-materializing those files.

## 1. Price-source validation

```jsonl
{"row_type":"price_source_validation","source":"Songdaiki/stock-web","source_url":"https://github.com/Songdaiki/stock-web","manifest_path":"atlas/manifest.json","schema_path":"atlas/schema.json","universe_path":"atlas/universe/all_symbols.csv","source_name":"FinanceData/marcap","source_repo_url":"https://github.com/FinanceData/marcap","manifest_min_date":"1995-05-02","manifest_max_date":"2026-02-20","tradable_row_count":14354401,"raw_row_count":15214118,"symbol_count":5414,"calibration_shard_root":"atlas/ohlcv_tradable_by_symbol_year","raw_shard_root":"atlas/ohlcv_raw_by_symbol_year","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","validation_status":"usable_for_historical_calibration"}
```

All trigger rows use stock-web tradable shards, raw/unadjusted OHLC, and complete 30/90/180-trading-day forward windows before the manifest max date `2026-02-20`. Share-count sanity for each 180D window stayed below the 1.2 corporate-action contamination threshold.

## 2. Round / canonical / fine-deep compression

- Derived round: `R2`
- Derived large sector: `L2_AI_SEMICONDUCTOR_ELECTRONICS`
- Canonical target: `C06_HBM_MEMORY_CUSTOMER_CAPACITY`
- Fine/deep axis: `HBM_CUSTOMER_CAPACITY_LOCK_VOLUME_QUALIFICATION_REOPEN_DECAY`

Mechanism compression:

```text
HBM customer demand / AI accelerator socket
  -> customer qualification or booked supply / capacity lock
  -> HBM revenue share, mix, ASP, or shipment visibility
  -> EPS/FCF revision and durable rerating
```

The positive C06 row is not “memory stocks went up.” It is closer to a factory booking ledger: who has qualified volume, what capacity is already spoken for, and whether HBM is large enough in DRAM revenue to move earnings. Samsung's 2024 cases show the inverse: capacity plan or partial approval without key-customer volume bridge can become a false positive or hard 4C.

## 3. No-repeat and novelty check

Strict duplicate key:

```text
canonical_archetype_id + symbol + trigger_type + entry_date
```

Selected symbols:

```text
000660 SK하이닉스
005930 삼성전자
```

The `C06` index top-covered list did not show these two as the leading repeated C06 symbols in the snapshot. This run therefore intentionally uses the actual memory producers as a concentrated control set rather than another equipment-supplier proxy set.

```text
new_independent_case_count = 9
new_symbol_count = 2
same_archetype_new_trigger_family_count = 9
positive_case_count = 5
counterexample_count = 4
stage4b_case_count = 1
stage4c_case_count = 1
hard_duplicate_count = 0
minimum_new_independent_case_ratio = 1.00
minimum_new_symbol_count_pass = true
minimum_positive_counterexample_pass = true
```

## 4. Case summary and price path grid

| Symbol | Company | Trigger type | Trigger date | Entry | MFE30 | MFE90 | MFE180 | MAE30 | MAE90 | MAE180 | Role | Current profile verdict |
|---|---|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| 000660 | SK하이닉스 | Stage2-Actionable | 2023-10-26 | 2023-10-27 @ 119,100 | 13.01 | 46.85 | 108.65 | -2.35 | -2.35 | -2.35 | positive | current_profile_too_late_if_waits_for_green |
| 000660 | SK하이닉스 | Stage3-Yellow | 2024-01-25 | 2024-01-26 @ 136,000 | 28.60 | 58.09 | 82.72 | -3.16 | -3.16 | -3.16 | positive | current_profile_correct_but_green_buffer_should_not_delay_yellow |
| 000660 | SK하이닉스 | Stage3-Green | 2024-04-25 | 2024-04-25 @ 170,600 | 26.03 | 45.66 | 45.66 | -0.94 | -11.14 | -15.18 | positive | current_profile_correct_with_later_4b_overlay_needed |
| 000660 | SK하이닉스 | Stage4B | 2024-07-11 | 2024-07-12 @ 233,000 | 1.29 | 1.29 | 1.29 | -34.94 | -37.90 | -37.90 | counterexample | current_profile_4b_too_late_if_waits_for_thesis_break |
| 000660 | SK하이닉스 | Stage2-Actionable | 2025-01-23 | 2025-01-31 @ 199,200 | 10.19 | 23.74 | 169.58 | -8.99 | -18.32 | -18.32 | positive | current_profile_too_late_if_capex_disappointment_blocks_reopen |
| 005930 | 삼성전자 | Stage4C | 2024-05-24 | 2024-05-24 @ 75,900 | 14.76 | 17.00 | 17.00 | -3.16 | -21.61 | -34.26 | counterexample | current_profile_should_route_to_4c_not_stage2 |
| 005930 | 삼성전자 | Stage2 | 2024-07-24 | 2024-07-24 @ 82,000 | 5.00 | 5.00 | 5.00 | -14.88 | -39.15 | -39.15 | counterexample | current_profile_false_positive_if_approval_headline_treated_as_green |
| 005930 | 삼성전자 | Stage2 | 2024-08-07 | 2024-08-07 @ 74,700 | 7.36 | 7.36 | 7.36 | -16.73 | -33.20 | -33.20 | counterexample | current_profile_false_positive_if_partial_pass_counts_as_capacity_lock |
| 005930 | 삼성전자 | Stage2-Actionable | 2025-01-31 | 2025-01-31 @ 52,400 | 12.79 | 18.32 | 94.66 | -3.05 | -3.05 | -3.05 | positive | current_profile_too_harsh_if_permanent_4c_blocks_reopen |

## 5. Case-level interpretation

### 5.1 SK하이닉스 positive controls

**000660 / 2023-10-27 / Stage2-Actionable.**  
This is the early C06 unlock. The company was still loss-making, but HBM3 and high-capacity DRAM were already improving the sales and operating-loss trajectory. The price path rewarded the early bridge: 90D MFE was `46.85%` and 180D MFE was `108.65%`, with 180D MAE only `-2.35%`. A Green-only model would be late here.

**000660 / 2024-01-26 / Stage3-Yellow.**  
The profit swing and AI-server memory demand turned the row from “premium-memory mix” into visible HBM capacity rerating. 30D MFE was already `28.60%`; 90D MFE reached `58.09%`. This is a clean Yellow row, but not a reason to loosen all Green thresholds globally.

**000660 / 2024-04-25 / Stage3-Green.**  
This is the cleanest customer-capacity lock row: Nvidia-supplier status, HBM3E shipment, and HBM-focused capex. The 30D/90D MFE path was strong, but 90D/180D MAE widened after the July peak. It strengthens the rule that C06 Green can coexist with later local 4B overlay.

**000660 / 2024-07-12 / Stage4B.**  
This row protects the model from confusing a great C06 company with a good new entry. The HBM thesis was not broken, but the stock was sitting on a crowded post-rerating shelf. 90D MFE was only `1.29%`, while 90D MAE was `-37.90%`. Correct handling is local Stage4B watch, not hard 4C.

**000660 / 2025-01-31 / Stage2-Actionable.**  
This is a reopen case after the 2024 drawdown. HBM had become material in DRAM revenue, 2025 sales visibility existed, and 2026 shipment discussions were visible, but the capex plan disappointed some investors. The path says C06 should reopen Stage2-Actionable rather than permanently block after a prior post-peak drawdown: 180D MFE was `169.58%`.

### 5.2 Samsung counterexamples and reset case

**005930 / 2024-05-24 / Stage4C.**  
The reported Nvidia HBM test failure is the opposite of a C06 unlock. If key-customer qualification is missing, capacity plan is not enough. The 180D path had only `17.00%` MFE and `-34.26%` MAE, validating hard thesis-break treatment.

**005930 / 2024-07-24 / Stage2.**  
A muted HBM3 approval for the China-market H20 route was not the same as HBM3E flagship volume. The model should not treat this as Yellow or Green. 90D/180D MAE reached `-39.15%`.

**005930 / 2024-08-07 / Stage2.**  
The 8-layer HBM3E approval headline still lacked a signed supply deal and left 12-layer HBM3E pending. This row blocks the shortcut “test passed = capacity lock.” 180D MFE was only `7.36%`, while 180D MAE was `-33.20%`.

**005930 / 2025-01-31 / Stage2-Actionable.**  
This is the decay/reopen edge case. The 2024 failure should not become a permanent 4C scar. After a large price reset, redesigned HBM3E timing and memory recovery created an asymmetric Stage2-watch row. It is not clean Green, but the 180D MFE of `94.66%` says a reset-plus-redesign path deserves re-evaluation.

## 6. Evidence source map

| source_id | publisher/date | as-of use | url |
|---|---|---|---|
| EV_C06_20231026_YNA_SKH_Q3_HBM3 | Yonhap News Agency / 2023-10-26 | SK hynix Q3 2023: HBM3 and high-capacity mobile DRAM sales improved revenue and operating loss; focus on HBM/DDR5 high-performance products. | https://en.yna.co.kr/view/AEN20231026001353320 |
| EV_C06_20240125_REUTERS_SKH_Q4 | Reuters / 2024-01-24/25 | SK hynix swing to profit, strong AI-chip demand, HBM3E roadmap, AI products supply tight. | https://www.reuters.com/technology/sk-hynix-swings-q4-profit-strong-ai-chip-demand-2024-01-24/ |
| EV_C06_20240125_YNA_SKH_Q4 | Yonhap News Agency / 2024-01-25 | SK hynix Q4 2023 operating profit on demand for premium memory and AI-server/mobile applications. | https://en.yna.co.kr/view/AEN20240125001552320 |
| EV_C06_20240425_REUTERS_SKH_Q1 | Reuters / 2024-04-25 | SK hynix Q1 2024 profit beat, full memory recovery on AI demand, Nvidia HBM supplier status, HBM3E mass production and HBM-focused capex. | https://www.reuters.com/technology/sk-hynix-q1-profit-beats-expectations-ai-boom-2024-04-24/ |
| EV_C06_20240725_REUTERS_SKH_Q2 | Reuters / 2024-07-24/25 | SK hynix six-year-high Q2 profit and HBM shipment growth, but shares sold off as expectations were elevated; used as non-price context for local 4B overlay. | https://www.reuters.com/technology/nvidia-supplier-sk-hynixs-q2-profit-soars-ai-boom-2024-07-24/ |
| EV_C06_20250123_REUTERS_SKH_Q4_2024 | Reuters / 2025-01-23 | SK hynix Q4 2024: high-end semiconductor sales expected to more than double, HBM 40% of DRAM revenue, supply talks for 2026; capex plan underwhelmed. | https://www.reuters.com/technology/nvidia-supplier-sk-hynix-posts-record-quarterly-profit-2025-01-22/ |
| EV_C06_20240524_REUTERS_SAMSUNG_HBM_TEST_FAIL | Reuters / 2024-05-24 | Samsung HBM3/HBM3E had not passed Nvidia tests due to reported heat/power issues; Samsung said testing proceeded as planned. | https://www.reuters.com/technology/samsungs-hbm-chips-failing-nvidia-tests-due-heat-power-consumption-woes-sources-2024-05-23/ |
| EV_C06_20240724_REUTERS_SAMSUNG_HBM3_H20 | Reuters / 2024-07-24 | Samsung HBM3 cleared for Nvidia China-market H20 only; HBM3E still had not met Nvidia standards. | https://www.reuters.com/technology/nvidia-clears-samsungs-hbm3-chips-use-china-market-processor-sources-say-2024-07-23/ |
| EV_C06_20240807_REUTERS_SAMSUNG_8L_HBM3E | Reuters / 2024-08-07 | Samsung 8-layer HBM3E passed tests according to sources, but no supply deal yet and 12-layer product still pending; Samsung said optimization continued. | https://www.reuters.com/technology/artificial-intelligence/samsungs-8-layer-hbm3e-chips-clear-nvidias-tests-use-sources-say-2024-08-06/ |
| EV_C06_20250131_REUTERS_SAMSUNG_Q4_2024 | Reuters / 2025-01-31 | Samsung warned Q1 AI chip sales would be sluggish due to China restrictions and product transition, but planned improved HBM3E launch and memory recovery from Q2. | https://www.reuters.com/technology/samsung-q4-profit-growth-slows-chip-issues-weigh-2025-01-31/ |

## 7. Machine-readable trigger rows

```jsonl
{"row_type":"trigger","case_id":"C06_000660_20231027_Q3_HBM3_DRAM_PROFIT_TURN","symbol":"000660","company":"SK하이닉스","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C06_HBM_MEMORY_CUSTOMER_CAPACITY","fine_archetype_id":"HBM3_SALES_MIX_EARLY_PROFITABILITY_BRIDGE","trigger_type":"Stage2-Actionable","trigger_date":"2023-10-26","entry_date":"2023-10-27","entry_price":119100.0,"price_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","stock_web_tradable_shard_path":"atlas/ohlcv_tradable_by_symbol_year/000/000660/2023.csv","stock_web_profile_path":"atlas/symbol_profiles/000/000660.json","MFE_30D_pct":13.01,"MFE_90D_pct":46.85,"MFE_180D_pct":108.65,"MAE_30D_pct":-2.35,"MAE_90D_pct":-2.35,"MAE_180D_pct":-2.35,"peak_30D_date":"2023-12-04","peak_90D_date":"2024-03-08","peak_180D_date":"2024-07-11","trough_30D_date":"2023-10-31","trough_90D_date":"2023-10-31","trough_180D_date":"2023-10-31","role":"positive","outcome_label":"positive_early_hbm_mix_before_full_earnings_recovery","current_profile_verdict":"current_profile_too_late_if_waits_for_green","score_return_alignment":"aligned","calibration_usable":true,"validation_status":"usable_clean_180D_window","hard_duplicate_key":"C06_HBM_MEMORY_CUSTOMER_CAPACITY|000660|Stage2-Actionable|2023-10-27","evidence_source_ids":["EV_C06_20231026_YNA_SKH_Q3_HBM3"],"raw_component_score_breakdown":{"EPS_FCF":16,"EarningsVisibility":18,"BottleneckPricing":18,"MarketMispricing":13,"ValuationRerating":10,"CapitalAllocation":3,"InformationConfidence":5},"raw_total_score":83,"dedupe_role":"representative_candidate","residual_contribution":"C06 distinguishes true customer-capacity lock from partial/failed HBM qualification and adds local 4B overlay for post-peak HBM leader entries."}
{"row_type":"trigger","case_id":"C06_000660_20240126_Q4_SWING_PROFIT_AI_SERVER","symbol":"000660","company":"SK하이닉스","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C06_HBM_MEMORY_CUSTOMER_CAPACITY","fine_archetype_id":"HBM_CAPACITY_REDEPLOYMENT_PROFIT_SWING","trigger_type":"Stage3-Yellow","trigger_date":"2024-01-25","entry_date":"2024-01-26","entry_price":136000.0,"price_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","stock_web_tradable_shard_path":"atlas/ohlcv_tradable_by_symbol_year/000/000660/2024.csv","stock_web_profile_path":"atlas/symbol_profiles/000/000660.json","MFE_30D_pct":28.6,"MFE_90D_pct":58.09,"MFE_180D_pct":82.72,"MAE_30D_pct":-3.16,"MAE_90D_pct":-3.16,"MAE_180D_pct":-3.16,"peak_30D_date":"2024-03-08","peak_90D_date":"2024-06-11","peak_180D_date":"2024-07-11","trough_30D_date":"2024-02-01","trough_90D_date":"2024-02-01","trough_180D_date":"2024-02-01","role":"positive","outcome_label":"positive_profit_swing_capacity_redeployment","current_profile_verdict":"current_profile_correct_but_green_buffer_should_not_delay_yellow","score_return_alignment":"aligned","calibration_usable":true,"validation_status":"usable_clean_180D_window","hard_duplicate_key":"C06_HBM_MEMORY_CUSTOMER_CAPACITY|000660|Stage3-Yellow|2024-01-26","evidence_source_ids":["EV_C06_20240125_REUTERS_SKH_Q4","EV_C06_20240125_YNA_SKH_Q4"],"raw_component_score_breakdown":{"EPS_FCF":20,"EarningsVisibility":20,"BottleneckPricing":19,"MarketMispricing":14,"ValuationRerating":11,"CapitalAllocation":4,"InformationConfidence":5},"raw_total_score":93,"dedupe_role":"representative_candidate","residual_contribution":"C06 distinguishes true customer-capacity lock from partial/failed HBM qualification and adds local 4B overlay for post-peak HBM leader entries."}
{"row_type":"trigger","case_id":"C06_000660_20240425_Q1_HBM_CAPEX_NVIDIA_SUPPLY","symbol":"000660","company":"SK하이닉스","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C06_HBM_MEMORY_CUSTOMER_CAPACITY","fine_archetype_id":"HBM3E_NVIDIA_SUPPLIER_CAPEX_CAPACITY_LOCK","trigger_type":"Stage3-Green","trigger_date":"2024-04-25","entry_date":"2024-04-25","entry_price":170600.0,"price_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","stock_web_tradable_shard_path":"atlas/ohlcv_tradable_by_symbol_year/000/000660/2024.csv","stock_web_profile_path":"atlas/symbol_profiles/000/000660.json","MFE_30D_pct":26.03,"MFE_90D_pct":45.66,"MFE_180D_pct":45.66,"MAE_30D_pct":-0.94,"MAE_90D_pct":-11.14,"MAE_180D_pct":-15.18,"peak_30D_date":"2024-06-11","peak_90D_date":"2024-07-11","peak_180D_date":"2024-07-11","trough_30D_date":"2024-05-02","trough_90D_date":"2024-08-05","trough_180D_date":"2024-09-19","role":"positive","outcome_label":"positive_customer_capacity_lock_high_mfe","current_profile_verdict":"current_profile_correct_with_later_4b_overlay_needed","score_return_alignment":"aligned","calibration_usable":true,"validation_status":"usable_clean_180D_window","hard_duplicate_key":"C06_HBM_MEMORY_CUSTOMER_CAPACITY|000660|Stage3-Green|2024-04-25","evidence_source_ids":["EV_C06_20240425_REUTERS_SKH_Q1"],"raw_component_score_breakdown":{"EPS_FCF":23,"EarningsVisibility":21,"BottleneckPricing":19,"MarketMispricing":14,"ValuationRerating":11,"CapitalAllocation":4,"InformationConfidence":5},"raw_total_score":97,"dedupe_role":"representative_candidate","residual_contribution":"C06 distinguishes true customer-capacity lock from partial/failed HBM qualification and adds local 4B overlay for post-peak HBM leader entries."}
{"row_type":"trigger","case_id":"C06_000660_20240712_POST_PEAK_HBM_LEADER_LOCAL_4B","symbol":"000660","company":"SK하이닉스","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C06_HBM_MEMORY_CUSTOMER_CAPACITY","fine_archetype_id":"HBM_LEADER_POST_PEAK_LOCAL_4B_NOT_FULL_4C","trigger_type":"Stage4B","trigger_date":"2024-07-11","entry_date":"2024-07-12","entry_price":233000.0,"price_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","stock_web_tradable_shard_path":"atlas/ohlcv_tradable_by_symbol_year/000/000660/2024.csv","stock_web_profile_path":"atlas/symbol_profiles/000/000660.json","MFE_30D_pct":1.29,"MFE_90D_pct":1.29,"MFE_180D_pct":1.29,"MAE_30D_pct":-34.94,"MAE_90D_pct":-37.9,"MAE_180D_pct":-37.9,"peak_30D_date":"2024-07-12","peak_90D_date":"2024-07-12","peak_180D_date":"2024-07-12","trough_30D_date":"2024-08-05","trough_90D_date":"2024-09-19","trough_180D_date":"2024-09-19","role":"counterexample","outcome_label":"counterexample_great_company_bad_entry_local_4b","current_profile_verdict":"current_profile_4b_too_late_if_waits_for_thesis_break","score_return_alignment":"guardrail_aligned","calibration_usable":true,"validation_status":"usable_clean_180D_window","hard_duplicate_key":"C06_HBM_MEMORY_CUSTOMER_CAPACITY|000660|Stage4B|2024-07-12","evidence_source_ids":["EV_C06_20240725_REUTERS_SKH_Q2"],"raw_component_score_breakdown":{"EPS_FCF":22,"EarningsVisibility":20,"BottleneckPricing":19,"MarketMispricing":8,"ValuationRerating":5,"CapitalAllocation":4,"InformationConfidence":5},"raw_total_score":83,"dedupe_role":"representative_candidate","residual_contribution":"C06 distinguishes true customer-capacity lock from partial/failed HBM qualification and adds local 4B overlay for post-peak HBM leader entries."}
{"row_type":"trigger","case_id":"C06_000660_20250131_HBM_40PCT_DRAM_REVENUE_2025_ORDERS","symbol":"000660","company":"SK하이닉스","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C06_HBM_MEMORY_CUSTOMER_CAPACITY","fine_archetype_id":"HBM_REVENUE_SHARE_SUPPLY_VISIBILITY_AFTER_RESET","trigger_type":"Stage2-Actionable","trigger_date":"2025-01-23","entry_date":"2025-01-31","entry_price":199200.0,"price_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","stock_web_tradable_shard_path":"atlas/ohlcv_tradable_by_symbol_year/000/000660/2025.csv","stock_web_profile_path":"atlas/symbol_profiles/000/000660.json","MFE_30D_pct":10.19,"MFE_90D_pct":23.74,"MFE_180D_pct":169.58,"MAE_30D_pct":-8.99,"MAE_90D_pct":-18.32,"MAE_180D_pct":-18.32,"peak_30D_date":"2025-02-19","peak_90D_date":"2025-06-12","peak_180D_date":"2025-10-27","trough_30D_date":"2025-03-11","trough_90D_date":"2025-04-09","trough_180D_date":"2025-04-09","role":"positive","outcome_label":"positive_reset_after_capex_worry_but_hbm_visibility_persists","current_profile_verdict":"current_profile_too_late_if_capex_disappointment_blocks_reopen","score_return_alignment":"aligned","calibration_usable":true,"validation_status":"usable_clean_180D_window","hard_duplicate_key":"C06_HBM_MEMORY_CUSTOMER_CAPACITY|000660|Stage2-Actionable|2025-01-31","evidence_source_ids":["EV_C06_20250123_REUTERS_SKH_Q4_2024"],"raw_component_score_breakdown":{"EPS_FCF":23,"EarningsVisibility":20,"BottleneckPricing":19,"MarketMispricing":13,"ValuationRerating":10,"CapitalAllocation":3,"InformationConfidence":5},"raw_total_score":93,"dedupe_role":"representative_candidate","residual_contribution":"C06 distinguishes true customer-capacity lock from partial/failed HBM qualification and adds local 4B overlay for post-peak HBM leader entries."}
{"row_type":"trigger","case_id":"C06_005930_20240524_HBM3E_NVIDIA_TEST_FAILURE","symbol":"005930","company":"삼성전자","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C06_HBM_MEMORY_CUSTOMER_CAPACITY","fine_archetype_id":"CUSTOMER_QUALIFICATION_FAILURE_THESIS_BREAK","trigger_type":"Stage4C","trigger_date":"2024-05-24","entry_date":"2024-05-24","entry_price":75900.0,"price_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","stock_web_tradable_shard_path":"atlas/ohlcv_tradable_by_symbol_year/005/005930/2024.csv","stock_web_profile_path":"atlas/symbol_profiles/005/005930.json","MFE_30D_pct":14.76,"MFE_90D_pct":17.0,"MFE_180D_pct":17.0,"MAE_30D_pct":-3.16,"MAE_90D_pct":-21.61,"MAE_180D_pct":-34.26,"peak_30D_date":"2024-07-05","peak_90D_date":"2024-07-11","peak_180D_date":"2024-07-11","trough_30D_date":"2024-05-30","trough_90D_date":"2024-10-07","trough_180D_date":"2024-11-14","role":"counterexample","outcome_label":"counterexample_customer_qualification_failure_blocks_c06","current_profile_verdict":"current_profile_should_route_to_4c_not_stage2","score_return_alignment":"guardrail_aligned","calibration_usable":true,"validation_status":"usable_clean_180D_window","hard_duplicate_key":"C06_HBM_MEMORY_CUSTOMER_CAPACITY|005930|Stage4C|2024-05-24","evidence_source_ids":["EV_C06_20240524_REUTERS_SAMSUNG_HBM_TEST_FAIL"],"raw_component_score_breakdown":{"EPS_FCF":8,"EarningsVisibility":7,"BottleneckPricing":5,"MarketMispricing":10,"ValuationRerating":7,"CapitalAllocation":4,"InformationConfidence":8},"raw_total_score":49,"dedupe_role":"representative_candidate","residual_contribution":"C06 distinguishes true customer-capacity lock from partial/failed HBM qualification and adds local 4B overlay for post-peak HBM leader entries."}
{"row_type":"trigger","case_id":"C06_005930_20240724_MUTED_HBM3_H20_APPROVAL","symbol":"005930","company":"삼성전자","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C06_HBM_MEMORY_CUSTOMER_CAPACITY","fine_archetype_id":"MUTED_CUSTOMER_APPROVAL_NOT_FULL_HBM3E_RERATING","trigger_type":"Stage2","trigger_date":"2024-07-24","entry_date":"2024-07-24","entry_price":82000.0,"price_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","stock_web_tradable_shard_path":"atlas/ohlcv_tradable_by_symbol_year/005/005930/2024.csv","stock_web_profile_path":"atlas/symbol_profiles/005/005930.json","MFE_30D_pct":5.0,"MFE_90D_pct":5.0,"MFE_180D_pct":5.0,"MAE_30D_pct":-14.88,"MAE_90D_pct":-39.15,"MAE_180D_pct":-39.15,"peak_30D_date":"2024-08-01","peak_90D_date":"2024-08-01","peak_180D_date":"2024-08-01","trough_30D_date":"2024-09-04","trough_90D_date":"2024-11-14","trough_180D_date":"2024-11-14","role":"counterexample","outcome_label":"counterexample_muted_approval_not_enough_for_yellow","current_profile_verdict":"current_profile_false_positive_if_approval_headline_treated_as_green","score_return_alignment":"misaligned_false_positive","calibration_usable":true,"validation_status":"usable_clean_180D_window","hard_duplicate_key":"C06_HBM_MEMORY_CUSTOMER_CAPACITY|005930|Stage2|2024-07-24","evidence_source_ids":["EV_C06_20240724_REUTERS_SAMSUNG_HBM3_H20"],"raw_component_score_breakdown":{"EPS_FCF":12,"EarningsVisibility":10,"BottleneckPricing":8,"MarketMispricing":11,"ValuationRerating":8,"CapitalAllocation":4,"InformationConfidence":7},"raw_total_score":60,"dedupe_role":"representative_candidate","residual_contribution":"C06 distinguishes true customer-capacity lock from partial/failed HBM qualification and adds local 4B overlay for post-peak HBM leader entries."}
{"row_type":"trigger","case_id":"C06_005930_20240807_PARTIAL_8L_HBM3E_APPROVAL_NO_SUPPLY_DEAL","symbol":"005930","company":"삼성전자","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C06_HBM_MEMORY_CUSTOMER_CAPACITY","fine_archetype_id":"PARTIAL_CUSTOMER_APPROVAL_WITHOUT_VOLUME_BRIDGE","trigger_type":"Stage2","trigger_date":"2024-08-07","entry_date":"2024-08-07","entry_price":74700.0,"price_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","stock_web_tradable_shard_path":"atlas/ohlcv_tradable_by_symbol_year/005/005930/2024.csv","stock_web_profile_path":"atlas/symbol_profiles/005/005930.json","MFE_30D_pct":7.36,"MFE_90D_pct":7.36,"MFE_180D_pct":7.36,"MAE_30D_pct":-16.73,"MAE_90D_pct":-33.2,"MAE_180D_pct":-33.2,"peak_30D_date":"2024-08-16","peak_90D_date":"2024-08-16","peak_180D_date":"2024-08-16","trough_30D_date":"2024-09-19","trough_90D_date":"2024-11-14","trough_180D_date":"2024-11-14","role":"counterexample","outcome_label":"counterexample_partial_approval_without_volume_contract","current_profile_verdict":"current_profile_false_positive_if_partial_pass_counts_as_capacity_lock","score_return_alignment":"misaligned_false_positive","calibration_usable":true,"validation_status":"usable_clean_180D_window","hard_duplicate_key":"C06_HBM_MEMORY_CUSTOMER_CAPACITY|005930|Stage2|2024-08-07","evidence_source_ids":["EV_C06_20240807_REUTERS_SAMSUNG_8L_HBM3E"],"raw_component_score_breakdown":{"EPS_FCF":13,"EarningsVisibility":11,"BottleneckPricing":10,"MarketMispricing":11,"ValuationRerating":8,"CapitalAllocation":4,"InformationConfidence":8},"raw_total_score":65,"dedupe_role":"representative_candidate","residual_contribution":"C06 distinguishes true customer-capacity lock from partial/failed HBM qualification and adds local 4B overlay for post-peak HBM leader entries."}
{"row_type":"trigger","case_id":"C06_005930_20250131_RESET_HBM_REDESIGN_MEMORY_RECOVERY","symbol":"005930","company":"삼성전자","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C06_HBM_MEMORY_CUSTOMER_CAPACITY","fine_archetype_id":"SAMSUNG_HBM_RESET_REOPEN_NOT_PERMANENT_4C","trigger_type":"Stage2-Actionable","trigger_date":"2025-01-31","entry_date":"2025-01-31","entry_price":52400.0,"price_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","stock_web_tradable_shard_path":"atlas/ohlcv_tradable_by_symbol_year/005/005930/2025.csv","stock_web_profile_path":"atlas/symbol_profiles/005/005930.json","MFE_30D_pct":12.79,"MFE_90D_pct":18.32,"MFE_180D_pct":94.66,"MAE_30D_pct":-3.05,"MAE_90D_pct":-3.05,"MAE_180D_pct":-3.05,"peak_30D_date":"2025-02-20","peak_90D_date":"2025-03-27","peak_180D_date":"2025-10-27","trough_30D_date":"2025-02-03","trough_90D_date":"2025-02-03","trough_180D_date":"2025-02-03","role":"positive","outcome_label":"positive_reset_watch_after_hard_2024_failure","current_profile_verdict":"current_profile_too_harsh_if_permanent_4c_blocks_reopen","score_return_alignment":"misaligned_false_positive","calibration_usable":true,"validation_status":"usable_clean_180D_window","hard_duplicate_key":"C06_HBM_MEMORY_CUSTOMER_CAPACITY|005930|Stage2-Actionable|2025-01-31","evidence_source_ids":["EV_C06_20250131_REUTERS_SAMSUNG_Q4_2024"],"raw_component_score_breakdown":{"EPS_FCF":15,"EarningsVisibility":14,"BottleneckPricing":12,"MarketMispricing":16,"ValuationRerating":13,"CapitalAllocation":5,"InformationConfidence":6},"raw_total_score":81,"dedupe_role":"representative_candidate","residual_contribution":"C06 distinguishes true customer-capacity lock from partial/failed HBM qualification and adds local 4B overlay for post-peak HBM leader entries."}
```

## 8. Machine-readable score simulation rows

```jsonl
{"row_type":"score_simulation","case_id":"C06_000660_20231027_Q3_HBM3_DRAM_PROFIT_TURN","symbol":"000660","before_profile_id":"e2r_2_1_stock_web_calibrated_proxy","after_profile_id":"e2r_C06_hbm_customer_capacity_shadow_profile","raw_component_score_breakdown":{"EPS_FCF":16,"EarningsVisibility":18,"BottleneckPricing":18,"MarketMispricing":13,"ValuationRerating":10,"CapitalAllocation":3,"InformationConfidence":5},"raw_total_score":83,"trigger_type":"Stage2-Actionable","MFE_90D_pct":46.85,"MAE_90D_pct":-2.35,"score_return_alignment":"aligned","profile_residual":"current_profile_too_late_if_waits_for_green"}
{"row_type":"score_simulation","case_id":"C06_000660_20240126_Q4_SWING_PROFIT_AI_SERVER","symbol":"000660","before_profile_id":"e2r_2_1_stock_web_calibrated_proxy","after_profile_id":"e2r_C06_hbm_customer_capacity_shadow_profile","raw_component_score_breakdown":{"EPS_FCF":20,"EarningsVisibility":20,"BottleneckPricing":19,"MarketMispricing":14,"ValuationRerating":11,"CapitalAllocation":4,"InformationConfidence":5},"raw_total_score":93,"trigger_type":"Stage3-Yellow","MFE_90D_pct":58.09,"MAE_90D_pct":-3.16,"score_return_alignment":"aligned","profile_residual":"current_profile_correct_but_green_buffer_should_not_delay_yellow"}
{"row_type":"score_simulation","case_id":"C06_000660_20240425_Q1_HBM_CAPEX_NVIDIA_SUPPLY","symbol":"000660","before_profile_id":"e2r_2_1_stock_web_calibrated_proxy","after_profile_id":"e2r_C06_hbm_customer_capacity_shadow_profile","raw_component_score_breakdown":{"EPS_FCF":23,"EarningsVisibility":21,"BottleneckPricing":19,"MarketMispricing":14,"ValuationRerating":11,"CapitalAllocation":4,"InformationConfidence":5},"raw_total_score":97,"trigger_type":"Stage3-Green","MFE_90D_pct":45.66,"MAE_90D_pct":-11.14,"score_return_alignment":"aligned","profile_residual":"current_profile_correct_with_later_4b_overlay_needed"}
{"row_type":"score_simulation","case_id":"C06_000660_20240712_POST_PEAK_HBM_LEADER_LOCAL_4B","symbol":"000660","before_profile_id":"e2r_2_1_stock_web_calibrated_proxy","after_profile_id":"e2r_C06_hbm_customer_capacity_shadow_profile","raw_component_score_breakdown":{"EPS_FCF":22,"EarningsVisibility":20,"BottleneckPricing":19,"MarketMispricing":8,"ValuationRerating":5,"CapitalAllocation":4,"InformationConfidence":5},"raw_total_score":83,"trigger_type":"Stage4B","MFE_90D_pct":1.29,"MAE_90D_pct":-37.9,"score_return_alignment":"guardrail_aligned","profile_residual":"current_profile_4b_too_late_if_waits_for_thesis_break"}
{"row_type":"score_simulation","case_id":"C06_000660_20250131_HBM_40PCT_DRAM_REVENUE_2025_ORDERS","symbol":"000660","before_profile_id":"e2r_2_1_stock_web_calibrated_proxy","after_profile_id":"e2r_C06_hbm_customer_capacity_shadow_profile","raw_component_score_breakdown":{"EPS_FCF":23,"EarningsVisibility":20,"BottleneckPricing":19,"MarketMispricing":13,"ValuationRerating":10,"CapitalAllocation":3,"InformationConfidence":5},"raw_total_score":93,"trigger_type":"Stage2-Actionable","MFE_90D_pct":23.74,"MAE_90D_pct":-18.32,"score_return_alignment":"aligned","profile_residual":"current_profile_too_late_if_capex_disappointment_blocks_reopen"}
{"row_type":"score_simulation","case_id":"C06_005930_20240524_HBM3E_NVIDIA_TEST_FAILURE","symbol":"005930","before_profile_id":"e2r_2_1_stock_web_calibrated_proxy","after_profile_id":"e2r_C06_hbm_customer_capacity_shadow_profile","raw_component_score_breakdown":{"EPS_FCF":8,"EarningsVisibility":7,"BottleneckPricing":5,"MarketMispricing":10,"ValuationRerating":7,"CapitalAllocation":4,"InformationConfidence":8},"raw_total_score":49,"trigger_type":"Stage4C","MFE_90D_pct":17.0,"MAE_90D_pct":-21.61,"score_return_alignment":"guardrail_aligned","profile_residual":"current_profile_should_route_to_4c_not_stage2"}
{"row_type":"score_simulation","case_id":"C06_005930_20240724_MUTED_HBM3_H20_APPROVAL","symbol":"005930","before_profile_id":"e2r_2_1_stock_web_calibrated_proxy","after_profile_id":"e2r_C06_hbm_customer_capacity_shadow_profile","raw_component_score_breakdown":{"EPS_FCF":12,"EarningsVisibility":10,"BottleneckPricing":8,"MarketMispricing":11,"ValuationRerating":8,"CapitalAllocation":4,"InformationConfidence":7},"raw_total_score":60,"trigger_type":"Stage2","MFE_90D_pct":5.0,"MAE_90D_pct":-39.15,"score_return_alignment":"misaligned_false_positive","profile_residual":"current_profile_false_positive_if_approval_headline_treated_as_green"}
{"row_type":"score_simulation","case_id":"C06_005930_20240807_PARTIAL_8L_HBM3E_APPROVAL_NO_SUPPLY_DEAL","symbol":"005930","before_profile_id":"e2r_2_1_stock_web_calibrated_proxy","after_profile_id":"e2r_C06_hbm_customer_capacity_shadow_profile","raw_component_score_breakdown":{"EPS_FCF":13,"EarningsVisibility":11,"BottleneckPricing":10,"MarketMispricing":11,"ValuationRerating":8,"CapitalAllocation":4,"InformationConfidence":8},"raw_total_score":65,"trigger_type":"Stage2","MFE_90D_pct":7.36,"MAE_90D_pct":-33.2,"score_return_alignment":"misaligned_false_positive","profile_residual":"current_profile_false_positive_if_partial_pass_counts_as_capacity_lock"}
{"row_type":"score_simulation","case_id":"C06_005930_20250131_RESET_HBM_REDESIGN_MEMORY_RECOVERY","symbol":"005930","before_profile_id":"e2r_2_1_stock_web_calibrated_proxy","after_profile_id":"e2r_C06_hbm_customer_capacity_shadow_profile","raw_component_score_breakdown":{"EPS_FCF":15,"EarningsVisibility":14,"BottleneckPricing":12,"MarketMispricing":16,"ValuationRerating":13,"CapitalAllocation":5,"InformationConfidence":6},"raw_total_score":81,"trigger_type":"Stage2-Actionable","MFE_90D_pct":18.32,"MAE_90D_pct":-3.05,"score_return_alignment":"misaligned_false_positive","profile_residual":"current_profile_too_harsh_if_permanent_4c_blocks_reopen"}
```

## 9. Machine-readable aggregate / shadow / residual rows

```jsonl
{"row_type":"aggregate","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C06_HBM_MEMORY_CUSTOMER_CAPACITY","selected_round":"R2","selected_loop":122,"calibration_usable_trigger_count":9,"representative_trigger_count":9,"new_independent_case_count":9,"new_symbol_count":2,"same_archetype_new_trigger_family_count":9,"positive_case_count":5,"counterexample_count":4,"stage4b_case_count":1,"stage4c_case_count":1,"current_profile_error_count":6,"source_proxy_only_count":0,"evidence_url_pending_count":0,"pre_index_representative_rows":17,"need_to_30_before":13,"expected_rows_after_acceptance":26,"need_to_30_after_acceptance":4,"need_to_50_after_acceptance":24,"diversity_score_summary":{"new_independent_ratio":1.0,"hard_duplicate_count":0,"minimum_new_symbol_count_pass":true,"minimum_positive_counterexample_pass":true}}
{"row_type":"shadow_weight","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C06_HBM_MEMORY_CUSTOMER_CAPACITY","rule_candidate":"C06_CUSTOMER_CAPACITY_LOCK_REQUIRES_VOLUME_QUALIFICATION_AND_REOPEN_DECAY","direction":"scope_specific_rule_candidate","production_scoring_changed":false,"shadow_weight_only":true,"do_not_propose_new_weight_delta":false,"proposed_effect":{"positive_gate":"raise Stage2-Actionable/Yellow when HBM revenue share, customer supply status, booked capacity, or shipment plan is explicit","negative_gate":"block Yellow/Green when HBM evidence is only partial approval, lower-end customer route, or key-customer qualification failure","4b_gate":"post-peak HBM leaders require local Stage4B even when thesis remains intact","decay_gate":"hard 4C from failed qualification should decay after price reset plus redesigned product/customer path"}}
{"row_type":"residual_contribution","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C06_HBM_MEMORY_CUSTOMER_CAPACITY","new_axis":"C06_CUSTOMER_CAPACITY_LOCK_REQUIRES_VOLUME_QUALIFICATION_AND_REOPEN_DECAY","existing_axis_strengthened":["stage2_required_bridge","price_only_blowoff_blocks_positive_stage","local_4b_watch_guard","hard_4c_confirmation"],"existing_axis_weakened":["permanent_hard_4c_for_samsung_after_price_reset"],"mechanism":"HBM customer/capacity evidence behaves like a contract bridge: it must identify real customer qualification or booked capacity, not just memory beta. But once the failed-qualification shock is old and price resets, the model should reopen Stage2-watch when a redesigned product and market recovery path appears."}
```

## 10. Score / return alignment summary

```text
aligned_positive_rows = 4
guardrail_aligned_rows = 2
misaligned_false_positive_rows = 3
current_profile_error_count = 6
```

Interpretation:

```text
C06 should not be treated as broad memory beta.
C06 Stage2-Actionable / Yellow requires at least one of:
  - identified HBM customer qualification or supply route,
  - booked/sold-out HBM capacity,
  - HBM revenue share large enough to move DRAM profit,
  - explicit shipment or product-generation transition tied to major AI accelerator demand.

C06 should block or downgrade when:
  - the route is only partial approval for a lower-end customer product,
  - flagship HBM3E/12-layer product remains unqualified,
  - no supply deal or volume bridge exists,
  - price is post-peak even though the underlying HBM thesis remains intact.

C06 hard 4C should decay when:
  - the failed-qualification evidence is old,
  - price has reset deeply,
  - redesigned product/customer path is visible,
  - memory cycle recovery gives an independent EPS bridge.
```

## 11. Proposed shadow rule candidate

```text
rule_candidate = C06_CUSTOMER_CAPACITY_LOCK_REQUIRES_VOLUME_QUALIFICATION_AND_REOPEN_DECAY
production_scoring_changed = false
shadow_weight_only = true
```

Rule text:

```text
For C06_HBM_MEMORY_CUSTOMER_CAPACITY, promote to Stage2-Actionable/Stage3-Yellow only when HBM evidence identifies customer qualification, booked capacity, HBM revenue share, or shipment visibility. Treat partial approvals, lower-end customer routes, and unqualified flagship HBM products as Stage2-watch or Stage4C depending on severity. Apply local Stage4B after post-peak HBM leader extensions even when the thesis is intact. Allow a failed-qualification 4C to decay into Stage2-Actionable after price reset plus redesigned product/customer path.
```

Why this is not the global rule repeated:

```text
The global rule already says price-only blowoff should not become positive and hard 4C should route to thesis break. This loop adds a C06-specific distinction: HBM capacity is only real when customer qualification or volume bridge exists, while prior HBM failure is not permanent if the product/customer path reopens after a reset.
```

## 12. Validation scope

```text
entry_date_in_tradable_shard = true for all rows
entry_price_from_close_column = true for all rows
forward_180D_window_available_by_manifest_max_date = true for all rows
MFE_30D_pct / MFE_90D_pct / MFE_180D_pct complete = true for all rows
MAE_30D_pct / MAE_90D_pct / MAE_180D_pct complete = true for all rows
window_180D_corporate_action_contaminated = false for all rows under share-ratio >= 1.2 rule
trigger_type_canonical = true for all rows
calibration_usable = true for all rows
```

Caveat: this run is intentionally concentrated in the two actual Korean memory producers, not a broad HBM equipment/value-chain supplier sample. That is deliberate: prior C06 rows were supplier-heavy; this loop uses the producer/control pair to sharpen customer-qualification and capacity-lock logic.

## 13. Deferred Coding Agent Handoff Prompt

```text
Do not execute during this research loop.

When batching this MD into stock_agent later:
1. Place the file under docs/round using the exact output filename.
2. Run the v12 ingestion/calibration pipeline, not a live scanner.
3. Validate trigger rows for required fields, canonical trigger labels, complete MFE/MAE 30/90/180D, and no corporate-action contamination.
4. Use the aggregate/shadow/residual rows only as candidate profile evidence.
5. Do not change production scoring solely from this file; merge with the broader C06 corpus and promotion decision ledger.
6. Consider a C06-specific rule candidate: customer/capacity lock requires qualification/volume bridge; partial approval blocks Yellow/Green; hard 4C can decay after price reset plus redesigned product path.
```

## 14. Next research state

```text
completed_round = R2
completed_loop = 122
selection_basis = docs/core/V12_Research_No_Repeat_Index.md
selected_priority_bucket = Priority 0 / C06_HBM_MEMORY_CUSTOMER_CAPACITY
round_schedule_status = coverage_index_selected
round_sector_consistency = pass
production_scoring_changed = false
shadow_weight_only = true
next_recommended_archetypes = C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH, C11_BATTERY_ORDERBOOK_RERATING, C01_ORDER_BACKLOG_MARGIN_BRIDGE, C28_SOFTWARE_SECURITY_CONTRACT_RETENTION, C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK
```
