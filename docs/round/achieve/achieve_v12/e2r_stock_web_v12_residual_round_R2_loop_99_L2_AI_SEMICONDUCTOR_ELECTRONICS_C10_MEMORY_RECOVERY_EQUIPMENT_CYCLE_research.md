# E2R Stock-Web v12 Residual Research — R2 loop 99 / L2 / C10

```yaml
schema_family: v12_sector_archetype_residual
selected_round: R2
selected_loop: 99
large_sector_id: L2_AI_SEMICONDUCTOR_ELECTRONICS
canonical_archetype_id: C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE
fine_archetype_id: MEMORY_RECOVERY_EQUIPMENT_ORDER_CONVERSION_VS_GENERIC_MEMORY_BETA
loop_objective:
  - coverage_gap_fill
  - counterexample_mining
  - stage2_actionable_bonus_stress_test
  - 4B_non_price_requirement_stress_test
  - canonical_archetype_compression
selection_basis: docs/core/V12_Research_No_Repeat_Index.md
selected_priority_bucket: Priority 0
production_scoring_changed: false
shadow_weight_only: true
stock_agent_code_accessed: false
stock_agent_code_patch_written: false
price_atlas_repo: Songdaiki/stock-web
price_source: FinanceData/marcap
price_basis: tradable_raw
price_adjustment_status: raw_unadjusted_marcap
manifest_max_date: 2026-02-20
evidence_url_status: evidence_url_pending
source_quality: source_proxy_only
```

## 1. Selection and novelty check

`V12_Research_No_Repeat_Index.md` places `C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE` in Priority 0 with 21 rows, still 9 rows short of the 30-row minimum stability zone and 29 rows short of the 50-row practical calibration zone. Its investigation target is to separate broad memory recovery beta from real equipment-order conversion.

The registry check found the latest existing `C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE` file at R2 loop 98. Therefore this run is assigned:

```text
selected_round = R2
selected_loop = 99
large_sector_id = L2_AI_SEMICONDUCTOR_ELECTRONICS
canonical_archetype_id = C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE
output_file = e2r_stock_web_v12_residual_round_R2_loop_99_L2_AI_SEMICONDUCTOR_ELECTRONICS_C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE_research.md
```

Hard duplicate key checked by this run:

```text
canonical_archetype_id + symbol + trigger_type + entry_date
```

Local run-level novelty:

```text
240810 | memory_equipment_recovery_beta_without_firm_order_bridge | 2024-03-20
036930 | deposition_equipment_price_spike_before_order_revision_bridge | 2024-02-28
084370 | deposition_equipment_recovery_with_customer_ramp_bridge_proxy | 2024-03-21
319660 | process_equipment_recovery_with_order_conversion_proxy | 2024-03-21
240810 | late_cycle_rebound_without_revision_followthrough | 2024-07-04
319660 | retest_after_memory_recovery_order_bridge | 2024-06-07
```

No new production patch is applied. This is a residual research handoff MD only.

---

## 2. Price source validation

Stock-Web manifest and schema basis used by this run:

```text
source_name = FinanceData/marcap
source_repo_url = https://github.com/FinanceData/marcap
price_adjustment_status = raw_unadjusted_marcap
price_basis = tradable_raw
calibration_shard_root = atlas/ohlcv_tradable_by_symbol_year
raw_shard_root = atlas/ohlcv_raw_by_symbol_year
manifest_max_date = 2026-02-20
tradable_row_count = 14,354,401
symbol_count = 5,414
```

Schema formula used:

```text
MFE_N_pct = (max high from entry_date through N tradable rows / entry_price - 1) * 100
MAE_N_pct = (min low from entry_date through N tradable rows / entry_price - 1) * 100
```

Calibration caveat:

```text
All rows are raw/unadjusted marcap OHLC.
Corporate-action candidate windows are blocked by default.
The selected 2024 windows are not near each selected symbol's listed corporate-action candidate dates in the profile files.
```

---

## 3. Research hypothesis

C10 is not a generic semiconductor momentum label.

The correct mechanism is:

```text
memory price / capex recovery
  -> customer equipment order or shipment acceptance
  -> utilization / revenue conversion
  -> revision or margin bridge
  -> durable Stage2 or Yellow/Green candidate
```

The common false mechanism is:

```text
memory index rebounds
  -> equipment basket price spike
  -> no order/revision bridge
  -> 4B local spike or late-chase entry
  -> high MAE / poor 90D-180D asymmetry
```

This loop therefore tests whether C10 should require a stricter `order_conversion_bridge` before granting Stage2 actionable support.

---

## 4. Case ledger

### Case A — 240810 원익IPS: memory recovery beta without durable order bridge

Observed price path:

```text
2024-03-20 close/entry = 37,400
observed peak high = 44,850 on 2024-04-08
observed trough low = 26,950 on 2024-10-25
MFE_180D ≈ +19.9%
MAE_180D ≈ -27.9%
```

Interpretation:

The initial memory-equipment rebound created a valid short-lived MFE, but the path later behaved like a weak bridge case. A positive 30D burst did not protect the 180D path. This is the archetypal C10 trap: the market hears “memory recovery” while the score engine needs actual equipment order/revision conversion.

Classification:

```text
positive_or_counterexample = counterexample
current_profile_error = residual_false_positive_risk
suggested_guardrail = require_order_or_revision_bridge_before_stage2_bonus
```

### Case B — 036930 주성엔지니어링: ALD/deposition spike with poor follow-through

Observed price path:

```text
2024-02-28 close/entry = 40,000
observed peak high = 41,450 on 2024-04-08
observed trough low = 30,650 on 2024-07-18
MFE_180D ≈ +3.6%
MAE_180D ≈ -23.4%
```

Interpretation:

The price action had a strong one-day equipment spike, but post-entry asymmetry was poor. This is useful because the symbol fits the memory-equipment universe, yet the specific trigger did not show the order/revision bridge required for durable C10 rerating.

Classification:

```text
positive_or_counterexample = counterexample
current_profile_error = stage2_false_positive_or_yellow_cap_candidate
suggested_guardrail = cap_generic_memory_equipment_spike_at_stage2_watch_without_order_bridge
```

### Case C — 084370 유진테크: positive C10 path with high volatility

Observed price path:

```text
2024-03-21 close/entry = 41,450
observed peak high = 60,000 on 2024-05-28
observed trough low = 37,400 on 2024-03-21
MFE_180D ≈ +44.8%
MAE_180D ≈ -9.8%
```

Interpretation:

This is the positive side of C10. The same memory-recovery backdrop works when it is tied to equipment-order conversion proxies and not merely beta. The path still has drawdown, so it supports Stage2/Yellow more than automatic Green.

Classification:

```text
positive_or_counterexample = positive
current_profile_error = none_or_minor_yellow_timing
suggested_rule = allow_stage2_bonus_when_order_bridge_and_revision_proxy_coexist
```

### Case D — 319660 피에스케이: dry strip / process equipment recovery with better asymmetry

Observed price path:

```text
2024-03-21 close/entry = 29,300
observed peak high = 39,100 on 2024-07-11
observed trough low = 27,750 on 2024-03-25
MFE_180D ≈ +33.4%
MAE_180D ≈ -6.1%
```

Interpretation:

This is the cleaner C10 positive candidate in the sample. The price path gives enough MFE before major adverse drift, and the MAE is structurally tolerable compared with 240810 and 036930. The case argues that C10 should not be blocked globally; it should be bridge-gated.

Classification:

```text
positive_or_counterexample = positive
current_profile_error = possible_lateness_if_yellow_only
suggested_rule = stage2_bonus_candidate_delta_when_memory_recovery_plus_order_conversion_bridge
```

### Case E — 240810 원익IPS late retest: 4B/late-chase trap

Observed price path:

```text
2024-07-04 close/entry = 40,100
observed peak high = 40,300 on 2024-07-05
observed trough low = 26,950 on 2024-10-25
MFE_180D ≈ +0.5%
MAE_180D ≈ -32.8%
```

