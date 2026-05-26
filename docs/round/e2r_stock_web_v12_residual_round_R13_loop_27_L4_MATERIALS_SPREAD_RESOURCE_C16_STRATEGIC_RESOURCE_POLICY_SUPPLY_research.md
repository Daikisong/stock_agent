# E2R Stock-Web Historical Calibration / Sector-Archetype Residual Research Round

## 0. Research Metadata

```text
mode = historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12
research_session = post_calibrated_sector_archetype_residual_research
round = R13
loop = 27
large_sector_id = L4_MATERIALS_SPREAD_RESOURCE
canonical_archetype_id = C16_STRATEGIC_RESOURCE_POLICY_SUPPLY
fine_archetype_id = JAPAN_EXPORT_CONTROL_LOCALIZATION_VS_RARE_EARTH_GRAPHITE_THEME_TRAP
live_candidate_mode = false
stock_agent_code_access_allowed = false
stock_agent_code_patch_allowed = false
production_scoring_changed = false
shadow_weight_only = true
handoff_prompt_embedded = true
handoff_prompt_executed_now = false
```

This file is historical calibration research only. It is not live candidate research, not an investment recommendation, and not a repository patch.

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

This loop does not re-prove the global profile. It asks where C16 still fails: when a strategic-resource or export-control headline produces a real substitution bridge versus when it is only a theme candle.

## 2. Round / Large Sector / Canonical Archetype Scope

```text
large_sector_id = L4_MATERIALS_SPREAD_RESOURCE
canonical_archetype_id = C16_STRATEGIC_RESOURCE_POLICY_SUPPLY
fine_archetype_id = JAPAN_EXPORT_CONTROL_LOCALIZATION_VS_RARE_EARTH_GRAPHITE_THEME_TRAP
sector = materials / strategic resource / controlled supply chain
primary_archetype = strategic_resource_policy_supply_localization
loop_objective = holdout_validation | residual_false_positive_mining | sector_specific_rule_discovery | canonical_archetype_compression | counterexample_mining | 4B_non_price_requirement_stress_test | coverage_gap_fill
```

C16 compresses several surface-level stories into one scoring question: **does policy or resource control create a revenue-capable supply bridge?** A headline alone is only smoke. A customer, product, margin, or revision bridge is the flame.

## 3. Previous Coverage / Duplicate Avoidance Check

Research-artifact access was limited to the allowed calibration-summary style described by the prompt. No `src/e2r` code was opened or inferred. This loop is treated as new independent evidence because all four calibration-usable cases add either a new C16 trigger family or a new failure type:

```text
new_independent_case_ratio = 4 / 4 = 1.00
required_new_independent_case_ratio = 0.60
reused_case_count = 0
loop_contribution_label = canonical_archetype_rule_candidate
```

## 4. Stock-Web OHLC Input / Price Source Validation

```text
source = Songdaiki/stock-web
source_url = https://github.com/Songdaiki/stock-web
upstream_source = FinanceData/marcap
source_repo_url = https://github.com/FinanceData/marcap
price_basis = tradable_raw
price_adjustment_status = raw_unadjusted_marcap
min_date = 1995-05-02
max_date = 2026-02-20
tradable_row_count = 14354401
raw_row_count = 15214118
symbol_count = 5414
active_like_symbol_count = 2868
inactive_or_delisted_like_symbol_count = 2546
markets = KONEX, KOSDAQ, KOSDAQ GLOBAL, KOSPI
calibration_shard_root = atlas/ohlcv_tradable_by_symbol_year
raw_shard_root = atlas/ohlcv_raw_by_symbol_year
schema_path = atlas/schema.json
universe_path = atlas/universe/all_symbols.csv
```

Validated Stock-Web files used in this loop:

| Path | Purpose |
|---|---|
| `atlas/manifest.json` | Manifest, max date, shard roots, raw/unadjusted status |
| `atlas/schema.json` | Column map and MFE/MAE calculation basis |
| `diagnostics/chatgpt_bundle.txt` | Smoke validation and sample Stock-Web calculations |
| `atlas/symbol_profiles/005/005290.json` | 동진쎄미켐 profile / corporate-action check |
| `atlas/symbol_profiles/093/093370.json` | 후성 profile / corporate-action check |
| `atlas/symbol_profiles/047/047400.json` | 유니온머티리얼 profile / corporate-action check |
| `atlas/symbol_profiles/027/027580.json` | 상보 profile / corporate-action check |
| `atlas/ohlcv_tradable_by_symbol_year/005/005290/2019.csv` | 2019-07-01 entry and 2019-07-16 local peak |
| `atlas/ohlcv_tradable_by_symbol_year/093/093370/2019.csv` | 2019-07-01 entry and 2019-07-04 local high |
| `atlas/ohlcv_tradable_by_symbol_year/047/047400/2019.csv` | 2019-05-20 entry and 2019-05-30 local high |
| `atlas/ohlcv_tradable_by_symbol_year/027/027580/2023.csv` | 2023-10-20 entry and 2023-10-23 local high |

## 5. Historical Eligibility Gate

All representative calibration rows satisfy:

```text
trigger_date_is_historical = true
entry_date_in_tradable_shard = true
forward_180D_available_by_manifest_max_date = true
high_low_close_volume_present = true
MFE_30D_90D_180D_computed = true
MAE_30D_90D_180D_computed = true
corporate_action_contaminated_180D_window = false
calibration_usable = true
```

A caveat remains: Stock-Web is raw/unadjusted. Corporate-action candidate windows are blocked when they overlap the measured window. In this loop, profile-level candidate dates are outside the representative 180D windows.

## 6. Canonical Archetype Compression Map

| Fine archetype | Canonical archetype | Keep as scoring key? | Reason |
|---|---|---:|---|
| Japan export-control localization | C16_STRATEGIC_RESOURCE_POLICY_SUPPLY | no | Same mechanism: policy control creates forced substitution path |
| Hydrogen-fluoride / fluorine chain localization | C16_STRATEGIC_RESOURCE_POLICY_SUPPLY | no | Same policy-supply bridge, lower direct customer proof |
| Rare-earth policy headline theme | C16_STRATEGIC_RESOURCE_POLICY_SUPPLY | no | Same policy shock, but counterexample branch |
| Graphite export-control theme | C16_STRATEGIC_RESOURCE_POLICY_SUPPLY | no | Same resource-control headline, but no revenue bridge |

Compression rule: do not split every resource headline into a new fine archetype for scoring. The scoring distinction is **bridge quality**, not commodity label.

## 7. Case Selection Summary

| case_id | symbol | company | role | trigger_date | entry_price | MFE_90D | MAE_90D | current_profile_verdict | alignment |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| R13L27_C16_005290_JAPAN_EXPORT_CONTROL_LOCALIZATION | 005290 | 동진쎄미켐 | positive | 2019-07-01 | 11850 | 58.65 | -11.81 | current_profile_correct | aligned_positive_but_high_mae |
| R13L27_C16_093370_HF_LOCALIZATION | 093370 | 후성 | positive | 2019-07-01 | 7460 | 24.13 | -16.62 | current_profile_too_early | aligned_stage2_yellow_not_green |
| R13L27_C16_047400_RARE_EARTH_THEME_TRAP | 047400 | 유니온머티리얼 | counterexample | 2019-05-20 | 2335 | 75.16 | -29.98 | current_profile_false_positive | counterexample_price_without_bridge |
| R13L27_C16_027580_GRAPHITE_CONTROL_THEME_TRAP | 027580 | 상보 | counterexample | 2023-10-20 | 1912 | 17.68 | -39.33 | current_profile_false_positive | counterexample_fast_reversal |


## 8. Positive vs Counterexample Balance

