---
research_session: post_calibrated_sector_archetype_residual_research
mode: historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12
selected_round: R1
selected_loop: 115
selection_basis: docs/core/V12_Research_No_Repeat_Index.md
selected_priority_bucket: Priority 0
round_schedule_status: coverage_index_selected
round_sector_consistency: pass
large_sector_id: L1_INDUSTRIALS_INFRA_DEFENSE_GRID
canonical_archetype_id: C01_ORDER_BACKLOG_MARGIN_BRIDGE
fine_archetype_id: C01_SHIPBUILDING_ENGINE_BACKLOG_MARGIN_FCF_CONVERSION_BRIDGE
deep_sub_archetype_id: C01_DEEP_KOREA_SHIPBUILDING_LNG_ENGINE_BACKLOG_TO_MARGIN_FCF_VS_ORDERBOOK_MEMORY
primary_price_source: Songdaiki/stock-web
price_basis: tradable_raw
price_adjustment_status: raw_unadjusted_marcap
stock_web_manifest_max_date: 2026-02-20
upstream_source: FinanceData/marcap
production_scoring_changed: false
shadow_weight_only: true
handoff_prompt_embedded: true
handoff_prompt_executed_now: false
created_at_kst: 2026-06-13T19:20:00+09:00
---

# E2R Stock-Web v12 Residual Research — R1 / C01 Order Backlog Margin Bridge

## 0. Executive Summary

This standalone Markdown file follows the v12 Stock-Web historical calibration prompt. It is a historical calibration artifact only: no live watchlist, no trading instruction, no production code patch, and no active scoring mutation.

- **Selected target:** `C01_ORDER_BACKLOG_MARGIN_BRIDGE`
- **Reason:** the No-Repeat coverage ledger places C01 in Priority 0 with 19 rows, still below the 30-row floor; earlier same-session outputs already covered C02/C09/C14/C10/C06/C07/C11.
- **Loop:** visible standard C01 archive reaches loop 114, so this artifact uses loop 115.
- **New independent cases:** 8
- **Usable trigger rows:** 9, including 1 local 4B overlay row.
- **Representative trigger rows:** 8
- **Positive cases:** 4
- **Counterexamples:** 4
- **Current profile residual errors:** 5
- **Rule candidate:** require verified backlog-to-margin/FCF/revision bridge before C01 can move to Yellow/Green; keep group-inherited backlog, supplier beta, M&A/vertical-integration synergy, and revenue-recognition delay cases in Watch unless entity-level conversion appears.

## 1. Stock-Web Price Source Validation

The run uses `Songdaiki/stock-web` tradable OHLCV shards, upstream `FinanceData/marcap`, raw/unadjusted OHLC, and manifest `max_date=2026-02-20`. Every calibration-usable trigger has a complete 180-trading-day forward window inside the manifest date.

```jsonl
{"row_type":"price_source_validation","source":"Songdaiki/stock-web","source_url":"https://github.com/Songdaiki/stock-web","manifest_path":"atlas/manifest.json","schema_path":"atlas/schema.json","universe_path":"atlas/universe/all_symbols.csv","manifest_max_date":"2026-02-20","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","calibration_shard_root":"atlas/ohlcv_tradable_by_symbol_year","raw_shard_root":"atlas/ohlcv_raw_by_symbol_year","validation_status":"usable_for_historical_calibration","upstream_source":"FinanceData/marcap"}
```

## 2. Coverage-Index Selection

C01 was selected by coverage gap, not by sequential round cycling. Earlier same-session artifacts filled C02, C09, C14, C10, C06, C07, and C11. The next remaining Priority 0 target is C01.

```json
{
  "selected_round": "R1",
  "selected_loop": 115,
  "selection_basis": "docs/core/V12_Research_No_Repeat_Index.md",
  "selected_priority_bucket": "Priority 0",
  "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID",
  "canonical_archetype_id": "C01_ORDER_BACKLOG_MARGIN_BRIDGE",
  "fine_archetype_id": "C01_SHIPBUILDING_ENGINE_BACKLOG_MARGIN_FCF_CONVERSION_BRIDGE",
  "deep_sub_archetype_id": "C01_DEEP_KOREA_SHIPBUILDING_LNG_ENGINE_BACKLOG_TO_MARGIN_FCF_VS_ORDERBOOK_MEMORY",
  "anti_repeat_key": "canonical_archetype_id + symbol + trigger_type + entry_date",
  "coverage_reason": "C01 has 19 rows in the No-Repeat Index, below the 30-row floor. Earlier same-session outputs covered C02, C09, C14, C10, C06, C07, and C11, so C01 is the next remaining Priority 0 target."
}
```

## 3. Hypothesis

C01 should not mean “the company has a backlog.” Backlog is a warehouse full of locked future work; the rerating only becomes investable when that warehouse has a working conveyor belt into revenue, margin, revision, and cash flow. The residual question is whether C01 can distinguish:
1. real backlog duration and order quality,
2. backlog-to-sales conversion,
3. margin bridge from vessel mix, cost normalization, or engine/supplier utilization,
4. FCF and working-capital confirmation, and
5. price extension that has outrun fresh non-price evidence.

In short: **backlog is the reservoir; margin/FCF is the pipe pressure.** C01 should score the water only when the pipe actually moves it.

## 4. Canonical Compression Map

```json
{
  "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID",
  "canonical_archetype_id": "C01_ORDER_BACKLOG_MARGIN_BRIDGE",
  "fine_archetype_id": "C01_SHIPBUILDING_ENGINE_BACKLOG_MARGIN_FCF_CONVERSION_BRIDGE",
  "deep_sub_archetype_id": "C01_DEEP_KOREA_SHIPBUILDING_LNG_ENGINE_BACKLOG_TO_MARGIN_FCF_VS_ORDERBOOK_MEMORY",
  "included_subtypes": [
    "shipbuilder_group_backlog_duration",
    "main_yard_margin_turnaround",
    "marine_engine_order_backlog",
    "LNG_insulation_supplier_order_margin_bridge",
    "offshore_wind_specialty_vessel_revenue_delay",
    "price_extension_local_4B_watch"
  ],
  "excluded_subtypes": [
    "C02_power_grid_or_datacenter_CAPEX_without_shipbuilding_backlog",
    "C03_defense_export_backlog_only",
    "C05_EPC_mega_contract_margin_gap_without_shipyard_backlog",
    "C32_control_premium_tender_or_MA_only"
  ]
}
```

## 5. Evidence Source Map

| Symbol | Company | Trigger evidence date | Evidence route | C01 relevance |
|---|---|---:|---|---|
| 009540 | HD한국조선해양 / HD Korea Shipbuilding & Offshore Engineering | 2023-01-02 | www.hd-ksoe.com / www.hhi.co.kr | group_shipyard_orderbacklog_margin_bridge |
| 010140 | 삼성중공업 / Samsung Heavy Industries | 2023-04-06 | rdata.kbsec.com / quartr.com | shipbuilder_backlog_duration_margin_turn_bridge |
| 329180 | HD현대중공업 / HD Hyundai Heavy Industries | 2024-02-06 | www.hhi.co.kr / www.hd-ksoe.com | main_yard_operating_profit_margin_backlog_bridge |
| 010620 | HD현대미포 / HD Hyundai Mipo | 2023-01-02 | www.hd-ksoe.com | mid_size_shipyard_backlog_without_margin_bridge |
| 082740 | 한화엔진 / HSD Engine / Hanwha Engine | 2023-01-25 | www.kedglobal.com | marine_engine_order_backlog_shipbuilder_supply_chain_bridge |
| 071970 | HD현대마린엔진 / STX Heavy Industries | 2024-07-31 | www.hd.com / koreajoongangdaily.joins.com | marine_engine_vertical_integration_backlog_high_MAE_guard |
| 100090 | SK오션플랜트 / SK Oceanplant | 2024-05-17 | securities.miraeasset.com / www.investkorea.org | offshore_wind_specialty_vessel_orderbook_revenue_delay_guard |
| 017960 | 한국카본 / Hankuk Carbon | 2024-01-02 | www.hcarbon.com / www.hcarbon.com | lng_insulation_backlog_supplier_margin_lag_guard |

## 6. Corporate Action / Contamination Check

