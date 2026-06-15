# E2R v12 Historical Calibration Research — R3 / C11 Battery Orderbook Rerating / loop 141

```yaml
mode: historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12
research_session: post_calibrated_sector_archetype_residual_research
stock_agent_code_patch_allowed: false
production_scoring_changed: false
shadow_weight_only: true
handoff_prompt_executed_now: false
selected_round: R3
selected_loop: 141
large_sector_id: L3_BATTERY_EV_GREEN_MOBILITY
canonical_archetype_id: C11_BATTERY_ORDERBOOK_RERATING
fine_archetype_id: mixed_c11_orderbook_quality_revenue_timing_leaf_set
selection_basis: docs/core/V12_Research_No_Repeat_Index.md
selected_priority_bucket: Priority 0
round_schedule_status: coverage_index_selected_not_sequential
round_sector_consistency: pass
price_data_source: Songdaiki/stock-web
price_basis: tradable_raw
price_adjustment_status: raw_unadjusted_marcap
stock_web_manifest_max_date: 2026-02-20
output_filename: e2r_stock_web_v12_residual_round_R3_loop_141_L3_BATTERY_EV_GREEN_MOBILITY_C11_BATTERY_ORDERBOOK_RERATING_research.md
```

## 1. Selection / no-repeat rationale

`V12_Research_No_Repeat_Index.md` lists `C11_BATTERY_ORDERBOOK_RERATING` as Priority 0 with 18 representative rows, 12 rows short of the 30-row minimum stability zone. This session already added one C11 pass at loop 131 using 코윈테크, 윤성에프앤씨, 원익피앤이, 하나기술, and 티에스아이. This loop deliberately avoids that set and uses six new symbols / trigger families: 포스코퓨처엠, 에코프로비엠, 피엔티, 씨아이에스, 필에너지, and 엠플러스.

The research question is not whether “orderbook is good.” The actual residual is sharper: **when does a battery orderbook headline have enough customer/order/revenue/margin bridge to deserve Stage2-Actionable, and when is it only a backlog/mega-contract headline that should be capped at Stage2-Watch or local 4B-Watch?**

## 2. Price atlas validation

- primary price source: `Songdaiki/stock-web`
- calibration shard root: `atlas/ohlcv_tradable_by_symbol_year`
- basis: `tradable_raw`
- adjustment status: `raw_unadjusted_marcap`
- MFE/MAE formula: max high / min low from entry row through N tradable rows versus entry close.
- all six usable rows have complete 30D/90D/180D MFE and MAE.
- no selected entry → D+180 window overlaps the corporate-action candidate dates listed in each stock-web symbol profile.

## 3. Case summary

| case_id | symbol/name | trigger | entry | MFE/MAE 30D | MFE/MAE 90D | MFE/MAE 180D | outcome | residual |
|---|---|---:|---:|---:|---:|---:|---|---|
| C11_L141_01_POSCO_FUTURE_M_20230130_SDI_40T | 003670 포스코퓨처엠 | 2023-01-30 | 2023-01-31 @ 224000 | 20.54/-5.58 | 88.62/-5.58 | 209.82/-5.58 | positive | missed_structural_magnitude_if_contract_bridge_underweighted |
| C11_L141_02_ECOPROBM_20231201_SDI_44T | 247540 에코프로비엠 | 2023-12-01 | 2023-12-04 @ 323000 | 9.6/-17.96 | 9.6/-34.67 | 9.6/-49.23 | counterexample | mega_contract_overweighted_without_margin_and_entry_guard |
| C11_L141_03_PNT_20240416_ELECTRODE_EQUIPMENT_CONTRACT | 137400 피엔티 | 2024-04-16 | 2024-04-17 @ 38650 | 74.39/-1.55 | 131.57/-1.55 | 131.57/-5.3 | positive | signed_order_quality_correctly_leads_price_but_requires_4b_exit_after_peak |
| C11_L141_04_CIS_20240327_BACKLOG_EXPECTATION | 222080 씨아이에스 | 2024-03-27 | 2024-03-28 @ 13160 | 1.82/-21.5 | 1.82/-40.73 | 1.82/-46.43 | counterexample | backlog_count_without_conversion_timing_false_positive |
| C11_L141_05_PHILENERGY_20231117_ADVANCED_STACKER_ORDER | 378340 필에너지 | 2023-11-17 | 2023-11-20 @ 19160 | 6.21/-11.27 | 86.33/-13.88 | 86.33/-38.0 | positive_with_4B_overlay | positive_orderbook_but_exit_guard_missing |
| C11_L141_06_MPLUS_20230817_BACKLOG_3X_SALES | 259630 엠플러스 | 2023-08-17 | 2023-08-18 @ 14950 | 33.78/-11.04 | 33.78/-28.56 | 33.78/-35.72 | counterexample | backlog_size_without_customer_capex_followthrough_false_positive |


