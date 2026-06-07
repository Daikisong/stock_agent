# E2R Stock-Web v12 Residual Research — R6 / C22 Insurance Rate Cycle Reserve

```yaml
schema: e2r_stock_web_v12_residual_research_md
version: v12
selected_round: R6
selected_loop: 104
large_sector_id: L6_FINANCIAL_CAPITAL_RETURN_DIGITAL
canonical_archetype_id: C22_INSURANCE_RATE_CYCLE_RESERVE
fine_archetype_id: NONLIFE_INSURANCE_VALUEUP_RATE_CYCLE_RESERVE_QUALITY_CAPITAL_RETURN_BRIDGE_VS_RESERVE_QUALITY_FALSE_POSITIVE
selected_priority_bucket: Priority 1
selection_basis: docs/core/V12_Research_No_Repeat_Index.md
price_source: Songdaiki/stock-web
price_basis: tradable_raw
price_adjustment_status: raw_unadjusted_marcap
stock_web_manifest_max_date: 2026-02-20
live_candidate_mode: false
current_stock_discovery_allowed: false
stock_agent_code_access_allowed: false
stock_agent_code_patch_allowed: false
production_scoring_changed: false
shadow_weight_only: true
handoff_prompt_embedded: true
handoff_prompt_executed_now: false
```

## 1. Execution scope

This run follows the v12 historical calibration mode. It does not scan current candidates, does not open or infer `stock_agent/src`, does not patch production scoring, and does not create a live watchlist. The only output is this standalone historical residual Markdown file.

The price source is fixed to `Songdaiki/stock-web`, `tradable_raw`, `raw_unadjusted_marcap`. The manifest snapshot used here is:

```json
{
  "source_name": "FinanceData/marcap",
  "price_adjustment_status": "raw_unadjusted_marcap",
  "min_date": "1995-05-02",
  "max_date": "2026-02-20",
  "tradable_row_count": 14354401,
  "symbol_count": 5414,
  "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year"
}
```

## 2. Coverage selection

Selected archetype: `C22_INSURANCE_RATE_CYCLE_RESERVE`.

Reason:

```text
Priority 1 table:
C22_INSURANCE_RATE_CYCLE_RESERVE rows = 42
need to 50 = 8
investigation point = insurance rate cycle, reserve quality, capital return
```

Round mapping is valid:

```text
C21~C22 -> R6 / L6_FINANCIAL_CAPITAL_RETURN_DIGITAL
```

This run therefore uses:

```text
selected_round = R6
large_sector_id = L6_FINANCIAL_CAPITAL_RETURN_DIGITAL
```

## 3. Hypothesis

C22 should not treat “insurance value-up” or “rate-cycle label” as a standalone positive. The mechanism is more like an insurance float engine:

```text
premium/rate cycle + underwriting discipline + reserve quality + capital return
        -> sustainable ROE / CSM confidence / shareholder yield
        -> Stage2-Actionable or Yellow evidence

headline value-up / low PBR / insurance beta without reserve quality
        -> temporary rerating
        -> high MAE or full-window 4C-like fade
```

The important separator is whether the market is buying actual reserve-quality/capital-return bridge, or merely a low-PBR financial beta costume.

External event anchor used for the common trigger window:

- Reuters, 2024-02-28, `S.Korea considering penalties on firms failing to boost shareholder return`, describing additional pressure around the Corporate Value-up Programme and shareholder-return criteria.
- Reuters, 2024-03-14, `South Korea regulator to speed up corporate reforms, eyes bold measures`, describing follow-up measures and tax-incentive discussion after the February programme.

## 4. Case set

### Case 1 — Samsung Fire & Marine / 삼성화재 (`000810`) positive with 4B watch

```text
case_id = C22_000810_20240229_VALUEUP_RESERVE_QUALITY_CAPITAL_RETURN_BRIDGE
trigger_date = 2024-02-28
entry_date = 2024-02-29
entry_price = 298,000
local_peak_date = 2024-06-28
local_peak_high = 393,500
local_MFE = +32.05%
full_peak_date = 2024-12-03
full_peak_high = 435,000
full_MFE = +45.97%
trough_date = 2024-04-19
trough_low = 272,500
MAE = -8.56%
classification = positive_with_4b_watch
```

Interpretation:

Samsung Fire is the cleanest positive among the three. It participates in the insurance value-up/capital-return regime and the price route confirms that the market kept assigning value after the trigger. However, full-window peak extension into December is a 4B-watch path; the calibration should recognize the positive bridge but avoid treating the whole later price extension as pure C22 evidence.

Price row anchors:

```text
2024-02-29, o=290500, h=301500, l=285500, c=298000
2024-04-19, o=282000, h=283000, l=272500, c=277500
2024-06-28, o=381500, h=393500, l=378500, c=389000
2024-12-03, o=401500, h=435000, l=401000, c=435000
```

### Case 2 — DB Insurance / DB손해보험 (`005830`) positive but high-MAE reserve-quality watch

```text
case_id = C22_005830_20240229_VALUEUP_CSM_ROE_CAPITAL_RETURN_BRIDGE
trigger_date = 2024-02-28
entry_date = 2024-02-29
entry_price = 98,800
peak_date = 2024-07-02
peak_high = 120,700
MFE = +22.17%
trough_date = 2024-04-12
trough_low = 86,500
MAE = -12.45%
classification = positive_high_mae_reserve_quality_watch
```

Interpretation:

DB Insurance is still a positive C22 case because the route eventually confirmed a high forward high. But the drawdown was not small. That means C22 should avoid a clean Green-style promotion unless reserve quality, capital policy, and earnings visibility are all present. In mechanical terms, DB behaves like a good engine that still knocks under load: the direction is right, but the vibration tells us the reserve-quality filter cannot be optional.

Price row anchors:

```text
2024-02-29, o=97900, h=99600, l=95800, c=98800
2024-04-12, o=94000, h=94000, l=86500, c=88100
2024-07-02, o=108000, h=120700, l=108000, c=114400
```

### Case 3 — Hyundai Marine & Fire / 현대해상 (`001450`) counterexample

```text
case_id = C22_001450_20240229_VALUEUP_RATE_CYCLE_RESERVE_FALSE_POSITIVE
trigger_date = 2024-02-28
entry_date = 2024-02-29
entry_price = 31,500
peak_date = 2024-03-15
peak_high = 35,850
MFE = +13.81%
trough_date = 2024-12-09
trough_low = 24,750
MAE = -21.43%
classification = counterexample_full_window_4c_like
```

Interpretation:

Hyundai Marine & Fire had enough early beta to tempt a stage upgrade. But the full path fails. This is the exact counterexample C22 needs: the same broad insurance value-up/rate-cycle label can produce a temporary rerating while later reserve or loss-ratio uncertainty erases the route. The shadow rule should force C22 to ask whether the value-up headline is actually tied to reserve quality and capital return, not just sector beta.

Price row anchors:

```text
2024-02-29, o=31400, h=32100, l=31200, c=31500
2024-03-15, o=34900, h=35850, l=34500, c=34500
2024-12-09, o=25700, h=25950, l=24750, c=25200
```

## 5. Positive / counterexample balance

```text
new_independent_case_count = 3
reused_case_count = 0
same_archetype_new_symbol_count = 3
same_archetype_new_trigger_family_count = 3
calibration_usable_case_count = 3
calibration_usable_trigger_count = 3
positive_case_count = 2
counterexample_count = 1
current_profile_error_count = 2
verified_url_repair_needed_count = 2
```

Balance:

- Positive: Samsung Fire, DB Insurance.
- Counterexample: Hyundai Marine & Fire.
- Stress point: all three have the same broad Korea value-up / financial capital-return regime, but only the companies with stronger reserve-quality/capital-return interpretation produced durable enough evidence.
- Residual error: a generic low-PBR/value-up sector bonus can over-score Hyundai Marine and over-cleanly score DB despite its high MAE.

## 6. Stage interpretation

### Samsung Fire

```text
baseline_current_proxy = e2r_2_1_stock_web_calibrated
old_risk = Stage3-Yellow_or_Green_watch from value-up + insurance beta
shadow_read = Stage2-Actionable_to_Stage3-Yellow with 4B watch
reason = positive, but full-window extension requires non-price confirmation
```

### DB Insurance

```text
baseline_current_proxy = e2r_2_1_stock_web_calibrated
old_risk = Stage3-Yellow_watch
shadow_read = Stage2-Actionable_or_Yellow
reason = positive path, but MAE demands reserve-quality and capital-policy confirmation
```

