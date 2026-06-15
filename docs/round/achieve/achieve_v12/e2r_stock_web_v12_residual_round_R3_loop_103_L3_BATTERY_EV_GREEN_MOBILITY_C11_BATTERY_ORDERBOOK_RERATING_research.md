---
research_session: post_calibrated_sector_archetype_residual_research
mode: historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12
output_file: e2r_stock_web_v12_residual_round_R3_loop_103_L3_BATTERY_EV_GREEN_MOBILITY_C11_BATTERY_ORDERBOOK_RERATING_research.md
selected_round: R3
selected_loop: 103
large_sector_id: L3_BATTERY_EV_GREEN_MOBILITY
canonical_archetype_id: C11_BATTERY_ORDERBOOK_RERATING
fine_archetype_id: mixed_C11_battery_foil_can_material_orderbook_third_pass
selection_basis: docs/core/V12_Research_No_Repeat_Index.md
selected_priority_bucket: Priority 0 / under 30 rows
round_schedule_status: coverage_index_selected
round_sector_consistency: pass
price_source: Songdaiki/stock-web
price_basis: tradable_raw
price_adjustment_status: raw_unadjusted_marcap
stock_web_manifest_max_date: '2026-02-20'
production_scoring_changed: false
shadow_weight_only: true
handoff_prompt_embedded: true
handoff_prompt_executed_now: false
---

# E2R Stock-Web V12 Residual Research — R3 / C11 Battery Orderbook Rerating / Loop 103

## 1. Selection and novelty check

이번 실행은 **C11_BATTERY_ORDERBOOK_RERATING 3차 패스**다. No-Repeat Index의 static ledger 기준 C11은 `18 rows / need-to-30 12`로 남아 있고, 이 대화에서 직전 C11 loop_101 및 loop_102가 총 11개 row를 추가했기 때문에 session-adjusted로는 `18 -> 29` 근처까지 올라온 상태다. 이번 파일은 새 symbol 5개를 추가해 C11을 30-row 실전 보정권 위로 넘기는 목적이다.

Hard duplicate key는 `canonical_archetype_id + symbol + trigger_type + entry_date`로 보며, 직전 C11에서 사용한 `003670`, `348370`, `066970`, `393890`, `011790`, `373220`, `006400`, `247540`, `020150`, `005070`, `078600`은 모두 피했다.

```text
selected_round = R3
selected_loop = 103
large_sector_id = L3_BATTERY_EV_GREEN_MOBILITY
canonical_archetype_id = C11_BATTERY_ORDERBOOK_RERATING
standard_filename_ok = true
new_symbol_count = 5
new_trigger_family_count = 5
hard_duplicate_count = 0
```

## 2. Price-source validation

Stock-Web manifest assumption:

```text
source_name = FinanceData/marcap
price_basis = tradable_raw
price_adjustment_status = raw_unadjusted_marcap
calibration_shard_root = atlas/ohlcv_tradable_by_symbol_year
manifest_max_date = 2026-02-20
```

Schema rule applied:

```text
MFE_N_pct = (max high from entry_date through N tradable rows / entry_price - 1) * 100
MAE_N_pct = (min low from entry_date through N tradable rows / entry_price - 1) * 100
required_windows = 30D, 90D, 180D
```

Rejected-candidate note: `006110 삼아알미늄` was considered, but its symbol profile includes a `2023-02-09` corporate-action candidate inside the proposed 180D window. Under the V12 rule, that row should not be used as calibration-usable. It is therefore excluded from the trigger set rather than silently forced into the dataset.

## 3. Case set and price-path result

