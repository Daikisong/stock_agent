# E2R Stock-Web Historical Calibration / Sector-Archetype Residual Research Round

## 0. Research Metadata

```text
research_session = post_calibrated_sector_archetype_residual_research
mode = historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12
repo_session = later_batch_implementation_only
output_file = e2r_stock_web_v12_residual_round_R4_loop_14_L4_MATERIALS_SPREAD_RESOURCE_C16_STRATEGIC_RESOURCE_POLICY_SUPPLY_research.md
scheduled_round = R4
scheduled_loop = 14
completed_round = R4
completed_loop = 14
large_sector_id = L4_MATERIALS_SPREAD_RESOURCE
canonical_archetype_id = C16_STRATEGIC_RESOURCE_POLICY_SUPPLY
fine_archetype_id = LITHIUM_NICKEL_GRAPHITE_RESOURCE_POLICY_SUPPLY_VERIFICATION_GUARD
price_source = Songdaiki/stock-web
price_basis = tradable_raw
price_adjustment_status = raw_unadjusted_marcap
stock_web_manifest_max_date = 2026-02-20
round_schedule_status = valid
round_sector_consistency = pass
production_scoring_changed = false
shadow_weight_only = true
handoff_prompt_embedded = true
handoff_prompt_executed_now = false
```

This loop adds **4** new independent cases, **3** counterexamples, and **3** residual errors for **R4/L4_MATERIALS_SPREAD_RESOURCE/C16_STRATEGIC_RESOURCE_POLICY_SUPPLY**.

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

This MD does not re-prove the already-applied Stage2 or price-only blowoff rules. It tests a narrower R4/C16 residual: **strategic-resource policy optionality is not the same as verified supply economics**. A lithium headline is a mine gate, not ore in the truck; calibration should distinguish the signboard from the loaded shipment.

## 2. Round / Large Sector / Canonical Archetype Scope

|Field|Value|
|---|---|
|scheduled_round|R4|
|scheduled_loop|14|
|large_sector_id|L4_MATERIALS_SPREAD_RESOURCE|
|canonical_archetype_id|C16_STRATEGIC_RESOURCE_POLICY_SUPPLY|
|fine_archetype_id|LITHIUM_NICKEL_GRAPHITE_RESOURCE_POLICY_SUPPLY_VERIFICATION_GUARD|
|loop_objective|coverage_gap_fill\|counterexample_mining\|residual_false_positive_mining\|canonical_archetype_compression\|4B_non_price_requirement_stress_test\|sector_specific_rule_discovery|
|rule_scope_target|canonical_archetype_specific|
|production_change|false|

## 3. Previous Coverage / Duplicate Avoidance Check

Local v12 registry scan found R4 loop 10-12 concentrated in `C17_CHEMICAL_COMMODITY_MARGIN_SPREAD`, and R4 loop 13 in `C15_MATERIAL_SPREAD_SUPERCYCLE`. No existing R4/C16 file was found in the local result set. POSCO Holdings appeared in prior C15 steel-spread coverage, but the 2023 trigger here is a different resource-policy / lithium-supply trigger family and is treated as a new C16 independent case. STX was considered but rejected for quantitative calibration because its profile carries corporate-action candidates inside the likely 180D resource-theme window.

## 4. Stock-Web OHLC Input / Price Source Validation

```text
price_atlas_repo = https://github.com/Songdaiki/stock-web
manifest = atlas/manifest.json
schema = atlas/schema.json
universe = atlas/universe/all_symbols.csv
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
calibration_shard_root = atlas/ohlcv_tradable_by_symbol_year
raw_shard_root = atlas/ohlcv_raw_by_symbol_year
```

Stock-Web schema uses `d,o,h,l,c,v,a,mc,s,m` for tradable shards. The calibration rows below use `tradable_raw`, not adjusted prices. Corporate-action windows are blocked when the symbol profile marks overlap; this is why STX is kept as narrative-only.

## 5. Historical Eligibility Gate

|symbol|profile path|profile status|180D window status|calibration usable|
|---:|---|---|---|---|
|005490|atlas/symbol_profiles/005/005490.json|corporate_action_candidate_count=0|clean|true|
|001570|atlas/symbol_profiles/001/001570.json|corporate-action candidates are old and outside 2023 window|clean|true|
|009520|atlas/symbol_profiles/009/009520.json|corporate-action candidates are old and outside 2023 window|clean|true|
|010130|atlas/symbol_profiles/010/010130.json|corporate_action_candidate_count=0|clean|true|
|011810|atlas/symbol_profiles/011/011810.json|corporate-action candidates include 2023-09-15 and 2024-01-05|blocked|false / narrative_only|

## 6. Canonical Archetype Compression Map

`C16_STRATEGIC_RESOURCE_POLICY_SUPPLY` is compressed into one C16 scoring family:

```text
resource_policy_headline
→ resource ownership / permit / offtake / eligible capacity
→ utilization and margin bridge
→ revision visibility
→ Stage3-Green-shadow only if conversion is visible
```

Fine archetypes covered in this loop:

```text
LITHIUM_RESOURCE_VALUE_CHAIN_RERATING_WITH_REAL_ASSET_BASE
LITHIUM_RESOURCE_OPTIONALITY_WITHOUT_VERIFIED_ECONOMICS
RESOURCE_PROXY_AFFILIATE_BETA_WITHOUT_DIRECT_RESOURCE_ECONOMICS
BATTERY_METALS_RECYCLING_JV_OPTIONALITY_WITHOUT_NEAR_TERM_REVISION
```

## 7. Case Selection Summary

|case_id|symbol|trigger|entry|entry_price|MFE90|MAE90|MFE180|MAE180|outcome|current profile|
|---|---:|---|---|---:|---:|---:|---:|---:|---|---|
|R4L14_C16_POSCOHOLD_20230712_LITHIUM_RESOURCE_RERATING|005490|2023-07-12|2023-07-12|417,500|83.0|-6.71|83.0|-8.86|structural_success_then_4B_required|current_profile_correct|
|R4L14_C16_KUMYANG_20230726_LITHIUM_OPTIONALITY_BLOWOFF|001570|2023-07-26|2023-07-26|152,200|27.46|-45.47|27.46|-52.5|failed_rerating_high_MAE|current_profile_false_positive|
|R4L14_C16_POSCOMTECH_20230726_RESOURCE_PROXY_BLOWOFF|009520|2023-07-26|2023-07-26|39,150|20.05|-46.23|20.05|-48.94|failed_resource_proxy_rerating|current_profile_false_positive|
|R4L14_C16_KOREAZINC_20220915_BATTERY_METALS_JV_FALSE_START|010130|2022-09-15|2022-09-15|634,000|8.04|-20.35|8.04|-21.61|stage2_watch_failed_rerating|current_profile_too_early|


## 8. Positive vs Counterexample Balance

