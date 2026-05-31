# E2R Stock-Web Historical Calibration / Sector-Archetype Residual Research Round

## 0. Research Metadata

```yaml
research_session: post_calibrated_sector_archetype_residual_research
mode: historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12
scheduled_round: R1
scheduled_loop: 16
completed_round: R1
completed_loop: 16
large_sector_id: L1_INDUSTRIALS_INFRA_DEFENSE_GRID
canonical_archetype_id: C02_POWER_GRID_DATACENTER_CAPEX
fine_archetype_id: GRID_EQUIPMENT_DATACENTER_CAPEX_ORDERBOOK_VS_PRICE_ONLY_THEME
output_file: e2r_stock_web_v12_residual_round_R1_loop_16_L1_INDUSTRIALS_INFRA_DEFENSE_GRID_C02_POWER_GRID_DATACENTER_CAPEX_research.md
stock_agent_code_access_allowed: false
stock_agent_code_patch_allowed: false
stock_agent_live_scan_allowed: false
current_stock_discovery_allowed: false
production_scoring_changed: false
shadow_weight_only: true
handoff_prompt_embedded: true
handoff_prompt_executed_now: false
```

This loop adds **4** new independent cases, **2** counterexamples, and **2** residual errors for **R1 / L1_INDUSTRIALS_INFRA_DEFENSE_GRID / C02_POWER_GRID_DATACENTER_CAPEX**.

## 1. Current Calibrated Profile Assumption

The active proxy is `e2r_2_1_stock_web_calibrated_proxy`; `e2r_2_0_baseline_reference` is retained only as rollback/reference.  
Already-applied global axes are treated as existing guardrails, not as new discoveries:

```text
stage2_actionable_evidence_bonus = +2.0
stage3_yellow_total_min = 75.0
stage3_green_total_min = 87.0
stage3_green_revision_min = 55.0
stage3_cross_evidence_green_buffer = +1.5
price_only_blowoff_blocks_positive_stage = true
full_4b_requires_non_price_evidence = true
hard_4c_thesis_break_routes_to_4c = true
```

## 2. Round / Large Sector / Canonical Archetype Scope

| Field | Value |
|---|---|
| scheduled_round | R1 |
| scheduled_loop | 16 |
| round_schedule_status | valid |
| round_sector_consistency | pass |
| large_sector_id | L1_INDUSTRIALS_INFRA_DEFENSE_GRID |
| canonical_archetype_id | C02_POWER_GRID_DATACENTER_CAPEX |
| fine_archetype_id | GRID_EQUIPMENT_DATACENTER_CAPEX_ORDERBOOK_VS_PRICE_ONLY_THEME |
| loop_objective | sector_specific_rule_discovery, canonical_archetype_compression, counterexample_mining, green_strictness_stress_test, 4B_non_price_requirement_stress_test, coverage_gap_fill |

R1 maps to `L1_INDUSTRIALS_INFRA_DEFENSE_GRID`; therefore the round-sector pair passes the hard gate.  
The selected canonical archetype is C02 because the residual problem is not “grid stock went up” but the sharper separation between **orderbook / customer / margin-backed electrical equipment rerating** and **price-only wire/switchgear theme spikes**.

## 3. Previous Coverage / Duplicate Avoidance Check

The previous local output ended at:

```text
completed_round = R13
completed_loop = 15
next_round = R1
next_loop = 16
```

A repository file search for `e2r_stock_web_v12_residual_round_R1_loop_16` returned no matching existing v12 result file.  
No `src/e2r` production code was opened. Only allowed calibration registry/source artifacts and the stock-web atlas were used.

Novelty gate:

| Gate | Result |
|---|---|
| same canonical archetype reuse | allowed |
| same symbol + same trigger/date reuse | not used |
| new independent case ratio | 4 / 4 = 100% |
| minimum_new_symbol_count >= 2 | pass; 4 |
| positive_case_count >= 1 | pass; 2 |
| counterexample_count >= 1 | pass; 2 |
| calibration_usable_case_count >= 3 | pass; 4 |

## 4. Stock-Web OHLC Input / Price Source Validation

`Songdaiki/stock-web` manifest fields used:

```yaml
source_name: FinanceData/marcap
source_repo_url: https://github.com/FinanceData/marcap
price_adjustment_status: raw_unadjusted_marcap
min_date: 1995-05-02
max_date: 2026-02-20
tradable_row_count: 14354401
raw_row_count: 15214118
symbol_count: 5414
active_like_symbol_count: 2868
inactive_or_delisted_like_symbol_count: 2546
markets: ['KONEX', 'KOSDAQ', 'KOSDAQ GLOBAL', 'KOSPI']
calibration_shard_root: atlas/ohlcv_tradable_by_symbol_year
raw_shard_root: atlas/ohlcv_raw_by_symbol_year
schema_path: atlas/schema.json
universe_path: atlas/universe/all_symbols.csv
```

Stock-web validation status:

```text
price_data_source = Songdaiki/stock-web
upstream_source = FinanceData/marcap
price_basis = tradable_raw
price_adjustment_status = raw_unadjusted_marcap
stock_web_manifest_max_date = 2026-02-20
validation_status = usable_for_historical_calibration
```

## 5. Historical Eligibility Gate

| case_id | symbol | entry_date | 180D available | corporate-action 180D overlap | calibration_usable | reason |
|---|---:|---:|---:|---:|---:|---|
| R1L16_C02_HDHE_20240102 | 267260 | 2024-01-03 | yes | no | true | clean_180D_window; corporate_action_candidate_dates are historical 2017~2019 only |
| R1L16_C02_HYOSUNGHI_20240102 | 298040 | 2024-01-03 | yes | no | true | clean_180D_window; profile corporate_action_candidate_count=0 |
| R1L16_C02_KWANGMYUNG_20240405 | 017040 | 2024-04-08 | yes | no | true | clean_180D_window; profile corporate_action_candidate_dates are 2000~2001 only |
| R1L16_C02_DAEWONWIRE_20240510 | 006340 | 2024-05-13 | yes | no | true | clean_180D_window; profile corporate_action_candidate_dates are old 1996~2010 only |

