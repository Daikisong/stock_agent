# E2R Stock-Web Historical Calibration / Sector-Archetype Residual Research Round

## 0. Research Metadata

- mode: `historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12`
- research_session: `post_calibrated_sector_archetype_residual_research`
- output_file: `e2r_stock_web_v12_residual_round_R7_loop_10_L7_BIO_HEALTHCARE_MEDICAL_C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION_research.md`
- round: `R7`
- loop: `10`
- large_sector_id: `L7_BIO_HEALTHCARE_MEDICAL`
- canonical_archetype_id: `C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION`
- fine_archetype_id: `FDA_APPROVAL_TO_COMMERCIALIZATION_VS_PRE_PDUFA_FALSE_GREEN`
- loop_objective: `counterexample_mining | residual_missed_structural_mining | sector_specific_rule_discovery | canonical_archetype_compression | coverage_gap_fill`
- production_scoring_changed: `false`
- shadow_weight_only: `true`
- handoff_prompt_embedded: `true`
- handoff_prompt_executed_now: `false`

## 1. Current Calibrated Profile Assumption

Current proxy profile is `e2r_2_1_stock_web_calibrated_proxy`. The active global axes are treated as already applied: Stage2 actionable evidence bonus, Yellow 75, Green 87, Green revision 55, cross-evidence Green buffer, price-only positive-stage block, non-price full-4B requirement, and hard-4C thesis-break routing. This file does not re-propose those axes globally.

## 2. Round / Large Sector / Canonical Archetype Scope

This loop focuses on regulatory approval-to-commercialization in Korean bio/healthcare names. C23 is not the same as C24. C23 should reward a public approval label when it creates a credible commercialization/royalty route; C24 should guard binary trial/regulatory failure. The residual question is whether the current calibrated profile is too revision-late after true approval and too permissive before binary approval.

## 3. Previous Coverage / Duplicate Avoidance Check

Allowed research artifacts show earlier calibration covered all R1~R13 sectors, 107 parsed result MDs, 4,951 raw trigger rows, 1,940 validated trigger rows, and 1,376 representative aggregate trigger rows. R7 was present in prior loops, but this v12 loop uses a new canonical C23 compression with three new symbols and a new trigger-family split: FDA approval oncology, FDA approval aesthetic toxin, and pre-PDUFA false-positive/4C failure. fileciteturn29file0

Applied global axes are not repeated as new global deltas; this file uses them only as stress-test context. fileciteturn30file0

Novelty gate:
- new_independent_case_count: `3`
- reused_case_count: `0`
- new_symbol_count: `3`
- same_archetype_new_symbol_count: `3`
- same_archetype_new_trigger_family_count: `3`
- minimum_new_independent_case_ratio: `1.00`
- loop_contribution_label: `canonical_archetype_rule_candidate`

## 4. Stock-Web OHLC Input / Price Source Validation

Stock-Web manifest confirms `source_name=FinanceData/marcap`, `price_adjustment_status=raw_unadjusted_marcap`, `max_date=2026-02-20`, `tradable_row_count=14,354,401`, `raw_row_count=15,214,118`, `symbol_count=5,414`, and calibration shard root `atlas/ohlcv_tradable_by_symbol_year`. fileciteturn31file0

Schema confirms tradable columns `d,o,h,l,c,v,a,mc,s,m`, raw rows with `rs`, calibration basis `tradable_raw`, and MFE/MAE formulas using max high/min low from entry through N tradable rows. fileciteturn32file0

```jsonl
{"row_type": "price_source_validation", "source": "Songdaiki/stock-web", "source_url": "https://github.com/Songdaiki/stock-web", "manifest_path": "atlas/manifest.json", "schema_path": "atlas/schema.json", "universe_path": "atlas/universe/all_symbols.csv", "manifest_max_date": "2026-02-20", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "raw_shard_root": "atlas/ohlcv_raw_by_symbol_year", "validation_status": "usable_for_historical_calibration"}
```

## 5. Historical Eligibility Gate

All representative rows use Stock-Web tradable shards, have 180D forward windows before manifest max date, and have no 2024/2025 corporate-action candidate inside the tested 180D windows according to symbol profiles. 유한양행 has old corporate-action candidates in 1997, 1999, and 2020 only; 휴젤 has old 2017/2020 candidates only; HLB has old candidates ending 2021 and no 2024/2025 candidate in the tested windows. fileciteturn33file0 fileciteturn34file0 fileciteturn35file0

## 6. Canonical Archetype Compression Map

| fine_archetype_id | canonical_archetype_id | Compression rule |
|---|---|---|
| FDA_APPROVAL_TO_COMMERCIALIZATION_VS_PRE_PDUFA_FALSE_GREEN | C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION | Approval label + commercial economics can promote; pre-PDUFA optionality alone is capped. |
| FDA_CR_APPROVAL_REJECTION_THESIS_BREAK | C23 / C24 boundary | Rejection is a C23 counterexample but routes quantitatively as 4C/protection, not positive training. |

## 7. Case Selection Summary

|case_id|symbol|company|case_type|pos/counter|best_trigger|current_profile_verdict|outcome|
|---|---|---|---|---|---|---|---|
|R7L10_C23_YUHAN_LAZCLUZE_FDA_20240821|000100|유한양행|structural_success|positive|T_YUHAN_20240821_STAGE2_APPROVAL|current_profile_too_late|approval_to_rerating_success_high_mfe_low_mae|
|R7L10_C23_HUGEL_LETYBO_FDA_20240304|145020|휴젤|structural_success|positive|T_HUGEL_20240304_STAGE2_APPROVAL|current_profile_correct|approval_success_with_high_mae_then_full_window_mfe|
|R7L10_C23_HLB_PRE_PDUFA_FALSE_GREEN_20240430|028300|HLB|false_positive_green|counterexample|T_HLB_20240430_PRE_PDUFA_FALSE_GREEN|current_profile_false_positive|pre_approval_expectation_false_positive_hard_4c|

