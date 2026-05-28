# E2R Stock-Web Historical Calibration / Sector-Archetype Residual Research Round

## 0. Research Metadata

- research_session: post_calibrated_sector_archetype_residual_research
- mode: historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12
- round: R7
- loop: 28
- large_sector_id: L7_BIO_HEALTHCARE_MEDICAL
- canonical_archetype_id: C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT
- fine_archetype_id: EXPORT_REIMBURSEMENT_IMPLEMENTATION_QUALITY_GATE
- output_format: one_standalone_markdown_file
- production_scoring_changed: false
- shadow_weight_only: true
- current_stock_discovery_allowed: false
- stock_agent_code_access_allowed: false
- handoff_prompt_embedded: true
- handoff_prompt_executed_now: false

## 1. Current Calibrated Profile Assumption

Current proxy profile is `e2r_2_1_stock_web_calibrated_proxy`; rollback reference is `e2r_2_0_baseline_reference`. Existing global axes are treated as already applied: Stage2-actionable evidence bonus, Yellow 75, Green 87/revision 55, cross-evidence buffer, price-only blowoff guard, full-4B non-price requirement, and hard-4C thesis-break routing.

This loop does **not** propose a global rule. It tests whether C25 needs a narrower archetype rule: medical-device export/reimbursement narratives should be promoted only when export implementation, reimbursement utilization, installed-base pull-through, or repeat-order evidence exists.

## 2. Round / Large Sector / Canonical Archetype Scope

- round: R7
- loop: 28
- large_sector_id: L7_BIO_HEALTHCARE_MEDICAL
- canonical_archetype_id: C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT
- loop_objective: `coverage_gap_fill`, `counterexample_mining`, `canonical_archetype_compression`, `green_strictness_stress_test`, `4C_thesis_break_timing_test`
- selected coverage gap: R7/C25 after R7/C24 trial-data work lacked balanced medical-device export/reimbursement positives and counterexamples.

## 3. Previous Coverage / Duplicate Avoidance Check

`stock_agent` code was not opened. Repository search over allowed research/artifact scope did not surface an existing C25 row set for the selected symbols. The loop uses five new symbols inside the same canonical archetype: 클래시스, 덴티움, 뷰노, 레이, 인바디.

Novelty counters:

```text
new_independent_case_count = 5
reused_case_count = 0
new_symbol_count = 5
same_archetype_new_symbol_count = 5
same_archetype_new_trigger_family_count = 4
new_canonical_archetype_count = 0
new_trigger_family_count = 4
positive_case_count = 3
counterexample_count = 2
current_profile_error_count = 3
```

## 4. Stock-Web OHLC Input / Price Source Validation

Stock-Web manifest fields used:

```json
{
  "row_type": "price_source_validation",
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

Manifest confirms raw/unadjusted marcap basis, max_date `2026-02-20`, tradable row count 14,354,401, raw row count 15,214,118, and calibration shard root `atlas/ohlcv_tradable_by_symbol_year`. It also states zero-volume and zero-OHLC rows are excluded from calibration shards and corporate-action-contaminated windows are blocked by default.

## 5. Historical Eligibility Gate

All representative triggers below are historical, have stock-web tradable entry rows, and have at least 180 trading days available before the manifest max date. The five representative triggers are clean for 180D calibration under profile corporate-action dates:

| symbol | profile_path | corporate_action_candidate_dates | 180D status |
|---:|---|---|---|
| 214150 | atlas/symbol_profiles/214/214150.json | 2017-12-28 | clean_180D_window |
| 145720 | atlas/symbol_profiles/145/145720.json | [] | clean_180D_window |
| 338220 | atlas/symbol_profiles/338/338220.json | [] | clean_180D_window |
| 228670 | atlas/symbol_profiles/228/228670.json | 2021-06-03, 2021-06-23 | clean_180D_window |
| 041830 | atlas/symbol_profiles/041/041830.json | 2010-04-23, 2010-05-18 | clean_180D_window |

## 6. Canonical Archetype Compression Map

C25 is compressed into three fine-archetype families for this loop:

| fine_archetype_id | canonical mapping | interpretation |
|---|---|---|
| AESTHETIC_DEVICE_EXPORT_CONSUMABLE_MARGIN | C25 | device install-base and consumable pull-through create margin bridge |
| DENTAL_IMPLANT_EXPORT_REORDER_MARGIN | C25 | export/reorder visibility and margin bridge create EPS rerating |
| MEDICAL_AI_REIMBURSEMENT_IMPLEMENTATION | C25 | reimbursement/adoption route can rerate before conventional revisions |
| DENTAL_DIGITAL_EXPORT_EXECUTION_RISK | C25 | export narrative without order quality can fail |
| BODY_COMPOSITION_DEVICE_SINGLE_SPIKE_GUARD | C25 | single-day device/earnings enthusiasm is not a durable C25 rerating |

## 7. Case Selection Summary

| case_id | symbol | company | role | case_type | best_trigger | current_profile_verdict | score_price_alignment |
|---|---:|---|---|---|---|---|---|
| C25-R7L28-214150-CLASSYS-EXPORT-MARGIN | 214150 | 클래시스 | positive | structural_success | T-214150-2023-05-02-S2A | current_profile_correct | strong_positive_alignment |
| C25-R7L28-145720-DENTIUM-CHINA-IMPLANT | 145720 | 덴티움 | positive | structural_success | T-145720-2022-11-09-S2A | current_profile_correct | strong_positive_alignment |
| C25-R7L28-338220-VUNO-AI-REIMBURSEMENT | 338220 | 뷰노 | positive | missed_structural | T-338220-2023-02-24-S2A | current_profile_too_late | missed_structural_if_revision_gate_too_strict |
| C25-R7L28-228670-RAY-CHINA-DENTAL-CALL-OFF | 228670 | 레이 | counterexample | failed_rerating | T-228670-2023-05-15-S2A | current_profile_false_positive | weak_score_return_alignment |
| C25-R7L28-041830-INBODY-EXPORT-SPIKE | 041830 | 인바디 | counterexample | price_moved_without_evidence | T-041830-2023-02-28-S2A | current_profile_false_positive | single_spike_no_sustained_rerating |

## 8. Positive vs Counterexample Balance

Positive cases: 3. Counterexamples: 2. Calibration-usable representative cases: 5. The balance is adequate for canonical-archetype shadow proposal, but not for a global profile change.

The common separation is simple: when C25 evidence is an implemented route—exports feeding installed base, repeat orders, reimbursement utilization, or visible margin bridge—the price path had strong MFE and tolerable early MAE. When evidence was mostly a one-day device narrative or unclosed channel thesis, MFE was capped and drawdown became thesis-breaking.

## 9. Evidence Source Map

| symbol | evidence family | trigger family | evidence treatment |
|---:|---|---|---|
| 214150 | aesthetic device exports + consumable margin | export implementation | supports Stage2/Green |
| 145720 | dental implant export/reorder + margin | export/reorder implementation | supports Stage2/Green |
| 338220 | medical-AI reimbursement/adoption route | reimbursement implementation | supports Stage2 before EPS revision closes |
| 228670 | dental digital export/channel narrative | execution-risk counterexample | blocks Green without order-quality proof |
| 041830 | body-composition device export/earnings spike | single-day spike guard | blocks Green without repeat implementation evidence |

External article/disclosure retrieval was not used for weight calibration. Quantitative calibration depends only on stock-web OHLC rows. Implementation agent should verify public event sources before promoting any shadow axis.

## 10. Price Data Source Map

| symbol | representative shard | profile |
|---:|---|---|
| 214150 | atlas/ohlcv_tradable_by_symbol_year/214/214150/2023.csv | atlas/symbol_profiles/214/214150.json |
| 145720 | atlas/ohlcv_tradable_by_symbol_year/145/145720/2022.csv; 2023.csv | atlas/symbol_profiles/145/145720.json |
| 338220 | atlas/ohlcv_tradable_by_symbol_year/338/338220/2023.csv | atlas/symbol_profiles/338/338220.json |
| 228670 | atlas/ohlcv_tradable_by_symbol_year/228/228670/2023.csv | atlas/symbol_profiles/228/228670.json |
| 041830 | atlas/ohlcv_tradable_by_symbol_year/041/041830/2023.csv | atlas/symbol_profiles/041/041830.json |

## 11. Case-by-Case Trigger Grid

| trigger_id | symbol | trigger_type | trigger_date | entry_date | entry_price | MFE_30D | MFE_90D | MFE_180D | MAE_30D | MAE_90D | MAE_180D | peak_date | peak_price | current_profile_verdict |
|---|---:|---|---|---|---:|---:|---:|---:|---:|---:|---:|---|---:|---|
| T-214150-2023-05-02-S2A | 214150 | Stage2-Actionable | 2023-05-02 | 2023-05-02 | 25,150 | 40.95 | 67.00 | 71.17 | -7.75 | -7.75 | -7.75 | 2023-11-30 | 43,050 | current_profile_correct |
| T-214150-2023-06-14-GREEN | 214150 | Stage3-Green | 2023-06-14 | 2023-06-14 | 32,900 | 16.26 | 30.85 | 30.85 | -11.25 | -11.25 | -11.25 | 2023-11-30 | 43,050 | current_profile_correct |
| T-145720-2022-11-09-S2A | 145720 | Stage2-Actionable | 2022-11-09 | 2022-11-09 | 77,000 | 20.52 | 75.32 | 140.26 | -2.60 | -2.60 | -2.60 | 2023-06-02 | 185,000 | current_profile_correct |
| T-145720-2023-03-31-GREEN | 145720 | Stage3-Green | 2023-03-31 | 2023-03-31 | 139,700 | 32.43 | 32.43 | 32.43 | -3.36 | -18.68 | -34.00 | 2023-06-02 | 185,000 | current_profile_correct |
| T-338220-2023-02-24-S2A | 338220 | Stage2-Actionable | 2023-02-24 | 2023-02-24 | 14,770 | 35.75 | 171.50 | 370.55 | -15.17 | -15.17 | -15.17 | 2023-09-07 | 69,500 | current_profile_too_late |
| T-338220-2023-09-07-4B | 338220 | Stage4B | 2023-09-07 | 2023-09-07 | 63,600 | 9.28 | 9.28 | 9.28 | -46.70 | -61.71 | -61.71 | 2023-09-07 | 69,500 | current_profile_correct |
| T-228670-2023-05-15-S2A | 228670 | Stage2-Actionable | 2023-05-15 | 2023-05-15 | 35,550 | 18.57 | 18.57 | 18.57 | -7.45 | -44.44 | -45.43 | 2023-06-15 | 42,150 | current_profile_false_positive |
| T-228670-2023-08-14-4C | 228670 | Stage4C | 2023-08-14 | 2023-08-14 | 28,250 | 4.07 | 11.50 | 11.50 | -25.66 | -31.33 | -31.33 | 2023-08-24 | 29,400 | current_profile_4C_too_late |
| T-041830-2023-02-28-S2A | 041830 | Stage2-Actionable | 2023-02-28 | 2023-02-28 | 29,000 | 5.00 | 12.24 | 12.24 | -7.07 | -10.52 | -18.97 | 2023-04-11 | 32,550 | current_profile_false_positive |

## 12. Trigger-Level OHLC Backtest Tables

Representative trigger aggregate only includes rows with `dedupe_for_aggregate=true` and `aggregate_group_role=representative`.

| aggregate subset | count | avg_MFE_90D_pct | avg_MAE_90D_pct | avg_MFE_180D_pct | avg_MAE_180D_pct |
|---|---:|---:|---:|---:|---:|
| positives only | 3 | 104.61 | -8.51 | 193.99 | -8.51 |
| counterexamples only | 2 | 15.41 | -27.48 | 15.41 | -32.20 |
| all representative | 5 | 68.93 | -16.10 | 122.56 | -17.99 |

## 13. Current Calibrated Profile Stress Test

- The calibrated profile handled 클래시스 and 덴티움 correctly because non-price evidence plausibly connected export demand to margin/revision and customer quality.
- It would likely be too late on 뷰노 if it insists on a conventional revision gate before recognizing reimbursement implementation as Stage2-actionable.
- It can be too generous on 레이 and 인바디 if it treats single-day export/device enthusiasm as Stage3-quality evidence.
- Existing 4B/4C guards were strengthened: 뷰노 needed 4B as an overlay near a valuation/positioning blowoff, while 레이 needed a hard 4C route after the earlier channel thesis broke.

## 14. Stage2 / Yellow / Green Comparison

| case | Stage2 entry | Green comparison entry | green_lateness_ratio | interpretation |
|---|---:|---:|---:|---|
| 클래시스 | 25,150 | 32,900 | 0.43 | Green moderately late but still usable |
| 덴티움 | 77,000 | 139,700 | 0.58 | Green captured some upside but Stage2 was far superior |
| 뷰노 | 14,770 | not_applicable | not_applicable | revision-style Green would miss structural reimbursement move |
| 레이 | 35,550 | no valid Green | not_applicable | Green should be blocked by execution risk |
| 인바디 | 29,000 | no valid Green | not_applicable | spike should stay Stage2/watch, not Green |

## 15. 4B Local vs Full-window Timing Audit

| trigger | four_b_evidence_type | local proximity | full-window proximity | verdict |
|---|---|---:|---:|---|
| T-338220-2023-09-07-4B | valuation_blowoff, positioning_overheat, price_only_local_peak | 0.96 | 0.96 | good_full_window_4B_timing |
| T-214150-2023-11-30-implicit | price_only, valuation_repricing | 1.00 | 1.00 | watch-only unless non-price 4B emerges |
| T-145720-2023-06-02-implicit | price_only, valuation_repricing | 1.00 | 1.00 | watch-only unless revision/margin fatigue emerges |

## 16. 4C Protection Audit

레이 is the main 4C case: after the earlier export/channel thesis failed to hold, the 2023-08-14 break from 37,200/36,750 area to 28,250 close and subsequent lows below 20,000 created a thesis-break route. Label: `hard_4c_success`. VUNO's post-September collapse is a 4B-to-risk-management lesson, but not a hard 4C thesis-break unless reimbursement/adoption evidence itself breaks.

## 17. Sector-Specific Rule Candidate

No sector-wide rule is proposed. The sample is all L7 and one canonical archetype. Extending it to all healthcare would be too broad because trial-data, commercialization, diagnostics, aesthetic devices, and dental implants have different evidence clocks.

## 18. Canonical-Archetype Rule Candidate

Proposed C25-only shadow rule:

```text
if canonical_archetype_id == C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT:
    positive_stage_promotion requires at least one of:
        implemented reimbursement/utilization evidence,
        repeat export/order evidence,
        installed-base + consumable pull-through,
        margin bridge or early revision evidence.

    if evidence is only single-day device headline, export rumor, or channel narrative:
        block Stage3-Green;
        keep at Stage2/Watch unless follow-through evidence appears.

    if reimbursement/adoption evidence is real but EPS revision is not yet visible:
        allow Stage2-Actionable bonus;
        do not force Green until margin/revision closes.
