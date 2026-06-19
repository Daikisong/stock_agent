# E2R Stock-Web v12 Residual Research — R1 / C05 Mid-size Builder Working-Capital Cashflow Gate

```text
research_session: post_calibrated_sector_archetype_residual_research
mode: historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12
production_scoring_changed: false
shadow_weight_only: true
handoff_prompt_embedded: true
handoff_prompt_executed_now: false
stock_agent_code_access_allowed: false
stock_agent_code_patch_allowed: false
stock_agent_live_scan_allowed: false
current_stock_discovery_allowed: false
auto_trading_allowed: false
```

## 1. Selection metadata

```text
selected_round: R1
selected_loop: 207
selection_basis: docs/core/V12_Research_No_Repeat_Index.md
selected_priority_bucket: Priority 1 balance reinforcement / URL-proxy quality repair
round_schedule_status: coverage_index_selected
round_sector_consistency: pass

large_sector_id: L1_INDUSTRIALS_INFRA_DEFENSE_GRID
canonical_archetype_id: C05_EPC_MEGA_CONTRACT_MARGIN_GAP
fine_archetype_id: C05_MIDSIZE_BUILDER_WORKING_CAPITAL_CASHFLOW_GATE_V5

loop_objective:
- residual_false_positive_mining
- stage2_actionable_bonus_stress_test
- 4C_thesis_break_timing_test
- sector_specific_rule_discovery
- counterexample_mining
```

### Why this loop

No-Repeat Index는 현재 모든 C01~C32가 80 rows를 넘은 상태라 단순 row 채우기보다 품질 보강을 우선한다. Priority 1에서 C05는 `margin/working-capital 실패 반례와 4C 전환 타이밍 보강`으로 남아 있다. 직전 C05 루프들이 GS E&C, HDC Hyundai Development, Dongbu, Kumho, Kyeryong, SGC 등 대형/중형 대표 건설사를 많이 다뤘으므로 이번 루프는 **Kolon Global / IS Dongseo / HL D&I Halla / KCC E&C / HS Hwasung / Ilsung Construction**으로 확장했다.

Hard duplicate key:

```text
canonical_archetype_id + symbol + trigger_type + entry_date
```

이번 배치의 duplicate key는 기존 top-symbol 과밀군 `028050 / 006360 / 000720 / 047040 / 375500 / 294870`를 피하고, 중형건설사 working-capital / cost-rate / cashflow bridge로 새 표본을 구성했다.

## 2. Stock-Web price atlas validation

```text
price_source: Songdaiki/stock-web
upstream_source: FinanceData/marcap
price_basis: tradable_raw
price_adjustment_status: raw_unadjusted_marcap
manifest_max_date: 2026-02-20
calibration_shard_root: atlas/ohlcv_tradable_by_symbol_year
schema_columns: d,o,h,l,c,v,a,mc,s,m
mfe_formula: (max high from entry_date through N tradable rows / entry_close - 1) * 100
mae_formula: (min low from entry_date through N tradable rows / entry_close - 1) * 100
```

Profile check summary:

```text
003070: active_like; last_date 2026-02-20; recent corporate action candidate 2025-12-11 is outside the 2024-08-28 entry~180D window.
010780: active_like; last_date 2026-02-20; no corporate action candidate inside 2025-02-10~180D window.
014790: active_like; last_date 2026-02-20; no corporate action candidate inside 2025-04-30~180D window.
021320: active_like; last_date 2026-02-20; no corporate action candidate inside 2025-02-28~180D window.
002460: active_like; last_date 2026-02-20; no corporate action candidate inside 2025-03-25~180D window.
013360: active_like; last_date 2026-02-20; no corporate action candidate inside 2025-02-25~180D window.
```

All six usable trigger rows have complete entry OHLCV and 30/90/180D MFE·MAE.

## 3. Trigger-level result table

