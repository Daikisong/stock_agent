# E2R Stock-Web Historical Calibration / Sector-Archetype Residual Research Round
## 0. Research Metadata
- selected_round: R4
- selected_loop: 100
- selected_priority_bucket: Priority 0
- selection_basis: docs/core/V12_Research_No_Repeat_Index.md
- round_schedule_status: coverage_index_selected
- round_sector_consistency: pass
- large_sector_id: L4_MATERIALS_SPREAD_RESOURCE
- canonical_archetype_id: C15_MATERIAL_SPREAD_SUPERCYCLE
- fine_archetype_id: COPPER_ZINC_STEEL_SPREAD_MARGIN_BRIDGE_VS_COMMODITY_HEADLINE_BLOWOFF
- loop_objective: coverage_gap_fill | counterexample_mining | stage2_actionable_bonus_stress_test | 4B_non_price_requirement_stress_test | canonical_archetype_compression
- output_file: e2r_stock_web_v12_residual_round_R4_loop_100_L4_MATERIALS_SPREAD_RESOURCE_C15_MATERIAL_SPREAD_SUPERCYCLE_research.md

## 1. Current Calibrated Profile Assumption
before_profile_id = e2r_2_1_stock_web_calibrated_proxy

after_profile_id = proposed_C15_material_spread_company_margin_bridge_shadow_profile

rollback_reference_profile_id = e2r_2_0_baseline_reference

C15 is not a generic commodity-supercycle bucket. A useful C15 row requires a bridge from commodity spread to the company: ASP, volume, inventory cost lag, OPM/revision, cash conversion, or supply constraint that the specific company can monetize. The row should punish two common mistakes: (1) metal-price beta without company margin proof, and (2) post-event governance/control-premium MFE being misattributed to materials spread.

## 2. Round / Large Sector / Canonical Archetype Scope
| field | value |
|---|---|
| selected_round | R4 |
| large_sector_id | L4_MATERIALS_SPREAD_RESOURCE |
| canonical_archetype_id | C15_MATERIAL_SPREAD_SUPERCYCLE |
| fine_archetype_id | COPPER_ZINC_STEEL_SPREAD_MARGIN_BRIDGE_VS_COMMODITY_HEADLINE_BLOWOFF |
| round_sector_consistency | pass |

## 3. Previous Coverage / Duplicate Avoidance Check
No-Repeat Index shows C15 at 6 rows, 6 symbols, positive/counter = 0/2 and 4B/4C = 1/0. Covered symbols include 001390, 001550, 005490, 009520, 025860, and 103140. This loop avoids those exact symbols and adds four new symbols: 006260, 010130, 001430, and 004020. Hard duplicate key is canonical_archetype_id + symbol + trigger_type + entry_date; none of the selected rows reuse that key.

## 4. Stock-Web OHLC Input / Price Source Validation
| field | value |
|---|---|
| price_source | Songdaiki/stock-web |
| manifest_path | atlas/manifest.json |
| stock_web_manifest_max_date | 2026-02-20 |
| price_basis | tradable_raw |
| price_adjustment_status | raw_unadjusted_marcap |
| shard_root | atlas/ohlcv_tradable_by_symbol_year |
| manifest_generated_at | 2026-05-21T16:28:39.421691+00:00 |

## 5. Historical Eligibility Gate
| case | entry_date | forward_180D_available | corporate_action_window_status | calibration_usable |
|---|---:|---:|---|---:|
| C15_006260_20240411_COPPER_CABLE_SPREAD_BACKLOG_BRIDGE | 2024-04-11 | true | clean_180D_window | true |
| C15_010130_20240415_ZINC_PRECIOUS_METAL_SPREAD_WITH_GOVERNANCE_CONTAMINATION | 2024-04-15 | true | clean_180D_window_but_thesis_contaminated_after_2024_09_13 | true |
| C15_001430_20240514_SPECIAL_STEEL_SPREAD_HEADLINE_FALSE_POSITIVE | 2024-05-14 | true | clean_180D_window | true |
| C15_004020_20240207_STEEL_SPREAD_SUPERCYCLE_FALSE_POSITIVE | 2024-02-07 | true | clean_180D_window | true |

