# E2R Stock-Web Historical Calibration / Sector-Archetype Residual Research Round

## 0. Research Metadata

```json
{
  "scheduled_round": "R1",
  "scheduled_loop": 12,
  "round_schedule_status": "valid",
  "round_sector_consistency": "pass",
  "completed_round": "R1",
  "completed_loop": 12,
  "next_round": "R2",
  "next_loop": 12,
  "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID",
  "canonical_archetype_id": "C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY",
  "fine_archetype_id": "CZECH_NUCLEAR_PREFERRED_BIDDER_DIRECT_BRIDGE_VS_POLICY_SPIKE",
  "loop_objective": [
    "coverage_gap_fill",
    "sector_specific_rule_discovery",
    "canonical_archetype_compression",
    "counterexample_mining",
    "4B_non_price_requirement_stress_test",
    "4C_thesis_break_timing_test",
    "stage2_actionable_bonus_stress_test"
  ],
  "price_source": "Songdaiki/stock-web",
  "stock_web_manifest_max_date": "2026-02-20",
  "price_basis": "tradable_raw",
  "price_adjustment_status": "raw_unadjusted_marcap",
  "new_independent_case_count": 5,
  "reused_case_count": 0,
  "new_symbol_count": 5,
  "same_archetype_new_symbol_count": 5,
  "same_archetype_new_trigger_family_count": 1,
  "new_trigger_family_count": 1,
  "calibration_usable_case_count": 5,
  "calibration_usable_trigger_count": 8,
  "positive_case_count": 3,
  "counterexample_count": 2,
  "current_profile_error_count": 3,
  "diversity_score_summary": "same_archetype_new_symbol +20, counterexample_gap +8, residual_error +15, new_trigger_family +4, wrong_round_penalty 0; estimated total +47",
  "do_not_propose_new_weight_delta": false,
  "sector_specific_rule_candidate": true,
  "canonical_archetype_rule_candidate": true,
  "loop_contribution_label": "canonical_archetype_rule_candidate",
  "new_axis_proposed": [
    "C04_direct_project_role_bridge_required_for_green",
    "C04_policy_headline_gap_requires_high_MAE_guard",
    "C04_legal_delay_watch_to_4C_route"
  ],
  "existing_axis_strengthened": [
    "full_4b_requires_non_price_evidence",
    "price_only_blowoff_blocks_positive_stage",
    "hard_4c_thesis_break_routes_to_4c"
  ],
  "existing_axis_weakened": []
}
```

One-line contribution:

```text
This loop adds 5 new independent cases, 2 counterexamples, and 3 residual errors for R1/L1_INDUSTRIALS_INFRA_DEFENSE_GRID/C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY.
```

## 1. Current Calibrated Profile Assumption

```text
current_default_profile_proxy = e2r_2_1_stock_web_calibrated
previous_baseline_reference = e2r_2_0_baseline
stage2_actionable_evidence_bonus = +2.0
stage3_yellow_total_min = 75.0
stage3_green_total_min = 87.0
stage3_green_revision_min = 55.0
stage3_cross_evidence_green_buffer = +1.5
price_only_blowoff_blocks_positive_stage = true
full_4b_requires_non_price_evidence = true
hard_4c_thesis_break_routes_to_4c = true
```

This loop does not re-prove the global profile. It stress-tests the calibrated profile on a fresh R1/C04 coverage gap: nuclear policy and project events where a national tender headline can look like a full rerating but the stock path depends on direct project role, contract conversion, legal delay risk, and whether the event-day gap becomes a local peak.

## 2. Round / Large Sector / Canonical Archetype Scope

```text
scheduled_round = R1
scheduled_loop = 12
large_sector_id = L1_INDUSTRIALS_INFRA_DEFENSE_GRID
canonical_archetype_id = C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY
fine_archetype_id = CZECH_NUCLEAR_PREFERRED_BIDDER_DIRECT_BRIDGE_VS_POLICY_SPIKE
round_sector_consistency = pass
```

R1 is the correct scheduled round after the prior R13/Loop 11 completion. R1 maps to L1_INDUSTRIALS_INFRA_DEFENSE_GRID, so the sector gate passes. C04 was selected because local prior R1 files covered C02 power-grid/data-center capex and C03 defense-export backlog, leaving nuclear policy/project-delay logic under-covered.

## 3. Previous Coverage / Duplicate Avoidance Check

Local v12 outputs inspected for duplicate avoidance:

- R1 Loop 10: `C02_POWER_GRID_DATACENTER_CAPEX`.
- R1 Loop 11: `C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG`.
- R13 Loop 11: cross-archetype 4B/4C redteam checkpoint.

No local v12 C04 file was found in `/mnt/data`. The selected cases use a new canonical archetype, new trigger family, and five symbols not counted in the previous C02/C03 R1 loop files for this archetype. Reused case count is zero.

## 4. Stock-Web OHLC Input / Price Source Validation

The stock-web manifest was inspected before case selection.

```json
{
  "source_name": "FinanceData/marcap",
  "source_repo_url": "https://github.com/FinanceData/marcap",
  "price_adjustment_status": "raw_unadjusted_marcap",
  "min_date": "1995-05-02",
  "max_date": "2026-02-20",
  "tradable_row_count": 14354401,
  "raw_row_count": 15214118,
  "symbol_count": 5414,
  "active_like_symbol_count": 2868,
  "inactive_or_delisted_like_symbol_count": 2546,
  "markets": [
    "KONEX",
    "KOSDAQ",
    "KOSDAQ GLOBAL",
    "KOSPI"
  ],
  "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year",
  "raw_shard_root": "atlas/ohlcv_raw_by_symbol_year",
  "schema_path": "atlas/schema.json",
  "universe_path": "atlas/universe/all_symbols.csv"
}
```

Validation conclusion:

```text
price_data_source = Songdaiki/stock-web
upstream_source = FinanceData/marcap
price_basis = tradable_raw
price_adjustment_status = raw_unadjusted_marcap
stock_web_manifest_max_date = 2026-02-20
calibration_shard_root = atlas/ohlcv_tradable_by_symbol_year
validation_status = usable_for_historical_calibration
```

Raw/unadjusted OHLC means this loop treats corporate-action contaminated windows as blocked. The five 2024-07-18 entry windows were checked against profile caveats. 034020 has historical corporate-action candidates in 2019/2020, 083650 in 2006/2015, and 100840 in 2008 plus 2024-04/05, none overlapping the 2024-07-18 to D+180 windows used here. 052690 and 051600 show no corporate-action candidates.

## 5. Historical Eligibility Gate

All representative Stage2-Actionable rows pass the historical eligibility gate.

```text
trigger_date_is_past = true
entry_date_in_tradable_shard = true
entry_date = 2024-07-18 for all representative cases
entry_price = close column on entry_date
forward_180D_available_by_manifest_max_date = true
corporate_action_contaminated_180D_window = false
calibration_usable_case_count = 5
calibration_usable_representative_trigger_count = 5
```

1Y fields are left non-primary in this MD because the loop objective is 30D/90D/180D residual calibration. 2Y is unavailable from 2024-07-18 under stock-web max date 2026-02-20, so 2Y is not used for calibration.

## 6. Canonical Archetype Compression Map

```text
canonical_archetype_id = C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY
fine_archetype = CZECH_NUCLEAR_PREFERRED_BIDDER_DIRECT_BRIDGE_VS_POLICY_SPIKE
```

Compression rule:

```text
policy_headline_only -> Stage2-Watch or Stage2-Actionable, not Green
direct_project_role + commercial bridge -> Stage2-Actionable / Stage3-Yellow candidate
confirmed contract + revision/margin bridge -> Stage3-Green candidate
legal stay / appeal / contract signing block -> 4B overlay first; hard 4C only if thesis evidence breaks
```

The C04 archetype behaves like a bridge inspection. The headline is the truck entering the bridge; the question is whether the bridge actually reaches earnings. A design pure-play with a huge gap but no direct contract conversion can fall through the middle, while an O&M or equipment route can walk across later after a frightening first wobble.

