# E2R v12 residual calibration research

## 0. Execution metadata

```yaml
schema_family: v12_sector_archetype_residual
selected_round: R6
selected_loop: 111
large_sector_id: L6_FINANCIAL_CAPITAL_RETURN_DIGITAL
canonical_archetype_id: C22_INSURANCE_RATE_CYCLE_RESERVE
fine_archetype_id: NONLIFE_RESERVE_CSM_CAPITAL_RETURN_BRIDGE_VS_LIFE_GA_DISTRIBUTION_LABEL_RECLASSIFICATION
selection_basis:
  main_execution_prompt: docs/core/e2r_v12_prompt_round_scheduler_corrected.txt
  no_repeat_index: docs/core/V12_Research_No_Repeat_Index.md
web_raw_fetch_status_this_turn:
  main_execution_prompt: read_ok
  no_repeat_index: read_ok
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

`C22_INSURANCE_RATE_CYCLE_RESERVE` remains Priority 0 in the no-repeat index: 6 representative rows, still 24 rows short of the 30-row minimum. The visible covered set is concentrated in `000540`, `000810`, `001450`, `003690`, `085620`, and `138930`, so this loop reuses and consolidates current-session C22 rows as a sector-specific rule formalization pass.

The previous local sector-specific C22 pass reached `R6/C22 loop 110`. This run continues as `R6/C22 loop 111`.

This is not a live insurance-stock screen. It is a historical calibration / residual rule file. Direct uncached symbol-shard fetch has been unstable in recent turns, so the trigger rows below reuse stock-web-derived local rows already calculated in this v12 session. Exact trigger keys should be deduped against C22 loop 109~110 and R13 financial/insurance guardrail rows if already represented. No production scoring is changed.

---

## 1. Research thesis

C22 is not `insurance stock + Value-up = Stage2`.

It is the insurance accounting bridge:

```text
rate cycle / reserve quality / CSM / loss ratio / solvency / capital return
→ earnings quality, book-value trust, payout capacity and price validation
```

The model must split six routes.

1. **Nonlife reserve/loss-ratio/capital-return positive-control**
   - Stage2 can remain open when reserve quality and capital-return bridge validate with meaningful MFE and controlled MAE.

2. **Reinsurance rate-cycle low-volatility control**
   - C22 may stay Stage2-Watch/Actionable if underwriting, reinsurance pricing and reserve discipline are visible, even if MFE is modest.

3. **Life-insurance / Value-up label with weak reserve-capital bridge**
   - Stage2 should be capped when CSM, solvency, reserve quality and shareholder-return bridge do not translate into price validation.

4. **GA / insurance-distribution commission bridge**
   - GA companies may have real distribution economics, but they are not reserve-cycle/solvency C22 cases.
   - Reclassify to distribution-commission axis and cap C22 contribution.

5. **GA high-MFE path**
   - High MFE can be tradable, but if the bridge is commission/distribution and not reserve/solvency, C22 Green must be blocked.

6. **Insurance label / financial beta without bridge**
   - Low MFE and meaningful MAE require Stage2 cap or false-positive block.

---

## 2. Validation scope

```yaml
validation_scope:
  required_cases: 5
  actual_cases: 5
  source_archetypes:
    - C22_INSURANCE_RATE_CYCLE_RESERVE
    - R13_CROSS_ARCHETYPE_STAGE2_FALSE_POSITIVE_REVIEW
    - R13_CROSS_ARCHETYPE_ACCOUNTING_TRUST_PRICE_VALIDATION
    - R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL
  price_windows:
    - 30D MFE/MAE
    - 90D MFE/MAE
    - 180D MFE/MAE
  output_use:
    - C22 canonical rule refinement
    - reserve/CSM/capital-return bridge split
    - GA/distribution reclassification guard
    - weak insurance label false-positive block
