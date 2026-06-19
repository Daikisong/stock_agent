# E2R Stock-Web v12 Residual Research — R4 / L4 / C15 Cement coal-power price-pass-through spread repair

```text
selected_round: R4
selected_loop: 194
selection_basis: docs/core/V12_Research_No_Repeat_Index.md
selected_priority_bucket: Priority 1 balance reinforcement / URL-proxy quality repair
round_schedule_status: coverage_index_selected
round_sector_consistency: pass

large_sector_id: L4_MATERIALS_SPREAD_RESOURCE
canonical_archetype_id: C15_MATERIAL_SPREAD_SUPERCYCLE
fine_archetype_id: C15_CEMENT_COAL_POWER_PRICE_PASS_THROUGH_SPREAD_REPAIR

mode: historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12
research_session: post_calibrated_sector_archetype_residual_research
production_scoring_changed: false
shadow_weight_only: true
stock_agent_code_patch_allowed: false
stock_agent_live_scan_allowed: false
current_stock_discovery_allowed: false
```

## 1. Coverage-index selection

The no-repeat ledger says all C01~C32 archetypes are above the 80-row level, so the scheduler is no longer a simple row-count filler. Priority 1 now asks for balance/quality reinforcement in C05, C01, C13, C15, and C10. I selected `C15_MATERIAL_SPREAD_SUPERCYCLE` because the latest C15 work in this session was steel/pipe/spread-heavy; this loop adds a different C15 sub-family: **cement price pass-through versus coal/electricity/demand spread durability**.

```text
index_snapshot:
  representative_rows: 11200
  C15 rows/symbols: 208 / 60
  C15 positives/counter: 32 / 55
  C15 4B/4C: 27 / 4
  next_direction_from_index: spread reversal and inventory-cycle counterexample reinforcement

anti_repeat_basis:
  hard_duplicate_key: canonical_archetype_id + symbol + trigger_type + entry_date
  selected_subfamily_not_reused: cement_coal_power_price_pass_through
  new_symbol_count: 5
  new_trigger_family_count: 3
```

## 2. Stock-Web price atlas validation

```text
price_source: Songdaiki/stock-web
manifest_max_date: 2026-02-20
source_name: FinanceData/marcap
price_basis: tradable_raw
price_adjustment_status: raw_unadjusted_marcap
calibration_shard_root: atlas/ohlcv_tradable_by_symbol_year
tradable_columns: d,o,h,l,c,v,a,mc,s,m
MFE_N_pct: (max high from entry_date through N tradable rows / entry_price - 1) * 100
MAE_N_pct: (min low from entry_date through N tradable rows / entry_price - 1) * 100
```

Profile checks used the Stock-Web symbol profiles. The selected windows do not overlap each symbol's corporate-action candidate dates: Hanil Cement candidates are 2020-08-14 and 2021-09-13; Sungshin candidates are historical 1998~2001; Sampyo's candidates end in 2014; Asia Cement has a 2022-04-06 candidate; Hanil Hyundai Cement candidates end in 2016. All usable rows have at least 180 forward tradable rows.

## 3. Evidence basis

- Korea Times / Asiae June 2023 price-hike conflict: Sungshin Cement and Ssangyong C&E announced mid-teen cement price hikes after operating losses; Hanil, Asia, and Sampyo were profitable but had not yet announced their own hikes. This is a good C15 test because the price-pass-through evidence was sector-level and contested by buyers.
- CemNet February 2024: Sungshin Cement's 2023 operating profit surged to KRW77.73bn and net profit turned positive, giving a real issuer-level profit bridge.
- Asiae March 2024 Hanil Cement note: Q4 2023 sales/OP, Remital price-driven growth, stabilized coal cost, price defense, recovered operating cash flow, and strong balance sheet.
- CemNet December 2024: demand weakened and Q3 sales fell for Hanil, Asia, and Sampyo while electricity rates rose, testing whether demand decline should be sticky hard 4C or just local 4B/watch.

## 4. Trigger-level backtest table

| # | Symbol | Name | Trigger | Entry | Entry px | 30D MFE/MAE | 90D MFE/MAE | 180D MFE/MAE | Role |
|---:|---|---|---|---|---:|---:|---:|---:|---|
| 1 | 004980 | Sungshin Cement | Stage4B | 2023-06-05 | 9,980 | 4.61/-17.33 | 14.13/-18.84 | 14.13/-20.84 | loss_plus_price_hike_watch |
| 2 | 038500 | Sampyo Cement | Stage2 | 2023-06-07 | 3,750 | 2.80/-15.47 | 2.80/-16.93 | 2.80/-21.87 | profitable_but_no_direct_price_hike_bridge |
| 3 | 183190 | Asia Cement | Stage2 | 2023-06-07 | 10,590 | 3.02/-14.83 | 10.67/-18.32 | 10.67/-18.32 | sector_price_hike_proxy_without_company_bridge |
| 4 | 004980 | Sungshin Cement | Stage2-Actionable | 2024-02-21 | 8,770 | 9.35/-5.36 | 14.03/-6.73 | 14.03/-13.23 | actual_operating_profit_turnaround |
| 5 | 300720 | Hanil Cement | Stage2-Actionable | 2024-03-25 | 12,260 | 8.24/-1.71 | 37.68/-1.71 | 37.68/-1.71 | price_defense_and_cashflow_bridge |
| 6 | 006390 | Hanil Hyundai Cement | Stage4B | 2024-03-25 | 15,010 | 3.93/-2.47 | 14.59/-10.53 | 14.59/-12.72 | shipment_decline_and_cost_ratio_watch |
| 7 | 038500 | Sampyo Cement | Stage4B | 2024-12-30 | 2,945 | 18.85/-1.02 | 20.88/-2.72 | 22.58/-2.72 | demand_decline_sales_drop_but_not_hard_4c |
| 8 | 300720 | Hanil Cement | Stage4B | 2024-12-30 | 14,520 | 13.64/-1.31 | 30.17/-1.31 | 50.83/-1.31 | volume_demand_decline_offset_test |
| 9 | 183190 | Asia Cement | Stage4B | 2024-12-30 | 10,280 | 5.54/-2.63 | 12.26/-5.06 | 52.72/-5.06 | largest_sales_drop_but_forward_rebound |


