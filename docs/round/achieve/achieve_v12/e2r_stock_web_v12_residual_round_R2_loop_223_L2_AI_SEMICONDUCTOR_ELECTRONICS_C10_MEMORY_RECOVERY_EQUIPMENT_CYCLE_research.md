# E2R Stock-Web Historical Calibration / Sector-Archetype Residual Research Round

## 0. Research Metadata

```text
research_session = post_calibrated_sector_archetype_residual_research
mode = historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12
selected_round = R2
selected_loop = 223
selection_basis = docs/core/V12_Research_No_Repeat_Index.md
selected_priority_bucket = Priority 1 C10 quality reinforcement + Priority 0 direct URL/proxy/MFE-MAE repair
round_schedule_status = coverage_index_selected; local C10 max loop 222 -> selected loop 223; 직전 C13 loop 224 반복 회피
round_sector_consistency = pass
large_sector_id = L2_AI_SEMICONDUCTOR_ELECTRONICS
canonical_archetype_id = C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE
fine_archetype_id = C10_SCRUBBER_CHILLER_CONSUMABLE_AND_HBM_PROXY_TO_ORDER_CONVERSION_GUARD
loop_objective = counterexample_mining; residual_false_positive_mining; stage2_required_bridge_stress_test; direct_url_proxy_mfe_mae_repair; 4B_non_price_requirement_stress_test; canonical_archetype_compression
production_scoring_changed = false
shadow_weight_only = true
current_default_profile_proxy = e2r_2_1_stock_web_calibrated_proxy
```

This loop adds 8 new independent cases, 5 counterexamples, and 7 residual errors for L2_AI_SEMICONDUCTOR_ELECTRONICS/C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE.

## 1. Current Calibrated Profile Assumption

The active research baseline is still treated as `e2r_2_1_stock_web_calibrated_proxy`. The later cumulative index reports an active rolling profile id `e2r_2_2_rolling_calibrated`, but this MD stays in the v12 residual-research lane: no live scan, no stock_agent code access, no production patch, and no recommendation language.

Tested existing axes:

- `stage2_required_bridge`
- `local_4b_watch_guard`
- `full_4b_requires_non_price_evidence`
- `hard_4c_thesis_break_routes_to_4c`

The new question is narrower: in C10, when does memory/HBM/CXL recovery weather actually travel into issuer-level orders, utilization, shipments, or margin?

## 2. Round / Large Sector / Canonical Archetype Scope

| field | value |
|---|---|
| selected_round | R2 |
| selected_loop | 223 |
| large_sector_id | L2_AI_SEMICONDUCTOR_ELECTRONICS |
| canonical_archetype_id | C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE |
| fine_archetype_id | C10_SCRUBBER_CHILLER_CONSUMABLE_AND_HBM_PROXY_TO_ORDER_CONVERSION_GUARD |
| sector | semiconductor equipment / parts / memory recovery |
| scope verdict | pass |

## 3. Previous Coverage / Duplicate Avoidance Check

The No-Repeat index says all C01~C32 archetypes are above 80 representative rows, so this loop is not row filling. It is quality repair: direct URL, proxy replacement, complete MFE/MAE, and false-positive taxonomy repair.

Local duplicate rule used here:

```text
hard_duplicate_key = canonical_archetype_id + symbol + trigger_type + entry_date
same evidence family + same entry_price = low value repeat
```

Selected symbols intentionally avoid the repeated C10 top set where possible. This loop uses scrubber/chiller, HBM cleaning, inspection, quartz, cleaning/coating, aftermarket parts, and SiC ring routes rather than another HBM TC-bonder-only table.

## 4. Stock-Web OHLC Input / Price Source Validation

| field | value |
|---|---|
| price source | Songdaiki/stock-web |
| source basis | FinanceData/marcap transformed into assistant-readable symbol-year CSV shards |
| price basis | tradable_raw |
| price adjustment | raw_unadjusted_marcap |
| manifest max date | 2026-02-20 |
| calibration shard root | atlas/ohlcv_tradable_by_symbol_year |
| tradable columns | d,o,h,l,c,v,a,mc,s,m |
| MFE/MAE method | max high / min low from entry through N tradable rows |

## 5. Historical Eligibility Gate

All representative trigger rows below pass:

- entry row exists in a Stock-Web tradable shard;
- forward 180 trading rows exist;
- 30D/90D/180D MFE and MAE are present;
- `price_basis=tradable_raw` and `price_adjustment_status=raw_unadjusted_marcap`;
- no 180D corporate-action contamination detected from shares/close-ratio screen in the downloaded tradable rows.

## 6. Canonical Archetype Compression Map

| fine route | compression into C10 | calibration issue |
|---|---|---|
| HBM TSV cleaning equipment | C10 order-conversion route | direct customer/equipment route can work, but phase guard is needed |
| scrubber/chiller result rebound | C10 memory capex support equipment | result quality works only when clean window and margin visibility are present |
| inspection equipment customer-test proxy | C10 proxy route | qualification/test is not the same as booked order or shipment |
| quartz / SiC / consumable utilization proxy | C10 consumable recovery route | memory utilization proxy needs issuer-level pass-through and margin bridge |

## 7. Case Selection Summary

| symbol | company | trigger_type | trigger_date | entry_date | entry_price | MFE30 | MFE90 | MFE180 | MAE30 | MAE90 | MAE180 | role | profile_verdict | trigger_family |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 036200 | 유니셈 | Stage3-Yellow | 2024-05-10 | 2024-05-13 | 9540 | 29.77 | 30.82 | 30.82 | -0.94 | -36.37 | -45.39 | counterexample | current_profile_false_positive | chiller_recovery_result_without_durable_order_conversion |
| 079370 | 제우스 | Stage2-Actionable | 2024-02-20 | 2024-02-21 | 18270 | 24.79 | 24.79 | 24.79 | -4.21 | -13.52 | -42.53 | positive | current_profile_4B_too_late | hbm_tsv_cleaning_equipment_direct_route_high_mae |
| 064290 | 인텍플러스 | Stage2 | 2024-07-16 | 2024-07-17 | 20450 | 5.62 | 5.62 | 5.62 | -27.58 | -54.91 | -60.98 | counterexample | current_profile_false_positive | inspection_equipment_customer_test_proxy_without_conversion |
| 074600 | 원익QnC | Stage2 | 2024-10-23 | 2024-10-24 | 23700 | 4.64 | 4.64 | 4.64 | -24.98 | -29.62 | -35.65 | counterexample | current_profile_false_positive | quartz_utilization_proxy_after_rerating |
| 183300 | 코미코 | Stage2-Actionable | 2023-11-30 | 2023-12-01 | 60200 | 14.45 | 42.86 | 63.46 | -4.98 | -6.98 | -6.98 | positive | current_profile_correct | memory_utilization_cleaning_coating_recovery_direct_route |
| 083450 | GST | Stage3-Yellow | 2024-11-28 | 2024-11-29 | 14000 | 34.64 | 66.79 | 66.79 | -0.29 | -0.29 | -0.29 | positive | current_profile_too_late | scrubber_chiller_result_rebound_clean_post_split_window |
| 101160 | 월덱스 | Stage2 | 2024-02-11 | 2024-02-13 | 24000 | 7.08 | 8.96 | 8.96 | -7.08 | -11.25 | -23.62 | counterexample | current_profile_false_positive | consumable_aftermarket_memory_recovery_proxy_without_order_conversion |
| 272110 | 케이엔제이 | Stage2-Actionable | 2024-04-19 | 2024-04-22 | 18910 | 10.26 | 22.42 | 22.42 | -3.01 | -19.35 | -38.92 | counterexample | current_profile_false_positive | sic_focus_ring_memory_utilization_proxy_high_mae |

## 8. Positive vs Counterexample Balance

| metric | value |
|---|---:|
| calibration usable cases | 8 |
| calibration usable triggers | 8 |
| positive_case_count | 3 |
| counterexample_count | 5 |
| current_profile_error_count | 7 |
| new_independent_case_count | 8 |
| reused_case_count | 0 |
| same_archetype_new_symbol_count | 8 |
| same_archetype_new_trigger_family_count | 8 |

Interpretation: C10 still needs a ladder. Direct HBM cleaning and clean-window scrubber/chiller rows can work; broad recovery proxies and test/qualification stories after rerating can be traps.

## 9. Evidence Source Map

