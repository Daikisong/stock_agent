# E2R Stock-Web Historical Calibration / Sector-Archetype Residual Research Round

## 0. Research Metadata

```text
research_session = post_calibrated_sector_archetype_residual_research
mode = historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12
output_format = one_standalone_markdown_file
stock_agent_code_access_allowed = false
stock_agent_code_patch_allowed = false
stock_agent_live_scan_allowed = false
current_stock_discovery_allowed = false
production_scoring_changed = false
shadow_weight_only = true
handoff_prompt_embedded = true
handoff_prompt_executed_now = false

scheduled_round = R11
scheduled_loop = 10
completed_round = R11
completed_loop = 10
computed_next_round = R12
computed_next_loop = 10
round_schedule_status = valid
round_sector_consistency = pass

large_sector_id = L10_POLICY_EVENT_CROSS_REDTEAM_MISC
canonical_archetype_id = C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP
fine_archetype_id = CONTROL_PREMIUM_TENDER_OFFER_EVENT_CAP
```

One-line contribution:

```text
This loop adds 3 new independent cases, 1 counterexamples, and 2 residual errors for R11/L10_POLICY_EVENT_CROSS_REDTEAM_MISC/C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP.
```

## 1. Current Calibrated Profile Assumption

```text
current_default_profile_proxy = e2r_2_1_stock_web_calibrated
previous_baseline_reference = e2r_2_0_baseline

stage2_actionable_evidence_bonus = +2.0
stage3_yellow_total_min = 75.0
stage3_green_total_min = 87.0
stage3_green_revision_min = 55.0
stage3_cross_evidence_green_buffer = +1.5
price_only_blowoff_blocks_positive_stage = true
full_4b_requires_non_price_evidence = true
hard_4c_thesis_break_routes_to_4c = true
```

This MD does not re-prove the global Stage2/Green/4B rules. It stress-tests whether **C32 governance / control-premium / tender-offer events** need a shadow profile that distinguishes:

1. binding tender offer or court-backed control-premium event;
2. non-binding sale process or rumor-like event premium;
3. event cap / tender cap / dilution / legal-overhang 4B overlays.

## 2. Round / Large Sector / Canonical Archetype Scope

| Field | Value |
|---|---|
| scheduled_round | R11 |
| scheduled_loop | 10 |
| large_sector_id | L10_POLICY_EVENT_CROSS_REDTEAM_MISC |
| canonical_archetype_id | C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP |
| fine_archetype_id | CONTROL_PREMIUM_TENDER_OFFER_EVENT_CAP |
| loop_objective | coverage_gap_fill / sector_specific_rule_discovery / canonical_archetype_compression / 4B_non_price_requirement_stress_test / 4C_thesis_break_timing_test / counterexample_mining |
| next_round | R12 |
| next_loop | 10 |

Round-sector gate:

```text
R11 permits L10_POLICY_EVENT_CROSS_REDTEAM_MISC for policy/event/cross-redteam research.
round_sector_consistency = pass
```

## 3. Previous Coverage / Duplicate Avoidance Check

Allowed artifacts were used only for coverage and duplicate avoidance. `ingest_summary.md` reports loops 1~9 and R1~R13 coverage in the existing calibration set. The generated R10 loop 10 file from the prior step sets the next state to R11 loop 10, so this MD continues the sequential scheduler.

Duplicate avoidance result:

| Candidate | Prior exact symbol + trigger + entry family duplicate? | Decision |
|---|---:|---|
| 에스엠 041510 / 2023-02-10 HYBE-Kakao control battle | no exact duplicate found in allowed summary scope | use |
| 고려아연 010130 / 2024-09-13 Young Poong-MBK tender event | no exact duplicate found in allowed summary scope | use |
| HMM 011200 / 2023-12-18 sale preferred-bidder event | no exact duplicate found in allowed summary scope; post-2023-11-10 corporate-action candidate window checked | use with caveat |

## 4. Stock-Web OHLC Input / Price Source Validation

```text
price_data_source = Songdaiki/stock-web
source_repo_url = https://github.com/Songdaiki/stock-web
manifest_path = atlas/manifest.json
schema_path = atlas/schema.json
universe_path = atlas/universe/all_symbols.csv
stock_web_manifest_max_date = 2026-02-20
price_basis = tradable_raw
price_adjustment_status = raw_unadjusted_marcap
calibration_shard_root = atlas/ohlcv_tradable_by_symbol_year
raw_shard_root = atlas/ohlcv_raw_by_symbol_year
```

Manifest validation:

| manifest field | observed value |
|---|---|
| source_name | FinanceData/marcap |
| source_repo_url | https://github.com/FinanceData/marcap |
| price_adjustment_status | raw_unadjusted_marcap |
| min_date | 1995-05-02 |
| max_date | 2026-02-20 |
| tradable_row_count | 14354401 |
| raw_row_count | 15214118 |
| symbol_count | 5414 |
| active_like_symbol_count | 2868 |
| inactive_or_delisted_like_symbol_count | 2546 |
| markets | KONEX / KOSDAQ / KOSDAQ GLOBAL / KOSPI |

## 5. Historical Eligibility Gate

