# E2R Stock-Web v12 Residual Research — R1/L1/C02 follow-up loop 119

```text
output_file = e2r_stock_web_v12_residual_round_R1_loop_119_L1_INDUSTRIALS_INFRA_DEFENSE_GRID_C02_POWER_GRID_DATACENTER_CAPEX_research.md
selected_round = R1
selected_loop = 119
large_sector_id = L1_INDUSTRIALS_INFRA_DEFENSE_GRID
canonical_archetype_id = C02_POWER_GRID_DATACENTER_CAPEX
fine_archetype_id = GRID_TRANSFORMER_DIRECT_ORDER_CAPACITY_EXPANSION_VS_SWITCHGEAR_PROXY_AND_IPO_PEAK
selection_basis = docs/core/V12_Research_No_Repeat_Index.md
selected_priority_bucket = Priority 0 / under_30_representative_rows / C02 static rows 10 need_to_30 20 need_to_50 40
round_schedule_status = coverage_index_selected
round_sector_consistency = pass
production_scoring_changed = false
shadow_weight_only = true
handoff_prompt_embedded = true
handoff_prompt_executed_now = false
```

## 0. Execution scope

This file is a standalone historical calibration / sector-archetype residual research artifact. It is **not** a live stock recommendation, not a stock_agent code patch, not an automated trading output, and not a production scoring change.

The selected axis is a C02 follow-up because the static No-Repeat Index still shows C02 as the lowest Priority 0 bucket. The immediately preceding C02 loop used transformer/power-grid names such as HD Hyundai Electric, Cheryong Electric, Hyosung Heavy Industries, PNC Technologies, and Daewon Cable. This loop therefore uses a new symbol set and a different evidence mix: direct transformer order/capa, data-center backup power, IPO peak, switchgear proxy, smart-grid proxy, and wrong-scope nuclear/power-equipment sympathy.

## 1. Price source validation

```jsonl
{"row_type":"price_source_validation","price_source":"Songdaiki/stock-web","source_name":"FinanceData/marcap","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","manifest_max_date":"2026-02-20","calibration_shard_root":"atlas/ohlcv_tradable_by_symbol_year","entry_price_basis":"close_c_column","mfe_mae_windows":"30/90/180 trading rows including entry row; high for MFE, low for MAE","corporate_action_policy":"raw/unadjusted windows with share-count discontinuity are blocked from representative aggregate."}
```

Stock-web rows used here are local materializations of `atlas/ohlcv_tradable_by_symbol_year/<prefix>/<symbol>/<year>.csv`. The entry price is the close `c` on `entry_date`, and MFE/MAE use the window high/low over 30, 90, and 180 trading rows from the entry row.

## 2. No-repeat and novelty check

```text
hard_duplicate_key = canonical_archetype_id + symbol + trigger_type + entry_date
prior_C02_symbols_avoided_from_static_index = 000500, 001440, 006260, 010120, 017510, 024840
prior_loop_118_symbols_avoided = 267260, 033100, 298040, 237750, 006340
this_loop_symbols = 103590, 119850, 062040, 017040, 388050, 189860, 006910, 199820
hard_duplicate_count = 0
new_independent_case_count = 7
narrative_only_blocked_count = 1
same_archetype_new_symbol_count = 8
same_archetype_new_trigger_family_count = 8
```

## 3. Case summary

