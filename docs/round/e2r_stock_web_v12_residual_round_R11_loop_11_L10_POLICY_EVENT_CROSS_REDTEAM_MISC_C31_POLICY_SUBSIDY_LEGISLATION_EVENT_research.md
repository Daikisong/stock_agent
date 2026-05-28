# E2R Stock-Web Historical Calibration / Sector-Archetype Residual Research Round

## 0. Research Metadata

```yaml
research_session: post_calibrated_sector_archetype_residual_research
mode: historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12
output_file: e2r_stock_web_v12_residual_round_R11_loop_11_L10_POLICY_EVENT_CROSS_REDTEAM_MISC_C31_POLICY_SUBSIDY_LEGISLATION_EVENT_research.md
scheduled_round: R11
scheduled_loop: 11
completed_round: R11
completed_loop: 11
large_sector_id: L10_POLICY_EVENT_CROSS_REDTEAM_MISC
canonical_archetype_id: C31_POLICY_SUBSIDY_LEGISLATION_EVENT
fine_archetype_id: EAST_SEA_EXPLORATION_POLICY_EVENT_DIRECT_BENEFICIARY_MAP
production_scoring_changed: false
shadow_weight_only: true
stock_agent_code_access_allowed: false
stock_agent_code_patch_allowed: false
stock_agent_live_scan_allowed: false
current_stock_discovery_allowed: false
stock_web_price_atlas_access_required: true
handoff_prompt_embedded: true
handoff_prompt_executed_now: false
```

This loop adds 6 new independent cases, 4 counterexamples, and 4 residual errors for R11/L10_POLICY_EVENT_CROSS_REDTEAM_MISC/C31_POLICY_SUBSIDY_LEGISLATION_EVENT.

## 1. Current Calibrated Profile Assumption

The current proxy is `e2r_2_1_stock_web_calibrated_proxy`, not the older E2R 2.0 baseline. The already-applied global axes are treated as live assumptions: Stage2-Actionable evidence bonus, Yellow/Green thresholds, price-only blowoff block, non-price 4B requirement, and hard 4C thesis-break routing. This MD does not re-prove those axes. It stress-tests a residual problem inside C31: a broad policy headline can be real non-price evidence at the country level while still being weak or false company-specific evidence.

## 2. Round / Large Sector / Canonical Archetype Scope

- scheduled_round: `R11`
- scheduled_loop: `11`
- large_sector_id: `L10_POLICY_EVENT_CROSS_REDTEAM_MISC`
- canonical_archetype_id: `C31_POLICY_SUBSIDY_LEGISLATION_EVENT`
- round_sector_consistency: `pass`
- loop_objective: `coverage_gap_fill | counterexample_mining | sector_specific_rule_discovery | canonical_archetype_compression | 4B_non_price_requirement_stress_test`

The chosen event is the 2024-06-03 South Korean East Sea offshore oil/gas exploration announcement. Reuters reported that the president approved exploratory drilling, that potential reserves were not yet proven, that a 20% success probability was discussed, and that energy stocks including Korea Gas and Daesung Energy jumped. citeturn497721news0 A follow-up Reuters piece emphasized both "great potential" and the still-uncertain, drilling-dependent nature of the prospect. citeturn793381news1

## 3. Previous Coverage / Duplicate Avoidance Check

R11 already has `85` representative triggers and `27` unique cases, with many 4B and price-only/no-evidence rows. This loop therefore avoids merely restating that price-only blowoff should be blocked; it isolates the residual distinction between **country-level policy evidence** and **company-specific beneficiary mapping**. fileciteturn466file0L3-L19

No stock_agent source code was opened. No production scoring change is proposed.

## 4. Stock-Web OHLC Input / Price Source Validation

The Stock-Web manifest says the atlas is built from FinanceData/marcap, has `price_adjustment_status = raw_unadjusted_marcap`, and has manifest `max_date = 2026-02-20`. fileciteturn467file0L4-L13 It also reports `calibration_shard_root = atlas/ohlcv_tradable_by_symbol_year`, raw shard root, schema path, universe path, market coverage, and the caveat that raw/unadjusted OHLC is not corporate-action adjusted. fileciteturn467file0L33-L58

The schema defines tradable raw calibration, excludes invalid/zero-OHLC rows from tradable shards, and defines `MFE_N_pct` / `MAE_N_pct` from the max high / min low over N tradable rows. fileciteturn486file0L3-L24

## 5. Historical Eligibility Gate

All representative trigger rows below use 2024-06-04 as next-trading-day close after the policy headline, because event timing is not treated as safely known for every market participant. The event is historical, the entry rows exist in Stock-Web tradable shards, and the manifest max date provides more than 180 forward tradable days.

Profile caveats:

- `036460` 한국가스공사: no corporate-action candidates, clean profile around the tested window. fileciteturn470file0L185-L196
- `117580` 대성에너지: no corporate-action candidates, clean profile around the tested window. fileciteturn479file0L135-L146
- `039610` 화성밸브: corporate-action candidates exist historically, but the last listed candidate is 2019-02-18, outside the 2024-2025 test window. fileciteturn482file0L14-L31
- `004090` 한국석유: historical corporate-action candidates exist in 1997 and 2021, outside the 2024-2025 window. fileciteturn471file0L26-L41
- `024060` 흥구석유: historical corporate-action candidates are pre-2009, outside the 2024-2025 window. fileciteturn476file0L21-L39
- `008970` 동양철관: later 2025 corporate-action candidate dates are after the 180D test window; the 2024-06 to early-2025 180D calibration path is treated as usable. fileciteturn484file0L31-L53

## 6. Canonical Archetype Compression Map

| fine_archetype_id | canonical_archetype_id | compression logic |
|---|---|---|
| EAST_SEA_EXPLORATION_POLICY_EVENT_DIRECT_BENEFICIARY_MAP | C31_POLICY_SUBSIDY_LEGISLATION_EVENT | A policy announcement creates optionality, but Stage2-Actionable requires a direct beneficiary map. |
| PERIPHERAL_ENERGY_THEME_PRICE_SPIKE | C31_POLICY_SUBSIDY_LEGISLATION_EVENT | Peripheral theme names may be tradable but should not become Green without order/economics confirmation. |
| POLICY_EVENT_4B_PRE_COMMERCIALIZATION_OVERHEAT | C31_POLICY_SUBSIDY_LEGISLATION_EVENT | A strong price move before drilling result is 4B overlay, not 4C thesis break. |

## 7. Case Selection Summary

| case_id | symbol | company | role | positive_or_counterexample | why selected |
|---|---:|---|---|---|---|
| R11L11_C31_KOGAS_DIRECT_POLICY_OPTIONALITY | 036460 | 한국가스공사 | Stage2 direct policy optionality | positive | State-linked gas/LNG route; strong MFE but not confirmed Green. |
| R11L11_C31_HSVALVE_PERIPHERAL_EQUIPMENT_OPTIONALITY | 039610 | 화성밸브 | peripheral Stage2 watch | positive | Large second-wave MFE, but no backlog/order evidence. |
| R11L11_C31_KOREA_OIL_PRICE_ONLY_THEME | 004090 | 한국석유 | price theme false positive | counterexample | MFE was small vs large 180D MAE. |
| R11L11_C31_HEUNGGU_OIL_PRICE_ONLY_THEME | 024060 | 흥구석유 | price theme false positive | counterexample | Fuel distributor not direct resource beneficiary. |
| R11L11_C31_DAESUNG_CITY_GAS_THEME_FADE | 117580 | 대성에너지 | city-gas theme fade | counterexample | Daily-limit headline move, no direct contract/tariff route. |
| R11L11_C31_DONGYANG_PIPE_PRICE_SPIKE | 008970 | 동양철관 | pipeline theme high-MAE | counterexample | High beta, high MAE, no confirmed order conversion. |

