# E2R Stock-Web v12 Residual Research — R13 Loop 194 — R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL

```text
research_file = e2r_stock_web_v12_residual_round_R13_loop_194_L10_POLICY_EVENT_CROSS_REDTEAM_MISC_R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL_research.md
research_session = post_calibrated_sector_archetype_residual_research
mode = historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12
output_format = one_standalone_markdown_file
production_scoring_changed = false
shadow_weight_only = true
handoff_prompt_embedded = true
handoff_prompt_executed_now = false
do_not_propose_new_weight_delta = true
```

## 1. Execution Metadata

| field | value |
|---|---|
| `selected_round` | `R13` |
| `selected_loop` | `194` |
| `selection_basis` | `docs/core/V12_Research_No_Repeat_Index.md as duplicate-prevention / representative-compression ledger only` |
| `selected_priority_bucket` | `Priority 2 R13 high-MAE representative compression / quality repair` |
| `round_schedule_status` | `coverage_index_selected` |
| `round_sector_consistency` | `pass` |
| `large_sector_id` | `L10_POLICY_EVENT_CROSS_REDTEAM_MISC` |
| `canonical_archetype_id` | `R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL` |
| `fine_archetype_id` | `R13_HIGH_MAE_REPRESENTATIVE_COMPRESSION` |
| `loop_objective` | `cross-archetype high-MAE guardrail stress test using representative prior v12 triggers` |
| `loop_contribution_label` | `holdout_validation_passed` |
| `source_large_sector_count` | `4` |
| `source_canonical_count` | `5` |
| `source_symbol_count` | `8` |

R13은 개별 sector positive case를 새로 찾는 라운드가 아니라, R1~R12에서 반복적으로 나온 high-MAE / false-positive / 4B-vs-4C 경계 문제를 압축 점검하는 checkpoint다. 이번 파일은 **신규 독립 weight 근거를 추가하지 않고**, 이미 생성된 대표 trigger rows를 재사용해 current calibrated profile의 잔여 위험을 검증한다.

## 2. Stock-Web Manifest / Schema Validation

| field | value |
|---|---|
| `price_data_source` | `Songdaiki/stock-web` |
| `upstream_source` | `FinanceData/marcap` |
| `price_basis` | `tradable_raw` |
| `price_adjustment_status` | `raw_unadjusted_marcap` |
| `calibration_shard_root` | `atlas/ohlcv_tradable_by_symbol_year` |
| `stock_web_manifest_max_date` | `2026-02-20` |
| `tradable_schema` | `d,o,h,l,c,v,a,mc,s,m` |
| `MFE_definition` | `(max high from entry_date through N tradable rows / entry_price - 1) * 100` |
| `MAE_definition` | `(min low from entry_date through N tradable rows / entry_price - 1) * 100` |

All rows below preserve the existing Stock-Web raw/unadjusted basis from the source MDs. R13 reuses previously verified tradable shard entries; no current/live scan and no price-route hunt was performed.

## 3. Coverage / Novelty Check

| check | result |
|---|---:|
| `new_independent_case_count` | `0` |
| `reused_representative_case_count` | `8` |
| `new_independent_trigger_count` | `0` |
| `reused_representative_trigger_count` | `8` |
| `unique_source_symbol_count` | `8` |
| `unique_source_large_sector_count` | `4` |
| `unique_source_canonical_count` | `5` |
| `calibration_usable_case_count` | `8` |
| `calibration_usable_trigger_count` | `8` |
| `source_proxy_only_count` | `0` |
| `evidence_url_pending_count` | `0` |
| `missing_required_mfe_mae_count` | `0` |
| `corporate_action_contaminated_180D_count` | `0` |
| `insufficient_forward_window_180D_count` | `0` |
| `production_scoring_changed` | `false` |
| `shadow_weight_only` | `true` |
| `do_not_propose_new_weight_delta` | `true` |

Hard duplicate policy is preserved by marking all reused rows as `is_new_independent_case=false`, `independent_evidence_weight=0.0`, and `do_not_count_as_new_case=true`. This R13 file should be ingested as a representative holdout audit, not as fresh archetype coverage.

## 4. Source Coverage Matrix

| source_large_sector_id | source_canonical_archetype_id | symbols | rows | role |
|---|---|---:|---:|---|
| `L4_MATERIALS_SPREAD_RESOURCE` | `C15_MATERIAL_SPREAD_SUPERCYCLE` | `001230,103140` | 2 | representative_high_MAE_false_positive |
| `L2_AI_SEMICONDUCTOR_ELECTRONICS` | `C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE` | `166090,240810` | 2 | representative_high_MAE_false_positive,representative_high_MAE_stage2_cap |
| `L1_INDUSTRIALS_INFRA_DEFENSE_GRID` | `C02_POWER_GRID_DATACENTER_CAPEX` | `010120,033100` | 2 | representative_high_MAE_4B_not_hard_4c,representative_high_MAE_late_stage2_actionable |
| `L3_BATTERY_EV_GREEN_MOBILITY` | `C13_BATTERY_JV_UTILIZATION_AMPC_IRA` | `003670` | 1 | representative_high_MFE_high_MAE_positive_control |
| `L3_BATTERY_EV_GREEN_MOBILITY` | `C14_EV_DEMAND_SLOWDOWN_4B_4C` | `006400` | 1 | representative_hard_4c_success_control |

## 5. Representative Case Summary

| # | source | symbol | company | trigger | entry_date | entry_price | MFE/MAE 30D | MFE/MAE 90D | MFE/MAE 180D | peak | drawdown_after_peak | R13 role | verdict |
|---:|---|---|---|---|---|---:|---:|---:|---:|---|---:|---|---|
| 1 | `C15_MATERIAL_SPREAD_SUPERCYCLE` | `001230` | Dongkuk Steel legacy entity | `Stage2-Actionable` | 2021-05-18 | 25,250 | 2.57/-18.81 | 2.57/-30.69 | 2.57/-46.93 | 2021-05-18 @ 25,900 | -48.26 | representative_high_MAE_false_positive | `current_profile_false_positive` |
| 2 | `C15_MATERIAL_SPREAD_SUPERCYCLE` | `103140` | Poongsan | `Stage2-Actionable` | 2024-05-16 | 77,300 | 0.91/-28.07 | 0.91/-39.20 | 0.91/-40.30 | 2024-05-16 @ 78,000 | -40.83 | representative_high_MAE_false_positive | `current_profile_false_positive` |
| 3 | `C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE` | `240810` | Wonik IPS | `Stage2-Actionable` | 2024-07-30 | 35,200 | 9.38/-17.47 | 9.38/-39.91 | 9.38/-40.91 | 2024-08-21 @ 38,500 | -45.97 | representative_high_MAE_false_positive | `current_profile_false_positive` |
| 4 | `C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE` | `166090` | Hana Materials | `Stage2` | 2024-06-26 | 63,900 | 8.45/-38.73 | 8.45/-56.65 | 8.45/-65.81 | 2024-07-02 @ 69,300 | -68.47 | representative_high_MAE_stage2_cap | `current_profile_correct_if_capped_at_stage2_but_not_actionable` |
| 5 | `C02_POWER_GRID_DATACENTER_CAPEX` | `033100` | JeRyong Electric | `Stage2-Actionable` | 2024-05-29 | 73,900 | 35.05/-17.73 | 36.27/-41.54 | 36.27/-50.54 | 2024-07-11 @ 100,700 | -63.70 | representative_high_MAE_late_stage2_actionable | `current_profile_false_positive_if_stage2_actionable_is_not_capped_by_entry_quality` |
| 6 | `C13_BATTERY_JV_UTILIZATION_AMPC_IRA` | `003670` | POSCO Future M | `Stage2-Actionable` | 2023-06-02 | 374,000 | 12.30/-7.89 | 85.56/-16.18 | 85.56/-38.10 | 2023-07-26 @ 694,000 | -66.64 | representative_high_MFE_high_MAE_positive_control | `current_profile_missed_structural_if_capacity_JV_not_mapped_but_green_block_correct` |
| 7 | `C14_EV_DEMAND_SLOWDOWN_4B_4C` | `006400` | Samsung SDI | `Stage4C` | 2024-10-31 | 327,000 | 4.28/-27.98 | 4.28/-42.87 | 4.28/-51.77 | 2024-10-31 @ 341,000 | -53.75 | representative_hard_4c_success_control | `current_profile_correct` |
| 8 | `C02_POWER_GRID_DATACENTER_CAPEX` | `010120` | LS ELECTRIC | `Stage4B` | 2024-07-25 | 215,500 | 19.26/-38.33 | 19.26/-41.44 | 40.84/-41.44 | 2025-02-19 @ 303,500 | -58.42 | representative_high_MAE_4B_not_hard_4c | `current_profile_correct_if_local_4B_not_hard_4C` |

## 6. Actual 1D OHLC Entry Rows

| symbol | entry_date | o | h | l | c | v | price_shard_path | profile_path | contamination |
|---|---|---:|---:|---:|---:|---:|---|---|---|
| `001230` | 2021-05-18 | 23,750 | 25,900 | 23,500 | 25,250 | 5,334,664 | `atlas/ohlcv_tradable_by_symbol_year/001/001230/2021.csv; atlas/ohlcv_tradable_by_symbol_year/001/001230/2022.csv` | `atlas/symbol_profiles/001/001230.json` | `clean_180D_window` |
| `103140` | 2024-05-16 | 78,000 | 78,000 | 74,400 | 77,300 | 562,357 | `atlas/ohlcv_tradable_by_symbol_year/103/103140/2024.csv; atlas/ohlcv_tradable_by_symbol_year/103/103140/2025.csv; atlas/ohlcv_tradable_by_symbol_year/103/103140/2026.csv` | `atlas/symbol_profiles/103/103140.json` | `clean_180D_window` |
| `240810` | 2024-07-30 | 34,800 | 35,350 | 34,200 | 35,200 | 144,309 | `atlas/ohlcv_tradable_by_symbol_year/240/240810/2024.csv; atlas/ohlcv_tradable_by_symbol_year/240/240810/2025.csv` | `atlas/symbol_profiles/240/240810.json` | `clean_180D_window` |
| `166090` | 2024-06-26 | 58,600 | 66,600 | 58,600 | 63,900 | 685,393 | `atlas/ohlcv_tradable_by_symbol_year/166/166090/2024.csv; atlas/ohlcv_tradable_by_symbol_year/166/166090/2025.csv` | `atlas/symbol_profiles/166/166090.json` | `clean_180D_window` |
| `033100` | 2024-05-29 | 78,100 | 78,900 | 72,500 | 73,900 | 1,114,957 | `atlas/ohlcv_tradable_by_symbol_year/033/033100/2024.csv; atlas/ohlcv_tradable_by_symbol_year/033/033100/2025.csv` | `atlas/symbol_profiles/033/033100.json` | `clean_180D_window` |
| `003670` | 2023-06-02 | 361,500 | 381,500 | 358,500 | 374,000 | 1,467,089 | `atlas/ohlcv_tradable_by_symbol_year/003/003670/2023.csv` | `atlas/symbol_profiles/003/003670.json` | `clean_180D_window` |
| `006400` | 2024-10-31 | 334,500 | 341,000 | 327,000 | 327,000 | 378,994 | `atlas/ohlcv_tradable_by_symbol_year/006/006400/2024.csv; atlas/ohlcv_tradable_by_symbol_year/006/006400/2025.csv` | `atlas/symbol_profiles/006/006400.json` | `clean_180D_window` |
| `010120` | 2024-07-25 | 249,500 | 257,000 | 214,500 | 215,500 | 2,303,383 | `atlas/ohlcv_tradable_by_symbol_year/010/010120/2024.csv; atlas/ohlcv_tradable_by_symbol_year/010/010120/2025.csv; atlas/ohlcv_tradable_by_symbol_year/010/010120/2026.csv` | `atlas/symbol_profiles/010/010120.json` | `clean_180D_window` |

## 7. High-MAE Distribution

| metric | value |
|---|---:|
| `avg_MFE_90D_pct` | `20.84` |
| `avg_MAE_90D_pct` | `-38.56` |
| `avg_MFE_180D_pct` | `23.53` |
| `avg_MAE_180D_pct` | `-46.98` |
| `MAE90 <= -30% rows` | `7/8` |
| `MAE180 <= -40% rows` | `7/8` |
| `MFE180 < 20% rows` | `5/8` |
| `counterexample avg MFE180` | `11.52` |
| `counterexample avg MAE180` | `-48.9` |
| `positive/control avg MFE180` | `43.56` |
| `positive/control avg MAE180` | `-43.77` |

Interpretation: high MAE is not a universal sell/avoid signal. It is a **stage-escalation brake**. The guardrail should block Actionable/Yellow/Green escalation when the evidence is generic, late-cycle, or price-extension-driven, while preserving true hard 4C and true structural winners with direct customer/order/capacity bridge.

## 8. Case Notes

### 8.1. Dongkuk Steel legacy entity (`001230`) — Stage2-Actionable — representative_high_MAE_false_positive

- Source row: `e2r_stock_web_v12_residual_round_R4_loop_191_L4_MATERIALS_SPREAD_RESOURCE_C15_MATERIAL_SPREAD_SUPERCYCLE_research.md` / `C15-001230-20210517-STAGE2A`.
- Evidence: Dongkuk Steel's Q1 profit and rebar-price strength arrived after the steel/rebar cycle had already run hard.
- Evidence URL: https://www.kedglobal.com/earnings/newsView/ked202105170018
- Price path: 90D MFE/MAE `2.57/-30.69`, 180D MFE/MAE `2.57/-46.93`.
- Residual lesson: R13 cap blocks Stage2-Actionable when commodity/spread evidence appears on the entry-day peak and no forward duration bridge exists.

### 8.2. Poongsan (`103140`) — Stage2-Actionable — representative_high_MAE_false_positive

- Source row: `e2r_stock_web_v12_residual_round_R4_loop_191_L4_MATERIALS_SPREAD_RESOURCE_C15_MATERIAL_SPREAD_SUPERCYCLE_research.md` / `C15-103140-20240514-STAGE2A`.
- Evidence: Copper-price and defense-seasonality narrative was present, but company-specific volume/cost conversion remained thin.
- Evidence URL: https://v.daum.net/v/fXzID0JqJ6?f=p
- Price path: 90D MFE/MAE `0.91/-39.20`, 180D MFE/MAE `0.91/-40.30`.
- Residual lesson: R13 cap prevents generic commodity-price beta from behaving like a company-specific rerating trigger.

### 8.3. Wonik IPS (`240810`) — Stage2-Actionable — representative_high_MAE_false_positive

- Source row: `e2r_stock_web_v12_residual_round_R2_loop_193_L2_AI_SEMICONDUCTOR_ELECTRONICS_C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE_research.md` / `C10_193_T01`.
- Evidence: Broker/news profit-turn expectation referenced memory-cycle recovery but not a firm supplier-level order conversion.
- Evidence URL: https://www.asiae.co.kr/en/article/2024073007450660238
- Price path: 90D MFE/MAE `9.38/-39.91`, 180D MFE/MAE `9.38/-40.91`.
- Residual lesson: Generic memory-cycle recovery is capped unless supplier-specific order or revenue conversion is visible.

