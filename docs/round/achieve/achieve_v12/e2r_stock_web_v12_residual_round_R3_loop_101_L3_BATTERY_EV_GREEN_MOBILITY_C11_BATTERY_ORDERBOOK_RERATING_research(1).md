---
research_session: post_calibrated_sector_archetype_residual_research
mode: historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12
selected_round: R3
selected_loop: 101
selection_basis: docs/core/V12_Research_No_Repeat_Index.md
selected_priority_bucket: Priority 0
round_schedule_status: coverage_index_selected
round_sector_consistency: pass
large_sector_id: L3_BATTERY_EV_GREEN_MOBILITY
canonical_archetype_id: C11_BATTERY_ORDERBOOK_RERATING
fine_archetype_id: C11_CATHODE_CELL_ORDERBOOK_MARGIN_FCF_CONVERSION_BRIDGE
deep_sub_archetype_id: C11_DEEP_HIGH_NICKEL_CATHODE_CELL_LONG_TERM_ORDERBOOK_BRIDGE_VS_CUSTOMER_CALLOFF_AND_MARGIN_LAG
primary_price_source: Songdaiki/stock-web
price_basis: tradable_raw
price_adjustment_status: raw_unadjusted_marcap
stock_web_manifest_max_date: 2026-02-20
upstream_source: FinanceData/marcap
production_scoring_changed: false
shadow_weight_only: true
handoff_prompt_embedded: true
handoff_prompt_executed_now: false
created_at_kst: 2026-06-13T18:52:34+09:00
---

# E2R Stock-Web v12 Residual Research — R3 / C11 Battery Orderbook Rerating

## 0. Executive Summary

This standalone Markdown file follows the v12 Stock-Web historical calibration prompt. It is a historical calibration artifact only: no live watchlist, no trading instruction, no production code patch, and no active scoring mutation.

- **Selected target:** `C11_BATTERY_ORDERBOOK_RERATING`
- **Reason:** the No-Repeat coverage ledger places C11 in Priority 0 with 18 rows, still below the 30-row floor.
- **Loop:** visible C11 compact archive reached loop 100, so this artifact uses loop 101.
- **New independent cases:** 6
- **Usable trigger rows:** 8, including 2 local 4B overlay rows.
- **Representative trigger rows:** 6
- **Positive cases:** 2
- **Counterexamples:** 4
- **Local 4B cases:** 2
- **Narrative-only 4C confirmation:** 1, L&F 2025 contract-scale reduction; not included as calibration-usable trigger because the Stock-Web manifest ends at 2026-02-20.
- **Current profile residual errors:** 5
- **Rule candidate:** require verified orderbook-to-margin/FCF/revision bridge before C11 can move to Yellow/Green; route parent-proxy, late-cycle contract-size, and capex-heavy volume contracts to Watch or local 4B.

## 1. Stock-Web Price Source Validation

The run uses `Songdaiki/stock-web` tradable OHLCV shards, upstream `FinanceData/marcap`, raw/unadjusted OHLC, and manifest `max_date=2026-02-20`. Every calibration-usable trigger has a complete 180-trading-day forward window inside the manifest date.

```jsonl
{"row_type": "price_source_validation", "source": "Songdaiki/stock-web", "source_url": "https://github.com/Songdaiki/stock-web", "manifest_path": "atlas/manifest.json", "schema_path": "atlas/schema.json", "universe_path": "atlas/universe/all_symbols.csv", "manifest_max_date": "2026-02-20", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "raw_shard_root": "atlas/ohlcv_raw_by_symbol_year", "validation_status": "usable_for_historical_calibration", "upstream_source": "FinanceData/marcap"}
```

## 2. Coverage-Index Selection

C11 was selected by coverage gap, not by sequential round cycling. Earlier session artifacts already filled C02, C09, C14, C10, C06, and C07. The next remaining Priority 0 target is C11.

```text
selected_round = R3
selected_loop = 101
selected_priority_bucket = Priority 0
large_sector_id = L3_BATTERY_EV_GREEN_MOBILITY
canonical_archetype_id = C11_BATTERY_ORDERBOOK_RERATING
fine_archetype_id = C11_CATHODE_CELL_ORDERBOOK_MARGIN_FCF_CONVERSION_BRIDGE
deep_sub_archetype_id = C11_DEEP_HIGH_NICKEL_CATHODE_CELL_LONG_TERM_ORDERBOOK_BRIDGE_VS_CUSTOMER_CALLOFF_AND_MARGIN_LAG
anti_repeat_key = canonical_archetype_id + symbol + trigger_type + entry_date
```

## 3. Hypothesis

C11 should not mean “battery headline went up.” The durable mechanism is narrower:

1. customer/orderbook quality becomes visible,
2. capacity or utilization is economically locked,
3. ASP/mix or spread supports margin,
4. margin/revision/FCF confirms the orderbook is not just revenue volume,
5. price extension is demoted to local 4B watch when incremental non-price evidence stalls.

In short: **orderbook is the door; margin/FCF is the room.** C11 should score the investor only after the thesis walks through the door and stays in the room.

## 4. Canonical Compression Map

```json
{
  "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY",
  "canonical_archetype_id": "C11_BATTERY_ORDERBOOK_RERATING",
  "fine_archetype_id": "C11_CATHODE_CELL_ORDERBOOK_MARGIN_FCF_CONVERSION_BRIDGE",
  "deep_sub_archetype_id": "C11_DEEP_HIGH_NICKEL_CATHODE_CELL_LONG_TERM_ORDERBOOK_BRIDGE_VS_CUSTOMER_CALLOFF_AND_MARGIN_LAG",
  "included_subtypes": [
    "cathode_long_term_customer_contract",
    "direct_customer_high_MAE_orderbook",
    "late_cycle_cathode_contract_size_trap",
    "cell_JV_capacity_parent_proxy",
    "cell_customer_orderbook_capex_drag",
    "late_orderbook_blowoff_local_4B_watch"
  ],
  "excluded_subtypes": [
    "C12_customer_calloff_risk_only_without_initial_orderbook_rerating",
    "C13_AMPC_IRA_JV_utilization_subsidy_only",
    "C14_EV_demand_slowdown_without_orderbook_origin"
  ]
}
```

## 5. Evidence Source Map

| Symbol | Company | Trigger evidence | Evidence route | C11 relevance |
|---|---|---|---|---|
| 003670 | POSCO Future M | 2023-01-30 | POSCO Future M / POSCO Newsroom / Yonhap | 10-year, KRW 40T NCA cathode order from Samsung SDI. Direct long-term orderbook bridge. |
| 066970 | L&F | 2023-02-28 | Reuters / later Reuters contract reduction | KRW 3.83T Tesla cathode order; strong initial MFE but later severe MAE and 2025 scale cut. |
| 247540 | EcoPro BM | 2023-12-01 | KED Global / Korea JoongAng Daily | KRW 44T Samsung SDI cathode deal, but late-cycle entry without margin/FCF confirmation. |
| 006400 | Samsung SDI | 2023-04-26 | Samsung SDI / GM / Reuters | More-than-30GWh GM JV capacity; parent-level capex and margin bridge required. |
| 373220 | LG Energy Solution | 2023-10-05 | LGES / Toyota / Reuters | 20GWh annual Toyota supply; volume orderbook did not prevent drawdown without margin bridge. |
| 096770 | SK Innovation | 2021-05-20 | Ford / Reuters | BlueOvalSK 60GWh MoU; parent-proxy capacity headline did not become durable rerating. |

## 6. Corporate Action / Contamination Check

