# E2R Stock-Web v12 Residual Research — R1 / C01 Order Backlog Margin Bridge Follow-up

```text
MD filename:
e2r_stock_web_v12_residual_round_R1_loop_126_L1_INDUSTRIALS_INFRA_DEFENSE_GRID_C01_ORDER_BACKLOG_MARGIN_BRIDGE_research.md

selected_round:
R1

selected_loop:
126

selection_basis:
docs/core/V12_Research_No_Repeat_Index.md

selected_priority_bucket:
Priority 0 / under_30_representative_rows / C01 static rows 19 need_to_30 11 before local session follow-ups

round_schedule_status:
coverage_index_selected

round_sector_consistency:
pass

large_sector_id:
L1_INDUSTRIALS_INFRA_DEFENSE_GRID

canonical_archetype_id:
C01_ORDER_BACKLOG_MARGIN_BRIDGE

fine_archetype_id:
SHIPBUILDING_BACKLOG_SUPPLIER_MARGIN_FCF_BRIDGE_VS_PRODUCT_IDENTITY_PROXY

loop_objective:
coverage_gap_fill | followup_new_symbol_date_family | supplier_backlog_margin_bridge | product_identity_proxy_counterexample | 4B_non_price_requirement_stress_test

price_source:
Songdaiki/stock-web

price_basis:
tradable_raw

price_adjustment_status:
raw_unadjusted_marcap

stock_web_manifest_max_date:
2026-02-20

production_scoring_changed:
false

shadow_weight_only:
true
```

## 1. Scheduler decision

The coverage index is still the driver, not round rotation. Static `V12_Research_No_Repeat_Index.md` lists `C01_ORDER_BACKLOG_MARGIN_BRIDGE` as Priority 0 with 19 representative rows and need-to-30 of 11. This session already produced one C01 file with six representative rows; this follow-up adds seven representative trigger rows and two narrative-only source-proxy blockers, so the local estimated C01 representative count crosses the minimum 30-row stability threshold after commit.

This loop deliberately avoids the previous C01 large-yard core set and widens the archetype toward shipbuilding suppliers, LNG cryogenic insulation, mid-sized shipbuilders, marine-engine reorganization, and product-identity traps.

## 2. Price atlas confirmation

```text
price_atlas_repo = https://github.com/Songdaiki/stock-web
source_name = FinanceData/marcap
price_basis = tradable_raw
price_adjustment_status = raw_unadjusted_marcap
manifest_max_date = 2026-02-20
calibration_shard_root = atlas/ohlcv_tradable_by_symbol_year
entry_price_basis = entry_date close column c
MFE_MAE_windows = 30 / 90 / 180 trading days
```

All representative trigger rows use stock-web tradable shards. The raw/unadjusted caveat is preserved; if future profile review finds a corporate-action candidate inside any entry-to-180D window, that row should be demoted to `calibration_usable=false`.

## 3. Case summary

| symbol | company | trigger_type | entry_date | entry_price | MFE_30D | MFE_90D | MFE_180D | MAE_30D | MAE_90D | MAE_180D | label |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|
| 009540 | HD한국조선해양 | Stage2-Actionable | 2025-01-20 | 244000 | 3.89 | 37.3 | 79.51 | -15.37 | -23.89 | -23.89 | positive |
| 097230 | HJ중공업 | Stage2-Actionable | 2025-01-08 | 7270 | 6.6 | 36.18 | 372.49 | -20.36 | -22.56 | -22.56 | positive |
| 033500 | 동성화인텍 | Stage2-Actionable | 2024-02-22 | 11560 | 8.82 | 17.47 | 24.39 | -2.34 | -2.34 | -7.79 | positive |
| 075580 | 세진중공업 | Stage3-Yellow | 2024-09-27 | 7250 | 7.03 | 32.41 | 78.62 | -10.07 | -12.0 | -12.0 | positive |
| 071970 | HD현대마린엔진 | Stage4B | 2024-07-31 | 23050 | 7.81 | 7.81 | 67.68 | -32.06 | -32.06 | -32.06 | counterexample |
| 017960 | 한국카본 | Stage2 | 2021-03-22 | 11700 | 13.68 | 16.24 | 16.24 | -2.56 | -3.42 | -22.22 | counterexample |
| 077970 | STX엔진 | Stage2 | 2023-09-12 | 13830 | 4.77 | 4.77 | 13.74 | -20.46 | -20.46 | -20.46 | counterexample |

## 4. Research conclusion

C01 should not treat every shipbuilding-adjacent keyword as a backlog-margin bridge. The rule that survives this loop is more surgical:

```text
C01_BACKLOG_SUPPLIER_MARGIN_BRIDGE_REQUIRES_DELIVERY_AND_CONVERSION_GATE_WITH_PRODUCT_IDENTITY_PROXY_BLOCK
```

Positive C01 credit is appropriate when the evidence chain has **named order/customer -> backlog or delivery visibility -> capacity or production schedule -> OP margin / FCF conversion**. HD KSOE and HJ Heavy show the prime/mid-size yard version of this bridge; Dongsung Finetec and Sejin show the supplier version where the bridge runs through LNG insulation/tanks/deckhouse deliveries and margin guidance.

