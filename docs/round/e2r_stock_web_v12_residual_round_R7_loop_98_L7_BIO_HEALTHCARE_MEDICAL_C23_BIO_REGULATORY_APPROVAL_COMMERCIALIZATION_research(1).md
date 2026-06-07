# E2R Stock-Web Historical Calibration / Sector-Archetype Residual Research Round

## 0. Research Metadata

```text
research_session = post_calibrated_sector_archetype_residual_research
mode = historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12
scheduled_round = R7
scheduled_loop = 98
round_schedule_status = valid
round_sector_consistency = pass
large_sector_id = L7_BIO_HEALTHCARE_MEDICAL
canonical_archetype_id = C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION
fine_archetype_id = BOTULINUM_TOXIN_FDA_APPROVAL_COMMERCIALIZATION_BRIDGE_VS_BIOSIMILAR_COMMERCIALIZATION_FALSE_STAGE2_AND_ONCOLOGY_APPROVAL_EVENT_CAP
loop_objective = coverage_gap_fill | counterexample_mining | stage2_actionable_bonus_stress_test | 4B_4C_guardrail_stress_test | approval_commercialization_guardrail | high_MAE_guardrail | canonical_archetype_compression
output_file = e2r_stock_web_v12_residual_round_R7_loop_98_L7_BIO_HEALTHCARE_MEDICAL_C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION_research.md
```

This file is the corrected final output for this execution. The scheduler is coverage-index-first. A C17 duplicate artifact was generated during this run but is not the final artifact because C17 was already finalized immediately before. After local C08/C09/C01/C07/C06/C10/C14/C11/C02/C13/C19/C27/C12/C24/C28/C17 supplementation, C23 is the next unsupplemented Priority 0 archetype.

## 1. Current Calibrated Profile Assumption

```text
current_default_profile_proxy = e2r_2_2_rolling_calibrated
previous_baseline_reference = e2r_2_1_stock_web_calibrated
production_scoring_changed = false
shadow_weight_only = true
```

Existing axes tested:

```text
stage2_required_bridge = existing_axis_strengthened
local_4b_watch_guard = existing_axis_strengthened
approval_commercialization_guardrail = existing_axis_strengthened
high_MAE_guardrail = existing_axis_strengthened
hard_4c_thesis_break_routes_to_4c = existing_axis_kept
full_4b_requires_non_price_evidence = existing_axis_kept
price_only_blowoff_blocks_positive_stage = existing_axis_kept
```

## 2. Round / Large Sector / Canonical Archetype Scope

```text
scheduled_round = R7
scheduled_loop = 98
large_sector_id = L7_BIO_HEALTHCARE_MEDICAL
canonical_archetype_id = C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION
round_sector_consistency = pass
coverage_index_override_previous_round = true
```

C23 is a regulatory approval-to-commercialization archetype. Approval is the regulatory door opening; the useful signal is whether launch, channel access, pricing, repeat demand, margin and revision walk through that door.

## 3. Previous Coverage / Duplicate Avoidance Check

No-Repeat hard key used:

```text
canonical_archetype_id + symbol + trigger_type + entry_date
```

No-Repeat snapshot context:

```text
C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION = 29 rows / Priority 0
recent local C08/C09/C01/C07/C06/C10/C14/C11/C02/C13/C19/C27/C12/C24/C28/C17 artifacts accounted for but not duplicated
C17 duplicate generated during this run discarded from final output
```

Selected rows avoid hard duplicates and add new C23 trigger families:

```text
145020 / Stage2-Actionable / 2024-02-14
068270 / Stage2-Actionable / 2024-03-29
067630 / Stage4B / 2024-03-25
```

## 4. Stock-Web OHLC Input / Price Source Validation

| field | value |
|---|---|
| source | Songdaiki/stock-web |
| upstream_source | FinanceData/marcap |
| manifest | atlas/manifest.json |
| stock_web_manifest_max_date | 2026-02-20 |
| price_basis | tradable_raw |
| price_adjustment_status | raw_unadjusted_marcap |
| calibration_shard_root | atlas/ohlcv_tradable_by_symbol_year |

| symbol | profile path | CA window status |
|---|---|---|
| 145020 | atlas/symbol_profiles/145/145020.json | selected 2024 window clean after old 2017/2020 CA candidates |
| 068270 | atlas/symbol_profiles/068/068270.json | selected after 2024-01-12 CA candidate; post-CA 180D window |
| 067630 | atlas/symbol_profiles/067/067630.json | selected 2024 window clean after old 2013/2015/2018/2019/2021 CA candidates |

## 5. Historical Eligibility Gate

| case_id | symbol | entry_date | entry in shard | forward 180D | OHLC valid | CA clean | calibration_usable |
|---|---|---:|---|---:|---|---|---|
| R7L98_C23_HUGEL_2024_BOTULINUM_TOXIN_FDA_APPROVAL_COMMERCIALIZATION_BRIDGE_POSITIVE | 145020 | 2024-02-14 | yes | 180 | yes | yes | true |
| R7L98_C23_CELLTRION_2024_BIOSIMILAR_COMMERCIALIZATION_FALSE_STAGE2 | 068270 | 2024-03-29 | yes | 180 | yes | post-CA clean | true |
| R7L98_C23_HLBLIFESCI_2024_ONCOLOGY_APPROVAL_COMMERCIALIZATION_EVENT_CAP_4B | 067630 | 2024-03-25 | yes | 180 | yes | yes | true |

## 6. Canonical Archetype Compression Map

| canonical | fine/deep split | meaning |
|---|---|---|
| C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION | BOTULINUM_TOXIN_FDA_APPROVAL_COMMERCIALIZATION_BRIDGE | Positive Stage2 requires approval-to-launch, channel/distributor, pricing, repeat demand, margin and revision bridge. |
| C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION | BIOSIMILAR_COMMERCIALIZATION_FALSE_STAGE2 | Biosimilar approval watch without sales/channel/pricing/margin bridge can become false Stage2. |
| C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION | ONCOLOGY_APPROVAL_EVENT_CAP_4B | Oncology approval/commercialization event premium should route to 4B when launch/sales/margin bridge is missing. |

