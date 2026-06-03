# E2R Stock-Web Historical Calibration / Sector-Archetype Residual Research Round

## 0. Research Metadata

```json
{
  "mode": "historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12",
  "research_session": "post_calibrated_sector_archetype_residual_research",
  "scheduled_round": "R2",
  "scheduled_loop": 12,
  "round_schedule_status": "valid",
  "round_sector_consistency": "pass",
  "completed_round": "R2",
  "completed_loop": 12,
  "next_round": "R3",
  "next_loop": 12,
  "large_sector_id": "L2_AI_SEMICONDUCTOR_ELECTRONICS",
  "canonical_archetype_id": "C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH",
  "fine_archetype_id": "HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH_DIRECT_ROLE_VS_THEME",
  "loop_objective": ["coverage_gap_fill", "sector_specific_rule_discovery", "canonical_archetype_compression", "counterexample_mining", "green_strictness_stress_test", "4B_non_price_requirement_stress_test", "stage2_actionable_bonus_stress_test"],
  "price_source": "Songdaiki/stock-web",
  "stock_web_manifest_max_date": "2026-02-20",
  "price_basis": "tradable_raw",
  "price_adjustment_status": "raw_unadjusted_marcap",
  "production_scoring_changed": false,
  "shadow_weight_only": true,
  "new_independent_case_count": 4,
  "reused_case_count": 0,
  "new_symbol_count": 4,
  "same_archetype_new_symbol_count": 4,
  "same_archetype_new_trigger_family_count": 4,
  "new_trigger_family_count": 4,
  "calibration_usable_case_count": 4,
  "calibration_usable_trigger_count": 6,
  "positive_case_count": 3,
  "counterexample_count": 1,
  "current_profile_error_count": 3,
  "diversity_score_summary": "estimated +55; wrong_round_penalty=0; repeated_same_symbol_penalty=0; schema_rematerialization_penalty=0",
  "loop_contribution_label": "canonical_archetype_rule_candidate",
  "do_not_propose_new_weight_delta": false
}
```

This loop adds **4** new independent cases, **1** counterexample, and **3** residual errors for **R2 / L2_AI_SEMICONDUCTOR_ELECTRONICS / C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH**.

This file does not perform live scanning and does not recommend securities. It is a historical calibration artifact only. The question tested here is narrow: in R2, does HBM equipment relative strength mean the same thing when it comes from a **direct equipment role and customer/order bridge** versus a **theme-only price chase**? The stock-web rows say no. Direct equipment routes behaved like a gear engaging a drivetrain; theme-only routes behaved like a loose belt—fast for a moment, then slipping violently.

## 1. Current Calibrated Profile Assumption

```text
current_default_profile_proxy = e2r_2_1_stock_web_calibrated_proxy
previous_baseline_reference = e2r_2_0_baseline_reference
stage2_actionable_evidence_bonus = +2.0
stage3_yellow_total_min = 75.0
stage3_green_total_min = 87.0
stage3_green_revision_min = 55.0
stage3_cross_evidence_green_buffer = +1.5
price_only_blowoff_blocks_positive_stage = true
full_4b_requires_non_price_evidence = true
hard_4c_thesis_break_routes_to_4c = true
```

The existing global axes are not re-proposed. This loop stress-tests them inside C07 and proposes only sector/canonical-archetype shadow rules.

## 2. Round / Large Sector / Canonical Archetype Scope

```text
scheduled_round = R2
scheduled_loop = 12
large_sector_id = L2_AI_SEMICONDUCTOR_ELECTRONICS
canonical_archetype_id = C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH
fine_archetype_id = HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH_DIRECT_ROLE_VS_THEME
round_schedule_status = valid
round_sector_consistency = pass
```

R2 is the correct scheduled round after R1 loop 12. The file stays inside the AI / semiconductor / electronics lane.

## 3. Previous Coverage / Duplicate Avoidance Check

Local v12 outputs already contained R2 loop 10 for `C06_HBM_MEMORY_CUSTOMER_CAPACITY` with 삼성전자/SK하이닉스 and R2 loop 11 for `C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY` with 리노공업/티에스이/ISC. This loop avoids those symbols and trigger families.

```text
same_canonical_archetype_research = allowed
same_symbol_same_trigger_date_research = avoided
new_symbol_count = 4
same_archetype_new_symbol_count = 4
same_archetype_new_trigger_family_count = 4
new_independent_case_ratio = 1.00
wrong_round_penalty = 0
```

## 4. Stock-Web OHLC Input / Price Source Validation

```text
price_data_source = Songdaiki/stock-web
source_basis = FinanceData/marcap
price_basis = tradable_raw
price_adjustment_status = raw_unadjusted_marcap
manifest_path = atlas/manifest.json
schema_path = atlas/schema.json
universe_path = atlas/universe/all_symbols.csv
stock_web_manifest_max_date = 2026-02-20
calibration_shard_root = atlas/ohlcv_tradable_by_symbol_year
raw_shard_root = atlas/ohlcv_raw_by_symbol_year
tradable_row_count = 14354401
raw_row_count = 15214118
symbol_count = 5414
```

The inspected schema uses `d,o,h,l,c,v,a,mc,s,m` for tradable shards. Raw/unadjusted OHLC is used; corporate-action-contaminated windows are blocked by default.

## 5. Historical Eligibility Gate

All representative triggers are historical, have an entry row in the tradable shard, have at least 180 forward tradable days before the manifest max date, and do not overlap the listed corporate-action candidate dates in their 180D calibration windows.

| symbol | company | price_shard_path | profile_path | corporate_action_window_status | profile summary |
| --- | --- | --- | --- | --- | --- |
| 042700 | 한미반도체 | atlas/ohlcv_tradable_by_symbol_year/042/042700/2024.csv | atlas/symbol_profiles/042/042700.json | clean_180D_window | active_like; last_date 2026-02-20; corporate-action candidates 2006-11-10, 2017-05-11, 2022-04-06; chosen 2024 window clean |
| 089030 | 테크윙 | atlas/ohlcv_tradable_by_symbol_year/089/089030/2024.csv | atlas/symbol_profiles/089/089030.json | clean_180D_window | active_like; last_date 2026-02-20; corporate-action candidates 2011/2022 only; chosen 2024 window clean |
| 232140 | 와이씨 | atlas/ohlcv_tradable_by_symbol_year/232/232140/2024.csv | atlas/symbol_profiles/232/232140.json | clean_180D_window | active_like; current name 와이씨 from 2024-04-25; corporate-action candidate 2017-04-05 only; 2024 window clean |
| 003160 | 디아이 | atlas/ohlcv_tradable_by_symbol_year/003/003160/2024.csv | atlas/symbol_profiles/003/003160.json | clean_180D_window | active_like; last_date 2026-02-20; corporate-action candidates 1997/1998/1999 only; chosen 2024 window clean |

## 6. Canonical Archetype Compression Map

