# E2R Stock-Web Historical Calibration / Sector-Archetype Residual Research Round

## 0. Research Metadata

```json
{
  "research_session": "post_calibrated_sector_archetype_residual_research",
  "mode": "historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12",
  "scheduled_round": "R5",
  "scheduled_loop": 83,
  "round_schedule_status": "valid",
  "round_sector_consistency": "pass",
  "completed_round": "R5",
  "completed_loop": 83,
  "computed_next_round": "R6",
  "computed_next_loop": 83,
  "large_sector_id": "L5_CONSUMER_BRAND_DISTRIBUTION",
  "canonical_archetype_id": "C19_BRAND_RETAIL_INVENTORY_MARGIN",
  "fine_archetype_id": "CONVENIENCE_RETAIL_TRAFFIC_INVENTORY_MARGIN_RECOVERY_VS_DEPARTMENT_DUTYFREE_APPAREL_DESTOCKING_FADE",
  "loop_objective": [
    "coverage_gap_fill",
    "counterexample_mining",
    "stage2_actionable_bonus_stress_test",
    "4B_non_price_requirement_stress_test",
    "sector_specific_rule_discovery",
    "canonical_archetype_compression",
    "source_repair_queue_creation"
  ],
  "output_file": "e2r_stock_web_v12_residual_round_R5_loop_83_L5_CONSUMER_BRAND_DISTRIBUTION_C19_BRAND_RETAIL_INVENTORY_MARGIN_research.md",
  "price_source": "Songdaiki/stock-web",
  "price_basis": "tradable_raw",
  "price_adjustment_status": "raw_unadjusted_marcap",
  "stock_web_manifest_max_date": "2026-02-20",
  "production_scoring_changed": false,
  "shadow_weight_only": true,
  "handoff_prompt_executed_now": false,
  "do_not_propose_new_weight_delta": true
}
```

This loop adds 3 new independent cases, 2 counterexamples, and 3 residual errors for R5/L5_CONSUMER_BRAND_DISTRIBUTION/C19_BRAND_RETAIL_INVENTORY_MARGIN.

## 1. Current Calibrated Profile Assumption

```text
before_profile_id = e2r_2_1_stock_web_calibrated_proxy
after_profile_id = proposed_C19_inventory_margin_bridge_shadow_profile
rollback_reference_profile_id = e2r_2_0_baseline_reference

production_scoring_changed = false
shadow_weight_only = true
handoff_prompt_executed_now = false
```

Already-applied global axes are treated as baseline, not re-proposed globally:

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

## 2. Round / Large Sector / Canonical Archetype Scope

```text
completed_previous_round = R4
completed_previous_loop = 83
scheduled_round = R5
scheduled_loop = 83
allowed_large_sector = L5_CONSUMER_BRAND_DISTRIBUTION
selected_large_sector = L5_CONSUMER_BRAND_DISTRIBUTION
selected_canonical_archetype_id = C19_BRAND_RETAIL_INVENTORY_MARGIN
computed_next_round = R6
computed_next_loop = 83
round_schedule_status = valid
round_sector_consistency = pass
```

R5 is the consumer / brand / distribution round. This file uses C19 rather than C18/C20 because C19 remains a cleaner inventory-margin stress test: a retailer can show traffic, reopening, or destocking headlines while the back room is still carrying stale inventory or weak gross-margin conversion.

## 3. Previous Coverage / Duplicate Avoidance Check

NO-REPEAT INDEX is used only as a duplicate ledger.

```text
hard_duplicate_key = canonical_archetype_id + symbol + trigger_type + entry_date
```

Current C19 snapshot:

```text
C19_BRAND_RETAIL_INVENTORY_MARGIN:
  rows = 89
  symbols = 17
  date_range = 2021-05-17~2024-10-16
  good/bad Stage2 = 17/14
  4B/4C = 18/7
  top-covered symbols = 111770, 081660, 383220, UNKNOWN_SYMBOL, 020000, 036620
```

This run avoids those top-covered rows and adds:

```text
282330 / BGF리테일 / convenience-store traffic-inventory margin recovery
004170 / 신세계 / department-store/duty-free traffic rebound fade
093050 / LF / apparel destocking optimism fade
```

No hard duplicate is intentionally reused. All selected cases are marked `source_proxy_only=true / evidence_url_pending=true`, therefore they are eligible for source-repair queue creation but not immediate production promotion.

## 4. Stock-Web OHLC Input / Price Source Validation

