# E2R Stock-Web Historical Calibration / Sector-Archetype Residual Research Round

## 0. Research Metadata

```json
{
  "scheduled_round": "R1",
  "scheduled_loop": 11,
  "round_schedule_status": "valid",
  "round_sector_consistency": "pass",
  "completed_round": "R1",
  "completed_loop": 11,
  "next_round": "R2",
  "next_loop": 11,
  "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID",
  "canonical_archetype_id": "C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG",
  "fine_archetype_id": "DEFENSE_EXPORT_FRAMEWORK_BACKLOG_POLAND_EXECUTIVE_CONTRACT",
  "loop_objective": [
    "coverage_gap_fill",
    "sector_specific_rule_discovery",
    "canonical_archetype_compression",
    "stage2_actionable_bonus_stress_test",
    "green_strictness_stress_test",
    "4B_non_price_requirement_stress_test",
    "4C_thesis_break_timing_test",
    "counterexample_mining"
  ],
  "price_source": "Songdaiki/stock-web",
  "stock_web_manifest_max_date": "2026-02-20",
  "price_basis": "tradable_raw",
  "price_adjustment_status": "raw_unadjusted_marcap",
  "new_independent_case_count": 3,
  "reused_case_count": 0,
  "new_symbol_count": 3,
  "same_archetype_new_symbol_count": 3,
  "same_archetype_new_trigger_family_count": 3,
  "new_trigger_family_count": 3,
  "calibration_usable_case_count": 3,
  "calibration_usable_trigger_count": 5,
  "positive_case_count": 2,
  "counterexample_count": 1,
  "current_profile_error_count": 1,
  "diversity_score_summary": "estimated +35; wrong_round_penalty=0; repeated_same_symbol_penalty=0",
  "do_not_propose_new_weight_delta": false,
  "loop_contribution_label": "canonical_archetype_rule_candidate"
}
```

This loop adds 3 new independent cases, 1 counterexample, and 1 residual error for R1/L1_INDUSTRIALS_INFRA_DEFENSE_GRID/C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG.

## 1. Current Calibrated Profile Assumption

Current proxy profile:

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

This MD does not change production scoring. All proposed axes are shadow-only.

## 2. Round / Large Sector / Canonical Archetype Scope

```text
scheduled_round = R1
scheduled_loop = 11
large_sector_id = L1_INDUSTRIALS_INFRA_DEFENSE_GRID
canonical_archetype_id = C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG
fine_archetype_id = DEFENSE_EXPORT_FRAMEWORK_BACKLOG_POLAND_EXECUTIVE_CONTRACT
round_schedule_status = valid
round_sector_consistency = pass
```

R1 allows industrials, orders, infrastructure, defense, grid, EPC and policy-linked industrial backlog. This run intentionally avoids C02 power-grid repetition from loop 10 and selects C03 defense export framework/backlog.

## 3. Previous Coverage / Duplicate Avoidance Check

Allowed artifacts show historical loops 1~9 and all rounds R1~R13 already covered in the repository ingest snapshot. The local prior cycle completed R13 loop 10, so scheduler moves to R1 loop 11.

Duplicate governor result:

```text
same_canonical_archetype_research = allowed
same_symbol_same_trigger_date_research = avoided
new_symbol_count = 3
same_archetype_new_symbol_count = 3
same_archetype_new_trigger_family_count = 3
new_independent_case_ratio = 1.00
```

The selected sample set is not a restatement of C02 transformer/grid cases and not a generic “defense stocks rose” bundle. The specific residual is: direct sovereign framework/executive contract routes behave differently from complex export headline routes where margin, delivery and platform-development risk remain unresolved.

## 4. Stock-Web OHLC Input / Price Source Validation

```text
price_data_source = Songdaiki/stock-web
source_basis = FinanceData/marcap
price_basis = tradable_raw
price_adjustment_status = raw_unadjusted_marcap
manifest_max_date = 2026-02-20
calibration_shard_root = atlas/ohlcv_tradable_by_symbol_year
raw_shard_root = atlas/ohlcv_raw_by_symbol_year
```

Symbols validated:

```text
012450 한화에어로스페이스
064350 현대로템
047810 한국항공우주
```

Corporate-action / profile notes:

```text
012450: profile exists, 2022/2023 shards present, 180D window usable.
064350: one old corporate-action candidate in 2020-08-14, outside the 2022-07-29~D+180 window.
047810: no corporate-action candidates, 180D window usable.
```

## 5. Historical Eligibility Gate

All representative triggers satisfy:

```text
trigger_date is historical = true
entry_date exists in stock-web tradable shard = true
forward 180D trading window available = true
required OHLC fields available = true
corporate_action_contaminated_180D_window = false
calibration_usable = true
```

## 6. Canonical Archetype Compression Map

