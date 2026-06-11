# E2R stock-web v12 residual research — R4 loop 112 — C16 Strategic Resource Policy Supply

```yaml
schema: e2r_stock_web_v12_residual_research
selected_round: R4
selected_loop: 112
large_sector_id: L4_MATERIALS_SPREAD_RESOURCE
canonical_archetype_id: C16_STRATEGIC_RESOURCE_POLICY_SUPPLY
fine_archetype_id: CRITICAL_MINERAL_SUPPLY_TIGHTNESS_PROCESSING_BRIDGE_VS_RESOURCE_LABEL_BLOWOFF
selection_basis: docs/core/V12_Research_No_Repeat_Index.md
selection_basis_mode: coverage_gap_selected
selected_priority_bucket: Priority 0
price_source: Songdaiki/stock-web
price_basis: tradable_raw
price_adjustment_status: raw_unadjusted_marcap
stock_web_manifest_max_date: 2026-02-20
production_scoring_changed: false
shadow_weight_only: true
do_not_patch_code: true
do_not_trade: true
```

## 1. Coverage / novelty check

C16 is still under-covered in the repository index: `12 rows / 10 symbols`.
The visible top-covered symbols are `000910`, `001120`, `001550`, `012800`, `024840`, `024890`, so this pass uses `010130`, `006110`, and `018470`.

The no-repeat key is treated as:

```text
canonical_archetype_id + symbol + trigger_type + entry_date
```

This run avoids reusing the prior C16 keys visible in the index and the prior local C16 pass.  
`010130` is cross-canonical reused from governance/control-premium work, but its entry date and trigger family here are different and its role is explicitly capped by governance-confound validation.

## 2. Research question

C16 should not reward the word “critical mineral” by itself.

The test is whether a listed company has a concrete bridge from strategic-resource policy or supply tightness to listed-company economics:

```text
policy/supply shock
→ named mineral/feedstock
→ processing/offtake/smelting capacity
→ ASP / spread / utilization / cash conversion
→ price path confirms without later non-C16 contamination
```

This pass stresses three paths:

1. `010130 Korea Zinc` — actual zinc/smelting bridge, but later governance/tender contamination.
2. `006110 Sam-A Aluminium` — aluminium/battery-foil label with large high-MAE failure.
3. `018470 Choil Aluminium` — commodity/resource beta label with low-MFE/high-MAE failure.

External evidence used:
- Reuters, 2024-04-09, zinc smelter treatment charges collapsed as zinc mine supply faltered.
- Korea Zinc public company background: refined zinc / lead smelting and critical metal production.
- Reuters / global reporting context: strategic-resource supply-chain re-shoring does not automatically create listed-company profit bridge.

## 3. Trigger rows JSONL