| Symbol | Profile path | Corporate action contamination note |
|---|---|---|
| 009540 | `atlas/symbol_profiles/009/009540.json` | Candidate corporate-action windows are outside the trigger-to-180D windows used here; row uses tradable shard only. |
| 010140 | `atlas/symbol_profiles/010/010140.json` | Candidate corporate-action windows are outside the trigger-to-180D windows used here; row uses tradable shard only. |
| 010620 | `atlas/symbol_profiles/010/010620.json` | Candidate corporate-action windows are outside the trigger-to-180D windows used here; row uses tradable shard only. |
| 017960 | `atlas/symbol_profiles/017/017960.json` | Candidate corporate-action windows are outside the trigger-to-180D windows used here; row uses tradable shard only. |
| 071970 | `atlas/symbol_profiles/071/071970.json` | Candidate corporate-action windows are outside the trigger-to-180D windows used here; row uses tradable shard only. |
| 082740 | `atlas/symbol_profiles/082/082740.json` | Candidate corporate-action windows are outside the trigger-to-180D windows used here; row uses tradable shard only. |
| 100090 | `atlas/symbol_profiles/100/100090.json` | Candidate corporate-action windows are outside the trigger-to-180D windows used here; row uses tradable shard only. |
| 329180 | `atlas/symbol_profiles/329/329180.json` | Candidate corporate-action windows are outside the trigger-to-180D windows used here; row uses tradable shard only. |

## 7. Trigger Path Summary

| Row | Symbol | Trigger | Entry | MFE30 / MAE30 | MFE90 / MAE90 | MFE180 / MAE180 | Role |
|---|---|---|---:|---:|---:|---:|---|
| R1L115-C01-001 | 009540 | Stage2-Actionable | 2023-01-03 @ 69500 | 24.46% / -2.01% | 29.21% / -2.01% | 87.05% / -2.01% | positive |
| R1L115-C01-002 | 010140 | Stage2-Actionable | 2023-04-07 @ 5240 | 16.03% / -2.10% | 80.73% / -2.10% | 80.73% / -2.10% | positive |
| R1L115-C01-003 | 329180 | Stage3-Yellow | 2024-02-07 @ 113600 | 12.50% / -5.02% | 34.33% / -5.02% | 95.86% / -5.02% | positive |
| R1L115-C01-004 | 010620 | Stage2-Actionable | 2023-01-03 @ 82500 | 1.82% / -13.09% | 1.82% / -23.27% | 17.21% / -23.27% | counterexample |
| R1L115-C01-005 | 082740 | Stage2-Actionable | 2023-01-26 @ 7100 | 28.17% / -3.80% | 35.07% / -4.51% | 79.58% / -4.51% | positive |
| R1L115-C01-006 | 071970 | Stage2-Actionable | 2024-08-01 @ 24600 | 0.61% / -36.34% | 0.61% / -36.34% | 57.11% / -36.34% | counterexample |
| R1L115-C01-007 | 100090 | Stage2-Actionable | 2024-05-17 @ 13650 | 29.89% / -2.27% | 29.89% / -24.54% | 29.89% / -24.54% | counterexample |
| R1L115-C01-008 | 017960 | Stage2-Actionable | 2024-01-03 @ 11390 | 3.25% / -7.90% | 4.83% / -13.35% | 17.21% / -13.35% | counterexample |
| R1L115-C01-009 | 010140 | Stage4B-Watch | 2024-07-26 @ 11870 | 3.45% / -21.40% | 3.54% / -21.40% | 33.45% / -21.40% | stage4b_overlay |

## 8. Case Notes

### HD한국조선해양
Clean group-level backlog exposure worked in 2023, but the row still argues for a bridge: holding-company backlog needs main-yard margin and working-capital evidence before Green.

### 삼성중공업
The April 2023 backlog-duration signal behaved like a valid C01 Stage2 trigger. The later 2024 overlay shows the opposite side: old backlog evidence should not keep the name in Yellow after price extension without fresh confirmation.

### HD현대중공업
This is the cleaner main-yard version of C01. Operating-profit normalization plus backlog quality supported Yellow, while Green remains gated by FCF/revision and execution risk.

### HD현대미포
Group shipbuilding strength did not immunize a smaller yard from margin and project-mix drag. This is the clearest counterexample against inherited backlog scoring.

### 한화엔진
Engine supplier backlog can be valid C01 when order intake is direct and tied to shipyard demand. It still needs the late-cycle watch because supplier beta can outrun revenue conversion.

### HD현대마린엔진
M&A/vertical integration created a plausible backlog story, but the immediate path had severe MAE. Integration synergy is not a substitute for entity-level orders and margin.

### SK오션플랜트
Backlog and capacity narrative failed when revenue recognition lag dominated. This row strengthens the revenue-recognition delay guard.

### 한국카본
LNG insulation supplier exposure was real but early 2024 did not produce near-term MFE. Supplier beta belongs in Watch until disclosed order conversion and margin timing appear.

## 9. Machine-Readable Trigger Rows — JSONL

