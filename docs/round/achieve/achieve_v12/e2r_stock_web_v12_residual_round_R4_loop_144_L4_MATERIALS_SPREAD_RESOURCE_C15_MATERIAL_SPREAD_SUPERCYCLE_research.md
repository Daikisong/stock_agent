# E2R Stock-Web V12 Residual Research — R4 / C15 MATERIAL SPREAD SUPERCYCLE

```yaml
research_session: post_calibrated_sector_archetype_residual_research
mode: historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12
selected_round: R4
selected_loop: 144
large_sector_id: L4_MATERIALS_SPREAD_RESOURCE
canonical_archetype_id: C15_MATERIAL_SPREAD_SUPERCYCLE
fine_archetype_id: mixed_C15_polysilicon_steel_refining_copper_latex_spread_holdout
selection_basis: docs/core/V12_Research_No_Repeat_Index.md
selected_priority_bucket: Priority 2 quality holdout; static C15 rows=73, guidance=URL/proxy repair, counterexample/4B/4C balance, new spread bridge paths
round_schedule_status: coverage_index_selected
round_sector_consistency: pass
price_source: Songdaiki/stock-web
price_basis: tradable_raw
price_adjustment_status: raw_unadjusted_marcap
stock_web_manifest_max_date: 2026-02-20
production_code_patch_included: false
production_scoring_patch_applied: false
handoff_prompt_executed_now: false
```

## 1. Selection rationale

`V12_Research_No_Repeat_Index.md` shows C15 as already above the 50-row threshold, so this loop is not a quantity-fill loop. It is a quality holdout pass for material spread supercycle cases: polysilicon, NB-latex/BPA, refining cracks, copper, and steel. The key question is whether the current profile still over-upgrades spread headlines into Stage3 without enough evidence that the spread flows into operating margin, FCF, and durable price path.

This loop adds **6 calibration-usable rows**, **6 new/holdout spread trigger families**, **3 counterexamples**, and **5 residual profile errors** for `R4/L4/C15`.

## 2. Stock-Web manifest/schema confirmation

```yaml
source_name: FinanceData/marcap
price_adjustment_status: raw_unadjusted_marcap
calibration_shard_root: atlas/ohlcv_tradable_by_symbol_year
tradable_shard_columns: d,o,h,l,c,v,a,mc,s,m
MFE_formula: max high from entry_date through N tradable rows / entry_price - 1
MAE_formula: min low from entry_date through N tradable rows / entry_price - 1
corporate_action_rule: 180D window blocked when corporate-action candidate overlaps
manifest_max_date: 2026-02-20
```

## 3. Case summary

| symbol | name | trigger_date | trigger_type | classification | evidence_family | MFE_180D_pct | MAE_180D_pct | drawdown_after_peak_pct |
|---|---|---:|---|---|---|---:|---:|---:|
| 010060 | OCI/OCI홀딩스 | 2021-07-29 | Stage3-Yellow | positive_with_local_4B_watch | polysilicon_price_surge_to_actual_operating_profit | 43.2203 | -28.7288 | -50.2367 |
| 011780 | 금호석유화학 | 2021-03-23 | 4B | counterexample_high_MAE_after_spread_peak | nb_latex_bpa_spread_supercycle_peak | 28.1116 | -34.1202 | -48.5762 |
| 010950 | S-Oil | 2022-04-28 | 4B | counterexample_fast_peak_margin_fade | refining_crack_margin_inventory_gain_supercycle | 17.7033 | -26.2201 | -37.3171 |
| 103140 | 풍산 | 2024-10-21 | Stage3-Yellow | positive_with_decontamination_and_local_4B_watch | copper_price_rebound_plus_defense_growth_contaminated_MFE | 138.9758 | -34.3528 | -10.2381 |
| 005490 | POSCO/POSCO홀딩스 | 2021-04-14 | Stage3-Yellow | positive_with_local_4B_watch_spread_bridge | steel_spread_demand_price_record_earnings_bridge | 22.1566 | -23.1905 | -37.1221 |
| 004020 | 현대제철 | 2021-04-28 | 4B | counterexample_margin_bridge_insufficient | steel_recovery_q1_black_swing_without_sustainable_spread_bridge | 9.7561 | -35.453 | -41.1905 |

