# E2R Stock-Web Historical Calibration / Sector-Archetype Residual Research Round

## 0. Research Metadata

```text
mode = historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12
research_session = post_calibrated_sector_archetype_residual_research
scheduled_round = R4
scheduled_loop = 73
completed_round = R4
completed_loop = 73
large_sector_id = L4_MATERIALS_SPREAD_RESOURCE
canonical_archetype_id = C16_STRATEGIC_RESOURCE_POLICY_SUPPLY
fine_archetype_id = STRATEGIC_RESOURCE_POLICY_SUPPLY_WITH_CASHFLOW_BRIDGE_GUARD
loop_objective = sector_specific_rule_discovery | canonical_archetype_compression | residual_false_positive_mining | residual_missed_structural_mining | 4B_non_price_requirement_stress_test | counterexample_mining | coverage_gap_fill
production_scoring_changed = false
shadow_weight_only = true
stock_agent_code_access_allowed = false
stock_agent_code_patch_allowed = false
stock_agent_live_scan_allowed = false
current_stock_discovery_allowed = false
stock_web_price_atlas_access_required = true
handoff_prompt_embedded = true
handoff_prompt_executed_now = false
```

This loop adds 4 new independent cases, 2 counterexamples, and 4 residual errors for R4/L4_MATERIALS_SPREAD_RESOURCE/C16_STRATEGIC_RESOURCE_POLICY_SUPPLY.

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

This file does not re-prove the already-applied global Stage2/Green/4B axes. The residual is narrower: in strategic resources, the same word—lithium, copper, rare earth, resource security—can either be a real bridge into future earnings or just a loud label on an empty drum. The shadow rule must distinguish resource optionality backed by funding/customer/margin evidence from policy-keyword price spikes.

## 2. Round / Large Sector / Canonical Archetype Scope

| field | value |
|---|---|
| scheduled_round | R4 |
| scheduled_loop | 73 |
| large_sector_id | L4_MATERIALS_SPREAD_RESOURCE |
| canonical_archetype_id | C16_STRATEGIC_RESOURCE_POLICY_SUPPLY |
| fine_archetype_id | STRATEGIC_RESOURCE_POLICY_SUPPLY_WITH_CASHFLOW_BRIDGE_GUARD |
| round_sector_consistency | pass |
| round_schedule_status | valid |

R4 maps to L4_MATERIALS_SPREAD_RESOURCE. The previous local R4 files already covered C15_MATERIAL_SPREAD_SUPERCYCLE and C17_CHEMICAL_COMMODITY_MARGIN_SPREAD, so this loop fills the C16 strategic-resource coverage gap without jumping to another round.

## 3. Previous Coverage / Duplicate Avoidance Check

Local v12 artifact names available in the working directory show R4 Loop 71 for C15 and R4 Loop 72 for C17. The immediately preceding generated artifact reported `next_round = R4` and `next_loop = 73`. Therefore this file resolves the schedule as R4/Loop73 and selects C16.

| duplicate axis | status |
|---|---|
| same canonical + same symbol + same trigger date + same entry date | no conflict |
| previous R4 C15 material spread supercycle | not reused |
| previous R4 C17 chemical commodity spread | not reused |
| new_symbol_count | 4 |
| same_archetype_new_symbol_count | 4 |
| same_archetype_new_trigger_family_count | 4 |
| minimum_new_independent_case_ratio | 1.00 |
| schema_rematerialization_only | false |

## 4. Stock-Web OHLC Input / Price Source Validation

| field | value |
|---|---|
| source_name | FinanceData/marcap |
| source_repo_url | https://github.com/FinanceData/marcap |
| price_data_repo | Songdaiki/stock-web |
| price_adjustment_status | raw_unadjusted_marcap |
| min_date | 1995-05-02 |
| max_date | 2026-02-20 |
| tradable_row_count | 14354401 |
| raw_row_count | 15214118 |
| symbol_count | 5414 |
| active_like_symbol_count | 2868 |
| inactive_or_delisted_like_symbol_count | 2546 |
| markets | KONEX, KOSDAQ, KOSDAQ GLOBAL, KOSPI |
| calibration_shard_root | atlas/ohlcv_tradable_by_symbol_year |
| raw_shard_root | atlas/ohlcv_raw_by_symbol_year |
| schema_path | atlas/schema.json |
| universe_path | atlas/universe/all_symbols.csv |

Schema validation basis: tradable shards use `d,o,h,l,c,v,a,mc,s,m`; raw shards additionally include `rs`. MFE and MAE use the schema formula `(max high / entry_price - 1) * 100` and `(min low / entry_price - 1) * 100` over tradable rows. The atlas manifest max date is 2026-02-20, so all forward windows here are bounded by stock-web rather than by the current calendar date.

## 5. Historical Eligibility Gate

| case_id | symbol | profile_path | profile caveat | 180D forward window | corporate action window | calibration_usable |
|---|---:|---|---|---:|---|---|
| R4L73_C16_POSCOHOLDINGS_20230331_LITHIUM_RESOURCE_BRIDGE | 005490 | atlas/symbol_profiles/005/005490.json | corporate_action_candidate_count=0 | 180 | clean_180D_window | true |
| R4L73_C16_IGUINDUSTRY_20240314_COPPER_SUPPLY_TIGHTNESS | 025820 | atlas/symbol_profiles/025/025820.json | candidates are 1996/2007 only | 180 | clean_180D_window | true |
| R4L73_C16_GEUMYANG_20230726_LITHIUM_RESOURCE_BLOWOFF | 001570 | atlas/symbol_profiles/001/001570.json | candidates are old, through 2007 | 180 | clean_180D_window | true |
| R4L73_C16_UNIONMATERIAL_20230419_RARE_EARTH_POLICY_SPIKE | 047400 | atlas/symbol_profiles/047/047400.json | candidate is 2011 only | 180 | clean_180D_window | true |

STX was considered for the same strategic-resource policy theme but rejected for quantitative calibration because its profile contains corporate-action candidate dates in 2023-09-15 and 2024-01-05; this loop keeps STX out of representative rows rather than letting a contaminated 180D window sneak into the ledger.

## 6. Canonical Archetype Compression Map

```text
canonical_archetype_id = C16_STRATEGIC_RESOURCE_POLICY_SUPPLY
fine_archetype_id = STRATEGIC_RESOURCE_POLICY_SUPPLY_WITH_CASHFLOW_BRIDGE_GUARD
compressed fine families:
- lithium / brine / battery-resource verticalization
- copper supply tightness / electrification resource beta
- lithium resource blowoff without financing and execution bridge
- rare-earth / permanent-magnet policy spike without customer or margin confirmation
```

The compression works because the difference is not the metal. The difference is the bridge. A strategic-resource case becomes investable when resource optionality can walk across a bridge made of funding capacity, customer route, production visibility, margin bridge, or confirmed revision. Without that bridge, the same resource keyword behaves like a banner in the wind.

## 7. Case Selection Summary

The selected cases balance two positive resource-bridge or supply-tightness paths and two counterexamples. POSCO홀딩스 is the high-quality verticalization case; 이구산업 is a smaller copper supply-tightness case with strong MFE but thinner company-level confirmation. 금양 and 유니온머티리얼 are deliberately included as counterexamples: both had large MFE, but their evidence quality was closer to resource-theme beta than durable cash-flow proof.

## 8. Positive vs Counterexample Balance

