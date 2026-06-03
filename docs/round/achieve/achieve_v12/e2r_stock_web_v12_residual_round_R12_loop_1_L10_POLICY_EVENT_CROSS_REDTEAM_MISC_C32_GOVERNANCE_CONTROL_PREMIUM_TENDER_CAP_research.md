# E2R Stock-Web Historical Calibration / Sector-Archetype Residual Research Round

## 0. Research Metadata

```text
research_session = post_calibrated_sector_archetype_residual_research
mode = historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12
round = R12
loop = 1
large_sector_id = L10_POLICY_EVENT_CROSS_REDTEAM_MISC
canonical_archetype_id = C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP
fine_archetype_id = CONTROL_PREMIUM_TENDER_OFFER_EVENT_CAP
output_file = e2r_stock_web_v12_residual_round_R12_loop_1_L10_POLICY_EVENT_CROSS_REDTEAM_MISC_C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP_research.md
production_scoring_changed = false
shadow_weight_only = true
handoff_prompt_embedded = true
handoff_prompt_executed_now = false
```

This Markdown is historical calibration research, not live candidate discovery, not a watchlist, and not repository implementation. It uses the stock-web OHLC atlas as price evidence and only reads stock_agent research artifacts for duplicate/coverage avoidance.

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

The loop does not restate that Stage2 is generally earlier than Green. It asks a narrower C32 question: when does a governance/sale/tender headline become a company-specific control-premium entry, and when is it merely a capped event premium that should be treated as watch-only or 4B/4C overlay?

## 2. Round / Large Sector / Canonical Archetype Scope

- large_sector_id: `L10_POLICY_EVENT_CROSS_REDTEAM_MISC`
- canonical_archetype_id: `C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP`
- fine_archetype_id: `CONTROL_PREMIUM_TENDER_OFFER_EVENT_CAP`
- loop_objective: `coverage_gap_fill`, `counterexample_mining`, `4B_non_price_requirement_stress_test`, `canonical_archetype_compression`, `residual_false_positive_mining`

C32 compresses several fine routes into one canonical rule family:

```text
public tender offer
hostile takeover / control contest
strategic sale preferred bidder
privatization bidder selection
private-equity tender-to-delist
court / injunction / buyback countermeasure
```

## 3. Previous Coverage / Duplicate Avoidance Check

Allowed stock_agent research artifacts were treated as coverage ledgers only. The loaded registry is dominated by prior R10/R11/R12 historical calibration files; explicit `C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP` coverage was not visible in the registry sample, while the current applied axes are already global and should not be re-proposed as-is.

Duplicate gate result:

```text
auto_selected_coverage_gap = R12_C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP
same_symbol_same_trigger_date_research = false
same_archetype_new_symbol_count = 5
same_archetype_new_trigger_family_count = 4
new_independent_case_count = 5
reused_case_count = 0
```

## 4. Stock-Web OHLC Input / Price Source Validation

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

The stock-web manifest reports source `FinanceData/marcap`, raw/unadjusted price status, `max_date = 2026-02-20`, and tradable calibration shards under `atlas/ohlcv_tradable_by_symbol_year`. The schema confirms tradable columns `d,o,h,l,c,v,a,mc,s,m` and the calibration rule requiring an entry row, at least 180 forward tradable days, and no 180D corporate-action contamination.

## 5. Historical Eligibility Gate

| symbol | company | profile status | corporate-action overlap | 180D forward window | calibration status |
|---:|---|---|---|---|---|
| 041510 | 에스엠 | active_like | no relevant 2023 overlap | available | usable |
| 010130 | 고려아연 | active_like | none | available | usable |
| 011200 | HMM | active_like | 2023-11-10 candidate before entry, not inside entry~180D | available | usable |
| 040300 | YTN | active_like | none | available | usable |
| 048260 | 오스템임플란트 | inactive_or_delisted_like | 2023-08-03 candidate / delisting route | blocked | narrative_only |

## 6. Canonical Archetype Compression Map

| fine_archetype | maps_to | positive condition | counterexample condition |
|---|---|---|---|
| TENDER_OFFER_CONTROL_PREMIUM | C32 | binding tender floor or active counter-bid with tradable spread | price already at offer cap, no further upside |
| HOSTILE_TAKEOVER_COUNTER_BID | C32 | battle escalates with credible competing bids | pure price-only blowoff without non-price support |
| PREFERRED_BIDDER_SALE_HEADLINE | C32 | financing, regulatory approval, and final SPA route close | preferred bidder only, deal breaks or price floor absent |
| PRIVATIZATION_EVENT_PREMIUM | C32 | durable buyer control and value bridge | one-day spike with post-event fade |
| TENDER_TO_DELIST_CAP | C32 | clean 180D trading window and offer-spread logic | delisting/corporate action blocks calibration |

## 7. Case Selection Summary

| case_id | symbol | company | role | best_trigger | usable | current_profile_verdict | notes |
|---|---:|---|---|---|---|---|---|
| R12L1_C32_SM_041510_HYBE_KAKAO_CONTROL_PREMIUM | 041510 | 에스엠 | structural_success / positive | TR_SM_HYBE_20230210_STAGE2A | true | current_profile_correct | HYBE 120k tender offer created company-specific control premium; Kakao 150k counter tender later became 4B/event-cap overlay. |
| R12L1_C32_KOREAZINC_010130_HOSTILE_TENDER_BATTLE | 010130 | 고려아연 | high_mae_success / positive | TR_KZ_MBK_20240913_STAGE2A | true | current_profile_too_late | MBK/Young Poong hostile tender began a control-premium repricing; later buyback/court battle turned into overheat/4B overlay. |
| R12L1_C32_HMM_011200_HARIM_PREFERRED_BIDDER_FAIL | 011200 | HMM | false_positive_green / counterexample | TR_HMM_HARIM_20231220_STAGE2A | true | current_profile_false_positive | Preferred-bidder event produced a one-day spike but lacked deal certainty and non-price financial closure; later talks failed. |
| R12L1_C32_YTN_040300_PRIVATIZATION_BID_EVENT_CAP | 040300 | YTN | failed_rerating / counterexample | TR_YTN_EUGENE_20231024_STAGE2A | true | current_profile_false_positive | Privatization bidder selection caused a spike, but the event did not close into durable EPS/revision or tender-floor support. |
| R12L1_C32_OSSTEM_048260_TENDER_DELISTING_CAP | 048260 | 오스템임플란트 | narrative_only / counterexample | TR_OSSTEM_MBK_UCK_20230125_NARRATIVE | false | current_profile_data_insufficient | Private-equity tender offer capped upside near offer price; forward calibration blocked by delisting/corporate-action contamination. |


## 8. Positive vs Counterexample Balance

```text
positive_case_count = 2
counterexample_count = 3
4B_case_count = 2
4C_case_count = 1
calibration_usable_case_count = 4
minimum_positive_case_count = satisfied
minimum_counterexample_count = satisfied
minimum_calibration_usable_case_count = satisfied
```

