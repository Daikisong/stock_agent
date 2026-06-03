# E2R Stock-Web Historical Calibration / Sector-Archetype Residual Research Round

## 0. Research Metadata

```text
mode = historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12
research_session = post_calibrated_sector_archetype_residual_research
repo_session = later_batch_implementation_only
output_format = one_standalone_markdown_file
production_scoring_changed = false
shadow_weight_only = true
handoff_prompt_embedded = true
handoff_prompt_executed_now = false
created_at = 2026-05-25T11:25:00
```

This file is historical calibration research, not a live stock screen, not an investment recommendation, and not a repository patch.

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

The loop does **not** re-propose the already-applied global rules. It stress-tests whether governance/control-premium events still create a residual false-positive path when the event premium is visually explosive but not backed by revision, margin bridge, order backlog, or cash-flow improvement.

## 2. Round / Large Sector / Canonical Archetype Scope

```text
round = R12
loop = 10
large_sector_id = L10_POLICY_EVENT_CROSS_REDTEAM_MISC
canonical_archetype_id = C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP
fine_archetype_id = HOSTILE_TENDER_CONTROL_PREMIUM_CAP_VS_EPS_RERATING_FALSE_GREEN
loop_objective = counterexample_mining | residual_false_positive_mining | 4B_non_price_requirement_stress_test | sector_specific_rule_discovery | canonical_archetype_compression | coverage_gap_fill
```

The selected archetype is the R12 misc/governance residual: the “event tail wagging the evidence dog” problem: a tender/control premium can make price behave like a rerating for a short window, but the mechanism is different from E2R’s EPS/FCF rerating.

## 3. Previous Coverage / Duplicate Avoidance Check

Accessible ingest artifacts showed broad R1~R13 and loop 1~9 coverage, but the visible registry slice did not show a dedicated v12 residual row for `C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP` after the R8/R9/R10/R11 v12 files created in this session. The ingest summary also shows older results were broad and many rows were rejected for price-source/schema reasons. fileciteturn55file0

Novelty gate:

| metric | value |
|---|---:|
| new_independent_case_count | 3 |
| reused_case_count | 0 |
| new_symbol_count | 3 |
| same_archetype_new_symbol_count | 3 |
| same_archetype_new_trigger_family_count | 3 |
| new_canonical_archetype_count | 1 |
| positive_case_count | 1 |
| counterexample_count | 2 |
| calibration_usable_case_count | 3 |
| new_independent_case_ratio | 1.00 |

No reused symbol/entry group is counted as independent evidence.

## 4. Stock-Web OHLC Input / Price Source Validation

The price source is `Songdaiki/stock-web`, using FinanceData/marcap transformed into symbol-year CSV shards. The manifest reports `max_date = 2026-02-20`, `tradable_row_count = 14,354,401`, `symbol_count = 5,414`, `calibration_shard_root = atlas/ohlcv_tradable_by_symbol_year`, and `price_adjustment_status = raw_unadjusted_marcap`. fileciteturn82file0

The schema defines tradable shard columns `d/o/h/l/c/v/a/mc/s/m`, raw shard columns with additional `rs`, `calibration_basis = tradable_raw`, and the MFE/MAE formula used here. fileciteturn83file0

```json
{"row_type": "price_source_validation", "source": "Songdaiki/stock-web", "source_url": "https://github.com/Songdaiki/stock-web", "manifest_path": "atlas/manifest.json", "schema_path": "atlas/schema.json", "universe_path": "atlas/universe/all_symbols.csv", "manifest_max_date": "2026-02-20", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "raw_shard_root": "atlas/ohlcv_raw_by_symbol_year", "validation_status": "usable_for_historical_calibration"}
```

## 5. Historical Eligibility Gate

| symbol | profile path | profile caveat | 180D status | calibration usable |
|---|---|---|---|---|
| 010130 | atlas/symbol_profiles/010/010130.json | no corporate-action candidate dates | clean | true |
| 041510 | atlas/symbol_profiles/041/041510.json | old corporate-action candidates only, outside tested window | clean | true |
| 000240 | atlas/symbol_profiles/000/000240.json | old corporate-action candidates only, outside tested window | clean | true |

Korea Zinc profile shows no corporate-action candidate dates and `raw_unadjusted_marcap` status. fileciteturn84file0
SM profile shows corporate-action candidates only in 2002/2005, outside the 2023 test window. fileciteturn85file0
Hankook & Company profile shows corporate-action candidates before 2014, outside the 2023/2024 test window. fileciteturn86file0

## 6. Canonical Archetype Compression Map