```jsonl
{"canonical_archetype_id":"C16_STRATEGIC_RESOURCE_POLICY_SUPPLY","large_sector_id":"L4_MATERIALS_SPREAD_RESOURCE","symbol":"010130","name":"고려아연","trigger_type":"Stage2-Actionable","entry_date":"2024-04-09","entry_close":469000,"trigger_family":"ZINC_TC_COLLAPSE_SUPPLY_TIGHTNESS_SMELTER_BRIDGE","case_role":"positive_control_with_governance_confound_cap","mfe_30d_pct":6.40,"mae_30d_pct":-3.94,"mfe_90d_pct":16.42,"mae_90d_pct":-3.94,"mfe_180d_pct":68.66,"mae_180d_pct":-3.94,"peak_date_30d":"2024-05-09","trough_date_30d":"2024-04-25","peak_date_90d":"2024-05-21","trough_date_90d":"2024-04-25","peak_date_180d":"2024-10-04","trough_date_180d":"2024-04-25","calibration_usable":true,"caveat":"180D MFE is contaminated by later governance/tender event after 2024-09-13; learn only the supply-bridge allowance and apply contribution cap.","local_4b_watch":true,"stage2_actionable_bonus_allowed":true,"stage3_green_allowed":false}
{"canonical_archetype_id":"C16_STRATEGIC_RESOURCE_POLICY_SUPPLY","large_sector_id":"L4_MATERIALS_SPREAD_RESOURCE","symbol":"006110","name":"삼아알미늄","trigger_type":"Stage2-Watch","entry_date":"2024-05-20","entry_close":75500,"trigger_family":"ALUMINIUM_BATTERY_FOIL_RESOURCE_LABEL_HIGH_MFE_HIGH_MAE","case_role":"counterexample","mfe_30d_pct":28.34,"mae_30d_pct":-7.28,"mfe_90d_pct":28.34,"mae_90d_pct":-47.55,"mfe_180d_pct":28.34,"mae_180d_pct":-53.58,"peak_date_30d":"2024-06-11","trough_date_30d":"2024-05-22","peak_date_90d":"2024-06-11","trough_date_90d":"2024-08-05","peak_date_180d":"2024-06-11","trough_date_180d":"2024-11-15","calibration_usable":true,"caveat":"Corporate-action candidate in 2023 is outside this forward window; raw 2024 path is usable with caveat.","local_4b_watch":true,"stage2_actionable_bonus_allowed":false,"stage3_green_allowed":false}
{"canonical_archetype_id":"C16_STRATEGIC_RESOURCE_POLICY_SUPPLY","large_sector_id":"L4_MATERIALS_SPREAD_RESOURCE","symbol":"018470","name":"조일알미늄","trigger_type":"Stage2-Watch","entry_date":"2024-05-20","entry_close":2470,"trigger_family":"ALUMINIUM_ROLLING_COMMODITY_BETA_LOW_MFE_HIGH_MAE","case_role":"counterexample","mfe_30d_pct":7.29,"mae_30d_pct":-17.41,"mfe_90d_pct":7.29,"mae_90d_pct":-41.30,"mfe_180d_pct":7.29,"mae_180d_pct":-44.70,"peak_date_30d":"2024-05-21","trough_date_30d":"2024-06-19","peak_date_90d":"2024-05-21","trough_date_90d":"2024-08-05","peak_date_180d":"2024-05-21","trough_date_180d":"2024-11-15","calibration_usable":true,"caveat":"Full-window extension reached 2024-12-09 low 1264, but 180D row uses 2024-11-15 low 1366.","local_4b_watch":true,"stage2_actionable_bonus_allowed":false,"stage3_green_allowed":false}
```

## 4. Case notes

### 4.1 010130 — Korea Zinc — positive bridge, but capped by governance contamination

Korea Zinc is not just a resource word. It has a smelting/processing bridge: refined zinc and lead, byproducts, and critical metal exposure. The zinc treatment-charge collapse in April 2024 was a real upstream supply-tightness signal.

Price path:

```text
entry: 2024-04-09 close 469,000
30D high: 499,000 / low: 450,500
90D high: 546,000 / low: 450,500
180D high: 791,000 / low: 450,500
```

Interpretation:

- The 30D/90D path supports a limited C16 Stage2 allowance.
- The 180D MFE should not be fully credited to C16 because the later September–October move was contaminated by a governance/control-premium tender battle.
- Score contribution should be capped after a non-C16 event becomes dominant.

### 4.2 006110 — Sam-A Aluminium — aluminium/battery-foil label high-MFE/high-MAE trap

Sam-A Aluminium shows why C16 cannot reward “strategic aluminium / battery foil” vocabulary alone.

Price path:

```text
entry: 2024-05-20 close 75,500
30D high: 96,900 / low: 70,000
90D high: 96,900 / low: 39,600
180D high: 96,900 / low: 35,050
```

The first move created a tempting +28% MFE. But the same trigger window later produced a deep drawdown, so it should be treated as:

```text
resource_label + high MFE + no refreshed margin/cash bridge
→ local_4B_watch
→ block Stage3-Green
```

### 4.3 018470 — Choil Aluminium — low-MFE/high-MAE false positive

Choil Aluminium is the stricter negative control. The entry had aluminium-resource vocabulary, but the listed-company conversion was weak.