|symbol|name|trigger_type|entry_date|entry_price|MFE_30D_pct|MAE_30D_pct|MFE_90D_pct|MAE_90D_pct|MFE_180D_pct|MAE_180D_pct|drawdown_after_peak_pct|case_role|
|---|---|---|---|---|---|---|---|---|---|---|---|---|
|096770|SK이노베이션|Stage2-Actionable|2023-04-26|177500|16.9|-3.21|29.3|-11.1|29.3|-36.51|-50.89|counterexample|
|002710|TCC스틸|Stage3-Yellow|2023-03-10|17100|186.55|-8.77|236.26|-8.77|340.35|-8.77|-38.51|positive|
|014820|동원시스템즈|Stage2-Actionable|2023-05-02|43400|3.34|-8.64|3.34|-22.81|3.34|-36.41|-38.46|counterexample|
|001530|DI동일|Stage3-Yellow|2023-05-18|20200|17.57|-3.37|52.48|-4.7|64.11|-4.7|-27.45|positive|
|091580|상신이디피|Stage3-Yellow|2024-12-06|7140|17.23|-8.82|38.66|-8.82|58.26|-8.82|-16.11|positive|

## 4. Case-level residual notes

### 4.1 096770 SK이노베이션 — parent/JV capacity headline is not enough

Hyundai Motor Group and SK On approved a US battery-cell JV with 35GWh annual capacity and enough planned supply for about 300,000 EVs. That is legitimate C11 Stage2-Actionable evidence, but the listed parent stock path shows why **battery subsidiary JV capacity does not automatically equal C11 Stage3 orderbook rerating**. The 180D MFE was only `+29.30%`, while 180D MAE reached `-36.51%` and post-peak drawdown reached `-50.89%`. This should be compressed into Stage2 cap / Stage4B watch unless SK On segment margin, shipment, and financing bridge are also confirmed.

### 4.2 002710 TCC스틸 — true upside, but vertical MFE needs local 4B exit

TCC Steel is a strong positive holdout. Nickel-plated steel sheets for cylindrical battery cases created a clean C11 battery-can material rerating route. The price path confirms it: 30D MFE `+186.55%`, 90D MFE `+236.26%`, 180D MFE `+340.35%`, with only `-8.77%` MAE. However, after the July peak the post-peak drawdown was `-38.51%`. The lesson is not to block the positive row; it is to keep **local 4B watch** once vertical MFE detaches from shipment/margin confirmation.

### 4.3 014820 동원시스템즈 — capacity financing without named shipment is a false Stage2/3 path

Dongwon Systems had a credible secondary-battery-materials narrative: green bond financing, Asan cylindrical battery-can facilities, aluminum foil, and cell pouch expansion. But the price path rejects a Stage3 unlock. 180D MFE was only `+3.34%`, while 90D MAE was `-22.81%` and 180D MAE was `-36.41%`. This is the cleanest counterexample in the file: **capex or financing headline must not substitute for named customer shipment and margin bridge**.

### 4.4 001530 DI동일 — capacity expansion can work when path stays low-MAE

DI동일 / Dong-il Aluminium is the positive foil-capacity case. The trigger was capacity expansion to meet growing EV battery market demand. This translated into 90D MFE `+52.48%`, 180D MFE `+64.11%`, and 180D MAE only `-4.70%`. The row supports allowing Stage3-Yellow when capacity expansion is not just theme, but a visible conversion route into battery foil demand. Still, post-peak drawdown `-27.45%` means local 4B monitoring should remain active.

### 4.5 091580 상신이디피 — customer concentration can be positive if revenue-share bridge is visible

Sangsin EDP is a battery CAN supplier row. Its report evidence links middle/large CAN to automotive/ESS batteries and indicates meaningful sales exposure. The 180D path is constructive: MFE `+58.26%`, MAE `-8.82%`, and post-peak drawdown `-16.11%`. Customer concentration is normally a risk, but for C11 it can be positive when the component is embedded in the battery maker's production chain and revenue share is visible.

## 5. Current calibrated profile stress test

Current calibrated global rules already block obvious price-only blowoff and require non-price evidence for full 4B. The residual C11 error is subtler:

```text
residual_error_1 = parent_or_subsidiary_JV_capacity_headline_can_be_overweighted
residual_error_2 = capex_or_financing_for_battery_materials_can_be_misread_as_orderbook
residual_error_3 = strong battery-can/foil beta can be positive, but must still trigger local 4B after vertical MFE
residual_error_4 = customer concentration is not automatically negative; it becomes positive only when revenue-share and utilization bridge are visible
```

The profile should not simply increase or decrease C11. It should **split the C11 bridge**:

```text
allow_upstage_if = named_customer + shipment/delivery timing + revenue recognition + margin/FCF or utilization bridge
cap_stage_if = parent-level JV only OR capacity financing only OR theme-only battery material proxy
activate_4B_watch_if = fast MFE + post-peak drawdown > 25% OR no fresh shipment/margin update after vertical rerating
```

## 6. Machine-readable trigger rows

```jsonl
{"row_type": "trigger", "research_file": "e2r_stock_web_v12_residual_round_R3_loop_103_L3_BATTERY_EV_GREEN_MOBILITY_C11_BATTERY_ORDERBOOK_RERATING_research.md", "selected_round": "R3", "selected_loop": 103, "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C11_BATTERY_ORDERBOOK_RERATING", "fine_archetype_id": "battery_parent_jv_orderbook_proxy_high_mae", "symbol": "096770", "symbol_name": "SK이노베이션", "trigger_type": "Stage2-Actionable", "trigger_date": "2023-04-25", "entry_date": "2023-04-26", "entry_price": 177500, "MFE_30D_pct": 16.9, "MAE_30D_pct": -3.21, "MFE_90D_pct": 29.3, "MAE_90D_pct": -11.1, "MFE_180D_pct": 29.3, "MAE_180D_pct": -36.51, "peak_date": "2023-07-26", "peak_price": 229500, "drawdown_after_peak_pct": -50.89, "post_peak_trough_date": "2024-01-19", "last_window_date": "2024-01-19", "price_source": "Songdaiki/stock-web", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/096/096770/2023.csv", "calibration_usable": true, "mfe_mae_complete": true, "window_180D_corporate_action_contaminated": false, "corporate_action_candidate_dates_note": "2024-11-20 only; outside entry~180D window", "evidence_source_url": "https://www.hyundai.com/worldwide/en/newsroom/detail/hyundai-motor-group-and-sk-on-to-establish-ev-battery-cell-production-joint-venture-in-us-0000000237", "case_role": "counterexample", "outcome_label": "counterexample_parent_jv_high_mae", "recommended_stage_after_calibration": "Stage2 cap / Stage4B watch", "current_profile_error": "Parent/JV capacity evidence could be over-read as orderbook rerating even though stock path had -36.51% 180D MAE and -50.89% post-peak drawdown.", "hard_duplicate_key": "C11_BATTERY_ORDERBOOK_RERATING|096770|Stage2-Actionable|2023-04-26"}
{"row_type": "trigger", "research_file": "e2r_stock_web_v12_residual_round_R3_loop_103_L3_BATTERY_EV_GREEN_MOBILITY_C11_BATTERY_ORDERBOOK_RERATING_research.md", "selected_round": "R3", "selected_loop": 103, "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C11_BATTERY_ORDERBOOK_RERATING", "fine_archetype_id": "cylindrical_battery_can_material_orderbook_beta", "symbol": "002710", "symbol_name": "TCC스틸", "trigger_type": "Stage3-Yellow", "trigger_date": "2023-03-09", "entry_date": "2023-03-10", "entry_price": 17100, "MFE_30D_pct": 186.55, "MAE_30D_pct": -8.77, "MFE_90D_pct": 236.26, "MAE_90D_pct": -8.77, "MFE_180D_pct": 340.35, "MAE_180D_pct": -8.77, "peak_date": "2023-07-26", "peak_price": 75300, "drawdown_after_peak_pct": -38.51, "post_peak_trough_date": "2023-08-17", "last_window_date": "2023-11-30", "price_source": "Songdaiki/stock-web", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/002/002710/2023.csv", "calibration_usable": true, "mfe_mae_complete": true, "window_180D_corporate_action_contaminated": false, "corporate_action_candidate_dates_note": "2009-05-08 only; outside entry~180D window", "evidence_source_url": "https://www.asiae.co.kr/en/print.htm?idxno=2023030908193595931", "case_role": "positive", "outcome_label": "positive_high_mfe_with_4b_exit_need", "recommended_stage_after_calibration": "Stage3-Yellow with local 4B after peak", "current_profile_error": "The old profile can catch upside but needs a local 4B exit/overheat rule after vertical MFE because post-peak drawdown reached -38.51%.", "hard_duplicate_key": "C11_BATTERY_ORDERBOOK_RERATING|002710|Stage3-Yellow|2023-03-10"}
{"row_type": "trigger", "research_file": "e2r_stock_web_v12_residual_round_R3_loop_103_L3_BATTERY_EV_GREEN_MOBILITY_C11_BATTERY_ORDERBOOK_RERATING_research.md", "selected_round": "R3", "selected_loop": 103, "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C11_BATTERY_ORDERBOOK_RERATING", "fine_archetype_id": "battery_can_capacity_financing_false_stage2", "symbol": "014820", "symbol_name": "동원시스템즈", "trigger_type": "Stage2-Actionable", "trigger_date": "2023-04-28", "entry_date": "2023-05-02", "entry_price": 43400, "MFE_30D_pct": 3.34, "MAE_30D_pct": -8.64, "MFE_90D_pct": 3.34, "MAE_90D_pct": -22.81, "MFE_180D_pct": 3.34, "MAE_180D_pct": -36.41, "peak_date": "2023-05-08", "peak_price": 44850, "drawdown_after_peak_pct": -38.46, "post_peak_trough_date": "2023-11-01", "last_window_date": "2024-01-24", "price_source": "Songdaiki/stock-web", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/014/014820/2023.csv", "calibration_usable": true, "mfe_mae_complete": true, "window_180D_corporate_action_contaminated": false, "corporate_action_candidate_dates_note": "1999-04-26, 2002-05-31, 2005-03-15, 2013-01-28; outside entry~180D window", "evidence_source_url": "https://pulse.mk.co.kr/news/english/10723889", "case_role": "counterexample", "outcome_label": "counterexample_capacity_financing_no_margin_bridge", "recommended_stage_after_calibration": "Stage2 cap / Stage4B watch", "current_profile_error": "Capacity funding and battery-material ambition were not enough; without named customer shipment and margin bridge, MFE was only +3.34% while 180D MAE hit -36.41%.", "hard_duplicate_key": "C11_BATTERY_ORDERBOOK_RERATING|014820|Stage2-Actionable|2023-05-02"}
{"row_type": "trigger", "research_file": "e2r_stock_web_v12_residual_round_R3_loop_103_L3_BATTERY_EV_GREEN_MOBILITY_C11_BATTERY_ORDERBOOK_RERATING_research.md", "selected_round": "R3", "selected_loop": 103, "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C11_BATTERY_ORDERBOOK_RERATING", "fine_archetype_id": "aluminum_foil_capacity_expansion_orderbook_proxy", "symbol": "001530", "symbol_name": "DI동일", "trigger_type": "Stage3-Yellow", "trigger_date": "2023-05-17", "entry_date": "2023-05-18", "entry_price": 20200, "MFE_30D_pct": 17.57, "MAE_30D_pct": -3.37, "MFE_90D_pct": 52.48, "MAE_90D_pct": -4.7, "MFE_180D_pct": 64.11, "MAE_180D_pct": -4.7, "peak_date": "2023-11-14", "peak_price": 33150, "drawdown_after_peak_pct": -27.45, "post_peak_trough_date": "2024-01-18", "last_window_date": "2024-02-08", "price_source": "Songdaiki/stock-web", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/001/001530/2023.csv", "calibration_usable": true, "mfe_mae_complete": true, "window_180D_corporate_action_contaminated": false, "corporate_action_candidate_dates_note": "2022-04-19 only; outside entry~180D window", "evidence_source_url": "https://www.yieh.com/en/News/south-koreas-dong-il-aluminium-increases-production-capacity-for-growing-demand-in-global-ev-battery-markets/141154", "case_role": "positive", "outcome_label": "positive_capacity_conversion_with_low_mae", "recommended_stage_after_calibration": "Stage3-Yellow / local 4B after peak", "current_profile_error": "This is the positive holdout: capacity expansion plus industry demand translated into +64.11% MFE with only -4.70% 180D MAE; still needs post-peak 4B monitoring.", "hard_duplicate_key": "C11_BATTERY_ORDERBOOK_RERATING|001530|Stage3-Yellow|2023-05-18"}
{"row_type": "trigger", "research_file": "e2r_stock_web_v12_residual_round_R3_loop_103_L3_BATTERY_EV_GREEN_MOBILITY_C11_BATTERY_ORDERBOOK_RERATING_research.md", "selected_round": "R3", "selected_loop": 103, "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C11_BATTERY_ORDERBOOK_RERATING", "fine_archetype_id": "battery_can_customer_concentration_revenue_share", "symbol": "091580", "symbol_name": "상신이디피", "trigger_type": "Stage3-Yellow", "trigger_date": "2024-12-05", "entry_date": "2024-12-06", "entry_price": 7140, "MFE_30D_pct": 17.23, "MAE_30D_pct": -8.82, "MFE_90D_pct": 38.66, "MAE_90D_pct": -8.82, "MFE_180D_pct": 58.26, "MAE_180D_pct": -8.82, "peak_date": "2025-08-12", "peak_price": 11300, "drawdown_after_peak_pct": -16.11, "post_peak_trough_date": "2025-08-21", "last_window_date": "2025-09-03", "price_source": "Songdaiki/stock-web", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/091/091580/2024.csv", "calibration_usable": true, "mfe_mae_complete": true, "window_180D_corporate_action_contaminated": false, "corporate_action_candidate_dates_note": "2007-06-11, 2010-01-26, 2011-05-11; outside entry~180D window", "evidence_source_url": "https://w4.kirs.or.kr/download/research/241205_IT%EB%B6%80%ED%92%88_%EC%83%81%EC%8B%A0%EC%9D%B4%EB%94%94%ED%94%BC%28091580%29_%EC%95%88%EC%A0%84%ED%95%9C%20%EC%9D%B4%EC%B0%A8%EC%A0%84%EC%A7%80%EB%A5%BC%20%EC%9C%84%ED%95%9C%20CAN%20%EC%A0%9C%EC%A1%B0%20%ED%9A%8C%EC%82%AC_%ED%95%9C%EA%B5%AD%EA%B8%B0%EC%88%A0%EC%8B%A0%EC%9A%A9%ED%8F%89%EA%B0%80%28%EC%A3%BC%29.pdf", "case_role": "positive", "outcome_label": "positive_customer_concentration_component_rerating", "recommended_stage_after_calibration": "Stage3-Yellow / 4B watch if MAE widens", "current_profile_error": "Customer concentration is normally a risk, but here CAN revenue share and 180D path supported a positive C11 row; profile should reward revenue-share bridge but cap if customer utilization deteriorates.", "hard_duplicate_key": "C11_BATTERY_ORDERBOOK_RERATING|091580|Stage3-Yellow|2024-12-06"}
```

