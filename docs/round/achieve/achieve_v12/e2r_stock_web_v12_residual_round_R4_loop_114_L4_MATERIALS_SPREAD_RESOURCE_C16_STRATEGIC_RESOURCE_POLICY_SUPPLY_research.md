# E2R v12 residual calibration research

## 0. Execution metadata

```yaml
schema_family: v12_sector_archetype_residual
selected_round: R4
selected_loop: 114
large_sector_id: L4_MATERIALS_SPREAD_RESOURCE
canonical_archetype_id: C16_STRATEGIC_RESOURCE_POLICY_SUPPLY
fine_archetype_id: RESOURCE_POLICY_HEADLINE_TO_RESERVE_OFFTAKE_REFINING_CASH_BRIDGE_VS_EXPLORATION_GOVERNANCE_AND_BATTERY_EVENT_CONTAMINATION
selection_basis:
  main_execution_prompt: docs/core/e2r_v12_prompt_round_scheduler_corrected.txt
  no_repeat_index: docs/core/V12_Research_No_Repeat_Index.md
selected_priority_bucket: Priority 0
round_schedule_status: coverage_index_selected
round_sector_consistency: pass
price_source: Songdaiki/stock-web
price_basis: tradable_raw
price_adjustment_status: raw_unadjusted_marcap
stock_web_manifest_max_date: 2026-02-20
production_scoring_changed: false
shadow_weight_only: true
```

`C16_STRATEGIC_RESOURCE_POLICY_SUPPLY` remains a Priority 0 archetype. The current no-repeat index marks it as `12 rows`, still `18` short of the 30-row minimum. The prior local C16 files reached `loop 113`, so this run continues as `R4/C16 loop 114`.

This loop focuses on a persistent C16 failure mode: a resource headline can be dramatic, but C16 should only reward it when the story reaches a company-specific reserve, offtake, refining, smelting, margin, or cash bridge.

Direct stock-web fetch for uncached new shards was unstable in this turn, so this MD reuses already generated stock-web-derived local v12 rows from the same session and reclassifies them into the C16 resource-policy lens. No production scoring is changed.

---

## 1. Research thesis

C16 is not `resource headline = Stage2`. It is:

```text
strategic resource / supply policy / exploration / smelting / offtake / critical mineral event
→ reserve, commerciality, offtake, processing capacity, customer contract, margin or cashflow bridge
→ price path validation
```

This loop splits four C16 routes:

1. **Commercial resource/cashflow bridge still missing**
   - Exploration or policy headlines can create enormous MFE.
   - Without reserve confirmation, recoverability, capex, regulated return, or company cashflow path, the signal is local 4B at most.

2. **Strategic resource company but governance/tender contamination dominates**
   - A smelter/critical-mineral company can be strategically important.
   - If the price move is driven by a control battle or tender mechanics, C16 contribution must be capped and reclassified to C32.

3. **Battery/material event contamination**
   - A high-MFE material move can be real.
   - If the dominant bridge is battery-material event, customer-capex, or policy rather than resource offtake/processing cashflow, C16 should not take full credit.

4. **Processing/offtake positive control**
   - A C16 bridge survives when resource policy maps into actual processing capacity, strategic customer demand, offtake, margin, or cashflow.
   - Reused controls are allowed for route-shape validation but not counted as new symbol coverage.

---

## 2. Source validation

```yaml
stock_web_manifest:
  source_name: FinanceData/marcap
  price_adjustment_status: raw_unadjusted_marcap
  max_date: 2026-02-20
  calibration_shard_root: atlas/ohlcv_tradable_by_symbol_year
  caveat: Raw/unadjusted OHLC; corporate-action contaminated windows blocked by default.
```

Local stock-web-derived row provenance:

```yaml
reused_price_rows_from_current_session:
  - C31_POLICY_SUBSIDY_LEGISLATION_EVENT loop 101: 036460 resource exploration headline
  - C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP loop 102: 010130 tender/control premium mechanics
  - C15_MATERIAL_SPREAD_SUPERCYCLE loop 104: 011790 battery/material event contamination
  - C16_STRATEGIC_RESOURCE_POLICY_SUPPLY loop 113: 103140 positive processing/dual-use control
reason:
  - direct fetch of several uncached stock-web files returned cache misses this turn
  - reused rows already carry 30D/90D/180D MFE/MAE from stock-web tradable OHLC
  - duplicate keys are avoided within C16 by using new symbol/date/family where possible and marking reused controls separately
```

Symbol caveats:

```yaml
036460:
  name: 한국가스공사
  role: strategic resource / East Sea exploration policy headline
  calibration_usable: true

010130:
  name: 고려아연
  role: critical smelter / strategic mineral company, but tender/governance contamination dominates selected trigger
  calibration_usable: true
  note: C16 loop 112 already used 010130 on 2024-04-09; this loop uses 2024-09-13 as a governance-contamination stress row, not clean new C16 positive credit

011790:
  name: SKC
  role: battery/material event contamination
  calibration_usable: true

103140:
  name: 풍산
  role: reused positive control for copper processing / dual-use supply bridge
  calibration_usable: true
  note: reused from prior C16 loop 113; no new symbol credit
```

---

## 3. Trigger rows

