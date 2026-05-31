# E2R Stock-Web Historical Calibration / Sector-Archetype Residual Research Round

## 0. Research Metadata

```text
research_session = post_calibrated_sector_archetype_residual_research
mode = historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12
output_format = one_standalone_markdown_file
scheduled_round = R10
scheduled_loop = 11
completed_round = R10
completed_loop = 11
next_round = R11
next_loop = 11
round_schedule_status = valid
round_sector_consistency = pass
large_sector_id = L9_CONSTRUCTION_REALESTATE_HOUSING
canonical_archetype_id = C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK
fine_archetype_id = PF_POLICY_LIQUIDITY_BACKSTOP_DIRECT_SUPPORT_SPLIT
output_file = e2r_stock_web_v12_residual_round_R10_loop_11_L9_CONSTRUCTION_REALESTATE_HOUSING_C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK_research.md
price_source = Songdaiki/stock-web
stock_web_manifest_max_date = 2026-02-20
production_scoring_changed = false
shadow_weight_only = true
```

This loop adds 5 new independent cases, 3 counterexamples, and 5 residual errors for R10/L9_CONSTRUCTION_REALESTATE_HOUSING/C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK.

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

This MD does not re-prove the global Stage2 bonus or Green strictness. It stress-tests whether C30 construction/PF evidence needs a sector split between **direct support / balance-sheet repair** and **generic policy beta**.

## 2. Round / Large Sector / Canonical Archetype Scope

- scheduled_round: `R10`
- scheduled_loop: `11`
- large_sector_id: `L9_CONSTRUCTION_REALESTATE_HOUSING`
- canonical_archetype_id: `C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK`
- fine_archetype_id: `PF_POLICY_LIQUIDITY_BACKSTOP_DIRECT_SUPPORT_SPLIT`
- loop_objective: `coverage_gap_fill`, `residual_false_positive_mining`, `residual_missed_structural_mining`, `sector_specific_rule_discovery`, `canonical_archetype_compression`, `4B_non_price_requirement_stress_test`

R10 maps to `L9_CONSTRUCTION_REALESTATE_HOUSING`, so the round-sector consistency gate passes.

## 3. Previous Coverage / Duplicate Avoidance Check

Local v12 filename registry indicates Loop 10 has R1~R13 complete and Loop 11 has R1~R9 complete. Therefore the first missing round is R10 / Loop 11.

The prior R10 Loop 10 file used HDC현대산업개발, GS건설, and 태영건설. This loop avoids those symbols and chooses five non-duplicate cases: 대우건설, 신세계건설, DL이앤씨, 계룡건설, 동부건설.

```text
new_independent_case_count = 5
reused_case_count = 0
new_symbol_count = 5
same_archetype_new_symbol_count = 5
same_archetype_new_trigger_family_count = 5
duplicate_low_value_loop = false
```

## 4. Stock-Web OHLC Input / Price Source Validation

The Stock-Web manifest was checked before selecting cases.

```text
source_name = FinanceData/marcap
source_repo_url = https://github.com/FinanceData/marcap
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
raw_shard_columns = d,o,h,l,c,v,a,mc,s,m,rs
MFE_N_pct = (max high from entry_date through N tradable rows / entry_price - 1) * 100
MAE_N_pct = (min low from entry_date through N tradable rows / entry_price - 1) * 100
calibration_basis = tradable_raw
```

## 5. Historical Eligibility Gate

| case_id | symbol | profile path | entry | forward window | corporate-action window status | calibration_usable |
|---|---:|---|---:|---:|---|---|
| R10L11_C30_DAEWOO_202403_POLICY_BACKSTOP_SURVIVOR | 047040 | atlas/symbol_profiles/047/047040.json | 2024-03-27 | 180D available | clean_180D_window | true |
| R10L11_C30_SHINSEGAE_202403_PARENT_SUPPORT_EVENT_PREMIUM | 034300 | atlas/symbol_profiles/034/034300.json | 2024-03-27 | 180D available | clean_180D_window; prior CA 2024-02-06 before entry | true |
| R10L11_C30_DL_202403_POLICY_REVALUE_FALSE_POSITIVE | 375500 | atlas/symbol_profiles/375/375500.json | 2024-03-27 | 180D available | clean_180D_window | true |
| R10L11_C30_KYERYONG_202403_POLICY_REVALUE_FALSE_POSITIVE | 013580 | atlas/symbol_profiles/013/013580.json | 2024-03-27 | 180D available | clean_180D_window | true |
| R10L11_C30_DONGBU_202403_POLICY_REVALUE_LATE_DRAWDOWN | 005960 | atlas/symbol_profiles/005/005960.json | 2024-03-27 | 180D available | clean_180D_window | true |

## 6. Canonical Archetype Compression Map

| fine_archetype | canonical_archetype_id | use in this loop |
|---|---|---|
| POLICY_LIQUIDITY_BACKSTOP_LARGE_BUILDER_SURVIVOR | C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK | 대우건설 positive structural repair/survivor path |
| PARENT_SUPPORT_EVENT_PREMIUM_BRIDGE | C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK | 신세계건설 direct support / event-premium bridge |
| POLICY_BETA_WITHOUT_BALANCE_SHEET_REPAIR | C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK | DL이앤씨 / 계룡건설 / 동부건설 counterexample family |
| SMALL_MID_BUILDER_LATE_DRAWDOWN_GUARD | C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK | 동부건설 late drawdown guard |

The compression point is simple: in construction/PF, policy liquidity is not one signal. It is either a bridge with balance-sheet repair or merely a tide lifting weak hulls for a short time.

## 7. Case Selection Summary

| case_id | symbol | company | role | polarity | best trigger | entry | MFE90 | MAE90 | verdict |
|---|---:|---|---|---|---|---:|---:|---:|---|
| R10L11_C30_DAEWOO_202403_POLICY_BACKSTOP_SURVIVOR | 047040 | 대우건설 | structural_success | positive | R10L11_T01_DAEWOO_STAGE2_POLICY_BACKSTOP | 2024-03-27 / 3730 | 33.11% | -4.02% | current_profile_missed_structural |
| R10L11_C30_SHINSEGAE_202403_PARENT_SUPPORT_EVENT_PREMIUM | 034300 | 신세계건설 | structural_success | positive | R10L11_T02_SHINSEGAE_STAGE2_PARENT_SUPPORT | 2024-03-27 / 10630 | 75.45% | -7.34% | current_profile_missed_structural |
| R10L11_C30_DL_202403_POLICY_REVALUE_FALSE_POSITIVE | 375500 | DL이앤씨 | failed_rerating | counterexample | R10L11_T03_DL_POLICY_BETA_CAP | 2024-03-27 / 36450 | 8.37% | -21.54% | current_profile_false_positive |
| R10L11_C30_KYERYONG_202403_POLICY_REVALUE_FALSE_POSITIVE | 013580 | 계룡건설 | failed_rerating | counterexample | R10L11_T04_KYERYONG_POLICY_BETA_CAP | 2024-03-27 / 14240 | 8.78% | -11.31% | current_profile_too_early |
| R10L11_C30_DONGBU_202403_POLICY_REVALUE_LATE_DRAWDOWN | 005960 | 동부건설 | failed_rerating | counterexample | R10L11_T05_DONGBU_POLICY_BETA_CAP | 2024-03-27 / 5030 | 3.98% | -5.57% | current_profile_false_positive |


## 8. Positive vs Counterexample Balance

```text
positive_case_count = 2
counterexample_count = 3
4B_case_count = 1
4C_case_count = 0
calibration_usable_case_count = 5
calibration_usable_trigger_count = 6
representative_trigger_count = 5
```

