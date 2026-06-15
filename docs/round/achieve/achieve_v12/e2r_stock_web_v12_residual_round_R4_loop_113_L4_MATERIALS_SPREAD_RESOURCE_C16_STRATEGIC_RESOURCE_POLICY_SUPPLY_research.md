# E2R v12 residual calibration research

## 0. Execution metadata

```yaml
schema_family: v12_sector_archetype_residual
selected_round: R4
selected_loop: 113
large_sector_id: L4_MATERIALS_SPREAD_RESOURCE
canonical_archetype_id: C16_STRATEGIC_RESOURCE_POLICY_SUPPLY
fine_archetype_id: COPPER_CRITICAL_MATERIAL_PROCESSING_AND_DUAL_USE_SUPPLY_BRIDGE_VS_METAL_LABEL_FALSE_POSITIVE
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

`C16_STRATEGIC_RESOURCE_POLICY_SUPPLY`는 repo index 기준 12 rows / 10 symbols인 부족 구역이다. 직전 로컬 C16 산출물은 loop 112였으므로 이번은 `R4/C16 loop 113`으로 이어간다. 이번 pass는 C16 visible-new tuple 중심으로 `103140`, `025820`, `021050`, `004020`을 쓴다. `010130`은 직전 C16에서 이미 사용했기 때문에 이번에는 직접 trigger row에서 제외하고 contamination-cap reference로만 언급한다.

---

## 1. Research thesis

C16은 C15와 닮아 보이지만 초점이 다르다.

- C15: metal price/spread가 company margin으로 번역되는가.
- C16: strategic resource / critical supply / dual-use material policy가 실제 processing, supply security, offtake, customer or defense bridge로 닫히는가.

그래서 C16의 scoring gate는 “자원 단어”가 아니라 다음 사슬을 본다.

```text
strategic resource / critical material / dual-use supply relevance
→ actual processing capacity or offtake/supply relationship
→ listed-company ASP-volume-margin-cash bridge
→ price path alignment
```

이번 loop의 핵심은 `copper / steel / non-ferrous / dual-use` vocabulary가 있어도, 상장사 cash bridge가 없으면 C16 Stage2를 열면 안 된다는 점이다.

---

## 2. Source validation

```yaml
stock_web_manifest:
  source_name: FinanceData/marcap
  price_adjustment_status: raw_unadjusted_marcap
  max_date: 2026-02-20
  calibration_shard_root: atlas/ohlcv_tradable_by_symbol_year
  caveat: Raw/unadjusted OHLC; corporate-action-contaminated windows blocked by default.
```

Symbol caveats:

```yaml
103140:
  name: 풍산
  market: KOSPI
  corporate_action_candidate_count: 0
  calibration_caveat: clean in relevant window

025820:
  name: 이구산업
  market: KOSPI
  relevant_window_after_old_corporate_action_candidates: true

021050:
  name: 서원
  market: KOSPI
  relevant_window_after_old_corporate_action_candidates: true

004020:
  name: 현대제철
  market: KOSPI
  relevant_window_after_old_corporate_action_candidates: true
