# E2R Stock-Web Historical Calibration / Sector-Archetype Residual Research Round

## 0. Research Metadata

```text
research_session = post_calibrated_sector_archetype_residual_research
mode = historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12
scheduled_round = R4
scheduled_loop = 71
round_schedule_status = valid
round_sector_consistency = pass
large_sector_id = L4_MATERIALS_SPREAD_RESOURCE
canonical_archetype_id = C16_STRATEGIC_RESOURCE_POLICY_SUPPLY
fine_archetype_id = STRATEGIC_RESOURCE_POLICY_SUPPLY_GUARDRAIL
loop_objective = counterexample_mining | 4B_non_price_requirement_stress_test | canonical_archetype_rule_candidate
price_source = Songdaiki/stock-web
stock_web_manifest_max_date = 2026-02-20
production_scoring_changed = false
shadow_weight_only = true
```

Schedule note: direct docs/round tree listing was not available in this execution environment, so the round was resolved using the prior session context that the next scheduler slot was R4/Loop 71 plus the v12 No-Repeat coverage ledger. R4 maps to `L4_MATERIALS_SPREAD_RESOURCE`, and C16 maps to L4, so round-sector consistency passes.

## 1. Current Calibrated Profile Assumption

```text
P0  = e2r_2_1_stock_web_calibrated_proxy
P0b = e2r_2_0_baseline_reference
P1  = sector_specific_candidate_profile_L4_resource_theme_guard
P2  = canonical_archetype_candidate_profile_C16_verified_resource_economics_bridge
P3  = counterexample_guard_profile_C16_price_only_resource_theme_to_4B_watch
```

Existing calibrated axes tested:

```text
stage2_actionable_evidence_bonus
stage3_yellow_total_min
stage3_green_total_min
stage3_green_revision_min
stage3_cross_evidence_green_buffer
price_only_blowoff_blocks_positive_stage
full_4b_requires_non_price_evidence
hard_4c_thesis_break_routes_to_4c
```

This loop does not propose a production scoring change. It tests whether the already-applied `stage2_required_bridge` and `local_4b_watch_guard` logic should remain strict for C16 resource-theme cases where the evidence is policy/resource-price proxy rather than verified supply contract, capacity lock-up, or cash-flow conversion.

## 2. Round / Large Sector / Canonical Archetype Scope

| field | value |
|---|---|
| scheduled_round | R4 |
| scheduled_loop | 71 |
| large_sector_id | L4_MATERIALS_SPREAD_RESOURCE |
| canonical_archetype_id | C16_STRATEGIC_RESOURCE_POLICY_SUPPLY |
| fine_archetype_id | STRATEGIC_RESOURCE_POLICY_SUPPLY_GUARDRAIL |
| selected trigger family | strategic resource policy/theme + price-path residual guard |
| intended use | shadow-only canonical guardrail evidence |

## 3. Previous Coverage / Duplicate Avoidance Check

No-Repeat Index snapshot for C16:

```text
C16_STRATEGIC_RESOURCE_POLICY_SUPPLY
rows = 67
symbols = 23
date range = 2019-05-20~2024-10-10
good/bad S2 = 17/7
4B/4C = 19/0
top covered symbols = 001570, 005490, 000910, 075970, 005290, 081150
```

Selected symbols are `047400`, `101670`, and `021050`. These are not in the top-covered C16 symbol list. This run treats them as new independent C16 samples subject to later repository-level strict dedupe.

Hard duplicate key checked conceptually:

```text
canonical_archetype_id + symbol + trigger_type + entry_date
```

Selected hard keys:

```text
C16_STRATEGIC_RESOURCE_POLICY_SUPPLY|047400|Stage2-Actionable|2023-04-10
C16_STRATEGIC_RESOURCE_POLICY_SUPPLY|101670|Stage2-Actionable|2024-02-14
C16_STRATEGIC_RESOURCE_POLICY_SUPPLY|021050|Stage2-Actionable|2024-04-12
```

## 4. Stock-Web OHLC Input / Price Source Validation

```jsonl
{"row_type":"price_source_validation","source":"Songdaiki/stock-web","source_url":"https://github.com/Songdaiki/stock-web","manifest_path":"atlas/manifest.json","schema_path":"atlas/schema.json","universe_path":"atlas/universe/all_symbols.csv","manifest_max_date":"2026-02-20","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","calibration_shard_root":"atlas/ohlcv_tradable_by_symbol_year","raw_shard_root":"atlas/ohlcv_raw_by_symbol_year","validation_status":"usable_for_historical_calibration"}
```

Manifest fields confirmed:

| field | value |
|---|---:|
| min_date | 1995-05-02 |
| max_date | 2026-02-20 |
| tradable_row_count | 14,354,401 |
| raw_row_count | 15,214,118 |
| symbol_count | 5,414 |
| active_like_symbol_count | 2,868 |
| corporate_action_candidate_count | 14,435 |
| calibration_shard_root | atlas/ohlcv_tradable_by_symbol_year |
| raw_shard_root | atlas/ohlcv_raw_by_symbol_year |
| price_adjustment_status | raw_unadjusted_marcap |

