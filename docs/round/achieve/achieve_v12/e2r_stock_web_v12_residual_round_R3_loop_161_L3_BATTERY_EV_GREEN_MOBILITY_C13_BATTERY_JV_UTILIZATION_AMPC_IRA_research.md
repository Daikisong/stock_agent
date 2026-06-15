# E2R Stock-Web v12 Residual Research — R3 loop 161 — C13 Battery JV Utilization / AMPC / IRA

```text
completed_round = R3
completed_loop = 161
selection_basis = docs/core/V12_Research_No_Repeat_Index.md
selected_priority_bucket = Priority 2 quality-repair after session-aware P0/P1 clearing
round_schedule_status = coverage_index_selected_not_sequential
round_sector_consistency = pass
large_sector_id = L3_BATTERY_EV_GREEN_MOBILITY
canonical_archetype_id = C13_BATTERY_JV_UTILIZATION_AMPC_IRA
fine_archetype_id = mixed_c13_ampc_optical_profit_jv_utilization_reset_leaf_set
output_filename = e2r_stock_web_v12_residual_round_R3_loop_161_L3_BATTERY_EV_GREEN_MOBILITY_C13_BATTERY_JV_UTILIZATION_AMPC_IRA_research.md
```

## 1. Scope guard

This research follows the E2R Historical Calibration Prompt v12. It is not a live candidate scan, not a broker/API task, not a `stock_agent` code patch, and not a production scoring change. The only output is this standalone historical calibration Markdown file using actual `Songdaiki/stock-web` 1D OHLCV rows.

```text
production_scoring_changed = false
shadow_weight_only = true
stock_agent_code_patch_allowed = false
stock_agent_live_scan_allowed = false
must_use_actual_stock_web_1D_OHLC = true
must_include_complete_30_90_180_mfe_mae_in_every_trigger_row = true
```

## 2. Coverage-index selection rationale

The original No-Repeat Index shows `C13_BATTERY_JV_UTILIZATION_AMPC_IRA` at 58 rows, above the 50-row minimum but still one of the thinnest Priority 2 archetypes after this session's P0/P1 clearing and after C08/C19/C25 quality-repair passes. This loop is therefore not an expansion pass for an under-30 bucket; it is a quality-repair pass focused on a recurring C13 residual: AMPC/IRA and JV headlines often create accounting-looking operating profit before true utilization, call-off, and ex-credit profitability are durable.

```text
index_baseline_coverage_before = C13 rows 58
index_baseline_coverage_after_if_accepted = C13 rows 65
selection_reason = Priority 2 quality repair; AMPC optical profit vs utilization/call-off conversion stress test
new_independent_case_count = 7
reused_case_count = 0
same_archetype_new_symbol_count = 2
same_archetype_new_trigger_family_count = 7
narrative_only_blocked_case_count = 1  # SK Innovation/SK On candidate blocked by stock-web corporate-action window
```

## 3. Price source validation

```text
price_source = Songdaiki/stock-web
source_basis = FinanceData/marcap transformed into assistant-readable symbol-year CSV shards
price_basis = tradable_raw
price_adjustment_status = raw_unadjusted_marcap
calibration_shard_root = atlas/ohlcv_tradable_by_symbol_year
stock_web_manifest_max_date = 2026-02-20
entry_price_rule = entry_date close column c
MFE_MAE_rule = max high / min low after entry_date through 30/90/180 trading rows
```

Profile check:

```text
373220 LG에너지솔루션: active_like, last_date 2026-02-20, corporate_action_candidate_count = 0, usable for 2024~2025 trigger windows.
006400 삼성SDI: active_like, last_date 2026-02-20, corporate_action_candidate_dates = 1996-01-03|1998-11-03|2014-07-15; no overlap with 2024~2025 180D windows.
096770 SK이노베이션/SK On: profile has corporate_action_candidate_date = 2024-11-20; Q3-2024 SK On first-profit row is kept narrative-only/blocked because the candidate date overlaps the 180D window.
```

## 4. Human-readable case table