## 7. Case Selection Summary

| case_id | symbol | company | role | selected reason |
|---|---|---|---|---|
| R7L98_C23_HUGEL_2024_BOTULINUM_TOXIN_FDA_APPROVAL_COMMERCIALIZATION_BRIDGE_POSITIVE | 145020 | 휴젤 | positive | Botulinum-toxin approval/commercialization bridge produced strong MFE with shallow early MAE. |
| R7L98_C23_CELLTRION_2024_BIOSIMILAR_COMMERCIALIZATION_FALSE_STAGE2 | 068270 | 셀트리온 | counterexample | Biosimilar commercialization watch had low MFE without clear sales/channel/margin bridge. |
| R7L98_C23_HLBLIFESCI_2024_ONCOLOGY_APPROVAL_COMMERCIALIZATION_EVENT_CAP_4B | 067630 | HLB생명과학 | counterexample / 4B | Oncology approval/commercialization premium capped around the March spike and later de-rated deeply. |

## 8. Positive vs Counterexample Balance

```text
positive_case_count = 1
counterexample_count = 2
4B_case_count = 1
4C_case_count = 0
calibration_usable_case_count = 3
calibration_usable_trigger_count = 3
```

## 9. Evidence Source Map

| case | evidence status | evidence_url_pending | source_proxy_only | usage |
|---|---|---|---|---|
| Hugel botulinum-toxin FDA approval commercialization bridge | historical public/report proxy | true | true | shadow-only positive |
| Celltrion biosimilar commercialization false Stage2 | historical public/news proxy | true | true | false-Stage2 guardrail |
| HLB Life Science oncology approval commercialization event cap | historical public/news proxy | true | true | 4B overlay counterexample |

## 10. Price Data Source Map

| symbol | shard | profile |
|---|---|---|
| 145020 | atlas/ohlcv_tradable_by_symbol_year/145/145020/2024.csv | atlas/symbol_profiles/145/145020.json |
| 068270 | atlas/ohlcv_tradable_by_symbol_year/068/068270/2024.csv | atlas/symbol_profiles/068/068270.json |
| 067630 | atlas/ohlcv_tradable_by_symbol_year/067/067630/2024.csv | atlas/symbol_profiles/067/067630.json |

## 11. Case-by-Case Trigger Grid

| trigger_id | symbol | trigger_type | entry_date | entry_price | role | verdict |
|---|---|---|---:|---:|---|---|
| R7L98_C23_HUGEL_2024_STAGE2_ACTIONABLE_BOTULINUM_TOXIN_FDA_APPROVAL_COMMERCIALIZATION_BRIDGE | 145020 | Stage2-Actionable | 2024-02-14 | 161100 | positive | approval-to-commercialization bridge worked |
| R7L98_C23_CELLTRION_2024_STAGE2_FALSE_POSITIVE_BIOSIMILAR_COMMERCIALIZATION_WATCH | 068270 | Stage2-Actionable | 2024-03-29 | 191200 | counterexample | biosimilar commercialization false Stage2 |
| R7L98_C23_HLBLIFESCI_2024_STAGE4B_ONCOLOGY_APPROVAL_COMMERCIALIZATION_EVENT_CAP | 067630 | Stage4B | 2024-03-25 | 24300 | counterexample/4B | oncology approval/commercialization event cap |

## 12. Trigger-Level OHLC Backtest Tables

| trigger_id | entry | MFE30 | MAE30 | MFE90 | MAE90 | MFE180 | MAE180 | peak_date | peak_price | drawdown_after_peak |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| R7L98_C23_HUGEL_2024_STAGE2_ACTIONABLE_BOTULINUM_TOXIN_FDA_APPROVAL_COMMERCIALIZATION_BRIDGE | 161100 | 35.94 | -3.72 | 62.94 | -3.72 | 62.94 | -3.72 | 2024-06-11 | 262500 | -18.10 |
| R7L98_C23_CELLTRION_2024_STAGE2_FALSE_POSITIVE_BIOSIMILAR_COMMERCIALIZATION_WATCH | 191200 | 3.03 | -7.90 | 3.03 | -9.26 | 3.03 | -9.26 | 2024-05-07 | 197000 | -11.93 |
| R7L98_C23_HLBLIFESCI_2024_STAGE4B_ONCOLOGY_APPROVAL_COMMERCIALIZATION_EVENT_CAP | 24300 | 2.88 | -34.57 | 2.88 | -62.55 | 2.88 | -62.55 | 2024-03-26 | 25000 | -63.60 |

## 13. Current Calibrated Profile Stress Test

| axis | outcome |
|---|---|
| stage2_required_bridge | strengthen: C23 Stage2 needs approval-to-launch / channel access / pricing / repeat demand / sales conversion / margin / revision bridge |
| approval_commercialization_guardrail | strengthen: approval label alone cannot promote positive stage |
| local_4b_watch_guard | strengthen: bridge-missing biosimilar and oncology approval premiums should route to 4B watch |
| high_MAE_guardrail | strengthen: high-MAE C23 rows cannot promote without durable sales/margin bridge |
| hard_4c_thesis_break_routes_to_4c | keep |
| full_4b_requires_non_price_evidence | keep |
| price_only_blowoff_blocks_positive_stage | keep |

## 14. Stage2 / Yellow / Green / 4B Comparison

No confirmed Stage3-Green row is introduced. The useful split is whether approval becomes launch, channel, sales and margin evidence.

| symbol | stage quality | explanation |
|---|---|---|
| 145020 | good_stage2_with_later_watch | Approval/commercialization bridge produced strong MFE and shallow MAE, but later valuation watch remains necessary. |
| 068270 | bad_stage2 | Biosimilar commercialization watch lacked sales/channel/margin bridge and produced low MFE. |
| 067630 | good_4B | Oncology approval/commercialization event premium peaked immediately and later drew down deeply. |

