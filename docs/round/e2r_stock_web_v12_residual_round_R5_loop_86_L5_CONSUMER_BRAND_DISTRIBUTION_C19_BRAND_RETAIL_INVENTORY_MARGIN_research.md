# E2R Stock-Web v12 Residual Research — R5 Loop 86 / L5 / C19

## 0. Research Metadata

```json
{
  "research_session": "post_calibrated_sector_archetype_residual_research",
  "mode": "historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12",
  "scheduled_round": "R5",
  "scheduled_loop": 86,
  "round_schedule_status": "valid",
  "round_sector_consistency": "pass",
  "completed_round": "R5",
  "completed_loop": 86,
  "computed_next_round": "R6",
  "computed_next_loop": 86,
  "large_sector_id": "L5_CONSUMER_BRAND_DISTRIBUTION",
  "canonical_archetype_id": "C19_BRAND_RETAIL_INVENTORY_MARGIN",
  "fine_archetype_id": "ATHLEISURE_FASHION_BEAUTY_BRAND_INVENTORY_NORMALIZATION_SELLTHROUGH_ARPU_MARGIN_BRIDGE_VS_RETAIL_THEME_FADE",
  "loop_objective": [
    "coverage_gap_fill",
    "counterexample_mining",
    "brand_retail_inventory_margin_guardrail",
    "inventory_normalization_to_sellthrough_margin_bridge_test",
    "brand_theme_MFE_vs_channel_reorder_ARPU_margin_bridge_test",
    "local_4B_timing_after_brand_retail_MFE",
    "source_proxy_runtime_promotion_blocker",
    "high_MAE_guardrail",
    "canonical_archetype_compression",
    "source_repair_queue_creation"
  ],
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

## 1. Current Calibrated Profile Assumption

```text
current_default_profile_proxy = e2r_2_1_stock_web_calibrated
previous_baseline_reference = e2r_2_0_baseline
production_scoring_changed = false
shadow_weight_only = true
handoff_prompt_executed_now = false
```

This file is a standalone historical calibration / sector-archetype residual research artifact. It does not patch `stock_agent`, does not run live discovery, and does not propose immediate production scoring changes.

## 2. Round / Large Sector / Canonical Archetype Scope

```text
scheduled_round = R5
scheduled_loop = 86
allowed_large_sector = L5_CONSUMER_BRAND_DISTRIBUTION
selected_large_sector = L5_CONSUMER_BRAND_DISTRIBUTION
selected_canonical_archetype_id = C19_BRAND_RETAIL_INVENTORY_MARGIN
computed_next_round = R6
computed_next_loop = 86
round_schedule_status = valid
round_sector_consistency = pass
```

R5 is the consumer / brand / distribution round. This run selects C19 because loop84 used C18 and loop85 used C20. C19 is the remaining consumer-brand route in this rotation.

The tested mechanism:

```text
brand / fashion / athleisure / retail inventory rebound headline
→ channel sell-through
→ inventory turns and reorder cadence
→ ASP or discount control
→ ARPU / product mix
→ gross-margin conversion
→ durable rerating or retail-theme fade
```

C19 is the fitting room and the warehouse together. The model should not call a brand rebound clean Green until the product actually sells through, reorders, and carries margin.

## 3. Previous Coverage / Duplicate Avoidance Check

No-Repeat is used only as a duplicate ledger.

```text
hard_duplicate_key = canonical_archetype_id + symbol + trigger_type + entry_date
```

C19 top-covered symbols include `111770`, `081660`, `383220`, `UNKNOWN_SYMBOL`, `020000`, and `036620`. This run avoids that top-covered set and uses:

```text
337930 / 브랜드엑스코퍼레이션
093050 / LF
031430 / 신세계인터내셔날
```

All three are treated as new independent C19 brand-retail inventory/margin cases for this loop. No hard duplicate is intentionally reused.

## 4. Stock-Web OHLC Input / Price Source Validation

```text
price_source = Songdaiki/stock-web
source_basis = FinanceData/marcap transformed into symbol-year CSV shards
price_basis = tradable_raw
price_adjustment_status = raw_unadjusted_marcap
manifest_max_date = 2026-02-20
calibration_shard_root = atlas/ohlcv_tradable_by_symbol_year
```

Per-symbol profile status:

| symbol | company | profile path | corporate-action caveat |
|---|---|---|---|
| 337930 | 브랜드엑스코퍼레이션 | `atlas/symbol_profiles/337/337930.json` | old 2021 CA candidate; selected 2024/2025 forward window clean |
| 093050 | LF | `atlas/symbol_profiles/093/093050.json` | no profile-level CA candidate |
| 031430 | 신세계인터내셔날 | `atlas/symbol_profiles/031/031430.json` | old 2022 CA candidate; selected 2024 forward window clean |

## 5. Historical Eligibility Gate

| case_id | symbol | entry_date | entry_price | forward window | 180D status | calibration_usable |
|---|---:|---|---:|---:|---|---|
| R5L86-C19-01 | 337930 | 2024-06-26 | 6,290 | 180D | clean | true |
| R5L86-C19-02 | 093050 | 2024-03-07 | 13,640 | 180D | clean | true |
| R5L86-C19-03 | 031430 | 2024-03-07 | 15,870 | 180D | clean | true |

## 6. Canonical Archetype Compression Map

| canonical_archetype_id | fine/deep route | keep / reject logic |
|---|---|---|
| C19_BRAND_RETAIL_INVENTORY_MARGIN | ATHLEISURE_DTC_BRAND_INVENTORY_MARGIN | keep Stage2 with sell-through, reorder, ASP/mix and margin bridge; add local 4B after MFE |
| C19_BRAND_RETAIL_INVENTORY_MARGIN | VALUE_FASHION_BRAND_MARGIN_RECOVERY | keep Stage2 only with inventory-turn and margin bridge watch |
| C19_BRAND_RETAIL_INVENTORY_MARGIN | FASHION_BEAUTY_RETAIL_REBOUND_FADE | reject fashion/beauty rebound without sell-through, discount and margin bridge |

## 7. Case Selection Summary

| case_id | symbol | company | trigger_type | entry_date | entry_price | MFE_180D_pct | MAE_180D_pct | current_profile_verdict |
|---|---:|---|---|---|---:|---:|---:|---|
| R5L86-C19-01 | 337930 | 브랜드엑스코퍼레이션 | Stage2-Actionable | 2024-06-26 | 6,290 | 112.72 | -6.99 | current_profile_partially_correct_local_4B_watch_needed |
| R5L86-C19-02 | 093050 | LF | Stage2-Actionable | 2024-03-07 | 13,640 | 16.72 | -4.03 | current_profile_partially_correct_inventory_margin_bridge_needed |
| R5L86-C19-03 | 031430 | 신세계인터내셔날 | Stage2-FalsePositive | 2024-03-07 | 15,870 | 15.69 | -21.93 | current_profile_false_positive_inventory_margin_bridge_gap |

## 8. Positive vs Counterexample Balance

```text
positive_case_count = 2
counterexample_count = 1
4B_or_4C_case_count = 3
calibration_usable_case_count = 3
new_independent_case_count = 3
```

## 9. Evidence Source Map

All selected evidence is currently `source_proxy_only=true / evidence_url_pending=true`.

This MD creates a source-repair queue and a C19 shadow guardrail candidate. It must not be promoted directly into runtime weights until a later source-repair pass attaches primary evidence URLs: channel sell-through, inventory turns, reorder cadence, ASP/discount control, ARPU/product mix, gross-margin bridge, disclosure or report evidence.

## 10. Price Data Source Map

| symbol | shard path | profile path |
|---|---|---|
| 337930 | `atlas/ohlcv_tradable_by_symbol_year/337/337930/2024.csv` and `2025.csv` | `atlas/symbol_profiles/337/337930.json` |
| 093050 | `atlas/ohlcv_tradable_by_symbol_year/093/093050/2024.csv` | `atlas/symbol_profiles/093/093050.json` |
| 031430 | `atlas/ohlcv_tradable_by_symbol_year/031/031430/2024.csv` | `atlas/symbol_profiles/031/031430.json` |

## 11. Case-by-Case Trigger Grid

### Case 1 — 337930 / 브랜드엑스코퍼레이션

C19 athleisure/DTC brand positive with local 4B watch. The June entry produced a very large MFE into July~October, but the later 2025 drawdown shows why clean Green requires sell-through, inventory and margin source repair.

### Case 2 — 093050 / LF

C19 value-fashion brand positive with controlled MAE. The March entry generated moderate MFE and contained MAE, but the return profile is not strong enough for clean Green unless inventory turns, channel mix and margin conversion are verified.

### Case 3 — 031430 / 신세계인터내셔날

C19 fashion/beauty inventory rebound false positive. The early rebound MFE faded into a larger drawdown. This rejects brand/inventory rebound language without sell-through, discount control and gross-margin bridge.

## 12. Trigger-Level OHLC Backtest Tables

| symbol | entry | MFE30 | MAE30 | MFE90 | MAE90 | MFE180 | MAE180 | peak | post-peak DD |
|---|---:|---:|---:|---:|---:|---:|---:|---|---:|
| 337930 | 6,290 | 45.31 | -4.61 | 112.72 | -4.61 | 112.72 | -6.99 | 2024-10-07 / 13,380 | -57.25 |
| 093050 | 13,640 | 16.72 | -0.88 | 16.72 | -4.03 | 16.72 | -4.03 | 2024-03-28 / 15,920 | -17.78 |
| 031430 | 15,870 | 15.69 | -1.76 | 15.69 | -9.39 | 15.69 | -21.93 | 2024-04-01 / 18,360 | -32.52 |

## 13. Current Calibrated Profile Stress Test

| case_id | P0 likely behavior | actual path | verdict |
|---|---|---|---|
| R5L86-C19-01 | Stage2-Actionable if inventory/margin bridge exists | large MFE, later drawdown | partially correct; local 4B/inventory-margin watch needed |
| R5L86-C19-02 | Stage2-Actionable if inventory normalization exists | moderate MFE, controlled MAE | partially correct; bridge required |
| R5L86-C19-03 | risk of treating fashion/beauty rebound as Stage2 | early MFE then larger MAE | false positive |

## 14. Stage2 / Yellow / Green Comparison

```text
green_lateness_ratio = not_applicable
reason = no confirmed Stage3-Green trigger is assigned in this residual MD
```

For C19, the residual is whether brand-retail MFE becomes clean Stage2/Green before sell-through, inventory turns, discount control and margin conversion are proven.

## 15. 4B Local vs Full-window Timing Audit

| case_id | local proximity | full-window proximity | verdict |
|---|---:|---:|---|
| R5L86-C19-01 | 0.88 | 0.78 | local 4B watch after DTC brand MFE if sell-through/inventory/margin bridge stalls |
| R5L86-C19-02 | 0.70 | 0.60 | brand value MFE allowed only with inventory margin bridge watch |
| R5L86-C19-03 | 0.35 | 0.30 | brand inventory rebound rejected without sell-through/discount/margin bridge |

## 16. 4C Protection Audit

No hard 4C is promoted from this file.

```text
four_c_protection_label = hard_4C_requires_non_price_inventory_or_channel_demand_break
hard_4c_price_only_allowed = false
```

Price drawdown alone is not hard 4C. C19 hard 4C requires confirmed inventory impairment, channel demand break, sell-through failure, ASP/discount compression, reorder collapse or margin thesis break.

## 17. Sector-Specific Rule Candidate

```text
rule_scope = no_new_global_rule
sector_specific_rule_candidate = L5/C19 brand-retail rows need sell-through, inventory turns, reorder cadence, ASP/discount control, ARPU/mix and gross-margin conversion before clean Stage2/Green
confidence = low
reason = all evidence rows are source_proxy_only / evidence_url_pending
```

## 18. Canonical-Archetype Rule Candidate

```text
canonical_archetype_id = C19_BRAND_RETAIL_INVENTORY_MARGIN
candidate_axis = C19_brand_retail_sellthrough_inventory_discount_margin_bridge_required
effect = keep DTC/value-brand positives with local 4B/inventory-margin watch; demote fashion/beauty rebound false positives
production_scoring_changed = false
shadow_weight_only = true
do_not_propose_new_weight_delta = true
```

## 19. Before / After Backtest Comparison

| profile | eligible triggers | avg MFE90 | avg MAE90 | false-positive behavior | verdict |
|---|---:|---:|---:|---|---|
| P0 e2r_2_1_stock_web_calibrated_proxy | 3 | 48.38 | -6.01 | may over-credit brand rebound MFE without sell-through/margin bridge | needs C19 inventory-margin bridge repair |
| P1 canonical shadow bridge profile | 3 | 64.72 on kept positives | demotes 031430 | better alignment, source repair required |

## 20. Score-Return Alignment Matrix

| case_id | weighted before | label before | weighted after | label after | alignment |
|---|---:|---|---:|---|---|
| R5L86-C19-01 | 78 | Stage2-Actionable | 74 | Stage2-Actionable + local 4B/inventory-margin watch | partially aligned |
| R5L86-C19-02 | 78 | Stage2-Actionable | 74 | Stage2-Actionable + local 4B/inventory-margin watch | partially aligned |
| R5L86-C19-03 | 58 | Stage2-Watch/FalsePositive | 44 | Rejected-Stage2 / Brand-inventory RiskWatch | improved |

## 21. Coverage Matrix

| large_sector_id | canonical_archetype_id | fine_archetype_id | positive | counterexample | 4B | 4C | new cases | reused | usable triggers | current errors | sector rule | canonical rule | coverage gap after |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---|---|---|
| L5_CONSUMER_BRAND_DISTRIBUTION | C19_BRAND_RETAIL_INVENTORY_MARGIN | ATHLEISURE_FASHION_BEAUTY_BRAND_INVENTORY_NORMALIZATION_SELLTHROUGH_ARPU_MARGIN_BRIDGE_VS_RETAIL_THEME_FADE | 2 | 1 | 3-watch | 0-hard | 3 | 0 | 3 | 2 | no | yes | source repair needed |

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
  - source_proxy_only_blocks_runtime_promotion
  - high_MAE_guardrail
  - local_4B_watch_before_full_4B_when_MFE_outruns_bridge
residual_error_types_found:
  - brand_retail_inventory_rebound_false_positive
  - sellthrough_inventory_discount_margin_bridge_required
  - local_4B_late_after_brand_MFE
  - source_proxy_runtime_promotion_risk
  - high_MAE_positive_Green_blocker
new_axis_proposed: false
existing_axis_strengthened:
  - C19_brand_retail_sellthrough_inventory_discount_margin_bridge_required
  - source_proxy_only_blocks_runtime_promotion
  - local_4B_watch_before_full_4B_when_MFE_outruns_bridge
  - high_MAE_blocks_clean_Green
existing_axis_weakened: null
existing_axis_kept:
  - full_4b_requires_non_price_evidence
  - hard_4c_thesis_break_routes_to_4c
sector_specific_rule_candidate: null
canonical_archetype_rule_candidate: C19_brand_retail_sellthrough_inventory_discount_margin_bridge_required
no_new_signal_reason: null
loop_contribution_label: canonical_archetype_rule_candidate
do_not_propose_new_weight_delta: true
```

