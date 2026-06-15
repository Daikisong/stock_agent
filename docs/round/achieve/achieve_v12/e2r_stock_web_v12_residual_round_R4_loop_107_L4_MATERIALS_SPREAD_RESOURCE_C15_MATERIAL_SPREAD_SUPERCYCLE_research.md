# stock-web v12 residual research — R4/L4/C15 MATERIAL_SPREAD_SUPERCYCLE

## 0. Execution metadata

```yaml
mode: historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12
research_session: post_calibrated_sector_archetype_residual_research
selected_round: R4
selected_loop: 107
large_sector_id: L4_MATERIALS_SPREAD_RESOURCE
canonical_archetype_id: C15_MATERIAL_SPREAD_SUPERCYCLE
fine_archetype_id: COPPER_CONCENTRATE_SQUEEZE_DOWNSTREAM_FABRICATOR_MARGIN_BRIDGE_VS_COPPER_BETA_PRICE_ONLY_BLOWOFF
selection_basis: docs/core/V12_Research_No_Repeat_Index.md
selected_priority_bucket: Priority 1
round_schedule_status: coverage_index_selected
round_sector_consistency: pass
price_source: Songdaiki/stock-web
price_basis: tradable_raw
price_adjustment_status: raw_unadjusted_marcap
stock_web_manifest_max_date: 2026-02-20
stock_agent_code_access_allowed: false
stock_agent_code_patch_allowed: false
production_scoring_changed: false
shadow_weight_only: true
handoff_prompt_embedded: true
handoff_prompt_executed_now: false
```

This standalone Markdown follows the v12 requirement: no live candidate discovery, no code patching, no production scoring change. It only adds historical calibration cases with stock-web OHLCV rows and a deferred handoff prompt.

---

## 1. Why this loop / coverage gap

`C15_MATERIAL_SPREAD_SUPERCYCLE` is still in the Priority 1 reinforcement bucket. The current index shows 33 rows, so it is above the minimum stability threshold but still 17 rows short of the 50-row practical calibration target.

Earlier C15 work already used:
- 풍산 / copper spread positive
- 고려아연 / zinc local control with governance contamination
- 현대제철 / steel spread false rebound

This loop intentionally avoids that case set and uses copper downstream fabricators instead:
- 025820 이구산업
- 012800 대창
- 021050 서원

The shared macro trigger is the March 2024 copper raw-material squeeze: Chinese copper smelters agreed to cut output amid concentrate tightness and collapsing treatment charges, shifting the narrative from weak demand to stressed copper supply. This is a useful C15 test because downstream/fabricator equities often react as if copper price beta is automatically margin positive, but actual economics depend on inventory, pass-through, hedge timing, ASP, volume, and working-capital drag.

---

## 2. Price atlas verification

`Songdaiki/stock-web` manifest confirms:

```yaml
source_name: FinanceData/marcap
price_adjustment_status: raw_unadjusted_marcap
min_date: 1995-05-02
max_date: 2026-02-20
tradable_row_count: 14354401
calibration_shard_root: atlas/ohlcv_tradable_by_symbol_year
research_pack_default_price_basis: tradable_raw
zero_volume_rows_excluded_from_calibration_shards: true
corporate_action_contaminated_windows_blocked_by_default: true
```

All three selected windows are in 2024, far away from old corporate-action candidate dates in the relevant symbol profiles. Their old discontinuities are therefore noted but do not contaminate the 2024 calibration windows used here.

---

## 3. Case table

