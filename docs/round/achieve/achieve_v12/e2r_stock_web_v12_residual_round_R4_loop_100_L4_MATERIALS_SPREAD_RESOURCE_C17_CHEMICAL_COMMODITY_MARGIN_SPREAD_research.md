# E2R Stock-Web v12 Residual Research — R4 / C17 Chemical Commodity Margin Spread

```yaml
research_session: post_calibrated_sector_archetype_residual_research
mode: historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12
selected_round: R4
selected_loop: 100
large_sector_id: L4_MATERIALS_SPREAD_RESOURCE
canonical_archetype_id: C17_CHEMICAL_COMMODITY_MARGIN_SPREAD
fine_archetype_id: REFINING_SPREAD_SPANDEX_AND_CHEMICAL_MARGIN_BRIDGE_VS_COMMODITY_LABEL_FALSE_POSITIVE
selection_basis: docs/core/V12_Research_No_Repeat_Index.md
selected_priority_bucket: Priority 0
round_schedule_status: coverage_index_selected
round_sector_consistency: pass
price_source: Songdaiki/stock-web
price_basis: tradable_raw
source_basis: FinanceData/marcap transformed into assistant-readable symbol-year CSV shards
price_adjustment_status: raw_unadjusted_marcap
stock_web_manifest_max_date: 2026-02-20
production_scoring_changed: false
shadow_weight_only: true
handoff_prompt_embedded: true
handoff_prompt_executed_now: false
standard_v12_result_filename: e2r_stock_web_v12_residual_round_R4_loop_100_L4_MATERIALS_SPREAD_RESOURCE_C17_CHEMICAL_COMMODITY_MARGIN_SPREAD_research.md
```

---

## 1. Selection and no-repeat rationale

The No-Repeat Index shows **C17_CHEMICAL_COMMODITY_MARGIN_SPREAD** at 12 representative rows, still Priority 0. Existing high-repeat C17 symbols include `011780`, `011170`, `004000`, `006650`, `014680`, and `014830`; this run avoids those and adds four distinct symbols and four distinct trigger families.

```text
previous_C17_rows: 12
new_independent_case_count: 4
reused_case_count: 0
same_archetype_new_symbol_count: 4
same_archetype_new_trigger_family_count: 4
coverage_if_accepted: 12 -> 16
still_priority_0_gap_to_30: 14
```

Selected symbols:

| symbol | name | reason for inclusion | no-repeat status |
|---|---|---|---|
| 010950 | S-Oil | refining spread / crack-margin proxy with later fade | new for C17 sample set |
| 298020 | 효성티앤씨 | spandex / textile chemical spread recovery with high-MAE tail | new for C17 sample set |
| 051910 | LG화학 | petrochemical/battery vocabulary false positive; weak commodity-margin bridge | new for C17 sample set |
| 011790 | SKC | chemical/material rerating with violent price MFE but bridge fragility | new for C17 sample set |

---

## 2. Validation scope

```text
validation_scope = stock_web_1D_tradable_ohlcv_only
used_shard_root = atlas/ohlcv_tradable_by_symbol_year
raw_reference_only = false
current_stock_discovery = false
live_scan = false
price_route_hunt = false
stock_agent_code_access = false
```

Source files checked:

```text
atlas/manifest.json
atlas/symbol_profiles/010/010950.json
atlas/symbol_profiles/298/298020.json
atlas/symbol_profiles/051/051910.json
atlas/symbol_profiles/011/011790.json
atlas/ohlcv_tradable_by_symbol_year/010/010950/2024.csv
atlas/ohlcv_tradable_by_symbol_year/298/298020/2024.csv
atlas/ohlcv_tradable_by_symbol_year/051/051910/2024.csv
atlas/ohlcv_tradable_by_symbol_year/011/011790/2024.csv
```

Corporate-action contamination screen:

| symbol | corporate-action profile | 2024 calibration window contamination |
|---|---|---|
| 010950 | older raw discontinuity only; candidate date 2001-12-03 | no 2024 blocked date inside selected window |
| 298020 | no corporate-action candidate | clean |
| 051910 | no corporate-action candidate | clean |
| 011790 | older raw discontinuities only; candidate dates 1998-01-03 / 2001-12-21 | no 2024 blocked date inside selected window |

