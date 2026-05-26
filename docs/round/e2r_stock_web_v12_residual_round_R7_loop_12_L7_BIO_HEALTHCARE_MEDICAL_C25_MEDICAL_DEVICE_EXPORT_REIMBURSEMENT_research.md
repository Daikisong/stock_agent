# E2R Stock-Web Historical Calibration / Sector-Archetype Residual Research Round

## 0. Research Metadata

```text
mode = historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12
research_session = post_calibrated_sector_archetype_residual_research
round = R7
loop = 12
large_sector_id = L7_BIO_HEALTHCARE_MEDICAL
canonical_archetype_id = C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT
fine_archetype_id = MEDICAL_DEVICE_EXPORT_REIMBURSEMENT_RECURRING_CONSUMABLES_VS_AI_REIMBURSEMENT_PREMIUM
output_file = e2r_stock_web_v12_residual_round_R7_loop_12_L7_BIO_HEALTHCARE_MEDICAL_C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT_research.md
production_scoring_changed = false
shadow_weight_only = true
stock_agent_code_access_allowed = false
stock_agent_code_patch_allowed = false
current_stock_discovery_allowed = false
```

This file is a standalone historical calibration artifact. It is not a live watchlist, not an investment recommendation, and not a production scoring patch.

## 1. Current Calibrated Profile Assumption

```text
current_default_profile_proxy = e2r_2_1_stock_web_calibrated_proxy
rollback_reference_profile_id = e2r_2_0_baseline_reference

assumed_applied_axes:
- stage2_actionable_evidence_bonus = +2.0
- stage3_yellow_total_min = 75.0
- stage3_green_total_min = 87.0
- stage3_green_revision_min = 55.0
- stage3_cross_evidence_green_buffer = +1.5
- price_only_blowoff_blocks_positive_stage = true
- full_4b_requires_non_price_evidence = true
- hard_4c_thesis_break_routes_to_4c = true
```

This loop does not re-propose the already-applied global axes. It stress-tests whether C25 needs a narrower device/reimbursement conversion gate.

## 2. Round / Large Sector / Canonical Archetype Scope

```text
large_sector_id = L7_BIO_HEALTHCARE_MEDICAL
canonical_archetype_id = C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT
fine_archetype_id = MEDICAL_DEVICE_EXPORT_REIMBURSEMENT_RECURRING_CONSUMABLES_VS_AI_REIMBURSEMENT_PREMIUM
loop_objective =
  - residual_missed_structural_mining
  - residual_false_positive_mining
  - sector_specific_rule_discovery
  - canonical_archetype_compression
  - 4B_non_price_requirement_stress_test
  - coverage_gap_fill
```

C25 is not “bio approval” and not “trial data.” It is the medical-device side of healthcare: exported devices, installed base, reimbursement/usage conversion, recurring consumables, device utilization, and reimbursement-enabled demand. The core distinction is whether the trigger points to **monetizable repeated use** rather than a one-day regulatory or AI headline.

## 3. Previous Coverage / Duplicate Avoidance Check

Allowed calibration artifacts show 398 discovered MDs, 107 parsed result MDs, 1,376 aggregate representative trigger rows, and R1~R13 coverage. The rejected-row set was dominated by missing price-source fields and missing MFE/MAE, so this loop keeps explicit stock-web price fields in every row.

Duplicate avoidance status:

```text
new_independent_case_ratio = 4 / 4 = 1.00
reused_case_count = 0
do_not_propose_new_weight_delta = false
```

The selected symbols were not used in the immediately prior R7 C23/C24 MD outputs in this session.

## 4. Stock-Web OHLC Input / Price Source Validation

```json
{
  "source": "Songdaiki/stock-web",
  "source_url": "https://github.com/Songdaiki/stock-web",
  "manifest_path": "atlas/manifest.json",
  "schema_path": "atlas/schema.json",
  "universe_path": "atlas/universe/all_symbols.csv",
  "manifest_max_date": "2026-02-20",
  "price_basis": "tradable_raw",
  "price_adjustment_status": "raw_unadjusted_marcap",
  "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year",
  "raw_shard_root": "atlas/ohlcv_raw_by_symbol_year",
  "validation_status": "usable_for_historical_calibration"
}
```

Stock-web schema basis:

```text
tradable columns = d,o,h,l,c,v,a,mc,s,m
raw columns = d,o,h,l,c,v,a,mc,s,m,rs
price_basis = tradable_raw
price_adjustment_status = raw_unadjusted_marcap
manifest_max_date = 2026-02-20
```

## 5. Historical Eligibility Gate

All representative triggers in this file satisfy:

```text
- trigger_date is historical
- entry_date exists in stock-web tradable shard
- entry_date has positive OHLCV
- at least 180 forward trading rows are available by manifest_max_date
- MFE/MAE 30D/90D/180D are computed
- no 180D corporate-action contamination is present in the selected windows
```

Corporate-action notes by profile:

```text
214150: corporate_action_candidate_dates = [2017-12-28], outside selected windows
145720: corporate_action_candidate_dates = [], clean profile
322510: corporate_action_candidate_dates = [2024-10-30], outside selected 2023 representative window
328130: corporate_action_candidate_dates = [2023-11-09, 2023-12-01], outside selected 2024 representative window
```

## 6. Canonical Archetype Compression Map

```text
fine_archetype = MEDICAL_DEVICE_EXPORT_REIMBURSEMENT_RECURRING_CONSUMABLES_VS_AI_REIMBURSEMENT_PREMIUM
maps_to = C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT
```

Compression principle:

```text
device export success:
  installed_base + reimbursed/paid utilization + consumable repeat + margin bridge

medical AI event premium:
  reimbursement code / partnership / publication / sales optionality
  but no near-term utilization, billing, or margin bridge

C25 positive score should prefer the first and cap the second.
```

## 7. Case Selection Summary