| symbol | name | trigger_type | entry_date | entry_close | 30D MFE/MAE | 90D MFE/MAE | 180D MFE/MAE | 180D peak | peak-to-trough DD | role |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| 003070 | Kolon Global | Stage4B | 2024-08-28 | 10,430 | 15.53/-13.71 | 15.53/-24.07 | 15.53/-24.07 | 2024-08-28 | -34.27% | counterexample_guardrail |
| 010780 | IS Dongseo | Stage2-Actionable | 2025-02-10 | 19,420 | 5.30/-15.14 | 28.22/-18.95 | 28.22/-18.95 | 2025-06-09 | -29.32% | positive_control |
| 014790 | HL D&I Halla | Stage4B | 2025-04-30 | 2,485 | 13.48/-5.43 | 24.55/-5.43 | 24.55/-9.66 | 2025-08-08 | -27.46% | 4b_offset_quality |
| 021320 | KCC E&C | Stage2-Actionable | 2025-02-28 | 3,955 | 6.32/-3.92 | 49.68/-3.92 | 50.70/-3.92 | 2025-07-14 | -22.73% | positive_control |
| 002460 | HS Hwasung | Stage2 | 2025-03-25 | 9,600 | 5.83/-4.79 | 23.54/-4.79 | 45.21/-4.79 | 2025-12-16 | -3.16% | guarded_positive |
| 013360 | Ilsung Construction | Stage4C | 2025-02-25 | 3,520 | 41.05/-23.01 | 41.05/-52.27 | 41.05/-66.14 | 2025-04-02 | -75.99% | hard_4c_positive_control |

## 4. Actual Stock-Web entry OHLCV rows

| symbol | d | o | h | l | c | v | amount | market_cap | market |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| 003070 | 2024-08-28 | 11,740 | 12,050 | 10,390 | 10,430 | 793,106 | 8,791,318,100 | 197,468,196,590 | KOSPI |
| 010780 | 2025-02-10 | 19,600 | 19,720 | 19,210 | 19,420 | 16,050 | 311,615,110 | 586,231,073,920 | KOSPI |
| 014790 | 2025-04-30 | 2,480 | 2,505 | 2,460 | 2,485 | 37,048 | 92,093,730 | 94,078,623,485 | KOSPI |
| 021320 | 2025-02-28 | 4,065 | 4,075 | 3,955 | 3,955 | 11,757 | 47,226,780 | 84,637,000,000 | KOSDAQ |
| 002460 | 2025-03-25 | 9,560 | 9,770 | 9,520 | 9,600 | 25,058 | 241,206,160 | 97,440,000,000 | KOSPI |
| 013360 | 2025-02-25 | 3,620 | 3,730 | 3,455 | 3,520 | 1,783,917 | 6,407,407,865 | 190,167,577,600 | KOSPI |

## 5. Case notes

### 5.1 003070 Kolon Global — Stage4B, not hard 4C yet

Evidence date: 2024-08-28. Asia Business Daily reported that Kolon Global's long-term borrowings increased sharply, Q2 operating profit fell to only KRW0.3bn, cost of sales rose, operating cash flow was negative, receivables increased, and interest coverage was below 1x. This is a strong **working-capital / interest-coverage warning**. However, the article also describes refinancing/project-acquisition actions, so the correct v12 treatment is local Stage4B/watch rather than immediate hard 4C.

Forward path validates the guardrail: entry-day peak followed by -24.07% 180D MAE and -34.27% peak-to-trough drawdown. The issue was not price-only weakness; the non-price working-capital bridge had already deteriorated.

### 5.2 010780 IS Dongseo — Stage2-Actionable with high-MAE cap

Evidence date: 2025-02-10. The Q4 2024 presentation reported construction-division revenue of KRW119.3bn, OP KRW15.0bn, and 12.5% OPM. That is a real second bridge: margin conversion, not just construction backlog language. But the row still had -18.95% 180D MAE and no repeated cashflow evidence in the source, so Yellow/Green remains blocked.

### 5.3 014790 HL D&I Halla — ugly quarter routes to Stage4B/watch

Evidence date: 2025-04-30. Reuters/TradingView reported Q1 operating profit of KRW14.2bn, down 22.7% YoY. Because the issuer remained profitable and the forward path had +24.55% 180D MFE with only -9.66% MAE, this is a useful counterexample against sticky hard-4C logic. Negative YoY profit language alone should route to Stage4B/watch unless there is cashflow, liquidity, order-collapse, or trust-break confirmation.

