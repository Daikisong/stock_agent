# E2R Stock-Web Historical Calibration / Sector-Archetype Residual Research Round

## 0. Research Metadata

```text
research_session = post_calibrated_sector_archetype_residual_research
mode = historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12
round = R9
loop = 30
large_sector_id = L3_BATTERY_EV_GREEN_MOBILITY
canonical_archetype_id = C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE
selection_mode = auto_coverage_gap_fill
output_format = one_standalone_markdown_file
production_scoring_changed = false
shadow_weight_only = true
stock_agent_code_access_allowed = false
stock_agent_code_patch_allowed = false
stock_web_price_atlas_access_required = true
```

This file is not a live candidate scan and not an investment recommendation. It is a historical calibration artifact for the sector/canonical-archetype residual ledger.

## 1. Current Calibrated Profile Assumption

```text
current_default_profile_proxy = e2r_2_1_stock_web_calibrated_proxy
rollback_reference_profile_id = e2r_2_0_baseline_reference

existing calibrated axes assumed:
- stage2_actionable_evidence_bonus = +2.0
- stage3_yellow_total_min = 75.0
- stage3_green_total_min = 87.0
- stage3_green_revision_min = 55.0
- stage3_cross_evidence_green_buffer = +1.5
- price_only_blowoff_blocks_positive_stage = true
- full_4b_requires_non_price_evidence = true
- hard_4c_thesis_break_routes_to_4c = true
```

The loop does not re-prove that Stage2 is earlier than Green. The question is narrower: **inside C29, when is mobility volume/mix evidence a real EPS-rerating bridge, and when is it just EV/optionality price heat?**

## 2. Round / Large Sector / Canonical Archetype Scope

```text
round = R9
large_sector_id = L3_BATTERY_EV_GREEN_MOBILITY
canonical_archetype_id = C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE
loop_objective = coverage_gap_fill; counterexample_mining; green_strictness_stress_test; 4B_non_price_requirement_stress_test; canonical_archetype_compression
```

Fine archetypes compressed into C29:

| fine_archetype_id | canonical mapping | mechanism |
|---|---|---|
| OEM_SUV_MIX_VOLUME_OPERATING_LEVERAGE | C29 | OEM volume recovery + SUV/RV mix + operating leverage |
| AUTO_LAMP_NA_MIX_MARGIN_BRIDGE | C29 | auto-parts customer volume + content/mix + margin bridge |
| EV_CHASSIS_ADAS_OPTIONALITY_WITHOUT_MARGIN_BRIDGE | C29 | EV/ADAS option narrative without confirmed margin bridge |
| EV_THERMAL_MODULE_OPTIONALITY_HIGH_MAE | C29 | EV thermal/module optionality with high-MAE path |

## 3. Previous Coverage / Duplicate Avoidance Check

Allowed stock_agent research artifact read: `data/e2r/calibration/md_registry.jsonl`.

Observed registry pattern in the accessible excerpt: many parsed loops already exist for R10/R11/R12/R13 and older R1 rounds, with repeated loop materialization visible in the registry. This loop therefore avoids rematerializing R1/R2 HBM/defense/grid cases and does not reuse the prior R8/C26 output from the immediately preceding chat turn.

```text
auto_selected_coverage_gap =
  R9/C29 mobility volume-margin operating leverage needed a split between:
  (a) real positive cases where volume/mix converted into margin/revision,
  (b) EV optionality cases where price and narrative moved before margin evidence.

duplicate_avoidance:
  - no stock_agent src/e2r code opened
  - no production patch written
  - new symbols in this loop: 000270, 005850, 204320, 011210
  - narrative-only blocker symbol: 009900
```

## 4. Stock-Web OHLC Input / Price Source Validation

| field | value |
|---|---|
| source | Songdaiki/stock-web |
| upstream source | FinanceData/marcap |
| source_name | FinanceData/marcap |
| manifest_path | atlas/manifest.json |
| schema_path | atlas/schema.json |
| universe_path | atlas/universe/all_symbols.csv |
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
| price_basis | tradable_raw |
| price_adjustment_status | raw_unadjusted_marcap |

Validation status: `usable_for_historical_calibration`.

The atlas is raw/unadjusted. Corporate-action candidate windows are blocked from calibration by default. All representative trigger windows below use tradable shards and avoid candidate corporate-action dates inside the 180D window, except the explicitly narrative-only 명신산업 case.

## 5. Historical Eligibility Gate

| case_id | symbol | entry_date | 180D forward available by manifest max_date | corporate-action overlap in 180D | calibration_usable |
|---|---:|---|---|---|---|
| C29-KIA-2020-MIX-OPLEV | 000270 | 2020-10-27 | yes | no | true |
| C29-SL-2024-Q1-LAMP-MIX | 005850 | 2024-05-17 | yes | no | true |
| C29-HLMANDO-2021-EV-CHASSIS-THEME | 204320 | 2021-01-08 | yes | no | true |
| C29-HYUNDAIWIA-2021-THERMAL-MODULE | 011210 | 2021-01-08 | yes | no | true |
| C29-MYEONGSHIN-2020-IPO-TESLA-NARR | 009900 | 2020-12-07 | yes | yes, 2021-06-18 | false |

## 6. Canonical Archetype Compression Map

C29 should not be a single “car stock went up” bucket. It is a gearbox with two shafts:

1. **Operating shaft**: volume route → mix/customer quality → gross/operating margin bridge → revision. This can promote to Stage2-Actionable and sometimes Stage3-Green.
2. **Option shaft**: EV/platform/thermal/ADAS/IPO narrative → relative strength → valuation repricing. This can be a Stage2 watch or tactical Stage2, but it should not become Green without margin/revision closure.

This loop compresses OEM, lamp/auto-parts, chassis/ADAS, and thermal-module paths into C29 while proposing a canonical guard for the second shaft.

## 7. Case Selection Summary

| case_id | symbol | company_name | case_type | positive_or_counterexample | fine_archetype_id | best_trigger | current_profile_verdict |
| --- | --- | --- | --- | --- | --- | --- | --- |
| C29-KIA-2020-MIX-OPLEV | 000270 | 기아 | structural_success | positive | OEM_SUV_MIX_VOLUME_OPERATING_LEVERAGE | T-C29-KIA-20201027-S2A | current_profile_correct |
| C29-SL-2024-Q1-LAMP-MIX | 005850 | 에스엘 | structural_success | positive | AUTO_LAMP_NA_MIX_MARGIN_BRIDGE | T-C29-SL-20240517-S2A | current_profile_correct |
| C29-HLMANDO-2021-EV-CHASSIS-THEME | 204320 | HL만도 | false_positive_green | counterexample | EV_CHASSIS_ADAS_OPTIONALITY_WITHOUT_MARGIN_BRIDGE | T-C29-HLMANDO-20210108-S2A | current_profile_false_positive |
| C29-HYUNDAIWIA-2021-THERMAL-MODULE | 011210 | 현대위아 | high_mae_success | counterexample | EV_THERMAL_MODULE_OPTIONALITY_HIGH_MAE | T-C29-HYUNDAIWIA-20210108-S2A | current_profile_too_early |
| C29-MYEONGSHIN-2020-IPO-TESLA-NARR | 009900 | 명신산업 | narrative_only | counterexample | EV_SUPPLIER_IPO_THEME_CORPORATE_ACTION_BLOCKED | T-C29-MYEONGSHIN-20201207-NARR | current_profile_data_insufficient |