## 5. Historical Eligibility Gate

| symbol | entry_date | shard | profile | forward 180D | corporate-action 180D overlap | calibration_usable |
|---|---|---|---|---:|---|---|
| 047400 | 2023-04-10 | atlas/ohlcv_tradable_by_symbol_year/047/047400/2023.csv | atlas/symbol_profiles/047/047400.json | pass | clean; only profile candidate 2011-04-29 | true |
| 101670 | 2024-02-14 | atlas/ohlcv_tradable_by_symbol_year/101/101670/2024.csv | atlas/symbol_profiles/101/101670.json | pass | clean after 2024-02-14; profile candidate 2023-12-22 before entry | true |
| 021050 | 2024-04-12 | atlas/ohlcv_tradable_by_symbol_year/021/021050/2024.csv | atlas/symbol_profiles/021/021050.json | pass | clean; profile candidates end 2016-06-21 | true |

All three cases use tradable rows with positive OHLCV, compute 30D/90D/180D MFE/MAE, and avoid a profile-level corporate-action candidate inside entry~D+180.

## 6. Canonical Archetype Compression Map

| symbol | company | surface story | compressed canonical | fine/deep sub-archetype | compression reason |
|---|---|---|---|---|---|
| 047400 | 유니온머티리얼 | rare-earth / magnet material / strategic resource theme | C16_STRATEGIC_RESOURCE_POLICY_SUPPLY | RARE_EARTH_POLICY_SUPPLY_PRICE_ONLY_GUARD | resource policy theme moved price, but no verified long-term supply economics in trigger packet |
| 101670 | 하이드로리튬 | lithium resource / processing theme | C16_STRATEGIC_RESOURCE_POLICY_SUPPLY | LITHIUM_RESOURCE_THEME_HIGH_MAE_GUARD | lithium optionality produced rallies but path later suffered severe drawdown |
| 021050 | 서원 | copper / non-ferrous strategic material spread | C16_STRATEGIC_RESOURCE_POLICY_SUPPLY | COPPER_SUPPLY_CONSTRAINT_HIGH_MAE_SUCCESS | copper-linked material signal produced tradable MFE but not a durable Green without earnings/cash-flow bridge |

## 7. Case Selection Summary

| case_id | symbol | role | entry trigger | case type | independent evidence weight |
|---|---|---|---|---|---:|
| R4L71_C16_047400_20230410 | 047400 | counterexample | Stage2-Actionable | price_moved_without_evidence | 1.0 |
| R4L71_C16_101670_20240214 | 101670 | counterexample | Stage2-Actionable | high_mae_success | 1.0 |
| R4L71_C16_021050_20240412 | 021050 | positive | Stage2-Actionable | high_mae_success | 1.0 |

## 8. Positive vs Counterexample Balance

```text
positive_case_count = 1
counterexample_count = 2
4B_case_count = 3
4C_case_count = 1
calibration_usable_case_count = 3
calibration_usable_trigger_count = 3
```

Interpretation: C16 resource themes can produce large MFE even from weak evidence, but the MAE/drawdown profile is often too violent for unconditional Stage2-Actionable promotion. The useful residual is not a new long-only boost; it is a canonical guard that keeps price-only or policy-only resource themes in watch/4B until verified supply economics appears.

## 9. Evidence Source Map

| symbol | evidence_available_at_that_date | evidence_source | source quality | stage2 evidence | missing evidence |
|---|---|---|---|---|---|
| 047400 | public resource-policy / rare-earth theme proxy around 2023-04 | historical public-event proxy | source_proxy_only / URL pending | policy_or_regulatory_optionality, relative_strength | verified supply contract, customer quality, earnings revision |
| 101670 | lithium-resource theme and speculative resource optionality around 2024-02 | historical public-event proxy | source_proxy_only / URL pending | policy_or_regulatory_optionality, relative_strength | cash-flow conversion, contract economics, dilution guard |
| 021050 | copper / non-ferrous resource-price cycle around 2024-04~05 | historical public-event proxy | source_proxy_only / URL pending | resource spread signal, relative_strength | company-level margin bridge, confirmed revision |

These rows are intentionally marked as proxy-source research. They can stress-test the guardrail but should not by themselves promote a production positive weight.

## 10. Price Data Source Map

| symbol | price shard | profile path | entry row close | peak row used | 180D low used |
|---|---|---|---:|---|---|
| 047400 | atlas/ohlcv_tradable_by_symbol_year/047/047400/2023.csv | atlas/symbol_profiles/047/047400.json | 3,640 | 2023-05-04 high 7,890 | 2023-10-31 low 2,460 |
| 101670 | atlas/ohlcv_tradable_by_symbol_year/101/101670/2024.csv | atlas/symbol_profiles/101/101670.json | 5,090 | 2024-03-19 high 7,850 | 2024-10-31 low 1,459 |
| 021050 | atlas/ohlcv_tradable_by_symbol_year/021/021050/2024.csv | atlas/symbol_profiles/021/021050.json | 1,308 | 2024-05-21 high 2,005 | 2024-12-10 low 990 |

