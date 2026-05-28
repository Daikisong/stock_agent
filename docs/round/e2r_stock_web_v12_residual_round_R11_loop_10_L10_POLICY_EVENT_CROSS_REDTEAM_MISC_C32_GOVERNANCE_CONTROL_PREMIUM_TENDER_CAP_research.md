# E2R Stock-Web Historical Calibration / Sector-Archetype Residual Research Round

## 0. Research Metadata

```yaml
research_session: post_calibrated_sector_archetype_residual_research
mode: historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12
scheduled_round: R11
scheduled_loop: 10
completed_round: R11
completed_loop: 10
large_sector_id: L10_POLICY_EVENT_CROSS_REDTEAM_MISC
canonical_archetype_id: C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP
fine_archetype_id: CONTROL_PREMIUM_TENDER_CAP_GOVERNANCE_EVENT_RISK
output_file: e2r_stock_web_v12_residual_round_R11_loop_10_L10_POLICY_EVENT_CROSS_REDTEAM_MISC_C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP_research.md
production_scoring_changed: false
shadow_weight_only: true
stock_agent_code_access_allowed: false
stock_agent_code_patch_allowed: false
stock_web_price_atlas_access_required: true
```

This loop adds **4** new independent cases, **2** counterexamples, and **2** residual errors for `R11/L10_POLICY_EVENT_CROSS_REDTEAM_MISC/C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP`.

## 1. Current Calibrated Profile Assumption

`P0 = e2r_2_1_stock_web_calibrated_proxy`.

Already-applied global axes are treated as existing infrastructure, not new discoveries:

```text
stage2_actionable_evidence_bonus = +2.0
stage3_yellow_total_min = 75.0
stage3_green_total_min = 87.0
stage3_green_revision_min = 55.0
stage3_cross_evidence_green_buffer = +1.5
price_only_blowoff_blocks_positive_stage = true
full_4b_requires_non_price_evidence = true
hard_4c_thesis_break_routes_to_4c = true
```

The research question here is narrower: **when a governance/control-premium/tender event causes real upside, what keeps it from being misread as durable Stage3-Green?**

## 2. Round / Large Sector / Canonical Archetype Scope

| field | value |
|---|---|
| scheduled_round | R11 |
| scheduled_loop | 10 |
| large_sector_id | L10_POLICY_EVENT_CROSS_REDTEAM_MISC |
| canonical_archetype_id | C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP |
| fine_archetype_id | CONTROL_PREMIUM_TENDER_CAP_GOVERNANCE_EVENT_RISK |
| round_sector_consistency | pass |
| loop_objective | coverage_gap_fill, counterexample_mining, 4B_non_price_requirement_stress_test, 4C_thesis_break_timing_test, canonical_archetype_compression |

R11 is a cross/policy/event round. `C32` is valid here because the cases are not operating-sector reratings; they are **control-premium / tender / privatization / governance event** paths.

## 3. Previous Coverage / Duplicate Avoidance Check

`reports/e2r_calibration/by_round/R11.md` shows R11 already has 85 representative triggers and 27 unique cases, with many Stage2/4B/4C examples. This loop therefore avoids a generic event-premium recap and focuses on a specific residual: **binding tender premium vs. non-binding control story false Green**.

Anti-duplication status:

```text
new_independent_case_count = 4
reused_case_count = 0
new_symbol_count = 4
same_archetype_new_symbol_count = 4
same_archetype_new_trigger_family_count = 4
new_trigger_family_count = 4
```

## 4. Stock-Web OHLC Input / Price Source Validation

Manifest fields observed:

| field | value |
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
| markets | KONEX, KOSDAQ, KOSDAQ GLOBAL, KOSPI |
| calibration_shard_root | atlas/ohlcv_tradable_by_symbol_year |
| raw_shard_root | atlas/ohlcv_raw_by_symbol_year |
| schema_path | atlas/schema.json |
| universe_path | atlas/universe/all_symbols.csv |

Schema basis:

```text
tradable columns = d,o,h,l,c,v,a,mc,s,m
raw columns      = d,o,h,l,c,v,a,mc,s,m,rs
price_basis      = tradable_raw
adjustment       = raw_unadjusted_marcap
```

## 5. Historical Eligibility Gate

| symbol | company | profile_path | entry windows | corporate-action status | calibration_usable |
|---|---|---|---|---|---|
| 041510 | 에스엠 | atlas/symbol_profiles/041/041510.json | 2023-02/03 forward 180D | no 2023 event-window candidate in profile | true |
| 010130 | 고려아연 | atlas/symbol_profiles/010/010130.json | 2024-09/12 forward 180D | profile has 0 corporate-action candidate dates | true |
| 011200 | HMM | atlas/symbol_profiles/011/011200.json | 2023-12 forward 180D | candidate date 2023-11-10 precedes entry; no 180D overlap by profile list | true |
| 008930 | 한미사이언스 | atlas/symbol_profiles/008/008930.json | 2024-01 forward 180D | profile candidate dates are pre-2024 legacy events | true |

## 6. Canonical Archetype Compression Map

| fine_archetype | canonical_archetype_id | compression reason |
|---|---|---|
| control-premium binding tender | C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP | explicit price/quantity/date terms create event-premium route |
| hostile tender + legal defense | C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP | non-price 4B evidence from legal/tender mechanics |
| privatization preferred bidder | C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP | sale route may rerate, but terms/financing can break thesis |
| family-control merger dispute | C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP | event premium without binding tender is false-Green prone |

## 7. Case Selection Summary

| case_id | symbol | company | role | best trigger | current profile issue |
|---|---:|---|---|---|---|
| C32_SM_2023_TENDER_WAR | 041510 | 에스엠 | positive / 4B overlay success | C32_SM_2023_T1 | correct only if tender cap blocks Green |
| C32_KZ_2024_CONTROL_TENDER | 010130 | 고려아연 | positive / 4B overlay success | C32_KZ_2024_T1 | correct only if event premium separated from structural Green |
| C32_HMM_2023_PRIVATIZATION_SALE | 011200 | HMM | counterexample / failed rerating | C32_HMM_2023_T1 | false positive if preferred-bidder route is upgraded to Green |
| C32_HANMI_2024_CONTROL_DISPUTE | 008930 | 한미사이언스 | counterexample / false positive Green | C32_HANMI_2024_T1 | false positive if control-dispute spike is treated as durable rerating |