```

---

## 3. Trigger rows

```jsonl
{"row_type":"trigger","schema_family":"v12_sector_archetype_residual","round":"R4","loop":113,"large_sector_id":"L4_MATERIALS_SPREAD_RESOURCE","canonical_archetype_id":"C16_STRATEGIC_RESOURCE_POLICY_SUPPLY","fine_archetype_id":"DUAL_USE_COPPER_ALLOY_AND_AMMUNITION_SUPPLY_PROCESSING_BRIDGE_WITH_MAE_WATCH","symbol":"103140","name":"풍산","trigger_type":"Stage2-Actionable","entry_date":"2024-04-26","entry_close":62900,"price_basis":"tradable_raw","mfe_30d_pct":25.44,"mae_30d_pct":-10.17,"mfe_90d_pct":25.44,"mae_90d_pct":-25.28,"mfe_180d_pct":25.44,"mae_180d_pct":-26.63,"forward_high_30d":78900,"forward_low_30d":56500,"forward_high_90d":78900,"forward_low_90d":47000,"forward_high_180d":78900,"forward_low_180d":46150,"calibration_usable":true,"case_role":"positive_with_high_MAE_watch","novelty_key":"C16_STRATEGIC_RESOURCE_POLICY_SUPPLY|103140|Stage2-Actionable|2024-04-26","non_price_bridge":"actual copper/non-ferrous processing plus ammunition/defense dual-use supply relevance","score_alignment":"Stage2 may open, but high MAE requires local 4B watch and refreshed order/margin bridge"}
{"row_type":"trigger","schema_family":"v12_sector_archetype_residual","round":"R4","loop":113,"large_sector_id":"L4_MATERIALS_SPREAD_RESOURCE","canonical_archetype_id":"C16_STRATEGIC_RESOURCE_POLICY_SUPPLY","fine_archetype_id":"COPPER_PROCESSING_LABEL_WITHOUT_OFFTAKE_OR_CASH_CONVERSION_BRIDGE","symbol":"025820","name":"이구산업","trigger_type":"Stage2-FalsePositive","entry_date":"2024-05-20","entry_close":7880,"price_basis":"tradable_raw","mfe_30d_pct":6.85,"mae_30d_pct":-33.88,"mfe_90d_pct":6.85,"mae_90d_pct":-51.84,"mfe_180d_pct":6.85,"mae_180d_pct":-55.01,"forward_high_30d":8420,"forward_low_30d":5210,"forward_high_90d":8420,"forward_low_90d":3795,"forward_high_180d":8420,"forward_low_180d":3545,"calibration_usable":true,"case_role":"counterexample","novelty_key":"C16_STRATEGIC_RESOURCE_POLICY_SUPPLY|025820|Stage2-FalsePositive|2024-05-20","non_price_bridge":"copper processing label without visible strategic offtake or cash conversion bridge","score_alignment":"low-MFE/high-MAE; block Stage2-Actionable bonus"}
{"row_type":"trigger","schema_family":"v12_sector_archetype_residual","round":"R4","loop":113,"large_sector_id":"L4_MATERIALS_SPREAD_RESOURCE","canonical_archetype_id":"C16_STRATEGIC_RESOURCE_POLICY_SUPPLY","fine_archetype_id":"BRASS_COPPER_ALLOY_THEME_WITHOUT_STRATEGIC_CUSTOMER_BRIDGE","symbol":"021050","name":"서원","trigger_type":"Stage2-FalsePositive","entry_date":"2024-05-20","entry_close":1916,"price_basis":"tradable_raw","mfe_30d_pct":4.65,"mae_30d_pct":-28.18,"mfe_90d_pct":4.65,"mae_90d_pct":-43.95,"mfe_180d_pct":4.65,"mae_180d_pct":-48.17,"forward_high_30d":2005,"forward_low_30d":1377,"forward_high_90d":2005,"forward_low_90d":1074,"forward_high_180d":2005,"forward_low_180d":993,"calibration_usable":true,"case_role":"counterexample","novelty_key":"C16_STRATEGIC_RESOURCE_POLICY_SUPPLY|021050|Stage2-FalsePositive|2024-05-20","non_price_bridge":"brass/copper alloy vocabulary without strategic customer, offtake, or margin bridge","score_alignment":"pure resource label false positive"}
{"row_type":"trigger","schema_family":"v12_sector_archetype_residual","round":"R4","loop":113,"large_sector_id":"L4_MATERIALS_SPREAD_RESOURCE","canonical_archetype_id":"C16_STRATEGIC_RESOURCE_POLICY_SUPPLY","fine_archetype_id":"STEEL_SUPPLY_SECURITY_LABEL_WITHOUT_POLICY_OR_MARGIN_BRIDGE","symbol":"004020","name":"현대제철","trigger_type":"Stage2-FalsePositive","entry_date":"2024-05-20","entry_close":32350,"price_basis":"tradable_raw","mfe_30d_pct":0.62,"mae_30d_pct":-11.90,"mfe_90d_pct":0.62,"mae_90d_pct":-24.73,"mfe_180d_pct":0.62,"mae_180d_pct":-38.49,"forward_high_30d":32550,"forward_low_30d":28500,"forward_high_90d":32550,"forward_low_90d":24350,"forward_high_180d":32550,"forward_low_180d":19900,"calibration_usable":true,"case_role":"counterexample","novelty_key":"C16_STRATEGIC_RESOURCE_POLICY_SUPPLY|004020|Stage2-FalsePositive|2024-05-20","non_price_bridge":"generic steel supply/security or value label without strategic policy, offtake, margin or cash bridge","score_alignment":"large-cap strategic-material vocabulary also fails without company-specific bridge"}
```

---

## 4. Case analysis

### Case A — 103140 풍산: dual-use copper/materials bridge, but MAE watch

`풍산` is not merely a copper-price proxy. It has actual copper/non-ferrous processing and a defense/ammunition side, so the company can sit closer to C16 than generic small-cap copper labels. The stock path confirms there was an early tradable bridge: 2024-04-26 entry close 62,900 and 2024-05-14 high 78,900.

But the bridge was not stable enough for green scoring. The path later printed 2024-08-05 low 47,000 and 2024-12-09 low 46,150. C16 should score it as `Stage2-Actionable with local 4B/high-MAE watch`, not as clean Stage3-Green.

**Calibration lesson:** actual processing + dual-use supply can open the C16 gate, but only refreshed orders, ASP/margin bridge, or defense backlog can keep the gate open.

### Case B — 025820 이구산업: copper processing label without strategic cash bridge

`이구산업` is a strong C16 false-positive. It has copper-processing vocabulary and can move with copper beta, but the price path is almost pure theme decay. Entry 2024-05-20 close 7,880; high 8,420; then 2024-08-05 low 3,795 and 2024-12-09 low 3,545.

**Calibration lesson:** copper vocabulary is not strategic supply. C16 should require a named supply/offtake relationship, end-customer bridge, margin conversion, or policy-backed bottleneck evidence.

### Case C — 021050 서원: copper-alloy label false positive

`서원` is the lower-quality version of the same mistake. Entry 1,916, forward high 2,005, low 993 by 2024-12-09. It is a textbook `resource label without strategic supply bridge` block.

**Calibration lesson:** brass/copper-alloy labels are not enough. If MFE is below 10% and MAE collapses beyond -25%, C16 should remove Stage2-Actionable credit unless a fresh company-specific bridge appears.

### Case D — 004020 현대제철: large-cap steel is not automatically strategic resource alpha

`현대제철` is useful because it proves the guardrail is not only for small caps. Entry 2024-05-20 close 32,350, high only 32,550, then 2024-12-09 low 19,900. Even large-cap steel/supply-security vocabulary fails if demand, margin, utilization, inventory, or policy transfer bridge is absent.

**Calibration lesson:** C16 should not mistake “important material” for “investable bottleneck.” Strategic importance is necessary but not sufficient; cash conversion is the hinge.

---

## 5. Aggregate score-return alignment

```yaml
new_independent_case_count: 4
new_visible_C16_symbol_count: 4
same_archetype_new_trigger_family_count: 4
calibration_usable_case_count: 4
calibration_usable_trigger_count: 4
positive_case_count: 1
counterexample_count: 3
current_profile_error_count: 3
```

| symbol | role | 30D MFE/MAE | 90D MFE/MAE | 180D MFE/MAE | calibration lesson |
|---|---:|---:|---:|---:|---|
| 103140 | positive + MAE watch | +25.44 / -10.17 | +25.44 / -25.28 | +25.44 / -26.63 | real processing/dual-use bridge, but needs refresh |
| 025820 | counterexample | +6.85 / -33.88 | +6.85 / -51.84 | +6.85 / -55.01 | copper label without offtake/cash bridge |
| 021050 | counterexample | +4.65 / -28.18 | +4.65 / -43.95 | +4.65 / -48.17 | copper-alloy label false positive |
| 004020 | counterexample | +0.62 / -11.90 | +0.62 / -24.73 | +0.62 / -38.49 | steel value/supply label without margin bridge |

---

## 6. Current calibrated profile stress test

### Existing error risk

C16 can over-reward this pattern:

```text
critical material / copper / steel / non-ferrous label
+ macro resource shortage headline
+ early volume spike
```

But strategic-resource alpha behaves like a locked door. The metal word is just a key-shaped object; it only opens the door when it matches a company-level lock: processing capacity, offtake, customer pull-through, policy transfer, margin, or cash conversion.

### Strengthened rule candidate

```text
C16_STRATEGIC_RESOURCE_BRIDGE_REQUIREMENT

