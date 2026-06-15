---
research_mode: stock_web_v12_residual_cross_archetype_redteam
selected_round: R13
selected_loop: 2
large_sector_id: L10_POLICY_EVENT_CROSS_REDTEAM_MISC
canonical_archetype_id: R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL
fine_archetype_id: CROSS_ARCHETYPE_VERTICAL_MFE_HIGH_MAE_AND_LOW_MFE_HIGH_MAE_ROUTE_RETEST
price_source: Songdaiki/stock-web
price_basis: tradable_raw
price_adjustment_status: raw_unadjusted_marcap
selection_basis: docs/core/V12_Research_No_Repeat_Index.md
output_file: e2r_stock_web_v12_residual_round_R13_loop_2_L10_POLICY_EVENT_CROSS_REDTEAM_MISC_R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL_research.md
---

# stock-web v12 residual research — R13 cross-archetype high-MAE guardrail retest

## 0. Execution contract

This run follows the v12 post-calibrated historical trigger-level residual research procedure.  
`NO-REPEAT INDEX` is used only as a duplicate-avoidance and coverage ledger.  
No production scoring patch is proposed here; all candidate rules are shadow-calibration only.

- selected_round: `R13`
- selected_loop: `2`
- selected_priority_bucket: `Priority 0`
- large_sector_id: `L10_POLICY_EVENT_CROSS_REDTEAM_MISC`
- canonical_archetype_id: `R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL`
- fine_archetype_id: `CROSS_ARCHETYPE_VERTICAL_MFE_HIGH_MAE_AND_LOW_MFE_HIGH_MAE_ROUTE_RETEST`

### Loop decision

Prior local R13 high-MAE work exists at `R13 / loop 1`, so this pass is `loop 2` for the same selected pair. Other R13 scopes have their own loop numbering and do not block this pair-specific increment.

### Why R13 now?

The last sector pass strengthened `C17_CHEMICAL_COMMODITY_MARGIN_SPREAD`, and the next recommended residual target was R13 high-MAE red-team work. This run therefore does not search for new sector-specific positives. It compares already observed high-MAE structures across C15/C17/C31 and checks whether the profile should route them into 4B watch, contribution cap, or hard Stage2 false-positive block.

---

## 1. Validation scope

This R13 run uses six price paths:

1. `036460 / 한국가스공사 / C31` — policy/exploration headline with vertical MFE and later drawdown.
2. `011790 / SKC / C17` — materials/battery-event contamination after vertical MFE.
3. `006110 / 삼아알미늄 / C15` — aluminium/battery-foil high-MFE then severe drawdown.
4. `009830 / 한화솔루션 / C17` — low-MFE/high-MAE chemical/solar false positive.
5. `018470 / 조일알미늄 / C15` — low-MFE/high-MAE aluminium rolling false positive.
6. `005380 / 현대차 / C31` — real shareholder-return policy, but price alignment fails under margin/cycle override.

All rows use stock-web `tradable_raw` 1D OHLC. Corporate-action-contaminated windows are not used as positive score evidence.

---

## 2. Cross-case summary

| symbol | source archetype | entry_date | entry_close | 30D MFE/MAE | 90D MFE/MAE | 180D MFE/MAE | R13 route |
|---|---|---:|---:|---:|---:|---:|---|
| 036460 한국가스공사 | C31 | 2024-06-03 | 38,700 | +66.67% / -3.49% | +66.67% / -5.68% | +66.67% / -23.51% | local_4B_watch_not_stage3_green |
| 011790 SKC | C17 | 2024-05-23 | 117,000 | +70.94% / -7.61% | +70.94% / -8.03% | +70.94% / -22.82% | contribution_cap + local_4B_watch |
| 006110 삼아알미늄 | C15 | 2024-05-20 | 75,500 | +28.34% / -7.28% | +28.34% / -47.55% | +28.34% / -53.58% | stage2_cap_then_4B_watch |
| 009830 한화솔루션 | C17 | 2024-05-20 | 31,800 | +7.86% / -14.15% | +7.86% / -30.35% | +7.86% / -37.11% | Stage2_FalsePositive_Block |
| 018470 조일알미늄 | C15 | 2024-05-20 | 2,470 | +7.29% / -18.83% | +7.29% / -41.30% | +7.29% / -48.83% | Stage2_FalsePositive_Block |
| 005380 현대차 | C31 | 2024-08-28 | 259,000 | +3.09% / -14.48% | +3.09% / -22.82% | +3.09% / -32.12% | policy_bonus_cap_when_price_alignment_fails |

---

## 3. Case notes

### 3.1 한국가스공사 — policy/exploration MFE is not automatically Green

The 2024-06-03 exploration/policy headline created a sharp vertical MFE. Entry close was 38,700 and the forward high reached 64,500.  
But the non-price bridge was still exploration-stage and economics were not confirmed. The later low at 29,600 converts the case into a classic `vertical_MFE_high_MAE_watch`.

