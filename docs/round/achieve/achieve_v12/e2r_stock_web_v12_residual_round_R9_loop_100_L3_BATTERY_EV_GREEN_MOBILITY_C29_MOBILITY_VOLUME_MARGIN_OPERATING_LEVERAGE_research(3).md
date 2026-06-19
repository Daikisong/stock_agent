# E2R Stock-Web V12 Residual Research — R9 / C29 Mobility Volume-Margin Operating Leverage

## 0. Execution Metadata

```yaml
research_session: post_calibrated_sector_archetype_residual_research
mode: historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12
selected_round: R9
selected_loop: 100
selection_basis: docs/core/V12_Research_No_Repeat_Index.md + local generated loop memory
selected_priority_bucket: Priority 2 quality_repair_after_local_priority0_priority1_fill
round_schedule_status: coverage_index_selected
round_sector_consistency: pass
large_sector_id: L3_BATTERY_EV_GREEN_MOBILITY
canonical_archetype_id: C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE
fine_archetype_id: C29_AUTOMOTIVE_VOLUME_MIX_MARGIN_OPERATING_LEVERAGE_BRIDGE_V1
deep_sub_archetype_id: C29_DEEP_AUTO_OEM_PARTS_TIRE_THERMAL_EXPORT_VOLUME_MIX_MARGIN_VS_LABEL_SPIKE
output_file: e2r_stock_web_v12_residual_round_R9_loop_100_L3_BATTERY_EV_GREEN_MOBILITY_C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE_research.md
production_scoring_changed: false
shadow_weight_only: true
handoff_prompt_embedded: true
handoff_prompt_executed_now: false
```

## 1. Selection Rationale

The scheduler is coverage-index-first rather than sequential R1→R13. Published No-Repeat Index coverage already places C29 at 90 representative rows, so this is not minimum coverage fill. The local session has already pushed multiple under-30 and under-50 canonicals into the 50-row practical band; therefore C29 is selected as Priority 2 quality repair: separate real automotive volume/mix/margin operating leverage from generic mobility or auto label spikes.

C29 maps to `R9 / L3_BATTERY_EV_GREEN_MOBILITY` under the representative mapping. R13 is not used because this is still a sector-specific mobility archetype, not a cross-archetype red-team checkpoint.

## 2. Stock-Web Price Atlas Validation

```yaml
price_data_source: Songdaiki/stock-web
source_name: FinanceData/marcap
price_basis: tradable_raw
price_adjustment_status: raw_unadjusted_marcap
manifest_max_date: 2026-02-20
calibration_shard_root: atlas/ohlcv_tradable_by_symbol_year
required_price_fields: [MFE_30D_pct, MFE_90D_pct, MFE_180D_pct, MAE_30D_pct, MAE_90D_pct, MAE_180D_pct]
forward_window_policy: 180 trading-day window must be inside manifest max_date
raw_shard_used_for_weight_calibration: false
```

Price windows were computed locally from downloaded Stock-Web 2024–2025 tradable shards. Entry uses close on the first eligible tradable date after the evidence timing rule. MFE uses forward-window high; MAE uses forward-window low; both are measured from entry close.

## 3. Case Matrix

| # | Symbol | Company | Trigger | Entry | Type | Outcome | MFE180 | MAE180 | Note |
|---:|---|---|---|---|---|---|---:|---:|---|
| 1 | `005380` | Hyundai Motor / 현대차 | 2024-04-25 | 2024-04-26 @ 249500 | `Stage3-Yellow` | good_yellow_not_green_due_drawdown | 20.04% | -20.92% | positive_with_high_MAE_local_4B_watch |
| 2 | `000270` | Kia / 기아 | 2025-01-24 | 2025-01-31 @ 102000 | `Stage2-Actionable` | record_profit_label_not_enough | 17.45% | -20.29% | counterexample_high_MAE_after_record_profit_label |
| 3 | `012330` | Hyundai Mobis / 현대모비스 | 2025-01-24 | 2025-01-31 @ 263500 | `Stage3-Yellow` | delayed_but_clean_positive | 24.10% | -11.95% | positive_bridge |
| 4 | `204320` | HL Mando / HL만도 | 2024-07-26 | 2024-07-29 @ 39850 | `Stage2-Actionable` | early_stage2_false_positive | 17.94% | -22.58% | counterexample_high_MAE_before_any_order_margin_confirmation |
| 5 | `161390` | Hankook Tire & Technology / 한국타이어앤테크놀로지 | 2025-02-04 | 2025-02-05 @ 37750 | `Stage3-Yellow` | clean_positive_low_MAE | 28.48% | -4.77% | positive_clean_bridge |
| 6 | `011210` | Hyundai Wia / 현대위아 | 2025-01-24 | 2025-01-31 @ 38950 | `Stage3-Yellow` | missed_structural_positive | 48.91% | -5.26% | positive_missed_structural |
| 7 | `018880` | Hanon Systems / 한온시스템 | 2025-02-13 | 2025-02-14 @ 4360 | `Stage4B` | confirmed_margin_break_counterexample | 13.65% | -32.57% | counterexample_hard_4B_to_4C_watch |
| 8 | `003620` | KG Mobility / KG모빌리티 | 2025-01-03 | 2025-01-06 @ 3905 | `Stage2-Actionable` | MFE_spike_but_not_sustained | 25.10% | -19.08% | counterexample_recovery_spike_without_sustained_bridge |

