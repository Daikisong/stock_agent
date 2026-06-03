# E2R Stock-Web Historical Calibration / Sector-Archetype Residual Research Round

## 0. Research Metadata

```text
research_session = post_calibrated_sector_archetype_residual_research
mode = historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12
round = R11
loop = 10
large_sector_id = L10_POLICY_EVENT_CROSS_REDTEAM_MISC
canonical_archetype_id = C31_POLICY_SUBSIDY_LEGISLATION_EVENT
fine_archetype_id = NUCLEAR_RESOURCE_POLICY_EVENT_PASS_THROUGH_VS_PRICE_ONLY_THEME
loop_objective = counterexample_mining | residual_false_positive_mining | 4B_non_price_requirement_stress_test | 4C_thesis_break_timing_test | sector_specific_rule_discovery | canonical_archetype_compression | coverage_gap_fill
output_file = e2r_stock_web_v12_residual_round_R11_loop_10_L10_POLICY_EVENT_CROSS_REDTEAM_MISC_C31_POLICY_SUBSIDY_LEGISLATION_EVENT_research.md
production_scoring_changed = false
shadow_weight_only = true
```

This file is a standalone v12 residual calibration research artifact. It is not a live stock screen, not an investment recommendation, and not a repository patch.

## 1. Current Calibrated Profile Assumption

```text
current_default_profile_proxy = e2r_2_1_stock_web_calibrated_proxy
rollback_reference_profile_id = e2r_2_0_baseline_reference
stage2_actionable_evidence_bonus = +2.0
stage3_yellow_total_min = 75.0
stage3_green_total_min = 87.0
stage3_green_revision_min = 55.0
stage3_cross_evidence_green_buffer = +1.5
price_only_blowoff_blocks_positive_stage = true
full_4b_requires_non_price_evidence = true
hard_4c_thesis_break_routes_to_4c = true
```

The research does not re-propose these global axes. It stress-tests whether C31 policy-event cases need a narrower cap or bridge rule: when a government headline is not connected to direct beneficiary economics, it should remain an option-value watch or 4B/4C overlay rather than a Green promotion.

## 2. Round / Large Sector / Canonical Archetype Scope

| field | value |
|---|---|
| round | R11 정책·지정학·재난·이벤트 |
| large_sector_id | L10_POLICY_EVENT_CROSS_REDTEAM_MISC |
| canonical_archetype_id | C31_POLICY_SUBSIDY_LEGISLATION_EVENT |
| fine_archetype_id | NUCLEAR_RESOURCE_POLICY_EVENT_PASS_THROUGH_VS_PRICE_ONLY_THEME |
| research question | Does a policy/project event translate into contract, margin, and revision evidence, or does it remain price-only policy beta? |

## 3. Previous Coverage / Duplicate Avoidance Check

Accessible calibration artifact summary showed all R1-R13 sectors covered through prior loops, but R11 policy-event residuals were not directly visible in the accessible `md_registry` slice used for this loop. Prior global axes were already applied from cross-round evidence and are treated as locked background assumptions.

Duplicate avoidance decision:

```text
repeated_same_symbol_same_trigger_date = false
same_R1_R2_HBM_grid_defense_repetition = false
schema_rematerialization_only = false
new_symbol_count = 3
new_independent_case_ratio = 1.00
```

## 4. Stock-Web OHLC Input / Price Source Validation

Stock-Web manifest was checked for this run.

```text
source = Songdaiki/stock-web
source_name = FinanceData/marcap
price_basis = tradable_raw
price_adjustment_status = raw_unadjusted_marcap
min_date = 1995-05-02
max_date = 2026-02-20
tradable_row_count = 14354401
raw_row_count = 15214118
symbol_count = 5414
active_like_symbol_count = 2868
inactive_or_delisted_like_symbol_count = 2546
markets = KONEX | KOSDAQ | KOSDAQ GLOBAL | KOSPI
calibration_shard_root = atlas/ohlcv_tradable_by_symbol_year
raw_shard_root = atlas/ohlcv_raw_by_symbol_year
schema_path = atlas/schema.json
universe_path = atlas/universe/all_symbols.csv
```

Schema basis:

```text
tradable_shard_columns = d,o,h,l,c,v,a,mc,s,m
MFE_N_pct = (max high from entry_date through N tradable rows / entry_price - 1) * 100
MAE_N_pct = (min low from entry_date through N tradable rows / entry_price - 1) * 100
calibration_usable requires entry row, positive OHLCV, 180 forward tradable days, and no 180D corporate-action contamination.
```

## 5. Historical Eligibility Gate

| symbol | company | profile_path | entry window status | corporate-action 180D status | forward 180D status | calibration_usable |
|---|---|---|---|---|---|---|
| 034020 | 두산에너빌리티 | atlas/symbol_profiles/034/034020.json | entry row exists | clean_180D_window; profile CA dates are 2019-05-29, 2020-02-18, 2020-12-24 | available | true |
| 052690 | 한전기술 | atlas/symbol_profiles/052/052690.json | entry row exists | clean_180D_window; profile CA list empty | available | true |
| 036460 | 한국가스공사 | atlas/symbol_profiles/036/036460.json | entry row exists | clean_180D_window; profile CA list empty | available | true |

## 6. Canonical Archetype Compression Map

| case cluster | canonical_archetype_id | fine_archetype_id | compression decision |
|---|---|---|---|
| Czech nuclear preferred-bidder event with beneficiary chain | C31_POLICY_SUBSIDY_LEGISLATION_EVENT | CZECH_NUCLEAR_POLICY_PROJECT_PASS_THROUGH | Keep as C31, not C04, because this loop tests policy/project-event gating rather than nuclear construction execution depth. |
| East Sea oil/gas drilling approval and resource option theme | C31_POLICY_SUBSIDY_LEGISLATION_EVENT | RESOURCE_EXPLORATION_POLICY_OPTION_VALUE_THEME | Keep as C31 because the primary trigger is presidential/government approval and exploration optionality, not confirmed commodity spread. |
| Legal/appeal overlay after project selection | C31_POLICY_SUBSIDY_LEGISLATION_EVENT | PROJECT_EVENT_LEGAL_DELAY_4B_4C_OVERLAY | Retain as C31 overlay; do not train positive entry weights. |

