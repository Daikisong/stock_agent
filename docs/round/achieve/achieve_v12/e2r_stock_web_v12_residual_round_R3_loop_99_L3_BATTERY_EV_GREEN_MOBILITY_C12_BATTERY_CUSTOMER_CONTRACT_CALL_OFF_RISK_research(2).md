# E2R Stock-Web v12 Residual Research — R3 loop 99 / L3 / C12

```yaml
schema_family: v12_sector_archetype_residual
research_session: post_calibrated_sector_archetype_residual_research
mode: historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12
selected_round: R3
selected_loop: 99
large_sector_id: L3_BATTERY_EV_GREEN_MOBILITY
canonical_archetype_id: C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK
fine_archetype_id: C12_CUSTOMER_CONTRACT_CALLOFF_UTILIZATION_MARGIN_FCF_BRIDGE
deep_sub_archetype_id: C12_DEEP_CELL_CATHODE_SEPARATOR_ELECTROLYTE_CUSTOMER_PULL_VS_CONTRACT_HEADLINE
selected_priority_bucket: Priority 1
selection_basis: docs/core/V12_Research_No_Repeat_Index.md
round_schedule_status: coverage_index_selected
round_sector_consistency: pass
production_scoring_changed: false
shadow_weight_only: true
handoff_prompt_embedded: true
handoff_prompt_executed_now: false
price_data_source: Songdaiki/stock-web
upstream_source: FinanceData/marcap
price_basis: tradable_raw
price_adjustment_status: raw_unadjusted_marcap
stock_web_manifest_max_date: 2026-02-20
```

## 1. Executive Summary

This loop adds **7 calibration-usable C12 trigger rows**, including **3 hard-4C positive protection paths**, **4 counterexamples/residual errors**, and **1 false-hard-4C exception** for `R3 / L3_BATTERY_EV_GREEN_MOBILITY / C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK`.

C12 is the customer-contract and call-off bucket. A supply agreement, JV capacity, or customer label is not the same as actual customer pull. The conveyor only matters if the customer keeps pulling units, utilization holds, inventory normalizes, ASP/mix survive, and the path reaches margin / FCF / revision. This loop therefore separates three states:

1. **Contract headline without margin/FCF bridge** → Stage2-Watch or blocked Yellow.
2. **Confirmed utilization / customer-pull / margin break** → hard Stage4C.
3. **Growth-exception or recovery path without non-price call-off break** → local Stage4B watch, not hard Stage4C.

## 2. Coverage-Index Selection

- `V12_Research_No_Repeat_Index.md` places C12 in Priority 1 with 32 rows and 18 more rows needed to reach the 50-row practical calibration zone.
- In this session, Priority 0 canonical buckets C02, C09, C14, C10, C06, C07, C11, C01 and C28 were already covered once. The next coverage-first target is therefore the first Priority 1 bucket, `C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK`.
- Existing visible C12 file is `c12_r3_loop98_battery_customer_contract_calloff_risk_23afca31.md`; this output uses the standard v12 filename and `selected_loop=99`.
- Hard duplicate key avoided: `canonical_archetype_id + symbol + trigger_type + entry_date`.
- Prior C12 loop 98 used mostly 2024 C12 compact rows with noncanonical trigger-family labels and compact MFE/MAE aliases. This loop writes canonical `Stage2-Actionable`, `Stage4B`, `Stage4C` rows with full 30/90/180 MFE/MAE fields.

## 3. Price Source Validation

```json
{"row_type":"price_source_validation","price_atlas_repo":"Songdaiki/stock-web","manifest":"atlas/manifest.json","source_name":"FinanceData/marcap","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","calibration_shard_root":"atlas/ohlcv_tradable_by_symbol_year","manifest_max_date":"2026-02-20","notes":"Raw/unadjusted OHLC. Zero-volume and invalid rows are excluded from calibration shards. Corporate-action-contaminated windows are blocked by default."}
```

| symbol | profile path | selected shard(s) | corporate-action status |
|---|---|---|---|
| 373220 | atlas/symbol_profiles/373/373220.json | atlas/ohlcv_tradable_by_symbol_year/373/373220/2023.csv | no corporate action candidates |
| 006400 | atlas/symbol_profiles/006/006400.json | atlas/ohlcv_tradable_by_symbol_year/006/006400/2023.csv | old candidates only; no selected-window overlap |
| 247540 | atlas/symbol_profiles/247/247540.json | atlas/ohlcv_tradable_by_symbol_year/247/247540/2023.csv | 2022 candidates only; no selected-window overlap |
| 361610 | atlas/symbol_profiles/361/361610.json | atlas/ohlcv_tradable_by_symbol_year/361/361610/2024.csv | no corporate action candidates |
| 278280 | atlas/symbol_profiles/278/278280.json | atlas/ohlcv_tradable_by_symbol_year/278/278280/2024.csv | no corporate action candidates |
| 005070 | atlas/symbol_profiles/005/005070.json | atlas/ohlcv_tradable_by_symbol_year/005/005070/2024.csv | old candidates only through 2019; no selected-window overlap |
| 348370 | atlas/symbol_profiles/348/348370.json | atlas/ohlcv_tradable_by_symbol_year/348/348370/2024.csv | no corporate action candidates |

## 4. Evidence Source Map

| symbol | evidence family | source quality | C12 interpretation |
|---|---|---|---|
| 373220 | Toyota 20GWh LGES supply agreement | source URLs present | direct customer-contract evidence, but margin/FCF bridge missing |
| 006400 | GM/Samsung SDI JV capacity | source URLs present | parent-level capacity proxy; must not substitute for listed-parent customer pull |
| 247540 | Samsung SDI cathode supply contract | source URLs present | large contract size after cycle peak; needs call-off, inventory and margin validation |
| 361610 | separator utilization/call-off break proxy | source proxy pending | hard-4C positive path once non-price call-off/utilization break is verified |
| 278280 | electrolyte customer-pull/margin break proxy | source proxy pending | hard-4C positive path |
| 005070 | cathode-material customer-demand/margin reset proxy | source proxy pending | hard-4C positive path |
| 348370 | electrolyte growth exception / false-hard-4C proxy | source proxy pending | broad call-off guard must not force hard 4C without thesis-break proof |

## 5. Case-by-Case Trigger Grid