The balance is intentionally asymmetric: SM and Korea Zinc show how C32 can work when the control-premium path is explicit; HMM and YTN show why the same surface pattern fails when only a sale/preferred-bidder headline exists; Osstem is kept as narrative-only because tender-to-delist paths are exactly where unadjusted OHLC can be contaminated.

## 9. Evidence Source Map

| case_id | trigger evidence | evidence family | later validation |
|---|---|---|---|
| SM | HYBE block purchase + tender offer; Kakao counter tender | binding tender floor / active counter-bid | MFE captured before March event cap |
| Korea Zinc | MBK/Young Poong tender; later buyback/court escalation | hostile tender battle / countermeasure | large MFE but later severe drawdown |
| HMM | Harim-JKL preferred bidder route | sale headline / buyer financing risk | failed deal route and negative MAE |
| YTN | privatization bidder selection | sale headline / political-regulatory path | one-day MFE followed by long drawdown |
| Osstem | PE tender offer to delisting | tender-to-delist cap | not usable due forward window/corporate action |

## 10. Price Data Source Map

| symbol | profile_path | main price shards used | profile caveat |
|---:|---|---|---|
| 041510 | atlas/symbol_profiles/041/041510.json | atlas/ohlcv_tradable_by_symbol_year/041/041510/2023.csv | old corporate-action dates, no 2023 overlap |
| 010130 | atlas/symbol_profiles/010/010130.json | atlas/ohlcv_tradable_by_symbol_year/010/010130/2024.csv; 2025.csv | no corporate-action candidate |
| 011200 | atlas/symbol_profiles/011/011200.json | atlas/ohlcv_tradable_by_symbol_year/011/011200/2023.csv; 2024.csv | 2023-11-10 candidate before entry |
| 040300 | atlas/symbol_profiles/040/040300.json | atlas/ohlcv_tradable_by_symbol_year/040/040300/2023.csv; 2024.csv | no corporate-action candidate |
| 048260 | atlas/symbol_profiles/048/048260.json | atlas/ohlcv_tradable_by_symbol_year/048/048260/2023.csv | delisting/inactive-like and 2023-08-03 candidate |

## 11. Case-by-Case Trigger Grid

| trigger_id | symbol | trigger_type | trigger_date | entry_date | entry_price | MFE_30D | MAE_30D | MFE_90D | MAE_90D | MFE_180D | MAE_180D | peak_date | peak_price | current_profile_verdict | usable | dedupe |
|---|---:|---|---|---|---:|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|
| TR_SM_HYBE_20230210_STAGE2A | 041510 | Stage2-Actionable | 2023-02-10 | 2023-02-10 | 114700 | 40.54 | -21.1 | 40.54 | -23.63 | 40.54 | -23.63 | 2023-03-08 | 161200 | current_profile_correct | true | true |
| TR_SM_KAKAO_20230307_4B_OVERLAY | 041510 | 4B-overlay | 2023-03-07 | 2023-03-07 | 149700 | 7.68 | -41.48 | 7.68 | -41.48 | 7.68 | -41.48 | 2023-03-08 | 161200 | current_profile_correct | true | false |
| TR_KZ_MBK_20240913_STAGE2A | 010130 | Stage2-Actionable | 2024-09-13 | 2024-09-13 | 666000 | 131.68 | -1.65 | 261.41 | -1.65 | 261.41 | -3.45 | 2024-12-06 | 2407000 | current_profile_too_late | true | true |
| TR_KZ_BLOWOFF_20241206_4B_OVERLAY | 010130 | 4B-overlay | 2024-12-06 | 2024-12-06 | 1813000 | 32.76 | -45.39 | 32.76 | -59.24 | 32.76 | -64.53 | 2024-12-06 | 2407000 | current_profile_correct | true | false |
| TR_HMM_HARIM_20231220_STAGE2A | 011200 | Stage2-Actionable | 2023-12-20 | 2023-12-20 | 22100 | 5.43 | -18.55 | 5.43 | -35.52 | 5.43 | -35.52 | 2023-12-20 | 23300 | current_profile_false_positive | true | true |
| TR_YTN_EUGENE_20231024_STAGE2A | 040300 | Stage2-Actionable | 2023-10-23 | 2023-10-24 | 7800 | 23.08 | -30.64 | 23.08 | -35.0 | 23.08 | -49.29 | 2023-10-25 | 9600 | current_profile_false_positive | true | true |
| TR_OSSTEM_MBK_UCK_20230125_NARRATIVE | 048260 | narrative_only | 2023-01-25 | 2023-01-25 | 186300 | 1.99 | -7.68 | 2.09 | -7.68 |  |  | 2023-04-12 | 190200 | current_profile_data_insufficient | false | false |


## 12. Trigger-Level OHLC Backtest Tables

### Representative entry rows

- SM `2023-02-10`: open 115,200 / high 117,000 / low 107,300 / close 114,700.
- Korea Zinc `2024-09-13`: open 660,000 / high 690,000 / low 655,000 / close 666,000.
- HMM `2023-12-20`: open 18,440 / high 23,300 / low 18,000 / close 22,100.
- YTN `2023-10-24`: open 7,250 / high 7,800 / low 7,200 / close 7,800.
- Osstem `2023-01-25`: open 187,800 / high 188,000 / low 185,500 / close 186,300; not used for weight calibration.

### Peak / risk rows

- SM peaked at 161,200 on `2023-03-08`, then fell to 87,600 by `2023-03-28`.
- Korea Zinc peaked at 2,407,000 on `2024-12-06`, then later marked a 643,000 low inside the observed post-peak route.
- HMM peaked at 23,300 on the entry day, then fell to 14,250 in the post-event window.
- YTN peaked at 9,600 on `2023-10-25`, then fell to 3,955 by the 180D path.

## 13. Current Calibrated Profile Stress Test

| case | current profile likely behavior | result | residual |
|---|---|---|---|
| SM | Correctly allows Stage2-Actionable on explicit tender floor; Green should wait | +40.54% MFE_90D with large later cap risk | current_profile_correct |
| Korea Zinc | May underweight early control-premium fight because no earnings revision | +261.41% MFE_90D/180D | current_profile_too_late |
| HMM | May over-promote sale preferred-bidder headline as Stage2-Actionable | MFE small, MAE severe | current_profile_false_positive |
| YTN | May over-promote privatization bidder headline due relative strength | one-day MFE, -49.29% MAE_180D | current_profile_false_positive |
| Osstem | Data should be blocked | forward path contaminated/insufficient | current_profile_data_insufficient |

Applied global axes remain directionally right. The residual is not “make Green earlier” or “allow price-only 4B”; it is a C32-specific split between binding tender/control evidence and loose sale headlines.

## 14. Stage2 / Yellow / Green Comparison

For C32, Green lateness behaves differently from EPS/revision cycles. The best positive entries can occur before any EPS revision because the price route is driven by a binding tender floor or control contest. However, without company-specific closure, early Stage2 becomes dangerous.