## 8. Positive vs Counterexample Balance

```text
positive_case_count = 2
counterexample_count = 2
4B_case_count = 2
4C_watch_or_thesis_break_case_count = 2
calibration_usable_case_count = 4
```

The key split is not “event good / event bad.” It is:

```text
binding tender + observable auction cap => Stage2-Actionable + 4B overlay
non-binding sale/control narrative + unresolved terms/legal risk => Stage2 watch, not Green
```

## 9. Evidence Source Map

| case | event evidence family | source style |
|---|---|---|
| SM | HYBE/Kakao tender competition and explicit tender price mechanics | public tender-offer/news chronology |
| Korea Zinc | MBK/Young Poong hostile tender offer, counter-offer/buyback/legal contest | public tender-offer/news chronology |
| HMM | privatization preferred-bidder route, later negotiation/terms failure | public sale/news chronology |
| Hanmi Science | OCI-Hanmi integration/control-family dispute and shareholder-control route | public merger/control-dispute chronology |

This MD uses those public events only to timestamp trigger availability. Quantitative calibration uses only stock-web OHLC rows.

## 10. Price Data Source Map

| symbol | shard(s) used | profile |
|---|---|---|
| 041510 | atlas/ohlcv_tradable_by_symbol_year/041/041510/2023.csv | atlas/symbol_profiles/041/041510.json |
| 010130 | atlas/ohlcv_tradable_by_symbol_year/010/010130/2024.csv; 2025.csv | atlas/symbol_profiles/010/010130.json |
| 011200 | atlas/ohlcv_tradable_by_symbol_year/011/011200/2023.csv; 2024.csv | atlas/symbol_profiles/011/011200.json |
| 008930 | atlas/ohlcv_tradable_by_symbol_year/008/008930/2024.csv | atlas/symbol_profiles/008/008930.json |

## 11. Case-by-Case Trigger Grid

| trigger_id | case_id | type | trigger_date | entry_date | entry_price | outcome | aggregate |
|---|---|---|---|---|---:|---|---|
| C32_SM_2023_T1 | C32_SM_2023_TENDER_WAR | Stage2-Actionable | 2023-02-10 | 2023-02-10 | 114700 | event premium success, then tender-cap drawdown | yes |
| C32_SM_2023_T2 | C32_SM_2023_TENDER_WAR | Stage4B | 2023-03-07 | 2023-03-07 | 149700 | good full-window 4B overlay | no |
| C32_KZ_2024_T1 | C32_KZ_2024_CONTROL_TENDER | Stage2-Actionable | 2024-09-13 | 2024-09-13 | 666000 | large control-premium MFE, then crash | yes |
| C32_KZ_2024_T2 | C32_KZ_2024_CONTROL_TENDER | Stage4B | 2024-12-05 | 2024-12-05 | 2000000 | good full-window 4B overlay | no |
| C32_HMM_2023_T1 | C32_HMM_2023_PRIVATIZATION_SALE | Stage2 event-premium risk watch | 2023-12-19 | 2023-12-19 | 18430 | failed rerating after local premium | yes |
| C32_HANMI_2024_T1 | C32_HANMI_2024_CONTROL_DISPUTE | Stage2 event-premium risk watch | 2024-01-15 | 2024-01-15 | 43300 | control-dispute false Green risk | yes |

## 12. Trigger-Level OHLC Backtest Tables

| trigger_id | entry | MFE30 | MAE30 | MFE90 | MAE90 | MFE180 | MAE180 | peak_date | peak_price | drawdown_after_peak |
|---|---:|---:|---:|---:|---:|---:|---:|---|---:|---:|
| C32_SM_2023_T1 | 114700 | 40.54 | -9.24 | 40.54 | -21.10 | 40.54 | -21.10 | 2023-03-08 | 161200 | -43.86 |
| C32_SM_2023_T2 | 149700 | 7.68 | -39.55 | 7.68 | -39.55 | 7.68 | -40.21 | 2023-03-08 | 161200 | -43.86 |
| C32_KZ_2024_T1 | 666000 | 131.68 | -1.65 | 261.41 | -1.65 | 261.41 | -3.45 | 2024-12-06 | 2407000 | -73.29 |
| C32_KZ_2024_T2 | 2000000 | 20.35 | -52.45 | 20.35 | -67.85 | 20.35 | -67.85 | 2024-12-06 | 2407000 | -73.29 |
| C32_HMM_2023_T1 | 18430 | 26.42 | -10.20 | 26.42 | -22.68 | 26.42 | -22.68 | 2023-12-20 | 23300 | -38.84 |
| C32_HANMI_2024_T1 | 43300 | 29.79 | -10.62 | 29.79 | -28.41 | 29.79 | -30.02 | 2024-01-16 | 56200 | -46.09 |

Representative aggregate, deduped:

```text
representative_trigger_count = 4
avg_MFE_90D_pct = 89.54
avg_MAE_90D_pct = -18.46
avg_MFE_180D_pct = 89.54
avg_MAE_180D_pct = -19.31
```

## 13. Current Calibrated Profile Stress Test

| case | P0 likely read | actual price alignment | verdict |
|---|---|---|---|
| SM | Stage2/Yellow valid; Green must be capped by tender mechanics | strong MFE, then deep drawdown from auction peak | current_profile_correct |
| Korea Zinc | Stage2 valid; Green must not be structural | extraordinary MFE and extreme post-peak drawdown | current_profile_correct |
| HMM | could over-upgrade preferred-bidder event to Yellow/Green | local spike, then deal/terms risk and MAE | current_profile_false_positive |
| Hanmi Science | could over-upgrade control-dispute price spike | large early MFE but persistent MAE after dispute | current_profile_false_positive |

Stress answers:

```text
stage2_actionable_evidence_bonus: useful only when tender/sale evidence is binding or terms-visible
stage3_yellow_total_min: adequate, but C32 needs a governance/event risk drag
stage3_green_total_min: too permissive if control-premium event is counted as durable revision
stage3_green_revision_min: should remain strict; C32 usually lacks real revision evidence
price_only_blowoff_guard: strengthened
full_4b_requires_non_price_evidence: strengthened, because tender/legal evidence is the real 4B
hard_4c_routing: kept; deal failure/terms break should route to 4C/watch
```

## 14. Stage2 / Yellow / Green Comparison

C32 behaves like a sealed-bid auction, not like a factory ramp. The first public tender/sale route can be tradable Stage2, but Green requires durable post-event economics or confirmed closeout, not just a premium headline.

| rule question | finding |
|---|---|
| Is Stage2 earlier than Green? | Yes, but this is not new; the residual is **whether Green should exist at all**. |
| Should Stage3-Green fire on tender premium? | Generally no, unless there is confirmed closeout plus post-deal EPS/asset value visibility. |
| What did Green miss? | In SM/Korea Zinc, Green would arrive close to event cap; in HMM/Hanmi, Green would be false. |
| C32 shadow rule | `binding_tender_event_can_promote_stage2_but_blocks_stage3_green_without_post_event_visibility` |

## 15. 4B Local vs Full-window Timing Audit

| trigger | local proximity | full-window proximity | verdict |
|---|---:|---:|---|
| C32_SM_2023_T2 | 0.75 | 0.75 | good_full_window_4B_timing |
| C32_KZ_2024_T2 | 0.77 | 0.77 | good_full_window_4B_timing |
| C32_HMM_2023_T1 | 1.00 | 1.00 | event premium local peak; watch/4B, not Green |
| C32_HANMI_2024_T1 | 1.00 | 1.00 | price-only/control-dispute spike; cap at watch |

C32 4B is not merely price exhaustion. It needs one of:

```text
explicit tender cap
competing tender price ceiling
legal block / injunction / hostile defense
deal-financing uncertainty
control-premium blowoff
```

## 16. 4C Protection Audit

| case | 4C / thesis-break cue | protection label |
|---|---|---|
| HMM | sale negotiation / terms risk after preferred-bidder spike | thesis_break_watch_only |
| Hanmi Science | shareholder/control route did not become clean closeout | thesis_break_watch_only |
| SM | post-auction cap and tender-result mechanics | hard_4c_not_needed_if_4B_taken |
| Korea Zinc | legal/control battle persists; 4B was primary protection | hard_4c_not_needed_if_4B_taken |

## 17. Sector-Specific Rule Candidate

```text
rule_scope = sector_specific
large_sector_id = L10_POLICY_EVENT_CROSS_REDTEAM_MISC
axis = control_premium_event_green_block_without_binding_closeout
candidate_delta = +1 risk drag / Green block
```

Rule candidate:

```text
If a C32 event is driven by control premium, tender, privatization, or governance contest:
    allow Stage2-Actionable only when public event terms are visible;
    require binding tender/price/quantity/date or legally confirmed closeout for promotion beyond watch;
    block Stage3-Green unless there is post-event financial/revision visibility independent of the event premium;
    route legal/deal failure, tender withdrawal, or financing/terms break to 4C/watch.
```

## 18. Canonical-Archetype Rule Candidate

```text
canonical_archetype_id = C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP
rule_scope = canonical_archetype_specific
proposal_type = archetype_shadow_only
```

Canonical shadow rule:

```text
C32_binding_tender_cap_guard:
    + Stage2 evidence: public tender/sale/control event with visible terms.
    + 4B overlay: explicit tender price cap, competing offer cap, legal block, or blowoff.
    - Green block: no confirmed post-event earnings/revision/asset-value bridge.
    - Risk drag: non-binding preferred bidder, family dispute, litigation, CB/dilution, financing conditions.
```

## 19. Before / After Backtest Comparison

| profile_id | scope | eligible triggers | selected entries | avg MFE90 | avg MAE90 | false positive rate | missed structural count | verdict |
|---|---|---:|---|---:|---:|---:|---:|---|
| P0 e2r_2_1_stock_web_calibrated_proxy | current proxy | 4 | all representative | 89.54 | -18.46 | 0.50 | 0 | good Stage2, weak C32 Green guard |
| P0b e2r_2_0_baseline_reference | rollback | 4 | likely later/price-heavy | 54.0 est. | -24.0 est. | 0.50 | 1 | less precise event split |
| P1 sector_specific_candidate_profile | L10 | 4 | binding event as Stage2; non-binding as watch | 150.98 on positives | -11.38 on positives | 0.00 | 0 | better score-return alignment |
| P2 canonical_archetype_candidate_profile | C32 | 4 | same as P1, C32-only | 150.98 on positives | -11.38 on positives | 0.00 | 0 | preferred |
| P3 counterexample_guard_profile | C32 guard | 4 | blocks HMM/Hanmi Green | n/a | n/a | 0.00 | 0 | guardrail-only |

## 20. Score-Return Alignment Matrix

| case | weighted before | label before | weighted after | label after | price alignment |
|---|---:|---|---:|---|---|
| SM | 78 | Stage3-Yellow | 78 | Stage2-Actionable + 4B watch | event premium tradable; Green blocked |
| Korea Zinc | 86 | Stage3 border | 82 | Stage2-Actionable + 4B watch | large MFE but extreme drawdown |
| HMM | 76 | false Yellow/Green | 66 | event-premium risk watch | avoids failed rerating |
| Hanmi Science | 77 | false Yellow/Green | 64 | event-premium risk watch | avoids control-dispute chase |

## 21. Coverage Matrix

| large_sector_id | canonical_archetype_id | fine_archetype_id | positive_case_count | counterexample_count | 4B_case_count | 4C_case_count | new_independent_case_count | reused_case_count | calibration_usable_trigger_count | representative_trigger_count | current_profile_error_count | sector_rule_candidate | canonical_rule_candidate | coverage_gap_after_this_loop |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|---|---|
| L10_POLICY_EVENT_CROSS_REDTEAM_MISC | C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP | CONTROL_PREMIUM_TENDER_CAP_GOVERNANCE_EVENT_RISK | 2 | 2 | 2 | 2 | 4 | 0 | 6 | 4 | 2 | true | true | reduced: binding vs non-binding control premium now separated |

