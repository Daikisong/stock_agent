# E2R Stock-Web v12 Residual Research — R3 / L3 / C13 Battery JV·AMPC·IRA Utilization Direct Row Repair V2

```text
research_session: post_calibrated_sector_archetype_residual_research
mode: historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12
selected_round: R3
selected_loop: 202
selection_basis: docs/core/V12_Research_No_Repeat_Index.md
selected_priority_bucket: Priority 1 balance reinforcement / AMPC·IRA durability and JV utilization failure repair
round_schedule_status: coverage_index_selected
round_sector_consistency: pass
large_sector_id: L3_BATTERY_EV_GREEN_MOBILITY
canonical_archetype_id: C13_BATTERY_JV_UTILIZATION_AMPC_IRA
fine_archetype_id: BATTERY_JV_AMPC_UTILIZATION_DIRECT_ROW_REPAIR_V2
output_filename: e2r_stock_web_v12_residual_round_R3_loop_202_L3_BATTERY_EV_GREEN_MOBILITY_C13_BATTERY_JV_UTILIZATION_AMPC_IRA_research.md
production_scoring_changed: false
shadow_weight_only: true
handoff_prompt_embedded: true
handoff_prompt_executed_now: false
```

## 1. Research objective

This file is a historical calibration artifact. It is not a live stock scan, not a trading recommendation, and not a `stock_agent` code patch. The loop continues C13 quality repair after the recent C10 hard-4C reopening study: C13 battery names often mix four signals in the same evidence packet — IRA/AMPC or regional-policy support, JV/customer capacity, utilization or inventory pressure, and offset/recovery language. The research question is whether the current calibrated profile should treat those packets as `Stage2`, `Stage2-Actionable`, local `Stage4B/watch`, or hard `Stage4C`.

```text
loop_objective:
  - stage2_actionable_bonus_stress_test
  - 4C_thesis_break_timing_test
  - holdout_validation
  - counterexample_mining
  - canonical_archetype_compression
```

## 2. Coverage / No-Repeat interpretation

The No-Repeat Index is used as a duplicate-prevention ledger only. Current cumulative corpus has no 30/50/80-row shortage for C01~C32, but Priority 1 still calls out `C13_BATTERY_JV_UTILIZATION_AMPC_IRA` for AMPC/IRA durability and JV/utilization failure-case repair.

```text
hard_duplicate_key: canonical_archetype_id + symbol + trigger_type + entry_date
same_canonical_allowed: true
same_symbol_allowed_only_with_new_trigger_date_or_trigger_family: true
minimum_new_independent_case_ratio: 0.60
actual_new_independent_case_ratio: 1.00
minimum_new_symbol_count: 2
actual_new_symbol_count: 8
```

Recent visible/local-session C13 duplicate groups avoided:

```text
C13 / 003670 / Stage2-Actionable / 2023-06-02
C13 / 003670 / Stage4B / 2025-02-03
C13 / 006400 / Stage2 / 2023-04-26
C13 / 006400 / Stage4B / 2024-07-30
C13 / 006400 / Stage4C / 2024-08-29
C13 / 373220 / Stage4B / 2024-04-25, 2024-10-28, 2025-01-24
C13 / 373220 / Stage2-Actionable / 2025-04-30
C13 / 096770 / Stage2 / 2023-07-28
C13 / 096770 / Stage4B / 2024-08-01
C13 / 051910 / Stage2-Actionable / 2022-11-22, 2024-02-07
C13 / 051910 / Stage4B / 2024-10-29
C13 / 011790 / Stage4B / 2024-08-07, 2024-10-18
C13 / 066970 / Stage4B / 2024-08-07, 2025-02-05
C13 / 247540 / Stage2 / 2023-12-04
C13 / 247540 / Stage4B / 2024-02-07
C13 / 247540 / Stage4C / 2024-11-04
```

## 3. Stock-Web manifest / schema validation

```text
price_data_source: Songdaiki/stock-web
price_data_repo: https://github.com/Songdaiki/stock-web
upstream_source: FinanceData/marcap
price_basis: tradable_raw
price_adjustment_status: raw_unadjusted_marcap
stock_web_manifest_max_date: 2026-02-20
calibration_shard_root: atlas/ohlcv_tradable_by_symbol_year
tradable_schema: d,o,h,l,c,v,a,mc,s,m
entry_price_basis: entry_date close, c column
MFE_N_pct: (max high from entry_date through N trading rows / entry_price - 1) * 100
MAE_N_pct: (min low from entry_date through N trading rows / entry_price - 1) * 100
```

Corporate-action / forward-window check:

```text
393890 WCP: corporate_action_candidate_count=0 in prior profile check; selected 2024-05-31 180D window clean by row continuity.
020150 LOTTE Energy Materials: corporate_action_candidate_count=0 in prior profile check; selected 2024-05-10 180D window clean by row continuity.
066970 L&F: profile has older 2016-02-19 and 2021-08-11 candidates; no overlap with 2025-02-19 180D window.
005070 Cosmo AM&T: older corporate-action candidates through 2019-11-13; no overlap with 2025-01-20 180D window.
247540 EcoPro BM: older corporate-action candidates on 2022-06-27 and 2022-07-15; no overlap with 2025-01-16 180D window.
278280 Chunbo: corporate_action_candidate_count=0 in prior profile check; selected 2024-09-23 180D window clean by row continuity.
096770 SK Innovation: profile candidate 2024-11-20 lies before selected 2025-02-06 entry; no overlap with 2025 forward window.
051910 LG Chem: corporate_action_candidate_count=0 in prior profile check; selected 2025-02-07 180D window clean by row continuity.
```

## 4. Evidence table

| Symbol | Company | Trigger date | Trigger | Evidence source | Evidence used |
|---|---|---|---|---|---|
| 393890 | W-Scope Chungju Plant | 2024-05-31 | Stage4C | https://securities.miraeasset.com/newir/view/pc/en/investor/researchReportsView.jsp?messageId=2323784 | Mirae Asset coverage described WCP share weakness from lackluster 1Q24 results and intensifying separator competition. For C13 this is a direct separator-utilization/margin-stress row, not a mere EV macro slowdown headline. |
| 020150 | LOTTE Energy Materials | 2024-05-10 | Stage2-Actionable | https://securities.miraeasset.com/bbs/download/2126850.pdf?attachmentId=2126850 | The May 2024 report framed fixed-cost pressure from low utilization but expected copper-foil utilization recovery toward the mid-70% range and downstream inventory restocking. The thesis was real but the forward path shows why Actionable must remain capped. |
| 066970 | L&F | 2025-02-19 | Stage4B | https://biz.chosun.com/en/en-industry/2025/02/19/QEZM6G5RB5BINMGGHOWVJZDZKU/ | L&F had severe 2023-2024 losses and weak cathode demand, but the evidence also contained a product-offset route through high-Ni and LFP cathode focus. This row tests 4B/watch versus hard 4C. |
| 005070 | Cosmo Advanced Materials & Technology | 2025-01-20 | Stage2-Actionable | https://www.mk.co.kr/en/business/11222344 | Cosmo AM&T reported five consecutive surplus years and 20 consecutive profitable quarters, a clean profitability bridge. The stock-web path, however, had no 180D upside and deep MAE, making it a valid Actionable-but-not-Yellow/Green cap row. |
| 247540 | EcoPro BM | 2025-01-16 | Stage4B | https://securities.miraeasset.com/newir/view/pc/en/investor/researchReportsView.jsp?messageId=2329709 | The January 2025 note reduced operating-loss estimates due to reversal of inventory valuation provisions and argued earnings had likely bottomed, but customer pull/utilization recovery remained insufficient for Stage2-Actionable or Yellow. |
| 278280 | Chunbo | 2024-09-23 | Stage2 | https://chunbochem.com/en/investment/ir_report_view.html?bs=&pg=1&seq=11&sf=&ss= | Chunbo 2Q24 IR and related coverage pointed to North America-bound electrolyte additive shipments, but China oversupply and lithium-price pressure kept the recovery delayed. This is Stage2 only, not Actionable. |
| 096770 | SK Innovation | 2025-02-06 | Stage4B | https://www.reuters.com/business/energy/south-koreas-sk-innovation-expects-2025-refining-margins-remain-flat-2025-02-06/ | Reuters reported SK Innovation expected IRA adjustment rather than repeal and planned sizable battery capex, while the broader group remained exposed to flat refining and battery-unit execution risk. C13 treats this as 4B/watch because the battery capex route remains, but unit economics are not yet proven. |
| 051910 | LG Chem | 2025-02-04 | Stage2-Actionable | https://securities.miraeasset.com/bbs/download/2134148.pdf?attachmentId=2134148 | Mirae Asset estimated cathode-material OPM at 2-3% in 4Q24 and discussed 2025 shipment/ASP guidance, giving a second bridge beyond long-lead Tennessee capex. This is a positive reopen row with a direct margin-guidance bridge. |