| case_id | symbol | company | role | trigger_type | entry_date | entry_price | MFE30 | MAE30 | MFE90 | MAE90 | MFE180 | MAE180 | verdict |
|---|---|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| C12_373220_2023-10-06_STAGE2_LGES_TOYOTA_CONTRACT_CAPEX_DRAG | 373220 | LG Energy Solution / LG에너지솔루션 | counterexample | Stage2-Actionable | 2023-10-06 | 464000 | 7.97 | -19.07 | 7.97 | -21.98 | 7.97 | -30.5 | current_profile_false_positive_if_customer_volume_contract_overrides_margin_fcf_bridge |
| C12_006400_2023-04-27_STAGE2_SDI_GM_JV_PARENT_CALL_OFF_GUARD | 006400 | Samsung SDI / 삼성SDI | counterexample | Stage2-Actionable | 2023-04-27 | 706000 | 5.52 | -7.22 | 5.52 | -17.42 | 5.52 | -49.86 | current_profile_false_positive_if_JV_capacity_counts_as_customer_pull_without_parent_margin_bridge |
| C12_247540_2023-12-04_STAGE2_ECOPROBM_SDI_CONTRACT_LATE_CYCLE | 247540 | EcoPro BM / 에코프로비엠 | counterexample | Stage2-Actionable | 2023-12-04 | 323000 | 9.6 | -17.96 | 9.6 | -34.67 | 9.6 | -49.23 | current_profile_false_positive_if_large_customer_contract_size_promotes_yellow_after_cycle_peak |
| C12_361610_2024-03-25_STAGE4C_SEPARATOR_CUSTOMER_CALLOFF_UTILIZATION_BREAK | 361610 | SK아이이테크놀로지 | 4C_success | Stage4C | 2024-03-25 | 76300 | 1.83 | -23.59 | 1.83 | -59.44 | 1.83 | -70.31 | current_profile_correct_if_hard_4c_requires_utilization_calloff_margin_break |
| C12_278280_2024-03-25_STAGE4C_ELECTROLYTE_CUSTOMER_PULL_MARGIN_BREAK | 278280 | 천보 | 4C_success | Stage4C | 2024-03-25 | 89100 | 1.8 | -13.92 | 1.8 | -45.01 | 1.8 | -57.58 | current_profile_correct_if_hard_4c_requires_customer_pull_margin_break |
| C12_005070_2024-03-25_STAGE4C_CATHODE_CUSTOMER_PULL_MARGIN_RESET | 005070 | 코스모신소재 | 4C_success | Stage4C | 2024-03-25 | 171300 | 2.51 | -17.69 | 2.51 | -41.56 | 2.51 | -69.64 | current_profile_correct_if_hard_4c_requires_customer_pull_margin_break |
| C12_348370_2024-01-22_STAGE4B_ELECTROLYTE_FALSE_HARD_4C_EXCEPTION | 348370 | 엔켐 | 4B_too_early_or_false_4c_counterexample | Stage4B | 2024-01-22 | 103400 | 246.71 | -3.09 | 246.71 | -3.09 | 246.71 | -3.09 | current_profile_false_positive_if_broad_calloff_guard_routes_growth_exception_to_hard_4c |

## 6. Trigger-Level OHLC Backtest Tables

| case_id | symbol | entry_date | entry_price | peak_180D | peak_date | trough_180D | trough_date | drawdown_after_peak_180D | profile CA status |
|---|---|---:|---:|---:|---|---:|---|---:|---|
| C12_373220_2023-10-06_STAGE2_LGES_TOYOTA_CONTRACT_CAPEX_DRAG | 373220 | 2023-10-06 | 464000 | 501000 | 2023-10-12 | 322500 | 2024-06-28 | -35.63 | clean_180D_window |
| C12_006400_2023-04-27_STAGE2_SDI_GM_JV_PARENT_CALL_OFF_GUARD | 006400 | 2023-04-27 | 706000 | 745000 | 2023-06-12 | 354000 | 2024-01-23 | -52.48 | clean_180D_window_old_candidates_only |
| C12_247540_2023-12-04_STAGE2_ECOPROBM_SDI_CONTRACT_LATE_CYCLE | 247540 | 2023-12-04 | 323000 | 354000 | 2023-12-04 | 164000 | 2024-08-05 | -53.67 | clean_180D_window_old_candidates_only |
| C12_361610_2024-03-25_STAGE4C_SEPARATOR_CUSTOMER_CALLOFF_UTILIZATION_BREAK | 361610 | 2024-03-25 | 76300 | 77700 | 2024-03-26 | 22650 | 2024-12-09 | -70.85 | clean_180D_window |
| C12_278280_2024-03-25_STAGE4C_ELECTROLYTE_CUSTOMER_PULL_MARGIN_BREAK | 278280 | 2024-03-25 | 89100 | 90700 | 2024-03-25 | 37800 | 2024-12-09 | -58.32 | clean_180D_window |
| C12_005070_2024-03-25_STAGE4C_CATHODE_CUSTOMER_PULL_MARGIN_RESET | 005070 | 2024-03-25 | 171300 | 175600 | 2024-03-25 | 52000 | 2024-12-09 | -70.39 | clean_180D_window_old_candidates_only |
| C12_348370_2024-01-22_STAGE4B_ELECTROLYTE_FALSE_HARD_4C_EXCEPTION | 348370 | 2024-01-22 | 103400 | 358500 | 2024-02-21 | 100200 | 2024-01-22 | -72.05 | clean_180D_window |

## 7. Current Calibrated Profile Stress Test

### 7.1 Residual false positives: contract label is not customer pull

`373220`, `006400`, and `247540` stress the same mechanism. Public customer/JV/contract evidence was real, but the price path punished entries that treated contract vocabulary as a completed rerating bridge. The current profile can still be too generous if it allows customer contract size, JV capacity, or OEM name quality to substitute for margin, FCF, working capital and revision evidence.

### 7.2 Hard-4C positives: call-off/utilization/margin break should protect capital

`361610`, `278280`, and `005070` show tiny MFE and deep 90D/180D MAE from selected hard-4C entries. These are useful because they are not just “battery stocks went down.” They map to the C12 thesis break: customer pull fails, utilization weakens, inventory/margin pressure dominates, and the contract label no longer protects the stock.

### 7.3 False-hard-4C exception: growth exception filter is required

`348370` is the guardrail against an overbroad C12 rule. A battery downcycle or generic customer call-off fear would have been catastrophically wrong if routed directly to hard 4C without non-price thesis-break evidence. The row produced +246.71% MFE from the selected entry. C12 therefore needs a two-key lock: hard 4C requires a customer-pull/utilization/margin break, while growth-exception evidence can keep the row at local 4B watch until the thesis break is proven.

## 8. Stage2 / Yellow / Green Comparison

| state | current failure mode | C12 repair |
|---|---|---|
| Stage2-Actionable | customer/JV/contract evidence creates Actionable label but no shipment cadence or margin bridge | allow Stage2-Watch / Actionable only; block Yellow until customer pull and margin/FCF bridge appear |
| Stage3-Yellow | contract size or OEM quality pushes score above 75 despite cycle/MAE risk | require at least two non-price bridge confirmations: shipment/call-off + margin/revision/FCF |
| Stage3-Green | should remain rare in C12 | do not loosen Green; require durable customer confirmation, low inventory risk, margin visibility and revision |
| Stage4B | price blowoff or local overheating appears but thesis not broken | local watch only; do not call full 4B without non-price deterioration |
| Stage4C | customer call-off/utilization/margin break is confirmed | route to hard 4C |

## 9. 4B Local vs Full-window Timing Audit