```text
source = Songdaiki/stock-web
upstream_source = FinanceData/marcap
price_basis = tradable_raw
price_adjustment_status = raw_unadjusted_marcap
calibration_shard_root = atlas/ohlcv_tradable_by_symbol_year
manifest_max_date = 2026-02-20
tradable_row_count = 14354401
raw_row_count = 15214118
symbol_count = 5414
```

Symbol profile checks:

| symbol | company | profile path | corporate_action_candidate_dates | selected 180D status |
|---|---|---|---|---|
| 282330 | BGF리테일 | `atlas/symbol_profiles/282/282330.json` | none | clean |
| 004170 | 신세계 | `atlas/symbol_profiles/004/004170.json` | 1996-01-03, 2004-12-22, 2011-02-01, 2011-02-25, 2011-06-10 | clean for 2024 selected window |
| 093050 | LF | `atlas/symbol_profiles/093/093050.json` | none | clean |

## 5. Historical Eligibility Gate

| case_id | symbol | trigger_date | entry_date | entry_price | 180D forward available | OHLC available | MFE/MAE 30/90/180D | CA contaminated 180D | usable |
|---|---:|---|---|---:|---|---|---|---|---|
| R5L83-C19-01 | 282330 | 2024-07-11 | 2024-07-12 | 103900 | yes | yes | yes | no | true |
| R5L83-C19-02 | 004170 | 2024-05-09 | 2024-05-10 | 176700 | yes | yes | yes | no | true |
| R5L83-C19-03 | 093050 | 2024-03-21 | 2024-03-22 | 14760 | yes | yes | yes | no | true |

Entry rule: when evidence timing is not reliably intraday, the next or same tradable close is used conservatively. All rows use Stock-Web tradable close as entry price.

## 6. Canonical Archetype Compression Map

| canonical | fine/deep path | Stage2 bridge | Green blocker | 4B/4C use |
|---|---|---|---|---|
| C19_BRAND_RETAIL_INVENTORY_MARGIN | CONVENIENCE_RETAIL_TRAFFIC_INVENTORY_MARGIN_RECOVERY | traffic + inventory discipline + margin bridge | none if MAE controlled and margin bridge refreshes | not 4B |
| C19_BRAND_RETAIL_INVENTORY_MARGIN | DEPARTMENT_DUTYFREE_TRAFFIC_BETA_FADE | traffic/reopening headline only | no inventory-turn or gross-margin bridge | local 4B watch only |
| C19_BRAND_RETAIL_INVENTORY_MARGIN | APPAREL_DESTOCKING_OPTIMISM_SMALL_MFE_FADE | generic destocking headline | no sell-through/reorder refresh | cap at Stage2-Watch / local 4B watch |

C19 is the warehouse before the shop window. A retail stock can look busy at the front door while the margin is still stuck in the back room. This file tests whether the system should ask for the back-room ledger: inventory turn, sell-through, reorder, and gross-margin conversion.

## 7. Case Selection Summary

| case_id | role | symbol | company | why selected |
|---|---|---:|---|---|
| R5L83-C19-01 | positive | 282330 | BGF리테일 | New C19 symbol; controlled MAE and recovery path when retail traffic and margin bridge are both present |
| R5L83-C19-02 | counterexample | 004170 | 신세계 | New C19 symbol; traffic/reopening rally showed small MFE and later drawdown without durable margin bridge |
| R5L83-C19-03 | counterexample | 093050 | LF | New C19 symbol; apparel destocking optimism produced small MFE, then MAE widened |

## 8. Positive vs Counterexample Balance

```text
positive_case_count = 1
counterexample_count = 2
4B_case_count = 2
4C_case_count = 0
calibration_usable_case_count = 3
new_independent_case_count = 3
new_independent_case_ratio = 1.00
```

The positive case is not used to propose a global delta because all evidence remains source-proxy. The two counterexamples support a C19-specific guard: traffic/destocking headlines should not receive Stage2-Actionable weight without inventory-margin conversion.

## 9. Evidence Source Map

| case_id | evidence status | source repair need |
|---|---|---|
| R5L83-C19-01 | source_proxy_only=true; evidence_url_pending=true | verify same-store sales/traffic, inventory discipline, gross-margin bridge |
| R5L83-C19-02 | source_proxy_only=true; evidence_url_pending=true | verify duty-free/department traffic headline vs actual margin bridge |
| R5L83-C19-03 | source_proxy_only=true; evidence_url_pending=true | verify apparel inventory cleanup, sell-through, reorder cadence |

## 10. Price Data Source Map