The balance is adequate for a sector/canonical shadow rule candidate: two positive cases prove the path exists, while three counterexamples prevent the rule from degenerating into a broad “policy headline = buyable Stage2” shortcut.

## 9. Evidence Source Map

| evidence family | trigger date | evidence timing rule | stage use | notes |
|---|---:|---|---|---|
| Korean construction liquidity/backstop policy | 2024-03-27 | same-day close allowed because public report was available during the Korean trading day window | Stage2 / Stage2-cap | Used as common macro trigger, not sufficient alone for Green. |
| Stricter PF restructuring regime | 2024-05-13 | after entry, regime context only | stress test / counterexample audit | Not used to backdate trigger. |
| Direct support / event-premium path | 2024-03-27 entry, 2024-09-30 overlay | Stage2 repair bridge and later 4B overlay | Shinsegae case | Event premium is 4B overlay, not new positive evidence. |
| OHLC validation | 2024 stock-web rows | entry and forward windows | backtest | All representative triggers use tradable_raw rows. |

## 10. Price Data Source Map

| symbol | company | price_shard_path | profile_path | stock-web profile caveat |
|---:|---|---|---|---|
| 047040 | 대우건설 | atlas/ohlcv_tradable_by_symbol_year/047/047040/2024.csv | atlas/symbol_profiles/047/047040.json | historical CA candidates only, outside 2024 study window |
| 034300 | 신세계건설 | atlas/ohlcv_tradable_by_symbol_year/034/034300/2024.csv | atlas/symbol_profiles/034/034300.json | 2024-02-06 CA candidate before entry; inactive-like after 2025 |
| 375500 | DL이앤씨 | atlas/ohlcv_tradable_by_symbol_year/375/375500/2024.csv | atlas/symbol_profiles/375/375500.json | 2022 CA candidates outside 2024 study window |
| 013580 | 계룡건설 | atlas/ohlcv_tradable_by_symbol_year/013/013580/2024.csv | atlas/symbol_profiles/013/013580.json | 1999 CA candidate outside study window |
| 005960 | 동부건설 | atlas/ohlcv_tradable_by_symbol_year/005/005960/2024.csv | atlas/symbol_profiles/005/005960.json | historical CA candidates outside study window |

## 11. Case-by-Case Trigger Grid

| case_id | symbol | company | role | polarity | best trigger | entry | MFE90 | MAE90 | verdict |
|---|---:|---|---|---|---|---:|---:|---:|---|
| R10L11_C30_DAEWOO_202403_POLICY_BACKSTOP_SURVIVOR | 047040 | 대우건설 | structural_success | positive | R10L11_T01_DAEWOO_STAGE2_POLICY_BACKSTOP | 2024-03-27 / 3730 | 33.11% | -4.02% | current_profile_missed_structural |
| R10L11_C30_SHINSEGAE_202403_PARENT_SUPPORT_EVENT_PREMIUM | 034300 | 신세계건설 | structural_success | positive | R10L11_T02_SHINSEGAE_STAGE2_PARENT_SUPPORT | 2024-03-27 / 10630 | 75.45% | -7.34% | current_profile_missed_structural |
| R10L11_C30_DL_202403_POLICY_REVALUE_FALSE_POSITIVE | 375500 | DL이앤씨 | failed_rerating | counterexample | R10L11_T03_DL_POLICY_BETA_CAP | 2024-03-27 / 36450 | 8.37% | -21.54% | current_profile_false_positive |
| R10L11_C30_KYERYONG_202403_POLICY_REVALUE_FALSE_POSITIVE | 013580 | 계룡건설 | failed_rerating | counterexample | R10L11_T04_KYERYONG_POLICY_BETA_CAP | 2024-03-27 / 14240 | 8.78% | -11.31% | current_profile_too_early |
| R10L11_C30_DONGBU_202403_POLICY_REVALUE_LATE_DRAWDOWN | 005960 | 동부건설 | failed_rerating | counterexample | R10L11_T05_DONGBU_POLICY_BETA_CAP | 2024-03-27 / 5030 | 3.98% | -5.57% | current_profile_false_positive |


## 12. Trigger-Level OHLC Backtest Tables

| trigger_id | company | entry date | entry price | MFE30 | MAE30 | MFE90 | MAE90 | MFE180 | MAE180 | peak | drawdown after peak | outcome |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---|---:|---|
| R10L11_T01_DAEWOO_STAGE2_POLICY_BACKSTOP | 대우건설 | 2024-03-27 | 3,730 | 3.75% | -4.02% | 33.11% | -4.02% | 33.11% | -15.01% | 2024-07-18 / 4,965 | -36.15% | policy_backstop_survivor_success |
| R10L11_T02_SHINSEGAE_STAGE2_PARENT_SUPPORT | 신세계건설 | 2024-03-27 | 10,630 | 8.75% | -6.11% | 75.45% | -7.34% | 75.45% | -7.34% | 2024-05-30 / 18,650 | -47.18% | direct_support_event_premium_success |
| R10L11_T03_DL_POLICY_BETA_CAP | DL이앤씨 | 2024-03-27 | 36,450 | 3.70% | -12.35% | 8.37% | -21.54% | 8.37% | -21.54% | 2024-06-13 / 39,500 | -27.59% | policy_beta_false_positive_high_mae |
| R10L11_T04_KYERYONG_POLICY_BETA_CAP | 계룡건설 | 2024-03-27 | 14,240 | 4.56% | -11.31% | 8.78% | -11.31% | 9.41% | -11.45% | 2024-08-21 / 15,580 | -19.06% | mid_builder_policy_beta_weak_alignment |
| R10L11_T05_DONGBU_POLICY_BETA_CAP | 동부건설 | 2024-03-27 | 5,030 | 3.98% | -4.47% | 3.98% | -5.57% | 3.98% | -29.03% | 2024-04-26 / 5,230 | -31.74% | policy_beta_late_drawdown_counterexample |
| R10L11_T02B_SHINSEGAE_4B_EVENT_PREMIUM_OVERLAY | 신세계건설 | 2024-09-30 | 18,160 | 0.50% | -0.50% | 1.05% | -1.10% | 1.05% | -1.10% | 2024-12-23 / 18,350 | -2.12% | 4B_overlay_success |


## 13. Current Calibrated Profile Stress Test

| case | current profile likely action | actual path | verdict | adjustment need |
|---|---|---|---|---|
| 대우건설 | Under-credit as generic construction policy beta | Low early MAE, later +33.11% MFE90 | current_profile_missed_structural | Allow survivor/direct-support path to Stage2-Actionable |
| 신세계건설 | Under-credit repair/event-premium path or treat as noisy distress | +75.45% MFE90 with later event premium | current_profile_missed_structural | Add parent/direct-support repair bridge and 4B event overlay |
| DL이앤씨 | Could over-credit policy headline and valuation beta | MFE90 +8.37% vs MAE90 -21.54% | current_profile_false_positive | Cap generic policy beta without direct repair evidence |
| 계룡건설 | Could promote too early on policy beta | MFE180 +9.41% vs persistent high MAE | current_profile_too_early | Require low-MAE confirmation or direct balance-sheet evidence |
| 동부건설 | Could leave as Stage2-watch too long after weak MFE | MFE180 +3.98% vs MAE180 -29.03% | current_profile_false_positive | Add late-drawdown / thesis-break watch guard |

Required questions:

1. Current calibrated profile is directionally right about price-only blowoffs, but too coarse for C30 policy backstops.
2. Actual MFE/MAE shows a clear split: direct-support/survivor cases worked; generic policy beta did not.
3. Stage2 bonus is not globally wrong, but should be conditional in C30.
4. Yellow threshold 75 is not the key issue; evidence composition is.
5. Green threshold 87 / revision 55 should remain strict because PF repair without financial confirmation is fragile.
6. Price-only blowoff guard remains appropriate.
7. Full 4B non-price requirement is strengthened by the Shinsegae event-premium overlay.
8. Hard 4C routing is appropriate for true thesis breaks, but policy-beta failures need a watch/cap state before hard 4C.

## 14. Stage2 / Yellow / Green Comparison

No confirmed Stage3-Green trigger is used as a representative trigger in this loop. Therefore:

```text
green_lateness_ratio = not_applicable
reason = no_confirmed_Stage3_Green_trigger
```

The residual issue is not that Green is too late. It is that C30 Stage2 can become too early if macro policy support is not split from direct repair evidence.

## 15. 4B Local vs Full-window Timing Audit

| trigger | stage2 entry | 4B entry | local proximity | full-window proximity | evidence type | verdict |
|---|---:|---:|---:|---:|---|---|
| R10L11_T02B_SHINSEGAE_4B_EVENT_PREMIUM_OVERLAY | 10,630 | 18,160 | 0.94 | 0.94 | control_premium_or_event_premium | good_full_window_4B_timing |
| 대우건설 July price spike | 3,730 | n/a | n/a | n/a | price_only | do_not_treat_as_full_4B |

The lesson is precise: price strength after a PF stress repair is not itself 4B. A control/event premium near the full observed window peak is 4B overlay evidence.

## 16. 4C Protection Audit

No new hard 4C representative trigger is promoted from this loop. DL이앤씨, 계룡건설, and 동부건설 are treated as **thesis_break_watch_only** / cap cases rather than hard 4C rows. The useful protection mechanism is earlier: stop generic policy beta from entering Stage2-Actionable unless direct support, low-MAE relative strength, or balance-sheet repair is visible.

## 17. Sector-Specific Rule Candidate

```text
rule_id = l9_c30_policy_backstop_split_gate
rule_scope = sector_specific
large_sector_id = L9_CONSTRUCTION_REALESTATE_HOUSING
canonical_archetype_id = C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK
proposal_type = sector_shadow_only
```

Proposed rule:

- If C30 evidence is only a macro policy/liquidity headline, cap the trigger at Stage2-Watch or Stage2-Cap.
- Promote toward Stage2-Actionable only if at least one of the following is present:
  - direct parent/group support,
  - explicit refinancing/deleveraging bridge,
  - large-builder survivor differentiation with low early MAE and relative strength,
  - credible non-price evidence that PF exposure is being ring-fenced or reduced.
- Price-only relief rallies cannot become positive Stage2/3 evidence.

## 18. Canonical-Archetype Rule Candidate

```text
rule_id = c30_direct_support_or_repair_bridge_bonus
rule_scope = canonical_archetype_specific
canonical_archetype_id = C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK
proposal_type = archetype_shadow_only
```

C30 needs a canonical compression axis:

```text
direct_support_or_repair_bridge = +1 shadow component
policy_beta_without_repair = -2 shadow component
control_premium_event_4B_overlay = +1 overlay-only component
```

This does not change production scoring. It creates a ledger-level shadow rule candidate.

## 19. Before / After Backtest Comparison

| profile_id | scope | hypothesis | eligible triggers | avg MFE90 | avg MAE90 | avg MFE180 | avg MAE180 | false positive rate | missed structural count | alignment verdict |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---|
| P0 e2r_2_1_stock_web_calibrated_proxy | current proxy | Macro policy support may over-credit generic C30 beta | 5 | 25.94% | -9.96% | 26.06% | -16.87% | 60% | 2 | mixed; high dispersion |
| P0b e2r_2_0_baseline_reference | rollback reference | Lower Stage2 discrimination, more late-positive misses | 5 | 25.94% | -9.96% | 26.06% | -16.87% | 60% | 3 | weaker |
| P1 sector_specific_candidate_profile | L9 sector | Split direct support from generic policy beta | 5 | 54.28% selected positives | -5.68% selected positives | 54.28% | -11.18% | 0% selected | 0 | strong |
| P2 canonical_archetype_candidate_profile | C30 | Require balance-sheet repair, parent support, or low-MAE relative strength before promotion | 5 | 54.28% selected positives | -5.68% selected positives | 54.28% | -11.18% | 0% selected | 0 | strong |
| P3 counterexample_guard_profile | guardrail | Cap generic policy beta and treat event premium as 4B overlay | 6 | 54.28% selected positives | -5.68% selected positives | 54.28% | -11.18% | 0% selected | 0 | best risk-adjusted |


## 20. Score-Return Alignment Matrix

| case | before stage | after stage | price-return alignment |
|---|---|---|---|
| 대우건설 | Stage2-Watch | Stage2-Actionable | improved: low MAE and +33.11% MFE90 |
| 신세계건설 | Stage2-Watch | Stage2-Actionable + later 4B overlay | improved: +75.45% MFE90, event premium captured as risk overlay |
| DL이앤씨 | Stage2-Actionable | Stage2-Watch / cap | improved: high MAE avoided |
| 계룡건설 | Stage2-Watch | Stage2-Watch-Cap | improved: weak MFE/MAE remains non-promotional |
| 동부건설 | Stage2-Watch | Stage1/Watch | improved: low MFE and late drawdown blocked |

## 21. Coverage Matrix

| large_sector_id | canonical_archetype_id | fine_archetype_id | positive_case_count | counterexample_count | 4B_case_count | 4C_case_count | new_independent_case_count | reused_case_count | calibration_usable_trigger_count | representative_trigger_count | current_profile_error_count | sector_rule_candidate | canonical_rule_candidate | coverage_gap_after_this_loop |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|---|---|
| L9_CONSTRUCTION_REALESTATE_HOUSING | C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK | PF_POLICY_LIQUIDITY_BACKSTOP_DIRECT_SUPPORT_SPLIT | 2 | 3 | 1 | 0 | 5 | 0 | 6 | 5 | 5 | true | true | Need more 2025 direct-deleveraging and PF restructuring cases after clean forward windows become available. |


## 22. Residual Contribution Summary

```text
new_independent_case_count: 5
reused_case_count: 0
reused_case_ids: []
new_symbol_count: 5
new_canonical_archetype_count: 0
new_fine_archetype_count: 4
new_trigger_family_count: 5
tested_existing_calibrated_axes: stage2_actionable_evidence_bonus, stage3_yellow_total_min, stage3_green_total_min, price_only_blowoff_blocks_positive_stage, full_4b_requires_non_price_evidence, hard_4c_thesis_break_routes_to_4c
residual_error_types_found: generic_policy_backstop_false_positive, direct_support_missed_structural, event_premium_4b_overlay_needed, small_mid_builder_late_drawdown
new_axis_proposed: l9_c30_policy_backstop_split_gate, c30_direct_support_or_repair_bridge_bonus, c30_policy_beta_without_repair_penalty, c30_control_premium_event_4b_overlay
existing_axis_strengthened: price_only_blowoff_blocks_positive_stage, full_4b_requires_non_price_evidence, hard_4c_thesis_break_routes_to_4c
existing_axis_weakened: null
existing_axis_kept: stage2_actionable_evidence_bonus, stage3_yellow_total_min, stage3_green_total_min, stage3_green_revision_min, stage3_cross_evidence_green_buffer
sector_specific_rule_candidate: true
canonical_archetype_rule_candidate: true
no_new_signal_reason: null
loop_contribution_label: sector_specific_rule_candidate
do_not_propose_new_weight_delta: false
```

