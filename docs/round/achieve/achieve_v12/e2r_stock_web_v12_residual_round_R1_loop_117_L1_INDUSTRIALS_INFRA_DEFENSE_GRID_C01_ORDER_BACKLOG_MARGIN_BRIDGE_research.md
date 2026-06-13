# E2R Stock-Web v12 Residual Research — R1 / C01 fitting·valve·engine-parts backlog margin bridge third pass

```yaml
research_session: post_calibrated_sector_archetype_residual_research
mode: historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12
selected_round: R1
selected_loop: 117
large_sector_id: L1_INDUSTRIALS_INFRA_DEFENSE_GRID
canonical_archetype_id: C01_ORDER_BACKLOG_MARGIN_BRIDGE
fine_archetype_id: mixed_C01_fitting_valve_engine_parts_backlog_margin_bridge_third_pass
selection_basis: docs/core/V12_Research_No_Repeat_Index.md
selected_priority_bucket: Priority 0 / static C01 rows=19 / need-to-30=11 / need-to-50=31
round_schedule_status: coverage_index_selected
round_sector_consistency: pass
price_source: Songdaiki/stock-web
price_basis: tradable_raw
price_adjustment_status: raw_unadjusted_marcap
stock_web_manifest_max_date: 2026-02-20
production_scoring_changed: false
shadow_weight_only: true
handoff_prompt_embedded: true
handoff_prompt_executed_now: false
```

## 1. Selection rationale

The v12 runner requires coverage-index-first selection rather than mechanical R1→R13 rotation. The static No-Repeat ledger still marks `C01_ORDER_BACKLOG_MARGIN_BRIDGE` as Priority 0 with 19 representative rows, 11 rows short of the 30-row minimum stability threshold. This pass therefore continues C01, but avoids the current-session C01 shipbuilder / LNG-insulation / engine rows already used in earlier loops.

Prior current-session C01 symbols explicitly avoided: `329180`, `010620`, `082740`, `075580`, `071970`, `100090`, `010140`, `009540`, `042660`, `077970`, `033500`, `017960`, `097230`.

New sample set: `023160`, `014620`, `013030`, `086670`, `073010`, `103230`.

## 2. Stock-Web manifest / schema confirmation

- manifest: https://raw.githubusercontent.com/Songdaiki/stock-web/main/atlas/manifest.json
- schema: https://raw.githubusercontent.com/Songdaiki/stock-web/main/atlas/schema.json
- calibration shard basis: `atlas/ohlcv_tradable_by_symbol_year/{prefix}/{ticker}/{year}.csv`
- price basis: `tradable_raw`, raw/unadjusted marcap OHLC
- MFE/MAE definition: max high / min low from entry row through N tradable rows.
- manifest max date: `2026-02-20`

Corporate-action contamination check: no selected 180D window overlaps known profile-level corporate-action candidates found in the candidate profiles available through Stock-Web. 30/90/180D forward windows are present for all selected rows.

## 3. Evidence map