## 8. Positive vs Counterexample Balance

```text
positive_case_count = 2
counterexample_count = 2
narrative_only_case_count = 1
calibration_usable_case_count = 4
new_independent_case_count = 4
new_independent_case_ratio = 1.00
```

Positive balance:
- 기아: OEM volume/mix and margin recovery became a genuine rerating bridge.
- 에스엘: lamps/electronics mix and HMG/North America volume produced a clean short-window rerating.

Counterexample balance:
- HL만도: EV/ADAS/chassis optionality was too narrative-heavy and suffered large MAE.
- 현대위아: EV thermal/module optionality eventually had MFE, but entry quality was poor because margin/revision were not yet closed.

Narrative-only:
- 명신산업: IPO/Tesla supplier path is useful narratively but blocked for weight calibration by stock-web corporate-action candidate window.

## 9. Evidence Source Map

| case_id | evidence family | Stage2 evidence | Stage3 evidence | red-team issue |
|---|---|---|---|---|
| C29-KIA-2020-MIX-OPLEV | quarterly earnings / OEM mix / volume recovery | RV/SUV mix, volume recovery, RS | margin bridge, revision visibility | event premium later mixed with core thesis |
| C29-SL-2024-Q1-LAMP-MIX | quarterly earnings / auto-parts mix | lamp/electronics mix, HMG/North America volume | confirmed margin bridge, financial visibility | later valuation ceiling/drawdown |
| C29-HLMANDO-2021-EV-CHASSIS-THEME | EV/ADAS/chassis optionality | RS, EV theme, customer option | weak/unknown margin bridge at trigger date | chip/volume risk and price-theme blowoff |
| C29-HYUNDAIWIA-2021-THERMAL-MODULE | EV thermal/module optionality | RS, EV thermal module option | insufficient confirmed revision at trigger date | high MAE and price-only local 4B |
| C29-MYEONGSHIN-2020-IPO-TESLA-NARR | IPO/Tesla supplier narrative | strong theme/RS | not calibrated | corporate-action blocked |

## 10. Price Data Source Map

| symbol | profile_path | first_date | last_date | trading_day_count | row_status_counts | corporate_action_candidate_dates |
| --- | --- | --- | --- | --- | --- | --- |
| 000270 | atlas/symbol_profiles/000/000270.json | 1995-05-02 | 2026-02-20 | 7743 | tradable_ohlcv=7743; non_tradable_zero_volume=22 | 1999-03-05, 1999-04-21, 1999-07-16 |
| 005850 | atlas/symbol_profiles/005/005850.json | 1995-05-02 | 2026-02-20 | 7594 | tradable_ohlcv=7594; non_tradable_zero_volume=171 | 2002-07-30, 2003-12-16, 2007-10-22, 2019-04-16 |
| 204320 | atlas/symbol_profiles/204/204320.json | 2014-10-06 | 2026-02-20 | 2790 | tradable_ohlcv=2790; non_tradable_zero_volume=3 | 2018-05-08 |
| 011210 | atlas/symbol_profiles/011/011210.json | 2011-02-21 | 2026-02-20 | 3689 | tradable_ohlcv=3689; non_tradable_zero_volume=0 | none |
| 009900 | atlas/symbol_profiles/009/009900.json | 2020-12-07 | 2026-02-20 | 1275 | tradable_ohlcv=1275; non_tradable_zero_volume=0 | 2021-06-18 |

## 11. Case-by-Case Trigger Grid

| trigger_id | case_id | symbol | trigger_type | trigger_date | entry_date | entry_price | MFE_90D_pct | MAE_90D_pct | MFE_180D_pct | MAE_180D_pct | trigger_outcome_label | current_profile_verdict | dedupe_for_aggregate |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| T-C29-KIA-20201027-S2A | C29-KIA-2020-MIX-OPLEV | 000270 | Stage2-Actionable | 2020-10-26 | 2020-10-27 | 52900 | 92.8 | -6.2 | 92.8 | -6.2 | structural_success | current_profile_correct | True |
| T-C29-KIA-20210120-GREEN | C29-KIA-2020-MIX-OPLEV | 000270 | Stage3-Green | 2021-01-20 | 2021-01-20 | 87600 | 16.4 | -15.2 | 16.4 | -15.2 | late_green | current_profile_too_late | False |
| T-C29-KIA-20210208-4B | C29-KIA-2020-MIX-OPLEV | 000270 | Stage4B | 2021-02-08 | 2021-02-08 | 86300 | 8.6 | -13.9 | 8.6 | -13.9 | 4B_overlay_success | current_profile_correct | False |
| T-C29-SL-20240517-S2A | C29-SL-2024-Q1-LAMP-MIX | 005850 | Stage2-Actionable | 2024-05-16 | 2024-05-17 | 35500 | 34.2 | -14.4 | 34.2 | -18.2 | structural_success_with_later_drawdown | current_profile_correct | True |
| T-C29-HLMANDO-20210108-S2A | C29-HLMANDO-2021-EV-CHASSIS-THEME | 204320 | Stage2-Actionable | 2021-01-08 | 2021-01-08 | 77400 | 15.0 | -26.4 | 15.0 | -26.4 | false_positive_green_or_failed_rerating | current_profile_false_positive | True |
| T-C29-HYUNDAIWIA-20210108-S2A | C29-HYUNDAIWIA-2021-THERMAL-MODULE | 011210 | Stage2-Actionable | 2021-01-08 | 2021-01-08 | 85900 | 26.3 | -21.2 | 33.9 | -21.2 | high_mae_success | current_profile_too_early | True |
| T-C29-HYUNDAIWIA-20210121-4BLOCAL | C29-HYUNDAIWIA-2021-THERMAL-MODULE | 011210 | Stage4B | 2021-01-21 | 2021-01-21 | 108500 | 0.0 | -37.6 | 6.0 | -37.6 | 4B_too_early | current_profile_4B_too_early | False |

## 12. Trigger-Level OHLC Backtest Tables

Representative trigger inclusion rule:

```text
aggregate_metric_inclusion =
  calibration_usable == true
  AND dedupe_for_aggregate == true
  AND aggregate_group_role == representative
  AND do_not_count_as_new_case != true
```

