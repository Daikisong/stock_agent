# E2R V12 No-Repeat Standalone Residual Research
## L2 / C10 Memory Recovery Equipment Cycle — 2024 generic memory equipment recovery

metadata:
```text
selected_round: R2
scheduler_override_used: true
scheduled_round_inherited: false
large_sector_id: L2_AI_SEMICONDUCTOR_ELECTRONICS
canonical_archetype_id: C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE
fine_archetype_id: MEMORY_RECOVERY_EQUIPMENT_CYCLE_NOT_HBM_CUSTOMER_LOCK
loop_objective: coverage_gap_fill|green_strictness_stress_test|4B_non_price_requirement_stress_test|counterexample_mining
price_source: Songdaiki/stock-web
stock_web_manifest_max_date: 2026-02-20
output_file: e2r_stock_web_v12_no_repeat_standalone_L2_AI_SEMICONDUCTOR_ELECTRONICS_C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE_memory_recovery_equipment_2024_research.md
production_scoring_changed: false
shadow_weight_only: true
```

## 1. Prompt / index basis

This standalone MD follows `docs/core/e2r_v12_prompt_round_scheduler_corrected.txt` with the user-specified scheduler override.  
`V12_Research_No_Repeat_Index.md` was used only as duplicate avoidance and coverage-gap selection support.

No-Repeat Index observation:
- C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE is present in the canonical list but does not appear in the current archetype coverage table.
- This run therefore selects an under-covered R2/L2 archetype rather than repeating C06 HBM customer capacity, C07 HBM equipment order, C08 test socket quality, or C09 advanced equipment valuation blowoff.
- Hard duplicate rule checked: no selected row uses an existing `C10 + symbol + trigger_type + entry_date` key from the No-Repeat table.