## 8. Positive vs Counterexample Balance

- positive_case_count: 2
- counterexample_count: 4
- calibration_usable_case_count: 6
- calibration_usable_trigger_count: 7
- new_independent_case_count: 6
- reused_case_count: 0

This is deliberately counterexample-heavy because R11 already has many event-premium / 4B rows and the residual error is over-acceptance of generic policy headlines as company-specific evidence.

## 9. Evidence Source Map

| evidence family | source | trigger implication |
|---|---|---|
| Government exploration approval | Reuters / WSJ, 2024-06-03 | Valid country-level policy evidence. |
| 20% success probability / drilling dependency | Reuters, 2024-06-03 and 2024-06-07 | Caps Stage3-Green before drilling/economics confirmation. |
| Energy stock reaction | Reuters, 2024-06-03 | Supports relative-strength observation but not direct evidence. |
| Stock-Web OHLC | Songdaiki/stock-web tradable shards | Used for MFE/MAE and 4B timing. |

## 10. Price Data Source Map

| symbol | shard | profile | entry_date | entry_price | profile status |
|---:|---|---|---|---:|---|
| 036460 | atlas/ohlcv_tradable_by_symbol_year/036/036460/2024.csv | atlas/symbol_profiles/036/036460.json | 2024-06-04 | 39400 | clean |
| 039610 | atlas/ohlcv_tradable_by_symbol_year/039/039610/2024.csv | atlas/symbol_profiles/039/039610.json | 2024-06-04 | 8630 | clean 2024 window |
| 004090 | atlas/ohlcv_tradable_by_symbol_year/004/004090/2024.csv | atlas/symbol_profiles/004/004090.json | 2024-06-04 | 23300 | clean 2024 window |
| 024060 | atlas/ohlcv_tradable_by_symbol_year/024/024060/2024.csv | atlas/symbol_profiles/024/024060.json | 2024-06-04 | 19240 | clean 2024 window |
| 117580 | atlas/ohlcv_tradable_by_symbol_year/117/117580/2024.csv | atlas/symbol_profiles/117/117580.json | 2024-06-04 | 12500 | clean |
| 008970 | atlas/ohlcv_tradable_by_symbol_year/008/008970/2024.csv | atlas/symbol_profiles/008/008970.json | 2024-06-04 | 1175 | clean 180D window |

## 11. Case-by-Case Trigger Grid

| trigger_id | type | symbol | entry | evidence split | current profile verdict |
|---|---|---:|---:|---|---|
| TR_R11L11_KOGAS_STAGE2_2024_06_03 | Stage2-Actionable | 036460 | 39400 | policy + direct gas-system linkage; no confirmed commercial discovery | current_profile_correct |
| TR_R11L11_KOGAS_4B_2024_06_20 | Stage4B | 036460 | 63500 | valuation/positioning before economics confirmation | current_profile_correct |
| TR_R11L11_HSVALVE_STAGE2_2024_06_03 | Stage2_event_premium_risk_watch | 039610 | 8630 | policy + equipment optionality, no order | current_profile_too_late |
| TR_R11L11_KOREAOIL_STAGE2_2024_06_03 | Stage2 candidate rejected | 004090 | 23300 | generic oil theme only | current_profile_false_positive |
| TR_R11L11_HEUNGGU_STAGE2_2024_06_03 | Stage2 candidate rejected | 024060 | 19240 | fuel distributor theme only | current_profile_false_positive |
| TR_R11L11_DAESUNG_STAGE2_2024_06_03 | Stage2 candidate rejected | 117580 | 12500 | city gas distributor theme only | current_profile_false_positive |
| TR_R11L11_DONGYANG_STAGE2_2024_06_03 | Stage2 candidate rejected | 008970 | 1175 | pipeline theme only | current_profile_false_positive |

## 12. Trigger-Level OHLC Backtest Tables

| trigger_id | entry_price | MFE_30D | MAE_30D | MFE_90D | MAE_90D | MFE_180D | MAE_180D | peak_date | peak_price | drawdown_after_peak |
|---|---:|---:|---:|---:|---:|---:|---:|---|---:|---:|
| TR_R11L11_KOGAS_STAGE2_2024_06_03 | 39400 | 63.71 | -5.20 | 63.71 | -7.36 | 63.71 | -24.87 | 2024-06-20 | 64500 | -54.11 |
| TR_R11L11_KOGAS_4B_2024_06_20 | 63500 | 1.57 | -34.72 | 1.57 | -42.52 | 1.57 | -53.39 | 2024-06-20 | 64500 | -54.11 |
| TR_R11L11_HSVALVE_STAGE2_2024_06_03 | 8630 | 28.39 | -21.21 | 77.52 | -21.21 | 78.68 | -21.21 | 2024-08-23 | 15420 | -46.76 |
| TR_R11L11_KOREAOIL_STAGE2_2024_06_03 | 23300 | 20.60 | -28.67 | 20.60 | -34.51 | 20.60 | -47.51 | 2024-06-05 | 28100 | -56.48 |
| TR_R11L11_HEUNGGU_STAGE2_2024_06_03 | 19240 | 8.89 | -28.85 | 13.83 | -35.76 | 13.83 | -42.83 | 2024-08-13 | 21900 | -49.77 |
| TR_R11L11_DAESUNG_STAGE2_2024_06_03 | 12500 | 12.80 | -28.88 | 12.80 | -31.92 | 12.80 | -37.84 | 2024-06-04 | 14100 | -44.89 |
| TR_R11L11_DONGYANG_STAGE2_2024_06_03 | 1175 | 42.81 | -22.55 | 42.81 | -29.70 | 42.81 | -31.66 | 2024-06-07 | 1678 | -50.77 |

Selected price-row anchors:

- KOGAS entered at 2024-06-04 close 39,400 and later printed a 64,500 high on 2024-06-20. fileciteturn472file0L12-L24 The later 2025 low area includes 29,600 on 2025-02-11. fileciteturn474file0L26-L31
- 한국석유 entered at 2024-06-04 close 23,300 and printed 28,100 on 2024-06-05, then later hit 12,230 on 2025-02-10. fileciteturn475file0L12-L18 fileciteturn488file0L26-L28
- 흥구석유 entered at 2024-06-04 close 19,240, later printed 21,900 on 2024-08-13 and 11,000 on 2025-02-07. fileciteturn477file0L12-L18 fileciteturn489file0L22-L27
- 대성에너지 entered at 2024-06-04 close 12,500, hit 14,100 intraday, and later faded below 8,000 in early 2025. fileciteturn480file0L12-L18 fileciteturn490file0L39-L43
- 화성밸브 entered at 2024-06-04 close 8,630 and later printed a second-wave 15,420 high on 2024-08-23. fileciteturn483file0L12-L18 fileciteturn483file0L66-L70
- 동양철관 entered at 2024-06-04 close 1,175, printed 1,678 on 2024-06-07, then fell to the 826 area by 2024-08-05. fileciteturn485file0L12-L18 fileciteturn485file0L55-L57

## 13. Current Calibrated Profile Stress Test

| case | current profile expected behavior | actual alignment | verdict |
|---|---|---|---|
| 한국가스공사 | Accept Stage2-Actionable, cap before confirmed discovery/economics | High MFE but large later drawdown; Stage2 ok, Green unsafe | current_profile_correct |
| 화성밸브 | Watch as peripheral event-premium unless order/backlog appears | Strong second-wave MFE suggests Stage2 watch useful, but not Green | current_profile_too_late |
| 한국석유 | Should reject Green; should not accept generic headline as direct evidence | MFE small vs high MAE | current_profile_false_positive if generic policy accepted |
| 흥구석유 | Same as above | MFE small, MAE large | current_profile_false_positive |
| 대성에너지 | Same as above | Immediate high, then large fade | current_profile_false_positive |
| 동양철관 | Same as above | High MFE, high MAE, no order conversion | current_profile_false_positive |

