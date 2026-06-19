# E2R Stock-Web v12 Residual Research — R4 / L4 / C15 Material Spread Supercycle

```text
research_session = post_calibrated_sector_archetype_residual_research
mode = historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12
output_file = e2r_stock_web_v12_residual_round_R4_loop_191_L4_MATERIALS_SPREAD_RESOURCE_C15_MATERIAL_SPREAD_SUPERCYCLE_research.md
production_scoring_changed = false
shadow_weight_only = true
stock_agent_code_access_allowed = false
stock_agent_code_patch_allowed = false
stock_agent_live_scan_allowed = false
current_stock_discovery_allowed = false
price_route_hunt_allowed = false
```

## 0. Research constants

```text
selected_round = R4
selected_loop = 191
large_sector_id = L4_MATERIALS_SPREAD_RESOURCE
canonical_archetype_id = C15_MATERIAL_SPREAD_SUPERCYCLE
fine_archetype_family = MATERIAL_SPREAD_DURATION_INVENTORY_GAIN_REVERSAL
selection_basis = docs/core/V12_Research_No_Repeat_Index.md
scheduler_mode = coverage_index_first
round_sector_consistency = pass
```

This file is a standalone historical calibration MD. It does not implement or propose an immediate production patch. It only records trigger-level evidence, actual stock-web price paths, score/stage alignment stress tests, and a deferred coding-agent handoff.

## 1. Coverage-index selection and No-Repeat audit

The No-Repeat Index is used only as a coverage and duplicate ledger. Current C15 status is treated as **sufficient row count but still quality-reinforcement eligible**, especially because C15 has many spread-cycle rows but remains vulnerable to late-cycle evidence, inventory gain language, source-quality repair, and insufficient 4C separation.

```text
selected_canonical_archetype_id = C15_MATERIAL_SPREAD_SUPERCYCLE
reason_for_selection = Priority 1 quality reinforcement after C05/C01/C13 recent runs
recent_conversation_archetypes_avoided = C05, C01, C13
new_symbol_count = 7
new_independent_case_count = 8
new_independent_trigger_count = 8
hard_duplicate_key_format = canonical_archetype_id + symbol + trigger_type + entry_date
hard_duplicate_detected_in_batch = false
new_independent_ratio = 1.00
```

The selected C15 research question is not “do commodity/spread headlines work?” The tighter residual question is:

> When steel, refining, copper, or metal spread evidence appears after a sharp price/spread cycle, what extra evidence is required before Stage2-Actionable can become Stage3-Yellow or Green?

## 2. Stock-Web price atlas validation

```text
price_atlas_repo = https://github.com/Songdaiki/stock-web
upstream_source = FinanceData/marcap
price_basis = tradable_raw
price_adjustment_status = raw_unadjusted_marcap
manifest_min_date = 1995-05-02
manifest_max_date = 2026-02-20
tradable_row_count = 14354401
raw_row_count = 15214118
calibration_shard_root = atlas/ohlcv_tradable_by_symbol_year
tradable_columns = d,o,h,l,c,v,a,mc,s,m
```

MFE / MAE calculations use entry close as denominator and the maximum high / minimum low from entry date through the selected number of tradable rows. Entry is the next tradable day after evidence date unless same-day timing is explicitly usable. All eight trigger rows below have 180 tradable rows available by the manifest max date.

Corporate action contamination screen:

```text
method = tradable shard s-column constant check + raw close-ratio discontinuity screen
180D_window_rule = if shares change or major raw discontinuity appears, calibration_usable=false
batch_result = all usable trigger rows passed 180D clean-window screen
```

## 3. Coverage matrix for this batch

| Metric | Value |
|---|---:|
| new_independent_case_count | 8 |
| new_independent_trigger_count | 8 |
| unique_symbol_count | 7 |
| calibration_usable_case_count | 8 |
| positive_or_local_positive_case_count | 3 |
| counterexample_or_guardrail_case_count | 5 |
| source_proxy_only_count | 0 |
| evidence_url_pending_count | 0 |
| missing_required_mfe_mae_count | 0 |
| corporate_action_contaminated_180D_count | 0 |
| insufficient_forward_window_180D_count | 0 |
| current_profile_error_count | 6 |

## 4. Trigger-level backtest table

| Symbol | Company | Trigger | Evidence date | Entry date | Entry close | 30D MFE/MAE | 90D MFE/MAE | 180D MFE/MAE | 180D peak | DD after peak | Role |
|---|---|---|---:|---:|---:|---:|---:|---:|---|---:|---|
| 005490 | POSCO / POSCO Holdings | Stage2-Actionable | 2021-04-26 | 2021-04-27 | 377,500 | 9.54% / -11.79% | 9.54% / -18.94% | 9.54% / -31.13% | 2021-05-10 @ 413,500 | -37.12% | counterexample |
| 004020 | Hyundai Steel | Stage2-Actionable | 2021-04-27 | 2021-04-28 | 57,400 | 9.76% / -12.02% | 9.76% / -21.17% | 9.76% / -35.45% | 2021-05-11 @ 63,000 | -41.19% | counterexample |
| 001230 | Dongkuk Steel legacy entity | Stage2-Actionable | 2021-05-17 | 2021-05-18 | 25,250 | 2.57% / -18.81% | 2.57% / -30.69% | 2.57% / -46.93% | 2021-05-18 @ 25,900 | -48.26% | hard_counterexample |
| 001430 | SeAH Besteel | Stage2-Actionable | 2021-04-29 | 2021-04-30 | 26,150 | 39.39% / -10.71% | 39.39% / -10.71% | 39.39% / -33.84% | 2021-05-11 @ 36,450 | -52.54% | local_positive_high_drawdown |
| 010950 | S-Oil | Stage2-Actionable | 2022-04-27 | 2022-04-28 | 104,500 | 17.70% / -2.87% | 17.70% / -18.85% | 17.70% / -26.22% | 2022-06-13 @ 123,000 | -37.32% | local_positive_counterexample |
| 103140 | Poongsan | Stage2-Actionable | 2024-05-14 | 2024-05-16 | 77,300 | 0.91% / -28.07% | 0.91% / -39.20% | 0.91% / -40.30% | 2024-05-16 @ 78,000 | -40.83% | hard_counterexample |
| 010950 | S-Oil | 4B | 2024-04-26 | 2024-04-29 | 73,200 | 1.23% / -9.29% | 1.23% / -19.81% | 1.23% / -27.05% | 2024-04-29 @ 74,100 | -27.94% | stage4b_confirmation |
| 025820 | Igu Industry | Stage2-Actionable | 2024-10-10 | 2024-10-11 | 4,780 | 6.49% / -22.18% | 6.49% / -25.84% | 26.78% / -25.84% | 2025-03-26 @ 6,060 | -35.40% | lagging_positive_high_mae |

## 5. Per-case residual notes


### 1. C15-005490-20210426-STAGE2A — POSCO / POSCO Holdings (005490)