## 4. Evidence ledger

| case_id | evidence summary | evidence URLs | source_proxy_only | profile CA check |
|---|---|---|---:|---|
| C11_L141_01_POSCO_FUTURE_M_20230130_SDI_40T | Samsung SDI와 2023~2032년 10년, 40조원 규모 high-nickel NCA 양극재 공급계약. 단순 테마가 아니라 명명 고객·계약기간·계약금액이 모두 확인된 hard orderbook bridge. | https://www.poscofuturem.com/en/pr/view.do?num=658 | false | profile CA dates=2015-05-04, 2021-02-03; 180D window contaminated=false |
| C11_L141_02_ECOPROBM_20231201_SDI_44T | 삼성SDI와 2024~2028년 5년, 약 44조원 high-nickel NCA 양극재 공급계약. 계약 규모는 거대했지만 entry는 이미 당일 급등 후였고, EV/양극재 ASP 하락 국면에서 margin/revision bridge가 약했다. | https://ecoprobm.com/sub0701/view/page/1/id/1385 | false | profile CA dates=2022-06-27, 2022-07-15; 180D window contaminated=false |
| C11_L141_03_PNT_20240416_ELECTRODE_EQUIPMENT_CONTRACT | 660억3800만원 2차전지 전극공정 장비 공급계약. 2023년 매출 대비 12.1%로 금액이 작지 않고 계약기간도 2025-11-17까지 명시되어 order-to-revenue bridge가 확인된다. | https://www.edaily.co.kr/News/Read?mediaCodeNo=257&newsId=02915926638856776 | false | profile CA dates=2012-11-30, 2012-12-26, 2019-05-07, 2019-05-30; 180D window contaminated=false |
| C11_L141_04_CIS_20240327_BACKLOG_EXPECTATION | 2023년 신규수주와 고객 협의 물량으로 수주잔고 1조원 기대가 있었지만, 장비업 특성상 긴 리드타임·매출 인식 지연·낮은 OPM 변수가 같이 존재했다. | https://m.thebell.co.kr/m/newsview.asp?newskey=202403080901104280101912&svccode=<br>https://securities.miraeasset.com/bbs/download/2119745.pdf?attachmentId=2119745 | true | profile CA dates=2017-01-20; 180D window contaminated=false |
| C11_L141_05_PHILENERGY_20231117_ADVANCED_STACKER_ORDER | 998억원 규모 단일판매·공급계약과 3000억원 돌파 수주잔고. 기존 고객사의 미국 JV 라인 공급으로 추정되어 orderbook-to-revenue bridge는 있었지만, 90D 이후 drawdown이 커 4B overlay가 필요했다. | https://www.hanaw.com/download/research/FileServer/WEB/info/small_cap/2023/11/17/231120_philenergy.pdf | true | profile CA dates=2023-09-27, 2023-10-23; 180D window contaminated=false |
| C11_L141_06_MPLUS_20230817_BACKLOG_3X_SALES | 조립공정 turn-key 수주 가능성과 작년 매출액 3배 수준 수주잔고, 신규수주 급성장 narrative. 그러나 가격경로는 초반 MFE 후 90D/180D drawdown이 커 매출 인식과 고객 capex cycle 검증이 부족했다. | https://www.hanaw.com/download/research/FileServer/WEB/info/small_cap/2023/08/16/230817_mplus.pdf | true | profile CA dates=2020-09-23, 2020-10-19; 180D window contaminated=false |


## 5. Interpretation by case

### 5.1 POSCO Future M / 003670 / positive structural orderbook