```text
green_lateness_ratio = not_applicable
reason = no confirmed Stage3-Green trigger
```

## 15. 4B Local vs Full-window Timing Audit

| trigger | local proximity | full-window proximity | timing verdict |
|---|---:|---:|---|
| 068270 biosimilar commercialization false Stage2 | 0.97 | 0.97 | false Stage2 due missing sales / channel / pricing / margin bridge |
| 067630 oncology approval event cap | 0.97 | 0.97 | good full-window 4B timing after approval/commercialization event premium |
| 145020 approval commercialization bridge | n/a | n/a | positive Stage2, but later approval-commercialization valuation watch required |

## 16. 4C Protection Audit

```text
4C_case_count = 0
four_c_protection_label = thesis_break_watch_only for 068270 / 067630
```

No hard 4C candidate is introduced in this C23 file. The counterexamples are bridge-missing / event-cap rows, not confirmed thesis-break rows.

## 17. Sector-Specific Rule Candidate

```text
sector_specific_rule_candidate = true
rule_scope = sector_specific
rule = In L7 regulatory approval commercialization cases, Stage2 requires verified approval-to-launch conversion, channel/formulary access, pricing/mix, repeat demand, sales conversion, margin and revision bridge. Approval, FDA, biosimilar, oncology, commercialization or relative-strength label alone remains watch/4B.
proposal_status = shadow_only
```

## 18. Canonical-Archetype Rule Candidate

```text
canonical_archetype_rule_candidate = true
canonical_archetype_id = C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION
rule = C23 should split true approval-to-launch/channel/margin positives from biosimilar false Stage2 and approval event-cap rows. Event-cap rows are 4B overlay/risk calibration, not Stage3-Green promotion evidence.
proposal_status = shadow_only_not_production
```

## 19. Before / After Backtest Comparison

| profile | hypothesis | eligible triggers | avg_MFE90 | avg_MAE90 | false_positive_or_guardrail_rate | verdict |
|---|---|---:|---:|---:|---:|---|
| P0 e2r_2_2_rolling_calibrated_proxy | current profile | 3 | 22.95 | -25.18 | 0.67 | mixed; C23 approval-to-sales bridge split needed |
| P0b e2r_2_1_stock_web_calibrated_reference | older calibrated baseline | 3 | 22.95 | -25.18 | 0.67 | weaker C23 bridge split |
| P1 sector_specific_candidate_profile | L7 approval-to-launch margin bridge required | 2 | 32.99 | -6.49 | 0.50 | better |
| P2 canonical_archetype_candidate_profile | C23 bridge vs event-cap split | 2 | 32.99 | -6.49 | 0.50 | best explanatory fit |
| P3 counterexample_guard_profile | reject bridge-missing approval themes as positive | 1 | 62.94 | -3.72 | 0.00 | safest but source-proxy blockers remain |

## 20. Score-Return Alignment Matrix

| trigger | score before | stage before | score after | stage after | MFE90 | MAE90 | alignment |
|---|---:|---|---:|---|---:|---:|---|
| 145020 approval bridge | 66 | Stage2-Watch | 81 | Stage2-Actionable | 62.94 | -3.72 | approval_commercialization_positive |
| 068270 biosimilar false | 66 | Stage2-Actionable | 52 | Stage1/Watch | 3.03 | -9.26 | biosimilar_approval_false_stage2 |
| 067630 approval event cap | 70 | Stage3-Yellow-like | 54 | Stage4B-watch | 2.88 | -62.55 | approval_event_cap_4B_guard |

## 21. Coverage Matrix

```jsonl
{"row_type": "coverage_matrix", "large_sector_id": "L7_BIO_HEALTHCARE_MEDICAL", "canonical_archetype_id": "C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION", "fine_archetype_id": "BOTULINUM_TOXIN_FDA_APPROVAL_COMMERCIALIZATION_BRIDGE_VS_BIOSIMILAR_COMMERCIALIZATION_FALSE_STAGE2_AND_ONCOLOGY_APPROVAL_EVENT_CAP", "positive_case_count": 1, "counterexample_count": 2, "4B_case_count": 1, "4C_case_count": 0, "new_independent_case_count": 3, "reused_case_count": 0, "calibration_usable_trigger_count": 3, "representative_trigger_count": 2, "current_profile_error_count": 2, "sector_rule_candidate": true, "canonical_rule_candidate": true, "coverage_gap_after_this_loop": "C23 is the next unsupplemented Priority 0 archetype after local C08/C09/C01/C07/C06/C10/C14/C11/C02/C13/C19/C27/C12/C24/C28/C17 supplementation. This run adds Hugel, Celltrion, and HLB Life Science while avoiding the immediately preceding C24 and C28 outputs and avoiding the C17 duplicate generated and discarded during this run."}
```

## 22. Residual Contribution Summary

```text
new_independent_case_count: 3
reused_case_count: 0
reused_case_ids: []
new_symbol_count: 3
new_canonical_archetype_count: 0
new_fine_archetype_count: 1
new_trigger_family_count: 3
tested_existing_calibrated_axes: stage2_required_bridge, local_4b_watch_guard, approval_commercialization_guardrail, high_MAE_guardrail, hard_4c_thesis_break_routes_to_4c, full_4b_requires_non_price_evidence, price_only_blowoff_blocks_positive_stage
residual_error_types_found: approval_commercialization_positive, biosimilar_approval_false_stage2, approval_event_cap_4B
new_axis_proposed: null
existing_axis_strengthened: stage2_required_bridge, local_4b_watch_guard, approval_commercialization_guardrail, high_MAE_guardrail
existing_axis_weakened: null
existing_axis_kept: full_4b_requires_non_price_evidence, price_only_blowoff_blocks_positive_stage, hard_4c_thesis_break_routes_to_4c
sector_specific_rule_candidate: true
canonical_archetype_rule_candidate: true
no_new_signal_reason: null
loop_contribution_label: canonical_archetype_rule_candidate
do_not_propose_new_weight_delta: true
```