| fine_archetype_id | canonical_archetype_id | Compression logic |
| --- | --- | --- |
| HBM_TCBONDER_DIRECT_ORDER_RELATIVE_STRENGTH | C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH | direct HBM package equipment role + customer/order quality + relative strength |
| HBM_TEST_HANDLER_EQUIPMENT_RELATIVE_STRENGTH | C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH | handler/test equipment route with clear relative strength |
| HBM_MEMORY_TESTER_DIRECT_CUSTOMER_HIGH_MAE | C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH | memory tester route, but high-MAE handling required |
| HBM_TESTER_THEME_WITHOUT_ORDER_CONFIRMATION | C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH | theme-only / weak direct-order evidence counterexample |

## 7. Case Selection Summary

| case_id | symbol | company | role | positive_or_counterexample | why selected |
| --- | --- | --- | --- | --- | --- |
| R2L12_C07_042700_HANMI_TCBONDER | 042700 | 한미반도체 | structural_success | positive | direct_HBM_equipment_order_route_success_with_late_4B_need |
| R2L12_C07_089030_TECHWING_HBM_HANDLER | 089030 | 테크윙 | structural_success | positive | HBM_handler_relative_strength_success_but_requires_4B_overlay_after_blowoff |
| R2L12_C07_232140_YC_TESTER_HIGH_MAE | 232140 | 와이씨 | high_mae_success | positive | direct_tester_route_success_with_high_MAE_and_late_green_risk |
| R2L12_C07_003160_DI_TESTER_THEME_COUNTEREXAMPLE | 003160 | 디아이 | false_positive_green | counterexample | theme_relative_strength_false_green_counterexample |

## 8. Positive vs Counterexample Balance

```text
positive_case_count = 3
counterexample_count = 1
calibration_usable_case_count = 4
calibration_usable_trigger_count = 6
minimum_positive_case_count = pass
minimum_counterexample_count = pass
minimum_calibration_usable_case_count = pass
```

The balance is intentionally asymmetric: three direct-equipment positives plus one hard counterexample. That shape is useful because C07 is not missing proof that HBM equipment can work; it is missing a guard that prevents every strong HBM-adjacent chart from being treated as direct equipment evidence.

## 9. Evidence Source Map

| symbol | trigger_date | evidence family | stage2 fields | stage3 fields | red-team issue |
| --- | --- | --- | --- | --- | --- |
| 042700 | 2024-02-08 | HBM_TCBONDER_DIRECT_ORDER_RELATIVE_STRENGTH | public_event_or_disclosure, customer_or_order_quality, relative_strength, capacity_or_volume_route, early_revision_signal | confirmed_revision, multiple_public_sources, financial_visibility, durable_customer_confirmation | direct_HBM_equipment_order_route_success_with_late_4B_need |
| 089030 | 2024-02-13 | HBM_TEST_HANDLER_EQUIPMENT_RELATIVE_STRENGTH | public_event_or_disclosure, customer_or_order_quality, relative_strength, capacity_or_volume_route, early_revision_signal | confirmed_revision, multiple_public_sources, financial_visibility, repeat_order_or_conversion | HBM_handler_relative_strength_success_but_requires_4B_overlay_after_blowoff |
| 232140 | 2024-04-18 | HBM_MEMORY_TESTER_DIRECT_CUSTOMER_HIGH_MAE | public_event_or_disclosure, customer_or_order_quality, relative_strength, capacity_or_volume_route | multiple_public_sources, financial_visibility | direct_tester_route_success_with_high_MAE_and_late_green_risk |
| 003160 | 2024-04-15 | HBM_TESTER_THEME_WITHOUT_ORDER_CONFIRMATION | public_event_or_disclosure, relative_strength | multiple_public_sources | theme_relative_strength_false_green_counterexample |

Evidence source enrichment remains required before any future production promotion. This MD uses evidence family and stock-web OHLC rows for historical residual calibration, not live investment research.

## 10. Price Data Source Map

| symbol | company | price_shard_path | profile_path | corporate_action_window_status | profile summary |
| --- | --- | --- | --- | --- | --- |
| 042700 | 한미반도체 | atlas/ohlcv_tradable_by_symbol_year/042/042700/2024.csv | atlas/symbol_profiles/042/042700.json | clean_180D_window | active_like; last_date 2026-02-20; corporate-action candidates 2006-11-10, 2017-05-11, 2022-04-06; chosen 2024 window clean |
| 089030 | 테크윙 | atlas/ohlcv_tradable_by_symbol_year/089/089030/2024.csv | atlas/symbol_profiles/089/089030.json | clean_180D_window | active_like; last_date 2026-02-20; corporate-action candidates 2011/2022 only; chosen 2024 window clean |
| 232140 | 와이씨 | atlas/ohlcv_tradable_by_symbol_year/232/232140/2024.csv | atlas/symbol_profiles/232/232140.json | clean_180D_window | active_like; current name 와이씨 from 2024-04-25; corporate-action candidate 2017-04-05 only; 2024 window clean |
| 003160 | 디아이 | atlas/ohlcv_tradable_by_symbol_year/003/003160/2024.csv | atlas/symbol_profiles/003/003160.json | clean_180D_window | active_like; last_date 2026-02-20; corporate-action candidates 1997/1998/1999 only; chosen 2024 window clean |

## 11. Case-by-Case Trigger Grid

| case_id | symbol | company | role | trigger | entry | entry_price | MFE30 | MFE90 | MFE180 | MAE30 | MAE90 | MAE180 | peak | drawdown | current_profile |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| R2L12_C07_042700_HANMI_TCBONDER | 042700 | 한미반도체 | structural_success | Stage2-Actionable | 2024-02-08 | 78500 | 37.32 | 150.0 | 150.0 | -9.94 | -10.32 | -10.32 | 2024-06-14 | -53.47 | current_profile_too_late |
| R2L12_C07_089030_TECHWING_HBM_HANDLER | 089030 | 테크윙 | structural_success | Stage2-Actionable | 2024-02-13 | 18690 | 92.62 | 243.98 | 278.81 | -6.05 | -6.05 | -6.05 | 2024-07-11 | -57.63 | current_profile_correct |
| R2L12_C07_232140_YC_TESTER_HIGH_MAE | 232140 | 와이씨 | high_mae_success | Stage2-Actionable | 2024-04-18 | 9460 | 88.48 | 142.6 | 142.6 | -25.48 | -25.48 | -25.48 | 2024-06-13 | -33.03 | current_profile_too_early |
| R2L12_C07_003160_DI_TESTER_THEME_COUNTEREXAMPLE | 003160 | 디아이 | false_positive_green | Stage3-Green-Candidate | 2024-04-15 | 22650 | 13.91 | 35.98 | 35.98 | -27.59 | -44.19 | -44.19 | 2024-06-27 | -58.96 | current_profile_false_positive |

## 12. Trigger-Level OHLC Backtest Tables