| case_id | symbol | entry_date | forward 180D available by stock-web max_date? | corporate-action overlap? | calibration_usable |
|---|---:|---:|---:|---:|---:|
| R11L10-C32-SM-20230210 | 041510 | 2023-02-10 | yes | no 180D overlap; profile candidate dates are 2002/2005 | true |
| R11L10-C32-KZ-20240913 | 010130 | 2024-09-13 | yes | no corporate-action candidates | true |
| R11L10-C32-HMM-20231218 | 011200 | 2023-12-18 | yes | profile has 2023-11-10 candidate, but entry is after that date; no entry~D+180 overlap | true |

HMM is marked with a caveat because the profile reports a 2023-11-10 corporate-action candidate. The representative event entry is 2023-12-18, after that candidate date, so the 180D calibration window is not blocked by the rule used in this prompt.

## 6. Canonical Archetype Compression Map

| fine_archetype | canonical_archetype_id | compression rationale |
|---|---|---|
| HYBE/Kakao SM tender battle | C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP | binding tender/control-premium event with explicit cap |
| Young Poong-MBK Korea Zinc hostile tender / buyback response | C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP | hostile control event + counter-tender + legal/dilution overhang |
| HMM sale preferred-bidder process and collapse | C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP | non-binding sale-process event premium with closing-certainty failure |

## 7. Case Selection Summary

| case_id | symbol | company | role | trigger family | entry | 180D MFE | 180D MAE | current profile verdict |
|---|---:|---|---|---|---:|---:|---:|---|
| R11L10-C32-SM-20230210 | 041510 | 에스엠 | positive / 4B overlay success | binding tender-control battle | 114,700 | 40.54% | -21.1% | current_profile_correct |
| R11L10-C32-KZ-20240913 | 010130 | 고려아연 | positive / 4B too late risk | hostile tender + counter tender | 666,000 | 261.41% | -3.45% | current_profile_4B_too_late |
| R11L10-C32-HMM-20231218 | 011200 | HMM | counterexample / false positive Green risk | preferred bidder but closing uncertain | 17,540 | 32.84% | -14.42% | current_profile_false_positive |

## 8. Positive vs Counterexample Balance

```text
positive_case_count = 2
counterexample_count = 1
calibration_usable_case_count = 3
calibration_usable_trigger_count = 3 representative + 2 overlay comparison rows
```

Interpretation:

- C32 can work as a fast Stage2-Actionable event archetype when there is **binding tender price / explicit control-premium mechanism / identifiable event cap**.
- C32 should not become structural Stage3-Green when the event is only a sale process, rumor, preferred-bidder designation, or headline premium without closing certainty.
- 4B must remain an overlay. Tender cap, buyback counteroffer, legal challenge, dilution/share-issuance plan, and event-price exhaustion are not “fundamental thesis breaks,” but they can end the favorable event-premium window.

## 9. Evidence Source Map

| case | event evidence at trigger | evidence source status |
|---|---|---|
| 에스엠 | HYBE control-stake acquisition and tender-offer battle; Kakao later tender offer at 150,000 won | AP / public reporting available; exact exchange filing enrichment required before production promotion |
| 고려아연 | Young Poong + MBK tender offer at 660,000 won; later court/tender/buyback/legal-overhang sequence | Reuters / public reporting available; exact local filing enrichment required |
| HMM | Harim/JKL preferred-bidder sale process; later sale process breakdown | public reporting summary available; exact Korean source enrichment required |

## 10. Price Data Source Map

| symbol | shard path | profile path | row validation |
|---:|---|---|---|
| 041510 | atlas/ohlcv_tradable_by_symbol_year/041/041510/2023.csv | atlas/symbol_profiles/041/041510.json | usable |
| 010130 | atlas/ohlcv_tradable_by_symbol_year/010/010130/2024.csv; atlas/ohlcv_tradable_by_symbol_year/010/010130/2025.csv | atlas/symbol_profiles/010/010130.json | usable |
| 011200 | atlas/ohlcv_tradable_by_symbol_year/011/011200/2023.csv; atlas/ohlcv_tradable_by_symbol_year/011/011200/2024.csv | atlas/symbol_profiles/011/011200.json | usable after 2023-11-10 caveat |

## 11. Case-by-Case Trigger Grid

| trigger_id | case_id | trigger_type | trigger_date | entry_date | entry_price | stage2 fields | stage3 fields | stage4B fields | stage4C fields |
|---|---|---|---:|---:|---:|---|---|---|---|
| R11L10-C32-SM-Stage2-20230210 | R11L10-C32-SM-20230210 | Stage2-Actionable | 2023-02-10 | 2023-02-10 | 114,700 | public_event_or_disclosure; relative_strength; control_premium_or_event_premium | multiple_public_sources; financial_visibility:not_supported | explicit_event_cap; valuation_blowoff | none |
| R11L10-C32-KZ-Stage2-20240913 | R11L10-C32-KZ-20240913 | Stage2-Actionable | 2024-09-13 | 2024-09-13 | 666,000 | public_event_or_disclosure; relative_strength; control_premium_or_event_premium | multiple_public_sources; low_red_team_risk:false | valuation_blowoff; legal_or_regulatory_block; capital_raise_or_overhang | none |
| R11L10-C32-HMM-Stage2-20231218 | R11L10-C32-HMM-20231218 | Stage2-Actionable | 2023-12-18 | 2023-12-18 | 17,540 | public_event_or_disclosure; relative_strength; control_premium_or_event_premium | financial_visibility:not_supported; low_red_team_risk:false | price_only_local_peak; legal_or_contract_risk | thesis_evidence_broken; contract_cancelled |

## 12. Trigger-Level OHLC Backtest Tables