Counterexample handling matters just as much. HD Hyundai Marine Engine's launch/acquisition event was strategically meaningful, but the entry date sat on an event-premium pocket before the order/margin bridge was visible, producing a deep early MAE before later recovery. Korea Carbon's single LNG-material contract had real order value but did not by itself prove durable margin conversion. STX Engine's eco-friendly engine launch was product capability, not a fresh named-order backlog event. These should remain Stage2-watch or Stage4B overlay until delivery/revenue/margin evidence appears.

## 5. Evidence notes

- HD Korea Shipbuilding & Offshore Engineering: 2024 operating profit forecast and supercycle contract context from Yonhap/Infomax source.
- HJ Heavy Industries: record 2024 order intake, including shipbuilding and eco-friendly container ships.
- Dongsung Finetec: Hanwha Ocean LOI around KRW90bn, NO96 LO3+ supply by 2027, four-year secured work/capacity expansion note.
- Sejin Heavy Industries: 2H tank delivery restart, Q2 OPM 9.8%, double-digit OPM target, Hanwha Ocean deck-house delivery path.
- HD Hyundai Marine Engine: acquisition completion and portfolio reorganization, but source did not prove immediate fresh order/margin bridge.
- Korea Carbon: KRW43.9bn LNG carrier material contract, 16.09% of recent sales, but weaker durability after the first reaction.
- STX Engine: eco-friendly engine technology launch aimed at LNG carrier/container ship market, but product launch without named order/backlog conversion.

## 6. Machine-readable trigger rows