| fine_archetype_id | canonical_archetype_id | Compression logic |
|---|---|---|
| DEFENSE_EXPORT_FRAMEWORK_BACKLOG_POLAND_EXECUTIVE_CONTRACT | C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG | Sovereign buyer + framework agreement + executive contract + delivery/backlog visibility. |
| DEFENSE_EXPORT_FRAMEWORK_BACKLOG_POLAND_EXECUTION_RISK | C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG | Export headline exists, but aircraft platform delivery, margin, service center and revision proof remain weaker. |

## 7. Case Selection Summary

| case_id | symbol | company | role | why selected |
|---|---:|---|---|---|
| R1L11_C03_012450_POLAND_K9_HANWHA | 012450 | 한화에어로스페이스 | structural_success | K9 Poland framework/executive contract route with strong 180D MFE. |
| R1L11_C03_064350_POLAND_K2_HYUNDAI_ROTEM | 064350 | 현대로템 | high_mae_success | K2 Poland route validates Stage2/Yellow but warns against too-easy Green due to drawdown. |
| R1L11_C03_047810_POLAND_FA50_KAI | 047810 | 한국항공우주 | failed_rerating | Same Poland defense procurement umbrella, but weaker full-window price path and higher MAE. |

## 8. Positive vs Counterexample Balance

```text
positive_case_count = 2
counterexample_count = 1
calibration_usable_case_count = 3
4B_case_count = 1
4C_case_count = 1
```

Interpretation: C03 should reward direct sovereign framework/executive-contract visibility, but should cap export headlines that lack margin, delivery and revision bridge. This is not a global Stage2-bonus restatement; it is a C03 compression rule.

## 9. Evidence Source Map

| symbol | evidence family | evidence timing | validation status |
|---:|---|---|---|
| 012450 | K9 Poland framework / executive contract | 2022-07~2022-08 | public-source verified at summary level; exact source URL enrichment required |
| 064350 | K2 Poland framework / executive contract | 2022-07~2022-08 | public-source verified at summary level; exact source URL enrichment required |
| 047810 | FA-50 Poland export contract | 2022-07 | public-source verified at summary level; exact source URL enrichment required |

## 10. Price Data Source Map

| symbol | price_shard_path | profile_path | entry_date | forward window |
|---:|---|---|---|---|
| 012450 | atlas/ohlcv_tradable_by_symbol_year/012/012450/2022.csv + 2023.csv | atlas/symbol_profiles/012/012450.json | 2022-07-29 | usable |
| 064350 | atlas/ohlcv_tradable_by_symbol_year/064/064350/2022.csv + 2023.csv | atlas/symbol_profiles/064/064350.json | 2022-07-29 | usable |
| 047810 | atlas/ohlcv_tradable_by_symbol_year/047/047810/2022.csv + 2023.csv | atlas/symbol_profiles/047/047810.json | 2022-07-29 | usable |

## 11. Case-by-Case Trigger Grid

| case | symbol | trigger | entry | entry_price | MFE_30 | MFE_90 | MFE_180 | MAE_30 | MAE_90 | MAE_180 | verdict |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|
| Hanwha K9 Poland | 012450 | Stage2-Actionable | 2022-07-29 | 64,400 | +34.78% | +34.78% | +84.47% | -6.06% | -7.61% | -7.61% | direct sovereign framework success |
| Hyundai Rotem K2 Poland | 064350 | Stage2-Actionable | 2022-07-29 | 26,550 | +23.73% | +23.73% | +23.73% | -9.42% | -9.42% | -10.73% | high-MAE but valid success |
| KAI FA-50 Poland | 047810 | Stage2-Actionable | 2022-07-29 | 57,000 | +12.11% | +12.11% | +12.11% | -5.09% | -19.30% | -27.11% | export headline overpromotion counterexample |


## 12. Trigger-Level OHLC Backtest Tables

Representative trigger aggregate:

| metric | 012450 | 064350 | 047810 |
|---|---:|---:|---:|
| entry_price | 64,400 | 26,550 | 57,000 |
| MFE_30D_pct | +34.78 | +23.73 | +12.11 |
| MFE_90D_pct | +34.78 | +23.73 | +12.11 |
| MFE_180D_pct | +84.47 | +23.73 | +12.11 |
| MAE_30D_pct | -6.06 | -9.42 | -5.09 |
| MAE_90D_pct | -7.61 | -9.42 | -19.30 |
| MAE_180D_pct | -7.61 | -10.73 | -27.11 |

Aggregate representative metric:

```text
positive_avg_MFE_180D_pct = 54.10
positive_avg_MAE_180D_pct = -9.17
counterexample_MFE_180D_pct = 12.11
counterexample_MAE_180D_pct = -27.11
```

## 13. Current Calibrated Profile Stress Test

| case | current profile likely label | actual result | verdict |
|---|---|---|---|
| 012450 Hanwha | Stage3-Yellow, not automatic Green | Large MFE and tolerable MAE | current_profile_correct |
| 064350 Rotem | Stage3-Yellow, Green only after execution proof | Valid MFE but high drawdown | current_profile_correct |
| 047810 KAI | Stage2-Actionable could be overpromoted if all export contracts treated alike | Low MFE / high MAE | current_profile_false_positive |

