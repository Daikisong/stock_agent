# E2R V12 No-Repeat Standalone Residual Research
## R1 / L1 / C03 — Defense export framework / prime-subsystem 4B refresh guard

metadata:
```text
selected_round: R1
scheduler_override_used: true
scheduled_round_inherited: false
large_sector_id: L1_INDUSTRIALS_INFRA_DEFENSE_GRID
canonical_archetype_id: C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG
fine_archetype_id: DEFENSE_SUBSYSTEM_PRIME_4B_REFRESH_GUARD
loop_objective: coverage_gap_fill|new_symbol_expansion|new_trigger_family|counterexample_mining|positive_counterexample_balance|4B_after_export_framework_premium|green_strictness_stress_test
price_source: Songdaiki/stock-web
stock_web_manifest_max_date: 2026-02-20
output_file: e2r_stock_web_v12_no_repeat_standalone_L1_INDUSTRIALS_INFRA_DEFENSE_GRID_C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG_defense_subsystem_prime_4b_refresh_2023_2024_research.md
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

This run avoids those top-covered C03 symbols and adds 064350, 003570 and the new symbol 077970.  
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
064350 현대로템: selected 2023 forward window clean; corporate-action candidate is 2020-08-14 and outside selected test window.
003570 SNT다이내믹스: selected 2024/2025 forward window clean; corporate-action candidates are 1998/2000/2003/2006 and outside selected test window.
077970 STX엔진: selected 2024/2025 pre-2025-04-21 event window clean; next corporate-action candidate is 2025-04-21, after the selected post-peak low.
```

## 3. Research thesis

C03 should distinguish fresh defense backlog from an already-capitalized export framework premium:

```text
defense export framework / subsystem backlog attention
→ signed tranche, customer order or subsystem allocation
→ customer financing, delivery schedule and acceptance
→ production capacity, input-cost pass-through and localization/offset
→ margin and revision bridge
→ rerating or local 4B cap
```

The first export framework is the map. Stage2 can follow the map when the convoy begins to move. Green should require the convoy itself: signed tranche, funded customer, delivery slot, subsystem allocation and margin bridge. If the market has already paid for the map, stale evidence becomes 4B.

## 4. Case table

| case_id | symbol | role | entry | entry_price | peak | low_180d | MFE_30D | MFE_90D | MFE_180D | MAE_180D | post-peak DD |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| C03_064350_HYUNDAIROTEM_20230705_EXPORT_FRAMEWORK_PREMIUM_4B_REFRESH | 064350 | prime_armored_vehicle_export_framework_premium_counterexample | 2023-07-05 | 38550 | 39500 on 2023-07-05 | 26550 on 2023-10-04 | 2.46% | 2.46% | 2.46% | -31.13% | -32.78% |
| C03_003570_SNTDYNAMICS_20240726_POWERPACK_SUBSYSTEM_BACKLOG_STAGE2 | 003570 | positive_powerpack_subsystem_backlog_stage2_success_with_later_4b_refresh | 2024-07-26 | 21150 | 37800 on 2025-03-12 | 16260 on 2024-12-09 | 26.48% | 33.33% | 78.72% | -23.12% | -28.44% |
| C03_077970_STXENGINE_20240816_NAVAL_DEFENSE_ENGINE_BACKLOG_STAGE2 | 077970 | positive_naval_defense_engine_backlog_stage2_success_with_later_4b_watch | 2024-08-16 | 21550 | 31650 on 2025-02-18 | 15150 on 2024-12-09 | 13.23% | 13.23% | 46.87% | -29.7% | -42.15% |

## 5. Stage evidence split

### Stage2 / Stage2-Actionable
- Defense export-framework backlog can be a valid Stage2 route when backed by signed tranche/customer order, delivery schedule and margin/revision visibility.
- 003570 is the subsystem anchor: powerpack/transmission allocation links the prime export cycle to direct revenue and margin.
- 077970 adds a new engine-subsystem symbol: naval/defense engine backlog is a Stage2 route only when customer order duration and delivery cadence are visible.

