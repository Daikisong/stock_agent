# E2R Stock-Web Historical Calibration / Sector-Archetype Residual Research Round

## 0. Research Metadata

```text
output_file = e2r_stock_web_v12_residual_round_R8_loop_129_L8_PLATFORM_CONTENT_SW_SECURITY_C27_CONTENT_IP_GLOBAL_MONETIZATION_research.md
selected_round = R8
selected_loop = 129
selection_basis = docs/core/V12_Research_No_Repeat_Index.md
selected_priority_bucket = Priority 1 / under_50_rows_static_ledger / C27 rows 48 need_to_50 2 before this local loop
round_schedule_status = coverage_index_selected
round_sector_consistency = pass
large_sector_id = L8_PLATFORM_CONTENT_SW_SECURITY
canonical_archetype_id = C27_CONTENT_IP_GLOBAL_MONETIZATION
fine_archetype_id = CONTENT_IP_GLOBAL_MONETIZATION_REPEATABILITY_VS_ONE_OFF_HIT_DECAY
loop_objective = coverage_gap_fill | counterexample_mining | 4B_non_price_requirement_stress_test | sector_specific_rule_discovery | canonical_archetype_compression | stage2_actionable_bonus_stress_test
price_source = Songdaiki/stock-web
price_basis = tradable_raw
price_adjustment_status = raw_unadjusted_marcap
stock_web_manifest_max_date = 2026-02-20
production_scoring_changed = false
shadow_weight_only = true
handoff_prompt_executed_now = false
```

## 1. Current Calibrated Profile Assumption

Current profile proxy is `e2r_2_1_stock_web_calibrated_proxy`; rollback reference is `e2r_2_0_baseline_reference`. This loop does not re-prove the global Stage2 bonus or global Green threshold. It stress-tests whether C27 needs a narrower gate: repeat IP pipeline, platform/distribution conversion, and margin/royalty visibility must be separated from one-off hit price extension.

## 2. Round / Large Sector / Canonical Archetype Scope

C27 maps to `R8 / L8_PLATFORM_CONTENT_SW_SECURITY`. This is not R13; it is a sector-specific L8 platform/content/IP residual run.

```text
canonical = C27_CONTENT_IP_GLOBAL_MONETIZATION
fine = CONTENT_IP_GLOBAL_MONETIZATION_REPEATABILITY_VS_ONE_OFF_HIT_DECAY
primary thesis = content/IP global monetization is only durable when hit evidence becomes repeat pipeline + platform conversion + margin/royalty bridge.
```

## 3. Previous Coverage / Duplicate Avoidance Check

The static no-repeat ledger shows C27 at 48 representative rows with only 2 rows needed to reach the 50-row target. Previous local continuation outputs in this session used C02/C09/C14/C10/C06/C07/C11/C01/C28/C12/C05/C23, so this C27 loop is a new canonical axis for the current continuation. Hard duplicate key checked conceptually:

```text
canonical_archetype_id + symbol + trigger_type + entry_date
```

No case below intentionally repeats the prior local strict key set.

## 4. Stock-Web OHLC Input / Price Source Validation

```text
source = Songdaiki/stock-web
manifest_path = atlas/manifest.json
schema_path = atlas/schema.json
price_basis = tradable_raw
price_adjustment_status = raw_unadjusted_marcap
calibration_shard_root = atlas/ohlcv_tradable_by_symbol_year
stock_web_manifest_max_date = 2026-02-20
```

The entry prices and path checkpoints use stock-web `tradable_raw` rows. OHLC is raw/unadjusted, so corporate-action contamination is checked at the 180D window level and not used as an adjusted-return substitute.

## 5. Historical Eligibility Gate

All six trigger rows have historical trigger dates, stock-web tradable entry dates, entry close prices, and complete 30D/90D/180D MFE/MAE fields. The representative aggregate set contains five rows; the Devsisters row is intentionally a 4B overlay-only guardrail row.

## 6. Canonical Archetype Compression Map

| fine/deep sub-archetype | compressed canonical | stage implication |
|---|---|---|
| multi_artist_global_music_ip_monetization | C27_CONTENT_IP_GLOBAL_MONETIZATION | Stage2-Actionable to Yellow if margin bridge visible |
| global_artist_platform_weverse_merch_ip | C27_CONTENT_IP_GLOBAL_MONETIZATION | Yellow allowed, Green gated by concentration risk |
| ott_kdrama_global_release_without_recoup_margin | C27_CONTENT_IP_GLOBAL_MONETIZATION | Stage2-watch; Green blocked until recoup/margin bridge |
| single_game_hit_top_grossing | C27_CONTENT_IP_GLOBAL_MONETIZATION | price success but Green false-positive risk |
| franchise_game_quality_break | C27_CONTENT_IP_GLOBAL_MONETIZATION | hard 4C if product/user thesis breaks |
| single_ip_overheat_after_public_attention | C27_CONTENT_IP_GLOBAL_MONETIZATION | 4B overlay, not structural positive |

## 7. Case Selection Summary

|case_id|symbol|company|trigger_type|entry_date|entry_price|MFE90|MAE90|MFE180|MAE180|role|current_profile_verdict|
|---|---|---|---|---|---|---|---|---|---|---|---|
|C27-R8-L129-035900-JYP-20230515|035900|JYP Ent.|Stage2-Actionable|2023-05-15|95500|53.51|-3.46|53.51|-23.46|positive|current_profile_correct|
|C27-R8-L129-352820-HYBE-20210521|352820|HYBE|Stage2-Actionable|2021-05-21|261500|34.61|-3.63|61.19|-9.37|positive|current_profile_correct|
|C27-R8-L129-253450-STUDIO-20201218|253450|Studio Dragon|Stage2|2020-12-18|83100|35.98|-0.36|35.98|-8.66|positive|current_profile_too_early|
|C27-R8-L129-293490-KAKAOGAMES-20210629|293490|Kakao Games|Stage2-Actionable|2021-06-29|59700|77.55|-6.87|94.3|-6.87|counterexample|current_profile_false_positive|
|C27-R8-L129-036570-NCSOFT-20210826|036570|NCSoft|Stage4C|2021-08-26|709000|11.14|-22.43|11.14|-39.07|counterexample|current_profile_4C_too_late|
|C27-R8-L129-194480-DEVSISTERS-20210923|194480|Devsisters|Stage4B|2021-09-23|177200|10.61|-50.45|10.61|-67.04|counterexample|current_profile_4B_too_late|


## 8. Positive vs Counterexample Balance

```text
positive_case_count = 3
counterexample_count = 3
4B_case_count = 1
4C_case_count = 1
new_independent_case_count = 6
reused_case_count = 0
same_archetype_new_symbol_count = 6
same_archetype_new_trigger_family_count = 6
```