| Symbol | Profile path | Corporate action contamination note |
|---|---|---|
| 003670 | `atlas/symbol_profiles/003/003670.json` | Known candidate dates 2015-05-04 and 2021-02-03; no overlap with 2023 trigger/180D window. |
| 066970 | `atlas/symbol_profiles/066/066970.json` | Known candidate dates 2016-02-19 and 2021-08-11; no overlap with 2023 trigger/180D window. |
| 247540 | `atlas/symbol_profiles/247/247540.json` | Known candidate dates 2022-06-27 and 2022-07-15; no overlap with 2023-12 trigger/180D window. |
| 006400 | `atlas/symbol_profiles/006/006400.json` | Older candidate dates only; no overlap with 2023 trigger/180D window. |
| 373220 | `atlas/symbol_profiles/373/373220.json` | No corporate action candidates in profile. |
| 096770 | `atlas/symbol_profiles/096/096770.json` | Known candidate date 2024-11-20; no overlap with 2021 trigger/180D window. |


## 7. Trigger-Level Backtest Summary

| Symbol | Company | Trigger | Entry | Entry Price | MFE90 | MAE90 | MFE180 | MAE180 | Verdict |
|---|---|---|---:|---:|---:|---:|---:|---:|---|
| 003670 | POSCO Future M / 포스코퓨처엠 | Stage2-Actionable | 2023-01-31 | 224000 | 88.62 | -5.58 | 209.82 | -5.58 | current_profile_correct_for_stage2_but_needs_local_4B_after_blowoff |
| 066970 | L&F / 엘앤에프 | Stage2-Actionable | 2023-03-02 | 250500 | 39.52 | -12.57 | 39.52 | -48.94 | current_profile_4B_too_late_if_contract_memory_extended_to_green |
| 247540 | EcoPro BM / 에코프로비엠 | Stage2-Actionable | 2023-12-04 | 323000 | 9.60 | -34.67 | 9.60 | -49.23 | current_profile_false_positive_if_contract_size_promotes_yellow |
| 006400 | Samsung SDI / 삼성SDI | Stage2-Actionable | 2023-04-27 | 706000 | 5.52 | -17.42 | 5.52 | -49.86 | current_profile_false_positive_if_JV_capacity_substitutes_for_parent_margin |
| 373220 | LG Energy Solution / LG에너지솔루션 | Stage2-Actionable | 2023-10-06 | 464000 | 7.97 | -21.98 | 7.97 | -30.50 | current_profile_false_positive_if_volume_contract_overrides_margin_bridge |
| 096770 | SK Innovation / SK이노베이션 | Stage2-Actionable | 2021-05-21 | 280000 | 7.86 | -19.46 | 7.86 | -31.07 | current_profile_false_positive_if_JV_capacity_promotes_actionable_without_margin_bridge |


## 8. Local 4B Overlay Rows

| Symbol | Company | 4B Entry | Entry Price | Local peak proximity | MFE180 | MAE180 | Why 4B |
|---|---|---:|---:|---:|---:|---:|---|
| 003670 | POSCO Future M / 포스코퓨처엠 | 2023-07-26 | 560000 | 71.49% | 23.93 | -58.66 | late-July cathode-material blowoff after the valid early POSCO orderbook rerating; non-price bridge no longer caught up with price extension |
| 066970 | L&F / 엘앤에프 | 2023-04-03 | 328000 | 78.28% | 6.55 | -61.01 | local peak after Tesla order reaction; orderbook memory should move to 4B watch unless margin/FCF bridge confirms durability |


## 9. Positive / Counterexample Balance

```text
positive_case_count = 2
counterexample_count = 4
stage4b_case_count = 2
stage4c_case_count = 1 narrative_only_not_calibration_usable
current_profile_error_count = 5
source_proxy_only_count = 0
evidence_url_pending_count = 0
```

The positive cases are not “battery winners”; they are orderbook rows that either delivered strong forward MFE or were useful Stage2 positives before a later 4B watch. Counterexamples are cases where contract size, JV capacity, or global customer identity looked impressive but failed to protect 90D/180D MAE.

## 10. Case Notes

### 10.1 POSCO Future M — valid C11 orderbook, later local 4B

The Samsung SDI 10-year KRW 40T cathode contract is a clean C11 Stage2 trigger. The path confirms that early orderbook evidence could support Actionable and Yellow. However, the same row also teaches the late-cycle rule: after the July battery-material blowoff, price outran fresh margin/revision evidence and should enter local 4B watch.

### 10.2 L&F — Stage2-positive, Green-block, later 4C narrative

The Tesla order produced high MFE quickly, so it is not a simple false positive. The problem is durability. MAE deepened sharply after the peak, and the 2025 contract-scale reduction confirms that customer orderbook without call-off/margin durability should not be allowed to carry Green.

### 10.3 EcoPro BM — direct contract but late-cycle trap

The Samsung SDI KRW 44T contract is real evidence, but the December 2023 entry appears after the large cathode rerating wave. The forward path is dominated by MAE, not fresh MFE. C11 must therefore include a late-cycle valuation and EV demand guard.

### 10.4 Samsung SDI — JV capacity is not parent-level margin

A GM JV capacity plan can be strategically important while still failing as a listed-parent Stage3 trigger. The parent has capex, utilization, pricing, and FCF burden. C11 should not substitute JV capacity for parent margin bridge.

### 10.5 LG Energy Solution — volume orderbook versus capex drag

Toyota 20GWh annual supply is a strong customer headline, but the stock path shows that volume orderbook alone does not secure rerating. C11 Yellow needs operating-margin or revision bridge, not just shipment volume.

### 10.6 SK Innovation — parent-proxy and legal/margin risk

BlueOvalSK capacity gave a plausible battery orderbook story, but SK Innovation had parent-level legal, capex, and profitability complexity. This row strengthens the parent-proxy guard.

## 11. Machine-Readable Trigger Rows — JSONL