---

## 3. Case-level thesis summary

### Case A — 010950 / S-Oil / refining-spread rebound that should remain Stage2 until margin evidence follows

`010950` produced a clean but ultimately capped 2024 price path. The 2024-02-13 entry at 71,500 produced a quick peak of 84,500 by early April, but the same 180D window later reached a low of 56,900. This is not a hard 4C: it is a **local 4B / Stage2 durability problem**. The important C17 lesson is that refining or chemical spread vocabulary can catch a tradable Stage2, but the model should not promote it toward Green unless spread durability converts into earnings revision and FCF visibility.

```text
classification: mixed_positive_with_later_4B_watch
residual_error: current profile may over-credit commodity rebound if non-price margin revision evidence is thin
rule_need: require spread-to-company-margin bridge before Stage3-Yellow/Green
```

### Case B — 298020 / 효성티앤씨 / spandex spread rebound with large MFE but unacceptable high-MAE tail

`298020` is the cleanest positive in this set at first glance. A 2024-03-29 entry at 324,500 saw a 421,500 peak, roughly +29.9% MFE. But the same window later drew down to 192,000, roughly -40.8% MAE. This is precisely why C17 should not read “spread supercycle” as a one-way path. It deserves Stage2-Actionable when spread recovery is visible, but it needs a **high-MAE guardrail** unless inventory, ASP, utilization, and margin revision confirm that the spread is persistent.

```text
classification: positive_price_path_with_high_MAE_guardrail
residual_error: MFE is captured, but post-peak loss is too large for Green-style scoring
rule_need: require margin persistence and operating leverage confirmation before extending Stage2 into Stage3
```

### Case C — 051910 / LG화학 / commodity-chemical vocabulary false positive

`051910` is the counterexample. A 2024-02-16 entry at 504,000 barely reached 520,000, but the 180D low was 263,500. The model should treat broad “chemical rebound” language as insufficient when the company-level bridge is diluted by battery exposure, weak petrochemical spread conversion, and absent revision confirmation. This case strengthens a **Stage2 false-positive review** axis inside C17.

```text
classification: counterexample
residual_error: overbroad chemical-cycle label would create poor score-return alignment
rule_need: block Stage2-Actionable if company-specific commodity margin bridge is missing
```

### Case D — 011790 / SKC / violent material/chemical rerating requiring local 4B guard

`011790` generated a very large MFE after a 2024-03-14 entry: from 114,700 to 200,000 at the June high. But it later fell to 93,400 during the 180D window. This is not a “missed winner” case only; it is a **positive-MFE / high-MAE dual case**. The correct calibration is to allow Stage2-Actionable when evidence is fresh, but to force local 4B after the blowoff unless non-price evidence confirms margin durability.

```text
classification: positive_MFE_with_local_4B_after_blowoff
residual_error: price-only continuation would overstay the rerating
rule_need: blowoff proximity + high MAE guard for C17 commodity/material spikes
```

---

## 4. Trigger-level backtest table

| symbol | name | trigger_type | entry_date | entry_price | MFE_30D | MAE_30D | MFE_90D | MAE_90D | MFE_180D | MAE_180D | outcome |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| 010950 | S-Oil | Stage2-Actionable | 2024-02-13 | 71,500 | +11.75% | -1.40% | +18.18% | -7.13% | +18.18% | -20.42% | mixed positive / later 4B watch |
| 298020 | 효성티앤씨 | Stage2-Actionable | 2024-03-29 | 324,500 | +21.57% | -5.70% | +29.89% | -17.57% | +29.89% | -40.83% | positive with high-MAE guard |
| 051910 | LG화학 | Stage2 | 2024-02-16 | 504,000 | +3.17% | -14.68% | +3.17% | -30.56% | +3.17% | -47.72% | counterexample |
| 011790 | SKC | Stage2-Actionable | 2024-03-14 | 114,700 | +30.51% | -4.53% | +74.37% | -11.68% | +74.37% | -18.57% | positive MFE with local 4B guard |