The 2023-01-30 Samsung SDI cathode contract had all three features C11 wants: named customer, stated amount/period, and direct product linkage. The path was clean: entry close 224,000, 90D MFE +88.62%, 180D MFE +209.82%, with 180D MAE only -5.58%. This is the clean positive prototype for C11.

### 5.2 EcoPro BM / 247540 / mega-contract false positive

The 2023-12-01 Samsung SDI contract was even larger on paper, but the entry came after a sharp contract-day rerating and the cycle backdrop was worse. MFE never exceeded +9.60% over the 180D window while MAE reached -49.23%. C11 therefore needs a mega-contract entry guard: contract size alone must not outrank ASP/margin/revision and entry-location risk.

### 5.3 PNT / 137400 / signed equipment order positive with exit discipline

The 2024-04-16 electrode-process equipment contract was smaller than the cathode mega-contracts but cleaner as a trigger: contract amount was 12.1% of prior-year revenue and delivery period was visible. The price path delivered +74.39% MFE by 30D and +131.57% by 90D with only -1.55% MAE through 90D. The 180D close faded back near entry, so the rule should preserve Stage2-Actionable while adding a local 4B/staged-exit guard after the orderbook-led price oxygen is consumed.

### 5.4 CIS / 222080 / backlog count without conversion timing

CIS had a credible backlog story, but the exact residual is revenue-recognition lag. From the 2024-03-27 trigger, 90D MFE was only +1.82% while 90D MAE was -40.73% and 180D MAE was -46.43%. The evidence was not fake; the timing bridge was insufficient. Current profile should avoid treating backlog quantity as equal to near-term revenue/margin conversion.

### 5.5 Philenergy / 378340 / real orderbook but 4B overlay required

Philenergy had a concrete 99.8bn won contract and reported backlog above 300bn won. The row worked strongly through 90D, with +86.33% MFE, but then rolled down to -38.00% MAE by 180D. This is not a simple false positive. It is a C11 positive that requires a local 4B-Watch after the 90D price peak if later conversion is delayed.

### 5.6 mPLUS / 259630 / backlog headline peak reversal

mPLUS had a strong turn-key/backlog narrative, but price behavior shows why C11 cannot stop at backlog/sales ratio. The row had +33.78% MFE in the first 30D but fell to -28.56% MAE by 90D and -35.72% by 180D. The correct profile action is not Green unlock; it is Stage2-Watch or local 4B-Watch until customer capex follow-through and margin conversion are visible.

## 6. Machine-readable trigger rows JSONL