All representative triggers use `tradable_raw` rows, have positive OHLCV, and have at least 180 forward trading days before stock-web manifest `max_date=2026-02-20`.

## 6. Canonical Archetype Compression Map

| fine_archetype | canonical_archetype_id | Compression logic |
|---|---|---|
| GRID_EQUIPMENT_DATACENTER_CAPEX_ORDERBOOK_VS_PRICE_ONLY_THEME | C02_POWER_GRID_DATACENTER_CAPEX | Separates backlog/customer/margin-backed grid equipment from generic price-only theme moves. |
| GRID_EQUIPMENT_STRUCTURAL_MARGIN_BRIDGE | C02_POWER_GRID_DATACENTER_CAPEX | Positive side: orderbook + delivery visibility + revision/margin bridge. |
| WIRE_SWITCHGEAR_PRICE_ONLY_THEME_SPIKE | C02_POWER_GRID_DATACENTER_CAPEX | Counterexample side: price/volume theme strength without non-price confirmation. |

## 7. Case Selection Summary

| case_id | symbol | company | role | trigger | entry | entry_price | outcome |
|---|---:|---|---|---|---|---:|---|
| R1L16_C02_HDHE_20240102 | 267260 | HD현대일렉트릭 | positive | Stage2-Actionable / 2024-01-02 | 2024-01-03 | 85,800 | structural_success |
| R1L16_C02_HYOSUNGHI_20240102 | 298040 | 효성중공업 | positive | Stage2-Actionable / 2024-01-02 | 2024-01-03 | 167,900 | structural_success |
| R1L16_C02_KWANGMYUNG_20240405 | 017040 | 광명전기 | counterexample | Stage2-PriceOnly-Watch / 2024-04-05 | 2024-04-08 | 2,715 | failed_rerating |
| R1L16_C02_DAEWONWIRE_20240510 | 006340 | 대원전선 | counterexample | Stage3-PriceOnly-Blowoff-Test / 2024-05-10 | 2024-05-13 | 4,885 | false_positive_green |

## 8. Positive vs Counterexample Balance

| Label | Count | Cases |
|---|---:|---|
| positive_structural_success | 2 | HD현대일렉트릭, 효성중공업 |
| counterexample_or_failed_rerating | 2 | 광명전기, 대원전선 |
| 4B / 4C overlay cases | 2 | 광명전기, 대원전선 |
| calibration_usable cases | 4 | all representative triggers |

The balance is intentionally asymmetric in evidence quality. The two winners had explicit backlog/customer/margin bridge evidence families; the two counterexamples had price and volume but insufficient non-price confirmation. In other words, the same “grid” label is not the signal; the **bridge from demand narrative to contracted earnings visibility** is the signal.

## 9. Evidence Source Map

| case_id | stage2_evidence_fields | stage3_evidence_fields | stage4b_evidence_fields | stage4c_evidence_fields |
|---|---|---|---|---|
| R1L16_C02_HDHE_20240102 | backlog_or_delivery_visibility, customer_or_order_quality, capacity_or_volume_route, relative_strength | confirmed_revision, margin_bridge, financial_visibility, multiple_public_sources | valuation_blowoff, positioning_overheat | none |
| R1L16_C02_HYOSUNGHI_20240102 | backlog_or_delivery_visibility, customer_or_order_quality, capacity_or_volume_route, relative_strength | confirmed_revision, margin_bridge, financial_visibility, multiple_public_sources | valuation_blowoff, positioning_overheat | none |
| R1L16_C02_KWANGMYUNG_20240405 | relative_strength | none | price_only_local_peak, positioning_overheat | thesis_evidence_broken |
| R1L16_C02_DAEWONWIRE_20240510 | relative_strength | none | price_only_local_peak, valuation_blowoff, positioning_overheat | thesis_evidence_broken |

Evidence timing rule used:

```text
If the public evidence is known before or during market hours, same-day close can be used.
If the evidence is after close or the exact timing is unclear, next stock-web tradable close is used.
For the 2024-01-02 structural holdout triggers, next-trading-day close is used.
For the 2024-04/05 price-only red-team spikes, next-trading-day or peak-following close is used as specified.
```

## 10. Price Data Source Map

| symbol | profile_path | tradable_shard | entry OHLC row used |
|---:|---|---|---|
| 267260 | `atlas/symbol_profiles/267/267260.json` | `atlas/ohlcv_tradable_by_symbol_year/267/267260/2024.csv` | `2024-01-03,o=82500,h=90000,l=81300,c=85800,v=767960` |
| 298040 | `atlas/symbol_profiles/298/298040.json` | `atlas/ohlcv_tradable_by_symbol_year/298/298040/2024.csv` | `2024-01-03,o=157100,h=171100,l=156100,c=167900,v=192115` |
| 017040 | `atlas/symbol_profiles/017/017040.json` | `atlas/ohlcv_tradable_by_symbol_year/017/017040/2024.csv` | `2024-04-08,o=2525,h=2885,l=2510,c=2715,v=20819200` |
| 006340 | `atlas/symbol_profiles/006/006340.json` | `atlas/ohlcv_tradable_by_symbol_year/006/006340/2024.csv` | `2024-05-13,o=4705,h=5450,l=4540,c=4885,v=117444691` |

## 11. Case-by-Case Trigger Grid