### 8.4. Hana Materials (`166090`) — Stage2 — representative_high_MAE_stage2_cap

- Source row: `e2r_stock_web_v12_residual_round_R2_loop_193_L2_AI_SEMICONDUCTOR_ELECTRONICS_C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE_research.md` / `C10_193_T08`.
- Evidence: Memory-utilization recovery and consumables demand language appeared, but it did not survive MAE stress.
- Evidence URL: https://www.businesspost.co.kr/BP?command=article_view&num=356811
- Price path: 90D MFE/MAE `8.45/-56.65`, 180D MFE/MAE `8.45/-65.81`.
- Residual lesson: Stage2 can remain as an early-cycle observation, but high-MAE guardrail blocks Actionable/Yellow/Green escalation.

### 8.5. JeRyong Electric (`033100`) — Stage2-Actionable — representative_high_MAE_late_stage2_actionable

- Source row: `e2r_stock_web_v12_residual_round_R1_loop_193_L1_INDUSTRIALS_INFRA_DEFENSE_GRID_C02_POWER_GRID_DATACENTER_CAPEX_research.md` / `C02_R1L193_033100_20240529_STAGE2A_HMAE`.
- Evidence: Q1 growth, export share, US transformer shortage, and order backlog were real, but the entry was late and extremely drawdown-prone.
- Evidence URL: https://www.thebigdata.co.kr/view.php?ud=202405290538457085cd1e7f0bdf_23
- Price path: 90D MFE/MAE `36.27/-41.54`, 180D MFE/MAE `36.27/-50.54`.
- Residual lesson: Real backlog/shortage evidence remains valuable, but high-MAE late-entry condition caps it below Yellow/Green.

### 8.6. POSCO Future M (`003670`) — Stage2-Actionable — representative_high_MFE_high_MAE_positive_control

- Source row: `e2r_stock_web_v12_residual_round_R3_loop_190_L3_BATTERY_EV_GREEN_MOBILITY_C13_BATTERY_JV_UTILIZATION_AMPC_IRA_research.md` / `R3L190_C13_003670_20230602_STAGE2_ACTIONABLE`.
- Evidence: GM/POSCO Future M North America CAM/precursor expansion provided a real structural capacity bridge, although the later drawdown was severe.
- Evidence URL: https://www.poscofuturem.com/en/pr/view.do?num=695 ; https://news.gm.com/home.detail.html/Pages/news/us/en/2023/jun/0602-posco.html
- Price path: 90D MFE/MAE `85.56/-16.18`, 180D MFE/MAE `85.56/-38.10`.
- Residual lesson: R13 high-MAE guardrail must not block all volatile winners; direct customer/JV capacity bridge preserves Stage2-Actionable while preventing Green.

### 8.7. Samsung SDI (`006400`) — Stage4C — representative_hard_4c_success_control

- Source row: `e2r_stock_web_v12_residual_round_R3_loop_192_L3_BATTERY_EV_GREEN_MOBILITY_C14_EV_DEMAND_SLOWDOWN_4B_4C_research.md` / `C14_006400_20241030_STAGE4C_EV_SLOWDOWN_BATTERY_UNIT_COLLAPSE`.
- Evidence: Q3 2024 release showed sharp battery earnings deterioration, European EV slowdown, and lower cylindrical utilization.
- Evidence URL: https://www.samsungsdi.com/sdi-now/sdi-news/4082.html
- Price path: 90D MFE/MAE `4.28/-42.87`, 180D MFE/MAE `4.28/-51.77`.
- Residual lesson: This is the control case showing that high-MAE guardrail should preserve true hard 4C when non-price thesis break is confirmed.

### 8.8. LS ELECTRIC (`010120`) — Stage4B — representative_high_MAE_4B_not_hard_4c

- Source row: `e2r_stock_web_v12_residual_round_R1_loop_193_L1_INDUSTRIALS_INFRA_DEFENSE_GRID_C02_POWER_GRID_DATACENTER_CAPEX_research.md` / `C02_R1L193_010120_20240725_4B`.
- Evidence: 2Q24 official deck showed record profitability driven by the US electric business, while price extension and high MAE required 4B watch instead of Green.
- Evidence URL: https://www.ls-electric.com/ko/company/data/24_2Q_Results.pdf
- Price path: 90D MFE/MAE `19.26/-41.44`, 180D MFE/MAE `40.84/-41.44`.
- Residual lesson: High MAE and extension should trigger local 4B watch, not hard 4C, because subsequent 180D MFE still reached 40.84%.

## 9. Current Calibrated Profile Stress Test

| case | before_stage | before_score | after_stage | after_score | profile verdict | R13 correction |
|---|---|---:|---|---:|---|---|
| `R13_HMAE_194_001230_C15_REBAR_SPREAD_LATE_CYCLE` | `Stage2-Actionable` | 76.0 | `Stage2` | 60.0 | `current_profile_false_positive` | R13 cap blocks Stage2-Actionable when commodity/spread evidence appears on the entry-day peak and no forward duration bridge exists. |
| `R13_HMAE_194_103140_C15_COPPER_HEADLINE_NO_BRIDGE` | `Stage2-Actionable` | 77.0 | `Stage2` | 61.0 | `current_profile_false_positive` | R13 cap prevents generic commodity-price beta from behaving like a company-specific rerating trigger. |
| `R13_HMAE_194_240810_C10_MEMORY_RECOVERY_FORECAST_NO_ORDER` | `Stage2-Actionable` | 74.0 | `Stage2` | 58.0 | `current_profile_false_positive` | Generic memory-cycle recovery is capped unless supplier-specific order or revenue conversion is visible. |
| `R13_HMAE_194_166090_C10_UTILIZATION_CONSUMABLES_HIGH_MAE` | `Stage2` | 66.0 | `Stage2` | 54.0 | `current_profile_correct_if_capped_at_stage2_but_not_actionable` | Stage2 can remain as an early-cycle observation, but high-MAE guardrail blocks Actionable/Yellow/Green escalation. |
| `R13_HMAE_194_033100_C02_TRANSFORMER_SHORTAGE_LATE_STAGE2A` | `Stage2-Actionable` | 72.0 | `Stage2` | 63.0 | `current_profile_false_positive_if_stage2_actionable_is_not_capped_by_entry_quality` | Real backlog/shortage evidence remains valuable, but high-MAE late-entry condition caps it below Yellow/Green. |
| `R13_HMAE_194_003670_C13_HIGH_MFE_HIGH_DRAWDOWN_WINNER` | `Stage2-Actionable` | 70.0 | `Stage2-Actionable` | 72.0 | `current_profile_missed_structural_if_capacity_JV_not_mapped_but_green_block_correct` | R13 high-MAE guardrail must not block all volatile winners; direct customer/JV capacity bridge preserves Stage2-Actionable while preventing Green. |
| `R13_HMAE_194_006400_C14_HARD_4C_SUCCESS_HIGH_MAE` | `Stage4C` | 34.0 | `Stage4C` | 31.0 | `current_profile_correct` | This is the control case showing that high-MAE guardrail should preserve true hard 4C when non-price thesis break is confirmed. |
| `R13_HMAE_194_010120_C02_LS_ELECTRIC_EXTENSION_4B` | `Stage2-Actionable` | 67.0 | `Stage4B` | 57.0 | `current_profile_correct_if_local_4B_not_hard_4C` | High MAE and extension should trigger local 4B watch, not hard 4C, because subsequent 180D MFE still reached 40.84%. |

The proposed R13 correction is not a weight delta. It is a parser/aggregator-facing audit rule: high-MAE representative rows should stress-test whether a trigger was too generic, too late, or missing non-price bridge before it contributes to any future promotion decision.

## 10. Stage3 Yellow / Green Lateness Audit

| status | value |
|---|---|
| Stage3-Green rows in this R13 compression | 0 |
| green_lateness_ratio | `not_applicable` |
| reason | `no_confirmed_Stage3_Green_trigger` |
| Stage3 implication | high-MAE rows with no direct order/customer/margin bridge must not loosen Green; true structural winner rows may remain Stage2-Actionable or Yellow watch, but not Green from price alone. |

## 11. 4B Timing Audit

| trigger_id | trigger_type | local/full timing verdict | evidence type | protection label |
|---|---|---|---|---|
| `R13_HMAE_194_T01` | `Stage2-Actionable` | `stage2_entry_was_already_cycle_peak` | `valuation_blowoff,margin_or_backlog_slowdown` | `thesis_break_watch_only` |
| `R13_HMAE_194_T02` | `Stage2-Actionable` | `stage2_entry_was_already_cycle_peak` | `valuation_blowoff,price_only` | `thesis_break_watch_only` |
| `R13_HMAE_194_T03` | `Stage2-Actionable` | `stage2_overpromotion_before_supplier_conversion` | `revision_slowdown,margin_or_backlog_slowdown` | `thesis_break_watch_only` |
| `R13_HMAE_194_T04` | `Stage2` | `high_mae_stage2_must_not_escalate_to_green` | `margin_or_backlog_slowdown,positioning_overheat` | `thesis_break_watch_only` |
| `R13_HMAE_194_T05` | `Stage2-Actionable` | `late_entry_guard_needed_before_green` | `valuation_blowoff,positioning_overheat` | `thesis_break_watch_only` |
| `R13_HMAE_194_T06` | `Stage2-Actionable` | `needs_local_4B_after_peak_not_initial_stage2_block` | `positioning_overheat,valuation_blowoff` | `false_break_if_initial_trigger_blocked` |
| `R13_HMAE_194_T07` | `Stage4C` | `hard_4c_good_timing_after_non_price_thesis_break` | `revision_slowdown,margin_or_backlog_slowdown` | `hard_4c_success` |
| `R13_HMAE_194_T08` | `Stage4B` | `good_local_4b_but_not_full_window_4c` | `positioning_overheat,valuation_blowoff` | `false_break_if_routed_to_hard_4c` |

R13 conclusion: local 4B must be allowed to exist without collapsing into hard 4C. LS ELECTRIC and POSCO Future M show later upside after high-MAE/extension conditions. Samsung SDI 2024 shows the opposite: when non-price thesis break is explicit, hard 4C must remain protected.

## 12. 4C Protection Audit

| case | label | rationale |
|---|---|---|
| `R13_HMAE_194_001230_C15_REBAR_SPREAD_LATE_CYCLE` | `thesis_break_watch_only` | Evidence supports watch/cap, not hard 4C. |
| `R13_HMAE_194_103140_C15_COPPER_HEADLINE_NO_BRIDGE` | `thesis_break_watch_only` | Evidence supports watch/cap, not hard 4C. |
| `R13_HMAE_194_240810_C10_MEMORY_RECOVERY_FORECAST_NO_ORDER` | `thesis_break_watch_only` | Evidence supports watch/cap, not hard 4C. |
| `R13_HMAE_194_166090_C10_UTILIZATION_CONSUMABLES_HIGH_MAE` | `thesis_break_watch_only` | Evidence supports watch/cap, not hard 4C. |
| `R13_HMAE_194_033100_C02_TRANSFORMER_SHORTAGE_LATE_STAGE2A` | `thesis_break_watch_only` | Evidence supports watch/cap, not hard 4C. |
| `R13_HMAE_194_003670_C13_HIGH_MFE_HIGH_DRAWDOWN_WINNER` | `false_break_if_initial_trigger_blocked` | Hard 4C would have overblocked later upside; hold as local 4B/watch. |
| `R13_HMAE_194_006400_C14_HARD_4C_SUCCESS_HIGH_MAE` | `hard_4c_success` | Non-price EV slowdown + utilization/profit collapse aligned with 180D downside. |
| `R13_HMAE_194_010120_C02_LS_ELECTRIC_EXTENSION_4B` | `false_break_if_routed_to_hard_4c` | Hard 4C would have overblocked later upside; hold as local 4B/watch. |

## 13. Score Component Breakdown

All scores are research proxies, not production scoring. The canonical component keys below are included to keep the row machine-readable.

### R13_HMAE_194_T01 — Dongkuk Steel legacy entity

```json
{
  "row_type": "score_simulation",
  "profile_id": "e2r_2_1_stock_web_calibrated_proxy_vs_R13_high_MAE_guard",
  "case_id": "R13_HMAE_194_001230_C15_REBAR_SPREAD_LATE_CYCLE",
  "trigger_id": "R13_HMAE_194_T01",
  "symbol": "001230",
  "source_canonical_archetype_id": "C15_MATERIAL_SPREAD_SUPERCYCLE",
  "raw_component_scores_before": {
    "contract_score": 0.25,
    "backlog_visibility_score": 0.2,
    "margin_bridge_score": 0.58,
    "revision_score": 0.62,
    "relative_strength_score": 0.66,
    "customer_quality_score": 0.2,
    "policy_or_regulatory_score": 0.1,
    "valuation_repricing_score": 0.74,
    "execution_risk_score": 0.55,
    "legal_or_contract_risk_score": 0.1,
    "dilution_cb_risk_score": 0.05,
    "accounting_trust_risk_score": 0.05
  },
  "weighted_score_before": 76.0,
  "stage_label_before": "Stage2-Actionable",
  "raw_component_scores_after": {
    "contract_score": 0.2,
    "backlog_visibility_score": 0.12,
    "margin_bridge_score": 0.35,
    "revision_score": 0.48,
    "relative_strength_score": 0.4,
    "customer_quality_score": 0.15,
    "policy_or_regulatory_score": 0.1,
    "valuation_repricing_score": 0.3,
    "execution_risk_score": 0.72,
    "legal_or_contract_risk_score": 0.1,
    "dilution_cb_risk_score": 0.05,
    "accounting_trust_risk_score": 0.05
  },
  "weighted_score_after": 60.0,
  "stage_label_after": "Stage2",
  "component_delta_explanation": "R13 cap blocks Stage2-Actionable when commodity/spread evidence appears on the entry-day peak and no forward duration bridge exists.",
  "production_scoring_changed": false,
  "do_not_propose_new_weight_delta": true
}
```

### R13_HMAE_194_T02 — Poongsan