## 4. Actual Stock-Web price-path table

| symbol | entry_date | entry_price | MFE_30D_pct | MAE_30D_pct | MFE_90D_pct | MAE_90D_pct | MFE_180D_pct | MAE_180D_pct | peak_date | peak_price | drawdown_after_peak_pct | corporate_action_180D |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|
| 010060 | 2021-07-29 | 118000 | 24.1525 | -14.4068 | 43.2203 | -14.4068 | 43.2203 | -28.7288 | 2021-10-01 | 169000 | -50.2367 | False |
| 011780 | 2021-03-23 | 233000 | 25.5365 | -6.4378 | 28.1116 | -13.0901 | 28.1116 | -34.1202 | 2021-05-06 | 298500 | -48.5762 | False |
| 010950 | 2022-04-28 | 104500 | 17.7033 | -2.8708 | 17.7033 | -18.8517 | 17.7033 | -26.2201 | 2022-06-13 | 123000 | -37.3171 | False |
| 103140 | 2024-10-21 | 70300 | 5.2632 | -27.4538 | 5.2632 | -34.3528 | 138.9758 | -34.3528 | 2025-07-16 | 168000 | -10.2381 | False |
| 005490 | 2021-04-14 | 338500 | 22.1566 | -4.579 | 22.1566 | -9.6012 | 22.1566 | -23.1905 | 2021-05-10 | 413500 | -37.1221 | False |
| 004020 | 2021-04-28 | 57400 | 9.7561 | -12.0209 | 9.7561 | -21.1672 | 9.7561 | -35.453 | 2021-05-11 | 63000 | -41.1905 | False |

## 5. Case notes

### 5.1 OCI / OCI Holdings — polysilicon spread positive, but with local 4B overlay

OCI's 2Q21 operating profit turned positive and exceeded KRW100bn as polysilicon price increases from supply shortage flowed into earnings. The path validates that a material spread can become Stage3-Yellow, but the 180D MAE of **-28.7288%** and post-peak drawdown of **-50.2367%** argue for a local 4B overlay after fast spread MFE.

### 5.2 Kumho Petrochemical — NB-latex/BPA spread peak reversal

The NB-latex/BPA spread thesis was real at the time, but the price path shows a classic supercycle peak problem: 90D MFE stayed positive while 180D MAE reached **-34.1202%**. C15 should not keep Stage3 open once spread momentum stops improving or inventory/channel indicators roll over.

### 5.3 S-Oil — refining crack margin is real, but inventory/refining spread fades quickly

S-Oil's Q1 2022 performance was backed by strong cracking margins and inventory gains. The issue is not evidence absence; the issue is duration. MFE peaked within 30D and then the 180D path fell to **-26.2201%**. This is a C15/C17 boundary example where spread profit should be treated as Stage2-Actionable plus 4B watch unless margin durability is refreshed.

### 5.4 Poongsan — copper spread needs defense decontamination

Poongsan had a valid copper-price rebound thesis, but the later price path also reflected defense growth. C15 should retain the positive metal-spread signal while separating it from C03 defense-export rerating. The row is positive, but high MAE and cross-canonical contamination require local 4B sizing/entry guard.

### 5.5 POSCO Holdings — steel spread bridge worked, but late drawdown remains

POSCO's 2021 steel demand/pricing bridge was one of the cleaner positive C15 examples. MFE reached **22.1566%** with a strong operating-profit backdrop. Still, the post-peak drawdown of **-37.1221%** means C15 needs a post-MFE 4B watch layer rather than a simple Green hold.

### 5.6 Hyundai Steel — steel recovery headline without sustainable spread bridge

