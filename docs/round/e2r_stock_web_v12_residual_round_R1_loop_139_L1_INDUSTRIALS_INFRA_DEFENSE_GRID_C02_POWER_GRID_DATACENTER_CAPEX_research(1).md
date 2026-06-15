---
title: "E2R Stock-Web V12 Residual Research — R1 Loop 139 — C02 Power Grid / Datacenter CAPEX"
created_at_kst: "2026-06-13"
mode: "historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12"
selected_round: "R1"
selected_loop: 139
selected_priority_bucket: "Priority 0"
large_sector_id: "L1_INDUSTRIALS_INFRA_DEFENSE_GRID"
canonical_archetype_id: "C02_POWER_GRID_DATACENTER_CAPEX"
fine_archetype_id: "C02_GRID_TRANSFORMER_DATACENTER_CAPEX_BACKLOG_ASP_CAPACITY_BRIDGE"
deep_sub_archetype_id: "C02_DEEP_US_GRID_DATACENTER_TRANSFORMER_ASP_CAPA_LOCK_VS_PRICE_ONLY_THEME_PROXY"
stock_web_manifest_max_date: "2026-02-20"
price_basis: "tradable_raw"
price_adjustment_status: "raw_unadjusted_marcap"
production_scoring_changed: false
shadow_weight_only: true
handoff_prompt_executed_now: false
---

# E2R Stock-Web V12 Residual Research — R1 Loop 139 — C02 Power Grid / Datacenter CAPEX

> This is a historical calibration artifact only. It is not a live scan, not a watchlist, not investment advice, and not a production scoring patch.

## 0. Execution Mode / Scope Lock

```text
mode = historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12
current_stock_discovery_allowed = false
stock_agent_code_access_allowed = false
stock_agent_code_patch_allowed = false
production_scoring_changed = false
shadow_weight_only = true
output_format = one_standalone_markdown_file
```

This run follows the coverage-index-first scheduler. It uses stock_agent research artifacts only for coverage and duplicate avoidance; it does not inspect or patch `src/e2r`.

## 1. Current Calibrated Profile Proxy

Current profile proxy assumed by the execution prompt: `e2r_2_1_stock_web_calibrated`. Existing global safeguards are treated as already present: Stage2 Actionable evidence bonus, Stage3-Yellow 75, Stage3-Green 87 with revision gate, price-only blowoff block, full 4B non-price evidence requirement, and hard 4C thesis-break routing. This research does not re-prove those global rules; it adds C02 residual evidence.

## 2. Allowed Research Artifacts Read

| artifact | role | url |
| --- | --- | --- |
| MAIN EXECUTION PROMPT | procedure source | https://raw.githubusercontent.com/Songdaiki/stock_agent/main/docs/core/e2r_v12_prompt_round_scheduler_corrected.txt |
| V12_Research_No_Repeat_Index.md | coverage and duplicate avoidance only | https://raw.githubusercontent.com/Songdaiki/stock_agent/main/docs/core/V12_Research_No_Repeat_Index.md |
| docs/round directory listing | loop discovery only | https://github.com/Songdaiki/stock_agent/tree/main/docs/round |

No stock_agent source code was used.

## 3. Stock-Web Price Atlas Manifest Check

| atlas_version | source_name | price_adjustment_status | min_date | max_date | tradable_row_count | raw_row_count | symbol_count | active_like_symbol_count | calibration_shard_root | raw_shard_root |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1.0.0 | FinanceData/marcap | raw_unadjusted_marcap | 1995-05-02 | 2026-02-20 | 14354401 | 15214118 | 5414 | 2868 | atlas/ohlcv_tradable_by_symbol_year | atlas/ohlcv_raw_by_symbol_year |

All trigger rows use `atlas/ohlcv_tradable_by_symbol_year` close on entry date as entry price. Raw shards were not used for calibration.

## 4. Coverage-Index Scheduler Decision

| field | value |
| --- | --- |
| selected_priority_bucket | Priority 0 |
| selection_basis | C02 is No-Repeat Priority 0 rank 1: 10 rows, need 20 to 30 and 40 to 50. |
| selected_round | R1 |
| large_sector_id | L1_INDUSTRIALS_INFRA_DEFENSE_GRID |
| canonical_archetype_id | C02_POWER_GRID_DATACENTER_CAPEX |
| loop_rule | max visible C02 R1 loop=138 in docs/round listing, selected_loop=139 |

## 5. Canonical / Fine / Deep Archetype

```text
canonical_archetype_id = C02_POWER_GRID_DATACENTER_CAPEX
fine_archetype_id = C02_GRID_TRANSFORMER_DATACENTER_CAPEX_BACKLOG_ASP_CAPACITY_BRIDGE
deep_sub_archetype_id = C02_DEEP_US_GRID_DATACENTER_TRANSFORMER_ASP_CAPA_LOCK_VS_PRICE_ONLY_THEME_PROXY
```

Mechanism: C02 works when grid/datacenter CAPEX pressure appears as firm-specific order/backlog quality, ASP/lead-time power, capacity constraint, and margin/revision bridge. It fails when a stock merely borrows the sector story after price has already rerated.

## 6. Novelty / No-Repeat Check

| check | result | detail |
| --- | --- | --- |
| top covered symbols avoided when possible | pass | No-Repeat top C02 symbols listed 000500, 001440, 006260, 010120, 017510, 024840; selected primary symbols are outside that visible top-covered set. |
| hard duplicate key | pass | No duplicate canonical + symbol + trigger_type + entry_date key repeated from visible summary. |
| new trigger families | pass | ASP/margin bridge, distribution transformer backlog, late 4B watch, margin-gap Stage2, switchgear/cable source-proxy counterexamples. |

## 7. Evidence Source Map

| source_id | url |
| --- | --- |
| SRC_HDHE_2024_02_16 | https://securities.miraeasset.com/bbs/download/2122467.pdf?attachmentId=2122467 |
| SRC_JERYONG_YUANTA_2024_03_08 | https://www.myasset.com/myasset/research/rs_list/rs_view.cmd?SEQ=193547&cd006=&cd007=RE01&cd008= |
| SRC_JERYONG_NEWS_2024_05_29 | https://www.thebigdata.co.kr/view.php?ud=202405290538457085cd1e7f0bdf_23 |
| SRC_HYOSUNG_MIRAE_2024_11_01 | https://securities.miraeasset.com/newir/view/pc/en/investor/researchReportsView.jsp?messageId=2328068 |
| SRC_HYOSUNG_IBK_2025_04_07 | https://www.bondweb.co.kr/_research/downloadPage.asp?gn=1&number=841472 |
| SRC_ILJIN_MIRAE_2024_11_15 | https://securities.miraeasset.com/bbs/download/2132362.pdf?attachmentId=2132362 |
| SRC_KWANGMYUNG_THEME_2024_04_18 | https://www.thebigdata.co.kr/view.php?ud=202404180550415310cd1e7f0bdf_23 |
| SRC_KWANGMYUNG_CONTRACT_2023_11_24 | https://v.daum.net/v/4yNxFYbDyx |
| SRC_DAEWON_CABLE_SECTOR_2024_05_20 | https://pulse.mk.co.kr/news/english/11019506 |
| SRC_GLOBAL_CONTEXT_IEA_2026 | https://www.iea.org/reports/energy-and-ai/energy-demand-from-ai |

## 8. Symbol Profile / Corporate Action Validation

| symbol | profile_path | corporate_action_candidate_dates | corporate_action_clean_2024_2025_180D_windows |
| --- | --- | --- | --- |
| 006340 | atlas/symbol_profiles/006/006340.json | 1996-11-29,1997-06-19,1999-09-10,2000-03-21,2007-01-25,2010-05-07 | true |
| 017040 | atlas/symbol_profiles/017/017040.json | 2000-01-24,2000-04-25,2001-12-10 | true |
| 033100 | atlas/symbol_profiles/033/033100.json | 1999-11-30,1999-12-27,2000-02-21,2000-08-30,2006-01-06,2007-08-31,2011-11-28,2014-11-06 | true |
| 103590 | atlas/symbol_profiles/103/103590.json | 2024-02-13 | true |
| 267260 | atlas/symbol_profiles/267/267260.json | 2017-11-17,2017-11-28,2017-12-11,2018-11-23,2018-12-18,2019-12-30 | true |
| 298040 | atlas/symbol_profiles/298/298040.json | none | true |

