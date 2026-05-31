# E2R V12 No-Repeat Standalone Residual Research
## R1 / L1 / C03 — Defense export framework backlog / armored-vehicle 4B guard

metadata:
```text
selected_round: R1
scheduler_override_used: true
scheduled_round_inherited: false
large_sector_id: L1_INDUSTRIALS_INFRA_DEFENSE_GRID
canonical_archetype_id: C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG
fine_archetype_id: ARMORED_VEHICLE_POWERPACK_EXPORT_BACKLOG_4B_GUARD
loop_objective: coverage_gap_fill|new_symbol_expansion|new_trigger_family|counterexample_mining|positive_counterexample_balance|4B_after_export_framework_premium|green_strictness_stress_test
price_source: Songdaiki/stock-web
stock_web_manifest_max_date: 2026-02-20
output_file: e2r_stock_web_v12_no_repeat_standalone_L1_INDUSTRIALS_INFRA_DEFENSE_GRID_C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG_armored_vehicle_powerpack_4b_2022_2024_research.md
production_scoring_changed: false
shadow_weight_only: true
```

## 1. Prompt / no-repeat basis

This MD follows `docs/core/e2r_v12_prompt_round_scheduler_corrected.txt` as a standalone historical residual research artifact.  
`V12_Research_No_Repeat_Index.md` is used only for duplicate avoidance and coverage-gap selection.

No-Repeat selection:
```text
C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG current coverage:
rows=7, symbols=4, date range=2022-07-29~2024-11-12, good/bad S2=4/1, 4B/4C=0/0
top covered symbols: 012450(3), 079550(2), 047810(1), 065450(1)
```

This run avoids those top-covered C03 symbols and adds 064350 and 003570.  
Each row uses a new `C03 + symbol + trigger_type + entry_date` hard key.

## 2. Stock-Web source check

Manifest:
```text
source_name: FinanceData/marcap
price_adjustment_status: raw_unadjusted_marcap
min_date: 1995-05-02
max_date: 2026-02-20
tradable_row_count: 14354401
calibration_shard_root: atlas/ohlcv_tradable_by_symbol_year
raw_shard_root: atlas/ohlcv_raw_by_symbol_year
```

Selected profiles:
```text
064350 현대로템: selected 2022/2023 forward window clean; corporate-action candidate is 2020-08-14 and outside selected test window.
003570 SNT다이내믹스: selected 2024 forward window clean; corporate-action candidates are 1998/2000/2003/2006 and outside selected test window.
```

## 3. Research thesis

C03 should not treat every defense export framework headline as fully bankable backlog. It should test whether framework attention becomes signed, financeable, deliverable and margin-accretive backlog:

```text
defense export framework / backlog attention
→ signed tranche and customer financing
→ delivery schedule, localization or offset clarity
→ production capacity and subsystem allocation
→ acceptance, margin and revision bridge
→ rerating or local 4B cap
```

An export framework is the map. Green should require the convoy: signed tranche, funded customer, delivery slots, factory capacity and a margin bridge.

## 4. Case table

| case_id | symbol | role | entry | entry_price | peak | low_180d | MFE_30D | MFE_90D | MFE_180D | MAE_180D | post-peak DD |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| C03_064350_HYUNDAIROTEM_20220729_POLAND_K2_FRAMEWORK_STAGE2 | 064350 | positive_armored_vehicle_export_framework_stage2_success_with_later_4b | 2022-07-29 | 26550 | 32850 on 2022-08-26 | 23050 on 2022-10-27 | 23.73% | 23.73% | 23.73% | -13.18% | -29.83% |
| C03_064350_HYUNDAIROTEM_20220826_POLAND_K2_EXPORT_PREMIUM_4B | 064350 | armored_vehicle_export_framework_price_premium_counterexample | 2022-08-26 | 30550 | 32850 on 2022-08-26 | 23050 on 2022-10-27 | 7.53% | 7.53% | 7.53% | -24.55% | -29.83% |
| C03_003570_SNTDYNAMICS_20240228_POWERPACK_BACKLOG_STAGE2 | 003570 | positive_powerpack_transmission_backlog_stage2_success_with_later_4b_watch | 2024-02-28 | 18340 | 26750 on 2024-07-26 | 16220 on 2024-03-21 | 8.78% | 22.41% | 45.86% | -11.56% | -30.47% |