The residual issue is not that the global price-only guard is wrong. It is that **policy_or_regulatory_score** can be too generous unless it asks: “does the named company have a direct statutory, operator, budget, concession, order, tariff, or economics route?”

## 14. Stage2 / Yellow / Green Comparison

No Stage3-Green trigger is accepted in this MD. The event was real, but the project was exploratory, drilling-dependent, and explicitly uncertain. Reuters reported that the project would need drilling to prove resources and cited a 20% success rate; this makes Stage3-Green inappropriate without later confirmation. citeturn497721news0turn793381news1

`green_lateness_ratio = not_applicable` for all representative Stage2 rows because no confirmed Stage3-Green trigger is recognized.

## 15. 4B Local vs Full-window Timing Audit

| trigger_id | four_b_evidence_type | local_peak_proximity | full_window_peak_proximity | verdict |
|---|---|---:|---:|---|
| TR_R11L11_KOGAS_4B_2024_06_20 | valuation_blowoff + positioning_overheat + event cap | 0.97 | 0.97 | good_full_window_4B_timing |
| TR_R11L11_KOREAOIL_STAGE2_2024_06_03 | price_only | 0.00 | 0.00 | price_only_local_4B_too_early |
| TR_R11L11_HEUNGGU_STAGE2_2024_06_03 | price_only | n/a | n/a | price_only_local_4B_too_early |
| TR_R11L11_DAESUNG_STAGE2_2024_06_03 | price_only | 1.00 | 1.00 | price_only_local_4B_too_early |
| TR_R11L11_DONGYANG_STAGE2_2024_06_03 | price_only | 1.00 | 1.00 | price_only_local_4B_too_early |

4B is useful here as an overlay. It should not be treated as an immediate sell rule on every spike, but when a policy event has not yet converted into commercial/economic evidence, sharp local peaks need a risk overlay.

## 16. 4C Protection Audit

No hard 4C thesis-break row is accepted at the 2024-06 trigger because the initial event itself was exploratory. `hard_4c_thesis_break_routes_to_4c` is kept, but this loop does not claim a confirmed 4C break unless later evidence explicitly invalidates the discovery/economics thesis.

Protection label for this MD: `thesis_break_watch_only`.

## 17. Sector-Specific Rule Candidate

```text
rule_id = L10_C31_DIRECT_BENEFICIARY_MAPPING_REQUIRED
rule_scope = sector_specific
large_sector_id = L10_POLICY_EVENT_CROSS_REDTEAM_MISC
proposal_type = sector_shadow_only
```

For policy-event rounds, a policy headline should not automatically become Stage2-Actionable for every adjacent theme stock. Stage2-Actionable requires at least one direct beneficiary mapping:

```text
operator_or_concession_route
statutory_budget_or_subsidy_route
confirmed procurement/order route
tariff/reimbursement/regulated-return route
capacity/volume route controlled by the company
company-specific commercial economics route
```

If none exists, cap the row at:

```text
Stage2_event_premium_risk_watch
or
Stage2-Actionable_candidate_rejected
```

## 18. Canonical-Archetype Rule Candidate

```text
rule_id = C31_POLICY_EVENT_PROBABILITY_AND_DIRECT_ROUTE_DISCOUNT
rule_scope = canonical_archetype_specific
canonical_archetype_id = C31_POLICY_SUBSIDY_LEGISLATION_EVENT
proposal_type = canonical_shadow_only
```

C31 should treat a policy event as a **switchboard**, not a battery. The headline supplies voltage, but the current only reaches companies with a wired circuit: operator rights, budget, tariff, procurement, order, or regulated return. Peripheral names can still move, but they should be scored as event-premium risk watch unless that wire is visible.

## 19. Before / After Backtest Comparison

| profile_id | scope | hypothesis | eligible triggers | avg MFE_90D | avg MAE_90D | false positive rate | verdict |
|---|---|---|---:|---:|---:|---|---|
| P0_e2r_2_1_stock_web_calibrated_proxy | current | Current global profile accepts Stage2 evidence but blocks price-only Green/4B promotion. Residual risk: generic policy headline may still be over-counted as company-specific Stage2-Actionable. | 6 | 37.88 | -26.13 | 4/6 if generic policy is accepted as company-specific | partially_aligned_residual_false_positive |
| P0b_e2r_2_0_baseline_reference | rollback | Earlier baseline would more easily treat policy headline + RS as positive without direct beneficiary map. | 6 | 37.88 | -26.13 | 5/6 | too_permissive_for_policy_themes |
| P1_sector_specific_candidate_profile | L10_POLICY_EVENT_CROSS_REDTEAM_MISC | Require direct beneficiary mapping for Stage2-Actionable; otherwise cap at event-premium risk watch. | 6 | 70.62 | -14.29 | 1/2 among accepted | better_MAE_filtering |
| P2_canonical_archetype_candidate_profile | C31_POLICY_SUBSIDY_LEGISLATION_EVENT | For C31, policy event is not enough; require operator/statutory budget/concession/order/tariff/economics link. | 6 | 70.62 | -14.29 | 1/2 among accepted | best_explanatory_compression |
| P3_counterexample_guard_profile | guard | Peripheral policy-theme names with MFE but missing direct mapping get 4B/event-premium overlay, not Stage3 promotion. | 6 | counterexamples avg ~22.0 | counterexamples avg ~32.7 | 0 promoted | keeps_watchlist_without_green_false_positive |

## 20. Score-Return Alignment Matrix

| bucket | selected cases | price result | score implication |
|---|---|---|---|
| Direct policy beneficiary | 한국가스공사 | high MFE but high later drawdown | Stage2-Actionable allowed; Green capped until confirmed economics |
| Peripheral equipment with repeat theme beta | 화성밸브 | high MFE, moderate MAE | Stage2 watch allowed; no Green without order/backlog |
| Generic oil/fuel/city-gas theme | 한국석유, 흥구석유, 대성에너지 | low-to-moderate MFE, high MAE | reject Stage2-Actionable unless direct route appears |
| Material/pipeline theme | 동양철관 | high MFE, high MAE | watch-only; 4B overlay after spike |

## 21. Coverage Matrix

| large_sector_id | canonical_archetype_id | fine_archetype_id | positive_case_count | counterexample_count | 4B_case_count | 4C_case_count | new_independent_case_count | reused_case_count | calibration_usable_trigger_count | representative_trigger_count | current_profile_error_count | sector_rule_candidate | canonical_rule_candidate | coverage_gap_after_this_loop |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|---|---|
| L10_POLICY_EVENT_CROSS_REDTEAM_MISC | C31_POLICY_SUBSIDY_LEGISLATION_EVENT | EAST_SEA_EXPLORATION_POLICY_EVENT_DIRECT_BENEFICIARY_MAP | 2 | 4 | 1 | 0 | 6 | 0 | 7 | 6 | 4 | true | true | Still needs holdout cases from subsidy/legislation domains outside energy. |

## 22. Residual Contribution Summary