## 22. Residual Contribution Summary

```text
new_independent_case_count: 4
reused_case_count: 0
reused_case_ids: []
new_symbol_count: 4
new_canonical_archetype_count: 0
new_fine_archetype_count: 1
new_trigger_family_count: 4
tested_existing_calibrated_axes:
  - stage2_actionable_evidence_bonus
  - full_4b_requires_non_price_evidence
  - hard_4c_thesis_break_routes_to_4c
  - price_only_blowoff_blocks_positive_stage
residual_error_types_found:
  - event_premium_false_green
  - binding_tender_cap_needed
  - deal_break_4C_watch
  - legal_governance_risk_drag
new_axis_proposed: null
existing_axis_strengthened:
  - C32 binding tender / explicit cap Green block
  - C32 non-binding sale/control story risk drag
  - full_4b_requires_non_price_evidence
existing_axis_weakened: null
existing_axis_kept:
  - stage2_actionable_evidence_bonus
  - hard_4c_thesis_break_routes_to_4c
sector_specific_rule_candidate: true
canonical_archetype_rule_candidate: true
no_new_signal_reason: null
loop_contribution_label: canonical_archetype_rule_candidate
do_not_propose_new_weight_delta: false
```

## 23. Validation Scope / Non-Validation Scope

Validated:

```text
- Stock-Web manifest/schema/profile paths
- trigger_date vs entry_date split
- actual tradable_raw OHLC rows for entry, peak, drawdown anchors
- 30D/90D/180D MFE/MAE proxy calculations
- C32 positive/counterexample balance
- local vs full-window 4B split
```

Not validated:

```text
- exact production scoring implementation
- live candidates
- broker/API routes
- source-route discovery outside historical event timestamping
- current investment attractiveness
```

## 24. Shadow Weight Calibration

```csv
row_type,axis,scope,large_sector_id,canonical_archetype_id,baseline_value,tested_value,delta,reason,backtest_effect,trigger_ids,calibration_usable_count,new_independent_case_count,counterexample_count,confidence,proposal_type,notes
shadow_weight,C32_binding_tender_cap_guard,canonical_archetype_specific,L10_POLICY_EVENT_CROSS_REDTEAM_MISC,C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP,0,1,+1,"binding tender can promote Stage2 but blocks Green without post-event visibility","reduced false Green in HMM/Hanmi while preserving SM/Korea Zinc event premium","C32_SM_2023_T1|C32_KZ_2024_T1|C32_HMM_2023_T1|C32_HANMI_2024_T1",4,4,2,medium,archetype_shadow_only,"not production; post-calibrated residual"
shadow_weight,C32_non_binding_control_story_risk_drag,canonical_archetype_specific,L10_POLICY_EVENT_CROSS_REDTEAM_MISC,C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP,0,1,+1,"preferred-bidder or family-control story without closeout has high MAE","blocks HMM/Hanmi false Yellow/Green","C32_HMM_2023_T1|C32_HANMI_2024_T1",2,2,2,medium,archetype_shadow_only,"not production; post-calibrated residual"
shadow_weight,C32_4B_explicit_event_cap,canonical_archetype_specific,L10_POLICY_EVENT_CROSS_REDTEAM_MISC,C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP,0,1,+1,"explicit tender cap/legal battle produces non-price 4B evidence","SM/Korea Zinc 4B overlay aligned with post-peak drawdown","C32_SM_2023_T2|C32_KZ_2024_T2",2,2,0,medium,archetype_shadow_only,"not production; post-calibrated residual"
```

## 25. Machine-Readable Rows

### 25.1 price_source_validation

```jsonl
{"row_type": "price_source_validation", "source": "Songdaiki/stock-web", "source_url": "https://github.com/Songdaiki/stock-web", "manifest_path": "atlas/manifest.json", "schema_path": "atlas/schema.json", "universe_path": "atlas/universe/all_symbols.csv", "manifest_max_date": "2026-02-20", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "raw_shard_root": "atlas/ohlcv_raw_by_symbol_year", "validation_status": "usable_for_historical_calibration"}
```

### 25.2 case rows

```jsonl
{"row_type": "case", "case_id": "C32_SM_2023_TENDER_WAR", "symbol": "041510", "company_name": "에스엠", "round": "R11", "loop": "10", "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP", "fine_archetype_id": "CONTROL_PREMIUM_TENDER_CAP_GOVERNANCE_EVENT_RISK", "case_type": "4B_overlay_success", "positive_or_counterexample": "positive", "best_trigger": "C32_SM_2023_T1", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "binding tender premium works only as event premium; non-binding governance stories create false Green risk", "current_profile_verdict": "current_profile_correct", "price_source": "Songdaiki/stock-web", "notes": "HYBE/Kakao control-premium tender contest. Binding tender terms produced event-premium MFE, then tender-cap/auction-end drawdown warned against treating it as durable Stage3-Green."}
{"row_type": "case", "case_id": "C32_KZ_2024_CONTROL_TENDER", "symbol": "010130", "company_name": "고려아연", "round": "R11", "loop": "10", "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP", "fine_archetype_id": "CONTROL_PREMIUM_TENDER_CAP_GOVERNANCE_EVENT_RISK", "case_type": "4B_overlay_success", "positive_or_counterexample": "positive", "best_trigger": "C32_KZ_2024_T1", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "binding tender premium works only as event premium; non-binding governance stories create false Green risk", "current_profile_verdict": "current_profile_correct", "price_source": "Songdaiki/stock-web", "notes": "MBK/Young Poong tender offer and Korea Zinc countermeasures generated a large control-premium repricing; the price path demanded explicit 4B separation from structural Green."}
{"row_type": "case", "case_id": "C32_HMM_2023_PRIVATIZATION_SALE", "symbol": "011200", "company_name": "HMM", "round": "R11", "loop": "10", "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP", "fine_archetype_id": "CONTROL_PREMIUM_TENDER_CAP_GOVERNANCE_EVENT_RISK", "case_type": "failed_rerating", "positive_or_counterexample": "counterexample", "best_trigger": "C32_HMM_2023_T1", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "binding tender premium works only as event premium; non-binding governance stories create false Green risk", "current_profile_verdict": "current_profile_false_positive", "price_source": "Songdaiki/stock-web", "notes": "Privatization/preferred-bidder premium spiked and faded as deal certainty and financing/terms risk dominated. Event-premium watch should not be Green."}
{"row_type": "case", "case_id": "C32_HANMI_2024_CONTROL_DISPUTE", "symbol": "008930", "company_name": "한미사이언스", "round": "R11", "loop": "10", "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP", "fine_archetype_id": "CONTROL_PREMIUM_TENDER_CAP_GOVERNANCE_EVENT_RISK", "case_type": "false_positive_green", "positive_or_counterexample": "counterexample", "best_trigger": "C32_HANMI_2024_T1", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "binding tender premium works only as event premium; non-binding governance stories create false Green risk", "current_profile_verdict": "current_profile_false_positive", "price_source": "Songdaiki/stock-web", "notes": "OCI-Hanmi integration/control-family dispute produced a sharp event repricing but no clean binding tender closeout; forward MAE was large and durable Green was not justified."}
```

