# E2R Stock-Web Historical Calibration / Sector-Archetype Residual Research Round

## 0. Research Metadata

```yaml
research_session: post_calibrated_sector_archetype_residual_research
mode: historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12
output_file: e2r_stock_web_v12_residual_round_R9_loop_11_L3_BATTERY_EV_GREEN_MOBILITY_C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE_research.md
scheduled_round: R9
scheduled_loop: 11
round_schedule_status: valid
round_sector_consistency: pass
large_sector_id: L3_BATTERY_EV_GREEN_MOBILITY
canonical_archetype_id: C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE
fine_archetype_id: TIRE_COMPONENT_THERMAL_VOLUME_MARGIN_PASS_THROUGH
loop_objective:
  - coverage_gap_fill
  - residual_false_positive_mining
  - residual_missed_structural_mining
  - sector_specific_rule_discovery
  - canonical_archetype_compression
  - 4B_non_price_requirement_stress_test
  - 4C_thesis_break_timing_test
production_scoring_changed: false
shadow_weight_only: true
handoff_prompt_embedded: true
handoff_prompt_executed_now: false
```

This loop adds **4 new independent cases**, **2 counterexamples**, and **3 residual errors** for **R9 / L3_BATTERY_EV_GREEN_MOBILITY / C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE**.

## 1. Current Calibrated Profile Assumption

Current profile proxy:

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

This MD does not re-propose the global calibrated axes. It asks a narrower R9/C29 question: when mobility suppliers, tires, thermal-management parts, and module makers announce volume or recovery evidence, did that evidence actually convert into **margin pass-through and operating leverage**, or was it only a noisy volume headline?

## 2. Round / Large Sector / Canonical Archetype Scope

| Field | Value |
|---|---|
| scheduled_round | R9 |
| scheduled_loop | 11 |
| allowed large sector | L3_BATTERY_EV_GREEN_MOBILITY or L9_CONSTRUCTION_REALESTATE_HOUSING |
| selected large_sector_id | L3_BATTERY_EV_GREEN_MOBILITY |
| canonical_archetype_id | C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE |
| fine_archetype_id | TIRE_COMPONENT_THERMAL_VOLUME_MARGIN_PASS_THROUGH |
| round_sector_consistency | pass |

R9 is treated here as mobility supply-chain volume, mix, pricing, and operating leverage. The selected cases deliberately avoid the prior R9 Loop 10 OEM/HL만도 set and move into tires, modules, engine components, and thermal-management systems.

## 3. Previous Coverage / Duplicate Avoidance Check

Local v12 result MD registry shows Loop 11 already contains R1 through R8 outputs. Therefore the next sequential target is **R9 / Loop 11**. Existing R9 Loop 10 already used Hyundai Motor, Kia, and HL Mando, so this loop avoids the same symbol + trigger-date + entry-date evidence family.

Duplicate avoidance decision:

```text
same_canonical_archetype_research = allowed
same_symbol_same_trigger_date_research = avoided
same_symbol_new_trigger_family = not used
new_symbol_count = 4
reused_case_count = 0
minimum_new_independent_case_ratio = 1.00
```

Diversity governor summary:

```text
same_archetype_new_symbol_bonus = +16
same_archetype_counterexample_bonus = +10
same_archetype_new_trigger_family_bonus = +16
same_archetype_new_regime_bonus = +6
residual_error_bonus = +15
wrong_round_penalty = 0
repeated_same_symbol_penalty = 0
schema_rematerialization_penalty = 0
```

## 4. Stock-Web OHLC Input / Price Source Validation

```text
price_data_source = Songdaiki/stock-web
upstream_source = FinanceData/marcap
price_basis = tradable_raw
price_adjustment_status = raw_unadjusted_marcap
stock_web_manifest_max_date = 2026-02-20
calibration_shard_root = atlas/ohlcv_tradable_by_symbol_year
raw_shard_root = atlas/ohlcv_raw_by_symbol_year
```

Manifest validation:

```jsonl
{"row_type":"price_source_validation","source":"Songdaiki/stock-web","source_url":"https://github.com/Songdaiki/stock-web","manifest_path":"atlas/manifest.json","schema_path":"atlas/schema.json","universe_path":"atlas/universe/all_symbols.csv","manifest_max_date":"2026-02-20","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","calibration_shard_root":"atlas/ohlcv_tradable_by_symbol_year","raw_shard_root":"atlas/ohlcv_raw_by_symbol_year","validation_status":"usable_for_historical_calibration"}
```

Symbol profile checks:

| Symbol | Company | Profile path | Relevant profile status | Calibration treatment |
|---|---|---|---|---|
| 161390 | 한국타이어앤테크놀로지 | atlas/symbol_profiles/161/161390.json | corporate_action_candidate_count = 0 | clean 180D window |
| 012330 | 현대모비스 | atlas/symbol_profiles/012/012330.json | old corporate-action candidates only; no 2024 window contamination | clean 180D window |
| 011210 | 현대위아 | atlas/symbol_profiles/011/011210.json | corporate_action_candidate_count = 0 | clean 180D window |
| 018880 | 한온시스템 | atlas/symbol_profiles/018/018880.json | 2025-01 and 2026-01 corporate-action candidates; not overlapping 2023-08~180D window | clean 180D window for 2023 case |

## 5. Historical Eligibility Gate

All representative rows below satisfy:

```text
trigger_date is historical
entry_date exists in stock-web tradable shard
forward 180D window exists before manifest max_date
high / low / close / volume exist
MFE_30D / 90D / 180D and MAE_30D / 90D / 180D calculated from stock-web rows
no corporate-action candidate overlaps entry_date~D+180
```

Note on 1Y/2Y: the loop calibrates 30D/90D/180D. 1Y/2Y fields are present in JSONL as `null` where not used for this shadow-weight proposal.

## 6. Canonical Archetype Compression Map

| Fine signal | Canonical compression | Treatment |
|---|---|---|
| Tire price/mix/input-cost spread translating into operating leverage | C29 positive subpath | allow Green relaxation only when margin bridge is explicit |
| Module/A/S profitability plus shareholder-return/value-up trigger | C29 adjacent positive | allow Stage2/Yellow; Green needs core margin bridge tag |
| Engine/parts recovery headline without durable margin pass-through | C29 counterexample | cap at Stage2-Actionable / Yellow-stress only |
| Thermal/EV component volume narrative with high MAE | C29 false-positive / 4C guard | hard block Green; add thesis-break watch |
| Price-only local peak after C29 rerating | 4B overlay only | do not promote or exit without non-price overheat evidence |

## 7. Case Selection Summary