## 5. Entry-row validation

| Symbol | Entry date | Open | High | Low | Close / entry | Volume | Market | Stock-Web tradable shard |
|---|---|---:|---:|---:|---:|---:|---|---|
| 393890 | 2024-05-31 | 33750 | 36150 | 33700 | 35350 | 349806 | KOSDAQ | atlas/ohlcv_tradable_by_symbol_year/393/393890/2024.csv |
| 020150 | 2024-05-10 | 48300 | 48750 | 45750 | 45900 | 207682 | KOSPI | atlas/ohlcv_tradable_by_symbol_year/020/020150/2024.csv |
| 066970 | 2025-02-19 | 81400 | 92700 | 81100 | 89700 | 813044 | KOSPI | atlas/ohlcv_tradable_by_symbol_year/066/066970/2025.csv |
| 005070 | 2025-01-20 | 55600 | 61100 | 55400 | 61100 | 688775 | KOSPI | atlas/ohlcv_tradable_by_symbol_year/005/005070/2025.csv |
| 247540 | 2025-01-16 | 134700 | 136600 | 130900 | 131300 | 676789 | KOSDAQ GLOBAL | atlas/ohlcv_tradable_by_symbol_year/247/247540/2025.csv |
| 278280 | 2024-09-23 | 53100 | 54200 | 52200 | 53700 | 19604 | KOSDAQ | atlas/ohlcv_tradable_by_symbol_year/278/278280/2024.csv |
| 096770 | 2025-02-06 | 124500 | 125500 | 120900 | 124500 | 180135 | KOSPI | atlas/ohlcv_tradable_by_symbol_year/096/096770/2025.csv |
| 051910 | 2025-02-07 | 220000 | 224500 | 216000 | 217000 | 322872 | KOSPI | atlas/ohlcv_tradable_by_symbol_year/051/051910/2025.csv |

## 6. Trigger-level price path results

| # | Symbol | Company | Trigger | Entry | Entry price | 30D MFE/MAE | 90D MFE/MAE | 180D MFE/MAE | Peak date | Peak price | DD after peak | Verdict |
|---:|---|---|---|---|---:|---:|---:|---:|---|---:|---:|---|
| 1 | 393890 | W-Scope Chungju Plant | Stage4C | 2024-05-31 | 35350 | 2.26/-17.11 | 2.26/-52.48 | 2.26/-72.62 | 2024-05-31 | 36150 | -73.22 | correct_hard_4c |
| 2 | 020150 | LOTTE Energy Materials | Stage2-Actionable | 2024-05-10 | 45900 | 28.98/-3.70 | 28.98/-33.55 | 28.98/-55.88 | 2024-06-18 | 59200 | -65.79 | actionable_but_green_cap_required |
| 3 | 066970 | L&F | Stage4B | 2025-02-19 | 89700 | 4.68/-35.34 | 4.68/-47.60 | 66.11/-47.60 | 2025-10-29 | 149000 | -22.48 | correct_4b_watch_not_hard4c |
| 4 | 005070 | Cosmo Advanced Materials & Technology | Stage2-Actionable | 2025-01-20 | 61100 | 0.00/-22.67 | 0.00/-51.72 | 0.00/-51.72 | 2025-01-20 | 61100 | -51.72 | actionable_but_green_cap_required |
| 5 | 247540 | EcoPro BM | Stage4B | 2025-01-16 | 131300 | 7.92/-15.69 | 7.92/-38.23 | 8.91/-38.23 | 2025-10-16 | 143000 | -12.80 | 4b_watch_but_positive_reopen_not_proven |
| 6 | 278280 | Chunbo | Stage2 | 2024-09-23 | 53700 | 22.35/-2.79 | 22.35/-36.03 | 22.35/-44.04 | 2024-10-08 | 65700 | -54.26 | stage2_false_positive_without_second_bridge |
| 7 | 096770 | SK Innovation | Stage4B | 2025-02-06 | 124500 | 12.61/-3.61 | 12.61/-35.10 | 12.61/-35.10 | 2025-03-13 | 140200 | -42.37 | 4b_watch_but_positive_reopen_not_proven |
| 8 | 051910 | LG Chem | Stage2-Actionable | 2025-02-07 | 217000 | 21.43/-4.15 | 27.19/-16.36 | 95.16/-16.36 | 2025-10-30 | 423500 | -8.97 | actionable_positive_control |

## 7. Case interpretation

### 7.1 Hard 4C that should remain hard

`393890 / 2024-05-31 / Stage4C` is the cleanest hard-4C positive control in this batch. The evidence packet is not just “EV demand is weak.” It has separator-specific competition and weak quarterly performance. Stock-Web confirms the later path: `180D MFE/MAE = 2.26 / -72.62`, with the peak already on the entry row. C13 should not reopen this without a later direct order/utilization recovery bridge.

### 7.2 Stage2-Actionable that needs a high-MAE / Green cap

`020150 / 2024-05-10`, `005070 / 2025-01-20`, and `051910 / 2025-02-07` are all useful for the same reason: each contains a real second bridge, but not all second bridges deserve Yellow or Green. LOTTE Energy Materials had a utilization-rebound thesis but then suffered `-55.88%` 180D MAE. Cosmo AM&T had continuous profitability but `0.00%` 180D MFE and `-51.72%` 180D MAE. LG Chem was the positive reopen control because the 2025 cathode-margin/shipments guide later aligned with `95.16%` 180D MFE. The rule should preserve Actionable when margin/shipments are explicit, while blocking Yellow/Green until broader cash/margin conversion appears.

### 7.3 4B/watch versus false hard 4C

`066970 / 2025-02-19` and `096770 / 2025-02-06` show why hard 4C needs weak offset quality, not just ugly earnings or policy uncertainty. L&F had severe historical losses but later produced `66.11%` 180D MFE. SK Innovation had battery capex / IRA uncertainty and group-level cyclicality, but still showed enough battery-capex route to stay in 4B/watch. These are “do not Green, but do not irreversible-break by default” rows.