| symbol | representative trigger | entry | peak | MFE_30D | MAE_30D | MFE_90D | MAE_90D | MFE_180D | MAE_180D | outcome |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| 000270 | T-C29-KIA-20201027-S2A | 52,900 | 102,000 | 25.9% | -6.2% | 92.8% | -6.2% | 92.8% | -6.2% | strong positive |
| 005850 | T-C29-SL-20240517-S2A | 35,500 | 47,650 | 34.2% | -5.8% | 34.2% | -14.4% | 34.2% | -18.2% | positive with later drawdown |
| 204320 | T-C29-HLMANDO-20210108-S2A | 77,400 | 89,000 | 15.0% | -18.6% | 15.0% | -26.4% | 15.0% | -26.4% | false positive / failed rerating |
| 011210 | T-C29-HYUNDAIWIA-20210108-S2A | 85,900 | 115,000 | 26.3% | -15.4% | 26.3% | -21.2% | 33.9% | -21.2% | high-MAE success / too early |

Interpretation: C29 should not reward relative strength alone. The same road speed means different things depending on the engine. Kia and SL had an earnings engine; HL만도 and Hyundai Wia had narrative turbo first, torque later or not enough.

## 13. Current Calibrated Profile Stress Test

| question | answer |
|---|---|
| current calibrated profile likely judgment | It would correctly respect KIA/SL as Stage2/Yellow candidates, but may over-credit HL만도/현대위아 because RS + EV optionality can satisfy too much of Stage2. |
| actual MFE/MAE alignment | Positive cases had high MFE with tolerable early MAE. Counterexamples had high MAE or failed rerating despite initial price response. |
| Stage2 bonus too much or too little? | Too generous for C29 when evidence is EV optionality + RS only. Appropriate when volume route + customer/mix + margin bridge coexist. |
| Yellow threshold 75 | Kept. It is acceptable as long as C29 optionality-only names are capped/guarded. |
| Green threshold 87 / revision 55 | Strengthen within C29: Green should require margin_bridge_score and revision_score, not just RS/valuation repricing. |
| price-only blowoff guard | Strengthened. Hyundai Wia 2021-01-21 local 4B was price-only and too early versus full-window peak. |
| full 4B non-price requirement | Kept. Kia 2021-02-08 had event-premium unwind; Hyundai Wia local peak lacked non-price slowdown. |
| hard 4C routing | No hard 4C calibration in this loop; future C29 4C needs order cancellation / customer production cut / thesis-break evidence. |

Current profile verdict counts:

```text
current_profile_correct = 3 trigger rows
current_profile_too_late = 1 trigger row
current_profile_false_positive = 1 representative case
current_profile_too_early = 1 representative case
current_profile_4B_too_early = 1 overlay row
```

## 14. Stage2 / Yellow / Green Comparison

Kia provides the useful lateness audit:

```text
Stage2_Actionable entry_price = 52,900 on 2020-10-27
Stage3_Green proxy entry_price = 87,600 on 2021-01-20
full peak after Stage2 = 102,000
green_lateness_ratio = (87,600 - 52,900) / (102,000 - 52,900) = 0.71
```

A 0.71 ratio means Green appeared after most of the upside was already consumed. This does not mean Green threshold should be weakened globally. It means C29 needs a **Stage2-Actionable quality gate**: if volume route + mix/customer quality + margin bridge are already visible, earlier Stage2 can carry enough conviction without waiting for a late Green.

For HL만도 and Hyundai Wia, the opposite is true. Their early trigger had RS and EV optionality, but not enough durable margin/revision evidence. Here, Stage2 bonus should be clipped, not boosted.

## 15. 4B Local vs Full-window Timing Audit

| case | 4B trigger | local_peak_proximity | full_window_peak_proximity | verdict |
|---|---|---:|---:|---|
| 기아 | T-C29-KIA-20210208-4B | 0.68 | 0.68 | good event-premium 4B overlay, not a hard 4C |
| 현대위아 | T-C29-HYUNDAIWIA-20210121-4BLOCAL | 1.00 | 0.78 | price_only_local_4B_too_early |

Kia’s 4B overlay was about event-premium removal. The core OEM mix/margin thesis was not broken. Hyundai Wia’s local 4B was mostly price heat; full-window peak came later. This strengthens the existing rule: price-only local peaks should not become full 4B without non-price evidence.

## 16. 4C Protection Audit

No full hard-4C calibration row is proposed. The narrative-only 명신산업 row flags a future 4C research need, but corporate-action contamination blocks it from this quantitative loop.

```text
four_c_protection_label:
- Kia: thesis_break_watch_only
- Hyundai Wia: false_break for price-only local 4B
- HL만도: false_break / failed rerating, not hard 4C
```

## 17. Sector-Specific Rule Candidate

```text
rule_scope = sector_specific
large_sector_id = L3_BATTERY_EV_GREEN_MOBILITY
candidate = L3 mobility volume/mix margin bridge guard
```

Rule candidate:

```text
if large_sector_id == L3_BATTERY_EV_GREEN_MOBILITY
and canonical_archetype_id == C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE:

    if volume_route + customer_quality_or_mix + margin_bridge are all supported:
        add c29_volume_mix_margin_bridge_bonus = +1.0 to +3.0 shadow only

    if relative_strength + EV_optionality dominate
    and margin_bridge_score < 45
    and revision_score < 45:
        cap positive promotion at Watch/Stage2 or Stage2-Yellow
        do not allow Stage3-Green

    if price_only_local_peak and no non_price_4B_evidence:
        keep as local overlay only
        do_not_treat_as_full_4B = true
```

## 18. Canonical-Archetype Rule Candidate

```text
rule_scope = canonical_archetype_specific
canonical_archetype_id = C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE
preferred = true
```

Canonical rule candidate:

> In C29, evidence quality is not measured by “car/EV theme intensity.” It is measured by whether customer volume, mix/content, and margin bridge close the loop into revision. Relative strength is a speedometer, not the engine.

## 19. Before / After Backtest Comparison

| profile_id | profile_scope | profile_hypothesis | eligible_trigger_count | avg_MFE_90D_pct | avg_MAE_90D_pct | avg_MFE_180D_pct | avg_MAE_180D_pct | false_positive_rate | score_return_alignment_verdict |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| P0_e2r_2_1_stock_web_calibrated_proxy | current_proxy | Global calibrated profile without C29-specific mix/margin guard. | 4 | 42.1 | -17.1 | 44.0 | -18.0 | 2/4 | mixed; too permissive for EV optionality cases |
| P0b_e2r_2_0_baseline_reference | rollback_reference | Earlier baseline, less strict on price-only / non-price 4B requirements. | 4 | 34.0 | -21.0 | 37.0 | -22.5 | 2/4+ | worse; can chase local EV spikes |
| P1_L3_sector_specific_candidate | sector_specific | L3 mobility needs volume/mix/margin bridge before promotion, not just EV option narrative. | 2 | 63.5 | -10.3 | 63.5 | -12.2 | 0/2 selected | improved |
| P2_C29_canonical_archetype_candidate | canonical_archetype_specific | Within C29, distinguish true operating leverage from EV/local blowoff optionality. | 2 | 63.5 | -10.3 | 63.5 | -12.2 | 0/2 selected | best for this loop |
| P3_counterexample_guard_profile | canonical_archetype_specific | Block Green where RS and EV optionality dominate but contract/revision/margin bridge are weak. | 2 | 63.5 | -10.3 | 63.5 | -12.2 | 0/2 selected | guard works; not enough for global promotion |

