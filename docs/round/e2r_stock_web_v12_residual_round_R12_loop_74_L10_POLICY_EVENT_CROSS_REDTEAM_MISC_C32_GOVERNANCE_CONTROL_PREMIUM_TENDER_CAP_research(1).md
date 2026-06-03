# E2R Stock-Web Historical Calibration / Sector-Archetype Residual Research Round

## 0. Research Metadata

```text
mode = historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12
research_session = post_calibrated_sector_archetype_residual_research
scheduled_round = R12
scheduled_loop = 74
completed_round = R12
completed_loop = 74
large_sector_id = L10_POLICY_EVENT_CROSS_REDTEAM_MISC
canonical_archetype_id = C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP
fine_archetype_id = TARGET_VS_BIDDER_TENDER_CONTROL_PREMIUM_SPLIT
output_file = e2r_stock_web_v12_residual_round_R12_loop_74_L10_POLICY_EVENT_CROSS_REDTEAM_MISC_C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP_research.md
round_schedule_status = valid
round_sector_consistency = pass
production_scoring_changed = false
shadow_weight_only = true
handoff_prompt_embedded = true
handoff_prompt_executed_now = false
```

This loop adds 3 new independent calibration-usable cases, 1 calibration-usable counterexample, 1 narrative-only blocked counterexample, and 2 residual errors for R12/L10_POLICY_EVENT_CROSS_REDTEAM_MISC/C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP.

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

The residual question is not whether Stage2 is earlier than Green. The question is whether a C32 control-premium headline belongs to the equity being scored. In a takeover battle, the target may receive a cash/control premium, while the bidder may carry funding, integration, dilution, regulatory, or overpayment risk.

## 2. Round / Large Sector / Canonical Archetype Scope

| field | value |
|---|---|
| scheduled_round | R12 |
| scheduled_loop | 74 |
| selected large_sector_id | L10_POLICY_EVENT_CROSS_REDTEAM_MISC |
| canonical_archetype_id | C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP |
| fine_archetype_id | TARGET_VS_BIDDER_TENDER_CONTROL_PREMIUM_SPLIT |
| loop_objective | sector_specific_rule_discovery; canonical_archetype_compression; counterexample_mining; coverage_gap_fill; 4B_non_price_requirement_stress_test |
| next_round | R13 |
| next_loop | 74 |

## 3. Previous Coverage / Duplicate Avoidance Check

Allowed stock_agent artifact access was restricted to research outputs and the stock-web atlas. The immediately previous local output was R11 / Loop 74 and pointed to next_round=R12. This R12 file avoids the prior R11 C31 value-up-policy axis and uses a different canonical archetype, C32.

```text
same_canonical_archetype_research = allowed
same_symbol_same_trigger_date_research = avoided
minimum_new_independent_case_ratio = 1.00 among calibration-usable representative cases
new_symbol_count = 4 including 1 narrative-only blocked symbol
new_independent_case_count = 3
reused_case_count = 0
```

## 4. Stock-Web OHLC Input / Price Source Validation

```text
source = Songdaiki/stock-web
source_basis = FinanceData/marcap transformed into assistant-readable symbol-year CSV shards
source_name = FinanceData/marcap
source_repo_url = https://github.com/FinanceData/marcap
price_adjustment_status = raw_unadjusted_marcap
min_date = 1995-05-02
max_date = 2026-02-20
tradable_row_count = 14354401
raw_row_count = 15214118
symbol_count = 5414
active_like_symbol_count = 2868
inactive_or_delisted_like_symbol_count = 2546
markets = KONEX | KOSDAQ | KOSDAQ GLOBAL | KOSPI
calibration_shard_root = atlas/ohlcv_tradable_by_symbol_year
raw_shard_root = atlas/ohlcv_raw_by_symbol_year
schema_path = atlas/schema.json
universe_path = atlas/universe/all_symbols.csv
price_basis = tradable_raw
```

The stock-web manifest states that raw/unadjusted OHLC is used, zero-volume and invalid OHLC rows are excluded from calibration shards, and corporate-action-contaminated windows are blocked by default.

## 5. Historical Eligibility Gate

| case_id | symbol | entry_date | entry in tradable shard | 180D available by manifest max_date | corporate-action 180D status | calibration_usable |
|---|---:|---:|---|---|---|---|
| C32_SM_2023_TARGET_TENDER_WAR | 041510 | 2023-02-10 | yes | yes | clean_180D_window | true |
| C32_KOREAZINC_2024_TARGET_HOSTILE_TENDER | 010130 | 2024-09-13 | yes | yes | clean_180D_window | true |
| C32_KAKAO_2023_BIDDER_TENDER_COUNTEREXAMPLE | 035720 | 2023-03-07 | yes | yes | clean_180D_window | true |
| C32_YOUNGPOONG_2024_BIDDER_SPILLOVER_NARRATIVE | 000670 | 2024-09-13 | yes | yes | blocked: 2025-04-25 inside 180D | false |

## 6. Canonical Archetype Compression Map

| fine_archetype_id | canonical_archetype_id | compression note |
|---|---|---|
| TARGET_CASH_TENDER_CONTROL_PREMIUM | C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP | target receives direct cash/control premium; positive scoring allowed if event is public and clean |
| HOSTILE_TENDER_WITH_COUNTER_BID | C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP | target rerating may extend beyond first tender price when squeeze/counterbid remains |
| BIDDER_CASH_OUTFLOW_CONTROL_RISK | C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP | same headline must not be treated as positive target premium for bidder equity |
| HOLDER_SIDE_SPILLOVER | C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP | not calibration-usable here because Young Poong 180D window is corporate-action blocked |

## 7. Case Selection Summary

