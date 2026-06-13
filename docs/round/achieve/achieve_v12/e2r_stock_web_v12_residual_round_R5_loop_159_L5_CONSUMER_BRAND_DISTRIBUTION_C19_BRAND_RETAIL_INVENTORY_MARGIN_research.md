# E2R Stock-Web v12 Residual Research — R5/L5/C19 loop 159

```text
completed_round = R5
completed_loop = 159
selection_basis = docs/core/V12_Research_No_Repeat_Index.md
selected_priority_bucket = Priority 2 quality-repair after session-aware P0/P1 clearing
round_schedule_status = coverage_index_selected_not_sequential
round_sector_consistency = pass
large_sector_id = L5_CONSUMER_BRAND_DISTRIBUTION
canonical_archetype_id = C19_BRAND_RETAIL_INVENTORY_MARGIN
fine_archetype_id = mixed_c19_brand_retail_inventory_margin_bridge_leaf_set
research_session = post_calibrated_sector_archetype_residual_research
production_scoring_changed = false
shadow_weight_only = true
handoff_prompt_embedded = true
handoff_prompt_executed_now = false
```

## 1. Selection memo

Original `V12_Research_No_Repeat_Index.md` shows C19 at exactly 50 representative rows, which is no longer a shortage bucket but is the thinnest Priority-2 peer together with C08. In this chat session, loops 121-158 cleared the original P0/P1 backlog and loop 158 already performed a C08 quality-repair pass. Therefore loop 159 selects C19, not to inflate a well-covered region blindly, but to add URL-backed brand/retail margin rows that separate **true margin conversion**, **inventory/SG&A drag**, **subsidiary contamination**, and **late-entry 4B exit risk**.

The selected round follows the archetype: C19 -> R5 / L5. This is not an R1-R13 sequential scheduler run.

## 2. Price source validation

```text
price_source = Songdaiki/stock-web
source_basis = FinanceData/marcap
price_basis = tradable_raw
price_adjustment_status = raw_unadjusted_marcap
calibration_shard_root = atlas/ohlcv_tradable_by_symbol_year
manifest_max_date = 2026-02-20
entry_price_rule = next tradable close after evidence date
MFE_MAE_rule = max high / min low over entry-date-inclusive 30/90/180 tradable rows
```

All rows below have 30D/90D/180D forward windows within the stock-web manifest max date. Profile checks found no entry-to-D180 corporate-action candidate overlap for the selected windows. F&F, FILA, and Brand X have historical corporate-action candidate dates in their profiles, but those dates are outside this loop's entry-to-D180 windows.

## 3. Case table

