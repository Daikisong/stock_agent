# stock-web v12 residual calibration — R1 loop 145 / C02_POWER_GRID_DATACENTER_CAPEX

## Metadata

```yaml
expected_v12_result_file: true
filename: e2r_stock_web_v12_residual_round_R1_loop_145_L1_INDUSTRIALS_INFRA_DEFENSE_GRID_C02_POWER_GRID_DATACENTER_CAPEX_research.md
selected_round: R1
selected_loop: 145
selection_basis: docs/core/V12_Research_No_Repeat_Index.md
selected_priority_bucket: Priority 0/1 quality repair after recent C05/C01/C13/C15/C10 runs — C02 direct URL repair, 4B-heavy/4C-empty balance, theme-blowoff counterexamples
round_schedule_status: coverage_index_selected
round_sector_consistency: pass
large_sector_id: L1_INDUSTRIALS_INFRA_DEFENSE_GRID
canonical_archetype_id: C02_POWER_GRID_DATACENTER_CAPEX
fine_archetype_id: POWER_GRID_DATACENTER_CAPEX_ORDER_MARGIN_BRIDGE_VS_THEME_BLOWOFF
loop_objective: C02 power-grid/datacenter CAPEX order-margin bridge validation; URL/proxy repair; high-MAE and price-only 4B guardrail mining; positive/counterexample balance
price_source: Songdaiki/stock-web
price_basis: tradable_raw
price_adjustment_status: raw_unadjusted_marcap
stock_web_manifest_max_date: 2026-02-20
production_scoring_changed: false
shadow_weight_only: true
new_independent_case_count: 7
reused_case_count: 0
same_archetype_new_symbol_count: 6
same_archetype_new_trigger_family_count: 7
calibration_usable_case_count: 7
calibration_usable_trigger_count: 7
positive_case_count: 5
counterexample_count: 2
current_profile_error_count: 4
stage4b_or_4c_case_count: 2
source_proxy_only_count: 1
evidence_url_pending_count: 0
rows_missing_required_mfe_mae: 0
new_axis_proposed: C02_GRID_DATACENTER_ORDER_MARGIN_BRIDGE_GATE
existing_axis_strengthened: [stage2_required_bridge, local_4b_watch_guard, full_4b_requires_non_price_evidence, earlier_thesis_break_watch]
existing_axis_weakened: null
next_recommended_archetypes: [C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH, C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF, C14_EV_DEMAND_SLOWDOWN_4B_4C, C16_STRATEGIC_RESOURCE_POLICY_SUPPLY]
```

## Selection note

이번 실행은 직전 로컬 산출물 C05 → C01 → C13 → C15 → C10을 피했다. No-Repeat 장부상 C02는 이미 representative row가 충분하지만, 4B 비중이 높고 hard 4C row가 비어 있으며 URL/proxy 품질 보강 대상이 큰 축에 남아 있다. 따라서 단순 row 증설이 아니라 **직접 URL repair + price-only theme blowoff 분리 + order/backlog/margin bridge gate**를 목표로 삼았다. R1 root에서 확인되는 기존 C02 표준 파일의 최대 loop는 144이므로 이번 파일은 C02 loop 145로 둔다.

## Price atlas validation

| field | value |
|---|---|
| price_data_repo | Songdaiki/stock-web |
| calibration_shard_root | atlas/ohlcv_tradable_by_symbol_year |
| price_basis | tradable_raw |
| price_adjustment_status | raw_unadjusted_marcap |
| stock_web_manifest_max_date | 2026-02-20 |
| entry rule used | evidence timing unclear or after-market unknown → next stock-web tradable close |
| forward window | all trigger rows have >=180 trading days after entry in downloaded stock-web shards |
| raw shard use | not used for weight calibration; only tradable shard used for prices |
| corporate action note | profile checks were attempted; where profile content was unavailable in this environment, downloaded tradable windows were validated for positive OHLC and sufficient forward rows. Rows are marked clean for 180D only, not for 2Y. |

### Local stock-web shards used

| symbol | shard years | price_shard_path examples | profile_path |
|---|---:|---|---|
| 267260 | 2025 | `atlas/ohlcv_tradable_by_symbol_year/267/267260/2025.csv` | `atlas/symbol_profiles/267/267260.json` |
| 010120 | 2025 | `atlas/ohlcv_tradable_by_symbol_year/010/010120/2025.csv` | `atlas/symbol_profiles/010/010120.json` |
| 298040 | 2025,2026 | `atlas/ohlcv_tradable_by_symbol_year/298/298040/2025.csv, atlas/ohlcv_tradable_by_symbol_year/298/298040/2026.csv` | `atlas/symbol_profiles/298/298040.json` |
| 001440 | 2024,2025 | `atlas/ohlcv_tradable_by_symbol_year/001/001440/2024.csv, atlas/ohlcv_tradable_by_symbol_year/001/001440/2025.csv` | `atlas/symbol_profiles/001/001440.json` |
| 033100 | 2024,2025,2026 | `atlas/ohlcv_tradable_by_symbol_year/033/033100/2024.csv, atlas/ohlcv_tradable_by_symbol_year/033/033100/2025.csv, atlas/ohlcv_tradable_by_symbol_year/033/033100/2026.csv` | `atlas/symbol_profiles/033/033100.json` |
| 006340 | 2024,2025 | `atlas/ohlcv_tradable_by_symbol_year/006/006340/2024.csv, atlas/ohlcv_tradable_by_symbol_year/006/006340/2025.csv` | `atlas/symbol_profiles/006/006340.json` |

## Evidence matrix