### 25.3 trigger rows

```jsonl
{"row_type": "trigger", "trigger_id": "C32_SM_2023_T1", "case_id": "C32_SM_2023_TENDER_WAR", "symbol": "041510", "company_name": "에스엠", "round": "R11", "loop": "10", "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP", "fine_archetype_id": "CONTROL_PREMIUM_TENDER_CAP_GOVERNANCE_EVENT_RISK", "sector": "policy_event_governance_control_premium", "primary_archetype": "governance_control_premium_tender_cap", "loop_objective": "coverage_gap_fill|counterexample_mining|4B_non_price_requirement_stress_test|4C_thesis_break_timing_test|canonical_archetype_compression", "trigger_type": "Stage2-Actionable", "trigger_date": "2023-02-10", "evidence_available_at_that_date": "HYBE stake acquisition/tender-offer route made control-premium evidence public; later Kakao counter-tender confirmed auction mechanics.", "evidence_source": "public tender-offer/news chronology; stock-web shard row 2023-02-10 c=114700", "stage2_evidence_fields": ["public_event_or_disclosure", "customer_or_order_quality", "policy_or_regulatory_optionality"], "stage3_evidence_fields": ["multiple_public_sources"], "stage4b_evidence_fields": ["valuation_blowoff", "control_premium_or_event_premium"], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/041/041510/2023.csv", "profile_path": "atlas/symbol_profiles/041/041510.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "entry_date": "2023-02-10", "entry_price": 114700, "MFE_30D_pct": 40.54, "MFE_90D_pct": 40.54, "MFE_180D_pct": 40.54, "MFE_1Y_pct": 40.54, "MFE_2Y_pct": null, "MAE_30D_pct": -9.24, "MAE_90D_pct": -21.1, "MAE_180D_pct": -21.1, "MAE_1Y_pct": -28.07, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2023-03-08", "peak_price": 161200, "drawdown_after_peak_pct": -43.86, "green_lateness_ratio": 0.75, "four_b_local_peak_proximity": null, "four_b_full_window_peak_proximity": null, "four_b_timing_verdict": "not_4B_trigger_representative_entry", "four_b_evidence_type": ["control_premium_or_event_premium"], "four_c_protection_label": "not_applicable", "trigger_outcome_label": "event_premium_success_then_tender_cap_drawdown", "current_profile_verdict": "current_profile_correct", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window", "same_entry_group_id": "SM_2023_2023-02-10_114700", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false}
{"row_type": "trigger", "trigger_id": "C32_SM_2023_T2", "case_id": "C32_SM_2023_TENDER_WAR", "symbol": "041510", "company_name": "에스엠", "round": "R11", "loop": "10", "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP", "fine_archetype_id": "CONTROL_PREMIUM_TENDER_CAP_GOVERNANCE_EVENT_RISK", "sector": "policy_event_governance_control_premium", "primary_archetype": "governance_control_premium_tender_cap", "loop_objective": "coverage_gap_fill|counterexample_mining|4B_non_price_requirement_stress_test|4C_thesis_break_timing_test|canonical_archetype_compression", "trigger_type": "Stage4B", "trigger_date": "2023-03-07", "evidence_available_at_that_date": "Kakao's higher tender price created a visible auction cap and event-premium blowoff zone.", "evidence_source": "public tender-offer/news chronology; stock-web shard row 2023-03-07 c=149700", "stage2_evidence_fields": ["public_event_or_disclosure"], "stage3_evidence_fields": [], "stage4b_evidence_fields": ["valuation_blowoff", "control_premium_or_event_premium", "explicit_event_cap"], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/041/041510/2023.csv", "profile_path": "atlas/symbol_profiles/041/041510.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "entry_date": "2023-03-07", "entry_price": 149700, "MFE_30D_pct": 7.68, "MFE_90D_pct": 7.68, "MFE_180D_pct": 7.68, "MFE_1Y_pct": 7.68, "MFE_2Y_pct": null, "MAE_30D_pct": -39.55, "MAE_90D_pct": -39.55, "MAE_180D_pct": -40.21, "MAE_1Y_pct": -44.89, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2023-03-08", "peak_price": 161200, "drawdown_after_peak_pct": -43.86, "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": 0.75, "four_b_full_window_peak_proximity": 0.75, "four_b_timing_verdict": "good_full_window_4B_timing", "four_b_evidence_type": ["valuation_blowoff", "control_premium_or_event_premium", "explicit_event_cap"], "four_c_protection_label": "not_applicable", "trigger_outcome_label": "good_4B_overlay", "current_profile_verdict": "current_profile_correct", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window", "same_entry_group_id": "SM_2023_2023-03-07_149700", "dedupe_for_aggregate": false, "aggregate_group_role": "4B_overlay_only", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 0.25, "do_not_count_as_new_case": false}
{"row_type": "trigger", "trigger_id": "C32_KZ_2024_T1", "case_id": "C32_KZ_2024_CONTROL_TENDER", "symbol": "010130", "company_name": "고려아연", "round": "R11", "loop": "10", "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP", "fine_archetype_id": "CONTROL_PREMIUM_TENDER_CAP_GOVERNANCE_EVENT_RISK", "sector": "policy_event_governance_control_premium", "primary_archetype": "governance_control_premium_tender_cap", "loop_objective": "coverage_gap_fill|counterexample_mining|4B_non_price_requirement_stress_test|4C_thesis_break_timing_test|canonical_archetype_compression", "trigger_type": "Stage2-Actionable", "trigger_date": "2024-09-13", "evidence_available_at_that_date": "MBK/Young Poong tender offer at 660,000 won made a binding control-premium route public.", "evidence_source": "public tender-offer/news chronology; stock-web shard row 2024-09-13 c=666000", "stage2_evidence_fields": ["public_event_or_disclosure", "policy_or_regulatory_optionality"], "stage3_evidence_fields": ["multiple_public_sources"], "stage4b_evidence_fields": ["valuation_blowoff", "control_premium_or_event_premium", "legal_or_regulatory_block"], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/010/010130/2024.csv", "profile_path": "atlas/symbol_profiles/010/010130.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "entry_date": "2024-09-13", "entry_price": 666000, "MFE_30D_pct": 131.68, "MFE_90D_pct": 261.41, "MFE_180D_pct": 261.41, "MFE_1Y_pct": 261.41, "MFE_2Y_pct": null, "MAE_30D_pct": -1.65, "MAE_90D_pct": -1.65, "MAE_180D_pct": -3.45, "MAE_1Y_pct": -3.45, "below_entry_price_flag_30D": false, "below_entry_price_flag_90D": false, "peak_date": "2024-12-06", "peak_price": 2407000, "drawdown_after_peak_pct": -73.29, "green_lateness_ratio": 0.77, "four_b_local_peak_proximity": null, "four_b_full_window_peak_proximity": null, "four_b_timing_verdict": "not_4B_trigger_representative_entry", "four_b_evidence_type": ["control_premium_or_event_premium"], "four_c_protection_label": "not_applicable", "trigger_outcome_label": "large_control_premium_success_then_crash", "current_profile_verdict": "current_profile_correct", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window", "same_entry_group_id": "KZ_2024_2024-09-13_666000", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false}
{"row_type": "trigger", "trigger_id": "C32_KZ_2024_T2", "case_id": "C32_KZ_2024_CONTROL_TENDER", "symbol": "010130", "company_name": "고려아연", "round": "R11", "loop": "10", "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP", "fine_archetype_id": "CONTROL_PREMIUM_TENDER_CAP_GOVERNANCE_EVENT_RISK", "sector": "policy_event_governance_control_premium", "primary_archetype": "governance_control_premium_tender_cap", "loop_objective": "coverage_gap_fill|counterexample_mining|4B_non_price_requirement_stress_test|4C_thesis_break_timing_test|canonical_archetype_compression", "trigger_type": "Stage4B", "trigger_date": "2024-12-05", "evidence_available_at_that_date": "Control battle, buyback/tender mechanics, legal uncertainty and parabolic valuation made the event cap explicit.", "evidence_source": "stock-web shard row 2024-12-05 c=2000000; public tender-offer/legal battle chronology", "stage2_evidence_fields": ["public_event_or_disclosure"], "stage3_evidence_fields": [], "stage4b_evidence_fields": ["valuation_blowoff", "positioning_overheat", "legal_or_regulatory_block", "control_premium_or_event_premium"], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/010/010130/2024.csv", "profile_path": "atlas/symbol_profiles/010/010130.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "entry_date": "2024-12-05", "entry_price": 2000000, "MFE_30D_pct": 20.35, "MFE_90D_pct": 20.35, "MFE_180D_pct": 20.35, "MFE_1Y_pct": 20.35, "MFE_2Y_pct": null, "MAE_30D_pct": -52.45, "MAE_90D_pct": -67.85, "MAE_180D_pct": -67.85, "MAE_1Y_pct": -67.85, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2024-12-06", "peak_price": 2407000, "drawdown_after_peak_pct": -73.29, "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": 0.77, "four_b_full_window_peak_proximity": 0.77, "four_b_timing_verdict": "good_full_window_4B_timing", "four_b_evidence_type": ["valuation_blowoff", "positioning_overheat", "legal_or_regulatory_block", "control_premium_or_event_premium"], "four_c_protection_label": "not_applicable", "trigger_outcome_label": "good_4B_overlay", "current_profile_verdict": "current_profile_correct", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window", "same_entry_group_id": "KZ_2024_2024-12-05_2000000", "dedupe_for_aggregate": false, "aggregate_group_role": "4B_overlay_only", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 0.25, "do_not_count_as_new_case": false}
{"row_type": "trigger", "trigger_id": "C32_HMM_2023_T1", "case_id": "C32_HMM_2023_PRIVATIZATION_SALE", "symbol": "011200", "company_name": "HMM", "round": "R11", "loop": "10", "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP", "fine_archetype_id": "CONTROL_PREMIUM_TENDER_CAP_GOVERNANCE_EVENT_RISK", "sector": "policy_event_governance_control_premium", "primary_archetype": "governance_control_premium_tender_cap", "loop_objective": "coverage_gap_fill|counterexample_mining|4B_non_price_requirement_stress_test|4C_thesis_break_timing_test|canonical_archetype_compression", "trigger_type": "Stage2_event_premium_risk_watch", "trigger_date": "2023-12-19", "evidence_available_at_that_date": "Preferred-bidder/sale-route evidence became public, but deal terms, CB/dilution and state-seller negotiation risk kept it below Green.", "evidence_source": "public sale-preferred-bidder chronology; stock-web shard row 2023-12-19 c=18430", "stage2_evidence_fields": ["public_event_or_disclosure", "policy_or_regulatory_optionality"], "stage3_evidence_fields": [], "stage4b_evidence_fields": ["control_premium_or_event_premium", "dilution_or_cb", "capital_raise_or_overhang"], "stage4c_evidence_fields": ["thesis_evidence_broken"], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/011/011200/2023.csv", "profile_path": "atlas/symbol_profiles/011/011200.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "entry_date": "2023-12-19", "entry_price": 18430, "MFE_30D_pct": 26.42, "MFE_90D_pct": 26.42, "MFE_180D_pct": 26.42, "MFE_1Y_pct": 26.42, "MFE_2Y_pct": null, "MAE_30D_pct": -10.2, "MAE_90D_pct": -22.68, "MAE_180D_pct": -22.68, "MAE_1Y_pct": -22.68, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2023-12-20", "peak_price": 23300, "drawdown_after_peak_pct": -38.84, "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": 1.0, "four_b_full_window_peak_proximity": 1.0, "four_b_timing_verdict": "event_premium_local_peak_but_no_durable_green", "four_b_evidence_type": ["control_premium_or_event_premium", "dilution_or_cb", "capital_raise_or_overhang"], "four_c_protection_label": "thesis_break_watch_only", "trigger_outcome_label": "failed_rerating_after_event_premium", "current_profile_verdict": "current_profile_false_positive", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window", "same_entry_group_id": "HMM_2023_2023-12-19_18430", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false}
{"row_type": "trigger", "trigger_id": "C32_HANMI_2024_T1", "case_id": "C32_HANMI_2024_CONTROL_DISPUTE", "symbol": "008930", "company_name": "한미사이언스", "round": "R11", "loop": "10", "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP", "fine_archetype_id": "CONTROL_PREMIUM_TENDER_CAP_GOVERNANCE_EVENT_RISK", "sector": "policy_event_governance_control_premium", "primary_archetype": "governance_control_premium_tender_cap", "loop_objective": "coverage_gap_fill|counterexample_mining|4B_non_price_requirement_stress_test|4C_thesis_break_timing_test|canonical_archetype_compression", "trigger_type": "Stage2_event_premium_risk_watch", "trigger_date": "2024-01-15", "evidence_available_at_that_date": "OCI-Hanmi integration/control-dispute evidence created event premium, but no binding tender closeout or low-red-team governance path existed.", "evidence_source": "public merger/control-dispute chronology; stock-web shard row 2024-01-15 c=43300", "stage2_evidence_fields": ["public_event_or_disclosure", "policy_or_regulatory_optionality"], "stage3_evidence_fields": [], "stage4b_evidence_fields": ["control_premium_or_event_premium", "legal_or_regulatory_block", "positioning_overheat"], "stage4c_evidence_fields": ["thesis_evidence_broken"], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/008/008930/2024.csv", "profile_path": "atlas/symbol_profiles/008/008930.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "entry_date": "2024-01-15", "entry_price": 43300, "MFE_30D_pct": 29.79, "MFE_90D_pct": 29.79, "MFE_180D_pct": 29.79, "MFE_1Y_pct": 29.79, "MFE_2Y_pct": null, "MAE_30D_pct": -10.62, "MAE_90D_pct": -28.41, "MAE_180D_pct": -30.02, "MAE_1Y_pct": -34.87, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2024-01-16", "peak_price": 56200, "drawdown_after_peak_pct": -46.09, "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": 1.0, "four_b_full_window_peak_proximity": 1.0, "four_b_timing_verdict": "price_only_local_4B_too_early_without_binding_tender", "four_b_evidence_type": ["control_premium_or_event_premium", "legal_or_regulatory_block", "positioning_overheat"], "four_c_protection_label": "thesis_break_watch_only", "trigger_outcome_label": "control_dispute_false_positive_green", "current_profile_verdict": "current_profile_false_positive", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window", "same_entry_group_id": "HANMI_2024_2024-01-15_43300", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false}
```