## 7. Case Selection Summary

| case_id | symbol | company | role | trigger family | positive_or_counterexample | short thesis |
|---|---:|---|---|---|---|---|
| R11L10C31_034020_20240718 | 034020 | 두산에너빌리티 | high_mae_success | preferred_bidder_policy_project | positive | Czech nuclear preferred-bidder headline initially whipsawed, but direct equipment/supplier pass-through kept later upside alive. |
| R11L10C31_052690_20240718 | 052690 | 한전기술 | failed_rerating | preferred_bidder_policy_project_without_revision_bridge | counterexample | Same Czech policy/project headline, but engineering beneficiary economics did not close fast enough; event-day peak dominated the 180D window. |
| R11L10C31_036460_20240603 | 036460 | 한국가스공사 | price_moved_without_evidence | resource_exploration_policy_approval | counterexample / 4B | Oil/gas reserve approval created a large headline rally before commercial proof; the local/full peak came early and reversed sharply. |

## 8. Positive vs Counterexample Balance

```text
positive_case_count = 1
counterexample_count = 2
4B_case_count = 1
4C_case_count = 1
calibration_usable_case_count = 3
representative_trigger_count = 3
```

The loop is counterexample-heavy by design. C31 already has a natural tendency to over-score policy optionality. The useful contribution is to separate a direct-beneficiary project event from a price-only policy headline.

## 9. Evidence Source Map

| case_id | evidence date | evidence source | evidence available at trigger date | stage2 evidence | stage3 evidence | 4B/4C evidence |
|---|---|---|---|---|---|---|
| R11L10C31_034020_20240718 | 2024-07-17/18 | Reuters report: KHNP selected as Czech preferred bidder; related Korean nuclear names gained. | yes | public_event_or_disclosure, policy_or_regulatory_optionality, customer_or_order_quality | partial margin/contract visibility only; not immediate Green | later legal appeal and project delay risk watch |
| R11L10C31_052690_20240718 | 2024-07-17/18 | Same Czech preferred-bidder event. | yes | public_event_or_disclosure, policy_or_regulatory_optionality | weak confirmed_revision and weak margin bridge during 180D | legal_or_regulatory_block, price_only_local_peak |
| R11L10C31_036460_20240603 | 2024-06-03 | Reuters and WSJ: Korean president approved exploration of possible East Sea oil/gas reserves; Korea Gas shares surged. | yes | public_event_or_disclosure, policy_or_regulatory_optionality, resource_optionality | no confirmed commercial reserve / no revision bridge at trigger | price_only_local_peak, explicit_event_cap, thesis_evidence_broken_watch |

External source notes: Reuters reported Korea’s KHNP selection as preferred bidder for the Czech nuclear project on 2024-07-17, with related Korean nuclear stocks moving; Reuters also reported Korea’s 2024-06-03 oil/gas exploration approval and the uncertainty around commercial viability. WSJ separately noted Korea Gas’ sharp rally on the drilling approval.

## 10. Price Data Source Map

| symbol | entry_date | price_shard_path | profile_path | price_basis | adjustment | manifest max date |
|---:|---|---|---|---|---|---|
| 034020 | 2024-07-18 | atlas/ohlcv_tradable_by_symbol_year/034/034020/2024.csv; 2025.csv | atlas/symbol_profiles/034/034020.json | tradable_raw | raw_unadjusted_marcap | 2026-02-20 |
| 052690 | 2024-07-18 | atlas/ohlcv_tradable_by_symbol_year/052/052690/2024.csv; 2025.csv | atlas/symbol_profiles/052/052690.json | tradable_raw | raw_unadjusted_marcap | 2026-02-20 |
| 036460 | 2024-06-03 | atlas/ohlcv_tradable_by_symbol_year/036/036460/2024.csv; 2025.csv | atlas/symbol_profiles/036/036460.json | tradable_raw | raw_unadjusted_marcap | 2026-02-20 |

## 11. Case-by-Case Trigger Grid

| trigger_id | case_id | trigger_type | trigger_date | entry_date | entry_price | evidence fields | current profile verdict | aggregate role |
|---|---|---|---|---|---:|---|---|---|
| R11C31_034020_T1_STAGE2 | R11L10C31_034020_20240718 | Stage2-Actionable | 2024-07-17 | 2024-07-18 | 21000 | public_event_or_disclosure; policy_or_regulatory_optionality; customer_or_order_quality | current_profile_too_late | representative |
| R11C31_034020_T2_4B | R11L10C31_034020_20240718 | 4B-overlay | 2025-02-18 | 2025-02-18 | 30300 | valuation_blowoff; positioning_overheat; revision_watch | current_profile_4B_too_late | 4B_overlay_only |
| R11C31_052690_T1_STAGE2 | R11L10C31_052690_20240718 | Stage2-Actionable | 2024-07-17 | 2024-07-18 | 82000 | public_event_or_disclosure; policy_or_regulatory_optionality | current_profile_false_positive | representative |
| R11C31_052690_T2_4C | R11L10C31_052690_20240718 | 4C-watch | 2024-10-30 | 2024-10-31 | 68800 | legal_or_regulatory_block; project delay appeal | current_profile_4C_too_late | 4C_overlay_only |
| R11C31_036460_T1_STAGE2 | R11L10C31_036460_20240603 | Stage2-Policy-Option | 2024-06-03 | 2024-06-03 | 38700 | public_event_or_disclosure; policy_or_regulatory_optionality; resource_optionality | current_profile_false_positive | representative |
| R11C31_036460_T2_4B | R11L10C31_036460_20240603 | 4B-overlay | 2024-06-20 | 2024-06-20 | 63500 | price_only_local_peak; valuation_blowoff; explicit_event_cap | current_profile_correct | 4B_overlay_only |

## 12. Trigger-Level OHLC Backtest Tables

### 12.1 Representative trigger rows