| case | symbol | evidence family | direct/proxy | source | evidence summary as of trigger |
|---|---:|---|---|---|---|
| C02_R1L145_267260_20250120_HDHE_4Q24_MARGIN_ORDER_BRIDGE | 267260 | direct_ir_margin_order_bridge | direct_or_direct_plus_supplement | https://www.hd-hyundaielectric.com/elect/en/IR/IRdata1.jsp | 4Q 2024 earning-release IR item dated 2025-01-20; company product map includes power transformer, GIS, switchgear, distribution transformer. |
| C02_R1L145_010120_20250120_LSELECTRIC_4Q24_US_HVTR_BACKLOG | 010120 | direct_ir_us_hvtr_backlog_growth | direct_or_direct_plus_supplement | https://www.ls-electric.com/ko/company/data/24_4Q_Results.pdf | 4Q 2024 earning release: Electric business U.S. HVTR/SWGR growth, U.S. customer expansion, order backlog FY23 2.3T -> FY24 3.4T. |
| C02_R1L145_298040_20250519_HYOSUNG_EU_UHV_AI_SUPPLIER | 298040 | direct_contract_ai_grid_supplier_expansion | direct_or_direct_plus_supplement | https://www.hyosung.com/en/newsroom/view/18994 | Company news: KRW85bn ultra-high-voltage transformer supply contract with Scottish Power; first Germany supply contract; explicit AI power-equipment supplier ambition. |
| C02_R1L145_001440_20240919_TAIHAN_FIRST_US_HVDC | 001440 | direct_us_hvdc_hvac_order_accumulation | direct_or_direct_plus_supplement | https://www.taihan.com/en/news/pr/taihanNews | Company news: first U.S. HVDC project worth about KRW90bn; 320kV HVDC and 500kV HVAC grids for Silicon Valley/San Jose; U.S. year-to-date orders about KRW610bn. |
| C02_R1L145_033100_20240318_JERYONG_US_DISTRIBUTION_TRANSFORMER_BACKLOG | 033100 | official_business_mapping_plus_us_shortage_backlog_bridge | direct_or_direct_plus_supplement | https://kind.krx.co.kr/common/disclsviewer.do?acptno=20240318000363&docno=&method=search&viewerhost= ; supplemental=https://www.myasset.com/myasset/research/rs_list/rs_view.cmd?SEQ=193547&cd006=&cd007=RE01&cd008= | Official annual report identifies transformer/switchgear/GIS business; supplemental broker evidence says distribution transformer exposure, export ratio jump, U.S. shortage and backlog expansion. |
| C02_R1L145_001440_20240725_TAIHAN_SINGLE_CONTRACT_TOO_EARLY | 001440 | single_contract_headline_without_current_margin_bridge | direct_or_direct_plus_supplement | https://www.taihan.com/en/news/pr/taihanNews | Company news: KRW190bn long-term U.S. contract for EHV grid components; cumulative U.S. orders about KRW520bn at that point, but price path showed high-MAE before later stronger confirmation. |
| C02_R1L145_006340_20240626_DAEWON_PRICE_ONLY_US_TRANSFORMER_EXPECTATION | 006340 | price_only_theme_expectation_no_direct_order_bridge | proxy_only | https://securities.miraeasset.com/bbs/download/2129191.pdf?attachmentId=2129191 ; supplemental=https://securities.miraeasset.com/bbs/download/2125425.pdf?attachmentId=2125425 | Proxy/news-flow: stock surged on U.S. transformer-order expectation and AI/data-center power narrative; no direct order/backlog bridge at trigger. |

## Trigger path table — stock-web actual 1D OHLC

| case_id | symbol | trigger_type | trigger_date | entry_date | entry_price | MFE_30D_pct | MAE_30D_pct | MFE_90D_pct | MAE_90D_pct | MFE_180D_pct | MAE_180D_pct | peak_date | peak_price | drawdown_after_peak_pct | case_polarity | current_profile_verdict |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| C02_R1L145_267260_20250120_HDHE_4Q24_MARGIN_ORDER_BRIDGE | 267260 | Stage3-Yellow | 2025-01-20 | 2025-01-21 | 385000 | 16.8831 | -18.3117 | 16.8831 | -31.2987 | 81.039 | -31.2987 | 2025-10-21 | 697000 | -3.4433 | positive | current_profile_too_early_for_green_but_correct_for_yellow |
| C02_R1L145_010120_20250120_LSELECTRIC_4Q24_US_HVTR_BACKLOG | 010120 | Stage3-Yellow | 2025-01-20 | 2025-01-21 | 207000 | 46.6184 | -4.2029 | 46.6184 | -29.0821 | 61.3527 | -29.0821 | 2025-08-05 | 334000 | -24.2515 | positive | current_profile_too_early_for_green_but_correct_for_actionable_yellow |
| C02_R1L145_298040_20250519_HYOSUNG_EU_UHV_AI_SUPPLIER | 298040 | Stage3-Green | 2025-05-19 | 2025-05-20 | 582000 | 62.543 | -3.0928 | 157.3883 | -3.0928 | 358.9347 | -3.0928 | 2026-01-30 | 2671000 | -21.3403 | positive | current_profile_correct_for_green_but_requires_later_4b_overlay |
| C02_R1L145_001440_20240919_TAIHAN_FIRST_US_HVDC | 001440 | Stage2-Actionable | 2024-09-19 | 2024-09-20 | 11700 | 17.7778 | -3.4188 | 23.4188 | -14.5299 | 50.3419 | -14.5299 | 2025-06-23 | 17590 | -8.5844 | positive | current_profile_correct_for_stage2_actionable_not_green |
| C02_R1L145_033100_20240318_JERYONG_US_DISTRIBUTION_TRANSFORMER_BACKLOG | 033100 | Stage3-Green | 2024-03-18 | 2024-03-19 | 32550 | 108.6022 | -0.9217 | 209.3702 | -0.9217 | 209.3702 | -0.9217 | 2024-07-11 | 100700 | -63.7041 | positive | current_profile_correct_for_green_then_later_4b_overlay_needed |
| C02_R1L145_001440_20240725_TAIHAN_SINGLE_CONTRACT_TOO_EARLY | 001440 | Stage4B | 2024-07-25 | 2024-07-26 | 13620 | 6.5345 | -24.5962 | 6.5345 | -26.5786 | 6.5345 | -26.5786 | 2024-08-01 | 14510 | -31.082 | counterexample | current_profile_too_early_or_false_positive_if_actionable_without_margin_bridge |
| C02_R1L145_006340_20240626_DAEWON_PRICE_ONLY_US_TRANSFORMER_EXPECTATION | 006340 | Stage4B | 2024-06-26 | 2024-06-27 | 4350 | 9.7701 | -39.3103 | 9.7701 | -41.3793 | 9.7701 | -49.3103 | 2024-06-28 | 4775 | -53.822 | counterexample | current_profile_false_positive_if_price_only_theme_given_actionable_bonus |