All selected entry windows have 180 tradable rows available before the stock-web manifest max_date of 2026-02-20.

## 9. Trigger-Level Price Path Summary

| symbol | company_name | trigger_type | case_role | entry_date | entry_price | MFE_30D_pct | MAE_30D_pct | MFE_90D_pct | MAE_90D_pct | MFE_180D_pct | MAE_180D_pct | peak_date_180D | drawdown_after_peak_pct | current_profile_verdict |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 267260 | HD현대일렉트릭 | Stage2-Actionable | positive | 2024-02-16 | 115900 | 59.62 | -0.52 | 179.12 | -0.52 | 256.77 | -0.52 | 2024-11-12 | -8.46 | correct_stage2_actionable_accept |
| 033100 | 제룡전기 | Stage2-Actionable | positive | 2024-03-08 | 32550 | 73.58 | -7.68 | 209.37 | -7.68 | 209.37 | -7.68 | 2024-07-11 | -61.07 | correct_stage2_actionable_accept_but_4b_watch_needed_after_peak |
| 033100 | 제룡전기 | Stage4B | counterexample | 2024-05-29 | 73900 | 35.05 | -17.73 | 36.27 | -41.54 | 36.27 | -50.54 | 2024-07-11 | -63.7 | current_profile_needs_local_4b_watch_after_fast_rerating |
| 298040 | 효성중공업 | Stage2-Actionable | positive | 2024-11-01 | 417500 | 24.07 | -8.5 | 31.5 | -12.34 | 224.79 | -12.34 | 2025-07-28 | -7.37 | correct_stage2_actionable_accept |
| 103590 | 일진전기 | Stage2-Actionable | positive_mixed | 2024-11-15 | 24650 | 15.42 | -16.84 | 52.33 | -16.84 | 80.12 | -19.68 | 2025-07-29 | -10.36 | correct_stage2_but_green_blocked_until_margin_bridge |
| 017040 | 광명전기 | Stage2 | counterexample | 2024-04-18 | 2690 | 23.42 | -15.43 | 23.42 | -40.0 | 23.42 | -53.53 | 2024-05-08 | -62.35 | current_profile_should_block_actionable_on_source_proxy_only |
| 006340 | 대원전선 | Stage4B | counterexample | 2024-05-20 | 4440 | 7.55 | -26.01 | 7.55 | -42.57 | 7.55 | -50.34 | 2024-06-28 | -53.82 | current_profile_should_keep_price_only_cable_proxy_out_of_positive_promotion |

## 10. Positive Case Notes

### C02_R1L139_CASE_001_HDHE_20240216_STRUCTURAL_ASP_BACKLOG — HD현대일렉트릭 (267260)

Evidence: 2023 revenue and operating profit surged, with 1Q24 margin expected to improve on higher ASP and stabilizing cost ratio; use as confirmed ASP/margin bridge, not merely price momentum. Source: `SRC_HDHE_2024_02_16`.


Backtest: entry 2024-02-16 close 115900; MFE90 179.12%, MAE90 -0.52%, MFE180 256.77%, MAE180 -0.52%.


### C02_R1L139_CASE_002_JERYONG_20240308_EXPORT_BACKLOG_CAPA — 제룡전기 (033100)

Evidence: Yuanta-style research reported distribution-transformer purity, export mix jump, 2023 earnings surge, 3Q23 backlog KRW323.1bn and high-margin 2024 outlook. Source: `SRC_JERYONG_YUANTA_2024_03_08`.


Backtest: entry 2024-03-08 close 32550; MFE90 209.37%, MAE90 -7.68%, MFE180 209.37%, MAE180 -7.68%.


### C02_R1L139_CASE_004_HYOSUNG_20241101_LARGE_BACKLOG_OVERSEAS — 효성중공업 (298040)

Evidence: 3Q24 review showed operating profit beat and heavy-industry transformer demand backdrop; later 2025 source confirms 2024 backlog quality, US/Europe mix and capacity expansion bridge. Source: `SRC_HYOSUNG_MIRAE_2024_11_01`.


Backtest: entry 2024-11-01 close 417500; MFE90 31.5%, MAE90 -12.34%, MFE180 224.79%, MAE180 -12.34%.


### C02_R1L139_CASE_005_ILJIN_20241115_BACKLOG_WITH_MARGIN_GAP — 일진전기 (103590)

Evidence: 3Q24 revenue beat and backlog high, but operating profit declined YoY and OP margin was only 4.4%; C02 should accept backlog but require margin bridge before Green. Source: `SRC_ILJIN_MIRAE_2024_11_15`.


Backtest: entry 2024-11-15 close 24650; MFE90 52.33%, MAE90 -16.84%, MFE180 80.12%, MAE180 -19.68%.


## 11. Counterexample / 4B Watch Notes

### C02_R1L139_CASE_003_JERYONG_20240529_LATE_PRICE_4B_WATCH — 제룡전기 (033100)

Evidence: Later article still showed strong 1Q24 revenue/profit and backlog, but entry after rerating produced large 90/180D MAE; this is a local 4B watch/entry-risk row, not a thesis-failure 4C. Source: `SRC_JERYONG_NEWS_2024_05_29`.


Backtest: entry 2024-05-29 close 73900; MFE90 36.27%, MAE90 -41.54%, MFE180 36.27%, MAE180 -50.54%. This row is useful because the story can remain structurally true while the entry becomes a poor calibration point if it is late or only source-proxy.


### C02_R1L139_CASE_006_KWANGMYUNG_20240418_THEME_PROXY_COUNTER — 광명전기 (017040)

Evidence: Theme article tied the stock to AI/data-center power demand and noted prior Samsung P4 switchgear contracts, but the 2024 trigger lacked fresh company-level backlog/ASP/capacity bridge. Source: `SRC_KWANGMYUNG_THEME_2024_04_18`.


Backtest: entry 2024-04-18 close 2690; MFE90 23.42%, MAE90 -40.0%, MFE180 23.42%, MAE180 -53.53%. This row is useful because the story can remain structurally true while the entry becomes a poor calibration point if it is late or only source-proxy.


### C02_R1L139_CASE_007_DAEWON_20240520_CABLE_THEME_LATE_COUNTER — 대원전선 (006340)

Evidence: Sector article showed cable industry/global demand strength, but this row uses Daewon as a basket/proxy candidate after a sharp rerating; without firm-specific backlog bridge it must remain 4B watch or reject for promotion. Source: `SRC_DAEWON_CABLE_SECTOR_2024_05_20`.


Backtest: entry 2024-05-20 close 4440; MFE90 7.55%, MAE90 -42.57%, MFE180 7.55%, MAE180 -50.34%. This row is useful because the story can remain structurally true while the entry becomes a poor calibration point if it is late or only source-proxy.


## 12. 30D / 90D / 180D Path Interpretation

Positive rows averaged MFE90 118.08% with MAE90 -9.35%. Counterexample rows averaged MFE90 22.41% with MAE90 -41.37%. The lesson is not that C02 should be loosened; the lesson is that verified bridge rows can move violently upward, while late/source-proxy entries become deep drawdown traps.

## 13. Stage2 / Stage2-Actionable Alignment

C02 Stage2-Actionable should require at least one firm-specific non-price bridge: confirmed order/backlog visibility, ASP/lead-time/capacity evidence, or margin/revision conversion. Source-proxy news about AI/data-center power demand is not enough.

## 14. Stage3-Yellow / Stage3-Green Alignment

C02 can unlock Stage3-Yellow with strong backlog + ASP/capacity + earnings visibility. It should not unlock Stage3-Green merely because MFE was large; Green still needs revision/margin confirmation and valuation/late-entry guard.

## 15. Local 4B vs Full 4B Split