## 23. Validation Scope / Non-Validation Scope

Validated:

- Actual Stock-Web tradable_raw entry rows.
- Actual 30D / 90D / 180D MFE and MAE windows from Stock-Web 1D OHLC.
- Corporate-action window status from symbol profiles.
- Round schedule and large-sector consistency.
- Duplicate avoidance versus previous R10 Loop 10 symbol set.

Not validated:

- No current/live candidate scan.
- No production scoring patch.
- No brokerage or automated trading action.
- No attempt to infer exact `stock_agent` source-code structure.
- No 1Y/2Y calibration for Shinsegae because the profile becomes inactive/delisted-like after early 2025.

## 24. Shadow Weight Calibration

```csv
row_type,axis,scope,large_sector_id,canonical_archetype_id,baseline_value,tested_value,delta,reason,backtest_effect,trigger_ids,calibration_usable_count,new_independent_case_count,counterexample_count,confidence,proposal_type,notes
shadow_weight,l9_c30_policy_backstop_split_gate,sector_specific,L9_CONSTRUCTION_REALESTATE_HOUSING,C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK,0,1,+1,"Macro policy backstop must split direct support / survivor path from generic sector beta","keeps Daewoo/Shinsegae positive while capping DL/Kyeryong/Dongbu false positives","R10L11_T01_DAEWOO_STAGE2_POLICY_BACKSTOP|R10L11_T02_SHINSEGAE_STAGE2_PARENT_SUPPORT|R10L11_T03_DL_POLICY_BETA_CAP|R10L11_T04_KYERYONG_POLICY_BETA_CAP|R10L11_T05_DONGBU_POLICY_BETA_CAP",5,5,3,medium,sector_shadow_only,"not production; post-calibrated residual"
shadow_weight,c30_direct_support_or_repair_bridge_bonus,canonical_archetype_specific,L9_CONSTRUCTION_REALESTATE_HOUSING,C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK,0,1,+1,"Direct parent support, debt repair, or balance-sheet bridge deserves a C30-specific Stage2-Actionable path","raises positive cases without relying on price-only movement","R10L11_T01_DAEWOO_STAGE2_POLICY_BACKSTOP|R10L11_T02_SHINSEGAE_STAGE2_PARENT_SUPPORT",2,2,0,medium,canonical_shadow_only,"not production; requires direct non-price evidence"
shadow_weight,c30_policy_beta_without_repair_penalty,canonical_archetype_specific,L9_CONSTRUCTION_REALESTATE_HOUSING,C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK,0,-2,-2,"Generic policy headline without deleveraging or direct support had weak MFE/MAE alignment","reduces false positive promotion for DL/Kyeryong/Dongbu","R10L11_T03_DL_POLICY_BETA_CAP|R10L11_T04_KYERYONG_POLICY_BETA_CAP|R10L11_T05_DONGBU_POLICY_BETA_CAP",3,3,3,medium,canonical_shadow_only,"not production; cap rather than short signal"
shadow_weight,c30_control_premium_event_4b_overlay,canonical_archetype_specific,L9_CONSTRUCTION_REALESTATE_HOUSING,C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK,0,1,+1,"Control/event premium around a repaired PF thesis should be 4B overlay, not new positive trigger","captures Shinsegae full-window event-premium proximity","R10L11_T02B_SHINSEGAE_4B_EVENT_PREMIUM_OVERLAY",1,0,0,low,overlay_shadow_only,"4B risk calibration only"
```

## 25. Machine-Readable Rows