| case_id | ticker | name | evidence_date | trigger_type | label | entry_date | entry_price | MFE30/MAE30 | MFE90/MAE90 | MFE180/MAE180 | thesis_short |
|---|---:|---|---|---|---|---|---:|---:|---:|---:|---|
| C19_L159_01 | 139480 | E-Mart | 2024-02-14 | Stage4B-Watch | counterexample | 2024-02-15 | 75800 | 2.37/-9.89 | 2.37/-27.70 | 2.37/-27.70 | 2023 annual operating loss looked like a hard retail break, but the evidence was contaminated by Shinsegae Construction losses; still, actual price path punished the weak retail/affiliate mix. |
| C19_L159_02 | 139480 | E-Mart | 2025-05-12 | Stage2-Actionable | positive_with_4b_exit_guard | 2025-05-13 | 84800 | 9.08/-4.72 | 20.05/-16.63 | 20.05/-17.10 | Q1 2025 profit rebound had core-big-box/Traders and affiliate-profit bridge; path delivered 20% MFE but still required high-MAE guard. |
| C19_L159_03 | 023530 | Lotte Shopping | 2025-05-09 | Stage2-Watch | counterexample | 2025-05-12 | 75800 | 10.69/-5.01 | 10.69/-15.17 | 14.78/-17.28 | Operating profit improved on overseas operations, but sales fell and net profit base effect made the signal too mixed for C19 actionable promotion. |
| C19_L159_04 | 337930 | XEXYMIX / Brand X | 2024-08-12 | Stage2-Actionable | positive_with_4b_exit_guard | 2024-08-13 | 10780 | 10.39/-17.90 | 24.12/-53.15 | 24.12/-53.15 | Q2 sales/OP surprise and China-store inventory recognition created a valid C19 growth/margin bridge, but entry came after strong price acceleration and later MAE was severe. |
| C19_L159_05 | 081660 | FILA Holdings / Misto Holdings | 2025-03-24 | Stage2-Watch | positive_watch | 2025-03-25 | 38800 | 1.93/-13.53 | 1.93/-15.72 | 17.65/-15.72 | 2024 revenue/OP growth and capital-return upgrade supported brand-retail quality, but MFE stayed below strong rerating threshold until late in the window. |
| C19_L159_06 | 383220 | F&F | 2025-04-29 | Stage2-Watch | false_hard_4c_counterexample | 2025-04-30 | 70600 | 13.17/-4.82 | 18.27/-13.60 | 18.27/-16.57 | Domestic fashion slump and 1Q OP decline were real, but overseas defense/China renewal prevented a clean hard 4C; price path showed moderate relief before renewed drawdown. |
| C19_L159_07 | 282330 | BGF Retail | 2024-08-01 | Stage2-Watch | false_hard_4c_counterexample | 2024-08-02 | 111600 | 10.39/-4.93 | 12.01/-12.19 | 12.01/-12.19 | Q2 OP slipped due to rain and SG&A, while peak-season and product-hit offsets remained; price path did not validate an immediate hard 4C. |
| C19_L159_08 | 069960 | Hyundai Department Store | 2024-08-08 | Stage2-Watch | positive_false4c_audit | 2024-08-09 | 45450 | 10.45/-0.11 | 10.89/-8.69 | 49.61/-8.69 | Q2 net loss and OP decline looked negative, but sales still rose and the subsequent path generated large 180D MFE, making this a false hard-4C audit row. |


## 4. Interpretation

C19 is a place where the machine can be fooled by two very different masks. One mask is the **storefront mask**: sales, store count, traffic, China expansion, or overseas outlets look alive. The other is the **stockroom mask**: inventory, markdowns, SG&A, affiliate drag, and one-off losses are quietly eating the margin. The useful C19 signal is not that the shop is busy; it is that the cash register, stockroom, and margin bridge are moving in the same direction.

Key residual findings:

1. **Retail turnaround must be segmented.** E-Mart 2024 looked like a hard break at the consolidated level, but much of the damage came from Shinsegae Construction. E-Mart 2025 then showed that the core retail/Traders/affiliate bridge could recover, but even that positive row still had a near -17% 180D MAE.
2. **Brand expansion without exit discipline becomes a 4B trap.** Brand X had a genuine Q2 surprise and China-store growth narrative, but the entry came after momentum had already burned oxygen; 180D MAE of -53.15% means C19 needs an explicit late-entry exit guard.
3. **Negative retail headlines can be false 4C.** Hyundai Department Store's Q2 2024 net loss headline was followed by +49.61% 180D MFE. BGF's weather/SG&A drag similarly did not validate an immediate hard 4C.
4. **Profit growth without sales/quality breadth is only Stage2-Watch.** Lotte Shopping's operating profit jump was useful, but sales contraction and net-profit base effects made it a watch row rather than a clean actionable row.
5. **Global brand/capital-return rows require rerating speed audit.** FILA/Misto had robust annual profit and shareholder-return evidence, but forward MFE arrived slowly; this is quality support, not a Green unlock by itself.

## 5. Machine-readable trigger rows JSONL