- **Evidence family:** `steel_price_hike_plus_demand_recovery_earnings_beat`
- **Evidence URL:** https://en.yna.co.kr/view/AEN20210426002851320
- **Evidence summary:** Q1 operating profit jumped to KRW 1.55tn and product price hikes on auto/ship/construction steel demand explained the improvement.
- **Trigger / entry:** trigger `2021-04-26`, entry `2021-04-27` at close `377,500`.
- **Actual 1D result:** 30D MFE/MAE `9.54%` / `-11.79%`, 90D `9.54%` / `-18.94%`, 180D `9.54%` / `-31.13%`.
- **Path shape:** 180D peak `2021-05-10` at `413,500`, trough `2021-11-30` at `260,000`, drawdown after peak `-37.12%`.
- **Residual read:** The spread and price-hike evidence was real, but the best 180D high arrived within two weeks and the later drawdown was much larger than upside.
- **Score/stage simulation:** `Stage3-Yellow` / `78.0` → `Stage2-Actionable` / `70.5` under shadow rule only.


### 2. C15-004020-20210427-STAGE2A — Hyundai Steel (004020)

- **Evidence family:** `steel_price_hike_turnaround_earnings_beat`
- **Evidence URL:** https://en.yna.co.kr/view/AEN20210427007052320
- **Evidence summary:** Hyundai Steel swung to profit in Q1 2021; price hikes and demand recovery lifted sales and operating profit beat consensus.
- **Trigger / entry:** trigger `2021-04-27`, entry `2021-04-28` at close `57,400`.
- **Actual 1D result:** 30D MFE/MAE `9.76%` / `-12.02%`, 90D `9.76%` / `-21.17%`, 180D `9.76%` / `-35.45%`.
- **Path shape:** 180D peak `2021-05-11` at `63,000`, trough `2021-12-01` at `37,050`, drawdown after peak `-41.19%`.
- **Residual read:** The fundamental evidence was broad and timely, but the price path again peaked early and turned into a deep 180D drawdown.
- **Score/stage simulation:** `Stage3-Yellow` / `77.5` → `Stage2-Actionable` / `70.0` under shadow rule only.


### 3. C15-001230-20210517-STAGE2A — Dongkuk Steel legacy entity (001230)

- **Evidence family:** `rebar_price_rally_q1_profit_spike`
- **Evidence URL:** https://www.kedglobal.com/earnings/newsView/ked202105170018
- **Evidence summary:** Q1 operating profit hit a five-year high while rebar/steel prices had already jumped sharply in the recovery cycle.
- **Trigger / entry:** trigger `2021-05-17`, entry `2021-05-18` at close `25,250`.
- **Actual 1D result:** 30D MFE/MAE `2.57%` / `-18.81%`, 90D `2.57%` / `-30.69%`, 180D `2.57%` / `-46.93%`.
- **Path shape:** 180D peak `2021-05-18` at `25,900`, trough `2022-01-27` at `13,400`, drawdown after peak `-48.26%`.
- **Residual read:** Evidence arrived after the cycle had already expressed itself in price; 180D upside was almost absent while MAE exceeded -45%.
- **Score/stage simulation:** `Stage2-Actionable` / `76.0` → `Stage2` / `66.0` under shadow rule only.


### 4. C15-001430-20210429-STAGE2A — SeAH Besteel (001430)

- **Evidence family:** `special_steel_q1_profit_spike`
- **Evidence URL:** https://www.asiae.co.kr/en/article/2021042915294119605
- **Evidence summary:** Q1 provisional sales and operating profit rose sharply YoY, giving a clean near-term spread-cycle confirmation.
- **Trigger / entry:** trigger `2021-04-29`, entry `2021-04-30` at close `26,150`.
- **Actual 1D result:** 30D MFE/MAE `39.39%` / `-10.71%`, 90D `39.39%` / `-10.71%`, 180D `39.39%` / `-33.84%`.
- **Path shape:** 180D peak `2021-05-11` at `36,450`, trough `2022-01-19` at `17,300`, drawdown after peak `-52.54%`.
- **Residual read:** This is the useful positive control: local MFE was strong, but full-window drawdown argues against automatic Green.
- **Score/stage simulation:** `Stage3-Yellow` / `78.0` → `Stage3-Yellow` / `75.0` under shadow rule only.


### 5. C15-010950-20220427-STAGE2A — S-Oil (010950)

- **Evidence family:** `refining_crack_margin_inventory_gain_earnings_beat`
- **Evidence URL:** https://en.yna.co.kr/view/AEN20220427005752320
- **Evidence summary:** Q1 earnings more than doubled on improved sales, inventory-related gains, strong cracking margin, and higher oil prices.
- **Trigger / entry:** trigger `2022-04-27`, entry `2022-04-28` at close `104,500`.
- **Actual 1D result:** 30D MFE/MAE `17.70%` / `-2.87%`, 90D `17.70%` / `-18.85%`, 180D `17.70%` / `-26.22%`.
- **Path shape:** 180D peak `2022-06-13` at `123,000`, trough `2023-01-06` at `77,100`, drawdown after peak `-37.32%`.
- **Residual read:** The first 30D worked, but the 180D path turned down as inventory-gain and refining-margin tailwinds normalized.
- **Score/stage simulation:** `Stage3-Yellow` / `79.0` → `Stage2-Actionable` / `72.0` under shadow rule only.


### 6. C15-103140-20240514-STAGE2A — Poongsan (103140)

- **Evidence family:** `copper_price_rally_plus_defense_peak_expectation`
- **Evidence URL:** https://v.daum.net/v/fXzID0JqJ6?f=p
- **Evidence summary:** Copper price rise and defense seasonality were framed as 2Q earnings drivers, while 1Q had already slowed and cost/volume quality was mixed.
- **Trigger / entry:** trigger `2024-05-14`, entry `2024-05-16` at close `77,300`.
- **Actual 1D result:** 30D MFE/MAE `0.91%` / `-28.07%`, 90D `0.91%` / `-39.20%`, 180D `0.91%` / `-40.30%`.
- **Path shape:** 180D peak `2024-05-16` at `78,000`, trough `2024-12-09` at `46,150`, drawdown after peak `-40.83%`.
- **Residual read:** Commodity price thesis did not translate into stock-specific forward returns; peak was the entry day and 180D MAE exceeded -40%.
- **Score/stage simulation:** `Stage2-Actionable` / `77.0` → `Stage2` / `65.5` under shadow rule only.


### 7. C15-010950-20240426-STAGE4B — S-Oil (010950)