Hyundai Steel's 1Q21 black-swing was real, but the forward path had only **9.7561%** MFE and **-35.453%** MAE. That is a Stage2 evidence row, not a clean Stage3-Yellow spread supercycle row.

## 6. Score/return alignment

```yaml
positive_case_count: 3
counterexample_count: 3
local_4B_watch_count: 6
current_profile_error_count: 5
avg_MFE_180D_pct: 43.3206
avg_MAE_180D_pct: -30.3442
rows_with_MAE180_below_minus_20pct: 6
rows_with_MFE180_above_20pct: 4
```

The return alignment is asymmetric. Material spread evidence often creates enough MFE to justify Stage2 or Stage3-Yellow, but the same group repeatedly shows deep 180D MAE after the spread peak. C15 therefore needs a two-layer gate: first, require realized spread to operating-margin/FCF bridge; second, require local 4B when peak proximity or non-C15 contaminant contribution is large.

## 7. Shadow rule candidate

```text
C15_MATERIAL_SPREAD_REQUIRES_REALIZED_SPREAD_OPM_FCF_BRIDGE_AND_CONTAMINANT_DECONFLATION_WITH_LOCAL_4B_CAP
```

Rule sketch:

```yaml
stage2_allowed_when:
  - public commodity/spread improvement exists
  - company has direct spread exposure
  - no hard thesis break
stage3_yellow_allowed_when:
  - realized ASP/spread improvement is visible
  - operating margin or FCF bridge is confirmed
  - inventory gain or one-off gain is separated from recurring spread economics
  - non-C15 contaminant such as defense, governance, battery optionality, or refining inventory gain is deconflated
local_4b_overlay_when:
  - MFE90 or MFE180 is strong but MAE180 <= -20pct
  - peak occurs early and drawdown_after_peak <= -30pct
  - spread evidence is real but unsupported by margin persistence
  - cross-canonical contaminant explains a material part of MFE
stage3_block_when:
  - evidence is only commodity price headline
  - company-level margin/FCF bridge is missing
  - spread is already mean-reverting or inventory/channel indicators deteriorate
```

Existing axes tested:

```yaml
existing_axis_tested:
  - stage2_required_bridge
  - local_4b_watch_guard
  - price_only_blowoff_blocks_positive_stage
existing_axis_strengthened:
  - local_4b_watch_guard
  - stage2_required_bridge
existing_axis_weakened: []
new_axis_proposed:
  - C15_material_spread_bridge_plus_contaminant_deconflation
loop_contribution_label: holdout_validation_passed
```

## 8. Machine-readable JSONL trigger rows