### 5.4 021320 KCC E&C — direct operating-result bridge

Evidence date: 2025-02-28. KCC E&C's investor-relations financial table shows FY2024 operating result materially above FY2023, with FY2024 gross profit and operating result improvement. A separate mid-sized builder article also stated KCC E&C's H1 operating profit rose from KRW14.9bn to KRW20.6bn. That gives a margin bridge and a cleaner forward path: +50.70% 180D MFE / -3.92% MAE.

### 5.5 002460 HS Hwasung — Stage2, not Actionable yet

Evidence date: 2025-03-25. The AGM reference material states FY2024 sales fell 32.6% and operating profit fell 6%, though management highlighted peer-relative profitability and liquidity-risk management. This is enough to preserve Stage2 but not enough for Stage2-Actionable/Yellow, because revenue contraction and liquidity focus indicate an incomplete cashflow bridge. The forward path was strong (+45.21% 180D MFE / -4.79% MAE), so this is a current-profile too-late stress row, but still not a Green loosening row.

### 5.6 013360 Ilsung Construction — hard 4C with squeeze risk

Evidence date: 2025-02-25. DART/FSS disclosure showed operating income turned deeply negative in FY2024. The row had a large early squeeze (+41.05% 30D MFE) but then collapsed into -52.27% 90D MAE and -66.14% 180D MAE. This is the cleanest row for C05 hard 4C timing: hard 4C should be based on confirmed non-price earnings break and weak offset quality, not on waiting for the price collapse.

## 6. Residual contribution

```text
new_independent_case_count: 6
new_independent_trigger_count: 6
unique_symbol_count: 6
positive_or_reopen_case_count: 3
counterexample_or_guardrail_case_count: 3
stage2_count: 1
stage2_actionable_count: 2
stage4b_count: 2
stage4c_count: 1

source_proxy_only_count: 0
evidence_url_pending_count: 0
missing_required_mfe_mae_count: 0
missing_entry_price_count: 0
missing_actual_entry_ohlcv_count: 0
corporate_action_contaminated_180D_count: 0
insufficient_forward_window_180D_count: 0

production_scoring_changed: false
shadow_weight_only: true
ready_for_batch_ingest: true
```

### Proposed shadow rule candidate

```text
rule_candidate:
C05_MIDSIZE_BUILDER_WORKING_CAPITAL_CASHFLOW_GATE_V5

sector_rule_candidate:
L1_CONSTRUCTION_MARGIN_CASHFLOW_AND_INTEREST_COVERAGE_GATE
```

Core residual:

```text
- EPC / construction revenue, backlog, or recovery headline alone cannot create Stage2-Actionable, Yellow, or Green.
- Stage2-Actionable requires at least one direct second bridge:
  operating-profit conversion, cost-rate recovery, working-capital release,
  receivable collection improvement, interest-coverage improvement,
  debt/net-cash improvement, high-margin project recognition, or cashflow visibility.
- YoY OP decline, cost-rate pressure, receivable build, interest-coverage weakness,
  or high debt ratio routes first to Stage4B/watch.
- Hard Stage4C requires confirmed non-price thesis break:
  sustained operating loss, liquidity stress, interest-coverage failure,
  order/backlog collapse, accounting/trust break, or weak offset quality.
- Early squeeze / MFE after bad construction evidence should not cancel hard-4C if 90D/180D path later confirms thesis break.
- Strong forward path after weak YoY profit language warns against sticky hard-4C.
- Stage3-Green remains blocked until cashflow/working-capital evidence repeats across more than one evidence family.
```

Shadow weight implication:

```text
current_C05_weight_profile_proxy: EPS/Vis/Bott/Mis/Val/Cap/Info = 18/22/10/12/10/8/20
proposed_shadow_direction:
  earnings_visibility: maintain_or_plus_small
  information_confidence: maintain_high
  capital_allocation: maintain
  bottleneck_pricing: no increase
  valuation_rerating: no increase
production_weight_delta_now: 0
promotion_status: hold_for_batch_aggregation
```