| symbol | entry | local 4B/full 4B implication | audit result |
|---|---|---|---|
| 348370 | 2024-01-22 Stage4B | broad C12 fear would have routed too early to hard 4C | local Stage4B watch only; hard 4C blocked by growth-exception filter |
| 247540 | 2023-12-04 Stage2-Actionable | contract-size excitement after cycle peak should have carried late-cycle 4B guard | Stage2-Watch or guarded Actionable; not Yellow |
| 361610/278280/005070 | 2024-03-25 Stage4C | not a price-only 4B; severe path supports thesis-break protection | hard 4C confirmed when non-price break is verified |

## 10. 4C Protection Audit

C12 hard 4C should be routed only when the following are present together:

- customer call-off or order cut / pull failure,
- utilization or shipment cadence deterioration,
- inventory, ASP, margin, working capital, FCF, or revision break,
- no credible growth-exception path that keeps the customer contract thesis alive.

This loop supports hard 4C for `361610`, `278280`, and `005070`, but blocks hard 4C for `348370` unless a non-price customer-pull thesis break is proven.

## 11. Sector-Specific Rule Candidate

```text
rule_id = L3_C12_customer_contract_requires_pull_margin_fcf_bridge
scope = L3_BATTERY_EV_GREEN_MOBILITY / C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK
action = tighten Stage2-Actionable -> Yellow promotion when customer-contract evidence lacks shipment cadence, utilization, margin, working-capital, FCF or revision bridge
positive_guard = do not route generic battery weakness to hard 4C if growth-exception or customer expansion evidence is still alive
```

## 12. Canonical-Archetype Rule Candidate

```text
new_axis_proposed = C12_customer_pull_utilization_margin_fcf_bridge_required_before_Yellow_or_Green_plus_growth_exception_filter_before_hard_4C
existing_axis_strengthened = stage2_required_bridge, hard_4c_confirmation, local_4b_watch_guard, full_4b_requires_non_price_evidence
existing_axis_weakened = null
```

## 13. Before / After Backtest Comparison

| group | current proxy behavior | candidate C12 behavior | expected calibration effect |
|---|---|---|---|
| customer contract headline | may over-promote to Yellow | require customer pull + margin/FCF bridge | lower false-positive rate |
| JV/capacity parent proxy | may count as backlog | treat as parent-level proxy until listed-parent margin path proves out | reduce high-MAE Stage2 entries |
| hard call-off/utilization break | may remain 4B/watch too long | route to hard 4C with non-price confirmation | improve protection |
| electrolyte growth exception | may be crushed by broad EV downcycle guard | block hard 4C until thesis break is proven | reduce false hard-4C exits |

## 14. Score-Return Alignment Matrix

| symbol | current proxy score/stage | candidate C12 stage | MFE180 | MAE180 | alignment |
|---|---|---|---:|---:|---|
| 373220 | 77 / Stage3-Yellow | Stage2-Watch | 7.97 | -30.50 | candidate better |
| 006400 | 75 / Stage3-Yellow | Stage2-Watch | 5.52 | -49.86 | candidate better |
| 247540 | 79 / Stage3-Yellow | Stage2-Watch / local 4B guard | 9.60 | -49.23 | candidate better |
| 361610 | 39 / watch | Stage4C | 1.83 | -70.31 | candidate better |
| 278280 | 42 / watch | Stage4C | 1.80 | -57.58 | candidate better |
| 005070 | 44 / watch | Stage4C | 2.51 | -69.64 | candidate better |
| 348370 | 25 / hard-4C if overbroad | local Stage4B watch | 246.71 | -3.09 | candidate better |

## 15. Coverage Matrix

```text
selected_priority_bucket = Priority 1
C12 current rows in No-Repeat Index = 32
this loop representative trigger rows = 7
estimated C12 rows after adding this loop = 39
need to 50 after this loop = 11
new C12 symbols from this loop = 4
new trigger families = 7
positive/counterexample balance = 3/4
4B/4C rows = 1/3
```

## 16. Residual Contribution Summary

This loop adds **7** new independent C12 cases, **4** counterexamples, and **4** current-profile residual errors for `R3 / L3_BATTERY_EV_GREEN_MOBILITY / C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK`.

```text
loop_contribution_label = canonical_archetype_rule_candidate
do_not_propose_new_weight_delta = false
sector_specific_rule_candidate = true
canonical_archetype_rule_candidate = true
```

## 17. Validation Scope / Non-Validation Scope

Validation scope:

- Historical trigger-level calibration only.
- Songdaiki/stock-web 1D OHLCV rows.
- `tradable_raw` / `raw_unadjusted_marcap` basis.
- Entry-date forward 30/90/180D MFE/MAE.
- Clean 180D corporate-action windows.
- Current calibrated profile stress test.

Non-validation scope:

- No current/live stock recommendation.
- No production scoring patch.
- No live scan.
- No brokerage/API/auto-trading logic.
- No green unlock from outcome hindsight.

## 18. Shadow Weight Calibration

```text
scope = canonical_archetype_specific
canonical_archetype_id = C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK
candidate_delta_when_customer_contract_without_pull_margin_fcf_bridge = -8 to -14 score points
candidate_stage_effect = block Stage3-Yellow / Stage3-Green; keep Stage2-Watch or guarded Stage2-Actionable
candidate_4c_effect = require non-price customer-pull/utilization/margin thesis break before hard 4C
candidate_exception = if growth-exception evidence exists, route to local 4B watch instead of hard 4C
```

## 19. Machine-Readable Rows