```

## 19. Before / After Backtest Comparison

| profile_id | scope | selected entries | avg_MFE_90D | avg_MAE_90D | false_positive_rate | missed_structural_count | verdict |
|---|---|---:|---:|---:|---:|---:|---|
| P0 e2r_2_1_stock_web_calibrated_proxy | global current | 5 | 68.93 | -16.10 | 0.40 | 1 | good global, rough C25 edge |
| P0b e2r_2_0_baseline_reference | global old | 5 | 68.93 | -16.10 | 0.60 | 1 | too permissive on device narratives |
| P1 sector_specific_candidate_profile | L7 | 5 | 68.93 | -16.10 | 0.40 | 1 | too broad for L7 |
| P2 canonical_archetype_candidate_profile | C25 | 5 | 104.61 on promoted positives | -8.51 on positives | 0.00 after guard | 0 after reimbursement softener | best alignment |
| P3 counterexample_guard_profile | C25 guard | 2 rejected | 15.41 | -27.48 | 0.00 promoted | 0 | protects against Ray/InBody |

## 20. Score-Return Alignment Matrix

| symbol | before label | after label | MFE_90D | MAE_90D | alignment |
|---:|---|---|---:|---:|---|
| 214150 | Stage2-Actionable | Stage3-Yellow/Green candidate | 67.00 | -7.75 | aligned positive |
| 145720 | Stage2-Actionable | Stage3-Yellow/Green candidate | 75.32 | -2.60 | aligned positive |
| 338220 | Watch/Stage2 too late | Stage2-Actionable | 171.50 | -15.17 | missed structural corrected |
| 228670 | Stage2/possible Yellow | Watch/guarded Stage2 | 18.57 | -44.44 | false positive reduced |
| 041830 | Stage2/possible Yellow | Watch/guarded Stage2 | 12.24 | -10.52 | false positive reduced |

## 21. Coverage Matrix

| large_sector_id | canonical_archetype_id | fine_archetype_id | positive_case_count | counterexample_count | 4B_case_count | 4C_case_count | new_independent_case_count | reused_case_count | calibration_usable_trigger_count | representative_trigger_count | current_profile_error_count | sector_rule_candidate | canonical_rule_candidate | coverage_gap_after_this_loop |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|---|---|
| L7_BIO_HEALTHCARE_MEDICAL | C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT | EXPORT_REIMBURSEMENT_IMPLEMENTATION_QUALITY_GATE | 3 | 2 | 1 | 1 | 5 | 0 | 9 | 5 | 3 | false | true | positive/counterexample balance improved; still needs more reimbursement implementation holdouts |

## 22. Residual Contribution Summary

```text
new_independent_case_count: 5
reused_case_count: 0
reused_case_ids: []
new_symbol_count: 5
same_archetype_new_symbol_count: 5
same_archetype_new_trigger_family_count: 4
new_canonical_archetype_count: 0
new_fine_archetype_count: 5
new_trigger_family_count: 4
tested_existing_calibrated_axes: stage3_green_revision_min, price_only_blowoff_blocks_positive_stage, full_4b_requires_non_price_evidence, hard_4c_thesis_break_routes_to_4c
residual_error_types_found: missed reimbursement implementation structural move; export/channel false positive; single-day device spike false positive
new_axis_proposed: c25_implemented_export_or_reimbursement_bonus; c25_single_day_device_spike_guard; c25_revision_gate_softener_for_reimbursement_implementation
existing_axis_strengthened: price_only_blowoff_blocks_positive_stage; full_4b_requires_non_price_evidence; hard_4c_thesis_break_routes_to_4c
existing_axis_weakened: none globally; C25-only softener for revision gate proposed
existing_axis_kept: stage2_actionable_evidence_bonus; yellow/green thresholds
sector_specific_rule_candidate: false
canonical_archetype_rule_candidate: true
no_new_signal_reason: null
loop_contribution_label: residual_error_found|canonical_archetype_rule_candidate
do_not_propose_new_weight_delta: false
auto_selected_coverage_gap: R7/C25 undercovered after R7/C24
```

## 23. Validation Scope / Non-Validation Scope

Validated:

- stock-web manifest, price basis, and max date.
- symbol profiles and corporate-action caveats.
- 30D/90D/180D OHLC MFE/MAE using stock-web rows and clean 180D windows.
- representative-trigger dedupe logic.

Not validated:

- live candidate status.
- production `stock_agent` code paths.
- external public event articles/disclosures beyond narrative labels.
- investment recommendation suitability.

## 24. Shadow Weight Calibration

```csv
row_type,axis,scope,large_sector_id,canonical_archetype_id,baseline_value,tested_value,delta,reason,backtest_effect,trigger_ids,calibration_usable_count,new_independent_case_count,counterexample_count,confidence,proposal_type,notes
shadow_weight,c25_implemented_export_or_reimbursement_bonus,canonical_archetype_specific,L7_BIO_HEALTHCARE_MEDICAL,C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT,0,1,+1,"implemented export/reimbursement/reorder evidence distinguishes Classys/Dentium/VUNO from Ray/InBody","improves positive/counterexample separation without changing global profile","T-214150-2023-05-02-S2A|T-145720-2022-11-09-S2A|T-338220-2023-02-24-S2A",5,5,2,medium,canonical_shadow_only,"not production; post-calibrated residual"
shadow_weight,c25_single_day_device_spike_guard,canonical_archetype_specific,L7_BIO_HEALTHCARE_MEDICAL,C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT,0,1,+1,"single-day medical-device headline without reimbursement utilization/reorder should not reach Green","reduces Ray/InBody false positives","T-228670-2023-05-15-S2A|T-041830-2023-02-28-S2A",5,5,2,medium,canonical_shadow_only,"guard; not global"
shadow_weight,c25_revision_gate_softener_for_reimbursement_implementation,canonical_archetype_specific,L7_BIO_HEALTHCARE_MEDICAL,C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT,0,1,+1,"AI reimbursement implementation may rerate before classic EPS revision closes","reduces VUNO missed-structural error","T-338220-2023-02-24-S2A",5,5,2,low,canonical_shadow_only,"applies only with policy/reimbursement + customer adoption evidence"
```

## 25. Machine-Readable Rows

### 25.1 price_source_validation

```jsonl
{"row_type":"price_source_validation","source":"Songdaiki/stock-web","source_url":"https://github.com/Songdaiki/stock-web","manifest_path":"atlas/manifest.json","schema_path":"atlas/schema.json","universe_path":"atlas/universe/all_symbols.csv","manifest_max_date":"2026-02-20","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","calibration_shard_root":"atlas/ohlcv_tradable_by_symbol_year","raw_shard_root":"atlas/ohlcv_raw_by_symbol_year","validation_status":"usable_for_historical_calibration"}
```

### 25.2 case rows

```jsonl
{"row_type":"case","case_id":"C25-R7L28-214150-CLASSYS-EXPORT-MARGIN","symbol":"214150","company_name":"클래시스","round":"R7","loop":"28","large_sector_id":"L7_BIO_HEALTHCARE_MEDICAL","canonical_archetype_id":"C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT","fine_archetype_id":"AESTHETIC_DEVICE_EXPORT_CONSUMABLE_MARGIN","case_type":"structural_success","positive_or_counterexample":"positive","best_trigger":"T-214150-2023-05-02-S2A","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"strong_positive_alignment","current_profile_verdict":"current_profile_correct","price_source":"Songdaiki/stock-web","notes":"Export/installed-base/consumable-margin route behaved like a high-quality C25 implementation case, not a one-day device headline."}
{"row_type":"case","case_id":"C25-R7L28-145720-DENTIUM-CHINA-IMPLANT","symbol":"145720","company_name":"덴티움","round":"R7","loop":"28","large_sector_id":"L7_BIO_HEALTHCARE_MEDICAL","canonical_archetype_id":"C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT","fine_archetype_id":"DENTAL_IMPLANT_EXPORT_REORDER_MARGIN","case_type":"structural_success","positive_or_counterexample":"positive","best_trigger":"T-145720-2022-11-09-S2A","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"strong_positive_alignment","current_profile_verdict":"current_profile_correct","price_source":"Songdaiki/stock-web","notes":"China/export dental implant demand with margin visibility produced large follow-through."}
{"row_type":"case","case_id":"C25-R7L28-338220-VUNO-AI-REIMBURSEMENT","symbol":"338220","company_name":"뷰노","round":"R7","loop":"28","large_sector_id":"L7_BIO_HEALTHCARE_MEDICAL","canonical_archetype_id":"C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT","fine_archetype_id":"MEDICAL_AI_REIMBURSEMENT_IMPLEMENTATION","case_type":"missed_structural","positive_or_counterexample":"positive","best_trigger":"T-338220-2023-02-24-S2A","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"missed_structural_if_revision_gate_too_strict","current_profile_verdict":"current_profile_too_late","price_source":"Songdaiki/stock-web","notes":"Medical-AI reimbursement/adoption optionality moved well before conventional earnings revision would fully close."}
{"row_type":"case","case_id":"C25-R7L28-228670-RAY-CHINA-DENTAL-CALL-OFF","symbol":"228670","company_name":"레이","round":"R7","loop":"28","large_sector_id":"L7_BIO_HEALTHCARE_MEDICAL","canonical_archetype_id":"C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT","fine_archetype_id":"DENTAL_DIGITAL_EXPORT_EXECUTION_RISK","case_type":"failed_rerating","positive_or_counterexample":"counterexample","best_trigger":"T-228670-2023-05-15-S2A","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"weak_score_return_alignment","current_profile_verdict":"current_profile_false_positive","price_source":"Songdaiki/stock-web","notes":"Export/channel narrative rallied briefly, but drawdown showed that order quality and execution risk were not closed."}
{"row_type":"case","case_id":"C25-R7L28-041830-INBODY-EXPORT-SPIKE","symbol":"041830","company_name":"인바디","round":"R7","loop":"28","large_sector_id":"L7_BIO_HEALTHCARE_MEDICAL","canonical_archetype_id":"C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT","fine_archetype_id":"BODY_COMPOSITION_DEVICE_SINGLE_SPIKE_GUARD","case_type":"price_moved_without_evidence","positive_or_counterexample":"counterexample","best_trigger":"T-041830-2023-02-28-S2A","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"single_spike_no_sustained_rerating","current_profile_verdict":"current_profile_false_positive","price_source":"Songdaiki/stock-web","notes":"One-off export/earnings enthusiasm did not become a durable C25 rerating without visible implementation/reorder evidence."}
```

### 25.3 trigger rows

```jsonl
{"row_type":"trigger","trigger_id":"T-214150-2023-05-02-S2A","case_id":"C25-R7L28-214150-CLASSYS-EXPORT-MARGIN","symbol":"214150","company_name":"클래시스","round":"R7","loop":"28","large_sector_id":"L7_BIO_HEALTHCARE_MEDICAL","canonical_archetype_id":"C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT","fine_archetype_id":"AESTHETIC_DEVICE_EXPORT_CONSUMABLE_MARGIN","sector":"bio_healthcare_medical","primary_archetype":"medical_device_export_reimbursement","loop_objective":"coverage_gap_fill|counterexample_mining|canonical_archetype_compression","trigger_type":"Stage2-Actionable","trigger_date":"2023-05-02","evidence_available_at_that_date":"Export/installed-base/consumable-margin evidence after 2023 spring earnings momentum; stock-web close used for event-level entry.","evidence_source":"historical public earnings/export narrative; price row verified in stock-web 214150/2023.csv","stage2_evidence_fields":["public_event_or_disclosure","customer_or_order_quality","relative_strength","capacity_or_volume_route"],"stage3_evidence_fields":["margin_bridge","financial_visibility","multiple_public_sources"],"stage4b_evidence_fields":[],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/214/214150/2023.csv","profile_path":"atlas/symbol_profiles/214/214150.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","entry_date":"2023-05-02","entry_price":25150,"MFE_30D_pct":40.95,"MFE_90D_pct":67.0,"MFE_180D_pct":71.17,"MFE_1Y_pct":null,"MFE_2Y_pct":null,"MAE_30D_pct":-7.75,"MAE_90D_pct":-7.75,"MAE_180D_pct":-7.75,"MAE_1Y_pct":null,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2023-11-30","peak_price":43050,"drawdown_after_peak_pct":-32.87,"green_lateness_ratio":0.43,"four_b_local_peak_proximity":null,"four_b_full_window_peak_proximity":null,"four_b_timing_verdict":null,"four_b_evidence_type":[],"four_c_protection_label":null,"trigger_outcome_label":"structural_success","current_profile_verdict":"current_profile_correct","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"G-214150-2023-05-02","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"T-214150-2023-06-14-GREEN","case_id":"C25-R7L28-214150-CLASSYS-EXPORT-MARGIN","symbol":"214150","company_name":"클래시스","round":"R7","loop":"28","large_sector_id":"L7_BIO_HEALTHCARE_MEDICAL","canonical_archetype_id":"C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT","fine_archetype_id":"AESTHETIC_DEVICE_EXPORT_CONSUMABLE_MARGIN","sector":"bio_healthcare_medical","primary_archetype":"medical_device_export_reimbursement","loop_objective":"coverage_gap_fill|counterexample_mining|canonical_archetype_compression","trigger_type":"Stage3-Green","trigger_date":"2023-06-14","evidence_available_at_that_date":"Stronger relative strength and apparent margin bridge after export/consumable narrative became obvious.","evidence_source":"stock-web 214150/2023.csv label-comparison row; external evidence not used for production scoring","stage2_evidence_fields":["relative_strength"],"stage3_evidence_fields":["margin_bridge","financial_visibility"],"stage4b_evidence_fields":[],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/214/214150/2023.csv","profile_path":"atlas/symbol_profiles/214/214150.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","entry_date":"2023-06-14","entry_price":32900,"MFE_30D_pct":16.26,"MFE_90D_pct":30.85,"MFE_180D_pct":30.85,"MFE_1Y_pct":null,"MFE_2Y_pct":null,"MAE_30D_pct":-11.25,"MAE_90D_pct":-11.25,"MAE_180D_pct":-11.25,"MAE_1Y_pct":null,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2023-11-30","peak_price":43050,"drawdown_after_peak_pct":-32.87,"green_lateness_ratio":0.43,"four_b_local_peak_proximity":null,"four_b_full_window_peak_proximity":null,"four_b_timing_verdict":null,"four_b_evidence_type":[],"four_c_protection_label":null,"trigger_outcome_label":"label_comparison_green_not_too_late","current_profile_verdict":"current_profile_correct","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"G-214150-2023-06-14","dedupe_for_aggregate":false,"aggregate_group_role":"label_comparison_only","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":0.25,"do_not_count_as_new_case":true}
{"row_type":"trigger","trigger_id":"T-145720-2022-11-09-S2A","case_id":"C25-R7L28-145720-DENTIUM-CHINA-IMPLANT","symbol":"145720","company_name":"덴티움","round":"R7","loop":"28","large_sector_id":"L7_BIO_HEALTHCARE_MEDICAL","canonical_archetype_id":"C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT","fine_archetype_id":"DENTAL_IMPLANT_EXPORT_REORDER_MARGIN","sector":"bio_healthcare_medical","primary_archetype":"medical_device_export_reimbursement","loop_objective":"coverage_gap_fill|counterexample_mining|canonical_archetype_compression","trigger_type":"Stage2-Actionable","trigger_date":"2022-11-09","evidence_available_at_that_date":"China/export dental implant demand and margin visibility became investable after 2022 autumn earnings/order flow.","evidence_source":"historical earnings/export narrative; price row verified in stock-web 145720/2022.csv","stage2_evidence_fields":["public_event_or_disclosure","customer_or_order_quality","relative_strength","early_revision_signal"],"stage3_evidence_fields":["margin_bridge","financial_visibility","repeat_order_or_conversion"],"stage4b_evidence_fields":[],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/145/145720/2022.csv","profile_path":"atlas/symbol_profiles/145/145720.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","entry_date":"2022-11-09","entry_price":77000,"MFE_30D_pct":20.52,"MFE_90D_pct":75.32,"MFE_180D_pct":140.26,"MFE_1Y_pct":null,"MFE_2Y_pct":null,"MAE_30D_pct":-2.6,"MAE_90D_pct":-2.6,"MAE_180D_pct":-2.6,"MAE_1Y_pct":null,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2023-06-02","peak_price":185000,"drawdown_after_peak_pct":-38.6,"green_lateness_ratio":0.58,"four_b_local_peak_proximity":null,"four_b_full_window_peak_proximity":null,"four_b_timing_verdict":null,"four_b_evidence_type":[],"four_c_protection_label":null,"trigger_outcome_label":"structural_success","current_profile_verdict":"current_profile_correct","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"G-145720-2022-11-09","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"T-145720-2023-03-31-GREEN","case_id":"C25-R7L28-145720-DENTIUM-CHINA-IMPLANT","symbol":"145720","company_name":"덴티움","round":"R7","loop":"28","large_sector_id":"L7_BIO_HEALTHCARE_MEDICAL","canonical_archetype_id":"C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT","fine_archetype_id":"DENTAL_IMPLANT_EXPORT_REORDER_MARGIN","sector":"bio_healthcare_medical","primary_archetype":"medical_device_export_reimbursement","loop_objective":"coverage_gap_fill|counterexample_mining|canonical_archetype_compression","trigger_type":"Stage3-Green","trigger_date":"2023-03-31","evidence_available_at_that_date":"By late March 2023 the rerating became visible in price and margin/revision confidence.","evidence_source":"stock-web 145720/2023.csv label-comparison row","stage2_evidence_fields":["relative_strength"],"stage3_evidence_fields":["confirmed_revision","margin_bridge","financial_visibility"],"stage4b_evidence_fields":[],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/145/145720/2023.csv","profile_path":"atlas/symbol_profiles/145/145720.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","entry_date":"2023-03-31","entry_price":139700,"MFE_30D_pct":32.43,"MFE_90D_pct":32.43,"MFE_180D_pct":32.43,"MFE_1Y_pct":null,"MFE_2Y_pct":null,"MAE_30D_pct":-3.36,"MAE_90D_pct":-18.68,"MAE_180D_pct":-34.0,"MAE_1Y_pct":null,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2023-06-02","peak_price":185000,"drawdown_after_peak_pct":-38.6,"green_lateness_ratio":0.58,"four_b_local_peak_proximity":null,"four_b_full_window_peak_proximity":null,"four_b_timing_verdict":null,"four_b_evidence_type":[],"four_c_protection_label":null,"trigger_outcome_label":"green_somewhat_late_but_still_usable","current_profile_verdict":"current_profile_correct","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"G-145720-2023-03-31","dedupe_for_aggregate":false,"aggregate_group_role":"label_comparison_only","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":0.25,"do_not_count_as_new_case":true}
{"row_type":"trigger","trigger_id":"T-338220-2023-02-24-S2A","case_id":"C25-R7L28-338220-VUNO-AI-REIMBURSEMENT","symbol":"338220","company_name":"뷰노","round":"R7","loop":"28","large_sector_id":"L7_BIO_HEALTHCARE_MEDICAL","canonical_archetype_id":"C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT","fine_archetype_id":"MEDICAL_AI_REIMBURSEMENT_IMPLEMENTATION","sector":"bio_healthcare_medical","primary_archetype":"medical_device_export_reimbursement","loop_objective":"coverage_gap_fill|counterexample_mining|canonical_archetype_compression","trigger_type":"Stage2-Actionable","trigger_date":"2023-02-24","evidence_available_at_that_date":"Medical-AI reimbursement/adoption optionality with hospital-use route; early implementation signal mattered before classic revisions.","evidence_source":"historical public reimbursement/adoption narrative; price row verified in stock-web 338220/2023.csv","stage2_evidence_fields":["public_event_or_disclosure","policy_or_regulatory_optionality","customer_or_order_quality","relative_strength"],"stage3_evidence_fields":["multiple_public_sources"],"stage4b_evidence_fields":[],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/338/338220/2023.csv","profile_path":"atlas/symbol_profiles/338/338220.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","entry_date":"2023-02-24","entry_price":14770,"MFE_30D_pct":35.75,"MFE_90D_pct":171.5,"MFE_180D_pct":370.55,"MFE_1Y_pct":null,"MFE_2Y_pct":null,"MAE_30D_pct":-15.17,"MAE_90D_pct":-15.17,"MAE_180D_pct":-15.17,"MAE_1Y_pct":null,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2023-09-07","peak_price":69500,"drawdown_after_peak_pct":-65.83,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":null,"four_b_full_window_peak_proximity":null,"four_b_timing_verdict":null,"four_b_evidence_type":[],"four_c_protection_label":null,"trigger_outcome_label":"missed_structural_if_revision_gate_too_strict","current_profile_verdict":"current_profile_too_late","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"G-338220-2023-02-24","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"T-338220-2023-09-07-4B","case_id":"C25-R7L28-338220-VUNO-AI-REIMBURSEMENT","symbol":"338220","company_name":"뷰노","round":"R7","loop":"28","large_sector_id":"L7_BIO_HEALTHCARE_MEDICAL","canonical_archetype_id":"C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT","fine_archetype_id":"MEDICAL_AI_REIMBURSEMENT_IMPLEMENTATION","sector":"bio_healthcare_medical","primary_archetype":"medical_device_export_reimbursement","loop_objective":"coverage_gap_fill|counterexample_mining|canonical_archetype_compression","trigger_type":"Stage4B","trigger_date":"2023-09-07","evidence_available_at_that_date":"Post-rerating valuation/positioning overheat; 4B should be overlay, not initial positive stage.","evidence_source":"stock-web 338220/2023.csv 4B overlay row","stage2_evidence_fields":[],"stage3_evidence_fields":[],"stage4b_evidence_fields":["valuation_blowoff","positioning_overheat","price_only_local_peak"],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/338/338220/2023.csv","profile_path":"atlas/symbol_profiles/338/338220.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","entry_date":"2023-09-07","entry_price":63600,"MFE_30D_pct":9.28,"MFE_90D_pct":9.28,"MFE_180D_pct":9.28,"MFE_1Y_pct":null,"MFE_2Y_pct":null,"MAE_30D_pct":-46.7,"MAE_90D_pct":-61.71,"MAE_180D_pct":-61.71,"MAE_1Y_pct":null,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2023-09-07","peak_price":69500,"drawdown_after_peak_pct":-65.83,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":0.96,"four_b_full_window_peak_proximity":0.96,"four_b_timing_verdict":"good_full_window_4B_timing","four_b_evidence_type":["valuation_blowoff","positioning_overheat","price_only_local_peak"],"four_c_protection_label":null,"trigger_outcome_label":"4B_overlay_success","current_profile_verdict":"current_profile_correct","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"G-338220-2023-09-07","dedupe_for_aggregate":false,"aggregate_group_role":"4B_overlay_only","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":0.25,"do_not_count_as_new_case":true}
{"row_type":"trigger","trigger_id":"T-228670-2023-05-15-S2A","case_id":"C25-R7L28-228670-RAY-CHINA-DENTAL-CALL-OFF","symbol":"228670","company_name":"레이","round":"R7","loop":"28","large_sector_id":"L7_BIO_HEALTHCARE_MEDICAL","canonical_archetype_id":"C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT","fine_archetype_id":"DENTAL_DIGITAL_EXPORT_EXECUTION_RISK","sector":"bio_healthcare_medical","primary_archetype":"medical_device_export_reimbursement","loop_objective":"coverage_gap_fill|counterexample_mining|canonical_archetype_compression","trigger_type":"Stage2-Actionable","trigger_date":"2023-05-15","evidence_available_at_that_date":"Dental digital export/channel narrative after spring 2023; recurring order quality and execution risk not closed.","evidence_source":"historical public export/channel narrative; price row verified in stock-web 228670/2023.csv","stage2_evidence_fields":["public_event_or_disclosure","relative_strength","customer_or_order_quality"],"stage3_evidence_fields":[],"stage4b_evidence_fields":["execution_risk_score"],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/228/228670/2023.csv","profile_path":"atlas/symbol_profiles/228/228670.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","entry_date":"2023-05-15","entry_price":35550,"MFE_30D_pct":18.57,"MFE_90D_pct":18.57,"MFE_180D_pct":18.57,"MFE_1Y_pct":null,"MFE_2Y_pct":null,"MAE_30D_pct":-7.45,"MAE_90D_pct":-44.44,"MAE_180D_pct":-45.43,"MAE_1Y_pct":null,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2023-06-15","peak_price":42150,"drawdown_after_peak_pct":-54.0,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":null,"four_b_full_window_peak_proximity":null,"four_b_timing_verdict":null,"four_b_evidence_type":["execution_risk_score"],"four_c_protection_label":null,"trigger_outcome_label":"failed_rerating","current_profile_verdict":"current_profile_false_positive","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"G-228670-2023-05-15","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"T-228670-2023-08-14-4C","case_id":"C25-R7L28-228670-RAY-CHINA-DENTAL-CALL-OFF","symbol":"228670","company_name":"레이","round":"R7","loop":"28","large_sector_id":"L7_BIO_HEALTHCARE_MEDICAL","canonical_archetype_id":"C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT","fine_archetype_id":"DENTAL_DIGITAL_EXPORT_EXECUTION_RISK","sector":"bio_healthcare_medical","primary_archetype":"medical_device_export_reimbursement","loop_objective":"coverage_gap_fill|counterexample_mining|canonical_archetype_compression","trigger_type":"Stage4C","trigger_date":"2023-08-14","evidence_available_at_that_date":"Sharp post-earnings/order-quality repricing; thesis moved from watch to broken for the earlier export rerating thesis.","evidence_source":"stock-web 228670/2023.csv 4C overlay row","stage2_evidence_fields":[],"stage3_evidence_fields":[],"stage4b_evidence_fields":["margin_or_backlog_slowdown"],"stage4c_evidence_fields":["call_off_or_order_cut","thesis_evidence_broken"],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/228/228670/2023.csv","profile_path":"atlas/symbol_profiles/228/228670.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","entry_date":"2023-08-14","entry_price":28250,"MFE_30D_pct":4.07,"MFE_90D_pct":11.5,"MFE_180D_pct":11.5,"MFE_1Y_pct":null,"MFE_2Y_pct":null,"MAE_30D_pct":-25.66,"MAE_90D_pct":-31.33,"MAE_180D_pct":-31.33,"MAE_1Y_pct":null,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2023-08-24","peak_price":29400,"drawdown_after_peak_pct":-34.01,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":null,"four_b_full_window_peak_proximity":null,"four_b_timing_verdict":null,"four_b_evidence_type":["margin_or_backlog_slowdown"],"four_c_protection_label":"hard_4c_success","trigger_outcome_label":"4C_success","current_profile_verdict":"current_profile_4C_too_late","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"G-228670-2023-08-14","dedupe_for_aggregate":false,"aggregate_group_role":"4C_overlay_only","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":0.25,"do_not_count_as_new_case":true}
{"row_type":"trigger","trigger_id":"T-041830-2023-02-28-S2A","case_id":"C25-R7L28-041830-INBODY-EXPORT-SPIKE","symbol":"041830","company_name":"인바디","round":"R7","loop":"28","large_sector_id":"L7_BIO_HEALTHCARE_MEDICAL","canonical_archetype_id":"C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT","fine_archetype_id":"BODY_COMPOSITION_DEVICE_SINGLE_SPIKE_GUARD","sector":"bio_healthcare_medical","primary_archetype":"medical_device_export_reimbursement","loop_objective":"coverage_gap_fill|counterexample_mining|canonical_archetype_compression","trigger_type":"Stage2-Actionable","trigger_date":"2023-02-28","evidence_available_at_that_date":"Device export/earnings enthusiasm after single sharp rerating day; durable reimbursement/export implementation not proven.","evidence_source":"historical earnings/export narrative; price row verified in stock-web 041830/2023.csv","stage2_evidence_fields":["public_event_or_disclosure","relative_strength"],"stage3_evidence_fields":[],"stage4b_evidence_fields":["price_only_local_peak"],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/041/041830/2023.csv","profile_path":"atlas/symbol_profiles/041/041830.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","entry_date":"2023-02-28","entry_price":29000,"MFE_30D_pct":5.0,"MFE_90D_pct":12.24,"MFE_180D_pct":12.24,"MFE_1Y_pct":null,"MFE_2Y_pct":null,"MAE_30D_pct":-7.07,"MAE_90D_pct":-10.52,"MAE_180D_pct":-18.97,"MAE_1Y_pct":null,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2023-04-11","peak_price":32550,"drawdown_after_peak_pct":-24.27,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":null,"four_b_full_window_peak_proximity":null,"four_b_timing_verdict":null,"four_b_evidence_type":["price_only_local_peak"],"four_c_protection_label":null,"trigger_outcome_label":"price_moved_without_evidence","current_profile_verdict":"current_profile_false_positive","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"G-041830-2023-02-28","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
```

### 25.4 score_simulation rows

```jsonl
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"C25-R7L28-214150-CLASSYS-EXPORT-MARGIN","trigger_id":"T-214150-2023-05-02-S2A","symbol":"214150","large_sector_id":"L7_BIO_HEALTHCARE_MEDICAL","canonical_archetype_id":"C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT","raw_component_scores_before":{"contract_score":2,"backlog_visibility_score":0,"margin_bridge_score":18,"revision_score":16,"relative_strength_score":14,"customer_quality_score":16,"policy_or_regulatory_score":0,"valuation_repricing_score":10,"execution_risk_score":3,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_before":74.2,"stage_label_before":"Stage2-Actionable","raw_component_scores_after":{"contract_score":2,"backlog_visibility_score":0,"margin_bridge_score":20,"revision_score":16,"relative_strength_score":14,"customer_quality_score":18,"policy_or_regulatory_score":0,"valuation_repricing_score":10,"execution_risk_score":3,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_after":78.2,"stage_label_after":"Stage3-Yellow","changed_components":["customer_quality_score","policy_or_regulatory_score","execution_risk_score","margin_bridge_score"],"component_delta_explanation":"C25 shadow profile separates implemented export/reimbursement/reorder evidence from single-day device narrative and execution-risk cases.","MFE_90D_pct":67.0,"MAE_90D_pct":-7.75,"score_return_alignment_label":"structural_success","current_profile_verdict":"current_profile_correct"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"C25-R7L28-214150-CLASSYS-EXPORT-MARGIN","trigger_id":"T-214150-2023-06-14-GREEN","symbol":"214150","large_sector_id":"L7_BIO_HEALTHCARE_MEDICAL","canonical_archetype_id":"C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT","raw_component_scores_before":{"contract_score":2,"backlog_visibility_score":0,"margin_bridge_score":18,"revision_score":16,"relative_strength_score":14,"customer_quality_score":16,"policy_or_regulatory_score":0,"valuation_repricing_score":10,"execution_risk_score":3,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_before":74.2,"stage_label_before":"Stage2-Actionable","raw_component_scores_after":{"contract_score":2,"backlog_visibility_score":0,"margin_bridge_score":20,"revision_score":16,"relative_strength_score":14,"customer_quality_score":18,"policy_or_regulatory_score":0,"valuation_repricing_score":10,"execution_risk_score":3,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_after":78.2,"stage_label_after":"Stage3-Yellow","changed_components":["customer_quality_score","policy_or_regulatory_score","execution_risk_score","margin_bridge_score"],"component_delta_explanation":"C25 shadow profile separates implemented export/reimbursement/reorder evidence from single-day device narrative and execution-risk cases.","MFE_90D_pct":30.85,"MAE_90D_pct":-11.25,"score_return_alignment_label":"label_comparison_green_not_too_late","current_profile_verdict":"current_profile_correct"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"C25-R7L28-145720-DENTIUM-CHINA-IMPLANT","trigger_id":"T-145720-2022-11-09-S2A","symbol":"145720","large_sector_id":"L7_BIO_HEALTHCARE_MEDICAL","canonical_archetype_id":"C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT","raw_component_scores_before":{"contract_score":4,"backlog_visibility_score":0,"margin_bridge_score":20,"revision_score":18,"relative_strength_score":13,"customer_quality_score":18,"policy_or_regulatory_score":0,"valuation_repricing_score":11,"execution_risk_score":3,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_before":82.2,"stage_label_before":"Stage3-Yellow","raw_component_scores_after":{"contract_score":4,"backlog_visibility_score":0,"margin_bridge_score":22,"revision_score":18,"relative_strength_score":13,"customer_quality_score":20,"policy_or_regulatory_score":0,"valuation_repricing_score":11,"execution_risk_score":3,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_after":86.2,"stage_label_after":"Stage3-Yellow","changed_components":["customer_quality_score","policy_or_regulatory_score","execution_risk_score","margin_bridge_score"],"component_delta_explanation":"C25 shadow profile separates implemented export/reimbursement/reorder evidence from single-day device narrative and execution-risk cases.","MFE_90D_pct":75.32,"MAE_90D_pct":-2.6,"score_return_alignment_label":"structural_success","current_profile_verdict":"current_profile_correct"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"C25-R7L28-145720-DENTIUM-CHINA-IMPLANT","trigger_id":"T-145720-2023-03-31-GREEN","symbol":"145720","large_sector_id":"L7_BIO_HEALTHCARE_MEDICAL","canonical_archetype_id":"C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT","raw_component_scores_before":{"contract_score":4,"backlog_visibility_score":0,"margin_bridge_score":20,"revision_score":18,"relative_strength_score":13,"customer_quality_score":18,"policy_or_regulatory_score":0,"valuation_repricing_score":11,"execution_risk_score":3,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_before":82.2,"stage_label_before":"Stage3-Yellow","raw_component_scores_after":{"contract_score":4,"backlog_visibility_score":0,"margin_bridge_score":22,"revision_score":18,"relative_strength_score":13,"customer_quality_score":20,"policy_or_regulatory_score":0,"valuation_repricing_score":11,"execution_risk_score":3,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_after":86.2,"stage_label_after":"Stage3-Yellow","changed_components":["customer_quality_score","policy_or_regulatory_score","execution_risk_score","margin_bridge_score"],"component_delta_explanation":"C25 shadow profile separates implemented export/reimbursement/reorder evidence from single-day device narrative and execution-risk cases.","MFE_90D_pct":32.43,"MAE_90D_pct":-18.68,"score_return_alignment_label":"green_somewhat_late_but_still_usable","current_profile_verdict":"current_profile_correct"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"C25-R7L28-338220-VUNO-AI-REIMBURSEMENT","trigger_id":"T-338220-2023-02-24-S2A","symbol":"338220","large_sector_id":"L7_BIO_HEALTHCARE_MEDICAL","canonical_archetype_id":"C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT","raw_component_scores_before":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":0,"revision_score":5,"relative_strength_score":15,"customer_quality_score":12,"policy_or_regulatory_score":22,"valuation_repricing_score":13,"execution_risk_score":8,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_before":62.2,"stage_label_before":"Stage2-Actionable","raw_component_scores_after":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":0,"revision_score":7,"relative_strength_score":15,"customer_quality_score":14,"policy_or_regulatory_score":26,"valuation_repricing_score":13,"execution_risk_score":8,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_after":70.2,"stage_label_after":"Stage2-Actionable","changed_components":["customer_quality_score","policy_or_regulatory_score","execution_risk_score","margin_bridge_score"],"component_delta_explanation":"C25 shadow profile separates implemented export/reimbursement/reorder evidence from single-day device narrative and execution-risk cases.","MFE_90D_pct":171.5,"MAE_90D_pct":-15.17,"score_return_alignment_label":"missed_structural_if_revision_gate_too_strict","current_profile_verdict":"current_profile_too_late"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"C25-R7L28-338220-VUNO-AI-REIMBURSEMENT","trigger_id":"T-338220-2023-09-07-4B","symbol":"338220","large_sector_id":"L7_BIO_HEALTHCARE_MEDICAL","canonical_archetype_id":"C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT","raw_component_scores_before":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":0,"revision_score":5,"relative_strength_score":15,"customer_quality_score":12,"policy_or_regulatory_score":22,"valuation_repricing_score":13,"execution_risk_score":8,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_before":62.2,"stage_label_before":"Stage4B-overlay","raw_component_scores_after":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":0,"revision_score":7,"relative_strength_score":15,"customer_quality_score":14,"policy_or_regulatory_score":26,"valuation_repricing_score":13,"execution_risk_score":8,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_after":70.2,"stage_label_after":"Stage4B-overlay","changed_components":["customer_quality_score","policy_or_regulatory_score","execution_risk_score","margin_bridge_score"],"component_delta_explanation":"C25 shadow profile separates implemented export/reimbursement/reorder evidence from single-day device narrative and execution-risk cases.","MFE_90D_pct":9.28,"MAE_90D_pct":-61.71,"score_return_alignment_label":"4B_overlay_success","current_profile_verdict":"current_profile_correct"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"C25-R7L28-228670-RAY-CHINA-DENTAL-CALL-OFF","trigger_id":"T-228670-2023-05-15-S2A","symbol":"228670","large_sector_id":"L7_BIO_HEALTHCARE_MEDICAL","canonical_archetype_id":"C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT","raw_component_scores_before":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":2,"revision_score":3,"relative_strength_score":12,"customer_quality_score":10,"policy_or_regulatory_score":0,"valuation_repricing_score":8,"execution_risk_score":18,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_before":24.2,"stage_label_before":"Watch/Stage2","raw_component_scores_after":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":2,"revision_score":3,"relative_strength_score":12,"customer_quality_score":7,"policy_or_regulatory_score":0,"valuation_repricing_score":6,"execution_risk_score":23,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_after":16.2,"stage_label_after":"Watch/Stage2","changed_components":["customer_quality_score","policy_or_regulatory_score","execution_risk_score","margin_bridge_score"],"component_delta_explanation":"C25 shadow profile separates implemented export/reimbursement/reorder evidence from single-day device narrative and execution-risk cases.","MFE_90D_pct":18.57,"MAE_90D_pct":-44.44,"score_return_alignment_label":"failed_rerating","current_profile_verdict":"current_profile_false_positive"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"C25-R7L28-228670-RAY-CHINA-DENTAL-CALL-OFF","trigger_id":"T-228670-2023-08-14-4C","symbol":"228670","large_sector_id":"L7_BIO_HEALTHCARE_MEDICAL","canonical_archetype_id":"C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT","raw_component_scores_before":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":2,"revision_score":3,"relative_strength_score":12,"customer_quality_score":10,"policy_or_regulatory_score":0,"valuation_repricing_score":8,"execution_risk_score":18,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_before":24.2,"stage_label_before":"Stage4C","raw_component_scores_after":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":2,"revision_score":3,"relative_strength_score":12,"customer_quality_score":7,"policy_or_regulatory_score":0,"valuation_repricing_score":6,"execution_risk_score":23,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_after":16.2,"stage_label_after":"Stage4C","changed_components":["customer_quality_score","policy_or_regulatory_score","execution_risk_score","margin_bridge_score"],"component_delta_explanation":"C25 shadow profile separates implemented export/reimbursement/reorder evidence from single-day device narrative and execution-risk cases.","MFE_90D_pct":11.5,"MAE_90D_pct":-31.33,"score_return_alignment_label":"4C_success","current_profile_verdict":"current_profile_4C_too_late"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"C25-R7L28-041830-INBODY-EXPORT-SPIKE","trigger_id":"T-041830-2023-02-28-S2A","symbol":"041830","large_sector_id":"L7_BIO_HEALTHCARE_MEDICAL","canonical_archetype_id":"C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT","raw_component_scores_before":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":5,"revision_score":3,"relative_strength_score":12,"customer_quality_score":0,"policy_or_regulatory_score":0,"valuation_repricing_score":6,"execution_risk_score":10,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_before":20.0,"stage_label_before":"Watch/Stage2","raw_component_scores_after":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":5,"revision_score":3,"relative_strength_score":10,"customer_quality_score":0,"policy_or_regulatory_score":0,"valuation_repricing_score":6,"execution_risk_score":14,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_after":15.6,"stage_label_after":"Watch/Stage2","changed_components":["customer_quality_score","policy_or_regulatory_score","execution_risk_score","margin_bridge_score"],"component_delta_explanation":"C25 shadow profile separates implemented export/reimbursement/reorder evidence from single-day device narrative and execution-risk cases.","MFE_90D_pct":12.24,"MAE_90D_pct":-10.52,"score_return_alignment_label":"price_moved_without_evidence","current_profile_verdict":"current_profile_false_positive"}
```

### 25.5 shadow_weight rows

```csv
row_type,axis,scope,large_sector_id,canonical_archetype_id,baseline_value,tested_value,delta,reason,backtest_effect,trigger_ids,calibration_usable_count,new_independent_case_count,counterexample_count,confidence,proposal_type,notes
shadow_weight,c25_implemented_export_or_reimbursement_bonus,canonical_archetype_specific,L7_BIO_HEALTHCARE_MEDICAL,C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT,0,1,+1,"implemented export/reimbursement/reorder evidence distinguishes Classys/Dentium/VUNO from Ray/InBody","improves positive/counterexample separation without changing global profile","T-214150-2023-05-02-S2A|T-145720-2022-11-09-S2A|T-338220-2023-02-24-S2A",5,5,2,medium,canonical_shadow_only,"not production; post-calibrated residual"
shadow_weight,c25_single_day_device_spike_guard,canonical_archetype_specific,L7_BIO_HEALTHCARE_MEDICAL,C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT,0,1,+1,"single-day medical-device headline without reimbursement utilization/reorder should not reach Green","reduces Ray/InBody false positives","T-228670-2023-05-15-S2A|T-041830-2023-02-28-S2A",5,5,2,medium,canonical_shadow_only,"guard; not global"
shadow_weight,c25_revision_gate_softener_for_reimbursement_implementation,canonical_archetype_specific,L7_BIO_HEALTHCARE_MEDICAL,C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT,0,1,+1,"AI reimbursement implementation may rerate before classic EPS revision closes","reduces VUNO missed-structural error","T-338220-2023-02-24-S2A",5,5,2,low,canonical_shadow_only,"applies only with policy/reimbursement + customer adoption evidence"
```

### 25.6 residual_contribution row

```jsonl
{"row_type":"residual_contribution","round":"R7","loop":"28","large_sector_id":"L7_BIO_HEALTHCARE_MEDICAL","canonical_archetype_id":"C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT","new_independent_case_count":5,"reused_case_count":0,"new_symbol_count":5,"same_archetype_new_symbol_count":5,"same_archetype_new_trigger_family_count":4,"new_canonical_archetype_count":0,"new_trigger_family_count":4,"positive_case_count":3,"counterexample_count":2,"current_profile_error_count":3,"tested_existing_calibrated_axes":["stage3_green_revision_min","price_only_blowoff_blocks_positive_stage","full_4b_requires_non_price_evidence","hard_4c_thesis_break_routes_to_4c"],"residual_error_types_found":["C25 reimbursement implementation missed structural if revision gate too strict","single-day device narrative false positive","export channel execution-risk false positive"],"loop_contribution_label":"residual_error_found|canonical_archetype_rule_candidate","do_not_propose_new_weight_delta":false,"auto_selected_coverage_gap":"R7/C25 lacked balanced positive/counterexample coverage after prior R7/C24 trial-data loop"}
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
next_round = R8
next_large_sector_id = L8_PLATFORM_CONTENT_SW_SECURITY
next_canonical_archetype_id = C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE
reason = R7 C24/C25 now has balanced positive/counterexample residual coverage; move to undercovered platform/software archetypes.
```

## 28. Source Notes

- Price source: Songdaiki/stock-web `atlas/manifest.json`, `atlas/symbol_profiles/*`, and `atlas/ohlcv_tradable_by_symbol_year/*`.
- Price basis: raw/unadjusted FinanceData/marcap transformed into stock-web shards.
- Key verified OHLC rows include: 214150 2023-05-02 close 25,150 and 2023-11-30 high 43,050; 145720 2022-11-09 close 77,000 and 2023-06-02 high 185,000; 338220 2023-02-24 close 14,770 and 2023-09-07 high 69,500; 228670 2023-05-15 close 35,550 and subsequent low path through 2023-11/12; 041830 2023-02-28 close 29,000 and capped MFE through 2023 spring.
- External event-source validation should be completed before implementation promotion. This MD is shadow-only calibration research, not an investment recommendation.