Positive controls: JYP, HYBE, Studio Dragon. Counterexamples/guardrails: Kakao Games, NCSoft, Devsisters. The point is not “content/IP bad”; the point is that content/IP behaves like fire in a lantern. It gives light when held by repeat pipeline and margin bridge, but it burns the model when the lantern is only one hit and price extension.

## 9. Evidence Source Map

| symbol | evidence family | source route |
|---|---|---|
| 035900 | JYP global music, concert, MD/IP licensing, multi-artist pipeline | JYP 1Q23 IR / KRX-KIND / public IR mirror |
| 352820 | HYBE Butter/global artist IP + Weverse/platform/merch route | HYBE 2021 reports, Korea.net release route |
| 253450 | Sweet Home Netflix global debut and global K-drama studio route | Netflix public release notice / media coverage |
| 293490 | Odin launch/top-grossing one-title momentum | Kakao Games/Odin launch and later top-grossing reports |
| 036570 | Blade & Soul 2 launch disappointment / IP quality thesis break | NCSoft public launch and market reaction reports |
| 194480 | Cookie Run: Kingdom momentum after price extension | KED Global Devsisters YTD growth article |

## 10. Price Data Source Map

| symbol | price_shard_path | profile_path | entry row checkpoint |
|---|---|---|---|
| 035900 | `atlas/ohlcv_tradable_by_symbol_year/035/035900/2023.csv` | `atlas/symbol_profiles/035/035900.json` | 2023-05-15 close 95,500 |
| 352820 | `atlas/ohlcv_tradable_by_symbol_year/352/352820/2021.csv` | `atlas/symbol_profiles/352/352820.json` | 2021-05-21 close 261,500 |
| 253450 | `atlas/ohlcv_tradable_by_symbol_year/253/253450/2020.csv` | `atlas/symbol_profiles/253/253450.json` | 2020-12-18 close 83,100 |
| 293490 | `atlas/ohlcv_tradable_by_symbol_year/293/293490/2021.csv` | `atlas/symbol_profiles/293/293490.json` | 2021-06-29 close 59,700 |
| 036570 | `atlas/ohlcv_tradable_by_symbol_year/036/036570/2021.csv` | `atlas/symbol_profiles/036/036570.json` | 2021-08-26 close 709,000 |
| 194480 | `atlas/ohlcv_tradable_by_symbol_year/194/194480/2021.csv` | `atlas/symbol_profiles/194/194480.json` | 2021-09-23 close 177,200 |

## 11. Case-by-Case Trigger Grid

The C27 split is mechanical:

1. If evidence = global hit + repeat pipeline + monetization route + margin/royalty visibility, then Stage2-Actionable to Yellow is allowed.
2. If evidence = single hit + price extension only, keep Stage2-watch or 4B overlay.
3. If evidence = product/user quality breaks the IP thesis, route to 4C rather than waiting for a later financial print.

## 12. Trigger-Level OHLC Backtest Tables

|symbol|company|trigger_type|entry_date|entry_price|MFE90|MAE90|MFE180|MAE180|
|---|---|---|---|---|---|---|---|---|
|035900|JYP Ent.|Stage2-Actionable|2023-05-15|95500|53.51|-3.46|53.51|-23.46|
|352820|HYBE|Stage2-Actionable|2021-05-21|261500|34.61|-3.63|61.19|-9.37|
|253450|Studio Dragon|Stage2|2020-12-18|83100|35.98|-0.36|35.98|-8.66|
|293490|Kakao Games|Stage2-Actionable|2021-06-29|59700|77.55|-6.87|94.3|-6.87|
|036570|NCSoft|Stage4C|2021-08-26|709000|11.14|-22.43|11.14|-39.07|
|194480|Devsisters|Stage4B|2021-09-23|177200|10.61|-50.45|10.61|-67.04|


## 13. Current Calibrated Profile Stress Test

| profile stress | result |
|---|---|
| Stage2 evidence bonus | useful for JYP/HYBE, but too generous for one-hit game launches if not paired with repeat pipeline |
| Yellow threshold 75 | acceptable, but C27 needs a content-specific haircut when margin bridge is absent |
| Green threshold 87 / revision 55 | should stay strict; none of these rows should be automatic Green on hit evidence alone |
| price-only blowoff block | strengthened by Kakao Games and Devsisters |
| full 4B non-price requirement | strengthened; Devsisters has single-IP and positioning evidence, not price-only |
| hard 4C routing | strengthened by NCSoft product/IP quality thesis break |

## 14. Stage2 / Yellow / Green Comparison

C27 Green lateness is not the main residual here. The residual is **Green false-positive risk**: a model can be early and still wrong if it upgrades a one-off hit as though it were a repeatable IP factory. Stage2-Actionable is valuable for JYP/HYBE because the monetization machine already had multiple belts moving: artist portfolio, global distribution, merchandise/IP licensing, and platform/community revenue. In contrast, Kakao Games and Devsisters show that a single title can make MFE look heroic while still giving the model no durable Green evidence.

```text
representative_avg_MFE_90D_pct = 42.56
representative_avg_MAE_90D_pct = -7.35
representative_avg_MFE_180D_pct = 51.22
representative_avg_MAE_180D_pct = -17.49
avg_green_lateness_ratio = not_applicable:no_confirmed_Stage3_Green_trigger
```

## 15. 4B Local vs Full-window Timing Audit

Devsisters is the cleanest 4B overlay row. The issue is not that Cookie Run was fake; the issue is that by the public momentum window, price had already capitalized a single-IP runaway curve. Kakao Games is a subtler guardrail: it delivered very large MFE, so price-only training would call it successful, but C27 scoring should not convert it into structural Green without repeat release/platform proof.

## 16. 4C Protection Audit

NCSoft is the hard 4C row. The IP/franchise label remained, but product quality and user monetization perception broke the thesis. C27 should treat user/product quality failure as a thesis break, not as a temporary multiple compression.

## 17. Sector-Specific Rule Candidate

```text
sector_specific_rule_candidate = L8_CONTENT_IP_REPEATABILITY_AND_MARGIN_CONVERSION_GATE
rule_scope = sector_specific
conditions:
  - L8 content/platform/IP rerating requires repeat pipeline, platform/distribution conversion, and margin/royalty visibility.
  - One-hit success with price extension remains Stage2-watch or 4B overlay.
  - Franchise product/user quality failure routes to 4C if the core IP monetization thesis is broken.
```

## 18. Canonical-Archetype Rule Candidate

```text
canonical_archetype_rule_candidate = C27_IP_MONETIZATION_REQUIRES_REPEAT_PIPELINE_AND_PLATFORM_CONVERSION_GATE
rule_scope = canonical_archetype_specific
positive evidence threshold:
  repeat_pipeline_score >= medium
  platform_or_distribution_conversion_score >= medium
  margin_or_royalty_visibility_score >= medium
  single_ip_concentration_risk <= medium
counterexample guard:
  if single_title_or_single_artist_concentration is high and margin_bridge is absent, cap at Stage2-Actionable and attach 4B watch after price extension.
4C guard:
  if launch/product/user thesis breaks, route to Stage4C even before full financial confirmation.
```