| fine_archetype_id | canonical_archetype_id | compression reason |
|---|---|---|
| HOSTILE_TENDER_CONTROL_PREMIUM_CAP_VS_EPS_RERATING_FALSE_GREEN | C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP | Tender offers, control fights, buyback counteroffers, and white-knight bids share the same failure mode: price can gap like a rerating without an EPS/FCF bridge. |

## 7. Case Selection Summary

| case_id | symbol | company | role | event trigger | why included |
|---|---:|---|---|---|---|
| R12L10C32_KZINC_2024_TENDER_CONTROL_PREMIUM | 010130 | 고려아연 | positive event premium / 4B overlay | 2024-09-13 hostile tender | Explosive control-premium MFE, but non-price 4B needed to avoid treating it as structural Green. |
| R12L10C32_SM_2023_HYBE_KAKAO_TENDER_BATTLE | 041510 | 에스엠 | counterexample | 2023-02-10 / 2023-03 tender battle | Fast event peak, then tender-cap reversion; strategic buyer quality was not an operating revision. |
| R12L10C32_HANKOOK_2023_MBK_TENDER_FAILED | 000240 | 한국앤컴퍼니 | counterexample | 2023-12-05 tender/control premium | Small MFE and large MAE after event premium faded. |

## 8. Positive vs Counterexample Balance

```text
positive_case_count = 1
counterexample_count = 2
4B_case_count = 3
4C_case_count = 2
calibration_usable_case_count = 3
```

The positive case is positive only as **event-premium path validation**, not as structural Stage3 training evidence. The two counterexamples show why C32 should be an overlay/guard archetype rather than an EPS rerating archetype.

## 9. Evidence Source Map

| case | trigger evidence | public source note |
|---|---|---|
| 고려아연 | MBK/Young Poong tender offer at 660,000 KRW; target called it hostile. | Reuters reported the tender and the 19.8% share surge on 2024-09-13. citeturn686297news0 |
| 고려아연 4B watch | Court allowed Korea Zinc buyback offer; price closed near 877,000 KRW and tender offer price context became explicit. | Reuters described the court ruling and 877,000 KRW close on 2024-10-21. citeturn686297news2 |
| 에스엠 | Kakao tender at 150,000 KRW after HYBE/SM control battle. | AP reported Kakao’s 35% tender offer at 150,000 KRW and HYBE’s earlier failed 120,000 KRW tender. citeturn686297news1 |
| 한국앤컴퍼니 | MBK-related tender/control premium window, then failure/reversion. | Event-level source is treated as public/regulatory context; calibration weight is based on stock-web price path, not source narrative. |

## 10. Price Data Source Map

| symbol | entry shard | supporting shard | profile |
|---:|---|---|---|
| 010130 | atlas/ohlcv_tradable_by_symbol_year/010/010130/2024.csv | atlas/ohlcv_tradable_by_symbol_year/010/010130/2025.csv | atlas/symbol_profiles/010/010130.json |
| 041510 | atlas/ohlcv_tradable_by_symbol_year/041/041510/2023.csv | n/a | atlas/symbol_profiles/041/041510.json |
| 000240 | atlas/ohlcv_tradable_by_symbol_year/000/000240/2023.csv | atlas/ohlcv_tradable_by_symbol_year/000/000240/2024.csv | atlas/symbol_profiles/000/000240.json |

Korea Zinc 2024 rows contain the 2024-09-13 entry close at 666,000 KRW, the 2024-10-29 high at 1,543,000 KRW, and the 2024-12-06 high at 2,407,000 KRW. fileciteturn87file0
Korea Zinc 2025 rows contain the 2025-04-09 low at 643,000 KRW within the 180D observed window from the 2024-09 entry. fileciteturn88file0
SM 2023 rows contain the 2023-02-10 entry close at 114,700 KRW, 2023-03-08 high at 161,200 KRW, and 2023-03-27 low at 90,500 KRW. fileciteturn89file0
SM late-2023 rows show the post-event fade toward 82,500~90,000 KRW range by December. fileciteturn90file0
Hankook & Company 2023 rows contain the 2023-12-05 entry close at 21,850 KRW, 2023-12-07 high at 23,750 KRW, and December reversion. fileciteturn91file0
Hankook & Company 2024 rows show the subsequent low path into the 14,600~15,000 KRW zone. fileciteturn92file0

## 11. Case-by-Case Trigger Grid

| trigger_id | symbol | trigger_type | trigger_date | entry_date | entry_price | current_profile_verdict | representative |
|---|---:|---|---|---|---:|---|---|
| R12L10C32_KZINC_T1_STAGE2_EVENT_2024_09_13 | 010130 | Stage2-Actionable | 2024-09-13 | 2024-09-13 | 666000 | current_profile_false_positive | true |
| R12L10C32_SM_T1_STAGE2_EVENT_2023_02_10 | 041510 | Stage2-Actionable | 2023-02-10 | 2023-02-10 | 114700 | current_profile_false_positive | true |
| R12L10C32_HANKOOK_T1_STAGE2_EVENT_2023_12_05 | 000240 | Stage2-Actionable | 2023-12-05 | 2023-12-05 | 21850 | current_profile_false_positive | true |