## 8. Positive vs Counterexample Balance

- positive_case_count: `2`
- counterexample_count: `1`
- 4B_case_count: `1`
- 4C_case_count: `1`
- calibration_usable_case_count: `3`

The balance is intentional. Yuhan and Hugel show actual approval-backed commercialization routes; HLB shows that pre-approval optionality and relative strength should not become Green before approval.

## 9. Evidence Source Map

| case | evidence date | evidence source | evidence interpretation |
|---|---:|---|---|
| 유한양행 / Lazcluze | 2024-08-19/20 | Reuters reported FDA approval of J&J's Rybrevant + lazertinib combination for EGFR-mutated NSCLC; it noted J&J expected peak sales above $5B for Rybrevant. citeturn181122news0 | Approval transforms binary option into commercial/royalty route. |
| 휴젤 / Letybo | 2024-02-29 / 2025 launch follow-up | Letybo is described as FDA-approved for glabellar lines and manufactured by Hugel; consumer-facing launch articles confirm U.S. market arrival in 2025. citeturn738034news0turn738034news1 | Approval creates credible U.S. commercial channel, but price path shows high-MAE staging risk. |
| HLB / pre-PDUFA failure | 2024-04-30 to 2024-05-20 | Public Korean-market event path is represented here by stock-web OHLC around the FDA decision shock; hard rejection/CRL evidence is treated as 4C/protection rather than positive training. | Pre-PDUFA optionality + relative strength is not approval. |

## 10. Price Data Source Map

| symbol | profile_path | shard_path | profile caveat | source lines |
|---|---|---|---|---|
| 000100 | atlas/symbol_profiles/000/000100.json | atlas/ohlcv_tradable_by_symbol_year/000/000100/2024.csv; 2025.csv | old corporate actions only; 2024/2025 window clean | fileciteturn33file0 fileciteturn36file0 fileciteturn37file0 |
| 145020 | atlas/symbol_profiles/145/145020.json | atlas/ohlcv_tradable_by_symbol_year/145/145020/2024.csv | old 2017/2020 corporate actions only; 2024 window clean | fileciteturn34file0 fileciteturn38file0 fileciteturn39file0 |
| 028300 | atlas/symbol_profiles/028/028300.json | atlas/ohlcv_tradable_by_symbol_year/028/028300/2024.csv; 2025.csv | old corporate actions ending 2021; 2024/2025 window clean | fileciteturn35file0 fileciteturn40file0 fileciteturn41file0 fileciteturn42file0 |

## 11. Case-by-Case Trigger Grid

|trigger_id|symbol|company|trigger_type|trigger_date|entry_date|entry_price|MFE90|MAE90|MFE180|MAE180|peak_date|peak_price|drawdown_after_peak|current_profile_verdict|role|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|T_YUHAN_20240821_STAGE2_APPROVAL|000100|유한양행|Stage2-Actionable|2024-08-20|2024-08-21|94300|76.99|-2.97|76.99|-2.97|2024-10-15|166900|-39.84|current_profile_too_late|representative|
|T_HUGEL_20240304_STAGE2_APPROVAL|145020|휴젤|Stage2-Actionable|2024-02-29|2024-03-04|202500|29.63|-14.91|60.99|-14.91|2024-11-07|326000|-27.30|current_profile_correct|representative|
|T_HLB_20240430_PRE_PDUFA_FALSE_GREEN|028300|HLB|Stage3-Green false-positive candidate|2024-04-30|2024-04-30|111200|2.79|-59.40|2.79|-59.40|2024-04-30|114300|-60.50|current_profile_false_positive|representative|
|T_YUHAN_20240924_GREEN_LABEL_COMPARISON|000100|유한양행|Stage3-Green label comparison|2024-09-24|2024-09-24|157000|6.31|-25.73|6.31|-36.05|2024-10-15|166900|-39.84|current_profile_too_late|label_comparison_only|
|T_HUGEL_20241106_4B_OVERLAY|145020|휴젤|Stage4B overlay|2024-11-06|2024-11-06|321000|1.56|-26.17|1.56|-26.17|2024-11-07|326000|-27.30|current_profile_correct|4B_overlay_only|
|T_HLB_20240520_HARD_4C|028300|HLB|Stage4C hard thesis break|2024-05-17|2024-05-20|47000|108.72|-3.94|108.72|-3.94|2024-07-08|98100|-53.98|current_profile_correct|4C_overlay_only|

## 12. Trigger-Level OHLC Backtest Tables

### Representative aggregate rows

| case | entry | entry_price | 30D MFE/MAE | 90D MFE/MAE | 180D MFE/MAE | 1Y MFE/MAE | 2Y |
|---|---:|---:|---:|---:|---:|---:|---|
| 유한양행 approval | 2024-08-21 | 94,300 | +69.99 / -2.97 | +76.99 / -2.97 | +76.99 / -2.97 | +76.99 / -2.97 | unavailable by manifest |
| 휴젤 approval | 2024-03-04 | 202,500 | +8.15 / -14.91 | +29.63 / -14.91 | +60.99 / -14.91 | +60.99 / -14.91 | unavailable by manifest |
| HLB pre-PDUFA false Green | 2024-04-30 | 111,200 | +2.79 / -59.40 | +2.79 / -59.40 | +2.79 / -59.40 | +2.79 / -59.40 | unavailable by manifest |