```jsonl
{"row_id": "R3L99-C12-001", "case_id": "C12_373220_2023-10-06_STAGE2_LGES_TOYOTA_CONTRACT_CAPEX_DRAG", "symbol": "373220", "company_name": "LG Energy Solution / LG에너지솔루션", "trigger_type": "Stage2-Actionable", "trigger_family": "cell_customer_contract_without_margin_fcf_bridge", "trigger_date": "2023-10-05", "entry_date": "2023-10-06", "entry_price": 464000.0, "MFE_30D_pct": 7.97, "MAE_30D_pct": -19.07, "MFE_90D_pct": 7.97, "MAE_90D_pct": -21.98, "MFE_180D_pct": 7.97, "MAE_180D_pct": -30.5, "MFE_250D_pct": 7.97, "MAE_250D_pct": -32.97, "MFE_500D_pct": 13.58, "MAE_500D_pct": -42.67, "peak_date_180D": "2023-10-12", "peak_price_180D": 501000.0, "trough_date_180D": "2024-06-28", "trough_price_180D": 322500.0, "drawdown_after_peak_180D_pct": -35.63, "case_role": "counterexample", "outcome_label": "counterexample_customer_volume_contract_not_margin_fcf_bridge", "current_profile_error": true, "current_profile_verdict": "current_profile_false_positive_if_customer_volume_contract_overrides_margin_fcf_bridge", "baseline_profile_decision": "Stage2-Actionable / Yellow if global OEM customer contract is overweighted", "proposed_profile_decision": "Stage2-Watch or Actionable only; Yellow requires shipment cadence, margin/revision and FCF bridge", "evidence_summary": "LGES announced a long-term Toyota supply agreement for annual 20GWh starting 2025. The contract was real customer visibility, but the forward stock path shows that volume-contract evidence without operating-margin/FCF bridge can still become a high-MAE C12 false positive.", "source_proxy_only": false, "evidence_url_pending": false, "source_urls": ["https://news.lgensol.com/company-news/press-releases/2177/", "https://global.toyota/en/newsroom/corporate/39865919.html", "https://www.reuters.com/business/autos-transportation/lg-energy-solution-signs-supply-agreement-with-toyota-2023-10-04/"], "price_path_anchor_urls": ["https://github.com/Songdaiki/stock-web/blob/main/atlas/ohlcv_tradable_by_symbol_year/373/373220/2023.csv?plain=1", "https://github.com/Songdaiki/stock-web/blob/main/atlas/symbol_profiles/373/373220.json?plain=1"], "fine_archetype_id": "C12_CELL_CUSTOMER_CONTRACT_CAPEX_MARGIN_FCF_GUARD", "deep_sub_archetype_id": "C12_DEEP_TOYOTA_20GWH_SUPPLY_CONTRACT_VS_OPERATING_MARGIN_FCF_BRIDGE", "profile_corporate_action_candidate_count": 0, "corporate_action_candidate_dates": [], "corporate_action_window_status": "clean_180D_window", "new_to_c12_symbol": false, "new_to_c12_trigger_family": true, "independent_evidence_weight": 0.5, "do_not_count_as_new_case": false, "row_type": "trigger", "round": "R3", "loop": 99, "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK", "price_data_source": "Songdaiki/stock-web", "price_source": "Songdaiki/stock-web", "upstream_source": "FinanceData/marcap", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "calibration_usable": true, "forward_window_trading_days": 180, "forward_window_status": "complete_180D_within_manifest_max_date", "corporate_action_window_contaminated": false, "same_entry_group_id": "C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK|373220|Stage2-Actionable|2023-10-06", "dedupe_for_aggregate": true, "aggregate_group_role": "representative_case", "representative_trigger": true, "novelty_key": "C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK|373220|Stage2-Actionable|2023-10-06", "dedupe_status": "new_independent_case", "entry_price_field": "close"}
{"row_id": "R3L99-C12-002", "case_id": "C12_006400_2023-04-27_STAGE2_SDI_GM_JV_PARENT_CALL_OFF_GUARD", "symbol": "006400", "company_name": "Samsung SDI / 삼성SDI", "trigger_type": "Stage2-Actionable", "trigger_family": "cell_customer_JV_capacity_parent_proxy_calloff_guard", "trigger_date": "2023-04-26", "entry_date": "2023-04-27", "entry_price": 706000.0, "MFE_30D_pct": 5.52, "MAE_30D_pct": -7.22, "MFE_90D_pct": 5.52, "MAE_90D_pct": -17.42, "MFE_180D_pct": 5.52, "MAE_180D_pct": -49.86, "MFE_250D_pct": 5.52, "MAE_250D_pct": -51.56, "MFE_500D_pct": 5.52, "MAE_500D_pct": -77.25, "peak_date_180D": "2023-06-12", "peak_price_180D": 745000.0, "trough_date_180D": "2024-01-23", "trough_price_180D": 354000.0, "drawdown_after_peak_180D_pct": -52.48, "case_role": "counterexample", "outcome_label": "counterexample_parent_proxy_capacity_not_customer_pull_or_margin_bridge", "current_profile_error": true, "current_profile_verdict": "current_profile_false_positive_if_JV_capacity_counts_as_customer_pull_without_parent_margin_bridge", "baseline_profile_decision": "Stage2-Actionable if JV capacity treated as contract backlog", "proposed_profile_decision": "Stage2-Watch until parent-level utilization, customer pull, capex digestion, margin and FCF bridge appear", "evidence_summary": "Samsung SDI and GM planned a >30GWh U.S. battery JV. C12 should not let parent-level capacity/JV vocabulary substitute for actual listed-parent shipment cadence, call-off risk reduction, margin and FCF conversion.", "source_proxy_only": false, "evidence_url_pending": false, "source_urls": ["https://www.samsungsdi.com/sdi-now/sdi-news/3162.html?idx=3162&pageIndex=2&pagesize=15", "https://news.gm.com/home.detail.html/Pages/news/us/en/2023/apr/0426-samsungsdi.html", "https://www.reuters.com/business/autos-transportation/gm-samsung-sdi-plan-build-new-us-battery-plant-sources-2023-04-24/"], "price_path_anchor_urls": ["https://github.com/Songdaiki/stock-web/blob/main/atlas/ohlcv_tradable_by_symbol_year/006/006400/2023.csv?plain=1", "https://github.com/Songdaiki/stock-web/blob/main/atlas/symbol_profiles/006/006400.json?plain=1"], "fine_archetype_id": "C12_CELL_JV_CAPACITY_PARENT_PROXY_CALLOFF_MARGIN_GUARD", "deep_sub_archetype_id": "C12_DEEP_GM_JV_30GWH_CAPACITY_VS_PARENT_FCF_AND_UTILIZATION", "profile_corporate_action_candidate_count": 3, "corporate_action_candidate_dates": ["1996-04-29", "1998-10-16", "2014-04-22"], "corporate_action_window_status": "clean_180D_window_old_candidates_only", "new_to_c12_symbol": false, "new_to_c12_trigger_family": true, "independent_evidence_weight": 0.5, "do_not_count_as_new_case": false, "row_type": "trigger", "round": "R3", "loop": 99, "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK", "price_data_source": "Songdaiki/stock-web", "price_source": "Songdaiki/stock-web", "upstream_source": "FinanceData/marcap", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "calibration_usable": true, "forward_window_trading_days": 180, "forward_window_status": "complete_180D_within_manifest_max_date", "corporate_action_window_contaminated": false, "same_entry_group_id": "C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK|006400|Stage2-Actionable|2023-04-27", "dedupe_for_aggregate": true, "aggregate_group_role": "representative_case", "representative_trigger": true, "novelty_key": "C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK|006400|Stage2-Actionable|2023-04-27", "dedupe_status": "new_independent_case", "entry_price_field": "close"}
{"row_id": "R3L99-C12-003", "case_id": "C12_247540_2023-12-04_STAGE2_ECOPROBM_SDI_CONTRACT_LATE_CYCLE", "symbol": "247540", "company_name": "EcoPro BM / 에코프로비엠", "trigger_type": "Stage2-Actionable", "trigger_family": "cathode_customer_supply_contract_late_cycle_calloff_guard", "trigger_date": "2023-12-01", "entry_date": "2023-12-04", "entry_price": 323000.0, "MFE_30D_pct": 9.6, "MAE_30D_pct": -17.96, "MFE_90D_pct": 9.6, "MAE_90D_pct": -34.67, "MFE_180D_pct": 9.6, "MAE_180D_pct": -49.23, "MFE_250D_pct": 9.6, "MAE_250D_pct": -62.72, "MFE_500D_pct": 9.6, "MAE_500D_pct": -74.89, "peak_date_180D": "2023-12-04", "peak_price_180D": 354000.0, "trough_date_180D": "2024-08-05", "trough_price_180D": 164000.0, "drawdown_after_peak_180D_pct": -53.67, "case_role": "counterexample", "outcome_label": "counterexample_large_customer_contract_not_enough_after_cycle_peak", "current_profile_error": true, "current_profile_verdict": "current_profile_false_positive_if_large_customer_contract_size_promotes_yellow_after_cycle_peak", "baseline_profile_decision": "Stage2-Actionable / Yellow if contract size is overweighted", "proposed_profile_decision": "Stage2-Watch only until customer pull, ASP/mix, inventory and margin/revision bridge are visible; late-cycle 4B guard remains active", "evidence_summary": "EcoPro BM's KRW 44T Samsung SDI cathode deal was a direct customer-contract event, but the late-cycle entry produced only single-digit MFE and severe 90D/180D MAE. C12 needs call-off and margin confirmation, not only contract size.", "source_proxy_only": false, "evidence_url_pending": false, "source_urls": ["https://www.kedglobal.com/batteries/newsView/ked202312030001", "https://koreajoongangdaily.joins.com/news/2023-12-03/business/industry/EcoPro-BM-secures-34-billion-deal-as-Samsung-SDIs-cathode-supplier/1926748"], "price_path_anchor_urls": ["https://github.com/Songdaiki/stock-web/blob/main/atlas/ohlcv_tradable_by_symbol_year/247/247540/2023.csv?plain=1", "https://github.com/Songdaiki/stock-web/blob/main/atlas/symbol_profiles/247/247540.json?plain=1"], "fine_archetype_id": "C12_CATHODE_CUSTOMER_SUPPLY_CONTRACT_LATE_CYCLE_MARGIN_GUARD", "deep_sub_archetype_id": "C12_DEEP_SDI_44T_CATHODE_CONTRACT_VS_EV_DEMAND_AND_MARGIN_BREAK", "profile_corporate_action_candidate_count": 2, "corporate_action_candidate_dates": ["2022-06-27", "2022-07-15"], "corporate_action_window_status": "clean_180D_window_old_candidates_only", "new_to_c12_symbol": false, "new_to_c12_trigger_family": true, "independent_evidence_weight": 0.5, "do_not_count_as_new_case": false, "row_type": "trigger", "round": "R3", "loop": 99, "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK", "price_data_source": "Songdaiki/stock-web", "price_source": "Songdaiki/stock-web", "upstream_source": "FinanceData/marcap", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "calibration_usable": true, "forward_window_trading_days": 180, "forward_window_status": "complete_180D_within_manifest_max_date", "corporate_action_window_contaminated": false, "same_entry_group_id": "C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK|247540|Stage2-Actionable|2023-12-04", "dedupe_for_aggregate": true, "aggregate_group_role": "representative_case", "representative_trigger": true, "novelty_key": "C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK|247540|Stage2-Actionable|2023-12-04", "dedupe_status": "new_independent_case", "entry_price_field": "close"}
{"row_id": "R3L99-C12-004", "case_id": "C12_361610_2024-03-25_STAGE4C_SEPARATOR_CUSTOMER_CALLOFF_UTILIZATION_BREAK", "symbol": "361610", "company_name": "SK아이이테크놀로지", "trigger_type": "Stage4C", "trigger_family": "separator_customer_calloff_utilization_hard_4c", "trigger_date": "2024-03-25", "entry_date": "2024-03-25", "entry_price": 76300.0, "MFE_30D_pct": 1.83, "MAE_30D_pct": -23.59, "MFE_90D_pct": 1.83, "MAE_90D_pct": -59.44, "MFE_180D_pct": 1.83, "MAE_180D_pct": -70.31, "MFE_250D_pct": 1.83, "MAE_250D_pct": -72.87, "MFE_500D_pct": 1.83, "MAE_500D_pct": -77.85, "peak_date_180D": "2024-03-26", "peak_price_180D": 77700.0, "trough_date_180D": "2024-12-09", "trough_price_180D": 22650.0, "drawdown_after_peak_180D_pct": -70.85, "case_role": "4C_success", "outcome_label": "positive_hard_4c_separator_customer_calloff_utilization_break", "current_profile_error": false, "current_profile_verdict": "current_profile_correct_if_hard_4c_requires_utilization_calloff_margin_break", "baseline_profile_decision": "Stage2/4B risk if contract label remains unresolved", "proposed_profile_decision": "Stage4C confirmed only when customer call-off/utilization plus margin break is non-price-confirmed", "evidence_summary": "Separator supplier path with almost no MFE and deep 90D/180D MAE supports hard-4C routing once utilization/call-off and margin break are confirmed. This is a C12 customer-pull failure, not merely broad EV weakness.", "source_proxy_only": true, "evidence_url_pending": true, "source_urls": [], "price_path_anchor_urls": ["https://github.com/Songdaiki/stock-web/blob/main/atlas/ohlcv_tradable_by_symbol_year/361/361610/2024.csv?plain=1", "https://github.com/Songdaiki/stock-web/blob/main/atlas/symbol_profiles/361/361610.json?plain=1"], "fine_archetype_id": "C12_SEPARATOR_CUSTOMER_CALLOFF_UTILIZATION_HARD_4C", "deep_sub_archetype_id": "C12_DEEP_SEPARATOR_CUSTOMER_PULL_FAILURE_WITH_NO_RECOVERY_MFE", "profile_corporate_action_candidate_count": 0, "corporate_action_candidate_dates": [], "corporate_action_window_status": "clean_180D_window", "new_to_c12_symbol": false, "new_to_c12_trigger_family": true, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false, "row_type": "trigger", "round": "R3", "loop": 99, "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK", "price_data_source": "Songdaiki/stock-web", "price_source": "Songdaiki/stock-web", "upstream_source": "FinanceData/marcap", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "calibration_usable": true, "forward_window_trading_days": 180, "forward_window_status": "complete_180D_within_manifest_max_date", "corporate_action_window_contaminated": false, "same_entry_group_id": "C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK|361610|Stage4C|2024-03-25", "dedupe_for_aggregate": true, "aggregate_group_role": "representative_case", "representative_trigger": true, "novelty_key": "C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK|361610|Stage4C|2024-03-25", "dedupe_status": "new_independent_case", "entry_price_field": "close"}
{"row_id": "R3L99-C12-005", "case_id": "C12_278280_2024-03-25_STAGE4C_ELECTROLYTE_CUSTOMER_PULL_MARGIN_BREAK", "symbol": "278280", "company_name": "천보", "trigger_type": "Stage4C", "trigger_family": "electrolyte_customer_pull_margin_hard_4c", "trigger_date": "2024-03-25", "entry_date": "2024-03-25", "entry_price": 89100.0, "MFE_30D_pct": 1.8, "MAE_30D_pct": -13.92, "MFE_90D_pct": 1.8, "MAE_90D_pct": -45.01, "MFE_180D_pct": 1.8, "MAE_180D_pct": -57.58, "MFE_250D_pct": 1.8, "MAE_250D_pct": -60.49, "MFE_500D_pct": 1.8, "MAE_500D_pct": -64.31, "peak_date_180D": "2024-03-25", "peak_price_180D": 90700.0, "trough_date_180D": "2024-12-09", "trough_price_180D": 37800.0, "drawdown_after_peak_180D_pct": -58.32, "case_role": "4C_success", "outcome_label": "positive_hard_4c_electrolyte_customer_pull_margin_break", "current_profile_error": false, "current_profile_verdict": "current_profile_correct_if_hard_4c_requires_customer_pull_margin_break", "baseline_profile_decision": "Stage2/4B if electrolyte contract vocabulary remains unbroken", "proposed_profile_decision": "Stage4C confirmed once customer pull, inventory and margin break are present; do not rescue with generic battery-policy label", "evidence_summary": "Electrolyte materials path shows a hard customer-pull/margin break template: almost no recovery MFE and sustained deep MAE. This adds a positive C12 4C path distinct from cell-maker headline recovery.", "source_proxy_only": true, "evidence_url_pending": true, "source_urls": [], "price_path_anchor_urls": ["https://github.com/Songdaiki/stock-web/blob/main/atlas/ohlcv_tradable_by_symbol_year/278/278280/2024.csv?plain=1", "https://github.com/Songdaiki/stock-web/blob/main/atlas/symbol_profiles/278/278280.json?plain=1"], "fine_archetype_id": "C12_ELECTROLYTE_CUSTOMER_PULL_MARGIN_HARD_4C", "deep_sub_archetype_id": "C12_DEEP_ELECTROLYTE_CUSTOMER_PULL_FAILURE_WITH_MARGIN_RESET", "profile_corporate_action_candidate_count": 0, "corporate_action_candidate_dates": [], "corporate_action_window_status": "clean_180D_window", "new_to_c12_symbol": true, "new_to_c12_trigger_family": true, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false, "row_type": "trigger", "round": "R3", "loop": 99, "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK", "price_data_source": "Songdaiki/stock-web", "price_source": "Songdaiki/stock-web", "upstream_source": "FinanceData/marcap", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "calibration_usable": true, "forward_window_trading_days": 180, "forward_window_status": "complete_180D_within_manifest_max_date", "corporate_action_window_contaminated": false, "same_entry_group_id": "C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK|278280|Stage4C|2024-03-25", "dedupe_for_aggregate": true, "aggregate_group_role": "representative_case", "representative_trigger": true, "novelty_key": "C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK|278280|Stage4C|2024-03-25", "dedupe_status": "new_independent_case", "entry_price_field": "close"}
{"row_id": "R3L99-C12-006", "case_id": "C12_005070_2024-03-25_STAGE4C_CATHODE_CUSTOMER_PULL_MARGIN_RESET", "symbol": "005070", "company_name": "코스모신소재", "trigger_type": "Stage4C", "trigger_family": "cathode_material_customer_pull_margin_hard_4c", "trigger_date": "2024-03-25", "entry_date": "2024-03-25", "entry_price": 171300.0, "MFE_30D_pct": 2.51, "MAE_30D_pct": -17.69, "MFE_90D_pct": 2.51, "MAE_90D_pct": -41.56, "MFE_180D_pct": 2.51, "MAE_180D_pct": -69.64, "MFE_250D_pct": 2.51, "MAE_250D_pct": -71.22, "MFE_500D_pct": 2.51, "MAE_500D_pct": -76.12, "peak_date_180D": "2024-03-25", "peak_price_180D": 175600.0, "trough_date_180D": "2024-12-09", "trough_price_180D": 52000.0, "drawdown_after_peak_180D_pct": -70.39, "case_role": "4C_success", "outcome_label": "positive_hard_4c_cathode_customer_pull_margin_reset", "current_profile_error": false, "current_profile_verdict": "current_profile_correct_if_hard_4c_requires_customer_pull_margin_break", "baseline_profile_decision": "Stage2/4B if cathode customer-demand break is underweighted", "proposed_profile_decision": "Stage4C confirmed by customer-demand/utilization and margin break; contract headline cannot prevent hard thesis break", "evidence_summary": "Cathode material path adds another C12 hard-4C calibration row: single-digit MFE, severe 90D/180D MAE, and no evidence that customer pull or margin bridge repaired the thesis in the forward window.", "source_proxy_only": true, "evidence_url_pending": true, "source_urls": [], "price_path_anchor_urls": ["https://github.com/Songdaiki/stock-web/blob/main/atlas/ohlcv_tradable_by_symbol_year/005/005070/2024.csv?plain=1", "https://github.com/Songdaiki/stock-web/blob/main/atlas/symbol_profiles/005/005070.json?plain=1"], "fine_archetype_id": "C12_CATHODE_CUSTOMER_PULL_MARGIN_HARD_4C", "deep_sub_archetype_id": "C12_DEEP_CATHODE_CUSTOMER_DEMAND_BREAK_WITH_SEVERE_180D_MAE", "profile_corporate_action_candidate_count": 8, "corporate_action_candidate_dates": ["2000-01-13", "2001-02-02", "2001-03-30", "2002-07-02", "2003-01-30", "2005-05-04", "2008-01-22", "2019-11-13"], "corporate_action_window_status": "clean_180D_window_old_candidates_only", "new_to_c12_symbol": true, "new_to_c12_trigger_family": true, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false, "row_type": "trigger", "round": "R3", "loop": 99, "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK", "price_data_source": "Songdaiki/stock-web", "price_source": "Songdaiki/stock-web", "upstream_source": "FinanceData/marcap", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "calibration_usable": true, "forward_window_trading_days": 180, "forward_window_status": "complete_180D_within_manifest_max_date", "corporate_action_window_contaminated": false, "same_entry_group_id": "C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK|005070|Stage4C|2024-03-25", "dedupe_for_aggregate": true, "aggregate_group_role": "representative_case", "representative_trigger": true, "novelty_key": "C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK|005070|Stage4C|2024-03-25", "dedupe_status": "new_independent_case", "entry_price_field": "close"}
{"row_id": "R3L99-C12-007", "case_id": "C12_348370_2024-01-22_STAGE4B_ELECTROLYTE_FALSE_HARD_4C_EXCEPTION", "symbol": "348370", "company_name": "엔켐", "trigger_type": "Stage4B", "trigger_family": "electrolyte_growth_exception_false_hard_4c_filter", "trigger_date": "2024-01-22", "entry_date": "2024-01-22", "entry_price": 103400.0, "MFE_30D_pct": 246.71, "MAE_30D_pct": -3.09, "MFE_90D_pct": 246.71, "MAE_90D_pct": -3.09, "MFE_180D_pct": 246.71, "MAE_180D_pct": -3.09, "MFE_250D_pct": 246.71, "MAE_250D_pct": -20.12, "MFE_500D_pct": 246.71, "MAE_500D_pct": -45.34, "peak_date_180D": "2024-02-21", "peak_price_180D": 358500.0, "trough_date_180D": "2024-01-22", "trough_price_180D": 100200.0, "drawdown_after_peak_180D_pct": -72.05, "case_role": "4B_too_early_or_false_4c_counterexample", "outcome_label": "counterexample_false_hard_4c_electrolyte_growth_exception", "current_profile_error": true, "current_profile_verdict": "current_profile_false_positive_if_broad_calloff_guard_routes_growth_exception_to_hard_4c", "baseline_profile_decision": "Hard 4C if broad EV slowdown/call-off label is over-applied", "proposed_profile_decision": "Local Stage4B watch only until non-price customer call-off thesis break is proven; growth exception filter blocks hard 4C", "evidence_summary": "엔켐 demonstrates the exception side of C12. A broad customer-calloff/EV-demand guard would have misrouted the stock to hard 4C before a +246.71% MFE. C12 needs a growth-exception filter before hard-4C routing.", "source_proxy_only": true, "evidence_url_pending": true, "source_urls": [], "price_path_anchor_urls": ["https://github.com/Songdaiki/stock-web/blob/main/atlas/ohlcv_tradable_by_symbol_year/348/348370/2024.csv?plain=1", "https://github.com/Songdaiki/stock-web/blob/main/atlas/symbol_profiles/348/348370.json?plain=1"], "fine_archetype_id": "C12_ELECTROLYTE_GROWTH_EXCEPTION_FALSE_HARD_4C", "deep_sub_archetype_id": "C12_DEEP_ELECTROLYTE_CUSTOMER_GROWTH_EXCEPTION_BLOWOFF_VS_BROAD_CALLOFF_GUARD", "profile_corporate_action_candidate_count": 0, "corporate_action_candidate_dates": [], "corporate_action_window_status": "clean_180D_window", "new_to_c12_symbol": true, "new_to_c12_trigger_family": true, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false, "row_type": "trigger", "round": "R3", "loop": 99, "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK", "price_data_source": "Songdaiki/stock-web", "price_source": "Songdaiki/stock-web", "upstream_source": "FinanceData/marcap", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "calibration_usable": true, "forward_window_trading_days": 180, "forward_window_status": "complete_180D_within_manifest_max_date", "corporate_action_window_contaminated": false, "same_entry_group_id": "C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK|348370|Stage4B|2024-01-22", "dedupe_for_aggregate": true, "aggregate_group_role": "representative_case", "representative_trigger": true, "novelty_key": "C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK|348370|Stage4B|2024-01-22", "dedupe_status": "new_independent_case", "entry_price_field": "close"}
{"row_type": "score_simulation", "symbol": "373220", "canonical_archetype_id": "C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK", "entry_date": "2023-10-06", "current_proxy_score": 77, "candidate_C12_guarded_score": 65, "current_proxy_stage": "Stage3-Yellow", "candidate_stage": "Stage2-Watch", "delta": -12, "decision_reason": "Toyota 20GWh contract needs shipment cadence, margin/revision, working-capital and FCF bridge before Yellow."}
{"row_type": "score_simulation", "symbol": "006400", "canonical_archetype_id": "C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK", "entry_date": "2023-04-27", "current_proxy_score": 75, "candidate_C12_guarded_score": 63, "current_proxy_stage": "Stage3-Yellow", "candidate_stage": "Stage2-Watch", "delta": -12, "decision_reason": "GM JV capacity is not listed-parent customer pull unless utilization/margin/FCF bridge confirms it."}
{"row_type": "score_simulation", "symbol": "247540", "canonical_archetype_id": "C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK", "entry_date": "2023-12-04", "current_proxy_score": 79, "candidate_C12_guarded_score": 60, "current_proxy_stage": "Stage3-Yellow", "candidate_stage": "Stage2-Watch / local 4B guard", "delta": -19, "decision_reason": "Huge customer contract size after cycle peak needs call-off and ASP/margin validation."}
{"row_type": "score_simulation", "symbol": "361610", "canonical_archetype_id": "C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK", "entry_date": "2024-03-25", "current_proxy_score": 39, "candidate_C12_guarded_score": 18, "current_proxy_stage": "Stage2-Watch / 4B", "candidate_stage": "Stage4C", "delta": -21, "decision_reason": "Confirmed utilization/customer-pull break plus tiny MFE/deep MAE supports hard 4C."}
{"row_type": "score_simulation", "symbol": "278280", "canonical_archetype_id": "C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK", "entry_date": "2024-03-25", "current_proxy_score": 42, "candidate_C12_guarded_score": 20, "current_proxy_stage": "Stage2-Watch / 4B", "candidate_stage": "Stage4C", "delta": -22, "decision_reason": "Electrolyte customer-pull/margin break should route to hard 4C."}
{"row_type": "score_simulation", "symbol": "005070", "canonical_archetype_id": "C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK", "entry_date": "2024-03-25", "current_proxy_score": 44, "candidate_C12_guarded_score": 19, "current_proxy_stage": "Stage2-Watch / 4B", "candidate_stage": "Stage4C", "delta": -25, "decision_reason": "Cathode-material customer-demand break and severe 180D MAE support hard 4C."}
{"row_type": "score_simulation", "symbol": "348370", "canonical_archetype_id": "C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK", "entry_date": "2024-01-22", "current_proxy_score": 25, "candidate_C12_guarded_score": 66, "current_proxy_stage": "Hard 4C if broad call-off guard over-applied", "candidate_stage": "local Stage4B watch, not hard 4C", "delta": 41, "decision_reason": "Growth-exception filter prevents broad C12 call-off guard from misclassifying an extreme MFE winner."}
{"row_type": "stage_transition", "row_id": "R3L99-C12-001", "symbol": "373220", "canonical_archetype_id": "C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK", "trigger_type": "Stage2-Actionable", "entry_date": "2023-10-06", "transition_label": "Stage2_false_positive_or_Yellow_block_supported", "mfe_mae_180_spread_pct": -22.53, "profile_residual": "current_profile_false_positive_if_customer_volume_contract_overrides_margin_fcf_bridge"}
{"row_type": "stage_transition", "row_id": "R3L99-C12-002", "symbol": "006400", "canonical_archetype_id": "C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK", "trigger_type": "Stage2-Actionable", "entry_date": "2023-04-27", "transition_label": "Stage2_false_positive_or_Yellow_block_supported", "mfe_mae_180_spread_pct": -44.34, "profile_residual": "current_profile_false_positive_if_JV_capacity_counts_as_customer_pull_without_parent_margin_bridge"}
{"row_type": "stage_transition", "row_id": "R3L99-C12-003", "symbol": "247540", "canonical_archetype_id": "C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK", "trigger_type": "Stage2-Actionable", "entry_date": "2023-12-04", "transition_label": "Stage2_false_positive_or_Yellow_block_supported", "mfe_mae_180_spread_pct": -39.63, "profile_residual": "current_profile_false_positive_if_large_customer_contract_size_promotes_yellow_after_cycle_peak"}
{"row_type": "stage_transition", "row_id": "R3L99-C12-004", "symbol": "361610", "canonical_archetype_id": "C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK", "trigger_type": "Stage4C", "entry_date": "2024-03-25", "transition_label": "hard_4C_confirmation_supported", "mfe_mae_180_spread_pct": -68.48, "profile_residual": "current_profile_correct_if_hard_4c_requires_utilization_calloff_margin_break"}
{"row_type": "stage_transition", "row_id": "R3L99-C12-005", "symbol": "278280", "canonical_archetype_id": "C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK", "trigger_type": "Stage4C", "entry_date": "2024-03-25", "transition_label": "hard_4C_confirmation_supported", "mfe_mae_180_spread_pct": -55.78, "profile_residual": "current_profile_correct_if_hard_4c_requires_customer_pull_margin_break"}
{"row_type": "stage_transition", "row_id": "R3L99-C12-006", "symbol": "005070", "canonical_archetype_id": "C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK", "trigger_type": "Stage4C", "entry_date": "2024-03-25", "transition_label": "hard_4C_confirmation_supported", "mfe_mae_180_spread_pct": -67.13, "profile_residual": "current_profile_correct_if_hard_4c_requires_customer_pull_margin_break"}
{"row_type": "stage_transition", "row_id": "R3L99-C12-007", "symbol": "348370", "canonical_archetype_id": "C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK", "trigger_type": "Stage4B", "entry_date": "2024-01-22", "transition_label": "local_4B_watch_not_full_4C_or_false_hard_4C_counterexample", "mfe_mae_180_spread_pct": 243.62, "profile_residual": "current_profile_false_positive_if_broad_calloff_guard_routes_growth_exception_to_hard_4c"}
{"row_type": "shadow_weight", "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK", "scope": "canonical_archetype_specific", "proposed_rule_id": "C12_customer_pull_utilization_margin_fcf_bridge_required_before_Yellow_or_Green", "direction": "tighten_promotion_bridge", "target_stage": "Stage2-Actionable_to_Stage3-Yellow", "supporting_rows": ["R3L99-C12-001", "R3L99-C12-002", "R3L99-C12-003"], "counterbalance_rows": ["R3L99-C12-004", "R3L99-C12-005", "R3L99-C12-006", "R3L99-C12-007"], "max_shadow_delta": "-8_to_-14_score_when_bridge_absent", "do_not_apply_globally": true}
{"row_type": "shadow_weight", "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK", "scope": "canonical_archetype_specific", "proposed_rule_id": "C12_growth_exception_filter_before_hard_4C", "direction": "block_overbroad_hard_4c", "target_stage": "Stage4C", "supporting_rows": ["R3L99-C12-007"], "counterbalance_rows": ["R3L99-C12-004", "R3L99-C12-005", "R3L99-C12-006"], "max_shadow_delta": "Stage4C_to_local_4B_watch_when_no_non_price_calloff_break", "do_not_apply_globally": true}
{"row_type": "residual_contribution", "selected_round": "R3", "selected_loop": 99, "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK", "new_independent_case_count": 7, "reused_case_count": 0, "new_symbol_count": 4, "same_archetype_new_symbol_count": 4, "same_archetype_new_trigger_family_count": 7, "new_trigger_family_count": 7, "positive_case_count": 3, "counterexample_count": 4, "stage4b_case_count": 1, "stage4c_case_count": 3, "current_profile_error_count": 4, "loop_contribution_label": "canonical_archetype_rule_candidate", "do_not_propose_new_weight_delta": false, "new_axis_proposed": "C12_customer_pull_utilization_margin_fcf_bridge_required_before_Yellow_or_Green_plus_growth_exception_filter_before_hard_4C", "existing_axis_strengthened": "stage2_required_bridge, hard_4c_confirmation, local_4b_watch_guard, full_4b_requires_non_price_evidence", "existing_axis_weakened": null}
```