| case | symbol | company | role | trigger | entry/price | 30D MFE/MAE | 90D MFE/MAE | 180D MFE/MAE | verdict |
|---|---:|---|---|---|---|---:|---:|---:|---|
| C13-L161-CASE01-373220-LGES-Q1-2024-AMPC-CAPEX-CUT | 373220 | LG에너지솔루션 | counterexample / high-MAE watch | Stage2 2024-04-26 | 2024-04-26 / 372000 | 6.72 / -12.37 | 12.63 / -16.4 | 19.35 / -16.4 | current_profile_false_positive_if_AMPC_prevents_loss_but_utilization_capex_signal_is_weak |
| C13-L161-CASE02-373220-LGES-Q2-2024-REVENUE-CUT-RESET | 373220 | LG에너지솔루션 | positive / false-hard-4C reset | 4C-Watch 2024-07-26 | 2024-07-26 / 325000 | 28.92 / -4.31 | 36.62 / -4.31 | 36.62 / -4.46 | current_profile_too_bearish_if_revenue_cut_is_already_priced_and_IRA_geopolitical_offset_remains |
| C13-L161-CASE03-373220-LGES-Q3-2024-IRA-OPTICAL-PROFIT | 373220 | LG에너지솔루션 | counterexample / AMPC optical-profit trap | Stage2-Actionable 2024-10-29 | 2024-10-29 / 409000 | 6.48 / -9.29 | 6.48 / -20.54 | 6.48 / -34.96 | current_profile_false_positive_if_IRA_credit_is_counted_without_ex_IRA_operating_profit_or_utilization_durability |
| C13-L161-CASE04-373220-LGES-Q1-2025-AMPC-ESS-RESET | 373220 | LG에너지솔루션 | positive / staged-entry high-MAE | Stage2-Watch 2025-04-30 | 2025-04-30 / 324500 | 1.39 / -18.03 | 24.19 / -18.03 | 62.4 / -18.03 | current_profile_too_late_if_cost_cutting_capacity_reallocation_and_AMPC_support_are_seen_only_after_clean_OP_confirmation |
| C13-L161-CASE05-006400-SAMSUNGSDI-HUNGARY-UTILIZATION-2024 | 006400 | 삼성SDI | positive / utilization-to-MFE with exit guard | Stage2-Actionable 2024-01-31 | 2024-01-31 / 372500 | 25.77 / -2.55 | 32.75 / -2.55 | 32.75 / -20.94 | current_profile_correct_but_needs_180D_exit_guard_when_utilization_signal_lacks_AMPC_revenue_conversion |
| C13-L161-CASE06-006400-SAMSUNGSDI-STARPLUS-DOE-LOAN | 006400 | 삼성SDI | counterexample / JV funding headline | Stage2 2024-12-04 | 2024-12-04 / 259000 | 3.47 / -11.39 | 3.47 / -34.36 | 3.47 / -39.11 | current_profile_false_positive_if_ATVM_or_JV_funding_is_promoted_without_near_term_utilization_and_calloff_visibility |
| C13-L161-CASE07-006400-SAMSUNGSDI-Q1-2025-LOSS-RESET | 006400 | 삼성SDI | positive / false-hard-4C reset | 4C-Watch 2025-04-28 | 2025-04-28 / 184200 | 0.71 / -14.39 | 27.04 / -14.39 | 118.24 / -14.39 | current_profile_too_bearish_if_Q1_loss_is_used_as_hard_4C_without_JV_yield_ESS_new_order_offset |

## 5. Case notes

### CASE01 — LG Energy Solution / 373220 — AMPC prevents accounting loss but does not prove utilization

LGES's Q1 2024 trigger is a C13 trap. The company had operating profit, but the evidence also said the quarter would have been a loss without the IRA credit and that capex would be minimized because EV demand had slowed. The price path gave only 19.35% 180D MFE with -16.40% MAE. That is not clean Stage2-Actionable; it is a watch row requiring ex-AMPC profitability and utilization confirmation.

### CASE02 — LG Energy Solution / 373220 — negative guidance reset became a false-hard-4C positive

The Q2 2024 Reuters trigger looked ugly: revenue guidance cut, expansion pace slowed, IRA credit estimate reduced. But the stock-web path from the next trading day produced 36.62% 90D/180D MFE with shallow -4.31% 90D MAE. C13 must therefore avoid firing hard 4C on demand-slowdown vocabulary alone when price has already reset and China-supply-chain/IRA policy offsets remain.

### CASE03 — LG Energy Solution / 373220 — Q3 2024 optical profit fails the ex-credit bridge