```jsonl
{"row_type": "price_source_validation", "source": "Songdaiki/stock-web", "source_url": "https://github.com/Songdaiki/stock-web", "manifest_path": "atlas/manifest.json", "schema_path": "atlas/schema.json", "universe_path": "atlas/universe/all_symbols.csv", "manifest_max_date": "2026-02-20", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "raw_shard_root": "atlas/ohlcv_raw_by_symbol_year", "validation_status": "usable_for_historical_calibration"}
{"row_type": "case", "case_id": "R10L11_C30_DAEWOO_202403_POLICY_BACKSTOP_SURVIVOR", "symbol": "047040", "company_name": "대우건설", "round": "R10", "loop": "11", "large_sector_id": "L9_CONSTRUCTION_REALESTATE_HOUSING", "canonical_archetype_id": "C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK", "fine_archetype_id": "PF_POLICY_LIQUIDITY_BACKSTOP_DIRECT_SUPPORT_SPLIT", "case_type": "structural_success", "positive_or_counterexample": "positive", "best_trigger": "R10L11_T01_DAEWOO_STAGE2_POLICY_BACKSTOP", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "after_profile_better", "current_profile_verdict": "current_profile_missed_structural", "price_source": "Songdaiki/stock-web", "notes": "Generic policy support alone is weak, but the market differentiated this large-builder survivor path with low early MAE and later relative strength."}
{"row_type": "case", "case_id": "R10L11_C30_SHINSEGAE_202403_PARENT_SUPPORT_EVENT_PREMIUM", "symbol": "034300", "company_name": "신세계건설", "round": "R10", "loop": "11", "large_sector_id": "L9_CONSTRUCTION_REALESTATE_HOUSING", "canonical_archetype_id": "C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK", "fine_archetype_id": "PF_POLICY_LIQUIDITY_BACKSTOP_DIRECT_SUPPORT_SPLIT", "case_type": "structural_success", "positive_or_counterexample": "positive", "best_trigger": "R10L11_T02_SHINSEGAE_STAGE2_PARENT_SUPPORT", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "after_profile_better", "current_profile_verdict": "current_profile_missed_structural", "price_source": "Songdaiki/stock-web", "notes": "A 2024-02-06 corporate-action candidate exists before entry; entry~D+180 is treated as clean. 1Y/2Y not used because profile becomes inactive/delisted-like after early 2025."}
{"row_type": "case", "case_id": "R10L11_C30_DL_202403_POLICY_REVALUE_FALSE_POSITIVE", "symbol": "375500", "company_name": "DL이앤씨", "round": "R10", "loop": "11", "large_sector_id": "L9_CONSTRUCTION_REALESTATE_HOUSING", "canonical_archetype_id": "C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK", "fine_archetype_id": "PF_POLICY_LIQUIDITY_BACKSTOP_DIRECT_SUPPORT_SPLIT", "case_type": "failed_rerating", "positive_or_counterexample": "counterexample", "best_trigger": "R10L11_T03_DL_POLICY_BETA_CAP", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "after_profile_better", "current_profile_verdict": "current_profile_false_positive", "price_source": "Songdaiki/stock-web", "notes": "A clean 180D window exists; profile has old 2022 CA candidates outside this study window."}
{"row_type": "case", "case_id": "R10L11_C30_KYERYONG_202403_POLICY_REVALUE_FALSE_POSITIVE", "symbol": "013580", "company_name": "계룡건설", "round": "R10", "loop": "11", "large_sector_id": "L9_CONSTRUCTION_REALESTATE_HOUSING", "canonical_archetype_id": "C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK", "fine_archetype_id": "PF_POLICY_LIQUIDITY_BACKSTOP_DIRECT_SUPPORT_SPLIT", "case_type": "failed_rerating", "positive_or_counterexample": "counterexample", "best_trigger": "R10L11_T04_KYERYONG_POLICY_BETA_CAP", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "after_profile_better", "current_profile_verdict": "current_profile_too_early", "price_source": "Songdaiki/stock-web", "notes": "This is a clean 2024 window; only historical 1999 CA candidate is outside the study period."}
{"row_type": "case", "case_id": "R10L11_C30_DONGBU_202403_POLICY_REVALUE_LATE_DRAWDOWN", "symbol": "005960", "company_name": "동부건설", "round": "R10", "loop": "11", "large_sector_id": "L9_CONSTRUCTION_REALESTATE_HOUSING", "canonical_archetype_id": "C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK", "fine_archetype_id": "PF_POLICY_LIQUIDITY_BACKSTOP_DIRECT_SUPPORT_SPLIT", "case_type": "failed_rerating", "positive_or_counterexample": "counterexample", "best_trigger": "R10L11_T05_DONGBU_POLICY_BETA_CAP", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "after_profile_better", "current_profile_verdict": "current_profile_false_positive", "price_source": "Songdaiki/stock-web", "notes": "Profile CA candidates are historical and outside the 2024 study window."}
{"row_type": "trigger", "trigger_id": "R10L11_T01_DAEWOO_STAGE2_POLICY_BACKSTOP", "case_id": "R10L11_C30_DAEWOO_202403_POLICY_BACKSTOP_SURVIVOR", "symbol": "047040", "company_name": "대우건설", "round": "R10", "loop": "11", "large_sector_id": "L9_CONSTRUCTION_REALESTATE_HOUSING", "canonical_archetype_id": "C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK", "fine_archetype_id": "PF_POLICY_LIQUIDITY_BACKSTOP_DIRECT_SUPPORT_SPLIT", "sector": "construction_realestate_housing", "primary_archetype": "PF_balance_sheet_break", "loop_objective": "coverage_gap_fill|residual_false_positive_mining|sector_specific_rule_discovery", "trigger_type": "Stage2-Actionable", "trigger_date": "2024-03-27", "evidence_available_at_that_date": "2024-03-27 Korean policy/liquidity support package for construction firms; large-builder survivor balance-sheet path with later relative-strength confirmation.", "evidence_source": "2024-03-27 Korean policy/liquidity-support report; Stock-Web OHLC row validation; later company/regime context used only for label audit", "stage2_evidence_fields": ["public_event_or_disclosure", "policy_or_regulatory_optionality", "relative_strength"], "stage3_evidence_fields": ["financial_visibility", "low_red_team_risk"], "stage4b_evidence_fields": [], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/047/047040/2024.csv", "profile_path": "atlas/symbol_profiles/047/047040.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "entry_date": "2024-03-27", "entry_price": 3730, "MFE_30D_pct": 3.75, "MFE_90D_pct": 33.11, "MFE_180D_pct": 33.11, "MFE_1Y_pct": null, "MFE_2Y_pct": null, "MAE_30D_pct": -4.02, "MAE_90D_pct": -4.02, "MAE_180D_pct": -15.01, "MAE_1Y_pct": null, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2024-07-18", "peak_price": 4965, "drawdown_after_peak_pct": -36.15, "green_lateness_ratio": "not_applicable:no_confirmed_Stage3_Green_trigger", "four_b_local_peak_proximity": null, "four_b_full_window_peak_proximity": null, "four_b_timing_verdict": "not_applicable", "four_b_evidence_type": [], "four_c_protection_label": "not_applicable", "trigger_outcome_label": "policy_backstop_survivor_success", "current_profile_verdict": "current_profile_missed_structural", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window", "same_entry_group_id": "R10L11_G01_047040_20240327", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false}
{"row_type": "trigger", "trigger_id": "R10L11_T02_SHINSEGAE_STAGE2_PARENT_SUPPORT", "case_id": "R10L11_C30_SHINSEGAE_202403_PARENT_SUPPORT_EVENT_PREMIUM", "symbol": "034300", "company_name": "신세계건설", "round": "R10", "loop": "11", "large_sector_id": "L9_CONSTRUCTION_REALESTATE_HOUSING", "canonical_archetype_id": "C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK", "fine_archetype_id": "PF_POLICY_LIQUIDITY_BACKSTOP_DIRECT_SUPPORT_SPLIT", "sector": "construction_realestate_housing", "primary_archetype": "PF_balance_sheet_break", "loop_objective": "coverage_gap_fill|residual_false_positive_mining|sector_specific_rule_discovery", "trigger_type": "Stage2-Actionable", "trigger_date": "2024-03-27", "evidence_available_at_that_date": "PF stress was reframed by parent-support / direct balance-sheet repair optionality; later control-premium/event-premium path validated the support bridge rather than generic sector beta.", "evidence_source": "2024-03-27 Korean policy/liquidity-support report; Stock-Web OHLC row validation; later company/regime context used only for label audit", "stage2_evidence_fields": ["public_event_or_disclosure", "policy_or_regulatory_optionality", "financial_visibility"], "stage3_evidence_fields": ["multiple_public_sources", "low_red_team_risk"], "stage4b_evidence_fields": ["control_premium_or_event_premium"], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/034/034300/2024.csv", "profile_path": "atlas/symbol_profiles/034/034300.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "entry_date": "2024-03-27", "entry_price": 10630, "MFE_30D_pct": 8.75, "MFE_90D_pct": 75.45, "MFE_180D_pct": 75.45, "MFE_1Y_pct": null, "MFE_2Y_pct": null, "MAE_30D_pct": -6.11, "MAE_90D_pct": -7.34, "MAE_180D_pct": -7.34, "MAE_1Y_pct": null, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2024-05-30", "peak_price": 18650, "drawdown_after_peak_pct": -47.18, "green_lateness_ratio": "not_applicable:no_confirmed_Stage3_Green_trigger", "four_b_local_peak_proximity": null, "four_b_full_window_peak_proximity": null, "four_b_timing_verdict": "not_applicable", "four_b_evidence_type": [], "four_c_protection_label": "not_applicable", "trigger_outcome_label": "direct_support_event_premium_success", "current_profile_verdict": "current_profile_missed_structural", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window", "same_entry_group_id": "R10L11_G02_034300_20240327", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false}
{"row_type": "trigger", "trigger_id": "R10L11_T03_DL_POLICY_BETA_CAP", "case_id": "R10L11_C30_DL_202403_POLICY_REVALUE_FALSE_POSITIVE", "symbol": "375500", "company_name": "DL이앤씨", "round": "R10", "loop": "11", "large_sector_id": "L9_CONSTRUCTION_REALESTATE_HOUSING", "canonical_archetype_id": "C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK", "fine_archetype_id": "PF_POLICY_LIQUIDITY_BACKSTOP_DIRECT_SUPPORT_SPLIT", "sector": "construction_realestate_housing", "primary_archetype": "PF_balance_sheet_break", "loop_objective": "coverage_gap_fill|residual_false_positive_mining|sector_specific_rule_discovery", "trigger_type": "Stage2-Cap", "trigger_date": "2024-03-27", "evidence_available_at_that_date": "Generic PF policy support and construction-sector repricing did not convert into clean balance-sheet repair or margin visibility.", "evidence_source": "2024-03-27 Korean policy/liquidity-support report; Stock-Web OHLC row validation; later company/regime context used only for label audit", "stage2_evidence_fields": ["public_event_or_disclosure", "policy_or_regulatory_optionality"], "stage3_evidence_fields": [], "stage4b_evidence_fields": ["valuation_blowoff"], "stage4c_evidence_fields": ["thesis_evidence_broken"], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/375/375500/2024.csv", "profile_path": "atlas/symbol_profiles/375/375500.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "entry_date": "2024-03-27", "entry_price": 36450, "MFE_30D_pct": 3.7, "MFE_90D_pct": 8.37, "MFE_180D_pct": 8.37, "MFE_1Y_pct": null, "MFE_2Y_pct": null, "MAE_30D_pct": -12.35, "MAE_90D_pct": -21.54, "MAE_180D_pct": -21.54, "MAE_1Y_pct": null, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2024-06-13", "peak_price": 39500, "drawdown_after_peak_pct": -27.59, "green_lateness_ratio": "not_applicable:no_confirmed_Stage3_Green_trigger", "four_b_local_peak_proximity": null, "four_b_full_window_peak_proximity": null, "four_b_timing_verdict": "not_applicable", "four_b_evidence_type": [], "four_c_protection_label": "thesis_break_watch_only", "trigger_outcome_label": "policy_beta_false_positive_high_mae", "current_profile_verdict": "current_profile_false_positive", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window", "same_entry_group_id": "R10L11_G03_375500_20240327", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false}
{"row_type": "trigger", "trigger_id": "R10L11_T04_KYERYONG_POLICY_BETA_CAP", "case_id": "R10L11_C30_KYERYONG_202403_POLICY_REVALUE_FALSE_POSITIVE", "symbol": "013580", "company_name": "계룡건설", "round": "R10", "loop": "11", "large_sector_id": "L9_CONSTRUCTION_REALESTATE_HOUSING", "canonical_archetype_id": "C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK", "fine_archetype_id": "PF_POLICY_LIQUIDITY_BACKSTOP_DIRECT_SUPPORT_SPLIT", "sector": "construction_realestate_housing", "primary_archetype": "PF_balance_sheet_break", "loop_objective": "coverage_gap_fill|residual_false_positive_mining|sector_specific_rule_discovery", "trigger_type": "Stage2-Cap", "trigger_date": "2024-03-27", "evidence_available_at_that_date": "Medium-builder policy beta did not produce enough MFE relative to early and later drawdown; no direct deleveraging or parent-support bridge.", "evidence_source": "2024-03-27 Korean policy/liquidity-support report; Stock-Web OHLC row validation; later company/regime context used only for label audit", "stage2_evidence_fields": ["public_event_or_disclosure", "policy_or_regulatory_optionality"], "stage3_evidence_fields": [], "stage4b_evidence_fields": [], "stage4c_evidence_fields": ["thesis_evidence_broken"], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/013/013580/2024.csv", "profile_path": "atlas/symbol_profiles/013/013580.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "entry_date": "2024-03-27", "entry_price": 14240, "MFE_30D_pct": 4.56, "MFE_90D_pct": 8.78, "MFE_180D_pct": 9.41, "MFE_1Y_pct": null, "MFE_2Y_pct": null, "MAE_30D_pct": -11.31, "MAE_90D_pct": -11.31, "MAE_180D_pct": -11.45, "MAE_1Y_pct": null, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2024-08-21", "peak_price": 15580, "drawdown_after_peak_pct": -19.06, "green_lateness_ratio": "not_applicable:no_confirmed_Stage3_Green_trigger", "four_b_local_peak_proximity": null, "four_b_full_window_peak_proximity": null, "four_b_timing_verdict": "not_applicable", "four_b_evidence_type": [], "four_c_protection_label": "thesis_break_watch_only", "trigger_outcome_label": "mid_builder_policy_beta_weak_alignment", "current_profile_verdict": "current_profile_too_early", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window", "same_entry_group_id": "R10L11_G04_013580_20240327", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false}
{"row_type": "trigger", "trigger_id": "R10L11_T05_DONGBU_POLICY_BETA_CAP", "case_id": "R10L11_C30_DONGBU_202403_POLICY_REVALUE_LATE_DRAWDOWN", "symbol": "005960", "company_name": "동부건설", "round": "R10", "loop": "11", "large_sector_id": "L9_CONSTRUCTION_REALESTATE_HOUSING", "canonical_archetype_id": "C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK", "fine_archetype_id": "PF_POLICY_LIQUIDITY_BACKSTOP_DIRECT_SUPPORT_SPLIT", "sector": "construction_realestate_housing", "primary_archetype": "PF_balance_sheet_break", "loop_objective": "coverage_gap_fill|residual_false_positive_mining|sector_specific_rule_discovery", "trigger_type": "Stage2-Cap", "trigger_date": "2024-03-27", "evidence_available_at_that_date": "Policy-liquidity headline did not repair small/mid-builder balance-sheet risk; low MFE and late drawdown argue for watch/cap rather than Stage2 promotion.", "evidence_source": "2024-03-27 Korean policy/liquidity-support report; Stock-Web OHLC row validation; later company/regime context used only for label audit", "stage2_evidence_fields": ["public_event_or_disclosure", "policy_or_regulatory_optionality"], "stage3_evidence_fields": [], "stage4b_evidence_fields": [], "stage4c_evidence_fields": ["thesis_evidence_broken"], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/005/005960/2024.csv", "profile_path": "atlas/symbol_profiles/005/005960.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "entry_date": "2024-03-27", "entry_price": 5030, "MFE_30D_pct": 3.98, "MFE_90D_pct": 3.98, "MFE_180D_pct": 3.98, "MFE_1Y_pct": null, "MFE_2Y_pct": null, "MAE_30D_pct": -4.47, "MAE_90D_pct": -5.57, "MAE_180D_pct": -29.03, "MAE_1Y_pct": null, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2024-04-26", "peak_price": 5230, "drawdown_after_peak_pct": -31.74, "green_lateness_ratio": "not_applicable:no_confirmed_Stage3_Green_trigger", "four_b_local_peak_proximity": null, "four_b_full_window_peak_proximity": null, "four_b_timing_verdict": "not_applicable", "four_b_evidence_type": [], "four_c_protection_label": "thesis_break_watch_only", "trigger_outcome_label": "policy_beta_late_drawdown_counterexample", "current_profile_verdict": "current_profile_false_positive", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window", "same_entry_group_id": "R10L11_G05_005960_20240327", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false}
{"row_type": "trigger", "trigger_id": "R10L11_T02B_SHINSEGAE_4B_EVENT_PREMIUM_OVERLAY", "case_id": "R10L11_C30_SHINSEGAE_202403_PARENT_SUPPORT_EVENT_PREMIUM", "symbol": "034300", "company_name": "신세계건설", "round": "R10", "loop": "11", "large_sector_id": "L9_CONSTRUCTION_REALESTATE_HOUSING", "canonical_archetype_id": "C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK", "fine_archetype_id": "PF_POLICY_LIQUIDITY_BACKSTOP_DIRECT_SUPPORT_SPLIT", "sector": "construction_realestate_housing", "primary_archetype": "PF_balance_sheet_break", "loop_objective": "4B_non_price_requirement_stress_test", "trigger_type": "4B-overlay", "trigger_date": "2024-09-30", "entry_date": "2024-09-30", "entry_price": 18160, "evidence_available_at_that_date": "Control/event-premium trading regime after direct support path; not a positive Stage2 trigger, but a risk overlay on the repaired thesis.", "evidence_source": "Stock-Web OHLC event-premium plateau validation; company-event source enrichment deferred to implementation ledger", "stage2_evidence_fields": [], "stage3_evidence_fields": [], "stage4b_evidence_fields": ["valuation_blowoff", "control_premium_or_event_premium", "positioning_overheat"], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/034/034300/2024.csv", "profile_path": "atlas/symbol_profiles/034/034300.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": 0.5, "MFE_90D_pct": 1.05, "MFE_180D_pct": 1.05, "MFE_1Y_pct": null, "MFE_2Y_pct": null, "MAE_30D_pct": -0.5, "MAE_90D_pct": -1.1, "MAE_180D_pct": -1.1, "MAE_1Y_pct": null, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2024-12-23", "peak_price": 18350, "drawdown_after_peak_pct": -2.12, "green_lateness_ratio": "not_applicable:4B_overlay", "four_b_local_peak_proximity": 0.94, "four_b_full_window_peak_proximity": 0.94, "four_b_timing_verdict": "good_full_window_4B_timing", "four_b_evidence_type": ["control_premium_or_event_premium"], "four_c_protection_label": "not_applicable", "trigger_outcome_label": "4B_overlay_success", "current_profile_verdict": "current_profile_4B_too_late", "calibration_usable": true, "forward_window_trading_days": 60, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window_for_prior_stage;4B_overlay_short_window", "same_entry_group_id": "R10L11_G02B_034300_20240930", "dedupe_for_aggregate": false, "aggregate_group_role": "4B_overlay_only", "is_new_independent_case": false, "reuse_reason": "same_case_4B_overlay_not_new_case", "independent_evidence_weight": 0.25, "do_not_count_as_new_case": true}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R10L11_C30_DAEWOO_202403_POLICY_BACKSTOP_SURVIVOR", "trigger_id": "R10L11_T01_DAEWOO_STAGE2_POLICY_BACKSTOP", "symbol": "047040", "large_sector_id": "L9_CONSTRUCTION_REALESTATE_HOUSING", "canonical_archetype_id": "C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK", "raw_component_scores_before": {"contract_score": 4, "backlog_visibility_score": 5, "margin_bridge_score": 3, "revision_score": 2, "relative_strength_score": 5, "customer_quality_score": 0, "policy_or_regulatory_score": 8, "valuation_repricing_score": 5, "execution_risk_score": -2, "legal_or_contract_risk_score": -1, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_before": 74, "stage_label_before": "Stage2-Watch", "raw_component_scores_after": {"contract_score": 5, "backlog_visibility_score": 6, "margin_bridge_score": 3, "revision_score": 2, "relative_strength_score": 8, "customer_quality_score": 0, "policy_or_regulatory_score": 8, "valuation_repricing_score": 5, "execution_risk_score": -1, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_after": 79, "stage_label_after": "Stage2-Actionable", "changed_components": ["policy_or_regulatory_score", "execution_risk_score", "relative_strength_score", "valuation_repricing_score"], "component_delta_explanation": "C30 policy-liquidity evidence is split between direct repair/support and generic sector beta; generic support is capped unless supported by balance-sheet repair, parent support, or low-MAE relative strength.", "MFE_90D_pct": 33.11, "MAE_90D_pct": -4.02, "score_return_alignment_label": "after_profile_better", "current_profile_verdict": "current_profile_missed_structural"}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R10L11_C30_SHINSEGAE_202403_PARENT_SUPPORT_EVENT_PREMIUM", "trigger_id": "R10L11_T02_SHINSEGAE_STAGE2_PARENT_SUPPORT", "symbol": "034300", "large_sector_id": "L9_CONSTRUCTION_REALESTATE_HOUSING", "canonical_archetype_id": "C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK", "raw_component_scores_before": {"contract_score": 2, "backlog_visibility_score": 3, "margin_bridge_score": 1, "revision_score": 1, "relative_strength_score": 4, "customer_quality_score": 0, "policy_or_regulatory_score": 7, "valuation_repricing_score": 5, "execution_risk_score": -4, "legal_or_contract_risk_score": -2, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_before": 68, "stage_label_before": "Stage2-Watch", "raw_component_scores_after": {"contract_score": 3, "backlog_visibility_score": 4, "margin_bridge_score": 2, "revision_score": 1, "relative_strength_score": 8, "customer_quality_score": 0, "policy_or_regulatory_score": 7, "valuation_repricing_score": 8, "execution_risk_score": -1, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_after": 81, "stage_label_after": "Stage2-Actionable", "changed_components": ["policy_or_regulatory_score", "execution_risk_score", "relative_strength_score", "valuation_repricing_score"], "component_delta_explanation": "C30 policy-liquidity evidence is split between direct repair/support and generic sector beta; generic support is capped unless supported by balance-sheet repair, parent support, or low-MAE relative strength.", "MFE_90D_pct": 75.45, "MAE_90D_pct": -7.34, "score_return_alignment_label": "after_profile_better", "current_profile_verdict": "current_profile_missed_structural"}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R10L11_C30_DL_202403_POLICY_REVALUE_FALSE_POSITIVE", "trigger_id": "R10L11_T03_DL_POLICY_BETA_CAP", "symbol": "375500", "large_sector_id": "L9_CONSTRUCTION_REALESTATE_HOUSING", "canonical_archetype_id": "C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK", "raw_component_scores_before": {"contract_score": 4, "backlog_visibility_score": 5, "margin_bridge_score": 2, "revision_score": 1, "relative_strength_score": 4, "customer_quality_score": 0, "policy_or_regulatory_score": 8, "valuation_repricing_score": 5, "execution_risk_score": -2, "legal_or_contract_risk_score": -1, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_before": 76, "stage_label_before": "Stage2-Actionable", "raw_component_scores_after": {"contract_score": 4, "backlog_visibility_score": 5, "margin_bridge_score": 1, "revision_score": 0, "relative_strength_score": 3, "customer_quality_score": 0, "policy_or_regulatory_score": 5, "valuation_repricing_score": 3, "execution_risk_score": -5, "legal_or_contract_risk_score": -2, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_after": 67, "stage_label_after": "Stage2-Watch", "changed_components": ["policy_or_regulatory_score", "execution_risk_score", "relative_strength_score", "valuation_repricing_score"], "component_delta_explanation": "C30 policy-liquidity evidence is split between direct repair/support and generic sector beta; generic support is capped unless supported by balance-sheet repair, parent support, or low-MAE relative strength.", "MFE_90D_pct": 8.37, "MAE_90D_pct": -21.54, "score_return_alignment_label": "after_profile_better", "current_profile_verdict": "current_profile_false_positive"}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R10L11_C30_KYERYONG_202403_POLICY_REVALUE_FALSE_POSITIVE", "trigger_id": "R10L11_T04_KYERYONG_POLICY_BETA_CAP", "symbol": "013580", "large_sector_id": "L9_CONSTRUCTION_REALESTATE_HOUSING", "canonical_archetype_id": "C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK", "raw_component_scores_before": {"contract_score": 3, "backlog_visibility_score": 4, "margin_bridge_score": 1, "revision_score": 1, "relative_strength_score": 4, "customer_quality_score": 0, "policy_or_regulatory_score": 8, "valuation_repricing_score": 4, "execution_risk_score": -2, "legal_or_contract_risk_score": -1, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_before": 73, "stage_label_before": "Stage2-Watch", "raw_component_scores_after": {"contract_score": 3, "backlog_visibility_score": 4, "margin_bridge_score": 1, "revision_score": 0, "relative_strength_score": 3, "customer_quality_score": 0, "policy_or_regulatory_score": 5, "valuation_repricing_score": 3, "execution_risk_score": -4, "legal_or_contract_risk_score": -2, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_after": 65, "stage_label_after": "Stage2-Watch-Cap", "changed_components": ["policy_or_regulatory_score", "execution_risk_score", "relative_strength_score", "valuation_repricing_score"], "component_delta_explanation": "C30 policy-liquidity evidence is split between direct repair/support and generic sector beta; generic support is capped unless supported by balance-sheet repair, parent support, or low-MAE relative strength.", "MFE_90D_pct": 8.78, "MAE_90D_pct": -11.31, "score_return_alignment_label": "after_profile_better", "current_profile_verdict": "current_profile_too_early"}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R10L11_C30_DONGBU_202403_POLICY_REVALUE_LATE_DRAWDOWN", "trigger_id": "R10L11_T05_DONGBU_POLICY_BETA_CAP", "symbol": "005960", "large_sector_id": "L9_CONSTRUCTION_REALESTATE_HOUSING", "canonical_archetype_id": "C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK", "raw_component_scores_before": {"contract_score": 2, "backlog_visibility_score": 3, "margin_bridge_score": 0, "revision_score": 0, "relative_strength_score": 3, "customer_quality_score": 0, "policy_or_regulatory_score": 8, "valuation_repricing_score": 3, "execution_risk_score": -2, "legal_or_contract_risk_score": -1, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_before": 71, "stage_label_before": "Stage2-Watch", "raw_component_scores_after": {"contract_score": 2, "backlog_visibility_score": 3, "margin_bridge_score": 0, "revision_score": 0, "relative_strength_score": 2, "customer_quality_score": 0, "policy_or_regulatory_score": 4, "valuation_repricing_score": 2, "execution_risk_score": -6, "legal_or_contract_risk_score": -3, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_after": 61, "stage_label_after": "Stage1/Watch", "changed_components": ["policy_or_regulatory_score", "execution_risk_score", "relative_strength_score", "valuation_repricing_score"], "component_delta_explanation": "C30 policy-liquidity evidence is split between direct repair/support and generic sector beta; generic support is capped unless supported by balance-sheet repair, parent support, or low-MAE relative strength.", "MFE_90D_pct": 3.98, "MAE_90D_pct": -5.57, "score_return_alignment_label": "after_profile_better", "current_profile_verdict": "current_profile_false_positive"}
{"row_type": "residual_contribution", "round": "R10", "loop": "11", "scheduled_round": "R10", "scheduled_loop": 11, "round_schedule_status": "valid", "round_sector_consistency": "pass", "large_sector_id": "L9_CONSTRUCTION_REALESTATE_HOUSING", "canonical_archetype_id": "C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK", "new_independent_case_count": 5, "reused_case_count": 0, "new_symbol_count": 5, "same_archetype_new_symbol_count": 5, "same_archetype_new_trigger_family_count": 5, "new_trigger_family_count": 5, "positive_case_count": 2, "counterexample_count": 3, "current_profile_error_count": 5, "tested_existing_calibrated_axes": ["stage2_actionable_evidence_bonus", "stage3_yellow_total_min", "stage3_green_total_min", "price_only_blowoff_blocks_positive_stage", "full_4b_requires_non_price_evidence", "hard_4c_thesis_break_routes_to_4c"], "residual_error_types_found": ["generic_policy_backstop_false_positive", "direct_support_missed_structural", "event_premium_4b_overlay_needed", "small_mid_builder_late_drawdown"], "diversity_score_summary": "new_symbol +15; same_archetype_new_symbol +20; counterexample_gap +12; residual_error +25; wrong_round_penalty 0; duplicate penalties 0", "loop_contribution_label": "sector_specific_rule_candidate", "do_not_propose_new_weight_delta": false}
```

