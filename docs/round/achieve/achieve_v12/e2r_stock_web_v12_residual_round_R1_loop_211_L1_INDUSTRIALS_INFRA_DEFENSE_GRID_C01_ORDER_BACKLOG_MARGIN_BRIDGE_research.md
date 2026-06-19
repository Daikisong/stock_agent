# E2R Stock-Web Historical Calibration / Sector-Archetype Residual Research Round

## 0. Research Metadata

| field | value |
|---|---|
| selected_round | `R1` |
| selected_loop | `211` |
| selection_basis | `docs/core/V12_Research_No_Repeat_Index.md` |
| selected_priority_bucket | `Priority 1 C01 balance-quality reinforcement + Priority 0 direct URL/proxy/MFE-MAE repair` |
| round_schedule_status | `coverage_index_selected` |
| round_sector_consistency | `pass` |
| large_sector_id | `L1_INDUSTRIALS_INFRA_DEFENSE_GRID` |
| canonical_archetype_id | `C01_ORDER_BACKLOG_MARGIN_BRIDGE` |
| fine_archetype_id | `C01_SHIPBUILDING_BACKLOG_MARGIN_CASH_DIRECT_URL_REPAIR` |
| loop_objective | `counterexample_mining; residual_false_positive_mining; residual_missed_structural_mining; direct_url_proxy_mfe_mae_repair; 4B_non_price_requirement_stress_test; 4C_thesis_break_timing_test; canonical_archetype_compression` |
| price_source | `Songdaiki/stock-web` |
| stock_web_manifest_max_date | `2026-02-20` |
| production_scoring_changed | `false` |
| shadow_weight_only | `true` |
| handoff_prompt_embedded | `true` |
| handoff_prompt_executed_now | `false` |

This loop adds **7 new independent trigger cases**, **3 counterexamples/guardrails**, and **3 residual errors** for `L1_INDUSTRIALS_INFRA_DEFENSE_GRID/C01_ORDER_BACKLOG_MARGIN_BRIDGE`. It deliberately does not repeat the immediately prior C01 loop's supplier-only set as a pure reprint; instead it mixes two less-covered/new symbols (`014940`, `077970`) with reused large shipbuilder symbols on **new trigger families**: supplier price-revision bridge, engine customer-route bridge, early versus late Mipo confirmation, engine backlog phase risk, and major-shipyard result Green timing.

## 1. Current Calibrated Profile Assumption

| item | assumption |
|---|---|
| current_default_profile_proxy | `e2r_2_1_stock_web_calibrated_proxy` |
| rollback_reference_profile_id | `e2r_2_0_baseline_reference` |
| active axes stress-tested | `stage2_required_bridge`, `stage2_actionable_evidence_bonus`, `stage3_green_total_min`, `stage3_green_revision_min`, `full_4b_requires_non_price_evidence`, `hard_4c_thesis_break_routes_to_4c` |
| production change | none |

The profile already blocks pure price-only promotion. The residual question here is narrower: **when does C01 backlog/order evidence become earnings-quality evidence, and when is a good-looking result actually a late-cycle Green trap?** The mechanical analogy is a shipyard slipway: a backlog is the hull on the rails, but margin and cash conversion are the water under it. Without that water, the hull may look finished but still cannot sail.

## 2. Round / Large Sector / Canonical Archetype Scope

| scope field | value |
|---|---|
| selected_round | `R1` |
| large_sector_id | `L1_INDUSTRIALS_INFRA_DEFENSE_GRID` |
| canonical_archetype_id | `C01_ORDER_BACKLOG_MARGIN_BRIDGE` |
| fine_archetype_id | `C01_SHIPBUILDING_BACKLOG_MARGIN_CASH_DIRECT_URL_REPAIR` |
| valid mapping | `C01~C05 -> R1 / L1_INDUSTRIALS_INFRA_DEFENSE_GRID` |
| invalid_round_sector_pair | `false` |

## 3. Previous Coverage / Duplicate Avoidance Check

| check | result |
|---|---|
| NO-REPEAT index status | all C01~C32 are above 80 rows; quality repair phase |
| Priority 0 repair attached | direct URL/proxy/MFE-MAE completeness |
| Priority 1 target used | `C01_ORDER_BACKLOG_MARGIN_BRIDGE` |
| exact duplicate key avoided | `canonical_archetype_id + symbol + trigger_type + entry_date` |
| same_archetype_new_symbol_count | `2` |
| same_archetype_new_trigger_family_count | `7` |
| reused_case_count | `0` |
| reused symbol note | large shipbuilder symbols are reused only with different trigger dates/families; exact entry keys are new |

## 4. Stock-Web OHLC Input / Price Source Validation

| field | value |
|---|---|
| source_name | `FinanceData/marcap` |
| price_data_source | `Songdaiki/stock-web` |
| source_repo_url | `https://github.com/Songdaiki/stock-web` |
| price_basis | `tradable_raw` |
| price_adjustment_status | `raw_unadjusted_marcap` |
| calibration_shard_root | `atlas/ohlcv_tradable_by_symbol_year` |
| raw_shard_root | `atlas/ohlcv_raw_by_symbol_year` |
| schema_path | `atlas/schema.json` |
| universe_path | `atlas/universe/all_symbols.csv` |
| manifest_max_date | `2026-02-20` |
| MFE/MAE formula | max high / min low from entry date through 30, 90, 180 tradable rows divided by entry close |

## 5. Historical Eligibility Gate

|symbol|profile_path|entry_date|forward rows observed|CA window|calibration_usable|block_reasons|
|---|---|---|---|---|---|---|
|014940|atlas/symbol_profiles/014/014940.json|2024-06-14|409|clean_180D_window|true|[]|
|077970|atlas/symbol_profiles/077/077970.json|2024-05-17|428|clean_180D_window|true|[]|
|010620|atlas/symbol_profiles/010/010620.json|2024-04-29|383|clean_180D_window|true|[]|
|010620|atlas/symbol_profiles/010/010620.json|2024-07-29|322|clean_180D_window|true|[]|
|082740|atlas/symbol_profiles/082/082740.json|2025-02-17|214|clean_180D_window|true|[]|
|329180|atlas/symbol_profiles/329/329180.json|2024-07-29|345|clean_180D_window|true|[]|
|010140|atlas/symbol_profiles/010/010140.json|2025-02-07|220|clean_180D_window|true|[]|


All representative trigger rows have `MFE_30D_pct`, `MFE_90D_pct`, `MFE_180D_pct`, `MAE_30D_pct`, `MAE_90D_pct`, and `MAE_180D_pct`. Share-count stability was checked from the `s` column over entry~D+180; all selected rows stayed below the corporate-action blocking threshold.

## 6. Canonical Archetype Compression Map

| evidence family | compresses to | rule use |
|---|---|---|
| supplier price revision and shipbuilding equipment demand | `C01_ORDER_BACKLOG_MARGIN_BRIDGE` | treat as C01 only when customer route and margin/price-revision bridge are issuer-specific |
| engine supplier customer mix / backlog | `C01_ORDER_BACKLOG_MARGIN_BRIDGE` | allow Stage2-Actionable, but Green requires backlog-to-margin conversion |
| early orderbook to profit-turnaround bridge | `C01_ORDER_BACKLOG_MARGIN_BRIDGE` | positive when loss-burnoff mechanism is explicit |
| late profit confirmation after rerating | `C01_ORDER_BACKLOG_MARGIN_BRIDGE` | cap Green if entry phase has high-MAE risk |
| major shipbuilder result / backlog | `C01_ORDER_BACKLOG_MARGIN_BRIDGE` | split result quality, one-off cost, offshore execution risk, and phase |

## 7. Case Selection Summary

|case_id|symbol|company|trigger_type|trigger_family|entry_date|entry_price|role|MFE90|MAE90|MFE180|MAE180|current_profile_verdict|
|---|---|---|---|---|---|---|---|---|---|---|---|---|
|C01-R1-L211-01|014940|오리엔탈정공|Stage2-Actionable|small_shipbuilding_equipment_price_revision_and_margin_conversion|2024-06-14|3,530.00|positive|41.5|-4.39|82.44|-9.21|current_profile_correct|
|C01-R1-L211-02|077970|STX엔진|Stage2-Actionable|engine_supplier_customer_mix_and_defense_civil_bridge|2024-05-17|13,840.00|positive|76.3|-6.94|99.78|-6.94|current_profile_correct|
|C01-R1-L211-03|010620|HD현대미포|Stage2-Actionable|mipo_early_orderbook_to_turnaround_bridge|2024-04-29|74,200.00|positive|65.5|-7.55|94.47|-7.55|current_profile_correct|
|C01-R1-L211-04|010620|HD현대미포|Stage3-Green|mipo_late_turnaround_report_green_high_mae_trap|2024-07-29|116,800.00|counterexample|11.99|-21.23|41.01|-21.23|current_profile_too_early|
|C01-R1-L211-05|082740|한화엔진|Stage3-Green|engine_backlog_good_but_entry_phase_high_mae|2025-02-17|25,750.00|counterexample|25.63|-22.33|109.32|-22.33|current_profile_too_early|
|C01-R1-L211-06|329180|HD현대중공업|Stage3-Green|major_shipbuilder_2q_result_green_but_offshore_cost_and_phase_mae|2024-07-29|208,000.00|counterexample|17.55|-18.8|95.19|-18.8|current_profile_too_early|
|C01-R1-L211-07|010140|삼성중공업|Stage3-Green|samsung_heavy_backlog_and_clean_margin_confirmation|2025-02-07|12,770.00|positive|45.26|-2.35|154.5|-2.35|current_profile_correct|


## 8. Positive vs Counterexample Balance

| bucket | count | symbols | interpretation |
|---|---:|---|---|
| positive structural / clean bridge | `4` | `014940`, `077970`, `010620` early, `010140` | direct customer/order/margin bridge was early enough or clean enough |
| counterexample / Green timing guard | `3` | `010620` late, `082740`, `329180` | good evidence existed, but Green at that phase carried high 30/90D MAE |
| 4B/4C guardrail path | `3` | `010620`, `082740`, `329180` | high MAE with live bridge should become watch/phase guard, not automatic thesis death |

## 9. Evidence Source Map

