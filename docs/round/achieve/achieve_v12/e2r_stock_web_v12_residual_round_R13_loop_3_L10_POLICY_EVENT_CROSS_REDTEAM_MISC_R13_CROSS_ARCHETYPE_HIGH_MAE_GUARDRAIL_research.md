# E2R v12 R13 cross-archetype residual calibration research

## 0. Execution metadata

```yaml
schema_family: v12_sector_archetype_residual
selected_round: R13
selected_loop: 3
large_sector_id: L10_POLICY_EVENT_CROSS_REDTEAM_MISC
canonical_archetype_id: R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL
fine_archetype_id: CROSS_ARCHETYPE_HIGH_MAE_ROUTE_SPLIT_METAL_RESOURCE_NUCLEAR_SUPPLIER_AND_EVENT_CONTAMINATION
selection_basis:
  main_execution_prompt: docs/core/e2r_v12_prompt_round_scheduler_corrected.txt
  no_repeat_index: docs/core/V12_Research_No_Repeat_Index.md
selected_priority_bucket: Priority 0
round_schedule_status: coverage_index_selected
round_sector_consistency: pass
price_source: Songdaiki/stock-web
price_basis: tradable_raw
price_adjustment_status: raw_unadjusted_marcap
stock_web_manifest_max_date: 2026-02-20
production_scoring_changed: false
shadow_weight_only: true
```

R13은 개별 sector positive를 새로 캐는 round가 아니라 cross-archetype checkpoint다. 이번 loop는 직전 C15/C16 보강에서 나온 금속/자원 high-MAE와 C04 nuclear supplier blowoff를 한데 묶어 `high_MAE_route_split`을 검증한다.

이 세션에서 `R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL`은 loop 1, loop 2를 이미 만들었으므로 이번 동일 canonical pair는 `loop 3`으로 이어간다.

---

## 1. Research thesis

High MAE는 하나의 증상이지만 원인은 여러 종류다. 같은 -25% drawdown이라도 치료법은 다르다.

```text
A. high MFE + high MAE + non-price bridge exists
   → local 4B watch, not hard 4C immediately

B. low MFE + high MAE + no company-specific bridge
   → Stage2 false-positive block

C. high MFE + later price path dominated by different archetype
   → source-archetype contribution cap / reclassification
```

이번 loop의 목적은 “MFE가 컸으니 성공” 또는 “MAE가 컸으니 실패”라는 단선 판단을 막는 것이다. 가격경로는 공장의 압력계처럼 보이는 숫자다. 압력이 높다고 다 같은 사고가 아니듯, MFE/MAE도 driver bridge와 함께 읽어야 한다.

---

## 2. Validation scope

```yaml
validation_scope:
  selected_cases:
    - 010130 / C15-C16-C32 overlap / 고려아연
    - 103140 / C16-C15 dual-use material / 풍산
    - 025820 / C15-C16 copper label / 이구산업
    - 021050 / C15-C16 copper alloy label / 서원
    - 004020 / C15-C16 steel material label / 현대제철
    - 457550 / C04 nuclear supplier blowoff / 우진엔텍
  required_price_windows:
    - 30D MFE/MAE
    - 90D MFE/MAE
    - 180D MFE/MAE
  output_use:
    - guardrail calibration
    - no production scoring changes
    - shadow-weight rule candidate only
```

---

## 3. Trigger rows