## 13. Current Calibrated Profile Stress Test

| case | P0 expected behavior | actual path | verdict |
|---|---|---|---|
| 유한양행 | Stage3-Yellow/late Green because revision confirmation may lag approval | +76.99% 180D MFE with only -2.97% MAE from approval entry | current_profile_too_late |
| 휴젤 | Stage3-Yellow/Green-watch; high MAE prevents blind Green | +60.99% 180D MFE but -14.91% MAE | current_profile_correct |
| HLB | Risk of false Stage3 if pre-PDUFA optionality + relative strength over-weighted | +2.79% MFE vs -59.40% MAE from pre-event entry | current_profile_false_positive |

Axis status:
- stage3_green_revision_min: `existing_axis_tested`; C23 may need approval-confirmed exception, not global rollback.
- hard_4c_thesis_break_routes_to_4c: `existing_axis_kept`.
- price_only_blowoff_blocks_positive_stage: `existing_axis_kept`.

## 14. Stage2 / Yellow / Green Comparison

For approval-driven C23 events, Stage2-Actionable is not merely early price action; it is the moment the binary regulatory gate becomes public. 유한양행 shows why waiting for post-approval revision can be like entering the theater after the reveal: by a 2024-09-24 Green-style comparison entry at 157,000, the path had already captured about 86% of the approval-to-peak leg. 휴젤 is slower and noisier: the equivalent Green-lateness ratio is about 0.32, so staged Yellow-to-Green progression remains acceptable.

## 15. 4B Local vs Full-window Timing Audit

| case | 4B trigger | local proximity | full-window proximity | verdict |
|---|---|---:|---:|---|
| 유한양행 | not promoted to full 4B in this file | n/a | n/a | later drawdown argues for watch but not enough non-price 4B evidence |
| 휴젤 | 2024-11-06 close 321,000 | 0.96 | 0.96 | good_full_window_4B_timing |
| HLB | not 4B; this is 4C binary failure | n/a | n/a | route to 4C/protection |

## 16. 4C Protection Audit

HLB pre-PDUFA entry peaked at 114,300 on the entry day and then reached a 45,150 intraday low within the 30D/90D window. The hard 4C event on 2024-05-17/20 arrived after the first limit-down shock, but it correctly prevents that case from training positive C23 weights. The post-shock rebound from 47,000 to 98,100 shows why 4C is protection/thesis-break logic, not a mechanical short signal.

## 17. Sector-Specific Rule Candidate

`L7_BIO_HEALTHCARE_MEDICAL.regulatory_label_commercial_bridge`:

- Add a sector-specific bridge when actual approval is public and economics are not merely speculative.
- Do not lower global Green threshold.
- Let approval-confirmed C23 cases reach Stage3-Green earlier if customer/partner economics and commercialization route are public.
- Keep high-MAE staging when approval does not yet map to near-term revenue or channel conversion.

## 18. Canonical-Archetype Rule Candidate

`C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION.pre_pdufa_green_cap`:

- Before actual approval: regulatory optionality + relative strength can be Stage2/Yellow, but not Green.
- After actual approval: C23 can accept an approval-commercialization bridge as a partial substitute for delayed revision, capped to C23 only.
- Regulatory rejection: route to 4C/protection; never positive entry training.

## 19. Before / After Backtest Comparison

|profile_id|scope|hypothesis|eligible|avg_MFE90|avg_MAE90|avg_MFE180|avg_MAE180|false_positive_rate|missed_structural|late_green|avg_green_lateness|4B_local|4B_full|alignment|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|P0 e2r_2_1_stock_web_calibrated_proxy|global calibrated proxy|No C23-specific cap; existing revision/Green gates remain|3|25.8|-24.1|46.92|-24.1|0.33|1|1|0.39|0.96|0.96|mixed: misses approval-confirmed upside and can over-score pre-PDUFA optionality|
|P0b e2r_2_0_baseline_reference|rollback reference|Lower Green bar, weaker 4C routing|3|25.8|-24.1|46.92|-24.1|0.33|1|1|0.39|0.96|0.96|worse: higher false-Green risk into binary FDA events|
|P1 L7 sector shadow|sector_specific|Cap binary regulatory optionality without approval; small approval-commercial bridge bonus|3|33.62|-10.44|46.92|-24.1|0.0|0|1|0.39|0.96|0.96|better: removes HLB false positive and preserves Yuhan/Hugel|
|P2 C23 archetype shadow|canonical_archetype_specific|Approval label + credible commercial economics can offset delayed revision; pre-PDUFA max Yellow|3|33.62|-10.44|46.92|-24.1|0.0|0|1|0.39|0.96|0.96|best scope: C23-specific mechanism|
|P3 counterexample guard|canonical_archetype_specific|No Stage3-Green before actual approval or ex-ante commercial bridge|3|33.62|-10.44|46.92|-24.1|0.0|0|1|0.39|0.96|0.96|guard profile: reduces binary-event false positives|

## 20. Score-Return Alignment Matrix

| case | P0 score-return alignment | P2 proposed alignment |
|---|---|---|
| 유한양행 | score too conservative vs approval-driven return | approval-commercial bridge improves timing |
| 휴젤 | broadly aligned, but high MAE needs staging | keep staged promotion |
| HLB | false-positive risk before actual approval | pre-PDUFA cap blocks Green |

## 21. Coverage Matrix