```

---

## 3. Source validation

```yaml
stock_web_manifest:
  source_name: FinanceData/marcap
  price_adjustment_status: raw_unadjusted_marcap
  max_date: 2026-02-20
  calibration_shard_root: atlas/ohlcv_tradable_by_symbol_year
  caveat: Raw/unadjusted OHLC; corporate-action contaminated windows blocked by default.
```

Local stock-web-derived row provenance:

```yaml
reused_price_rows_from_current_session:
  - e2r_stock_web_v12_residual_round_R6_loop_109_L6_FINANCIAL_CAPITAL_RETURN_DIGITAL_C22_INSURANCE_RATE_CYCLE_RESERVE_research.md
  - e2r_stock_web_v12_residual_round_R6_loop_110_L6_FINANCIAL_CAPITAL_RETURN_DIGITAL_C22_INSURANCE_RATE_CYCLE_RESERVE_research.md
  - R13 financial/insurance Stage2 false-positive, accounting-trust and high-MAE guardrail files
reason:
  - rows were already calculated from Songdaiki/stock-web tradable raw 1D OHLC
  - current file formalizes the sector-specific C22 reserve/CSM/capital-return rule after R13 checks
  - exact duplicate trigger keys should not be counted again as new aggregate rows
  - no production scoring changed
```

Symbol caveats:

```yaml
005830:
  name: DB손해보험
  role: nonlife reserve/loss-ratio/capital-return positive-control
  calibration_usable: true

003690:
  name: 코리안리
  role: reinsurance rate-cycle reserve low-volatility control
  calibration_usable: true
  no_repeat_note: visible-covered C22 symbol; use as control if deduped

088350:
  name: 한화생명
  role: life-insurance Value-up label weak bridge cap
  calibration_usable: true

244920:
  name: 에이플러스에셋
  role: GA insurance distribution commission bridge, not reserve-cycle C22
  calibration_usable: true

211050:
  name: 인카금융서비스
  role: GA distribution high-MFE path with corporate-action-adjacent local 4B watch
  calibration_usable: true