Local 4B applies when a valid thesis has already rerated quickly and entry risk rises, as in the later 제룡전기 row. Full 4B should require non-price deterioration or failure of the bridge, not simply price extension. Source-proxy rows with no company bridge should be `No-Promotion/Watch`, not positive promotion.

## 16. Hard 4C / Thesis Break Check

No hard 4C is asserted here. The counterexamples are late-entry or source-proxy failures, not confirmed thesis breaks. A hard 4C for C02 would require backlog cancellation, margin collapse, capacity/lead-time normalization, customer loss, or accounting/trust deterioration.

## 17. Raw Component Score Breakdown

| case_id | symbol | evidence | revision | visibility | valuation | bottleneck | quality | risk | score_before | score_after | stage_after |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| C02_R1L139_CASE_001_HDHE_20240216_STRUCTURAL_ASP_BACKLOG | 267260 | 88 | 78 | 86 | 57 | 84 | 80 | 42 | 79.4 | 83.2 | Stage3-Yellow |
| C02_R1L139_CASE_002_JERYONG_20240308_EXPORT_BACKLOG_CAPA | 033100 | 86 | 76 | 82 | 50 | 88 | 73 | 48 | 77.8 | 81.0 | Stage3-Yellow |
| C02_R1L139_CASE_003_JERYONG_20240529_LATE_PRICE_4B_WATCH | 033100 | 84 | 76 | 82 | 30 | 86 | 73 | 72 | 77.0 | 69.5 | Stage4B-Watch |
| C02_R1L139_CASE_004_HYOSUNG_20241101_LARGE_BACKLOG_OVERSEAS | 298040 | 82 | 72 | 81 | 55 | 82 | 78 | 45 | 75.7 | 79.4 | Stage3-Yellow |
| C02_R1L139_CASE_005_ILJIN_20241115_BACKLOG_WITH_MARGIN_GAP | 103590 | 78 | 63 | 77 | 48 | 78 | 64 | 60 | 73.0 | 74.6 | Stage2-Actionable |
| C02_R1L139_CASE_006_KWANGMYUNG_20240418_THEME_PROXY_COUNTER | 017040 | 39 | 28 | 35 | 34 | 45 | 38 | 78 | 62.0 | 53.5 | Stage1-Watch |
| C02_R1L139_CASE_007_DAEWON_20240520_CABLE_THEME_LATE_COUNTER | 006340 | 34 | 25 | 33 | 26 | 52 | 36 | 82 | 60.5 | 49.0 | Stage4B-Watch/No-Promotion |

## 18. Current Calibrated Profile Stress Test

| case_id | symbol | verdict | error_or_residual |
| --- | --- | --- | --- |
| C02_R1L139_CASE_001_HDHE_20240216_STRUCTURAL_ASP_BACKLOG | 267260 | correct_stage2_actionable_accept | no |
| C02_R1L139_CASE_002_JERYONG_20240308_EXPORT_BACKLOG_CAPA | 033100 | correct_stage2_actionable_accept_but_4b_watch_needed_after_peak | no |
| C02_R1L139_CASE_003_JERYONG_20240529_LATE_PRICE_4B_WATCH | 033100 | current_profile_needs_local_4b_watch_after_fast_rerating | yes |
| C02_R1L139_CASE_004_HYOSUNG_20241101_LARGE_BACKLOG_OVERSEAS | 298040 | correct_stage2_actionable_accept | no |
| C02_R1L139_CASE_005_ILJIN_20241115_BACKLOG_WITH_MARGIN_GAP | 103590 | correct_stage2_but_green_blocked_until_margin_bridge | no |
| C02_R1L139_CASE_006_KWANGMYUNG_20240418_THEME_PROXY_COUNTER | 017040 | current_profile_should_block_actionable_on_source_proxy_only | yes |
| C02_R1L139_CASE_007_DAEWON_20240520_CABLE_THEME_LATE_COUNTER | 006340 | current_profile_should_keep_price_only_cable_proxy_out_of_positive_promotion | no |

Residual: the current profile is directionally correct on true C02 bridge cases, but should be stricter on source-proxy entries and late-after-rerating entries.

## 19. Shadow Rule Candidate

```text
rule_id = C02_verified_backlog_ASP_capacity_margin_bridge_before_actionable_or_yellow
scope = canonical_archetype_id == C02_POWER_GRID_DATACENTER_CAPEX
action = require firm-specific non-price bridge for Actionable/Yellow; keep source-proxy and late price-only rows in Stage1-Watch or local 4B-Watch
do_not_lower_stage3_green = true
production_scoring_changed = false
```

## 20. Score-Return Alignment Summary

| trigger_row_count | calibration_usable_trigger_count | unique_symbol_count | positive_case_count | counterexample_count | stage4b_case_count | avg_positive_MFE_90D_pct | avg_positive_MAE_90D_pct | avg_counter_MFE_90D_pct | avg_counter_MAE_90D_pct | current_profile_error_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 7 | 7 | 6 | 4 | 3 | 2 | 118.08 | -9.35 | 22.41 | -41.37 | 2 |

## 21. Residual Contribution Summary

```json
{
  "batch_ingest_action": "eligible_for_later_batch_review",
  "canonical_archetype_id": "C02_POWER_GRID_DATACENTER_CAPEX",
  "dominant_counter_mechanism": "theme/proxy or late after price rerating without fresh firm-specific bridge",
  "dominant_positive_mechanism": "company-specific backlog/order visibility plus ASP/capacity/margin bridge in transformers/power equipment",
  "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID",
  "recommended_patch_scope": "canonical_archetype_specific_C02_only",
  "residual_error_type": [
    "source_proxy_false_positive",
    "late_price_after_valid_thesis_high_mae",
    "margin_gap_blocks_green"
  ],
  "row_type": "residual_contribution",
  "selected_loop": 139,
  "selected_round": "R1"
}
```

## 22. Machine-Readable Case Rows JSONL

```jsonl
{"case_id": "C02_R1L139_CASE_001_HDHE_20240216_STRUCTURAL_ASP_BACKLOG", "case_role": "positive", "case_summary": "2023 revenue and operating profit surged, with 1Q24 margin expected to improve on higher ASP and stabilizing cost ratio; use as confirmed ASP/margin bridge, not merely price momentum.", "company_name": "HD현대일렉트릭", "dedupe_key": "C02_POWER_GRID_DATACENTER_CAPEX|267260|Stage2-Actionable|2024-02-16", "row_type": "case", "symbol": "267260", "usable_for_counterexample": false, "usable_for_promotion": true}
{"case_id": "C02_R1L139_CASE_002_JERYONG_20240308_EXPORT_BACKLOG_CAPA", "case_role": "positive", "case_summary": "Yuanta-style research reported distribution-transformer purity, export mix jump, 2023 earnings surge, 3Q23 backlog KRW323.1bn and high-margin 2024 outlook.", "company_name": "제룡전기", "dedupe_key": "C02_POWER_GRID_DATACENTER_CAPEX|033100|Stage2-Actionable|2024-03-08", "row_type": "case", "symbol": "033100", "usable_for_counterexample": false, "usable_for_promotion": true}
{"case_id": "C02_R1L139_CASE_003_JERYONG_20240529_LATE_PRICE_4B_WATCH", "case_role": "counterexample", "case_summary": "Later article still showed strong 1Q24 revenue/profit and backlog, but entry after rerating produced large 90/180D MAE; this is a local 4B watch/entry-risk row, not a thesis-failure 4C.", "company_name": "제룡전기", "dedupe_key": "C02_POWER_GRID_DATACENTER_CAPEX|033100|Stage4B|2024-05-29", "row_type": "case", "symbol": "033100", "usable_for_counterexample": true, "usable_for_promotion": false}
{"case_id": "C02_R1L139_CASE_004_HYOSUNG_20241101_LARGE_BACKLOG_OVERSEAS", "case_role": "positive", "case_summary": "3Q24 review showed operating profit beat and heavy-industry transformer demand backdrop; later 2025 source confirms 2024 backlog quality, US/Europe mix and capacity expansion bridge.", "company_name": "효성중공업", "dedupe_key": "C02_POWER_GRID_DATACENTER_CAPEX|298040|Stage2-Actionable|2024-11-01", "row_type": "case", "symbol": "298040", "usable_for_counterexample": false, "usable_for_promotion": true}
{"case_id": "C02_R1L139_CASE_005_ILJIN_20241115_BACKLOG_WITH_MARGIN_GAP", "case_role": "positive_mixed", "case_summary": "3Q24 revenue beat and backlog high, but operating profit declined YoY and OP margin was only 4.4%; C02 should accept backlog but require margin bridge before Green.", "company_name": "일진전기", "dedupe_key": "C02_POWER_GRID_DATACENTER_CAPEX|103590|Stage2-Actionable|2024-11-15", "row_type": "case", "symbol": "103590", "usable_for_counterexample": false, "usable_for_promotion": true}
{"case_id": "C02_R1L139_CASE_006_KWANGMYUNG_20240418_THEME_PROXY_COUNTER", "case_role": "counterexample", "case_summary": "Theme article tied the stock to AI/data-center power demand and noted prior Samsung P4 switchgear contracts, but the 2024 trigger lacked fresh company-level backlog/ASP/capacity bridge.", "company_name": "광명전기", "dedupe_key": "C02_POWER_GRID_DATACENTER_CAPEX|017040|Stage2|2024-04-18", "row_type": "case", "symbol": "017040", "usable_for_counterexample": true, "usable_for_promotion": false}
{"case_id": "C02_R1L139_CASE_007_DAEWON_20240520_CABLE_THEME_LATE_COUNTER", "case_role": "counterexample", "case_summary": "Sector article showed cable industry/global demand strength, but this row uses Daewon as a basket/proxy candidate after a sharp rerating; without firm-specific backlog bridge it must remain 4B watch or reject for promotion.", "company_name": "대원전선", "dedupe_key": "C02_POWER_GRID_DATACENTER_CAPEX|006340|Stage4B|2024-05-20", "row_type": "case", "symbol": "006340", "usable_for_counterexample": true, "usable_for_promotion": false}
```