```jsonl
{"row_type":"price_source_validation","source":"Songdaiki/stock-web","source_url":"https://github.com/Songdaiki/stock-web","manifest_path":"atlas/manifest.json","schema_path":"atlas/schema.json","universe_path":"atlas/universe/all_symbols.csv","manifest_max_date":"2026-02-20","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","calibration_shard_root":"atlas/ohlcv_tradable_by_symbol_year","raw_shard_root":"atlas/ohlcv_raw_by_symbol_year","validation_status":"usable_for_historical_calibration","upstream_source":"FinanceData/marcap"}
{"row_type":"trigger","row_id":"R1L115-C01-001","symbol":"009540","company_name":"HD한국조선해양 / HD Korea Shipbuilding & Offshore Engineering","trigger_date":"2023-01-02","trigger_type":"Stage2-Actionable","trigger_family":"group_shipyard_orderbacklog_margin_bridge","case_role":"positive","representative_trigger":true,"evidence_summary":"HD Hyundai group shipyards entered 2023 with multi-year shipbuilding backlog. The listed holding company row tests whether group backlog plus improving vessel pricing can support Stage2 before margin fully normalizes.","baseline_profile_decision":"Stage2-Actionable / possible Yellow if group backlog visibility is over-weighted","proposed_profile_decision":"Stage2-Actionable; Yellow requires margin and working-capital bridge at the listed entity or main yards","current_profile_verdict":"current_profile_mostly_correct_for_stage2_but_should_require_margin_bridge_before_green","current_profile_error":false,"outcome_label":"positive_backlog_rerating","score_current":76,"score_candidate":79,"stage_current":"Stage2-Actionable","stage_candidate":"Stage3-Yellow guarded","delta":3,"source_urls":["https://www.hd-ksoe.com/data/HDKSOE%20Value-up_EN_241213_1.pdf","https://www.hhi.co.kr/en/investors/financial-info/highlight"],"entry_date":"2023-01-03","entry_price":69500.0,"MFE_30D_pct":24.46,"MAE_30D_pct":-2.01,"peak_date_30D":"2023-02-15","peak_price_30D":86500.0,"trough_date_30D":"2023-01-03","trough_price_30D":68100.0,"window_len_30D":31,"MFE_90D_pct":29.21,"MAE_90D_pct":-2.01,"peak_date_90D":"2023-05-15","peak_price_90D":89800.0,"trough_date_90D":"2023-01-03","trough_price_90D":68100.0,"window_len_90D":91,"MFE_180D_pct":87.05,"MAE_180D_pct":-2.01,"peak_date_180D":"2023-07-17","peak_price_180D":130000.0,"trough_date_180D":"2023-01-03","trough_price_180D":68100.0,"window_len_180D":181,"MFE_250D_pct":87.05,"MAE_250D_pct":-2.01,"peak_date_250D":"2023-07-17","peak_price_250D":130000.0,"trough_date_250D":"2023-01-03","trough_price_250D":68100.0,"window_len_250D":251,"MFE_500D_pct":258.27,"MAE_500D_pct":-2.01,"peak_date_500D":"2025-01-20","peak_price_500D":249000.0,"trough_date_500D":"2023-01-03","trough_price_500D":68100.0,"window_len_500D":501,"drawdown_after_peak_180D_pct":-15.23,"below_entry_within_30D":true,"below_entry_within_90D":true,"below_entry_within_180D":true,"price_path_anchor_urls":["https://github.com/Songdaiki/stock-web/blob/main/atlas/ohlcv_tradable_by_symbol_year/009/009540/2023.csv?plain=1"],"symbol_profile_url":"https://github.com/Songdaiki/stock-web/blob/main/atlas/symbol_profiles/009/009540.json?plain=1","price_data_source":"Songdaiki/stock-web","upstream_source":"FinanceData/marcap","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","calibration_usable":true,"forward_window_status":"complete_180D_within_manifest_max_date","corporate_action_window_contaminated":false,"source_proxy_only":false,"evidence_url_pending":false,"large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C01_ORDER_BACKLOG_MARGIN_BRIDGE","fine_archetype_id":"C01_SHIPBUILDING_ENGINE_BACKLOG_MARGIN_FCF_CONVERSION_BRIDGE","deep_sub_archetype_id":"C01_DEEP_KOREA_SHIPBUILDING_LNG_ENGINE_BACKLOG_TO_MARGIN_FCF_VS_ORDERBOOK_MEMORY","case_id":"C01_009540_2023-01-03_STAGE2_ACTIONABLE_GROUP_SHIPYARD_ORDERBACKLOG_MARGIN_BRIDGE","novelty_key":"C01_ORDER_BACKLOG_MARGIN_BRIDGE|009540|Stage2-Actionable|2023-01-03","dedupe_status":"new_independent_case","aggregate_group_role":"representative_case","entry_price_field":"close","raw_component_score_breakdown":{"evidence_quality":16,"backlog_visibility":17,"margin_bridge":16,"fcf_or_working_capital_bridge":10,"revision_visibility":12,"valuation_or_extension_risk_penalty":-2,"red_team_risk_penalty":-1}}
{"row_type":"trigger","row_id":"R1L115-C01-002","symbol":"010140","company_name":"삼성중공업 / Samsung Heavy Industries","trigger_date":"2023-04-06","trigger_type":"Stage2-Actionable","trigger_family":"shipbuilder_backlog_duration_margin_turn_bridge","case_role":"positive","representative_trigger":true,"evidence_summary":"A 2023 sell-side report cited roughly USD23.8B of shipbuilding/offshore backlog, enough for about 3.9 years of work, before the visible earnings turn accelerated.","baseline_profile_decision":"Stage2-Actionable if backlog duration and high-value LNG mix are visible","proposed_profile_decision":"Stage2-Actionable; Yellow only when backlog duration is paired with OPM/revision improvement","current_profile_verdict":"current_profile_correct_for_stage2_and_yellow_after_margin_bridge","current_profile_error":false,"outcome_label":"positive_backlog_to_margin_rerating","score_current":78,"score_candidate":82,"stage_current":"Stage2-Actionable","stage_candidate":"Stage3-Yellow guarded","delta":4,"source_urls":["https://rdata.kbsec.com/pdf_data/20230406174254857E.pdf","https://quartr.com/events/samsung-heavy-industries-co-ltd-010140-investor-presentation_FYFugbrR"],"entry_date":"2023-04-07","entry_price":5240.0,"MFE_30D_pct":16.03,"MAE_30D_pct":-2.1,"peak_date_30D":"2023-05-23","peak_price_30D":6080.0,"trough_date_30D":"2023-04-10","trough_price_30D":5130.0,"window_len_30D":31,"MFE_90D_pct":80.73,"MAE_90D_pct":-2.1,"peak_date_90D":"2023-08-02","peak_price_90D":9470.0,"trough_date_90D":"2023-04-10","trough_price_90D":5130.0,"window_len_90D":91,"MFE_180D_pct":80.73,"MAE_180D_pct":-2.1,"peak_date_180D":"2023-08-02","peak_price_180D":9470.0,"trough_date_180D":"2023-04-10","trough_price_180D":5130.0,"window_len_180D":181,"MFE_250D_pct":80.73,"MAE_250D_pct":-2.1,"peak_date_250D":"2023-08-02","peak_price_250D":9470.0,"trough_date_250D":"2023-04-10","trough_price_250D":5130.0,"window_len_250D":251,"MFE_500D_pct":202.29,"MAE_500D_pct":-2.1,"peak_date_500D":"2025-03-19","peak_price_500D":15840.0,"trough_date_500D":"2023-04-10","trough_price_500D":5130.0,"window_len_500D":501,"drawdown_after_peak_180D_pct":-28.09,"below_entry_within_30D":true,"below_entry_within_90D":true,"below_entry_within_180D":true,"price_path_anchor_urls":["https://github.com/Songdaiki/stock-web/blob/main/atlas/ohlcv_tradable_by_symbol_year/010/010140/2023.csv?plain=1"],"symbol_profile_url":"https://github.com/Songdaiki/stock-web/blob/main/atlas/symbol_profiles/010/010140.json?plain=1","price_data_source":"Songdaiki/stock-web","upstream_source":"FinanceData/marcap","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","calibration_usable":true,"forward_window_status":"complete_180D_within_manifest_max_date","corporate_action_window_contaminated":false,"source_proxy_only":false,"evidence_url_pending":false,"large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C01_ORDER_BACKLOG_MARGIN_BRIDGE","fine_archetype_id":"C01_SHIPBUILDING_ENGINE_BACKLOG_MARGIN_FCF_CONVERSION_BRIDGE","deep_sub_archetype_id":"C01_DEEP_KOREA_SHIPBUILDING_LNG_ENGINE_BACKLOG_TO_MARGIN_FCF_VS_ORDERBOOK_MEMORY","case_id":"C01_010140_2023-04-07_STAGE2_ACTIONABLE_SHIPBUILDER_BACKLOG_DURATION_MARGIN_TURN_BRIDGE","novelty_key":"C01_ORDER_BACKLOG_MARGIN_BRIDGE|010140|Stage2-Actionable|2023-04-07","dedupe_status":"new_independent_case","aggregate_group_role":"representative_case","entry_price_field":"close","raw_component_score_breakdown":{"evidence_quality":16,"backlog_visibility":17,"margin_bridge":16,"fcf_or_working_capital_bridge":10,"revision_visibility":12,"valuation_or_extension_risk_penalty":-2,"red_team_risk_penalty":-1}}
{"row_type":"trigger","row_id":"R1L115-C01-003","symbol":"329180","company_name":"HD현대중공업 / HD Hyundai Heavy Industries","trigger_date":"2024-02-06","trigger_type":"Stage3-Yellow","trigger_family":"main_yard_operating_profit_margin_backlog_bridge","case_role":"positive","representative_trigger":true,"evidence_summary":"2024 entry tests a main-yard case where backlog quality and operating-profit normalization were becoming visible, not merely order headlines.","baseline_profile_decision":"Stage3-Yellow when operating profit and backlog quality are both visible","proposed_profile_decision":"Stage3-Yellow; Green still blocked unless FCF/revision and execution-risk checks pass","current_profile_verdict":"current_profile_correct_but_green_should_not_be_loosened_by_price_path","current_profile_error":false,"outcome_label":"positive_margin_bridge_rerating","score_current":84,"score_candidate":86,"stage_current":"Stage3-Yellow","stage_candidate":"Stage3-Yellow guarded","delta":2,"source_urls":["https://www.hhi.co.kr/en/investors/financial-info/highlight","https://www.hd-ksoe.com/data/HDKSOE%20Value-up_EN_241213_1.pdf"],"entry_date":"2024-02-07","entry_price":113600.0,"MFE_30D_pct":12.5,"MAE_30D_pct":-5.02,"peak_date_30D":"2024-03-20","peak_price_30D":127800.0,"trough_date_30D":"2024-02-14","trough_price_30D":107900.0,"window_len_30D":31,"MFE_90D_pct":34.33,"MAE_90D_pct":-5.02,"peak_date_90D":"2024-06-21","peak_price_90D":152600.0,"trough_date_90D":"2024-02-14","trough_price_90D":107900.0,"window_len_90D":91,"MFE_180D_pct":95.86,"MAE_180D_pct":-5.02,"peak_date_180D":"2024-08-09","peak_price_180D":222500.0,"trough_date_180D":"2024-02-14","trough_price_180D":107900.0,"window_len_180D":181,"MFE_250D_pct":227.02,"MAE_250D_pct":-5.02,"peak_date_250D":"2025-02-13","peak_price_250D":371500.0,"trough_date_250D":"2024-02-14","trough_price_250D":107900.0,"window_len_250D":251,"MFE_500D_pct":463.38,"MAE_500D_pct":-5.02,"peak_date_500D":"2025-10-27","peak_price_500D":640000.0,"trough_date_500D":"2024-02-14","trough_price_500D":107900.0,"window_len_500D":460,"drawdown_after_peak_180D_pct":-24.09,"below_entry_within_30D":true,"below_entry_within_90D":true,"below_entry_within_180D":true,"price_path_anchor_urls":["https://github.com/Songdaiki/stock-web/blob/main/atlas/ohlcv_tradable_by_symbol_year/329/329180/2024.csv?plain=1"],"symbol_profile_url":"https://github.com/Songdaiki/stock-web/blob/main/atlas/symbol_profiles/329/329180.json?plain=1","price_data_source":"Songdaiki/stock-web","upstream_source":"FinanceData/marcap","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","calibration_usable":true,"forward_window_status":"complete_180D_within_manifest_max_date","corporate_action_window_contaminated":false,"source_proxy_only":false,"evidence_url_pending":false,"large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C01_ORDER_BACKLOG_MARGIN_BRIDGE","fine_archetype_id":"C01_SHIPBUILDING_ENGINE_BACKLOG_MARGIN_FCF_CONVERSION_BRIDGE","deep_sub_archetype_id":"C01_DEEP_KOREA_SHIPBUILDING_LNG_ENGINE_BACKLOG_TO_MARGIN_FCF_VS_ORDERBOOK_MEMORY","case_id":"C01_329180_2024-02-07_STAGE3_YELLOW_MAIN_YARD_OPERATING_PROFIT_MARGIN_BACKLOG_BRIDGE","novelty_key":"C01_ORDER_BACKLOG_MARGIN_BRIDGE|329180|Stage3-Yellow|2024-02-07","dedupe_status":"new_independent_case","aggregate_group_role":"representative_case","entry_price_field":"close","raw_component_score_breakdown":{"evidence_quality":16,"backlog_visibility":17,"margin_bridge":16,"fcf_or_working_capital_bridge":10,"revision_visibility":12,"valuation_or_extension_risk_penalty":-2,"red_team_risk_penalty":-1}}
{"row_type":"trigger","row_id":"R1L115-C01-004","symbol":"010620","company_name":"HD현대미포 / HD Hyundai Mipo","trigger_date":"2023-01-02","trigger_type":"Stage2-Actionable","trigger_family":"mid_size_shipyard_backlog_without_margin_bridge","case_role":"counterexample","representative_trigger":true,"evidence_summary":"Mid-size vessel backlog exposure did not immediately translate into clean margin/FCF conversion; the early 2023 path suffered deep MAE before any durable rerating.","baseline_profile_decision":"Stage2-Actionable if group shipbuilding backlog is over-generalized","proposed_profile_decision":"Stage2-Watch until margin, mix and loss-project drag are explicitly bridged","current_profile_verdict":"current_profile_false_positive_if_group_backlog_is_inherited_without_entity_margin_bridge","current_profile_error":true,"outcome_label":"counterexample_backlog_without_margin_bridge","score_current":75,"score_candidate":64,"stage_current":"Stage2-Actionable","stage_candidate":"Stage2-Watch","delta":-11,"source_urls":["https://www.hd-ksoe.com/data/HDKSOE%20Value-up_EN_241213_1.pdf"],"entry_date":"2023-01-03","entry_price":82500.0,"MFE_30D_pct":1.82,"MAE_30D_pct":-13.09,"peak_date_30D":"2023-01-03","peak_price_30D":84000.0,"trough_date_30D":"2023-01-06","trough_price_30D":71700.0,"window_len_30D":31,"MFE_90D_pct":1.82,"MAE_90D_pct":-23.27,"peak_date_90D":"2023-01-03","peak_price_90D":84000.0,"trough_date_90D":"2023-03-16","trough_price_90D":63300.0,"window_len_90D":91,"MFE_180D_pct":17.21,"MAE_180D_pct":-23.27,"peak_date_180D":"2023-08-02","peak_price_180D":96700.0,"trough_date_180D":"2023-03-16","trough_price_180D":63300.0,"window_len_180D":181,"MFE_250D_pct":17.21,"MAE_250D_pct":-23.27,"peak_date_250D":"2023-08-02","peak_price_250D":96700.0,"trough_date_250D":"2023-03-16","trough_price_250D":63300.0,"window_len_250D":251,"MFE_500D_pct":72.73,"MAE_500D_pct":-28.73,"peak_date_500D":"2024-12-23","peak_price_500D":142500.0,"trough_date_500D":"2024-04-16","trough_price_500D":58800.0,"window_len_500D":501,"drawdown_after_peak_180D_pct":-16.44,"below_entry_within_30D":true,"below_entry_within_90D":true,"below_entry_within_180D":true,"price_path_anchor_urls":["https://github.com/Songdaiki/stock-web/blob/main/atlas/ohlcv_tradable_by_symbol_year/010/010620/2023.csv?plain=1"],"symbol_profile_url":"https://github.com/Songdaiki/stock-web/blob/main/atlas/symbol_profiles/010/010620.json?plain=1","price_data_source":"Songdaiki/stock-web","upstream_source":"FinanceData/marcap","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","calibration_usable":true,"forward_window_status":"complete_180D_within_manifest_max_date","corporate_action_window_contaminated":false,"source_proxy_only":false,"evidence_url_pending":false,"large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C01_ORDER_BACKLOG_MARGIN_BRIDGE","fine_archetype_id":"C01_SHIPBUILDING_ENGINE_BACKLOG_MARGIN_FCF_CONVERSION_BRIDGE","deep_sub_archetype_id":"C01_DEEP_KOREA_SHIPBUILDING_LNG_ENGINE_BACKLOG_TO_MARGIN_FCF_VS_ORDERBOOK_MEMORY","case_id":"C01_010620_2023-01-03_STAGE2_ACTIONABLE_MID_SIZE_SHIPYARD_BACKLOG_WITHOUT_MARGIN_BRIDGE","novelty_key":"C01_ORDER_BACKLOG_MARGIN_BRIDGE|010620|Stage2-Actionable|2023-01-03","dedupe_status":"new_independent_case","aggregate_group_role":"representative_case","entry_price_field":"close","raw_component_score_breakdown":{"evidence_quality":16,"backlog_visibility":12,"margin_bridge":7,"fcf_or_working_capital_bridge":4,"revision_visibility":5,"valuation_or_extension_risk_penalty":-10,"red_team_risk_penalty":-8}}
{"row_type":"trigger","row_id":"R1L115-C01-005","symbol":"082740","company_name":"한화엔진 / HSD Engine / Hanwha Engine","trigger_date":"2023-01-25","trigger_type":"Stage2-Actionable","trigger_family":"marine_engine_order_backlog_shipbuilder_supply_chain_bridge","case_role":"positive","representative_trigger":true,"evidence_summary":"KED reported HSD Engine order volume exceeded USD162.1M in one month; the row tests whether engine backlog tied to shipyard demand is a valid C01 supplier bridge.","baseline_profile_decision":"Stage2-Actionable if engine order conversion is visible","proposed_profile_decision":"Stage2-Actionable; Yellow only after engine backlog converts into revenue/margin revision","current_profile_verdict":"current_profile_correct_for_stage2_supplier_backlog_but_needs_late_4B_watch_after_price_extension","current_profile_error":false,"outcome_label":"positive_supplier_backlog_rerating","score_current":77,"score_candidate":81,"stage_current":"Stage2-Actionable","stage_candidate":"Stage3-Yellow guarded","delta":4,"source_urls":["https://www.kedglobal.com/shipping-shipbuilding/newsView/ked202301250005"],"entry_date":"2023-01-26","entry_price":7100.0,"MFE_30D_pct":28.17,"MAE_30D_pct":-3.8,"peak_date_30D":"2023-02-14","peak_price_30D":9100.0,"trough_date_30D":"2023-01-26","trough_price_30D":6830.0,"window_len_30D":31,"MFE_90D_pct":35.07,"MAE_90D_pct":-4.51,"peak_date_90D":"2023-06-08","peak_price_90D":9590.0,"trough_date_90D":"2023-03-20","trough_price_90D":6780.0,"window_len_90D":91,"MFE_180D_pct":79.58,"MAE_180D_pct":-4.51,"peak_date_180D":"2023-08-02","peak_price_180D":12750.0,"trough_date_180D":"2023-03-20","trough_price_180D":6780.0,"window_len_180D":181,"MFE_250D_pct":79.58,"MAE_250D_pct":-4.51,"peak_date_250D":"2023-08-02","peak_price_250D":12750.0,"trough_date_250D":"2023-03-20","trough_price_250D":6780.0,"window_len_250D":251,"MFE_500D_pct":304.93,"MAE_500D_pct":-4.51,"peak_date_500D":"2025-02-14","peak_price_500D":28750.0,"trough_date_500D":"2023-03-20","trough_price_500D":6780.0,"window_len_500D":501,"drawdown_after_peak_180D_pct":-37.8,"below_entry_within_30D":true,"below_entry_within_90D":true,"below_entry_within_180D":true,"price_path_anchor_urls":["https://github.com/Songdaiki/stock-web/blob/main/atlas/ohlcv_tradable_by_symbol_year/082/082740/2023.csv?plain=1"],"symbol_profile_url":"https://github.com/Songdaiki/stock-web/blob/main/atlas/symbol_profiles/082/082740.json?plain=1","price_data_source":"Songdaiki/stock-web","upstream_source":"FinanceData/marcap","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","calibration_usable":true,"forward_window_status":"complete_180D_within_manifest_max_date","corporate_action_window_contaminated":false,"source_proxy_only":false,"evidence_url_pending":false,"large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C01_ORDER_BACKLOG_MARGIN_BRIDGE","fine_archetype_id":"C01_SHIPBUILDING_ENGINE_BACKLOG_MARGIN_FCF_CONVERSION_BRIDGE","deep_sub_archetype_id":"C01_DEEP_KOREA_SHIPBUILDING_LNG_ENGINE_BACKLOG_TO_MARGIN_FCF_VS_ORDERBOOK_MEMORY","case_id":"C01_082740_2023-01-26_STAGE2_ACTIONABLE_MARINE_ENGINE_ORDER_BACKLOG_SHIPBUILDER_SUPPLY_CHAIN_BRIDGE","novelty_key":"C01_ORDER_BACKLOG_MARGIN_BRIDGE|082740|Stage2-Actionable|2023-01-26","dedupe_status":"new_independent_case","aggregate_group_role":"representative_case","entry_price_field":"close","raw_component_score_breakdown":{"evidence_quality":16,"backlog_visibility":17,"margin_bridge":16,"fcf_or_working_capital_bridge":10,"revision_visibility":12,"valuation_or_extension_risk_penalty":-2,"red_team_risk_penalty":-1}}
{"row_type":"trigger","row_id":"R1L115-C01-006","symbol":"071970","company_name":"HD현대마린엔진 / STX Heavy Industries","trigger_date":"2024-07-31","trigger_type":"Stage2-Actionable","trigger_family":"marine_engine_vertical_integration_backlog_high_MAE_guard","case_role":"counterexample","representative_trigger":true,"evidence_summary":"HD Hyundai completed the STX Heavy Industries acquisition and launched HD Hyundai Marine Engine, creating a plausible engine-backlog integration story, but the immediate path had very high MAE before later rerating.","baseline_profile_decision":"Stage2-Actionable or Yellow if acquisition synergy is over-counted as backlog bridge","proposed_profile_decision":"Stage2-Watch/Actionable only; require post-acquisition order, revenue and margin confirmation; activate high-MAE guard","current_profile_verdict":"current_profile_false_positive_if_MA_synergy_substitutes_for_margin_bridge","current_profile_error":true,"outcome_label":"counterexample_high_MAE_then_delayed_rerating","score_current":79,"score_candidate":66,"stage_current":"Stage3-Yellow","stage_candidate":"Stage2-Watch","delta":-13,"source_urls":["https://www.hd.com/en/newsroom/media-hub/press/view?detailsKey=3176","https://koreajoongangdaily.joins.com/news/2024-07-30/business/industry/STX-Heavy-Industries-renamed-HD-Hyundai-Marine-Engine-after-acquisition/2101936"],"entry_date":"2024-08-01","entry_price":24600.0,"MFE_30D_pct":0.61,"MAE_30D_pct":-36.34,"peak_date_30D":"2024-08-01","peak_price_30D":24750.0,"trough_date_30D":"2024-09-06","trough_price_30D":15660.0,"window_len_30D":31,"MFE_90D_pct":0.61,"MAE_90D_pct":-36.34,"peak_date_90D":"2024-08-01","peak_price_90D":24750.0,"trough_date_90D":"2024-09-06","trough_price_90D":15660.0,"window_len_90D":91,"MFE_180D_pct":57.11,"MAE_180D_pct":-36.34,"peak_date_180D":"2025-04-28","peak_price_180D":38650.0,"trough_date_180D":"2024-09-06","trough_price_180D":15660.0,"window_len_180D":181,"MFE_250D_pct":247.76,"MAE_250D_pct":-36.34,"peak_date_250D":"2025-08-08","peak_price_250D":85550.0,"trough_date_250D":"2024-09-06","trough_price_250D":15660.0,"window_len_250D":251,"MFE_500D_pct":333.33,"MAE_500D_pct":-36.34,"peak_date_500D":"2025-11-03","peak_price_500D":106600.0,"trough_date_500D":"2024-09-06","trough_price_500D":15660.0,"window_len_500D":342,"drawdown_after_peak_180D_pct":-6.6,"below_entry_within_30D":true,"below_entry_within_90D":true,"below_entry_within_180D":true,"price_path_anchor_urls":["https://github.com/Songdaiki/stock-web/blob/main/atlas/ohlcv_tradable_by_symbol_year/071/071970/2024.csv?plain=1","https://github.com/Songdaiki/stock-web/blob/main/atlas/ohlcv_tradable_by_symbol_year/071/071970/2025.csv?plain=1"],"symbol_profile_url":"https://github.com/Songdaiki/stock-web/blob/main/atlas/symbol_profiles/071/071970.json?plain=1","price_data_source":"Songdaiki/stock-web","upstream_source":"FinanceData/marcap","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","calibration_usable":true,"forward_window_status":"complete_180D_within_manifest_max_date","corporate_action_window_contaminated":false,"source_proxy_only":false,"evidence_url_pending":false,"large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C01_ORDER_BACKLOG_MARGIN_BRIDGE","fine_archetype_id":"C01_SHIPBUILDING_ENGINE_BACKLOG_MARGIN_FCF_CONVERSION_BRIDGE","deep_sub_archetype_id":"C01_DEEP_KOREA_SHIPBUILDING_LNG_ENGINE_BACKLOG_TO_MARGIN_FCF_VS_ORDERBOOK_MEMORY","case_id":"C01_071970_2024-08-01_STAGE2_ACTIONABLE_MARINE_ENGINE_VERTICAL_INTEGRATION_BACKLOG_HIGH_MAE_GUARD","novelty_key":"C01_ORDER_BACKLOG_MARGIN_BRIDGE|071970|Stage2-Actionable|2024-08-01","dedupe_status":"new_independent_case","aggregate_group_role":"representative_case","entry_price_field":"close","raw_component_score_breakdown":{"evidence_quality":16,"backlog_visibility":12,"margin_bridge":7,"fcf_or_working_capital_bridge":4,"revision_visibility":5,"valuation_or_extension_risk_penalty":-10,"red_team_risk_penalty":-8}}
{"row_type":"trigger","row_id":"R1L115-C01-007","symbol":"100090","company_name":"SK오션플랜트 / SK Oceanplant","trigger_date":"2024-05-17","trigger_type":"Stage2-Actionable","trigger_family":"offshore_wind_specialty_vessel_orderbook_revenue_delay_guard","case_role":"counterexample","representative_trigger":true,"evidence_summary":"A 1Q24 report noted revenue recognition delay and a consensus miss. The row is a C01-adjacent orderbook-to-margin trap: orderbook narrative exists, but execution timing and revenue conversion lag dominate.","baseline_profile_decision":"Stage2-Actionable if backlog and offshore wind capacity are over-counted","proposed_profile_decision":"Stage2-Watch until revenue recognition and margin bridge are confirmed; no Yellow from backlog alone","current_profile_verdict":"current_profile_false_positive_if_order_backlog_ignores_revenue_recognition_delay","current_profile_error":true,"outcome_label":"counterexample_revenue_recognition_delay","score_current":73,"score_candidate":61,"stage_current":"Stage2-Actionable","stage_candidate":"Stage2-Watch","delta":-12,"source_proxy_only":false,"source_urls":["https://securities.miraeasset.com/bbs/download/2127169.pdf?attachmentId=2127169","https://www.investkorea.org/ik-en/bbs/i-465/detail.do?ntt_sn=492595"],"entry_date":"2024-05-17","entry_price":13650.0,"MFE_30D_pct":29.89,"MAE_30D_pct":-2.27,"peak_date_30D":"2024-06-04","peak_price_30D":17730.0,"trough_date_30D":"2024-06-21","trough_price_30D":13340.0,"window_len_30D":31,"MFE_90D_pct":29.89,"MAE_90D_pct":-24.54,"peak_date_90D":"2024-06-04","peak_price_90D":17730.0,"trough_date_90D":"2024-08-05","trough_price_90D":10300.0,"window_len_90D":91,"MFE_180D_pct":29.89,"MAE_180D_pct":-24.54,"peak_date_180D":"2024-06-04","peak_price_180D":17730.0,"trough_date_180D":"2024-08-05","trough_price_180D":10300.0,"window_len_180D":181,"MFE_250D_pct":62.27,"MAE_250D_pct":-24.54,"peak_date_250D":"2025-05-19","peak_price_250D":22150.0,"trough_date_250D":"2024-08-05","trough_price_250D":10300.0,"window_len_250D":251,"MFE_500D_pct":130.77,"MAE_500D_pct":-24.54,"peak_date_500D":"2025-09-15","peak_price_500D":31500.0,"trough_date_500D":"2024-08-05","trough_price_500D":10300.0,"window_len_500D":395,"drawdown_after_peak_180D_pct":-41.91,"below_entry_within_30D":true,"below_entry_within_90D":true,"below_entry_within_180D":true,"price_path_anchor_urls":["https://github.com/Songdaiki/stock-web/blob/main/atlas/ohlcv_tradable_by_symbol_year/100/100090/2024.csv?plain=1"],"symbol_profile_url":"https://github.com/Songdaiki/stock-web/blob/main/atlas/symbol_profiles/100/100090.json?plain=1","price_data_source":"Songdaiki/stock-web","upstream_source":"FinanceData/marcap","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","calibration_usable":true,"forward_window_status":"complete_180D_within_manifest_max_date","corporate_action_window_contaminated":false,"evidence_url_pending":false,"large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C01_ORDER_BACKLOG_MARGIN_BRIDGE","fine_archetype_id":"C01_SHIPBUILDING_ENGINE_BACKLOG_MARGIN_FCF_CONVERSION_BRIDGE","deep_sub_archetype_id":"C01_DEEP_KOREA_SHIPBUILDING_LNG_ENGINE_BACKLOG_TO_MARGIN_FCF_VS_ORDERBOOK_MEMORY","case_id":"C01_100090_2024-05-17_STAGE2_ACTIONABLE_OFFSHORE_WIND_SPECIALTY_VESSEL_ORDERBOOK_REVENUE_DELAY_GUARD","novelty_key":"C01_ORDER_BACKLOG_MARGIN_BRIDGE|100090|Stage2-Actionable|2024-05-17","dedupe_status":"new_independent_case","aggregate_group_role":"representative_case","entry_price_field":"close","raw_component_score_breakdown":{"evidence_quality":16,"backlog_visibility":12,"margin_bridge":7,"fcf_or_working_capital_bridge":4,"revision_visibility":5,"valuation_or_extension_risk_penalty":-10,"red_team_risk_penalty":-8}}
{"row_type":"trigger","row_id":"R1L115-C01-008","symbol":"017960","company_name":"한국카본 / Hankuk Carbon","trigger_date":"2024-01-02","trigger_type":"Stage2-Actionable","trigger_family":"lng_insulation_backlog_supplier_margin_lag_guard","case_role":"counterexample","representative_trigger":true,"evidence_summary":"Hankuk Carbon is a LNG-carrier insulation supplier. Early 2024 supplier exposure alone had muted 30/90/180D MFE until the later 2025 rerating; C01 should require order conversion and margin timing, not just shipbuilding beta.","baseline_profile_decision":"Stage2-Actionable if LNG shipbuilding supplier beta is over-counted","proposed_profile_decision":"Stage2-Watch until disclosed supply contract/order backlog and OPM bridge are visible","current_profile_verdict":"current_profile_false_positive_if_supplier_beta_replaces_order_margin_bridge","current_profile_error":true,"outcome_label":"counterexample_supplier_beta_without_near_term_bridge","score_current":72,"score_candidate":62,"stage_current":"Stage2-Actionable","stage_candidate":"Stage2-Watch","delta":-10,"source_proxy_only":false,"source_urls":["https://www.hcarbon.com/en/ourBusiness/ship.do","https://www.hcarbon.com/en/esg/directorate.do","https://kind.krx.co.kr/common/disclsviewer.do?acptno=20240516000945&docno=&method=search&viewerhost="],"entry_date":"2024-01-03","entry_price":11390.0,"MFE_30D_pct":3.25,"MAE_30D_pct":-7.9,"peak_date_30D":"2024-01-04","peak_price_30D":11760.0,"trough_date_30D":"2024-02-01","trough_price_30D":10490.0,"window_len_30D":31,"MFE_90D_pct":4.83,"MAE_90D_pct":-13.35,"peak_date_90D":"2024-05-14","peak_price_90D":11940.0,"trough_date_90D":"2024-03-08","trough_price_90D":9870.0,"window_len_90D":91,"MFE_180D_pct":17.21,"MAE_180D_pct":-13.35,"peak_date_180D":"2024-08-20","peak_price_180D":13350.0,"trough_date_180D":"2024-03-08","trough_price_180D":9870.0,"window_len_180D":181,"MFE_250D_pct":17.21,"MAE_250D_pct":-17.47,"peak_date_250D":"2024-08-20","peak_price_250D":13350.0,"trough_date_250D":"2024-12-09","trough_price_250D":9400.0,"window_len_250D":251,"MFE_500D_pct":245.04,"MAE_500D_pct":-17.47,"peak_date_500D":"2025-10-16","peak_price_500D":39300.0,"trough_date_500D":"2024-12-09","trough_price_500D":9400.0,"window_len_500D":485,"drawdown_after_peak_180D_pct":-21.65,"below_entry_within_30D":true,"below_entry_within_90D":true,"below_entry_within_180D":true,"price_path_anchor_urls":["https://github.com/Songdaiki/stock-web/blob/main/atlas/ohlcv_tradable_by_symbol_year/017/017960/2024.csv?plain=1"],"symbol_profile_url":"https://github.com/Songdaiki/stock-web/blob/main/atlas/symbol_profiles/017/017960.json?plain=1","price_data_source":"Songdaiki/stock-web","upstream_source":"FinanceData/marcap","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","calibration_usable":true,"forward_window_status":"complete_180D_within_manifest_max_date","corporate_action_window_contaminated":false,"evidence_url_pending":false,"large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C01_ORDER_BACKLOG_MARGIN_BRIDGE","fine_archetype_id":"C01_SHIPBUILDING_ENGINE_BACKLOG_MARGIN_FCF_CONVERSION_BRIDGE","deep_sub_archetype_id":"C01_DEEP_KOREA_SHIPBUILDING_LNG_ENGINE_BACKLOG_TO_MARGIN_FCF_VS_ORDERBOOK_MEMORY","case_id":"C01_017960_2024-01-03_STAGE2_ACTIONABLE_LNG_INSULATION_BACKLOG_SUPPLIER_MARGIN_LAG_GUARD","novelty_key":"C01_ORDER_BACKLOG_MARGIN_BRIDGE|017960|Stage2-Actionable|2024-01-03","dedupe_status":"new_independent_case","aggregate_group_role":"representative_case","entry_price_field":"close","raw_component_score_breakdown":{"evidence_quality":16,"backlog_visibility":12,"margin_bridge":7,"fcf_or_working_capital_bridge":4,"revision_visibility":5,"valuation_or_extension_risk_penalty":-10,"red_team_risk_penalty":-8}}
{"row_type":"trigger","row_id":"R1L115-C01-009","symbol":"010140","company_name":"삼성중공업 / Samsung Heavy Industries","trigger_date":"2024-07-26","trigger_type":"Stage4B-Watch","trigger_family":"shipbuilder_price_extension_local_4b_watch_without_incremental_bridge","case_role":"stage4b_overlay","representative_trigger":false,"evidence_summary":"After the 2023/2024 shipbuilding rerating, Samsung Heavy reached a local extension zone. The 30/90D path turned MAE-heavy, supporting local 4B watch rather than full 4C.","baseline_profile_decision":"May remain Stage3-Yellow if old backlog evidence is over-retained","proposed_profile_decision":"local 4B watch; full 4B needs non-price deterioration, and 4C needs thesis break confirmation","current_profile_verdict":"current_profile_4B_too_late_if_price_extension_ignored","current_profile_error":true,"outcome_label":"local_4B_watch_supported","score_current":82,"score_candidate":71,"stage_current":"Stage3-Yellow","stage_candidate":"Stage4B-Watch","delta":-11,"source_urls":["https://quartr.com/events/samsung-heavy-industries-co-ltd-010140-investor-presentation_FYFugbrR","https://www.imarinenews.com/20846.html"],"entry_date":"2024-07-26","entry_price":11870.0,"MFE_30D_pct":3.45,"MAE_30D_pct":-21.4,"peak_date_30D":"2024-07-26","peak_price_30D":12280.0,"trough_date_30D":"2024-09-09","trough_price_30D":9330.0,"window_len_30D":31,"MFE_90D_pct":3.54,"MAE_90D_pct":-21.4,"peak_date_90D":"2024-11-25","peak_price_90D":12290.0,"trough_date_90D":"2024-09-09","trough_price_90D":9330.0,"window_len_90D":91,"MFE_180D_pct":33.45,"MAE_180D_pct":-21.4,"peak_date_180D":"2025-03-19","peak_price_180D":15840.0,"trough_date_180D":"2024-09-09","trough_price_180D":9330.0,"window_len_180D":181,"MFE_250D_pct":70.18,"MAE_250D_pct":-21.4,"peak_date_250D":"2025-08-05","peak_price_250D":20200.0,"trough_date_250D":"2024-09-09","trough_price_250D":9330.0,"window_len_250D":251,"MFE_500D_pct":173.8,"MAE_500D_pct":-21.4,"peak_date_500D":"2025-10-30","peak_price_500D":32500.0,"trough_date_500D":"2024-09-09","trough_price_500D":9330.0,"window_len_500D":346,"drawdown_after_peak_180D_pct":-20.14,"below_entry_within_30D":true,"below_entry_within_90D":true,"below_entry_within_180D":true,"price_path_anchor_urls":["https://github.com/Songdaiki/stock-web/blob/main/atlas/ohlcv_tradable_by_symbol_year/010/010140/2024.csv?plain=1","https://github.com/Songdaiki/stock-web/blob/main/atlas/ohlcv_tradable_by_symbol_year/010/010140/2025.csv?plain=1"],"symbol_profile_url":"https://github.com/Songdaiki/stock-web/blob/main/atlas/symbol_profiles/010/010140.json?plain=1","price_data_source":"Songdaiki/stock-web","upstream_source":"FinanceData/marcap","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","calibration_usable":true,"forward_window_status":"complete_180D_within_manifest_max_date","corporate_action_window_contaminated":false,"source_proxy_only":false,"evidence_url_pending":false,"large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C01_ORDER_BACKLOG_MARGIN_BRIDGE","fine_archetype_id":"C01_SHIPBUILDING_BACKLOG_PRICE_EXTENSION_LOCAL_4B_WATCH","deep_sub_archetype_id":"C01_DEEP_VALID_BACKLOG_AFTER_PRICE_EXTENSION_LOCAL_4B_VS_FULL_4C_CONFIRMATION","case_id":"C01_010140_2024-07-26_STAGE4B_WATCH_SHIPBUILDER_PRICE_EXTENSION_LOCAL_4B_WATCH_WITHOUT_INCREMENTAL_BRIDGE","novelty_key":"C01_ORDER_BACKLOG_MARGIN_BRIDGE|010140|Stage4B-Watch|2024-07-26","dedupe_status":"same_case_new_trigger_family","aggregate_group_role":"4B_overlay_only","entry_price_field":"close","raw_component_score_breakdown":{"evidence_quality":16,"backlog_visibility":17,"margin_bridge":7,"fcf_or_working_capital_bridge":4,"revision_visibility":5,"valuation_or_extension_risk_penalty":-10,"red_team_risk_penalty":-8}}
```