## 20. Batch Ingest Self-Audit

```text
expected_v12_result_file: true
filename_pattern_pass: true
metadata_filename_consistency: pass
jsonl_trigger_row_count: 7
calibration_usable_trigger_count: 7
representative_trigger_count: 7
new_weight_evidence_candidate_count: 7
guardrail_candidate_count: 4
narrative_only_or_rejected_count: 0
rows_missing_required_mfe_mae: 0
rows_missing_entry_price_or_date: 0
rows_with_noncanonical_trigger_type: 0
rows_with_compact_mfe_mae_alias_only: 0
ready_for_batch_ingest: true
```

## 21. Deferred Coding Agent Handoff Prompt

### Purpose

You are now in the repository implementation phase. The attached Markdown files are v12 post-calibrated residual research outputs produced using the Songdaiki/stock-web OHLC atlas. These MDs are not live candidate research. They are historical calibration research designed to extend the already-applied e2r_2_1_stock_web_calibrated profile. Do not blindly apply every shadow row. Ingest the machine-readable rows and update the sector/canonical-archetype calibration ledger.

### Price source context

- Primary historical price source used by the research MD: Songdaiki/stock-web.
- Price basis: tradable_raw.
- Price adjustment status: raw_unadjusted_marcap.
- Price shard pattern: atlas/ohlcv_tradable_by_symbol_year/{prefix}/{symbol}/{year}.csv.
- Symbol profile pattern: atlas/symbol_profiles/{prefix}/{symbol}.json.

