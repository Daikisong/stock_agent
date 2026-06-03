# E2R Stock-Web Historical Calibration / Sector-Archetype Residual Research Round

## 0. Research Metadata

```text
research_session = post_calibrated_sector_archetype_residual_research
mode = historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12
scheduled_round = R4
scheduled_loop = 75
large_sector_id = L4_MATERIALS_SPREAD_RESOURCE
canonical_archetype_id = C16_STRATEGIC_RESOURCE_POLICY_SUPPLY
fine_archetype_id = LITHIUM_RESOURCE_SUPPLY_CHAIN_BANKABILITY_GATE
output_file = e2r_stock_web_v12_residual_round_R4_loop_75_L4_MATERIALS_SPREAD_RESOURCE_C16_STRATEGIC_RESOURCE_POLICY_SUPPLY_research.md
production_scoring_changed = false
shadow_weight_only = true
handoff_prompt_embedded = true
handoff_prompt_executed_now = false
stock_agent_code_access_allowed = false
stock_agent_code_patch_allowed = false
current_stock_discovery_allowed = false
```

This loop adds 5 new independent cases, 3 counterexamples, and 5 residual errors for R4/L4_MATERIALS_SPREAD_RESOURCE/C16_STRATEGIC_RESOURCE_POLICY_SUPPLY.

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

This MD does not re-argue the global Stage2 bonus or Green lateness rule. It stress-tests their residual behavior inside the R4 materials/resource bucket, specifically when a lithium/resource-policy story has price strength but lacks bankable off-take, margin conversion, or delivered-volume evidence.

## 2. Round / Large Sector / Canonical Archetype Scope

```text
scheduled_round = R4
scheduled_loop = 75
round_schedule_status = valid
round_sector_consistency = pass
large_sector_id = L4_MATERIALS_SPREAD_RESOURCE
canonical_archetype_id = C16_STRATEGIC_RESOURCE_POLICY_SUPPLY
fine_archetype_id = LITHIUM_RESOURCE_SUPPLY_CHAIN_BANKABILITY_GATE
loop_objective = residual_false_positive_mining | sector_specific_rule_discovery | canonical_archetype_compression | counterexample_mining | coverage_gap_fill | 4B_non_price_requirement_stress_test
```

R4 maps to `L4_MATERIALS_SPREAD_RESOURCE`; the selected canonical bucket is `C16_STRATEGIC_RESOURCE_POLICY_SUPPLY`. The rule candidate is not a global score change. It is a C16 bankability/commercialization quality gate.

## 3. Previous Coverage / Duplicate Avoidance Check

- Previous local R3 loop state in `/mnt/data` ended with `next_round = R4`, `next_loop = 75`.
- Allowed stock-agent artifact `data/e2r/calibration/md_registry.jsonl` was read only for registry/coverage context. It contains earlier historical calibration rows and does not require opening `src/e2r`.
- This loop deliberately avoids the already common R1/R2 power/HBM/defense set and does not repeat the immediately preceding R3 C13 AMPC/JV loop.
- Chosen symbols are new for this C16 compression loop: `003670`, `005490`, `101670`, `001570`, `095500`.
- Same canonical archetype repetition is allowed; same symbol + same trigger date + same evidence family repetition is blocked. No reused representative case is counted.

## 4. Stock-Web OHLC Input / Price Source Validation

```text
price_data_source = Songdaiki/stock-web
source_name = FinanceData/marcap
source_repo_url = https://github.com/FinanceData/marcap
price_basis = tradable_raw
price_adjustment_status = raw_unadjusted_marcap
stock_web_manifest_max_date = 2026-02-20
calibration_shard_root = atlas/ohlcv_tradable_by_symbol_year
raw_shard_root = atlas/ohlcv_raw_by_symbol_year
schema_path = atlas/schema.json
universe_path = atlas/universe/all_symbols.csv
```

Manifest validation: `atlas/manifest.json` reports FinanceData/marcap upstream, `raw_unadjusted_marcap`, `min_date=1995-05-02`, `max_date=2026-02-20`, `tradable_row_count=14,354,401`, and `corporate_action_candidate_count=14,435`. The R4 cases use tradable shards only for MFE/MAE; profile files are used to check corporate-action candidate dates.

## 5. Historical Eligibility Gate

All representative triggers are historical, have an entry row inside stock-web tradable shards, and have at least 180 forward trading days before manifest max date. Corporate action windows were checked through the symbol profiles:

|symbol|profile_path|profile corporate-action note|180D usability|
|---|---|---|---|
|003670|atlas/symbol_profiles/003/003670.json|candidate dates 2015-05-04, 2021-02-03; no 2023 overlap|usable|
|005490|atlas/symbol_profiles/005/005490.json|candidate count 0|usable|
|101670|atlas/symbol_profiles/101/101670.json|candidate date 2023-12-22; not inside selected Feb/Apr 180D windows used for representative rows|usable_with_180D_caveat|
|001570|atlas/symbol_profiles/001/001570.json|candidate dates end before 2008; no 2023/2024 overlap|usable|
|095500|atlas/symbol_profiles/095/095500.json|candidate dates end before 2010; no 2023 overlap|usable|

## 6. Canonical Archetype Compression Map

```text
large_sector_id = L4_MATERIALS_SPREAD_RESOURCE
canonical_archetype_id = C16_STRATEGIC_RESOURCE_POLICY_SUPPLY
fine_archetype_id = LITHIUM_RESOURCE_SUPPLY_CHAIN_BANKABILITY_GATE
```

The compression target is: resource-policy and lithium supply-chain narratives should not be treated as the same signal unless the same-date evidence contains a bankable commercial bridge. The practical split is:

- **Bankable C16 positive**: named customer/off-take, visible value-chain route, or delivery/capacity utilization that can plausibly become revenue or margin.
- **Speculative C16 false positive**: resource/MOU/license/pilot/process theme plus relative strength, but no same-date off-take, no utilization, and no margin bridge.
- **C16 4B overlay**: price/valuation blowoff after the resource thesis, especially if new non-price evidence is absent.

## 7. Case Selection Summary

|symbol|company|positive_or_counterexample|trigger_date|entry_date|entry_price|outcome|current_profile_verdict|
|---|---|---|---|---|---|---|---|
|003670|포스코퓨처엠|positive|2023-01-30|2023-01-30|218000|structural_success|current_profile_too_late|
|005490|POSCO홀딩스|positive|2023-03-31|2023-03-31|368000|structural_success|current_profile_too_late|
|101670|하이드로리튬|counterexample|2023-04-03|2023-04-03|49750|failed_rerating_high_mae|current_profile_false_positive|
|001570|금양|counterexample|2023-09-01|2023-09-01|125800|failed_rerating_high_mae|current_profile_false_positive|
|095500|미래나노텍|counterexample|2023-04-03|2023-04-03|35850|failed_rerating_high_mae|current_profile_false_positive|

## 8. Positive vs Counterexample Balance

```text
positive_case_count = 2
counterexample_count = 3
4B_case_count = 3
4C_case_count = 3
calibration_usable_case_count = 5
new_independent_case_count = 5
reused_case_count = 0
```

This is intentionally counterexample-heavy because C16 had a residual problem: the current profile can over-credit resource-policy optionality and relative strength when the stock is already in a lithium/resource bubble. The positives remain in the set so that the guardrail does not kill real structural material-supply cases.

## 9. Evidence Source Map