## 23. Machine-Readable Trigger Rows JSONL

```jsonl
{"MAE_180D_date": "2024-02-16", "MAE_180D_pct": -0.52, "MAE_180D_price": 115300, "MAE_30D_date": "2024-02-16", "MAE_30D_pct": -0.52, "MAE_30D_price": 115300, "MAE_90D_date": "2024-02-16", "MAE_90D_pct": -0.52, "MAE_90D_price": 115300, "MFE_180D_date": "2024-11-12", "MFE_180D_pct": 256.77, "MFE_180D_price": 413500, "MFE_30D_date": "2024-03-28", "MFE_30D_pct": 59.62, "MFE_30D_price": 185000, "MFE_90D_date": "2024-06-28", "MFE_90D_pct": 179.12, "MFE_90D_price": 323500, "below_entry_180D": true, "blocked_reason": null, "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "calibration_usable": true, "canonical_archetype_id": "C02_POWER_GRID_DATACENTER_CAPEX", "case_id": "C02_R1L139_CASE_001_HDHE_20240216_STRUCTURAL_ASP_BACKLOG", "case_role": "positive", "company_name": "HD현대일렉트릭", "corporate_action_candidate_dates": ["2017-11-17", "2017-11-28", "2017-12-11", "2018-11-23", "2018-12-18", "2019-12-30"], "corporate_action_clean_180D": true, "current_profile_verdict": "correct_stage2_actionable_accept", "dedupe_key": "C02_POWER_GRID_DATACENTER_CAPEX|267260|Stage2-Actionable|2024-02-16", "deep_sub_archetype_id": "C02_DEEP_HIGH_VOLTAGE_TRANSFORMER_US_ASP_COST_RATIO_VISIBILITY", "drawdown_after_peak_pct": -8.46, "drawdown_after_peak_trough_date": "2024-11-12", "drawdown_after_peak_trough_price": 378500, "entry_date": "2024-02-16", "entry_price": 115900, "entry_price_basis": "close_on_entry_date", "evidence_date": "2024-02-16", "evidence_family": "verified_earnings_visibility_asp_margin_bridge", "evidence_source_id": "SRC_HDHE_2024_02_16", "evidence_summary": "2023 revenue and operating profit surged, with 1Q24 margin expected to improve on higher ASP and stabilizing cost ratio; use as confirmed ASP/margin bridge, not merely price momentum.", "evidence_url": "https://securities.miraeasset.com/bbs/download/2122467.pdf?attachmentId=2122467", "fine_archetype_id": "C02_GRID_TRANSFORMER_ASP_MARGIN_EARNINGS_VISIBILITY_BRIDGE", "forward_window_180D_trading_rows": 180, "forward_window_30D_trading_rows": 30, "forward_window_90D_trading_rows": 90, "forward_window_trading_days": 180, "independent_evidence_weight": 1.0, "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "market": "KOSPI", "new_symbol_for_c02": true, "not_representative_for_aggregate": false, "peak_date_180D": "2024-11-12", "peak_price_180D": 413500, "price_adjustment_status": "raw_unadjusted_marcap", "price_basis": "tradable_raw", "price_data_source": "Songdaiki/stock-web", "profile_path": "atlas/symbol_profiles/267/267260.json", "research_version": "v12", "row_type": "trigger", "selected_loop": 139, "selected_round": "R1", "stock_web_manifest_max_date": "2026-02-20", "symbol": "267260", "tradable_shard_paths": ["atlas/ohlcv_tradable_by_symbol_year/267/267260/2024.csv"], "trigger_date": "2024-02-16", "trigger_type": "Stage2-Actionable", "upstream_source": "FinanceData/marcap", "window_end_180D": "2024-11-12", "window_end_30D": "2024-03-29", "window_end_90D": "2024-06-28"}
{"MAE_180D_date": "2024-03-08", "MAE_180D_pct": -7.68, "MAE_180D_price": 30050, "MAE_30D_date": "2024-03-08", "MAE_30D_pct": -7.68, "MAE_30D_price": 30050, "MAE_90D_date": "2024-03-08", "MAE_90D_pct": -7.68, "MAE_90D_price": 30050, "MFE_180D_date": "2024-07-11", "MFE_180D_pct": 209.37, "MFE_180D_price": 100700, "MFE_30D_date": "2024-04-12", "MFE_30D_pct": 73.58, "MFE_30D_price": 56500, "MFE_90D_date": "2024-07-11", "MFE_90D_pct": 209.37, "MFE_90D_price": 100700, "below_entry_180D": true, "blocked_reason": null, "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "calibration_usable": true, "canonical_archetype_id": "C02_POWER_GRID_DATACENTER_CAPEX", "case_id": "C02_R1L139_CASE_002_JERYONG_20240308_EXPORT_BACKLOG_CAPA", "case_role": "positive", "company_name": "제룡전기", "corporate_action_candidate_dates": ["1999-11-30", "1999-12-27", "2000-02-21", "2000-08-30", "2006-01-06", "2007-08-31", "2011-11-28", "2014-11-06"], "corporate_action_clean_180D": true, "current_profile_verdict": "correct_stage2_actionable_accept_but_4b_watch_needed_after_peak", "dedupe_key": "C02_POWER_GRID_DATACENTER_CAPEX|033100|Stage2-Actionable|2024-03-08", "deep_sub_archetype_id": "C02_DEEP_US_DISTRIBUTION_TRANSFORMER_EXPORT_MIX_BACKLOG_OPM_38", "drawdown_after_peak_pct": -61.07, "drawdown_after_peak_trough_date": "2024-12-02", "drawdown_after_peak_trough_price": 39200, "entry_date": "2024-03-08", "entry_price": 32550, "entry_price_basis": "close_on_entry_date", "evidence_date": "2024-03-08", "evidence_family": "distribution_transformer_backlog_export_asp_bridge", "evidence_source_id": "SRC_JERYONG_YUANTA_2024_03_08", "evidence_summary": "Yuanta-style research reported distribution-transformer purity, export mix jump, 2023 earnings surge, 3Q23 backlog KRW323.1bn and high-margin 2024 outlook.", "evidence_url": "https://www.myasset.com/myasset/research/rs_list/rs_view.cmd?SEQ=193547&cd006=&cd007=RE01&cd008=", "fine_archetype_id": "C02_DISTRIBUTION_TRANSFORMER_EXPORT_BACKLOG_OPM_BRIDGE", "forward_window_180D_trading_rows": 180, "forward_window_30D_trading_rows": 30, "forward_window_90D_trading_rows": 90, "forward_window_trading_days": 180, "independent_evidence_weight": 1.0, "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "market": "KOSDAQ", "new_symbol_for_c02": true, "not_representative_for_aggregate": false, "peak_date_180D": "2024-07-11", "peak_price_180D": 100700, "price_adjustment_status": "raw_unadjusted_marcap", "price_basis": "tradable_raw", "price_data_source": "Songdaiki/stock-web", "profile_path": "atlas/symbol_profiles/033/033100.json", "research_version": "v12", "row_type": "trigger", "selected_loop": 139, "selected_round": "R1", "stock_web_manifest_max_date": "2026-02-20", "symbol": "033100", "tradable_shard_paths": ["atlas/ohlcv_tradable_by_symbol_year/033/033100/2024.csv"], "trigger_date": "2024-03-08", "trigger_type": "Stage2-Actionable", "upstream_source": "FinanceData/marcap", "window_end_180D": "2024-12-02", "window_end_30D": "2024-04-19", "window_end_90D": "2024-07-18"}
{"MAE_180D_date": "2024-12-09", "MAE_180D_pct": -50.54, "MAE_180D_price": 36550, "MAE_30D_date": "2024-06-10", "MAE_30D_pct": -17.73, "MAE_30D_price": 60800, "MAE_90D_date": "2024-09-09", "MAE_90D_pct": -41.54, "MAE_90D_price": 43200, "MFE_180D_date": "2024-07-11", "MFE_180D_pct": 36.27, "MFE_180D_price": 100700, "MFE_30D_date": "2024-07-10", "MFE_30D_pct": 35.05, "MFE_30D_price": 99800, "MFE_90D_date": "2024-07-11", "MFE_90D_pct": 36.27, "MFE_90D_price": 100700, "below_entry_180D": true, "blocked_reason": null, "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "calibration_usable": true, "canonical_archetype_id": "C02_POWER_GRID_DATACENTER_CAPEX", "case_id": "C02_R1L139_CASE_003_JERYONG_20240529_LATE_PRICE_4B_WATCH", "case_role": "counterexample", "company_name": "제룡전기", "corporate_action_candidate_dates": ["1999-11-30", "1999-12-27", "2000-02-21", "2000-08-30", "2006-01-06", "2007-08-31", "2011-11-28", "2014-11-06"], "corporate_action_clean_180D": true, "current_profile_verdict": "current_profile_needs_local_4b_watch_after_fast_rerating", "dedupe_key": "C02_POWER_GRID_DATACENTER_CAPEX|033100|Stage4B|2024-05-29", "deep_sub_archetype_id": "C02_DEEP_SUCCESSFUL_BACKLOG_BUT_PRICE_RAN_AHEAD_MAE_GUARD", "drawdown_after_peak_pct": -63.7, "drawdown_after_peak_trough_date": "2024-12-09", "drawdown_after_peak_trough_price": 36550, "entry_date": "2024-05-29", "entry_price": 73900, "entry_price_basis": "close_on_entry_date", "evidence_date": "2024-05-29", "evidence_family": "late_price_after_success_high_mae_guardrail", "evidence_source_id": "SRC_JERYONG_NEWS_2024_05_29", "evidence_summary": "Later article still showed strong 1Q24 revenue/profit and backlog, but entry after rerating produced large 90/180D MAE; this is a local 4B watch/entry-risk row, not a thesis-failure 4C.", "evidence_url": "https://www.thebigdata.co.kr/view.php?ud=202405290538457085cd1e7f0bdf_23", "fine_archetype_id": "C02_DISTRIBUTION_TRANSFORMER_LATE_ENTRY_4B_WATCH_AFTER_EVIDENCE_SUCCESS", "forward_window_180D_trading_rows": 180, "forward_window_30D_trading_rows": 30, "forward_window_90D_trading_rows": 90, "forward_window_trading_days": 180, "independent_evidence_weight": 0.5, "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "market": "KOSDAQ", "new_symbol_for_c02": true, "not_representative_for_aggregate": false, "peak_date_180D": "2024-07-11", "peak_price_180D": 100700, "price_adjustment_status": "raw_unadjusted_marcap", "price_basis": "tradable_raw", "price_data_source": "Songdaiki/stock-web", "profile_path": "atlas/symbol_profiles/033/033100.json", "research_version": "v12", "row_type": "trigger", "selected_loop": 139, "selected_round": "R1", "stock_web_manifest_max_date": "2026-02-20", "symbol": "033100", "tradable_shard_paths": ["atlas/ohlcv_tradable_by_symbol_year/033/033100/2024.csv", "atlas/ohlcv_tradable_by_symbol_year/033/033100/2025.csv"], "trigger_date": "2024-05-29", "trigger_type": "Stage4B", "upstream_source": "FinanceData/marcap", "window_end_180D": "2025-02-25", "window_end_30D": "2024-07-10", "window_end_90D": "2024-10-11"}
{"MAE_180D_date": "2024-12-24", "MAE_180D_pct": -12.34, "MAE_180D_price": 366000, "MAE_30D_date": "2024-11-26", "MAE_30D_pct": -8.5, "MAE_30D_price": 382000, "MAE_90D_date": "2024-12-24", "MAE_90D_pct": -12.34, "MAE_90D_price": 366000, "MFE_180D_date": "2025-07-28", "MFE_180D_pct": 224.79, "MFE_180D_price": 1356000, "MFE_30D_date": "2024-11-12", "MFE_30D_pct": 24.07, "MFE_30D_price": 518000, "MFE_90D_date": "2025-02-06", "MFE_90D_pct": 31.5, "MFE_90D_price": 549000, "below_entry_180D": true, "blocked_reason": null, "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "calibration_usable": true, "canonical_archetype_id": "C02_POWER_GRID_DATACENTER_CAPEX", "case_id": "C02_R1L139_CASE_004_HYOSUNG_20241101_LARGE_BACKLOG_OVERSEAS", "case_role": "positive", "company_name": "효성중공업", "corporate_action_candidate_dates": [], "corporate_action_clean_180D": true, "current_profile_verdict": "correct_stage2_actionable_accept", "dedupe_key": "C02_POWER_GRID_DATACENTER_CAPEX|298040|Stage2-Actionable|2024-11-01", "deep_sub_archetype_id": "C02_DEEP_US_EUROPE_EHV_TRANSFORMER_ORDER_BACKLOG_CAPACITY_EXPANSION", "drawdown_after_peak_pct": -7.37, "drawdown_after_peak_trough_date": "2025-07-29", "drawdown_after_peak_trough_price": 1256000, "entry_date": "2024-11-01", "entry_price": 417500, "entry_price_basis": "close_on_entry_date", "evidence_date": "2024-11-01", "evidence_family": "large_backlog_overseas_high_voltage_transformer_bridge", "evidence_source_id": "SRC_HYOSUNG_MIRAE_2024_11_01", "evidence_summary": "3Q24 review showed operating profit beat and heavy-industry transformer demand backdrop; later 2025 source confirms 2024 backlog quality, US/Europe mix and capacity expansion bridge.", "evidence_url": "https://securities.miraeasset.com/newir/view/pc/en/investor/researchReportsView.jsp?messageId=2328068", "fine_archetype_id": "C02_HIGH_VOLTAGE_TRANSFORMER_OVERSEAS_BACKLOG_CAPACITY_BRIDGE", "forward_window_180D_trading_rows": 180, "forward_window_30D_trading_rows": 30, "forward_window_90D_trading_rows": 90, "forward_window_trading_days": 180, "independent_evidence_weight": 1.0, "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "market": "KOSPI", "new_symbol_for_c02": true, "not_representative_for_aggregate": false, "peak_date_180D": "2025-07-28", "peak_price_180D": 1356000, "price_adjustment_status": "raw_unadjusted_marcap", "price_basis": "tradable_raw", "price_data_source": "Songdaiki/stock-web", "profile_path": "atlas/symbol_profiles/298/298040.json", "research_version": "v12", "row_type": "trigger", "selected_loop": 139, "selected_round": "R1", "stock_web_manifest_max_date": "2026-02-20", "symbol": "298040", "tradable_shard_paths": ["atlas/ohlcv_tradable_by_symbol_year/298/298040/2024.csv", "atlas/ohlcv_tradable_by_symbol_year/298/298040/2025.csv"], "trigger_date": "2024-11-01", "trigger_type": "Stage2-Actionable", "upstream_source": "FinanceData/marcap", "window_end_180D": "2025-07-29", "window_end_30D": "2024-12-12", "window_end_90D": "2025-03-18"}
{"MAE_180D_date": "2025-04-09", "MAE_180D_pct": -19.68, "MAE_180D_price": 19800, "MAE_30D_date": "2024-11-29", "MAE_30D_pct": -16.84, "MAE_30D_price": 20500, "MAE_90D_date": "2024-11-29", "MAE_90D_pct": -16.84, "MAE_90D_price": 20500, "MFE_180D_date": "2025-07-29", "MFE_180D_pct": 80.12, "MFE_180D_price": 44400, "MFE_30D_date": "2024-12-18", "MFE_30D_pct": 15.42, "MFE_30D_price": 28450, "MFE_90D_date": "2025-01-24", "MFE_90D_pct": 52.33, "MFE_90D_price": 37550, "below_entry_180D": true, "blocked_reason": null, "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "calibration_usable": true, "canonical_archetype_id": "C02_POWER_GRID_DATACENTER_CAPEX", "case_id": "C02_R1L139_CASE_005_ILJIN_20241115_BACKLOG_WITH_MARGIN_GAP", "case_role": "positive_mixed", "company_name": "일진전기", "corporate_action_candidate_dates": ["2024-02-13"], "corporate_action_clean_180D": true, "current_profile_verdict": "correct_stage2_but_green_blocked_until_margin_bridge", "dedupe_key": "C02_POWER_GRID_DATACENTER_CAPEX|103590|Stage2-Actionable|2024-11-15", "deep_sub_archetype_id": "C02_DEEP_RECORD_BACKLOG_EXPORT_MIX_WITH_OPM_GAP_AND_ONE_OFF_ADJUSTMENT", "drawdown_after_peak_pct": -10.36, "drawdown_after_peak_trough_date": "2025-08-12", "drawdown_after_peak_trough_price": 39800, "entry_date": "2024-11-15", "entry_price": 24650, "entry_price_basis": "close_on_entry_date", "evidence_date": "2024-11-15", "evidence_family": "record_backlog_but_margin_bridge_watch", "evidence_source_id": "SRC_ILJIN_MIRAE_2024_11_15", "evidence_summary": "3Q24 revenue beat and backlog high, but operating profit declined YoY and OP margin was only 4.4%; C02 should accept backlog but require margin bridge before Green.", "evidence_url": "https://securities.miraeasset.com/bbs/download/2132362.pdf?attachmentId=2132362", "fine_archetype_id": "C02_HEAVY_ELECTRICAL_BACKLOG_MARGIN_GAP_STAGE2_ONLY", "forward_window_180D_trading_rows": 180, "forward_window_30D_trading_rows": 30, "forward_window_90D_trading_rows": 90, "forward_window_trading_days": 180, "independent_evidence_weight": 1.0, "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "market": "KOSPI", "new_symbol_for_c02": true, "not_representative_for_aggregate": false, "peak_date_180D": "2025-07-29", "peak_price_180D": 44400, "price_adjustment_status": "raw_unadjusted_marcap", "price_basis": "tradable_raw", "price_data_source": "Songdaiki/stock-web", "profile_path": "atlas/symbol_profiles/103/103590.json", "research_version": "v12", "row_type": "trigger", "selected_loop": 139, "selected_round": "R1", "stock_web_manifest_max_date": "2026-02-20", "symbol": "103590", "tradable_shard_paths": ["atlas/ohlcv_tradable_by_symbol_year/103/103590/2024.csv", "atlas/ohlcv_tradable_by_symbol_year/103/103590/2025.csv"], "trigger_date": "2024-11-15", "trigger_type": "Stage2-Actionable", "upstream_source": "FinanceData/marcap", "window_end_180D": "2025-08-12", "window_end_30D": "2024-12-27", "window_end_90D": "2025-04-01"}
{"MAE_180D_date": "2024-10-31", "MAE_180D_pct": -53.53, "MAE_180D_price": 1250, "MAE_30D_date": "2024-05-30", "MAE_30D_pct": -15.43, "MAE_30D_price": 2275, "MAE_90D_date": "2024-08-05", "MAE_90D_pct": -40.0, "MAE_90D_price": 1614, "MFE_180D_date": "2024-05-08", "MFE_180D_pct": 23.42, "MFE_180D_price": 3320, "MFE_30D_date": "2024-05-08", "MFE_30D_pct": 23.42, "MFE_30D_price": 3320, "MFE_90D_date": "2024-05-08", "MFE_90D_pct": 23.42, "MFE_90D_price": 3320, "below_entry_180D": true, "blocked_reason": null, "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "calibration_usable": true, "canonical_archetype_id": "C02_POWER_GRID_DATACENTER_CAPEX", "case_id": "C02_R1L139_CASE_006_KWANGMYUNG_20240418_THEME_PROXY_COUNTER", "case_role": "counterexample", "company_name": "광명전기", "corporate_action_candidate_dates": ["2000-01-24", "2000-04-25", "2001-12-10"], "corporate_action_clean_180D": true, "current_profile_verdict": "current_profile_should_block_actionable_on_source_proxy_only", "dedupe_key": "C02_POWER_GRID_DATACENTER_CAPEX|017040|Stage2|2024-04-18", "deep_sub_archetype_id": "C02_DEEP_SEMICONDUCTOR_SWITCHGEAR_SINGLE_CONTRACT_HISTORY_VS_NO_CURRENT_BRIDGE", "drawdown_after_peak_pct": -62.35, "drawdown_after_peak_trough_date": "2024-10-31", "drawdown_after_peak_trough_price": 1250, "entry_date": "2024-04-18", "entry_price": 2690, "entry_price_basis": "close_on_entry_date", "evidence_date": "2024-04-18", "evidence_family": "price_only_sector_proxy_without_company_backlog_bridge", "evidence_source_id": "SRC_KWANGMYUNG_THEME_2024_04_18", "evidence_summary": "Theme article tied the stock to AI/data-center power demand and noted prior Samsung P4 switchgear contracts, but the 2024 trigger lacked fresh company-level backlog/ASP/capacity bridge.", "evidence_url": "https://www.thebigdata.co.kr/view.php?ud=202404180550415310cd1e7f0bdf_23", "fine_archetype_id": "C02_SWITCHGEAR_THEME_PROXY_NO_FRESH_BACKLOG_BRIDGE", "forward_window_180D_trading_rows": 180, "forward_window_30D_trading_rows": 30, "forward_window_90D_trading_rows": 90, "forward_window_trading_days": 180, "independent_evidence_weight": 1.0, "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "market": "KOSPI", "new_symbol_for_c02": true, "not_representative_for_aggregate": false, "peak_date_180D": "2024-05-08", "peak_price_180D": 3320, "price_adjustment_status": "raw_unadjusted_marcap", "price_basis": "tradable_raw", "price_data_source": "Songdaiki/stock-web", "profile_path": "atlas/symbol_profiles/017/017040.json", "research_version": "v12", "row_type": "trigger", "selected_loop": 139, "selected_round": "R1", "stock_web_manifest_max_date": "2026-02-20", "symbol": "017040", "tradable_shard_paths": ["atlas/ohlcv_tradable_by_symbol_year/017/017040/2024.csv", "atlas/ohlcv_tradable_by_symbol_year/017/017040/2025.csv"], "trigger_date": "2024-04-18", "trigger_type": "Stage2", "upstream_source": "FinanceData/marcap", "window_end_180D": "2025-01-14", "window_end_30D": "2024-06-03", "window_end_90D": "2024-08-28"}
{"MAE_180D_date": "2024-12-09", "MAE_180D_pct": -50.34, "MAE_180D_price": 2205, "MAE_30D_date": "2024-06-10", "MAE_30D_pct": -26.01, "MAE_30D_price": 3285, "MAE_90D_date": "2024-09-09", "MAE_90D_pct": -42.57, "MAE_90D_price": 2550, "MFE_180D_date": "2024-06-28", "MFE_180D_pct": 7.55, "MFE_180D_price": 4775, "MFE_30D_date": "2024-06-28", "MFE_30D_pct": 7.55, "MFE_30D_price": 4775, "MFE_90D_date": "2024-06-28", "MFE_90D_pct": 7.55, "MFE_90D_price": 4775, "below_entry_180D": true, "blocked_reason": null, "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "calibration_usable": true, "canonical_archetype_id": "C02_POWER_GRID_DATACENTER_CAPEX", "case_id": "C02_R1L139_CASE_007_DAEWON_20240520_CABLE_THEME_LATE_COUNTER", "case_role": "counterexample", "company_name": "대원전선", "corporate_action_candidate_dates": ["1996-11-29", "1997-06-19", "1999-09-10", "2000-03-21", "2007-01-25", "2010-05-07"], "corporate_action_clean_180D": true, "current_profile_verdict": "current_profile_should_keep_price_only_cable_proxy_out_of_positive_promotion", "dedupe_key": "C02_POWER_GRID_DATACENTER_CAPEX|006340|Stage4B|2024-05-20", "deep_sub_archetype_id": "C02_DEEP_CABLE_BASKET_PRICE_ONLY_SUPERCYCLE_PROXY_WITHOUT_BACKLOG_QUALITY", "drawdown_after_peak_pct": -53.82, "drawdown_after_peak_trough_date": "2024-12-09", "drawdown_after_peak_trough_price": 2205, "entry_date": "2024-05-20", "entry_price": 4440, "entry_price_basis": "close_on_entry_date", "evidence_date": "2024-05-20", "evidence_family": "sector_proxy_cable_after_theme_run_high_mae", "evidence_source_id": "SRC_DAEWON_CABLE_SECTOR_2024_05_20", "evidence_summary": "Sector article showed cable industry/global demand strength, but this row uses Daewon as a basket/proxy candidate after a sharp rerating; without firm-specific backlog bridge it must remain 4B watch or reject for promotion.", "evidence_url": "https://pulse.mk.co.kr/news/english/11019506", "fine_archetype_id": "C02_CABLE_SECTOR_PROXY_AFTER_PRICE_RUN_LOCAL_4B_WATCH", "forward_window_180D_trading_rows": 180, "forward_window_30D_trading_rows": 30, "forward_window_90D_trading_rows": 90, "forward_window_trading_days": 180, "independent_evidence_weight": 1.0, "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "market": "KOSPI", "new_symbol_for_c02": true, "not_representative_for_aggregate": false, "peak_date_180D": "2024-06-28", "peak_price_180D": 4775, "price_adjustment_status": "raw_unadjusted_marcap", "price_basis": "tradable_raw", "price_data_source": "Songdaiki/stock-web", "profile_path": "atlas/symbol_profiles/006/006340.json", "research_version": "v12", "row_type": "trigger", "selected_loop": 139, "selected_round": "R1", "stock_web_manifest_max_date": "2026-02-20", "symbol": "006340", "tradable_shard_paths": ["atlas/ohlcv_tradable_by_symbol_year/006/006340/2024.csv", "atlas/ohlcv_tradable_by_symbol_year/006/006340/2025.csv"], "trigger_date": "2024-05-20", "trigger_type": "Stage4B", "upstream_source": "FinanceData/marcap", "window_end_180D": "2025-02-14", "window_end_30D": "2024-07-01", "window_end_90D": "2024-09-27"}
```