### Hyundai Marine & Fire

```text
baseline_current_proxy = e2r_2_1_stock_web_calibrated
old_risk = false Stage2-Actionable risk from sector beta
shadow_read = Stage1_or_4C_watch
reason = broad value-up/rate-cycle label without reserve-quality bridge failed full-window
```

## 7. Proposed shadow rule

```text
axis_id = c22_reserve_quality_capital_return_bridge_required_for_stage2_actionable_shadow_only
```

Rule:

```text
For C22_INSURANCE_RATE_CYCLE_RESERVE, do not allow a low-PBR/value-up/rate-cycle headline to reach Stage2-Actionable unless at least one non-price bridge exists:

1. explicit capital return policy or payout improvement visibility,
2. reserve quality / loss-ratio discipline evidence,
3. CSM or ROE durability evidence,
4. clean solvency/capital adequacy support.

If only broad sector beta exists, apply rate_cycle_label_only penalty.
If MFE is positive but MAE exceeds roughly 10-12% before bridge confirmation, cap at Stage2-Actionable or route to 4B/4C watch depending on later thesis break.
```

Suggested shadow deltas:

```json
{
  "reserve_quality_evidence": 1.2,
  "explicit_capital_return_policy": 0.8,
  "rate_cycle_label_only": -1.0,
  "high_mae_after_valueup_label": -0.8,
  "loss_ratio_or_reserve_uncertainty": -1.2
}
```

No production scoring is changed in this run.

## 8. Machine-readable rows

### case rows

```jsonl
{"row_type": "case", "case_id": "C22_000810_20240229_VALUEUP_RESERVE_QUALITY_CAPITAL_RETURN_BRIDGE", "ticker": "000810", "name": "삼성화재", "market": "KOSPI", "trigger_date": "2024-02-28", "entry_date": "2024-02-29", "entry_price": 298000, "local_peak_date": "2024-06-28", "local_peak_high": 393500, "local_mfe_pct": 32.05, "full_peak_date": "2024-12-03", "full_peak_high": 435000, "full_mfe_pct": 45.97, "trough_date": "2024-04-19", "trough_low": 272500, "mae_pct": -8.56, "classification": "positive_with_4b_watch", "trigger_family": "valueup_capital_return_plus_reserve_quality", "calibration_usable": true}
{"row_type": "case", "case_id": "C22_005830_20240229_VALUEUP_CSM_ROE_CAPITAL_RETURN_BRIDGE", "ticker": "005830", "name": "DB손해보험", "market": "KOSPI", "trigger_date": "2024-02-28", "entry_date": "2024-02-29", "entry_price": 98800, "peak_date": "2024-07-02", "peak_high": 120700, "mfe_pct": 22.17, "trough_date": "2024-04-12", "trough_low": 86500, "mae_pct": -12.45, "classification": "positive_high_mae_reserve_quality_watch", "trigger_family": "insurance_valueup_csm_roe_bridge", "calibration_usable": true}
{"row_type": "case", "case_id": "C22_001450_20240229_VALUEUP_RATE_CYCLE_RESERVE_FALSE_POSITIVE", "ticker": "001450", "name": "현대해상", "market": "KOSPI", "trigger_date": "2024-02-28", "entry_date": "2024-02-29", "entry_price": 31500, "peak_date": "2024-03-15", "peak_high": 35850, "mfe_pct": 13.81, "trough_date": "2024-12-09", "trough_low": 24750, "mae_pct": -21.43, "classification": "counterexample_full_window_4c_like", "trigger_family": "insurance_valueup_without_reserve_quality_bridge", "calibration_usable": true}
```

### trigger rows