## 7. Machine-readable score simulation rows

```jsonl
{"row_type": "score_simulation", "symbol": "096770", "canonical_archetype_id": "C11_BATTERY_ORDERBOOK_RERATING", "eps_fcf_explosion": 47, "earnings_visibility": 56, "bottleneck_pricing": 62, "market_mispricing": 45, "valuation_rerating": 50, "capital_allocation": 42, "information_confidence": 72, "raw_total_score_proxy": 68.0, "baseline_stage_proxy": "Stage2-Actionable", "recommended_stage_after_price_path": "Stage2 cap / Stage4B watch", "score_return_alignment_note": "Parent/JV capacity evidence could be over-read as orderbook rerating even though stock path had -36.51% 180D MAE and -50.89% post-peak drawdown."}
{"row_type": "score_simulation", "symbol": "002710", "canonical_archetype_id": "C11_BATTERY_ORDERBOOK_RERATING", "eps_fcf_explosion": 58, "earnings_visibility": 66, "bottleneck_pricing": 72, "market_mispricing": 67, "valuation_rerating": 56, "capital_allocation": 45, "information_confidence": 70, "raw_total_score_proxy": 78.5, "baseline_stage_proxy": "Stage3-Yellow", "recommended_stage_after_price_path": "Stage3-Yellow with local 4B after peak", "score_return_alignment_note": "The old profile can catch upside but needs a local 4B exit/overheat rule after vertical MFE because post-peak drawdown reached -38.51%."}
{"row_type": "score_simulation", "symbol": "014820", "canonical_archetype_id": "C11_BATTERY_ORDERBOOK_RERATING", "eps_fcf_explosion": 42, "earnings_visibility": 48, "bottleneck_pricing": 55, "market_mispricing": 43, "valuation_rerating": 41, "capital_allocation": 38, "information_confidence": 68, "raw_total_score_proxy": 61.0, "baseline_stage_proxy": "Stage2 cap", "recommended_stage_after_price_path": "Stage2 cap / Stage4B watch", "score_return_alignment_note": "Capacity funding and battery-material ambition were not enough; without named customer shipment and margin bridge, MFE was only +3.34% while 180D MAE hit -36.41%."}
{"row_type": "score_simulation", "symbol": "001530", "canonical_archetype_id": "C11_BATTERY_ORDERBOOK_RERATING", "eps_fcf_explosion": 56, "earnings_visibility": 64, "bottleneck_pricing": 68, "market_mispricing": 59, "valuation_rerating": 54, "capital_allocation": 44, "information_confidence": 69, "raw_total_score_proxy": 76.0, "baseline_stage_proxy": "Stage3-Yellow", "recommended_stage_after_price_path": "Stage3-Yellow / local 4B after peak", "score_return_alignment_note": "This is the positive holdout: capacity expansion plus industry demand translated into +64.11% MFE with only -4.70% 180D MAE; still needs post-peak 4B monitoring."}
{"row_type": "score_simulation", "symbol": "091580", "canonical_archetype_id": "C11_BATTERY_ORDERBOOK_RERATING", "eps_fcf_explosion": 54, "earnings_visibility": 63, "bottleneck_pricing": 66, "market_mispricing": 58, "valuation_rerating": 53, "capital_allocation": 43, "information_confidence": 67, "raw_total_score_proxy": 74.5, "baseline_stage_proxy": "Stage2-Actionable", "recommended_stage_after_price_path": "Stage3-Yellow / 4B watch if MAE widens", "score_return_alignment_note": "Customer concentration is normally a risk, but here CAN revenue share and 180D path supported a positive C11 row; profile should reward revenue-share bridge but cap if customer utilization deteriorates."}
```