### Rules

1. Use only `calibration_usable=true` rows for quantitative calibration.
2. Do not count reused cases as new independent evidence unless `independent_evidence_weight > 0`.
3. Do not treat `schema_rematerialization_only` or `duplicate_low_value_loop` as new evidence.
4. Do not apply global deltas unless multiple large_sector_id values support the same direction.
5. Prefer sector-specific or canonical-archetype-specific shadow profiles.
6. Positive score promotion requires non-price evidence and clean 180D MFE/MAE.
7. 4B rows are overlay/risk calibration only.
8. 4C rows are thesis-break/protection calibration only.
9. Price-only rows cannot promote Stage2/Stage3.
10. If a v12 MD weakens an already applied axis, log it as residual counterexample rather than immediately reverting.
11. Production scoring must not change unless the user explicitly asks for another promotion batch.

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

## 22. Next Round State

```text
completed_round = R3
completed_loop = 99
selection_basis = docs/core/V12_Research_No_Repeat_Index.md
selected_priority_bucket = Priority 1
next_recommended_archetypes = C05_EPC_MEGA_CONTRACT_MARGIN_GAP, C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION, C27_CONTENT_IP_GLOBAL_MONETIZATION, C02_POWER_GRID_DATACENTER_CAPEX
round_schedule_status = coverage_index_selected
round_sector_consistency = pass
```

## 23. Source Notes

- Price atlas: Songdaiki/stock-web.
- Upstream source: FinanceData/marcap.
- Price basis: tradable_raw.
- Price adjustment status: raw_unadjusted_marcap.
- This file is historical calibration research only and is not a current investment recommendation.
