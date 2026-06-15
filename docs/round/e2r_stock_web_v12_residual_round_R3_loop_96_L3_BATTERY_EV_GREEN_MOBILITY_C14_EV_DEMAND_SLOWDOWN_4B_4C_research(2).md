# E2R Stock-Web Historical Calibration / Sector-Archetype Residual Research — R3 loop 96 C14

```yaml
research_session: post_calibrated_sector_archetype_residual_research
mode: historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12
output_format: one_standalone_markdown_file
selected_round: R3
selected_loop: 96
selected_priority_bucket: Priority 0
selection_basis: docs/core/V12_Research_No_Repeat_Index.md
large_sector_id: L3_BATTERY_EV_GREEN_MOBILITY
canonical_archetype_id: C14_EV_DEMAND_SLOWDOWN_4B_4C
fine_archetype_id: C14_BATTERY_MATERIAL_EQUIPMENT_EV_DEMAND_RESET_RECOVERY_EXCEPTION_FILTER
deep_sub_archetype_id: C14_DEEP_2024_EV_DEMAND_SLOWDOWN_HARD_4C_VS_CAPEX_EQUIPMENT_RECOVERY_MFE_EXCEPTION
primary_price_source: Songdaiki/stock-web
upstream_source: FinanceData/marcap
price_basis: tradable_raw
price_adjustment_status: raw_unadjusted_marcap
production_scoring_changed: false
shadow_weight_only: true
handoff_prompt_embedded: true
handoff_prompt_executed_now: false
stock_agent_code_access_allowed: false
stock_agent_code_patch_allowed: false
stock_agent_live_scan_allowed: false
auto_trading_allowed: false
```

## 0. Executive summary

This run continues the Priority 0 C14 gap fill after the earlier loop 95. The no-repeat ledger reports `C14_EV_DEMAND_SLOWDOWN_4B_4C` at 11 rows, and this local batch has already added loop 95, so the archetype is still under the 30-row stability zone. This file intentionally avoids the loop 95 symbols (`361610`, `278280`, `005070`, `348370`, `006400`) and uses a different 2024 regime split: late-2024 battery-material hard breaks versus spring/summer battery capex recovery exceptions.

The residual finding is simple: **EV demand slowdown is not a universal hard-4C switch**. It behaves like a floodgate with two doors. Battery materials that enter a margin/utilization reset after late-2024 can go almost straight into hard drawdown with low MFE. Battery equipment or mixed-platform names can still produce large 30D/90D MFE before any final fade. The proposed C14-specific rule is therefore: **route to Stage4C only when utilization/call-off/margin break is confirmed and the recovery-MFE band is absent; if recovery MFE appears before non-price break confirmation, keep it at Stage4B watch.**

## 1. Prompt compliance gate

```text
current_stock_discovery_allowed = false
live_candidate_mode = false
auto_trading_allowed = false
brokerage_api_allowed = false
stock_agent_code_access_allowed = false
stock_agent_code_patch_allowed = false
production_scoring_changed = false
shadow_weight_only = true
must_use_actual_stock_web_1D_OHLC = true
must_include_backtest_result = true
must_include_positive_and_counterexample_balance = true
must_output_every_usable_trigger_as_jsonl = true
must_include_complete_30_90_180_mfe_mae_in_every_trigger_row = true
trigger_type_must_be_canonical_stage_label = true
```

## 2. Coverage-index scheduler decision

- Scheduler mode: `coverage_index_first`
- Sequential R1~R13 cycle used: `false`
- Selected canonical: `C14_EV_DEMAND_SLOWDOWN_4B_4C`
- Derived round: `R3`
- Derived large sector: `L3_BATTERY_EV_GREEN_MOBILITY`
- Current no-repeat ledger row count for C14: `11`
- Local-session C14 contribution before this file: loop 95 added `5` usable trigger rows
- Local adjusted estimate before this file: `16`
- This loop adds: `7` usable trigger rows
- Local adjusted estimate after this file: `23`
- Need to 30 after this file: `7`
- Investigation point from ledger: EV demand slowdown, utilization, call-off, hard 4C confirmation
- Selected loop rule: prior local C14 loop `95` + 1 = `96`

## 3. Price source validation

```json
{"row_type": "price_source_validation", "price_data_source": "Songdaiki/stock-web", "upstream_source": "FinanceData/marcap", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "manifest_max_date": "2026-02-20", "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "raw_shard_root": "atlas/ohlcv_raw_by_symbol_year", "tradable_row_count": 14354401, "raw_row_count": 15214118, "symbol_count": 5414, "must_use_actual_stock_web_1D_OHLC": true, "manifest_url": "https://raw.githubusercontent.com/Daikisong/stock-web/main/atlas/manifest.json"}
```

Manifest fields checked:

| field | value |
|---|---|
| source_name | FinanceData/marcap |
| price_adjustment_status | raw_unadjusted_marcap |
| min_date | 1995-05-02 |
| max_date | 2026-02-20 |
| tradable_row_count | 14354401 |
| raw_row_count | 15214118 |
| symbol_count | 5414 |
| active_like_symbol_count | 2868 |
| inactive_or_delisted_like_symbol_count | 2546 |
| calibration_shard_root | atlas/ohlcv_tradable_by_symbol_year |
| raw_shard_root | atlas/ohlcv_raw_by_symbol_year |

## 4. Symbol profile and corporate-action gate

| case_id | symbol | name | profile_last_date | profile_corporate_action_candidate_count | corporate_action_candidate_dates | corporate_action_contaminated_180D_window | price_shards |
| --- | --- | --- | --- | --- | --- | --- | --- |
| C14-R3L96-01 | 051910 | LG화학 | 2026-02-20 | 0 | [] | False | ['atlas/ohlcv_tradable_by_symbol_year/051/051910/2024.csv','atlas/ohlcv_tradable_by_symbol_year/051/051910/2025.csv'] |
| C14-R3L96-02 | 020150 | 롯데에너지머티리얼즈 | 2026-02-20 | 0 | [] | False | ['atlas/ohlcv_tradable_by_symbol_year/020/020150/2024.csv','atlas/ohlcv_tradable_by_symbol_year/020/020150/2025.csv'] |
| C14-R3L96-03 | 093370 | 후성 | 2026-02-20 | 0 | [] | False | ['atlas/ohlcv_tradable_by_symbol_year/093/093370/2024.csv','atlas/ohlcv_tradable_by_symbol_year/093/093370/2025.csv'] |
| C14-R3L96-04 | 121600 | 나노신소재 | 2026-02-20 | 1 | ["2015-12-17"] | False | ['atlas/ohlcv_tradable_by_symbol_year/121/121600/2024.csv','atlas/ohlcv_tradable_by_symbol_year/121/121600/2025.csv'] |
| C14-R3L96-05 | 137400 | 피엔티 | 2026-02-20 | 4 | ["2012-11-30", "2012-12-26", "2019-05-07", "2019-05-30"] | False | ['atlas/ohlcv_tradable_by_symbol_year/137/137400/2024.csv','atlas/ohlcv_tradable_by_symbol_year/137/137400/2025.csv'] |
| C14-R3L96-06 | 011790 | SKC | 2026-02-20 | 2 | ["1998-01-03", "2001-12-21"] | False | ['atlas/ohlcv_tradable_by_symbol_year/011/011790/2024.csv','atlas/ohlcv_tradable_by_symbol_year/011/011790/2025.csv'] |
| C14-R3L96-07 | 222080 | 씨아이에스 | 2026-02-20 | 1 | ["2017-01-20"] | False | ['atlas/ohlcv_tradable_by_symbol_year/222/222080/2024.csv','atlas/ohlcv_tradable_by_symbol_year/222/222080/2025.csv'] |

Interpretation:

- `051910`, `020150`, and `093370` have no atlas corporate-action candidate dates.
- `121600`, `137400`, `011790`, and `222080` have candidate dates, but all are before the 2024/2025 entry-to-D+180 windows used here.
- No selected entry-to-D+180 window overlaps atlas corporate-action candidate dates.
- All seven cases are marked `calibration_usable=true` for 30D/90D/180D trigger-level path analysis.
- Evidence is intentionally marked `source_proxy_only=true` and `evidence_url_pending=true`; this file proposes a shadow rule candidate, not a production patch.

## 5. Canonical compression map

```text
large_sector_id = L3_BATTERY_EV_GREEN_MOBILITY
canonical_archetype_id = C14_EV_DEMAND_SLOWDOWN_4B_4C

fine/deep map:
- C14_LATE_2024_BATTERY_MATERIAL_MARGIN_RESET_HARD_4C
  -> C14_DEEP_CATHODE_COPPERFOIL_ELECTROLYTE_CNT_NO_RECOVERY_MFE
- C14_SPRING_2024_BATTERY_CAPEX_EQUIPMENT_RECOVERY_EXCEPTION
  -> C14_DEEP_EQUIPMENT_ORDER_VISIBILITY_RECOVERY_MFE_BEFORE_LATER_FADE
- C14_AUGUST_2024_MACRO_SHOCK_FALSE_HARD_4C
  -> C14_DEEP_MACRO_SELLDOWN_LOCAL_RECOVERY_BEFORE_THESIS_BREAK
```

## 6. Duplicate avoidance

Hard duplicate key format:

```text
canonical_archetype_id + symbol + trigger_type + entry_date
```

New keys used:

```text
C14_EV_DEMAND_SLOWDOWN_4B_4C|051910|Stage4C|2024-10-29
C14_EV_DEMAND_SLOWDOWN_4B_4C|020150|Stage4C|2024-10-29
C14_EV_DEMAND_SLOWDOWN_4B_4C|093370|Stage4C|2024-10-29
C14_EV_DEMAND_SLOWDOWN_4B_4C|121600|Stage4C|2024-10-29
C14_EV_DEMAND_SLOWDOWN_4B_4C|137400|Stage4B|2024-04-30
C14_EV_DEMAND_SLOWDOWN_4B_4C|011790|Stage4B|2024-04-30
C14_EV_DEMAND_SLOWDOWN_4B_4C|222080|Stage4B|2024-08-05
```

The prior local C14 loop 95 used `361610`, `278280`, `005070`, `348370`, and `006400`; none are reused here. The older visible compact loop 94 symbol set cited in loop 95 is also not reused directly.

## 7. Case set balance

| case_id | symbol | name | case_role | trigger_type | entry_date | entry_price | MFE_30D_pct | MFE_90D_pct | MFE_180D_pct | MAE_30D_pct | MAE_90D_pct | MAE_180D_pct | current_profile_verdict |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| C14-R3L96-01 | 051910 | LG화학 | positive_hard_4c | Stage4C | 2024-10-29 | 318500 | 4.4 | 4.4 | 4.4 | -22.76 | -34.69 | -43.01 | current_profile_correct |
| C14-R3L96-02 | 020150 | 롯데에너지머티리얼즈 | positive_hard_4c | Stage4C | 2024-10-29 | 38150 | 2.49 | 2.49 | 2.49 | -45.22 | -46.92 | -48.99 | current_profile_correct |
| C14-R3L96-03 | 093370 | 후성 | positive_hard_4c | Stage4C | 2024-10-29 | 6130 | 2.77 | 2.77 | 2.77 | -25.2 | -29.04 | -38.01 | current_profile_correct |
| C14-R3L96-04 | 121600 | 나노신소재 | positive_hard_4c_with_small_recovery_mfe | Stage4C | 2024-10-29 | 85300 | 8.79 | 8.79 | 8.79 | -31.07 | -33.06 | -48.24 | current_profile_correct_but_requires_recovery_band_cap |
| C14-R3L96-05 | 137400 | 피엔티 | counterexample_false_hard_4c | Stage4B | 2024-04-30 | 40250 | 111.18 | 122.36 | 122.36 | -0.99 | -0.99 | -9.07 | current_profile_false_positive_if_hard_4c_without_recovery_filter |
| C14-R3L96-06 | 011790 | SKC | counterexample_false_hard_4c | Stage4B | 2024-04-30 | 110400 | 81.07 | 81.16 | 81.16 | -8.24 | -8.24 | -18.21 | current_profile_false_positive_if_hard_4c_without_recovery_filter |
| C14-R3L96-07 | 222080 | 씨아이에스 | counterexample_false_hard_4c | Stage4B | 2024-08-05 | 8000 | 52.88 | 52.88 | 52.88 | -2.5 | -11.88 | -18.75 | current_profile_false_positive_if_hard_4c_on_macro_price_shock |

Balance summary:

```text
trigger_row_count = 7
calibration_usable_trigger_count = 7
new_independent_case_count = 7
reused_case_count = 0
new_symbol_count = 7
same_archetype_new_symbol_count = 7
same_archetype_new_trigger_family_count = 3
positive_case_count = 4
counterexample_count = 3
Stage4C_case_count = 4
Stage4B_case_count = 3
current_profile_error_count = 3
source_proxy_only_count = 7
evidence_url_pending_count = 7
```

## 8. OHLC backtest grid

| case_id | symbol | entry_date | entry_price | peak_price_30D | peak_date_30D | min_price_30D | min_date_30D | peak_price_90D | min_price_90D | min_date_90D | peak_price_180D | min_price_180D | min_date_180D | drawdown_after_peak_180D_pct |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| C14-R3L96-01 | 051910 | 2024-10-29 | 318500 | 332500 | 2024-10-29 | 246000 | 2024-12-09 | 332500 | 208000 | 2025-02-10 | 332500 | 181500 | 2025-05-26 | -45.41 |
| C14-R3L96-02 | 020150 | 2024-10-29 | 38150 | 39100 | 2024-10-30 | 20900 | 2024-12-09 | 39100 | 20250 | 2025-02-03 | 39100 | 19460 | 2025-05-22 | -50.23 |
| C14-R3L96-03 | 093370 | 2024-10-29 | 6130 | 6300 | 2024-11-05 | 4585 | 2024-11-15 | 6300 | 4350 | 2025-03-11 | 6300 | 3800 | 2025-04-09 | -39.68 |
| C14-R3L96-04 | 121600 | 2024-10-29 | 85300 | 92800 | 2024-11-06 | 58800 | 2024-12-09 | 92800 | 57100 | 2025-01-02 | 92800 | 44150 | 2025-05-27 | -52.42 |
| C14-R3L96-05 | 137400 | 2024-04-30 | 40250 | 85000 | 2024-06-13 | 39850 | 2024-05-02 | 89500 | 39850 | 2024-05-02 | 89500 | 36600 | 2024-12-30 | -59.11 |
| C14-R3L96-06 | 011790 | 2024-04-30 | 110400 | 199900 | 2024-06-14 | 101300 | 2024-05-17 | 200000 | 101300 | 2024-05-17 | 200000 | 90300 | 2024-12-09 | -54.85 |
| C14-R3L96-07 | 222080 | 2024-08-05 | 8000 | 12230 | 2024-08-20 | 7800 | 2024-08-05 | 12230 | 7050 | 2024-12-09 | 12230 | 6500 | 2025-04-09 | -46.85 |

### Price-path reading

- `051910`, `020150`, `093370`, and `121600`: late-2024 material-exposure entries show low MFE and large 30D/90D/180D MAE. These support hard-4C routing only when a non-price utilization/call-off/margin break is confirmed.
- `137400`, `011790`, and `222080`: broad EV slowdown or macro shock mapped directly to hard 4C would have failed. Their 30D/90D MFE windows were too large to justify immediate hard 4C without a confirmed thesis break.
- The C14 rule should therefore include a recovery-MFE exception band. This does not cancel hard 4C; it says hard 4C should wait until the non-price break and recovery-band test point in the same direction.

## 9. Current calibrated profile stress test

Current proxy assumptions:

```text
stage2_actionable_evidence_bonus = +2.0
stage3_yellow_total_min = 75.0
stage3_green_total_min = 87.0
stage3_green_revision_min = 55.0
stage3_cross_evidence_green_buffer = +1.5
price_only_blowoff_blocks_positive_stage = true
full_4b_requires_non_price_evidence = true
hard_4c_thesis_break_routes_to_4c = true
```

Stress-test answers:

1. The current profile is directionally correct for material names where a non-price thesis break is present.
2. It remains vulnerable when a broad EV macro-slowdown proxy is treated as sufficient for hard 4C across equipment/order-visibility names.
3. Stage2-actionable bonus is not the main issue in this file; the residual is 4B/4C routing.
4. Yellow/Green thresholds are not loosened.
5. Price-only blowoff guard remains useful, but C14 also needs a **price-recovery exception guard** on the downside.
6. Full 4B non-price requirement is strengthened: recovery MFE without non-price break should stay watch-level.
7. Hard 4C routing should be recovery-band filtered for C14.

## 10. Score / return alignment and raw component score breakdown

| case_id | symbol | trigger_type | current_total_proxy | shadow_total_proxy | component_breakdown | score_return_alignment |
| --- | --- | --- | --- | --- | --- | --- |
| C14-R3L96-01 | 051910 | Stage4C | 74 | 68 | {"EPS/revision": 18, "visibility": 18, "bottleneck": 10, "mispricing": 8, "valuation": 5, "capital": 6, "info_confidence": 35} | aligned_hard_4c |
| C14-R3L96-02 | 020150 | Stage4C | 74 | 68 | {"EPS/revision": 18, "visibility": 18, "bottleneck": 10, "mispricing": 8, "valuation": 5, "capital": 6, "info_confidence": 35} | aligned_hard_4c |
| C14-R3L96-03 | 093370 | Stage4C | 74 | 68 | {"EPS/revision": 18, "visibility": 18, "bottleneck": 10, "mispricing": 8, "valuation": 5, "capital": 6, "info_confidence": 35} | aligned_hard_4c |
| C14-R3L96-04 | 121600 | Stage4C | 72 | 65 | {"EPS/revision": 16, "visibility": 15, "bottleneck": 10, "mispricing": 8, "valuation": 6, "capital": 6, "info_confidence": 28} | aligned_hard_4c |
| C14-R3L96-05 | 137400 | Stage4B | 82 | 73 | {"EPS/revision": 18, "visibility": 22, "bottleneck": 16, "mispricing": 14, "valuation": 10, "capital": 8, "info_confidence": 22} | hard_4c_would_be_false_positive_due_to_recovery_mfe |
| C14-R3L96-06 | 011790 | Stage4B | 82 | 73 | {"EPS/revision": 18, "visibility": 22, "bottleneck": 16, "mispricing": 14, "valuation": 10, "capital": 8, "info_confidence": 22} | hard_4c_would_be_false_positive_due_to_recovery_mfe |
| C14-R3L96-07 | 222080 | Stage4B | 82 | 73 | {"EPS/revision": 18, "visibility": 22, "bottleneck": 16, "mispricing": 14, "valuation": 10, "capital": 8, "info_confidence": 22} | hard_4c_would_be_false_positive_due_to_recovery_mfe |

Interpretation:

- The hard-4C material cases align with low MFE and high MAE, so the shadow profile does not weaken `hard_4c_confirmation`.
- The capex/equipment recovery exceptions show why C14 should not use a single broad EV slowdown label as a hard 4C switch.
- This is a canonical-archetype-specific filter, not a global scoring relaxation.

## 11. Machine-readable rows — trigger JSONL