| case_id | role | symbol | company | trigger family | why selected |
|---|---|---:|---|---|---|
| C32_SM_2023_TARGET_TENDER_WAR | positive | 041510 | 에스엠 | target-company competing tender | direct target control premium; large MFE before Green confirmation |
| C32_KOREAZINC_2024_TARGET_HOSTILE_TENDER | positive + 4B stress | 010130 | 고려아연 | hostile tender and counter-offer squeeze | target premium expanded far beyond first offer; non-price 4B was locally real but full-window early |
| C32_KAKAO_2023_BIDDER_TENDER_COUNTEREXAMPLE | counterexample | 035720 | 카카오 | bidder-side cash tender | same event is negative/ambiguous for the acquirer; target/bidder split needed |
| C32_YOUNGPOONG_2024_BIDDER_SPILLOVER_NARRATIVE | narrative-only counterexample | 000670 | 영풍 | bidder/holder-side spillover | useful guardrail example, but corporate-action blocked in 180D |

## 8. Positive vs Counterexample Balance

```text
positive_case_count = 2
counterexample_count = 1 calibration-usable + 1 narrative-only blocked
4B_case_count = 1
4C_case_count = 0
calibration_usable_case_count = 3
calibration_usable_trigger_count = 5
representative_trigger_count = 3
```

## 9. Evidence Source Map

| case | evidence timing | source summary |
|---|---|---|
| 에스엠 | 2023-02-10 / 2023-03-07 | HYBE became a major/controlling-route bidder; Kakao then offered a competing 150,000 KRW/share tender for up to 35% of SM. |
| 고려아연 | 2024-09-13 / 2024-10-31 | MBK/Young Poong launched a 660,000 KRW tender; later share-issuance/FSS investigation supplied non-price 4B evidence. |
| 카카오 | 2023-03-07 | Kakao was the bidder paying cash for SM shares, so the same control-premium event should not promote Kakao as a target-premium recipient. |
| 영풍 | 2024-09-13 | Young Poong bidder/holder side reacted sharply, but stock-web profile blocks the forward 180D calibration window. |

## 10. Price Data Source Map

| symbol | company | profile_path | tradable shard(s) used | profile status |
|---:|---|---|---|---|
| 041510 | 에스엠 | atlas/symbol_profiles/041/041510.json | atlas/ohlcv_tradable_by_symbol_year/041/041510/2023.csv; 2024.csv | active_like; no 2023/2024 CA overlap |
| 010130 | 고려아연 | atlas/symbol_profiles/010/010130.json | atlas/ohlcv_tradable_by_symbol_year/010/010130/2024.csv; 2025.csv | active_like; corporate_action_candidate_count=0 |
| 035720 | 카카오 | atlas/symbol_profiles/035/035720.json | atlas/ohlcv_tradable_by_symbol_year/035/035720/2023.csv | active_like; CA candidates are outside 2023 180D window |
| 000670 | 영풍 | atlas/symbol_profiles/000/000670.json | atlas/ohlcv_tradable_by_symbol_year/000/000670/2024.csv; 2025.csv | active_like; 2025-04-25 CA candidate blocks 180D |

## 11. Case-by-Case Trigger Grid

| trigger_id | symbol | trigger_type | trigger_date | entry_date | entry_price | case role | current_profile_verdict | dedupe |
|---|---:|---|---:|---:|---:|---|---|---|
| T_C32_SM_STAGE2_2023_02_10 | 041510 | Stage2-Actionable | 2023-02-10 | 2023-02-10 | 114700 | structural_success | current_profile_correct | representative |
| T_C32_SM_GREEN_2023_03_07 | 041510 | Stage3-Green comparison | 2023-03-07 | 2023-03-07 | 149700 | label comparison | current_profile_too_late | label_comparison_only |
| T_C32_KZ_STAGE2_2024_09_13 | 010130 | Stage2-Actionable | 2024-09-13 | 2024-09-13 | 666000 | structural_success | current_profile_correct | representative |
| T_C32_KZ_4B_2024_10_31 | 010130 | Stage4B overlay | 2024-10-31 | 2024-10-31 | 998000 | 4B_too_early | current_profile_4B_too_early | 4B_overlay_only |
| T_C32_KAKAO_BIDDER_2023_03_07 | 035720 | Stage2 counterexample | 2023-03-07 | 2023-03-07 | 61500 | failed_rerating | current_profile_false_positive | representative |

## 12. Trigger-Level OHLC Backtest Tables

| trigger_id | entry | MFE_30D | MAE_30D | MFE_90D | MAE_90D | MFE_180D | MAE_180D | MFE_1Y | MFE_2Y | peak_date | peak_price | drawdown_after_peak |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| T_C32_SM_STAGE2_2023_02_10 | 114700 | 40.54 | -9.24 | 40.54 | -23.63 | 40.54 | -23.63 | 40.54 | 40.54 | 2023-03-08 | 161200 | -45.66 |
| T_C32_SM_GREEN_2023_03_07 | 149700 | 7.68 | -41.48 | 7.68 | -41.48 | 7.68 | -41.48 | 7.68 | 7.68 | 2023-03-08 | 161200 | -45.66 |
| T_C32_KZ_STAGE2_2024_09_13 | 666000 | 131.68 | -1.65 | 261.41 | -1.65 | 261.41 | -3.45 | 261.41 | unavailable | 2024-12-06 | 2407000 | -73.29 |
| T_C32_KZ_4B_2024_10_31 | 998000 | 141.18 | -10.02 | 141.18 | -35.57 | 141.18 | -35.57 | 141.18 | unavailable | 2024-12-06 | 2407000 | -73.29 |
| T_C32_KAKAO_BIDDER_2023_03_07 | 61500 | 2.60 | -6.50 | 2.60 | -20.98 | 2.60 | -39.35 | 2.60 | 2.60 | 2023-03-07 | 63100 | -40.89 |