## 8. Aggregate / shadow-weight / residual-contribution rows

```jsonl
{"row_type": "aggregate", "research_file": "e2r_stock_web_v12_residual_round_R3_loop_103_L3_BATTERY_EV_GREEN_MOBILITY_C11_BATTERY_ORDERBOOK_RERATING_research.md", "canonical_archetype_id": "C11_BATTERY_ORDERBOOK_RERATING", "usable_trigger_count": 5, "positive_case_count": 3, "counterexample_count": 2, "stage4b_watch_case_count": 4, "stage4c_case_count": 0, "mean_MFE_180D_pct": 99.07, "mean_MAE_180D_pct": -19.04, "median_MFE_180D_pct": 58.26, "median_MAE_180D_pct": -8.82, "current_profile_error_count": 4}
{"row_type": "shadow_weight_candidate", "canonical_archetype_id": "C11_BATTERY_ORDERBOOK_RERATING", "rule_candidate": "C11_ORDERBOOK_REQUIRES_NAMED_CUSTOMER_SHIPMENT_CAPACITY_AND_MARGIN_CONVERSION_GATE_THIRD_PASS", "increase_axes": ["earnings_visibility", "information_confidence", "customer_quality_delivery_bridge"], "decrease_axes": ["headline_orderbook_without_shipment", "parent_or_capacity_proxy_without_segment_margin"], "guardrail_axes": ["local_4b_watch_guard", "price_only_blowoff_blocks_positive_stage", "full_4b_requires_non_price_evidence"], "proposal_strength": "medium"}
{"row_type": "residual_contribution", "canonical_archetype_id": "C11_BATTERY_ORDERBOOK_RERATING", "contribution_label": "canonical_archetype_rule_candidate", "summary": "C11 needs separation of named-customer/orderbook evidence from delivery/revenue/margin conversion. Battery can/foil proxy can work, but parent JV and capacity-financing headlines need 4B/high-MAE caps."}
```