```jsonl
{"row_type": "price_source_validation", "source": "Songdaiki/stock-web", "source_url": "https://github.com/Songdaiki/stock-web", "manifest_path": "atlas/manifest.json", "schema_path": "atlas/schema.json", "universe_path": "atlas/universe/all_symbols.csv", "manifest_max_date": "2026-02-20", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "raw_shard_root": "atlas/ohlcv_raw_by_symbol_year", "validation_status": "usable_for_historical_calibration", "upstream_source": "FinanceData/marcap"}
{"row_id": "R3L101-C11-001", "case_id": "C11_003670_2023-01-31_STAGE2_POSCO_SDI_CATHODE_ORDERBOOK", "symbol": "003670", "company_name": "POSCO Future M / 포스코퓨처엠", "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C11_BATTERY_ORDERBOOK_RERATING", "trigger_type": "Stage2-Actionable", "trigger_family": "cathode_long_term_orderbook_customer_bridge", "trigger_date": "2023-01-30", "entry_date": "2023-01-31", "entry_price": 224000.0, "price_data_source": "Songdaiki/stock-web", "upstream_source": "FinanceData/marcap", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "calibration_usable": true, "forward_window_status": "complete_180D_within_manifest_max_date", "corporate_action_window_contaminated": false, "source_proxy_only": false, "evidence_url_pending": false, "evidence_summary": "POSCO Chemical/Future M announced a 10-year high-nickel NCA cathode supply contract to Samsung SDI worth KRW 40T. This is a direct C11 orderbook bridge, but Green still needs margin/revision confirmation.", "baseline_profile_decision": "Stage2-Actionable / possible Yellow if contract quality bridge verified", "proposed_profile_decision": "Stage2-Actionable; Yellow only after margin/revision bridge; local 4B after blowoff", "current_profile_verdict": "current_profile_correct_for_stage2_but_needs_local_4B_after_blowoff", "current_profile_error": false, "outcome_label": "positive_structural_rerating_then_late_blowoff_watch", "case_role": "positive", "representative_trigger": true, "aggregate_group_role": "representative_case", "MFE_30D_pct": 20.54, "MAE_30D_pct": -5.58, "MFE_90D_pct": 88.62, "MAE_90D_pct": -5.58, "MFE_180D_pct": 209.82, "MAE_180D_pct": -5.58, "MFE_250D_pct": 209.82, "MAE_250D_pct": -5.58, "MFE_500D_pct": 209.82, "MAE_500D_pct": -45.22, "peak_date_180D": "2023-07-26", "peak_price_180D": 694000.0, "trough_date_180D": "2023-02-23", "trough_price_180D": 211500.0, "drawdown_after_peak_180D_pct": -60.52, "below_entry_within_30D": true, "below_entry_within_90D": true, "novelty_key": "C11_BATTERY_ORDERBOOK_RERATING|003670|Stage2-Actionable|2023-01-31", "dedupe_status": "new_independent_case", "price_path_anchor_urls": ["https://github.com/Songdaiki/stock-web/blob/main/atlas/ohlcv_tradable_by_symbol_year/003/003670/2023.csv?plain=1", "https://github.com/Songdaiki/stock-web/blob/main/atlas/symbol_profiles/003/003670.json?plain=1"], "source_urls": ["https://www.poscofuturem.com/en/pr/view.do?num=658", "https://newsroom.posco.com/en/posco-chemical-lands-40-trillion-krw-cathode-materials-supply-contract-for-samsung-sdis-batteries/", "https://en.yna.co.kr/view/AEN20230130007400320"], "fine_archetype_id": "C11_CATHODE_ORDERBOOK_LONG_TERM_CUSTOMER_MARGIN_BRIDGE", "deep_sub_archetype_id": "C11_DEEP_NCA_CATHODE_SDI_10Y_ORDERBOOK_VERTICAL_INTEGRATION_VS_LITHIUM_BETA", "entry_price_field": "close"}
{"row_id": "R3L101-C11-002", "case_id": "C11_066970_2023-03-02_STAGE2_LNF_TESLA_CATHODE_ORDERBOOK_HIGH_MAE", "symbol": "066970", "company_name": "L&F / 엘앤에프", "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C11_BATTERY_ORDERBOOK_RERATING", "trigger_type": "Stage2-Actionable", "trigger_family": "cathode_customer_orderbook_high_MAE_bridge", "trigger_date": "2023-02-28", "entry_date": "2023-03-02", "entry_price": 250500.0, "price_data_source": "Songdaiki/stock-web", "upstream_source": "FinanceData/marcap", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "calibration_usable": true, "forward_window_status": "complete_180D_within_manifest_max_date", "corporate_action_window_contaminated": false, "source_proxy_only": false, "evidence_url_pending": false, "evidence_summary": "L&F disclosed a KRW 3.83T Tesla cathode supply order for 2024-2025. The stock produced a strong 30/90D MFE, but the path later suffered severe MAE and the contract scale was later cut, making it a Stage2-positive but Green-block/4B guard example.", "baseline_profile_decision": "Stage2-Actionable or Yellow if contract size overweighted", "proposed_profile_decision": "Stage2-Actionable only; Green blocked until margin/FCF and customer call-off durability verified", "current_profile_verdict": "current_profile_4B_too_late_if_contract_memory_extended_to_green", "current_profile_error": true, "outcome_label": "positive_stage2_high_MAE_not_green", "case_role": "positive_high_MAE_guard", "representative_trigger": true, "aggregate_group_role": "representative_case", "MFE_30D_pct": 39.52, "MAE_30D_pct": -12.57, "MFE_90D_pct": 39.52, "MAE_90D_pct": -12.57, "MFE_180D_pct": 39.52, "MAE_180D_pct": -48.94, "MFE_250D_pct": 39.52, "MAE_250D_pct": -48.94, "MFE_500D_pct": 39.52, "MAE_500D_pct": -72.18, "peak_date_180D": "2023-04-03", "peak_price_180D": 349500.0, "trough_date_180D": "2023-11-01", "trough_price_180D": 127900.0, "drawdown_after_peak_180D_pct": -63.4, "below_entry_within_30D": true, "below_entry_within_90D": true, "novelty_key": "C11_BATTERY_ORDERBOOK_RERATING|066970|Stage2-Actionable|2023-03-02", "dedupe_status": "new_independent_case", "price_path_anchor_urls": ["https://github.com/Songdaiki/stock-web/blob/main/atlas/ohlcv_tradable_by_symbol_year/066/066970/2023.csv?plain=1", "https://github.com/Songdaiki/stock-web/blob/main/atlas/symbol_profiles/066/066970.json?plain=1"], "source_urls": ["https://www.reuters.com/business/autos-transportation/skoreas-lf-wins-29-bln-order-tesla-its-affiliates-2023-02-28/", "https://www.reuters.com/world/asia-pacific/south-koreas-lf-says-value-battery-material-supply-deal-tesla-cut-7386-2025-12-29/", "https://pulse.mk.co.kr/news/english/11918715"], "fine_archetype_id": "C11_CATHODE_DIRECT_CUSTOMER_ORDERBOOK_MARGIN_DURABILITY_TEST", "deep_sub_archetype_id": "C11_DEEP_TESLA_4680_CATHODE_ORDERBOOK_HIGH_MAE_VS_CALLOFF_AND_CONTRACT_SCALE_CUT", "entry_price_field": "close"}
{"row_id": "R3L101-C11-003", "case_id": "C11_247540_2023-12-04_STAGE2_ECOPROBM_SDI_ORDERBOOK_TOO_LATE", "symbol": "247540", "company_name": "EcoPro BM / 에코프로비엠", "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C11_BATTERY_ORDERBOOK_RERATING", "trigger_type": "Stage2-Actionable", "trigger_family": "cathode_orderbook_late_cycle_false_positive", "trigger_date": "2023-12-01", "entry_date": "2023-12-04", "entry_price": 323000.0, "price_data_source": "Songdaiki/stock-web", "upstream_source": "FinanceData/marcap", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "calibration_usable": true, "forward_window_status": "complete_180D_within_manifest_max_date", "corporate_action_window_contaminated": false, "source_proxy_only": false, "evidence_url_pending": false, "evidence_summary": "EcoPro BM signed a five-year, KRW 44T high-nickel cathode supply agreement with Samsung SDI. Despite direct C11 evidence, the entry sat after the battery-material rerating wave and lacked fresh margin/FCF durability.", "baseline_profile_decision": "Stage2-Actionable / Yellow if contract size overweighted", "proposed_profile_decision": "Stage2-Watch or Actionable only after margin/revision bridge; late-cycle valuation guard active", "current_profile_verdict": "current_profile_false_positive_if_contract_size_promotes_yellow", "current_profile_error": true, "outcome_label": "counterexample_late_orderbook_not_rerating", "case_role": "counterexample", "representative_trigger": true, "aggregate_group_role": "representative_case", "MFE_30D_pct": 9.6, "MAE_30D_pct": -17.96, "MFE_90D_pct": 9.6, "MAE_90D_pct": -34.67, "MFE_180D_pct": 9.6, "MAE_180D_pct": -49.23, "MFE_250D_pct": 9.6, "MAE_250D_pct": -62.72, "MFE_500D_pct": 9.6, "MAE_500D_pct": -74.89, "peak_date_180D": "2023-12-04", "peak_price_180D": 354000.0, "trough_date_180D": "2024-08-05", "trough_price_180D": 164000.0, "drawdown_after_peak_180D_pct": -53.67, "below_entry_within_30D": true, "below_entry_within_90D": true, "novelty_key": "C11_BATTERY_ORDERBOOK_RERATING|247540|Stage2-Actionable|2023-12-04", "dedupe_status": "new_independent_case", "price_path_anchor_urls": ["https://github.com/Songdaiki/stock-web/blob/main/atlas/ohlcv_tradable_by_symbol_year/247/247540/2023.csv?plain=1", "https://github.com/Songdaiki/stock-web/blob/main/atlas/symbol_profiles/247/247540.json?plain=1"], "source_urls": ["https://www.kedglobal.com/batteries/newsView/ked202312030001", "https://koreajoongangdaily.joins.com/news/2023-12-03/business/industry/EcoPro-BM-secures-34-billion-deal-as-Samsung-SDIs-cathode-supplier/1926748"], "fine_archetype_id": "C11_CATHODE_ORDERBOOK_LATE_CYCLE_MARGIN_FCF_GUARD", "deep_sub_archetype_id": "C11_DEEP_SDI_44T_CATHODE_ORDERBOOK_LATE_STAGE_VALUATION_AND_EV_DEMAND_GUARD", "entry_price_field": "close"}
{"row_id": "R3L101-C11-004", "case_id": "C11_006400_2023-04-27_STAGE2_SDI_GM_JV_CAPACITY_PARENT_PROXY", "symbol": "006400", "company_name": "Samsung SDI / 삼성SDI", "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C11_BATTERY_ORDERBOOK_RERATING", "trigger_type": "Stage2-Actionable", "trigger_family": "battery_cell_JV_capacity_parent_proxy_guard", "trigger_date": "2023-04-26", "entry_date": "2023-04-27", "entry_price": 706000.0, "price_data_source": "Songdaiki/stock-web", "upstream_source": "FinanceData/marcap", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "calibration_usable": true, "forward_window_status": "complete_180D_within_manifest_max_date", "corporate_action_window_contaminated": false, "source_proxy_only": false, "evidence_url_pending": false, "evidence_summary": "Samsung SDI and GM planned a more-than-30GWh U.S. battery JV. This is C11-adjacent capacity/orderbook visibility, but the listed-parent path requires capex, utilization, and margin bridge rather than JV headline alone.", "baseline_profile_decision": "Stage2-Actionable if JV capacity treated as backlog", "proposed_profile_decision": "Stage2-Watch until utilization/margin/FCF bridge appears", "current_profile_verdict": "current_profile_false_positive_if_JV_capacity_substitutes_for_parent_margin", "current_profile_error": true, "outcome_label": "counterexample_parent_proxy_capacity_not_margin_bridge", "case_role": "counterexample", "representative_trigger": true, "aggregate_group_role": "representative_case", "MFE_30D_pct": 5.52, "MAE_30D_pct": -7.22, "MFE_90D_pct": 5.52, "MAE_90D_pct": -17.42, "MFE_180D_pct": 5.52, "MAE_180D_pct": -49.86, "MFE_250D_pct": 5.52, "MAE_250D_pct": -51.56, "MFE_500D_pct": 5.52, "MAE_500D_pct": -77.25, "peak_date_180D": "2023-06-12", "peak_price_180D": 745000.0, "trough_date_180D": "2024-01-23", "trough_price_180D": 354000.0, "drawdown_after_peak_180D_pct": -52.48, "below_entry_within_30D": true, "below_entry_within_90D": true, "novelty_key": "C11_BATTERY_ORDERBOOK_RERATING|006400|Stage2-Actionable|2023-04-27", "dedupe_status": "new_independent_case", "price_path_anchor_urls": ["https://github.com/Songdaiki/stock-web/blob/main/atlas/ohlcv_tradable_by_symbol_year/006/006400/2023.csv?plain=1", "https://github.com/Songdaiki/stock-web/blob/main/atlas/symbol_profiles/006/006400.json?plain=1"], "source_urls": ["https://www.samsungsdi.com/sdi-now/sdi-news/3162.html?idx=3162&pageIndex=2&pagesize=15", "https://news.gm.com/home.detail.html/Pages/news/us/en/2023/apr/0426-samsungsdi.html", "https://www.reuters.com/business/autos-transportation/gm-samsung-sdi-plan-build-new-us-battery-plant-sources-2023-04-24/"], "fine_archetype_id": "C11_CELL_JV_CAPACITY_ORDERBOOK_PARENT_MARGIN_BRIDGE_GUARD", "deep_sub_archetype_id": "C11_DEEP_GM_JV_30GWH_CAPACITY_PARENT_PROXY_VS_FCF_AND_CAPEX_DRAG", "entry_price_field": "close"}
{"row_id": "R3L101-C11-005", "case_id": "C11_373220_2023-10-06_STAGE2_LGES_TOYOTA_ORDERBOOK_CAPEX_DRAG", "symbol": "373220", "company_name": "LG Energy Solution / LG에너지솔루션", "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C11_BATTERY_ORDERBOOK_RERATING", "trigger_type": "Stage2-Actionable", "trigger_family": "battery_cell_customer_orderbook_capex_drag_guard", "trigger_date": "2023-10-05", "entry_date": "2023-10-06", "entry_price": 464000.0, "price_data_source": "Songdaiki/stock-web", "upstream_source": "FinanceData/marcap", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "calibration_usable": true, "forward_window_status": "complete_180D_within_manifest_max_date", "corporate_action_window_contaminated": false, "source_proxy_only": false, "evidence_url_pending": false, "evidence_summary": "LGES signed a long-term Toyota supply agreement for annual 20GWh starting 2025. The contract is real, but the stock path shows that orderbook volume without margin/FCF bridge can still be punished.", "baseline_profile_decision": "Stage2-Actionable / Yellow if global OEM order overweighted", "proposed_profile_decision": "Stage2-Watch or Actionable only; Yellow requires operating-margin/revision bridge", "current_profile_verdict": "current_profile_false_positive_if_volume_contract_overrides_margin_bridge", "current_profile_error": true, "outcome_label": "counterexample_orderbook_without_margin_FCF_bridge", "case_role": "counterexample", "representative_trigger": true, "aggregate_group_role": "representative_case", "MFE_30D_pct": 7.97, "MAE_30D_pct": -19.07, "MFE_90D_pct": 7.97, "MAE_90D_pct": -21.98, "MFE_180D_pct": 7.97, "MAE_180D_pct": -30.5, "MFE_250D_pct": 7.97, "MAE_250D_pct": -32.97, "MFE_500D_pct": 13.58, "MAE_500D_pct": -42.67, "peak_date_180D": "2023-10-12", "peak_price_180D": 501000.0, "trough_date_180D": "2024-06-28", "trough_price_180D": 322500.0, "drawdown_after_peak_180D_pct": -35.63, "below_entry_within_30D": true, "below_entry_within_90D": true, "novelty_key": "C11_BATTERY_ORDERBOOK_RERATING|373220|Stage2-Actionable|2023-10-06", "dedupe_status": "new_independent_case", "price_path_anchor_urls": ["https://github.com/Songdaiki/stock-web/blob/main/atlas/ohlcv_tradable_by_symbol_year/373/373220/2023.csv?plain=1", "https://github.com/Songdaiki/stock-web/blob/main/atlas/symbol_profiles/373/373220.json?plain=1"], "source_urls": ["https://news.lgensol.com/company-news/press-releases/2177/", "https://global.toyota/en/newsroom/corporate/39865919.html", "https://www.reuters.com/business/autos-transportation/lg-energy-solution-signs-supply-agreement-with-toyota-2023-10-04/"], "fine_archetype_id": "C11_CELL_CUSTOMER_ORDERBOOK_CAPEX_MARGIN_FCF_BRIDGE", "deep_sub_archetype_id": "C11_DEEP_TOYOTA_20GWH_ORDERBOOK_CAPEX_DRAG_VS_OPERATING_MARGIN_REVISION", "entry_price_field": "close"}
{"row_id": "R3L101-C11-006", "case_id": "C11_096770_2021-05-21_STAGE2_SK_FORD_JV_PARENT_PROXY", "symbol": "096770", "company_name": "SK Innovation / SK이노베이션", "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C11_BATTERY_ORDERBOOK_RERATING", "trigger_type": "Stage2-Actionable", "trigger_family": "battery_cell_JV_orderbook_parent_proxy_guard", "trigger_date": "2021-05-20", "entry_date": "2021-05-21", "entry_price": 280000.0, "price_data_source": "Songdaiki/stock-web", "upstream_source": "FinanceData/marcap", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "calibration_usable": true, "forward_window_status": "complete_180D_within_manifest_max_date", "corporate_action_window_contaminated": false, "source_proxy_only": false, "evidence_url_pending": false, "evidence_summary": "Ford and SK Innovation signed an MoU to form BlueOvalSK with approximately 60GWh annual battery-cell capacity. The path is a parent-proxy counterexample: capacity/orderbook headlines did not translate into durable listed-parent margin/FCF rerating.", "baseline_profile_decision": "Stage2-Actionable if JV orderbook is credited directly", "proposed_profile_decision": "Stage2-Watch unless parent-level margin/FCF bridge and legal-risk pass appear", "current_profile_verdict": "current_profile_false_positive_if_JV_capacity_promotes_actionable_without_margin_bridge", "current_profile_error": true, "outcome_label": "counterexample_parent_proxy_capacity_not_FCF", "case_role": "counterexample", "representative_trigger": true, "aggregate_group_role": "representative_case", "MFE_30D_pct": 7.86, "MAE_30D_pct": -6.43, "MFE_90D_pct": 7.86, "MAE_90D_pct": -19.46, "MFE_180D_pct": 7.86, "MAE_180D_pct": -31.07, "MFE_250D_pct": 7.86, "MAE_250D_pct": -32.68, "MFE_500D_pct": 7.86, "MAE_500D_pct": -49.11, "peak_date_180D": "2021-06-24", "peak_price_180D": 302000.0, "trough_date_180D": "2021-12-01", "trough_price_180D": 193000.0, "drawdown_after_peak_180D_pct": -36.09, "below_entry_within_30D": true, "below_entry_within_90D": true, "novelty_key": "C11_BATTERY_ORDERBOOK_RERATING|096770|Stage2-Actionable|2021-05-21", "dedupe_status": "new_independent_case", "price_path_anchor_urls": ["https://github.com/Songdaiki/stock-web/blob/main/atlas/ohlcv_tradable_by_symbol_year/096/096770/2021.csv?plain=1", "https://github.com/Songdaiki/stock-web/blob/main/atlas/symbol_profiles/096/096770.json?plain=1"], "source_urls": ["https://corporate.ford.com/articles/electrification/ford-commits-to-manufacturing-batteries/www.ford.com/corporate/articles/electrification/ford-commits-to-manufacturing-batteries/", "https://www.reuters.com/business/autos-transportation/skorea-battery-maker-sk-innovation-ford-motor-create-jv-ev-batteries-2021-05-20/"], "fine_archetype_id": "C11_CELL_JV_ORDERBOOK_PARENT_PROXY_LEGAL_MARGIN_GUARD", "deep_sub_archetype_id": "C11_DEEP_BLUEOVALSK_60GWH_PARENT_PROXY_VS_BATTERY_LOSS_AND_LEGAL_RISK", "entry_price_field": "close"}
{"row_id": "R3L101-C11-007", "case_id": "C11_003670_2023-01-31_STAGE2_POSCO_SDI_CATHODE_ORDERBOOK_STAGE4B_OVERLAY", "symbol": "003670", "company_name": "POSCO Future M / 포스코퓨처엠", "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C11_BATTERY_ORDERBOOK_RERATING", "trigger_type": "Stage4B-Watch", "trigger_family": "late_orderbook_blowoff_local_4B_watch", "trigger_date": "2023-07-26", "entry_date": "2023-07-26", "entry_price": 560000.0, "price_data_source": "Songdaiki/stock-web", "upstream_source": "FinanceData/marcap", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "calibration_usable": true, "forward_window_status": "complete_180D_within_manifest_max_date", "corporate_action_window_contaminated": false, "source_proxy_only": false, "evidence_url_pending": false, "evidence_summary": "late-July cathode-material blowoff after the valid early POSCO orderbook rerating; non-price bridge no longer caught up with price extension", "baseline_profile_decision": "May remain Stage3-Yellow if old orderbook evidence is over-retained", "proposed_profile_decision": "local 4B watch; full 4B needs non-price deterioration; hard 4C not from price alone", "current_profile_verdict": "current_profile_4B_too_late_if_price_extension_ignored", "current_profile_error": true, "outcome_label": "local_4B_watch_supported", "case_role": "stage4b_overlay", "representative_trigger": false, "aggregate_group_role": "4B_overlay_only", "MFE_30D_pct": 23.93, "MAE_30D_pct": -28.57, "MFE_90D_pct": 23.93, "MAE_90D_pct": -58.66, "MFE_180D_pct": 23.93, "MAE_180D_pct": -58.66, "MFE_250D_pct": 23.93, "MAE_250D_pct": -62.95, "MFE_500D_pct": 23.93, "MAE_500D_pct": -82.41, "peak_date_180D": "2023-07-26", "peak_price_180D": 694000.0, "trough_date_180D": "2023-11-01", "trough_price_180D": 231500.0, "drawdown_after_peak_180D_pct": -66.64, "below_entry_within_30D": true, "below_entry_within_90D": true, "novelty_key": "C11_BATTERY_ORDERBOOK_RERATING|003670|Stage4B-Watch|2023-07-26", "dedupe_status": "same_case_new_trigger_family", "price_path_anchor_urls": ["https://github.com/Songdaiki/stock-web/blob/main/atlas/ohlcv_tradable_by_symbol_year/003/003670/2023.csv?plain=1", "https://github.com/Songdaiki/stock-web/blob/main/atlas/symbol_profiles/003/003670.json?plain=1"], "source_urls": ["https://www.poscofuturem.com/en/pr/view.do?num=658", "https://newsroom.posco.com/en/posco-chemical-lands-40-trillion-krw-cathode-materials-supply-contract-for-samsung-sdis-batteries/", "https://en.yna.co.kr/view/AEN20230130007400320"], "fine_archetype_id": "C11_LATE_BATTERY_ORDERBOOK_BLOWOFF_LOCAL_4B_WATCH", "deep_sub_archetype_id": "C11_DEEP_VALID_ORDERBOOK_AFTER_PRICE_EXTENSION_LOCAL_4B_VS_FULL_4C_CONFIRMATION", "entry_price_field": "close", "local_peak_proximity_from_stage2_to_4B_pct": 71.49}
{"row_id": "R3L101-C11-008", "case_id": "C11_066970_2023-03-02_STAGE2_LNF_TESLA_CATHODE_ORDERBOOK_HIGH_MAE_STAGE4B_OVERLAY", "symbol": "066970", "company_name": "L&F / 엘앤에프", "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C11_BATTERY_ORDERBOOK_RERATING", "trigger_type": "Stage4B-Watch", "trigger_family": "late_orderbook_blowoff_local_4B_watch", "trigger_date": "2023-04-03", "entry_date": "2023-04-03", "entry_price": 328000.0, "price_data_source": "Songdaiki/stock-web", "upstream_source": "FinanceData/marcap", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "calibration_usable": true, "forward_window_status": "complete_180D_within_manifest_max_date", "corporate_action_window_contaminated": false, "source_proxy_only": false, "evidence_url_pending": false, "evidence_summary": "local peak after Tesla order reaction; orderbook memory should move to 4B watch unless margin/FCF bridge confirms durability", "baseline_profile_decision": "May remain Stage3-Yellow if old orderbook evidence is over-retained", "proposed_profile_decision": "local 4B watch; full 4B needs non-price deterioration; hard 4C not from price alone", "current_profile_verdict": "current_profile_4B_too_late_if_price_extension_ignored", "current_profile_error": true, "outcome_label": "local_4B_watch_supported", "case_role": "stage4b_overlay", "representative_trigger": false, "aggregate_group_role": "4B_overlay_only", "MFE_30D_pct": 6.55, "MAE_30D_pct": -28.96, "MFE_90D_pct": 6.55, "MAE_90D_pct": -35.21, "MFE_180D_pct": 6.55, "MAE_180D_pct": -61.01, "MFE_250D_pct": 6.55, "MAE_250D_pct": -61.01, "MFE_500D_pct": 6.55, "MAE_500D_pct": -83.6, "peak_date_180D": "2023-04-03", "peak_price_180D": 349500.0, "trough_date_180D": "2023-11-01", "trough_price_180D": 127900.0, "drawdown_after_peak_180D_pct": -63.4, "below_entry_within_30D": true, "below_entry_within_90D": true, "novelty_key": "C11_BATTERY_ORDERBOOK_RERATING|066970|Stage4B-Watch|2023-04-03", "dedupe_status": "same_case_new_trigger_family", "price_path_anchor_urls": ["https://github.com/Songdaiki/stock-web/blob/main/atlas/ohlcv_tradable_by_symbol_year/066/066970/2023.csv?plain=1", "https://github.com/Songdaiki/stock-web/blob/main/atlas/symbol_profiles/066/066970.json?plain=1"], "source_urls": ["https://www.reuters.com/business/autos-transportation/skoreas-lf-wins-29-bln-order-tesla-its-affiliates-2023-02-28/", "https://www.reuters.com/world/asia-pacific/south-koreas-lf-says-value-battery-material-supply-deal-tesla-cut-7386-2025-12-29/", "https://pulse.mk.co.kr/news/english/11918715"], "fine_archetype_id": "C11_LATE_BATTERY_ORDERBOOK_BLOWOFF_LOCAL_4B_WATCH", "deep_sub_archetype_id": "C11_DEEP_VALID_ORDERBOOK_AFTER_PRICE_EXTENSION_LOCAL_4B_VS_FULL_4C_CONFIRMATION", "entry_price_field": "close", "local_peak_proximity_from_stage2_to_4B_pct": 78.28}
```