| bucket | count | cases |
|---|---:|---|
| structural/resource bridge success | 2 | POSCO홀딩스, 이구산업 |
| counterexample or false-positive risk | 2 | 금양, 유니온머티리얼 |
| 4B overlay cases | 3 | POSCO late-July overlay, 금양, 유니온머티리얼 |
| 4C / thesis-break watch | 2 | 금양, 유니온머티리얼 |
| calibration usable representative cases | 4 | all representative cases |

## 9. Evidence Source Map

| case_id | evidence family | Stage2 evidence | Stage3 evidence | 4B evidence | 4C evidence |
|---|---|---|---|---|---|
| POSCOHOLDINGS_20230331 | lithium/brine strategic-resource verticalization | public_event_or_disclosure, policy_or_regulatory_optionality, capacity_or_volume_route, relative_strength | financial_visibility, multiple_public_sources, durable_customer_confirmation | valuation_blowoff, positioning_overheat | none |
| IGUINDUSTRY_20240314 | copper strategic supply-tightness | public_event_or_disclosure, policy_or_regulatory_optionality, relative_strength | multiple_public_sources | positioning_overheat | none |
| GEUMYANG_20230726 | lithium resource theme blowoff | public_event_or_disclosure, relative_strength, policy_or_regulatory_optionality | none | valuation_blowoff, positioning_overheat, capital_raise_or_overhang, dilution_or_cb | thesis_evidence_broken |
| UNIONMATERIAL_20230419 | rare-earth policy spike | public_event_or_disclosure, policy_or_regulatory_optionality, relative_strength | none | price_only_local_peak, valuation_blowoff, positioning_overheat | thesis_evidence_broken |

## 10. Price Data Source Map

| symbol | company | shard | verified row excerpts |
|---:|---|---|---|
| 005490 | POSCO홀딩스 | atlas/ohlcv_tradable_by_symbol_year/005/005490/2023.csv | entry: 2023-03-31 o=338000 h=392000 l=337000 c=368000; peak: 2023-07-26 h=764000 c=630000 |
| 025820 | 이구산업 | atlas/ohlcv_tradable_by_symbol_year/025/025820/2024.csv | entry: 2024-03-14 o=4400 h=4825 l=4185 c=4220; peak: 2024-05-20 h=8420 c=7880 |
| 001570 | 금양 | atlas/ohlcv_tradable_by_symbol_year/001/001570/2023.csv and 2024.csv | entry/peak: 2023-07-26 o=163500 h=194000 l=126200 c=152200; low marker: 2024-01-26 l=72300 c=80000 |
| 047400 | 유니온머티리얼 | atlas/ohlcv_tradable_by_symbol_year/047/047400/2023.csv | entry: 2023-04-19 o=3510 h=4120 l=3435 c=3935; peak: 2023-05-04 h=7890 c=6570; low marker: 2023-07-26 l=3315 c=3385 |

## 11. Case-by-Case Trigger Grid

| case_id | symbol | company | role | trigger | entry_date | entry_price | MFE_30D | MFE_90D | MFE_180D | MAE_30D | MAE_90D | MAE_180D | peak_date | peak_price | current_profile_verdict |
|---|---:|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---|---:|---|
| R4L73_C16_POSCOHOLDINGS_20230331_LITHIUM_RESOURCE_BRIDGE | 005490 | POSCO홀딩스 | structural_success | Stage2-Actionable-resource-bridge | 2023-03-31 | 368000 | 18.48% | 107.61% | 107.61% | -8.42% | -8.42% | -8.42% | 2023-07-26 | 764000 | current_profile_too_late |
| R4L73_C16_IGUINDUSTRY_20240314_COPPER_SUPPLY_TIGHTNESS | 025820 | 이구산업 | stage2_promote_candidate | Stage2-Actionable-copper-strategic-supply | 2024-03-14 | 4220 | 73.22% | 99.53% | 99.53% | -1.30% | -1.30% | -5.21% | 2024-05-20 | 8420 | current_profile_too_late |
| R4L73_C16_GEUMYANG_20230726_LITHIUM_RESOURCE_BLOWOFF | 001570 | 금양 | 4B_overlay_success | Stage4B-resource-theme-blowoff | 2023-07-26 | 152200 | 27.46% | 27.46% | 27.46% | -30.75% | -45.01% | -52.50% | 2023-07-26 | 194000 | current_profile_false_positive |
| R4L73_C16_UNIONMATERIAL_20230419_RARE_EARTH_POLICY_SPIKE | 047400 | 유니온머티리얼 | false_positive_green | Stage2-Actionable-policy-resource-spike | 2023-04-19 | 3935 | 100.51% | 100.51% | 100.51% | -12.71% | -15.76% | -23.76% | 2023-05-04 | 7890 | current_profile_false_positive |
| R4L73_C16_POSCOHOLDINGS_20230331_LITHIUM_RESOURCE_BRIDGE | 005490 | POSCO홀딩스 | 4B_overlay_success | Stage4B-valuation-blowoff-overlay | 2023-07-24 | 642000 | 19.00% | 19.00% | 19.00% | -13.55% | -22.12% | -36.40% | 2023-07-26 | 764000 | current_profile_4B_too_late |


## 12. Trigger-Level OHLC Backtest Tables

The table below is duplicated intentionally: it is the human-readable counterpart to the JSONL trigger rows in section 25. Representative rows use `dedupe_for_aggregate=true`; the POSCO late-July 4B overlay is kept as `4B_overlay_only` and is not counted as a new independent aggregate case.

| case_id | symbol | company | role | trigger | entry_date | entry_price | MFE_30D | MFE_90D | MFE_180D | MAE_30D | MAE_90D | MAE_180D | peak_date | peak_price | current_profile_verdict |
|---|---:|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---|---:|---|
| R4L73_C16_POSCOHOLDINGS_20230331_LITHIUM_RESOURCE_BRIDGE | 005490 | POSCO홀딩스 | structural_success | Stage2-Actionable-resource-bridge | 2023-03-31 | 368000 | 18.48% | 107.61% | 107.61% | -8.42% | -8.42% | -8.42% | 2023-07-26 | 764000 | current_profile_too_late |
| R4L73_C16_IGUINDUSTRY_20240314_COPPER_SUPPLY_TIGHTNESS | 025820 | 이구산업 | stage2_promote_candidate | Stage2-Actionable-copper-strategic-supply | 2024-03-14 | 4220 | 73.22% | 99.53% | 99.53% | -1.30% | -1.30% | -5.21% | 2024-05-20 | 8420 | current_profile_too_late |
| R4L73_C16_GEUMYANG_20230726_LITHIUM_RESOURCE_BLOWOFF | 001570 | 금양 | 4B_overlay_success | Stage4B-resource-theme-blowoff | 2023-07-26 | 152200 | 27.46% | 27.46% | 27.46% | -30.75% | -45.01% | -52.50% | 2023-07-26 | 194000 | current_profile_false_positive |
| R4L73_C16_UNIONMATERIAL_20230419_RARE_EARTH_POLICY_SPIKE | 047400 | 유니온머티리얼 | false_positive_green | Stage2-Actionable-policy-resource-spike | 2023-04-19 | 3935 | 100.51% | 100.51% | 100.51% | -12.71% | -15.76% | -23.76% | 2023-05-04 | 7890 | current_profile_false_positive |
| R4L73_C16_POSCOHOLDINGS_20230331_LITHIUM_RESOURCE_BRIDGE | 005490 | POSCO홀딩스 | 4B_overlay_success | Stage4B-valuation-blowoff-overlay | 2023-07-24 | 642000 | 19.00% | 19.00% | 19.00% | -13.55% | -22.12% | -36.40% | 2023-07-26 | 764000 | current_profile_4B_too_late |