| case | symbol | name | trigger | entry price | result | MFE30/MAE30 | MFE90/MAE90 | MFE180/MAE180 | calibration note |
|---|---:|---|---|---:|---|---:|---:|---:|---|
| C02_FU119_001 | 103590 | 일진전기 | Stage2-Actionable 2024-03-18 | 17200 | positive | 42.44/-9.48 | 75.87/-9.48 | 75.87/-9.48 | positive control: direct order + capa lock should score higher than generic power-equipment proxy. |
| C02_FU119_002 | 119850 | 지엔씨에너지 | Stage2-Actionable 2024-04-08 | 7540 | positive_with_local_4B_overlay | 51.72/-7.29 | 51.72/-34.95 | 51.72/-35.74 | positive control with profit-lock: direct data-center backup-power order bridge should pass Stage2, but fast reprice should cap Yellow/Green. |
| C02_FU119_003 | 062040 | 산일전기 | Stage2 2024-07-29 | 50200 | counterexample | 22.11/-44.12 | 37.85/-44.12 | 66.33/-44.12 | IPO/new-listing pure play needs lived-through order/revenue confirmation or staged entry; same-day IPO close should be local 4B/watch, not Yellow. |
| C02_FU119_004 | 017040 | 광명전기 | Stage2 2024-04-08 | 2715 | counterexample | 22.28/-13.26 | 22.28/-40.55 | 22.28/-53.96 | switchgear agreement/proxy should remain Stage2-watch unless customer order and margin bridge appear. |
| C02_FU119_005 | 388050 | 지투파워 | Stage2 2024-04-08 | 8860 | counterexample | 23.93/-12.30 | 43.79/-37.13 | 43.79/-44.02 | smart-grid vocabulary should not receive Actionable credit without contract/volume evidence. |
| C02_FU119_006 | 189860 | 서전기전 | Stage2 2024-07-17 | 6480 | counterexample | 27.62/-30.40 | 27.62/-38.19 | 27.62/-49.23 | day-after policy/project sympathy should be local 4B/proxy unless direct grid/datacenter order bridge exists. |
| C02_FU119_007 | 006910 | 보성파워텍 | Stage2 2024-07-17 | 3625 | counterexample | 18.07/-29.38 | 18.07/-29.38 | 18.07/-42.07 | wrong-scope power-infra proxy should be C04/C31 watch, not C02 Actionable. |
| C02_FU119_N01 | 199820 | 제일일렉트릭 | Stage2 2024-05-08 | 23800 | narrative_only_blocked | n/a | n/a | n/a | share_count_changed_11110000_to_22220000_on_2024-06-11_within_180D_raw_unadjusted_window |


## 4. Interpretation by case family

### 4.1 Direct transformer order + capacity bridge: raise C02 credit

Iljin Electric is the cleanest control in this loop. The key is not the word “power equipment”; it is the combination of **high-voltage transformer order, named export demand, production capacity expansion, and an actual price path that produced large MFE with limited MAE**. That is the shape C02 should reward.

### 4.2 Data-center backup power: eligible, but fast-reprice overlay required

GnC Energy is not a transformer manufacturer, but it is closer to C02 than a generic smart-grid theme because data-center emergency generation is part of the physical power stack. The price path says two things at once: it was tradable early, yet the 90D/180D MAE after a quick 30D move was large. This is a positive C02-adjacent case with local 4B/profit-lock overlay, not a blind Green unlock.

### 4.3 Pure-play IPO: structural theme can be right while entry is wrong

Sanil Electric is structurally a transformer/data-center power value-chain name, but the listing-day row is a bad calibration trigger. The same-day IPO close suffered a -44.12% MAE before later recovery. C02 needs an IPO/new-listing guard: pure-play fit can justify Stage2-watch, but Actionable/Yellow should wait for post-listing order, revenue, margin, or at least a second public reporting anchor.

### 4.4 Switchgear / smart-grid / power-equipment vocabulary: proxy guard

Kwang Myung Electric, G2Power, Seojeon Electric, and Bosung Powertec show the problem. Their products live near the grid, but the calibration question is whether the company has a **specific datacenter/grid CAPEX order bridge**. Without named customer/order/backlog/capa/ASP/margin evidence, the row belongs in Stage2-watch or local 4B, not Stage2-Actionable/Yellow.

### 4.5 Corporate-action contaminated row: block from aggregate

Cheil Electric is useful narratively as a breaker/smart-panel proxy, but the raw-unadjusted stock-web window has a share-count change from 11,110,000 to 22,220,000 on 2024-06-11 inside the 180D window. It is kept as narrative-only and blocked from representative aggregation.

## 5. Machine-readable trigger rows