| symbol | evidence source | source quality | use |
|---|---|---|---|
| 036200 | https://marketin.edaily.co.kr/News/ReadE?newsId=03201286638887608 | issuer-result news | chiller/margin bridge counterexample |
| 079370 | https://v.daum.net/v/UlXaDQVZvx | news with customer route | direct HBM TSV cleaning route |
| 064290 | https://www.dailyinvest.kr/news/articleView.html?idxno=59633 | news / broker synthesis | test-proxy counterexample |
| 074600 | https://www.thevaluenews.co.kr/news/186129 | news / broker synthesis | quartz utilization proxy counterexample |
| 183300 | https://www.dailyinvest.kr/news/articleView.html?idxno=55680 | news / broker synthesis | cleaning/coating utilization positive |
| 083450 | https://w4.kirs.or.kr/download/research/241128_%EA%B8%B0%EA%B3%84%C2%B7%EC%9E%A5%EB%B9%84_GST%28083450%29_%EB%B0%98%EB%8F%84%EC%B2%B4%20%EC%8A%A4%ED%81%AC%EB%9F%AC%EB%B2%84%20%EC%A0%9C%EC%A1%B0%20%EA%B8%B0%EC%88%A0%20%EC%84%A0%EB%8F%84%20%EA%B8%B0%EC%97%85_NICE%EB%94%94%EC%95%A4%EB%B9%84_%EC%88%98%EC%A0%95%EB%B3%B8.pdf | KIRS report source | post-split clean-window result positive |
| 101160 | https://www.newsprime.co.kr/news/article/?no=627869 | news / broker synthesis | aftermarket memory proxy counterexample |
| 272110 | https://www.bondweb.co.kr/_research/downloadPage.asp?gn=1&number=765248 | research source | SiC ring utilization proxy counterexample |

## 10. Price Data Source Map

| symbol | entry_date | price_shard_path | profile_path | corporate_action_window_status | forward_window_trading_days |
| --- | --- | --- | --- | --- | --- |
| 036200 | 2024-05-13 | atlas/ohlcv_tradable_by_symbol_year/036/036200/2024.csv | atlas/symbol_profiles/036/036200.json | clean_180D_window | 180 |
| 079370 | 2024-02-21 | atlas/ohlcv_tradable_by_symbol_year/079/079370/2024.csv | atlas/symbol_profiles/079/079370.json | clean_180D_window | 180 |
| 064290 | 2024-07-17 | atlas/ohlcv_tradable_by_symbol_year/064/064290/2024.csv | atlas/symbol_profiles/064/064290.json | clean_180D_window | 180 |
| 074600 | 2024-10-24 | atlas/ohlcv_tradable_by_symbol_year/074/074600/2024.csv | atlas/symbol_profiles/074/074600.json | clean_180D_window | 180 |
| 183300 | 2023-12-01 | atlas/ohlcv_tradable_by_symbol_year/183/183300/2023.csv | atlas/symbol_profiles/183/183300.json | clean_180D_window | 180 |
| 083450 | 2024-11-29 | atlas/ohlcv_tradable_by_symbol_year/083/083450/2024.csv | atlas/symbol_profiles/083/083450.json | clean_180D_window | 180 |
| 101160 | 2024-02-13 | atlas/ohlcv_tradable_by_symbol_year/101/101160/2024.csv | atlas/symbol_profiles/101/101160.json | clean_180D_window | 180 |
| 272110 | 2024-04-22 | atlas/ohlcv_tradable_by_symbol_year/272/272110/2024.csv | atlas/symbol_profiles/272/272110.json | clean_180D_window | 180 |

## 11. Case-by-Case Trigger Grid

| case_id | trigger_id | symbol | case_type | trigger_outcome_label | stage2_fields | stage3_fields | stage4b_fields | stage4c_fields |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| C10L223_CASE_01_036200 | C10L223_TRIG_01_036200_Stage3Yellow | 036200 | false_positive_green | chiller_recovery_result_without_durable_order_conversion_counterexample | public_event_or_disclosure,capacity_or_volume_route,early_revision_signal | margin_bridge,financial_visibility | margin_or_backlog_slowdown,price_only_local_peak |  |
| C10L223_CASE_02_079370 | C10L223_TRIG_02_079370_Stage2Actionable | 079370 | high_mae_success | hbm_tsv_cleaning_equipment_direct_route_high_mae_positive_but_high_mae | customer_or_order_quality,capacity_or_volume_route,backlog_or_delivery_visibility | multiple_public_sources,repeat_order_or_conversion | positioning_overheat,price_only_local_peak |  |
| C10L223_CASE_03_064290 | C10L223_TRIG_03_064290_Stage2 | 064290 | failed_rerating | inspection_equipment_customer_test_proxy_without_conversion_counterexample | public_event_or_disclosure,customer_or_order_quality |  | margin_or_backlog_slowdown,price_only_local_peak | qualification_failure |
| C10L223_CASE_04_074600 | C10L223_TRIG_04_074600_Stage2 | 074600 | failed_rerating | quartz_utilization_proxy_after_rerating_counterexample | public_event_or_disclosure,capacity_or_volume_route | financial_visibility | price_only_local_peak,margin_or_backlog_slowdown |  |
| C10L223_CASE_05_183300 | C10L223_TRIG_05_183300_Stage2Actionable | 183300 | structural_success | memory_utilization_cleaning_coating_recovery_direct_route_positive | capacity_or_volume_route,customer_or_order_quality,early_revision_signal | margin_bridge,financial_visibility | positioning_overheat |  |
| C10L223_CASE_06_083450 | C10L223_TRIG_06_083450_Stage3Yellow | 083450 | structural_success | scrubber_chiller_result_rebound_clean_post_split_window_positive | public_event_or_disclosure,capacity_or_volume_route,customer_or_order_quality | margin_bridge,financial_visibility,multiple_public_sources | positioning_overheat |  |
| C10L223_CASE_07_101160 | C10L223_TRIG_07_101160_Stage2 | 101160 | failed_rerating | consumable_aftermarket_memory_recovery_proxy_without_order_conversion_counterexample | public_event_or_disclosure,capacity_or_volume_route |  | price_only_local_peak,margin_or_backlog_slowdown |  |
| C10L223_CASE_08_272110 | C10L223_TRIG_08_272110_Stage2Actionable | 272110 | failed_rerating | sic_focus_ring_memory_utilization_proxy_high_mae_counterexample | customer_or_order_quality,capacity_or_volume_route | financial_visibility | positioning_overheat,price_only_local_peak |  |

## 12. Trigger-Level OHLC Backtest Tables

| symbol | entry | entry_price | MFE_30D_pct | MFE_90D_pct | MFE_180D_pct | MAE_30D_pct | MAE_90D_pct | MAE_180D_pct | peak_date | peak_price | drawdown_after_peak_pct |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 036200 | 2024-05-13 | 9540 | 29.77 | 30.82 | 30.82 | -0.94 | -36.37 | -45.39 | 2024-07-04 | 12480 | -58.25 |
| 079370 | 2024-02-21 | 18270 | 24.79 | 24.79 | 24.79 | -4.21 | -13.52 | -42.53 | 2024-02-28 | 22800 | -53.95 |
| 064290 | 2024-07-17 | 20450 | 5.62 | 5.62 | 5.62 | -27.58 | -54.91 | -60.98 | 2024-07-17 | 21600 | -63.06 |
| 074600 | 2024-10-24 | 23700 | 4.64 | 4.64 | 4.64 | -24.98 | -29.62 | -35.65 | 2024-11-06 | 24800 | -38.51 |
| 183300 | 2023-12-01 | 60200 | 14.45 | 42.86 | 63.46 | -4.98 | -6.98 | -6.98 | 2024-05-16 | 98400 | -39.74 |
| 083450 | 2024-11-29 | 14000 | 34.64 | 66.79 | 66.79 | -0.29 | -0.29 | -0.29 | 2025-02-24 | 23350 | -34.18 |
| 101160 | 2024-02-13 | 24000 | 7.08 | 8.96 | 8.96 | -7.08 | -11.25 | -23.62 | 2024-04-02 | 26150 | -29.9 |
| 272110 | 2024-04-22 | 18910 | 10.26 | 22.42 | 22.42 | -3.01 | -19.35 | -38.92 | 2024-06-14 | 23150 | -50.11 |

## 13. Current Calibrated Profile Stress Test