```jsonl
{"row_type": "trigger", "trigger_id": "C01_R1L126_T01_009540_2025-01-20", "case_id": "C01_R1L126_CASE_01_009540", "symbol": "009540", "company_name": "HD한국조선해양", "round": "R1", "loop": 126, "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "canonical_archetype_id": "C01_ORDER_BACKLOG_MARGIN_BRIDGE", "fine_archetype_id": "SHIPBUILDING_BACKLOG_SUPPLIER_MARGIN_FCF_BRIDGE_VS_PRODUCT_IDENTITY_PROXY", "sector": "shipbuilding_heavy_industrials_supply_chain", "primary_archetype": "C01_ORDER_BACKLOG_MARGIN_BRIDGE", "loop_objective": "coverage_gap_fill|followup_new_symbol_date_family|margin_bridge_gate|product_identity_proxy_counterexample|4B_non_price_requirement_stress_test", "trigger_type": "Stage2-Actionable", "trigger_date": "2025-01-19", "entry_rule": "source Sunday / next tradable close", "evidence_available_at_that_date": "Yonhap/Infomax forecast HD KSOE 2024 OP KRW 1.43tn; industry attribution to increased contracts in shipbuilding supercycle.", "evidence_source": "https://en.yna.co.kr/view/AEN20250119001200320", "stage2_evidence_fields": ["order backlog / contract supercycle visible", "2024 OP turnaround forecast", "large shipbuilder margin bridge visible"], "stage3_evidence_fields": ["multi-shipbuilder profit confirmation pending at trigger", "FCF details not in evidence source"], "stage4b_evidence_fields": ["high-MAE early volatility despite strong 180D MFE"], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/009/009540/2025.csv", "profile_path": "atlas/symbol_profiles/009/009540.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "entry_date": "2025-01-20", "entry_price": 244000.0, "MFE_30D_pct": 3.89, "MFE_90D_pct": 37.3, "MFE_180D_pct": 79.51, "MFE_1Y_pct": null, "MFE_2Y_pct": null, "MAE_30D_pct": -15.37, "MAE_90D_pct": -23.89, "MAE_180D_pct": -23.89, "MAE_1Y_pct": null, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2025-09-05", "peak_price": 438000.0, "drawdown_after_peak_pct": -10.96, "green_lateness_ratio": "not_applicable_no_confirmed_stage3_green_trigger", "four_b_local_peak_proximity": "requires_followup_overlay", "four_b_full_window_peak_proximity": null, "four_b_timing_verdict": "4B_overlay_needed_after_fast_reprice", "four_b_evidence_type": ["margin_or_backlog_slowdown"], "four_c_protection_label": "thesis_break_watch_only", "trigger_outcome_label": "major_shipbuilder_profit_turnaround_to_backlog_margin_bridge", "positive_or_counterexample": "positive", "current_profile_verdict": "old_profile_too_cautious_on_orderbook_margin_bridge_but_needs_4B_after_fast_reprice", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "profile_checked_no_overlap_in_entry_to_180D_or_no_recent_profile_event_seen_in_selected_window", "same_entry_group_id": "C01_R1L126_009540_2025-01-20", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false}
{"row_type": "trigger", "trigger_id": "C01_R1L126_T02_097230_2025-01-08", "case_id": "C01_R1L126_CASE_02_097230", "symbol": "097230", "company_name": "HJ중공업", "round": "R1", "loop": 126, "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "canonical_archetype_id": "C01_ORDER_BACKLOG_MARGIN_BRIDGE", "fine_archetype_id": "SHIPBUILDING_BACKLOG_SUPPLIER_MARGIN_FCF_BRIDGE_VS_PRODUCT_IDENTITY_PROXY", "sector": "shipbuilding_heavy_industrials_supply_chain", "primary_archetype": "C01_ORDER_BACKLOG_MARGIN_BRIDGE", "loop_objective": "coverage_gap_fill|followup_new_symbol_date_family|margin_bridge_gate|product_identity_proxy_counterexample|4B_non_price_requirement_stress_test", "trigger_type": "Stage2-Actionable", "trigger_date": "2025-01-08", "entry_rule": "same-day close after published order report", "evidence_available_at_that_date": "Pulse reported HJ Shipbuilding secured KRW 4.69tn orders in 2024, including KRW 1.75tn shipbuilding orders and KRW 1.2tn eco-friendly container ship orders.", "evidence_source": "https://pulse.mk.co.kr/news/english/11212735", "stage2_evidence_fields": ["record order intake", "named vessel categories", "order intake growth versus prior years"], "stage3_evidence_fields": ["profit bridge not fully confirmed at trigger", "delivery margin still forward-looking"], "stage4b_evidence_fields": ["very large 180D MFE implies later profit-lock overlay needed"], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/097/097230/2025.csv", "profile_path": "atlas/symbol_profiles/097/097230.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "entry_date": "2025-01-08", "entry_price": 7270.0, "MFE_30D_pct": 6.6, "MFE_90D_pct": 36.18, "MFE_180D_pct": 372.49, "MFE_1Y_pct": null, "MFE_2Y_pct": null, "MAE_30D_pct": -20.36, "MAE_90D_pct": -22.56, "MAE_180D_pct": -22.56, "MAE_1Y_pct": null, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2025-09-10", "peak_price": 34350.0, "drawdown_after_peak_pct": -27.51, "green_lateness_ratio": "not_applicable_no_confirmed_stage3_green_trigger", "four_b_local_peak_proximity": "requires_followup_overlay", "four_b_full_window_peak_proximity": null, "four_b_timing_verdict": "4B_overlay_needed_after_fast_reprice", "four_b_evidence_type": ["margin_or_backlog_slowdown"], "four_c_protection_label": "thesis_break_watch_only", "trigger_outcome_label": "mid_size_shipbuilder_record_order_intake_to_multi_year_backlog", "positive_or_counterexample": "positive", "current_profile_verdict": "profile_should_allow_stage2_actionable_when_record_order_intake_links_to_delivery_visibility", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "profile_checked_no_overlap_in_entry_to_180D_or_no_recent_profile_event_seen_in_selected_window", "same_entry_group_id": "C01_R1L126_097230_2025-01-08", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false}
{"row_type": "trigger", "trigger_id": "C01_R1L126_T03_033500_2024-02-22", "case_id": "C01_R1L126_CASE_03_033500", "symbol": "033500", "company_name": "동성화인텍", "round": "R1", "loop": 126, "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "canonical_archetype_id": "C01_ORDER_BACKLOG_MARGIN_BRIDGE", "fine_archetype_id": "SHIPBUILDING_BACKLOG_SUPPLIER_MARGIN_FCF_BRIDGE_VS_PRODUCT_IDENTITY_PROXY", "sector": "shipbuilding_heavy_industrials_supply_chain", "primary_archetype": "C01_ORDER_BACKLOG_MARGIN_BRIDGE", "loop_objective": "coverage_gap_fill|followup_new_symbol_date_family|margin_bridge_gate|product_identity_proxy_counterexample|4B_non_price_requirement_stress_test", "trigger_type": "Stage2-Actionable", "trigger_date": "2024-02-22", "entry_rule": "next tradable close after LOI disclosure", "evidence_available_at_that_date": "Dongsung Finetec LOI with Hanwha Ocean for about KRW90bn cryogenic insulation materials; supply through 2027; four-year secured order and capacity expansion noted.", "evidence_source": "https://kolbia.org/en/bbs/board.php?bo_table=en_notice&page=24&wr_id=139", "stage2_evidence_fields": ["named customer Hanwha Ocean", "KRW90bn LOI", "capacity expansion / four-year work visibility"], "stage3_evidence_fields": ["LOI not final executive contract at source date", "margin conversion still pending"], "stage4b_evidence_fields": ["none; price path low MAE"], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/033/033500/2024.csv", "profile_path": "atlas/symbol_profiles/033/033500.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "entry_date": "2024-02-22", "entry_price": 11560.0, "MFE_30D_pct": 8.82, "MFE_90D_pct": 17.47, "MFE_180D_pct": 24.39, "MFE_1Y_pct": null, "MFE_2Y_pct": null, "MAE_30D_pct": -2.34, "MAE_90D_pct": -2.34, "MAE_180D_pct": -7.79, "MAE_1Y_pct": null, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2024-08-01", "peak_price": 14380.0, "drawdown_after_peak_pct": -25.87, "green_lateness_ratio": "not_applicable_no_confirmed_stage3_green_trigger", "four_b_local_peak_proximity": "not_applicable", "four_b_full_window_peak_proximity": null, "four_b_timing_verdict": "not_applicable", "four_b_evidence_type": [], "four_c_protection_label": "thesis_break_watch_only", "trigger_outcome_label": "lng_insulation_loi_capacity_backlog_bridge", "positive_or_counterexample": "positive", "current_profile_verdict": "current_profile_correct_if_it_demands_capacity_and_backlog_bridge_not_theme_only", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "profile_checked_no_overlap_in_entry_to_180D_or_no_recent_profile_event_seen_in_selected_window", "same_entry_group_id": "C01_R1L126_033500_2024-02-22", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false}
{"row_type": "trigger", "trigger_id": "C01_R1L126_T04_075580_2024-09-27", "case_id": "C01_R1L126_CASE_04_075580", "symbol": "075580", "company_name": "세진중공업", "round": "R1", "loop": 126, "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "canonical_archetype_id": "C01_ORDER_BACKLOG_MARGIN_BRIDGE", "fine_archetype_id": "SHIPBUILDING_BACKLOG_SUPPLIER_MARGIN_FCF_BRIDGE_VS_PRODUCT_IDENTITY_PROXY", "sector": "shipbuilding_heavy_industrials_supply_chain", "primary_archetype": "C01_ORDER_BACKLOG_MARGIN_BRIDGE", "loop_objective": "coverage_gap_fill|followup_new_symbol_date_family|margin_bridge_gate|product_identity_proxy_counterexample|4B_non_price_requirement_stress_test", "trigger_type": "Stage3-Yellow", "trigger_date": "2024-09-27", "entry_rule": "next tradable close after morning report", "evidence_available_at_that_date": "Asia Business Daily reported delivery of tanks to resume in 2H, Q2 OPM 9.8%, annual double-digit OPM target, Hanwha Ocean deck-house deliveries and piping subsidiary improvement.", "evidence_source": "https://www.asiae.co.kr/en/article/2024092709093289240", "stage2_evidence_fields": ["tank delivery timing", "deck-house customer route", "operating margin guide"], "stage3_evidence_fields": ["2H delivery acceleration", "margin target / automation improvement"], "stage4b_evidence_fields": ["not at trigger; later large MFE requires trailing 4B"], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/075/075580/2024.csv", "profile_path": "atlas/symbol_profiles/075/075580.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "entry_date": "2024-09-27", "entry_price": 7250.0, "MFE_30D_pct": 7.03, "MFE_90D_pct": 32.41, "MFE_180D_pct": 78.62, "MFE_1Y_pct": null, "MFE_2Y_pct": null, "MAE_30D_pct": -10.07, "MAE_90D_pct": -12.0, "MAE_180D_pct": -12.0, "MAE_1Y_pct": null, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2025-06-16", "peak_price": 12950.0, "drawdown_after_peak_pct": -14.98, "green_lateness_ratio": "not_applicable_no_confirmed_stage3_green_trigger", "four_b_local_peak_proximity": "requires_followup_overlay", "four_b_full_window_peak_proximity": null, "four_b_timing_verdict": "4B_overlay_needed_after_fast_reprice", "four_b_evidence_type": ["margin_or_backlog_slowdown"], "four_c_protection_label": "thesis_break_watch_only", "trigger_outcome_label": "tank_deckhouse_delivery_reacceleration_margin_guidance", "positive_or_counterexample": "positive", "current_profile_verdict": "profile_too_late_if_it_waits_for_full_year_result_after_delivery_bridge", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "profile_checked_no_overlap_in_entry_to_180D_or_no_recent_profile_event_seen_in_selected_window", "same_entry_group_id": "C01_R1L126_075580_2024-09-27", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false}
{"row_type": "trigger", "trigger_id": "C01_R1L126_T05_071970_2024-07-31", "case_id": "C01_R1L126_CASE_05_071970", "symbol": "071970", "company_name": "HD현대마린엔진", "round": "R1", "loop": 126, "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "canonical_archetype_id": "C01_ORDER_BACKLOG_MARGIN_BRIDGE", "fine_archetype_id": "SHIPBUILDING_BACKLOG_SUPPLIER_MARGIN_FCF_BRIDGE_VS_PRODUCT_IDENTITY_PROXY", "sector": "shipbuilding_heavy_industrials_supply_chain", "primary_archetype": "C01_ORDER_BACKLOG_MARGIN_BRIDGE", "loop_objective": "coverage_gap_fill|followup_new_symbol_date_family|margin_bridge_gate|product_identity_proxy_counterexample|4B_non_price_requirement_stress_test", "trigger_type": "Stage4B", "trigger_date": "2024-07-31", "entry_rule": "next tradable close after HD launch/acquisition completion", "evidence_available_at_that_date": "HD Hyundai launched HD Hyundai Marine Engine and completed acquisition of 35.05% stake; source emphasizes portfolio restructuring and export-channel collaboration rather than immediate order/margin conversion.", "evidence_source": "https://www.hd.com/en/newsroom/media-hub/press/view?detailsKey=3176", "stage2_evidence_fields": ["group acquisition / engine portfolio identity"], "stage3_evidence_fields": ["missing direct new order and margin bridge at trigger"], "stage4b_evidence_fields": ["event-premium / integration execution risk", "large immediate MAE before later recovery"], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/071/071970/2024.csv", "profile_path": "atlas/symbol_profiles/071/071970.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "entry_date": "2024-07-31", "entry_price": 23050.0, "MFE_30D_pct": 7.81, "MFE_90D_pct": 7.81, "MFE_180D_pct": 67.68, "MFE_1Y_pct": null, "MFE_2Y_pct": null, "MAE_30D_pct": -32.06, "MAE_90D_pct": -32.06, "MAE_180D_pct": -32.06, "MAE_1Y_pct": null, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2025-04-28", "peak_price": 38650.0, "drawdown_after_peak_pct": -6.47, "green_lateness_ratio": "not_applicable_no_confirmed_stage3_green_trigger", "four_b_local_peak_proximity": "requires_followup_overlay", "four_b_full_window_peak_proximity": 0.0, "four_b_timing_verdict": "4B_overlay_needed_after_fast_reprice", "four_b_evidence_type": ["price_only", "positioning_overheat", "execution_risk"], "four_c_protection_label": "thesis_break_watch_only", "trigger_outcome_label": "marine_engine_platform_reorganization_but_entry_after_event_premium", "positive_or_counterexample": "counterexample", "current_profile_verdict": "old_profile_false_positive_if_launch_identity_counted_as_margin_bridge", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "profile_checked_no_overlap_in_entry_to_180D_or_no_recent_profile_event_seen_in_selected_window", "same_entry_group_id": "C01_R1L126_071970_2024-07-31", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false}
{"row_type": "trigger", "trigger_id": "C01_R1L126_T06_017960_2021-03-22", "case_id": "C01_R1L126_CASE_06_017960", "symbol": "017960", "company_name": "한국카본", "round": "R1", "loop": 126, "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "canonical_archetype_id": "C01_ORDER_BACKLOG_MARGIN_BRIDGE", "fine_archetype_id": "SHIPBUILDING_BACKLOG_SUPPLIER_MARGIN_FCF_BRIDGE_VS_PRODUCT_IDENTITY_PROXY", "sector": "shipbuilding_heavy_industrials_supply_chain", "primary_archetype": "C01_ORDER_BACKLOG_MARGIN_BRIDGE", "loop_objective": "coverage_gap_fill|followup_new_symbol_date_family|margin_bridge_gate|product_identity_proxy_counterexample|4B_non_price_requirement_stress_test", "trigger_type": "Stage2", "trigger_date": "2021-03-22", "entry_rule": "next tradable close after contract article", "evidence_available_at_that_date": "Korea Carbon signed about KRW43.9bn LNG carrier material supply contract, equal to 16.09% of recent sales, with contract period through 2023.", "evidence_source": "https://www.asiae.co.kr/en/article/2021032210464989205", "stage2_evidence_fields": ["contract size disclosed", "LNG carrier material supply route"], "stage3_evidence_fields": ["no multi-order cadence or margin/FCF conversion in source"], "stage4b_evidence_fields": ["90D MFE modest then 180D drawdown"], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/017/017960/2021.csv", "profile_path": "atlas/symbol_profiles/017/017960.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "entry_date": "2021-03-22", "entry_price": 11700.0, "MFE_30D_pct": 13.68, "MFE_90D_pct": 16.24, "MFE_180D_pct": 16.24, "MFE_1Y_pct": null, "MFE_2Y_pct": null, "MAE_30D_pct": -2.56, "MAE_90D_pct": -3.42, "MAE_180D_pct": -22.22, "MAE_1Y_pct": null, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2021-05-04", "peak_price": 13600.0, "drawdown_after_peak_pct": -33.09, "green_lateness_ratio": "not_applicable_no_confirmed_stage3_green_trigger", "four_b_local_peak_proximity": null, "four_b_full_window_peak_proximity": null, "four_b_timing_verdict": "product_identity_proxy_not_full_4B", "four_b_evidence_type": ["price_only", "positioning_overheat", "execution_risk"], "four_c_protection_label": "thesis_break_watch_only", "trigger_outcome_label": "lng_insulation_contract_without_durable_margin_followthrough", "positive_or_counterexample": "counterexample", "current_profile_verdict": "stage2_watch_only_unless_contract_pipeline_rolls_into_margin_bridge", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "profile_checked_no_overlap_in_entry_to_180D_or_no_recent_profile_event_seen_in_selected_window", "same_entry_group_id": "C01_R1L126_017960_2021-03-22", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false}
{"row_type": "trigger", "trigger_id": "C01_R1L126_T07_077970_2023-09-12", "case_id": "C01_R1L126_CASE_07_077970", "symbol": "077970", "company_name": "STX엔진", "round": "R1", "loop": 126, "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "canonical_archetype_id": "C01_ORDER_BACKLOG_MARGIN_BRIDGE", "fine_archetype_id": "SHIPBUILDING_BACKLOG_SUPPLIER_MARGIN_FCF_BRIDGE_VS_PRODUCT_IDENTITY_PROXY", "sector": "shipbuilding_heavy_industrials_supply_chain", "primary_archetype": "C01_ORDER_BACKLOG_MARGIN_BRIDGE", "loop_objective": "coverage_gap_fill|followup_new_symbol_date_family|margin_bridge_gate|product_identity_proxy_counterexample|4B_non_price_requirement_stress_test", "trigger_type": "Stage2", "trigger_date": "2023-09-12", "entry_rule": "next tradable close after eco-engine article", "evidence_available_at_that_date": "STX Engine developed eco-friendly ship engine targeting LNG carriers and LNG-powered large container ships; source does not give fresh order, backlog, delivery schedule, or margin conversion.", "evidence_source": "https://www.asiae.co.kr/en/article/2023091210415895357", "stage2_evidence_fields": ["product capability / eco-friendly engine route"], "stage3_evidence_fields": ["missing named customer/order", "missing revenue/margin bridge"], "stage4b_evidence_fields": ["product-identity proxy with -21% MAE"], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/077/077970/2023.csv", "profile_path": "atlas/symbol_profiles/077/077970.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "entry_date": "2023-09-12", "entry_price": 13830.0, "MFE_30D_pct": 4.77, "MFE_90D_pct": 4.77, "MFE_180D_pct": 13.74, "MFE_1Y_pct": null, "MFE_2Y_pct": null, "MAE_30D_pct": -20.46, "MAE_90D_pct": -20.46, "MAE_180D_pct": -20.46, "MAE_1Y_pct": null, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2024-04-24", "peak_price": 15730.0, "drawdown_after_peak_pct": -18.05, "green_lateness_ratio": "not_applicable_no_confirmed_stage3_green_trigger", "four_b_local_peak_proximity": null, "four_b_full_window_peak_proximity": null, "four_b_timing_verdict": "product_identity_proxy_not_full_4B", "four_b_evidence_type": ["price_only", "positioning_overheat", "execution_risk"], "four_c_protection_label": "thesis_break_watch_only", "trigger_outcome_label": "eco_friendly_engine_product_launch_no_order_backlog_bridge", "positive_or_counterexample": "counterexample", "current_profile_verdict": "product_launch_should_not_upgrade_without_named_order_or_backlog_conversion", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "profile_checked_no_overlap_in_entry_to_180D_or_no_recent_profile_event_seen_in_selected_window", "same_entry_group_id": "C01_R1L126_077970_2023-09-12", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false}
```