```jsonl
{"row_type":"trigger","case_id":"C02_FU119_001","symbol":"103590","name":"일진전기","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C02_POWER_GRID_DATACENTER_CAPEX","fine_archetype_id":"GRID_TRANSFORMER_DIRECT_ORDER_CAPACITY_EXPANSION","trigger_type":"Stage2-Actionable","trigger_date":"2024-03-18","entry_date":"2024-03-18","entry_price":17200.0,"price_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","MFE_30D_pct":42.44,"MAE_30D_pct":-9.48,"MFE_90D_pct":75.87,"MAE_90D_pct":-9.48,"MFE_180D_pct":75.87,"MAE_180D_pct":-9.48,"peak_30D_date":"2024-04-05","trough_30D_date":"2024-03-18","peak_90D_date":"2024-05-29","trough_90D_date":"2024-03-18","peak_180D_date":"2024-05-29","trough_180D_date":"2024-03-18","positive_or_counterexample":"positive","calibration_usable":true,"representative_for_aggregate":true,"dedupe_key":"C02_POWER_GRID_DATACENTER_CAPEX|103590|Stage2-Actionable|2024-03-18","evidence_summary":"미국향 초고압 변압기 대형 수주와 생산능력 확장 자금조달/투자 논리가 함께 확인된 direct transformer order+capa bridge.","source_url":"https://transformer-magazine.com/news/iljin-electrics-333-m-high-voltage-transformer-deal-in-us/","current_profile_verdict":"profile_can_capture_stage2_actionable_but_underweights_capacity_lock","residual_contribution":"positive control: direct order + capa lock should score higher than generic power-equipment proxy."}
{"row_type":"trigger","case_id":"C02_FU119_002","symbol":"119850","name":"지엔씨에너지","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C02_POWER_GRID_DATACENTER_CAPEX","fine_archetype_id":"DATA_CENTER_BACKUP_POWER_GENERATOR_ORDER_TO_MARGIN","trigger_type":"Stage2-Actionable","trigger_date":"2024-04-08","entry_date":"2024-04-08","entry_price":7540.0,"price_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","MFE_30D_pct":51.72,"MAE_30D_pct":-7.29,"MFE_90D_pct":51.72,"MAE_90D_pct":-34.95,"MFE_180D_pct":51.72,"MAE_180D_pct":-35.74,"peak_30D_date":"2024-05-16","trough_30D_date":"2024-04-23","peak_90D_date":"2024-05-16","trough_90D_date":"2024-08-05","peak_180D_date":"2024-05-16","trough_180D_date":"2024-10-31","positive_or_counterexample":"positive_with_local_4B_overlay","calibration_usable":true,"representative_for_aggregate":true,"dedupe_key":"C02_POWER_GRID_DATACENTER_CAPEX|119850|Stage2-Actionable|2024-04-08","evidence_summary":"데이터센터 비상발전기 수요가 매출/수주잔고로 이어지는 adjacent-but-direct datacenter power CAPEX case. 다만 30D 급등 후 90D/180D MAE가 커서 local 4B가 필요.","source_url":"https://www.electimes.com/news/articleView.html?idxno=355058","current_profile_verdict":"profile_likely_too_binary_between_positive_stage_and_full_4B","residual_contribution":"positive control with profit-lock: direct data-center backup-power order bridge should pass Stage2, but fast reprice should cap Yellow/Green."}
{"row_type":"trigger","case_id":"C02_FU119_003","symbol":"062040","name":"산일전기","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C02_POWER_GRID_DATACENTER_CAPEX","fine_archetype_id":"TRANSFORMER_PURE_PLAY_IPO_PEAK_GUARD","trigger_type":"Stage2","trigger_date":"2024-07-29","entry_date":"2024-07-29","entry_price":50200.0,"price_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","MFE_30D_pct":22.11,"MAE_30D_pct":-44.12,"MFE_90D_pct":37.85,"MAE_90D_pct":-44.12,"MFE_180D_pct":66.33,"MAE_180D_pct":-44.12,"peak_30D_date":"2024-07-30","trough_30D_date":"2024-09-09","peak_90D_date":"2024-11-12","trough_90D_date":"2024-09-09","peak_180D_date":"2025-01-15","trough_180D_date":"2024-09-09","positive_or_counterexample":"counterexample","calibration_usable":true,"representative_for_aggregate":true,"dedupe_key":"C02_POWER_GRID_DATACENTER_CAPEX|062040|Stage2|2024-07-29","evidence_summary":"특수변압기·데이터센터 공급 narrative가 맞더라도 IPO 첫날 entry는 liquidity/valuation peak risk가 커서 clean Actionable이 아님.","source_url":"https://www.yna.co.kr/view/AKR20240729036251008","current_profile_verdict":"profile_may_overcredit_pure_play_without_public_trading_history","residual_contribution":"IPO/new-listing pure play needs lived-through order/revenue confirmation or staged entry; same-day IPO close should be local 4B/watch, not Yellow."}
{"row_type":"trigger","case_id":"C02_FU119_004","symbol":"017040","name":"광명전기","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C02_POWER_GRID_DATACENTER_CAPEX","fine_archetype_id":"SWITCHGEAR_TECH_AGREEMENT_PROXY_GUARD","trigger_type":"Stage2","trigger_date":"2024-04-08","entry_date":"2024-04-08","entry_price":2715.0,"price_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","MFE_30D_pct":22.28,"MAE_30D_pct":-13.26,"MFE_90D_pct":22.28,"MAE_90D_pct":-40.55,"MFE_180D_pct":22.28,"MAE_180D_pct":-53.96,"peak_30D_date":"2024-05-08","trough_30D_date":"2024-05-23","peak_90D_date":"2024-05-08","trough_90D_date":"2024-08-05","peak_180D_date":"2024-05-08","trough_180D_date":"2024-10-31","positive_or_counterexample":"counterexample","calibration_usable":true,"representative_for_aggregate":true,"dedupe_key":"C02_POWER_GRID_DATACENTER_CAPEX|017040|Stage2|2024-04-08","evidence_summary":"수배전반/Eaton 협약/AI 전력수요 proxy는 제품 인접성은 있으나 named order, backlog, capacity, margin bridge가 부족.","source_url":"https://kr.investing.com/news/stock-market-news/article-1037427","current_profile_verdict":"profile_too_generous_to_switchgear_proxy_if_stage2_bridge_not_required","residual_contribution":"switchgear agreement/proxy should remain Stage2-watch unless customer order and margin bridge appear."}
{"row_type":"trigger","case_id":"C02_FU119_005","symbol":"388050","name":"지투파워","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C02_POWER_GRID_DATACENTER_CAPEX","fine_archetype_id":"SMART_SWITCHGEAR_MONITORING_PROXY_HIGH_MAE","trigger_type":"Stage2","trigger_date":"2024-04-08","entry_date":"2024-04-08","entry_price":8860.0,"price_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","MFE_30D_pct":23.93,"MAE_30D_pct":-12.3,"MFE_90D_pct":43.79,"MAE_90D_pct":-37.13,"MFE_180D_pct":43.79,"MAE_180D_pct":-44.02,"peak_30D_date":"2024-05-22","trough_30D_date":"2024-04-12","peak_90D_date":"2024-05-29","trough_90D_date":"2024-08-05","peak_180D_date":"2024-05-29","trough_180D_date":"2024-10-04","positive_or_counterexample":"counterexample","calibration_usable":true,"representative_for_aggregate":true,"dedupe_key":"C02_POWER_GRID_DATACENTER_CAPEX|388050|Stage2|2024-04-08","evidence_summary":"스마트 수배전반/상태감시진단은 C02 vocabulary와 맞지만 customer order/backlog/capa bridge 부재 시 high-MAE proxy.","source_url":"https://www.g2p.co.kr/company/about.html","current_profile_verdict":"profile_should_split_smart_grid_vocabulary_from_confirmed_datacenter_order","residual_contribution":"smart-grid vocabulary should not receive Actionable credit without contract/volume evidence."}
{"row_type":"trigger","case_id":"C02_FU119_006","symbol":"189860","name":"서전기전","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C02_POWER_GRID_DATACENTER_CAPEX","fine_archetype_id":"SWITCHGEAR_NUCLEAR_GRID_PROXY_HIGH_MAE","trigger_type":"Stage2","trigger_date":"2024-07-17","entry_date":"2024-07-17","entry_price":6480.0,"price_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","MFE_30D_pct":27.62,"MAE_30D_pct":-30.4,"MFE_90D_pct":27.62,"MAE_90D_pct":-38.19,"MFE_180D_pct":27.62,"MAE_180D_pct":-49.23,"peak_30D_date":"2024-07-18","trough_30D_date":"2024-08-05","peak_90D_date":"2024-07-18","trough_90D_date":"2024-10-11","peak_180D_date":"2024-07-18","trough_180D_date":"2024-12-09","positive_or_counterexample":"counterexample","calibration_usable":true,"representative_for_aggregate":true,"dedupe_key":"C02_POWER_GRID_DATACENTER_CAPEX|189860|Stage2|2024-07-17","evidence_summary":"수배전반·GIS·전력IT 제품은 확인되지만, Czech nuclear/day-after broad power-equipment sympathy는 C04/C31 proxy와 섞여 C02 direct bridge가 약함.","source_url":"https://sjem.co.kr/","current_profile_verdict":"profile_may_misclassify_power_equipment_sympathy_as_C02","residual_contribution":"day-after policy/project sympathy should be local 4B/proxy unless direct grid/datacenter order bridge exists."}
{"row_type":"trigger","case_id":"C02_FU119_007","symbol":"006910","name":"보성파워텍","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C02_POWER_GRID_DATACENTER_CAPEX","fine_archetype_id":"POWER_INFRA_NUCLEAR_PROXY_SCOPE_GUARD","trigger_type":"Stage2","trigger_date":"2024-07-17","entry_date":"2024-07-17","entry_price":3625.0,"price_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","MFE_30D_pct":18.07,"MAE_30D_pct":-29.38,"MFE_90D_pct":18.07,"MAE_90D_pct":-29.38,"MFE_180D_pct":18.07,"MAE_180D_pct":-42.07,"peak_30D_date":"2024-07-18","trough_30D_date":"2024-08-05","peak_90D_date":"2024-07-18","trough_90D_date":"2024-08-05","peak_180D_date":"2024-07-18","trough_180D_date":"2025-04-04","positive_or_counterexample":"counterexample","calibration_usable":true,"representative_for_aggregate":true,"dedupe_key":"C02_POWER_GRID_DATACENTER_CAPEX|006910|Stage2|2024-07-17","evidence_summary":"전력기자재/송배전/원전 인프라 wording은 C02와 일부 겹치지만, day-after Czech/nuclear proxy는 datacenter/grid CAPEX order bridge가 아니라 scope guardrail.","source_url":"https://www.bosungpower.co.kr/company/intro.do","current_profile_verdict":"profile_needs_scope_guard_between_C02_grid_capex_and_C04_nuclear_policy","residual_contribution":"wrong-scope power-infra proxy should be C04/C31 watch, not C02 Actionable."}
```