| trigger_id | entry | MFE 30D | MAE 30D | MFE 90D | MAE 90D | MFE 180D | MAE 180D | peak_date | peak_price | drawdown_after_peak |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| SM Stage2 | 114,700 | 40.54% | -21.1% | 40.54% | -21.1% | 40.54% | -21.1% | 2023-03-08 | 161,200 | -43.86% |
| KZ Stage2 | 666,000 | 131.68% | -1.65% | 261.41% | -1.65% | 261.41% | -3.45% | 2024-12-06 | 2,407,000 | -73.29% |
| HMM Stage2 | 17,540 | 32.84% | -9.92% | 32.84% | -14.42% | 32.84% | -14.42% | 2023-12-20 | 23,300 | -35.58% |

## 13. Current Calibrated Profile Stress Test

| case | P0 judgment likely | actual return alignment | verdict |
|---|---|---|---|
| SM | Stage2/Yellow event premium, not structural Green | correct: strong but capped event premium, then drawdown | current_profile_correct |
| Korea Zinc | Stage2/Yellow quickly, but 4B may arrive late if legal/dilution/tender-cap overlays are not strong enough | price path kept running to a full-window blowoff; 4B needs event-specific cap and legal/dilution fields | current_profile_4B_too_late |
| HMM | Sale preferred-bidder event could be over-promoted to Stage3-Yellow/Green if control premium is treated as binding | MFE existed, but not durable; sale uncertainty/collapse made this a false positive for structural rerating | current_profile_false_positive |

Axis answers:

| axis | finding |
|---|---|
| Stage2 actionable bonus | useful for binding tender/control battle; excessive for non-binding sale process |
| Yellow threshold 75 | acceptable if tender binding score is high; too permissive if completion risk is ignored |
| Green threshold 87 / revision 55 | Green should generally not be used for C32 unless the event directly changes durable EPS/FCF |
| price-only blowoff guard | strengthened |
| full 4B non-price requirement | strengthened: tender cap, buyback, litigation, dilution are non-price 4B evidence |
| hard 4C routing | strengthened for failed sale / cancelled process / blocked tender |

## 14. Stage2 / Yellow / Green Comparison

| case | Stage2 entry | hypothetical Green entry | green_lateness_ratio | interpretation |
|---|---:|---:|---:|---|
| SM | 114,700 | 149,700 near Kakao tender-price phase | 0.75 | Green near most event upside; Stage2 captured event better |
| Korea Zinc | 666,000 | not used as structural Green | n/a | C32 should remain event-premium Stage2/Yellow plus 4B overlay |
| HMM | 17,540 | should be blocked | n/a | non-binding sale event is not Green evidence |

## 15. 4B Local vs Full-window Timing Audit

| case | local peak proxy | full-window peak | 4B evidence | verdict |
|---|---:|---:|---|---|
| SM | 161,200 | 161,200 | tender-price cap / event premium | good_full_window_4B_timing |
| Korea Zinc | 1,543,000 local late-Oct | 2,407,000 Dec 6 | tender battle + buyback + legal/dilution overhang | local 4B too early if price-only; full-window 4B needs non-price evidence |
| HMM | 23,300 Dec 20 | 23,300 | price-only spike + non-binding sale completion risk | price_only_local_4B_too_early unless completion risk is included |

## 16. 4C Protection Audit

| case | 4C label | protection interpretation |
|---|---|---|
| SM | thesis_break_watch_only | not hard 4C; event premium faded but business continued |
| Korea Zinc | thesis_break_watch_only | not hard 4C; event premium/legal/dilution overlay only |
| HMM | hard_4c_success | sale-process breakdown should route out of positive promotion |

## 17. Sector-Specific Rule Candidate

```text
rule_scope = sector_specific
axis = c32_control_premium_tender_binding_score
baseline_value = 0
tested_value = +1
proposal_type = sector_shadow_only
```

Rule candidate:

> In L10 policy/event/cross-redteam cases, a control-premium headline can receive Stage2-Actionable support only when the event has a binding tender price, formal offer, court/filing visibility, or explicit buyer/seller mechanism. Otherwise it should remain event-watch, not structural Stage3.

## 18. Canonical-Archetype Rule Candidate

```text
rule_scope = canonical_archetype_specific
axis_1 = c32_binding_tender_offer_control_premium_bonus
axis_2 = c32_non_binding_sale_process_completion_risk_cap
axis_3 = c32_tender_price_cap_4b_overlay
```

Canonical rule:

> C32 should be scored as a fast event-premium archetype, not an EPS rerating archetype. Positive promotion requires binding event mechanics. Full 4B requires non-price evidence such as tender cap reached, court/legal block, dilution/share issuance, hostile-control litigation, failed closing, or explicit withdrawal.

## 19. Before / After Backtest Comparison

| profile | selected trigger count | avg MFE 90D | avg MAE 90D | false positive rate | missed structural count | alignment |
|---|---:|---:|---:|---:|---:|---|
| P0 e2r_2_1_stock_web_calibrated_proxy | 3 | 111.60% | -12.39% | 33% | 0 | mixed: event spikes captured but HMM over-promoted |
| P0b e2r_2_0_baseline_reference | 3 | 111.60% | -12.39% | 67% | 0 | weaker event-completion distinction |
| P1 sector_specific_candidate_profile | 3 | 111.60% | -12.39% | 0~33% | 0 | better if non-binding sale-process cap is enforced |
| P2 canonical_archetype_candidate_profile | 3 | 111.60% | -12.39% | 0~33% | 0 | best fit for C32 compression |
| P3 counterexample_guard_profile | 1 selected positive / HMM blocked | 40.54%+ | lower false positives | 0% | 0 | conservative but may miss Korea Zinc blowoff continuation |