```jsonl
{"row_type": "trigger", "version": "v12", "case_id": "C19_L159_01", "round": "R5", "loop": 159, "large_sector_id": "L5_CONSUMER_BRAND_DISTRIBUTION", "canonical_archetype_id": "C19_BRAND_RETAIL_INVENTORY_MARGIN", "fine_archetype_id": "mixed_c19_brand_retail_inventory_margin_bridge_leaf_set", "ticker": "139480", "symbol": "139480", "name": "E-Mart", "market": "KRX", "evidence_date": "2024-02-14", "evidence_url": "https://en.yna.co.kr/view/AEN20240214005800320", "evidence_family": "annual_operating_loss_construction_subsidiary_drag", "trigger_type": "Stage4B-Watch", "entry_date": "2024-02-15", "entry_price": 75800.0, "price_source": "Songdaiki/stock-web", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "MFE_30D_pct": 2.37, "MAE_30D_pct": -9.89, "MFE_90D_pct": 2.37, "MAE_90D_pct": -27.7, "MFE_180D_pct": 2.37, "MAE_180D_pct": -27.7, "peak_30D_date": "2024-02-15", "trough_30D_date": "2024-03-26", "peak_90D_date": "2024-02-15", "trough_90D_date": "2024-06-27", "peak_180D_date": "2024-02-15", "trough_180D_date": "2024-06-27", "calibration_usable": true, "aggregate_representative": true, "case_label": "counterexample", "novelty": "new_symbol_or_new_trigger_family_vs_session_loop_121_158", "corporate_action_window_status": "no_entry_to_D180_overlap_in_checked_profile_or_profile_candidate_dates_pre_window", "thesis": "2023 annual operating loss looked like a hard retail break, but the evidence was contaminated by Shinsegae Construction losses; still, actual price path punished the weak retail/affiliate mix."}
{"row_type": "trigger", "version": "v12", "case_id": "C19_L159_02", "round": "R5", "loop": 159, "large_sector_id": "L5_CONSUMER_BRAND_DISTRIBUTION", "canonical_archetype_id": "C19_BRAND_RETAIL_INVENTORY_MARGIN", "fine_archetype_id": "mixed_c19_brand_retail_inventory_margin_bridge_leaf_set", "ticker": "139480", "symbol": "139480", "name": "E-Mart", "market": "KRX", "evidence_date": "2025-05-12", "evidence_url": "https://en.yna.co.kr/view/AEN20250512004351320", "evidence_family": "core_big_box_traders_turnaround_affiliate_profit", "trigger_type": "Stage2-Actionable", "entry_date": "2025-05-13", "entry_price": 84800.0, "price_source": "Songdaiki/stock-web", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "MFE_30D_pct": 9.08, "MAE_30D_pct": -4.72, "MFE_90D_pct": 20.05, "MAE_90D_pct": -16.63, "MFE_180D_pct": 20.05, "MAE_180D_pct": -17.1, "peak_30D_date": "2025-05-30", "trough_30D_date": "2025-06-18", "peak_90D_date": "2025-07-09", "trough_90D_date": "2025-09-02", "peak_180D_date": "2025-07-09", "trough_180D_date": "2025-11-05", "calibration_usable": true, "aggregate_representative": true, "case_label": "positive_with_4b_exit_guard", "novelty": "new_symbol_or_new_trigger_family_vs_session_loop_121_158", "corporate_action_window_status": "no_entry_to_D180_overlap_in_checked_profile_or_profile_candidate_dates_pre_window", "thesis": "Q1 2025 profit rebound had core-big-box/Traders and affiliate-profit bridge; path delivered 20% MFE but still required high-MAE guard."}
{"row_type": "trigger", "version": "v12", "case_id": "C19_L159_03", "round": "R5", "loop": 159, "large_sector_id": "L5_CONSUMER_BRAND_DISTRIBUTION", "canonical_archetype_id": "C19_BRAND_RETAIL_INVENTORY_MARGIN", "fine_archetype_id": "mixed_c19_brand_retail_inventory_margin_bridge_leaf_set", "ticker": "023530", "symbol": "023530", "name": "Lotte Shopping", "market": "KRX", "evidence_date": "2025-05-09", "evidence_url": "https://en.yna.co.kr/view/AEN20250509002151320", "evidence_family": "overseas_mall_profit_turnaround_sales_decline_base_effect", "trigger_type": "Stage2-Watch", "entry_date": "2025-05-12", "entry_price": 75800.0, "price_source": "Songdaiki/stock-web", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "MFE_30D_pct": 10.69, "MAE_30D_pct": -5.01, "MFE_90D_pct": 10.69, "MAE_90D_pct": -15.17, "MFE_180D_pct": 14.78, "MAE_180D_pct": -17.28, "peak_30D_date": "2025-06-09", "trough_30D_date": "2025-06-18", "peak_90D_date": "2025-06-09", "trough_90D_date": "2025-09-03", "peak_180D_date": "2026-02-02", "trough_180D_date": "2025-11-04", "calibration_usable": true, "aggregate_representative": true, "case_label": "counterexample", "novelty": "new_symbol_or_new_trigger_family_vs_session_loop_121_158", "corporate_action_window_status": "no_entry_to_D180_overlap_in_checked_profile_or_profile_candidate_dates_pre_window", "thesis": "Operating profit improved on overseas operations, but sales fell and net profit base effect made the signal too mixed for C19 actionable promotion."}
{"row_type": "trigger", "version": "v12", "case_id": "C19_L159_04", "round": "R5", "loop": 159, "large_sector_id": "L5_CONSUMER_BRAND_DISTRIBUTION", "canonical_archetype_id": "C19_BRAND_RETAIL_INVENTORY_MARGIN", "fine_archetype_id": "mixed_c19_brand_retail_inventory_margin_bridge_leaf_set", "ticker": "337930", "symbol": "337930", "name": "XEXYMIX / Brand X", "market": "KRX", "evidence_date": "2024-08-12", "evidence_url": "https://view.asiae.co.kr/en/article/2024080916105531627", "evidence_family": "q2_surprise_overseas_expansion_inventory_recognition", "trigger_type": "Stage2-Actionable", "entry_date": "2024-08-13", "entry_price": 10780.0, "price_source": "Songdaiki/stock-web", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "MFE_30D_pct": 10.39, "MAE_30D_pct": -17.9, "MFE_90D_pct": 24.12, "MAE_90D_pct": -53.15, "MFE_180D_pct": 24.12, "MAE_180D_pct": -53.15, "peak_30D_date": "2024-08-28", "trough_30D_date": "2024-09-06", "peak_90D_date": "2024-10-07", "trough_90D_date": "2024-12-06", "peak_180D_date": "2024-10-07", "trough_180D_date": "2024-12-06", "calibration_usable": true, "aggregate_representative": true, "case_label": "positive_with_4b_exit_guard", "novelty": "new_symbol_or_new_trigger_family_vs_session_loop_121_158", "corporate_action_window_status": "no_entry_to_D180_overlap_in_checked_profile_or_profile_candidate_dates_pre_window", "thesis": "Q2 sales/OP surprise and China-store inventory recognition created a valid C19 growth/margin bridge, but entry came after strong price acceleration and later MAE was severe."}
{"row_type": "trigger", "version": "v12", "case_id": "C19_L159_05", "round": "R5", "loop": 159, "large_sector_id": "L5_CONSUMER_BRAND_DISTRIBUTION", "canonical_archetype_id": "C19_BRAND_RETAIL_INVENTORY_MARGIN", "fine_archetype_id": "mixed_c19_brand_retail_inventory_margin_bridge_leaf_set", "ticker": "081660", "symbol": "081660", "name": "FILA Holdings / Misto Holdings", "market": "KRX", "evidence_date": "2025-03-24", "evidence_url": "https://www.mistoholdings.com/newsroom/eng/press/detail/110.do", "evidence_family": "global_brand_profit_recovery_capital_return", "trigger_type": "Stage2-Watch", "entry_date": "2025-03-25", "entry_price": 38800.0, "price_source": "Songdaiki/stock-web", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "MFE_30D_pct": 1.93, "MAE_30D_pct": -13.53, "MFE_90D_pct": 1.93, "MAE_90D_pct": -15.72, "MFE_180D_pct": 17.65, "MAE_180D_pct": -15.72, "peak_30D_date": "2025-03-25", "trough_30D_date": "2025-04-09", "peak_90D_date": "2025-03-25", "trough_90D_date": "2025-06-16", "peak_180D_date": "2025-12-05", "trough_180D_date": "2025-06-16", "calibration_usable": true, "aggregate_representative": true, "case_label": "positive_watch", "novelty": "new_symbol_or_new_trigger_family_vs_session_loop_121_158", "corporate_action_window_status": "no_entry_to_D180_overlap_in_checked_profile_or_profile_candidate_dates_pre_window", "thesis": "2024 revenue/OP growth and capital-return upgrade supported brand-retail quality, but MFE stayed below strong rerating threshold until late in the window."}
{"row_type": "trigger", "version": "v12", "case_id": "C19_L159_06", "round": "R5", "loop": 159, "large_sector_id": "L5_CONSUMER_BRAND_DISTRIBUTION", "canonical_archetype_id": "C19_BRAND_RETAIL_INVENTORY_MARGIN", "fine_archetype_id": "mixed_c19_brand_retail_inventory_margin_bridge_leaf_set", "ticker": "383220", "symbol": "383220", "name": "F&F", "market": "KRX", "evidence_date": "2025-04-29", "evidence_url": "https://en.topdaily.kr/articles/6256", "evidence_family": "domestic_slump_overseas_defense_china_store_renewal", "trigger_type": "Stage2-Watch", "entry_date": "2025-04-30", "entry_price": 70600.0, "price_source": "Songdaiki/stock-web", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "MFE_30D_pct": 13.17, "MAE_30D_pct": -4.82, "MFE_90D_pct": 18.27, "MAE_90D_pct": -13.6, "MFE_180D_pct": 18.27, "MAE_180D_pct": -16.57, "peak_30D_date": "2025-06-12", "trough_30D_date": "2025-05-19", "peak_90D_date": "2025-07-08", "trough_90D_date": "2025-08-19", "peak_180D_date": "2025-07-08", "trough_180D_date": "2025-11-05", "calibration_usable": true, "aggregate_representative": true, "case_label": "false_hard_4c_counterexample", "novelty": "new_symbol_or_new_trigger_family_vs_session_loop_121_158", "corporate_action_window_status": "no_entry_to_D180_overlap_in_checked_profile_or_profile_candidate_dates_pre_window", "thesis": "Domestic fashion slump and 1Q OP decline were real, but overseas defense/China renewal prevented a clean hard 4C; price path showed moderate relief before renewed drawdown."}
{"row_type": "trigger", "version": "v12", "case_id": "C19_L159_07", "round": "R5", "loop": 159, "large_sector_id": "L5_CONSUMER_BRAND_DISTRIBUTION", "canonical_archetype_id": "C19_BRAND_RETAIL_INVENTORY_MARGIN", "fine_archetype_id": "mixed_c19_brand_retail_inventory_margin_bridge_leaf_set", "ticker": "282330", "symbol": "282330", "name": "BGF Retail", "market": "KRX", "evidence_date": "2024-08-01", "evidence_url": "https://www.asiae.co.kr/en/article/2024080115312444899", "evidence_family": "weather_sga_margin_drag_peak_season_offset", "trigger_type": "Stage2-Watch", "entry_date": "2024-08-02", "entry_price": 111600.0, "price_source": "Songdaiki/stock-web", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "MFE_30D_pct": 10.39, "MAE_30D_pct": -4.93, "MFE_90D_pct": 12.01, "MAE_90D_pct": -12.19, "MFE_180D_pct": 12.01, "MAE_180D_pct": -12.19, "peak_30D_date": "2024-09-05", "trough_30D_date": "2024-08-02", "peak_90D_date": "2024-09-25", "trough_90D_date": "2024-12-09", "peak_180D_date": "2024-09-25", "trough_180D_date": "2024-12-09", "calibration_usable": true, "aggregate_representative": true, "case_label": "false_hard_4c_counterexample", "novelty": "new_symbol_or_new_trigger_family_vs_session_loop_121_158", "corporate_action_window_status": "no_entry_to_D180_overlap_in_checked_profile_or_profile_candidate_dates_pre_window", "thesis": "Q2 OP slipped due to rain and SG&A, while peak-season and product-hit offsets remained; price path did not validate an immediate hard 4C."}
{"row_type": "trigger", "version": "v12", "case_id": "C19_L159_08", "round": "R5", "loop": 159, "large_sector_id": "L5_CONSUMER_BRAND_DISTRIBUTION", "canonical_archetype_id": "C19_BRAND_RETAIL_INVENTORY_MARGIN", "fine_archetype_id": "mixed_c19_brand_retail_inventory_margin_bridge_leaf_set", "ticker": "069960", "symbol": "069960", "name": "Hyundai Department Store", "market": "KRX", "evidence_date": "2024-08-08", "evidence_url": "https://en.yna.co.kr/view/AEN20240808006300320", "evidence_family": "q2_net_loss_op_decline_sales_growth_false_4c", "trigger_type": "Stage2-Watch", "entry_date": "2024-08-09", "entry_price": 45450.0, "price_source": "Songdaiki/stock-web", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "MFE_30D_pct": 10.45, "MAE_30D_pct": -0.11, "MFE_90D_pct": 10.89, "MAE_90D_pct": -8.69, "MFE_180D_pct": 49.61, "MAE_180D_pct": -8.69, "peak_30D_date": "2024-09-13", "trough_30D_date": "2024-08-09", "peak_90D_date": "2024-09-27", "trough_90D_date": "2024-11-15", "peak_180D_date": "2025-05-12", "trough_180D_date": "2024-11-15", "calibration_usable": true, "aggregate_representative": true, "case_label": "positive_false4c_audit", "novelty": "new_symbol_or_new_trigger_family_vs_session_loop_121_158", "corporate_action_window_status": "no_entry_to_D180_overlap_in_checked_profile_or_profile_candidate_dates_pre_window", "thesis": "Q2 net loss and OP decline looked negative, but sales still rose and the subsequent path generated large 180D MFE, making this a false hard-4C audit row."}
```