| case_id | symbol | company | role | trigger | entry | entry_price | MFE30 | MFE90 | MFE180 | MAE30 | MAE90 | MAE180 | peak | drawdown | current_profile |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| R2L12_C07_042700_HANMI_TCBONDER | 042700 | 한미반도체 | structural_success | Stage2-Actionable | 2024-02-08 | 78500 | 37.32 | 150.0 | 150.0 | -9.94 | -10.32 | -10.32 | 2024-06-14 | -53.47 | current_profile_too_late |
| R2L12_C07_089030_TECHWING_HBM_HANDLER | 089030 | 테크윙 | structural_success | Stage2-Actionable | 2024-02-13 | 18690 | 92.62 | 243.98 | 278.81 | -6.05 | -6.05 | -6.05 | 2024-07-11 | -57.63 | current_profile_correct |
| R2L12_C07_232140_YC_TESTER_HIGH_MAE | 232140 | 와이씨 | high_mae_success | Stage2-Actionable | 2024-04-18 | 9460 | 88.48 | 142.6 | 142.6 | -25.48 | -25.48 | -25.48 | 2024-06-13 | -33.03 | current_profile_too_early |
| R2L12_C07_003160_DI_TESTER_THEME_COUNTEREXAMPLE | 003160 | 디아이 | false_positive_green | Stage3-Green-Candidate | 2024-04-15 | 22650 | 13.91 | 35.98 | 35.98 | -27.59 | -44.19 | -44.19 | 2024-06-27 | -58.96 | current_profile_false_positive |

Representative interpretation:

- 한미반도체 and 테크윙 both show that direct HBM equipment role + relative strength can deserve earlier Yellow/Green-shadow treatment than the strict revision-only Green gate.
- 와이씨 shows a high-MAE success pattern: the eventual MFE was large, but the entry-day and early-window low made unguarded Green psychologically and quantitatively fragile.
- 디아이는 the counterexample: relative strength and HBM tester narrative alone produced much weaker score-return alignment and severe MAE.

## 13. Current Calibrated Profile Stress Test

| case | current profile verdict | why | actual alignment |
| --- | --- | --- | --- |
| R2L12_C07_042700_HANMI_TCBONDER | current_profile_too_late | TC-bonder / HBM packaging equipment demand was already a public order-quality narrative. The price row shows the first decisive gap-up day; this trigger tests whether direct equipment route + relative strength deserved Yellow before strict Green confirmation. | MFE90=150.0 / MAE90=-10.32 / drawdown=-53.47 |
| R2L12_C07_089030_TECHWING_HBM_HANDLER | current_profile_correct | HBM test-handler / advanced package inspection route gained public attention with strong relative strength. This is a clean example where equipment-specific path, not just memory-price beta, led the move. | MFE90=243.98 / MAE90=-6.05 / drawdown=-57.63 |
| R2L12_C07_232140_YC_TESTER_HIGH_MAE | current_profile_too_early | Memory tester/HBM tester narrative produced a massive move, but the entry-day low and subsequent whipsaw show why C07 should tolerate high MAE only when direct customer/order quality is explicit. | MFE90=142.6 / MAE90=-25.48 / drawdown=-33.03 |
| R2L12_C07_003160_DI_TESTER_THEME_COUNTEREXAMPLE | current_profile_false_positive | Tester/HBM theme momentum was strong, but direct order visibility and durable revision confirmation were weaker than the price move. The path had modest MFE versus severe MAE, making it a C07 false-Green counterexample. | MFE90=35.98 / MAE90=-44.19 / drawdown=-58.96 |

Current profile verdict summary:

```text
current_profile_correct = 1
current_profile_too_late = 1
current_profile_too_early = 1
current_profile_false_positive = 1
current_profile_error_count = 3
```

## 14. Stage2 / Yellow / Green Comparison

```text
Stage2-Actionable worked when direct equipment role + customer/order quality were both visible.
Yellow threshold 75 was generally appropriate.
Green threshold 87 / revision 55 was too slow for Hanmi-style direct equipment winners, but too permissive for DI-style theme-only relative strength.
Therefore the residual is not global Green threshold; it is C07 evidence composition.
```

Green lateness proxy:

| symbol | Stage2 entry | observed peak | green_lateness_ratio | verdict |
| --- | --- | --- | --- | --- |
| 042700 | 78,500 | 196,200 | 0.45 | Green can be late if direct equipment evidence is already strong |
| 089030 | 18,690 | 70,800 | 0.34 | Green acceptable but 4B overlay required near peak |
| 232140 | 9,460 | 22,950 | 0.58 | high-MAE success; Yellow/guarded Green only |
| 003160 | 22,650 | 30,800 | not_applicable | theme-only Green candidate should be capped |

## 15. 4B Local vs Full-window Timing Audit

| symbol | 4B evidence type | local proximity | full-window proximity | verdict |
| --- | --- | --- | --- | --- |
| 042700 | valuation_blowoff, positioning_overheat | 0.93 | 1.00 | good full-window 4B if non-price evidence exists |
| 089030 | valuation_blowoff, positioning_overheat | 0.95 | 1.00 | good full-window 4B if non-price evidence exists |
| 232140 | valuation_blowoff, positioning_overheat | 0.87 | 1.00 | high-MAE success needs late 4B overlay |
| 003160 | price_only, positioning_overheat | 0.41 | 1.00 | local price-only 4B too early; not full 4B without non-price evidence |

This strengthens, rather than re-proposes, the already-applied `full_4b_requires_non_price_evidence` axis.

## 16. 4C Protection Audit

```text
hard_4c_success = 0
hard_4c_late = 0
false_break = 0
thesis_break_watch_only = 1
```

DI is a watch-only 4C case. Price drawdown alone is not enough for hard 4C; however, the poor MFE/MAE after a weak evidence bridge supports a C07 thesis-break watch route when order/revision evidence fails to appear after a theme spike.

## 17. Sector-Specific Rule Candidate

```text
rule_scope = sector_specific
rule_id = R2_direct_equipment_role_bridge_bonus
proposal_type = sector_shadow_only
```

In R2, early promotion should reward direct equipment role + customer/order evidence + relative strength. The rule should not reward generic HBM chart momentum without a customer/order bridge.

## 18. Canonical-Archetype Rule Candidate

```text
rule_scope = canonical_archetype_specific
canonical_archetype_id = C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH
rule_id = C07_direct_equipment_role_bridge_required_for_green
```

Candidate rule:

```text
if canonical_archetype_id == C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH:
    if direct_equipment_role and customer_or_order_quality and relative_strength:
        allow Stage3-Green-shadow even if revision confirmation is still developing
    if relative_strength is strong but contract/order/customer/revision components are weak:
        cap at Stage2-Watch or Stage3-Yellow
    if MFE is high but MAE is also severe:
        label as high_MAE_success, not unrestricted Green
```

## 19. Before / After Backtest Comparison

| profile | scope | eligible | avg MFE90 | avg MAE90 | avg MFE180 | avg MAE180 | false positive | verdict |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| P0_e2r_2_1_stock_web_calibrated_proxy | current_proxy | 4 | 143.14 | -21.51 | 151.85 | -21.51 | 0.25 | mixed; direct-equipment positives align, theme-only DI false-Green remains residual error |
| P0b_e2r_2_0_baseline_reference | rollback_reference | 4 | 143.14 | -21.51 | 151.85 | -21.51 | 0.25 | weaker than current proxy |
| P1_sector_specific_candidate_profile | sector_specific | 4 | 178.86 | -13.95 | 190.47 | -13.95 | 0.0 | better; preserves direct equipment winners and blocks DI false Green |
| P2_canonical_archetype_candidate_profile | canonical_archetype_specific | 4 | 178.86 | -13.95 | 190.47 | -13.95 | 0.0 | best candidate for shadow ledger |
| P3_counterexample_guard_profile | counterexample_guard | 4 | 178.86 | -13.95 | 190.47 | -13.95 | 0.0 | strong guardrail; keep shadow-only until more C07 cases |