```jsonl
{"row_type":"trigger","case_id":"C11_L141_01_POSCO_FUTURE_M_20230130_SDI_40T","symbol":"003670","name":"포스코퓨처엠","round":"R3","loop":141,"large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C11_BATTERY_ORDERBOOK_RERATING","fine_archetype_id":"CATHODE_LONG_TERM_SUPPLY_ORDERBOOK_MARGIN_BRIDGE","trigger_date":"2023-01-30","trigger_type":"Stage2-Actionable","entry_rule":"next_trading_day_close","entry_date":"2023-01-31","entry_price":224000.0,"MFE_30D_pct":20.54,"MAE_30D_pct":-5.58,"MFE_90D_pct":88.62,"MAE_90D_pct":-5.58,"MFE_180D_pct":209.82,"MAE_180D_pct":-5.58,"end_30D":"2023-03-14","end_90D":"2023-06-12","end_180D":"2023-10-24","peak_180D_date":"2023-07-26","trough_180D_date":"2023-02-23","outcome_label":"positive","calibration_usable":true,"corporate_action_window_180D_contaminated":false,"price_data_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","evidence_urls":["https://www.poscofuturem.com/en/pr/view.do?num=658"],"source_proxy_only":false,"current_profile_error":false,"expected_current_stage":"Stage2-Actionable","suggested_stage":"Stage3-Yellow","residual_label":"missed_structural_magnitude_if_contract_bridge_underweighted"}
{"row_type":"trigger","case_id":"C11_L141_02_ECOPROBM_20231201_SDI_44T","symbol":"247540","name":"에코프로비엠","round":"R3","loop":141,"large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C11_BATTERY_ORDERBOOK_RERATING","fine_archetype_id":"CATHODE_MEGA_CONTRACT_ASP_DOWNTURN_FALSE_POSITIVE","trigger_date":"2023-12-01","trigger_type":"Stage2-FalsePositiveReview","entry_rule":"next_trading_day_close","entry_date":"2023-12-04","entry_price":323000.0,"MFE_30D_pct":9.6,"MAE_30D_pct":-17.96,"MFE_90D_pct":9.6,"MAE_90D_pct":-34.67,"MFE_180D_pct":9.6,"MAE_180D_pct":-49.23,"end_30D":"2024-01-17","end_90D":"2024-04-16","end_180D":"2024-08-27","peak_180D_date":"2023-12-04","trough_180D_date":"2024-08-05","outcome_label":"counterexample","calibration_usable":true,"corporate_action_window_180D_contaminated":false,"price_data_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","evidence_urls":["https://ecoprobm.com/sub0701/view/page/1/id/1385"],"source_proxy_only":false,"current_profile_error":true,"expected_current_stage":"Stage2-Actionable","suggested_stage":"Stage2-Watch_or_4B-Watch","residual_label":"mega_contract_overweighted_without_margin_and_entry_guard"}
{"row_type":"trigger","case_id":"C11_L141_03_PNT_20240416_ELECTRODE_EQUIPMENT_CONTRACT","symbol":"137400","name":"피엔티","round":"R3","loop":141,"large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C11_BATTERY_ORDERBOOK_RERATING","fine_archetype_id":"BATTERY_EQUIPMENT_SIGNED_ORDER_REVENUE_TIMING","trigger_date":"2024-04-16","trigger_type":"Stage2-Actionable","entry_rule":"next_trading_day_close","entry_date":"2024-04-17","entry_price":38650.0,"MFE_30D_pct":74.39,"MAE_30D_pct":-1.55,"MFE_90D_pct":131.57,"MAE_90D_pct":-1.55,"MFE_180D_pct":131.57,"MAE_180D_pct":-5.3,"end_30D":"2024-05-31","end_90D":"2024-08-27","end_180D":"2025-01-13","peak_180D_date":"2024-06-19","trough_180D_date":"2024-12-30","outcome_label":"positive","calibration_usable":true,"corporate_action_window_180D_contaminated":false,"price_data_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","evidence_urls":["https://www.edaily.co.kr/News/Read?mediaCodeNo=257&newsId=02915926638856776"],"source_proxy_only":false,"current_profile_error":false,"expected_current_stage":"Stage2-Actionable","suggested_stage":"Stage3-Yellow_with_staged_exit","residual_label":"signed_order_quality_correctly_leads_price_but_requires_4b_exit_after_peak"}
{"row_type":"trigger","case_id":"C11_L141_04_CIS_20240327_BACKLOG_EXPECTATION","symbol":"222080","name":"씨아이에스","round":"R3","loop":141,"large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C11_BATTERY_ORDERBOOK_RERATING","fine_archetype_id":"ELECTRODE_EQUIPMENT_BACKLOG_REVENUE_RECOGNITION_DELAY","trigger_date":"2024-03-27","trigger_type":"Stage2-FalsePositiveReview","entry_rule":"next_trading_day_close","entry_date":"2024-03-28","entry_price":13160.0,"MFE_30D_pct":1.82,"MAE_30D_pct":-21.5,"MFE_90D_pct":1.82,"MAE_90D_pct":-40.73,"MFE_180D_pct":1.82,"MAE_180D_pct":-46.43,"end_30D":"2024-05-13","end_90D":"2024-08-07","end_180D":"2024-12-20","peak_180D_date":"2024-03-28","trough_180D_date":"2024-12-09","outcome_label":"counterexample","calibration_usable":true,"corporate_action_window_180D_contaminated":false,"price_data_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","evidence_urls":["https://m.thebell.co.kr/m/newsview.asp?newskey=202403080901104280101912&svccode=","https://securities.miraeasset.com/bbs/download/2119745.pdf?attachmentId=2119745"],"source_proxy_only":true,"current_profile_error":true,"expected_current_stage":"Stage2-Actionable","suggested_stage":"Stage2-Watch_or_4B-Watch","residual_label":"backlog_count_without_conversion_timing_false_positive"}
{"row_type":"trigger","case_id":"C11_L141_05_PHILENERGY_20231117_ADVANCED_STACKER_ORDER","symbol":"378340","name":"필에너지","round":"R3","loop":141,"large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C11_BATTERY_ORDERBOOK_RERATING","fine_archetype_id":"ADVANCED_STACKER_CUSTOMER_EXPANSION_ORDERBOOK_4B_OVERLAY","trigger_date":"2023-11-17","trigger_type":"Stage2-Actionable","entry_rule":"next_trading_day_close","entry_date":"2023-11-20","entry_price":19160.0,"MFE_30D_pct":6.21,"MAE_30D_pct":-11.27,"MFE_90D_pct":86.33,"MAE_90D_pct":-13.88,"MFE_180D_pct":86.33,"MAE_180D_pct":-38.0,"end_30D":"2024-01-03","end_90D":"2024-04-01","end_180D":"2024-08-12","peak_180D_date":"2024-03-29","trough_180D_date":"2024-08-08","outcome_label":"positive_with_4B_overlay","calibration_usable":true,"corporate_action_window_180D_contaminated":false,"price_data_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","evidence_urls":["https://www.hanaw.com/download/research/FileServer/WEB/info/small_cap/2023/11/17/231120_philenergy.pdf"],"source_proxy_only":true,"current_profile_error":true,"expected_current_stage":"Stage2-Actionable","suggested_stage":"Stage2-Actionable_then_local_4B-Watch_after_90D_peak","residual_label":"positive_orderbook_but_exit_guard_missing"}
{"row_type":"trigger","case_id":"C11_L141_06_MPLUS_20230817_BACKLOG_3X_SALES","symbol":"259630","name":"엠플러스","round":"R3","loop":141,"large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C11_BATTERY_ORDERBOOK_RERATING","fine_archetype_id":"ASSEMBLY_EQUIPMENT_TURNKEY_BACKLOG_PEAK_REVERSAL","trigger_date":"2023-08-17","trigger_type":"Stage2-FalsePositiveReview","entry_rule":"next_trading_day_close","entry_date":"2023-08-18","entry_price":14950.0,"MFE_30D_pct":33.78,"MAE_30D_pct":-11.04,"MFE_90D_pct":33.78,"MAE_90D_pct":-28.56,"MFE_180D_pct":33.78,"MAE_180D_pct":-35.72,"end_30D":"2023-10-04","end_90D":"2024-01-02","end_180D":"2024-05-16","peak_180D_date":"2023-09-06","trough_180D_date":"2024-01-25","outcome_label":"counterexample","calibration_usable":true,"corporate_action_window_180D_contaminated":false,"price_data_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","evidence_urls":["https://www.hanaw.com/download/research/FileServer/WEB/info/small_cap/2023/08/16/230817_mplus.pdf"],"source_proxy_only":true,"current_profile_error":true,"expected_current_stage":"Stage2-Actionable","suggested_stage":"Stage2-Watch_or_local_4B-Watch","residual_label":"backlog_size_without_customer_capex_followthrough_false_positive"}
```