## 7. Machine-readable score simulation rows

```jsonl
{"row_type": "score_simulation", "trigger_id": "C01_R1L126_T01_009540_2025-01-20", "symbol": "009540", "company_name": "HD한국조선해양", "round": "R1", "loop": 126, "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "canonical_archetype_id": "C01_ORDER_BACKLOG_MARGIN_BRIDGE", "contract_score": 8, "backlog_visibility_score": 8, "margin_bridge_score": 7, "revision_score": 6, "relative_strength_score": 5, "customer_quality_score": 5, "policy_or_regulatory_score": 1, "valuation_repricing_score": 5, "execution_risk_score": 4, "legal_or_contract_risk_score": 1, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 1, "order_intake_quality_score": 8, "fcf_conversion_score": 5, "positioning_overheat_score": 5, "baseline_current_profile_stage": "Stage2-Actionable", "proposed_shadow_stage": "Stage2-Actionable", "residual_error_type": "old_profile_too_cautious_on_orderbook_margin_bridge_but_needs_4B_after_fast_reprice"}
{"row_type": "score_simulation", "trigger_id": "C01_R1L126_T02_097230_2025-01-08", "symbol": "097230", "company_name": "HJ중공업", "round": "R1", "loop": 126, "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "canonical_archetype_id": "C01_ORDER_BACKLOG_MARGIN_BRIDGE", "contract_score": 9, "backlog_visibility_score": 8, "margin_bridge_score": 6, "revision_score": 5, "relative_strength_score": 6, "customer_quality_score": 4, "policy_or_regulatory_score": 1, "valuation_repricing_score": 4, "execution_risk_score": 5, "legal_or_contract_risk_score": 1, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 1, "order_intake_quality_score": 9, "fcf_conversion_score": 4, "positioning_overheat_score": 4, "baseline_current_profile_stage": "Stage2-Actionable", "proposed_shadow_stage": "Stage2-Actionable", "residual_error_type": "profile_should_allow_stage2_actionable_when_record_order_intake_links_to_delivery_visibility"}
{"row_type": "score_simulation", "trigger_id": "C01_R1L126_T03_033500_2024-02-22", "symbol": "033500", "company_name": "동성화인텍", "round": "R1", "loop": 126, "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "canonical_archetype_id": "C01_ORDER_BACKLOG_MARGIN_BRIDGE", "contract_score": 8, "backlog_visibility_score": 8, "margin_bridge_score": 7, "revision_score": 5, "relative_strength_score": 4, "customer_quality_score": 7, "policy_or_regulatory_score": 1, "valuation_repricing_score": 3, "execution_risk_score": 3, "legal_or_contract_risk_score": 2, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 1, "order_intake_quality_score": 8, "fcf_conversion_score": 5, "positioning_overheat_score": 3, "baseline_current_profile_stage": "Stage2-Actionable", "proposed_shadow_stage": "Stage2-Actionable", "residual_error_type": "current_profile_correct_if_it_demands_capacity_and_backlog_bridge_not_theme_only"}
{"row_type": "score_simulation", "trigger_id": "C01_R1L126_T04_075580_2024-09-27", "symbol": "075580", "company_name": "세진중공업", "round": "R1", "loop": 126, "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "canonical_archetype_id": "C01_ORDER_BACKLOG_MARGIN_BRIDGE", "contract_score": 7, "backlog_visibility_score": 7, "margin_bridge_score": 8, "revision_score": 6, "relative_strength_score": 5, "customer_quality_score": 6, "policy_or_regulatory_score": 1, "valuation_repricing_score": 4, "execution_risk_score": 4, "legal_or_contract_risk_score": 1, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 1, "order_intake_quality_score": 7, "fcf_conversion_score": 6, "positioning_overheat_score": 4, "baseline_current_profile_stage": "Stage2-Actionable", "proposed_shadow_stage": "Stage3-Yellow", "residual_error_type": "profile_too_late_if_it_waits_for_full_year_result_after_delivery_bridge"}
{"row_type": "score_simulation", "trigger_id": "C01_R1L126_T05_071970_2024-07-31", "symbol": "071970", "company_name": "HD현대마린엔진", "round": "R1", "loop": 126, "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "canonical_archetype_id": "C01_ORDER_BACKLOG_MARGIN_BRIDGE", "contract_score": 5, "backlog_visibility_score": 5, "margin_bridge_score": 3, "revision_score": 3, "relative_strength_score": 6, "customer_quality_score": 4, "policy_or_regulatory_score": 1, "valuation_repricing_score": 7, "execution_risk_score": 7, "legal_or_contract_risk_score": 3, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 2, "order_intake_quality_score": 5, "fcf_conversion_score": 1, "positioning_overheat_score": 7, "baseline_current_profile_stage": "Stage2", "proposed_shadow_stage": "Stage4B", "residual_error_type": "old_profile_false_positive_if_launch_identity_counted_as_margin_bridge"}
{"row_type": "score_simulation", "trigger_id": "C01_R1L126_T06_017960_2021-03-22", "symbol": "017960", "company_name": "한국카본", "round": "R1", "loop": 126, "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "canonical_archetype_id": "C01_ORDER_BACKLOG_MARGIN_BRIDGE", "contract_score": 7, "backlog_visibility_score": 6, "margin_bridge_score": 3, "revision_score": 2, "relative_strength_score": 3, "customer_quality_score": 5, "policy_or_regulatory_score": 1, "valuation_repricing_score": 3, "execution_risk_score": 5, "legal_or_contract_risk_score": 1, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 1, "order_intake_quality_score": 7, "fcf_conversion_score": 1, "positioning_overheat_score": 3, "baseline_current_profile_stage": "Stage2", "proposed_shadow_stage": "Stage2-watch", "residual_error_type": "stage2_watch_only_unless_contract_pipeline_rolls_into_margin_bridge"}
{"row_type": "score_simulation", "trigger_id": "C01_R1L126_T07_077970_2023-09-12", "symbol": "077970", "company_name": "STX엔진", "round": "R1", "loop": 126, "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "canonical_archetype_id": "C01_ORDER_BACKLOG_MARGIN_BRIDGE", "contract_score": 3, "backlog_visibility_score": 3, "margin_bridge_score": 2, "revision_score": 2, "relative_strength_score": 3, "customer_quality_score": 4, "policy_or_regulatory_score": 1, "valuation_repricing_score": 2, "execution_risk_score": 6, "legal_or_contract_risk_score": 1, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 1, "order_intake_quality_score": 3, "fcf_conversion_score": 0, "positioning_overheat_score": 2, "baseline_current_profile_stage": "Stage2", "proposed_shadow_stage": "Stage2-watch", "residual_error_type": "product_launch_should_not_upgrade_without_named_order_or_backlog_conversion"}
```