## 10. Stage Transition Rows — JSONL

```jsonl
{"row_type":"stage_transition","row_id":"R1L115-C01-001","symbol":"009540","canonical_archetype_id":"C01_ORDER_BACKLOG_MARGIN_BRIDGE","trigger_type":"Stage2-Actionable","entry_date":"2023-01-03","transition_label":"Stage2_or_Yellow_supported_but_Green_requires_margin_FCF_bridge","mfe_mae_180_spread_pct":85.04,"profile_residual":"current_profile_mostly_correct_for_stage2_but_should_require_margin_bridge_before_green"}
{"row_type":"stage_transition","row_id":"R1L115-C01-002","symbol":"010140","canonical_archetype_id":"C01_ORDER_BACKLOG_MARGIN_BRIDGE","trigger_type":"Stage2-Actionable","entry_date":"2023-04-07","transition_label":"Stage2_or_Yellow_supported_but_Green_requires_margin_FCF_bridge","mfe_mae_180_spread_pct":78.63,"profile_residual":"current_profile_correct_for_stage2_and_yellow_after_margin_bridge"}
{"row_type":"stage_transition","row_id":"R1L115-C01-003","symbol":"329180","canonical_archetype_id":"C01_ORDER_BACKLOG_MARGIN_BRIDGE","trigger_type":"Stage3-Yellow","entry_date":"2024-02-07","transition_label":"Stage2_or_Yellow_supported_but_Green_requires_margin_FCF_bridge","mfe_mae_180_spread_pct":90.84,"profile_residual":"current_profile_correct_but_green_should_not_be_loosened_by_price_path"}
{"row_type":"stage_transition","row_id":"R1L115-C01-004","symbol":"010620","canonical_archetype_id":"C01_ORDER_BACKLOG_MARGIN_BRIDGE","trigger_type":"Stage2-Actionable","entry_date":"2023-01-03","transition_label":"Stage2_false_positive_or_Yellow_block_supported","mfe_mae_180_spread_pct":-6.06,"profile_residual":"current_profile_false_positive_if_group_backlog_is_inherited_without_entity_margin_bridge"}
{"row_type":"stage_transition","row_id":"R1L115-C01-005","symbol":"082740","canonical_archetype_id":"C01_ORDER_BACKLOG_MARGIN_BRIDGE","trigger_type":"Stage2-Actionable","entry_date":"2023-01-26","transition_label":"Stage2_or_Yellow_supported_but_Green_requires_margin_FCF_bridge","mfe_mae_180_spread_pct":75.07,"profile_residual":"current_profile_correct_for_stage2_supplier_backlog_but_needs_late_4B_watch_after_price_extension"}
{"row_type":"stage_transition","row_id":"R1L115-C01-006","symbol":"071970","canonical_archetype_id":"C01_ORDER_BACKLOG_MARGIN_BRIDGE","trigger_type":"Stage2-Actionable","entry_date":"2024-08-01","transition_label":"Stage2_false_positive_or_Yellow_block_supported","mfe_mae_180_spread_pct":20.77,"profile_residual":"current_profile_false_positive_if_MA_synergy_substitutes_for_margin_bridge"}
{"row_type":"stage_transition","row_id":"R1L115-C01-007","symbol":"100090","canonical_archetype_id":"C01_ORDER_BACKLOG_MARGIN_BRIDGE","trigger_type":"Stage2-Actionable","entry_date":"2024-05-17","transition_label":"Stage2_false_positive_or_Yellow_block_supported","mfe_mae_180_spread_pct":5.35,"profile_residual":"current_profile_false_positive_if_order_backlog_ignores_revenue_recognition_delay"}
{"row_type":"stage_transition","row_id":"R1L115-C01-008","symbol":"017960","canonical_archetype_id":"C01_ORDER_BACKLOG_MARGIN_BRIDGE","trigger_type":"Stage2-Actionable","entry_date":"2024-01-03","transition_label":"Stage2_false_positive_or_Yellow_block_supported","mfe_mae_180_spread_pct":3.86,"profile_residual":"current_profile_false_positive_if_supplier_beta_replaces_order_margin_bridge"}
{"row_type":"stage_transition","row_id":"R1L115-C01-009","symbol":"010140","canonical_archetype_id":"C01_ORDER_BACKLOG_MARGIN_BRIDGE","trigger_type":"Stage4B-Watch","entry_date":"2024-07-26","transition_label":"Stage3_to_local_4B_watch_supported","mfe_mae_180_spread_pct":12.05,"profile_residual":"current_profile_4B_too_late_if_price_extension_ignored"}
```