The Q3 2024 release is the cleanest negative calibration row. Reported operating profit was strong, but the release itself stated that the profit included KRW 466bn of IRA tax credit and would have been an operating loss excluding the credit. The stock-web path had only 6.48% 180D MFE and -34.96% 180D MAE. This is the exact residual rule: AMPC should not be treated as equivalent to durable utilization-adjusted operating leverage.

### CASE04 — LG Energy Solution / 373220 — 2025 AMPC/ESS reset worked, but only with staged-entry language

The Q1 2025 trigger worked over 180D: 62.40% MFE. But the path still first suffered -18.03% 30D/90D/180D MAE. The evidence was better than 2024 Q3 because it combined cost-cutting, capacity reallocation, North America shipments, ESS/LFP direction, and AMPC support. That deserves Stage2-Watch or staged Stage2-Actionable, not immediate Green.

### CASE05 — Samsung SDI / 006400 — utilization signal worked early but decayed by 180D

Samsung SDI's early-2024 utilization/Hungary plant signal produced 25.77% 30D MFE and 32.75% 90D MFE. The same row later carried -20.94% 180D MAE. The correct C13 treatment is not to ignore utilization, but to pair it with exit discipline: if JV/utilization evidence is not followed by AMPC/revenue/margin conversion, 4B watch should arrive before the 180D decay.

### CASE06 — Samsung SDI / 006400 — StarPlus/DOE loan headline lacked near-term utilization

The December 2024 StarPlus Energy loan headline was a classic C13 headline-risk row. It pointed to future U.S. capacity and policy support, but the path produced only 3.47% 180D MFE and -39.11% 180D MAE. C13 should score conditional loans, future JV capacity, and ATVM/IRA headlines as Stage2-Watch unless they are tied to current call-off, yield, shipment, or AMPC revenue recognition.

### CASE07 — Samsung SDI / 006400 — Q1 loss was a false-hard-4C once price was already reset

Samsung SDI's Q1 2025 release showed a KRW 434.1bn operating loss, lower utilization, and inventory-adjustment pressure. Yet the same release also reported early operations/high yield at the Stellantis JV and GM JV construction. The stock-web path produced 118.24% 180D MFE from a depressed entry. C13 must therefore distinguish unoffset utilization collapse from reset-price situations where JV/ESS/product offsets remain alive.

### Narrative-only blocked row — SK Innovation / 096770 — SK On first profit but corporate-action contaminated window

SK Innovation/SK On is analytically important for C13 because SK On achieved its first quarterly profit in Q3 2024 and disclosed AMPC benefit. However, the stock-web profile has a `corporate_action_candidate_date = 2024-11-20`, which overlaps the Q3 2024 180D forward window. This row is therefore retained as narrative-only and excluded from calibration aggregate.

## 6. Score-return alignment and residual rule

```text
calibration_usable_trigger_count = 7
representative_trigger_count = 7
positive_case_count = 4
counterexample_count = 3
4B_watch_or_overlay_count = 5
4C_or_false4C_audit_count = 3
current_profile_error_count = 5
avg_MFE_90D_pct = 20.45
avg_MAE_90D_pct = -15.80
avg_MFE_180D_pct = 39.90
avg_MAE_180D_pct = -21.18
```

The residual error is not "AMPC good" or "EV demand bad." C13 behaves like a two-layer valve. The first valve is accounting/policy support: IRA/AMPC, DOE/ATVM loan, JV construction, production credit, utilization. The second valve is conversion: ex-credit operating profit, call-off, shipment, utilization rate, yield, ESS/EV mix, customer inventory normalization, and margin bridge. When only the first valve opens, the stock can still hit -30% to -40% MAE. When both valves open after a price reset, hard 4C becomes too bearish.

## 7. Proposed shadow rule candidate

```text
sector_specific_rule_candidate = L3_C13_AMPC_JV_UTILIZATION_CONVERSION_AND_RESET_GATE_V1
canonical_archetype_rule_candidate = C13_AMPC_OPTICAL_PROFIT_JV_UTILIZATION_AND_FALSE_4C_RESET_GATE_V1
new_axis_proposed = c13_ampc_optical_profit_jv_utilization_and_false_4c_reset_gate
existing_axis_strengthened = full_4b_requires_non_price_evidence|price_only_blowoff_blocks_positive_stage
existing_axis_weakened = hard_4c_thesis_break_routes_to_4c_should_not_fire_on_demand_slowdown_or_customer_inventory_language_alone
```