| trigger_id | symbol | entry_date | entry_price | MFE_30D_pct | MAE_30D_pct | MFE_90D_pct | MAE_90D_pct | MFE_180D_pct | MAE_180D_pct | peak_date | peak_price | drawdown_after_peak_pct | outcome |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---|---:|---:|---|
| R11C31_034020_T1_STAGE2 | 034020 | 2024-07-18 | 21000 | 19.05 | -27.86 | 19.05 | -27.86 | 47.14 | -27.86 | 2025-02-19 | 30900 | -35.40 | high_mae_success |
| R11C31_052690_T1_STAGE2 | 052690 | 2024-07-18 | 82000 | 19.63 | -24.88 | 19.63 | -24.88 | 19.63 | -39.27 | 2024-07-18 | 98100 | -49.24 | failed_rerating |
| R11C31_036460_T1_STAGE2 | 036460 | 2024-06-03 | 38700 | 66.67 | -23.26 | 66.67 | -23.26 | 66.67 | -23.51 | 2024-06-20 | 64500 | -54.11 | price_moved_without_evidence |

### 12.2 Overlay trigger rows

| trigger_id | symbol | trigger_type | entry_date | entry_price | local/full peak relation | verdict |
|---|---:|---|---|---:|---|---|
| R11C31_034020_T2_4B | 034020 | 4B-overlay | 2025-02-18 | 30300 | near full-window peak 30900 | good_full_window_4B_timing but late; non-price overheat/revision watch needed |
| R11C31_052690_T2_4C | 052690 | 4C-watch | 2024-10-31 | 68800 | after event-day peak, before December drawdown | legal delay watch should cap Green earlier |
| R11C31_036460_T2_4B | 036460 | 4B-overlay | 2024-06-20 | 63500 | near full-window peak 64500 | excellent local/full 4B timing if explicit event cap used |

## 13. Current Calibrated Profile Stress Test

| case_id | current profile behavior | path verdict | calibrated-axis status |
|---|---|---|---|
| R11L10C31_034020_20240718 | Might keep at Stage2/Yellow because Green revision gate waits for harder contract/margin evidence. | Too conservative if it treats all policy event risk as equal; 180D MFE eventually +47.14 despite high MAE. | existing_axis_kept; new C31 bridge needed to distinguish direct supplier pass-through. |
| R11L10C31_052690_20240718 | Could over-promote if policy score + relative strength bridges to Green without revision. | False positive: event-day peak dominated; 180D MAE -39.27. | existing_axis_strengthened for C31 Green revision/margin bridge only. |
| R11L10C31_036460_20240603 | Price-only guard should block positive promotion, but policy option score can still overstate Stage2 if uncapped. | Huge MFE but also headline-only blowoff and -54.11 drawdown after peak. | existing_axis_strengthened: full 4B needs non-price/event-cap evidence; price-only is not positive training. |

## 14. Stage2 / Yellow / Green Comparison

| case_id | Stage2 entry | hypothetical Yellow/Green handling | green_lateness_ratio | interpretation |
|---|---|---|---:|---|
| R11L10C31_034020_20240718 | 21000 | Green should wait for margin/revision, but Yellow should remain available because beneficiary chain is direct. | not_applicable | No confirmed Green trigger in this loop; Yellow is the right holding pen. |
| R11L10C31_052690_20240718 | 82000 | Green cap required until revision/margin bridge appears. | not_applicable | Event-day upside was already mostly consumed. |
| R11L10C31_036460_20240603 | 38700 | Stage2 policy-option only; no Yellow/Green without drilling/commercial confirmation. | not_applicable | Outcome is a 4B/4C overlay case, not positive promotion. |

## 15. 4B Local vs Full-window Timing Audit

| trigger_id | symbol | Stage2 price | 4B price | local peak | full window peak | local proximity | full proximity | evidence type | timing verdict |
|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| R11C31_034020_T2_4B | 034020 | 21000 | 30300 | 30900 | 30900 | 0.94 | 0.94 | valuation_blowoff, positioning_overheat, revision_watch | good_full_window_4B_timing_but_late |
| R11C31_052690_T2_4C | 052690 | 82000 | 68800 | 98100 | 98100 | -0.84 | -0.84 | legal_or_regulatory_block, project_delay | not_4B; 4C/watch cap |
| R11C31_036460_T2_4B | 036460 | 38700 | 63500 | 64500 | 64500 | 0.96 | 0.96 | explicit_event_cap, price_only_local_peak, valuation_blowoff | good_full_window_4B_timing if event-cap evidence is counted |

## 16. 4C Protection Audit

| case_id | 4C / thesis-break label | evidence | protection result |
|---|---|---|---|
| R11L10C31_034020_20240718 | thesis_break_watch_only | legal appeals and project finalization risk, but later price recovered into 2025. | Do not hard 4C; use 4B/watch overlay. |
| R11L10C31_052690_20240718 | hard_4c_late | legal appeal/project delay risk after event-day peak and no revision bridge. | 4C/watch would have reduced exposure before December/April lows. |
| R11L10C31_036460_20240603 | hard_4c_success_if_event_cap_used | commercial reserve was not proved at headline date; price-only theme reversed materially. | Event-cap 4B/4C watch near 2024-06-20 peak would have protected most drawdown. |

## 17. Sector-Specific Rule Candidate

```text
rule_id = L10_C31_POLICY_EVENT_EXECUTION_BRIDGE_CAP
rule_scope = sector_specific
axis = policy_event_positive_promotion_cap
baseline_value = no_C31_specific_cap
candidate_value = cap_policy_event_without_execution_bridge_at_Stage2_or_Yellow
```

Candidate rule:

> In L10/C31, a policy/subsidy/legislation/project headline may raise Stage2 option value, but it cannot promote to Stage3-Green unless at least two non-price execution bridge fields are present: direct beneficiary role, signed/selected bidder status, contract or order economics, margin/revision bridge, customer/funding commitment, or commercialization milestone. Resource exploration headlines without commercial proof remain policy-option or 4B/4C watch.

Expected effect:

- Keeps Doosan Enerbility as a Stage2/Yellow high-MAE success, not an immediate Green.
- Caps KEPCO E&C-style same-headline false Green when revision/margin bridge is missing.
- Treats Korea Gas’ resource exploration spike as 4B/4C overlay, not positive entry training.

## 18. Canonical-Archetype Rule Candidate

```text
rule_id = C31_POLICY_EVENT_DIRECT_BENEFICIARY_BRIDGE
rule_scope = canonical_archetype_specific
axis = direct_beneficiary_execution_bridge_score
baseline_value = 0
candidate_value = +2 for direct beneficiary + execution bridge; -3 cap for policy-only headline without bridge
confidence = low_to_medium
proposal_type = canonical_archetype_shadow_only
```

C31 needs a fork:

1. **Direct pass-through policy project**: selected bidder / supplier chain / contract path. This can earn Stage2-Actionable and possibly Yellow.
2. **Policy-option headline**: exploration, subsidy, legislation, or political announcement with uncertain beneficiary economics. This is capped until revision/contract evidence appears.
3. **Event-cap / legal-delay overlay**: use for 4B/4C risk, not positive promotion.

## 19. Before / After Backtest Comparison

| profile_id | profile_scope | hypothesis | selected entry count | avg MFE_90D | avg MAE_90D | avg MFE_180D | avg MAE_180D | false_positive_rate | verdict |
|---|---|---|---:|---:|---:|---:|---:|---:|---|
| P0 e2r_2_1_stock_web_calibrated_proxy | current | global calibrated profile only | 3 | 35.12 | -25.33 | 44.48 | -30.21 | 0.67 | Too blunt for policy-event heterogeneity. |
| P0b e2r_2_0_baseline_reference | rollback | looser Green without calibrated guardrails | 3 | 35.12 | -25.33 | 44.48 | -30.21 | 0.67 | Worse; would over-train headline beta. |
| P1 L10 sector candidate | sector_specific | cap policy-only events; require execution bridge | 2 positive/Yellow eligible, 1 overlay-only | 19.34 | -26.37 | 33.39 | -33.56 | 0.50 | Better risk separation; still high MAE in nuclear names. |
| P2 C31 archetype candidate | canonical_archetype_specific | direct-beneficiary bridge + event-cap overlay | 1 positive, 2 overlay/counterexample | 19.05 | -27.86 | 47.14 | -27.86 | 0.00 for Green | Best explanatory alignment. |
| P3 counterexample guard | guard | policy-only headline cannot promote beyond Stage2 | 1 positive, 2 blocked/overlay | 19.05 | -27.86 | 47.14 | -27.86 | 0.00 for Green | Conservative but robust. |

## 20. Score-Return Alignment Matrix

| case_id | weighted_score_before | stage_before | weighted_score_after | stage_after | MFE_180D | MAE_180D | score-return alignment |
|---|---:|---|---:|---|---:|---:|---|
| R11L10C31_034020_20240718 | 74 | Stage3-Yellow | 78 | Stage3-Yellow+direct bridge | 47.14 | -27.86 | aligned but high-MAE; do not Green without revision. |
| R11L10C31_052690_20240718 | 76 | Stage3-Yellow / false Green risk | 67 | Stage2-watch | 19.63 | -39.27 | after-profile better; event peak was not durable rerating. |
| R11L10C31_036460_20240603 | 72 | Stage2-Actionable risk | 58 | 4B/4C overlay-only | 66.67 | -23.51 | raw MFE misleading; drawdown and lack of proof make positive training unsafe. |

## 21. Coverage Matrix

| large_sector_id | canonical_archetype_id | fine_archetype_id | positive_case_count | counterexample_count | 4B_case_count | 4C_case_count | new_independent_case_count | reused_case_count | calibration_usable_trigger_count | representative_trigger_count | current_profile_error_count | sector_rule_candidate | canonical_rule_candidate | coverage_gap_after_this_loop |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|---|---|
| L10_POLICY_EVENT_CROSS_REDTEAM_MISC | C31_POLICY_SUBSIDY_LEGISLATION_EVENT | NUCLEAR_RESOURCE_POLICY_EVENT_PASS_THROUGH_VS_PRICE_ONLY_THEME | 1 | 2 | 2 | 1 | 3 | 0 | 6 | 3 | 2 | true | true | needs holdout: policy subsidy legislation outside nuclear/resource, e.g. tender/capex subsidy and disaster-policy cases |

## 22. Residual Contribution Summary

```text
new_independent_case_count: 3
reused_case_count: 0
reused_case_ids: []
new_symbol_count: 3
same_archetype_new_symbol_count: 3
same_archetype_new_trigger_family_count: 3
new_canonical_archetype_count: 0
new_fine_archetype_count: 3
new_trigger_family_count: 3
tested_existing_calibrated_axes: [stage3_green_revision_min, price_only_blowoff_blocks_positive_stage, full_4b_requires_non_price_evidence, hard_4c_thesis_break_routes_to_4c]
residual_error_types_found: [policy_headline_false_positive, direct_beneficiary_missed_structural, price_only_theme_4B_drawdown]
new_axis_proposed: [policy_event_execution_bridge_cap, c31_direct_beneficiary_bridge_score]
existing_axis_strengthened: [stage3_green_revision_min in C31, full_4b_requires_non_price_evidence, hard_4c_thesis_break_routes_to_4c]
existing_axis_weakened: []
existing_axis_kept: [stage2_actionable_evidence_bonus, stage3_yellow_total_min]
sector_specific_rule_candidate: true
canonical_archetype_rule_candidate: true
no_new_signal_reason: null
loop_contribution_label: canonical_archetype_rule_candidate
do_not_propose_new_weight_delta: false
```

## 23. Validation Scope / Non-Validation Scope

Validated:

- Stock-Web manifest and schema fields.
- Symbol profiles for 034020, 052690, 036460.
- Entry rows and 2024/2025 tradable OHLC paths used for 180D MFE/MAE.
- 180D corporate-action contamination absence by profile dates.
- Positive/counterexample balance and representative trigger dedupe.

Not validated in this loop:

- Production `stock_agent` code behavior.
- Live/current investment status.
- Full 1Y/2Y backtest windows; 180D is the calibration basis.
- Exact analyst consensus revision series; score components are research proxy scores.

## 24. Shadow Weight Calibration

```csv
row_type,axis,scope,large_sector_id,canonical_archetype_id,baseline_value,tested_value,delta,reason,backtest_effect,trigger_ids,calibration_usable_count,new_independent_case_count,counterexample_count,confidence,proposal_type,notes
shadow_weight,policy_event_positive_promotion_cap,sector_specific,L10_POLICY_EVENT_CROSS_REDTEAM_MISC,C31_POLICY_SUBSIDY_LEGISLATION_EVENT,0,1,+1,"Policy/resource headlines without execution bridge created false-positive or 4B-only paths.","reduces C31 false Green risk; preserves direct-beneficiary Stage2/Yellow",R11C31_034020_T1_STAGE2|R11C31_052690_T1_STAGE2|R11C31_036460_T1_STAGE2,3,3,2,low_to_medium,sector_shadow_only,"not production; post-calibrated residual"
shadow_weight,c31_direct_beneficiary_execution_bridge,canonical_archetype_specific,L10_POLICY_EVENT_CROSS_REDTEAM_MISC,C31_POLICY_SUBSIDY_LEGISLATION_EVENT,0,2,+2,"Direct beneficiary plus contract/project pass-through distinguishes nuclear supplier success from policy beta.","keeps 034020 eligible while capping 052690/036460",R11C31_034020_T1_STAGE2|R11C31_052690_T1_STAGE2|R11C31_036460_T1_STAGE2,3,3,2,low_to_medium,canonical_shadow_only,"requires holdout before production"
shadow_weight,c31_policy_only_green_cap,canonical_archetype_specific,L10_POLICY_EVENT_CROSS_REDTEAM_MISC,C31_POLICY_SUBSIDY_LEGISLATION_EVENT,0,-3,-3,"Policy-only headline should not bridge to Green without margin/revision/commercial evidence.","blocks false Green for 052690 and 036460",R11C31_052690_T1_STAGE2|R11C31_036460_T1_STAGE2,2,2,2,medium,counterexample_guard,"not a global rollback"
```

## 25. Machine-Readable Rows

### 25.1 price_source_validation

```jsonl
{"row_type":"price_source_validation","source":"Songdaiki/stock-web","source_url":"https://github.com/Songdaiki/stock-web","manifest_path":"atlas/manifest.json","schema_path":"atlas/schema.json","universe_path":"atlas/universe/all_symbols.csv","manifest_max_date":"2026-02-20","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","calibration_shard_root":"atlas/ohlcv_tradable_by_symbol_year","raw_shard_root":"atlas/ohlcv_raw_by_symbol_year","validation_status":"usable_for_historical_calibration"}
```

### 25.2 case rows

```jsonl
{"row_type":"case","case_id":"R11L10C31_034020_20240718","symbol":"034020","company_name":"두산에너빌리티","round":"R11","loop":"10","large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"C31_POLICY_SUBSIDY_LEGISLATION_EVENT","fine_archetype_id":"CZECH_NUCLEAR_POLICY_PROJECT_PASS_THROUGH","case_type":"high_mae_success","positive_or_counterexample":"positive","best_trigger":"R11C31_034020_T1_STAGE2","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"aligned_high_mae_success","current_profile_verdict":"current_profile_too_late","price_source":"Songdaiki/stock-web","notes":"Direct-beneficiary nuclear supplier chain; Stage2/Yellow valid but Green requires revision/margin bridge."}
{"row_type":"case","case_id":"R11L10C31_052690_20240718","symbol":"052690","company_name":"한전기술","round":"R11","loop":"10","large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"C31_POLICY_SUBSIDY_LEGISLATION_EVENT","fine_archetype_id":"CZECH_NUCLEAR_POLICY_PROJECT_WITHOUT_REVISION_BRIDGE","case_type":"failed_rerating","positive_or_counterexample":"counterexample","best_trigger":"R11C31_052690_T1_STAGE2","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"misaligned_policy_headline_peak","current_profile_verdict":"current_profile_false_positive","price_source":"Songdaiki/stock-web","notes":"Same Czech headline but weaker realized revision/margin bridge; event-day peak dominates."}
{"row_type":"case","case_id":"R11L10C31_036460_20240603","symbol":"036460","company_name":"한국가스공사","round":"R11","loop":"10","large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"C31_POLICY_SUBSIDY_LEGISLATION_EVENT","fine_archetype_id":"RESOURCE_EXPLORATION_POLICY_OPTION_VALUE_THEME","case_type":"price_moved_without_evidence","positive_or_counterexample":"counterexample","best_trigger":"R11C31_036460_T1_STAGE2","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"misleading_MFE_price_only_theme","current_profile_verdict":"current_profile_false_positive","price_source":"Songdaiki/stock-web","notes":"Headline-driven exploration option; no commercial reserve/revision proof at trigger."}
```

### 25.3 trigger rows

