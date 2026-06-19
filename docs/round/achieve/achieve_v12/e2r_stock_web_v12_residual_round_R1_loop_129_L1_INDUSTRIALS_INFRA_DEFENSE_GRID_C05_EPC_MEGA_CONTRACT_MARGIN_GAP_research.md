# E2R v12 Residual Research — R1 / C05 EPC Mega Contract Margin Gap / Loop 129

## 0. Metadata

```text
selected_round: R1
selected_loop: 129
selection_basis: docs/core/V12_Research_No_Repeat_Index.md
selected_priority_bucket: Priority 1 balance/quality repair — C05 margin/working-capital failure, large EPC top-symbol cluster, direct URL/MFE-MAE repair
round_schedule_status: coverage_index_selected
round_sector_consistency: pass
large_sector_id: L1_INDUSTRIALS_INFRA_DEFENSE_GRID
canonical_archetype_id: C05_EPC_MEGA_CONTRACT_MARGIN_GAP
fine_archetype_id: LARGE_EPC_CONTRACT_MARGIN_COST_RATE_BRIDGE
research_session: post_calibrated_sector_archetype_residual_research
mode: historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12
price_source: Songdaiki/stock-web
price_basis: tradable_raw
price_adjustment_status: raw_unadjusted_marcap
stock_web_manifest_max_date: 2026-02-20
production_scoring_changed: false
shadow_weight_only: true
```

Output filename:

```text
e2r_stock_web_v12_residual_round_R1_loop_129_L1_INDUSTRIALS_INFRA_DEFENSE_GRID_C05_EPC_MEGA_CONTRACT_MARGIN_GAP_research.md
```

## 1. Selection rationale / No-Repeat check

`V12_Research_No_Repeat_Index.md` shows that C01~C32 are above the old 30/50/80 row fill targets. The next priority is quality repair: direct URL/proxy reduction, complete 30/90/180D price fields, and balance repair. C05 is explicitly listed in Priority 1 with 180 rows, 54 symbols, positive/counter 29/39, 4B/4C 23/10, and top symbols including `028050`, `006360`, `000720`, `047040`, and `375500`.

The previous local C05 loop 128 deliberately avoided the top-symbol cluster and used small/mid EPC and public-construction rows. This loop returns to the C05 top-symbol cluster, but every row uses a new symbol/date/evidence-family combination relative to loop 128.

Hard duplicate key used:

```text
canonical_archetype_id + symbol + trigger_type + entry_date + evidence_family
```

## 2. Case matrix

| case_id | symbol | company | trigger_type | trigger_date | entry_date | entry_price | MFE_180D_pct | MAE_180D_pct | outcome |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| C05_L129_000720_20230626_STAGE2A | 000720 | 현대건설 | Stage2-Actionable | 2023-06-26 | 2023-06-26 | 40800.00 | 8.82 | -23.53 | counterexample_high_mae_contract_headline |
| C05_L129_028050_20240403_STAGE2A | 028050 | 삼성E&A | Stage2-Actionable | 2024-04-03 | 2024-04-03 | 25300.00 | 15.81 | -35.57 | counterexample_high_mae_delayed_margin_conversion |
| C05_L129_006360_20240403_STAGE3Y | 006360 | GS건설 | Stage3-Yellow | 2024-04-03 | 2024-04-03 | 15630.00 | 39.16 | -10.17 | positive_but_green_requires_cost_and_quality_recovery_confirmation |
| C05_L129_028260_20241211_STAGE3Y | 028260 | 삼성물산 | Stage3-Yellow | 2024-12-11 | 2024-12-11 | 116500.00 | 62.15 | -7.21 | positive_large_epc_order_with_clean_drawdown_profile |
| C05_L129_375500_20241031_STAGE3G | 375500 | DL이앤씨 | Stage3-Green | 2024-10-31 | 2024-10-31 | 30900.00 | 93.20 | -5.18 | positive_margin_bridge_case |
| C05_L129_047040_20250526_STAGE3Y | 047040 | 대우건설 | Stage3-Yellow | 2025-05-26 | 2025-05-26 | 4025.00 | 99.75 | -17.52 | positive_but_high_90D_MAE_and_long_execution_yellow_not_green |

## 3. Evidence summary

- Hyundai E&C (`000720`) was awarded Packages 1 & 4 for the SATORP/Amiral petrochemical expansion. The evidence is a direct company release with named project, EPC packages, and specific facility scope. The price path, however, peaked on the entry day and then carried a -23.53% 180D MAE, so contract size alone should not open Green.
- Samsung E&A (`028050`) announced approximately USD 6bn Fadhili Gas Increment Program contracts with Aramco, including Package #1 Gas Treatment and Package #4 Utilities/Offsites and full EPC execution. The row is direct and strong at Stage2, but the -35.57% 180D MAE shows that C05 Green requires explicit margin/EPS/execution bridge beyond order size.
- GS E&C (`006360`) had a Fadhili sulfur recovery unit contract, reported as USD 1.22bn and roughly 41 months in duration. The price path was positive, but prior cost/quality overhang means the current profile should keep a Green cap until cost-rate and quality trust recovery is confirmed.
- Samsung C&T (`028260`) secured a USD 2.84bn Qatar desalination and combined-cycle power EPC contract. This row has a clean 180D MFE/MAE profile and a direct project role, but project completion is expected in 2029, so the proper classification is Yellow-to-Green only after margin execution evidence.
- DL E&C (`375500`) is the cleanest margin-bridge row: Q3 2024 showed operating-profit rebound, cost-rate improvement, selective order strategy, and subsequent strong MFE with shallow MAE.
- Daewoo E&C (`047040`) signed a USD 784mn Turkmenistan fertilizer plant final contract equal to roughly 10% of 2024 sales. It is positive but still a 37-month execution project, and the 90D/180D drawdown means Green should wait for ground-breaking, cost-rate, and revenue conversion evidence.