## 6. Canonical Archetype Compression Map
```text
C15_MATERIAL_SPREAD_SUPERCYCLE
  -> COMPANY_MARGIN_BRIDGE_PRESENT
     -> 006260 LS: copper/cable spread and backlog/cable monetization produced high MFE, but post-peak MAE requires local 4B watch
  -> LOCAL_SPREAD_POSITIVE_WITH_ARCHETYPE_SWITCH_RISK
     -> 010130 Korea Zinc: 30/90D nonferrous spread path is modest positive, but 180D MFE is governance/control-premium contamination and should switch to C32
  -> SPREAD_HEADLINE_WITHOUT_VOLUME_OPM_BRIDGE
     -> 001430 SeAH Besteel Holdings: small MFE, deep MAE, special-steel label did not become durable margin
  -> STEEL_SUPERCYCLE_LABEL_FALSE_POSITIVE
     -> 004020 Hyundai Steel: cyclical steel spread label failed across 30/90/180D
```

## 7. Case Selection Summary
| case_id | symbol | company | role | new independent | reason |
|---|---:|---|---|---:|---|
| C15_006260_20240411_COPPER_CABLE_SPREAD_BACKLOG_BRIDGE | 006260 | LS | positive_with_4B_watch | true | positive MFE from copper/cable spread, but large post-peak drawdown requires local 4B |
| C15_010130_20240415_ZINC_PRECIOUS_METAL_SPREAD_WITH_GOVERNANCE_CONTAMINATION | 010130 | 고려아연 | mixed_positive_archetype_switch | true | 90D spread path modest; 180D MFE belongs to governance/control premium |
| C15_001430_20240514_SPECIAL_STEEL_SPREAD_HEADLINE_FALSE_POSITIVE | 001430 | 세아베스틸지주 | counterexample | true | special-steel spread headline failed margin/volume bridge |
| C15_004020_20240207_STEEL_SPREAD_SUPERCYCLE_FALSE_POSITIVE | 004020 | 현대제철 | counterexample | true | steel spread/supercycle label failed return path |

## 8. Positive vs Counterexample Balance
| count_type | count |
|---|---:|
| positive_case_count | 1 |
| mixed_positive_count | 1 |
| counterexample_count | 2 |
| local_4B_watch_count | 1 |
| archetype_switch_required_count | 1 |
| calibration_usable_case_count | 4 |
| calibration_usable_trigger_count | 4 |

## 9. Evidence Source Map
| case | evidence_available_at_that_date | evidence_source |
|---|---|---|
| 006260 2024-04-11 | copper/cable spread and cable backlog/capacity narrative were market-visible; company-level bridge needed confirmation | public commodity/cable spread proxy; price path from stock-web |
| 010130 2024-04-15 | zinc/precious-metal spread path was market-visible; later governance/control-premium event is a separate archetype | public nonferrous spread proxy; price path from stock-web |
| 001430 2024-05-14 | special-steel spread narrative was market-visible but volume and OPM bridge were weak | public special-steel spread proxy; price path from stock-web |
| 004020 2024-02-07 | steel-cycle and value/cyclical rebound narrative were market-visible but steel margin bridge was weak | public steel spread proxy; price path from stock-web |

## 10. Price Data Source Map
| symbol | profile_path | price_shard_path |
|---:|---|---|
| 006260 | atlas/symbol_profiles/006/006260.json | atlas/ohlcv_tradable_by_symbol_year/006/006260/2024.csv |
| 010130 | atlas/symbol_profiles/010/010130.json | atlas/ohlcv_tradable_by_symbol_year/010/010130/2024.csv |
| 001430 | atlas/symbol_profiles/001/001430.json | atlas/ohlcv_tradable_by_symbol_year/001/001430/2024.csv |
| 004020 | atlas/symbol_profiles/004/004020.json | atlas/ohlcv_tradable_by_symbol_year/004/004020/2024.csv |