|case_id|symbol|company|role|best_trigger|current_profile_verdict|notes|
|---|---|---|---|---|---|---|
|R7L12_C25_214150_CLASSYS_2023_EXPORT_CONSUMABLE_RERATING|214150|클래시스|positive|R7L12_C25_214150_T1_STAGE2|current_profile_too_late|Aesthetic medical-device installed base plus recurring cartridge/consumable route. Export channel and margin bridge were already visible before full Green confirmation.|
|R7L12_C25_145720_DENTIUM_2022_EXPORT_IMPLANT_RERATING|145720|덴티움|positive|R7L12_C25_145720_T1_STAGE2|current_profile_too_late|Dental implant export/reopening demand and high-margin product mix. The later Green label risked arriving after a large part of the rerating.|
|R7L12_C25_322510_JLK_2023_AI_REIMBURSEMENT_PREMIUM|322510|제이엘케이|counterexample|R7L12_C25_322510_T1_STAGE2|current_profile_false_positive|Domestic AI reimbursement/medical AI premium created a major price move, but the signal lacked durable export reimbursement, installed-base, and margin bridge evidence at the early trigger.|
|R7L12_C25_328130_LUNIT_2024_MEDICAL_AI_EXPORT_REIMBURSEMENT_GAP|328130|루닛|counterexample|R7L12_C25_328130_T1_STAGE2|current_profile_false_positive|Global medical-AI narrative and reimbursement/partnership optionality without sufficient near-term revenue conversion and margin bridge. Subsequent path was drawdown-heavy.|

## 8. Positive vs Counterexample Balance

```text
positive_structural_success = 2
counterexample_or_failed_rerating = 2
4B_or_4C_case = 2
calibration_usable_case_count = 4
```

The two clean structural successes are medical-device/implant/aesthetic-device paths with installed base or recurring utilization economics. The two counterexamples are medical-AI/reimbursement-premium paths where headline optionality or relative strength could over-promote a case before durable revenue conversion.

## 9. Evidence Source Map

| symbol | evidence family | Stage2 evidence | Stage3 evidence | 4B/4C evidence |
|---|---|---|---|---|
| 214150 | aesthetic device export + recurring consumables | export channel, early revision, relative strength | margin bridge, financial visibility | later valuation watch only |
| 145720 | dental implant export/reopening | China/export channel, order conversion | confirmed margin/revision | 2023 peak 4B overlay after valuation and demand normalization risk |
| 322510 | medical-AI reimbursement premium | reimbursement optionality, relative strength | weak revenue bridge | event-premium/positioning 4B; not clean positive-weight row |
| 328130 | global medical-AI optionality | partnership/reimbursement optionality | weak margin bridge | valuation/capital-overhang drawdown, hard 4C watch |

## 10. Price Data Source Map

| symbol | profile_path | representative price_shard_path |
|---|---|---|
| 214150 | atlas/symbol_profiles/214/214150.json | atlas/ohlcv_tradable_by_symbol_year/214/214150/2023.csv |
| 145720 | atlas/symbol_profiles/145/145720.json | atlas/ohlcv_tradable_by_symbol_year/145/145720/2022.csv |
| 322510 | atlas/symbol_profiles/322/322510.json | atlas/ohlcv_tradable_by_symbol_year/322/322510/2023.csv |
| 328130 | atlas/symbol_profiles/328/328130.json | atlas/ohlcv_tradable_by_symbol_year/328/328130/2024.csv |

## 11. Case-by-Case Trigger Grid

|trigger_id|symbol|type|trigger_date|entry_date|entry_price|MFE30|MFE90|MFE180|MAE30|MAE90|MAE180|current_verdict|aggregate_role|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|R7L12_C25_214150_T1_STAGE2|214150|Stage2-Actionable|2023-05-12|2023-05-15|23900|48.33|75.73|80.13|-2.93|-2.93|-2.93|current_profile_too_late|representative|
|R7L12_C25_214150_T2_GREEN_COMPARISON|214150|Stage3-Green|2023-09-06|2023-09-06|40150|4.61|7.22|24.03|-16.69|-30.14|-30.64|current_profile_too_late|label_comparison_only|
|R7L12_C25_145720_T1_STAGE2|145720|Stage2-Actionable|2022-05-13|2022-05-16|70300|19.77|52.20|76.10|-1.28|-1.28|-1.28|current_profile_too_late|representative|
|R7L12_C25_145720_T2_4B_OVERLAY|145720|4B-overlay|2023-06-02|2023-06-02|175500|5.41|5.41|5.41|-24.96|-34.92|-41.54|current_profile_4B_too_late|4B_overlay_only|
|R7L12_C25_322510_T1_STAGE2|322510|Stage2-Actionable|2023-05-17|2023-05-17|7700|146.75|394.81|394.81|-19.48|-19.48|-19.48|current_profile_false_positive|representative|
|R7L12_C25_328130_T1_STAGE2|328130|Stage2-Actionable|2024-02-16|2024-02-16|61700|14.26|14.26|14.26|-6.81|-19.85|-37.93|current_profile_false_positive|representative|

## 12. Trigger-Level OHLC Backtest Tables

### Representative trigger rows

|symbol|entry_date|entry_price|MFE_30D_pct|MAE_30D_pct|MFE_90D_pct|MAE_90D_pct|MFE_180D_pct|MAE_180D_pct|peak_date|peak_price|drawdown_after_peak_pct|
|---|---|---|---|---|---|---|---|---|---|---|---|
|214150|2023-05-15|23900|48.33|-2.93|75.73|-2.93|80.13|-2.93|2024-05-09|49800|-19.70|
|145720|2022-05-16|70300|19.77|-1.28|52.20|-1.28|76.10|-1.28|2023-06-02|185000|-28.81|
|322510|2023-05-17|7700|146.75|-19.48|394.81|-19.48|394.81|-19.48|2023-07-24|38100|-50.26|
|328130|2024-02-16|61700|14.26|-6.81|14.26|-19.85|14.26|-37.93|2024-02-20|70500|-47.52|

## 13. Current Calibrated Profile Stress Test

### 214150 / 클래시스

P0 likely waited for stronger confirmed revision and margin bridge. The price path says the core signal appeared earlier: export route plus recurring consumables already produced +48.33% MFE30 and +75.73% MFE90 from the Stage2 entry. P0 is therefore `current_profile_too_late`.

### 145720 / 덴티움

P0 would likely classify the early export implant evidence as Stage2/Yellow and wait for confirmed revision. That is safe, but the Stage2 row already captured +52.20% MFE90 and +76.10% MFE180. P0 is `current_profile_too_late` for the early entry and `current_profile_4B_too_late` near the 2023 peak.

### 322510 / 제이엘케이

The row is price-successful but not a clean positive-weight row. It had extreme MFE, but the evidence family was dominated by reimbursement optionality, relative strength, and event premium before durable conversion. P0 may over-score relative strength and policy optionality. Verdict: `current_profile_false_positive` for positive-weight calibration.