## 23. Validation Scope / Non-Validation Scope

Validation scope:

```text
- Stock-web tradable raw OHLC path
- entry_date / entry_price
- MFE/MAE 30D/90D/180D
- corporate-action window cleanliness
- C23 bio regulatory approval commercialization bridge vs false Stage2 / event-cap split
```

Non-validation scope:

```text
- Exact as-of evidence URLs remain pending for all selected cases.
- No production scoring update.
- No live candidate scan.
- No investment recommendation.
```

## 24. Shadow Weight Calibration

```csv
row_type,axis,scope,large_sector_id,canonical_archetype_id,baseline_value,tested_value,delta,reason,backtest_effect,trigger_ids,calibration_usable_count,new_independent_case_count,counterexample_count,confidence,proposal_type,notes
shadow_weight,stage2_required_bridge,canonical_archetype,L7_BIO_HEALTHCARE_MEDICAL,C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION,configured,C23_requires_approval_launch_channel_sales_margin_revision_bridge,0,"C23 Stage2 should require approval-to-launch conversion, channel/formulary access, pricing/mix, repeat demand, commercialization margin, and revision bridge, not regulatory approval label alone","Hugel positive worked; Celltrion and HLB Life Science event/watch rows failed positive-stage promotion","R7L98_C23_HUGEL_2024_STAGE2_ACTIONABLE_BOTULINUM_TOXIN_FDA_APPROVAL_COMMERCIALIZATION_BRIDGE|R7L98_C23_CELLTRION_2024_STAGE2_FALSE_POSITIVE_BIOSIMILAR_COMMERCIALIZATION_WATCH|R7L98_C23_HLBLIFESCI_2024_STAGE4B_ONCOLOGY_APPROVAL_COMMERCIALIZATION_EVENT_CAP",3,3,2,low,canonical_shadow_only,"do_not_propose_new_weight_delta=true because source-proxy/evidence-url-pending rows remain"
shadow_weight,local_4b_watch_guard,canonical_archetype,L7_BIO_HEALTHCARE_MEDICAL,C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION,configured,cap_bridge_missing_biosimilar_and_oncology_approval_event_premiums_as_4B_watch,0,"Approval and commercialization premiums can peak before channel access, sales conversion, pricing, launch readiness and margin bridge is proven","Celltrion had low MFE after biosimilar/commercialization watch; HLB Life Science showed 4B event-cap behavior after March oncology approval/commercialization premium","R7L98_C23_CELLTRION_2024_STAGE2_FALSE_POSITIVE_BIOSIMILAR_COMMERCIALIZATION_WATCH|R7L98_C23_HLBLIFESCI_2024_STAGE4B_ONCOLOGY_APPROVAL_COMMERCIALIZATION_EVENT_CAP",2,2,2,medium,guardrail_shadow_only,"4B overlay only; not production"
shadow_weight,high_MAE_guardrail,canonical_archetype,L7_BIO_HEALTHCARE_MEDICAL,C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION,configured,block_positive_stage_when_approval_theme_has_high_or_persistent_MAE_without_sales_margin_bridge,0,"High or persistent MAE after bridge-missing C23 entries should block Stage2/Stage3 promotion unless launch, sales conversion and margin evidence survives","Celltrion remained low-MFE and HLB Life Science MAE90=-62.55","R7L98_C23_CELLTRION_2024_STAGE2_FALSE_POSITIVE_BIOSIMILAR_COMMERCIALIZATION_WATCH|R7L98_C23_HLBLIFESCI_2024_STAGE4B_ONCOLOGY_APPROVAL_COMMERCIALIZATION_EVENT_CAP",2,2,2,medium,guardrail_shadow_only,"canonical shadow profile only"
```

## 25. Machine-Readable Rows

### 25.1 price_source_validation

```jsonl
{"row_type": "price_source_validation", "source": "Songdaiki/stock-web", "source_url": "https://github.com/Songdaiki/stock-web", "manifest_path": "atlas/manifest.json", "schema_path": "atlas/schema.json", "universe_path": "atlas/universe/all_symbols.csv", "manifest_max_date": "2026-02-20", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "raw_shard_root": "atlas/ohlcv_raw_by_symbol_year", "validation_status": "usable_for_historical_calibration", "source_name": "FinanceData/marcap", "tradable_row_count": 14354401, "raw_row_count": 15214118, "symbol_count": 5414, "active_like_symbol_count": 2868, "inactive_or_delisted_like_symbol_count": 2546}
```

### 25.2 case rows