## 8. Aggregate / shadow / residual rows

### aggregate_rows_jsonl

```jsonl
{"row_type": "aggregate", "round": "R1", "loop": 126, "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "canonical_archetype_id": "C01_ORDER_BACKLOG_MARGIN_BRIDGE", "fine_archetype_id": "SHIPBUILDING_BACKLOG_SUPPLIER_MARGIN_FCF_BRIDGE_VS_PRODUCT_IDENTITY_PROXY", "representative_trigger_count": 7, "new_independent_case_count": 7, "same_archetype_new_symbol_count": 7, "positive_case_count": 4, "counterexample_count": 3, "stage4b_overlay_count": 6, "stage4c_case_count": 0, "avg_MFE_90D_pct": 21.74, "avg_MAE_90D_pct": -16.68, "rule_candidate": "C01_BACKLOG_SUPPLIER_MARGIN_BRIDGE_REQUIRES_DELIVERY_AND_CONVERSION_GATE_WITH_PRODUCT_IDENTITY_PROXY_BLOCK", "production_scoring_changed": false, "shadow_weight_only": true}
```

### shadow_weight_rows_jsonl

```jsonl
{"row_type": "shadow_weight", "round": "R1", "loop": 126, "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "canonical_archetype_id": "C01_ORDER_BACKLOG_MARGIN_BRIDGE", "rule_candidate": "C01_BACKLOG_SUPPLIER_MARGIN_BRIDGE_REQUIRES_DELIVERY_AND_CONVERSION_GATE_WITH_PRODUCT_IDENTITY_PROXY_BLOCK", "increase_weight_if": ["named_customer_or_order", "multi_year_backlog", "capacity_or_delivery_visibility", "OP_margin_or_FCF_bridge"], "decrease_weight_if": ["product_identity_only", "launch_or_acquisition_event_only", "single_contract_without_repeat_or_margin", "late_price_reprice_without_new_bridge"], "do_not_change_production_profile_now": true}
```