Axis verdicts:

```text
stage2_actionable_evidence_bonus = existing_axis_tested
stage3_yellow_total_min = existing_axis_kept
stage3_green_total_min = existing_axis_strengthened for C03 if margin/delivery bridge missing
full_4b_requires_non_price_evidence = existing_axis_strengthened
hard_4c_thesis_break_routes_to_4c = existing_axis_strengthened
```

## 14. Stage2 / Yellow / Green Comparison

C03 needs three layers:

```text
Stage2-Watch:
  export headline, defense policy tailwind, buyer interest, MoU/framework only

Stage2-Actionable / Yellow:
  sovereign buyer + named platform + framework or executive contract + delivery/backlog visibility

Stage3-Green:
  confirmed backlog conversion + margin/revision proof + low execution/legal risk
```

KAI illustrates why Green should not be inherited from customer quality alone. Aircraft export contracts can carry training, delivery, integration and margin timing risk that is not identical to K9/K2 urgent-delivery backlog.

## 15. 4B Local vs Full-window Timing Audit

| trigger | local_peak_proximity | full_window_peak_proximity | verdict |
|---|---:|---:|---|
| Hanwha 2023-04-10 | 0.97 | 0.97 | good_full_window_4B_timing_if_non_price_evidence_confirmed |
| KAI 2022-09-07 local peak | 0.99 | 0.99 | price_only_local_4B_too_early_without_margin_or_delivery_slowdown |

Rule implication: price-only peaks must remain overlay-only unless accompanied by valuation blowoff, revision slowdown, margin deterioration, contract delay, or explicit execution risk.

## 16. 4C Protection Audit

KAI shows a high-MAE counterexample, but the later 2023 recovery warns against hard 4C based on price alone. The correct guardrail is:

```text
hard_4c_requires = explicit thesis break OR confirmed delivery/margin/revision deterioration
price_only_large_MAE = 4C_watch_only
```

## 17. Sector-Specific Rule Candidate

```text
rule_scope = sector_specific
large_sector_id = L1_INDUSTRIALS_INFRA_DEFENSE_GRID
candidate_axis = defense_export_framework_to_executive_contract_bridge
```

Candidate rule:

```text
For L1 defense export cases, raise Stage2/Yellow confidence when a sovereign buyer,
named platform, framework/executive contract, and delivery/backlog visibility all exist.
Do not lift to Green unless margin/revision and execution-risk bridge also exist.
```

## 18. Canonical-Archetype Rule Candidate

```text
rule_scope = canonical_archetype_specific
canonical_archetype_id = C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG
new_axis_proposed =
  c03_direct_sovereign_framework_to_executive_contract_bonus
  c03_aircraft_export_without_margin_delivery_bridge_cap
  c03_price_only_defense_peak_overlay_only
```

## 19. Before / After Backtest Comparison

| profile | selected triggers | avg_MFE_90D | avg_MAE_90D | avg_MFE_180D | avg_MAE_180D | false_positive_rate | verdict |
|---|---:|---:|---:|---:|---:|---:|---|
| P0 e2r_2_1_stock_web_calibrated_proxy | 3 | 23.54 | -12.11 | 40.10 | -15.15 | 0.33 | acceptable but KAI overpromotion remains |
| P0b e2r_2_0_baseline_reference | 3 | 23.54 | -12.11 | 40.10 | -15.15 | 0.33 | too blunt; treats export headlines similarly |
| P1 sector_specific_candidate_profile | 3 | 29.26 | -8.52 | 54.10 | -9.17 | 0.00 among promoted | better separation |
| P2 canonical_archetype_candidate_profile | 3 | 29.26 | -8.52 | 54.10 | -9.17 | 0.00 among promoted | best explanatory fit |
| P3 counterexample_guard_profile | 3 | 23.54 | -12.11 | 40.10 | -15.15 | 0.00 Green false-positive | conservative, may miss early Hanwha |

## 20. Score-Return Alignment Matrix

| case | weighted_score_before | stage_before | weighted_score_after | stage_after | alignment |
|---|---:|---|---:|---|---|
| 012450 | 78.0 | Stage3-Yellow | 83.0 | Stage3-Yellow-high | score increase aligned; still below Green |
| 064350 | 76.0 | Stage3-Yellow | 80.0 | Stage3-Yellow | high-MAE success; do not over-Green |
| 047810 | 74.0 | Stage2-Actionable | 66.0 | Stage2-Watch | cap aligned with low MFE/high MAE |

## 21. Coverage Matrix