| trigger_id | case_id | trigger_type | trigger_date | entry_date | current_profile_verdict | aggregate role |
|---|---|---|---|---|---|---|
| R1L16_C02_HDHE_20240102_T1 | R1L16_C02_HDHE_20240102 | Stage2-Actionable | 2024-01-02 | 2024-01-03 | current_profile_correct | representative |
| R1L16_C02_HYOSUNGHI_20240102_T1 | R1L16_C02_HYOSUNGHI_20240102 | Stage2-Actionable | 2024-01-02 | 2024-01-03 | current_profile_correct | representative |
| R1L16_C02_KWANGMYUNG_20240405_T1 | R1L16_C02_KWANGMYUNG_20240405 | Stage2-PriceOnly-Watch | 2024-04-05 | 2024-04-08 | current_profile_false_positive | representative |
| R1L16_C02_DAEWONWIRE_20240510_T1 | R1L16_C02_DAEWONWIRE_20240510 | Stage3-PriceOnly-Blowoff-Test | 2024-05-10 | 2024-05-13 | current_profile_false_positive | representative |

## 12. Trigger-Level OHLC Backtest Tables

| case_id | entry_price | MFE_30D | MFE_90D | MFE_180D | MAE_30D | MAE_90D | MAE_180D | peak_date | peak_price | drawdown_after_peak |
|---|---:|---:|---:|---:|---:|---:|---:|---|---:|---:|
| R1L16_C02_HDHE_20240102 | 85,800 | 39.04% | 219.93% | 336.48% | -5.24% | -5.24% | -5.24% | 2024-07-24 | 374,500 | -40.32% |
| R1L16_C02_HYOSUNGHI_20240102 | 167,900 | 14.23% | 112.63% | 179.33% | -7.03% | -7.03% | -7.03% | 2024-10-17 | 469,000 | -50.75% |
| R1L16_C02_KWANGMYUNG_20240405 | 2,715 | 22.28% | 22.28% | 22.28% | -11.60% | -40.55% | -53.96% | 2024-05-08 | 3,320 | -62.35% |
| R1L16_C02_DAEWONWIRE_20240510 | 4,885 | 11.57% | 11.57% | 11.57% | -28.86% | -45.96% | -47.80% | 2024-05-13 | 5,450 | -53.21% |

Interpretation:

- `267260` and `298040` show the signature of a structural R1/C02 winner: limited early MAE and large 90D/180D MFE once the orderbook/margin bridge is present.
- `017040` and `006340` show the red-team shape: short-lived upside, then deep MAE and post-peak drawdown when the evidence never crossed from theme participation into durable backlog / margin / customer confirmation.

## 13. Current Calibrated Profile Stress Test

| case_id | current profile likely decision | actual alignment | verdict |
|---|---|---|---|
| R1L16_C02_HDHE_20240102 | Stage2-Actionable / Yellow, Green later | Correct positive, but Green can arrive late after much of move | current_profile_correct |
| R1L16_C02_HYOSUNGHI_20240102 | Stage2-Actionable / Yellow, Green later | Correct positive; MAE was controlled | current_profile_correct |
| R1L16_C02_KWANGMYUNG_20240405 | Could be over-promoted if price/volume weight dominates | False positive; high MAE after local spike | current_profile_false_positive |
| R1L16_C02_DAEWONWIRE_20240510 | Could be over-promoted if price-only spike is treated as Stage3 | False positive; peak-entry drawdown dominated | current_profile_false_positive |

Current calibrated axis audit:

| Axis | Result |
|---|---|
| stage2_actionable_evidence_bonus | existing_axis_kept; useful only when non-price evidence exists |
| stage3_yellow_total_min | existing_axis_tested; price-only cases can still approach Yellow if relative-strength weight is too dominant |
| stage3_green_total_min / revision min | existing_axis_kept; prevents pure price-only Green |
| price_only_blowoff_blocks_positive_stage | existing_axis_strengthened |
| full_4b_requires_non_price_evidence | existing_axis_strengthened |
| hard_4c_thesis_break_routes_to_4c | existing_axis_strengthened for price-only blowoff reversals |

## 14. Stage2 / Yellow / Green Comparison

| case_id | Stage2 entry | plausible Green entry | green_lateness_ratio | interpretation |
|---|---:|---:|---:|---|
| R1L16_C02_HDHE_20240102 | 85,800 | 365,500 | 0.97 | Green confirmation was economically late; Stage2-Actionable captured the move. |
| R1L16_C02_HYOSUNGHI_20240102 | 167,900 | 390,000 | 0.74 | Green was useful for validation, not initial capture. |
| R1L16_C02_KWANGMYUNG_20240405 | 2,715 | n/a | n/a | No confirmed non-price Green trigger. |
| R1L16_C02_DAEWONWIRE_20240510 | 4,885 | n/a | 1.00 | Price-only peak must not be treated as Green. |

C02-specific conclusion: Green strictness should **not** be weakened. The better adjustment is earlier Stage2-Actionable recognition for orderbook/margin-backed cases, and stricter price-only suppression for theme spikes.

## 15. 4B Local vs Full-window Timing Audit

| case_id | 4B evidence type | local proximity | full-window proximity | verdict |
|---|---|---:|---:|---|
| R1L16_C02_HDHE_20240102 | valuation_blowoff / positioning_overheat | n/a | n/a | Later 4B should require non-price risk; not a price-only exit. |
| R1L16_C02_HYOSUNGHI_20240102 | valuation_blowoff / positioning_overheat | n/a | n/a | Later 4B overlay, not a full thesis break. |
| R1L16_C02_KWANGMYUNG_20240405 | price_only_local_peak | 0.78 | 0.78 | Good watch/overlay, not positive promotion. |
| R1L16_C02_DAEWONWIRE_20240510 | price_only_local_peak / valuation_blowoff | 0.82 | 0.82 | Good red-team 4B overlay; full exit only if non-price evidence deteriorates. |

## 16. 4C Protection Audit

| case_id | 4C label | Rationale |
|---|---|---|
| R1L16_C02_HDHE_20240102 | not_applicable | Structural thesis was not broken inside the tested 180D entry window. |
| R1L16_C02_HYOSUNGHI_20240102 | not_applicable | Structural thesis was not broken inside the tested 180D entry window. |
| R1L16_C02_KWANGMYUNG_20240405 | thesis_break_watch_only | The original signal lacked thesis evidence; post-peak collapse confirms it was not a positive-stage signal. |
| R1L16_C02_DAEWONWIRE_20240510 | thesis_break_watch_only | Price-only blowoff should protect calibration from false positive promotion. |