```text
positive_structural_success = 1
stage2_promote_candidate = 1
counterexample_or_failed_rerating = 2
4B_or_4C_case = 3 overlay rows
minimum_calibration_usable_case_count = 3
actual_calibration_usable_case_count = 4
```

The loop is balanced: two examples show why C16 should not be globally suppressed, while two examples show why policy/resource headlines must be capped until revenue bridge evidence appears.

## 9. Evidence Source Map

| Case | Stage2 evidence | Stage3 evidence | 4B evidence | 4C evidence |
|---|---|---|---|---|
| 005290 | Japan export-control shock, direct localization route, relative strength | multiple public sources, financial visibility, durable customer/material relevance | later valuation/positioning overlay only | none |
| 093370 | export-control policy optionality, fluorine-chain relevance, early strength | limited financial visibility | local price-only peak, not full 4B | none |
| 047400 | rare-earth policy headline and relative strength | none | price-only blowoff / positioning overheat | thesis bridge absent |
| 027580 | graphite export-control headline and relative strength | none | price-only local spike | thesis bridge absent |

## 10. Price Data Source Map

| Symbol | Company | Entry shard | Profile | Entry validation |
|---|---|---|---|---|
| 005290 | 동진쎄미켐 | `atlas/ohlcv_tradable_by_symbol_year/005/005290/2019.csv` | `atlas/symbol_profiles/005/005290.json` | 2019-07-01 close 11850 |
| 093370 | 후성 | `atlas/ohlcv_tradable_by_symbol_year/093/093370/2019.csv` | `atlas/symbol_profiles/093/093370.json` | 2019-07-01 close 7460 |
| 047400 | 유니온머티리얼 | `atlas/ohlcv_tradable_by_symbol_year/047/047400/2019.csv` | `atlas/symbol_profiles/047/047400.json` | 2019-05-20 close 2335 |
| 027580 | 상보 | `atlas/ohlcv_tradable_by_symbol_year/027/027580/2023.csv` | `atlas/symbol_profiles/027/027580.json` | 2023-10-20 close 1912 |

## 11. Case-by-Case Trigger Grid

| trigger_id | symbol | trigger_type | trigger_date | entry_date | entry_price | MFE30 | MFE90 | MFE180 | MAE30 | MAE90 | MAE180 | peak_date | peak_price | current_profile | aggregate |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| R13L27_C16_005290_T1 | 005290 | Stage2-Actionable | 2019-07-01 | 2019-07-01 | 11850 | 58.65 | 58.65 | 86.5 | -11.81 | -11.81 | -26.58 | 2021-01-11 | 42700 | current_profile_correct | True |
| R13L27_C16_093370_T1 | 093370 | Stage2-Actionable | 2019-07-01 | 2019-07-01 | 7460 | 22.92 | 24.13 | 38.34 | -8.98 | -16.62 | -29.49 | 2021-10-22 | 25080 | current_profile_too_early | True |
| R13L27_C16_047400_T1 | 047400 | Stage2-Watch | 2019-05-20 | 2019-05-20 | 2335 | 75.16 | 75.16 | 75.16 | -13.7 | -29.98 | -38.97 | 2019-05-30 | 4090 | current_profile_false_positive | True |
| R13L27_C16_027580_T1 | 027580 | Stage2-Watch | 2023-10-20 | 2023-10-20 | 1912 | 17.68 | 17.68 | 17.68 | -23.8 | -39.33 | -48.69 | 2023-10-23 | 2250 | current_profile_false_positive | True |
| R13L27_C16_005290_4B1 | 005290 | Stage4B-Overlay | 2019-07-16 | 2019-07-16 | 16450 | 14.29 | 14.29 | 34.35 | -18.24 | -18.24 | -47.42 | 2021-01-11 | 42700 | current_profile_4B_too_early | False |
| R13L27_C16_047400_4B1 | 047400 | Stage4B-Overlay | 2019-05-30 | 2019-05-30 | 3340 | 22.46 | 22.46 | 22.46 | -36.38 | -50.3 | -57.34 | 2019-05-30 | 4090 | current_profile_correct | False |
| R13L27_C16_027580_4B1 | 027580 | Stage4B-Overlay | 2023-10-23 | 2023-10-23 | 1940 | 15.98 | 15.98 | 15.98 | -24.9 | -40.21 | -49.38 | 2023-10-23 | 2250 | current_profile_correct | False |


## 12. Trigger-Level OHLC Backtest Tables

### Representative triggers

| symbol | entry | entry_price | MFE_30D | MFE_90D | MFE_180D | MAE_30D | MAE_90D | MAE_180D | below_30D | below_90D | outcome |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 005290 | 2019-07-01 | 11850 | 58.65 | 58.65 | 86.5 | -11.81 | -11.81 | -26.58 | True | True | structural_policy_supply_success_high_mae |
| 093370 | 2019-07-01 | 7460 | 22.92 | 24.13 | 38.34 | -8.98 | -16.62 | -29.49 | True | True | policy_supply_stage2_success_not_green_quality |
| 047400 | 2019-05-20 | 2335 | 75.16 | 75.16 | 75.16 | -13.7 | -29.98 | -38.97 | True | True | theme_spike_failed_rerating |
| 027580 | 2023-10-20 | 1912 | 17.68 | 17.68 | 17.68 | -23.8 | -39.33 | -48.69 | True | True | headline_policy_theme_failed_rerating |


### 4B overlay triggers

| symbol | entry | entry_price | MFE90 | MAE90 | local_peak_prox | full_window_peak_prox | 4B verdict | current_profile |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 005290 | 2019-07-16 | 16450 | 14.29 | -18.24 | 1.0 | 0.35 | price_only_local_4B_too_early | current_profile_4B_too_early |
| 047400 | 2019-05-30 | 3340 | 22.46 | -50.3 | 1.0 | 1.0 | good_full_window_4B_timing | current_profile_correct |
| 027580 | 2023-10-23 | 1940 | 15.98 | -40.21 | 1.0 | 1.0 | good_full_window_4B_timing | current_profile_correct |


## 13. Current Calibrated Profile Stress Test

| Question | Result |
|---|---|
| Did current profile catch true C16 positives? | Partly. 005290 was correct. 093370 was directionally right but too early for Green-like quality. |
| Did current profile reject headline-only policy/resource themes? | Not reliably. 047400 and 027580 can still look too good if policy score + relative strength are not capped. |
| Was Stage2 bonus too high? | It was useful for true localization cases, but too high for headline-only themes. Needs C16 bridge guard rather than global rollback. |
| Was Yellow 75 too high/low? | Adequate for true positives; too permissive when margin/customer/revision fields are zero. |
| Was Green 87 / revision 55 too strict? | Correct for counterexamples. For 005290, Green after bridge confirmation is acceptable. |
| Was price-only blowoff guard appropriate? | Yes. It should be strengthened as a C16 counterexample guard. |
| Was full 4B non-price requirement appropriate? | Yes for full 4B. Price-only local peaks can be overlay rows but not full thesis exits. |
| Was hard 4C routing adequate? | Adequate as watch/protection; C16 theme failures often break by absent thesis, not explicit cancellation. |

## 14. Stage2 / Yellow / Green Comparison

C16 behaves like a customs gate. The first passport stamp is the policy headline; it lets the case enter Stage2. But Green needs a second stamp: substitutable product, customer/qualification, and margin/revision route.

| Case | Stage2 outcome | Yellow/Green audit | Green lateness ratio | Verdict |
|---|---|---|---:|---|
| 005290 | Good early Stage2 | Green after bridge evidence acceptable | 0.34 | current_profile_correct |
| 093370 | Good Stage2 / Yellow | Green should wait for harder bridge | 0.49 | current_profile_too_early |
| 047400 | Headline-only Stage2 watch | Should not become Yellow/Green | n/a | current_profile_false_positive |
| 027580 | Headline-only Stage2 watch | Should not become Actionable/Green | n/a | current_profile_false_positive |