---

## 5. Machine-readable rows

### 5.1 case rows JSONL

```jsonl
{"row_type":"case","selected_round":"R4","selected_loop":100,"large_sector_id":"L4_MATERIALS_SPREAD_RESOURCE","canonical_archetype_id":"C17_CHEMICAL_COMMODITY_MARGIN_SPREAD","fine_archetype_id":"REFINING_SPREAD_SPANDEX_AND_CHEMICAL_MARGIN_BRIDGE_VS_COMMODITY_LABEL_FALSE_POSITIVE","symbol":"010950","name":"S-Oil","case_role":"mixed_positive_with_later_4B_watch","novelty":"new_symbol_for_C17","source_price_file":"atlas/ohlcv_tradable_by_symbol_year/010/010950/2024.csv","profile_file":"atlas/symbol_profiles/010/010950.json"}
{"row_type":"case","selected_round":"R4","selected_loop":100,"large_sector_id":"L4_MATERIALS_SPREAD_RESOURCE","canonical_archetype_id":"C17_CHEMICAL_COMMODITY_MARGIN_SPREAD","fine_archetype_id":"REFINING_SPREAD_SPANDEX_AND_CHEMICAL_MARGIN_BRIDGE_VS_COMMODITY_LABEL_FALSE_POSITIVE","symbol":"298020","name":"효성티앤씨","case_role":"positive_with_high_MAE_guardrail","novelty":"new_symbol_for_C17","source_price_file":"atlas/ohlcv_tradable_by_symbol_year/298/298020/2024.csv","profile_file":"atlas/symbol_profiles/298/298020.json"}
{"row_type":"case","selected_round":"R4","selected_loop":100,"large_sector_id":"L4_MATERIALS_SPREAD_RESOURCE","canonical_archetype_id":"C17_CHEMICAL_COMMODITY_MARGIN_SPREAD","fine_archetype_id":"REFINING_SPREAD_SPANDEX_AND_CHEMICAL_MARGIN_BRIDGE_VS_COMMODITY_LABEL_FALSE_POSITIVE","symbol":"051910","name":"LG화학","case_role":"counterexample","novelty":"new_symbol_for_C17","source_price_file":"atlas/ohlcv_tradable_by_symbol_year/051/051910/2024.csv","profile_file":"atlas/symbol_profiles/051/051910.json"}
{"row_type":"case","selected_round":"R4","selected_loop":100,"large_sector_id":"L4_MATERIALS_SPREAD_RESOURCE","canonical_archetype_id":"C17_CHEMICAL_COMMODITY_MARGIN_SPREAD","fine_archetype_id":"REFINING_SPREAD_SPANDEX_AND_CHEMICAL_MARGIN_BRIDGE_VS_COMMODITY_LABEL_FALSE_POSITIVE","symbol":"011790","name":"SKC","case_role":"positive_MFE_with_local_4B_after_blowoff","novelty":"new_symbol_for_C17","source_price_file":"atlas/ohlcv_tradable_by_symbol_year/011/011790/2024.csv","profile_file":"atlas/symbol_profiles/011/011790.json"}
```

### 5.2 trigger rows JSONL