## 11. Case-by-Case Trigger Grid
| case_id | symbol | company | trigger_type | entry_date | entry_price | MFE30 | MAE30 | MFE90 | MAE90 | MFE180 | MAE180 | verdict |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| C15_006260_20240411_COPPER_CABLE_SPREAD_BACKLOG_BRIDGE | 006260 | LS | Stage2-Actionable | 2024-04-11 | 114900 | 69.54 | -8.01 | 69.54 | -18.19 | 69.54 | -26.46 | positive_but_high_MAE_after_copper_blowoff |
| C15_010130_20240415_ZINC_PRECIOUS_METAL_SPREAD_WITH_GOVERNANCE_CONTAMINATION | 010130 | 고려아연 | Stage2-Actionable | 2024-04-15 | 485000 | 12.58 | -7.11 | 13.2 | -7.11 | 218.14 | -7.11 | mixed_positive_requires_archetype_switch_after_governance_event |
| C15_001430_20240514_SPECIAL_STEEL_SPREAD_HEADLINE_FALSE_POSITIVE | 001430 | 세아베스틸지주 | Stage2 | 2024-05-14 | 23850 | 7.76 | -13.21 | 7.76 | -26.0 | 7.76 | -26.0 | counterexample_channel_inventory_and_volume_missing |
| C15_004020_20240207_STEEL_SPREAD_SUPERCYCLE_FALSE_POSITIVE | 004020 | 현대제철 | Stage2 | 2024-02-07 | 37000 | 1.35 | -13.11 | 1.35 | -23.92 | 1.35 | -45.68 | hard_counterexample_spread_label_without_company_margin |

## 12. Trigger-Level OHLC Backtest Method
MFE_N_pct = max(high over horizon) / entry_price - 1. MAE_N_pct = min(low over horizon) / entry_price - 1. Horizons are calculated from tradable_raw stock-web daily rows available in the selected symbol-year shards. All representative rows include entry date, entry price, 30D/90D/180D MFE, 30D/90D/180D MAE, peak date, peak price, trough date, trough price, and corporate-action window status.

Important C15 caveat: 010130's 180D path includes a governance/control-premium regime shift beginning after the 90D window. This row is intentionally kept because it teaches the scorer not to let C15 claim a C32-style return path. For pure C15 weight calibration, 010130 should be credited mainly for its 30/90D local spread path, while its 180D MFE should be routed to archetype-switch logic.

## 13. Current Calibrated Profile Stress Test
1. Current profile is still vulnerable when C15 receives Stage2-Actionable credit from commodity vocabulary alone. 001430 and 004020 show the failure mode: small MFE, large MAE, no durable margin bridge.
2. LS shows that a company-level bridge can work, but not as unconditional Green. The return path had +69.54% MFE but later carried -26.46% MAE from entry, so post-peak local 4B is needed.
3. Korea Zinc shows an archetype-contamination failure. A materials spread row can later become a governance/control-premium row. If the scorer credits all 180D MFE to C15, it overfits the wrong cause.
4. Therefore, this loop strengthens price_only_blowoff_blocks_positive_stage and full_4b_requires_non_price_evidence.
5. The new C15-specific rule is not a broad weight increase. It is a bridge requirement: commodity spread -> company ASP/volume/OPM/revision/FCF.

## 14. Stage2 / Yellow / Green Comparison
| case | Stage2 timing | Yellow/Green implication | residual error |
|---|---|---|---|
| 006260 | Stage2-Actionable can be valid only with cable/backlog/margin bridge | Yellow allowed after confirmation; Green should wait for margin durability and avoid price-only blowoff | local 4B needed after high-MAE reversal |
| 010130 | Stage2-Actionable can be valid on 30/90D spread only | Green should not claim 180D governance MFE under C15 | archetype switch to C32 required after governance/control-premium event |
| 001430 | Stage2 should remain watch only | Yellow/Green blocked | special-steel label without volume/OPM bridge is false positive |
| 004020 | Stage2 should remain watch only | Yellow/Green blocked | steel spread label without company margin is hard false positive |

## 15. Proposed Shadow Rule Candidate
```yaml
C15_MATERIAL_SPREAD_SUPERCYCLE_shadow_rule:
  rule_id: C15_COMPANY_MARGIN_BRIDGE_REQUIRED
  applies_to:
    large_sector_id: L4_MATERIALS_SPREAD_RESOURCE
    canonical_archetype_id: C15_MATERIAL_SPREAD_SUPERCYCLE
  positive_requirements:
    - commodity_spread_or_ASP_tailwind_visible
    - company_specific_volume_or_backlog_or_delivery_bridge_visible
    - OPM_or_revision_or_FCF_bridge_visible_or_near_visible
    - no_non_C15_archetype_contamination_in_forward_window
  block_or_cap_conditions:
    - price_only_commodity_beta
    - supercycle_label_without_company_margin_bridge
    - high_MAE_after_initial_MFE_without_revision_support
    - governance_control_premium_or_tender_event_takes_over_return_path
  stage_effect:
    Stage2: allowed only as watch if commodity-only
    Stage2-Actionable: requires at least one non-price company bridge
    Stage3-Yellow: requires ASP/volume/OPM or FCF confirmation
    Stage3-Green: not loosened by this loop
    local_4B: required after high MFE if subsequent MAE exceeds -18% without new margin confirmation
```