| symbol | shard | profile |
|---|---|---|
| 282330 | `atlas/ohlcv_tradable_by_symbol_year/282/282330/2024.csv` | `atlas/symbol_profiles/282/282330.json` |
| 004170 | `atlas/ohlcv_tradable_by_symbol_year/004/004170/2024.csv` | `atlas/symbol_profiles/004/004170.json` |
| 093050 | `atlas/ohlcv_tradable_by_symbol_year/093/093050/2024.csv` | `atlas/symbol_profiles/093/093050.json` |

## 11. Case-by-Case Trigger Grid

| case | symbol | trigger | entry | entry price | outcome | current profile verdict |
|---|---:|---|---|---:|---|---|
| R5L83-C19-01 | 282330 | Stage2-Actionable | 2024-07-12 | 103900 | structural success after margin bridge | current_profile_missed_structural |
| R5L83-C19-02 | 004170 | Stage2-FalsePositive | 2024-05-10 | 176700 | traffic beta fade | current_profile_false_positive |
| R5L83-C19-03 | 093050 | Stage2-FalsePositive | 2024-03-22 | 14760 | destocking optimism fade | current_profile_false_positive |

## 12. Trigger-Level OHLC Backtest Tables

| case | symbol | entry | MFE 30D | MAE 30D | MFE 90D | MAE 90D | MFE 180D | MAE 180D | peak date | peak price | drawdown after peak |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---|---:|---:|
| R5L83-C19-01 | 282330 | 103900 | 10.88% | -4.72% | 20.31% | -4.72% | 20.31% | -8.85% | 2024-09-25 | 125000 | -12.48% |
| R5L83-C19-02 | 004170 | 176700 | 1.19% | -9.28% | 1.19% | -12.39% | 1.19% | -15.78% | 2024-05-10 | 178800 | -15.78% |
| R5L83-C19-03 | 093050 | 14760 | 7.86% | -0.88% | 7.86% | -8.40% | 7.86% | -16.40% | 2024-03-28 | 15920 | -16.40% |

## 13. Current Calibrated Profile Stress Test

| case | current profile likely action | actual path | verdict |
|---|---|---|---|
| R5L83-C19-01 | Stage2-Watch because C19 evidence was not explicit enough | controlled drawdown and >20% 90D MFE | current_profile_missed_structural |
| R5L83-C19-02 | Stage2-Actionable if traffic beta was over-credited | MFE tiny, MAE widened | current_profile_false_positive |
| R5L83-C19-03 | Stage2-Actionable if destocking was treated as bridge | small MFE and later drawdown | current_profile_false_positive |

Answers to mandatory stress-test questions:

```text
1. current calibrated profile tends to under-credit C19 only when the inventory-margin bridge is present but source evidence is thin.
2. It over-credits traffic/destocking headlines when sell-through and margin conversion are absent.
3. Stage2 actionable bonus is not globally wrong, but C19 needs a bridge requirement.
4. Yellow threshold 75 is acceptable; issue is evidence qualification, not total threshold.
5. Green 87 / revision 55 should remain strict.
6. price-only blowoff guard is appropriate.
7. full 4B non-price requirement is appropriate; C19 fades should be local 4B watch unless margin/revision evidence breaks.
8. hard 4C routing should not be triggered by price-only retail fade.
```

## 14. Stage2 / Yellow / Green Comparison

No confirmed Stage3-Green trigger is used in this file.

```text
green_lateness_ratio = not_applicable
reason = no_confirmed_Stage3_Green_trigger
```

C19 lesson: Stage2 should become actionable only when the chain reaches inventory-turn / sell-through / reorder / margin conversion. If the chain stops at traffic or destocking narrative, the label should remain Stage2-Watch or local 4B watch.

## 15. 4B Local vs Full-window Timing Audit

| case | local 4B proximity | full-window 4B proximity | verdict |
|---|---:|---:|---|
| R5L83-C19-01 | n/a | n/a | no 4B |
| R5L83-C19-02 | 1.00 | 1.00 | good local 4B watch, not full 4B without non-price break |
| R5L83-C19-03 | 0.62 | 0.62 | price-assisted local 4B watch |

## 16. 4C Protection Audit

No hard 4C is proposed.

```text
four_c_protection_label = thesis_break_watch_only or false_break
hard_4c_price_only_allowed_count = 0
```

## 17. Sector-Specific Rule Candidate

```text
rule_scope = canonical_archetype_specific
axis = C19_inventory_margin_bridge_required
candidate_rule =
  For C19 retail/brand inventory-margin rows, Stage2-Actionable should require:
  1. traffic or channel evidence,
  2. inventory-turn or sell-through evidence,
  3. gross-margin or operating-margin bridge,
  4. no severe discount/promotion burden.
```

## 18. Canonical-Archetype Rule Candidate