```jsonl
{"row_type": "case", "case_id": "R7L98_C23_HUGEL_2024_BOTULINUM_TOXIN_FDA_APPROVAL_COMMERCIALIZATION_BRIDGE_POSITIVE", "symbol": "145020", "company_name": "휴젤", "round": "R7", "loop": "98", "large_sector_id": "L7_BIO_HEALTHCARE_MEDICAL", "canonical_archetype_id": "C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION", "fine_archetype_id": "BOTULINUM_TOXIN_FDA_APPROVAL_COMMERCIALIZATION_BRIDGE_VS_BIOSIMILAR_COMMERCIALIZATION_FALSE_STAGE2_AND_ONCOLOGY_APPROVAL_EVENT_CAP", "case_type": "structural_success_with_later_approval_commercialization_valuation_watch", "positive_or_counterexample": "positive", "best_trigger": "R7L98_C23_HUGEL_2024_STAGE2_ACTIONABLE_BOTULINUM_TOXIN_FDA_APPROVAL_COMMERCIALIZATION_BRIDGE", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "Botulinum-toxin FDA approval / commercialization bridge produced strong 30D/90D/180D MFE with shallow early MAE. C23 works when regulatory approval is tied to US launch path, distributor/channel quality, reimbursement/pricing, repeat procedure demand, margin and revision bridge.", "current_profile_verdict": "current_profile_kept_but_C23_positive_requires_approval_launch_channel_pricing_margin_revision_bridge_not_approval_label_only", "price_source": "Songdaiki/stock-web", "notes": "Selected 2024 window clean after old 2017/2020 corporate-action candidates. Source-proxy only, so no production weight delta."}
{"row_type": "case", "case_id": "R7L98_C23_CELLTRION_2024_BIOSIMILAR_COMMERCIALIZATION_FALSE_STAGE2", "symbol": "068270", "company_name": "셀트리온", "round": "R7", "loop": "98", "large_sector_id": "L7_BIO_HEALTHCARE_MEDICAL", "canonical_archetype_id": "C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION", "fine_archetype_id": "BOTULINUM_TOXIN_FDA_APPROVAL_COMMERCIALIZATION_BRIDGE_VS_BIOSIMILAR_COMMERCIALIZATION_FALSE_STAGE2_AND_ONCOLOGY_APPROVAL_EVENT_CAP", "case_type": "failed_rerating_biosimilar_approval_commercialization_bridge_missing", "positive_or_counterexample": "counterexample", "best_trigger": "R7L98_C23_CELLTRION_2024_STAGE2_FALSE_POSITIVE_BIOSIMILAR_COMMERCIALIZATION_WATCH", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "Biosimilar approval/commercialization watch after the late-March rebound had low forward MFE and persistent MAE. C23 Stage2 should not be awarded without approval-to-sales conversion, formulary/channel access, price/mix, inventory, margin and revision bridge.", "current_profile_verdict": "current_profile_false_positive_if_biosimilar_approval_watch_counts_without_sales_channel_pricing_margin_revision_bridge", "price_source": "Songdaiki/stock-web", "notes": "Entry selected after 2024-01-12 corporate-action candidate boundary. Source-proxy only."}
{"row_type": "case", "case_id": "R7L98_C23_HLBLIFESCI_2024_ONCOLOGY_APPROVAL_COMMERCIALIZATION_EVENT_CAP_4B", "symbol": "067630", "company_name": "HLB생명과학", "round": "R7", "loop": "98", "large_sector_id": "L7_BIO_HEALTHCARE_MEDICAL", "canonical_archetype_id": "C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION", "fine_archetype_id": "BOTULINUM_TOXIN_FDA_APPROVAL_COMMERCIALIZATION_BRIDGE_VS_BIOSIMILAR_COMMERCIALIZATION_FALSE_STAGE2_AND_ONCOLOGY_APPROVAL_EVENT_CAP", "case_type": "event_cap_4b_counterexample", "positive_or_counterexample": "counterexample", "best_trigger": "R7L98_C23_HLBLIFESCI_2024_STAGE4B_ONCOLOGY_APPROVAL_COMMERCIALIZATION_EVENT_CAP", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "Oncology approval/commercialization event premium capped after the March spike and then de-rated sharply. C23 should route bridge-missing regulatory commercialization premiums to 4B unless approval path, launch readiness, partner/distribution, financing runway, sales conversion, margin and revision bridge remain visible.", "current_profile_verdict": "current_profile_4B_too_late_if_approval_commercialization_event_premium_not_capped", "price_source": "Songdaiki/stock-web", "notes": "Selected 2024 window clean after old 2013/2015/2018/2019/2021 corporate-action candidates. Source-proxy only."}
```

### 25.3 trigger rows

