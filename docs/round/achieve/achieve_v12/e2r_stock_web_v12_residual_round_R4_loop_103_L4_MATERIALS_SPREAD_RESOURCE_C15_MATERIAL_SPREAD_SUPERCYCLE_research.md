# E2R v12 residual calibration research

## 0. Execution metadata

```yaml
schema_family: v12_sector_archetype_residual
selected_round: R4
selected_loop: 103
large_sector_id: L4_MATERIALS_SPREAD_RESOURCE
canonical_archetype_id: C15_MATERIAL_SPREAD_SUPERCYCLE
fine_archetype_id: COPPER_ZINC_STEEL_PRICE_BETA_TO_LISTED_COMPANY_MARGIN_BRIDGE_VS_SMALLCAP_METAL_THEME_BLOWOFF
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

`C15_MATERIAL_SPREAD_SUPERCYCLE`는 repo index 기준 6 rows / 6 symbols인 얇은 구역이다. 직전 로컬 C15 산출물은 loop 102였으므로 이번은 `R4/C15 loop 103`으로 이어간다. 이번 pass는 기존 visible top-covered symbol이 아닌 `010130`, `025820`, `021050`, `004020`을 사용한다. `010130`은 C16/C32에서 본 적이 있지만 C15 canonical에서는 새 tuple이며, 금속 spread bridge와 governance contamination cap을 함께 보정하기 위한 positive-control로만 쓴다.

---

## 1. Research thesis

C15의 본질은 “금속 가격이 올랐다”가 아니다. 실제 calibration에 필요한 것은 다음 사슬이다.

```text
metal price / spread supercycle
→ company-specific ASP / inventory gain / volume / margin bridge
→ revenue or cash-flow revision
→ price path alignment
```

이번 루프는 이 사슬이 닫힌 케이스와 끊긴 케이스를 분리한다.

- `고려아연(010130)`: actual smelting / precious and base-metal processing bridge가 있어 C15 positive-control로 쓸 수 있지만, 2024년 9월 이후 가격경로는 governance/tender event가 지배해 C15 contribution을 cap해야 한다.
- `이구산업(025820)`: copper-processing vocabulary와 copper beta가 강한 day-one spike를 만들었지만, listed-company margin/cash bridge 없이 low-MFE/high-MAE로 무너진 counterexample.
- `서원(021050)`: brass/copper-alloy theme spike 후 급락한 small-cap metal beta counterexample.
- `현대제철(004020)`: steel spread / undervalued steel label이 있어도 demand/margin bridge가 없으면 Stage2를 열면 안 되는 large-cap low-MFE/high-MAE counterexample.

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
010130:
  name: 고려아연
  case_role: positive_control_with_non_C15_event_contamination_cap
  note: 2024-09 이후 governance/tender path dominates; C15 contribution capped after contamination.

025820:
  name: 이구산업
  market: KOSPI
  corporate_action_candidate_dates: 1996-01-03, 2007-04-30, 2007-07-11
  relevant_window_after_candidate: true

021050:
  name: 서원
  market: KOSPI
  corporate_action_candidate_dates: 1996-12-24, 1997-09-25, 2008-04-16, 2016-06-21
  relevant_window_after_candidate: true

004020:
  name: 현대제철
  market: KOSPI
  corporate_action_candidate_dates: 1997-01-03, 1997-10-16, 1999-03-25, 1999-07-14, 2000-04-12, 2014-01-24
  relevant_window_after_candidate: true
```

---

## 3. Trigger rows