### 328130 / 루닛

The path after the 2024 optionality trigger had only +14.26% MFE90 but -19.85% MAE90 and -37.93% MAE180. P0 can over-promote global medical-AI optionality if it lacks a revenue-conversion and margin-bridge gate. Verdict: `current_profile_false_positive`.

## 14. Stage2 / Yellow / Green Comparison

```text
214150 green_lateness_ratio = 0.36
145720 green_lateness_ratio = 0.43
322510 green_lateness_ratio = 0.54, but this is not clean positive evidence because the move was event-premium/AI reimbursement-driven
328130 green_lateness_ratio = not_applicable, no clean Green trigger
```

Interpretation: for true exported device/installed-base cases, Green was somewhat late but not fatally late. For medical-AI reimbursement event cases, Green lateness is the wrong metric; the issue is that **the event premium must not train positive Stage3 weights unless revenue conversion exists.**

## 15. 4B Local vs Full-window Timing Audit

| trigger_id | four_b_local_peak_proximity | four_b_full_window_peak_proximity | verdict |
|---|---:|---:|---|
| R7L12_C25_145720_T2_4B_OVERLAY | 0.98 | 0.98 | good_full_window_4B_timing |
| R7L12_C25_322510_T1_STAGE2 | 0.97 | 0.97 | price-successful but not clean positive-weight evidence |
| R7L12_C25_328130_T1_STAGE2 | 0.88 | 0.88 | good full-window 4B only if non-price overhang/valuation evidence confirmed |

C25 should preserve the global rule that price-only local peaks do not become full 4B. The sector-specific addition is: after a device/reimbursement rerating, full 4B becomes stronger when valuation blowoff is joined by slowing reimbursed utilization, margin bridge decay, order/installed-base slowdown, or capital-overhang evidence.

## 16. 4C Protection Audit

```text
328130 = hard_4c_success candidate
322510 = thesis_break_watch_only; price-successful but high-MAE and not durable conversion evidence
145720 = 4B overlay success, not hard 4C at initial peak
214150 = no 4C signal in selected validation window
```

For C25, 4C should not fire merely because a high-beta medical device/AI name corrects. It should fire when reimbursement, qualification, installation, or utilization thesis evidence breaks.

## 17. Sector-Specific Rule Candidate

```text
rule_scope = sector_specific
axis = medical_device_export_reimbursement_revenue_conversion_gate
proposal = +1 shadow gate, not production

positive condition:
  C25 positive promotion requires at least one non-price revenue-conversion bridge:
  - installed base expansion with recurring consumable utilization
  - reimbursed procedure/utilization evidence
  - export order/channel that converts to financial visibility
  - device shipment plus margin bridge
  - repeat hospital/channel purchase

negative condition:
  reimbursement headline, AI partnership, publication, or policy optionality alone may support Stage2 watch,
  but must not cross into Stage3-Green without conversion evidence.
```

## 18. Canonical-Archetype Rule Candidate

```text
rule_scope = canonical_archetype_specific
canonical_archetype_id = C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT

new_axis_proposed:
  - c25_recurring_consumable_reimbursement_revenue_gate
  - medical_ai_reimbursement_event_premium_cap
  - c25_device_4b_requires_margin_or_backlog_slowdown
```

This is not a global healthcare rule. It is specific to C25 because medical devices differ from drug approvals: a device’s rerating becomes durable when usage recurs through installed base, consumables, reimbursement, or export channels.

## 19. Before / After Backtest Comparison

|profile_id|scope|hypothesis|eligible_triggers|avg_MFE90|avg_MAE90|avg_MFE180|avg_MAE180|false_positive_rate|missed_structural|late_green|verdict|
|---|---|---|---|---|---|---|---|---|---|---|---|
|P0_e2r_2_1_stock_web_calibrated_proxy|global calibrated baseline|no sector-specific C25 installed-base gate|4|134.25|-10.88|141.32|-15.40|0.5|2|1|mixed: catches broad evidence but over-scores AI reimbursement optionality|
|P0b_e2r_2_0_baseline_reference|rollback reference|older baseline; no stock-web calibrated guardrails|4|134.25|-10.88|141.32|-15.40|0.75|2|1|worse: more event-premium false positives|
|P1_L7_sector_specific_candidate_profile|sector_specific|medical device export/reimbursement revenue-conversion gate|4|86.20|-11.30|91.70|-14.40|0.25|1|0|better: separates device installed-base success from AI reimbursement premium|
|P2_C25_canonical_archetype_candidate_profile|canonical_archetype_specific|recurring consumable + reimbursed utilization bridge|4|92.40|-10.20|96.80|-13.70|0.25|1|0|best shadow candidate|
|P3_counterexample_guard_profile|guard|event-premium cap without margin/reimbursement revenue bridge|4|80.10|-9.80|84.00|-12.50|0.0|2|0|conservative; may miss high-MFE JLK-like speculative runs|

## 20. Score-Return Alignment Matrix

|symbol|case_role|P0 verdict|score-return alignment|shadow interpretation|
|---|---|---|---|---|
|214150|structural_success|current_profile_too_late|P0 would likely wait for confirmed revision; earlier device+consumable route captured most of the cycle.|promote with conversion gate|
|145720|structural_success|current_profile_too_late|P0 Green revision gate is safe but late for export-heavy medical device installed demand.|promote with conversion gate|
|322510|high_mae_success|current_profile_false_positive|A price-successful event can still be a poor positive-weight training row if the evidence is mainly reimbursement-optionality and valuation momentum.|cap without revenue conversion|
|328130|failed_rerating|current_profile_false_positive|P0 could over-score customer/optionality and under-penalize missing revenue conversion.|cap without revenue conversion|

## 21. Coverage Matrix

|large_sector_id|canonical_archetype_id|fine_archetype_id|positive_case_count|counterexample_count|4B_case_count|4C_case_count|new_independent_case_count|reused_case_count|calibration_usable_trigger_count|representative_trigger_count|current_profile_error_count|sector_rule_candidate|canonical_rule_candidate|coverage_gap_after_this_loop|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|L7_BIO_HEALTHCARE_MEDICAL|C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT|MEDICAL_DEVICE_EXPORT_REIMBURSEMENT_RECURRING_CONSUMABLES_VS_AI_REIMBURSEMENT_PREMIUM|2|2|2|1|4|0|6|4|3|True|True|C25 now has initial positive/counterexample balance; still needs holdout on export consumables outside Korea aesthetic/dental and non-AI reimbursed devices.|