```jsonl
{"row_type": "trigger", "trigger_id": "R7L98_C23_HUGEL_2024_STAGE2_ACTIONABLE_BOTULINUM_TOXIN_FDA_APPROVAL_COMMERCIALIZATION_BRIDGE", "case_id": "R7L98_C23_HUGEL_2024_BOTULINUM_TOXIN_FDA_APPROVAL_COMMERCIALIZATION_BRIDGE_POSITIVE", "symbol": "145020", "company_name": "휴젤", "round": "R7", "loop": "98", "large_sector_id": "L7_BIO_HEALTHCARE_MEDICAL", "canonical_archetype_id": "C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION", "fine_archetype_id": "BOTULINUM_TOXIN_FDA_APPROVAL_COMMERCIALIZATION_BRIDGE_VS_BIOSIMILAR_COMMERCIALIZATION_FALSE_STAGE2_AND_ONCOLOGY_APPROVAL_EVENT_CAP", "sector": "botulinum_toxin_FDA_approval_US_launch_commercialization", "primary_archetype": "approval_launch_channel_pricing_margin_revision_bridge", "loop_objective": "coverage_gap_fill | counterexample_mining | stage2_actionable_bonus_stress_test | 4B_4C_guardrail_stress_test | approval_commercialization_guardrail | high_MAE_guardrail | canonical_archetype_compression", "trigger_type": "Stage2-Actionable", "trigger_date": "2024-02-14", "entry_date": "2024-02-14", "entry_price": 161100.0, "evidence_available_at_that_date": "botulinum-toxin FDA approval / US launch path / distributor-channel and pricing/margin revision bridge proxy before March approval rerating; exact as-of source URL pending", "evidence_source": "source_proxy_historical_public_report_proxy", "stage2_evidence_fields": ["regulatory_approval_proxy", "US_launch_path_proxy", "channel_partner_proxy", "pricing_margin_proxy", "revision_bridge_proxy"], "stage3_evidence_fields": ["strong_MFE30", "very_strong_MFE90", "shallow_MAE90"], "stage4b_evidence_fields": ["later_approval_commercialization_valuation_watch", "post_peak_recheck"], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/145/145020/2024.csv", "profile_path": "atlas/symbol_profiles/145/145020.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": 35.94, "MFE_90D_pct": 62.94, "MFE_180D_pct": 62.94, "MFE_1Y_pct": "not_calculated", "MFE_2Y_pct": "not_calculated", "MAE_30D_pct": -3.72, "MAE_90D_pct": -3.72, "MAE_180D_pct": -3.72, "MAE_1Y_pct": "not_calculated", "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2024-06-11", "peak_price": 262500.0, "drawdown_after_peak_pct": -18.1, "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": null, "four_b_full_window_peak_proximity": null, "four_b_timing_verdict": "positive_stage2_but_later_regulatory_approval_commercialization_valuation_4B_watch_needed", "four_b_evidence_type": ["approval_commercialization_bridge", "US_launch_channel", "valuation_watch"], "four_c_protection_label": "not_applicable", "trigger_outcome_label": "good_stage2_regulatory_approval_commercialization_bridge_success", "current_profile_verdict": "current_profile_kept_but_source_proxy_blocks_positive_delta", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window_after_old_2017_2020_CA", "same_entry_group_id": "R7L98_C23_145020_2024-02-14_161100", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false, "evidence_url_pending": true, "source_proxy_only": true}
{"row_type": "trigger", "trigger_id": "R7L98_C23_CELLTRION_2024_STAGE2_FALSE_POSITIVE_BIOSIMILAR_COMMERCIALIZATION_WATCH", "case_id": "R7L98_C23_CELLTRION_2024_BIOSIMILAR_COMMERCIALIZATION_FALSE_STAGE2", "symbol": "068270", "company_name": "셀트리온", "round": "R7", "loop": "98", "large_sector_id": "L7_BIO_HEALTHCARE_MEDICAL", "canonical_archetype_id": "C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION", "fine_archetype_id": "BOTULINUM_TOXIN_FDA_APPROVAL_COMMERCIALIZATION_BRIDGE_VS_BIOSIMILAR_COMMERCIALIZATION_FALSE_STAGE2_AND_ONCOLOGY_APPROVAL_EVENT_CAP", "sector": "biosimilar_approval_commercialization_sales_channel_watch", "primary_archetype": "biosimilar_approval_watch_without_sales_channel_pricing_margin_revision_bridge", "loop_objective": "coverage_gap_fill | counterexample_mining | stage2_actionable_bonus_stress_test | 4B_4C_guardrail_stress_test | approval_commercialization_guardrail | high_MAE_guardrail | canonical_archetype_compression", "trigger_type": "Stage2-Actionable", "trigger_date": "2024-03-29", "entry_date": "2024-03-29", "entry_price": 191200.0, "evidence_available_at_that_date": "biosimilar approval/commercialization recovery watch without confirmed approval-to-sales conversion, formulary/channel access, pricing/mix, inventory or margin revision bridge; exact as-of source URL pending", "evidence_source": "source_proxy_historical_public_news_proxy", "stage2_evidence_fields": ["biosimilar_approval_watch", "commercialization_theme", "relative_strength_rebound"], "stage3_evidence_fields": [], "stage4b_evidence_fields": ["low_MFE90", "persistent_MAE90", "sales_channel_pricing_margin_bridge_missing"], "stage4c_evidence_fields": ["thesis_break_watch_only"], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/068/068270/2024.csv", "profile_path": "atlas/symbol_profiles/068/068270.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": 3.03, "MFE_90D_pct": 3.03, "MFE_180D_pct": 3.03, "MFE_1Y_pct": "not_calculated", "MFE_2Y_pct": "not_calculated", "MAE_30D_pct": -7.9, "MAE_90D_pct": -9.26, "MAE_180D_pct": -9.26, "MAE_1Y_pct": "not_calculated", "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2024-05-07", "peak_price": 197000.0, "drawdown_after_peak_pct": -11.93, "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": 0.97, "four_b_full_window_peak_proximity": 0.97, "four_b_timing_verdict": "biosimilar_commercialization_watch_was_false_stage2_due_missing_sales_channel_pricing_margin_revision_bridge", "four_b_evidence_type": ["biosimilar_approval_premium", "bridge_missing", "low_MFE"], "four_c_protection_label": "thesis_break_watch_only", "trigger_outcome_label": "bad_stage2_biosimilar_commercialization_watch_without_sales_margin_bridge", "current_profile_verdict": "current_profile_false_positive_if_biosimilar_approval_watch_counts_without_sales_channel_pricing_margin_revision_bridge", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "post_2024-01-12_CA_boundary_clean_180D_window", "same_entry_group_id": "R7L98_C23_068270_2024-03-29_191200", "dedupe_for_aggregate": true, "aggregate_group_role": "representative_false_stage2", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false, "evidence_url_pending": true, "source_proxy_only": true}
{"row_type": "trigger", "trigger_id": "R7L98_C23_HLBLIFESCI_2024_STAGE4B_ONCOLOGY_APPROVAL_COMMERCIALIZATION_EVENT_CAP", "case_id": "R7L98_C23_HLBLIFESCI_2024_ONCOLOGY_APPROVAL_COMMERCIALIZATION_EVENT_CAP_4B", "symbol": "067630", "company_name": "HLB생명과학", "round": "R7", "loop": "98", "large_sector_id": "L7_BIO_HEALTHCARE_MEDICAL", "canonical_archetype_id": "C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION", "fine_archetype_id": "BOTULINUM_TOXIN_FDA_APPROVAL_COMMERCIALIZATION_BRIDGE_VS_BIOSIMILAR_COMMERCIALIZATION_FALSE_STAGE2_AND_ONCOLOGY_APPROVAL_EVENT_CAP", "sector": "oncology_approval_commercialization_event_premium", "primary_archetype": "approval_commercialization_event_cap_4B", "loop_objective": "coverage_gap_fill | counterexample_mining | stage2_actionable_bonus_stress_test | 4B_4C_guardrail_stress_test | approval_commercialization_guardrail | high_MAE_guardrail | canonical_archetype_compression", "trigger_type": "Stage4B", "trigger_date": "2024-03-25", "entry_date": "2024-03-25", "entry_price": 24300.0, "evidence_available_at_that_date": "oncology approval/commercialization event premium without confirmed approval path durability, launch readiness, partner/distribution, funding runway, sales conversion or margin bridge; exact as-of source URL pending", "evidence_source": "source_proxy_historical_public_news_proxy", "stage2_evidence_fields": ["oncology_approval_event", "commercialization_theme", "relative_strength_spike"], "stage3_evidence_fields": [], "stage4b_evidence_fields": ["event_premium_cap", "low_MFE90", "deep_MAE90", "approval_launch_margin_bridge_missing"], "stage4c_evidence_fields": ["thesis_break_watch_only"], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/067/067630/2024.csv", "profile_path": "atlas/symbol_profiles/067/067630.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": 2.88, "MFE_90D_pct": 2.88, "MFE_180D_pct": 2.88, "MFE_1Y_pct": "not_calculated", "MFE_2Y_pct": "not_calculated", "MAE_30D_pct": -34.57, "MAE_90D_pct": -62.55, "MAE_180D_pct": -62.55, "MAE_1Y_pct": "not_calculated", "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2024-03-26", "peak_price": 25000.0, "drawdown_after_peak_pct": -63.6, "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": 0.97, "four_b_full_window_peak_proximity": 0.97, "four_b_timing_verdict": "good_full_window_4B_timing_oncology_approval_commercialization_event_cap_due_missing_launch_sales_margin_bridge", "four_b_evidence_type": ["approval_commercialization_event_premium", "positioning_overheat", "bridge_missing"], "four_c_protection_label": "thesis_break_watch_only", "trigger_outcome_label": "event_cap_4B_success_approval_commercialization_event_premium", "current_profile_verdict": "current_profile_4B_too_late_if_approval_commercialization_event_premium_not_capped", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window_after_old_2013_2015_2018_2019_2021_CA", "same_entry_group_id": "R7L98_C23_067630_2024-03-25_24300", "dedupe_for_aggregate": false, "aggregate_group_role": "4B_overlay_only", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false, "evidence_url_pending": true, "source_proxy_only": true}
```

