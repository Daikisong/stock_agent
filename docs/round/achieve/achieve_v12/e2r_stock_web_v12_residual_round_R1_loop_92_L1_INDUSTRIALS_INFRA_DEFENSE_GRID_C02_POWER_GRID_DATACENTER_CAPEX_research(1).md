# E2R v12 residual research — R1 loop 92 — L1 C02 POWER GRID / DATACENTER CAPEX

```yaml
schema_family: v12_sector_archetype_residual
mode: historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12
research_session: post_calibrated_sector_archetype_residual_research
selected_round: R1
selected_loop: 92
large_sector_id: L1_INDUSTRIALS_INFRA_DEFENSE_GRID
canonical_archetype_id: C02_POWER_GRID_DATACENTER_CAPEX
fine_archetype_id: TRANSFORMER_DATACENTER_CAPEX_ORDER_MARGIN_BRIDGE_VS_PRICE_ONLY_LATE_EXTENSION
selected_priority_bucket: Priority 0
selection_basis: docs/core/V12_Research_No_Repeat_Index.md
loop_objective:
  - coverage_gap_fill
  - counterexample_mining
  - stage2_actionable_bonus_stress_test
  - 4B_non_price_requirement_stress_test
  - local_vs_full_4B_timing_test
production_scoring_changed: false
shadow_weight_only: true
stock_agent_code_accessed: false
stock_agent_code_patch_written: false
price_source: Songdaiki/stock-web
price_basis: tradable_raw
price_adjustment_status: raw_unadjusted_marcap
manifest_max_date: 2026-02-20
evidence_url_policy: source_proxy_only_until_exact_url_verified
```

## 1. Selection and novelty check

`V12_Research_No_Repeat_Index.md` still marks `C02_POWER_GRID_DATACENTER_CAPEX` as a thin Priority 0 bucket: 24 rows, 6 rows short of the 30-row minimum stability zone.
This loop therefore targets **power-grid / transformer / switchgear / datacenter CAPEX** cases where the market is trying to decide whether a theme headline has become a real backlog-and-margin bridge.

Prior registry inspection shows existing C02 files through `R1 loop 91`; therefore the selected identifier for this run is:

```text
output_file = e2r_stock_web_v12_residual_round_R1_loop_92_L1_INDUSTRIALS_INFRA_DEFENSE_GRID_C02_POWER_GRID_DATACENTER_CAPEX_research.md
```

Hard duplicate gate:

```text
duplicate_key = canonical_archetype_id + symbol + trigger_type + entry_date
result = pass
reason = new trigger-family/date combinations; one same-symbol reuse is intentionally a later price-only extension red-team path
```

## 2. Price-source validation

The price source is `Songdaiki/stock-web`, calibration shard root `atlas/ohlcv_tradable_by_symbol_year`, with raw/unadjusted `FinanceData/marcap` rows filtered into tradable shards.

```text
source_name = FinanceData/marcap
price_basis = tradable_raw
price_adjustment_status = raw_unadjusted_marcap
calibration_shard_root = atlas/ohlcv_tradable_by_symbol_year
MFE_N_pct = (max high from entry_date through N tradable rows / entry_price - 1) * 100
MAE_N_pct = (min low from entry_date through N tradable rows / entry_price - 1) * 100
```

Corporate-action caveat:

```text
- 267260 has historical corporate-action candidates before the 2024 sample window.
- 010120 has old corporate-action candidates outside the 2024 sample window.
- 103590 has a corporate-action candidate dated 2024-02-13, so the 2024-03-18 sample is used after that window; exact batch validation should still keep the corporate-action blocker active if the tool flags the forward window.
- 298040 has no corporate-action candidate in the profile.
```

## 3. Research thesis

C02 should not reward “electric equipment went up” as a standalone reason.
The rule should behave like a circuit breaker board:

```text
transformer/datacenter CAPEX headline
  -> order/backlog confirmation
  -> production capacity or delivery visibility
  -> ASP / margin / operating leverage bridge
  -> revision or FCF bridge
  -> Stage3-Green candidate
```

If the path stops at **price strength + theme label**, the candidate should stay at Yellow/4B-watch. If the entry is after a near-vertical move and no fresh non-price bridge is available, the correct state is not “new Green”; it is **local 4B event-cap / late-extension guard**.

## 4. Case table