## 7. Raw component score simulation JSONL

These are shadow research scores only. They do not patch production scoring.

```jsonl
{"row_type":"score_simulation","case_id":"C11_L141_01_POSCO_FUTURE_M_20230130_SDI_40T","symbol":"003670","baseline_proxy_score":70.84,"current_profile_proxy_score":72.84,"component_scores":{"eps_fcf_explosion":72,"earnings_visibility":88,"bottleneck_pricing_power":70,"market_mispricing":62,"valuation_rerating":58,"capital_allocation":45,"information_confidence":90},"return_alignment":"aligned","current_profile_error":false,"reason":"missed_structural_magnitude_if_contract_bridge_underweighted"}
{"row_type":"score_simulation","case_id":"C11_L141_02_ECOPROBM_20231201_SDI_44T","symbol":"247540","baseline_proxy_score":54.5,"current_profile_proxy_score":56.5,"component_scores":{"eps_fcf_explosion":54,"earnings_visibility":78,"bottleneck_pricing_power":58,"market_mispricing":30,"valuation_rerating":24,"capital_allocation":35,"information_confidence":84},"return_alignment":"aligned","current_profile_error":true,"reason":"mega_contract_overweighted_without_margin_and_entry_guard"}
{"row_type":"score_simulation","case_id":"C11_L141_03_PNT_20240416_ELECTRODE_EQUIPMENT_CONTRACT","symbol":"137400","baseline_proxy_score":65.24,"current_profile_proxy_score":67.24,"component_scores":{"eps_fcf_explosion":68,"earnings_visibility":76,"bottleneck_pricing_power":66,"market_mispricing":64,"valuation_rerating":52,"capital_allocation":42,"information_confidence":82},"return_alignment":"aligned","current_profile_error":false,"reason":"signed_order_quality_correctly_leads_price_but_requires_4b_exit_after_peak"}
{"row_type":"score_simulation","case_id":"C11_L141_04_CIS_20240327_BACKLOG_EXPECTATION","symbol":"222080","baseline_proxy_score":46.32,"current_profile_proxy_score":48.32,"component_scores":{"eps_fcf_explosion":42,"earnings_visibility":64,"bottleneck_pricing_power":52,"market_mispricing":28,"valuation_rerating":26,"capital_allocation":32,"information_confidence":72},"return_alignment":"aligned","current_profile_error":true,"reason":"backlog_count_without_conversion_timing_false_positive"}
{"row_type":"score_simulation","case_id":"C11_L141_05_PHILENERGY_20231117_ADVANCED_STACKER_ORDER","symbol":"378340","baseline_proxy_score":58.24,"current_profile_proxy_score":60.24,"component_scores":{"eps_fcf_explosion":62,"earnings_visibility":72,"bottleneck_pricing_power":60,"market_mispricing":58,"valuation_rerating":44,"capital_allocation":36,"information_confidence":68},"return_alignment":"aligned","current_profile_error":true,"reason":"positive_orderbook_but_exit_guard_missing"}
{"row_type":"score_simulation","case_id":"C11_L141_06_MPLUS_20230817_BACKLOG_3X_SALES","symbol":"259630","baseline_proxy_score":48.01,"current_profile_proxy_score":50.01,"component_scores":{"eps_fcf_explosion":48,"earnings_visibility":62,"bottleneck_pricing_power":55,"market_mispricing":36,"valuation_rerating":30,"capital_allocation":28,"information_confidence":68},"return_alignment":"aligned","current_profile_error":true,"reason":"backlog_size_without_customer_capex_followthrough_false_positive"}
```