## 4. Residual Findings

1. **Direct OEM record-profit labels are not sufficient.** Hyundai and Kia both had strong profit/margin headlines, but only Hyundai delivered a 20% peak before the path broke into a -20% 180D drawdown. Kia did not clear 20% MFE within 180D and hit a -20% MAE. C29 needs an explicit tariff/FX/demand-risk filter before Green.
2. **Supplier mix matters.** Hyundai Mobis, Hankook Tire, and Hyundai Wia had cleaner volume/margin or mix bridges and produced better MFE/MAE alignment. These should be allowed Stage3-Yellow or Green-watch only when the bridge is tied to profit mix, not to mobility label alone.
3. **Parts names with weak margin bridge should remain Stage2 or local 4B.** HL Mando, Hanon Systems, and KG Mobility show why an auto-parts or export-volume label can create MFE spikes but still fail as a durable C29 rerating without margin or cash conversion.
4. **4C should require issuer-level margin or demand break.** Hanon is the cleanest 4B→4C candidate because the non-price evidence included restructuring/loss and EV thermal demand weakness. Generic auto demand weakness alone should first route to local 4B watch, not hard 4C.

## 5. Proposed Shadow Rule Candidate

```yaml
selected_round: R9
selected_loop: 100
large_sector_id: L3_BATTERY_EV_GREEN_MOBILITY
canonical_archetype_id: C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE
fine_archetype_id: C29_AUTOMOTIVE_VOLUME_MIX_MARGIN_OPERATING_LEVERAGE_BRIDGE_V1
deep_sub_archetype_id: C29_DEEP_AUTO_OEM_PARTS_TIRE_THERMAL_EXPORT_VOLUME_MIX_MARGIN_VS_LABEL_SPIKE
trigger_row_count: 8
calibration_usable_trigger_count: 8
representative_trigger_count: 8
new_independent_case_count: 8
reused_case_count: 0
same_archetype_new_symbol_count: 8
positive_case_count: 4
counterexample_count: 4
stage4b_case_count: 5
stage4c_case_count: 1
current_profile_error_count: 6
source_proxy_only_count: 4
evidence_url_pending_count: 0
promotion_blocked_until_url_repair: true_for_source_proxy_rows_only
new_axis_proposed: C29_verified_volume_mix_margin_operating_leverage_bridge_required_before_Yellow_or_Green_plus_mobility_label_spike_to_local_4B_or_4C_watch
existing_axis_strengthened: ["stage2_required_bridge", "local_4b_watch_guard", "price_only_blowoff_blocks_positive_stage", "full_4b_requires_non_price_evidence"]
existing_axis_weakened: ["hard_4c_thesis_break_routes_to_4c_when_only_generic_auto_volume_or_mobility_label_is_present"]
do_not_propose_new_weight_delta: false
loop_contribution_label: canonical_archetype_rule_candidate
```

### Rule sketch