### 7.4 Stage2 false positive where the second bridge is missing

`278280 / 2024-09-23` remains Stage2 only. North America-bound electrolyte-additive shipment language is meaningful, but the row still carried oversupply and lithium-price drag. The price path reached `22.35%` MFE but also `-44.04%` MAE. This is exactly the point where Stage2-Actionable should require a second bridge such as firm shipment conversion, customer pull, or margin guidance.

## 8. Score simulation summary

This is a research proxy score simulation, not `stock_agent` production scoring.

| Symbol | Trigger | Score before | Stage before | Score after | Stage after | Delta reason |
|---|---|---:|---|---:|---|---|
| 393890 | Stage4C | 46 | Stage4B/watch | 38 | Stage4C | C13 utilization / customer-pull / offset-quality split |
| 020150 | Stage2-Actionable | 73 | Stage2-Actionable | 70 | Stage2-Actionable_capped | C13 utilization / customer-pull / offset-quality split |
| 066970 | Stage4B | 53 | Stage4C_if_offset_ignored | 57 | Stage4B/watch | C13 utilization / customer-pull / offset-quality split |
| 005070 | Stage2-Actionable | 73 | Stage2-Actionable | 70 | Stage2-Actionable_capped | C13 utilization / customer-pull / offset-quality split |
| 247540 | Stage4B | 53 | Stage4C_if_offset_ignored | 57 | Stage4B/watch | C13 utilization / customer-pull / offset-quality split |
| 278280 | Stage2 | 64 | Stage2 | 58 | Stage2_capped_watch | C13 utilization / customer-pull / offset-quality split |
| 096770 | Stage4B | 53 | Stage4C_if_offset_ignored | 57 | Stage4B/watch | C13 utilization / customer-pull / offset-quality split |
| 051910 | Stage2-Actionable | 73 | Stage2-Actionable | 70 | Stage2-Actionable_capped | C13 utilization / customer-pull / offset-quality split |

## 9. Residual contribution summary

```text
new_independent_case_count: 8
new_independent_trigger_count: 8
unique_symbol_count: 8

stage2_count: 1
stage2_actionable_count: 3
stage4b_count: 3
stage4c_count: 1

positive_or_reopen_case_count: 3
counterexample_or_guardrail_case_count: 5
current_profile_error_count: 3

source_proxy_only_count: 0
evidence_url_pending_count: 0
missing_required_mfe_mae_count: 0
corporate_action_contaminated_180D_count: 0
insufficient_forward_window_180D_count: 0

production_scoring_changed: false
shadow_weight_only: true
```

Rule candidate:

```text
canonical_rule_candidate:
C13_UTILIZATION_CUSTOMER_PULL_AND_OFFSET_QUALITY_GATE

core residual:
- AMPC / IRA / JV / regional supply-chain language alone does not create Stage2-Actionable or Yellow.
- Stage2-Actionable requires at least one direct second bridge: utilization rebound, customer pull/call-off, shipment conversion, ex-subsidy margin, or cathode-material OPM/ASP guidance.
- A true direct margin/shipment bridge can reopen Stage2-Actionable after a weak battery-material year.
- Deep MAE on a valid direct-bridge row should block Yellow/Green, not erase Stage2-Actionable.
- Hard 4C requires utilization/margin thesis break plus weak or absent offset quality. If product/customer/geographic recovery bridge survives, route to local Stage4B/watch instead.
```

## 10. Machine-readable JSONL trigger rows