## 5. Case notes

### 5.1 Early price-hike rows: sector pass-through is not the same as issuer margin conversion

The June 2023 cement price-hike conflict was real bottleneck-pricing evidence, but it had two weaknesses. First, the direct issuer bridge was asymmetric: Sungshin had an announced hike after a Q1 loss, while Hanil/Asia/Sampyo were mostly sector-follow-through candidates. Second, buyers disputed the cost justification because thermal coal had fallen from the prior year's extreme. That makes these rows Stage2 or local Stage4B/watch, not clean Stage3-Yellow.

Observed forward paths support the guardrail. Sampyo's sector-proxy row had only 2.80% 180D MFE with -21.87% MAE, and Asia's row had 10.67% 180D MFE with -18.32% MAE. The pass-through headline did not guarantee durable rerating without issuer-specific volume/margin/cash bridge.

### 5.2 Issuer-level profit and cash bridge works better, but still does not loosen Green

Sungshin's February 2024 turnaround was more concrete than the 2023 price-hike headline. Its 180D MFE/MAE was 14.03% / -13.23%, usable but not a Green-quality acceleration. Hanil Cement's March 2024 row was stronger because the evidence included Q4 OP, Remital pricing, coal stabilization, price defense, operating cash flow, and balance-sheet quality. Its 180D path was 37.68% MFE with only -1.71% MAE.

This is the key C15 nuance: **cement price pass-through can be Stage2-Actionable when it has a second bridge, but C15 Green still needs repeat cashflow / working-capital / margin durability rather than a single price hike or single-quarter profit print.**

### 5.3 Demand-decline rows in late 2024 should often be 4B/watch, not hard 4C

The December 2024 sector decline row looked ugly: sales fell for Hanil, Asia, and Sampyo, demand was weakening, and electricity tariffs were up. But the forward paths were unexpectedly strong. Sampyo's 180D MFE/MAE was 22.58% / -2.72%, Hanil's was 50.83% / -1.31%, and Asia's was 52.72% / -5.06%.

That means a demand-decline headline should not become sticky hard 4C without a company-level thesis break such as pricing failure, coal/electricity cost shock that cannot be passed through, cashflow/working-capital deterioration, or balance-sheet stress.

## 6. Score-return alignment and current profile stress test

```text
new_independent_case_count: 9
reused_case_count: 0
new_symbol_count: 5
same_archetype_new_symbol_count: 5
same_archetype_new_trigger_family_count: 3
new_trigger_family_count: 3

calibration_usable_case_count: 9
calibration_usable_trigger_count: 9
positive_case_count: 2
counterexample_count: 7
current_profile_error_count: 9

source_proxy_only_count: 0
evidence_url_pending_count: 0
missing_required_mfe_mae_count: 0
missing_entry_price_count: 0
missing_entry_date_count: 0
corporate_action_contaminated_180D_count: 0
insufficient_forward_window_180D_count: 0

production_scoring_changed: false
shadow_weight_only: true
do_not_propose_new_weight_delta: false
```

Diversity summary:

```text
- New C15 subfamily: cement / bituminous coal / electricity / price-pass-through spread.
- New symbols in this subfamily: 004980, 038500, 183190, 300720, 006390.
- Positive controls: issuer-level profit/cash bridge rows for Hanil and Sungshin.
- Counterexamples: sector price-hike proxy rows with weak MFE or deep MAE.
- 4B watch holdouts: late-2024 demand-decline rows with strong forward rebound.
```

## 7. Residual contribution

```text
loop_contribution_label: canonical_archetype_rule_candidate
existing_axis_tested:
  - stage2_required_bridge
  - local_4b_watch_guard
  - stage3_green_not_loosened
existing_axis_strengthened:
  - stage2_required_bridge
  - local_4b_watch_guard
existing_axis_kept:
  - stage3_green_not_loosened
new_axis_proposed: no_global_axis
sector_specific_rule_candidate: L4_MATERIAL_PRICE_PASS_THROUGH_SECOND_BRIDGE_GATE
canonical_archetype_rule_candidate: C15_CEMENT_PRICE_PASS_THROUGH_VOLUME_COST_CASHFLOW_GATE
```

### Proposed shadow rule candidate

```text
C15_CEMENT_PRICE_PASS_THROUGH_VOLUME_COST_CASHFLOW_GATE:
  1. Cement price hike / coal cost / electricity cost headline alone remains Stage2 or local Stage4B/watch.
  2. Stage2-Actionable requires at least one issuer-level second bridge:
     - reported operating-profit conversion,
     - realized price defense with shipment stability,
     - coal/electricity cost stabilization,
     - cashflow / working-capital recovery,
     - balance-sheet resilience,
     - or durable product-mix pricing power such as Remital.
  3. Sector-level pass-through evidence without issuer-specific margin conversion blocks Stage3-Yellow/Green.
  4. Demand-decline evidence should route to Stage4B/watch first.
  5. Hard Stage4C requires confirmed issuer-level pricing failure, margin spread break, cashflow/working-capital deterioration, or balance-sheet stress; demand headline or price drawdown alone is insufficient.
```

This loop adds 9 new independent cases, 7 counterexamples/guardrails, and 9 residual errors for R4/L4/C15.

## 8. Machine-readable trigger rows JSONL