## 24. Machine-Readable Score Simulation Rows JSONL

```jsonl
{"baseline_current_proxy_stage": "Stage3-Yellow", "baseline_current_proxy_total_score": 79.4, "canonical_archetype_id": "C02_POWER_GRID_DATACENTER_CAPEX", "case_id": "C02_R1L139_CASE_001_HDHE_20240216_STRUCTURAL_ASP_BACKLOG", "current_profile_verdict": "correct_stage2_actionable_accept", "raw_component_scores": {"bottleneck": 84, "evidence": 88, "quality": 80, "revision": 78, "risk": 42, "valuation": 57, "visibility": 86}, "row_type": "score_simulation", "shadow_adjustment_axis": "C02_backlog_ASP_capacity_margin_bridge_and_price_only_4B_guard", "shadow_rule_stage": "Stage3-Yellow", "shadow_rule_total_score": 83.2, "symbol": "267260"}
{"baseline_current_proxy_stage": "Stage3-Yellow", "baseline_current_proxy_total_score": 77.8, "canonical_archetype_id": "C02_POWER_GRID_DATACENTER_CAPEX", "case_id": "C02_R1L139_CASE_002_JERYONG_20240308_EXPORT_BACKLOG_CAPA", "current_profile_verdict": "correct_stage2_actionable_accept_but_4b_watch_needed_after_peak", "raw_component_scores": {"bottleneck": 88, "evidence": 86, "quality": 73, "revision": 76, "risk": 48, "valuation": 50, "visibility": 82}, "row_type": "score_simulation", "shadow_adjustment_axis": "C02_backlog_ASP_capacity_margin_bridge_and_price_only_4B_guard", "shadow_rule_stage": "Stage3-Yellow", "shadow_rule_total_score": 81.0, "symbol": "033100"}
{"baseline_current_proxy_stage": "Stage3-Yellow", "baseline_current_proxy_total_score": 77.0, "canonical_archetype_id": "C02_POWER_GRID_DATACENTER_CAPEX", "case_id": "C02_R1L139_CASE_003_JERYONG_20240529_LATE_PRICE_4B_WATCH", "current_profile_verdict": "current_profile_needs_local_4b_watch_after_fast_rerating", "raw_component_scores": {"bottleneck": 86, "evidence": 84, "quality": 73, "revision": 76, "risk": 72, "valuation": 30, "visibility": 82}, "row_type": "score_simulation", "shadow_adjustment_axis": "C02_backlog_ASP_capacity_margin_bridge_and_price_only_4B_guard", "shadow_rule_stage": "Stage4B-Watch", "shadow_rule_total_score": 69.5, "symbol": "033100"}
{"baseline_current_proxy_stage": "Stage3-Yellow", "baseline_current_proxy_total_score": 75.7, "canonical_archetype_id": "C02_POWER_GRID_DATACENTER_CAPEX", "case_id": "C02_R1L139_CASE_004_HYOSUNG_20241101_LARGE_BACKLOG_OVERSEAS", "current_profile_verdict": "correct_stage2_actionable_accept", "raw_component_scores": {"bottleneck": 82, "evidence": 82, "quality": 78, "revision": 72, "risk": 45, "valuation": 55, "visibility": 81}, "row_type": "score_simulation", "shadow_adjustment_axis": "C02_backlog_ASP_capacity_margin_bridge_and_price_only_4B_guard", "shadow_rule_stage": "Stage3-Yellow", "shadow_rule_total_score": 79.4, "symbol": "298040"}
{"baseline_current_proxy_stage": "Stage2-Actionable", "baseline_current_proxy_total_score": 73.0, "canonical_archetype_id": "C02_POWER_GRID_DATACENTER_CAPEX", "case_id": "C02_R1L139_CASE_005_ILJIN_20241115_BACKLOG_WITH_MARGIN_GAP", "current_profile_verdict": "correct_stage2_but_green_blocked_until_margin_bridge", "raw_component_scores": {"bottleneck": 78, "evidence": 78, "quality": 64, "revision": 63, "risk": 60, "valuation": 48, "visibility": 77}, "row_type": "score_simulation", "shadow_adjustment_axis": "C02_backlog_ASP_capacity_margin_bridge_and_price_only_4B_guard", "shadow_rule_stage": "Stage2-Actionable", "shadow_rule_total_score": 74.6, "symbol": "103590"}
{"baseline_current_proxy_stage": "Stage2", "baseline_current_proxy_total_score": 62.0, "canonical_archetype_id": "C02_POWER_GRID_DATACENTER_CAPEX", "case_id": "C02_R1L139_CASE_006_KWANGMYUNG_20240418_THEME_PROXY_COUNTER", "current_profile_verdict": "current_profile_should_block_actionable_on_source_proxy_only", "raw_component_scores": {"bottleneck": 45, "evidence": 39, "quality": 38, "revision": 28, "risk": 78, "valuation": 34, "visibility": 35}, "row_type": "score_simulation", "shadow_adjustment_axis": "C02_backlog_ASP_capacity_margin_bridge_and_price_only_4B_guard", "shadow_rule_stage": "Stage1-Watch", "shadow_rule_total_score": 53.5, "symbol": "017040"}
{"baseline_current_proxy_stage": "Stage2", "baseline_current_proxy_total_score": 60.5, "canonical_archetype_id": "C02_POWER_GRID_DATACENTER_CAPEX", "case_id": "C02_R1L139_CASE_007_DAEWON_20240520_CABLE_THEME_LATE_COUNTER", "current_profile_verdict": "current_profile_should_keep_price_only_cable_proxy_out_of_positive_promotion", "raw_component_scores": {"bottleneck": 52, "evidence": 34, "quality": 36, "revision": 25, "risk": 82, "valuation": 26, "visibility": 33}, "row_type": "score_simulation", "shadow_adjustment_axis": "C02_backlog_ASP_capacity_margin_bridge_and_price_only_4B_guard", "shadow_rule_stage": "Stage4B-Watch/No-Promotion", "shadow_rule_total_score": 49.0, "symbol": "006340"}
```