```csv
row_type,axis,scope,large_sector_id,canonical_archetype_id,baseline_value,tested_value,delta,reason,backtest_effect,trigger_ids,calibration_usable_count,new_independent_case_count,counterexample_count,confidence,proposal_type,notes
shadow_weight,l9_c30_policy_backstop_split_gate,sector_specific,L9_CONSTRUCTION_REALESTATE_HOUSING,C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK,0,1,+1,"Macro policy backstop must split direct support / survivor path from generic sector beta","keeps Daewoo/Shinsegae positive while capping DL/Kyeryong/Dongbu false positives","R10L11_T01_DAEWOO_STAGE2_POLICY_BACKSTOP|R10L11_T02_SHINSEGAE_STAGE2_PARENT_SUPPORT|R10L11_T03_DL_POLICY_BETA_CAP|R10L11_T04_KYERYONG_POLICY_BETA_CAP|R10L11_T05_DONGBU_POLICY_BETA_CAP",5,5,3,medium,sector_shadow_only,"not production; post-calibrated residual"
shadow_weight,c30_direct_support_or_repair_bridge_bonus,canonical_archetype_specific,L9_CONSTRUCTION_REALESTATE_HOUSING,C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK,0,1,+1,"Direct parent support, debt repair, or balance-sheet bridge deserves a C30-specific Stage2-Actionable path","raises positive cases without relying on price-only movement","R10L11_T01_DAEWOO_STAGE2_POLICY_BACKSTOP|R10L11_T02_SHINSEGAE_STAGE2_PARENT_SUPPORT",2,2,0,medium,canonical_shadow_only,"not production; requires direct non-price evidence"
shadow_weight,c30_policy_beta_without_repair_penalty,canonical_archetype_specific,L9_CONSTRUCTION_REALESTATE_HOUSING,C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK,0,-2,-2,"Generic policy headline without deleveraging or direct support had weak MFE/MAE alignment","reduces false positive promotion for DL/Kyeryong/Dongbu","R10L11_T03_DL_POLICY_BETA_CAP|R10L11_T04_KYERYONG_POLICY_BETA_CAP|R10L11_T05_DONGBU_POLICY_BETA_CAP",3,3,3,medium,canonical_shadow_only,"not production; cap rather than short signal"
shadow_weight,c30_control_premium_event_4b_overlay,canonical_archetype_specific,L9_CONSTRUCTION_REALESTATE_HOUSING,C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK,0,1,+1,"Control/event premium around a repaired PF thesis should be 4B overlay, not new positive trigger","captures Shinsegae full-window event-premium proximity","R10L11_T02B_SHINSEGAE_4B_EVENT_PREMIUM_OVERLAY",1,0,0,low,overlay_shadow_only,"4B risk calibration only"
```

