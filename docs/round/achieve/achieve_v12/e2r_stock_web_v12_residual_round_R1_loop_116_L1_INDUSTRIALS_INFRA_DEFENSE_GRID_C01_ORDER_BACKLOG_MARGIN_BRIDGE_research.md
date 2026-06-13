# E2R Stock-Web v12 Residual Research — R1 / C01 Order Backlog Margin Bridge second-pass fill

```yaml
research_session: post_calibrated_sector_archetype_residual_research
mode: historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12
selected_round: R1
selected_loop: 116
large_sector_id: L1_INDUSTRIALS_INFRA_DEFENSE_GRID
canonical_archetype_id: C01_ORDER_BACKLOG_MARGIN_BRIDGE
fine_archetype_id: mixed_C01_shipbuilding_supplier_backlog_margin_bridge_second_pass
selection_basis: docs/core/V12_Research_No_Repeat_Index.md
selected_priority_bucket: Priority 0 / under 30 rows
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

The v12 runner requires coverage-index-first selection, not mechanical R1→R13 rotation. The No-Repeat ledger marks `C01_ORDER_BACKLOG_MARGIN_BRIDGE` as Priority 0 with 19 representative rows and need-to-30 of 11 in the static ledger. In this conversation, one prior C01 pass added 6 non-overlapping shipbuilding/engine/offshore symbols; this pass therefore treats C01 as session-adjusted 25 → 32 rows after acceptance.

This pass avoids the prior current-session C01 symbols `329180`, `010620`, `082740`, `075580`, `071970`, and `100090`. The new sample set is `010140`, `009540`, `042660`, `077970`, `033500`, `017960`, and `097230`.

## 2. Stock-Web manifest / schema confirmation

- manifest: https://raw.githubusercontent.com/Songdaiki/stock-web/main/atlas/manifest.json
- schema: https://raw.githubusercontent.com/Songdaiki/stock-web/main/atlas/schema.json
- calibration shard basis: `atlas/ohlcv_tradable_by_symbol_year/{prefix}/{ticker}/{year}.csv`
- price basis: `tradable_raw`, raw/unadjusted marcap OHLC
- MFE/MAE definition: max high / min low from entry row through N tradable rows.
- manifest max date: `2026-02-20`

Corporate-action contamination check in this MD uses the Stock-Web schema logic directionally: 180D windows are blocked if share count changes by >=20% or if close-to-close jumps are roughly split/merge-like. No selected 180D window is flagged.

## 3. Evidence map

| symbol | evidence family | source URLs | interpretation |
|---|---|---|---|
| 010140 삼성중공업 | Q1 2023 operating-profit turn + existing backlog/guidance | https://www.geojeoneul.com/news/articleView.html?idxno=29563, https://www.infostockdaily.co.kr/news/articleView.html?idxno=188494 | Clean backlog → revenue/margin bridge positive. |
| 009540 HD한국조선해양 | Q2 2023 profit turn after earlier stock run | https://www.yna.co.kr/view/AKR20230727109201527 | Profit-turn headline was real, but entry after the move had poor 90/180D path; cap late-chase Stage3. |
| 042660 한화오션 | H1 2024 black-turn, but Q2 still loss-making on operating line | https://www.hanwha.co.kr/newsroom/media_center/news/news_view.do?seq=13621, https://v.daum.net/v/20240726152030093 | Turnaround positive, but needs local 4B watch if early MAE is large. |
| 077970 STX엔진 | Civil-engine recovery and large order/backlog report | https://www.shinyoung.com/files/20250421/d957043e780b5.pdf | Missed structural positive; order recovery converts to large MFE but post-peak drawdown needs local 4B. |
| 033500 동성화인텍 | LNGC insulation backlog and record earnings bridge | https://stock.pstatic.net/stock-research/company/79/20240517_company_303092000.pdf | Supplier backlog positive; 180D reward opens late after modest 30/90D path. |
| 017960 한국카본 | K-LNG order boom / insulation supplier demand | https://www.sentv.co.kr/article/view/sentv202401180087 | Same LNG insulation theme, but immediate return was low; Stage2 yes, Stage3 no without stronger margin timing. |
| 097230 HJ중공업 | H1 2024 shipbuilding+construction backlog growth | https://v.daum.net/v/HmM2ovxppB?f=p, https://infostockdaily.co.kr/news/articleView.html?idxno=204747 | Mixed segment backlog can produce huge later MFE, but 30/90D MAE is severe; stage cap/4B guard needed. |

## 4. Price path table

| symbol | name | trigger_type | entry_date | entry_price | MFE_30D_pct | MAE_30D_pct | MFE_90D_pct | MAE_90D_pct | MFE_180D_pct | MAE_180D_pct | peak_date | peak_price | drawdown_after_peak_pct | case_polarity |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 010140 | 삼성중공업 | Stage3-Yellow | 2023-05-09 | 5610 | 24.60 | -3.57 | 68.81 | -3.57 | 68.81 | -3.57 | 2023-08-02 | 9470 | -28.09 | positive_with_4B_watch |
| 009540 | HD한국조선해양 | Stage2-Actionable | 2023-07-28 | 123700 | 1.46 | -10.91 | 1.46 | -28.05 | 4.28 | -28.05 | 2024-03-21 | 129000 | -14.11 | counterexample |
| 042660 | 한화오션 | Stage3-Yellow | 2024-07-29 | 30100 | 17.28 | -15.61 | 36.38 | -15.61 | 199.00 | -15.61 | 2025-04-25 | 90000 | -9.00 | positive_with_4B_watch |
| 077970 | STX엔진 | Stage3-Yellow | 2025-04-22 | 22050 | 22.45 | -3.40 | 119.50 | -9.71 | 125.85 | -9.71 | 2025-09-05 | 49800 | -42.37 | positive_with_4B_watch |
| 033500 | 동성화인텍 | Stage3-Yellow | 2024-05-17 | 12890 | 2.79 | -9.08 | 11.56 | -16.21 | 74.17 | -17.30 | 2025-01-22 | 22450 | -12.87 | positive_with_4B_watch |
| 017960 | 한국카본 | Stage2-Actionable | 2024-01-19 | 10840 | 2.21 | -4.89 | 10.15 | -8.95 | 23.15 | -8.95 | 2024-08-20 | 13350 | -21.65 | counterexample |
| 097230 | HJ중공업 | Stage2-Actionable | 2024-06-27 | 3510 | 7.55 | -23.08 | 7.55 | -37.89 | 182.05 | -37.89 | 2025-03-06 | 9900 | -34.34 | counterexample |

## 5. Case notes

### 010140 삼성중공업 — positive backlog-to-margin bridge
The trigger is not the backlog headline alone. The usable C01 signal appears when the 2021~2022 LNG/backlog base begins to show up in actual quarterly profit. Entry on 2023-05-09 delivered 90D/180D MFE of 68.81% with only -3.57% MAE. This is the cleanest `Stage3-Yellow` row in the set, but the -28.09% post-peak drawdown still supports local 4B watch after fast rerating.

### 009540 HD한국조선해양 — late-chase counterexample
The Q2 2023 profit turn was fundamentally valid, yet the market had already priced a large part of the shipbuilding turnaround. Entry on 2023-07-28 had only 4.28% 180D MFE and -28.05% 90/180D MAE. This should not be promoted as C01 Stage3 merely because the profit-turn headline exists; it needs a late-chase valuation/price-path cap.

### 042660 한화오션 — turnaround positive with 4B watch
H1 2024 turned profitable at the aggregate level, but Q2 still carried an operating loss. The path from 2024-07-29 had strong 90D/180D MFE, but also -15.61% MAE. C01 can allow Stage3-Yellow only when the margin bridge is visible and should add a local 4B watch when the initial retracement exceeds normal execution noise.

### 077970 STX엔진 — missed structural positive / post-peak 4B
The April 2025 evidence shows civil-engine recovery and long-backlog recovery after a long slump. Entry on 2025-04-22 produced 119.50% 90D MFE and 125.85% 180D MFE with modest MAE. However, drawdown after peak was -42.37%, so the rule should distinguish early recognition from post-peak 4B risk.

### 033500 동성화인텍 — supplier backlog positive, slower conversion
The LNG insulation backlog is not just a theme; it is tied to named Korean yard customers and high backlog visibility. Still, the stock only opened its return window slowly: 30D MFE 2.79%, 90D MFE 11.56%, 180D MFE 74.17%. C01 should avoid requiring immediate 30D confirmation when the delivery/revenue-recognition bridge is credible.

### 017960 한국카본 — low-alpha supplier counterexample
Korea Carbon shares the LNG insulation demand chain, but from the January 2024 trigger the path was weaker: 180D MFE 23.15% with 90D MFE only 10.15%. This is Stage2-Actionable rather than Stage3; backlog visibility alone is insufficient unless margin/recognition timing is stronger.

### 097230 HJ중공업 — mixed-segment backlog high-MAE counterexample
The H1 2024 backlog story combined construction and shipbuilding. That made the headline large, but the path was hazardous: 30D MAE -23.08%, 90D MAE -37.89%, then later 180D MFE 182.05%. This is exactly why C01 needs a mixed-segment backlog cap: not every large order backlog belongs in the same clean shipbuilding margin-bridge bucket.

## 6. Current calibrated profile stress test

Current calibrated axes such as `stage2_required_bridge`, `local_4b_watch_guard`, and `price_only_blowoff_blocks_positive_stage` are directionally correct, but C01 still needs a more exact rule. The case set shows three distinct sub-mechanisms:

1. **Clean backlog-to-margin conversion:** Samsung Heavy, STX Engine, and Dongsung FineTec show that order backlog is useful when it converts into revenue recognition, earnings visibility, and customer/order quality.
2. **Late-chase false promotion:** HD Korea Shipbuilding shows that a real profit turn can still be a bad C01 entry if the stock has already rerated and fresh margin bridge is not incremental.
3. **Mixed-segment/high-MAE backlog:** HJ Heavy and Hanwha Ocean show that backlog and turnaround can be true while the entry path still demands local 4B or Stage2 cap.

### Proposed shadow rule candidate

```text
C01_BACKLOG_TO_MARGIN_FCF_RECOGNITION_GATE_WITH_LATE_CHASE_AND_MIXED_SEGMENT_CAP
```

Rule shape:

```text
if canonical_archetype_id == C01_ORDER_BACKLOG_MARGIN_BRIDGE:
    require at least two of:
        - named/order backlog or durable customer backlog
        - delivery/revenue-recognition schedule visibility
        - actual margin bridge or earnings turn confirmation
        - FCF / working-capital non-deterioration signal
    cap at Stage2-Actionable if:
        - trigger is only backlog/headline and margin bridge is absent
        - 90D MAE <= -20% before fresh recognition evidence
        - evidence follows a prior price run and incremental revision is weak
        - backlog is mixed segment construction+shipbuilding without segment margin clarity
    allow Stage3-Yellow if:
        - margin bridge is confirmed and 90D MAE does not exceed sector execution noise
    add local_4B_watch if:
        - post-peak drawdown <= -25%, even if the 180D MFE is strong