### Stage3 / Green
- C03 Green should require signed tranche or customer order duration, financing, localization/offset or subsystem acceptance, production capacity and margin/revision confirmation.
- Subsystem rows need an extra bridge: the model should prove that the prime contract pulls through to the subsystem supplier rather than merely importing the prime-contractor narrative.

### 4B
- 064350 / 2023-07-05 fills a prime-contractor 4B refresh pocket. The prior framework was real, but by this point the price needed fresh signed tranche/delivery/margin evidence. The stock made its forward high at the trigger window and then drew down.
- 003570 and 077970 both remain eligible for later 4B refresh after their Stage2 paths become capitalized.

### 4C
- No hard contract cancellation, financing failure or production halt is asserted.
- The failure mode here is evidence staleness, not thesis death: framework/backlog remains plausible, but incremental tranche/order/delivery/margin evidence must refresh before Green.

## 6. Raw component score breakdown

```json
{
  "C03_003570_SNTDYNAMICS_20240726_POWERPACK_SUBSYSTEM_BACKLOG_STAGE2": {
    "customer_financing_visibility": 5,
    "delivery_capacity_bridge": 8,
    "export_framework_backlog": 9,
    "information_confidence": 4,
    "margin_revision_bridge": 6,
    "market_mispricing": 9,
    "signed_tranche_visibility": 6,
    "total": 54,
    "valuation_rerating_runway": 7
  },
  "C03_064350_HYUNDAIROTEM_20230705_EXPORT_FRAMEWORK_PREMIUM_4B_REFRESH": {
    "customer_financing_visibility": 4,
    "delivery_capacity_bridge": 4,
    "export_framework_backlog": 7,
    "information_confidence": 3,
    "margin_revision_bridge": 3,
    "market_mispricing": 4,
    "signed_tranche_visibility": 4,
    "total": 30,
    "valuation_rerating_runway": 1
  },
  "C03_077970_STXENGINE_20240816_NAVAL_DEFENSE_ENGINE_BACKLOG_STAGE2": {
    "customer_financing_visibility": 5,
    "delivery_capacity_bridge": 7,
    "export_framework_backlog": 8,
    "information_confidence": 4,
    "margin_revision_bridge": 6,
    "market_mispricing": 8,
    "signed_tranche_visibility": 6,
    "total": 50,
    "valuation_rerating_runway": 6
  }
}
```

## 7. Current calibrated profile stress test

Suggested C03 guard:
```text
if defense_export_framework and signed_tranche_order_delivery_margin_bridge_visible:
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
- 064350 / 2023-07-05: prime-contractor export framework can be over-promoted if the model treats stale framework evidence as fresh signed tranche, delivery and margin proof.
```

## 8. Machine-readable rows