## 7. Case Selection Summary

| case_id | symbol | company | role | trigger | entry | entry_price | MFE30 | MAE30 | MFE180 | MAE180 | current verdict |
|---|---:|---|---|---|---|---:|---:|---:|---:|---:|---|
| R1L12_C04_051600_CZECH_MAINTENANCE_BRIDGE | 051600 | 한전KPS | structural_success | 2024-07-17 | 2024-07-18 | 38,900 | 21.98 | -7.84 | 23.65 | -7.84 | current_profile_correct |
| R1L12_C04_083650_CZECH_BOILER_EQUIPMENT_HIGH_BETA | 083650 | 비에이치아이 | high_mae_success | 2024-07-17 | 2024-07-18 | 8,810 | 19.52 | -19.41 | 181.5 | -20.54 | current_profile_too_late |
| R1L12_C04_100840_CZECH_HEAT_EXCHANGER_SUPPLY_CHAIN | 100840 | SNT에너지 | structural_success | 2024-07-17 | 2024-07-18 | 12,030 | 31.92 | -16.04 | 219.2 | -16.04 | current_profile_too_late |
| R1L12_C04_034020_CZECH_NSSS_HIGH_MAE | 034020 | 두산에너빌리티 | high_mae_success | 2024-07-17 | 2024-07-18 | 21,000 | 19.05 | -27.86 | 45.48 | -27.86 | current_profile_4B_too_early |
| R1L12_C04_052690_CZECH_DESIGN_PURE_PLAY_SPIKE | 052690 | 한전기술 | false_positive_green | 2024-07-17 | 2024-07-18 | 82,000 | 19.63 | -24.88 | 19.63 | -39.27 | current_profile_false_positive |


Selection logic:

```text
positive_structural_success = 3
counterexample_or_failed_rerating = 2
4B_overlay_case = 3
4C_watch_case = 1 narrative-only, not quantitative
minimum_new_symbol_count = pass
minimum_counterexample_count = pass
minimum_positive_case_count = pass
minimum_calibration_usable_case_count = pass
```

## 8. Positive vs Counterexample Balance

Positive cases are 051600, 083650, and 100840. Their evidence bridge is not merely “nuclear theme up”; each has a plausible service/equipment/supply-chain route where delayed confirmation still produced a positive 180D path.

Counterexamples are 052690 and 034020 for different reasons. 052690 is the cleanest false-positive path: the event-day high was the full-window peak, and the 180D low reached -39.09% from entry. 034020 is not a failed thesis in price terms because MFE_180D reached +45.48%, but the -27.86% MAE and event-day local spike mean a calibrated profile should not label the first gap as clean Green.

## 9. Evidence Source Map

| evidence date | evidence family | source class | used for score? | notes |
|---|---|---|---|---|
| 2024-07-17 | KHNP selected as preferred bidder for Czech Dukovany nuclear reactors | Reuters / public tender announcement | yes, Stage2 only | National project headline; not yet direct company contract/revision evidence. |
| 2024-07-18 | Korea nuclear supply-chain stocks reacted | stock-web OHLC rows | price validation only | Price action cannot create Stage2/Stage3 evidence alone. |
| 2024-10-30 | Czech anti-monopoly office preliminary measure / appeals | Reuters / legal-delay news | 4B/4C stress note | Used as non-price overlay context, not representative entry. |
| 2025-05-06 | Czech court temporary block of signing | AP / legal-delay news | narrative-only 4C watch | Outside this loop's representative entry window; not used as new quantitative trigger. |

Evidence separation:

```text
Stage2 = public preferred-bidder event + sector policy optionality + beneficiary role hypothesis
Stage3 = direct commercial bridge / revision / margin bridge, mostly absent at the 2024-07-18 entry
4B = local price blowoff plus later legal delay watch
4C = only if contract signing block, tender loss, cancellation, or thesis evidence break becomes hard evidence
```

## 10. Price Data Source Map

| symbol | company | profile_path | inspected shard rows | corporate-action window status |
|---:|---|---|---|---|
| 034020 | 두산에너빌리티 | atlas/symbol_profiles/034/034020.json | 2024-07-18 row: o 23850 / h 25000 / l 20900 / c 21000; 2025-02-18 peak h 30550 | clean_180D_window |
| 052690 | 한전기술 | atlas/symbol_profiles/052/052690.json | 2024-07-18 row: o 95000 / h 98100 / l 80700 / c 82000; 2025-04-09 low 49800 | clean_180D_window |
| 051600 | 한전KPS | atlas/symbol_profiles/051/051600.json | 2024-07-18 row: o 43500 / h 47450 / l 38550 / c 38900; 2025-01-24 high 48100 | clean_180D_window |
| 083650 | 비에이치아이 | atlas/symbol_profiles/083/083650.json | 2024-07-18 row: o 10210 / h 10530 / l 8760 / c 8810; 2025-02-14 high 24800 | clean_180D_window |
| 100840 | SNT에너지 | atlas/symbol_profiles/100/100840.json | 2024-07-18 row: o 14490 / h 15870 / l 11830 / c 12030; 2025-03-06 high 38400 | clean_180D_window |

## 11. Case-by-Case Trigger Grid

| case | Stage2 evidence | Stage3 evidence at trigger | 4B evidence | 4C evidence | verdict |
|---|---|---|---|---|---|
| 051600 | preferred bidder + O&M/service route | partial financial visibility, not Green | event-day local high, but no full 4B | none | preserve Stage2-Actionable, wait for bridge |
| 083650 | preferred bidder + equipment route | not confirmed at trigger | high beta, local blowoff | none | Stage2-Actionable only; later confirmation matters |
| 100840 | preferred bidder + energy equipment route | not confirmed at trigger | gap + momentum | none | Stage2-Actionable with high-MAE guard |
| 034020 | preferred bidder + large equipment route | insufficient margin bridge at trigger | event-day high, high MAE | none | not Green; high-MAE success |
| 052690 | preferred bidder + design pure-play | insufficient direct contract/revision bridge | event-day full peak | later legal delay watch | false positive if Green |

## 12. Trigger-Level OHLC Backtest Tables

| symbol | entry | price | high30/low30 | MFE30/MAE30 | high90/low90 | MFE90/MAE90 | high180/low180 | MFE180/MAE180 | peak | drawdown_after_peak |
|---:|---|---:|---|---|---|---|---|---|---|---:|
| 051600 | 2024-07-18 | 38,900 | 47,450/35,850 | 21.98 / -7.84 | 47,450/35,850 | 21.98 / -7.84 | 48,100/35,850 | 23.65 / -7.84 | 2025-01-24 48,100 | -21.0 |
| 083650 | 2024-07-18 | 8,810 | 10,530/7,100 | 19.52 / -19.41 | 10,530/7,000 | 19.52 / -20.54 | 24,800/7,000 | 181.5 / -20.54 | 2025-02-14 24,800 | -38.43 |
| 100840 | 2024-07-18 | 12,030 | 15,870/10,100 | 31.92 / -16.04 | 15,870/10,100 | 31.92 / -16.04 | 38,400/10,100 | 219.2 / -16.04 | 2025-03-06 38,400 | -26.04 |
| 034020 | 2024-07-18 | 21,000 | 25,000/15,150 | 19.05 / -27.86 | 25,000/15,150 | 19.05 / -27.86 | 30,550/15,150 | 45.48 / -27.86 | 2025-02-18 30,550 | -34.66 |
| 052690 | 2024-07-18 | 82,000 | 98,100/61,600 | 19.63 / -24.88 | 98,100/61,600 | 19.63 / -24.88 | 98,100/49,800 | 19.63 / -39.27 | 2024-07-18 98,100 | -49.24 |


Interpretation:

- 052690 is the central counterexample: event-day excitement gave MFE_30D +19.63%, but the same day was the full peak and the later 180D low was -39.09%.
- 034020 and 083650 show why C04 cannot be judged by early MAE alone. They were painful entries first, then later positive if the supply-chain bridge survived.
- 051600 is the cleaner positive because the service/O&M bridge kept MAE contained while MFE_180D stayed positive.
- 100840 shows a successful but high-beta route: the right response is not automatic Green, but a Stage2-Actionable row with a high-MAE guard and later bridge validation.

## 13. Current Calibrated Profile Stress Test

| symbol | current profile likely label | actual alignment | verdict |
|---:|---|---|---|
| 051600 | Stage2-Actionable | correct; moderate MFE and manageable MAE | current_profile_correct |
| 083650 | Stage2 or delayed Stage2-Actionable | too late if it waits for full confirmation; MFE_180D +181.50 | current_profile_too_late |
| 100840 | Stage2 or delayed Stage2-Actionable | too late if direct bridge ignored; MFE_180D +219.20 | current_profile_too_late |
| 034020 | could over-promote to Yellow on headline | local 4B too early, but not failed thesis | current_profile_4B_too_early |
| 052690 | could over-promote to Green on pure-play price strength | false positive; peak on entry day | current_profile_false_positive |

Answers to required stress questions:

```text
1. current calibrated profile likely catches the broad nuclear event, but may not sufficiently separate direct project role from policy headline.
2. Actual MFE/MAE alignment is mixed: three positives, two counterexamples/high-MAE guards.
3. Stage2 bonus is not too high if bounded by C04 direct-role guard.
4. Yellow threshold 75 is acceptable, but C04 needs a direct bridge to avoid 052690-like false positives.
5. Green 87/revision 55 remains appropriate; this loop strengthens the rule that C04 Green needs actual revision or contract visibility.
6. price-only blowoff guard is appropriate and strengthened.
7. full 4B non-price requirement is appropriate; local event-day peaks alone were too early for 034020/100840/BHI.
8. hard 4C should not fire on an appeal/watch item alone; it should fire only after hard contract-signing block, cancellation, or thesis evidence break.
```

## 14. Stage2 / Yellow / Green Comparison

C04 is a classic “permission vs conversion” problem. The preferred-bidder event grants permission to model future work, but it does not by itself convert to revenue. Stage2 can start at the public event. Yellow can start when direct company role becomes plausible and the price path does not immediately fail. Green should wait for direct project scope, order conversion, revision, or margin bridge.

```text
Stage2-Actionable works for: 051600, 083650, 100840, 034020
Stage2-Watch / blocked Green works for: 052690
Stage3-Yellow requires: direct project role + bridge evidence
Stage3-Green requires: confirmed revision or durable contract visibility
```

Green lateness is not the central residual here; premature Green is. Therefore `green_lateness_ratio = not_applicable` for representative rows.

## 15. 4B Local vs Full-window Timing Audit

| symbol | local peak reference | full-window peak | local/full split | verdict |
|---:|---|---|---:|---|
| 034020 | 2024-07-18 high 25000 | 2025-02-18 high 30550 | 0.58 | price_only_local_4B_too_early |
| 052690 | 2024-07-18 high 98100 | 2024-07-18 high 98100 | 1.00 | local peak was full peak; still needs non-price 4B evidence for full exit |
| 100840 | 2024-07-18 high 15870 | 2025-03-06 high 38400 | 0.15 | price_only_local_4B_too_early |
| 083650 | 2024-07-18 high 10530 | 2025-02-14 high 24800 | 0.11 | price_only_local_4B_too_early |
| 051600 | 2024-07-18 high 47450 | 2025-01-24 high 48100 | 0.93 | acceptable local peak proximity, but not a full 4B without non-price evidence |

The loop strengthens the existing 4B non-price requirement. Local heat can be a yellow caution tag, not a full 4B. In C04, the actual 4B/4C overlay should wait for legal delay, failed signing, contract cancellation, or explicit scope loss.

## 16. 4C Protection Audit

No representative hard 4C row is used for weight calibration in this MD. A later Czech contract-signing delay or court block is relevant as a watch item, but this loop does not use it as a new quantitative entry because the selected representative rows are the 2024-07-18 post-preferred-bidder Stage2 entries.

```text
four_c_protection_label = thesis_break_watch_only
hard_4c_success = not_tested_quantitatively
hard_4c_late = not_tested_quantitatively
```

## 17. Sector-Specific Rule Candidate

```text
rule_scope = sector_specific
large_sector_id = L1_INDUSTRIALS_INFRA_DEFENSE_GRID
rule_candidate = C04 nuclear project headline must be split into direct-role buckets
```

Proposed sector shadow rule:

```text
For L1 nuclear policy/project events, public preferred-bidder selection may create Stage2-Actionable only. Yellow/Green promotion requires at least one direct-role bridge: equipment scope, O&M/service link, design/engineering fee visibility, order conversion, or financial revision. If the event creates a large gap but direct bridge is weak, cap at Stage2-Watch or Stage2-Actionable and attach high-MAE guard.
```

## 18. Canonical-Archetype Rule Candidate

```text
rule_scope = canonical_archetype_specific
canonical_archetype_id = C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY
```

Canonical shadow axes:

```text
C04_direct_project_role_bridge_required_for_green = +1
C04_policy_headline_gap_requires_high_MAE_guard = +1
C04_legal_delay_watch_to_4C_route = +1
```

The scoring lesson is not “buy all nuclear beneficiaries on a tender headline.” It is more surgical: identify whether the company is a bridge pier, a decorative railing, or just a flag waving above the bridge. The price path punishes the flag-only cases.

## 19. Before / After Backtest Comparison

| profile | eligible cases | avg MFE90 | avg MAE90 | avg MFE180 | avg MAE180 | false positive count | missed structural count | verdict |
|---|---:|---:|---:|---:|---:|---:|---:|---|
| P0 e2r_2_1_stock_web_calibrated_proxy | 5 | 22.33 | -18.34 | 97.77 | -22.30 | 1 | 2 | useful but under-splits direct role |
| P0b e2r_2_0_baseline_reference | 5 | 22.33 | -18.34 | 97.77 | -22.30 | 2 | 2 | more vulnerable to headline/RS over-promotion |
| P1 sector_specific_candidate_profile | 5 | 22.33 | -18.34 | 97.77 | -22.30 | 1 | 1 | better by adding nuclear direct-role bridge |
| P2 canonical_archetype_candidate_profile | 5 | 22.33 | -18.34 | 97.77 | -22.30 | 0-1 | 1 | best explanation; keeps positives but blocks 052690 Green |
| P3 counterexample_guard_profile | 5 | 20.63 | -14.98 | 81.74 | -18.10 | 0 | 2 | safer but may miss BHI/SNT high-beta success |

Aggregate arithmetic uses representative triggers only and excludes local 4B overlay rows from aggregate counts.

## 20. Score-Return Alignment Matrix

| symbol | weighted before | label before | weighted after | label after | alignment |
|---:|---:|---|---:|---|---|
| 051600 | 78 | Stage2-Actionable | 81 | Stage2-Actionable | correct positive bridge |
| 083650 | 72 | Stage2 | 80 | Stage2-Actionable | missed structural if bridge ignored |
| 100840 | 74 | Stage2 | 82 | Stage2-Actionable | missed structural if bridge ignored |
| 034020 | 84 | Stage3-Yellow | 78 | Stage2-Actionable | high-MAE success, not clean Green |
| 052690 | 88 | Stage3-Green | 66 | Stage2-Watch | false positive blocked |

## 21. Coverage Matrix