```text
canonical_archetype_id = C19_BRAND_RETAIL_INVENTORY_MARGIN

positive path:
  traffic / channel normalization
  → inventory turn or sell-through
  → margin bridge
  → controlled MAE
  → durable rerating

counterexample path:
  traffic / reopening / destocking headline
  → no reorder or margin refresh
  → small MFE
  → MAE widens
  → local 4B watch
```

## 19. Before / After Backtest Comparison

| profile | eligible cases | avg MFE 90D | avg MAE 90D | false-positive count | missed structural count | verdict |
|---|---:|---:|---:|---:|---:|---|
| P0 e2r_2_1_stock_web_calibrated_proxy | 3 | 11.45% | -8.50% | 2 | 1 | mixed |
| P0b e2r_2_0_baseline_reference | 3 | 11.45% | -8.50% | 1 | 2 | too conservative for BGF, too loose on traffic beta when price strong |
| P1 sector_specific_candidate_profile | 3 | 11.45% | -8.50% | 1 | 1 | better but still broad |
| P2 canonical_archetype_candidate_profile | 3 | 11.45% | -8.50% | 0 | 0 | best explanation, source repair required |
| P3 counterexample_guard_profile | 2 | 4.53% | -10.40% | 0 | 0 | keeps weak bridge rows out of Actionable |

## 20. Score-Return Alignment Matrix

| case | before stage | after stage | alignment |
|---|---|---|---|
| R5L83-C19-01 | Stage2-Watch | Stage2-Actionable | improved; bridge explains MFE |
| R5L83-C19-02 | Stage2-Actionable | Stage2-Watch | improved; weak bridge explains fade |
| R5L83-C19-03 | Stage2-Actionable | Stage2-Watch | improved; weak bridge explains fade |

## 21. Coverage Matrix

| large_sector_id | canonical_archetype_id | fine_archetype_id | positives | counterexamples | 4B | 4C | new independent | reused | usable triggers | representative triggers | current profile errors | sector rule candidate | canonical rule candidate | coverage gap after loop |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|---|---|
| L5_CONSUMER_BRAND_DISTRIBUTION | C19_BRAND_RETAIL_INVENTORY_MARGIN | CONVENIENCE_RETAIL_TRAFFIC_INVENTORY_MARGIN_RECOVERY_VS_DEPARTMENT_DUTYFREE_APPAREL_DESTOCKING_FADE | 1 | 2 | 2 | 0 | 3 | 0 | 3 | 3 | 3 | no | yes | still needs source URL repair and more non-proxy positives |

## 22. Residual Contribution Summary

```text
new_independent_case_count: 3
reused_case_count: 0
reused_case_ids: []
new_symbol_count: 3
new_canonical_archetype_count: 0
new_fine_archetype_count: 1
new_trigger_family_count: 3
tested_existing_calibrated_axes:
  - stage2_actionable_evidence_bonus
  - price_only_blowoff_blocks_positive_stage
  - full_4b_requires_non_price_evidence
  - hard_4c_thesis_break_routes_to_4c
residual_error_types_found:
  - current_profile_missed_structural
  - current_profile_false_positive
  - local_4b_watch_after_weak_bridge
new_axis_proposed: null
existing_axis_strengthened: C19_inventory_margin_bridge_required
existing_axis_weakened: null
existing_axis_kept:
  - stage3_green_total_min
  - full_4b_requires_non_price_evidence
sector_specific_rule_candidate: null
canonical_archetype_rule_candidate: C19_inventory_margin_bridge_required
no_new_signal_reason: null
loop_contribution_label: canonical_archetype_rule_candidate
do_not_propose_new_weight_delta: true
```

## 23. Validation Scope / Non-Validation Scope

Validated:

```text
- scheduled_round / scheduled_loop consistency
- R5 -> L5 round-sector consistency
- C19 canonical archetype mapping
- Stock-Web manifest/schema/profile route
- 1D OHLC entry / MFE / MAE / peak / drawdown calculation
- no intentional hard duplicate reuse
```

Not validated:

```text
- external source URL confirmation
- DART/report/news evidence source repair
- production scoring implementation
- live candidate scan
```

## 24. Shadow Weight Calibration