```jsonl
{"row_type":"trigger","selected_round":"R4","selected_loop":100,"large_sector_id":"L4_MATERIALS_SPREAD_RESOURCE","canonical_archetype_id":"C17_CHEMICAL_COMMODITY_MARGIN_SPREAD","fine_archetype_id":"REFINING_SPREAD_SPANDEX_AND_CHEMICAL_MARGIN_BRIDGE_VS_COMMODITY_LABEL_FALSE_POSITIVE","symbol":"010950","name":"S-Oil","trigger_type":"Stage2-Actionable","trigger_subtype":"refining_spread_rebound_requires_margin_revision_bridge","entry_date":"2024-02-13","entry_price":71500,"price_source":"Songdaiki/stock-web","price_basis":"tradable_raw","MFE_30D_pct":11.75,"MAE_30D_pct":-1.40,"MFE_90D_pct":18.18,"MAE_90D_pct":-7.13,"MFE_180D_pct":18.18,"MAE_180D_pct":-20.42,"peak_price_30D":79900,"trough_price_30D":70500,"peak_price_90D":84500,"trough_price_90D":66400,"peak_price_180D":84500,"trough_price_180D":56900,"outcome_label":"mixed_positive_later_4B_watch","corporate_action_contamination":"none_in_2024_window","current_profile_error":"spread_vocabulary_can_overstay_without_margin_revision"}
{"row_type":"trigger","selected_round":"R4","selected_loop":100,"large_sector_id":"L4_MATERIALS_SPREAD_RESOURCE","canonical_archetype_id":"C17_CHEMICAL_COMMODITY_MARGIN_SPREAD","fine_archetype_id":"REFINING_SPREAD_SPANDEX_AND_CHEMICAL_MARGIN_BRIDGE_VS_COMMODITY_LABEL_FALSE_POSITIVE","symbol":"298020","name":"효성티앤씨","trigger_type":"Stage2-Actionable","trigger_subtype":"spandex_spread_recovery_requires_inventory_ASP_margin_persistence","entry_date":"2024-03-29","entry_price":324500,"price_source":"Songdaiki/stock-web","price_basis":"tradable_raw","MFE_30D_pct":21.57,"MAE_30D_pct":-5.70,"MFE_90D_pct":29.89,"MAE_90D_pct":-17.57,"MFE_180D_pct":29.89,"MAE_180D_pct":-40.83,"peak_price_30D":394500,"trough_price_30D":306000,"peak_price_90D":421500,"trough_price_90D":267500,"peak_price_180D":421500,"trough_price_180D":192000,"outcome_label":"positive_MFE_high_MAE_guardrail","corporate_action_contamination":"none","current_profile_error":"positive_path_but_high_MAE_requires_local_4B_guard"}
{"row_type":"trigger","selected_round":"R4","selected_loop":100,"large_sector_id":"L4_MATERIALS_SPREAD_RESOURCE","canonical_archetype_id":"C17_CHEMICAL_COMMODITY_MARGIN_SPREAD","fine_archetype_id":"REFINING_SPREAD_SPANDEX_AND_CHEMICAL_MARGIN_BRIDGE_VS_COMMODITY_LABEL_FALSE_POSITIVE","symbol":"051910","name":"LG화학","trigger_type":"Stage2","trigger_subtype":"overbroad_chemical_rebound_label_without_company_margin_bridge","entry_date":"2024-02-16","entry_price":504000,"price_source":"Songdaiki/stock-web","price_basis":"tradable_raw","MFE_30D_pct":3.17,"MAE_30D_pct":-14.68,"MFE_90D_pct":3.17,"MAE_90D_pct":-30.56,"MFE_180D_pct":3.17,"MAE_180D_pct":-47.72,"peak_price_30D":520000,"trough_price_30D":430000,"peak_price_90D":520000,"trough_price_90D":350000,"peak_price_180D":520000,"trough_price_180D":263500,"outcome_label":"counterexample","corporate_action_contamination":"none","current_profile_error":"commodity_chemical_label_false_positive"}
{"row_type":"trigger","selected_round":"R4","selected_loop":100,"large_sector_id":"L4_MATERIALS_SPREAD_RESOURCE","canonical_archetype_id":"C17_CHEMICAL_COMMODITY_MARGIN_SPREAD","fine_archetype_id":"REFINING_SPREAD_SPANDEX_AND_CHEMICAL_MARGIN_BRIDGE_VS_COMMODITY_LABEL_FALSE_POSITIVE","symbol":"011790","name":"SKC","trigger_type":"Stage2-Actionable","trigger_subtype":"material_chemical_price_MFE_requires_blowoff_and_margin_bridge_guard","entry_date":"2024-03-14","entry_price":114700,"price_source":"Songdaiki/stock-web","price_basis":"tradable_raw","MFE_30D_pct":30.51,"MAE_30D_pct":-4.53,"MFE_90D_pct":74.37,"MAE_90D_pct":-11.68,"MFE_180D_pct":74.37,"MAE_180D_pct":-18.57,"peak_price_30D":149700,"trough_price_30D":109500,"peak_price_90D":200000,"trough_price_90D":101300,"peak_price_180D":200000,"trough_price_180D":93400,"outcome_label":"positive_MFE_local_4B_after_blowoff","corporate_action_contamination":"none_in_2024_window","current_profile_error":"price_only_blowoff_can_overextend_stage2_actionable"}
```