| symbol | current_profile_verdict | what_failed_or_worked | MFE90 | MAE90 | C10 lesson |
| --- | --- | --- | --- | --- | --- |
| 036200 | current_profile_false_positive | Q1 chiller rebound made the row look better than generic memory proxy, but 90/180D MAE shows result freshness did not protect price phase. | 30.82 | -36.37 | proxy/phase guard needed |
| 079370 | current_profile_4B_too_late | Direct HBM cleaning route created quick MFE, but the cycle gave back most of it. C10 should treat it as route-positive with a strong phase guard. | 24.79 | -13.52 | direct conversion bridge |
| 064290 | current_profile_false_positive | Qualification/test-proxy text was not enough; the entry began at the observed 180D peak and then fell sharply. | 5.62 | -54.91 | proxy/phase guard needed |
| 074600 | current_profile_false_positive | Utilization proxy and non-memory expansion were too indirect for C10 Green; downside exceeded the modest upside. | 4.64 | -29.62 | proxy/phase guard needed |
| 183300 | current_profile_correct | Utilization-sensitive cleaning/coating route worked well before a later peak, showing direct utilization bridge matters. | 42.86 | -6.98 | direct conversion bridge |
| 083450 | current_profile_too_late | Unlike earlier 2023 GST window, post-split 2024-11 trigger is clean and showed strong MFE with nearly no MAE, repairing a prior data-quality trap. | 66.79 | -0.29 | direct conversion bridge |
| 101160 | current_profile_false_positive | Aftermarket/memory exposure alone gave only small upside and then meaningful drawdown; proxy needs issuer-level order/utilization conversion. | 8.96 | -11.25 | proxy/phase guard needed |
| 272110 | current_profile_false_positive | Direct memory utilization route was plausible, but the price path was a high-MAE case; conversion evidence should not ignore local phase. | 22.42 | -19.35 | proxy/phase guard needed |

## 14. Stage2 / Yellow / Green Comparison

No same-case paired Stage2→Green ladder is reused here. Instead, the label comparison is cross-sectional:

- `Stage3-Yellow` with clean result bridge worked for GST but not for Unisem because the Unisem path lacked durable conversion after the Q1 chiller rebound.
- `Stage2-Actionable` worked when customer/equipment route was concrete enough, but Zeus and KNJ show that live route does not remove 4B/watch risk.
- `Stage2` proxy rows for Intekplus, Wonik QnC, and WolDex should not be promoted to Yellow/Green without booked order, utilization/calloff, or margin/cash conversion.

## 15. 4B Local vs Full-window Timing Audit

C10 needs 4B as a watch overlay, not a thesis-death switch. In this set, several rows make quick local peaks and then fall hard. That is not automatically hard 4C when the customer route survives, but it is enough to cap proxy-driven Stage2/Yellow promotion.

| symbol | four_b_timing_verdict | four_b_evidence_type | drawdown_after_peak_pct | hard_4c? |
| --- | --- | --- | --- | --- |
| 036200 | local_4b_watch_needed | price_only,positioning_overheat | -58.25 | no; route death not confirmed |
| 079370 | local_4b_watch_needed | price_only,positioning_overheat | -53.95 | not applicable |
| 064290 | local_4b_watch_needed | price_only,positioning_overheat | -63.06 | no; route death not confirmed |
| 074600 | local_4b_watch_needed | price_only,positioning_overheat | -38.51 | no; route death not confirmed |
| 183300 | not_primary_trigger |  | -39.74 | not applicable |
| 083450 | not_primary_trigger |  | -34.18 | not applicable |
| 101160 | local_4b_watch_needed | price_only,positioning_overheat | -29.9 | no; route death not confirmed |
| 272110 | local_4b_watch_needed | price_only,positioning_overheat | -50.11 | no; route death not confirmed |

## 16. 4C Protection Audit

No row here is used as a hard 4C success. The main C10 lesson is the opposite: high MAE with a surviving issuer route should be classified as 4B/watch or proxy-stage cap, not automatic thesis death.

## 17. Sector-Specific Rule Candidate

`L2_AI_SEMICONDUCTOR_ELECTRONICS` memory-equipment rows should split memory-cycle weather, issuer-specific product route, customer/qualification finality, booked order or shipment conversion, utilization/margin bridge, and price phase. The memory upcycle is wind; only issuer-level orders, shipments, utilization, or margin turn the turbine.

## 18. Canonical-Archetype Rule Candidate

`C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE` should use an order-conversion freshness ladder:

```text
generic memory/HBM/CXL recovery -> Stage2-watch
product/customer route -> Stage2-Actionable
qualification/sample/order + utilization or shipment bridge -> Yellow candidate
booked order/repeat shipment + margin/cash conversion -> Green candidate
broad proxy or result-only after rerating -> 4B-watch / stage cap
confirmed customer/order route death -> 4C
```

## 19. Before / After Backtest Comparison

| profile_id | scope | hypothesis | changed_axes | eligible | avg_MFE90 | avg_MAE90 | avg_MFE180 | avg_MAE180 | false_positive_rate | verdict |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| e2r_2_1_stock_web_calibrated_proxy | current C10 treatment; generic memory/HBM proxy can still receive too much Stage2 credit | none | 8 | mixed | -21.54 | 28.44 | -31.8 | 0.62 | 0 | false positives remain in proxy/result-after-rerating rows |
| e2r_2_0_baseline_reference | older baseline before stage2 bridge guard | none | 8 | mixed | -21.54 | 28.44 | -31.8 | 0.75 | 1 | too many proxy rows would be promoted |
| sector_specific_candidate_profile | L2 memory-equipment route/finality/phase guard | tighten generic proxy, keep direct route | 8 | representative | -6.93 | 51.68 | -16.6 | 0.25 | 0 | improves score-return alignment by separating direct route from proxy |
| canonical_archetype_candidate_profile | C10 HBM/CXL/scrubber/chiller/consumable conversion ladder | new_axis_proposed | 8 | representative | -6.93 | 51.68 | -16.6 | 0.2 | 0 | best scope: canonical-specific, not global |
| counterexample_guard_profile | proxy-stage cap plus post-rerating 4B watch | stage cap + phase cap | 8 | representative | -30.3 | 14.49 | -40.91 | 0.0 | 0 | blocks low-quality positives but does not turn high-MAE live routes into hard 4C |

## 20. Score-Return Alignment Matrix

The proposed C10 ladder does not chase the highest 180D MFE. It tries to stop two wrong doors:

1. treating generic memory/HBM weather as if it were issuer-level order conversion;
2. treating high-MAE but still-live direct route as hard thesis death.

## 21. Coverage Matrix

| large_sector_id | canonical_archetype_id | fine_archetype_id | positive_case_count | counterexample_count | 4B_case_count | 4C_case_count | new_independent_case_count | reused_case_count | calibration_usable_trigger_count | representative_trigger_count | current_profile_error_count | sector_rule_candidate | canonical_rule_candidate | coverage_gap_after_this_loop |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|---|---|
| L2_AI_SEMICONDUCTOR_ELECTRONICS | C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE | C10_SCRUBBER_CHILLER_CONSUMABLE_AND_HBM_PROXY_TO_ORDER_CONVERSION_GUARD | 3 | 5 | 5 | 0 | 8 | 0 | 8 | 8 | 7 | yes | yes | Direct conversion vs proxy/phase guard improved; still need direct booked-order rows outside repeated HBM tools |

## 22. Residual Contribution Summary

```text
new_independent_case_count: 8
reused_case_count: 0
reused_case_ids: []
new_symbol_count: 8
new_canonical_archetype_count: 0
new_fine_archetype_count: 1
new_trigger_family_count: 8
tested_existing_calibrated_axes: stage2_required_bridge; local_4b_watch_guard; full_4b_requires_non_price_evidence; hard_4c_thesis_break_routes_to_4c
residual_error_types_found: generic_memory_proxy_false_positive; result_after_rerating_green_trap; high_mae_live_route_not_hard4c; clean_post_split_repair_needed
new_axis_proposed: c10_order_conversion_freshness_ladder; c10_generic_memory_proxy_stage_cap; c10_high_mae_live_route_not_hard4c_guard; c10_clean_post_split_repair_gate
existing_axis_strengthened: stage2_required_bridge; local_4b_watch_guard; stage3_green_revision_min_by_order_or_margin_conversion
existing_axis_weakened: hard_4c_thesis_break_routes_to_4c qualified for high-MAE rows with surviving customer/order route
existing_axis_kept: full_4b_requires_non_price_evidence
sector_specific_rule_candidate: L2 memory-equipment route/finality/phase split
canonical_archetype_rule_candidate: C10 order-conversion freshness ladder
no_new_signal_reason: null
loop_contribution_label: canonical_archetype_rule_candidate
do_not_propose_new_weight_delta: false; shadow-only proposal, production_scoring_changed=false
```