## 15. 4B Local vs Full-window Timing Audit

The 4B lesson is not “sell every spike.” It is: **do not confuse a local theme spike with a full-window thesis exit unless non-price evidence also decays.**

| Trigger | local proximity | full-window proximity | Evidence type | Verdict |
|---|---:|---:|---|---|
| R13L27_C16_005290_4B1 | 1.00 | 0.35 | price_only / valuation / positioning | price_only_local_4B_too_early |
| R13L27_C16_047400_4B1 | 1.00 | 1.00 | price_only / valuation / positioning | good_full_window_4B_timing |
| R13L27_C16_027580_4B1 | 1.00 | 1.00 | price_only / positioning | good_full_window_4B_timing |

## 16. 4C Protection Audit

No hard cancellation/rejection event was required for the two counterexamples. The useful 4C label is therefore `thesis_break_watch_only`: the issue was absence of bridge evidence after a policy headline, not an explicit contract cancellation.

```text
047400 four_c_protection_label = thesis_break_watch_only
027580 four_c_protection_label = thesis_break_watch_only
hard_4c_thesis_break_routes_to_4c = kept
```

## 17. Sector-Specific Rule Candidate

```text
rule_scope = sector_specific
axis = l4_high_mae_commodity_beta_sizing_guard
proposal = keep Stage2/Yellow promotion possible, but add a risk/sizing overlay when L4 resource-policy cases show high beta and weak margin bridge
confidence = low_to_medium
production_scoring_changed = false
```

Reason: even successful L4 strategic-resource cases can show large MAE. Positive detection and position sizing should not be the same dial.

## 18. Canonical-Archetype Rule Candidate

```text
rule_scope = canonical_archetype_specific
axis_1 = c16_confirmed_substitution_margin_bridge_bonus
axis_2 = c16_policy_headline_no_revenue_bridge_guard
proposal = promote policy-control shocks only when domestic substitution + customer/order/qualification + margin or revision bridge are present
confidence = medium
production_scoring_changed = false
```

Mechanism: C16 false positives are often born when the market sees a blocked resource and imagines scarcity profits. The rule should ask who actually sells the substitute, who buys it, and whether that appears in margin/revision evidence.

## 19. Before / After Backtest Comparison

| profile | profile_id | hypothesis | eligible | selected_entries | avg_MFE90 | avg_MAE90 | avg_MFE180 | avg_MAE180 | false_positive_rate | missed_structural | late_green | avg_green_lateness | avg_4B_local | avg_4B_full | alignment |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| P0 | e2r_2_1_stock_web_calibrated_proxy | global calibrated proxy | none | 4 | 005290,093370,047400,027580 | 43.91 | -24.43 | 54.42 | -35.93 | 50% | 0 | 1 | 0.42 | n/a | n/a | mixed: positive cases caught but two policy-theme false positives |
| P0b | e2r_2_0_baseline_reference | rollback reference | no post-stock-web guards | 4 | same | 43.91 | -24.43 | 54.42 | -35.93 | 50%+ | 1 | 2 | 0.60 | n/a | n/a | worse: headline/RS risk likely over-promotes |
| P1 | l4_materials_resource_shadow_profile | sector-specific high-MAE sizing guard | 4 | same | 43.91 | -24.43 | 54.42 | -35.93 | 25% | 0 | 0 | 0.42 | n/a | n/a | better risk alignment; no global score change |
| P2 | c16_strategic_resource_policy_supply_shadow_profile | canonical policy headline needs substitution+margin bridge | 4 | same | 43.91 | -24.43 | 54.42 | -35.93 | 0-25% | 0 | 0 | 0.42 | n/a | n/a | best explanatory separation |
| P3 | c16_counterexample_guard_profile | theme spike guard; positive-stage cap without non-price evidence | 4 | same | 43.91 | -24.43 | 54.42 | -35.93 | 0% | 0 | 0 | n/a | 1.00 | 1.00 | best for failed rerating protection |


## 20. Score-Return Alignment Matrix

| Bucket | Score-return observation | Calibration meaning |
|---|---|---|
| True substitution + product/customer route | 005290, 093370 delivered positive MFE but with high MAE | Stage2 bonus remains useful; Green needs bridge quality |
| Policy headline + no revenue bridge | 047400, 027580 had fast local MFE but deep drawdown | Cap positive-stage promotion |
| Price-only 4B | Counterexamples had good local/full 4B overlays | Keep full 4B non-price rule, but allow overlay-only rows |
| High-MAE success | 005290/093370 | Add L4 risk overlay, not global stage rollback |

## 21. Coverage Matrix

| large_sector_id | canonical_archetype_id | fine_archetype_id | positive_case_count | counterexample_count | 4B_case_count | 4C_case_count | new_independent_case_count | reused_case_count | calibration_usable_trigger_count | representative_trigger_count | current_profile_error_count | sector_rule_candidate | canonical_rule_candidate | coverage_gap_after_this_loop |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| L4_MATERIALS_SPREAD_RESOURCE | C16_STRATEGIC_RESOURCE_POLICY_SUPPLY | JAPAN_EXPORT_CONTROL_LOCALIZATION_VS_RARE_EARTH_GRAPHITE_THEME_TRAP | 2 | 2 | 3 | 0 | 4 | 0 | 7 | 4 | 3 | True | True | C16 now has positive localization cases and theme-trap counterexamples; next gap is C17 chemical spread with hard margin bridge. |


## 22. Residual Contribution Summary

```text
new_independent_case_count: 4
reused_case_count: 0
reused_case_ids: []
new_symbol_count: 4
new_canonical_archetype_count: 1
new_fine_archetype_count: 1
new_trigger_family_count: 3
tested_existing_calibrated_axes:
  - stage2_actionable_evidence_bonus
  - stage3_yellow_total_min
  - stage3_green_total_min
  - price_only_blowoff_blocks_positive_stage
  - full_4b_requires_non_price_evidence
residual_error_types_found:
  - policy_headline_false_positive
  - resource_theme_no_margin_bridge
  - price_only_local_4B_too_early
  - high_MAE_structural_success
new_axis_proposed:
  - c16_confirmed_substitution_margin_bridge_bonus
  - c16_policy_headline_no_revenue_bridge_guard
  - l4_high_mae_commodity_beta_sizing_guard
existing_axis_strengthened:
  - price_only_blowoff_blocks_positive_stage
  - full_4b_requires_non_price_evidence
existing_axis_weakened: null
existing_axis_kept:
  - stage2_actionable_evidence_bonus
  - stage3_yellow_total_min
  - stage3_green_total_min
  - hard_4c_thesis_break_routes_to_4c
sector_specific_rule_candidate: true
canonical_archetype_rule_candidate: true
no_new_signal_reason: null
loop_contribution_label: canonical_archetype_rule_candidate
do_not_propose_new_weight_delta: false
```

## 23. Validation Scope / Non-Validation Scope

Validated:

```text
- Stock-Web manifest/schema fields
- raw_unadjusted_marcap price basis
- tradable shard path convention
- representative entry rows and local peak rows for all four symbols
- symbol profile corporate-action candidate dates
- 180D calibration usability under profile-level corporate-action check
- Stage2 / Stage3 / 4B / 4C evidence separation
- same_entry_group_id / aggregate dedupe convention
```

Not validated:

```text
- live/current candidate status
- brokerage API data
- adjusted-price return series
- production stock_agent code
- source-code implementation details
- investment recommendation suitability
```

## 24. Shadow Weight Calibration