## Score simulation — current calibrated profile proxy stress test

Weights used only as research proxy for C02 based on No-Repeat coverage matrix snapshot: eps_fcf=21, earnings_visibility=24, bottleneck/pricing=20, market_mispricing=13, valuation=12, capital_allocation=5, information_confidence=5. This does not patch production scoring.

| symbol | case_id | eps_fcf_explosion | earnings_visibility | bottleneck_pricing | market_mispricing | valuation_rerating | capital_allocation | information_confidence | weighted_proxy_total | proxy_stage_read | actual_path_verdict |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 267260 | C02_R1L145_267260_20250120_HDHE_4Q24_MARGIN_ORDER_BRIDGE | 68 | 80 | 83 | 55 | 48 | 45 | 80 | 69.24 | Stage2-Actionable-proxy | current_profile_too_early_for_green_but_correct_for_yellow |
| 010120 | C02_R1L145_010120_20250120_LSELECTRIC_4Q24_US_HVTR_BACKLOG | 72 | 82 | 80 | 55 | 50 | 55 | 82 | 70.8 | Stage2-Actionable-proxy | current_profile_too_early_for_green_but_correct_for_actionable_yellow |
| 298040 | C02_R1L145_298040_20250519_HYOSUNG_EU_UHV_AI_SUPPLIER | 86 | 88 | 90 | 62 | 60 | 58 | 85 | 79.59 | Stage3-Yellow-proxy | current_profile_correct_for_green_but_requires_later_4b_overlay |
| 001440 | C02_R1L145_001440_20240919_TAIHAN_FIRST_US_HVDC | 65 | 72 | 78 | 52 | 45 | 45 | 82 | 65.04 | Stage2-Actionable-proxy | current_profile_correct_for_stage2_actionable_not_green |
| 033100 | C02_R1L145_033100_20240318_JERYONG_US_DISTRIBUTION_TRANSFORMER_BACKLOG | 88 | 84 | 92 | 60 | 50 | 40 | 70 | 76.34 | Stage3-Yellow-proxy | current_profile_correct_for_green_then_later_4b_overlay_needed |
| 001440 | C02_R1L145_001440_20240725_TAIHAN_SINGLE_CONTRACT_TOO_EARLY | 50 | 60 | 70 | 45 | 40 | 40 | 75 | 55.3 | Stage2-watch-proxy | current_profile_too_early_or_false_positive_if_actionable_without_margin_bridge |
| 006340 | C02_R1L145_006340_20240626_DAEWON_PRICE_ONLY_US_TRANSFORMER_EXPECTATION | 38 | 35 | 45 | 30 | 25 | 30 | 45 | 36.03 | Stage0/1-or-4B-cap-proxy | current_profile_false_positive_if_price_only_theme_given_actionable_bonus |

### Current profile stress-test answers

1. C02의 calibrated profile은 direct transformer/GIS/HVTR/HVDC evidence가 있으면 Stage2-Actionable 또는 Yellow까지 빠르게 열 수 있다. 이번 positive rows에서는 방향은 맞았다.

2. 그러나 HD Hyundai Electric과 LS ELECTRIC처럼 180D right-tail이 맞더라도 90D MAE가 -29%~-31%까지 깊어질 수 있다. Green unlock은 “증거가 맞다”가 아니라 “경로가 견딜 수 있다”까지 요구해야 한다.

3. Stage2 actionable bonus는 direct order/backlog/margin bridge가 있는 cases에는 부족하지 않다. 다만 Taihan 2024-07-25와 Daewon 2024-06-26처럼 단일 계약 headline 또는 price-only theme에 같은 bonus를 주면 과하다.

4. Yellow threshold 75는 C02에서 적절하지만, single-contract headline row는 margin/revenue conversion proof 없이는 Yellow에 못 올라가게 gate가 필요하다.

5. Green threshold 87/revision 55는 Hyosung 2025-05-19, Jeryong 2024-03-18 같은 direct bottleneck + visible conversion + low initial MAE에는 적절하다. 다만 Jeryong은 이후 parabolic drawdown이 커서 별도 4B overlay가 필요하다.

6. Price-only blowoff guard는 Daewon row에서 반드시 유지해야 한다. 가격만 소리를 질러도 order book이 침묵하면 그 신호는 Stage2 evidence가 아니라 4B risk evidence다.

7. Full 4B non-price requirement는 유지한다. C02에서 4B는 valuation/positioning 과열뿐 아니라 margin bridge absence, source_proxy_only, contract-to-revenue lag가 붙을 때 더 잘 작동한다.

8. Hard 4C routing은 이번 sample에서 직접 thesis break가 확인되지 않아 새 hard-4C delta를 제안하지 않는다. 대신 C02의 4C-empty issue는 향후 order cancellation, delivery delay, customer deferral, transformer margin collapse cases로 따로 채워야 한다.

## Machine-readable JSONL trigger rows