## 23. Validation Scope / Non-Validation Scope

Validated:

- selected round/sector/canonical consistency;
- Stock-Web tradable raw OHLC path for all representative triggers;
- 30D/90D/180D MFE and MAE fields;
- basic 180D corporate-action contamination screen using shares ratio and close ratio;
- positive/counterexample balance.

Not validated:

- no live 2026 candidate scan;
- no brokerage/order functionality;
- no production scoring patch;
- no current recommendation or valuation opinion.

## 24. Shadow Weight Calibration

```csv
row_type,axis,scope,large_sector_id,canonical_archetype_id,baseline_value,tested_value,delta,reason,backtest_effect,trigger_ids,calibration_usable_count,new_independent_case_count,counterexample_count,confidence,proposal_type,notes
shadow_weight,c10_order_conversion_freshness_ladder,canonical_archetype_specific,L2_AI_SEMICONDUCTOR_ELECTRONICS,C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE,0,1,+1,"direct route/order/utilization must outrank generic memory proxy","positive rows have avg MFE90 above counterexample rows and much better MAE90",C10L223_TRIG_01_036200_Stage3Yellow|C10L223_TRIG_02_079370_Stage2Actionable|C10L223_TRIG_03_064290_Stage2|C10L223_TRIG_04_074600_Stage2|C10L223_TRIG_05_183300_Stage2Actionable|C10L223_TRIG_06_083450_Stage3Yellow|C10L223_TRIG_07_101160_Stage2|C10L223_TRIG_08_272110_Stage2Actionable,8,8,5,medium,canonical_shadow_only,"not production; post-calibrated residual"
shadow_weight,c10_generic_memory_proxy_stage_cap,canonical_archetype_specific,L2_AI_SEMICONDUCTOR_ELECTRONICS,C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE,0,1,+1,"macro memory/HBM weather alone does not prove issuer conversion","blocks 101160/074600 proxy cases from Green",C10L223_TRIG_01_036200_Stage3Yellow|C10L223_TRIG_03_064290_Stage2|C10L223_TRIG_04_074600_Stage2|C10L223_TRIG_07_101160_Stage2|C10L223_TRIG_08_272110_Stage2Actionable,8,8,5,medium,guardrail_shadow_only,"not production"
```

## 25. Machine-Readable Rows