| large_sector_id | canonical_archetype_id | fine_archetype_id | positive_case_count | counterexample_count | 4B_case_count | 4C_case_count | new_independent_case_count | reused_case_count | calibration_usable_trigger_count | representative_trigger_count | current_profile_error_count | sector_rule_candidate | canonical_rule_candidate | coverage_gap_after_this_loop |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|---|---|
| L1_INDUSTRIALS_INFRA_DEFENSE_GRID | C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG | DEFENSE_EXPORT_FRAMEWORK_BACKLOG_POLAND_EXECUTIVE_CONTRACT | 2 | 1 | 1 | 1 | 3 | 0 | 5 | 3 | 1 | true | true | Need exact original public-source URLs and more non-Poland holdout cases; C03 has now separated direct framework/executive contract from weaker export headline. |


## 22. Residual Contribution Summary

```text
new_independent_case_count: 3
reused_case_count: 0
reused_case_ids: []
new_symbol_count: 3
new_canonical_archetype_count: 0
new_fine_archetype_count: 2
new_trigger_family_count: 3
tested_existing_calibrated_axes:
  - stage2_actionable_evidence_bonus
  - stage3_yellow_total_min
  - stage3_green_total_min
  - full_4b_requires_non_price_evidence
  - hard_4c_thesis_break_routes_to_4c
residual_error_types_found:
  - aircraft_export_headline_overpromotion
  - missing_margin_delivery_bridge
  - high_MAE_after_export_headline
new_axis_proposed:
  - c03_direct_sovereign_framework_to_executive_contract_bonus
  - c03_aircraft_export_without_margin_delivery_bridge_cap
  - c03_price_only_defense_peak_overlay_only
existing_axis_strengthened:
  - full_4b_requires_non_price_evidence
  - hard_4c_thesis_break_routes_to_4c
existing_axis_weakened: null
existing_axis_kept:
  - stage2_actionable_evidence_bonus
  - stage3_yellow_total_min
sector_specific_rule_candidate: true
canonical_archetype_rule_candidate: true
no_new_signal_reason: null
loop_contribution_label: canonical_archetype_rule_candidate
do_not_propose_new_weight_delta: false
```

## 23. Validation Scope / Non-Validation Scope

Validated:

```text
- stock-web manifest and price basis
- profile availability for 012450, 064350, 047810
- representative entry prices from stock-web tradable shards
- 30D/90D/180D MFE/MAE proxy calculations
- clean 180D corporate-action windows
- R1/L1/C03 schedule consistency
```

Not validated:

```text
- production scoring code
- live watchlist
- brokerage execution
- exact original disclosure URLs for every contract row
- post-2026-02-20 price path
```

## 24. Shadow Weight Calibration

```csv
row_type,axis,scope,large_sector_id,canonical_archetype_id,baseline_value,tested_value,delta,reason,backtest_effect,trigger_ids,calibration_usable_count,new_independent_case_count,counterexample_count,confidence,proposal_type,notes
shadow_weight,c03_direct_sovereign_framework_to_executive_contract_bonus,canonical_archetype_specific,L1_INDUSTRIALS_INFRA_DEFENSE_GRID,C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG,0,+2,+2,"Direct sovereign buyer + framework-to-executive path distinguishes K9/K2 from broad defense theme","positive rows had avg 180D MFE 54.10 pct and manageable MAE","R1L11_T01_HANWHA_STAGE2_POLAND_K9_FRAMEWORK|R1L11_T02_ROTEM_STAGE2_POLAND_K2_FRAMEWORK",3,3,1,medium,canonical_shadow_only,"not production; requires exact evidence URL enrichment"
shadow_weight,c03_aircraft_export_without_margin_delivery_bridge_cap,canonical_archetype_specific,L1_INDUSTRIALS_INFRA_DEFENSE_GRID,C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG,0,-3,-3,"FA-50 headline did not behave like K9/K2 backlog bridge; Green requires delivery/margin/revision proof","counterexample had 180D MFE 12.11 pct and MAE -27.11 pct","R1L11_T03_KAI_STAGE2_FA50_POLAND_CONTRACT",3,3,1,medium,canonical_shadow_only,"do not globally weaken defense; cap aircraft/complex platform Green only"
shadow_weight,c03_price_only_defense_peak_overlay_only,canonical_archetype_specific,L1_INDUSTRIALS_INFRA_DEFENSE_GRID,C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG,0,1,+1,"Local/full-window peaks need non-price 4B evidence before full 4B","prevents price-only exit label from suppressing structural backlog winners too early","R1L11_T01B_HANWHA_4B_FULL_WINDOW_CHECK|R1L11_T03B_KAI_4C_HIGH_MAE_GUARD",3,3,1,low,guardrail_shadow_only,"overlay/risk calibration only"
```

## 25. Machine-Readable Rows