|symbol|company|trigger_date|entry rule date|source URL|summary|
|---|---|---|---|---|---|
|014940|오리엔탈정공|2024-06-13|2024-06-14|https://w4.kirs.or.kr/download/research/240613_%EA%B8%B0%EA%B3%84%EC%9E%A5%EB%B9%84_%EC%98%A4%EB%A6%AC%EC%97%94%ED%83%88%EC%A0%95%EA%B3%B5%28014940%29_%EC%84%A0%EB%B0%95%EC%9A%A9%20%ED%81%AC%EB%A0%88%EC%9D%B8%20%EB%B0%8F%20%EC%83%81%EB%B6%80%20%EA%B5%AC%EC%A1%B0%EB%AC%BC%20%EC%A0%9C%EC%A1%B0%20%EC%A0%84%EB%AC%B8%EA%B8%B0%EC%97%85_%EB%82%98%EC%9D%B4%EC%8A%A4%EB%94%94%EC%95%A4%EB%B9%84.pdf|KIRS/NICE D&B report dated 2024-06-13 links shipbuilding equipment demand with shipbuilding order flow and notes 1Q24 order-backlog unit-price revision effects. It is a direct issuer/sector report rather than a broker headline.|
|077970|STX엔진|2024-05-16|2024-05-17|https://kind.krx.co.kr/common/disclsviewer.do?acptno=20240516000707&docno=&method=search&viewerhost=|KRX/KIND quarterly report for STX Engine dated 2024-05-16 identifies Q1 revenue, key customers including 방위사업청 and Hanwha Aerospace, and operating segment context. The row tests whether C01 can admit engine-supply bridge rows without treating them as generic shipbuilding beta.|
|010620|HD현대미포|2024-04-26|2024-04-29|https://www.hanaw.com/download/research/FileServer/WEB/industry/enterprise/2024/04/25/HD_HM_240426_1Q24Re.pdf|Hana report dated 2024-04-26 says 1Q24 new orders reached USD 2.56bn, already 82.5% of annual target, and backlog rose sharply to USD 8.03bn by sales basis while old low-margin backlog was being cleared.|
|010620|HD현대미포|2024-07-26|2024-07-29|https://stock.pstatic.net/stock-research/company/61/20240726_company_271472000.pdf|Hi Investment report dated 2024-07-26 says HD Hyundai Mipo finally turned profitable after six consecutive quarterly losses and includes backlog trend. This was a stronger confirmation, but it came after local rerating and then suffered >20% MAE.|
|082740|한화엔진|2025-02-14|2025-02-17|https://www.hanwha-engine.com/attach/download/206b6f42-87a2-4646-8b50-b5a2a4e5de48|Hanwha Engine 2024 performance material shows backlog of KRW 3.3841tn at 2024-12-31 with ship engines at 96.3%. The bridge is real, but the 30/90D MAE was deep before later recovery.|
|329180|HD현대중공업|2024-07-26|2024-07-29|https://www.hanaw.com/download/research/FileServer/WEB/industry/enterprise/2024/07/25/HD_HHI_2Q24Re.pdf|Hana report dated 2024-07-26 says cost savings and FX helped, 1H orders reached USD 6.60bn or 69.2% of annual target, and sales-basis backlog was USD 33.5bn, while offshore remained weak with one-off advance-payment cost.|
|010140|삼성중공업|2025-02-06|2025-02-07|https://www.ibks.com/company/common/download.jsp?filename=20250206074137953_ko.pdf&filepath=%2Ffiles%2Ftradeinfo%2Fbusreport; https://home.imeritz.com/include/resource/research/WorkFlow/20250205102728702K_02.pdf|IBK and Meritz materials dated 2025-02-06 discuss 2024 operating-profit achievement, order backlog, and 2025 earnings expansion; Meritz cites 2024 year-end backlog of KRW 32.3tn, with Russian project caveat.|


## 10. Price Data Source Map

|symbol|shard|entry_date|O|H|L|C/entry|V|CA status|
|---|---|---|---|---|---|---|---|---|
|014940|atlas/ohlcv_tradable_by_symbol_year/014/014940/2024.csv|2024-06-14|3,455.00|3,575.00|3,425.00|3,530.00|153076|clean_180D_window|
|077970|atlas/ohlcv_tradable_by_symbol_year/077/077970/2024.csv|2024-05-17|14,440.00|14,580.00|13,490.00|13,840.00|149912|clean_180D_window|
|010620|atlas/ohlcv_tradable_by_symbol_year/010/010620/2024.csv|2024-04-29|74,400.00|74,900.00|73,100.00|74,200.00|276821|clean_180D_window|
|010620|atlas/ohlcv_tradable_by_symbol_year/010/010620/2024.csv|2024-07-29|113,300.00|117,900.00|111,800.00|116,800.00|502974|clean_180D_window|
|082740|atlas/ohlcv_tradable_by_symbol_year/082/082740/2025.csv|2025-02-17|24,500.00|27,450.00|23,900.00|25,750.00|9382582|clean_180D_window|
|329180|atlas/ohlcv_tradable_by_symbol_year/329/329180/2024.csv|2024-07-29|207,000.00|210,000.00|201,000.00|208,000.00|413038|clean_180D_window|
|010140|atlas/ohlcv_tradable_by_symbol_year/010/010140/2025.csv|2025-02-07|12,910.00|12,930.00|12,630.00|12,770.00|6918096|clean_180D_window|


## 11. Case-by-Case Trigger Grid

|symbol|Stage2 evidence|Stage3 evidence|4B evidence|4C evidence|current profile verdict|
|---|---|---|---|---|---|
|014940|public_event_or_disclosure, customer_or_order_quality, backlog_or_delivery_visibility|margin_bridge, financial_visibility|none|none|current_profile_correct|
|077970|public_event_or_disclosure, customer_or_order_quality, capacity_or_volume_route|financial_visibility|none|none|current_profile_correct|
|010620|public_event_or_disclosure, backlog_or_delivery_visibility, early_revision_signal|margin_bridge, financial_visibility|none|none|current_profile_correct|
|010620|public_event_or_disclosure, backlog_or_delivery_visibility|confirmed_revision, margin_bridge, multiple_public_sources|price_only_local_peak, positioning_overheat|none|current_profile_too_early|
|082740|public_event_or_disclosure, backlog_or_delivery_visibility, customer_or_order_quality|financial_visibility, margin_bridge|price_only_local_peak, positioning_overheat|none|current_profile_too_early|
|329180|public_event_or_disclosure, backlog_or_delivery_visibility, customer_or_order_quality|confirmed_revision, margin_bridge|margin_or_backlog_slowdown, price_only_local_peak|none|current_profile_too_early|
|010140|public_event_or_disclosure, backlog_or_delivery_visibility, customer_or_order_quality|confirmed_revision, margin_bridge, multiple_public_sources, financial_visibility|none|none|current_profile_correct|


## 12. Trigger-Level OHLC Backtest Tables

|symbol|entry_date|entry_price|MFE_30D_pct|MAE_30D_pct|MFE_90D_pct|MAE_90D_pct|MFE_180D_pct|MAE_180D_pct|peak_date|peak_price|drawdown_after_peak_pct|
|---|---|---|---|---|---|---|---|---|---|---|---|
|014940|2024-06-14|3,530.00|19.26|-3.4|41.5|-4.39|82.44|-9.21|2025-01-20|6,440.00|-22.98|
|077970|2024-05-17|13,840.00|34.83|-6.86|76.3|-6.94|99.78|-6.94|2025-02-13|27,650.00|-8.68|
|010620|2024-04-29|74,200.00|7.01|-7.55|65.5|-7.55|94.47|-7.55|2025-01-21|144,300.00|-13.65|
|010620|2024-07-29|116,800.00|5.14|-21.23|11.99|-21.23|41.01|-21.23|2025-04-25|164,700.00|-3.76|
|082740|2025-02-17|25,750.00|7.96|-21.17|25.63|-22.33|109.32|-22.33|2025-11-03|53,900.00|-22.91|
|329180|2024-07-29|208,000.00|6.97|-18.32|17.55|-18.8|95.19|-18.8|2025-04-25|406,000.00|-4.93|
|010140|2025-02-07|12,770.00|24.04|-2.35|45.26|-2.35|154.5|-2.35|2025-10-30|32,500.00|-11.23|


## 13. Current Calibrated Profile Stress Test

|symbol|before_score|before_stage|after_score|after_stage|MFE90|MAE90|MFE180|current_profile_verdict|interpretation|
|---|---|---|---|---|---|---|---|---|---|
|014940|78|Stage2-Actionable|82|Stage3-Yellow|41.5|-4.39|82.44|current_profile_correct|Small shipbuilding-equipment supplier: the bridge is not just “shipbuilders have backlog”; the report gives item-level demand linkage and 1Q24 price-revision/margin route. The 180D path shows strong upside with moderate MAE.|
|077970|72|Stage2|78|Stage2-Actionable|76.3|-6.94|99.78|current_profile_correct|The bridge is customer-route and segment-quality rather than headline ship orders. Price path validates Stage2-Actionable, not automatic Green.|
|010620|76|Stage2-Actionable|84|Stage3-Yellow|65.5|-7.55|94.47|current_profile_correct|Early order/backlog evidence appeared before the clean profit print. It supports Stage2-Actionable/Yellow once the loss-burnoff mechanism is stated.|
|010620|88|Stage3-Green|77|Stage2-Actionable|11.99|-21.23|41.01|current_profile_too_early|Same symbol as case 03, but a different trigger family: post-confirmation Green timing. The lesson is not that Mipo was bad; the Green label was late-cycle/high-MAE unless phase asymmetry was checked.|
|082740|88|Stage3-Green|79|Stage2-Actionable|25.63|-22.33|109.32|current_profile_too_early|Backlog quality was strong, but a Green trigger without price-phase/high-MAE guard would be uncomfortable. Later success does not erase the initial calibration error.|
|329180|89|Stage3-Green|82|Stage3-Yellow|17.55|-18.8|95.19|current_profile_too_early|Good result/backlog eventually worked, but immediate 90D path included almost -19% MAE. Green should wait for phase asymmetry and offshore-cost qualification.|
|010140|85|Stage3-Yellow|89|Stage3-Green|45.26|-2.35|154.5|current_profile_correct|Unlike the high-MAE Green traps, this row combines backlog, margin confirmation and a clean post-trigger path; it supports Green when conversion and price phase both cooperate.|


Stress-test answers:

1. Current profile would usually promote direct backlog/order/result evidence to Stage2-Actionable or Yellow, and could promote clean confirmed revisions to Green.
2. For `014940`, `077970`, early `010620`, and `010140`, that is broadly aligned with the 90D/180D price path.
3. For late `010620`, `082740`, and `329180`, Stage3-Green at the confirmation date is too phase-blind: the thesis survives, but the entry timing has high-MAE risk.
4. Stage2-Actionable bonus is not globally wrong; it needs a C01-specific **bridge specificity** split.
5. Green 87/revision 55 is not too strict; in this archetype it is sometimes too permissive when evidence is result-only after rerating.
6. Price-only blowoff guard remains appropriate.
7. Full 4B non-price requirement remains appropriate; high local MAE by itself is watch, not full 4B.
8. Hard 4C routing should be qualified: no cancellation, customer route death, accounting break, or repeated cash damage was confirmed in the high-MAE live-bridge rows.

## 14. Stage2 / Yellow / Green Comparison

| comparison | observation |
|---|---|
| Stage2-Actionable positives | average MFE90 `57.14` / MAE90 `-5.31` |
| Stage3-Green counterexample set | average MFE90 `18.39` / MAE90 `-20.79` |
| Green lateness ratio | `not_computable_without_same-case Stage2/Green pairs`; phase risk inferred by MAE and local rerating context |
| main lesson | Green is not outcome hindsight; for C01 it needs margin/cash freshness plus phase sanity |

## 15. 4B Local vs Full-window Timing Audit