## 12. Stage Transition Rows — JSONL

```jsonl
{"row_type": "stage_transition", "row_id": "R3L101-C11-001", "symbol": "003670", "canonical_archetype_id": "C11_BATTERY_ORDERBOOK_RERATING", "trigger_type": "Stage2-Actionable", "entry_date": "2023-01-31", "transition_label": "Stage2_to_Yellow_supported_but_Green_requires_margin_revision_bridge", "mfe_mae_180_spread_pct": 204.24, "profile_residual": "current_profile_correct_for_stage2_but_needs_local_4B_after_blowoff"}
{"row_type": "stage_transition", "row_id": "R3L101-C11-002", "symbol": "066970", "canonical_archetype_id": "C11_BATTERY_ORDERBOOK_RERATING", "trigger_type": "Stage2-Actionable", "entry_date": "2023-03-02", "transition_label": "Stage2_to_Yellow_supported_but_Green_requires_margin_revision_bridge", "mfe_mae_180_spread_pct": -9.42, "profile_residual": "current_profile_4B_too_late_if_contract_memory_extended_to_green"}
{"row_type": "stage_transition", "row_id": "R3L101-C11-003", "symbol": "247540", "canonical_archetype_id": "C11_BATTERY_ORDERBOOK_RERATING", "trigger_type": "Stage2-Actionable", "entry_date": "2023-12-04", "transition_label": "Stage2_false_positive_or_Yellow_block_supported", "mfe_mae_180_spread_pct": -39.63, "profile_residual": "current_profile_false_positive_if_contract_size_promotes_yellow"}
{"row_type": "stage_transition", "row_id": "R3L101-C11-004", "symbol": "006400", "canonical_archetype_id": "C11_BATTERY_ORDERBOOK_RERATING", "trigger_type": "Stage2-Actionable", "entry_date": "2023-04-27", "transition_label": "Stage2_false_positive_or_Yellow_block_supported", "mfe_mae_180_spread_pct": -44.34, "profile_residual": "current_profile_false_positive_if_JV_capacity_substitutes_for_parent_margin"}
{"row_type": "stage_transition", "row_id": "R3L101-C11-005", "symbol": "373220", "canonical_archetype_id": "C11_BATTERY_ORDERBOOK_RERATING", "trigger_type": "Stage2-Actionable", "entry_date": "2023-10-06", "transition_label": "Stage2_false_positive_or_Yellow_block_supported", "mfe_mae_180_spread_pct": -22.53, "profile_residual": "current_profile_false_positive_if_volume_contract_overrides_margin_bridge"}
{"row_type": "stage_transition", "row_id": "R3L101-C11-006", "symbol": "096770", "canonical_archetype_id": "C11_BATTERY_ORDERBOOK_RERATING", "trigger_type": "Stage2-Actionable", "entry_date": "2021-05-21", "transition_label": "Stage2_false_positive_or_Yellow_block_supported", "mfe_mae_180_spread_pct": -23.21, "profile_residual": "current_profile_false_positive_if_JV_capacity_promotes_actionable_without_margin_bridge"}
{"row_type": "stage_transition", "row_id": "R3L101-C11-007", "symbol": "003670", "canonical_archetype_id": "C11_BATTERY_ORDERBOOK_RERATING", "trigger_type": "Stage4B-Watch", "entry_date": "2023-07-26", "transition_label": "Stage3_to_local_4B_watch_supported", "mfe_mae_180_spread_pct": -34.73, "profile_residual": "current_profile_4B_too_late_if_price_extension_ignored"}
{"row_type": "stage_transition", "row_id": "R3L101-C11-008", "symbol": "066970", "canonical_archetype_id": "C11_BATTERY_ORDERBOOK_RERATING", "trigger_type": "Stage4B-Watch", "entry_date": "2023-04-03", "transition_label": "Stage3_to_local_4B_watch_supported", "mfe_mae_180_spread_pct": -54.46, "profile_residual": "current_profile_4B_too_late_if_price_extension_ignored"}
```