```csv
row_type,axis,scope,large_sector_id,canonical_archetype_id,baseline_value,tested_value,delta,reason,backtest_effect,trigger_ids,calibration_usable_count,new_independent_case_count,counterexample_count,confidence,proposal_type,notes
shadow_weight,C19_inventory_margin_bridge_required,canonical_archetype_specific,L5_CONSUMER_BRAND_DISTRIBUTION,C19_BRAND_RETAIL_INVENTORY_MARGIN,0,1,+1,"Require sell-through/reorder/inventory-turn plus margin bridge before C19 Stage2-Actionable promotion","BGF retail path positive while Shinsegae/LF fade without bridge","R5L83-C19-01-T1|R5L83-C19-02-T1|R5L83-C19-03-T1",3,3,2,low,canonical_shadow_only,"source_proxy_only; do not apply before evidence URL repair"
shadow_weight,C19_department_dutyfree_and_apparel_fade_guard,canonical_archetype_specific,L5_CONSUMER_BRAND_DISTRIBUTION,C19_BRAND_RETAIL_INVENTORY_MARGIN,0,1,+1,"Cap traffic/destocking headlines without inventory-margin conversion at Stage2-Watch or local 4B watch","Reduces false positive labels for high-MAE or low-MFE retail rebounds","R5L83-C19-02-T1|R5L83-C19-03-T1",2,2,2,low,canonical_shadow_only,"not production; post-calibrated residual"
```

## 25. Machine-Readable Rows