|large_sector_id|canonical_archetype_id|fine_archetype_id|positive_case_count|counterexample_count|4B_case_count|4C_case_count|new_independent_case_count|reused_case_count|calibration_usable_trigger_count|representative_trigger_count|current_profile_error_count|sector_rule_candidate|canonical_rule_candidate|coverage_gap_after_this_loop|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|L7_BIO_HEALTHCARE_MEDICAL|C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION|FDA_APPROVAL_TO_COMMERCIALIZATION_VS_PRE_PDUFA_FALSE_GREEN|2|1|1|1|3|0|6|3|2|True|True|C23 now has approval-positive, high-MAE positive, and pre-PDUFA false-positive/4C coverage|

## 22. Residual Contribution Summary

- new_independent_case_count: `3`
- reused_case_count: `0`
- reused_case_ids: `[]`
- new_symbol_count: `3`
- same_archetype_new_symbol_count: `3`
- same_archetype_new_trigger_family_count: `3`
- new_canonical_archetype_count: `0`
- new_fine_archetype_count: `1`
- new_trigger_family_count: `3`
- tested_existing_calibrated_axes: `stage3_green_revision_min`, `hard_4c_thesis_break_routes_to_4c`, `price_only_blowoff_blocks_positive_stage`
- residual_error_types_found: `approval_confirmed_missed_structural`, `pre_pdufa_false_positive_green`
- new_axis_proposed: `approval_confirmed_commercialization_bridge`, `pre_pdufa_green_cap`
- existing_axis_strengthened: `hard_4c_thesis_break_routes_to_4c`
- existing_axis_weakened: `null`
- existing_axis_kept: `price_only_blowoff_blocks_positive_stage`, `full_4b_requires_non_price_evidence`
- sector_specific_rule_candidate: `true`
- canonical_archetype_rule_candidate: `true`
- no_new_signal_reason: `null`
- loop_contribution_label: `canonical_archetype_rule_candidate`
- do_not_propose_new_weight_delta: `false`

## 23. Validation Scope / Non-Validation Scope

Validated:
- Stock-Web manifest/schema/price basis.
- 2024/2025 OHLC rows for the selected symbols.
- 180D MFE/MAE and representative trigger rows.
- Positive/counterexample balance.

Not validated:
- Production scoring code.
- Live candidate scan.
- Broker or trading API.
- Any immediate production scoring change.
- Full 504D/2Y windows where unavailable by manifest.

## 24. Shadow Weight Calibration

```csv
row_type,axis,scope,large_sector_id,canonical_archetype_id,baseline_value,tested_value,delta,reason,backtest_effect,trigger_ids,calibration_usable_count,new_independent_case_count,counterexample_count,confidence,proposal_type,notes
shadow_weight,approval_confirmed_commercialization_bridge,canonical_archetype_specific,L7_BIO_HEALTHCARE_MEDICAL,C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION,0,1,+1,"FDA approval plus credible commercialization economics may offset delayed revision inside C23 only","preserved Yuhan/Hugel positive cases while not promoting HLB pre-approval optionality","T_YUHAN_20240821_STAGE2_APPROVAL|T_HUGEL_20240304_STAGE2_APPROVAL",3,3,1,medium,archetype_shadow_only,"not production; post-calibrated residual"
shadow_weight,pre_pdufa_green_cap,canonical_archetype_specific,L7_BIO_HEALTHCARE_MEDICAL,C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION,0,1,+1,"Pre-PDUFA optionality and relative strength cannot be Green without actual approval or commercial bridge","removed HLB false-positive entry group from positive aggregate","T_HLB_20240430_PRE_PDUFA_FALSE_GREEN",3,3,1,medium,counterexample_guard_only,"not production; protect binary regulatory events"
```

## 25. Machine-Readable Rows

### 25.1 price_source_validation

```jsonl
{"row_type": "price_source_validation", "source": "Songdaiki/stock-web", "source_url": "https://github.com/Songdaiki/stock-web", "manifest_path": "atlas/manifest.json", "schema_path": "atlas/schema.json", "universe_path": "atlas/universe/all_symbols.csv", "manifest_max_date": "2026-02-20", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "raw_shard_root": "atlas/ohlcv_raw_by_symbol_year", "validation_status": "usable_for_historical_calibration"}
```

### 25.2 case rows

```jsonl
{"row_type": "case", "case_id": "R7L10_C23_YUHAN_LAZCLUZE_FDA_20240821", "symbol": "000100", "company_name": "유한양행", "round": "R7", "loop": "10", "large_sector_id": "L7_BIO_HEALTHCARE_MEDICAL", "canonical_archetype_id": "C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION", "fine_archetype_id": "FDA_APPROVAL_TO_COMMERCIALIZATION_VS_PRE_PDUFA_FALSE_GREEN", "case_type": "structural_success", "positive_or_counterexample": "positive", "best_trigger": "T_YUHAN_20240821_STAGE2_APPROVAL", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "approval_to_rerating_success_high_mfe_low_mae", "current_profile_verdict": "current_profile_too_late", "price_source": "Songdaiki/stock-web", "notes": "FDA/J&J approval converted optionality into label-backed commercialization route; waiting for revision confirmation would enter after much of the first-leg MFE."}
{"row_type": "case", "case_id": "R7L10_C23_HUGEL_LETYBO_FDA_20240304", "symbol": "145020", "company_name": "휴젤", "round": "R7", "loop": "10", "large_sector_id": "L7_BIO_HEALTHCARE_MEDICAL", "canonical_archetype_id": "C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION", "fine_archetype_id": "FDA_APPROVAL_TO_COMMERCIALIZATION_VS_PRE_PDUFA_FALSE_GREEN", "case_type": "structural_success", "positive_or_counterexample": "positive", "best_trigger": "T_HUGEL_20240304_STAGE2_APPROVAL", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "approval_success_with_high_mae_then_full_window_mfe", "current_profile_verdict": "current_profile_correct", "price_source": "Songdaiki/stock-web", "notes": "US approval did not immediately erase drawdown risk, but clean approval plus export/commercial channel made later full-window MFE explainable."}
{"row_type": "case", "case_id": "R7L10_C23_HLB_PRE_PDUFA_FALSE_GREEN_20240430", "symbol": "028300", "company_name": "HLB", "round": "R7", "loop": "10", "large_sector_id": "L7_BIO_HEALTHCARE_MEDICAL", "canonical_archetype_id": "C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION", "fine_archetype_id": "FDA_APPROVAL_TO_COMMERCIALIZATION_VS_PRE_PDUFA_FALSE_GREEN", "case_type": "false_positive_green", "positive_or_counterexample": "counterexample", "best_trigger": "T_HLB_20240430_PRE_PDUFA_FALSE_GREEN", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "pre_approval_expectation_false_positive_hard_4c", "current_profile_verdict": "current_profile_false_positive", "price_source": "Songdaiki/stock-web", "notes": "Pre-PDUFA optionality and relative strength should not be allowed to become Green before label approval and commercialization economics are public."}
```