```jsonl
{"MAE_180D_pct": -43.01, "MAE_30D_pct": -22.76, "MAE_90D_pct": -34.69, "MFE_180D_pct": 4.4, "MFE_30D_pct": 4.4, "MFE_90D_pct": 4.4, "aggregate_group_role": "representative", "below_entry_price_flag_180D": true, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "calibration_block_reasons": [], "calibration_usable": true, "canonical_archetype_id": "C14_EV_DEMAND_SLOWDOWN_4B_4C", "case_id": "C14-R3L96-01", "case_role": "positive_hard_4c", "corporate_action_candidate_dates": [], "corporate_action_window_status": "not_contaminated", "current_profile_error": false, "current_profile_total_score_proxy": 74, "current_profile_verdict": "current_profile_correct", "dedupe_for_aggregate": true, "deep_sub_archetype_id": "C14_DEEP_2024_EV_DEMAND_SLOWDOWN_HARD_4C_VS_CAPEX_EQUIPMENT_RECOVERY_MFE_EXCEPTION", "do_not_count_as_new_case": false, "drawdown_after_peak_min_date": "2025-05-26", "drawdown_after_peak_min_price": 181500, "drawdown_after_peak_pct": -45.41, "entry_date": "2024-10-29", "entry_price": 318500, "entry_price_basis": "close", "evidence_family": "battery_chemical_material_demand_margin_reset", "evidence_url_pending": true, "fine_archetype_id": "C14_BATTERY_MATERIAL_EQUIPMENT_EV_DEMAND_RESET_RECOVERY_EXCEPTION_FILTER", "forward_window_trading_days": 180, "independent_evidence_weight": 1.0, "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "market": "KOSPI", "min_date_180D": "2025-05-26", "min_date_30D": "2024-12-09", "min_date_90D": "2025-02-10", "min_price_180D": 181500, "min_price_30D": 246000, "min_price_90D": 208000, "name": "LG화학", "peak_date": "2024-10-29", "peak_date_180D": "2024-10-29", "peak_date_30D": "2024-10-29", "peak_date_90D": "2024-10-29", "peak_price": 332500, "peak_price_180D": 332500, "peak_price_30D": 332500, "peak_price_90D": 332500, "price_adjustment_status": "raw_unadjusted_marcap", "price_basis": "tradable_raw", "price_data_source": "Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/051/051910/2024.csv; atlas/ohlcv_tradable_by_symbol_year/051/051910/2025.csv", "price_source": "Songdaiki/stock-web", "profile_path": "atlas/symbol_profiles/051/051910.json", "raw_component_score_breakdown": {"EPS/revision": 18, "bottleneck": 10, "capital": 6, "info_confidence": 35, "mispricing": 8, "valuation": 5, "visibility": 18}, "research_file": "e2r_stock_web_v12_residual_round_R3_loop_96_L3_BATTERY_EV_GREEN_MOBILITY_C14_EV_DEMAND_SLOWDOWN_4B_4C_research.md", "residual_contribution": "hard_4c_recovery_band_filter", "reuse_reason": "none_new_symbol_or_new_trigger_family_for_c14_loop96", "row_type": "trigger", "same_entry_group_id": "C14_EV_DEMAND_SLOWDOWN_4B_4C|051910|Stage4C|2024-10-29", "score_return_alignment": "aligned_hard_4c", "selected_loop": 96, "selected_priority_bucket": "Priority 0", "selected_round": "R3", "shadow_profile_total_score_proxy": 68, "source_proxy_only": true, "stage2_evidence_fields": [], "stage3_evidence_fields": [], "stage4b_evidence_fields": ["macro_ev_slowdown_pressure", "price_only_local_peak_watch", "valuation_or_positioning_watch"], "stage4c_evidence_fields": ["utilization_or_margin_break_required", "demand_or_calloff_reset_required", "hard_thesis_break_only_after_non_price_confirmation"], "stock_web_manifest_max_date": "2026-02-20", "symbol": "051910", "trigger_date": "2024-10-29", "trigger_family": "late_2024_ev_material_margin_reset", "trigger_outcome_label": "confirmed_demand_slowdown_margin_reset_hard_4c", "trigger_type": "Stage4C", "upstream_source": "FinanceData/marcap"}
{"MAE_180D_pct": -48.99, "MAE_30D_pct": -45.22, "MAE_90D_pct": -46.92, "MFE_180D_pct": 2.49, "MFE_30D_pct": 2.49, "MFE_90D_pct": 2.49, "aggregate_group_role": "representative", "below_entry_price_flag_180D": true, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "calibration_block_reasons": [], "calibration_usable": true, "canonical_archetype_id": "C14_EV_DEMAND_SLOWDOWN_4B_4C", "case_id": "C14-R3L96-02", "case_role": "positive_hard_4c", "corporate_action_candidate_dates": [], "corporate_action_window_status": "not_contaminated", "current_profile_error": false, "current_profile_total_score_proxy": 74, "current_profile_verdict": "current_profile_correct", "dedupe_for_aggregate": true, "deep_sub_archetype_id": "C14_DEEP_2024_EV_DEMAND_SLOWDOWN_HARD_4C_VS_CAPEX_EQUIPMENT_RECOVERY_MFE_EXCEPTION", "do_not_count_as_new_case": false, "drawdown_after_peak_min_date": "2025-05-22", "drawdown_after_peak_min_price": 19460, "drawdown_after_peak_pct": -50.23, "entry_date": "2024-10-29", "entry_price": 38150, "entry_price_basis": "close", "evidence_family": "copper_foil_utilization_margin_break", "evidence_url_pending": true, "fine_archetype_id": "C14_BATTERY_MATERIAL_EQUIPMENT_EV_DEMAND_RESET_RECOVERY_EXCEPTION_FILTER", "forward_window_trading_days": 180, "independent_evidence_weight": 1.0, "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "market": "KOSPI", "min_date_180D": "2025-05-22", "min_date_30D": "2024-12-09", "min_date_90D": "2025-02-03", "min_price_180D": 19460, "min_price_30D": 20900, "min_price_90D": 20250, "name": "롯데에너지머티리얼즈", "peak_date": "2024-10-30", "peak_date_180D": "2024-10-30", "peak_date_30D": "2024-10-30", "peak_date_90D": "2024-10-30", "peak_price": 39100, "peak_price_180D": 39100, "peak_price_30D": 39100, "peak_price_90D": 39100, "price_adjustment_status": "raw_unadjusted_marcap", "price_basis": "tradable_raw", "price_data_source": "Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/020/020150/2024.csv; atlas/ohlcv_tradable_by_symbol_year/020/020150/2025.csv", "price_source": "Songdaiki/stock-web", "profile_path": "atlas/symbol_profiles/020/020150.json", "raw_component_score_breakdown": {"EPS/revision": 18, "bottleneck": 10, "capital": 6, "info_confidence": 35, "mispricing": 8, "valuation": 5, "visibility": 18}, "research_file": "e2r_stock_web_v12_residual_round_R3_loop_96_L3_BATTERY_EV_GREEN_MOBILITY_C14_EV_DEMAND_SLOWDOWN_4B_4C_research.md", "residual_contribution": "hard_4c_recovery_band_filter", "reuse_reason": "none_new_symbol_or_new_trigger_family_for_c14_loop96", "row_type": "trigger", "same_entry_group_id": "C14_EV_DEMAND_SLOWDOWN_4B_4C|020150|Stage4C|2024-10-29", "score_return_alignment": "aligned_hard_4c", "selected_loop": 96, "selected_priority_bucket": "Priority 0", "selected_round": "R3", "shadow_profile_total_score_proxy": 68, "source_proxy_only": true, "stage2_evidence_fields": [], "stage3_evidence_fields": [], "stage4b_evidence_fields": ["macro_ev_slowdown_pressure", "price_only_local_peak_watch", "valuation_or_positioning_watch"], "stage4c_evidence_fields": ["utilization_or_margin_break_required", "demand_or_calloff_reset_required", "hard_thesis_break_only_after_non_price_confirmation"], "stock_web_manifest_max_date": "2026-02-20", "symbol": "020150", "trigger_date": "2024-10-29", "trigger_family": "late_2024_ev_material_margin_reset", "trigger_outcome_label": "copper_foil_demand_slowdown_hard_4c", "trigger_type": "Stage4C", "upstream_source": "FinanceData/marcap"}
{"MAE_180D_pct": -38.01, "MAE_30D_pct": -25.2, "MAE_90D_pct": -29.04, "MFE_180D_pct": 2.77, "MFE_30D_pct": 2.77, "MFE_90D_pct": 2.77, "aggregate_group_role": "representative", "below_entry_price_flag_180D": true, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "calibration_block_reasons": [], "calibration_usable": true, "canonical_archetype_id": "C14_EV_DEMAND_SLOWDOWN_4B_4C", "case_id": "C14-R3L96-03", "case_role": "positive_hard_4c", "corporate_action_candidate_dates": [], "corporate_action_window_status": "not_contaminated", "current_profile_error": false, "current_profile_total_score_proxy": 74, "current_profile_verdict": "current_profile_correct", "dedupe_for_aggregate": true, "deep_sub_archetype_id": "C14_DEEP_2024_EV_DEMAND_SLOWDOWN_HARD_4C_VS_CAPEX_EQUIPMENT_RECOVERY_MFE_EXCEPTION", "do_not_count_as_new_case": false, "drawdown_after_peak_min_date": "2025-04-09", "drawdown_after_peak_min_price": 3800, "drawdown_after_peak_pct": -39.68, "entry_date": "2024-10-29", "entry_price": 6130, "entry_price_basis": "close", "evidence_family": "electrolyte_chemical_spread_demand_reset", "evidence_url_pending": true, "fine_archetype_id": "C14_BATTERY_MATERIAL_EQUIPMENT_EV_DEMAND_RESET_RECOVERY_EXCEPTION_FILTER", "forward_window_trading_days": 180, "independent_evidence_weight": 1.0, "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "market": "KOSPI", "min_date_180D": "2025-04-09", "min_date_30D": "2024-11-15", "min_date_90D": "2025-03-11", "min_price_180D": 3800, "min_price_30D": 4585, "min_price_90D": 4350, "name": "후성", "peak_date": "2024-11-05", "peak_date_180D": "2024-11-05", "peak_date_30D": "2024-11-05", "peak_date_90D": "2024-11-05", "peak_price": 6300, "peak_price_180D": 6300, "peak_price_30D": 6300, "peak_price_90D": 6300, "price_adjustment_status": "raw_unadjusted_marcap", "price_basis": "tradable_raw", "price_data_source": "Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/093/093370/2024.csv; atlas/ohlcv_tradable_by_symbol_year/093/093370/2025.csv", "price_source": "Songdaiki/stock-web", "profile_path": "atlas/symbol_profiles/093/093370.json", "raw_component_score_breakdown": {"EPS/revision": 18, "bottleneck": 10, "capital": 6, "info_confidence": 35, "mispricing": 8, "valuation": 5, "visibility": 18}, "research_file": "e2r_stock_web_v12_residual_round_R3_loop_96_L3_BATTERY_EV_GREEN_MOBILITY_C14_EV_DEMAND_SLOWDOWN_4B_4C_research.md", "residual_contribution": "hard_4c_recovery_band_filter", "reuse_reason": "none_new_symbol_or_new_trigger_family_for_c14_loop96", "row_type": "trigger", "same_entry_group_id": "C14_EV_DEMAND_SLOWDOWN_4B_4C|093370|Stage4C|2024-10-29", "score_return_alignment": "aligned_hard_4c", "selected_loop": 96, "selected_priority_bucket": "Priority 0", "selected_round": "R3", "shadow_profile_total_score_proxy": 68, "source_proxy_only": true, "stage2_evidence_fields": [], "stage3_evidence_fields": [], "stage4b_evidence_fields": ["macro_ev_slowdown_pressure", "price_only_local_peak_watch", "valuation_or_positioning_watch"], "stage4c_evidence_fields": ["utilization_or_margin_break_required", "demand_or_calloff_reset_required", "hard_thesis_break_only_after_non_price_confirmation"], "stock_web_manifest_max_date": "2026-02-20", "symbol": "093370", "trigger_date": "2024-10-29", "trigger_family": "late_2024_ev_material_margin_reset", "trigger_outcome_label": "electrolyte_chemical_downcycle_hard_4c", "trigger_type": "Stage4C", "upstream_source": "FinanceData/marcap"}
{"MAE_180D_pct": -48.24, "MAE_30D_pct": -31.07, "MAE_90D_pct": -33.06, "MFE_180D_pct": 8.79, "MFE_30D_pct": 8.79, "MFE_90D_pct": 8.79, "aggregate_group_role": "representative", "below_entry_price_flag_180D": true, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "calibration_block_reasons": [], "calibration_usable": true, "canonical_archetype_id": "C14_EV_DEMAND_SLOWDOWN_4B_4C", "case_id": "C14-R3L96-04", "case_role": "positive_hard_4c_with_small_recovery_mfe", "corporate_action_candidate_dates": ["2015-12-17"], "corporate_action_window_status": "not_contaminated", "current_profile_error": false, "current_profile_total_score_proxy": 72, "current_profile_verdict": "current_profile_correct_but_requires_recovery_band_cap", "dedupe_for_aggregate": true, "deep_sub_archetype_id": "C14_DEEP_2024_EV_DEMAND_SLOWDOWN_HARD_4C_VS_CAPEX_EQUIPMENT_RECOVERY_MFE_EXCEPTION", "do_not_count_as_new_case": false, "drawdown_after_peak_min_date": "2025-05-27", "drawdown_after_peak_min_price": 44150, "drawdown_after_peak_pct": -52.42, "entry_date": "2024-10-29", "entry_price": 85300, "entry_price_basis": "close", "evidence_family": "advanced_battery_material_margin_reset", "evidence_url_pending": true, "fine_archetype_id": "C14_BATTERY_MATERIAL_EQUIPMENT_EV_DEMAND_RESET_RECOVERY_EXCEPTION_FILTER", "forward_window_trading_days": 180, "independent_evidence_weight": 1.0, "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "market": "KOSDAQ", "min_date_180D": "2025-05-27", "min_date_30D": "2024-12-09", "min_date_90D": "2025-01-02", "min_price_180D": 44150, "min_price_30D": 58800, "min_price_90D": 57100, "name": "나노신소재", "peak_date": "2024-11-06", "peak_date_180D": "2024-11-06", "peak_date_30D": "2024-11-06", "peak_date_90D": "2024-11-06", "peak_price": 92800, "peak_price_180D": 92800, "peak_price_30D": 92800, "peak_price_90D": 92800, "price_adjustment_status": "raw_unadjusted_marcap", "price_basis": "tradable_raw", "price_data_source": "Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/121/121600/2024.csv; atlas/ohlcv_tradable_by_symbol_year/121/121600/2025.csv", "price_source": "Songdaiki/stock-web", "profile_path": "atlas/symbol_profiles/121/121600.json", "raw_component_score_breakdown": {"EPS/revision": 16, "bottleneck": 10, "capital": 6, "info_confidence": 28, "mispricing": 8, "valuation": 6, "visibility": 15}, "research_file": "e2r_stock_web_v12_residual_round_R3_loop_96_L3_BATTERY_EV_GREEN_MOBILITY_C14_EV_DEMAND_SLOWDOWN_4B_4C_research.md", "residual_contribution": "hard_4c_recovery_band_filter", "reuse_reason": "none_new_symbol_or_new_trigger_family_for_c14_loop96", "row_type": "trigger", "same_entry_group_id": "C14_EV_DEMAND_SLOWDOWN_4B_4C|121600|Stage4C|2024-10-29", "score_return_alignment": "aligned_hard_4c", "selected_loop": 96, "selected_priority_bucket": "Priority 0", "selected_round": "R3", "shadow_profile_total_score_proxy": 65, "source_proxy_only": true, "stage2_evidence_fields": [], "stage3_evidence_fields": [], "stage4b_evidence_fields": ["macro_ev_slowdown_pressure", "price_only_local_peak_watch", "valuation_or_positioning_watch"], "stage4c_evidence_fields": ["utilization_or_margin_break_required", "demand_or_calloff_reset_required", "hard_thesis_break_only_after_non_price_confirmation"], "stock_web_manifest_max_date": "2026-02-20", "symbol": "121600", "trigger_date": "2024-10-29", "trigger_family": "late_2024_ev_material_margin_reset", "trigger_outcome_label": "cnt_battery_material_demand_reset_hard_4c_with_recovery_band_cap", "trigger_type": "Stage4C", "upstream_source": "FinanceData/marcap"}
{"MAE_180D_pct": -9.07, "MAE_30D_pct": -0.99, "MAE_90D_pct": -0.99, "MFE_180D_pct": 122.36, "MFE_30D_pct": 111.18, "MFE_90D_pct": 122.36, "aggregate_group_role": "representative", "below_entry_price_flag_180D": true, "below_entry_price_flag_30D": false, "below_entry_price_flag_90D": false, "calibration_block_reasons": [], "calibration_usable": true, "canonical_archetype_id": "C14_EV_DEMAND_SLOWDOWN_4B_4C", "case_id": "C14-R3L96-05", "case_role": "counterexample_false_hard_4c", "corporate_action_candidate_dates": ["2012-11-30", "2012-12-26", "2019-05-07", "2019-05-30"], "corporate_action_window_status": "not_contaminated", "current_profile_error": true, "current_profile_total_score_proxy": 82, "current_profile_verdict": "current_profile_false_positive_if_hard_4c_without_recovery_filter", "dedupe_for_aggregate": true, "deep_sub_archetype_id": "C14_DEEP_2024_EV_DEMAND_SLOWDOWN_HARD_4C_VS_CAPEX_EQUIPMENT_RECOVERY_MFE_EXCEPTION", "do_not_count_as_new_case": false, "drawdown_after_peak_min_date": "2024-12-30", "drawdown_after_peak_min_price": 36600, "drawdown_after_peak_pct": -59.11, "entry_date": "2024-04-30", "entry_price": 40250, "entry_price_basis": "close", "evidence_family": "battery_capex_equipment_order_visibility_exception", "evidence_url_pending": true, "fine_archetype_id": "C14_BATTERY_MATERIAL_EQUIPMENT_EV_DEMAND_RESET_RECOVERY_EXCEPTION_FILTER", "forward_window_trading_days": 180, "independent_evidence_weight": 1.0, "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "market": "KOSDAQ GLOBAL", "min_date_180D": "2024-12-30", "min_date_30D": "2024-05-02", "min_date_90D": "2024-05-02", "min_price_180D": 36600, "min_price_30D": 39850, "min_price_90D": 39850, "name": "피엔티", "peak_date": "2024-06-19", "peak_date_180D": "2024-06-19", "peak_date_30D": "2024-06-13", "peak_date_90D": "2024-06-19", "peak_price": 89500, "peak_price_180D": 89500, "peak_price_30D": 85000, "peak_price_90D": 89500, "price_adjustment_status": "raw_unadjusted_marcap", "price_basis": "tradable_raw", "price_data_source": "Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/137/137400/2024.csv; atlas/ohlcv_tradable_by_symbol_year/137/137400/2025.csv", "price_source": "Songdaiki/stock-web", "profile_path": "atlas/symbol_profiles/137/137400.json", "raw_component_score_breakdown": {"EPS/revision": 18, "bottleneck": 16, "capital": 8, "info_confidence": 22, "mispricing": 14, "valuation": 10, "visibility": 22}, "research_file": "e2r_stock_web_v12_residual_round_R3_loop_96_L3_BATTERY_EV_GREEN_MOBILITY_C14_EV_DEMAND_SLOWDOWN_4B_4C_research.md", "residual_contribution": "false_hard_4c_recovery_mfe_exception", "reuse_reason": "none_new_symbol_or_new_trigger_family_for_c14_loop96", "row_type": "trigger", "same_entry_group_id": "C14_EV_DEMAND_SLOWDOWN_4B_4C|137400|Stage4B|2024-04-30", "score_return_alignment": "hard_4c_would_be_false_positive_due_to_recovery_mfe", "selected_loop": 96, "selected_priority_bucket": "Priority 0", "selected_round": "R3", "shadow_profile_total_score_proxy": 73, "source_proxy_only": true, "stage2_evidence_fields": [], "stage3_evidence_fields": [], "stage4b_evidence_fields": ["macro_ev_slowdown_pressure", "price_only_local_peak_watch", "recovery_mfe_exception_filter"], "stage4c_evidence_fields": ["utilization_or_margin_break_required", "demand_or_calloff_reset_required", "hard_thesis_break_only_after_non_price_confirmation"], "stock_web_manifest_max_date": "2026-02-20", "symbol": "137400", "trigger_date": "2024-04-30", "trigger_family": "spring_2024_equipment_recovery_exception", "trigger_outcome_label": "battery_equipment_recovery_mfe_exception_after_demand_fear", "trigger_type": "Stage4B", "upstream_source": "FinanceData/marcap"}
{"MAE_180D_pct": -18.21, "MAE_30D_pct": -8.24, "MAE_90D_pct": -8.24, "MFE_180D_pct": 81.16, "MFE_30D_pct": 81.07, "MFE_90D_pct": 81.16, "aggregate_group_role": "representative", "below_entry_price_flag_180D": true, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "calibration_block_reasons": [], "calibration_usable": true, "canonical_archetype_id": "C14_EV_DEMAND_SLOWDOWN_4B_4C", "case_id": "C14-R3L96-06", "case_role": "counterexample_false_hard_4c", "corporate_action_candidate_dates": ["1998-01-03", "2001-12-21"], "corporate_action_window_status": "not_contaminated", "current_profile_error": true, "current_profile_total_score_proxy": 82, "current_profile_verdict": "current_profile_false_positive_if_hard_4c_without_recovery_filter", "dedupe_for_aggregate": true, "deep_sub_archetype_id": "C14_DEEP_2024_EV_DEMAND_SLOWDOWN_HARD_4C_VS_CAPEX_EQUIPMENT_RECOVERY_MFE_EXCEPTION", "do_not_count_as_new_case": false, "drawdown_after_peak_min_date": "2024-12-09", "drawdown_after_peak_min_price": 90300, "drawdown_after_peak_pct": -54.85, "entry_date": "2024-04-30", "entry_price": 110400, "entry_price_basis": "close", "evidence_family": "copper_foil_parent_mix_exception", "evidence_url_pending": true, "fine_archetype_id": "C14_BATTERY_MATERIAL_EQUIPMENT_EV_DEMAND_RESET_RECOVERY_EXCEPTION_FILTER", "forward_window_trading_days": 180, "independent_evidence_weight": 1.0, "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "market": "KOSPI", "min_date_180D": "2024-12-09", "min_date_30D": "2024-05-17", "min_date_90D": "2024-05-17", "min_price_180D": 90300, "min_price_30D": 101300, "min_price_90D": 101300, "name": "SKC", "peak_date": "2024-06-18", "peak_date_180D": "2024-06-18", "peak_date_30D": "2024-06-14", "peak_date_90D": "2024-06-18", "peak_price": 200000, "peak_price_180D": 200000, "peak_price_30D": 199900, "peak_price_90D": 200000, "price_adjustment_status": "raw_unadjusted_marcap", "price_basis": "tradable_raw", "price_data_source": "Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/011/011790/2024.csv; atlas/ohlcv_tradable_by_symbol_year/011/011790/2025.csv", "price_source": "Songdaiki/stock-web", "profile_path": "atlas/symbol_profiles/011/011790.json", "raw_component_score_breakdown": {"EPS/revision": 18, "bottleneck": 16, "capital": 8, "info_confidence": 22, "mispricing": 14, "valuation": 10, "visibility": 22}, "research_file": "e2r_stock_web_v12_residual_round_R3_loop_96_L3_BATTERY_EV_GREEN_MOBILITY_C14_EV_DEMAND_SLOWDOWN_4B_4C_research.md", "residual_contribution": "false_hard_4c_recovery_mfe_exception", "reuse_reason": "none_new_symbol_or_new_trigger_family_for_c14_loop96", "row_type": "trigger", "same_entry_group_id": "C14_EV_DEMAND_SLOWDOWN_4B_4C|011790|Stage4B|2024-04-30", "score_return_alignment": "hard_4c_would_be_false_positive_due_to_recovery_mfe", "selected_loop": 96, "selected_priority_bucket": "Priority 0", "selected_round": "R3", "shadow_profile_total_score_proxy": 73, "source_proxy_only": true, "stage2_evidence_fields": [], "stage3_evidence_fields": [], "stage4b_evidence_fields": ["macro_ev_slowdown_pressure", "price_only_local_peak_watch", "recovery_mfe_exception_filter"], "stage4c_evidence_fields": ["utilization_or_margin_break_required", "demand_or_calloff_reset_required", "hard_thesis_break_only_after_non_price_confirmation"], "stock_web_manifest_max_date": "2026-02-20", "symbol": "011790", "trigger_date": "2024-04-30", "trigger_family": "spring_2024_equipment_recovery_exception", "trigger_outcome_label": "copper_foil_platform_recovery_mfe_exception_before_later_fade", "trigger_type": "Stage4B", "upstream_source": "FinanceData/marcap"}
{"MAE_180D_pct": -18.75, "MAE_30D_pct": -2.5, "MAE_90D_pct": -11.88, "MFE_180D_pct": 52.88, "MFE_30D_pct": 52.88, "MFE_90D_pct": 52.88, "aggregate_group_role": "representative", "below_entry_price_flag_180D": true, "below_entry_price_flag_30D": false, "below_entry_price_flag_90D": true, "calibration_block_reasons": [], "calibration_usable": true, "canonical_archetype_id": "C14_EV_DEMAND_SLOWDOWN_4B_4C", "case_id": "C14-R3L96-07", "case_role": "counterexample_false_hard_4c", "corporate_action_candidate_dates": ["2017-01-20"], "corporate_action_window_status": "not_contaminated", "current_profile_error": true, "current_profile_total_score_proxy": 82, "current_profile_verdict": "current_profile_false_positive_if_hard_4c_on_macro_price_shock", "dedupe_for_aggregate": true, "deep_sub_archetype_id": "C14_DEEP_2024_EV_DEMAND_SLOWDOWN_HARD_4C_VS_CAPEX_EQUIPMENT_RECOVERY_MFE_EXCEPTION", "do_not_count_as_new_case": false, "drawdown_after_peak_min_date": "2025-04-09", "drawdown_after_peak_min_price": 6500, "drawdown_after_peak_pct": -46.85, "entry_date": "2024-08-05", "entry_price": 8000, "entry_price_basis": "close", "evidence_family": "battery_equipment_local_order_optionality_exception", "evidence_url_pending": true, "fine_archetype_id": "C14_BATTERY_MATERIAL_EQUIPMENT_EV_DEMAND_RESET_RECOVERY_EXCEPTION_FILTER", "forward_window_trading_days": 180, "independent_evidence_weight": 1.0, "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "market": "KOSDAQ GLOBAL", "min_date_180D": "2025-04-09", "min_date_30D": "2024-08-05", "min_date_90D": "2024-12-09", "min_price_180D": 6500, "min_price_30D": 7800, "min_price_90D": 7050, "name": "씨아이에스", "peak_date": "2024-08-20", "peak_date_180D": "2024-08-20", "peak_date_30D": "2024-08-20", "peak_date_90D": "2024-08-20", "peak_price": 12230, "peak_price_180D": 12230, "peak_price_30D": 12230, "peak_price_90D": 12230, "price_adjustment_status": "raw_unadjusted_marcap", "price_basis": "tradable_raw", "price_data_source": "Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/222/222080/2024.csv; atlas/ohlcv_tradable_by_symbol_year/222/222080/2025.csv", "price_source": "Songdaiki/stock-web", "profile_path": "atlas/symbol_profiles/222/222080.json", "raw_component_score_breakdown": {"EPS/revision": 18, "bottleneck": 16, "capital": 8, "info_confidence": 22, "mispricing": 14, "valuation": 10, "visibility": 22}, "research_file": "e2r_stock_web_v12_residual_round_R3_loop_96_L3_BATTERY_EV_GREEN_MOBILITY_C14_EV_DEMAND_SLOWDOWN_4B_4C_research.md", "residual_contribution": "false_hard_4c_recovery_mfe_exception", "reuse_reason": "none_new_symbol_or_new_trigger_family_for_c14_loop96", "row_type": "trigger", "same_entry_group_id": "C14_EV_DEMAND_SLOWDOWN_4B_4C|222080|Stage4B|2024-08-05", "score_return_alignment": "hard_4c_would_be_false_positive_due_to_recovery_mfe", "selected_loop": 96, "selected_priority_bucket": "Priority 0", "selected_round": "R3", "shadow_profile_total_score_proxy": 73, "source_proxy_only": true, "stage2_evidence_fields": [], "stage3_evidence_fields": [], "stage4b_evidence_fields": ["macro_ev_slowdown_pressure", "price_only_local_peak_watch", "recovery_mfe_exception_filter"], "stage4c_evidence_fields": ["utilization_or_margin_break_required", "demand_or_calloff_reset_required", "hard_thesis_break_only_after_non_price_confirmation"], "stock_web_manifest_max_date": "2026-02-20", "symbol": "222080", "trigger_date": "2024-08-05", "trigger_family": "august_2024_macro_shock_recovery_exception", "trigger_outcome_label": "battery_equipment_local_recovery_after_macro_slowdown_shock", "trigger_type": "Stage4B", "upstream_source": "FinanceData/marcap"}
```