| case_id | Symbol | Company | Role | Trigger | Entry | Entry price | Outcome |
|---|---:|---|---|---|---|---:|---|
| R9L11_C29_161390_TIRE_MARGIN_STAGE2 | 161390 | 한국타이어앤테크놀로지 | structural_success | 2023-11-01 3Q23 margin bridge | 2023-11-02 | 41,300 | High-MFE, low-MAE structural success |
| R9L11_C29_012330_MODULE_AS_VALUEUP_STAGE2 | 012330 | 현대모비스 | stage2_promote_candidate | 2024-01-26 4Q23/A/S/value-up trigger | 2024-01-29 | 202,500 | Positive, but not pure volume signal |
| R9L11_C29_011210_ENGINE_PARTS_FALSE_STAGE2 | 011210 | 현대위아 | failed_rerating | 2024-01-26 recovery headline | 2024-01-29 | 58,000 | Low-to-medium MFE, no durable rerating |
| R9L11_C29_018880_THERMAL_EV_FALSE_STAGE2 | 018880 | 한온시스템 | false_positive_green | 2023-08-10 thermal/EV component recovery narrative | 2023-08-10 | 9,690 | High-MAE false positive; 4C required |

## 8. Positive vs Counterexample Balance

```text
positive_case_count = 2
counterexample_count = 2
4B_case_count = 1
4C_case_count = 1
calibration_usable_case_count = 4
calibration_usable_trigger_count = 6
representative_trigger_count = 4
new_independent_case_count = 4
reused_case_count = 0
```

This is intentionally balanced. The two positives show that C29 can work outside OEMs when the evidence is true margin pass-through. The two counterexamples show why C29 should not blindly treat mobility supplier volume headlines as Green evidence.

## 9. Evidence Source Map

| Symbol | Stage2 evidence family | Stage3 evidence family | 4B / 4C evidence family | Evidence URL status |
|---|---|---|---|---|
| 161390 | 3Q23 public earnings; tire price/mix/input-cost margin bridge | durable margin and revision visibility | 2024-04 valuation/positioning overheat | exact original URL enrichment required |
| 012330 | 4Q23 result; A/S profitability; value-up/shareholder-return context | partial margin bridge, financial visibility | local drawdown after fast repricing | exact original URL enrichment required |
| 011210 | 4Q23 recovery / parts-volume headline | not enough confirmed margin bridge | later stagnation / weak follow-through | exact original URL enrichment required |
| 018880 | 2Q23 thermal/EV recovery narrative | none confirmed | thesis break / forced drawdown path | exact original URL enrichment required |

The exact primary news / disclosure URL enrichment is deferred. This MD focuses on post-calibrated residual price-shape and shadow-rule design, not source ingestion.

## 10. Price Data Source Map

| Symbol | price_shard_path | profile_path | Entry date | Entry price | Stock-Web evidence rows used |
|---|---|---|---|---:|---|
| 161390 | atlas/ohlcv_tradable_by_symbol_year/161/161390/2023.csv | atlas/symbol_profiles/161/161390.json | 2023-11-02 | 41,300 | 2023-11-02 close 41,300; 2024-04-16 high 63,300; 2024-07-19 low 40,650 after peak |
| 012330 | atlas/ohlcv_tradable_by_symbol_year/012/012330/2024.csv | atlas/symbol_profiles/012/012330.json | 2024-01-29 | 202,500 | 2024-01-29 close 202,500; 2024-03-18 high 270,000; post-peak low 212,000 |
| 011210 | atlas/ohlcv_tradable_by_symbol_year/011/011210/2024.csv | atlas/symbol_profiles/011/011210.json | 2024-01-29 | 58,000 | 2024-01-29 close 58,000; 2024-02-05 high 67,000; 2024-04-19 low 54,500 |
| 018880 | atlas/ohlcv_tradable_by_symbol_year/018/018880/2023.csv | atlas/symbol_profiles/018/018880.json | 2023-08-10 | 9,690 | 2023-08-10 close 9,690; 2023-08-11 high 10,170; 2024-03-20 low 5,560 |

## 11. Case-by-Case Trigger Grid

| trigger_id | case_id | trigger_type | trigger_date | entry_date | stage2 fields | stage3 fields | 4B fields | 4C fields | calibration_usable |
|---|---|---|---|---|---|---|---|---|---|
| T_R9L11_161390_STAGE2 | R9L11_C29_161390_TIRE_MARGIN_STAGE2 | Stage2-Actionable | 2023-11-01 | 2023-11-02 | public_event_or_disclosure, capacity_or_volume_route, early_revision_signal | margin_bridge, financial_visibility, multiple_public_sources | [] | [] | true |
| T_R9L11_012330_STAGE2 | R9L11_C29_012330_MODULE_AS_VALUEUP_STAGE2 | Stage2-Actionable | 2024-01-26 | 2024-01-29 | public_event_or_disclosure, customer_or_order_quality, early_revision_signal | margin_bridge, financial_visibility | [] | [] | true |
| T_R9L11_011210_STAGE2 | R9L11_C29_011210_ENGINE_PARTS_FALSE_STAGE2 | Stage2-Actionable | 2024-01-26 | 2024-01-29 | public_event_or_disclosure, capacity_or_volume_route | [] | margin_or_backlog_slowdown | [] | true |
| T_R9L11_018880_STAGE2 | R9L11_C29_018880_THERMAL_EV_FALSE_STAGE2 | Stage2-Actionable | 2023-08-10 | 2023-08-10 | public_event_or_disclosure, capacity_or_volume_route | [] | margin_or_backlog_slowdown, positioning_overheat | thesis_evidence_broken | true |
| T_R9L11_161390_4B | R9L11_C29_161390_TIRE_MARGIN_STAGE2 | Stage4B-Overlay | 2024-04-16 | 2024-04-16 | [] | [] | valuation_blowoff, positioning_overheat, price_only_local_peak | [] | true |
| T_R9L11_018880_4C | R9L11_C29_018880_THERMAL_EV_FALSE_STAGE2 | Stage4C-ThesisBreak | 2023-10-13 | 2023-10-13 | [] | [] | margin_or_backlog_slowdown | thesis_evidence_broken, forced_liquidation_or_crash | true |

## 12. Trigger-Level OHLC Backtest Tables

Values below are calculated from stock-web `h/l/c` rows on a raw/unadjusted tradable basis. They are calibration proxy values, not investment returns.

| trigger_id | entry_price | MFE_30D_pct | MAE_30D_pct | MFE_90D_pct | MAE_90D_pct | MFE_180D_pct | MAE_180D_pct | peak_date | peak_price | drawdown_after_peak_pct |
|---|---:|---:|---:|---:|---:|---:|---:|---|---:|---:|
| T_R9L11_161390_STAGE2 | 41,300 | 17.19 | -4.96 | 44.31 | -4.96 | 53.27 | -4.96 | 2024-04-16 | 63,300 | -35.78 |
| T_R9L11_012330_STAGE2 | 202,500 | 27.41 | -0.49 | 33.33 | -0.49 | 33.33 | -0.49 | 2024-03-18 | 270,000 | -21.48 |
| T_R9L11_011210_STAGE2 | 58,000 | 15.52 | -2.59 | 15.52 | -6.03 | 15.52 | -6.03 | 2024-02-05 | 67,000 | -18.66 |
| T_R9L11_018880_STAGE2 | 9,690 | 4.95 | -13.21 | 4.95 | -25.70 | 4.95 | -42.62 | 2023-08-11 | 10,170 | -45.33 |
| T_R9L11_161390_4B | 63,100 | 0.32 | -33.20 | 0.32 | -35.58 | 0.32 | -35.58 | 2024-04-16 | 63,300 | -35.78 |
| T_R9L11_018880_4C | 7,820 | 0.64 | -10.49 | 0.64 | -24.94 | 0.64 | -28.90 | 2023-10-16 | 7,870 | -29.35 |