## 13. Current Calibrated Profile Stress Test

| question | result |
|---|---|
| Current profile on SM target event | Mostly correct; non-price public tender evidence exists. But Green was late relative to the offer-cap peak. |
| Current profile on Korea Zinc target event | Correct for Stage2/Actionable target premium; too early if 2024-10-31 is treated as full 4B rather than risk-watch overlay. |
| Current profile on Kakao bidder-side event | False positive risk if C32 headline is not role-split; bidder equity suffered drawdown while target equity captured the premium. |
| Stage2 bonus | Useful for target cases; excessive if applied to bidders/acquirers without cash-outflow penalty. |
| Yellow 75 | Fine for target cases; too loose for bidder-side tender headlines. |
| Green 87 / revision 55 | Not the central axis; Green can be too late near a fixed tender cap. |
| price-only blowoff guard | Kept and strengthened: target/control events require public offer evidence, not price alone. |
| full 4B non-price requirement | Kept, but Korea Zinc shows non-price 4B can still be full-window early. |
| hard 4C routing | No hard 4C in this loop. |

## 14. Stage2 / Yellow / Green Comparison

SM is the cleanest lateness example inside C32. The first target control-premium trigger at 114,700 captured most of the move. The later Kakao tender Green-style confirmation at 149,700 had a green_lateness_ratio of about 0.75:

```text
green_lateness_ratio = (149700 - 114700) / (161200 - 114700) = 0.75
```

This does not argue for weakening Green globally. It argues that C32 target cash-tender cases should preserve a Stage2-Actionable lane when the premium is already quantified by a public cash offer.

## 15. 4B Local vs Full-window Timing Audit

Korea Zinc shows why a single 4B peak proximity is dangerous.

```text
Stage2_Actionable_entry_price = 666000
Stage4B_overlay_entry_price = 998000
local_peak_after_stage2_before_overlay_context = 1543000
full_window_peak_after_stage2 = 2407000

four_b_local_peak_proximity = (998000 - 666000) / (1543000 - 666000) = 0.38
four_b_full_window_peak_proximity = (998000 - 666000) / (2407000 - 666000) = 0.19
four_b_timing_verdict = non_price_4B_local_risk_too_early_for_full_window_peak
```

Even though the 2024-10-31 evidence was non-price, it should be treated as 4B-watch or partial-risk overlay, not full exit calibration. The event engine needs a distinction between “non-price risk exists” and “the control-premium squeeze has exhausted.”

## 16. 4C Protection Audit

No hard 4C case is promoted in this MD. Korea Zinc after the share-issuance controversy remains a 4B-watch case rather than hard 4C because the prior thesis was not fully broken; the control contest continued and the full-window high occurred later.

```text
four_c_protection_label = thesis_break_watch_only
hard_4c_success = not_applicable
hard_4c_late = not_applicable
```

## 17. Sector-Specific Rule Candidate

```text
rule_scope = canonical_archetype_specific
rule_id = C32_TARGET_VS_BIDDER_ROLE_SPLIT
proposal_type = shadow_only

if canonical_archetype_id == C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP:
    require issuer_role in [target, bidder, holder_spillover, controlling_shareholder_vehicle]
    if issuer_role == target and public cash tender / competing tender / quantified control premium exists:
        allow Stage2-Actionable promotion with target_cash_offer_spread_buffer
    if issuer_role == bidder:
        cap positive Stage2 contribution unless acquisition economics are explicitly accretive
        add bidder_cash_outflow_or_integration_risk penalty
    if issuer_role == holder_spillover:
        treat as narrative or watch unless value capture is directly monetizable and cleanly evidenced
```

## 18. Canonical-Archetype Rule Candidate

```text
canonical_rule_candidate = true
canonical_axis = C32_control_premium_role_split
tested_value = enabled
baseline_value = not_explicit
```

The same headline can mean three different things:

1. The target is being bought, so the premium is a direct cash-or-control bridge.
2. The bidder is paying, so the premium may be a cash-outflow/integration/regulatory risk.
3. The holder/spillover vehicle may benefit mark-to-market, but calibration must be blocked if the price window is corporate-action contaminated or if monetization is not direct.

## 19. Before / After Backtest Comparison

| profile_id | profile_scope | eligible triggers | selected entries | avg_MFE_90D | avg_MAE_90D | avg_MFE_180D | avg_MAE_180D | false_positive_rate | verdict |
|---|---|---:|---|---:|---:|---:|---:|---:|---|
| P0 e2r_2_1_stock_web_calibrated_proxy | current proxy | 3 | SM target; KZ target; Kakao bidder | 101.52 | -15.42 | 101.52 | -22.14 | 33.3% | good target capture but bidder false-positive risk |
| P0b e2r_2_0_baseline_reference | rollback reference | 3 | same | 101.52 | -15.42 | 101.52 | -22.14 | 33.3% | less explicit non-price filtering |
| P1 sector_specific_candidate_profile | L10 shadow | 2 | target-only C32 entries | 150.98 | -12.64 | 150.98 | -13.54 | 0.0% | improved alignment by role-splitting |
| P2 canonical_archetype_candidate_profile | C32 shadow | 2 | target cash/control premium only | 150.98 | -12.64 | 150.98 | -13.54 | 0.0% | canonical rule candidate |
| P3 counterexample_guard_profile | C32 guard | 3 evaluated / 2 selected | excludes bidder-side false positive | 150.98 | -12.64 | 150.98 | -13.54 | 0.0% | best guardrail |

## 20. Score-Return Alignment Matrix