- **Evidence family:** `refining_margin_outlook_but_utilization_and_cycle_quality_watch`
- **Evidence URL:** https://www.reuters.com/business/energy/s-oil-says-q2-refining-margins-remain-steady-then-trend-upward-2024-04-26/
- **Evidence summary:** S-Oil forecast steady/upward Q2 margins, but CDU utilization was lower than the prior quarter and maintenance risk was visible.
- **Trigger / entry:** trigger `2024-04-26`, entry `2024-04-29` at close `73,200`.
- **Actual 1D result:** 30D MFE/MAE `1.23%` / `-9.29%`, 90D `1.23%` / `-19.81%`, 180D `1.23%` / `-27.05%`.
- **Path shape:** 180D peak `2024-04-29` at `74,100`, trough `2024-12-09` at `53,400`, drawdown after peak `-27.94%`.
- **Residual read:** This validates an earlier local 4B watch: not necessarily hard 4C on day one, but positive-stage promotion should be blocked.
- **Score/stage simulation:** `Stage2` / `68.0` → `4B` / `63.0` under shadow rule only.


### 8. C15-025820-20241010-STAGE2A — Igu Industry (025820)

- **Evidence family:** `copper_lagging_effect_profit_improvement_cost_offset`
- **Evidence URL:** https://www.ibtomato.com/ExternalView.aspx?no=13254&type=1
- **Evidence summary:** H1 profit improved on copper-price lagging effect, but the article also flagged uncertainty, cost pressure, and roll-margin needs.
- **Trigger / entry:** trigger `2024-10-10`, entry `2024-10-11` at close `4,780`.
- **Actual 1D result:** 30D MFE/MAE `6.49%` / `-22.18%`, 90D `6.49%` / `-25.84%`, 180D `26.78%` / `-25.84%`.
- **Path shape:** 180D peak `2025-03-26` at `6,060`, trough `2024-12-09` at `3,545`, drawdown after peak `-35.40%`.
- **Residual read:** This is a delayed positive but not clean Green: 180D MFE eventually reached 26.78%, while interim MAE exceeded -25%.
- **Score/stage simulation:** `Stage2-Actionable` / `75.0` → `Stage2-Actionable` / `71.0` under shadow rule only.


## 6. Stage/score residual interpretation

### Main residual

C15 spread-cycle evidence is **real but path-sensitive**. In this batch, steel price hikes, rebar spread expansion, refining margin/inventory gains, copper lagging effects, and copper-defense mixed theses often produced either very short-lived MFE or delayed MFE with large interim MAE. The failure mode is not missing evidence; it is **duration blindness**.

```text
residual_contribution_label = material_spread_duration_and_inventory_gain_reversal_quality_repair
new_axis_proposed = false
existing_axis_strengthened = stage2_required_bridge, price_only_blowoff_blocks_positive_stage, full_4b_requires_non_price_evidence
existing_axis_refined = hard_4c_confirmation_requires_duration_or_thesis_break_follow_through
existing_axis_weakened = none
```

### C15 shadow rule candidate

```text
rule_candidate = C15_SPREAD_DURATION_AND_INVENTORY_GAIN_REVERSAL_GATE
scope = large_sector:L4 + canonical:C15 only
production_scoring_changed = false
shadow_weight_only = true
```

Proposed shadow logic:

1. **Spread duration gate:** Stage3-Yellow requires either confirmed forward spread persistence, company-specific contract/ASP duration, or volume-cost bridge. A single quarter of spread windfall is Stage2 evidence, not Green evidence.
2. **Inventory gain blocker:** If profit beat is materially driven by inventory-related gain or input-price timing, cap at Stage2-Actionable unless recurring margin bridge appears.
3. **Commodity headline blocker:** Copper/steel/oil headline price strength requires stock-specific operating bridge. Commodity price alone should not lift valuation-rerating or market-mispricing components enough for Yellow/Green.
4. **Late-cycle 4B watch:** If entry is near a prior spread/stock peak and forward evidence lacks duration, local 4B watch can activate without forcing immediate hard 4C.

### Shadow component delta candidate

| Component | Direction | Rationale |
|---|---:|---|
| bottleneck_pricing | -1.0 | Reduce credit when price/spread evidence is already late-cycle or inventory-gain driven. |
| earnings_visibility | -0.5 | Single-quarter commodity earnings are less durable without forward contract/volume bridge. |
| valuation_rerating | -1.0 | Avoid rerating credit when 180D path shows peak-proximity reversal. |
| information_confidence | +0.5 | Add confidence only when source is direct and bridge language is specific. |

## 7. Machine-readable JSONL rows