```jsonl
{"row_type":"trigger","schema_family":"v12_sector_archetype_residual","round":"R13","loop":3,"large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL","fine_archetype_id":"NON_C15_EVENT_CONTAMINATION_CAP_DESPITE_HIGH_MFE","source_archetype_id":"C15_MATERIAL_SPREAD_SUPERCYCLE","symbol":"010130","name":"고려아연","trigger_type":"Stage2-Actionable","entry_date":"2024-04-09","entry_close":469000,"price_basis":"tradable_raw","mfe_30d_pct":16.42,"mae_30d_pct":-3.94,"mfe_90d_pct":18.76,"mae_90d_pct":-5.12,"mfe_180d_pct":229.00,"mae_180d_pct":-5.12,"forward_high_30d":546000,"forward_low_30d":450500,"forward_high_90d":557000,"forward_low_90d":445000,"forward_high_180d":1543000,"forward_low_180d":445000,"calibration_usable":true,"case_role":"positive_with_event_contamination_cap","novelty_key":"R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL|010130|Stage2-Actionable|2024-04-09","route":"contribution_cap_after_non_source_driver_dominates","guardrail_lesson":"large later MFE must not be credited wholly to source archetype if governance/tender driver dominates"}
{"row_type":"trigger","schema_family":"v12_sector_archetype_residual","round":"R13","loop":3,"large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL","fine_archetype_id":"DUAL_USE_MATERIAL_POSITIVE_WITH_HIGH_MAE_4B_WATCH","source_archetype_id":"C16_STRATEGIC_RESOURCE_POLICY_SUPPLY","symbol":"103140","name":"풍산","trigger_type":"Stage2-Actionable","entry_date":"2024-04-26","entry_close":62900,"price_basis":"tradable_raw","mfe_30d_pct":25.44,"mae_30d_pct":-10.17,"mfe_90d_pct":25.44,"mae_90d_pct":-25.28,"mfe_180d_pct":25.44,"mae_180d_pct":-26.63,"forward_high_30d":78900,"forward_low_30d":56500,"forward_high_90d":78900,"forward_low_90d":47000,"forward_high_180d":78900,"forward_low_180d":46150,"calibration_usable":true,"case_role":"positive_with_local_4B_watch","novelty_key":"R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL|103140|Stage2-Actionable|2024-04-26","route":"local_4B_watch_not_hard_4C","guardrail_lesson":"actual processing/dual-use bridge can keep Stage2 alive, but high MAE blocks Stage3-Green without refresh"}
{"row_type":"trigger","schema_family":"v12_sector_archetype_residual","round":"R13","loop":3,"large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL","fine_archetype_id":"COPPER_LABEL_LOW_MFE_HIGH_MAE_STAGE2_BLOCK","source_archetype_id":"C15_C16_SHARED","symbol":"025820","name":"이구산업","trigger_type":"Stage2-FalsePositive","entry_date":"2024-05-20","entry_close":7880,"price_basis":"tradable_raw","mfe_30d_pct":6.85,"mae_30d_pct":-33.88,"mfe_90d_pct":6.85,"mae_90d_pct":-51.84,"mfe_180d_pct":6.85,"mae_180d_pct":-55.01,"forward_high_30d":8420,"forward_low_30d":5210,"forward_high_90d":8420,"forward_low_90d":3795,"forward_high_180d":8420,"forward_low_180d":3545,"calibration_usable":true,"case_role":"hard_counterexample","novelty_key":"R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL|025820|Stage2-FalsePositive|2024-05-20","route":"Stage2_FalsePositive_Block","guardrail_lesson":"metal label without cash bridge produces low-MFE/high-MAE failure"}
{"row_type":"trigger","schema_family":"v12_sector_archetype_residual","round":"R13","loop":3,"large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL","fine_archetype_id":"COPPER_ALLOY_LABEL_LOW_MFE_HIGH_MAE_STAGE2_BLOCK","source_archetype_id":"C15_C16_SHARED","symbol":"021050","name":"서원","trigger_type":"Stage2-FalsePositive","entry_date":"2024-05-20","entry_close":1916,"price_basis":"tradable_raw","mfe_30d_pct":4.65,"mae_30d_pct":-28.18,"mfe_90d_pct":4.65,"mae_90d_pct":-43.95,"mfe_180d_pct":4.65,"mae_180d_pct":-48.17,"forward_high_30d":2005,"forward_low_30d":1377,"forward_high_90d":2005,"forward_low_90d":1074,"forward_high_180d":2005,"forward_low_180d":993,"calibration_usable":true,"case_role":"hard_counterexample","novelty_key":"R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL|021050|Stage2-FalsePositive|2024-05-20","route":"Stage2_FalsePositive_Block","guardrail_lesson":"small MFE and deep MAE should zero Stage2 actionable bonus"}
{"row_type":"trigger","schema_family":"v12_sector_archetype_residual","round":"R13","loop":3,"large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL","fine_archetype_id":"LARGECAP_STEEL_LABEL_LOW_MFE_HIGH_MAE_STAGE2_BLOCK","source_archetype_id":"C15_C16_SHARED","symbol":"004020","name":"현대제철","trigger_type":"Stage2-FalsePositive","entry_date":"2024-05-20","entry_close":32350,"price_basis":"tradable_raw","mfe_30d_pct":0.62,"mae_30d_pct":-11.90,"mfe_90d_pct":0.62,"mae_90d_pct":-24.73,"mfe_180d_pct":0.62,"mae_180d_pct":-38.49,"forward_high_30d":32550,"forward_low_30d":28500,"forward_high_90d":32550,"forward_low_90d":24350,"forward_high_180d":32550,"forward_low_180d":19900,"calibration_usable":true,"case_role":"hard_counterexample","novelty_key":"R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL|004020|Stage2-FalsePositive|2024-05-20","route":"Stage2_FalsePositive_Block","guardrail_lesson":"large-cap material importance does not rescue absent margin/demand bridge"}
{"row_type":"trigger","schema_family":"v12_sector_archetype_residual","round":"R13","loop":3,"large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL","fine_archetype_id":"NUCLEAR_SUPPLIER_BLOWOFF_HIGH_MFE_HIGH_MAE_4B_TO_BLOCK","source_archetype_id":"C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY","symbol":"457550","name":"우진엔텍","trigger_type":"Stage2-Watch","entry_date":"2024-07-18","entry_close":31500,"price_basis":"tradable_raw","mfe_30d_pct":32.06,"mae_30d_pct":-50.83,"mfe_90d_pct":32.06,"mae_90d_pct":-50.83,"mfe_180d_pct":32.06,"mae_180d_pct":-58.25,"forward_high_30d":41600,"forward_low_30d":15490,"forward_high_90d":41600,"forward_low_90d":15490,"forward_high_180d":41600,"forward_low_180d":13150,"calibration_usable":true,"case_role":"vertical_MFE_high_MAE_supplier_blowoff","novelty_key":"R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL|457550|Stage2-Watch|2024-07-18","route":"local_4B_watch_then_block_without_contract_bridge","guardrail_lesson":"intraday supplier blowoff should not become Stage3-Green without contract/cash bridge"}
```