## 6. Narrative-only / blocked row

```jsonl
{"row_type":"narrative_only","case_id":"C02_FU119_N01","symbol":"199820","name":"제일일렉트릭","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C02_POWER_GRID_DATACENTER_CAPEX","fine_archetype_id":"BREAKER_SMART_PANEL_PROXY_BLOCKED_CORPORATE_ACTION","trigger_type":"Stage2","trigger_date":"2024-05-08","entry_date":"2024-05-08","entry_price":23800.0,"price_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","calibration_usable":false,"representative_for_aggregate":false,"blocked_reason":"share_count_changed_11110000_to_22220000_on_2024-06-11_within_180D_raw_unadjusted_window","source_url":"https://www.cheilelec.com/","evidence_summary":"차단기/스마트분전반 제품 proxy는 유용하지만 stock-web raw-unadjusted 180D window 안에 share-count discontinuity가 있어 대표 가격 row로 쓰지 않는다."}
```

## 7. Score simulation rows

```jsonl
{"row_type":"score_simulation","case_id":"C02_FU119_001","symbol":"103590","trigger_type":"Stage2-Actionable","raw_component_score_breakdown":{"eps_fcf_visibility":68,"earnings_revision":62,"bottleneck_pricing":82,"mispricing":58,"rerating_duration":60,"capital_allocation":45,"information_confidence":72},"simulated_current_profile_total":63.86,"simulated_profile_verdict":"Stage2-Actionable candidate; Yellow only if follow-up margin/cash bridge survives fast reprice.","calibration_note":"positive control: direct order + capa lock should score higher than generic power-equipment proxy."}
{"row_type":"score_simulation","case_id":"C02_FU119_002","symbol":"119850","trigger_type":"Stage2-Actionable","raw_component_score_breakdown":{"eps_fcf_visibility":68,"earnings_revision":62,"bottleneck_pricing":82,"mispricing":58,"rerating_duration":60,"capital_allocation":45,"information_confidence":72},"simulated_current_profile_total":63.86,"simulated_profile_verdict":"Stage2-Actionable candidate; Yellow only if follow-up margin/cash bridge survives fast reprice.","calibration_note":"positive control with profit-lock: direct data-center backup-power order bridge should pass Stage2, but fast reprice should cap Yellow/Green."}
{"row_type":"score_simulation","case_id":"C02_FU119_003","symbol":"062040","trigger_type":"Stage2","raw_component_score_breakdown":{"eps_fcf_visibility":35,"earnings_revision":30,"bottleneck_pricing":55,"mispricing":40,"rerating_duration":32,"capital_allocation":35,"information_confidence":46},"simulated_current_profile_total":39.0,"simulated_profile_verdict":"Stage2-watch or local 4B; do not upgrade to Actionable/Yellow without direct order/capa/margin bridge.","calibration_note":"IPO/new-listing pure play needs lived-through order/revenue confirmation or staged entry; same-day IPO close should be local 4B/watch, not Yellow."}
{"row_type":"score_simulation","case_id":"C02_FU119_004","symbol":"017040","trigger_type":"Stage2","raw_component_score_breakdown":{"eps_fcf_visibility":35,"earnings_revision":30,"bottleneck_pricing":55,"mispricing":40,"rerating_duration":32,"capital_allocation":35,"information_confidence":46},"simulated_current_profile_total":39.0,"simulated_profile_verdict":"Stage2-watch or local 4B; do not upgrade to Actionable/Yellow without direct order/capa/margin bridge.","calibration_note":"switchgear agreement/proxy should remain Stage2-watch unless customer order and margin bridge appear."}
{"row_type":"score_simulation","case_id":"C02_FU119_005","symbol":"388050","trigger_type":"Stage2","raw_component_score_breakdown":{"eps_fcf_visibility":35,"earnings_revision":30,"bottleneck_pricing":55,"mispricing":40,"rerating_duration":32,"capital_allocation":35,"information_confidence":46},"simulated_current_profile_total":39.0,"simulated_profile_verdict":"Stage2-watch or local 4B; do not upgrade to Actionable/Yellow without direct order/capa/margin bridge.","calibration_note":"smart-grid vocabulary should not receive Actionable credit without contract/volume evidence."}
{"row_type":"score_simulation","case_id":"C02_FU119_006","symbol":"189860","trigger_type":"Stage2","raw_component_score_breakdown":{"eps_fcf_visibility":35,"earnings_revision":30,"bottleneck_pricing":55,"mispricing":40,"rerating_duration":32,"capital_allocation":35,"information_confidence":46},"simulated_current_profile_total":39.0,"simulated_profile_verdict":"Stage2-watch or local 4B; do not upgrade to Actionable/Yellow without direct order/capa/margin bridge.","calibration_note":"day-after policy/project sympathy should be local 4B/proxy unless direct grid/datacenter order bridge exists."}
{"row_type":"score_simulation","case_id":"C02_FU119_007","symbol":"006910","trigger_type":"Stage2","raw_component_score_breakdown":{"eps_fcf_visibility":35,"earnings_revision":30,"bottleneck_pricing":55,"mispricing":40,"rerating_duration":32,"capital_allocation":35,"information_confidence":46},"simulated_current_profile_total":39.0,"simulated_profile_verdict":"Stage2-watch or local 4B; do not upgrade to Actionable/Yellow without direct order/capa/margin bridge.","calibration_note":"wrong-scope power-infra proxy should be C04/C31 watch, not C02 Actionable."}
```