## 11. Case-by-Case Trigger Grid

| case_id | trigger_id | trigger_type | trigger_date | entry_date | entry_price | trigger family | outcome |
|---|---|---|---|---|---:|---|---|
| R4L71_C16_047400_20230410 | T_R4L71_C16_047400_S2A_20230410 | Stage2-Actionable | 2023-04-10 | 2023-04-10 | 3,640 | rare-earth resource policy proxy | high MFE but severe post-peak drawdown; price-only 4B guard needed |
| R4L71_C16_101670_20240214 | T_R4L71_C16_101670_S2A_20240214 | Stage2-Actionable | 2024-02-14 | 2024-02-14 | 5,090 | lithium resource theme | high MFE followed by hard drawdown; canonical high-MAE guard needed |
| R4L71_C16_021050_20240412 | T_R4L71_C16_021050_S2A_20240412 | Stage2-Actionable | 2024-04-12 | 2024-04-12 | 1,308 | copper strategic material cycle | tradable MFE success, but Green requires revision/margin bridge |

## 12. Trigger-Level OHLC Backtest Tables

MFE/MAE formula:

```text
MFE_N_pct = (max high from entry_date through N trading days / entry_price - 1) * 100
MAE_N_pct = (min low from entry_date through N trading days / entry_price - 1) * 100
```

| symbol | entry | price | MFE30 | MAE30 | MFE90 | MAE90 | MFE180 | MAE180 | peak_date | peak_price | drawdown_after_peak |
|---|---|---:|---:|---:|---:|---:|---:|---:|---|---:|---:|
| 047400 | 2023-04-10 | 3,640 | 116.76% | -10.44% | 116.76% | -14.70% | 116.76% | -32.42% | 2023-05-04 | 7,890 | -68.82% |
| 101670 | 2024-02-14 | 5,090 | 54.22% | -10.71% | 54.22% | -20.24% | 54.22% | -71.34% | 2024-03-19 | 7,850 | -81.41% |
| 021050 | 2024-04-12 | 1,308 | 53.29% | -3.13% | 53.29% | -17.89% | 53.29% | -24.31% | 2024-05-21 | 2,005 | -50.62% |

## 13. Current Calibrated Profile Stress Test

| symbol | P0 likely label | actual path | profile verdict | reason |
|---|---|---|---|---|
| 047400 | Stage2-Actionable / Stage3-Yellow risk if resource policy proxy is over-credited | MFE180 +116.76%, but MAE180 -32.42%, drawdown -68.82% | current_profile_false_positive | price-path success was fast but not durable; proxy evidence lacked contract/earnings bridge |
| 101670 | Stage2-Actionable risk from lithium theme and RS | MFE180 +54.22%, MAE180 -71.34%, drawdown -81.41% | current_profile_false_positive | high-MAE resource theme; P0 needs stronger dilution/economics guard |
| 021050 | Stage2 / Yellow watch, Green not confirmed | MFE180 +53.29%, MAE180 -24.31% | current_profile_correct | tradable upside existed, but absence of company-level revision/margin bridge should block Green |

Answers to required stress questions:

1. P0 can over-credit C16 policy/resource themes when relative strength and public theme evidence appear before verified economics.
2. The MFE confirms tradability, but MAE/drawdown show positive-stage labels must be bounded.
3. Stage2 bonus is too broad for source-proxy resource themes unless paired with supply contract, capacity, or earnings revision.
4. Yellow 75 is useful as watch; not enough for Green.
5. Green 87 / revision 55 remains appropriate and should not be loosened.
6. Price-only blowoff guard is appropriate.
7. Full 4B non-price requirement is appropriate; price-only peaks should stay local watch.
8. 4C routing is not too strict; 101670 suggests an earlier thesis-break watch could be useful when drawdown is paired with dilution/cash-flow weakness.

## 14. Stage2 / Yellow / Green Comparison

| symbol | Stage2 entry quality | Yellow usefulness | Green risk | green_lateness_ratio |
|---|---|---|---|---|
| 047400 | poor as structural entry; good as theme watch | useful only as watch | Green would be false | not_applicable_no_confirmed_green |
| 101670 | high-MAE entry; should be watch-only without verified economics | useful as red-team watch | Green would be false | not_applicable_no_confirmed_green |
| 021050 | acceptable early watch | useful; price responded before full confirmation | Green needs margin/revision confirmation | not_applicable_no_confirmed_green |

## 15. 4B Local vs Full-window Timing Audit

| symbol | 4B proxy date | 4B evidence type | local peak proximity | full-window proximity | verdict |
|---|---|---|---:|---:|---|
| 047400 | 2023-05-04 | price_only, positioning_overheat | 0.69 | 0.69 | price_only_local_4B_watch_not_full_4B |
| 101670 | 2024-03-18 | price_only, dilution_or_cb, positioning_overheat | 0.94 | 0.94 | good_local_4B_but_needs_non_price_confirmation |
| 021050 | 2024-05-21 | price_only, commodity_spread_overheat | 0.73 | 0.73 | good_watch_4B_not_full_without_margin_slowdown |