```jsonl
{"row_type":"trigger","trigger_id":"R1L145_C02_T01_267260_20250120","case_id":"C02_R1L145_267260_20250120_HDHE_4Q24_MARGIN_ORDER_BRIDGE","symbol":"267260","company_name":"HD HYUNDAI ELECTRIC","round":"R1","loop":145,"large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C02_POWER_GRID_DATACENTER_CAPEX","fine_archetype_id":"POWER_GRID_DATACENTER_CAPEX_ORDER_MARGIN_BRIDGE_VS_THEME_BLOWOFF","sector":"Electrical equipment / power transformer / GIS","primary_archetype":"power_grid_datacenter_capex","loop_objective":"C02 direct URL/proxy repair and order-margin bridge vs theme-blowoff calibration","trigger_type":"Stage3-Yellow","trigger_date":"2025-01-20","evidence_available_at_that_date":"4Q 2024 earning-release IR item dated 2025-01-20; company product map includes power transformer, GIS, switchgear, distribution transformer.","evidence_source":"https://www.hd-hyundaielectric.com/elect/en/IR/IRdata1.jsp","source_type":"company_ir","source_proxy_only":false,"stage2_evidence_fields":["public company IR event","direct grid-equipment product mapping","transformer/GIS/switchgear exposure","order-demand narrative with current earnings release"],"stage3_evidence_fields":["earnings-release confirmation","margin/order bridge likely visible","multiple non-price evidence fields"],"stage4b_evidence_fields":["early 2025 valuation/positioning overheat risk","post-entry 90D MAE exceeded -30% despite later right-tail"],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/267/267260/2025.csv","profile_path":"atlas/symbol_profiles/267/267260.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","entry_date":"2025-01-21","entry_price":385000.0,"MFE_30D_pct":16.8831,"MFE_90D_pct":16.8831,"MFE_180D_pct":81.039,"MFE_1Y_pct":153.5065,"MFE_2Y_pct":null,"MAE_30D_pct":-18.3117,"MAE_90D_pct":-31.2987,"MAE_180D_pct":-31.2987,"MAE_1Y_pct":-31.2987,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2025-10-21","peak_price":697000.0,"drawdown_after_peak_pct":-3.4433,"green_lateness_ratio":null,"four_b_local_peak_proximity":"low","four_b_full_window_peak_proximity":"watch","four_b_timing_verdict":"not_primary","four_b_evidence_type":"valuation_positioning_watch","four_c_protection_label":"not_triggered_no_hard_thesis_break","trigger_outcome_label":"direct_grid_equipment_earnings_order_bridge_high_mae_success","current_profile_verdict":"current_profile_too_early_for_green_but_correct_for_yellow","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_downloaded_tradable_window; 1Y/2Y may be unavailable_or_unchecked","same_entry_group_id":"267260_2025-01-21_C02_POWER_GRID_DATACENTER_CAPEX_direct_ir_margin_order_bridge","dedupe_for_aggregate":"keep_representative","aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false,"case_role":"high_mae_success","case_polarity":"positive","component_scores":{"eps_fcf_explosion":68,"earnings_visibility":80,"bottleneck_pricing":83,"market_mispricing":55,"valuation_rerating":48,"capital_allocation":45,"information_confidence":80},"weighted_proxy_total":69.24}
{"row_type":"trigger","trigger_id":"R1L145_C02_T02_010120_20250120","case_id":"C02_R1L145_010120_20250120_LSELECTRIC_4Q24_US_HVTR_BACKLOG","symbol":"010120","company_name":"LS ELECTRIC","round":"R1","loop":145,"large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C02_POWER_GRID_DATACENTER_CAPEX","fine_archetype_id":"POWER_GRID_DATACENTER_CAPEX_ORDER_MARGIN_BRIDGE_VS_THEME_BLOWOFF","sector":"Electrical equipment / high-voltage transformer / switchgear","primary_archetype":"power_grid_datacenter_capex","loop_objective":"C02 direct URL/proxy repair and order-margin bridge vs theme-blowoff calibration","trigger_type":"Stage3-Yellow","trigger_date":"2025-01-20","evidence_available_at_that_date":"4Q 2024 earning release: Electric business U.S. HVTR/SWGR growth, U.S. customer expansion, order backlog FY23 2.3T -> FY24 3.4T.","evidence_source":"https://www.ls-electric.com/ko/company/data/24_4Q_Results.pdf","source_type":"company_ir_pdf","source_proxy_only":false,"stage2_evidence_fields":["company IR event","U.S. HVTR/SWGR demand","order backlog expansion","customer expansion"],"stage3_evidence_fields":["consolidated performance acceleration","electric-segment OP growth","order backlog conversion evidence"],"stage4b_evidence_fields":["post-peak 90D drawdown after first surge","crowded AI-grid positioning risk"],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/010/010120/2025.csv","profile_path":"atlas/symbol_profiles/010/010120.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","entry_date":"2025-01-21","entry_price":207000.0,"MFE_30D_pct":46.6184,"MFE_90D_pct":46.6184,"MFE_180D_pct":61.3527,"MFE_1Y_pct":217.8744,"MFE_2Y_pct":null,"MAE_30D_pct":-4.2029,"MAE_90D_pct":-29.0821,"MAE_180D_pct":-29.0821,"MAE_1Y_pct":-29.0821,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2025-08-05","peak_price":334000.0,"drawdown_after_peak_pct":-24.2515,"green_lateness_ratio":null,"four_b_local_peak_proximity":"medium","four_b_full_window_peak_proximity":"watch","four_b_timing_verdict":"not_primary","four_b_evidence_type":"valuation_positioning_watch","four_c_protection_label":"not_triggered_no_hard_thesis_break","trigger_outcome_label":"us_hvtr_swgr_backlog_growth_yellow_with_high_mae","current_profile_verdict":"current_profile_too_early_for_green_but_correct_for_actionable_yellow","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_downloaded_tradable_window; 1Y/2Y may be unavailable_or_unchecked","same_entry_group_id":"010120_2025-01-21_C02_POWER_GRID_DATACENTER_CAPEX_direct_ir_us_hvtr_backlog_growth","dedupe_for_aggregate":"keep_representative","aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false,"case_role":"high_mae_success","case_polarity":"positive","component_scores":{"eps_fcf_explosion":72,"earnings_visibility":82,"bottleneck_pricing":80,"market_mispricing":55,"valuation_rerating":50,"capital_allocation":55,"information_confidence":82},"weighted_proxy_total":70.8}
{"row_type":"trigger","trigger_id":"R1L145_C02_T03_298040_20250519","case_id":"C02_R1L145_298040_20250519_HYOSUNG_EU_UHV_AI_SUPPLIER","symbol":"298040","company_name":"HYOSUNG HEAVY INDUSTRIES","round":"R1","loop":145,"large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C02_POWER_GRID_DATACENTER_CAPEX","fine_archetype_id":"POWER_GRID_DATACENTER_CAPEX_ORDER_MARGIN_BRIDGE_VS_THEME_BLOWOFF","sector":"Electrical equipment / ultra-high-voltage transformer","primary_archetype":"power_grid_datacenter_capex","loop_objective":"C02 direct URL/proxy repair and order-margin bridge vs theme-blowoff calibration","trigger_type":"Stage3-Green","trigger_date":"2025-05-19","evidence_available_at_that_date":"Company news: KRW85bn ultra-high-voltage transformer supply contract with Scottish Power; first Germany supply contract; explicit AI power-equipment supplier ambition.","evidence_source":"https://www.hyosung.com/en/newsroom/view/18994","source_type":"company_news","source_proxy_only":false,"stage2_evidence_fields":["direct contract win","ultra-high-voltage transformer product","named utility customer","AI/grid demand route"],"stage3_evidence_fields":["multi-region expansion","visible contract value","strategic supplier positioning","low initial MAE"],"stage4b_evidence_fields":["later parabolic rise requires local 4B overlay after right-tail"],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/298/298040/2025.csv","profile_path":"atlas/symbol_profiles/298/298040.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","entry_date":"2025-05-20","entry_price":582000.0,"MFE_30D_pct":62.543,"MFE_90D_pct":157.3883,"MFE_180D_pct":358.9347,"MFE_1Y_pct":null,"MFE_2Y_pct":null,"MAE_30D_pct":-3.0928,"MAE_90D_pct":-3.0928,"MAE_180D_pct":-3.0928,"MAE_1Y_pct":null,"below_entry_price_flag_30D":false,"below_entry_price_flag_90D":false,"peak_date":"2026-01-30","peak_price":2671000.0,"drawdown_after_peak_pct":-21.3403,"green_lateness_ratio":null,"four_b_local_peak_proximity":"medium","four_b_full_window_peak_proximity":"watch","four_b_timing_verdict":"not_primary","four_b_evidence_type":"valuation_positioning_watch","four_c_protection_label":"not_triggered_no_hard_thesis_break","trigger_outcome_label":"europe_uhv_transformer_contract_green_structural_success","current_profile_verdict":"current_profile_correct_for_green_but_requires_later_4b_overlay","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_downloaded_tradable_window; 1Y/2Y may be unavailable_or_unchecked","same_entry_group_id":"298040_2025-05-20_C02_POWER_GRID_DATACENTER_CAPEX_direct_contract_ai_grid_supplier_expansion","dedupe_for_aggregate":"keep_representative","aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false,"case_role":"structural_success","case_polarity":"positive","component_scores":{"eps_fcf_explosion":86,"earnings_visibility":88,"bottleneck_pricing":90,"market_mispricing":62,"valuation_rerating":60,"capital_allocation":58,"information_confidence":85},"weighted_proxy_total":79.59}
{"row_type":"trigger","trigger_id":"R1L145_C02_T04_001440_20240919","case_id":"C02_R1L145_001440_20240919_TAIHAN_FIRST_US_HVDC","symbol":"001440","company_name":"Taihan Cable & Solution","round":"R1","loop":145,"large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C02_POWER_GRID_DATACENTER_CAPEX","fine_archetype_id":"POWER_GRID_DATACENTER_CAPEX_ORDER_MARGIN_BRIDGE_VS_THEME_BLOWOFF","sector":"Cable / HVDC / HVAC grid equipment","primary_archetype":"power_grid_datacenter_capex","loop_objective":"C02 direct URL/proxy repair and order-margin bridge vs theme-blowoff calibration","trigger_type":"Stage2-Actionable","trigger_date":"2024-09-19","evidence_available_at_that_date":"Company news: first U.S. HVDC project worth about KRW90bn; 320kV HVDC and 500kV HVAC grids for Silicon Valley/San Jose; U.S. year-to-date orders about KRW610bn.","evidence_source":"https://www.taihan.com/en/news/pr/taihanNews","source_type":"company_news","source_proxy_only":false,"stage2_evidence_fields":["direct company contract news","HVDC/HVAC technology mapping","named U.S. grid geography","cumulative U.S. order evidence"],"stage3_evidence_fields":["later FY2024 financial result supports order-to-revenue bridge","expanded global order intake"],"stage4b_evidence_fields":["contract headline already partially priced; 90D MAE double-digit"],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/001/001440/2024.csv","profile_path":"atlas/symbol_profiles/001/001440.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","entry_date":"2024-09-20","entry_price":11700.0,"MFE_30D_pct":17.7778,"MFE_90D_pct":23.4188,"MFE_180D_pct":50.3419,"MFE_1Y_pct":55.2991,"MFE_2Y_pct":null,"MAE_30D_pct":-3.4188,"MAE_90D_pct":-14.5299,"MAE_180D_pct":-14.5299,"MAE_1Y_pct":-14.5299,"below_entry_price_flag_30D":false,"below_entry_price_flag_90D":true,"peak_date":"2025-06-23","peak_price":17590.0,"drawdown_after_peak_pct":-8.5844,"green_lateness_ratio":null,"four_b_local_peak_proximity":"low","four_b_full_window_peak_proximity":"watch","four_b_timing_verdict":"not_primary","four_b_evidence_type":"valuation_positioning_watch","four_c_protection_label":"not_triggered_no_hard_thesis_break","trigger_outcome_label":"us_hvdc_hvac_order_accumulation_actionable_positive","current_profile_verdict":"current_profile_correct_for_stage2_actionable_not_green","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_downloaded_tradable_window; 1Y/2Y may be unavailable_or_unchecked","same_entry_group_id":"001440_2024-09-20_C02_POWER_GRID_DATACENTER_CAPEX_direct_us_hvdc_hvac_order_accumulation","dedupe_for_aggregate":"keep_representative","aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false,"case_role":"stage2_promote_candidate","case_polarity":"positive","component_scores":{"eps_fcf_explosion":65,"earnings_visibility":72,"bottleneck_pricing":78,"market_mispricing":52,"valuation_rerating":45,"capital_allocation":45,"information_confidence":82},"weighted_proxy_total":65.04}
{"row_type":"trigger","trigger_id":"R1L145_C02_T05_033100_20240318","case_id":"C02_R1L145_033100_20240318_JERYONG_US_DISTRIBUTION_TRANSFORMER_BACKLOG","symbol":"033100","company_name":"Jeryong Electric","round":"R1","loop":145,"large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C02_POWER_GRID_DATACENTER_CAPEX","fine_archetype_id":"POWER_GRID_DATACENTER_CAPEX_ORDER_MARGIN_BRIDGE_VS_THEME_BLOWOFF","sector":"Distribution transformer","primary_archetype":"power_grid_datacenter_capex","loop_objective":"C02 direct URL/proxy repair and order-margin bridge vs theme-blowoff calibration","trigger_type":"Stage3-Green","trigger_date":"2024-03-18","evidence_available_at_that_date":"Official annual report identifies transformer/switchgear/GIS business; supplemental broker evidence says distribution transformer exposure, export ratio jump, U.S. shortage and backlog expansion.","evidence_source":"https://kind.krx.co.kr/common/disclsviewer.do?acptno=20240318000363&docno=&method=search&viewerhost= ; supplemental=https://www.myasset.com/myasset/research/rs_list/rs_view.cmd?SEQ=193547&cd006=&cd007=RE01&cd008=","source_type":"official_disclosure_plus_broker_supplement","source_proxy_only":false,"stage2_evidence_fields":["official disclosure business mapping","transformer exposure","U.S. shortage/order backlog supplemental evidence","export mix acceleration"],"stage3_evidence_fields":["large revenue/OP growth proxy","backlog visibility","niche bottleneck/pricing power"],"stage4b_evidence_fields":["parabolic right-tail later required 4B overlay even though initial Green was valid"],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/033/033100/2024.csv","profile_path":"atlas/symbol_profiles/033/033100.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","entry_date":"2024-03-19","entry_price":32550.0,"MFE_30D_pct":108.6022,"MFE_90D_pct":209.3702,"MFE_180D_pct":209.3702,"MFE_1Y_pct":209.3702,"MFE_2Y_pct":null,"MAE_30D_pct":-0.9217,"MAE_90D_pct":-0.9217,"MAE_180D_pct":-0.9217,"MAE_1Y_pct":-9.063,"below_entry_price_flag_30D":false,"below_entry_price_flag_90D":false,"peak_date":"2024-07-11","peak_price":100700.0,"drawdown_after_peak_pct":-63.7041,"green_lateness_ratio":null,"four_b_local_peak_proximity":"high","four_b_full_window_peak_proximity":"watch","four_b_timing_verdict":"needed_after_right_tail","four_b_evidence_type":"valuation_positioning_watch","four_c_protection_label":"not_triggered_no_hard_thesis_break","trigger_outcome_label":"distribution_transformer_export_backlog_green_right_tail","current_profile_verdict":"current_profile_correct_for_green_then_later_4b_overlay_needed","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_downloaded_tradable_window; 1Y/2Y may be unavailable_or_unchecked","same_entry_group_id":"033100_2024-03-19_C02_POWER_GRID_DATACENTER_CAPEX_official_business_mapping_plus_us_shortage_backlog_bridge","dedupe_for_aggregate":"keep_representative","aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false,"case_role":"structural_success","case_polarity":"positive","component_scores":{"eps_fcf_explosion":88,"earnings_visibility":84,"bottleneck_pricing":92,"market_mispricing":60,"valuation_rerating":50,"capital_allocation":40,"information_confidence":70},"weighted_proxy_total":76.34}
{"row_type":"trigger","trigger_id":"R1L145_C02_T06_001440_20240725","case_id":"C02_R1L145_001440_20240725_TAIHAN_SINGLE_CONTRACT_TOO_EARLY","symbol":"001440","company_name":"Taihan Cable & Solution","round":"R1","loop":145,"large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C02_POWER_GRID_DATACENTER_CAPEX","fine_archetype_id":"POWER_GRID_DATACENTER_CAPEX_ORDER_MARGIN_BRIDGE_VS_THEME_BLOWOFF","sector":"Cable / EHV grid components","primary_archetype":"power_grid_datacenter_capex","loop_objective":"C02 direct URL/proxy repair and order-margin bridge vs theme-blowoff calibration","trigger_type":"Stage4B","trigger_date":"2024-07-25","evidence_available_at_that_date":"Company news: KRW190bn long-term U.S. contract for EHV grid components; cumulative U.S. orders about KRW520bn at that point, but price path showed high-MAE before later stronger confirmation.","evidence_source":"https://www.taihan.com/en/news/pr/taihanNews","source_type":"company_news","source_proxy_only":false,"stage2_evidence_fields":["direct contract headline","U.S. EHV grid component route"],"stage3_evidence_fields":[],"stage4b_evidence_fields":["headline already crowded","no immediate margin/revenue bridge at trigger","subsequent 90D/180D MAE below -26%"],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/001/001440/2024.csv","profile_path":"atlas/symbol_profiles/001/001440.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","entry_date":"2024-07-26","entry_price":13620.0,"MFE_30D_pct":6.5345,"MFE_90D_pct":6.5345,"MFE_180D_pct":6.5345,"MFE_1Y_pct":33.4068,"MFE_2Y_pct":null,"MAE_30D_pct":-24.5962,"MAE_90D_pct":-26.5786,"MAE_180D_pct":-26.5786,"MAE_1Y_pct":-26.5786,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-08-01","peak_price":14510.0,"drawdown_after_peak_pct":-31.082,"green_lateness_ratio":null,"four_b_local_peak_proximity":"high","four_b_full_window_peak_proximity":"high","four_b_timing_verdict":"needed_at_or_near_trigger","four_b_evidence_type":"price_only_or_contract_without_margin_bridge","four_c_protection_label":"not_triggered_no_hard_thesis_break","trigger_outcome_label":"single_contract_too_early_high_mae_local_4b","current_profile_verdict":"current_profile_too_early_or_false_positive_if_actionable_without_margin_bridge","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_downloaded_tradable_window; 1Y/2Y may be unavailable_or_unchecked","same_entry_group_id":"001440_2024-07-26_C02_POWER_GRID_DATACENTER_CAPEX_single_contract_headline_without_current_margin_bridge","dedupe_for_aggregate":"keep_representative","aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false,"case_role":"4B_overlay_success","case_polarity":"counterexample","component_scores":{"eps_fcf_explosion":50,"earnings_visibility":60,"bottleneck_pricing":70,"market_mispricing":45,"valuation_rerating":40,"capital_allocation":40,"information_confidence":75},"weighted_proxy_total":55.3}
{"row_type":"trigger","trigger_id":"R1L145_C02_T07_006340_20240626","case_id":"C02_R1L145_006340_20240626_DAEWON_PRICE_ONLY_US_TRANSFORMER_EXPECTATION","symbol":"006340","company_name":"Daewon Cable","round":"R1","loop":145,"large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C02_POWER_GRID_DATACENTER_CAPEX","fine_archetype_id":"POWER_GRID_DATACENTER_CAPEX_ORDER_MARGIN_BRIDGE_VS_THEME_BLOWOFF","sector":"Cable / wire / theme sympathy","primary_archetype":"power_grid_datacenter_capex","loop_objective":"C02 direct URL/proxy repair and order-margin bridge vs theme-blowoff calibration","trigger_type":"Stage4B","trigger_date":"2024-06-26","evidence_available_at_that_date":"Proxy/news-flow: stock surged on U.S. transformer-order expectation and AI/data-center power narrative; no direct order/backlog bridge at trigger.","evidence_source":"https://securities.miraeasset.com/bbs/download/2129191.pdf?attachmentId=2129191 ; supplemental=https://securities.miraeasset.com/bbs/download/2125425.pdf?attachmentId=2125425","source_type":"broker_news_proxy","source_proxy_only":true,"stage2_evidence_fields":["AI/power-demand theme only","sympathy price movement"],"stage3_evidence_fields":[],"stage4b_evidence_fields":["price-only local peak","no direct customer/order/backlog evidence","maximum drawdown near -50% over 180D"],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/006/006340/2024.csv","profile_path":"atlas/symbol_profiles/006/006340.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","entry_date":"2024-06-27","entry_price":4350.0,"MFE_30D_pct":9.7701,"MFE_90D_pct":9.7701,"MFE_180D_pct":9.7701,"MFE_1Y_pct":9.7701,"MFE_2Y_pct":null,"MAE_30D_pct":-39.3103,"MAE_90D_pct":-41.3793,"MAE_180D_pct":-49.3103,"MAE_1Y_pct":-49.3103,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-06-28","peak_price":4775.0,"drawdown_after_peak_pct":-53.822,"green_lateness_ratio":null,"four_b_local_peak_proximity":"high","four_b_full_window_peak_proximity":"high","four_b_timing_verdict":"needed_at_or_near_trigger","four_b_evidence_type":"price_only_or_contract_without_margin_bridge","four_c_protection_label":"not_triggered_no_hard_thesis_break","trigger_outcome_label":"price_only_transformer_expectation_blowoff_high_mae","current_profile_verdict":"current_profile_false_positive_if_price_only_theme_given_actionable_bonus","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_downloaded_tradable_window; 1Y/2Y may be unavailable_or_unchecked","same_entry_group_id":"006340_2024-06-27_C02_POWER_GRID_DATACENTER_CAPEX_price_only_theme_expectation_no_direct_order_bridge","dedupe_for_aggregate":"keep_representative","aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false,"case_role":"price_moved_without_evidence","case_polarity":"counterexample","component_scores":{"eps_fcf_explosion":38,"earnings_visibility":35,"bottleneck_pricing":45,"market_mispricing":30,"valuation_rerating":25,"capital_allocation":30,"information_confidence":45},"weighted_proxy_total":36.03}
```