| case_id | symbol | name | trigger_date | entry_date | entry_price | peak_date | peak_high | trough_date | trough_low | MFE | MAE | classification |
|---|---:|---|---|---|---:|---|---:|---|---:|---:|---:|---|
| C15-R4L107-01 | 025820 | 이구산업 | 2024-03-14 | 2024-03-14 | 4,220 | 2024-05-20 | 8,420 | 2024-11-15 | 3,720 | +99.53% | -11.85% | positive_with_full_4B_watch |
| C15-R4L107-02 | 012800 | 대창 | 2024-03-14 | 2024-03-14 | 1,400 | 2024-05-21 | 2,320 | 2024-12-09 | 1,008 | +65.71% | -28.00% | high_MFE_high_MAE_counterexample |
| C15-R4L107-03 | 021050 | 서원 | 2024-03-14 | 2024-03-14 | 1,291 | 2024-05-21 | 2,005 | 2024-12-09 | 993 | +55.31% | -23.08% | high_MFE_high_MAE_counterexample |

Formula:
- `MFE = (forward_peak_high - entry_price) / entry_price`
- `MAE = (forward_trough_low - entry_price) / entry_price`
- The forward window is bounded by available 2024 calibration rows; the purpose is not live performance attribution but rule calibration against observed path risk.

---

## 4. Case notes

### 4.1 C15-R4L107-01 — 이구산업 / copper squeeze positive with 4B watch

**Thesis.**
The copper concentrate squeeze created a strong C15 spread-supercycle impulse. 이구산업 reacted like a high-beta copper downstream fabricator. The path confirms that the model should not discard all small/mid downstream copper names outright: when copper narrative pressure persists for several months, the early path can produce large MFE.

**OHLC evidence.**
- Entry row: 2024-03-14 close 4,220.
- Peak row: 2024-05-20 high 8,420.
- Later trough row: 2024-11-15 low 3,720.

**Interpretation.**
This is usable as a positive but not as a clean Green. The local positive phase was powerful, but full-window MAE later widened. A good C15 profile should allow Stage2-Actionable when copper squeeze + volume confirmation appears, but Stage3-Green should require a non-price bridge such as confirmed inventory gains, ASP pass-through, operating margin revision, or supply contract evidence.

---

### 4.2 C15-R4L107-02 — 대창 / copper beta blowoff counterexample

**Thesis.**
대창 shows the danger of treating a commodity-price squeeze as company-level earnings evidence. The MFE was high, but the path later gave back much of the move and produced a deep drawdown.

**OHLC evidence.**
- Entry row: 2024-03-14 close 1,400.
- Peak row: 2024-05-21 high 2,320.
- Full-window trough: 2024-12-09 low 1,008.

**Interpretation.**
This is a classic C15 high-MFE/high-MAE counterexample. The profile can give a tactical event-cap or 4B overlay, but if no margin/working-capital bridge appears, it should not become durable Stage3 evidence.

---

### 4.3 C15-R4L107-03 — 서원 / copper downstream sympathy counterexample

**Thesis.**
서원 confirms the same mechanism from a second, smaller downstream copper-brass name. The initial run looked like a spread-supercycle move, but the later path shows that copper beta without company-specific margin proof remains fragile.

**OHLC evidence.**
- Entry row: 2024-03-14 close 1,291.
- Peak row: 2024-05-21 high 2,005.
- Full-window trough: 2024-12-09 low 993.

**Interpretation.**
This is a second counterexample against broad copper-basket scoring. The model should avoid compressing “copper price up” into “all copper fabricators deserve Green.” Small cap liquidity, pass-through uncertainty, inventory timing, and demand elasticity can turn the same copper headline into a 4B/4C risk profile.

---

## 5. Residual error analysis

### Current profile likely error

The current calibrated profile can still misread:

```text
copper squeeze headline
+ material/supercycle keyword
+ strong 1D volume/price expansion
= Stage3-Yellow/Green-like signal
```

The residual error is not “copper does not work.” The error is **translation failure**:

```text
raw-material squeeze -> copper price beta -> downstream equity spike
does not automatically imply
company-specific spread-to-margin conversion
```

In lived-market terms, the commodity headline is the wind; the company’s margin structure is the sail. A sailboat can move fast with the wind, but if the sail is torn by inventory losses, hedges, weak demand, or working-capital drag, the same wind does not carry it very far.