## 5. Stage evidence split

### Stage2 / Stage2-Actionable
- Defense export-framework backlog can be a valid Stage2 route when the framework is tied to signed tranche visibility, customer financing, delivery schedule and margin/revision route.
- 064350 is the prime-contractor armored-vehicle positive anchor. The July 2022 export-framework trigger produced meaningful MFE before the August premium became a 4B problem.
- 003570 is the subsystem/powerpack anchor. The February 2024 row shows that subsystem allocation can become Stage2 when it creates a direct bridge from prime export cycle to revenue and margin.

### Stage3 / Green
- C03 Green should require signed tranche, customer financing, delivery schedule, localization/offset clarity, production capacity and margin/revision confirmation.
- Framework headlines alone are not enough. The model should ask whether the order is funded, factory-scheduled, accepted and margin-accretive.

### 4B
- 064350 / 2022-08-26 fills the missing local 4B pocket for C03. The price had already capitalized the initial framework, and the forward path produced a meaningful post-peak drawdown until incremental tranche/delivery evidence refreshed.
- The key guard is simple: after the first export-framework rerating, price strength cannot substitute for a new signed tranche, delivery slot, capacity plan and revision bridge.

### 4C
- No hard contract cancellation, financing failure, or production halt is asserted.
- The C03 break mode in this MD is not a thesis break. It is export-framework evidence exhaustion: the framework remains plausible, but incremental tranche/delivery/margin evidence does not support the price already paid.

## 6. Raw component score breakdown

```json
{
  "C03_003570_SNTDYNAMICS_20240228_POWERPACK_BACKLOG_STAGE2": {
    "customer_financing_visibility": 6,
    "delivery_capacity_bridge": 8,
    "export_framework_backlog": 9,
    "information_confidence": 4,
    "margin_revision_bridge": 6,
    "market_mispricing": 9,
    "total": 48,
    "valuation_rerating_runway": 6
  },
  "C03_064350_HYUNDAIROTEM_20220729_POLAND_K2_FRAMEWORK_STAGE2": {
    "customer_financing_visibility": 8,
    "delivery_capacity_bridge": 8,
    "export_framework_backlog": 11,
    "information_confidence": 4,
    "margin_revision_bridge": 7,
    "market_mispricing": 10,
    "total": 55,
    "valuation_rerating_runway": 7
  },
  "C03_064350_HYUNDAIROTEM_20220826_POLAND_K2_EXPORT_PREMIUM_4B": {
    "customer_financing_visibility": 4,
    "delivery_capacity_bridge": 4,
    "export_framework_backlog": 7,
    "information_confidence": 3,
    "margin_revision_bridge": 3,
    "market_mispricing": 4,
    "total": 26,
    "valuation_rerating_runway": 1
  }
}
```

## 7. Current calibrated profile stress test

Suggested C03 guard:
```text
if defense_export_framework and signed_tranche_financing_delivery_margin_bridge_visible:
    allow_stage2_actionable = true

if defense_export_framework_price_premium and no incremental_signed_tranche_delivery_margin_revision_bridge:
    block_stage3_green = true
    route_to_local_4B_watch = true

if subsystem_export_chain and allocation_capacity_margin_bridge_visible:
    allow_subsystem_stage2_but_require_prime_to_subsystem_bridge = true
```

Residual error:
```text
current_profile_error_count = 1
- 064350 / 2022-08-26: prime-contractor export framework can be over-promoted if the model treats the first framework premium as fresh signed tranche, delivery and margin proof.
```

## 8. Machine-readable rows