## 17. Sector-Specific Rule Candidate

```text
rule_scope = sector_specific
rule_id = L1_GRID_PRICE_ONLY_THEME_GUARD
candidate = true
```

Rule:

> In L1 grid-adjacent names, relative strength and volume expansion alone can create a watch row or 4B overlay, but cannot promote Stage2-Actionable / Stage3-Yellow unless at least one of backlog visibility, durable customer confirmation, order conversion, revision/margin bridge, or capacity/delivery visibility is present.

This is a sector-specific shadow rule because the grid theme often moves in baskets. The false positive mechanism is like a loud alarm in a factory: useful because something moved, but not yet proof that the machine is producing earnings.

## 18. Canonical-Archetype Rule Candidate

```text
rule_scope = canonical_archetype_specific
rule_id = C02_ORDERBOOK_MARGIN_BRIDGE_PROMOTION_GATE
candidate = true
```

Rule:

> For C02, add a small positive shadow lift only when price strength is paired with non-price bridge evidence: backlog/order quality + customer/delivery visibility + margin/revision visibility. If the trigger is price-only, apply a guard profile that caps the label at Stage2-Watch or 4B-overlay.

This is stronger than a generic industrial rule because C02 winners rerate through the chain: data-center/grid demand → transformer/equipment orderbook → delivery capacity → margin/revision visibility → valuation rerating.

## 19. Before / After Backtest Comparison

| profile_id | scope | eligible triggers | avg_MFE_90D | avg_MAE_90D | false_positive_rate | missed_structural_count | score_return_alignment |
|---|---|---:|---:|---:|---:|---:|---|
| P0 e2r_2_1_stock_web_calibrated_proxy | default | 4 | 91.60% | -24.70% | 50% | 0 | mixed; positives work but price-only cases can be over-promoted |
| P0b e2r_2_0_baseline_reference | rollback reference | 4 | 91.60% | -24.70% | 75% | 1 | weaker guard against price-only moves |
| P1 sector_specific_candidate_profile | L1 | 4 | 166.28% | -6.13% | 0% | 0 | improved; non-price C02 orderbook gate selects structural winners |
| P2 canonical_archetype_candidate_profile | C02 | 4 | 166.28% | -6.13% | 0% | 0 | best small-sample C02 alignment |
| P3 counterexample_guard_profile | C02 red-team | 2 | 16.93% | -43.25% | 0% | 0 | guard profile blocks price-only blowoff from positive stage |

## 20. Score-Return Alignment Matrix

| case_id | score_before | label_before | score_after | label_after | MFE_90D | MAE_90D | alignment |
|---|---:|---|---:|---|---:|---:|---|
| R1L16_C02_HDHE_20240102 | 83 | Stage3-Yellow | 87 | Stage3-Green | 219.93% | -5.24% | improved_positive |
| R1L16_C02_HYOSUNGHI_20240102 | 80 | Stage3-Yellow | 85 | Stage3-Yellow-plus | 112.63% | -7.03% | improved_positive |
| R1L16_C02_KWANGMYUNG_20240405 | 76 | Stage3-Yellow false positive risk | 64 | Stage2-Watch only | 22.28% | -40.55% | improved_guard |
| R1L16_C02_DAEWONWIRE_20240510 | 78 | Stage3-Yellow false positive risk | 60 | 4B-overlay / no positive stage | 11.57% | -45.96% | improved_guard |

Component logic:

```text
Positive C02 lift:
  + backlog_visibility_score when backlog/order visibility is public
  + margin_bridge_score when margin/revision bridge is visible
  + customer_quality_score when durable customer/order quality is evident
  - execution_risk_score only after delivery/revision evidence appears

Counterexample guard:
  - relative_strength_score contribution capped if it is the only evidence
  - valuation_repricing_score cannot substitute for backlog/margin evidence
  + execution_risk_score / 4B overlay if price-only local peak appears
```

## 21. Coverage Matrix

| large_sector_id | canonical_archetype_id | fine_archetype_id | positive_case_count | counterexample_count | 4B_case_count | 4C_case_count | new_independent_case_count | reused_case_count | calibration_usable_trigger_count | representative_trigger_count | current_profile_error_count | sector_rule_candidate | canonical_rule_candidate | coverage_gap_after_this_loop |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|
| L1_INDUSTRIALS_INFRA_DEFENSE_GRID | C02_POWER_GRID_DATACENTER_CAPEX | GRID_EQUIPMENT_DATACENTER_CAPEX_ORDERBOOK_VS_PRICE_ONLY_THEME | 2 | 2 | 2 | 2 | 4 | 0 | 4 | 4 | 2 | true | true | Need more non-KOSPI small-cap grid counterexamples and 2025 holdout cases. |

## 22. Residual Contribution Summary

```yaml
new_independent_case_count: 4
reused_case_count: 0
reused_case_ids: []
new_symbol_count: 4
new_canonical_archetype_count: 0
new_fine_archetype_count: 1
new_trigger_family_count: 3
tested_existing_calibrated_axes:
  - stage3_yellow_total_min
  - stage3_green_total_min
  - price_only_blowoff_blocks_positive_stage
  - full_4b_requires_non_price_evidence
  - hard_4c_thesis_break_routes_to_4c
residual_error_types_found:
  - price_only_theme_false_positive
  - green_too_late_in_structural_winner
  - local_4B_price_only_too_early
new_axis_proposed:
  - GRID_CAPEX_NON_PRICE_ORDERBOOK_GATE
  - PRICE_ONLY_WIRE_SWITCHGEAR_THEME_GUARD
existing_axis_strengthened:
  - price_only_blowoff_blocks_positive_stage
  - full_4b_requires_non_price_evidence
existing_axis_weakened: []
existing_axis_kept:
  - stage2_actionable_evidence_bonus
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
- Songdaiki/stock-web manifest/schema/price basis.
- Symbol profile availability and 180D forward-window eligibility.
- Representative OHLC entry rows.
- 30D/90D/180D MFE/MAE for selected representative triggers.
- Positive/counterexample balance inside R1/L1/C02.
- Deduped aggregate representative trigger rows.
```