```jsonl
{"row_type": "trigger", "trigger_id": "R3L202_C13_T01_393890_2024-05-31", "case_id": "C13_WCP_20240531_SEPARATOR_COMPETITION_Q1_WEAKNESS_HARD4C", "symbol": "393890", "company_name": "W-Scope Chungju Plant", "round": "R3", "loop": 202, "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C13_BATTERY_JV_UTILIZATION_AMPC_IRA", "fine_archetype_id": "BATTERY_JV_AMPC_UTILIZATION_DIRECT_ROW_REPAIR_V2", "sector": "battery_ev_green_mobility", "primary_archetype": "battery_jv_utilization_ampc_ira", "loop_objective": ["stage2_actionable_bonus_stress_test", "4C_thesis_break_timing_test", "holdout_validation", "counterexample_mining", "canonical_archetype_compression"], "trigger_type": "Stage4C", "trigger_date": "2024-05-31", "evidence_available_at_that_date": "same_day_or_next_tradable_close_per_timestamp_conservatism", "evidence_source": "https://securities.miraeasset.com/newir/view/pc/en/investor/researchReportsView.jsp?messageId=2323784", "evidence_summary": "Mirae Asset coverage described WCP share weakness from lackluster 1Q24 results and intensifying separator competition. For C13 this is a direct separator-utilization/margin-stress row, not a mere EV macro slowdown headline.", "evidence_family": "separator_Q1_weakness_intensifying_competition_utilization_margin_break", "stage2_evidence_fields": [], "stage3_evidence_fields": [], "stage4b_evidence_fields": [], "stage4c_evidence_fields": ["utilization_or_margin_thesis_break", "weak_or_unproven_offset_quality"], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/393/393890/2024.csv", "profile_path": "atlas/symbol_profiles/393/393890.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "entry_date": "2024-05-31", "entry_price": 35350.0, "entry_open": 33750.0, "entry_high": 36150.0, "entry_low": 33700.0, "entry_volume": 349806.0, "MFE_30D_pct": 2.26, "MFE_90D_pct": 2.26, "MFE_180D_pct": 2.26, "MFE_1Y_pct": null, "MFE_2Y_pct": null, "MAE_30D_pct": -17.11, "MAE_90D_pct": -52.48, "MAE_180D_pct": -72.62, "MAE_1Y_pct": null, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2024-05-31", "peak_price": 36150.0, "drawdown_after_peak_pct": -73.22, "green_lateness_ratio": "not_applicable_no_stage3_green_trigger", "four_b_local_peak_proximity": "case_specific", "four_b_full_window_peak_proximity": "case_specific", "four_b_timing_verdict": "local_4b_or_hard_4c_boundary_audit", "four_b_evidence_type": ["utilization_pressure", "inventory_loss_or_fixed_cost_pressure", "offset_quality_present"], "four_c_protection_label": "hard_4c_success", "trigger_outcome_label": "hard_4c_positive_control", "current_profile_verdict": "correct_hard_4c", "calibration_usable": true, "forward_window_trading_days": 180, "forward_available_rows_in_cached_stock_web": 385, "calibration_block_reasons": [], "corporate_action_window_status": "clean_no_candidate_overlap_180D_window", "corporate_action_profile_note": "corporate_action_candidate_count=0 in prior profile check; selected 2024-05-31 180D window clean by row continuity.", "same_entry_group_id": "C13_393890_2024-05-31", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": "same canonical allowed; hard duplicate key is new relative to recent session and local generated artifacts", "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false, "raw_component_scores_before": {"eps_fcf_explosion": 0, "earnings_visibility": -3, "bottleneck_pricing": -2, "market_mispricing": -2, "valuation_rerating": 0, "capital_allocation": 0, "information_confidence": 2, "execution_risk": -4, "accounting_trust_risk": -2, "utilization_bridge": -4, "offset_quality": 0, "ex_subsidy_margin_quality": 0}, "weighted_score_before": 46, "stage_label_before": "Stage4B/watch", "raw_component_scores_after": {"eps_fcf_explosion": 0, "earnings_visibility": -4, "bottleneck_pricing": -3, "market_mispricing": -2, "valuation_rerating": 0, "capital_allocation": 0, "information_confidence": 3, "execution_risk": -5, "accounting_trust_risk": -3, "utilization_bridge": -5, "offset_quality": -1, "ex_subsidy_margin_quality": 0}, "weighted_score_after": 38, "stage_label_after": "Stage4C", "component_delta_explanation": "C13 needs direct utilization/customer-pull/margin bridge for Actionable and weak-offset quality for hard 4C; otherwise use Stage2 cap or local 4B/watch."}
{"row_type": "trigger", "trigger_id": "R3L202_C13_T02_020150_2024-05-10", "case_id": "C13_LOTTE_ENERGY_20240510_UTILIZATION_REBOUND_THESIS_HIGH_MAE", "symbol": "020150", "company_name": "LOTTE Energy Materials", "round": "R3", "loop": 202, "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C13_BATTERY_JV_UTILIZATION_AMPC_IRA", "fine_archetype_id": "BATTERY_JV_AMPC_UTILIZATION_DIRECT_ROW_REPAIR_V2", "sector": "battery_ev_green_mobility", "primary_archetype": "battery_jv_utilization_ampc_ira", "loop_objective": ["stage2_actionable_bonus_stress_test", "4C_thesis_break_timing_test", "holdout_validation", "counterexample_mining", "canonical_archetype_compression"], "trigger_type": "Stage2-Actionable", "trigger_date": "2024-05-10", "evidence_available_at_that_date": "same_day_or_next_tradable_close_per_timestamp_conservatism", "evidence_source": "https://securities.miraeasset.com/bbs/download/2126850.pdf?attachmentId=2126850", "evidence_summary": "The May 2024 report framed fixed-cost pressure from low utilization but expected copper-foil utilization recovery toward the mid-70% range and downstream inventory restocking. The thesis was real but the forward path shows why Actionable must remain capped.", "evidence_family": "copper_foil_utilization_rebound_expectation_fixed_cost_pressure", "stage2_evidence_fields": ["utilization_recovery_or_customer_pull", "margin_guidance_or_profitability_bridge"], "stage3_evidence_fields": [], "stage4b_evidence_fields": [], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/020/020150/2024.csv", "profile_path": "atlas/symbol_profiles/020/020150.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "entry_date": "2024-05-10", "entry_price": 45900.0, "entry_open": 48300.0, "entry_high": 48750.0, "entry_low": 45750.0, "entry_volume": 207682.0, "MFE_30D_pct": 28.98, "MFE_90D_pct": 28.98, "MFE_180D_pct": 28.98, "MFE_1Y_pct": null, "MFE_2Y_pct": null, "MAE_30D_pct": -3.7, "MAE_90D_pct": -33.55, "MAE_180D_pct": -55.88, "MAE_1Y_pct": null, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2024-06-18", "peak_price": 59200.0, "drawdown_after_peak_pct": -65.79, "green_lateness_ratio": "not_applicable_no_stage3_green_trigger", "four_b_local_peak_proximity": "case_specific", "four_b_full_window_peak_proximity": "case_specific", "four_b_timing_verdict": "local_4b_or_hard_4c_boundary_audit", "four_b_evidence_type": [], "four_c_protection_label": "not_applicable", "trigger_outcome_label": "stage2_actionable_high_mae_counterexample", "current_profile_verdict": "actionable_but_green_cap_required", "calibration_usable": true, "forward_window_trading_days": 180, "forward_available_rows_in_cached_stock_web": 399, "calibration_block_reasons": [], "corporate_action_window_status": "clean_no_candidate_overlap_180D_window", "corporate_action_profile_note": "corporate_action_candidate_count=0 in prior profile check; selected 2024-05-10 180D window clean by row continuity.", "same_entry_group_id": "C13_020150_2024-05-10", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": "same canonical allowed; hard duplicate key is new relative to recent session and local generated artifacts", "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false, "raw_component_scores_before": {"eps_fcf_explosion": 2, "earnings_visibility": 4, "bottleneck_pricing": 2, "market_mispricing": 2, "valuation_rerating": 2, "capital_allocation": 1, "information_confidence": 3, "execution_risk": -2, "accounting_trust_risk": 0, "utilization_bridge": 3, "offset_quality": 2, "ex_subsidy_margin_quality": 2}, "weighted_score_before": 73, "stage_label_before": "Stage2-Actionable", "raw_component_scores_after": {"eps_fcf_explosion": 2, "earnings_visibility": 4, "bottleneck_pricing": 2, "market_mispricing": 1, "valuation_rerating": 1, "capital_allocation": 1, "information_confidence": 3, "execution_risk": -2, "accounting_trust_risk": 0, "utilization_bridge": 3, "offset_quality": 2, "ex_subsidy_margin_quality": 2, "high_mae_green_cap": -3}, "weighted_score_after": 70, "stage_label_after": "Stage2-Actionable_capped", "component_delta_explanation": "C13 needs direct utilization/customer-pull/margin bridge for Actionable and weak-offset quality for hard 4C; otherwise use Stage2 cap or local 4B/watch."}
{"row_type": "trigger", "trigger_id": "R3L202_C13_T03_066970_2025-02-19", "case_id": "C13_LNF_20250219_LOSS_HISTORY_HIGH_NI_LFP_OFFSET_4B", "symbol": "066970", "company_name": "L&F", "round": "R3", "loop": 202, "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C13_BATTERY_JV_UTILIZATION_AMPC_IRA", "fine_archetype_id": "BATTERY_JV_AMPC_UTILIZATION_DIRECT_ROW_REPAIR_V2", "sector": "battery_ev_green_mobility", "primary_archetype": "battery_jv_utilization_ampc_ira", "loop_objective": ["stage2_actionable_bonus_stress_test", "4C_thesis_break_timing_test", "holdout_validation", "counterexample_mining", "canonical_archetype_compression"], "trigger_type": "Stage4B", "trigger_date": "2025-02-19", "evidence_available_at_that_date": "same_day_or_next_tradable_close_per_timestamp_conservatism", "evidence_source": "https://biz.chosun.com/en/en-industry/2025/02/19/QEZM6G5RB5BINMGGHOWVJZDZKU/", "evidence_summary": "L&F had severe 2023-2024 losses and weak cathode demand, but the evidence also contained a product-offset route through high-Ni and LFP cathode focus. This row tests 4B/watch versus hard 4C.", "evidence_family": "multi_year_loss_but_high_nickel_LFP_focus_offset", "stage2_evidence_fields": [], "stage3_evidence_fields": [], "stage4b_evidence_fields": ["utilization_pressure", "inventory_or_fixed_cost_pressure", "offset_quality_present"], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/066/066970/2025.csv", "profile_path": "atlas/symbol_profiles/066/066970.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "entry_date": "2025-02-19", "entry_price": 89700.0, "entry_open": 81400.0, "entry_high": 92700.0, "entry_low": 81100.0, "entry_volume": 813044.0, "MFE_30D_pct": 4.68, "MFE_90D_pct": 4.68, "MFE_180D_pct": 66.11, "MFE_1Y_pct": null, "MFE_2Y_pct": null, "MAE_30D_pct": -35.34, "MAE_90D_pct": -47.6, "MAE_180D_pct": -47.6, "MAE_1Y_pct": null, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2025-10-29", "peak_price": 149000.0, "drawdown_after_peak_pct": -22.48, "green_lateness_ratio": "not_applicable_no_stage3_green_trigger", "four_b_local_peak_proximity": "case_specific", "four_b_full_window_peak_proximity": "case_specific", "four_b_timing_verdict": "local_4b_or_hard_4c_boundary_audit", "four_b_evidence_type": ["utilization_pressure", "inventory_loss_or_fixed_cost_pressure", "offset_quality_present"], "four_c_protection_label": "false_break_or_watch_only", "trigger_outcome_label": "false_hard_4c_control", "current_profile_verdict": "correct_4b_watch_not_hard4c", "calibration_usable": true, "forward_window_trading_days": 180, "forward_available_rows_in_cached_stock_web": 245, "calibration_block_reasons": [], "corporate_action_window_status": "clean_no_candidate_overlap_180D_window", "corporate_action_profile_note": "profile has older 2016-02-19 and 2021-08-11 candidates; no overlap with 2025-02-19 180D window.", "same_entry_group_id": "C13_066970_2025-02-19", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": "same canonical allowed; hard duplicate key is new relative to recent session and local generated artifacts", "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false, "raw_component_scores_before": {"eps_fcf_explosion": 0, "earnings_visibility": -2, "bottleneck_pricing": -1, "market_mispricing": -1, "valuation_rerating": 0, "capital_allocation": 0, "information_confidence": 2, "execution_risk": -3, "accounting_trust_risk": -1, "utilization_bridge": -3, "offset_quality": 2, "ex_subsidy_margin_quality": 0}, "weighted_score_before": 53, "stage_label_before": "Stage4C_if_offset_ignored", "raw_component_scores_after": {"eps_fcf_explosion": 0, "earnings_visibility": -2, "bottleneck_pricing": -1, "market_mispricing": -1, "valuation_rerating": 0, "capital_allocation": 0, "information_confidence": 3, "execution_risk": -3, "accounting_trust_risk": -1, "utilization_bridge": -3, "offset_quality": 4, "ex_subsidy_margin_quality": 0}, "weighted_score_after": 57, "stage_label_after": "Stage4B/watch", "component_delta_explanation": "C13 needs direct utilization/customer-pull/margin bridge for Actionable and weak-offset quality for hard 4C; otherwise use Stage2 cap or local 4B/watch."}
{"row_type": "trigger", "trigger_id": "R3L202_C13_T04_005070_2025-01-20", "case_id": "C13_COSMO_AMT_20250120_PROFIT_CONTINUITY_FALSE_ACTIONABLE", "symbol": "005070", "company_name": "Cosmo Advanced Materials & Technology", "round": "R3", "loop": 202, "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C13_BATTERY_JV_UTILIZATION_AMPC_IRA", "fine_archetype_id": "BATTERY_JV_AMPC_UTILIZATION_DIRECT_ROW_REPAIR_V2", "sector": "battery_ev_green_mobility", "primary_archetype": "battery_jv_utilization_ampc_ira", "loop_objective": ["stage2_actionable_bonus_stress_test", "4C_thesis_break_timing_test", "holdout_validation", "counterexample_mining", "canonical_archetype_compression"], "trigger_type": "Stage2-Actionable", "trigger_date": "2025-01-20", "evidence_available_at_that_date": "same_day_or_next_tradable_close_per_timestamp_conservatism", "evidence_source": "https://www.mk.co.kr/en/business/11222344", "evidence_summary": "Cosmo AM&T reported five consecutive surplus years and 20 consecutive profitable quarters, a clean profitability bridge. The stock-web path, however, had no 180D upside and deep MAE, making it a valid Actionable-but-not-Yellow/Green cap row.", "evidence_family": "profit_surplus_continuity_cathode_facility_investment_but_no_forward_rerating", "stage2_evidence_fields": ["utilization_recovery_or_customer_pull", "margin_guidance_or_profitability_bridge"], "stage3_evidence_fields": [], "stage4b_evidence_fields": [], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/005/005070/2025.csv", "profile_path": "atlas/symbol_profiles/005/005070.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "entry_date": "2025-01-20", "entry_price": 61100.0, "entry_open": 55600.0, "entry_high": 61100.0, "entry_low": 55400.0, "entry_volume": 688775.0, "MFE_30D_pct": 0.0, "MFE_90D_pct": 0.0, "MFE_180D_pct": 0.0, "MFE_1Y_pct": null, "MFE_2Y_pct": null, "MAE_30D_pct": -22.67, "MAE_90D_pct": -51.72, "MAE_180D_pct": -51.72, "MAE_1Y_pct": null, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2025-01-20", "peak_price": 61100.0, "drawdown_after_peak_pct": -51.72, "green_lateness_ratio": "not_applicable_no_stage3_green_trigger", "four_b_local_peak_proximity": "case_specific", "four_b_full_window_peak_proximity": "case_specific", "four_b_timing_verdict": "local_4b_or_hard_4c_boundary_audit", "four_b_evidence_type": [], "four_c_protection_label": "not_applicable", "trigger_outcome_label": "failed_positive_control", "current_profile_verdict": "actionable_but_green_cap_required", "calibration_usable": true, "forward_window_trading_days": 180, "forward_available_rows_in_cached_stock_web": 230, "calibration_block_reasons": [], "corporate_action_window_status": "clean_no_candidate_overlap_180D_window", "corporate_action_profile_note": "older corporate-action candidates through 2019-11-13; no overlap with 2025-01-20 180D window.", "same_entry_group_id": "C13_005070_2025-01-20", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": "same canonical allowed; hard duplicate key is new relative to recent session and local generated artifacts", "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false, "raw_component_scores_before": {"eps_fcf_explosion": 2, "earnings_visibility": 4, "bottleneck_pricing": 2, "market_mispricing": 2, "valuation_rerating": 2, "capital_allocation": 1, "information_confidence": 3, "execution_risk": -2, "accounting_trust_risk": 0, "utilization_bridge": 3, "offset_quality": 2, "ex_subsidy_margin_quality": 2}, "weighted_score_before": 73, "stage_label_before": "Stage2-Actionable", "raw_component_scores_after": {"eps_fcf_explosion": 2, "earnings_visibility": 4, "bottleneck_pricing": 2, "market_mispricing": 1, "valuation_rerating": 1, "capital_allocation": 1, "information_confidence": 3, "execution_risk": -2, "accounting_trust_risk": 0, "utilization_bridge": 3, "offset_quality": 2, "ex_subsidy_margin_quality": 2, "high_mae_green_cap": -3}, "weighted_score_after": 70, "stage_label_after": "Stage2-Actionable_capped", "component_delta_explanation": "C13 needs direct utilization/customer-pull/margin bridge for Actionable and weak-offset quality for hard 4C; otherwise use Stage2 cap or local 4B/watch."}
{"row_type": "trigger", "trigger_id": "R3L202_C13_T05_247540_2025-01-16", "case_id": "C13_ECOPROBM_20250116_BOTTOMING_REVERSAL_PROVISION_4B", "symbol": "247540", "company_name": "EcoPro BM", "round": "R3", "loop": 202, "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C13_BATTERY_JV_UTILIZATION_AMPC_IRA", "fine_archetype_id": "BATTERY_JV_AMPC_UTILIZATION_DIRECT_ROW_REPAIR_V2", "sector": "battery_ev_green_mobility", "primary_archetype": "battery_jv_utilization_ampc_ira", "loop_objective": ["stage2_actionable_bonus_stress_test", "4C_thesis_break_timing_test", "holdout_validation", "counterexample_mining", "canonical_archetype_compression"], "trigger_type": "Stage4B", "trigger_date": "2025-01-16", "evidence_available_at_that_date": "same_day_or_next_tradable_close_per_timestamp_conservatism", "evidence_source": "https://securities.miraeasset.com/newir/view/pc/en/investor/researchReportsView.jsp?messageId=2329709", "evidence_summary": "The January 2025 note reduced operating-loss estimates due to reversal of inventory valuation provisions and argued earnings had likely bottomed, but customer pull/utilization recovery remained insufficient for Stage2-Actionable or Yellow.", "evidence_family": "inventory_valuation_loss_reversal_bottoming_language_without_customer_pull", "stage2_evidence_fields": [], "stage3_evidence_fields": [], "stage4b_evidence_fields": ["utilization_pressure", "inventory_or_fixed_cost_pressure", "offset_quality_present"], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/247/247540/2025.csv", "profile_path": "atlas/symbol_profiles/247/247540.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "entry_date": "2025-01-16", "entry_price": 131300.0, "entry_open": 134700.0, "entry_high": 136600.0, "entry_low": 130900.0, "entry_volume": 676789.0, "MFE_30D_pct": 7.92, "MFE_90D_pct": 7.92, "MFE_180D_pct": 8.91, "MFE_1Y_pct": null, "MFE_2Y_pct": null, "MAE_30D_pct": -15.69, "MAE_90D_pct": -38.23, "MAE_180D_pct": -38.23, "MAE_1Y_pct": null, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2025-10-16", "peak_price": 143000.0, "drawdown_after_peak_pct": -12.8, "green_lateness_ratio": "not_applicable_no_stage3_green_trigger", "four_b_local_peak_proximity": "case_specific", "four_b_full_window_peak_proximity": "case_specific", "four_b_timing_verdict": "local_4b_or_hard_4c_boundary_audit", "four_b_evidence_type": ["utilization_pressure", "inventory_loss_or_fixed_cost_pressure", "offset_quality_present"], "four_c_protection_label": "false_break_or_watch_only", "trigger_outcome_label": "4b_watch_not_reopen_yet", "current_profile_verdict": "4b_watch_but_positive_reopen_not_proven", "calibration_usable": true, "forward_window_trading_days": 180, "forward_available_rows_in_cached_stock_web": 232, "calibration_block_reasons": [], "corporate_action_window_status": "clean_no_candidate_overlap_180D_window", "corporate_action_profile_note": "older corporate-action candidates on 2022-06-27 and 2022-07-15; no overlap with 2025-01-16 180D window.", "same_entry_group_id": "C13_247540_2025-01-16", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": "same canonical allowed; hard duplicate key is new relative to recent session and local generated artifacts", "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false, "raw_component_scores_before": {"eps_fcf_explosion": 0, "earnings_visibility": -2, "bottleneck_pricing": -1, "market_mispricing": -1, "valuation_rerating": 0, "capital_allocation": 0, "information_confidence": 2, "execution_risk": -3, "accounting_trust_risk": -1, "utilization_bridge": -3, "offset_quality": 2, "ex_subsidy_margin_quality": 0}, "weighted_score_before": 53, "stage_label_before": "Stage4C_if_offset_ignored", "raw_component_scores_after": {"eps_fcf_explosion": 0, "earnings_visibility": -2, "bottleneck_pricing": -1, "market_mispricing": -1, "valuation_rerating": 0, "capital_allocation": 0, "information_confidence": 3, "execution_risk": -3, "accounting_trust_risk": -1, "utilization_bridge": -3, "offset_quality": 4, "ex_subsidy_margin_quality": 0}, "weighted_score_after": 57, "stage_label_after": "Stage4B/watch", "component_delta_explanation": "C13 needs direct utilization/customer-pull/margin bridge for Actionable and weak-offset quality for hard 4C; otherwise use Stage2 cap or local 4B/watch."}
{"row_type": "trigger", "trigger_id": "R3L202_C13_T06_278280_2024-09-23", "case_id": "C13_CHUNBO_20240923_2Q_IR_NA_SHIPMENTS_BUT_MARGIN_DELAY", "symbol": "278280", "company_name": "Chunbo", "round": "R3", "loop": 202, "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C13_BATTERY_JV_UTILIZATION_AMPC_IRA", "fine_archetype_id": "BATTERY_JV_AMPC_UTILIZATION_DIRECT_ROW_REPAIR_V2", "sector": "battery_ev_green_mobility", "primary_archetype": "battery_jv_utilization_ampc_ira", "loop_objective": ["stage2_actionable_bonus_stress_test", "4C_thesis_break_timing_test", "holdout_validation", "counterexample_mining", "canonical_archetype_compression"], "trigger_type": "Stage2", "trigger_date": "2024-09-23", "evidence_available_at_that_date": "same_day_or_next_tradable_close_per_timestamp_conservatism", "evidence_source": "https://chunbochem.com/en/investment/ir_report_view.html?bs=&pg=1&seq=11&sf=&ss=", "evidence_summary": "Chunbo 2Q24 IR and related coverage pointed to North America-bound electrolyte additive shipments, but China oversupply and lithium-price pressure kept the recovery delayed. This is Stage2 only, not Actionable.", "evidence_family": "north_america_shipments_began_but_china_oversupply_lithium_price_drag", "stage2_evidence_fields": ["utilization_recovery_or_customer_pull", "margin_guidance_or_profitability_bridge"], "stage3_evidence_fields": [], "stage4b_evidence_fields": [], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/278/278280/2024.csv", "profile_path": "atlas/symbol_profiles/278/278280.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "entry_date": "2024-09-23", "entry_price": 53700.0, "entry_open": 53100.0, "entry_high": 54200.0, "entry_low": 52200.0, "entry_volume": 19604.0, "MFE_30D_pct": 22.35, "MFE_90D_pct": 22.35, "MFE_180D_pct": 22.35, "MFE_1Y_pct": null, "MFE_2Y_pct": null, "MAE_30D_pct": -2.79, "MAE_90D_pct": -36.03, "MAE_180D_pct": -44.04, "MAE_1Y_pct": null, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2024-10-08", "peak_price": 65700.0, "drawdown_after_peak_pct": -54.26, "green_lateness_ratio": "not_applicable_no_stage3_green_trigger", "four_b_local_peak_proximity": "case_specific", "four_b_full_window_peak_proximity": "case_specific", "four_b_timing_verdict": "local_4b_or_hard_4c_boundary_audit", "four_b_evidence_type": [], "four_c_protection_label": "not_applicable", "trigger_outcome_label": "stage2_false_positive_second_bridge_missing", "current_profile_verdict": "stage2_false_positive_without_second_bridge", "calibration_usable": true, "forward_window_trading_days": 180, "forward_available_rows_in_cached_stock_web": 309, "calibration_block_reasons": [], "corporate_action_window_status": "clean_no_candidate_overlap_180D_window", "corporate_action_profile_note": "corporate_action_candidate_count=0 in prior profile check; selected 2024-09-23 180D window clean by row continuity.", "same_entry_group_id": "C13_278280_2024-09-23", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": "same canonical allowed; hard duplicate key is new relative to recent session and local generated artifacts", "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false, "raw_component_scores_before": {"eps_fcf_explosion": 1, "earnings_visibility": 2, "bottleneck_pricing": 1, "market_mispricing": 1, "valuation_rerating": 1, "capital_allocation": 0, "information_confidence": 2, "execution_risk": -2, "accounting_trust_risk": 0, "utilization_bridge": 1, "offset_quality": 1, "ex_subsidy_margin_quality": 0}, "weighted_score_before": 64, "stage_label_before": "Stage2", "raw_component_scores_after": {"eps_fcf_explosion": 1, "earnings_visibility": 1, "bottleneck_pricing": 1, "market_mispricing": 0, "valuation_rerating": 0, "capital_allocation": 0, "information_confidence": 2, "execution_risk": -3, "accounting_trust_risk": 0, "utilization_bridge": 0, "offset_quality": 1, "ex_subsidy_margin_quality": 0, "requires_second_bridge": -3}, "weighted_score_after": 58, "stage_label_after": "Stage2_capped_watch", "component_delta_explanation": "C13 needs direct utilization/customer-pull/margin bridge for Actionable and weak-offset quality for hard 4C; otherwise use Stage2 cap or local 4B/watch."}
{"row_type": "trigger", "trigger_id": "R3L202_C13_T07_096770_2025-02-06", "case_id": "C13_SKINNO_20250206_SKON_FLAT_IRA_CAPEX_4B", "symbol": "096770", "company_name": "SK Innovation", "round": "R3", "loop": 202, "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C13_BATTERY_JV_UTILIZATION_AMPC_IRA", "fine_archetype_id": "BATTERY_JV_AMPC_UTILIZATION_DIRECT_ROW_REPAIR_V2", "sector": "battery_ev_green_mobility", "primary_archetype": "battery_jv_utilization_ampc_ira", "loop_objective": ["stage2_actionable_bonus_stress_test", "4C_thesis_break_timing_test", "holdout_validation", "counterexample_mining", "canonical_archetype_compression"], "trigger_type": "Stage4B", "trigger_date": "2025-02-06", "evidence_available_at_that_date": "same_day_or_next_tradable_close_per_timestamp_conservatism", "evidence_source": "https://www.reuters.com/business/energy/south-koreas-sk-innovation-expects-2025-refining-margins-remain-flat-2025-02-06/", "evidence_summary": "Reuters reported SK Innovation expected IRA adjustment rather than repeal and planned sizable battery capex, while the broader group remained exposed to flat refining and battery-unit execution risk. C13 treats this as 4B/watch because the battery capex route remains, but unit economics are not yet proven.", "evidence_family": "battery_capex_IRA_policy_uncertainty_multi_segment_offset", "stage2_evidence_fields": [], "stage3_evidence_fields": [], "stage4b_evidence_fields": ["utilization_pressure", "inventory_or_fixed_cost_pressure", "offset_quality_present"], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/096/096770/2025.csv", "profile_path": "atlas/symbol_profiles/096/096770.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "entry_date": "2025-02-06", "entry_price": 124500.0, "entry_open": 124500.0, "entry_high": 125500.0, "entry_low": 120900.0, "entry_volume": 180135.0, "MFE_30D_pct": 12.61, "MFE_90D_pct": 12.61, "MFE_180D_pct": 12.61, "MFE_1Y_pct": null, "MFE_2Y_pct": null, "MAE_30D_pct": -3.61, "MAE_90D_pct": -35.1, "MAE_180D_pct": -35.1, "MAE_1Y_pct": null, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2025-03-13", "peak_price": 140200.0, "drawdown_after_peak_pct": -42.37, "green_lateness_ratio": "not_applicable_no_stage3_green_trigger", "four_b_local_peak_proximity": "case_specific", "four_b_full_window_peak_proximity": "case_specific", "four_b_timing_verdict": "local_4b_or_hard_4c_boundary_audit", "four_b_evidence_type": ["utilization_pressure", "inventory_loss_or_fixed_cost_pressure", "offset_quality_present"], "four_c_protection_label": "false_break_or_watch_only", "trigger_outcome_label": "multi_segment_offset_watch", "current_profile_verdict": "4b_watch_but_positive_reopen_not_proven", "calibration_usable": true, "forward_window_trading_days": 180, "forward_available_rows_in_cached_stock_web": 254, "calibration_block_reasons": [], "corporate_action_window_status": "clean_no_candidate_overlap_180D_window", "corporate_action_profile_note": "profile candidate 2024-11-20 lies before selected 2025-02-06 entry; no overlap with 2025 forward window.", "same_entry_group_id": "C13_096770_2025-02-06", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": "same canonical allowed; hard duplicate key is new relative to recent session and local generated artifacts", "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false, "raw_component_scores_before": {"eps_fcf_explosion": 0, "earnings_visibility": -2, "bottleneck_pricing": -1, "market_mispricing": -1, "valuation_rerating": 0, "capital_allocation": 0, "information_confidence": 2, "execution_risk": -3, "accounting_trust_risk": -1, "utilization_bridge": -3, "offset_quality": 2, "ex_subsidy_margin_quality": 0}, "weighted_score_before": 53, "stage_label_before": "Stage4C_if_offset_ignored", "raw_component_scores_after": {"eps_fcf_explosion": 0, "earnings_visibility": -2, "bottleneck_pricing": -1, "market_mispricing": -1, "valuation_rerating": 0, "capital_allocation": 0, "information_confidence": 3, "execution_risk": -3, "accounting_trust_risk": -1, "utilization_bridge": -3, "offset_quality": 4, "ex_subsidy_margin_quality": 0}, "weighted_score_after": 57, "stage_label_after": "Stage4B/watch", "component_delta_explanation": "C13 needs direct utilization/customer-pull/margin bridge for Actionable and weak-offset quality for hard 4C; otherwise use Stage2 cap or local 4B/watch."}
{"row_type": "trigger", "trigger_id": "R3L202_C13_T08_051910_2025-02-07", "case_id": "C13_LGCHEM_20250204_CATHODE_MARGIN_GUIDANCE_ACTIONABLE", "symbol": "051910", "company_name": "LG Chem", "round": "R3", "loop": 202, "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C13_BATTERY_JV_UTILIZATION_AMPC_IRA", "fine_archetype_id": "BATTERY_JV_AMPC_UTILIZATION_DIRECT_ROW_REPAIR_V2", "sector": "battery_ev_green_mobility", "primary_archetype": "battery_jv_utilization_ampc_ira", "loop_objective": ["stage2_actionable_bonus_stress_test", "4C_thesis_break_timing_test", "holdout_validation", "counterexample_mining", "canonical_archetype_compression"], "trigger_type": "Stage2-Actionable", "trigger_date": "2025-02-04", "evidence_available_at_that_date": "same_day_or_next_tradable_close_per_timestamp_conservatism", "evidence_source": "https://securities.miraeasset.com/bbs/download/2134148.pdf?attachmentId=2134148", "evidence_summary": "Mirae Asset estimated cathode-material OPM at 2-3% in 4Q24 and discussed 2025 shipment/ASP guidance, giving a second bridge beyond long-lead Tennessee capex. This is a positive reopen row with a direct margin-guidance bridge.", "evidence_family": "cathode_shipments_and_OP_margin_guidance_recovery", "stage2_evidence_fields": ["utilization_recovery_or_customer_pull", "margin_guidance_or_profitability_bridge"], "stage3_evidence_fields": [], "stage4b_evidence_fields": [], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/051/051910/2025.csv", "profile_path": "atlas/symbol_profiles/051/051910.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "entry_date": "2025-02-07", "entry_price": 217000.0, "entry_open": 220000.0, "entry_high": 224500.0, "entry_low": 216000.0, "entry_volume": 322872.0, "MFE_30D_pct": 21.43, "MFE_90D_pct": 27.19, "MFE_180D_pct": 95.16, "MFE_1Y_pct": null, "MFE_2Y_pct": null, "MAE_30D_pct": -4.15, "MAE_90D_pct": -16.36, "MAE_180D_pct": -16.36, "MAE_1Y_pct": null, "below_entry_price_flag_30D": false, "below_entry_price_flag_90D": true, "peak_date": "2025-10-30", "peak_price": 423500.0, "drawdown_after_peak_pct": -8.97, "green_lateness_ratio": "not_applicable_no_stage3_green_trigger", "four_b_local_peak_proximity": "case_specific", "four_b_full_window_peak_proximity": "case_specific", "four_b_timing_verdict": "local_4b_or_hard_4c_boundary_audit", "four_b_evidence_type": [], "four_c_protection_label": "not_applicable", "trigger_outcome_label": "positive_reopen_with_margin_bridge", "current_profile_verdict": "actionable_positive_control", "calibration_usable": true, "forward_window_trading_days": 180, "forward_available_rows_in_cached_stock_web": 253, "calibration_block_reasons": [], "corporate_action_window_status": "clean_no_candidate_overlap_180D_window", "corporate_action_profile_note": "corporate_action_candidate_count=0 in prior profile check; selected 2025-02-07 180D window clean by row continuity.", "same_entry_group_id": "C13_051910_2025-02-07", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": "same canonical allowed; hard duplicate key is new relative to recent session and local generated artifacts", "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false, "raw_component_scores_before": {"eps_fcf_explosion": 2, "earnings_visibility": 4, "bottleneck_pricing": 2, "market_mispricing": 2, "valuation_rerating": 2, "capital_allocation": 1, "information_confidence": 3, "execution_risk": -2, "accounting_trust_risk": 0, "utilization_bridge": 3, "offset_quality": 2, "ex_subsidy_margin_quality": 2}, "weighted_score_before": 73, "stage_label_before": "Stage2-Actionable", "raw_component_scores_after": {"eps_fcf_explosion": 2, "earnings_visibility": 4, "bottleneck_pricing": 2, "market_mispricing": 1, "valuation_rerating": 1, "capital_allocation": 1, "information_confidence": 3, "execution_risk": -2, "accounting_trust_risk": 0, "utilization_bridge": 3, "offset_quality": 2, "ex_subsidy_margin_quality": 2, "high_mae_green_cap": -3}, "weighted_score_after": 70, "stage_label_after": "Stage2-Actionable_capped", "component_delta_explanation": "C13 needs direct utilization/customer-pull/margin bridge for Actionable and weak-offset quality for hard 4C; otherwise use Stage2 cap or local 4B/watch."}
```