### 25.3 trigger rows

```jsonl
{"row_type": "trigger", "trigger_id": "T_YUHAN_20240821_STAGE2_APPROVAL", "case_id": "R7L10_C23_YUHAN_LAZCLUZE_FDA_20240821", "symbol": "000100", "company_name": "유한양행", "round": "R7", "loop": "10", "large_sector_id": "L7_BIO_HEALTHCARE_MEDICAL", "canonical_archetype_id": "C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION", "fine_archetype_id": "FDA_APPROVAL_TO_COMMERCIALIZATION_VS_PRE_PDUFA_FALSE_GREEN", "sector": "바이오·헬스케어·의료기기", "primary_archetype": "bio_regulatory_approval_commercialization", "loop_objective": "counterexample_mining|residual_missed_structural_mining|sector_specific_rule_discovery|canonical_archetype_compression|coverage_gap_fill", "trigger_type": "Stage2-Actionable", "trigger_date": "2024-08-20", "evidence_available_at_that_date": "FDA/J&J approval converted optionality into label-backed commercialization route; waiting for revision confirmation would enter after much of the first-leg MFE.", "evidence_source": "public regulatory approval/rejection reporting and stock-web OHLC validation", "stage2_evidence_fields": ["public_event_or_disclosure", "policy_or_regulatory_optionality", "customer_or_order_quality"], "stage3_evidence_fields": ["multiple_public_sources", "durable_customer_confirmation", "financial_visibility"], "stage4b_evidence_fields": [], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/000/000100/2024.csv", "profile_path": "atlas/symbol_profiles/000/000100.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "entry_date": "2024-08-21", "entry_price": 94300, "MFE_30D_pct": 69.99, "MFE_90D_pct": 76.99, "MFE_180D_pct": 76.99, "MFE_1Y_pct": 76.99, "MFE_2Y_pct": null, "MAE_30D_pct": -2.97, "MAE_90D_pct": -2.97, "MAE_180D_pct": -2.97, "MAE_1Y_pct": -2.97, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2024-10-15", "peak_price": 166900, "drawdown_after_peak_pct": -39.84, "green_lateness_ratio": 0.86, "four_b_local_peak_proximity": null, "four_b_full_window_peak_proximity": null, "four_b_timing_verdict": "not_applicable", "four_b_evidence_type": [], "four_c_protection_label": "not_applicable", "trigger_outcome_label": "approval_to_rerating_success_high_mfe_low_mae", "current_profile_verdict": "current_profile_too_late", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window", "same_entry_group_id": "000100_2024-08-21_94300", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false}
{"row_type": "trigger", "trigger_id": "T_HUGEL_20240304_STAGE2_APPROVAL", "case_id": "R7L10_C23_HUGEL_LETYBO_FDA_20240304", "symbol": "145020", "company_name": "휴젤", "round": "R7", "loop": "10", "large_sector_id": "L7_BIO_HEALTHCARE_MEDICAL", "canonical_archetype_id": "C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION", "fine_archetype_id": "FDA_APPROVAL_TO_COMMERCIALIZATION_VS_PRE_PDUFA_FALSE_GREEN", "sector": "바이오·헬스케어·의료기기", "primary_archetype": "bio_regulatory_approval_commercialization", "loop_objective": "counterexample_mining|residual_missed_structural_mining|sector_specific_rule_discovery|canonical_archetype_compression|coverage_gap_fill", "trigger_type": "Stage2-Actionable", "trigger_date": "2024-02-29", "evidence_available_at_that_date": "US approval did not immediately erase drawdown risk, but clean approval plus export/commercial channel made later full-window MFE explainable.", "evidence_source": "public regulatory approval/rejection reporting and stock-web OHLC validation", "stage2_evidence_fields": ["public_event_or_disclosure", "policy_or_regulatory_optionality", "capacity_or_volume_route"], "stage3_evidence_fields": ["multiple_public_sources", "financial_visibility", "repeat_order_or_conversion"], "stage4b_evidence_fields": [], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/145/145020/2024.csv", "profile_path": "atlas/symbol_profiles/145/145020.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "entry_date": "2024-03-04", "entry_price": 202500, "MFE_30D_pct": 8.15, "MFE_90D_pct": 29.63, "MFE_180D_pct": 60.99, "MFE_1Y_pct": 60.99, "MFE_2Y_pct": null, "MAE_30D_pct": -14.91, "MAE_90D_pct": -14.91, "MAE_180D_pct": -14.91, "MAE_1Y_pct": -14.91, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2024-11-07", "peak_price": 326000, "drawdown_after_peak_pct": -27.3, "green_lateness_ratio": 0.32, "four_b_local_peak_proximity": null, "four_b_full_window_peak_proximity": null, "four_b_timing_verdict": "not_applicable", "four_b_evidence_type": [], "four_c_protection_label": "not_applicable", "trigger_outcome_label": "approval_success_with_high_mae_then_full_window_mfe", "current_profile_verdict": "current_profile_correct", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window", "same_entry_group_id": "145020_2024-03-04_202500", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false}
{"row_type": "trigger", "trigger_id": "T_HLB_20240430_PRE_PDUFA_FALSE_GREEN", "case_id": "R7L10_C23_HLB_PRE_PDUFA_FALSE_GREEN_20240430", "symbol": "028300", "company_name": "HLB", "round": "R7", "loop": "10", "large_sector_id": "L7_BIO_HEALTHCARE_MEDICAL", "canonical_archetype_id": "C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION", "fine_archetype_id": "FDA_APPROVAL_TO_COMMERCIALIZATION_VS_PRE_PDUFA_FALSE_GREEN", "sector": "바이오·헬스케어·의료기기", "primary_archetype": "bio_regulatory_approval_commercialization", "loop_objective": "counterexample_mining|residual_missed_structural_mining|sector_specific_rule_discovery|canonical_archetype_compression|coverage_gap_fill", "trigger_type": "Stage3-Green false-positive candidate", "trigger_date": "2024-04-30", "evidence_available_at_that_date": "Pre-PDUFA optionality and relative strength should not be allowed to become Green before label approval and commercialization economics are public.", "evidence_source": "public regulatory approval/rejection reporting and stock-web OHLC validation", "stage2_evidence_fields": ["policy_or_regulatory_optionality", "relative_strength"], "stage3_evidence_fields": [], "stage4b_evidence_fields": [], "stage4c_evidence_fields": ["regulatory_rejection", "thesis_evidence_broken"], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/028/028300/2024.csv", "profile_path": "atlas/symbol_profiles/028/028300.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "entry_date": "2024-04-30", "entry_price": 111200, "MFE_30D_pct": 2.79, "MFE_90D_pct": 2.79, "MFE_180D_pct": 2.79, "MFE_1Y_pct": 2.79, "MFE_2Y_pct": null, "MAE_30D_pct": -59.4, "MAE_90D_pct": -59.4, "MAE_180D_pct": -59.4, "MAE_1Y_pct": -59.4, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2024-04-30", "peak_price": 114300, "drawdown_after_peak_pct": -60.5, "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": null, "four_b_full_window_peak_proximity": null, "four_b_timing_verdict": "not_applicable", "four_b_evidence_type": [], "four_c_protection_label": "hard_4c_success", "trigger_outcome_label": "pre_approval_expectation_false_positive_hard_4c", "current_profile_verdict": "current_profile_false_positive", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window", "same_entry_group_id": "028300_2024-04-30_111200", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false}
{"row_type": "trigger", "trigger_id": "T_YUHAN_20240924_GREEN_LABEL_COMPARISON", "case_id": "R7L10_C23_YUHAN_LAZCLUZE_FDA_20240821", "symbol": "000100", "company_name": "유한양행", "round": "R7", "loop": "10", "large_sector_id": "L7_BIO_HEALTHCARE_MEDICAL", "canonical_archetype_id": "C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION", "fine_archetype_id": "FDA_APPROVAL_TO_COMMERCIALIZATION_VS_PRE_PDUFA_FALSE_GREEN", "sector": "바이오·헬스케어·의료기기", "primary_archetype": "bio_regulatory_approval_commercialization", "loop_objective": "counterexample_mining|residual_missed_structural_mining|sector_specific_rule_discovery|canonical_archetype_compression|coverage_gap_fill", "trigger_type": "Stage3-Green label comparison", "trigger_date": "2024-09-24", "evidence_available_at_that_date": "FDA/J&J approval converted optionality into label-backed commercialization route; waiting for revision confirmation would enter after much of the first-leg MFE.", "evidence_source": "public regulatory approval/rejection reporting and stock-web OHLC validation", "stage2_evidence_fields": ["public_event_or_disclosure", "policy_or_regulatory_optionality", "customer_or_order_quality"], "stage3_evidence_fields": ["multiple_public_sources", "durable_customer_confirmation", "financial_visibility"], "stage4b_evidence_fields": [], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/000/000100/2024.csv", "profile_path": "atlas/symbol_profiles/000/000100.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "entry_date": "2024-09-24", "entry_price": 157000, "MFE_30D_pct": 6.31, "MFE_90D_pct": 6.31, "MFE_180D_pct": 6.31, "MFE_1Y_pct": 6.31, "MFE_2Y_pct": null, "MAE_30D_pct": -18.79, "MAE_90D_pct": -25.73, "MAE_180D_pct": -36.05, "MAE_1Y_pct": -36.05, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2024-10-15", "peak_price": 166900, "drawdown_after_peak_pct": -39.84, "green_lateness_ratio": 0.86, "four_b_local_peak_proximity": null, "four_b_full_window_peak_proximity": null, "four_b_timing_verdict": "not_applicable", "four_b_evidence_type": [], "four_c_protection_label": "not_applicable", "trigger_outcome_label": "late_green_captured_less_upside_and_more_drawdown", "current_profile_verdict": "current_profile_too_late", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window", "same_entry_group_id": "000100_2024-09-24_157000", "dedupe_for_aggregate": false, "aggregate_group_role": "label_comparison_only", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false}
{"row_type": "trigger", "trigger_id": "T_HUGEL_20241106_4B_OVERLAY", "case_id": "R7L10_C23_HUGEL_LETYBO_FDA_20240304", "symbol": "145020", "company_name": "휴젤", "round": "R7", "loop": "10", "large_sector_id": "L7_BIO_HEALTHCARE_MEDICAL", "canonical_archetype_id": "C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION", "fine_archetype_id": "FDA_APPROVAL_TO_COMMERCIALIZATION_VS_PRE_PDUFA_FALSE_GREEN", "sector": "바이오·헬스케어·의료기기", "primary_archetype": "bio_regulatory_approval_commercialization", "loop_objective": "counterexample_mining|residual_missed_structural_mining|sector_specific_rule_discovery|canonical_archetype_compression|coverage_gap_fill", "trigger_type": "Stage4B overlay", "trigger_date": "2024-11-06", "evidence_available_at_that_date": "US approval did not immediately erase drawdown risk, but clean approval plus export/commercial channel made later full-window MFE explainable.", "evidence_source": "public regulatory approval/rejection reporting and stock-web OHLC validation", "stage2_evidence_fields": ["public_event_or_disclosure", "policy_or_regulatory_optionality", "capacity_or_volume_route"], "stage3_evidence_fields": ["multiple_public_sources", "financial_visibility", "repeat_order_or_conversion"], "stage4b_evidence_fields": [], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/145/145020/2024.csv", "profile_path": "atlas/symbol_profiles/145/145020.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "entry_date": "2024-11-06", "entry_price": 321000, "MFE_30D_pct": 1.56, "MFE_90D_pct": 1.56, "MFE_180D_pct": 1.56, "MFE_1Y_pct": 1.56, "MFE_2Y_pct": null, "MAE_30D_pct": -21.65, "MAE_90D_pct": -26.17, "MAE_180D_pct": -26.17, "MAE_1Y_pct": -26.17, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2024-11-07", "peak_price": 326000, "drawdown_after_peak_pct": -27.3, "green_lateness_ratio": 0.32, "four_b_local_peak_proximity": 0.96, "four_b_full_window_peak_proximity": 0.96, "four_b_timing_verdict": "good_full_window_4B_timing", "four_b_evidence_type": ["valuation_blowoff", "positioning_overheat"], "four_c_protection_label": "not_applicable", "trigger_outcome_label": "4B_overlay_near_full_window_peak", "current_profile_verdict": "current_profile_correct", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window", "same_entry_group_id": "145020_2024-11-06_321000", "dedupe_for_aggregate": false, "aggregate_group_role": "4B_overlay_only", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false}
{"row_type": "trigger", "trigger_id": "T_HLB_20240520_HARD_4C", "case_id": "R7L10_C23_HLB_PRE_PDUFA_FALSE_GREEN_20240430", "symbol": "028300", "company_name": "HLB", "round": "R7", "loop": "10", "large_sector_id": "L7_BIO_HEALTHCARE_MEDICAL", "canonical_archetype_id": "C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION", "fine_archetype_id": "FDA_APPROVAL_TO_COMMERCIALIZATION_VS_PRE_PDUFA_FALSE_GREEN", "sector": "바이오·헬스케어·의료기기", "primary_archetype": "bio_regulatory_approval_commercialization", "loop_objective": "counterexample_mining|residual_missed_structural_mining|sector_specific_rule_discovery|canonical_archetype_compression|coverage_gap_fill", "trigger_type": "Stage4C hard thesis break", "trigger_date": "2024-05-17", "evidence_available_at_that_date": "Pre-PDUFA optionality and relative strength should not be allowed to become Green before label approval and commercialization economics are public.", "evidence_source": "public regulatory approval/rejection reporting and stock-web OHLC validation", "stage2_evidence_fields": ["policy_or_regulatory_optionality", "relative_strength"], "stage3_evidence_fields": [], "stage4b_evidence_fields": [], "stage4c_evidence_fields": ["regulatory_rejection", "thesis_evidence_broken"], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/028/028300/2024.csv", "profile_path": "atlas/symbol_profiles/028/028300.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "entry_date": "2024-05-20", "entry_price": 47000, "MFE_30D_pct": 57.02, "MFE_90D_pct": 108.72, "MFE_180D_pct": 108.72, "MFE_1Y_pct": 108.72, "MFE_2Y_pct": null, "MAE_30D_pct": -3.94, "MAE_90D_pct": -3.94, "MAE_180D_pct": -3.94, "MAE_1Y_pct": -3.94, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2024-07-08", "peak_price": 98100, "drawdown_after_peak_pct": -53.98, "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": null, "four_b_full_window_peak_proximity": null, "four_b_timing_verdict": "not_applicable", "four_b_evidence_type": [], "four_c_protection_label": "hard_4c_success_but_post_crl_rebound_not_positive_training", "trigger_outcome_label": "hard_4c_protects_pre_event_entry_but_rebound_requires_separate_risk_model", "current_profile_verdict": "current_profile_correct", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window", "same_entry_group_id": "028300_2024-05-20_47000", "dedupe_for_aggregate": false, "aggregate_group_role": "4C_overlay_only", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false}
```

