# stock-web v12 residual research — R13 CROSS ARCHETYPE 4B/4C REDTEAM

```yaml
artifact_type: e2r_stock_web_v12_residual_research
selected_round: R13
selected_loop: 4
large_sector_id: L10_POLICY_EVENT_CROSS_REDTEAM_MISC
canonical_archetype_id: R13_CROSS_ARCHETYPE_4B_4C_REDTEAM
fine_archetype_id: CROSS_ARCHETYPE_4B_WATCH_TOO_EARLY_VS_HARD_4C_LATE_ROUTE_V4
selection_basis: docs/core/V12_Research_No_Repeat_Index.md
round_schedule_status: coverage_index_selected
round_sector_consistency: pass
price_source: Songdaiki/stock-web
price_basis: tradable_raw
price_adjustment_status: raw_unadjusted_marcap
stock_web_manifest_max_date: 2026-02-20
stock_web_shard_root: atlas/ohlcv_tradable_by_symbol_year
created_at_utc: 2026-06-07
```

## 1. Selection note

R13 is used as a cross-archetype checkpoint, not as a new sector-discovery round.  
This pass retests whether the current calibrated profile separates:

- **local 4B watch**: price has run too far or has high-MAE risk, but non-price bridge is not yet thesis-broken.
- **hard 4C review**: price-return alignment is poor, MAE is deep, and the company-specific bridge has not refreshed.
- **contribution cap / reclassification**: MFE exists, but the dominant price driver belongs to a different canonical archetype.

This is the next local pass after the prior `R13_CROSS_ARCHETYPE_4B_4C_REDTEAM` file, so the selected loop is `4`.

## 2. Case set

| case_id | symbol | name | source canonical | role | entry_date | entry_close | key forward path | route decision |
|---|---:|---|---|---|---:|---:|---|---|
| R13_4B4C_V4_01 | 064350 | 현대로템 | C31 | positive control | 2025-02-26 | 85,600 | 2025-03-19 high 116,800; 2025-06-23 high 220,500 | do not hard-4C; keep Stage2 when direct contract bridge exists |
| R13_4B4C_V4_02 | 036460 | 한국가스공사 | C31 | 4B watch → later 4C review | 2024-06-03 | 38,700 | 2024-06-20 high 64,500; 2025-02-11 low 29,600 | local 4B until drilling/economics bridge fails; then hard 4C review |
| R13_4B4C_V4_03 | 011790 | SKC | C17 | contamination cap + 4B watch | 2024-05-23 | 117,000 | 2024-06-18 high 200,000; 2024-12-09 low 90,300 | cap C17 contribution; require reclassification if driver is materials/battery event |
| R13_4B4C_V4_04 | 009830 | 한화솔루션 | C17 | hard 4C candidate | 2024-05-20 | 31,800 | high only 34,300; 2024-10-23 low 20,000 | do not linger in 4B; low-MFE/high-MAE hard 4C review |
| R13_4B4C_V4_05 | 018470 | 조일알미늄 | C15 | hard 4C candidate | 2024-05-20 | 2,470 | high only 2,650; 2024-12-09 low 1,264 | hard 4C; commodity beta label failed |
| R13_4B4C_V4_06 | 005380 | 현대차 | C31 | real-event contribution cap | 2024-08-28 | 259,000 | high only 267,000; 2025-04-11 low 175,800 | real policy/cash-return event, but price alignment failed; cap contribution |

## 3. Trigger rows JSONL