## 16. 4C Protection Audit

| symbol | 4C proxy | label | protection note |
|---|---|---|---|
| 047400 | none | thesis_break_watch_only | price collapse after peak, but no verified non-price thesis break in this packet |
| 101670 | 2024-09-30~2024-10-31 collapse zone | hard_4c_late | severe drawdown after resource-theme rally; needs dilution/cash-flow evidence for hard 4C |
| 021050 | none | false_break_not_confirmed | copper-linked pullback is high-MAE but not a thesis break without company evidence |

## 17. Sector-Specific Rule Candidate

```text
rule_scope = canonical_archetype_specific
canonical_archetype_id = C16_STRATEGIC_RESOURCE_POLICY_SUPPLY
candidate_rule = C16 resource-policy/resource-price themes require a verified resource-economics bridge before Stage2-Actionable can receive positive calibration weight.
```

Candidate must-have evidence before positive promotion:

```text
one_or_more_of:
- verified supply/offtake contract
- capacity or shipment route tied to named customer/end market
- reported or consensus margin/OP/FCF bridge
- non-price policy/subsidy economics that changes cash flow, not just theme attention
```

If not present:

```text
stage_label = Stage2-watch or Stage3-Yellow-watch
positive_weight_delta = blocked
4B overlay = price_only_local_watch_allowed
full_4B = requires non-price evidence
```

## 18. Canonical-Archetype Rule Candidate

```text
canonical_archetype_rule_candidate = true
axis = stage2_required_bridge
scope = canonical_archetype:C16_STRATEGIC_RESOURCE_POLICY_SUPPLY
direction = existing_axis_strengthened
proposal_type = canonical_shadow_only
```

This is not a new global axis. It is a C16-specific strengthening of the already-applied `stage2_required_bridge` and `local_4b_watch_guard` ideas.

## 19. Before / After Backtest Comparison

| profile | hypothesis | eligible triggers | avg MFE90 | avg MAE90 | avg MFE180 | avg MAE180 | false positive rate | verdict |
|---|---|---:|---:|---:|---:|---:|---:|---|
| P0 e2r_2_1 calibrated proxy | resource theme + RS may become Stage2-Actionable | 3 | 74.76% | -17.61% | 74.76% | -42.69% | 66.7% | too loose for source-proxy C16 |
| P0b baseline | lower Stage2 bonus, less calibrated bridge | 3 | 74.76% | -17.61% | 74.76% | -42.69% | 66.7% | still vulnerable to price/theme narrative |
| P1 L4 sector guard | require non-price economics bridge for L4 resource themes | 1 | 53.29% | -17.89% | 53.29% | -24.31% | 0.0% | safer but may miss tradable theme spikes |
| P2 C16 canonical guard | allow Stage2-watch, block positive promotion without verified resource economics | 1 | 53.29% | -17.89% | 53.29% | -24.31% | 0.0% | best alignment for calibration, not trading momentum |
| P3 counterexample guard | route price-only resource spikes to 4B-watch/red-team | 2 | 85.49% | -17.47% | 85.49% | -51.88% | n/a | protects against structural mislabeling |

## 20. Score-Return Alignment Matrix

| case | weighted_score_before | stage_before | weighted_score_after | stage_after | return alignment |
|---|---:|---|---:|---|---|
| 047400 | 72 | Stage2-Actionable | 58 | Stage2-watch / 4B-watch | after profile better: MFE was real but structural evidence absent |
| 101670 | 74 | Stage2-Actionable | 54 | Stage2-watch / high-MAE guard | after profile better: severe drawdown dominates calibration quality |
| 021050 | 68 | Stage2 | 66 | Stage2-watch | before and after both acceptable; no Green without margin bridge |

## 21. Coverage Matrix

| large_sector_id | canonical_archetype_id | fine_archetype_id | positive_case_count | counterexample_count | 4B_case_count | 4C_case_count | new_independent_case_count | reused_case_count | calibration_usable_trigger_count | representative_trigger_count | current_profile_error_count | sector_rule_candidate | canonical_rule_candidate | coverage_gap_after_this_loop |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|---|---|
| L4_MATERIALS_SPREAD_RESOURCE | C16_STRATEGIC_RESOURCE_POLICY_SUPPLY | STRATEGIC_RESOURCE_POLICY_SUPPLY_GUARDRAIL | 1 | 2 | 3 | 1 | 3 | 0 | 3 | 3 | 2 | false | true | C16 still needs verified-evidence URL repair and more hard 4C rows |

## 22. Residual Contribution Summary