Rule statement:

```text
For C13_BATTERY_JV_UTILIZATION_AMPC_IRA, Stage2-Actionable should require at least one policy/JV support bridge and one conversion bridge.

policy_or_jv_support_bridge examples:
- IRA/AMPC amount disclosed and recurring enough to matter
- JV plant in actual operation, not only announced/financed
- named OEM/customer facility ramp or call-off
- North America/ESS capacity reallocation tied to shipment plan

conversion_bridge examples:
- ex-AMPC operating profit or narrowing ex-AMPC loss
- utilization/yield improvement
- shipment/revenue timing
- ESS/EV product mix improvement
- customer inventory normalization
- margin/revision bridge

If only policy/JV support is present, keep Stage2-Watch.
If reported operating profit disappears ex-AMPC, block Stage2-Actionable unless utilization/revenue conversion is separately confirmed.
If demand-slowdown or quarterly loss appears after a large price reset and offsets remain live, do not jump directly to hard 4C; use 4B/4C-watch with a second confirmation trigger.
```

## 8. Raw component score breakdown

```jsonl
{"case_id": "C13-L161-CASE01-373220-LGES-Q1-2024-AMPC-CAPEX-CUT", "current_proxy_score": 62, "proposed_shadow_score": 56, "risk_penalty": 3, "bridge_bonus": 5}
{"case_id": "C13-L161-CASE02-373220-LGES-Q2-2024-REVENUE-CUT-RESET", "current_proxy_score": 76, "proposed_shadow_score": 80, "risk_penalty": 1, "bridge_bonus": 5}
{"case_id": "C13-L161-CASE03-373220-LGES-Q3-2024-IRA-OPTICAL-PROFIT", "current_proxy_score": 62, "proposed_shadow_score": 56, "risk_penalty": 3, "bridge_bonus": 5}
{"case_id": "C13-L161-CASE04-373220-LGES-Q1-2025-AMPC-ESS-RESET", "current_proxy_score": 74, "proposed_shadow_score": 74, "risk_penalty": 3, "bridge_bonus": 5}
{"case_id": "C13-L161-CASE05-006400-SAMSUNGSDI-HUNGARY-UTILIZATION-2024", "current_proxy_score": 73, "proposed_shadow_score": 73, "risk_penalty": 1, "bridge_bonus": 2}
{"case_id": "C13-L161-CASE06-006400-SAMSUNGSDI-STARPLUS-DOE-LOAN", "current_proxy_score": 59, "proposed_shadow_score": 53, "risk_penalty": 6, "bridge_bonus": 5}
{"case_id": "C13-L161-CASE07-006400-SAMSUNGSDI-Q1-2025-LOSS-RESET", "current_proxy_score": 76, "proposed_shadow_score": 80, "risk_penalty": 1, "bridge_bonus": 5}
```

## 9. Machine-readable trigger rows JSONL