```jsonl
{"MAE_180D_pct": -13.18, "MAE_30D_pct": -9.42, "MAE_90D_pct": -13.18, "MFE_180D_pct": 23.73, "MFE_30D_pct": 23.73, "MFE_90D_pct": 23.73, "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "calibration_usable": true, "canonical_archetype_id": "C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG", "case_id": "C03_064350_HYUNDAIROTEM_20220729_POLAND_K2_FRAMEWORK_STAGE2", "case_role": "positive_armored_vehicle_export_framework_stage2_success_with_later_4b", "company_name": "현대로템", "corporate_action_window_status": "clean_2022_2023_forward_window; corporate-action candidate is 2020-08-14 and outside selected test window", "current_profile_error": false, "current_profile_verdict": "Stage2 was useful when armored-vehicle export framework/backlog evidence appeared before the export premium was fully capitalized. Green still requires signed tranche visibility, customer financing, delivery schedule, localization/offset, production capacity and margin/revision bridge; after the August 2022 premium the same evidence required local 4B discipline.", "dedupe_for_aggregate": true, "do_not_count_as_new_case": false, "drawdown_after_peak_pct": -29.83, "entry_date": "2022-07-29", "entry_price": 26550, "evidence_family": "poland_k2_armored_vehicle_export_framework_backlog_capacity_stage2_route", "evidence_url_pending": false, "fine_archetype_id": "ARMORED_VEHICLE_POWERPACK_EXPORT_BACKLOG_4B_GUARD", "forward_window_trading_days": 180, "independent_evidence_weight": 1.0, "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "low_date_180d": "2022-10-27", "low_price_180d": 23050, "peak_date": "2022-08-26", "peak_price": 32850, "positive_or_counterexample": "positive", "price_adjustment_status": "raw_unadjusted_marcap", "price_basis": "tradable_raw", "price_data_source": "Songdaiki/stock-web", "profile_path": "atlas/symbol_profiles/064/064350.json", "raw_component_score_breakdown": {"customer_financing_visibility": 8, "delivery_capacity_bridge": 8, "export_framework_backlog": 11, "information_confidence": 4, "margin_revision_bridge": 7, "market_mispricing": 10, "total": 55, "valuation_rerating_runway": 7}, "reuse_reason": null, "same_entry_group_id": "C03_064350_HYUNDAIROTEM_20220729_POLAND_K2_FRAMEWORK_STAGE2", "schema_version": "v12_no_repeat_standalone_trigger_row_v1", "selected_round": "R1", "source_proxy_only": false, "stage2_evidence_fields": ["defense_export_framework_or_backlog_attention", "signed_tranche_customer_financing_or_subsystem_allocation_visibility", "delivery_capacity_margin_revision_route"], "stage3_evidence_fields": ["signed_tranche_and_delivery_schedule_required", "customer_financing_localization_offset_required", "capacity_acceptance_margin_revision_bridge_required"], "stage4b_evidence_fields": ["defense_export_framework_price_premium", "valuation_or_positioning_overheat", "post_peak_drawdown"], "stage4c_evidence_fields": ["tranche_or_financing_delay", "delivery_acceptance_capacity_bottleneck", "margin_revision_bridge_failure"], "symbol": "064350", "tradable_shard_path": "atlas/ohlcv_tradable_by_symbol_year/064/064350/2022.csv", "trigger_date": "2022-07-29", "trigger_type": "Stage2-Actionable", "upstream_source": "FinanceData/marcap"}
{"MAE_180D_pct": -24.55, "MAE_30D_pct": -23.08, "MAE_90D_pct": -24.55, "MFE_180D_pct": 7.53, "MFE_30D_pct": 7.53, "MFE_90D_pct": 7.53, "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "calibration_usable": true, "canonical_archetype_id": "C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG", "case_id": "C03_064350_HYUNDAIROTEM_20220826_POLAND_K2_EXPORT_PREMIUM_4B", "case_role": "armored_vehicle_export_framework_price_premium_counterexample", "company_name": "현대로템", "corporate_action_window_status": "clean_2022_2023_forward_window; corporate-action candidate is 2020-08-14 and outside selected test window", "current_profile_error": true, "current_profile_verdict": "Armored-vehicle export-framework price premium should route to local 4B or counterexample unless incremental signed tranche, financing, delivery schedule, capacity and margin/revision evidence keep expanding after the spike.", "dedupe_for_aggregate": true, "do_not_count_as_new_case": false, "drawdown_after_peak_pct": -29.83, "entry_date": "2022-08-26", "entry_price": 30550, "evidence_family": "armored_vehicle_export_framework_price_premium_without_incremental_tranche_delivery_margin_revision", "evidence_url_pending": false, "fine_archetype_id": "ARMORED_VEHICLE_POWERPACK_EXPORT_BACKLOG_4B_GUARD", "forward_window_trading_days": 180, "independent_evidence_weight": 1.0, "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "low_date_180d": "2022-10-27", "low_price_180d": 23050, "peak_date": "2022-08-26", "peak_price": 32850, "positive_or_counterexample": "counterexample", "price_adjustment_status": "raw_unadjusted_marcap", "price_basis": "tradable_raw", "price_data_source": "Songdaiki/stock-web", "profile_path": "atlas/symbol_profiles/064/064350.json", "raw_component_score_breakdown": {"customer_financing_visibility": 4, "delivery_capacity_bridge": 4, "export_framework_backlog": 7, "information_confidence": 3, "margin_revision_bridge": 3, "market_mispricing": 4, "total": 26, "valuation_rerating_runway": 1}, "reuse_reason": null, "same_entry_group_id": "C03_064350_HYUNDAIROTEM_20220826_POLAND_K2_EXPORT_PREMIUM_4B", "schema_version": "v12_no_repeat_standalone_trigger_row_v1", "selected_round": "R1", "source_proxy_only": false, "stage2_evidence_fields": ["defense_export_framework_or_backlog_attention", "signed_tranche_customer_financing_or_subsystem_allocation_visibility", "delivery_capacity_margin_revision_route"], "stage3_evidence_fields": ["signed_tranche_and_delivery_schedule_required", "customer_financing_localization_offset_required", "capacity_acceptance_margin_revision_bridge_required"], "stage4b_evidence_fields": ["defense_export_framework_price_premium", "valuation_or_positioning_overheat", "post_peak_drawdown"], "stage4c_evidence_fields": ["tranche_or_financing_delay", "delivery_acceptance_capacity_bottleneck", "margin_revision_bridge_failure"], "symbol": "064350", "tradable_shard_path": "atlas/ohlcv_tradable_by_symbol_year/064/064350/2022.csv", "trigger_date": "2022-08-26", "trigger_type": "4B-local-price-only", "upstream_source": "FinanceData/marcap"}
{"MAE_180D_pct": -11.56, "MAE_30D_pct": -11.56, "MAE_90D_pct": -11.56, "MFE_180D_pct": 45.86, "MFE_30D_pct": 8.78, "MFE_90D_pct": 22.41, "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "calibration_usable": true, "canonical_archetype_id": "C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG", "case_id": "C03_003570_SNTDYNAMICS_20240228_POWERPACK_BACKLOG_STAGE2", "case_role": "positive_powerpack_transmission_backlog_stage2_success_with_later_4b_watch", "company_name": "SNT다이내믹스", "corporate_action_window_status": "clean_2024_forward_window; corporate-action candidates are 1998-12-22, 2000-04-28, 2000-07-03, 2003-03-31, 2006-04-05, all outside selected test window", "current_profile_error": false, "current_profile_verdict": "Subsystem defense-export rows can be valid Stage2 when powerpack/transmission backlog or customer allocation evidence creates a direct bridge from the prime-contract export cycle to revenue and margin. Green still requires subsystem share, production schedule, customer acceptance, pass-through and revision confirmation.", "dedupe_for_aggregate": true, "do_not_count_as_new_case": false, "drawdown_after_peak_pct": -30.47, "entry_date": "2024-02-28", "entry_price": 18340, "evidence_family": "armored_vehicle_powerpack_transmission_export_backlog_subsystem_stage2_route", "evidence_url_pending": false, "fine_archetype_id": "ARMORED_VEHICLE_POWERPACK_EXPORT_BACKLOG_4B_GUARD", "forward_window_trading_days": 180, "independent_evidence_weight": 1.0, "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "low_date_180d": "2024-03-21", "low_price_180d": 16220, "peak_date": "2024-07-26", "peak_price": 26750, "positive_or_counterexample": "positive", "price_adjustment_status": "raw_unadjusted_marcap", "price_basis": "tradable_raw", "price_data_source": "Songdaiki/stock-web", "profile_path": "atlas/symbol_profiles/003/003570.json", "raw_component_score_breakdown": {"customer_financing_visibility": 6, "delivery_capacity_bridge": 8, "export_framework_backlog": 9, "information_confidence": 4, "margin_revision_bridge": 6, "market_mispricing": 9, "total": 48, "valuation_rerating_runway": 6}, "reuse_reason": null, "same_entry_group_id": "C03_003570_SNTDYNAMICS_20240228_POWERPACK_BACKLOG_STAGE2", "schema_version": "v12_no_repeat_standalone_trigger_row_v1", "selected_round": "R1", "source_proxy_only": false, "stage2_evidence_fields": ["defense_export_framework_or_backlog_attention", "signed_tranche_customer_financing_or_subsystem_allocation_visibility", "delivery_capacity_margin_revision_route"], "stage3_evidence_fields": ["signed_tranche_and_delivery_schedule_required", "customer_financing_localization_offset_required", "capacity_acceptance_margin_revision_bridge_required"], "stage4b_evidence_fields": ["defense_export_framework_price_premium", "valuation_or_positioning_overheat", "post_peak_drawdown"], "stage4c_evidence_fields": ["tranche_or_financing_delay", "delivery_acceptance_capacity_bottleneck", "margin_revision_bridge_failure"], "symbol": "003570", "tradable_shard_path": "atlas/ohlcv_tradable_by_symbol_year/003/003570/2024.csv", "trigger_date": "2024-02-28", "trigger_type": "Stage2-Actionable", "upstream_source": "FinanceData/marcap"}
```