## 12. Machine-readable rows — score simulation JSONL

```jsonl
{"MAE_90D_pct": -34.69, "MFE_90D_pct": 4.4, "after_profile_id": "proposed_C14_recovery_band_shadow_profile", "before_profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "C14-R3L96-01", "current_profile_total_score_proxy": 74, "current_profile_verdict": "current_profile_correct", "raw_component_score_breakdown": {"EPS/revision": 18, "bottleneck": 10, "capital": 6, "info_confidence": 35, "mispricing": 8, "valuation": 5, "visibility": 18}, "research_file": "e2r_stock_web_v12_residual_round_R3_loop_96_L3_BATTERY_EV_GREEN_MOBILITY_C14_EV_DEMAND_SLOWDOWN_4B_4C_research.md", "rollback_reference_profile_id": "e2r_2_0_baseline_reference", "row_type": "score_simulation", "score_return_alignment": "aligned_hard_4c", "shadow_profile_total_score_proxy": 68, "symbol": "051910"}
{"MAE_90D_pct": -46.92, "MFE_90D_pct": 2.49, "after_profile_id": "proposed_C14_recovery_band_shadow_profile", "before_profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "C14-R3L96-02", "current_profile_total_score_proxy": 74, "current_profile_verdict": "current_profile_correct", "raw_component_score_breakdown": {"EPS/revision": 18, "bottleneck": 10, "capital": 6, "info_confidence": 35, "mispricing": 8, "valuation": 5, "visibility": 18}, "research_file": "e2r_stock_web_v12_residual_round_R3_loop_96_L3_BATTERY_EV_GREEN_MOBILITY_C14_EV_DEMAND_SLOWDOWN_4B_4C_research.md", "rollback_reference_profile_id": "e2r_2_0_baseline_reference", "row_type": "score_simulation", "score_return_alignment": "aligned_hard_4c", "shadow_profile_total_score_proxy": 68, "symbol": "020150"}
{"MAE_90D_pct": -29.04, "MFE_90D_pct": 2.77, "after_profile_id": "proposed_C14_recovery_band_shadow_profile", "before_profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "C14-R3L96-03", "current_profile_total_score_proxy": 74, "current_profile_verdict": "current_profile_correct", "raw_component_score_breakdown": {"EPS/revision": 18, "bottleneck": 10, "capital": 6, "info_confidence": 35, "mispricing": 8, "valuation": 5, "visibility": 18}, "research_file": "e2r_stock_web_v12_residual_round_R3_loop_96_L3_BATTERY_EV_GREEN_MOBILITY_C14_EV_DEMAND_SLOWDOWN_4B_4C_research.md", "rollback_reference_profile_id": "e2r_2_0_baseline_reference", "row_type": "score_simulation", "score_return_alignment": "aligned_hard_4c", "shadow_profile_total_score_proxy": 68, "symbol": "093370"}
{"MAE_90D_pct": -33.06, "MFE_90D_pct": 8.79, "after_profile_id": "proposed_C14_recovery_band_shadow_profile", "before_profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "C14-R3L96-04", "current_profile_total_score_proxy": 72, "current_profile_verdict": "current_profile_correct_but_requires_recovery_band_cap", "raw_component_score_breakdown": {"EPS/revision": 16, "bottleneck": 10, "capital": 6, "info_confidence": 28, "mispricing": 8, "valuation": 6, "visibility": 15}, "research_file": "e2r_stock_web_v12_residual_round_R3_loop_96_L3_BATTERY_EV_GREEN_MOBILITY_C14_EV_DEMAND_SLOWDOWN_4B_4C_research.md", "rollback_reference_profile_id": "e2r_2_0_baseline_reference", "row_type": "score_simulation", "score_return_alignment": "aligned_hard_4c", "shadow_profile_total_score_proxy": 65, "symbol": "121600"}
{"MAE_90D_pct": -0.99, "MFE_90D_pct": 122.36, "after_profile_id": "proposed_C14_recovery_band_shadow_profile", "before_profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "C14-R3L96-05", "current_profile_total_score_proxy": 82, "current_profile_verdict": "current_profile_false_positive_if_hard_4c_without_recovery_filter", "raw_component_score_breakdown": {"EPS/revision": 18, "bottleneck": 16, "capital": 8, "info_confidence": 22, "mispricing": 14, "valuation": 10, "visibility": 22}, "research_file": "e2r_stock_web_v12_residual_round_R3_loop_96_L3_BATTERY_EV_GREEN_MOBILITY_C14_EV_DEMAND_SLOWDOWN_4B_4C_research.md", "rollback_reference_profile_id": "e2r_2_0_baseline_reference", "row_type": "score_simulation", "score_return_alignment": "hard_4c_would_be_false_positive_due_to_recovery_mfe", "shadow_profile_total_score_proxy": 73, "symbol": "137400"}
{"MAE_90D_pct": -8.24, "MFE_90D_pct": 81.16, "after_profile_id": "proposed_C14_recovery_band_shadow_profile", "before_profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "C14-R3L96-06", "current_profile_total_score_proxy": 82, "current_profile_verdict": "current_profile_false_positive_if_hard_4c_without_recovery_filter", "raw_component_score_breakdown": {"EPS/revision": 18, "bottleneck": 16, "capital": 8, "info_confidence": 22, "mispricing": 14, "valuation": 10, "visibility": 22}, "research_file": "e2r_stock_web_v12_residual_round_R3_loop_96_L3_BATTERY_EV_GREEN_MOBILITY_C14_EV_DEMAND_SLOWDOWN_4B_4C_research.md", "rollback_reference_profile_id": "e2r_2_0_baseline_reference", "row_type": "score_simulation", "score_return_alignment": "hard_4c_would_be_false_positive_due_to_recovery_mfe", "shadow_profile_total_score_proxy": 73, "symbol": "011790"}
{"MAE_90D_pct": -11.88, "MFE_90D_pct": 52.88, "after_profile_id": "proposed_C14_recovery_band_shadow_profile", "before_profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "C14-R3L96-07", "current_profile_total_score_proxy": 82, "current_profile_verdict": "current_profile_false_positive_if_hard_4c_on_macro_price_shock", "raw_component_score_breakdown": {"EPS/revision": 18, "bottleneck": 16, "capital": 8, "info_confidence": 22, "mispricing": 14, "valuation": 10, "visibility": 22}, "research_file": "e2r_stock_web_v12_residual_round_R3_loop_96_L3_BATTERY_EV_GREEN_MOBILITY_C14_EV_DEMAND_SLOWDOWN_4B_4C_research.md", "rollback_reference_profile_id": "e2r_2_0_baseline_reference", "row_type": "score_simulation", "score_return_alignment": "hard_4c_would_be_false_positive_due_to_recovery_mfe", "shadow_profile_total_score_proxy": 73, "symbol": "222080"}
```