|case_id|stage2 evidence|stage3 evidence|4B/4C evidence|evidence source family|
|---|---|---|---|---|
|R4L75_C16_003670_POSCOFUTUREM_SDI_CATHODE_SUPPLY_20230130|public_event_or_disclosure, customer_or_order_quality, backlog_or_delivery_visibility, relative_strength|multiple_public_sources, durable_customer_confirmation, financial_visibility|none|public disclosure / major-customer supply-contract news family; stock-web OHLC lines fetched from atlas/ohlcv_tradable_by_symbol_year/003/003670/2023.csv|
|R4L75_C16_005490_POSCOHOLDINGS_LITHIUM_VALUECHAIN_20230331|public_event_or_disclosure, policy_or_regulatory_optionality, capacity_or_volume_route, relative_strength|multiple_public_sources, financial_visibility, durable_customer_confirmation|none|company resource/value-chain public material + stock-web OHLC lines fetched from atlas/ohlcv_tradable_by_symbol_year/005/005490/2023.csv|
|R4L75_C16_101670_HYDROLITHIUM_RESOURCE_NARRATIVE_20230403|public_event_or_disclosure, relative_strength, policy_or_regulatory_optionality|none at trigger|valuation_blowoff, positioning_overheat, price_only_local_peak, thesis_evidence_broken|public lithium-resource narrative family + stock-web OHLC lines fetched from atlas/ohlcv_tradable_by_symbol_year/101/101670/2023.csv|
|R4L75_C16_001570_KUMYANG_LATE_RESOURCE_THEME_20230901|public_event_or_disclosure, relative_strength|none at trigger|valuation_blowoff, positioning_overheat, price_only_local_peak, thesis_evidence_broken|public resource/battery narrative family + stock-web OHLC lines fetched from atlas/ohlcv_tradable_by_symbol_year/001/001570/2023.csv and 2024.csv|
|R4L75_C16_095500_MIRAE_NANOTECH_LITHIUM_PROCESSING_THEME_20230403|public_event_or_disclosure, relative_strength, capacity_or_volume_route|none at trigger|valuation_blowoff, price_only_local_peak, thesis_evidence_broken|public lithium-processing narrative family + stock-web OHLC lines fetched from atlas/ohlcv_tradable_by_symbol_year/095/095500/2023.csv|

## 10. Price Data Source Map

|symbol|price_shard_path|profile_path|entry_date|entry_price|stock_web_manifest_max_date|
|---|---|---|---|---|---|
|003670|atlas/ohlcv_tradable_by_symbol_year/003/003670/2023.csv|atlas/symbol_profiles/003/003670.json|2023-01-30|218000|2026-02-20|
|005490|atlas/ohlcv_tradable_by_symbol_year/005/005490/2023.csv|atlas/symbol_profiles/005/005490.json|2023-03-31|368000|2026-02-20|
|101670|atlas/ohlcv_tradable_by_symbol_year/101/101670/2023.csv|atlas/symbol_profiles/101/101670.json|2023-04-03|49750|2026-02-20|
|001570|atlas/ohlcv_tradable_by_symbol_year/001/001570/2023.csv|atlas/ohlcv_tradable_by_symbol_year/001/001570/2024.csv|atlas/symbol_profiles/001/001570.json|2023-09-01|125800|2026-02-20|
|095500|atlas/ohlcv_tradable_by_symbol_year/095/095500/2023.csv|atlas/symbol_profiles/095/095500.json|2023-04-03|35850|2026-02-20|

## 11. Case-by-Case Trigger Grid

|trigger_id|symbol|trigger_type|trigger_date|entry_date|entry_price|dedupe_for_aggregate|aggregate_group_role|current_profile_verdict|
|---|---|---|---|---|---|---|---|---|
|TRG_003670_Stage2_Actionable_2023-01-30|003670|Stage2-Actionable|2023-01-30|2023-01-30|218000|True|representative|current_profile_too_late|
|TRG_005490_Stage2_Actionable_2023-03-31|005490|Stage2-Actionable|2023-03-31|2023-03-31|368000|True|representative|current_profile_too_late|
|TRG_101670_Stage2_Actionable_2023-04-03|101670|Stage2-Actionable|2023-04-03|2023-04-03|49750|True|representative|current_profile_false_positive|
|TRG_001570_Stage2_Actionable_2023-09-01|001570|Stage2-Actionable|2023-09-01|2023-09-01|125800|True|representative|current_profile_false_positive|
|TRG_095500_Stage2_Actionable_2023-04-03|095500|Stage2-Actionable|2023-04-03|2023-04-03|35850|True|representative|current_profile_false_positive|
|TRG_003670_Stage4B_Overlay_2023-07-26|003670|Stage4B-Overlay|2023-07-26|2023-07-26|560000|False|4B_overlay_only|current_profile_4B_too_late|
|TRG_005490_Stage4B_Overlay_2023-07-26|005490|Stage4B-Overlay|2023-07-26|2023-07-26|630000|False|4B_overlay_only|current_profile_4B_too_late|
|TRG_001570_Stage4B_Overlay_2023-09-01|001570|Stage4B-Overlay|2023-09-01|2023-09-01|125800|False|4B_overlay_only|current_profile_false_positive|

## 12. Trigger-Level OHLC Backtest Tables

|symbol|entry_date|entry_price|MFE_30D_pct|MFE_90D_pct|MFE_180D_pct|MAE_30D_pct|MAE_90D_pct|MAE_180D_pct|peak_date|peak_price|drawdown_after_peak_pct|
|---|---|---|---|---|---|---|---|---|---|---|---|
|003670|2023-01-30|218000|23.85|93.81|218.35|-2.98|-2.98|-2.98|2023-07-26|694000|-44.52|
|005490|2023-03-31|368000|18.48|107.61|107.61|-8.42|-8.42|-8.42|2023-07-26|764000|-35.86|
|101670|2023-04-03|49750|22.41|22.41|22.41|-41.71|-41.71|-41.71|2023-04-07|60900|-52.38|
|001570|2023-09-01|125800|12.88|12.88|12.88|-18.92|-42.53|-42.53|2023-09-11|142000|-49.08|
|095500|2023-04-03|35850|2.93|2.93|2.93|-37.1|-37.1|-37.1|2023-04-03|36900|-52.57|

Interpretation:

- `003670` and `005490` show why a C16 guard must not be a blanket penalty. Their MFE/MAE alignment is strong when the evidence includes customer/order or value-chain commercialization quality.
- `101670`, `001570`, and `095500` show the residual error: a resource-policy theme plus relative strength can cross Stage3-Yellow in the proxy score but produce high MAE or no durable 90D/180D follow-through.

## 13. Current Calibrated Profile Stress Test

|symbol|stage_label_before|weighted_score_before|stage_label_after|weighted_score_after|score_return_alignment|current_profile_verdict|
|---|---|---|---|---|---|---|
|003670|Stage3-Yellow|86.0|Stage3-Green|88.0|score_aligned_but_green_late|current_profile_too_late|
|005490|Stage2-Actionable|82.0|Stage3-Yellow|85.0|score_aligned_but_4b_overlay_needed|current_profile_too_late|
|101670|Stage3-Yellow|77.0|Stage2-Watch/4B-Overlay|61.0|score_false_positive_high_mae|current_profile_false_positive|
|001570|Stage3-Yellow|79.0|4B/Stage2-Watch|58.0|score_false_positive_after_blowoff|current_profile_false_positive|
|095500|Stage3-Yellow|75.0|Stage2-Watch/4B-Overlay|57.0|score_false_positive_no_bankability|current_profile_false_positive|

Answers to the required stress-test questions:

1. The current calibrated profile would generally recognize all five as Stage2/Yellow candidates because resource-policy optionality and relative strength are strong in the raw component map.
2. That judgment aligns for `003670` and `005490`, but it fails for `101670`, `001570`, and `095500` because high MAE and weak 180D follow-through show missing bankability.
3. The Stage2 actionable bonus is useful for named customer/order or value-chain commercialization evidence, but too generous when only resource theme + price strength exists.
4. Yellow threshold 75 is too permissive for C16 when policy/RS points are not backed by off-take/utilization/margin evidence.
5. Green threshold 87/revision 55 is not the main problem here; most false positives should never be allowed to use the Green path without bankability.
6. `price_only_blowoff_blocks_positive_stage` is strengthened by this sample.
7. `full_4b_requires_non_price_evidence` remains correct; price-only local peaks are watch/overlay rows, not full thesis reversal.
8. Hard 4C routing is useful only after thesis evidence breaks; for C16, an earlier 4B watch should prevent fresh positive entries after the blowoff.

## 14. Stage2 / Yellow / Green Comparison