```

---

## 4. Trigger rows

```jsonl
{"row_type":"trigger","schema_family":"v12_sector_archetype_residual","round":"R6","loop":111,"large_sector_id":"L6_FINANCIAL_CAPITAL_RETURN_DIGITAL","canonical_archetype_id":"C22_INSURANCE_RATE_CYCLE_RESERVE","fine_archetype_id":"NONLIFE_RESERVE_LOSS_RATIO_CAPITAL_RETURN_POSITIVE_CONTROL","symbol":"005830","company_name":"DB손해보험","trigger_type":"Stage2-Actionable","trigger_date":"2024-02-26","entry_date":"2024-02-26","entry_price":95000,"price_data_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":15.79,"MAE_30D_pct":-4.11,"MFE_90D_pct":27.05,"MAE_90D_pct":-9.26,"MFE_180D_pct":30.53,"MAE_180D_pct":-9.26,"forward_high_30d":110000,"forward_low_30d":91100,"forward_high_90d":120700,"forward_low_90d":86200,"forward_high_180d":124000,"forward_low_180d":86200,"calibration_usable":true,"case_role":"positive_control","novelty_key":"C22_INSURANCE_RATE_CYCLE_RESERVE|005830|Stage2-Actionable|2024-02-26","trigger_outcome_label":"nonlife_reserve_capital_return_positive_control","current_profile_verdict":"current_profile_correct","non_price_bridge":"nonlife reserve quality, loss-ratio discipline and capital-return bridge","dedupe_for_aggregate":true,"aggregate_group_role":"representative","do_not_count_as_new_case":true,"reuse_reason":"current-session C22/R13 control row"}
{"row_type":"trigger","schema_family":"v12_sector_archetype_residual","round":"R6","loop":111,"large_sector_id":"L6_FINANCIAL_CAPITAL_RETURN_DIGITAL","canonical_archetype_id":"C22_INSURANCE_RATE_CYCLE_RESERVE","fine_archetype_id":"REINSURANCE_RATE_CYCLE_RESERVE_LOW_VOL_CONTROL","symbol":"003690","company_name":"코리안리","trigger_type":"Stage2-Watch","trigger_date":"2024-02-26","entry_date":"2024-02-26","entry_price":7930,"price_data_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":6.81,"MAE_30D_pct":-1.01,"MFE_90D_pct":6.81,"MAE_90D_pct":-5.42,"MFE_180D_pct":13.49,"MAE_180D_pct":-5.42,"forward_high_30d":8470,"forward_low_30d":7850,"forward_high_90d":8470,"forward_low_90d":7500,"forward_high_180d":9000,"forward_low_180d":7500,"calibration_usable":true,"case_role":"reused_reinsurance_control","novelty_key":"C22_INSURANCE_RATE_CYCLE_RESERVE|003690|Stage2-Watch|2024-02-26","trigger_outcome_label":"reinsurance_rate_cycle_low_vol_control","current_profile_verdict":"current_profile_watch_correct","non_price_bridge":"reinsurance pricing, reserve discipline and underwriting-cycle bridge","dedupe_for_aggregate":true,"aggregate_group_role":"control","do_not_count_as_new_case":true,"reuse_reason":"visible-covered C22 control row"}
{"row_type":"trigger","schema_family":"v12_sector_archetype_residual","round":"R6","loop":111,"large_sector_id":"L6_FINANCIAL_CAPITAL_RETURN_DIGITAL","canonical_archetype_id":"C22_INSURANCE_RATE_CYCLE_RESERVE","fine_archetype_id":"LIFE_INSURANCE_VALUEUP_LABEL_WITHOUT_SOLVENCY_CSM_CAPITAL_BRIDGE_CAP","symbol":"088350","company_name":"한화생명","trigger_type":"Stage2-Watch","trigger_date":"2024-02-26","entry_date":"2024-02-26","entry_price":3060,"price_data_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":9.31,"MAE_30D_pct":-8.17,"MFE_90D_pct":9.31,"MAE_90D_pct":-15.69,"MFE_180D_pct":9.31,"MAE_180D_pct":-15.69,"forward_high_30d":3345,"forward_low_30d":2810,"forward_high_90d":3345,"forward_low_90d":2580,"forward_high_180d":3345,"forward_low_180d":2580,"calibration_usable":true,"case_role":"stage2_cap","novelty_key":"C22_INSURANCE_RATE_CYCLE_RESERVE|088350|Stage2-Watch|2024-02-26","trigger_outcome_label":"life_insurance_valueup_label_stage2_cap","current_profile_verdict":"current_profile_false_positive_risk","non_price_bridge":"life-insurance value-up label without refreshed solvency, CSM, reserve or payout bridge","dedupe_for_aggregate":true,"aggregate_group_role":"representative","do_not_count_as_new_case":true,"reuse_reason":"current-session C22/R13 weak-label row"}
{"row_type":"trigger","schema_family":"v12_sector_archetype_residual","round":"R6","loop":111,"large_sector_id":"L6_FINANCIAL_CAPITAL_RETURN_DIGITAL","canonical_archetype_id":"C22_INSURANCE_RATE_CYCLE_RESERVE","fine_archetype_id":"GA_INSURANCE_DISTRIBUTION_COMMISSION_BRIDGE_RECLASSIFICATION_CAP","symbol":"244920","company_name":"에이플러스에셋","trigger_type":"Stage2-Watch","trigger_date":"2024-05-10","entry_date":"2024-05-10","entry_price":4100,"price_data_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":9.76,"MAE_30D_pct":-2.32,"MFE_90D_pct":9.76,"MAE_90D_pct":-13.78,"MFE_180D_pct":14.63,"MAE_180D_pct":-13.78,"forward_high_30d":4500,"forward_low_30d":4005,"forward_high_90d":4500,"forward_low_90d":3535,"forward_high_180d":4700,"forward_low_180d":3535,"calibration_usable":true,"case_role":"reclassification_cap","novelty_key":"C22_INSURANCE_RATE_CYCLE_RESERVE|244920|Stage2-Watch|2024-05-10","trigger_outcome_label":"GA_distribution_commission_bridge_reclassify","current_profile_verdict":"current_profile_reclassification_needed","non_price_bridge":"insurance distribution / GA commission bridge, not reserve quality or solvency bridge","dedupe_for_aggregate":true,"aggregate_group_role":"representative","do_not_count_as_new_case":true,"reuse_reason":"current-session C22 loop 110 GA row"}
{"row_type":"trigger","schema_family":"v12_sector_archetype_residual","round":"R6","loop":111,"large_sector_id":"L6_FINANCIAL_CAPITAL_RETURN_DIGITAL","canonical_archetype_id":"C22_INSURANCE_RATE_CYCLE_RESERVE","fine_archetype_id":"GA_DISTRIBUTION_HIGH_MFE_BUT_NOT_C22_GREEN_LOCAL_4B","symbol":"211050","company_name":"인카금융서비스","trigger_type":"Stage2-Watch","trigger_date":"2024-05-02","entry_date":"2024-05-02","entry_price":4925,"price_data_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":31.57,"MAE_30D_pct":-4.57,"MFE_90D_pct":31.57,"MAE_90D_pct":-16.35,"MFE_180D_pct":31.57,"MAE_180D_pct":-16.35,"forward_high_30d":6480,"forward_low_30d":4700,"forward_high_90d":6480,"forward_low_90d":4120,"forward_high_180d":6480,"forward_low_180d":4120,"calibration_usable":true,"case_role":"vertical_MFE_reclassification_watch","novelty_key":"C22_INSURANCE_RATE_CYCLE_RESERVE|211050|Stage2-Watch|2024-05-02","trigger_outcome_label":"GA_distribution_high_MFE_local_4B_reclassify","current_profile_verdict":"current_profile_overcredits_C22_if_not_reclassified","non_price_bridge":"GA distribution / commission platform economics after corporate-action-adjacent window; not reserve/solvency bridge","dedupe_for_aggregate":true,"aggregate_group_role":"representative","do_not_count_as_new_case":true,"reuse_reason":"current-session C22 loop 110 GA row"}
```

---

## 5. Case analysis

### 5.1 DB Insurance / 005830 — nonlife reserve and capital-return positive-control

DB Insurance is the C22 row the model should preserve. It had meaningful MFE and controlled drawdown.

```yaml
entry_close: 95000
30D_MFE_MAE: +15.79 / -4.11
90D_MFE_MAE: +27.05 / -9.26
180D_MFE_MAE: +30.53 / -9.26
route: keep Stage2
```

This is not generic insurance beta. The bridge is reserve quality, loss-ratio discipline and capital-return trust.

---

### 5.2 Korean Re / 003690 — reinsurance low-volatility control

Korean Re is a cleaner underwriting/rate-cycle control, but the MFE is more modest.

```yaml
entry_close: 7930
30D_MFE_MAE: +6.81 / -1.01
90D_MFE_MAE: +6.81 / -5.42
180D_MFE_MAE: +13.49 / -5.42
route: Stage2-Watch control
```

It should not be over-promoted, but it is economically closer to C22 than GA distribution cases.

---

### 5.3 Hanwha Life / 088350 — life-insurance value-up label cap

Hanwha Life is the weak-label guardrail. The stock had insufficient MFE and deeper MAE than the positive controls.

```yaml
entry_close: 3060
30D_MFE_MAE: +9.31 / -8.17
90D_MFE_MAE: +9.31 / -15.69
180D_MFE_MAE: +9.31 / -15.69
route: Stage2 cap
```

Life-insurance C22 requires CSM, solvency, reserve quality and payout evidence. Value-up label alone is not enough.

---

### 5.4 A Plus Asset / 244920 — GA distribution reclassification cap

A Plus Asset has an insurance-adjacent business, but its bridge is distribution commission economics.

```yaml
entry_close: 4100
30D_MFE_MAE: +9.76 / -2.32
90D_MFE_MAE: +9.76 / -13.78
180D_MFE_MAE: +14.63 / -13.78
route: reclassify / cap C22 contribution
```

The cash source can be real, but the taxonomy is wrong. C22 should not treat this as reserve-cycle validation.

---

### 5.5 INCA Financial Service / 211050 — high MFE but wrong C22 bridge

INCA produced large MFE, which makes it dangerous for price-only learning. But the bridge is GA distribution/commission economics, not C22 reserve or solvency.

```yaml
entry_close: 4925
30D_MFE_MAE: +31.57 / -4.57
90D_MFE_MAE: +31.57 / -16.35
180D_MFE_MAE: +31.57 / -16.35
route: local 4B / reclassify
```

C22 Green should be blocked unless reserve/solvency/rate-cycle bridge is present.

---

## 6. Score-return alignment

```yaml
new_independent_case_count: 0
reused_control_case_count: 5
calibration_usable_case_count: 5
calibration_usable_trigger_count: 5
positive_case_count: 2
counterexample_or_cap_count: 3
local_4B_or_reclassification_count: 2
current_profile_error_count: 3
duplicate_note: exact C22 novelty keys may already be represented in loops 109~110 or R13 financial/insurance guardrails; use this file as rule-formalization evidence unless batch ingest finds new keys
```

| symbol | role | 30D MFE/MAE | 90D MFE/MAE | 180D MFE/MAE | lesson |
|---|---:|---:|---:|---:|---|
| 005830 | positive-control | +15.79 / -4.11 | +27.05 / -9.26 | +30.53 / -9.26 | nonlife reserve/capital-return bridge validates |
| 003690 | reinsurance control | +6.81 / -1.01 | +6.81 / -5.42 | +13.49 / -5.42 | underwriting/rate-cycle bridge is cleaner than label beta |
| 088350 | weak life label cap | +9.31 / -8.17 | +9.31 / -15.69 | +9.31 / -15.69 | CSM/solvency/payout bridge needed |
| 244920 | GA reclassify cap | +9.76 / -2.32 | +9.76 / -13.78 | +14.63 / -13.78 | distribution commission is not reserve-cycle trust |
| 211050 | high-MFE reclassify | +31.57 / -4.57 | +31.57 / -16.35 | +31.57 / -16.35 | high MFE still not C22 Green if bridge is GA commission |

---

## 7. Raw component score breakdown

```jsonl
{"row_type":"score_simulation","profile_id":"P0","symbol":"005830","raw_component_scores_before":{"reserve_quality_score":4,"loss_ratio_quality_score":4,"rate_cycle_support_score":3,"CSM_or_solvency_score":3,"capital_return_execution_score":4,"commission_distribution_bridge":0,"validation_score":4,"label_only_risk":0},"weighted_score_before":78,"stage_label_before":"Stage2-Actionable","raw_component_scores_after":{"reserve_quality_score":5,"capital_return_execution_score":4,"label_only_risk":0},"weighted_score_after":81,"stage_label_after":"Stage2-Actionable","component_delta_explanation":"nonlife reserve and capital-return bridge validates with strong MFE and controlled MAE"}
{"row_type":"score_simulation","profile_id":"P0","symbol":"003690","raw_component_scores_before":{"reserve_quality_score":3,"loss_ratio_quality_score":2,"rate_cycle_support_score":3,"CSM_or_solvency_score":3,"capital_return_execution_score":2,"commission_distribution_bridge":0,"validation_score":2,"label_only_risk":0},"weighted_score_before":68,"stage_label_before":"Stage2-Watch","raw_component_scores_after":{"rate_cycle_support_score":4,"validation_score":2},"weighted_score_after":70,"stage_label_after":"Stage2-Watch","component_delta_explanation":"reinsurance bridge is economically clean but MFE remains modest"}
{"row_type":"score_simulation","profile_id":"P0","symbol":"088350","raw_component_scores_before":{"reserve_quality_score":1,"loss_ratio_quality_score":1,"rate_cycle_support_score":2,"CSM_or_solvency_score":1,"capital_return_execution_score":1,"commission_distribution_bridge":0,"validation_score":0,"label_only_risk":4},"weighted_score_before":60,"stage_label_before":"Stage2","raw_component_scores_after":{"CSM_or_solvency_score":0,"capital_return_execution_score":0,"label_only_risk":5},"weighted_score_after":50,"stage_label_after":"Stage2Cap","component_delta_explanation":"life-insurance value-up label lacks solvency, CSM and payout bridge"}
{"row_type":"score_simulation","profile_id":"P0","symbol":"244920","raw_component_scores_before":{"reserve_quality_score":0,"loss_ratio_quality_score":0,"rate_cycle_support_score":1,"CSM_or_solvency_score":0,"capital_return_execution_score":1,"commission_distribution_bridge":3,"validation_score":1,"label_only_risk":3},"weighted_score_before":58,"stage_label_before":"Stage2-Watch","raw_component_scores_after":{"reserve_quality_score":0,"commission_distribution_bridge":4,"label_only_risk":4},"weighted_score_after":54,"stage_label_after":"Stage2Cap_Reclassify","component_delta_explanation":"GA commission bridge belongs to distribution axis, not C22 reserve cycle"}
{"row_type":"score_simulation","profile_id":"P0","symbol":"211050","raw_component_scores_before":{"reserve_quality_score":0,"loss_ratio_quality_score":0,"rate_cycle_support_score":1,"CSM_or_solvency_score":0,"capital_return_execution_score":1,"commission_distribution_bridge":4,"validation_score":3,"label_only_risk":3},"weighted_score_before":66,"stage_label_before":"Stage2-Watch","raw_component_scores_after":{"reserve_quality_score":0,"commission_distribution_bridge":5,"validation_score":2,"label_only_risk":4},"weighted_score_after":61,"stage_label_after":"Local4B_Reclassify","component_delta_explanation":"high MFE is real but dominant bridge is GA distribution, not reserve/solvency C22"}
```

---

## 8. Profile comparison

```jsonl
{"row_type":"profile_comparison","profile_id":"P0","profile_scope":"baseline_current_proxy","profile_hypothesis":"e2r_2_2_current_proxy","eligible_trigger_count":5,"selected_entry_trigger_per_case":5,"avg_MFE_90D_pct":16.90,"avg_MAE_90D_pct":-12.10,"avg_MFE_180D_pct":20.71,"avg_MAE_180D_pct":-12.10,"false_positive_rate":0.40,"reclassification_needed_count":2,"score_return_alignment_verdict":"partially_aligned_but_GA_distribution_still_risks_overcredit"}
{"row_type":"profile_comparison","profile_id":"P1","profile_scope":"sector_specific_candidate_profile","profile_hypothesis":"require_reserve_CSM_solvency_or_capital_return_bridge","eligible_trigger_count":5,"selected_entry_trigger_per_case":5,"avg_MFE_90D_pct":16.90,"avg_MAE_90D_pct":-12.10,"avg_MFE_180D_pct":20.71,"avg_MAE_180D_pct":-12.10,"false_positive_rate":0.20,"reclassification_needed_count":2,"score_return_alignment_verdict":"better_bridge_filter_with_GA_reclassification"}
{"row_type":"profile_comparison","profile_id":"P2","profile_scope":"canonical_archetype_candidate_profile","profile_hypothesis":"C22_RESERVE_CSM_CAPITAL_RETURN_BRIDGE_REQUIREMENT_V111","eligible_trigger_count":5,"selected_entry_trigger_per_case":5,"avg_MFE_90D_pct":16.90,"avg_MAE_90D_pct":-12.10,"avg_MFE_180D_pct":20.71,"avg_MAE_180D_pct":-12.10,"false_positive_rate":0.20,"reclassification_needed_count":2,"score_return_alignment_verdict":"preferred_shadow_rule"}
```

---

## 9. Current calibrated profile stress test

### Existing error risk

C22 can still over-credit:

```text
insurance label
Value-up financial beta
GA / insurance-distribution adjacency
```

That is too broad. C22 should ask whether the insurer’s balance sheet became more trustworthy.

```text
reserve quality -> loss ratio -> CSM / solvency -> capital return -> price validation
```

A GA distributor may be a cash business, but it is not an insurance reserve book. It is a sales pipe, not the reservoir.

### Rule candidate

```text
C22_RESERVE_CSM_CAPITAL_RETURN_BRIDGE_REQUIREMENT_V111