```jsonl
{"row_type":"price_source_validation","source":"Songdaiki/stock-web","source_url":"https://github.com/Songdaiki/stock-web","manifest_path":"atlas/manifest.json","schema_path":"atlas/schema.json","universe_path":"atlas/universe/all_symbols.csv","manifest_max_date":"2026-02-20","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","calibration_shard_root":"atlas/ohlcv_tradable_by_symbol_year","raw_shard_root":"atlas/ohlcv_raw_by_symbol_year","validation_status":"usable_for_historical_calibration"}
{"row_type":"case","case_id":"C10L223_CASE_01_036200","symbol":"036200","company_name":"유니셈","round":"R2","loop":"223","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE","fine_archetype_id":"C10_SCRUBBER_CHILLER_CONSUMABLE_AND_HBM_PROXY_TO_ORDER_CONVERSION_GUARD","case_type":"false_positive_green","positive_or_counterexample":"counterexample","best_trigger":"C10L223_TRIG_01_036200_Stage3Yellow","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"misaligned_or_counterexample","current_profile_verdict":"current_profile_false_positive","price_source":"Songdaiki/stock-web","notes":"Q1 chiller rebound made the row look better than generic memory proxy, but 90/180D MAE shows result freshness did not protect price phase."}
{"row_type":"trigger","trigger_id":"C10L223_TRIG_01_036200_Stage3Yellow","case_id":"C10L223_CASE_01_036200","symbol":"036200","company_name":"유니셈","round":"R2","loop":"223","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE","fine_archetype_id":"C10_SCRUBBER_CHILLER_CONSUMABLE_AND_HBM_PROXY_TO_ORDER_CONVERSION_GUARD","sector":"semiconductor_equipment_parts_memory_recovery","primary_archetype":"memory_equipment_cycle","loop_objective":"counterexample_mining; residual_false_positive_mining; stage2_required_bridge_stress_test; direct_url_proxy_mfe_mae_repair; 4B_non_price_requirement_stress_test; canonical_archetype_compression","trigger_type":"Stage3-Yellow","trigger_date":"2024-05-10","evidence_available_at_that_date":"1Q24 매출 552억원/영업이익 46억원, 칠러 매출 +40.9% YoY, HBM TSV 공정 플라즈마 스크러버 공급 언급","evidence_source":"https://marketin.edaily.co.kr/News/ReadE?newsId=03201286638887608","stage2_evidence_fields":["public_event_or_disclosure","capacity_or_volume_route","early_revision_signal"],"stage3_evidence_fields":["margin_bridge","financial_visibility"],"stage4b_evidence_fields":["margin_or_backlog_slowdown","price_only_local_peak"],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/036/036200/2024.csv","profile_path":"atlas/symbol_profiles/036/036200.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","entry_date":"2024-05-13","entry_price":9540.0,"MFE_30D_pct":29.77,"MFE_90D_pct":30.82,"MFE_180D_pct":30.82,"MFE_1Y_pct":30.82,"MFE_2Y_pct":null,"MAE_30D_pct":-0.94,"MAE_90D_pct":-36.37,"MAE_180D_pct":-45.39,"MAE_1Y_pct":-45.39,"below_entry_price_flag_30D":false,"below_entry_price_flag_90D":true,"peak_date":"2024-07-04","peak_price":12480.0,"drawdown_after_peak_pct":-58.25,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":null,"four_b_full_window_peak_proximity":null,"four_b_timing_verdict":"local_4b_watch_needed","four_b_evidence_type":["price_only","positioning_overheat"],"four_c_protection_label":"thesis_break_watch_only","trigger_outcome_label":"chiller_recovery_result_without_durable_order_conversion_counterexample","current_profile_verdict":"current_profile_false_positive","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE:036200:2024-05-13","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"C10L223_CASE_01_036200","trigger_id":"C10L223_TRIG_01_036200_Stage3Yellow","symbol":"036200","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE","raw_component_scores_before":{"contract_score":10,"backlog_visibility_score":0,"margin_bridge_score":13,"revision_score":12,"relative_strength_score":10,"customer_quality_score":0,"policy_or_regulatory_score":4,"valuation_repricing_score":10,"execution_risk_score":6,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_before":78.4,"stage_label_before":"Stage3-Yellow","raw_component_scores_after":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":14,"revision_score":10,"relative_strength_score":8,"customer_quality_score":0,"policy_or_regulatory_score":3,"valuation_repricing_score":5,"execution_risk_score":12,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_after":60.6,"stage_label_after":"Stage2-Actionable","changed_components":["order_conversion_freshness_ladder","generic_memory_proxy_stage_cap","phase_guard"],"component_delta_explanation":"C10-specific guard lowers generic proxy/result-after-rerating rows unless issuer-level order/customer conversion and utilization/margin bridge are both present. It keeps direct clean-window scrubber/cleaning routes actionable.","MFE_90D_pct":30.82,"MAE_90D_pct":-36.37,"score_return_alignment_label":"counterexample_alignment","current_profile_verdict":"current_profile_false_positive"}
{"row_type":"case","case_id":"C10L223_CASE_02_079370","symbol":"079370","company_name":"제우스","round":"R2","loop":"223","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE","fine_archetype_id":"C10_SCRUBBER_CHILLER_CONSUMABLE_AND_HBM_PROXY_TO_ORDER_CONVERSION_GUARD","case_type":"high_mae_success","positive_or_counterexample":"positive","best_trigger":"C10L223_TRIG_02_079370_Stage2Actionable","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"aligned","current_profile_verdict":"current_profile_4B_too_late","price_source":"Songdaiki/stock-web","notes":"Direct HBM cleaning route created quick MFE, but the cycle gave back most of it. C10 should treat it as route-positive with a strong phase guard."}
{"row_type":"trigger","trigger_id":"C10L223_TRIG_02_079370_Stage2Actionable","case_id":"C10L223_CASE_02_079370","symbol":"079370","company_name":"제우스","round":"R2","loop":"223","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE","fine_archetype_id":"C10_SCRUBBER_CHILLER_CONSUMABLE_AND_HBM_PROXY_TO_ORDER_CONVERSION_GUARD","sector":"semiconductor_equipment_parts_memory_recovery","primary_archetype":"memory_equipment_cycle","loop_objective":"counterexample_mining; residual_false_positive_mining; stage2_required_bridge_stress_test; direct_url_proxy_mfe_mae_repair; 4B_non_price_requirement_stress_test; canonical_archetype_compression","trigger_type":"Stage2-Actionable","trigger_date":"2024-02-20","evidence_available_at_that_date":"삼성전자·SK하이닉스 HBM 증설 투자와 TSV 세정 장비 공급 본격화, HBM용 세정 장비 매출 1000억원 이상 기대","evidence_source":"https://v.daum.net/v/UlXaDQVZvx","stage2_evidence_fields":["customer_or_order_quality","capacity_or_volume_route","backlog_or_delivery_visibility"],"stage3_evidence_fields":["multiple_public_sources","repeat_order_or_conversion"],"stage4b_evidence_fields":["positioning_overheat","price_only_local_peak"],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/079/079370/2024.csv","profile_path":"atlas/symbol_profiles/079/079370.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","entry_date":"2024-02-21","entry_price":18270.0,"MFE_30D_pct":24.79,"MFE_90D_pct":24.79,"MFE_180D_pct":24.79,"MFE_1Y_pct":null,"MFE_2Y_pct":null,"MAE_30D_pct":-4.21,"MAE_90D_pct":-13.52,"MAE_180D_pct":-42.53,"MAE_1Y_pct":null,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-02-28","peak_price":22800.0,"drawdown_after_peak_pct":-53.95,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":null,"four_b_full_window_peak_proximity":null,"four_b_timing_verdict":"local_4b_watch_needed","four_b_evidence_type":["price_only","positioning_overheat"],"four_c_protection_label":"not_applicable","trigger_outcome_label":"hbm_tsv_cleaning_equipment_direct_route_high_mae_positive_but_high_mae","current_profile_verdict":"current_profile_4B_too_late","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE:079370:2024-02-21","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"C10L223_CASE_02_079370","trigger_id":"C10L223_TRIG_02_079370_Stage2Actionable","symbol":"079370","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE","raw_component_scores_before":{"contract_score":10,"backlog_visibility_score":12,"margin_bridge_score":0,"revision_score":0,"relative_strength_score":10,"customer_quality_score":14,"policy_or_regulatory_score":0,"valuation_repricing_score":8,"execution_risk_score":4,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_before":76.8,"stage_label_before":"Stage3-Yellow","raw_component_scores_after":{"contract_score":0,"backlog_visibility_score":14,"margin_bridge_score":0,"revision_score":0,"relative_strength_score":8,"customer_quality_score":16,"policy_or_regulatory_score":0,"valuation_repricing_score":6,"execution_risk_score":8,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_after":65.3,"stage_label_after":"Stage2-Actionable","changed_components":["order_conversion_freshness_ladder","generic_memory_proxy_stage_cap","phase_guard"],"component_delta_explanation":"C10-specific guard lowers generic proxy/result-after-rerating rows unless issuer-level order/customer conversion and utilization/margin bridge are both present. It keeps direct clean-window scrubber/cleaning routes actionable.","MFE_90D_pct":24.79,"MAE_90D_pct":-13.52,"score_return_alignment_label":"positive_alignment","current_profile_verdict":"current_profile_4B_too_late"}
{"row_type":"case","case_id":"C10L223_CASE_03_064290","symbol":"064290","company_name":"인텍플러스","round":"R2","loop":"223","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE","fine_archetype_id":"C10_SCRUBBER_CHILLER_CONSUMABLE_AND_HBM_PROXY_TO_ORDER_CONVERSION_GUARD","case_type":"failed_rerating","positive_or_counterexample":"counterexample","best_trigger":"C10L223_TRIG_03_064290_Stage2","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"misaligned_or_counterexample","current_profile_verdict":"current_profile_false_positive","price_source":"Songdaiki/stock-web","notes":"Qualification/test-proxy text was not enough; the entry began at the observed 180D peak and then fell sharply."}
{"row_type":"trigger","trigger_id":"C10L223_TRIG_03_064290_Stage2","case_id":"C10L223_CASE_03_064290","symbol":"064290","company_name":"인텍플러스","round":"R2","loop":"223","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE","fine_archetype_id":"C10_SCRUBBER_CHILLER_CONSUMABLE_AND_HBM_PROXY_TO_ORDER_CONVERSION_GUARD","sector":"semiconductor_equipment_parts_memory_recovery","primary_archetype":"memory_equipment_cycle","loop_objective":"counterexample_mining; residual_false_positive_mining; stage2_required_bridge_stress_test; direct_url_proxy_mfe_mae_repair; 4B_non_price_requirement_stress_test; canonical_archetype_compression","trigger_type":"Stage2","trigger_date":"2024-07-16","evidence_available_at_that_date":"HBM/2.5D 패키징 검사 장비 추가 수주 기대와 글로벌 파운드리 퀄리티 테스트 통과 기대가 있었지만, 1Q 손실과 2Q 컨센서스 하회 전망이 병존","evidence_source":"https://www.dailyinvest.kr/news/articleView.html?idxno=59633","stage2_evidence_fields":["public_event_or_disclosure","customer_or_order_quality"],"stage3_evidence_fields":[],"stage4b_evidence_fields":["margin_or_backlog_slowdown","price_only_local_peak"],"stage4c_evidence_fields":["qualification_failure"],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/064/064290/2024.csv","profile_path":"atlas/symbol_profiles/064/064290.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","entry_date":"2024-07-17","entry_price":20450.0,"MFE_30D_pct":5.62,"MFE_90D_pct":5.62,"MFE_180D_pct":5.62,"MFE_1Y_pct":5.62,"MFE_2Y_pct":null,"MAE_30D_pct":-27.58,"MAE_90D_pct":-54.91,"MAE_180D_pct":-60.98,"MAE_1Y_pct":-60.98,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-07-17","peak_price":21600.0,"drawdown_after_peak_pct":-63.06,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":null,"four_b_full_window_peak_proximity":null,"four_b_timing_verdict":"local_4b_watch_needed","four_b_evidence_type":["price_only","positioning_overheat"],"four_c_protection_label":"thesis_break_watch_only","trigger_outcome_label":"inspection_equipment_customer_test_proxy_without_conversion_counterexample","current_profile_verdict":"current_profile_false_positive","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE:064290:2024-07-17","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"C10L223_CASE_03_064290","trigger_id":"C10L223_TRIG_03_064290_Stage2","symbol":"064290","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE","raw_component_scores_before":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":0,"revision_score":0,"relative_strength_score":0,"customer_quality_score":14,"policy_or_regulatory_score":4,"valuation_repricing_score":10,"execution_risk_score":6,"legal_or_contract_risk_score":2,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_before":46.7,"stage_label_before":"Stage2","raw_component_scores_after":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":0,"revision_score":0,"relative_strength_score":0,"customer_quality_score":16,"policy_or_regulatory_score":3,"valuation_repricing_score":5,"execution_risk_score":12,"legal_or_contract_risk_score":8,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_after":40.2,"stage_label_after":"Watch","changed_components":["order_conversion_freshness_ladder","generic_memory_proxy_stage_cap","phase_guard"],"component_delta_explanation":"C10-specific guard lowers generic proxy/result-after-rerating rows unless issuer-level order/customer conversion and utilization/margin bridge are both present. It keeps direct clean-window scrubber/cleaning routes actionable.","MFE_90D_pct":5.62,"MAE_90D_pct":-54.91,"score_return_alignment_label":"counterexample_alignment","current_profile_verdict":"current_profile_false_positive"}
{"row_type":"case","case_id":"C10L223_CASE_04_074600","symbol":"074600","company_name":"원익QnC","round":"R2","loop":"223","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE","fine_archetype_id":"C10_SCRUBBER_CHILLER_CONSUMABLE_AND_HBM_PROXY_TO_ORDER_CONVERSION_GUARD","case_type":"failed_rerating","positive_or_counterexample":"counterexample","best_trigger":"C10L223_TRIG_04_074600_Stage2","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"misaligned_or_counterexample","current_profile_verdict":"current_profile_false_positive","price_source":"Songdaiki/stock-web","notes":"Utilization proxy and non-memory expansion were too indirect for C10 Green; downside exceeded the modest upside."}
{"row_type":"trigger","trigger_id":"C10L223_TRIG_04_074600_Stage2","case_id":"C10L223_CASE_04_074600","symbol":"074600","company_name":"원익QnC","round":"R2","loop":"223","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE","fine_archetype_id":"C10_SCRUBBER_CHILLER_CONSUMABLE_AND_HBM_PROXY_TO_ORDER_CONVERSION_GUARD","sector":"semiconductor_equipment_parts_memory_recovery","primary_archetype":"memory_equipment_cycle","loop_objective":"counterexample_mining; residual_false_positive_mining; stage2_required_bridge_stress_test; direct_url_proxy_mfe_mae_repair; 4B_non_price_requirement_stress_test; canonical_archetype_compression","trigger_type":"Stage2","trigger_date":"2024-10-23","evidence_available_at_that_date":"쿼츠 하반기 가동률 80~85% 추정, 비메모리 진입 확대와 2025년 쿼츠 매출 증가 기대","evidence_source":"https://www.thevaluenews.co.kr/news/186129","stage2_evidence_fields":["public_event_or_disclosure","capacity_or_volume_route"],"stage3_evidence_fields":["financial_visibility"],"stage4b_evidence_fields":["price_only_local_peak","margin_or_backlog_slowdown"],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/074/074600/2024.csv","profile_path":"atlas/symbol_profiles/074/074600.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","entry_date":"2024-10-24","entry_price":23700.0,"MFE_30D_pct":4.64,"MFE_90D_pct":4.64,"MFE_180D_pct":4.64,"MFE_1Y_pct":17.51,"MFE_2Y_pct":null,"MAE_30D_pct":-24.98,"MAE_90D_pct":-29.62,"MAE_180D_pct":-35.65,"MAE_1Y_pct":-35.65,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-11-06","peak_price":24800.0,"drawdown_after_peak_pct":-38.51,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":null,"four_b_full_window_peak_proximity":null,"four_b_timing_verdict":"local_4b_watch_needed","four_b_evidence_type":["price_only","positioning_overheat"],"four_c_protection_label":"thesis_break_watch_only","trigger_outcome_label":"quartz_utilization_proxy_after_rerating_counterexample","current_profile_verdict":"current_profile_false_positive","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE:074600:2024-10-24","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"C10L223_CASE_04_074600","trigger_id":"C10L223_TRIG_04_074600_Stage2","symbol":"074600","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE","raw_component_scores_before":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":0,"revision_score":12,"relative_strength_score":10,"customer_quality_score":0,"policy_or_regulatory_score":4,"valuation_repricing_score":10,"execution_risk_score":6,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_before":55.4,"stage_label_before":"Stage2","raw_component_scores_after":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":0,"revision_score":10,"relative_strength_score":8,"customer_quality_score":0,"policy_or_regulatory_score":3,"valuation_repricing_score":5,"execution_risk_score":12,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_after":46.6,"stage_label_after":"Stage2","changed_components":["order_conversion_freshness_ladder","generic_memory_proxy_stage_cap","phase_guard"],"component_delta_explanation":"C10-specific guard lowers generic proxy/result-after-rerating rows unless issuer-level order/customer conversion and utilization/margin bridge are both present. It keeps direct clean-window scrubber/cleaning routes actionable.","MFE_90D_pct":4.64,"MAE_90D_pct":-29.62,"score_return_alignment_label":"counterexample_alignment","current_profile_verdict":"current_profile_false_positive"}
{"row_type":"case","case_id":"C10L223_CASE_05_183300","symbol":"183300","company_name":"코미코","round":"R2","loop":"223","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE","fine_archetype_id":"C10_SCRUBBER_CHILLER_CONSUMABLE_AND_HBM_PROXY_TO_ORDER_CONVERSION_GUARD","case_type":"structural_success","positive_or_counterexample":"positive","best_trigger":"C10L223_TRIG_05_183300_Stage2Actionable","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"aligned","current_profile_verdict":"current_profile_correct","price_source":"Songdaiki/stock-web","notes":"Utilization-sensitive cleaning/coating route worked well before a later peak, showing direct utilization bridge matters."}
{"row_type":"trigger","trigger_id":"C10L223_TRIG_05_183300_Stage2Actionable","case_id":"C10L223_CASE_05_183300","symbol":"183300","company_name":"코미코","round":"R2","loop":"223","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE","fine_archetype_id":"C10_SCRUBBER_CHILLER_CONSUMABLE_AND_HBM_PROXY_TO_ORDER_CONVERSION_GUARD","sector":"semiconductor_equipment_parts_memory_recovery","primary_archetype":"memory_equipment_cycle","loop_objective":"counterexample_mining; residual_false_positive_mining; stage2_required_bridge_stress_test; direct_url_proxy_mfe_mae_repair; 4B_non_price_requirement_stress_test; canonical_archetype_compression","trigger_type":"Stage2-Actionable","trigger_date":"2023-11-30","evidence_available_at_that_date":"메모리 반도체 가동률 회복과 해외법인 손익 개선 기대가 세정·코팅 본업 회복의 early route로 제시","evidence_source":"https://www.dailyinvest.kr/news/articleView.html?idxno=55680","stage2_evidence_fields":["capacity_or_volume_route","customer_or_order_quality","early_revision_signal"],"stage3_evidence_fields":["margin_bridge","financial_visibility"],"stage4b_evidence_fields":["positioning_overheat"],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/183/183300/2023.csv","profile_path":"atlas/symbol_profiles/183/183300.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","entry_date":"2023-12-01","entry_price":60200.0,"MFE_30D_pct":14.45,"MFE_90D_pct":42.86,"MFE_180D_pct":63.46,"MFE_1Y_pct":63.46,"MFE_2Y_pct":null,"MAE_30D_pct":-4.98,"MAE_90D_pct":-6.98,"MAE_180D_pct":-6.98,"MAE_1Y_pct":-47.59,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-05-16","peak_price":98400.0,"drawdown_after_peak_pct":-39.74,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":null,"four_b_full_window_peak_proximity":null,"four_b_timing_verdict":"not_primary_trigger","four_b_evidence_type":[],"four_c_protection_label":"not_applicable","trigger_outcome_label":"memory_utilization_cleaning_coating_recovery_direct_route_positive","current_profile_verdict":"current_profile_correct","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE:183300:2023-12-01","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"C10L223_CASE_05_183300","trigger_id":"C10L223_TRIG_05_183300_Stage2Actionable","symbol":"183300","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE","raw_component_scores_before":{"contract_score":10,"backlog_visibility_score":0,"margin_bridge_score":13,"revision_score":12,"relative_strength_score":10,"customer_quality_score":14,"policy_or_regulatory_score":0,"valuation_repricing_score":7,"execution_risk_score":3,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_before":90.5,"stage_label_before":"Stage3-Green","raw_component_scores_after":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":14,"revision_score":10,"relative_strength_score":8,"customer_quality_score":16,"policy_or_regulatory_score":0,"valuation_repricing_score":7,"execution_risk_score":3,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_after":77.5,"stage_label_after":"Stage3-Yellow","changed_components":["order_conversion_freshness_ladder","generic_memory_proxy_stage_cap","phase_guard"],"component_delta_explanation":"C10-specific guard lowers generic proxy/result-after-rerating rows unless issuer-level order/customer conversion and utilization/margin bridge are both present. It keeps direct clean-window scrubber/cleaning routes actionable.","MFE_90D_pct":42.86,"MAE_90D_pct":-6.98,"score_return_alignment_label":"positive_alignment","current_profile_verdict":"current_profile_correct"}
{"row_type":"case","case_id":"C10L223_CASE_06_083450","symbol":"083450","company_name":"GST","round":"R2","loop":"223","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE","fine_archetype_id":"C10_SCRUBBER_CHILLER_CONSUMABLE_AND_HBM_PROXY_TO_ORDER_CONVERSION_GUARD","case_type":"structural_success","positive_or_counterexample":"positive","best_trigger":"C10L223_TRIG_06_083450_Stage3Yellow","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"aligned","current_profile_verdict":"current_profile_too_late","price_source":"Songdaiki/stock-web","notes":"Unlike earlier 2023 GST window, post-split 2024-11 trigger is clean and showed strong MFE with nearly no MAE, repairing a prior data-quality trap."}
{"row_type":"trigger","trigger_id":"C10L223_TRIG_06_083450_Stage3Yellow","case_id":"C10L223_CASE_06_083450","symbol":"083450","company_name":"GST","round":"R2","loop":"223","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE","fine_archetype_id":"C10_SCRUBBER_CHILLER_CONSUMABLE_AND_HBM_PROXY_TO_ORDER_CONVERSION_GUARD","sector":"semiconductor_equipment_parts_memory_recovery","primary_archetype":"memory_equipment_cycle","loop_objective":"counterexample_mining; residual_false_positive_mining; stage2_required_bridge_stress_test; direct_url_proxy_mfe_mae_repair; 4B_non_price_requirement_stress_test; canonical_archetype_compression","trigger_type":"Stage3-Yellow","trigger_date":"2024-11-28","evidence_available_at_that_date":"2024년 3분기 누적 매출 반등과 스크러버·칠러 기술/시장지위 확인; stock count split 이후 clean window로 재검증","evidence_source":"https://w4.kirs.or.kr/download/research/241128_%EA%B8%B0%EA%B3%84%C2%B7%EC%9E%A5%EB%B9%84_GST%28083450%29_%EB%B0%98%EB%8F%84%EC%B2%B4%20%EC%8A%A4%ED%81%AC%EB%9F%AC%EB%B2%84%20%EC%A0%9C%EC%A1%B0%20%EA%B8%B0%EC%88%A0%20%EC%84%A0%EB%8F%84%20%EA%B8%B0%EC%97%85_NICE%EB%94%94%EC%95%A4%EB%B9%84_%EC%88%98%EC%A0%95%EB%B3%B8.pdf","stage2_evidence_fields":["public_event_or_disclosure","capacity_or_volume_route","customer_or_order_quality"],"stage3_evidence_fields":["margin_bridge","financial_visibility","multiple_public_sources"],"stage4b_evidence_fields":["positioning_overheat"],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/083/083450/2024.csv","profile_path":"atlas/symbol_profiles/083/083450.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","entry_date":"2024-11-29","entry_price":14000.0,"MFE_30D_pct":34.64,"MFE_90D_pct":66.79,"MFE_180D_pct":66.79,"MFE_1Y_pct":121.79,"MFE_2Y_pct":null,"MAE_30D_pct":-0.29,"MAE_90D_pct":-0.29,"MAE_180D_pct":-0.29,"MAE_1Y_pct":-0.29,"below_entry_price_flag_30D":false,"below_entry_price_flag_90D":false,"peak_date":"2025-02-24","peak_price":23350.0,"drawdown_after_peak_pct":-34.18,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":null,"four_b_full_window_peak_proximity":null,"four_b_timing_verdict":"not_primary_trigger","four_b_evidence_type":[],"four_c_protection_label":"not_applicable","trigger_outcome_label":"scrubber_chiller_result_rebound_clean_post_split_window_positive","current_profile_verdict":"current_profile_too_late","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE:083450:2024-11-29","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"C10L223_CASE_06_083450","trigger_id":"C10L223_TRIG_06_083450_Stage3Yellow","symbol":"083450","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE","raw_component_scores_before":{"contract_score":10,"backlog_visibility_score":0,"margin_bridge_score":13,"revision_score":12,"relative_strength_score":10,"customer_quality_score":14,"policy_or_regulatory_score":4,"valuation_repricing_score":7,"execution_risk_score":3,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_before":94.5,"stage_label_before":"Stage3-Green","raw_component_scores_after":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":14,"revision_score":10,"relative_strength_score":8,"customer_quality_score":16,"policy_or_regulatory_score":3,"valuation_repricing_score":7,"execution_risk_score":3,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_after":80.5,"stage_label_after":"Stage3-Yellow","changed_components":["order_conversion_freshness_ladder","generic_memory_proxy_stage_cap","phase_guard"],"component_delta_explanation":"C10-specific guard lowers generic proxy/result-after-rerating rows unless issuer-level order/customer conversion and utilization/margin bridge are both present. It keeps direct clean-window scrubber/cleaning routes actionable.","MFE_90D_pct":66.79,"MAE_90D_pct":-0.29,"score_return_alignment_label":"positive_alignment","current_profile_verdict":"current_profile_too_late"}
{"row_type":"case","case_id":"C10L223_CASE_07_101160","symbol":"101160","company_name":"월덱스","round":"R2","loop":"223","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE","fine_archetype_id":"C10_SCRUBBER_CHILLER_CONSUMABLE_AND_HBM_PROXY_TO_ORDER_CONVERSION_GUARD","case_type":"failed_rerating","positive_or_counterexample":"counterexample","best_trigger":"C10L223_TRIG_07_101160_Stage2","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"misaligned_or_counterexample","current_profile_verdict":"current_profile_false_positive","price_source":"Songdaiki/stock-web","notes":"Aftermarket/memory exposure alone gave only small upside and then meaningful drawdown; proxy needs issuer-level order/utilization conversion."}
{"row_type":"trigger","trigger_id":"C10L223_TRIG_07_101160_Stage2","case_id":"C10L223_CASE_07_101160","symbol":"101160","company_name":"월덱스","round":"R2","loop":"223","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE","fine_archetype_id":"C10_SCRUBBER_CHILLER_CONSUMABLE_AND_HBM_PROXY_TO_ORDER_CONVERSION_GUARD","sector":"semiconductor_equipment_parts_memory_recovery","primary_archetype":"memory_equipment_cycle","loop_objective":"counterexample_mining; residual_false_positive_mining; stage2_required_bridge_stress_test; direct_url_proxy_mfe_mae_repair; 4B_non_price_requirement_stress_test; canonical_archetype_compression","trigger_type":"Stage2","trigger_date":"2024-02-11","evidence_available_at_that_date":"반도체 시장 회복과 애프터마켓 채택률 상승, 메모리향 매출 비중 및 NAND 시황 연동성 확인","evidence_source":"https://www.newsprime.co.kr/news/article/?no=627869","stage2_evidence_fields":["public_event_or_disclosure","capacity_or_volume_route"],"stage3_evidence_fields":[],"stage4b_evidence_fields":["price_only_local_peak","margin_or_backlog_slowdown"],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/101/101160/2024.csv","profile_path":"atlas/symbol_profiles/101/101160.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","entry_date":"2024-02-13","entry_price":24000.0,"MFE_30D_pct":7.08,"MFE_90D_pct":8.96,"MFE_180D_pct":8.96,"MFE_1Y_pct":null,"MFE_2Y_pct":null,"MAE_30D_pct":-7.08,"MAE_90D_pct":-11.25,"MAE_180D_pct":-23.62,"MAE_1Y_pct":null,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-04-02","peak_price":26150.0,"drawdown_after_peak_pct":-29.9,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":null,"four_b_full_window_peak_proximity":null,"four_b_timing_verdict":"local_4b_watch_needed","four_b_evidence_type":["price_only","positioning_overheat"],"four_c_protection_label":"thesis_break_watch_only","trigger_outcome_label":"consumable_aftermarket_memory_recovery_proxy_without_order_conversion_counterexample","current_profile_verdict":"current_profile_false_positive","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE:101160:2024-02-13","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"C10L223_CASE_07_101160","trigger_id":"C10L223_TRIG_07_101160_Stage2","symbol":"101160","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE","raw_component_scores_before":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":0,"revision_score":0,"relative_strength_score":10,"customer_quality_score":0,"policy_or_regulatory_score":4,"valuation_repricing_score":10,"execution_risk_score":6,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_before":43.4,"stage_label_before":"Watch","raw_component_scores_after":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":0,"revision_score":0,"relative_strength_score":8,"customer_quality_score":0,"policy_or_regulatory_score":3,"valuation_repricing_score":5,"execution_risk_score":12,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_after":36.6,"stage_label_after":"Watch","changed_components":["order_conversion_freshness_ladder","generic_memory_proxy_stage_cap","phase_guard"],"component_delta_explanation":"C10-specific guard lowers generic proxy/result-after-rerating rows unless issuer-level order/customer conversion and utilization/margin bridge are both present. It keeps direct clean-window scrubber/cleaning routes actionable.","MFE_90D_pct":8.96,"MAE_90D_pct":-11.25,"score_return_alignment_label":"counterexample_alignment","current_profile_verdict":"current_profile_false_positive"}
{"row_type":"case","case_id":"C10L223_CASE_08_272110","symbol":"272110","company_name":"케이엔제이","round":"R2","loop":"223","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE","fine_archetype_id":"C10_SCRUBBER_CHILLER_CONSUMABLE_AND_HBM_PROXY_TO_ORDER_CONVERSION_GUARD","case_type":"failed_rerating","positive_or_counterexample":"counterexample","best_trigger":"C10L223_TRIG_08_272110_Stage2Actionable","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"misaligned_or_counterexample","current_profile_verdict":"current_profile_false_positive","price_source":"Songdaiki/stock-web","notes":"Direct memory utilization route was plausible, but the price path was a high-MAE case; conversion evidence should not ignore local phase."}
{"row_type":"trigger","trigger_id":"C10L223_TRIG_08_272110_Stage2Actionable","case_id":"C10L223_CASE_08_272110","symbol":"272110","company_name":"케이엔제이","round":"R2","loop":"223","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE","fine_archetype_id":"C10_SCRUBBER_CHILLER_CONSUMABLE_AND_HBM_PROXY_TO_ORDER_CONVERSION_GUARD","sector":"semiconductor_equipment_parts_memory_recovery","primary_archetype":"memory_equipment_cycle","loop_objective":"counterexample_mining; residual_false_positive_mining; stage2_required_bridge_stress_test; direct_url_proxy_mfe_mae_repair; 4B_non_price_requirement_stress_test; canonical_archetype_compression","trigger_type":"Stage2-Actionable","trigger_date":"2024-04-19","evidence_available_at_that_date":"메모리 반도체 가동률 회복이 SiC Focus Ring 부품 실적 성장으로 이어진다는 route가 제시","evidence_source":"https://www.bondweb.co.kr/_research/downloadPage.asp?gn=1&number=765248","stage2_evidence_fields":["customer_or_order_quality","capacity_or_volume_route"],"stage3_evidence_fields":["financial_visibility"],"stage4b_evidence_fields":["positioning_overheat","price_only_local_peak"],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/272/272110/2024.csv","profile_path":"atlas/symbol_profiles/272/272110.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","entry_date":"2024-04-22","entry_price":18910.0,"MFE_30D_pct":10.26,"MFE_90D_pct":22.42,"MFE_180D_pct":22.42,"MFE_1Y_pct":22.42,"MFE_2Y_pct":null,"MAE_30D_pct":-3.01,"MAE_90D_pct":-19.35,"MAE_180D_pct":-38.92,"MAE_1Y_pct":-38.92,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-06-14","peak_price":23150.0,"drawdown_after_peak_pct":-50.11,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":null,"four_b_full_window_peak_proximity":null,"four_b_timing_verdict":"local_4b_watch_needed","four_b_evidence_type":["price_only","positioning_overheat"],"four_c_protection_label":"thesis_break_watch_only","trigger_outcome_label":"sic_focus_ring_memory_utilization_proxy_high_mae_counterexample","current_profile_verdict":"current_profile_false_positive","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE:272110:2024-04-22","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"C10L223_CASE_08_272110","trigger_id":"C10L223_TRIG_08_272110_Stage2Actionable","symbol":"272110","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE","raw_component_scores_before":{"contract_score":10,"backlog_visibility_score":0,"margin_bridge_score":0,"revision_score":12,"relative_strength_score":10,"customer_quality_score":14,"policy_or_regulatory_score":0,"valuation_repricing_score":10,"execution_risk_score":6,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_before":75.4,"stage_label_before":"Stage3-Yellow","raw_component_scores_after":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":0,"revision_score":10,"relative_strength_score":8,"customer_quality_score":16,"policy_or_regulatory_score":0,"valuation_repricing_score":5,"execution_risk_score":12,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_after":59.6,"stage_label_after":"Stage2","changed_components":["order_conversion_freshness_ladder","generic_memory_proxy_stage_cap","phase_guard"],"component_delta_explanation":"C10-specific guard lowers generic proxy/result-after-rerating rows unless issuer-level order/customer conversion and utilization/margin bridge are both present. It keeps direct clean-window scrubber/cleaning routes actionable.","MFE_90D_pct":22.42,"MAE_90D_pct":-19.35,"score_return_alignment_label":"counterexample_alignment","current_profile_verdict":"current_profile_false_positive"}
{"row_type":"residual_contribution","round":"R2","loop":"223","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE","new_independent_case_count":8,"reused_case_count":0,"new_symbol_count":8,"new_trigger_family_count":8,"tested_existing_calibrated_axes":["stage2_required_bridge","local_4b_watch_guard","full_4b_requires_non_price_evidence","hard_4c_thesis_break_routes_to_4c"],"residual_error_types_found":["generic_memory_proxy_false_positive","result_after_rerating_green_trap","high_mae_live_route_not_hard4c","clean_post_split_repair_needed"],"loop_contribution_label":"canonical_archetype_rule_candidate","do_not_propose_new_weight_delta":false}
```