This loop adds 3 new independent cases, 1 counterexample, and 2 residual errors for R5/L5_CONSUMER_BRAND_DISTRIBUTION/C19_BRAND_RETAIL_INVENTORY_MARGIN.

## 23. Validation Scope / Non-Validation Scope

Validated in this MD:

```text
- Stock-Web profile path exists for selected symbols
- Stock-Web tradable shard path exists for selected symbols
- entry_date / entry_price are taken from tradable_raw close
- MFE / MAE / peak / post-peak drawdown are computed from observed OHLC windows
- corporate-action windows are checked at profile level
- scheduled_round / scheduled_loop / large_sector consistency
```

Not validated in this MD:

```text
- primary evidence URL
- exact publication time
- sell-through or inventory-turn evidence
- reorder cadence and ARPU/mix data
- ASP/discount control
- gross/OP margin conversion
- production scoring implementation
```

## 24. Shadow Weight Calibration

```csv
row_type,axis,scope,large_sector_id,canonical_archetype_id,baseline_value,tested_value,delta,reason,backtest_effect,trigger_ids,calibration_usable_count,new_independent_case_count,counterexample_count,confidence,proposal_type,notes
shadow_weight,C19_brand_retail_sellthrough_inventory_discount_margin_bridge_required,canonical_archetype_specific,L5_CONSUMER_BRAND_DISTRIBUTION,C19_BRAND_RETAIL_INVENTORY_MARGIN,0,1,+1,"Require sell-through, inventory turns, reorder cadence, ASP/discount control, ARPU/mix and gross-margin conversion before clean Stage2/Green","keeps 337930/093050 with local 4B or inventory-margin watch; demotes 031430","R5L86-C19-01-S2A-20240626|R5L86-C19-02-S2A-20240307|R5L86-C19-03-S2FP-20240307",3,3,1,low,canonical_shadow_only,"source repair required; not production"
```