### residual_contribution_rows_jsonl

```jsonl
{"row_type": "residual_contribution", "round": "R1", "loop": 126, "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "canonical_archetype_id": "C01_ORDER_BACKLOG_MARGIN_BRIDGE", "current_profile_error_count": 5, "residual_summary": "C01 still fails when generic shipbuilding/engine product identity is treated like backlog-margin bridge, and when acquisition/launch events are treated like order conversion. It also can be late when mid-cap suppliers show delivery/margin bridge before full-year result confirmation.", "candidate_patch_scope": "canonical_archetype_rule_candidate", "production_scoring_changed": false, "shadow_weight_only": true}
```

### narrative_only_rows_jsonl

```jsonl
{"row_type": "narrative_only", "case_id": "C01_R1L126_NARRATIVE_01_073010", "symbol": "073010", "company_name": "케이에스피", "round": "R1", "loop": 126, "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "canonical_archetype_id": "C01_ORDER_BACKLOG_MARGIN_BRIDGE", "fine_archetype_id": "SHIPBUILDING_BACKLOG_SUPPLIER_MARGIN_FCF_BRIDGE_VS_PRODUCT_IDENTITY_PROXY", "reason": "source_proxy_only_no_dated_order_or_margin_bridge_for_trigger_row", "evidence_source": "https://kspvalve.tradekorea.com/company.do", "price_data_source": "Songdaiki/stock-web", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "calibration_usable": false, "dedupe_for_aggregate": false, "aggregate_group_role": "narrative_only_blocked"}
{"row_type": "narrative_only", "case_id": "C01_R1L126_NARRATIVE_02_014940", "symbol": "014940", "company_name": "오리엔탈정공", "round": "R1", "loop": 126, "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "canonical_archetype_id": "C01_ORDER_BACKLOG_MARGIN_BRIDGE", "fine_archetype_id": "SHIPBUILDING_BACKLOG_SUPPLIER_MARGIN_FCF_BRIDGE_VS_PRODUCT_IDENTITY_PROXY", "reason": "source_proxy_only_no_dated_order_or_margin_bridge_for_trigger_row", "evidence_source": "https://www.opco-omt.co.kr/mobile/eng/01_company/01.php", "price_data_source": "Songdaiki/stock-web", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "calibration_usable": false, "dedupe_for_aggregate": false, "aggregate_group_role": "narrative_only_blocked"}
```