### 25.4 score_simulation rows

```jsonl
{"row_type": "score_simulation", "profile_id": "e2r_2_2_rolling_calibrated_proxy", "case_id": "R7L98_C23_HUGEL_2024_BOTULINUM_TOXIN_FDA_APPROVAL_COMMERCIALIZATION_BRIDGE_POSITIVE", "trigger_id": "R7L98_C23_HUGEL_2024_STAGE2_ACTIONABLE_BOTULINUM_TOXIN_FDA_APPROVAL_COMMERCIALIZATION_BRIDGE", "symbol": "145020", "large_sector_id": "L7_BIO_HEALTHCARE_MEDICAL", "canonical_archetype_id": "C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION", "raw_component_scores_before": {"contract_score": 25, "backlog_visibility_score": 35, "margin_bridge_score": 35, "revision_score": 35, "relative_strength_score": 60, "customer_quality_score": 45, "policy_or_regulatory_score": 55, "valuation_repricing_score": 55, "execution_risk_score": 55, "legal_or_contract_risk_score": 30, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_before": 66, "stage_label_before": "Stage2-Watch", "raw_component_scores_after": {"contract_score": 55, "backlog_visibility_score": 60, "margin_bridge_score": 65, "revision_score": 60, "relative_strength_score": 80, "customer_quality_score": 60, "policy_or_regulatory_score": 70, "valuation_repricing_score": 45, "execution_risk_score": 35, "legal_or_contract_risk_score": 20, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_after": 81, "stage_label_after": "Stage2-Actionable", "changed_components": ["contract_score", "backlog_visibility_score", "margin_bridge_score", "revision_score", "relative_strength_score", "customer_quality_score", "policy_or_regulatory_score", "execution_risk_score"], "component_delta_explanation": "botulinum_toxin_FDA_approval_commercialization_positive", "MFE_90D_pct": 62.94, "MAE_90D_pct": -3.72, "score_return_alignment_label": "approval_commercialization_positive", "current_profile_verdict": "current_profile_kept_but_source_proxy_blocks_positive_delta"}
{"row_type": "score_simulation", "profile_id": "e2r_2_2_rolling_calibrated_proxy", "case_id": "R7L98_C23_CELLTRION_2024_BIOSIMILAR_COMMERCIALIZATION_FALSE_STAGE2", "trigger_id": "R7L98_C23_CELLTRION_2024_STAGE2_FALSE_POSITIVE_BIOSIMILAR_COMMERCIALIZATION_WATCH", "symbol": "068270", "large_sector_id": "L7_BIO_HEALTHCARE_MEDICAL", "canonical_archetype_id": "C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION", "raw_component_scores_before": {"contract_score": 20, "backlog_visibility_score": 30, "margin_bridge_score": 25, "revision_score": 25, "relative_strength_score": 60, "customer_quality_score": 40, "policy_or_regulatory_score": 55, "valuation_repricing_score": 55, "execution_risk_score": 55, "legal_or_contract_risk_score": 30, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 5}, "weighted_score_before": 66, "stage_label_before": "Stage2-Actionable", "raw_component_scores_after": {"contract_score": 5, "backlog_visibility_score": 5, "margin_bridge_score": 5, "revision_score": 5, "relative_strength_score": 20, "customer_quality_score": 15, "policy_or_regulatory_score": 25, "valuation_repricing_score": 25, "execution_risk_score": 75, "legal_or_contract_risk_score": 45, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 10}, "weighted_score_after": 52, "stage_label_after": "Stage1/Watch", "changed_components": ["backlog_visibility_score", "margin_bridge_score", "revision_score", "relative_strength_score", "policy_or_regulatory_score", "valuation_repricing_score", "execution_risk_score"], "component_delta_explanation": "biosimilar_commercialization_false_stage2", "MFE_90D_pct": 3.03, "MAE_90D_pct": -9.26, "score_return_alignment_label": "biosimilar_approval_false_stage2", "current_profile_verdict": "current_profile_false_positive_if_biosimilar_approval_watch_counts_without_sales_channel_pricing_margin_revision_bridge"}
{"row_type": "score_simulation", "profile_id": "e2r_2_2_rolling_calibrated_proxy", "case_id": "R7L98_C23_HLBLIFESCI_2024_ONCOLOGY_APPROVAL_COMMERCIALIZATION_EVENT_CAP_4B", "trigger_id": "R7L98_C23_HLBLIFESCI_2024_STAGE4B_ONCOLOGY_APPROVAL_COMMERCIALIZATION_EVENT_CAP", "symbol": "067630", "large_sector_id": "L7_BIO_HEALTHCARE_MEDICAL", "canonical_archetype_id": "C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION", "raw_component_scores_before": {"contract_score": 15, "backlog_visibility_score": 20, "margin_bridge_score": 20, "revision_score": 20, "relative_strength_score": 75, "customer_quality_score": 25, "policy_or_regulatory_score": 60, "valuation_repricing_score": 65, "execution_risk_score": 75, "legal_or_contract_risk_score": 55, "dilution_cb_risk_score": 5, "accounting_trust_risk_score": 5}, "weighted_score_before": 70, "stage_label_before": "Stage3-Yellow-like", "raw_component_scores_after": {"contract_score": 5, "backlog_visibility_score": 5, "margin_bridge_score": 0, "revision_score": 5, "relative_strength_score": 20, "customer_quality_score": 5, "policy_or_regulatory_score": 15, "valuation_repricing_score": 25, "execution_risk_score": 95, "legal_or_contract_risk_score": 70, "dilution_cb_risk_score": 10, "accounting_trust_risk_score": 10}, "weighted_score_after": 54, "stage_label_after": "Stage4B-watch", "changed_components": ["backlog_visibility_score", "margin_bridge_score", "revision_score", "relative_strength_score", "policy_or_regulatory_score", "valuation_repricing_score", "execution_risk_score", "legal_or_contract_risk_score"], "component_delta_explanation": "oncology_approval_event_cap_4B_guard", "MFE_90D_pct": 2.88, "MAE_90D_pct": -62.55, "score_return_alignment_label": "approval_event_cap_4B_guard", "current_profile_verdict": "current_profile_4B_too_late_if_approval_commercialization_event_premium_not_capped"}
```