Interpretation:

The same ticker can produce both an early short-lived MFE and a later high-MAE trap. For C10, this means relative strength after a prior failed bridge should be treated as a 4B/late-chase risk unless a fresh order or revision event resets the thesis.

Classification:

```text
positive_or_counterexample = counterexample
current_profile_error = high_mae_late_chase
suggested_guardrail = if_same_symbol_prior_bridge_failed_then_require_fresh_order_or_revision_reset
```

### Case F — 319660 피에스케이 retest: acceptable secondary trigger

Observed price path:

```text
2024-06-07 close/entry = 33,500
observed peak high = 39,100 on 2024-07-11
observed trough low = 32,300 on 2024-06-25
MFE_180D ≈ +16.7%
MAE_180D ≈ -6.0%
```

Interpretation:

This secondary trigger behaves differently from the late 240810 rebound. Retest triggers can still be useful when the prior base already has a healthier order-conversion profile. This argues for a positive C10 exception, not a broad retest ban.

Classification:

```text
positive_or_counterexample = positive
current_profile_error = none
suggested_rule = allow_retest_if_prior_positive_asymmetry_and_bridge_proxy_remain_intact
```

---

## 5. Trigger rows JSONL

```jsonl
{"row_type": "trigger", "schema_family": "v12_sector_archetype_residual", "selected_round": "R2", "selected_loop": 99, "large_sector_id": "L2_AI_SEMICONDUCTOR_ELECTRONICS", "canonical_archetype_id": "C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE", "fine_archetype_id": "WAFER_PROCESS_MEMORY_RECOVERY_EQUIPMENT_ORDER_CONVERSION_VS_GENERIC_MEMORY_BETA", "symbol": "240810", "name": "원익IPS", "trigger_date": "2024-03-20", "entry_date": "2024-03-20", "entry_price": 37400, "trigger_type": "memory_equipment_recovery_beta_without_firm_order_bridge", "price_source": "Songdaiki/stock-web", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "mfe_30d_pct": 19.9, "mae_30d_pct": -8.3, "mfe_90d_pct": 19.9, "mae_90d_pct": -10.6, "mfe_180d_pct": 19.9, "mae_180d_pct": -27.9, "peak_date_observed": "2024-04-08", "peak_high_observed": 44850, "trough_date_observed": "2024-10-25", "trough_low_observed": 26950, "current_profile_outcome_label": "residual_false_positive_risk", "evidence_url_status": "evidence_url_pending", "source_quality": "source_proxy_only", "duplicate_key": "C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE|240810|memory_equipment_recovery_beta_without_firm_order_bridge|2024-03-20"}
{"row_type": "trigger", "schema_family": "v12_sector_archetype_residual", "selected_round": "R2", "selected_loop": 99, "large_sector_id": "L2_AI_SEMICONDUCTOR_ELECTRONICS", "canonical_archetype_id": "C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE", "fine_archetype_id": "ALD_DEPOSITION_MEMORY_RECOVERY_ORDER_CONVERSION_VS_CYCLE_SPIKE", "symbol": "036930", "name": "주성엔지니어링", "trigger_date": "2024-02-28", "entry_date": "2024-02-28", "entry_price": 40000, "trigger_type": "deposition_equipment_price_spike_before_order_revision_bridge", "price_source": "Songdaiki/stock-web", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "mfe_30d_pct": 3.6, "mae_30d_pct": -16.6, "mfe_90d_pct": 3.6, "mae_90d_pct": -21.3, "mfe_180d_pct": 3.6, "mae_180d_pct": -23.4, "peak_date_observed": "2024-04-08", "peak_high_observed": 41450, "trough_date_observed": "2024-07-18", "trough_low_observed": 30650, "current_profile_outcome_label": "stage2_false_positive_or_yellow_cap_candidate", "evidence_url_status": "evidence_url_pending", "source_quality": "source_proxy_only", "duplicate_key": "C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE|036930|deposition_equipment_price_spike_before_order_revision_bridge|2024-02-28"}
{"row_type": "trigger", "schema_family": "v12_sector_archetype_residual", "selected_round": "R2", "selected_loop": 99, "large_sector_id": "L2_AI_SEMICONDUCTOR_ELECTRONICS", "canonical_archetype_id": "C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE", "fine_archetype_id": "LPCVD_DEPOSITION_MEMORY_RECOVERY_ORDER_REVISION_BRIDGE", "symbol": "084370", "name": "유진테크", "trigger_date": "2024-03-21", "entry_date": "2024-03-21", "entry_price": 41450, "trigger_type": "deposition_equipment_recovery_with_customer_ramp_bridge_proxy", "price_source": "Songdaiki/stock-web", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "mfe_30d_pct": 36.6, "mae_30d_pct": -9.8, "mfe_90d_pct": 44.8, "mae_90d_pct": -9.8, "mfe_180d_pct": 44.8, "mae_180d_pct": -9.8, "peak_date_observed": "2024-05-28", "peak_high_observed": 60000, "trough_date_observed": "2024-03-21", "trough_low_observed": 37400, "current_profile_outcome_label": "positive_but_high_volatility", "evidence_url_status": "evidence_url_pending", "source_quality": "source_proxy_only", "duplicate_key": "C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE|084370|deposition_equipment_recovery_with_customer_ramp_bridge_proxy|2024-03-21"}
{"row_type": "trigger", "schema_family": "v12_sector_archetype_residual", "selected_round": "R2", "selected_loop": 99, "large_sector_id": "L2_AI_SEMICONDUCTOR_ELECTRONICS", "canonical_archetype_id": "C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE", "fine_archetype_id": "DRY_STRIP_ETCH_MEMORY_RECOVERY_EQUIPMENT_ORDER_CONVERSION", "symbol": "319660", "name": "피에스케이", "trigger_date": "2024-03-21", "entry_date": "2024-03-21", "entry_price": 29300, "trigger_type": "process_equipment_recovery_with_order_conversion_proxy", "price_source": "Songdaiki/stock-web", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "mfe_30d_pct": 14.3, "mae_30d_pct": -5.3, "mfe_90d_pct": 24.9, "mae_90d_pct": -6.1, "mfe_180d_pct": 33.4, "mae_180d_pct": -6.1, "peak_date_observed": "2024-07-11", "peak_high_observed": 39100, "trough_date_observed": "2024-03-25", "trough_low_observed": 27750, "current_profile_outcome_label": "positive_c10_order_bridge_candidate", "evidence_url_status": "evidence_url_pending", "source_quality": "source_proxy_only", "duplicate_key": "C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE|319660|process_equipment_recovery_with_order_conversion_proxy|2024-03-21"}
{"row_type": "trigger", "schema_family": "v12_sector_archetype_residual", "selected_round": "R2", "selected_loop": 99, "large_sector_id": "L2_AI_SEMICONDUCTOR_ELECTRONICS", "canonical_archetype_id": "C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE", "fine_archetype_id": "WAFER_PROCESS_MEMORY_RECOVERY_EQUIPMENT_LATE_CHASE_HIGH_MAE", "symbol": "240810", "name": "원익IPS", "trigger_date": "2024-07-04", "entry_date": "2024-07-04", "entry_price": 40100, "trigger_type": "late_cycle_rebound_without_revision_followthrough", "price_source": "Songdaiki/stock-web", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "mfe_30d_pct": 0.5, "mae_30d_pct": -25.6, "mfe_90d_pct": 0.5, "mae_90d_pct": -31.0, "mfe_180d_pct": 0.5, "mae_180d_pct": -32.8, "peak_date_observed": "2024-07-05", "peak_high_observed": 40300, "trough_date_observed": "2024-10-25", "trough_low_observed": 26950, "current_profile_outcome_label": "late_chase_high_mae_counterexample", "evidence_url_status": "evidence_url_pending", "source_quality": "source_proxy_only", "duplicate_key": "C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE|240810|late_cycle_rebound_without_revision_followthrough|2024-07-04"}
{"row_type": "trigger", "schema_family": "v12_sector_archetype_residual", "selected_round": "R2", "selected_loop": 99, "large_sector_id": "L2_AI_SEMICONDUCTOR_ELECTRONICS", "canonical_archetype_id": "C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE", "fine_archetype_id": "DRY_STRIP_ETCH_MEMORY_RECOVERY_STAGE2_RETEST", "symbol": "319660", "name": "피에스케이", "trigger_date": "2024-06-07", "entry_date": "2024-06-07", "entry_price": 33500, "trigger_type": "retest_after_memory_recovery_order_bridge", "price_source": "Songdaiki/stock-web", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "mfe_30d_pct": 16.7, "mae_30d_pct": -3.6, "mfe_90d_pct": 16.7, "mae_90d_pct": -6.0, "mfe_180d_pct": 16.7, "mae_180d_pct": -6.0, "peak_date_observed": "2024-07-11", "peak_high_observed": 39100, "trough_date_observed": "2024-06-25", "trough_low_observed": 32300, "current_profile_outcome_label": "secondary_positive_retest", "evidence_url_status": "evidence_url_pending", "source_quality": "source_proxy_only", "duplicate_key": "C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE|319660|retest_after_memory_recovery_order_bridge|2024-06-07"}
```