| case_id | symbol | name | trigger | entry | entry_price | path | MFE_30 | MAE_30 | MFE_90 | MAE_90 | MFE_180 | MAE_180 |
|---|---:|---|---|---|---:|---|---:|---:|---:|---:|---:|---:|
| C02_267260_2024-02-20_GRID_CAPEX_BACKLOG_POSITIVE | 267260 | HD현대일렉트릭 | transformer backlog / export grid CAPEX bridge | 2024-02-20 | 134400 | positive | 41.74 | -12.65 | 140.7 | -12.65 | 178.65 | -12.65 |
| C02_010120_2024-03-05_GRID_SWITCHGEAR_POSITIVE | 010120 | LS ELECTRIC | switchgear/datacenter CAPEX bridge | 2024-03-05 | 77800 | positive | 102.7 | -9.0 | 213.62 | -9.0 | 213.62 | -9.0 |
| C02_298040_2024-03-04_GRID_TRANSFORMER_CAPACITY_POSITIVE | 298040 | 효성중공업 | transformer capacity / order margin bridge | 2024-03-04 | 222500 | positive-high-MAE | 60.45 | -12.36 | 110.79 | -12.36 | 110.79 | -12.36 |
| C02_103590_2024-03-18_CABLE_GRID_ORDER_BRIDGE_POSITIVE | 103590 | 일진전기 | grid cable / transformer order bridge | 2024-03-18 | 17200 | positive-smaller-cap-beta | 42.44 | -9.48 | 75.87 | -9.48 | 75.87 | -9.48 |
| C02_267260_2024-07-24_GRID_PRICE_ONLY_LATE_EXTENSION_COUNTER | 267260 | HD현대일렉트릭 | price-only late extension after rerating | 2024-07-24 | 365500 | counterexample | 2.46 | -34.88 | 2.46 | -38.3 | 2.46 | -38.3 |

## 5. Trigger rows JSONL