## 20. Score-Return Alignment Matrix

| symbol | before label | after label | MFE90 | MAE90 | alignment |
| --- | --- | --- | --- | --- | --- |
| 042700 | Stage3-Yellow | Stage3-Green-Shadow | 150.00 | -10.32 | direct equipment route deserved earlier promotion |
| 089030 | Stage3-Yellow | Stage3-Green-Shadow | 243.98 | -6.05 | strong alignment, but 4B overlay near peak |
| 232140 | Stage3-Yellow | Stage3-Yellow-High-MAE-Guarded | 142.60 | -25.48 | worked, but only with high-MAE guard |
| 003160 | Stage3-Green | Stage2-Watch | 35.98 | -44.19 | false-Green counterexample |

## 21. Coverage Matrix

| large_sector_id | canonical_archetype_id | fine_archetype_id | positive_case_count | counterexample_count | 4B_case_count | 4C_case_count | new_independent_case_count | reused_case_count | calibration_usable_trigger_count | representative_trigger_count | current_profile_error_count | sector_rule_candidate | canonical_rule_candidate | coverage_gap_after_this_loop |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| L2_AI_SEMICONDUCTOR_ELECTRONICS | C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH | HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH_DIRECT_ROLE_VS_THEME | 3 | 1 | 2 | 1 | 4 | 0 | 6 | 4 | 3 | True | True | C07 now has direct-equipment positives plus one theme-only false-Green counterexample; still needs more non-HBM equipment holdouts |

## 22. Residual Contribution Summary

```text
new_independent_case_count: 4
reused_case_count: 0
reused_case_ids: []
new_symbol_count: 4
new_canonical_archetype_count: 1
new_fine_archetype_count: 4
new_trigger_family_count: 4
tested_existing_calibrated_axes: stage2_actionable_evidence_bonus, stage3_yellow_total_min, stage3_green_total_min, stage3_green_revision_min, stage3_cross_evidence_green_buffer, price_only_blowoff_blocks_positive_stage, full_4b_requires_non_price_evidence, hard_4c_thesis_break_routes_to_4c
residual_error_types_found: theme_only_relative_strength_false_green, high_MAE_success_requires_direct_customer_order_bridge, late_4B_after_HBM_equipment_blowoff, green_strictness_too_late_for_direct_equipment_winner
new_axis_proposed: C07_direct_equipment_role_bridge_required_for_green
existing_axis_strengthened: full_4b_requires_non_price_evidence, price_only_blowoff_blocks_positive_stage
existing_axis_weakened: null
existing_axis_kept: stage2_actionable_evidence_bonus, stage3_yellow_total_min, stage3_green_total_min, stage3_green_revision_min, stage3_cross_evidence_green_buffer, hard_4c_thesis_break_routes_to_4c
sector_specific_rule_candidate: true
canonical_archetype_rule_candidate: true
no_new_signal_reason: null
loop_contribution_label: canonical_archetype_rule_candidate
do_not_propose_new_weight_delta: false
```

## 23. Validation Scope / Non-Validation Scope

Validated:

```text
- stock-web manifest max_date and price basis
- tradable shard paths and schema columns
- representative trigger OHLC rows around entry/peak/drawdown
- clean 180D corporate-action window for selected cases
- positive/counterexample balance
- same_entry_group_id dedupe logic
- current calibrated profile stress test
```

Not validated:

```text
- live candidate suitability
- current 2026 Stage3 status
- production score code behavior
- brokerage or auto-trading behavior
- exact future implementation path inside stock_agent src/e2r
- complete original URL enrichment for every public evidence item
```

## 24. Shadow Weight Calibration

```csv
row_type,axis,scope,large_sector_id,canonical_archetype_id,baseline_value,tested_value,delta,reason,backtest_effect,trigger_ids,calibration_usable_count,new_independent_case_count,counterexample_count,confidence,proposal_type,notes
shadow_weight,C07_direct_equipment_role_bridge_required_for_green,canonical_archetype_specific,L2_AI_SEMICONDUCTOR_ELECTRONICS,C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH,0,1,+1,"Hanmi/Techwing/YC show direct HBM equipment route + customer/order quality converted into very high MFE, while DI shows theme-only relative strength can become false Green with severe MAE.",false_positive_rate 0.25 -> 0.00 in this loop proxy after capping DI; direct-equipment winners retained; average MAE improves by excluding false-Green representative from promoted set.,R2L12_T01_HANMI_STAGE2_TCBONDER_ORDER_RS|R2L12_T02_TECHWING_STAGE2_HANDLER_RS|R2L12_T03_YC_STAGE2_TESTER_RS_HIGH_MAE|R2L12_T04_DI_STAGE3_FALSE_GREEN_TESTER_THEME,4,4,1,medium,canonical_archetype_shadow_only,not production; post-calibrated residual
```

## 25. Machine-Readable Rows