## 11. Score Simulation Rows — JSONL

```jsonl
{"row_type":"score_simulation","symbol":"009540","canonical_archetype_id":"C01_ORDER_BACKLOG_MARGIN_BRIDGE","entry_date":"2023-01-03","current_proxy_score":76,"candidate_C01_guarded_score":79,"current_proxy_stage":"Stage2-Actionable","candidate_stage":"Stage3-Yellow guarded","delta":3,"decision_reason":"Stage2-Actionable; Yellow requires margin and working-capital bridge at the listed entity or main yards","raw_component_score_breakdown":{"evidence_quality":16,"backlog_visibility":17,"margin_bridge":16,"fcf_or_working_capital_bridge":10,"revision_visibility":12,"valuation_or_extension_risk_penalty":-2,"red_team_risk_penalty":-1}}
{"row_type":"score_simulation","symbol":"010140","canonical_archetype_id":"C01_ORDER_BACKLOG_MARGIN_BRIDGE","entry_date":"2023-04-07","current_proxy_score":78,"candidate_C01_guarded_score":82,"current_proxy_stage":"Stage2-Actionable","candidate_stage":"Stage3-Yellow guarded","delta":4,"decision_reason":"Stage2-Actionable; Yellow only when backlog duration is paired with OPM/revision improvement","raw_component_score_breakdown":{"evidence_quality":16,"backlog_visibility":17,"margin_bridge":16,"fcf_or_working_capital_bridge":10,"revision_visibility":12,"valuation_or_extension_risk_penalty":-2,"red_team_risk_penalty":-1}}
{"row_type":"score_simulation","symbol":"329180","canonical_archetype_id":"C01_ORDER_BACKLOG_MARGIN_BRIDGE","entry_date":"2024-02-07","current_proxy_score":84,"candidate_C01_guarded_score":86,"current_proxy_stage":"Stage3-Yellow","candidate_stage":"Stage3-Yellow guarded","delta":2,"decision_reason":"Stage3-Yellow; Green still blocked unless FCF/revision and execution-risk checks pass","raw_component_score_breakdown":{"evidence_quality":16,"backlog_visibility":17,"margin_bridge":16,"fcf_or_working_capital_bridge":10,"revision_visibility":12,"valuation_or_extension_risk_penalty":-2,"red_team_risk_penalty":-1}}
{"row_type":"score_simulation","symbol":"010620","canonical_archetype_id":"C01_ORDER_BACKLOG_MARGIN_BRIDGE","entry_date":"2023-01-03","current_proxy_score":75,"candidate_C01_guarded_score":64,"current_proxy_stage":"Stage2-Actionable","candidate_stage":"Stage2-Watch","delta":-11,"decision_reason":"Stage2-Watch until margin, mix and loss-project drag are explicitly bridged","raw_component_score_breakdown":{"evidence_quality":16,"backlog_visibility":12,"margin_bridge":7,"fcf_or_working_capital_bridge":4,"revision_visibility":5,"valuation_or_extension_risk_penalty":-10,"red_team_risk_penalty":-8}}
{"row_type":"score_simulation","symbol":"082740","canonical_archetype_id":"C01_ORDER_BACKLOG_MARGIN_BRIDGE","entry_date":"2023-01-26","current_proxy_score":77,"candidate_C01_guarded_score":81,"current_proxy_stage":"Stage2-Actionable","candidate_stage":"Stage3-Yellow guarded","delta":4,"decision_reason":"Stage2-Actionable; Yellow only after engine backlog converts into revenue/margin revision","raw_component_score_breakdown":{"evidence_quality":16,"backlog_visibility":17,"margin_bridge":16,"fcf_or_working_capital_bridge":10,"revision_visibility":12,"valuation_or_extension_risk_penalty":-2,"red_team_risk_penalty":-1}}
{"row_type":"score_simulation","symbol":"071970","canonical_archetype_id":"C01_ORDER_BACKLOG_MARGIN_BRIDGE","entry_date":"2024-08-01","current_proxy_score":79,"candidate_C01_guarded_score":66,"current_proxy_stage":"Stage3-Yellow","candidate_stage":"Stage2-Watch","delta":-13,"decision_reason":"Stage2-Watch/Actionable only; require post-acquisition order, revenue and margin confirmation; activate high-MAE guard","raw_component_score_breakdown":{"evidence_quality":16,"backlog_visibility":12,"margin_bridge":7,"fcf_or_working_capital_bridge":4,"revision_visibility":5,"valuation_or_extension_risk_penalty":-10,"red_team_risk_penalty":-8}}
{"row_type":"score_simulation","symbol":"100090","canonical_archetype_id":"C01_ORDER_BACKLOG_MARGIN_BRIDGE","entry_date":"2024-05-17","current_proxy_score":73,"candidate_C01_guarded_score":61,"current_proxy_stage":"Stage2-Actionable","candidate_stage":"Stage2-Watch","delta":-12,"decision_reason":"Stage2-Watch until revenue recognition and margin bridge are confirmed; no Yellow from backlog alone","raw_component_score_breakdown":{"evidence_quality":16,"backlog_visibility":12,"margin_bridge":7,"fcf_or_working_capital_bridge":4,"revision_visibility":5,"valuation_or_extension_risk_penalty":-10,"red_team_risk_penalty":-8}}
{"row_type":"score_simulation","symbol":"017960","canonical_archetype_id":"C01_ORDER_BACKLOG_MARGIN_BRIDGE","entry_date":"2024-01-03","current_proxy_score":72,"candidate_C01_guarded_score":62,"current_proxy_stage":"Stage2-Actionable","candidate_stage":"Stage2-Watch","delta":-10,"decision_reason":"Stage2-Watch until disclosed supply contract/order backlog and OPM bridge are visible","raw_component_score_breakdown":{"evidence_quality":16,"backlog_visibility":12,"margin_bridge":7,"fcf_or_working_capital_bridge":4,"revision_visibility":5,"valuation_or_extension_risk_penalty":-10,"red_team_risk_penalty":-8}}
```