## 7. Machine-readable JSONL trigger rows

```jsonl
{"row_type": "trigger", "research_version": "v12", "selected_round": "R1", "selected_loop": 207, "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "canonical_archetype_id": "C05_EPC_MEGA_CONTRACT_MARGIN_GAP", "fine_archetype_id": "C05_MIDSIZE_BUILDER_WORKING_CAPITAL_CASHFLOW_GATE_V5", "symbol": "003070", "name": "Kolon Global", "trigger_type": "Stage4B", "evidence_date": "2024-08-28", "entry_date": "2024-08-28", "entry_price": 10430.0, "entry_ohlcv": {"d": "2024-08-28", "o": 11740.0, "h": 12050.0, "l": 10390.0, "c": 10430.0, "v": 793106, "a": 8791318100, "mc": 197468196590, "s": 18932713, "m": "KOSPI"}, "price_source_validation": {"price_source": "Songdaiki/stock-web", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "manifest_max_date": "2026-02-20", "tradable_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "forward_180D_available": true, "corporate_action_contaminated_180D": false, "calibration_usable": true}, "forward_return_path": {"mfe_30d_pct": 15.53, "mae_30d_pct": -13.71, "mfe_90d_pct": 15.53, "mae_90d_pct": -24.07, "mfe_180d_pct": 15.53, "mae_180d_pct": -24.07, "peak_180d_date": "2024-08-28", "trough_180d_date": "2024-12-09", "drawdown_from_peak_180d_pct": -34.27}, "evidence_summary": "Q2 2024 liquidity/interest-coverage stress, construction-cost inflation, receivable build and operating cash outflow; not hard 4C because there was still an asset/project acquisition and refinance path.", "evidence_url": "https://www.asiae.co.kr/en/article/2024082713514491469", "source_proxy_only": false, "evidence_url_pending": false, "score_simulation": {"raw_component_breakdown": {"eps_fcf_explosion": 6, "earnings_visibility": 10, "bottleneck_pricing": 4, "market_mispricing": 8, "valuation_rerating": 5, "capital_allocation": 5, "information_confidence": 18}, "total_score_proxy": 56}, "current_profile_alignment": "error_or_stress", "residual_label": "counterexample_guardrail", "representative_for_aggregate": true, "production_scoring_changed": false, "shadow_weight_only": true}
{"row_type": "trigger", "research_version": "v12", "selected_round": "R1", "selected_loop": 207, "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "canonical_archetype_id": "C05_EPC_MEGA_CONTRACT_MARGIN_GAP", "fine_archetype_id": "C05_MIDSIZE_BUILDER_WORKING_CAPITAL_CASHFLOW_GATE_V5", "symbol": "010780", "name": "IS Dongseo", "trigger_type": "Stage2-Actionable", "evidence_date": "2025-02-10", "entry_date": "2025-02-10", "entry_price": 19420.0, "entry_ohlcv": {"d": "2025-02-10", "o": 19600.0, "h": 19720.0, "l": 19210.0, "c": 19420.0, "v": 16050, "a": 311615110, "mc": 586231073920, "s": 30186976, "m": "KOSPI"}, "price_source_validation": {"price_source": "Songdaiki/stock-web", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "manifest_max_date": "2026-02-20", "tradable_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "forward_180D_available": true, "corporate_action_contaminated_180D": false, "calibration_usable": true}, "forward_return_path": {"mfe_30d_pct": 5.3, "mae_30d_pct": -15.14, "mfe_90d_pct": 28.22, "mae_90d_pct": -18.95, "mfe_180d_pct": 28.22, "mae_180d_pct": -18.95, "peak_180d_date": "2025-06-09", "trough_180d_date": "2025-04-03", "drawdown_from_peak_180d_pct": -29.32}, "evidence_summary": "Q4 2024 construction division revenue KRW119.3bn, OP KRW15.0bn, 12.5% OPM; direct margin bridge but still multi-segment and high-MAE cap.", "evidence_url": "https://www.isdongseo.co.kr/util/download?file_orinal=IS_Dongseo_Q4_2024_Earnings_Presentation_Script.pdf&path_to_file=board%2F75%2F03b780b9711d5f2e3b01b202e7c8ffb1.pdf", "source_proxy_only": false, "evidence_url_pending": false, "score_simulation": {"raw_component_breakdown": {"eps_fcf_explosion": 15, "earnings_visibility": 18, "bottleneck_pricing": 8, "market_mispricing": 11, "valuation_rerating": 8, "capital_allocation": 7, "information_confidence": 15}, "total_score_proxy": 82}, "current_profile_alignment": "aligned_positive", "residual_label": "positive_control", "representative_for_aggregate": true, "production_scoring_changed": false, "shadow_weight_only": true}
{"row_type": "trigger", "research_version": "v12", "selected_round": "R1", "selected_loop": 207, "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "canonical_archetype_id": "C05_EPC_MEGA_CONTRACT_MARGIN_GAP", "fine_archetype_id": "C05_MIDSIZE_BUILDER_WORKING_CAPITAL_CASHFLOW_GATE_V5", "symbol": "014790", "name": "HL D&I Halla", "trigger_type": "Stage4B", "evidence_date": "2025-04-30", "entry_date": "2025-04-30", "entry_price": 2485.0, "entry_ohlcv": {"d": "2025-04-30", "o": 2480.0, "h": 2505.0, "l": 2460.0, "c": 2485.0, "v": 37048, "a": 92093730, "mc": 94078623485, "s": 37858601, "m": "KOSPI"}, "price_source_validation": {"price_source": "Songdaiki/stock-web", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "manifest_max_date": "2026-02-20", "tradable_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "forward_180D_available": true, "corporate_action_contaminated_180D": false, "calibration_usable": true}, "forward_return_path": {"mfe_30d_pct": 13.48, "mae_30d_pct": -5.43, "mfe_90d_pct": 24.55, "mae_90d_pct": -5.43, "mfe_180d_pct": 24.55, "mae_180d_pct": -9.66, "peak_180d_date": "2025-08-08", "trough_180d_date": "2025-10-20", "drawdown_from_peak_180d_pct": -27.46}, "evidence_summary": "Q1 2025 OP KRW14.2bn, down 22.7% YoY; ugly but not a thesis-break because earnings remained positive and later forward path was resilient.", "evidence_url": "https://www.tradingview.com/news/reuters.com%2C2025%3Anewsml_L4N3R80QA%3A0-hl-d-i-halla-q1-operating-profit-14-2-billion-won-down-22-7-from-year-earlier/", "source_proxy_only": false, "evidence_url_pending": false, "score_simulation": {"raw_component_breakdown": {"eps_fcf_explosion": 8, "earnings_visibility": 12, "bottleneck_pricing": 5, "market_mispricing": 9, "valuation_rerating": 6, "capital_allocation": 6, "information_confidence": 16}, "total_score_proxy": 62}, "current_profile_alignment": "error_or_stress", "residual_label": "4b_offset_quality", "representative_for_aggregate": true, "production_scoring_changed": false, "shadow_weight_only": true}
{"row_type": "trigger", "research_version": "v12", "selected_round": "R1", "selected_loop": 207, "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "canonical_archetype_id": "C05_EPC_MEGA_CONTRACT_MARGIN_GAP", "fine_archetype_id": "C05_MIDSIZE_BUILDER_WORKING_CAPITAL_CASHFLOW_GATE_V5", "symbol": "021320", "name": "KCC E&C", "trigger_type": "Stage2-Actionable", "evidence_date": "2025-02-28", "entry_date": "2025-02-28", "entry_price": 3955.0, "entry_ohlcv": {"d": "2025-02-28", "o": 4065.0, "h": 4075.0, "l": 3955.0, "c": 3955.0, "v": 11757, "a": 47226780, "mc": 84637000000, "s": 21400000, "m": "KOSDAQ"}, "price_source_validation": {"price_source": "Songdaiki/stock-web", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "manifest_max_date": "2026-02-20", "tradable_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "forward_180D_available": true, "corporate_action_contaminated_180D": false, "calibration_usable": true}, "forward_return_path": {"mfe_30d_pct": 6.32, "mae_30d_pct": -3.92, "mfe_90d_pct": 49.68, "mae_90d_pct": -3.92, "mfe_180d_pct": 50.7, "mae_180d_pct": -3.92, "peak_180d_date": "2025-07-14", "trough_180d_date": "2025-04-07", "drawdown_from_peak_180d_pct": -22.73}, "evidence_summary": "FY2024 financial data showed operating result improving materially vs FY2023, and mid-size-builder coverage cited H1 2024 OP increase; direct margin bridge with low MAE.", "evidence_url": "https://www.kccworld.net/eng/investment/balance.do", "source_proxy_only": false, "evidence_url_pending": false, "score_simulation": {"raw_component_breakdown": {"eps_fcf_explosion": 17, "earnings_visibility": 18, "bottleneck_pricing": 8, "market_mispricing": 12, "valuation_rerating": 9, "capital_allocation": 8, "information_confidence": 16}, "total_score_proxy": 88}, "current_profile_alignment": "aligned_positive", "residual_label": "positive_control", "representative_for_aggregate": true, "production_scoring_changed": false, "shadow_weight_only": true}
{"row_type": "trigger", "research_version": "v12", "selected_round": "R1", "selected_loop": 207, "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "canonical_archetype_id": "C05_EPC_MEGA_CONTRACT_MARGIN_GAP", "fine_archetype_id": "C05_MIDSIZE_BUILDER_WORKING_CAPITAL_CASHFLOW_GATE_V5", "symbol": "002460", "name": "HS Hwasung", "trigger_type": "Stage2", "evidence_date": "2025-03-25", "entry_date": "2025-03-25", "entry_price": 9600.0, "entry_ohlcv": {"d": "2025-03-25", "o": 9560.0, "h": 9770.0, "l": 9520.0, "c": 9600.0, "v": 25058, "a": 241206160, "mc": 97440000000, "s": 10150000, "m": "KOSPI"}, "price_source_validation": {"price_source": "Songdaiki/stock-web", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "manifest_max_date": "2026-02-20", "tradable_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "forward_180D_available": true, "corporate_action_contaminated_180D": false, "calibration_usable": true}, "forward_return_path": {"mfe_30d_pct": 5.83, "mae_30d_pct": -4.79, "mfe_90d_pct": 23.54, "mae_90d_pct": -4.79, "mfe_180d_pct": 45.21, "mae_180d_pct": -4.79, "peak_180d_date": "2025-12-16", "trough_180d_date": "2025-04-07", "drawdown_from_peak_180d_pct": -3.16}, "evidence_summary": "FY2024 sales and OP declined but OP stayed positive and profitability was described as strong versus peers; liquidity-risk management kept it at Stage2 rather than Actionable/Yellow.", "evidence_url": "https://www.hwasung.com/assets_e/images/company/Hwasung_2025_67th_AGM_Reference_material_%28ENG_%29.pdf", "source_proxy_only": false, "evidence_url_pending": false, "score_simulation": {"raw_component_breakdown": {"eps_fcf_explosion": 12, "earnings_visibility": 15, "bottleneck_pricing": 7, "market_mispricing": 11, "valuation_rerating": 7, "capital_allocation": 8, "information_confidence": 14}, "total_score_proxy": 74}, "current_profile_alignment": "error_or_stress", "residual_label": "guarded_positive", "representative_for_aggregate": true, "production_scoring_changed": false, "shadow_weight_only": true}
{"row_type": "trigger", "research_version": "v12", "selected_round": "R1", "selected_loop": 207, "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "canonical_archetype_id": "C05_EPC_MEGA_CONTRACT_MARGIN_GAP", "fine_archetype_id": "C05_MIDSIZE_BUILDER_WORKING_CAPITAL_CASHFLOW_GATE_V5", "symbol": "013360", "name": "Ilsung Construction", "trigger_type": "Stage4C", "evidence_date": "2025-02-25", "entry_date": "2025-02-25", "entry_price": 3520.0, "entry_ohlcv": {"d": "2025-02-25", "o": 3620.0, "h": 3730.0, "l": 3455.0, "c": 3520.0, "v": 1783917, "a": 6407407865, "mc": 190167577600, "s": 54024880, "m": "KOSPI"}, "price_source_validation": {"price_source": "Songdaiki/stock-web", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "manifest_max_date": "2026-02-20", "tradable_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "forward_180D_available": true, "corporate_action_contaminated_180D": false, "calibration_usable": true}, "forward_return_path": {"mfe_30d_pct": 41.05, "mae_30d_pct": -23.01, "mfe_90d_pct": 41.05, "mae_90d_pct": -52.27, "mfe_180d_pct": 41.05, "mae_180d_pct": -66.14, "peak_180d_date": "2025-04-02", "trough_180d_date": "2025-11-19", "drawdown_from_peak_180d_pct": -75.99}, "evidence_summary": "FY2024 operating income turned deeply negative; the early squeeze/MFE was followed by severe 90/180D MAE, supporting hard 4C only when non-price earnings break and weak offset align.", "evidence_url": "https://englishdart.fss.or.kr/dsbh001/main.do?rcpNo=20250225801008", "source_proxy_only": false, "evidence_url_pending": false, "score_simulation": {"raw_component_breakdown": {"eps_fcf_explosion": 2, "earnings_visibility": 5, "bottleneck_pricing": 3, "market_mispricing": 4, "valuation_rerating": 3, "capital_allocation": 4, "information_confidence": 20}, "total_score_proxy": 41}, "current_profile_alignment": "error_or_stress", "residual_label": "hard_4c_positive_control", "representative_for_aggregate": true, "production_scoring_changed": false, "shadow_weight_only": true}
```