```text
IF canonical_archetype_id == C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE:
  require at least one verified issuer-level bridge before Stage3-Yellow:
    - unit volume growth with region/channel quality
    - product/mix improvement (hybrid, premium tire, AS/core parts, high-margin export mix)
    - operating margin or FCF conversion improvement
    - credible guidance/revision confirmation after tariff/FX/demand sensitivity
  block Stage3-Green if:
    - evidence is only auto/mobility label or record-profit headline
    - 90D MAE <= -20% before verified margin bridge
    - event is supplier proxy without direct order/revenue/margin confirmation
  route to local 4B watch when:
    - MFE spike appears but final 180D path fades
    - tariff, EV slowdown, restructuring, or domestic-demand gap is visible
  route to hard 4C only when:
    - issuer-level margin/loss/restructuring/customer-pull break is verified
```

## 6. Trigger Rows JSONL

```jsonl
{"MAE_180D_pct": -20.92, "MAE_30D_pct": -5.81, "MAE_90D_pct": -13.23, "MFE_180D_pct": 20.04, "MFE_30D_pct": 11.22, "MFE_90D_pct": 20.04, "balance_sheet_risk": 58, "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "calibration_usable": true, "canonical_archetype_id": "C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE", "capital_return": 63, "case_id": "C29_R9_L100_005380_20240426_STAGE3Y", "classification": "positive_with_high_MAE_local_4B_watch", "company": "Hyundai Motor / 현대차", "corporate_action_window_check": "no 2024-2025 profile candidate overlap flagged in selected 180D window; raw/unadjusted caveat retained", "current_profile_error": "green_if_unchecked; yellow acceptable only with MAE guard", "demand_volume": 72, "entry_date": "2024-04-26", "entry_price": 249500.0, "evidence_summary": "Q1 2024 revenue reached a record first-quarter level, operating margin stayed high at 8.7%, and North America/India plus SUV/hybrid mix supported the volume-margin bridge.", "evidence_url": "https://www.hyundai.com/worldwide/en/newsroom/detail/hyundai-motor-announces-2024-q1-business-results-0000000755", "fine_archetype_id": "C29_AUTOMOTIVE_VOLUME_MIX_MARGIN_OPERATING_LEVERAGE_BRIDGE_V1", "forward_window_trading_days": 180, "hard_duplicate_check": "new C29 symbol/trigger_date/entry_date family for this local session", "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "mix_margin": 74, "outcome_tag": "good_yellow_not_green_due_drawdown", "peak_180D_date": "2024-06-28", "price_adjustment_status": "raw_unadjusted_marcap", "price_basis": "tradable_raw", "price_data_source": "Songdaiki/stock-web", "price_path_alignment": 59, "raw_total": 73.4, "representative_for_aggregate": true, "revision_visibility": 66, "simulated_stage": "Stage3-Yellow_not_Green", "source_proxy_only": false, "stage4b_local": true, "stage4c": false, "symbol": "005380", "trigger_date": "2024-04-25", "trigger_family": "Q1_2024_revenue_mix_margin_guidance_bridge", "trigger_type": "Stage3-Yellow", "trough_180D_date": "2024-11-14", "upstream_source": "FinanceData/marcap"}
{"MAE_180D_pct": -20.29, "MAE_30D_pct": -10.39, "MAE_90D_pct": -20.29, "MFE_180D_pct": 17.45, "MFE_30D_pct": 0.78, "MFE_90D_pct": 0.98, "balance_sheet_risk": 46, "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "calibration_usable": true, "canonical_archetype_id": "C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE", "capital_return": 64, "case_id": "C29_R9_L100_000270_20250131_STAGE2A", "classification": "counterexample_high_MAE_after_record_profit_label", "company": "Kia / 기아", "corporate_action_window_check": "no 2024-2025 profile candidate overlap flagged in selected 180D window; raw/unadjusted caveat retained", "current_profile_error": "stage2_too_easy_if_record_profit_label_without_tariff_sensitivity_filter", "demand_volume": 68, "entry_date": "2025-01-31", "entry_price": 102000.0, "evidence_summary": "FY2024 operating profit reached KRW 12.67tn and management supplied 2025 revenue/OP targets, but the price path carried tariff/demand drawdown before any durable volume-margin rerating.", "evidence_url": "https://www.reuters.com/business/autos-transportation/kia-posts-operating-profit-127-trln-won-2024-2025-01-24/", "fine_archetype_id": "C29_AUTOMOTIVE_VOLUME_MIX_MARGIN_OPERATING_LEVERAGE_BRIDGE_V1", "forward_window_trading_days": 180, "hard_duplicate_check": "new C29 symbol/trigger_date/entry_date family for this local session", "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "mix_margin": 70, "outcome_tag": "record_profit_label_not_enough", "peak_180D_date": "2025-10-21", "price_adjustment_status": "raw_unadjusted_marcap", "price_basis": "tradable_raw", "price_data_source": "Songdaiki/stock-web", "price_path_alignment": 40, "raw_total": 66.8, "representative_for_aggregate": true, "revision_visibility": 57, "simulated_stage": "Stage2-Actionable_with_4B_watch", "source_proxy_only": true, "stage4b_local": true, "stage4c": false, "symbol": "000270", "trigger_date": "2025-01-24", "trigger_family": "FY2024_record_profit_2025_guidance_but_tariff_cycle_risk", "trigger_type": "Stage2-Actionable", "trough_180D_date": "2025-04-11", "upstream_source": "FinanceData/marcap"}
{"MAE_180D_pct": -11.95, "MAE_30D_pct": -8.73, "MAE_90D_pct": -11.95, "MFE_180D_pct": 24.1, "MFE_30D_pct": 2.09, "MFE_90D_pct": 10.25, "balance_sheet_risk": 62, "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "calibration_usable": true, "canonical_archetype_id": "C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE", "capital_return": 54, "case_id": "C29_R9_L100_012330_20250131_STAGE3Y", "classification": "positive_bridge", "company": "Hyundai Mobis / 현대모비스", "corporate_action_window_check": "no 2024-2025 profile candidate overlap flagged in selected 180D window; raw/unadjusted caveat retained", "current_profile_error": "yellow_timing_ok_but_green_should_wait_for_sustained_revision", "demand_volume": 65, "entry_date": "2025-01-31", "entry_price": 263500.0, "evidence_summary": "2024 operating profit rose materially with high-value parts/A-S contribution; the price path had controlled MAE and a later 180D MFE above 20%.", "evidence_url": "https://pulse.mk.co.kr/news/english/11226327", "fine_archetype_id": "C29_AUTOMOTIVE_VOLUME_MIX_MARGIN_OPERATING_LEVERAGE_BRIDGE_V1", "forward_window_trading_days": 180, "hard_duplicate_check": "new C29 symbol/trigger_date/entry_date family for this local session", "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "mix_margin": 78, "outcome_tag": "delayed_but_clean_positive", "peak_180D_date": "2025-09-09", "price_adjustment_status": "raw_unadjusted_marcap", "price_basis": "tradable_raw", "price_data_source": "Songdaiki/stock-web", "price_path_alignment": 71, "raw_total": 76.1, "representative_for_aggregate": true, "revision_visibility": 69, "simulated_stage": "Stage3-Yellow", "source_proxy_only": true, "stage4b_local": false, "stage4c": false, "symbol": "012330", "trigger_date": "2025-01-24", "trigger_family": "AS_core_parts_margin_mix_operating_leverage_bridge", "trigger_type": "Stage3-Yellow", "trough_180D_date": "2025-04-14", "upstream_source": "FinanceData/marcap"}
{"MAE_180D_pct": -22.58, "MAE_30D_pct": -22.58, "MAE_90D_pct": -22.58, "MFE_180D_pct": 17.94, "MFE_30D_pct": 1.25, "MFE_90D_pct": 8.91, "balance_sheet_risk": 42, "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "calibration_usable": true, "canonical_archetype_id": "C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE", "capital_return": 44, "case_id": "C29_R9_L100_204320_20240729_STAGE2A", "classification": "counterexample_high_MAE_before_any_order_margin_confirmation", "company": "HL Mando / HL만도", "corporate_action_window_check": "no 2024-2025 profile candidate overlap flagged in selected 180D window; raw/unadjusted caveat retained", "current_profile_error": "stage2_actionable_too_easy_if_OP_up_without_net_margin_or_customer_mix_confirmation", "demand_volume": 60, "entry_date": "2024-07-29", "entry_price": 39850.0, "evidence_summary": "Q2 2024 revenue and operating profit improved, but net profit missed market expectations; the price path quickly drew down more than 20% before any durable C29 rerating.", "evidence_url": "https://en.yna.co.kr/view/AEN20240726008300320", "fine_archetype_id": "C29_AUTOMOTIVE_VOLUME_MIX_MARGIN_OPERATING_LEVERAGE_BRIDGE_V1", "forward_window_trading_days": 180, "hard_duplicate_check": "new C29 symbol/trigger_date/entry_date family for this local session", "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "mix_margin": 55, "outcome_tag": "early_stage2_false_positive", "peak_180D_date": "2025-02-13", "price_adjustment_status": "raw_unadjusted_marcap", "price_basis": "tradable_raw", "price_data_source": "Songdaiki/stock-web", "price_path_alignment": 35, "raw_total": 61.4, "representative_for_aggregate": true, "revision_visibility": 49, "simulated_stage": "Stage2_only_or_4B_watch", "source_proxy_only": true, "stage4b_local": true, "stage4c": false, "symbol": "204320", "trigger_date": "2024-07-26", "trigger_family": "Q2_parts_revenue_OP_up_but_net_expectation_miss", "trigger_type": "Stage2-Actionable", "trough_180D_date": "2024-09-09", "upstream_source": "FinanceData/marcap"}
{"MAE_180D_pct": -4.77, "MAE_30D_pct": -2.91, "MAE_90D_pct": -4.77, "MFE_180D_pct": 28.48, "MFE_30D_pct": 12.05, "MFE_90D_pct": 15.36, "balance_sheet_risk": 68, "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "calibration_usable": true, "canonical_archetype_id": "C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE", "capital_return": 59, "case_id": "C29_R9_L100_161390_20250205_STAGE3Y", "classification": "positive_clean_bridge", "company": "Hankook Tire & Technology / 한국타이어앤테크놀로지", "corporate_action_window_check": "no 2024-2025 profile candidate overlap flagged in selected 180D window; raw/unadjusted caveat retained", "current_profile_error": "none_or_minor; validates bridge-weighting rather than price-only", "demand_volume": 72, "entry_date": "2025-02-05", "entry_price": 37750.0, "evidence_summary": "2024 sales and operating profit rose strongly, with high-value-added large-rim tire mix supporting margin leverage; the 180D path showed high MFE with shallow MAE.", "evidence_url": "https://www.hankookandcompany.com/en/media/news/article-2229.do", "fine_archetype_id": "C29_AUTOMOTIVE_VOLUME_MIX_MARGIN_OPERATING_LEVERAGE_BRIDGE_V1", "forward_window_trading_days": 180, "hard_duplicate_check": "new C29 symbol/trigger_date/entry_date family for this local session", "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "mix_margin": 84, "outcome_tag": "clean_positive_low_MAE", "peak_180D_date": "2025-07-24", "price_adjustment_status": "raw_unadjusted_marcap", "price_basis": "tradable_raw", "price_data_source": "Songdaiki/stock-web", "price_path_alignment": 82, "raw_total": 81.5, "representative_for_aggregate": true, "revision_visibility": 73, "simulated_stage": "Stage3-Yellow_green_watch", "source_proxy_only": false, "stage4b_local": false, "stage4c": false, "symbol": "161390", "trigger_date": "2025-02-04", "trigger_family": "premium_tire_mix_OP_margin_operating_leverage_bridge", "trigger_type": "Stage3-Yellow", "trough_180D_date": "2025-04-08", "upstream_source": "FinanceData/marcap"}
{"MAE_180D_pct": -5.26, "MAE_30D_pct": -5.26, "MAE_90D_pct": -5.26, "MFE_180D_pct": 48.91, "MFE_30D_pct": 19.64, "MFE_90D_pct": 29.4, "balance_sheet_risk": 70, "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "calibration_usable": true, "canonical_archetype_id": "C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE", "capital_return": 55, "case_id": "C29_R9_L100_011210_20250131_STAGE3Y", "classification": "positive_missed_structural", "company": "Hyundai Wia / 현대위아", "corporate_action_window_check": "no 2024-2025 profile candidate overlap flagged in selected 180D window; raw/unadjusted caveat retained", "current_profile_error": "too_late_if_machine_tool_divestiture_noise_blocks_core_auto_margin_bridge", "demand_volume": 69, "entry_date": "2025-01-31", "entry_price": 38950.0, "evidence_summary": "2024 operating profit remained positive and net income improved sharply; the path showed a strong 180D MFE with shallow MAE, suggesting a missed structural mobility-margin rerating.", "evidence_url": "https://en.hyundai-wia.com/investment/income_statement01.asp", "fine_archetype_id": "C29_AUTOMOTIVE_VOLUME_MIX_MARGIN_OPERATING_LEVERAGE_BRIDGE_V1", "forward_window_trading_days": 180, "hard_duplicate_check": "new C29 symbol/trigger_date/entry_date family for this local session", "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "mix_margin": 77, "outcome_tag": "missed_structural_positive", "peak_180D_date": "2025-10-22", "price_adjustment_status": "raw_unadjusted_marcap", "price_basis": "tradable_raw", "price_data_source": "Songdaiki/stock-web", "price_path_alignment": 88, "raw_total": 82.3, "representative_for_aggregate": true, "revision_visibility": 71, "simulated_stage": "Stage3-Yellow_green_watch", "source_proxy_only": false, "stage4b_local": false, "stage4c": false, "symbol": "011210", "trigger_date": "2025-01-24", "trigger_family": "auto_parts_profitability_net_income_recovery_bridge", "trigger_type": "Stage3-Yellow", "trough_180D_date": "2025-02-03", "upstream_source": "FinanceData/marcap"}
{"MAE_180D_pct": -32.57, "MAE_30D_pct": -13.88, "MAE_90D_pct": -32.57, "MFE_180D_pct": 13.65, "MFE_30D_pct": 10.44, "MFE_90D_pct": 10.44, "balance_sheet_risk": 24, "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "calibration_usable": true, "canonical_archetype_id": "C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE", "capital_return": 25, "case_id": "C29_R9_L100_018880_20250214_STAGE4B", "classification": "counterexample_hard_4B_to_4C_watch", "company": "Hanon Systems / 한온시스템", "corporate_action_window_check": "no 2024-2025 profile candidate overlap flagged in selected 180D window; raw/unadjusted caveat retained", "current_profile_error": "4C_should_trigger_only_after_non_price_margin_break_not_after_generic_EV_slowdown_label", "demand_volume": 42, "entry_date": "2025-02-14", "entry_price": 4360.0, "evidence_summary": "FY2024/Q4 included one-time restructuring and a Q4 operating loss while EV thermal demand stayed weak; the path had poor 90D/180D MAE and only weak rebound MFE.", "evidence_url": "https://www.hanonsystems.com/En/Media/NewsDetails/337", "fine_archetype_id": "C29_AUTOMOTIVE_VOLUME_MIX_MARGIN_OPERATING_LEVERAGE_BRIDGE_V1", "forward_window_trading_days": 180, "hard_duplicate_check": "new C29 symbol/trigger_date/entry_date family for this local session", "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "mix_margin": 31, "outcome_tag": "confirmed_margin_break_counterexample", "peak_180D_date": "2025-10-30", "price_adjustment_status": "raw_unadjusted_marcap", "price_basis": "tradable_raw", "price_data_source": "Songdaiki/stock-web", "price_path_alignment": 22, "raw_total": 49.7, "representative_for_aggregate": true, "revision_visibility": 28, "simulated_stage": "Stage4B_to_4C_watch", "source_proxy_only": false, "stage4b_local": true, "stage4c": true, "symbol": "018880", "trigger_date": "2025-02-13", "trigger_family": "EV_thermal_supplier_restructuring_loss_margin_break", "trigger_type": "Stage4B", "trough_180D_date": "2025-06-02", "upstream_source": "FinanceData/marcap"}
{"MAE_180D_pct": -19.08, "MAE_30D_pct": -9.35, "MAE_90D_pct": -18.44, "MFE_180D_pct": 25.1, "MFE_30D_pct": 2.43, "MFE_90D_pct": 25.1, "balance_sheet_risk": 37, "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "calibration_usable": true, "canonical_archetype_id": "C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE", "capital_return": 30, "case_id": "C29_R9_L100_003620_20250106_STAGE2A", "classification": "counterexample_recovery_spike_without_sustained_bridge", "company": "KG Mobility / KG모빌리티", "corporate_action_window_check": "no 2024-2025 profile candidate overlap flagged in selected 180D window; raw/unadjusted caveat retained", "current_profile_error": "could_false_positive_if_90D_MFE_ignores_later_volume_margin_sustainability", "demand_volume": 58, "entry_date": "2025-01-06", "entry_price": 3905.0, "evidence_summary": "2024 exports rose to a decade high but total sales fell on weak domestic demand. The price path had a short MFE spike but later closed negative over 180D, so export-volume label alone was not enough.", "evidence_url": "https://en.yna.co.kr/view/AEN20250103008700320", "fine_archetype_id": "C29_AUTOMOTIVE_VOLUME_MIX_MARGIN_OPERATING_LEVERAGE_BRIDGE_V1", "forward_window_trading_days": 180, "hard_duplicate_check": "new C29 symbol/trigger_date/entry_date family for this local session", "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "mix_margin": 45, "outcome_tag": "MFE_spike_but_not_sustained", "peak_180D_date": "2025-02-26", "price_adjustment_status": "raw_unadjusted_marcap", "price_basis": "tradable_raw", "price_data_source": "Songdaiki/stock-web", "price_path_alignment": 46, "raw_total": 58.2, "representative_for_aggregate": true, "revision_visibility": 39, "simulated_stage": "Stage2_label_only_with_4B_watch", "source_proxy_only": true, "stage4b_local": true, "stage4c": false, "symbol": "003620", "trigger_date": "2025-01-03", "trigger_family": "export_volume_positive_but_domestic_volume_margin_gap", "trigger_type": "Stage2-Actionable", "trough_180D_date": "2025-10-13", "upstream_source": "FinanceData/marcap"}
```