```jsonl
{"MAE_180D_pct": -20.84, "MAE_30D_pct": -17.33, "MAE_90D_pct": -18.84, "MFE_180D_pct": 14.13, "MFE_30D_pct": 4.61, "MFE_90D_pct": 14.13, "aggregate_group_role": "representative", "calibration_usable": true, "canonical_archetype_id": "C15_MATERIAL_SPREAD_SUPERCYCLE", "case_id": "C15_CEMENT_01_004980_2023-06-05_Stage4B", "case_role": "loss_plus_price_hike_watch", "company_name": "Sungshin Cement", "corporate_action_window_status": "not_contaminated", "current_profile_error_type": "green_blocker_or_4c_stickiness_risk", "current_profile_expected_label": "capped_stage2_or_4b_watch", "dedupe_for_aggregate": true, "do_not_count_as_new_case": false, "entry_amount": 9657723100.0, "entry_close": 9980.0, "entry_date": "2023-06-05", "entry_high": 10440.0, "entry_low": 9800.0, "entry_market_cap": 244670408540.0, "entry_open": 9920.0, "entry_price": 9980.0, "evidence_date": "2023-06-05", "evidence_summary": "Sungshin announced a 14.3% cement price increase after a Q1 operating loss; coal/electricity/price-passing debate made the row a 4B watch, not a clean positive rerating.", "evidence_urls": ["https://www.asiae.co.kr/en/article/2023060510253612929", "https://www.koreatimes.co.kr/business/companies/20230606/builders-cry-foul-over-soaring-cement-prices"], "fine_archetype_id": "C15_CEMENT_COAL_POWER_PRICE_PASS_THROUGH_SPREAD_REPAIR", "forward_window_trading_days": 180, "independent_evidence_weight": 1.0, "large_sector_id": "L4_MATERIALS_SPREAD_RESOURCE", "market": "KOSPI", "peak_180D_date": "2023-08-18", "peak_30D_date": "2023-06-05", "peak_90D_date": "2023-08-18", "price_adjustment_status": "raw_unadjusted_marcap", "price_basis": "tradable_raw", "price_data_source": "Songdaiki/stock-web", "price_source": "Songdaiki/stock-web", "raw_component_score_breakdown": {"bottleneck_pricing": 17, "capital_allocation": 4, "earnings_visibility": 10, "eps_fcf_explosion": 8, "information_confidence": 13, "market_mispricing": 8, "valuation_rerating": 7}, "raw_total_score": 67, "residual_label": "cement_price_pass_through_needs_volume_cost_cash_second_bridge", "result_file": "e2r_stock_web_v12_residual_round_R4_loop_194_L4_MATERIALS_SPREAD_RESOURCE_C15_MATERIAL_SPREAD_SUPERCYCLE_research.md", "reuse_reason": "same canonical, new cement/fuel-price trigger family; no same ticker+trigger+entry duplication in this session", "role": "counterexample_or_guardrail", "row_type": "trigger", "same_entry_group_id": "C15_CEMENT_004980_2023-06-05_Stage4B", "selected_loop": 194, "selected_round": "R4", "stock_web_profile": "atlas/symbol_profiles/004/004980.json", "stock_web_shard": "atlas/ohlcv_tradable_by_symbol_year/004/004980/2023.csv", "symbol": "004980", "trigger_date": "2023-06-05", "trigger_type": "Stage4B", "trough_180D_date": "2024-01-25", "trough_30D_date": "2023-07-07", "trough_90D_date": "2023-07-27"}
{"MAE_180D_pct": -21.87, "MAE_30D_pct": -15.47, "MAE_90D_pct": -16.93, "MFE_180D_pct": 2.8, "MFE_30D_pct": 2.8, "MFE_90D_pct": 2.8, "aggregate_group_role": "representative", "calibration_usable": true, "canonical_archetype_id": "C15_MATERIAL_SPREAD_SUPERCYCLE", "case_id": "C15_CEMENT_02_038500_2023-06-07_Stage2", "case_role": "profitable_but_no_direct_price_hike_bridge", "company_name": "Sampyo Cement", "corporate_action_window_status": "not_contaminated", "current_profile_error_type": "stage2_bridge_quality_test", "current_profile_expected_label": "capped_stage2_or_4b_watch", "dedupe_for_aggregate": true, "do_not_count_as_new_case": false, "entry_amount": 852806195.0, "entry_close": 3750.0, "entry_date": "2023-06-07", "entry_high": 3810.0, "entry_low": 3750.0, "entry_market_cap": 404686147500.0, "entry_open": 3755.0, "entry_price": 3750.0, "evidence_date": "2023-06-06", "evidence_summary": "Sampyo was cited as profitable in Q1 while the industry expected follow-on price hikes, but evidence was sector-level rather than issuer-level margin conversion.", "evidence_urls": ["https://www.koreatimes.co.kr/business/companies/20230606/builders-cry-foul-over-soaring-cement-prices"], "fine_archetype_id": "C15_CEMENT_COAL_POWER_PRICE_PASS_THROUGH_SPREAD_REPAIR", "forward_window_trading_days": 180, "independent_evidence_weight": 1.0, "large_sector_id": "L4_MATERIALS_SPREAD_RESOURCE", "market": "KOSDAQ", "peak_180D_date": "2023-06-13", "peak_30D_date": "2023-06-13", "peak_90D_date": "2023-06-13", "price_adjustment_status": "raw_unadjusted_marcap", "price_basis": "tradable_raw", "price_data_source": "Songdaiki/stock-web", "price_source": "Songdaiki/stock-web", "raw_component_score_breakdown": {"bottleneck_pricing": 14, "capital_allocation": 3, "earnings_visibility": 11, "eps_fcf_explosion": 9, "information_confidence": 11, "market_mispricing": 8, "valuation_rerating": 7}, "raw_total_score": 63, "residual_label": "cement_price_pass_through_needs_volume_cost_cash_second_bridge", "result_file": "e2r_stock_web_v12_residual_round_R4_loop_194_L4_MATERIALS_SPREAD_RESOURCE_C15_MATERIAL_SPREAD_SUPERCYCLE_research.md", "reuse_reason": "same canonical, new cement/fuel-price trigger family; no same ticker+trigger+entry duplication in this session", "role": "counterexample", "row_type": "trigger", "same_entry_group_id": "C15_CEMENT_038500_2023-06-07_Stage2", "selected_loop": 194, "selected_round": "R4", "stock_web_profile": "atlas/symbol_profiles/038/038500.json", "stock_web_shard": "atlas/ohlcv_tradable_by_symbol_year/038/038500/2023.csv", "symbol": "038500", "trigger_date": "2023-06-06", "trigger_type": "Stage2", "trough_180D_date": "2024-01-23", "trough_30D_date": "2023-07-10", "trough_90D_date": "2023-07-26"}
{"MAE_180D_pct": -18.32, "MAE_30D_pct": -14.83, "MAE_90D_pct": -18.32, "MFE_180D_pct": 10.67, "MFE_30D_pct": 3.02, "MFE_90D_pct": 10.67, "aggregate_group_role": "representative", "calibration_usable": true, "canonical_archetype_id": "C15_MATERIAL_SPREAD_SUPERCYCLE", "case_id": "C15_CEMENT_03_183190_2023-06-07_Stage2", "case_role": "sector_price_hike_proxy_without_company_bridge", "company_name": "Asia Cement", "corporate_action_window_status": "not_contaminated", "current_profile_error_type": "stage2_bridge_quality_test", "current_profile_expected_label": "capped_stage2_or_4b_watch", "dedupe_for_aggregate": true, "do_not_count_as_new_case": false, "entry_amount": 790146550.0, "entry_close": 10590.0, "entry_date": "2023-06-07", "entry_high": 10910.0, "entry_low": 10510.0, "entry_market_cap": 412566173100.0, "entry_open": 10770.0, "entry_price": 10590.0, "evidence_date": "2023-06-06", "evidence_summary": "Asia Cement was included among profitable Q1 cement makers expected to consider hikes, but the row lacked a direct Asia Cement shipment/margin bridge.", "evidence_urls": ["https://www.koreatimes.co.kr/business/companies/20230606/builders-cry-foul-over-soaring-cement-prices", "https://www.asiae.co.kr/en/article/2023060510253612929"], "fine_archetype_id": "C15_CEMENT_COAL_POWER_PRICE_PASS_THROUGH_SPREAD_REPAIR", "forward_window_trading_days": 180, "independent_evidence_weight": 1.0, "large_sector_id": "L4_MATERIALS_SPREAD_RESOURCE", "market": "KOSPI", "peak_180D_date": "2023-10-18", "peak_30D_date": "2023-06-07", "peak_90D_date": "2023-10-18", "price_adjustment_status": "raw_unadjusted_marcap", "price_basis": "tradable_raw", "price_data_source": "Songdaiki/stock-web", "price_source": "Songdaiki/stock-web", "raw_component_score_breakdown": {"bottleneck_pricing": 14, "capital_allocation": 3, "earnings_visibility": 11, "eps_fcf_explosion": 9, "information_confidence": 11, "market_mispricing": 8, "valuation_rerating": 7}, "raw_total_score": 63, "residual_label": "cement_price_pass_through_needs_volume_cost_cash_second_bridge", "result_file": "e2r_stock_web_v12_residual_round_R4_loop_194_L4_MATERIALS_SPREAD_RESOURCE_C15_MATERIAL_SPREAD_SUPERCYCLE_research.md", "reuse_reason": "same canonical, new cement/fuel-price trigger family; no same ticker+trigger+entry duplication in this session", "role": "counterexample", "row_type": "trigger", "same_entry_group_id": "C15_CEMENT_183190_2023-06-07_Stage2", "selected_loop": 194, "selected_round": "R4", "stock_web_profile": "atlas/symbol_profiles/183/183190.json", "stock_web_shard": "atlas/ohlcv_tradable_by_symbol_year/183/183190/2023.csv", "symbol": "183190", "trigger_date": "2023-06-06", "trigger_type": "Stage2", "trough_180D_date": "2023-07-26", "trough_30D_date": "2023-06-29", "trough_90D_date": "2023-07-26"}
{"MAE_180D_pct": -13.23, "MAE_30D_pct": -5.36, "MAE_90D_pct": -6.73, "MFE_180D_pct": 14.03, "MFE_30D_pct": 9.35, "MFE_90D_pct": 14.03, "aggregate_group_role": "representative", "calibration_usable": true, "canonical_archetype_id": "C15_MATERIAL_SPREAD_SUPERCYCLE", "case_id": "C15_CEMENT_04_004980_2024-02-21_Stage2Actionable", "case_role": "actual_operating_profit_turnaround", "company_name": "Sungshin Cement", "corporate_action_window_status": "not_contaminated", "current_profile_error_type": "stage2_bridge_quality_test", "current_profile_expected_label": "capped_stage2_or_4b_watch", "dedupe_for_aggregate": true, "do_not_count_as_new_case": false, "entry_amount": 15008508670.0, "entry_close": 8770.0, "entry_date": "2024-02-21", "entry_high": 9590.0, "entry_low": 8770.0, "entry_market_cap": 215005960210.0, "entry_open": 9580.0, "entry_price": 8770.0, "evidence_date": "2024-02-21", "evidence_summary": "Sungshin reported 2023 operating profit KRW77.73bn versus KRW1.83bn in 2022, with net profit turning positive from a prior loss.", "evidence_urls": ["https://www.cemnet.com/News/story/176446/sungshin-cement-swings-into-the-black-in-2023.html"], "fine_archetype_id": "C15_CEMENT_COAL_POWER_PRICE_PASS_THROUGH_SPREAD_REPAIR", "forward_window_trading_days": 180, "independent_evidence_weight": 1.0, "large_sector_id": "L4_MATERIALS_SPREAD_RESOURCE", "market": "KOSPI", "peak_180D_date": "2024-06-05", "peak_30D_date": "2024-02-21", "peak_90D_date": "2024-06-05", "price_adjustment_status": "raw_unadjusted_marcap", "price_basis": "tradable_raw", "price_data_source": "Songdaiki/stock-web", "price_source": "Songdaiki/stock-web", "raw_component_score_breakdown": {"bottleneck_pricing": 15, "capital_allocation": 5, "earnings_visibility": 16, "eps_fcf_explosion": 18, "information_confidence": 14, "market_mispricing": 10, "valuation_rerating": 9}, "raw_total_score": 87, "residual_label": "cement_price_pass_through_needs_volume_cost_cash_second_bridge", "result_file": "e2r_stock_web_v12_residual_round_R4_loop_194_L4_MATERIALS_SPREAD_RESOURCE_C15_MATERIAL_SPREAD_SUPERCYCLE_research.md", "reuse_reason": "same canonical, new cement/fuel-price trigger family; no same ticker+trigger+entry duplication in this session", "role": "positive_structural_success", "row_type": "trigger", "same_entry_group_id": "C15_CEMENT_004980_2024-02-21_Stage2-Actionable", "selected_loop": 194, "selected_round": "R4", "stock_web_profile": "atlas/symbol_profiles/004/004980.json", "stock_web_shard": "atlas/ohlcv_tradable_by_symbol_year/004/004980/2024.csv", "symbol": "004980", "trigger_date": "2024-02-21", "trigger_type": "Stage2-Actionable", "trough_180D_date": "2024-08-05", "trough_30D_date": "2024-02-28", "trough_90D_date": "2024-04-16"}
{"MAE_180D_pct": -1.71, "MAE_30D_pct": -1.71, "MAE_90D_pct": -1.71, "MFE_180D_pct": 37.68, "MFE_30D_pct": 8.24, "MFE_90D_pct": 37.68, "aggregate_group_role": "representative", "calibration_usable": true, "canonical_archetype_id": "C15_MATERIAL_SPREAD_SUPERCYCLE", "case_id": "C15_CEMENT_05_300720_2024-03-25_Stage2Actionable", "case_role": "price_defense_and_cashflow_bridge", "company_name": "Hanil Cement", "corporate_action_window_status": "not_contaminated", "current_profile_error_type": "stage2_bridge_quality_test", "current_profile_expected_label": "capped_stage2_or_4b_watch", "dedupe_for_aggregate": true, "do_not_count_as_new_case": false, "entry_amount": 565313870.0, "entry_close": 12260.0, "entry_date": "2024-03-25", "entry_high": 12340.0, "entry_low": 12140.0, "entry_market_cap": 849146480400.0, "entry_open": 12260.0, "entry_price": 12260.0, "evidence_date": "2024-03-25", "evidence_summary": "Shinhan/Asiae described Q4 2023 sales KRW493.8bn, OP KRW64.7bn, Remital price-driven growth, stable coal costs, and recovered operating cash flow.", "evidence_urls": ["https://www.asiae.co.kr/en/article/2024032507455089335", "https://www.hanilcement.com/en/html/about/ct_04.html"], "fine_archetype_id": "C15_CEMENT_COAL_POWER_PRICE_PASS_THROUGH_SPREAD_REPAIR", "forward_window_trading_days": 180, "independent_evidence_weight": 1.0, "large_sector_id": "L4_MATERIALS_SPREAD_RESOURCE", "market": "KOSPI", "peak_180D_date": "2024-06-05", "peak_30D_date": "2024-04-30", "peak_90D_date": "2024-06-05", "price_adjustment_status": "raw_unadjusted_marcap", "price_basis": "tradable_raw", "price_data_source": "Songdaiki/stock-web", "price_source": "Songdaiki/stock-web", "raw_component_score_breakdown": {"bottleneck_pricing": 17, "capital_allocation": 8, "earnings_visibility": 18, "eps_fcf_explosion": 17, "information_confidence": 16, "market_mispricing": 11, "valuation_rerating": 11}, "raw_total_score": 98, "residual_label": "cement_price_pass_through_needs_volume_cost_cash_second_bridge", "result_file": "e2r_stock_web_v12_residual_round_R4_loop_194_L4_MATERIALS_SPREAD_RESOURCE_C15_MATERIAL_SPREAD_SUPERCYCLE_research.md", "reuse_reason": "same canonical, new cement/fuel-price trigger family; no same ticker+trigger+entry duplication in this session", "role": "positive_structural_success", "row_type": "trigger", "same_entry_group_id": "C15_CEMENT_300720_2024-03-25_Stage2-Actionable", "selected_loop": 194, "selected_round": "R4", "stock_web_profile": "atlas/symbol_profiles/300/300720.json", "stock_web_shard": "atlas/ohlcv_tradable_by_symbol_year/300/300720/2024.csv", "symbol": "300720", "trigger_date": "2024-03-25", "trigger_type": "Stage2-Actionable", "trough_180D_date": "2024-04-05", "trough_30D_date": "2024-04-05", "trough_90D_date": "2024-04-05"}
{"MAE_180D_pct": -12.72, "MAE_30D_pct": -2.47, "MAE_90D_pct": -10.53, "MFE_180D_pct": 14.59, "MFE_30D_pct": 3.93, "MFE_90D_pct": 14.59, "aggregate_group_role": "representative", "calibration_usable": true, "canonical_archetype_id": "C15_MATERIAL_SPREAD_SUPERCYCLE", "case_id": "C15_CEMENT_06_006390_2024-03-25_Stage4B", "case_role": "shipment_decline_and_cost_ratio_watch", "company_name": "Hanil Hyundai Cement", "corporate_action_window_status": "not_contaminated", "current_profile_error_type": "green_blocker_or_4c_stickiness_risk", "current_profile_expected_label": "capped_stage2_or_4b_watch", "dedupe_for_aggregate": true, "do_not_count_as_new_case": false, "entry_amount": 86638510.0, "entry_close": 15010.0, "entry_date": "2024-03-25", "entry_high": 15120.0, "entry_low": 14950.0, "entry_market_cap": 290108356720.0, "entry_open": 14950.0, "entry_price": 15010.0, "evidence_date": "2024-03-25", "evidence_summary": "Hanil Cement coverage noted Hanil Hyundai Cement shipment decline partly offset group earnings and thermal-coal cost ratio rose near year-end; the direct bridge is a watch, not a thesis-break.", "evidence_urls": ["https://www.asiae.co.kr/en/article/2024032507455089335"], "fine_archetype_id": "C15_CEMENT_COAL_POWER_PRICE_PASS_THROUGH_SPREAD_REPAIR", "forward_window_trading_days": 180, "independent_evidence_weight": 1.0, "large_sector_id": "L4_MATERIALS_SPREAD_RESOURCE", "market": "KOSPI", "peak_180D_date": "2024-06-07", "peak_30D_date": "2024-04-09", "peak_90D_date": "2024-06-07", "price_adjustment_status": "raw_unadjusted_marcap", "price_basis": "tradable_raw", "price_data_source": "Songdaiki/stock-web", "price_source": "Songdaiki/stock-web", "raw_component_score_breakdown": {"bottleneck_pricing": 12, "capital_allocation": 4, "earnings_visibility": 9, "eps_fcf_explosion": 8, "information_confidence": 12, "market_mispricing": 7, "valuation_rerating": 6}, "raw_total_score": 58, "residual_label": "cement_price_pass_through_needs_volume_cost_cash_second_bridge", "result_file": "e2r_stock_web_v12_residual_round_R4_loop_194_L4_MATERIALS_SPREAD_RESOURCE_C15_MATERIAL_SPREAD_SUPERCYCLE_research.md", "reuse_reason": "same canonical, new cement/fuel-price trigger family; no same ticker+trigger+entry duplication in this session", "role": "counterexample_or_guardrail", "row_type": "trigger", "same_entry_group_id": "C15_CEMENT_006390_2024-03-25_Stage4B", "selected_loop": 194, "selected_round": "R4", "stock_web_profile": "atlas/symbol_profiles/006/006390.json", "stock_web_shard": "atlas/ohlcv_tradable_by_symbol_year/006/006390/2024.csv", "symbol": "006390", "trigger_date": "2024-03-25", "trigger_type": "Stage4B", "trough_180D_date": "2024-12-09", "trough_30D_date": "2024-04-17", "trough_90D_date": "2024-08-05"}
{"MAE_180D_pct": -2.72, "MAE_30D_pct": -1.02, "MAE_90D_pct": -2.72, "MFE_180D_pct": 22.58, "MFE_30D_pct": 18.85, "MFE_90D_pct": 20.88, "aggregate_group_role": "representative", "calibration_usable": true, "canonical_archetype_id": "C15_MATERIAL_SPREAD_SUPERCYCLE", "case_id": "C15_CEMENT_07_038500_2024-12-30_Stage4B", "case_role": "demand_decline_sales_drop_but_not_hard_4c", "company_name": "Sampyo Cement", "corporate_action_window_status": "not_contaminated", "current_profile_error_type": "green_blocker_or_4c_stickiness_risk", "current_profile_expected_label": "capped_stage2_or_4b_watch", "dedupe_for_aggregate": true, "do_not_count_as_new_case": false, "entry_amount": 429040735.0, "entry_close": 2945.0, "entry_date": "2024-12-30", "entry_high": 2985.0, "entry_low": 2940.0, "entry_market_cap": 317813521170.0, "entry_open": 2970.0, "entry_price": 2945.0, "evidence_date": "2024-12-30", "evidence_summary": "CemNet reported Q3 2024 cement-sector downturn: Sampyo Cement sales fell 4.5%, with domestic demand weakening and electricity costs rising.", "evidence_urls": ["https://www.cemnet.com/News/story/178382/south-korea-cement-industry-boosts-use-of-alternative-fuels-as-demand-declines.html"], "fine_archetype_id": "C15_CEMENT_COAL_POWER_PRICE_PASS_THROUGH_SPREAD_REPAIR", "forward_window_trading_days": 180, "independent_evidence_weight": 1.0, "large_sector_id": "L4_MATERIALS_SPREAD_RESOURCE", "market": "KOSDAQ", "peak_180D_date": "2025-08-05", "peak_30D_date": "2025-01-14", "peak_90D_date": "2025-04-22", "price_adjustment_status": "raw_unadjusted_marcap", "price_basis": "tradable_raw", "price_data_source": "Songdaiki/stock-web", "price_source": "Songdaiki/stock-web", "raw_component_score_breakdown": {"bottleneck_pricing": 10, "capital_allocation": 4, "earnings_visibility": 8, "eps_fcf_explosion": 7, "information_confidence": 14, "market_mispricing": 7, "valuation_rerating": 6}, "raw_total_score": 56, "residual_label": "cement_price_pass_through_needs_volume_cost_cash_second_bridge", "result_file": "e2r_stock_web_v12_residual_round_R4_loop_194_L4_MATERIALS_SPREAD_RESOURCE_C15_MATERIAL_SPREAD_SUPERCYCLE_research.md", "reuse_reason": "same canonical, new cement/fuel-price trigger family; no same ticker+trigger+entry duplication in this session", "role": "counterexample_or_guardrail", "row_type": "trigger", "same_entry_group_id": "C15_CEMENT_038500_2024-12-30_Stage4B", "selected_loop": 194, "selected_round": "R4", "stock_web_profile": "atlas/symbol_profiles/038/038500.json", "stock_web_shard": "atlas/ohlcv_tradable_by_symbol_year/038/038500/2024.csv", "symbol": "038500", "trigger_date": "2024-12-30", "trigger_type": "Stage4B", "trough_180D_date": "2025-04-07", "trough_30D_date": "2025-01-06", "trough_90D_date": "2025-04-07"}
{"MAE_180D_pct": -1.31, "MAE_30D_pct": -1.31, "MAE_90D_pct": -1.31, "MFE_180D_pct": 50.83, "MFE_30D_pct": 13.64, "MFE_90D_pct": 30.17, "aggregate_group_role": "representative", "calibration_usable": true, "canonical_archetype_id": "C15_MATERIAL_SPREAD_SUPERCYCLE", "case_id": "C15_CEMENT_08_300720_2024-12-30_Stage4B", "case_role": "volume_demand_decline_offset_test", "company_name": "Hanil Cement", "corporate_action_window_status": "not_contaminated", "current_profile_error_type": "green_blocker_or_4c_stickiness_risk", "current_profile_expected_label": "capped_stage2_or_4b_watch", "dedupe_for_aggregate": true, "do_not_count_as_new_case": false, "entry_amount": 1667127160.0, "entry_close": 14520.0, "entry_date": "2024-12-30", "entry_high": 14940.0, "entry_low": 14410.0, "entry_market_cap": 1005677560800.0, "entry_open": 14940.0, "entry_price": 14520.0, "evidence_date": "2024-12-30", "evidence_summary": "CemNet reported Hanil Cement Q3 2024 sales fell 8.3%; this is a demand/volume watch row that should not auto-trigger hard 4C while pricing/cash bridge may survive.", "evidence_urls": ["https://www.cemnet.com/News/story/178382/south-korea-cement-industry-boosts-use-of-alternative-fuels-as-demand-declines.html"], "fine_archetype_id": "C15_CEMENT_COAL_POWER_PRICE_PASS_THROUGH_SPREAD_REPAIR", "forward_window_trading_days": 180, "independent_evidence_weight": 1.0, "large_sector_id": "L4_MATERIALS_SPREAD_RESOURCE", "market": "KOSPI", "peak_180D_date": "2025-07-18", "peak_30D_date": "2025-02-17", "peak_90D_date": "2025-04-22", "price_adjustment_status": "raw_unadjusted_marcap", "price_basis": "tradable_raw", "price_data_source": "Songdaiki/stock-web", "price_source": "Songdaiki/stock-web", "raw_component_score_breakdown": {"bottleneck_pricing": 12, "capital_allocation": 6, "earnings_visibility": 10, "eps_fcf_explosion": 8, "information_confidence": 14, "market_mispricing": 8, "valuation_rerating": 7}, "raw_total_score": 65, "residual_label": "cement_price_pass_through_needs_volume_cost_cash_second_bridge", "result_file": "e2r_stock_web_v12_residual_round_R4_loop_194_L4_MATERIALS_SPREAD_RESOURCE_C15_MATERIAL_SPREAD_SUPERCYCLE_research.md", "reuse_reason": "same canonical, new cement/fuel-price trigger family; no same ticker+trigger+entry duplication in this session", "role": "counterexample_or_guardrail", "row_type": "trigger", "same_entry_group_id": "C15_CEMENT_300720_2024-12-30_Stage4B", "selected_loop": 194, "selected_round": "R4", "stock_web_profile": "atlas/symbol_profiles/300/300720.json", "stock_web_shard": "atlas/ohlcv_tradable_by_symbol_year/300/300720/2024.csv", "symbol": "300720", "trigger_date": "2024-12-30", "trigger_type": "Stage4B", "trough_180D_date": "2025-01-02", "trough_30D_date": "2025-01-02", "trough_90D_date": "2025-01-02"}
{"MAE_180D_pct": -5.06, "MAE_30D_pct": -2.63, "MAE_90D_pct": -5.06, "MFE_180D_pct": 52.72, "MFE_30D_pct": 5.54, "MFE_90D_pct": 12.26, "aggregate_group_role": "representative", "calibration_usable": true, "canonical_archetype_id": "C15_MATERIAL_SPREAD_SUPERCYCLE", "case_id": "C15_CEMENT_09_183190_2024-12-30_Stage4B", "case_role": "largest_sales_drop_but_forward_rebound", "company_name": "Asia Cement", "corporate_action_window_status": "not_contaminated", "current_profile_error_type": "green_blocker_or_4c_stickiness_risk", "current_profile_expected_label": "capped_stage2_or_4b_watch", "dedupe_for_aggregate": true, "do_not_count_as_new_case": false, "entry_amount": 205043120.0, "entry_close": 10280.0, "entry_date": "2024-12-30", "entry_high": 10400.0, "entry_low": 10270.0, "entry_market_cap": 388959076080.0, "entry_open": 10370.0, "entry_price": 10280.0, "evidence_date": "2024-12-30", "evidence_summary": "CemNet reported Asia Cement Q3 2024 sales fell 14.7%; the forward path is a holdout against sticky hard 4C without cashflow/order collapse.", "evidence_urls": ["https://www.cemnet.com/News/story/178382/south-korea-cement-industry-boosts-use-of-alternative-fuels-as-demand-declines.html"], "fine_archetype_id": "C15_CEMENT_COAL_POWER_PRICE_PASS_THROUGH_SPREAD_REPAIR", "forward_window_trading_days": 180, "independent_evidence_weight": 1.0, "large_sector_id": "L4_MATERIALS_SPREAD_RESOURCE", "market": "KOSPI", "peak_180D_date": "2025-08-05", "peak_30D_date": "2025-01-21", "peak_90D_date": "2025-05-19", "price_adjustment_status": "raw_unadjusted_marcap", "price_basis": "tradable_raw", "price_data_source": "Songdaiki/stock-web", "price_source": "Songdaiki/stock-web", "raw_component_score_breakdown": {"bottleneck_pricing": 10, "capital_allocation": 4, "earnings_visibility": 8, "eps_fcf_explosion": 7, "information_confidence": 14, "market_mispricing": 7, "valuation_rerating": 6}, "raw_total_score": 56, "residual_label": "cement_price_pass_through_needs_volume_cost_cash_second_bridge", "result_file": "e2r_stock_web_v12_residual_round_R4_loop_194_L4_MATERIALS_SPREAD_RESOURCE_C15_MATERIAL_SPREAD_SUPERCYCLE_research.md", "reuse_reason": "same canonical, new cement/fuel-price trigger family; no same ticker+trigger+entry duplication in this session", "role": "counterexample_or_guardrail", "row_type": "trigger", "same_entry_group_id": "C15_CEMENT_183190_2024-12-30_Stage4B", "selected_loop": 194, "selected_round": "R4", "stock_web_profile": "atlas/symbol_profiles/183/183190.json", "stock_web_shard": "atlas/ohlcv_tradable_by_symbol_year/183/183190/2024.csv", "symbol": "183190", "trigger_date": "2024-12-30", "trigger_type": "Stage4B", "trough_180D_date": "2025-04-07", "trough_30D_date": "2025-02-12", "trough_90D_date": "2025-04-07"}
```