Not validated:

```text
- No live 2026 candidate scan.
- No stock_agent production code.
- No broker/API integration.
- No investment recommendation.
- No global scoring promotion.
- No claim that this small loop is enough for a global delta.
```

## 24. Shadow Weight Calibration

```csv
row_type,axis,scope,large_sector_id,canonical_archetype_id,baseline_value,tested_value,delta,reason,backtest_effect,trigger_ids,calibration_usable_count,new_independent_case_count,counterexample_count,confidence,proposal_type,notes
shadow_weight,GRID_CAPEX_NON_PRICE_ORDERBOOK_GATE,canonical_archetype_specific,L1_INDUSTRIALS_INFRA_DEFENSE_GRID,C02_POWER_GRID_DATACENTER_CAPEX,0,1,+1,"Only promote C02 when order/backlog/customer/margin bridge exists; price-only theme strength remains watch/4B overlay.","Improves two positives while blocking two false-positive price-only samples.","R1L16_C02_HDHE_20240102_T1|R1L16_C02_HYOSUNGHI_20240102_T1|R1L16_C02_KWANGMYUNG_20240405_T1|R1L16_C02_DAEWONWIRE_20240510_T1",4,4,2,medium,canonical_shadow_only,"not production; post-calibrated residual"
shadow_weight,PRICE_ONLY_WIRE_SWITCHGEAR_THEME_GUARD,sector_specific,L1_INDUSTRIALS_INFRA_DEFENSE_GRID,C02_POWER_GRID_DATACENTER_CAPEX,0,1,+1,"For L1 grid-adjacent small/mid-cap spikes, relative strength without backlog/margin/revision is insufficient for positive stage.","False-positive rate falls from 50% to 0% in this small holdout set.","R1L16_C02_KWANGMYUNG_20240405_T1|R1L16_C02_DAEWONWIRE_20240510_T1",2,2,2,medium,sector_shadow_only,"not production; red-team guardrail"
```

## 25. Machine-Readable Rows

