# E2R Stock-Web v12 Residual Research — R3 loop 100 / L3 / C12

```yaml
schema_family: v12_sector_archetype_residual
research_session: post_calibrated_sector_archetype_residual_research
mode: historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12
selected_round: R3
selected_loop: 100
large_sector_id: L3_BATTERY_EV_GREEN_MOBILITY
canonical_archetype_id: C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK
fine_archetype_id: C12_CUSTOMER_CALLOFF_DELIVERY_ACCEPTANCE_MARGIN_FCF_BRIDGE
deep_sub_archetype_id: C12_DEEP_CATHODE_SEPARATOR_COPPER_FOIL_CNT_EQUIPMENT_CUSTOMER_PULL_VS_CONTRACT_BACKLOG_LABEL
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

This loop adds **8 calibration-usable C12 trigger rows** for `R3 / L3_BATTERY_EV_GREEN_MOBILITY / C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK`.

The C12 mechanism is a two-key lock. A customer name, supply agreement, JV capacity, or battery-equipment backlog is only the first key. The second key is actual customer pull: shipment cadence, utilization, delivery acceptance, ASP/mix, margin, FCF, or revision. Without that second key, the stage machine can mistake a label on the box for a moving conveyor belt.

This loop separates four paths:

1. **Contract/backlog label without delivery or margin bridge** → Stage2-Watch / guarded Actionable, not Yellow.
2. **Confirmed client demand / stock-rebalancing break** → hard Stage4C.
3. **Recovery or growth-exception evidence** → local Stage4B watch, not hard 4C.
4. **Verified revenue conversion despite temporary slowdown** → Stage2-Actionable can survive the sector downcycle.

## 2. Coverage-Index Selection

- `V12_Research_No_Repeat_Index.md` places C12 in Priority 1 with 32 rows and 18 more rows needed to reach the 50-row practical calibration zone.
- Prior local loop `R3_loop_99 / C12` added 7 representative triggers, so the local-session adjusted C12 count was 39.
- This loop adds 8 representative triggers and moves the local-session adjusted count to **47**, leaving **3** more rows to reach the 50-row practical calibration zone.
- Hard duplicate key avoided: `canonical_archetype_id + symbol + trigger_type + entry_date`.
- Prior C12 loop99 symbols `373220`, `006400`, `247540`, `361610`, `278280`, `005070`, `348370` are not reused in this loop.

## 3. Price Source Validation

```json
{"row_type":"price_source_validation","price_atlas_repo":"Songdaiki/stock-web","manifest":"atlas/manifest.json","source_name":"FinanceData/marcap","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","calibration_shard_root":"atlas/ohlcv_tradable_by_symbol_year","manifest_max_date":"2026-02-20","notes":"Raw/unadjusted OHLC. Zero-volume and invalid rows are excluded from calibration shards. Corporate-action-contaminated windows are blocked by default."}
```

| symbol | profile path | selected shard | corporate-action status |
|---|---|---|---|
| 003670 | atlas/symbol_profiles/003/003670.json | atlas/ohlcv_tradable_by_symbol_year/003/003670/2023.csv | clean_180D_window_old_candidates_only |
| 066970 | atlas/symbol_profiles/066/066970.json | atlas/ohlcv_tradable_by_symbol_year/066/066970/2023.csv | clean_180D_window_old_candidates_only |
| 011790 | atlas/symbol_profiles/011/011790.json | atlas/ohlcv_tradable_by_symbol_year/011/011790/2024.csv | clean_180D_window_old_candidates_only |
| 393890 | atlas/symbol_profiles/393/393890.json | atlas/ohlcv_tradable_by_symbol_year/393/393890/2024.csv | clean_180D_window |
| 121600 | atlas/symbol_profiles/121/121600.json | atlas/ohlcv_tradable_by_symbol_year/121/121600/2024.csv | clean_180D_window_old_candidates_only |
| 336370 | atlas/symbol_profiles/336/336370.json | atlas/ohlcv_tradable_by_symbol_year/336/336370/2024.csv | clean_180D_window_after_Jan2024_candidates |
| 137400 | atlas/symbol_profiles/137/137400.json | atlas/ohlcv_tradable_by_symbol_year/137/137400/2024.csv | clean_180D_window_old_candidates_only |
| 222080 | atlas/symbol_profiles/222/222080.json | atlas/ohlcv_tradable_by_symbol_year/222/222080/2025.csv | clean_180D_window_old_candidates_only |

## 4. Evidence Source Map

| symbol | evidence family | source quality | C12 interpretation |
|---|---|---|---|
| 003670 | cathode_GM_Ultium_CAM_contract_without_sustained_calloff_margin_bridge | source_urls_present | Stage2-Actionable allowed, but Yellow/Green require customer pull, shipment cadence, margin/revision bridge, and local 4B watch after blowoff |
| 066970 | cathode_Tesla_contract_size_calloff_reduction_guard | source_urls_present | Stage2-Watch or guarded Actionable until actual shipment/call-off, ASP/mix and margin evidence confirm the contract path |
| 011790 | copper_foil_customer_calloff_margin_break_to_local_4B_watch | source_proxy_pending | Local Stage4B watch after price recovery if customer-pull and margin bridge are not verified; hard 4C only after non-price thesis break |
| 393890 | separator_client_demand_stock_rebalancing_hard_4C | source_urls_present | Stage4C when customer demand reduction and stock-rebalancing evidence are verified |
| 121600 | CNT_conductive_additive_growth_exception_before_hard_4C | source_proxy_pending | Local Stage4B watch only; growth-exception and customer-expansion bridge must be checked before hard 4C |
| 336370 | copper_foil_customer_diversification_growth_exception_before_hard_4C | source_urls_present | Local Stage4B watch only; require actual customer loss/margin break before hard 4C |
| 137400 | battery_equipment_backlog_customer_delivery_delay_calloff_guard | source_proxy_pending | Stage2-Actionable only; block Yellow until delivery acceptance, customer capex schedule, revenue and margin bridge are visible |
| 222080 | battery_equipment_temporary_slowdown_revenue_conversion_exception | source_urls_present | Stage2-Actionable can proceed when revenue conversion, backlog delivery and margin evidence survive the temporary slowdown |

## 5. Case-by-Case Trigger Grid

| case_id | symbol | company | role | trigger_type | entry_date | entry_price | MFE30 | MAE30 | MFE90 | MAE90 | MFE180 | MAE180 | verdict |
|---|---|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| C12_003670_2023-06-05_STAGE2ACTIONABLE_CATHODE_GM_ULTIUM_CAM_CONTRACT_WITHOUT_SUSTAINED_CALLOFF_MARGIN_BRIDGE | 003670 | POSCO Future M / 포스코퓨처엠 | positive_with_4B_late_cycle_guard | Stage2-Actionable | 2023-06-05 | 369500 | 44.52 | -4.74 | 61.84 | -12.58 | 61.84 | -39.92 | current_profile_too_loose_if_CAM_contract_keeps_Yellow_after_calloff_margin_visibility_fades |
| C12_066970_2023-03-02_STAGE2ACTIONABLE_CATHODE_TESLA_CONTRACT_SIZE_CALLOFF_REDUCTION_GUARD | 066970 | L&F / 엘앤에프 | counterexample | Stage2-Actionable | 2023-03-02 | 274000 | 13.87 | -6.02 | 33.58 | -9.31 | 35.4 | -39.05 | current_profile_false_positive_if_contract_size_substitutes_for_confirmed_calloff_and_margin_conversion |
| C12_011790_2024-03-26_STAGE4B_COPPER_FOIL_CUSTOMER_CALLOFF_MARGIN_BREAK_TO_LOCAL_4B_WATCH | 011790 | SKC / SKC | counterexample_4B | Stage4B | 2024-03-26 | 91400 | 14.0 | -9.52 | 27.13 | -16.08 | 27.13 | -45.84 | current_profile_false_positive_if_copper_foil_label_remains_Actionable_after_customer_pull_and_margin_pressure |
| C12_393890_2024-06-10_STAGE4C_SEPARATOR_CLIENT_DEMAND_STOCK_REBALANCING_HARD_4C | 393890 | WCP / 더블유씨피 | 4C_success | Stage4C | 2024-06-10 | 27700 | 7.04 | -22.38 | 7.04 | -43.14 | 10.11 | -60.58 | current_profile_correct_if_hard_4c_requires_client_demand_or_stock_rebalancing_break |
| C12_121600_2024-08-19_STAGE4B_CNT_CONDUCTIVE_ADDITIVE_GROWTH_EXCEPTION_BEFORE_HARD_4C | 121600 | Advanced Nano Products / 나노신소재 | positive_exception | Stage4B | 2024-08-19 | 89500 | 7.82 | -14.19 | 36.98 | -18.88 | 44.47 | -21.56 | current_profile_false_negative_if_generic_battery_calloff_guard_forces_hard_4C_on_CNT_growth_exception |
| C12_336370_2024-10-24_STAGE4B_COPPER_FOIL_CUSTOMER_DIVERSIFICATION_GROWTH_EXCEPTION_BEFORE_HARD_4C | 336370 | Solus Advanced Materials / 솔루스첨단소재 | positive_exception | Stage4B | 2024-10-24 | 10400 | 32.21 | -6.25 | 56.25 | -10.1 | 79.33 | -14.71 | current_profile_false_negative_if_EV_downcycle_calloff_guard_ignores_customer_diversification_and_recovery |
| C12_137400_2024-06-17_STAGE2ACTIONABLE_BATTERY_EQUIPMENT_BACKLOG_CUSTOMER_DELIVERY_DELAY_CALLOFF_GUARD | 137400 | PNT / 피엔티 | counterexample | Stage2-Actionable | 2024-06-17 | 69400 | 13.4 | -8.2 | 13.4 | -25.65 | 17.72 | -42.51 | current_profile_false_positive_if_battery_equipment_backlog_is_treated_as_completed_customer_pull |
| C12_222080_2025-02-17_STAGE2ACTIONABLE_BATTERY_EQUIPMENT_TEMPORARY_SLOWDOWN_REVENUE_CONVERSION_EXCEPTION | 222080 | CIS / 씨아이에스 | positive_exception | Stage2-Actionable | 2025-02-17 | 8180 | 15.28 | -7.7 | 31.17 | -10.15 | 50.86 | -10.15 | current_profile_too_conservative_if_temporary_slowdown_blocks_revenue_conversion_exception |

## 6. Trigger-Level OHLC Backtest Tables

| case_id | symbol | entry_date | entry_price | peak_180D | peak_date | trough_180D | trough_date | drawdown_after_peak_180D | profile CA status |
|---|---|---:|---:|---:|---|---:|---|---:|---|
| C12_003670_2023-06-05_STAGE2ACTIONABLE_CATHODE_GM_ULTIUM_CAM_CONTRACT_WITHOUT_SUSTAINED_CALLOFF_MARGIN_BRIDGE | 003670 | 2023-06-05 | 369500 | 598000 | 2023-07-26 | 222000 | 2024-01-18 | -62.88 | clean_180D_window_old_candidates_only |
| C12_066970_2023-03-02_STAGE2ACTIONABLE_CATHODE_TESLA_CONTRACT_SIZE_CALLOFF_REDUCTION_GUARD | 066970 | 2023-03-02 | 274000 | 371000 | 2023-07-26 | 167000 | 2023-11-01 | -54.99 | clean_180D_window_old_candidates_only |
| C12_011790_2024-03-26_STAGE4B_COPPER_FOIL_CUSTOMER_CALLOFF_MARGIN_BREAK_TO_LOCAL_4B_WATCH | 011790 | 2024-03-26 | 91400 | 116200 | 2024-06-17 | 49500 | 2024-12-09 | -57.4 | clean_180D_window_old_candidates_only |
| C12_393890_2024-06-10_STAGE4C_SEPARATOR_CLIENT_DEMAND_STOCK_REBALANCING_HARD_4C | 393890 | 2024-06-10 | 27700 | 30500 | 2024-08-01 | 10920 | 2025-02-04 | -64.2 | clean_180D_window |
| C12_121600_2024-08-19_STAGE4B_CNT_CONDUCTIVE_ADDITIVE_GROWTH_EXCEPTION_BEFORE_HARD_4C | 121600 | 2024-08-19 | 89500 | 129300 | 2025-01-06 | 70200 | 2024-11-13 | -45.71 | clean_180D_window_old_candidates_only |
| C12_336370_2024-10-24_STAGE4B_COPPER_FOIL_CUSTOMER_DIVERSIFICATION_GROWTH_EXCEPTION_BEFORE_HARD_4C | 336370 | 2024-10-24 | 10400 | 18650 | 2025-03-04 | 8870 | 2024-11-13 | -52.44 | clean_180D_window_after_Jan2024_candidates |
| C12_137400_2024-06-17_STAGE2ACTIONABLE_BATTERY_EQUIPMENT_BACKLOG_CUSTOMER_DELIVERY_DELAY_CALLOFF_GUARD | 137400 | 2024-06-17 | 69400 | 81700 | 2024-07-03 | 39900 | 2024-12-09 | -51.16 | clean_180D_window_old_candidates_only |
| C12_222080_2025-02-17_STAGE2ACTIONABLE_BATTERY_EQUIPMENT_TEMPORARY_SLOWDOWN_REVENUE_CONVERSION_EXCEPTION | 222080 | 2025-02-17 | 8180 | 12340 | 2025-08-05 | 7350 | 2025-03-07 | -40.44 | clean_180D_window_old_candidates_only |

## 7. Current Calibrated Profile Stress Test

### 7.1 Contract and backlog vocabulary still needs a bridge

`066970`, `011790`, and `137400` show how C12 can still over-promote a case if contract size, copper-foil structural demand, or equipment backlog is treated as already-converted customer pull. The repair is not to delete the positive evidence, but to force the second key: actual customer shipment/call-off, delivery acceptance, margin, FCF, or revision.

### 7.2 A real hard-4C route exists, but it must be narrow

`393890` is the clean hard-4C row in this loop. Client demand reduction and stock-rebalancing evidence maps directly to C12 thesis break. The path has tiny MFE and deep MAE, so hard 4C is protective rather than merely bearish storytelling.

### 7.3 Growth exceptions prevent overbroad 4C

`121600`, `336370`, and `222080` protect the profile from a blunt EV-downcycle rule. CNT penetration, copper-foil customer diversification, and equipment revenue conversion can still create positive paths. Generic EV weakness alone must not route these to hard 4C.

## 8. Stage2 / Yellow / Green Comparison

| state | residual failure mode | C12 repair |
|---|---|---|
| Stage2-Actionable | contract/backlog evidence is real but second-key evidence is absent | allow Watch or guarded Actionable only |
| Stage3-Yellow | customer label or backlog amount pushes score above 75 | require shipment/call-off + margin/FCF/revision bridge |
| Stage3-Green | should remain rare in C12 | do not loosen Green; require durable customer pull and clean revision |
| Stage4B | price blowoff or sector weakness appears without thesis break | local watch only |
| Stage4C | customer-pull/utilization/stock-rebalancing/margin break is confirmed | hard 4C allowed |

## 9. 4B Local vs Full-window Timing Audit

| route | rows | implication |
|---|---|---|
| local 4B after positive contract blowoff | 003670, 011790 | keep the positive bridge but demand late-cycle recheck |
| hard 4C client demand break | 393890 | allow hard 4C only when non-price customer-pull break is visible |
| false hard-4C exception | 121600, 336370, 222080 | do not turn generic EV weakness into hard 4C when revenue/customer expansion is alive |
| guarded Stage2 | 066970, 137400 | contract/backlog label is insufficient for Yellow |

## 10. Sector-Specific Rule Candidate

```text
rule_id = L3_C12_customer_pull_delivery_acceptance_margin_fcf_bridge
scope = L3_BATTERY_EV_GREEN_MOBILITY / C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK
action = tighten Stage2-Actionable -> Yellow promotion when customer-contract, JV capacity, supplier backlog, or equipment order evidence lacks shipment/call-off, delivery acceptance, utilization, margin, FCF, or revision bridge
positive_guard = do not route generic EV weakness to hard 4C if growth-exception, customer diversification, or revenue-conversion evidence is still alive
```

## 11. Canonical-Archetype Rule Candidate

```text
new_axis_proposed = C12_customer_pull_delivery_acceptance_margin_fcf_bridge_required_before_Yellow_plus_growth_exception_filter_before_hard_4C
existing_axis_strengthened = stage2_required_bridge, hard_4c_confirmation, local_4b_watch_guard, full_4b_requires_non_price_evidence
existing_axis_weakened = hard_4c_thesis_break_routes_to_4c_when_only_generic_EV_slowdown_or_backlog_label_is_present
```

## 12. Score-Return Alignment Matrix

| symbol | current proxy behavior | candidate C12 behavior | MFE180 | MAE180 | alignment |
|---|---|---|---:|---:|---|
| 003670 | Yellow can persist after CAM contract blowoff | guarded Actionable + local 4B recheck | 61.84 | -39.92 | candidate better |
| 066970 | Tesla contract size can over-promote Yellow | Stage2-Watch until real pull/margin bridge | 35.40 | -39.05 | candidate better |
| 011790 | copper-foil demand label can keep positive stage alive | local 4B watch when bridge absent | 27.13 | -45.84 | candidate better |
| 393890 | may remain merely watch | hard 4C when client-demand break is verified | 10.11 | -60.58 | candidate better |
| 121600 | broad EV slowdown could force false 4C | growth-exception filter | 44.47 | -21.56 | candidate better |
| 336370 | copper-foil weakness could force false 4C | customer-diversification exception | 79.33 | -14.71 | candidate better |
| 137400 | equipment backlog can over-promote Yellow | delivery-acceptance bridge required | 17.72 | -42.51 | candidate better |
| 222080 | temporary slowdown can hide revenue conversion | Actionable survives if revenue/margin proves out | 50.86 | -10.15 | candidate better |

## 13. Coverage Matrix

```text
selected_priority_bucket = Priority 1
C12 current rows in No-Repeat Index = 32
prior local C12 loop99 representative triggers = 7
this loop representative trigger rows = 8
local-session adjusted C12 rows after this loop = 47
need to 50 after this loop = 3
new C12 symbols from this loop = 6
new trigger families = 8
positive/counterexample balance = 4/4
4B/4C rows = 3/1
source_proxy_only_count = 3
evidence_url_pending_count = 3
```

## 14. Residual Contribution Summary

This loop adds **8** independent C12 cases, **4** positives or growth exceptions, **4** counterexamples / hard-break rows, and **6** current-profile residual errors.

```text
loop_contribution_label = canonical_archetype_rule_candidate
do_not_propose_new_weight_delta = false
sector_specific_rule_candidate = true
canonical_archetype_rule_candidate = true
```

## 15. Validation Scope / Non-Validation Scope

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

## 16. Machine-Readable Rows

```jsonl
{"row_id": "R3L100-C12-001", "symbol": "003670", "company_name": "POSCO Future M / 포스코퓨처엠", "trigger_type": "Stage2-Actionable", "trigger_family": "cathode_GM_Ultium_CAM_contract_without_sustained_calloff_margin_bridge", "trigger_date": "2023-06-02", "entry_date": "2023-06-05", "entry_price": 369500.0, "MFE_30D_pct": 44.52, "MAE_30D_pct": -4.74, "MFE_90D_pct": 61.84, "MAE_90D_pct": -12.58, "MFE_180D_pct": 61.84, "MAE_180D_pct": -39.92, "MFE_250D_pct": 61.84, "MAE_250D_pct": -47.77, "MFE_500D_pct": 61.84, "MAE_500D_pct": -61.3, "peak_date_180D": "2023-07-26", "peak_price_180D": 598000.0, "trough_date_180D": "2024-01-18", "trough_price_180D": 222000.0, "drawdown_after_peak_180D_pct": -62.88, "case_role": "positive_with_4B_late_cycle_guard", "outcome_label": "positive_contract_bridge_but_requires_late_cycle_4B_watch", "current_profile_error": true, "current_profile_verdict": "current_profile_too_loose_if_CAM_contract_keeps_Yellow_after_calloff_margin_visibility_fades", "baseline_profile_decision": "Stage3-Yellow if GM/Ultium binding agreement and CAM capacity are overweighted", "proposed_profile_decision": "Stage2-Actionable allowed, but Yellow/Green require customer pull, shipment cadence, margin/revision bridge, and local 4B watch after blowoff", "evidence_summary": "POSCO Future M and GM expanded the Ultium CAM project and described a binding supply arrangement. The path produced large MFE, but also a severe post-peak drawdown. C12 should keep the positive bridge while forcing a later customer-pull/margin recheck.", "source_proxy_only": false, "evidence_url_pending": false, "source_urls": ["https://www.poscofuturem.com/en/pr/view.do?num=695", "https://www.gm.ca/content/public/ca/en/gm/home/company/canada/ultium-cam.html", "https://www.kedglobal.com/batteries/newsView/ked202306020015"], "fine_archetype_id": "C12_CATHODE_CUSTOMER_CAM_CONTRACT_CALL_OFF_MARGIN_BRIDGE", "deep_sub_archetype_id": "C12_DEEP_GM_ULTIUM_CAM_CONTRACT_VS_LATE_CYCLE_CALLOFF_MARGIN_FADE", "profile_corporate_action_candidate_count": 2, "corporate_action_candidate_dates": ["2015-05-04", "2021-02-03"], "corporate_action_window_status": "clean_180D_window_old_candidates_only", "new_to_c12_symbol": true, "independent_evidence_weight": 1.0, "case_id": "C12_003670_2023-06-05_STAGE2ACTIONABLE_CATHODE_GM_ULTIUM_CAM_CONTRACT_WITHOUT_SUSTAINED_CALLOFF_MARGIN_BRIDGE", "price_path_anchor_urls": ["https://github.com/Songdaiki/stock-web/blob/main/atlas/ohlcv_tradable_by_symbol_year/003/003670/2023.csv?plain=1", "https://github.com/Songdaiki/stock-web/blob/main/atlas/symbol_profiles/003/003670.json?plain=1"], "do_not_count_as_new_case": false, "row_type": "trigger", "round": "R3", "loop": 100, "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK", "price_data_source": "Songdaiki/stock-web", "price_source": "Songdaiki/stock-web", "upstream_source": "FinanceData/marcap", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "calibration_usable": true, "forward_window_trading_days": 180, "forward_window_status": "complete_180D_within_manifest_max_date", "corporate_action_window_contaminated": false, "same_entry_group_id": "C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK|003670|Stage2-Actionable|2023-06-05", "dedupe_for_aggregate": true, "aggregate_group_role": "representative_case", "representative_trigger": true, "novelty_key": "C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK|003670|Stage2-Actionable|2023-06-05", "dedupe_status": "new_independent_case", "entry_price_field": "close"}
{"row_id": "R3L100-C12-002", "symbol": "066970", "company_name": "L&F / 엘앤에프", "trigger_type": "Stage2-Actionable", "trigger_family": "cathode_Tesla_contract_size_calloff_reduction_guard", "trigger_date": "2023-02-28", "entry_date": "2023-03-02", "entry_price": 274000.0, "MFE_30D_pct": 13.87, "MAE_30D_pct": -6.02, "MFE_90D_pct": 33.58, "MAE_90D_pct": -9.31, "MFE_180D_pct": 35.4, "MAE_180D_pct": -39.05, "MFE_250D_pct": 35.4, "MAE_250D_pct": -49.82, "MFE_500D_pct": 35.4, "MAE_500D_pct": -71.1, "peak_date_180D": "2023-07-26", "peak_price_180D": 371000.0, "trough_date_180D": "2023-11-01", "trough_price_180D": 167000.0, "drawdown_after_peak_180D_pct": -54.99, "case_role": "counterexample", "outcome_label": "counterexample_contract_size_not_durable_customer_pull", "current_profile_error": true, "current_profile_verdict": "current_profile_false_positive_if_contract_size_substitutes_for_confirmed_calloff_and_margin_conversion", "baseline_profile_decision": "Stage3-Yellow if Tesla customer label and contract amount are scored as durable pull", "proposed_profile_decision": "Stage2-Watch or guarded Actionable until actual shipment/call-off, ASP/mix and margin evidence confirm the contract path", "evidence_summary": "The 2023 Tesla high-nickel cathode contract created direct customer visibility, but the later stock path shows why C12 cannot let contract value alone unlock Yellow after the battery cycle has peaked.", "source_proxy_only": false, "evidence_url_pending": false, "source_urls": ["https://www.kedglobal.com/batteries/newsView/ked202302280017", "https://www.reuters.com/world/asia-pacific/south-koreas-lf-says-value-battery-material-supply-deal-with-tesla-cut-7386-2025-12-29/", "https://pulse.mk.co.kr/news/english/11918715"], "fine_archetype_id": "C12_CATHODE_TESLA_SUPPLY_CONTRACT_CALLOFF_REVISION_GUARD", "deep_sub_archetype_id": "C12_DEEP_TESLA_4680_CATHODE_CONTRACT_SIZE_VS_ACTUAL_PULL", "profile_corporate_action_candidate_count": 2, "corporate_action_candidate_dates": ["2016-02-19", "2021-08-11"], "corporate_action_window_status": "clean_180D_window_old_candidates_only", "new_to_c12_symbol": false, "independent_evidence_weight": 0.8, "case_id": "C12_066970_2023-03-02_STAGE2ACTIONABLE_CATHODE_TESLA_CONTRACT_SIZE_CALLOFF_REDUCTION_GUARD", "price_path_anchor_urls": ["https://github.com/Songdaiki/stock-web/blob/main/atlas/ohlcv_tradable_by_symbol_year/066/066970/2023.csv?plain=1", "https://github.com/Songdaiki/stock-web/blob/main/atlas/symbol_profiles/066/066970.json?plain=1"], "do_not_count_as_new_case": false, "row_type": "trigger", "round": "R3", "loop": 100, "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK", "price_data_source": "Songdaiki/stock-web", "price_source": "Songdaiki/stock-web", "upstream_source": "FinanceData/marcap", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "calibration_usable": true, "forward_window_trading_days": 180, "forward_window_status": "complete_180D_within_manifest_max_date", "corporate_action_window_contaminated": false, "same_entry_group_id": "C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK|066970|Stage2-Actionable|2023-03-02", "dedupe_for_aggregate": true, "aggregate_group_role": "representative_case", "representative_trigger": true, "novelty_key": "C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK|066970|Stage2-Actionable|2023-03-02", "dedupe_status": "new_independent_case", "entry_price_field": "close"}
{"row_id": "R3L100-C12-003", "symbol": "011790", "company_name": "SKC / SKC", "trigger_type": "Stage4B", "trigger_family": "copper_foil_customer_calloff_margin_break_to_local_4B_watch", "trigger_date": "2024-03-25", "entry_date": "2024-03-26", "entry_price": 91400.0, "MFE_30D_pct": 14.0, "MAE_30D_pct": -9.52, "MFE_90D_pct": 27.13, "MAE_90D_pct": -16.08, "MFE_180D_pct": 27.13, "MAE_180D_pct": -45.84, "MFE_250D_pct": 27.13, "MAE_250D_pct": -49.56, "MFE_500D_pct": 35.23, "MAE_500D_pct": -54.7, "peak_date_180D": "2024-06-17", "peak_price_180D": 116200.0, "trough_date_180D": "2024-12-09", "trough_price_180D": 49500.0, "drawdown_after_peak_180D_pct": -57.4, "case_role": "counterexample_4B", "outcome_label": "counterexample_local_4B_needed_when_copper_foil_pull_breaks_but_MFE_band_remains", "current_profile_error": true, "current_profile_verdict": "current_profile_false_positive_if_copper_foil_label_remains_Actionable_after_customer_pull_and_margin_pressure", "baseline_profile_decision": "Stage2-Actionable if copper-foil structural demand is over-weighted", "proposed_profile_decision": "Local Stage4B watch after price recovery if customer-pull and margin bridge are not verified; hard 4C only after non-price thesis break", "evidence_summary": "SKC is a copper-foil route into battery customers. The path supports a C12 local 4B guard: a recovery MFE band existed, but the later MAE was too large to let broad customer-contract vocabulary keep a positive stage alive.", "source_proxy_only": true, "evidence_url_pending": true, "source_urls": ["https://biz.chosun.com/en/en-industry/2026/01/20/OBGDFGZFJNCB5F7SYY3Z6K2HWE/", "https://www.umicore.com/en/media/newsroom/slowdown-in-ev-growth-significantly-impacts-2024-outlook-for-umicores-battery-materials-activities/"], "fine_archetype_id": "C12_COPPER_FOIL_CUSTOMER_PULL_MARGIN_GUARD", "deep_sub_archetype_id": "C12_DEEP_COPPER_FOIL_PULL_BREAK_VS_RECOVERY_MFE_BAND", "profile_corporate_action_candidate_count": 2, "corporate_action_candidate_dates": ["1998-01-03", "2001-12-21"], "corporate_action_window_status": "clean_180D_window_old_candidates_only", "new_to_c12_symbol": false, "independent_evidence_weight": 0.7, "case_id": "C12_011790_2024-03-26_STAGE4B_COPPER_FOIL_CUSTOMER_CALLOFF_MARGIN_BREAK_TO_LOCAL_4B_WATCH", "price_path_anchor_urls": ["https://github.com/Songdaiki/stock-web/blob/main/atlas/ohlcv_tradable_by_symbol_year/011/011790/2024.csv?plain=1", "https://github.com/Songdaiki/stock-web/blob/main/atlas/symbol_profiles/011/011790.json?plain=1"], "do_not_count_as_new_case": false, "row_type": "trigger", "round": "R3", "loop": 100, "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK", "price_data_source": "Songdaiki/stock-web", "price_source": "Songdaiki/stock-web", "upstream_source": "FinanceData/marcap", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "calibration_usable": true, "forward_window_trading_days": 180, "forward_window_status": "complete_180D_within_manifest_max_date", "corporate_action_window_contaminated": false, "same_entry_group_id": "C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK|011790|Stage4B|2024-03-26", "dedupe_for_aggregate": true, "aggregate_group_role": "representative_case", "representative_trigger": true, "novelty_key": "C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK|011790|Stage4B|2024-03-26", "dedupe_status": "new_independent_case", "entry_price_field": "close"}
{"row_id": "R3L100-C12-004", "symbol": "393890", "company_name": "WCP / 더블유씨피", "trigger_type": "Stage4C", "trigger_family": "separator_client_demand_stock_rebalancing_hard_4C", "trigger_date": "2024-06-07", "entry_date": "2024-06-10", "entry_price": 27700.0, "MFE_30D_pct": 7.04, "MAE_30D_pct": -22.38, "MFE_90D_pct": 7.04, "MAE_90D_pct": -43.14, "MFE_180D_pct": 10.11, "MAE_180D_pct": -60.58, "MFE_250D_pct": 10.11, "MAE_250D_pct": -65.99, "MFE_500D_pct": 10.11, "MAE_500D_pct": -67.94, "peak_date_180D": "2024-08-01", "peak_price_180D": 30500.0, "trough_date_180D": "2025-02-04", "trough_price_180D": 10920.0, "drawdown_after_peak_180D_pct": -64.2, "case_role": "4C_success", "outcome_label": "hard_4C_supported_when_separator_customer_demand_and_stock_rebalancing_break", "current_profile_error": false, "current_profile_verdict": "current_profile_correct_if_hard_4c_requires_client_demand_or_stock_rebalancing_break", "baseline_profile_decision": "Stage2-Watch if separator capacity is scored without client pull validation", "proposed_profile_decision": "Stage4C when customer demand reduction and stock-rebalancing evidence are verified", "evidence_summary": "Separator demand concerns and client inventory rebalancing are directly C12-like. The forward path shows small MFE and severe MAE, supporting a hard-4C confirmation route once the non-price break is verified.", "source_proxy_only": false, "evidence_url_pending": false, "source_urls": ["https://www.mk.co.kr/en/stock/11035006", "https://www.sneresearch.com/en/insight/release_view/433/page/0"], "fine_archetype_id": "C12_SEPARATOR_CLIENT_DEMAND_STOCK_REBALANCING_4C", "deep_sub_archetype_id": "C12_DEEP_WCP_SEPARATOR_EU_CUSTOMER_STOCK_REBALANCING_BREAK", "profile_corporate_action_candidate_count": 0, "corporate_action_candidate_dates": [], "corporate_action_window_status": "clean_180D_window", "new_to_c12_symbol": true, "independent_evidence_weight": 1.0, "case_id": "C12_393890_2024-06-10_STAGE4C_SEPARATOR_CLIENT_DEMAND_STOCK_REBALANCING_HARD_4C", "price_path_anchor_urls": ["https://github.com/Songdaiki/stock-web/blob/main/atlas/ohlcv_tradable_by_symbol_year/393/393890/2024.csv?plain=1", "https://github.com/Songdaiki/stock-web/blob/main/atlas/symbol_profiles/393/393890.json?plain=1"], "do_not_count_as_new_case": false, "row_type": "trigger", "round": "R3", "loop": 100, "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK", "price_data_source": "Songdaiki/stock-web", "price_source": "Songdaiki/stock-web", "upstream_source": "FinanceData/marcap", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "calibration_usable": true, "forward_window_trading_days": 180, "forward_window_status": "complete_180D_within_manifest_max_date", "corporate_action_window_contaminated": false, "same_entry_group_id": "C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK|393890|Stage4C|2024-06-10", "dedupe_for_aggregate": true, "aggregate_group_role": "representative_case", "representative_trigger": true, "novelty_key": "C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK|393890|Stage4C|2024-06-10", "dedupe_status": "new_independent_case", "entry_price_field": "close"}
{"row_id": "R3L100-C12-005", "symbol": "121600", "company_name": "Advanced Nano Products / 나노신소재", "trigger_type": "Stage4B", "trigger_family": "CNT_conductive_additive_growth_exception_before_hard_4C", "trigger_date": "2024-08-16", "entry_date": "2024-08-19", "entry_price": 89500.0, "MFE_30D_pct": 7.82, "MAE_30D_pct": -14.19, "MFE_90D_pct": 36.98, "MAE_90D_pct": -18.88, "MFE_180D_pct": 44.47, "MAE_180D_pct": -21.56, "MFE_250D_pct": 44.47, "MAE_250D_pct": -25.92, "MFE_500D_pct": 44.47, "MAE_500D_pct": -28.72, "peak_date_180D": "2025-01-06", "peak_price_180D": 129300.0, "trough_date_180D": "2024-11-13", "trough_price_180D": 70200.0, "drawdown_after_peak_180D_pct": -45.71, "case_role": "positive_exception", "outcome_label": "growth_exception_filter_blocks_overbroad_battery_downcycle_4C", "current_profile_error": true, "current_profile_verdict": "current_profile_false_negative_if_generic_battery_calloff_guard_forces_hard_4C_on_CNT_growth_exception", "baseline_profile_decision": "Hard 4C if broad EV-demand slowdown is over-applied", "proposed_profile_decision": "Local Stage4B watch only; growth-exception and customer-expansion bridge must be checked before hard 4C", "evidence_summary": "CNT conductive additive demand can decouple from a generic EV slowdown if customer penetration and revenue mix improve. The row protects C12 from overbroad hard-4C routing.", "source_proxy_only": true, "evidence_url_pending": true, "source_urls": ["https://securities.miraeasset.com/bbs/download/2130623.pdf?attachmentId=2130623", "https://www.idtechex.com/ko/research-report/carbon-nanotubes-2025/1099"], "fine_archetype_id": "C12_CNT_CONDUCTIVE_ADDITIVE_GROWTH_EXCEPTION_FILTER", "deep_sub_archetype_id": "C12_DEEP_CNT_CUSTOMER_PENETRATION_VS_GENERIC_EV_SLOWDOWN", "profile_corporate_action_candidate_count": 1, "corporate_action_candidate_dates": ["2015-12-17"], "corporate_action_window_status": "clean_180D_window_old_candidates_only", "new_to_c12_symbol": true, "independent_evidence_weight": 0.8, "case_id": "C12_121600_2024-08-19_STAGE4B_CNT_CONDUCTIVE_ADDITIVE_GROWTH_EXCEPTION_BEFORE_HARD_4C", "price_path_anchor_urls": ["https://github.com/Songdaiki/stock-web/blob/main/atlas/ohlcv_tradable_by_symbol_year/121/121600/2024.csv?plain=1", "https://github.com/Songdaiki/stock-web/blob/main/atlas/symbol_profiles/121/121600.json?plain=1"], "do_not_count_as_new_case": false, "row_type": "trigger", "round": "R3", "loop": 100, "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK", "price_data_source": "Songdaiki/stock-web", "price_source": "Songdaiki/stock-web", "upstream_source": "FinanceData/marcap", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "calibration_usable": true, "forward_window_trading_days": 180, "forward_window_status": "complete_180D_within_manifest_max_date", "corporate_action_window_contaminated": false, "same_entry_group_id": "C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK|121600|Stage4B|2024-08-19", "dedupe_for_aggregate": true, "aggregate_group_role": "representative_case", "representative_trigger": true, "novelty_key": "C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK|121600|Stage4B|2024-08-19", "dedupe_status": "new_independent_case", "entry_price_field": "close"}
{"row_id": "R3L100-C12-006", "symbol": "336370", "company_name": "Solus Advanced Materials / 솔루스첨단소재", "trigger_type": "Stage4B", "trigger_family": "copper_foil_customer_diversification_growth_exception_before_hard_4C", "trigger_date": "2024-10-23", "entry_date": "2024-10-24", "entry_price": 10400.0, "MFE_30D_pct": 32.21, "MAE_30D_pct": -6.25, "MFE_90D_pct": 56.25, "MAE_90D_pct": -10.1, "MFE_180D_pct": 79.33, "MAE_180D_pct": -14.71, "MFE_250D_pct": 79.33, "MAE_250D_pct": -18.65, "MFE_500D_pct": 79.33, "MAE_500D_pct": -21.92, "peak_date_180D": "2025-03-04", "peak_price_180D": 18650.0, "trough_date_180D": "2024-11-13", "trough_price_180D": 8870.0, "drawdown_after_peak_180D_pct": -52.44, "case_role": "positive_exception", "outcome_label": "customer_diversification_recovery_exception_blocks_false_hard_4C", "current_profile_error": true, "current_profile_verdict": "current_profile_false_negative_if_EV_downcycle_calloff_guard_ignores_customer_diversification_and_recovery", "baseline_profile_decision": "Hard 4C or blocked Stage2 if all copper foil is treated as customer-calloff failure", "proposed_profile_decision": "Local Stage4B watch only; require actual customer loss/margin break before hard 4C", "evidence_summary": "Battery copper foil recovery and customer diversification evidence can keep the C12 thesis alive. This row is a false-hard-4C exception rather than a positive global unlock.", "source_proxy_only": false, "evidence_url_pending": false, "source_urls": ["https://www.asiae.co.kr/en/article/2024102314004483747", "https://www.solusadvancedmaterials.com/en/intro/intro/", "https://www.thelec.net/news/articleView.html?idxno=10094"], "fine_archetype_id": "C12_COPPER_FOIL_CUSTOMER_DIVERSIFICATION_EXCEPTION", "deep_sub_archetype_id": "C12_DEEP_SOLUS_COPPER_FOIL_CUSTOMER_EXPANSION_VS_EV_DOWNTURN", "profile_corporate_action_candidate_count": 2, "corporate_action_candidate_dates": ["2024-01-08", "2024-01-30"], "corporate_action_window_status": "clean_180D_window_after_Jan2024_candidates", "new_to_c12_symbol": true, "independent_evidence_weight": 1.0, "case_id": "C12_336370_2024-10-24_STAGE4B_COPPER_FOIL_CUSTOMER_DIVERSIFICATION_GROWTH_EXCEPTION_BEFORE_HARD_4C", "price_path_anchor_urls": ["https://github.com/Songdaiki/stock-web/blob/main/atlas/ohlcv_tradable_by_symbol_year/336/336370/2024.csv?plain=1", "https://github.com/Songdaiki/stock-web/blob/main/atlas/symbol_profiles/336/336370.json?plain=1"], "do_not_count_as_new_case": false, "row_type": "trigger", "round": "R3", "loop": 100, "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK", "price_data_source": "Songdaiki/stock-web", "price_source": "Songdaiki/stock-web", "upstream_source": "FinanceData/marcap", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "calibration_usable": true, "forward_window_trading_days": 180, "forward_window_status": "complete_180D_within_manifest_max_date", "corporate_action_window_contaminated": false, "same_entry_group_id": "C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK|336370|Stage4B|2024-10-24", "dedupe_for_aggregate": true, "aggregate_group_role": "representative_case", "representative_trigger": true, "novelty_key": "C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK|336370|Stage4B|2024-10-24", "dedupe_status": "new_independent_case", "entry_price_field": "close"}
{"row_id": "R3L100-C12-007", "symbol": "137400", "company_name": "PNT / 피엔티", "trigger_type": "Stage2-Actionable", "trigger_family": "battery_equipment_backlog_customer_delivery_delay_calloff_guard", "trigger_date": "2024-06-14", "entry_date": "2024-06-17", "entry_price": 69400.0, "MFE_30D_pct": 13.4, "MAE_30D_pct": -8.2, "MFE_90D_pct": 13.4, "MAE_90D_pct": -25.65, "MFE_180D_pct": 17.72, "MAE_180D_pct": -42.51, "MFE_250D_pct": 17.72, "MAE_250D_pct": -48.85, "MFE_500D_pct": 17.72, "MAE_500D_pct": -54.03, "peak_date_180D": "2024-07-03", "peak_price_180D": 81700.0, "trough_date_180D": "2024-12-09", "trough_price_180D": 39900.0, "drawdown_after_peak_180D_pct": -51.16, "case_role": "counterexample", "outcome_label": "equipment_backlog_not_same_as_customer_pull_or_delivery_acceptance", "current_profile_error": true, "current_profile_verdict": "current_profile_false_positive_if_battery_equipment_backlog_is_treated_as_completed_customer_pull", "baseline_profile_decision": "Stage3-Yellow if equipment backlog and customer diversification are overweighted", "proposed_profile_decision": "Stage2-Actionable only; block Yellow until delivery acceptance, customer capex schedule, revenue and margin bridge are visible", "evidence_summary": "Battery-equipment backlog can still be vulnerable to customer delivery timing and capex schedule. C12 should not let backlog vocabulary substitute for customer pull and delivery acceptance.", "source_proxy_only": true, "evidence_url_pending": true, "source_urls": ["https://securities.miraeasset.com/bbs/download/2128649.pdf?attachmentId=2128649", "https://www.businesskorea.co.kr/news/articleView.html?idxno=260255", "https://www.epnt.co.kr/en/m22.php"], "fine_archetype_id": "C12_BATTERY_EQUIPMENT_BACKLOG_DELIVERY_ACCEPTANCE_GUARD", "deep_sub_archetype_id": "C12_DEEP_PNT_BACKLOG_CUSTOMER_DELIVERY_DELAY_VS_REVENUE_MARGIN_BRIDGE", "profile_corporate_action_candidate_count": 4, "corporate_action_candidate_dates": ["2012-11-30", "2012-12-26", "2019-05-07", "2019-05-30"], "corporate_action_window_status": "clean_180D_window_old_candidates_only", "new_to_c12_symbol": true, "independent_evidence_weight": 0.8, "case_id": "C12_137400_2024-06-17_STAGE2ACTIONABLE_BATTERY_EQUIPMENT_BACKLOG_CUSTOMER_DELIVERY_DELAY_CALLOFF_GUARD", "price_path_anchor_urls": ["https://github.com/Songdaiki/stock-web/blob/main/atlas/ohlcv_tradable_by_symbol_year/137/137400/2024.csv?plain=1", "https://github.com/Songdaiki/stock-web/blob/main/atlas/symbol_profiles/137/137400.json?plain=1"], "do_not_count_as_new_case": false, "row_type": "trigger", "round": "R3", "loop": 100, "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK", "price_data_source": "Songdaiki/stock-web", "price_source": "Songdaiki/stock-web", "upstream_source": "FinanceData/marcap", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "calibration_usable": true, "forward_window_trading_days": 180, "forward_window_status": "complete_180D_within_manifest_max_date", "corporate_action_window_contaminated": false, "same_entry_group_id": "C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK|137400|Stage2-Actionable|2024-06-17", "dedupe_for_aggregate": true, "aggregate_group_role": "representative_case", "representative_trigger": true, "novelty_key": "C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK|137400|Stage2-Actionable|2024-06-17", "dedupe_status": "new_independent_case", "entry_price_field": "close"}
{"row_id": "R3L100-C12-008", "symbol": "222080", "company_name": "CIS / 씨아이에스", "trigger_type": "Stage2-Actionable", "trigger_family": "battery_equipment_temporary_slowdown_revenue_conversion_exception", "trigger_date": "2025-02-14", "entry_date": "2025-02-17", "entry_price": 8180.0, "MFE_30D_pct": 15.28, "MAE_30D_pct": -7.7, "MFE_90D_pct": 31.17, "MAE_90D_pct": -10.15, "MFE_180D_pct": 50.86, "MAE_180D_pct": -10.15, "MFE_250D_pct": 50.86, "MAE_250D_pct": -13.08, "MFE_500D_pct": 50.86, "MAE_500D_pct": -18.58, "peak_date_180D": "2025-08-05", "peak_price_180D": 12340.0, "trough_date_180D": "2025-03-07", "trough_price_180D": 7350.0, "drawdown_after_peak_180D_pct": -40.44, "case_role": "positive_exception", "outcome_label": "temporary_demand_slowdown_can_be_positive_when_revenue_conversion_proves_out", "current_profile_error": true, "current_profile_verdict": "current_profile_too_conservative_if_temporary_slowdown_blocks_revenue_conversion_exception", "baseline_profile_decision": "Blocked or 4B if all battery equipment is treated as call-off risk", "proposed_profile_decision": "Stage2-Actionable can proceed when revenue conversion, backlog delivery and margin evidence survive the temporary slowdown", "evidence_summary": "CIS reported record revenue despite a temporary demand slowdown. This is the mirror image of C12 false positives: customer/capex weakness should not block a verified revenue-conversion exception.", "source_proxy_only": false, "evidence_url_pending": false, "source_urls": ["https://biz.chosun.com/en/en-industry/2025/02/14/5JD7V2GTVJC7DMIS3M2VZV2IYI/", "https://www.mk.co.kr/en/society/11312691"], "fine_archetype_id": "C12_BATTERY_EQUIPMENT_REVENUE_CONVERSION_EXCEPTION", "deep_sub_archetype_id": "C12_DEEP_CIS_TEMPORARY_SLOWDOWN_VS_REVENUE_CONVERSION_EXCEPTION", "profile_corporate_action_candidate_count": 1, "corporate_action_candidate_dates": ["2017-01-20"], "corporate_action_window_status": "clean_180D_window_old_candidates_only", "new_to_c12_symbol": true, "independent_evidence_weight": 1.0, "case_id": "C12_222080_2025-02-17_STAGE2ACTIONABLE_BATTERY_EQUIPMENT_TEMPORARY_SLOWDOWN_REVENUE_CONVERSION_EXCEPTION", "price_path_anchor_urls": ["https://github.com/Songdaiki/stock-web/blob/main/atlas/ohlcv_tradable_by_symbol_year/222/222080/2025.csv?plain=1", "https://github.com/Songdaiki/stock-web/blob/main/atlas/symbol_profiles/222/222080.json?plain=1"], "do_not_count_as_new_case": false, "row_type": "trigger", "round": "R3", "loop": 100, "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK", "price_data_source": "Songdaiki/stock-web", "price_source": "Songdaiki/stock-web", "upstream_source": "FinanceData/marcap", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "calibration_usable": true, "forward_window_trading_days": 180, "forward_window_status": "complete_180D_within_manifest_max_date", "corporate_action_window_contaminated": false, "same_entry_group_id": "C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK|222080|Stage2-Actionable|2025-02-17", "dedupe_for_aggregate": true, "aggregate_group_role": "representative_case", "representative_trigger": true, "novelty_key": "C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK|222080|Stage2-Actionable|2025-02-17", "dedupe_status": "new_independent_case", "entry_price_field": "close"}
{"row_type": "score_simulation", "symbol": "003670", "canonical_archetype_id": "C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK", "entry_date": "2023-06-05", "current_proxy_stage": "Stage2/Yellow without late 4B guard", "candidate_stage": "Stage2-Actionable / guarded Yellow", "current_proxy_score": 76, "candidate_C12_guarded_score": 64, "delta": -4, "decision_reason": "current_profile_too_loose_if_CAM_contract_keeps_Yellow_after_calloff_margin_visibility_fades"}
{"row_type": "score_simulation", "symbol": "066970", "canonical_archetype_id": "C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK", "entry_date": "2023-03-02", "current_proxy_stage": "Stage3-Yellow if contract/backlog overweighted", "candidate_stage": "Stage2-Watch / guarded Actionable", "current_proxy_score": 76, "candidate_C12_guarded_score": 64, "delta": -12, "decision_reason": "current_profile_false_positive_if_contract_size_substitutes_for_confirmed_calloff_and_margin_conversion"}
{"row_type": "score_simulation", "symbol": "011790", "canonical_archetype_id": "C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK", "entry_date": "2024-03-26", "current_proxy_stage": "Stage2-Actionable / Yellow if bridge overweighted", "candidate_stage": "local Stage4B watch", "current_proxy_score": 76, "candidate_C12_guarded_score": 30, "delta": -16, "decision_reason": "current_profile_false_positive_if_copper_foil_label_remains_Actionable_after_customer_pull_and_margin_pressure"}
{"row_type": "score_simulation", "symbol": "393890", "canonical_archetype_id": "C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK", "entry_date": "2024-06-10", "current_proxy_stage": "Stage2-Watch / late 4B", "candidate_stage": "Stage4C", "current_proxy_score": 45, "candidate_C12_guarded_score": 30, "delta": -25, "decision_reason": "current_profile_correct_if_hard_4c_requires_client_demand_or_stock_rebalancing_break"}
{"row_type": "score_simulation", "symbol": "121600", "canonical_archetype_id": "C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK", "entry_date": "2024-08-19", "current_proxy_stage": "hard-4C / blocked / too cautious", "candidate_stage": "local Stage4B watch, not hard 4C", "current_proxy_score": 45, "candidate_C12_guarded_score": 30, "delta": 10, "decision_reason": "current_profile_false_negative_if_generic_battery_calloff_guard_forces_hard_4C_on_CNT_growth_exception"}
{"row_type": "score_simulation", "symbol": "336370", "canonical_archetype_id": "C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK", "entry_date": "2024-10-24", "current_proxy_stage": "hard-4C / blocked / too cautious", "candidate_stage": "local Stage4B watch, not hard 4C", "current_proxy_score": 45, "candidate_C12_guarded_score": 30, "delta": 10, "decision_reason": "current_profile_false_negative_if_EV_downcycle_calloff_guard_ignores_customer_diversification_and_recovery"}
{"row_type": "score_simulation", "symbol": "137400", "canonical_archetype_id": "C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK", "entry_date": "2024-06-17", "current_proxy_stage": "Stage3-Yellow if contract/backlog overweighted", "candidate_stage": "Stage2-Watch / guarded Actionable", "current_proxy_score": 76, "candidate_C12_guarded_score": 64, "delta": -12, "decision_reason": "current_profile_false_positive_if_battery_equipment_backlog_is_treated_as_completed_customer_pull"}
{"row_type": "score_simulation", "symbol": "222080", "canonical_archetype_id": "C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK", "entry_date": "2025-02-17", "current_proxy_stage": "hard-4C / blocked / too cautious", "candidate_stage": "Stage2-Actionable / guarded Yellow", "current_proxy_score": 45, "candidate_C12_guarded_score": 64, "delta": 10, "decision_reason": "current_profile_too_conservative_if_temporary_slowdown_blocks_revenue_conversion_exception"}
{"row_type": "stage_transition", "row_id": "R3L100-C12-001", "symbol": "003670", "canonical_archetype_id": "C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK", "trigger_type": "Stage2-Actionable", "entry_date": "2023-06-05", "transition_label": "positive_exception_or_guarded_Yellow_supported", "mfe_mae_180_spread_pct": 21.92, "profile_residual": "current_profile_too_loose_if_CAM_contract_keeps_Yellow_after_calloff_margin_visibility_fades"}
{"row_type": "stage_transition", "row_id": "R3L100-C12-002", "symbol": "066970", "canonical_archetype_id": "C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK", "trigger_type": "Stage2-Actionable", "entry_date": "2023-03-02", "transition_label": "Stage2_false_positive_or_Yellow_block_supported", "mfe_mae_180_spread_pct": -3.65, "profile_residual": "current_profile_false_positive_if_contract_size_substitutes_for_confirmed_calloff_and_margin_conversion"}
{"row_type": "stage_transition", "row_id": "R3L100-C12-003", "symbol": "011790", "canonical_archetype_id": "C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK", "trigger_type": "Stage4B", "entry_date": "2024-03-26", "transition_label": "local_4B_watch_or_false_hard_4C_exception", "mfe_mae_180_spread_pct": -18.71, "profile_residual": "current_profile_false_positive_if_copper_foil_label_remains_Actionable_after_customer_pull_and_margin_pressure"}
{"row_type": "stage_transition", "row_id": "R3L100-C12-004", "symbol": "393890", "canonical_archetype_id": "C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK", "trigger_type": "Stage4C", "entry_date": "2024-06-10", "transition_label": "hard_4C_confirmation_supported", "mfe_mae_180_spread_pct": -50.47, "profile_residual": "current_profile_correct_if_hard_4c_requires_client_demand_or_stock_rebalancing_break"}
{"row_type": "stage_transition", "row_id": "R3L100-C12-005", "symbol": "121600", "canonical_archetype_id": "C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK", "trigger_type": "Stage4B", "entry_date": "2024-08-19", "transition_label": "local_4B_watch_or_false_hard_4C_exception", "mfe_mae_180_spread_pct": 22.91, "profile_residual": "current_profile_false_negative_if_generic_battery_calloff_guard_forces_hard_4C_on_CNT_growth_exception"}
{"row_type": "stage_transition", "row_id": "R3L100-C12-006", "symbol": "336370", "canonical_archetype_id": "C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK", "trigger_type": "Stage4B", "entry_date": "2024-10-24", "transition_label": "local_4B_watch_or_false_hard_4C_exception", "mfe_mae_180_spread_pct": 64.62, "profile_residual": "current_profile_false_negative_if_EV_downcycle_calloff_guard_ignores_customer_diversification_and_recovery"}
{"row_type": "stage_transition", "row_id": "R3L100-C12-007", "symbol": "137400", "canonical_archetype_id": "C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK", "trigger_type": "Stage2-Actionable", "entry_date": "2024-06-17", "transition_label": "Stage2_false_positive_or_Yellow_block_supported", "mfe_mae_180_spread_pct": -24.79, "profile_residual": "current_profile_false_positive_if_battery_equipment_backlog_is_treated_as_completed_customer_pull"}
{"row_type": "stage_transition", "row_id": "R3L100-C12-008", "symbol": "222080", "canonical_archetype_id": "C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK", "trigger_type": "Stage2-Actionable", "entry_date": "2025-02-17", "transition_label": "positive_exception_or_guarded_Yellow_supported", "mfe_mae_180_spread_pct": 40.71, "profile_residual": "current_profile_too_conservative_if_temporary_slowdown_blocks_revenue_conversion_exception"}
{"row_type": "shadow_weight", "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK", "scope": "canonical_archetype_specific", "proposed_rule_id": "C12_customer_pull_delivery_acceptance_margin_fcf_bridge_required_before_Yellow", "direction": "tighten_promotion_bridge", "target_stage": "Stage2-Actionable_to_Stage3-Yellow", "supporting_rows": ["R3L100-C12-002", "R3L100-C12-003", "R3L100-C12-007"], "counterbalance_rows": ["R3L100-C12-001", "R3L100-C12-005", "R3L100-C12-006", "R3L100-C12-008"], "max_shadow_delta": "-8_to_-15_score_when_customer_pull_or_margin_bridge_absent", "do_not_apply_globally": true}
{"row_type": "shadow_weight", "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK", "scope": "canonical_archetype_specific", "proposed_rule_id": "C12_growth_exception_filter_before_hard_4C", "direction": "block_overbroad_hard_4c", "target_stage": "Stage4C", "supporting_rows": ["R3L100-C12-005", "R3L100-C12-006", "R3L100-C12-008"], "counterbalance_rows": ["R3L100-C12-004"], "max_shadow_delta": "Stage4C_to_local_4B_watch_when_no_non_price_calloff_or_margin_break", "do_not_apply_globally": true}
{"row_type": "residual_contribution", "selected_round": "R3", "selected_loop": 100, "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK", "new_independent_case_count": 8, "reused_case_count": 0, "new_symbol_count": 6, "same_archetype_new_symbol_count": 6, "same_archetype_new_trigger_family_count": 8, "new_trigger_family_count": 8, "positive_case_count": 4, "counterexample_count": 4, "stage4b_case_count": 3, "stage4c_case_count": 1, "current_profile_error_count": 6, "source_proxy_only_count": 3, "evidence_url_pending_count": 3, "loop_contribution_label": "canonical_archetype_rule_candidate", "do_not_propose_new_weight_delta": false, "new_axis_proposed": "C12_customer_pull_delivery_acceptance_margin_fcf_bridge_required_before_Yellow_plus_growth_exception_filter_before_hard_4C", "existing_axis_strengthened": "stage2_required_bridge, hard_4c_confirmation, local_4b_watch_guard, full_4b_requires_non_price_evidence", "existing_axis_weakened": "hard_4c_thesis_break_routes_to_4c_when_only_generic_EV_slowdown_or_backlog_label_is_present"}
```

## 17. Batch Ingest Self-Audit

```text
expected_v12_result_file: true
filename_pattern_pass: true
metadata_filename_consistency: pass
jsonl_trigger_row_count: 8
calibration_usable_trigger_count: 8
representative_trigger_count: 8
new_weight_evidence_candidate_count: 8
guardrail_candidate_count: 5
narrative_only_or_rejected_count: 0
rows_missing_required_mfe_mae: 0
rows_missing_entry_price_or_date: 0
rows_with_noncanonical_trigger_type: 0
rows_with_compact_mfe_mae_alias_only: 0
ready_for_batch_ingest: true
```

## 18. Deferred Coding Agent Handoff Prompt

### Purpose

You are now in the repository implementation phase. The attached Markdown files are v12 post-calibrated residual research outputs produced using the Songdaiki/stock-web OHLC atlas. These MDs are not live candidate research. They are historical calibration research designed to extend the already-applied calibrated profile. Do not blindly apply every shadow row. Ingest the machine-readable rows and update the sector/canonical-archetype calibration ledger.

### Price source context

- Primary historical price source used by the research MD: Songdaiki/stock-web.
- Price basis: tradable_raw.
- Price adjustment status: raw_unadjusted_marcap.
- Price shard pattern: atlas/ohlcv_tradable_by_symbol_year/{prefix}/{symbol}/{year}.csv.
- Symbol profile pattern: atlas/symbol_profiles/{prefix}/{symbol}.json.

### Rules

1. Use only `calibration_usable=true` rows for quantitative calibration.
2. Do not count reused symbols as duplicate if `same_entry_group_id` is new.
3. Do not apply global deltas unless multiple large sectors support the same direction.
4. Prefer sector-specific or canonical-archetype-specific shadow profiles.
5. Positive score promotion requires non-price evidence and clean 180D MFE/MAE.
6. 4B rows are overlay/risk calibration only.
7. 4C rows are thesis-break/protection calibration only.
8. Price-only rows cannot promote Stage2/Stage3.
9. If a v12 MD weakens an already applied axis, log it as residual counterexample rather than immediately reverting.
10. Production scoring must not change unless the user explicitly asks for another promotion batch.

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

## 19. Next Round State

```text
completed_round = R3
completed_loop = 100
selection_basis = docs/core/V12_Research_No_Repeat_Index.md
selected_priority_bucket = Priority 1
next_recommended_archetypes = C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK, C02_POWER_GRID_DATACENTER_CAPEX, C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF, C14_EV_DEMAND_SLOWDOWN_4B_4C, C06_HBM_MEMORY_CUSTOMER_CAPACITY
round_schedule_status = coverage_index_selected
round_sector_consistency = pass
```

## 20. Source Notes

- Price atlas: Songdaiki/stock-web.
- Upstream source: FinanceData/marcap.
- Price basis: tradable_raw.
- Price adjustment status: raw_unadjusted_marcap.
- This file is historical calibration research only and is not a current investment recommendation.