| symbol | evidence family | evidence summary | source URLs |
|---|---|---|---|
| 023160 태광 | welded_fitting_h2_order_recovery_lng_offshore_mix | 2024-09-20 Eugene fitting report: 1Q/2Q orders recovering from 4Q23 trough, H2 quarterly orders expected above 70bn KRW, LNG carrier/offshore stainless mix has higher ASP/margin leverage. | https://www.eugenefn.com/common/files/amail//20240920_B20_Js_heo_9.pdf |
| 014620 성광벤드 | new_orders_shipbuilding_lng_mix_margin_reacceleration | 2024-08-13 article/research framing: shipbuilding cycle recovery and new orders reaching prior-cycle levels; 2024 mix expected to recover after delayed projects. | https://www.dailyinvest.kr/news/articleView.html?idxno=60218<br>https://ssl.pstatic.net/imgstock/upload/research/company/1710458815306.pdf |
| 013030 하이록코리아 | instrumentation_fitting_valve_quality_but_low_alpha_path | 2024-05-23 company report maintained Buy target; 2024E revenue/OP growth but price path did not open strong C01 rerating window. Good balance sheet/margin quality, weak incremental rerating trigger. | https://stock.pstatic.net/stock-research/company/2/20240523_company_79405000.pdf<br>https://www.hy-lok.com/about/FinanceInfo.hylok |
| 086670 비엠티 | industrial_fitting_valve_multicycle_exposure_high_mae_false_stage2 | 2024-05-28/29 KIRS and follow-up article: precision fitting/valve exposure to semiconductor, alternative fuel, shipbuilding/offshore; evidence was real but not enough to protect 90/180D MAE without order/revenue bridge. | https://w4.kirs.or.kr/download/research/240528_%EB%B9%84%EC%97%A0%ED%8B%B0.pdf<br>https://www.dailyinvest.kr/news/articleView.html?idxno=58928 |
| 073010 케이에스피 | marine_engine_parts_backlog_capacity_expansion | 2024-04-25 report/article: engine-parts backlog rose from roughly 10bn KRW in 2020 to 59.1bn KRW in 2023 and capacity expansion was expected to unlock additional ship-engine orders. | https://www.asiae.co.kr/article/2024042507303347966<br>https://www.hanaw.com/download/research/FileServer/WEB/info/small_cap/2024/04/24/240425_KSP_F.pdf |
| 103230 에스앤더블유 | ship_engine_parts_delivery_from_accumulated_backlog | 2024-12-19 NICE/KIRS report: 2024 ship-engine parts sales expected to rise as deliveries from accumulated post-2020 backlog proceed. | https://w4.kirs.or.kr/download/research/241219_%EA%B8%B0%EA%B3%84_%EC%97%90%EC%8A%A4%EC%95%A4%EB%8D%94%EB%B8%94%EB%A5%98%28103230%29_%ED%95%B4%EC%96%91%EC%97%90%EC%84%9C%20%EC%9A%B0%EC%A3%BC%EB%A1%9C%2C%2060%EB%85%84%20%EA%B8%B0%EC%88%A0%EC%9D%98%20%EC%A7%84%ED%99%94_NICE%EB%94%94%EC%95%A4%EB%B9%84.pdf |

## 4. Price path table

| symbol | name | trigger_type | entry_date | entry_price | MFE_30D_pct | MAE_30D_pct | MFE_90D_pct | MAE_90D_pct | MFE_180D_pct | MAE_180D_pct | peak_date | peak_price | drawdown_after_peak_pct | case_polarity |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---|---:|---:|---|
| 023160 | 태광 | Stage3-Yellow | 2024-09-23 | 14610 | 2.6694 | -18.6858 | 65.9822 | -18.6858 | 84.8049 | -18.6858 | 2025-03-04 | 27000 | -34.4444 | positive_with_4B_watch |
| 014620 | 성광벤드 | Stage3-Yellow | 2024-08-14 | 15050 | 12.2924 | -10.2990 | 65.7807 | -17.8073 | 115.9468 | -17.8073 | 2025-01-17 | 32500 | -30.6154 | positive_with_4B_watch |
| 013030 | 하이록코리아 | Stage2-Actionable | 2024-05-24 | 28500 | 6.1404 | -8.5965 | 6.1404 | -17.8947 | 13.8596 | -21.4035 | 2025-01-22 | 32450 | -16.1787 | counterexample |
| 086670 | 비엠티 | Stage2-Actionable | 2024-05-30 | 12700 | 11.2598 | -5.9055 | 11.2598 | -29.3701 | 11.2598 | -45.6693 | 2024-06-05 | 14130 | -51.1677 | counterexample |
| 073010 | 케이에스피 | Stage3-Yellow | 2024-04-25 | 3920 | 44.1327 | -5.1020 | 44.1327 | -5.1020 | 44.1327 | -14.7959 | 2024-05-13 | 5650 | -40.8850 | positive_with_4B_watch |
| 103230 | 에스앤더블유 | Stage3-Yellow | 2024-12-20 | 3135 | 16.1085 | -12.5997 | 25.6778 | -13.0781 | 94.5774 | -13.0781 | 2025-09-11 | 6100 | -25.9836 | positive_with_4B_watch |

## 5. Case notes

### 023160 태광 — positive, but not without early-MAE and post-peak 4B guard
The evidence is not just “fitting theme”. The useful C01 signal is the recovery in quarterly order flow plus the mix argument: LNG carrier / offshore stainless fitting has higher ASP and margin leverage than plain carbon fitting. Entry at 2024-09-23 produced 90D MFE of `65.9822%` and 180D MFE of `84.8049%`, but the 30D MAE was already `-18.6858%` and the post-peak drawdown reached `-34.4444%`. C01 should allow Stage3-Yellow only after the order-to-margin bridge is visible and should add local 4B after fast rerating.