```yaml
new_independent_case_count: 6
reused_case_count: 0
reused_case_ids: []
new_symbol_count: 6
new_canonical_archetype_count: 0
new_fine_archetype_count: 1
new_trigger_family_count: 4
tested_existing_calibrated_axes:
  - stage2_actionable_evidence_bonus
  - price_only_blowoff_blocks_positive_stage
  - full_4b_requires_non_price_evidence
  - hard_4c_thesis_break_routes_to_4c
residual_error_types_found:
  - generic_policy_headline_overcount
  - peripheral_theme_false_positive
  - price_only_local_4B_too_early
new_axis_proposed:
  - C31_POLICY_EVENT_PROBABILITY_AND_DIRECT_ROUTE_DISCOUNT
existing_axis_strengthened:
  - price_only_blowoff_blocks_positive_stage
  - full_4b_requires_non_price_evidence
existing_axis_weakened: []
existing_axis_kept:
  - stage2_actionable_evidence_bonus
  - stage3_yellow_total_min
  - stage3_green_total_min
  - stage3_green_revision_min
  - stage3_cross_evidence_green_buffer
  - hard_4c_thesis_break_routes_to_4c
sector_specific_rule_candidate: true
canonical_archetype_rule_candidate: true
no_new_signal_reason: null
loop_contribution_label: canonical_archetype_rule_candidate
do_not_propose_new_weight_delta: false
```

## 23. Validation Scope / Non-Validation Scope

Validated:

- Historical R11/C31 policy-event behavior around a specific 2024 event.
- Actual Stock-Web OHLC rows for entry, peak, MFE/MAE, and drawdown anchors.
- Clean 180D calibration paths for selected representative rows.
- Current calibrated profile stress test under shadow-only assumptions.

Not validated:

- Current/live candidates.
- Any 2026 recommendation or watchlist.
- Any production scoring implementation.
- Any brokerage or auto-trading integration.
- Any source-code behavior inside `stock_agent/src/e2r`.

## 24. Shadow Weight Calibration

```csv
row_type,axis,scope,large_sector_id,canonical_archetype_id,baseline_value,tested_value,delta,reason,backtest_effect,trigger_ids,calibration_usable_count,new_independent_case_count,counterexample_count,confidence,proposal_type,notes
shadow_weight,c31_direct_beneficiary_mapping_required,canonical_archetype_specific,L10_POLICY_EVENT_CROSS_REDTEAM_MISC,C31_POLICY_SUBSIDY_LEGISLATION_EVENT,0,1,+1,"generic policy headline overcounts peripheral names","reduced false-positive promotion in 4/6 cases","TR_R11L11_KOGAS_STAGE2_2024_06_03|TR_R11L11_HSVALVE_STAGE2_2024_06_03|TR_R11L11_KOREAOIL_STAGE2_2024_06_03|TR_R11L11_HEUNGGU_STAGE2_2024_06_03|TR_R11L11_DAESUNG_STAGE2_2024_06_03|TR_R11L11_DONGYANG_STAGE2_2024_06_03",6,6,4,medium,canonical_shadow_only,"not production; post-calibrated residual"
shadow_weight,c31_event_probability_discount,canonical_archetype_specific,L10_POLICY_EVENT_CROSS_REDTEAM_MISC,C31_POLICY_SUBSIDY_LEGISLATION_EVENT,0,1,+1,"exploratory policy events should be discounted until drilling/economics confirmation","caps premature Green in unproven resource-policy event","TR_R11L11_KOGAS_STAGE2_2024_06_03|TR_R11L11_KOGAS_4B_2024_06_20",2,2,0,medium,canonical_shadow_only,"not production; keeps Stage2 but blocks Green"
shadow_weight,c31_peripheral_theme_price_only_4b_overlay,sector_specific,L10_POLICY_EVENT_CROSS_REDTEAM_MISC,C31_POLICY_SUBSIDY_LEGISLATION_EVENT,0,1,+1,"peripheral event-theme spikes show high MAE without direct mapping","turns price-only move into overlay/risk watch instead of promotion","TR_R11L11_KOREAOIL_STAGE2_2024_06_03|TR_R11L11_HEUNGGU_STAGE2_2024_06_03|TR_R11L11_DAESUNG_STAGE2_2024_06_03|TR_R11L11_DONGYANG_STAGE2_2024_06_03",4,4,4,medium,sector_shadow_only,"not production; supports existing price-only guard"
```

## 25. Machine-Readable Rows

### 25.1 price_source_validation

```jsonl
{"row_type": "price_source_validation", "source": "Songdaiki/stock-web", "source_url": "https://github.com/Songdaiki/stock-web", "manifest_path": "atlas/manifest.json", "schema_path": "atlas/schema.json", "universe_path": "atlas/universe/all_symbols.csv", "manifest_max_date": "2026-02-20", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "raw_shard_root": "atlas/ohlcv_raw_by_symbol_year", "validation_status": "usable_for_historical_calibration"}
```

### 25.2 case rows

```jsonl
{"row_type":"case","case_id":"R11L11_C31_KOGAS_DIRECT_POLICY_OPTIONALITY","symbol":"036460","company_name":"한국가스공사","case_type":"stage2_promote_candidate","polarity":"positive","best_trigger":"TR_R11L11_KOGAS_STAGE2_2024_06_03","current_profile_verdict":"current_profile_correct","notes":"Direct state-run gas utility / LNG importer route; policy event had direct national energy-system linkage but still lacked commercial discovery confirmation.","round":"R11","loop":"11","large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"C31_POLICY_SUBSIDY_LEGISLATION_EVENT","fine_archetype_id":"EAST_SEA_EXPLORATION_POLICY_EVENT_DIRECT_BENEFICIARY_MAP","positive_or_counterexample":"positive","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"mixed_policy_event_alignment","price_source":"Songdaiki/stock-web"}
{"row_type":"case","case_id":"R11L11_C31_HSVALVE_PERIPHERAL_EQUIPMENT_OPTIONALITY","symbol":"039610","company_name":"화성밸브","case_type":"high_mae_success","polarity":"positive","best_trigger":"TR_R11L11_HSVALVE_STAGE2_2024_06_03","current_profile_verdict":"current_profile_too_late","notes":"Peripheral equipment optionality produced a second-wave MFE, but company-specific order conversion was absent; positive only for Stage2 watch, not Green.","round":"R11","loop":"11","large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"C31_POLICY_SUBSIDY_LEGISLATION_EVENT","fine_archetype_id":"EAST_SEA_EXPLORATION_POLICY_EVENT_DIRECT_BENEFICIARY_MAP","positive_or_counterexample":"positive","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"mixed_policy_event_alignment","price_source":"Songdaiki/stock-web"}
{"row_type":"case","case_id":"R11L11_C31_KOREA_OIL_PRICE_ONLY_THEME","symbol":"004090","company_name":"한국석유","case_type":"false_positive_green","polarity":"counterexample","best_trigger":"TR_R11L11_KOREAOIL_STAGE2_2024_06_03","current_profile_verdict":"current_profile_false_positive","notes":"Generic oil-theme rerating without operator, concession, budget, order or margin bridge evidence.","round":"R11","loop":"11","large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"C31_POLICY_SUBSIDY_LEGISLATION_EVENT","fine_archetype_id":"EAST_SEA_EXPLORATION_POLICY_EVENT_DIRECT_BENEFICIARY_MAP","positive_or_counterexample":"counterexample","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"mixed_policy_event_alignment","price_source":"Songdaiki/stock-web"}
{"row_type":"case","case_id":"R11L11_C31_HEUNGGU_OIL_PRICE_ONLY_THEME","symbol":"024060","company_name":"흥구석유","case_type":"false_positive_green","polarity":"counterexample","best_trigger":"TR_R11L11_HEUNGGU_STAGE2_2024_06_03","current_profile_verdict":"current_profile_false_positive","notes":"Fuel distributor price spike; broad energy policy headline did not map to direct earnings route.","round":"R11","loop":"11","large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"C31_POLICY_SUBSIDY_LEGISLATION_EVENT","fine_archetype_id":"EAST_SEA_EXPLORATION_POLICY_EVENT_DIRECT_BENEFICIARY_MAP","positive_or_counterexample":"counterexample","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"mixed_policy_event_alignment","price_source":"Songdaiki/stock-web"}
{"row_type":"case","case_id":"R11L11_C31_DAESUNG_CITY_GAS_THEME_FADE","symbol":"117580","company_name":"대성에너지","case_type":"failed_rerating","polarity":"counterexample","best_trigger":"TR_R11L11_DAESUNG_STAGE2_2024_06_03","current_profile_verdict":"current_profile_false_positive","notes":"City-gas distributor moved on energy headline; no drilling economics, tariff, concession, or volume bridge at trigger.","round":"R11","loop":"11","large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"C31_POLICY_SUBSIDY_LEGISLATION_EVENT","fine_archetype_id":"EAST_SEA_EXPLORATION_POLICY_EVENT_DIRECT_BENEFICIARY_MAP","positive_or_counterexample":"counterexample","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"mixed_policy_event_alignment","price_source":"Songdaiki/stock-web"}
{"row_type":"case","case_id":"R11L11_C31_DONGYANG_PIPE_PRICE_SPIKE","symbol":"008970","company_name":"동양철관","case_type":"price_moved_without_evidence","polarity":"counterexample","best_trigger":"TR_R11L11_DONGYANG_STAGE2_2024_06_03","current_profile_verdict":"current_profile_false_positive","notes":"Pipeline-material theme; large MFE but rapid MAE and no confirmed order/backlog path from the policy event.","round":"R11","loop":"11","large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"C31_POLICY_SUBSIDY_LEGISLATION_EVENT","fine_archetype_id":"EAST_SEA_EXPLORATION_POLICY_EVENT_DIRECT_BENEFICIARY_MAP","positive_or_counterexample":"counterexample","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"mixed_policy_event_alignment","price_source":"Songdaiki/stock-web"}
```