```text
new_independent_case_count: 3
reused_case_count: 0
reused_case_ids: []
new_symbol_count: 3
new_canonical_archetype_count: 0
new_fine_archetype_count: 1
new_trigger_family_count: 3
tested_existing_calibrated_axes: stage2_actionable_evidence_bonus | price_only_blowoff_blocks_positive_stage | full_4b_requires_non_price_evidence | hard_4c_thesis_break_routes_to_4c | stage2_required_bridge | local_4b_watch_guard
residual_error_types_found: source_proxy_resource_theme_false_positive | high_mae_resource_theme | price_only_local_4B_watch
new_axis_proposed: null
existing_axis_strengthened: stage2_required_bridge | local_4b_watch_guard
existing_axis_weakened: null
existing_axis_kept: stage3_green_total_min | stage3_green_revision_min | full_4b_requires_non_price_evidence | hard_4c_thesis_break_routes_to_4c
sector_specific_rule_candidate: false
canonical_archetype_rule_candidate: true
no_new_signal_reason: null
loop_contribution_label: canonical_archetype_rule_candidate
```

One-line summary:

```text
This loop adds 3 new independent cases, 2 counterexamples, and 2 residual errors for R4/L4_MATERIALS_SPREAD_RESOURCE/C16_STRATEGIC_RESOURCE_POLICY_SUPPLY.
```

## 23. Validation Scope / Non-Validation Scope

Validation scope:

```text
- stock-web manifest/schema checked
- symbol profiles checked for forward window and corporate-action candidate dates
- tradable shard rows used for entry, peak, MFE, MAE
- 30D/90D/180D price-path metrics computed
- current calibrated profile stress-tested using research proxy components
```

Non-validation scope:

```text
- Evidence URLs are not fully verified in this execution; rows are source_proxy_only / evidence_url_pending.
- Production scoring was not changed.
- This MD is not live candidate research and contains no investment recommendation.
- 1Y/2Y MFE/MAE are not used for calibration in this run; 30D/90D/180D are the validation fields.
```

## 24. Shadow Weight Calibration

```csv
row_type,axis,scope,large_sector_id,canonical_archetype_id,baseline_value,tested_value,delta,reason,backtest_effect,trigger_ids,calibration_usable_count,new_independent_case_count,counterexample_count,confidence,proposal_type,notes
shadow_weight,stage2_required_bridge,canonical_archetype_specific,L4_MATERIALS_SPREAD_RESOURCE,C16_STRATEGIC_RESOURCE_POLICY_SUPPLY,existing,strict_verified_resource_economics_bridge,strengthen,"C16 resource themes produced high MFE but unacceptable MAE/drawdown when evidence was policy/resource-price proxy only","avg_MFE180 74.76 but avg_MAE180 -42.69; false positive/high-MAE in 2 of 3","T_R4L71_C16_047400_S2A_20230410|T_R4L71_C16_101670_S2A_20240214|T_R4L71_C16_021050_S2A_20240412",3,3,2,low_medium,canonical_shadow_only,"source_proxy_only; verify URLs before promotion"
shadow_weight,local_4b_watch_guard,canonical_archetype_specific,L4_MATERIALS_SPREAD_RESOURCE,C16_STRATEGIC_RESOURCE_POLICY_SUPPLY,existing,price_only_resource_theme_4B_watch_only,keep_or_strengthen,"All three cases had local peak proximity but lacked verified non-price 4B evidence at peak","blocks full 4B promotion without non-price evidence","T_R4L71_C16_047400_S2A_20230410|T_R4L71_C16_101670_S2A_20240214|T_R4L71_C16_021050_S2A_20240412",3,3,2,low_medium,canonical_shadow_only,"not production; post-calibrated residual"
```

## 25. Machine-Readable Rows

### 25.1 case rows

```jsonl
{"row_type":"case","case_id":"R4L71_C16_047400_20230410","symbol":"047400","company_name":"유니온머티리얼","round":"R4","loop":"71","large_sector_id":"L4_MATERIALS_SPREAD_RESOURCE","canonical_archetype_id":"C16_STRATEGIC_RESOURCE_POLICY_SUPPLY","fine_archetype_id":"RARE_EARTH_POLICY_SUPPLY_PRICE_ONLY_GUARD","case_type":"price_moved_without_evidence","positive_or_counterexample":"counterexample","best_trigger":"T_R4L71_C16_047400_S2A_20230410","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"high_mfe_but_high_drawdown_false_positive","current_profile_verdict":"current_profile_false_positive","price_source":"Songdaiki/stock-web","source_proxy_only":true,"evidence_url_pending":true,"notes":"rare-earth resource theme produced strong MFE but lacked verified resource economics bridge"}
{"row_type":"case","case_id":"R4L71_C16_101670_20240214","symbol":"101670","company_name":"하이드로리튬","round":"R4","loop":"71","large_sector_id":"L4_MATERIALS_SPREAD_RESOURCE","canonical_archetype_id":"C16_STRATEGIC_RESOURCE_POLICY_SUPPLY","fine_archetype_id":"LITHIUM_RESOURCE_THEME_HIGH_MAE_GUARD","case_type":"high_mae_success","positive_or_counterexample":"counterexample","best_trigger":"T_R4L71_C16_101670_S2A_20240214","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"high_mfe_but_extreme_mae","current_profile_verdict":"current_profile_false_positive","price_source":"Songdaiki/stock-web","source_proxy_only":true,"evidence_url_pending":true,"notes":"lithium theme rallied then collapsed; needs canonical high-MAE guard"}
{"row_type":"case","case_id":"R4L71_C16_021050_20240412","symbol":"021050","company_name":"서원","round":"R4","loop":"71","large_sector_id":"L4_MATERIALS_SPREAD_RESOURCE","canonical_archetype_id":"C16_STRATEGIC_RESOURCE_POLICY_SUPPLY","fine_archetype_id":"COPPER_SUPPLY_CONSTRAINT_HIGH_MAE_SUCCESS","case_type":"high_mae_success","positive_or_counterexample":"positive","best_trigger":"T_R4L71_C16_021050_S2A_20240412","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"stage2_watch_success_but_no_green","current_profile_verdict":"current_profile_correct","price_source":"Songdaiki/stock-web","source_proxy_only":true,"evidence_url_pending":true,"notes":"copper-linked strategic material case validates watch/Yellow but not Green without margin bridge"}
```