| case_id | current score label | proposed score label | actual path | alignment |
|---|---|---|---|---|
| C32_SM_2023_TARGET_TENDER_WAR | Stage3-Yellow/Green late | Stage2-Actionable target premium | +40.54% MFE before sharp post-cap drawdown | aligned after target-premium lane |
| C32_KOREAZINC_2024_TARGET_HOSTILE_TENDER | Stage3-Yellow/Green; 4B risk | Stage2 target premium + 4B-watch not full 4B | +261.41% MFE; later -73.29% from peak | aligned with 4B timing split |
| C32_KAKAO_2023_BIDDER_TENDER_COUNTEREXAMPLE | possible Stage2 false positive | Watch/No-promote | +2.60% MFE, -39.35% 180D MAE | false positive avoided |
| C32_YOUNGPOONG_2024_BIDDER_SPILLOVER_NARRATIVE | data insufficient | narrative-only | blocked by 2025-04-25 CA candidate | not used for weights |

## 21. Coverage Matrix

| large_sector_id | canonical_archetype_id | fine_archetype_id | positive_case_count | counterexample_count | 4B_case_count | 4C_case_count | new_independent_case_count | reused_case_count | calibration_usable_trigger_count | representative_trigger_count | current_profile_error_count | sector_rule_candidate | canonical_rule_candidate | coverage_gap_after_this_loop |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|---|---|
| L10_POLICY_EVENT_CROSS_REDTEAM_MISC | C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP | TARGET_VS_BIDDER_TENDER_CONTROL_PREMIUM_SPLIT | 2 | 1 usable + 1 narrative-only | 1 | 0 | 3 | 0 | 5 | 3 | 2 | true | true | bidder/holder spillover still needs more clean cases |

## 22. Residual Contribution Summary

```text
new_independent_case_count: 3
reused_case_count: 0
reused_case_ids: []
new_symbol_count: 4
new_canonical_archetype_count: 0
new_fine_archetype_count: 1
new_trigger_family_count: 3
tested_existing_calibrated_axes:
  - price_only_blowoff_blocks_positive_stage
  - full_4b_requires_non_price_evidence
residual_error_types_found:
  - bidder_side_tender_false_positive
  - non_price_4B_local_risk_too_early_for_full_window_peak
new_axis_proposed:
  - C32_target_vs_bidder_role_split
  - C32_target_cash_offer_spread_buffer
  - C32_bidder_cash_outflow_or_integration_risk_penalty
existing_axis_strengthened:
  - price_only_blowoff_blocks_positive_stage
  - full_4b_requires_non_price_evidence
existing_axis_weakened: null
existing_axis_kept:
  - stage2_actionable_evidence_bonus
  - stage3_yellow_total_min
  - stage3_green_total_min
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
- stock-web manifest max_date and price basis
- symbol profile first/last date and corporate action windows
- tradable shard entry prices and high/low windows for representative cases
- 30D/90D/180D MFE/MAE for calibration-usable triggers
- same_entry_group_id and representative trigger dedupe
- target vs bidder split as C32-specific shadow rule candidate
```

Not validated / not done:

```text
- no current/live scan
- no stock_agent src/e2r code access
- no production scoring change
- no brokerage/API/autotrading
- no attempt to use manifest max_date beyond 2026-02-20
- no global rule promotion
```

## 24. Shadow Weight Calibration

```csv
row_type,axis,scope,large_sector_id,canonical_archetype_id,baseline_value,tested_value,delta,reason,backtest_effect,trigger_ids,calibration_usable_count,new_independent_case_count,counterexample_count,confidence,proposal_type,notes
shadow_weight,C32_target_vs_bidder_role_split,canonical_archetype_specific,L10_POLICY_EVENT_CROSS_REDTEAM_MISC,C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP,0,1,+1,"target receives premium but bidder pays premium","removed Kakao false positive while keeping SM/Korea Zinc target successes","T_C32_SM_STAGE2_2023_02_10|T_C32_KZ_STAGE2_2024_09_13|T_C32_KAKAO_BIDDER_2023_03_07",3,3,1,medium,canonical_shadow_only,"not production; post-calibrated residual"
shadow_weight,C32_target_cash_offer_spread_buffer,canonical_archetype_specific,L10_POLICY_EVENT_CROSS_REDTEAM_MISC,C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP,0,1,+1,"quantified cash tender provides direct premium bridge","preserves early target entries before Green confirmation","T_C32_SM_STAGE2_2023_02_10|T_C32_KZ_STAGE2_2024_09_13",2,2,0,medium,canonical_shadow_only,"only when issuer_role=target"
shadow_weight,C32_bidder_cash_outflow_or_integration_risk_penalty,canonical_archetype_specific,L10_POLICY_EVENT_CROSS_REDTEAM_MISC,C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP,0,1,+1,"bidder-side event should be capped unless accretive economics are evidenced","blocks Kakao-style bidder false positive","T_C32_KAKAO_BIDDER_2023_03_07",1,1,1,medium,counterexample_guard,"not a short signal; no-promote guard"
shadow_weight,C32_full_4B_requires_peak_exhaustion_or_thesis_break,canonical_archetype_specific,L10_POLICY_EVENT_CROSS_REDTEAM_MISC,C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP,0,1,+1,"non-price 4B can still be too early in an active control squeeze","Korea Zinc 2024-10-31 remained before full-window peak","T_C32_KZ_4B_2024_10_31",1,0,0,low,4B_overlay_shadow_only,"treat as 4B-watch unless squeeze exhaustion is evidenced"
```

## 25. Machine-Readable Rows