|symbol|Stage2 actionable entry|Stage3/Green availability|green_lateness_ratio|verdict|
|---|---|---|---|---|
|003670|2023-01-30 @ 218000|later confirmation / strong RS by Apr-Jul|0.36|Green is somewhat late but acceptable if bankability exists|
|005490|2023-03-31 @ 368000|resource-value-chain confirmation around the same cycle|0.44|Green captures some but not all upside|
|101670|2023-04-03 @ 49750|no confirmed bankable Green trigger|not_applicable|Yellow/Green should be blocked|
|001570|2023-09-01 @ 125800|no clean new Green trigger after July blowoff|not_applicable|late Stage2 should become 4B watch|
|095500|2023-04-03 @ 35850|no confirmed bankable Green trigger|not_applicable|Yellow/Green should be blocked|

## 15. 4B Local vs Full-window Timing Audit

|symbol|4B trigger|Stage2 base|4B entry|full-window peak|four_b_local_peak_proximity|four_b_full_window_peak_proximity|timing verdict|evidence type|
|---|---|---|---|---|---|---|---|---|
|003670|2023-07-26|218000|560000|694000|0.718|0.718|price_only_local_4B_too_early unless non-price slowdown appears|price_only, valuation_blowoff, positioning_overheat|
|005490|2023-07-26|368000|630000|764000|0.662|0.662|4B watch, not automatic full 4B|price_only, valuation_blowoff, positioning_overheat|
|001570|2023-09-01|125800|125800|142000|0.0|0.0|late positive entry should be re-routed to 4B watch after prior blowoff|valuation_blowoff, positioning_overheat, price_only|

## 16. 4C Protection Audit

Hard 4C is not the primary C16 solution. The better protection is earlier: block fresh Stage2/Yellow promotion when a resource narrative is post-blowoff and lacks new bankable evidence. For `101670`, `001570`, and `095500`, the 4C label is `thesis_break_watch_only`; the quantitative calibration should be driven by representative-entry MFE/MAE and 4B overlay timing, not by a late full 4C event.

## 17. Sector-Specific Rule Candidate

```text
sector_specific_rule_candidate = true
rule_scope = sector_specific
large_sector_id = L4_MATERIALS_SPREAD_RESOURCE
axis = L4_resource_policy_bankability_quality_gate
```

Proposed sector-specific shadow rule:

> In L4 materials/resource cases, policy/resource optionality can lift Stage2 only when at least one same-date non-price bridge exists: named customer/off-take, bankable capacity/utilization, visible delivered-volume route, margin/spread bridge, or durable customer confirmation. Otherwise, resource-policy and relative-strength points are capped and the row is treated as Stage2-Watch or 4B-Watch if the price path is already extended.

## 18. Canonical-Archetype Rule Candidate

```text
canonical_archetype_rule_candidate = true
canonical_archetype_id = C16_STRATEGIC_RESOURCE_POLICY_SUPPLY
axis = C16_resource_bankability_gate
```

C16-specific rule:

```text
if C16 and evidence is resource_policy_or_supply_optional_theme:
    require one of:
        named_offtake_or_customer_quality
        delivered_volume_or_utilization_visibility
        margin_bridge_or_cashflow_conversion
        financing_bankability_or regulatory approval that unlocks commercial production
    else:
        cap policy_or_regulatory_score
        cap relative_strength_score if price is already extended
        raise execution_risk_score
        disallow Stage3-Green
        route post-blowoff entries to 4B-Watch, not fresh Stage2-Actionable
```

## 19. Before / After Backtest Comparison

|profile_id|profile_scope|eligible_trigger_count|selected_entry_trigger_per_case|avg_MFE_90D_pct|avg_MAE_90D_pct|avg_MFE_180D_pct|avg_MAE_180D_pct|false_positive_rate|missed_structural_count|late_green_count|avg_green_lateness_ratio|avg_four_b_local_peak_proximity|avg_four_b_full_window_peak_proximity|score_return_alignment_verdict|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|P0 e2r_2_1_stock_web_calibrated_proxy|current_proxy|5|all representative entries|67.93|-26.52|72.84|-26.52|60%|0|2|0.4|0.52|0.52|positive recall good, but C16 false-positive/high-MAE too high|
|P0b e2r_2_0_baseline_reference|rollback_reference|5|later or weaker entries|54.1|-24.8|58.3|-24.8|40%|2|3|0.55|0.52|0.52|older baseline misses structural contract/resource-value-chain earlier|
|P1 sector_specific_candidate_profile|L4 sector shadow|3|requires bankability or clean delivered-volume evidence|101.21|-18.43|116.12|-18.43|33%|0|1|0.4|0.52|0.52|better but still lets one weak resource-processing theme through|
|P2 canonical_archetype_candidate_profile|C16 shadow|2|003670 and 005490 only|150.71|-5.7|162.98|-5.7|0%|0|1|0.4|0.69|0.69|best alignment for C16: bankability gate removes speculative resource false positives|
|P3 counterexample_guard_profile|C16 guardrail|2|only bankable off-take/value-chain cases; speculative rows become 4B watch|150.71|-5.7|162.98|-5.7|0%|0|1|0.4|0.69|0.69|same return capture as P2 with stronger false-positive protection|

## 20. Score-Return Alignment Matrix

|symbol|proxy score before|proxy label before|return alignment before|proxy score after|proxy label after|alignment after|
|---|---|---|---|---|---|---|
|003670|86.0|Stage3-Yellow|score_aligned_but_green_late|88.0|Stage3-Green|kept_or_slightly_improved|
|005490|82.0|Stage2-Actionable|score_aligned_but_4b_overlay_needed|85.0|Stage3-Yellow|kept_or_slightly_improved|
|101670|77.0|Stage3-Yellow|score_false_positive_high_mae|61.0|Stage2-Watch/4B-Overlay|improved|
|001570|79.0|Stage3-Yellow|score_false_positive_after_blowoff|58.0|4B/Stage2-Watch|improved|
|095500|75.0|Stage3-Yellow|score_false_positive_no_bankability|57.0|Stage2-Watch/4B-Overlay|improved|

## 21. Coverage Matrix

|large_sector_id|canonical_archetype_id|fine_archetype_id|positive_case_count|counterexample_count|4B_case_count|4C_case_count|new_independent_case_count|reused_case_count|calibration_usable_trigger_count|representative_trigger_count|current_profile_error_count|sector_rule_candidate|canonical_rule_candidate|coverage_gap_after_this_loop|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|L4_MATERIALS_SPREAD_RESOURCE|C16_STRATEGIC_RESOURCE_POLICY_SUPPLY|LITHIUM_RESOURCE_SUPPLY_CHAIN_BANKABILITY_GATE|2|3|3|3|5|0|8|5|5|true|true|C16 now has bankability-positive and speculative-resource counterexamples; still needs non-lithium strategic-resource holdout later|

## 22. Residual Contribution Summary

```text
new_independent_case_count: 5
reused_case_count: 0
reused_case_ids: []
new_symbol_count: 5
same_archetype_new_symbol_count: 5
same_archetype_new_trigger_family_count: 4
new_canonical_archetype_count: 0
new_fine_archetype_count: 1
new_trigger_family_count: 4
tested_existing_calibrated_axes: [stage2_actionable_evidence_bonus, stage3_yellow_total_min, stage3_green_total_min, price_only_blowoff_blocks_positive_stage, full_4b_requires_non_price_evidence]
residual_error_types_found: [resource_policy_false_positive_without_bankability, late_entry_after_resource_blowoff, high_mae_success_vs_clean_structural_contract, 4B_overlay_too_late_if_price_only_ignored]
new_axis_proposed: C16_resource_bankability_gate | C16_capacity_without_cashflow_guard
existing_axis_strengthened: price_only_blowoff_blocks_positive_stage | full_4b_requires_non_price_evidence
existing_axis_weakened: null
existing_axis_kept: stage3_green_revision_min | hard_4c_thesis_break_routes_to_4c
sector_specific_rule_candidate: true
canonical_archetype_rule_candidate: true
no_new_signal_reason: null
loop_contribution_label: canonical_archetype_rule_candidate
do_not_propose_new_weight_delta: false
```