## 9. Aggregate row

```json
{
  "row_type": "aggregate",
  "result_file": "e2r_stock_web_v12_residual_round_R4_loop_194_L4_MATERIALS_SPREAD_RESOURCE_C15_MATERIAL_SPREAD_SUPERCYCLE_research.md",
  "selected_round": "R4",
  "selected_loop": 194,
  "large_sector_id": "L4_MATERIALS_SPREAD_RESOURCE",
  "canonical_archetype_id": "C15_MATERIAL_SPREAD_SUPERCYCLE",
  "fine_archetype_id": "C15_CEMENT_COAL_POWER_PRICE_PASS_THROUGH_SPREAD_REPAIR",
  "new_independent_case_count": 9,
  "reused_case_count": 0,
  "new_symbol_count": 5,
  "new_trigger_family_count": 3,
  "positive_case_count": 2,
  "counterexample_count": 7,
  "current_profile_error_count": 9,
  "calibration_usable_trigger_count": 9,
  "loop_contribution_label": "canonical_archetype_rule_candidate",
  "do_not_propose_new_weight_delta": false,
  "production_scoring_changed": false,
  "shadow_weight_only": true
}
```

## 10. Shadow weight row

```json
{
  "row_type": "shadow_weight",
  "large_sector_id": "L4_MATERIALS_SPREAD_RESOURCE",
  "canonical_archetype_id": "C15_MATERIAL_SPREAD_SUPERCYCLE",
  "fine_archetype_id": "C15_CEMENT_COAL_POWER_PRICE_PASS_THROUGH_SPREAD_REPAIR",
  "rule_candidate": "C15_CEMENT_PRICE_PASS_THROUGH_VOLUME_COST_CASHFLOW_GATE",
  "axis": "stage2_required_bridge",
  "direction": "strengthen_stage2_actionable_second_bridge; keep_green_strict; avoid_sticky_hard_4c_on_demand_headline",
  "max_shadow_delta": 1.0,
  "reason": "Cement pass-through rows split cleanly between sector-proxy headlines with weak forward path and issuer-level profit/cash bridge rows with better forward path.",
  "production_scoring_changed": false,
  "shadow_weight_only": true
}
```