## 20. Score-Return Alignment Matrix

| case | score-return alignment | reason |
|---|---|---|
| SM | aligned | formal tender/control battle created tradable premium, but event cap mattered |
| Korea Zinc | partially aligned | positive event signal was correct; 4B full-window timing required non-price overlay |
| HMM | misaligned under naive profile | sale-process headline produced spike but not durable rerating |

## 21. Coverage Matrix

| large_sector_id | canonical_archetype_id | fine_archetype_id | positive_case_count | counterexample_count | 4B_case_count | 4C_case_count | new_independent_case_count | reused_case_count | calibration_usable_trigger_count | representative_trigger_count | current_profile_error_count | sector_rule_candidate | canonical_rule_candidate | coverage_gap_after_this_loop |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|
| L10_POLICY_EVENT_CROSS_REDTEAM_MISC | C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP | CONTROL_PREMIUM_TENDER_OFFER_EVENT_CAP | 2 | 1 | 3 | 1 | 3 | 0 | 5 | 3 | 2 | true | true | still needs more non-Korean tender/privatization cases and delisting/tender-clean cases |

## 22. Residual Contribution Summary

```text
new_independent_case_count: 3
reused_case_count: 0
reused_case_ids: []
new_symbol_count: 3
same_archetype_new_symbol_count: 3
same_archetype_new_trigger_family_count: 4
new_canonical_archetype_count: 0
new_fine_archetype_count: 1
new_trigger_family_count: 4
tested_existing_calibrated_axes:
  - price_only_blowoff_blocks_positive_stage
  - full_4b_requires_non_price_evidence
  - hard_4c_thesis_break_routes_to_4c
residual_error_types_found:
  - event_premium_false_positive
  - non_binding_sale_process_promoted_too_high
  - full_window_4B_too_late_after_tender_blowoff
new_axis_proposed:
  - c32_binding_tender_offer_control_premium_bonus
  - c32_non_binding_sale_process_completion_risk_cap
  - c32_tender_price_cap_4b_overlay
existing_axis_strengthened:
  - full_4b_requires_non_price_evidence
  - hard_4c_thesis_break_routes_to_4c
existing_axis_weakened: null
existing_axis_kept:
  - price_only_blowoff_blocks_positive_stage
sector_specific_rule_candidate: true
canonical_archetype_rule_candidate: true
no_new_signal_reason: null
loop_contribution_label: canonical_archetype_rule_candidate
do_not_propose_new_weight_delta: false
```

## 23. Validation Scope / Non-Validation Scope

Validated:

- stock-web manifest and price basis;
- symbol profiles and corporate-action caveats;
- entry-date, entry-price, MFE/MAE, peak, drawdown based on stock-web rows;
- C32 shadow-score logic at research-proxy level.

Not validated:

- no production scoring code was opened;
- no source parser code was inferred;
- no live candidate scan was run;
- no investment recommendation is made;
- exact exchange filing URLs still require enrichment before any production promotion batch.

## 24. Shadow Weight Calibration

```csv
row_type,axis,scope,large_sector_id,canonical_archetype_id,baseline_value,tested_value,delta,reason,backtest_effect,trigger_ids,calibration_usable_count,new_independent_case_count,counterexample_count,confidence,proposal_type,notes
shadow_weight,c32_binding_tender_offer_control_premium_bonus,canonical_archetype_specific,L10_POLICY_EVENT_CROSS_REDTEAM_MISC,C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP,0,1,+1,"Binding tender/control-premium event separated SM/Korea Zinc from HMM-style non-binding sale process","keeps positive event premium while reducing false Green",R11L10-C32-SM-Stage2-20230210|R11L10-C32-KZ-Stage2-20240913,2,2,0,medium,canonical_shadow_only,"not production; exact source URL enrichment required"
shadow_weight,c32_non_binding_sale_process_completion_risk_cap,canonical_archetype_specific,L10_POLICY_EVENT_CROSS_REDTEAM_MISC,C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP,0,1,+1,"HMM sale-process spike did not become durable rerating","blocks Stage3-Green on non-binding sale headlines",R11L10-C32-HMM-Stage2-20231218,1,1,1,medium,canonical_shadow_only,"not production"
shadow_weight,c32_tender_price_cap_4b_overlay,canonical_archetype_specific,L10_POLICY_EVENT_CROSS_REDTEAM_MISC,C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP,0,1,+1,"Tender price cap, legal challenge and dilution are non-price 4B evidence","improves 4B timing in SM/Korea Zinc",R11L10-C32-SM-Stage2-20230210|R11L10-C32-KZ-Stage2-20240913,2,2,0,medium,canonical_shadow_only,"not production"
```

## 25. Machine-Readable Rows