```jsonl
{"row_type":"price_source_validation","source":"Songdaiki/stock-web","source_url":"https://github.com/Songdaiki/stock-web","manifest_path":"atlas/manifest.json","schema_path":"atlas/schema.json","universe_path":"atlas/universe/all_symbols.csv","manifest_max_date":"2026-02-20","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","calibration_shard_root":"atlas/ohlcv_tradable_by_symbol_year","raw_shard_root":"atlas/ohlcv_raw_by_symbol_year","validation_status":"usable_for_historical_calibration"}
{"row_type":"case","round":"R12","loop":"74","large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP","fine_archetype_id":"TARGET_VS_BIDDER_TENDER_CONTROL_PREMIUM_SPLIT","price_source":"Songdaiki/stock-web","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"case_id":"C32_SM_2023_TARGET_TENDER_WAR","symbol":"041510","company_name":"에스엠","case_type":"structural_success","positive_or_counterexample":"positive","best_trigger":"T_C32_SM_STAGE2_2023_02_10","calibration_usable":true,"current_profile_verdict":"current_profile_correct","notes":"Target-company control premium: HYBE stake purchase/tender followed by Kakao competing tender. Clean 180D window."}
{"row_type":"case","round":"R12","loop":"74","large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP","fine_archetype_id":"TARGET_VS_BIDDER_TENDER_CONTROL_PREMIUM_SPLIT","price_source":"Songdaiki/stock-web","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"case_id":"C32_KOREAZINC_2024_TARGET_HOSTILE_TENDER","symbol":"010130","company_name":"고려아연","case_type":"structural_success_high_mae_with_4B_overlay","positive_or_counterexample":"positive","best_trigger":"T_C32_KZ_STAGE2_2024_09_13","calibration_usable":true,"current_profile_verdict":"current_profile_4B_too_early","notes":"Target-company hostile tender battle; 4B overlay on share-issuance/FSS issue was locally useful but too early for full-window peak."}
{"row_type":"case","round":"R12","loop":"74","large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP","fine_archetype_id":"TARGET_VS_BIDDER_TENDER_CONTROL_PREMIUM_SPLIT","price_source":"Songdaiki/stock-web","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"case_id":"C32_KAKAO_2023_BIDDER_TENDER_COUNTEREXAMPLE","symbol":"035720","company_name":"카카오","case_type":"failed_rerating","positive_or_counterexample":"counterexample","best_trigger":"T_C32_KAKAO_BIDDER_2023_03_07","calibration_usable":true,"current_profile_verdict":"current_profile_false_positive","notes":"Bidder/acquirer cash-outflow side of the same SM control event; tender headline did not transmit as positive C32 evidence to bidder equity."}
{"row_type":"case","round":"R12","loop":"74","large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP","fine_archetype_id":"TARGET_VS_BIDDER_TENDER_CONTROL_PREMIUM_SPLIT","price_source":"Songdaiki/stock-web","is_new_independent_case":false,"reuse_reason":null,"independent_evidence_weight":0.0,"case_id":"C32_YOUNGPOONG_2024_BIDDER_SPILLOVER_NARRATIVE","symbol":"000670","company_name":"영풍","case_type":"narrative_only","positive_or_counterexample":"counterexample","best_trigger":"T_C32_YP_BIDDER_2024_09_13","calibration_usable":false,"current_profile_verdict":"current_profile_data_insufficient","notes":"Bidder/holder side reacted sharply, but symbol profile has 2025-04-25 corporate-action candidate inside the 180D window; not used for weights."}
{"round":"R12","loop":"74","large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP","fine_archetype_id":"TARGET_VS_BIDDER_TENDER_CONTROL_PREMIUM_SPLIT","sector":"policy_event_cross_redteam_misc","primary_archetype":"governance_control_premium_tender_cap","loop_objective":"sector_specific_rule_discovery|canonical_archetype_compression|counterexample_mining|coverage_gap_fill|4B_non_price_requirement_stress_test","price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","row_type":"trigger","trigger_id":"T_C32_SM_STAGE2_2023_02_10","case_id":"C32_SM_2023_TARGET_TENDER_WAR","symbol":"041510","company_name":"에스엠","trigger_type":"Stage2-Actionable","trigger_date":"2023-02-10","entry_date":"2023-02-10","entry_price":114700,"evidence_available_at_that_date":"HYBE became largest shareholder and launched a tender route to raise ownership; target-company cash/control premium became explicit.","evidence_source":"AP / public tender-offer reports; stock-web 041510 2023 row shows entry close 114700 and subsequent Mar 8 high 161200.","stage2_evidence_fields":["public_event_or_disclosure","customer_or_order_quality","policy_or_regulatory_optionality","relative_strength"],"stage3_evidence_fields":["multiple_public_sources","durable_customer_confirmation"],"stage4b_evidence_fields":[],"stage4c_evidence_fields":[],"price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/041/041510/2023.csv","profile_path":"atlas/symbol_profiles/041/041510.json","MFE_30D_pct":40.54,"MFE_90D_pct":40.54,"MFE_180D_pct":40.54,"MFE_1Y_pct":40.54,"MFE_2Y_pct":40.54,"MAE_30D_pct":-9.24,"MAE_90D_pct":-23.63,"MAE_180D_pct":-23.63,"MAE_1Y_pct":-37.49,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2023-03-08","peak_price":161200,"drawdown_after_peak_pct":-45.66,"green_lateness_ratio":0.75,"four_b_local_peak_proximity":null,"four_b_full_window_peak_proximity":null,"four_b_timing_verdict":null,"four_b_evidence_type":[],"four_c_protection_label":"not_applicable","trigger_outcome_label":"target_control_premium_success_but_green_late","current_profile_verdict":"current_profile_correct","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"G_SM_2023_02_10","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"round":"R12","loop":"74","large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP","fine_archetype_id":"TARGET_VS_BIDDER_TENDER_CONTROL_PREMIUM_SPLIT","sector":"policy_event_cross_redteam_misc","primary_archetype":"governance_control_premium_tender_cap","loop_objective":"sector_specific_rule_discovery|canonical_archetype_compression|counterexample_mining|coverage_gap_fill|4B_non_price_requirement_stress_test","price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","row_type":"trigger","trigger_id":"T_C32_SM_GREEN_2023_03_07","case_id":"C32_SM_2023_TARGET_TENDER_WAR","symbol":"041510","company_name":"에스엠","trigger_type":"Stage3-Green-label-comparison","trigger_date":"2023-03-07","entry_date":"2023-03-07","entry_price":149700,"evidence_available_at_that_date":"Kakao competing tender at 150,000 KRW per share made the final control-premium cap more explicit.","evidence_source":"AP 2023-03-07 Kakao tender report; stock-web row 2023-03-07 close 149700.","stage2_evidence_fields":["public_event_or_disclosure","relative_strength"],"stage3_evidence_fields":["multiple_public_sources","financial_visibility"],"stage4b_evidence_fields":["explicit_event_cap"],"stage4c_evidence_fields":[],"price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/041/041510/2023.csv","profile_path":"atlas/symbol_profiles/041/041510.json","MFE_30D_pct":7.68,"MFE_90D_pct":7.68,"MFE_180D_pct":7.68,"MFE_1Y_pct":7.68,"MFE_2Y_pct":7.68,"MAE_30D_pct":-41.48,"MAE_90D_pct":-41.48,"MAE_180D_pct":-41.48,"MAE_1Y_pct":-52.1,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2023-03-08","peak_price":161200,"drawdown_after_peak_pct":-45.66,"green_lateness_ratio":0.75,"four_b_local_peak_proximity":0.75,"four_b_full_window_peak_proximity":0.75,"four_b_timing_verdict":"event_cap_near_full_window_peak","four_b_evidence_type":["control_premium_or_event_premium","valuation_blowoff"],"four_c_protection_label":"not_applicable","trigger_outcome_label":"green_late_near_offer_cap","current_profile_verdict":"current_profile_too_late","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"G_SM_2023_03_07","dedupe_for_aggregate":false,"aggregate_group_role":"label_comparison_only","is_new_independent_case":false,"reuse_reason":"same case label comparison only","independent_evidence_weight":0.0,"do_not_count_as_new_case":true}
{"round":"R12","loop":"74","large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP","fine_archetype_id":"TARGET_VS_BIDDER_TENDER_CONTROL_PREMIUM_SPLIT","sector":"policy_event_cross_redteam_misc","primary_archetype":"governance_control_premium_tender_cap","loop_objective":"sector_specific_rule_discovery|canonical_archetype_compression|counterexample_mining|coverage_gap_fill|4B_non_price_requirement_stress_test","price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","row_type":"trigger","trigger_id":"T_C32_KZ_STAGE2_2024_09_13","case_id":"C32_KOREAZINC_2024_TARGET_HOSTILE_TENDER","symbol":"010130","company_name":"고려아연","trigger_type":"Stage2-Actionable","trigger_date":"2024-09-13","entry_date":"2024-09-13","entry_price":666000,"evidence_available_at_that_date":"MBK/Young Poong tender offer at 660,000 KRW with control-rights objective; Korea Zinc opposed it as hostile.","evidence_source":"Reuters 2024-09-13; stock-web 010130 2024 row shows 2024-09-13 close 666000 and later Dec 6 high 2407000.","stage2_evidence_fields":["public_event_or_disclosure","policy_or_regulatory_optionality","relative_strength"],"stage3_evidence_fields":["multiple_public_sources","financial_visibility","durable_customer_confirmation"],"stage4b_evidence_fields":[],"stage4c_evidence_fields":[],"price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/010/010130/2024.csv","profile_path":"atlas/symbol_profiles/010/010130.json","MFE_30D_pct":131.68,"MFE_90D_pct":261.41,"MFE_180D_pct":261.41,"MFE_1Y_pct":261.41,"MFE_2Y_pct":null,"MAE_30D_pct":-1.65,"MAE_90D_pct":-1.65,"MAE_180D_pct":-3.45,"MAE_1Y_pct":-3.45,"below_entry_price_flag_30D":false,"below_entry_price_flag_90D":false,"peak_date":"2024-12-06","peak_price":2407000,"drawdown_after_peak_pct":-73.29,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":null,"four_b_full_window_peak_proximity":null,"four_b_timing_verdict":null,"four_b_evidence_type":[],"four_c_protection_label":"not_applicable","trigger_outcome_label":"target_hostile_tender_structural_success","current_profile_verdict":"current_profile_correct","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"G_KZ_2024_09_13","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"round":"R12","loop":"74","large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP","fine_archetype_id":"TARGET_VS_BIDDER_TENDER_CONTROL_PREMIUM_SPLIT","sector":"policy_event_cross_redteam_misc","primary_archetype":"governance_control_premium_tender_cap","loop_objective":"sector_specific_rule_discovery|canonical_archetype_compression|counterexample_mining|coverage_gap_fill|4B_non_price_requirement_stress_test","price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","row_type":"trigger","trigger_id":"T_C32_KZ_4B_2024_10_31","case_id":"C32_KOREAZINC_2024_TARGET_HOSTILE_TENDER","symbol":"010130","company_name":"고려아연","trigger_type":"Stage4B-overlay","trigger_date":"2024-10-31","entry_date":"2024-10-31","entry_price":998000,"evidence_available_at_that_date":"FSS investigation into share-issuance plan after tender/buyback sequence; non-price risk existed but it did not mark the full-window top.","evidence_source":"Reuters 2024-10-31; stock-web shows 2024-10-31 close 998000, later 2024-12-06 high 2407000.","stage2_evidence_fields":[],"stage3_evidence_fields":[],"stage4b_evidence_fields":["legal_or_regulatory_block","capital_raise_or_overhang","positioning_overheat"],"stage4c_evidence_fields":[],"price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/010/010130/2024.csv","profile_path":"atlas/symbol_profiles/010/010130.json","MFE_30D_pct":141.18,"MFE_90D_pct":141.18,"MFE_180D_pct":141.18,"MFE_1Y_pct":141.18,"MFE_2Y_pct":null,"MAE_30D_pct":-10.02,"MAE_90D_pct":-35.57,"MAE_180D_pct":-35.57,"MAE_1Y_pct":-35.57,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-12-06","peak_price":2407000,"drawdown_after_peak_pct":-73.29,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":0.38,"four_b_full_window_peak_proximity":0.19,"four_b_timing_verdict":"non_price_4B_local_risk_too_early_for_full_window_peak","four_b_evidence_type":["legal_or_regulatory_block","capital_raise_or_overhang","positioning_overheat"],"four_c_protection_label":"thesis_break_watch_only","trigger_outcome_label":"4B_too_early_for_full_window","current_profile_verdict":"current_profile_4B_too_early","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"G_KZ_2024_10_31","dedupe_for_aggregate":false,"aggregate_group_role":"4B_overlay_only","is_new_independent_case":false,"reuse_reason":"same case 4B timing overlay","independent_evidence_weight":0.0,"do_not_count_as_new_case":true}
{"round":"R12","loop":"74","large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP","fine_archetype_id":"TARGET_VS_BIDDER_TENDER_CONTROL_PREMIUM_SPLIT","sector":"policy_event_cross_redteam_misc","primary_archetype":"governance_control_premium_tender_cap","loop_objective":"sector_specific_rule_discovery|canonical_archetype_compression|counterexample_mining|coverage_gap_fill|4B_non_price_requirement_stress_test","price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","row_type":"trigger","trigger_id":"T_C32_KAKAO_BIDDER_2023_03_07","case_id":"C32_KAKAO_2023_BIDDER_TENDER_COUNTEREXAMPLE","symbol":"035720","company_name":"카카오","trigger_type":"Stage2-Actionable-counterexample","trigger_date":"2023-03-07","entry_date":"2023-03-07","entry_price":61500,"evidence_available_at_that_date":"Kakao launched a 150,000 KRW tender for up to 35% of SM; event was positive for target control premium but cash-outflow/acquirer-risk for bidder equity.","evidence_source":"AP 2023-03-07; stock-web 035720 2023 row shows 2023-03-07 close 61500 and subsequent 180D drawdown.","stage2_evidence_fields":["public_event_or_disclosure"],"stage3_evidence_fields":[],"stage4b_evidence_fields":["valuation_blowoff","capital_raise_or_overhang"],"stage4c_evidence_fields":[],"price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/035/035720/2023.csv","profile_path":"atlas/symbol_profiles/035/035720.json","MFE_30D_pct":2.6,"MFE_90D_pct":2.6,"MFE_180D_pct":2.6,"MFE_1Y_pct":2.6,"MFE_2Y_pct":2.6,"MAE_30D_pct":-6.5,"MAE_90D_pct":-20.98,"MAE_180D_pct":-39.35,"MAE_1Y_pct":-39.35,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2023-03-07","peak_price":63100,"drawdown_after_peak_pct":-40.89,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":1.0,"four_b_full_window_peak_proximity":1.0,"four_b_timing_verdict":"bidder_side_event_cap_false_positive","four_b_evidence_type":["capital_raise_or_overhang","valuation_blowoff"],"four_c_protection_label":"false_break","trigger_outcome_label":"bidder_side_failed_rerating","current_profile_verdict":"current_profile_false_positive","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"G_KAKAO_2023_03_07","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"narrative_only","case_id":"C32_YOUNGPOONG_2024_BIDDER_SPILLOVER_NARRATIVE","symbol":"000670","company_name":"영풍","large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP","reason":"bidder_side_spillover_case_blocked_by_corporate_action_candidate_inside_180D_window_2025_04_25","price_source":"Songdaiki/stock-web","usage":"not_weight_calibration"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"C32_SM_2023_TARGET_TENDER_WAR","trigger_id":"T_C32_SM_STAGE2_2023_02_10","symbol":"041510","large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP","raw_component_scores_before":{"contract_score":18,"backlog_visibility_score":0,"margin_bridge_score":0,"revision_score":0,"relative_strength_score":15,"customer_quality_score":0,"policy_or_regulatory_score":8,"valuation_repricing_score":18,"execution_risk_score":4,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_before":82,"stage_label_before":"Stage3-Yellow","raw_component_scores_after":{"contract_score":20,"backlog_visibility_score":0,"margin_bridge_score":0,"revision_score":0,"relative_strength_score":17,"customer_quality_score":0,"policy_or_regulatory_score":10,"valuation_repricing_score":20,"execution_risk_score":4,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_after":88,"stage_label_after":"Stage3-Green","changed_components":["target_vs_bidder_role_split","cash_offer_spread_buffer","bidder_cash_outflow_penalty"],"component_delta_explanation":"target cash tender/competing bid receives canonical C32 bonus","MFE_90D_pct":40.54,"MAE_90D_pct":-23.63,"score_return_alignment_label":"aligned","current_profile_verdict":"current_profile_correct"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"C32_KOREAZINC_2024_TARGET_HOSTILE_TENDER","trigger_id":"T_C32_KZ_STAGE2_2024_09_13","symbol":"010130","large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP","raw_component_scores_before":{"contract_score":20,"backlog_visibility_score":0,"margin_bridge_score":0,"revision_score":0,"relative_strength_score":18,"customer_quality_score":0,"policy_or_regulatory_score":12,"valuation_repricing_score":20,"execution_risk_score":0,"legal_or_contract_risk_score":6,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_before":84,"stage_label_before":"Stage3-Yellow","raw_component_scores_after":{"contract_score":22,"backlog_visibility_score":0,"margin_bridge_score":0,"revision_score":0,"relative_strength_score":20,"customer_quality_score":0,"policy_or_regulatory_score":13,"valuation_repricing_score":22,"execution_risk_score":0,"legal_or_contract_risk_score":6,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_after":90,"stage_label_after":"Stage3-Green","changed_components":["target_vs_bidder_role_split","cash_offer_spread_buffer","bidder_cash_outflow_penalty"],"component_delta_explanation":"hostile tender target receives target-side control premium conversion bonus","MFE_90D_pct":261.41,"MAE_90D_pct":-1.65,"score_return_alignment_label":"aligned","current_profile_verdict":"current_profile_correct"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"C32_KAKAO_2023_BIDDER_TENDER_COUNTEREXAMPLE","trigger_id":"T_C32_KAKAO_BIDDER_2023_03_07","symbol":"035720","large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP","raw_component_scores_before":{"contract_score":10,"backlog_visibility_score":0,"margin_bridge_score":0,"revision_score":0,"relative_strength_score":0,"customer_quality_score":0,"policy_or_regulatory_score":4,"valuation_repricing_score":8,"execution_risk_score":12,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_before":76,"stage_label_before":"Stage3-Yellow","raw_component_scores_after":{"contract_score":4,"backlog_visibility_score":0,"margin_bridge_score":0,"revision_score":0,"relative_strength_score":0,"customer_quality_score":0,"policy_or_regulatory_score":2,"valuation_repricing_score":4,"execution_risk_score":22,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_after":62,"stage_label_after":"Watch/No-promote","changed_components":["target_vs_bidder_role_split","cash_offer_spread_buffer","bidder_cash_outflow_penalty"],"component_delta_explanation":"bidder-side cash outflow and integration/regulatory risk cap prevents false positive","MFE_90D_pct":2.6,"MAE_90D_pct":-20.98,"score_return_alignment_label":"false_positive_avoided_after_guard","current_profile_verdict":"current_profile_false_positive"}
{"row_type":"score_simulation","profile_id":"counterexample_guard_profile","case_id":"C32_KOREAZINC_2024_TARGET_HOSTILE_TENDER","trigger_id":"T_C32_KZ_4B_2024_10_31","symbol":"010130","large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP","raw_component_scores_before":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":0,"revision_score":0,"relative_strength_score":0,"customer_quality_score":0,"policy_or_regulatory_score":0,"valuation_repricing_score":20,"execution_risk_score":12,"legal_or_contract_risk_score":18,"dilution_cb_risk_score":16,"accounting_trust_risk_score":0},"weighted_score_before":0,"stage_label_before":"4B-overlay","raw_component_scores_after":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":0,"revision_score":0,"relative_strength_score":0,"customer_quality_score":0,"policy_or_regulatory_score":0,"valuation_repricing_score":20,"execution_risk_score":12,"legal_or_contract_risk_score":18,"dilution_cb_risk_score":16,"accounting_trust_risk_score":0},"weighted_score_after":0,"stage_label_after":"4B-watch-only","changed_components":["target_vs_bidder_role_split","cash_offer_spread_buffer","bidder_cash_outflow_penalty"],"component_delta_explanation":"full 4B must distinguish local legal/issuance risk from full-window control-premium squeeze","MFE_90D_pct":141.18,"MAE_90D_pct":-35.57,"score_return_alignment_label":"aligned","current_profile_verdict":"current_profile_4B_too_early"}
{"row_type":"residual_contribution","round":"R12","loop":"74","large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP","new_independent_case_count":3,"reused_case_count":0,"new_symbol_count":4,"new_trigger_family_count":3,"tested_existing_calibrated_axes":["price_only_blowoff_blocks_positive_stage","full_4b_requires_non_price_evidence"],"residual_error_types_found":["bidder_side_tender_false_positive","local_non_price_4B_too_early_for_full_window"],"loop_contribution_label":"canonical_archetype_rule_candidate","do_not_propose_new_weight_delta":false}
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
completed_round = R12
completed_loop = 74
next_round = R13
next_loop = 74
round_schedule_status = valid
round_sector_consistency = pass
```