## 16. Aggregate Metrics
```json
{
  "calibration_usable_case_count": 4,
  "calibration_usable_trigger_count": 4,
  "canonical_archetype_id": "C15_MATERIAL_SPREAD_SUPERCYCLE",
  "counterexample_count": 2,
  "current_profile_error_count": 4,
  "fine_archetype_id": "COPPER_ZINC_STEEL_SPREAD_MARGIN_BRIDGE_VS_COMMODITY_HEADLINE_BLOWOFF",
  "large_sector_id": "L4_MATERIALS_SPREAD_RESOURCE",
  "mean_MAE_180D_pct": -26.31,
  "mean_MAE_30D_pct": -10.36,
  "mean_MAE_90D_pct": -18.8,
  "mean_MFE_180D_pct": 74.2,
  "mean_MFE_30D_pct": 22.81,
  "mean_MFE_90D_pct": 22.96,
  "mixed_positive_count": 1,
  "new_independent_case_count": 4,
  "note": "010130 180D MFE is intentionally flagged as post-90D governance/control-premium contamination and should not be credited to C15 pure spread rule.",
  "positive_case_count": 1,
  "reused_case_count": 0,
  "row_type": "aggregate_metric",
  "same_archetype_new_symbol_count": 4,
  "same_archetype_new_trigger_family_count": 4,
  "schema_family": "v12_sector_archetype_residual",
  "selected_loop": 100,
  "selected_round": "R4"
}
```