## Residual contribution

### Positive-side residual

- **Direct transformer/HVTR/HVDC/GIS exposure + order/backlog evidence**는 C02에서 실제 right-tail MFE를 강하게 설명했다. Hyosung, Jeryong, LS ELECTRIC, HD Hyundai Electric, Taihan 2024-09-19 모두 단순 theme보다 product/customer/order가 구체적이었다.

- 그러나 right-tail이 맞더라도 path가 곧장 평탄하지는 않았다. HD Hyundai Electric과 LS ELECTRIC은 180D/1Y right-tail이 강했지만 90D MAE가 깊었다. 따라서 C02 Green은 “좋은 산업”이 아니라 “견딜 수 있는 가격경로”까지 포함해야 한다.

### Counterexample-side residual

- **single-contract headline**은 Stage2-Actionable 후보가 될 수 있지만, current-year revenue/margin bridge가 빠지면 4B local cap이 필요했다. Taihan 2024-07-25는 같은 회사의 2024-09-19보다 evidence stack이 얇았고, entry 이후 180D MFE는 6.53%에 그친 반면 MAE는 -26.58%였다.

- **price-only U.S. transformer expectation**은 C02 evidence가 아니라 risk evidence다. Daewon Cable은 데이터센터/전력망 서사의 문패를 달았지만, 직접 order/backlog bridge가 없었고 180D MAE가 -49.31%까지 열렸다.