## 26. Deferred Coding Agent Handoff Prompt

### Purpose

You are now in the repository implementation phase. The attached Markdown files are v12 post-calibrated residual research outputs produced using the Songdaiki/stock-web OHLC atlas.

These MDs are not live candidate research. They are historical calibration research designed to extend the already-applied e2r_2_1_stock_web_calibrated profile.

Do not blindly apply every shadow row.
Ingest the machine-readable rows and update the sector/canonical-archetype calibration ledger.

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
completed_round = R10
completed_loop = 11
next_round = R11
next_loop = 11
round_schedule_status = valid
round_sector_consistency = pass
```

## 28. Source Notes

- Primary price atlas: Songdaiki/stock-web.
- Manifest: `atlas/manifest.json`.
- Schema: `atlas/schema.json`.
- Price basis: `tradable_raw`.
- Price adjustment status: `raw_unadjusted_marcap`.
- Representative price shards:
  - `atlas/ohlcv_tradable_by_symbol_year/047/047040/2024.csv`
  - `atlas/ohlcv_tradable_by_symbol_year/034/034300/2024.csv`
  - `atlas/ohlcv_tradable_by_symbol_year/375/375500/2024.csv`
  - `atlas/ohlcv_tradable_by_symbol_year/013/013580/2024.csv`
  - `atlas/ohlcv_tradable_by_symbol_year/005/005960/2024.csv`
- Evidence notes use historical macro and company/regime context only; no live recommendation language is present.