## 20. Score-Return Alignment Matrix

| symbol | current proxy label | proposed shadow label | MFE_90D | MAE_90D | alignment |
|---:|---|---|---:|---:|---|
| 000270 | Stage2-Actionable | Stage3-Yellow candidate | 92.8% | -6.2% | current correct; Green late |
| 005850 | Stage3-Yellow | Stage3-Green candidate | 34.2% | -14.4% | proposed C29 margin bridge helps |
| 204320 | Stage2-Actionable / possible false Green | Watch/Stage2 cap | 15.0% | -26.4% | proposed guard improves |
| 011210 | Stage2-Actionable too early | Watch/Stage2 cap until margin/revision | 26.3% | -21.2% | proposed guard reduces high-MAE entry |

## 21. Coverage Matrix

| large_sector_id | canonical_archetype_id | fine_archetype_id | positive_case_count | counterexample_count | 4B_case_count | 4C_case_count | new_independent_case_count | reused_case_count | calibration_usable_trigger_count | representative_trigger_count | current_profile_error_count | sector_rule_candidate | canonical_rule_candidate | coverage_gap_after_this_loop |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| L3_BATTERY_EV_GREEN_MOBILITY | C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE | OEM_SUV_MIX_VOLUME_OPERATING_LEVERAGE; AUTO_LAMP_NA_MIX_MARGIN_BRIDGE; EV_CHASSIS_ADAS_OPTIONALITY_WITHOUT_MARGIN_BRIDGE; EV_THERMAL_MODULE_OPTIONALITY_HIGH_MAE | 2 | 2 | 2 | 0 | 4 | 0 | 7 | 4 | 3 | True | True | full 4C thesis-break cases still missing; more supplier counterexamples needed outside 2021 EV spike |

## 22. Residual Contribution Summary

```text
new_independent_case_count: 4
reused_case_count: 0
reused_case_ids: []
new_symbol_count: 4
same_archetype_new_symbol_count: 4
same_archetype_new_trigger_family_count: 4
new_canonical_archetype_count: 0
new_fine_archetype_count: 4
new_trigger_family_count: 4

tested_existing_calibrated_axes:
- stage2_actionable_evidence_bonus
- stage3_green_revision_min
- price_only_blowoff_blocks_positive_stage
- full_4b_requires_non_price_evidence

residual_error_types_found:
- EV optionality false positive
- high-MAE success
- price-only local 4B too early

new_axis_proposed:
- c29_volume_mix_margin_bridge_bonus
- c29_ev_optionality_without_margin_revision_guard
- c29_price_only_local_4b_overlay_guard

existing_axis_strengthened:
- stage3_green_revision_min in C29 only
- price_only_blowoff_blocks_positive_stage
- full_4b_requires_non_price_evidence

existing_axis_weakened:
- none

existing_axis_kept:
- stage2_actionable_evidence_bonus, but only after C29 evidence quality split

sector_specific_rule_candidate: true
canonical_archetype_rule_candidate: true
no_new_signal_reason: null

loop_contribution_label: canonical_archetype_rule_candidate
do_not_propose_new_weight_delta: false
```

## 23. Validation Scope / Non-Validation Scope

Validated:
- stock-web manifest max date and price basis
- symbol profile existence and corporate-action candidate status
- actual OHLC entries for representative and comparison triggers
- 30D/90D/180D MFE/MAE using stock-web tradable rows
- C29 positive/counterexample balance
- 4B local vs full-window split for Kia and Hyundai Wia

Not validated:
- no live candidate discovery
- no current watchlist
- no brokerage/API integration
- no production score change
- no stock_agent src/e2r inspection
- no hard 4C quantitative protection row

## 24. Shadow Weight Calibration

```csv
row_type,axis,scope,large_sector_id,canonical_archetype_id,baseline_value,tested_value,delta,reason,backtest_effect,trigger_ids,calibration_usable_count,new_independent_case_count,counterexample_count,confidence,proposal_type,notes
shadow_weight,c29_volume_mix_margin_bridge_bonus,canonical_archetype_specific,L3_BATTERY_EV_GREEN_MOBILITY,C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE,0,1,+1,Kia and SL cases show better score-return alignment when volume route + customer/mix + margin bridge are combined.,selected positives avg MFE90 63.5 vs P0 all 42.1; MAE90 improves -17.1 to -10.3,T-C29-KIA-20201027-S2A|T-C29-SL-20240517-S2A,4,4,2,medium,canonical_shadow_only,not production; post-calibrated residual
shadow_weight,c29_ev_optionality_without_margin_revision_guard,canonical_archetype_specific,L3_BATTERY_EV_GREEN_MOBILITY,C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE,0,-2,-2 or Green cap,HL만도 and 현대위아 show high MAE when EV optionality/RS precede margin and revision confirmation.,blocks 2/2 counterexamples from Green promotion while preserving KIA/SL positives,T-C29-HLMANDO-20210108-S2A|T-C29-HYUNDAIWIA-20210108-S2A,4,4,2,medium,canonical_shadow_only,sector/archetype guard only
shadow_weight,c29_price_only_local_4b_overlay_guard,canonical_archetype_specific,L3_BATTERY_EV_GREEN_MOBILITY,C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE,full_4b_requires_non_price_evidence=true,kept and localized,0; strengthen interpretation,Hyundai Wia local 4B at 2021-01-21 was price-only and too early versus full-window peak; Kia 2021-02-08 had event-premium non-price overlay.,distinguishes event premium 4B from price-only local peak,T-C29-KIA-20210208-4B|T-C29-HYUNDAIWIA-20210121-4BLOCAL,4,4,2,medium,canonical_shadow_only,"existing axis strengthened, not new global rule"
```

## 25. Machine-Readable Rows