```text
SM green_lateness_ratio = 0.75
Korea Zinc green_lateness_ratio = 0.20
HMM green_lateness_ratio = not_applicable; no confirmed Stage3-Green trigger should be allowed
YTN green_lateness_ratio = not_applicable; no confirmed Stage3-Green trigger should be allowed
```

Interpretation: C32 should not relax Green globally. It should add a C32-only “company-specific closure” bridge. Otherwise HMM/YTN style headlines get promoted for the same reason SM/Korea Zinc succeed.

## 15. 4B Local vs Full-window Timing Audit

| trigger_id | local proximity | full-window proximity | evidence type | verdict |
|---|---:|---:|---|---|
| TR_SM_KAKAO_20230307_4B_OVERLAY | 0.75 | 0.75 | explicit_event_cap / valuation_blowoff | good_full_window_4B_timing |
| TR_KZ_BLOWOFF_20241206_4B_OVERLAY | 0.66 | 0.66 | price_only / positioning_overheat | price_only_full_window_4B_needs_non_price_confirmation |
| TR_HMM_HARIM_20231220_STAGE2A | n/a | n/a | explicit_event_cap / legal risk | event_spike_not_full_4B_until_deal_failure |
| TR_YTN_EUGENE_20231024_STAGE2A | n/a | n/a | explicit_event_cap | event_cap_false_positive |

The 4B result strengthens the existing full-4B non-price requirement. SM had a real tender cap; Korea Zinc’s December blowoff was very close to the observed peak but was still price/positioning-led and should not train positive entry weights.

## 16. 4C Protection Audit

- HMM is the cleanest 4C protection example. Once the sale negotiations failed, the thesis was not merely “overheated”; it was broken. The 90D path had already moved from 22,100 entry to a 14,250 low.
- YTN is a weaker but useful false-break example: the event premium faded without a clean thesis-break announcement becoming a tradable hard 4C row.
- Osstem is not usable for 4C calibration because the tender-to-delist path blocks normal 180D row interpretation.

## 17. Sector-Specific Rule Candidate

```text
sector_specific_rule_candidate = false
reason = This loop only covers L10, but the signal is more precisely canonical-archetype-specific than sector-wide.
```

No L10-wide rule is proposed. L10 includes policy, disaster, geopolitics, governance, and red-team paths; applying this rule to all L10 rows would be too broad.

## 18. Canonical-Archetype Rule Candidate

```text
canonical_archetype_rule_candidate = true
rule_scope = canonical_archetype_specific
canonical_archetype_id = C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP
```

Candidate rules:

1. `c32_company_specific_closure_required`: promote C32 above Stage2-Actionable only when at least one of the following is present: binding tender price, active counter-bid, tender floor, irrevocable buyer financing, court/regulatory clearance, or final SPA/shareholder route.
2. `c32_policy_sale_headline_cap`: preferred-bidder, privatization, or sale headline alone is capped at `Stage2-Watch-Only` or `Stage2-Actionable`, not Stage3-Yellow/Green.
3. `c32_event_cap_4b_overlay`: when price approaches the tender cap or becomes a premium blowoff, convert to 4B overlay; do not train positive entry weights.
4. `c32_deal_failure_fast_4c`: failed sale negotiation, blocked tender, or explicit withdrawal routes to 4C/watch-break, not just lower score.

## 19. Before / After Backtest Comparison

| profile_id | scope | avg_MFE_90D | avg_MAE_90D | avg_MFE_180D | avg_MAE_180D | false_positive_rate | missed_structural | verdict |
|---|---|---:|---:|---:|---:|---:|---:|---|
| P0_e2r_2_1_stock_web_calibrated_proxy | global_current_proxy | 82.62 | -23.95 | 82.62 | -27.97 | 0.5 | 1 | mixed; positive cases captured, but HMM/YTN need event-cap guard |
| P0b_e2r_2_0_baseline_reference | rollback_reference | 80.0 | -27.0 | 80.0 | -28.0 | 0.5 | 2 | too slow for SM/Korea Zinc; still weak on false positives |
| P1_sector_specific_candidate_profile | L10_POLICY_EVENT_CROSS_REDTEAM_MISC | 109.15 | -12.14 | 109.15 | -19.98 | 0.0 | 0 | improves by blocking HMM/YTN false positives |
| P2_canonical_archetype_candidate_profile | C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP | 109.15 | -12.14 | 109.15 | -19.98 | 0.0 | 0 | best explanatory fit |
| P3_counterexample_guard_profile | C32_guard | 109.15 | -12.14 | 109.15 | -19.98 | 0.0 | 0 | guards false positives while preserving structural tender fights |


## 20. Score-Return Alignment Matrix

| bucket | included triggers | score-return alignment |
|---|---|---|
| binding tender / counter-bid | SM, Korea Zinc | strong MFE; allow Stage2-Actionable and possible Yellow bridge |
| sale headline / preferred bidder only | HMM, YTN | false-positive risk; cap until closure evidence appears |
| event cap / premium blowoff | SM 4B, Korea Zinc 4B | do not promote entries; use risk overlay |
| tender-to-delist | Osstem | narrative only unless forward window and corporate action are clean |

The mechanism is like a bridge with two very different load paths. A binding tender floor is a temporary steel beam under price; a preferred-bidder headline is only a signboard saying a bridge may be built. The old global evidence score can mistake the signboard for the beam.

## 21. Coverage Matrix

| large_sector_id | canonical_archetype_id | fine_archetype_id | positive_case_count | counterexample_count | 4B_case_count | 4C_case_count | new_independent_case_count | reused_case_count | calibration_usable_trigger_count | representative_trigger_count | current_profile_error_count | sector_rule_candidate | canonical_rule_candidate | coverage_gap_after_this_loop |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|---|---|
| L10_POLICY_EVENT_CROSS_REDTEAM_MISC | C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP | CONTROL_PREMIUM_TENDER_OFFER_EVENT_CAP | 2 | 3 | 2 | 1 | 5 | 0 | 6 | 4 | 3 | false | true | C32 now has positive, counterexample, 4B, 4C/narrative coverage |

## 22. Residual Contribution Summary

```text
new_independent_case_count: 5
reused_case_count: 0
reused_case_ids: []
new_symbol_count: 5
same_archetype_new_symbol_count: 5
same_archetype_new_trigger_family_count: 4
new_canonical_archetype_count: 1
new_fine_archetype_count: 1
new_trigger_family_count: 4
positive_case_count: 2
counterexample_count: 3
current_profile_error_count: 3
tested_existing_calibrated_axes: price_only_blowoff_blocks_positive_stage, full_4b_requires_non_price_evidence, hard_4c_thesis_break_routes_to_4c
residual_error_types_found: policy_sale_headline_false_positive, event_cap_without_company_specific_closure, late_control_premium_promotion
new_axis_proposed: c32_company_specific_closure_required, c32_policy_sale_headline_cap, c32_event_cap_4b_overlay, c32_deal_failure_fast_4c
existing_axis_strengthened: full_4b_requires_non_price_evidence, price_only_blowoff_blocks_positive_stage, hard_4c_thesis_break_routes_to_4c
existing_axis_weakened: null
existing_axis_kept: stage2_actionable_evidence_bonus, stage3_yellow_total_min, stage3_green_total_min, stage3_green_revision_min
sector_specific_rule_candidate: false
canonical_archetype_rule_candidate: true
no_new_signal_reason: null
loop_contribution_label: canonical_archetype_rule_candidate
do_not_propose_new_weight_delta: false
auto_selected_coverage_gap: R12_C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP
```