### 25.3 trigger rows

```jsonl
{"row_type":"trigger","round":"R11","loop":"11","large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"C31_POLICY_SUBSIDY_LEGISLATION_EVENT","fine_archetype_id":"EAST_SEA_EXPLORATION_POLICY_EVENT_DIRECT_BENEFICIARY_MAP","sector":"policy_event_energy_theme","primary_archetype":"policy_event_to_direct_beneficiary_vs_peripheral_theme","loop_objective":"coverage_gap_fill|counterexample_mining|sector_specific_rule_discovery|canonical_archetype_compression|4B_non_price_requirement_stress_test","trigger_id":"TR_R11L11_KOGAS_STAGE2_2024_06_03","case_id":"R11L11_C31_KOGAS_DIRECT_POLICY_OPTIONALITY","symbol":"036460","company_name":"한국가스공사","trigger_type":"Stage2-Actionable","trigger_date":"2024-06-03","entry_date":"2024-06-04","entry_price":39400,"evidence_available_at_that_date":"South Korea approved East Sea offshore exploration drilling; KOGAS was named among energy stocks that jumped; direct national LNG/gas-system linkage but no commercial discovery yet.","evidence_source":"Reuters 2024-06-03; WSJ 2024-06-03; Songdaiki/stock-web shard rows","stage2_evidence_fields":["public_event_or_disclosure","policy_or_regulatory_optionality","capacity_or_volume_route"],"stage3_evidence_fields":["multiple_public_sources"],"stage4b_evidence_fields":[],"stage4c_evidence_fields":[],"price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/036/036460/2024.csv","profile_path":"atlas/symbol_profiles/036/036460.json","MFE_30D_pct":63.71,"MFE_90D_pct":63.71,"MFE_180D_pct":63.71,"MFE_1Y_pct":63.71,"MFE_2Y_pct":null,"MAE_30D_pct":-5.2,"MAE_90D_pct":-7.36,"MAE_180D_pct":-24.87,"MAE_1Y_pct":-24.87,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-06-20","peak_price":64500,"drawdown_after_peak_pct":-54.11,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":null,"four_b_full_window_peak_proximity":null,"four_b_timing_verdict":null,"four_b_evidence_type":[],"four_c_protection_label":"thesis_break_watch_only","trigger_outcome_label":"direct_policy_optional_success_high_drawdown","current_profile_verdict":"current_profile_correct","calibration_usable":true,"forward_window_trading_days":180,"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"036460_2024-06-04_39400","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false,"price_data_source":"Songdaiki/stock-web","price_data_repo":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","calibration_block_reasons":[],"reuse_reason":null}
{"row_type":"trigger","round":"R11","loop":"11","large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"C31_POLICY_SUBSIDY_LEGISLATION_EVENT","fine_archetype_id":"EAST_SEA_EXPLORATION_POLICY_EVENT_DIRECT_BENEFICIARY_MAP","sector":"policy_event_energy_theme","primary_archetype":"policy_event_to_direct_beneficiary_vs_peripheral_theme","loop_objective":"coverage_gap_fill|counterexample_mining|sector_specific_rule_discovery|canonical_archetype_compression|4B_non_price_requirement_stress_test","trigger_id":"TR_R11L11_KOGAS_4B_2024_06_20","case_id":"R11L11_C31_KOGAS_DIRECT_POLICY_OPTIONALITY","symbol":"036460","company_name":"한국가스공사","trigger_type":"Stage4B","trigger_date":"2024-06-20","entry_date":"2024-06-20","entry_price":63500,"evidence_available_at_that_date":"Price had already approached full observed-window high while commercial feasibility and drilling result remained unconfirmed; this is 4B overlay, not thesis break.","evidence_source":"Reuters 2024-06-03/2024-06-07; Songdaiki/stock-web shard rows","stage2_evidence_fields":[],"stage3_evidence_fields":[],"stage4b_evidence_fields":["valuation_blowoff","positioning_overheat","explicit_event_cap"],"stage4c_evidence_fields":[],"price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/036/036460/2024.csv","profile_path":"atlas/symbol_profiles/036/036460.json","MFE_30D_pct":1.57,"MFE_90D_pct":1.57,"MFE_180D_pct":1.57,"MFE_1Y_pct":1.57,"MFE_2Y_pct":null,"MAE_30D_pct":-34.72,"MAE_90D_pct":-42.52,"MAE_180D_pct":-53.39,"MAE_1Y_pct":-53.39,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-06-20","peak_price":64500,"drawdown_after_peak_pct":-54.11,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":0.97,"four_b_full_window_peak_proximity":0.97,"four_b_timing_verdict":"good_full_window_4B_timing","four_b_evidence_type":["valuation_blowoff","positioning_overheat","explicit_event_cap"],"four_c_protection_label":"thesis_break_watch_only","trigger_outcome_label":"4B_overlay_success","current_profile_verdict":"current_profile_correct","calibration_usable":true,"forward_window_trading_days":180,"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"036460_2024-06-20_63500","dedupe_for_aggregate":false,"aggregate_group_role":"4B_overlay_only","is_new_independent_case":true,"independent_evidence_weight":0.5,"do_not_count_as_new_case":true,"price_data_source":"Songdaiki/stock-web","price_data_repo":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","calibration_block_reasons":[],"reuse_reason":null}
{"row_type":"trigger","round":"R11","loop":"11","large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"C31_POLICY_SUBSIDY_LEGISLATION_EVENT","fine_archetype_id":"EAST_SEA_EXPLORATION_POLICY_EVENT_DIRECT_BENEFICIARY_MAP","sector":"policy_event_energy_theme","primary_archetype":"policy_event_to_direct_beneficiary_vs_peripheral_theme","loop_objective":"coverage_gap_fill|counterexample_mining|sector_specific_rule_discovery|canonical_archetype_compression|4B_non_price_requirement_stress_test","trigger_id":"TR_R11L11_HSVALVE_STAGE2_2024_06_03","case_id":"R11L11_C31_HSVALVE_PERIPHERAL_EQUIPMENT_OPTIONALITY","symbol":"039610","company_name":"화성밸브","trigger_type":"Stage2_event_premium_risk_watch","trigger_date":"2024-06-03","entry_date":"2024-06-04","entry_price":8630,"evidence_available_at_that_date":"Valve-equipment theme attached to gas exploration policy; no company-specific order or backlog confirmation at trigger.","evidence_source":"Reuters 2024-06-03/2024-06-07; Songdaiki/stock-web shard rows","stage2_evidence_fields":["public_event_or_disclosure","policy_or_regulatory_optionality"],"stage3_evidence_fields":[],"stage4b_evidence_fields":[],"stage4c_evidence_fields":[],"price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/039/039610/2024.csv","profile_path":"atlas/symbol_profiles/039/039610.json","MFE_30D_pct":28.39,"MFE_90D_pct":77.52,"MFE_180D_pct":78.68,"MFE_1Y_pct":78.68,"MFE_2Y_pct":null,"MAE_30D_pct":-21.21,"MAE_90D_pct":-21.21,"MAE_180D_pct":-21.21,"MAE_1Y_pct":-21.21,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-08-23","peak_price":15420,"drawdown_after_peak_pct":-46.76,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":null,"four_b_full_window_peak_proximity":null,"four_b_timing_verdict":null,"four_b_evidence_type":[],"four_c_protection_label":"thesis_break_watch_only","trigger_outcome_label":"peripheral_event_trade_success_not_green","current_profile_verdict":"current_profile_too_late","calibration_usable":true,"forward_window_trading_days":180,"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"039610_2024-06-04_8630","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false,"price_data_source":"Songdaiki/stock-web","price_data_repo":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","calibration_block_reasons":[],"reuse_reason":null}
{"row_type":"trigger","round":"R11","loop":"11","large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"C31_POLICY_SUBSIDY_LEGISLATION_EVENT","fine_archetype_id":"EAST_SEA_EXPLORATION_POLICY_EVENT_DIRECT_BENEFICIARY_MAP","sector":"policy_event_energy_theme","primary_archetype":"policy_event_to_direct_beneficiary_vs_peripheral_theme","loop_objective":"coverage_gap_fill|counterexample_mining|sector_specific_rule_discovery|canonical_archetype_compression|4B_non_price_requirement_stress_test","trigger_id":"TR_R11L11_KOREAOIL_STAGE2_2024_06_03","case_id":"R11L11_C31_KOREA_OIL_PRICE_ONLY_THEME","symbol":"004090","company_name":"한국석유","trigger_type":"Stage2-Actionable_candidate_rejected","trigger_date":"2024-06-03","entry_date":"2024-06-04","entry_price":23300,"evidence_available_at_that_date":"Generic oil-stock policy theme; no operator/concession/order/margin bridge. MFE came fast, but forward MAE overwhelmed the signal.","evidence_source":"Reuters 2024-06-03; Songdaiki/stock-web shard rows","stage2_evidence_fields":["public_event_or_disclosure","policy_or_regulatory_optionality"],"stage3_evidence_fields":[],"stage4b_evidence_fields":["price_only_local_peak"],"stage4c_evidence_fields":[],"price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/004/004090/2024.csv","profile_path":"atlas/symbol_profiles/004/004090.json","MFE_30D_pct":20.6,"MFE_90D_pct":20.6,"MFE_180D_pct":20.6,"MFE_1Y_pct":20.6,"MFE_2Y_pct":null,"MAE_30D_pct":-28.67,"MAE_90D_pct":-34.51,"MAE_180D_pct":-47.51,"MAE_1Y_pct":-47.51,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-06-05","peak_price":28100,"drawdown_after_peak_pct":-56.48,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":0.0,"four_b_full_window_peak_proximity":0.0,"four_b_timing_verdict":"price_only_local_4B_too_early","four_b_evidence_type":["price_only"],"four_c_protection_label":"thesis_break_watch_only","trigger_outcome_label":"policy_theme_false_positive","current_profile_verdict":"current_profile_false_positive","calibration_usable":true,"forward_window_trading_days":180,"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"004090_2024-06-04_23300","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false,"price_data_source":"Songdaiki/stock-web","price_data_repo":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","calibration_block_reasons":[],"reuse_reason":null}
{"row_type":"trigger","round":"R11","loop":"11","large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"C31_POLICY_SUBSIDY_LEGISLATION_EVENT","fine_archetype_id":"EAST_SEA_EXPLORATION_POLICY_EVENT_DIRECT_BENEFICIARY_MAP","sector":"policy_event_energy_theme","primary_archetype":"policy_event_to_direct_beneficiary_vs_peripheral_theme","loop_objective":"coverage_gap_fill|counterexample_mining|sector_specific_rule_discovery|canonical_archetype_compression|4B_non_price_requirement_stress_test","trigger_id":"TR_R11L11_HEUNGGU_STAGE2_2024_06_03","case_id":"R11L11_C31_HEUNGGU_OIL_PRICE_ONLY_THEME","symbol":"024060","company_name":"흥구석유","trigger_type":"Stage2-Actionable_candidate_rejected","trigger_date":"2024-06-03","entry_date":"2024-06-04","entry_price":19240,"evidence_available_at_that_date":"Fuel-distributor theme moved with oil/gas headline; no direct resource ownership or contract visibility.","evidence_source":"Reuters 2024-06-03; Songdaiki/stock-web shard rows","stage2_evidence_fields":["public_event_or_disclosure","policy_or_regulatory_optionality"],"stage3_evidence_fields":[],"stage4b_evidence_fields":["price_only_local_peak"],"stage4c_evidence_fields":[],"price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/024/024060/2024.csv","profile_path":"atlas/symbol_profiles/024/024060.json","MFE_30D_pct":8.89,"MFE_90D_pct":13.83,"MFE_180D_pct":13.83,"MFE_1Y_pct":13.83,"MFE_2Y_pct":null,"MAE_30D_pct":-28.85,"MAE_90D_pct":-35.76,"MAE_180D_pct":-42.83,"MAE_1Y_pct":-42.83,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-08-13","peak_price":21900,"drawdown_after_peak_pct":-49.77,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":null,"four_b_full_window_peak_proximity":null,"four_b_timing_verdict":"price_only_local_4B_too_early","four_b_evidence_type":["price_only"],"four_c_protection_label":"thesis_break_watch_only","trigger_outcome_label":"policy_theme_false_positive","current_profile_verdict":"current_profile_false_positive","calibration_usable":true,"forward_window_trading_days":180,"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"024060_2024-06-04_19240","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false,"price_data_source":"Songdaiki/stock-web","price_data_repo":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","calibration_block_reasons":[],"reuse_reason":null}
{"row_type":"trigger","round":"R11","loop":"11","large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"C31_POLICY_SUBSIDY_LEGISLATION_EVENT","fine_archetype_id":"EAST_SEA_EXPLORATION_POLICY_EVENT_DIRECT_BENEFICIARY_MAP","sector":"policy_event_energy_theme","primary_archetype":"policy_event_to_direct_beneficiary_vs_peripheral_theme","loop_objective":"coverage_gap_fill|counterexample_mining|sector_specific_rule_discovery|canonical_archetype_compression|4B_non_price_requirement_stress_test","trigger_id":"TR_R11L11_DAESUNG_STAGE2_2024_06_03","case_id":"R11L11_C31_DAESUNG_CITY_GAS_THEME_FADE","symbol":"117580","company_name":"대성에너지","trigger_type":"Stage2-Actionable_candidate_rejected","trigger_date":"2024-06-03","entry_date":"2024-06-04","entry_price":12500,"evidence_available_at_that_date":"City gas distributor hit daily limit, but no specific tariff, volume, concession, or exploration ownership evidence existed.","evidence_source":"Reuters 2024-06-03; Songdaiki/stock-web shard rows","stage2_evidence_fields":["public_event_or_disclosure","policy_or_regulatory_optionality"],"stage3_evidence_fields":[],"stage4b_evidence_fields":["price_only_local_peak"],"stage4c_evidence_fields":[],"price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/117/117580/2024.csv","profile_path":"atlas/symbol_profiles/117/117580.json","MFE_30D_pct":12.8,"MFE_90D_pct":12.8,"MFE_180D_pct":12.8,"MFE_1Y_pct":12.8,"MFE_2Y_pct":null,"MAE_30D_pct":-28.88,"MAE_90D_pct":-31.92,"MAE_180D_pct":-37.84,"MAE_1Y_pct":-37.84,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-06-04","peak_price":14100,"drawdown_after_peak_pct":-44.89,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":1.0,"four_b_full_window_peak_proximity":1.0,"four_b_timing_verdict":"price_only_local_4B_too_early","four_b_evidence_type":["price_only"],"four_c_protection_label":"thesis_break_watch_only","trigger_outcome_label":"policy_theme_false_positive","current_profile_verdict":"current_profile_false_positive","calibration_usable":true,"forward_window_trading_days":180,"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"117580_2024-06-04_12500","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false,"price_data_source":"Songdaiki/stock-web","price_data_repo":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","calibration_block_reasons":[],"reuse_reason":null}
{"row_type":"trigger","round":"R11","loop":"11","large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"C31_POLICY_SUBSIDY_LEGISLATION_EVENT","fine_archetype_id":"EAST_SEA_EXPLORATION_POLICY_EVENT_DIRECT_BENEFICIARY_MAP","sector":"policy_event_energy_theme","primary_archetype":"policy_event_to_direct_beneficiary_vs_peripheral_theme","loop_objective":"coverage_gap_fill|counterexample_mining|sector_specific_rule_discovery|canonical_archetype_compression|4B_non_price_requirement_stress_test","trigger_id":"TR_R11L11_DONGYANG_STAGE2_2024_06_03","case_id":"R11L11_C31_DONGYANG_PIPE_PRICE_SPIKE","symbol":"008970","company_name":"동양철관","trigger_type":"Stage2-Actionable_candidate_rejected","trigger_date":"2024-06-03","entry_date":"2024-06-04","entry_price":1175,"evidence_available_at_that_date":"Pipeline-material theme; price had direct theme beta but no order/backlog conversion from drilling policy at trigger.","evidence_source":"Reuters 2024-06-03; Songdaiki/stock-web shard rows","stage2_evidence_fields":["public_event_or_disclosure","policy_or_regulatory_optionality"],"stage3_evidence_fields":[],"stage4b_evidence_fields":["price_only_local_peak"],"stage4c_evidence_fields":[],"price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/008/008970/2024.csv","profile_path":"atlas/symbol_profiles/008/008970.json","MFE_30D_pct":42.81,"MFE_90D_pct":42.81,"MFE_180D_pct":42.81,"MFE_1Y_pct":42.81,"MFE_2Y_pct":null,"MAE_30D_pct":-22.55,"MAE_90D_pct":-29.7,"MAE_180D_pct":-31.66,"MAE_1Y_pct":-31.66,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-06-07","peak_price":1678,"drawdown_after_peak_pct":-50.77,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":1.0,"four_b_full_window_peak_proximity":1.0,"four_b_timing_verdict":"price_only_local_4B_too_early","four_b_evidence_type":["price_only"],"four_c_protection_label":"thesis_break_watch_only","trigger_outcome_label":"policy_theme_false_positive_high_mae","current_profile_verdict":"current_profile_false_positive","calibration_usable":true,"forward_window_trading_days":180,"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"008970_2024-06-04_1175","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false,"price_data_source":"Songdaiki/stock-web","price_data_repo":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","calibration_block_reasons":[],"reuse_reason":null}
```