Interpretation:

```text
exploration_policy_headline + huge early MFE + no confirmed economics
→ local_4B_watch
→ block Stage3-Green unless economics/cash bridge refreshes
```

### 3.2 SKC — high MFE, but wrong-archetype contamination

SKC’s move from 117,000 to 200,000 looks excellent if read as pure C17 spread expansion.  
The problem is driver purity. The path was better explained as a materials/battery event rather than a clean chemical feedstock-product spread path. After the spike, the price later dropped to the low-90,000s.

Interpretation:

```text
MFE_30D >= +30
and dominant_driver != source_archetype_driver
→ cap source-archetype contribution
→ route to R13 event-contamination watch
```

### 3.3 삼아알미늄 — enough MFE to tempt the model, but MAE says the bridge decayed

Entry close was 75,500. The path reached 96,900 but later fell to 35,050.  
This is not a hard "never buy aluminium foil" rule. It is a rule that the profile cannot keep Stage2-Actionable bonus alive after margin/revision/cash bridge decay.

Interpretation:

```text
MFE_30D around +25~30
and MAE_90D <= -25
and no refreshed bridge
→ Stage2 bonus cap
→ local_4B watch
```

### 3.4 한화솔루션 — low MFE/high MAE means Stage2 false positive

The trigger had only +7.86% MFE but reached -37.11% MAE.  
This is the opposite of "volatile winner"; it is a low-quality Stage2 candidate. Petrochemical/solar/cheap-feedstock wording did not become listed-company margin/cash conversion.

Interpretation:

```text
MFE_90D < +10
and MAE_90D <= -25
and no segment margin/cash bridge
→ Stage2_FalsePositive_Block
```

### 3.5 조일알미늄 — commodity label with no listed-company translation

Entry close was 2,470, forward high only 2,650, later low 1,264.  
The signal is not "aluminium is bad"; it is "commodity vocabulary without company-level spread conversion is not enough."

Interpretation:

```text
commodity_label == true
and company_specific_margin_bridge == false
and low_MFE_high_MAE == true
→ Stage2_FalsePositive_Block
```

### 3.6 현대차 — real cash-return policy can still fail price alignment

Hyundai’s shareholder-return plan was real, but the price path after 2024-08-28 did not align: only +3.09% MFE versus -32.12% later MAE.  
For C31, the R13 lesson is that a real policy/capital-return event can still be capped when margin-cycle or sector-cycle pressure overwhelms it.

Interpretation:

```text
policy_cash_return_real == true
but MFE_90D < +10
and MAE_180D <= -25
→ keep policy fact
→ cap price-score contribution
```

---

## 4. Trigger rows JSONL