## 8. Batch ingest self-audit

```text
filename_matches_required_regex: true
metadata_round_matches_filename: true
metadata_loop_matches_filename: true
selected_round_from_canonical: pass
large_sector_from_canonical: pass
r13_scope_violation: false
stock_agent_code_opened: false
stock_agent_code_patched: false
production_scoring_changed: false
current_live_scan_performed: false
auto_trading_or_brokerage_api: false
actual_stock_web_1D_OHLC_used: true
all_usable_rows_have_entry_price: true
all_usable_rows_have_30_90_180_mfe_mae: true
all_usable_rows_have_evidence_url: true
source_proxy_only_rows: 0
evidence_url_pending_rows: 0
```

## 9. Deferred Coding Agent Handoff Prompt

```text
Do not execute in this research session.

When batch-applying v12 residual research later, parse this MD as a standard v12 result file.
Use only calibration_usable trigger rows. Do not treat any narrative-only row as promotion evidence.
Consider C05_MIDSIZE_BUILDER_WORKING_CAPITAL_CASHFLOW_GATE_V5 as a shadow candidate only.
Do not loosen Stage3-Green. Preserve the existing global requirements and only test whether C05 needs a stronger working-capital / interest-coverage / cashflow second-bridge gate for Stage2-Actionable and a tighter non-price confirmation gate for hard 4C.
```

## 10. Next Research State

```text
completed_round: R1
completed_loop: 207
selection_basis: docs/core/V12_Research_No_Repeat_Index.md
selected_priority_bucket: Priority 1 balance reinforcement / URL-proxy quality repair
round_schedule_status: coverage_index_selected
round_sector_consistency: pass

next_recommended_archetypes:
- C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE_SUPPLIER_ORDER_DIRECT_URL_REPAIR
- C13_BATTERY_JV_UTILIZATION_AMPC_IRA_EX_SUBSIDY_MARGIN_DIRECT_REPAIR
- C16_STRATEGIC_RESOURCE_POLICY_SUPPLY_DIRECT_OFFTAKE_POSITIVE_CONTROL_REPAIR
- C01_ORDER_BACKLOG_MARGIN_BRIDGE_WORKING_CAPITAL_CASHFLOW_ONLY_REPAIR
- R13_CROSS_ARCHETYPE_4B_4C_REDTEAM_OFFSET_QUALITY_REFRESH
```