## 7. Score Simulation JSONL

```jsonl
{"balance_sheet_risk": 58, "capital_return": 63, "case_id": "C29_R9_L100_005380_20240426_STAGE3Y", "current_profile_error": "green_if_unchecked; yellow acceptable only with MAE guard", "demand_volume": 72, "mix_margin": 74, "price_path_alignment": 59, "raw_total": 73.4, "revision_visibility": 66, "simulated_stage": "Stage3-Yellow_not_Green", "symbol": "005380", "trigger_type": "Stage3-Yellow"}
{"balance_sheet_risk": 46, "capital_return": 64, "case_id": "C29_R9_L100_000270_20250131_STAGE2A", "current_profile_error": "stage2_too_easy_if_record_profit_label_without_tariff_sensitivity_filter", "demand_volume": 68, "mix_margin": 70, "price_path_alignment": 40, "raw_total": 66.8, "revision_visibility": 57, "simulated_stage": "Stage2-Actionable_with_4B_watch", "symbol": "000270", "trigger_type": "Stage2-Actionable"}
{"balance_sheet_risk": 62, "capital_return": 54, "case_id": "C29_R9_L100_012330_20250131_STAGE3Y", "current_profile_error": "yellow_timing_ok_but_green_should_wait_for_sustained_revision", "demand_volume": 65, "mix_margin": 78, "price_path_alignment": 71, "raw_total": 76.1, "revision_visibility": 69, "simulated_stage": "Stage3-Yellow", "symbol": "012330", "trigger_type": "Stage3-Yellow"}
{"balance_sheet_risk": 42, "capital_return": 44, "case_id": "C29_R9_L100_204320_20240729_STAGE2A", "current_profile_error": "stage2_actionable_too_easy_if_OP_up_without_net_margin_or_customer_mix_confirmation", "demand_volume": 60, "mix_margin": 55, "price_path_alignment": 35, "raw_total": 61.4, "revision_visibility": 49, "simulated_stage": "Stage2_only_or_4B_watch", "symbol": "204320", "trigger_type": "Stage2-Actionable"}
{"balance_sheet_risk": 68, "capital_return": 59, "case_id": "C29_R9_L100_161390_20250205_STAGE3Y", "current_profile_error": "none_or_minor; validates bridge-weighting rather than price-only", "demand_volume": 72, "mix_margin": 84, "price_path_alignment": 82, "raw_total": 81.5, "revision_visibility": 73, "simulated_stage": "Stage3-Yellow_green_watch", "symbol": "161390", "trigger_type": "Stage3-Yellow"}
{"balance_sheet_risk": 70, "capital_return": 55, "case_id": "C29_R9_L100_011210_20250131_STAGE3Y", "current_profile_error": "too_late_if_machine_tool_divestiture_noise_blocks_core_auto_margin_bridge", "demand_volume": 69, "mix_margin": 77, "price_path_alignment": 88, "raw_total": 82.3, "revision_visibility": 71, "simulated_stage": "Stage3-Yellow_green_watch", "symbol": "011210", "trigger_type": "Stage3-Yellow"}
{"balance_sheet_risk": 24, "capital_return": 25, "case_id": "C29_R9_L100_018880_20250214_STAGE4B", "current_profile_error": "4C_should_trigger_only_after_non_price_margin_break_not_after_generic_EV_slowdown_label", "demand_volume": 42, "mix_margin": 31, "price_path_alignment": 22, "raw_total": 49.7, "revision_visibility": 28, "simulated_stage": "Stage4B_to_4C_watch", "symbol": "018880", "trigger_type": "Stage4B"}
{"balance_sheet_risk": 37, "capital_return": 30, "case_id": "C29_R9_L100_003620_20250106_STAGE2A", "current_profile_error": "could_false_positive_if_90D_MFE_ignores_later_volume_margin_sustainability", "demand_volume": 58, "mix_margin": 45, "price_path_alignment": 46, "raw_total": 58.2, "revision_visibility": 39, "simulated_stage": "Stage2_label_only_with_4B_watch", "symbol": "003620", "trigger_type": "Stage2-Actionable"}
```