## Batch Ingest Self-Audit

```text
expected_v12_result_file: true
filename_pattern_pass: true
metadata_filename_consistency: pass
jsonl_trigger_row_count: 8
calibration_usable_trigger_count: 8
representative_trigger_count: 8
new_weight_evidence_candidate_count: 8
guardrail_candidate_count: 5
narrative_only_or_rejected_count: 0
rows_missing_required_mfe_mae: 0
rows_missing_entry_price_or_date: 0
rows_with_noncanonical_trigger_type: 0
rows_with_compact_mfe_mae_alias_only: 0
ready_for_batch_ingest: true
```

## 26. Deferred Coding Agent Handoff Prompt

### Purpose
You are now in the repository implementation phase. The attached Markdown files are v12 post-calibrated residual research outputs produced using the Songdaiki/stock-web OHLC atlas. These MDs are not live candidate research. They are historical calibration research designed to extend the already-applied e2r_2_1_stock_web_calibrated profile. Do not blindly apply every shadow row. Ingest the machine-readable rows and update the sector/canonical-archetype calibration ledger.

### Price source context
- Primary historical price source used by the research MD: Songdaiki/stock-web.
- Price basis: tradable_raw.
- Price adjustment status: raw_unadjusted_marcap.
- Price shard pattern: atlas/ohlcv_tradable_by_symbol_year/<prefix>/<ticker>/<year>.csv.
- Symbol profile pattern: atlas/symbol_profiles/<prefix>/<ticker>.json.