## 13. Score Simulation Rows — JSONL

```jsonl
{"row_type": "score_simulation", "symbol": "003670", "canonical_archetype_id": "C11_BATTERY_ORDERBOOK_RERATING", "entry_date": "2023-01-31", "current_proxy_score": 82, "candidate_C11_guarded_score": 84, "current_proxy_stage": "Stage3-Yellow", "candidate_stage": "Stage3-Yellow", "delta": 2, "decision_reason": "Stage2-Actionable; Yellow only after margin/revision bridge; local 4B after blowoff"}
{"row_type": "score_simulation", "symbol": "066970", "canonical_archetype_id": "C11_BATTERY_ORDERBOOK_RERATING", "entry_date": "2023-03-02", "current_proxy_score": 81, "candidate_C11_guarded_score": 73, "current_proxy_stage": "Stage3-Yellow", "candidate_stage": "Stage2-Actionable", "delta": -8, "decision_reason": "Stage2-Actionable only; Green blocked until margin/FCF and customer call-off durability verified"}
{"row_type": "score_simulation", "symbol": "247540", "canonical_archetype_id": "C11_BATTERY_ORDERBOOK_RERATING", "entry_date": "2023-12-04", "current_proxy_score": 79, "candidate_C11_guarded_score": 66, "current_proxy_stage": "Stage3-Yellow", "candidate_stage": "Stage2-Watch", "delta": -13, "decision_reason": "Stage2-Watch or Actionable only after margin/revision bridge; late-cycle valuation guard active"}
{"row_type": "score_simulation", "symbol": "006400", "canonical_archetype_id": "C11_BATTERY_ORDERBOOK_RERATING", "entry_date": "2023-04-27", "current_proxy_score": 75, "candidate_C11_guarded_score": 64, "current_proxy_stage": "Stage3-Yellow", "candidate_stage": "Stage2-Watch", "delta": -11, "decision_reason": "Stage2-Watch until utilization/margin/FCF bridge appears"}
{"row_type": "score_simulation", "symbol": "373220", "canonical_archetype_id": "C11_BATTERY_ORDERBOOK_RERATING", "entry_date": "2023-10-06", "current_proxy_score": 76, "candidate_C11_guarded_score": 65, "current_proxy_stage": "Stage3-Yellow", "candidate_stage": "Stage2-Watch", "delta": -11, "decision_reason": "Stage2-Watch or Actionable only; Yellow requires operating-margin/revision bridge"}
{"row_type": "score_simulation", "symbol": "096770", "canonical_archetype_id": "C11_BATTERY_ORDERBOOK_RERATING", "entry_date": "2021-05-21", "current_proxy_score": 74, "candidate_C11_guarded_score": 62, "current_proxy_stage": "Stage2-Actionable", "candidate_stage": "Stage2-Watch", "delta": -12, "decision_reason": "Stage2-Watch unless parent-level margin/FCF bridge and legal-risk pass appear"}
```