### 25.4 score_simulation rows

```jsonl
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"R11L11_C31_KOGAS_DIRECT_POLICY_OPTIONALITY","trigger_id":"TR_R11L11_KOGAS_STAGE2_2024_06_03","symbol":"036460","large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"C31_POLICY_SUBSIDY_LEGISLATION_EVENT","raw_component_scores_before":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":0,"revision_score":0,"relative_strength_score":22,"customer_quality_score":0,"policy_or_regulatory_score":22,"valuation_repricing_score":12,"execution_risk_score":0,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0,"direct_beneficiary_mapping_score":0,"event_probability_discount_score":0,"price_only_theme_risk_score":0},"weighted_score_before":72,"stage_label_before":"Stage2-Actionable","raw_component_scores_after":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":0,"revision_score":0,"relative_strength_score":22,"customer_quality_score":0,"policy_or_regulatory_score":25,"valuation_repricing_score":0,"execution_risk_score":0,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0,"direct_beneficiary_mapping_score":20,"event_probability_discount_score":-6,"price_only_theme_risk_score":0},"weighted_score_after":81,"stage_label_after":"Stage2-Actionable_high_quality_watch","changed_components":["direct_beneficiary_mapping_score","event_probability_discount_score"],"component_delta_explanation":"C31-specific direct beneficiary map separates policy evidence from generic price-theme evidence.","MFE_90D_pct":63.71,"MAE_90D_pct":-7.36,"score_return_alignment_label":"improved_after_direct_mapping_guard","current_profile_verdict":"current_profile_correct"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"R11L11_C31_HSVALVE_PERIPHERAL_EQUIPMENT_OPTIONALITY","trigger_id":"TR_R11L11_HSVALVE_STAGE2_2024_06_03","symbol":"039610","large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"C31_POLICY_SUBSIDY_LEGISLATION_EVENT","raw_component_scores_before":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":0,"revision_score":0,"relative_strength_score":22,"customer_quality_score":0,"policy_or_regulatory_score":22,"valuation_repricing_score":12,"execution_risk_score":0,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0,"direct_beneficiary_mapping_score":0,"event_probability_discount_score":0,"price_only_theme_risk_score":0},"weighted_score_before":70,"stage_label_before":"Stage2-Actionable_candidate","raw_component_scores_after":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":0,"revision_score":0,"relative_strength_score":20,"customer_quality_score":0,"policy_or_regulatory_score":14,"valuation_repricing_score":0,"execution_risk_score":0,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0,"direct_beneficiary_mapping_score":8,"event_probability_discount_score":-8,"price_only_theme_risk_score":-6},"weighted_score_after":64,"stage_label_after":"Stage2_event_premium_risk_watch","changed_components":["direct_beneficiary_mapping_score","event_probability_discount_score","price_only_theme_risk_score"],"component_delta_explanation":"C31-specific direct beneficiary map separates policy evidence from generic price-theme evidence.","MFE_90D_pct":77.52,"MAE_90D_pct":-21.21,"score_return_alignment_label":"improved_after_direct_mapping_guard","current_profile_verdict":"current_profile_too_late"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"R11L11_C31_KOREA_OIL_PRICE_ONLY_THEME","trigger_id":"TR_R11L11_KOREAOIL_STAGE2_2024_06_03","symbol":"004090","large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"C31_POLICY_SUBSIDY_LEGISLATION_EVENT","raw_component_scores_before":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":0,"revision_score":0,"relative_strength_score":22,"customer_quality_score":0,"policy_or_regulatory_score":22,"valuation_repricing_score":6,"execution_risk_score":0,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0,"direct_beneficiary_mapping_score":0,"event_probability_discount_score":0,"price_only_theme_risk_score":0},"weighted_score_before":67,"stage_label_before":"Stage2-Actionable_candidate","raw_component_scores_after":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":0,"revision_score":0,"relative_strength_score":22,"customer_quality_score":0,"policy_or_regulatory_score":10,"valuation_repricing_score":0,"execution_risk_score":0,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0,"direct_beneficiary_mapping_score":0,"event_probability_discount_score":-10,"price_only_theme_risk_score":-14},"weighted_score_after":48,"stage_label_after":"Stage2_candidate_rejected_price_theme","changed_components":["direct_beneficiary_mapping_score","event_probability_discount_score","price_only_theme_risk_score","policy_or_regulatory_score"],"component_delta_explanation":"C31-specific direct beneficiary map separates policy evidence from generic price-theme evidence.","MFE_90D_pct":20.6,"MAE_90D_pct":-34.51,"score_return_alignment_label":"improved_after_direct_mapping_guard","current_profile_verdict":"current_profile_false_positive"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"R11L11_C31_HEUNGGU_OIL_PRICE_ONLY_THEME","trigger_id":"TR_R11L11_HEUNGGU_STAGE2_2024_06_03","symbol":"024060","large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"C31_POLICY_SUBSIDY_LEGISLATION_EVENT","raw_component_scores_before":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":0,"revision_score":0,"relative_strength_score":14,"customer_quality_score":0,"policy_or_regulatory_score":22,"valuation_repricing_score":6,"execution_risk_score":0,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0,"direct_beneficiary_mapping_score":0,"event_probability_discount_score":0,"price_only_theme_risk_score":0},"weighted_score_before":67,"stage_label_before":"Stage2-Actionable_candidate","raw_component_scores_after":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":0,"revision_score":0,"relative_strength_score":14,"customer_quality_score":0,"policy_or_regulatory_score":10,"valuation_repricing_score":0,"execution_risk_score":0,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0,"direct_beneficiary_mapping_score":0,"event_probability_discount_score":-10,"price_only_theme_risk_score":-14},"weighted_score_after":48,"stage_label_after":"Stage2_candidate_rejected_price_theme","changed_components":["direct_beneficiary_mapping_score","event_probability_discount_score","price_only_theme_risk_score","policy_or_regulatory_score"],"component_delta_explanation":"C31-specific direct beneficiary map separates policy evidence from generic price-theme evidence.","MFE_90D_pct":13.83,"MAE_90D_pct":-35.76,"score_return_alignment_label":"improved_after_direct_mapping_guard","current_profile_verdict":"current_profile_false_positive"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"R11L11_C31_DAESUNG_CITY_GAS_THEME_FADE","trigger_id":"TR_R11L11_DAESUNG_STAGE2_2024_06_03","symbol":"117580","large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"C31_POLICY_SUBSIDY_LEGISLATION_EVENT","raw_component_scores_before":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":0,"revision_score":0,"relative_strength_score":14,"customer_quality_score":0,"policy_or_regulatory_score":22,"valuation_repricing_score":6,"execution_risk_score":0,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0,"direct_beneficiary_mapping_score":0,"event_probability_discount_score":0,"price_only_theme_risk_score":0},"weighted_score_before":67,"stage_label_before":"Stage2-Actionable_candidate","raw_component_scores_after":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":0,"revision_score":0,"relative_strength_score":14,"customer_quality_score":0,"policy_or_regulatory_score":10,"valuation_repricing_score":0,"execution_risk_score":0,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0,"direct_beneficiary_mapping_score":0,"event_probability_discount_score":-10,"price_only_theme_risk_score":-14},"weighted_score_after":48,"stage_label_after":"Stage2_candidate_rejected_price_theme","changed_components":["direct_beneficiary_mapping_score","event_probability_discount_score","price_only_theme_risk_score","policy_or_regulatory_score"],"component_delta_explanation":"C31-specific direct beneficiary map separates policy evidence from generic price-theme evidence.","MFE_90D_pct":12.8,"MAE_90D_pct":-31.92,"score_return_alignment_label":"improved_after_direct_mapping_guard","current_profile_verdict":"current_profile_false_positive"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"R11L11_C31_DONGYANG_PIPE_PRICE_SPIKE","trigger_id":"TR_R11L11_DONGYANG_STAGE2_2024_06_03","symbol":"008970","large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"C31_POLICY_SUBSIDY_LEGISLATION_EVENT","raw_component_scores_before":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":0,"revision_score":0,"relative_strength_score":22,"customer_quality_score":0,"policy_or_regulatory_score":22,"valuation_repricing_score":12,"execution_risk_score":0,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0,"direct_beneficiary_mapping_score":0,"event_probability_discount_score":0,"price_only_theme_risk_score":0},"weighted_score_before":67,"stage_label_before":"Stage2-Actionable_candidate","raw_component_scores_after":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":0,"revision_score":0,"relative_strength_score":22,"customer_quality_score":0,"policy_or_regulatory_score":10,"valuation_repricing_score":0,"execution_risk_score":0,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0,"direct_beneficiary_mapping_score":0,"event_probability_discount_score":-10,"price_only_theme_risk_score":-14},"weighted_score_after":48,"stage_label_after":"Stage2_candidate_rejected_price_theme","changed_components":["direct_beneficiary_mapping_score","event_probability_discount_score","price_only_theme_risk_score","policy_or_regulatory_score"],"component_delta_explanation":"C31-specific direct beneficiary map separates policy evidence from generic price-theme evidence.","MFE_90D_pct":42.81,"MAE_90D_pct":-29.7,"score_return_alignment_label":"improved_after_direct_mapping_guard","current_profile_verdict":"current_profile_false_positive"}
```