```text
positive_case_count = 1
counterexample_count = 3
calibration_usable_case_count = 4
new_independent_case_count = 4
reused_case_count = 0
new_independent_case_ratio = 1.00
```

The positive row is not a blanket endorsement of resource headlines. POSCO Holdings worked because the resource story was attached to an operating-cash-flow base and a broader value-chain strategy. The three counterexamples show the other side of the same object: option value, affiliate beta, or JV language can shine like ore, but if it is not milled into margin and revision, it behaves like a theme candle.

## 9. Evidence Source Map

|case|Stage2 evidence|Stage3 evidence|4B/4C evidence|
|---|---|---|---|
|POSCO Holdings 2023|resource policy optionality, relative strength, value-chain visibility|partial financial visibility and multiple public sources|July blowoff / positioning overheat|
|Kumyang 2023|resource narrative, policy optionality, relative strength|missing verified economics and revision|price-only blowoff, later thesis-break watch|
|POSCO M-Tech 2023|resource proxy beta, relative strength|missing direct resource economics|proxy blowoff, later drawdown|
|Korea Zinc 2022|battery-metal/recycling optionality|missing near-term revision bridge|local strength faded into failed rerating|

## 10. Price Data Source Map

|symbol|entry shard|entry date|entry close|profile|
|---:|---|---|---:|---|
|005490|atlas/ohlcv_tradable_by_symbol_year/005/005490/2023.csv|2023-07-12|417,500|atlas/symbol_profiles/005/005490.json|
|001570|atlas/ohlcv_tradable_by_symbol_year/001/001570/2023.csv|2023-07-26|152,200|atlas/symbol_profiles/001/001570.json|
|009520|atlas/ohlcv_tradable_by_symbol_year/009/009520/2023.csv|2023-07-26|39,150|atlas/symbol_profiles/009/009520.json|
|010130|atlas/ohlcv_tradable_by_symbol_year/010/010130/2022.csv|2022-09-15|634,000|atlas/symbol_profiles/010/010130.json|

## 11. Case-by-Case Trigger Grid

### POSCO Holdings — structural success with 4B overlay need

The Stage2 resource/value-chain signal on 2023-07-12 caught a real rerating path, but the late-July acceleration exhausted a large part of the cycle. The correct shadow interpretation is **Stage2/Yellow allowed, Green only after verified resource economics / utilization / margin bridge**.

### Kumyang — lithium optionality false-positive guard

The stock displayed enormous same-day upside, but from the trigger close the forward path had high downside. This is the archetypal C16 false-positive: resource optionality became a stock-market furnace before ore economics were visible.

### POSCO M-Tech — affiliate/proxy resource beta guard

The stock inherited POSCO lithium enthusiasm but did not carry direct resource economics. C16 needs a proxy discount: a child-company halo should not inherit the parent-resource score without direct conversion evidence.

### Korea Zinc — real industrial base, but no immediate revision bridge

This is not a low-quality company counterexample; it is a timing counterexample. Battery-metal/recycling optionality was plausible, but the Stage2 signal lacked near-term revision bridge and failed to produce a compelling 90D/180D MFE/MAE profile.

## 12. Trigger-Level OHLC Backtest Tables

|case_id|symbol|trigger|entry|entry_price|MFE90|MAE90|MFE180|MAE180|outcome|current profile|
|---|---:|---|---|---:|---:|---:|---:|---:|---|---|
|R4L14_C16_POSCOHOLD_20230712_LITHIUM_RESOURCE_RERATING|005490|2023-07-12|2023-07-12|417,500|83.0|-6.71|83.0|-8.86|structural_success_then_4B_required|current_profile_correct|
|R4L14_C16_KUMYANG_20230726_LITHIUM_OPTIONALITY_BLOWOFF|001570|2023-07-26|2023-07-26|152,200|27.46|-45.47|27.46|-52.5|failed_rerating_high_MAE|current_profile_false_positive|
|R4L14_C16_POSCOMTECH_20230726_RESOURCE_PROXY_BLOWOFF|009520|2023-07-26|2023-07-26|39,150|20.05|-46.23|20.05|-48.94|failed_resource_proxy_rerating|current_profile_false_positive|
|R4L14_C16_KOREAZINC_20220915_BATTERY_METALS_JV_FALSE_START|010130|2022-09-15|2022-09-15|634,000|8.04|-20.35|8.04|-21.61|stage2_watch_failed_rerating|current_profile_too_early|


## 13. Current Calibrated Profile Stress Test

|question|answer|
|---|---|
|How would current profile judge the cases?|It would mostly accept strategic-resource and policy optionality as Stage2/Yellow when relative strength is strong.|
|Was that aligned with MFE/MAE?|Aligned for POSCO Holdings; too early or false positive for Kumyang, POSCO M-Tech, and Korea Zinc.|
|Was Stage2 bonus too high?|Not globally. It was too permissive for C16 rows lacking resource-economics conversion.|
|Was Yellow 75 too low/high?|For C16 proxy/resource optionality, 75 is too reachable unless policy score is capped.|
|Was Green 87 / revision 55 too strict?|Not too strict. C16 should keep revision/margin bridge strictness.|
|Was price-only blowoff guard appropriate?|Yes; this loop strengthens it for resource optionality.|
|Was full 4B non-price requirement appropriate?|Yes. Price-only rows are de-risk overlays unless paired with non-price deterioration.|
|Was 4C routing late or excessive?|Hard 4C is useful for Kumyang / POSCO M-Tech only after resource-economics or proxy thesis breaks, not merely on volatility.|

Current profile verdict counts:

```text
current_profile_correct = 1
current_profile_false_positive = 2
current_profile_too_early = 1
current_profile_error_count = 3
```

## 14. Stage2 / Yellow / Green Comparison

The Stage2 label remains useful for real resource optionality, but C16 should treat Green as a tollgate. The car must show cargo: reserve/economics, permitting/ownership, offtake, utilization, margin bridge, or confirmed revision. Without that cargo, relative strength is just an engine revving in neutral.

```text
POSCO Holdings: Stage2/Yellow worked; Green at late-July price peak would be late/high-risk.
Kumyang: Stage2 may be watch-only; Yellow/Green would be false positive.
POSCO M-Tech: resource-proxy beta should not become Yellow/Green.
Korea Zinc: Stage2 watch was reasonable; Yellow/Green was too early.
```

## 15. 4B Local vs Full-window Timing Audit

|case|4B local proximity|4B full-window proximity|verdict|
|---|---:|---:|---|
|POSCO Holdings|1.00|1.00|late-July blowoff was good 4B overlay timing|
|Kumyang|1.00|1.00|full-window counterexample 4B at trigger/peak|
|POSCO M-Tech|1.00|1.00|proxy blowoff 4B at same-day peak|
|Korea Zinc|0.39|1.00|local strength not enough for full 4B without non-price evidence|

## 16. 4C Protection Audit