## 4. Actual Stock-Web entry OHLC rows

| symbol | entry_date | o | h | l | c | v | m | price_shard_path |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 000720 | 2023-06-26 | 42700.00 | 44400.00 | 40400.00 | 40800.00 | 8540029 | KOSPI | atlas/ohlcv_tradable_by_symbol_year/000/000720/<year>.csv |
| 028050 | 2024-04-03 | 25000.00 | 26750.00 | 25000.00 | 25300.00 | 5117106 | KOSPI | atlas/ohlcv_tradable_by_symbol_year/028/028050/<year>.csv |
| 006360 | 2024-04-03 | 15500.00 | 16550.00 | 15400.00 | 15630.00 | 4065591 | KOSPI | atlas/ohlcv_tradable_by_symbol_year/006/006360/<year>.csv |
| 028260 | 2024-12-11 | 115800.00 | 116600.00 | 114700.00 | 116500.00 | 256239 | KOSPI | atlas/ohlcv_tradable_by_symbol_year/028/028260/<year>.csv |
| 375500 | 2024-10-31 | 30750.00 | 30900.00 | 30050.00 | 30900.00 | 98638 | KOSPI | atlas/ohlcv_tradable_by_symbol_year/375/375500/<year>.csv |
| 047040 | 2025-05-26 | 4045.00 | 4045.00 | 3875.00 | 4025.00 | 2742868 | KOSPI | atlas/ohlcv_tradable_by_symbol_year/047/047040/<year>.csv |

## 5. 30D / 90D / 180D MFE-MAE and peak/drawdown

| trigger_id | symbol | entry_date | MFE_30D_pct | MAE_30D_pct | MFE_90D_pct | MAE_90D_pct | MFE_180D_pct | MAE_180D_pct | peak_180D | trough_180D | drawdown_after_peak_pct |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| C05_L129_T001_000720_STAGE2A_20230626 | 000720 | 2023-06-26 | 8.82 | -15.32 | 8.82 | -18.50 | 8.82 | -23.53 | 2023-06-26 | 2024-01-25 | -29.73 |
| C05_L129_T002_028050_STAGE2A_20240403 | 028050 | 2024-04-03 | 6.72 | -5.34 | 15.81 | -14.62 | 15.81 | -35.57 | 2024-07-30 | 2024-12-09 | -44.37 |
| C05_L129_T003_006360_STAGE3Y_20240403 | 006360 | 2024-04-03 | 6.97 | -10.17 | 30.52 | -10.17 | 39.16 | -10.17 | 2024-08-27 | 2024-04-19 | -22.48 |
| C05_L129_T004_028260_STAGE3Y_20241211 | 028260 | 2024-12-11 | 6.35 | -3.52 | 17.42 | -7.21 | 62.15 | -7.21 | 2025-07-17 | 2025-04-09 | -17.79 |
| C05_L129_T005_375500_STAGE3G_20241031 | 375500 | 2024-10-31 | 12.62 | -5.18 | 51.94 | -5.18 | 93.20 | -5.18 | 2025-06-26 | 2024-11-13 | -22.78 |
| C05_L129_T006_047040_STAGE3Y_20250526 | 047040 | 2025-05-26 | 19.38 | -3.73 | 19.38 | -12.05 | 99.75 | -17.52 | 2026-02-12 | 2025-11-07 | -12.06 |

## 6. Current profile residual diagnosis

The current calibrated profile already blocks price-only blowoff and requires non-price evidence for full 4B, but C05 still has a different residual problem: **contract amount is often mistaken for margin visibility**.

In C05, a mega EPC contract is a signed work queue, not automatically a profit pool. The contract can be the warehouse full of materials, while margin/FCF is the finished product leaving the dock. If cost-to-complete, working capital, cost-rate, claims, execution schedule, and guidance are not visible, the warehouse can still become a margin trap.

Observed residuals:

1. `000720` and `028050` show that direct mega-contract evidence can still be poor 180D alignment if it lacks immediate cost-rate or margin bridge.
2. `006360` and `047040` show that a valid contract row may still need a Green cap because legacy quality/cost or long execution duration can keep MAE material.
3. `028260` and `375500` show what the profile should reward: direct EPC role plus either execution track record or explicit margin/cost-rate improvement.

## 7. Proposed shadow rule candidate

```text
new_axis_proposed: C05_CONTRACT_TO_MARGIN_COST_RATE_CASH_BRIDGE_GATE
production_scoring_changed: false
shadow_weight_only: true
```

Rule candidate:

```text
For C05_EPC_MEGA_CONTRACT_MARGIN_GAP, contract amount/customer/project scope can open Stage2 evidence, but Stage2-Actionable requires at least two of:
  1. named customer/project and signed EPC contract,
  2. contract value material to revenue/backlog,
  3. explicit cost-rate/margin bridge,
  4. order-to-revenue timing with near-term recognition,
  5. working-capital or claims risk controlled,
  6. company-level earnings/revision/OP bridge.

Stage3-Green should require a margin/cost-rate/earnings bridge, not merely a mega contract headline. If the evidence is contract-only and 90D/180D MAE is deep, keep the row at Stage2 or Stage2-Actionable with local 4B watch.
```

Suggested shadow weight direction:

```text
before: EPS/Visibility/Bottleneck/Mispricing/Valuation/Capital/Info = 18/22/10/12/10/8/20
after:  EPS/Visibility/Bottleneck/Mispricing/Valuation/Capital/Info = 17/25/9/10/8/9/22
delta:  -1/+3/-1/-2/-2/+1/+2
```