## 8. Aggregate row

```json
{
  "row_type": "aggregate",
  "round": "R3",
  "loop": 141,
  "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY",
  "canonical_archetype_id": "C11_BATTERY_ORDERBOOK_RERATING",
  "new_independent_case_count": 6,
  "usable_trigger_row_count": 6,
  "representative_trigger_count": 6,
  "positive_case_count": 2,
  "positive_with_4B_overlay_count": 1,
  "counterexample_count": 3,
  "stage4b_watch_or_overlay_count": 4,
  "stage4c_case_count": 0,
  "current_profile_error_count": 4,
  "index_baseline_rows_before": 18,
  "index_baseline_rows_after_if_accepted": 24,
  "session_aware_after_loop131_and_loop141_if_accepted": "about 29 rows",
  "source_proxy_only_count": 3,
  "evidence_url_pending_count": 0,
  "valid_rows_missing_required_mfe_mae": 0
}
```

## 9. Shadow rule candidate

```json
{
  "row_type": "shadow_weight",
  "do_not_apply_now": true,
  "do_not_propose_new_weight_delta": false,
  "axis": "C11_ORDERBOOK_QUALITY_REVENUE_TIMING_AND_4B_EXIT_GATE_V2",
  "candidate_rule": "Stage2-Actionable requires named customer/order amount plus delivery/revenue-timing bridge; mega contract or backlog headline alone is capped at Stage2-Watch when ASP/margin, customer capex timing, or entry MAE risk is unresolved. Local 4B watch should trigger after orderbook-led price peak if subsequent revenue/margin conversion is delayed.",
  "suggested_scope": [
    "C11_BATTERY_ORDERBOOK_RERATING",
    "L3_BATTERY_EV_GREEN_MOBILITY"
  ],
  "expected_effect": "reduce mega-contract/backlog false positives while preserving signed-order positives such as POSCO Future M and PNT"
}
```

## 10. Residual contribution summary