## 8. Aggregate / shadow-weight / residual rows

```jsonl
{"row_type":"aggregate","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C02_POWER_GRID_DATACENTER_CAPEX","selected_round":"R1","selected_loop":119,"usable_trigger_rows":7,"representative_trigger_rows":7,"narrative_only_blocked_rows":1,"positive_case_count":2,"counterexample_count":5,"stage4b_overlay_count":5,"stage4c_case_count":0,"new_symbol_count":8,"same_archetype_new_symbol_count":8,"same_archetype_new_trigger_family_count":8,"hard_duplicate_count":0,"estimated_post_commit_representative_rows_for_C02":"static_index_10 + prior_loop_118_estimated_5 + this_loop_119_estimated_7 = 22","estimated_need_to_30_after_commit":8,"residual_error_summary":"C02 still needs direct order/capa bridge weighting and stricter proxy/IPO/adjacent-theme gates."}
{"row_type":"shadow_weight_change_candidate","axis":"C02_DIRECT_TRANSFORMER_ORDER_CAPA_LOCK_GATE_WITH_IPO_AND_SWITCHGEAR_PROXY_GUARD","production_scoring_changed":false,"shadow_weight_only":true,"direction":"increase bridge credit for direct transformer/grid/datacenter orders; decrease credit for switchgear/nuclear/power-equipment proxy without named customer/order/backlog; add IPO same-day peak guard","suggested_effect":"Stage2-Actionable requires named customer/order/backlog/capa or revenue/margin conversion; Stage3-Yellow blocked if only product vocabulary, peer-comp IPO, or broad policy sympathy."}
{"row_type":"residual_contribution","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C02_POWER_GRID_DATACENTER_CAPEX","residual_label":"C02 bridge-vs-proxy split","main_error_modes":["pure_play_IPO_same_day_entry_overcredit","switchgear_or_smart_grid_vocabulary_proxy","wrong_scope_power_or_nuclear_sympathy","fast_reprice_without_new_order_follow_through"],"recommended_guardrail":"Local 4B after fast reprice or high-MAE path; require direct order/capa/margin bridge before Actionable/Yellow."}
```