## 14. Aggregate Row — JSON

```json
{
  "usable_trigger_rows": 8,
  "representative_trigger_rows": 6,
  "median_MFE_30D_pct": 8.79,
  "median_MAE_30D_pct": -9.89,
  "median_MFE_90D_pct": 8.79,
  "median_MAE_90D_pct": -18.44,
  "median_MFE_180D_pct": 8.79,
  "median_MAE_180D_pct": -40.0,
  "positive_to_counterexample_ratio": "2:4"
}
```

## 15. Profile Comparison

| Profile | Eligibility rule | Selected representative cases | Avg MFE90 | Avg MAE90 | Avg MFE180 | Avg MAE180 | Verdict |
|---|---|---:|---:|---:|---:|---:|---|
| P0 current calibrated proxy | Contract/JV/orderbook headline can support Actionable/Yellow if confidence is high | 6 | 16.66 | -22.58 | 46.51 | -30.85 | Too permissive for parent-proxy and late-cycle entries. |
| P0b current + price-only blowoff guard | Blocks obvious price-only Green but not all contract-size traps | 5 | 18.42 | -24.89 | 54.24 | -31.05 | Better, but still overweights volume orderbook without margin/FCF. |
| P1 L3 sector rule | Requires customer/orderbook and utilization bridge | 3 | 18.86 | -10.52 | 85.65 | -24.72 | Stronger but still lets L&F high-MAE pass unless Green is blocked. |
| P2 C11 canonical bridge rule | Requires orderbook + margin/revision/FCF bridge for Yellow/Green | 2 | 64.07 | -9.08 | 124.67 | -27.26 | Best alignment; keeps POSCO and Stage2-positive L&F while blocking Green. |
| P3 counterexample guard | Routes late-cycle orderbook, parent-proxy capacity, and capex-heavy volume contracts to Watch/4B | 4 blocked | 7.73 | -25.88 | 7.73 | -40.16 | Prevents most MAE-heavy false positives. |