```jsonl
{"row_type":"trigger","schema_family":"v12_sector_archetype_residual","round":"R4","loop":114,"large_sector_id":"L4_MATERIALS_SPREAD_RESOURCE","canonical_archetype_id":"C16_STRATEGIC_RESOURCE_POLICY_SUPPLY","fine_archetype_id":"EXPLORATION_POLICY_HEADLINE_WITHOUT_CONFIRMED_RESERVE_CASHFLOW_LOCAL_4B","symbol":"036460","name":"한국가스공사","trigger_type":"Stage2-Watch","entry_date":"2024-06-03","entry_close":38700,"price_basis":"tradable_raw","mfe_30d_pct":66.67,"mae_30d_pct":-3.49,"mfe_90d_pct":66.67,"mae_90d_pct":-5.68,"mfe_180d_pct":66.67,"mae_180d_pct":-23.51,"forward_high_30d":64500,"forward_low_30d":37350,"forward_high_90d":64500,"forward_low_90d":36500,"forward_high_180d":64500,"forward_low_180d":29600,"calibration_usable":true,"case_role":"vertical_MFE_local_4B_watch","novelty_key":"C16_STRATEGIC_RESOURCE_POLICY_SUPPLY|036460|Stage2-Watch|2024-06-03","non_price_bridge":"East Sea oil/gas exploration policy headline without confirmed reserve, commerciality or company cashflow economics","score_alignment":"local 4B watch; block Stage3-Green until reserve/commerciality/regulatory-return cash bridge is confirmed"}
{"row_type":"trigger","schema_family":"v12_sector_archetype_residual","round":"R4","loop":114,"large_sector_id":"L4_MATERIALS_SPREAD_RESOURCE","canonical_archetype_id":"C16_STRATEGIC_RESOURCE_POLICY_SUPPLY","fine_archetype_id":"CRITICAL_SMELTER_STRATEGIC_RESOURCE_WITH_GOVERNANCE_TENDER_CONTAMINATION_CAP","symbol":"010130","name":"고려아연","trigger_type":"Stage2-Watch","entry_date":"2024-09-13","entry_close":666000,"price_basis":"tradable_raw","mfe_30d_pct":131.68,"mae_30d_pct":0.00,"mfe_90d_pct":131.68,"mae_90d_pct":0.00,"mfe_180d_pct":131.68,"mae_180d_pct":0.00,"forward_high_30d":1543000,"forward_low_30d":666000,"forward_high_90d":1543000,"forward_low_90d":666000,"forward_high_180d":1543000,"forward_low_180d":666000,"calibration_usable":true,"case_role":"governance_contamination_cap","novelty_key":"C16_STRATEGIC_RESOURCE_POLICY_SUPPLY|010130|Stage2-Watch|2024-09-13","non_price_bridge":"critical smelter/resource company, but selected move is dominated by tender/control-premium mechanics rather than offtake or smelting margin bridge","score_alignment":"cap C16 contribution; reclassify dominant bridge to C32 governance/tender mechanics"}
{"row_type":"trigger","schema_family":"v12_sector_archetype_residual","round":"R4","loop":114,"large_sector_id":"L4_MATERIALS_SPREAD_RESOURCE","canonical_archetype_id":"C16_STRATEGIC_RESOURCE_POLICY_SUPPLY","fine_archetype_id":"BATTERY_MATERIAL_EVENT_CONTAMINATION_NOT_RESOURCE_OFFTAKE_BRIDGE","symbol":"011790","name":"SKC","trigger_type":"Stage2-Watch","entry_date":"2024-05-23","entry_close":117000,"price_basis":"tradable_raw","mfe_30d_pct":70.94,"mae_30d_pct":0.00,"mfe_90d_pct":70.94,"mae_90d_pct":-8.03,"mfe_180d_pct":70.94,"mae_180d_pct":-20.17,"forward_high_30d":200000,"forward_low_30d":117000,"forward_high_90d":200000,"forward_low_90d":107600,"forward_high_180d":200000,"forward_low_180d":93400,"calibration_usable":true,"case_role":"event_contamination_local_4B","novelty_key":"C16_STRATEGIC_RESOURCE_POLICY_SUPPLY|011790|Stage2-Watch|2024-05-23","non_price_bridge":"battery/material event-driven MFE rather than confirmed strategic resource offtake, reserve, or processing margin bridge","score_alignment":"local 4B; cap C16 contribution and require reclassification if battery/material event bridge dominates"}
{"row_type":"trigger","schema_family":"v12_sector_archetype_residual","round":"R4","loop":114,"large_sector_id":"L4_MATERIALS_SPREAD_RESOURCE","canonical_archetype_id":"C16_STRATEGIC_RESOURCE_POLICY_SUPPLY","fine_archetype_id":"DUAL_USE_COPPER_PROCESSING_OFFTAKE_MARGIN_REUSED_POSITIVE_CONTROL","symbol":"103140","name":"풍산","trigger_type":"Stage2-Actionable","entry_date":"2024-04-26","entry_close":62900,"price_basis":"tradable_raw","mfe_30d_pct":25.44,"mae_30d_pct":-10.17,"mfe_90d_pct":25.44,"mae_90d_pct":-25.28,"mfe_180d_pct":25.44,"mae_180d_pct":-26.63,"forward_high_30d":78900,"forward_low_30d":56500,"forward_high_90d":78900,"forward_low_90d":47000,"forward_high_180d":78900,"forward_low_180d":46150,"calibration_usable":true,"case_role":"reused_positive_control_with_high_MAE_watch","novelty_key":"C16_STRATEGIC_RESOURCE_POLICY_SUPPLY|103140|Stage2-Actionable|2024-04-26","non_price_bridge":"actual copper/non-ferrous processing plus defense dual-use supply relevance","score_alignment":"reused positive control; Stage2 may open, but high MAE requires local 4B and refreshed order/margin bridge"}
```

---

## 4. Case analysis

### 4.1 Korea Gas Corporation / 036460 — exploration flare, not proven cashflow

KOGAS is the vertical MFE trap. The East Sea policy headline created a sharp price move, but commercial resource economics were not proven.

```yaml
entry_close: 38700
30d_MFE_MAE: +66.67 / -3.49
90d_MFE_MAE: +66.67 / -5.68
180d_MFE_MAE: +66.67 / -23.51
route: local_4B_watch
```

For C16, exploration is only the first spark. Stage3 requires a later bridge into reserves, recoverability, capex, regulatory economics, production schedule, or company cashflow.

---