```jsonl
{"MAE_180D_pct": -31.13, "MAE_30D_pct": -26.85, "MAE_90D_pct": -31.13, "MFE_180D_pct": 2.46, "MFE_30D_pct": 2.46, "MFE_90D_pct": 2.46, "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "calibration_usable": true, "canonical_archetype_id": "C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG", "case_id": "C03_064350_HYUNDAIROTEM_20230705_EXPORT_FRAMEWORK_PREMIUM_4B_REFRESH", "case_role": "prime_armored_vehicle_export_framework_premium_counterexample", "company_name": "현대로템", "corporate_action_window_status": "clean_2023_forward_window; corporate-action candidate is 2020-08-14 and outside selected test window", "current_profile_error": true, "current_profile_verdict": "Prime-contractor export-framework premium should route to local 4B when the first framework and early delivery narrative is already capitalized but incremental signed tranche, financing, production/delivery schedule, localization/offset and margin/revision evidence have not refreshed.", "dedupe_for_aggregate": true, "do_not_count_as_new_case": false, "drawdown_after_peak_pct": -32.78, "entry_date": "2023-07-05", "entry_price": 38550, "evidence_family": "prime_armored_vehicle_export_framework_price_premium_without_incremental_signed_tranche_delivery_margin_revision", "evidence_url_pending": false, "fine_archetype_id": "DEFENSE_SUBSYSTEM_PRIME_4B_REFRESH_GUARD", "forward_window_trading_days": 180, "independent_evidence_weight": 1.0, "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "low_date_180d": "2023-10-04", "low_price_180d": 26550, "peak_date": "2023-07-05", "peak_price": 39500, "positive_or_counterexample": "counterexample", "price_adjustment_status": "raw_unadjusted_marcap", "price_basis": "tradable_raw", "price_data_source": "Songdaiki/stock-web", "profile_path": "atlas/symbol_profiles/064/064350.json", "raw_component_score_breakdown": {"customer_financing_visibility": 4, "delivery_capacity_bridge": 4, "export_framework_backlog": 7, "information_confidence": 3, "margin_revision_bridge": 3, "market_mispricing": 4, "signed_tranche_visibility": 4, "total": 30, "valuation_rerating_runway": 1}, "reuse_reason": null, "same_entry_group_id": "C03_064350_HYUNDAIROTEM_20230705_EXPORT_FRAMEWORK_PREMIUM_4B_REFRESH", "schema_version": "v12_no_repeat_standalone_trigger_row_v1", "selected_round": "R1", "source_proxy_only": false, "stage2_evidence_fields": ["defense_export_framework_or_subsystem_backlog_attention", "signed_tranche_customer_order_or_subsystem_allocation_visibility", "delivery_capacity_margin_revision_route"], "stage3_evidence_fields": ["signed_tranche_order_duration_and_customer_financing_required", "delivery_schedule_localization_offset_or_subsystem_acceptance_required", "capacity_input_cost_margin_revision_bridge_required"], "stage4b_evidence_fields": ["defense_export_framework_or_subsystem_price_premium", "valuation_or_positioning_overheat", "post_peak_drawdown"], "stage4c_evidence_fields": ["tranche_financing_or_customer_order_delay", "delivery_acceptance_capacity_bottleneck", "margin_revision_bridge_failure"], "symbol": "064350", "tradable_shard_path": "atlas/ohlcv_tradable_by_symbol_year/064/064350/2023.csv", "trigger_date": "2023-07-05", "trigger_type": "4B-local-price-only", "upstream_source": "FinanceData/marcap"}
{"MAE_180D_pct": -23.12, "MAE_30D_pct": -12.06, "MAE_90D_pct": -23.12, "MFE_180D_pct": 78.72, "MFE_30D_pct": 26.48, "MFE_90D_pct": 33.33, "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "calibration_usable": true, "canonical_archetype_id": "C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG", "case_id": "C03_003570_SNTDYNAMICS_20240726_POWERPACK_SUBSYSTEM_BACKLOG_STAGE2", "case_role": "positive_powerpack_subsystem_backlog_stage2_success_with_later_4b_refresh", "company_name": "SNT다이내믹스", "corporate_action_window_status": "clean_2024_2025_forward_window; corporate-action candidates are 1998-12-22, 2000-04-28, 2000-07-03, 2003-03-31, 2006-04-05, all outside selected test window", "current_profile_error": false, "current_profile_verdict": "Subsystem defense-export rows can be Stage2 when powerpack/transmission allocation links the prime export cycle to revenue and margin. Green still requires named subsystem share, production slot, customer acceptance, input-cost pass-through and revision bridge; after the later rerating, 4B refresh discipline is still required.", "dedupe_for_aggregate": true, "do_not_count_as_new_case": false, "drawdown_after_peak_pct": -28.44, "entry_date": "2024-07-26", "entry_price": 21150, "evidence_family": "armored_vehicle_powerpack_transmission_subsystem_allocation_backlog_stage2_route", "evidence_url_pending": false, "fine_archetype_id": "DEFENSE_SUBSYSTEM_PRIME_4B_REFRESH_GUARD", "forward_window_trading_days": 180, "independent_evidence_weight": 1.0, "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "low_date_180d": "2024-12-09", "low_price_180d": 16260, "peak_date": "2025-03-12", "peak_price": 37800, "positive_or_counterexample": "positive", "price_adjustment_status": "raw_unadjusted_marcap", "price_basis": "tradable_raw", "price_data_source": "Songdaiki/stock-web", "profile_path": "atlas/symbol_profiles/003/003570.json", "raw_component_score_breakdown": {"customer_financing_visibility": 5, "delivery_capacity_bridge": 8, "export_framework_backlog": 9, "information_confidence": 4, "margin_revision_bridge": 6, "market_mispricing": 9, "signed_tranche_visibility": 6, "total": 54, "valuation_rerating_runway": 7}, "reuse_reason": null, "same_entry_group_id": "C03_003570_SNTDYNAMICS_20240726_POWERPACK_SUBSYSTEM_BACKLOG_STAGE2", "schema_version": "v12_no_repeat_standalone_trigger_row_v1", "selected_round": "R1", "source_proxy_only": false, "stage2_evidence_fields": ["defense_export_framework_or_subsystem_backlog_attention", "signed_tranche_customer_order_or_subsystem_allocation_visibility", "delivery_capacity_margin_revision_route"], "stage3_evidence_fields": ["signed_tranche_order_duration_and_customer_financing_required", "delivery_schedule_localization_offset_or_subsystem_acceptance_required", "capacity_input_cost_margin_revision_bridge_required"], "stage4b_evidence_fields": ["defense_export_framework_or_subsystem_price_premium", "valuation_or_positioning_overheat", "post_peak_drawdown"], "stage4c_evidence_fields": ["tranche_financing_or_customer_order_delay", "delivery_acceptance_capacity_bottleneck", "margin_revision_bridge_failure"], "symbol": "003570", "tradable_shard_path": "atlas/ohlcv_tradable_by_symbol_year/003/003570/2024.csv", "trigger_date": "2024-07-26", "trigger_type": "Stage2-Actionable", "upstream_source": "FinanceData/marcap"}
{"MAE_180D_pct": -29.7, "MAE_30D_pct": -20.46, "MAE_90D_pct": -29.7, "MFE_180D_pct": 46.87, "MFE_30D_pct": 13.23, "MFE_90D_pct": 13.23, "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "calibration_usable": true, "canonical_archetype_id": "C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG", "case_id": "C03_077970_STXENGINE_20240816_NAVAL_DEFENSE_ENGINE_BACKLOG_STAGE2", "case_role": "positive_naval_defense_engine_backlog_stage2_success_with_later_4b_watch", "company_name": "STX엔진", "corporate_action_window_status": "clean_2024_2025_pre_2025_04_21_window; next corporate-action candidate is 2025-04-21 and outside the selected post-peak low calculation", "current_profile_error": false, "current_profile_verdict": "Defense-engine subsystem rows can be valid Stage2 when customer order/backlog and delivery visibility connect to ship/defense export cycles. Green still requires order duration, customer mix, delivery schedule, engine capacity, input-cost pass-through and margin/revision confirmation.", "dedupe_for_aggregate": true, "do_not_count_as_new_case": false, "drawdown_after_peak_pct": -42.15, "entry_date": "2024-08-16", "entry_price": 21550, "evidence_family": "naval_defense_engine_export_backlog_customer_order_stage2_route", "evidence_url_pending": false, "fine_archetype_id": "DEFENSE_SUBSYSTEM_PRIME_4B_REFRESH_GUARD", "forward_window_trading_days": 180, "independent_evidence_weight": 1.0, "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "low_date_180d": "2024-12-09", "low_price_180d": 15150, "peak_date": "2025-02-18", "peak_price": 31650, "positive_or_counterexample": "positive", "price_adjustment_status": "raw_unadjusted_marcap", "price_basis": "tradable_raw", "price_data_source": "Songdaiki/stock-web", "profile_path": "atlas/symbol_profiles/077/077970.json", "raw_component_score_breakdown": {"customer_financing_visibility": 5, "delivery_capacity_bridge": 7, "export_framework_backlog": 8, "information_confidence": 4, "margin_revision_bridge": 6, "market_mispricing": 8, "signed_tranche_visibility": 6, "total": 50, "valuation_rerating_runway": 6}, "reuse_reason": null, "same_entry_group_id": "C03_077970_STXENGINE_20240816_NAVAL_DEFENSE_ENGINE_BACKLOG_STAGE2", "schema_version": "v12_no_repeat_standalone_trigger_row_v1", "selected_round": "R1", "source_proxy_only": false, "stage2_evidence_fields": ["defense_export_framework_or_subsystem_backlog_attention", "signed_tranche_customer_order_or_subsystem_allocation_visibility", "delivery_capacity_margin_revision_route"], "stage3_evidence_fields": ["signed_tranche_order_duration_and_customer_financing_required", "delivery_schedule_localization_offset_or_subsystem_acceptance_required", "capacity_input_cost_margin_revision_bridge_required"], "stage4b_evidence_fields": ["defense_export_framework_or_subsystem_price_premium", "valuation_or_positioning_overheat", "post_peak_drawdown"], "stage4c_evidence_fields": ["tranche_financing_or_customer_order_delay", "delivery_acceptance_capacity_bottleneck", "margin_revision_bridge_failure"], "symbol": "077970", "tradable_shard_path": "atlas/ohlcv_tradable_by_symbol_year/077/077970/2024.csv", "trigger_date": "2024-08-16", "trigger_type": "Stage2-Actionable", "upstream_source": "FinanceData/marcap"}
```