---

## 6. Aggregate metrics

```json
{
  "row_type": "aggregate_metric",
  "schema_family": "v12_sector_archetype_residual",
  "selected_round": "R2",
  "selected_loop": 99,
  "large_sector_id": "L2_AI_SEMICONDUCTOR_ELECTRONICS",
  "canonical_archetype_id": "C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE",
  "trigger_row_count": 6,
  "unique_symbol_count": 4,
  "positive_count": 3,
  "counterexample_count": 3,
  "median_mfe_90d_pct": 18.3,
  "median_mae_90d_pct": -8.0,
  "high_mae_counterexample_count": 3,
  "best_positive_symbol": "084370",
  "worst_counterexample_symbol": "240810",
  "production_scoring_changed": false,
  "shadow_weight_only": true
}
```

---

## 7. Score-return alignment

### Alignment found

```text
If memory recovery label + actual order/revision bridge:
    score_return_alignment improves
    examples: 084370, 319660
```

### Misalignment found

```text
If memory recovery label only, or late retest without fresh bridge:
    local MFE may appear
    90D/180D MAE can dominate
    examples: 240810, 036930
```

### Practical scoring implication

C10 should not receive a simple memory-cycle beta bonus. It should be a bridge-gated archetype.

Potential scoring features to test later:

```text
c10_order_conversion_bridge_present
c10_customer_capex_or_delivery_acceptance_present
c10_revision_or_margin_bridge_present
c10_prior_failed_bridge_same_symbol
c10_late_retest_without_fresh_order_reset
```