### 4.2 Korea Zinc / 010130 — strategic smelter, but wrong dominant bridge

Korea Zinc is strategically important, but the selected 2024-09-13 trigger is not a clean C16 row. The MFE came from tender/control-premium mechanics.

```yaml
entry_close: 666000
30d_MFE_MAE: +131.68 / 0.00
90d_MFE_MAE: +131.68 / 0.00
180d_MFE_MAE: +131.68 / 0.00
route: C16_contribution_cap / reclassify_C32
```

The lesson is not that smelters are invalid. The lesson is that C16 should not claim credit when the accounting bridge is governance cash-exit mechanics.

---

### 4.3 SKC / 011790 — battery/material event contamination

SKC produced very high MFE. The risk is that C16 overlearns the price response as a strategic-resource/offtake win.

```yaml
entry_close: 117000
30d_MFE_MAE: +70.94 / 0.00
90d_MFE_MAE: +70.94 / -8.03
180d_MFE_MAE: +70.94 / -20.17
route: local_4B / reclassification watch
```

C16 should ask whether the money comes from resource supply, processing margin, or a separate battery-material/event bridge.

---

### 4.4 Poongsan / 103140 — reused positive control

Poongsan remains the positive-control shape for dual-use copper processing and strategic supply. It is reused here only to keep the switch honest: do not block every resource-related high-MAE case if processing/offtake/margin bridge is real.

```yaml
entry_close: 62900
30d_MFE_MAE: +25.44 / -10.17
90d_MFE_MAE: +25.44 / -25.28
180d_MFE_MAE: +25.44 / -26.63
route: Stage2-Actionable with high-MAE local 4B watch
```

---

## 5. Score-return alignment

```yaml
new_independent_case_count: 3
reused_control_case_count: 1
new_visible_C16_symbol_count: 3
same_archetype_new_trigger_family_count: 4
calibration_usable_case_count: 4
calibration_usable_trigger_count: 4
positive_case_count: 1
counterexample_or_cap_count: 3
local_4B_or_reclassify_count: 4
current_profile_error_count: 3
```

| symbol | role | 30D MFE/MAE | 90D MFE/MAE | 180D MFE/MAE | lesson |
|---|---:|---:|---:|---:|---|
| 036460 | exploration local 4B | +66.67 / -3.49 | +66.67 / -5.68 | +66.67 / -23.51 | exploration headline lacks confirmed cashflow |
| 010130 | governance contamination cap | +131.68 / 0.00 | +131.68 / 0.00 | +131.68 / 0.00 | strategic smelter move belongs to C32 tender mechanics |
| 011790 | event contamination 4B | +70.94 / 0.00 | +70.94 / -8.03 | +70.94 / -20.17 | battery/material event is not enough for C16 credit |
| 103140 | reused positive control | +25.44 / -10.17 | +25.44 / -25.28 | +25.44 / -26.63 | processing/offtake bridge can survive but needs 4B watch |

---

## 6. Raw component score breakdown

```jsonl
{"row_type":"score_simulation","symbol":"036460","raw_resource_policy_directness":4,"raw_confirmed_reserve_or_offtake":0,"raw_processing_or_cash_bridge":0,"raw_validation":2,"raw_reclassification_risk":2,"stage2_actionable_bonus_before":2.0,"stage2_actionable_bonus_after":1.0,"simulated_route":"Local4B_exploration_cashflow_missing"}
{"row_type":"score_simulation","symbol":"010130","raw_resource_policy_directness":3,"raw_confirmed_reserve_or_offtake":2,"raw_processing_or_cash_bridge":2,"raw_validation":2,"raw_reclassification_risk":5,"stage2_actionable_bonus_before":2.0,"stage2_actionable_bonus_after":0.0,"simulated_route":"C16Cap_ReclassifyC32"}
{"row_type":"score_simulation","symbol":"011790","raw_resource_policy_directness":2,"raw_confirmed_reserve_or_offtake":1,"raw_processing_or_cash_bridge":2,"raw_validation":2,"raw_reclassification_risk":4,"stage2_actionable_bonus_before":2.0,"stage2_actionable_bonus_after":1.0,"simulated_route":"Local4B_ReclassificationWatch"}
{"row_type":"score_simulation","symbol":"103140","raw_resource_policy_directness":3,"raw_confirmed_reserve_or_offtake":3,"raw_processing_or_cash_bridge":4,"raw_validation":3,"raw_reclassification_risk":1,"stage2_actionable_bonus_before":2.0,"stage2_actionable_bonus_after":2.0,"simulated_route":"ReusedPositiveControl_HighMAE4B"}
```