## 6. Raw component score simulation JSONL

These are shadow-only stress-test scores, not production patches.

```jsonl
{"row_type": "score_simulation", "case_id": "C19_L159_01", "ticker": "139480", "current_default_profile_proxy": "e2r_2_1_stock_web_calibrated", "shadow_only": true, "eps_fcf_explosion": 36, "earnings_visibility": 32, "pricing_power": 35, "mispricing": 55, "valuation_rerating": 28, "capital_allocation": 38, "info_confidence": 76, "c19_bridge": 30, "simulated_total": 57.0, "current_profile_error": "too_hard_or_misclassified_subsidiary_drag_risk"}
{"row_type": "score_simulation", "case_id": "C19_L159_02", "ticker": "139480", "current_default_profile_proxy": "e2r_2_1_stock_web_calibrated", "shadow_only": true, "eps_fcf_explosion": 67, "earnings_visibility": 61, "pricing_power": 58, "mispricing": 63, "valuation_rerating": 52, "capital_allocation": 50, "info_confidence": 82, "c19_bridge": 69, "simulated_total": 76.0, "current_profile_error": "positive_but_high_mae_requires_staged_entry"}
{"row_type": "score_simulation", "case_id": "C19_L159_03", "ticker": "023530", "current_default_profile_proxy": "e2r_2_1_stock_web_calibrated", "shadow_only": true, "eps_fcf_explosion": 56, "earnings_visibility": 49, "pricing_power": 44, "mispricing": 59, "valuation_rerating": 42, "capital_allocation": 45, "info_confidence": 80, "c19_bridge": 48, "simulated_total": 68.0, "current_profile_error": "op_profit_growth_without_sales_or_net_quality_overpromotes"}
{"row_type": "score_simulation", "case_id": "C19_L159_04", "ticker": "337930", "current_default_profile_proxy": "e2r_2_1_stock_web_calibrated", "shadow_only": true, "eps_fcf_explosion": 78, "earnings_visibility": 63, "pricing_power": 67, "mispricing": 61, "valuation_rerating": 38, "capital_allocation": 45, "info_confidence": 78, "c19_bridge": 74, "simulated_total": 79.0, "current_profile_error": "late_entry_after_brand_momentum_needs_4b_exit_guard"}
{"row_type": "score_simulation", "case_id": "C19_L159_05", "ticker": "081660", "current_default_profile_proxy": "e2r_2_1_stock_web_calibrated", "shadow_only": true, "eps_fcf_explosion": 62, "earnings_visibility": 57, "pricing_power": 59, "mispricing": 58, "valuation_rerating": 50, "capital_allocation": 77, "info_confidence": 84, "c19_bridge": 62, "simulated_total": 74.0, "current_profile_error": "capital_return_quality_but_not_fast_rerating"}
{"row_type": "score_simulation", "case_id": "C19_L159_06", "ticker": "383220", "current_default_profile_proxy": "e2r_2_1_stock_web_calibrated", "shadow_only": true, "eps_fcf_explosion": 48, "earnings_visibility": 45, "pricing_power": 58, "mispricing": 60, "valuation_rerating": 47, "capital_allocation": 48, "info_confidence": 78, "c19_bridge": 54, "simulated_total": 69.0, "current_profile_error": "domestic_slump_not_hard4c_when_overseas_defense_exists"}
{"row_type": "score_simulation", "case_id": "C19_L159_07", "ticker": "282330", "current_default_profile_proxy": "e2r_2_1_stock_web_calibrated", "shadow_only": true, "eps_fcf_explosion": 44, "earnings_visibility": 43, "pricing_power": 46, "mispricing": 55, "valuation_rerating": 44, "capital_allocation": 42, "info_confidence": 76, "c19_bridge": 42, "simulated_total": 63.0, "current_profile_error": "weather_sga_drag_should_stay_watch_not_4c"}
{"row_type": "score_simulation", "case_id": "C19_L159_08", "ticker": "069960", "current_default_profile_proxy": "e2r_2_1_stock_web_calibrated", "shadow_only": true, "eps_fcf_explosion": 49, "earnings_visibility": 46, "pricing_power": 52, "mispricing": 68, "valuation_rerating": 60, "capital_allocation": 51, "info_confidence": 76, "c19_bridge": 50, "simulated_total": 71.0, "current_profile_error": "net_loss_headline_false4c_when_sales_and_retail_asset_value_survive"}
```