```jsonl
{"row_type":"trigger","trigger_id":"R11C31_034020_T1_STAGE2","case_id":"R11L10C31_034020_20240718","symbol":"034020","company_name":"두산에너빌리티","round":"R11","loop":"10","large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"C31_POLICY_SUBSIDY_LEGISLATION_EVENT","fine_archetype_id":"CZECH_NUCLEAR_POLICY_PROJECT_PASS_THROUGH","sector":"정책·지정학·재난·이벤트","primary_archetype":"policy_project_preferred_bidder_direct_beneficiary","loop_objective":"counterexample_mining|sector_specific_rule_discovery|coverage_gap_fill","trigger_type":"Stage2-Actionable","trigger_date":"2024-07-17","evidence_available_at_that_date":"KHNP selected preferred bidder for Czech nuclear project; related Korean nuclear names moved.","evidence_source":"Reuters 2024-07-17 Czech nuclear preferred bidder report","stage2_evidence_fields":["public_event_or_disclosure","policy_or_regulatory_optionality","customer_or_order_quality"],"stage3_evidence_fields":["partial_financial_visibility"],"stage4b_evidence_fields":[],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/034/034020/2024.csv","profile_path":"atlas/symbol_profiles/034/034020.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","entry_date":"2024-07-18","entry_price":21000,"MFE_30D_pct":19.05,"MFE_90D_pct":19.05,"MFE_180D_pct":47.14,"MFE_1Y_pct":null,"MFE_2Y_pct":null,"MAE_30D_pct":-27.86,"MAE_90D_pct":-27.86,"MAE_180D_pct":-27.86,"MAE_1Y_pct":null,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2025-02-19","peak_price":30900,"drawdown_after_peak_pct":-35.4,"green_lateness_ratio":null,"four_b_local_peak_proximity":null,"four_b_full_window_peak_proximity":null,"four_b_timing_verdict":"not_applicable","four_b_evidence_type":[],"four_c_protection_label":"thesis_break_watch_only","trigger_outcome_label":"high_mae_success","current_profile_verdict":"current_profile_too_late","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"034020_2024-07-18_21000","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"R11C31_034020_T2_4B","case_id":"R11L10C31_034020_20240718","symbol":"034020","company_name":"두산에너빌리티","round":"R11","loop":"10","large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"C31_POLICY_SUBSIDY_LEGISLATION_EVENT","fine_archetype_id":"CZECH_NUCLEAR_POLICY_PROJECT_PASS_THROUGH","sector":"정책·지정학·재난·이벤트","primary_archetype":"policy_project_4B_overlay","loop_objective":"4B_non_price_requirement_stress_test","trigger_type":"4B-overlay","trigger_date":"2025-02-18","evidence_available_at_that_date":"Near full-window peak after renewed nuclear-policy move; use as overlay not positive training.","evidence_source":"stock-web price path + nuclear policy continuation watch","stage2_evidence_fields":[],"stage3_evidence_fields":[],"stage4b_evidence_fields":["valuation_blowoff","positioning_overheat","margin_or_backlog_slowdown"],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/034/034020/2025.csv","profile_path":"atlas/symbol_profiles/034/034020.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","entry_date":"2025-02-18","entry_price":30300,"MFE_30D_pct":2.0,"MFE_90D_pct":null,"MFE_180D_pct":null,"MFE_1Y_pct":null,"MFE_2Y_pct":null,"MAE_30D_pct":-17.49,"MAE_90D_pct":null,"MAE_180D_pct":null,"MAE_1Y_pct":null,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":null,"peak_date":"2025-02-19","peak_price":30900,"drawdown_after_peak_pct":-35.4,"green_lateness_ratio":null,"four_b_local_peak_proximity":0.94,"four_b_full_window_peak_proximity":0.94,"four_b_timing_verdict":"good_full_window_4B_timing_but_late","four_b_evidence_type":["valuation_blowoff","positioning_overheat"],"four_c_protection_label":"thesis_break_watch_only","trigger_outcome_label":"4B_overlay_success","current_profile_verdict":"current_profile_4B_too_late","calibration_usable":true,"forward_window_trading_days":30,"calibration_block_reasons":[],"corporate_action_window_status":"clean_30D_window","same_entry_group_id":"034020_2025-02-18_30300","dedupe_for_aggregate":false,"aggregate_group_role":"4B_overlay_only","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":0.5,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"R11C31_052690_T1_STAGE2","case_id":"R11L10C31_052690_20240718","symbol":"052690","company_name":"한전기술","round":"R11","loop":"10","large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"C31_POLICY_SUBSIDY_LEGISLATION_EVENT","fine_archetype_id":"CZECH_NUCLEAR_POLICY_PROJECT_WITHOUT_REVISION_BRIDGE","sector":"정책·지정학·재난·이벤트","primary_archetype":"policy_project_beneficiary_without_margin_bridge","loop_objective":"residual_false_positive_mining|counterexample_mining","trigger_type":"Stage2-Actionable","trigger_date":"2024-07-17","evidence_available_at_that_date":"Same Czech preferred-bidder event; indirect engineering beneficiary but no immediate margin/revision bridge.","evidence_source":"Reuters 2024-07-17 Czech nuclear preferred bidder report","stage2_evidence_fields":["public_event_or_disclosure","policy_or_regulatory_optionality"],"stage3_evidence_fields":[],"stage4b_evidence_fields":[],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/052/052690/2024.csv","profile_path":"atlas/symbol_profiles/052/052690.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","entry_date":"2024-07-18","entry_price":82000,"MFE_30D_pct":19.63,"MFE_90D_pct":19.63,"MFE_180D_pct":19.63,"MFE_1Y_pct":null,"MFE_2Y_pct":null,"MAE_30D_pct":-24.88,"MAE_90D_pct":-24.88,"MAE_180D_pct":-39.27,"MAE_1Y_pct":null,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-07-18","peak_price":98100,"drawdown_after_peak_pct":-49.24,"green_lateness_ratio":null,"four_b_local_peak_proximity":null,"four_b_full_window_peak_proximity":null,"four_b_timing_verdict":"not_applicable","four_b_evidence_type":[],"four_c_protection_label":"hard_4c_late","trigger_outcome_label":"failed_rerating","current_profile_verdict":"current_profile_false_positive","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"052690_2024-07-18_82000","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"R11C31_052690_T2_4C","case_id":"R11L10C31_052690_20240718","symbol":"052690","company_name":"한전기술","round":"R11","loop":"10","large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"C31_POLICY_SUBSIDY_LEGISLATION_EVENT","fine_archetype_id":"PROJECT_EVENT_LEGAL_DELAY_4B_4C_OVERLAY","sector":"정책·지정학·재난·이벤트","primary_archetype":"legal_delay_project_event_cap","loop_objective":"4C_thesis_break_timing_test","trigger_type":"4C-watch","trigger_date":"2024-10-30","evidence_available_at_that_date":"Czech watchdog temporarily prohibited final contract signing amid appeals.","evidence_source":"Reuters 2024-10-30 Czech watchdog contract signing halt report","stage2_evidence_fields":[],"stage3_evidence_fields":[],"stage4b_evidence_fields":["legal_or_regulatory_block"],"stage4c_evidence_fields":["legal_or_regulatory_block","thesis_evidence_broken"],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/052/052690/2024.csv","profile_path":"atlas/symbol_profiles/052/052690.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","entry_date":"2024-10-31","entry_price":68800,"MFE_30D_pct":4.8,"MFE_90D_pct":10.32,"MFE_180D_pct":null,"MFE_1Y_pct":null,"MFE_2Y_pct":null,"MAE_30D_pct":-4.07,"MAE_90D_pct":-27.62,"MAE_180D_pct":null,"MAE_1Y_pct":null,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2025-02-14","peak_price":75900,"drawdown_after_peak_pct":-34.39,"green_lateness_ratio":null,"four_b_local_peak_proximity":-0.84,"four_b_full_window_peak_proximity":-0.84,"four_b_timing_verdict":"not_4B_legal_4C_watch","four_b_evidence_type":["legal_or_regulatory_block"],"four_c_protection_label":"hard_4c_late","trigger_outcome_label":"4C_late","current_profile_verdict":"current_profile_4C_too_late","calibration_usable":true,"forward_window_trading_days":90,"calibration_block_reasons":[],"corporate_action_window_status":"clean_90D_window","same_entry_group_id":"052690_2024-10-31_68800","dedupe_for_aggregate":false,"aggregate_group_role":"4C_overlay_only","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":0.5,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"R11C31_036460_T1_STAGE2","case_id":"R11L10C31_036460_20240603","symbol":"036460","company_name":"한국가스공사","round":"R11","loop":"10","large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"C31_POLICY_SUBSIDY_LEGISLATION_EVENT","fine_archetype_id":"RESOURCE_EXPLORATION_POLICY_OPTION_VALUE_THEME","sector":"정책·지정학·재난·이벤트","primary_archetype":"resource_exploration_policy_option_headline","loop_objective":"counterexample_mining|4B_non_price_requirement_stress_test","trigger_type":"Stage2-Policy-Option","trigger_date":"2024-06-03","evidence_available_at_that_date":"Government approval of East Sea oil/gas exploration option; commercial reserve not proved.","evidence_source":"Reuters 2024-06-03 oil/gas exploration approval report; WSJ Korea Gas rally report","stage2_evidence_fields":["public_event_or_disclosure","policy_or_regulatory_optionality"],"stage3_evidence_fields":[],"stage4b_evidence_fields":[],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/036/036460/2024.csv","profile_path":"atlas/symbol_profiles/036/036460.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","entry_date":"2024-06-03","entry_price":38700,"MFE_30D_pct":66.67,"MFE_90D_pct":66.67,"MFE_180D_pct":66.67,"MFE_1Y_pct":null,"MFE_2Y_pct":null,"MAE_30D_pct":-23.26,"MAE_90D_pct":-23.26,"MAE_180D_pct":-23.51,"MAE_1Y_pct":null,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-06-20","peak_price":64500,"drawdown_after_peak_pct":-54.11,"green_lateness_ratio":null,"four_b_local_peak_proximity":null,"four_b_full_window_peak_proximity":null,"four_b_timing_verdict":"not_applicable","four_b_evidence_type":[],"four_c_protection_label":"hard_4c_success_if_event_cap_used","trigger_outcome_label":"price_moved_without_evidence","current_profile_verdict":"current_profile_false_positive","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"036460_2024-06-03_38700","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"R11C31_036460_T2_4B","case_id":"R11L10C31_036460_20240603","symbol":"036460","company_name":"한국가스공사","round":"R11","loop":"10","large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"C31_POLICY_SUBSIDY_LEGISLATION_EVENT","fine_archetype_id":"RESOURCE_EXPLORATION_POLICY_OPTION_VALUE_THEME","sector":"정책·지정학·재난·이벤트","primary_archetype":"event_cap_price_only_4B","loop_objective":"4B_non_price_requirement_stress_test","trigger_type":"4B-overlay","trigger_date":"2024-06-20","evidence_available_at_that_date":"Resource-option rally reached full-window peak before drilling/commercial confirmation.","evidence_source":"stock-web price path + Reuters/WSJ event context","stage2_evidence_fields":[],"stage3_evidence_fields":[],"stage4b_evidence_fields":["price_only_local_peak","valuation_blowoff","explicit_event_cap"],"stage4c_evidence_fields":["thesis_evidence_broken"],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/036/036460/2024.csv","profile_path":"atlas/symbol_profiles/036/036460.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","entry_date":"2024-06-20","entry_price":63500,"MFE_30D_pct":1.57,"MFE_90D_pct":1.57,"MFE_180D_pct":1.57,"MFE_1Y_pct":null,"MFE_2Y_pct":null,"MAE_30D_pct":-42.52,"MAE_90D_pct":-42.52,"MAE_180D_pct":-53.39,"MAE_1Y_pct":null,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-06-20","peak_price":64500,"drawdown_after_peak_pct":-54.11,"green_lateness_ratio":null,"four_b_local_peak_proximity":0.96,"four_b_full_window_peak_proximity":0.96,"four_b_timing_verdict":"good_full_window_4B_timing_with_event_cap","four_b_evidence_type":["price_only","valuation_blowoff","explicit_event_cap"],"four_c_protection_label":"hard_4c_success","trigger_outcome_label":"4B_overlay_success","current_profile_verdict":"current_profile_correct","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"036460_2024-06-20_63500","dedupe_for_aggregate":false,"aggregate_group_role":"4B_overlay_only","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":0.5,"do_not_count_as_new_case":false}
```