## 25. Machine-Readable Aggregate / Shadow / Residual Rows JSONL

```jsonl
{"avg_counter_MAE_90D_pct": -41.37, "avg_counter_MFE_90D_pct": 22.41, "avg_positive_MAE_90D_pct": -9.35, "avg_positive_MFE_90D_pct": 118.08, "calibration_usable_trigger_count": 7, "canonical_archetype_id": "C02_POWER_GRID_DATACENTER_CAPEX", "counterexample_count": 3, "current_profile_error_count": 2, "deep_sub_archetype_id": "C02_DEEP_US_GRID_DATACENTER_TRANSFORMER_ASP_CAPA_LOCK_VS_PRICE_ONLY_THEME_PROXY", "fine_archetype_id": "C02_GRID_TRANSFORMER_DATACENTER_CAPEX_BACKLOG_ASP_CAPACITY_BRIDGE", "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "new_symbol_count_for_c02": 6, "new_symbols_for_c02": ["006340", "017040", "033100", "103590", "267260", "298040"], "positive_case_count": 4, "production_scoring_changed": false, "row_type": "aggregate", "rule_candidate": "C02 requires verified order/backlog + ASP/capacity/margin bridge for Actionable/Yellow; source-proxy or late price-only cable/switchgear rows remain Stage1/Stage4B watch and no positive promotion.", "selected_loop": 139, "selected_round": "R1", "shadow_weight_only": true, "source_proxy_only_count": 2, "stage4b_case_count": 2, "trigger_row_count": 7, "unique_symbol_count": 6}
{"canonical_archetype_id": "C02_POWER_GRID_DATACENTER_CAPEX", "do_not_apply_now": true, "existing_axis_strengthened": ["stage2_required_bridge", "local_4b_watch_guard", "price_only_blowoff_blocks_positive_stage"], "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "new_axis_candidate": "C02_verified_backlog_ASP_capacity_margin_bridge_before_actionable_or_yellow", "proposal_type": "scope_limited_shadow_rule_candidate", "risk_note": "Do not loosen Stage3-Green threshold. C02 winners can show large MFE, but late entries can also suffer 40~75% MAE; Green still needs revision/margin confirmation.", "row_type": "shadow_weight", "selected_loop": 139, "selected_round": "R1", "suggested_directional_effect": "increase evidence/visibility/bottleneck weight only when firm-specific order backlog, ASP/capacity or margin bridge are present; penalize source_proxy_only and late price-only entries."}
{"batch_ingest_action": "eligible_for_later_batch_review", "canonical_archetype_id": "C02_POWER_GRID_DATACENTER_CAPEX", "dominant_counter_mechanism": "theme/proxy or late after price rerating without fresh firm-specific bridge", "dominant_positive_mechanism": "company-specific backlog/order visibility plus ASP/capacity/margin bridge in transformers/power equipment", "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "recommended_patch_scope": "canonical_archetype_specific_C02_only", "residual_error_type": ["source_proxy_false_positive", "late_price_after_valid_thesis_high_mae", "margin_gap_blocks_green"], "row_type": "residual_contribution", "selected_loop": 139, "selected_round": "R1"}
```