```jsonl
{"row_type": "trigger", "research_session": "post_calibrated_sector_archetype_residual_research", "selected_round": "R4", "selected_loop": 144, "large_sector_id": "L4_MATERIALS_SPREAD_RESOURCE", "canonical_archetype_id": "C15_MATERIAL_SPREAD_SUPERCYCLE", "fine_archetype_id": "mixed_C15_polysilicon_steel_refining_copper_latex_spread_holdout", "case_id": "C15_010060_2021_POLYSILICON_PRICE_SURGE_ACTUAL_OP_BRIDGE", "symbol": "010060", "name": "OCI/OCI홀딩스", "trigger_type": "Stage3-Yellow", "trigger_date": "2021-07-29", "entry_date": "2021-07-29", "entry_price": 118000.0, "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "MFE_30D_pct": 24.1525, "MAE_30D_pct": -14.4068, "MFE_90D_pct": 43.2203, "MAE_90D_pct": -14.4068, "MFE_180D_pct": 43.2203, "MAE_180D_pct": -28.7288, "peak_date": "2021-10-01", "peak_price": 169000.0, "drawdown_after_peak_pct": -50.2367, "window_180D_end_date": "2022-04-22", "window_180D_corporate_action_contaminated": false, "calibration_usable": true, "classification": "positive_with_local_4B_watch", "evidence_family": "polysilicon_price_surge_to_actual_operating_profit", "source_url": "https://www.asiae.co.kr/en/article/2021072817125685550", "source_summary": "2Q21 operating profit turned positive and exceeded KRW100bn, reflecting polysilicon price increases caused by supply shortage.", "raw_component_score_breakdown": {"eps_fcf_explosion": 23, "earnings_visibility": 14, "bottleneck_pricing": 24, "market_mispricing": 10, "valuation_rerating": 8, "capital_allocation": 3, "information_confidence": 7}, "current_profile_pre_rule_score": 79.0, "shadow_rule_post_score": 75.5, "current_profile_error": "Stage3 signal was directionally right, but raw price path requires a local 4B overlay because MAE180 and peak drawdown were deep.", "reuse_reason": "new_symbol_or_new_C15_trigger_family_holdout", "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false}
{"row_type": "trigger", "research_session": "post_calibrated_sector_archetype_residual_research", "selected_round": "R4", "selected_loop": 144, "large_sector_id": "L4_MATERIALS_SPREAD_RESOURCE", "canonical_archetype_id": "C15_MATERIAL_SPREAD_SUPERCYCLE", "fine_archetype_id": "mixed_C15_polysilicon_steel_refining_copper_latex_spread_holdout", "case_id": "C15_011780_2021_NB_LATEX_BPA_SPREAD_PEAK_REVERSAL", "symbol": "011780", "name": "금호석유화학", "trigger_type": "4B", "trigger_date": "2021-03-23", "entry_date": "2021-03-23", "entry_price": 233000.0, "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "MFE_30D_pct": 25.5365, "MAE_30D_pct": -6.4378, "MFE_90D_pct": 28.1116, "MAE_90D_pct": -13.0901, "MFE_180D_pct": 28.1116, "MAE_180D_pct": -34.1202, "peak_date": "2021-05-06", "peak_price": 298500.0, "drawdown_after_peak_pct": -48.5762, "window_180D_end_date": "2021-12-09", "window_180D_corporate_action_contaminated": false, "calibration_usable": true, "classification": "counterexample_high_MAE_after_spread_peak", "evidence_family": "nb_latex_bpa_spread_supercycle_peak", "source_url": "https://rdata.kbsec.com/pdf_data/20210322145204253E.pdf", "source_summary": "KB Securities framed 2021 catalysts around NB-latex and BPA spread levels, but the later path suffered a deep 180D drawdown.", "raw_component_score_breakdown": {"eps_fcf_explosion": 22, "earnings_visibility": 12, "bottleneck_pricing": 21, "market_mispricing": 9, "valuation_rerating": 9, "capital_allocation": 3, "information_confidence": 8}, "current_profile_pre_rule_score": 77.0, "shadow_rule_post_score": 66.0, "current_profile_error": "Spread assumptions were valid but peak proximity and cyclicality required faster 4B; Stage3 holding without spread-sustainability confirmation was too permissive.", "reuse_reason": "new_symbol_or_new_C15_trigger_family_holdout", "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false}
{"row_type": "trigger", "research_session": "post_calibrated_sector_archetype_residual_research", "selected_round": "R4", "selected_loop": 144, "large_sector_id": "L4_MATERIALS_SPREAD_RESOURCE", "canonical_archetype_id": "C15_MATERIAL_SPREAD_SUPERCYCLE", "fine_archetype_id": "mixed_C15_polysilicon_steel_refining_copper_latex_spread_holdout", "case_id": "C15_010950_2022_REFINING_CRACK_MARGIN_SUPERCYCLE_FADE", "symbol": "010950", "name": "S-Oil", "trigger_type": "4B", "trigger_date": "2022-04-28", "entry_date": "2022-04-28", "entry_price": 104500.0, "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "MFE_30D_pct": 17.7033, "MAE_30D_pct": -2.8708, "MFE_90D_pct": 17.7033, "MAE_90D_pct": -18.8517, "MFE_180D_pct": 17.7033, "MAE_180D_pct": -26.2201, "peak_date": "2022-06-13", "peak_price": 123000.0, "drawdown_after_peak_pct": -37.3171, "window_180D_end_date": "2023-01-17", "window_180D_corporate_action_contaminated": false, "calibration_usable": true, "classification": "counterexample_fast_peak_margin_fade", "evidence_family": "refining_crack_margin_inventory_gain_supercycle", "source_url": "https://en.yna.co.kr/view/AEN20220427005752320", "source_summary": "Q1 performance was driven by strong cracking margin, high oil prices and refining operating profit, but the forward price path peaked quickly and then faded.", "raw_component_score_breakdown": {"eps_fcf_explosion": 21, "earnings_visibility": 13, "bottleneck_pricing": 19, "market_mispricing": 8, "valuation_rerating": 8, "capital_allocation": 3, "information_confidence": 8}, "current_profile_pre_rule_score": 76.0, "shadow_rule_post_score": 64.5, "current_profile_error": "C15/C17 boundary: spread profit was real, but inventory gain and refining margin cyclicality required local 4B rather than Stage3 persistence.", "reuse_reason": "new_symbol_or_new_C15_trigger_family_holdout", "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false}
{"row_type": "trigger", "research_session": "post_calibrated_sector_archetype_residual_research", "selected_round": "R4", "selected_loop": 144, "large_sector_id": "L4_MATERIALS_SPREAD_RESOURCE", "canonical_archetype_id": "C15_MATERIAL_SPREAD_SUPERCYCLE", "fine_archetype_id": "mixed_C15_polysilicon_steel_refining_copper_latex_spread_holdout", "case_id": "C15_103140_2024_COPPER_DEFENSE_DECONTAMINATION_HOLDOUT", "symbol": "103140", "name": "풍산", "trigger_type": "Stage3-Yellow", "trigger_date": "2024-10-21", "entry_date": "2024-10-21", "entry_price": 70300.0, "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "MFE_30D_pct": 5.2632, "MAE_30D_pct": -27.4538, "MFE_90D_pct": 5.2632, "MAE_90D_pct": -34.3528, "MFE_180D_pct": 138.9758, "MAE_180D_pct": -34.3528, "peak_date": "2025-07-16", "peak_price": 168000.0, "drawdown_after_peak_pct": -10.2381, "window_180D_end_date": "2025-07-16", "window_180D_corporate_action_contaminated": false, "calibration_usable": true, "classification": "positive_with_decontamination_and_local_4B_watch", "evidence_family": "copper_price_rebound_plus_defense_growth_contaminated_MFE", "source_url": "https://www.asiae.co.kr/en/article/2024101807525861876", "source_summary": "Hana Securities highlighted defense growth potential and forecast copper prices could rise again in 4Q24; the later MFE was huge but came through a volatile path.", "raw_component_score_breakdown": {"eps_fcf_explosion": 20, "earnings_visibility": 15, "bottleneck_pricing": 19, "market_mispricing": 12, "valuation_rerating": 10, "capital_allocation": 4, "information_confidence": 8}, "current_profile_pre_rule_score": 81.0, "shadow_rule_post_score": 78.0, "current_profile_error": "Positive C15 signal should survive, but copper spread contribution must be decontaminated from defense export rerating and 4B entry quality must be enforced.", "reuse_reason": "new_symbol_or_new_C15_trigger_family_holdout", "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false}
{"row_type": "trigger", "research_session": "post_calibrated_sector_archetype_residual_research", "selected_round": "R4", "selected_loop": 144, "large_sector_id": "L4_MATERIALS_SPREAD_RESOURCE", "canonical_archetype_id": "C15_MATERIAL_SPREAD_SUPERCYCLE", "fine_archetype_id": "mixed_C15_polysilicon_steel_refining_copper_latex_spread_holdout", "case_id": "C15_005490_2021_STEEL_SPREAD_RECORD_EARNINGS_POSITIVE_WITH_4B", "symbol": "005490", "name": "POSCO/POSCO홀딩스", "trigger_type": "Stage3-Yellow", "trigger_date": "2021-04-14", "entry_date": "2021-04-14", "entry_price": 338500.0, "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "MFE_30D_pct": 22.1566, "MAE_30D_pct": -4.579, "MFE_90D_pct": 22.1566, "MAE_90D_pct": -9.6012, "MFE_180D_pct": 22.1566, "MAE_180D_pct": -23.1905, "peak_date": "2021-05-10", "peak_price": 413500.0, "drawdown_after_peak_pct": -37.1221, "window_180D_end_date": "2022-01-03", "window_180D_corporate_action_contaminated": false, "calibration_usable": true, "classification": "positive_with_local_4B_watch_spread_bridge", "evidence_family": "steel_spread_demand_price_record_earnings_bridge", "source_url": "https://www.asiae.co.kr/en/print.htm?idxno=2021041309314970672", "source_summary": "POSCO reported strong preliminary Q1 operating profit and better Q2 expectations due to strong market conditions and improved external environment.", "raw_component_score_breakdown": {"eps_fcf_explosion": 22, "earnings_visibility": 16, "bottleneck_pricing": 20, "market_mispricing": 10, "valuation_rerating": 9, "capital_allocation": 5, "information_confidence": 8}, "current_profile_pre_rule_score": 80.0, "shadow_rule_post_score": 76.0, "current_profile_error": "Steel spread and operating-profit bridge were real, but post-peak drawdown argues for a local 4B overlay after fast MFE.", "reuse_reason": "new_symbol_or_new_C15_trigger_family_holdout", "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false}
{"row_type": "trigger", "research_session": "post_calibrated_sector_archetype_residual_research", "selected_round": "R4", "selected_loop": 144, "large_sector_id": "L4_MATERIALS_SPREAD_RESOURCE", "canonical_archetype_id": "C15_MATERIAL_SPREAD_SUPERCYCLE", "fine_archetype_id": "mixed_C15_polysilicon_steel_refining_copper_latex_spread_holdout", "case_id": "C15_004020_2021_STEEL_RECOVERY_FALSE_STAGE3_SPREAD", "symbol": "004020", "name": "현대제철", "trigger_type": "4B", "trigger_date": "2021-04-28", "entry_date": "2021-04-28", "entry_price": 57400.0, "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "MFE_30D_pct": 9.7561, "MAE_30D_pct": -12.0209, "MFE_90D_pct": 9.7561, "MAE_90D_pct": -21.1672, "MFE_180D_pct": 9.7561, "MAE_180D_pct": -35.453, "peak_date": "2021-05-11", "peak_price": 63000.0, "drawdown_after_peak_pct": -41.1905, "window_180D_end_date": "2022-01-17", "window_180D_corporate_action_contaminated": false, "calibration_usable": true, "classification": "counterexample_margin_bridge_insufficient", "evidence_family": "steel_recovery_q1_black_swing_without_sustainable_spread_bridge", "source_url": "https://en.yna.co.kr/view/AEN20210427007052320", "source_summary": "Hyundai Steel swung to black in 1Q21 on strong sales amid global recovery, but the price path showed low MFE and deep 180D MAE.", "raw_component_score_breakdown": {"eps_fcf_explosion": 18, "earnings_visibility": 12, "bottleneck_pricing": 15, "market_mispricing": 9, "valuation_rerating": 7, "capital_allocation": 3, "information_confidence": 7}, "current_profile_pre_rule_score": 74.0, "shadow_rule_post_score": 62.0, "current_profile_error": "Stage2 was defensible, but Stage3 required stronger spread-to-margin persistence and FCF bridge; otherwise this becomes high-MAE false positive.", "reuse_reason": "new_symbol_or_new_C15_trigger_family_holdout", "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false}
```