```jsonl
{"case_id":"R13_4B4C_V4_01","symbol":"064350","name":"현대로템","source_canonical_archetype_id":"C31_POLICY_SUBSIDY_LEGISLATION_EVENT","trigger_type":"Stage2-Actionable","entry_date":"2025-02-26","entry_close":85600,"mfe_30d_pct":36.45,"mae_30d_pct":-8.64,"mfe_90d_pct":157.59,"mae_90d_pct":-8.64,"mfe_180d_pct":157.59,"mae_180d_pct":-8.64,"route":"keep_stage2_do_not_hard_4c","calibration_usable":true,"dominant_driver":"signed_direct_export_contract_revenue_bridge","notes":"Direct Morocco rail order/revenue bridge with strong price alignment; avoid 4B/4C too early."}
{"case_id":"R13_4B4C_V4_02","symbol":"036460","name":"한국가스공사","source_canonical_archetype_id":"C31_POLICY_SUBSIDY_LEGISLATION_EVENT","trigger_type":"Stage2-Actionable","entry_date":"2024-06-03","entry_close":38700,"mfe_30d_pct":66.67,"mae_30d_pct":-5.68,"mfe_90d_pct":66.67,"mae_90d_pct":-5.68,"mfe_180d_pct":66.67,"mae_180d_pct":-23.51,"route":"local_4b_watch_then_hard_4c_if_economics_not_confirmed","calibration_usable":true,"dominant_driver":"exploration_policy_headline_without_confirmed_economics","notes":"Vertical MFE from drilling approval/potential reserves; local 4B is right before economics bridge is tested."}
{"case_id":"R13_4B4C_V4_03","symbol":"011790","name":"SKC","source_canonical_archetype_id":"C17_CHEMICAL_COMMODITY_MARGIN_SPREAD","trigger_type":"Stage2-Actionable","entry_date":"2024-05-23","entry_close":117000,"mfe_30d_pct":70.94,"mae_30d_pct":0.00,"mfe_90d_pct":70.94,"mae_90d_pct":-8.03,"mfe_180d_pct":70.94,"mae_180d_pct":-22.82,"route":"local_4b_watch_plus_source_archetype_contribution_cap","calibration_usable":true,"dominant_driver":"materials_battery_event_not_clean_c17_spread","notes":"High MFE exists but dominant driver is not pure chemical feedstock/product spread; cap C17 credit."}
{"case_id":"R13_4B4C_V4_04","symbol":"009830","name":"한화솔루션","source_canonical_archetype_id":"C17_CHEMICAL_COMMODITY_MARGIN_SPREAD","trigger_type":"Stage2-Watch","entry_date":"2024-05-20","entry_close":31800,"mfe_30d_pct":7.86,"mae_30d_pct":-13.21,"mfe_90d_pct":7.86,"mae_90d_pct":-30.35,"mfe_180d_pct":7.86,"mae_180d_pct":-37.11,"route":"hard_4c_review","calibration_usable":true,"dominant_driver":"petchem_solar_mix_without_margin_cash_bridge","notes":"Low MFE/high MAE; 4B watch would be too lenient."}
{"case_id":"R13_4B4C_V4_05","symbol":"018470","name":"조일알미늄","source_canonical_archetype_id":"C15_MATERIAL_SPREAD_SUPERCYCLE","trigger_type":"Stage2-Watch","entry_date":"2024-05-20","entry_close":2470,"mfe_30d_pct":7.29,"mae_30d_pct":-18.83,"mfe_90d_pct":7.29,"mae_90d_pct":-41.30,"mfe_180d_pct":7.29,"mae_180d_pct":-48.83,"route":"hard_4c_review","calibration_usable":true,"dominant_driver":"aluminium_commodity_beta_without_listed_company_spread_bridge","notes":"Commodity vocabulary did not translate into price-return alignment."}
{"case_id":"R13_4B4C_V4_06","symbol":"005380","name":"현대차","source_canonical_archetype_id":"C31_POLICY_SUBSIDY_LEGISLATION_EVENT","trigger_type":"Stage2-Actionable","entry_date":"2024-08-28","entry_close":259000,"mfe_30d_pct":3.09,"mae_30d_pct":-13.71,"mfe_90d_pct":3.09,"mae_90d_pct":-22.82,"mfe_180d_pct":3.09,"mae_180d_pct":-32.12,"route":"real_event_contribution_cap_and_hard_4c_review_if_no_price_alignment","calibration_usable":true,"dominant_driver":"shareholder_return_policy_real_but_margin_cycle_override","notes":"The policy/cash-return event was real, but price path did not validate Stage2 contribution."}
```

## 4. Rule candidate

```text
rule_id = R13_4B_4C_ROUTE_SPLIT_V4

if direct_contract_or_cash_transfer == true
and company_specific_revenue_or_cash_bridge == true
and MFE_90D_pct >= +20
and MAE_90D_pct > -15:
    keep_stage2_actionable_bonus = true
    block_hard_4c = true
```

```text
if MFE_30D_pct >= +25
and MAE_180D_pct <= -20
and confirmed_non_price_bridge == false:
    route = local_4B_watch
    block_stage3_green = true
```

```text
if MFE_90D_pct < +10
and MAE_90D_pct <= -25
and refreshed_revenue_margin_cash_bridge == false:
    route = hard_4C_thesis_break_review
    stage2_actionable_bonus = 0
```

```text
if dominant_price_driver != selected_canonical_archetype_driver
and MFE_30D_pct >= +30:
    cap_source_archetype_contribution = true
    require_cross_archetype_reclassification = true
```

## 5. Residual contribution summary

```yaml
new_independent_case_count: 6
calibration_usable_case_count: 6
positive_control_count: 1
local_4b_watch_count: 2
hard_4c_or_contribution_cap_count: 5
current_profile_error_count: 4
loop_contribution_label: cross_archetype_4b_4c_redteam_guardrail_candidate
new_axis_proposed: R13_4B_4C_ROUTE_SPLIT_V4
existing_axis_strengthened:
  - direct_contract_bridge_blocks_hard_4c_too_early
  - vertical_mfe_without_confirmed_economics_routes_to_local_4b
  - low_mfe_high_mae_routes_to_hard_4c
  - dominant_driver_mismatch_caps_source_archetype_contribution
do_not_propose_new_weight_delta: false
next_recommended_archetypes:
  - C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG
  - C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY
  - C15_MATERIAL_SPREAD_SUPERCYCLE
  - C16_STRATEGIC_RESOURCE_POLICY_SUPPLY
  - R13_CROSS_ARCHETYPE_ACCOUNTING_TRUST_PRICE_VALIDATION
```