## 7. Aggregate JSON

```json
{
  "row_type": "aggregate",
  "round": "R5",
  "loop": 159,
  "large_sector_id": "L5_CONSUMER_BRAND_DISTRIBUTION",
  "canonical_archetype_id": "C19_BRAND_RETAIL_INVENTORY_MARGIN",
  "new_independent_case_count": 8,
  "usable_trigger_row_count": 8,
  "representative_trigger_count": 8,
  "positive_case_count": 4,
  "counterexample_count": 4,
  "stage4b_watch_or_overlay_count": 5,
  "stage4c_or_false4c_audit_count": 3,
  "current_profile_error_count": 6,
  "index_baseline_coverage_before": "C19 rows 50",
  "index_baseline_coverage_after_if_accepted": "C19 rows 58",
  "selection_basis": "docs/core/V12_Research_No_Repeat_Index.md",
  "selected_priority_bucket": "Priority 2 quality-repair after session-aware P0/P1 clearing",
  "do_not_propose_new_weight_delta": false,
  "rule_candidate": "C19_INVENTORY_MARGIN_RETAIL_SUBSIDIARY_AND_EXIT_GATE_V1"
}
```

## 8. Shadow rule candidate

```json
{
  "row_type": "shadow_rule_candidate",
  "round": "R5",
  "loop": 159,
  "large_sector_id": "L5_CONSUMER_BRAND_DISTRIBUTION",
  "canonical_archetype_id": "C19_BRAND_RETAIL_INVENTORY_MARGIN",
  "rule_candidate_id": "C19_INVENTORY_MARGIN_RETAIL_SUBSIDIARY_AND_EXIT_GATE_V1",
  "production_scoring_changed": false,
  "shadow_weight_only": true,
  "positive_gate": [
    "brand_or_retail_revenue_growth_is_not_enough",
    "require_margin_or_operating_profit_bridge",
    "require_inventory_markdown_or_sga_drag_not_worsening",
    "if_consolidated_loss_is_subsidiary_contaminated_then_do_not_auto_hard_4c",
    "if_strong_brand_momentum_entry_has_MAE90_below_minus_20_then_apply_local_4b_exit_guard"
  ],
  "block_or_watch_gate": [
    "sales_growth_with_op_margin_deterioration",
    "qoq_or_yoy_profit_drop_due_to_sga_inventory_weather_without_recovery_confirmation",
    "operating_profit_growth_but_sales_decline_and_base_effect_net_profit",
    "late_report_after_price_acceleration_without_inventory_or_reorder_follow_through"
  ],
  "expected_profile_effect": "Improve C19 Stage2/4B/4C routing by separating retail-margin conversion from consolidated-subsidiary noise and late brand-momentum blowoff."
}
```