## 2. Stock-Web price source check

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
240810 원익IPS: profile clean for 2024 window; corporate_action_candidate_count=0.
095610 테스: 2011/2016 corporate-action candidates only; 2024 window clean.
036930 주성엔지니어링: 2000 corporate-action candidate only; 2024 window clean.
```

## 3. Research thesis

C10 is not HBM customer-capacity proof. It is the weaker, broader mechanism:

```text
memory downturn bottoming
→ generic equipment beta / capex expectation
→ price rerating attempt
→ only becomes Green if order/backlog/revision/customer visibility closes
```

The residual question is whether generic memory equipment recovery should receive the same structural visibility treatment as HBM customer-capacity or explicit equipment-order archetypes. The 2024 cases below say no: the cycle can create strong Stage2/Yellow rallies, but without backlog/revision/customer proof it often becomes high-MAE or false-Green risk.

## 4. Case table

| case_id | symbol | role | entry | entry_price | peak | low_180d | MFE_180D | MAE_180D | post-peak DD |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|
| C10_240810_WONIKIPS_20240229_MEMORY_EQUIP_STAGE2_HIGH_MAE | 240810 | high_mae_success | 2024-02-29 | 32800 | 44850 on 2024-04-08 | 27800 on 2024-09-11 | 36.74% | -15.24% | -38.02% |
| C10_095610_TES_20240229_GENERIC_MEMORY_EQUIP_FALSE_GREEN | 095610 | failed_rerating | 2024-02-29 | 19980 | 26400 on 2024-04-02 | 15880 on 2024-09-09 | 32.13% | -20.52% | -39.85% |
| C10_036930_JUSUNG_20240228_MEMORY_RECOVERY_BETA_REVISION_GAP | 036930 | false_positive_green | 2024-02-28 | 40000 | 41450 on 2024-04-08 | 22050 on 2024-09-09 | 3.62% | -44.88% | -46.8% |

## 5. Stage evidence split

### Stage2 / Stage2-Actionable evidence
- Memory cycle bottoming and equipment beta were visible through sector-relative strength.
- Price action supported attention, especially 240810 and 095610 in late February / early April 2024.
- This is enough for Stage2-Actionable watch, not enough for Green.

### Stage3 evidence
- C10 Green should require at least one of:
  - explicit customer capacity/order/backlog bridge;
  - FY1/FY2 revision confirmation;
  - repeat equipment order visibility;
  - margin bridge from actual order conversion.
- The selected cases do not consistently close this bridge.

### 4B evidence
- 095610 and 240810 both produced sharp rallies, then gave back a large part of the move.
- 4B should be local watch unless non-price evidence shows the cycle has become durable.

### 4C evidence
- 036930 shows the clearest false-Green risk: a strong beta rally around late February / April 2024, followed by a deep 180D drawdown.
- In C10, failure is not necessarily immediate hard 4C; it is often a slow revision-gap fade.

## 6. Current calibrated profile stress test

The current calibrated profile already blocks price-only positive promotion and requires non-price evidence for full 4B. C10 adds an archetype-specific nuance:

```text
Generic memory recovery equipment beta should not inherit C06/C07 visibility credit.
C10 Stage2 can be early, but C10 Green should require order/backlog/revision closure.
If the row only has broad memory recovery + relative strength, cap the state at Stage2-Actionable or Stage3-Yellow.
```

Residual errors:
```text
current_profile_error_count = 2
- 095610: generic memory recovery beta could be over-promoted if relative strength is mistaken for visibility.
- 036930: valuation/equipment beta rally could be misread as Green without durable revision bridge.
```

## 7. Machine-readable rows

```jsonl
{"MAE_180D_pct": -15.24, "MAE_30D_pct": -2.29, "MAE_90D_pct": -2.29, "MFE_180D_pct": 36.74, "MFE_30D_pct": 36.74, "MFE_90D_pct": 36.74, "aggregate_group_role": "representative", "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "calibration_usable": true, "canonical_archetype_id": "C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE", "case_id": "C10_240810_WONIKIPS_20240229_MEMORY_EQUIP_STAGE2_HIGH_MAE", "case_role": "high_mae_success", "company_name": "원익IPS", "corporate_action_window_status": "clean_180d_by_profile", "current_profile_error": false, "current_profile_verdict": "current_profile_should_keep_stage2_actionable_not_green", "dedupe_for_aggregate": true, "do_not_count_as_new_case": false, "drawdown_after_peak_pct": -38.02, "entry_date": "2024-02-29", "entry_price": 32800, "evidence_family": "memory_equipment_cycle_recovery_without_explicit_hbm_customer_lock", "evidence_url_pending": false, "fine_archetype_id": "MEMORY_RECOVERY_EQUIPMENT_CYCLE_NOT_HBM_CUSTOMER_LOCK", "forward_window_trading_days": 180, "independent_evidence_weight": 1.0, "large_sector_id": "L2_AI_SEMICONDUCTOR_ELECTRONICS", "peak_date": "2024-04-08", "peak_price": 44850, "positive_or_counterexample": "positive", "price_adjustment_status": "raw_unadjusted_marcap", "price_basis": "tradable_raw", "price_data_source": "Songdaiki/stock-web", "reuse_reason": null, "same_entry_group_id": "C10_240810_WONIKIPS_20240229_MEMORY_EQUIP_STAGE2_HIGH_MAE", "scheduled_round": "R2", "schema_version": "v12_no_repeat_standalone_trigger_row_v1", "selected_round": "R2", "source_proxy_only": false, "stage2_evidence_fields": ["memory_downturn_bottoming", "equipment_order_expectation", "relative_strength"], "stage3_evidence_fields": ["revision_bridge_required", "customer_or_backlog_confirmation_missing_or_partial"], "stage4b_evidence_fields": ["valuation_beta_rally", "positioning_overheat", "post_peak_drawdown"], "stage4c_evidence_fields": ["revision_gap", "capex_delay_risk", "generic_cycle_fade"], "symbol": "240810", "trigger_date": "2024-02-29", "trigger_type": "Stage2-Actionable", "upstream_source": "FinanceData/marcap"}
{"MAE_180D_pct": -20.52, "MAE_30D_pct": -5.66, "MAE_90D_pct": -5.66, "MFE_180D_pct": 32.13, "MFE_30D_pct": 32.13, "MFE_90D_pct": 32.13, "aggregate_group_role": "representative", "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "calibration_usable": true, "canonical_archetype_id": "C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE", "case_id": "C10_095610_TES_20240229_GENERIC_MEMORY_EQUIP_FALSE_GREEN", "case_role": "failed_rerating", "company_name": "테스", "corporate_action_window_status": "clean_180d_by_profile", "current_profile_error": true, "current_profile_verdict": "current_profile_false_green_risk_if_generic_cycle_is_treated_as_visibility", "dedupe_for_aggregate": true, "do_not_count_as_new_case": false, "drawdown_after_peak_pct": -39.85, "entry_date": "2024-02-29", "entry_price": 19980, "evidence_family": "generic_memory_recovery_beta_without_order_backlog_revision_bridge", "evidence_url_pending": false, "fine_archetype_id": "MEMORY_RECOVERY_EQUIPMENT_CYCLE_NOT_HBM_CUSTOMER_LOCK", "forward_window_trading_days": 180, "independent_evidence_weight": 1.0, "large_sector_id": "L2_AI_SEMICONDUCTOR_ELECTRONICS", "peak_date": "2024-04-02", "peak_price": 26400, "positive_or_counterexample": "counterexample", "price_adjustment_status": "raw_unadjusted_marcap", "price_basis": "tradable_raw", "price_data_source": "Songdaiki/stock-web", "reuse_reason": null, "same_entry_group_id": "C10_095610_TES_20240229_GENERIC_MEMORY_EQUIP_FALSE_GREEN", "scheduled_round": "R2", "schema_version": "v12_no_repeat_standalone_trigger_row_v1", "selected_round": "R2", "source_proxy_only": false, "stage2_evidence_fields": ["memory_downturn_bottoming", "equipment_order_expectation", "relative_strength"], "stage3_evidence_fields": ["revision_bridge_required", "customer_or_backlog_confirmation_missing_or_partial"], "stage4b_evidence_fields": ["valuation_beta_rally", "positioning_overheat", "post_peak_drawdown"], "stage4c_evidence_fields": ["revision_gap", "capex_delay_risk", "generic_cycle_fade"], "symbol": "095610", "trigger_date": "2024-02-29", "trigger_type": "Stage2-Actionable", "upstream_source": "FinanceData/marcap"}
{"MAE_180D_pct": -44.88, "MAE_30D_pct": -16.37, "MAE_90D_pct": -16.37, "MFE_180D_pct": 3.62, "MFE_30D_pct": 3.62, "MFE_90D_pct": 3.62, "aggregate_group_role": "representative", "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "calibration_usable": true, "canonical_archetype_id": "C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE", "case_id": "C10_036930_JUSUNG_20240228_MEMORY_RECOVERY_BETA_REVISION_GAP", "case_role": "false_positive_green", "company_name": "주성엔지니어링", "corporate_action_window_status": "clean_180d_by_profile", "current_profile_error": true, "current_profile_verdict": "current_profile_green_too_loose_if_valuation_beta_counts_as_visibility", "dedupe_for_aggregate": true, "do_not_count_as_new_case": false, "drawdown_after_peak_pct": -46.8, "entry_date": "2024-02-28", "entry_price": 40000, "evidence_family": "memory_recovery_equipment_beta_without_durable_customer_capacity_or_backlog", "evidence_url_pending": false, "fine_archetype_id": "MEMORY_RECOVERY_EQUIPMENT_CYCLE_NOT_HBM_CUSTOMER_LOCK", "forward_window_trading_days": 180, "independent_evidence_weight": 1.0, "large_sector_id": "L2_AI_SEMICONDUCTOR_ELECTRONICS", "peak_date": "2024-04-08", "peak_price": 41450, "positive_or_counterexample": "counterexample", "price_adjustment_status": "raw_unadjusted_marcap", "price_basis": "tradable_raw", "price_data_source": "Songdaiki/stock-web", "reuse_reason": null, "same_entry_group_id": "C10_036930_JUSUNG_20240228_MEMORY_RECOVERY_BETA_REVISION_GAP", "scheduled_round": "R2", "schema_version": "v12_no_repeat_standalone_trigger_row_v1", "selected_round": "R2", "source_proxy_only": false, "stage2_evidence_fields": ["memory_downturn_bottoming", "equipment_order_expectation", "relative_strength"], "stage3_evidence_fields": ["revision_bridge_required", "customer_or_backlog_confirmation_missing_or_partial"], "stage4b_evidence_fields": ["valuation_beta_rally", "positioning_overheat", "post_peak_drawdown"], "stage4c_evidence_fields": ["revision_gap", "capex_delay_risk", "generic_cycle_fade"], "symbol": "036930", "trigger_date": "2024-02-28", "trigger_type": "Stage3-Yellow", "upstream_source": "FinanceData/marcap"}
```

## 8. Aggregate / residual contribution

```json
{
  "calibration_usable_case_count": 3,
  "canonical_archetype_id": "C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE",
  "counterexample_count": 2,
  "current_profile_error_count": 2,
  "evidence_url_pending_count": 0,
  "fine_archetype_id": "MEMORY_RECOVERY_EQUIPMENT_CYCLE_NOT_HBM_CUSTOMER_LOCK",
  "hard_duplicate_avoided": true,
  "index_update_needed": true,
  "large_sector_id": "L2_AI_SEMICONDUCTOR_ELECTRONICS",
  "loop_contribution_label": "coverage_gap_fill",
  "new_independent_case_count": 3,
  "positive_case_count": 1,
  "reused_case_count": 0,
  "schema_version": "v12_no_repeat_standalone_aggregate_v1",
  "selected_round": "R2",
  "shadow_rule_candidate": "C10 generic memory equipment recovery should remain Stage2/Yellow unless order/backlog/revision/customer visibility closes.",
  "source_proxy_only_count": 0
}
```

## 9. Deferred Coding Agent Handoff Prompt

Do not execute this in the research session.

```text
Read this standalone v12 residual research MD.
Add the machine-readable rows to the next v12 calibration ingest candidate set only if:
1. canonical_archetype_id=C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE is registered in the runtime archetype mapper;
2. no row violates the hard duplicate key canonical_archetype_id + symbol + trigger_type + entry_date;
3. price fields are verified again from Songdaiki/stock-web tradable shards;
4. C10 Green logic is implemented as a guard, not a global Green threshold relaxation.

Suggested patch axis:
- stage2_required_bridge for C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE
- local_4b_watch_guard for generic memory equipment beta without non-price order/revision evidence

Do not change production scoring directly from this single MD.
Batch with additional C10 cases before applying runtime weight.
```

## 10. Final contribution line

This loop adds 3 new independent cases, 2 counterexamples, and 2 current-profile residual errors for R2/L2_AI_SEMICONDUCTOR_ELECTRONICS/C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE.