---

## 6. Proposed shadow rule

```yaml
shadow_rule_id: c15_company_specific_spread_to_margin_bridge_required_for_stage2_actionable_shadow_only
scope:
  large_sector_id: L4_MATERIALS_SPREAD_RESOURCE
  canonical_archetype_id: C15_MATERIAL_SPREAD_SUPERCYCLE
trigger_family:
  - copper_concentrate_squeeze
  - copper_price_breakout
  - material_spread_supercycle
  - downstream_fabricator_beta
positive_evidence_required_for_stage2_actionable:
  any_two_of:
    - confirmed ASP/pass-through evidence
    - inventory gain or hedge timing evidence
    - operating margin or earnings revision evidence
    - volume/order/customer demand confirmation
    - company-specific supply or product mix bridge
downgrade_or_cap_conditions:
  - commodity price headline only
  - downstream beta with no margin bridge
  - high-MFE/high-MAE blowoff path
  - small-cap liquidity spike with no operating confirmation
recommended_score_effect_shadow_only:
  base_keyword_c15_score_cap: Stage2
  allow_stage2_actionable: true_if_positive_evidence_required_met
  block_stage3_green: true_if_only_commodity_beta
  add_4B_watch: true_if_MFE_gt_40pct_and_MAE_gt_15pct
  add_4C_watch: true_if_MFE_lt_10pct_or_full_window_MAE_lt_minus_20pct
production_scoring_changed_now: false
```

---

## 7. Machine-readable rows

### 7.1 case rows

```jsonl
{"row_type":"case","case_id":"C15-R4L107-01","canonical_archetype_id":"C15_MATERIAL_SPREAD_SUPERCYCLE","fine_archetype_id":"COPPER_CONCENTRATE_SQUEEZE_DOWNSTREAM_FABRICATOR_MARGIN_BRIDGE_VS_COPPER_BETA_PRICE_ONLY_BLOWOFF","large_sector_id":"L4_MATERIALS_SPREAD_RESOURCE","symbol":"025820","name":"이구산업","trigger_date":"2024-03-14","entry_date":"2024-03-14","entry_price":4220,"peak_date":"2024-05-20","peak_high":8420,"trough_date":"2024-11-15","trough_low":3720,"mfe_pct":99.53,"mae_pct":-11.85,"classification":"positive_with_full_4B_watch","calibration_usable":true,"evidence_family":"copper_concentrate_squeeze_downstream_fabricator","reused_case":false}
{"row_type":"case","case_id":"C15-R4L107-02","canonical_archetype_id":"C15_MATERIAL_SPREAD_SUPERCYCLE","fine_archetype_id":"COPPER_CONCENTRATE_SQUEEZE_DOWNSTREAM_FABRICATOR_MARGIN_BRIDGE_VS_COPPER_BETA_PRICE_ONLY_BLOWOFF","large_sector_id":"L4_MATERIALS_SPREAD_RESOURCE","symbol":"012800","name":"대창","trigger_date":"2024-03-14","entry_date":"2024-03-14","entry_price":1400,"peak_date":"2024-05-21","peak_high":2320,"trough_date":"2024-12-09","trough_low":1008,"mfe_pct":65.71,"mae_pct":-28.00,"classification":"high_MFE_high_MAE_counterexample","calibration_usable":true,"evidence_family":"copper_concentrate_squeeze_downstream_beta","reused_case":false}
{"row_type":"case","case_id":"C15-R4L107-03","canonical_archetype_id":"C15_MATERIAL_SPREAD_SUPERCYCLE","fine_archetype_id":"COPPER_CONCENTRATE_SQUEEZE_DOWNSTREAM_FABRICATOR_MARGIN_BRIDGE_VS_COPPER_BETA_PRICE_ONLY_BLOWOFF","large_sector_id":"L4_MATERIALS_SPREAD_RESOURCE","symbol":"021050","name":"서원","trigger_date":"2024-03-14","entry_date":"2024-03-14","entry_price":1291,"peak_date":"2024-05-21","peak_high":2005,"trough_date":"2024-12-09","trough_low":993,"mfe_pct":55.31,"mae_pct":-23.08,"classification":"high_MFE_high_MAE_counterexample","calibration_usable":true,"evidence_family":"copper_concentrate_squeeze_downstream_beta","reused_case":false}
```