## 9. Residual contribution summary

```text
new_axis_proposed = c19_inventory_margin_retail_subsidiary_and_exit_gate
existing_axis_strengthened = price_only_blowoff_blocks_positive_stage|full_4b_requires_non_price_evidence|hard_4c_thesis_break_routes_to_4c_should_not_fire_on_headline_loss_alone
existing_axis_weakened = none
current_profile_error_count = 6
positive_case_count = 4
counterexample_count = 4
4B_watch_or_overlay_count = 5
4C_or_false4C_audit_count = 3
auto_selected_coverage_gap = index baseline C19 rows 50 -> 58 if accepted
```

## 10. Deferred Coding Agent Handoff Prompt

```text
Do not execute during research. Later coding-agent task:

Read this MD plus the v12 batch corpus. Ingest only rows with calibration_usable=true and complete entry_date, entry_price, trigger_type, MFE_30D_pct, MAE_30D_pct, MFE_90D_pct, MAE_90D_pct, MFE_180D_pct, MAE_180D_pct, large_sector_id, canonical_archetype_id. Deduplicate by canonical_archetype_id + ticker + trigger_type + entry_date. Consider a shadow-only C19 rule candidate:
C19_INVENTORY_MARGIN_RETAIL_SUBSIDIARY_AND_EXIT_GATE_V1.

Do not loosen Stage3-Green. Do not apply a broad consumer-sector boost. Patch only if the full v12 corpus confirms that C19 false positives are reduced by requiring a margin/inventory/SG&A bridge and by separating consolidated subsidiary contamination from true retail-margin thesis breaks.
```

## 11. Next research state

```text
completed_round = R5
completed_loop = 159
selection_basis = docs/core/V12_Research_No_Repeat_Index.md
selected_priority_bucket = Priority 2 quality-repair after session-aware P0/P1 clearing
next_recommended_archetypes = C19_BRAND_RETAIL_INVENTORY_MARGIN|C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG|C22_INSURANCE_RATE_CYCLE_RESERVE|C13_BATTERY_JV_UTILIZATION_AMPC_IRA|R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL
round_schedule_status = coverage_index_selected_not_sequential
round_sector_consistency = pass
```