The loop supports `hard_4c_thesis_break_routes_to_4c`, but only when the thesis break is evidence-based. In resource-policy names, price drawdown alone can be noisy; the 4C route should look for broken permit/resource economics, failed offtake, financing stress, utilization delays, or verified revision deterioration.

## 17. Sector-Specific Rule Candidate

```text
sector_specific_rule_candidate = false
reason = this loop is C16 canonical-specific; sector-level L4 rule needs more C15/C16/C17 combined holdout rows.
```

## 18. Canonical-Archetype Rule Candidate

```text
canonical_archetype_rule_candidate = true
rule_scope = canonical_archetype_specific
axis_1 = C16_RESOURCE_SUPPLY_VERIFICATION_GATE
axis_2 = C16_RESOURCE_PROXY_DISCOUNT
axis_3 = C16_RESOURCE_OPTIONALITY_BLOWOFF_CAP
```

Rule candidate:

```text
If canonical_archetype_id == C16_STRATEGIC_RESOURCE_POLICY_SUPPLY:
    cap positive stage at Stage2-Watch or Stage2-Actionable unless at least two conversion fields are present:
        - resource ownership / permit / reserve economics
        - customer offtake or volume route
        - eligible capacity / utilization ramp
        - margin bridge or confirmed revision
        - balance-sheet endurance for long lead-time capex
    If evidence is mostly price + policy headline + affiliate proxy beta:
        block Stage3-Green
        add resource_proxy_discount
        allow 4B overlay if valuation/positioning overheat is visible
```

## 19. Before / After Backtest Comparison

|profile_id|eligible triggers|avg MFE90|avg MAE90|avg MFE180|avg MAE180|false positive rate|missed structural|late Green|score-return alignment|
|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
|P0 e2r_2_1_stock_web_calibrated_proxy|4|34.64|-29.69|34.64|-32.98|0.75|0|1|mixed; resource optionality over-scores three rows|
|P0b e2r_2_0_baseline_reference|4|34.64|-29.69|34.64|-32.98|0.75|1|1|too blunt; misses distinction between POSCO and proxy names|
|P1 L4 sector candidate profile|4|34.64|-29.69|34.64|-32.98|0.50|0|1|not enough sector breadth; no sector rule proposed|
|P2 C16 strategic resource shadow profile|4|34.64|-29.69|34.64|-32.98|0.25|0|1|best alignment; blocks proxy and optionality false positives|
|P3 C16 counterexample guard profile|3|18.55|-37.35|18.55|-41.02|0.00|0|not_applicable|best for counterexample suppression, but too conservative for POSCO|

## 20. Score-Return Alignment Matrix

|case|P0 label|P2 C16 shadow label|return alignment verdict|
|---|---|---|---|
|POSCO Holdings|Stage3-Yellow|Stage3-Yellow / Green-shadow watch|aligned; positive but 4B needed|
|Kumyang|Stage2/false-Yellow risk|Stage1/Watch|improved; blocks false positive|
|POSCO M-Tech|Stage2/false-Yellow risk|Stage1/Watch|improved; blocks proxy halo|
|Korea Zinc|Stage2-Actionable|Stage2-Watch|improved; prevents premature Yellow/Green|

## 21. Coverage Matrix

|large_sector_id|canonical_archetype_id|fine_archetype_id|positive_case_count|counterexample_count|4B_case_count|4C_case_count|new_independent_case_count|reused_case_count|calibration_usable_trigger_count|representative_trigger_count|current_profile_error_count|sector_rule_candidate|canonical_rule_candidate|coverage_gap_after_this_loop|
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|---|---|
|L4_MATERIALS_SPREAD_RESOURCE|C16_STRATEGIC_RESOURCE_POLICY_SUPPLY|LITHIUM_NICKEL_GRAPHITE_RESOURCE_POLICY_SUPPLY_VERIFICATION_GUARD|1|3|3|2|4|0|4|4|3|false|true|C16 now has initial positive/counterexample coverage; still needs non-Korea holdout and more true-positive resource-utilization rows.|


## 22. Residual Contribution Summary

```text
new_independent_case_count: 4
reused_case_count: 0
reused_case_ids: []
new_symbol_count: 4
new_canonical_archetype_count: 1
new_fine_archetype_count: 4
new_trigger_family_count: 4
tested_existing_calibrated_axes:
  - stage2_actionable_evidence_bonus
  - stage3_green_revision_min
  - full_4b_requires_non_price_evidence
  - price_only_blowoff_blocks_positive_stage
  - hard_4c_thesis_break_routes_to_4c
residual_error_types_found:
  - resource_policy_false_positive
  - proxy_resource_beta_false_green
  - resource_optional_blowoff_high_MAE
  - JV_optionality_without_revision
new_axis_proposed:
  - C16_RESOURCE_SUPPLY_VERIFICATION_GATE
  - C16_RESOURCE_PROXY_DISCOUNT
existing_axis_strengthened:
  - price_only_blowoff_blocks_positive_stage
  - full_4b_requires_non_price_evidence
  - stage3_green_revision_min
existing_axis_weakened: null
existing_axis_kept:
  - stage2_actionable_evidence_bonus
  - hard_4c_thesis_break_routes_to_4c
sector_specific_rule_candidate: false
canonical_archetype_rule_candidate: true
no_new_signal_reason: null
loop_contribution_label: canonical_archetype_rule_candidate
do_not_propose_new_weight_delta: false
```

## 23. Validation Scope / Non-Validation Scope

Validated:

```text
- historical trigger-level OHLC using Songdaiki/stock-web tradable shards
- 30D / 90D / 180D MFE/MAE primary calibration windows
- corporate-action profile gate for selected cases
- C16-specific score-return alignment stress test
- positive/counterexample balance
```

Not validated:

```text
- live 2026 candidates
- investment recommendations
- production scoring changes
- exact intraday disclosure timing
- brokerage/API integration
- stock_agent source code behavior
```

## 24. Shadow Weight Calibration

```csv
row_type,axis,scope,large_sector_id,canonical_archetype_id,baseline_value,tested_value,delta,reason,backtest_effect,trigger_ids,calibration_usable_count,new_independent_case_count,counterexample_count,confidence,proposal_type,notes
shadow_weight,C16_RESOURCE_SUPPLY_VERIFICATION_GATE,canonical_archetype_specific,L4_MATERIALS_SPREAD_RESOURCE,C16_STRATEGIC_RESOURCE_POLICY_SUPPLY,0,1,+1,"Require verified resource economics / ownership-permitting / utilization / margin bridge before Green.","Reduces 3 false-positive Yellow/Green resource-optionality rows while preserving POSCO Holdings as Stage2/Yellow positive.","R4L14_C16_T01_POSCOHOLD_20230712_S2A|R4L14_C16_T02_KUMYANG_20230726_FALSE_GREEN|R4L14_C16_T03_POSCOMTECH_20230726_FALSE_GREEN|R4L14_C16_T04_KOREAZINC_20220915_STAGE2_FALSE_START",4,4,3,medium,canonical_shadow_only,"not production; post-calibrated residual"
shadow_weight,C16_RESOURCE_PROXY_DISCOUNT,canonical_archetype_specific,L4_MATERIALS_SPREAD_RESOURCE,C16_STRATEGIC_RESOURCE_POLICY_SUPPLY,0,1,+1,"Affiliate/proxy names cannot inherit parent strategic-resource score without direct economics.","Blocks POSCO M-Tech style proxy blowoff from false Green promotion.","R4L14_C16_T03_POSCOMTECH_20230726_FALSE_GREEN",1,1,1,medium,canonical_shadow_only,"not production; proxy guard"
```