| symbol | trigger_type | four_b_evidence_type | local_peak_proximity | full_window_peak_proximity | timing_verdict |
|---|---|---|---|---|---|
| 010620 | Stage3-Green | price_only_local_peak, positioning_overheat | watch_only_phase_risk | not_full_window_4b | local_watch_not_full_4b |
| 082740 | Stage3-Green | price_only_local_peak, positioning_overheat | watch_only_phase_risk | not_full_window_4b | local_watch_not_full_4b |
| 329180 | Stage3-Green | margin_or_backlog_slowdown, price_only_local_peak | watch_only_phase_risk | not_full_window_4b | local_watch_not_full_4b |

These are not sell-signal studies. They are calibration rows showing that a full 4B overlay should require non-price risk, while local 4B-watch is enough to cap Green when entry-phase MAE is elevated.

## 16. 4C Protection Audit

| symbol | stage4c_evidence_fields | four_c_protection_label | interpretation |
|---|---|---|---|
| 010620 | none | not_4c_route_death_unconfirmed | high MAE but profit-turnaround route survived |
| 082740 | none | not_4c_route_death_unconfirmed | high MAE but backlog route and later recovery survived |
| 329180 | none | not_4c_route_death_unconfirmed | offshore one-off/cost issue is watch, not thesis death |

## 17. Sector-Specific Rule Candidate

`L1_INDUSTRIALS_INFRA_DEFENSE_GRID` order/backlog evidence should remain capped below Green unless issuer-level margin, cash conversion, production mix, or direct customer route proves that the backlog can travel into earnings without a fresh high-MAE phase penalty.

## 18. Canonical-Archetype Rule Candidate

`C01_ORDER_BACKLOG_MARGIN_BRIDGE` should use a **backlog-to-margin-cash phase ladder**:

`backlog quantity -> customer/order quality -> margin/cash conversion -> price-phase sanity`.

Supplier and engine rows can be Actionable when the customer route is direct. Late result Green is capped when the 30/90D MAE trap is unresolved. High-MAE with a live bridge is a watch state, not hard 4C.

## 19. Before / After Backtest Comparison

|profile_id|eligible|avg_MFE90|avg_MAE90|avg_MFE180|avg_MAE180|false_positive_rate|verdict|
|---|---|---|---|---|---|---|---|
|P0_e2r_2_1_stock_web_calibrated_proxy|7|40.53|-11.94|96.67|-12.63|0.43|mixed; three Green timing errors remain|
|P0b_e2r_2_0_baseline_reference|7|40.53|-11.94|96.67|-12.63|0.57|worse false-positive control|
|P1_L1_sector_specific_candidate_profile|5|48.11|-8.49|94.44|-9.46|0.25|improves false-positive control while retaining positives|
|P2_C01_canonical_candidate_profile|4|57.14|-5.31|107.8|-6.51|0.0|best alignment for clean conversion positives|
|P3_C01_counterexample_guard_profile|3|18.39|-20.79|81.84|-20.79|0.67|guards against over-eager Green and over-eager 4C|


## 20. Score-Return Alignment Matrix

|symbol|score before -> after|price path|alignment label|
|---|---|---|---|
|014940|78 Stage2-Actionable -> 82 Stage3-Yellow|MFE90 41.5 / MAE90 -4.39 / MFE180 82.44|aligned|
|077970|72 Stage2 -> 78 Stage2-Actionable|MFE90 76.3 / MAE90 -6.94 / MFE180 99.78|aligned|
|010620|76 Stage2-Actionable -> 84 Stage3-Yellow|MFE90 65.5 / MAE90 -7.55 / MFE180 94.47|aligned|
|010620|88 Stage3-Green -> 77 Stage2-Actionable|MFE90 11.99 / MAE90 -21.23 / MFE180 41.01|residual_error_or_guardrail_needed|
|082740|88 Stage3-Green -> 79 Stage2-Actionable|MFE90 25.63 / MAE90 -22.33 / MFE180 109.32|residual_error_or_guardrail_needed|
|329180|89 Stage3-Green -> 82 Stage3-Yellow|MFE90 17.55 / MAE90 -18.8 / MFE180 95.19|residual_error_or_guardrail_needed|
|010140|85 Stage3-Yellow -> 89 Stage3-Green|MFE90 45.26 / MAE90 -2.35 / MFE180 154.5|aligned|


## 21. Coverage Matrix

| large_sector_id | canonical_archetype_id | fine_archetype_id | positive_case_count | counterexample_count | 4B_case_count | 4C_case_count | new_independent_case_count | reused_case_count | calibration_usable_trigger_count | representative_trigger_count | current_profile_error_count | sector_rule_candidate | canonical_rule_candidate | coverage_gap_after_this_loop |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|---|---|
| L1_INDUSTRIALS_INFRA_DEFENSE_GRID | C01_ORDER_BACKLOG_MARGIN_BRIDGE | C01_SHIPBUILDING_BACKLOG_MARGIN_CASH_DIRECT_URL_REPAIR | 4 | 3 | 3 | 0 | 7 | 0 | 7 | 7 | 3 | yes | yes | C01 now has additional supplier/engine direct bridge rows and late-Green high-MAE counterexamples |

## 22. Residual Contribution Summary

new_independent_case_count: `7`
reused_case_count: `0`
reused_case_ids: `[]`
new_symbol_count: `2`
new_canonical_archetype_count: `0`
new_fine_archetype_count: `1`
new_trigger_family_count: `7`
tested_existing_calibrated_axes: `stage2_actionable_evidence_bonus`, `stage3_green_total_min`, `stage3_green_revision_min`, `full_4b_requires_non_price_evidence`, `hard_4c_thesis_break_routes_to_4c`
residual_error_types_found: `late-result Green high-MAE trap`, `backlog headline vs margin/cash conversion gap`, `high-MAE live-bridge not hard-4C`
new_axis_proposed: `c01_backlog_margin_cash_phase_asymmetry_ladder; c01_supplier_engine_bridge_quality_gate; c01_high_mae_live_bridge_not_4c_guard`
existing_axis_strengthened: `stage2_required_bridge; stage3_green_revision_min_by_margin_cash_freshness; local_4b_watch_guard; full_4b_requires_non_price_evidence`
existing_axis_weakened: `hard_4c_thesis_break_routes_to_4c_qualified_for_high_mae_live_bridge_only`
existing_axis_kept: `stage2_actionable_evidence_bonus; price_only_blowoff_blocks_positive_stage`
sector_specific_rule_candidate: `L1 order/backlog rows should remain capped below Green unless issuer-level margin, cash conversion, production mix, or direct customer route proves that the backlog can travel into earnings without a fresh high-MAE phase penalty.`
canonical_archetype_rule_candidate: `C01 should use a backlog-to-margin-cash phase ladder: backlog quantity -> customer/order quality -> margin/cash conversion -> price-phase sanity.`
no_new_signal_reason: `null`
loop_contribution_label: `canonical_archetype_rule_candidate`
do_not_propose_new_weight_delta: `false`

## 23. Validation Scope / Non-Validation Scope

Validated:

- Stock-Web tradable raw OHLC entry rows for all seven triggers.
- 30D/90D/180D MFE and MAE for every representative trigger.
- Round/sector/canonical mapping consistency.
- Exact duplicate key avoidance for this local execution.
- Positive/counterexample balance.

Not validated in this MD:

- Live candidates or current recommendations.
- Production scoring source code.
- Broker target price accuracy.
- Any price data beyond Stock-Web manifest max date `2026-02-20`.

## 24. Shadow Weight Calibration

```csv
row_type,axis,scope,large_sector_id,canonical_archetype_id,baseline_value,tested_value,delta,reason,backtest_effect,trigger_ids,calibration_usable_count,new_independent_case_count,counterexample_count,confidence,proposal_type,notes
shadow_weight,c01_backlog_margin_cash_phase_asymmetry_ladder,canonical_archetype_specific,L1_INDUSTRIALS_INFRA_DEFENSE_GRID,C01_ORDER_BACKLOG_MARGIN_BRIDGE,0,1,+1,"Separate backlog quantity from margin/cash conversion and price phase","drops late-result/high-MAE Green traps while keeping 4 clean positives","C01-R1-L211-04-T1|C01-R1-L211-05-T1|C01-R1-L211-06-T1",7,7,3,medium,canonical_shadow_only,"not production; post-calibrated residual"
shadow_weight,c01_high_mae_live_bridge_not_4c_guard,canonical_archetype_specific,L1_INDUSTRIALS_INFRA_DEFENSE_GRID,C01_ORDER_BACKLOG_MARGIN_BRIDGE,0,1,+1,"High MAE after valid bridge should become watch, not automatic thesis death","keeps 010620/082740/329180 as timing-risk examples rather than hard 4C","C01-R1-L211-04-T1|C01-R1-L211-05-T1|C01-R1-L211-06-T1",7,7,3,low,guardrail_shadow_only,"qualifies hard_4c_thesis_break_routes_to_4c only for live-bridge rows"
```

## 25. Machine-Readable Rows