```json
{
  "row_type": "score_simulation",
  "profile_id": "e2r_2_1_stock_web_calibrated_proxy_vs_R13_high_MAE_guard",
  "case_id": "R13_HMAE_194_103140_C15_COPPER_HEADLINE_NO_BRIDGE",
  "trigger_id": "R13_HMAE_194_T02",
  "symbol": "103140",
  "source_canonical_archetype_id": "C15_MATERIAL_SPREAD_SUPERCYCLE",
  "raw_component_scores_before": {
    "contract_score": 0.2,
    "backlog_visibility_score": 0.18,
    "margin_bridge_score": 0.55,
    "revision_score": 0.58,
    "relative_strength_score": 0.62,
    "customer_quality_score": 0.2,
    "policy_or_regulatory_score": 0.1,
    "valuation_repricing_score": 0.72,
    "execution_risk_score": 0.5,
    "legal_or_contract_risk_score": 0.1,
    "dilution_cb_risk_score": 0.05,
    "accounting_trust_risk_score": 0.05
  },
  "weighted_score_before": 77.0,
  "stage_label_before": "Stage2-Actionable",
  "raw_component_scores_after": {
    "contract_score": 0.15,
    "backlog_visibility_score": 0.12,
    "margin_bridge_score": 0.3,
    "revision_score": 0.42,
    "relative_strength_score": 0.35,
    "customer_quality_score": 0.15,
    "policy_or_regulatory_score": 0.1,
    "valuation_repricing_score": 0.28,
    "execution_risk_score": 0.7,
    "legal_or_contract_risk_score": 0.1,
    "dilution_cb_risk_score": 0.05,
    "accounting_trust_risk_score": 0.05
  },
  "weighted_score_after": 61.0,
  "stage_label_after": "Stage2",
  "component_delta_explanation": "R13 cap prevents generic commodity-price beta from behaving like a company-specific rerating trigger.",
  "production_scoring_changed": false,
  "do_not_propose_new_weight_delta": true
}
```

### R13_HMAE_194_T03 — Wonik IPS

```json
{
  "row_type": "score_simulation",
  "profile_id": "e2r_2_1_stock_web_calibrated_proxy_vs_R13_high_MAE_guard",
  "case_id": "R13_HMAE_194_240810_C10_MEMORY_RECOVERY_FORECAST_NO_ORDER",
  "trigger_id": "R13_HMAE_194_T03",
  "symbol": "240810",
  "source_canonical_archetype_id": "C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE",
  "raw_component_scores_before": {
    "contract_score": 0.25,
    "backlog_visibility_score": 0.2,
    "margin_bridge_score": 0.45,
    "revision_score": 0.58,
    "relative_strength_score": 0.55,
    "customer_quality_score": 0.25,
    "policy_or_regulatory_score": 0.1,
    "valuation_repricing_score": 0.52,
    "execution_risk_score": 0.58,
    "legal_or_contract_risk_score": 0.1,
    "dilution_cb_risk_score": 0.05,
    "accounting_trust_risk_score": 0.05
  },
  "weighted_score_before": 74.0,
  "stage_label_before": "Stage2-Actionable",
  "raw_component_scores_after": {
    "contract_score": 0.12,
    "backlog_visibility_score": 0.1,
    "margin_bridge_score": 0.25,
    "revision_score": 0.38,
    "relative_strength_score": 0.38,
    "customer_quality_score": 0.18,
    "policy_or_regulatory_score": 0.1,
    "valuation_repricing_score": 0.3,
    "execution_risk_score": 0.74,
    "legal_or_contract_risk_score": 0.1,
    "dilution_cb_risk_score": 0.05,
    "accounting_trust_risk_score": 0.05
  },
  "weighted_score_after": 58.0,
  "stage_label_after": "Stage2",
  "component_delta_explanation": "Generic memory-cycle recovery is capped unless supplier-specific order or revenue conversion is visible.",
  "production_scoring_changed": false,
  "do_not_propose_new_weight_delta": true
}
```

### R13_HMAE_194_T04 — Hana Materials

```json
{
  "row_type": "score_simulation",
  "profile_id": "e2r_2_1_stock_web_calibrated_proxy_vs_R13_high_MAE_guard",
  "case_id": "R13_HMAE_194_166090_C10_UTILIZATION_CONSUMABLES_HIGH_MAE",
  "trigger_id": "R13_HMAE_194_T04",
  "symbol": "166090",
  "source_canonical_archetype_id": "C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE",
  "raw_component_scores_before": {
    "contract_score": 0.18,
    "backlog_visibility_score": 0.18,
    "margin_bridge_score": 0.38,
    "revision_score": 0.52,
    "relative_strength_score": 0.55,
    "customer_quality_score": 0.25,
    "policy_or_regulatory_score": 0.08,
    "valuation_repricing_score": 0.45,
    "execution_risk_score": 0.62,
    "legal_or_contract_risk_score": 0.08,
    "dilution_cb_risk_score": 0.05,
    "accounting_trust_risk_score": 0.05
  },
  "weighted_score_before": 66.0,
  "stage_label_before": "Stage2",
  "raw_component_scores_after": {
    "contract_score": 0.1,
    "backlog_visibility_score": 0.1,
    "margin_bridge_score": 0.22,
    "revision_score": 0.36,
    "relative_strength_score": 0.32,
    "customer_quality_score": 0.18,
    "policy_or_regulatory_score": 0.08,
    "valuation_repricing_score": 0.25,
    "execution_risk_score": 0.82,
    "legal_or_contract_risk_score": 0.08,
    "dilution_cb_risk_score": 0.05,
    "accounting_trust_risk_score": 0.05
  },
  "weighted_score_after": 54.0,
  "stage_label_after": "Stage2",
  "component_delta_explanation": "Stage2 can remain as an early-cycle observation, but high-MAE guardrail blocks Actionable/Yellow/Green escalation.",
  "production_scoring_changed": false,
  "do_not_propose_new_weight_delta": true
}
```

### R13_HMAE_194_T05 — JeRyong Electric

```json
{
  "row_type": "score_simulation",
  "profile_id": "e2r_2_1_stock_web_calibrated_proxy_vs_R13_high_MAE_guard",
  "case_id": "R13_HMAE_194_033100_C02_TRANSFORMER_SHORTAGE_LATE_STAGE2A",
  "trigger_id": "R13_HMAE_194_T05",
  "symbol": "033100",
  "source_canonical_archetype_id": "C02_POWER_GRID_DATACENTER_CAPEX",
  "raw_component_scores_before": {
    "contract_score": 0.62,
    "backlog_visibility_score": 0.72,
    "margin_bridge_score": 0.6,
    "revision_score": 0.68,
    "relative_strength_score": 0.74,
    "customer_quality_score": 0.52,
    "policy_or_regulatory_score": 0.3,
    "valuation_repricing_score": 0.78,
    "execution_risk_score": 0.6,
    "legal_or_contract_risk_score": 0.1,
    "dilution_cb_risk_score": 0.05,
    "accounting_trust_risk_score": 0.05
  },
  "weighted_score_before": 72.0,
  "stage_label_before": "Stage2-Actionable",
  "raw_component_scores_after": {
    "contract_score": 0.58,
    "backlog_visibility_score": 0.68,
    "margin_bridge_score": 0.48,
    "revision_score": 0.56,
    "relative_strength_score": 0.46,
    "customer_quality_score": 0.48,
    "policy_or_regulatory_score": 0.3,
    "valuation_repricing_score": 0.35,
    "execution_risk_score": 0.82,
    "legal_or_contract_risk_score": 0.1,
    "dilution_cb_risk_score": 0.05,
    "accounting_trust_risk_score": 0.05
  },
  "weighted_score_after": 63.0,
  "stage_label_after": "Stage2",
  "component_delta_explanation": "Real backlog/shortage evidence remains valuable, but high-MAE late-entry condition caps it below Yellow/Green.",
  "production_scoring_changed": false,
  "do_not_propose_new_weight_delta": true
}
```

### R13_HMAE_194_T06 — POSCO Future M

```json
{
  "row_type": "score_simulation",
  "profile_id": "e2r_2_1_stock_web_calibrated_proxy_vs_R13_high_MAE_guard",
  "case_id": "R13_HMAE_194_003670_C13_HIGH_MFE_HIGH_DRAWDOWN_WINNER",
  "trigger_id": "R13_HMAE_194_T06",
  "symbol": "003670",
  "source_canonical_archetype_id": "C13_BATTERY_JV_UTILIZATION_AMPC_IRA",
  "raw_component_scores_before": {
    "contract_score": 0.82,
    "backlog_visibility_score": 0.66,
    "margin_bridge_score": 0.34,
    "revision_score": 0.44,
    "relative_strength_score": 0.76,
    "customer_quality_score": 0.9,
    "policy_or_regulatory_score": 0.76,
    "valuation_repricing_score": 0.72,
    "execution_risk_score": 0.48,
    "legal_or_contract_risk_score": 0.12,
    "dilution_cb_risk_score": 0.08,
    "accounting_trust_risk_score": 0.05
  },
  "weighted_score_before": 70.0,
  "stage_label_before": "Stage2-Actionable",
  "raw_component_scores_after": {
    "contract_score": 0.86,
    "backlog_visibility_score": 0.7,
    "margin_bridge_score": 0.32,
    "revision_score": 0.42,
    "relative_strength_score": 0.62,
    "customer_quality_score": 0.9,
    "policy_or_regulatory_score": 0.76,
    "valuation_repricing_score": 0.46,
    "execution_risk_score": 0.62,
    "legal_or_contract_risk_score": 0.12,
    "dilution_cb_risk_score": 0.08,
    "accounting_trust_risk_score": 0.05
  },
  "weighted_score_after": 72.0,
  "stage_label_after": "Stage2-Actionable",
  "component_delta_explanation": "R13 high-MAE guardrail must not block all volatile winners; direct customer/JV capacity bridge preserves Stage2-Actionable while preventing Green.",
  "production_scoring_changed": false,
  "do_not_propose_new_weight_delta": true
}
```

### R13_HMAE_194_T07 — Samsung SDI

```json
{
  "row_type": "score_simulation",
  "profile_id": "e2r_2_1_stock_web_calibrated_proxy_vs_R13_high_MAE_guard",
  "case_id": "R13_HMAE_194_006400_C14_HARD_4C_SUCCESS_HIGH_MAE",
  "trigger_id": "R13_HMAE_194_T07",
  "symbol": "006400",
  "source_canonical_archetype_id": "C14_EV_DEMAND_SLOWDOWN_4B_4C",
  "raw_component_scores_before": {
    "contract_score": 0.15,
    "backlog_visibility_score": 0.1,
    "margin_bridge_score": 0.06,
    "revision_score": 0.08,
    "relative_strength_score": 0.2,
    "customer_quality_score": 0.35,
    "policy_or_regulatory_score": 0.3,
    "valuation_repricing_score": 0.22,
    "execution_risk_score": 0.9,
    "legal_or_contract_risk_score": 0.15,
    "dilution_cb_risk_score": 0.1,
    "accounting_trust_risk_score": 0.08
  },
  "weighted_score_before": 34.0,
  "stage_label_before": "Stage4C",
  "raw_component_scores_after": {
    "contract_score": 0.12,
    "backlog_visibility_score": 0.08,
    "margin_bridge_score": 0.03,
    "revision_score": 0.05,
    "relative_strength_score": 0.18,
    "customer_quality_score": 0.32,
    "policy_or_regulatory_score": 0.25,
    "valuation_repricing_score": 0.18,
    "execution_risk_score": 0.96,
    "legal_or_contract_risk_score": 0.15,
    "dilution_cb_risk_score": 0.1,
    "accounting_trust_risk_score": 0.08
  },
  "weighted_score_after": 31.0,
  "stage_label_after": "Stage4C",
  "component_delta_explanation": "This is the control case showing that high-MAE guardrail should preserve true hard 4C when non-price thesis break is confirmed.",
  "production_scoring_changed": false,
  "do_not_propose_new_weight_delta": true
}
```

### R13_HMAE_194_T08 — LS ELECTRIC

```json
{
  "row_type": "score_simulation",
  "profile_id": "e2r_2_1_stock_web_calibrated_proxy_vs_R13_high_MAE_guard",
  "case_id": "R13_HMAE_194_010120_C02_LS_ELECTRIC_EXTENSION_4B",
  "trigger_id": "R13_HMAE_194_T08",
  "symbol": "010120",
  "source_canonical_archetype_id": "C02_POWER_GRID_DATACENTER_CAPEX",
  "raw_component_scores_before": {
    "contract_score": 0.68,
    "backlog_visibility_score": 0.74,
    "margin_bridge_score": 0.72,
    "revision_score": 0.7,
    "relative_strength_score": 0.78,
    "customer_quality_score": 0.62,
    "policy_or_regulatory_score": 0.3,
    "valuation_repricing_score": 0.82,
    "execution_risk_score": 0.58,
    "legal_or_contract_risk_score": 0.1,
    "dilution_cb_risk_score": 0.05,
    "accounting_trust_risk_score": 0.05
  },
  "weighted_score_before": 67.0,
  "stage_label_before": "Stage2-Actionable",
  "raw_component_scores_after": {
    "contract_score": 0.66,
    "backlog_visibility_score": 0.72,
    "margin_bridge_score": 0.66,
    "revision_score": 0.62,
    "relative_strength_score": 0.48,
    "customer_quality_score": 0.6,
    "policy_or_regulatory_score": 0.3,
    "valuation_repricing_score": 0.36,
    "execution_risk_score": 0.78,
    "legal_or_contract_risk_score": 0.1,
    "dilution_cb_risk_score": 0.05,
    "accounting_trust_risk_score": 0.05
  },
  "weighted_score_after": 57.0,
  "stage_label_after": "Stage4B",
  "component_delta_explanation": "High MAE and extension should trigger local 4B watch, not hard 4C, because subsequent 180D MFE still reached 40.84%.",
  "production_scoring_changed": false,
  "do_not_propose_new_weight_delta": true
}
```

## 14. Profile Comparison

| profile_id | scope | changed_axes | eligible | avg_MFE90 | avg_MAE90 | avg_MFE180 | avg_MAE180 | false_positive_rate | verdict |
|---|---|---|---:|---:|---:|---:|---:|---:|---|
| `P0_e2r_2_1_stock_web_calibrated_proxy` | `current_proxy` | `none` | 8 | 20.84 | -38.56 | 23.53 | -46.98 | 0.625 | `residual_high_MAE_false_positive_risk_remains` |
| `P0b_e2r_2_0_baseline_reference` | `rollback_reference` | `rollback_reference_only` | 8 | 20.84 | -38.56 | 23.53 | -46.98 | 0.75 | `worse_than_current_proxy` |
| `P1_R13_high_MAE_stage_escalation_brake` | `global_candidate_audit_only` | `no_weight_delta; audit tag only` | 8 | 20.84 | -38.56 | 23.53 | -46.98 | 0.25 | `best_holdout_alignment_without_weight_delta` |
| `P2_source_canonical_specific_existing_guards` | `canonical_existing_axis_stress_test` | `stage2_required_bridge|local_4b_watch_guard|hard_4c_confirmation` | 8 | 20.84 | -38.56 | 23.53 | -46.98 | 0.375 | `acceptable_if_representative_compression_is_used` |
| `P3_counterexample_guard_profile` | `guard_profile` | `data_quality_guard_only` | 8 | 20.84 | -38.56 | 23.53 | -46.98 | 0.125 | `safe_but_may_under_credit_structural_winners` |

## 15. Residual Contribution

| field | value |
|---|---|
| `rule_scope` | `no_new_rule` |
| `sector_specific_rule_candidate` | `none` |
| `canonical_archetype_rule_candidate` | `R13_HIGH_MAE_GREEN_AND_ACTIONABLE_CAP` |
| `new_axis_proposed` | `false` |
| `existing_axis_strengthened` | `stage2_required_bridge|stage3_green_not_loosened|local_4b_watch_guard|hard_4c_confirmation` |
| `existing_axis_weakened` | `none` |
| `production_scoring_changed` | `false` |
| `shadow_weight_only` | `true` |
| `do_not_propose_new_weight_delta` | `true` |
| `residual_summary` | `High-MAE rows should become representative stress-test rows, not fresh promotion evidence. MAE is used as an escalation brake only after checking evidence quality and 4B/4C context.` |