```jsonl
{"row_type":"price_source_validation","source":"Songdaiki/stock-web","source_url":"https://github.com/Songdaiki/stock-web","manifest_path":"atlas/manifest.json","schema_path":"atlas/schema.json","universe_path":"atlas/universe/all_symbols.csv","manifest_max_date":"2026-02-20","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","calibration_shard_root":"atlas/ohlcv_tradable_by_symbol_year","raw_shard_root":"atlas/ohlcv_raw_by_symbol_year","validation_status":"usable_for_historical_calibration"}
{"row_type":"case","case_id":"R2L12_C07_042700_HANMI_TCBONDER","symbol":"042700","company_name":"한미반도체","round":"R2","loop":"12","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH","fine_archetype_id":"HBM_TCBONDER_DIRECT_ORDER_RELATIVE_STRENGTH","case_type":"structural_success","positive_or_counterexample":"positive","best_trigger":"R2L12_T01_HANMI_STAGE2_TCBONDER_ORDER_RS","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"direct_HBM_equipment_order_route_success_with_late_4B_need","current_profile_verdict":"current_profile_too_late","price_source":"Songdaiki/stock-web","notes":"TC-bonder / HBM packaging equipment demand was already a public order-quality narrative. The price row shows the first decisive gap-up day; this trigger tests whether direct equipment route + relative strength deserved Yellow before strict Green confirmation."}
{"row_type":"case","case_id":"R2L12_C07_089030_TECHWING_HBM_HANDLER","symbol":"089030","company_name":"테크윙","round":"R2","loop":"12","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH","fine_archetype_id":"HBM_TEST_HANDLER_EQUIPMENT_RELATIVE_STRENGTH","case_type":"structural_success","positive_or_counterexample":"positive","best_trigger":"R2L12_T02_TECHWING_STAGE2_HANDLER_RS","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"HBM_handler_relative_strength_success_but_requires_4B_overlay_after_blowoff","current_profile_verdict":"current_profile_correct","price_source":"Songdaiki/stock-web","notes":"HBM test-handler / advanced package inspection route gained public attention with strong relative strength. This is a clean example where equipment-specific path, not just memory-price beta, led the move."}
{"row_type":"case","case_id":"R2L12_C07_232140_YC_TESTER_HIGH_MAE","symbol":"232140","company_name":"와이씨","round":"R2","loop":"12","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH","fine_archetype_id":"HBM_MEMORY_TESTER_DIRECT_CUSTOMER_HIGH_MAE","case_type":"high_mae_success","positive_or_counterexample":"positive","best_trigger":"R2L12_T03_YC_STAGE2_TESTER_RS_HIGH_MAE","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"direct_tester_route_success_with_high_MAE_and_late_green_risk","current_profile_verdict":"current_profile_too_early","price_source":"Songdaiki/stock-web","notes":"Memory tester/HBM tester narrative produced a massive move, but the entry-day low and subsequent whipsaw show why C07 should tolerate high MAE only when direct customer/order quality is explicit."}
{"row_type":"case","case_id":"R2L12_C07_003160_DI_TESTER_THEME_COUNTEREXAMPLE","symbol":"003160","company_name":"디아이","round":"R2","loop":"12","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH","fine_archetype_id":"HBM_TESTER_THEME_WITHOUT_ORDER_CONFIRMATION","case_type":"false_positive_green","positive_or_counterexample":"counterexample","best_trigger":"R2L12_T04_DI_STAGE3_FALSE_GREEN_TESTER_THEME","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"theme_relative_strength_false_green_counterexample","current_profile_verdict":"current_profile_false_positive","price_source":"Songdaiki/stock-web","notes":"Tester/HBM theme momentum was strong, but direct order visibility and durable revision confirmation were weaker than the price move. The path had modest MFE versus severe MAE, making it a C07 false-Green counterexample."}
{"row_type":"trigger","trigger_id":"R2L12_T01_HANMI_STAGE2_TCBONDER_ORDER_RS","case_id":"R2L12_C07_042700_HANMI_TCBONDER","symbol":"042700","company_name":"한미반도체","round":"R2","loop":"12","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH","fine_archetype_id":"HBM_TCBONDER_DIRECT_ORDER_RELATIVE_STRENGTH","sector":"AI·반도체·전자부품","primary_archetype":"HBM equipment order relative strength","loop_objective":"coverage_gap_fill|sector_specific_rule_discovery|canonical_archetype_compression|counterexample_mining|green_strictness_stress_test|4B_non_price_requirement_stress_test|stage2_actionable_bonus_stress_test","trigger_type":"Stage2-Actionable","trigger_date":"2024-02-08","evidence_available_at_that_date":"TC-bonder / HBM packaging equipment demand was already a public order-quality narrative. The price row shows the first decisive gap-up day; this trigger tests whether direct equipment route + relative strength deserved Yellow before strict Green confirmation.","evidence_source":"company disclosure/media/analyst-public narrative; exact production URL enrichment required before promotion; stock-web shard rows 2024-02-08~2024-09-26 inspected","stage2_evidence_fields":["public_event_or_disclosure","customer_or_order_quality","relative_strength","capacity_or_volume_route","early_revision_signal"],"stage3_evidence_fields":["confirmed_revision","multiple_public_sources","financial_visibility","durable_customer_confirmation"],"stage4b_evidence_fields":["valuation_blowoff","positioning_overheat"],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/042/042700/2024.csv","profile_path":"atlas/symbol_profiles/042/042700.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","entry_date":"2024-02-08","entry_price":78500,"MFE_30D_pct":37.32,"MFE_90D_pct":150.0,"MFE_180D_pct":150.0,"MFE_1Y_pct":null,"MFE_2Y_pct":null,"MAE_30D_pct":-9.94,"MAE_90D_pct":-10.32,"MAE_180D_pct":-10.32,"MAE_1Y_pct":null,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-06-14","peak_price":196200,"drawdown_after_peak_pct":-53.47,"green_lateness_ratio":0.45,"four_b_local_peak_proximity":0.93,"four_b_full_window_peak_proximity":1.0,"four_b_timing_verdict":"good_full_window_4B_timing_if_supported_by_valuation_or_positioning_evidence","four_b_evidence_type":["valuation_blowoff","positioning_overheat"],"four_c_protection_label":"not_applicable","trigger_outcome_label":"direct_HBM_equipment_order_route_success_with_late_4B_need","current_profile_verdict":"current_profile_too_late","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"R2L12_042700_20240208_78500","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"R2L12_T02_TECHWING_STAGE2_HANDLER_RS","case_id":"R2L12_C07_089030_TECHWING_HBM_HANDLER","symbol":"089030","company_name":"테크윙","round":"R2","loop":"12","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH","fine_archetype_id":"HBM_TEST_HANDLER_EQUIPMENT_RELATIVE_STRENGTH","sector":"AI·반도체·전자부품","primary_archetype":"HBM equipment order relative strength","loop_objective":"coverage_gap_fill|sector_specific_rule_discovery|canonical_archetype_compression|counterexample_mining|green_strictness_stress_test|4B_non_price_requirement_stress_test|stage2_actionable_bonus_stress_test","trigger_type":"Stage2-Actionable","trigger_date":"2024-02-13","evidence_available_at_that_date":"HBM test-handler / advanced package inspection route gained public attention with strong relative strength. This is a clean example where equipment-specific path, not just memory-price beta, led the move.","evidence_source":"public HBM equipment narrative; stock-web shard rows 2024-02-13~2024-09-26 inspected","stage2_evidence_fields":["public_event_or_disclosure","customer_or_order_quality","relative_strength","capacity_or_volume_route","early_revision_signal"],"stage3_evidence_fields":["confirmed_revision","multiple_public_sources","financial_visibility","repeat_order_or_conversion"],"stage4b_evidence_fields":["valuation_blowoff","positioning_overheat"],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/089/089030/2024.csv","profile_path":"atlas/symbol_profiles/089/089030.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","entry_date":"2024-02-13","entry_price":18690,"MFE_30D_pct":92.62,"MFE_90D_pct":243.98,"MFE_180D_pct":278.81,"MFE_1Y_pct":null,"MFE_2Y_pct":null,"MAE_30D_pct":-6.05,"MAE_90D_pct":-6.05,"MAE_180D_pct":-6.05,"MAE_1Y_pct":null,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-07-11","peak_price":70800,"drawdown_after_peak_pct":-57.63,"green_lateness_ratio":0.34,"four_b_local_peak_proximity":0.95,"four_b_full_window_peak_proximity":1.0,"four_b_timing_verdict":"good_full_window_4B_timing_if_non_price_overheat_confirmed","four_b_evidence_type":["valuation_blowoff","positioning_overheat"],"four_c_protection_label":"not_applicable","trigger_outcome_label":"HBM_handler_relative_strength_success_but_requires_4B_overlay_after_blowoff","current_profile_verdict":"current_profile_correct","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"R2L12_089030_20240213_18690","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"R2L12_T03_YC_STAGE2_TESTER_RS_HIGH_MAE","case_id":"R2L12_C07_232140_YC_TESTER_HIGH_MAE","symbol":"232140","company_name":"와이씨","round":"R2","loop":"12","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH","fine_archetype_id":"HBM_MEMORY_TESTER_DIRECT_CUSTOMER_HIGH_MAE","sector":"AI·반도체·전자부품","primary_archetype":"HBM equipment order relative strength","loop_objective":"coverage_gap_fill|sector_specific_rule_discovery|canonical_archetype_compression|counterexample_mining|green_strictness_stress_test|4B_non_price_requirement_stress_test|stage2_actionable_bonus_stress_test","trigger_type":"Stage2-Actionable","trigger_date":"2024-04-18","evidence_available_at_that_date":"Memory tester/HBM tester narrative produced a massive move, but the entry-day low and subsequent whipsaw show why C07 should tolerate high MAE only when direct customer/order quality is explicit.","evidence_source":"public tester/HBM customer narrative; stock-web shard rows 2024-04-18~2024-07-05 inspected","stage2_evidence_fields":["public_event_or_disclosure","customer_or_order_quality","relative_strength","capacity_or_volume_route"],"stage3_evidence_fields":["multiple_public_sources","financial_visibility"],"stage4b_evidence_fields":["valuation_blowoff","positioning_overheat"],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/232/232140/2024.csv","profile_path":"atlas/symbol_profiles/232/232140.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","entry_date":"2024-04-18","entry_price":9460,"MFE_30D_pct":88.48,"MFE_90D_pct":142.6,"MFE_180D_pct":142.6,"MFE_1Y_pct":null,"MFE_2Y_pct":null,"MAE_30D_pct":-25.48,"MAE_90D_pct":-25.48,"MAE_180D_pct":-25.48,"MAE_1Y_pct":null,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-06-13","peak_price":22950,"drawdown_after_peak_pct":-33.03,"green_lateness_ratio":0.58,"four_b_local_peak_proximity":0.87,"four_b_full_window_peak_proximity":1.0,"four_b_timing_verdict":"high_MAE_success_needs_4B_overlay_after_full_window_peak","four_b_evidence_type":["valuation_blowoff","positioning_overheat"],"four_c_protection_label":"not_applicable","trigger_outcome_label":"direct_tester_route_success_with_high_MAE_and_late_green_risk","current_profile_verdict":"current_profile_too_early","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"R2L12_232140_20240418_9460","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"R2L12_T04_DI_STAGE3_FALSE_GREEN_TESTER_THEME","case_id":"R2L12_C07_003160_DI_TESTER_THEME_COUNTEREXAMPLE","symbol":"003160","company_name":"디아이","round":"R2","loop":"12","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH","fine_archetype_id":"HBM_TESTER_THEME_WITHOUT_ORDER_CONFIRMATION","sector":"AI·반도체·전자부품","primary_archetype":"HBM equipment order relative strength","loop_objective":"coverage_gap_fill|sector_specific_rule_discovery|canonical_archetype_compression|counterexample_mining|green_strictness_stress_test|4B_non_price_requirement_stress_test|stage2_actionable_bonus_stress_test","trigger_type":"Stage3-Green-Candidate","trigger_date":"2024-04-15","evidence_available_at_that_date":"Tester/HBM theme momentum was strong, but direct order visibility and durable revision confirmation were weaker than the price move. The path had modest MFE versus severe MAE, making it a C07 false-Green counterexample.","evidence_source":"public tester/HBM theme narrative; stock-web shard rows 2024-04-15~2024-09-03 inspected","stage2_evidence_fields":["public_event_or_disclosure","relative_strength"],"stage3_evidence_fields":["multiple_public_sources"],"stage4b_evidence_fields":["valuation_blowoff","positioning_overheat","price_only_local_peak"],"stage4c_evidence_fields":["thesis_evidence_broken"],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/003/003160/2024.csv","profile_path":"atlas/symbol_profiles/003/003160.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","entry_date":"2024-04-15","entry_price":22650,"MFE_30D_pct":13.91,"MFE_90D_pct":35.98,"MFE_180D_pct":35.98,"MFE_1Y_pct":null,"MFE_2Y_pct":null,"MAE_30D_pct":-27.59,"MAE_90D_pct":-44.19,"MAE_180D_pct":-44.19,"MAE_1Y_pct":null,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-06-27","peak_price":30800,"drawdown_after_peak_pct":-58.96,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":0.41,"four_b_full_window_peak_proximity":1.0,"four_b_timing_verdict":"price_only_local_4B_too_early_until_non_price_order_or_revision_slowdown_exists","four_b_evidence_type":["price_only","positioning_overheat"],"four_c_protection_label":"thesis_break_watch_only","trigger_outcome_label":"theme_relative_strength_false_green_counterexample","current_profile_verdict":"current_profile_false_positive","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"R2L12_003160_20240415_22650","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"R2L12_T01_HANMI_4B_TCBONDER_ORDER_RS","case_id":"R2L12_C07_042700_HANMI_TCBONDER","symbol":"042700","company_name":"한미반도체","round":"R2","loop":"12","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH","fine_archetype_id":"HBM_TCBONDER_DIRECT_ORDER_RELATIVE_STRENGTH","sector":"AI·반도체·전자부품","primary_archetype":"HBM equipment order relative strength","loop_objective":"4B_non_price_requirement_stress_test","trigger_type":"Stage4B-Overlay","trigger_date":"2024-06-14","evidence_available_at_that_date":"Observed full-window price peak. Treat as full 4B only if valuation/revision/positioning evidence exists; price-only local top remains overlay-only.","evidence_source":"stock-web OHLC peak plus public valuation/positioning narrative enrichment required","stage2_evidence_fields":[],"stage3_evidence_fields":["confirmed_revision","multiple_public_sources","financial_visibility","durable_customer_confirmation"],"stage4b_evidence_fields":["valuation_blowoff","positioning_overheat","price_only_local_peak"],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/042/042700/2024.csv","profile_path":"atlas/symbol_profiles/042/042700.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","entry_date":"2024-06-14","entry_price":196200,"MFE_30D_pct":0.0,"MFE_90D_pct":0.0,"MFE_180D_pct":0.0,"MFE_1Y_pct":null,"MFE_2Y_pct":null,"MAE_30D_pct":-26.73,"MAE_90D_pct":-53.47,"MAE_180D_pct":-53.47,"MAE_1Y_pct":null,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-06-14","peak_price":196200,"drawdown_after_peak_pct":-53.47,"green_lateness_ratio":0.45,"four_b_local_peak_proximity":0.93,"four_b_full_window_peak_proximity":1.0,"four_b_timing_verdict":"good_full_window_4B_timing_if_supported_by_valuation_or_positioning_evidence","four_b_evidence_type":["valuation_blowoff","positioning_overheat","price_only"],"four_c_protection_label":"not_applicable","trigger_outcome_label":"4B_overlay_success","current_profile_verdict":"current_profile_4B_too_late","calibration_usable":true,"forward_window_trading_days":90,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"R2L12_042700_20240614_196200","dedupe_for_aggregate":false,"aggregate_group_role":"4B_overlay_only","is_new_independent_case":false,"reuse_reason":"same case 4B timing overlay; not representative aggregate row","independent_evidence_weight":0.25,"do_not_count_as_new_case":true}
{"row_type":"trigger","trigger_id":"R2L12_T02_TECHWING_4B_HANDLER_RS","case_id":"R2L12_C07_089030_TECHWING_HBM_HANDLER","symbol":"089030","company_name":"테크윙","round":"R2","loop":"12","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH","fine_archetype_id":"HBM_TEST_HANDLER_EQUIPMENT_RELATIVE_STRENGTH","sector":"AI·반도체·전자부품","primary_archetype":"HBM equipment order relative strength","loop_objective":"4B_non_price_requirement_stress_test","trigger_type":"Stage4B-Overlay","trigger_date":"2024-07-11","evidence_available_at_that_date":"Observed full-window price peak. Treat as full 4B only if valuation/revision/positioning evidence exists; price-only local top remains overlay-only.","evidence_source":"stock-web OHLC peak plus public valuation/positioning narrative enrichment required","stage2_evidence_fields":[],"stage3_evidence_fields":["confirmed_revision","multiple_public_sources","financial_visibility","repeat_order_or_conversion"],"stage4b_evidence_fields":["valuation_blowoff","positioning_overheat","price_only_local_peak"],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/089/089030/2024.csv","profile_path":"atlas/symbol_profiles/089/089030.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","entry_date":"2024-07-11","entry_price":70800,"MFE_30D_pct":0.0,"MFE_90D_pct":0.0,"MFE_180D_pct":0.0,"MFE_1Y_pct":null,"MFE_2Y_pct":null,"MAE_30D_pct":-28.82,"MAE_90D_pct":-57.63,"MAE_180D_pct":-57.63,"MAE_1Y_pct":null,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-07-11","peak_price":70800,"drawdown_after_peak_pct":-57.63,"green_lateness_ratio":0.34,"four_b_local_peak_proximity":0.95,"four_b_full_window_peak_proximity":1.0,"four_b_timing_verdict":"good_full_window_4B_timing_if_non_price_overheat_confirmed","four_b_evidence_type":["valuation_blowoff","positioning_overheat","price_only"],"four_c_protection_label":"not_applicable","trigger_outcome_label":"4B_overlay_success","current_profile_verdict":"current_profile_correct","calibration_usable":true,"forward_window_trading_days":90,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"R2L12_089030_20240711_70800","dedupe_for_aggregate":false,"aggregate_group_role":"4B_overlay_only","is_new_independent_case":false,"reuse_reason":"same case 4B timing overlay; not representative aggregate row","independent_evidence_weight":0.25,"do_not_count_as_new_case":true}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"R2L12_C07_042700_HANMI_TCBONDER","trigger_id":"R2L12_T01_HANMI_STAGE2_TCBONDER_ORDER_RS","symbol":"042700","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH","raw_component_scores_before":{"contract_score":54,"backlog_visibility_score":48,"margin_bridge_score":45,"revision_score":52,"relative_strength_score":88,"customer_quality_score":78,"policy_or_regulatory_score":0,"valuation_repricing_score":70,"execution_risk_score":30,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0,"order_intake_quality_score":82,"capacity_or_shipment_score":74,"positioning_overheat_score":58,"thesis_break_score":0},"weighted_score_before":84.0,"stage_label_before":"Stage3-Yellow","raw_component_scores_after":{"contract_score":54,"backlog_visibility_score":48,"margin_bridge_score":45,"revision_score":55,"relative_strength_score":92,"customer_quality_score":82,"policy_or_regulatory_score":0,"valuation_repricing_score":70,"execution_risk_score":28,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0,"order_intake_quality_score":87,"capacity_or_shipment_score":74,"positioning_overheat_score":58,"thesis_break_score":0},"weighted_score_after":89.0,"stage_label_after":"Stage3-Green-Shadow","changed_components":["relative_strength_score","customer_quality_score","order_intake_quality_score","revision_score","execution_risk_score"],"component_delta_explanation":"C07 shadow profile rewards direct HBM equipment/customer/order-quality evidence but caps theme-only relative strength when revision/order evidence is thin.","MFE_90D_pct":150.0,"MAE_90D_pct":-10.32,"score_return_alignment_label":"direct_HBM_equipment_order_route_success_with_late_4B_need","current_profile_verdict":"current_profile_too_late"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"R2L12_C07_089030_TECHWING_HBM_HANDLER","trigger_id":"R2L12_T02_TECHWING_STAGE2_HANDLER_RS","symbol":"089030","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH","raw_component_scores_before":{"contract_score":42,"backlog_visibility_score":40,"margin_bridge_score":38,"revision_score":48,"relative_strength_score":86,"customer_quality_score":72,"policy_or_regulatory_score":0,"valuation_repricing_score":66,"execution_risk_score":34,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0,"order_intake_quality_score":70,"capacity_or_shipment_score":78,"positioning_overheat_score":52,"thesis_break_score":0},"weighted_score_before":82.0,"stage_label_before":"Stage3-Yellow","raw_component_scores_after":{"contract_score":42,"backlog_visibility_score":40,"margin_bridge_score":38,"revision_score":51,"relative_strength_score":91,"customer_quality_score":72,"policy_or_regulatory_score":0,"valuation_repricing_score":66,"execution_risk_score":33,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0,"order_intake_quality_score":74,"capacity_or_shipment_score":83,"positioning_overheat_score":52,"thesis_break_score":0},"weighted_score_after":88.0,"stage_label_after":"Stage3-Green-Shadow","changed_components":["relative_strength_score","capacity_or_shipment_score","order_intake_quality_score","revision_score","execution_risk_score"],"component_delta_explanation":"C07 shadow profile rewards direct HBM equipment/customer/order-quality evidence but caps theme-only relative strength when revision/order evidence is thin.","MFE_90D_pct":243.98,"MAE_90D_pct":-6.05,"score_return_alignment_label":"HBM_handler_relative_strength_success_but_requires_4B_overlay_after_blowoff","current_profile_verdict":"current_profile_correct"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"R2L12_C07_232140_YC_TESTER_HIGH_MAE","trigger_id":"R2L12_T03_YC_STAGE2_TESTER_RS_HIGH_MAE","symbol":"232140","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH","raw_component_scores_before":{"contract_score":38,"backlog_visibility_score":34,"margin_bridge_score":28,"revision_score":42,"relative_strength_score":82,"customer_quality_score":68,"policy_or_regulatory_score":0,"valuation_repricing_score":64,"execution_risk_score":52,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0,"order_intake_quality_score":64,"capacity_or_shipment_score":72,"positioning_overheat_score":58,"thesis_break_score":0},"weighted_score_before":80.0,"stage_label_before":"Stage3-Yellow","raw_component_scores_after":{"contract_score":38,"backlog_visibility_score":34,"margin_bridge_score":28,"revision_score":42,"relative_strength_score":85,"customer_quality_score":72,"policy_or_regulatory_score":0,"valuation_repricing_score":64,"execution_risk_score":56,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0,"order_intake_quality_score":64,"capacity_or_shipment_score":75,"positioning_overheat_score":64,"thesis_break_score":0},"weighted_score_after":84.0,"stage_label_after":"Stage3-Yellow-High-MAE-Guarded","changed_components":["customer_quality_score","relative_strength_score","capacity_or_shipment_score","execution_risk_score","positioning_overheat_score"],"component_delta_explanation":"C07 shadow profile rewards direct HBM equipment/customer/order-quality evidence but caps theme-only relative strength when revision/order evidence is thin.","MFE_90D_pct":142.6,"MAE_90D_pct":-25.48,"score_return_alignment_label":"direct_tester_route_success_with_high_MAE_and_late_green_risk","current_profile_verdict":"current_profile_too_early"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"R2L12_C07_003160_DI_TESTER_THEME_COUNTEREXAMPLE","trigger_id":"R2L12_T04_DI_STAGE3_FALSE_GREEN_TESTER_THEME","symbol":"003160","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH","raw_component_scores_before":{"contract_score":12,"backlog_visibility_score":18,"margin_bridge_score":20,"revision_score":36,"relative_strength_score":86,"customer_quality_score":48,"policy_or_regulatory_score":0,"valuation_repricing_score":74,"execution_risk_score":66,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0,"order_intake_quality_score":34,"capacity_or_shipment_score":44,"positioning_overheat_score":78,"thesis_break_score":0},"weighted_score_before":88.0,"stage_label_before":"Stage3-Green","raw_component_scores_after":{"contract_score":4,"backlog_visibility_score":18,"margin_bridge_score":20,"revision_score":28,"relative_strength_score":86,"customer_quality_score":34,"policy_or_regulatory_score":0,"valuation_repricing_score":56,"execution_risk_score":74,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0,"order_intake_quality_score":22,"capacity_or_shipment_score":44,"positioning_overheat_score":86,"thesis_break_score":0},"weighted_score_after":70.0,"stage_label_after":"Stage2-Watch","changed_components":["contract_score","customer_quality_score","order_intake_quality_score","revision_score","valuation_repricing_score","execution_risk_score","positioning_overheat_score"],"component_delta_explanation":"C07 shadow profile rewards direct HBM equipment/customer/order-quality evidence but caps theme-only relative strength when revision/order evidence is thin.","MFE_90D_pct":35.98,"MAE_90D_pct":-44.19,"score_return_alignment_label":"theme_relative_strength_false_green_counterexample","current_profile_verdict":"current_profile_false_positive"}
{"row_type":"residual_contribution","round":"R2","loop":"12","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH","new_independent_case_count":4,"reused_case_count":0,"new_symbol_count":4,"new_trigger_family_count":4,"tested_existing_calibrated_axes":["stage2_actionable_evidence_bonus","stage3_yellow_total_min","stage3_green_total_min","stage3_green_revision_min","stage3_cross_evidence_green_buffer","price_only_blowoff_blocks_positive_stage","full_4b_requires_non_price_evidence","hard_4c_thesis_break_routes_to_4c"],"residual_error_types_found":["theme_only_relative_strength_false_green","high_MAE_success_requires_direct_customer_order_bridge","late_4B_after_HBM_equipment_blowoff","green_strictness_too_late_for_direct_equipment_winner"],"loop_contribution_label":"canonical_archetype_rule_candidate","do_not_propose_new_weight_delta":false}
```