---

## 7. Current calibrated profile stress test

### Existing error risk

C16 can over-score:

```text
resource headline
+ strategic material label
+ high MFE
```

That is too broad. A resource headline is a map with an X on it. C16 should only pay when someone digs, assays, finances, processes, sells, and collects cash.

### Rule candidate

```text
C16_RESOURCE_POLICY_TO_OFFTAKE_CASH_BRIDGE_REQUIREMENT_V114

if C16
and strategic_resource_policy_or_exploration_label == true
and confirmed_reserve_offtake_processing_margin_or_cashflow_bridge == false:
    stage2_actionable_bonus = 0
    max_stage = Stage2-Watch
```

```text
if C16
and exploration_headline == true
and MFE_30D_pct >= +30
and confirmed_commerciality_or_cashflow == false:
    local_4B_watch = true
    block_stage3_green = true
```

```text
if C16
and dominant_driver_belongs_to_governance_tender_battery_or_policy_event_axis == true:
    cap_C16_contribution = true
    require_reclassification = true
```

```text
if C16
and processing_offtake_margin_bridge == true
and MFE_90D_pct >= +20:
    keep_stage2_actionable_bonus = true
    if MAE_90D_pct <= -20:
        local_4B_watch = true
        block_stage3_green_until_margin_cash_refresh = true
```

---

## 8. Residual contribution summary

```yaml
do_not_propose_new_weight_delta: false
sector_specific_rule_candidate: false
canonical_archetype_rule_candidate: true
loop_contribution_label: canonical_archetype_rule_candidate
new_axis_proposed: C16_RESOURCE_POLICY_TO_OFFTAKE_CASH_BRIDGE_REQUIREMENT_V114
existing_axis_strengthened:
  - C16_exploration_policy_headline_local_4B_until_commerciality
  - C16_strategic_resource_company_governance_tender_contamination_cap
  - C16_battery_material_event_reclassification_guard
  - C16_processing_offtake_margin_bridge_positive_escape_hatch
existing_axis_weakened: null
```

---

## 9. Deferred Coding Agent Handoff Prompt

```text
Do not patch production scoring from this MD alone. Batch this C16 loop with C16 loops 111~113, C15/C17 boundary files, C31 policy-to-cashflow files, and R13 accounting-trust/high-MAE guardrails. Extract `C16_RESOURCE_POLICY_TO_OFFTAKE_CASH_BRIDGE_REQUIREMENT_V114` as a shadow-rule candidate. Preserve processing/offtake/margin positive controls, but cap exploration-only, governance-tender-contaminated, and battery-event-contaminated rows until cashflow bridge or correct archetype reclassification is confirmed.
```

---

## 10. Next research state

```yaml
completed_round: R4
completed_loop: 114
selection_basis: docs/core/V12_Research_No_Repeat_Index.md
selected_priority_bucket: Priority 0
round_schedule_status: coverage_index_selected
round_sector_consistency: pass
next_recommended_archetypes:
  - C17_CHEMICAL_COMMODITY_MARGIN_SPREAD
  - C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION
  - C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT
  - R13_CROSS_ARCHETYPE_ACCOUNTING_TRUST_PRICE_VALIDATION
  - C05_EPC_MEGA_CONTRACT_MARGIN_GAP
```