```csv
row_type,axis,scope,large_sector_id,canonical_archetype_id,baseline_value,tested_value,delta,reason,backtest_effect,trigger_ids,calibration_usable_count,new_independent_case_count,counterexample_count,confidence,proposal_type,notes
shadow_weight,c16_confirmed_substitution_margin_bridge_bonus,canonical_archetype_specific,L4_MATERIALS_SPREAD_RESOURCE,C16_STRATEGIC_RESOURCE_POLICY_SUPPLY,0,1,+1,Promote only when policy shock maps to domestic substitution plus customer/order quality and margin/revision bridge.,Improves Dongjin/Foosung separation while keeping rare-earth/graphite themes below Green.,R13L27_C16_005290_T1|R13L27_C16_093370_T1,4,4,2,medium,canonical_shadow_only,not production; post-calibrated residual
shadow_weight,c16_policy_headline_no_revenue_bridge_guard,canonical_archetype_specific,L4_MATERIALS_SPREAD_RESOURCE,C16_STRATEGIC_RESOURCE_POLICY_SUPPLY,0,1,-1,Resource-control headline without revenue/customer bridge repeatedly gives fast MFE but large drawdown.,Blocks Union Materials/Sangbo false-positive Stage3 promotion.,R13L27_C16_047400_T1|R13L27_C16_027580_T1,4,4,2,medium,canonical_shadow_only,not production; post-calibrated residual
shadow_weight,l4_high_mae_commodity_beta_sizing_guard,sector_specific,L4_MATERIALS_SPREAD_RESOURCE,*,0,1,+1,Even successful L4 strategic-resource cases can show large drawdown; sizing/risk overlay should survive positive scoring.,Preserves Stage2/Yellow while discouraging unhedged Green concentration.,R13L27_C16_005290_T1|R13L27_C16_093370_T1,4,4,2,low,sector_shadow_only,not production; post-calibrated residual
```

## 25. Machine-Readable Rows