## 12. Aggregate Row — JSON

```json
{
  "usable_trigger_rows": 9,
  "representative_trigger_rows": 8,
  "median_MFE_30D_pct": 14.27,
  "median_MAE_30D_pct": -4.41,
  "median_MFE_90D_pct": 29.55,
  "median_MAE_90D_pct": -9.18,
  "median_MFE_180D_pct": 68.34,
  "median_MAE_180D_pct": -9.18,
  "positive_to_counterexample_ratio": "4:4",
  "stage4b_overlay_rows": 1,
  "current_profile_error_rows": 5
}
```

## 13. Profile Comparison

| Profile | Eligibility rule | Selected representative cases | Avg MFE90 | Avg MAE90 | Avg MFE180 | Avg MAE180 | Verdict |
|---|---|---:|---:|---:|---:|---:|---|
| P0 current calibrated proxy | Backlog / orderbook headline can support Actionable if confidence is high | 8 | 27.06 | -13.89 | 58.08 | -13.89 | Mixed; catches winners but allows high-MAE inherited/supplier cases. |
| P1 L1 sector bridge rule | Requires backlog + visible margin/revision or conversion bridge | 4 | 44.84 | -3.41 | 85.81 | -3.41 | Strong alignment with clean C01 winners. |
| P2 C01 counterexample guard | Blocks inherited backlog, M&A synergy, revenue-delay and supplier beta without entity bridge | 4 blocked | 9.29 | -24.38 | 30.36 | -24.38 | Prevents false positives and MAE-heavy entries. |
| P3 local 4B overlay | Price extension without incremental non-price bridge moves to Watch, not full 4C | 1 overlay | 3.54 | -21.40 | 33.45 | -21.40 | Supports local 4B watch while avoiding premature thesis-break classification. |