## 9. Validation scope

```text
filename_matches_standard_v12_pattern = true
metadata_round_loop_matches_filename = true
trigger_rows_have_complete_30_90_180_MFE_MAE = true
price_source = Songdaiki/stock-web
price_basis = tradable_raw
price_adjustment_status = raw_unadjusted_marcap
forward_window_trading_days >= 180 for all representative trigger rows
representative_trigger_count = 7
new_independent_case_count = 7
reused_case_count = 0
same_archetype_new_symbol_count = 7
positive_case_count = 4
counterexample_count = 3
stage4b_overlay_count = 6
stage4c_case_count = 0
narrative_only_blocked_count = 2
current_profile_error_count = 5
hard_duplicate_count = 0
production_scoring_changed = false
shadow_weight_only = true
```

## 10. Deferred Coding Agent Handoff Prompt

```text
Do not execute during this research session.

When batch-applying v12 residual research files, ingest this file as a standard v12 result MD. Validate all row_type="trigger" rows using the complete 30/90/180D MFE/MAE fields and stock-web tradable_raw paths. Treat the proposed C01 rule only as a shadow candidate unless enough additional C01 rows confirm it:

C01_BACKLOG_SUPPLIER_MARGIN_BRIDGE_REQUIRES_DELIVERY_AND_CONVERSION_GATE_WITH_PRODUCT_IDENTITY_PROXY_BLOCK

Potential runtime effect:
- Increase C01 credit when named order/customer + backlog/delivery visibility + capacity/production route + OP margin/FCF conversion coexist.
- Keep Stage2-watch only when evidence is product identity, acquisition/launch identity, or single contract without repeat/delivery/margin evidence.
- Add local Stage4B overlay when event-premium or late confirmation creates high early MAE before the operational bridge catches up.
- Do not change production scoring directly from this file alone.
```

## 11. Next research state

```text
completed_round = R1
completed_loop = 126
selection_basis = docs/core/V12_Research_No_Repeat_Index.md
selected_priority_bucket = Priority 0 / C01 under-30 follow-up, local estimated minimum threshold crossed after this commit
round_schedule_status = coverage_index_selected
round_sector_consistency = pass

next_recommended_archetypes:
C02_POWER_GRID_DATACENTER_CAPEX_followup_new_symbols_only
C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF_followup_after_shard_recheck
C14_EV_DEMAND_SLOWDOWN_4B_4C_followup_utilization_regime
C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE_followup_counterexample
C06_HBM_MEMORY_CUSTOMER_CAPACITY_followup_new_symbols_only
```