```jsonl
{"row_type":"trigger","schema_family":"v12_sector_archetype_residual","round":"R4","loop":103,"large_sector_id":"L4_MATERIALS_SPREAD_RESOURCE","canonical_archetype_id":"C15_MATERIAL_SPREAD_SUPERCYCLE","fine_archetype_id":"ZINC_BASE_METAL_SMELTER_MARGIN_BRIDGE_WITH_GOVERNANCE_CONTAMINATION_CAP","symbol":"010130","name":"고려아연","trigger_type":"Stage2-Actionable","entry_date":"2024-04-09","entry_close":469000,"price_basis":"tradable_raw","mfe_30d_pct":16.42,"mae_30d_pct":-3.94,"mfe_90d_pct":18.76,"mae_90d_pct":-5.12,"mfe_180d_pct":229.00,"mae_180d_pct":-5.12,"forward_high_30d":546000,"forward_low_30d":450500,"forward_high_90d":557000,"forward_low_90d":445000,"forward_high_180d":1543000,"forward_low_180d":445000,"calibration_usable":true,"case_role":"positive_control_with_contamination_cap","novelty_key":"C15_MATERIAL_SPREAD_SUPERCYCLE|010130|Stage2-Actionable|2024-04-09","non_price_bridge":"actual non-ferrous smelting / zinc and base-metal processing bridge","score_alignment":"early C15 positive, but later governance/tender event must cap C15 contribution"}
{"row_type":"trigger","schema_family":"v12_sector_archetype_residual","round":"R4","loop":103,"large_sector_id":"L4_MATERIALS_SPREAD_RESOURCE","canonical_archetype_id":"C15_MATERIAL_SPREAD_SUPERCYCLE","fine_archetype_id":"COPPER_PROCESSING_THEME_SPIKE_WITHOUT_MARGIN_CASH_BRIDGE","symbol":"025820","name":"이구산업","trigger_type":"Stage2-FalsePositive","entry_date":"2024-05-20","entry_close":7880,"price_basis":"tradable_raw","mfe_30d_pct":6.85,"mae_30d_pct":-33.88,"mfe_90d_pct":6.85,"mae_90d_pct":-51.84,"mfe_180d_pct":6.85,"mae_180d_pct":-55.01,"forward_high_30d":8420,"forward_low_30d":5210,"forward_high_90d":8420,"forward_low_90d":3795,"forward_high_180d":8420,"forward_low_180d":3545,"calibration_usable":true,"case_role":"counterexample","novelty_key":"C15_MATERIAL_SPREAD_SUPERCYCLE|025820|Stage2-FalsePositive|2024-05-20","non_price_bridge":"copper processing label without refreshed ASP-volume-margin-cash bridge","score_alignment":"small MFE followed by deep MAE; block Stage2-Actionable bonus"}
{"row_type":"trigger","schema_family":"v12_sector_archetype_residual","round":"R4","loop":103,"large_sector_id":"L4_MATERIALS_SPREAD_RESOURCE","canonical_archetype_id":"C15_MATERIAL_SPREAD_SUPERCYCLE","fine_archetype_id":"BRASS_COPPER_ALLOY_SMALLCAP_THEME_SPIKE_LOW_MFE_HIGH_MAE","symbol":"021050","name":"서원","trigger_type":"Stage2-FalsePositive","entry_date":"2024-05-20","entry_close":1916,"price_basis":"tradable_raw","mfe_30d_pct":4.65,"mae_30d_pct":-28.18,"mfe_90d_pct":4.65,"mae_90d_pct":-43.95,"mfe_180d_pct":4.65,"mae_180d_pct":-48.17,"forward_high_30d":2005,"forward_low_30d":1377,"forward_high_90d":2005,"forward_low_90d":1074,"forward_high_180d":2005,"forward_low_180d":993,"calibration_usable":true,"case_role":"counterexample","novelty_key":"C15_MATERIAL_SPREAD_SUPERCYCLE|021050|Stage2-FalsePositive|2024-05-20","non_price_bridge":"brass/copper-alloy theme label without listed-company spread conversion","score_alignment":"low-MFE/high-MAE; pure metal beta should not open C15 Stage2"}
{"row_type":"trigger","schema_family":"v12_sector_archetype_residual","round":"R4","loop":103,"large_sector_id":"L4_MATERIALS_SPREAD_RESOURCE","canonical_archetype_id":"C15_MATERIAL_SPREAD_SUPERCYCLE","fine_archetype_id":"STEEL_SPREAD_VALUE_LABEL_WITHOUT_DEMAND_MARGIN_BRIDGE","symbol":"004020","name":"현대제철","trigger_type":"Stage2-FalsePositive","entry_date":"2024-05-20","entry_close":32350,"price_basis":"tradable_raw","mfe_30d_pct":0.62,"mae_30d_pct":-11.90,"mfe_90d_pct":0.62,"mae_90d_pct":-24.73,"mfe_180d_pct":0.62,"mae_180d_pct":-38.49,"forward_high_30d":32550,"forward_low_30d":28500,"forward_high_90d":32550,"forward_low_90d":24350,"forward_high_180d":32550,"forward_low_180d":19900,"calibration_usable":true,"case_role":"counterexample","novelty_key":"C15_MATERIAL_SPREAD_SUPERCYCLE|004020|Stage2-FalsePositive|2024-05-20","non_price_bridge":"steel spread/value label without demand, margin or inventory gain bridge","score_alignment":"large-cap metal label also fails if MFE is absent and MAE expands"}
```

---

## 4. Case analysis

### Case A — 010130 고려아연: real smelting bridge, but later contamination cap

`고려아연` is the positive-control because it is not just a thin metal theme. It has an actual smelting / base-metal processing structure. The early price path after 2024-04-09 aligned with a metals/spread thesis: entry close 469,000, 2024-05-21 high 546,000, and 2024-08-28 high 557,000.

However, the later 2024-09~10 blow-off became dominated by governance/control-premium dynamics. That means C15 can learn the early smelting-spread bridge, but it must not absorb the entire 2024-10 tender-control premium as “material spread supercycle alpha.”

```text
C15 credit allowed until metal/smelting bridge window.
C15 contribution capped after governance/tender event begins to dominate.
```

### Case B — 025820 이구산업: copper beta spike without cash bridge