### 25.5 shadow_weight rows

See section 24 CSV.

### 25.6 residual_contribution row

```jsonl
{"row_type":"residual_contribution","round":"R11","loop":"11","large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"C31_POLICY_SUBSIDY_LEGISLATION_EVENT","new_independent_case_count":6,"reused_case_count":0,"new_symbol_count":6,"new_trigger_family_count":4,"tested_existing_calibrated_axes":["stage2_actionable_evidence_bonus","price_only_blowoff_blocks_positive_stage","full_4b_requires_non_price_evidence","hard_4c_thesis_break_routes_to_4c"],"residual_error_types_found":["generic_policy_headline_overcount","peripheral_theme_false_positive","price_only_local_4B_too_early"],"loop_contribution_label":"canonical_archetype_rule_candidate","do_not_propose_new_weight_delta":false}
```

### 25.7 narrative_only rows

```jsonl
{"row_type": "narrative_only", "case_id": "R11L11_C31_NO_CONFIRMED_4C_IN_TRIGGER_WINDOW", "symbol": "MULTI", "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "C31_POLICY_SUBSIDY_LEGISLATION_EVENT", "reason": "4C thesis-break not claimed at 2024 trigger because exploration result/economics confirmation was not yet available at trigger date", "price_source": "Songdaiki/stock-web", "usage": "not_weight_calibration"}
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
completed_round = R11
completed_loop = 11
next_round = R12
next_loop = 11
round_schedule_status = valid
round_sector_consistency = pass
```

## 28. Source Notes

Primary price source: `Songdaiki/stock-web`, `price_basis=tradable_raw`, `price_adjustment_status=raw_unadjusted_marcap`.

Non-price evidence sources are historical public reporting around 2024-06-03 and 2024-06-07. Reuters and WSJ were used only to identify the event evidence available at trigger time, not to scan current candidates. The row-level price calculations use Stock-Web OHLC anchor rows and schema formulas.