```jsonl
{"case_id": "C13-L161-CASE01-373220-LGES-Q1-2024-AMPC-CAPEX-CUT", "code": "373220", "trigger_type": "Stage2", "trigger_date": "2024-04-26", "role": "counterexample / high-MAE watch", "verdict": "current_profile_false_positive_if_AMPC_prevents_loss_but_utilization_capex_signal_is_weak", "evidence": "Reuters: Q1 profit plunged 75%; LGES would have recorded a loss without IRA credit; capex to be minimized on slow EV demand.", "url": "https://www.reuters.com/technology/battery-firm-lg-energy-solution-q1-profit-plunges-weak-ev-sales-2024-04-25/", "entry_date": "2024-04-26", "entry_price": 372000.0, "MFE_30D_pct": 6.72, "MAE_30D_pct": -12.37, "peak_30D_date": "2024-05-07", "trough_30D_date": "2024-05-30", "MFE_90D_pct": 12.63, "MAE_90D_pct": -16.4, "peak_90D_date": "2024-09-03", "trough_90D_date": "2024-08-05", "MFE_180D_pct": 19.35, "MAE_180D_pct": -16.4, "peak_180D_date": "2024-10-08", "trough_180D_date": "2024-08-05", "company": "LG에너지솔루션", "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C13_BATTERY_JV_UTILIZATION_AMPC_IRA", "price_source": "Songdaiki/stock-web", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "calibration_usable": true, "dedupe_key": "C13_BATTERY_JV_UTILIZATION_AMPC_IRA|373220|Stage2|2024-04-26"}
{"case_id": "C13-L161-CASE02-373220-LGES-Q2-2024-REVENUE-CUT-RESET", "code": "373220", "trigger_type": "4C-Watch", "trigger_date": "2024-07-26", "role": "positive / false-hard-4C reset", "verdict": "current_profile_too_bearish_if_revenue_cut_is_already_priced_and_IRA_geopolitical_offset_remains", "evidence": "Reuters: LGES cut 2024 revenue target, slowed expansion, and cut IRA credit estimate; market nevertheless repriced China-supply-chain/geopolitical offsets.", "url": "https://www.reuters.com/technology/battery-firm-lg-energy-solution-q2-profit-plunges-weak-ev-demand-2024-07-25/", "entry_date": "2024-07-26", "entry_price": 325000.0, "MFE_30D_pct": 28.92, "MAE_30D_pct": -4.31, "peak_30D_date": "2024-09-03", "trough_30D_date": "2024-08-05", "MFE_90D_pct": 36.62, "MAE_90D_pct": -4.31, "peak_90D_date": "2024-10-08", "trough_90D_date": "2024-08-05", "MFE_180D_pct": 36.62, "MAE_180D_pct": -4.46, "peak_180D_date": "2024-10-08", "trough_180D_date": "2025-04-03", "company": "LG에너지솔루션", "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C13_BATTERY_JV_UTILIZATION_AMPC_IRA", "price_source": "Songdaiki/stock-web", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "calibration_usable": true, "dedupe_key": "C13_BATTERY_JV_UTILIZATION_AMPC_IRA|373220|4C-Watch|2024-07-26"}
{"case_id": "C13-L161-CASE03-373220-LGES-Q3-2024-IRA-OPTICAL-PROFIT", "code": "373220", "trigger_type": "Stage2-Actionable", "trigger_date": "2024-10-29", "role": "counterexample / AMPC optical-profit trap", "verdict": "current_profile_false_positive_if_IRA_credit_is_counted_without_ex_IRA_operating_profit_or_utilization_durability", "evidence": "LGES Q3 release: KRW448.3bn OP included estimated IRA credit of KRW466bn; excluding credit, operating loss would have been KRW17.7bn.", "url": "https://news.lgensol.com/company-news/press-releases/3343/", "entry_date": "2024-10-29", "entry_price": 409000.0, "MFE_30D_pct": 6.48, "MAE_30D_pct": -9.29, "peak_30D_date": "2024-11-11", "trough_30D_date": "2024-11-15", "MFE_90D_pct": 6.48, "MAE_90D_pct": -20.54, "peak_90D_date": "2024-11-11", "trough_90D_date": "2025-03-14", "MFE_180D_pct": 6.48, "MAE_180D_pct": -34.96, "peak_180D_date": "2024-11-11", "trough_180D_date": "2025-05-23", "company": "LG에너지솔루션", "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C13_BATTERY_JV_UTILIZATION_AMPC_IRA", "price_source": "Songdaiki/stock-web", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "calibration_usable": true, "dedupe_key": "C13_BATTERY_JV_UTILIZATION_AMPC_IRA|373220|Stage2-Actionable|2024-10-29"}
{"case_id": "C13-L161-CASE04-373220-LGES-Q1-2025-AMPC-ESS-RESET", "code": "373220", "trigger_type": "Stage2-Watch", "trigger_date": "2025-04-30", "role": "positive / staged-entry high-MAE", "verdict": "current_profile_too_late_if_cost_cutting_capacity_reallocation_and_AMPC_support_are_seen_only_after_clean_OP_confirmation", "evidence": "LGES Q1 2025 release: KRW6.3tn revenue, KRW375bn OP, KRW458bn IRA tax credit, and North America capacity reallocation toward ESS/LFP.", "url": "https://inside.lgensol.com/en/2025/04/lg-energy-solution-releases-2025-first-quarter-financial-results/", "entry_date": "2025-04-30", "entry_price": 324500.0, "MFE_30D_pct": 1.39, "MAE_30D_pct": -18.03, "peak_30D_date": "2025-05-08", "trough_30D_date": "2025-05-23", "MFE_90D_pct": 24.19, "MAE_90D_pct": -18.03, "peak_90D_date": "2025-07-31", "trough_90D_date": "2025-05-23", "MFE_180D_pct": 62.4, "MAE_180D_pct": -18.03, "peak_180D_date": "2025-10-29", "trough_180D_date": "2025-05-23", "company": "LG에너지솔루션", "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C13_BATTERY_JV_UTILIZATION_AMPC_IRA", "price_source": "Songdaiki/stock-web", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "calibration_usable": true, "dedupe_key": "C13_BATTERY_JV_UTILIZATION_AMPC_IRA|373220|Stage2-Watch|2025-04-30"}
{"case_id": "C13-L161-CASE05-006400-SAMSUNGSDI-HUNGARY-UTILIZATION-2024", "code": "006400", "trigger_type": "Stage2-Actionable", "trigger_date": "2024-01-31", "role": "positive / utilization-to-MFE with exit guard", "verdict": "current_profile_correct_but_needs_180D_exit_guard_when_utilization_signal_lacks_AMPC_revenue_conversion", "evidence": "Samsung SDI commented that its Hungary mass-production plant maintained about 90% operating rate while discussing all-solid-state/EV battery direction.", "url": "https://www.asiae.co.kr/en/print.htm?idxno=2024013011160973222", "entry_date": "2024-01-31", "entry_price": 372500.0, "MFE_30D_pct": 25.77, "MAE_30D_pct": -2.55, "peak_30D_date": "2024-03-13", "trough_30D_date": "2024-03-06", "MFE_90D_pct": 32.75, "MAE_90D_pct": -2.55, "peak_90D_date": "2024-03-25", "trough_90D_date": "2024-03-06", "MFE_180D_pct": 32.75, "MAE_180D_pct": -20.94, "peak_180D_date": "2024-03-25", "trough_180D_date": "2024-08-05", "company": "삼성SDI", "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C13_BATTERY_JV_UTILIZATION_AMPC_IRA", "price_source": "Songdaiki/stock-web", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "calibration_usable": true, "dedupe_key": "C13_BATTERY_JV_UTILIZATION_AMPC_IRA|006400|Stage2-Actionable|2024-01-31"}
{"case_id": "C13-L161-CASE06-006400-SAMSUNGSDI-STARPLUS-DOE-LOAN", "code": "006400", "trigger_type": "Stage2", "trigger_date": "2024-12-04", "role": "counterexample / JV funding headline", "verdict": "current_profile_false_positive_if_ATVM_or_JV_funding_is_promoted_without_near_term_utilization_and_calloff_visibility", "evidence": "DOE conditional commitment / StarPlus Energy: Stellantis-Samsung JV planned Kokomo plants, 67GWh annual capacity target, but funding approval and EV demand/policy risk remained.", "url": "https://www.theverge.com/2024/12/3/24312175/stellantis-samsung-doe-atvm-ev-battery-loan", "entry_date": "2024-12-04", "entry_price": 259000.0, "MFE_30D_pct": 3.47, "MAE_30D_pct": -11.39, "peak_30D_date": "2024-12-16", "trough_30D_date": "2025-01-13", "MFE_90D_pct": 3.47, "MAE_90D_pct": -34.36, "peak_90D_date": "2024-12-16", "trough_90D_date": "2025-04-09", "MFE_180D_pct": 3.47, "MAE_180D_pct": -39.11, "peak_180D_date": "2024-12-16", "trough_180D_date": "2025-05-22", "company": "삼성SDI", "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C13_BATTERY_JV_UTILIZATION_AMPC_IRA", "price_source": "Songdaiki/stock-web", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "calibration_usable": true, "dedupe_key": "C13_BATTERY_JV_UTILIZATION_AMPC_IRA|006400|Stage2|2024-12-04"}
{"case_id": "C13-L161-CASE07-006400-SAMSUNGSDI-Q1-2025-LOSS-RESET", "code": "006400", "trigger_type": "4C-Watch", "trigger_date": "2025-04-28", "role": "positive / false-hard-4C reset", "verdict": "current_profile_too_bearish_if_Q1_loss_is_used_as_hard_4C_without_JV_yield_ESS_new_order_offset", "evidence": "Samsung SDI Q1 2025 release: KRW434.1bn operating loss and lower utilization, but U.S. Stellantis JV early operations/high yields and GM JV construction were underway.", "url": "https://samsungsdi.com/sdi-now/sdi-news/4344.html", "entry_date": "2025-04-28", "entry_price": 184200.0, "MFE_30D_pct": 0.71, "MAE_30D_pct": -14.39, "peak_30D_date": "2025-04-29", "trough_30D_date": "2025-05-22", "MFE_90D_pct": 27.04, "MAE_90D_pct": -14.39, "peak_90D_date": "2025-08-11", "trough_90D_date": "2025-05-22", "MFE_180D_pct": 118.24, "MAE_180D_pct": -14.39, "peak_180D_date": "2026-01-23", "trough_180D_date": "2025-05-22", "company": "삼성SDI", "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C13_BATTERY_JV_UTILIZATION_AMPC_IRA", "price_source": "Songdaiki/stock-web", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "calibration_usable": true, "dedupe_key": "C13_BATTERY_JV_UTILIZATION_AMPC_IRA|006400|4C-Watch|2025-04-28"}
```