### 5.3 score simulation rows JSONL

```jsonl
{"row_type":"score_simulation","symbol":"010950","canonical_archetype_id":"C17_CHEMICAL_COMMODITY_MARGIN_SPREAD","raw_component_score_breakdown":{"EPS_FCF_Explosion":12,"Earnings_Visibility_Quality":13,"Bottleneck_Pricing_Power":12,"Market_Mispricing":11,"Valuation_Rerating_Runway":10,"Capital_Allocation":4,"Information_Confidence":5},"base_total":67,"stage_before_shadow":"Stage2-Actionable","shadow_adjustment":"cap_to_Stage2_watch_unless_margin_revision_confirms","stage_after_shadow":"Stage2-Actionable / local_4B_watch"}
{"row_type":"score_simulation","symbol":"298020","canonical_archetype_id":"C17_CHEMICAL_COMMODITY_MARGIN_SPREAD","raw_component_score_breakdown":{"EPS_FCF_Explosion":15,"Earnings_Visibility_Quality":14,"Bottleneck_Pricing_Power":13,"Market_Mispricing":12,"Valuation_Rerating_Runway":11,"Capital_Allocation":4,"Information_Confidence":5},"base_total":74,"stage_before_shadow":"Stage2-Actionable","shadow_adjustment":"high_MAE_guardrail_blocks_Green_style_extension","stage_after_shadow":"Stage2-Actionable / 4B_watch_after_peak"}
{"row_type":"score_simulation","symbol":"051910","canonical_archetype_id":"C17_CHEMICAL_COMMODITY_MARGIN_SPREAD","raw_component_score_breakdown":{"EPS_FCF_Explosion":8,"Earnings_Visibility_Quality":9,"Bottleneck_Pricing_Power":7,"Market_Mispricing":9,"Valuation_Rerating_Runway":8,"Capital_Allocation":4,"Information_Confidence":4},"base_total":49,"stage_before_shadow":"Stage2_if_overbroad_label_used","shadow_adjustment":"block_Stage2_Actionable_without_company_margin_bridge","stage_after_shadow":"Stage1_or_Stage2_watch_only"}
{"row_type":"score_simulation","symbol":"011790","canonical_archetype_id":"C17_CHEMICAL_COMMODITY_MARGIN_SPREAD","raw_component_score_breakdown":{"EPS_FCF_Explosion":14,"Earnings_Visibility_Quality":13,"Bottleneck_Pricing_Power":14,"Market_Mispricing":12,"Valuation_Rerating_Runway":12,"Capital_Allocation":4,"Information_Confidence":6},"base_total":75,"stage_before_shadow":"Stage2-Actionable","shadow_adjustment":"local_4B_after_blowoff_unless_non_price_bridge_confirms","stage_after_shadow":"Stage2-Actionable then local_4B_watch"}
```

### 5.4 aggregate rows JSONL

```jsonl
{"row_type":"aggregate","selected_round":"R4","selected_loop":100,"large_sector_id":"L4_MATERIALS_SPREAD_RESOURCE","canonical_archetype_id":"C17_CHEMICAL_COMMODITY_MARGIN_SPREAD","trigger_count":4,"positive_case_count":1,"mixed_positive_count":2,"counterexample_count":1,"local_4b_watch_count":3,"current_profile_error_count":4,"avg_MFE_30D_pct":16.75,"avg_MAE_30D_pct":-6.58,"avg_MFE_90D_pct":31.40,"avg_MAE_90D_pct":-16.74,"avg_MFE_180D_pct":31.40,"avg_MAE_180D_pct":-31.88,"median_MFE_180D_pct":24.04,"median_MAE_180D_pct":-30.63,"rule_candidate":"C17_company_margin_bridge_and_high_MAE_guardrail"}
```