## 26. Deferred Coding Agent Handoff Prompt

### Purpose

You are now in the repository implementation phase. The attached Markdown files are v12 post-calibrated residual research outputs produced using the Songdaiki/stock-web OHLC atlas.

These MDs are not live candidate research. They are historical calibration research designed to extend the already-applied e2r_2_1_stock_web_calibrated profile.

Do not blindly apply every shadow row. Ingest the machine-readable rows and update the sector/canonical-archetype calibration ledger.

### Price source context

- Primary historical price source used by the research MD: Songdaiki/stock-web.
- Price basis: tradable_raw.
- Price adjustment status: raw_unadjusted_marcap.
- Price shard pattern: atlas/ohlcv_tradable_by_symbol_year/<prefix>/<ticker>/<year>.csv.
- Symbol profile pattern: atlas/symbol_profiles/<prefix>/<ticker>.json.

### Rules

- Use only calibration_usable=true rows for quantitative calibration.
- Do not count reused cases as new independent evidence unless independent_evidence_weight > 0.
- Do not treat schema_rematerialization_only or duplicate_low_value_loop as new evidence.
- Do not apply global deltas unless multiple large_sector_id values support the same direction.
- Prefer sector_specific or canonical_archetype_specific shadow profiles.
- Positive score promotion requires non-price evidence and clean 180D MFE/MAE.
- 4B rows are overlay/risk calibration only.
- 4C rows are thesis-break/protection calibration only.
- price-only rows cannot promote Stage2/Stage3.
- If a v12 MD weakens an already applied axis, log it as residual counterexample rather than immediately reverting.
- Production scoring must not change unless the user explicitly asks for another promotion batch.