---

## 4. Case analysis

### Case A — 010130 고려아연: high MFE with dominant-driver contamination

`고려아연` had a legitimate early materials/smelting bridge. Entry 469,000, early high 546,000, and 90D high 557,000 make it a usable positive-control for materials/resource exposure.

But the 180D high 1,543,000 is not a clean C15/C16 metal-spread result. That later leg was dominated by governance/control-premium dynamics. The right R13 route is:

```text
keep early source-archetype credit
cap source contribution after dominant non-source driver appears
require cross-archetype reclassification
```

### Case B — 103140 풍산: real bridge, but MAE requires local 4B

`풍산` is a real bridge case, not a pure theme. It has non-ferrous/copper processing and defense/ammunition dual-use relevance. The entry-to-high path reached +25.44%, so hard blocking would throw away a usable signal.

But MAE later went below -25%, so the guardrail should prevent `Stage3-Green`. This is a classic `local_4B_watch` case.

```text
actual bridge exists
+ MFE_30D >= +20
+ MAE_90D <= -20
→ Stage2 remains, Stage3 blocked until bridge refresh
```

### Case C — 025820 이구산업: low-MFE/high-MAE hard false positive

`이구산업` shows the other side. MFE never crossed +10%, but MAE expanded past -50%. That is not a 4B watch. It is a Stage2 false-positive block.

### Case D — 021050 서원: copper-alloy label decay

`서원` repeats the same failure in a smaller, cleaner form. MFE +4.65%, MAE -48.17%. This is a hard block.

### Case E — 004020 현대제철: large-cap material label can also fail