## 13. Machine-readable rows — aggregate / shadow / residual JSONL

```jsonl
{"calibration_usable_case_count": 7, "calibration_usable_trigger_count": 7, "canonical_archetype_id": "C14_EV_DEMAND_SLOWDOWN_4B_4C", "counterexample_count": 3, "current_profile_error_count": 3, "do_not_propose_new_weight_delta": false, "evidence_url_pending_count": 7, "existing_axis_strengthened": ["hard_4c_confirmation", "local_4b_watch_guard", "full_4b_requires_non_price_evidence"], "existing_axis_weakened": null, "fine_archetype_id": "C14_BATTERY_MATERIAL_EQUIPMENT_EV_DEMAND_RESET_RECOVERY_EXCEPTION_FILTER", "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "loop_contribution_label": "canonical_archetype_rule_candidate", "new_axis_proposed": "C14_hard_4c_requires_confirmed_utilization_calloff_margin_break_plus_no_recovery_mfe_band_before_routing_to_Stage4C", "new_independent_case_count": 7, "new_trigger_family_count": 3, "positive_case_count": 4, "promotion_blocked_until_url_repair": true, "representative_trigger_count": 7, "research_file": "e2r_stock_web_v12_residual_round_R3_loop_96_L3_BATTERY_EV_GREEN_MOBILITY_C14_EV_DEMAND_SLOWDOWN_4B_4C_research.md", "reused_case_count": 0, "row_type": "aggregate", "same_archetype_new_symbol_count": 7, "same_archetype_new_trigger_family_count": 3, "selected_loop": 96, "selected_round": "R3", "source_proxy_only_count": 7, "stage4b_case_count": 3, "stage4c_case_count": 4}
{"canonical_archetype_id": "C14_EV_DEMAND_SLOWDOWN_4B_4C", "counterexample_cases": ["C14-R3L96-05", "C14-R3L96-06", "C14-R3L96-07"], "do_not_propose_global_delta": true, "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "max_shadow_delta": 1, "positive_support_cases": ["C14-R3L96-01", "C14-R3L96-02", "C14-R3L96-03", "C14-R3L96-04"], "production_scoring_changed": false, "requires_url_repair_before_apply": true, "research_file": "e2r_stock_web_v12_residual_round_R3_loop_96_L3_BATTERY_EV_GREEN_MOBILITY_C14_EV_DEMAND_SLOWDOWN_4B_4C_research.md", "row_type": "shadow_weight_candidate", "rule_candidate": "If broad EV demand slowdown is present but 30D/90D MFE recovery band exceeds +20% without confirmed utilization/call-off/margin break, route to Stage4B watch instead of hard Stage4C.", "scope": "canonical_archetype", "shadow_rule_id": "C14_RECOVERY_MFE_EXCEPTION_FILTER_FOR_HARD_4C"}
{"This loop adds": "7 new independent cases, 3 counterexamples, and 3 residual errors for R3/C14.", "canonical_archetype_id": "C14_EV_DEMAND_SLOWDOWN_4B_4C", "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "main_residual": "Broad EV slowdown mapped directly to hard 4C is too blunt for capex/equipment recovery paths.", "new_axis_proposed": "C14_hard_4c_requires_confirmed_utilization_calloff_margin_break_plus_no_recovery_mfe_band_before_routing_to_Stage4C", "next_recommended_archetypes": ["C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE", "C02_POWER_GRID_DATACENTER_CAPEX", "C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF", "C14_EV_DEMAND_SLOWDOWN_4B_4C", "C06_HBM_MEMORY_CUSTOMER_CAPACITY"], "research_file": "e2r_stock_web_v12_residual_round_R3_loop_96_L3_BATTERY_EV_GREEN_MOBILITY_C14_EV_DEMAND_SLOWDOWN_4B_4C_research.md", "row_type": "residual_contribution_summary"}
```