## 13. Current Calibrated Profile Stress Test

| case_id | current calibrated profile likely judgment | observed path | verdict | residual interpretation |
|---|---|---|---|---|
| POSCOHOLDINGS_20230331 | Stage2/Yellow first, Green after more confirmation | 107.61% 90D/180D MFE; evidence bridge was already stronger than a generic theme | current_profile_too_late | C16 needs a resource+cashflow bridge bonus |
| IGUINDUSTRY_20240314 | Stage2/Yellow because RS and copper theme were strong but company bridge thinner | 99.53% 90D MFE with low early MAE | current_profile_too_late | sector-specific resource tightness can be actionable, but should not get full Green without margin/revision |
| GEUMYANG_20230726 | Stage2/Yellow risk if lithium keyword and RS dominate | 27.46% local MFE but -52.50% 180D MAE | current_profile_false_positive | resource keyword without execution/funding proof should cap promotion and route to 4B risk |
| UNIONMATERIAL_20230419 | Stage2/Yellow risk from rare-earth policy spike | 100.51% MFE but heavy post-peak drawdown and weak Stage3 bridge | current_profile_false_positive | policy keyword + price surge needs customer/margin confirmation |

Existing axes tested: `stage2_actionable_evidence_bonus`, `price_only_blowoff_blocks_positive_stage`, `full_4b_requires_non_price_evidence`, and `stage3_green_revision_min`. The result keeps the existing global axes but adds a C16-specific bridge/guard pair.

## 14. Stage2 / Yellow / Green Comparison

| case_id | Stage2/Actionable entry | estimated Yellow/Green issue | green_lateness_ratio | interpretation |
|---|---|---|---:|---|
| POSCOHOLDINGS | 2023-03-31 at 368000 | Green likely after more confirmation or after major move | 0.39 | Green was not catastrophic, but Stage2/Yellow underweighted the resource-cashflow bridge |
| IGUINDUSTRY | 2024-03-14 at 4220 | Green should remain constrained by thin margin/revision bridge | 0.54 | Yellow is acceptable; full Green should need margin/revision |
| GEUMYANG | 2023-07-26 at 152200 | no valid Green; should be 4B risk | not_applicable | price-only/local blowoff guard should dominate |
| UNIONMATERIAL | 2023-04-19 at 3935 | no valid Green; policy spike lacks company bridge | not_applicable | cap at Stage2-watch/4B-risk unless customer/margin evidence appears |

## 15. 4B Local vs Full-window Timing Audit

| trigger_id | four_b_local_peak_proximity | four_b_full_window_peak_proximity | four_b_timing_verdict | evidence type |
|---|---:|---:|---|---|
| POSCOHOLDINGS_T2_4B | 0.89 | 0.89 | good_full_window_4B_timing | valuation_blowoff, positioning_overheat |
| GEUMYANG_T1 | 1.00 | 1.00 | good_full_window_4B_timing_with_non_price_financing_execution_risk | valuation_blowoff, positioning_overheat, capital_raise_or_overhang, dilution_or_cb |
| UNIONMATERIAL_T1 | 0.97 | 0.97 | price_only_local_4B_too_early_unless_policy_spike_has_non_price_evidence | price_only, valuation_blowoff, positioning_overheat |

The 4B split matters. POSCO's late-July overlay is not a reason to erase the earlier valid resource bridge; it is a separate risk layer. Geumyang and UnionMaterial show the opposite: the policy/resource label itself should not promote Stage3 when the non-price evidence is weak and the stock is already near a local/full-window blowoff.

## 16. 4C Protection Audit

| case_id | 4C label | protection interpretation |
|---|---|---|
| POSCOHOLDINGS | thesis_break_watch_only | no hard 4C in the tested window; valuation 4B was sufficient |
| IGUINDUSTRY | false_break | copper beta drawdown was not enough to call thesis break without company-level failure evidence |
| GEUMYANG | hard_4c_success | later financing/execution skepticism and deep drawdown validate earlier 4B/4C routing |
| UNIONMATERIAL | thesis_break_watch_only | policy spike faded; hard 4C requires stronger company-level evidence than price fade alone |

## 17. Sector-Specific Rule Candidate

```text
rule_scope = sector_specific
large_sector_id = L4_MATERIALS_SPREAD_RESOURCE
candidate = L4 strategic-resource evidence requires a bridge from policy/resource optionality to cash-flow or production visibility.
```

Sector rule candidate: promote L4 resource cases only when at least two of the following are present: `resource/project ownership or secured supply`, `funding/balance-sheet capacity`, `customer or offtake route`, `margin/ASP bridge`, `production/capacity timeline`, or `confirmed revision`. Price-only resource spikes and policy keywords without those bridges are not positive Stage2/Stage3 evidence; they are 4B-risk or narrative-only rows.

## 18. Canonical-Archetype Rule Candidate

```text
rule_scope = canonical_archetype_specific
canonical_archetype_id = C16_STRATEGIC_RESOURCE_POLICY_SUPPLY
new_axis_proposed = c16_resource_cashflow_bridge_bonus
new_axis_proposed = c16_policy_keyword_without_cashflow_stage_cap
new_axis_proposed = c16_resource_rerating_valuation_4b_overlay
```

Canonical rule candidate: C16 should split into two tracks.

1. `C16 bridge-positive`: resource optionality plus funding/customer/production/margin bridge. This can receive a +1 shadow bonus and may reach Green if revision/margin evidence follows.
2. `C16 keyword-only`: policy/resource keyword plus RS without customer/margin/funding proof. This is capped below Green and may be routed to 4B watch if valuation/positioning is already extreme.

## 19. Before / After Backtest Comparison

| profile_id | scope | eligible_trigger_count | selected_entry_trigger_per_case | avg_MFE_90D | avg_MAE_90D | avg_MFE_180D | avg_MAE_180D | false_positive_rate | missed_structural_count | late_green_count | avg_green_lateness_ratio | avg_4B_local | avg_4B_full | verdict |
|---|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|
| P0_e2r_2_1_stock_web_calibrated_proxy | current_proxy | 4 | POSCO_T1, IGU_T1, GEUMYANG_T1, UNION_T1 | 83.78% | -16.87% | 83.78% | -25.47% | 50.0% | 1 | 2 | 0.47 | 0.92 | 0.92 | current profile catches broad Stage2 but over-promotes policy/resource themes without bridge |
| P0b_e2r_2_0_baseline_reference | rollback_reference | 4 | same | 83.78% | -16.87% | 83.78% | -25.47% | 50.0% | 2 | 3 | 0.58 | 0.86 | 0.86 | too slow on POSCO and too permissive on price-only themes |
| P1_sector_specific_candidate_profile | L4 sector | 4 | same | 83.78% | -16.87% | 83.78% | -25.47% | 25.0% | 0 | 1 | 0.42 | 0.90 | 0.90 | improves score-return alignment by separating real resource bridge from theme spike |
| P2_canonical_archetype_candidate_profile | C16 canonical | 4 | same | 83.78% | -16.87% | 83.78% | -25.47% | 0.0% for promoted rows | 0 | 1 | 0.39 | 0.89 | 0.89 | best canonical compression: promote only resource+cashflow bridge, cap policy keyword only |
| P3_counterexample_guard_profile | C16 guard | 4 | same | 99.03% on flagged positives, 63.99% on capped false positives | -4.86% on promoted positives, -30.39% on capped false positives | 99.03% / 63.99% | -6.82% / -38.13% | 0.0% promoted false positive | 1 | 1 | 0.39 | 0.99 | 0.99 | strongest false-positive guard, but may undercount early theme MFE |