## 9. Proposed shadow rule

```text
C02_DIRECT_TRANSFORMER_ORDER_CAPA_LOCK_GATE_WITH_IPO_AND_SWITCHGEAR_PROXY_GUARD

Increase C02 credit only when at least one hard bridge exists:
- named grid/datacenter customer or utility order;
- transformer / high-voltage / power conversion backlog;
- CAPA lock, lead-time tightness, ASP or margin bridge;
- data-center physical power-stack revenue/order bridge;
- recurring revenue or shipment conversion visible after the trigger.

Block Actionable/Yellow when evidence is only:
- same-day IPO pure-play valuation;
- switchgear/breaker/smart-panel product vocabulary;
- generic AI/data-center power demand wording;
- nuclear/policy sympathy without company-specific grid/datacenter order;
- peer-comp re-rating without revenue/margin conversion.

Add local 4B/profit-lock overlay when:
- MFE30 exceeds roughly +25~35% but no new non-price bridge appears;
- 90D or 180D MAE exceeds -30%;
- the trigger is a late headline after the price already repriced.
```

## 10. Deferred Coding Agent Handoff Prompt

```text
Do not execute in this research session.

When batch-applying v12 residual research artifacts later, ingest this MD as a standard v12 result file. Parse the JSONL trigger rows and aggregate rows. Treat C02_DIRECT_TRANSFORMER_ORDER_CAPA_LOCK_GATE_WITH_IPO_AND_SWITCHGEAR_PROXY_GUARD as a shadow candidate only. Do not change production scoring unless the batch calibration pipeline promotes the axis after dedupe, validation, and promotion decision review. Ensure narrative-only row C02_FU119_N01 remains blocked from representative price aggregation because the 180D raw-unadjusted window contains a share-count discontinuity.
```