```

## 7. Raw component score simulation

Weights used for this shadow simulation are C01-like: EPS/FCF 20%, visibility 25%, bottleneck/order quality 18%, mispricing 12%, valuation 12%, capital allocation 8%, information confidence 5%.

```jsonl
{"row_type": "score_simulation", "symbol": "010140", "name": "삼성중공업", "canonical_archetype_id": "C01_ORDER_BACKLOG_MARGIN_BRIDGE", "component_scores": {"eps_fcf_explosion": 72, "earnings_visibility": 82, "bottleneck_pricing": 73, "market_mispricing": 63, "valuation_rerating": 58, "capital_allocation": 50, "information_confidence": 74}, "weights": {"eps_fcf_explosion": 0.2, "earnings_visibility": 0.25, "bottleneck_pricing": 0.18, "market_mispricing": 0.12, "valuation_rerating": 0.12, "capital_allocation": 0.08, "information_confidence": 0.05}, "shadow_weighted_total_score": 70.26, "simulated_stage": "Stage3-Yellow", "score_return_alignment": "pass"}
{"row_type": "score_simulation", "symbol": "009540", "name": "HD한국조선해양", "canonical_archetype_id": "C01_ORDER_BACKLOG_MARGIN_BRIDGE", "component_scores": {"eps_fcf_explosion": 61, "earnings_visibility": 72, "bottleneck_pricing": 68, "market_mispricing": 48, "valuation_rerating": 39, "capital_allocation": 45, "information_confidence": 70}, "weights": {"eps_fcf_explosion": 0.2, "earnings_visibility": 0.25, "bottleneck_pricing": 0.18, "market_mispricing": 0.12, "valuation_rerating": 0.12, "capital_allocation": 0.08, "information_confidence": 0.05}, "shadow_weighted_total_score": 59.98, "simulated_stage": "Stage2-Actionable", "score_return_alignment": "stage_cap_required"}
{"row_type": "score_simulation", "symbol": "042660", "name": "한화오션", "canonical_archetype_id": "C01_ORDER_BACKLOG_MARGIN_BRIDGE", "component_scores": {"eps_fcf_explosion": 67, "earnings_visibility": 76, "bottleneck_pricing": 70, "market_mispricing": 55, "valuation_rerating": 50, "capital_allocation": 47, "information_confidence": 69}, "weights": {"eps_fcf_explosion": 0.2, "earnings_visibility": 0.25, "bottleneck_pricing": 0.18, "market_mispricing": 0.12, "valuation_rerating": 0.12, "capital_allocation": 0.08, "information_confidence": 0.05}, "shadow_weighted_total_score": 64.81, "simulated_stage": "Stage3-Yellow", "score_return_alignment": "pass"}
{"row_type": "score_simulation", "symbol": "077970", "name": "STX엔진", "canonical_archetype_id": "C01_ORDER_BACKLOG_MARGIN_BRIDGE", "component_scores": {"eps_fcf_explosion": 69, "earnings_visibility": 78, "bottleneck_pricing": 74, "market_mispricing": 57, "valuation_rerating": 48, "capital_allocation": 42, "information_confidence": 67}, "weights": {"eps_fcf_explosion": 0.2, "earnings_visibility": 0.25, "bottleneck_pricing": 0.18, "market_mispricing": 0.12, "valuation_rerating": 0.12, "capital_allocation": 0.08, "information_confidence": 0.05}, "shadow_weighted_total_score": 65.93, "simulated_stage": "Stage3-Yellow", "score_return_alignment": "pass"}
{"row_type": "score_simulation", "symbol": "033500", "name": "동성화인텍", "canonical_archetype_id": "C01_ORDER_BACKLOG_MARGIN_BRIDGE", "component_scores": {"eps_fcf_explosion": 66, "earnings_visibility": 76, "bottleneck_pricing": 72, "market_mispricing": 58, "valuation_rerating": 50, "capital_allocation": 43, "information_confidence": 68}, "weights": {"eps_fcf_explosion": 0.2, "earnings_visibility": 0.25, "bottleneck_pricing": 0.18, "market_mispricing": 0.12, "valuation_rerating": 0.12, "capital_allocation": 0.08, "information_confidence": 0.05}, "shadow_weighted_total_score": 64.96, "simulated_stage": "Stage3-Yellow", "score_return_alignment": "pass"}
{"row_type": "score_simulation", "symbol": "017960", "name": "한국카본", "canonical_archetype_id": "C01_ORDER_BACKLOG_MARGIN_BRIDGE", "component_scores": {"eps_fcf_explosion": 58, "earnings_visibility": 66, "bottleneck_pricing": 70, "market_mispricing": 49, "valuation_rerating": 45, "capital_allocation": 41, "information_confidence": 64}, "weights": {"eps_fcf_explosion": 0.2, "earnings_visibility": 0.25, "bottleneck_pricing": 0.18, "market_mispricing": 0.12, "valuation_rerating": 0.12, "capital_allocation": 0.08, "information_confidence": 0.05}, "shadow_weighted_total_score": 58.46, "simulated_stage": "Stage2-Actionable", "score_return_alignment": "stage_cap_required"}
{"row_type": "score_simulation", "symbol": "097230", "name": "HJ중공업", "canonical_archetype_id": "C01_ORDER_BACKLOG_MARGIN_BRIDGE", "component_scores": {"eps_fcf_explosion": 55, "earnings_visibility": 62, "bottleneck_pricing": 60, "market_mispricing": 45, "valuation_rerating": 40, "capital_allocation": 38, "information_confidence": 58}, "weights": {"eps_fcf_explosion": 0.2, "earnings_visibility": 0.25, "bottleneck_pricing": 0.18, "market_mispricing": 0.12, "valuation_rerating": 0.12, "capital_allocation": 0.08, "information_confidence": 0.05}, "shadow_weighted_total_score": 53.44, "simulated_stage": "Stage2-Actionable", "score_return_alignment": "stage_cap_required"}
```

## 8. Machine-readable trigger rows

```jsonl
{"row_type": "trigger", "research_file": "e2r_stock_web_v12_residual_round_R1_loop_116_L1_INDUSTRIALS_INFRA_DEFENSE_GRID_C01_ORDER_BACKLOG_MARGIN_BRIDGE_research.md", "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "canonical_archetype_id": "C01_ORDER_BACKLOG_MARGIN_BRIDGE", "source_repo": "Songdaiki/stock-web", "symbol": "010140", "name": "삼성중공업", "evidence_date": "2023-05-08", "trigger_date": "2023-05-08", "entry_date": "2023-05-09", "entry_price": 5610.0, "trigger_type": "Stage3-Yellow", "fine_archetype_id": "positive_margin_bridge", "MFE_30D_pct": 24.6, "MAE_30D_pct": -3.57, "MFE_90D_pct": 68.81, "MAE_90D_pct": -3.57, "MFE_180D_pct": 68.81, "MAE_180D_pct": -3.57, "peak_date": "2023-08-02", "peak_price": 9470.0, "drawdown_after_peak_pct": -28.09, "window_180D_corporate_action_contaminated": false, "calibration_usable": true, "forward_rows_180D": 180, "component_scores": {"eps_fcf_explosion": 72, "earnings_visibility": 82, "bottleneck_pricing": 73, "market_mispricing": 63, "valuation_rerating": 58, "capital_allocation": 50, "information_confidence": 74}, "shadow_weighted_total_score": 70.26, "case_polarity": "positive_with_4B_watch", "evidence_urls": ["https://www.geojeoneul.com/news/articleView.html?idxno=29563", "https://www.infostockdaily.co.kr/news/articleView.html?idxno=188494"]}
{"row_type": "trigger", "research_file": "e2r_stock_web_v12_residual_round_R1_loop_116_L1_INDUSTRIALS_INFRA_DEFENSE_GRID_C01_ORDER_BACKLOG_MARGIN_BRIDGE_research.md", "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "canonical_archetype_id": "C01_ORDER_BACKLOG_MARGIN_BRIDGE", "source_repo": "Songdaiki/stock-web", "symbol": "009540", "name": "HD한국조선해양", "evidence_date": "2023-07-27", "trigger_date": "2023-07-27", "entry_date": "2023-07-28", "entry_price": 123700.0, "trigger_type": "Stage2-Actionable", "fine_archetype_id": "late_chase_counterexample", "MFE_30D_pct": 1.46, "MAE_30D_pct": -10.91, "MFE_90D_pct": 1.46, "MAE_90D_pct": -28.05, "MFE_180D_pct": 4.28, "MAE_180D_pct": -28.05, "peak_date": "2024-03-21", "peak_price": 129000.0, "drawdown_after_peak_pct": -14.11, "window_180D_corporate_action_contaminated": false, "calibration_usable": true, "forward_rows_180D": 180, "component_scores": {"eps_fcf_explosion": 61, "earnings_visibility": 72, "bottleneck_pricing": 68, "market_mispricing": 48, "valuation_rerating": 39, "capital_allocation": 45, "information_confidence": 70}, "shadow_weighted_total_score": 59.98, "case_polarity": "counterexample", "evidence_urls": ["https://www.yna.co.kr/view/AKR20230727109201527"]}
{"row_type": "trigger", "research_file": "e2r_stock_web_v12_residual_round_R1_loop_116_L1_INDUSTRIALS_INFRA_DEFENSE_GRID_C01_ORDER_BACKLOG_MARGIN_BRIDGE_research.md", "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "canonical_archetype_id": "C01_ORDER_BACKLOG_MARGIN_BRIDGE", "source_repo": "Songdaiki/stock-web", "symbol": "042660", "name": "한화오션", "evidence_date": "2024-07-26", "trigger_date": "2024-07-26", "entry_date": "2024-07-29", "entry_price": 30100.0, "trigger_type": "Stage3-Yellow", "fine_archetype_id": "turnaround_positive_with_4b_watch", "MFE_30D_pct": 17.28, "MAE_30D_pct": -15.61, "MFE_90D_pct": 36.38, "MAE_90D_pct": -15.61, "MFE_180D_pct": 199.0, "MAE_180D_pct": -15.61, "peak_date": "2025-04-25", "peak_price": 90000.0, "drawdown_after_peak_pct": -9.0, "window_180D_corporate_action_contaminated": false, "calibration_usable": true, "forward_rows_180D": 180, "component_scores": {"eps_fcf_explosion": 67, "earnings_visibility": 76, "bottleneck_pricing": 70, "market_mispricing": 55, "valuation_rerating": 50, "capital_allocation": 47, "information_confidence": 69}, "shadow_weighted_total_score": 64.81, "case_polarity": "positive_with_4B_watch", "evidence_urls": ["https://www.hanwha.co.kr/newsroom/media_center/news/news_view.do?seq=13621", "https://v.daum.net/v/20240726152030093"]}
{"row_type": "trigger", "research_file": "e2r_stock_web_v12_residual_round_R1_loop_116_L1_INDUSTRIALS_INFRA_DEFENSE_GRID_C01_ORDER_BACKLOG_MARGIN_BRIDGE_research.md", "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "canonical_archetype_id": "C01_ORDER_BACKLOG_MARGIN_BRIDGE", "source_repo": "Songdaiki/stock-web", "symbol": "077970", "name": "STX엔진", "evidence_date": "2025-04-21", "trigger_date": "2025-04-21", "entry_date": "2025-04-22", "entry_price": 22050.0, "trigger_type": "Stage3-Yellow", "fine_archetype_id": "civil_engine_order_recovery_positive_4b_watch", "MFE_30D_pct": 22.45, "MAE_30D_pct": -3.4, "MFE_90D_pct": 119.5, "MAE_90D_pct": -9.71, "MFE_180D_pct": 125.85, "MAE_180D_pct": -9.71, "peak_date": "2025-09-05", "peak_price": 49800.0, "drawdown_after_peak_pct": -42.37, "window_180D_corporate_action_contaminated": false, "calibration_usable": true, "forward_rows_180D": 180, "component_scores": {"eps_fcf_explosion": 69, "earnings_visibility": 78, "bottleneck_pricing": 74, "market_mispricing": 57, "valuation_rerating": 48, "capital_allocation": 42, "information_confidence": 67}, "shadow_weighted_total_score": 65.93, "case_polarity": "positive_with_4B_watch", "evidence_urls": ["https://www.shinyoung.com/files/20250421/d957043e780b5.pdf"]}
{"row_type": "trigger", "research_file": "e2r_stock_web_v12_residual_round_R1_loop_116_L1_INDUSTRIALS_INFRA_DEFENSE_GRID_C01_ORDER_BACKLOG_MARGIN_BRIDGE_research.md", "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "canonical_archetype_id": "C01_ORDER_BACKLOG_MARGIN_BRIDGE", "source_repo": "Songdaiki/stock-web", "symbol": "033500", "name": "동성화인텍", "evidence_date": "2024-05-16", "trigger_date": "2024-05-16", "entry_date": "2024-05-17", "entry_price": 12890.0, "trigger_type": "Stage3-Yellow", "fine_archetype_id": "lng_insulation_backlog_positive", "MFE_30D_pct": 2.79, "MAE_30D_pct": -9.08, "MFE_90D_pct": 11.56, "MAE_90D_pct": -16.21, "MFE_180D_pct": 74.17, "MAE_180D_pct": -17.3, "peak_date": "2025-01-22", "peak_price": 22450.0, "drawdown_after_peak_pct": -12.87, "window_180D_corporate_action_contaminated": false, "calibration_usable": true, "forward_rows_180D": 180, "component_scores": {"eps_fcf_explosion": 66, "earnings_visibility": 76, "bottleneck_pricing": 72, "market_mispricing": 58, "valuation_rerating": 50, "capital_allocation": 43, "information_confidence": 68}, "shadow_weighted_total_score": 64.96, "case_polarity": "positive_with_4B_watch", "evidence_urls": ["https://stock.pstatic.net/stock-research/company/79/20240517_company_303092000.pdf"]}
{"row_type": "trigger", "research_file": "e2r_stock_web_v12_residual_round_R1_loop_116_L1_INDUSTRIALS_INFRA_DEFENSE_GRID_C01_ORDER_BACKLOG_MARGIN_BRIDGE_research.md", "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "canonical_archetype_id": "C01_ORDER_BACKLOG_MARGIN_BRIDGE", "source_repo": "Songdaiki/stock-web", "symbol": "017960", "name": "한국카본", "evidence_date": "2024-01-18", "trigger_date": "2024-01-18", "entry_date": "2024-01-19", "entry_price": 10840.0, "trigger_type": "Stage2-Actionable", "fine_archetype_id": "lng_insulation_backlog_low_alpha_counterexample", "MFE_30D_pct": 2.21, "MAE_30D_pct": -4.89, "MFE_90D_pct": 10.15, "MAE_90D_pct": -8.95, "MFE_180D_pct": 23.15, "MAE_180D_pct": -8.95, "peak_date": "2024-08-20", "peak_price": 13350.0, "drawdown_after_peak_pct": -21.65, "window_180D_corporate_action_contaminated": false, "calibration_usable": true, "forward_rows_180D": 180, "component_scores": {"eps_fcf_explosion": 58, "earnings_visibility": 66, "bottleneck_pricing": 70, "market_mispricing": 49, "valuation_rerating": 45, "capital_allocation": 41, "information_confidence": 64}, "shadow_weighted_total_score": 58.46, "case_polarity": "counterexample", "evidence_urls": ["https://www.sentv.co.kr/article/view/sentv202401180087"]}
{"row_type": "trigger", "research_file": "e2r_stock_web_v12_residual_round_R1_loop_116_L1_INDUSTRIALS_INFRA_DEFENSE_GRID_C01_ORDER_BACKLOG_MARGIN_BRIDGE_research.md", "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "canonical_archetype_id": "C01_ORDER_BACKLOG_MARGIN_BRIDGE", "source_repo": "Songdaiki/stock-web", "symbol": "097230", "name": "HJ중공업", "evidence_date": "2024-06-26", "trigger_date": "2024-06-26", "entry_date": "2024-06-27", "entry_price": 3510.0, "trigger_type": "Stage2-Actionable", "fine_archetype_id": "mixed_segment_backlog_high_mae_counterexample", "MFE_30D_pct": 7.55, "MAE_30D_pct": -23.08, "MFE_90D_pct": 7.55, "MAE_90D_pct": -37.89, "MFE_180D_pct": 182.05, "MAE_180D_pct": -37.89, "peak_date": "2025-03-06", "peak_price": 9900.0, "drawdown_after_peak_pct": -34.34, "window_180D_corporate_action_contaminated": false, "calibration_usable": true, "forward_rows_180D": 180, "component_scores": {"eps_fcf_explosion": 55, "earnings_visibility": 62, "bottleneck_pricing": 60, "market_mispricing": 45, "valuation_rerating": 40, "capital_allocation": 38, "information_confidence": 58}, "shadow_weighted_total_score": 53.44, "case_polarity": "counterexample", "evidence_urls": ["https://v.daum.net/v/HmM2ovxppB?f=p", "https://infostockdaily.co.kr/news/articleView.html?idxno=204747"]}
```

## 9. Aggregate / shadow-weight / residual contribution rows

```jsonl
{"row_type": "aggregate", "research_file": "e2r_stock_web_v12_residual_round_R1_loop_116_L1_INDUSTRIALS_INFRA_DEFENSE_GRID_C01_ORDER_BACKLOG_MARGIN_BRIDGE_research.md", "selected_round": "R1", "selected_loop": 116, "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "canonical_archetype_id": "C01_ORDER_BACKLOG_MARGIN_BRIDGE", "calibration_usable_rows": 7, "representative_rows": 7, "positive_case_count": 2, "counterexample_count": 3, "positive_with_4B_watch_count": 2, "4C_case_count": 0, "current_profile_error_count": 5, "avg_MFE_90D_pct": 36.49, "avg_MAE_90D_pct": -17.14, "session_adjusted_C01_rows_before": 25, "session_adjusted_C01_rows_after": 32}
{"row_type": "shadow_weight", "canonical_archetype_id": "C01_ORDER_BACKLOG_MARGIN_BRIDGE", "candidate_axis": "C01_BACKLOG_TO_MARGIN_FCF_RECOGNITION_GATE_WITH_LATE_CHASE_AND_MIXED_SEGMENT_CAP", "proposal_type": "sector_specific_shadow_rule_candidate", "do_not_apply_now": true, "suggested_delta": "increase earnings_visibility and bottleneck_pricing gate strictness; cap valuation_rerating if backlog headline follows a prior price run without fresh margin bridge; add local_4B watch for post-peak drawdown >25% or MAE90<-20%", "support_rows": ["010140", "009540", "042660", "077970", "033500", "017960", "097230"]}
{"row_type": "residual_contribution", "canonical_archetype_id": "C01_ORDER_BACKLOG_MARGIN_BRIDGE", "residual_error": "current profile can still over-promote backlog headlines after the price path has already discounted the margin bridge, and can under-separate clean shipbuilding margin conversion from mixed-segment backlog stories", "new_axis_proposed": "C01_BACKLOG_TO_MARGIN_FCF_RECOGNITION_GATE_WITH_LATE_CHASE_AND_MIXED_SEGMENT_CAP", "existing_axis_strengthened": ["stage2_required_bridge", "local_4b_watch_guard", "price_only_blowoff_blocks_positive_stage"], "existing_axis_weakened": null}
```

## 10. Novelty / duplicate audit

```yaml
same_canonical_archetype_research_allowed: true
same_symbol_same_trigger_date_research: false
previous_current_session_C01_symbols_avoided:
  - '329180'
  - '010620'
  - '082740'
  - '075580'
  - '071970'
  - '100090'
new_symbols_this_file:
  - '010140'
  - '009540'
  - '042660'
  - '077970'
  - '033500'
  - '017960'
  - '097230'
static_no_repeat_C01_rows: 19
session_adjusted_C01_rows_before_this_file: 25
session_adjusted_C01_rows_after_this_file: 32
hard_duplicate_key_basis: canonical_archetype_id + symbol + trigger_type + entry_date
hard_duplicate_detected: false
```

## 11. Deferred Coding Agent Handoff Prompt

```text
You are the implementation/coding agent for stock_agent. Do not execute this handoff inside the research session. Later, when multiple v12 research MDs have been collected, ingest this MD as a standalone V12 result file.

Target file:
e2r_stock_web_v12_residual_round_R1_loop_116_L1_INDUSTRIALS_INFRA_DEFENSE_GRID_C01_ORDER_BACKLOG_MARGIN_BRIDGE_research.md

Task:
1. Parse all row_type=trigger JSONL rows.
2. Verify each row has entry_date, entry_price, trigger_type, large_sector_id, canonical_archetype_id, MFE_30D_pct, MAE_30D_pct, MFE_90D_pct, MAE_90D_pct, MFE_180D_pct, MAE_180D_pct.
3. Deduplicate by canonical_archetype_id + symbol + trigger_type + entry_date.
4. Aggregate this file into C01_ORDER_BACKLOG_MARGIN_BRIDGE.
5. Treat the proposed rule as shadow_weight_only until enough independent C01 rows confirm the late-chase and mixed-segment caps.
6. Do not apply production scoring changes without batch-level validation.
```

## 12. Batch Ingest Self-Audit

```yaml
standard_filename_ok: true
filename_matches_metadata: true
uses_no_repeat_index_as_ledger_only: true
uses_stock_web_actual_ohlcv: true
all_rows_have_entry_date: true
all_rows_have_entry_price: true
all_rows_have_MFE_30D_pct: true
all_rows_have_MAE_30D_pct: true
all_rows_have_MFE_90D_pct: true
all_rows_have_MAE_90D_pct: true
all_rows_have_MFE_180D_pct: true
all_rows_have_MAE_180D_pct: true
calibration_usable_rows: 7
representative_rows: 7
source_proxy_only_rows: 0
evidence_url_pending_rows: 0
future_data_leakage_detected: false
corporate_action_contaminated_rows: 0
insufficient_forward_window_rows: 0
production_code_patch_included: false
production_scoring_patch_applied: false
handoff_prompt_executed_now: false
```

## 13. Next research state

```text
completed_round = R1
completed_loop = 116
selection_basis = docs/core/V12_Research_No_Repeat_Index.md
selected_priority_bucket = Priority 0 / under 30 rows
next_recommended_archetypes = C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF | C14_EV_DEMAND_SLOWDOWN_4B_4C | C06_HBM_MEMORY_CUSTOMER_CAPACITY | C11_BATTERY_ORDERBOOK_RERATING
round_schedule_status = coverage_index_selected
round_sector_consistency = pass
```