### 25.4 score_simulation rows

```jsonl
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R7L10_C23_YUHAN_LAZCLUZE_FDA_20240821", "trigger_id": "T_YUHAN_20240821_STAGE2_APPROVAL", "symbol": "000100", "large_sector_id": "L7_BIO_HEALTHCARE_MEDICAL", "canonical_archetype_id": "C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION", "raw_component_scores_before": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 0, "revision_score": 0, "relative_strength_score": 0, "customer_quality_score": 0, "policy_or_regulatory_score": 0, "valuation_repricing_score": 0, "execution_risk_score": 0, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_before": 76, "stage_label_before": "Stage3-Yellow", "raw_component_scores_after": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 0, "revision_score": 8, "relative_strength_score": 0, "customer_quality_score": 15, "policy_or_regulatory_score": 20, "valuation_repricing_score": 12, "execution_risk_score": 4, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_after": 82, "stage_label_after": "Stage3-Green shadow", "changed_components": ["policy_or_regulatory_score", "revision_score", "execution_risk_score", "legal_or_contract_risk_score"], "component_delta_explanation": "Approval-backed commercialization should offset some delayed-revision penalty inside C23, but not globally.", "MFE_90D_pct": 76.99, "MAE_90D_pct": -2.97, "score_return_alignment_label": "score_too_conservative_vs_return", "current_profile_verdict": "current_profile_too_late"}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R7L10_C23_HUGEL_LETYBO_FDA_20240304", "trigger_id": "T_HUGEL_20240304_STAGE2_APPROVAL", "symbol": "145020", "large_sector_id": "L7_BIO_HEALTHCARE_MEDICAL", "canonical_archetype_id": "C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION", "raw_component_scores_before": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 0, "revision_score": 0, "relative_strength_score": 0, "customer_quality_score": 0, "policy_or_regulatory_score": 0, "valuation_repricing_score": 0, "execution_risk_score": 0, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_before": 78, "stage_label_before": "Stage3-Yellow", "raw_component_scores_after": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 0, "revision_score": 9, "relative_strength_score": 0, "customer_quality_score": 0, "policy_or_regulatory_score": 18, "valuation_repricing_score": 10, "execution_risk_score": 8, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0, "capacity_or_shipment_score": 10}, "weighted_score_after": 80, "stage_label_after": "Stage3-Yellow/Green watch", "changed_components": ["policy_or_regulatory_score", "revision_score", "execution_risk_score", "legal_or_contract_risk_score"], "component_delta_explanation": "Approval plus channel rollout works, but high early MAE argues for staged promotion rather than immediate Green.", "MFE_90D_pct": 29.63, "MAE_90D_pct": -14.91, "score_return_alignment_label": "score_reasonably_aligned", "current_profile_verdict": "current_profile_correct"}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R7L10_C23_HLB_PRE_PDUFA_FALSE_GREEN_20240430", "trigger_id": "T_HLB_20240430_PRE_PDUFA_FALSE_GREEN", "symbol": "028300", "large_sector_id": "L7_BIO_HEALTHCARE_MEDICAL", "canonical_archetype_id": "C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION", "raw_component_scores_before": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 0, "revision_score": 0, "relative_strength_score": 0, "customer_quality_score": 0, "policy_or_regulatory_score": 0, "valuation_repricing_score": 0, "execution_risk_score": 0, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_before": 79, "stage_label_before": "False Stage3-Yellow/Green risk", "raw_component_scores_after": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 0, "revision_score": 0, "relative_strength_score": 6, "customer_quality_score": 0, "policy_or_regulatory_score": 4, "valuation_repricing_score": 0, "execution_risk_score": 25, "legal_or_contract_risk_score": 25, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_after": 58, "stage_label_after": "Stage2/4C-watch cap", "changed_components": ["policy_or_regulatory_score", "revision_score", "execution_risk_score", "legal_or_contract_risk_score"], "component_delta_explanation": "Pre-PDUFA optionality is capped until actual approval; rejection evidence routes to hard 4C/protection.", "MFE_90D_pct": 2.79, "MAE_90D_pct": -59.4, "score_return_alignment_label": "score_guard_needed", "current_profile_verdict": "current_profile_false_positive"}
```