if C16
and strategic_resource_or_critical_material_label == true
and company_specific_processing_offtake_customer_policy_cash_bridge == false:
    stage2_actionable_bonus = 0
    max_stage = Stage2-Watch
```

### Low-MFE/high-MAE block

```text
C16_RESOURCE_LABEL_LOW_MFE_HIGH_MAE_BLOCK

if C16
and MFE_90D_pct < +10
and MAE_90D_pct <= -25
and refreshed_offtake_or_cash_bridge == false:
    Stage2_FalsePositive_Block = true
```

### Positive-with-watch escape hatch

```text
C16_DUAL_USE_PROCESSING_ESCAPE_HATCH_WITH_4B_WATCH

if C16
and actual_processing_capacity == true
and dual_use_or_strategic_customer_relevance == true
and MFE_30D_pct >= +20:
    keep_stage2_actionable_bonus = true
    if MAE_90D_pct <= -20:
        local_4B_watch = true
        block_stage3_green_until_bridge_refresh = true
```

---

## 7. Residual contribution summary

```yaml
do_not_propose_new_weight_delta: false
sector_specific_rule_candidate: false
canonical_archetype_rule_candidate: true
loop_contribution_label: canonical_archetype_rule_candidate
new_axis_proposed: C16_RESOURCE_LABEL_LOW_MFE_HIGH_MAE_BLOCK
existing_axis_strengthened:
  - C16_company_specific_processing_offtake_cash_bridge_requirement
  - C16_resource_label_stage2_block_without_execution_bridge
  - C16_dual_use_processing_positive_with_4B_watch
  - C16_largecap_material_importance_not_enough_without_margin_bridge
existing_axis_weakened: null
```

---

## 8. Next recommended archetypes

```text
R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL
R13_CROSS_ARCHETYPE_STAGE2_FALSE_POSITIVE_REVIEW
C05_EPC_MEGA_CONTRACT_MARGIN_GAP
C18_CONSUMER_EXPORT_CHANNEL_REORDER
C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE
```