## 25. Machine-Readable Rows

```jsonl
{"row_type": "price_source_validation", "source": "Songdaiki/stock-web", "source_url": "https://github.com/Songdaiki/stock-web", "manifest_path": "atlas/manifest.json", "schema_path": "atlas/schema.json", "universe_path": "atlas/universe/all_symbols.csv", "manifest_max_date": "2026-02-20", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "raw_shard_root": "atlas/ohlcv_raw_by_symbol_year", "validation_status": "usable_for_historical_calibration"}
{"row_type": "case", "case_id": "R5L86-C19-01", "symbol": "337930", "company_name": "브랜드엑스코퍼레이션", "round": "R5", "loop": 86, "large_sector_id": "L5_CONSUMER_BRAND_DISTRIBUTION", "canonical_archetype_id": "C19_BRAND_RETAIL_INVENTORY_MARGIN", "fine_archetype_id": "ATHLEISURE_FASHION_BEAUTY_BRAND_INVENTORY_NORMALIZATION_SELLTHROUGH_ARPU_MARGIN_BRIDGE_VS_RETAIL_THEME_FADE", "case_type": "athleisure_DTC_brand_inventory_margin_positive_with_local_4B_watch", "positive_or_counterexample": "positive", "best_trigger": "R5L86-C19-01-S2A-20240626", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "large_positive_MFE_but_local_4B_and_inventory_sellthrough_margin_bridge_required", "current_profile_verdict": "current_profile_partially_correct_local_4B_watch_needed", "price_source": "Songdaiki/stock-web", "notes": "C19 brand positives need channel sell-through, inventory normalization, reorder cadence, ARPU/mix and gross/OP margin bridge before clean Green."}
{"row_type": "trigger", "trigger_id": "R5L86-C19-01-S2A-20240626", "case_id": "R5L86-C19-01", "symbol": "337930", "company_name": "브랜드엑스코퍼레이션", "round": "R5", "loop": 86, "large_sector_id": "L5_CONSUMER_BRAND_DISTRIBUTION", "canonical_archetype_id": "C19_BRAND_RETAIL_INVENTORY_MARGIN", "fine_archetype_id": "ATHLEISURE_FASHION_BEAUTY_BRAND_INVENTORY_NORMALIZATION_SELLTHROUGH_ARPU_MARGIN_BRIDGE_VS_RETAIL_THEME_FADE", "loop_objective": "coverage_gap_fill|counterexample_mining|brand_retail_inventory_margin_guardrail|sellthrough_inventory_margin_bridge|canonical_archetype_compression", "trigger_type": "Stage2-Actionable", "trigger_date": "2024-06-26", "evidence_available_at_that_date": "athleisure / DTC brand / inventory normalization and margin recovery proxy; primary sell-through, reorder and margin evidence pending", "evidence_source": "source_proxy_only; evidence_url_pending", "stage2_evidence_fields": ["brand_strength_proxy", "inventory_rebound_proxy", "channel_sellthrough_proxy"], "stage3_evidence_fields": ["confirmed_sellthrough", "inventory_turns", "reorder_cadence", "ASP_or_discount_control", "ARPU_or_mix", "gross_margin_conversion"], "stage4b_evidence_fields": ["brand_MFE_without_inventory_margin_bridge", "post_peak_drawdown", "source_proxy_gap"], "stage4c_evidence_fields": ["hard_inventory_or_channel_demand_break_watch_only"], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/337/337930/2024.csv", "profile_path": "atlas/symbol_profiles/337/337930.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "entry_date": "2024-06-26", "entry_price": 6290, "MFE_30D_pct": 45.31, "MFE_90D_pct": 112.72, "MFE_180D_pct": 112.72, "MFE_1Y_pct": null, "MFE_2Y_pct": null, "MAE_30D_pct": -4.61, "MAE_90D_pct": -4.61, "MAE_180D_pct": -6.99, "MAE_1Y_pct": null, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2024-10-07", "peak_price": 13380, "drawdown_after_peak_pct": -57.25, "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": 0.88, "four_b_full_window_peak_proximity": 0.78, "four_b_timing_verdict": "local_4B_watch_after_DTC_brand_MFE_if_sellthrough_inventory_margin_bridge_stalls", "four_b_evidence_type": ["brand_MFE_without_inventory_margin_bridge", "post_peak_drawdown", "source_proxy_gap"], "four_c_protection_label": "hard_4C_requires_non_price_inventory_or_channel_demand_break", "trigger_outcome_label": "large_positive_MFE_but_local_4B_and_inventory_sellthrough_margin_bridge_required", "current_profile_verdict": "current_profile_partially_correct_local_4B_watch_needed", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_2024_2025_window_after_old_2021_CA_candidate", "same_entry_group_id": "R5L86-C19-01", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R5L86-C19-01", "trigger_id": "R5L86-C19-01-S2A-20240626", "symbol": "337930", "large_sector_id": "L5_CONSUMER_BRAND_DISTRIBUTION", "canonical_archetype_id": "C19_BRAND_RETAIL_INVENTORY_MARGIN", "raw_component_scores_before": {"brand_strength_score": 50, "inventory_normalization_score": 40, "channel_sellthrough_score": 40, "reorder_visibility_score": 35, "ASP_or_discount_control_score": 35, "ARPU_or_mix_score": 35, "gross_margin_bridge_score": 40, "revision_score": 40, "relative_strength_score": 70, "valuation_blowoff_risk_score": 75, "execution_risk_score": 55, "source_quality_score": 20, "4B_watch_score": 45}, "weighted_score_before": 78, "stage_label_before": "Stage2-Actionable", "raw_component_scores_after": {"brand_strength_score": 50, "inventory_normalization_score": 40, "channel_sellthrough_score": 40, "reorder_visibility_score": 35, "ASP_or_discount_control_score": 35, "ARPU_or_mix_score": 35, "gross_margin_bridge_score": 40, "revision_score": 40, "relative_strength_score": 70, "valuation_blowoff_risk_score": 90, "execution_risk_score": 65, "source_quality_score": 10, "4B_watch_score": 80}, "weighted_score_after": 74, "stage_label_after": "Stage2-Actionable + local 4B/inventory-margin watch", "changed_components": ["inventory_normalization_score", "channel_sellthrough_score", "reorder_visibility_score", "ASP_or_discount_control_score", "gross_margin_bridge_score", "source_quality_score", "4B_watch_score"], "component_delta_explanation": "C19 requires brand/retail MFE to convert into sell-through, inventory turns, reorder cadence, ASP/discount control, ARPU/mix and gross-margin conversion before clean Stage2/Green; brand rebound MFE alone is demoted or wrapped with local 4B/high-MAE watch.", "MFE_90D_pct": 112.72, "MAE_90D_pct": -4.61, "score_return_alignment_label": "large_positive_MFE_but_local_4B_and_inventory_sellthrough_margin_bridge_required", "current_profile_verdict": "current_profile_partially_correct_local_4B_watch_needed"}
{"row_type": "case", "case_id": "R5L86-C19-02", "symbol": "093050", "company_name": "LF", "round": "R5", "loop": 86, "large_sector_id": "L5_CONSUMER_BRAND_DISTRIBUTION", "canonical_archetype_id": "C19_BRAND_RETAIL_INVENTORY_MARGIN", "fine_archetype_id": "ATHLEISURE_FASHION_BEAUTY_BRAND_INVENTORY_NORMALIZATION_SELLTHROUGH_ARPU_MARGIN_BRIDGE_VS_RETAIL_THEME_FADE", "case_type": "fashion_brand_value_inventory_margin_positive_with_controlled_MAE_watch", "positive_or_counterexample": "positive", "best_trigger": "R5L86-C19-02-S2A-20240307", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "moderate_positive_MFE_but_inventory_margin_bridge_still_required", "current_profile_verdict": "current_profile_partially_correct_inventory_margin_bridge_needed", "price_source": "Songdaiki/stock-web", "notes": "C19 value-brand positives need inventory turn, channel mix, ASP/discount control and margin conversion before clean Green."}
{"row_type": "trigger", "trigger_id": "R5L86-C19-02-S2A-20240307", "case_id": "R5L86-C19-02", "symbol": "093050", "company_name": "LF", "round": "R5", "loop": 86, "large_sector_id": "L5_CONSUMER_BRAND_DISTRIBUTION", "canonical_archetype_id": "C19_BRAND_RETAIL_INVENTORY_MARGIN", "fine_archetype_id": "ATHLEISURE_FASHION_BEAUTY_BRAND_INVENTORY_NORMALIZATION_SELLTHROUGH_ARPU_MARGIN_BRIDGE_VS_RETAIL_THEME_FADE", "loop_objective": "coverage_gap_fill|counterexample_mining|brand_retail_inventory_margin_guardrail|sellthrough_inventory_margin_bridge|canonical_archetype_compression", "trigger_type": "Stage2-Actionable", "trigger_date": "2024-03-07", "evidence_available_at_that_date": "fashion brand / retail inventory normalization / margin recovery and value rerating proxy; primary inventory and channel margin evidence pending", "evidence_source": "source_proxy_only; evidence_url_pending", "stage2_evidence_fields": ["brand_strength_proxy", "inventory_rebound_proxy", "channel_sellthrough_proxy"], "stage3_evidence_fields": ["confirmed_sellthrough", "inventory_turns", "reorder_cadence", "ASP_or_discount_control", "ARPU_or_mix", "gross_margin_conversion"], "stage4b_evidence_fields": ["brand_MFE_without_inventory_margin_bridge", "post_peak_drawdown", "source_proxy_gap"], "stage4c_evidence_fields": ["hard_inventory_or_channel_demand_break_watch_only"], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/093/093050/2024.csv", "profile_path": "atlas/symbol_profiles/093/093050.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "entry_date": "2024-03-07", "entry_price": 13640, "MFE_30D_pct": 16.72, "MFE_90D_pct": 16.72, "MFE_180D_pct": 16.72, "MFE_1Y_pct": null, "MFE_2Y_pct": null, "MAE_30D_pct": -0.88, "MAE_90D_pct": -4.03, "MAE_180D_pct": -4.03, "MAE_1Y_pct": null, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2024-03-28", "peak_price": 15920, "drawdown_after_peak_pct": -17.78, "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": 0.7, "four_b_full_window_peak_proximity": 0.6, "four_b_timing_verdict": "brand_value_MFE_allowed_only_with_inventory_margin_bridge_watch", "four_b_evidence_type": ["brand_MFE_without_inventory_margin_bridge", "post_peak_drawdown", "source_proxy_gap"], "four_c_protection_label": "hard_4C_requires_non_price_inventory_or_channel_demand_break", "trigger_outcome_label": "moderate_positive_MFE_but_inventory_margin_bridge_still_required", "current_profile_verdict": "current_profile_partially_correct_inventory_margin_bridge_needed", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_2024_window_no_profile_CA_candidate", "same_entry_group_id": "R5L86-C19-02", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R5L86-C19-02", "trigger_id": "R5L86-C19-02-S2A-20240307", "symbol": "093050", "large_sector_id": "L5_CONSUMER_BRAND_DISTRIBUTION", "canonical_archetype_id": "C19_BRAND_RETAIL_INVENTORY_MARGIN", "raw_component_scores_before": {"brand_strength_score": 50, "inventory_normalization_score": 40, "channel_sellthrough_score": 40, "reorder_visibility_score": 35, "ASP_or_discount_control_score": 35, "ARPU_or_mix_score": 35, "gross_margin_bridge_score": 40, "revision_score": 40, "relative_strength_score": 55, "valuation_blowoff_risk_score": 45, "execution_risk_score": 55, "source_quality_score": 20, "4B_watch_score": 45}, "weighted_score_before": 78, "stage_label_before": "Stage2-Actionable", "raw_component_scores_after": {"brand_strength_score": 50, "inventory_normalization_score": 40, "channel_sellthrough_score": 40, "reorder_visibility_score": 35, "ASP_or_discount_control_score": 35, "ARPU_or_mix_score": 35, "gross_margin_bridge_score": 40, "revision_score": 40, "relative_strength_score": 55, "valuation_blowoff_risk_score": 45, "execution_risk_score": 55, "source_quality_score": 10, "4B_watch_score": 80}, "weighted_score_after": 74, "stage_label_after": "Stage2-Actionable + local 4B/inventory-margin watch", "changed_components": ["inventory_normalization_score", "channel_sellthrough_score", "reorder_visibility_score", "ASP_or_discount_control_score", "gross_margin_bridge_score", "source_quality_score", "4B_watch_score"], "component_delta_explanation": "C19 requires brand/retail MFE to convert into sell-through, inventory turns, reorder cadence, ASP/discount control, ARPU/mix and gross-margin conversion before clean Stage2/Green; brand rebound MFE alone is demoted or wrapped with local 4B/high-MAE watch.", "MFE_90D_pct": 16.72, "MAE_90D_pct": -4.03, "score_return_alignment_label": "moderate_positive_MFE_but_inventory_margin_bridge_still_required", "current_profile_verdict": "current_profile_partially_correct_inventory_margin_bridge_needed"}
{"row_type": "case", "case_id": "R5L86-C19-03", "symbol": "031430", "company_name": "신세계인터내셔날", "round": "R5", "loop": 86, "large_sector_id": "L5_CONSUMER_BRAND_DISTRIBUTION", "canonical_archetype_id": "C19_BRAND_RETAIL_INVENTORY_MARGIN", "fine_archetype_id": "ATHLEISURE_FASHION_BEAUTY_BRAND_INVENTORY_NORMALIZATION_SELLTHROUGH_ARPU_MARGIN_BRIDGE_VS_RETAIL_THEME_FADE", "case_type": "fashion_beauty_brand_inventory_rebound_false_positive", "positive_or_counterexample": "counterexample", "best_trigger": "R5L86-C19-03-S2FP-20240307", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "initial_MFE_then_high_MAE_brand_inventory_false_positive", "current_profile_verdict": "current_profile_false_positive_inventory_margin_bridge_gap", "price_source": "Songdaiki/stock-web", "notes": "Fashion/beauty retail rebound should be rejected unless sell-through, inventory turns, discount control, channel mix and margin bridge are explicit."}
{"row_type": "trigger", "trigger_id": "R5L86-C19-03-S2FP-20240307", "case_id": "R5L86-C19-03", "symbol": "031430", "company_name": "신세계인터내셔날", "round": "R5", "loop": 86, "large_sector_id": "L5_CONSUMER_BRAND_DISTRIBUTION", "canonical_archetype_id": "C19_BRAND_RETAIL_INVENTORY_MARGIN", "fine_archetype_id": "ATHLEISURE_FASHION_BEAUTY_BRAND_INVENTORY_NORMALIZATION_SELLTHROUGH_ARPU_MARGIN_BRIDGE_VS_RETAIL_THEME_FADE", "loop_objective": "coverage_gap_fill|counterexample_mining|brand_retail_inventory_margin_guardrail|sellthrough_inventory_margin_bridge|canonical_archetype_compression", "trigger_type": "Stage2-FalsePositive", "trigger_date": "2024-03-07", "evidence_available_at_that_date": "fashion/beauty brand inventory rebound and retail margin recovery proxy without confirmed sell-through, discount control and margin bridge", "evidence_source": "source_proxy_only; evidence_url_pending", "stage2_evidence_fields": ["brand_strength_proxy", "inventory_rebound_proxy", "channel_sellthrough_proxy"], "stage3_evidence_fields": ["confirmed_sellthrough", "inventory_turns", "reorder_cadence", "ASP_or_discount_control", "ARPU_or_mix", "gross_margin_conversion"], "stage4b_evidence_fields": ["brand_MFE_without_inventory_margin_bridge", "post_peak_drawdown", "source_proxy_gap"], "stage4c_evidence_fields": ["hard_inventory_or_channel_demand_break_watch_only"], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/031/031430/2024.csv", "profile_path": "atlas/symbol_profiles/031/031430.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "entry_date": "2024-03-07", "entry_price": 15870, "MFE_30D_pct": 15.69, "MFE_90D_pct": 15.69, "MFE_180D_pct": 15.69, "MFE_1Y_pct": null, "MFE_2Y_pct": null, "MAE_30D_pct": -1.76, "MAE_90D_pct": -9.39, "MAE_180D_pct": -21.93, "MAE_1Y_pct": null, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2024-04-01", "peak_price": 18360, "drawdown_after_peak_pct": -32.52, "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": 0.35, "four_b_full_window_peak_proximity": 0.3, "four_b_timing_verdict": "brand_inventory_rebound_rejected_without_sellthrough_discount_margin_bridge", "four_b_evidence_type": ["brand_MFE_without_inventory_margin_bridge", "post_peak_drawdown", "source_proxy_gap"], "four_c_protection_label": "hard_4C_requires_non_price_inventory_or_channel_demand_break", "trigger_outcome_label": "initial_MFE_then_high_MAE_brand_inventory_false_positive", "current_profile_verdict": "current_profile_false_positive_inventory_margin_bridge_gap", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_2024_window_after_old_2022_CA_candidate", "same_entry_group_id": "R5L86-C19-03", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R5L86-C19-03", "trigger_id": "R5L86-C19-03-S2FP-20240307", "symbol": "031430", "large_sector_id": "L5_CONSUMER_BRAND_DISTRIBUTION", "canonical_archetype_id": "C19_BRAND_RETAIL_INVENTORY_MARGIN", "raw_component_scores_before": {"brand_strength_score": 35, "inventory_normalization_score": 15, "channel_sellthrough_score": 10, "reorder_visibility_score": 5, "ASP_or_discount_control_score": 5, "ARPU_or_mix_score": 10, "gross_margin_bridge_score": 5, "revision_score": 15, "relative_strength_score": 35, "valuation_blowoff_risk_score": 55, "execution_risk_score": 75, "source_quality_score": 15, "4B_watch_score": 70}, "weighted_score_before": 58, "stage_label_before": "Stage2-Watch/FalsePositive", "raw_component_scores_after": {"brand_strength_score": 35, "inventory_normalization_score": 0, "channel_sellthrough_score": 0, "reorder_visibility_score": 0, "ASP_or_discount_control_score": 0, "ARPU_or_mix_score": 10, "gross_margin_bridge_score": 0, "revision_score": 15, "relative_strength_score": 35, "valuation_blowoff_risk_score": 55, "execution_risk_score": 85, "source_quality_score": 5, "4B_watch_score": 85}, "weighted_score_after": 44, "stage_label_after": "Rejected-Stage2 / Brand-inventory RiskWatch", "changed_components": ["inventory_normalization_score", "channel_sellthrough_score", "reorder_visibility_score", "ASP_or_discount_control_score", "gross_margin_bridge_score", "source_quality_score", "4B_watch_score"], "component_delta_explanation": "C19 requires brand/retail MFE to convert into sell-through, inventory turns, reorder cadence, ASP/discount control, ARPU/mix and gross-margin conversion before clean Stage2/Green; brand rebound MFE alone is demoted or wrapped with local 4B/high-MAE watch.", "MFE_90D_pct": 15.69, "MAE_90D_pct": -9.39, "score_return_alignment_label": "initial_MFE_then_high_MAE_brand_inventory_false_positive", "current_profile_verdict": "current_profile_false_positive_inventory_margin_bridge_gap"}
{"row_type": "shadow_weight", "axis": "C19_brand_retail_sellthrough_inventory_discount_margin_bridge_required", "scope": "canonical_archetype_specific", "large_sector_id": "L5_CONSUMER_BRAND_DISTRIBUTION", "canonical_archetype_id": "C19_BRAND_RETAIL_INVENTORY_MARGIN", "baseline_value": 0, "tested_value": 1, "delta": "+1", "reason": "Brand/retail inventory-margin rerating requires sell-through, inventory turns, reorder cadence, ASP/discount control, ARPU/mix and gross-margin conversion; brand rebound MFE without bridge fades into high MAE or needs local 4B watch.", "backtest_effect": "keeps 337930/093050 with local 4B or inventory-margin watch; demotes 031430 fashion/beauty rebound false positive", "trigger_ids": "R5L86-C19-01-S2A-20240626|R5L86-C19-02-S2A-20240307|R5L86-C19-03-S2FP-20240307", "calibration_usable_count": 3, "new_independent_case_count": 3, "counterexample_count": 1, "confidence": "low", "proposal_type": "canonical_shadow_only", "notes": "source_proxy_only/evidence_url_pending; not production"}
{"row_type": "residual_contribution", "round": "R5", "loop": 86, "large_sector_id": "L5_CONSUMER_BRAND_DISTRIBUTION", "canonical_archetype_id": "C19_BRAND_RETAIL_INVENTORY_MARGIN", "new_independent_case_count": 3, "reused_case_count": 0, "new_symbol_count": 3, "new_trigger_family_count": 3, "tested_existing_calibrated_axes": ["stage2_actionable_evidence_bonus", "price_only_blowoff_blocks_positive_stage", "full_4b_requires_non_price_evidence", "hard_4c_thesis_break_routes_to_4c", "source_proxy_only_blocks_runtime_promotion", "high_MAE_guardrail", "local_4B_watch_before_full_4B_when_MFE_outruns_bridge"], "residual_error_types_found": ["brand_retail_inventory_rebound_false_positive", "sellthrough_inventory_discount_margin_bridge_required", "local_4B_late_after_brand_MFE", "source_proxy_runtime_promotion_risk", "high_MAE_positive_Green_blocker"], "loop_contribution_label": "canonical_archetype_rule_candidate", "do_not_propose_new_weight_delta": true}
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
- Do not treat source_proxy_only or evidence_url_pending rows as runtime promotion-ready.
- Keep production scoring unchanged unless a later batch validates primary evidence and aggregate thresholds.
- For C19, test a canonical-archetype guard requiring sell-through, inventory turns, reorder cadence, ASP/discount control, ARPU/mix and gross-margin conversion before clean Stage2/Green.

## 27. Next Round State

```text
completed_round = R5
completed_loop = 86
next_round = R6
next_loop = 86
round_schedule_status = valid
round_sector_consistency = pass
```

## 28. Source Notes

```text
MAIN_EXECUTION_PROMPT = docs/core/e2r_v12_prompt_round_scheduler_corrected.txt
NO_REPEAT_INDEX = docs/core/V12_Research_No_Repeat_Index.md
price_source = Songdaiki/stock-web
```