## 8. Aggregate Row JSON

```json
{
  "calibration_usable_trigger_count": 8,
  "canonical_archetype_id": "C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE",
  "counterexample_count": 4,
  "current_profile_error_count": 6,
  "deep_sub_archetype_id": "C29_DEEP_AUTO_OEM_PARTS_TIRE_THERMAL_EXPORT_VOLUME_MIX_MARGIN_VS_LABEL_SPIKE",
  "do_not_propose_new_weight_delta": false,
  "evidence_url_pending_count": 0,
  "existing_axis_strengthened": [
    "stage2_required_bridge",
    "local_4b_watch_guard",
    "price_only_blowoff_blocks_positive_stage",
    "full_4b_requires_non_price_evidence"
  ],
  "existing_axis_weakened": [
    "hard_4c_thesis_break_routes_to_4c_when_only_generic_auto_volume_or_mobility_label_is_present"
  ],
  "fine_archetype_id": "C29_AUTOMOTIVE_VOLUME_MIX_MARGIN_OPERATING_LEVERAGE_BRIDGE_V1",
  "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY",
  "loop_contribution_label": "canonical_archetype_rule_candidate",
  "new_axis_proposed": "C29_verified_volume_mix_margin_operating_leverage_bridge_required_before_Yellow_or_Green_plus_mobility_label_spike_to_local_4B_or_4C_watch",
  "new_independent_case_count": 8,
  "positive_case_count": 4,
  "promotion_blocked_until_url_repair": "true_for_source_proxy_rows_only",
  "representative_trigger_count": 8,
  "reused_case_count": 0,
  "same_archetype_new_symbol_count": 8,
  "selected_loop": 100,
  "selected_round": "R9",
  "source_proxy_only_count": 4,
  "stage4b_case_count": 5,
  "stage4c_case_count": 1,
  "trigger_row_count": 8
}
```