## 11. Machine-readable aggregate / shadow / residual rows

```jsonl
{"row_type": "aggregate", "round": "R3", "loop": 202, "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C13_BATTERY_JV_UTILIZATION_AMPC_IRA", "new_independent_case_count": 8, "new_independent_trigger_count": 8, "unique_symbol_count": 8, "positive_case_count": 3, "counterexample_count": 5, "stage4b_case_count": 3, "stage4c_case_count": 1, "stage2_or_actionable_count": 4, "source_proxy_only_count": 0, "evidence_url_pending_count": 0, "missing_required_mfe_mae_count": 0, "corporate_action_contaminated_180D_count": 0, "insufficient_forward_window_180D_count": 0, "production_scoring_changed": false, "shadow_weight_only": true}
{"row_type": "shadow_weight", "round": "R3", "loop": 202, "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C13_BATTERY_JV_UTILIZATION_AMPC_IRA", "rule_candidate": "C13_UTILIZATION_CUSTOMER_PULL_AND_OFFSET_QUALITY_GATE", "do_not_propose_new_weight_delta": false, "production_scoring_changed": false, "shadow_weight_only": true, "suggested_patch_axis": "stage2_required_bridge + local_4b_watch_guard + earlier_thesis_break_watch", "component_direction": {"earnings_visibility": "requires direct shipment/utilization or margin guidance", "information_confidence": "up when direct company/IR source exists", "valuation_rerating": "capped under high MAE", "execution_risk": "more negative under utilization collapse", "offset_quality": "separates 4B/watch from hard 4C"}}
{"row_type": "residual_contribution", "round": "R3", "loop": 202, "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C13_BATTERY_JV_UTILIZATION_AMPC_IRA", "loop_contribution_label": "C13_utilization_customer_pull_and_offset_quality_direct_url_repair", "existing_axis_strengthened": ["stage2_required_bridge", "local_4b_watch_guard", "earlier_thesis_break_watch"], "existing_axis_refined": ["hard_4c_requires_weak_offset_quality", "high_mae_true_positive_green_cap"], "new_axis_proposed": false, "production_scoring_changed": false}
```