### 5.5 shadow rule candidate JSONL

```jsonl
{"row_type":"shadow_rule","large_sector_id":"L4_MATERIALS_SPREAD_RESOURCE","canonical_archetype_id":"C17_CHEMICAL_COMMODITY_MARGIN_SPREAD","new_axis_proposed":"C17_company_margin_bridge_required","rule_text":"For C17, commodity/refining/chemical spread vocabulary may open Stage2 only when company-level margin bridge is present; Stage2-Actionable requires evidence of spread-to-OPM or spread-to-FCF conversion, not just commodity price sympathy.","safe_axis":"stage2_required_bridge","expected_effect":"reduce LG화학-like false positives while preserving S-Oil/SKC/효성티앤씨 early MFE capture"}
{"row_type":"shadow_rule","large_sector_id":"L4_MATERIALS_SPREAD_RESOURCE","canonical_archetype_id":"C17_CHEMICAL_COMMODITY_MARGIN_SPREAD","new_axis_proposed":"C17_high_MAE_after_spread_blowoff_guard","rule_text":"When C17 MFE is price-only and 90D/180D MAE risk is high, force local 4B watch unless fresh non-price revision, inventory, utilization, ASP, and margin persistence evidence appear.","safe_axis":"local_4b_watch_guard","expected_effect":"avoid overstaying spandex/material/chemical blowoff paths after large MFE"}
```

### 5.6 residual contribution row JSONL

```jsonl
{"row_type":"residual_contribution","selected_round":"R4","selected_loop":100,"large_sector_id":"L4_MATERIALS_SPREAD_RESOURCE","canonical_archetype_id":"C17_CHEMICAL_COMMODITY_MARGIN_SPREAD","loop_contribution_label":"canonical_archetype_rule_candidate","new_axis_proposed":"C17_company_margin_bridge_required | C17_high_MAE_after_spread_blowoff_guard","existing_axis_strengthened":"stage2_required_bridge | price_only_blowoff_blocks_positive_stage | full_4b_requires_non_price_evidence | local_4b_watch_guard | high_MAE_guardrail","existing_axis_weakened":null,"do_not_propose_new_weight_delta":false,"why_it_matters":"C17 is not merely a commodity beta bucket; it needs company-level spread-to-margin conversion and high-MAE control."}
```

---

## 6. Score-return alignment notes

C17’s central failure mode is **good MFE with bad survival quality**. That shape is clear in the aggregate:

```text
average_30D_MFE: +16.75%
average_30D_MAE: -6.58%
average_90D_MFE: +31.40%
average_90D_MAE: -16.74%
average_180D_MFE: +31.40%
average_180D_MAE: -31.88%
```

This means the model can capture early Stage2 moves, but the same ruleset should not promote price-only spread spikes too far. The core shadow calibration should therefore not be a raw weight increase. It should be a **bridge-and-guard pair**:

```text
1. company-level spread-to-margin bridge required for Stage2-Actionable
2. high-MAE / local-4B guard after spread-driven blowoff
```

---

## 7. Current calibrated profile stress test

Current global calibrated profile already includes:

```text
stage2_actionable_evidence_bonus = +2.0
price_only_blowoff_blocks_positive_stage = true
full_4b_requires_non_price_evidence = true
hard_4c_thesis_break_routes_to_4c = true
```

C17-specific residual errors after this run:

| residual | evidence from cases | proposed fix |
|---|---|---|
| overbroad commodity label | 051910 produced only +3.17% MFE and -47.72% 180D MAE | block Stage2-Actionable without company margin bridge |
| positive MFE but high MAE | 298020 produced +29.89% MFE and -40.83% 180D MAE | add high-MAE / local 4B guard |
| spread rebound fades | 010950 peaked +18.18% but later fell -20.42% | do not upgrade beyond Stage2 without revision/FCF confirmation |
| price-only chemical/material blowoff | 011790 ran +74.37% but later -18.57% | local 4B after blowoff unless non-price bridge appears |