## 9. Aggregate row

```json
{
  "calibration_usable_case_count": 3,
  "canonical_archetype_id": "C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG",
  "counterexample_count": 1,
  "current_profile_error_count": 1,
  "evidence_url_pending_count": 0,
  "fine_archetype_id": "ARMORED_VEHICLE_POWERPACK_EXPORT_BACKLOG_4B_GUARD",
  "hard_duplicate_avoided": true,
  "index_update_needed": true,
  "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID",
  "loop_contribution_label": "defense_export_framework_armored_vehicle_powerpack_backlog_4b_guard",
  "new_independent_case_count": 3,
  "positive_case_count": 2,
  "reused_case_count": 0,
  "schema_version": "v12_no_repeat_standalone_aggregate_v1",
  "selected_round": "R1",
  "shadow_rule_candidate": "C03 defense export-framework rows should allow Stage2 when export framework/backlog evidence is backed by signed tranches, financing, delivery schedule, subsystem allocation and margin/revision bridge, but should route to local 4B when the price already capitalizes the framework and incremental tranche/delivery evidence has not refreshed.",
  "source_proxy_only_count": 0
}
```


## 10. Deferred Coding Agent Handoff Prompt

Do not execute this handoff inside the research session.

```text
Read this standalone v12 residual research MD.
Before batch apply:
1. Verify all OHLC rows again from Songdaiki/stock-web tradable shards.
2. Check no hard duplicate exists for C03 + symbol + trigger_type + entry_date.
3. Add C03-specific defense export-framework / signed-tranche / financing / delivery-capacity / margin-revision / local-4B guard only as a shadow candidate until more rows exist.

Candidate rule:
- C03_STAGE2_ALLOWED_ON_SIGNED_TRANCHE_FINANCING_DELIVERY_MARGIN_BRIDGE
- C03_GREEN_REQUIRES_TRANCHE_FINANCING_LOCALIZATION_CAPACITY_ACCEPTANCE_REVISION
- C03_EXPORT_FRAMEWORK_PRICE_PREMIUM_LOCAL_4B
- C03_SUBSYSTEM_STAGE2_REQUIRES_PRIME_TO_SUBSYSTEM_ALLOCATION_BRIDGE

Do not lower global Stage3 Green thresholds.
Do not treat this single MD as production-ready.
```

## 11. Final contribution line

This loop adds 3 new independent cases, 1 counterexample, and 1 current-profile residual error for R1/L1_INDUSTRIALS_INFRA_DEFENSE_GRID/C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG.