### Rules
- Use only calibration_usable=true rows for quantitative calibration.
- Do not count reused cases as new independent evidence unless independent_evidence_weight > 0.
- Do not treat schema_rematerialization_only or duplicate_low_value_loop as new evidence.
- Do not apply global deltas unless multiple large_sector_id values support the same direction.
- Prefer sector_specific or canonical_archetype_specific shadow profiles.
- Positive score promotion requires non-price evidence and clean 180D MFE/MAE.
- 4B rows are overlay/risk calibration only.
- 4C rows are thesis-break/protection calibration only.
- price-only rows cannot promote Stage2/Stage3.
- If a v12 MD weakens an already applied axis, log it as residual counterexample rather than immediately reverting.
- Production scoring must not change unless the user explicitly asks for another promotion batch.

### Expected repository tasks
1. Parse case / trigger / score_simulation / shadow_weight / residual_contribution rows.
2. Validate stock-web price source fields.
3. Validate large_sector_id and canonical_archetype_id.
4. Validate novelty and reuse fields.
5. Deduplicate same_entry_group_id and reused cases.
6. Aggregate by large_sector_id and canonical_archetype_id.
7. Update sector_shadow_profile and archetype_shadow_profile only.
8. Preserve global calibrated profile unless explicitly promoted.
9. Report new independent cases, counterexamples, and residual error types.
10. Add tests that duplicate low-value loops cannot change weights.