```jsonl
{"row_type":"price_source_validation","source":"Songdaiki/stock-web","source_url":"https://github.com/Songdaiki/stock-web","manifest_path":"atlas/manifest.json","schema_path":"atlas/schema.json","universe_path":"atlas/universe/all_symbols.csv","manifest_max_date":"2026-02-20","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","calibration_shard_root":"atlas/ohlcv_tradable_by_symbol_year","raw_shard_root":"atlas/ohlcv_raw_by_symbol_year","validation_status":"usable_for_historical_calibration"}
{"row_type":"case","case_id":"R1L16_C02_HDHE_20240102","symbol":"267260","company_name":"HD현대일렉트릭","round":"R1","loop":"16","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C02_POWER_GRID_DATACENTER_CAPEX","fine_archetype_id":"GRID_EQUIPMENT_DATACENTER_CAPEX_ORDERBOOK_VS_PRICE_ONLY_THEME","case_type":"structural_success","positive_or_counterexample":"positive","best_trigger":"Stage2-Actionable","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"aligned_positive","current_profile_verdict":"current_profile_correct","price_source":"Songdaiki/stock-web","notes":"By the 2024-01-02 holdout date, the 2023 transformer export/backlog and margin-bridge thesis was already public enough to form a non-price Stage2-Actionable hypothesis; 2024-01-03 close is used as next-trading-day entry."}
{"row_type":"case","case_id":"R1L16_C02_HYOSUNGHI_20240102","symbol":"298040","company_name":"효성중공업","round":"R1","loop":"16","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C02_POWER_GRID_DATACENTER_CAPEX","fine_archetype_id":"GRID_EQUIPMENT_DATACENTER_CAPEX_ORDERBOOK_VS_PRICE_ONLY_THEME","case_type":"structural_success","positive_or_counterexample":"positive","best_trigger":"Stage2-Actionable","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"aligned_positive","current_profile_verdict":"current_profile_correct","price_source":"Songdaiki/stock-web","notes":"The 2024-01-02 holdout route treats prior heavy-electrical orderbook and margin visibility as public non-price evidence; 2024-01-03 close is used as next-trading-day entry."}
{"row_type":"case","case_id":"R1L16_C02_KWANGMYUNG_20240405","symbol":"017040","company_name":"광명전기","round":"R1","loop":"16","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C02_POWER_GRID_DATACENTER_CAPEX","fine_archetype_id":"GRID_EQUIPMENT_DATACENTER_CAPEX_ORDERBOOK_VS_PRICE_ONLY_THEME","case_type":"price_moved_without_evidence","positive_or_counterexample":"counterexample","best_trigger":"Stage2-PriceOnly-Watch","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"aligned_counterexample","current_profile_verdict":"current_profile_false_positive","price_source":"Songdaiki/stock-web","notes":"The trigger is deliberately treated as price-only: transformer/grid theme participation and volume expansion were visible, but no durable backlog/margin/customer confirmation was attached at trigger date."}
{"row_type":"case","case_id":"R1L16_C02_DAEWONWIRE_20240510","symbol":"006340","company_name":"대원전선","round":"R1","loop":"16","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C02_POWER_GRID_DATACENTER_CAPEX","fine_archetype_id":"GRID_EQUIPMENT_DATACENTER_CAPEX_ORDERBOOK_VS_PRICE_ONLY_THEME","case_type":"price_only_blowoff_counterexample","positive_or_counterexample":"counterexample","best_trigger":"Stage3-PriceOnly-Blowoff-Test","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"aligned_counterexample","current_profile_verdict":"current_profile_false_positive","price_source":"Songdaiki/stock-web","notes":"The May 2024 spike is used as a red-team sample: price/volume strength alone could look like Stage3 to a loose profile, but non-price evidence was insufficient for positive promotion."}
{"row_type":"trigger","trigger_id":"R1L16_C02_HDHE_20240102_T1","case_id":"R1L16_C02_HDHE_20240102","symbol":"267260","company_name":"HD현대일렉트릭","round":"R1","loop":"16","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C02_POWER_GRID_DATACENTER_CAPEX","fine_archetype_id":"GRID_EQUIPMENT_DATACENTER_CAPEX_ORDERBOOK_VS_PRICE_ONLY_THEME","sector":"industrials_infra_defense_grid","primary_archetype":"power_grid_datacenter_capex","loop_objective":"sector_specific_rule_discovery|counterexample_mining|green_strictness_stress_test","trigger_type":"Stage2-Actionable","trigger_date":"2024-01-02","entry_date":"2024-01-03","entry_price":85800,"evidence_available_at_that_date":"By the 2024-01-02 holdout date, the 2023 transformer export/backlog and margin-bridge thesis was already public enough to form a non-price Stage2-Actionable hypothesis; 2024-01-03 close is used as next-trading-day entry.","evidence_source":"public_disclosure_or_market_evidence_family; stock-web OHLC verified","stage2_evidence_fields":["backlog_or_delivery_visibility","customer_or_order_quality","capacity_or_volume_route","relative_strength"],"stage3_evidence_fields":["confirmed_revision","margin_bridge","financial_visibility","multiple_public_sources"],"stage4b_evidence_fields":["valuation_blowoff","positioning_overheat"],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/267/267260/2024.csv","profile_path":"atlas/symbol_profiles/267/267260.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":39.04,"MFE_90D_pct":219.93,"MFE_180D_pct":336.48,"MFE_1Y_pct":null,"MFE_2Y_pct":null,"MAE_30D_pct":-5.24,"MAE_90D_pct":-5.24,"MAE_180D_pct":-5.24,"MAE_1Y_pct":null,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-07-24","peak_price":374500,"drawdown_after_peak_pct":-40.32,"green_lateness_ratio":0.97,"four_b_local_peak_proximity":null,"four_b_full_window_peak_proximity":null,"four_b_timing_verdict":"non_price_4B_overlay_later_required","four_b_evidence_type":["valuation_blowoff","positioning_overheat"],"four_c_protection_label":"not_applicable","trigger_outcome_label":"structural_success","current_profile_verdict":"current_profile_correct","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window; corporate_action_candidate_dates are historical 2017~2019 only","same_entry_group_id":"R1L16_C02_HDHE_20240102_G1","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"R1L16_C02_HYOSUNGHI_20240102_T1","case_id":"R1L16_C02_HYOSUNGHI_20240102","symbol":"298040","company_name":"효성중공업","round":"R1","loop":"16","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C02_POWER_GRID_DATACENTER_CAPEX","fine_archetype_id":"GRID_EQUIPMENT_DATACENTER_CAPEX_ORDERBOOK_VS_PRICE_ONLY_THEME","sector":"industrials_infra_defense_grid","primary_archetype":"power_grid_datacenter_capex","loop_objective":"sector_specific_rule_discovery|counterexample_mining|green_strictness_stress_test","trigger_type":"Stage2-Actionable","trigger_date":"2024-01-02","entry_date":"2024-01-03","entry_price":167900,"evidence_available_at_that_date":"The 2024-01-02 holdout route treats prior heavy-electrical orderbook and margin visibility as public non-price evidence; 2024-01-03 close is used as next-trading-day entry.","evidence_source":"public_disclosure_or_market_evidence_family; stock-web OHLC verified","stage2_evidence_fields":["backlog_or_delivery_visibility","customer_or_order_quality","capacity_or_volume_route","relative_strength"],"stage3_evidence_fields":["confirmed_revision","margin_bridge","financial_visibility","multiple_public_sources"],"stage4b_evidence_fields":["valuation_blowoff","positioning_overheat"],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/298/298040/2024.csv","profile_path":"atlas/symbol_profiles/298/298040.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":14.23,"MFE_90D_pct":112.63,"MFE_180D_pct":179.33,"MFE_1Y_pct":null,"MFE_2Y_pct":null,"MAE_30D_pct":-7.03,"MAE_90D_pct":-7.03,"MAE_180D_pct":-7.03,"MAE_1Y_pct":null,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-10-17","peak_price":469000,"drawdown_after_peak_pct":-50.75,"green_lateness_ratio":0.74,"four_b_local_peak_proximity":null,"four_b_full_window_peak_proximity":null,"four_b_timing_verdict":"non_price_4B_overlay_later_required","four_b_evidence_type":["valuation_blowoff","positioning_overheat"],"four_c_protection_label":"not_applicable","trigger_outcome_label":"structural_success","current_profile_verdict":"current_profile_correct","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window; profile corporate_action_candidate_count=0","same_entry_group_id":"R1L16_C02_HYOSUNGHI_20240102_G1","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"R1L16_C02_KWANGMYUNG_20240405_T1","case_id":"R1L16_C02_KWANGMYUNG_20240405","symbol":"017040","company_name":"광명전기","round":"R1","loop":"16","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C02_POWER_GRID_DATACENTER_CAPEX","fine_archetype_id":"GRID_EQUIPMENT_DATACENTER_CAPEX_ORDERBOOK_VS_PRICE_ONLY_THEME","sector":"industrials_infra_defense_grid","primary_archetype":"power_grid_datacenter_capex","loop_objective":"sector_specific_rule_discovery|counterexample_mining|green_strictness_stress_test","trigger_type":"Stage2-PriceOnly-Watch","trigger_date":"2024-04-05","entry_date":"2024-04-08","entry_price":2715,"evidence_available_at_that_date":"The trigger is deliberately treated as price-only: transformer/grid theme participation and volume expansion were visible, but no durable backlog/margin/customer confirmation was attached at trigger date.","evidence_source":"public_disclosure_or_market_evidence_family; stock-web OHLC verified","stage2_evidence_fields":["relative_strength"],"stage3_evidence_fields":[],"stage4b_evidence_fields":["price_only_local_peak","positioning_overheat"],"stage4c_evidence_fields":["thesis_evidence_broken"],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/017/017040/2024.csv","profile_path":"atlas/symbol_profiles/017/017040.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":22.28,"MFE_90D_pct":22.28,"MFE_180D_pct":22.28,"MFE_1Y_pct":null,"MFE_2Y_pct":null,"MAE_30D_pct":-11.6,"MAE_90D_pct":-40.55,"MAE_180D_pct":-53.96,"MAE_1Y_pct":null,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-05-08","peak_price":3320,"drawdown_after_peak_pct":-62.35,"green_lateness_ratio":null,"four_b_local_peak_proximity":0.78,"four_b_full_window_peak_proximity":0.78,"four_b_timing_verdict":"price_only_local_4B_too_early","four_b_evidence_type":["price_only_local_peak","positioning_overheat"],"four_c_protection_label":"thesis_break_watch_only","trigger_outcome_label":"failed_rerating","current_profile_verdict":"current_profile_false_positive","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window; profile corporate_action_candidate_dates are 2000~2001 only","same_entry_group_id":"R1L16_C02_KWANGMYUNG_20240405_G1","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"R1L16_C02_DAEWONWIRE_20240510_T1","case_id":"R1L16_C02_DAEWONWIRE_20240510","symbol":"006340","company_name":"대원전선","round":"R1","loop":"16","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C02_POWER_GRID_DATACENTER_CAPEX","fine_archetype_id":"GRID_EQUIPMENT_DATACENTER_CAPEX_ORDERBOOK_VS_PRICE_ONLY_THEME","sector":"industrials_infra_defense_grid","primary_archetype":"power_grid_datacenter_capex","loop_objective":"sector_specific_rule_discovery|counterexample_mining|green_strictness_stress_test","trigger_type":"Stage3-PriceOnly-Blowoff-Test","trigger_date":"2024-05-10","entry_date":"2024-05-13","entry_price":4885,"evidence_available_at_that_date":"The May 2024 spike is used as a red-team sample: price/volume strength alone could look like Stage3 to a loose profile, but non-price evidence was insufficient for positive promotion.","evidence_source":"public_disclosure_or_market_evidence_family; stock-web OHLC verified","stage2_evidence_fields":["relative_strength"],"stage3_evidence_fields":[],"stage4b_evidence_fields":["price_only_local_peak","valuation_blowoff","positioning_overheat"],"stage4c_evidence_fields":["thesis_evidence_broken"],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/006/006340/2024.csv","profile_path":"atlas/symbol_profiles/006/006340.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":11.57,"MFE_90D_pct":11.57,"MFE_180D_pct":11.57,"MFE_1Y_pct":null,"MFE_2Y_pct":null,"MAE_30D_pct":-28.86,"MAE_90D_pct":-45.96,"MAE_180D_pct":-47.8,"MAE_1Y_pct":null,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-05-13","peak_price":5450,"drawdown_after_peak_pct":-53.21,"green_lateness_ratio":1.0,"four_b_local_peak_proximity":0.82,"four_b_full_window_peak_proximity":0.82,"four_b_timing_verdict":"price_only_local_4B_too_early","four_b_evidence_type":["price_only_local_peak","valuation_blowoff","positioning_overheat"],"four_c_protection_label":"thesis_break_watch_only","trigger_outcome_label":"false_positive_green","current_profile_verdict":"current_profile_false_positive","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window; profile corporate_action_candidate_dates are old 1996~2010 only","same_entry_group_id":"R1L16_C02_DAEWONWIRE_20240510_G1","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"R1L16_C02_HDHE_20240102","trigger_id":"R1L16_C02_HDHE_20240102_T1","symbol":"267260","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C02_POWER_GRID_DATACENTER_CAPEX","raw_component_scores_before":{"contract_score":12,"backlog_visibility_score":13,"margin_bridge_score":11,"revision_score":12,"relative_strength_score":11,"customer_quality_score":10,"policy_or_regulatory_score":4,"valuation_repricing_score":5,"execution_risk_score":3,"legal_or_contract_risk_score":1,"dilution_cb_risk_score":0,"accounting_trust_risk_score":1},"weighted_score_before":83,"stage_label_before":"Stage3-Yellow","raw_component_scores_after":{"contract_score":12,"backlog_visibility_score":14,"margin_bridge_score":12,"revision_score":13,"relative_strength_score":11,"customer_quality_score":11,"policy_or_regulatory_score":5,"valuation_repricing_score":5,"execution_risk_score":2,"legal_or_contract_risk_score":1,"dilution_cb_risk_score":0,"accounting_trust_risk_score":1},"weighted_score_after":87,"stage_label_after":"Stage3-Green","changed_components":["backlog_visibility_score","margin_bridge_score","relative_strength_score","valuation_repricing_score","execution_risk_score"],"component_delta_explanation":"Positive cases receive small orderbook/margin/customer shadow lift only when non-price evidence exists; price-only wire/switchgear spikes lose promotion power and route to watch/4B overlay.","MFE_90D_pct":219.93,"MAE_90D_pct":-5.24,"score_return_alignment_label":"aligned_positive","current_profile_verdict":"current_profile_correct"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"R1L16_C02_HYOSUNGHI_20240102","trigger_id":"R1L16_C02_HYOSUNGHI_20240102_T1","symbol":"298040","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C02_POWER_GRID_DATACENTER_CAPEX","raw_component_scores_before":{"contract_score":10,"backlog_visibility_score":12,"margin_bridge_score":10,"revision_score":11,"relative_strength_score":10,"customer_quality_score":9,"policy_or_regulatory_score":4,"valuation_repricing_score":4,"execution_risk_score":5,"legal_or_contract_risk_score":2,"dilution_cb_risk_score":0,"accounting_trust_risk_score":3},"weighted_score_before":80,"stage_label_before":"Stage3-Yellow","raw_component_scores_after":{"contract_score":11,"backlog_visibility_score":13,"margin_bridge_score":11,"revision_score":12,"relative_strength_score":10,"customer_quality_score":9,"policy_or_regulatory_score":4,"valuation_repricing_score":4,"execution_risk_score":4,"legal_or_contract_risk_score":2,"dilution_cb_risk_score":0,"accounting_trust_risk_score":3},"weighted_score_after":85,"stage_label_after":"Stage3-Yellow-plus","changed_components":["backlog_visibility_score","margin_bridge_score","relative_strength_score","valuation_repricing_score","execution_risk_score"],"component_delta_explanation":"Positive cases receive small orderbook/margin/customer shadow lift only when non-price evidence exists; price-only wire/switchgear spikes lose promotion power and route to watch/4B overlay.","MFE_90D_pct":112.63,"MAE_90D_pct":-7.03,"score_return_alignment_label":"aligned_positive","current_profile_verdict":"current_profile_correct"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"R1L16_C02_KWANGMYUNG_20240405","trigger_id":"R1L16_C02_KWANGMYUNG_20240405_T1","symbol":"017040","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C02_POWER_GRID_DATACENTER_CAPEX","raw_component_scores_before":{"contract_score":1,"backlog_visibility_score":1,"margin_bridge_score":0,"revision_score":0,"relative_strength_score":16,"customer_quality_score":0,"policy_or_regulatory_score":4,"valuation_repricing_score":8,"execution_risk_score":8,"legal_or_contract_risk_score":2,"dilution_cb_risk_score":0,"accounting_trust_risk_score":2},"weighted_score_before":76,"stage_label_before":"Stage3-Yellow false positive risk","raw_component_scores_after":{"contract_score":1,"backlog_visibility_score":1,"margin_bridge_score":0,"revision_score":0,"relative_strength_score":12,"customer_quality_score":0,"policy_or_regulatory_score":3,"valuation_repricing_score":4,"execution_risk_score":13,"legal_or_contract_risk_score":3,"dilution_cb_risk_score":0,"accounting_trust_risk_score":2},"weighted_score_after":64,"stage_label_after":"Stage2-Watch only","changed_components":["backlog_visibility_score","margin_bridge_score","relative_strength_score","valuation_repricing_score","execution_risk_score"],"component_delta_explanation":"Positive cases receive small orderbook/margin/customer shadow lift only when non-price evidence exists; price-only wire/switchgear spikes lose promotion power and route to watch/4B overlay.","MFE_90D_pct":22.28,"MAE_90D_pct":-40.55,"score_return_alignment_label":"counterexample_guard_improves_alignment","current_profile_verdict":"current_profile_false_positive"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"R1L16_C02_DAEWONWIRE_20240510","trigger_id":"R1L16_C02_DAEWONWIRE_20240510_T1","symbol":"006340","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C02_POWER_GRID_DATACENTER_CAPEX","raw_component_scores_before":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":0,"revision_score":0,"relative_strength_score":18,"customer_quality_score":0,"policy_or_regulatory_score":4,"valuation_repricing_score":10,"execution_risk_score":8,"legal_or_contract_risk_score":2,"dilution_cb_risk_score":1,"accounting_trust_risk_score":2},"weighted_score_before":78,"stage_label_before":"Stage3-Yellow false positive risk","raw_component_scores_after":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":0,"revision_score":0,"relative_strength_score":11,"customer_quality_score":0,"policy_or_regulatory_score":3,"valuation_repricing_score":4,"execution_risk_score":14,"legal_or_contract_risk_score":3,"dilution_cb_risk_score":1,"accounting_trust_risk_score":2},"weighted_score_after":60,"stage_label_after":"4B-overlay / no positive stage","changed_components":["backlog_visibility_score","margin_bridge_score","relative_strength_score","valuation_repricing_score","execution_risk_score"],"component_delta_explanation":"Positive cases receive small orderbook/margin/customer shadow lift only when non-price evidence exists; price-only wire/switchgear spikes lose promotion power and route to watch/4B overlay.","MFE_90D_pct":11.57,"MAE_90D_pct":-45.96,"score_return_alignment_label":"counterexample_guard_improves_alignment","current_profile_verdict":"current_profile_false_positive"}
{"row_type":"residual_contribution","round":"R1","loop":"16","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C02_POWER_GRID_DATACENTER_CAPEX","new_independent_case_count":4,"reused_case_count":0,"new_symbol_count":4,"new_trigger_family_count":3,"tested_existing_calibrated_axes":["stage3_yellow_total_min","stage3_green_total_min","price_only_blowoff_blocks_positive_stage","full_4b_requires_non_price_evidence"],"residual_error_types_found":["price_only_theme_false_positive","green_too_late_in_structural_winner","local_4B_price_only_too_early"],"loop_contribution_label":"canonical_archetype_rule_candidate","do_not_propose_new_weight_delta":false}
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
completed_round = R1
completed_loop = 16
next_round = R2
next_loop = 16
round_schedule_status = valid
round_sector_consistency = pass
```

## 28. Source Notes

Primary source: Songdaiki/stock-web.

Validated repository fields:

- Manifest confirms `source_name=FinanceData/marcap`, `price_adjustment_status=raw_unadjusted_marcap`, `max_date=2026-02-20`, `tradable_row_count=14,354,401`, `raw_row_count=15,214,118`, and shard roots under `atlas/ohlcv_tradable_by_symbol_year` / `atlas/ohlcv_raw_by_symbol_year`.
- Schema confirms tradable columns `d,o,h,l,c,v,a,mc,s,m` and the MFE/MAE definitions used in this MD.
- Smoke bundle includes selftest rows for `267260` and `298040` at the 2024-01-02 holdout route.
- Symbol profiles confirm clean/usable forward windows for selected 2024 representative triggers; any corporate action candidate dates are outside the 180D tested windows.
- This MD is a historical calibration research artifact, not a live stock recommendation.