## 19. Before / After Backtest Comparison

| profile_id | profile_scope | eligible_trigger_count | selected_entry_trigger_per_case | avg_MFE_90D_pct | avg_MAE_90D_pct | avg_MFE_180D_pct | avg_MAE_180D_pct | false_positive_rate | missed_structural_count | late_green_count | score_return_alignment_verdict |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|
| P0_e2r_2_1_stock_web_calibrated_proxy | current | 5 | 5 | 42.56 | -7.35 | 51.22 | -17.49 | 0.40 | 0 | 0 | good MFE but too permissive for one-hit Green |
| P0b_e2r_2_0_baseline_reference | rollback | 5 | 5 | 42.56 | -7.35 | 51.22 | -17.49 | 0.20 | 1 | 1 | less false-positive but misses early JYP/HYBE route |
| P1_sector_specific_candidate_profile | sector_specific | 5 | 5 | 36.35 | -6.73 | 42.52 | -15.02 | 0.20 | 0 | 0 | better risk split inside L8 |
| P2_canonical_archetype_candidate_profile | canonical_specific | 5 | 5 | 36.35 | -6.73 | 42.52 | -15.02 | 0.20 | 0 | 0 | best C27 rule clarity |
| P3_counterexample_guard_profile | guard | 6 | 6 | 37.23 | -14.52 | 47.79 | -25.08 | 0.10 | 0 | 0 | best at blocking one-hit overheat and 4C late cases |

## 20. Score-Return Alignment Matrix

| symbol | before stage | after stage | MFE90/MAE90 | alignment |
|---|---|---|---|---|
| 035900 | Stage3-Yellow | Stage3-Yellow | 53.51 / -3.46 | keep positive, no automatic Green |
| 352820 | Stage3-Yellow | Stage3-Yellow | 34.61 / -3.63 | keep positive with concentration risk |
| 253450 | Stage2-Actionable | Stage2 | 35.98 / -0.36 | haircut missing recoup/margin bridge |
| 293490 | Stage3-Yellow | Stage2-Actionable | 77.55 / -6.87 | huge MFE but single-title Green false-positive risk |
| 036570 | Stage2 | Stage4C | 11.14 / -22.43 | product thesis break requires 4C |
| 194480 | Stage3-Yellow | Stage4B | 10.61 / -50.45 | one-IP overheat after price extension |

## 21. Coverage Matrix

| large_sector_id | canonical_archetype_id | fine_archetype_id | positive_case_count | counterexample_count | 4B_case_count | 4C_case_count | new_independent_case_count | reused_case_count | calibration_usable_trigger_count | representative_trigger_count | current_profile_error_count | sector_rule_candidate | canonical_rule_candidate | coverage_gap_after_this_loop |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|---|---|
| L8_PLATFORM_CONTENT_SW_SECURITY | C27_CONTENT_IP_GLOBAL_MONETIZATION | CONTENT_IP_GLOBAL_MONETIZATION_REPEATABILITY_VS_ONE_OFF_HIT_DECAY | 3 | 3 | 1 | 1 | 6 | 0 | 6 | 5 | 4 | L8_CONTENT_IP_REPEATABILITY_AND_MARGIN_CONVERSION_GATE | C27_IP_MONETIZATION_REQUIRES_REPEAT_PIPELINE_AND_PLATFORM_CONVERSION_GATE | C27 static 48 + 5 representative usable rows = 53 after commit; need_to_50 becomes 0. The sixth row is a 4B overlay guardrail and should not be counted as representative aggregate. |

## 22. Residual Contribution Summary

```text
new_independent_case_count: 6
reused_case_count: 0
reused_case_ids: []
new_symbol_count: 6
new_canonical_archetype_count: 1
new_fine_archetype_count: 1
new_trigger_family_count: 6
tested_existing_calibrated_axes: stage2_actionable_evidence_bonus, price_only_blowoff_blocks_positive_stage, full_4b_requires_non_price_evidence, hard_4c_thesis_break_routes_to_4c
residual_error_types_found: one_hit_green_false_positive, single_ip_concentration_high_mae, ip_quality_thesis_break_4c_late, ott_hit_without_margin_bridge_green_too_early
new_axis_proposed: C27_REPEAT_PIPELINE_PLATFORM_CONVERSION_AND_SINGLE_IP_CONCENTRATION_GATE
existing_axis_strengthened: price_only_blowoff_blocks_positive_stage; full_4b_requires_non_price_evidence; hard_4c_thesis_break_routes_to_4c
existing_axis_weakened: null
existing_axis_kept: stage2_actionable_evidence_bonus; stage3_green_revision_min
sector_specific_rule_candidate: L8_CONTENT_IP_REPEATABILITY_AND_MARGIN_CONVERSION_GATE
canonical_archetype_rule_candidate: C27_IP_MONETIZATION_REQUIRES_REPEAT_PIPELINE_AND_PLATFORM_CONVERSION_GATE
no_new_signal_reason: null
loop_contribution_label: canonical_archetype_rule_candidate
do_not_propose_new_weight_delta: false
```

## 23. Validation Scope / Non-Validation Scope

Validated: historical 1D OHLC entry/forward path, complete 30/90/180D MFE/MAE fields, canonical mapping, duplicate key novelty against local continuation list, positive/counterexample balance.

Not validated here: production scoring code, live candidate quality, brokerage/API feasibility, post-2026-02-20 price path, or adjusted-return reconstruction.

## 24. Shadow Weight Calibration

```csv
row_type,axis,scope,large_sector_id,canonical_archetype_id,baseline_value,tested_value,delta,reason,backtest_effect,trigger_ids,calibration_usable_count,new_independent_case_count,counterexample_count,confidence,proposal_type,notes
shadow_weight,C27_repeat_pipeline_platform_conversion_gate,canonical_archetype_specific,L8_PLATFORM_CONTENT_SW_SECURITY,C27_CONTENT_IP_GLOBAL_MONETIZATION,0,1,+1,"Require repeat IP pipeline/platform conversion/margin bridge before Yellow/Green; haircut one-hit or single-title blowoff","keeps JYP/HYBE/Studio Dragon as Stage2~Yellow, pushes Kakao Games/Devsisters one-hit cases down to guarded Stage2/4B, routes NCSoft product thesis break to 4C","C27-R8-L129-035900-JYP-20230515-T1|C27-R8-L129-352820-HYBE-20210521-T1|C27-R8-L129-253450-STUDIO-20201218-T1|C27-R8-L129-293490-KAKAOGAMES-20210629-T1|C27-R8-L129-036570-NCSOFT-20210826-T1|C27-R8-L129-194480-DEVSISTERS-20210923-T1",6,6,3,medium,canonical_shadow_only,"not production; post-calibrated residual"
```