## 16. Shadow Weight Proposal

No new numerical weight delta is proposed. The only shadow artifact is a zero-delta audit marker.

```csv
row_type,axis,scope,large_sector_id,canonical_archetype_id,old_weight,new_weight,delta,evidence_summary,expected_effect,representative_trigger_ids,usable_trigger_count,positive_count,counterexample_count,confidence,application_status,notes
shadow_weight,R13_HIGH_MAE_REPRESENTATIVE_COMPRESSION,global_candidate_audit_only,L10_POLICY_EVENT_CROSS_REDTEAM_MISC,R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL,0,0,0,"Compress high-MAE representative rows across C02/C10/C13/C14/C15 without adding new independent evidence weight","prevents reused high-MAE rows from inflating future promotion decisions while preserving true 4C and true structural controls","R13_HMAE_194_T01|R13_HMAE_194_T02|R13_HMAE_194_T03|R13_HMAE_194_T04|R13_HMAE_194_T05|R13_HMAE_194_T06|R13_HMAE_194_T07|R13_HMAE_194_T08",8,3,5,medium,holdout_audit_only,"do_not_propose_new_weight_delta=true; production scoring unchanged"
```

## 17. Machine-Readable Rows

Every `trigger` row includes canonical MFE/MAE keys for 30D/90D/180D and explicit Stock-Web source fields. Rows are marked as reused representative holdout audit rows, not new independent evidence.