## 28. Source Notes

Stock-web:
- manifest: atlas/manifest.json
- profiles: atlas/symbol_profiles/041/041510.json; atlas/symbol_profiles/010/010130.json; atlas/symbol_profiles/035/035720.json; atlas/symbol_profiles/000/000670.json
- shards: atlas/ohlcv_tradable_by_symbol_year/041/041510/2023.csv; atlas/ohlcv_tradable_by_symbol_year/041/041510/2024.csv; atlas/ohlcv_tradable_by_symbol_year/010/010130/2024.csv; atlas/ohlcv_tradable_by_symbol_year/010/010130/2025.csv; atlas/ohlcv_tradable_by_symbol_year/035/035720/2023.csv

External evidence:
- Reuters, 2024-09-13: MBK/Young Poong Korea Zinc tender offer at 660,000 KRW and target/bidder share reaction.
- Reuters, 2024-10-31: FSS investigation into Korea Zinc share-issuance plan after tender/buyback sequence.
- Reuters, 2024-12-03: Korea Zinc special shareholder meeting / control contest continuation.
- AP, 2023-03-07: Kakao tender offer for up to 35% of SM at 150,000 KRW after HYBE bid route.
- AP, 2023-02-22: HYBE became SM's largest single shareholder and aimed to increase stake through tender mechanics.