## 9. Shadow rule candidate

```text
C11_ORDERBOOK_REQUIRES_NAMED_CUSTOMER_SHIPMENT_CAPACITY_AND_MARGIN_CONVERSION_GATE_THIRD_PASS
```

Rule compression:

```text
IF canonical_archetype_id == C11_BATTERY_ORDERBOOK_RERATING:
  Stage3-Yellow may unlock only when at least two of the following are present:
    - named customer or clearly identifiable battery maker chain
    - shipment/delivery timing or utilization/capacity conversion
    - revenue recognition or segment sales bridge
    - margin/FCF bridge or material spread stability
  ELSE:
    cap at Stage2-Actionable or Stage2 cap

  IF evidence is parent-level JV, financing-only capex, or generic battery-material theme:
    require Stage4B watch unless 90D/180D MAE remains controlled and follow-up revenue bridge appears

  IF MFE_90D or MFE_180D is large but post-peak drawdown exceeds 25%:
    add local_4B_watch even for positive rows
```

## 10. Deferred Coding Agent Handoff Prompt

```text
You are a later coding agent. Do not execute this during the research session.

Task:
- Ingest this MD as a V12 residual research file.
- Parse all machine-readable trigger rows.
- Validate standard filename and metadata consistency.
- Validate complete MFE/MAE 30D/90D/180D fields.
- Treat all 5 trigger rows as calibration_usable=true only if the stock-web corporate-action profile still shows no candidate inside entry~180D.
- Add the proposed C11 shadow rule candidate to the candidate pool, not production scoring.
- Compare the rule against existing C11 rows before applying any weight delta.

Expected patch target later:
- archetype-specific rule candidate for C11 only.
- no global Stage2/Stage3 threshold change from this file alone.
```