### 7.2 trigger rows

```jsonl
{"row_type":"trigger","trigger_id":"TRG-C15-R4L107-COPPER-20240314","trigger_date":"2024-03-14","trigger_family":"copper_concentrate_squeeze","external_source_url":"https://www.reuters.com/markets/commodities/raw-materials-squeeze-jolts-copper-out-its-torpor-2024-03-14/","summary":"Copper market reactivated by concentrate squeeze, Chinese smelter output curbs, and collapsing spot treatment charges.","canonical_archetype_id":"C15_MATERIAL_SPREAD_SUPERCYCLE","evidence_quality":"verified_macro_trigger"}
{"row_type":"trigger","trigger_id":"TRG-C15-R4L107-COPPER-CUTS-20240313","trigger_date":"2024-03-13","trigger_family":"copper_smelter_production_cuts","external_source_url":"https://www.reuters.com/markets/commodities/chinas-top-copper-smelters-agree-production-cut-amid-raw-material-tightness-2024-03-13/","summary":"Chinese top copper smelters agreed to production cuts at some loss-making plants amid raw material tightness and decade-low spot treatment charges.","canonical_archetype_id":"C15_MATERIAL_SPREAD_SUPERCYCLE","evidence_quality":"verified_macro_trigger"}
```

### 7.3 score simulation rows

```jsonl
{"row_type":"score_simulation","canonical_archetype_id":"C15_MATERIAL_SPREAD_SUPERCYCLE","case_id":"C15-R4L107-01","current_profile_expected_stage":"Stage3-Yellow_or_Stage2_Actionable","observed_path":"large_MFE_but_full_window_4B_watch","residual_error":"would_overpromote_if_no_margin_bridge_required","proposed_shadow_adjustment":"require_company_specific_spread_to_margin_bridge_for_Green"}
{"row_type":"score_simulation","canonical_archetype_id":"C15_MATERIAL_SPREAD_SUPERCYCLE","case_id":"C15-R4L107-02","current_profile_expected_stage":"Stage3-Yellow_possible_due_price_volume","observed_path":"high_MFE_high_MAE_blowoff","residual_error":"commodity_beta_misread_as_margin_conversion","proposed_shadow_adjustment":"cap_at_Stage2_and_add_4B_watch_without_margin_bridge"}
{"row_type":"score_simulation","canonical_archetype_id":"C15_MATERIAL_SPREAD_SUPERCYCLE","case_id":"C15-R4L107-03","current_profile_expected_stage":"Stage2_or_Stage3-Yellow_possible_due_copper_theme","observed_path":"high_MFE_high_MAE_counterexample","residual_error":"downstream_sympathy_not_company_evidence","proposed_shadow_adjustment":"downgrade_price_only_copper_fabricator_spikes"}
```

### 7.4 aggregate row

```jsonl
{"row_type":"aggregate","selected_round":"R4","selected_loop":107,"large_sector_id":"L4_MATERIALS_SPREAD_RESOURCE","canonical_archetype_id":"C15_MATERIAL_SPREAD_SUPERCYCLE","new_independent_case_count":3,"reused_case_count":0,"same_archetype_new_symbol_count":3,"same_archetype_new_trigger_family_count":3,"calibration_usable_case_count":3,"calibration_usable_trigger_count":3,"positive_case_count":1,"counterexample_count":2,"current_profile_error_count":3,"verified_url_repair_needed_count":0,"sector_specific_rule_candidate":true,"canonical_archetype_rule_candidate":true,"loop_contribution_label":"canonical_archetype_rule_candidate","do_not_propose_new_weight_delta":false}
```