### 25.4 score_simulation rows

```jsonl
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "C32_SM_2023_TENDER_WAR", "trigger_id": "C32_SM_2023_T1", "symbol": "041510", "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP", "raw_component_scores_before": {"contract_score": 20, "backlog_visibility_score": 0, "margin_bridge_score": 0, "revision_score": 0, "relative_strength_score": 0, "customer_quality_score": 0, "policy_or_regulatory_score": 16, "valuation_repricing_score": 18, "execution_risk_score": 8, "legal_or_contract_risk_score": 4, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_before": 78, "stage_label_before": "Stage3-Yellow", "raw_component_scores_after": {"contract_score": 20, "backlog_visibility_score": 0, "margin_bridge_score": 0, "revision_score": 0, "relative_strength_score": 0, "customer_quality_score": 0, "policy_or_regulatory_score": 16, "valuation_repricing_score": 18, "execution_risk_score": 8, "legal_or_contract_risk_score": 4, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_after": 78, "stage_label_after": "Stage2-Actionable+4B_watch", "changed_components": ["stage3_green_block_if_control_premium_has_explicit_tender_cap"], "component_delta_explanation": "Binding tender supports event entry, but explicit cap blocks durable Green.", "MFE_90D_pct": 40.54, "MAE_90D_pct": -21.1, "score_return_alignment_label": "aligned_after_C32_event_cap_guard", "current_profile_verdict": "current_profile_correct"}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "C32_KZ_2024_CONTROL_TENDER", "trigger_id": "C32_KZ_2024_T1", "symbol": "010130", "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP", "raw_component_scores_before": {"contract_score": 22, "backlog_visibility_score": 0, "margin_bridge_score": 0, "revision_score": 0, "relative_strength_score": 18, "customer_quality_score": 0, "policy_or_regulatory_score": 20, "valuation_repricing_score": 22, "execution_risk_score": 0, "legal_or_contract_risk_score": 6, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_before": 86, "stage_label_before": "Stage3-Yellow/Green-border", "raw_component_scores_after": {"contract_score": 22, "backlog_visibility_score": 0, "margin_bridge_score": 0, "revision_score": 0, "relative_strength_score": 18, "customer_quality_score": 0, "policy_or_regulatory_score": 20, "valuation_repricing_score": 22, "execution_risk_score": 0, "legal_or_contract_risk_score": 10, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_after": 82, "stage_label_after": "Stage2-Actionable+4B_watch", "changed_components": ["legal/governance-risk drag", "explicit tender-cap overlay"], "component_delta_explanation": "Large MFE validates event premium, not a production Green rerating.", "MFE_90D_pct": 261.41, "MAE_90D_pct": -1.65, "score_return_alignment_label": "aligned_after_C32_event_cap_guard", "current_profile_verdict": "current_profile_correct"}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "C32_HMM_2023_PRIVATIZATION_SALE", "trigger_id": "C32_HMM_2023_T1", "symbol": "011200", "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP", "raw_component_scores_before": {"contract_score": 12, "backlog_visibility_score": 0, "margin_bridge_score": 0, "revision_score": 0, "relative_strength_score": 0, "customer_quality_score": 0, "policy_or_regulatory_score": 17, "valuation_repricing_score": 15, "execution_risk_score": 0, "legal_or_contract_risk_score": 12, "dilution_cb_risk_score": 14, "accounting_trust_risk_score": 0}, "weighted_score_before": 76, "stage_label_before": "Stage3-Yellow_false_positive", "raw_component_scores_after": {"contract_score": 12, "backlog_visibility_score": 0, "margin_bridge_score": 0, "revision_score": 0, "relative_strength_score": 0, "customer_quality_score": 0, "policy_or_regulatory_score": 17, "valuation_repricing_score": 15, "execution_risk_score": 0, "legal_or_contract_risk_score": 18, "dilution_cb_risk_score": 20, "accounting_trust_risk_score": 0}, "weighted_score_after": 66, "stage_label_after": "Stage2_event_premium_risk_watch", "changed_components": ["seller/terms certainty requirement", "CB/dilution drag"], "component_delta_explanation": "Preferred-bidder premium faded; missing binding closeout and dilution overhang block Green.", "MFE_90D_pct": 26.42, "MAE_90D_pct": -22.68, "score_return_alignment_label": "aligned_after_C32_event_cap_guard", "current_profile_verdict": "current_profile_false_positive"}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "C32_HANMI_2024_CONTROL_DISPUTE", "trigger_id": "C32_HANMI_2024_T1", "symbol": "008930", "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP", "raw_component_scores_before": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 0, "revision_score": 0, "relative_strength_score": 18, "customer_quality_score": 0, "policy_or_regulatory_score": 12, "valuation_repricing_score": 19, "execution_risk_score": 0, "legal_or_contract_risk_score": 14, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_before": 77, "stage_label_before": "Stage3-Yellow_false_positive", "raw_component_scores_after": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 0, "revision_score": 0, "relative_strength_score": 18, "customer_quality_score": 0, "policy_or_regulatory_score": 12, "valuation_repricing_score": 19, "execution_risk_score": 0, "legal_or_contract_risk_score": 22, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_after": 64, "stage_label_after": "Stage2_event_premium_risk_watch", "changed_components": ["binding tender / clean closeout requirement", "family-control dispute risk drag"], "component_delta_explanation": "Event premium spike had large subsequent MAE and lacked tender closeout certainty.", "MFE_90D_pct": 29.79, "MAE_90D_pct": -28.41, "score_return_alignment_label": "aligned_after_C32_event_cap_guard", "current_profile_verdict": "current_profile_false_positive"}
```