## 12. Trigger-Level OHLC Backtest Tables

| symbol | entry | entry_price | MFE_30D | MAE_30D | MFE_90D | MAE_90D | MFE_180D | MAE_180D | peak_date | peak_price | drawdown_after_peak |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---|---:|---:|
| 010130 | 2024-09-13 | 666000 | 131.68% | -1.65% | 261.41% | -1.65% | 261.41% | -3.45% | 2024-12-06 | 2407000 | -73.29% |
| 041510 | 2023-02-10 | 114700 | 40.54% | -9.24% | 40.54% | -21.10% | 40.54% | -21.10% | 2023-03-08 | 161200 | -43.86% |
| 000240 | 2023-12-05 | 21850 | 8.70% | -32.04% | 8.70% | -33.14% | 8.70% | -33.18% | 2023-12-07 | 23750 | -38.53% |

## 13. Current Calibrated Profile Stress Test

| case | current calibrated profile likely behavior | backtest alignment | verdict |
|---|---|---|---|
| 고려아연 | Price/action/event evidence may look like strong Stage2/Yellow if event premium is not separated. | MFE was huge, but the mechanism was control-premium/offer escalation; post-peak drawdown was severe. | current_profile_false_positive |
| 에스엠 | Strategic acquirer quality and price strength could be overread as rerating. | The tender price acted as a cap; price reverted after event resolution. | current_profile_false_positive |
| 한국앤컴퍼니 | Tender headline could generate Stage2 event score. | MFE was only +8.70%, while 30D/90D MAE exceeded -32%. | current_profile_false_positive |

Answers to v12 stress-test questions:

1. The current profile should avoid Stage3 Green because revision/margin/backlog evidence is absent.
2. The actual MFE/MAE confirms that control-premium price action alone is not enough for positive stage training.
3. Stage2 actionable bonus is not globally wrong, but for C32 it needs an event-only lane.
4. Yellow threshold 75 is too permissive if event premium contributes like structural valuation repricing.
5. Green 87 / revision 55 is appropriate; C32 should require realized operating revision before Green.
6. price-only blowoff guard is appropriate, but C32 needs more than price-only: even non-price tender evidence is still not EPS evidence.
7. full 4B non-price requirement is strengthened, but full-window timing can still be too early.
8. hard 4C routing should treat failed offer/withdrawn control path as event-thesis break.

## 14. Stage2 / Yellow / Green Comparison

No case receives a confirmed Stage3-Green trigger under the proposed C32 guard. All three cases can be Stage2 event-watch rows, but none should become Green without:

```text
confirmed_revision
margin_bridge
financial_visibility
durable_customer_confirmation
low_red_team_risk
```

`green_lateness_ratio = not_applicable` for all three because the correct conclusion is not “Green was late”; it is “Green should not be emitted from a tender/control-premium event alone.”

## 15. 4B Local vs Full-window Timing Audit

| symbol | Stage2 entry | candidate 4B date | 4B entry price | local proximity | full-window proximity | verdict |
|---:|---|---|---:|---:|---:|---|
| 010130 | 2024-09-13 | 2024-10-21 | 877000 | 0.24 | 0.12 | non-price 4B watch, too early for full-window exit |
| 041510 | 2023-02-10 | 2023-03-07 | 149700 | 0.94 | 0.94 | good local event cap, not positive stage |
| 000240 | 2023-12-05 | 2023-12-07 | 22100 | 0.13 | 0.13 | event cap too early, failed after offer window |

C32 teaches a narrower point than the global 4B rule: full 4B should require non-price evidence, but control-premium non-price evidence can still be a **local event cap**, not a full-cycle peak.

## 16. 4C Protection Audit

| case | 4C-like break | protection label |
|---|---|---|
| 고려아연 | drawdown after 2024-12-06 event blowoff reached roughly -73% within observed path | thesis_break_watch_only |
| 에스엠 | post-tender reversion after control battle resolution | hard_4c_success |
| 한국앤컴퍼니 | tender premium failed quickly; MAE exceeded -33% while MFE was only +8.7% | hard_4c_success |

## 17. Sector-Specific Rule Candidate

```text
rule_scope = sector_specific
large_sector_id = L10_POLICY_EVENT_CROSS_REDTEAM_MISC
axis = l10_control_premium_event_overlay_cap
candidate_delta = +1 guard / -15 positive-stage cap
```

Sector rule:

> In L10 policy/event/cross-redteam cases, tender/control-premium evidence may create Stage2 event-watch and 4B overlay rows, but it cannot promote Stage3-Yellow/Green unless at least one non-event operating bridge is present: confirmed revision, margin bridge, backlog/order conversion, or FCF improvement.

## 18. Canonical-Archetype Rule Candidate

```text
rule_scope = canonical_archetype_specific
canonical_archetype_id = C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP
axis = c32_tender_premium_positive_stage_cap
candidate_delta = cap valuation_repricing contribution to <= 40 unless operating evidence exists
```

Canonical rule:

> For C32, control premium, tender price, buyback counteroffer, white-knight bid, court ruling, and governance contest are event-premium evidence. They can strengthen `four_b_evidence_type`, but they should not be counted as structural valuation rerating for Stage3 unless supported by `revision_score >= 55` or an explicit operating/cash-flow bridge.

## 19. Before / After Backtest Comparison

| profile_id | scope | eligible triggers | avg MFE90 | avg MAE90 | false positive rate | score-return alignment |
|---|---|---:|---:|---:|---:|---|
| P0 e2r_2_1_stock_web_calibrated_proxy | current | 3 | 103.55% | -18.63% | 0.67 | weak: event premiums pollute positive-stage evidence |
| P0b e2r_2_0_baseline_reference | rollback | 3 | 103.55% | -18.63% | 1.00 | weaker: would over-trust price and event headlines |
| P1 sector_specific_candidate_profile | L10 | 3 | 103.55% event-observed | -18.63% | 0.00 for positive-stage training | stronger: routes C32 to event overlay |
| P2 canonical_archetype_candidate_profile | C32 | 3 | 103.55% event-observed | -18.63% | 0.00 for positive-stage training | strongest: caps tender premium |
| P3 counterexample_guard_profile | C32 guard | 2 counterexamples | 24.62% | -27.12% | 0.00 | prevents failed tender false Green |

## 20. Score-Return Alignment Matrix

| case | before score/stage | after score/stage | MFE90 | MAE90 | alignment |
|---|---|---|---:|---:|---|
| 고려아연 | 78 / Stage3-Yellow if event premium misread | 63 / 4B-watch event overlay | 261.41% | -1.65% | event premium valid, positive-stage invalid |
| 에스엠 | 76 / Yellow if strategic buyer overread | 58 / event overlay only | 40.54% | -21.10% | after better matches tender-cap reversion |
| 한국앤컴퍼니 | 72 / Stage2 or Yellow if headline overweighted | 49 / event overlay only | 8.70% | -33.14% | after avoids false positive |

## 21. Coverage Matrix

| large_sector_id | canonical_archetype_id | fine_archetype_id | positive_case_count | counterexample_count | 4B_case_count | 4C_case_count | new_independent_case_count | reused_case_count | calibration_usable_trigger_count | representative_trigger_count | current_profile_error_count | sector_rule_candidate | canonical_rule_candidate | coverage_gap_after_this_loop |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|---|---|
| L10_POLICY_EVENT_CROSS_REDTEAM_MISC | C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP | HOSTILE_TENDER_CONTROL_PREMIUM_CAP_VS_EPS_RERATING_FALSE_GREEN | 1 | 2 | 3 | 2 | 3 | 0 | 3 | 3 | 3 | true | true | still needs non-Korea tender holdout and delisting/take-private examples |

## 22. Residual Contribution Summary

```text
new_independent_case_count: 3
reused_case_count: 0
reused_case_ids: []
new_symbol_count: 3
same_archetype_new_symbol_count: 3
same_archetype_new_trigger_family_count: 3
new_canonical_archetype_count: 1
new_fine_archetype_count: 1
new_trigger_family_count: 3
tested_existing_calibrated_axes: price_only_blowoff_blocks_positive_stage, full_4b_requires_non_price_evidence, stage3_green_revision_min
residual_error_types_found: control_premium_false_positive, event_cap_reversion, 4B_full_window_too_early
new_axis_proposed: c32_tender_premium_positive_stage_cap | c32_event_overlay_not_structural_rerating
existing_axis_strengthened: full_4b_requires_non_price_evidence in C32; stage3_green_revision_min in C32
existing_axis_weakened: null
existing_axis_kept: price_only_blowoff_blocks_positive_stage, hard_4c_thesis_break_routes_to_4c
sector_specific_rule_candidate: true
canonical_archetype_rule_candidate: true
no_new_signal_reason: null
loop_contribution_label: canonical_archetype_rule_candidate
do_not_propose_new_weight_delta: false
```

## 23. Validation Scope / Non-Validation Scope

Validated:

```text
- stock-web manifest/schema checked
- symbol profiles checked
- 180D windows available by manifest max_date
- trigger entry rows exist
- 30D / 90D / 180D MFE and MAE calculated from stock-web rows
- corporate-action contaminated windows not present for tested windows
- positive/counterexample balance satisfied
```