```jsonl
{"row_type": "trigger", "canonical_archetype_id": "C22_INSURANCE_RATE_CYCLE_RESERVE", "large_sector_id": "L6_FINANCIAL_CAPITAL_RETURN_DIGITAL", "trigger_id": "TRG_C22_000810_20240229_VALUEUP_RESERVE_QUALITY_CAPITAL_RETURN_BRIDGE", "ticker": "000810", "name": "삼성화재", "trigger_date": "2024-02-28", "entry_date": "2024-02-29", "entry_price": 298000, "trigger_family": "valueup_capital_return_plus_reserve_quality", "classification": "positive_with_4b_watch", "calibration_usable": true}
{"row_type": "trigger", "canonical_archetype_id": "C22_INSURANCE_RATE_CYCLE_RESERVE", "large_sector_id": "L6_FINANCIAL_CAPITAL_RETURN_DIGITAL", "trigger_id": "TRG_C22_005830_20240229_VALUEUP_CSM_ROE_CAPITAL_RETURN_BRIDGE", "ticker": "005830", "name": "DB손해보험", "trigger_date": "2024-02-28", "entry_date": "2024-02-29", "entry_price": 98800, "trigger_family": "insurance_valueup_csm_roe_bridge", "classification": "positive_high_mae_reserve_quality_watch", "calibration_usable": true}
{"row_type": "trigger", "canonical_archetype_id": "C22_INSURANCE_RATE_CYCLE_RESERVE", "large_sector_id": "L6_FINANCIAL_CAPITAL_RETURN_DIGITAL", "trigger_id": "TRG_C22_001450_20240229_VALUEUP_RATE_CYCLE_RESERVE_FALSE_POSITIVE", "ticker": "001450", "name": "현대해상", "trigger_date": "2024-02-28", "entry_date": "2024-02-29", "entry_price": 31500, "trigger_family": "insurance_valueup_without_reserve_quality_bridge", "classification": "counterexample_full_window_4c_like", "calibration_usable": true}
```

### score_simulation rows

```jsonl
{"row_type": "score_simulation", "case_id": "C22_000810_20240229_VALUEUP_RESERVE_QUALITY_CAPITAL_RETURN_BRIDGE", "baseline_current_proxy": "e2r_2_1_stock_web_calibrated", "pre_shadow_expected_stage": "Stage3-Yellow_or_Green_watch", "proposed_shadow_adjustment": "+reserve_quality_capital_return_bridge, -full_4b_without_non_price_evidence", "post_shadow_stage": "Stage2-Actionable_to_Stage3-Yellow_with_4B_watch", "reason": "삼성화재는 C22 positive지만 4B full-window 과열을 같이 분리해야 한다."}
{"row_type": "score_simulation", "case_id": "C22_005830_20240229_VALUEUP_CSM_ROE_CAPITAL_RETURN_BRIDGE", "baseline_current_proxy": "e2r_2_1_stock_web_calibrated", "pre_shadow_expected_stage": "Stage3-Yellow_watch", "proposed_shadow_adjustment": "+csm_roe_capital_return_bridge, -high_mae_reserve_uncertainty", "post_shadow_stage": "Stage2-Actionable_or_Yellow", "reason": "DB손보는 positive지만 12%대 MAE를 허용하지 않으려면 reserve quality 확인이 필요하다."}
{"row_type": "score_simulation", "case_id": "C22_001450_20240229_VALUEUP_RATE_CYCLE_RESERVE_FALSE_POSITIVE", "baseline_current_proxy": "e2r_2_1_stock_web_calibrated", "pre_shadow_expected_stage": "Stage2-Actionable_false_positive_risk", "proposed_shadow_adjustment": "-reserve_quality_missing, -rate_cycle_label_only, route_to_4C_watch", "post_shadow_stage": "Stage1_or_4C_watch", "reason": "현대해상은 같은 value-up/rate-cycle label에서도 reserve quality bridge가 약하면 full-window drawdown이 커진다."}
```

### aggregate row

```jsonl
{"row_type": "aggregate", "canonical_archetype_id": "C22_INSURANCE_RATE_CYCLE_RESERVE", "large_sector_id": "L6_FINANCIAL_CAPITAL_RETURN_DIGITAL", "new_independent_case_count": 3, "reused_case_count": 0, "same_archetype_new_symbol_count": 3, "same_archetype_new_trigger_family_count": 3, "calibration_usable_case_count": 3, "calibration_usable_trigger_count": 3, "positive_case_count": 2, "counterexample_count": 1, "current_profile_error_count": 2, "verified_url_repair_needed_count": 2}
```

### shadow_weight row