---

## 8. Positive and counterexample balance

```text
positive_case_count: 1
mixed_positive_count: 2
counterexample_count: 1
local_4b_watch_count: 3
current_profile_error_count: 4
```

Positive:

```text
298020: spandex spread recovery had large MFE but must be guarded because 180D MAE became extreme.
```

Mixed positives:

```text
010950: refining spread rebound worked early but decayed.
011790: very large MFE but price-only extension required local 4B guard.
```

Counterexample:

```text
051910: broad chemical-cycle label was not enough; weak score-return alignment.
```

---

## 9. Deferred Coding Agent Handoff Prompt

```text
You are a coding agent working in Songdaiki/stock_agent after a batch of v12 research MDs has been collected.

Do not apply this single MD directly without batch comparison.

When implementing, inspect all C17_CHEMICAL_COMMODITY_MARGIN_SPREAD v12 research rows and test whether the following canonical-archetype-specific shadow rules are supported:

1. Add/strengthen C17_company_margin_bridge_required:
   - Commodity/refining/chemical spread vocabulary can open Stage2 only.
   - Stage2-Actionable requires evidence that spread improvement reaches company-level OPM, FCF, ASP, utilization, or earnings revision.
   - Do not treat generic commodity price sympathy as sufficient.

2. Add/strengthen C17_high_MAE_after_spread_blowoff_guard:
   - If C17 price MFE is strong but non-price bridge is thin, force local 4B watch after a blowoff move.
   - Do not promote to Stage3-Green unless margin durability and revision quality are confirmed.

3. Preserve existing global guardrails:
   - price_only_blowoff_blocks_positive_stage
   - full_4b_requires_non_price_evidence
   - high_MAE_guardrail
   - stage2_required_bridge

Expected safe effect:
- Preserve early S-Oil / SKC / 효성티앤씨 style MFE capture.
- Reduce LG화학-style overbroad chemical-label false positives.
- Reduce overstaying after C17 blowoffs with weak margin persistence.
```

---

## 10. Residual contribution summary

```text
new_independent_case_count: 4
reused_case_count: 0
same_archetype_new_symbol_count: 4
same_archetype_new_trigger_family_count: 4
calibration_usable_case_count: 4
calibration_usable_trigger_count: 4
positive_case_count: 1
mixed_positive_count: 2
counterexample_count: 1
local_4b_watch_count: 3
current_profile_error_count: 4
diversity_score_summary: Priority 0 C17 shortage fill; existing repeated 011780/011170/004000/006650/014680/014830 avoided; 010950/298020/051910/011790 added.
do_not_propose_new_weight_delta: false
auto_selected_coverage_gap: C17 rows 12 -> 16 if accepted; still Priority 0, need 14 to 30
sector_specific_rule_candidate: true
canonical_archetype_rule_candidate: true
loop_contribution_label: canonical_archetype_rule_candidate
new_axis_proposed: C17_company_margin_bridge_required | C17_high_MAE_after_spread_blowoff_guard
existing_axis_strengthened: stage2_required_bridge | price_only_blowoff_blocks_positive_stage | full_4b_requires_non_price_evidence | local_4b_watch_guard | high_MAE_guardrail
existing_axis_weakened: null
```

---

## 11. Next execution state

```yaml
completed_round: R4
completed_loop: 100
completed_large_sector_id: L4_MATERIALS_SPREAD_RESOURCE
completed_canonical_archetype_id: C17_CHEMICAL_COMMODITY_MARGIN_SPREAD
selection_basis: docs/core/V12_Research_No_Repeat_Index.md
selected_priority_bucket: Priority 0
round_schedule_status: coverage_index_selected
round_sector_consistency: pass
next_recommended_archetypes:
  - C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION
  - C05_EPC_MEGA_CONTRACT_MARGIN_GAP
  - C24_BIO_TRIAL_DATA_EVENT_RISK
  - C13_BATTERY_JV_UTILIZATION_AMPC_IRA
  - C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK
  - C28_SOFTWARE_SECURITY_CONTRACT_RETENTION
```