## 20. Score-Return Alignment Matrix

| trigger_id | raw component diagnosis | before_score / label | after_score / label | MFE_90D | MAE_90D | alignment |
|---|---|---|---|---:|---:|---|
| POSCOHOLDINGS_T1 | policy + resource + funding/customer bridge | 84 / Stage3-Yellow | 88 / Stage3-Green | 107.61% | -8.42% | after improves missed-structural timing |
| IGUINDUSTRY_T1 | copper supply beta, thinner company bridge | 76 / Stage3-Yellow | 78 / Stage3-Yellow | 99.53% | -1.30% | kept as Yellow, not Green |
| GEUMYANG_T1 | resource keyword + RS, weak funding/execution bridge | 79 / Stage3-Yellow | 63 / Stage2-watch_or_4B-risk | 27.46% | -45.01% | after reduces false positive |
| UNIONMATERIAL_T1 | policy keyword + price spike, no margin/customer bridge | 77 / Stage3-Yellow | 61 / Stage2-watch_or_4B-risk | 100.51% | -15.76% | after avoids treating theme spike as structural |
| POSCOHOLDINGS_T2_4B | valid prior rerating but late valuation blowoff | 83 / Stage3-Yellow | 68 / Stage2-Actionable/4B-watch | 19.00% | -22.12% | after separates 4B overlay from fresh positive trigger |

## 21. Coverage Matrix

| large_sector_id | canonical_archetype_id | fine_archetype_id | positive_case_count | counterexample_count | 4B_case_count | 4C_case_count | new_independent_case_count | reused_case_count | calibration_usable_trigger_count | representative_trigger_count | current_profile_error_count | sector_rule_candidate | canonical_rule_candidate | coverage_gap_after_this_loop |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|---|---|
| L4_MATERIALS_SPREAD_RESOURCE | C16_STRATEGIC_RESOURCE_POLICY_SUPPLY | STRATEGIC_RESOURCE_POLICY_SUPPLY_WITH_CASHFLOW_BRIDGE_GUARD | 2 | 2 | 3 | 2 | 4 | 0 | 5 | 4 | 4 | true | true | C16 now has balanced resource-bridge positives and policy/theme false positives; still needs non-Korea holdout later |


## 22. Residual Contribution Summary

```text
new_independent_case_count: 4
reused_case_count: 0
reused_case_ids: []
new_symbol_count: 4
new_canonical_archetype_count: 1
new_fine_archetype_count: 1
new_trigger_family_count: 4
tested_existing_calibrated_axes: stage2_actionable_evidence_bonus, price_only_blowoff_blocks_positive_stage, full_4b_requires_non_price_evidence, stage3_green_revision_min
residual_error_types_found: resource_keyword_false_positive, policy_theme_without_cashflow_bridge, valuation_blowoff_after_resource_rerating, missed_structural_resource_bridge
new_axis_proposed: c16_resource_cashflow_bridge_bonus, c16_policy_keyword_without_cashflow_stage_cap, c16_resource_rerating_valuation_4b_overlay
existing_axis_strengthened: price_only_blowoff_blocks_positive_stage, full_4b_requires_non_price_evidence
existing_axis_weakened: null
existing_axis_kept: stage2_actionable_evidence_bonus, stage3_yellow_total_min, stage3_green_total_min, stage3_green_revision_min, stage3_cross_evidence_green_buffer, hard_4c_thesis_break_routes_to_4c
sector_specific_rule_candidate: true
canonical_archetype_rule_candidate: true
no_new_signal_reason: null
loop_contribution_label: canonical_archetype_rule_candidate
do_not_propose_new_weight_delta: false
```

## 23. Validation Scope / Non-Validation Scope

Validated scope:

```text
- Historical trigger-level rows only.
- R4/L4/C16 strategic-resource policy/supply calibration.
- Songdaiki/stock-web tradable_raw OHLC rows.
- 30D/90D/180D MFE/MAE, peak and post-peak drawdown fields.
- Corporate-action contamination check at profile level.
- Shadow-only sector/canonical rule proposal.
```

Non-validation scope:

```text
- No current stock discovery.
- No live watchlist.
- No stock_agent src/e2r code inspection.
- No production scoring change.
- No brokerage/API/trading integration.
- No claim that C16 is globally applicable outside L4 without future holdout loops.
```

## 24. Shadow Weight Calibration

```csv
row_type,axis,scope,large_sector_id,canonical_archetype_id,baseline_value,tested_value,delta,reason,backtest_effect,trigger_ids,calibration_usable_count,new_independent_case_count,counterexample_count,confidence,proposal_type,notes
shadow_weight,c16_resource_cashflow_bridge_bonus,canonical_archetype_specific,L4_MATERIALS_SPREAD_RESOURCE,C16_STRATEGIC_RESOURCE_POLICY_SUPPLY,0,1,+1,"Strategic resource policy/supply evidence should earn promotion only when resource optionality is attached to balance-sheet capacity, customer route, production visibility, or margin bridge","POSCO and copper-supply sample retained positive promotion while price-only resource themes are not promoted",R4L73_C16_POSCOHOLDINGS_T1|R4L73_C16_IGUINDUSTRY_T1,4,4,2,medium,canonical_shadow_only,"not production; post-calibrated residual"
shadow_weight,c16_policy_keyword_without_cashflow_stage_cap,canonical_archetype_specific,L4_MATERIALS_SPREAD_RESOURCE,C16_STRATEGIC_RESOURCE_POLICY_SUPPLY,0,1,+1,"Policy/resource keyword plus RS without contract/margin/customer/funding evidence should be capped at Stage2-watch or 4B-risk","Reduces Geumyang and UnionMaterial false-positive Stage3/Yellow risk despite large local MFE",R4L73_C16_GEUMYANG_T1|R4L73_C16_UNIONMATERIAL_T1,2,2,2,medium,canonical_shadow_only,"not production; post-calibrated residual"
shadow_weight,c16_resource_rerating_valuation_4b_overlay,canonical_archetype_specific,L4_MATERIALS_SPREAD_RESOURCE,C16_STRATEGIC_RESOURCE_POLICY_SUPPLY,0,1,+1,"After a valid strategic-resource rerating, a vertical move into valuation/positioning blowoff should shift to 4B overlay rather than re-trigger positive Stage3","POSCO 2023 late-July overlay and Geumyang blowoff both improve timing when local/full-window proximity is split",R4L73_C16_POSCOHOLDINGS_T2_4B|R4L73_C16_GEUMYANG_T1,2,1,1,medium,canonical_shadow_only,"not production; 4B overlay only"
```

## 25. Machine-Readable Rows