## Shadow rule candidate

```yaml
axis_id: C02_GRID_DATACENTER_ORDER_MARGIN_BRIDGE_GATE
scope: canonical_archetype_specific
large_sector_id: L1_INDUSTRIALS_INFRA_DEFENSE_GRID
canonical_archetype_id: C02_POWER_GRID_DATACENTER_CAPEX
rule_type: stage2_required_bridge_and_4b_local_cap
production_scoring_changed: false
shadow_weight_only: true
activation_condition: [C02 candidate; AI/data-center/power-grid CAPEX narrative; power transformer/GIS/switchgear/HVDC/HVAC/cable exposure]
positive_gate: Stage2-Actionable requires at least two of: direct customer/order/backlog evidence, high-voltage product mapping, current-year revenue or margin bridge, repeat/geographic customer expansion, official company evidence.
yellow_gate: Stage3-Yellow requires positive gate plus margin/order conversion or multiple public sources; contract headline alone capped below Yellow.
green_gate: Stage3-Green requires strong direct bottleneck evidence, visible conversion, and drawdown-aware confirmation; parabolic right-tail still needs later 4B overlay.
four_b_gate: If evidence is price-only, proxy-only, or single-contract-without-current-margin-bridge, cap as Stage4B/watch even if theme is hot.
four_c_delta: no hard-4C delta from this loop; future C02 loops should mine cancellation/delay/customer deferral cases.
expected_effect: reduce C02 false positives from AI-grid sympathy and single-headline chase while preserving structural transformer/HVDC winners.
```