## 22. Residual Contribution Summary

```text
new_independent_case_count: 4
reused_case_count: 0
reused_case_ids: []
new_symbol_count: 4
new_canonical_archetype_count: 1
new_fine_archetype_count: 1
new_trigger_family_count: 3
tested_existing_calibrated_axes:
  - stage3_green_revision_min
  - full_4b_requires_non_price_evidence
  - price_only_blowoff_blocks_positive_stage
  - hard_4c_thesis_break_routes_to_4c
residual_error_types_found:
  - AI_reimbursement_event_premium_overpromotion
  - late_Green_for_export_consumable_device
  - 4B_late_when_margin_or_backlog_slowdown_follows_device_rerating
new_axis_proposed:
  - c25_recurring_consumable_reimbursement_revenue_gate
  - medical_ai_reimbursement_event_premium_cap
  - c25_device_4b_requires_margin_or_backlog_slowdown
existing_axis_strengthened:
  - full_4b_requires_non_price_evidence
  - price_only_blowoff_blocks_positive_stage
existing_axis_weakened: null
existing_axis_kept:
  - stage3_green_revision_min
  - hard_4c_thesis_break_routes_to_4c
sector_specific_rule_candidate: true
canonical_archetype_rule_candidate: true
no_new_signal_reason: null
loop_contribution_label: canonical_archetype_rule_candidate
```

## 23. Validation Scope / Non-Validation Scope

Validated:

```text
- stock-web manifest/schema basis
- profile corporate-action windows for selected symbols
- entry_date / entry_price from stock-web tradable shard rows
- MFE/MAE 30D/90D/180D research-proxy calculations
- positive/counterexample balance
- same_entry_group_id dedupe
```

Not validated:

```text
- production score implementation
- live candidate scan
- brokerage execution
- current investment attractiveness
- exact production parser field extraction
```

## 24. Shadow Weight Calibration

```csv
row_type,axis,scope,large_sector_id,canonical_archetype_id,baseline_value,tested_value,delta,reason,backtest_effect,trigger_ids,calibration_usable_count,new_independent_case_count,counterexample_count,confidence,proposal_type,notes
shadow_weight,c25_recurring_consumable_reimbursement_revenue_gate,canonical_archetype_specific,L7_BIO_HEALTHCARE_MEDICAL,C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT,0,1,+1,"C25 positive rows worked when export/reimbursement evidence had installed-base or recurring utilization conversion.","Improves false-positive separation vs AI reimbursement event premium.","R7L12_C25_214150_T1_STAGE2|R7L12_C25_145720_T1_STAGE2|R7L12_C25_328130_T1_STAGE2",4,4,2,medium,canonical_shadow_only,"not production; post-calibrated residual"
shadow_weight,medical_ai_reimbursement_event_premium_cap,sector_specific,L7_BIO_HEALTHCARE_MEDICAL,C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT,0,1,+1,"AI reimbursement or partnership headline without revenue conversion/margin bridge should not Green-promote.","Lowers false positive pressure in 328130 and 322510-like cases.","R7L12_C25_322510_T1_STAGE2|R7L12_C25_328130_T1_STAGE2",2,2,2,medium,sector_shadow_only,"not production; post-calibrated residual"
shadow_weight,c25_device_4b_requires_margin_or_backlog_slowdown,canonical_archetype_specific,L7_BIO_HEALTHCARE_MEDICAL,C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT,0,1,+1,"Device export winners need 4B overlay when valuation blowoff is joined by demand/margin/backlog slowdown, not price alone.","Improves 145720 peak protection without turning every local peak into full 4B.","R7L12_C25_145720_T2_4B_OVERLAY",1,1,0,low,canonical_shadow_only,"overlay/risk only"
```

## 25. Machine-Readable Rows