## 14. Residual contribution summary

```text
This loop adds 7 new independent cases, 3 counterexamples, and 3 residual errors for R3/C14.
```

Residual contribution:

```text
loop_contribution_label = canonical_archetype_rule_candidate
sector_specific_rule_candidate = true
canonical_archetype_rule_candidate = true
do_not_propose_new_weight_delta = false
promotion_blocked_until_url_repair = true
new_axis_proposed = C14_hard_4c_requires_confirmed_utilization_calloff_margin_break_plus_no_recovery_mfe_band_before_routing_to_Stage4C
existing_axis_strengthened = hard_4c_confirmation, local_4b_watch_guard, full_4b_requires_non_price_evidence
existing_axis_weakened = null
```

Practical rule candidate:

```text
For C14, hard Stage4C should require both:
1. non-price thesis break evidence: utilization/call-off/order cut/margin reset; and
2. no recovery-MFE exception: 30D/90D recovery band does not exceed the exception threshold.

If broad EV demand slowdown exists but recovery MFE exceeds the exception band before non-price confirmation, route to Stage4B watch, not hard 4C.
```

## 15. Batch Ingest Self-Audit

```text
expected_v12_result_file: true
filename_pattern_pass: true
metadata_filename_consistency: pass
jsonl_trigger_row_count: 7
calibration_usable_trigger_count: 7
representative_trigger_count: 7
new_weight_evidence_candidate_count: 7
guardrail_candidate_count: 7
narrative_only_or_rejected_count: 0
rows_missing_required_mfe_mae: 0
rows_missing_entry_price_or_date: 0
rows_with_noncanonical_trigger_type: 0
rows_with_compact_mfe_mae_alias_only: 0
ready_for_batch_ingest: true
```