## Same-entry and duplicate audit

| case | duplicate key | action | reason |
|---|---|---|---|
| C02_R1L145_267260_20250120_HDHE_4Q24_MARGIN_ORDER_BRIDGE | `C02_POWER_GRID_DATACENTER_CAPEX+267260+Stage3-Yellow+2025-01-21+direct_ir_margin_order_bridge` | keep_representative | New trigger_date/entry_date/evidence_family within this session; no reuse of recent C05/C01/C13/C15/C10 artifacts. |
| C02_R1L145_010120_20250120_LSELECTRIC_4Q24_US_HVTR_BACKLOG | `C02_POWER_GRID_DATACENTER_CAPEX+010120+Stage3-Yellow+2025-01-21+direct_ir_us_hvtr_backlog_growth` | keep_representative | New trigger_date/entry_date/evidence_family within this session; no reuse of recent C05/C01/C13/C15/C10 artifacts. |
| C02_R1L145_298040_20250519_HYOSUNG_EU_UHV_AI_SUPPLIER | `C02_POWER_GRID_DATACENTER_CAPEX+298040+Stage3-Green+2025-05-20+direct_contract_ai_grid_supplier_expansion` | keep_representative | New trigger_date/entry_date/evidence_family within this session; no reuse of recent C05/C01/C13/C15/C10 artifacts. |
| C02_R1L145_001440_20240919_TAIHAN_FIRST_US_HVDC | `C02_POWER_GRID_DATACENTER_CAPEX+001440+Stage2-Actionable+2024-09-20+direct_us_hvdc_hvac_order_accumulation` | keep_representative | New trigger_date/entry_date/evidence_family within this session; no reuse of recent C05/C01/C13/C15/C10 artifacts. |
| C02_R1L145_033100_20240318_JERYONG_US_DISTRIBUTION_TRANSFORMER_BACKLOG | `C02_POWER_GRID_DATACENTER_CAPEX+033100+Stage3-Green+2024-03-19+official_business_mapping_plus_us_shortage_backlog_bridge` | keep_representative | New trigger_date/entry_date/evidence_family within this session; no reuse of recent C05/C01/C13/C15/C10 artifacts. |
| C02_R1L145_001440_20240725_TAIHAN_SINGLE_CONTRACT_TOO_EARLY | `C02_POWER_GRID_DATACENTER_CAPEX+001440+Stage4B+2024-07-26+single_contract_headline_without_current_margin_bridge` | keep_representative | New trigger_date/entry_date/evidence_family within this session; no reuse of recent C05/C01/C13/C15/C10 artifacts. |
| C02_R1L145_006340_20240626_DAEWON_PRICE_ONLY_US_TRANSFORMER_EXPECTATION | `C02_POWER_GRID_DATACENTER_CAPEX+006340+Stage4B+2024-06-27+price_only_theme_expectation_no_direct_order_bridge` | keep_representative | New trigger_date/entry_date/evidence_family within this session; no reuse of recent C05/C01/C13/C15/C10 artifacts. |