Not validated:

```text
- no production scoring code inspected
- no stock_agent source code inspected
- no live candidate scan
- no broker/API/autotrading action
- no recommendation language
```

## 24. Shadow Weight Calibration

```csv
row_type,axis,scope,large_sector_id,canonical_archetype_id,baseline_value,tested_value,delta,reason,backtest_effect,trigger_ids,calibration_usable_count,new_independent_case_count,counterexample_count,confidence,proposal_type,notes
shadow_weight,c32_tender_premium_positive_stage_cap,canonical_archetype_specific,L10_POLICY_EVENT_CROSS_REDTEAM_MISC,C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP,0,1,+1,"Tender/control premium should cap positive Stage3 unless revision or operating bridge exists","reduced false positive count from 3 to 0 for positive-stage training","R12L10C32_KZINC_T1_STAGE2_EVENT_2024_09_13|R12L10C32_SM_T1_STAGE2_EVENT_2023_02_10|R12L10C32_HANKOOK_T1_STAGE2_EVENT_2023_12_05",3,3,2,medium,canonical_shadow_only,"not production; post-calibrated residual"
shadow_weight,c32_event_overlay_not_structural_rerating,sector_specific,L10_POLICY_EVENT_CROSS_REDTEAM_MISC,C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP,0,1,+1,"C32 price jumps are event-premium overlays, not EPS/FCF rerating evidence","routes rows to 4B/event watch instead of Stage3-Green","R12L10C32_KZINC_T1_STAGE2_EVENT_2024_09_13|R12L10C32_SM_T1_STAGE2_EVENT_2023_02_10|R12L10C32_HANKOOK_T1_STAGE2_EVENT_2023_12_05",3,3,2,medium,sector_shadow_only,"requires batch promotion later"
```

## 25. Machine-Readable Rows