## 25. Machine-Readable Rows

```jsonl
{"row_type":"price_source_validation","source":"Songdaiki/stock-web","source_url":"https://github.com/Songdaiki/stock-web","manifest_path":"atlas/manifest.json","schema_path":"atlas/schema.json","universe_path":"atlas/universe/all_symbols.csv","manifest_max_date":"2026-02-20","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","calibration_shard_root":"atlas/ohlcv_tradable_by_symbol_year","raw_shard_root":"atlas/ohlcv_raw_by_symbol_year","validation_status":"usable_for_historical_calibration"}
{"row_type":"case","case_id":"C27-R8-L129-035900-JYP-20230515","symbol":"035900","company_name":"JYP Ent.","round":"R8","loop":"129","large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C27_CONTENT_IP_GLOBAL_MONETIZATION","fine_archetype_id":"CONTENT_IP_GLOBAL_MONETIZATION_REPEATABILITY_VS_ONE_OFF_HIT_DECAY","case_type":"structural_success","positive_or_counterexample":"positive","best_trigger":"C27-R8-L129-035900-JYP-20230515-T1","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"good_stage2_actionable_yellow_not_green_without_margin_duration","current_profile_verdict":"current_profile_correct","price_source":"Songdaiki/stock-web","notes":"Adds repeat-artist and IP licensing route; no Green without repeat margin duration."}
{"row_type":"trigger","trigger_id":"C27-R8-L129-035900-JYP-20230515-T1","case_id":"C27-R8-L129-035900-JYP-20230515","symbol":"035900","company_name":"JYP Ent.","round":"R8","loop":"129","large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C27_CONTENT_IP_GLOBAL_MONETIZATION","fine_archetype_id":"CONTENT_IP_GLOBAL_MONETIZATION_REPEATABILITY_VS_ONE_OFF_HIT_DECAY","sector":"platform_content_sw_security","primary_archetype":"content_ip_global_monetization","loop_objective":"coverage_gap_fill | counterexample_mining | 4B_non_price_requirement_stress_test | sector_specific_rule_discovery | canonical_archetype_compression | stage2_actionable_bonus_stress_test","trigger_type":"Stage2-Actionable","trigger_date":"2023-05-15","entry_date":"2023-05-15","entry_price":95500,"evidence_available_at_that_date":"1Q23 earnings + North America/global music, concert, MD/IP licensing expansion; multi-artist pipeline around TWICE, Stray Kids, NMIXX, A2K","evidence_source":"JYP 1Q23 IR material / analyst route; KRX/KIND and public IR mirrors","stage2_evidence_fields":["public_event_or_disclosure","relative_strength","early_revision_signal","capacity_or_volume_route"],"stage3_evidence_fields":["multiple_public_sources","financial_visibility","repeat_order_or_conversion","margin_bridge"],"stage4b_evidence_fields":["revision_slowdown_after_peak","positioning_overheat"],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/035/035900/2023.csv","profile_path":"atlas/symbol_profiles/035/035900.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":47.23,"MFE_90D_pct":53.51,"MFE_180D_pct":53.51,"MFE_1Y_pct":null,"MFE_2Y_pct":null,"MAE_30D_pct":-3.46,"MAE_90D_pct":-3.46,"MAE_180D_pct":-23.46,"MAE_1Y_pct":null,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2023-07-25","peak_price":146600,"drawdown_after_peak_pct":-49.05,"green_lateness_ratio":"not_applicable:no_confirmed_Stage3_Green_trigger","four_b_local_peak_proximity":null,"four_b_full_window_peak_proximity":null,"four_b_timing_verdict":"not_primary_4b_row","four_b_evidence_type":[],"four_c_protection_label":"not_applicable","trigger_outcome_label":"multi_artist_global_ip_monetization_positive_but_green_requires_margin_duration","current_profile_verdict":"current_profile_correct","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"C27-R8-L129-035900-JYP-20230515::2023-05-15","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"C27-R8-L129-035900-JYP-20230515","trigger_id":"C27-R8-L129-035900-JYP-20230515-T1","symbol":"035900","large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C27_CONTENT_IP_GLOBAL_MONETIZATION","raw_component_scores_before":{"contract_score":18,"backlog_visibility_score":6,"margin_bridge_score":20,"revision_score":20,"relative_strength_score":18,"customer_quality_score":18,"policy_or_regulatory_score":8,"valuation_repricing_score":12,"execution_risk_score":-6,"legal_or_contract_risk_score":-2,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_before":77,"stage_label_before":"Stage3-Yellow","raw_component_scores_after":{"contract_score":20,"backlog_visibility_score":6,"margin_bridge_score":22,"revision_score":20,"relative_strength_score":18,"customer_quality_score":21,"policy_or_regulatory_score":8,"valuation_repricing_score":12,"execution_risk_score":-6,"legal_or_contract_risk_score":-2,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_after":81,"stage_label_after":"Stage3-Yellow","changed_components":["repeat_pipeline_score","platform_conversion_score","single_ip_concentration_haircut","margin_conversion_gate"],"component_delta_explanation":"Adds repeat-artist and IP licensing route; no Green without repeat margin duration.","MFE_90D_pct":53.51,"MAE_90D_pct":-3.46,"score_return_alignment_label":"good_stage2_actionable_yellow_not_green_without_margin_duration","current_profile_verdict":"current_profile_correct"}
{"row_type":"case","case_id":"C27-R8-L129-352820-HYBE-20210521","symbol":"352820","company_name":"HYBE","round":"R8","loop":"129","large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C27_CONTENT_IP_GLOBAL_MONETIZATION","fine_archetype_id":"CONTENT_IP_GLOBAL_MONETIZATION_REPEATABILITY_VS_ONE_OFF_HIT_DECAY","case_type":"structural_success","positive_or_counterexample":"positive","best_trigger":"C27-R8-L129-352820-HYBE-20210521-T1","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"stage2_actionable_captures_platform_conversion_before_green","current_profile_verdict":"current_profile_correct","price_source":"Songdaiki/stock-web","notes":"Platform/IP route supports Yellow; concentration and military-cycle risk prevents automatic Green."}
{"row_type":"trigger","trigger_id":"C27-R8-L129-352820-HYBE-20210521-T1","case_id":"C27-R8-L129-352820-HYBE-20210521","symbol":"352820","company_name":"HYBE","round":"R8","loop":"129","large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C27_CONTENT_IP_GLOBAL_MONETIZATION","fine_archetype_id":"CONTENT_IP_GLOBAL_MONETIZATION_REPEATABILITY_VS_ONE_OFF_HIT_DECAY","sector":"platform_content_sw_security","primary_archetype":"content_ip_global_monetization","loop_objective":"coverage_gap_fill | counterexample_mining | 4B_non_price_requirement_stress_test | sector_specific_rule_discovery | canonical_archetype_compression | stage2_actionable_bonus_stress_test","trigger_type":"Stage2-Actionable","trigger_date":"2021-05-21","entry_date":"2021-05-21","entry_price":261500,"evidence_available_at_that_date":"BTS Butter global release + Weverse/IP/merchandise monetization route, with label/platform expansion evidence already visible in 2021","evidence_source":"HYBE 2021 sell-side report and public release route; Korea.net/BTS Butter release reference","stage2_evidence_fields":["public_event_or_disclosure","relative_strength","capacity_or_volume_route","early_revision_signal"],"stage3_evidence_fields":["durable_customer_confirmation","multiple_public_sources","financial_visibility","repeat_order_or_conversion"],"stage4b_evidence_fields":["artist_concentration_risk","valuation_blowoff"],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/352/352820/2021.csv","profile_path":"atlas/symbol_profiles/352/352820.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":24.66,"MFE_90D_pct":34.61,"MFE_180D_pct":61.19,"MFE_1Y_pct":null,"MFE_2Y_pct":null,"MAE_30D_pct":-3.63,"MAE_90D_pct":-3.63,"MAE_180D_pct":-9.37,"MAE_1Y_pct":null,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2021-11-17","peak_price":421500,"drawdown_after_peak_pct":-43.77,"green_lateness_ratio":"not_applicable:no_confirmed_Stage3_Green_trigger","four_b_local_peak_proximity":null,"four_b_full_window_peak_proximity":null,"four_b_timing_verdict":"not_primary_4b_row","four_b_evidence_type":[],"four_c_protection_label":"not_applicable","trigger_outcome_label":"global_artist_ip_platform_monetization_positive_with_concentration_risk","current_profile_verdict":"current_profile_correct","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"C27-R8-L129-352820-HYBE-20210521::2021-05-21","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"C27-R8-L129-352820-HYBE-20210521","trigger_id":"C27-R8-L129-352820-HYBE-20210521-T1","symbol":"352820","large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C27_CONTENT_IP_GLOBAL_MONETIZATION","raw_component_scores_before":{"contract_score":18,"backlog_visibility_score":6,"margin_bridge_score":12,"revision_score":20,"relative_strength_score":18,"customer_quality_score":18,"policy_or_regulatory_score":8,"valuation_repricing_score":12,"execution_risk_score":-6,"legal_or_contract_risk_score":-2,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_before":76,"stage_label_before":"Stage3-Yellow","raw_component_scores_after":{"contract_score":20,"backlog_visibility_score":6,"margin_bridge_score":14,"revision_score":20,"relative_strength_score":18,"customer_quality_score":21,"policy_or_regulatory_score":8,"valuation_repricing_score":12,"execution_risk_score":-6,"legal_or_contract_risk_score":-2,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_after":80,"stage_label_after":"Stage3-Yellow","changed_components":["repeat_pipeline_score","platform_conversion_score","single_ip_concentration_haircut","margin_conversion_gate"],"component_delta_explanation":"Platform/IP route supports Yellow; concentration and military-cycle risk prevents automatic Green.","MFE_90D_pct":34.61,"MAE_90D_pct":-3.63,"score_return_alignment_label":"stage2_actionable_captures_platform_conversion_before_green","current_profile_verdict":"current_profile_correct"}
{"row_type":"case","case_id":"C27-R8-L129-253450-STUDIO-20201218","symbol":"253450","company_name":"Studio Dragon","round":"R8","loop":"129","large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C27_CONTENT_IP_GLOBAL_MONETIZATION","fine_archetype_id":"CONTENT_IP_GLOBAL_MONETIZATION_REPEATABILITY_VS_ONE_OFF_HIT_DECAY","case_type":"structural_success_mixed","positive_or_counterexample":"positive","best_trigger":"C27-R8-L129-253450-STUDIO-20201218-T1","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"stage2_watch_is_right_green_would_be_too_early","current_profile_verdict":"current_profile_too_early","price_source":"Songdaiki/stock-web","notes":"The new gate reduces Green/Yellow credit when OTT hit lacks recoup-rate or repeat-margin proof."}
{"row_type":"trigger","trigger_id":"C27-R8-L129-253450-STUDIO-20201218-T1","case_id":"C27-R8-L129-253450-STUDIO-20201218","symbol":"253450","company_name":"Studio Dragon","round":"R8","loop":"129","large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C27_CONTENT_IP_GLOBAL_MONETIZATION","fine_archetype_id":"CONTENT_IP_GLOBAL_MONETIZATION_REPEATABILITY_VS_ONE_OFF_HIT_DECAY","sector":"platform_content_sw_security","primary_archetype":"content_ip_global_monetization","loop_objective":"coverage_gap_fill | counterexample_mining | 4B_non_price_requirement_stress_test | sector_specific_rule_discovery | canonical_archetype_compression | stage2_actionable_bonus_stress_test","trigger_type":"Stage2","trigger_date":"2020-12-18","entry_date":"2020-12-18","entry_price":83100,"evidence_available_at_that_date":"Sweet Home global Netflix debut + global K-drama production studio optionality; evidence showed IP export route but margin durability was not yet fully confirmed","evidence_source":"Netflix Sweet Home global debut notice and Korean content/global OTT coverage","stage2_evidence_fields":["public_event_or_disclosure","policy_or_regulatory_optionality","relative_strength"],"stage3_evidence_fields":["multiple_public_sources"],"stage4b_evidence_fields":["valuation_blowoff","margin_visibility_gap"],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/253/253450/2020.csv","profile_path":"atlas/symbol_profiles/253/253450.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":35.98,"MFE_90D_pct":35.98,"MFE_180D_pct":35.98,"MFE_1Y_pct":null,"MFE_2Y_pct":null,"MAE_30D_pct":-0.36,"MAE_90D_pct":-0.36,"MAE_180D_pct":-8.66,"MAE_1Y_pct":null,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2021-01-21","peak_price":113000,"drawdown_after_peak_pct":-32.83,"green_lateness_ratio":"not_applicable:no_confirmed_Stage3_Green_trigger","four_b_local_peak_proximity":0.91,"four_b_full_window_peak_proximity":0.91,"four_b_timing_verdict":"local_valuation_watch_not_full_4b_without_margin_slowdown","four_b_evidence_type":["valuation_blowoff"],"four_c_protection_label":"not_applicable","trigger_outcome_label":"global_ott_ip_route_positive_but_production_margin_bridge_missing","current_profile_verdict":"current_profile_too_early","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"C27-R8-L129-253450-STUDIO-20201218::2020-12-18","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"C27-R8-L129-253450-STUDIO-20201218","trigger_id":"C27-R8-L129-253450-STUDIO-20201218-T1","symbol":"253450","large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C27_CONTENT_IP_GLOBAL_MONETIZATION","raw_component_scores_before":{"contract_score":18,"backlog_visibility_score":6,"margin_bridge_score":12,"revision_score":12,"relative_strength_score":18,"customer_quality_score":18,"policy_or_regulatory_score":8,"valuation_repricing_score":12,"execution_risk_score":-6,"legal_or_contract_risk_score":-2,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_before":72,"stage_label_before":"Stage2-Actionable","raw_component_scores_after":{"contract_score":18,"backlog_visibility_score":6,"margin_bridge_score":9,"revision_score":12,"relative_strength_score":18,"customer_quality_score":18,"policy_or_regulatory_score":8,"valuation_repricing_score":8,"execution_risk_score":-6,"legal_or_contract_risk_score":-2,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_after":68,"stage_label_after":"Stage2","changed_components":["repeat_pipeline_score","platform_conversion_score","single_ip_concentration_haircut","margin_conversion_gate"],"component_delta_explanation":"The new gate reduces Green/Yellow credit when OTT hit lacks recoup-rate or repeat-margin proof.","MFE_90D_pct":35.98,"MAE_90D_pct":-0.36,"score_return_alignment_label":"stage2_watch_is_right_green_would_be_too_early","current_profile_verdict":"current_profile_too_early"}
{"row_type":"case","case_id":"C27-R8-L129-293490-KAKAOGAMES-20210629","symbol":"293490","company_name":"Kakao Games","round":"R8","loop":"129","large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C27_CONTENT_IP_GLOBAL_MONETIZATION","fine_archetype_id":"CONTENT_IP_GLOBAL_MONETIZATION_REPEATABILITY_VS_ONE_OFF_HIT_DECAY","case_type":"one_hit_price_success_green_guardrail","positive_or_counterexample":"counterexample","best_trigger":"C27-R8-L129-293490-KAKAOGAMES-20210629-T1","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"positive_price_path_but_should_not_train_as_structural_green","current_profile_verdict":"current_profile_false_positive","price_source":"Songdaiki/stock-web","notes":"Single-title concentration gets haircut despite high MFE; keep as Stage2-Actionable/4B watch, not Green."}
{"row_type":"trigger","trigger_id":"C27-R8-L129-293490-KAKAOGAMES-20210629-T1","case_id":"C27-R8-L129-293490-KAKAOGAMES-20210629","symbol":"293490","company_name":"Kakao Games","round":"R8","loop":"129","large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C27_CONTENT_IP_GLOBAL_MONETIZATION","fine_archetype_id":"CONTENT_IP_GLOBAL_MONETIZATION_REPEATABILITY_VS_ONE_OFF_HIT_DECAY","sector":"platform_content_sw_security","primary_archetype":"content_ip_global_monetization","loop_objective":"coverage_gap_fill | counterexample_mining | 4B_non_price_requirement_stress_test | sector_specific_rule_discovery | canonical_archetype_compression | stage2_actionable_bonus_stress_test","trigger_type":"Stage2-Actionable","trigger_date":"2021-06-29","entry_date":"2021-06-29","entry_price":59700,"evidence_available_at_that_date":"Odin launch and top-grossing momentum created a very strong price path, but the evidence family was game-hit concentrated rather than repeat IP/platform conversion","evidence_source":"Kakao Games Odin launch / later top-grossing reporting route","stage2_evidence_fields":["public_event_or_disclosure","relative_strength","early_revision_signal"],"stage3_evidence_fields":["financial_visibility"],"stage4b_evidence_fields":["positioning_overheat","single_title_concentration","valuation_blowoff"],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/293/293490/2021.csv","profile_path":"atlas/symbol_profiles/293/293490.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":77.55,"MFE_90D_pct":77.55,"MFE_180D_pct":94.3,"MFE_1Y_pct":null,"MFE_2Y_pct":null,"MAE_30D_pct":-6.87,"MAE_90D_pct":-6.87,"MAE_180D_pct":-6.87,"MAE_1Y_pct":null,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2021-11-17","peak_price":116000,"drawdown_after_peak_pct":-36.64,"green_lateness_ratio":"not_applicable:no_confirmed_Stage3_Green_trigger","four_b_local_peak_proximity":0.78,"four_b_full_window_peak_proximity":0.54,"four_b_timing_verdict":"price_only_local_4B_too_early_without_repeat_pipeline_evidence","four_b_evidence_type":["positioning_overheat","valuation_blowoff"],"four_c_protection_label":"thesis_break_watch_only","trigger_outcome_label":"single_game_hit_price_success_but_durable_green_false_positive_risk","current_profile_verdict":"current_profile_false_positive","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"C27-R8-L129-293490-KAKAOGAMES-20210629::2021-06-29","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"C27-R8-L129-293490-KAKAOGAMES-20210629","trigger_id":"C27-R8-L129-293490-KAKAOGAMES-20210629-T1","symbol":"293490","large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C27_CONTENT_IP_GLOBAL_MONETIZATION","raw_component_scores_before":{"contract_score":8,"backlog_visibility_score":3,"margin_bridge_score":4,"revision_score":8,"relative_strength_score":24,"customer_quality_score":6,"policy_or_regulatory_score":3,"valuation_repricing_score":24,"execution_risk_score":-18,"legal_or_contract_risk_score":-4,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_before":82,"stage_label_before":"Stage3-Yellow","raw_component_scores_after":{"contract_score":8,"backlog_visibility_score":3,"margin_bridge_score":0,"revision_score":8,"relative_strength_score":24,"customer_quality_score":2,"policy_or_regulatory_score":3,"valuation_repricing_score":14,"execution_risk_score":-26,"legal_or_contract_risk_score":-4,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_after":72,"stage_label_after":"Stage2-Actionable","changed_components":["repeat_pipeline_score","platform_conversion_score","single_ip_concentration_haircut","margin_conversion_gate"],"component_delta_explanation":"Single-title concentration gets haircut despite high MFE; keep as Stage2-Actionable/4B watch, not Green.","MFE_90D_pct":77.55,"MAE_90D_pct":-6.87,"score_return_alignment_label":"positive_price_path_but_should_not_train_as_structural_green","current_profile_verdict":"current_profile_false_positive"}
{"row_type":"case","case_id":"C27-R8-L129-036570-NCSOFT-20210826","symbol":"036570","company_name":"NCSoft","round":"R8","loop":"129","large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C27_CONTENT_IP_GLOBAL_MONETIZATION","fine_archetype_id":"CONTENT_IP_GLOBAL_MONETIZATION_REPEATABILITY_VS_ONE_OFF_HIT_DECAY","case_type":"hard_4c_thesis_break","positive_or_counterexample":"counterexample","best_trigger":"C27-R8-L129-036570-NCSOFT-20210826-T1","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"hard_4c_routing_should_trigger_when_ip_quality_thesis_breaks","current_profile_verdict":"current_profile_4C_too_late","price_source":"Songdaiki/stock-web","notes":"When user/product quality breaks the franchise thesis, route to 4C rather than waiting for another quarter."}
{"row_type":"trigger","trigger_id":"C27-R8-L129-036570-NCSOFT-20210826-T1","case_id":"C27-R8-L129-036570-NCSOFT-20210826","symbol":"036570","company_name":"NCSoft","round":"R8","loop":"129","large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C27_CONTENT_IP_GLOBAL_MONETIZATION","fine_archetype_id":"CONTENT_IP_GLOBAL_MONETIZATION_REPEATABILITY_VS_ONE_OFF_HIT_DECAY","sector":"platform_content_sw_security","primary_archetype":"content_ip_global_monetization","loop_objective":"coverage_gap_fill | counterexample_mining | 4B_non_price_requirement_stress_test | sector_specific_rule_discovery | canonical_archetype_compression | stage2_actionable_bonus_stress_test","trigger_type":"Stage4C","trigger_date":"2021-08-26","entry_date":"2021-08-26","entry_price":709000,"evidence_available_at_that_date":"Blade & Soul 2 launch disappointment / monetization backlash broke the mobile-IP quality thesis despite established franchise ownership","evidence_source":"NCSoft public launch route and market reaction reporting route","stage2_evidence_fields":["public_event_or_disclosure"],"stage3_evidence_fields":[],"stage4b_evidence_fields":["positioning_overheat","execution_risk"],"stage4c_evidence_fields":["thesis_evidence_broken","customer_or_user_reaction_failure"],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/036/036570/2021.csv","profile_path":"atlas/symbol_profiles/036/036570.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":11.14,"MFE_90D_pct":11.14,"MFE_180D_pct":11.14,"MFE_1Y_pct":null,"MFE_2Y_pct":null,"MAE_30D_pct":-21.3,"MAE_90D_pct":-22.43,"MAE_180D_pct":-39.07,"MAE_1Y_pct":null,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2021-08-26","peak_price":788000,"drawdown_after_peak_pct":-45.18,"green_lateness_ratio":"not_applicable:no_confirmed_Stage3_Green_trigger","four_b_local_peak_proximity":0.94,"four_b_full_window_peak_proximity":0.94,"four_b_timing_verdict":"good_full_window_4B_timing_if_non_price_disappointment_evidence_present","four_b_evidence_type":["execution_risk","positioning_overheat"],"four_c_protection_label":"hard_4c_success","trigger_outcome_label":"franchise_ip_quality_break_hard_4c","current_profile_verdict":"current_profile_4C_too_late","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"C27-R8-L129-036570-NCSOFT-20210826::2021-08-26","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"C27-R8-L129-036570-NCSOFT-20210826","trigger_id":"C27-R8-L129-036570-NCSOFT-20210826-T1","symbol":"036570","large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C27_CONTENT_IP_GLOBAL_MONETIZATION","raw_component_scores_before":{"contract_score":8,"backlog_visibility_score":3,"margin_bridge_score":4,"revision_score":8,"relative_strength_score":24,"customer_quality_score":6,"policy_or_regulatory_score":3,"valuation_repricing_score":24,"execution_risk_score":-18,"legal_or_contract_risk_score":-4,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_before":69,"stage_label_before":"Stage2","raw_component_scores_after":{"contract_score":8,"backlog_visibility_score":3,"margin_bridge_score":4,"revision_score":8,"relative_strength_score":24,"customer_quality_score":-2,"policy_or_regulatory_score":3,"valuation_repricing_score":16,"execution_risk_score":-36,"legal_or_contract_risk_score":-4,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_after":49,"stage_label_after":"Stage4C","changed_components":["repeat_pipeline_score","platform_conversion_score","single_ip_concentration_haircut","margin_conversion_gate"],"component_delta_explanation":"When user/product quality breaks the franchise thesis, route to 4C rather than waiting for another quarter.","MFE_90D_pct":11.14,"MAE_90D_pct":-22.43,"score_return_alignment_label":"hard_4c_routing_should_trigger_when_ip_quality_thesis_breaks","current_profile_verdict":"current_profile_4C_too_late"}
{"row_type":"case","case_id":"C27-R8-L129-194480-DEVSISTERS-20210923","symbol":"194480","company_name":"Devsisters","round":"R8","loop":"129","large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C27_CONTENT_IP_GLOBAL_MONETIZATION","fine_archetype_id":"CONTENT_IP_GLOBAL_MONETIZATION_REPEATABILITY_VS_ONE_OFF_HIT_DECAY","case_type":"one_hit_overheat_4b","positive_or_counterexample":"counterexample","best_trigger":"C27-R8-L129-194480-DEVSISTERS-20210923-T1","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":0.75,"score_price_alignment":"stage4b_overlay_should_block_new_green_credit_after_price_extension","current_profile_verdict":"current_profile_4B_too_late","price_source":"Songdaiki/stock-web","notes":"Not a new structural positive: it is an overheat guardrail row for single-IP concentration."}
{"row_type":"trigger","trigger_id":"C27-R8-L129-194480-DEVSISTERS-20210923-T1","case_id":"C27-R8-L129-194480-DEVSISTERS-20210923","symbol":"194480","company_name":"Devsisters","round":"R8","loop":"129","large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C27_CONTENT_IP_GLOBAL_MONETIZATION","fine_archetype_id":"CONTENT_IP_GLOBAL_MONETIZATION_REPEATABILITY_VS_ONE_OFF_HIT_DECAY","sector":"platform_content_sw_security","primary_archetype":"content_ip_global_monetization","loop_objective":"coverage_gap_fill | counterexample_mining | 4B_non_price_requirement_stress_test | sector_specific_rule_discovery | canonical_archetype_compression | stage2_actionable_bonus_stress_test","trigger_type":"Stage4B","trigger_date":"2021-09-23","entry_date":"2021-09-23","entry_price":177200,"evidence_available_at_that_date":"Cookie Run: Kingdom global momentum was visible, but by the public overheat window the stock had already embedded a single-IP runaway scenario","evidence_source":"KED Global article on Devsisters YTD growth and Cookie Run Kingdom momentum","stage2_evidence_fields":["public_event_or_disclosure","relative_strength"],"stage3_evidence_fields":[],"stage4b_evidence_fields":["valuation_blowoff","positioning_overheat","single_title_concentration"],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/194/194480/2021.csv","profile_path":"atlas/symbol_profiles/194/194480.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":10.61,"MFE_90D_pct":10.61,"MFE_180D_pct":10.61,"MFE_1Y_pct":null,"MFE_2Y_pct":null,"MAE_30D_pct":-33.75,"MAE_90D_pct":-50.45,"MAE_180D_pct":-67.04,"MAE_1Y_pct":null,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2021-09-23","peak_price":196000,"drawdown_after_peak_pct":-70.2,"green_lateness_ratio":"not_applicable:no_confirmed_Stage3_Green_trigger","four_b_local_peak_proximity":0.95,"four_b_full_window_peak_proximity":0.95,"four_b_timing_verdict":"good_full_window_4B_timing_with_non_price_single_title_concentration","four_b_evidence_type":["valuation_blowoff","positioning_overheat"],"four_c_protection_label":"thesis_break_watch_only","trigger_outcome_label":"single_ip_overheat_full_window_4b_guardrail","current_profile_verdict":"current_profile_4B_too_late","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"C27-R8-L129-194480-DEVSISTERS-20210923::2021-09-23","dedupe_for_aggregate":false,"aggregate_group_role":"4B_overlay_only","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":0.75,"do_not_count_as_new_case":false}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"C27-R8-L129-194480-DEVSISTERS-20210923","trigger_id":"C27-R8-L129-194480-DEVSISTERS-20210923-T1","symbol":"194480","large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C27_CONTENT_IP_GLOBAL_MONETIZATION","raw_component_scores_before":{"contract_score":8,"backlog_visibility_score":3,"margin_bridge_score":4,"revision_score":8,"relative_strength_score":24,"customer_quality_score":6,"policy_or_regulatory_score":3,"valuation_repricing_score":24,"execution_risk_score":-18,"legal_or_contract_risk_score":-4,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_before":80,"stage_label_before":"Stage3-Yellow","raw_component_scores_after":{"contract_score":8,"backlog_visibility_score":3,"margin_bridge_score":0,"revision_score":8,"relative_strength_score":24,"customer_quality_score":2,"policy_or_regulatory_score":3,"valuation_repricing_score":14,"execution_risk_score":-26,"legal_or_contract_risk_score":-4,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_after":58,"stage_label_after":"Stage4B","changed_components":["repeat_pipeline_score","platform_conversion_score","single_ip_concentration_haircut","margin_conversion_gate"],"component_delta_explanation":"Not a new structural positive: it is an overheat guardrail row for single-IP concentration.","MFE_90D_pct":10.61,"MAE_90D_pct":-50.45,"score_return_alignment_label":"stage4b_overlay_should_block_new_green_credit_after_price_extension","current_profile_verdict":"current_profile_4B_too_late"}
{"row_type":"residual_contribution","round":"R8","loop":"129","large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C27_CONTENT_IP_GLOBAL_MONETIZATION","new_independent_case_count":6,"reused_case_count":0,"new_symbol_count":6,"new_trigger_family_count":6,"tested_existing_calibrated_axes":["stage2_actionable_evidence_bonus","price_only_blowoff_blocks_positive_stage","full_4b_requires_non_price_evidence","hard_4c_thesis_break_routes_to_4c"],"residual_error_types_found":["one_hit_green_false_positive","single_ip_concentration_high_mae","ip_quality_thesis_break_4c_late","ott_hit_without_margin_bridge_green_too_early"],"loop_contribution_label":"canonical_archetype_rule_candidate","do_not_propose_new_weight_delta":false}
```