| large_sector_id | canonical_archetype_id | fine_archetype_id | positive_case_count | counterexample_count | 4B_case_count | 4C_case_count | new_independent_case_count | reused_case_count | calibration_usable_trigger_count | representative_trigger_count | current_profile_error_count | sector_rule_candidate | canonical_rule_candidate | coverage_gap_after_this_loop |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|---|---|
| L1_INDUSTRIALS_INFRA_DEFENSE_GRID | C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY | CZECH_NUCLEAR_PREFERRED_BIDDER_DIRECT_BRIDGE_VS_POLICY_SPIKE | 3 | 2 | 3 | 1 narrative-only | 5 | 0 | 8 | 5 | 3 | true | true | C04 no longer empty; still needs non-Czech holdout and actual signed-contract stage rows |


## 22. Residual Contribution Summary

```text
new_independent_case_count: 5
reused_case_count: 0
reused_case_ids: []
new_symbol_count: 5
new_canonical_archetype_count: 1
new_fine_archetype_count: 1
new_trigger_family_count: 1
tested_existing_calibrated_axes: stage2_actionable_evidence_bonus, price_only_blowoff_blocks_positive_stage, full_4b_requires_non_price_evidence, hard_4c_thesis_break_routes_to_4c
residual_error_types_found: policy_headline_gap_false_positive, high_MAE_positive, local_4B_too_early, legal_delay_watch_not_hard_4C
new_axis_proposed: C04_direct_project_role_bridge_required_for_green; C04_policy_headline_gap_requires_high_MAE_guard; C04_legal_delay_watch_to_4C_route
existing_axis_strengthened: price_only_blowoff_blocks_positive_stage; full_4b_requires_non_price_evidence; hard_4c_thesis_break_routes_to_4c
existing_axis_weakened: none
existing_axis_kept: stage2_actionable_evidence_bonus; stage3_yellow_total_min; stage3_green_total_min; stage3_green_revision_min; stage3_cross_evidence_green_buffer
sector_specific_rule_candidate: true
canonical_archetype_rule_candidate: true
no_new_signal_reason: null
loop_contribution_label: canonical_archetype_rule_candidate
do_not_propose_new_weight_delta: false
```

## 23. Validation Scope / Non-Validation Scope

Validated:

```text
- stock-web manifest max_date and basis
- symbol profile availability and corporate-action caveats
- actual 2024-07-18 stock-web tradable rows for entry price
- 30D/90D/180D MFE/MAE using inspected OHLC extrema
- C04 direct-role vs policy-headline residual logic
```

Not validated:

```text
- current/live candidates
- investment recommendation
- production scoring code
- stock_agent src/e2r implementation
- brokerage or auto-trading logic
- 2Y windows, unavailable under manifest max_date
```

## 24. Shadow Weight Calibration

```csv
row_type,axis,scope,large_sector_id,canonical_archetype_id,baseline_value,tested_value,delta,reason,backtest_effect,trigger_ids,calibration_usable_count,new_independent_case_count,counterexample_count,confidence,proposal_type,notes
shadow_weight,C04_direct_project_role_bridge_required_for_green,canonical_archetype_specific,L1_INDUSTRIALS_INFRA_DEFENSE_GRID,C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY,0,1,+1,Require direct beneficiary role before Green promotion,Reduced false positive on 052690 while preserving 051600/083650/100840 positives,R1L12_C04_052690_CZECH_DESIGN_PURE_PLAY_SPIKE_STAGE2_ACTIONABLE|R1L12_C04_051600_CZECH_MAINTENANCE_BRIDGE_STAGE2_ACTIONABLE|R1L12_C04_083650_CZECH_BOILER_EQUIPMENT_HIGH_BETA_STAGE2_ACTIONABLE,5,5,2,medium,canonical_shadow_only,not production; post-calibrated residual
shadow_weight,C04_policy_headline_gap_requires_high_MAE_guard,canonical_archetype_specific,L1_INDUSTRIALS_INFRA_DEFENSE_GRID,C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY,0,1,+1,Policy headline plus gap-up frequently creates deep MAE,Flags 034020/052690/SNT event-day gaps as Stage2 watch or high-MAE success rather than clean Green,R1L12_C04_034020_CZECH_NSSS_HIGH_MAE_STAGE2_ACTIONABLE|R1L12_C04_052690_CZECH_DESIGN_PURE_PLAY_SPIKE_STAGE2_ACTIONABLE|R1L12_C04_100840_CZECH_HEAT_EXCHANGER_SUPPLY_CHAIN_STAGE2_ACTIONABLE,5,5,2,medium,canonical_shadow_only,not production; post-calibrated residual
```

## 25. Machine-Readable Rows