```jsonl
{"row_type": "price_source_validation", "source": "Songdaiki/stock-web", "source_url": "https://github.com/Songdaiki/stock-web", "manifest_path": "atlas/manifest.json", "schema_path": "atlas/schema.json", "universe_path": "atlas/universe/all_symbols.csv", "manifest_max_date": "2026-02-20", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "raw_shard_root": "atlas/ohlcv_raw_by_symbol_year", "validation_status": "usable_for_historical_calibration"}
{"row_type": "case", "case_id": "R12L10C32_KZINC_2024_TENDER_CONTROL_PREMIUM", "symbol": "010130", "company_name": "고려아연", "round": "R12", "loop": "10", "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP", "fine_archetype_id": "HOSTILE_TENDER_CONTROL_PREMIUM_CAP_VS_EPS_RERATING_FALSE_GREEN", "case_type": "4B_overlay_success", "positive_or_counterexample": "positive", "best_trigger": "R12L10C32_KZINC_T1_STAGE2_EVENT_2024_09_13", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "event_premium_exploded_then_large_post_peak_drawdown", "current_profile_verdict": "current_profile_false_positive", "price_source": "Songdaiki/stock-web", "notes": "MBK Partners/Young Poong hostile tender offer at 660,000 KRW; target publicly opposed the offer."}
{"row_type": "case", "case_id": "R12L10C32_SM_2023_HYBE_KAKAO_TENDER_BATTLE", "symbol": "041510", "company_name": "에스엠", "round": "R12", "loop": "10", "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP", "fine_archetype_id": "HOSTILE_TENDER_CONTROL_PREMIUM_CAP_VS_EPS_RERATING_FALSE_GREEN", "case_type": "failed_rerating", "positive_or_counterexample": "counterexample", "best_trigger": "R12L10C32_SM_T1_STAGE2_EVENT_2023_02_10", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "tender_cap_peak_then_reversion", "current_profile_verdict": "current_profile_false_positive", "price_source": "Songdaiki/stock-web", "notes": "HYBE founder-stake acquisition/tender battle followed by Kakao tender at 150,000 KRW; control premium became event cap rather than durable EPS rerating."}
{"row_type": "case", "case_id": "R12L10C32_HANKOOK_2023_MBK_TENDER_FAILED", "symbol": "000240", "company_name": "한국앤컴퍼니", "round": "R12", "loop": "10", "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP", "fine_archetype_id": "HOSTILE_TENDER_CONTROL_PREMIUM_CAP_VS_EPS_RERATING_FALSE_GREEN", "case_type": "failed_rerating", "positive_or_counterexample": "counterexample", "best_trigger": "R12L10C32_HANKOOK_T1_STAGE2_EVENT_2023_12_05", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "small_MFE_large_MAE_event_false_positive", "current_profile_verdict": "current_profile_false_positive", "price_source": "Songdaiki/stock-web", "notes": "MBK-related public tender/control-premium event lifted price briefly, but the price path failed to sustain without operating revision or successful control transfer."}
{"row_type": "trigger", "trigger_id": "R12L10C32_KZINC_T1_STAGE2_EVENT_2024_09_13", "case_id": "R12L10C32_KZINC_2024_TENDER_CONTROL_PREMIUM", "symbol": "010130", "company_name": "고려아연", "round": "R12", "loop": "10", "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP", "fine_archetype_id": "HOSTILE_TENDER_CONTROL_PREMIUM_CAP_VS_EPS_RERATING_FALSE_GREEN", "sector": "정책·지정학·재난·이벤트", "primary_archetype": "governance_control_premium_tender_cap", "loop_objective": "counterexample_mining|residual_false_positive_mining|4B_non_price_requirement_stress_test|sector_specific_rule_discovery|canonical_archetype_compression|coverage_gap_fill", "trigger_type": "Stage2-Actionable", "trigger_date": "2024-09-13", "evidence_available_at_that_date": "MBK Partners/Young Poong hostile tender offer at 660,000 KRW; target publicly opposed the offer.", "evidence_source": "Reuters 2024-09-13 and stock-web 010130 2024 shard", "stage2_evidence_fields": ["public_event_or_disclosure", "relative_strength", "policy_or_regulatory_optionality"], "stage3_evidence_fields": [], "stage4b_evidence_fields": ["valuation_blowoff", "positioning_overheat", "legal_or_regulatory_block"], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/010/010130/2024.csv", "profile_path": "atlas/symbol_profiles/010/010130.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "entry_date": "2024-09-13", "entry_price": 666000, "MFE_30D_pct": 131.68, "MFE_90D_pct": 261.41, "MFE_180D_pct": 261.41, "MFE_1Y_pct": 261.41, "MFE_2Y_pct": null, "MAE_30D_pct": -1.65, "MAE_90D_pct": -1.65, "MAE_180D_pct": -3.45, "MAE_1Y_pct": -3.45, "below_entry_price_flag_30D": false, "below_entry_price_flag_90D": false, "peak_date": "2024-12-06", "peak_price": 2407000, "drawdown_after_peak_pct": -73.29, "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": 0.24, "four_b_full_window_peak_proximity": 0.12, "four_b_timing_verdict": "non_price_4B_watch_too_early_for_full_window", "four_b_evidence_type": ["valuation_blowoff", "legal_or_regulatory_block", "positioning_overheat"], "four_c_protection_label": "thesis_break_watch_only", "trigger_outcome_label": "event_premium_exploded_then_large_post_peak_drawdown", "current_profile_verdict": "current_profile_false_positive", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window", "same_entry_group_id": "R12L10C32_010130_2024_09_13_666000", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false}
{"row_type": "trigger", "trigger_id": "R12L10C32_SM_T1_STAGE2_EVENT_2023_02_10", "case_id": "R12L10C32_SM_2023_HYBE_KAKAO_TENDER_BATTLE", "symbol": "041510", "company_name": "에스엠", "round": "R12", "loop": "10", "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP", "fine_archetype_id": "HOSTILE_TENDER_CONTROL_PREMIUM_CAP_VS_EPS_RERATING_FALSE_GREEN", "sector": "정책·지정학·재난·이벤트", "primary_archetype": "governance_control_premium_tender_cap", "loop_objective": "counterexample_mining|residual_false_positive_mining|4B_non_price_requirement_stress_test|sector_specific_rule_discovery|canonical_archetype_compression|coverage_gap_fill", "trigger_type": "Stage2-Actionable", "trigger_date": "2023-02-10", "evidence_available_at_that_date": "HYBE founder-stake acquisition/tender battle followed by Kakao tender at 150,000 KRW; control premium became event cap rather than durable EPS rerating.", "evidence_source": "AP 2023 Kakao tender article; stock-web 041510 2023 shard", "stage2_evidence_fields": ["public_event_or_disclosure", "relative_strength", "customer_or_order_quality"], "stage3_evidence_fields": [], "stage4b_evidence_fields": ["valuation_blowoff", "positioning_overheat", "explicit_event_cap"], "stage4c_evidence_fields": ["legal_or_contract_risk"], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/041/041510/2023.csv", "profile_path": "atlas/symbol_profiles/041/041510.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "entry_date": "2023-02-10", "entry_price": 114700, "MFE_30D_pct": 40.54, "MFE_90D_pct": 40.54, "MFE_180D_pct": 40.54, "MFE_1Y_pct": 40.54, "MFE_2Y_pct": null, "MAE_30D_pct": -9.24, "MAE_90D_pct": -21.1, "MAE_180D_pct": -21.1, "MAE_1Y_pct": -28.07, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2023-03-08", "peak_price": 161200, "drawdown_after_peak_pct": -43.86, "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": 0.94, "four_b_full_window_peak_proximity": 0.94, "four_b_timing_verdict": "good_local_event_cap_but_not_positive_stage", "four_b_evidence_type": ["valuation_blowoff", "explicit_event_cap", "positioning_overheat"], "four_c_protection_label": "hard_4c_success", "trigger_outcome_label": "tender_cap_peak_then_reversion", "current_profile_verdict": "current_profile_false_positive", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window", "same_entry_group_id": "R12L10C32_041510_2023_02_10_114700", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false}
{"row_type": "trigger", "trigger_id": "R12L10C32_HANKOOK_T1_STAGE2_EVENT_2023_12_05", "case_id": "R12L10C32_HANKOOK_2023_MBK_TENDER_FAILED", "symbol": "000240", "company_name": "한국앤컴퍼니", "round": "R12", "loop": "10", "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP", "fine_archetype_id": "HOSTILE_TENDER_CONTROL_PREMIUM_CAP_VS_EPS_RERATING_FALSE_GREEN", "sector": "정책·지정학·재난·이벤트", "primary_archetype": "governance_control_premium_tender_cap", "loop_objective": "counterexample_mining|residual_false_positive_mining|4B_non_price_requirement_stress_test|sector_specific_rule_discovery|canonical_archetype_compression|coverage_gap_fill", "trigger_type": "Stage2-Actionable", "trigger_date": "2023-12-05", "evidence_available_at_that_date": "MBK-related public tender/control-premium event lifted price briefly, but the price path failed to sustain without operating revision or successful control transfer.", "evidence_source": "public tender/regulatory news context; stock-web 000240 2023/2024 shards", "stage2_evidence_fields": ["public_event_or_disclosure", "relative_strength"], "stage3_evidence_fields": [], "stage4b_evidence_fields": ["valuation_blowoff", "explicit_event_cap", "positioning_overheat"], "stage4c_evidence_fields": ["thesis_evidence_broken"], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/000/000240/2023.csv", "profile_path": "atlas/symbol_profiles/000/000240.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "entry_date": "2023-12-05", "entry_price": 21850, "MFE_30D_pct": 8.7, "MFE_90D_pct": 8.7, "MFE_180D_pct": 8.7, "MFE_1Y_pct": 8.7, "MFE_2Y_pct": null, "MAE_30D_pct": -32.04, "MAE_90D_pct": -33.14, "MAE_180D_pct": -33.18, "MAE_1Y_pct": -33.18, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2023-12-07", "peak_price": 23750, "drawdown_after_peak_pct": -38.53, "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": 0.13, "four_b_full_window_peak_proximity": 0.13, "four_b_timing_verdict": "event_cap_too_early_and_failed_after_offer_window", "four_b_evidence_type": ["valuation_blowoff", "explicit_event_cap", "positioning_overheat"], "four_c_protection_label": "hard_4c_success", "trigger_outcome_label": "small_MFE_large_MAE_event_false_positive", "current_profile_verdict": "current_profile_false_positive", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window", "same_entry_group_id": "R12L10C32_000240_2023_12_05_21850", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R12L10C32_KZINC_2024_TENDER_CONTROL_PREMIUM", "trigger_id": "R12L10C32_KZINC_T1_STAGE2_EVENT_2024_09_13", "symbol": "010130", "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP", "raw_component_scores_before": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 0, "revision_score": 10, "relative_strength_score": 95, "customer_quality_score": 20, "policy_or_regulatory_score": 55, "valuation_repricing_score": 100, "execution_risk_score": 45, "legal_or_contract_risk_score": 70, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0, "control_premium_or_event_premium_score": 100}, "weighted_score_before": 78, "stage_label_before": "Stage3-Yellow_if_event_premium_misread_as_rerating", "raw_component_scores_after": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 0, "revision_score": 10, "relative_strength_score": 95, "customer_quality_score": 20, "policy_or_regulatory_score": 55, "valuation_repricing_score": 55, "execution_risk_score": 45, "legal_or_contract_risk_score": 70, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0, "control_premium_or_event_premium_score": 100}, "weighted_score_after": 63, "stage_label_after": "4B-watch_event_overlay_not_positive_stage", "changed_components": ["valuation_repricing_score", "control_premium_positive_stage_cap", "legal_or_contract_risk_score"], "component_delta_explanation": "control-premium/tender price evidence is retained as event overlay, but positive Stage2/3 promotion requires operating revision, margin bridge, or durable cash-flow evidence.", "MFE_90D_pct": 261.41, "MAE_90D_pct": -1.65, "score_return_alignment_label": "event_premium_alignment", "current_profile_verdict": "current_profile_false_positive"}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R12L10C32_SM_2023_HYBE_KAKAO_TENDER_BATTLE", "trigger_id": "R12L10C32_SM_T1_STAGE2_EVENT_2023_02_10", "symbol": "041510", "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP", "raw_component_scores_before": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 15, "revision_score": 20, "relative_strength_score": 90, "customer_quality_score": 70, "policy_or_regulatory_score": 20, "valuation_repricing_score": 85, "execution_risk_score": 55, "legal_or_contract_risk_score": 55, "dilution_cb_risk_score": 20, "accounting_trust_risk_score": 0, "control_premium_or_event_premium_score": 95}, "weighted_score_before": 76, "stage_label_before": "Stage3-Yellow_if_control_premium_misread_as_operating_leverage", "raw_component_scores_after": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 15, "revision_score": 20, "relative_strength_score": 90, "customer_quality_score": 70, "policy_or_regulatory_score": 20, "valuation_repricing_score": 40, "execution_risk_score": 55, "legal_or_contract_risk_score": 55, "dilution_cb_risk_score": 20, "accounting_trust_risk_score": 0, "control_premium_or_event_premium_score": 95}, "weighted_score_after": 58, "stage_label_after": "event_overlay_only_no_positive_promotion", "changed_components": ["valuation_repricing_score", "control_premium_positive_stage_cap", "legal_or_contract_risk_score"], "component_delta_explanation": "control-premium/tender price evidence is retained as event overlay, but positive Stage2/3 promotion requires operating revision, margin bridge, or durable cash-flow evidence.", "MFE_90D_pct": 40.54, "MAE_90D_pct": -21.1, "score_return_alignment_label": "false_positive_risk_alignment", "current_profile_verdict": "current_profile_false_positive"}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R12L10C32_HANKOOK_2023_MBK_TENDER_FAILED", "trigger_id": "R12L10C32_HANKOOK_T1_STAGE2_EVENT_2023_12_05", "symbol": "000240", "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP", "raw_component_scores_before": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 5, "revision_score": 5, "relative_strength_score": 65, "customer_quality_score": 20, "policy_or_regulatory_score": 15, "valuation_repricing_score": 75, "execution_risk_score": 60, "legal_or_contract_risk_score": 45, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0, "control_premium_or_event_premium_score": 80}, "weighted_score_before": 72, "stage_label_before": "Stage2-Actionable_or_Yellow_if_event_premium_overweighted", "raw_component_scores_after": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 5, "revision_score": 5, "relative_strength_score": 65, "customer_quality_score": 20, "policy_or_regulatory_score": 15, "valuation_repricing_score": 30, "execution_risk_score": 60, "legal_or_contract_risk_score": 45, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0, "control_premium_or_event_premium_score": 80}, "weighted_score_after": 49, "stage_label_after": "event_overlay_only_no_positive_promotion", "changed_components": ["valuation_repricing_score", "control_premium_positive_stage_cap", "legal_or_contract_risk_score"], "component_delta_explanation": "control-premium/tender price evidence is retained as event overlay, but positive Stage2/3 promotion requires operating revision, margin bridge, or durable cash-flow evidence.", "MFE_90D_pct": 8.7, "MAE_90D_pct": -33.14, "score_return_alignment_label": "false_positive_risk_alignment", "current_profile_verdict": "current_profile_false_positive"}
{"row_type": "residual_contribution", "round": "R12", "loop": "10", "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP", "new_independent_case_count": 3, "reused_case_count": 0, "new_symbol_count": 3, "same_archetype_new_symbol_count": 3, "same_archetype_new_trigger_family_count": 3, "new_canonical_archetype_count": 1, "new_trigger_family_count": 3, "tested_existing_calibrated_axes": ["price_only_blowoff_blocks_positive_stage", "full_4b_requires_non_price_evidence", "stage3_green_revision_min"], "residual_error_types_found": ["control_premium_false_positive", "event_cap_reversion", "4B_full_window_too_early"], "loop_contribution_label": "canonical_archetype_rule_candidate", "do_not_propose_new_weight_delta": false}
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
next_round = R12 holdout or R12
next_candidate_archetype = C31_POLICY_SUBSIDY_LEGISLATION_EVENT or C32 non-Korea-control-premium holdout
coverage_gap_remaining = non-tender governance premiums, statutory delisting/take-private examples, failed white-knight defenses
```

## 28. Source Notes

- Stock-web manifest/schema and symbol profiles are the validation source of truth for OHLC, price basis, corporate-action windows, and max date.
- Reuters/AP are used only to anchor public event timing; quantitative calibration uses stock-web rows.
- This file intentionally does not inspect or patch `stock_agent/src/e2r`.