### Expected repository tasks

1. Parse case / trigger / score_simulation / shadow_weight / residual_contribution rows.
2. Validate stock-web price source fields.
3. Validate large_sector_id and canonical_archetype_id.
4. Validate novelty and reuse fields.
5. Deduplicate same_entry_group_id and reused cases.
6. Aggregate by large_sector_id and canonical_archetype_id.
7. Update sector_shadow_profile and archetype_shadow_profile only.
8. Preserve global calibrated profile unless explicitly promoted.
9. Report new independent cases, counterexamples, and residual error types.
10. Add tests that duplicate low-value loops cannot change weights.

### Expected output

- Concise implementation summary.
- Rows accepted/rejected.
- New sector/canonical archetype coverage.
- Existing axis strengthened/weakened/kept.
- No investment recommendation language.

## 27. Next Round State

```text
completed_round = R2
completed_loop = 12
next_round = R3
next_loop = 12
round_schedule_status = valid
round_sector_consistency = pass
```

## 28. Source Notes

```text
price_atlas_repo = https://github.com/Songdaiki/stock-web
manifest = atlas/manifest.json
schema = atlas/schema.json
universe = atlas/universe/all_symbols.csv
price_basis = tradable_raw
price_adjustment_status = raw_unadjusted_marcap
stock_web_manifest_max_date = 2026-02-20

Inspected profile paths:
- atlas/symbol_profiles/042/042700.json
- atlas/symbol_profiles/089/089030.json
- atlas/symbol_profiles/232/232140.json
- atlas/symbol_profiles/003/003160.json

Inspected price shard paths:
- atlas/ohlcv_tradable_by_symbol_year/042/042700/2024.csv
- atlas/ohlcv_tradable_by_symbol_year/089/089030/2024.csv
- atlas/ohlcv_tradable_by_symbol_year/232/232140/2024.csv
- atlas/ohlcv_tradable_by_symbol_year/003/003160/2024.csv
```