```jsonl
{"calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "manifest_max_date": "2026-02-20", "manifest_path": "atlas/manifest.json", "price_adjustment_status": "raw_unadjusted_marcap", "price_basis": "tradable_raw", "raw_shard_root": "atlas/ohlcv_raw_by_symbol_year", "row_type": "price_source_validation", "schema_path": "atlas/schema.json", "source": "Songdaiki/stock-web", "source_url": "https://github.com/Songdaiki/stock-web", "universe_path": "atlas/universe/all_symbols.csv", "validation_status": "usable_for_historical_calibration"}
{"best_trigger": "C01-R1-L211-01-T1", "calibration_usable": true, "canonical_archetype_id": "C01_ORDER_BACKLOG_MARGIN_BRIDGE", "case_id": "C01-R1-L211-01", "case_type": "structural_success", "company_name": "오리엔탈정공", "current_profile_verdict": "current_profile_correct", "fine_archetype_id": "C01_SHIPBUILDING_BACKLOG_MARGIN_CASH_DIRECT_URL_REPAIR", "independent_evidence_weight": 1.0, "is_new_independent_case": true, "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "loop": 211, "notes": "Small shipbuilding-equipment supplier: the bridge is not just “shipbuilders have backlog”; the report gives item-level demand linkage and 1Q24 price-revision/margin route. The 180D path shows strong upside with moderate MAE.", "positive_or_counterexample": "positive", "price_source": "Songdaiki/stock-web", "reuse_reason": null, "round": "R1", "row_type": "case", "score_price_alignment": "aligned", "symbol": "014940"}
{"best_trigger": "C01-R1-L211-02-T1", "calibration_usable": true, "canonical_archetype_id": "C01_ORDER_BACKLOG_MARGIN_BRIDGE", "case_id": "C01-R1-L211-02", "case_type": "structural_success", "company_name": "STX엔진", "current_profile_verdict": "current_profile_correct", "fine_archetype_id": "C01_SHIPBUILDING_BACKLOG_MARGIN_CASH_DIRECT_URL_REPAIR", "independent_evidence_weight": 1.0, "is_new_independent_case": true, "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "loop": 211, "notes": "The bridge is customer-route and segment-quality rather than headline ship orders. Price path validates Stage2-Actionable, not automatic Green.", "positive_or_counterexample": "positive", "price_source": "Songdaiki/stock-web", "reuse_reason": null, "round": "R1", "row_type": "case", "score_price_alignment": "aligned", "symbol": "077970"}
{"best_trigger": "C01-R1-L211-03-T1", "calibration_usable": true, "canonical_archetype_id": "C01_ORDER_BACKLOG_MARGIN_BRIDGE", "case_id": "C01-R1-L211-03", "case_type": "structural_success", "company_name": "HD현대미포", "current_profile_verdict": "current_profile_correct", "fine_archetype_id": "C01_SHIPBUILDING_BACKLOG_MARGIN_CASH_DIRECT_URL_REPAIR", "independent_evidence_weight": 1.0, "is_new_independent_case": true, "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "loop": 211, "notes": "Early order/backlog evidence appeared before the clean profit print. It supports Stage2-Actionable/Yellow once the loss-burnoff mechanism is stated.", "positive_or_counterexample": "positive", "price_source": "Songdaiki/stock-web", "reuse_reason": null, "round": "R1", "row_type": "case", "score_price_alignment": "aligned", "symbol": "010620"}
{"best_trigger": "C01-R1-L211-04-T1", "calibration_usable": true, "canonical_archetype_id": "C01_ORDER_BACKLOG_MARGIN_BRIDGE", "case_id": "C01-R1-L211-04", "case_type": "failed_rerating", "company_name": "HD현대미포", "current_profile_verdict": "current_profile_too_early", "fine_archetype_id": "C01_SHIPBUILDING_BACKLOG_MARGIN_CASH_DIRECT_URL_REPAIR", "independent_evidence_weight": 1.0, "is_new_independent_case": true, "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "loop": 211, "notes": "Same symbol as case 03, but a different trigger family: post-confirmation Green timing. The lesson is not that Mipo was bad; the Green label was late-cycle/high-MAE unless phase asymmetry was checked.", "positive_or_counterexample": "counterexample", "price_source": "Songdaiki/stock-web", "reuse_reason": null, "round": "R1", "row_type": "case", "score_price_alignment": "residual_error_or_guardrail_needed", "symbol": "010620"}
{"best_trigger": "C01-R1-L211-05-T1", "calibration_usable": true, "canonical_archetype_id": "C01_ORDER_BACKLOG_MARGIN_BRIDGE", "case_id": "C01-R1-L211-05", "case_type": "high_mae_success", "company_name": "한화엔진", "current_profile_verdict": "current_profile_too_early", "fine_archetype_id": "C01_SHIPBUILDING_BACKLOG_MARGIN_CASH_DIRECT_URL_REPAIR", "independent_evidence_weight": 1.0, "is_new_independent_case": true, "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "loop": 211, "notes": "Backlog quality was strong, but a Green trigger without price-phase/high-MAE guard would be uncomfortable. Later success does not erase the initial calibration error.", "positive_or_counterexample": "counterexample", "price_source": "Songdaiki/stock-web", "reuse_reason": null, "round": "R1", "row_type": "case", "score_price_alignment": "residual_error_or_guardrail_needed", "symbol": "082740"}
{"best_trigger": "C01-R1-L211-06-T1", "calibration_usable": true, "canonical_archetype_id": "C01_ORDER_BACKLOG_MARGIN_BRIDGE", "case_id": "C01-R1-L211-06", "case_type": "high_mae_success", "company_name": "HD현대중공업", "current_profile_verdict": "current_profile_too_early", "fine_archetype_id": "C01_SHIPBUILDING_BACKLOG_MARGIN_CASH_DIRECT_URL_REPAIR", "independent_evidence_weight": 1.0, "is_new_independent_case": true, "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "loop": 211, "notes": "Good result/backlog eventually worked, but immediate 90D path included almost -19% MAE. Green should wait for phase asymmetry and offshore-cost qualification.", "positive_or_counterexample": "counterexample", "price_source": "Songdaiki/stock-web", "reuse_reason": null, "round": "R1", "row_type": "case", "score_price_alignment": "residual_error_or_guardrail_needed", "symbol": "329180"}
{"best_trigger": "C01-R1-L211-07-T1", "calibration_usable": true, "canonical_archetype_id": "C01_ORDER_BACKLOG_MARGIN_BRIDGE", "case_id": "C01-R1-L211-07", "case_type": "structural_success", "company_name": "삼성중공업", "current_profile_verdict": "current_profile_correct", "fine_archetype_id": "C01_SHIPBUILDING_BACKLOG_MARGIN_CASH_DIRECT_URL_REPAIR", "independent_evidence_weight": 1.0, "is_new_independent_case": true, "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "loop": 211, "notes": "Unlike the high-MAE Green traps, this row combines backlog, margin confirmation and a clean post-trigger path; it supports Green when conversion and price phase both cooperate.", "positive_or_counterexample": "positive", "price_source": "Songdaiki/stock-web", "reuse_reason": null, "round": "R1", "row_type": "case", "score_price_alignment": "aligned", "symbol": "010140"}
{"MAE_180D_pct": -9.21, "MAE_1Y_pct": -9.21, "MAE_30D_pct": -3.4, "MAE_90D_pct": -4.39, "MFE_180D_pct": 82.44, "MFE_1Y_pct": 97.73, "MFE_2Y_pct": null, "MFE_30D_pct": 19.26, "MFE_90D_pct": 41.5, "aggregate_group_role": "representative", "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "calibration_block_reasons": [], "calibration_usable": true, "canonical_archetype_id": "C01_ORDER_BACKLOG_MARGIN_BRIDGE", "case_id": "C01-R1-L211-01", "company_name": "오리엔탈정공", "corporate_action_window_status": "clean_180D_window", "current_profile_verdict": "current_profile_correct", "dedupe_for_aggregate": true, "do_not_count_as_new_case": false, "drawdown_after_peak_pct": -22.98, "entry_date": "2024-06-14", "entry_ohlc_row": {"a": 540304675.0, "c": 3530.0, "d": "2024-06-14", "h": 3575.0, "l": 3425.0, "m": "KOSDAQ", "mc": 160875023330.0, "o": 3455.0, "s": 45573661, "v": 153076.0}, "entry_price": 3530.0, "entry_price_basis": "entry_date_close", "evidence_available_at_that_date": "KIRS/NICE D&B report dated 2024-06-13 links shipbuilding equipment demand with shipbuilding order flow and notes 1Q24 order-backlog unit-price revision effects. It is a direct issuer/sector report rather than a broker headline.", "evidence_family": "small_shipbuilding_equipment_price_revision_and_margin_conversion", "evidence_source": ["https://w4.kirs.or.kr/download/research/240613_%EA%B8%B0%EA%B3%84%EC%9E%A5%EB%B9%84_%EC%98%A4%EB%A6%AC%EC%97%94%ED%83%88%EC%A0%95%EA%B3%B5%28014940%29_%EC%84%A0%EB%B0%95%EC%9A%A9%20%ED%81%AC%EB%A0%88%EC%9D%B8%20%EB%B0%8F%20%EC%83%81%EB%B6%80%20%EA%B5%AC%EC%A1%B0%EB%AC%BC%20%EC%A0%9C%EC%A1%B0%20%EC%A0%84%EB%AC%B8%EA%B8%B0%EC%97%85_%EB%82%98%EC%9D%B4%EC%8A%A4%EB%94%94%EC%95%A4%EB%B9%84.pdf"], "fine_archetype_id": "C01_SHIPBUILDING_BACKLOG_MARGIN_CASH_DIRECT_URL_REPAIR", "forward_window_trading_days": 180, "four_b_evidence_type": [], "four_b_full_window_peak_proximity": "not_applicable", "four_b_local_peak_proximity": "not_applicable", "four_b_timing_verdict": "not_applicable", "four_c_protection_label": "not_4c_route_death_unconfirmed", "green_lateness_ratio": null, "independent_evidence_weight": 1.0, "is_new_independent_case": true, "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "loop": 211, "loop_objective": "counterexample_mining; residual_false_positive_mining; residual_missed_structural_mining; direct_url_proxy_mfe_mae_repair; 4B_non_price_requirement_stress_test; 4C_thesis_break_timing_test; canonical_archetype_compression", "peak_date": "2025-01-20", "peak_price": 6440.0, "price_adjustment_status": "raw_unadjusted_marcap", "price_basis": "tradable_raw", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_data_source": "Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/014/014940/2024.csv", "price_source": "Songdaiki/stock-web", "primary_archetype": "order_backlog_margin_bridge", "profile_path": "atlas/symbol_profiles/014/014940.json", "reuse_reason": null, "round": "R1", "row_type": "trigger", "same_entry_group_id": "C01_ORDER_BACKLOG_MARGIN_BRIDGE|014940|Stage2-Actionable|2024-06-14", "sector": "industrials_infra_defense_grid", "stage2_evidence_fields": ["public_event_or_disclosure", "customer_or_order_quality", "backlog_or_delivery_visibility"], "stage3_evidence_fields": ["margin_bridge", "financial_visibility"], "stage4b_evidence_fields": [], "stage4c_evidence_fields": [], "stock_web_manifest_max_date": "2026-02-20", "symbol": "014940", "trigger_date": "2024-06-13", "trigger_id": "C01-R1-L211-01-T1", "trigger_outcome_label": "small_supplier_margin_bridge_positive", "trigger_type": "Stage2-Actionable"}
{"MAE_180D_pct": -6.94, "MAE_1Y_pct": -6.94, "MAE_30D_pct": -6.86, "MAE_90D_pct": -6.94, "MFE_180D_pct": 99.78, "MFE_1Y_pct": 128.68, "MFE_2Y_pct": null, "MFE_30D_pct": 34.83, "MFE_90D_pct": 76.3, "aggregate_group_role": "representative", "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "calibration_block_reasons": [], "calibration_usable": true, "canonical_archetype_id": "C01_ORDER_BACKLOG_MARGIN_BRIDGE", "case_id": "C01-R1-L211-02", "company_name": "STX엔진", "corporate_action_window_status": "clean_180D_window", "current_profile_verdict": "current_profile_correct", "dedupe_for_aggregate": true, "do_not_count_as_new_case": false, "drawdown_after_peak_pct": -8.68, "entry_date": "2024-05-17", "entry_ohlc_row": {"a": 2087796310.0, "c": 13840.0, "d": "2024-05-17", "h": 14580.0, "l": 13490.0, "m": "KOSPI", "mc": 318443231360.0, "o": 14440.0, "s": 23008904, "v": 149912.0}, "entry_price": 13840.0, "entry_price_basis": "entry_date_close", "evidence_available_at_that_date": "KRX/KIND quarterly report for STX Engine dated 2024-05-16 identifies Q1 revenue, key customers including 방위사업청 and Hanwha Aerospace, and operating segment context. The row tests whether C01 can admit engine-supply bridge rows without treating them as generic shipbuilding beta.", "evidence_family": "engine_supplier_customer_mix_and_defense_civil_bridge", "evidence_source": ["https://kind.krx.co.kr/common/disclsviewer.do?acptno=20240516000707&docno=&method=search&viewerhost="], "fine_archetype_id": "C01_SHIPBUILDING_BACKLOG_MARGIN_CASH_DIRECT_URL_REPAIR", "forward_window_trading_days": 180, "four_b_evidence_type": [], "four_b_full_window_peak_proximity": "not_applicable", "four_b_local_peak_proximity": "not_applicable", "four_b_timing_verdict": "not_applicable", "four_c_protection_label": "not_4c_route_death_unconfirmed", "green_lateness_ratio": null, "independent_evidence_weight": 1.0, "is_new_independent_case": true, "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "loop": 211, "loop_objective": "counterexample_mining; residual_false_positive_mining; residual_missed_structural_mining; direct_url_proxy_mfe_mae_repair; 4B_non_price_requirement_stress_test; 4C_thesis_break_timing_test; canonical_archetype_compression", "peak_date": "2025-02-13", "peak_price": 27650.0, "price_adjustment_status": "raw_unadjusted_marcap", "price_basis": "tradable_raw", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_data_source": "Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/077/077970/2024.csv", "price_source": "Songdaiki/stock-web", "primary_archetype": "order_backlog_margin_bridge", "profile_path": "atlas/symbol_profiles/077/077970.json", "reuse_reason": null, "round": "R1", "row_type": "trigger", "same_entry_group_id": "C01_ORDER_BACKLOG_MARGIN_BRIDGE|077970|Stage2-Actionable|2024-05-17", "sector": "industrials_infra_defense_grid", "stage2_evidence_fields": ["public_event_or_disclosure", "customer_or_order_quality", "capacity_or_volume_route"], "stage3_evidence_fields": ["financial_visibility"], "stage4b_evidence_fields": [], "stage4c_evidence_fields": [], "stock_web_manifest_max_date": "2026-02-20", "symbol": "077970", "trigger_date": "2024-05-16", "trigger_id": "C01-R1-L211-02-T1", "trigger_outcome_label": "engine_supplier_bridge_positive", "trigger_type": "Stage2-Actionable"}
{"MAE_180D_pct": -7.55, "MAE_1Y_pct": -7.55, "MAE_30D_pct": -7.55, "MAE_90D_pct": -7.55, "MFE_180D_pct": 94.47, "MFE_1Y_pct": 139.22, "MFE_2Y_pct": null, "MFE_30D_pct": 7.01, "MFE_90D_pct": 65.5, "aggregate_group_role": "representative", "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "calibration_block_reasons": [], "calibration_usable": true, "canonical_archetype_id": "C01_ORDER_BACKLOG_MARGIN_BRIDGE", "case_id": "C01-R1-L211-03", "company_name": "HD현대미포", "corporate_action_window_status": "clean_180D_window", "current_profile_verdict": "current_profile_correct", "dedupe_for_aggregate": true, "do_not_count_as_new_case": false, "drawdown_after_peak_pct": -13.65, "entry_date": "2024-04-29", "entry_ohlc_row": {"a": 20512047300.0, "c": 74200.0, "d": "2024-04-29", "h": 74900.0, "l": 73100.0, "m": "KOSPI", "mc": 2963707455800.0, "o": 74400.0, "s": 39942149, "v": 276821.0}, "entry_price": 74200.0, "entry_price_basis": "entry_date_close", "evidence_available_at_that_date": "Hana report dated 2024-04-26 says 1Q24 new orders reached USD 2.56bn, already 82.5% of annual target, and backlog rose sharply to USD 8.03bn by sales basis while old low-margin backlog was being cleared.", "evidence_family": "mipo_early_orderbook_to_turnaround_bridge", "evidence_source": ["https://www.hanaw.com/download/research/FileServer/WEB/industry/enterprise/2024/04/25/HD_HM_240426_1Q24Re.pdf"], "fine_archetype_id": "C01_SHIPBUILDING_BACKLOG_MARGIN_CASH_DIRECT_URL_REPAIR", "forward_window_trading_days": 180, "four_b_evidence_type": [], "four_b_full_window_peak_proximity": "not_applicable", "four_b_local_peak_proximity": "not_applicable", "four_b_timing_verdict": "not_applicable", "four_c_protection_label": "not_4c_route_death_unconfirmed", "green_lateness_ratio": null, "independent_evidence_weight": 1.0, "is_new_independent_case": true, "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "loop": 211, "loop_objective": "counterexample_mining; residual_false_positive_mining; residual_missed_structural_mining; direct_url_proxy_mfe_mae_repair; 4B_non_price_requirement_stress_test; 4C_thesis_break_timing_test; canonical_archetype_compression", "peak_date": "2025-01-21", "peak_price": 144300.0, "price_adjustment_status": "raw_unadjusted_marcap", "price_basis": "tradable_raw", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_data_source": "Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/010/010620/2024.csv", "price_source": "Songdaiki/stock-web", "primary_archetype": "order_backlog_margin_bridge", "profile_path": "atlas/symbol_profiles/010/010620.json", "reuse_reason": null, "round": "R1", "row_type": "trigger", "same_entry_group_id": "C01_ORDER_BACKLOG_MARGIN_BRIDGE|010620|Stage2-Actionable|2024-04-29", "sector": "industrials_infra_defense_grid", "stage2_evidence_fields": ["public_event_or_disclosure", "backlog_or_delivery_visibility", "early_revision_signal"], "stage3_evidence_fields": ["margin_bridge", "financial_visibility"], "stage4b_evidence_fields": [], "stage4c_evidence_fields": [], "stock_web_manifest_max_date": "2026-02-20", "symbol": "010620", "trigger_date": "2024-04-26", "trigger_id": "C01-R1-L211-03-T1", "trigger_outcome_label": "early_turnaround_bridge_positive", "trigger_type": "Stage2-Actionable"}
{"MAE_180D_pct": -21.23, "MAE_1Y_pct": -21.23, "MAE_30D_pct": -21.23, "MAE_90D_pct": -21.23, "MFE_180D_pct": 41.01, "MFE_1Y_pct": 89.64, "MFE_2Y_pct": null, "MFE_30D_pct": 5.14, "MFE_90D_pct": 11.99, "aggregate_group_role": "representative", "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "calibration_block_reasons": [], "calibration_usable": true, "canonical_archetype_id": "C01_ORDER_BACKLOG_MARGIN_BRIDGE", "case_id": "C01-R1-L211-04", "company_name": "HD현대미포", "corporate_action_window_status": "clean_180D_window", "current_profile_verdict": "current_profile_too_early", "dedupe_for_aggregate": true, "do_not_count_as_new_case": false, "drawdown_after_peak_pct": -3.76, "entry_date": "2024-07-29", "entry_ohlc_row": {"a": 58318324900.0, "c": 116800.0, "d": "2024-07-29", "h": 117900.0, "l": 111800.0, "m": "KOSPI", "mc": 4665243003200.0, "o": 113300.0, "s": 39942149, "v": 502974.0}, "entry_price": 116800.0, "entry_price_basis": "entry_date_close", "evidence_available_at_that_date": "Hi Investment report dated 2024-07-26 says HD Hyundai Mipo finally turned profitable after six consecutive quarterly losses and includes backlog trend. This was a stronger confirmation, but it came after local rerating and then suffered >20% MAE.", "evidence_family": "mipo_late_turnaround_report_green_high_mae_trap", "evidence_source": ["https://stock.pstatic.net/stock-research/company/61/20240726_company_271472000.pdf"], "fine_archetype_id": "C01_SHIPBUILDING_BACKLOG_MARGIN_CASH_DIRECT_URL_REPAIR", "forward_window_trading_days": 180, "four_b_evidence_type": ["price_only_local_peak", "positioning_overheat"], "four_b_full_window_peak_proximity": "not_full_window_4b", "four_b_local_peak_proximity": "watch_only_phase_risk", "four_b_timing_verdict": "local_watch_not_full_4b", "four_c_protection_label": "not_4c_route_death_unconfirmed", "green_lateness_ratio": "not_computable_without_case_stage2_pair", "independent_evidence_weight": 1.0, "is_new_independent_case": true, "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "loop": 211, "loop_objective": "counterexample_mining; residual_false_positive_mining; residual_missed_structural_mining; direct_url_proxy_mfe_mae_repair; 4B_non_price_requirement_stress_test; 4C_thesis_break_timing_test; canonical_archetype_compression", "peak_date": "2025-04-25", "peak_price": 164700.0, "price_adjustment_status": "raw_unadjusted_marcap", "price_basis": "tradable_raw", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_data_source": "Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/010/010620/2024.csv", "price_source": "Songdaiki/stock-web", "primary_archetype": "order_backlog_margin_bridge", "profile_path": "atlas/symbol_profiles/010/010620.json", "reuse_reason": null, "round": "R1", "row_type": "trigger", "same_entry_group_id": "C01_ORDER_BACKLOG_MARGIN_BRIDGE|010620|Stage3-Green|2024-07-29", "sector": "industrials_infra_defense_grid", "stage2_evidence_fields": ["public_event_or_disclosure", "backlog_or_delivery_visibility"], "stage3_evidence_fields": ["confirmed_revision", "margin_bridge", "multiple_public_sources"], "stage4b_evidence_fields": ["price_only_local_peak", "positioning_overheat"], "stage4c_evidence_fields": [], "stock_web_manifest_max_date": "2026-02-20", "symbol": "010620", "trigger_date": "2024-07-26", "trigger_id": "C01-R1-L211-04-T1", "trigger_outcome_label": "late_turnaround_green_high_mae_counterexample", "trigger_type": "Stage3-Green"}
{"MAE_180D_pct": -22.33, "MAE_1Y_pct": null, "MAE_30D_pct": -21.17, "MAE_90D_pct": -22.33, "MFE_180D_pct": 109.32, "MFE_1Y_pct": null, "MFE_2Y_pct": null, "MFE_30D_pct": 7.96, "MFE_90D_pct": 25.63, "aggregate_group_role": "representative", "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "calibration_block_reasons": [], "calibration_usable": true, "canonical_archetype_id": "C01_ORDER_BACKLOG_MARGIN_BRIDGE", "case_id": "C01-R1-L211-05", "company_name": "한화엔진", "corporate_action_window_status": "clean_180D_window", "current_profile_verdict": "current_profile_too_early", "dedupe_for_aggregate": true, "do_not_count_as_new_case": false, "drawdown_after_peak_pct": -22.91, "entry_date": "2025-02-17", "entry_ohlc_row": {"a": 244160275400.0, "c": 25750.0, "d": "2025-02-17", "h": 27450.0, "l": 23900.0, "m": "KOSPI", "mc": 2148763906500.0, "o": 24500.0, "s": 83447142, "v": 9382582.0}, "entry_price": 25750.0, "entry_price_basis": "entry_date_close", "evidence_available_at_that_date": "Hanwha Engine 2024 performance material shows backlog of KRW 3.3841tn at 2024-12-31 with ship engines at 96.3%. The bridge is real, but the 30/90D MAE was deep before later recovery.", "evidence_family": "engine_backlog_good_but_entry_phase_high_mae", "evidence_source": ["https://www.hanwha-engine.com/attach/download/206b6f42-87a2-4646-8b50-b5a2a4e5de48"], "fine_archetype_id": "C01_SHIPBUILDING_BACKLOG_MARGIN_CASH_DIRECT_URL_REPAIR", "forward_window_trading_days": 180, "four_b_evidence_type": ["price_only_local_peak", "positioning_overheat"], "four_b_full_window_peak_proximity": "not_full_window_4b", "four_b_local_peak_proximity": "watch_only_phase_risk", "four_b_timing_verdict": "local_watch_not_full_4b", "four_c_protection_label": "not_4c_route_death_unconfirmed", "green_lateness_ratio": "not_computable_without_case_stage2_pair", "independent_evidence_weight": 1.0, "is_new_independent_case": true, "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "loop": 211, "loop_objective": "counterexample_mining; residual_false_positive_mining; residual_missed_structural_mining; direct_url_proxy_mfe_mae_repair; 4B_non_price_requirement_stress_test; 4C_thesis_break_timing_test; canonical_archetype_compression", "peak_date": "2025-11-03", "peak_price": 53900.0, "price_adjustment_status": "raw_unadjusted_marcap", "price_basis": "tradable_raw", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_data_source": "Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/082/082740/2025.csv", "price_source": "Songdaiki/stock-web", "primary_archetype": "order_backlog_margin_bridge", "profile_path": "atlas/symbol_profiles/082/082740.json", "reuse_reason": null, "round": "R1", "row_type": "trigger", "same_entry_group_id": "C01_ORDER_BACKLOG_MARGIN_BRIDGE|082740|Stage3-Green|2025-02-17", "sector": "industrials_infra_defense_grid", "stage2_evidence_fields": ["public_event_or_disclosure", "backlog_or_delivery_visibility", "customer_or_order_quality"], "stage3_evidence_fields": ["financial_visibility", "margin_bridge"], "stage4b_evidence_fields": ["price_only_local_peak", "positioning_overheat"], "stage4c_evidence_fields": [], "stock_web_manifest_max_date": "2026-02-20", "symbol": "082740", "trigger_date": "2025-02-14", "trigger_id": "C01-R1-L211-05-T1", "trigger_outcome_label": "engine_backlog_green_entry_phase_counterexample", "trigger_type": "Stage3-Green"}
{"MAE_180D_pct": -18.8, "MAE_1Y_pct": -18.8, "MAE_30D_pct": -18.32, "MAE_90D_pct": -18.8, "MFE_180D_pct": 95.19, "MFE_1Y_pct": 146.63, "MFE_2Y_pct": null, "MFE_30D_pct": 6.97, "MFE_90D_pct": 17.55, "aggregate_group_role": "representative", "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "calibration_block_reasons": [], "calibration_usable": true, "canonical_archetype_id": "C01_ORDER_BACKLOG_MARGIN_BRIDGE", "case_id": "C01-R1-L211-06", "company_name": "HD현대중공업", "corporate_action_window_status": "clean_180D_window", "current_profile_verdict": "current_profile_too_early", "dedupe_for_aggregate": true, "do_not_count_as_new_case": false, "drawdown_after_peak_pct": -4.93, "entry_date": "2024-07-29", "entry_ohlc_row": {"a": 85452424000.0, "c": 208000.0, "d": "2024-07-29", "h": 210000.0, "l": 201000.0, "m": "KOSPI", "mc": 18464808128000.0, "o": 207000.0, "s": 88773116, "v": 413038.0}, "entry_price": 208000.0, "entry_price_basis": "entry_date_close", "evidence_available_at_that_date": "Hana report dated 2024-07-26 says cost savings and FX helped, 1H orders reached USD 6.60bn or 69.2% of annual target, and sales-basis backlog was USD 33.5bn, while offshore remained weak with one-off advance-payment cost.", "evidence_family": "major_shipbuilder_2q_result_green_but_offshore_cost_and_phase_mae", "evidence_source": ["https://www.hanaw.com/download/research/FileServer/WEB/industry/enterprise/2024/07/25/HD_HHI_2Q24Re.pdf"], "fine_archetype_id": "C01_SHIPBUILDING_BACKLOG_MARGIN_CASH_DIRECT_URL_REPAIR", "forward_window_trading_days": 180, "four_b_evidence_type": ["margin_or_backlog_slowdown", "price_only_local_peak"], "four_b_full_window_peak_proximity": "not_full_window_4b", "four_b_local_peak_proximity": "watch_only_phase_risk", "four_b_timing_verdict": "local_watch_not_full_4b", "four_c_protection_label": "not_4c_route_death_unconfirmed", "green_lateness_ratio": "not_computable_without_case_stage2_pair", "independent_evidence_weight": 1.0, "is_new_independent_case": true, "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "loop": 211, "loop_objective": "counterexample_mining; residual_false_positive_mining; residual_missed_structural_mining; direct_url_proxy_mfe_mae_repair; 4B_non_price_requirement_stress_test; 4C_thesis_break_timing_test; canonical_archetype_compression", "peak_date": "2025-04-25", "peak_price": 406000.0, "price_adjustment_status": "raw_unadjusted_marcap", "price_basis": "tradable_raw", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_data_source": "Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/329/329180/2024.csv", "price_source": "Songdaiki/stock-web", "primary_archetype": "order_backlog_margin_bridge", "profile_path": "atlas/symbol_profiles/329/329180.json", "reuse_reason": null, "round": "R1", "row_type": "trigger", "same_entry_group_id": "C01_ORDER_BACKLOG_MARGIN_BRIDGE|329180|Stage3-Green|2024-07-29", "sector": "industrials_infra_defense_grid", "stage2_evidence_fields": ["public_event_or_disclosure", "backlog_or_delivery_visibility", "customer_or_order_quality"], "stage3_evidence_fields": ["confirmed_revision", "margin_bridge"], "stage4b_evidence_fields": ["margin_or_backlog_slowdown", "price_only_local_peak"], "stage4c_evidence_fields": [], "stock_web_manifest_max_date": "2026-02-20", "symbol": "329180", "trigger_date": "2024-07-26", "trigger_id": "C01-R1-L211-06-T1", "trigger_outcome_label": "major_shipbuilder_green_high_mae_counterexample", "trigger_type": "Stage3-Green"}
{"MAE_180D_pct": -2.35, "MAE_1Y_pct": null, "MAE_30D_pct": -2.35, "MAE_90D_pct": -2.35, "MFE_180D_pct": 154.5, "MFE_1Y_pct": null, "MFE_2Y_pct": null, "MFE_30D_pct": 24.04, "MFE_90D_pct": 45.26, "aggregate_group_role": "representative", "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "calibration_block_reasons": [], "calibration_usable": true, "canonical_archetype_id": "C01_ORDER_BACKLOG_MARGIN_BRIDGE", "case_id": "C01-R1-L211-07", "company_name": "삼성중공업", "corporate_action_window_status": "clean_180D_window", "current_profile_verdict": "current_profile_correct", "dedupe_for_aggregate": true, "do_not_count_as_new_case": false, "drawdown_after_peak_pct": -11.23, "entry_date": "2025-02-07", "entry_ohlc_row": {"a": 88295738570.0, "c": 12770.0, "d": "2025-02-07", "h": 12930.0, "l": 12630.0, "m": "KOSPI", "mc": 11237600000000.0, "o": 12910.0, "s": 880000000, "v": 6918096.0}, "entry_price": 12770.0, "entry_price_basis": "entry_date_close", "evidence_available_at_that_date": "IBK and Meritz materials dated 2025-02-06 discuss 2024 operating-profit achievement, order backlog, and 2025 earnings expansion; Meritz cites 2024 year-end backlog of KRW 32.3tn, with Russian project caveat.", "evidence_family": "samsung_heavy_backlog_and_clean_margin_confirmation", "evidence_source": ["https://www.ibks.com/company/common/download.jsp?filename=20250206074137953_ko.pdf&filepath=%2Ffiles%2Ftradeinfo%2Fbusreport", "https://home.imeritz.com/include/resource/research/WorkFlow/20250205102728702K_02.pdf"], "fine_archetype_id": "C01_SHIPBUILDING_BACKLOG_MARGIN_CASH_DIRECT_URL_REPAIR", "forward_window_trading_days": 180, "four_b_evidence_type": [], "four_b_full_window_peak_proximity": "not_applicable", "four_b_local_peak_proximity": "not_applicable", "four_b_timing_verdict": "not_applicable", "four_c_protection_label": "not_4c_route_death_unconfirmed", "green_lateness_ratio": "not_computable_without_case_stage2_pair", "independent_evidence_weight": 1.0, "is_new_independent_case": true, "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "loop": 211, "loop_objective": "counterexample_mining; residual_false_positive_mining; residual_missed_structural_mining; direct_url_proxy_mfe_mae_repair; 4B_non_price_requirement_stress_test; 4C_thesis_break_timing_test; canonical_archetype_compression", "peak_date": "2025-10-30", "peak_price": 32500.0, "price_adjustment_status": "raw_unadjusted_marcap", "price_basis": "tradable_raw", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_data_source": "Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/010/010140/2025.csv", "price_source": "Songdaiki/stock-web", "primary_archetype": "order_backlog_margin_bridge", "profile_path": "atlas/symbol_profiles/010/010140.json", "reuse_reason": null, "round": "R1", "row_type": "trigger", "same_entry_group_id": "C01_ORDER_BACKLOG_MARGIN_BRIDGE|010140|Stage3-Green|2025-02-07", "sector": "industrials_infra_defense_grid", "stage2_evidence_fields": ["public_event_or_disclosure", "backlog_or_delivery_visibility", "customer_or_order_quality"], "stage3_evidence_fields": ["confirmed_revision", "margin_bridge", "multiple_public_sources", "financial_visibility"], "stage4b_evidence_fields": [], "stage4c_evidence_fields": [], "stock_web_manifest_max_date": "2026-02-20", "symbol": "010140", "trigger_date": "2025-02-06", "trigger_id": "C01-R1-L211-07-T1", "trigger_outcome_label": "clean_margin_backlog_green_positive", "trigger_type": "Stage3-Green"}
{"MAE_90D_pct": -4.39, "MFE_90D_pct": 41.5, "canonical_archetype_id": "C01_ORDER_BACKLOG_MARGIN_BRIDGE", "case_id": "C01-R1-L211-01", "changed_components": ["backlog_visibility_score", "margin_bridge_score", "valuation_repricing_score", "execution_risk_score"], "component_delta_explanation": "C01-specific ladder separates backlog quantity from margin/cash conversion and price-phase/high-MAE risk; production scoring unchanged.", "current_profile_verdict": "current_profile_correct", "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "raw_component_scores_after": {"accounting_trust_risk_score": 0, "backlog_visibility_score": 78, "contract_score": 58, "customer_quality_score": 70, "dilution_cb_risk_score": 0, "execution_risk_score": 0, "legal_or_contract_risk_score": 0, "margin_bridge_score": 76, "policy_or_regulatory_score": 0, "relative_strength_score": 0, "revision_score": 64, "valuation_repricing_score": 0}, "raw_component_scores_before": {"accounting_trust_risk_score": 0, "backlog_visibility_score": 78, "contract_score": 58, "customer_quality_score": 70, "dilution_cb_risk_score": 0, "execution_risk_score": 0, "legal_or_contract_risk_score": 0, "margin_bridge_score": 72, "policy_or_regulatory_score": 0, "relative_strength_score": 0, "revision_score": 0, "valuation_repricing_score": 0}, "row_type": "score_simulation", "score_return_alignment_label": "aligned", "stage_label_after": "Stage3-Yellow", "stage_label_before": "Stage2-Actionable", "symbol": "014940", "trigger_id": "C01-R1-L211-01-T1", "weighted_score_after": 82, "weighted_score_before": 78}
{"MAE_90D_pct": -6.94, "MFE_90D_pct": 76.3, "canonical_archetype_id": "C01_ORDER_BACKLOG_MARGIN_BRIDGE", "case_id": "C01-R1-L211-02", "changed_components": ["backlog_visibility_score", "margin_bridge_score", "valuation_repricing_score", "execution_risk_score"], "component_delta_explanation": "C01-specific ladder separates backlog quantity from margin/cash conversion and price-phase/high-MAE risk; production scoring unchanged.", "current_profile_verdict": "current_profile_correct", "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "raw_component_scores_after": {"accounting_trust_risk_score": 0, "backlog_visibility_score": 78, "contract_score": 62, "customer_quality_score": 70, "dilution_cb_risk_score": 0, "execution_risk_score": 0, "legal_or_contract_risk_score": 0, "margin_bridge_score": 76, "policy_or_regulatory_score": 0, "relative_strength_score": 0, "revision_score": 64, "valuation_repricing_score": 0}, "raw_component_scores_before": {"accounting_trust_risk_score": 0, "backlog_visibility_score": 78, "contract_score": 62, "customer_quality_score": 70, "dilution_cb_risk_score": 0, "execution_risk_score": 0, "legal_or_contract_risk_score": 0, "margin_bridge_score": 0, "policy_or_regulatory_score": 0, "relative_strength_score": 0, "revision_score": 0, "valuation_repricing_score": 0}, "row_type": "score_simulation", "score_return_alignment_label": "aligned", "stage_label_after": "Stage2-Actionable", "stage_label_before": "Stage2", "symbol": "077970", "trigger_id": "C01-R1-L211-02-T1", "weighted_score_after": 78, "weighted_score_before": 72}
{"MAE_90D_pct": -7.55, "MFE_90D_pct": 65.5, "canonical_archetype_id": "C01_ORDER_BACKLOG_MARGIN_BRIDGE", "case_id": "C01-R1-L211-03", "changed_components": ["backlog_visibility_score", "margin_bridge_score", "valuation_repricing_score", "execution_risk_score"], "component_delta_explanation": "C01-specific ladder separates backlog quantity from margin/cash conversion and price-phase/high-MAE risk; production scoring unchanged.", "current_profile_verdict": "current_profile_correct", "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "raw_component_scores_after": {"accounting_trust_risk_score": 0, "backlog_visibility_score": 78, "contract_score": 58, "customer_quality_score": 0, "dilution_cb_risk_score": 0, "execution_risk_score": 0, "legal_or_contract_risk_score": 0, "margin_bridge_score": 76, "policy_or_regulatory_score": 0, "relative_strength_score": 0, "revision_score": 64, "valuation_repricing_score": 0}, "raw_component_scores_before": {"accounting_trust_risk_score": 0, "backlog_visibility_score": 78, "contract_score": 58, "customer_quality_score": 0, "dilution_cb_risk_score": 0, "execution_risk_score": 0, "legal_or_contract_risk_score": 0, "margin_bridge_score": 72, "policy_or_regulatory_score": 0, "relative_strength_score": 0, "revision_score": 60, "valuation_repricing_score": 0}, "row_type": "score_simulation", "score_return_alignment_label": "aligned", "stage_label_after": "Stage3-Yellow", "stage_label_before": "Stage2-Actionable", "symbol": "010620", "trigger_id": "C01-R1-L211-03-T1", "weighted_score_after": 84, "weighted_score_before": 76}
{"MAE_90D_pct": -21.23, "MFE_90D_pct": 11.99, "canonical_archetype_id": "C01_ORDER_BACKLOG_MARGIN_BRIDGE", "case_id": "C01-R1-L211-04", "changed_components": ["backlog_visibility_score", "margin_bridge_score", "valuation_repricing_score", "execution_risk_score"], "component_delta_explanation": "C01-specific ladder separates backlog quantity from margin/cash conversion and price-phase/high-MAE risk; production scoring unchanged.", "current_profile_verdict": "current_profile_too_early", "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "raw_component_scores_after": {"accounting_trust_risk_score": 12, "backlog_visibility_score": 74, "contract_score": 58, "customer_quality_score": 0, "dilution_cb_risk_score": 0, "execution_risk_score": 68, "legal_or_contract_risk_score": 0, "margin_bridge_score": 62, "policy_or_regulatory_score": 0, "relative_strength_score": 0, "revision_score": 72, "valuation_repricing_score": 80}, "raw_component_scores_before": {"accounting_trust_risk_score": 12, "backlog_visibility_score": 74, "contract_score": 58, "customer_quality_score": 0, "dilution_cb_risk_score": 0, "execution_risk_score": 55, "legal_or_contract_risk_score": 0, "margin_bridge_score": 72, "policy_or_regulatory_score": 0, "relative_strength_score": 0, "revision_score": 72, "valuation_repricing_score": 68}, "row_type": "score_simulation", "score_return_alignment_label": "residual_error_or_guardrail_needed", "stage_label_after": "Stage2-Actionable", "stage_label_before": "Stage3-Green", "symbol": "010620", "trigger_id": "C01-R1-L211-04-T1", "weighted_score_after": 77, "weighted_score_before": 88}
{"MAE_90D_pct": -22.33, "MFE_90D_pct": 25.63, "canonical_archetype_id": "C01_ORDER_BACKLOG_MARGIN_BRIDGE", "case_id": "C01-R1-L211-05", "changed_components": ["backlog_visibility_score", "margin_bridge_score", "valuation_repricing_score", "execution_risk_score"], "component_delta_explanation": "C01-specific ladder separates backlog quantity from margin/cash conversion and price-phase/high-MAE risk; production scoring unchanged.", "current_profile_verdict": "current_profile_too_early", "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "raw_component_scores_after": {"accounting_trust_risk_score": 0, "backlog_visibility_score": 78, "contract_score": 58, "customer_quality_score": 70, "dilution_cb_risk_score": 0, "execution_risk_score": 68, "legal_or_contract_risk_score": 0, "margin_bridge_score": 62, "policy_or_regulatory_score": 0, "relative_strength_score": 0, "revision_score": 0, "valuation_repricing_score": 80}, "raw_component_scores_before": {"accounting_trust_risk_score": 0, "backlog_visibility_score": 78, "contract_score": 58, "customer_quality_score": 70, "dilution_cb_risk_score": 0, "execution_risk_score": 55, "legal_or_contract_risk_score": 0, "margin_bridge_score": 72, "policy_or_regulatory_score": 0, "relative_strength_score": 0, "revision_score": 0, "valuation_repricing_score": 68}, "row_type": "score_simulation", "score_return_alignment_label": "residual_error_or_guardrail_needed", "stage_label_after": "Stage2-Actionable", "stage_label_before": "Stage3-Green", "symbol": "082740", "trigger_id": "C01-R1-L211-05-T1", "weighted_score_after": 79, "weighted_score_before": 88}
{"MAE_90D_pct": -18.8, "MFE_90D_pct": 17.55, "canonical_archetype_id": "C01_ORDER_BACKLOG_MARGIN_BRIDGE", "case_id": "C01-R1-L211-06", "changed_components": ["backlog_visibility_score", "margin_bridge_score", "valuation_repricing_score", "execution_risk_score"], "component_delta_explanation": "C01-specific ladder separates backlog quantity from margin/cash conversion and price-phase/high-MAE risk; production scoring unchanged.", "current_profile_verdict": "current_profile_too_early", "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "raw_component_scores_after": {"accounting_trust_risk_score": 0, "backlog_visibility_score": 74, "contract_score": 58, "customer_quality_score": 70, "dilution_cb_risk_score": 0, "execution_risk_score": 68, "legal_or_contract_risk_score": 0, "margin_bridge_score": 62, "policy_or_regulatory_score": 0, "relative_strength_score": 0, "revision_score": 72, "valuation_repricing_score": 80}, "raw_component_scores_before": {"accounting_trust_risk_score": 0, "backlog_visibility_score": 74, "contract_score": 58, "customer_quality_score": 70, "dilution_cb_risk_score": 0, "execution_risk_score": 62, "legal_or_contract_risk_score": 0, "margin_bridge_score": 72, "policy_or_regulatory_score": 0, "relative_strength_score": 0, "revision_score": 72, "valuation_repricing_score": 68}, "row_type": "score_simulation", "score_return_alignment_label": "residual_error_or_guardrail_needed", "stage_label_after": "Stage3-Yellow", "stage_label_before": "Stage3-Green", "symbol": "329180", "trigger_id": "C01-R1-L211-06-T1", "weighted_score_after": 82, "weighted_score_before": 89}
{"MAE_90D_pct": -2.35, "MFE_90D_pct": 45.26, "canonical_archetype_id": "C01_ORDER_BACKLOG_MARGIN_BRIDGE", "case_id": "C01-R1-L211-07", "changed_components": ["backlog_visibility_score", "margin_bridge_score", "valuation_repricing_score", "execution_risk_score"], "component_delta_explanation": "C01-specific ladder separates backlog quantity from margin/cash conversion and price-phase/high-MAE risk; production scoring unchanged.", "current_profile_verdict": "current_profile_correct", "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "raw_component_scores_after": {"accounting_trust_risk_score": 12, "backlog_visibility_score": 78, "contract_score": 58, "customer_quality_score": 70, "dilution_cb_risk_score": 0, "execution_risk_score": 0, "legal_or_contract_risk_score": 0, "margin_bridge_score": 76, "policy_or_regulatory_score": 0, "relative_strength_score": 0, "revision_score": 72, "valuation_repricing_score": 0}, "raw_component_scores_before": {"accounting_trust_risk_score": 12, "backlog_visibility_score": 78, "contract_score": 58, "customer_quality_score": 70, "dilution_cb_risk_score": 0, "execution_risk_score": 0, "legal_or_contract_risk_score": 0, "margin_bridge_score": 72, "policy_or_regulatory_score": 0, "relative_strength_score": 0, "revision_score": 72, "valuation_repricing_score": 0}, "row_type": "score_simulation", "score_return_alignment_label": "aligned", "stage_label_after": "Stage3-Green", "stage_label_before": "Stage3-Yellow", "symbol": "010140", "trigger_id": "C01-R1-L211-07-T1", "weighted_score_after": 89, "weighted_score_before": 85}
{"avg_MAE_180D_pct": -12.63, "avg_MAE_90D_pct": -11.94, "avg_MFE_180D_pct": 96.67, "avg_MFE_90D_pct": 40.53, "avg_four_b_full_window_peak_proximity": "not_full_window_4b", "avg_four_b_local_peak_proximity": "watch_only_for_counterexample_rows", "avg_green_lateness_ratio": "not_computable_without_stage2_green_pairs", "canonical_archetype_id": "C01_ORDER_BACKLOG_MARGIN_BRIDGE", "changed_axes": "none", "changed_thresholds": "none", "eligible_trigger_count": 7, "false_positive_rate": 0.43, "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "late_green_count": 3, "loop": 211, "missed_structural_count": 0, "profile_hypothesis": "Current profile keeps Stage2 bridge and Green thresholds but lacks C01 phase-asymmetry distinction for supplier/engine/shipyard rows.", "profile_id": "P0_e2r_2_1_stock_web_calibrated_proxy", "profile_scope": "current_proxy", "round": "R1", "row_type": "profile_comparison", "score_return_alignment_verdict": "mixed; three Green timing errors remain", "selected_entry_trigger_per_case": "C01-R1-L211-01-T1|C01-R1-L211-02-T1|C01-R1-L211-03-T1|C01-R1-L211-04-T1|C01-R1-L211-05-T1|C01-R1-L211-06-T1|C01-R1-L211-07-T1", "selected_symbols": ["014940", "077970", "010620", "010620", "082740", "329180", "010140"]}
{"avg_MAE_180D_pct": -12.63, "avg_MAE_90D_pct": -11.94, "avg_MFE_180D_pct": 96.67, "avg_MFE_90D_pct": 40.53, "avg_four_b_full_window_peak_proximity": "not_full_window_4b", "avg_four_b_local_peak_proximity": "watch_only_for_counterexample_rows", "avg_green_lateness_ratio": "not_computable_without_stage2_green_pairs", "canonical_archetype_id": "C01_ORDER_BACKLOG_MARGIN_BRIDGE", "changed_axes": "rollback_to_old_baseline", "changed_thresholds": "looser Stage2 bridge; weaker 4B/4C guard", "eligible_trigger_count": 7, "false_positive_rate": 0.57, "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "late_green_count": 3, "loop": 211, "missed_structural_count": 0, "profile_hypothesis": "Older baseline would over-promote backlog headlines and suffer more high-MAE entries.", "profile_id": "P0b_e2r_2_0_baseline_reference", "profile_scope": "rollback_reference", "round": "R1", "row_type": "profile_comparison", "score_return_alignment_verdict": "worse false-positive control", "selected_entry_trigger_per_case": "C01-R1-L211-01-T1|C01-R1-L211-02-T1|C01-R1-L211-03-T1|C01-R1-L211-04-T1|C01-R1-L211-05-T1|C01-R1-L211-06-T1|C01-R1-L211-07-T1", "selected_symbols": ["014940", "077970", "010620", "010620", "082740", "329180", "010140"]}
{"avg_MAE_180D_pct": -9.46, "avg_MAE_90D_pct": -8.49, "avg_MFE_180D_pct": 94.44, "avg_MFE_90D_pct": 48.11, "avg_four_b_full_window_peak_proximity": "not_full_window_4b", "avg_four_b_local_peak_proximity": "watch_only_for_counterexample_rows", "avg_green_lateness_ratio": "not_computable_without_stage2_green_pairs", "canonical_archetype_id": "C01_ORDER_BACKLOG_MARGIN_BRIDGE", "changed_axes": "stage2_required_bridge kept; local_4b_watch_guard strengthened", "changed_thresholds": "Green capped below 87 without margin/cash/phase confirmation", "eligible_trigger_count": 5, "false_positive_rate": 0.25, "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "late_green_count": 1, "loop": 211, "missed_structural_count": 0, "profile_hypothesis": "L1 backlog rows need issuer-level conversion bridge before Green.", "profile_id": "P1_L1_sector_specific_candidate_profile", "profile_scope": "sector_specific", "round": "R1", "row_type": "profile_comparison", "score_return_alignment_verdict": "improves false-positive control while retaining positives", "selected_entry_trigger_per_case": "C01-R1-L211-01-T1|C01-R1-L211-02-T1|C01-R1-L211-03-T1|C01-R1-L211-07-T1|C01-R1-L211-04-T1", "selected_symbols": ["014940", "077970", "010620", "010140", "010620"]}
{"avg_MAE_180D_pct": -6.51, "avg_MAE_90D_pct": -5.31, "avg_MFE_180D_pct": 107.8, "avg_MFE_90D_pct": 57.14, "avg_four_b_full_window_peak_proximity": "not_full_window_4b", "avg_four_b_local_peak_proximity": "watch_only_for_counterexample_rows", "avg_green_lateness_ratio": "not_computable_without_stage2_green_pairs", "canonical_archetype_id": "C01_ORDER_BACKLOG_MARGIN_BRIDGE", "changed_axes": "c01_backlog_to_margin_cash_phase_ladder", "changed_thresholds": "Stage3-Green requires margin/cash freshness plus non-overheated phase", "eligible_trigger_count": 4, "false_positive_rate": 0.0, "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "late_green_count": 0, "loop": 211, "missed_structural_count": 0, "profile_hypothesis": "C01 splits backlog quantity, backlog quality, margin/cash conversion, and phase.", "profile_id": "P2_C01_canonical_candidate_profile", "profile_scope": "canonical_archetype_specific", "round": "R1", "row_type": "profile_comparison", "score_return_alignment_verdict": "best alignment for clean conversion positives", "selected_entry_trigger_per_case": "C01-R1-L211-01-T1|C01-R1-L211-02-T1|C01-R1-L211-03-T1|C01-R1-L211-07-T1", "selected_symbols": ["014940", "077970", "010620", "010140"]}
{"avg_MAE_180D_pct": -20.79, "avg_MAE_90D_pct": -20.79, "avg_MFE_180D_pct": 81.84, "avg_MFE_90D_pct": 18.39, "avg_four_b_full_window_peak_proximity": "not_full_window_4b", "avg_four_b_local_peak_proximity": "watch_only_for_counterexample_rows", "avg_green_lateness_ratio": "not_computable_without_stage2_green_pairs", "canonical_archetype_id": "C01_ORDER_BACKLOG_MARGIN_BRIDGE", "changed_axes": "hard_4c qualification; full_4b non-price evidence kept", "changed_thresholds": "4C only with route death/cancellation/accounting break/repeated cash damage", "eligible_trigger_count": 3, "false_positive_rate": 0.67, "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "late_green_count": 3, "loop": 211, "missed_structural_count": 0, "profile_hypothesis": "High-MAE but live bridge is not thesis death; it is timing/phase risk.", "profile_id": "P3_C01_counterexample_guard_profile", "profile_scope": "counterexample_guard", "round": "R1", "row_type": "profile_comparison", "score_return_alignment_verdict": "guards against over-eager Green and over-eager 4C", "selected_entry_trigger_per_case": "C01-R1-L211-04-T1|C01-R1-L211-05-T1|C01-R1-L211-06-T1", "selected_symbols": ["010620", "082740", "329180"]}
{"calibration_usable_case_count": 7, "calibration_usable_trigger_count": 7, "canonical_archetype_id": "C01_ORDER_BACKLOG_MARGIN_BRIDGE", "counterexample_count": 3, "current_profile_error_count": 3, "do_not_propose_new_weight_delta": false, "fine_archetype_id": "C01_SHIPBUILDING_BACKLOG_MARGIN_CASH_DIRECT_URL_REPAIR", "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "loop": 211, "loop_contribution_label": "canonical_archetype_rule_candidate", "new_independent_case_count": 7, "new_symbol_count": 2, "new_trigger_family_count": 7, "positive_case_count": 4, "production_scoring_changed": false, "representative_trigger_count": 7, "residual_contribution": "c01_backlog_margin_cash_phase_asymmetry_ladder", "reused_case_count": 0, "round": "R1", "row_type": "aggregate", "same_archetype_new_symbol_count": 2, "same_archetype_new_trigger_family_count": 7, "shadow_weight_only": true}
{"canonical_archetype_id": "C01_ORDER_BACKLOG_MARGIN_BRIDGE", "canonical_archetype_rule_candidate": "C01 should use a backlog-to-margin-cash phase ladder: backlog quantity -> customer/order quality -> margin/cash conversion -> price-phase sanity. Supplier/engine rows can be Actionable with direct customer route; late result Green is capped when 30/90D MAE risk is unresolved; high-MAE with live bridge is watch, not hard 4C.", "do_not_propose_new_weight_delta": false, "existing_axis_kept": "stage2_actionable_evidence_bonus; price_only_blowoff_blocks_positive_stage", "existing_axis_strengthened": "stage2_required_bridge; stage3_green_revision_min_by_margin_cash_freshness; local_4b_watch_guard; full_4b_requires_non_price_evidence", "existing_axis_weakened": "hard_4c_thesis_break_routes_to_4c_qualified_for_high_mae_live_bridge_only", "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "loop": 211, "loop_contribution_label": "canonical_archetype_rule_candidate", "new_axis_proposed": "c01_backlog_margin_cash_phase_asymmetry_ladder; c01_supplier_engine_bridge_quality_gate; c01_high_mae_live_bridge_not_4c_guard", "new_independent_case_count": 7, "new_symbol_count": 2, "new_trigger_family_count": 7, "residual_error_types_found": ["late-result Green high-MAE trap", "backlog headline versus margin/cash conversion gap", "high-MAE live-bridge not hard-4C"], "reused_case_count": 0, "round": "R1", "row_type": "residual_contribution", "sector_specific_rule_candidate": "L1 order/backlog rows should remain capped below Green unless issuer-level margin, cash conversion, production mix, or direct customer route proves that the backlog can travel into earnings without a fresh high-MAE phase penalty.", "tested_existing_calibrated_axes": ["stage2_required_bridge", "stage2_actionable_evidence_bonus", "stage3_green_total_min", "stage3_green_revision_min", "full_4b_requires_non_price_evidence", "hard_4c_thesis_break_routes_to_4c"]}
```