## 25. Machine-Readable Rows

```jsonl
{"row_type": "price_source_validation", "source": "Songdaiki/stock-web", "source_url": "https://github.com/Songdaiki/stock-web", "manifest_path": "atlas/manifest.json", "schema_path": "atlas/schema.json", "universe_path": "atlas/universe/all_symbols.csv", "manifest_max_date": "2026-02-20", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "raw_shard_root": "atlas/ohlcv_raw_by_symbol_year", "validation_status": "usable_for_historical_calibration"}
{"row_type": "case", "case_id": "R4L14_C16_POSCOHOLD_20230712_LITHIUM_RESOURCE_RERATING", "symbol": "005490", "company_name": "POSCO홀딩스", "round": "R4", "loop": "14", "large_sector_id": "L4_MATERIALS_SPREAD_RESOURCE", "canonical_archetype_id": "C16_STRATEGIC_RESOURCE_POLICY_SUPPLY", "fine_archetype_id": "LITHIUM_RESOURCE_VALUE_CHAIN_RERATING_WITH_REAL_ASSET_BASE", "case_type": "structural_success", "positive_or_counterexample": "positive", "best_trigger": "R4L14_C16_T01_POSCOHOLD_20230712_S2A", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "structural_success_then_4B_required", "current_profile_verdict": "current_profile_correct", "price_source": "Songdaiki/stock-web", "notes": "Positive: strategic-resource optionality worked only because resource route was attached to a larger balance-sheet and operating-cash-flow base. Green should still wait for resource economics / margin conversion."}
{"row_type": "case", "case_id": "R4L14_C16_KUMYANG_20230726_LITHIUM_OPTIONALITY_BLOWOFF", "symbol": "001570", "company_name": "금양", "round": "R4", "loop": "14", "large_sector_id": "L4_MATERIALS_SPREAD_RESOURCE", "canonical_archetype_id": "C16_STRATEGIC_RESOURCE_POLICY_SUPPLY", "fine_archetype_id": "LITHIUM_RESOURCE_OPTIONALITY_WITHOUT_VERIFIED_ECONOMICS", "case_type": "false_positive_green", "positive_or_counterexample": "counterexample", "best_trigger": "R4L14_C16_T02_KUMYANG_20230726_FALSE_GREEN", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "failed_rerating_high_MAE", "current_profile_verdict": "current_profile_false_positive", "price_source": "Songdaiki/stock-web", "notes": "Counterexample: strategic-resource label had high MFE only because entry included a same-day blowoff high; subsequent MAE dominated the calibration signal."}
{"row_type": "case", "case_id": "R4L14_C16_POSCOMTECH_20230726_RESOURCE_PROXY_BLOWOFF", "symbol": "009520", "company_name": "포스코엠텍", "round": "R4", "loop": "14", "large_sector_id": "L4_MATERIALS_SPREAD_RESOURCE", "canonical_archetype_id": "C16_STRATEGIC_RESOURCE_POLICY_SUPPLY", "fine_archetype_id": "RESOURCE_PROXY_AFFILIATE_BETA_WITHOUT_DIRECT_RESOURCE_ECONOMICS", "case_type": "false_positive_green", "positive_or_counterexample": "counterexample", "best_trigger": "R4L14_C16_T03_POSCOMTECH_20230726_FALSE_GREEN", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "failed_resource_proxy_rerating", "current_profile_verdict": "current_profile_false_positive", "price_source": "Songdaiki/stock-web", "notes": "Counterexample: affiliate/proxy beta should not inherit the parent company resource score unless direct economics are visible."}
{"row_type": "case", "case_id": "R4L14_C16_KOREAZINC_20220915_BATTERY_METALS_JV_FALSE_START", "symbol": "010130", "company_name": "고려아연", "round": "R4", "loop": "14", "large_sector_id": "L4_MATERIALS_SPREAD_RESOURCE", "canonical_archetype_id": "C16_STRATEGIC_RESOURCE_POLICY_SUPPLY", "fine_archetype_id": "BATTERY_METALS_RECYCLING_JV_OPTIONALITY_WITHOUT_NEAR_TERM_REVISION", "case_type": "failed_rerating", "positive_or_counterexample": "counterexample", "best_trigger": "R4L14_C16_T04_KOREAZINC_20220915_STAGE2_FALSE_START", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "stage2_watch_failed_rerating", "current_profile_verdict": "current_profile_too_early", "price_source": "Songdaiki/stock-web", "notes": "Counterexample: real industrial capability can still fail as a rerating trigger if the resource route does not convert into near-term revision."}
{"row_type": "trigger", "trigger_id": "R4L14_C16_T01_POSCOHOLD_20230712_S2A", "case_id": "R4L14_C16_POSCOHOLD_20230712_LITHIUM_RESOURCE_RERATING", "symbol": "005490", "company_name": "POSCO홀딩스", "round": "R4", "loop": "14", "large_sector_id": "L4_MATERIALS_SPREAD_RESOURCE", "canonical_archetype_id": "C16_STRATEGIC_RESOURCE_POLICY_SUPPLY", "fine_archetype_id": "LITHIUM_RESOURCE_VALUE_CHAIN_RERATING_WITH_REAL_ASSET_BASE", "sector": "steel_holding_company_battery_material_resource", "primary_archetype": "strategic_resource_supply_verification", "loop_objective": "coverage_gap_fill|counterexample_mining|residual_false_positive_mining|canonical_archetype_compression|4B_non_price_requirement_stress_test|sector_specific_rule_discovery", "trigger_type": "Stage2-Actionable", "trigger_date": "2023-07-12", "evidence_available_at_that_date": "Argentina lithium / cathode-material value-chain optionality became market-visible and was attached to a large operating asset base. The evidence was not only price: the group had a steel cash-flow base, resource development route, and battery-material strategy, but the later July move still required 4B de-risking.", "evidence_source": "public company/resource strategy and market disclosures; stock-web OHLC row 2023-07-12 close 417500, 2023-07-26 high 764000, 2024-04-08 low 380500.", "stage2_evidence_fields": ["public_event_or_disclosure", "policy_or_regulatory_optionality", "capacity_or_volume_route", "relative_strength"], "stage3_evidence_fields": ["financial_visibility", "multiple_public_sources", "margin_bridge"], "stage4b_evidence_fields": ["valuation_blowoff", "positioning_overheat", "price_only_local_peak"], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/005/005490/2023.csv", "profile_path": "atlas/symbol_profiles/005/005490.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "entry_date": "2023-07-12", "entry_price": 417500, "MFE_30D_pct": 83.0, "MFE_90D_pct": 83.0, "MFE_180D_pct": 83.0, "MFE_1Y_pct": 83.0, "MFE_2Y_pct": 83.0, "MAE_30D_pct": -6.71, "MAE_90D_pct": -6.71, "MAE_180D_pct": -8.86, "MAE_1Y_pct": -26.9, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2023-07-26", "peak_price": 764000, "drawdown_after_peak_pct": -50.2, "green_lateness_ratio": 0.65, "four_b_local_peak_proximity": 1.0, "four_b_full_window_peak_proximity": 1.0, "four_b_timing_verdict": "good_full_window_4B_timing_after_resource_optional_blowoff", "four_b_evidence_type": ["valuation_blowoff", "positioning_overheat", "price_only"], "four_c_protection_label": "thesis_break_watch_only", "trigger_outcome_label": "structural_success_then_4B_required", "current_profile_verdict": "current_profile_correct", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window_profile_candidate_count_0", "same_entry_group_id": "R4L14_C16_POSCOHOLD_20230712_LITHIUM_RESOURCE_RERATING__2023-07-12__417500", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false}
{"row_type": "trigger", "trigger_id": "R4L14_C16_T02_KUMYANG_20230726_FALSE_GREEN", "case_id": "R4L14_C16_KUMYANG_20230726_LITHIUM_OPTIONALITY_BLOWOFF", "symbol": "001570", "company_name": "금양", "round": "R4", "loop": "14", "large_sector_id": "L4_MATERIALS_SPREAD_RESOURCE", "canonical_archetype_id": "C16_STRATEGIC_RESOURCE_POLICY_SUPPLY", "fine_archetype_id": "LITHIUM_RESOURCE_OPTIONALITY_WITHOUT_VERIFIED_ECONOMICS", "sector": "battery_resource_optional_theme", "primary_archetype": "strategic_resource_policy_supply_false_positive", "loop_objective": "coverage_gap_fill|counterexample_mining|residual_false_positive_mining|canonical_archetype_compression|4B_non_price_requirement_stress_test|sector_specific_rule_discovery", "trigger_type": "Stage2-Actionable / false-Green stress", "trigger_date": "2023-07-26", "evidence_available_at_that_date": "Lithium/resource optionality and battery-material narrative were visible, but the trigger lacked verified reserve economics, offtake-backed cash-flow conversion, and near-term margin bridge. Price action itself supplied most of the score.", "evidence_source": "public resource optionality narrative; stock-web OHLC row 2023-07-26 close 152200, same-day high 194000, 2024-01-26 low 72300.", "stage2_evidence_fields": ["public_event_or_disclosure", "policy_or_regulatory_optionality", "relative_strength"], "stage3_evidence_fields": [], "stage4b_evidence_fields": ["valuation_blowoff", "positioning_overheat", "price_only_local_peak"], "stage4c_evidence_fields": ["thesis_evidence_broken"], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/001/001570/2023.csv", "profile_path": "atlas/symbol_profiles/001/001570.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "entry_date": "2023-07-26", "entry_price": 152200, "MFE_30D_pct": 27.46, "MFE_90D_pct": 27.46, "MFE_180D_pct": 27.46, "MFE_1Y_pct": 27.46, "MFE_2Y_pct": null, "MAE_30D_pct": -30.75, "MAE_90D_pct": -45.47, "MAE_180D_pct": -52.5, "MAE_1Y_pct": -60.0, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2023-07-26", "peak_price": 194000, "drawdown_after_peak_pct": -62.73, "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": 1.0, "four_b_full_window_peak_proximity": 1.0, "four_b_timing_verdict": "good_full_window_4B_timing_for_counterexample", "four_b_evidence_type": ["valuation_blowoff", "positioning_overheat", "price_only"], "four_c_protection_label": "hard_4c_success_if_resource_economics_guard_used", "trigger_outcome_label": "failed_rerating_high_MAE", "current_profile_verdict": "current_profile_false_positive", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window_old_corporate_action_candidates_do_not_overlap", "same_entry_group_id": "R4L14_C16_KUMYANG_20230726_LITHIUM_OPTIONALITY_BLOWOFF__2023-07-26__152200", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false}
{"row_type": "trigger", "trigger_id": "R4L14_C16_T03_POSCOMTECH_20230726_FALSE_GREEN", "case_id": "R4L14_C16_POSCOMTECH_20230726_RESOURCE_PROXY_BLOWOFF", "symbol": "009520", "company_name": "포스코엠텍", "round": "R4", "loop": "14", "large_sector_id": "L4_MATERIALS_SPREAD_RESOURCE", "canonical_archetype_id": "C16_STRATEGIC_RESOURCE_POLICY_SUPPLY", "fine_archetype_id": "RESOURCE_PROXY_AFFILIATE_BETA_WITHOUT_DIRECT_RESOURCE_ECONOMICS", "sector": "resource_proxy_affiliate", "primary_archetype": "strategic_resource_policy_supply_proxy_false_positive", "loop_objective": "coverage_gap_fill|counterexample_mining|residual_false_positive_mining|canonical_archetype_compression|4B_non_price_requirement_stress_test|sector_specific_rule_discovery", "trigger_type": "Stage2-Actionable / false-Green stress", "trigger_date": "2023-07-26", "evidence_available_at_that_date": "The stock traded as a POSCO lithium/resource proxy, but direct resource ownership, customer offtake, margin bridge, and revision evidence were much weaker than the parent-resource narrative.", "evidence_source": "resource-proxy market narrative; stock-web OHLC row 2023-07-26 close 39150, same-day high 47000, 2024-04-08 low 19990.", "stage2_evidence_fields": ["relative_strength", "policy_or_regulatory_optionality"], "stage3_evidence_fields": [], "stage4b_evidence_fields": ["valuation_blowoff", "positioning_overheat", "price_only_local_peak"], "stage4c_evidence_fields": ["thesis_evidence_broken"], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/009/009520/2023.csv", "profile_path": "atlas/symbol_profiles/009/009520.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "entry_date": "2023-07-26", "entry_price": 39150, "MFE_30D_pct": 20.05, "MFE_90D_pct": 20.05, "MFE_180D_pct": 20.05, "MFE_1Y_pct": 20.05, "MFE_2Y_pct": null, "MAE_30D_pct": -34.36, "MAE_90D_pct": -46.23, "MAE_180D_pct": -48.94, "MAE_1Y_pct": -55.0, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2023-07-26", "peak_price": 47000, "drawdown_after_peak_pct": -57.47, "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": 1.0, "four_b_full_window_peak_proximity": 1.0, "four_b_timing_verdict": "good_full_window_4B_timing_for_counterexample", "four_b_evidence_type": ["price_only", "positioning_overheat", "valuation_blowoff"], "four_c_protection_label": "hard_4c_success_if_proxy_discount_guard_used", "trigger_outcome_label": "failed_resource_proxy_rerating", "current_profile_verdict": "current_profile_false_positive", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window_old_corporate_action_candidates_do_not_overlap", "same_entry_group_id": "R4L14_C16_POSCOMTECH_20230726_RESOURCE_PROXY_BLOWOFF__2023-07-26__39150", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false}
{"row_type": "trigger", "trigger_id": "R4L14_C16_T04_KOREAZINC_20220915_STAGE2_FALSE_START", "case_id": "R4L14_C16_KOREAZINC_20220915_BATTERY_METALS_JV_FALSE_START", "symbol": "010130", "company_name": "고려아연", "round": "R4", "loop": "14", "large_sector_id": "L4_MATERIALS_SPREAD_RESOURCE", "canonical_archetype_id": "C16_STRATEGIC_RESOURCE_POLICY_SUPPLY", "fine_archetype_id": "BATTERY_METALS_RECYCLING_JV_OPTIONALITY_WITHOUT_NEAR_TERM_REVISION", "sector": "nonferrous_metals_recycling_battery_materials", "primary_archetype": "strategic_resource_policy_supply_jv_optional_false_start", "loop_objective": "coverage_gap_fill|counterexample_mining|residual_false_positive_mining|canonical_archetype_compression|4B_non_price_requirement_stress_test|sector_specific_rule_discovery", "trigger_type": "Stage2-Actionable", "trigger_date": "2022-09-15", "evidence_available_at_that_date": "Battery-metal / recycling / precursor optionality was visible, but the trigger did not yet show a near-term earnings revision, contracted volume bridge, or resource-to-margin conversion. It was legitimate Stage2 watch evidence, not Green.", "evidence_source": "public battery-metal/recycling/JV optionality; stock-web OHLC row 2022-09-15 close 634000, 2022-11-23 high 685000, 2023-01-05 low 505000.", "stage2_evidence_fields": ["public_event_or_disclosure", "policy_or_regulatory_optionality", "capacity_or_volume_route"], "stage3_evidence_fields": [], "stage4b_evidence_fields": ["price_only_local_peak", "positioning_overheat"], "stage4c_evidence_fields": ["thesis_evidence_broken"], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/010/010130/2022.csv", "profile_path": "atlas/symbol_profiles/010/010130.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "entry_date": "2022-09-15", "entry_price": 634000, "MFE_30D_pct": 2.05, "MFE_90D_pct": 8.04, "MFE_180D_pct": 8.04, "MFE_1Y_pct": 8.04, "MFE_2Y_pct": null, "MAE_30D_pct": -11.2, "MAE_90D_pct": -20.35, "MAE_180D_pct": -21.61, "MAE_1Y_pct": -21.61, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2022-11-23", "peak_price": 685000, "drawdown_after_peak_pct": -26.28, "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": 0.39, "four_b_full_window_peak_proximity": 1.0, "four_b_timing_verdict": "local_strength_not_full_4B_without_non_price_evidence", "four_b_evidence_type": ["price_only", "positioning_overheat"], "four_c_protection_label": "thesis_break_watch_only", "trigger_outcome_label": "stage2_watch_failed_rerating", "current_profile_verdict": "current_profile_too_early", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window_profile_candidate_count_0", "same_entry_group_id": "R4L14_C16_KOREAZINC_20220915_BATTERY_METALS_JV_FALSE_START__2022-09-15__634000", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R4L14_C16_POSCOHOLD_20230712_LITHIUM_RESOURCE_RERATING", "trigger_id": "R4L14_C16_T01_POSCOHOLD_20230712_S2A", "symbol": "005490", "large_sector_id": "L4_MATERIALS_SPREAD_RESOURCE", "canonical_archetype_id": "C16_STRATEGIC_RESOURCE_POLICY_SUPPLY", "raw_component_scores_before": {"contract_score": 2, "backlog_visibility_score": 4, "margin_bridge_score": 11, "revision_score": 12, "relative_strength_score": 14, "customer_quality_score": 2, "policy_or_regulatory_score": 16, "valuation_repricing_score": 14, "execution_risk_score": 4, "legal_or_contract_risk_score": 1, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_before": 80, "stage_label_before": "Stage3-Yellow", "raw_component_scores_after": {"contract_score": 2, "backlog_visibility_score": 4, "margin_bridge_score": 11, "revision_score": 12, "relative_strength_score": 14, "customer_quality_score": 2, "policy_or_regulatory_score": 16, "valuation_repricing_score": 14, "execution_risk_score": 4, "legal_or_contract_risk_score": 1, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_after": 80, "stage_label_after": "Stage3-Yellow", "changed_components": [], "component_delta_explanation": "P0 current calibrated proxy; no C16 shadow gate applied.", "MFE_90D_pct": 83.0, "MAE_90D_pct": -6.71, "score_return_alignment_label": "structural_success_then_4B_required", "current_profile_verdict": "current_profile_correct"}
{"row_type": "score_simulation", "profile_id": "C16_strategic_resource_supply_shadow_profile", "case_id": "R4L14_C16_POSCOHOLD_20230712_LITHIUM_RESOURCE_RERATING", "trigger_id": "R4L14_C16_T01_POSCOHOLD_20230712_S2A", "symbol": "005490", "large_sector_id": "L4_MATERIALS_SPREAD_RESOURCE", "canonical_archetype_id": "C16_STRATEGIC_RESOURCE_POLICY_SUPPLY", "raw_component_scores_before": {"contract_score": 2, "backlog_visibility_score": 4, "margin_bridge_score": 11, "revision_score": 12, "relative_strength_score": 14, "customer_quality_score": 2, "policy_or_regulatory_score": 16, "valuation_repricing_score": 14, "execution_risk_score": 4, "legal_or_contract_risk_score": 1, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_before": 80, "stage_label_before": "Stage3-Yellow", "raw_component_scores_after": {"contract_score": 2, "backlog_visibility_score": 4, "margin_bridge_score": 14, "revision_score": 14, "relative_strength_score": 14, "customer_quality_score": 2, "policy_or_regulatory_score": 18, "valuation_repricing_score": 14, "execution_risk_score": 3, "legal_or_contract_risk_score": 1, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_after": 86, "stage_label_after": "Stage3-Yellow / Green-shadow watch", "changed_components": ["margin_bridge_score", "revision_score", "policy_or_regulatory_score", "execution_risk_score"], "component_delta_explanation": "C16 shadow gate separates verified strategic resource conversion from price-only resource optionality. Policy/resource scores are capped unless economics, ownership/permitting, utilization, margin bridge, or revision appear.", "MFE_90D_pct": 83.0, "MAE_90D_pct": -6.71, "score_return_alignment_label": "structural_success_then_4B_required", "current_profile_verdict": "current_profile_correct"}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R4L14_C16_KUMYANG_20230726_LITHIUM_OPTIONALITY_BLOWOFF", "trigger_id": "R4L14_C16_T02_KUMYANG_20230726_FALSE_GREEN", "symbol": "001570", "large_sector_id": "L4_MATERIALS_SPREAD_RESOURCE", "canonical_archetype_id": "C16_STRATEGIC_RESOURCE_POLICY_SUPPLY", "raw_component_scores_before": {"contract_score": 0, "backlog_visibility_score": 1, "margin_bridge_score": 0, "revision_score": 3, "relative_strength_score": 17, "customer_quality_score": 0, "policy_or_regulatory_score": 18, "valuation_repricing_score": 17, "execution_risk_score": 12, "legal_or_contract_risk_score": 2, "dilution_cb_risk_score": 3, "accounting_trust_risk_score": 1}, "weighted_score_before": 72, "stage_label_before": "Stage2-Actionable / false-Yellow risk", "raw_component_scores_after": {"contract_score": 0, "backlog_visibility_score": 1, "margin_bridge_score": 0, "revision_score": 3, "relative_strength_score": 17, "customer_quality_score": 0, "policy_or_regulatory_score": 18, "valuation_repricing_score": 17, "execution_risk_score": 12, "legal_or_contract_risk_score": 2, "dilution_cb_risk_score": 3, "accounting_trust_risk_score": 1}, "weighted_score_after": 72, "stage_label_after": "Stage2-Actionable / false-Yellow risk", "changed_components": [], "component_delta_explanation": "P0 current calibrated proxy; no C16 shadow gate applied.", "MFE_90D_pct": 27.46, "MAE_90D_pct": -45.47, "score_return_alignment_label": "failed_rerating_high_MAE", "current_profile_verdict": "current_profile_false_positive"}
{"row_type": "score_simulation", "profile_id": "C16_strategic_resource_supply_shadow_profile", "case_id": "R4L14_C16_KUMYANG_20230726_LITHIUM_OPTIONALITY_BLOWOFF", "trigger_id": "R4L14_C16_T02_KUMYANG_20230726_FALSE_GREEN", "symbol": "001570", "large_sector_id": "L4_MATERIALS_SPREAD_RESOURCE", "canonical_archetype_id": "C16_STRATEGIC_RESOURCE_POLICY_SUPPLY", "raw_component_scores_before": {"contract_score": 0, "backlog_visibility_score": 1, "margin_bridge_score": 0, "revision_score": 3, "relative_strength_score": 17, "customer_quality_score": 0, "policy_or_regulatory_score": 18, "valuation_repricing_score": 17, "execution_risk_score": 12, "legal_or_contract_risk_score": 2, "dilution_cb_risk_score": 3, "accounting_trust_risk_score": 1}, "weighted_score_before": 72, "stage_label_before": "Stage2-Actionable / false-Yellow risk", "raw_component_scores_after": {"contract_score": 0, "backlog_visibility_score": 1, "margin_bridge_score": 0, "revision_score": 3, "relative_strength_score": 17, "customer_quality_score": 0, "policy_or_regulatory_score": 12, "valuation_repricing_score": 11, "execution_risk_score": 17, "legal_or_contract_risk_score": 4, "dilution_cb_risk_score": 3, "accounting_trust_risk_score": 1}, "weighted_score_after": 53, "stage_label_after": "Stage1/Watch - resource optionality only", "changed_components": ["policy_or_regulatory_score", "valuation_repricing_score", "execution_risk_score", "legal_or_contract_risk_score"], "component_delta_explanation": "C16 shadow gate separates verified strategic resource conversion from price-only resource optionality. Policy/resource scores are capped unless economics, ownership/permitting, utilization, margin bridge, or revision appear.", "MFE_90D_pct": 27.46, "MAE_90D_pct": -45.47, "score_return_alignment_label": "failed_rerating_high_MAE", "current_profile_verdict": "current_profile_false_positive"}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R4L14_C16_POSCOMTECH_20230726_RESOURCE_PROXY_BLOWOFF", "trigger_id": "R4L14_C16_T03_POSCOMTECH_20230726_FALSE_GREEN", "symbol": "009520", "large_sector_id": "L4_MATERIALS_SPREAD_RESOURCE", "canonical_archetype_id": "C16_STRATEGIC_RESOURCE_POLICY_SUPPLY", "raw_component_scores_before": {"contract_score": 0, "backlog_visibility_score": 1, "margin_bridge_score": 0, "revision_score": 2, "relative_strength_score": 18, "customer_quality_score": 0, "policy_or_regulatory_score": 16, "valuation_repricing_score": 16, "execution_risk_score": 11, "legal_or_contract_risk_score": 1, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_before": 73, "stage_label_before": "Stage2-Actionable / false-Yellow risk", "raw_component_scores_after": {"contract_score": 0, "backlog_visibility_score": 1, "margin_bridge_score": 0, "revision_score": 2, "relative_strength_score": 18, "customer_quality_score": 0, "policy_or_regulatory_score": 16, "valuation_repricing_score": 16, "execution_risk_score": 11, "legal_or_contract_risk_score": 1, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_after": 73, "stage_label_after": "Stage2-Actionable / false-Yellow risk", "changed_components": [], "component_delta_explanation": "P0 current calibrated proxy; no C16 shadow gate applied.", "MFE_90D_pct": 20.05, "MAE_90D_pct": -46.23, "score_return_alignment_label": "failed_resource_proxy_rerating", "current_profile_verdict": "current_profile_false_positive"}
{"row_type": "score_simulation", "profile_id": "C16_strategic_resource_supply_shadow_profile", "case_id": "R4L14_C16_POSCOMTECH_20230726_RESOURCE_PROXY_BLOWOFF", "trigger_id": "R4L14_C16_T03_POSCOMTECH_20230726_FALSE_GREEN", "symbol": "009520", "large_sector_id": "L4_MATERIALS_SPREAD_RESOURCE", "canonical_archetype_id": "C16_STRATEGIC_RESOURCE_POLICY_SUPPLY", "raw_component_scores_before": {"contract_score": 0, "backlog_visibility_score": 1, "margin_bridge_score": 0, "revision_score": 2, "relative_strength_score": 18, "customer_quality_score": 0, "policy_or_regulatory_score": 16, "valuation_repricing_score": 16, "execution_risk_score": 11, "legal_or_contract_risk_score": 1, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_before": 73, "stage_label_before": "Stage2-Actionable / false-Yellow risk", "raw_component_scores_after": {"contract_score": 0, "backlog_visibility_score": 1, "margin_bridge_score": 0, "revision_score": 2, "relative_strength_score": 18, "customer_quality_score": 0, "policy_or_regulatory_score": 8, "valuation_repricing_score": 10, "execution_risk_score": 16, "legal_or_contract_risk_score": 1, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_after": 54, "stage_label_after": "Stage1/Watch - proxy only", "changed_components": ["policy_or_regulatory_score", "valuation_repricing_score", "execution_risk_score"], "component_delta_explanation": "C16 shadow gate separates verified strategic resource conversion from price-only resource optionality. Policy/resource scores are capped unless economics, ownership/permitting, utilization, margin bridge, or revision appear.", "MFE_90D_pct": 20.05, "MAE_90D_pct": -46.23, "score_return_alignment_label": "failed_resource_proxy_rerating", "current_profile_verdict": "current_profile_false_positive"}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R4L14_C16_KOREAZINC_20220915_BATTERY_METALS_JV_FALSE_START", "trigger_id": "R4L14_C16_T04_KOREAZINC_20220915_STAGE2_FALSE_START", "symbol": "010130", "large_sector_id": "L4_MATERIALS_SPREAD_RESOURCE", "canonical_archetype_id": "C16_STRATEGIC_RESOURCE_POLICY_SUPPLY", "raw_component_scores_before": {"contract_score": 1, "backlog_visibility_score": 3, "margin_bridge_score": 2, "revision_score": 3, "relative_strength_score": 8, "customer_quality_score": 3, "policy_or_regulatory_score": 15, "valuation_repricing_score": 8, "execution_risk_score": 6, "legal_or_contract_risk_score": 1, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_before": 68, "stage_label_before": "Stage2-Actionable", "raw_component_scores_after": {"contract_score": 1, "backlog_visibility_score": 3, "margin_bridge_score": 2, "revision_score": 3, "relative_strength_score": 8, "customer_quality_score": 3, "policy_or_regulatory_score": 15, "valuation_repricing_score": 8, "execution_risk_score": 6, "legal_or_contract_risk_score": 1, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_after": 68, "stage_label_after": "Stage2-Actionable", "changed_components": [], "component_delta_explanation": "P0 current calibrated proxy; no C16 shadow gate applied.", "MFE_90D_pct": 8.04, "MAE_90D_pct": -20.35, "score_return_alignment_label": "stage2_watch_failed_rerating", "current_profile_verdict": "current_profile_too_early"}
{"row_type": "score_simulation", "profile_id": "C16_strategic_resource_supply_shadow_profile", "case_id": "R4L14_C16_KOREAZINC_20220915_BATTERY_METALS_JV_FALSE_START", "trigger_id": "R4L14_C16_T04_KOREAZINC_20220915_STAGE2_FALSE_START", "symbol": "010130", "large_sector_id": "L4_MATERIALS_SPREAD_RESOURCE", "canonical_archetype_id": "C16_STRATEGIC_RESOURCE_POLICY_SUPPLY", "raw_component_scores_before": {"contract_score": 1, "backlog_visibility_score": 3, "margin_bridge_score": 2, "revision_score": 3, "relative_strength_score": 8, "customer_quality_score": 3, "policy_or_regulatory_score": 15, "valuation_repricing_score": 8, "execution_risk_score": 6, "legal_or_contract_risk_score": 1, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_before": 68, "stage_label_before": "Stage2-Actionable", "raw_component_scores_after": {"contract_score": 1, "backlog_visibility_score": 3, "margin_bridge_score": 1, "revision_score": 2, "relative_strength_score": 8, "customer_quality_score": 3, "policy_or_regulatory_score": 12, "valuation_repricing_score": 8, "execution_risk_score": 8, "legal_or_contract_risk_score": 1, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_after": 61, "stage_label_after": "Stage2-Watch / no Green", "changed_components": ["policy_or_regulatory_score", "revision_score", "margin_bridge_score", "execution_risk_score"], "component_delta_explanation": "C16 shadow gate separates verified strategic resource conversion from price-only resource optionality. Policy/resource scores are capped unless economics, ownership/permitting, utilization, margin bridge, or revision appear.", "MFE_90D_pct": 8.04, "MAE_90D_pct": -20.35, "score_return_alignment_label": "stage2_watch_failed_rerating", "current_profile_verdict": "current_profile_too_early"}
{"row_type": "residual_contribution", "round": "R4", "loop": "14", "large_sector_id": "L4_MATERIALS_SPREAD_RESOURCE", "canonical_archetype_id": "C16_STRATEGIC_RESOURCE_POLICY_SUPPLY", "scheduled_round": "R4", "scheduled_loop": "14", "round_schedule_status": "valid", "round_sector_consistency": "pass", "new_independent_case_count": 4, "reused_case_count": 0, "new_symbol_count": 4, "same_archetype_new_symbol_count": 4, "same_archetype_new_trigger_family_count": 4, "new_trigger_family_count": 4, "positive_case_count": 1, "counterexample_count": 3, "current_profile_error_count": 3, "diversity_score_summary": "C16 gap fill; 4 new symbols/triggers for this canonical; resource-policy headline vs verified economics tested.", "tested_existing_calibrated_axes": ["stage2_actionable_evidence_bonus", "stage3_green_revision_min", "full_4b_requires_non_price_evidence", "price_only_blowoff_blocks_positive_stage", "hard_4c_thesis_break_routes_to_4c"], "residual_error_types_found": ["resource_policy_false_positive", "proxy_resource_beta_false_green", "resource_optional_blowoff_high_MAE", "JV_optionality_without_revision"], "loop_contribution_label": "canonical_archetype_rule_candidate", "do_not_propose_new_weight_delta": false}
{"row_type": "narrative_only", "case_id": "R4L14_C16_STX_202309_RESOURCE_TRADING_BLOCKED", "symbol": "011810", "large_sector_id": "L4_MATERIALS_SPREAD_RESOURCE", "canonical_archetype_id": "C16_STRATEGIC_RESOURCE_POLICY_SUPPLY", "reason": "stock-web profile shows corporate_action_candidate_dates 2023-09-15 and 2024-01-05; 180D resource-theme window is contaminated and not usable for weight calibration", "price_source": "Songdaiki/stock-web", "usage": "not_weight_calibration"}
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
completed_loop = 14
next_round = R5
next_loop = 14
round_schedule_status = valid
round_sector_consistency = pass
```

## 28. Source Notes

```text
stock_web_manifest = atlas/manifest.json
stock_web_schema = atlas/schema.json
universe = atlas/universe/all_symbols.csv
inspected_profiles:
  - atlas/symbol_profiles/005/005490.json
  - atlas/symbol_profiles/001/001570.json
  - atlas/symbol_profiles/009/009520.json
  - atlas/symbol_profiles/010/010130.json
  - atlas/symbol_profiles/011/011810.json (narrative-only blocked candidate)
inspected_price_rows:
  - 005490 2023-07-12 / 2023-07-26 / 2024-04-08
  - 001570 2023-07-26 / 2024-01-26
  - 009520 2023-07-26 / 2024-04-08
  - 010130 2022-09-15 / 2022-11-23 / 2023-01-05
```