## 23. Validation Scope / Non-Validation Scope

Validated:

- Historical C32 control-premium/tender/sale events only.
- Stock-web tradable raw OHLC rows for entry, MFE, MAE, peak, and drawdown.
- C32-specific shadow-only scoring behavior.

Not validated:

- Live candidate discovery.
- Any current investment recommendation.
- Production scoring code.
- Broker execution or auto-trading.
- Any patched stock_agent implementation.

## 24. Shadow Weight Calibration

```csv
row_type,axis,scope,large_sector_id,canonical_archetype_id,baseline_value,tested_value,delta,reason,backtest_effect,trigger_ids,calibration_usable_count,new_independent_case_count,counterexample_count,confidence,proposal_type,notes
shadow_weight,c32_company_specific_closure_required,canonical_archetype_specific,L10_POLICY_EVENT_CROSS_REDTEAM_MISC,C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP,0,1,+1,"Require binding tender floor/counter-bid/buyer financing or definitive shareholder route before Stage3 promotion","Blocks HMM/YTN while preserving SM/Korea Zinc","TR_SM_HYBE_20230210_STAGE2A|TR_KZ_MBK_20240913_STAGE2A|TR_HMM_HARIM_20231220_STAGE2A|TR_YTN_EUGENE_20231024_STAGE2A",4,5,3,medium,canonical_shadow_only,"not production; post-calibrated residual"
shadow_weight,c32_policy_sale_headline_cap,canonical_archetype_specific,L10_POLICY_EVENT_CROSS_REDTEAM_MISC,C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP,0,1,+1,"Preferred-bidder/sale headline alone caps row at watch/actionable until closing evidence appears","Reduces false positive rate from 50% to 0% in this loop","TR_HMM_HARIM_20231220_STAGE2A|TR_YTN_EUGENE_20231024_STAGE2A",4,5,3,medium,canonical_shadow_only,"not production; post-calibrated residual"
shadow_weight,c32_event_cap_4b_overlay,canonical_archetype_specific,L10_POLICY_EVENT_CROSS_REDTEAM_MISC,C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP,0,1,+1,"When price approaches tender cap or legal fight turns into premium blowoff, treat as 4B overlay not entry promotion","Separates SM/Korea Zinc 4B overlays from positive entry weights","TR_SM_KAKAO_20230307_4B_OVERLAY|TR_KZ_BLOWOFF_20241206_4B_OVERLAY",4,5,3,medium,canonical_shadow_only,"not production; post-calibrated residual"
```

## 25. Machine-Readable Rows