### Expected output
- Concise implementation summary.
- Rows accepted/rejected.
- New sector/canonical archetype coverage.
- Existing axis strengthened/weakened/kept.
- No investment recommendation language.

## 27. Next Round State

```text
completed_round = R2
completed_loop = 223
selection_basis = docs/core/V12_Research_No_Repeat_Index.md
selected_priority_bucket = Priority 1 C10 quality reinforcement + Priority 0 direct URL/proxy/MFE-MAE repair
next_recommended_archetypes = C15 spread freshness rows; C01/C05 direct FCF or cash-conversion rows; C13 strict-new utilization/ex-credit rows; C31 non-semi/battery awarded-cashflow rows; R13 only for genuinely new taxonomy compression
round_schedule_status = coverage_index_selected
round_sector_consistency = pass
```

## 28. Source Notes

- `docs/core/e2r_v12_prompt_round_scheduler_corrected.txt` requires standalone historical calibration MD, Stock-Web actual OHLC, complete 30/90/180D MFE/MAE, JSONL trigger rows, and standard filename.
- `docs/core/V12_Research_No_Repeat_Index.md` reports representative rows above 80 for all C01~C32 and directs the next runs toward URL/proxy/MFE-MAE quality repair and Priority 1 balance repair.
- `Songdaiki/stock-web` manifest max date is 2026-02-20; all entries here keep 180D windows within that atlas boundary.