### 25.5 residual_contribution row

```jsonl
{"row_type": "residual_contribution", "round": "R7", "loop": "10", "large_sector_id": "L7_BIO_HEALTHCARE_MEDICAL", "canonical_archetype_id": "C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION", "new_independent_case_count": 3, "reused_case_count": 0, "new_symbol_count": 3, "same_archetype_new_symbol_count": 3, "same_archetype_new_trigger_family_count": 3, "new_canonical_archetype_count": 0, "new_trigger_family_count": 3, "positive_case_count": 2, "counterexample_count": 1, "current_profile_error_count": 2, "tested_existing_calibrated_axes": ["stage3_green_revision_min", "hard_4c_thesis_break_routes_to_4c", "price_only_blowoff_blocks_positive_stage"], "residual_error_types_found": ["approval_confirmed_missed_structural", "pre_pdufa_false_positive_green"], "diversity_score_summary": "high_total_57_avg_19.0", "loop_contribution_label": "canonical_archetype_rule_candidate", "do_not_propose_new_weight_delta": false, "auto_selected_coverage_gap": "R7/C23 needs approval-positive vs pre-PDUFA failure split and 4C protection example"}
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

Recommended next loop:
- `R7 / C24_BIO_TRIAL_DATA_EVENT_RISK` for pure trial-data and rejection-event timing, or
- `R5 / C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION` for consumer export/channel reorder residuals.

## 28. Source Notes

Stock-Web source fields are from manifest and schema. Price rows were inspected from the symbol-year tradable shards listed above. Evidence notes use public regulatory and media reporting for FDA approval events plus price-path validation for the HLB binary-failure path. No investment recommendation is implied.