### 014620 성광벤드 — clean positive with local 4B after vertical rerating
The order recovery thesis did work: entry on 2024-08-14 opened `115.9468%` 180D MFE. However, this is not a price-only Green row. The non-price bridge is order recovery + high-value LNG/offshore mix + expected margin improvement. The post-peak drawdown of `-30.6154%` means the rule should not let C01 remain Stage3 without a local 4B exit/watch rule once the rerating compresses future return.

### 013030 하이록코리아 — quality company, weak incremental C01 rerating
The business quality and balance sheet are strong, but the specific 2024-05-23/24 trigger did not produce a clean C01 rerating. 90D MFE was only `6.1404%` and 180D MAE reached `-21.4035%`. This is a Stage2-Actionable quality watch row, not Stage3-Green. The rule should separate durable quality from fresh backlog-to-margin conversion.

### 086670 비엠티 — multi-cycle exposure false positive
BMT has legitimate fitting/valve exposure to semiconductor, alternative fuel, shipbuilding and offshore. The problem is attribution. Without named order, delivery timing, and margin bridge, a broad industrial exposure row can become a high-MAE false Stage2/Stage3. From entry, 180D MFE stayed at `11.2598%` while 180D MAE reached `-45.6693%`.

### 073010 케이에스피 — engine-parts backlog positive with post-peak 4B
This is the best engine-parts C01 row in the set. The report explicitly ties ship-engine customer backlog expansion, parts backlog growth, and capacity expansion to top-line growth. Entry produced `44.1327%` MFE within 30D and retained the same peak through 180D. But because the peak came quickly and post-peak drawdown was `-40.8850%`, C01 needs a fast-rerating local 4B overlay.

### 103230 에스앤더블유 — delayed engine-parts delivery positive
The trigger was a delivery-from-accumulated-backlog story, not just shipbuilding beta. From 2024-12-20 entry, 180D MFE reached `94.5774%` with 180D MAE of only `-13.0781%`. This supports allowing Stage3-Yellow when backlog is tied to actual delivery and revenue recognition, even if 30D confirmation is initially modest.

## 6. Current calibrated profile stress test

Current global axes remain directionally correct:

```text
stage2_required_bridge = strengthened
local_4b_watch_guard = strengthened
price_only_blowoff_blocks_positive_stage = strengthened
full_4b_requires_non_price_evidence = preserved
```

The residual C01 error is more specific. Fitting, valve and ship-engine component names can look like clean shipbuilding backlog rerating, but they are one layer removed from the yard orderbook. The rule should therefore require a second bridge:

```text
customer / order backlog
  -> delivery or revenue-recognition visibility
  -> ASP / product-mix / margin bridge
  -> FCF or working-capital non-deterioration
```

If this bridge is missing, C01 should stay at Stage2-Watch even when the sector theme is correct. If the bridge is present but the price path has already gone vertical, local 4B should be attached after post-peak drawdown or high MAE.

## 7. Proposed shadow rule candidate

```text
C01_FITTING_VALVE_ENGINE_PARTS_BACKLOG_REQUIRES_REVENUE_MARGIN_FCF_BRIDGE_WITH_LATE_CHASE_AND_4B_CAP_V117
```

Rule shape:

```text
if canonical_archetype_id == C01_ORDER_BACKLOG_MARGIN_BRIDGE
and fine_archetype in [fitting, valve, ship_engine_parts, shipbuilding_supplier_backlog]:
    require at least two of:
        - named or quantified order/backlog recovery
        - delivery/revenue-recognition timing
        - ASP/product-mix/margin bridge
        - FCF or working-capital non-deterioration
    cap at Stage2-Watch if:
        - evidence is only sector theme or multi-cycle exposure
        - 90D MAE <= -20% before fresh bridge evidence
        - 180D MFE is weak and margin bridge is absent
    add local Stage4B if:
        - post-peak drawdown <= -25%
        - fast MFE occurs without fresh delivery/margin confirmation
```

## 8. Machine-readable rows