```jsonl
{"row_type":"price_source_validation","source":"Songdaiki/stock-web","source_url":"https://github.com/Songdaiki/stock-web","manifest_path":"atlas/manifest.json","schema_path":"atlas/schema.json","universe_path":"atlas/universe/all_symbols.csv","manifest_max_date":"2026-02-20","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","calibration_shard_root":"atlas/ohlcv_tradable_by_symbol_year","raw_shard_root":"atlas/ohlcv_raw_by_symbol_year","validation_status":"usable_for_historical_calibration"}
{"row_type":"case","case_id":"R1L11_C03_012450_POLAND_K9_HANWHA","symbol":"012450","company_name":"한화에어로스페이스","round":"R1","loop":"11","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG","fine_archetype_id":"DEFENSE_EXPORT_FRAMEWORK_BACKLOG_POLAND_EXECUTIVE_CONTRACT","case_type":"structural_success","positive_or_counterexample":"positive","best_trigger":"R1L11_T01_HANWHA_STAGE2_POLAND_K9_FRAMEWORK","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"stage2 framework + executive contract backlog visibility aligned with large MFE and tolerable MAE","current_profile_verdict":"current_profile_correct","price_source":"Songdaiki/stock-web","notes":"K9 Poland framework/executive-contract route: customer quality and backlog visibility were stronger than a generic defense theme."}
{"row_type":"case","case_id":"R1L11_C03_064350_POLAND_K2_HYUNDAI_ROTEM","symbol":"064350","company_name":"현대로템","round":"R1","loop":"11","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG","fine_archetype_id":"DEFENSE_EXPORT_FRAMEWORK_BACKLOG_POLAND_EXECUTIVE_CONTRACT","case_type":"high_mae_success","positive_or_counterexample":"positive","best_trigger":"R1L11_T02_ROTEM_STAGE2_POLAND_K2_FRAMEWORK","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"confirmed K2 framework/executive route produced MFE, but MAE/drawdown warn against early Green without margin and delivery bridge.","current_profile_verdict":"current_profile_correct","price_source":"Songdaiki/stock-web","notes":"Positive Stage2/Yellow, but not an automatic Green. Needs execution/margin bridge after framework headlines."}
{"row_type":"case","case_id":"R1L11_C03_047810_POLAND_FA50_KAI","symbol":"047810","company_name":"한국항공우주","round":"R1","loop":"11","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG","fine_archetype_id":"DEFENSE_EXPORT_FRAMEWORK_BACKLOG_POLAND_EXECUTION_RISK","case_type":"failed_rerating","positive_or_counterexample":"counterexample","best_trigger":"R1L11_T03_KAI_STAGE2_FA50_POLAND_CONTRACT","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"FA-50 export headline had customer quality, but margin/delivery/backlog conversion was not enough for Green; high MAE and weak full-window capture.","current_profile_verdict":"current_profile_false_positive","price_source":"Songdaiki/stock-web","notes":"Counterexample: same Poland defense export cycle, but aircraft execution/margin bridge was weaker than K9/K2 immediate delivery route."}
{"row_type":"trigger","trigger_id":"R1L11_T01_HANWHA_STAGE2_POLAND_K9_FRAMEWORK","case_id":"R1L11_C03_012450_POLAND_K9_HANWHA","symbol":"012450","company_name":"한화에어로스페이스","round":"R1","loop":"11","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG","fine_archetype_id":"DEFENSE_EXPORT_FRAMEWORK_BACKLOG_POLAND_EXECUTIVE_CONTRACT","sector":"산업재·수주·인프라·방산","primary_archetype":"defense export framework backlog","loop_objective":"coverage_gap_fill|sector_specific_rule_discovery|stage2_actionable_bonus_stress_test","trigger_type":"Stage2-Actionable","trigger_date":"2022-07-29","evidence_available_at_that_date":"Poland K9 framework/executive contract visibility; delivery urgency and direct customer procurement route.","evidence_source":"public defense export reports; exact original URL enrichment required before production promotion","stage2_evidence_fields":["public_event_or_disclosure","customer_or_order_quality","backlog_or_delivery_visibility","policy_or_regulatory_optionality","relative_strength"],"stage3_evidence_fields":["multiple_public_sources","financial_visibility"],"stage4b_evidence_fields":[],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/012/012450/2022.csv|atlas/ohlcv_tradable_by_symbol_year/012/012450/2023.csv","profile_path":"atlas/symbol_profiles/012/012450.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","entry_date":"2022-07-29","entry_price":64400,"MFE_30D_pct":34.78,"MFE_90D_pct":34.78,"MFE_180D_pct":84.47,"MFE_1Y_pct":null,"MFE_2Y_pct":null,"MAE_30D_pct":-6.06,"MAE_90D_pct":-7.61,"MAE_180D_pct":-7.61,"MAE_1Y_pct":null,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2023-04-10","peak_price":118800,"drawdown_after_peak_pct":-27.19,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":null,"four_b_full_window_peak_proximity":null,"four_b_timing_verdict":"not_4B","four_b_evidence_type":[],"four_c_protection_label":"not_applicable","trigger_outcome_label":"structural_success","current_profile_verdict":"current_profile_correct","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"R1L11_012450_20220729_64400","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"R1L11_T01B_HANWHA_4B_FULL_WINDOW_CHECK","case_id":"R1L11_C03_012450_POLAND_K9_HANWHA","symbol":"012450","company_name":"한화에어로스페이스","round":"R1","loop":"11","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG","fine_archetype_id":"DEFENSE_EXPORT_FRAMEWORK_BACKLOG_POLAND_EXECUTIVE_CONTRACT","sector":"산업재·수주·인프라·방산","primary_archetype":"defense export framework backlog","loop_objective":"4B_non_price_requirement_stress_test","trigger_type":"Stage4B-Overlay","trigger_date":"2023-04-10","evidence_available_at_that_date":"Price reached full-window peak; valuation/revision evidence needed before full 4B, otherwise overlay only.","evidence_source":"stock-web price path; non-price 4B evidence URL enrichment required","stage2_evidence_fields":[],"stage3_evidence_fields":["confirmed_revision","financial_visibility"],"stage4b_evidence_fields":["price_only_local_peak","valuation_blowoff"],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/012/012450/2023.csv","profile_path":"atlas/symbol_profiles/012/012450.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","entry_date":"2023-04-10","entry_price":117300,"MFE_30D_pct":1.28,"MFE_90D_pct":1.28,"MFE_180D_pct":1.28,"MFE_1Y_pct":null,"MFE_2Y_pct":null,"MAE_30D_pct":-13.38,"MAE_90D_pct":-27.19,"MAE_180D_pct":-27.19,"MAE_1Y_pct":null,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2023-04-10","peak_price":118800,"drawdown_after_peak_pct":-27.19,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":0.97,"four_b_full_window_peak_proximity":0.97,"four_b_timing_verdict":"good_full_window_4B_timing_if_non_price_evidence_confirmed","four_b_evidence_type":["price_only","valuation_blowoff"],"four_c_protection_label":"thesis_break_watch_only","trigger_outcome_label":"4B_overlay_success","current_profile_verdict":"current_profile_4B_too_late","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"R1L11_012450_20230410_117300","dedupe_for_aggregate":false,"aggregate_group_role":"4B_overlay_only","is_new_independent_case":false,"reuse_reason":"same case 4B overlay timing, not aggregate representative","independent_evidence_weight":0.25,"do_not_count_as_new_case":true}
{"row_type":"trigger","trigger_id":"R1L11_T02_ROTEM_STAGE2_POLAND_K2_FRAMEWORK","case_id":"R1L11_C03_064350_POLAND_K2_HYUNDAI_ROTEM","symbol":"064350","company_name":"현대로템","round":"R1","loop":"11","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG","fine_archetype_id":"DEFENSE_EXPORT_FRAMEWORK_BACKLOG_POLAND_EXECUTIVE_CONTRACT","sector":"산업재·수주·인프라·방산","primary_archetype":"defense export framework backlog","loop_objective":"coverage_gap_fill|sector_specific_rule_discovery|stage2_actionable_bonus_stress_test","trigger_type":"Stage2-Actionable","trigger_date":"2022-07-29","evidence_available_at_that_date":"Poland K2 framework/executive contract path; direct OEM, delivery urgency, later local-production optionality.","evidence_source":"public defense export reports; exact original URL enrichment required before production promotion","stage2_evidence_fields":["public_event_or_disclosure","customer_or_order_quality","backlog_or_delivery_visibility","relative_strength"],"stage3_evidence_fields":["multiple_public_sources"],"stage4b_evidence_fields":[],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/064/064350/2022.csv|atlas/ohlcv_tradable_by_symbol_year/064/064350/2023.csv","profile_path":"atlas/symbol_profiles/064/064350.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","entry_date":"2022-07-29","entry_price":26550,"MFE_30D_pct":23.73,"MFE_90D_pct":23.73,"MFE_180D_pct":23.73,"MFE_1Y_pct":null,"MFE_2Y_pct":null,"MAE_30D_pct":-9.42,"MAE_90D_pct":-9.42,"MAE_180D_pct":-10.73,"MAE_1Y_pct":null,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2022-08-26","peak_price":32850,"drawdown_after_peak_pct":-27.85,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":null,"four_b_full_window_peak_proximity":null,"four_b_timing_verdict":"not_4B","four_b_evidence_type":[],"four_c_protection_label":"not_applicable","trigger_outcome_label":"high_mae_success","current_profile_verdict":"current_profile_correct","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"R1L11_064350_20220729_26550","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"R1L11_T03_KAI_STAGE2_FA50_POLAND_CONTRACT","case_id":"R1L11_C03_047810_POLAND_FA50_KAI","symbol":"047810","company_name":"한국항공우주","round":"R1","loop":"11","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG","fine_archetype_id":"DEFENSE_EXPORT_FRAMEWORK_BACKLOG_POLAND_EXECUTION_RISK","sector":"산업재·수주·인프라·방산","primary_archetype":"defense export framework backlog","loop_objective":"counterexample_mining|4C_thesis_break_timing_test","trigger_type":"Stage2-Actionable","trigger_date":"2022-07-29","evidence_available_at_that_date":"FA-50 Poland contract headline and customer quality; execution/margin/delivery bridge not sufficient for Green.","evidence_source":"public defense export reports; exact original URL enrichment required before production promotion","stage2_evidence_fields":["public_event_or_disclosure","customer_or_order_quality","backlog_or_delivery_visibility"],"stage3_evidence_fields":[],"stage4b_evidence_fields":["positioning_overheat"],"stage4c_evidence_fields":["thesis_evidence_broken"],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/047/047810/2022.csv|atlas/ohlcv_tradable_by_symbol_year/047/047810/2023.csv","profile_path":"atlas/symbol_profiles/047/047810.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","entry_date":"2022-07-29","entry_price":57000,"MFE_30D_pct":12.11,"MFE_90D_pct":12.11,"MFE_180D_pct":12.11,"MFE_1Y_pct":null,"MFE_2Y_pct":null,"MAE_30D_pct":-5.09,"MAE_90D_pct":-19.3,"MAE_180D_pct":-27.11,"MAE_1Y_pct":null,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2022-09-07","peak_price":63900,"drawdown_after_peak_pct":-35.0,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":0.99,"four_b_full_window_peak_proximity":0.99,"four_b_timing_verdict":"price_only_local_4B_too_early_without_margin_or_delivery_slowdown","four_b_evidence_type":["price_only","positioning_overheat"],"four_c_protection_label":"thesis_break_watch_only","trigger_outcome_label":"failed_rerating","current_profile_verdict":"current_profile_false_positive","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"R1L11_047810_20220729_57000","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"R1L11_T03B_KAI_4C_HIGH_MAE_GUARD","case_id":"R1L11_C03_047810_POLAND_FA50_KAI","symbol":"047810","company_name":"한국항공우주","round":"R1","loop":"11","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG","fine_archetype_id":"DEFENSE_EXPORT_FRAMEWORK_BACKLOG_POLAND_EXECUTION_RISK","sector":"산업재·수주·인프라·방산","primary_archetype":"defense export framework backlog","loop_objective":"4C_thesis_break_timing_test|counterexample_mining","trigger_type":"4C-Watch","trigger_date":"2023-03-14","evidence_available_at_that_date":"Full-window price path indicates severe MAE; needs non-price delivery/margin weakness confirmation before hard 4C.","evidence_source":"stock-web price path; non-price 4C evidence URL enrichment required","stage2_evidence_fields":[],"stage3_evidence_fields":[],"stage4b_evidence_fields":["positioning_overheat"],"stage4c_evidence_fields":["thesis_evidence_broken"],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/047/047810/2023.csv","profile_path":"atlas/symbol_profiles/047/047810.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","entry_date":"2023-03-14","entry_price":41550,"MFE_30D_pct":22.74,"MFE_90D_pct":47.65,"MFE_180D_pct":47.65,"MFE_1Y_pct":null,"MFE_2Y_pct":null,"MAE_30D_pct":-1.32,"MAE_90D_pct":-1.32,"MAE_180D_pct":-1.32,"MAE_1Y_pct":null,"below_entry_price_flag_30D":false,"below_entry_price_flag_90D":false,"peak_date":"2023-06-13","peak_price":61350,"drawdown_after_peak_pct":-22.98,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":null,"four_b_full_window_peak_proximity":null,"four_b_timing_verdict":"not_4B","four_b_evidence_type":[],"four_c_protection_label":"false_break_price_only_recovery","trigger_outcome_label":"4C_late_or_false_break","current_profile_verdict":"current_profile_4C_too_late","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"R1L11_047810_20230314_41550","dedupe_for_aggregate":false,"aggregate_group_role":"4C_overlay_only","is_new_independent_case":false,"reuse_reason":"same case hard-4C stress-test, not aggregate representative","independent_evidence_weight":0.25,"do_not_count_as_new_case":true}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"R1L11_C03_012450_POLAND_K9_HANWHA","trigger_id":"R1L11_T01_HANWHA_STAGE2_POLAND_K9_FRAMEWORK","symbol":"012450","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG","raw_component_scores_before":{"contract_score":78,"backlog_visibility_score":72,"margin_bridge_score":55,"revision_score":48,"relative_strength_score":68,"customer_quality_score":83,"policy_or_regulatory_score":65,"valuation_repricing_score":60,"execution_risk_score":28,"legal_or_contract_risk_score":15,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_before":78.0,"stage_label_before":"Stage3-Yellow","raw_component_scores_after":{"contract_score":84,"backlog_visibility_score":80,"margin_bridge_score":60,"revision_score":50,"relative_strength_score":68,"customer_quality_score":88,"policy_or_regulatory_score":68,"valuation_repricing_score":60,"execution_risk_score":24,"legal_or_contract_risk_score":12,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_after":83.0,"stage_label_after":"Stage3-Yellow-high","changed_components":["contract_score","backlog_visibility_score","customer_quality_score"],"component_delta_explanation":"Direct sovereign buyer + framework-to-executive contract bridge increases confidence, but margin/revision proof still caps Green.","MFE_90D_pct":34.78,"MAE_90D_pct":-7.61,"score_return_alignment_label":"stage2 framework + executive contract backlog visibility aligned with large MFE and tolerable MAE","current_profile_verdict":"current_profile_correct"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"R1L11_C03_064350_POLAND_K2_HYUNDAI_ROTEM","trigger_id":"R1L11_T02_ROTEM_STAGE2_POLAND_K2_FRAMEWORK","symbol":"064350","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG","raw_component_scores_before":{"contract_score":76,"backlog_visibility_score":70,"margin_bridge_score":47,"revision_score":44,"relative_strength_score":70,"customer_quality_score":82,"policy_or_regulatory_score":66,"valuation_repricing_score":58,"execution_risk_score":38,"legal_or_contract_risk_score":18,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_before":76.0,"stage_label_before":"Stage3-Yellow","raw_component_scores_after":{"contract_score":80,"backlog_visibility_score":76,"margin_bridge_score":48,"revision_score":44,"relative_strength_score":70,"customer_quality_score":86,"policy_or_regulatory_score":66,"valuation_repricing_score":56,"execution_risk_score":36,"legal_or_contract_risk_score":16,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_after":80.0,"stage_label_after":"Stage3-Yellow","changed_components":["contract_score","backlog_visibility_score","customer_quality_score","execution_risk_score"],"component_delta_explanation":"K2 framework was real and tradeable, but high MAE and later execution/margin need keep it below Green.","MFE_90D_pct":23.73,"MAE_90D_pct":-9.42,"score_return_alignment_label":"confirmed K2 framework/executive route produced MFE, but MAE/drawdown warn against early Green without margin and delivery bridge.","current_profile_verdict":"current_profile_correct"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"R1L11_C03_047810_POLAND_FA50_KAI","trigger_id":"R1L11_T03_KAI_STAGE2_FA50_POLAND_CONTRACT","symbol":"047810","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG","raw_component_scores_before":{"contract_score":74,"backlog_visibility_score":66,"margin_bridge_score":30,"revision_score":35,"relative_strength_score":60,"customer_quality_score":74,"policy_or_regulatory_score":62,"valuation_repricing_score":55,"execution_risk_score":58,"legal_or_contract_risk_score":22,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_before":74.0,"stage_label_before":"Stage2-Actionable","raw_component_scores_after":{"contract_score":68,"backlog_visibility_score":54,"margin_bridge_score":25,"revision_score":32,"relative_strength_score":50,"customer_quality_score":70,"policy_or_regulatory_score":60,"valuation_repricing_score":48,"execution_risk_score":66,"legal_or_contract_risk_score":25,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_after":66.0,"stage_label_after":"Stage2-Watch","changed_components":["backlog_visibility_score","margin_bridge_score","execution_risk_score","valuation_repricing_score"],"component_delta_explanation":"Aircraft export headline should not inherit K9/K2 confidence; missing margin/delivery conversion and high MAE require a cap.","MFE_90D_pct":12.11,"MAE_90D_pct":-19.3,"score_return_alignment_label":"FA-50 export headline had customer quality, but margin/delivery/backlog conversion was not enough for Green; high MAE and weak full-window capture.","current_profile_verdict":"current_profile_false_positive"}
{"row_type":"residual_contribution","round":"R1","loop":"11","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG","new_independent_case_count":3,"reused_case_count":0,"new_symbol_count":3,"new_trigger_family_count":3,"tested_existing_calibrated_axes":["stage2_actionable_evidence_bonus","stage3_yellow_total_min","stage3_green_total_min","full_4b_requires_non_price_evidence","hard_4c_thesis_break_routes_to_4c"],"residual_error_types_found":["aircraft_export_headline_overpromotion","missing_margin_delivery_bridge","price_only_4B_risk","high_MAE_after_export_headline"],"loop_contribution_label":"canonical_archetype_rule_candidate","do_not_propose_new_weight_delta":false}
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
completed_loop = 11
next_round = R2
next_loop = 11
round_schedule_status = valid
round_sector_consistency = pass
```

## 28. Source Notes

- stock-web manifest: atlas/manifest.json
- Hanwha Aerospace stock-web profile: atlas/symbol_profiles/012/012450.json
- Hyundai Rotem stock-web profile: atlas/symbol_profiles/064/064350.json
- KAI stock-web profile: atlas/symbol_profiles/047/047810.json
- Price rows: stock-web tradable shards listed in each trigger row.
- Evidence source notes require exact original URL enrichment before production promotion.
- No live candidate scan, no production patch, no brokerage action.