---

## 8. Current calibrated profile stress test

The current calibrated profile already blocks many price-only moves globally, but C10 has a specific residual problem:

```text
A price-only or memory-beta trigger can look like an early Stage2 in the first 30D window.
The same trigger can become a high-MAE 90D/180D case if equipment-order conversion is not visible.
```

Stress-test result:

```text
C10 global Stage2 bonus should be narrowed.
C10 positive treatment should require at least one non-price bridge:
  - customer equipment order
  - shipment/delivery acceptance
  - memory capex order conversion
  - revenue or revision bridge
```

Suggested shadow patch axis:

```json
{
  "row_type": "shadow_weight",
  "patch_axis": "stage2_required_bridge",
  "scope": "C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE",
  "condition": "memory_recovery_label_present AND NOT(order_conversion_bridge OR revision_bridge OR delivery_acceptance_proxy)",
  "effect": "cap at Stage2-watch or Yellow-watch; do not promote to Stage3-Green from price action alone",
  "promotion_readiness": "hold_for_more_url_verified_evidence"
}
```

Suggested positive exception:

```json
{
  "row_type": "shadow_weight",
  "patch_axis": "stage2_bonus_candidate_delta",
  "scope": "C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE",
  "condition": "order_conversion_bridge AND revision_or_margin_bridge AND 30D_MFE_to_MAE_asymmetry_positive",
  "effect": "+1 to +2 Stage2 actionable bridge score candidate; no automatic Green",
  "promotion_readiness": "hold_for_more_url_verified_evidence"
}
```