## 10. Aggregate row

```json
{
  "row_type": "v12_aggregate",
  "round": "R3",
  "loop": 161,
  "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY",
  "canonical_archetype_id": "C13_BATTERY_JV_UTILIZATION_AMPC_IRA",
  "usable_trigger_rows": 7,
  "representative_trigger_rows": 7,
  "positive_case_count": 4,
  "counterexample_count": 3,
  "stage4b_watch_or_overlay_count": 5,
  "stage4c_or_false4c_audit_count": 3,
  "current_profile_error_count": 5,
  "avg_MFE_90D_pct": 20.45,
  "avg_MAE_90D_pct": -15.8,
  "avg_MFE_180D_pct": 39.9,
  "avg_MAE_180D_pct": -21.18,
  "rule_candidate": "C13_AMPC_OPTICAL_PROFIT_JV_UTILIZATION_AND_FALSE_4C_RESET_GATE_V1"
}
```

## 11. Residual contribution summary

```text
loop_contribution_label = canonical_archetype_rule_candidate
new_axis_proposed = c13_ampc_optical_profit_jv_utilization_and_false_4c_reset_gate
existing_axis_strengthened = full_4b_requires_non_price_evidence|price_only_blowoff_blocks_positive_stage
existing_axis_weakened = hard_4c_thesis_break_routes_to_4c_should_not_fire_on_demand_slowdown_or_customer_inventory_language_alone

do_not_propose_new_weight_delta = false
production_scoring_changed = false
shadow_weight_only = true
```