if C22
and insurance_or_Valueup_label == true
and reserve_quality_CSM_solvency_loss_ratio_or_capital_return_bridge == false:
    stage2_actionable_bonus = 0
    max_stage = Stage2-Watch
```

```text
if C22
and nonlife_reserve_loss_ratio_capital_return_bridge == true
and MFE_90D_pct >= +20
and MAE_90D_pct > -10:
    keep_stage2_actionable_bonus = true
    allow_stage3_yellow_path = true
```

```text
if C22
and reinsurance_rate_cycle_reserve_bridge == true
and MFE_180D_pct >= +10
and MAE_180D_pct > -10:
    keep_stage2_watch_or_actionable = true
    use_as_low_vol_control = true
```

```text
if C22
and life_insurance_valueup_label == true
and CSM_solvency_capital_policy_bridge == false
and MFE_90D_pct < +10:
    route = Stage2Cap
    stage2_actionable_bonus = 0
```

```text
if C22
and insurance_distribution_or_GA_label == true
and reserve_quality_solvency_rate_cycle_bridge == false:
    route = Stage2Cap_ReclassifyToDistributionCommission
    block_C22_stage3_green = true
```

```text
if C22
and GA_distribution_commission_bridge == true
and MFE_30D_pct >= +25:
    local_4B_watch = true
    require_commission_cash_conversion_refresh = true
    do_not_score_as_C22_reserve_cycle_green = true