### 25.5 shadow_weight rows

See CSV in section 24.

### 25.6 residual_contribution row

```jsonl
{"row_type": "residual_contribution", "round": "R11", "loop": "10", "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP", "new_independent_case_count": 4, "reused_case_count": 0, "new_symbol_count": 4, "new_trigger_family_count": 4, "tested_existing_calibrated_axes": ["stage2_actionable_evidence_bonus", "full_4b_requires_non_price_evidence", "hard_4c_thesis_break_routes_to_4c", "price_only_blowoff_blocks_positive_stage"], "residual_error_types_found": ["event_premium_false_green", "binding_tender_cap_needed", "deal_break_4C_watch", "legal_governance_risk_drag"], "loop_contribution_label": "canonical_archetype_rule_candidate", "do_not_propose_new_weight_delta": false}
```

### 25.7 narrative_only rows

```jsonl
{"row_type":"narrative_only","case_id":"C32_SOURCE_ENRICHMENT_LATER","symbol":"000000","large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP","reason":"source-route enrichment for exact disclosure timestamps can be added in later batch; price calibration rows above are usable","price_source":"Songdaiki/stock-web","usage":"not_weight_calibration"}
```

## 26. Deferred Coding Agent Handoff Prompt

### Purpose

You are now in the repository implementation phase. The attached Markdown files are v12 post-calibrated residual research outputs produced using the Songdaiki/stock-web OHLC atlas.