```jsonl
{"canonical_archetype_id": "R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL", "source_archetype_id": "C31_POLICY_SUBSIDY_LEGISLATION_EVENT", "symbol": "036460", "name": "한국가스공사", "trigger_type": "Stage2-Actionable", "entry_date": "2024-06-03", "entry_close": 38700, "mfe_30d_pct": 66.67, "mae_30d_pct": -3.49, "mfe_90d_pct": 66.67, "mae_90d_pct": -5.68, "mfe_180d_pct": 66.67, "mae_180d_pct": -23.51, "classification": "vertical_MFE_high_MAE_watch", "bridge_status": "exploration/policy headline; confirmed economics absent", "calibration_usable": true, "rule_route": "local_4B_watch_not_stage3_green"}
{"canonical_archetype_id": "R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL", "source_archetype_id": "C17_CHEMICAL_COMMODITY_MARGIN_SPREAD", "symbol": "011790", "name": "SKC", "trigger_type": "Stage2-Actionable", "entry_date": "2024-05-23", "entry_close": 117000, "mfe_30d_pct": 70.94, "mae_30d_pct": -7.61, "mfe_90d_pct": 70.94, "mae_90d_pct": -8.03, "mfe_180d_pct": 70.94, "mae_180d_pct": -22.82, "classification": "vertical_MFE_event_contamination_high_MAE_watch", "bridge_status": "materials/battery-event contamination; C17 spread bridge not clean", "calibration_usable": true, "rule_route": "cap_source_archetype_contribution_and_local_4B_watch"}
{"canonical_archetype_id": "R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL", "source_archetype_id": "C15_MATERIAL_SPREAD_SUPERCYCLE", "symbol": "006110", "name": "삼아알미늄", "trigger_type": "Stage2-Watch", "entry_date": "2024-05-20", "entry_close": 75500, "mfe_30d_pct": 28.34, "mae_30d_pct": -7.28, "mfe_90d_pct": 28.34, "mae_90d_pct": -47.55, "mfe_180d_pct": 28.34, "mae_180d_pct": -53.58, "classification": "high_MFE_high_MAE_bridge_decay", "bridge_status": "aluminium/battery foil label without refreshed margin/cash bridge", "calibration_usable": true, "rule_route": "stage2_cap_then_4B_watch"}
{"canonical_archetype_id": "R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL", "source_archetype_id": "C17_CHEMICAL_COMMODITY_MARGIN_SPREAD", "symbol": "009830", "name": "한화솔루션", "trigger_type": "Stage2-Watch", "entry_date": "2024-05-20", "entry_close": 31800, "mfe_30d_pct": 7.86, "mae_30d_pct": -14.15, "mfe_90d_pct": 7.86, "mae_90d_pct": -30.35, "mfe_180d_pct": 7.86, "mae_180d_pct": -37.11, "classification": "low_MFE_high_MAE_false_positive", "bridge_status": "petchem/solar mix; spread headline did not translate into listed-company margin path", "calibration_usable": true, "rule_route": "Stage2_FalsePositive_Block"}
{"canonical_archetype_id": "R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL", "source_archetype_id": "C15_MATERIAL_SPREAD_SUPERCYCLE", "symbol": "018470", "name": "조일알미늄", "trigger_type": "Stage2-Watch", "entry_date": "2024-05-20", "entry_close": 2470, "mfe_30d_pct": 7.29, "mae_30d_pct": -18.83, "mfe_90d_pct": 7.29, "mae_90d_pct": -41.3, "mfe_180d_pct": 7.29, "mae_180d_pct": -48.83, "classification": "low_MFE_high_MAE_false_positive", "bridge_status": "aluminium rolling / commodity beta label without company-specific spread conversion", "calibration_usable": true, "rule_route": "Stage2_FalsePositive_Block"}
{"canonical_archetype_id": "R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL", "source_archetype_id": "C31_POLICY_SUBSIDY_LEGISLATION_EVENT", "symbol": "005380", "name": "현대차", "trigger_type": "Stage2-Actionable", "entry_date": "2024-08-28", "entry_close": 259000, "mfe_30d_pct": 3.09, "mae_30d_pct": -14.48, "mfe_90d_pct": 3.09, "mae_90d_pct": -22.82, "mfe_180d_pct": 3.09, "mae_180d_pct": -32.12, "classification": "real_policy_cash_return_but_low_MFE_high_MAE", "bridge_status": "shareholder return real, but margin/cycle override dominated", "calibration_usable": true, "rule_route": "bonus_cap_when_price_alignment_fails"}
```

---

## 5. Rule candidate

### R13_HIGH_MAE_ROUTE_SPLIT_V2

```text
if MFE_30D_pct >= +25
and MAE_90D_pct <= -25
and refreshed_non_price_bridge == false:
    route = local_4B_watch
    block_stage3_green = true
```

```text
if MFE_90D_pct < +10
and MAE_90D_pct <= -25
and company_specific_margin_revenue_cash_bridge == false:
    route = Stage2_FalsePositive_Block
    stage2_actionable_bonus = 0
```

```text
if MFE_30D_pct >= +30
and dominant_price_driver != canonical_archetype_driver:
    cap_source_archetype_contribution = true
    require_cross_archetype_reclassification = true
```

```text
if policy_or_cash_return_event_is_real == true
and MFE_90D_pct < +10
and MAE_180D_pct <= -25:
    keep_event_truth = true
    cap_price_score_contribution = true
```

---

## 6. Current calibrated profile stress test

Current profile risk:

- It can over-reward vertical MFE when the bridge is still exploratory or contaminated by another archetype.
- It can leave low-MFE/high-MAE rows in Stage2-Watch too long when the right route is Stage2-FalsePositive.
- It can confuse real non-price facts with aligned score-return behavior.

Shadow patch candidate only:

```text
add R13_HIGH_MAE_ROUTE_SPLIT_V2 as a cross-archetype guardrail;
do not alter production weights until more R13 rows accumulate.
```

---

## 7. Residual contribution summary

- new_independent_case_count: `6`
- reused_case_count_within_R13_HIGH_MAE: `0`
- calibration_usable_case_count: `6`
- positive_control_or_watch_count: `3`
- hard_counterexample_count: `3`
- current_profile_error_count: `4`
- loop_contribution_label: `cross_archetype_high_MAE_guardrail_candidate`
- new_axis_proposed: `R13_HIGH_MAE_ROUTE_SPLIT_V2`
- existing_axis_strengthened:
  - `vertical_MFE_local_4B_watch_without_refreshed_bridge`
  - `low_MFE_high_MAE_stage2_false_positive_block`
  - `dominant_driver_contamination_contribution_cap`
  - `real_policy_event_price_alignment_cap`

---

## 8. Next recommended archetypes

```text
R13_CROSS_ARCHETYPE_STAGE2_FALSE_POSITIVE_REVIEW
R13_CROSS_ARCHETYPE_4B_4C_REDTEAM
C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG
C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY
C15_MATERIAL_SPREAD_SUPERCYCLE
```