```jsonl
{"row_type": "trigger", "research_version": "v12", "case_id": "C01_023160_2024-09-23_welded_fitting_h2_order_recovery_lng_offshore_mix", "selected_round": "R1", "selected_loop": 117, "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "canonical_archetype_id": "C01_ORDER_BACKLOG_MARGIN_BRIDGE", "fine_archetype_id": "mixed_C01_fitting_valve_engine_parts_backlog_margin_bridge_third_pass", "symbol": "023160", "name": "태광", "trigger_date": "2024-09-20", "trigger_type": "Stage3-Yellow", "trigger_family": "welded_fitting_h2_order_recovery_lng_offshore_mix", "entry_date": "2024-09-23", "entry_price": 14610, "MFE_30D_pct": 2.6694, "MAE_30D_pct": -18.6858, "MFE_90D_pct": 65.9822, "MAE_90D_pct": -18.6858, "MFE_180D_pct": 84.8049, "MAE_180D_pct": -18.6858, "peak_date": "2025-03-04", "peak_price": 27000, "drawdown_after_peak_pct": -34.4444, "case_polarity": "positive_with_4B_watch", "calibration_usable": true, "representative": true, "source_proxy_only": false, "evidence_url_pending": false, "window_180D_corporate_action_contaminated": false, "production_scoring_changed": false, "evidence_urls": ["https://www.eugenefn.com/common/files/amail//20240920_B20_Js_heo_9.pdf"]}
{"row_type": "trigger", "research_version": "v12", "case_id": "C01_014620_2024-08-14_new_orders_shipbuilding_lng_mix_margin_reacceleration", "selected_round": "R1", "selected_loop": 117, "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "canonical_archetype_id": "C01_ORDER_BACKLOG_MARGIN_BRIDGE", "fine_archetype_id": "mixed_C01_fitting_valve_engine_parts_backlog_margin_bridge_third_pass", "symbol": "014620", "name": "성광벤드", "trigger_date": "2024-08-13", "trigger_type": "Stage3-Yellow", "trigger_family": "new_orders_shipbuilding_lng_mix_margin_reacceleration", "entry_date": "2024-08-14", "entry_price": 15050, "MFE_30D_pct": 12.2924, "MAE_30D_pct": -10.299, "MFE_90D_pct": 65.7807, "MAE_90D_pct": -17.8073, "MFE_180D_pct": 115.9468, "MAE_180D_pct": -17.8073, "peak_date": "2025-01-17", "peak_price": 32500, "drawdown_after_peak_pct": -30.6154, "case_polarity": "positive_with_4B_watch", "calibration_usable": true, "representative": true, "source_proxy_only": false, "evidence_url_pending": false, "window_180D_corporate_action_contaminated": false, "production_scoring_changed": false, "evidence_urls": ["https://www.dailyinvest.kr/news/articleView.html?idxno=60218", "https://ssl.pstatic.net/imgstock/upload/research/company/1710458815306.pdf"]}
{"row_type": "trigger", "research_version": "v12", "case_id": "C01_013030_2024-05-24_instrumentation_fitting_valve_quality_but_low_alpha_path", "selected_round": "R1", "selected_loop": 117, "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "canonical_archetype_id": "C01_ORDER_BACKLOG_MARGIN_BRIDGE", "fine_archetype_id": "mixed_C01_fitting_valve_engine_parts_backlog_margin_bridge_third_pass", "symbol": "013030", "name": "하이록코리아", "trigger_date": "2024-05-23", "trigger_type": "Stage2-Actionable", "trigger_family": "instrumentation_fitting_valve_quality_but_low_alpha_path", "entry_date": "2024-05-24", "entry_price": 28500, "MFE_30D_pct": 6.1404, "MAE_30D_pct": -8.5965, "MFE_90D_pct": 6.1404, "MAE_90D_pct": -17.8947, "MFE_180D_pct": 13.8596, "MAE_180D_pct": -21.4035, "peak_date": "2025-01-22", "peak_price": 32450, "drawdown_after_peak_pct": -16.1787, "case_polarity": "counterexample", "calibration_usable": true, "representative": true, "source_proxy_only": false, "evidence_url_pending": false, "window_180D_corporate_action_contaminated": false, "production_scoring_changed": false, "evidence_urls": ["https://stock.pstatic.net/stock-research/company/2/20240523_company_79405000.pdf", "https://www.hy-lok.com/about/FinanceInfo.hylok"]}
{"row_type": "trigger", "research_version": "v12", "case_id": "C01_086670_2024-05-30_industrial_fitting_valve_multicycle_exposure_high_mae_false_stage2", "selected_round": "R1", "selected_loop": 117, "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "canonical_archetype_id": "C01_ORDER_BACKLOG_MARGIN_BRIDGE", "fine_archetype_id": "mixed_C01_fitting_valve_engine_parts_backlog_margin_bridge_third_pass", "symbol": "086670", "name": "비엠티", "trigger_date": "2024-05-29", "trigger_type": "Stage2-Actionable", "trigger_family": "industrial_fitting_valve_multicycle_exposure_high_mae_false_stage2", "entry_date": "2024-05-30", "entry_price": 12700, "MFE_30D_pct": 11.2598, "MAE_30D_pct": -5.9055, "MFE_90D_pct": 11.2598, "MAE_90D_pct": -29.3701, "MFE_180D_pct": 11.2598, "MAE_180D_pct": -45.6693, "peak_date": "2024-06-05", "peak_price": 14130, "drawdown_after_peak_pct": -51.1677, "case_polarity": "counterexample", "calibration_usable": true, "representative": true, "source_proxy_only": false, "evidence_url_pending": false, "window_180D_corporate_action_contaminated": false, "production_scoring_changed": false, "evidence_urls": ["https://w4.kirs.or.kr/download/research/240528_%EB%B9%84%EC%97%A0%ED%8B%B0.pdf", "https://www.dailyinvest.kr/news/articleView.html?idxno=58928"]}
{"row_type": "trigger", "research_version": "v12", "case_id": "C01_073010_2024-04-25_marine_engine_parts_backlog_capacity_expansion", "selected_round": "R1", "selected_loop": 117, "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "canonical_archetype_id": "C01_ORDER_BACKLOG_MARGIN_BRIDGE", "fine_archetype_id": "mixed_C01_fitting_valve_engine_parts_backlog_margin_bridge_third_pass", "symbol": "073010", "name": "케이에스피", "trigger_date": "2024-04-25", "trigger_type": "Stage3-Yellow", "trigger_family": "marine_engine_parts_backlog_capacity_expansion", "entry_date": "2024-04-25", "entry_price": 3920, "MFE_30D_pct": 44.1327, "MAE_30D_pct": -5.102, "MFE_90D_pct": 44.1327, "MAE_90D_pct": -5.102, "MFE_180D_pct": 44.1327, "MAE_180D_pct": -14.7959, "peak_date": "2024-05-13", "peak_price": 5650, "drawdown_after_peak_pct": -40.885, "case_polarity": "positive_with_4B_watch", "calibration_usable": true, "representative": true, "source_proxy_only": false, "evidence_url_pending": false, "window_180D_corporate_action_contaminated": false, "production_scoring_changed": false, "evidence_urls": ["https://www.asiae.co.kr/article/2024042507303347966", "https://www.hanaw.com/download/research/FileServer/WEB/info/small_cap/2024/04/24/240425_KSP_F.pdf"]}
{"row_type": "trigger", "research_version": "v12", "case_id": "C01_103230_2024-12-20_ship_engine_parts_delivery_from_accumulated_backlog", "selected_round": "R1", "selected_loop": 117, "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "canonical_archetype_id": "C01_ORDER_BACKLOG_MARGIN_BRIDGE", "fine_archetype_id": "mixed_C01_fitting_valve_engine_parts_backlog_margin_bridge_third_pass", "symbol": "103230", "name": "에스앤더블유", "trigger_date": "2024-12-19", "trigger_type": "Stage3-Yellow", "trigger_family": "ship_engine_parts_delivery_from_accumulated_backlog", "entry_date": "2024-12-20", "entry_price": 3135, "MFE_30D_pct": 16.1085, "MAE_30D_pct": -12.5997, "MFE_90D_pct": 25.6778, "MAE_90D_pct": -13.0781, "MFE_180D_pct": 94.5774, "MAE_180D_pct": -13.0781, "peak_date": "2025-09-11", "peak_price": 6100, "drawdown_after_peak_pct": -25.9836, "case_polarity": "positive_with_4B_watch", "calibration_usable": true, "representative": true, "source_proxy_only": false, "evidence_url_pending": false, "window_180D_corporate_action_contaminated": false, "production_scoring_changed": false, "evidence_urls": ["https://w4.kirs.or.kr/download/research/241219_%EA%B8%B0%EA%B3%84_%EC%97%90%EC%8A%A4%EC%95%A4%EB%8D%94%EB%B8%94%EB%A5%98%28103230%29_%ED%95%B4%EC%96%91%EC%97%90%EC%84%9C%20%EC%9A%B0%EC%A3%BC%EB%A1%9C%2C%2060%EB%85%84%20%EA%B8%B0%EC%88%A0%EC%9D%98%20%EC%A7%84%ED%99%94_NICE%EB%94%94%EC%95%A4%EB%B9%84.pdf"]}
{"row_type": "score_simulation", "symbol": "023160", "entry_date": "2024-09-23", "current_profile_proxy": "e2r_2_2_rolling_calibrated", "raw_component_score_breakdown": {"eps_fcf_explosion": 66, "earnings_visibility": 71, "bottleneck_pricing": 73, "market_mispricing": 58, "valuation_rerating": 60, "capital_allocation": 52, "information_confidence": 68}, "simulated_total_score": 64.0, "simulated_stage_without_shadow_gate": "Stage3-Yellow", "shadow_rule_effect": "cap_to_Stage2_or_add_local_4B_if_margin/FCF bridge or high-MAE guard fails"}
{"row_type": "score_simulation", "symbol": "014620", "entry_date": "2024-08-14", "current_profile_proxy": "e2r_2_2_rolling_calibrated", "raw_component_score_breakdown": {"eps_fcf_explosion": 68, "earnings_visibility": 73, "bottleneck_pricing": 74, "market_mispricing": 60, "valuation_rerating": 62, "capital_allocation": 55, "information_confidence": 68}, "simulated_total_score": 65.71, "simulated_stage_without_shadow_gate": "Stage3-Yellow", "shadow_rule_effect": "cap_to_Stage2_or_add_local_4B_if_margin/FCF bridge or high-MAE guard fails"}
{"row_type": "score_simulation", "symbol": "013030", "entry_date": "2024-05-24", "current_profile_proxy": "e2r_2_2_rolling_calibrated", "raw_component_score_breakdown": {"eps_fcf_explosion": 53, "earnings_visibility": 65, "bottleneck_pricing": 62, "market_mispricing": 48, "valuation_rerating": 45, "capital_allocation": 60, "information_confidence": 64}, "simulated_total_score": 56.71, "simulated_stage_without_shadow_gate": "Stage2-Actionable", "shadow_rule_effect": "cap_to_Stage2_or_add_local_4B_if_margin/FCF bridge or high-MAE guard fails"}
{"row_type": "score_simulation", "symbol": "086670", "entry_date": "2024-05-30", "current_profile_proxy": "e2r_2_2_rolling_calibrated", "raw_component_score_breakdown": {"eps_fcf_explosion": 45, "earnings_visibility": 48, "bottleneck_pricing": 57, "market_mispricing": 44, "valuation_rerating": 42, "capital_allocation": 45, "information_confidence": 61}, "simulated_total_score": 48.86, "simulated_stage_without_shadow_gate": "Stage2-Actionable", "shadow_rule_effect": "cap_to_Stage2_or_add_local_4B_if_margin/FCF bridge or high-MAE guard fails"}
{"row_type": "score_simulation", "symbol": "073010", "entry_date": "2024-04-25", "current_profile_proxy": "e2r_2_2_rolling_calibrated", "raw_component_score_breakdown": {"eps_fcf_explosion": 72, "earnings_visibility": 70, "bottleneck_pricing": 69, "market_mispricing": 61, "valuation_rerating": 60, "capital_allocation": 48, "information_confidence": 69}, "simulated_total_score": 64.14, "simulated_stage_without_shadow_gate": "Stage3-Yellow", "shadow_rule_effect": "cap_to_Stage2_or_add_local_4B_if_margin/FCF bridge or high-MAE guard fails"}
{"row_type": "score_simulation", "symbol": "103230", "entry_date": "2024-12-20", "current_profile_proxy": "e2r_2_2_rolling_calibrated", "raw_component_score_breakdown": {"eps_fcf_explosion": 64, "earnings_visibility": 66, "bottleneck_pricing": 60, "market_mispricing": 57, "valuation_rerating": 56, "capital_allocation": 44, "information_confidence": 62}, "simulated_total_score": 58.43, "simulated_stage_without_shadow_gate": "Stage3-Yellow", "shadow_rule_effect": "cap_to_Stage2_or_add_local_4B_if_margin/FCF bridge or high-MAE guard fails"}
{"row_type": "aggregate", "selected_round": "R1", "selected_loop": 117, "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "canonical_archetype_id": "C01_ORDER_BACKLOG_MARGIN_BRIDGE", "trigger_row_count": 6, "calibration_usable_rows": 6, "positive_case_count": 4, "counterexample_count": 2, "stage4b_local_watch_count": 6, "stage4c_count": 0, "avg_MFE_90D_pct": 36.4956, "avg_MAE_90D_pct": -16.9897, "avg_MFE_180D_pct": 60.7635, "avg_MAE_180D_pct": -21.9066, "current_profile_error_count": 4, "source_proxy_only_rows": 0, "evidence_url_pending_rows": 0}
{"row_type": "shadow_weight", "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "canonical_archetype_id": "C01_ORDER_BACKLOG_MARGIN_BRIDGE", "shadow_rule_candidate": "C01_FITTING_VALVE_ENGINE_PARTS_BACKLOG_REQUIRES_REVENUE_MARGIN_FCF_BRIDGE_WITH_LATE_CHASE_AND_4B_CAP_V117", "expected_effect": "strengthen stage2_required_bridge for fitting/valve/engine-parts backlog proxies; keep positive cases that show order→delivery→margin conversion; cap late-chase or low-alpha supplier rows at Stage2-Watch/local4B"}
{"row_type": "residual_contribution", "residual_error_found": true, "new_axis_proposed": "fitting_valve_engine_parts_backlog_proxy_decontamination", "existing_axis_strengthened": ["stage2_required_bridge", "local_4b_watch_guard", "price_only_blowoff_blocks_positive_stage"], "existing_axis_weakened": [], "do_not_propose_new_weight_delta": false}
```