These MDs are not live candidate research. They are historical calibration research designed to extend the already-applied `e2r_2_1_stock_web_calibrated` profile.

Do not blindly apply every shadow row. Ingest the machine-readable rows and update the sector/canonical-archetype calibration ledger.

### Price source context

- Primary historical price source used by the research MD: Songdaiki/stock-web.
- Price basis: tradable_raw.
- Price adjustment status: raw_unadjusted_marcap.
- Price shard pattern: `atlas/ohlcv_tradable_by_symbol_year/<prefix>/<ticker>/<year>.csv`.
- Symbol profile pattern: `atlas/symbol_profiles/<prefix>/<ticker>.json`.

### Rules

- Use only `calibration_usable=true` rows for quantitative calibration.
- Do not count reused cases as new independent evidence unless `independent_evidence_weight > 0`.
- Do not treat `schema_rematerialization_only` or `duplicate_low_value_loop` as new evidence.
- Do not apply global deltas unless multiple `large_sector_id` values support the same direction.
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

Stock-Web source files inspected:

```text
atlas/manifest.json
atlas/schema.json
atlas/symbol_profiles/010/010130.json
atlas/symbol_profiles/041/041510.json
atlas/symbol_profiles/011/011200.json
atlas/symbol_profiles/008/008930.json
atlas/ohlcv_tradable_by_symbol_year/010/010130/2024.csv
atlas/ohlcv_tradable_by_symbol_year/010/010130/2025.csv
atlas/ohlcv_tradable_by_symbol_year/041/041510/2023.csv
atlas/ohlcv_tradable_by_symbol_year/011/011200/2023.csv
atlas/ohlcv_tradable_by_symbol_year/011/011200/2024.csv
atlas/ohlcv_tradable_by_symbol_year/008/008930/2024.csv
```

External event chronology was used only to set historical trigger dates. The numerical backtest is based on stock-web `tradable_raw` OHLC rows.