Interpretation:

- Shift weight from raw contract size / valuation rerating into visibility and information confidence.
- Give a modest capital/cash discipline boost only when working-capital or cost-rate evidence exists.
- Do not relax Stage3-Green thresholds; make C05 Green slower but cleaner.

## 8. Trigger JSONL

```jsonl
{"MAE_180D_pct": -23.53, "MAE_180D_trough_date": "2024-01-25", "MAE_180D_trough_low": 31200.0, "MAE_30D_pct": -15.32, "MAE_30D_trough_date": "2023-07-07", "MAE_90D_pct": -18.5, "MAE_90D_trough_date": "2023-10-31", "MFE_180D_pct": 8.82, "MFE_180D_peak_date": "2023-06-26", "MFE_180D_peak_high": 44400.0, "MFE_30D_pct": 8.82, "MFE_30D_peak_date": "2023-06-26", "MFE_90D_pct": 8.82, "MFE_90D_peak_date": "2023-06-26", "calibration_block_reasons": [], "calibration_usable": true, "canonical_archetype_id": "C05_EPC_MEGA_CONTRACT_MARGIN_GAP", "case_id": "C05_L129_000720_20230626_STAGE2A", "company_name": "Hyundai E&C", "company_name_kr": "현대건설", "corporate_action_window_status": "clean_180D_from_profile_candidates_or_post_2022_listing_check", "current_profile_verdict": "likely_overcredits_contract_amount_as_actionable", "dedupe_for_aggregate": true, "do_not_count_as_new_case": false, "drawdown_after_peak_pct": -29.73, "drawdown_after_peak_trough_date": "2024-01-25", "entry_date": "2023-06-26", "entry_ohlc": {"a": 359525992200.0, "c": 40800.0, "d": "2023-06-26", "h": 44400.0, "l": 40400.0, "m": "KOSPI", "mc": 4543315212000.0, "o": 42700.0, "s": 111355765, "v": 8540029.0}, "entry_price": 40800.0, "evidence_available_at_that_date": true, "evidence_family": "amiral_mega_epc_contract_without_margin_conversion_bridge", "evidence_source": "https://www.hdec.kr/en/newsroom/news_view.aspx?NewsListType=news_list&NewsSeq=805&NewsType=FUTURE", "evidence_source_note": "HDEC announced EPC packages 1 and 4 for the SATORP/Amiral petrochemical expansion in Jubail, including a mixed feed cracker and utilities/interconnecting facilities.", "evidence_timing_rule": "same_day_close_if_tradable_or_first_tradable_date_after_publication", "fine_archetype_id": "LARGE_EPC_CONTRACT_MARGIN_COST_RATE_BRIDGE", "independent_evidence_weight": 1.0, "is_new_independent_case": true, "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "loop": 129, "price_adjustment_status": "raw_unadjusted_marcap", "price_basis": "tradable_raw", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_data_source": "Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/000/000720/<year>.csv", "profile_path": "atlas/symbol_profiles/000/000720.json", "reuse_reason": null, "round": "R1", "row_type": "trigger", "same_entry_group_id": "C05_EPC_MEGA_CONTRACT_MARGIN_GAP|000720|Stage2-Actionable|2023-06-26|amiral_mega_epc_contract_without_margin_conversion_bridge", "shadow_rule_verdict": "Stage2_or_Stage2A_but_Green_blocked_until_cost_rate_margin_bridge", "source_proxy_only": false, "stage2_evidence_fields": ["signed_EPC_packages", "named_client_project", "mega_contract_scale"], "stage3_evidence_fields": ["no_as_of_margin_revision_bridge", "long_execution_duration"], "stage4b_evidence_fields": ["deep_180D_MAE_after_entry", "same_day_peak_then_deterioration"], "stage4c_evidence_fields": [], "stock_web_manifest_max_date": "2026-02-20", "symbol": "000720", "trigger_date": "2023-06-26", "trigger_id": "C05_L129_T001_000720_STAGE2A_20230626", "trigger_outcome_label": "counterexample_high_mae_contract_headline", "trigger_type": "Stage2-Actionable"}
{"MAE_180D_pct": -35.57, "MAE_180D_trough_date": "2024-12-09", "MAE_180D_trough_low": 16300.0, "MAE_30D_pct": -5.34, "MAE_30D_trough_date": "2024-04-19", "MAE_90D_pct": -14.62, "MAE_90D_trough_date": "2024-06-18", "MFE_180D_pct": 15.81, "MFE_180D_peak_date": "2024-07-30", "MFE_180D_peak_high": 29300.0, "MFE_30D_pct": 6.72, "MFE_30D_peak_date": "2024-04-30", "MFE_90D_pct": 15.81, "MFE_90D_peak_date": "2024-07-30", "calibration_block_reasons": [], "calibration_usable": true, "canonical_archetype_id": "C05_EPC_MEGA_CONTRACT_MARGIN_GAP", "case_id": "C05_L129_028050_20240403_STAGE2A", "company_name": "Samsung E&A", "company_name_kr": "삼성E&A", "corporate_action_window_status": "clean_180D_from_profile_candidates_or_post_2022_listing_check", "current_profile_verdict": "overcredits_mega_order_as_green_candidate", "dedupe_for_aggregate": true, "do_not_count_as_new_case": false, "drawdown_after_peak_pct": -44.37, "drawdown_after_peak_trough_date": "2024-12-09", "entry_date": "2024-04-03", "entry_ohlc": {"a": 132179182025.0, "c": 25300.0, "d": "2024-04-03", "h": 26750.0, "l": 25000.0, "m": "KOSPI", "mc": 4958800000000.0, "o": 25000.0, "s": 196000000, "v": 5117106.0}, "entry_price": 25300.0, "evidence_available_at_that_date": true, "evidence_family": "fadhili_gas_mega_epc_contract_large_order_but_no_near_term_margin_bridge", "evidence_source": "https://www.samsungena.com/en/newsroom/news/view?idx=15577", "evidence_source_note": "Samsung E&A announced approximately USD 6bn Fadhili Gas Increment Program contracts, including gas treatment, utilities/offsites, and full EPC execution.", "evidence_timing_rule": "same_day_close_if_tradable_or_first_tradable_date_after_publication", "fine_archetype_id": "LARGE_EPC_CONTRACT_MARGIN_COST_RATE_BRIDGE", "independent_evidence_weight": 1.0, "is_new_independent_case": true, "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "loop": 129, "price_adjustment_status": "raw_unadjusted_marcap", "price_basis": "tradable_raw", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_data_source": "Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/028/028050/<year>.csv", "profile_path": "atlas/symbol_profiles/028/028050.json", "reuse_reason": null, "round": "R1", "row_type": "trigger", "same_entry_group_id": "C05_EPC_MEGA_CONTRACT_MARGIN_GAP|028050|Stage2-Actionable|2024-04-03|fadhili_gas_mega_epc_contract_large_order_but_no_near_term_margin_bridge", "shadow_rule_verdict": "Stage2A_only; Green_requires_margin_EPS_or_execution_bridge", "source_proxy_only": false, "stage2_evidence_fields": ["USD_6bn_contract", "Aramco_customer", "full_EPC_scope"], "stage3_evidence_fields": ["execution_system_claim_only", "no_current_year_margin_bridge_at_trigger"], "stage4b_evidence_fields": ["180D_MAE_-35pct", "local_peak_after_Q2_but_failed_full_window"], "stage4c_evidence_fields": [], "stock_web_manifest_max_date": "2026-02-20", "symbol": "028050", "trigger_date": "2024-04-03", "trigger_id": "C05_L129_T002_028050_STAGE2A_20240403", "trigger_outcome_label": "counterexample_high_mae_delayed_margin_conversion", "trigger_type": "Stage2-Actionable"}
{"MAE_180D_pct": -10.17, "MAE_180D_trough_date": "2024-04-19", "MAE_180D_trough_low": 14040.0, "MAE_30D_pct": -10.17, "MAE_30D_trough_date": "2024-04-19", "MAE_90D_pct": -10.17, "MAE_90D_trough_date": "2024-04-19", "MFE_180D_pct": 39.16, "MFE_180D_peak_date": "2024-08-27", "MFE_180D_peak_high": 21750.0, "MFE_30D_pct": 6.97, "MFE_30D_peak_date": "2024-04-30", "MFE_90D_pct": 30.52, "MFE_90D_peak_date": "2024-07-31", "calibration_block_reasons": [], "calibration_usable": true, "canonical_archetype_id": "C05_EPC_MEGA_CONTRACT_MARGIN_GAP", "case_id": "C05_L129_006360_20240403_STAGE3Y", "company_name": "GS E&C", "company_name_kr": "GS건설", "corporate_action_window_status": "clean_180D_from_profile_candidates_or_post_2022_listing_check", "current_profile_verdict": "Stage2A_or_Yellow_supported", "dedupe_for_aggregate": true, "do_not_count_as_new_case": false, "drawdown_after_peak_pct": -22.48, "drawdown_after_peak_trough_date": "2024-11-13", "entry_date": "2024-04-03", "entry_ohlc": {"a": 64698222680.0, "c": 15630.0, "d": "2024-04-03", "h": 16550.0, "l": 15400.0, "m": "KOSPI", "mc": 1337638688700.0, "o": 15500.0, "s": 85581490, "v": 4065591.0}, "entry_price": 15630.0, "evidence_available_at_that_date": true, "evidence_family": "fadhili_sulfur_recovery_unit_contract_with_recovery_from_prior_quality_overhang", "evidence_source": "https://www.investkorea.org/ik-en/bbs/i-5073/detail.do?ntt_sn=492511", "evidence_source_note": "InvestKOREA/Yonhap report states GS E&C bagged a USD 1.22bn sulfur recovery unit deal within the Fadhili program, expected to take about 41 months.", "evidence_timing_rule": "same_day_close_if_tradable_or_first_tradable_date_after_publication", "fine_archetype_id": "LARGE_EPC_CONTRACT_MARGIN_COST_RATE_BRIDGE", "independent_evidence_weight": 1.0, "is_new_independent_case": true, "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "loop": 129, "price_adjustment_status": "raw_unadjusted_marcap", "price_basis": "tradable_raw", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_data_source": "Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/006/006360/<year>.csv", "profile_path": "atlas/symbol_profiles/006/006360.json", "reuse_reason": null, "round": "R1", "row_type": "trigger", "same_entry_group_id": "C05_EPC_MEGA_CONTRACT_MARGIN_GAP|006360|Stage3-Yellow|2024-04-03|fadhili_sulfur_recovery_unit_contract_with_recovery_from_prior_quality_overhang", "shadow_rule_verdict": "Stage3-Yellow_with_Green_cap_due_prior_cost_quality_overhang", "source_proxy_only": true, "stage2_evidence_fields": ["USD_1.22bn_contract", "named_project", "specialized_sulfur_recovery_unit"], "stage3_evidence_fields": ["strong_90D_180D_MFE", "but_contract_duration_long"], "stage4b_evidence_fields": ["prior_Geomdan_cost_quality_overhang_should_cap_Green"], "stage4c_evidence_fields": [], "stock_web_manifest_max_date": "2026-02-20", "symbol": "006360", "trigger_date": "2024-04-03", "trigger_id": "C05_L129_T003_006360_STAGE3Y_20240403", "trigger_outcome_label": "positive_but_green_requires_cost_and_quality_recovery_confirmation", "trigger_type": "Stage3-Yellow"}
{"MAE_180D_pct": -7.21, "MAE_180D_trough_date": "2025-04-09", "MAE_180D_trough_low": 108100.0, "MAE_30D_pct": -3.52, "MAE_30D_trough_date": "2025-01-02", "MAE_90D_pct": -7.21, "MAE_90D_trough_date": "2025-04-09", "MFE_180D_pct": 62.15, "MFE_180D_peak_date": "2025-07-17", "MFE_180D_peak_high": 188900.0, "MFE_30D_pct": 6.35, "MFE_30D_peak_date": "2025-01-23", "MFE_90D_pct": 17.42, "MFE_90D_peak_date": "2025-02-19", "calibration_block_reasons": [], "calibration_usable": true, "canonical_archetype_id": "C05_EPC_MEGA_CONTRACT_MARGIN_GAP", "case_id": "C05_L129_028260_20241211_STAGE3Y", "company_name": "Samsung C&T", "company_name_kr": "삼성물산", "corporate_action_window_status": "clean_180D_from_profile_candidates_or_post_2022_listing_check", "current_profile_verdict": "Stage2A_supported", "dedupe_for_aggregate": true, "do_not_count_as_new_case": false, "drawdown_after_peak_pct": -17.79, "drawdown_after_peak_trough_date": "2025-08-20", "entry_date": "2024-12-11", "entry_ohlc": {"a": 29701085930.0, "c": 116500.0, "d": "2024-12-11", "h": 116600.0, "l": 114700.0, "m": "KOSPI", "mc": 20711848465500.0, "o": 115800.0, "s": 177784107, "v": 256239.0}, "entry_price": 116500.0, "evidence_available_at_that_date": true, "evidence_family": "qatar_power_desalination_epc_named_project_with_follow_through", "evidence_source": "https://news.samsungcnt.com/en/features/engineering-construction/2024-12-samsung-campt-secures-2-84-billion-desalination-and-power-plant-project-in-qatar/", "evidence_source_note": "Samsung C&T announced a USD 2.84bn EPC contract for Qatar Facility E desalination and combined-cycle power plant, with sole EPC management and completion expected in 2029.", "evidence_timing_rule": "same_day_close_if_tradable_or_first_tradable_date_after_publication", "fine_archetype_id": "LARGE_EPC_CONTRACT_MARGIN_COST_RATE_BRIDGE", "independent_evidence_weight": 1.0, "is_new_independent_case": true, "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "loop": 129, "price_adjustment_status": "raw_unadjusted_marcap", "price_basis": "tradable_raw", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_data_source": "Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/028/028260/<year>.csv", "profile_path": "atlas/symbol_profiles/028/028260.json", "reuse_reason": null, "round": "R1", "row_type": "trigger", "same_entry_group_id": "C05_EPC_MEGA_CONTRACT_MARGIN_GAP|028260|Stage3-Yellow|2024-12-11|qatar_power_desalination_epc_named_project_with_follow_through", "shadow_rule_verdict": "Stage3-Yellow_possible_if_margin_visibility_confirmed", "source_proxy_only": false, "stage2_evidence_fields": ["USD_2.84bn_EPC_contract", "Kahramaa_project", "sole_EPC_management"], "stage3_evidence_fields": ["existing_Qatar_power_LNG_execution_track_record", "strong_180D_MFE_with_low_MAE"], "stage4b_evidence_fields": ["long_execution_to_2029_means_Green_requires_margin_monitor"], "stage4c_evidence_fields": [], "stock_web_manifest_max_date": "2026-02-20", "symbol": "028260", "trigger_date": "2024-12-11", "trigger_id": "C05_L129_T004_028260_STAGE3Y_20241211", "trigger_outcome_label": "positive_large_epc_order_with_clean_drawdown_profile", "trigger_type": "Stage3-Yellow"}
{"MAE_180D_pct": -5.18, "MAE_180D_trough_date": "2024-11-13", "MAE_180D_trough_low": 29300.0, "MAE_30D_pct": -5.18, "MAE_30D_trough_date": "2024-11-13", "MAE_90D_pct": -5.18, "MAE_90D_trough_date": "2024-11-13", "MFE_180D_pct": 93.2, "MFE_180D_peak_date": "2025-06-26", "MFE_180D_peak_high": 59700.0, "MFE_30D_pct": 12.62, "MFE_30D_peak_date": "2024-12-03", "MFE_90D_pct": 51.94, "MFE_90D_peak_date": "2025-03-10", "calibration_block_reasons": [], "calibration_usable": true, "canonical_archetype_id": "C05_EPC_MEGA_CONTRACT_MARGIN_GAP", "case_id": "C05_L129_375500_20241031_STAGE3G", "company_name": "DL E&C", "company_name_kr": "DL이앤씨", "corporate_action_window_status": "clean_180D_from_profile_candidates_or_post_2022_listing_check", "current_profile_verdict": "Stage2A_supported_if_only_contracts; Green_requires_margin_bridge", "dedupe_for_aggregate": true, "do_not_count_as_new_case": false, "drawdown_after_peak_pct": -22.78, "drawdown_after_peak_trough_date": "2025-07-28", "entry_date": "2024-10-31", "entry_ohlc": {"a": 2997358750.0, "c": 30900.0, "d": "2024-10-31", "h": 30900.0, "l": 30050.0, "m": "KOSPI", "mc": 1195632950700.0, "o": 30750.0, "s": 38693623, "v": 98638.0}, "entry_price": 30900.0, "evidence_available_at_that_date": true, "evidence_family": "cost_rate_margin_rebound_and_selective_order_strategy", "evidence_source": "https://www.dlenc.co.kr/eng/daelim/pr/NewsView.do?cd_mnu=EU035&currentPage=1&idx=25384&keyword=all&searchword=", "evidence_source_note": "DL E&C announced Q3 2024 cumulative sales/OP, improved cost rate, rebound in operating profit, and selective order strategy focused on profitability.", "evidence_timing_rule": "same_day_close_if_tradable_or_first_tradable_date_after_publication", "fine_archetype_id": "LARGE_EPC_CONTRACT_MARGIN_COST_RATE_BRIDGE", "independent_evidence_weight": 1.0, "is_new_independent_case": true, "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "loop": 129, "price_adjustment_status": "raw_unadjusted_marcap", "price_basis": "tradable_raw", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_data_source": "Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/375/375500/<year>.csv", "profile_path": "atlas/symbol_profiles/375/375500.json", "reuse_reason": null, "round": "R1", "row_type": "trigger", "same_entry_group_id": "C05_EPC_MEGA_CONTRACT_MARGIN_GAP|375500|Stage3-Green|2024-10-31|cost_rate_margin_rebound_and_selective_order_strategy", "shadow_rule_verdict": "Stage3-Green_supported_by_cost_rate_and_OP_bridge", "source_proxy_only": false, "stage2_evidence_fields": ["order_pipeline_present", "profitability_management"], "stage3_evidence_fields": ["Q3_OP_rebound", "cost_rate_improvement", "selective_high_profit_orders"], "stage4b_evidence_fields": [], "stage4c_evidence_fields": [], "stock_web_manifest_max_date": "2026-02-20", "symbol": "375500", "trigger_date": "2024-10-31", "trigger_id": "C05_L129_T005_375500_STAGE3G_20241031", "trigger_outcome_label": "positive_margin_bridge_case", "trigger_type": "Stage3-Green"}
{"MAE_180D_pct": -17.52, "MAE_180D_trough_date": "2025-11-07", "MAE_180D_trough_low": 3320.0, "MAE_30D_pct": -3.73, "MAE_30D_trough_date": "2025-05-26", "MAE_90D_pct": -12.05, "MAE_90D_trough_date": "2025-08-20", "MFE_180D_pct": 99.75, "MFE_180D_peak_date": "2026-02-12", "MFE_180D_peak_high": 8040.0, "MFE_30D_pct": 19.38, "MFE_30D_peak_date": "2025-06-05", "MFE_90D_pct": 19.38, "MFE_90D_peak_date": "2025-06-05", "calibration_block_reasons": [], "calibration_usable": true, "canonical_archetype_id": "C05_EPC_MEGA_CONTRACT_MARGIN_GAP", "case_id": "C05_L129_047040_20250526_STAGE3Y", "company_name": "Daewoo E&C", "company_name_kr": "대우건설", "corporate_action_window_status": "clean_180D_from_profile_candidates_or_post_2022_listing_check", "current_profile_verdict": "Stage2A_supported", "dedupe_for_aggregate": true, "do_not_count_as_new_case": false, "drawdown_after_peak_pct": -12.06, "drawdown_after_peak_trough_date": "2026-02-13", "entry_date": "2025-05-26", "entry_ohlc": {"a": 10941475875.0, "c": 4025.0, "d": "2025-05-26", "h": 4045.0, "l": 3875.0, "m": "KOSPI", "mc": 1672881117950.0, "o": 4045.0, "s": 415622638, "v": 2742868.0}, "entry_price": 4025.0, "evidence_available_at_that_date": true, "evidence_family": "turkmenistan_fertilizer_final_contract_with_first_central_asia_project", "evidence_source": "https://en.yna.co.kr/view/AEN20250526003100320", "evidence_source_note": "Daewoo E&C signed a USD 784mn final contract with Turkmenhimiya for a fertilizer plant in Turkmenabat; project equals roughly 10% of 2024 annual sales and targets 37-month completion after groundbreaking.", "evidence_timing_rule": "same_day_close_if_tradable_or_first_tradable_date_after_publication", "fine_archetype_id": "LARGE_EPC_CONTRACT_MARGIN_COST_RATE_BRIDGE", "independent_evidence_weight": 1.0, "is_new_independent_case": true, "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "loop": 129, "price_adjustment_status": "raw_unadjusted_marcap", "price_basis": "tradable_raw", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_data_source": "Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/047/047040/<year>.csv", "profile_path": "atlas/symbol_profiles/047/047040.json", "reuse_reason": null, "round": "R1", "row_type": "trigger", "same_entry_group_id": "C05_EPC_MEGA_CONTRACT_MARGIN_GAP|047040|Stage3-Yellow|2025-05-26|turkmenistan_fertilizer_final_contract_with_first_central_asia_project", "shadow_rule_verdict": "Stage3-Yellow_possible; Green_waits_for_groundbreaking_cost_margin_conversion", "source_proxy_only": true, "stage2_evidence_fields": ["USD_784mn_contract", "state_chemical_company_customer", "capacity_specified"], "stage3_evidence_fields": ["first_Central_Asia_project", "10pct_sales_scale", "strong_late_180D_MFE"], "stage4b_evidence_fields": ["90D_MAE_-12pct_and_long_37_month_execution"], "stage4c_evidence_fields": [], "stock_web_manifest_max_date": "2026-02-20", "symbol": "047040", "trigger_date": "2025-05-26", "trigger_id": "C05_L129_T006_047040_STAGE3Y_20250526", "trigger_outcome_label": "positive_but_high_90D_MAE_and_long_execution_yellow_not_green", "trigger_type": "Stage3-Yellow"}
```