## 9. Residual contribution summary

```yaml
new_independent_case_count: 6
reused_case_count: 0
same_archetype_new_symbol_count: 6
same_archetype_new_trigger_family_count: 6
calibration_usable_rows: 6
representative_rows: 6
positive_case_count: 4
counterexample_count: 2
stage4b_local_watch_count: 6
stage4c_count: 0
avg_MFE_90D_pct: 36.4956
avg_MAE_90D_pct: -16.9897
avg_MFE_180D_pct: 60.7635
avg_MAE_180D_pct: -21.9066
source_proxy_only_rows: 0
evidence_url_pending_rows: 0
rows_missing_required_mfe_mae: 0
production_code_patch_included: false
production_scoring_patch_applied: false
ready_for_batch_ingest: true
```

## 10. Deferred Coding Agent Handoff Prompt

```text
You are the coding agent for Songdaiki/stock_agent. Do not treat this MD as an instruction to patch production scoring immediately.

Task:
1. Ingest this V12 result MD together with other docs/round files.
2. Validate all trigger rows against required v12 fields.
3. Deduplicate by canonical_archetype_id + symbol + trigger_type + entry_date.
4. If accepted, evaluate the shadow rule candidate:
   C01_FITTING_VALVE_ENGINE_PARTS_BACKLOG_REQUIRES_REVENUE_MARGIN_FCF_BRIDGE_WITH_LATE_CHASE_AND_4B_CAP_V117
5. Test whether C01 fitting/valve/ship-engine-parts rows should require order/backlog + delivery/revenue + margin/FCF bridge before Stage3-Yellow.
6. Keep production scoring unchanged unless the batch calibration engine promotes this candidate after aggregate validation.
```