## 9. Validation Scope

```yaml
validation_scope: historical_trigger_level_calibration
live_candidate_mode: false
current_stock_discovery_allowed: false
brokerage_api_allowed: false
stock_agent_code_patch_allowed: false
stock_agent_src_accessed: false
stock_web_price_atlas_accessed: true
MFE_MAE_complete_for_all_usable_trigger_rows: true
calibration_usable_trigger_count: 8
narrative_only_or_rejected_count: 0
hard_duplicate_policy: canonical_archetype_id + symbol + trigger_type + entry_date not repeated within local C29 loop
```

## 10. Deferred Coding Agent Handoff Prompt

```text
Do not execute this handoff in the research session. In a later coding-agent batch, ingest this MD as a V12 result and evaluate whether C29 should receive a scoped bridge rule: verified volume/mix/margin operating-leverage evidence is required before Yellow/Green, while generic auto/mobility label spikes route to local 4B watch unless issuer-level margin/demand break confirms hard 4C. Preserve global Stage3-Green strictness; do not loosen global thresholds.
```

## 11. Next Research State

```text
completed_round = R9
completed_loop = 100
selection_basis = docs/core/V12_Research_No_Repeat_Index.md
selected_priority_bucket = Priority 2 quality_repair_after_local_priority0_priority1_fill
next_recommended_archetypes = C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK, R13_CROSS_ARCHETYPE_4B_4C_REDTEAM, C31_POLICY_SUBSIDY_LEGISLATION_EVENT, C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP, C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE
round_schedule_status = coverage_index_selected
round_sector_consistency = pass
```