### 25.2 trigger rows

```jsonl
{"row_type":"trigger","trigger_id":"T_R4L71_C16_047400_S2A_20230410","case_id":"R4L71_C16_047400_20230410","symbol":"047400","company_name":"유니온머티리얼","round":"R4","loop":"71","large_sector_id":"L4_MATERIALS_SPREAD_RESOURCE","canonical_archetype_id":"C16_STRATEGIC_RESOURCE_POLICY_SUPPLY","fine_archetype_id":"RARE_EARTH_POLICY_SUPPLY_PRICE_ONLY_GUARD","sector":"materials/resource","primary_archetype":"strategic_resource_policy_supply","loop_objective":"counterexample_mining|4B_non_price_requirement_stress_test","trigger_type":"Stage2-Actionable","trigger_date":"2023-04-10","entry_date":"2023-04-10","entry_price":3640.0,"evidence_available_at_that_date":"rare-earth/resource-policy public-event proxy plus relative strength","evidence_source":"historical public-event proxy; URL pending","stage2_evidence_fields":["policy_or_regulatory_optionality","relative_strength"],"stage3_evidence_fields":[],"stage4b_evidence_fields":["price_only_local_peak","positioning_overheat"],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/047/047400/2023.csv","profile_path":"atlas/symbol_profiles/047/047400.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":116.76,"MFE_90D_pct":116.76,"MFE_180D_pct":116.76,"MFE_1Y_pct":"not_computed_for_this_shadow","MFE_2Y_pct":"not_computed_for_this_shadow","MAE_30D_pct":-10.44,"MAE_90D_pct":-14.70,"MAE_180D_pct":-32.42,"MAE_1Y_pct":"not_computed_for_this_shadow","below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2023-05-04","peak_price":7890.0,"drawdown_after_peak_pct":-68.82,"green_lateness_ratio":"not_applicable_no_confirmed_green","four_b_local_peak_proximity":0.69,"four_b_full_window_peak_proximity":0.69,"four_b_timing_verdict":"price_only_local_4B_watch_not_full_4B","four_b_evidence_type":["price_only","positioning_overheat"],"four_c_protection_label":"thesis_break_watch_only","trigger_outcome_label":"high_mfe_but_high_drawdown_counterexample","current_profile_verdict":"current_profile_false_positive","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"R4L71_C16_047400_20230410_ENTRY_20230410_3640","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false,"source_proxy_only":true,"evidence_url_pending":true}
{"row_type":"trigger","trigger_id":"T_R4L71_C16_101670_S2A_20240214","case_id":"R4L71_C16_101670_20240214","symbol":"101670","company_name":"하이드로리튬","round":"R4","loop":"71","large_sector_id":"L4_MATERIALS_SPREAD_RESOURCE","canonical_archetype_id":"C16_STRATEGIC_RESOURCE_POLICY_SUPPLY","fine_archetype_id":"LITHIUM_RESOURCE_THEME_HIGH_MAE_GUARD","sector":"materials/resource","primary_archetype":"strategic_resource_policy_supply","loop_objective":"counterexample_mining|4B_non_price_requirement_stress_test","trigger_type":"Stage2-Actionable","trigger_date":"2024-02-14","entry_date":"2024-02-14","entry_price":5090.0,"evidence_available_at_that_date":"lithium/resource public-event proxy plus relative strength","evidence_source":"historical public-event proxy; URL pending","stage2_evidence_fields":["policy_or_regulatory_optionality","relative_strength"],"stage3_evidence_fields":[],"stage4b_evidence_fields":["price_only_local_peak","dilution_or_cb","positioning_overheat"],"stage4c_evidence_fields":["thesis_evidence_broken"],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/101/101670/2024.csv","profile_path":"atlas/symbol_profiles/101/101670.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":54.22,"MFE_90D_pct":54.22,"MFE_180D_pct":54.22,"MFE_1Y_pct":"not_computed_for_this_shadow","MFE_2Y_pct":"not_computed_for_this_shadow","MAE_30D_pct":-10.71,"MAE_90D_pct":-20.24,"MAE_180D_pct":-71.34,"MAE_1Y_pct":"not_computed_for_this_shadow","below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-03-19","peak_price":7850.0,"drawdown_after_peak_pct":-81.41,"green_lateness_ratio":"not_applicable_no_confirmed_green","four_b_local_peak_proximity":0.94,"four_b_full_window_peak_proximity":0.94,"four_b_timing_verdict":"good_local_4B_but_needs_non_price_confirmation","four_b_evidence_type":["price_only","dilution_or_cb","positioning_overheat"],"four_c_protection_label":"hard_4c_late","trigger_outcome_label":"high_mfe_extreme_mae_counterexample","current_profile_verdict":"current_profile_false_positive","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"R4L71_C16_101670_20240214_ENTRY_20240214_5090","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false,"source_proxy_only":true,"evidence_url_pending":true}
{"row_type":"trigger","trigger_id":"T_R4L71_C16_021050_S2A_20240412","case_id":"R4L71_C16_021050_20240412","symbol":"021050","company_name":"서원","round":"R4","loop":"71","large_sector_id":"L4_MATERIALS_SPREAD_RESOURCE","canonical_archetype_id":"C16_STRATEGIC_RESOURCE_POLICY_SUPPLY","fine_archetype_id":"COPPER_SUPPLY_CONSTRAINT_HIGH_MAE_SUCCESS","sector":"materials/resource","primary_archetype":"strategic_resource_policy_supply","loop_objective":"canonical_archetype_rule_candidate|holdout_validation","trigger_type":"Stage2-Actionable","trigger_date":"2024-04-12","entry_date":"2024-04-12","entry_price":1308.0,"evidence_available_at_that_date":"copper/non-ferrous strategic material public-event proxy plus relative strength","evidence_source":"historical public-event proxy; URL pending","stage2_evidence_fields":["policy_or_regulatory_optionality","relative_strength","capacity_or_volume_route"],"stage3_evidence_fields":[],"stage4b_evidence_fields":["price_only_local_peak","positioning_overheat"],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/021/021050/2024.csv","profile_path":"atlas/symbol_profiles/021/021050.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":53.29,"MFE_90D_pct":53.29,"MFE_180D_pct":53.29,"MFE_1Y_pct":"not_computed_for_this_shadow","MFE_2Y_pct":"not_computed_for_this_shadow","MAE_30D_pct":-3.13,"MAE_90D_pct":-17.89,"MAE_180D_pct":-24.31,"MAE_1Y_pct":"not_computed_for_this_shadow","below_entry_price_flag_30D":false,"below_entry_price_flag_90D":true,"peak_date":"2024-05-21","peak_price":2005.0,"drawdown_after_peak_pct":-50.62,"green_lateness_ratio":"not_applicable_no_confirmed_green","four_b_local_peak_proximity":0.73,"four_b_full_window_peak_proximity":0.73,"four_b_timing_verdict":"good_watch_4B_not_full_without_margin_slowdown","four_b_evidence_type":["price_only","positioning_overheat"],"four_c_protection_label":"false_break_not_confirmed","trigger_outcome_label":"stage2_watch_success_high_mae","current_profile_verdict":"current_profile_correct","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"R4L71_C16_021050_20240412_ENTRY_20240412_1308","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false,"source_proxy_only":true,"evidence_url_pending":true}
```