## 11. Batch ingest self-audit

```text
filename_matches_standard_v12_pattern: true
metadata_round_loop_matches_filename: true
row_type_trigger_only_for_usable_rows: true
trigger_type_canonical_stage_label: true
entry_date_present_all_rows: true
entry_price_positive_all_rows: true
price_source_songdaiki_stock_web_all_rows: true
price_basis_tradable_raw_all_rows: true
price_adjustment_status_raw_unadjusted_all_rows: true
forward_window_trading_days_180_all_rows: true
MFE_MAE_30_90_180_present_all_rows: true
large_sector_id_present_all_rows: true
canonical_archetype_id_present_all_rows: true
corporate_action_window_status_not_contaminated_all_rows: true
same_entry_group_id_present_all_rows: true
dedupe_for_aggregate_present_all_rows: true
aggregate_group_role_present_all_rows: true
calibration_usable_true_all_rows: true
ready_for_batch_ingest: true
```

## 12. Deferred Coding Agent Handoff Prompt

```text
Do not execute in this research session.

When batch-applying v12 research, parse this MD as a standard v12 result file.
Use only row_type="trigger" rows with calibration_usable=true and corporate_action_window_status="not_contaminated".
Treat C15_CEMENT_PRICE_PASS_THROUGH_VOLUME_COST_CASHFLOW_GATE as a shadow candidate, not an immediate production change.
Compare against existing C15 rules for spread persistence, inventory gain, and hard 4C offset checks.
If adopted, scope the patch to C15 / L4 cement price-pass-through rows only.
Do not loosen Stage3-Green. Strengthen the Stage2-Actionable bridge and hard-4C issuer-level thesis-break requirement.
```

## 13. Next Research State

```text
completed_round: R4
completed_loop: 194
selection_basis: docs/core/V12_Research_No_Repeat_Index.md
selected_priority_bucket: Priority 1 balance reinforcement / URL-proxy quality repair
round_schedule_status: coverage_index_selected
round_sector_consistency: pass

next_recommended_archetypes:
- C05_EPC_MEGA_CONTRACT_MARGIN_GAP_WORKING_CAPITAL_CASHFLOW_ONLY_REPAIR
- C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE_SUPPLIER_ORDER_DIRECT_URL_REPAIR
- C13_BATTERY_JV_UTILIZATION_AMPC_IRA_EX_SUBSIDY_MARGIN_DIRECT_REPAIR
- C16_STRATEGIC_RESOURCE_POLICY_SUPPLY_DIRECT_OFFTAKE_POSITIVE_CONTROL_REPAIR
- R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL_HOLDOUT_REFRESH
```