```jsonl
{"row_type":"case","research_file":"e2r_stock_web_v12_residual_round_R13_loop_194_L10_POLICY_EVENT_CROSS_REDTEAM_MISC_R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL_research.md","case_id":"R13_HMAE_194_001230_C15_REBAR_SPREAD_LATE_CYCLE","round":"R13","loop":"194","large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL","fine_archetype_id":"R13_HIGH_MAE_REPRESENTATIVE_COMPRESSION","source_research_file":"e2r_stock_web_v12_residual_round_R4_loop_191_L4_MATERIALS_SPREAD_RESOURCE_C15_MATERIAL_SPREAD_SUPERCYCLE_research.md","source_case_id":"C15-001230-20210517-STAGE2A","source_trigger_id":"C15-001230-20210517-STAGE2A","source_large_sector_id":"L4_MATERIALS_SPREAD_RESOURCE","source_canonical_archetype_id":"C15_MATERIAL_SPREAD_SUPERCYCLE","source_fine_archetype_id":"REBAR_SPREAD_LATE_CYCLE_BLOWOFF","symbol":"001230","company_name":"Dongkuk Steel legacy entity","best_trigger":"R13_HMAE_194_T01","case_type":"representative_high_MAE_false_positive","positive_or_counterexample":"counterexample","score_price_alignment":"late_cycle_spread_stage2_actionable_false_positive","current_profile_verdict":"current_profile_false_positive","price_source":"Songdaiki/stock-web","calibration_usable":true,"is_new_independent_case":false,"reuse_reason":"R13 representative compression of existing validated v12 trigger row; no new independent evidence weight.","independent_evidence_weight":0.0,"do_not_count_as_new_case":true,"do_not_propose_new_weight_delta":true,"notes":"R13 cap blocks Stage2-Actionable when commodity/spread evidence appears on the entry-day peak and no forward duration bridge exists."}
{"row_type":"trigger","research_file":"e2r_stock_web_v12_residual_round_R13_loop_194_L10_POLICY_EVENT_CROSS_REDTEAM_MISC_R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL_research.md","trigger_id":"R13_HMAE_194_T01","case_id":"R13_HMAE_194_001230_C15_REBAR_SPREAD_LATE_CYCLE","symbol":"001230","company_name":"Dongkuk Steel legacy entity","market":"KOSPI","round":"R13","loop":"194","large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL","fine_archetype_id":"R13_HIGH_MAE_REPRESENTATIVE_COMPRESSION","sector":"cross_archetype_redteam_misc","primary_archetype":"R13_high_MAE_guardrail","source_research_file":"e2r_stock_web_v12_residual_round_R4_loop_191_L4_MATERIALS_SPREAD_RESOURCE_C15_MATERIAL_SPREAD_SUPERCYCLE_research.md","source_trigger_id":"C15-001230-20210517-STAGE2A","source_large_sector_id":"L4_MATERIALS_SPREAD_RESOURCE","source_canonical_archetype_id":"C15_MATERIAL_SPREAD_SUPERCYCLE","source_fine_archetype_id":"REBAR_SPREAD_LATE_CYCLE_BLOWOFF","loop_objective":"R13 high-MAE cross-archetype holdout validation; representative compression only.","trigger_type":"Stage2-Actionable","trigger_date":"2021-05-17","evidence_available_at_that_date":"Dongkuk Steel's Q1 profit and rebar-price strength arrived after the steel/rebar cycle had already run hard.","evidence_source":"https://www.kedglobal.com/earnings/newsView/ked202105170018","stage2_evidence_fields":["rebar price increase","Q1 operating profit spike","commodity spread language"],"stage3_evidence_fields":[],"stage4b_evidence_fields":["price/commodity cycle already near peak","no company-specific forward spread-duration evidence"],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/001/001230/2021.csv; atlas/ohlcv_tradable_by_symbol_year/001/001230/2022.csv","profile_path":"atlas/symbol_profiles/001/001230.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","entry_date":"2021-05-18","entry_price":25250,"actual_1d_ohlc_row":{"o":23750,"h":25900,"l":23500,"c":25250,"v":5334664},"MFE_30D_pct":2.57,"MFE_90D_pct":2.57,"MFE_180D_pct":2.57,"MFE_1Y_pct":null,"MFE_2Y_pct":null,"MAE_30D_pct":-18.81,"MAE_90D_pct":-30.69,"MAE_180D_pct":-46.93,"MAE_1Y_pct":null,"MAE_2Y_pct":null,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2021-05-18","peak_price":25900,"trough_date":"2022-01-27","trough_price":13400,"drawdown_after_peak_pct":-48.26,"green_lateness_ratio":"not_applicable_no_confirmed_Stage3_Green_trigger","four_b_local_peak_proximity":"not_comparable_cross_case","four_b_full_window_peak_proximity":"not_comparable_cross_case","four_b_timing_verdict":"stage2_entry_was_already_cycle_peak","four_b_evidence_type":["valuation_blowoff","margin_or_backlog_slowdown"],"four_c_protection_label":"thesis_break_watch_only","trigger_outcome_label":"late_cycle_spread_stage2_actionable_false_positive","current_profile_verdict":"current_profile_false_positive","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL|001230|Stage2-Actionable|2021-05-18","dedupe_for_aggregate":true,"aggregate_group_role":"representative_holdout_audit","is_new_independent_case":false,"reuse_reason":"R13 representative compression of prior v12 validated row; no new independent evidence weight.","independent_evidence_weight":0.0,"do_not_count_as_new_case":true,"source_proxy_only":false,"evidence_url_pending":false,"do_not_propose_new_weight_delta":true}
{"row_type":"score_simulation","research_file":"e2r_stock_web_v12_residual_round_R13_loop_194_L10_POLICY_EVENT_CROSS_REDTEAM_MISC_R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL_research.md","profile_id":"R13_high_MAE_representative_guard","case_id":"R13_HMAE_194_001230_C15_REBAR_SPREAD_LATE_CYCLE","trigger_id":"R13_HMAE_194_T01","symbol":"001230","round":"R13","loop":"194","large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL","source_canonical_archetype_id":"C15_MATERIAL_SPREAD_SUPERCYCLE","raw_component_scores_before":{"contract_score":0.25,"backlog_visibility_score":0.2,"margin_bridge_score":0.58,"revision_score":0.62,"relative_strength_score":0.66,"customer_quality_score":0.2,"policy_or_regulatory_score":0.1,"valuation_repricing_score":0.74,"execution_risk_score":0.55,"legal_or_contract_risk_score":0.1,"dilution_cb_risk_score":0.05,"accounting_trust_risk_score":0.05},"weighted_score_before":76.0,"stage_label_before":"Stage2-Actionable","raw_component_scores_after":{"contract_score":0.2,"backlog_visibility_score":0.12,"margin_bridge_score":0.35,"revision_score":0.48,"relative_strength_score":0.4,"customer_quality_score":0.15,"policy_or_regulatory_score":0.1,"valuation_repricing_score":0.3,"execution_risk_score":0.72,"legal_or_contract_risk_score":0.1,"dilution_cb_risk_score":0.05,"accounting_trust_risk_score":0.05},"weighted_score_after":60.0,"stage_label_after":"Stage2","component_delta_explanation":"R13 cap blocks Stage2-Actionable when commodity/spread evidence appears on the entry-day peak and no forward duration bridge exists.","production_scoring_changed":false,"do_not_propose_new_weight_delta":true,"MFE_90D_pct":2.57,"MAE_90D_pct":-30.69,"MFE_180D_pct":2.57,"MAE_180D_pct":-46.93,"score_return_alignment_label":"late_cycle_spread_stage2_actionable_false_positive","current_profile_verdict":"current_profile_false_positive"}
{"row_type":"case","research_file":"e2r_stock_web_v12_residual_round_R13_loop_194_L10_POLICY_EVENT_CROSS_REDTEAM_MISC_R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL_research.md","case_id":"R13_HMAE_194_103140_C15_COPPER_HEADLINE_NO_BRIDGE","round":"R13","loop":"194","large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL","fine_archetype_id":"R13_HIGH_MAE_REPRESENTATIVE_COMPRESSION","source_research_file":"e2r_stock_web_v12_residual_round_R4_loop_191_L4_MATERIALS_SPREAD_RESOURCE_C15_MATERIAL_SPREAD_SUPERCYCLE_research.md","source_case_id":"C15-103140-20240514-STAGE2A","source_trigger_id":"C15-103140-20240514-STAGE2A","source_large_sector_id":"L4_MATERIALS_SPREAD_RESOURCE","source_canonical_archetype_id":"C15_MATERIAL_SPREAD_SUPERCYCLE","source_fine_archetype_id":"COPPER_PRICE_THESIS_WITH_VOLUME_COST_OFFSET","symbol":"103140","company_name":"Poongsan","best_trigger":"R13_HMAE_194_T02","case_type":"representative_high_MAE_false_positive","positive_or_counterexample":"counterexample","score_price_alignment":"copper_headline_without_volume_margin_bridge","current_profile_verdict":"current_profile_false_positive","price_source":"Songdaiki/stock-web","calibration_usable":true,"is_new_independent_case":false,"reuse_reason":"R13 representative compression of existing validated v12 trigger row; no new independent evidence weight.","independent_evidence_weight":0.0,"do_not_count_as_new_case":true,"do_not_propose_new_weight_delta":true,"notes":"R13 cap prevents generic commodity-price beta from behaving like a company-specific rerating trigger."}
{"row_type":"trigger","research_file":"e2r_stock_web_v12_residual_round_R13_loop_194_L10_POLICY_EVENT_CROSS_REDTEAM_MISC_R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL_research.md","trigger_id":"R13_HMAE_194_T02","case_id":"R13_HMAE_194_103140_C15_COPPER_HEADLINE_NO_BRIDGE","symbol":"103140","company_name":"Poongsan","market":"KOSPI","round":"R13","loop":"194","large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL","fine_archetype_id":"R13_HIGH_MAE_REPRESENTATIVE_COMPRESSION","sector":"cross_archetype_redteam_misc","primary_archetype":"R13_high_MAE_guardrail","source_research_file":"e2r_stock_web_v12_residual_round_R4_loop_191_L4_MATERIALS_SPREAD_RESOURCE_C15_MATERIAL_SPREAD_SUPERCYCLE_research.md","source_trigger_id":"C15-103140-20240514-STAGE2A","source_large_sector_id":"L4_MATERIALS_SPREAD_RESOURCE","source_canonical_archetype_id":"C15_MATERIAL_SPREAD_SUPERCYCLE","source_fine_archetype_id":"COPPER_PRICE_THESIS_WITH_VOLUME_COST_OFFSET","loop_objective":"R13 high-MAE cross-archetype holdout validation; representative compression only.","trigger_type":"Stage2-Actionable","trigger_date":"2024-05-14","evidence_available_at_that_date":"Copper-price and defense-seasonality narrative was present, but company-specific volume/cost conversion remained thin.","evidence_source":"https://v.daum.net/v/fXzID0JqJ6?f=p","stage2_evidence_fields":["copper price rally","defense sales seasonality","earnings expectation language"],"stage3_evidence_fields":[],"stage4b_evidence_fields":["entry-day peak proximity","commodity headline without company-level bridge"],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/103/103140/2024.csv; atlas/ohlcv_tradable_by_symbol_year/103/103140/2025.csv; atlas/ohlcv_tradable_by_symbol_year/103/103140/2026.csv","profile_path":"atlas/symbol_profiles/103/103140.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","entry_date":"2024-05-16","entry_price":77300,"actual_1d_ohlc_row":{"o":78000,"h":78000,"l":74400,"c":77300,"v":562357},"MFE_30D_pct":0.91,"MFE_90D_pct":0.91,"MFE_180D_pct":0.91,"MFE_1Y_pct":null,"MFE_2Y_pct":null,"MAE_30D_pct":-28.07,"MAE_90D_pct":-39.2,"MAE_180D_pct":-40.3,"MAE_1Y_pct":null,"MAE_2Y_pct":null,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-05-16","peak_price":78000,"trough_date":"2024-12-09","trough_price":46150,"drawdown_after_peak_pct":-40.83,"green_lateness_ratio":"not_applicable_no_confirmed_Stage3_Green_trigger","four_b_local_peak_proximity":"not_comparable_cross_case","four_b_full_window_peak_proximity":"not_comparable_cross_case","four_b_timing_verdict":"stage2_entry_was_already_cycle_peak","four_b_evidence_type":["valuation_blowoff","price_only"],"four_c_protection_label":"thesis_break_watch_only","trigger_outcome_label":"copper_headline_without_volume_margin_bridge","current_profile_verdict":"current_profile_false_positive","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL|103140|Stage2-Actionable|2024-05-16","dedupe_for_aggregate":true,"aggregate_group_role":"representative_holdout_audit","is_new_independent_case":false,"reuse_reason":"R13 representative compression of prior v12 validated row; no new independent evidence weight.","independent_evidence_weight":0.0,"do_not_count_as_new_case":true,"source_proxy_only":false,"evidence_url_pending":false,"do_not_propose_new_weight_delta":true}
{"row_type":"score_simulation","research_file":"e2r_stock_web_v12_residual_round_R13_loop_194_L10_POLICY_EVENT_CROSS_REDTEAM_MISC_R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL_research.md","profile_id":"R13_high_MAE_representative_guard","case_id":"R13_HMAE_194_103140_C15_COPPER_HEADLINE_NO_BRIDGE","trigger_id":"R13_HMAE_194_T02","symbol":"103140","round":"R13","loop":"194","large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL","source_canonical_archetype_id":"C15_MATERIAL_SPREAD_SUPERCYCLE","raw_component_scores_before":{"contract_score":0.2,"backlog_visibility_score":0.18,"margin_bridge_score":0.55,"revision_score":0.58,"relative_strength_score":0.62,"customer_quality_score":0.2,"policy_or_regulatory_score":0.1,"valuation_repricing_score":0.72,"execution_risk_score":0.5,"legal_or_contract_risk_score":0.1,"dilution_cb_risk_score":0.05,"accounting_trust_risk_score":0.05},"weighted_score_before":77.0,"stage_label_before":"Stage2-Actionable","raw_component_scores_after":{"contract_score":0.15,"backlog_visibility_score":0.12,"margin_bridge_score":0.3,"revision_score":0.42,"relative_strength_score":0.35,"customer_quality_score":0.15,"policy_or_regulatory_score":0.1,"valuation_repricing_score":0.28,"execution_risk_score":0.7,"legal_or_contract_risk_score":0.1,"dilution_cb_risk_score":0.05,"accounting_trust_risk_score":0.05},"weighted_score_after":61.0,"stage_label_after":"Stage2","component_delta_explanation":"R13 cap prevents generic commodity-price beta from behaving like a company-specific rerating trigger.","production_scoring_changed":false,"do_not_propose_new_weight_delta":true,"MFE_90D_pct":0.91,"MAE_90D_pct":-39.2,"MFE_180D_pct":0.91,"MAE_180D_pct":-40.3,"score_return_alignment_label":"copper_headline_without_volume_margin_bridge","current_profile_verdict":"current_profile_false_positive"}
{"row_type":"case","research_file":"e2r_stock_web_v12_residual_round_R13_loop_194_L10_POLICY_EVENT_CROSS_REDTEAM_MISC_R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL_research.md","case_id":"R13_HMAE_194_240810_C10_MEMORY_RECOVERY_FORECAST_NO_ORDER","round":"R13","loop":"194","large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL","fine_archetype_id":"R13_HIGH_MAE_REPRESENTATIVE_COMPRESSION","source_research_file":"e2r_stock_web_v12_residual_round_R2_loop_193_L2_AI_SEMICONDUCTOR_ELECTRONICS_C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE_research.md","source_case_id":"C10_193_01_WONIK_IPS_2H24_PROFIT_TURN_FALSE_POSITIVE","source_trigger_id":"C10_193_T01","source_large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","source_canonical_archetype_id":"C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE","source_fine_archetype_id":"MEMORY_CAPEX_RECOVERY_ORDER_CONVERSION_GUARD","symbol":"240810","company_name":"Wonik IPS","best_trigger":"R13_HMAE_194_T03","case_type":"representative_high_MAE_false_positive","positive_or_counterexample":"counterexample","score_price_alignment":"memory_recovery_forecast_without_order_conversion","current_profile_verdict":"current_profile_false_positive","price_source":"Songdaiki/stock-web","calibration_usable":true,"is_new_independent_case":false,"reuse_reason":"R13 representative compression of existing validated v12 trigger row; no new independent evidence weight.","independent_evidence_weight":0.0,"do_not_count_as_new_case":true,"do_not_propose_new_weight_delta":true,"notes":"Generic memory-cycle recovery is capped unless supplier-specific order or revenue conversion is visible."}
{"row_type":"trigger","research_file":"e2r_stock_web_v12_residual_round_R13_loop_194_L10_POLICY_EVENT_CROSS_REDTEAM_MISC_R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL_research.md","trigger_id":"R13_HMAE_194_T03","case_id":"R13_HMAE_194_240810_C10_MEMORY_RECOVERY_FORECAST_NO_ORDER","symbol":"240810","company_name":"Wonik IPS","market":"KOSDAQ","round":"R13","loop":"194","large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL","fine_archetype_id":"R13_HIGH_MAE_REPRESENTATIVE_COMPRESSION","sector":"cross_archetype_redteam_misc","primary_archetype":"R13_high_MAE_guardrail","source_research_file":"e2r_stock_web_v12_residual_round_R2_loop_193_L2_AI_SEMICONDUCTOR_ELECTRONICS_C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE_research.md","source_trigger_id":"C10_193_T01","source_large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","source_canonical_archetype_id":"C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE","source_fine_archetype_id":"MEMORY_CAPEX_RECOVERY_ORDER_CONVERSION_GUARD","loop_objective":"R13 high-MAE cross-archetype holdout validation; representative compression only.","trigger_type":"Stage2-Actionable","trigger_date":"2024-07-30","evidence_available_at_that_date":"Broker/news profit-turn expectation referenced memory-cycle recovery but not a firm supplier-level order conversion.","evidence_source":"https://www.asiae.co.kr/en/article/2024073007450660238","stage2_evidence_fields":["2H24 profit-turn expectation","memory recovery narrative"],"stage3_evidence_fields":[],"stage4b_evidence_fields":["no order conversion","high 90D/180D MAE"],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/240/240810/2024.csv; atlas/ohlcv_tradable_by_symbol_year/240/240810/2025.csv","profile_path":"atlas/symbol_profiles/240/240810.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","entry_date":"2024-07-30","entry_price":35200,"actual_1d_ohlc_row":{"o":34800,"h":35350,"l":34200,"c":35200,"v":144309},"MFE_30D_pct":9.38,"MFE_90D_pct":9.38,"MFE_180D_pct":9.38,"MFE_1Y_pct":null,"MFE_2Y_pct":null,"MAE_30D_pct":-17.47,"MAE_90D_pct":-39.91,"MAE_180D_pct":-40.91,"MAE_1Y_pct":null,"MAE_2Y_pct":null,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-08-21","peak_price":38500,"trough_date":"2025-04-28","trough_price":20800,"drawdown_after_peak_pct":-45.97,"green_lateness_ratio":"not_applicable_no_confirmed_Stage3_Green_trigger","four_b_local_peak_proximity":"not_comparable_cross_case","four_b_full_window_peak_proximity":"not_comparable_cross_case","four_b_timing_verdict":"stage2_overpromotion_before_supplier_conversion","four_b_evidence_type":["revision_slowdown","margin_or_backlog_slowdown"],"four_c_protection_label":"thesis_break_watch_only","trigger_outcome_label":"memory_recovery_forecast_without_order_conversion","current_profile_verdict":"current_profile_false_positive","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL|240810|Stage2-Actionable|2024-07-30","dedupe_for_aggregate":true,"aggregate_group_role":"representative_holdout_audit","is_new_independent_case":false,"reuse_reason":"R13 representative compression of prior v12 validated row; no new independent evidence weight.","independent_evidence_weight":0.0,"do_not_count_as_new_case":true,"source_proxy_only":false,"evidence_url_pending":false,"do_not_propose_new_weight_delta":true}
{"row_type":"score_simulation","research_file":"e2r_stock_web_v12_residual_round_R13_loop_194_L10_POLICY_EVENT_CROSS_REDTEAM_MISC_R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL_research.md","profile_id":"R13_high_MAE_representative_guard","case_id":"R13_HMAE_194_240810_C10_MEMORY_RECOVERY_FORECAST_NO_ORDER","trigger_id":"R13_HMAE_194_T03","symbol":"240810","round":"R13","loop":"194","large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL","source_canonical_archetype_id":"C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE","raw_component_scores_before":{"contract_score":0.25,"backlog_visibility_score":0.2,"margin_bridge_score":0.45,"revision_score":0.58,"relative_strength_score":0.55,"customer_quality_score":0.25,"policy_or_regulatory_score":0.1,"valuation_repricing_score":0.52,"execution_risk_score":0.58,"legal_or_contract_risk_score":0.1,"dilution_cb_risk_score":0.05,"accounting_trust_risk_score":0.05},"weighted_score_before":74.0,"stage_label_before":"Stage2-Actionable","raw_component_scores_after":{"contract_score":0.12,"backlog_visibility_score":0.1,"margin_bridge_score":0.25,"revision_score":0.38,"relative_strength_score":0.38,"customer_quality_score":0.18,"policy_or_regulatory_score":0.1,"valuation_repricing_score":0.3,"execution_risk_score":0.74,"legal_or_contract_risk_score":0.1,"dilution_cb_risk_score":0.05,"accounting_trust_risk_score":0.05},"weighted_score_after":58.0,"stage_label_after":"Stage2","component_delta_explanation":"Generic memory-cycle recovery is capped unless supplier-specific order or revenue conversion is visible.","production_scoring_changed":false,"do_not_propose_new_weight_delta":true,"MFE_90D_pct":9.38,"MAE_90D_pct":-39.91,"MFE_180D_pct":9.38,"MAE_180D_pct":-40.91,"score_return_alignment_label":"memory_recovery_forecast_without_order_conversion","current_profile_verdict":"current_profile_false_positive"}
{"row_type":"case","research_file":"e2r_stock_web_v12_residual_round_R13_loop_194_L10_POLICY_EVENT_CROSS_REDTEAM_MISC_R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL_research.md","case_id":"R13_HMAE_194_166090_C10_UTILIZATION_CONSUMABLES_HIGH_MAE","round":"R13","loop":"194","large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL","fine_archetype_id":"R13_HIGH_MAE_REPRESENTATIVE_COMPRESSION","source_research_file":"e2r_stock_web_v12_residual_round_R2_loop_193_L2_AI_SEMICONDUCTOR_ELECTRONICS_C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE_research.md","source_case_id":"C10_193_08_HANA_MATERIALS_JUN24_MEMORY_UTILIZATION_CONSUMABLES_HIGH_MAE","source_trigger_id":"C10_193_T08","source_large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","source_canonical_archetype_id":"C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE","source_fine_archetype_id":"MEMORY_CONSUMABLES_UTILIZATION_RECOVERY_HIGH_MAE","symbol":"166090","company_name":"Hana Materials","best_trigger":"R13_HMAE_194_T04","case_type":"representative_high_MAE_stage2_cap","positive_or_counterexample":"counterexample","score_price_alignment":"consumables_utilization_stage2_high_mae_warning","current_profile_verdict":"current_profile_correct_if_capped_at_stage2_but_not_actionable","price_source":"Songdaiki/stock-web","calibration_usable":true,"is_new_independent_case":false,"reuse_reason":"R13 representative compression of existing validated v12 trigger row; no new independent evidence weight.","independent_evidence_weight":0.0,"do_not_count_as_new_case":true,"do_not_propose_new_weight_delta":true,"notes":"Stage2 can remain as an early-cycle observation, but high-MAE guardrail blocks Actionable/Yellow/Green escalation."}
{"row_type":"trigger","research_file":"e2r_stock_web_v12_residual_round_R13_loop_194_L10_POLICY_EVENT_CROSS_REDTEAM_MISC_R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL_research.md","trigger_id":"R13_HMAE_194_T04","case_id":"R13_HMAE_194_166090_C10_UTILIZATION_CONSUMABLES_HIGH_MAE","symbol":"166090","company_name":"Hana Materials","market":"KOSDAQ","round":"R13","loop":"194","large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL","fine_archetype_id":"R13_HIGH_MAE_REPRESENTATIVE_COMPRESSION","sector":"cross_archetype_redteam_misc","primary_archetype":"R13_high_MAE_guardrail","source_research_file":"e2r_stock_web_v12_residual_round_R2_loop_193_L2_AI_SEMICONDUCTOR_ELECTRONICS_C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE_research.md","source_trigger_id":"C10_193_T08","source_large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","source_canonical_archetype_id":"C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE","source_fine_archetype_id":"MEMORY_CONSUMABLES_UTILIZATION_RECOVERY_HIGH_MAE","loop_objective":"R13 high-MAE cross-archetype holdout validation; representative compression only.","trigger_type":"Stage2","trigger_date":"2024-06-26","evidence_available_at_that_date":"Memory-utilization recovery and consumables demand language appeared, but it did not survive MAE stress.","evidence_source":"https://www.businesspost.co.kr/BP?command=article_view&num=356811","stage2_evidence_fields":["memory utilization recovery","consumables demand improvement"],"stage3_evidence_fields":[],"stage4b_evidence_fields":["extreme high-MAE after utilization narrative","supplier beta without durable order book"],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/166/166090/2024.csv; atlas/ohlcv_tradable_by_symbol_year/166/166090/2025.csv","profile_path":"atlas/symbol_profiles/166/166090.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","entry_date":"2024-06-26","entry_price":63900,"actual_1d_ohlc_row":{"o":58600,"h":66600,"l":58600,"c":63900,"v":685393},"MFE_30D_pct":8.45,"MFE_90D_pct":8.45,"MFE_180D_pct":8.45,"MFE_1Y_pct":null,"MFE_2Y_pct":null,"MAE_30D_pct":-38.73,"MAE_90D_pct":-56.65,"MAE_180D_pct":-65.81,"MAE_1Y_pct":null,"MAE_2Y_pct":null,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-07-02","peak_price":69300,"trough_date":"2025-03-25","trough_price":21850,"drawdown_after_peak_pct":-68.47,"green_lateness_ratio":"not_applicable_no_confirmed_Stage3_Green_trigger","four_b_local_peak_proximity":"not_comparable_cross_case","four_b_full_window_peak_proximity":"not_comparable_cross_case","four_b_timing_verdict":"high_mae_stage2_must_not_escalate_to_green","four_b_evidence_type":["margin_or_backlog_slowdown","positioning_overheat"],"four_c_protection_label":"thesis_break_watch_only","trigger_outcome_label":"consumables_utilization_stage2_high_mae_warning","current_profile_verdict":"current_profile_correct_if_capped_at_stage2_but_not_actionable","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL|166090|Stage2|2024-06-26","dedupe_for_aggregate":true,"aggregate_group_role":"representative_holdout_audit","is_new_independent_case":false,"reuse_reason":"R13 representative compression of prior v12 validated row; no new independent evidence weight.","independent_evidence_weight":0.0,"do_not_count_as_new_case":true,"source_proxy_only":false,"evidence_url_pending":false,"do_not_propose_new_weight_delta":true}
{"row_type":"score_simulation","research_file":"e2r_stock_web_v12_residual_round_R13_loop_194_L10_POLICY_EVENT_CROSS_REDTEAM_MISC_R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL_research.md","profile_id":"R13_high_MAE_representative_guard","case_id":"R13_HMAE_194_166090_C10_UTILIZATION_CONSUMABLES_HIGH_MAE","trigger_id":"R13_HMAE_194_T04","symbol":"166090","round":"R13","loop":"194","large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL","source_canonical_archetype_id":"C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE","raw_component_scores_before":{"contract_score":0.18,"backlog_visibility_score":0.18,"margin_bridge_score":0.38,"revision_score":0.52,"relative_strength_score":0.55,"customer_quality_score":0.25,"policy_or_regulatory_score":0.08,"valuation_repricing_score":0.45,"execution_risk_score":0.62,"legal_or_contract_risk_score":0.08,"dilution_cb_risk_score":0.05,"accounting_trust_risk_score":0.05},"weighted_score_before":66.0,"stage_label_before":"Stage2","raw_component_scores_after":{"contract_score":0.1,"backlog_visibility_score":0.1,"margin_bridge_score":0.22,"revision_score":0.36,"relative_strength_score":0.32,"customer_quality_score":0.18,"policy_or_regulatory_score":0.08,"valuation_repricing_score":0.25,"execution_risk_score":0.82,"legal_or_contract_risk_score":0.08,"dilution_cb_risk_score":0.05,"accounting_trust_risk_score":0.05},"weighted_score_after":54.0,"stage_label_after":"Stage2","component_delta_explanation":"Stage2 can remain as an early-cycle observation, but high-MAE guardrail blocks Actionable/Yellow/Green escalation.","production_scoring_changed":false,"do_not_propose_new_weight_delta":true,"MFE_90D_pct":8.45,"MAE_90D_pct":-56.65,"MFE_180D_pct":8.45,"MAE_180D_pct":-65.81,"score_return_alignment_label":"consumables_utilization_stage2_high_mae_warning","current_profile_verdict":"current_profile_correct_if_capped_at_stage2_but_not_actionable"}
{"row_type":"case","research_file":"e2r_stock_web_v12_residual_round_R13_loop_194_L10_POLICY_EVENT_CROSS_REDTEAM_MISC_R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL_research.md","case_id":"R13_HMAE_194_033100_C02_TRANSFORMER_SHORTAGE_LATE_STAGE2A","round":"R13","loop":"194","large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL","fine_archetype_id":"R13_HIGH_MAE_REPRESENTATIVE_COMPRESSION","source_research_file":"e2r_stock_web_v12_residual_round_R1_loop_193_L1_INDUSTRIALS_INFRA_DEFENSE_GRID_C02_POWER_GRID_DATACENTER_CAPEX_research.md","source_case_id":"C02_R1L193_033100_20240529_STAGE2A_HMAE","source_trigger_id":"C02_R1L193_033100_20240529_STAGE2A_HMAE","source_large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","source_canonical_archetype_id":"C02_POWER_GRID_DATACENTER_CAPEX","source_fine_archetype_id":"GRID_DATACENTER_DISTRIBUTION_TRANSFORMER_EXPORT_HIGH_MAE","symbol":"033100","company_name":"JeRyong Electric","best_trigger":"R13_HMAE_194_T05","case_type":"representative_high_MAE_late_stage2_actionable","positive_or_counterexample":"counterexample","score_price_alignment":"strong_evidence_but_late_high_mae_guardrail","current_profile_verdict":"current_profile_false_positive_if_stage2_actionable_is_not_capped_by_entry_quality","price_source":"Songdaiki/stock-web","calibration_usable":true,"is_new_independent_case":false,"reuse_reason":"R13 representative compression of existing validated v12 trigger row; no new independent evidence weight.","independent_evidence_weight":0.0,"do_not_count_as_new_case":true,"do_not_propose_new_weight_delta":true,"notes":"Real backlog/shortage evidence remains valuable, but high-MAE late-entry condition caps it below Yellow/Green."}
{"row_type":"trigger","research_file":"e2r_stock_web_v12_residual_round_R13_loop_194_L10_POLICY_EVENT_CROSS_REDTEAM_MISC_R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL_research.md","trigger_id":"R13_HMAE_194_T05","case_id":"R13_HMAE_194_033100_C02_TRANSFORMER_SHORTAGE_LATE_STAGE2A","symbol":"033100","company_name":"JeRyong Electric","market":"KOSDAQ","round":"R13","loop":"194","large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL","fine_archetype_id":"R13_HIGH_MAE_REPRESENTATIVE_COMPRESSION","sector":"cross_archetype_redteam_misc","primary_archetype":"R13_high_MAE_guardrail","source_research_file":"e2r_stock_web_v12_residual_round_R1_loop_193_L1_INDUSTRIALS_INFRA_DEFENSE_GRID_C02_POWER_GRID_DATACENTER_CAPEX_research.md","source_trigger_id":"C02_R1L193_033100_20240529_STAGE2A_HMAE","source_large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","source_canonical_archetype_id":"C02_POWER_GRID_DATACENTER_CAPEX","source_fine_archetype_id":"GRID_DATACENTER_DISTRIBUTION_TRANSFORMER_EXPORT_HIGH_MAE","loop_objective":"R13 high-MAE cross-archetype holdout validation; representative compression only.","trigger_type":"Stage2-Actionable","trigger_date":"2024-05-29","evidence_available_at_that_date":"Q1 growth, export share, US transformer shortage, and order backlog were real, but the entry was late and extremely drawdown-prone.","evidence_source":"https://www.thebigdata.co.kr/view.php?ud=202405290538457085cd1e7f0bdf_23","stage2_evidence_fields":["Q1 sales/OP growth","US transformer shortage","order backlog"],"stage3_evidence_fields":[],"stage4b_evidence_fields":["late extension","valuation/peak proximity","90D MAE over -40%"],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/033/033100/2024.csv; atlas/ohlcv_tradable_by_symbol_year/033/033100/2025.csv","profile_path":"atlas/symbol_profiles/033/033100.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","entry_date":"2024-05-29","entry_price":73900,"actual_1d_ohlc_row":{"o":78100,"h":78900,"l":72500,"c":73900,"v":1114957},"MFE_30D_pct":35.05,"MFE_90D_pct":36.27,"MFE_180D_pct":36.27,"MFE_1Y_pct":null,"MFE_2Y_pct":null,"MAE_30D_pct":-17.73,"MAE_90D_pct":-41.54,"MAE_180D_pct":-50.54,"MAE_1Y_pct":null,"MAE_2Y_pct":null,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-07-11","peak_price":100700,"trough_date":"2024-12-09","trough_price":36550,"drawdown_after_peak_pct":-63.7,"green_lateness_ratio":"not_applicable_no_confirmed_Stage3_Green_trigger","four_b_local_peak_proximity":"not_comparable_cross_case","four_b_full_window_peak_proximity":"not_comparable_cross_case","four_b_timing_verdict":"late_entry_guard_needed_before_green","four_b_evidence_type":["valuation_blowoff","positioning_overheat"],"four_c_protection_label":"thesis_break_watch_only","trigger_outcome_label":"strong_evidence_but_late_high_mae_guardrail","current_profile_verdict":"current_profile_false_positive_if_stage2_actionable_is_not_capped_by_entry_quality","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL|033100|Stage2-Actionable|2024-05-29","dedupe_for_aggregate":true,"aggregate_group_role":"representative_holdout_audit","is_new_independent_case":false,"reuse_reason":"R13 representative compression of prior v12 validated row; no new independent evidence weight.","independent_evidence_weight":0.0,"do_not_count_as_new_case":true,"source_proxy_only":false,"evidence_url_pending":false,"do_not_propose_new_weight_delta":true}
{"row_type":"score_simulation","research_file":"e2r_stock_web_v12_residual_round_R13_loop_194_L10_POLICY_EVENT_CROSS_REDTEAM_MISC_R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL_research.md","profile_id":"R13_high_MAE_representative_guard","case_id":"R13_HMAE_194_033100_C02_TRANSFORMER_SHORTAGE_LATE_STAGE2A","trigger_id":"R13_HMAE_194_T05","symbol":"033100","round":"R13","loop":"194","large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL","source_canonical_archetype_id":"C02_POWER_GRID_DATACENTER_CAPEX","raw_component_scores_before":{"contract_score":0.62,"backlog_visibility_score":0.72,"margin_bridge_score":0.6,"revision_score":0.68,"relative_strength_score":0.74,"customer_quality_score":0.52,"policy_or_regulatory_score":0.3,"valuation_repricing_score":0.78,"execution_risk_score":0.6,"legal_or_contract_risk_score":0.1,"dilution_cb_risk_score":0.05,"accounting_trust_risk_score":0.05},"weighted_score_before":72.0,"stage_label_before":"Stage2-Actionable","raw_component_scores_after":{"contract_score":0.58,"backlog_visibility_score":0.68,"margin_bridge_score":0.48,"revision_score":0.56,"relative_strength_score":0.46,"customer_quality_score":0.48,"policy_or_regulatory_score":0.3,"valuation_repricing_score":0.35,"execution_risk_score":0.82,"legal_or_contract_risk_score":0.1,"dilution_cb_risk_score":0.05,"accounting_trust_risk_score":0.05},"weighted_score_after":63.0,"stage_label_after":"Stage2","component_delta_explanation":"Real backlog/shortage evidence remains valuable, but high-MAE late-entry condition caps it below Yellow/Green.","production_scoring_changed":false,"do_not_propose_new_weight_delta":true,"MFE_90D_pct":36.27,"MAE_90D_pct":-41.54,"MFE_180D_pct":36.27,"MAE_180D_pct":-50.54,"score_return_alignment_label":"strong_evidence_but_late_high_mae_guardrail","current_profile_verdict":"current_profile_false_positive_if_stage2_actionable_is_not_capped_by_entry_quality"}
{"row_type":"case","research_file":"e2r_stock_web_v12_residual_round_R13_loop_194_L10_POLICY_EVENT_CROSS_REDTEAM_MISC_R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL_research.md","case_id":"R13_HMAE_194_003670_C13_HIGH_MFE_HIGH_DRAWDOWN_WINNER","round":"R13","loop":"194","large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL","fine_archetype_id":"R13_HIGH_MAE_REPRESENTATIVE_COMPRESSION","source_research_file":"e2r_stock_web_v12_residual_round_R3_loop_190_L3_BATTERY_EV_GREEN_MOBILITY_C13_BATTERY_JV_UTILIZATION_AMPC_IRA_research.md","source_case_id":"C13_R3L190_003670_POSCO_GM_ULTIUM_CAM_EXPANSION","source_trigger_id":"R3L190_C13_003670_20230602_STAGE2_ACTIONABLE","source_large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","source_canonical_archetype_id":"C13_BATTERY_JV_UTILIZATION_AMPC_IRA","source_fine_archetype_id":"GM_POSCO_ULTIUM_CAM_JV_CAPACITY_BRIDGE","symbol":"003670","company_name":"POSCO Future M","best_trigger":"R13_HMAE_194_T06","case_type":"representative_high_MFE_high_MAE_positive_control","positive_or_counterexample":"positive_control","score_price_alignment":"true_winner_requires_timeboxed_profit_taking_not_initial_block","current_profile_verdict":"current_profile_missed_structural_if_capacity_JV_not_mapped_but_green_block_correct","price_source":"Songdaiki/stock-web","calibration_usable":true,"is_new_independent_case":false,"reuse_reason":"R13 representative compression of existing validated v12 trigger row; no new independent evidence weight.","independent_evidence_weight":0.0,"do_not_count_as_new_case":true,"do_not_propose_new_weight_delta":true,"notes":"R13 high-MAE guardrail must not block all volatile winners; direct customer/JV capacity bridge preserves Stage2-Actionable while preventing Green."}
{"row_type":"trigger","research_file":"e2r_stock_web_v12_residual_round_R13_loop_194_L10_POLICY_EVENT_CROSS_REDTEAM_MISC_R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL_research.md","trigger_id":"R13_HMAE_194_T06","case_id":"R13_HMAE_194_003670_C13_HIGH_MFE_HIGH_DRAWDOWN_WINNER","symbol":"003670","company_name":"POSCO Future M","market":"KOSPI","round":"R13","loop":"194","large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL","fine_archetype_id":"R13_HIGH_MAE_REPRESENTATIVE_COMPRESSION","sector":"cross_archetype_redteam_misc","primary_archetype":"R13_high_MAE_guardrail","source_research_file":"e2r_stock_web_v12_residual_round_R3_loop_190_L3_BATTERY_EV_GREEN_MOBILITY_C13_BATTERY_JV_UTILIZATION_AMPC_IRA_research.md","source_trigger_id":"R3L190_C13_003670_20230602_STAGE2_ACTIONABLE","source_large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","source_canonical_archetype_id":"C13_BATTERY_JV_UTILIZATION_AMPC_IRA","source_fine_archetype_id":"GM_POSCO_ULTIUM_CAM_JV_CAPACITY_BRIDGE","loop_objective":"R13 high-MAE cross-archetype holdout validation; representative compression only.","trigger_type":"Stage2-Actionable","trigger_date":"2023-06-02","evidence_available_at_that_date":"GM/POSCO Future M North America CAM/precursor expansion provided a real structural capacity bridge, although the later drawdown was severe.","evidence_source":"https://www.poscofuturem.com/en/pr/view.do?num=695 ; https://news.gm.com/home.detail.html/Pages/news/us/en/2023/jun/0602-posco.html","stage2_evidence_fields":["direct customer JV","North America CAM/precursor capacity","long supply chain bridge"],"stage3_evidence_fields":["structural customer-quality evidence but near-term utilization/ex-AMPC profit not yet proven"],"stage4b_evidence_fields":["post-peak drawdown over -60%","high-multiple battery-material exposure"],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/003/003670/2023.csv","profile_path":"atlas/symbol_profiles/003/003670.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","entry_date":"2023-06-02","entry_price":374000,"actual_1d_ohlc_row":{"o":361500,"h":381500,"l":358500,"c":374000,"v":1467089},"MFE_30D_pct":12.3,"MFE_90D_pct":85.56,"MFE_180D_pct":85.56,"MFE_1Y_pct":null,"MFE_2Y_pct":null,"MAE_30D_pct":-7.89,"MAE_90D_pct":-16.18,"MAE_180D_pct":-38.1,"MAE_1Y_pct":null,"MAE_2Y_pct":null,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2023-07-26","peak_price":694000,"trough_date":"2024-02-26","trough_price":231500,"drawdown_after_peak_pct":-66.64,"green_lateness_ratio":"not_applicable_no_confirmed_Stage3_Green_trigger","four_b_local_peak_proximity":"not_comparable_cross_case","four_b_full_window_peak_proximity":"not_comparable_cross_case","four_b_timing_verdict":"needs_local_4B_after_peak_not_initial_stage2_block","four_b_evidence_type":["positioning_overheat","valuation_blowoff"],"four_c_protection_label":"false_break_if_initial_trigger_blocked","trigger_outcome_label":"true_winner_requires_timeboxed_profit_taking_not_initial_block","current_profile_verdict":"current_profile_missed_structural_if_capacity_JV_not_mapped_but_green_block_correct","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL|003670|Stage2-Actionable|2023-06-02","dedupe_for_aggregate":true,"aggregate_group_role":"representative_holdout_audit","is_new_independent_case":false,"reuse_reason":"R13 representative compression of prior v12 validated row; no new independent evidence weight.","independent_evidence_weight":0.0,"do_not_count_as_new_case":true,"source_proxy_only":false,"evidence_url_pending":false,"do_not_propose_new_weight_delta":true}
{"row_type":"score_simulation","research_file":"e2r_stock_web_v12_residual_round_R13_loop_194_L10_POLICY_EVENT_CROSS_REDTEAM_MISC_R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL_research.md","profile_id":"R13_high_MAE_representative_guard","case_id":"R13_HMAE_194_003670_C13_HIGH_MFE_HIGH_DRAWDOWN_WINNER","trigger_id":"R13_HMAE_194_T06","symbol":"003670","round":"R13","loop":"194","large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL","source_canonical_archetype_id":"C13_BATTERY_JV_UTILIZATION_AMPC_IRA","raw_component_scores_before":{"contract_score":0.82,"backlog_visibility_score":0.66,"margin_bridge_score":0.34,"revision_score":0.44,"relative_strength_score":0.76,"customer_quality_score":0.9,"policy_or_regulatory_score":0.76,"valuation_repricing_score":0.72,"execution_risk_score":0.48,"legal_or_contract_risk_score":0.12,"dilution_cb_risk_score":0.08,"accounting_trust_risk_score":0.05},"weighted_score_before":70.0,"stage_label_before":"Stage2-Actionable","raw_component_scores_after":{"contract_score":0.86,"backlog_visibility_score":0.7,"margin_bridge_score":0.32,"revision_score":0.42,"relative_strength_score":0.62,"customer_quality_score":0.9,"policy_or_regulatory_score":0.76,"valuation_repricing_score":0.46,"execution_risk_score":0.62,"legal_or_contract_risk_score":0.12,"dilution_cb_risk_score":0.08,"accounting_trust_risk_score":0.05},"weighted_score_after":72.0,"stage_label_after":"Stage2-Actionable","component_delta_explanation":"R13 high-MAE guardrail must not block all volatile winners; direct customer/JV capacity bridge preserves Stage2-Actionable while preventing Green.","production_scoring_changed":false,"do_not_propose_new_weight_delta":true,"MFE_90D_pct":85.56,"MAE_90D_pct":-16.18,"MFE_180D_pct":85.56,"MAE_180D_pct":-38.1,"score_return_alignment_label":"true_winner_requires_timeboxed_profit_taking_not_initial_block","current_profile_verdict":"current_profile_missed_structural_if_capacity_JV_not_mapped_but_green_block_correct"}
{"row_type":"case","research_file":"e2r_stock_web_v12_residual_round_R13_loop_194_L10_POLICY_EVENT_CROSS_REDTEAM_MISC_R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL_research.md","case_id":"R13_HMAE_194_006400_C14_HARD_4C_SUCCESS_HIGH_MAE","round":"R13","loop":"194","large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL","fine_archetype_id":"R13_HIGH_MAE_REPRESENTATIVE_COMPRESSION","source_research_file":"e2r_stock_web_v12_residual_round_R3_loop_192_L3_BATTERY_EV_GREEN_MOBILITY_C14_EV_DEMAND_SLOWDOWN_4B_4C_research.md","source_case_id":"C14_006400_20241030_Q3_HARD_4C_SUCCESS","source_trigger_id":"C14_006400_20241030_STAGE4C_EV_SLOWDOWN_BATTERY_UNIT_COLLAPSE","source_large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","source_canonical_archetype_id":"C14_EV_DEMAND_SLOWDOWN_4B_4C","source_fine_archetype_id":"EV_DEMAND_SLOWDOWN_BATTERY_UNIT_EARNINGS_COLLAPSE_HARD_4C","symbol":"006400","company_name":"Samsung SDI","best_trigger":"R13_HMAE_194_T07","case_type":"representative_hard_4c_success_control","positive_or_counterexample":"positive_4c_control","score_price_alignment":"hard_4c_success_high_mae_protected","current_profile_verdict":"current_profile_correct","price_source":"Songdaiki/stock-web","calibration_usable":true,"is_new_independent_case":false,"reuse_reason":"R13 representative compression of existing validated v12 trigger row; no new independent evidence weight.","independent_evidence_weight":0.0,"do_not_count_as_new_case":true,"do_not_propose_new_weight_delta":true,"notes":"This is the control case showing that high-MAE guardrail should preserve true hard 4C when non-price thesis break is confirmed."}
{"row_type":"trigger","research_file":"e2r_stock_web_v12_residual_round_R13_loop_194_L10_POLICY_EVENT_CROSS_REDTEAM_MISC_R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL_research.md","trigger_id":"R13_HMAE_194_T07","case_id":"R13_HMAE_194_006400_C14_HARD_4C_SUCCESS_HIGH_MAE","symbol":"006400","company_name":"Samsung SDI","market":"KOSPI","round":"R13","loop":"194","large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL","fine_archetype_id":"R13_HIGH_MAE_REPRESENTATIVE_COMPRESSION","sector":"cross_archetype_redteam_misc","primary_archetype":"R13_high_MAE_guardrail","source_research_file":"e2r_stock_web_v12_residual_round_R3_loop_192_L3_BATTERY_EV_GREEN_MOBILITY_C14_EV_DEMAND_SLOWDOWN_4B_4C_research.md","source_trigger_id":"C14_006400_20241030_STAGE4C_EV_SLOWDOWN_BATTERY_UNIT_COLLAPSE","source_large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","source_canonical_archetype_id":"C14_EV_DEMAND_SLOWDOWN_4B_4C","source_fine_archetype_id":"EV_DEMAND_SLOWDOWN_BATTERY_UNIT_EARNINGS_COLLAPSE_HARD_4C","loop_objective":"R13 high-MAE cross-archetype holdout validation; representative compression only.","trigger_type":"Stage4C","trigger_date":"2024-10-30","evidence_available_at_that_date":"Q3 2024 release showed sharp battery earnings deterioration, European EV slowdown, and lower cylindrical utilization.","evidence_source":"https://www.samsungsdi.com/sdi-now/sdi-news/4082.html","stage2_evidence_fields":[],"stage3_evidence_fields":[],"stage4b_evidence_fields":["EV slowdown","utilization decline","profit collapse"],"stage4c_evidence_fields":["battery-business profit collapse","no near-term recovery bridge","demand slowdown with utilization damage"],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/006/006400/2024.csv; atlas/ohlcv_tradable_by_symbol_year/006/006400/2025.csv","profile_path":"atlas/symbol_profiles/006/006400.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","entry_date":"2024-10-31","entry_price":327000,"actual_1d_ohlc_row":{"o":334500,"h":341000,"l":327000,"c":327000,"v":378994},"MFE_30D_pct":4.28,"MFE_90D_pct":4.28,"MFE_180D_pct":4.28,"MFE_1Y_pct":null,"MFE_2Y_pct":null,"MAE_30D_pct":-27.98,"MAE_90D_pct":-42.87,"MAE_180D_pct":-51.77,"MAE_1Y_pct":null,"MAE_2Y_pct":null,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-10-31","peak_price":341000,"trough_date":"2025-04-10","trough_price":157700,"drawdown_after_peak_pct":-53.75,"green_lateness_ratio":"not_applicable_no_confirmed_Stage3_Green_trigger","four_b_local_peak_proximity":"not_comparable_cross_case","four_b_full_window_peak_proximity":"not_comparable_cross_case","four_b_timing_verdict":"hard_4c_good_timing_after_non_price_thesis_break","four_b_evidence_type":["revision_slowdown","margin_or_backlog_slowdown"],"four_c_protection_label":"hard_4c_success","trigger_outcome_label":"hard_4c_success_high_mae_protected","current_profile_verdict":"current_profile_correct","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL|006400|Stage4C|2024-10-31","dedupe_for_aggregate":true,"aggregate_group_role":"representative_holdout_audit","is_new_independent_case":false,"reuse_reason":"R13 representative compression of prior v12 validated row; no new independent evidence weight.","independent_evidence_weight":0.0,"do_not_count_as_new_case":true,"source_proxy_only":false,"evidence_url_pending":false,"do_not_propose_new_weight_delta":true}
{"row_type":"score_simulation","research_file":"e2r_stock_web_v12_residual_round_R13_loop_194_L10_POLICY_EVENT_CROSS_REDTEAM_MISC_R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL_research.md","profile_id":"R13_high_MAE_representative_guard","case_id":"R13_HMAE_194_006400_C14_HARD_4C_SUCCESS_HIGH_MAE","trigger_id":"R13_HMAE_194_T07","symbol":"006400","round":"R13","loop":"194","large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL","source_canonical_archetype_id":"C14_EV_DEMAND_SLOWDOWN_4B_4C","raw_component_scores_before":{"contract_score":0.15,"backlog_visibility_score":0.1,"margin_bridge_score":0.06,"revision_score":0.08,"relative_strength_score":0.2,"customer_quality_score":0.35,"policy_or_regulatory_score":0.3,"valuation_repricing_score":0.22,"execution_risk_score":0.9,"legal_or_contract_risk_score":0.15,"dilution_cb_risk_score":0.1,"accounting_trust_risk_score":0.08},"weighted_score_before":34.0,"stage_label_before":"Stage4C","raw_component_scores_after":{"contract_score":0.12,"backlog_visibility_score":0.08,"margin_bridge_score":0.03,"revision_score":0.05,"relative_strength_score":0.18,"customer_quality_score":0.32,"policy_or_regulatory_score":0.25,"valuation_repricing_score":0.18,"execution_risk_score":0.96,"legal_or_contract_risk_score":0.15,"dilution_cb_risk_score":0.1,"accounting_trust_risk_score":0.08},"weighted_score_after":31.0,"stage_label_after":"Stage4C","component_delta_explanation":"This is the control case showing that high-MAE guardrail should preserve true hard 4C when non-price thesis break is confirmed.","production_scoring_changed":false,"do_not_propose_new_weight_delta":true,"MFE_90D_pct":4.28,"MAE_90D_pct":-42.87,"MFE_180D_pct":4.28,"MAE_180D_pct":-51.77,"score_return_alignment_label":"hard_4c_success_high_mae_protected","current_profile_verdict":"current_profile_correct"}
{"row_type":"case","research_file":"e2r_stock_web_v12_residual_round_R13_loop_194_L10_POLICY_EVENT_CROSS_REDTEAM_MISC_R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL_research.md","case_id":"R13_HMAE_194_010120_C02_LS_ELECTRIC_EXTENSION_4B","round":"R13","loop":"194","large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL","fine_archetype_id":"R13_HIGH_MAE_REPRESENTATIVE_COMPRESSION","source_research_file":"e2r_stock_web_v12_residual_round_R1_loop_193_L1_INDUSTRIALS_INFRA_DEFENSE_GRID_C02_POWER_GRID_DATACENTER_CAPEX_research.md","source_case_id":"C02_R1L193_010120_20240725_4B","source_trigger_id":"C02_R1L193_010120_20240725_4B","source_large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","source_canonical_archetype_id":"C02_POWER_GRID_DATACENTER_CAPEX","source_fine_archetype_id":"GRID_DATACENTER_ELECTRIC_BUSINESS_PRICE_EXTENSION_4B","symbol":"010120","company_name":"LS ELECTRIC","best_trigger":"R13_HMAE_194_T08","case_type":"representative_high_MAE_4B_not_hard_4c","positive_or_counterexample":"positive_4B_control","score_price_alignment":"local_4b_watch_preserves_later_upside_but_blocks_green","current_profile_verdict":"current_profile_correct_if_local_4B_not_hard_4C","price_source":"Songdaiki/stock-web","calibration_usable":true,"is_new_independent_case":false,"reuse_reason":"R13 representative compression of existing validated v12 trigger row; no new independent evidence weight.","independent_evidence_weight":0.0,"do_not_count_as_new_case":true,"do_not_propose_new_weight_delta":true,"notes":"High MAE and extension should trigger local 4B watch, not hard 4C, because subsequent 180D MFE still reached 40.84%."}
{"row_type":"trigger","research_file":"e2r_stock_web_v12_residual_round_R13_loop_194_L10_POLICY_EVENT_CROSS_REDTEAM_MISC_R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL_research.md","trigger_id":"R13_HMAE_194_T08","case_id":"R13_HMAE_194_010120_C02_LS_ELECTRIC_EXTENSION_4B","symbol":"010120","company_name":"LS ELECTRIC","market":"KOSPI","round":"R13","loop":"194","large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL","fine_archetype_id":"R13_HIGH_MAE_REPRESENTATIVE_COMPRESSION","sector":"cross_archetype_redteam_misc","primary_archetype":"R13_high_MAE_guardrail","source_research_file":"e2r_stock_web_v12_residual_round_R1_loop_193_L1_INDUSTRIALS_INFRA_DEFENSE_GRID_C02_POWER_GRID_DATACENTER_CAPEX_research.md","source_trigger_id":"C02_R1L193_010120_20240725_4B","source_large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","source_canonical_archetype_id":"C02_POWER_GRID_DATACENTER_CAPEX","source_fine_archetype_id":"GRID_DATACENTER_ELECTRIC_BUSINESS_PRICE_EXTENSION_4B","loop_objective":"R13 high-MAE cross-archetype holdout validation; representative compression only.","trigger_type":"Stage4B","trigger_date":"2024-07-25","evidence_available_at_that_date":"2Q24 official deck showed record profitability driven by the US electric business, while price extension and high MAE required 4B watch instead of Green.","evidence_source":"https://www.ls-electric.com/ko/company/data/24_2Q_Results.pdf","stage2_evidence_fields":["US electric business growth","SWGR/HVTR strength"],"stage3_evidence_fields":["official profit bridge but extension was already crowded"],"stage4b_evidence_fields":["price extension","90D MAE over -40%","later peak still possible"],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/010/010120/2024.csv; atlas/ohlcv_tradable_by_symbol_year/010/010120/2025.csv; atlas/ohlcv_tradable_by_symbol_year/010/010120/2026.csv","profile_path":"atlas/symbol_profiles/010/010120.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","entry_date":"2024-07-25","entry_price":215500,"actual_1d_ohlc_row":{"o":249500,"h":257000,"l":214500,"c":215500,"v":2303383},"MFE_30D_pct":19.26,"MFE_90D_pct":19.26,"MFE_180D_pct":40.84,"MFE_1Y_pct":null,"MFE_2Y_pct":null,"MAE_30D_pct":-38.33,"MAE_90D_pct":-41.44,"MAE_180D_pct":-41.44,"MAE_1Y_pct":null,"MAE_2Y_pct":null,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2025-02-19","peak_price":303500,"trough_date":"2024-09-09","trough_price":126200,"drawdown_after_peak_pct":-58.42,"green_lateness_ratio":"not_applicable_no_confirmed_Stage3_Green_trigger","four_b_local_peak_proximity":"not_comparable_cross_case","four_b_full_window_peak_proximity":"not_comparable_cross_case","four_b_timing_verdict":"good_local_4b_but_not_full_window_4c","four_b_evidence_type":["positioning_overheat","valuation_blowoff"],"four_c_protection_label":"false_break_if_routed_to_hard_4c","trigger_outcome_label":"local_4b_watch_preserves_later_upside_but_blocks_green","current_profile_verdict":"current_profile_correct_if_local_4B_not_hard_4C","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL|010120|Stage4B|2024-07-25","dedupe_for_aggregate":true,"aggregate_group_role":"representative_holdout_audit","is_new_independent_case":false,"reuse_reason":"R13 representative compression of prior v12 validated row; no new independent evidence weight.","independent_evidence_weight":0.0,"do_not_count_as_new_case":true,"source_proxy_only":false,"evidence_url_pending":false,"do_not_propose_new_weight_delta":true}
{"row_type":"score_simulation","research_file":"e2r_stock_web_v12_residual_round_R13_loop_194_L10_POLICY_EVENT_CROSS_REDTEAM_MISC_R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL_research.md","profile_id":"R13_high_MAE_representative_guard","case_id":"R13_HMAE_194_010120_C02_LS_ELECTRIC_EXTENSION_4B","trigger_id":"R13_HMAE_194_T08","symbol":"010120","round":"R13","loop":"194","large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL","source_canonical_archetype_id":"C02_POWER_GRID_DATACENTER_CAPEX","raw_component_scores_before":{"contract_score":0.68,"backlog_visibility_score":0.74,"margin_bridge_score":0.72,"revision_score":0.7,"relative_strength_score":0.78,"customer_quality_score":0.62,"policy_or_regulatory_score":0.3,"valuation_repricing_score":0.82,"execution_risk_score":0.58,"legal_or_contract_risk_score":0.1,"dilution_cb_risk_score":0.05,"accounting_trust_risk_score":0.05},"weighted_score_before":67.0,"stage_label_before":"Stage2-Actionable","raw_component_scores_after":{"contract_score":0.66,"backlog_visibility_score":0.72,"margin_bridge_score":0.66,"revision_score":0.62,"relative_strength_score":0.48,"customer_quality_score":0.6,"policy_or_regulatory_score":0.3,"valuation_repricing_score":0.36,"execution_risk_score":0.78,"legal_or_contract_risk_score":0.1,"dilution_cb_risk_score":0.05,"accounting_trust_risk_score":0.05},"weighted_score_after":57.0,"stage_label_after":"Stage4B","component_delta_explanation":"High MAE and extension should trigger local 4B watch, not hard 4C, because subsequent 180D MFE still reached 40.84%.","production_scoring_changed":false,"do_not_propose_new_weight_delta":true,"MFE_90D_pct":19.26,"MAE_90D_pct":-41.44,"MFE_180D_pct":40.84,"MAE_180D_pct":-41.44,"score_return_alignment_label":"local_4b_watch_preserves_later_upside_but_blocks_green","current_profile_verdict":"current_profile_correct_if_local_4B_not_hard_4C"}
{"profile_id":"P0_e2r_2_1_stock_web_calibrated_proxy","profile_scope":"current_proxy","profile_hypothesis":"Current calibrated profile receives high-MAE rows as already-calibrated evidence.","changed_axes":"none","changed_thresholds":"none","eligible_trigger_count":8,"selected_entry_trigger_per_case":8,"avg_MFE_90D_pct":20.84,"avg_MAE_90D_pct":-38.56,"avg_MFE_180D_pct":23.53,"avg_MAE_180D_pct":-46.98,"false_positive_rate":0.625,"missed_structural_count":1,"late_green_count":0,"avg_green_lateness_ratio":"not_applicable","avg_four_b_local_peak_proximity":"not_comparable_cross_case","avg_four_b_full_window_peak_proximity":"not_comparable_cross_case","score_return_alignment_verdict":"residual_high_MAE_false_positive_risk_remains","row_type":"profile_comparison","research_file":"e2r_stock_web_v12_residual_round_R13_loop_194_L10_POLICY_EVENT_CROSS_REDTEAM_MISC_R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL_research.md","round":"R13","loop":"194","large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL","production_scoring_changed":false,"do_not_propose_new_weight_delta":true}
{"profile_id":"P0b_e2r_2_0_baseline_reference","profile_scope":"rollback_reference","profile_hypothesis":"Old baseline would over-credit generic cyclicality and price beta.","changed_axes":"rollback_reference_only","changed_thresholds":"pre_stock_web_calibration","eligible_trigger_count":8,"selected_entry_trigger_per_case":8,"avg_MFE_90D_pct":20.84,"avg_MAE_90D_pct":-38.56,"avg_MFE_180D_pct":23.53,"avg_MAE_180D_pct":-46.98,"false_positive_rate":0.75,"missed_structural_count":1,"late_green_count":0,"avg_green_lateness_ratio":"not_applicable","avg_four_b_local_peak_proximity":"not_comparable_cross_case","avg_four_b_full_window_peak_proximity":"not_comparable_cross_case","score_return_alignment_verdict":"worse_than_current_proxy","row_type":"profile_comparison","research_file":"e2r_stock_web_v12_residual_round_R13_loop_194_L10_POLICY_EVENT_CROSS_REDTEAM_MISC_R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL_research.md","round":"R13","loop":"194","large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL","production_scoring_changed":false,"do_not_propose_new_weight_delta":true}
{"profile_id":"P1_R13_high_MAE_stage_escalation_brake","profile_scope":"global_candidate_audit_only","profile_hypothesis":"High MAE acts as an escalation brake only when direct non-price bridge is missing.","changed_axes":"no_weight_delta; audit tag only","changed_thresholds":"do_not_escalate_to_Actionable_or_Green_when_high_MAE_late_entry_and_bridge_missing","eligible_trigger_count":8,"selected_entry_trigger_per_case":8,"avg_MFE_90D_pct":20.84,"avg_MAE_90D_pct":-38.56,"avg_MFE_180D_pct":23.53,"avg_MAE_180D_pct":-46.98,"false_positive_rate":0.25,"missed_structural_count":0,"late_green_count":0,"avg_green_lateness_ratio":"not_applicable","avg_four_b_local_peak_proximity":"not_comparable_cross_case","avg_four_b_full_window_peak_proximity":"not_comparable_cross_case","score_return_alignment_verdict":"best_holdout_alignment_without_weight_delta","row_type":"profile_comparison","research_file":"e2r_stock_web_v12_residual_round_R13_loop_194_L10_POLICY_EVENT_CROSS_REDTEAM_MISC_R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL_research.md","round":"R13","loop":"194","large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL","production_scoring_changed":false,"do_not_propose_new_weight_delta":true}
{"profile_id":"P2_source_canonical_specific_existing_guards","profile_scope":"canonical_existing_axis_stress_test","profile_hypothesis":"Existing canonical gates from C02/C10/C13/C14/C15 handle most cases if R13 compresses representatives correctly.","changed_axes":"stage2_required_bridge|local_4b_watch_guard|hard_4c_confirmation","changed_thresholds":"none_new","eligible_trigger_count":8,"selected_entry_trigger_per_case":8,"avg_MFE_90D_pct":20.84,"avg_MAE_90D_pct":-38.56,"avg_MFE_180D_pct":23.53,"avg_MAE_180D_pct":-46.98,"false_positive_rate":0.375,"missed_structural_count":0,"late_green_count":0,"avg_green_lateness_ratio":"not_applicable","avg_four_b_local_peak_proximity":"not_comparable_cross_case","avg_four_b_full_window_peak_proximity":"not_comparable_cross_case","score_return_alignment_verdict":"acceptable_if_representative_compression_is_used","row_type":"profile_comparison","research_file":"e2r_stock_web_v12_residual_round_R13_loop_194_L10_POLICY_EVENT_CROSS_REDTEAM_MISC_R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL_research.md","round":"R13","loop":"194","large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL","production_scoring_changed":false,"do_not_propose_new_weight_delta":true}
{"profile_id":"P3_counterexample_guard_profile","profile_scope":"guard_profile","profile_hypothesis":"Block positive promotion from high-MAE rows unless there is direct customer/order/margin bridge.","changed_axes":"data_quality_guard_only","changed_thresholds":"promotion_eligible=false when do_not_count_as_new_case=true","eligible_trigger_count":8,"selected_entry_trigger_per_case":8,"avg_MFE_90D_pct":20.84,"avg_MAE_90D_pct":-38.56,"avg_MFE_180D_pct":23.53,"avg_MAE_180D_pct":-46.98,"false_positive_rate":0.125,"missed_structural_count":1,"late_green_count":0,"avg_green_lateness_ratio":"not_applicable","avg_four_b_local_peak_proximity":"not_comparable_cross_case","avg_four_b_full_window_peak_proximity":"not_comparable_cross_case","score_return_alignment_verdict":"safe_but_may_under_credit_structural_winners","row_type":"profile_comparison","research_file":"e2r_stock_web_v12_residual_round_R13_loop_194_L10_POLICY_EVENT_CROSS_REDTEAM_MISC_R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL_research.md","round":"R13","loop":"194","large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL","production_scoring_changed":false,"do_not_propose_new_weight_delta":true}
{"row_type":"aggregate","research_file":"e2r_stock_web_v12_residual_round_R13_loop_194_L10_POLICY_EVENT_CROSS_REDTEAM_MISC_R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL_research.md","round":"R13","loop":"194","large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL","fine_archetype_id":"R13_HIGH_MAE_REPRESENTATIVE_COMPRESSION","eligible_trigger_count":8,"reused_representative_trigger_count":8,"new_independent_trigger_count":0,"unique_source_symbol_count":8,"unique_source_large_sector_count":4,"unique_source_canonical_count":5,"avg_MFE_90D_pct":20.84,"avg_MAE_90D_pct":-38.56,"avg_MFE_180D_pct":23.53,"avg_MAE_180D_pct":-46.98,"high_MAE90_row_count":7,"high_MAE180_row_count":7,"MFE180_below_20_row_count":5,"current_profile_error_count":6,"production_scoring_changed":false,"shadow_weight_only":true,"do_not_propose_new_weight_delta":true,"ready_for_batch_ingest":true}
{"row_type":"shadow_weight","research_file":"e2r_stock_web_v12_residual_round_R13_loop_194_L10_POLICY_EVENT_CROSS_REDTEAM_MISC_R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL_research.md","axis":"R13_HIGH_MAE_REPRESENTATIVE_COMPRESSION","scope":"global_candidate_audit_only","large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL","old_weight":0,"new_weight":0,"delta":0,"evidence_summary":"Representative compression of high-MAE rows across source canonicals; no new independent evidence weight.","expected_effect":"Prevents duplicate/reused high-MAE rows from inflating future promotion decisions while preserving true Stage4C and true structural controls.","representative_trigger_ids":["R13_HMAE_194_T01","R13_HMAE_194_T02","R13_HMAE_194_T03","R13_HMAE_194_T04","R13_HMAE_194_T05","R13_HMAE_194_T06","R13_HMAE_194_T07","R13_HMAE_194_T08"],"usable_trigger_count":8,"positive_count":3,"counterexample_count":5,"confidence":"medium","application_status":"holdout_audit_only","production_scoring_changed":false,"do_not_propose_new_weight_delta":true}
{"row_type":"residual_contribution","research_file":"e2r_stock_web_v12_residual_round_R13_loop_194_L10_POLICY_EVENT_CROSS_REDTEAM_MISC_R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL_research.md","round":"R13","loop":"194","large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL","fine_archetype_id":"R13_HIGH_MAE_REPRESENTATIVE_COMPRESSION","loop_contribution_label":"holdout_validation_passed","residual_error_type":"high_MAE_false_positive_and_4B_4C_boundary_stress_test","existing_axis_strengthened":["stage2_required_bridge","stage3_green_not_loosened","local_4b_watch_guard","hard_4c_confirmation"],"existing_axis_weakened":[],"new_axis_proposed":false,"sector_specific_rule_candidate":null,"canonical_archetype_rule_candidate":"R13_HIGH_MAE_GREEN_AND_ACTIONABLE_CAP","production_scoring_changed":false,"shadow_weight_only":true,"do_not_propose_new_weight_delta":true,"summary":"High MAE should be an escalation brake and representative compression guard, not a direct bearish rule and not a new weight delta."}
{"row_type":"narrative_only","research_file":"e2r_stock_web_v12_residual_round_R13_loop_194_L10_POLICY_EVENT_CROSS_REDTEAM_MISC_R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL_research.md","topic":"R13 interpretation","text":"The file intentionally reuses prior validated price-path rows. It should not be counted as fresh evidence but can be used to test parser handling of do_not_count_as_new_case=true and representative_holdout_audit rows."}
```