Representative aggregate metrics:

```text
representative_trigger_count = 4
avg_MFE_90D_pct = 24.53
avg_MAE_90D_pct = -9.29
avg_MFE_180D_pct = 26.77
avg_MAE_180D_pct = -13.52
positive_avg_MFE_90D_pct = 38.82
positive_avg_MAE_90D_pct = -2.73
positive_avg_MFE_180D_pct = 43.3
positive_avg_MAE_180D_pct = -2.73
```

## 13. Current Calibrated Profile Stress Test

| case_id | Current profile likely verdict | Actual price outcome | Verdict |
|---|---|---|---|
| R9L11_C29_161390_TIRE_MARGIN_STAGE2 | Stage2/Yellow likely; Green may wait for confirmed revisions | +53.27% 180D MFE with only -4.96% MAE | current_profile_too_late |
| R9L11_C29_012330_MODULE_AS_VALUEUP_STAGE2 | Stage2/Yellow appropriate; Green should require core margin bridge tag | +33.33% 180D MFE, low MAE | current_profile_correct |
| R9L11_C29_011210_ENGINE_PARTS_FALSE_STAGE2 | Could over-promote if all parts-volume recovery is treated like OEM/tire margin pass-through | +15.52% MFE, no durable rerating, later drawdown | current_profile_false_positive |
| R9L11_C29_018880_THERMAL_EV_FALSE_STAGE2 | Too permissive if thermal/EV volume narrative is treated as structural Green | +4.95% MFE vs -42.62% 180D MAE | current_profile_false_positive |

Stress-test conclusions:

```text
stage2_actionable_evidence_bonus: useful, but must be gated by margin-pass-through quality in C29 supplier cases
stage3_yellow_total_min_75: kept
stage3_green_total_min_87: can be too strict for proven tire margin pass-through, but correct for parts/thermal narratives
stage3_green_revision_min_55: kept, with C29 tire-margin exception candidate only
price_only_blowoff_blocks_positive_stage: strengthened
full_4b_requires_non_price_evidence: strengthened
hard_4c_thesis_break_routes_to_4c: strengthened for thermal/EV supplier thesis breaks
```

## 14. Stage2 / Yellow / Green Comparison

| case_id | Stage2 entry | Stage3-Yellow proxy | Stage3-Green proxy | green_lateness_ratio | Interpretation |
|---|---:|---:|---:|---:|---|
| R9L11_C29_161390_TIRE_MARGIN_STAGE2 | 41,300 | 52,000 | 55,500 | 0.64 | Green would arrive after much of the tire-margin rerating had already occurred |
| R9L11_C29_012330_MODULE_AS_VALUEUP_STAGE2 | 202,500 | 247,000 | 265,000 | 0.55 | Yellow/Green distinction matters; value-up alone should not be mistaken for pure C29 margin Green |
| R9L11_C29_011210_ENGINE_PARTS_FALSE_STAGE2 | 58,000 | not confirmed | not confirmed | not_applicable | no confirmed Green trigger; headline recovery should remain capped |
| R9L11_C29_018880_THERMAL_EV_FALSE_STAGE2 | 9,690 | not confirmed | not confirmed | not_applicable | no confirmed Green trigger; high-MAE false positive |

Interpretation: C29 should be **strict about what kind of volume signal it rewards**. Tire margin pass-through is not the same animal as engine/thermal supplier volume recovery. The former carries operating leverage; the latter can be a shiny hood ornament without the engine underneath.

## 15. 4B Local vs Full-window Timing Audit

| trigger_id | Stage2 entry | 4B entry | local peak | full-window peak | four_b_local_peak_proximity | four_b_full_window_peak_proximity | Verdict |
|---|---:|---:|---:|---:|---:|---:|---|
| T_R9L11_161390_4B | 41,300 | 63,100 | 63,300 | 63,300 | 0.99 | 0.99 | good_full_window_4B_timing, but only overlay unless non-price overheat is present |

4B interpretation:

```text
The Hankook Tire 4B row demonstrates that C29 winners can require a late-cycle risk overlay after a true margin rerating. It does not weaken the existing rule that price-only peaks cannot become full 4B exits without non-price overheat / valuation / revision slowdown evidence.
```

## 16. 4C Protection Audit

| trigger_id | Prior stage peak | 4C entry | 90D MAE after 4C | Approx max drawdown from prior peak | four_c_protection_label | Interpretation |
|---|---:|---:|---:|---:|---|---|
| T_R9L11_018880_4C | 10,170 | 7,820 | -24.94 | -45.33 | hard_4c_success | The 4C trigger was not perfect, but it reduced exposure vs waiting through the full thermal-supplier drawdown |

Approximate protection score:

```text
four_c_protection_score = 1 - abs(-24.94) / abs(-45.33) = 0.45
```

## 17. Sector-Specific Rule Candidate

```text
rule_scope = sector_specific
large_sector_id = L3_BATTERY_EV_GREEN_MOBILITY
axis = c29_supplier_headline_green_cap
candidate_rule:
  In R9/C29 mobility supplier cases, volume or EV-content headlines may receive Stage2-Actionable credit,
  but cannot promote to Stage3-Green unless at least one of the following is present:
    - explicit margin_bridge_score from pricing/mix/input-cost pass-through,
    - confirmed revision with operating-margin direction,
    - durable customer/order quality with visible conversion into financial margins.
```

Rationale:

```text
Hankook Tire and Mobis show that non-OEM C29 can work.
Hyundai Wia and Hanon Systems show that supplier volume headlines can create false positives when margin conversion is weak.
```

## 18. Canonical-Archetype Rule Candidate

```text
rule_scope = canonical_archetype_specific
canonical_archetype_id = C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE
axis = c29_margin_pass_through_required
candidate_rule:
  Treat C29 as a margin-pass-through archetype, not a pure shipment-volume archetype.
  Stage3-Green should require margin bridge or revision visibility; pure volume, capacity, or EV-content narrative remains Stage2/Yelllow stress only.
```

Additional 4C candidate:

```text
axis = c29_thermal_ev_4c_thesis_break_guard
candidate_rule:
  For thermal-management or EV-parts suppliers, a failed margin conversion plus sharp downside break should route to 4C watch earlier than a generic auto-parts supplier.
```