```jsonl
{"row_type":"price_source_validation","research_file":"e2r_stock_web_v12_residual_round_R4_loop_191_L4_MATERIALS_SPREAD_RESOURCE_C15_MATERIAL_SPREAD_SUPERCYCLE_research.md","manifest":{"source_name":"FinanceData/marcap","source_repo_url":"https://github.com/FinanceData/marcap","price_atlas_repo":"https://github.com/Songdaiki/stock-web","price_adjustment_status":"raw_unadjusted_marcap","price_basis":"tradable_raw","min_date":"1995-05-02","max_date":"2026-02-20","tradable_row_count":14354401,"raw_row_count":15214118,"symbol_count":5414,"active_like_symbol_count":2868,"inactive_or_delisted_like_symbol_count":2546,"calibration_shard_root":"atlas/ohlcv_tradable_by_symbol_year","schema_path":"atlas/schema.json","universe_path":"atlas/universe/all_symbols.csv"},"schema_mfe_mae_definition":"MFE_N=(max_high_from_entry_through_N_rows/entry_close)-1; MAE_N=(min_low_from_entry_through_N_rows/entry_close)-1","entry_price_basis":"entry close of next tradable day after evidence date unless evidence timing allows same-day","validation_status":"pass"}
{"row_type":"case","case_id":"C15-005490-20210426-STAGE2A","symbol":"005490","company_name":"POSCO / POSCO Holdings","large_sector_id":"L4_MATERIALS_SPREAD_RESOURCE","canonical_archetype_id":"C15_MATERIAL_SPREAD_SUPERCYCLE","fine_archetype_id":"STEEL_SPREAD_PRICE_HIKE_INVENTORY_PEAK_REVERSAL","case_role":"counterexample","evidence_family":"steel_price_hike_plus_demand_recovery_earnings_beat","trigger_date":"2021-04-26","entry_date":"2021-04-27","evidence_url":"https://en.yna.co.kr/view/AEN20210426002851320","evidence_summary":"Q1 operating profit jumped to KRW 1.55tn and product price hikes on auto/ship/construction steel demand explained the improvement.","calibration_usable":true,"corporate_action_window_status":"clean_by_tradable_shard_s_and_close_ratio","novelty_key":"C15_MATERIAL_SPREAD_SUPERCYCLE|005490|Stage2-Actionable|2021-04-27"}
{"row_type":"trigger","case_id":"C15-005490-20210426-STAGE2A","symbol":"005490","company_name":"POSCO / POSCO Holdings","large_sector_id":"L4_MATERIALS_SPREAD_RESOURCE","canonical_archetype_id":"C15_MATERIAL_SPREAD_SUPERCYCLE","fine_archetype_id":"STEEL_SPREAD_PRICE_HIKE_INVENTORY_PEAK_REVERSAL","trigger_type":"Stage2-Actionable","trigger_date":"2021-04-26","entry_date":"2021-04-27","entry_price":377500,"entry_ohlc":{"o":366000,"h":383000,"l":365500,"c":377500,"v":734422,"a":276851520500,"mc":32913030212500,"s":87186835,"m":"KOSPI"},"MFE_30D_pct":9.54,"MAE_30D_pct":-11.79,"MFE_90D_pct":9.54,"MAE_90D_pct":-18.94,"MFE_180D_pct":9.54,"MAE_180D_pct":-31.13,"MFE_1Y_pct":9.54,"MAE_1Y_pct":-32.19,"MFE_2Y_pct":null,"MAE_2Y_pct":null,"peak_180D_date":"2021-05-10","peak_180D_price":413500,"trough_180D_date":"2021-11-30","trough_180D_price":260000,"drawdown_after_peak_pct":-37.12,"forward_window_trading_days":180,"price_source_validation":"stock_web_tradable_raw_1D_verified","tradable_shards":["atlas/ohlcv_tradable_by_symbol_year/005/005490/2021.csv","atlas/ohlcv_tradable_by_symbol_year/005/005490/2022.csv"],"profile_contamination_check":"clean_by_tradable_shard_s_and_close_ratio","calibration_usable":true,"blocked_reason":null,"case_role":"counterexample","residual_label":"steel_price_hike_headline_not_enough_for_full_window_rerating","dedupe_key":"C15_MATERIAL_SPREAD_SUPERCYCLE|005490|Stage2-Actionable|2021-04-27"}
{"row_type":"score_simulation","case_id":"C15-005490-20210426-STAGE2A","symbol":"005490","profile_proxy":"e2r_2_1_stock_web_calibrated_current_proxy","raw_component_scores":{"eps_fcf_explosion":7.5,"earnings_visibility":7.0,"bottleneck_pricing":8.0,"market_mispricing":6.5,"valuation_rerating":5.5,"capital_allocation":4.0,"information_confidence":7.0},"weighted_total_before_shadow":78.0,"stage_before_shadow":"Stage3-Yellow","weighted_total_after_shadow":70.5,"stage_after_shadow":"Stage2-Actionable","shadow_rule_applied":"C15_SPREAD_DURATION_AND_INVENTORY_GAIN_REVERSAL_GATE","production_scoring_changed":false,"alignment_note":"The spread and price-hike evidence was real, but the best 180D high arrived within two weeks and the later drawdown was much larger than upside."}
{"row_type":"case","case_id":"C15-004020-20210427-STAGE2A","symbol":"004020","company_name":"Hyundai Steel","large_sector_id":"L4_MATERIALS_SPREAD_RESOURCE","canonical_archetype_id":"C15_MATERIAL_SPREAD_SUPERCYCLE","fine_archetype_id":"STEEL_SPREAD_PRICE_HIKE_INVENTORY_PEAK_REVERSAL","case_role":"counterexample","evidence_family":"steel_price_hike_turnaround_earnings_beat","trigger_date":"2021-04-27","entry_date":"2021-04-28","evidence_url":"https://en.yna.co.kr/view/AEN20210427007052320","evidence_summary":"Hyundai Steel swung to profit in Q1 2021; price hikes and demand recovery lifted sales and operating profit beat consensus.","calibration_usable":true,"corporate_action_window_status":"clean_by_tradable_shard_s_and_close_ratio","novelty_key":"C15_MATERIAL_SPREAD_SUPERCYCLE|004020|Stage2-Actionable|2021-04-28"}
{"row_type":"trigger","case_id":"C15-004020-20210427-STAGE2A","symbol":"004020","company_name":"Hyundai Steel","large_sector_id":"L4_MATERIALS_SPREAD_RESOURCE","canonical_archetype_id":"C15_MATERIAL_SPREAD_SUPERCYCLE","fine_archetype_id":"STEEL_SPREAD_PRICE_HIKE_INVENTORY_PEAK_REVERSAL","trigger_type":"Stage2-Actionable","trigger_date":"2021-04-27","entry_date":"2021-04-28","entry_price":57400,"entry_ohlc":{"o":57800,"h":58800,"l":55700,"c":57400,"v":3870822,"a":222090327700,"mc":7659788059000,"s":133445785,"m":"KOSPI"},"MFE_30D_pct":9.76,"MAE_30D_pct":-12.02,"MFE_90D_pct":9.76,"MAE_90D_pct":-21.17,"MFE_180D_pct":9.76,"MAE_180D_pct":-35.45,"MFE_1Y_pct":9.76,"MAE_1Y_pct":-35.45,"MFE_2Y_pct":null,"MAE_2Y_pct":null,"peak_180D_date":"2021-05-11","peak_180D_price":63000,"trough_180D_date":"2021-12-01","trough_180D_price":37050,"drawdown_after_peak_pct":-41.19,"forward_window_trading_days":180,"price_source_validation":"stock_web_tradable_raw_1D_verified","tradable_shards":["atlas/ohlcv_tradable_by_symbol_year/004/004020/2021.csv","atlas/ohlcv_tradable_by_symbol_year/004/004020/2022.csv"],"profile_contamination_check":"clean_by_tradable_shard_s_and_close_ratio","calibration_usable":true,"blocked_reason":null,"case_role":"counterexample","residual_label":"earnings_beat_without_forward_spread_duration","dedupe_key":"C15_MATERIAL_SPREAD_SUPERCYCLE|004020|Stage2-Actionable|2021-04-28"}
{"row_type":"score_simulation","case_id":"C15-004020-20210427-STAGE2A","symbol":"004020","profile_proxy":"e2r_2_1_stock_web_calibrated_current_proxy","raw_component_scores":{"eps_fcf_explosion":7.5,"earnings_visibility":7.0,"bottleneck_pricing":7.5,"market_mispricing":6.0,"valuation_rerating":5.5,"capital_allocation":4.0,"information_confidence":7.0},"weighted_total_before_shadow":77.5,"stage_before_shadow":"Stage3-Yellow","weighted_total_after_shadow":70.0,"stage_after_shadow":"Stage2-Actionable","shadow_rule_applied":"C15_SPREAD_DURATION_AND_INVENTORY_GAIN_REVERSAL_GATE","production_scoring_changed":false,"alignment_note":"The fundamental evidence was broad and timely, but the price path again peaked early and turned into a deep 180D drawdown."}
{"row_type":"case","case_id":"C15-001230-20210517-STAGE2A","symbol":"001230","company_name":"Dongkuk Steel legacy entity","large_sector_id":"L4_MATERIALS_SPREAD_RESOURCE","canonical_archetype_id":"C15_MATERIAL_SPREAD_SUPERCYCLE","fine_archetype_id":"REBAR_SPREAD_LATE_CYCLE_BLOWOFF","case_role":"hard_counterexample","evidence_family":"rebar_price_rally_q1_profit_spike","trigger_date":"2021-05-17","entry_date":"2021-05-18","evidence_url":"https://www.kedglobal.com/earnings/newsView/ked202105170018","evidence_summary":"Q1 operating profit hit a five-year high while rebar/steel prices had already jumped sharply in the recovery cycle.","calibration_usable":true,"corporate_action_window_status":"clean_by_tradable_shard_s_and_close_ratio","novelty_key":"C15_MATERIAL_SPREAD_SUPERCYCLE|001230|Stage2-Actionable|2021-05-18"}
{"row_type":"trigger","case_id":"C15-001230-20210517-STAGE2A","symbol":"001230","company_name":"Dongkuk Steel legacy entity","large_sector_id":"L4_MATERIALS_SPREAD_RESOURCE","canonical_archetype_id":"C15_MATERIAL_SPREAD_SUPERCYCLE","fine_archetype_id":"REBAR_SPREAD_LATE_CYCLE_BLOWOFF","trigger_type":"Stage2-Actionable","trigger_date":"2021-05-17","entry_date":"2021-05-18","entry_price":25250,"entry_ohlc":{"o":23750,"h":25900,"l":23500,"c":25250,"v":5334664,"a":132634345050,"mc":2409676609250,"s":95432737,"m":"KOSPI"},"MFE_30D_pct":2.57,"MAE_30D_pct":-18.81,"MFE_90D_pct":2.57,"MAE_90D_pct":-30.69,"MFE_180D_pct":2.57,"MAE_180D_pct":-46.93,"MFE_1Y_pct":2.57,"MAE_1Y_pct":-46.93,"MFE_2Y_pct":null,"MAE_2Y_pct":null,"peak_180D_date":"2021-05-18","peak_180D_price":25900,"trough_180D_date":"2022-01-27","trough_180D_price":13400,"drawdown_after_peak_pct":-48.26,"forward_window_trading_days":180,"price_source_validation":"stock_web_tradable_raw_1D_verified","tradable_shards":["atlas/ohlcv_tradable_by_symbol_year/001/001230/2021.csv","atlas/ohlcv_tradable_by_symbol_year/001/001230/2022.csv"],"profile_contamination_check":"clean_by_tradable_shard_s_and_close_ratio","calibration_usable":true,"blocked_reason":null,"case_role":"hard_counterexample","residual_label":"late_price_spread_cycle_stage2_false_positive","dedupe_key":"C15_MATERIAL_SPREAD_SUPERCYCLE|001230|Stage2-Actionable|2021-05-18"}
{"row_type":"score_simulation","case_id":"C15-001230-20210517-STAGE2A","symbol":"001230","profile_proxy":"e2r_2_1_stock_web_calibrated_current_proxy","raw_component_scores":{"eps_fcf_explosion":7.0,"earnings_visibility":6.5,"bottleneck_pricing":7.0,"market_mispricing":5.5,"valuation_rerating":5.0,"capital_allocation":3.0,"information_confidence":6.5},"weighted_total_before_shadow":76.0,"stage_before_shadow":"Stage2-Actionable","weighted_total_after_shadow":66.0,"stage_after_shadow":"Stage2","shadow_rule_applied":"C15_SPREAD_DURATION_AND_INVENTORY_GAIN_REVERSAL_GATE","production_scoring_changed":false,"alignment_note":"Evidence arrived after the cycle had already expressed itself in price; 180D upside was almost absent while MAE exceeded -45%."}
{"row_type":"case","case_id":"C15-001430-20210429-STAGE2A","symbol":"001430","company_name":"SeAH Besteel","large_sector_id":"L4_MATERIALS_SPREAD_RESOURCE","canonical_archetype_id":"C15_MATERIAL_SPREAD_SUPERCYCLE","fine_archetype_id":"SPECIAL_STEEL_SPREAD_LOCAL_WIN_FULL_WINDOW_REVERSAL","case_role":"local_positive_high_drawdown","evidence_family":"special_steel_q1_profit_spike","trigger_date":"2021-04-29","entry_date":"2021-04-30","evidence_url":"https://www.asiae.co.kr/en/article/2021042915294119605","evidence_summary":"Q1 provisional sales and operating profit rose sharply YoY, giving a clean near-term spread-cycle confirmation.","calibration_usable":true,"corporate_action_window_status":"clean_by_tradable_shard_s_and_close_ratio","novelty_key":"C15_MATERIAL_SPREAD_SUPERCYCLE|001430|Stage2-Actionable|2021-04-30"}
{"row_type":"trigger","case_id":"C15-001430-20210429-STAGE2A","symbol":"001430","company_name":"SeAH Besteel","large_sector_id":"L4_MATERIALS_SPREAD_RESOURCE","canonical_archetype_id":"C15_MATERIAL_SPREAD_SUPERCYCLE","fine_archetype_id":"SPECIAL_STEEL_SPREAD_LOCAL_WIN_FULL_WINDOW_REVERSAL","trigger_type":"Stage2-Actionable","trigger_date":"2021-04-29","entry_date":"2021-04-30","entry_price":26150,"entry_ohlc":{"o":28300,"h":28450,"l":24800,"c":26150,"v":968598,"a":25647696650,"mc":937794411850,"s":35862119,"m":"KOSPI"},"MFE_30D_pct":39.39,"MAE_30D_pct":-10.71,"MFE_90D_pct":39.39,"MAE_90D_pct":-10.71,"MFE_180D_pct":39.39,"MAE_180D_pct":-33.84,"MFE_1Y_pct":39.39,"MAE_1Y_pct":-45.51,"MFE_2Y_pct":null,"MAE_2Y_pct":null,"peak_180D_date":"2021-05-11","peak_180D_price":36450,"trough_180D_date":"2022-01-19","trough_180D_price":17300,"drawdown_after_peak_pct":-52.54,"forward_window_trading_days":180,"price_source_validation":"stock_web_tradable_raw_1D_verified","tradable_shards":["atlas/ohlcv_tradable_by_symbol_year/001/001430/2021.csv","atlas/ohlcv_tradable_by_symbol_year/001/001430/2022.csv"],"profile_contamination_check":"clean_by_tradable_shard_s_and_close_ratio","calibration_usable":true,"blocked_reason":null,"case_role":"local_positive_high_drawdown","residual_label":"local_mfe_success_but_green_blocked_by_180d_drawdown","dedupe_key":"C15_MATERIAL_SPREAD_SUPERCYCLE|001430|Stage2-Actionable|2021-04-30"}
{"row_type":"score_simulation","case_id":"C15-001430-20210429-STAGE2A","symbol":"001430","profile_proxy":"e2r_2_1_stock_web_calibrated_current_proxy","raw_component_scores":{"eps_fcf_explosion":8.0,"earnings_visibility":7.5,"bottleneck_pricing":7.5,"market_mispricing":6.0,"valuation_rerating":5.0,"capital_allocation":3.5,"information_confidence":7.0},"weighted_total_before_shadow":78.0,"stage_before_shadow":"Stage3-Yellow","weighted_total_after_shadow":75.0,"stage_after_shadow":"Stage3-Yellow","shadow_rule_applied":"C15_SPREAD_DURATION_AND_INVENTORY_GAIN_REVERSAL_GATE","production_scoring_changed":false,"alignment_note":"This is the useful positive control: local MFE was strong, but full-window drawdown argues against automatic Green."}
{"row_type":"case","case_id":"C15-010950-20220427-STAGE2A","symbol":"010950","company_name":"S-Oil","large_sector_id":"L4_MATERIALS_SPREAD_RESOURCE","canonical_archetype_id":"C15_MATERIAL_SPREAD_SUPERCYCLE","fine_archetype_id":"REFINING_MARGIN_INVENTORY_GAIN_LOCAL_WIN_REVERSAL","case_role":"local_positive_counterexample","evidence_family":"refining_crack_margin_inventory_gain_earnings_beat","trigger_date":"2022-04-27","entry_date":"2022-04-28","evidence_url":"https://en.yna.co.kr/view/AEN20220427005752320","evidence_summary":"Q1 earnings more than doubled on improved sales, inventory-related gains, strong cracking margin, and higher oil prices.","calibration_usable":true,"corporate_action_window_status":"clean_by_tradable_shard_s_and_close_ratio","novelty_key":"C15_MATERIAL_SPREAD_SUPERCYCLE|010950|Stage2-Actionable|2022-04-28"}
{"row_type":"trigger","case_id":"C15-010950-20220427-STAGE2A","symbol":"010950","company_name":"S-Oil","large_sector_id":"L4_MATERIALS_SPREAD_RESOURCE","canonical_archetype_id":"C15_MATERIAL_SPREAD_SUPERCYCLE","fine_archetype_id":"REFINING_MARGIN_INVENTORY_GAIN_LOCAL_WIN_REVERSAL","trigger_type":"Stage2-Actionable","trigger_date":"2022-04-27","entry_date":"2022-04-28","entry_price":104500,"entry_ohlc":{"o":106000,"h":107000,"l":103500,"c":104500,"v":334912,"a":35015614500,"mc":11764901764000,"s":112582792,"m":"KOSPI"},"MFE_30D_pct":17.7,"MAE_30D_pct":-2.87,"MFE_90D_pct":17.7,"MAE_90D_pct":-18.85,"MFE_180D_pct":17.7,"MAE_180D_pct":-26.22,"MFE_1Y_pct":17.7,"MAE_1Y_pct":-32.44,"MFE_2Y_pct":null,"MAE_2Y_pct":null,"peak_180D_date":"2022-06-13","peak_180D_price":123000,"trough_180D_date":"2023-01-06","trough_180D_price":77100,"drawdown_after_peak_pct":-37.32,"forward_window_trading_days":180,"price_source_validation":"stock_web_tradable_raw_1D_verified","tradable_shards":["atlas/ohlcv_tradable_by_symbol_year/010/010950/2022.csv","atlas/ohlcv_tradable_by_symbol_year/010/010950/2023.csv"],"profile_contamination_check":"clean_by_tradable_shard_s_and_close_ratio","calibration_usable":true,"blocked_reason":null,"case_role":"local_positive_counterexample","residual_label":"inventory_gain_margin_peak_requires_duration_gate","dedupe_key":"C15_MATERIAL_SPREAD_SUPERCYCLE|010950|Stage2-Actionable|2022-04-28"}
{"row_type":"score_simulation","case_id":"C15-010950-20220427-STAGE2A","symbol":"010950","profile_proxy":"e2r_2_1_stock_web_calibrated_current_proxy","raw_component_scores":{"eps_fcf_explosion":8.0,"earnings_visibility":7.0,"bottleneck_pricing":8.0,"market_mispricing":6.0,"valuation_rerating":5.5,"capital_allocation":4.0,"information_confidence":7.5},"weighted_total_before_shadow":79.0,"stage_before_shadow":"Stage3-Yellow","weighted_total_after_shadow":72.0,"stage_after_shadow":"Stage2-Actionable","shadow_rule_applied":"C15_SPREAD_DURATION_AND_INVENTORY_GAIN_REVERSAL_GATE","production_scoring_changed":false,"alignment_note":"The first 30D worked, but the 180D path turned down as inventory-gain and refining-margin tailwinds normalized."}
{"row_type":"case","case_id":"C15-103140-20240514-STAGE2A","symbol":"103140","company_name":"Poongsan","large_sector_id":"L4_MATERIALS_SPREAD_RESOURCE","canonical_archetype_id":"C15_MATERIAL_SPREAD_SUPERCYCLE","fine_archetype_id":"COPPER_PRICE_THESIS_WITH_VOLUME_COST_OFFSET","case_role":"hard_counterexample","evidence_family":"copper_price_rally_plus_defense_peak_expectation","trigger_date":"2024-05-14","entry_date":"2024-05-16","evidence_url":"https://v.daum.net/v/fXzID0JqJ6?f=p","evidence_summary":"Copper price rise and defense seasonality were framed as 2Q earnings drivers, while 1Q had already slowed and cost/volume quality was mixed.","calibration_usable":true,"corporate_action_window_status":"clean_by_tradable_shard_s_and_close_ratio","novelty_key":"C15_MATERIAL_SPREAD_SUPERCYCLE|103140|Stage2-Actionable|2024-05-16"}
{"row_type":"trigger","case_id":"C15-103140-20240514-STAGE2A","symbol":"103140","company_name":"Poongsan","large_sector_id":"L4_MATERIALS_SPREAD_RESOURCE","canonical_archetype_id":"C15_MATERIAL_SPREAD_SUPERCYCLE","fine_archetype_id":"COPPER_PRICE_THESIS_WITH_VOLUME_COST_OFFSET","trigger_type":"Stage2-Actionable","trigger_date":"2024-05-14","entry_date":"2024-05-16","entry_price":77300,"entry_ohlc":{"o":78000,"h":78000,"l":74400,"c":77300,"v":562357,"a":42846430300,"mc":2166276689400,"s":28024278,"m":"KOSPI"},"MFE_30D_pct":0.91,"MAE_30D_pct":-28.07,"MFE_90D_pct":0.91,"MAE_90D_pct":-39.2,"MFE_180D_pct":0.91,"MAE_180D_pct":-40.3,"MFE_1Y_pct":0.91,"MAE_1Y_pct":-40.3,"MFE_2Y_pct":null,"MAE_2Y_pct":null,"peak_180D_date":"2024-05-16","peak_180D_price":78000,"trough_180D_date":"2024-12-09","trough_180D_price":46150,"drawdown_after_peak_pct":-40.83,"forward_window_trading_days":180,"price_source_validation":"stock_web_tradable_raw_1D_verified","tradable_shards":["atlas/ohlcv_tradable_by_symbol_year/103/103140/2024.csv","atlas/ohlcv_tradable_by_symbol_year/103/103140/2025.csv","atlas/ohlcv_tradable_by_symbol_year/103/103140/2026.csv"],"profile_contamination_check":"clean_by_tradable_shard_s_and_close_ratio","calibration_usable":true,"blocked_reason":null,"case_role":"hard_counterexample","residual_label":"copper_price_headline_without_company_specific_volume_margin_bridge","dedupe_key":"C15_MATERIAL_SPREAD_SUPERCYCLE|103140|Stage2-Actionable|2024-05-16"}
{"row_type":"score_simulation","case_id":"C15-103140-20240514-STAGE2A","symbol":"103140","profile_proxy":"e2r_2_1_stock_web_calibrated_current_proxy","raw_component_scores":{"eps_fcf_explosion":6.5,"earnings_visibility":6.5,"bottleneck_pricing":7.0,"market_mispricing":6.0,"valuation_rerating":5.0,"capital_allocation":4.0,"information_confidence":6.5},"weighted_total_before_shadow":77.0,"stage_before_shadow":"Stage2-Actionable","weighted_total_after_shadow":65.5,"stage_after_shadow":"Stage2","shadow_rule_applied":"C15_SPREAD_DURATION_AND_INVENTORY_GAIN_REVERSAL_GATE","production_scoring_changed":false,"alignment_note":"Commodity price thesis did not translate into stock-specific forward returns; peak was the entry day and 180D MAE exceeded -40%."}
{"row_type":"case","case_id":"C15-010950-20240426-STAGE4B","symbol":"010950","company_name":"S-Oil","large_sector_id":"L4_MATERIALS_SPREAD_RESOURCE","canonical_archetype_id":"C15_MATERIAL_SPREAD_SUPERCYCLE","fine_archetype_id":"REFINING_MARGIN_LATE_CYCLE_LOCAL_4B","case_role":"stage4b_confirmation","evidence_family":"refining_margin_outlook_but_utilization_and_cycle_quality_watch","trigger_date":"2024-04-26","entry_date":"2024-04-29","evidence_url":"https://www.reuters.com/business/energy/s-oil-says-q2-refining-margins-remain-steady-then-trend-upward-2024-04-26/","evidence_summary":"S-Oil forecast steady/upward Q2 margins, but CDU utilization was lower than the prior quarter and maintenance risk was visible.","calibration_usable":true,"corporate_action_window_status":"clean_by_tradable_shard_s_and_close_ratio","novelty_key":"C15_MATERIAL_SPREAD_SUPERCYCLE|010950|4B|2024-04-29"}
{"row_type":"trigger","case_id":"C15-010950-20240426-STAGE4B","symbol":"010950","company_name":"S-Oil","large_sector_id":"L4_MATERIALS_SPREAD_RESOURCE","canonical_archetype_id":"C15_MATERIAL_SPREAD_SUPERCYCLE","fine_archetype_id":"REFINING_MARGIN_LATE_CYCLE_LOCAL_4B","trigger_type":"4B","trigger_date":"2024-04-26","entry_date":"2024-04-29","entry_price":73200,"entry_ohlc":{"o":74100,"h":74100,"l":72700,"c":73200,"v":361639,"a":26442221100,"mc":8241060374400,"s":112582792,"m":"KOSPI"},"MFE_30D_pct":1.23,"MAE_30D_pct":-9.29,"MFE_90D_pct":1.23,"MAE_90D_pct":-19.81,"MFE_180D_pct":1.23,"MAE_180D_pct":-27.05,"MFE_1Y_pct":1.23,"MAE_1Y_pct":-31.28,"MFE_2Y_pct":null,"MAE_2Y_pct":null,"peak_180D_date":"2024-04-29","peak_180D_price":74100,"trough_180D_date":"2024-12-09","trough_180D_price":53400,"drawdown_after_peak_pct":-27.94,"forward_window_trading_days":180,"price_source_validation":"stock_web_tradable_raw_1D_verified","tradable_shards":["atlas/ohlcv_tradable_by_symbol_year/010/010950/2024.csv","atlas/ohlcv_tradable_by_symbol_year/010/010950/2025.csv"],"profile_contamination_check":"clean_by_tradable_shard_s_and_close_ratio","calibration_usable":true,"blocked_reason":null,"case_role":"stage4b_confirmation","residual_label":"stage4b_watch_before_full_4c_requires_follow_through","dedupe_key":"C15_MATERIAL_SPREAD_SUPERCYCLE|010950|4B|2024-04-29"}
{"row_type":"score_simulation","case_id":"C15-010950-20240426-STAGE4B","symbol":"010950","profile_proxy":"e2r_2_1_stock_web_calibrated_current_proxy","raw_component_scores":{"eps_fcf_explosion":5.0,"earnings_visibility":5.5,"bottleneck_pricing":6.0,"market_mispricing":5.0,"valuation_rerating":4.5,"capital_allocation":4.0,"information_confidence":6.0},"weighted_total_before_shadow":68.0,"stage_before_shadow":"Stage2","weighted_total_after_shadow":63.0,"stage_after_shadow":"4B","shadow_rule_applied":"C15_SPREAD_DURATION_AND_INVENTORY_GAIN_REVERSAL_GATE","production_scoring_changed":false,"alignment_note":"This validates an earlier local 4B watch: not necessarily hard 4C on day one, but positive-stage promotion should be blocked."}
{"row_type":"case","case_id":"C15-025820-20241010-STAGE2A","symbol":"025820","company_name":"Igu Industry","large_sector_id":"L4_MATERIALS_SPREAD_RESOURCE","canonical_archetype_id":"C15_MATERIAL_SPREAD_SUPERCYCLE","fine_archetype_id":"COPPER_LAGGING_EFFECT_ROLL_MARGIN_GATE","case_role":"lagging_positive_high_mae","evidence_family":"copper_lagging_effect_profit_improvement_cost_offset","trigger_date":"2024-10-10","entry_date":"2024-10-11","evidence_url":"https://www.ibtomato.com/ExternalView.aspx?no=13254&type=1","evidence_summary":"H1 profit improved on copper-price lagging effect, but the article also flagged uncertainty, cost pressure, and roll-margin needs.","calibration_usable":true,"corporate_action_window_status":"clean_by_tradable_shard_s_and_close_ratio","novelty_key":"C15_MATERIAL_SPREAD_SUPERCYCLE|025820|Stage2-Actionable|2024-10-11"}
{"row_type":"trigger","case_id":"C15-025820-20241010-STAGE2A","symbol":"025820","company_name":"Igu Industry","large_sector_id":"L4_MATERIALS_SPREAD_RESOURCE","canonical_archetype_id":"C15_MATERIAL_SPREAD_SUPERCYCLE","fine_archetype_id":"COPPER_LAGGING_EFFECT_ROLL_MARGIN_GATE","trigger_type":"Stage2-Actionable","trigger_date":"2024-10-10","entry_date":"2024-10-11","entry_price":4780,"entry_ohlc":{"o":4905,"h":4965,"l":4765,"c":4780,"v":587923,"a":2865602515,"mc":159852760000,"s":33442000,"m":"KOSPI"},"MFE_30D_pct":6.49,"MAE_30D_pct":-22.18,"MFE_90D_pct":6.49,"MAE_90D_pct":-25.84,"MFE_180D_pct":26.78,"MAE_180D_pct":-25.84,"MFE_1Y_pct":28.66,"MAE_1Y_pct":-25.84,"MFE_2Y_pct":null,"MAE_2Y_pct":null,"peak_180D_date":"2025-03-26","peak_180D_price":6060,"trough_180D_date":"2024-12-09","trough_180D_price":3545,"drawdown_after_peak_pct":-35.4,"forward_window_trading_days":180,"price_source_validation":"stock_web_tradable_raw_1D_verified","tradable_shards":["atlas/ohlcv_tradable_by_symbol_year/025/025820/2024.csv","atlas/ohlcv_tradable_by_symbol_year/025/025820/2025.csv","atlas/ohlcv_tradable_by_symbol_year/025/025820/2026.csv"],"profile_contamination_check":"clean_by_tradable_shard_s_and_close_ratio","calibration_usable":true,"blocked_reason":null,"case_role":"lagging_positive_high_mae","residual_label":"lagging_effect_requires_cost_and_roll_margin_confirmation","dedupe_key":"C15_MATERIAL_SPREAD_SUPERCYCLE|025820|Stage2-Actionable|2024-10-11"}
{"row_type":"score_simulation","case_id":"C15-025820-20241010-STAGE2A","symbol":"025820","profile_proxy":"e2r_2_1_stock_web_calibrated_current_proxy","raw_component_scores":{"eps_fcf_explosion":7.0,"earnings_visibility":6.5,"bottleneck_pricing":6.5,"market_mispricing":5.5,"valuation_rerating":5.0,"capital_allocation":3.5,"information_confidence":6.5},"weighted_total_before_shadow":75.0,"stage_before_shadow":"Stage2-Actionable","weighted_total_after_shadow":71.0,"stage_after_shadow":"Stage2-Actionable","shadow_rule_applied":"C15_SPREAD_DURATION_AND_INVENTORY_GAIN_REVERSAL_GATE","production_scoring_changed":false,"alignment_note":"This is a delayed positive but not clean Green: 180D MFE eventually reached 26.78%, while interim MAE exceeded -25%."}
{"row_type":"aggregate","large_sector_id":"L4_MATERIALS_SPREAD_RESOURCE","canonical_archetype_id":"C15_MATERIAL_SPREAD_SUPERCYCLE","selected_round":"R4","selected_loop":191,"new_independent_case_count":8,"new_independent_trigger_count":8,"unique_symbol_count":7,"calibration_usable_case_count":8,"positive_case_count":3,"counterexample_or_guardrail_case_count":5,"source_proxy_only_count":0,"evidence_url_pending_count":0,"current_profile_error_count":6,"new_independent_ratio":1.0,"production_scoring_changed":false,"shadow_weight_only":true}
{"row_type":"shadow_weight","large_sector_id":"L4_MATERIALS_SPREAD_RESOURCE","canonical_archetype_id":"C15_MATERIAL_SPREAD_SUPERCYCLE","rule_candidate":"C15_SPREAD_DURATION_AND_INVENTORY_GAIN_REVERSAL_GATE","component_delta_candidate":{"bottleneck_pricing":-1.0,"earnings_visibility":-0.5,"valuation_rerating":-1.0,"information_confidence":0.5},"guardrail_candidate":{"spread_duration_required_for_stage3_yellow":true,"inventory_gain_green_blocker":true,"commodity_price_headline_requires_company_specific_volume_margin_bridge":true,"late_cycle_peak_proximity_sets_4B_watch":true},"production_scoring_changed":false,"shadow_weight_only":true}
{"row_type":"residual_contribution","large_sector_id":"L4_MATERIALS_SPREAD_RESOURCE","canonical_archetype_id":"C15_MATERIAL_SPREAD_SUPERCYCLE","residual_contribution_label":"material_spread_duration_and_inventory_gain_reversal_quality_repair","new_axis_proposed":false,"existing_axis_strengthened":["stage2_required_bridge","price_only_blowoff_blocks_positive_stage","full_4b_requires_non_price_evidence"],"existing_axis_refined":["hard_4c_confirmation_requires_duration_or_thesis_break_follow_through"],"existing_axis_weakened":[],"summary":"C15 spread headline works locally but frequently peaks before or soon after evidence; the residual is duration and company-specific margin bridge, not global threshold easing."}
```