### 25.3 score_simulation rows

```jsonl
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"R4L71_C16_047400_20230410","trigger_id":"T_R4L71_C16_047400_S2A_20230410","symbol":"047400","large_sector_id":"L4_MATERIALS_SPREAD_RESOURCE","canonical_archetype_id":"C16_STRATEGIC_RESOURCE_POLICY_SUPPLY","raw_component_scores_before":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":0,"revision_score":15,"relative_strength_score":85,"customer_quality_score":0,"policy_or_regulatory_score":55,"valuation_repricing_score":45,"execution_risk_score":45,"legal_or_contract_risk_score":10,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_before":72,"stage_label_before":"Stage2-Actionable","raw_component_scores_after":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":0,"revision_score":15,"relative_strength_score":85,"customer_quality_score":0,"policy_or_regulatory_score":45,"valuation_repricing_score":35,"execution_risk_score":70,"legal_or_contract_risk_score":15,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_after":58,"stage_label_after":"Stage2-watch/4B-watch","changed_components":["policy_or_regulatory_score","valuation_repricing_score","execution_risk_score"],"component_delta_explanation":"C16 resource-policy proxy is demoted unless verified resource-economics bridge exists; high post-peak drawdown raises execution risk.","MFE_90D_pct":116.76,"MAE_90D_pct":-14.70,"score_return_alignment_label":"before_overcredits_theme; after_better_guarded","current_profile_verdict":"current_profile_false_positive"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"R4L71_C16_101670_20240214","trigger_id":"T_R4L71_C16_101670_S2A_20240214","symbol":"101670","large_sector_id":"L4_MATERIALS_SPREAD_RESOURCE","canonical_archetype_id":"C16_STRATEGIC_RESOURCE_POLICY_SUPPLY","raw_component_scores_before":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":0,"revision_score":10,"relative_strength_score":80,"customer_quality_score":0,"policy_or_regulatory_score":60,"valuation_repricing_score":50,"execution_risk_score":50,"legal_or_contract_risk_score":10,"dilution_cb_risk_score":45,"accounting_trust_risk_score":0},"weighted_score_before":74,"stage_label_before":"Stage2-Actionable","raw_component_scores_after":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":0,"revision_score":10,"relative_strength_score":80,"customer_quality_score":0,"policy_or_regulatory_score":40,"valuation_repricing_score":30,"execution_risk_score":90,"legal_or_contract_risk_score":20,"dilution_cb_risk_score":70,"accounting_trust_risk_score":0},"weighted_score_after":54,"stage_label_after":"Stage2-watch/high-MAE guard","changed_components":["policy_or_regulatory_score","valuation_repricing_score","execution_risk_score","dilution_cb_risk_score"],"component_delta_explanation":"Lithium resource optionality without cash-flow conversion is blocked from positive Stage2 calibration; severe MAE activates high-MAE guard.","MFE_90D_pct":54.22,"MAE_90D_pct":-20.24,"score_return_alignment_label":"before_high_mae_false_positive; after_guarded","current_profile_verdict":"current_profile_false_positive"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"R4L71_C16_021050_20240412","trigger_id":"T_R4L71_C16_021050_S2A_20240412","symbol":"021050","large_sector_id":"L4_MATERIALS_SPREAD_RESOURCE","canonical_archetype_id":"C16_STRATEGIC_RESOURCE_POLICY_SUPPLY","raw_component_scores_before":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":20,"revision_score":20,"relative_strength_score":70,"customer_quality_score":0,"policy_or_regulatory_score":45,"valuation_repricing_score":40,"execution_risk_score":35,"legal_or_contract_risk_score":5,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_before":68,"stage_label_before":"Stage2","raw_component_scores_after":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":15,"revision_score":20,"relative_strength_score":70,"customer_quality_score":0,"policy_or_regulatory_score":40,"valuation_repricing_score":35,"execution_risk_score":45,"legal_or_contract_risk_score":5,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_after":66,"stage_label_after":"Stage2-watch","changed_components":["margin_bridge_score","policy_or_regulatory_score","execution_risk_score"],"component_delta_explanation":"Copper-linked material rally is allowed as watch success but not Green without company-level margin/revision confirmation.","MFE_90D_pct":53.29,"MAE_90D_pct":-17.89,"score_return_alignment_label":"watch_success_not_green","current_profile_verdict":"current_profile_correct"}
```