```jsonl
{"row_type": "price_source_validation", "source": "Songdaiki/stock-web", "source_url": "https://github.com/Songdaiki/stock-web", "manifest_path": "atlas/manifest.json", "schema_path": "atlas/schema.json", "universe_path": "atlas/universe/all_symbols.csv", "manifest_max_date": "2026-02-20", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "raw_shard_root": "atlas/ohlcv_raw_by_symbol_year", "validation_status": "usable_for_historical_calibration"}
{"row_type": "case", "case_id": "R11L10-C32-SM-20230210", "symbol": "041510", "company_name": "에스엠", "round": "R11", "loop": "10", "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP", "fine_archetype_id": "CONTROL_PREMIUM_TENDER_OFFER_EVENT_CAP", "case_type": "4B_overlay_success", "positive_or_counterexample": "positive", "best_trigger": "R11L10-C32-SM-Stage2-20230210", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "event_premium_positive_with_4B_cap", "current_profile_verdict": "current_profile_correct", "price_source": "Songdaiki/stock-web", "notes": "2023-03-08 high 161,200; later fall to 2023-03-27 low 90,500 after event premium faded."}
{"row_type": "trigger", "trigger_id": "R11L10-C32-SM-Stage2-20230210", "case_id": "R11L10-C32-SM-20230210", "symbol": "041510", "company_name": "에스엠", "round": "R11", "loop": "10", "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP", "fine_archetype_id": "CONTROL_PREMIUM_TENDER_OFFER_EVENT_CAP", "sector": "정책·지정학·재난·이벤트", "primary_archetype": "governance/control-premium/tender cap", "loop_objective": "coverage_gap_fill|sector_specific_rule_discovery|canonical_archetype_compression|4B_non_price_requirement_stress_test|4C_thesis_break_timing_test|counterexample_mining", "trigger_type": "Stage2-Actionable", "trigger_date": "2023-02-10", "entry_date": "2023-02-10", "entry_price": 114700, "evidence_available_at_that_date": "HYBE control-stake acquisition and tender-offer battle created a binding control-premium path; Kakao later raised the tender price to 150,000 won.", "evidence_source": "AP coverage of Kakao tender offer and HYBE stake/tender context; exact exchange filing enrichment required before production promotion.", "stage2_evidence_fields": ["public_event_or_disclosure", "relative_strength", "control_premium_or_event_premium"], "stage3_evidence_fields": ["multiple_public_sources", "durable_customer_confirmation:not_applicable", "financial_visibility:not_supported"], "stage4b_evidence_fields": ["control_premium_or_event_premium", "explicit_event_cap", "valuation_blowoff"], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/041/041510/2023.csv", "profile_path": "atlas/symbol_profiles/041/041510.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": 40.54, "MFE_90D_pct": 40.54, "MFE_180D_pct": 40.54, "MFE_1Y_pct": "not_calibrated_in_this_loop", "MFE_2Y_pct": "not_calibrated_in_this_loop", "MAE_30D_pct": -21.1, "MAE_90D_pct": -21.1, "MAE_180D_pct": -21.1, "MAE_1Y_pct": "not_calibrated_in_this_loop", "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2023-03-08", "peak_price": 161200, "drawdown_after_peak_pct": -43.86, "green_lateness_ratio": 0.75, "four_b_local_peak_proximity": 0.75, "four_b_full_window_peak_proximity": 0.75, "four_b_timing_verdict": "good_full_window_4B_timing", "four_b_evidence_type": ["control_premium_or_event_premium", "valuation_blowoff"], "four_c_protection_label": "thesis_break_watch_only", "trigger_outcome_label": "event_premium_positive_with_4B_cap", "current_profile_verdict": "current_profile_correct", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window", "same_entry_group_id": "R11L10-C32-SM-20230210-entry", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R11L10-C32-SM-20230210", "trigger_id": "R11L10-C32-SM-Stage2-20230210", "symbol": "041510", "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP", "raw_component_scores_before": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 0, "revision_score": 0, "relative_strength_score": 14, "customer_quality_score": 0, "policy_or_regulatory_score": 0, "valuation_repricing_score": 18, "execution_risk_score": 0, "legal_or_contract_risk_score": 8, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0, "control_premium_score": 21, "tender_binding_score": 18, "event_completion_risk_score": 8}, "weighted_score_before": 82, "stage_label_before": "Stage3-Yellow event premium", "raw_component_scores_after": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 0, "revision_score": 0, "relative_strength_score": 14, "customer_quality_score": 0, "policy_or_regulatory_score": 0, "valuation_repricing_score": 18, "execution_risk_score": 0, "legal_or_contract_risk_score": 8, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0, "control_premium_score": 24, "tender_binding_score": 18, "event_completion_risk_score": 8}, "weighted_score_after": 84, "stage_label_after": "Stage3-Yellow + 4B cap", "changed_components": ["control_premium_score", "tender_binding_score", "event_completion_risk_score", "dilution_cb_risk_score"], "component_delta_explanation": "C32 shadow profile separates binding tender/control-premium event from non-binding sale process or post-tender dilution/legal risk.", "MFE_90D_pct": 40.54, "MAE_90D_pct": -21.1, "score_return_alignment_label": "event_premium_positive_with_4B_cap", "current_profile_verdict": "current_profile_correct"}
{"row_type": "case", "case_id": "R11L10-C32-KZ-20240913", "symbol": "010130", "company_name": "고려아연", "round": "R11", "loop": "10", "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP", "fine_archetype_id": "CONTROL_PREMIUM_TENDER_OFFER_EVENT_CAP", "case_type": "4B_overlay_success", "positive_or_counterexample": "positive", "best_trigger": "R11L10-C32-KZ-Stage2-20240913", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "control_premium_positive_but_full_window_4B_needed", "current_profile_verdict": "current_profile_4B_too_late", "price_source": "Songdaiki/stock-web", "notes": "2024-12-06 high 2,407,000; later drawdown to 2025-04-09 low 643,000."}
{"row_type": "trigger", "trigger_id": "R11L10-C32-KZ-Stage2-20240913", "case_id": "R11L10-C32-KZ-20240913", "symbol": "010130", "company_name": "고려아연", "round": "R11", "loop": "10", "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP", "fine_archetype_id": "CONTROL_PREMIUM_TENDER_OFFER_EVENT_CAP", "sector": "정책·지정학·재난·이벤트", "primary_archetype": "governance/control-premium/tender cap", "loop_objective": "coverage_gap_fill|sector_specific_rule_discovery|canonical_archetype_compression|4B_non_price_requirement_stress_test|4C_thesis_break_timing_test|counterexample_mining", "trigger_type": "Stage2-Actionable", "trigger_date": "2024-09-13", "entry_date": "2024-09-13", "entry_price": 666000, "evidence_available_at_that_date": "Young Poong and MBK tender offer at 660,000 won opened an explicit hostile control-premium path; later court/tender/buyback/issuance events turned it into an event-premium blowoff.", "evidence_source": "Reuters tender-offer and later Korea Zinc control-battle coverage; exact local filings enrichment required before production promotion.", "stage2_evidence_fields": ["public_event_or_disclosure", "relative_strength", "control_premium_or_event_premium"], "stage3_evidence_fields": ["multiple_public_sources", "financial_visibility:not_supported", "low_red_team_risk:false"], "stage4b_evidence_fields": ["control_premium_or_event_premium", "valuation_blowoff", "capital_raise_or_overhang", "legal_or_regulatory_block"], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/010/010130/2024.csv|atlas/ohlcv_tradable_by_symbol_year/010/010130/2025.csv", "profile_path": "atlas/symbol_profiles/010/010130.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": 131.68, "MFE_90D_pct": 261.41, "MFE_180D_pct": 261.41, "MFE_1Y_pct": "not_calibrated_in_this_loop", "MFE_2Y_pct": "not_calibrated_in_this_loop", "MAE_30D_pct": -1.65, "MAE_90D_pct": -1.65, "MAE_180D_pct": -3.45, "MAE_1Y_pct": "not_calibrated_in_this_loop", "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2024-12-06", "peak_price": 2407000, "drawdown_after_peak_pct": -73.29, "green_lateness_ratio": "not_applicable_no_structural_green", "four_b_local_peak_proximity": 0.87, "four_b_full_window_peak_proximity": 1.0, "four_b_timing_verdict": "good_full_window_4B_timing", "four_b_evidence_type": ["control_premium_or_event_premium", "valuation_blowoff"], "four_c_protection_label": "thesis_break_watch_only", "trigger_outcome_label": "control_premium_positive_but_full_window_4B_needed", "current_profile_verdict": "current_profile_4B_too_late", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window", "same_entry_group_id": "R11L10-C32-KZ-20240913-entry", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R11L10-C32-KZ-20240913", "trigger_id": "R11L10-C32-KZ-Stage2-20240913", "symbol": "010130", "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP", "raw_component_scores_before": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 0, "revision_score": 0, "relative_strength_score": 18, "customer_quality_score": 0, "policy_or_regulatory_score": 0, "valuation_repricing_score": 22, "execution_risk_score": 0, "legal_or_contract_risk_score": 15, "dilution_cb_risk_score": 9, "accounting_trust_risk_score": 0, "control_premium_score": 24, "tender_binding_score": 20, "event_completion_risk_score": 15}, "weighted_score_before": 88, "stage_label_before": "Stage3-Green event premium", "raw_component_scores_after": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 0, "revision_score": 0, "relative_strength_score": 18, "customer_quality_score": 0, "policy_or_regulatory_score": 0, "valuation_repricing_score": 22, "execution_risk_score": 0, "legal_or_contract_risk_score": 15, "dilution_cb_risk_score": 17, "accounting_trust_risk_score": 0, "control_premium_score": 24, "tender_binding_score": 20, "event_completion_risk_score": 15}, "weighted_score_after": 82, "stage_label_after": "Stage3-Yellow + full 4B overlay", "changed_components": ["control_premium_score", "tender_binding_score", "event_completion_risk_score", "dilution_cb_risk_score"], "component_delta_explanation": "C32 shadow profile separates binding tender/control-premium event from non-binding sale process or post-tender dilution/legal risk.", "MFE_90D_pct": 261.41, "MAE_90D_pct": -1.65, "score_return_alignment_label": "control_premium_positive_but_full_window_4B_needed", "current_profile_verdict": "current_profile_4B_too_late"}
{"row_type": "case", "case_id": "R11L10-C32-HMM-20231218", "symbol": "011200", "company_name": "HMM", "round": "R11", "loop": "10", "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP", "fine_archetype_id": "CONTROL_PREMIUM_TENDER_OFFER_EVENT_CAP", "case_type": "false_positive_green", "positive_or_counterexample": "counterexample", "best_trigger": "R11L10-C32-HMM-Stage2-20231218", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "event_premium_spike_without_durable_rerating", "current_profile_verdict": "current_profile_false_positive", "price_source": "Songdaiki/stock-web", "notes": "2023-12-20 high 23,300; later 2024-04-08 low around 15,010 after sale uncertainty/collapse."}
{"row_type": "trigger", "trigger_id": "R11L10-C32-HMM-Stage2-20231218", "case_id": "R11L10-C32-HMM-20231218", "symbol": "011200", "company_name": "HMM", "round": "R11", "loop": "10", "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP", "fine_archetype_id": "CONTROL_PREMIUM_TENDER_OFFER_EVENT_CAP", "sector": "정책·지정학·재난·이벤트", "primary_archetype": "governance/control-premium/tender cap", "loop_objective": "coverage_gap_fill|sector_specific_rule_discovery|canonical_archetype_compression|4B_non_price_requirement_stress_test|4C_thesis_break_timing_test|counterexample_mining", "trigger_type": "Stage2-Actionable", "trigger_date": "2023-12-18", "entry_date": "2023-12-18", "entry_price": 17540, "evidence_available_at_that_date": "Preferred-bidder sale event created a sharp event-premium spike, but closing certainty was weak and the sale later broke down; this should not be promoted to structural Stage3-Green.", "evidence_source": "HMM sale-failure summary plus stock-web price row; exact local transaction-source enrichment required before production promotion.", "stage2_evidence_fields": ["public_event_or_disclosure", "relative_strength", "control_premium_or_event_premium"], "stage3_evidence_fields": ["confirmed_revision:not_supported", "financial_visibility:not_supported", "low_red_team_risk:false"], "stage4b_evidence_fields": ["price_only_local_peak", "explicit_event_cap", "legal_or_contract_risk"], "stage4c_evidence_fields": ["thesis_evidence_broken", "contract_cancelled"], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/011/011200/2023.csv|atlas/ohlcv_tradable_by_symbol_year/011/011200/2024.csv", "profile_path": "atlas/symbol_profiles/011/011200.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": 32.84, "MFE_90D_pct": 32.84, "MFE_180D_pct": 32.84, "MFE_1Y_pct": "not_calibrated_in_this_loop", "MFE_2Y_pct": "not_calibrated_in_this_loop", "MAE_30D_pct": -9.92, "MAE_90D_pct": -14.42, "MAE_180D_pct": -14.42, "MAE_1Y_pct": "not_calibrated_in_this_loop", "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2023-12-20", "peak_price": 23300, "drawdown_after_peak_pct": -35.58, "green_lateness_ratio": "not_applicable_no_structural_green", "four_b_local_peak_proximity": 1.0, "four_b_full_window_peak_proximity": 1.0, "four_b_timing_verdict": "price_only_local_4B_too_early", "four_b_evidence_type": ["price_only", "legal_or_contract_risk"], "four_c_protection_label": "hard_4c_success", "trigger_outcome_label": "event_premium_spike_without_durable_rerating", "current_profile_verdict": "current_profile_false_positive", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_after_2023_11_10_corporate_action_candidate", "same_entry_group_id": "R11L10-C32-HMM-20231218-entry", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R11L10-C32-HMM-20231218", "trigger_id": "R11L10-C32-HMM-Stage2-20231218", "symbol": "011200", "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP", "raw_component_scores_before": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 0, "revision_score": 0, "relative_strength_score": 11, "customer_quality_score": 0, "policy_or_regulatory_score": 0, "valuation_repricing_score": 11, "execution_risk_score": 0, "legal_or_contract_risk_score": 16, "dilution_cb_risk_score": 10, "accounting_trust_risk_score": 0, "control_premium_score": 13, "tender_binding_score": 4, "event_completion_risk_score": 24}, "weighted_score_before": 76, "stage_label_before": "Stage3-Yellow false positive risk", "raw_component_scores_after": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 0, "revision_score": 0, "relative_strength_score": 11, "customer_quality_score": 0, "policy_or_regulatory_score": 0, "valuation_repricing_score": 11, "execution_risk_score": 0, "legal_or_contract_risk_score": 16, "dilution_cb_risk_score": 10, "accounting_trust_risk_score": 0, "control_premium_score": 13, "tender_binding_score": 0, "event_completion_risk_score": 32}, "weighted_score_after": 63, "stage_label_after": "Stage2-Watch/4C-Watch", "changed_components": ["control_premium_score", "tender_binding_score", "event_completion_risk_score", "dilution_cb_risk_score"], "component_delta_explanation": "C32 shadow profile separates binding tender/control-premium event from non-binding sale process or post-tender dilution/legal risk.", "MFE_90D_pct": 32.84, "MAE_90D_pct": -14.42, "score_return_alignment_label": "event_premium_spike_without_durable_rerating", "current_profile_verdict": "current_profile_false_positive"}
{"row_type": "trigger", "trigger_id": "R11L10-C32-SM-4B-20230308", "case_id": "R11L10-C32-SM-20230210", "symbol": "041510", "company_name": "에스엠", "round": "R11", "loop": "10", "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP", "fine_archetype_id": "CONTROL_PREMIUM_TENDER_OFFER_EVENT_CAP", "sector": "정책·지정학·재난·이벤트", "primary_archetype": "governance/control-premium/tender cap", "loop_objective": "4B_non_price_requirement_stress_test", "trigger_type": "Stage4B-Overlay", "trigger_date": "2023-03-08", "entry_date": "2023-03-08", "entry_price": 158500, "evidence_available_at_that_date": "Kakao tender price acted as explicit event cap after control battle premium peaked.", "evidence_source": "AP/public reporting; exact exchange filing enrichment required.", "stage2_evidence_fields": [], "stage3_evidence_fields": [], "stage4b_evidence_fields": ["explicit_event_cap", "valuation_blowoff", "control_premium_or_event_premium"], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/041/041510/2023.csv", "profile_path": "atlas/symbol_profiles/041/041510.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": 1.7, "MFE_90D_pct": 1.7, "MFE_180D_pct": 1.7, "MAE_30D_pct": -42.9, "MAE_90D_pct": -42.9, "MAE_180D_pct": -42.9, "peak_date": "2023-03-08", "peak_price": 161200, "drawdown_after_peak_pct": -43.86, "green_lateness_ratio": 0.75, "four_b_local_peak_proximity": 1.0, "four_b_full_window_peak_proximity": 1.0, "four_b_timing_verdict": "good_full_window_4B_timing", "four_b_evidence_type": ["valuation_blowoff", "control_premium_or_event_premium", "explicit_event_cap"], "four_c_protection_label": "thesis_break_watch_only", "trigger_outcome_label": "4B_overlay_success", "current_profile_verdict": "current_profile_correct", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window", "same_entry_group_id": "R11L10-C32-SM-20230210-4b", "dedupe_for_aggregate": false, "aggregate_group_role": "4B_overlay_only", "is_new_independent_case": false, "reuse_reason": "same case, 4B overlay timing audit", "independent_evidence_weight": 0.0, "do_not_count_as_new_case": true}
{"row_type": "trigger", "trigger_id": "R11L10-C32-KZ-4B-20241206", "case_id": "R11L10-C32-KZ-20240913", "symbol": "010130", "company_name": "고려아연", "round": "R11", "loop": "10", "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP", "fine_archetype_id": "CONTROL_PREMIUM_TENDER_OFFER_EVENT_CAP", "sector": "정책·지정학·재난·이벤트", "primary_archetype": "governance/control-premium/tender cap", "loop_objective": "4B_non_price_requirement_stress_test", "trigger_type": "Stage4B-Overlay", "trigger_date": "2024-12-06", "entry_date": "2024-12-06", "entry_price": 1813000, "evidence_available_at_that_date": "Control-battle premium reached full-window blowoff zone after tender, buyback, legal dispute and financing/dilution concerns.", "evidence_source": "Reuters/public reporting; exact local filing enrichment required.", "stage2_evidence_fields": [], "stage3_evidence_fields": [], "stage4b_evidence_fields": ["valuation_blowoff", "legal_or_regulatory_block", "capital_raise_or_overhang", "control_premium_or_event_premium"], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/010/010130/2024.csv|atlas/ohlcv_tradable_by_symbol_year/010/010130/2025.csv", "profile_path": "atlas/symbol_profiles/010/010130.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": 32.76, "MFE_90D_pct": 32.76, "MFE_180D_pct": 32.76, "MAE_30D_pct": -54.99, "MAE_90D_pct": -64.53, "MAE_180D_pct": -64.53, "peak_date": "2024-12-06", "peak_price": 2407000, "drawdown_after_peak_pct": -73.29, "green_lateness_ratio": "not_applicable_event_4B_overlay", "four_b_local_peak_proximity": 1.0, "four_b_full_window_peak_proximity": 1.0, "four_b_timing_verdict": "good_full_window_4B_timing", "four_b_evidence_type": ["valuation_blowoff", "legal_or_regulatory_block", "capital_raise_or_overhang", "control_premium_or_event_premium"], "four_c_protection_label": "thesis_break_watch_only", "trigger_outcome_label": "4B_overlay_success", "current_profile_verdict": "current_profile_4B_too_late", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window", "same_entry_group_id": "R11L10-C32-KZ-20240913-4b", "dedupe_for_aggregate": false, "aggregate_group_role": "4B_overlay_only", "is_new_independent_case": false, "reuse_reason": "same case, 4B overlay timing audit", "independent_evidence_weight": 0.0, "do_not_count_as_new_case": true}
{"row_type": "residual_contribution", "round": "R11", "loop": "10", "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP", "new_independent_case_count": 3, "reused_case_count": 0, "new_symbol_count": 3, "same_archetype_new_symbol_count": 3, "same_archetype_new_trigger_family_count": 4, "new_trigger_family_count": 4, "positive_case_count": 2, "counterexample_count": 1, "current_profile_error_count": 2, "tested_existing_calibrated_axes": ["full_4b_requires_non_price_evidence", "hard_4c_thesis_break_routes_to_4c", "price_only_blowoff_blocks_positive_stage"], "residual_error_types_found": ["event_premium_false_positive", "4B_too_late_after_tender_blowoff", "non_binding_sale_process_promoted_too_high"], "loop_contribution_label": "canonical_archetype_rule_candidate", "do_not_propose_new_weight_delta": false}
```

## 26. Deferred Coding Agent Handoff Prompt

### Purpose

You are now in the repository implementation phase. The attached Markdown files are v12 post-calibrated residual research outputs produced using the Songdaiki/stock-web OHLC atlas.

These MDs are not live candidate research. They are historical calibration research designed to extend the already-applied e2r_2_1_stock_web_calibrated profile.

Do not blindly apply every shadow row.
Ingest the machine-readable rows and update the sector/canonical-archetype calibration ledger.

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
completed_round = R11
completed_loop = 10
next_round = R12
next_loop = 10
round_schedule_status = valid
round_sector_consistency = pass
```

## 28. Source Notes

- Stock-Web manifest max_date: 2026-02-20.
- Price basis: tradable_raw.
- Adjustment status: raw_unadjusted_marcap.
- Evidence URLs are intentionally treated as research references, not production-ready source objects.
- This file is not an investment recommendation and does not modify production scoring.