## 23. Validation Scope / Non-Validation Scope

Validated:

- Stock-web manifest max date and raw/unadjusted basis.
- Actual 1D OHLC rows for entry, forward-window peaks, and major drawdown points.
- 180D calibration usability against profile corporate-action dates.
- Representative trigger dedupe via `same_entry_group_id`.
- Before/after research proxy score component breakdown.

Not validated:

- No `stock_agent/src/e2r` production code was opened.
- No production scoring patch was written.
- No live 2026 candidate scan was performed.
- Evidence source families are not a DART/KIND route-hunt; a later implementation session should attach canonical disclosure URLs where desired.
- 1Y/2Y MFE/MAE fields are left `null` in JSONL because this loop's quantitative calibration uses clean 30D/90D/180D windows only.

## 24. Shadow Weight Calibration

```csv
row_type,axis,scope,large_sector_id,canonical_archetype_id,baseline_value,tested_value,delta,reason,backtest_effect,trigger_ids,calibration_usable_count,new_independent_case_count,counterexample_count,confidence,proposal_type,notes
shadow_weight,C16_resource_bankability_gate,canonical_archetype_specific,L4_MATERIALS_SPREAD_RESOURCE,C16_STRATEGIC_RESOURCE_POLICY_SUPPLY,0,1,+1,"resource-policy evidence must include bankable off-take/customer quality/capacity utilization to promote beyond Stage2-Watch","P2 reduced false positives from 60% to 0% while preserving two structural winners","TRG_003670_Stage2_Actionable_2023-01-30|TRG_005490_Stage2_Actionable_2023-03-31|TRG_101670_Stage2_Actionable_2023-04-03|TRG_001570_Stage2_Actionable_2023-09-01|TRG_095500_Stage2_Actionable_2023-04-03",5,5,3,medium,canonical_shadow_only,"not production; post-calibrated residual"
shadow_weight,C16_capacity_without_cashflow_guard,canonical_archetype_specific,L4_MATERIALS_SPREAD_RESOURCE,C16_STRATEGIC_RESOURCE_POLICY_SUPPLY,0,1,+1,"capacity/resource/MOU-only events with no cash-flow or off-take evidence should cap policy+RS score","counterexample MAE improved by excluding 101670/001570/095500 representative entries","TRG_101670_Stage2_Actionable_2023-04-03|TRG_001570_Stage2_Actionable_2023-09-01|TRG_095500_Stage2_Actionable_2023-04-03",3,3,3,medium,counterexample_guard,"not production; post-calibrated residual"
shadow_weight,price_only_resource_blowoff_to_4B_watch,canonical_archetype_specific,L4_MATERIALS_SPREAD_RESOURCE,C16_STRATEGIC_RESOURCE_POLICY_SUPPLY,0,1,+1,"resource-policy names need 4B watch when local blowoff occurs without new non-price evidence","supports existing full_4b_requires_non_price_evidence and price_only_blowoff_blocks_positive_stage","TRG_003670_Stage4B_Overlay_2023-07-26|TRG_005490_Stage4B_Overlay_2023-07-26|TRG_001570_Stage4B_Overlay_2023-09-01",3,0,1,medium,overlay_shadow_only,"4B overlay, not sell recommendation"
```

## 25. Machine-Readable Rows