```jsonl
{"MAE_180D_pct": -12.65, "MAE_30D_pct": -12.65, "MAE_90D_pct": -12.65, "MFE_180D_pct": 178.65, "MFE_30D_pct": 41.74, "MFE_90D_pct": 140.7, "canonical_archetype_id": "C02_POWER_GRID_DATACENTER_CAPEX", "case_id": "C02_267260_2024-02-20_GRID_CAPEX_BACKLOG_POSITIVE", "current_profile_result": "Stage3_Yellow_to_Green_supported", "entry_date": "2024-02-20", "entry_price": 134400, "evidence_family": "transformer_backlog_export_capacity_margin_bridge", "evidence_url_status": "evidence_url_pending", "fine_archetype_id": "TRANSFORMER_DATACENTER_CAPEX_ORDER_MARGIN_BRIDGE_VS_PRICE_ONLY_LATE_EXTENSION", "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "name": "HD현대일렉트릭", "path_label": "positive", "price_adjustment_status": "raw_unadjusted_marcap", "price_basis": "tradable_raw", "price_source": "Songdaiki/stock-web", "residual_error_type": "none_price_path_supported_bridge_but_url_pending", "row_type": "trigger", "source_quality": "source_proxy_only", "symbol": "267260", "trigger_date": "2024-02-20", "trigger_type": "grid_transformer_backlog_margin_bridge"}
{"MAE_180D_pct": -9.0, "MAE_30D_pct": -9.0, "MAE_90D_pct": -9.0, "MFE_180D_pct": 213.62, "MFE_30D_pct": 102.7, "MFE_90D_pct": 213.62, "canonical_archetype_id": "C02_POWER_GRID_DATACENTER_CAPEX", "case_id": "C02_010120_2024-03-05_GRID_SWITCHGEAR_POSITIVE", "current_profile_result": "Stage3_Yellow_supported_green_if_margin_revision_present", "entry_date": "2024-03-05", "entry_price": 77800, "evidence_family": "switchgear_datacenter_us_capex_order_margin_bridge", "evidence_url_status": "evidence_url_pending", "fine_archetype_id": "TRANSFORMER_DATACENTER_CAPEX_ORDER_MARGIN_BRIDGE_VS_PRICE_ONLY_LATE_EXTENSION", "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "name": "LS ELECTRIC", "path_label": "positive", "price_adjustment_status": "raw_unadjusted_marcap", "price_basis": "tradable_raw", "price_source": "Songdaiki/stock-web", "residual_error_type": "none_but_requires_non_price_bridge", "row_type": "trigger", "source_quality": "source_proxy_only", "symbol": "010120", "trigger_date": "2024-03-05", "trigger_type": "switchgear_datacenter_capex_order_bridge"}
{"MAE_180D_pct": -12.36, "MAE_30D_pct": -12.36, "MAE_90D_pct": -12.36, "MFE_180D_pct": 110.79, "MFE_30D_pct": 60.45, "MFE_90D_pct": 110.79, "canonical_archetype_id": "C02_POWER_GRID_DATACENTER_CAPEX", "case_id": "C02_298040_2024-03-04_GRID_TRANSFORMER_CAPACITY_POSITIVE", "current_profile_result": "Stage3_Yellow_supported_but_high_MAE_guard_needed", "entry_date": "2024-03-04", "entry_price": 222500, "evidence_family": "us_transformer_capacity_backlog_margin_bridge", "evidence_url_status": "evidence_url_pending", "fine_archetype_id": "TRANSFORMER_DATACENTER_CAPEX_ORDER_MARGIN_BRIDGE_VS_PRICE_ONLY_LATE_EXTENSION", "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "name": "효성중공업", "path_label": "positive_high_mfe_high_mae", "price_adjustment_status": "raw_unadjusted_marcap", "price_basis": "tradable_raw", "price_source": "Songdaiki/stock-web", "residual_error_type": "high_MAE_success_entry_timing_guard", "row_type": "trigger", "source_quality": "source_proxy_only", "symbol": "298040", "trigger_date": "2024-03-04", "trigger_type": "transformer_capacity_order_margin_bridge"}
{"MAE_180D_pct": -9.48, "MAE_30D_pct": -9.48, "MAE_90D_pct": -9.48, "MFE_180D_pct": 75.87, "MFE_30D_pct": 42.44, "MFE_90D_pct": 75.87, "canonical_archetype_id": "C02_POWER_GRID_DATACENTER_CAPEX", "case_id": "C02_103590_2024-03-18_CABLE_GRID_ORDER_BRIDGE_POSITIVE", "current_profile_result": "Stage2_to_Yellow_supported_if_order_visibility_present", "entry_date": "2024-03-18", "entry_price": 17200, "evidence_family": "grid_cable_transformer_order_margin_bridge", "evidence_url_status": "evidence_url_pending", "fine_archetype_id": "TRANSFORMER_DATACENTER_CAPEX_ORDER_MARGIN_BRIDGE_VS_PRICE_ONLY_LATE_EXTENSION", "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "name": "일진전기", "path_label": "positive_smaller_cap_beta", "price_adjustment_status": "raw_unadjusted_marcap", "price_basis": "tradable_raw", "price_source": "Songdaiki/stock-web", "residual_error_type": "needs_url_verified_order_bridge_to_avoid_theme_beta", "row_type": "trigger", "source_quality": "source_proxy_only", "symbol": "103590", "trigger_date": "2024-03-18", "trigger_type": "grid_cable_transformer_order_bridge"}
{"MAE_180D_pct": -38.3, "MAE_30D_pct": -34.88, "MAE_90D_pct": -38.3, "MFE_180D_pct": 2.46, "MFE_30D_pct": 2.46, "MFE_90D_pct": 2.46, "canonical_archetype_id": "C02_POWER_GRID_DATACENTER_CAPEX", "case_id": "C02_267260_2024-07-24_GRID_PRICE_ONLY_LATE_EXTENSION_COUNTER", "current_profile_result": "should_be_4B_watch_or_event_cap_not_new_Green", "entry_date": "2024-07-24", "entry_price": 365500, "evidence_family": "price_only_late_extension_without_fresh_order_margin_bridge", "evidence_url_status": "evidence_url_pending", "fine_archetype_id": "TRANSFORMER_DATACENTER_CAPEX_ORDER_MARGIN_BRIDGE_VS_PRICE_ONLY_LATE_EXTENSION", "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "name": "HD현대일렉트릭", "path_label": "counterexample_price_only_late_extension", "price_adjustment_status": "raw_unadjusted_marcap", "price_basis": "tradable_raw", "price_source": "Songdaiki/stock-web", "residual_error_type": "false_positive_if_price_momentum_overrides_bridge_requirement", "reuse_reason": "same symbol reused with a new trigger family and later entry date to test 4B/local-vs-full-window split", "row_type": "trigger", "source_quality": "source_proxy_only", "symbol": "267260", "trigger_date": "2024-07-24", "trigger_type": "late_price_only_grid_equipment_extension"}
```

## 6. Stage / profile stress test

### 6.1 Positive bridge behavior

For the early 2024 transformer/switchgear cases, price action confirms that the sector was not only a theme burst. HD현대일렉트릭, LS ELECTRIC, 효성중공업, and 일진전기 all produced large forward MFE after the first credible grid-CAPEX/backlog bridge window.

However, the common mechanism is not “electric equipment label.” It is:

```text
visible global grid bottleneck
+ transformer/switchgear delivery scarcity
+ order/backlog visibility
+ ASP or margin bridge
+ revision / operating leverage
```

This supports a C02-specific **Stage2-to-Yellow acceleration** only when at least two non-price bridge legs are present.

### 6.2 Counterexample behavior

The late HD현대일렉트릭 2024-07-24 entry deliberately reuses the same symbol with a different trigger family. The price path shows why C02 needs a late-extension guard:

```text
entry = 365500
max high through sampled forward window = 374500
subsequent low through sampled window = 225500
MFE_90D ≈ +2.46%
MAE_90D ≈ -38.3%
```

That is not a fresh Green signal. It is the market stretching the same bridge after most of the rerating has already been paid. The correct state should be local 4B watch / event-cap unless fresh backlog, capacity expansion, or margin revision evidence appears after the late entry.

## 7. Shadow rule candidate

```json
{
  "row_type": "shadow_weight",
  "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID",
  "canonical_archetype_id": "C02_POWER_GRID_DATACENTER_CAPEX",
  "fine_archetype_id": "TRANSFORMER_DATACENTER_CAPEX_ORDER_MARGIN_BRIDGE_VS_PRICE_ONLY_LATE_EXTENSION",
  "patch_axis": "stage2_required_bridge_and_late_extension_guard",
  "recommended_action": "hold_for_more_url_verified_evidence",
  "candidate_rule": {
    "stage2_to_yellow_bonus": {
      "require_any_two": [
        "signed_or_disclosed_order_backlog",
        "transformer_or_switchgear_capacity_delivery_visibility",
        "ASP_or_margin_revision_bridge",
        "customer_datacenter_or_grid_capex_source_bridge"
      ],
      "do_not_count": [
        "price_momentum_only",
        "sector ETF or peer beta only",
        "generic AI/datacenter headline without company-specific order bridge"
      ]
    },
    "late_extension_guard": {
      "if_prior_90D_price_runup_pct_greater_than": 80,
      "and_no_new_non_price_bridge_after_entry": true,
      "then_stage_cap": "4B_watch_or_Stage3_Yellow_max",
      "block_new_green": true
    }
  },
  "reason": "C02 positives were strong when backlog/order/capacity/margin bridge existed, but late price-only extension produced poor asymmetry."
}
```

## 8. Residual contribution summary

```json
{
  "row_type": "residual_contribution",
  "canonical_archetype_id": "C02_POWER_GRID_DATACENTER_CAPEX",
  "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID",
  "positive_case_count": 4,
  "counterexample_case_count": 1,
  "residual_error_found": true,
  "residual_error_type": [
    "late_price_only_extension_false_positive",
    "high_MAE_success_entry_timing_guard",
    "source_proxy_only_url_pending"
  ],
  "promotion_readiness": "not_ready_until_exact_url_verified",
  "suggested_next_evidence_work": [
    "verify exact order/backlog disclosures for 267260, 010120, 298040, 103590",
    "separate transformer/switchgear backlog bridge from generic AI datacenter label",
    "mine additional counterexamples in backup power, low-voltage apparatus, and cable subthemes"
  ]
}
```

## 9. Validation scope

```text
validated_price_rows = true
validated_source_repo = Songdaiki/stock-web
validated_price_basis = tradable_raw
validated_adjustment_status = raw_unadjusted_marcap
validated_manifest_max_date = 2026-02-20
validated_forward_window_policy = approximate_manual_from_visible_stock_web_rows
exact_non_price_url_validation = false
evidence_url_pending = true
source_proxy_only = true
production_patch_ready = false
shadow_rule_only = true
```

## 10. Deferred Coding Agent Handoff Prompt

```text
Do not apply this MD directly as a production scoring patch.

Batch-ingest this Markdown with the v12 calibration parser. Treat all trigger rows as source_proxy_only until exact evidence URLs are added. The useful patch axis is not a global Stage2 bonus. It is a C02-specific rule:

1. For C02_POWER_GRID_DATACENTER_CAPEX, allow Stage2-to-Yellow acceleration only when at least two non-price bridge legs exist:
   - order/backlog
   - capacity/delivery visibility
   - ASP/margin/revision bridge
   - explicit customer grid/datacenter CAPEX source bridge

2. Add/validate a late-extension guard:
   - if prior 90D price runup is already extreme and there is no fresh non-price bridge after entry, cap state at 4B-watch or Stage3-Yellow, not new Green.

3. Keep source_proxy_only rows blocked from automatic promotion until exact URLs are added.
```

## 11. Next research state

```text
completed_round = R1
completed_loop = 92
selection_basis = docs/core/V12_Research_No_Repeat_Index.md
selected_priority_bucket = Priority 0
selected_canonical_archetype_id = C02_POWER_GRID_DATACENTER_CAPEX
next_recommended_archetypes = C19_BRAND_RETAIL_INVENTORY_MARGIN, C27_CONTENT_IP_GLOBAL_MONETIZATION, C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK, C13_BATTERY_JV_UTILIZATION_AMPC_IRA, C24_BIO_TRIAL_DATA_EVENT_RISK, C28_SOFTWARE_SECURITY_CONTRACT_RETENTION
round_schedule_status = coverage_index_selected
round_sector_consistency = pass
```