## 16. Current Profile Error Analysis

The current calibrated profile already has useful guardrails: price-only blowoff should not become positive evidence, full 4B needs non-price deterioration, and Stage3-Green should not be loosened. The remaining C11 residual is more specific:

- contract size can be over-counted when margin/FCF visibility is missing;
- JV capacity can be over-counted when the listed parent carries capex or legal drag;
- old orderbook memory can keep a name in Yellow after price has already completed the rerating;
- valid early C11 positives still need a separate local 4B watch once price extension outruns incremental evidence.

## 17. Proposed Scope-Limited Rule Candidate

```json
{
  "rule_candidate_id": "C11_verified_orderbook_margin_fcf_conversion_bridge_required_before_Yellow_or_Green_plus_parent_proxy_and_contract_size_capex_guard",
  "scope": {
    "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY",
    "canonical_archetype_id": "C11_BATTERY_ORDERBOOK_RERATING"
  },
  "positive_stage_bridge": {
    "Stage2_Actionable": "Require verified orderbook/customer/capacity evidence plus at least one economic bridge: ASP/mix, utilization, spread, margin, FCF, or revision.",
    "Stage3_Yellow": "Require two independent non-price confirmations, one of which must connect orderbook to margin/revision/FCF rather than only shipment volume.",
    "Stage3_Green": "Do not loosen globally; C11 Green still requires revision/visibility, valuation pass, and red-team risk pass."
  },
  "negative_stage_guard": {
    "parent_proxy_guard": "JV or subsidiary capacity is not enough unless parent-level margin/FCF bridge is visible.",
    "contract_size_guard": "Large notional contract size is capped if utilization, call-off, or margin durability is unverified.",
    "local_4B_watch": "Trigger when price extension follows a valid early C11 rerating but incremental orderbook/margin evidence stalls.",
    "hard_4C": "Only after non-price thesis break, such as contract reduction, call-off failure, utilization break, margin downgrade, or FCF miss."
  },
  "weight_delta_candidate_shadow_only": {
    "orderbook_quality": "+0.25 within C11 only",
    "margin_fcf_bridge": "+0.35 within C11 only",
    "parent_proxy_penalty": "+0.25 risk penalty within C11 only",
    "price_momentum_without_bridge": "-0.20 within C11 only"
  },
  "production_change_executed": false
}
```

## 18. Residual Contribution Summary

```json
{
  "row_type": "residual_contribution",
  "selected_round": "R3",
  "selected_loop": 101,
  "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY",
  "canonical_archetype_id": "C11_BATTERY_ORDERBOOK_RERATING",
  "new_independent_case_count": 6,
  "reused_case_count": 0,
  "same_archetype_new_symbol_count": 6,
  "calibration_usable_trigger_count": 8,
  "representative_trigger_count": 6,
  "positive_case_count": 2,
  "counterexample_count": 4,
  "stage4b_case_count": 2,
  "stage4c_case_count": 1,
  "current_profile_error_count": 5,
  "source_proxy_only_count": 0,
  "evidence_url_pending_count": 0,
  "new_axis_proposed": "C11_verified_orderbook_margin_fcf_conversion_bridge_required_before_Yellow_or_Green_plus_parent_proxy_and_contract_size_capex_guard",
  "existing_axis_strengthened": [
    "stage2_required_bridge",
    "local_4b_watch_guard",
    "price_only_blowoff_blocks_positive_stage",
    "full_4b_requires_non_price_evidence"
  ],
  "existing_axis_weakened": null,
  "do_not_propose_new_weight_delta": false,
  "loop_contribution_label": "canonical_archetype_rule_candidate"
}
```