## 9. Machine-readable aggregate row

```json
{
  "row_type": "aggregate",
  "selected_round": "R4",
  "selected_loop": 144,
  "large_sector_id": "L4_MATERIALS_SPREAD_RESOURCE",
  "canonical_archetype_id": "C15_MATERIAL_SPREAD_SUPERCYCLE",
  "trigger_row_count": 6,
  "calibration_usable_rows": 6,
  "positive_case_count": 3,
  "counterexample_count": 3,
  "local_4B_watch_count": 6,
  "current_profile_error_count": 5,
  "avg_MFE_180D_pct": 43.3206,
  "avg_MAE_180D_pct": -30.3442,
  "new_axis_proposed": "C15_MATERIAL_SPREAD_REQUIRES_REALIZED_SPREAD_OPM_FCF_BRIDGE_AND_CONTAMINANT_DECONFLATION_WITH_LOCAL_4B_CAP",
  "existing_axis_strengthened": [
    "stage2_required_bridge",
    "local_4b_watch_guard",
    "price_only_blowoff_blocks_positive_stage"
  ]
}
```

## 10. Residual contribution summary

```yaml
new_independent_case_count: 6
reused_case_count: 0
new_symbol_count: 6
same_archetype_new_symbol_count: 6
same_archetype_new_trigger_family_count: 6
new_trigger_family_count: 6
positive_case_count: 3
counterexample_count: 3
current_profile_error_count: 5
diversity_score_summary: 6 symbols / 6 C15 spread families / positive 3 + counterexample 3 + local 4B 6
do_not_propose_new_weight_delta: false
loop_contribution_label: holdout_validation_passed
```