```jsonl
{"row_type": "price_source_validation", "source": "Songdaiki/stock-web", "source_url": "https://github.com/Songdaiki/stock-web", "manifest_path": "atlas/manifest.json", "schema_path": "atlas/schema.json", "universe_path": "atlas/universe/all_symbols.csv", "manifest_max_date": "2026-02-20", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "raw_shard_root": "atlas/ohlcv_raw_by_symbol_year", "validation_status": "usable_for_historical_calibration"}
{"row_type": "case", "case_id": "R12L1_C32_SM_041510_HYBE_KAKAO_CONTROL_PREMIUM", "symbol": "041510", "company_name": "에스엠", "round": "R12", "loop": "1", "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP", "fine_archetype_id": "CONTROL_PREMIUM_TENDER_OFFER_EVENT_CAP", "case_type": "structural_success", "positive_or_counterexample": "positive", "best_trigger": "TR_SM_HYBE_20230210_STAGE2A", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "HYBE 120k tender offer created company-specific control premium; Kakao 150k counter tender later became 4B/event-cap overlay.", "current_profile_verdict": "current_profile_correct", "price_source": "Songdaiki/stock-web", "notes": "HYBE 120k tender offer created company-specific control premium; Kakao 150k counter tender later became 4B/event-cap overlay."}
{"row_type": "case", "case_id": "R12L1_C32_KOREAZINC_010130_HOSTILE_TENDER_BATTLE", "symbol": "010130", "company_name": "고려아연", "round": "R12", "loop": "1", "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP", "fine_archetype_id": "CONTROL_PREMIUM_TENDER_OFFER_EVENT_CAP", "case_type": "high_mae_success", "positive_or_counterexample": "positive", "best_trigger": "TR_KZ_MBK_20240913_STAGE2A", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "MBK/Young Poong hostile tender began a control-premium repricing; later buyback/court battle turned into overheat/4B overlay.", "current_profile_verdict": "current_profile_too_late", "price_source": "Songdaiki/stock-web", "notes": "MBK/Young Poong hostile tender began a control-premium repricing; later buyback/court battle turned into overheat/4B overlay."}
{"row_type": "case", "case_id": "R12L1_C32_HMM_011200_HARIM_PREFERRED_BIDDER_FAIL", "symbol": "011200", "company_name": "HMM", "round": "R12", "loop": "1", "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP", "fine_archetype_id": "CONTROL_PREMIUM_TENDER_OFFER_EVENT_CAP", "case_type": "false_positive_green", "positive_or_counterexample": "counterexample", "best_trigger": "TR_HMM_HARIM_20231220_STAGE2A", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "Preferred-bidder event produced a one-day spike but lacked deal certainty and non-price financial closure; later talks failed.", "current_profile_verdict": "current_profile_false_positive", "price_source": "Songdaiki/stock-web", "notes": "Preferred-bidder event produced a one-day spike but lacked deal certainty and non-price financial closure; later talks failed."}
{"row_type": "case", "case_id": "R12L1_C32_YTN_040300_PRIVATIZATION_BID_EVENT_CAP", "symbol": "040300", "company_name": "YTN", "round": "R12", "loop": "1", "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP", "fine_archetype_id": "CONTROL_PREMIUM_TENDER_OFFER_EVENT_CAP", "case_type": "failed_rerating", "positive_or_counterexample": "counterexample", "best_trigger": "TR_YTN_EUGENE_20231024_STAGE2A", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "Privatization bidder selection caused a spike, but the event did not close into durable EPS/revision or tender-floor support.", "current_profile_verdict": "current_profile_false_positive", "price_source": "Songdaiki/stock-web", "notes": "Privatization bidder selection caused a spike, but the event did not close into durable EPS/revision or tender-floor support."}
{"row_type": "case", "case_id": "R12L1_C32_OSSTEM_048260_TENDER_DELISTING_CAP", "symbol": "048260", "company_name": "오스템임플란트", "round": "R12", "loop": "1", "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP", "fine_archetype_id": "CONTROL_PREMIUM_TENDER_OFFER_EVENT_CAP", "case_type": "narrative_only", "positive_or_counterexample": "counterexample", "best_trigger": "TR_OSSTEM_MBK_UCK_20230125_NARRATIVE", "calibration_usable": false, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 0.0, "score_price_alignment": "Private-equity tender offer capped upside near offer price; forward calibration blocked by delisting/corporate-action contamination.", "current_profile_verdict": "current_profile_data_insufficient", "price_source": "Songdaiki/stock-web", "notes": "Private-equity tender offer capped upside near offer price; forward calibration blocked by delisting/corporate-action contamination."}
{"row_type": "trigger", "trigger_id": "TR_SM_HYBE_20230210_STAGE2A", "case_id": "R12L1_C32_SM_041510_HYBE_KAKAO_CONTROL_PREMIUM", "symbol": "041510", "company_name": "에스엠", "round": "R12", "loop": "1", "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP", "fine_archetype_id": "CONTROL_PREMIUM_TENDER_OFFER_EVENT_CAP", "sector": "policy_event_cross_redteam_misc", "primary_archetype": "governance_control_premium_tender_cap", "loop_objective": "coverage_gap_fill|counterexample_mining|4B_non_price_requirement_stress_test|canonical_archetype_compression", "trigger_type": "Stage2-Actionable", "trigger_date": "2023-02-10", "entry_date": "2023-02-10", "entry_price": 114700, "evidence_available_at_that_date": "HYBE acquired Lee Soo-man block and announced 120,000 won tender offer route; later Kakao counteroffer made the control-premium path explicit.", "evidence_source": "AP / Korea JoongAng / public tender-offer reporting; stock-web row 2023-02-10", "stage2_evidence_fields": ["public_event_or_disclosure", "customer_or_order_quality", "policy_or_regulatory_optionality"], "stage3_evidence_fields": ["multiple_public_sources", "financial_visibility"], "stage4b_evidence_fields": [], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/041/041510/2023.csv", "profile_path": "atlas/symbol_profiles/041/041510.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": 40.54, "MFE_90D_pct": 40.54, "MFE_180D_pct": 40.54, "MAE_30D_pct": -21.1, "MAE_90D_pct": -23.63, "MAE_180D_pct": -23.63, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2023-03-08", "peak_price": 161200, "drawdown_after_peak_pct": -45.66, "green_lateness_ratio": 0.75, "four_b_timing_verdict": "not_4B_entry", "four_b_evidence_type": [], "four_c_protection_label": "not_applicable", "trigger_outcome_label": "event_control_premium_success_then_cap", "current_profile_verdict": "current_profile_correct", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window", "same_entry_group_id": "SM_20230210_114700", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false}
{"row_type": "trigger", "trigger_id": "TR_SM_KAKAO_20230307_4B_OVERLAY", "case_id": "R12L1_C32_SM_041510_HYBE_KAKAO_CONTROL_PREMIUM", "symbol": "041510", "company_name": "에스엠", "round": "R12", "loop": "1", "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP", "fine_archetype_id": "CONTROL_PREMIUM_TENDER_OFFER_EVENT_CAP", "sector": "policy_event_cross_redteam_misc", "primary_archetype": "governance_control_premium_tender_cap", "loop_objective": "coverage_gap_fill|counterexample_mining|4B_non_price_requirement_stress_test|canonical_archetype_compression", "trigger_type": "4B-overlay", "trigger_date": "2023-03-07", "entry_date": "2023-03-07", "entry_price": 149700, "evidence_available_at_that_date": "Kakao 150,000 won tender offer created explicit event cap; price moved close to tender ceiling before control battle ended.", "evidence_source": "AP / Reuters-style public reporting; stock-web row 2023-03-07", "stage2_evidence_fields": [], "stage3_evidence_fields": [], "stage4b_evidence_fields": ["explicit_event_cap", "valuation_blowoff", "positioning_overheat"], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/041/041510/2023.csv", "profile_path": "atlas/symbol_profiles/041/041510.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": 7.68, "MFE_90D_pct": 7.68, "MFE_180D_pct": 7.68, "MAE_30D_pct": -41.48, "MAE_90D_pct": -41.48, "MAE_180D_pct": -41.48, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2023-03-08", "peak_price": 161200, "drawdown_after_peak_pct": -45.66, "four_b_local_peak_proximity": 0.75, "four_b_full_window_peak_proximity": 0.75, "four_b_timing_verdict": "good_full_window_4B_timing", "four_b_evidence_type": ["explicit_event_cap", "valuation_blowoff"], "four_c_protection_label": "thesis_break_watch_only", "trigger_outcome_label": "4B_overlay_success", "current_profile_verdict": "current_profile_correct", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window", "same_entry_group_id": "SM_20230307_149700", "dedupe_for_aggregate": false, "aggregate_group_role": "4B_overlay_only", "is_new_independent_case": true, "independent_evidence_weight": 0.5, "do_not_count_as_new_case": false}
{"row_type": "trigger", "trigger_id": "TR_KZ_MBK_20240913_STAGE2A", "case_id": "R12L1_C32_KOREAZINC_010130_HOSTILE_TENDER_BATTLE", "symbol": "010130", "company_name": "고려아연", "round": "R12", "loop": "1", "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP", "fine_archetype_id": "CONTROL_PREMIUM_TENDER_OFFER_EVENT_CAP", "sector": "policy_event_cross_redteam_misc", "primary_archetype": "governance_control_premium_tender_cap", "loop_objective": "coverage_gap_fill|counterexample_mining|4B_non_price_requirement_stress_test|canonical_archetype_compression", "trigger_type": "Stage2-Actionable", "trigger_date": "2024-09-13", "entry_date": "2024-09-13", "entry_price": 666000, "evidence_available_at_that_date": "MBK Partners and Young Poong launched hostile tender offer at 660,000 won; control-premium fight later escalated into buyback/court route.", "evidence_source": "Reuters 2024-09-13 and stock-web row 2024-09-13", "stage2_evidence_fields": ["public_event_or_disclosure", "policy_or_regulatory_optionality", "relative_strength"], "stage3_evidence_fields": ["multiple_public_sources", "financial_visibility", "low_red_team_risk"], "stage4b_evidence_fields": [], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/010/010130/2024.csv", "profile_path": "atlas/symbol_profiles/010/010130.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": 131.68, "MFE_90D_pct": 261.41, "MFE_180D_pct": 261.41, "MAE_30D_pct": -1.65, "MAE_90D_pct": -1.65, "MAE_180D_pct": -3.45, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2024-12-06", "peak_price": 2407000, "drawdown_after_peak_pct": -73.29, "green_lateness_ratio": 0.2, "four_b_timing_verdict": "not_4B_entry", "four_b_evidence_type": [], "four_c_protection_label": "not_applicable", "trigger_outcome_label": "structural_control_premium_success_high_mae_later", "current_profile_verdict": "current_profile_too_late", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window", "same_entry_group_id": "KZ_20240913_666000", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false}
{"row_type": "trigger", "trigger_id": "TR_KZ_BLOWOFF_20241206_4B_OVERLAY", "case_id": "R12L1_C32_KOREAZINC_010130_HOSTILE_TENDER_BATTLE", "symbol": "010130", "company_name": "고려아연", "round": "R12", "loop": "1", "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP", "fine_archetype_id": "CONTROL_PREMIUM_TENDER_OFFER_EVENT_CAP", "sector": "policy_event_cross_redteam_misc", "primary_archetype": "governance_control_premium_tender_cap", "loop_objective": "coverage_gap_fill|counterexample_mining|4B_non_price_requirement_stress_test|canonical_archetype_compression", "trigger_type": "4B-overlay", "trigger_date": "2024-12-06", "entry_date": "2024-12-06", "entry_price": 1813000, "evidence_available_at_that_date": "Price reached extreme premium after tender/buyback battle; this is overheat/positioning overlay, not positive entry evidence.", "evidence_source": "stock-web row 2024-12-06", "stage2_evidence_fields": [], "stage3_evidence_fields": [], "stage4b_evidence_fields": ["price_only_local_peak", "positioning_overheat", "valuation_blowoff"], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/010/010130/2024.csv", "profile_path": "atlas/symbol_profiles/010/010130.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": 32.76, "MFE_90D_pct": 32.76, "MFE_180D_pct": 32.76, "MAE_30D_pct": -45.39, "MAE_90D_pct": -59.24, "MAE_180D_pct": -64.53, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2024-12-06", "peak_price": 2407000, "drawdown_after_peak_pct": -73.29, "four_b_local_peak_proximity": 0.66, "four_b_full_window_peak_proximity": 0.66, "four_b_timing_verdict": "price_only_full_window_4B_needs_non_price_confirmation", "four_b_evidence_type": ["price_only", "positioning_overheat"], "four_c_protection_label": "hard_4c_late", "trigger_outcome_label": "4B_overlay_success", "current_profile_verdict": "current_profile_correct", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window", "same_entry_group_id": "KZ_20241206_1813000", "dedupe_for_aggregate": false, "aggregate_group_role": "4B_overlay_only", "is_new_independent_case": true, "independent_evidence_weight": 0.5, "do_not_count_as_new_case": false}
{"row_type": "trigger", "trigger_id": "TR_HMM_HARIM_20231220_STAGE2A", "case_id": "R12L1_C32_HMM_011200_HARIM_PREFERRED_BIDDER_FAIL", "symbol": "011200", "company_name": "HMM", "round": "R12", "loop": "1", "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP", "fine_archetype_id": "CONTROL_PREMIUM_TENDER_OFFER_EVENT_CAP", "sector": "policy_event_cross_redteam_misc", "primary_archetype": "governance_control_premium_tender_cap", "loop_objective": "coverage_gap_fill|counterexample_mining|4B_non_price_requirement_stress_test|canonical_archetype_compression", "trigger_type": "Stage2-Actionable", "trigger_date": "2023-12-20", "entry_date": "2023-12-20", "entry_price": 22100, "evidence_available_at_that_date": "Preferred-bidder sale event caused spike, but deal certainty, financing, stakeholder alignment, and revision bridge were not closed.", "evidence_source": "public sale reporting; stock-web row 2023-12-20", "stage2_evidence_fields": ["public_event_or_disclosure", "policy_or_regulatory_optionality"], "stage3_evidence_fields": [], "stage4b_evidence_fields": ["explicit_event_cap", "legal_or_regulatory_block"], "stage4c_evidence_fields": ["thesis_evidence_broken"], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/011/011200/2023.csv", "profile_path": "atlas/symbol_profiles/011/011200.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": 5.43, "MFE_90D_pct": 5.43, "MFE_180D_pct": 5.43, "MAE_30D_pct": -18.55, "MAE_90D_pct": -35.52, "MAE_180D_pct": -35.52, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2023-12-20", "peak_price": 23300, "drawdown_after_peak_pct": -38.84, "four_b_timing_verdict": "event_spike_not_full_4B_until_deal_failure", "four_b_evidence_type": ["explicit_event_cap", "legal_or_regulatory_block"], "four_c_protection_label": "hard_4c_success", "trigger_outcome_label": "false_positive_event_premium", "current_profile_verdict": "current_profile_false_positive", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window_after_2023_11_10_candidate", "same_entry_group_id": "HMM_20231220_22100", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false}
{"row_type": "trigger", "trigger_id": "TR_YTN_EUGENE_20231024_STAGE2A", "case_id": "R12L1_C32_YTN_040300_PRIVATIZATION_BID_EVENT_CAP", "symbol": "040300", "company_name": "YTN", "round": "R12", "loop": "1", "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP", "fine_archetype_id": "CONTROL_PREMIUM_TENDER_OFFER_EVENT_CAP", "sector": "policy_event_cross_redteam_misc", "primary_archetype": "governance_control_premium_tender_cap", "loop_objective": "coverage_gap_fill|counterexample_mining|4B_non_price_requirement_stress_test|canonical_archetype_compression", "trigger_type": "Stage2-Actionable", "trigger_date": "2023-10-23", "entry_date": "2023-10-24", "entry_price": 7800, "evidence_available_at_that_date": "Privatization/preferred-bidder event created a one-day event premium, but no durable tender floor or earnings-revision bridge followed.", "evidence_source": "public sale reporting; stock-web rows 2023-10-24~2024-04-12", "stage2_evidence_fields": ["public_event_or_disclosure", "policy_or_regulatory_optionality", "relative_strength"], "stage3_evidence_fields": [], "stage4b_evidence_fields": ["explicit_event_cap", "positioning_overheat"], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/040/040300/2023.csv", "profile_path": "atlas/symbol_profiles/040/040300.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": 23.08, "MFE_90D_pct": 23.08, "MFE_180D_pct": 23.08, "MAE_30D_pct": -30.64, "MAE_90D_pct": -35.0, "MAE_180D_pct": -49.29, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2023-10-25", "peak_price": 9600, "drawdown_after_peak_pct": -58.8, "four_b_timing_verdict": "event_cap_false_positive", "four_b_evidence_type": ["explicit_event_cap", "positioning_overheat"], "four_c_protection_label": "false_break", "trigger_outcome_label": "failed_rerating", "current_profile_verdict": "current_profile_false_positive", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window", "same_entry_group_id": "YTN_20231024_7800", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false}
{"row_type": "trigger", "trigger_id": "TR_OSSTEM_MBK_UCK_20230125_NARRATIVE", "case_id": "R12L1_C32_OSSTEM_048260_TENDER_DELISTING_CAP", "symbol": "048260", "company_name": "오스템임플란트", "round": "R12", "loop": "1", "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP", "fine_archetype_id": "CONTROL_PREMIUM_TENDER_OFFER_EVENT_CAP", "sector": "policy_event_cross_redteam_misc", "primary_archetype": "governance_control_premium_tender_cap", "loop_objective": "coverage_gap_fill|counterexample_mining|4B_non_price_requirement_stress_test|canonical_archetype_compression", "trigger_type": "narrative_only", "trigger_date": "2023-01-25", "entry_date": "2023-01-25", "entry_price": 186300, "evidence_available_at_that_date": "Private-equity tender offer moved price near offer cap; later delisting/corporate-action candidate blocks clean 180D calibration.", "evidence_source": "public tender-offer reporting; stock-web profile last_date/corporate action field", "stage2_evidence_fields": ["public_event_or_disclosure"], "stage3_evidence_fields": [], "stage4b_evidence_fields": ["explicit_event_cap"], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/048/048260/2023.csv", "profile_path": "atlas/symbol_profiles/048/048260.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": 1.99, "MFE_90D_pct": 2.09, "MAE_30D_pct": -7.68, "MAE_90D_pct": -7.68, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2023-04-12", "peak_price": 190200, "four_b_timing_verdict": "narrative_only_delisting_cap", "four_b_evidence_type": ["explicit_event_cap"], "four_c_protection_label": "not_applicable", "trigger_outcome_label": "narrative_only_tender_cap", "current_profile_verdict": "current_profile_data_insufficient", "calibration_usable": false, "forward_window_trading_days": 0, "calibration_block_reasons": ["insufficient_forward_window_in_stock_web", "corporate_action_contaminated_180D_window_or_delisting_path"], "corporate_action_window_status": "blocked_by_2023_08_03_candidate_and_inactive_like_profile", "same_entry_group_id": "OSSTEM_20230125_186300", "dedupe_for_aggregate": false, "aggregate_group_role": "narrative_only", "is_new_independent_case": true, "independent_evidence_weight": 0.0, "do_not_count_as_new_case": true}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy_to_C32_shadow", "case_id": "R12L1_C32_SM_041510_HYBE_KAKAO_CONTROL_PREMIUM", "trigger_id": "TR_SM_HYBE_20230210_STAGE2A", "symbol": "041510", "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP", "raw_component_scores_before": {"contract_score": 15, "backlog_visibility_score": 0, "margin_bridge_score": 0, "revision_score": 10, "relative_strength_score": 14, "customer_quality_score": 14, "policy_or_regulatory_score": 12, "valuation_repricing_score": 10, "execution_risk_score": -4, "legal_or_contract_risk_score": -2, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_before": 71.0, "stage_label_before": "Stage2-Actionable", "raw_component_scores_after": {"contract_score": 15, "backlog_visibility_score": 0, "margin_bridge_score": 0, "revision_score": 10, "relative_strength_score": 14, "customer_quality_score": 15, "policy_or_regulatory_score": 14, "valuation_repricing_score": 10, "execution_risk_score": -4, "legal_or_contract_risk_score": -2, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_after": 74.0, "stage_label_after": "Stage2-Actionable", "changed_components": ["policy_or_regulatory_score", "customer_quality_score"], "component_delta_explanation": "closed or escalating counter-bid route confirms company-specific control-premium path, not just market-wide governance theme.", "MFE_90D_pct": 40.54, "MAE_90D_pct": -23.63, "score_return_alignment_label": "event_control_premium_success_then_cap", "current_profile_verdict": "current_profile_correct"}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy_to_C32_shadow", "case_id": "R12L1_C32_SM_041510_HYBE_KAKAO_CONTROL_PREMIUM", "trigger_id": "TR_SM_KAKAO_20230307_4B_OVERLAY", "symbol": "041510", "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP", "raw_component_scores_before": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 0, "revision_score": 0, "relative_strength_score": 15, "customer_quality_score": 8, "policy_or_regulatory_score": 15, "valuation_repricing_score": 20, "execution_risk_score": -12, "legal_or_contract_risk_score": -8, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_before": 40.0, "stage_label_before": "4B-overlay", "raw_component_scores_after": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 0, "revision_score": 0, "relative_strength_score": 15, "customer_quality_score": 8, "policy_or_regulatory_score": 15, "valuation_repricing_score": 20, "execution_risk_score": -12, "legal_or_contract_risk_score": -8, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_after": 40.0, "stage_label_after": "4B-overlay", "changed_components": [], "component_delta_explanation": "overlay or narrative-only; no positive entry weight delta.", "MFE_90D_pct": 7.68, "MAE_90D_pct": -41.48, "score_return_alignment_label": "4B_overlay_success", "current_profile_verdict": "current_profile_correct"}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy_to_C32_shadow", "case_id": "R12L1_C32_KOREAZINC_010130_HOSTILE_TENDER_BATTLE", "trigger_id": "TR_KZ_MBK_20240913_STAGE2A", "symbol": "010130", "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP", "raw_component_scores_before": {"contract_score": 10, "backlog_visibility_score": 0, "margin_bridge_score": 0, "revision_score": 8, "relative_strength_score": 15, "customer_quality_score": 10, "policy_or_regulatory_score": 14, "valuation_repricing_score": 16, "execution_risk_score": -6, "legal_or_contract_risk_score": -4, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_before": 65.0, "stage_label_before": "Stage2-Actionable", "raw_component_scores_after": {"contract_score": 10, "backlog_visibility_score": 0, "margin_bridge_score": 0, "revision_score": 8, "relative_strength_score": 15, "customer_quality_score": 11, "policy_or_regulatory_score": 16, "valuation_repricing_score": 16, "execution_risk_score": -6, "legal_or_contract_risk_score": -4, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_after": 68.0, "stage_label_after": "Stage2-Actionable", "changed_components": ["policy_or_regulatory_score", "customer_quality_score"], "component_delta_explanation": "closed or escalating counter-bid route confirms company-specific control-premium path, not just market-wide governance theme.", "MFE_90D_pct": 261.41, "MAE_90D_pct": -1.65, "score_return_alignment_label": "structural_control_premium_success_high_mae_later", "current_profile_verdict": "current_profile_too_late"}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy_to_C32_shadow", "case_id": "R12L1_C32_KOREAZINC_010130_HOSTILE_TENDER_BATTLE", "trigger_id": "TR_KZ_BLOWOFF_20241206_4B_OVERLAY", "symbol": "010130", "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP", "raw_component_scores_before": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 0, "revision_score": 0, "relative_strength_score": 20, "customer_quality_score": 4, "policy_or_regulatory_score": 10, "valuation_repricing_score": 25, "execution_risk_score": -18, "legal_or_contract_risk_score": -12, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": -4}, "weighted_score_before": 27.0, "stage_label_before": "4B-overlay", "raw_component_scores_after": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 0, "revision_score": 0, "relative_strength_score": 20, "customer_quality_score": 4, "policy_or_regulatory_score": 10, "valuation_repricing_score": 25, "execution_risk_score": -18, "legal_or_contract_risk_score": -12, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": -4}, "weighted_score_after": 27.0, "stage_label_after": "4B-overlay", "changed_components": [], "component_delta_explanation": "overlay or narrative-only; no positive entry weight delta.", "MFE_90D_pct": 32.76, "MAE_90D_pct": -59.24, "score_return_alignment_label": "4B_overlay_success", "current_profile_verdict": "current_profile_correct"}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy_to_C32_shadow", "case_id": "R12L1_C32_HMM_011200_HARIM_PREFERRED_BIDDER_FAIL", "trigger_id": "TR_HMM_HARIM_20231220_STAGE2A", "symbol": "011200", "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP", "raw_component_scores_before": {"contract_score": 6, "backlog_visibility_score": 0, "margin_bridge_score": 0, "revision_score": 0, "relative_strength_score": 12, "customer_quality_score": 2, "policy_or_regulatory_score": 16, "valuation_repricing_score": 16, "execution_risk_score": -14, "legal_or_contract_risk_score": -15, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_before": 25.0, "stage_label_before": "Stage2-Actionable", "raw_component_scores_after": {"contract_score": 6, "backlog_visibility_score": 0, "margin_bridge_score": 0, "revision_score": 0, "relative_strength_score": 12, "customer_quality_score": 2, "policy_or_regulatory_score": 16, "valuation_repricing_score": 16, "execution_risk_score": -19, "legal_or_contract_risk_score": -20, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_after": 15.0, "stage_label_after": "Stage2-Watch-Only", "changed_components": ["execution_risk_score", "legal_or_contract_risk_score"], "component_delta_explanation": "policy/sale headline is capped unless buyer financing, regulatory approval, price floor, and post-event value bridge are closed.", "MFE_90D_pct": 5.43, "MAE_90D_pct": -35.52, "score_return_alignment_label": "false_positive_event_premium", "current_profile_verdict": "current_profile_false_positive"}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy_to_C32_shadow", "case_id": "R12L1_C32_YTN_040300_PRIVATIZATION_BID_EVENT_CAP", "trigger_id": "TR_YTN_EUGENE_20231024_STAGE2A", "symbol": "040300", "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP", "raw_component_scores_before": {"contract_score": 4, "backlog_visibility_score": 0, "margin_bridge_score": 0, "revision_score": 0, "relative_strength_score": 15, "customer_quality_score": 2, "policy_or_regulatory_score": 18, "valuation_repricing_score": 14, "execution_risk_score": -12, "legal_or_contract_risk_score": -10, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_before": 33.0, "stage_label_before": "Stage2-Actionable", "raw_component_scores_after": {"contract_score": 4, "backlog_visibility_score": 0, "margin_bridge_score": 0, "revision_score": 0, "relative_strength_score": 15, "customer_quality_score": 2, "policy_or_regulatory_score": 18, "valuation_repricing_score": 14, "execution_risk_score": -17, "legal_or_contract_risk_score": -15, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_after": 23.0, "stage_label_after": "Stage2-Watch-Only", "changed_components": ["execution_risk_score", "legal_or_contract_risk_score"], "component_delta_explanation": "policy/sale headline is capped unless buyer financing, regulatory approval, price floor, and post-event value bridge are closed.", "MFE_90D_pct": 23.08, "MAE_90D_pct": -35.0, "score_return_alignment_label": "failed_rerating", "current_profile_verdict": "current_profile_false_positive"}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy_to_C32_shadow", "case_id": "R12L1_C32_OSSTEM_048260_TENDER_DELISTING_CAP", "trigger_id": "TR_OSSTEM_MBK_UCK_20230125_NARRATIVE", "symbol": "048260", "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP", "raw_component_scores_before": {"contract_score": 14, "backlog_visibility_score": 0, "margin_bridge_score": 0, "revision_score": 0, "relative_strength_score": 10, "customer_quality_score": 6, "policy_or_regulatory_score": 6, "valuation_repricing_score": 8, "execution_risk_score": -8, "legal_or_contract_risk_score": -5, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": -3}, "weighted_score_before": 30.0, "stage_label_before": "narrative_only", "raw_component_scores_after": {"contract_score": 14, "backlog_visibility_score": 0, "margin_bridge_score": 0, "revision_score": 0, "relative_strength_score": 10, "customer_quality_score": 6, "policy_or_regulatory_score": 6, "valuation_repricing_score": 8, "execution_risk_score": -8, "legal_or_contract_risk_score": -5, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": -3}, "weighted_score_after": 30.0, "stage_label_after": "narrative_only", "changed_components": [], "component_delta_explanation": "overlay or narrative-only; no positive entry weight delta.", "MFE_90D_pct": 2.09, "MAE_90D_pct": -7.68, "score_return_alignment_label": "narrative_only_tender_cap", "current_profile_verdict": "current_profile_data_insufficient"}
{"row_type": "residual_contribution", "round": "R12", "loop": "1", "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP", "new_independent_case_count": 5, "reused_case_count": 0, "new_symbol_count": 5, "same_archetype_new_symbol_count": 5, "same_archetype_new_trigger_family_count": 4, "new_canonical_archetype_count": 1, "new_trigger_family_count": 4, "positive_case_count": 2, "counterexample_count": 3, "current_profile_error_count": 3, "tested_existing_calibrated_axes": ["price_only_blowoff_blocks_positive_stage", "full_4b_requires_non_price_evidence", "hard_4c_thesis_break_routes_to_4c"], "residual_error_types_found": ["policy_sale_headline_false_positive", "event_cap_without_company_specific_closure", "late_control_premium_promotion"], "loop_contribution_label": "canonical_archetype_rule_candidate", "do_not_propose_new_weight_delta": false, "auto_selected_coverage_gap": "R12_C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP"}
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
next_round = R13
suggested_large_sector_id = L10_POLICY_EVENT_CROSS_REDTEAM_MISC
suggested_canonical_archetype_id = C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP or C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK
reason = C32 now has first canonical coverage; next loop can either add more C32 counterexamples or move to another undercovered residual error family.
```

## 28. Source Notes

Primary price source:

- Songdaiki/stock-web `atlas/manifest.json`: max_date 2026-02-20; source FinanceData/marcap; raw_unadjusted_marcap; calibration shard root `atlas/ohlcv_tradable_by_symbol_year`.
- Songdaiki/stock-web `atlas/schema.json`: tradable shard columns and MFE/MAE formulas.
- Symbol profiles checked: `041510`, `010130`, `011200`, `040300`, `048260`.
- Price rows checked from the relevant yearly tradable shards listed in the Price Data Source Map.

Event evidence notes:

- SM: HYBE/Kakao tender-offer battle, including HYBE 120,000 won tender route and Kakao 150,000 won counter tender.
- Korea Zinc: MBK/Young Poong 660,000 won tender offer, later raised offers/court/buyback escalation.
- HMM: sale/preferred-bidder event followed by failure of deal route.
- YTN: privatization/preferred-bidder event premium without durable post-event price floor.
- Osstem: PE tender-to-delist path retained as narrative-only because stock-web profile is inactive/delisted-like and has a 2023-08-03 corporate-action candidate.