### 25.4 score_simulation rows

```jsonl
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"R11L10C31_034020_20240718","trigger_id":"R11C31_034020_T1_STAGE2","symbol":"034020","large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"C31_POLICY_SUBSIDY_LEGISLATION_EVENT","raw_component_scores_before":{"contract_score":5,"backlog_visibility_score":4,"margin_bridge_score":3,"revision_score":3,"relative_strength_score":6,"customer_quality_score":8,"policy_or_regulatory_score":9,"valuation_repricing_score":5,"execution_risk_score":5,"legal_or_contract_risk_score":3,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_before":74,"stage_label_before":"Stage3-Yellow","raw_component_scores_after":{"contract_score":6,"backlog_visibility_score":5,"margin_bridge_score":3,"revision_score":3,"relative_strength_score":6,"customer_quality_score":9,"policy_or_regulatory_score":9,"valuation_repricing_score":5,"execution_risk_score":5,"legal_or_contract_risk_score":3,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0,"direct_beneficiary_execution_bridge_score":2},"weighted_score_after":78,"stage_label_after":"Stage3-Yellow_direct_bridge_watch","changed_components":["customer_quality_score","direct_beneficiary_execution_bridge_score"],"component_delta_explanation":"Direct supplier/project beneficiary chain permits Yellow but still lacks revision score for Green.","MFE_90D_pct":19.05,"MAE_90D_pct":-27.86,"score_return_alignment_label":"aligned_high_mae_success","current_profile_verdict":"current_profile_too_late"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"R11L10C31_052690_20240718","trigger_id":"R11C31_052690_T1_STAGE2","symbol":"052690","large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"C31_POLICY_SUBSIDY_LEGISLATION_EVENT","raw_component_scores_before":{"contract_score":2,"backlog_visibility_score":2,"margin_bridge_score":1,"revision_score":1,"relative_strength_score":8,"customer_quality_score":5,"policy_or_regulatory_score":9,"valuation_repricing_score":5,"execution_risk_score":6,"legal_or_contract_risk_score":3,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_before":76,"stage_label_before":"Stage3-Yellow_false_green_risk","raw_component_scores_after":{"contract_score":2,"backlog_visibility_score":2,"margin_bridge_score":1,"revision_score":1,"relative_strength_score":6,"customer_quality_score":4,"policy_or_regulatory_score":6,"valuation_repricing_score":4,"execution_risk_score":6,"legal_or_contract_risk_score":5,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0,"policy_only_green_cap":-3},"weighted_score_after":67,"stage_label_after":"Stage2-watch","changed_components":["policy_or_regulatory_score","relative_strength_score","policy_only_green_cap","legal_or_contract_risk_score"],"component_delta_explanation":"Policy event without revision/margin bridge should not bridge to Green; legal delay risk increases cap.","MFE_90D_pct":19.63,"MAE_90D_pct":-24.88,"score_return_alignment_label":"after_profile_better","current_profile_verdict":"current_profile_false_positive"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"R11L10C31_036460_20240603","trigger_id":"R11C31_036460_T1_STAGE2","symbol":"036460","large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"C31_POLICY_SUBSIDY_LEGISLATION_EVENT","raw_component_scores_before":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":0,"revision_score":0,"relative_strength_score":9,"customer_quality_score":2,"policy_or_regulatory_score":10,"valuation_repricing_score":6,"execution_risk_score":7,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_before":72,"stage_label_before":"Stage2-Actionable_policy_option_risk","raw_component_scores_after":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":0,"revision_score":0,"relative_strength_score":5,"customer_quality_score":1,"policy_or_regulatory_score":5,"valuation_repricing_score":3,"execution_risk_score":8,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0,"policy_only_green_cap":-3,"event_cap_4B_score":4},"weighted_score_after":58,"stage_label_after":"4B_4C_overlay_only","changed_components":["policy_or_regulatory_score","relative_strength_score","policy_only_green_cap","event_cap_4B_score"],"component_delta_explanation":"Exploration approval lacks commercial proof; treat as event-cap overlay despite high MFE.","MFE_90D_pct":66.67,"MAE_90D_pct":-23.26,"score_return_alignment_label":"MFE_misleading_without_4B","current_profile_verdict":"current_profile_false_positive"}
```