## 12. Batch Ingest Self-Audit

```text
filename_regex_valid: true
filename_round_matches_metadata: true
filename_loop_matches_metadata: true
round_sector_consistency: pass
canonical_archetype_valid: true
large_sector_id_valid: true
selected_round_from_archetype: R3
stock_web_manifest_checked: true
stock_web_schema_checked: true
actual_1D_OHLCV_rows_used: true
entry_row_exists_for_all_triggers: true
complete_30_90_180_mfe_mae_for_all_triggers: true
trigger_rows_missing_required_price_fields: 0
calibration_usable_trigger_count: 8
corporate_action_contaminated_180D_count: 0
insufficient_forward_window_180D_count: 0
hard_duplicate_key_reused_in_this_batch: false
minimum_new_independent_case_ratio_met: true
minimum_new_symbol_count_met: true
positive_and_counterexample_balance_met: true
source_proxy_only_count: 0
evidence_url_pending_count: 0
production_scoring_changed: false
handoff_prompt_executed_now: false
ready_for_batch_ingest: true
```

## 13. Deferred Coding Agent Handoff Prompt

```text
Do not execute during this research session.

Later coding-agent task:
Read this MD together with other v12 result MDs under docs/round and docs/round/achieve using --include-archive.
Parse JSONL trigger rows and aggregate/shadow rows.
Validate hard duplicate keys:
canonical_archetype_id + symbol + trigger_type + entry_date.
If rows pass validation, add them to v12 calibration corpus.
Do not change production scoring from this single MD alone.
Treat rule candidate C13_UTILIZATION_CUSTOMER_PULL_AND_OFFSET_QUALITY_GATE as shadow evidence only until confirmed across other C13 batches.
```

## 14. Next Research State

```text
completed_round: R3
completed_loop: 202
selection_basis: docs/core/V12_Research_No_Repeat_Index.md
selected_priority_bucket: Priority 1 balance reinforcement / AMPC·IRA durability and JV utilization failure repair
round_schedule_status: coverage_index_selected
round_sector_consistency: pass

next_recommended_archetypes:
- C05_EPC_MEGA_CONTRACT_MARGIN_GAP_HARD_4C_DIRECT_BREAK_ONLY
- C01_ORDER_BACKLOG_MARGIN_BRIDGE_WORKING_CAPITAL_CASHFLOW_ONLY_REPAIR
- C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE_SUPPLIER_ORDER_DIRECT_URL_REPAIR
- R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL_HOLDOUT_REFRESH
- C13_BATTERY_JV_UTILIZATION_AMPC_IRA_EX_SUBSIDY_MARGIN_DIRECT_REPAIR
```