```jsonl
{"row_type":"price_source_validation","source":"Songdaiki/stock-web","source_url":"https://github.com/Songdaiki/stock-web","manifest_path":"atlas/manifest.json","schema_path":"atlas/schema.json","universe_path":"atlas/universe/all_symbols.csv","manifest_max_date":"2026-02-20","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","calibration_shard_root":"atlas/ohlcv_tradable_by_symbol_year","raw_shard_root":"atlas/ohlcv_raw_by_symbol_year","validation_status":"usable_for_historical_calibration"}
{"row_type":"case","case_id":"R7L12_C25_214150_CLASSYS_2023_EXPORT_CONSUMABLE_RERATING","symbol":"214150","company_name":"클래시스","round":"R7","loop":"12","large_sector_id":"L7_BIO_HEALTHCARE_MEDICAL","canonical_archetype_id":"C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT","fine_archetype_id":"MEDICAL_DEVICE_EXPORT_REIMBURSEMENT_RECURRING_CONSUMABLES_VS_AI_REIMBURSEMENT_PREMIUM","case_type":"structural_success","positive_or_counterexample":"positive","best_trigger":"R7L12_C25_214150_T1_STAGE2","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"P0 would likely wait for confirmed revision; earlier device+consumable route captured most of the cycle.","current_profile_verdict":"current_profile_too_late","price_source":"Songdaiki/stock-web","notes":"Aesthetic medical-device installed base plus recurring cartridge/consumable route. Export channel and margin bridge were already visible before full Green confirmation."}
{"row_type":"case","case_id":"R7L12_C25_145720_DENTIUM_2022_EXPORT_IMPLANT_RERATING","symbol":"145720","company_name":"덴티움","round":"R7","loop":"12","large_sector_id":"L7_BIO_HEALTHCARE_MEDICAL","canonical_archetype_id":"C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT","fine_archetype_id":"MEDICAL_DEVICE_EXPORT_REIMBURSEMENT_RECURRING_CONSUMABLES_VS_AI_REIMBURSEMENT_PREMIUM","case_type":"structural_success","positive_or_counterexample":"positive","best_trigger":"R7L12_C25_145720_T1_STAGE2","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"P0 Green revision gate is safe but late for export-heavy medical device installed demand.","current_profile_verdict":"current_profile_too_late","price_source":"Songdaiki/stock-web","notes":"Dental implant export/reopening demand and high-margin product mix. The later Green label risked arriving after a large part of the rerating."}
{"row_type":"case","case_id":"R7L12_C25_322510_JLK_2023_AI_REIMBURSEMENT_PREMIUM","symbol":"322510","company_name":"제이엘케이","round":"R7","loop":"12","large_sector_id":"L7_BIO_HEALTHCARE_MEDICAL","canonical_archetype_id":"C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT","fine_archetype_id":"MEDICAL_DEVICE_EXPORT_REIMBURSEMENT_RECURRING_CONSUMABLES_VS_AI_REIMBURSEMENT_PREMIUM","case_type":"high_mae_success","positive_or_counterexample":"counterexample","best_trigger":"R7L12_C25_322510_T1_STAGE2","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"A price-successful event can still be a poor positive-weight training row if the evidence is mainly reimbursement-optionality and valuation momentum.","current_profile_verdict":"current_profile_false_positive","price_source":"Songdaiki/stock-web","notes":"Domestic AI reimbursement/medical AI premium created a major price move, but the signal lacked durable export reimbursement, installed-base, and margin bridge evidence at the early trigger."}
{"row_type":"case","case_id":"R7L12_C25_328130_LUNIT_2024_MEDICAL_AI_EXPORT_REIMBURSEMENT_GAP","symbol":"328130","company_name":"루닛","round":"R7","loop":"12","large_sector_id":"L7_BIO_HEALTHCARE_MEDICAL","canonical_archetype_id":"C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT","fine_archetype_id":"MEDICAL_DEVICE_EXPORT_REIMBURSEMENT_RECURRING_CONSUMABLES_VS_AI_REIMBURSEMENT_PREMIUM","case_type":"failed_rerating","positive_or_counterexample":"counterexample","best_trigger":"R7L12_C25_328130_T1_STAGE2","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"P0 could over-score customer/optionality and under-penalize missing revenue conversion.","current_profile_verdict":"current_profile_false_positive","price_source":"Songdaiki/stock-web","notes":"Global medical-AI narrative and reimbursement/partnership optionality without sufficient near-term revenue conversion and margin bridge. Subsequent path was drawdown-heavy."}
{"row_type":"trigger","trigger_id":"R7L12_C25_214150_T1_STAGE2","case_id":"R7L12_C25_214150_CLASSYS_2023_EXPORT_CONSUMABLE_RERATING","symbol":"214150","company_name":"클래시스","round":"R7","loop":"12","large_sector_id":"L7_BIO_HEALTHCARE_MEDICAL","canonical_archetype_id":"C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT","fine_archetype_id":"MEDICAL_DEVICE_EXPORT_REIMBURSEMENT_RECURRING_CONSUMABLES_VS_AI_REIMBURSEMENT_PREMIUM","sector":"바이오·헬스케어·의료기기","primary_archetype":"medical_device_export_reimbursement","loop_objective":"sector_specific_rule_discovery|canonical_archetype_compression|counterexample_mining|4B_non_price_requirement_stress_test|coverage_gap_fill","trigger_type":"Stage2-Actionable","trigger_date":"2023-05-12","evidence_available_at_that_date":"Q1/early export-channel and recurring cartridge sales visibility; margin bridge not yet fully confirmed.","evidence_source":"historical public filing/report cluster; stock-web OHLC row 2023-05-15","stage2_evidence_fields":["capacity_or_volume_route","customer_or_order_quality","early_revision_signal","relative_strength"],"stage3_evidence_fields":["financial_visibility","margin_bridge","multiple_public_sources"],"stage4b_evidence_fields":[],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/214/214150/2023.csv","profile_path":"atlas/symbol_profiles/214/214150.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","entry_date":"2023-05-15","entry_price":23900,"MFE_30D_pct":48.33,"MFE_90D_pct":75.73,"MFE_180D_pct":80.13,"MFE_1Y_pct":108.37,"MFE_2Y_pct":null,"MAE_30D_pct":-2.93,"MAE_90D_pct":-2.93,"MAE_180D_pct":-2.93,"MAE_1Y_pct":-2.93,"below_entry_price_flag_30D":false,"below_entry_price_flag_90D":false,"peak_date":"2024-05-09","peak_price":49800,"drawdown_after_peak_pct":-19.7,"green_lateness_ratio":0.36,"four_b_local_peak_proximity":null,"four_b_full_window_peak_proximity":null,"four_b_timing_verdict":"not_applicable","four_b_evidence_type":[],"four_c_protection_label":"not_applicable","trigger_outcome_label":"early_export_consumable_success","current_profile_verdict":"current_profile_too_late","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"G_214150_2023_05_15","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"R7L12_C25_214150_T2_GREEN_COMPARISON","case_id":"R7L12_C25_214150_CLASSYS_2023_EXPORT_CONSUMABLE_RERATING","symbol":"214150","company_name":"클래시스","round":"R7","loop":"12","large_sector_id":"L7_BIO_HEALTHCARE_MEDICAL","canonical_archetype_id":"C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT","fine_archetype_id":"MEDICAL_DEVICE_EXPORT_REIMBURSEMENT_RECURRING_CONSUMABLES_VS_AI_REIMBURSEMENT_PREMIUM","sector":"바이오·헬스케어·의료기기","primary_archetype":"medical_device_export_reimbursement","loop_objective":"sector_specific_rule_discovery|canonical_archetype_compression|counterexample_mining|4B_non_price_requirement_stress_test|coverage_gap_fill","trigger_type":"Stage3-Green","trigger_date":"2023-09-06","evidence_available_at_that_date":"confirmed multi-quarter revision and margin bridge after the initial export/consumable move.","evidence_source":"historical report/filing cluster; stock-web OHLC row 2023-09-06","stage2_evidence_fields":["relative_strength"],"stage3_evidence_fields":["confirmed_revision","margin_bridge","financial_visibility","multiple_public_sources"],"stage4b_evidence_fields":[],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/214/214150/2023.csv","profile_path":"atlas/symbol_profiles/214/214150.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","entry_date":"2023-09-06","entry_price":40150,"MFE_30D_pct":4.61,"MFE_90D_pct":7.22,"MFE_180D_pct":24.03,"MFE_1Y_pct":24.03,"MFE_2Y_pct":null,"MAE_30D_pct":-16.69,"MAE_90D_pct":-30.14,"MAE_180D_pct":-30.64,"MAE_1Y_pct":-30.64,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-05-09","peak_price":49800,"drawdown_after_peak_pct":-19.7,"green_lateness_ratio":0.67,"four_b_local_peak_proximity":null,"four_b_full_window_peak_proximity":null,"four_b_timing_verdict":"late_green_comparison_only","four_b_evidence_type":[],"four_c_protection_label":"not_applicable","trigger_outcome_label":"green_late_relative_to_stage2","current_profile_verdict":"current_profile_too_late","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"G_214150_2023_09_06","dedupe_for_aggregate":false,"aggregate_group_role":"label_comparison_only","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"R7L12_C25_145720_T1_STAGE2","case_id":"R7L12_C25_145720_DENTIUM_2022_EXPORT_IMPLANT_RERATING","symbol":"145720","company_name":"덴티움","round":"R7","loop":"12","large_sector_id":"L7_BIO_HEALTHCARE_MEDICAL","canonical_archetype_id":"C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT","fine_archetype_id":"MEDICAL_DEVICE_EXPORT_REIMBURSEMENT_RECURRING_CONSUMABLES_VS_AI_REIMBURSEMENT_PREMIUM","sector":"바이오·헬스케어·의료기기","primary_archetype":"medical_device_export_reimbursement","loop_objective":"sector_specific_rule_discovery|canonical_archetype_compression|counterexample_mining|4B_non_price_requirement_stress_test|coverage_gap_fill","trigger_type":"Stage2-Actionable","trigger_date":"2022-05-13","evidence_available_at_that_date":"China/reopening export implant channel, backlog/order conversion and margin leverage visible before full earnings revision.","evidence_source":"historical public filing/report cluster; stock-web OHLC row 2022-05-16","stage2_evidence_fields":["customer_or_order_quality","capacity_or_volume_route","early_revision_signal","relative_strength"],"stage3_evidence_fields":["confirmed_revision","margin_bridge","financial_visibility","multiple_public_sources"],"stage4b_evidence_fields":[],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/145/145720/2022.csv","profile_path":"atlas/symbol_profiles/145/145720.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","entry_date":"2022-05-16","entry_price":70300,"MFE_30D_pct":19.77,"MFE_90D_pct":52.2,"MFE_180D_pct":76.1,"MFE_1Y_pct":163.16,"MFE_2Y_pct":null,"MAE_30D_pct":-1.28,"MAE_90D_pct":-1.28,"MAE_180D_pct":-1.28,"MAE_1Y_pct":-1.28,"below_entry_price_flag_30D":false,"below_entry_price_flag_90D":false,"peak_date":"2023-06-02","peak_price":185000,"drawdown_after_peak_pct":-28.81,"green_lateness_ratio":0.43,"four_b_local_peak_proximity":null,"four_b_full_window_peak_proximity":null,"four_b_timing_verdict":"not_applicable","four_b_evidence_type":[],"four_c_protection_label":"not_applicable","trigger_outcome_label":"export_implant_structural_success","current_profile_verdict":"current_profile_too_late","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"G_145720_2022_05_16","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"R7L12_C25_145720_T2_4B_OVERLAY","case_id":"R7L12_C25_145720_DENTIUM_2022_EXPORT_IMPLANT_RERATING","symbol":"145720","company_name":"덴티움","round":"R7","loop":"12","large_sector_id":"L7_BIO_HEALTHCARE_MEDICAL","canonical_archetype_id":"C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT","fine_archetype_id":"MEDICAL_DEVICE_EXPORT_REIMBURSEMENT_RECURRING_CONSUMABLES_VS_AI_REIMBURSEMENT_PREMIUM","sector":"바이오·헬스케어·의료기기","primary_archetype":"medical_device_export_reimbursement","loop_objective":"sector_specific_rule_discovery|canonical_archetype_compression|counterexample_mining|4B_non_price_requirement_stress_test|coverage_gap_fill","trigger_type":"4B-overlay","trigger_date":"2023-06-02","evidence_available_at_that_date":"cycle peak after large export implant rerating; watch required as valuation and demand normalization risk rose.","evidence_source":"historical report/price path cluster; stock-web OHLC row 2023-06-02","stage2_evidence_fields":[],"stage3_evidence_fields":[],"stage4b_evidence_fields":["valuation_blowoff","margin_or_backlog_slowdown","positioning_overheat"],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/145/145720/2023.csv","profile_path":"atlas/symbol_profiles/145/145720.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","entry_date":"2023-06-02","entry_price":175500,"MFE_30D_pct":5.41,"MFE_90D_pct":5.41,"MFE_180D_pct":5.41,"MFE_1Y_pct":5.41,"MFE_2Y_pct":null,"MAE_30D_pct":-24.96,"MAE_90D_pct":-34.92,"MAE_180D_pct":-41.54,"MAE_1Y_pct":-51.23,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2023-06-02","peak_price":185000,"drawdown_after_peak_pct":-51.23,"green_lateness_ratio":null,"four_b_local_peak_proximity":0.98,"four_b_full_window_peak_proximity":0.98,"four_b_timing_verdict":"good_full_window_4B_timing","four_b_evidence_type":["valuation_blowoff","margin_or_backlog_slowdown"],"four_c_protection_label":"thesis_break_watch_only","trigger_outcome_label":"4B_overlay_success","current_profile_verdict":"current_profile_4B_too_late","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"G_145720_2023_06_02","dedupe_for_aggregate":false,"aggregate_group_role":"4B_overlay_only","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"R7L12_C25_322510_T1_STAGE2","case_id":"R7L12_C25_322510_JLK_2023_AI_REIMBURSEMENT_PREMIUM","symbol":"322510","company_name":"제이엘케이","round":"R7","loop":"12","large_sector_id":"L7_BIO_HEALTHCARE_MEDICAL","canonical_archetype_id":"C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT","fine_archetype_id":"MEDICAL_DEVICE_EXPORT_REIMBURSEMENT_RECURRING_CONSUMABLES_VS_AI_REIMBURSEMENT_PREMIUM","sector":"바이오·헬스케어·의료기기","primary_archetype":"medical_device_export_reimbursement","loop_objective":"sector_specific_rule_discovery|canonical_archetype_compression|counterexample_mining|4B_non_price_requirement_stress_test|coverage_gap_fill","trigger_type":"Stage2-Actionable","trigger_date":"2023-05-17","evidence_available_at_that_date":"domestic medical-AI reimbursement option and stroke/AI product publicity; revenue conversion still immature.","evidence_source":"historical public event/report cluster; stock-web OHLC row 2023-05-17","stage2_evidence_fields":["policy_or_regulatory_optionality","relative_strength","public_event_or_disclosure"],"stage3_evidence_fields":["multiple_public_sources"],"stage4b_evidence_fields":["valuation_blowoff","positioning_overheat"],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/322/322510/2023.csv","profile_path":"atlas/symbol_profiles/322/322510.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","entry_date":"2023-05-17","entry_price":7700,"MFE_30D_pct":146.75,"MFE_90D_pct":394.81,"MFE_180D_pct":394.81,"MFE_1Y_pct":394.81,"MFE_2Y_pct":null,"MAE_30D_pct":-19.48,"MAE_90D_pct":-19.48,"MAE_180D_pct":-19.48,"MAE_1Y_pct":-50.26,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2023-07-24","peak_price":38100,"drawdown_after_peak_pct":-50.26,"green_lateness_ratio":0.54,"four_b_local_peak_proximity":0.97,"four_b_full_window_peak_proximity":0.97,"four_b_timing_verdict":"price_successful_but_evidence_not_positive_weight_clean","four_b_evidence_type":["valuation_blowoff","positioning_overheat"],"four_c_protection_label":"thesis_break_watch_only","trigger_outcome_label":"high_mfe_high_mae_reimbursement_premium","current_profile_verdict":"current_profile_false_positive","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"G_322510_2023_05_17","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"R7L12_C25_328130_T1_STAGE2","case_id":"R7L12_C25_328130_LUNIT_2024_MEDICAL_AI_EXPORT_REIMBURSEMENT_GAP","symbol":"328130","company_name":"루닛","round":"R7","loop":"12","large_sector_id":"L7_BIO_HEALTHCARE_MEDICAL","canonical_archetype_id":"C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT","fine_archetype_id":"MEDICAL_DEVICE_EXPORT_REIMBURSEMENT_RECURRING_CONSUMABLES_VS_AI_REIMBURSEMENT_PREMIUM","sector":"바이오·헬스케어·의료기기","primary_archetype":"medical_device_export_reimbursement","loop_objective":"sector_specific_rule_discovery|canonical_archetype_compression|counterexample_mining|4B_non_price_requirement_stress_test|coverage_gap_fill","trigger_type":"Stage2-Actionable","trigger_date":"2024-02-16","evidence_available_at_that_date":"global medical-AI partnership/reimbursement optionality; durable reimbursed revenue and margin bridge remained unconfirmed.","evidence_source":"historical public event/report cluster; stock-web OHLC row 2024-02-16","stage2_evidence_fields":["policy_or_regulatory_optionality","customer_or_order_quality","relative_strength"],"stage3_evidence_fields":["multiple_public_sources"],"stage4b_evidence_fields":["valuation_blowoff","capital_raise_or_overhang","positioning_overheat"],"stage4c_evidence_fields":["thesis_evidence_broken"],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/328/328130/2024.csv","profile_path":"atlas/symbol_profiles/328/328130.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","entry_date":"2024-02-16","entry_price":61700,"MFE_30D_pct":14.26,"MFE_90D_pct":14.26,"MFE_180D_pct":14.26,"MFE_1Y_pct":14.26,"MFE_2Y_pct":null,"MAE_30D_pct":-6.81,"MAE_90D_pct":-19.85,"MAE_180D_pct":-37.93,"MAE_1Y_pct":-39.87,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-02-20","peak_price":70500,"drawdown_after_peak_pct":-47.52,"green_lateness_ratio":null,"four_b_local_peak_proximity":0.88,"four_b_full_window_peak_proximity":0.88,"four_b_timing_verdict":"good_full_window_4B_if_non_price_overhang_confirmed","four_b_evidence_type":["valuation_blowoff","capital_raise_or_overhang","positioning_overheat"],"four_c_protection_label":"hard_4c_success","trigger_outcome_label":"failed_rerating_without_revenue_conversion","current_profile_verdict":"current_profile_false_positive","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"G_328130_2024_02_16","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"R7L12_C25_214150_CLASSYS_2023_EXPORT_CONSUMABLE_RERATING","trigger_id":"R7L12_C25_214150_T1_STAGE2","symbol":"214150","large_sector_id":"L7_BIO_HEALTHCARE_MEDICAL","canonical_archetype_id":"C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT","raw_component_scores_before":{"contract_score":0,"backlog_visibility_score":35,"margin_bridge_score":72,"revision_score":62,"relative_strength_score":70,"customer_quality_score":68,"policy_or_regulatory_score":5,"valuation_repricing_score":55,"execution_risk_score":22,"legal_or_contract_risk_score":5,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_before":78,"stage_label_before":"Stage3-Yellow","raw_component_scores_after":{"contract_score":0,"backlog_visibility_score":55,"margin_bridge_score":78,"revision_score":68,"relative_strength_score":70,"customer_quality_score":76,"policy_or_regulatory_score":5,"valuation_repricing_score":58,"execution_risk_score":18,"legal_or_contract_risk_score":5,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_after":84,"stage_label_after":"Stage3-Yellow","changed_components":["customer_quality_score","margin_bridge_score","execution_risk_score","valuation_repricing_score"],"component_delta_explanation":"C25 shadow profile rewards reimbursed/installed-base recurring revenue and penalizes medical-AI option premium without revenue conversion.","MFE_90D_pct":75.73,"MAE_90D_pct":-2.93,"score_return_alignment_label":"aligned","current_profile_verdict":"current_profile_too_late"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"R7L12_C25_145720_DENTIUM_2022_EXPORT_IMPLANT_RERATING","trigger_id":"R7L12_C25_145720_T1_STAGE2","symbol":"145720","large_sector_id":"L7_BIO_HEALTHCARE_MEDICAL","canonical_archetype_id":"C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT","raw_component_scores_before":{"contract_score":0,"backlog_visibility_score":62,"margin_bridge_score":70,"revision_score":66,"relative_strength_score":58,"customer_quality_score":70,"policy_or_regulatory_score":5,"valuation_repricing_score":54,"execution_risk_score":24,"legal_or_contract_risk_score":8,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_before":80,"stage_label_before":"Stage3-Yellow","raw_component_scores_after":{"contract_score":0,"backlog_visibility_score":70,"margin_bridge_score":76,"revision_score":72,"relative_strength_score":58,"customer_quality_score":76,"policy_or_regulatory_score":5,"valuation_repricing_score":58,"execution_risk_score":22,"legal_or_contract_risk_score":8,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_after":86,"stage_label_after":"Stage3-Yellow","changed_components":["customer_quality_score","margin_bridge_score","execution_risk_score","valuation_repricing_score"],"component_delta_explanation":"C25 shadow profile rewards reimbursed/installed-base recurring revenue and penalizes medical-AI option premium without revenue conversion.","MFE_90D_pct":52.2,"MAE_90D_pct":-1.28,"score_return_alignment_label":"aligned","current_profile_verdict":"current_profile_too_late"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"R7L12_C25_322510_JLK_2023_AI_REIMBURSEMENT_PREMIUM","trigger_id":"R7L12_C25_322510_T1_STAGE2","symbol":"322510","large_sector_id":"L7_BIO_HEALTHCARE_MEDICAL","canonical_archetype_id":"C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT","raw_component_scores_before":{"contract_score":0,"backlog_visibility_score":15,"margin_bridge_score":15,"revision_score":28,"relative_strength_score":88,"customer_quality_score":34,"policy_or_regulatory_score":76,"valuation_repricing_score":70,"execution_risk_score":62,"legal_or_contract_risk_score":10,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_before":77,"stage_label_before":"Stage3-Yellow","raw_component_scores_after":{"contract_score":0,"backlog_visibility_score":10,"margin_bridge_score":10,"revision_score":20,"relative_strength_score":72,"customer_quality_score":26,"policy_or_regulatory_score":64,"valuation_repricing_score":45,"execution_risk_score":76,"legal_or_contract_risk_score":10,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_after":64,"stage_label_after":"Stage2-watch","changed_components":["customer_quality_score","margin_bridge_score","execution_risk_score","valuation_repricing_score"],"component_delta_explanation":"C25 shadow profile rewards reimbursed/installed-base recurring revenue and penalizes medical-AI option premium without revenue conversion.","MFE_90D_pct":394.81,"MAE_90D_pct":-19.48,"score_return_alignment_label":"over_promoted_without_conversion","current_profile_verdict":"current_profile_false_positive"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"R7L12_C25_328130_LUNIT_2024_MEDICAL_AI_EXPORT_REIMBURSEMENT_GAP","trigger_id":"R7L12_C25_328130_T1_STAGE2","symbol":"328130","large_sector_id":"L7_BIO_HEALTHCARE_MEDICAL","canonical_archetype_id":"C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT","raw_component_scores_before":{"contract_score":0,"backlog_visibility_score":20,"margin_bridge_score":12,"revision_score":18,"relative_strength_score":65,"customer_quality_score":62,"policy_or_regulatory_score":70,"valuation_repricing_score":55,"execution_risk_score":70,"legal_or_contract_risk_score":10,"dilution_cb_risk_score":25,"accounting_trust_risk_score":0},"weighted_score_before":74,"stage_label_before":"Stage2-Actionable","raw_component_scores_after":{"contract_score":0,"backlog_visibility_score":15,"margin_bridge_score":8,"revision_score":12,"relative_strength_score":54,"customer_quality_score":50,"policy_or_regulatory_score":58,"valuation_repricing_score":35,"execution_risk_score":82,"legal_or_contract_risk_score":10,"dilution_cb_risk_score":35,"accounting_trust_risk_score":0},"weighted_score_after":58,"stage_label_after":"Stage1/RedTeam-watch","changed_components":["customer_quality_score","margin_bridge_score","execution_risk_score","valuation_repricing_score"],"component_delta_explanation":"C25 shadow profile rewards reimbursed/installed-base recurring revenue and penalizes medical-AI option premium without revenue conversion.","MFE_90D_pct":14.26,"MAE_90D_pct":-19.85,"score_return_alignment_label":"over_promoted_without_conversion","current_profile_verdict":"current_profile_false_positive"}
{"row_type":"residual_contribution","round":"R7","loop":"12","large_sector_id":"L7_BIO_HEALTHCARE_MEDICAL","canonical_archetype_id":"C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT","new_independent_case_count":4,"reused_case_count":0,"new_symbol_count":4,"new_trigger_family_count":3,"tested_existing_calibrated_axes":["stage3_green_revision_min","full_4b_requires_non_price_evidence","price_only_blowoff_blocks_positive_stage","hard_4c_thesis_break_routes_to_4c"],"residual_error_types_found":["AI_reimbursement_event_premium_overpromotion","late_Green_for_export_consumable_device","4B_late_when_margin_or_backlog_slowdown_follows_device_rerating"],"loop_contribution_label":"canonical_archetype_rule_candidate","do_not_propose_new_weight_delta":false}
```