```jsonl
{"row_type": "price_source_validation", "source": "Songdaiki/stock-web", "source_url": "https://github.com/Songdaiki/stock-web", "manifest_path": "atlas/manifest.json", "schema_path": "atlas/schema.json", "universe_path": "atlas/universe/all_symbols.csv", "manifest_max_date": "2026-02-20", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "raw_shard_root": "atlas/ohlcv_raw_by_symbol_year", "validation_status": "usable_for_historical_calibration"}
{"row_type": "case", "case_id": "R4L73_C16_POSCOHOLDINGS_20230331_LITHIUM_RESOURCE_BRIDGE", "symbol": "005490", "company_name": "POSCO홀딩스", "round": "R4", "loop": "73", "large_sector_id": "L4_MATERIALS_SPREAD_RESOURCE", "canonical_archetype_id": "C16_STRATEGIC_RESOURCE_POLICY_SUPPLY", "fine_archetype_id": "STRATEGIC_RESOURCE_POLICY_SUPPLY_WITH_CASHFLOW_BRIDGE_GUARD", "case_type": "structural_success", "positive_or_counterexample": "positive", "best_trigger": "R4L73_C16_POSCOHOLDINGS_T1", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "resource bridge aligned with large 90D/180D MFE, but later valuation blowoff needed 4B overlay", "current_profile_verdict": "current_profile_too_late", "price_source": "Songdaiki/stock-web", "notes": "Profile has corporate_action_candidate_count=0; 2023 180D window clean."}
{"row_type": "case", "case_id": "R4L73_C16_IGUINDUSTRY_20240314_COPPER_SUPPLY_TIGHTNESS", "symbol": "025820", "company_name": "이구산업", "round": "R4", "loop": "73", "large_sector_id": "L4_MATERIALS_SPREAD_RESOURCE", "canonical_archetype_id": "C16_STRATEGIC_RESOURCE_POLICY_SUPPLY", "fine_archetype_id": "STRATEGIC_RESOURCE_POLICY_SUPPLY_WITH_CASHFLOW_BRIDGE_GUARD", "case_type": "stage2_promote_candidate", "positive_or_counterexample": "positive", "best_trigger": "R4L73_C16_IGUINDUSTRY_T1", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "resource tightness plus RS produced strong MFE, but thin company-level margin bridge argues for capped promotion", "current_profile_verdict": "current_profile_too_late", "price_source": "Songdaiki/stock-web", "notes": "Profile corporate-action candidates are 1996/2007 only; 2024 window clean."}
{"row_type": "case", "case_id": "R4L73_C16_GEUMYANG_20230726_LITHIUM_RESOURCE_BLOWOFF", "symbol": "001570", "company_name": "금양", "round": "R4", "loop": "73", "large_sector_id": "L4_MATERIALS_SPREAD_RESOURCE", "canonical_archetype_id": "C16_STRATEGIC_RESOURCE_POLICY_SUPPLY", "fine_archetype_id": "STRATEGIC_RESOURCE_POLICY_SUPPLY_WITH_CASHFLOW_BRIDGE_GUARD", "case_type": "4B_overlay_success", "positive_or_counterexample": "counterexample", "best_trigger": "R4L73_C16_GEUMYANG_T1", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "large MFE was already blowoff; high MAE confirms that resource-name-only promotion is dangerous", "current_profile_verdict": "current_profile_false_positive", "price_source": "Songdaiki/stock-web", "notes": "Profile has old corporate-action candidates through 2007 only; 2023/2024 window clean. Tradable last_date 2025-03-21 still supports 180D forward window."}
{"row_type": "case", "case_id": "R4L73_C16_UNIONMATERIAL_20230419_RARE_EARTH_POLICY_SPIKE", "symbol": "047400", "company_name": "유니온머티리얼", "round": "R4", "loop": "73", "large_sector_id": "L4_MATERIALS_SPREAD_RESOURCE", "canonical_archetype_id": "C16_STRATEGIC_RESOURCE_POLICY_SUPPLY", "fine_archetype_id": "STRATEGIC_RESOURCE_POLICY_SUPPLY_WITH_CASHFLOW_BRIDGE_GUARD", "case_type": "false_positive_green", "positive_or_counterexample": "counterexample", "best_trigger": "R4L73_C16_UNIONMATERIAL_T1", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "policy-resource keyword produced large MFE but poor evidence quality and heavy post-peak drawdown", "current_profile_verdict": "current_profile_false_positive", "price_source": "Songdaiki/stock-web", "notes": "Profile corporate-action candidate is 2011 only; 2023 window clean."}
{"row_type": "trigger", "trigger_id": "R4L73_C16_POSCOHOLDINGS_T1", "case_id": "R4L73_C16_POSCOHOLDINGS_20230331_LITHIUM_RESOURCE_BRIDGE", "symbol": "005490", "company_name": "POSCO홀딩스", "round": "R4", "loop": "73", "large_sector_id": "L4_MATERIALS_SPREAD_RESOURCE", "canonical_archetype_id": "C16_STRATEGIC_RESOURCE_POLICY_SUPPLY", "fine_archetype_id": "STRATEGIC_RESOURCE_POLICY_SUPPLY_WITH_CASHFLOW_BRIDGE_GUARD", "sector": "materials_spread_resource", "primary_archetype": "strategic resource policy supply", "loop_objective": "sector_specific_rule_discovery|canonical_archetype_compression|counterexample_mining|4B_non_price_requirement_stress_test|coverage_gap_fill", "trigger_type": "Stage2-Actionable-resource-bridge", "trigger_date": "2023-03-31", "evidence_available_at_that_date": "lithium/brine/resource verticalization narrative gained public visibility with an investable balance-sheet and group-materials route; the trigger is not price alone because POSCO Holdings had upstream resource optionality, downstream battery-material linkage, and cash-flow capacity to fund projects.", "evidence_source": "public resource/battery-material strategy narrative; stock-web entry row 2023-03-31 c=368000 and peak row 2023-07-26 h=764000 were verified from atlas/ohlcv_tradable_by_symbol_year/005/005490/2023.csv", "stage2_evidence_fields": ["public_event_or_disclosure", "policy_or_regulatory_optionality", "capacity_or_volume_route", "relative_strength"], "stage3_evidence_fields": ["financial_visibility", "multiple_public_sources", "durable_customer_confirmation"], "stage4b_evidence_fields": ["valuation_blowoff", "positioning_overheat"], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/005/005490/2023.csv", "profile_path": "atlas/symbol_profiles/005/005490.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "entry_date": "2023-03-31", "entry_price": 368000, "MFE_30D_pct": 18.48, "MFE_90D_pct": 107.61, "MFE_180D_pct": 107.61, "MFE_1Y_pct": 107.61, "MFE_2Y_pct": 107.61, "MAE_30D_pct": -8.42, "MAE_90D_pct": -8.42, "MAE_180D_pct": -8.42, "MAE_1Y_pct": -20.11, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2023-07-26", "peak_price": 764000, "drawdown_after_peak_pct": -46.07, "green_lateness_ratio": 0.39, "four_b_local_peak_proximity": 0.92, "four_b_full_window_peak_proximity": 0.92, "four_b_timing_verdict": "good_full_window_4B_timing_when_valuation_blowoff_is_counted", "four_b_evidence_type": ["valuation_blowoff", "positioning_overheat"], "four_c_protection_label": "thesis_break_watch_only", "trigger_outcome_label": "resource bridge aligned with large 90D/180D MFE, but later valuation blowoff needed 4B overlay", "current_profile_verdict": "current_profile_too_late", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window", "same_entry_group_id": "R4L73_C16_POSCOHOLDINGS_20230331_LITHIUM_RESOURCE_BRIDGE_2023-03-31", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R4L73_C16_POSCOHOLDINGS_20230331_LITHIUM_RESOURCE_BRIDGE", "trigger_id": "R4L73_C16_POSCOHOLDINGS_T1", "symbol": "005490", "large_sector_id": "L4_MATERIALS_SPREAD_RESOURCE", "canonical_archetype_id": "C16_STRATEGIC_RESOURCE_POLICY_SUPPLY", "raw_component_scores_before": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 2, "revision_score": 1, "relative_strength_score": 3, "customer_quality_score": 2, "policy_or_regulatory_score": 3, "valuation_repricing_score": 2, "execution_risk_score": -1, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_before": 84, "stage_label_before": "Stage3-Yellow", "raw_component_scores_after": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 2, "revision_score": 1, "relative_strength_score": 3, "customer_quality_score": 2, "policy_or_regulatory_score": 3, "valuation_repricing_score": 2, "execution_risk_score": -1, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_after": 88, "stage_label_after": "Stage3-Green", "changed_components": ["c16_cashflow_bridge_bonus", "c16_policy_keyword_without_margin_guard", "c16_resource_theme_financing_risk_guard"], "component_delta_explanation": "Shadow profile promotes strategic-resource cases only when policy/resource optionality is connected to funding capacity, customer route, margin bridge, or production visibility; otherwise resource keyword + RS is capped or routed to 4B watch.", "MFE_90D_pct": 107.61, "MAE_90D_pct": -8.42, "score_return_alignment_label": "aligned", "current_profile_verdict": "current_profile_too_late"}
{"row_type": "trigger", "trigger_id": "R4L73_C16_IGUINDUSTRY_T1", "case_id": "R4L73_C16_IGUINDUSTRY_20240314_COPPER_SUPPLY_TIGHTNESS", "symbol": "025820", "company_name": "이구산업", "round": "R4", "loop": "73", "large_sector_id": "L4_MATERIALS_SPREAD_RESOURCE", "canonical_archetype_id": "C16_STRATEGIC_RESOURCE_POLICY_SUPPLY", "fine_archetype_id": "STRATEGIC_RESOURCE_POLICY_SUPPLY_WITH_CASHFLOW_BRIDGE_GUARD", "sector": "materials_spread_resource", "primary_archetype": "strategic resource policy supply", "loop_objective": "sector_specific_rule_discovery|canonical_archetype_compression|counterexample_mining|4B_non_price_requirement_stress_test|coverage_gap_fill", "trigger_type": "Stage2-Actionable-copper-strategic-supply", "trigger_date": "2024-03-14", "evidence_available_at_that_date": "copper strategic-resource tightness and electrification demand provided a non-price macro/resource bridge. The case is deliberately smaller-cap and commodity-beta heavy, so it tests whether C16 should require supply-demand confirmation rather than generic metal-theme price strength.", "evidence_source": "public copper strategic-resource/supply-tightness narrative; stock-web entry row 2024-03-14 c=4220 and peak row 2024-05-20 h=8420 were verified from atlas/ohlcv_tradable_by_symbol_year/025/025820/2024.csv", "stage2_evidence_fields": ["public_event_or_disclosure", "policy_or_regulatory_optionality", "relative_strength"], "stage3_evidence_fields": ["multiple_public_sources"], "stage4b_evidence_fields": ["positioning_overheat"], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/025/025820/2024.csv", "profile_path": "atlas/symbol_profiles/025/025820.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "entry_date": "2024-03-14", "entry_price": 4220, "MFE_30D_pct": 73.22, "MFE_90D_pct": 99.53, "MFE_180D_pct": 99.53, "MFE_1Y_pct": 99.53, "MFE_2Y_pct": 99.53, "MAE_30D_pct": -1.3, "MAE_90D_pct": -1.3, "MAE_180D_pct": -5.21, "MAE_1Y_pct": -7.58, "below_entry_price_flag_30D": false, "below_entry_price_flag_90D": false, "peak_date": "2024-05-20", "peak_price": 8420, "drawdown_after_peak_pct": -44.18, "green_lateness_ratio": 0.54, "four_b_local_peak_proximity": 0.78, "four_b_full_window_peak_proximity": 0.78, "four_b_timing_verdict": "usable_4B_overlay_after_second_momentum_leg", "four_b_evidence_type": ["positioning_overheat", "valuation_blowoff"], "four_c_protection_label": "false_break", "trigger_outcome_label": "resource tightness plus RS produced strong MFE, but thin company-level margin bridge argues for capped promotion", "current_profile_verdict": "current_profile_too_late", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window", "same_entry_group_id": "R4L73_C16_IGUINDUSTRY_20240314_COPPER_SUPPLY_TIGHTNESS_2024-03-14", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R4L73_C16_IGUINDUSTRY_20240314_COPPER_SUPPLY_TIGHTNESS", "trigger_id": "R4L73_C16_IGUINDUSTRY_T1", "symbol": "025820", "large_sector_id": "L4_MATERIALS_SPREAD_RESOURCE", "canonical_archetype_id": "C16_STRATEGIC_RESOURCE_POLICY_SUPPLY", "raw_component_scores_before": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 1, "revision_score": 0, "relative_strength_score": 3, "customer_quality_score": 0, "policy_or_regulatory_score": 3, "valuation_repricing_score": 1, "execution_risk_score": -1, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_before": 76, "stage_label_before": "Stage3-Yellow", "raw_component_scores_after": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 1, "revision_score": 0, "relative_strength_score": 3, "customer_quality_score": 0, "policy_or_regulatory_score": 3, "valuation_repricing_score": 1, "execution_risk_score": -1, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_after": 78, "stage_label_after": "Stage3-Yellow", "changed_components": ["c16_cashflow_bridge_bonus", "c16_policy_keyword_without_margin_guard", "c16_resource_theme_financing_risk_guard"], "component_delta_explanation": "Shadow profile promotes strategic-resource cases only when policy/resource optionality is connected to funding capacity, customer route, margin bridge, or production visibility; otherwise resource keyword + RS is capped or routed to 4B watch.", "MFE_90D_pct": 99.53, "MAE_90D_pct": -1.3, "score_return_alignment_label": "aligned", "current_profile_verdict": "current_profile_too_late"}
{"row_type": "trigger", "trigger_id": "R4L73_C16_GEUMYANG_T1", "case_id": "R4L73_C16_GEUMYANG_20230726_LITHIUM_RESOURCE_BLOWOFF", "symbol": "001570", "company_name": "금양", "round": "R4", "loop": "73", "large_sector_id": "L4_MATERIALS_SPREAD_RESOURCE", "canonical_archetype_id": "C16_STRATEGIC_RESOURCE_POLICY_SUPPLY", "fine_archetype_id": "STRATEGIC_RESOURCE_POLICY_SUPPLY_WITH_CASHFLOW_BRIDGE_GUARD", "sector": "materials_spread_resource", "primary_archetype": "strategic resource policy supply", "loop_objective": "sector_specific_rule_discovery|canonical_archetype_compression|counterexample_mining|4B_non_price_requirement_stress_test|coverage_gap_fill", "trigger_type": "Stage4B-resource-theme-blowoff", "trigger_date": "2023-07-26", "evidence_available_at_that_date": "lithium/resource narrative and 2차전지 beta created a huge move, but project economics, financing burden, execution proof and cash-flow bridge were not strong enough to justify full structural Stage3 promotion at the blowoff area.", "evidence_source": "public lithium/resource-theme narrative; stock-web entry/peak row 2023-07-26 c=152200 h=194000 and 2024-01-26 l=72300 were verified from atlas/ohlcv_tradable_by_symbol_year/001/001570/2023.csv and 2024.csv", "stage2_evidence_fields": ["public_event_or_disclosure", "relative_strength", "policy_or_regulatory_optionality"], "stage3_evidence_fields": [], "stage4b_evidence_fields": ["valuation_blowoff", "positioning_overheat", "capital_raise_or_overhang", "dilution_or_cb"], "stage4c_evidence_fields": ["thesis_evidence_broken"], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/001/001570/2023.csv|atlas/ohlcv_tradable_by_symbol_year/001/001570/2024.csv", "profile_path": "atlas/symbol_profiles/001/001570.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "entry_date": "2023-07-26", "entry_price": 152200, "MFE_30D_pct": 27.46, "MFE_90D_pct": 27.46, "MFE_180D_pct": 27.46, "MFE_1Y_pct": 27.46, "MFE_2Y_pct": 27.46, "MAE_30D_pct": -30.75, "MAE_90D_pct": -45.01, "MAE_180D_pct": -52.5, "MAE_1Y_pct": -52.5, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2023-07-26", "peak_price": 194000, "drawdown_after_peak_pct": -62.73, "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": 1.0, "four_b_full_window_peak_proximity": 1.0, "four_b_timing_verdict": "good_full_window_4B_timing_with_non_price_financing_execution_risk", "four_b_evidence_type": ["valuation_blowoff", "positioning_overheat", "capital_raise_or_overhang", "dilution_or_cb"], "four_c_protection_label": "hard_4c_success", "trigger_outcome_label": "large MFE was already blowoff; high MAE confirms that resource-name-only promotion is dangerous", "current_profile_verdict": "current_profile_false_positive", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window", "same_entry_group_id": "R4L73_C16_GEUMYANG_20230726_LITHIUM_RESOURCE_BLOWOFF_2023-07-26", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R4L73_C16_GEUMYANG_20230726_LITHIUM_RESOURCE_BLOWOFF", "trigger_id": "R4L73_C16_GEUMYANG_T1", "symbol": "001570", "large_sector_id": "L4_MATERIALS_SPREAD_RESOURCE", "canonical_archetype_id": "C16_STRATEGIC_RESOURCE_POLICY_SUPPLY", "raw_component_scores_before": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": -2, "revision_score": -1, "relative_strength_score": 4, "customer_quality_score": 0, "policy_or_regulatory_score": 2, "valuation_repricing_score": -3, "execution_risk_score": -3, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": -2, "accounting_trust_risk_score": 0}, "weighted_score_before": 79, "stage_label_before": "Stage3-Yellow", "raw_component_scores_after": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": -2, "revision_score": -1, "relative_strength_score": 4, "customer_quality_score": 0, "policy_or_regulatory_score": 2, "valuation_repricing_score": -3, "execution_risk_score": -3, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": -2, "accounting_trust_risk_score": 0}, "weighted_score_after": 63, "stage_label_after": "Stage2-watch_or_4B-risk", "changed_components": ["c16_cashflow_bridge_bonus", "c16_policy_keyword_without_margin_guard", "c16_resource_theme_financing_risk_guard"], "component_delta_explanation": "Shadow profile promotes strategic-resource cases only when policy/resource optionality is connected to funding capacity, customer route, margin bridge, or production visibility; otherwise resource keyword + RS is capped or routed to 4B watch.", "MFE_90D_pct": 27.46, "MAE_90D_pct": -45.01, "score_return_alignment_label": "false_positive_reduced_by_shadow_guard", "current_profile_verdict": "current_profile_false_positive"}
{"row_type": "trigger", "trigger_id": "R4L73_C16_UNIONMATERIAL_T1", "case_id": "R4L73_C16_UNIONMATERIAL_20230419_RARE_EARTH_POLICY_SPIKE", "symbol": "047400", "company_name": "유니온머티리얼", "round": "R4", "loop": "73", "large_sector_id": "L4_MATERIALS_SPREAD_RESOURCE", "canonical_archetype_id": "C16_STRATEGIC_RESOURCE_POLICY_SUPPLY", "fine_archetype_id": "STRATEGIC_RESOURCE_POLICY_SUPPLY_WITH_CASHFLOW_BRIDGE_GUARD", "sector": "materials_spread_resource", "primary_archetype": "strategic resource policy supply", "loop_objective": "sector_specific_rule_discovery|canonical_archetype_compression|counterexample_mining|4B_non_price_requirement_stress_test|coverage_gap_fill", "trigger_type": "Stage2-Actionable-policy-resource-spike", "trigger_date": "2023-04-19", "evidence_available_at_that_date": "rare-earth export-control and permanent-magnet theme created a policy-resource spike, but the company-level contract, margin bridge, and confirmed revision channel were weak. This tests whether C16 needs a hard cap for policy keyword + price surge without customer/revenue confirmation.", "evidence_source": "public rare-earth/permanent-magnet policy narrative; stock-web entry row 2023-04-19 c=3935, peak row 2023-05-04 h=7890, and later low rows around July 2023 were verified from atlas/ohlcv_tradable_by_symbol_year/047/047400/2023.csv", "stage2_evidence_fields": ["public_event_or_disclosure", "policy_or_regulatory_optionality", "relative_strength"], "stage3_evidence_fields": [], "stage4b_evidence_fields": ["price_only_local_peak", "valuation_blowoff", "positioning_overheat"], "stage4c_evidence_fields": ["thesis_evidence_broken"], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/047/047400/2023.csv", "profile_path": "atlas/symbol_profiles/047/047400.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "entry_date": "2023-04-19", "entry_price": 3935, "MFE_30D_pct": 100.51, "MFE_90D_pct": 100.51, "MFE_180D_pct": 100.51, "MFE_1Y_pct": 100.51, "MFE_2Y_pct": 100.51, "MAE_30D_pct": -12.71, "MAE_90D_pct": -15.76, "MAE_180D_pct": -23.76, "MAE_1Y_pct": -31.49, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2023-05-04", "peak_price": 7890, "drawdown_after_peak_pct": -61.98, "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": 0.97, "four_b_full_window_peak_proximity": 0.97, "four_b_timing_verdict": "price_only_local_4B_too_early_unless_policy_spike_has_non_price_evidence", "four_b_evidence_type": ["price_only", "valuation_blowoff", "positioning_overheat"], "four_c_protection_label": "thesis_break_watch_only", "trigger_outcome_label": "policy-resource keyword produced large MFE but poor evidence quality and heavy post-peak drawdown", "current_profile_verdict": "current_profile_false_positive", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window", "same_entry_group_id": "R4L73_C16_UNIONMATERIAL_20230419_RARE_EARTH_POLICY_SPIKE_2023-04-19", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R4L73_C16_UNIONMATERIAL_20230419_RARE_EARTH_POLICY_SPIKE", "trigger_id": "R4L73_C16_UNIONMATERIAL_T1", "symbol": "047400", "large_sector_id": "L4_MATERIALS_SPREAD_RESOURCE", "canonical_archetype_id": "C16_STRATEGIC_RESOURCE_POLICY_SUPPLY", "raw_component_scores_before": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": -2, "revision_score": -1, "relative_strength_score": 4, "customer_quality_score": -1, "policy_or_regulatory_score": 3, "valuation_repricing_score": -2, "execution_risk_score": -2, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_before": 77, "stage_label_before": "Stage3-Yellow", "raw_component_scores_after": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": -2, "revision_score": -1, "relative_strength_score": 4, "customer_quality_score": -1, "policy_or_regulatory_score": 3, "valuation_repricing_score": -2, "execution_risk_score": -2, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_after": 61, "stage_label_after": "Stage2-watch_or_4B-risk", "changed_components": ["c16_cashflow_bridge_bonus", "c16_policy_keyword_without_margin_guard", "c16_resource_theme_financing_risk_guard"], "component_delta_explanation": "Shadow profile promotes strategic-resource cases only when policy/resource optionality is connected to funding capacity, customer route, margin bridge, or production visibility; otherwise resource keyword + RS is capped or routed to 4B watch.", "MFE_90D_pct": 100.51, "MAE_90D_pct": -15.76, "score_return_alignment_label": "false_positive_reduced_by_shadow_guard", "current_profile_verdict": "current_profile_false_positive"}
{"row_type": "trigger", "trigger_id": "R4L73_C16_POSCOHOLDINGS_T2_4B", "case_id": "R4L73_C16_POSCOHOLDINGS_20230331_LITHIUM_RESOURCE_BRIDGE", "symbol": "005490", "company_name": "POSCO홀딩스", "round": "R4", "loop": "73", "large_sector_id": "L4_MATERIALS_SPREAD_RESOURCE", "canonical_archetype_id": "C16_STRATEGIC_RESOURCE_POLICY_SUPPLY", "fine_archetype_id": "STRATEGIC_RESOURCE_POLICY_SUPPLY_WITH_CASHFLOW_BRIDGE_GUARD", "sector": "materials_spread_resource", "primary_archetype": "strategic resource policy supply", "loop_objective": "sector_specific_rule_discovery|canonical_archetype_compression|counterexample_mining|4B_non_price_requirement_stress_test|coverage_gap_fill", "trigger_type": "Stage4B-valuation-blowoff-overlay", "trigger_date": "2023-07-24", "evidence_available_at_that_date": "after the resource-bridge rerating, the vertical move into late-July 2023 became a valuation/positioning 4B overlay rather than a new positive Stage3 trigger.", "evidence_source": "stock-web 2023-07-24 c=642000 and 2023-07-26 h=764000; non-price overlay is valuation/positioning exhaustion after resource rerating.", "stage2_evidence_fields": [], "stage3_evidence_fields": [], "stage4b_evidence_fields": ["valuation_blowoff", "positioning_overheat"], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/005/005490/2023.csv", "profile_path": "atlas/symbol_profiles/005/005490.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "entry_date": "2023-07-24", "entry_price": 642000, "MFE_30D_pct": 19.0, "MFE_90D_pct": 19.0, "MFE_180D_pct": 19.0, "MFE_1Y_pct": 19.0, "MFE_2Y_pct": 19.0, "MAE_30D_pct": -13.55, "MAE_90D_pct": -22.12, "MAE_180D_pct": -36.4, "MAE_1Y_pct": -44.39, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2023-07-26", "peak_price": 764000, "drawdown_after_peak_pct": -46.07, "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": 0.89, "four_b_full_window_peak_proximity": 0.89, "four_b_timing_verdict": "good_full_window_4B_timing", "four_b_evidence_type": ["valuation_blowoff", "positioning_overheat"], "four_c_protection_label": "thesis_break_watch_only", "trigger_outcome_label": "4B overlay prevents rerating success from being re-bought as a new Stage3 signal", "current_profile_verdict": "current_profile_4B_too_late", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window", "same_entry_group_id": "R4L73_C16_POSCOHOLDINGS_20230331_LITHIUM_RESOURCE_BRIDGE_2023-07-24", "dedupe_for_aggregate": false, "aggregate_group_role": "4B_overlay_only", "is_new_independent_case": false, "reuse_reason": "same POSCO structural case used only for 4B overlay timing audit", "independent_evidence_weight": 0.0, "do_not_count_as_new_case": true}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R4L73_C16_POSCOHOLDINGS_20230331_LITHIUM_RESOURCE_BRIDGE", "trigger_id": "R4L73_C16_POSCOHOLDINGS_T2_4B", "symbol": "005490", "large_sector_id": "L4_MATERIALS_SPREAD_RESOURCE", "canonical_archetype_id": "C16_STRATEGIC_RESOURCE_POLICY_SUPPLY", "raw_component_scores_before": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 1, "revision_score": 0, "relative_strength_score": 3, "customer_quality_score": 1, "policy_or_regulatory_score": 2, "valuation_repricing_score": -3, "execution_risk_score": -2, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_before": 83, "stage_label_before": "Stage3-Yellow", "raw_component_scores_after": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 1, "revision_score": 0, "relative_strength_score": 3, "customer_quality_score": 1, "policy_or_regulatory_score": 2, "valuation_repricing_score": -3, "execution_risk_score": -2, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_after": 68, "stage_label_after": "Stage2-Actionable/4B-watch", "changed_components": ["c16_cashflow_bridge_bonus", "c16_policy_keyword_without_margin_guard", "c16_resource_theme_financing_risk_guard"], "component_delta_explanation": "Shadow profile promotes strategic-resource cases only when policy/resource optionality is connected to funding capacity, customer route, margin bridge, or production visibility; otherwise resource keyword + RS is capped or routed to 4B watch.", "MFE_90D_pct": 19.0, "MAE_90D_pct": -22.12, "score_return_alignment_label": "aligned", "current_profile_verdict": "current_profile_4B_too_late"}
{"row_type": "residual_contribution", "round": "R4", "loop": "73", "large_sector_id": "L4_MATERIALS_SPREAD_RESOURCE", "canonical_archetype_id": "C16_STRATEGIC_RESOURCE_POLICY_SUPPLY", "scheduled_round": "R4", "scheduled_loop": 73, "round_schedule_status": "valid", "round_sector_consistency": "pass", "new_independent_case_count": 4, "reused_case_count": 0, "new_symbol_count": 4, "same_archetype_new_symbol_count": 4, "same_archetype_new_trigger_family_count": 4, "new_trigger_family_count": 4, "positive_case_count": 2, "counterexample_count": 2, "current_profile_error_count": 4, "tested_existing_calibrated_axes": ["stage2_actionable_evidence_bonus", "price_only_blowoff_blocks_positive_stage", "full_4b_requires_non_price_evidence", "stage3_green_revision_min"], "residual_error_types_found": ["resource_keyword_false_positive", "policy_theme_without_cashflow_bridge", "valuation_blowoff_after_resource_rerating", "missed_structural_resource_bridge"], "loop_contribution_label": "canonical_archetype_rule_candidate", "do_not_propose_new_weight_delta": false, "diversity_score_summary": "new_symbols=4; counterexamples=2; new_trigger_families=4; duplicate_conflict=0"}
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
completed_round = R4
completed_loop = 73
next_round = R5
next_loop = 73
round_schedule_status = valid
round_sector_consistency = pass
```

## 28. Source Notes

Stock-web files consulted through the GitHub connector:

```text
- Songdaiki/stock-web atlas/manifest.json
- Songdaiki/stock-web atlas/schema.json
- atlas/symbol_profiles/005/005490.json
- atlas/symbol_profiles/025/025820.json
- atlas/symbol_profiles/001/001570.json
- atlas/symbol_profiles/047/047400.json
- atlas/symbol_profiles/011/011810.json for rejected/narrative-only STX contamination check
- atlas/ohlcv_tradable_by_symbol_year/005/005490/2023.csv
- atlas/ohlcv_tradable_by_symbol_year/025/025820/2024.csv
- atlas/ohlcv_tradable_by_symbol_year/001/001570/2023.csv
- atlas/ohlcv_tradable_by_symbol_year/001/001570/2024.csv
- atlas/ohlcv_tradable_by_symbol_year/047/047400/2023.csv
```

The MD is shadow-only research. It is not a current recommendation, not a live candidate scan, and not a production scoring patch.