```jsonl
{"row_type": "price_source_validation", "source": "Songdaiki/stock-web", "source_url": "https://github.com/Songdaiki/stock-web", "manifest_path": "atlas/manifest.json", "schema_path": "atlas/schema.json", "universe_path": "atlas/universe/all_symbols.csv", "manifest_max_date": "2026-02-20", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "raw_shard_root": "atlas/ohlcv_raw_by_symbol_year", "validation_status": "usable_for_historical_calibration"}
{"row_type": "case", "case_id": "R5L83-C19-01", "symbol": "282330", "company_name": "BGF리테일", "round": "R5", "loop": "83", "large_sector_id": "L5_CONSUMER_BRAND_DISTRIBUTION", "canonical_archetype_id": "C19_BRAND_RETAIL_INVENTORY_MARGIN", "fine_archetype_id": "CONVENIENCE_RETAIL_TRAFFIC_INVENTORY_MARGIN_RECOVERY_VS_DEPARTMENT_DUTYFREE_APPAREL_DESTOCKING_FADE", "case_type": "structural_success", "positive_or_counterexample": "positive", "best_trigger": "Stage2-Actionable", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "structural_success_after_margin_bridge", "current_profile_verdict": "current_profile_missed_structural", "price_source": "Songdaiki/stock-web", "notes": "source_proxy_only=true; evidence_url_pending=true; use as source-repair queue before runtime promotion"}
{"row_type": "case", "case_id": "R5L83-C19-02", "symbol": "004170", "company_name": "신세계", "round": "R5", "loop": "83", "large_sector_id": "L5_CONSUMER_BRAND_DISTRIBUTION", "canonical_archetype_id": "C19_BRAND_RETAIL_INVENTORY_MARGIN", "fine_archetype_id": "CONVENIENCE_RETAIL_TRAFFIC_INVENTORY_MARGIN_RECOVERY_VS_DEPARTMENT_DUTYFREE_APPAREL_DESTOCKING_FADE", "case_type": "failed_rerating", "positive_or_counterexample": "counterexample", "best_trigger": "Stage2-FalsePositive", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "stage2_false_positive_theme_fade", "current_profile_verdict": "current_profile_false_positive", "price_source": "Songdaiki/stock-web", "notes": "source_proxy_only=true; evidence_url_pending=true; use as source-repair queue before runtime promotion"}
{"row_type": "case", "case_id": "R5L83-C19-03", "symbol": "093050", "company_name": "LF", "round": "R5", "loop": "83", "large_sector_id": "L5_CONSUMER_BRAND_DISTRIBUTION", "canonical_archetype_id": "C19_BRAND_RETAIL_INVENTORY_MARGIN", "fine_archetype_id": "CONVENIENCE_RETAIL_TRAFFIC_INVENTORY_MARGIN_RECOVERY_VS_DEPARTMENT_DUTYFREE_APPAREL_DESTOCKING_FADE", "case_type": "failed_rerating", "positive_or_counterexample": "counterexample", "best_trigger": "Stage2-FalsePositive", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "inventory_cleanup_headline_failed_rerating", "current_profile_verdict": "current_profile_false_positive", "price_source": "Songdaiki/stock-web", "notes": "source_proxy_only=true; evidence_url_pending=true; use as source-repair queue before runtime promotion"}
{"row_type": "trigger", "trigger_id": "R5L83-C19-01-T1", "case_id": "R5L83-C19-01", "symbol": "282330", "company_name": "BGF리테일", "round": "R5", "loop": "83", "large_sector_id": "L5_CONSUMER_BRAND_DISTRIBUTION", "canonical_archetype_id": "C19_BRAND_RETAIL_INVENTORY_MARGIN", "fine_archetype_id": "CONVENIENCE_RETAIL_TRAFFIC_INVENTORY_MARGIN_RECOVERY_VS_DEPARTMENT_DUTYFREE_APPAREL_DESTOCKING_FADE", "sector": "consumer_brand_distribution", "primary_archetype": "brand_retail_inventory_margin", "loop_objective": "coverage_gap_fill|counterexample_mining|stage2_actionable_bonus_stress_test|4B_non_price_requirement_stress_test", "trigger_type": "Stage2-Actionable", "trigger_date": "2024-07-11", "evidence_available_at_that_date": "Convenience-store traffic/inventory discipline and margin recovery proxy; source URL pending.", "evidence_source": "source_proxy_only:true; evidence_url_pending:true", "stage2_evidence_fields": ["same-store traffic proxy", "inventory discipline", "gross-margin recovery candidate"], "stage3_evidence_fields": ["controlled MAE", "retail margin bridge", "channel repeatability"], "stage4b_evidence_fields": [], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/282/282330/2024.csv", "profile_path": "atlas/symbol_profiles/282/282330.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "entry_date": "2024-07-12", "entry_price": 103900, "MFE_30D_pct": 10.88, "MFE_90D_pct": 20.31, "MFE_180D_pct": 20.31, "MFE_1Y_pct": null, "MFE_2Y_pct": null, "MAE_30D_pct": -4.72, "MAE_90D_pct": -4.72, "MAE_180D_pct": -8.85, "MAE_1Y_pct": null, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2024-09-25", "peak_price": 125000, "drawdown_after_peak_pct": -12.48, "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": null, "four_b_full_window_peak_proximity": null, "four_b_timing_verdict": "not_applicable", "four_b_evidence_type": [], "four_c_protection_label": "not_applicable", "trigger_outcome_label": "structural_success_after_margin_bridge", "current_profile_verdict": "current_profile_missed_structural", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window", "same_entry_group_id": "R5L83-C19-01-ENTRY", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false}
{"row_type": "trigger", "trigger_id": "R5L83-C19-02-T1", "case_id": "R5L83-C19-02", "symbol": "004170", "company_name": "신세계", "round": "R5", "loop": "83", "large_sector_id": "L5_CONSUMER_BRAND_DISTRIBUTION", "canonical_archetype_id": "C19_BRAND_RETAIL_INVENTORY_MARGIN", "fine_archetype_id": "CONVENIENCE_RETAIL_TRAFFIC_INVENTORY_MARGIN_RECOVERY_VS_DEPARTMENT_DUTYFREE_APPAREL_DESTOCKING_FADE", "sector": "consumer_brand_distribution", "primary_archetype": "brand_retail_inventory_margin", "loop_objective": "coverage_gap_fill|counterexample_mining|stage2_actionable_bonus_stress_test|4B_non_price_requirement_stress_test", "trigger_type": "Stage2-FalsePositive", "trigger_date": "2024-05-09", "evidence_available_at_that_date": "Department-store/duty-free traffic rebound proxy without durable inventory-margin bridge; source URL pending.", "evidence_source": "source_proxy_only:true; evidence_url_pending:true", "stage2_evidence_fields": ["traffic rebound proxy", "duty-free reopening beta"], "stage3_evidence_fields": [], "stage4b_evidence_fields": ["margin bridge not refreshed", "post-peak drawdown"], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/004/004170/2024.csv", "profile_path": "atlas/symbol_profiles/004/004170.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "entry_date": "2024-05-10", "entry_price": 176700, "MFE_30D_pct": 1.19, "MFE_90D_pct": 1.19, "MFE_180D_pct": 1.19, "MFE_1Y_pct": null, "MFE_2Y_pct": null, "MAE_30D_pct": -9.28, "MAE_90D_pct": -12.39, "MAE_180D_pct": -15.78, "MAE_1Y_pct": null, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2024-05-10", "peak_price": 178800, "drawdown_after_peak_pct": -15.78, "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": 1.0, "four_b_full_window_peak_proximity": 1.0, "four_b_timing_verdict": "good_local_4B_watch_but_not_full_4B_without_non_price_break", "four_b_evidence_type": ["margin_or_backlog_slowdown", "positioning_overheat"], "four_c_protection_label": "thesis_break_watch_only", "trigger_outcome_label": "stage2_false_positive_theme_fade", "current_profile_verdict": "current_profile_false_positive", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window", "same_entry_group_id": "R5L83-C19-02-ENTRY", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false}
{"row_type": "trigger", "trigger_id": "R5L83-C19-03-T1", "case_id": "R5L83-C19-03", "symbol": "093050", "company_name": "LF", "round": "R5", "loop": "83", "large_sector_id": "L5_CONSUMER_BRAND_DISTRIBUTION", "canonical_archetype_id": "C19_BRAND_RETAIL_INVENTORY_MARGIN", "fine_archetype_id": "CONVENIENCE_RETAIL_TRAFFIC_INVENTORY_MARGIN_RECOVERY_VS_DEPARTMENT_DUTYFREE_APPAREL_DESTOCKING_FADE", "sector": "consumer_brand_distribution", "primary_archetype": "brand_retail_inventory_margin", "loop_objective": "coverage_gap_fill|counterexample_mining|stage2_actionable_bonus_stress_test|4B_non_price_requirement_stress_test", "trigger_type": "Stage2-FalsePositive", "trigger_date": "2024-03-21", "evidence_available_at_that_date": "Apparel destocking and inventory cleanup proxy, but weak reorder/sell-through evidence; source URL pending.", "evidence_source": "source_proxy_only:true; evidence_url_pending:true", "stage2_evidence_fields": ["destocking optimism", "inventory cleanup proxy"], "stage3_evidence_fields": [], "stage4b_evidence_fields": ["small MFE", "later MAE widening"], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/093/093050/2024.csv", "profile_path": "atlas/symbol_profiles/093/093050.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "entry_date": "2024-03-22", "entry_price": 14760, "MFE_30D_pct": 7.86, "MFE_90D_pct": 7.86, "MFE_180D_pct": 7.86, "MFE_1Y_pct": null, "MFE_2Y_pct": null, "MAE_30D_pct": -0.88, "MAE_90D_pct": -8.4, "MAE_180D_pct": -16.4, "MAE_1Y_pct": null, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2024-03-28", "peak_price": 15920, "drawdown_after_peak_pct": -16.4, "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": 0.62, "four_b_full_window_peak_proximity": 0.62, "four_b_timing_verdict": "price_assisted_local_4B_watch", "four_b_evidence_type": ["revision_slowdown", "margin_or_backlog_slowdown"], "four_c_protection_label": "false_break", "trigger_outcome_label": "inventory_cleanup_headline_failed_rerating", "current_profile_verdict": "current_profile_false_positive", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window", "same_entry_group_id": "R5L83-C19-03-ENTRY", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R5L83-C19-01", "trigger_id": "R5L83-C19-01-T1", "symbol": "282330", "large_sector_id": "L5_CONSUMER_BRAND_DISTRIBUTION", "canonical_archetype_id": "C19_BRAND_RETAIL_INVENTORY_MARGIN", "raw_component_scores_before": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 52, "revision_score": 42, "relative_strength_score": 45, "customer_quality_score": 58, "policy_or_regulatory_score": 0, "valuation_repricing_score": 44, "execution_risk_score": 28, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 10}, "weighted_score_before": 72, "stage_label_before": "Stage2-Watch", "raw_component_scores_after": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 65, "revision_score": 48, "relative_strength_score": 50, "customer_quality_score": 65, "policy_or_regulatory_score": 0, "valuation_repricing_score": 47, "execution_risk_score": 24, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 10}, "weighted_score_after": 77, "stage_label_after": "Stage2-Actionable", "changed_components": ["margin_bridge_score", "revision_score", "customer_quality_score", "execution_risk_score"], "component_delta_explanation": "C19 convenience-store positive needs traffic/inventory/margin bridge; when bridge is present, current profile may under-credit controlled MAE plus gradual MFE.", "MFE_90D_pct": 20.31, "MAE_90D_pct": -4.72, "score_return_alignment_label": "structural_success_after_margin_bridge", "current_profile_verdict": "current_profile_missed_structural"}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R5L83-C19-02", "trigger_id": "R5L83-C19-02-T1", "symbol": "004170", "large_sector_id": "L5_CONSUMER_BRAND_DISTRIBUTION", "canonical_archetype_id": "C19_BRAND_RETAIL_INVENTORY_MARGIN", "raw_component_scores_before": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 45, "revision_score": 41, "relative_strength_score": 55, "customer_quality_score": 50, "policy_or_regulatory_score": 0, "valuation_repricing_score": 58, "execution_risk_score": 44, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 12}, "weighted_score_before": 76, "stage_label_before": "Stage2-Actionable", "raw_component_scores_after": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 30, "revision_score": 34, "relative_strength_score": 42, "customer_quality_score": 45, "policy_or_regulatory_score": 0, "valuation_repricing_score": 45, "execution_risk_score": 55, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 12}, "weighted_score_after": 67, "stage_label_after": "Stage2-Watch", "changed_components": ["margin_bridge_score", "revision_score", "customer_quality_score", "execution_risk_score"], "component_delta_explanation": "Department/duty-free traffic beta without inventory-turn or margin bridge should not receive C19 actionable weight.", "MFE_90D_pct": 1.19, "MAE_90D_pct": -12.39, "score_return_alignment_label": "stage2_false_positive_theme_fade", "current_profile_verdict": "current_profile_false_positive"}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R5L83-C19-03", "trigger_id": "R5L83-C19-03-T1", "symbol": "093050", "large_sector_id": "L5_CONSUMER_BRAND_DISTRIBUTION", "canonical_archetype_id": "C19_BRAND_RETAIL_INVENTORY_MARGIN", "raw_component_scores_before": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 48, "revision_score": 40, "relative_strength_score": 48, "customer_quality_score": 42, "policy_or_regulatory_score": 0, "valuation_repricing_score": 50, "execution_risk_score": 36, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 10}, "weighted_score_before": 74, "stage_label_before": "Stage2-Actionable", "raw_component_scores_after": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 28, "revision_score": 32, "relative_strength_score": 35, "customer_quality_score": 35, "policy_or_regulatory_score": 0, "valuation_repricing_score": 38, "execution_risk_score": 52, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 10}, "weighted_score_after": 64, "stage_label_after": "Stage2-Watch", "changed_components": ["margin_bridge_score", "revision_score", "customer_quality_score", "execution_risk_score"], "component_delta_explanation": "Apparel destocking optimism needs sell-through/reorder and margin breath; otherwise C19 Stage2 should be capped.", "MFE_90D_pct": 7.86, "MAE_90D_pct": -8.4, "score_return_alignment_label": "inventory_cleanup_headline_failed_rerating", "current_profile_verdict": "current_profile_false_positive"}
{"row_type": "residual_contribution", "round": "R5", "loop": "83", "large_sector_id": "L5_CONSUMER_BRAND_DISTRIBUTION", "canonical_archetype_id": "C19_BRAND_RETAIL_INVENTORY_MARGIN", "new_independent_case_count": 3, "reused_case_count": 0, "new_symbol_count": 3, "new_trigger_family_count": 3, "tested_existing_calibrated_axes": ["stage2_actionable_evidence_bonus", "price_only_blowoff_blocks_positive_stage", "full_4b_requires_non_price_evidence", "hard_4c_thesis_break_routes_to_4c"], "residual_error_types_found": ["current_profile_missed_structural", "current_profile_false_positive", "local_4b_watch_after_weak_bridge"], "loop_contribution_label": "canonical_archetype_rule_candidate", "do_not_propose_new_weight_delta": true}
{"row_type": "narrative_only", "case_id": "R5L83-C19-SOURCE-REPAIR", "symbol": "MULTI", "large_sector_id": "L5_CONSUMER_BRAND_DISTRIBUTION", "canonical_archetype_id": "C19_BRAND_RETAIL_INVENTORY_MARGIN", "reason": "all non-price evidence is source_proxy_only/evidence_url_pending; use for queue creation before runtime promotion", "price_source": "Songdaiki/stock-web", "usage": "source_repair_and_shadow_guardrail_only"}
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
- Do not treat source_proxy_only or evidence_url_pending rows as runtime promotion evidence before source repair.
- Keep schema_rematerialization_only / duplicate_low_value_loop out of future weight deltas.
- For this MD, treat `C19_inventory_margin_bridge_required` as a canonical-archetype shadow guard only.

### Suggested implementation queue

```text
1. Parse all trigger rows from this MD.
2. Verify exact hard duplicate keys against v12_trigger_rows_validated.jsonl.
3. Repair source URLs for 282330 / 004170 / 093050.
4. Promote only after source repair confirms inventory-turn / sell-through / margin bridge fields.
5. Keep do_not_propose_new_weight_delta=true until URL repair and non-proxy evidence pass.
```

## 27. Next Round State

```text
completed_round = R5
completed_loop = 83
next_round = R6
next_loop = 83
round_schedule_status = valid
round_sector_consistency = pass
```

## 28. Source Notes

```text
MAIN_EXECUTION_PROMPT = docs/core/e2r_v12_prompt_round_scheduler_corrected.txt
NO_REPEAT_INDEX = docs/core/V12_Research_No_Repeat_Index.md
price_atlas_repo = Songdaiki/stock-web
manifest = atlas/manifest.json
schema = atlas/schema.json
production_scoring_changed = false
shadow_weight_only = true
source_proxy_only_count = 3
evidence_url_pending_count = 3
```