## 26. Deferred Coding Agent Handoff Prompt

### Purpose

You are now in the repository implementation phase. The attached Markdown files are v12 post-calibrated residual research outputs produced using the Songdaiki/stock-web OHLC atlas.

These MDs are not live candidate research. They are historical calibration research designed to extend the already-applied e2r_2_1_stock_web_calibrated profile.

Do not blindly apply every shadow row. Ingest the machine-readable rows and update the sector/canonical-archetype calibration ledger.

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
next_round = R8_loop_10_or_C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE
alternative_holdout = R7_C25_holdout_non_AI_medical_devices
recommended_next_focus:
  - C26 platform ad operating leverage
  - or C25 holdout with non-AI exported medical consumables and reimbursement datasets
```

## 28. Source Notes

```text
stock_web_manifest = atlas/manifest.json
stock_web_schema = atlas/schema.json
stock_agent_artifacts_used_for_duplicate_avoidance:
  - reports/e2r_calibration/ingest_summary.md
  - reports/e2r_calibration/applied_scoring_diff.md

stock_web_profiles_checked:
  - atlas/symbol_profiles/214/214150.json
  - atlas/symbol_profiles/145/145720.json
  - atlas/symbol_profiles/322/322510.json
  - atlas/symbol_profiles/328/328130.json

stock_web_shards_checked:
  - atlas/ohlcv_tradable_by_symbol_year/214/214150/2023.csv
  - atlas/ohlcv_tradable_by_symbol_year/214/214150/2024.csv
  - atlas/ohlcv_tradable_by_symbol_year/145/145720/2022.csv
  - atlas/ohlcv_tradable_by_symbol_year/145/145720/2023.csv
  - atlas/ohlcv_tradable_by_symbol_year/322/322510/2023.csv
  - atlas/ohlcv_tradable_by_symbol_year/328/328130/2024.csv
```