## 11. Next research state

```text
completed_round = R1
completed_loop = 117
selection_basis = docs/core/V12_Research_No_Repeat_Index.md
selected_priority_bucket = Priority 0 / C01 static rows 19 / need-to-30 11
next_recommended_archetypes = C01_ORDER_BACKLOG_MARGIN_BRIDGE_followup_if_still_below_30 | R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL_holdout_quality_only | C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK_holdout_only_if_new_delivery_or_calloff_path
round_schedule_status = coverage_index_selected
round_sector_consistency = pass
```

## 12. Batch Ingest Self-Audit

```yaml
standard_filename_ok: true
filename_matches_metadata: true
uses_no_repeat_index_as_ledger_only: true
uses_stock_web_actual_ohlcv: true
jsonl_trigger_row_count: 6
calibration_usable_rows: 6
representative_rows: 6
source_proxy_only_rows: 0
evidence_url_pending_rows: 0
rows_missing_required_mfe_mae: 0
rows_missing_entry_price_or_date: 0
rows_with_noncanonical_trigger_type: 0
future_data_leakage_detected: false
corporate_action_contaminated_rows: 0
insufficient_forward_window_rows: 0
production_code_patch_included: false
production_scoring_patch_applied: false
handoff_prompt_executed_now: false
ready_for_batch_ingest: true
```