```jsonl
{"row_type": "shadow_weight", "axis_id": "c22_reserve_quality_capital_return_bridge_required_for_stage2_actionable_shadow_only", "canonical_archetype_id": "C22_INSURANCE_RATE_CYCLE_RESERVE", "large_sector_id": "L6_FINANCIAL_CAPITAL_RETURN_DIGITAL", "proposed_weight_delta": {"reserve_quality_evidence": 1.2, "explicit_capital_return_policy": 0.8, "rate_cycle_label_only": -1.0, "high_mae_after_valueup_label": -0.8, "loss_ratio_or_reserve_uncertainty": -1.2}, "production_scoring_changed": false, "handoff_required": true}
```

### residual_contribution row

```jsonl
{"row_type": "residual_contribution", "label": "canonical_archetype_rule_candidate", "new_axis_proposed": "c22_reserve_quality_capital_return_bridge_required_for_stage2_actionable_shadow_only", "existing_axis_strengthened": "full_4b_requires_non_price_evidence scoped to C22 insurance value-up/rate-cycle rallies", "existing_axis_weakened": null, "do_not_propose_new_weight_delta": false}
```

## 9. Residual contribution summary

```text
diversity_score_summary:
C22 Priority 1 보강 + Samsung Fire reserve-quality/capital-return positive + DB positive/high-MAE watch + Hyundai Marine reserve-quality false-positive counterexample 분리

do_not_propose_new_weight_delta: false
auto_selected_coverage_gap: C22 rows 42, 50-row target까지 8 부족
sector_specific_rule_candidate: true
canonical_archetype_rule_candidate: true
loop_contribution_label: canonical_archetype_rule_candidate
new_axis_proposed: c22_reserve_quality_capital_return_bridge_required_for_stage2_actionable_shadow_only
existing_axis_strengthened: full_4b_requires_non_price_evidence scoped to C22 insurance value-up/rate-cycle rallies
existing_axis_weakened: null
next_recommended_archetypes: C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN, C22_INSURANCE_RATE_CYCLE_RESERVE, C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG
```

## 10. Deferred Coding Agent Handoff Prompt

```text
You are a later coding agent. Do not assume this MD changed production scoring. Read this Markdown as one candidate residual calibration handoff.

Task:
1. Ingest the machine-readable JSONL blocks above.
2. Validate that no hard duplicate exists for:
   canonical_archetype_id + symbol + trigger_family + entry_date.
3. If accepted, add the case/trigger/score_simulation/aggregate/shadow_weight/residual rows to the v12 calibration ingestion queue.
4. Do not patch production scoring directly from this MD.
5. Only implement `c22_reserve_quality_capital_return_bridge_required_for_stage2_actionable_shadow_only` after it is confirmed across enough independent C22 cases.
6. Keep the rule shadow-only until batch validation shows improved positive/counterexample separation.
```

## 11. Final metadata

```yaml
selected_round: R6
selected_loop: 104
selection_basis: docs/core/V12_Research_No_Repeat_Index.md
selected_priority_bucket: Priority 1
round_schedule_status: coverage_index_selected
round_sector_consistency: pass
large_sector_id: L6_FINANCIAL_CAPITAL_RETURN_DIGITAL
canonical_archetype_id: C22_INSURANCE_RATE_CYCLE_RESERVE
fine_archetype_id: NONLIFE_INSURANCE_VALUEUP_RATE_CYCLE_RESERVE_QUALITY_CAPITAL_RETURN_BRIDGE_VS_RESERVE_QUALITY_FALSE_POSITIVE
price_source: Songdaiki/stock-web
stock_web_manifest_max_date: 2026-02-20
new_independent_case_count: 3
reused_case_count: 0
same_archetype_new_symbol_count: 3
same_archetype_new_trigger_family_count: 3
calibration_usable_case_count: 3
calibration_usable_trigger_count: 3
positive_case_count: 2
counterexample_count: 1
current_profile_error_count: 2
verified_url_repair_needed_count: 2
do_not_propose_new_weight_delta: false
auto_selected_coverage_gap: C22 rows 42, 50-row target까지 8 부족
sector_specific_rule_candidate: true
canonical_archetype_rule_candidate: true
loop_contribution_label: canonical_archetype_rule_candidate
new_axis_proposed: c22_reserve_quality_capital_return_bridge_required_for_stage2_actionable_shadow_only
existing_axis_strengthened: full_4b_requires_non_price_evidence scoped to C22 insurance value-up/rate-cycle rallies
existing_axis_weakened: null
next_recommended_archetypes: C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN, C22_INSURANCE_RATE_CYCLE_RESERVE, C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG
```