## 9. Score simulation JSONL

```jsonl
{"alignment_verdict": "contract_size_without_margin_bridge_should_be_downgraded", "canonical_archetype_id": "C05_EPC_MEGA_CONTRACT_MARGIN_GAP", "case_id": "C05_L129_000720_20230626_STAGE2A", "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "loop": 129, "observed_MAE_180D_pct": -23.53, "observed_MFE_180D_pct": 8.82, "profile_after": "shadow_C05_contract_to_margin_cost_rate_bridge_v2", "profile_before": "e2r_2_2_rolling_calibrated_proxy_current", "raw_component_scores_after": {"bottleneck_pricing": 9, "capital_allocation": 8, "earnings_visibility": 25, "eps_fcf_explosion": 16, "information_confidence": 22, "market_mispricing": 10, "valuation_rerating": 8}, "raw_component_scores_before": {"bottleneck_pricing": 10, "capital_allocation": 8, "earnings_visibility": 22, "eps_fcf_explosion": 18, "information_confidence": 20, "market_mispricing": 12, "valuation_rerating": 10}, "round": "R1", "row_type": "score_simulation", "score_after_shadow": 65, "score_before_proxy": 76, "stage_after_shadow": "Stage2", "stage_before": "Stage2-Actionable", "symbol": "000720", "trigger_id": "C05_L129_T001_000720_STAGE2A_20230626"}
{"alignment_verdict": "contract_size_without_margin_bridge_should_be_downgraded", "canonical_archetype_id": "C05_EPC_MEGA_CONTRACT_MARGIN_GAP", "case_id": "C05_L129_028050_20240403_STAGE2A", "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "loop": 129, "observed_MAE_180D_pct": -35.57, "observed_MFE_180D_pct": 15.81, "profile_after": "shadow_C05_contract_to_margin_cost_rate_bridge_v2", "profile_before": "e2r_2_2_rolling_calibrated_proxy_current", "raw_component_scores_after": {"bottleneck_pricing": 9, "capital_allocation": 8, "earnings_visibility": 25, "eps_fcf_explosion": 16, "information_confidence": 22, "market_mispricing": 10, "valuation_rerating": 8}, "raw_component_scores_before": {"bottleneck_pricing": 10, "capital_allocation": 8, "earnings_visibility": 22, "eps_fcf_explosion": 18, "information_confidence": 20, "market_mispricing": 12, "valuation_rerating": 10}, "round": "R1", "row_type": "score_simulation", "score_after_shadow": 65, "score_before_proxy": 76, "stage_after_shadow": "Stage2", "stage_before": "Stage2-Actionable", "symbol": "028050", "trigger_id": "C05_L129_T002_028050_STAGE2A_20240403"}
{"alignment_verdict": "yellow_supported_but_green_requires_execution_margin_bridge", "canonical_archetype_id": "C05_EPC_MEGA_CONTRACT_MARGIN_GAP", "case_id": "C05_L129_006360_20240403_STAGE3Y", "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "loop": 129, "observed_MAE_180D_pct": -10.17, "observed_MFE_180D_pct": 39.16, "profile_after": "shadow_C05_contract_to_margin_cost_rate_bridge_v2", "profile_before": "e2r_2_2_rolling_calibrated_proxy_current", "raw_component_scores_after": {"bottleneck_pricing": 9, "capital_allocation": 8, "earnings_visibility": 25, "eps_fcf_explosion": 20, "information_confidence": 22, "market_mispricing": 10, "valuation_rerating": 8}, "raw_component_scores_before": {"bottleneck_pricing": 10, "capital_allocation": 8, "earnings_visibility": 22, "eps_fcf_explosion": 18, "information_confidence": 20, "market_mispricing": 12, "valuation_rerating": 10}, "round": "R1", "row_type": "score_simulation", "score_after_shadow": 81, "score_before_proxy": 78, "stage_after_shadow": "Stage3-Yellow", "stage_before": "Stage3-Yellow", "symbol": "006360", "trigger_id": "C05_L129_T003_006360_STAGE3Y_20240403"}
{"alignment_verdict": "yellow_supported_but_green_requires_execution_margin_bridge", "canonical_archetype_id": "C05_EPC_MEGA_CONTRACT_MARGIN_GAP", "case_id": "C05_L129_028260_20241211_STAGE3Y", "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "loop": 129, "observed_MAE_180D_pct": -7.21, "observed_MFE_180D_pct": 62.15, "profile_after": "shadow_C05_contract_to_margin_cost_rate_bridge_v2", "profile_before": "e2r_2_2_rolling_calibrated_proxy_current", "raw_component_scores_after": {"bottleneck_pricing": 9, "capital_allocation": 8, "earnings_visibility": 25, "eps_fcf_explosion": 20, "information_confidence": 22, "market_mispricing": 10, "valuation_rerating": 8}, "raw_component_scores_before": {"bottleneck_pricing": 10, "capital_allocation": 8, "earnings_visibility": 22, "eps_fcf_explosion": 18, "information_confidence": 20, "market_mispricing": 12, "valuation_rerating": 10}, "round": "R1", "row_type": "score_simulation", "score_after_shadow": 81, "score_before_proxy": 78, "stage_after_shadow": "Stage3-Yellow", "stage_before": "Stage3-Yellow", "symbol": "028260", "trigger_id": "C05_L129_T004_028260_STAGE3Y_20241211"}
{"alignment_verdict": "margin_cost_rate_bridge_supports_green", "canonical_archetype_id": "C05_EPC_MEGA_CONTRACT_MARGIN_GAP", "case_id": "C05_L129_375500_20241031_STAGE3G", "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "loop": 129, "observed_MAE_180D_pct": -5.18, "observed_MFE_180D_pct": 93.2, "profile_after": "shadow_C05_contract_to_margin_cost_rate_bridge_v2", "profile_before": "e2r_2_2_rolling_calibrated_proxy_current", "raw_component_scores_after": {"bottleneck_pricing": 9, "capital_allocation": 8, "earnings_visibility": 25, "eps_fcf_explosion": 20, "information_confidence": 22, "market_mispricing": 10, "valuation_rerating": 8}, "raw_component_scores_before": {"bottleneck_pricing": 10, "capital_allocation": 8, "earnings_visibility": 22, "eps_fcf_explosion": 18, "information_confidence": 20, "market_mispricing": 12, "valuation_rerating": 10}, "round": "R1", "row_type": "score_simulation", "score_after_shadow": 88, "score_before_proxy": 82, "stage_after_shadow": "Stage3-Green", "stage_before": "Stage3-Green", "symbol": "375500", "trigger_id": "C05_L129_T005_375500_STAGE3G_20241031"}
{"alignment_verdict": "yellow_supported_but_green_requires_execution_margin_bridge", "canonical_archetype_id": "C05_EPC_MEGA_CONTRACT_MARGIN_GAP", "case_id": "C05_L129_047040_20250526_STAGE3Y", "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "loop": 129, "observed_MAE_180D_pct": -17.52, "observed_MFE_180D_pct": 99.75, "profile_after": "shadow_C05_contract_to_margin_cost_rate_bridge_v2", "profile_before": "e2r_2_2_rolling_calibrated_proxy_current", "raw_component_scores_after": {"bottleneck_pricing": 9, "capital_allocation": 8, "earnings_visibility": 25, "eps_fcf_explosion": 20, "information_confidence": 22, "market_mispricing": 10, "valuation_rerating": 8}, "raw_component_scores_before": {"bottleneck_pricing": 10, "capital_allocation": 8, "earnings_visibility": 22, "eps_fcf_explosion": 18, "information_confidence": 20, "market_mispricing": 12, "valuation_rerating": 10}, "round": "R1", "row_type": "score_simulation", "score_after_shadow": 81, "score_before_proxy": 78, "stage_after_shadow": "Stage3-Yellow", "stage_before": "Stage3-Yellow", "symbol": "047040", "trigger_id": "C05_L129_T006_047040_STAGE3Y_20250526"}
```