### 7.5 shadow weight row

```jsonl
{"row_type":"shadow_weight","shadow_rule_id":"c15_company_specific_spread_to_margin_bridge_required_for_stage2_actionable_shadow_only","large_sector_id":"L4_MATERIALS_SPREAD_RESOURCE","canonical_archetype_id":"C15_MATERIAL_SPREAD_SUPERCYCLE","rule_type":"cap_and_bridge_requirement","production_scoring_changed_now":false,"candidate_effect":"reduce false Stage3 promotions for commodity-beta downstream fabricator blowoffs","positive_gate":"allow Stage2-Actionable only with ASP/inventory/margin/volume bridge","negative_gate":"cap or downgrade copper-price-only downstream spikes"}
```

### 7.6 residual contribution row

```jsonl
{"row_type":"residual_contribution","loop":"R4L107","canonical_archetype_id":"C15_MATERIAL_SPREAD_SUPERCYCLE","new_axis_proposed":"c15_company_specific_spread_to_margin_bridge_required_for_stage2_actionable_shadow_only","existing_axis_strengthened":"full_4b_requires_non_price_evidence scoped to copper/downstream material beta rallies","existing_axis_weakened":null,"next_recommended_archetypes":["C18_CONSUMER_EXPORT_CHANNEL_REORDER","C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION","C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT"]}
```

---

## 8. Deferred Coding Agent Handoff Prompt

```text
You are a coding agent working on Songdaiki/stock_agent.
Do not use this handoff as proof that production scoring must be changed immediately.
Batch this MD together with other v12 residual research MDs before implementation.

Research artifact:
- e2r_stock_web_v12_residual_round_R4_loop_107_L4_MATERIALS_SPREAD_RESOURCE_C15_MATERIAL_SPREAD_SUPERCYCLE_research.md

Goal:
Evaluate a shadow-only C15 rule:
c15_company_specific_spread_to_margin_bridge_required_for_stage2_actionable_shadow_only

Implement only if a batch of C15/C17/L4 residual research artifacts supports the same direction.

Expected behavior:
- For C15 material spread rallies, do not treat commodity-price headlines alone as Stage3-Green evidence.
- Allow Stage2-Actionable if there is credible company-specific evidence: ASP/pass-through, inventory gain, hedge timing, OPM/revision, volume/order/customer bridge.
- Add 4B watch when MFE is high but full-window MAE exceeds approximately 15%.
- Downgrade copper downstream beta names with no company bridge.
- Keep production scoring unchanged until batch approval.

Do not re-open live scans. Use only validated historical rows.
```

---

## 9. Final summary

```yaml
new_independent_case_count: 3
reused_case_count: 0
same_archetype_new_symbol_count: 3
same_archetype_new_trigger_family_count: 3
calibration_usable_case_count: 3
calibration_usable_trigger_count: 3
positive_case_count: 1
counterexample_count: 2
current_profile_error_count: 3
verified_url_repair_needed_count: 0
diversity_score_summary: C15 Priority 1 보강 + 이구산업 copper downstream positive-with-4B-watch + 대창/서원 copper-beta high-MFE/high-MAE counterexamples
do_not_propose_new_weight_delta: false
auto_selected_coverage_gap: C15 rows 33, 50-row target까지 17 부족
sector_specific_rule_candidate: true
canonical_archetype_rule_candidate: true
loop_contribution_label: canonical_archetype_rule_candidate
new_axis_proposed: c15_company_specific_spread_to_margin_bridge_required_for_stage2_actionable_shadow_only
existing_axis_strengthened: full_4b_requires_non_price_evidence scoped to C15 copper/downstream material beta rallies
existing_axis_weakened: null
next_recommended_archetypes:
  - C18_CONSUMER_EXPORT_CHANNEL_REORDER
  - C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION
  - C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT
```