## Batch Ingest Self-Audit

```text
expected_v12_result_file: true
filename_pattern_pass: true
metadata_filename_consistency: pass
round_schedule_status: coverage_index_selected
round_sector_consistency: pass
jsonl_trigger_row_count: 7
calibration_usable_trigger_count: 7
representative_trigger_count: 7
new_weight_evidence_candidate_count: 1
guardrail_candidate_count: 1
narrative_only_or_rejected_count: 0
rows_missing_required_mfe_mae: 0
rows_missing_entry_price_or_date: 0
rows_with_noncanonical_trigger_type: 0
rows_with_compact_mfe_mae_alias_only: 0
price_source: Songdaiki/stock-web
price_basis: tradable_raw
price_adjustment_status: raw_unadjusted_marcap
stock_agent_code_opened_or_patched: false
live_current_stock_discovery: false
ready_for_batch_ingest: true
```

## Deferred Coding Agent Handoff Prompt

```text
Do not patch production scoring from this MD alone. In the next batch calibration step, parse this v12 residual MD as a C02 canonical-archetype-specific shadow evidence candidate. Validate JSONL trigger rows, recalculate 30D/90D/180D MFE/MAE from Songdaiki/stock-web tradable shards, and test a C02_GRID_DATACENTER_ORDER_MARGIN_BRIDGE_GATE shadow rule. Compare false-positive reduction on price-only/proxy-only C02 rows against preservation of direct transformer/HVTR/HVDC winners. If multiple independent C02 loops confirm the same pattern, propose a guarded C02-specific stage2_required_bridge and 4B local cap patch spec only after aggregate validation.
```

## Final research state

```yaml
completed_round: R1
completed_loop: 145
completed_large_sector_id: L1_INDUSTRIALS_INFRA_DEFENSE_GRID
completed_canonical_archetype_id: C02_POWER_GRID_DATACENTER_CAPEX
completed_fine_archetype_id: POWER_GRID_DATACENTER_CAPEX_ORDER_MARGIN_BRIDGE_VS_THEME_BLOWOFF
loop_contribution_label: C02_grid_datacenter_order_margin_bridge_gate_positive_counter_4b_quality_repair
selected_priority_bucket: Priority 0/1 quality repair — direct URL repair, proxy-only reduction, C02 4B-heavy balance, hard-4C future mining gap
positive_case_count: 5
counterexample_count: 2
calibration_usable_trigger_count: 7
source_proxy_only_count: 1
evidence_url_pending_count: 0
rows_missing_required_mfe_mae: 0
production_scoring_changed: false
shadow_weight_only: true
round_schedule_status: coverage_index_selected
round_sector_consistency: pass
next_recommended_archetypes: [C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH, C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF, C14_EV_DEMAND_SLOWDOWN_4B_4C, C16_STRATEGIC_RESOURCE_POLICY_SUPPLY]
```