## 11. Residual Contribution Summary

```yaml
selected_round: R3
selected_loop: 103
selection_basis: docs/core/V12_Research_No_Repeat_Index.md
selected_priority_bucket: Priority 0 / under 30 rows
large_sector_id: L3_BATTERY_EV_GREEN_MOBILITY
canonical_archetype_id: C11_BATTERY_ORDERBOOK_RERATING
new_independent_case_count: 5
reused_case_count: 0
same_archetype_new_symbol_count: 5
same_archetype_new_trigger_family_count: 5
positive_case_count: 3
counterexample_count: 2
stage4b_watch_case_count: 4
stage4c_case_count: 0
current_profile_error_count: 4
calibration_usable_rows: 5
auto_selected_coverage_gap: No-Repeat static C11 18 -> 23 after this file; current-session adjusted C11 loop_101/102/103 기준 18 -> 34
sector_specific_rule_candidate: L3_C11_BATTERY_ORDERBOOK_SHIPMENT_MARGIN_BRIDGE_AND_HIGH_MAE_SPLIT
canonical_archetype_rule_candidate: C11_ORDERBOOK_REQUIRES_NAMED_CUSTOMER_SHIPMENT_CAPACITY_AND_MARGIN_CONVERSION_GATE_THIRD_PASS
loop_contribution_label: canonical_archetype_rule_candidate
existing_axis_strengthened:
  - stage2_required_bridge
  - local_4b_watch_guard
  - full_4b_requires_non_price_evidence
  - price_only_blowoff_blocks_positive_stage
existing_axis_weakened: null
production_scoring_patch_applied: false
handoff_prompt_executed_now: false
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
calibration_usable_rows: 5
representative_rows: 5
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
completed_round = R3
completed_loop = 103
selection_basis = docs/core/V12_Research_No_Repeat_Index.md
selected_priority_bucket = Priority 0 / under 30 rows
next_recommended_archetypes = C02_POWER_GRID_DATACENTER_CAPEX | C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF | C14_EV_DEMAND_SLOWDOWN_4B_4C | C06_HBM_MEMORY_CUSTOMER_CAPACITY
round_schedule_status = coverage_index_selected
round_sector_consistency = pass
```