```

---

## 10. Residual contribution summary

```yaml
do_not_propose_new_weight_delta: false
sector_specific_rule_candidate: false
canonical_archetype_rule_candidate: true
loop_contribution_label: canonical_archetype_rule_formalization_from_existing_controls
new_axis_proposed: C22_RESERVE_CSM_CAPITAL_RETURN_BRIDGE_REQUIREMENT_V111
existing_axis_strengthened:
  - C22_insurance_label_not_enough_without_reserve_solvency_bridge
  - C22_nonlife_reserve_capital_return_positive_escape_hatch
  - C22_reinsurance_rate_cycle_low_vol_control
  - C22_life_insurance_valueup_label_stage2_cap
  - C22_GA_distribution_reclassification_guard
existing_axis_weakened: null
```

---

## 11. Deferred Coding Agent Handoff Prompt

```text
Do not patch production scoring from this MD alone. Batch this C22 loop with C22 loops 109~110 and adjacent R13 insurance/financial accounting-trust, high-MAE and Stage2 false-positive files. Extract `C22_RESERVE_CSM_CAPITAL_RETURN_BRIDGE_REQUIREMENT_V111` as a shadow-rule candidate. Preserve nonlife reserve/loss-ratio/capital-return and reinsurance rate-cycle controls; cap life-insurance value-up labels without CSM/solvency/payout bridge; reclassify GA/insurance-distribution commission cases away from C22 reserve-cycle scoring.
```

---

## 12. Next research state

```yaml
completed_round: R6
completed_loop: 111
selection_basis: docs/core/V12_Research_No_Repeat_Index.md
selected_priority_bucket: Priority 0
round_schedule_status: coverage_index_selected
round_sector_consistency: pass
next_recommended_archetypes:
  - C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY
  - C15_MATERIAL_SPREAD_SUPERCYCLE
  - R13_CROSS_ARCHETYPE_STAGE2_FALSE_POSITIVE_REVIEW
  - C18_CONSUMER_EXPORT_CHANNEL_REORDER
  - C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE
```