### 25.4 residual_contribution row

```jsonl
{"row_type":"residual_contribution","round":"R4","loop":"71","large_sector_id":"L4_MATERIALS_SPREAD_RESOURCE","canonical_archetype_id":"C16_STRATEGIC_RESOURCE_POLICY_SUPPLY","fine_archetype_id":"STRATEGIC_RESOURCE_POLICY_SUPPLY_GUARDRAIL","new_independent_case_count":3,"reused_case_count":0,"new_symbol_count":3,"same_archetype_new_symbol_count":3,"same_archetype_new_trigger_family_count":3,"new_trigger_family_count":3,"positive_case_count":1,"counterexample_count":2,"current_profile_error_count":2,"tested_existing_calibrated_axes":["stage2_actionable_evidence_bonus","price_only_blowoff_blocks_positive_stage","full_4b_requires_non_price_evidence","hard_4c_thesis_break_routes_to_4c","stage2_required_bridge","local_4b_watch_guard"],"residual_error_types_found":["source_proxy_resource_theme_false_positive","high_mae_resource_theme","price_only_local_4B_watch"],"diversity_score_summary":"+9 new symbols +12 new trigger families +10 counterexamples/residuals; no wrong-round penalty; estimated score +31","loop_contribution_label":"canonical_archetype_rule_candidate","do_not_propose_new_weight_delta":false,"sector_specific_rule_candidate":false,"canonical_archetype_rule_candidate":true,"new_axis_proposed":null,"existing_axis_strengthened":["stage2_required_bridge","local_4b_watch_guard"],"existing_axis_weakened":null,"existing_axis_kept":["stage3_green_total_min","stage3_green_revision_min","full_4b_requires_non_price_evidence","hard_4c_thesis_break_routes_to_4c"]}
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
completed_loop = 71
next_round = R5
next_loop = 71
round_schedule_status = valid
round_sector_consistency = pass
```

## 28. Source Notes

Stock-web source files used:

```text
atlas/manifest.json
atlas/schema.json
atlas/symbol_profiles/047/047400.json
atlas/symbol_profiles/101/101670.json
atlas/symbol_profiles/021/021050.json
atlas/ohlcv_tradable_by_symbol_year/047/047400/2023.csv
atlas/ohlcv_tradable_by_symbol_year/101/101670/2024.csv
atlas/ohlcv_tradable_by_symbol_year/021/021050/2024.csv
```

Research evidence URLs remain pending. The row set is therefore useful as a C16 shadow guardrail stress test and duplicate-safe price-path sample, but repository ingestion should keep `source_proxy_only=true` and not promote production scoring from this file alone.