## 26. Validation Scope / Batch-Ingest Self Audit

| gate | status | detail |
| --- | --- | --- |
| standard_v12_filename | pass | e2r_stock_web_v12_residual_round_R1_loop_139_L1_INDUSTRIALS_INFRA_DEFENSE_GRID_C02_POWER_GRID_DATACENTER_CAPEX_research.md |
| selected_round_sector_consistency | pass | R1 / L1_INDUSTRIALS_INFRA_DEFENSE_GRID / C02 |
| actual_stock_web_ohlc_used | pass | all MFE/MAE computed from downloaded stock-web tradable symbol-year CSV shards |
| complete_30_90_180_mfe_mae | pass | all trigger rows include MFE/MAE 30D/90D/180D |
| corporate_action_contamination_180D | pass | no selected 2024~2025 entry window overlaps visible corporate_action_candidate_dates |
| positive_counterexample_balance | pass | positive/mixed=4, counterexample=3 |
| production_patch_written | pass | false |

## 27. Deferred Coding Agent Handoff Prompt

```text
You are a later batch implementation agent for stock_agent. Do not treat this MD as a live trading signal. Read all machine-readable JSONL blocks from this file. Validate filename/metadata consistency and stock-web price fields. If this row set survives batch aggregation with other V12 files, consider a scope-limited C02 rule candidate: require firm-specific order/backlog plus ASP/capacity/margin bridge before Stage2-Actionable/Stage3-Yellow; keep source-proxy and late price-only C02 rows in Stage1-Watch or local 4B-Watch. Do not lower Stage3-Green thresholds. Do not apply this single MD alone as a production scoring change.
```