## 10. Aggregate JSON

```json
{"calibration_usable_case_count": 6, "calibration_usable_trigger_count": 6, "canonical_archetype_id": "C05_EPC_MEGA_CONTRACT_MARGIN_GAP", "counterexample_count": 2, "current_profile_error_count": 4, "evidence_url_pending_count": 0, "existing_axis_strengthened": ["stage2_required_bridge", "local_4b_watch_guard", "full_4b_requires_non_price_evidence", "drawdown_aware_confirmation"], "existing_axis_weakened": [], "fine_archetype_id": "LARGE_EPC_CONTRACT_MARGIN_COST_RATE_BRIDGE", "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "loop": 129, "new_axis_proposed": "C05_CONTRACT_TO_MARGIN_COST_RATE_CASH_BRIDGE_GATE", "new_independent_case_count": 6, "positive_case_count": 4, "production_scoring_changed": false, "reused_case_count": 0, "round": "R1", "row_type": "aggregate", "rows_missing_required_mfe_mae": 0, "same_archetype_new_symbol_count": 6, "same_archetype_new_trigger_family_count": 6, "shadow_weight_only": true, "source_proxy_only_count": 2, "stage4b_case_count": 5, "stage4c_case_count": 0}
```

## 11. Batch ingest self-audit

```text
standard_v12_filename: pass
filename_round_matches_metadata_round: pass
filename_loop_matches_metadata_loop: pass
round_sector_consistency: pass
canonical_archetype_id_allowed: pass
trigger_type_canonical_label_only: pass
complete_30_90_180_mfe_mae_in_every_trigger_row: pass
rows_missing_required_mfe_mae: 0
entry_date_present_all_rows: pass
entry_price_present_all_rows: pass
actual_1d_ohlc_rows_present: pass
same_entry_group_deduplication_key_present: pass
source_urls_present: pass
evidence_url_pending_count: 0
source_proxy_only_count: 2
calibration_usable_trigger_count: 6
production_scoring_changed: false
shadow_weight_only: true
```