## 11. Deferred Coding Agent Handoff Prompt

```text
Do not execute this handoff inside the research session.

In a later coding-agent session, ingest this Markdown with the other V12 files. Parse the JSONL trigger rows and aggregate row. Treat the proposed rule only as a shadow candidate. Do not apply a global C15 weight change unless batch validation confirms that C15 spread rows with realized spread→OPM/FCF bridge outperform commodity-headline-only rows after controlling for local 4B and cross-canonical contaminant exposure.

Candidate patch axis:
C15_MATERIAL_SPREAD_REQUIRES_REALIZED_SPREAD_OPM_FCF_BRIDGE_AND_CONTAMINANT_DECONFLATION_WITH_LOCAL_4B_CAP

Expected implementation location is deferred to the later batch implementation session. This research session did not inspect stock_agent source code and did not patch production scoring.
```

## 12. Batch Ingest Self-Audit

```yaml
standard_filename_ok: true
filename_matches_metadata: true
uses_no_repeat_index_as_ledger_only: true
uses_stock_web_actual_ohlcv: true
jsonl_trigger_row_count: 6
calibration_usable_rows: 6
representative_rows: 6
source_proxy_only_rows: 0
evidence_url_pending_rows: 0
rows_missing_required_mfe_mae: 0
rows_missing_entry_price_or_date: 0
rows_with_noncanonical_trigger_type: 0
future_data_leakage_detected: false
corporate_action_contaminated_rows: 0
insufficient_forward_window_rows: 0
production_code_patch_included: false
production_scoring_patch_applied: false
handoff_prompt_executed_now: false
ready_for_batch_ingest: true
```

## 13. Next research state

```text
completed_round = R4
completed_loop = 144
selection_basis = docs/core/V12_Research_No_Repeat_Index.md
selected_priority_bucket = Priority 2 quality holdout / C15 rows 73 / material spread URL-proxy and 4B balance check
next_recommended_archetypes = C15_MATERIAL_SPREAD_SUPERCYCLE_holdout_only_if_new_naphtha_steel_nonferrous_spread_bridge | R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL_holdout_quality_only | C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION_quality_holdout
round_schedule_status = coverage_index_selected
round_sector_consistency = pass
```