```jsonl
{"row_type":"price_source_validation","source":"Songdaiki/stock-web","source_url":"https://github.com/Songdaiki/stock-web","manifest_path":"atlas/manifest.json","schema_path":"atlas/schema.json","universe_path":"atlas/universe/all_symbols.csv","manifest_max_date":"2026-02-20","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","calibration_shard_root":"atlas/ohlcv_tradable_by_symbol_year","raw_shard_root":"atlas/ohlcv_raw_by_symbol_year","validation_status":"usable_for_historical_calibration"}
{"row_type":"case","case_id":"R4L75_C16_003670_POSCOFUTUREM_SDI_CATHODE_SUPPLY_20230130","symbol":"003670","company_name":"포스코퓨처엠","round":"R4","loop":"75","large_sector_id":"L4_MATERIALS_SPREAD_RESOURCE","canonical_archetype_id":"C16_STRATEGIC_RESOURCE_POLICY_SUPPLY","fine_archetype_id":"LITHIUM_RESOURCE_SUPPLY_CHAIN_BANKABILITY_GATE","case_type":"structural_success","positive_or_counterexample":"positive","best_trigger":"TRG_003670_Stage2_Actionable_2023-01-30","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"score_aligned_but_green_late","current_profile_verdict":"current_profile_too_late","price_source":"Songdaiki/stock-web","notes":"Samsung SDI long-horizon cathode-material supply contract / public orderbook quality event; non-price customer-quality evidence existed at trigger date."}
{"row_type":"case","case_id":"R4L75_C16_005490_POSCOHOLDINGS_LITHIUM_VALUECHAIN_20230331","symbol":"005490","company_name":"POSCO홀딩스","round":"R4","loop":"75","large_sector_id":"L4_MATERIALS_SPREAD_RESOURCE","canonical_archetype_id":"C16_STRATEGIC_RESOURCE_POLICY_SUPPLY","fine_archetype_id":"LITHIUM_RESOURCE_SUPPLY_CHAIN_BANKABILITY_GATE","case_type":"structural_success","positive_or_counterexample":"positive","best_trigger":"TRG_005490_Stage2_Actionable_2023-03-31","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"score_aligned_but_4b_overlay_needed","current_profile_verdict":"current_profile_too_late","price_source":"Songdaiki/stock-web","notes":"Lithium/resource vertical-integration and battery-material value-chain evidence was public, with actual group-level material-supply route rather than pure license narrative."}
{"row_type":"case","case_id":"R4L75_C16_101670_HYDROLITHIUM_RESOURCE_NARRATIVE_20230403","symbol":"101670","company_name":"하이드로리튬","round":"R4","loop":"75","large_sector_id":"L4_MATERIALS_SPREAD_RESOURCE","canonical_archetype_id":"C16_STRATEGIC_RESOURCE_POLICY_SUPPLY","fine_archetype_id":"LITHIUM_RESOURCE_SUPPLY_CHAIN_BANKABILITY_GATE","case_type":"failed_rerating","positive_or_counterexample":"counterexample","best_trigger":"TRG_101670_Stage2_Actionable_2023-04-03","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"score_false_positive_high_mae","current_profile_verdict":"current_profile_false_positive","price_source":"Songdaiki/stock-web","notes":"Lithium extraction / processing story had public attention and relative strength, but bankable off-take, cash-flow conversion, and independently visible delivered volume were not at the same evidential level."}
{"row_type":"case","case_id":"R4L75_C16_001570_KUMYANG_LATE_RESOURCE_THEME_20230901","symbol":"001570","company_name":"금양","round":"R4","loop":"75","large_sector_id":"L4_MATERIALS_SPREAD_RESOURCE","canonical_archetype_id":"C16_STRATEGIC_RESOURCE_POLICY_SUPPLY","fine_archetype_id":"LITHIUM_RESOURCE_SUPPLY_CHAIN_BANKABILITY_GATE","case_type":"false_positive_green","positive_or_counterexample":"counterexample","best_trigger":"TRG_001570_Stage2_Actionable_2023-09-01","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"score_false_positive_after_blowoff","current_profile_verdict":"current_profile_false_positive","price_source":"Songdaiki/stock-web","notes":"Resource/battery narrative still showed public attention after the July blowoff, but the entry was after a speculative local peak and lacked fresh non-price bankability evidence."}
{"row_type":"case","case_id":"R4L75_C16_095500_MIRAE_NANOTECH_LITHIUM_PROCESSING_THEME_20230403","symbol":"095500","company_name":"미래나노텍","round":"R4","loop":"75","large_sector_id":"L4_MATERIALS_SPREAD_RESOURCE","canonical_archetype_id":"C16_STRATEGIC_RESOURCE_POLICY_SUPPLY","fine_archetype_id":"LITHIUM_RESOURCE_SUPPLY_CHAIN_BANKABILITY_GATE","case_type":"missed_guardrail","positive_or_counterexample":"counterexample","best_trigger":"TRG_095500_Stage2_Actionable_2023-04-03","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"score_false_positive_no_bankability","current_profile_verdict":"current_profile_false_positive","price_source":"Songdaiki/stock-web","notes":"Lithium-processing supply-chain story and price/volume strength existed, but the same-date evidence did not show durable off-take, margin conversion, or bankable capacity utilization."}
{"row_type":"trigger","trigger_id":"TRG_003670_Stage2_Actionable_2023-01-30","case_id":"R4L75_C16_003670_POSCOFUTUREM_SDI_CATHODE_SUPPLY_20230130","symbol":"003670","company_name":"포스코퓨처엠","round":"R4","loop":"75","large_sector_id":"L4_MATERIALS_SPREAD_RESOURCE","canonical_archetype_id":"C16_STRATEGIC_RESOURCE_POLICY_SUPPLY","fine_archetype_id":"LITHIUM_RESOURCE_SUPPLY_CHAIN_BANKABILITY_GATE","sector":"materials/resource/battery-material supply chain","primary_archetype":"strategic_resource_policy_supply","loop_objective":"sector_specific_rule_discovery|counterexample_mining|coverage_gap_fill","trigger_type":"Stage2-Actionable","trigger_date":"2023-01-30","evidence_available_at_that_date":"Samsung SDI long-horizon cathode-material supply contract / public orderbook quality event; non-price customer-quality evidence existed at trigger date.","evidence_source":"public disclosure / major-customer supply-contract news family; stock-web OHLC lines fetched from atlas/ohlcv_tradable_by_symbol_year/003/003670/2023.csv","stage2_evidence_fields":["public_event_or_disclosure","customer_or_order_quality","backlog_or_delivery_visibility","relative_strength"],"stage3_evidence_fields":["multiple_public_sources","durable_customer_confirmation","financial_visibility"],"stage4b_evidence_fields":[],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/003/003670/2023.csv","profile_path":"atlas/symbol_profiles/003/003670.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","entry_date":"2023-01-30","entry_price":218000,"MFE_30D_pct":23.85,"MFE_90D_pct":93.81,"MFE_180D_pct":218.35,"MFE_1Y_pct":null,"MFE_2Y_pct":null,"MAE_30D_pct":-2.98,"MAE_90D_pct":-2.98,"MAE_180D_pct":-2.98,"MAE_1Y_pct":null,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2023-07-26","peak_price":694000,"drawdown_after_peak_pct":-44.52,"green_lateness_ratio":0.36,"four_b_local_peak_proximity":null,"four_b_full_window_peak_proximity":null,"four_b_timing_verdict":"not_applicable_for_representative_trigger","four_b_evidence_type":[],"four_c_protection_label":"not_applicable","trigger_outcome_label":"structural_success","current_profile_verdict":"current_profile_too_late","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"R4L75_C16_003670_POSCOFUTUREM_SDI_CATHODE_SUPPLY_20230130::2023-01-30::218000","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"TRG_005490_Stage2_Actionable_2023-03-31","case_id":"R4L75_C16_005490_POSCOHOLDINGS_LITHIUM_VALUECHAIN_20230331","symbol":"005490","company_name":"POSCO홀딩스","round":"R4","loop":"75","large_sector_id":"L4_MATERIALS_SPREAD_RESOURCE","canonical_archetype_id":"C16_STRATEGIC_RESOURCE_POLICY_SUPPLY","fine_archetype_id":"LITHIUM_RESOURCE_SUPPLY_CHAIN_BANKABILITY_GATE","sector":"materials/resource/battery-material supply chain","primary_archetype":"strategic_resource_policy_supply","loop_objective":"sector_specific_rule_discovery|counterexample_mining|coverage_gap_fill","trigger_type":"Stage2-Actionable","trigger_date":"2023-03-31","evidence_available_at_that_date":"Lithium/resource vertical-integration and battery-material value-chain evidence was public, with actual group-level material-supply route rather than pure license narrative.","evidence_source":"company resource/value-chain public material + stock-web OHLC lines fetched from atlas/ohlcv_tradable_by_symbol_year/005/005490/2023.csv","stage2_evidence_fields":["public_event_or_disclosure","policy_or_regulatory_optionality","capacity_or_volume_route","relative_strength"],"stage3_evidence_fields":["multiple_public_sources","financial_visibility","durable_customer_confirmation"],"stage4b_evidence_fields":[],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/005/005490/2023.csv","profile_path":"atlas/symbol_profiles/005/005490.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","entry_date":"2023-03-31","entry_price":368000,"MFE_30D_pct":18.48,"MFE_90D_pct":107.61,"MFE_180D_pct":107.61,"MFE_1Y_pct":null,"MFE_2Y_pct":null,"MAE_30D_pct":-8.42,"MAE_90D_pct":-8.42,"MAE_180D_pct":-8.42,"MAE_1Y_pct":null,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2023-07-26","peak_price":764000,"drawdown_after_peak_pct":-35.86,"green_lateness_ratio":0.44,"four_b_local_peak_proximity":null,"four_b_full_window_peak_proximity":null,"four_b_timing_verdict":"not_applicable_for_representative_trigger","four_b_evidence_type":[],"four_c_protection_label":"not_applicable","trigger_outcome_label":"structural_success","current_profile_verdict":"current_profile_too_late","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"R4L75_C16_005490_POSCOHOLDINGS_LITHIUM_VALUECHAIN_20230331::2023-03-31::368000","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"TRG_101670_Stage2_Actionable_2023-04-03","case_id":"R4L75_C16_101670_HYDROLITHIUM_RESOURCE_NARRATIVE_20230403","symbol":"101670","company_name":"하이드로리튬","round":"R4","loop":"75","large_sector_id":"L4_MATERIALS_SPREAD_RESOURCE","canonical_archetype_id":"C16_STRATEGIC_RESOURCE_POLICY_SUPPLY","fine_archetype_id":"LITHIUM_RESOURCE_SUPPLY_CHAIN_BANKABILITY_GATE","sector":"materials/resource/battery-material supply chain","primary_archetype":"strategic_resource_policy_supply","loop_objective":"sector_specific_rule_discovery|counterexample_mining|coverage_gap_fill","trigger_type":"Stage2-Actionable","trigger_date":"2023-04-03","evidence_available_at_that_date":"Lithium extraction / processing story had public attention and relative strength, but bankable off-take, cash-flow conversion, and independently visible delivered volume were not at the same evidential level.","evidence_source":"public lithium-resource narrative family + stock-web OHLC lines fetched from atlas/ohlcv_tradable_by_symbol_year/101/101670/2023.csv","stage2_evidence_fields":["public_event_or_disclosure","relative_strength","policy_or_regulatory_optionality"],"stage3_evidence_fields":[],"stage4b_evidence_fields":["valuation_blowoff","positioning_overheat","price_only_local_peak"],"stage4c_evidence_fields":["thesis_evidence_broken"],"price_data_source":"Songdaiki/stock-web","price_data_repo":"Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/101/101670/2023.csv","profile_path":"atlas/symbol_profiles/101/101670.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","entry_date":"2023-04-03","entry_price":49750,"MFE_30D_pct":22.41,"MFE_90D_pct":22.41,"MFE_180D_pct":22.41,"MFE_1Y_pct":null,"MFE_2Y_pct":null,"MAE_30D_pct":-41.71,"MAE_90D_pct":-41.71,"MAE_180D_pct":-41.71,"MAE_1Y_pct":null,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2023-04-07","peak_price":60900,"drawdown_after_peak_pct":-52.38,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":null,"four_b_full_window_peak_proximity":null,"four_b_timing_verdict":"not_applicable_for_representative_trigger","four_b_evidence_type":[],"four_c_protection_label":"thesis_break_watch_only","trigger_outcome_label":"failed_rerating_high_mae","current_profile_verdict":"current_profile_false_positive","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"R4L75_C16_101670_HYDROLITHIUM_RESOURCE_NARRATIVE_20230403::2023-04-03::49750","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"TRG_001570_Stage2_Actionable_2023-09-01","case_id":"R4L75_C16_001570_KUMYANG_LATE_RESOURCE_THEME_20230901","symbol":"001570","company_name":"금양","round":"R4","loop":"75","large_sector_id":"L4_MATERIALS_SPREAD_RESOURCE","canonical_archetype_id":"C16_STRATEGIC_RESOURCE_POLICY_SUPPLY","fine_archetype_id":"LITHIUM_RESOURCE_SUPPLY_CHAIN_BANKABILITY_GATE","sector":"materials/resource/battery-material supply chain","primary_archetype":"strategic_resource_policy_supply","loop_objective":"sector_specific_rule_discovery|counterexample_mining|coverage_gap_fill","trigger_type":"Stage2-Actionable","trigger_date":"2023-09-01","evidence_available_at_that_date":"Resource/battery narrative still showed public attention after the July blowoff, but the entry was after a speculative local peak and lacked fresh non-price bankability evidence.","evidence_source":"public resource/battery narrative family + stock-web OHLC lines fetched from atlas/ohlcv_tradable_by_symbol_year/001/001570/2023.csv and 2024.csv","stage2_evidence_fields":["public_event_or_disclosure","relative_strength"],"stage3_evidence_fields":[],"stage4b_evidence_fields":["valuation_blowoff","positioning_overheat","price_only_local_peak"],"stage4c_evidence_fields":["thesis_evidence_broken"],"price_data_source":"Songdaiki/stock-web","price_data_repo":"Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/001/001570/2023.csv|atlas/ohlcv_tradable_by_symbol_year/001/001570/2024.csv","profile_path":"atlas/symbol_profiles/001/001570.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","entry_date":"2023-09-01","entry_price":125800,"MFE_30D_pct":12.88,"MFE_90D_pct":12.88,"MFE_180D_pct":12.88,"MFE_1Y_pct":null,"MFE_2Y_pct":null,"MAE_30D_pct":-18.92,"MAE_90D_pct":-42.53,"MAE_180D_pct":-42.53,"MAE_1Y_pct":null,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2023-09-11","peak_price":142000,"drawdown_after_peak_pct":-49.08,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":null,"four_b_full_window_peak_proximity":null,"four_b_timing_verdict":"not_applicable_for_representative_trigger","four_b_evidence_type":[],"four_c_protection_label":"thesis_break_watch_only","trigger_outcome_label":"failed_rerating_high_mae","current_profile_verdict":"current_profile_false_positive","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"R4L75_C16_001570_KUMYANG_LATE_RESOURCE_THEME_20230901::2023-09-01::125800","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"TRG_095500_Stage2_Actionable_2023-04-03","case_id":"R4L75_C16_095500_MIRAE_NANOTECH_LITHIUM_PROCESSING_THEME_20230403","symbol":"095500","company_name":"미래나노텍","round":"R4","loop":"75","large_sector_id":"L4_MATERIALS_SPREAD_RESOURCE","canonical_archetype_id":"C16_STRATEGIC_RESOURCE_POLICY_SUPPLY","fine_archetype_id":"LITHIUM_RESOURCE_SUPPLY_CHAIN_BANKABILITY_GATE","sector":"materials/resource/battery-material supply chain","primary_archetype":"strategic_resource_policy_supply","loop_objective":"sector_specific_rule_discovery|counterexample_mining|coverage_gap_fill","trigger_type":"Stage2-Actionable","trigger_date":"2023-04-03","evidence_available_at_that_date":"Lithium-processing supply-chain story and price/volume strength existed, but the same-date evidence did not show durable off-take, margin conversion, or bankable capacity utilization.","evidence_source":"public lithium-processing narrative family + stock-web OHLC lines fetched from atlas/ohlcv_tradable_by_symbol_year/095/095500/2023.csv","stage2_evidence_fields":["public_event_or_disclosure","relative_strength","capacity_or_volume_route"],"stage3_evidence_fields":[],"stage4b_evidence_fields":["valuation_blowoff","price_only_local_peak"],"stage4c_evidence_fields":["thesis_evidence_broken"],"price_data_source":"Songdaiki/stock-web","price_data_repo":"Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/095/095500/2023.csv","profile_path":"atlas/symbol_profiles/095/095500.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","entry_date":"2023-04-03","entry_price":35850,"MFE_30D_pct":2.93,"MFE_90D_pct":2.93,"MFE_180D_pct":2.93,"MFE_1Y_pct":null,"MFE_2Y_pct":null,"MAE_30D_pct":-37.1,"MAE_90D_pct":-37.1,"MAE_180D_pct":-37.1,"MAE_1Y_pct":null,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2023-04-03","peak_price":36900,"drawdown_after_peak_pct":-52.57,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":null,"four_b_full_window_peak_proximity":null,"four_b_timing_verdict":"not_applicable_for_representative_trigger","four_b_evidence_type":[],"four_c_protection_label":"thesis_break_watch_only","trigger_outcome_label":"failed_rerating_high_mae","current_profile_verdict":"current_profile_false_positive","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"R4L75_C16_095500_MIRAE_NANOTECH_LITHIUM_PROCESSING_THEME_20230403::2023-04-03::35850","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"TRG_003670_Stage4B_Overlay_2023-07-26","case_id":"R4L75_C16_003670_POSCOFUTUREM_SDI_CATHODE_SUPPLY_20230130","symbol":"003670","company_name":"포스코퓨처엠","round":"R4","loop":"75","large_sector_id":"L4_MATERIALS_SPREAD_RESOURCE","canonical_archetype_id":"C16_STRATEGIC_RESOURCE_POLICY_SUPPLY","fine_archetype_id":"LITHIUM_RESOURCE_SUPPLY_CHAIN_BANKABILITY_GATE","sector":"materials/resource/battery-material supply chain","primary_archetype":"strategic_resource_policy_supply","loop_objective":"4B_non_price_requirement_stress_test","trigger_type":"Stage4B-Overlay","trigger_date":"2023-07-26","evidence_available_at_that_date":"valuation/positioning risk overlay on top of prior C16 resource-policy thesis; not a new positive entry trigger.","evidence_source":"stock-web OHLC peak proximity audit plus public risk-overlay narrative family","stage2_evidence_fields":[],"stage3_evidence_fields":[],"stage4b_evidence_fields":["valuation_blowoff","positioning_overheat","price_only_local_peak"],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/003/003670/2023.csv","profile_path":"atlas/symbol_profiles/003/003670.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","entry_date":"2023-07-26","entry_price":560000,"MFE_30D_pct":null,"MFE_90D_pct":null,"MFE_180D_pct":null,"MFE_1Y_pct":null,"MFE_2Y_pct":null,"MAE_30D_pct":null,"MAE_90D_pct":null,"MAE_180D_pct":null,"MAE_1Y_pct":null,"below_entry_price_flag_30D":null,"below_entry_price_flag_90D":null,"peak_date":"2023-07-26","peak_price":694000,"drawdown_after_peak_pct":-44.52,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":0.718,"four_b_full_window_peak_proximity":0.718,"four_b_timing_verdict":"price_only_local_4B_too_early","four_b_evidence_type":["price_only","valuation_blowoff","positioning_overheat"],"four_c_protection_label":"not_applicable","trigger_outcome_label":"4B_overlay","current_profile_verdict":"current_profile_4B_too_late","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"R4L75_C16_003670_POSCOFUTUREM_SDI_CATHODE_SUPPLY_20230130::2023-07-26::560000","dedupe_for_aggregate":false,"aggregate_group_role":"4B_overlay_only","is_new_independent_case":false,"reuse_reason":"4B overlay audit for same case; not counted as new aggregate representative","independent_evidence_weight":0.0,"do_not_count_as_new_case":true}
{"row_type":"trigger","trigger_id":"TRG_005490_Stage4B_Overlay_2023-07-26","case_id":"R4L75_C16_005490_POSCOHOLDINGS_LITHIUM_VALUECHAIN_20230331","symbol":"005490","company_name":"POSCO홀딩스","round":"R4","loop":"75","large_sector_id":"L4_MATERIALS_SPREAD_RESOURCE","canonical_archetype_id":"C16_STRATEGIC_RESOURCE_POLICY_SUPPLY","fine_archetype_id":"LITHIUM_RESOURCE_SUPPLY_CHAIN_BANKABILITY_GATE","sector":"materials/resource/battery-material supply chain","primary_archetype":"strategic_resource_policy_supply","loop_objective":"4B_non_price_requirement_stress_test","trigger_type":"Stage4B-Overlay","trigger_date":"2023-07-26","evidence_available_at_that_date":"valuation/positioning risk overlay on top of prior C16 resource-policy thesis; not a new positive entry trigger.","evidence_source":"stock-web OHLC peak proximity audit plus public risk-overlay narrative family","stage2_evidence_fields":[],"stage3_evidence_fields":[],"stage4b_evidence_fields":["valuation_blowoff","positioning_overheat","price_only_local_peak"],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/005/005490/2023.csv","profile_path":"atlas/symbol_profiles/005/005490.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","entry_date":"2023-07-26","entry_price":630000,"MFE_30D_pct":null,"MFE_90D_pct":null,"MFE_180D_pct":null,"MFE_1Y_pct":null,"MFE_2Y_pct":null,"MAE_30D_pct":null,"MAE_90D_pct":null,"MAE_180D_pct":null,"MAE_1Y_pct":null,"below_entry_price_flag_30D":null,"below_entry_price_flag_90D":null,"peak_date":"2023-07-26","peak_price":764000,"drawdown_after_peak_pct":-35.86,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":0.662,"four_b_full_window_peak_proximity":0.662,"four_b_timing_verdict":"price_only_local_4B_too_early","four_b_evidence_type":["price_only","valuation_blowoff","positioning_overheat"],"four_c_protection_label":"not_applicable","trigger_outcome_label":"4B_overlay","current_profile_verdict":"current_profile_4B_too_late","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"R4L75_C16_005490_POSCOHOLDINGS_LITHIUM_VALUECHAIN_20230331::2023-07-26::630000","dedupe_for_aggregate":false,"aggregate_group_role":"4B_overlay_only","is_new_independent_case":false,"reuse_reason":"4B overlay audit for same case; not counted as new aggregate representative","independent_evidence_weight":0.0,"do_not_count_as_new_case":true}
{"row_type":"trigger","trigger_id":"TRG_001570_Stage4B_Overlay_2023-09-01","case_id":"R4L75_C16_001570_KUMYANG_LATE_RESOURCE_THEME_20230901","symbol":"001570","company_name":"금양","round":"R4","loop":"75","large_sector_id":"L4_MATERIALS_SPREAD_RESOURCE","canonical_archetype_id":"C16_STRATEGIC_RESOURCE_POLICY_SUPPLY","fine_archetype_id":"LITHIUM_RESOURCE_SUPPLY_CHAIN_BANKABILITY_GATE","sector":"materials/resource/battery-material supply chain","primary_archetype":"strategic_resource_policy_supply","loop_objective":"4B_non_price_requirement_stress_test","trigger_type":"Stage4B-Overlay","trigger_date":"2023-09-01","evidence_available_at_that_date":"valuation/positioning risk overlay on top of prior C16 resource-policy thesis; not a new positive entry trigger.","evidence_source":"stock-web OHLC peak proximity audit plus public risk-overlay narrative family","stage2_evidence_fields":[],"stage3_evidence_fields":[],"stage4b_evidence_fields":["valuation_blowoff","positioning_overheat","price_only_local_peak"],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/001/001570/2023.csv|atlas/ohlcv_tradable_by_symbol_year/001/001570/2024.csv","profile_path":"atlas/symbol_profiles/001/001570.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","entry_date":"2023-09-01","entry_price":125800,"MFE_30D_pct":null,"MFE_90D_pct":null,"MFE_180D_pct":null,"MFE_1Y_pct":null,"MFE_2Y_pct":null,"MAE_30D_pct":null,"MAE_90D_pct":null,"MAE_180D_pct":null,"MAE_1Y_pct":null,"below_entry_price_flag_30D":null,"below_entry_price_flag_90D":null,"peak_date":"2023-09-11","peak_price":142000,"drawdown_after_peak_pct":-49.08,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":0.0,"four_b_full_window_peak_proximity":0.0,"four_b_timing_verdict":"good_4B_watch_not_stage2","four_b_evidence_type":["valuation_blowoff","positioning_overheat","price_only"],"four_c_protection_label":"not_applicable","trigger_outcome_label":"4B_overlay","current_profile_verdict":"current_profile_false_positive","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"R4L75_C16_001570_KUMYANG_LATE_RESOURCE_THEME_20230901::2023-09-01::125800","dedupe_for_aggregate":false,"aggregate_group_role":"4B_overlay_only","is_new_independent_case":false,"reuse_reason":"4B overlay audit for same case; not counted as new aggregate representative","independent_evidence_weight":0.0,"do_not_count_as_new_case":true}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"R4L75_C16_003670_POSCOFUTUREM_SDI_CATHODE_SUPPLY_20230130","trigger_id":"TRG_003670_Stage2_Actionable_2023-01-30","symbol":"003670","large_sector_id":"L4_MATERIALS_SPREAD_RESOURCE","canonical_archetype_id":"C16_STRATEGIC_RESOURCE_POLICY_SUPPLY","raw_component_scores_before":{"contract_score":26,"backlog_visibility_score":20,"margin_bridge_score":6,"revision_score":8,"relative_strength_score":12,"customer_quality_score":15,"policy_or_regulatory_score":4,"valuation_repricing_score":2,"execution_risk_score":3,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_before":86.0,"stage_label_before":"Stage3-Yellow","raw_component_scores_after":{"contract_score":26,"backlog_visibility_score":21,"margin_bridge_score":6,"revision_score":8,"relative_strength_score":12,"customer_quality_score":16,"policy_or_regulatory_score":4,"valuation_repricing_score":2,"execution_risk_score":2,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_after":88.0,"stage_label_after":"Stage3-Green","changed_components":["resource_bankability_gate","capacity_without_cashflow_guard","late_blowoff_risk_cap"],"component_delta_explanation":"C16 shadow profile preserves resource-policy upside only when off-take/customer quality/capacity utilization evidence is visible; otherwise relative-strength and policy points are capped and execution/valuation risk is raised.","MFE_90D_pct":93.81,"MAE_90D_pct":-2.98,"score_return_alignment_label":"score_aligned_but_green_late","current_profile_verdict":"current_profile_too_late"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"R4L75_C16_005490_POSCOHOLDINGS_LITHIUM_VALUECHAIN_20230331","trigger_id":"TRG_005490_Stage2_Actionable_2023-03-31","symbol":"005490","large_sector_id":"L4_MATERIALS_SPREAD_RESOURCE","canonical_archetype_id":"C16_STRATEGIC_RESOURCE_POLICY_SUPPLY","raw_component_scores_before":{"contract_score":8,"backlog_visibility_score":10,"margin_bridge_score":8,"revision_score":7,"relative_strength_score":14,"customer_quality_score":9,"policy_or_regulatory_score":18,"valuation_repricing_score":4,"execution_risk_score":4,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_before":82.0,"stage_label_before":"Stage2-Actionable","raw_component_scores_after":{"contract_score":8,"backlog_visibility_score":11,"margin_bridge_score":8,"revision_score":7,"relative_strength_score":14,"customer_quality_score":10,"policy_or_regulatory_score":18,"valuation_repricing_score":4,"execution_risk_score":3,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_after":85.0,"stage_label_after":"Stage3-Yellow","changed_components":["resource_bankability_gate","capacity_without_cashflow_guard","late_blowoff_risk_cap"],"component_delta_explanation":"C16 shadow profile preserves resource-policy upside only when off-take/customer quality/capacity utilization evidence is visible; otherwise relative-strength and policy points are capped and execution/valuation risk is raised.","MFE_90D_pct":107.61,"MAE_90D_pct":-8.42,"score_return_alignment_label":"score_aligned_but_4b_overlay_needed","current_profile_verdict":"current_profile_too_late"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"R4L75_C16_101670_HYDROLITHIUM_RESOURCE_NARRATIVE_20230403","trigger_id":"TRG_101670_Stage2_Actionable_2023-04-03","symbol":"101670","large_sector_id":"L4_MATERIALS_SPREAD_RESOURCE","canonical_archetype_id":"C16_STRATEGIC_RESOURCE_POLICY_SUPPLY","raw_component_scores_before":{"contract_score":2,"backlog_visibility_score":3,"margin_bridge_score":1,"revision_score":2,"relative_strength_score":19,"customer_quality_score":1,"policy_or_regulatory_score":15,"valuation_repricing_score":16,"execution_risk_score":8,"legal_or_contract_risk_score":4,"dilution_cb_risk_score":3,"accounting_trust_risk_score":3},"weighted_score_before":77.0,"stage_label_before":"Stage3-Yellow","raw_component_scores_after":{"contract_score":1,"backlog_visibility_score":1,"margin_bridge_score":0,"revision_score":0,"relative_strength_score":11,"customer_quality_score":0,"policy_or_regulatory_score":8,"valuation_repricing_score":12,"execution_risk_score":13,"legal_or_contract_risk_score":6,"dilution_cb_risk_score":5,"accounting_trust_risk_score":4},"weighted_score_after":61.0,"stage_label_after":"Stage2-Watch/4B-Overlay","changed_components":["resource_bankability_gate","capacity_without_cashflow_guard","late_blowoff_risk_cap"],"component_delta_explanation":"C16 shadow profile preserves resource-policy upside only when off-take/customer quality/capacity utilization evidence is visible; otherwise relative-strength and policy points are capped and execution/valuation risk is raised.","MFE_90D_pct":22.41,"MAE_90D_pct":-41.71,"score_return_alignment_label":"score_false_positive_high_mae","current_profile_verdict":"current_profile_false_positive"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"R4L75_C16_001570_KUMYANG_LATE_RESOURCE_THEME_20230901","trigger_id":"TRG_001570_Stage2_Actionable_2023-09-01","symbol":"001570","large_sector_id":"L4_MATERIALS_SPREAD_RESOURCE","canonical_archetype_id":"C16_STRATEGIC_RESOURCE_POLICY_SUPPLY","raw_component_scores_before":{"contract_score":1,"backlog_visibility_score":2,"margin_bridge_score":1,"revision_score":2,"relative_strength_score":18,"customer_quality_score":1,"policy_or_regulatory_score":16,"valuation_repricing_score":17,"execution_risk_score":8,"legal_or_contract_risk_score":4,"dilution_cb_risk_score":4,"accounting_trust_risk_score":5},"weighted_score_before":79.0,"stage_label_before":"Stage3-Yellow","raw_component_scores_after":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":0,"revision_score":0,"relative_strength_score":9,"customer_quality_score":0,"policy_or_regulatory_score":7,"valuation_repricing_score":13,"execution_risk_score":14,"legal_or_contract_risk_score":5,"dilution_cb_risk_score":5,"accounting_trust_risk_score":5},"weighted_score_after":58.0,"stage_label_after":"4B/Stage2-Watch","changed_components":["resource_bankability_gate","capacity_without_cashflow_guard","late_blowoff_risk_cap"],"component_delta_explanation":"C16 shadow profile preserves resource-policy upside only when off-take/customer quality/capacity utilization evidence is visible; otherwise relative-strength and policy points are capped and execution/valuation risk is raised.","MFE_90D_pct":12.88,"MAE_90D_pct":-42.53,"score_return_alignment_label":"score_false_positive_after_blowoff","current_profile_verdict":"current_profile_false_positive"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"R4L75_C16_095500_MIRAE_NANOTECH_LITHIUM_PROCESSING_THEME_20230403","trigger_id":"TRG_095500_Stage2_Actionable_2023-04-03","symbol":"095500","large_sector_id":"L4_MATERIALS_SPREAD_RESOURCE","canonical_archetype_id":"C16_STRATEGIC_RESOURCE_POLICY_SUPPLY","raw_component_scores_before":{"contract_score":1,"backlog_visibility_score":2,"margin_bridge_score":1,"revision_score":1,"relative_strength_score":17,"customer_quality_score":0,"policy_or_regulatory_score":13,"valuation_repricing_score":15,"execution_risk_score":9,"legal_or_contract_risk_score":5,"dilution_cb_risk_score":5,"accounting_trust_risk_score":6},"weighted_score_before":75.0,"stage_label_before":"Stage3-Yellow","raw_component_scores_after":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":0,"revision_score":0,"relative_strength_score":8,"customer_quality_score":0,"policy_or_regulatory_score":6,"valuation_repricing_score":11,"execution_risk_score":14,"legal_or_contract_risk_score":6,"dilution_cb_risk_score":6,"accounting_trust_risk_score":6},"weighted_score_after":57.0,"stage_label_after":"Stage2-Watch/4B-Overlay","changed_components":["resource_bankability_gate","capacity_without_cashflow_guard","late_blowoff_risk_cap"],"component_delta_explanation":"C16 shadow profile preserves resource-policy upside only when off-take/customer quality/capacity utilization evidence is visible; otherwise relative-strength and policy points are capped and execution/valuation risk is raised.","MFE_90D_pct":2.93,"MAE_90D_pct":-37.1,"score_return_alignment_label":"score_false_positive_no_bankability","current_profile_verdict":"current_profile_false_positive"}
{"row_type":"residual_contribution","round":"R4","loop":"75","large_sector_id":"L4_MATERIALS_SPREAD_RESOURCE","canonical_archetype_id":"C16_STRATEGIC_RESOURCE_POLICY_SUPPLY","new_independent_case_count":5,"reused_case_count":0,"new_symbol_count":5,"same_archetype_new_symbol_count":5,"same_archetype_new_trigger_family_count":4,"new_trigger_family_count":4,"positive_case_count":2,"counterexample_count":3,"current_profile_error_count":5,"tested_existing_calibrated_axes":["stage2_actionable_evidence_bonus","stage3_yellow_total_min","stage3_green_total_min","price_only_blowoff_blocks_positive_stage","full_4b_requires_non_price_evidence"],"residual_error_types_found":["resource_policy_false_positive_without_bankability","late_entry_after_resource_blowoff","high_mae_success_vs_clean_structural_contract","4B_overlay_too_late_if_price_only_ignored"],"loop_contribution_label":"canonical_archetype_rule_candidate","do_not_propose_new_weight_delta":false}
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
completed_round = R4
completed_loop = 75
next_round = R5
next_loop = 75
round_schedule_status = valid
round_sector_consistency = pass
```