## 9. Aggregate row

```json
{
  "calibration_usable_case_count": 3,
  "canonical_archetype_id": "C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG",
  "counterexample_count": 1,
  "current_profile_error_count": 1,
  "evidence_url_pending_count": 0,
  "fine_archetype_id": "DEFENSE_SUBSYSTEM_PRIME_4B_REFRESH_GUARD",
  "hard_duplicate_avoided": true,
  "index_update_needed": true,
  "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID",
  "loop_contribution_label": "defense_export_framework_prime_subsystem_backlog_4b_refresh_new_dates_new_symbol",
  "new_independent_case_count": 3,
  "positive_case_count": 2,
  "reused_case_count": 0,
  "schema_version": "v12_no_repeat_standalone_aggregate_v1",
  "selected_round": "R1",
  "shadow_rule_candidate": "C03 defense export-framework rows should allow Stage2 when export/backlog evidence is backed by signed tranches, customer financing/order duration, delivery schedule, subsystem allocation, capacity and margin/revision bridge; after an export premium is already capitalized, require incremental tranche or order refresh before Green and route stale premium to local 4B.",
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
3. Add C03-specific defense export-framework / signed-tranche / subsystem allocation / delivery-capacity / margin-revision / local-4B refresh guard only as a shadow candidate until more rows exist.

Candidate rule:
- C03_STAGE2_ALLOWED_ON_SIGNED_ORDER_DELIVERY_MARGIN_BRIDGE
- C03_GREEN_REQUIRES_TRANCHE_FINANCING_DELIVERY_ACCEPTANCE_CAPACITY_REVISION
- C03_EXPORT_FRAMEWORK_PRICE_PREMIUM_LOCAL_4B_REFRESH
- C03_SUBSYSTEM_STAGE2_REQUIRES_PRIME_TO_SUBSYSTEM_ALLOCATION_BRIDGE

Do not lower global Stage3 Green thresholds.
Do not treat this single MD as production-ready.
```

## 11. Final contribution line

This loop adds 3 new independent cases, 1 counterexample, and 1 current-profile residual error for R1/L1_INDUSTRIALS_INFRA_DEFENSE_GRID/C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG.