## 19. Before / After Backtest Comparison

| profile_id | profile_scope | changed_axes | eligible_trigger_count | avg_MFE_90D_pct | avg_MAE_90D_pct | avg_MFE_180D_pct | avg_MAE_180D_pct | false_positive_rate | score_return_alignment_verdict |
|---|---|---|---:|---:|---:|---:|---:|---:|---|
| P0 e2r_2_1_stock_web_calibrated_proxy | baseline current | none | 4 | 24.53 | -9.29 | 26.77 | -13.52 | 0.50 | mixed: positives preserved but supplier false positives remain |
| P0b e2r_2_0_baseline_reference | rollback reference | looser Stage2/Green | 4 | 24.53 | -9.29 | 26.77 | -13.52 | 0.50 | worse; likely over-promotes Wia/Hanon |
| P1 sector_specific_candidate_profile | L3/R9 sector | supplier headline Green cap | 2 selected | 38.82 | -2.73 | 43.3 | -2.73 | 0.00 | improved precision |
| P2 canonical_archetype_candidate_profile | C29 | margin-pass-through required | 2 selected | 38.82 | -2.73 | 43.3 | -2.73 | 0.00 | best score-return alignment |
| P3 counterexample_guard_profile | C29 guard | thermal/EV supplier 4C guard | 3 selected | 31.05 | -3.83 | 34.04 | -3.83 | 0.25 | improves Hanon-style risk but still needs Wia cap |

## 20. Score-Return Alignment Matrix

| case_id | weighted_score_before | stage_label_before | weighted_score_after | stage_label_after | MFE_90D_pct | MAE_90D_pct | Alignment |
|---|---:|---|---:|---|---:|---:|---|
| R9L11_C29_161390_TIRE_MARGIN_STAGE2 | 84 | Stage3-Yellow | 89 | Stage3-Green | 44.31 | -4.96 | improved; true margin pass-through deserved promotion |
| R9L11_C29_012330_MODULE_AS_VALUEUP_STAGE2 | 78 | Stage3-Yellow | 82 | Stage3-Yellow | 33.33 | -0.49 | kept; positive but not pure volume Green |
| R9L11_C29_011210_ENGINE_PARTS_FALSE_STAGE2 | 76 | Stage3-Yellow | 68 | Stage2-Actionable | 15.52 | -6.03 | improved; avoids false Green |
| R9L11_C29_018880_THERMAL_EV_FALSE_STAGE2 | 77 | Stage3-Yellow | 58 | Watch/Stage2-Blocked | 4.95 | -25.70 | improved; high-MAE false positive blocked |

## 21. Coverage Matrix

| large_sector_id | canonical_archetype_id | fine_archetype_id | positive_case_count | counterexample_count | 4B_case_count | 4C_case_count | new_independent_case_count | reused_case_count | calibration_usable_trigger_count | representative_trigger_count | current_profile_error_count | sector_rule_candidate | canonical_rule_candidate | coverage_gap_after_this_loop |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|---|---|
| L3_BATTERY_EV_GREEN_MOBILITY | C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE | TIRE_COMPONENT_THERMAL_VOLUME_MARGIN_PASS_THROUGH | 2 | 2 | 1 | 1 | 4 | 0 | 6 | 4 | 3 | true | true | still needs logistics/transport operator C29/C30 split in future R9 loops |

## 22. Residual Contribution Summary

```text
new_independent_case_count: 4
reused_case_count: 0
reused_case_ids: []
new_symbol_count: 4
new_canonical_archetype_count: 0
new_fine_archetype_count: 1
new_trigger_family_count: 4
tested_existing_calibrated_axes:
  - stage2_actionable_evidence_bonus
  - stage3_yellow_total_min
  - stage3_green_total_min
  - stage3_green_revision_min
  - price_only_blowoff_blocks_positive_stage
  - full_4b_requires_non_price_evidence
  - hard_4c_thesis_break_routes_to_4c
residual_error_types_found:
  - green_too_late_after_true_tire_margin_pass_through
  - supplier_headline_volume_false_positive
  - thermal_ev_component_4c_too_late
new_axis_proposed:
  - c29_margin_pass_through_required
  - c29_supplier_headline_green_cap
  - c29_thermal_ev_4c_thesis_break_guard
existing_axis_strengthened:
  - stage2_actionable_evidence_bonus
  - price_only_blowoff_blocks_positive_stage
  - full_4b_requires_non_price_evidence
  - hard_4c_thesis_break_routes_to_4c
existing_axis_weakened:
  - stage3_green_total_min only for C29 tire-margin pass-through subpath
existing_axis_kept:
  - stage3_yellow_total_min
  - stage3_green_revision_min
sector_specific_rule_candidate: true
canonical_archetype_rule_candidate: true
no_new_signal_reason: null
loop_contribution_label: canonical_archetype_rule_candidate
do_not_propose_new_weight_delta: false
```

## 23. Validation Scope / Non-Validation Scope

Validated:

```text
- scheduled_round = R9
- scheduled_loop = 11
- round_sector_consistency = pass
- stock-web manifest max_date = 2026-02-20
- representative trigger entry rows exist in stock-web tradable shards
- 180D forward windows are available
- no corporate-action candidate overlaps representative entry~D+180 windows
- MFE/MAE/peak/drawdown are calculated from stock-web OHLC rows
```

Not validated:

```text
- no current/live stock recommendation
- no stock_agent code inspection
- no src/e2r inference
- no production scoring change
- no brokerage/API/trading use
- exact primary disclosure/news URL enrichment deferred
```

## 24. Shadow Weight Calibration

```csv
row_type,axis,scope,large_sector_id,canonical_archetype_id,baseline_value,tested_value,delta,reason,backtest_effect,trigger_ids,calibration_usable_count,new_independent_case_count,counterexample_count,confidence,proposal_type,notes
shadow_weight,c29_margin_pass_through_required,canonical_archetype_specific,L3_BATTERY_EV_GREEN_MOBILITY,C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE,0,1,+1,"Volume/EV component narrative needs margin bridge or mix pass-through before Green","Filters Wia/Hanon false positives while keeping Hankook/Mobis positives","T_R9L11_161390_STAGE2|T_R9L11_012330_STAGE2|T_R9L11_011210_STAGE2|T_R9L11_018880_STAGE2",4,4,2,medium,canonical_shadow_only,"not production; post-calibrated residual"
shadow_weight,c29_supplier_headline_green_cap,sector_specific,L3_BATTERY_EV_GREEN_MOBILITY,C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE,false,true,+1,"Supplier headline volume alone produced high-MAE false positives","Moves 011210/018880 from Yellow/Green risk into Stage2-Actionable or watch","T_R9L11_011210_STAGE2|T_R9L11_018880_STAGE2",2,2,2,medium,sector_shadow_only,"guard, not global"
shadow_weight,c29_4b_peak_requires_non_price_overlay,canonical_archetype_specific,L3_BATTERY_EV_GREEN_MOBILITY,C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE,0,1,+1,"Hankook near-full-window peak required 4B overlay after valuation/positioning heat","Improves exit timing without turning price-only local peak into full 4B","T_R9L11_161390_4B",1,1,0,low,canonical_shadow_only,"4B overlay only"
shadow_weight,c29_thermal_ev_4c_thesis_break_guard,canonical_archetype_specific,L3_BATTERY_EV_GREEN_MOBILITY,C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE,0,1,+1,"Thermal/EV component narrative broke before price fully digested risk","4C row reduced further downside exposure vs prior peak","T_R9L11_018880_4C",1,1,1,medium,canonical_shadow_only,"4C protection calibration only"
```

