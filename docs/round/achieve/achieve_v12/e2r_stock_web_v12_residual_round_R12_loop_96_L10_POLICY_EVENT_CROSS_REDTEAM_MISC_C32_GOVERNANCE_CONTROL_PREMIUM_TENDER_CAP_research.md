# E2R Stock-Web Historical Calibration / Sector-Archetype Residual Research Round

## 0. Research Metadata

```text
research_session = post_calibrated_sector_archetype_residual_research
mode = historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12
scheduled_round = R12
scheduled_loop = 96
round_schedule_status = valid
round_sector_consistency = pass
large_sector_id = L10_POLICY_EVENT_CROSS_REDTEAM_MISC
canonical_archetype_id = C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP
fine_archetype_id = SECURITIES_SALE_CONTROL_PREMIUM_BRIDGE_VS_MEDIA_PRIVATIZATION_FALSE_STAGE2_AND_BIO_HOLDCO_MERGER_CONTROL_EVENT_CAP
loop_objective = coverage_gap_fill | counterexample_mining | stage2_actionable_bonus_stress_test | 4B_non_price_requirement_stress_test | high_MAE_guardrail | tender_cap_guardrail | canonical_archetype_compression
output_file = e2r_stock_web_v12_residual_round_R12_loop_96_L10_POLICY_EVENT_CROSS_REDTEAM_MISC_C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP_research.md
```

This file is the corrected final output for this execution. The scheduler state after R11 loop 96 is R12 / loop 96. R12 is the L10 policy/event/cross-redteam/misc round, and this run fills C32 governance/control-premium/tender-cap behavior rather than repeating the immediately preceding R12 loop 95 C31 policy/subsidy file or R12 loop 94 C32 symbols.

## 1. Current Calibrated Profile Assumption

```text
current_default_profile_proxy = e2r_2_1_stock_web_calibrated
previous_baseline_reference = e2r_2_0_baseline
production_scoring_changed = false
shadow_weight_only = true
```

Existing axes tested:

```text
stage2_required_bridge = existing_axis_strengthened
local_4b_watch_guard = existing_axis_strengthened
high_MAE_guardrail = existing_axis_strengthened
tender_cap_guardrail = existing_axis_strengthened
hard_4c_thesis_break_routes_to_4c = existing_axis_kept
full_4b_requires_non_price_evidence = existing_axis_kept
price_only_blowoff_blocks_positive_stage = existing_axis_kept
```

## 2. Round / Large Sector / Canonical Archetype Scope

```text
scheduled_round = R12
scheduled_loop = 96
large_sector_id = L10_POLICY_EVENT_CROSS_REDTEAM_MISC
canonical_archetype_id = C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP
round_sector_consistency = pass
computed_next_round = R13
computed_next_loop = 96
```

C32 is a governance/control-premium/tender-cap archetype. The rumor is only the auctioneer's bell; the evidence is binding process, credible bidders, board/major-holder intent, regulatory and closing visibility, tender or transaction-price floor, and minority-holder path.

## 3. Previous Coverage / Duplicate Avoidance Check

No-Repeat hard key used:

```text
canonical_archetype_id + symbol + trigger_type + entry_date
```

No-Repeat snapshot context:

```text
C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP = 41 rows / 22 symbols / good-bad Stage2 16-12 / 4B-4C 3-0
top covered symbols include 010130(4), 036560(4), 000150(3), 041510(3), 241560(3), 000990(2)
previous R12 loop-94 C32 symbols avoided: 267250, 034730, 000240
previous R12 loop-95 C31 symbols avoided: 034230, 159580, 407400
previous R11 loop-96 C04 symbols avoided: 052690, 105840, 019990
previous R10 loop-96 C30 symbols avoided: 010960, 017000, 091590
```

Selected rows avoid hard duplicates and top repeated C32 symbols:

```text
001750 / Stage2-Actionable / 2024-07-10
040300 / Stage2-Actionable / 2024-02-05
008930 / Stage4B / 2024-01-16
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
| 001750 | atlas/symbol_profiles/001/001750.json | no corporate-action candidate |
| 040300 | atlas/symbol_profiles/040/040300.json | no corporate-action candidate |
| 008930 | atlas/symbol_profiles/008/008930.json | selected 2024 window clean after old 1999/2010/2012 CA candidates |

## 5. Historical Eligibility Gate

| case_id | symbol | entry_date | entry in shard | forward 180D | OHLC valid | CA clean | calibration_usable |
|---|---|---:|---|---:|---|---|---|
| R12L96_C32_HANYANGSEC_2024_SECURITIES_SALE_CONTROL_PREMIUM_BRIDGE_POSITIVE | 001750 | 2024-07-10 | yes | 180 | yes | yes | true |
| R12L96_C32_YTN_2024_MEDIA_PRIVATIZATION_CONTROL_FALSE_STAGE2 | 040300 | 2024-02-05 | yes | 180 | yes | yes | true |
| R12L96_C32_HANMISCIENCE_2024_BIO_HOLDCO_MERGER_CONTROL_EVENT_CAP_4B | 008930 | 2024-01-16 | yes | 180 | yes | yes | true |

## 6. Canonical Archetype Compression Map

| canonical | fine/deep split | meaning |
|---|---|---|
| C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP | SECURITIES_SALE_CONTROL_PREMIUM_BRIDGE | Positive Stage2 requires binding sale process, credible bidder set, major-holder/board intent, regulatory closing path and transaction-price floor. |
| C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP | MEDIA_PRIVATIZATION_FALSE_STAGE2 | Privatization/control watch without binding transaction economics and closing path can become false Stage2. |
| C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP | BIO_HOLDCO_MERGER_CONTROL_EVENT_CAP_4B | Merger/control premium should route to 4B when vote, litigation/regulatory path and price floor are missing. |

## 7. Case Selection Summary

| case_id | symbol | company | role | selected reason |
|---|---|---|---|---|
| R12L96_C32_HANYANGSEC_2024_SECURITIES_SALE_CONTROL_PREMIUM_BRIDGE_POSITIVE | 001750 | 한양증권 | positive | Sale/control-premium process produced strong MFE with shallow MAE. |
| R12L96_C32_YTN_2024_MEDIA_PRIVATIZATION_CONTROL_FALSE_STAGE2 | 040300 | YTN | counterexample | Media privatization/control-premium watch had brief MFE and then deep drawdown. |
| R12L96_C32_HANMISCIENCE_2024_BIO_HOLDCO_MERGER_CONTROL_EVENT_CAP_4B | 008930 | 한미사이언스 | counterexample / 4B | Bio-holdco merger/control premium capped on the January spike and then de-rated sharply. |

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
| Hanyang Securities sale/control-premium bridge | historical public/news proxy | true | true | shadow-only positive |
| YTN media privatization false Stage2 | historical public/news proxy | true | true | false-Stage2 guardrail |
| Hanmi Science bio-holdco merger/control event cap | historical public/news proxy | true | true | 4B overlay counterexample |

## 10. Price Data Source Map

| symbol | shard | profile |
|---|---|---|
| 001750 | atlas/ohlcv_tradable_by_symbol_year/001/001750/2024.csv and 2025.csv | atlas/symbol_profiles/001/001750.json |
| 040300 | atlas/ohlcv_tradable_by_symbol_year/040/040300/2024.csv | atlas/symbol_profiles/040/040300.json |
| 008930 | atlas/ohlcv_tradable_by_symbol_year/008/008930/2024.csv | atlas/symbol_profiles/008/008930.json |

## 11. Case-by-Case Trigger Grid

| trigger_id | symbol | trigger_type | entry_date | entry_price | role | verdict |
|---|---|---|---:|---:|---|---|
| R12L96_C32_HANYANGSEC_2024_STAGE2_ACTIONABLE_SECURITIES_SALE_CONTROL_PREMIUM_BRIDGE | 001750 | Stage2-Actionable | 2024-07-10 | 11700 | positive | securities sale/control-premium bridge worked |
| R12L96_C32_YTN_2024_STAGE2_FALSE_POSITIVE_MEDIA_PRIVATIZATION_CONTROL_WATCH | 040300 | Stage2-Actionable | 2024-02-05 | 5840 | counterexample | media privatization false Stage2 |
| R12L96_C32_HANMISCIENCE_2024_STAGE4B_BIO_HOLDCO_MERGER_CONTROL_EVENT_CAP | 008930 | Stage4B | 2024-01-16 | 56200 | counterexample/4B | bio-holdco merger/control event cap |

## 12. Trigger-Level OHLC Backtest Tables

| trigger_id | entry | MFE30 | MAE30 | MFE90 | MAE90 | MFE180 | MAE180 | peak_date | peak_price | drawdown_after_peak |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| R12L96_C32_HANYANGSEC_2024_STAGE2_ACTIONABLE_SECURITIES_SALE_CONTROL_PREMIUM_BRIDGE | 11700 | 65.90 | -1.79 | 65.90 | -1.79 | 65.90 | -3.42 | 2024-08-05 | 19410 | -41.73 |
| R12L96_C32_YTN_2024_STAGE2_FALSE_POSITIVE_MEDIA_PRIVATIZATION_CONTROL_WATCH | 5840 | 12.67 | -17.98 | 12.67 | -32.28 | 12.67 | -32.28 | 2024-02-07 | 6580 | -39.82 |
| R12L96_C32_HANMISCIENCE_2024_STAGE4B_BIO_HOLDCO_MERGER_CONTROL_EVENT_CAP | 56200 | 0.00 | -30.43 | 0.00 | -37.90 | 0.00 | -37.90 | 2024-01-16 | 56200 | -37.90 |

## 13. Current Calibrated Profile Stress Test

| axis | outcome |
|---|---|
| stage2_required_bridge | strengthen: C32 Stage2 needs binding process / bidder / board-major-holder / regulatory closing / price floor bridge |
| local_4b_watch_guard | strengthen: bridge-missing merger, privatization and control-premium spikes should route to 4B watch |
| tender_cap_guardrail | strengthen: positive promotion needs transaction/tender floor, not just governance heat |
| high_MAE_guardrail | strengthen: high-MAE control-premium rows cannot promote without durable closing bridge |
| hard_4c_thesis_break_routes_to_4c | keep; no confirmed hard 4C in this file |
| full_4b_requires_non_price_evidence | keep |
| price_only_blowoff_blocks_positive_stage | keep |

## 14. Stage2 / Yellow / Green / 4B Comparison

No confirmed Stage3-Green row is introduced. The useful split is whether governance/control narrative becomes a transaction bridge.

| symbol | stage quality | explanation |
|---|---|---|
| 001750 | good_stage2_with_later_watch | Sale process and control-premium bridge produced strong MFE with shallow MAE. |
| 040300 | bad_stage2 | Privatization/control watch lacked binding closing and price-floor bridge, then suffered high MAE. |
| 008930 | good_4B | Merger/control premium peaked on event day and then de-rated deeply. |

```text
green_lateness_ratio = not_applicable
reason = no confirmed Stage3-Green trigger
```

## 15. 4B Local vs Full-window Timing Audit

| trigger | local proximity | full-window proximity | timing verdict |
|---|---:|---:|---|
| 040300 media privatization false Stage2 | 0.89 | 0.89 | false Stage2 due missing binding transaction / closing / tender-price floor bridge |
| 008930 bio-holdco merger-control cap | 1.00 | 1.00 | good full-window 4B timing after January merger/control event premium |
| 001750 securities sale bridge | n/a | n/a | positive Stage2, but later tender-cap and sale-process valuation watch required |

## 16. 4C Protection Audit

```text
4C_case_count = 0
four_c_protection_label = regulatory_closing_watch_only / control_thesis_break_watch_only
```

No hard 4C candidate is introduced in this R12 loop 96 file. The counterexamples are bridge-missing / event-cap rows, not confirmed thesis-break rows.

## 17. Sector-Specific Rule Candidate

```text
sector_specific_rule_candidate = true
rule_scope = sector_specific
rule = In L10 governance/control-premium/tender-cap cases, Stage2 requires binding process, credible bidder or counterparty, board/major-holder intent, regulatory/closing visibility, tender or transaction-price floor, minority shareholder path, and valuation discipline. Governance, control-premium, privatization, sale, merger, activist or tender label alone remains watch/4B.
proposal_status = shadow_only
```

## 18. Canonical-Archetype Rule Candidate

```text
canonical_archetype_rule_candidate = true
canonical_archetype_id = C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP
rule = C32 should split true sale/tender/control-premium bridge positives from privatization false Stage2 and merger-control event caps. Event-cap rows are 4B overlay/risk calibration, not Stage3-Green promotion evidence.
proposal_status = shadow_only_not_production
```

## 19. Before / After Backtest Comparison

| profile | hypothesis | eligible triggers | avg_MFE90 | avg_MAE90 | false_positive_or_guardrail_rate | verdict |
|---|---|---:|---:|---:|---:|---|
| P0 e2r_2_1_stock_web_calibrated_proxy | current profile | 3 | 26.19 | -23.99 | 0.67 | mixed; C32 bridge split needed |
| P0b e2r_2_0_baseline_reference | older baseline | 3 | 26.19 | -23.99 | 0.67 | weaker 4B/Stage2 separation |
| P1 sector_specific_candidate_profile | L10 binding process/price-floor bridge required | 2 | 39.29 | -17.04 | 0.50 | better |
| P2 canonical_archetype_candidate_profile | C32 bridge vs event-cap split | 2 | 39.29 | -17.04 | 0.50 | best explanatory fit |
| P3 counterexample_guard_profile | reject bridge-missing control-premium themes as positive | 1 | 65.90 | -1.79 | 0.00 | safest but source-proxy blockers remain |

## 20. Score-Return Alignment Matrix

| trigger | score before | stage before | score after | stage after | MFE90 | MAE90 | alignment |
|---|---:|---|---:|---|---:|---:|---|
| 001750 securities sale bridge | 66 | Stage2-Watch | 78 | Stage2-Actionable | 65.90 | -1.79 | securities_sale_control_premium_positive |
| 040300 media privatization false | 66 | Stage2-Actionable | 52 | Stage1/Watch | 12.67 | -32.28 | media_privatization_control_false_stage2 |
| 008930 bio-holdco merger cap | 70 | Stage3-Yellow-like | 54 | Stage4B-watch | 0.00 | -37.90 | bio_holdco_merger_control_event_cap_4B_guard |

## 21. Coverage Matrix

```jsonl
{"row_type": "coverage_matrix", "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP", "fine_archetype_id": "SECURITIES_SALE_CONTROL_PREMIUM_BRIDGE_VS_MEDIA_PRIVATIZATION_FALSE_STAGE2_AND_BIO_HOLDCO_MERGER_CONTROL_EVENT_CAP", "positive_case_count": 1, "counterexample_count": 2, "4B_case_count": 1, "4C_case_count": 0, "new_independent_case_count": 3, "reused_case_count": 0, "calibration_usable_trigger_count": 3, "representative_trigger_count": 2, "current_profile_error_count": 2, "sector_rule_candidate": true, "canonical_rule_candidate": true, "coverage_gap_after_this_loop": "Adds C32 Hanyang Securities sale/control-premium positive, YTN media privatization false Stage2, and Hanmi Science bio-holdco merger/control event-cap 4B while avoiding top repeated C32 and previous R12/R11/R10 loop symbols."}
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
tested_existing_calibrated_axes: stage2_required_bridge, local_4b_watch_guard, tender_cap_guardrail, high_MAE_guardrail, hard_4c_thesis_break_routes_to_4c, full_4b_requires_non_price_evidence, price_only_blowoff_blocks_positive_stage
residual_error_types_found: securities_sale_control_premium_positive, media_privatization_control_false_stage2, bio_holdco_merger_control_event_cap_4B
new_axis_proposed: null
existing_axis_strengthened: stage2_required_bridge, local_4b_watch_guard, tender_cap_guardrail, high_MAE_guardrail
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
- C32 governance/control-premium/tender-cap bridge vs false Stage2 / event-cap split
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
shadow_weight,stage2_required_bridge,canonical_archetype,L10_POLICY_EVENT_CROSS_REDTEAM_MISC,C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP,configured,C32_requires_binding_process_bidders_board_major_holder_regulatory_closing_price_floor_bridge,0,"C32 Stage2 should require binding process, credible bidders, board/major-holder intent, regulatory/closing visibility, tender or transaction-price floor, and minority-shareholder path, not governance/control-premium label alone","Hanyang Securities positive worked; YTN and Hanmi Science event/watch rows failed positive-stage promotion","R12L96_C32_HANYANGSEC_2024_STAGE2_ACTIONABLE_SECURITIES_SALE_CONTROL_PREMIUM_BRIDGE|R12L96_C32_YTN_2024_STAGE2_FALSE_POSITIVE_MEDIA_PRIVATIZATION_CONTROL_WATCH|R12L96_C32_HANMISCIENCE_2024_STAGE4B_BIO_HOLDCO_MERGER_CONTROL_EVENT_CAP",3,3,2,low,canonical_shadow_only,"do_not_propose_new_weight_delta=true because source-proxy/evidence-url-pending rows remain"
shadow_weight,local_4b_watch_guard,canonical_archetype,L10_POLICY_EVENT_CROSS_REDTEAM_MISC,C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP,configured,cap_bridge_missing_merger_control_and_privatization_event_premiums_as_4B_watch,0,"Media privatization and bio-holdco merger/control premiums can peak before binding price, closing path, vote/litigation and minority-holder bridge is proven","YTN had brief MFE then deep MAE; Hanmi Science showed clean 4B event-cap behavior after January merger/control spike","R12L96_C32_YTN_2024_STAGE2_FALSE_POSITIVE_MEDIA_PRIVATIZATION_CONTROL_WATCH|R12L96_C32_HANMISCIENCE_2024_STAGE4B_BIO_HOLDCO_MERGER_CONTROL_EVENT_CAP",2,2,2,medium,guardrail_shadow_only,"4B overlay only; not production"
shadow_weight,high_MAE_guardrail,canonical_archetype,L10_POLICY_EVENT_CROSS_REDTEAM_MISC,C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP,configured,block_positive_stage_when_control_premium_theme_has_high_or_persistent_MAE_without_binding_closing_bridge,0,"High or persistent MAE after bridge-missing C32 entries should block Stage2/Stage3 promotion unless binding process, closing path and price floor evidence survives","YTN MAE90=-32.28 and Hanmi Science MAE90=-37.90","R12L96_C32_YTN_2024_STAGE2_FALSE_POSITIVE_MEDIA_PRIVATIZATION_CONTROL_WATCH|R12L96_C32_HANMISCIENCE_2024_STAGE4B_BIO_HOLDCO_MERGER_CONTROL_EVENT_CAP",2,2,2,medium,guardrail_shadow_only,"canonical shadow profile only"
```

## 25. Machine-Readable Rows

### 25.1 price_source_validation

```jsonl
{"row_type": "price_source_validation", "source": "Songdaiki/stock-web", "source_url": "https://github.com/Songdaiki/stock-web", "manifest_path": "atlas/manifest.json", "schema_path": "atlas/schema.json", "universe_path": "atlas/universe/all_symbols.csv", "manifest_max_date": "2026-02-20", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "raw_shard_root": "atlas/ohlcv_raw_by_symbol_year", "validation_status": "usable_for_historical_calibration", "source_name": "FinanceData/marcap", "tradable_row_count": 14354401, "raw_row_count": 15214118, "symbol_count": 5414, "active_like_symbol_count": 2868, "inactive_or_delisted_like_symbol_count": 2546}
```

### 25.2 case rows

```jsonl
{"row_type": "case", "case_id": "R12L96_C32_HANYANGSEC_2024_SECURITIES_SALE_CONTROL_PREMIUM_BRIDGE_POSITIVE", "symbol": "001750", "company_name": "한양증권", "round": "R12", "loop": "96", "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP", "fine_archetype_id": "SECURITIES_SALE_CONTROL_PREMIUM_BRIDGE_VS_MEDIA_PRIVATIZATION_FALSE_STAGE2_AND_BIO_HOLDCO_MERGER_CONTROL_EVENT_CAP", "case_type": "structural_success_with_later_sale_process_tender_cap_watch", "positive_or_counterexample": "positive", "best_trigger": "R12L96_C32_HANYANGSEC_2024_STAGE2_ACTIONABLE_SECURITIES_SALE_CONTROL_PREMIUM_BRIDGE", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "Securities-company sale/control-premium process and buyer competition bridge produced strong 30D/90D MFE with shallow MAE. C32 works when governance/control-premium narrative maps into real sale process, credible bidder set, board/major-holder intent, regulatory closing path, tender or transaction price discipline and downside floor.", "current_profile_verdict": "current_profile_kept_but_C32_positive_requires_sale_process_bidder_board_major_holder_regulatory_closing_price_floor_bridge_not_governance_label_only", "price_source": "Songdaiki/stock-web", "notes": "No corporate-action candidate in profile. Hanyang Securities has a clean 2024/2025 forward path in stock-web. Source-proxy only, so no production weight delta."}
{"row_type": "case", "case_id": "R12L96_C32_YTN_2024_MEDIA_PRIVATIZATION_CONTROL_FALSE_STAGE2", "symbol": "040300", "company_name": "YTN", "round": "R12", "loop": "96", "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP", "fine_archetype_id": "SECURITIES_SALE_CONTROL_PREMIUM_BRIDGE_VS_MEDIA_PRIVATIZATION_FALSE_STAGE2_AND_BIO_HOLDCO_MERGER_CONTROL_EVENT_CAP", "case_type": "failed_rerating_media_privatization_control_bridge_missing", "positive_or_counterexample": "counterexample", "best_trigger": "R12L96_C32_YTN_2024_STAGE2_FALSE_POSITIVE_MEDIA_PRIVATIZATION_CONTROL_WATCH", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "Media privatization/control-premium watch had a short February spike but then de-rated sharply. C32 Stage2 should not be awarded without binding transaction economics, regulatory closing visibility, board/major-holder alignment, tender price floor, minority shareholder path and valuation revision bridge.", "current_profile_verdict": "current_profile_false_positive_if_media_privatization_control_watch_counts_without_binding_transaction_regulatory_closing_tender_price_floor_bridge", "price_source": "Songdaiki/stock-web", "notes": "No corporate-action candidate in profile. Source-proxy only."}
{"row_type": "case", "case_id": "R12L96_C32_HANMISCIENCE_2024_BIO_HOLDCO_MERGER_CONTROL_EVENT_CAP_4B", "symbol": "008930", "company_name": "한미사이언스", "round": "R12", "loop": "96", "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP", "fine_archetype_id": "SECURITIES_SALE_CONTROL_PREMIUM_BRIDGE_VS_MEDIA_PRIVATIZATION_FALSE_STAGE2_AND_BIO_HOLDCO_MERGER_CONTROL_EVENT_CAP", "case_type": "event_cap_4b_counterexample", "positive_or_counterexample": "counterexample", "best_trigger": "R12L96_C32_HANMISCIENCE_2024_STAGE4B_BIO_HOLDCO_MERGER_CONTROL_EVENT_CAP", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "Bio-holdco merger/control event premium capped at the January governance spike and then suffered deep MAE. C32 should route bridge-missing merger/control premiums to 4B unless merger certainty, board control, shareholder vote, litigation/regulatory path, transaction-price floor and closing bridge remain visible.", "current_profile_verdict": "current_profile_4B_too_late_if_bio_holdco_merger_control_event_premium_not_capped", "price_source": "Songdaiki/stock-web", "notes": "Selected 2024 window clean after old 1999/2010/2012 corporate-action candidates. Source-proxy only."}
```

### 25.3 trigger rows

```jsonl
{"row_type": "trigger", "trigger_id": "R12L96_C32_HANYANGSEC_2024_STAGE2_ACTIONABLE_SECURITIES_SALE_CONTROL_PREMIUM_BRIDGE", "case_id": "R12L96_C32_HANYANGSEC_2024_SECURITIES_SALE_CONTROL_PREMIUM_BRIDGE_POSITIVE", "symbol": "001750", "company_name": "한양증권", "round": "R12", "loop": "96", "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP", "fine_archetype_id": "SECURITIES_SALE_CONTROL_PREMIUM_BRIDGE_VS_MEDIA_PRIVATIZATION_FALSE_STAGE2_AND_BIO_HOLDCO_MERGER_CONTROL_EVENT_CAP", "sector": "securities_company_sale_control_premium_transaction_process", "primary_archetype": "sale_process_bidder_board_major_holder_regulatory_closing_price_floor_bridge", "loop_objective": "coverage_gap_fill | counterexample_mining | stage2_actionable_bonus_stress_test | 4B_non_price_requirement_stress_test | high_MAE_guardrail | tender_cap_guardrail | canonical_archetype_compression", "trigger_type": "Stage2-Actionable", "trigger_date": "2024-07-10", "entry_date": "2024-07-10", "entry_price": 11700.0, "evidence_available_at_that_date": "securities-company sale process / control-premium watch with credible bidder set, major-holder intent, board process and closing-price floor proxy; exact as-of source URL pending", "evidence_source": "source_proxy_historical_public_news_proxy", "stage2_evidence_fields": ["sale_process_proxy", "bidder_set_proxy", "major_holder_intent_proxy", "regulatory_closing_path_proxy", "transaction_price_floor_proxy"], "stage3_evidence_fields": ["strong_MFE30", "strong_MFE90", "controlled_MAE90"], "stage4b_evidence_fields": ["later_sale_process_tender_cap_watch", "post_peak_recheck"], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/001/001750/2024.csv", "profile_path": "atlas/symbol_profiles/001/001750.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": 65.9, "MFE_90D_pct": 65.9, "MFE_180D_pct": 65.9, "MFE_1Y_pct": "not_calculated", "MFE_2Y_pct": "not_calculated", "MAE_30D_pct": -1.79, "MAE_90D_pct": -1.79, "MAE_180D_pct": -3.42, "MAE_1Y_pct": "not_calculated", "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2024-08-05", "peak_price": 19410.0, "drawdown_after_peak_pct": -41.73, "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": null, "four_b_full_window_peak_proximity": null, "four_b_timing_verdict": "positive_stage2_but_later_sale_process_tender_cap_valuation_watch_needed", "four_b_evidence_type": ["sale_process_bridge", "bidder_transaction_floor", "tender_cap_watch"], "four_c_protection_label": "not_applicable", "trigger_outcome_label": "good_stage2_securities_sale_control_premium_bridge_success", "current_profile_verdict": "current_profile_kept_but_source_proxy_blocks_positive_delta", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window_no_CA_candidate", "same_entry_group_id": "R12L96_C32_001750_2024-07-10_11700", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false, "evidence_url_pending": true, "source_proxy_only": true}
{"row_type": "trigger", "trigger_id": "R12L96_C32_YTN_2024_STAGE2_FALSE_POSITIVE_MEDIA_PRIVATIZATION_CONTROL_WATCH", "case_id": "R12L96_C32_YTN_2024_MEDIA_PRIVATIZATION_CONTROL_FALSE_STAGE2", "symbol": "040300", "company_name": "YTN", "round": "R12", "loop": "96", "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP", "fine_archetype_id": "SECURITIES_SALE_CONTROL_PREMIUM_BRIDGE_VS_MEDIA_PRIVATIZATION_FALSE_STAGE2_AND_BIO_HOLDCO_MERGER_CONTROL_EVENT_CAP", "sector": "media_privatization_control_premium_regulatory_closing_watch", "primary_archetype": "media_privatization_watch_without_binding_transaction_closing_price_floor_bridge", "loop_objective": "coverage_gap_fill | counterexample_mining | stage2_actionable_bonus_stress_test | 4B_non_price_requirement_stress_test | high_MAE_guardrail | tender_cap_guardrail | canonical_archetype_compression", "trigger_type": "Stage2-Actionable", "trigger_date": "2024-02-05", "entry_date": "2024-02-05", "entry_price": 5840.0, "evidence_available_at_that_date": "media privatization/control-premium watch without binding transaction price, closing path, tender floor, shareholder path or valuation revision bridge; exact as-of source URL pending", "evidence_source": "source_proxy_historical_public_news_proxy", "stage2_evidence_fields": ["media_privatization_watch", "control_premium_theme", "relative_strength_spike"], "stage3_evidence_fields": [], "stage4b_evidence_fields": ["brief_MFE_then_deep_MAE", "binding_transaction_price_floor_bridge_missing"], "stage4c_evidence_fields": ["regulatory_closing_watch_only"], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/040/040300/2024.csv", "profile_path": "atlas/symbol_profiles/040/040300.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": 12.67, "MFE_90D_pct": 12.67, "MFE_180D_pct": 12.67, "MFE_1Y_pct": "not_calculated", "MFE_2Y_pct": "not_calculated", "MAE_30D_pct": -17.98, "MAE_90D_pct": -32.28, "MAE_180D_pct": -32.28, "MAE_1Y_pct": "not_calculated", "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2024-02-07", "peak_price": 6580.0, "drawdown_after_peak_pct": -39.82, "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": 0.89, "four_b_full_window_peak_proximity": 0.89, "four_b_timing_verdict": "media_privatization_watch_was_false_stage2_due_missing_binding_transaction_closing_price_floor_bridge", "four_b_evidence_type": ["control_premium_event", "bridge_missing", "brief_MFE"], "four_c_protection_label": "regulatory_closing_watch_only", "trigger_outcome_label": "bad_stage2_media_privatization_control_watch_without_transaction_closing_bridge", "current_profile_verdict": "current_profile_false_positive_if_media_privatization_control_watch_counts_without_binding_transaction_regulatory_closing_tender_price_floor_bridge", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window_no_CA_candidate", "same_entry_group_id": "R12L96_C32_040300_2024-02-05_5840", "dedupe_for_aggregate": true, "aggregate_group_role": "representative_false_stage2", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false, "evidence_url_pending": true, "source_proxy_only": true}
{"row_type": "trigger", "trigger_id": "R12L96_C32_HANMISCIENCE_2024_STAGE4B_BIO_HOLDCO_MERGER_CONTROL_EVENT_CAP", "case_id": "R12L96_C32_HANMISCIENCE_2024_BIO_HOLDCO_MERGER_CONTROL_EVENT_CAP_4B", "symbol": "008930", "company_name": "한미사이언스", "round": "R12", "loop": "96", "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP", "fine_archetype_id": "SECURITIES_SALE_CONTROL_PREMIUM_BRIDGE_VS_MEDIA_PRIVATIZATION_FALSE_STAGE2_AND_BIO_HOLDCO_MERGER_CONTROL_EVENT_CAP", "sector": "bio_holdco_merger_control_premium_event", "primary_archetype": "bio_holdco_merger_control_event_cap_4B", "loop_objective": "coverage_gap_fill | counterexample_mining | stage2_actionable_bonus_stress_test | 4B_non_price_requirement_stress_test | high_MAE_guardrail | tender_cap_guardrail | canonical_archetype_compression", "trigger_type": "Stage4B", "trigger_date": "2024-01-16", "entry_date": "2024-01-16", "entry_price": 56200.0, "evidence_available_at_that_date": "bio-holdco merger/control event premium after January governance spike without confirmed vote, litigation/regulatory path, transaction price floor or closing bridge; exact as-of source URL pending", "evidence_source": "source_proxy_historical_public_news_proxy", "stage2_evidence_fields": ["bio_holdco_merger_event", "control_premium_theme", "relative_strength_spike"], "stage3_evidence_fields": [], "stage4b_evidence_fields": ["event_premium_cap", "deep_MAE30", "deep_MAE90", "shareholder_vote_litigation_closing_bridge_recheck"], "stage4c_evidence_fields": ["control_thesis_break_watch_only"], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/008/008930/2024.csv", "profile_path": "atlas/symbol_profiles/008/008930.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": 0.0, "MFE_90D_pct": 0.0, "MFE_180D_pct": 0.0, "MFE_1Y_pct": "not_calculated", "MFE_2Y_pct": "not_calculated", "MAE_30D_pct": -30.43, "MAE_90D_pct": -37.9, "MAE_180D_pct": -37.9, "MAE_1Y_pct": "not_calculated", "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2024-01-16", "peak_price": 56200.0, "drawdown_after_peak_pct": -37.9, "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": 1.0, "four_b_full_window_peak_proximity": 1.0, "four_b_timing_verdict": "good_full_window_4B_timing_bio_holdco_merger_control_event_cap", "four_b_evidence_type": ["merger_control_event_premium", "positioning_overheat", "price_only"], "four_c_protection_label": "control_thesis_break_watch_only", "trigger_outcome_label": "event_cap_4B_success_bio_holdco_merger_control_event_premium", "current_profile_verdict": "current_profile_4B_too_late_if_bio_holdco_merger_control_event_premium_not_capped", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window_after_old_1999_2010_2012_CA", "same_entry_group_id": "R12L96_C32_008930_2024-01-16_56200", "dedupe_for_aggregate": false, "aggregate_group_role": "4B_overlay_only", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false, "evidence_url_pending": true, "source_proxy_only": true}
```

### 25.4 score_simulation rows

```jsonl
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R12L96_C32_HANYANGSEC_2024_SECURITIES_SALE_CONTROL_PREMIUM_BRIDGE_POSITIVE", "trigger_id": "R12L96_C32_HANYANGSEC_2024_STAGE2_ACTIONABLE_SECURITIES_SALE_CONTROL_PREMIUM_BRIDGE", "symbol": "001750", "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP", "raw_component_scores_before": {"contract_score": 25, "backlog_visibility_score": 25, "margin_bridge_score": 20, "revision_score": 35, "relative_strength_score": 65, "customer_quality_score": 35, "policy_or_regulatory_score": 45, "valuation_repricing_score": 65, "execution_risk_score": 55, "legal_or_contract_risk_score": 35, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 5}, "weighted_score_before": 66, "stage_label_before": "Stage2-Watch", "raw_component_scores_after": {"contract_score": 55, "backlog_visibility_score": 45, "margin_bridge_score": 30, "revision_score": 60, "relative_strength_score": 75, "customer_quality_score": 50, "policy_or_regulatory_score": 55, "valuation_repricing_score": 55, "execution_risk_score": 35, "legal_or_contract_risk_score": 25, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_after": 78, "stage_label_after": "Stage2-Actionable", "changed_components": ["contract_score", "backlog_visibility_score", "revision_score", "relative_strength_score", "customer_quality_score", "execution_risk_score"], "component_delta_explanation": "securities_sale_control_premium_positive", "MFE_90D_pct": 65.9, "MAE_90D_pct": -1.79, "score_return_alignment_label": "securities_sale_control_premium_positive", "current_profile_verdict": "current_profile_kept_but_source_proxy_blocks_positive_delta"}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R12L96_C32_YTN_2024_MEDIA_PRIVATIZATION_CONTROL_FALSE_STAGE2", "trigger_id": "R12L96_C32_YTN_2024_STAGE2_FALSE_POSITIVE_MEDIA_PRIVATIZATION_CONTROL_WATCH", "symbol": "040300", "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP", "raw_component_scores_before": {"contract_score": 20, "backlog_visibility_score": 20, "margin_bridge_score": 15, "revision_score": 25, "relative_strength_score": 70, "customer_quality_score": 25, "policy_or_regulatory_score": 60, "valuation_repricing_score": 60, "execution_risk_score": 60, "legal_or_contract_risk_score": 45, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 5}, "weighted_score_before": 66, "stage_label_before": "Stage2-Actionable", "raw_component_scores_after": {"contract_score": 5, "backlog_visibility_score": 5, "margin_bridge_score": 0, "revision_score": 5, "relative_strength_score": 20, "customer_quality_score": 10, "policy_or_regulatory_score": 25, "valuation_repricing_score": 25, "execution_risk_score": 90, "legal_or_contract_risk_score": 60, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 10}, "weighted_score_after": 52, "stage_label_after": "Stage1/Watch", "changed_components": ["contract_score", "revision_score", "relative_strength_score", "policy_or_regulatory_score", "valuation_repricing_score", "execution_risk_score"], "component_delta_explanation": "media_privatization_control_false_stage2", "MFE_90D_pct": 12.67, "MAE_90D_pct": -32.28, "score_return_alignment_label": "media_privatization_control_false_stage2", "current_profile_verdict": "current_profile_false_positive_if_media_privatization_control_watch_counts_without_binding_transaction_regulatory_closing_tender_price_floor_bridge"}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R12L96_C32_HANMISCIENCE_2024_BIO_HOLDCO_MERGER_CONTROL_EVENT_CAP_4B", "trigger_id": "R12L96_C32_HANMISCIENCE_2024_STAGE4B_BIO_HOLDCO_MERGER_CONTROL_EVENT_CAP", "symbol": "008930", "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP", "raw_component_scores_before": {"contract_score": 20, "backlog_visibility_score": 20, "margin_bridge_score": 10, "revision_score": 25, "relative_strength_score": 70, "customer_quality_score": 25, "policy_or_regulatory_score": 60, "valuation_repricing_score": 65, "execution_risk_score": 60, "legal_or_contract_risk_score": 55, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 5}, "weighted_score_before": 70, "stage_label_before": "Stage3-Yellow-like", "raw_component_scores_after": {"contract_score": 5, "backlog_visibility_score": 5, "margin_bridge_score": 0, "revision_score": 5, "relative_strength_score": 20, "customer_quality_score": 5, "policy_or_regulatory_score": 25, "valuation_repricing_score": 25, "execution_risk_score": 90, "legal_or_contract_risk_score": 70, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 10}, "weighted_score_after": 54, "stage_label_after": "Stage4B-watch", "changed_components": ["contract_score", "revision_score", "relative_strength_score", "valuation_repricing_score", "execution_risk_score", "legal_or_contract_risk_score"], "component_delta_explanation": "bio_holdco_merger_control_event_cap_4B_guard", "MFE_90D_pct": 0.0, "MAE_90D_pct": -37.9, "score_return_alignment_label": "bio_holdco_merger_control_event_cap_4B_guard", "current_profile_verdict": "current_profile_4B_too_late_if_bio_holdco_merger_control_event_premium_not_capped"}
```

### 25.5 residual_contribution row

```jsonl
{"row_type": "residual_contribution", "round": "R12", "loop": "96", "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP", "fine_archetype_id": "SECURITIES_SALE_CONTROL_PREMIUM_BRIDGE_VS_MEDIA_PRIVATIZATION_FALSE_STAGE2_AND_BIO_HOLDCO_MERGER_CONTROL_EVENT_CAP", "new_independent_case_count": 3, "reused_case_count": 0, "new_symbol_count": 3, "same_archetype_new_symbol_count": 3, "same_archetype_new_trigger_family_count": 3, "new_trigger_family_count": 3, "positive_case_count": 1, "counterexample_count": 2, "4B_case_count": 1, "4C_case_count": 0, "tested_existing_calibrated_axes": ["stage2_required_bridge", "local_4b_watch_guard", "tender_cap_guardrail", "full_4b_requires_non_price_evidence", "price_only_blowoff_blocks_positive_stage", "high_MAE_guardrail"], "residual_error_types_found": ["securities_sale_control_premium_positive", "media_privatization_control_false_stage2", "bio_holdco_merger_control_event_cap_4B"], "loop_contribution_label": "canonical_archetype_rule_candidate", "do_not_propose_new_weight_delta": true, "source_proxy_only_count": 3, "evidence_url_pending_count": 3}
```

### 25.6 narrative_only row

```jsonl
{"row_type":"narrative_only","case_id":"none","symbol":"none","large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP","reason":"all selected rows have usable 180D stock-web windows; no narrative-only price row required","price_source":"Songdaiki/stock-web","usage":"not_weight_calibration"}
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
- Do not apply global deltas unless multiple large_sector_id values support the same direction.
- Positive score promotion requires non-price evidence and clean 180D MFE/MAE.
- 4B rows are overlay/risk calibration only.
- 4C rows are thesis-break/protection calibration only.
- False-positive rows should strengthen bridge requirements, not generate positive promotion.
- C32 rows need explicit binding process, credible bidder/counterparty, board/major-holder intent, regulatory/closing visibility, tender or transaction-price floor, minority shareholder path, or valuation discipline before positive promotion.
- In C32, bridge-missing control-premium event rows with low MFE/high MAE should route to 4B/watch, not Stage3.
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
10. Add tests that bridge-missing C32 governance/control-premium rows cannot promote positive stages.

### Expected output

- Concise implementation summary.
- Rows accepted/rejected.
- New sector/canonical archetype coverage.
- Existing axis strengthened/weakened/kept.
- No investment recommendation language.

## 27. Next Round State

```text
completed_round = R12
completed_loop = 96
next_round = R13
next_loop = 96
round_schedule_status = valid
round_sector_consistency = pass
```

## 28. Source Notes

- Main execution prompt: Songdaiki/stock_agent docs/core/e2r_v12_prompt_round_scheduler_corrected.txt.
- No-repeat index: Songdaiki/stock_agent docs/core/V12_Research_No_Repeat_Index.md.
- Price atlas: Songdaiki/stock-web atlas/manifest.json and per-symbol tradable shards.
- This file contains no investment recommendation and no production scoring change.