## 14. Current Profile Error Analysis

The current calibrated profile already has useful guardrails: Stage2 requires a bridge, price-only blowoff should not become positive evidence, and full 4B requires non-price deterioration. The remaining C01 residual is more specific:

- group-level shipbuilding backlog can be inherited too easily by smaller listed entities;
- supplier beta can be mistaken for direct order conversion;
- M&A or vertical-integration synergy can be mistaken for backlog-to-margin proof;
- revenue-recognition delay and working-capital drag must be explicit red-team fields;
- old backlog evidence should decay into local 4B watch after price extension unless fresh OPM/revision/FCF evidence appears.

## 15. Residual Contribution Summary

```json
{
  "loop_objective": "coverage_gap_fill + residual_false_positive_mining + residual_missed_structural_mining + canonical_archetype_specific_rule_discovery + 4B_non_price_requirement_stress_test",
  "new_independent_case_count": 8,
  "reused_case_count": 1,
  "same_archetype_new_symbol_count": 8,
  "same_archetype_new_trigger_family_count": 9,
  "calibration_usable_trigger_count": 9,
  "representative_trigger_count": 8,
  "positive_case_count": 4,
  "counterexample_count": 4,
  "stage4b_case_count": 1,
  "stage4c_case_count": 0,
  "current_profile_error_count": 5,
  "source_proxy_only_count": 0,
  "evidence_url_pending_count": 0,
  "diversity_score_summary": "new symbols 8 / representative triggers 8 / positive-counterexample balance 4:4 / same-case supplemental trigger 1",
  "sector_specific_rule_candidate": true,
  "canonical_archetype_rule_candidate": true,
  "loop_contribution_label": "canonical_archetype_rule_candidate"
}
```