Filename check:

```text
expected_filename = e2r_stock_web_v12_residual_round_R3_loop_96_L3_BATTERY_EV_GREEN_MOBILITY_C14_EV_DEMAND_SLOWDOWN_4B_4C_research.md
actual_filename = e2r_stock_web_v12_residual_round_R3_loop_96_L3_BATTERY_EV_GREEN_MOBILITY_C14_EV_DEMAND_SLOWDOWN_4B_4C_research.md
required_filename_regex = ^e2r_stock_web_v12_residual_round_R[0-9]+_loop_[0-9]+_[A-Z0-9_]+_[A-Z0-9_]+_research\.md$
filename_matches_standard_v12_pattern = true
metadata_round_loop_matches_filename = true
round_sector_consistency = pass
```

## 16. Deferred Coding Agent Handoff Prompt

```text
Do not execute this handoff in the research session.

Later batch implementation task:
1. Ingest this Markdown file together with other V12 research files.
2. Parse row_type="trigger" JSONL rows only if all required 30D/90D/180D MFE/MAE fields are present.
3. Validate Songdaiki/stock-web tradable_raw entry rows and corporate-action windows.
4. Treat this file as a C14 canonical-archetype-specific shadow rule candidate, not a global profile patch.
5. Candidate rule id: C14_RECOVERY_MFE_EXCEPTION_FILTER_FOR_HARD_4C.
6. Apply only if URL repair confirms the proxy evidence families: utilization/call-off/order cut/margin reset for hard 4C, and recovery-MFE exception for Stage4B watch.
7. Do not loosen Stage3-Green. Do not lower global Yellow. Do not use price-only evidence as positive Stage2/3 support.
```

## 17. Next research state

```text
completed_round = R3
completed_loop = 96
selection_basis = docs/core/V12_Research_No_Repeat_Index.md
selected_priority_bucket = Priority 0
next_recommended_archetypes = C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE, C02_POWER_GRID_DATACENTER_CAPEX, C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF, C14_EV_DEMAND_SLOWDOWN_4B_4C, C06_HBM_MEMORY_CUSTOMER_CAPACITY
round_schedule_status = coverage_index_selected
round_sector_consistency = pass
```