## 26. Deferred Coding Agent Handoff Prompt

### Purpose
You are now in the repository implementation phase. The attached Markdown files are v12 post-calibrated residual research outputs produced using the Songdaiki/stock-web OHLC atlas. These MDs are not live candidate research. They are historical calibration research designed to extend the already-applied e2r_2_1_stock_web_calibrated profile. Do not blindly apply every shadow row. Ingest the machine-readable rows and update the sector/canonical-archetype calibration ledger.

### Price source context
- Primary historical price source used by the research MD: Songdaiki/stock-web.
- Price basis: tradable_raw.
- Price adjustment status: raw_unadjusted_marcap.
- Price shard pattern: atlas/ohlcv_tradable_by_symbol_year/{prefix}/{symbol}/{year}.csv.
- Symbol profile pattern: atlas/symbol_profiles/{prefix}/{symbol}.json.

### Rules
1. Use only `calibration_usable=true` rows for quantitative calibration.
2. Do not count reused cases as new independent evidence unless `independent_evidence_weight > 0`.
3. Do not treat schema_rematerialization_only or duplicate_low_value_loop as new evidence.
4. Do not apply global deltas unless multiple large_sector_id values support the same direction.
5. Prefer sector_specific or canonical_archetype_specific shadow profiles.
6. Positive score promotion requires non-price evidence and clean 180D MFE/MAE.
7. 4B rows are overlay/risk calibration only.
8. 4C rows are thesis-break/protection calibration only.
9. Price-only rows cannot promote Stage2/Stage3.
10. Production scoring must not change unless the user explicitly asks for another promotion batch.

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
completed_round = R8
completed_loop = 129
selection_basis = docs/core/V12_Research_No_Repeat_Index.md
selected_priority_bucket = Priority 1 / under_50_rows_static_ledger / C27 rows 48 need_to_50 2 before this local loop
round_schedule_status = coverage_index_selected
round_sector_consistency = pass
next_recommended_archetypes = C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY_quality_repair, C19_BRAND_RETAIL_INVENTORY_MARGIN_quality_repair, C31_POLICY_SUBSIDY_LEGISLATION_EVENT_URL_repair, R13_CROSS_ARCHETYPE_4B_4C_REDTEAM_if_guardrail_needed, C27_CONTENT_IP_GLOBAL_MONETIZATION_followup_only_if_URL_repair_needed
```

## 28. Source Notes

- MAIN EXECUTION PROMPT: https://raw.githubusercontent.com/Songdaiki/stock_agent/main/docs/core/e2r_v12_prompt_round_scheduler_corrected.txt
- NO-REPEAT INDEX: https://raw.githubusercontent.com/Songdaiki/stock_agent/main/docs/core/V12_Research_No_Repeat_Index.md
- stock-web manifest: https://raw.githubusercontent.com/Songdaiki/stock-web/main/atlas/manifest.json
- JYP price row checkpoint: https://github.com/Songdaiki/stock-web/blob/main/atlas/ohlcv_tradable_by_symbol_year/035/035900/2023.csv?plain=1
- HYBE price row checkpoint: https://github.com/Songdaiki/stock-web/blob/main/atlas/ohlcv_tradable_by_symbol_year/352/352820/2021.csv?plain=1
- Studio Dragon price row checkpoint: https://github.com/Songdaiki/stock-web/blob/main/atlas/ohlcv_tradable_by_symbol_year/253/253450/2020.csv?plain=1
- Kakao Games price row checkpoint: https://github.com/Songdaiki/stock-web/blob/main/atlas/ohlcv_tradable_by_symbol_year/293/293490/2021.csv?plain=1
- NCSoft price row checkpoint: https://github.com/Songdaiki/stock-web/blob/main/atlas/ohlcv_tradable_by_symbol_year/036/036570/2021.csv?plain=1
- Devsisters price row checkpoint: https://github.com/Songdaiki/stock-web/blob/main/atlas/ohlcv_tradable_by_symbol_year/194/194480/2021.csv?plain=1
- Evidence references used as qualitative source routes: public JYP IR / HYBE reports / Netflix Sweet Home notice / Kakao Games Odin launch and top-grossing reports / NCSoft launch reaction routes / KED Global Devsisters article.