## 17. Machine-Readable JSONL Rows
```jsonl
{"MAE_180D_pct": -26.46, "MAE_30D_pct": -8.01, "MAE_90D_pct": -18.19, "MFE_180D_pct": 69.54, "MFE_30D_pct": 69.54, "MFE_90D_pct": 69.54, "calibration_usable": true, "canonical_archetype_id": "C15_MATERIAL_SPREAD_SUPERCYCLE", "case_id": "C15_006260_20240411_COPPER_CABLE_SPREAD_BACKLOG_BRIDGE", "company": "LS", "corporate_action_window_status": "clean_180D_window", "current_profile_error": "would_overpromote_if_copper_price_beta_is_treated_as_margin_bridge_without_backlog_delivery_and_OPM_confirmation", "entry_date": "2024-04-11", "entry_price": 114900.0, "fine_archetype_id": "COPPER_ZINC_STEEL_SPREAD_MARGIN_BRIDGE_VS_COMMODITY_HEADLINE_BLOWOFF", "large_sector_id": "L4_MATERIALS_SPREAD_RESOURCE", "peak_180D_date": "2024-05-21", "peak_180D_price": 194800.0, "peak_30D_date": "2024-05-21", "peak_30D_price": 194800.0, "peak_90D_date": "2024-05-21", "peak_90D_price": 194800.0, "row_type": "trigger", "schema_family": "v12_sector_archetype_residual", "source_url": "stock-web:atlas/ohlcv_tradable_by_symbol_year/006/006260/2024.csv", "symbol": "006260", "trigger_id": "C15_006260_20240411_S2A", "trigger_type": "Stage2-Actionable", "trough_180D_date": "2024-11-18", "trough_180D_price": 84500.0, "trough_30D_date": "2024-04-11", "trough_30D_price": 105700.0, "trough_90D_date": "2024-08-05", "trough_90D_price": 94000.0, "verdict": "positive_but_high_MAE_after_copper_blowoff"}
{"MAE_180D_pct": -7.11, "MAE_30D_pct": -7.11, "MAE_90D_pct": -7.11, "MFE_180D_pct": 218.14, "MFE_30D_pct": 12.58, "MFE_90D_pct": 13.2, "calibration_usable": true, "canonical_archetype_id": "C15_MATERIAL_SPREAD_SUPERCYCLE", "case_id": "C15_010130_20240415_ZINC_PRECIOUS_METAL_SPREAD_WITH_GOVERNANCE_CONTAMINATION", "company": "고려아연", "corporate_action_window_status": "clean_180D_window_but_thesis_contaminated_after_2024_09_13", "current_profile_error": "C15_should_not_take_credit_for_post_2024_09_control_premium_tender_like_price_path; switch_or_cap_to_C32_needed", "entry_date": "2024-04-15", "entry_price": 485000.0, "fine_archetype_id": "COPPER_ZINC_STEEL_SPREAD_MARGIN_BRIDGE_VS_COMMODITY_HEADLINE_BLOWOFF", "large_sector_id": "L4_MATERIALS_SPREAD_RESOURCE", "peak_180D_date": "2024-10-29", "peak_180D_price": 1543000.0, "peak_30D_date": "2024-05-21", "peak_30D_price": 546000.0, "peak_90D_date": "2024-07-15", "peak_90D_price": 549000.0, "row_type": "trigger", "schema_family": "v12_sector_archetype_residual", "source_url": "stock-web:atlas/ohlcv_tradable_by_symbol_year/010/010130/2024.csv", "symbol": "010130", "trigger_id": "C15_010130_20240415_S2A_TO_ARCHETYPE_SWITCH", "trigger_type": "Stage2-Actionable", "trough_180D_date": "2024-04-25", "trough_180D_price": 450500.0, "trough_30D_date": "2024-04-25", "trough_30D_price": 450500.0, "trough_90D_date": "2024-04-25", "trough_90D_price": 450500.0, "verdict": "mixed_positive_requires_archetype_switch_after_governance_event"}
{"MAE_180D_pct": -26.0, "MAE_30D_pct": -13.21, "MAE_90D_pct": -26.0, "MFE_180D_pct": 7.76, "MFE_30D_pct": 7.76, "MFE_90D_pct": 7.76, "calibration_usable": true, "canonical_archetype_id": "C15_MATERIAL_SPREAD_SUPERCYCLE", "case_id": "C15_001430_20240514_SPECIAL_STEEL_SPREAD_HEADLINE_FALSE_POSITIVE", "company": "세아베스틸지주", "corporate_action_window_status": "clean_180D_window", "current_profile_error": "materials_spread_headline_without_volume_ASP_OPM_bridge_should_not_receive_stage2_actionable_bonus", "entry_date": "2024-05-14", "entry_price": 23850.0, "fine_archetype_id": "COPPER_ZINC_STEEL_SPREAD_MARGIN_BRIDGE_VS_COMMODITY_HEADLINE_BLOWOFF", "large_sector_id": "L4_MATERIALS_SPREAD_RESOURCE", "peak_180D_date": "2024-05-16", "peak_180D_price": 25700.0, "peak_30D_date": "2024-05-16", "peak_30D_price": 25700.0, "peak_90D_date": "2024-05-16", "peak_90D_price": 25700.0, "row_type": "trigger", "schema_family": "v12_sector_archetype_residual", "source_url": "stock-web:atlas/ohlcv_tradable_by_symbol_year/001/001430/2024.csv", "symbol": "001430", "trigger_id": "C15_001430_20240514_S2_FALSE_POSITIVE", "trigger_type": "Stage2", "trough_180D_date": "2024-08-08", "trough_180D_price": 17650.0, "trough_30D_date": "2024-06-14", "trough_30D_price": 20700.0, "trough_90D_date": "2024-08-08", "trough_90D_price": 17650.0, "verdict": "counterexample_channel_inventory_and_volume_missing"}
{"MAE_180D_pct": -45.68, "MAE_30D_pct": -13.11, "MAE_90D_pct": -23.92, "MFE_180D_pct": 1.35, "MFE_30D_pct": 1.35, "MFE_90D_pct": 1.35, "calibration_usable": true, "canonical_archetype_id": "C15_MATERIAL_SPREAD_SUPERCYCLE", "case_id": "C15_004020_20240207_STEEL_SPREAD_SUPERCYCLE_FALSE_POSITIVE", "company": "현대제철", "corporate_action_window_status": "clean_180D_window", "current_profile_error": "steel_spread_supercycle_label_can_score_as_mispricing_but_actual_path_is_negative_when_company_margin_and_demand_bridge_are_absent", "entry_date": "2024-02-07", "entry_price": 37000.0, "fine_archetype_id": "COPPER_ZINC_STEEL_SPREAD_MARGIN_BRIDGE_VS_COMMODITY_HEADLINE_BLOWOFF", "large_sector_id": "L4_MATERIALS_SPREAD_RESOURCE", "peak_180D_date": "2024-02-13", "peak_180D_price": 37500.0, "peak_30D_date": "2024-02-13", "peak_30D_price": 37500.0, "peak_90D_date": "2024-02-13", "peak_90D_price": 37500.0, "row_type": "trigger", "schema_family": "v12_sector_archetype_residual", "source_url": "stock-web:atlas/ohlcv_tradable_by_symbol_year/004/004020/2024.csv", "symbol": "004020", "trigger_id": "C15_004020_20240207_S2_FALSE_POSITIVE", "trigger_type": "Stage2", "trough_180D_date": "2024-11-15", "trough_180D_price": 20100.0, "trough_30D_date": "2024-03-19", "trough_30D_price": 32150.0, "trough_90D_date": "2024-06-12", "trough_90D_price": 28150.0, "verdict": "hard_counterexample_spread_label_without_company_margin"}
{"canonical_archetype_id": "C15_MATERIAL_SPREAD_SUPERCYCLE", "case_id": "C15_006260_20240411_COPPER_CABLE_SPREAD_BACKLOG_BRIDGE", "company": "LS", "fine_archetype_id": "COPPER_ZINC_STEEL_SPREAD_MARGIN_BRIDGE_VS_COMMODITY_HEADLINE_BLOWOFF", "large_sector_id": "L4_MATERIALS_SPREAD_RESOURCE", "role": "positive", "row_type": "case", "schema_family": "v12_sector_archetype_residual", "symbol": "006260", "trigger_id": "C15_006260_20240411_S2A"}
{"canonical_archetype_id": "C15_MATERIAL_SPREAD_SUPERCYCLE", "case_id": "C15_010130_20240415_ZINC_PRECIOUS_METAL_SPREAD_WITH_GOVERNANCE_CONTAMINATION", "company": "고려아연", "fine_archetype_id": "COPPER_ZINC_STEEL_SPREAD_MARGIN_BRIDGE_VS_COMMODITY_HEADLINE_BLOWOFF", "large_sector_id": "L4_MATERIALS_SPREAD_RESOURCE", "role": "positive", "row_type": "case", "schema_family": "v12_sector_archetype_residual", "symbol": "010130", "trigger_id": "C15_010130_20240415_S2A_TO_ARCHETYPE_SWITCH"}
{"canonical_archetype_id": "C15_MATERIAL_SPREAD_SUPERCYCLE", "case_id": "C15_001430_20240514_SPECIAL_STEEL_SPREAD_HEADLINE_FALSE_POSITIVE", "company": "세아베스틸지주", "fine_archetype_id": "COPPER_ZINC_STEEL_SPREAD_MARGIN_BRIDGE_VS_COMMODITY_HEADLINE_BLOWOFF", "large_sector_id": "L4_MATERIALS_SPREAD_RESOURCE", "role": "counterexample", "row_type": "case", "schema_family": "v12_sector_archetype_residual", "symbol": "001430", "trigger_id": "C15_001430_20240514_S2_FALSE_POSITIVE"}
{"canonical_archetype_id": "C15_MATERIAL_SPREAD_SUPERCYCLE", "case_id": "C15_004020_20240207_STEEL_SPREAD_SUPERCYCLE_FALSE_POSITIVE", "company": "현대제철", "fine_archetype_id": "COPPER_ZINC_STEEL_SPREAD_MARGIN_BRIDGE_VS_COMMODITY_HEADLINE_BLOWOFF", "large_sector_id": "L4_MATERIALS_SPREAD_RESOURCE", "role": "counterexample", "row_type": "case", "schema_family": "v12_sector_archetype_residual", "symbol": "004020", "trigger_id": "C15_004020_20240207_S2_FALSE_POSITIVE"}
{"after_shadow_rule": "require_ASP_volume_OPM_bridge_for_C15_stage2_actionable", "after_stage": "Stage2-Actionable + local_4B_watch", "before_profile_id": "e2r_2_1_stock_web_calibrated_proxy", "before_stage": "Stage3-Yellow-risk", "case_id": "C15_006260_20240411_COPPER_CABLE_SPREAD_BACKLOG_BRIDGE", "reason": "large positive MFE but very large post-peak MAE; Green should wait for margin conversion", "row_type": "score_simulation"}
{"after_shadow_rule": "cap_C15_credit_after_archetype_switch_to_C32", "after_stage": "Stage2-Actionable until governance switch; C32 after switch", "before_profile_id": "e2r_2_1_stock_web_calibrated_proxy", "before_stage": "Stage2-Actionable", "case_id": "C15_010130_20240415_ZINC_PRECIOUS_METAL_SPREAD_WITH_GOVERNANCE_CONTAMINATION", "reason": "90D commodity spread path is modest; 180D MFE belongs to governance/control premium, not C15", "row_type": "score_simulation"}
{"after_shadow_rule": "block_stage2_actionable_without_volume_ASP_OPM_bridge", "after_stage": "Stage1/Stage2-watch only", "before_profile_id": "e2r_2_1_stock_web_calibrated_proxy", "before_stage": "Stage2-watch", "case_id": "C15_001430_20240514_SPECIAL_STEEL_SPREAD_HEADLINE_FALSE_POSITIVE", "reason": "MFE small, MAE deep; spread headline did not convert to company margin", "row_type": "score_simulation"}
{"after_shadow_rule": "hard_block_steel_spread_label_without_margin_bridge", "after_stage": "Stage1/Stage2-watch only", "before_profile_id": "e2r_2_1_stock_web_calibrated_proxy", "before_stage": "Stage2-watch", "case_id": "C15_004020_20240207_STEEL_SPREAD_SUPERCYCLE_FALSE_POSITIVE", "reason": "return path is negative across 30/90/180D despite cyclical headline", "row_type": "score_simulation"}
{"calibration_usable_case_count": 4, "calibration_usable_trigger_count": 4, "canonical_archetype_id": "C15_MATERIAL_SPREAD_SUPERCYCLE", "counterexample_count": 2, "current_profile_error_count": 4, "fine_archetype_id": "COPPER_ZINC_STEEL_SPREAD_MARGIN_BRIDGE_VS_COMMODITY_HEADLINE_BLOWOFF", "large_sector_id": "L4_MATERIALS_SPREAD_RESOURCE", "mean_MAE_180D_pct": -26.31, "mean_MAE_30D_pct": -10.36, "mean_MAE_90D_pct": -18.8, "mean_MFE_180D_pct": 74.2, "mean_MFE_30D_pct": 22.81, "mean_MFE_90D_pct": 22.96, "mixed_positive_count": 1, "new_independent_case_count": 4, "note": "010130 180D MFE is intentionally flagged as post-90D governance/control-premium contamination and should not be credited to C15 pure spread rule.", "positive_case_count": 1, "reused_case_count": 0, "row_type": "aggregate_metric", "same_archetype_new_symbol_count": 4, "same_archetype_new_trigger_family_count": 4, "schema_family": "v12_sector_archetype_residual", "selected_loop": 100, "selected_round": "R4"}
{"after_shadow_weight": 18, "axis": "EPS_FCF_Explosion", "before_weight": 20, "direction": "down_if_spread_only", "rationale": "commodity spread alone is not earnings explosion unless ASP-volume-OPM bridge is explicit", "row_type": "shadow_weight"}
{"after_shadow_weight": 18, "axis": "Earnings_Visibility_and_Quality", "before_weight": 12, "direction": "up", "rationale": "C15 needs realized/visible margin conversion more than headline price beta", "row_type": "shadow_weight"}
{"after_shadow_weight": 19, "axis": "Bottleneck_and_Pricing_Power", "before_weight": 20, "direction": "flat_down", "rationale": "supply bottleneck matters, but must be company-level not just macro commodity", "row_type": "shadow_weight"}
{"after_shadow_weight": 9, "axis": "Market_Mispricing", "before_weight": 10, "direction": "down", "rationale": "materials names rerate early and can blow off before margin evidence", "row_type": "shadow_weight"}
{"after_shadow_weight": 24, "axis": "Information_Confidence", "before_weight": 20, "direction": "up", "rationale": "external commodity and corporate margin evidence must agree; governance contamination must be classified", "row_type": "shadow_weight"}
{"contribution_label": "canonical_archetype_rule_candidate", "description": "Do not upgrade C15 to Stage2-Actionable/Yellow on metal spread or supercycle vocabulary alone; require ASP, volume, OPM/revision, backlog/delivery, or cash-flow bridge.", "residual_id": "C15_MARGIN_BRIDGE_REQUIRED", "row_type": "residual_contribution"}
{"contribution_label": "residual_error_found", "description": "When a materials company rerates after a governance/control-premium/tender dispute, cap C15 credit and switch/route the post-event return path to C32.", "residual_id": "C15_TO_C32_ARCHETYPE_SWITCH", "row_type": "residual_contribution"}
{"contribution_label": "guardrail_strengthened", "description": "Large MFE followed by >18% MAE should trigger local 4B watch even if 180D absolute MFE stays positive.", "residual_id": "C15_LOCAL_4B_AFTER_BLOWOFF", "row_type": "residual_contribution"}
```