```json
{
  "row_type": "residual_contribution",
  "new_axis_proposed": "c11_orderbook_quality_revenue_timing_and_4b_exit_gate",
  "existing_axis_strengthened": [
    "stage2_required_bridge",
    "local_4b_watch_guard",
    "price_only_blowoff_blocks_positive_stage"
  ],
  "existing_axis_weakened": [],
  "why_new": "C11 needs a sector-specific distinction between signed commercial orderbook that can convert into revenue and backlog/mega-contract headlines whose ASP, customer capex timing, or margin bridge is not yet synchronized with price.",
  "next_recommended_archetypes": [
    "C11_BATTERY_ORDERBOOK_RERATING",
    "C01_ORDER_BACKLOG_MARGIN_BRIDGE",
    "C02_POWER_GRID_DATACENTER_CAPEX",
    "C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF",
    "C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE",
    "C14_EV_DEMAND_SLOWDOWN_4B_4C"
  ]
}
```

## 11. Proposed canonical compression

Fine leaves in this MD compress back to C11 as follows.

```text
CATHODE_LONG_TERM_SUPPLY_ORDERBOOK_MARGIN_BRIDGE -> C11_BATTERY_ORDERBOOK_RERATING
CATHODE_MEGA_CONTRACT_ASP_DOWNTURN_FALSE_POSITIVE -> C11_BATTERY_ORDERBOOK_RERATING
BATTERY_EQUIPMENT_SIGNED_ORDER_REVENUE_TIMING -> C11_BATTERY_ORDERBOOK_RERATING
ELECTRODE_EQUIPMENT_BACKLOG_REVENUE_RECOGNITION_DELAY -> C11_BATTERY_ORDERBOOK_RERATING
ADVANCED_STACKER_CUSTOMER_EXPANSION_ORDERBOOK_4B_OVERLAY -> C11_BATTERY_ORDERBOOK_RERATING
ASSEMBLY_EQUIPMENT_TURNKEY_BACKLOG_PEAK_REVERSAL -> C11_BATTERY_ORDERBOOK_RERATING
```

## 12. Deferred Coding Agent Handoff Prompt — do not execute in this research loop

```text
You are the later batch implementation agent for stock_agent. Do not use this section during the research-writing loop.

Input MD:
e2r_stock_web_v12_residual_round_R3_loop_141_L3_BATTERY_EV_GREEN_MOBILITY_C11_BATTERY_ORDERBOOK_RERATING_research.md

Task:
1. Parse the trigger rows JSONL.
2. Validate that every usable row has entry_date, entry_price, trigger_type, 30D/90D/180D MFE and MAE, large_sector_id, and canonical_archetype_id.
3. Dedupe by canonical_archetype_id + symbol + trigger_type + entry_date.
4. Treat source_proxy_only rows as usable for aggregate only if URL is present; do not apply a high-confidence promotion without direct disclosure or IR confirmation.
5. Evaluate the shadow axis C11_ORDERBOOK_QUALITY_REVENUE_TIMING_AND_4B_EXIT_GATE_V2.
6. Candidate patch semantics: C11 Stage2-Actionable requires named customer/order amount plus delivery/revenue-timing bridge. Mega-contract or backlog headline alone is capped at Stage2-Watch when ASP/margin, customer capex timing, or entry MAE risk is unresolved. Add local 4B-Watch after 90D orderbook-led price peak when subsequent conversion evidence is delayed.
7. Do not loosen Stage3-Green threshold.
8. Keep all changes scope-limited to C11_BATTERY_ORDERBOOK_RERATING / L3_BATTERY_EV_GREEN_MOBILITY unless validated by other C11 rows.
```

## 13. Next research state

```text
completed_round = R3
completed_loop = 141
selection_basis = docs/core/V12_Research_No_Repeat_Index.md
selected_priority_bucket = Priority 0
round_schedule_status = coverage_index_selected_not_sequential
round_sector_consistency = pass
next_recommended_archetypes = C11_BATTERY_ORDERBOOK_RERATING | C01_ORDER_BACKLOG_MARGIN_BRIDGE | C02_POWER_GRID_DATACENTER_CAPEX | C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF | C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE | C14_EV_DEMAND_SLOWDOWN_4B_4C
```