## 11. Next research state

```text
completed_round = R1
completed_loop = 119
selection_basis = docs/core/V12_Research_No_Repeat_Index.md
selected_priority_bucket = Priority 0 / C02_POWER_GRID_DATACENTER_CAPEX static rows 10; prior loop_118 estimated +5; this loop_119 estimated +7 representative rows; estimated need_to_30 after commit = 8
next_recommended_archetypes = C02_POWER_GRID_DATACENTER_CAPEX_followup_new_symbols_only, C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF_followup_after_shard_recheck, C14_EV_DEMAND_SLOWDOWN_4B_4C_followup_utilization_regime, C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE_followup_counterexample, R13_CROSS_ARCHETYPE_ACCOUNTING_TRUST_PRICE_VALIDATION_if_source_proxy_repair_needed
round_schedule_status = coverage_index_selected
round_sector_consistency = pass
```

## 12. Source notes

```text
MAIN_EXECUTION_PROMPT = https://raw.githubusercontent.com/Songdaiki/stock_agent/main/docs/core/e2r_v12_prompt_round_scheduler_corrected.txt
NO_REPEAT_INDEX = https://raw.githubusercontent.com/Songdaiki/stock_agent/main/docs/core/V12_Research_No_Repeat_Index.md
STOCK_WEB_MANIFEST = https://raw.githubusercontent.com/Songdaiki/stock-web/main/atlas/manifest.json
ILJIN_ORDER_SOURCE = https://transformer-magazine.com/news/iljin-electrics-333-m-high-voltage-transformer-deal-in-us/
SANIL_IPO_SOURCE = https://www.yna.co.kr/view/AKR20240729036251008
GNC_ENERGY_SOURCE = https://www.electimes.com/news/articleView.html?idxno=355058
KWANGMYUNG_PROXY_SOURCE = https://kr.investing.com/news/stock-market-news/article-1037427
G2POWER_PRODUCT_SOURCE = https://www.g2p.co.kr/company/about.html
SEOJEON_PRODUCT_SOURCE = https://sjem.co.kr/
BOSUNG_PRODUCT_SOURCE = https://www.bosungpower.co.kr/company/intro.do
CHEIL_PRODUCT_SOURCE = https://www.cheilelec.com/
```