## 18. Residual Contribution Summary
| residual_id | contribution_label | description |
|---|---|---|
| C15_MARGIN_BRIDGE_REQUIRED | canonical_archetype_rule_candidate | Do not upgrade C15 on supercycle vocabulary alone; require ASP/volume/OPM/revision/FCF bridge. |
| C15_TO_C32_ARCHETYPE_SWITCH | residual_error_found | If governance/control-premium event takes over, cap C15 credit and route to C32. |
| C15_LOCAL_4B_AFTER_BLOWOFF | guardrail_strengthened | Large MFE followed by deep MAE should enter local 4B watch even if headline thesis remains alive. |

## 19. Deferred Coding Agent Handoff Prompt
```text
You are a coding agent in a later stock_agent batch-implementation session. Do not execute this during research ingestion. Read this MD as a v12 sector-archetype residual artifact. Add/adjust C15-specific shadow logic only after aggregating multiple C15 MDs. Candidate rule: C15_COMPANY_MARGIN_BRIDGE_REQUIRED. Require commodity spread -> company ASP/volume/OPM/revision/FCF bridge before Stage2-Actionable or Yellow. Add archetype contamination guard: if governance/control-premium/tender event explains the forward MFE, cap C15 credit and route the later path to C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP. Preserve global Green thresholds and do not loosen Stage3-Green.
```