Price path:

```text
entry: 2024-05-20 close 2,470
30D high: 2,650 / low: 2,040
90D high: 2,650 / low: 1,450
180D high: 2,650 / low: 1,366
full extension low: 2024-12-09 low 1,264
```

This is a direct Stage2-bonus block:

```text
strategic resource label
+ no named offtake / processing / ASP / margin bridge
+ MFE_90D < +10
+ MAE_90D <= -25
→ Stage2-FalsePositive / Stage2-Watch cap
```

## 5. Current profile stress test

The current calibrated profile should behave as follows:

```text
C16 current rule tendency:
- can over-credit commodity/resource vocabulary
- can over-credit policy/supply-chain language before company-level bridge
- can under-penalize high-MFE/high-MAE resource blowoffs
```

Required stress-test response:

| test | expected behavior |
|---|---|
| Korea Zinc 2024-04-09 | Stage2 allowed, but contribution capped after governance event dominates |
| Sam-A Aluminium 2024-05-20 | Stage2-Actionable bonus removed; local 4B watch |
| Choil Aluminium 2024-05-20 | Stage2 blocked; max Stage2-Watch |

## 6. Raw component score breakdown proposal

Shadow-only. No production scoring change.

```json
{
  "C16_STRATEGIC_RESOURCE_POLICY_SUPPLY": {
    "company_specific_processing_or_offtake_bridge": "+2.0",
    "named_mineral_supply_tightness_with_direct_listed_company_bridge": "+1.0",
    "resource_label_without_ASP_margin_cash_bridge": "-2.5",
    "commodity_beta_high_MFE_high_MAE_without_refresh": "-2.0",
    "non_C16_event_contamination_after_entry": "cap_positive_contribution",
    "stage3_green_requires_refreshed_margin_or_cash_bridge": true
  }
}
```

## 7. Candidate rule

```text
rule_id = C16_RESOURCE_LABEL_TO_CASH_BRIDGE_GATE

if canonical_archetype_id == C16_STRATEGIC_RESOURCE_POLICY_SUPPLY
and strategic_resource_or_policy_label == true
and company_specific_ASP_volume_processing_offtake_cash_bridge == false:
    stage2_actionable_bonus = 0
    max_stage = Stage2-Watch
```

```text
if canonical_archetype_id == C16_STRATEGIC_RESOURCE_POLICY_SUPPLY
and MFE_30D_pct >= +20
and MAE_90D_pct <= -25
and refreshed_margin_or_cash_bridge == false:
    local_4B_watch = true
    block_stage3_green = true
```

```text
if canonical_archetype_id == C16_STRATEGIC_RESOURCE_POLICY_SUPPLY
and later_non_C16_event_dominates_price_path == true:
    cap_C16_contribution_after_contamination_date = true
```

## 8. Residual contribution summary

```yaml
new_independent_case_count: 3
reused_case_count_within_C16_visible_basis: 0
cross_canonical_reused_symbol_count: 1
same_archetype_new_symbol_count_visible_index_basis: 3
same_archetype_new_trigger_family_count: 3
calibration_usable_case_count: 3
calibration_usable_trigger_count: 3
positive_case_count: 1
counterexample_count: 2
current_profile_error_count: 2
sector_specific_rule_candidate: false
canonical_archetype_rule_candidate: true
loop_contribution_label: canonical_archetype_rule_candidate
new_axis_proposed: null
existing_axis_strengthened:
  - C16_company_specific_processing_offtake_cash_bridge_requirement
  - C16_resource_label_without_margin_conversion_stage2_block
  - C16_vertical_MFE_local_4B_watch_after_resource_beta_blowoff
  - C16_non_C16_event_contamination_cap
next_recommended_archetypes:
  - C17_CHEMICAL_COMMODITY_MARGIN_SPREAD
  - R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL
  - R13_CROSS_ARCHETYPE_STAGE2_FALSE_POSITIVE_REVIEW
  - C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG
  - C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY
```