```jsonl
{"row_type": "price_source_validation", "source": "Songdaiki/stock-web", "source_url": "https://github.com/Songdaiki/stock-web", "manifest_path": "atlas/manifest.json", "schema_path": "atlas/schema.json", "universe_path": "atlas/universe/all_symbols.csv", "manifest_max_date": "2026-02-20", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "raw_shard_root": "atlas/ohlcv_raw_by_symbol_year", "validation_status": "usable_for_historical_calibration"}
{"row_type": "case", "case_id": "C29-KIA-2020-MIX-OPLEV", "symbol": "000270", "company_name": "기아", "round": "R9", "loop": "30", "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE", "fine_archetype_id": "OEM_SUV_MIX_VOLUME_OPERATING_LEVERAGE", "case_type": "structural_success", "positive_or_counterexample": "positive", "best_trigger": "T-C29-KIA-20201027-S2A", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "Stage2-Actionable entry had large 90D/180D MFE with contained MAE; Green appeared materially late.", "current_profile_verdict": "current_profile_correct", "price_source": "Songdaiki/stock-web", "notes": "2020년 하반기 RV/SUV mix와 판매 회복이 비용 충격 이후 operating leverage로 연결된 대표 positive. 2021년 1~2월 EV/Apple event premium이 붙었지만 Stage2 본체는 volume/mix/margin bridge였음."}
{"row_type": "case", "case_id": "C29-SL-2024-Q1-LAMP-MIX", "symbol": "005850", "company_name": "에스엘", "round": "R9", "loop": "30", "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE", "fine_archetype_id": "AUTO_LAMP_NA_MIX_MARGIN_BRIDGE", "case_type": "structural_success", "positive_or_counterexample": "positive", "best_trigger": "T-C29-SL-20240517-S2A", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "Q1-earnings trigger produced strong 30D/90D MFE; later drawdown argues for 4B overlay after price+revision fatigue.", "current_profile_verdict": "current_profile_correct", "price_source": "Songdaiki/stock-web", "notes": "램프/전장 믹스와 북미·현대기아 물량 회복이 실적 확인과 함께 주가로 반영된 positive. 단, 뒤따른 drawdown은 auto parts의 valuation multiple ceiling을 보여줌."}
{"row_type": "case", "case_id": "C29-HLMANDO-2021-EV-CHASSIS-THEME", "symbol": "204320", "company_name": "HL만도", "round": "R9", "loop": "30", "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE", "fine_archetype_id": "EV_CHASSIS_ADAS_OPTIONALITY_WITHOUT_MARGIN_BRIDGE", "case_type": "false_positive_green", "positive_or_counterexample": "counterexample", "best_trigger": "T-C29-HLMANDO-20210108-S2A", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "Positive MFE existed briefly, but the drawdown profile was too large for confirmed Stage3.", "current_profile_verdict": "current_profile_false_positive", "price_source": "Songdaiki/stock-web", "notes": "E-GMP/EV/ADAS optionality와 고객 다변화 narrative는 강했지만, 2021년 초 entry 이후 chip shortage와 margin bridge 부재가 MAE를 크게 키움. C29에서 pure optionality를 Green까지 올리는 것을 막아야 하는 counterexample."}
{"row_type": "case", "case_id": "C29-HYUNDAIWIA-2021-THERMAL-MODULE", "symbol": "011210", "company_name": "현대위아", "round": "R9", "loop": "30", "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE", "fine_archetype_id": "EV_THERMAL_MODULE_OPTIONALITY_HIGH_MAE", "case_type": "high_mae_success", "positive_or_counterexample": "counterexample", "best_trigger": "T-C29-HYUNDAIWIA-20210108-S2A", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "180D outcome was not bad, but early drawdown and price-only local 4B behavior weaken immediate Green promotion.", "current_profile_verdict": "current_profile_too_early", "price_source": "Songdaiki/stock-web", "notes": "전기차 열관리/모듈 optionality가 빠르게 가격에 반영됐지만, 초기 evidence는 capacity/order/margin bridge보다 narrative가 앞섰다. 180D MFE는 양호하나, early entry MAE가 크므로 current profile의 Stage2 bonus가 과할 수 있는 stress case."}
{"row_type": "case", "case_id": "C29-MYEONGSHIN-2020-IPO-TESLA-NARR", "symbol": "009900", "company_name": "명신산업", "round": "R9", "loop": "30", "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE", "fine_archetype_id": "EV_SUPPLIER_IPO_THEME_CORPORATE_ACTION_BLOCKED", "case_type": "narrative_only", "positive_or_counterexample": "counterexample", "best_trigger": "T-C29-MYEONGSHIN-20201207-NARR", "calibration_usable": false, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 0.0, "score_price_alignment": "Narrative-only. Not used for weight calibration.", "current_profile_verdict": "current_profile_data_insufficient", "price_source": "Songdaiki/stock-web", "notes": "상장 직후 EV/Tesla supplier narrative가 강했지만 stock-web profile상 2021-06-18 corporate-action candidate가 entry~D+180 window에 걸려 quantitative calibration에서는 제외."}
{"row_type": "trigger", "trigger_id": "T-C29-KIA-20201027-S2A", "case_id": "C29-KIA-2020-MIX-OPLEV", "symbol": "000270", "company_name": "기아", "round": "R9", "loop": "30", "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE", "fine_archetype_id": "OEM_SUV_MIX_VOLUME_OPERATING_LEVERAGE", "sector": "mobility/auto OEM and auto parts", "primary_archetype": "mobility volume margin operating leverage", "loop_objective": "coverage_gap_fill; counterexample_mining; green_strictness_stress_test; 4B_non_price_requirement_stress_test; canonical_archetype_compression", "trigger_type": "Stage2-Actionable", "trigger_date": "2020-10-26", "evidence_available_at_that_date": "2020년 3Q 실적/판매 회복 후 비용 충격을 넘는 RV/SUV mix와 volume recovery가 확인된 구간.", "evidence_source": "public quarterly earnings / IR-news evidence family: 3Q20 results, RV/SUV mix, US/Korea volume recovery", "stage2_evidence_fields": ["public_event_or_disclosure", "relative_strength", "capacity_or_volume_route", "early_revision_signal"], "stage3_evidence_fields": ["margin_bridge", "financial_visibility"], "stage4b_evidence_fields": [], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/000/000270/2020.csv", "profile_path": "atlas/symbol_profiles/000/000270.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "entry_date": "2020-10-27", "entry_price": 52900, "MFE_30D_pct": 25.9, "MFE_90D_pct": 92.8, "MFE_180D_pct": 92.8, "MFE_1Y_pct": 92.8, "MFE_2Y_pct": 92.8, "MAE_30D_pct": -6.2, "MAE_90D_pct": -6.2, "MAE_180D_pct": -6.2, "MAE_1Y_pct": -6.2, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2021-02-03", "peak_price": 102000, "drawdown_after_peak_pct": -27.2, "green_lateness_ratio": "0.71 when compared with 2021-01-20 Green proxy", "four_b_local_peak_proximity": null, "four_b_full_window_peak_proximity": null, "four_b_timing_verdict": "not_applicable", "four_b_evidence_type": [], "four_c_protection_label": "not_applicable", "trigger_outcome_label": "structural_success", "current_profile_verdict": "current_profile_correct", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window", "same_entry_group_id": "G-C29-KIA-20201027", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false}
{"row_type": "trigger", "trigger_id": "T-C29-KIA-20210120-GREEN", "case_id": "C29-KIA-2020-MIX-OPLEV", "symbol": "000270", "company_name": "기아", "round": "R9", "loop": "30", "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE", "fine_archetype_id": "OEM_SUV_MIX_VOLUME_OPERATING_LEVERAGE", "sector": "mobility/auto OEM and auto parts", "primary_archetype": "mobility volume margin operating leverage", "loop_objective": "coverage_gap_fill; counterexample_mining; green_strictness_stress_test; 4B_non_price_requirement_stress_test; canonical_archetype_compression", "trigger_type": "Stage3-Green", "trigger_date": "2021-01-20", "evidence_available_at_that_date": "강한 주가 반응과 EV/platform premium이 이미 붙은 뒤의 Green proxy. upside capture가 Stage2 대비 늦음.", "evidence_source": "public market/earnings-news family: EV/platform premium, margin visibility after 4Q run-up", "stage2_evidence_fields": ["relative_strength"], "stage3_evidence_fields": ["confirmed_revision", "multiple_public_sources", "financial_visibility"], "stage4b_evidence_fields": [], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/000/000270/2021.csv", "profile_path": "atlas/symbol_profiles/000/000270.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "entry_date": "2021-01-20", "entry_price": 87600, "MFE_30D_pct": 16.4, "MFE_90D_pct": 16.4, "MFE_180D_pct": 16.4, "MFE_1Y_pct": 16.4, "MFE_2Y_pct": 16.4, "MAE_30D_pct": -15.2, "MAE_90D_pct": -15.2, "MAE_180D_pct": -15.2, "MAE_1Y_pct": -15.2, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2021-02-03", "peak_price": 102000, "drawdown_after_peak_pct": -27.2, "green_lateness_ratio": 0.71, "four_b_local_peak_proximity": null, "four_b_full_window_peak_proximity": null, "four_b_timing_verdict": "not_applicable", "four_b_evidence_type": [], "four_c_protection_label": "not_applicable", "trigger_outcome_label": "late_green", "current_profile_verdict": "current_profile_too_late", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window", "same_entry_group_id": "G-C29-KIA-20210120", "dedupe_for_aggregate": false, "aggregate_group_role": "label_comparison_only", "is_new_independent_case": true, "reuse_reason": "same_case_green_lateness_comparison", "independent_evidence_weight": 0.25, "do_not_count_as_new_case": false}
{"row_type": "trigger", "trigger_id": "T-C29-KIA-20210208-4B", "case_id": "C29-KIA-2020-MIX-OPLEV", "symbol": "000270", "company_name": "기아", "round": "R9", "loop": "30", "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE", "fine_archetype_id": "OEM_SUV_MIX_VOLUME_OPERATING_LEVERAGE", "sector": "mobility/auto OEM and auto parts", "primary_archetype": "mobility volume margin operating leverage", "loop_objective": "coverage_gap_fill; counterexample_mining; green_strictness_stress_test; 4B_non_price_requirement_stress_test; canonical_archetype_compression", "trigger_type": "Stage4B", "trigger_date": "2021-02-08", "evidence_available_at_that_date": "Apple-car/event premium unwind after peak; core volume/mix thesis not broken, but event premium compression was a valid overlay risk.", "evidence_source": "public event-risk/news family: Apple-car speculation unwind, event premium reset", "stage2_evidence_fields": [], "stage3_evidence_fields": [], "stage4b_evidence_fields": ["explicit_event_cap", "positioning_overheat", "control_premium_or_event_premium"], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/000/000270/2021.csv", "profile_path": "atlas/symbol_profiles/000/000270.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "entry_date": "2021-02-08", "entry_price": 86300, "MFE_30D_pct": 0.9, "MFE_90D_pct": 8.6, "MFE_180D_pct": 8.6, "MFE_1Y_pct": 8.6, "MFE_2Y_pct": 8.6, "MAE_30D_pct": -13.9, "MAE_90D_pct": -13.9, "MAE_180D_pct": -13.9, "MAE_1Y_pct": -13.9, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2021-06-24", "peak_price": 93700, "drawdown_after_peak_pct": -27.2, "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": 0.68, "four_b_full_window_peak_proximity": 0.68, "four_b_timing_verdict": "good_full_window_4B_timing_for_event_premium_not_core_thesis_break", "four_b_evidence_type": ["positioning_overheat", "control_premium_or_event_premium"], "four_c_protection_label": "thesis_break_watch_only", "trigger_outcome_label": "4B_overlay_success", "current_profile_verdict": "current_profile_correct", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window", "same_entry_group_id": "G-C29-KIA-20210208", "dedupe_for_aggregate": false, "aggregate_group_role": "4B_overlay_only", "is_new_independent_case": true, "reuse_reason": "same_case_4b_timing_overlay", "independent_evidence_weight": 0.25, "do_not_count_as_new_case": false}
{"row_type": "trigger", "trigger_id": "T-C29-SL-20240517-S2A", "case_id": "C29-SL-2024-Q1-LAMP-MIX", "symbol": "005850", "company_name": "에스엘", "round": "R9", "loop": "30", "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE", "fine_archetype_id": "AUTO_LAMP_NA_MIX_MARGIN_BRIDGE", "sector": "mobility/auto OEM and auto parts", "primary_archetype": "mobility volume margin operating leverage", "loop_objective": "coverage_gap_fill; counterexample_mining; green_strictness_stress_test; 4B_non_price_requirement_stress_test; canonical_archetype_compression", "trigger_type": "Stage2-Actionable", "trigger_date": "2024-05-16", "evidence_available_at_that_date": "1Q24 실적 확인 후 램프/전장 mix, 북미/현대기아 물량, 영업레버리지 조합이 Stage2-Actionable로 승격된 구간.", "evidence_source": "public quarterly earnings / analyst-note evidence family: Q1 2024 results, lighting/electronics mix, North America and HMG volume", "stage2_evidence_fields": ["public_event_or_disclosure", "customer_or_order_quality", "capacity_or_volume_route", "early_revision_signal"], "stage3_evidence_fields": ["confirmed_revision", "margin_bridge", "financial_visibility", "low_red_team_risk"], "stage4b_evidence_fields": [], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/005/005850/2024.csv", "profile_path": "atlas/symbol_profiles/005/005850.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "entry_date": "2024-05-17", "entry_price": 35500, "MFE_30D_pct": 34.2, "MFE_90D_pct": 34.2, "MFE_180D_pct": 34.2, "MFE_1Y_pct": 34.2, "MFE_2Y_pct": null, "MAE_30D_pct": -5.8, "MAE_90D_pct": -14.4, "MAE_180D_pct": -18.2, "MAE_1Y_pct": -24.4, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2024-06-17", "peak_price": 47650, "drawdown_after_peak_pct": -39.0, "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": null, "four_b_full_window_peak_proximity": null, "four_b_timing_verdict": "not_applicable", "four_b_evidence_type": [], "four_c_protection_label": "not_applicable", "trigger_outcome_label": "structural_success_with_later_drawdown", "current_profile_verdict": "current_profile_correct", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window", "same_entry_group_id": "G-C29-SL-20240517", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false}
{"row_type": "trigger", "trigger_id": "T-C29-HLMANDO-20210108-S2A", "case_id": "C29-HLMANDO-2021-EV-CHASSIS-THEME", "symbol": "204320", "company_name": "HL만도", "round": "R9", "loop": "30", "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE", "fine_archetype_id": "EV_CHASSIS_ADAS_OPTIONALITY_WITHOUT_MARGIN_BRIDGE", "sector": "mobility/auto OEM and auto parts", "primary_archetype": "mobility volume margin operating leverage", "loop_objective": "coverage_gap_fill; counterexample_mining; green_strictness_stress_test; 4B_non_price_requirement_stress_test; canonical_archetype_compression", "trigger_type": "Stage2-Actionable", "trigger_date": "2021-01-08", "evidence_available_at_that_date": "E-GMP/ADAS/EV chassis optionality and relative strength were visible, but margin bridge and revision confirmation were not yet durable.", "evidence_source": "public theme/news family: E-GMP, EV chassis/ADAS optionality; no sufficient margin-bridge confirmation at trigger date", "stage2_evidence_fields": ["public_event_or_disclosure", "relative_strength", "policy_or_regulatory_optionality"], "stage3_evidence_fields": ["unknown_or_not_supported: confirmed_revision", "unknown_or_not_supported: margin_bridge"], "stage4b_evidence_fields": ["positioning_overheat"], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/204/204320/2021.csv", "profile_path": "atlas/symbol_profiles/204/204320.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "entry_date": "2021-01-08", "entry_price": 77400, "MFE_30D_pct": 15.0, "MFE_90D_pct": 15.0, "MFE_180D_pct": 15.0, "MFE_1Y_pct": 15.0, "MFE_2Y_pct": null, "MAE_30D_pct": -18.6, "MAE_90D_pct": -26.4, "MAE_180D_pct": -26.4, "MAE_1Y_pct": -26.4, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2021-01-11", "peak_price": 89000, "drawdown_after_peak_pct": -36.0, "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": null, "four_b_full_window_peak_proximity": null, "four_b_timing_verdict": "price_only_theme_peak_without_full_4B_non_price_confirmation", "four_b_evidence_type": ["price_only", "positioning_overheat"], "four_c_protection_label": "false_break", "trigger_outcome_label": "false_positive_green_or_failed_rerating", "current_profile_verdict": "current_profile_false_positive", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window", "same_entry_group_id": "G-C29-HLMANDO-20210108", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false}
{"row_type": "trigger", "trigger_id": "T-C29-HYUNDAIWIA-20210108-S2A", "case_id": "C29-HYUNDAIWIA-2021-THERMAL-MODULE", "symbol": "011210", "company_name": "현대위아", "round": "R9", "loop": "30", "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE", "fine_archetype_id": "EV_THERMAL_MODULE_OPTIONALITY_HIGH_MAE", "sector": "mobility/auto OEM and auto parts", "primary_archetype": "mobility volume margin operating leverage", "loop_objective": "coverage_gap_fill; counterexample_mining; green_strictness_stress_test; 4B_non_price_requirement_stress_test; canonical_archetype_compression", "trigger_type": "Stage2-Actionable", "trigger_date": "2021-01-08", "evidence_available_at_that_date": "EV thermal management/module optionality and strong RS were visible, but confirmed orders/margin bridge were not enough for immediate Green.", "evidence_source": "public theme/news family: EV thermal management, E-GMP module optionality, relative strength", "stage2_evidence_fields": ["public_event_or_disclosure", "relative_strength", "policy_or_regulatory_optionality"], "stage3_evidence_fields": ["unknown_or_not_supported: confirmed_revision", "unknown_or_not_supported: durable_customer_confirmation"], "stage4b_evidence_fields": ["price_only_local_peak", "positioning_overheat"], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/011/011210/2021.csv", "profile_path": "atlas/symbol_profiles/011/011210.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "entry_date": "2021-01-08", "entry_price": 85900, "MFE_30D_pct": 26.3, "MFE_90D_pct": 26.3, "MFE_180D_pct": 33.9, "MFE_1Y_pct": 33.9, "MFE_2Y_pct": null, "MAE_30D_pct": -15.4, "MAE_90D_pct": -21.2, "MAE_180D_pct": -21.2, "MAE_1Y_pct": -21.2, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2021-06-24", "peak_price": 115000, "drawdown_after_peak_pct": -41.1, "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": null, "four_b_full_window_peak_proximity": null, "four_b_timing_verdict": "not_applicable", "four_b_evidence_type": ["price_only", "positioning_overheat"], "four_c_protection_label": "thesis_break_watch_only", "trigger_outcome_label": "high_mae_success", "current_profile_verdict": "current_profile_too_early", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window", "same_entry_group_id": "G-C29-HYUNDAIWIA-20210108", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false}
{"row_type": "trigger", "trigger_id": "T-C29-HYUNDAIWIA-20210121-4BLOCAL", "case_id": "C29-HYUNDAIWIA-2021-THERMAL-MODULE", "symbol": "011210", "company_name": "현대위아", "round": "R9", "loop": "30", "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE", "fine_archetype_id": "EV_THERMAL_MODULE_OPTIONALITY_HIGH_MAE", "sector": "mobility/auto OEM and auto parts", "primary_archetype": "mobility volume margin operating leverage", "loop_objective": "coverage_gap_fill; counterexample_mining; green_strictness_stress_test; 4B_non_price_requirement_stress_test; canonical_archetype_compression", "trigger_type": "Stage4B", "trigger_date": "2021-01-21", "evidence_available_at_that_date": "local peak was mostly price/positioning. Non-price 4B evidence was insufficient, and full-window peak came later.", "evidence_source": "public market-price/euphoria family: local blowoff without non-price slowdown evidence", "stage2_evidence_fields": [], "stage3_evidence_fields": [], "stage4b_evidence_fields": ["price_only_local_peak", "positioning_overheat"], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/011/011210/2021.csv", "profile_path": "atlas/symbol_profiles/011/011210.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "entry_date": "2021-01-21", "entry_price": 108500, "MFE_30D_pct": 0.0, "MFE_90D_pct": 0.0, "MFE_180D_pct": 6.0, "MFE_1Y_pct": 6.0, "MFE_2Y_pct": null, "MAE_30D_pct": -30.3, "MAE_90D_pct": -37.6, "MAE_180D_pct": -37.6, "MAE_1Y_pct": -37.6, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2021-06-24", "peak_price": 115000, "drawdown_after_peak_pct": -41.1, "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": 1.0, "four_b_full_window_peak_proximity": 0.78, "four_b_timing_verdict": "price_only_local_4B_too_early", "four_b_evidence_type": ["price_only", "positioning_overheat"], "four_c_protection_label": "false_break", "trigger_outcome_label": "4B_too_early", "current_profile_verdict": "current_profile_4B_too_early", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window", "same_entry_group_id": "G-C29-HYUNDAIWIA-20210121", "dedupe_for_aggregate": false, "aggregate_group_role": "4B_overlay_only", "is_new_independent_case": true, "reuse_reason": "same_case_4b_local_vs_full_window_audit", "independent_evidence_weight": 0.25, "do_not_count_as_new_case": false}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "C29-KIA-2020-MIX-OPLEV", "trigger_id": "T-C29-KIA-20201027-S2A", "symbol": "000270", "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE", "raw_component_scores_before": {"contract_score": 20, "backlog_visibility_score": 30, "margin_bridge_score": 62, "revision_score": 50, "relative_strength_score": 72, "customer_quality_score": 65, "policy_or_regulatory_score": 15, "valuation_repricing_score": 30, "execution_risk_score": 25, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_before": 80, "stage_label_before": "Stage2-Actionable", "raw_component_scores_after": {"contract_score": 20, "backlog_visibility_score": 30, "margin_bridge_score": 67, "revision_score": 53, "relative_strength_score": 72, "customer_quality_score": 65, "policy_or_regulatory_score": 15, "valuation_repricing_score": 30, "execution_risk_score": 25, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_after": 83, "stage_label_after": "Stage3-Yellow", "changed_components": ["margin_bridge_score", "revision_score", "customer_quality_score"], "component_delta_explanation": "add +3 C29 volume/mix/margin bridge combo", "MFE_90D_pct": 92.8, "MAE_90D_pct": -6.2, "score_return_alignment_label": "aligned", "current_profile_verdict": "current_profile_correct"}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "C29-SL-2024-Q1-LAMP-MIX", "trigger_id": "T-C29-SL-20240517-S2A", "symbol": "005850", "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE", "raw_component_scores_before": {"contract_score": 35, "backlog_visibility_score": 45, "margin_bridge_score": 70, "revision_score": 63, "relative_strength_score": 68, "customer_quality_score": 70, "policy_or_regulatory_score": 10, "valuation_repricing_score": 35, "execution_risk_score": 30, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_before": 84, "stage_label_before": "Stage3-Yellow", "raw_component_scores_after": {"contract_score": 35, "backlog_visibility_score": 45, "margin_bridge_score": 75, "revision_score": 66, "relative_strength_score": 68, "customer_quality_score": 70, "policy_or_regulatory_score": 10, "valuation_repricing_score": 35, "execution_risk_score": 30, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_after": 89, "stage_label_after": "Stage3-Green", "changed_components": ["margin_bridge_score", "revision_score", "customer_quality_score"], "component_delta_explanation": "add +5 confirmed margin bridge and customer/volume mix", "MFE_90D_pct": 34.2, "MAE_90D_pct": -14.4, "score_return_alignment_label": "aligned", "current_profile_verdict": "current_profile_correct"}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "C29-HLMANDO-2021-EV-CHASSIS-THEME", "trigger_id": "T-C29-HLMANDO-20210108-S2A", "symbol": "204320", "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE", "raw_component_scores_before": {"contract_score": 20, "backlog_visibility_score": 25, "margin_bridge_score": 20, "revision_score": 25, "relative_strength_score": 80, "customer_quality_score": 58, "policy_or_regulatory_score": 55, "valuation_repricing_score": 60, "execution_risk_score": 65, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_before": 78, "stage_label_before": "Stage2-Actionable", "raw_component_scores_after": {"contract_score": 20, "backlog_visibility_score": 25, "margin_bridge_score": 15, "revision_score": 25, "relative_strength_score": 80, "customer_quality_score": 58, "policy_or_regulatory_score": 55, "valuation_repricing_score": 60, "execution_risk_score": 75, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_after": 67, "stage_label_after": "Watch/Stage2", "changed_components": ["execution_risk_score", "margin_bridge_score", "revision_score"], "component_delta_explanation": "apply -11 EV optionality without margin/revision guard", "MFE_90D_pct": 15.0, "MAE_90D_pct": -26.4, "score_return_alignment_label": "de_risked_counterexample", "current_profile_verdict": "current_profile_false_positive"}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "C29-HYUNDAIWIA-2021-THERMAL-MODULE", "trigger_id": "T-C29-HYUNDAIWIA-20210108-S2A", "symbol": "011210", "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE", "raw_component_scores_before": {"contract_score": 20, "backlog_visibility_score": 25, "margin_bridge_score": 20, "revision_score": 25, "relative_strength_score": 82, "customer_quality_score": 55, "policy_or_regulatory_score": 58, "valuation_repricing_score": 62, "execution_risk_score": 70, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_before": 80, "stage_label_before": "Stage2-Actionable", "raw_component_scores_after": {"contract_score": 20, "backlog_visibility_score": 25, "margin_bridge_score": 15, "revision_score": 25, "relative_strength_score": 82, "customer_quality_score": 55, "policy_or_regulatory_score": 58, "valuation_repricing_score": 62, "execution_risk_score": 80, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_after": 70, "stage_label_after": "Watch/Stage2", "changed_components": ["execution_risk_score", "margin_bridge_score", "revision_score"], "component_delta_explanation": "apply -10 price/optionality high-MAE guard", "MFE_90D_pct": 26.3, "MAE_90D_pct": -21.2, "score_return_alignment_label": "de_risked_counterexample", "current_profile_verdict": "current_profile_too_early"}
{"row_type": "narrative_only", "case_id": "C29-MYEONGSHIN-2020-IPO-TESLA-NARR", "symbol": "009900", "company_name": "명신산업", "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE", "reason": "corporate_action_contaminated_180D_window: profile lists 2021-06-18 corporate_action_candidate inside IPO/Tesla supplier event window", "price_source": "Songdaiki/stock-web", "usage": "not_weight_calibration", "profile_path": "atlas/symbol_profiles/009/009900.json"}
{"row_type": "residual_contribution", "round": "R9", "loop": "30", "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE", "new_independent_case_count": 4, "reused_case_count": 0, "new_symbol_count": 4, "same_archetype_new_symbol_count": 4, "same_archetype_new_trigger_family_count": 4, "new_canonical_archetype_count": 0, "new_trigger_family_count": 4, "tested_existing_calibrated_axes": ["stage2_actionable_evidence_bonus", "stage3_green_revision_min", "price_only_blowoff_blocks_positive_stage", "full_4b_requires_non_price_evidence"], "residual_error_types_found": ["EV optionality false positive", "high-MAE success", "price-only local 4B too early"], "loop_contribution_label": "canonical_archetype_rule_candidate", "do_not_propose_new_weight_delta": false, "auto_selected_coverage_gap": "R9/C29 mobility volume-margin evidence split: positive OEM/auto-parts operating leverage vs EV optionality/theme counterexamples"}
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
next_round = R9
next_loop_hint = C29 holdout validation with additional suppliers or C14 EV demand slowdown 4B/4C
next_priority =
  1. add hard 4C examples where customer volume/order thesis actually breaks
  2. add non-Kia OEM or second-tier supplier counterexamples
  3. test whether C29 guard applies to 2023-2025 auto-parts cycles
```

## 28. Source Notes

Stock-Web files inspected in this loop:
- atlas/manifest.json
- atlas/symbol_profiles/000/000270.json
- atlas/symbol_profiles/005/005850.json
- atlas/symbol_profiles/204/204320.json
- atlas/symbol_profiles/011/011210.json
- atlas/symbol_profiles/009/009900.json
- atlas/ohlcv_tradable_by_symbol_year/000/000270/2020.csv
- atlas/ohlcv_tradable_by_symbol_year/000/000270/2021.csv
- atlas/ohlcv_tradable_by_symbol_year/005/005850/2024.csv
- atlas/ohlcv_tradable_by_symbol_year/005/005850/2025.csv
- atlas/ohlcv_tradable_by_symbol_year/204/204320/2021.csv
- atlas/ohlcv_tradable_by_symbol_year/011/011210/2021.csv

Evidence-source text is represented as evidence-family labels, not full article copies. This MD is intended for calibration ledger ingestion, not as a public research note.