## Batch Ingest Self-Audit

expected_v12_result_file: `true`
filename_pattern_pass: `true`
metadata_filename_consistency: `pass`
jsonl_trigger_row_count: `7`
calibration_usable_trigger_count: `7`
representative_trigger_count: `7`
new_weight_evidence_candidate_count: `7`
guardrail_candidate_count: `3`
narrative_only_or_rejected_count: `0`
rows_missing_required_mfe_mae: `0`
rows_missing_entry_price_or_date: `0`
rows_with_noncanonical_trigger_type: `0`
rows_with_compact_mfe_mae_alias_only: `0`
ready_for_batch_ingest: `true`

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

completed_round = `R1`
completed_loop = `211`
selection_basis = `docs/core/V12_Research_No_Repeat_Index.md`
selected_priority_bucket = `Priority 1 C01 balance-quality reinforcement + Priority 0 direct URL/proxy/MFE-MAE repair`
next_recommended_archetypes = `C13 direct AMPC/utilization rows; C10 direct order-conversion rows; C15 spread freshness rows; C05 direct working-capital/FCF rows; C31 only for non-duplicate direct awarded-cashflow rows`
round_schedule_status = `coverage_index_selected`
round_sector_consistency = `pass`

## 28. Source Notes

- MAIN prompt: `https://raw.githubusercontent.com/Songdaiki/stock_agent/main/docs/core/e2r_v12_prompt_round_scheduler_corrected.txt`
- NO-REPEAT index: `https://raw.githubusercontent.com/Songdaiki/stock_agent/main/docs/core/V12_Research_No_Repeat_Index.md`
- Stock-Web manifest: `https://raw.githubusercontent.com/Songdaiki/stock-web/main/atlas/manifest.json`
- Stock-Web schema: `https://raw.githubusercontent.com/Songdaiki/stock-web/main/atlas/schema.json`
- Evidence URLs are listed in Section 9 and repeated inside JSONL trigger rows.