## 28. Final Research State

```json
{
  "calibration_usable_trigger_count": 7,
  "canonical_archetype_id": "C02_POWER_GRID_DATACENTER_CAPEX",
  "canonical_archetype_rule_candidate": true,
  "completed_loop": 139,
  "completed_round": "R1",
  "counterexample_count": 3,
  "current_profile_error_count": 2,
  "existing_axis_strengthened": [
    "stage2_required_bridge",
    "local_4b_watch_guard"
  ],
  "fine_archetype_id": "C02_GRID_TRANSFORMER_DATACENTER_CAPEX_BACKLOG_ASP_CAPACITY_BRIDGE",
  "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID",
  "loop_objective": "coverage_gap_fill + C02 bridge/4B residual rule discovery",
  "new_axis_proposed": "C02_verified_backlog_ASP_capacity_margin_bridge_before_actionable_or_yellow",
  "new_independent_case_count": 6,
  "new_symbol_count": 6,
  "next_recommended_archetypes": [
    "C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF",
    "C14_EV_DEMAND_SLOWDOWN_4B_4C",
    "C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE",
    "C06_HBM_MEMORY_CUSTOMER_CAPACITY"
  ],
  "positive_case_count": 4,
  "reused_case_count": 1,
  "round_schedule_status": "coverage_index_selected",
  "round_sector_consistency": "pass",
  "sector_specific_rule_candidate": true,
  "selected_priority_bucket": "Priority 0",
  "selection_basis": "docs/core/V12_Research_No_Repeat_Index.md",
  "stock_web_manifest_max_date": "2026-02-20"
}
```