## 18. Batch Ingest Self-Audit

| audit_item | value |
|---|---|
| `filename_matches_required_regex` | `true` |
| `filename_round_equals_metadata_round` | `true` |
| `filename_loop_equals_metadata_loop` | `true` |
| `round_sector_consistency_pass` | `true` |
| `R13_large_sector_is_L10` | `true` |
| `trigger_type_canonical_stage_label_only` | `true` |
| `all_trigger_rows_have_MFE_30_90_180_and_MAE_30_90_180` | `true` |
| `all_trigger_rows_have_price_source_fields` | `true` |
| `all_trigger_rows_have_profile_path` | `true` |
| `all_trigger_rows_have_price_shard_path` | `true` |
| `all_trigger_rows_calibration_usable` | `true` |
| `corporate_action_contaminated_180D_count` | `0` |
| `insufficient_forward_window_180D_count` | `0` |
| `source_proxy_only_count` | `0` |
| `evidence_url_pending_count` | `0` |
| `new_independent_case_count` | `0` |
| `reused_representative_case_count` | `8` |
| `aggregate_inclusion_for_new_weight` | `false` |
| `ready_for_batch_ingest` | `true` |

## 19. Deferred Coding Agent Handoff Prompt

```text
You are a coding agent working later, not during this research run.
Read this MD as an R13 representative high-MAE holdout audit.
Do not apply any numeric weight delta from this MD.
Validate that all trigger rows with do_not_count_as_new_case=true are excluded from new aggregate evidence counts, but remain available for R13 holdout/profile stress-test reports.
Check parser handling of trigger_type canonical labels Stage2, Stage2-Actionable, Stage4B, Stage4C.
Confirm that reused representative rows do not create hard duplicate keys in promotion inputs.
If implementation changes are needed later, add only data-quality / aggregate-filter handling for R13 representative compression. Do not loosen Stage3-Green thresholds.
```