`현대제철` matters because it prevents the rule from being only a small-cap anti-spike filter. MFE +0.62% and MAE -38.49% means large-cap steel/material label also needs a demand/margin bridge.

### Case F — 457550 우진엔텍: supplier blowoff route

`우진엔텍` had high MFE, but the drawdown was immediate and deep. It is not a clean positive. It starts as local 4B watch after blowoff, then becomes block/hard review if final-contract/cash bridge is not refreshed.

---

## 5. Aggregate score-return alignment

```yaml
new_independent_case_count: 6
calibration_usable_case_count: 6
calibration_usable_trigger_count: 6
positive_control_or_watch_count: 3
hard_counterexample_count: 3
current_profile_error_count: 4
```

| symbol | route | 30D MFE/MAE | 90D MFE/MAE | 180D MFE/MAE | lesson |
|---|---:|---:|---:|---:|---|
| 010130 | contribution cap | +16.42 / -3.94 | +18.76 / -5.12 | +229.00 / -5.12 | high MFE belongs partly to non-source driver |
| 103140 | local 4B watch | +25.44 / -10.17 | +25.44 / -25.28 | +25.44 / -26.63 | real bridge, high MAE blocks Green |
| 025820 | hard block | +6.85 / -33.88 | +6.85 / -51.84 | +6.85 / -55.01 | copper label false positive |
| 021050 | hard block | +4.65 / -28.18 | +4.65 / -43.95 | +4.65 / -48.17 | copper-alloy label false positive |
| 004020 | hard block | +0.62 / -11.90 | +0.62 / -24.73 | +0.62 / -38.49 | large-cap material label false positive |
| 457550 | 4B then block | +32.06 / -50.83 | +32.06 / -50.83 | +32.06 / -58.25 | supplier blowoff without contract bridge |

---

## 6. Current calibrated profile stress test

### Existing error risk

The current profile can overcompress high-MAE cases into one bucket. That is dangerous because high MAE is a bruise, not the injury. Sometimes it means volatility around a real bridge. Sometimes it means the bridge was imaginary. Sometimes it means the price moved for the wrong archetype.

### Rule candidate: route split

```text
R13_HIGH_MAE_ROUTE_SPLIT_V3

if MFE_30D_pct >= +20
and company_specific_bridge == true
and MAE_90D_pct <= -20:
    route = local_4B_watch
    block_stage3_green = true
    require_bridge_refresh = true
```

```text
if MFE_90D_pct < +10
and MAE_90D_pct <= -25
and company_specific_revenue_margin_cash_bridge == false:
    route = Stage2_FalsePositive_Block
    stage2_actionable_bonus = 0
    max_stage = Stage2-Watch
```

```text
if MFE_180D_pct >= +50
and dominant_price_driver != selected_source_archetype_driver:
    cap_source_archetype_contribution = true
    require_cross_archetype_reclassification = true
```

```text
if intraday_or_short_window_MFE_pct >= +25
and MAE_30D_pct <= -25
and final_contract_or_cash_bridge == false:
    route = local_4B_watch_then_hard_review
    block_stage3_green = true
```

---

## 7. Residual contribution summary

```yaml
do_not_propose_new_weight_delta: false
sector_specific_rule_candidate: false
canonical_archetype_rule_candidate: false
cross_archetype_rule_candidate: true
loop_contribution_label: cross_archetype_high_MAE_guardrail_candidate
new_axis_proposed: R13_HIGH_MAE_ROUTE_SPLIT_V3
existing_axis_strengthened:
  - vertical_MFE_local_4B_watch_without_bridge_refresh
  - low_MFE_high_MAE_stage2_false_positive_block
  - dominant_driver_contamination_contribution_cap
  - intraday_supplier_blowoff_4B_then_block
existing_axis_weakened: null
```

---

## 8. Next recommended archetypes

```text
R13_CROSS_ARCHETYPE_STAGE2_FALSE_POSITIVE_REVIEW
C05_EPC_MEGA_CONTRACT_MARGIN_GAP
C18_CONSUMER_EXPORT_CHANNEL_REORDER
C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE
C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE
```