`이구산업` shows why C15 needs a conversion bridge. It reacted to copper-processing/copper-price vocabulary, but the stock path was not durable. Entry 2024-05-20 close 7,880, same-day high 8,420, then August low 3,795 and December low 3,545.

The market heard “copper.” The score should ask: “Does this company actually convert copper price into margin, cash, inventory gain, or revision?” Without that, the signal is just a bright flare over wet wood.

### Case C — 021050 서원: brass/copper-alloy label, low-MFE/high-MAE

`서원` is a cleaner small-cap false-positive. Entry 2024-05-20 close 1,916, forward high 2,005, then August low 1,074 and December low 993. The price path says the theme did not become company-level earnings power.

This strengthens the rule: copper-alloy vocabulary is not enough. C15 must require a company-level ASP/volume/spread bridge.

### Case D — 004020 현대제철: large-cap metal value label can also fail

`현대제철` is a useful large-cap counterexample. It did not have the small-cap theme spike; it simply failed to align. Entry 2024-05-20 close 32,350, forward high 32,550, then 2024-08-05 low 24,350 and 2024-12-09 low 19,900.

That matters because C15 should not only police small-cap metal spikes. Steel/low-PBR/commodity value labels can also become false positives when demand, spread, margin or inventory bridge is absent.

---

## 5. Aggregate score-return alignment

```yaml
new_independent_case_count: 4
cross_canonical_reused_symbol_count: 1
new_visible_C15_symbol_count: 4
same_archetype_new_trigger_family_count: 4
calibration_usable_case_count: 4
calibration_usable_trigger_count: 4
positive_case_count: 1
counterexample_count: 3
current_profile_error_count: 3
```

| symbol | role | 30D MFE/MAE | 90D MFE/MAE | 180D MFE/MAE | calibration lesson |
|---|---:|---:|---:|---:|---|
| 010130 | positive-control + cap | +16.42 / -3.94 | +18.76 / -5.12 | +229.00 / -5.12 | early C15 bridge valid; later governance contamination capped |
| 025820 | counterexample | +6.85 / -33.88 | +6.85 / -51.84 | +6.85 / -55.01 | copper beta without margin/cash bridge fails |
| 021050 | counterexample | +4.65 / -28.18 | +4.65 / -43.95 | +4.65 / -48.17 | copper-alloy small-cap theme fails |
| 004020 | counterexample | +0.62 / -11.90 | +0.62 / -24.73 | +0.62 / -38.49 | large-cap steel label also needs demand/margin bridge |

---

## 6. Current calibrated profile stress test

### Existing error risk

The current C15 profile can over-reward:

```text
metal price rally headline
+ copper / steel / zinc vocabulary
+ early volume spike
```

This is too loose. The examples here show that price beta is a symptom, not proof. A company is not a copper future with a CEO; it has inventory, hedges, purchase costs, selling prices, utilization and customer demand. The model should score the conversion path, not the metal word.

### Strengthened rule candidate

```text
C15_COMPANY_SPECIFIC_SPREAD_CONVERSION_REQUIREMENT

if C15
and metal_price_rally_or_commodity_beta == true
and company_specific_ASP_volume_inventory_margin_cash_bridge == false:
    stage2_actionable_bonus = 0
    max_stage = Stage2-Watch
```

### Low-MFE/high-MAE block

```text
C15_LOW_MFE_HIGH_MAE_FALSE_POSITIVE_BLOCK

if C15
and MFE_90D_pct < +10
and MAE_90D_pct <= -25
and refreshed_margin_or_cash_bridge == false:
    Stage2_FalsePositive_Block = true
```

### Contamination cap

```text
C15_NON_C15_EVENT_CONTAMINATION_CAP

if C15
and later_non_C15_event_dominates_price_path == true:
    cap_C15_contribution_after_contamination_date = true
    require_cross_archetype_reclassification = true
```

---

## 7. Residual contribution summary

```yaml
do_not_propose_new_weight_delta: false
sector_specific_rule_candidate: false
canonical_archetype_rule_candidate: true
loop_contribution_label: canonical_archetype_rule_candidate
new_axis_proposed: C15_LOW_MFE_HIGH_MAE_FALSE_POSITIVE_BLOCK
existing_axis_strengthened:
  - C15_company_specific_spread_conversion_requirement
  - C15_metal_price_beta_stage2_block_without_margin_cash_bridge
  - C15_low_MFE_high_MAE_false_positive_block
  - C15_non_C15_event_contamination_cap
existing_axis_weakened: null
```

---

## 8. Next recommended archetypes

```text
C16_STRATEGIC_RESOURCE_POLICY_SUPPLY
R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL
R13_CROSS_ARCHETYPE_STAGE2_FALSE_POSITIVE_REVIEW
C05_EPC_MEGA_CONTRACT_MARGIN_GAP
C18_CONSUMER_EXPORT_CHANNEL_REORDER
```