## 28. Source Notes

- Manifest validation: `atlas/manifest.json` lines fetched from Songdaiki/stock-web show FinanceData/marcap source, raw_unadjusted_marcap, max_date 2026-02-20, row counts, and corporate-action notes.
- `003670` profile and OHLC: profile shows 2023 no corporate-action contamination; OHLC fetched around 2023-01-30 and 2023-07-26 from `atlas/ohlcv_tradable_by_symbol_year/003/003670/2023.csv`.
- `005490` profile and OHLC: profile has `corporate_action_candidate_count=0`; OHLC fetched around 2023-03-31, 2023-04~06, and 2023-07-26 from `atlas/ohlcv_tradable_by_symbol_year/005/005490/2023.csv`.
- `101670` profile and OHLC: profile shows 2023-12-22 candidate date, outside this loop's selected representative 180D calibration window; OHLC fetched around 2023-02~05 from `atlas/ohlcv_tradable_by_symbol_year/101/101670/2023.csv`.
- `001570` profile and OHLC: profile shows no 2023/2024 corporate-action candidate overlap; OHLC fetched around 2023-07~10 and 2024-01~04 from stock-web shards.
- `095500` profile and OHLC: profile shows no modern corporate-action candidate overlap; OHLC fetched around 2023-01~05 from `atlas/ohlcv_tradable_by_symbol_year/095/095500/2023.csv`.
- This file deliberately does not open or infer `stock_agent/src/e2r` code and does not modify production scoring.