## 19. Shadow Weight Delta Candidate — CSV

```csv
canonical_archetype_id,scope,component,delta,reason,production_change_executed
C11_BATTERY_ORDERBOOK_RERATING,C11_only,orderbook_quality,+0.25,valid C11 positives require direct customer/orderbook evidence,false
C11_BATTERY_ORDERBOOK_RERATING,C11_only,margin_fcf_bridge,+0.35,best separation came from margin/FCF/revision bridge,false
C11_BATTERY_ORDERBOOK_RERATING,C11_only,parent_proxy_risk,+0.25,JV/capacity headline punished parent-proxy entries,false
C11_BATTERY_ORDERBOOK_RERATING,C11_only,price_momentum_without_bridge,-0.20,late-cycle price extension produced MAE-heavy traps,false
```

## 20. Promotion Gate Check

```text
sample_size: 6 independent cases / 8 usable trigger rows
coverage_gap_filled: yes, C11 Priority 0 residual coverage
positive_counterexample_balance: 2 positive / 4 counterexamples
rule_candidate_quality: scope-limited, not global
stage3_green_loosened: false
production_profile_changed: false
promotion_recommendation: watchlist_for_future_apply_next_patch_review, not immediate production patch
```

## 21. Rejected / Non-Usable Rows

```jsonl
{"row_type":"rejected_or_narrative_only","symbol":"066970","company_name":"L&F","event_date":"2025-12-29","event_type":"Stage4C-narrative-only","reason":"Reuters/Pulse reported the 2023 Tesla contract scale was later cut. This is useful non-price thesis-break evidence, but the event has no complete 180D forward window inside Stock-Web manifest max_date 2026-02-20, so it is not calibration-usable as a trigger row.","calibration_usable":false,"source_urls":["https://www.reuters.com/world/asia-pacific/south-koreas-lf-says-value-battery-material-supply-deal-tesla-cut-7386-2025-12-29/","https://pulse.mk.co.kr/news/english/11918715"]}
```

## 22. Duplicate-Avoidance Audit

The duplicate key is `canonical_archetype_id + symbol + trigger_type + entry_date`.

```text
C11|003670|Stage2-Actionable|2023-01-31 = new_independent_case
C11|066970|Stage2-Actionable|2023-03-02 = new_independent_case
C11|247540|Stage2-Actionable|2023-12-04 = new_independent_case
C11|006400|Stage2-Actionable|2023-04-27 = new_independent_case
C11|373220|Stage2-Actionable|2023-10-06 = new_independent_case
C11|096770|Stage2-Actionable|2021-05-21 = new_independent_case
C11|003670|Stage4B-Watch|2023-07-26 = same_case_new_trigger_family
C11|066970|Stage4B-Watch|2023-04-03 = same_case_new_trigger_family
```

## 23. Failure Modes / Red Team

1. **Contract notional trap:** a large won amount can be absorbed by price before entry or destroyed by later utilization/call-off risk.
2. **Parent-proxy trap:** JV capacity belongs economically to a project and may not flow cleanly into parent EPS/FCF.
3. **Capex drag trap:** orderbook can be real while free cash flow remains pressured.
4. **Old-orderbook memory:** valid early positives become 4B watch if fresh evidence stops and price keeps extending.
5. **EV demand overlay:** C11 must not ignore C14-style demand slowdown. The two can interact, but C11 should not be replaced by C14 unless demand slowdown is the primary trigger.

## 24. Batch Ingest Self-Audit

```text
required_metadata_present: true
jsonl_trigger_rows_present: true
required_price_fields_present: true
MFE_MAE_30_90_180_present: true
price_data_source_is_stock_web: true
price_basis_tradable_raw: true
price_adjustment_status_raw_unadjusted_marcap: true
forward_180D_complete_for_usable_rows: true
corporate_action_contamination_checked: true
standalone_markdown: true
handoff_prompt_embedded: true
handoff_prompt_executed_now: false
```

## 25. Deferred Coding Agent Handoff Prompt

```text
You are the coding agent for Songdaiki/stock_agent. Do not run live stock screening or trading. Read this Markdown as a V12 historical calibration artifact. Parse the JSONL trigger rows, validate required fields, recalculate MFE/MAE from Songdaiki/stock-web tradable_raw shards, and dedupe by canonical_archetype_id + symbol + trigger_type + entry_date. If accepted, test whether a C11-scoped rule should strengthen stage2_required_bridge, local_4b_watch_guard, price_only_blowoff_blocks_positive_stage, and full_4b_requires_non_price_evidence. Do not loosen Stage3-Green globally. Do not apply production patches without promotion-gate review.
```

## 26. Next Round State

```json
{
  "next_recommended_archetypes": [
    "C01_ORDER_BACKLOG_MARGIN_BRIDGE",
    "C28_SOFTWARE_SECURITY_CONTRACT_RETENTION",
    "C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK",
    "C05_EPC_MEGA_CONTRACT_MARGIN_GAP"
  ],
  "selection_reason": "After C11, remaining strongest gaps are C01 and C28 Priority 0, followed by Priority 1 rows.",
  "round_schedule_status": "coverage_index_selected",
  "sequential_round_cycle_required": false
}
```

## 27. Final State

```json
{
  "generated_file": "e2r_stock_web_v12_residual_round_R3_loop_101_L3_BATTERY_EV_GREEN_MOBILITY_C11_BATTERY_ORDERBOOK_RERATING_research.md",
  "loop_contribution_label": "canonical_archetype_rule_candidate",
  "sector_specific_rule_candidate": true,
  "canonical_archetype_rule_candidate": true,
  "new_axis_proposed": "C11_verified_orderbook_margin_fcf_conversion_bridge_required_before_Yellow_or_Green_plus_parent_proxy_and_contract_size_capex_guard",
  "existing_axis_strengthened": [
    "stage2_required_bridge",
    "local_4b_watch_guard",
    "price_only_blowoff_blocks_positive_stage",
    "full_4b_requires_non_price_evidence"
  ],
  "existing_axis_weakened": null,
  "do_not_propose_new_weight_delta": false,
  "round_schedule_status": "coverage_index_selected",
  "round_sector_consistency": "pass"
}
```

## 28. Chat Response Fields

```text
generated_md_file: e2r_stock_web_v12_residual_round_R3_loop_101_L3_BATTERY_EV_GREEN_MOBILITY_C11_BATTERY_ORDERBOOK_RERATING_research.md
selected_round: R3
selected_loop: 101
selected_priority_bucket: Priority 0
large_sector_id: L3_BATTERY_EV_GREEN_MOBILITY
canonical_archetype_id: C11_BATTERY_ORDERBOOK_RERATING
fine_archetype_id: C11_CATHODE_CELL_ORDERBOOK_MARGIN_FCF_CONVERSION_BRIDGE
new_independent_case_count: 6
reused_case_count: 0
calibration_usable case 수: 6
calibration_usable trigger 수: 8
positive_case_count: 2
counterexample_count: 4
current_profile_error_count: 5
new_axis_proposed: C11_verified_orderbook_margin_fcf_conversion_bridge_required_before_Yellow_or_Green_plus_parent_proxy_and_contract_size_capex_guard
existing_axis_strengthened: stage2_required_bridge, local_4b_watch_guard, price_only_blowoff_blocks_positive_stage, full_4b_requires_non_price_evidence
next_recommended_archetypes: C01_ORDER_BACKLOG_MARGIN_BRIDGE, C28_SOFTWARE_SECURITY_CONTRACT_RETENTION, C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK, C05_EPC_MEGA_CONTRACT_MARGIN_GAP
round_schedule_status: coverage_index_selected
round_sector_consistency: pass
```