## 20. Next Research State

```text
completed_round = R13
completed_loop = 194
selection_basis = docs/core/V12_Research_No_Repeat_Index.md
selected_priority_bucket = Priority 2 R13 high-MAE representative compression / quality repair
round_schedule_status = coverage_index_selected
round_sector_consistency = pass
production_scoring_changed = false
shadow_weight_only = true
do_not_propose_new_weight_delta = true
next_recommended_archetypes = [
  R13_CROSS_ARCHETYPE_4B_4C_REDTEAM,
  R13_CROSS_ARCHETYPE_STAGE2_FALSE_POSITIVE_REVIEW,
  C02_POWER_GRID_DATACENTER_CAPEX_4B_4C_DIRECT_BREAK_REPAIR,
  C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE_4C_DIRECT_THESIS_BREAK_REPAIR,
  C05_EPC_MEGA_CONTRACT_MARGIN_GAP
]
```

## 21. Final Research Conclusion

This R13 run validates a narrow guardrail: **high MAE should slow stage escalation and prevent duplicate promotion evidence, but it should not become a universal bearish rule.** The POSCO Future M and LS ELECTRIC controls show why hard blocking would be too blunt; the Dongkuk/Poongsan/Wonik/Hana/JeRyong rows show why generic cycle evidence must be capped; the Samsung SDI hard-4C row shows why confirmed non-price thesis break still needs protection.