## 16. Proposed Shadow Rule Candidate

```json
{
  "row_type": "residual_rule_candidate",
  "canonical_archetype_id": "C01_ORDER_BACKLOG_MARGIN_BRIDGE",
  "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID",
  "new_axis_proposed": "C01_verified_backlog_margin_fcf_bridge_required_before_Yellow_or_Green_plus_supplier_or_MA_synergy_high_MAE_guard",
  "existing_axis_strengthened": [
    "stage2_required_bridge",
    "local_4b_watch_guard",
    "price_only_blowoff_blocks_positive_stage",
    "full_4b_requires_non_price_evidence"
  ],
  "existing_axis_weakened": null,
  "proposed_shadow_rule": "For C01, Stage2 may be allowed by verified order backlog/backlog-duration evidence, but Yellow/Green requires at least one non-price bridge among OPM/revision, revenue conversion, FCF/working-capital improvement, or confirmed supplier order conversion. Supplier beta, group-level inherited backlog, or M&A/vertical-integration synergy is Watch-only until entity-level margin bridge appears. Local 4B watch should activate when prior backlog evidence is stale and price extension is not matched by incremental non-price confirmation.",
  "do_not_propose_new_weight_delta": false
}
```

## 17. Validation Scope

```json
{
  "stock_agent_code_access_allowed": false,
  "stock_agent_code_patch_allowed": false,
  "stock_agent_live_scan_allowed": false,
  "current_stock_discovery_allowed": false,
  "auto_trading_allowed": false,
  "brokerage_api_allowed": false,
  "production_scoring_changed": false,
  "shadow_weight_only": true,
  "handoff_prompt_embedded": true,
  "handoff_prompt_executed_now": false,
  "must_use_actual_stock_web_1D_OHLC": true,
  "all_usable_rows_have_entry_price_and_30_90_180_mfe_mae": true
}
```

## 18. Deferred Coding Agent Handoff Prompt — Do Not Execute In This Research Session

```text
You are the later batch implementation agent for stock_agent. Do not rerun live discovery. Read this MD only as one V12 calibration artifact. Extract JSONL trigger rows, stage_transition rows, score_simulation rows, and the residual_rule_candidate. Validate that all usable triggers have entry_date, entry_price, canonical trigger_type, 30/90/180D MFE/MAE, large_sector_id, canonical_archetype_id, and Stock-Web price source fields. If accepted, add the C01 shadow rule candidate to the v12 patch review queue as a canonical-archetype-specific bridge rule. Do not loosen Stage3-Green globally. Do not convert local 4B watch into full 4B or 4C without non-price deterioration evidence. Maintain anti-repeat key canonical_archetype_id + symbol + trigger_type + entry_date.
```

## 19. Next Recommended Archetypes

`C28_SOFTWARE_SECURITY_CONTRACT_RETENTION`, `C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK`, `C05_EPC_MEGA_CONTRACT_MARGIN_GAP`, `C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION`