## 12. Deferred Coding Agent Handoff Prompt

```text
Do not execute this handoff in the research session.

Later coding-agent task:
1. Ingest this Markdown as a standard v12 result file.
2. Validate filename and metadata consistency: R3 / loop 161 / L3_BATTERY_EV_GREEN_MOBILITY / C13_BATTERY_JV_UTILIZATION_AMPC_IRA.
3. Parse every JSONL trigger row and verify required fields: entry_date, entry_price, trigger_type, MFE_30D_pct, MAE_30D_pct, MFE_90D_pct, MAE_90D_pct, MFE_180D_pct, MAE_180D_pct, large_sector_id, canonical_archetype_id.
4. Deduplicate by canonical_archetype_id + symbol + trigger_type + entry_date.
5. Exclude the narrative-only SK Innovation/SK On row from promotion because its stock-web profile has a 2024-11-20 corporate-action candidate overlapping the 180D window.
6. Consider a shadow patch named C13_AMPC_OPTICAL_PROFIT_JV_UTILIZATION_AND_FALSE_4C_RESET_GATE_V1.
7. Keep production scoring unchanged unless batch validation finds the same pattern across other C13 rows.
```

## 13. Next research state

```text
completed_round = R3
completed_loop = 161
selection_basis = docs/core/V12_Research_No_Repeat_Index.md
selected_priority_bucket = Priority 2 quality-repair after session-aware P0/P1 clearing
next_recommended_archetypes = C22_INSURANCE_RATE_CYCLE_RESERVE|C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG|C24_BIO_TRIAL_DATA_EVENT_RISK|C15_MATERIAL_SPREAD_SUPERCYCLE|C17_CHEMICAL_COMMODITY_MARGIN_SPREAD
round_schedule_status = coverage_index_selected_not_sequential
round_sector_consistency = pass
```