## 8. Batch Ingest Self-Audit

```text
standard_v12_filename = pass
selected_round = R4
large_sector_id = L4_MATERIALS_SPREAD_RESOURCE
canonical_archetype_id = C15_MATERIAL_SPREAD_SUPERCYCLE
round_sector_consistency = pass
stock_web_manifest_checked = pass
stock_web_schema_checked = pass
actual_1D_OHLC_rows_used = pass
entry_ohlc_present_for_every_trigger = pass
MFE_30_90_180_present_for_every_trigger = pass
MAE_30_90_180_present_for_every_trigger = pass
same_entry_deduped = pass
hard_duplicate_detected_in_batch = false
corporate_action_180D_contamination = false
forward_180D_window_available = true
source_proxy_only_count = 0
evidence_url_pending_count = 0
production_scoring_changed = false
shadow_weight_only = true
handoff_prompt_embedded = true
handoff_prompt_executed_now = false
```

## 9. Deferred Coding Agent Handoff Prompt

```text
Do not execute in this research session.

When batch-applying v12 research artifacts later, parse this MD as a C15/L4 shadow-rule candidate only.
Do not loosen global Stage3-Yellow or Stage3-Green thresholds.
Do not change production scoring based on this single file.
Aggregate with other C15 trigger rows and confirm that the same failure mode persists:
- late-cycle spread evidence peaks quickly;
- inventory gains create false durability;
- copper/steel/oil headline price strength needs company-specific volume/margin bridge;
- local 4B watch is useful before full hard 4C.

Candidate patch name:
C15_SPREAD_DURATION_AND_INVENTORY_GAIN_REVERSAL_GATE

Patch scope:
large_sector_id = L4_MATERIALS_SPREAD_RESOURCE
canonical_archetype_id = C15_MATERIAL_SPREAD_SUPERCYCLE

Required tests:
- C15 positive controls must not be demoted if forward spread duration and stock-specific margin bridge are present.
- Inventory-gain-only refining and steel cases should be capped at Stage2-Actionable.
- Commodity headline without company bridge should not receive valuation_rerating expansion.
- 4B local watch must not become hard 4C without thesis-break confirmation.
```

## 10. Next Research State

```text
next_recommended_archetypes:
- C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE
- C02_POWER_GRID_DATACENTER_CAPEX
- C14_EV_DEMAND_SLOWDOWN_4B_4C
- C15_SPREAD_DURATION_POSITIVE_CONTROL_REPAIR
- R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL
```