Suggested 4B guardrail:

```json
{
  "row_type": "shadow_weight",
  "patch_axis": "local_4b_watch_guard",
  "scope": "C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE",
  "condition": "late_retest_after_prior_failed_bridge AND no_fresh_order_or_revision_reset",
  "effect": "prefer 4B-watch / high-MAE warning over fresh Stage2",
  "promotion_readiness": "hold_for_more_counterexamples"
}
```

---

## 9. Residual contribution summary

```json
{
  "row_type": "residual_contribution",
  "selected_round": "R2",
  "selected_loop": 99,
  "large_sector_id": "L2_AI_SEMICONDUCTOR_ELECTRONICS",
  "canonical_archetype_id": "C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE",
  "contribution_label": "canonical_archetype_rule_candidate",
  "what_this_adds": [
    "Separates memory-equipment order conversion from generic memory beta.",
    "Adds C10-specific high-MAE counterexamples for late retests.",
    "Shows positive C10 path remains useful when order/revision bridge is present.",
    "Suggests stage2_required_bridge and local_4B_watch_guard axes for C10 only."
  ],
  "do_not_promote_yet_reason": "source_proxy_only and evidence_url_pending; exact non-price evidence URLs must be attached before production promotion."
}
```

---

## 10. Validation scope

```text
validation_scope = historical_trigger_level_calibration
current_live_stock_discovery = false
stock_agent_code_accessed = false
stock_agent_code_patch_written = false
brokerage_or_autotrading = false
price_source = Songdaiki/stock-web
price_basis = tradable_raw
adjustment_status = raw_unadjusted_marcap
forward_window_basis = manifest max_date 2026-02-20
production_scoring_changed = false
```

Limitations:

```text
- Non-price evidence is source_proxy_only.
- Exact order/revision/disclosure/report URLs were not verified in this run.
- Therefore all suggested scoring changes are shadow-only and should be held until URL-verified evidence rows exist.
```

---

## 11. Deferred Coding Agent Handoff Prompt

Do not execute this now.

```text
You are the later batch implementation agent for stock_agent.

Read this MD as one C10 residual calibration artifact only.
Do not treat it as a production patch by itself.

Tasks:
1. Ingest the JSONL trigger rows if schema-compatible.
2. Validate duplicate keys:
   canonical_archetype_id + symbol + trigger_type + entry_date.
3. Recompute MFE/MAE from Songdaiki/stock-web tradable_raw OHLC.
4. Attach exact non-price evidence URLs for each trigger before promotion.
5. Test a C10 scoped stage2_required_bridge rule:
   memory_recovery_label_present but no order_conversion_bridge/revision_bridge => cap Stage2/Yellow.
6. Test a C10 scoped positive exception:
   order_conversion_bridge + revision_or_margin_bridge + positive MFE/MAE asymmetry => limited Stage2 bonus.
7. Test a C10 scoped local_4B_watch_guard:
   late retest after prior failed bridge without fresh order reset => 4B-watch/high-MAE warning.
8. Do not modify global Stage2 or Green thresholds based on this single MD.
```

---

## 12. Next research state

```text
completed_round = R2
completed_loop = 99
selection_basis = docs/core/V12_Research_No_Repeat_Index.md
selected_priority_bucket = Priority 0
round_schedule_status = coverage_index_selected
round_sector_consistency = pass
production_scoring_changed = false
shadow_weight_only = true
next_recommended_archetypes = C14_EV_DEMAND_SLOWDOWN_4B_4C, C11_BATTERY_ORDERBOOK_RERATING, C02_POWER_GRID_DATACENTER_CAPEX, C19_BRAND_RETAIL_INVENTORY_MARGIN, C27_CONTENT_IP_GLOBAL_MONETIZATION
```