## 20. Completion State
completed_round: R4
completed_loop: 100
selection_basis: docs/core/V12_Research_No_Repeat_Index.md
selected_priority_bucket: Priority 0
round_schedule_status: coverage_index_selected
round_sector_consistency: pass
large_sector_id: L4_MATERIALS_SPREAD_RESOURCE
canonical_archetype_id: C15_MATERIAL_SPREAD_SUPERCYCLE
fine_archetype_id: COPPER_ZINC_STEEL_SPREAD_MARGIN_BRIDGE_VS_COMMODITY_HEADLINE_BLOWOFF
new_independent_case_count: 4
reused_case_count: 0
same_archetype_new_symbol_count: 4
same_archetype_new_trigger_family_count: 4
calibration_usable_case_count: 4
calibration_usable_trigger_count: 4
positive_case_count: 1
mixed_positive_count: 1
counterexample_count: 2
current_profile_error_count: 4
do_not_propose_new_weight_delta: false
auto_selected_coverage_gap: C15 rows 6 -> 10 if accepted; still Priority 0, need 20 to 30
sector_specific_rule_candidate: true
canonical_archetype_rule_candidate: true
loop_contribution_label: canonical_archetype_rule_candidate
new_axis_proposed: C15_company_margin_bridge_required
existing_axis_strengthened: price_only_blowoff_blocks_positive_stage | full_4b_requires_non_price_evidence | local_4b_after_blowoff
existing_axis_weakened: null
next_recommended_archetypes: C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION, C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN, C22_INSURANCE_RATE_CYCLE_RESERVE, C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT, C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG, C16_STRATEGIC_RESOURCE_POLICY_SUPPLY, C17_CHEMICAL_COMMODITY_MARGIN_SPREAD
```