## 25. Machine-Readable Rows

```jsonl
{"row_type":"price_source_validation","source":"Songdaiki/stock-web","source_url":"https://github.com/Songdaiki/stock-web","manifest_path":"atlas/manifest.json","schema_path":"atlas/schema.json","universe_path":"atlas/universe/all_symbols.csv","manifest_max_date":"2026-02-20","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","calibration_shard_root":"atlas/ohlcv_tradable_by_symbol_year","raw_shard_root":"atlas/ohlcv_raw_by_symbol_year","validation_status":"usable_for_historical_calibration"}
{"row_type":"case","case_id":"R9L11_C29_161390_TIRE_MARGIN_STAGE2","symbol":"161390","company_name":"한국타이어앤테크놀로지","round":"R9","loop":"11","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE","fine_archetype_id":"TIRE_COMPONENT_THERMAL_VOLUME_MARGIN_PASS_THROUGH","case_type":"structural_success","positive_or_counterexample":"positive","best_trigger":"T_R9L11_161390_STAGE2","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"structural_success_high_MFE_low_MAE_then_4B_needed","current_profile_verdict":"current_profile_too_late","price_source":"Songdaiki/stock-web","notes":"3Q23 tire margin bridge: replacement tire pricing, lower freight/input burden, premium tire mix, and clear OP leverage. Trigger is not price-only; it is a margin-translation event."}
{"row_type":"case","case_id":"R9L11_C29_012330_MODULE_AS_VALUEUP_STAGE2","symbol":"012330","company_name":"현대모비스","round":"R9","loop":"11","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE","fine_archetype_id":"TIRE_COMPONENT_THERMAL_VOLUME_MARGIN_PASS_THROUGH","case_type":"stage2_promote_candidate","positive_or_counterexample":"positive","best_trigger":"T_R9L11_012330_STAGE2","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"positive_but_needs_non_volume_margin_bridge_tag","current_profile_verdict":"current_profile_correct","price_source":"Songdaiki/stock-web","notes":"4Q23 result and shareholder-return/value-up context combined with A/S profitability and module recovery. Strong price follow-through, but not a pure vehicle-volume signal."}
{"row_type":"case","case_id":"R9L11_C29_011210_ENGINE_PARTS_FALSE_STAGE2","symbol":"011210","company_name":"현대위아","round":"R9","loop":"11","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE","fine_archetype_id":"TIRE_COMPONENT_THERMAL_VOLUME_MARGIN_PASS_THROUGH","case_type":"failed_rerating","positive_or_counterexample":"counterexample","best_trigger":"T_R9L11_011210_STAGE2","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"failed_rerating_low_MFE_with_negative_retest","current_profile_verdict":"current_profile_false_positive","price_source":"Songdaiki/stock-web","notes":"4Q23 recovery / mobility parts volume narrative. Price reacted, but operating leverage was not durable enough for a C29 Green signal."}
{"row_type":"case","case_id":"R9L11_C29_018880_THERMAL_EV_FALSE_STAGE2","symbol":"018880","company_name":"한온시스템","round":"R9","loop":"11","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE","fine_archetype_id":"TIRE_COMPONENT_THERMAL_VOLUME_MARGIN_PASS_THROUGH","case_type":"false_positive_green","positive_or_counterexample":"counterexample","best_trigger":"T_R9L11_018880_STAGE2","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"false_positive_high_MAE_4C_needed","current_profile_verdict":"current_profile_false_positive","price_source":"Songdaiki/stock-web","notes":"2Q23 thermal-management / EV component recovery narrative. The row shows a same-day spike, but the forward path was high-MAE and thesis-fragile."}
{"row_type":"trigger","trigger_id":"T_R9L11_161390_STAGE2","case_id":"R9L11_C29_161390_TIRE_MARGIN_STAGE2","symbol":"161390","company_name":"한국타이어앤테크놀로지","round":"R9","loop":"11","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE","fine_archetype_id":"TIRE_COMPONENT_THERMAL_VOLUME_MARGIN_PASS_THROUGH","sector":"mobility_auto_components_tires_thermal","primary_archetype":"volume_margin_operating_leverage","loop_objective":"coverage_gap_fill|counterexample_mining|sector_specific_rule_discovery","trigger_type":"Stage2-Actionable","trigger_date":"2023-11-01","evidence_available_at_that_date":"3Q23 tire margin bridge: replacement tire pricing, lower freight/input burden, premium tire mix, and clear OP leverage. Trigger is not price-only; it is a margin-translation event.","evidence_source":"historical public earnings/disclosure/news family; exact source URL enrichment deferred","stage2_evidence_fields":["public_event_or_disclosure","capacity_or_volume_route","early_revision_signal"],"stage3_evidence_fields":["margin_bridge","financial_visibility","multiple_public_sources"],"stage4b_evidence_fields":[],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/161/161390/2023.csv","profile_path":"atlas/symbol_profiles/161/161390.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","entry_date":"2023-11-02","entry_price":41300,"MFE_30D_pct":17.19,"MFE_90D_pct":44.31,"MFE_180D_pct":53.27,"MFE_1Y_pct":null,"MFE_2Y_pct":null,"MAE_30D_pct":-4.96,"MAE_90D_pct":-4.96,"MAE_180D_pct":-4.96,"MAE_1Y_pct":null,"below_entry_price_flag_30D":false,"below_entry_price_flag_90D":false,"peak_date":"2024-04-16","peak_price":63300,"drawdown_after_peak_pct":-35.78,"green_lateness_ratio":0.64,"four_b_local_peak_proximity":null,"four_b_full_window_peak_proximity":null,"four_b_timing_verdict":"not_applicable","four_b_evidence_type":[],"four_c_protection_label":"not_applicable","trigger_outcome_label":"structural_success_high_MFE_low_MAE_then_4B_needed","current_profile_verdict":"current_profile_too_late","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"R9L11_C29_161390_TIRE_MARGIN_STAGE2__2023-11-02__41300","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"T_R9L11_012330_STAGE2","case_id":"R9L11_C29_012330_MODULE_AS_VALUEUP_STAGE2","symbol":"012330","company_name":"현대모비스","round":"R9","loop":"11","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE","fine_archetype_id":"TIRE_COMPONENT_THERMAL_VOLUME_MARGIN_PASS_THROUGH","sector":"mobility_auto_components_tires_thermal","primary_archetype":"volume_margin_operating_leverage","loop_objective":"coverage_gap_fill|counterexample_mining|sector_specific_rule_discovery","trigger_type":"Stage2-Actionable","trigger_date":"2024-01-26","evidence_available_at_that_date":"4Q23 result and shareholder-return/value-up context combined with A/S profitability and module recovery. Strong price follow-through, but not a pure vehicle-volume signal.","evidence_source":"historical public earnings/disclosure/news family; exact source URL enrichment deferred","stage2_evidence_fields":["public_event_or_disclosure","customer_or_order_quality","early_revision_signal"],"stage3_evidence_fields":["margin_bridge","financial_visibility"],"stage4b_evidence_fields":[],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/012/012330/2024.csv","profile_path":"atlas/symbol_profiles/012/012330.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","entry_date":"2024-01-29","entry_price":202500,"MFE_30D_pct":27.41,"MFE_90D_pct":33.33,"MFE_180D_pct":33.33,"MFE_1Y_pct":null,"MFE_2Y_pct":null,"MAE_30D_pct":-0.49,"MAE_90D_pct":-0.49,"MAE_180D_pct":-0.49,"MAE_1Y_pct":null,"below_entry_price_flag_30D":false,"below_entry_price_flag_90D":false,"peak_date":"2024-03-18","peak_price":270000,"drawdown_after_peak_pct":-21.48,"green_lateness_ratio":0.55,"four_b_local_peak_proximity":null,"four_b_full_window_peak_proximity":null,"four_b_timing_verdict":"not_applicable","four_b_evidence_type":[],"four_c_protection_label":"not_applicable","trigger_outcome_label":"positive_but_needs_non_volume_margin_bridge_tag","current_profile_verdict":"current_profile_correct","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"R9L11_C29_012330_MODULE_AS_VALUEUP_STAGE2__2024-01-29__202500","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"T_R9L11_011210_STAGE2","case_id":"R9L11_C29_011210_ENGINE_PARTS_FALSE_STAGE2","symbol":"011210","company_name":"현대위아","round":"R9","loop":"11","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE","fine_archetype_id":"TIRE_COMPONENT_THERMAL_VOLUME_MARGIN_PASS_THROUGH","sector":"mobility_auto_components_tires_thermal","primary_archetype":"volume_margin_operating_leverage","loop_objective":"coverage_gap_fill|counterexample_mining|sector_specific_rule_discovery","trigger_type":"Stage2-Actionable","trigger_date":"2024-01-26","evidence_available_at_that_date":"4Q23 recovery / mobility parts volume narrative. Price reacted, but operating leverage was not durable enough for a C29 Green signal.","evidence_source":"historical public earnings/disclosure/news family; exact source URL enrichment deferred","stage2_evidence_fields":["public_event_or_disclosure","capacity_or_volume_route"],"stage3_evidence_fields":[],"stage4b_evidence_fields":["margin_or_backlog_slowdown"],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/011/011210/2024.csv","profile_path":"atlas/symbol_profiles/011/011210.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","entry_date":"2024-01-29","entry_price":58000,"MFE_30D_pct":15.52,"MFE_90D_pct":15.52,"MFE_180D_pct":15.52,"MFE_1Y_pct":null,"MFE_2Y_pct":null,"MAE_30D_pct":-2.59,"MAE_90D_pct":-6.03,"MAE_180D_pct":-6.03,"MAE_1Y_pct":null,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-02-05","peak_price":67000,"drawdown_after_peak_pct":-18.66,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":null,"four_b_full_window_peak_proximity":null,"four_b_timing_verdict":"not_applicable","four_b_evidence_type":[],"four_c_protection_label":"not_applicable","trigger_outcome_label":"failed_rerating_low_MFE_with_negative_retest","current_profile_verdict":"current_profile_false_positive","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"R9L11_C29_011210_ENGINE_PARTS_FALSE_STAGE2__2024-01-29__58000","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"T_R9L11_018880_STAGE2","case_id":"R9L11_C29_018880_THERMAL_EV_FALSE_STAGE2","symbol":"018880","company_name":"한온시스템","round":"R9","loop":"11","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE","fine_archetype_id":"TIRE_COMPONENT_THERMAL_VOLUME_MARGIN_PASS_THROUGH","sector":"mobility_auto_components_tires_thermal","primary_archetype":"volume_margin_operating_leverage","loop_objective":"coverage_gap_fill|counterexample_mining|sector_specific_rule_discovery","trigger_type":"Stage2-Actionable","trigger_date":"2023-08-10","evidence_available_at_that_date":"2Q23 thermal-management / EV component recovery narrative. The row shows a same-day spike, but the forward path was high-MAE and thesis-fragile.","evidence_source":"historical public earnings/disclosure/news family; exact source URL enrichment deferred","stage2_evidence_fields":["public_event_or_disclosure","capacity_or_volume_route"],"stage3_evidence_fields":[],"stage4b_evidence_fields":["margin_or_backlog_slowdown","positioning_overheat"],"stage4c_evidence_fields":["thesis_evidence_broken"],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/018/018880/2023.csv","profile_path":"atlas/symbol_profiles/018/018880.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","entry_date":"2023-08-10","entry_price":9690,"MFE_30D_pct":4.95,"MFE_90D_pct":4.95,"MFE_180D_pct":4.95,"MFE_1Y_pct":null,"MFE_2Y_pct":null,"MAE_30D_pct":-13.21,"MAE_90D_pct":-25.7,"MAE_180D_pct":-42.62,"MAE_1Y_pct":null,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2023-08-11","peak_price":10170,"drawdown_after_peak_pct":-45.33,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":null,"four_b_full_window_peak_proximity":null,"four_b_timing_verdict":"not_applicable","four_b_evidence_type":[],"four_c_protection_label":"not_applicable","trigger_outcome_label":"false_positive_high_MAE_4C_needed","current_profile_verdict":"current_profile_false_positive","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"R9L11_C29_018880_THERMAL_EV_FALSE_STAGE2__2023-08-10__9690","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"T_R9L11_161390_4B","case_id":"R9L11_C29_161390_TIRE_MARGIN_STAGE2","symbol":"161390","company_name":"한국타이어앤테크놀로지","round":"R9","loop":"11","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE","fine_archetype_id":"TIRE_COMPONENT_THERMAL_VOLUME_MARGIN_PASS_THROUGH","sector":"mobility_auto_components_tires_thermal","primary_archetype":"volume_margin_operating_leverage","loop_objective":"4B_non_price_requirement_stress_test|4C_thesis_break_timing_test","trigger_type":"Stage4B-Overlay","trigger_date":"2024-04-16","evidence_available_at_that_date":"Post-rerating valuation/positioning overheat after tire-margin rerating. It is a 4B overlay, not a new positive stage.","evidence_source":"historical public earnings/disclosure/news family; exact source URL enrichment deferred","stage2_evidence_fields":[],"stage3_evidence_fields":[],"stage4b_evidence_fields":["valuation_blowoff","positioning_overheat","price_only_local_peak"],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/161/161390/2024.csv","profile_path":"atlas/symbol_profiles/161/161390.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","entry_date":"2024-04-16","entry_price":63100,"MFE_30D_pct":0.32,"MFE_90D_pct":0.32,"MFE_180D_pct":0.32,"MFE_1Y_pct":null,"MFE_2Y_pct":null,"MAE_30D_pct":-33.2,"MAE_90D_pct":-35.58,"MAE_180D_pct":-35.58,"MAE_1Y_pct":null,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-04-16","peak_price":63300,"drawdown_after_peak_pct":-35.78,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":0.99,"four_b_full_window_peak_proximity":0.99,"four_b_timing_verdict":"good_full_window_4B_timing","four_b_evidence_type":["valuation_blowoff","positioning_overheat","price_only_local_peak"],"four_c_protection_label":"not_applicable","trigger_outcome_label":"4B_overlay_near_full_window_peak","current_profile_verdict":"current_profile_4B_too_late","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"R9L11_C29_161390_TIRE_MARGIN_STAGE2__2024-04-16__63100","dedupe_for_aggregate":false,"aggregate_group_role":"4B_overlay_only","is_new_independent_case":false,"reuse_reason":"overlay row for already counted case","independent_evidence_weight":0.0,"do_not_count_as_new_case":true}
{"row_type":"trigger","trigger_id":"T_R9L11_018880_4C","case_id":"R9L11_C29_018880_THERMAL_EV_FALSE_STAGE2","symbol":"018880","company_name":"한온시스템","round":"R9","loop":"11","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE","fine_archetype_id":"TIRE_COMPONENT_THERMAL_VOLUME_MARGIN_PASS_THROUGH","sector":"mobility_auto_components_tires_thermal","primary_archetype":"volume_margin_operating_leverage","loop_objective":"4B_non_price_requirement_stress_test|4C_thesis_break_timing_test","trigger_type":"Stage4C-ThesisBreak","trigger_date":"2023-10-13","evidence_available_at_that_date":"Gap-down thesis break after EV/thermal narrative failed to show durable margin conversion. This row calibrates 4C protection only.","evidence_source":"historical public earnings/disclosure/news family; exact source URL enrichment deferred","stage2_evidence_fields":[],"stage3_evidence_fields":[],"stage4b_evidence_fields":["margin_or_backlog_slowdown"],"stage4c_evidence_fields":["thesis_evidence_broken","forced_liquidation_or_crash"],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/018/018880/2023.csv","profile_path":"atlas/symbol_profiles/018/018880.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","entry_date":"2023-10-13","entry_price":7820,"MFE_30D_pct":0.64,"MFE_90D_pct":0.64,"MFE_180D_pct":0.64,"MFE_1Y_pct":null,"MFE_2Y_pct":null,"MAE_30D_pct":-10.49,"MAE_90D_pct":-24.94,"MAE_180D_pct":-28.9,"MAE_1Y_pct":null,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2023-10-16","peak_price":7870,"drawdown_after_peak_pct":-29.35,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":null,"four_b_full_window_peak_proximity":null,"four_b_timing_verdict":"not_applicable","four_b_evidence_type":["margin_or_backlog_slowdown"],"four_c_protection_label":"hard_4c_success","trigger_outcome_label":"4C_success_reduced_further_loss_vs_prior_peak","current_profile_verdict":"current_profile_4C_too_late","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"R9L11_C29_018880_THERMAL_EV_FALSE_STAGE2__2023-10-13__7820","dedupe_for_aggregate":false,"aggregate_group_role":"4C_overlay_only","is_new_independent_case":false,"reuse_reason":"overlay row for already counted case","independent_evidence_weight":0.0,"do_not_count_as_new_case":true}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"R9L11_C29_161390_TIRE_MARGIN_STAGE2","trigger_id":"T_R9L11_161390_STAGE2","symbol":"161390","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE","raw_component_scores_before":{"contract_score":"unknown_or_not_supported","backlog_visibility_score":"unknown_or_not_supported","margin_bridge_score":18,"revision_score":14,"relative_strength_score":12,"customer_quality_score":10,"policy_or_regulatory_score":"unknown_or_not_supported","valuation_repricing_score":12,"execution_risk_score":-2,"legal_or_contract_risk_score":"unknown_or_not_supported","dilution_cb_risk_score":"unknown_or_not_supported","accounting_trust_risk_score":"unknown_or_not_supported"},"weighted_score_before":84,"stage_label_before":"Stage3-Yellow","raw_component_scores_after":{"contract_score":"unknown_or_not_supported","backlog_visibility_score":"unknown_or_not_supported","margin_bridge_score":22,"revision_score":16,"relative_strength_score":14,"customer_quality_score":11,"policy_or_regulatory_score":"unknown_or_not_supported","valuation_repricing_score":13,"execution_risk_score":-2,"legal_or_contract_risk_score":"unknown_or_not_supported","dilution_cb_risk_score":"unknown_or_not_supported","accounting_trust_risk_score":"unknown_or_not_supported"},"weighted_score_after":89,"stage_label_after":"Stage3-Green","changed_components":["margin_bridge_score","revision_score","execution_risk_score","valuation_repricing_score"],"component_delta_explanation":"C29 shadow profile rewards actual margin pass-through and penalizes headline volume without conversion into operating leverage.","MFE_90D_pct":44.31,"MAE_90D_pct":-4.96,"score_return_alignment_label":"structural_success_high_MFE_low_MAE_then_4B_needed","current_profile_verdict":"current_profile_too_late"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"R9L11_C29_012330_MODULE_AS_VALUEUP_STAGE2","trigger_id":"T_R9L11_012330_STAGE2","symbol":"012330","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE","raw_component_scores_before":{"contract_score":"unknown_or_not_supported","backlog_visibility_score":"unknown_or_not_supported","margin_bridge_score":13,"revision_score":11,"relative_strength_score":13,"customer_quality_score":12,"policy_or_regulatory_score":"unknown_or_not_supported","valuation_repricing_score":14,"execution_risk_score":-1,"legal_or_contract_risk_score":"unknown_or_not_supported","dilution_cb_risk_score":"unknown_or_not_supported","accounting_trust_risk_score":"unknown_or_not_supported"},"weighted_score_before":78,"stage_label_before":"Stage3-Yellow","raw_component_scores_after":{"contract_score":"unknown_or_not_supported","backlog_visibility_score":"unknown_or_not_supported","margin_bridge_score":15,"revision_score":12,"relative_strength_score":13,"customer_quality_score":12,"policy_or_regulatory_score":"unknown_or_not_supported","valuation_repricing_score":13,"execution_risk_score":-1,"legal_or_contract_risk_score":"unknown_or_not_supported","dilution_cb_risk_score":"unknown_or_not_supported","accounting_trust_risk_score":"unknown_or_not_supported"},"weighted_score_after":82,"stage_label_after":"Stage3-Yellow","changed_components":["margin_bridge_score","revision_score","execution_risk_score","valuation_repricing_score"],"component_delta_explanation":"C29 shadow profile rewards actual margin pass-through and penalizes headline volume without conversion into operating leverage.","MFE_90D_pct":33.33,"MAE_90D_pct":-0.49,"score_return_alignment_label":"positive_but_needs_non_volume_margin_bridge_tag","current_profile_verdict":"current_profile_correct"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"R9L11_C29_011210_ENGINE_PARTS_FALSE_STAGE2","trigger_id":"T_R9L11_011210_STAGE2","symbol":"011210","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE","raw_component_scores_before":{"contract_score":"unknown_or_not_supported","backlog_visibility_score":"unknown_or_not_supported","margin_bridge_score":8,"revision_score":8,"relative_strength_score":11,"customer_quality_score":9,"policy_or_regulatory_score":"unknown_or_not_supported","valuation_repricing_score":9,"execution_risk_score":-5,"legal_or_contract_risk_score":"unknown_or_not_supported","dilution_cb_risk_score":"unknown_or_not_supported","accounting_trust_risk_score":"unknown_or_not_supported"},"weighted_score_before":76,"stage_label_before":"Stage3-Yellow","raw_component_scores_after":{"contract_score":"unknown_or_not_supported","backlog_visibility_score":"unknown_or_not_supported","margin_bridge_score":6,"revision_score":7,"relative_strength_score":8,"customer_quality_score":8,"policy_or_regulatory_score":"unknown_or_not_supported","valuation_repricing_score":7,"execution_risk_score":-8,"legal_or_contract_risk_score":"unknown_or_not_supported","dilution_cb_risk_score":"unknown_or_not_supported","accounting_trust_risk_score":"unknown_or_not_supported"},"weighted_score_after":68,"stage_label_after":"Stage2-Actionable","changed_components":["margin_bridge_score","revision_score","execution_risk_score","valuation_repricing_score"],"component_delta_explanation":"C29 shadow profile rewards actual margin pass-through and penalizes headline volume without conversion into operating leverage.","MFE_90D_pct":15.52,"MAE_90D_pct":-6.03,"score_return_alignment_label":"failed_rerating_low_MFE_with_negative_retest","current_profile_verdict":"current_profile_false_positive"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"R9L11_C29_018880_THERMAL_EV_FALSE_STAGE2","trigger_id":"T_R9L11_018880_STAGE2","symbol":"018880","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE","raw_component_scores_before":{"contract_score":"unknown_or_not_supported","backlog_visibility_score":"unknown_or_not_supported","margin_bridge_score":7,"revision_score":8,"relative_strength_score":10,"customer_quality_score":11,"policy_or_regulatory_score":"unknown_or_not_supported","valuation_repricing_score":10,"execution_risk_score":-4,"legal_or_contract_risk_score":-2,"dilution_cb_risk_score":"unknown_or_not_supported","accounting_trust_risk_score":"unknown_or_not_supported"},"weighted_score_before":77,"stage_label_before":"Stage3-Yellow","raw_component_scores_after":{"contract_score":"unknown_or_not_supported","backlog_visibility_score":"unknown_or_not_supported","margin_bridge_score":4,"revision_score":5,"relative_strength_score":4,"customer_quality_score":9,"policy_or_regulatory_score":"unknown_or_not_supported","valuation_repricing_score":5,"execution_risk_score":-13,"legal_or_contract_risk_score":-4,"dilution_cb_risk_score":"unknown_or_not_supported","accounting_trust_risk_score":"unknown_or_not_supported"},"weighted_score_after":58,"stage_label_after":"Watch/Stage2-Blocked","changed_components":["margin_bridge_score","revision_score","execution_risk_score","valuation_repricing_score"],"component_delta_explanation":"C29 shadow profile rewards actual margin pass-through and penalizes headline volume without conversion into operating leverage.","MFE_90D_pct":4.95,"MAE_90D_pct":-25.7,"score_return_alignment_label":"false_positive_high_MAE_4C_needed","current_profile_verdict":"current_profile_false_positive"}
{"row_type":"residual_contribution","round":"R9","loop":"11","scheduled_round":"R9","scheduled_loop":11,"round_schedule_status":"valid","round_sector_consistency":"pass","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE","new_independent_case_count":4,"reused_case_count":0,"new_symbol_count":4,"same_archetype_new_symbol_count":4,"same_archetype_new_trigger_family_count":4,"new_trigger_family_count":4,"positive_case_count":2,"counterexample_count":2,"current_profile_error_count":3,"diversity_score_summary":"new_symbol +16, counterexample_gap +8, residual_error +15, wrong_round_penalty 0, duplicate penalties 0","tested_existing_calibrated_axes":["stage2_actionable_evidence_bonus","stage3_yellow_total_min","stage3_green_total_min","stage3_green_revision_min","price_only_blowoff_blocks_positive_stage","full_4b_requires_non_price_evidence","hard_4c_thesis_break_routes_to_4c"],"residual_error_types_found":["supplier_headline_volume_false_positive","green_too_late_after_true_margin_pass_through","4C_too_late_for_thermal_component_thesis_break"],"loop_contribution_label":"canonical_archetype_rule_candidate","do_not_propose_new_weight_delta":false}
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
completed_round = R9
completed_loop = 11
next_round = R10
next_loop = 11
round_schedule_status = valid
round_sector_consistency = pass
```

## 28. Source Notes

Stock-Web source notes:

```text
manifest = atlas/manifest.json
schema = atlas/schema.json
universe = atlas/universe/all_symbols.csv
price_basis = tradable_raw
price_adjustment_status = raw_unadjusted_marcap
manifest_max_date = 2026-02-20
```

Referenced stock-web paths:

```text
atlas/manifest.json
atlas/symbol_profiles/161/161390.json
atlas/symbol_profiles/012/012330.json
atlas/symbol_profiles/011/011210.json
atlas/symbol_profiles/018/018880.json
atlas/ohlcv_tradable_by_symbol_year/161/161390/2023.csv
atlas/ohlcv_tradable_by_symbol_year/161/161390/2024.csv
atlas/ohlcv_tradable_by_symbol_year/012/012330/2024.csv
atlas/ohlcv_tradable_by_symbol_year/011/011210/2024.csv
atlas/ohlcv_tradable_by_symbol_year/018/018880/2023.csv
atlas/ohlcv_tradable_by_symbol_year/018/018880/2024.csv
```