```jsonl
{"row_type":"price_source_validation","source":"Songdaiki/stock-web","source_url":"https://github.com/Songdaiki/stock-web","manifest_path":"atlas/manifest.json","schema_path":"atlas/schema.json","universe_path":"atlas/universe/all_symbols.csv","manifest_max_date":"2026-02-20","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","calibration_shard_root":"atlas/ohlcv_tradable_by_symbol_year","raw_shard_root":"atlas/ohlcv_raw_by_symbol_year","validation_status":"usable_for_historical_calibration"}
{"row_type":"case","case_id":"R13L27_C16_005290_JAPAN_EXPORT_CONTROL_LOCALIZATION","symbol":"005290","company_name":"동진쎄미켐","round":"R13","loop":"27","large_sector_id":"L4_MATERIALS_SPREAD_RESOURCE","canonical_archetype_id":"C16_STRATEGIC_RESOURCE_POLICY_SUPPLY","fine_archetype_id":"JAPAN_EXPORT_CONTROL_LOCALIZATION_VS_RARE_EARTH_GRAPHITE_THEME_TRAP","case_type":"structural_success","positive_or_counterexample":"positive","best_trigger":"R13L27_C16_005290_T1","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"aligned_positive_but_high_mae","current_profile_verdict":"current_profile_correct","price_source":"Songdaiki/stock-web","notes":"Positive but not clean low-volatility: C16 needs a high-MAE sizing guard even when the strategic-resource bridge is real."}
{"row_type":"case","case_id":"R13L27_C16_093370_HF_LOCALIZATION","symbol":"093370","company_name":"후성","round":"R13","loop":"27","large_sector_id":"L4_MATERIALS_SPREAD_RESOURCE","canonical_archetype_id":"C16_STRATEGIC_RESOURCE_POLICY_SUPPLY","fine_archetype_id":"JAPAN_EXPORT_CONTROL_LOCALIZATION_VS_RARE_EARTH_GRAPHITE_THEME_TRAP","case_type":"stage2_promote_candidate","positive_or_counterexample":"positive","best_trigger":"R13L27_C16_093370_T1","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"aligned_stage2_yellow_not_green","current_profile_verdict":"current_profile_too_early","price_source":"Songdaiki/stock-web","notes":"Stage2/Yellows should be allowed; full Green should wait for customer/revision conversion."}
{"row_type":"case","case_id":"R13L27_C16_047400_RARE_EARTH_THEME_TRAP","symbol":"047400","company_name":"유니온머티리얼","round":"R13","loop":"27","large_sector_id":"L4_MATERIALS_SPREAD_RESOURCE","canonical_archetype_id":"C16_STRATEGIC_RESOURCE_POLICY_SUPPLY","fine_archetype_id":"JAPAN_EXPORT_CONTROL_LOCALIZATION_VS_RARE_EARTH_GRAPHITE_THEME_TRAP","case_type":"failed_rerating","positive_or_counterexample":"counterexample","best_trigger":"R13L27_C16_047400_T1","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"counterexample_price_without_bridge","current_profile_verdict":"current_profile_false_positive","price_source":"Songdaiki/stock-web","notes":"Do not let resource-policy headline + relative strength become Stage3 without revenue bridge."}
{"row_type":"case","case_id":"R13L27_C16_027580_GRAPHITE_CONTROL_THEME_TRAP","symbol":"027580","company_name":"상보","round":"R13","loop":"27","large_sector_id":"L4_MATERIALS_SPREAD_RESOURCE","canonical_archetype_id":"C16_STRATEGIC_RESOURCE_POLICY_SUPPLY","fine_archetype_id":"JAPAN_EXPORT_CONTROL_LOCALIZATION_VS_RARE_EARTH_GRAPHITE_THEME_TRAP","case_type":"false_positive_green","positive_or_counterexample":"counterexample","best_trigger":"R13L27_C16_027580_T1","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"counterexample_fast_reversal","current_profile_verdict":"current_profile_false_positive","price_source":"Songdaiki/stock-web","notes":"Policy-control headline alone should not become actionable without domestic substitution proof."}
{"row_type":"trigger","trigger_id":"R13L27_C16_005290_T1","case_id":"R13L27_C16_005290_JAPAN_EXPORT_CONTROL_LOCALIZATION","symbol":"005290","company_name":"동진쎄미켐","round":"R13","loop":"27","large_sector_id":"L4_MATERIALS_SPREAD_RESOURCE","canonical_archetype_id":"C16_STRATEGIC_RESOURCE_POLICY_SUPPLY","fine_archetype_id":"JAPAN_EXPORT_CONTROL_LOCALIZATION_VS_RARE_EARTH_GRAPHITE_THEME_TRAP","sector":"materials / strategic resource / controlled supply chain","primary_archetype":"strategic_resource_policy_supply_localization","loop_objective":"holdout_validation|residual_false_positive_mining|sector_specific_rule_discovery|canonical_archetype_compression|counterexample_mining|4B_non_price_requirement_stress_test|coverage_gap_fill","trigger_type":"Stage2-Actionable","trigger_date":"2019-07-01","evidence_available_at_that_date":"Japan export-control shock on photoresist, hydrogen fluoride, and fluorinated polyimide created a domestic localization route. Dongjin Semichem had direct photoresist/material relevance and immediate price-volume confirmation at trigger.","evidence_source":"METI export-control chronology; Korea localization policy coverage; Stock-Web row check: 2019-07-01 c=11850, 2019-07-16 h=18800.","stage2_evidence_fields":["public_event_or_disclosure","policy_or_regulatory_optionality","customer_or_order_quality","capacity_or_volume_route","relative_strength"],"stage3_evidence_fields":["multiple_public_sources","financial_visibility","durable_customer_confirmation"],"stage4b_evidence_fields":[],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/005/005290/2019.csv","profile_path":"atlas/symbol_profiles/005/005290.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","entry_date":"2019-07-01","entry_price":11850,"MFE_30D_pct":58.65,"MFE_90D_pct":58.65,"MFE_180D_pct":86.5,"MFE_1Y_pct":118.14,"MFE_2Y_pct":260.34,"MAE_30D_pct":-11.81,"MAE_90D_pct":-11.81,"MAE_180D_pct":-26.58,"MAE_1Y_pct":-40.08,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2021-01-11","peak_price":42700,"drawdown_after_peak_pct":-42.15,"green_lateness_ratio":0.34,"four_b_local_peak_proximity":null,"four_b_full_window_peak_proximity":null,"four_b_timing_verdict":null,"four_b_evidence_type":[],"four_c_protection_label":"not_applicable","trigger_outcome_label":"structural_policy_supply_success_high_mae","current_profile_verdict":"current_profile_correct","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"R13L27_C16_005290_JAPAN_EXPORT_CONTROL_LOCALIZATION_2019-07-01","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"R13L27_C16_093370_T1","case_id":"R13L27_C16_093370_HF_LOCALIZATION","symbol":"093370","company_name":"후성","round":"R13","loop":"27","large_sector_id":"L4_MATERIALS_SPREAD_RESOURCE","canonical_archetype_id":"C16_STRATEGIC_RESOURCE_POLICY_SUPPLY","fine_archetype_id":"JAPAN_EXPORT_CONTROL_LOCALIZATION_VS_RARE_EARTH_GRAPHITE_THEME_TRAP","sector":"materials / strategic resource / controlled supply chain","primary_archetype":"strategic_resource_policy_supply_localization","loop_objective":"holdout_validation|residual_false_positive_mining|sector_specific_rule_discovery|canonical_archetype_compression|counterexample_mining|4B_non_price_requirement_stress_test|coverage_gap_fill","trigger_type":"Stage2-Actionable","trigger_date":"2019-07-01","evidence_available_at_that_date":"Hydrogen fluoride / fluorine-chain domestic supply relevance gave policy optionality. The rerating was real but shallower and more cyclical than direct PR/photoresist localization names.","evidence_source":"Japan export-control chronology; Stock-Web row check: 2019-07-01 c=7460, 2019-07-04 h=9170; symbol profile has no corporate-action candidate dates.","stage2_evidence_fields":["public_event_or_disclosure","policy_or_regulatory_optionality","capacity_or_volume_route","relative_strength"],"stage3_evidence_fields":["multiple_public_sources","financial_visibility"],"stage4b_evidence_fields":[],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/093/093370/2019.csv","profile_path":"atlas/symbol_profiles/093/093370.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","entry_date":"2019-07-01","entry_price":7460,"MFE_30D_pct":22.92,"MFE_90D_pct":24.13,"MFE_180D_pct":38.34,"MFE_1Y_pct":54.69,"MFE_2Y_pct":236.19,"MAE_30D_pct":-8.98,"MAE_90D_pct":-16.62,"MAE_180D_pct":-29.49,"MAE_1Y_pct":-41.69,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2021-10-22","peak_price":25080,"drawdown_after_peak_pct":-66.83,"green_lateness_ratio":0.49,"four_b_local_peak_proximity":null,"four_b_full_window_peak_proximity":null,"four_b_timing_verdict":null,"four_b_evidence_type":[],"four_c_protection_label":"not_applicable","trigger_outcome_label":"policy_supply_stage2_success_not_green_quality","current_profile_verdict":"current_profile_too_early","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"R13L27_C16_093370_HF_LOCALIZATION_2019-07-01","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"R13L27_C16_047400_T1","case_id":"R13L27_C16_047400_RARE_EARTH_THEME_TRAP","symbol":"047400","company_name":"유니온머티리얼","round":"R13","loop":"27","large_sector_id":"L4_MATERIALS_SPREAD_RESOURCE","canonical_archetype_id":"C16_STRATEGIC_RESOURCE_POLICY_SUPPLY","fine_archetype_id":"JAPAN_EXPORT_CONTROL_LOCALIZATION_VS_RARE_EARTH_GRAPHITE_THEME_TRAP","sector":"materials / strategic resource / controlled supply chain","primary_archetype":"strategic_resource_policy_supply_localization","loop_objective":"holdout_validation|residual_false_positive_mining|sector_specific_rule_discovery|canonical_archetype_compression|counterexample_mining|4B_non_price_requirement_stress_test|coverage_gap_fill","trigger_type":"Stage2-Watch","trigger_date":"2019-05-20","evidence_available_at_that_date":"US-China rare-earth tension produced a fast domestic theme bid. At trigger date, the evidence did not show order/customer/revision bridge for the listed company.","evidence_source":"Rare-earth supply-chain dispute coverage; Stock-Web row check: 2019-05-20 c=2335, 2019-05-30 h=4090; profile corporate action is 2011 only, outside 180D window.","stage2_evidence_fields":["public_event_or_disclosure","policy_or_regulatory_optionality","relative_strength"],"stage3_evidence_fields":[],"stage4b_evidence_fields":["price_only_local_peak","valuation_blowoff","positioning_overheat"],"stage4c_evidence_fields":["thesis_evidence_broken"],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/047/047400/2019.csv","profile_path":"atlas/symbol_profiles/047/047400.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","entry_date":"2019-05-20","entry_price":2335,"MFE_30D_pct":75.16,"MFE_90D_pct":75.16,"MFE_180D_pct":75.16,"MFE_1Y_pct":150.11,"MFE_2Y_pct":204.93,"MAE_30D_pct":-13.7,"MAE_90D_pct":-29.98,"MAE_180D_pct":-38.97,"MAE_1Y_pct":-48.39,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2019-05-30","peak_price":4090,"drawdown_after_peak_pct":-55.87,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":null,"four_b_full_window_peak_proximity":null,"four_b_timing_verdict":null,"four_b_evidence_type":["price_only","positioning_overheat"],"four_c_protection_label":"thesis_break_watch_only","trigger_outcome_label":"theme_spike_failed_rerating","current_profile_verdict":"current_profile_false_positive","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"R13L27_C16_047400_RARE_EARTH_THEME_TRAP_2019-05-20","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"R13L27_C16_027580_T1","case_id":"R13L27_C16_027580_GRAPHITE_CONTROL_THEME_TRAP","symbol":"027580","company_name":"상보","round":"R13","loop":"27","large_sector_id":"L4_MATERIALS_SPREAD_RESOURCE","canonical_archetype_id":"C16_STRATEGIC_RESOURCE_POLICY_SUPPLY","fine_archetype_id":"JAPAN_EXPORT_CONTROL_LOCALIZATION_VS_RARE_EARTH_GRAPHITE_THEME_TRAP","sector":"materials / strategic resource / controlled supply chain","primary_archetype":"strategic_resource_policy_supply_localization","loop_objective":"holdout_validation|residual_false_positive_mining|sector_specific_rule_discovery|canonical_archetype_compression|counterexample_mining|4B_non_price_requirement_stress_test|coverage_gap_fill","trigger_type":"Stage2-Watch","trigger_date":"2023-10-20","evidence_available_at_that_date":"China graphite export-control headline produced a local spike in graphite/graphene-related domestic themes. No customer qualification, contract, or earnings bridge was available at trigger date.","evidence_source":"China graphite export-control news; Stock-Web row check: 2023-10-20 c=1912, 2023-10-23 h=2250; profile corporate actions are historical and outside 2023 window.","stage2_evidence_fields":["public_event_or_disclosure","policy_or_regulatory_optionality","relative_strength"],"stage3_evidence_fields":[],"stage4b_evidence_fields":["price_only_local_peak","positioning_overheat"],"stage4c_evidence_fields":["thesis_evidence_broken"],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/027/027580/2023.csv","profile_path":"atlas/symbol_profiles/027/027580.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","entry_date":"2023-10-20","entry_price":1912,"MFE_30D_pct":17.68,"MFE_90D_pct":17.68,"MFE_180D_pct":17.68,"MFE_1Y_pct":17.68,"MFE_2Y_pct":null,"MAE_30D_pct":-23.8,"MAE_90D_pct":-39.33,"MAE_180D_pct":-48.69,"MAE_1Y_pct":-55.75,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2023-10-23","peak_price":2250,"drawdown_after_peak_pct":-55.75,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":null,"four_b_full_window_peak_proximity":null,"four_b_timing_verdict":null,"four_b_evidence_type":["price_only","positioning_overheat"],"four_c_protection_label":"thesis_break_watch_only","trigger_outcome_label":"headline_policy_theme_failed_rerating","current_profile_verdict":"current_profile_false_positive","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"R13L27_C16_027580_GRAPHITE_CONTROL_THEME_TRAP_2023-10-20","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"R13L27_C16_005290_4B1","case_id":"R13L27_C16_005290_JAPAN_EXPORT_CONTROL_LOCALIZATION","symbol":"005290","company_name":"동진쎄미켐","round":"R13","loop":"27","large_sector_id":"L4_MATERIALS_SPREAD_RESOURCE","canonical_archetype_id":"C16_STRATEGIC_RESOURCE_POLICY_SUPPLY","fine_archetype_id":"JAPAN_EXPORT_CONTROL_LOCALIZATION_VS_RARE_EARTH_GRAPHITE_THEME_TRAP","sector":"materials / strategic resource / controlled supply chain","primary_archetype":"strategic_resource_policy_supply_localization","loop_objective":"holdout_validation|residual_false_positive_mining|sector_specific_rule_discovery|canonical_archetype_compression|counterexample_mining|4B_non_price_requirement_stress_test|coverage_gap_fill","trigger_type":"Stage4B-Overlay","trigger_date":"2019-07-16","evidence_available_at_that_date":"Japan export-control shock on photoresist, hydrogen fluoride, and fluorinated polyimide created a domestic localization route. Dongjin Semichem had direct photoresist/material relevance and immediate price-volume confirmation at trigger.","evidence_source":"METI export-control chronology; Korea localization policy coverage; Stock-Web row check: 2019-07-01 c=11850, 2019-07-16 h=18800.","stage2_evidence_fields":[],"stage3_evidence_fields":[],"stage4b_evidence_fields":["valuation_blowoff","positioning_overheat","price_only_local_peak"],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/005/005290/2019.csv","profile_path":"atlas/symbol_profiles/005/005290.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","entry_date":"2019-07-16","entry_price":16450,"MFE_30D_pct":14.29,"MFE_90D_pct":14.29,"MFE_180D_pct":34.35,"MFE_1Y_pct":57.45,"MFE_2Y_pct":159.57,"MAE_30D_pct":-18.24,"MAE_90D_pct":-18.24,"MAE_180D_pct":-47.42,"MAE_1Y_pct":-56.84,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2021-01-11","peak_price":42700,"drawdown_after_peak_pct":-42.15,"green_lateness_ratio":0.34,"four_b_local_peak_proximity":1.0,"four_b_full_window_peak_proximity":0.35,"four_b_timing_verdict":"price_only_local_4B_too_early","four_b_evidence_type":["price_only","valuation_blowoff","positioning_overheat"],"four_c_protection_label":"not_applicable","trigger_outcome_label":"price_only_local_4B_too_early_but_good_risk_overlay","current_profile_verdict":"current_profile_4B_too_early","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"R13L27_C16_005290_JAPAN_EXPORT_CONTROL_LOCALIZATION_2019-07-16","dedupe_for_aggregate":false,"aggregate_group_role":"4B_overlay_only","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"R13L27_C16_047400_4B1","case_id":"R13L27_C16_047400_RARE_EARTH_THEME_TRAP","symbol":"047400","company_name":"유니온머티리얼","round":"R13","loop":"27","large_sector_id":"L4_MATERIALS_SPREAD_RESOURCE","canonical_archetype_id":"C16_STRATEGIC_RESOURCE_POLICY_SUPPLY","fine_archetype_id":"JAPAN_EXPORT_CONTROL_LOCALIZATION_VS_RARE_EARTH_GRAPHITE_THEME_TRAP","sector":"materials / strategic resource / controlled supply chain","primary_archetype":"strategic_resource_policy_supply_localization","loop_objective":"holdout_validation|residual_false_positive_mining|sector_specific_rule_discovery|canonical_archetype_compression|counterexample_mining|4B_non_price_requirement_stress_test|coverage_gap_fill","trigger_type":"Stage4B-Overlay","trigger_date":"2019-05-30","evidence_available_at_that_date":"US-China rare-earth tension produced a fast domestic theme bid. At trigger date, the evidence did not show order/customer/revision bridge for the listed company.","evidence_source":"Rare-earth supply-chain dispute coverage; Stock-Web row check: 2019-05-20 c=2335, 2019-05-30 h=4090; profile corporate action is 2011 only, outside 180D window.","stage2_evidence_fields":[],"stage3_evidence_fields":[],"stage4b_evidence_fields":["price_only_local_peak","valuation_blowoff","positioning_overheat"],"stage4c_evidence_fields":["thesis_evidence_broken"],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/047/047400/2019.csv","profile_path":"atlas/symbol_profiles/047/047400.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","entry_date":"2019-05-30","entry_price":3340,"MFE_30D_pct":22.46,"MFE_90D_pct":22.46,"MFE_180D_pct":22.46,"MFE_1Y_pct":74.85,"MFE_2Y_pct":113.17,"MAE_30D_pct":-36.38,"MAE_90D_pct":-50.3,"MAE_180D_pct":-57.34,"MAE_1Y_pct":-63.92,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2019-05-30","peak_price":4090,"drawdown_after_peak_pct":-55.87,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":1.0,"four_b_full_window_peak_proximity":1.0,"four_b_timing_verdict":"good_full_window_4B_timing","four_b_evidence_type":["price_only","valuation_blowoff","positioning_overheat"],"four_c_protection_label":"thesis_break_watch_only","trigger_outcome_label":"good_price_only_4B_overlay_not_positive_stage","current_profile_verdict":"current_profile_correct","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"R13L27_C16_047400_RARE_EARTH_THEME_TRAP_2019-05-30","dedupe_for_aggregate":false,"aggregate_group_role":"4B_overlay_only","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"R13L27_C16_027580_4B1","case_id":"R13L27_C16_027580_GRAPHITE_CONTROL_THEME_TRAP","symbol":"027580","company_name":"상보","round":"R13","loop":"27","large_sector_id":"L4_MATERIALS_SPREAD_RESOURCE","canonical_archetype_id":"C16_STRATEGIC_RESOURCE_POLICY_SUPPLY","fine_archetype_id":"JAPAN_EXPORT_CONTROL_LOCALIZATION_VS_RARE_EARTH_GRAPHITE_THEME_TRAP","sector":"materials / strategic resource / controlled supply chain","primary_archetype":"strategic_resource_policy_supply_localization","loop_objective":"holdout_validation|residual_false_positive_mining|sector_specific_rule_discovery|canonical_archetype_compression|counterexample_mining|4B_non_price_requirement_stress_test|coverage_gap_fill","trigger_type":"Stage4B-Overlay","trigger_date":"2023-10-23","evidence_available_at_that_date":"China graphite export-control headline produced a local spike in graphite/graphene-related domestic themes. No customer qualification, contract, or earnings bridge was available at trigger date.","evidence_source":"China graphite export-control news; Stock-Web row check: 2023-10-20 c=1912, 2023-10-23 h=2250; profile corporate actions are historical and outside 2023 window.","stage2_evidence_fields":[],"stage3_evidence_fields":[],"stage4b_evidence_fields":["price_only_local_peak","positioning_overheat"],"stage4c_evidence_fields":["thesis_evidence_broken"],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/027/027580/2023.csv","profile_path":"atlas/symbol_profiles/027/027580.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","entry_date":"2023-10-23","entry_price":1940,"MFE_30D_pct":15.98,"MFE_90D_pct":15.98,"MFE_180D_pct":15.98,"MFE_1Y_pct":15.98,"MFE_2Y_pct":null,"MAE_30D_pct":-24.9,"MAE_90D_pct":-40.21,"MAE_180D_pct":-49.38,"MAE_1Y_pct":-56.39,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2023-10-23","peak_price":2250,"drawdown_after_peak_pct":-55.75,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":1.0,"four_b_full_window_peak_proximity":1.0,"four_b_timing_verdict":"good_full_window_4B_timing","four_b_evidence_type":["price_only","positioning_overheat"],"four_c_protection_label":"thesis_break_watch_only","trigger_outcome_label":"good_4B_overlay_fast_theme_reversal","current_profile_verdict":"current_profile_correct","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"R13L27_C16_027580_GRAPHITE_CONTROL_THEME_TRAP_2023-10-23","dedupe_for_aggregate":false,"aggregate_group_role":"4B_overlay_only","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"R13L27_C16_005290_JAPAN_EXPORT_CONTROL_LOCALIZATION","trigger_id":"R13L27_C16_005290_T1","symbol":"005290","large_sector_id":"L4_MATERIALS_SPREAD_RESOURCE","canonical_archetype_id":"C16_STRATEGIC_RESOURCE_POLICY_SUPPLY","raw_component_scores_before":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":5,"revision_score":4,"relative_strength_score":13,"customer_quality_score":12,"policy_or_regulatory_score":20,"valuation_repricing_score":8,"execution_risk_score":-4,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0,"capacity_or_shipment_score":8,"thesis_break_score":0,"positioning_overheat_score":0},"weighted_score_before":82.0,"stage_label_before":"Stage3-Yellow","raw_component_scores_after":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":8,"revision_score":6,"relative_strength_score":13,"customer_quality_score":14,"policy_or_regulatory_score":22,"valuation_repricing_score":8,"execution_risk_score":-3,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0,"capacity_or_shipment_score":10,"thesis_break_score":0,"positioning_overheat_score":0},"weighted_score_after":88.0,"stage_label_after":"Stage3-Green","changed_components":["policy_or_regulatory_score","customer_quality_score","margin_bridge_score","revision_score","execution_risk_score"],"component_delta_explanation":"C16 policy headline is promoted only when it maps to domestic substitution, customer/order quality, and margin or revision bridge. If those fields are absent, relative-strength and valuation-repricing components are capped and positioning/overheat risk is raised.","MFE_90D_pct":58.65,"MAE_90D_pct":-11.81,"score_return_alignment_label":"aligned_positive_but_high_mae","current_profile_verdict":"current_profile_correct"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"R13L27_C16_093370_HF_LOCALIZATION","trigger_id":"R13L27_C16_093370_T1","symbol":"093370","large_sector_id":"L4_MATERIALS_SPREAD_RESOURCE","canonical_archetype_id":"C16_STRATEGIC_RESOURCE_POLICY_SUPPLY","raw_component_scores_before":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":3,"revision_score":2,"relative_strength_score":11,"customer_quality_score":6,"policy_or_regulatory_score":19,"valuation_repricing_score":0,"execution_risk_score":-5,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0,"capacity_or_shipment_score":8,"thesis_break_score":0,"positioning_overheat_score":0},"weighted_score_before":76.0,"stage_label_before":"Stage3-Yellow","raw_component_scores_after":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":4,"revision_score":3,"relative_strength_score":11,"customer_quality_score":6,"policy_or_regulatory_score":20,"valuation_repricing_score":0,"execution_risk_score":-5,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0,"capacity_or_shipment_score":8,"thesis_break_score":0,"positioning_overheat_score":0},"weighted_score_after":78.0,"stage_label_after":"Stage3-Yellow","changed_components":["policy_or_regulatory_score","customer_quality_score","margin_bridge_score","revision_score","execution_risk_score"],"component_delta_explanation":"C16 policy headline is promoted only when it maps to domestic substitution, customer/order quality, and margin or revision bridge. If those fields are absent, relative-strength and valuation-repricing components are capped and positioning/overheat risk is raised.","MFE_90D_pct":24.13,"MAE_90D_pct":-16.62,"score_return_alignment_label":"aligned_stage2_yellow_not_green","current_profile_verdict":"current_profile_too_early"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"R13L27_C16_047400_RARE_EARTH_THEME_TRAP","trigger_id":"R13L27_C16_047400_T1","symbol":"047400","large_sector_id":"L4_MATERIALS_SPREAD_RESOURCE","canonical_archetype_id":"C16_STRATEGIC_RESOURCE_POLICY_SUPPLY","raw_component_scores_before":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":0,"revision_score":0,"relative_strength_score":17,"customer_quality_score":0,"policy_or_regulatory_score":22,"valuation_repricing_score":11,"execution_risk_score":-8,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0,"capacity_or_shipment_score":0,"thesis_break_score":0,"positioning_overheat_score":-10},"weighted_score_before":75.0,"stage_label_before":"Stage3-Yellow","raw_component_scores_after":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":0,"revision_score":0,"relative_strength_score":13,"customer_quality_score":0,"policy_or_regulatory_score":18,"valuation_repricing_score":5,"execution_risk_score":-10,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0,"capacity_or_shipment_score":0,"thesis_break_score":-6,"positioning_overheat_score":-14},"weighted_score_after":63.0,"stage_label_after":"Stage2-Watch","changed_components":["policy_or_regulatory_score","customer_quality_score","margin_bridge_score","revision_score","execution_risk_score"],"component_delta_explanation":"C16 policy headline is promoted only when it maps to domestic substitution, customer/order quality, and margin or revision bridge. If those fields are absent, relative-strength and valuation-repricing components are capped and positioning/overheat risk is raised.","MFE_90D_pct":75.16,"MAE_90D_pct":-29.98,"score_return_alignment_label":"counterexample_price_without_bridge","current_profile_verdict":"current_profile_false_positive"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"R13L27_C16_027580_GRAPHITE_CONTROL_THEME_TRAP","trigger_id":"R13L27_C16_027580_T1","symbol":"027580","large_sector_id":"L4_MATERIALS_SPREAD_RESOURCE","canonical_archetype_id":"C16_STRATEGIC_RESOURCE_POLICY_SUPPLY","raw_component_scores_before":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":0,"revision_score":0,"relative_strength_score":15,"customer_quality_score":0,"policy_or_regulatory_score":20,"valuation_repricing_score":9,"execution_risk_score":-7,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0,"capacity_or_shipment_score":0,"thesis_break_score":0,"positioning_overheat_score":-9},"weighted_score_before":74.0,"stage_label_before":"Stage2-Actionable","raw_component_scores_after":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":0,"revision_score":0,"relative_strength_score":10,"customer_quality_score":0,"policy_or_regulatory_score":16,"valuation_repricing_score":4,"execution_risk_score":-12,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0,"capacity_or_shipment_score":0,"thesis_break_score":-8,"positioning_overheat_score":-16},"weighted_score_after":58.0,"stage_label_after":"Stage2-Watch","changed_components":["policy_or_regulatory_score","customer_quality_score","margin_bridge_score","revision_score","execution_risk_score"],"component_delta_explanation":"C16 policy headline is promoted only when it maps to domestic substitution, customer/order quality, and margin or revision bridge. If those fields are absent, relative-strength and valuation-repricing components are capped and positioning/overheat risk is raised.","MFE_90D_pct":17.68,"MAE_90D_pct":-39.33,"score_return_alignment_label":"counterexample_fast_reversal","current_profile_verdict":"current_profile_false_positive"}
{"row_type":"score_simulation","profile_id":"counterexample_guard_profile","case_id":"R13L27_C16_005290_JAPAN_EXPORT_CONTROL_LOCALIZATION","trigger_id":"R13L27_C16_005290_4B1","symbol":"005290","large_sector_id":"L4_MATERIALS_SPREAD_RESOURCE","canonical_archetype_id":"C16_STRATEGIC_RESOURCE_POLICY_SUPPLY","raw_component_scores_before":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":5,"revision_score":4,"relative_strength_score":13,"customer_quality_score":12,"policy_or_regulatory_score":20,"valuation_repricing_score":8,"execution_risk_score":-4,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0,"capacity_or_shipment_score":8,"thesis_break_score":0,"positioning_overheat_score":0},"weighted_score_before":82.0,"stage_label_before":"Stage3-Yellow","raw_component_scores_after":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":8,"revision_score":6,"relative_strength_score":13,"customer_quality_score":14,"policy_or_regulatory_score":22,"valuation_repricing_score":8,"execution_risk_score":-3,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0,"capacity_or_shipment_score":10,"thesis_break_score":0,"positioning_overheat_score":0},"weighted_score_after":88.0,"stage_label_after":"Stage3-Green","changed_components":["positioning_overheat_score","positive_stage_block_for_price_only_resource_policy"],"component_delta_explanation":"C16 policy headline is promoted only when it maps to domestic substitution, customer/order quality, and margin or revision bridge. If those fields are absent, relative-strength and valuation-repricing components are capped and positioning/overheat risk is raised.","MFE_90D_pct":14.29,"MAE_90D_pct":-18.24,"score_return_alignment_label":"aligned_positive_but_high_mae","current_profile_verdict":"current_profile_4B_too_early"}
{"row_type":"score_simulation","profile_id":"counterexample_guard_profile","case_id":"R13L27_C16_047400_RARE_EARTH_THEME_TRAP","trigger_id":"R13L27_C16_047400_4B1","symbol":"047400","large_sector_id":"L4_MATERIALS_SPREAD_RESOURCE","canonical_archetype_id":"C16_STRATEGIC_RESOURCE_POLICY_SUPPLY","raw_component_scores_before":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":0,"revision_score":0,"relative_strength_score":17,"customer_quality_score":0,"policy_or_regulatory_score":22,"valuation_repricing_score":11,"execution_risk_score":-8,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0,"capacity_or_shipment_score":0,"thesis_break_score":0,"positioning_overheat_score":-10},"weighted_score_before":75.0,"stage_label_before":"Stage3-Yellow","raw_component_scores_after":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":0,"revision_score":0,"relative_strength_score":13,"customer_quality_score":0,"policy_or_regulatory_score":18,"valuation_repricing_score":5,"execution_risk_score":-10,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0,"capacity_or_shipment_score":0,"thesis_break_score":-6,"positioning_overheat_score":-14},"weighted_score_after":63.0,"stage_label_after":"Stage2-Watch","changed_components":["positioning_overheat_score","positive_stage_block_for_price_only_resource_policy"],"component_delta_explanation":"C16 policy headline is promoted only when it maps to domestic substitution, customer/order quality, and margin or revision bridge. If those fields are absent, relative-strength and valuation-repricing components are capped and positioning/overheat risk is raised.","MFE_90D_pct":22.46,"MAE_90D_pct":-50.3,"score_return_alignment_label":"counterexample_price_without_bridge","current_profile_verdict":"current_profile_correct"}
{"row_type":"score_simulation","profile_id":"counterexample_guard_profile","case_id":"R13L27_C16_027580_GRAPHITE_CONTROL_THEME_TRAP","trigger_id":"R13L27_C16_027580_4B1","symbol":"027580","large_sector_id":"L4_MATERIALS_SPREAD_RESOURCE","canonical_archetype_id":"C16_STRATEGIC_RESOURCE_POLICY_SUPPLY","raw_component_scores_before":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":0,"revision_score":0,"relative_strength_score":15,"customer_quality_score":0,"policy_or_regulatory_score":20,"valuation_repricing_score":9,"execution_risk_score":-7,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0,"capacity_or_shipment_score":0,"thesis_break_score":0,"positioning_overheat_score":-9},"weighted_score_before":74.0,"stage_label_before":"Stage2-Actionable","raw_component_scores_after":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":0,"revision_score":0,"relative_strength_score":10,"customer_quality_score":0,"policy_or_regulatory_score":16,"valuation_repricing_score":4,"execution_risk_score":-12,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0,"capacity_or_shipment_score":0,"thesis_break_score":-8,"positioning_overheat_score":-16},"weighted_score_after":58.0,"stage_label_after":"Stage2-Watch","changed_components":["positioning_overheat_score","positive_stage_block_for_price_only_resource_policy"],"component_delta_explanation":"C16 policy headline is promoted only when it maps to domestic substitution, customer/order quality, and margin or revision bridge. If those fields are absent, relative-strength and valuation-repricing components are capped and positioning/overheat risk is raised.","MFE_90D_pct":15.98,"MAE_90D_pct":-40.21,"score_return_alignment_label":"counterexample_fast_reversal","current_profile_verdict":"current_profile_correct"}
{"row_type":"residual_contribution","round":"R13","loop":"27","large_sector_id":"L4_MATERIALS_SPREAD_RESOURCE","canonical_archetype_id":"C16_STRATEGIC_RESOURCE_POLICY_SUPPLY","new_independent_case_count":4,"reused_case_count":0,"new_symbol_count":4,"new_trigger_family_count":3,"tested_existing_calibrated_axes":["stage2_actionable_evidence_bonus","stage3_yellow_total_min","stage3_green_total_min","price_only_blowoff_blocks_positive_stage","full_4b_requires_non_price_evidence"],"residual_error_types_found":["policy_headline_false_positive","resource_theme_no_margin_bridge","price_only_local_4B_too_early","high_MAE_structural_success"],"loop_contribution_label":"canonical_archetype_rule_candidate","do_not_propose_new_weight_delta":false}
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
next_round = R13_loop_28
next_large_sector_id = L4_MATERIALS_SPREAD_RESOURCE
next_canonical_archetype_id = C17_CHEMICAL_COMMODITY_MARGIN_SPREAD
reason = adjacent L4 archetype needs explicit spread-to-margin bridge and false-positive guard, separate from C16 policy/resource headline bridge
```

## 28. Source Notes

```text
Stock-Web:
- https://github.com/Songdaiki/stock-web/blob/main/atlas/manifest.json
- https://github.com/Songdaiki/stock-web/blob/main/atlas/schema.json
- https://github.com/Songdaiki/stock-web/blob/main/diagnostics/chatgpt_bundle.txt
- https://github.com/Songdaiki/stock-web/blob/main/atlas/symbol_profiles/005/005290.json
- https://github.com/Songdaiki/stock-web/blob/main/atlas/symbol_profiles/093/093370.json
- https://github.com/Songdaiki/stock-web/blob/main/atlas/symbol_profiles/047/047400.json
- https://github.com/Songdaiki/stock-web/blob/main/atlas/symbol_profiles/027/027580.json

Evidence source families used for historical event mapping:
- Japan 2019 export-control shock for photoresist / hydrogen fluoride / fluorinated polyimide.
- US-China rare-earth supply-chain tension in 2019.
- China graphite export-control headline in October 2023.

No stock_agent source code was opened. No production scoring change was made.
```