## 12. Deferred Coding Agent Handoff Prompt

```text
You are the later coding/calibration agent. Do not execute this handoff during the research run.

Ingest this MD only as a v12 residual research artifact. Parse trigger JSONL rows where row_type == "trigger" and required MFE/MAE fields are complete. Apply same-entry dedupe using same_entry_group_id. Use the aggregate row only as summary metadata.

Candidate axis to evaluate in batch:
C05_CONTRACT_TO_MARGIN_COST_RATE_CASH_BRIDGE_GATE

Do not patch production scoring directly from this single MD. Compare this candidate against the full representative C05 corpus and rejected rows. Promote only if the wider C05 sample confirms that contract-only Stage2-Actionable overcredits cases with weak margin/cost-rate/working-capital evidence and that margin/cost-rate bridge rows align better with 90D/180D forward returns.
```

## 13. Next research state

```text
completed_round = R1
completed_loop = 129
selection_basis = docs/core/V12_Research_No_Repeat_Index.md
selected_priority_bucket = Priority 1 balance/quality repair — C05 margin/working-capital failure and 4C transition timing 보강
next_recommended_archetypes = C01_ORDER_BACKLOG_MARGIN_BRIDGE; C13_BATTERY_JV_UTILIZATION_AMPC_IRA; C15_MATERIAL_SPREAD_SUPERCYCLE; C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE
round_schedule_status = coverage_index_selected
round_sector_consistency = pass
```