### 25.5 shadow_weight rows

See section 24 CSV.

### 25.6 residual_contribution row

```jsonl
{"row_type":"residual_contribution","round":"R11","loop":"10","large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"C31_POLICY_SUBSIDY_LEGISLATION_EVENT","new_independent_case_count":3,"reused_case_count":0,"new_symbol_count":3,"same_archetype_new_symbol_count":3,"same_archetype_new_trigger_family_count":3,"new_trigger_family_count":3,"tested_existing_calibrated_axes":["stage3_green_revision_min","price_only_blowoff_blocks_positive_stage","full_4b_requires_non_price_evidence","hard_4c_thesis_break_routes_to_4c"],"residual_error_types_found":["policy_headline_false_positive","direct_beneficiary_missed_structural","price_only_theme_4B_drawdown"],"loop_contribution_label":"canonical_archetype_rule_candidate","do_not_propose_new_weight_delta":false,"auto_selected_coverage_gap":"R11/C31 policy-event direct beneficiary vs policy-only headline split"}
```

### 25.7 narrative_only row

```jsonl
{"row_type":"narrative_only","case_id":"R11L10C31_CZECH_CONTRACT_LEGAL_APPEAL_CONTEXT","symbol":"052690","large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"C31_POLICY_SUBSIDY_LEGISLATION_EVENT","reason":"legal appeal evidence is overlay/protection context, not positive weight calibration","price_source":"Songdaiki/stock-web","usage":"not_positive_weight_calibration"}
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
next_round = R11 holdout or R12
recommended_next_scope = C31_POLICY_SUBSIDY_LEGISLATION_EVENT holdout outside nuclear/resource, or C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP
carry_forward_open_questions = [Does C31 direct-beneficiary bridge hold in subsidy/legislation cases?, Can event-cap 4B timing be generalized without overfitting to resource spikes?]
```

## 28. Source Notes

- Stock-Web manifest/schema/profile/shard data are the only price source used.
- Reuters 2024-07-17 Czech nuclear preferred-bidder report is used as historical trigger evidence for the Czech nuclear cases.
- Reuters 2024-10-30 Czech watchdog/appeals report is used as project-delay/4C overlay context.
- Reuters 2024-06-03 and WSJ Korea Gas rally report are used as historical evidence for the resource-exploration policy event.
- No stock_agent production code was opened or patched in this loop.