### 25.5 residual_contribution row

```jsonl
{"row_type": "residual_contribution", "round": "R7", "loop": "98", "large_sector_id": "L7_BIO_HEALTHCARE_MEDICAL", "canonical_archetype_id": "C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION", "fine_archetype_id": "BOTULINUM_TOXIN_FDA_APPROVAL_COMMERCIALIZATION_BRIDGE_VS_BIOSIMILAR_COMMERCIALIZATION_FALSE_STAGE2_AND_ONCOLOGY_APPROVAL_EVENT_CAP", "new_independent_case_count": 3, "reused_case_count": 0, "new_symbol_count": 3, "same_archetype_new_symbol_count": 3, "same_archetype_new_trigger_family_count": 3, "new_trigger_family_count": 3, "positive_case_count": 1, "counterexample_count": 2, "4B_case_count": 1, "4C_case_count": 0, "tested_existing_calibrated_axes": ["stage2_required_bridge", "local_4b_watch_guard", "approval_commercialization_guardrail", "full_4b_requires_non_price_evidence", "price_only_blowoff_blocks_positive_stage", "high_MAE_guardrail"], "residual_error_types_found": ["approval_commercialization_positive", "biosimilar_approval_false_stage2", "approval_event_cap_4B"], "loop_contribution_label": "canonical_archetype_rule_candidate", "do_not_propose_new_weight_delta": true, "source_proxy_only_count": 3, "evidence_url_pending_count": 3}
```

### 25.6 narrative_only row

```jsonl
{"row_type":"narrative_only","case_id":"none","symbol":"none","large_sector_id":"L7_BIO_HEALTHCARE_MEDICAL","canonical_archetype_id":"C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION","reason":"all selected rows have usable 180D stock-web windows; no narrative-only price row required","price_source":"Songdaiki/stock-web","usage":"not_weight_calibration"}
```

## 26. Deferred Coding Agent Handoff Prompt

### Purpose

You are now in the repository implementation phase. The attached Markdown files are v12 post-calibrated residual research outputs produced using the Songdaiki/stock-web OHLC atlas.

These MDs are not live candidate research. They are historical calibration research designed to extend the already-applied calibrated profile.

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
- Do not apply global deltas unless multiple large_sector_id values support the same direction.
- Positive score promotion requires non-price evidence and clean 180D MFE/MAE.
- 4B rows are overlay/risk calibration only.
- 4C rows are thesis-break/protection calibration only.
- False-positive rows should strengthen bridge requirements, not generate positive promotion.
- C23 rows need explicit approval-to-launch conversion, channel/formulary access, pricing/mix, repeat demand, sales conversion, margin and revision bridge before positive promotion.
- In C23, bridge-missing regulatory approval/commercialization rows with low MFE or high/persistent MAE should route to 4B/watch, not Stage3.
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
10. Add tests that bridge-missing C23 bio regulatory approval commercialization rows cannot promote positive stages.

### Expected output

- Concise implementation summary.
- Rows accepted/rejected.
- New sector/canonical archetype coverage.
- Existing axis strengthened/weakened/kept.
- No investment recommendation language.

## 27. Next Selection State

```text
completed_round = R7
completed_loop = 98
completed_canonical_archetype_id = C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION
coverage_scheduler_status = coverage_index_first
next_selection_rule = re-read V12_Research_No_Repeat_Index.md Priority 0 and local supplements
round_schedule_status = valid
round_sector_consistency = pass
```

## 28. Source Notes

- Main execution prompt: Songdaiki/stock_agent docs/core/e2r_v12_prompt_round_scheduler_corrected.txt.
- No-repeat index: Songdaiki/stock_agent docs/core/V12_Research_No_Repeat_Index.md.
- Price atlas: Songdaiki/stock-web atlas/manifest.json and per-symbol tradable shards.
- This file contains no investment recommendation and no production scoring change.