```jsonl
{"row_type": "price_source_validation", "source": "Songdaiki/stock-web", "source_url": "https://github.com/Songdaiki/stock-web", "manifest_path": "atlas/manifest.json", "schema_path": "atlas/schema.json", "universe_path": "atlas/universe/all_symbols.csv", "manifest_max_date": "2026-02-20", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "raw_shard_root": "atlas/ohlcv_raw_by_symbol_year", "validation_status": "usable_for_historical_calibration"}
{"row_type": "case", "case_id": "R1L12_C04_051600_CZECH_MAINTENANCE_BRIDGE", "symbol": "051600", "company_name": "한전KPS", "round": "R1", "loop": "12", "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "canonical_archetype_id": "C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY", "fine_archetype_id": "CZECH_NUCLEAR_PREFERRED_BIDDER_DIRECT_BRIDGE_VS_POLICY_SPIKE", "case_type": "structural_success", "positive_or_counterexample": "positive", "best_trigger": "R1L12_C04_051600_CZECH_MAINTENANCE_BRIDGE_STAGE2_ACTIONABLE", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "positive_bridge_preserved", "current_profile_verdict": "current_profile_correct", "price_source": "Songdaiki/stock-web", "notes": "Czech preferred-bidder event plus recurring O&M/commissioning-adjacent exposure; maintenance bridge rather than one-off EPC headline."}
{"row_type": "case", "case_id": "R1L12_C04_083650_CZECH_BOILER_EQUIPMENT_HIGH_BETA", "symbol": "083650", "company_name": "비에이치아이", "round": "R1", "loop": "12", "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "canonical_archetype_id": "C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY", "fine_archetype_id": "CZECH_NUCLEAR_PREFERRED_BIDDER_DIRECT_BRIDGE_VS_POLICY_SPIKE", "case_type": "high_mae_success", "positive_or_counterexample": "positive", "best_trigger": "R1L12_C04_083650_CZECH_BOILER_EQUIPMENT_HIGH_BETA_STAGE2_ACTIONABLE", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "delayed_positive_after_high_beta_drawdown", "current_profile_verdict": "current_profile_too_late", "price_source": "Songdaiki/stock-web", "notes": "Nuclear boiler/auxiliary-equipment route; early event was noisy, later orderability and nuclear-supply-chain beta mattered."}
{"row_type": "case", "case_id": "R1L12_C04_100840_CZECH_HEAT_EXCHANGER_SUPPLY_CHAIN", "symbol": "100840", "company_name": "SNT에너지", "round": "R1", "loop": "12", "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "canonical_archetype_id": "C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY", "fine_archetype_id": "CZECH_NUCLEAR_PREFERRED_BIDDER_DIRECT_BRIDGE_VS_POLICY_SPIKE", "case_type": "structural_success", "positive_or_counterexample": "positive", "best_trigger": "R1L12_C04_100840_CZECH_HEAT_EXCHANGER_SUPPLY_CHAIN_STAGE2_ACTIONABLE", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "supply_chain_positive_after_confirmation_lag", "current_profile_verdict": "current_profile_too_late", "price_source": "Songdaiki/stock-web", "notes": "Heat-exchanger / energy-equipment route; event-day spike alone was insufficient but direct supply-chain bridge later worked."}
{"row_type": "case", "case_id": "R1L12_C04_034020_CZECH_NSSS_HIGH_MAE", "symbol": "034020", "company_name": "두산에너빌리티", "round": "R1", "loop": "12", "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "canonical_archetype_id": "C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY", "fine_archetype_id": "CZECH_NUCLEAR_PREFERRED_BIDDER_DIRECT_BRIDGE_VS_POLICY_SPIKE", "case_type": "high_mae_success", "positive_or_counterexample": "counterexample", "best_trigger": "R1L12_C04_034020_CZECH_NSSS_HIGH_MAE_STAGE2_ACTIONABLE", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "event_spike_then_deep_MAE_then_recovery", "current_profile_verdict": "current_profile_4B_too_early", "price_source": "Songdaiki/stock-web", "notes": "Large nuclear-supply-chain beneficiary, but event-day gap was not clean entry; high MAE argues for direct-contract and drawdown-aware staging."}
{"row_type": "case", "case_id": "R1L12_C04_052690_CZECH_DESIGN_PURE_PLAY_SPIKE", "symbol": "052690", "company_name": "한전기술", "round": "R1", "loop": "12", "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "canonical_archetype_id": "C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY", "fine_archetype_id": "CZECH_NUCLEAR_PREFERRED_BIDDER_DIRECT_BRIDGE_VS_POLICY_SPIKE", "case_type": "false_positive_green", "positive_or_counterexample": "counterexample", "best_trigger": "R1L12_C04_052690_CZECH_DESIGN_PURE_PLAY_SPIKE_STAGE2_ACTIONABLE", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "opening_gap_peak_failed_to_convert", "current_profile_verdict": "current_profile_false_positive", "price_source": "Songdaiki/stock-web", "notes": "Design pure-play and policy headline produced local blowoff; absence of immediate contract/revision bridge left a failed-rerating path."}
{"row_type": "trigger", "trigger_id": "R1L12_C04_051600_CZECH_MAINTENANCE_BRIDGE_STAGE2_ACTIONABLE", "case_id": "R1L12_C04_051600_CZECH_MAINTENANCE_BRIDGE", "symbol": "051600", "company_name": "한전KPS", "round": "R1", "loop": "12", "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "canonical_archetype_id": "C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY", "fine_archetype_id": "CZECH_NUCLEAR_PREFERRED_BIDDER_DIRECT_BRIDGE_VS_POLICY_SPIKE", "sector": "industrials_infra_nuclear", "primary_archetype": "nuclear_policy_project_legal_delay", "loop_objective": "coverage_gap_fill|counterexample_mining|sector_specific_rule_discovery", "trigger_type": "Stage2-Actionable", "trigger_date": "2024-07-17", "evidence_available_at_that_date": "Czech preferred-bidder event plus recurring O&M/commissioning-adjacent exposure; maintenance bridge rather than one-off EPC headline.", "evidence_source": "Reuters 2024-07-17; public Czech/KHNP preferred-bidder announcement; stock-web OHLC row inspected", "stage2_evidence_fields": ["public_event_or_disclosure", "policy_or_regulatory_optionality", "relative_strength", "backlog_or_delivery_visibility"], "stage3_evidence_fields": ["financial_visibility"], "stage4b_evidence_fields": ["price_only_local_peak"], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/051/051600/2024.csv", "profile_path": "atlas/symbol_profiles/051/051600.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "entry_date": "2024-07-18", "entry_price": 38900, "MFE_30D_pct": 21.98, "MFE_90D_pct": 21.98, "MFE_180D_pct": 23.65, "MFE_1Y_pct": null, "MFE_2Y_pct": null, "MAE_30D_pct": -7.84, "MAE_90D_pct": -7.84, "MAE_180D_pct": -7.84, "MAE_1Y_pct": null, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2025-01-24", "peak_price": 48100, "drawdown_after_peak_pct": -21.0, "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": 0.93, "four_b_full_window_peak_proximity": 0.93, "four_b_timing_verdict": "price_only_local_4B_too_early", "four_b_evidence_type": ["price_only"], "four_c_protection_label": "thesis_break_watch_only", "trigger_outcome_label": "positive_bridge_preserved", "current_profile_verdict": "current_profile_correct", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window", "same_entry_group_id": "R1L12_C04_051600_CZECH_MAINTENANCE_BRIDGE_2024-07-18", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false}
{"row_type": "trigger", "trigger_id": "R1L12_C04_083650_CZECH_BOILER_EQUIPMENT_HIGH_BETA_STAGE2_ACTIONABLE", "case_id": "R1L12_C04_083650_CZECH_BOILER_EQUIPMENT_HIGH_BETA", "symbol": "083650", "company_name": "비에이치아이", "round": "R1", "loop": "12", "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "canonical_archetype_id": "C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY", "fine_archetype_id": "CZECH_NUCLEAR_PREFERRED_BIDDER_DIRECT_BRIDGE_VS_POLICY_SPIKE", "sector": "industrials_infra_nuclear", "primary_archetype": "nuclear_policy_project_legal_delay", "loop_objective": "coverage_gap_fill|counterexample_mining|sector_specific_rule_discovery", "trigger_type": "Stage2-Actionable", "trigger_date": "2024-07-17", "evidence_available_at_that_date": "Nuclear boiler/auxiliary-equipment route; early event was noisy, later orderability and nuclear-supply-chain beta mattered.", "evidence_source": "Reuters 2024-07-17; public Czech/KHNP preferred-bidder announcement; stock-web OHLC row inspected", "stage2_evidence_fields": ["public_event_or_disclosure", "policy_or_regulatory_optionality", "relative_strength", "backlog_or_delivery_visibility"], "stage3_evidence_fields": ["financial_visibility"], "stage4b_evidence_fields": ["price_only_local_peak"], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/083/083650/2024.csv", "profile_path": "atlas/symbol_profiles/083/083650.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "entry_date": "2024-07-18", "entry_price": 8810, "MFE_30D_pct": 19.52, "MFE_90D_pct": 19.52, "MFE_180D_pct": 181.5, "MFE_1Y_pct": null, "MFE_2Y_pct": null, "MAE_30D_pct": -19.41, "MAE_90D_pct": -20.54, "MAE_180D_pct": -20.54, "MAE_1Y_pct": null, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2025-02-14", "peak_price": 24800, "drawdown_after_peak_pct": -38.43, "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": 0.11, "four_b_full_window_peak_proximity": 0.11, "four_b_timing_verdict": "price_only_local_4B_too_early", "four_b_evidence_type": ["price_only"], "four_c_protection_label": "thesis_break_watch_only", "trigger_outcome_label": "delayed_positive_after_high_beta_drawdown", "current_profile_verdict": "current_profile_too_late", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window", "same_entry_group_id": "R1L12_C04_083650_CZECH_BOILER_EQUIPMENT_HIGH_BETA_2024-07-18", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false}
{"row_type": "trigger", "trigger_id": "R1L12_C04_100840_CZECH_HEAT_EXCHANGER_SUPPLY_CHAIN_STAGE2_ACTIONABLE", "case_id": "R1L12_C04_100840_CZECH_HEAT_EXCHANGER_SUPPLY_CHAIN", "symbol": "100840", "company_name": "SNT에너지", "round": "R1", "loop": "12", "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "canonical_archetype_id": "C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY", "fine_archetype_id": "CZECH_NUCLEAR_PREFERRED_BIDDER_DIRECT_BRIDGE_VS_POLICY_SPIKE", "sector": "industrials_infra_nuclear", "primary_archetype": "nuclear_policy_project_legal_delay", "loop_objective": "coverage_gap_fill|counterexample_mining|sector_specific_rule_discovery", "trigger_type": "Stage2-Actionable", "trigger_date": "2024-07-17", "evidence_available_at_that_date": "Heat-exchanger / energy-equipment route; event-day spike alone was insufficient but direct supply-chain bridge later worked.", "evidence_source": "Reuters 2024-07-17; public Czech/KHNP preferred-bidder announcement; stock-web OHLC row inspected", "stage2_evidence_fields": ["public_event_or_disclosure", "policy_or_regulatory_optionality", "relative_strength", "backlog_or_delivery_visibility"], "stage3_evidence_fields": ["financial_visibility"], "stage4b_evidence_fields": ["price_only_local_peak"], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/100/100840/2024.csv", "profile_path": "atlas/symbol_profiles/100/100840.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "entry_date": "2024-07-18", "entry_price": 12030, "MFE_30D_pct": 31.92, "MFE_90D_pct": 31.92, "MFE_180D_pct": 219.2, "MFE_1Y_pct": null, "MFE_2Y_pct": null, "MAE_30D_pct": -16.04, "MAE_90D_pct": -16.04, "MAE_180D_pct": -16.04, "MAE_1Y_pct": null, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2025-03-06", "peak_price": 38400, "drawdown_after_peak_pct": -26.04, "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": 0.15, "four_b_full_window_peak_proximity": 0.15, "four_b_timing_verdict": "price_only_local_4B_too_early", "four_b_evidence_type": ["price_only"], "four_c_protection_label": "thesis_break_watch_only", "trigger_outcome_label": "supply_chain_positive_after_confirmation_lag", "current_profile_verdict": "current_profile_too_late", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window", "same_entry_group_id": "R1L12_C04_100840_CZECH_HEAT_EXCHANGER_SUPPLY_CHAIN_2024-07-18", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false}
{"row_type": "trigger", "trigger_id": "R1L12_C04_100840_CZECH_HEAT_EXCHANGER_SUPPLY_CHAIN_LOCAL_4B_OVERLAY", "case_id": "R1L12_C04_100840_CZECH_HEAT_EXCHANGER_SUPPLY_CHAIN", "symbol": "100840", "company_name": "SNT에너지", "round": "R1", "loop": "12", "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "canonical_archetype_id": "C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY", "fine_archetype_id": "CZECH_NUCLEAR_PREFERRED_BIDDER_DIRECT_BRIDGE_VS_POLICY_SPIKE", "sector": "industrials_infra_nuclear", "primary_archetype": "nuclear_policy_project_legal_delay", "loop_objective": "coverage_gap_fill|counterexample_mining|sector_specific_rule_discovery", "trigger_type": "4B-overlay", "trigger_date": "2024-07-17", "evidence_available_at_that_date": "Heat-exchanger / energy-equipment route; event-day spike alone was insufficient but direct supply-chain bridge later worked.", "evidence_source": "Reuters 2024-07-17; public Czech/KHNP preferred-bidder announcement; stock-web OHLC row inspected", "stage2_evidence_fields": [], "stage3_evidence_fields": [], "stage4b_evidence_fields": ["price_only_local_peak", "valuation_blowoff"], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/100/100840/2024.csv", "profile_path": "atlas/symbol_profiles/100/100840.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "entry_date": "2024-07-18", "entry_price": 12030, "MFE_30D_pct": 31.92, "MFE_90D_pct": 31.92, "MFE_180D_pct": 219.2, "MFE_1Y_pct": null, "MFE_2Y_pct": null, "MAE_30D_pct": -16.04, "MAE_90D_pct": -16.04, "MAE_180D_pct": -16.04, "MAE_1Y_pct": null, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2025-03-06", "peak_price": 38400, "drawdown_after_peak_pct": -26.04, "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": 0.15, "four_b_full_window_peak_proximity": 0.15, "four_b_timing_verdict": "price_only_local_4B_too_early", "four_b_evidence_type": ["price_only"], "four_c_protection_label": "thesis_break_watch_only", "trigger_outcome_label": "overlay_only_not_full_exit", "current_profile_verdict": "current_profile_too_late", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window", "same_entry_group_id": "R1L12_C04_100840_CZECH_HEAT_EXCHANGER_SUPPLY_CHAIN_2024-07-18", "dedupe_for_aggregate": false, "aggregate_group_role": "4B_overlay_only", "is_new_independent_case": false, "reuse_reason": null, "independent_evidence_weight": 0.0, "do_not_count_as_new_case": true}
{"row_type": "trigger", "trigger_id": "R1L12_C04_034020_CZECH_NSSS_HIGH_MAE_STAGE2_ACTIONABLE", "case_id": "R1L12_C04_034020_CZECH_NSSS_HIGH_MAE", "symbol": "034020", "company_name": "두산에너빌리티", "round": "R1", "loop": "12", "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "canonical_archetype_id": "C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY", "fine_archetype_id": "CZECH_NUCLEAR_PREFERRED_BIDDER_DIRECT_BRIDGE_VS_POLICY_SPIKE", "sector": "industrials_infra_nuclear", "primary_archetype": "nuclear_policy_project_legal_delay", "loop_objective": "coverage_gap_fill|counterexample_mining|sector_specific_rule_discovery", "trigger_type": "Stage2-Actionable", "trigger_date": "2024-07-17", "evidence_available_at_that_date": "Large nuclear-supply-chain beneficiary, but event-day gap was not clean entry; high MAE argues for direct-contract and drawdown-aware staging.", "evidence_source": "Reuters 2024-07-17; public Czech/KHNP preferred-bidder announcement; stock-web OHLC row inspected", "stage2_evidence_fields": ["public_event_or_disclosure", "policy_or_regulatory_optionality", "relative_strength", "backlog_or_delivery_visibility"], "stage3_evidence_fields": ["unknown_or_not_supported"], "stage4b_evidence_fields": ["price_only_local_peak"], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/034/034020/2024.csv", "profile_path": "atlas/symbol_profiles/034/034020.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "entry_date": "2024-07-18", "entry_price": 21000, "MFE_30D_pct": 19.05, "MFE_90D_pct": 19.05, "MFE_180D_pct": 45.48, "MFE_1Y_pct": null, "MFE_2Y_pct": null, "MAE_30D_pct": -27.86, "MAE_90D_pct": -27.86, "MAE_180D_pct": -27.86, "MAE_1Y_pct": null, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2025-02-18", "peak_price": 30550, "drawdown_after_peak_pct": -34.66, "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": 0.42, "four_b_full_window_peak_proximity": 0.42, "four_b_timing_verdict": "price_only_local_4B_too_early", "four_b_evidence_type": ["price_only"], "four_c_protection_label": "thesis_break_watch_only", "trigger_outcome_label": "event_spike_then_deep_MAE_then_recovery", "current_profile_verdict": "current_profile_4B_too_early", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window", "same_entry_group_id": "R1L12_C04_034020_CZECH_NSSS_HIGH_MAE_2024-07-18", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false}
{"row_type": "trigger", "trigger_id": "R1L12_C04_034020_CZECH_NSSS_HIGH_MAE_LOCAL_4B_OVERLAY", "case_id": "R1L12_C04_034020_CZECH_NSSS_HIGH_MAE", "symbol": "034020", "company_name": "두산에너빌리티", "round": "R1", "loop": "12", "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "canonical_archetype_id": "C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY", "fine_archetype_id": "CZECH_NUCLEAR_PREFERRED_BIDDER_DIRECT_BRIDGE_VS_POLICY_SPIKE", "sector": "industrials_infra_nuclear", "primary_archetype": "nuclear_policy_project_legal_delay", "loop_objective": "coverage_gap_fill|counterexample_mining|sector_specific_rule_discovery", "trigger_type": "4B-overlay", "trigger_date": "2024-07-17", "evidence_available_at_that_date": "Large nuclear-supply-chain beneficiary, but event-day gap was not clean entry; high MAE argues for direct-contract and drawdown-aware staging.", "evidence_source": "Reuters 2024-07-17; public Czech/KHNP preferred-bidder announcement; stock-web OHLC row inspected", "stage2_evidence_fields": [], "stage3_evidence_fields": [], "stage4b_evidence_fields": ["price_only_local_peak", "valuation_blowoff"], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/034/034020/2024.csv", "profile_path": "atlas/symbol_profiles/034/034020.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "entry_date": "2024-07-18", "entry_price": 21000, "MFE_30D_pct": 19.05, "MFE_90D_pct": 19.05, "MFE_180D_pct": 45.48, "MFE_1Y_pct": null, "MFE_2Y_pct": null, "MAE_30D_pct": -27.86, "MAE_90D_pct": -27.86, "MAE_180D_pct": -27.86, "MAE_1Y_pct": null, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2025-02-18", "peak_price": 30550, "drawdown_after_peak_pct": -34.66, "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": 0.42, "four_b_full_window_peak_proximity": 0.42, "four_b_timing_verdict": "price_only_local_4B_too_early", "four_b_evidence_type": ["price_only"], "four_c_protection_label": "thesis_break_watch_only", "trigger_outcome_label": "overlay_only_not_full_exit", "current_profile_verdict": "current_profile_4B_too_early", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window", "same_entry_group_id": "R1L12_C04_034020_CZECH_NSSS_HIGH_MAE_2024-07-18", "dedupe_for_aggregate": false, "aggregate_group_role": "4B_overlay_only", "is_new_independent_case": false, "reuse_reason": null, "independent_evidence_weight": 0.0, "do_not_count_as_new_case": true}
{"row_type": "trigger", "trigger_id": "R1L12_C04_052690_CZECH_DESIGN_PURE_PLAY_SPIKE_STAGE2_ACTIONABLE", "case_id": "R1L12_C04_052690_CZECH_DESIGN_PURE_PLAY_SPIKE", "symbol": "052690", "company_name": "한전기술", "round": "R1", "loop": "12", "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "canonical_archetype_id": "C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY", "fine_archetype_id": "CZECH_NUCLEAR_PREFERRED_BIDDER_DIRECT_BRIDGE_VS_POLICY_SPIKE", "sector": "industrials_infra_nuclear", "primary_archetype": "nuclear_policy_project_legal_delay", "loop_objective": "coverage_gap_fill|counterexample_mining|sector_specific_rule_discovery", "trigger_type": "Stage2-Actionable", "trigger_date": "2024-07-17", "evidence_available_at_that_date": "Design pure-play and policy headline produced local blowoff; absence of immediate contract/revision bridge left a failed-rerating path.", "evidence_source": "Reuters 2024-07-17; public Czech/KHNP preferred-bidder announcement; stock-web OHLC row inspected", "stage2_evidence_fields": ["public_event_or_disclosure", "policy_or_regulatory_optionality", "relative_strength", "backlog_or_delivery_visibility"], "stage3_evidence_fields": ["unknown_or_not_supported"], "stage4b_evidence_fields": ["price_only_local_peak"], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/052/052690/2024.csv", "profile_path": "atlas/symbol_profiles/052/052690.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "entry_date": "2024-07-18", "entry_price": 82000, "MFE_30D_pct": 19.63, "MFE_90D_pct": 19.63, "MFE_180D_pct": 19.63, "MFE_1Y_pct": null, "MFE_2Y_pct": null, "MAE_30D_pct": -24.88, "MAE_90D_pct": -24.88, "MAE_180D_pct": -39.27, "MAE_1Y_pct": null, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2024-07-18", "peak_price": 98100, "drawdown_after_peak_pct": -49.24, "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": 1.0, "four_b_full_window_peak_proximity": 1.0, "four_b_timing_verdict": "price_only_local_peak_not_full_4B", "four_b_evidence_type": ["price_only"], "four_c_protection_label": "thesis_break_watch_only", "trigger_outcome_label": "opening_gap_peak_failed_to_convert", "current_profile_verdict": "current_profile_false_positive", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window", "same_entry_group_id": "R1L12_C04_052690_CZECH_DESIGN_PURE_PLAY_SPIKE_2024-07-18", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false}
{"row_type": "trigger", "trigger_id": "R1L12_C04_052690_CZECH_DESIGN_PURE_PLAY_SPIKE_LOCAL_4B_OVERLAY", "case_id": "R1L12_C04_052690_CZECH_DESIGN_PURE_PLAY_SPIKE", "symbol": "052690", "company_name": "한전기술", "round": "R1", "loop": "12", "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "canonical_archetype_id": "C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY", "fine_archetype_id": "CZECH_NUCLEAR_PREFERRED_BIDDER_DIRECT_BRIDGE_VS_POLICY_SPIKE", "sector": "industrials_infra_nuclear", "primary_archetype": "nuclear_policy_project_legal_delay", "loop_objective": "coverage_gap_fill|counterexample_mining|sector_specific_rule_discovery", "trigger_type": "4B-overlay", "trigger_date": "2024-07-17", "evidence_available_at_that_date": "Design pure-play and policy headline produced local blowoff; absence of immediate contract/revision bridge left a failed-rerating path.", "evidence_source": "Reuters 2024-07-17; public Czech/KHNP preferred-bidder announcement; stock-web OHLC row inspected", "stage2_evidence_fields": [], "stage3_evidence_fields": [], "stage4b_evidence_fields": ["price_only_local_peak", "valuation_blowoff"], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/052/052690/2024.csv", "profile_path": "atlas/symbol_profiles/052/052690.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "entry_date": "2024-07-18", "entry_price": 82000, "MFE_30D_pct": 19.63, "MFE_90D_pct": 19.63, "MFE_180D_pct": 19.63, "MFE_1Y_pct": null, "MFE_2Y_pct": null, "MAE_30D_pct": -24.88, "MAE_90D_pct": -24.88, "MAE_180D_pct": -39.27, "MAE_1Y_pct": null, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2024-07-18", "peak_price": 98100, "drawdown_after_peak_pct": -49.24, "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": 1.0, "four_b_full_window_peak_proximity": 1.0, "four_b_timing_verdict": "price_only_local_4B_too_early", "four_b_evidence_type": ["price_only"], "four_c_protection_label": "thesis_break_watch_only", "trigger_outcome_label": "overlay_only_not_full_exit", "current_profile_verdict": "current_profile_false_positive", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window", "same_entry_group_id": "R1L12_C04_052690_CZECH_DESIGN_PURE_PLAY_SPIKE_2024-07-18", "dedupe_for_aggregate": false, "aggregate_group_role": "4B_overlay_only", "is_new_independent_case": false, "reuse_reason": null, "independent_evidence_weight": 0.0, "do_not_count_as_new_case": true}
{"row_type": "score_simulation", "profile_id": "C04_direct_project_role_shadow_profile", "case_id": "R1L12_C04_051600_CZECH_MAINTENANCE_BRIDGE", "trigger_id": "R1L12_C04_051600_CZECH_MAINTENANCE_BRIDGE_STAGE2_ACTIONABLE", "symbol": "051600", "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "canonical_archetype_id": "C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY", "raw_component_scores_before": {"contract_score": 45, "backlog_visibility_score": 55, "margin_bridge_score": 50, "revision_score": 30, "relative_strength_score": 55, "customer_quality_score": 65, "policy_or_regulatory_score": 80, "valuation_repricing_score": 50, "execution_risk_score": 35, "legal_or_contract_risk_score": 20, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_before": 78, "stage_label_before": "Stage2-Actionable", "raw_component_scores_after": {"contract_score": 52, "backlog_visibility_score": 60, "margin_bridge_score": 55, "revision_score": 30, "relative_strength_score": 55, "customer_quality_score": 65, "policy_or_regulatory_score": 80, "valuation_repricing_score": 50, "execution_risk_score": 35, "legal_or_contract_risk_score": 20, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_after": 81, "stage_label_after": "Stage2-Actionable", "changed_components": ["direct_O&M_bridge +3"], "component_delta_explanation": "C04 shadow profile separates policy headline from direct project role, contract bridge, and legal-delay risk.", "MFE_90D_pct": 21.98, "MAE_90D_pct": -7.84, "score_return_alignment_label": "positive_bridge_preserved", "current_profile_verdict": "current_profile_correct"}
{"row_type": "score_simulation", "profile_id": "C04_direct_project_role_shadow_profile", "case_id": "R1L12_C04_083650_CZECH_BOILER_EQUIPMENT_HIGH_BETA", "trigger_id": "R1L12_C04_083650_CZECH_BOILER_EQUIPMENT_HIGH_BETA_STAGE2_ACTIONABLE", "symbol": "083650", "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "canonical_archetype_id": "C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY", "raw_component_scores_before": {"contract_score": 40, "backlog_visibility_score": 45, "margin_bridge_score": 35, "revision_score": 25, "relative_strength_score": 45, "customer_quality_score": 50, "policy_or_regulatory_score": 80, "valuation_repricing_score": 60, "execution_risk_score": 55, "legal_or_contract_risk_score": 20, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_before": 72, "stage_label_before": "Stage2", "raw_component_scores_after": {"contract_score": 48, "backlog_visibility_score": 55, "margin_bridge_score": 35, "revision_score": 25, "relative_strength_score": 45, "customer_quality_score": 50, "policy_or_regulatory_score": 80, "valuation_repricing_score": 60, "execution_risk_score": 60, "legal_or_contract_risk_score": 20, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_after": 80, "stage_label_after": "Stage2-Actionable", "changed_components": ["equipment_bridge +6", "high_beta_MAE_guard +2"], "component_delta_explanation": "C04 shadow profile separates policy headline from direct project role, contract bridge, and legal-delay risk.", "MFE_90D_pct": 19.52, "MAE_90D_pct": -20.54, "score_return_alignment_label": "delayed_positive_after_high_beta_drawdown", "current_profile_verdict": "current_profile_too_late"}
{"row_type": "score_simulation", "profile_id": "C04_direct_project_role_shadow_profile", "case_id": "R1L12_C04_100840_CZECH_HEAT_EXCHANGER_SUPPLY_CHAIN", "trigger_id": "R1L12_C04_100840_CZECH_HEAT_EXCHANGER_SUPPLY_CHAIN_STAGE2_ACTIONABLE", "symbol": "100840", "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "canonical_archetype_id": "C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY", "raw_component_scores_before": {"contract_score": 42, "backlog_visibility_score": 48, "margin_bridge_score": 38, "revision_score": 25, "relative_strength_score": 48, "customer_quality_score": 52, "policy_or_regulatory_score": 80, "valuation_repricing_score": 62, "execution_risk_score": 50, "legal_or_contract_risk_score": 20, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_before": 74, "stage_label_before": "Stage2", "raw_component_scores_after": {"contract_score": 50, "backlog_visibility_score": 58, "margin_bridge_score": 45, "revision_score": 25, "relative_strength_score": 48, "customer_quality_score": 52, "policy_or_regulatory_score": 80, "valuation_repricing_score": 62, "execution_risk_score": 50, "legal_or_contract_risk_score": 20, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_after": 82, "stage_label_after": "Stage2-Actionable", "changed_components": ["supply_chain_bridge +8"], "component_delta_explanation": "C04 shadow profile separates policy headline from direct project role, contract bridge, and legal-delay risk.", "MFE_90D_pct": 31.92, "MAE_90D_pct": -16.04, "score_return_alignment_label": "supply_chain_positive_after_confirmation_lag", "current_profile_verdict": "current_profile_too_late"}
{"row_type": "score_simulation", "profile_id": "C04_direct_project_role_shadow_profile", "case_id": "R1L12_C04_034020_CZECH_NSSS_HIGH_MAE", "trigger_id": "R1L12_C04_034020_CZECH_NSSS_HIGH_MAE_STAGE2_ACTIONABLE", "symbol": "034020", "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "canonical_archetype_id": "C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY", "raw_component_scores_before": {"contract_score": 55, "backlog_visibility_score": 55, "margin_bridge_score": 45, "revision_score": 25, "relative_strength_score": 65, "customer_quality_score": 70, "policy_or_regulatory_score": 85, "valuation_repricing_score": 65, "execution_risk_score": 55, "legal_or_contract_risk_score": 25, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_before": 84, "stage_label_before": "Stage3-Yellow", "raw_component_scores_after": {"contract_score": 50, "backlog_visibility_score": 55, "margin_bridge_score": 35, "revision_score": 25, "relative_strength_score": 65, "customer_quality_score": 70, "policy_or_regulatory_score": 85, "valuation_repricing_score": 65, "execution_risk_score": 65, "legal_or_contract_risk_score": 40, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_after": 78, "stage_label_after": "Stage2-Actionable", "changed_components": ["gap_MAE_guard -6", "no confirmed margin bridge -2"], "component_delta_explanation": "C04 shadow profile separates policy headline from direct project role, contract bridge, and legal-delay risk.", "MFE_90D_pct": 19.05, "MAE_90D_pct": -27.86, "score_return_alignment_label": "event_spike_then_deep_MAE_then_recovery", "current_profile_verdict": "current_profile_4B_too_early"}
{"row_type": "score_simulation", "profile_id": "C04_direct_project_role_shadow_profile", "case_id": "R1L12_C04_052690_CZECH_DESIGN_PURE_PLAY_SPIKE", "trigger_id": "R1L12_C04_052690_CZECH_DESIGN_PURE_PLAY_SPIKE_STAGE2_ACTIONABLE", "symbol": "052690", "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "canonical_archetype_id": "C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY", "raw_component_scores_before": {"contract_score": 50, "backlog_visibility_score": 45, "margin_bridge_score": 30, "revision_score": 20, "relative_strength_score": 80, "customer_quality_score": 60, "policy_or_regulatory_score": 85, "valuation_repricing_score": 75, "execution_risk_score": 60, "legal_or_contract_risk_score": 25, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_before": 88, "stage_label_before": "Stage3-Green", "raw_component_scores_after": {"contract_score": 25, "backlog_visibility_score": 25, "margin_bridge_score": 30, "revision_score": 20, "relative_strength_score": 80, "customer_quality_score": 60, "policy_or_regulatory_score": 85, "valuation_repricing_score": 55, "execution_risk_score": 70, "legal_or_contract_risk_score": 45, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_after": 66, "stage_label_after": "Stage2-Watch", "changed_components": ["policy_headline_gap_guard -12", "direct contract bridge missing -10"], "component_delta_explanation": "C04 shadow profile separates policy headline from direct project role, contract bridge, and legal-delay risk.", "MFE_90D_pct": 19.63, "MAE_90D_pct": -24.88, "score_return_alignment_label": "opening_gap_peak_failed_to_convert", "current_profile_verdict": "current_profile_false_positive"}
{"row_type": "residual_contribution", "round": "R1", "loop": "12", "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "canonical_archetype_id": "C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY", "new_independent_case_count": 5, "reused_case_count": 0, "new_symbol_count": 5, "new_trigger_family_count": 1, "tested_existing_calibrated_axes": ["stage2_actionable_evidence_bonus", "price_only_blowoff_blocks_positive_stage", "full_4b_requires_non_price_evidence", "hard_4c_thesis_break_routes_to_4c"], "residual_error_types_found": ["policy_headline_gap_false_positive", "high_MAE_positive", "local_4B_too_early", "legal_delay_not_yet_hard_4C"], "loop_contribution_label": "canonical_archetype_rule_candidate", "do_not_propose_new_weight_delta": false}
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
completed_round = R1
completed_loop = 12
next_round = R2
next_loop = 12
round_schedule_status = valid
round_sector_consistency = pass
```

## 28. Source Notes

```text
Stock-Web source:
- Songdaiki/stock-web atlas/manifest.json inspected.
- Songdaiki/stock-web symbol profiles inspected for 034020, 052690, 051600, 083650, 100840.
- Songdaiki/stock-web tradable OHLC shards inspected for 2024 and 2025 rows cited in Price Data Source Map.

Public event references used for evidence timing:
- Reuters, 2024-07-17: South Korea's KHNP selected as preferred bidder for Czech nuclear project.
- Reuters, 2024-10-30: Czech watchdog preliminary measure / appeals context.
- AP, 2025-05-06: Czech court temporarily blocks signing; used as narrative-only 4C watch context.

Non-investment statement:
- This MD is historical calibration research only. It is not live candidate discovery, stock recommendation, or trading advice.
```
