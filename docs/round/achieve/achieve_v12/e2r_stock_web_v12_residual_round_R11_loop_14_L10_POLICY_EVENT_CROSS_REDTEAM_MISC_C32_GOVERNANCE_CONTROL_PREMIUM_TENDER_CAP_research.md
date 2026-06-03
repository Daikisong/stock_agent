# E2R Stock-Web Historical Calibration / Sector-Archetype Residual Research Round
## 0. Research Metadata
```text
research_session = post_calibrated_sector_archetype_residual_research
mode = historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12
output_file = e2r_stock_web_v12_residual_round_R11_loop_14_L10_POLICY_EVENT_CROSS_REDTEAM_MISC_C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP_research.md
scheduled_round = R11
scheduled_loop = 14
round_schedule_status = valid
round_sector_consistency = pass
large_sector_id = L10_POLICY_EVENT_CROSS_REDTEAM_MISC
canonical_archetype_id = C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP
fine_archetype_id = CONTROL_PREMIUM_TENDER_CAP_VS_UNCLOSED_GOVERNANCE_STORY
loop_objective = coverage_gap_fill | counterexample_mining | residual_false_positive_mining | 4B_non_price_requirement_stress_test | 4C_thesis_break_timing_test | canonical_archetype_compression
production_scoring_changed = false
shadow_weight_only = true
stock_agent_code_access_allowed = false
stock_agent_code_patch_allowed = false
stock_web_price_atlas_access_required = true
handoff_prompt_embedded = true
handoff_prompt_executed_now = false
```
This loop adds 4 new independent cases, 2 counterexamples, and 4 residual errors for R11/L10_POLICY_EVENT_CROSS_REDTEAM_MISC/C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP.

## 1. Current Calibrated Profile Assumption

```text
current_default_profile_proxy = e2r_2_1_stock_web_calibrated_proxy
rollback_reference_profile_id = e2r_2_0_baseline_reference
stage2_actionable_evidence_bonus = +2.0
stage3_yellow_total_min = 75.0
stage3_green_total_min = 87.0
stage3_green_revision_min = 55.0
stage3_cross_evidence_green_buffer = +1.5
price_only_blowoff_blocks_positive_stage = true
full_4b_requires_non_price_evidence = true
hard_4c_thesis_break_routes_to_4c = true
```

This file does not re-prove the global calibration. It tests a narrow R11/C32 residual: the market often treats governance conflict, tender offers, sale processes, and family-control disputes as the same animal. They are not. A binding or competing tender offer is a price bridge; an unclosed sale process or boardroom dispute is closer to a bridge drawn on fogged glass.

## 2. Round / Large Sector / Canonical Archetype Scope

| field | value |
|---|---|
| scheduled_round | R11 |
| scheduled_loop | 14 |
| large_sector_id | L10_POLICY_EVENT_CROSS_REDTEAM_MISC |
| canonical_archetype_id | C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP |
| fine_archetype_id | CONTROL_PREMIUM_TENDER_CAP_VS_UNCLOSED_GOVERNANCE_STORY |
| invalid_round_sector_pair | false |
| rule_scope_target | canonical_archetype_specific first, sector_specific second |

R11 permits L10 policy/event/cross-redteam work. The file therefore stays in L10 and does not masquerade as R5/R6/R7/R8 sector work.

## 3. Previous Coverage / Duplicate Avoidance Check

Accessible local v12 artifacts show loops 10-13 complete through R13 and loop 14 complete through R10. The first missing round in loop 14 is therefore R11. Prior R11 loop 11-13 files mainly covered C31 policy/subsidy/legislation events; C32 had materially less loop-14 coverage. This run chooses new C32 symbols and does not reuse R11 C31 value-up/resource-policy cases.

| avoided repetition | current selection response |
|---|---|
| Reusing C31 Value-up and resource-policy themes | Not reused |
| Reusing R10 construction/PF policy-price spikes | Not reused |
| Treating all control-premium headlines as positive Stage3 | Blocked unless binding/competing tender or high deal-close probability exists |
| Treating price-only governance spike as 4B without evidence | Split into price-only overlay vs non-price tender/shareholder-vote evidence |

## 4. Stock-Web OHLC Input / Price Source Validation

| field | value |
|---|---|
| source | Songdaiki/stock-web |
| upstream_source | FinanceData/marcap |
| manifest_path | atlas/manifest.json |
| source_name | FinanceData/marcap |
| source_repo_url | https://github.com/FinanceData/marcap |
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
| price_basis | tradable_raw |
| price_adjustment_status | raw_unadjusted_marcap |

Stock-Web schema validation uses raw/unadjusted OHLC. Corporate-action-contaminated 180D windows are blocked. All representative rows in this file have a clean 180D window under the available profile data.

## 5. Historical Eligibility Gate

| case_id | symbol | entry_date | 180D window status | corporate-action status | calibration_usable |
|---|---:|---:|---|---|---|
| R11L14_C32_KOREAZINC_MBK_YOUNGPOONG_20240913 | 010130 | 2024-09-13 | available through at least D+180 before manifest max_date 2026-02-20 | clean_180D_window | true |
| R11L14_C32_SM_HYBE_KAKAO_20230210 | 041510 | 2023-02-10 | available through at least D+180 before manifest max_date 2026-02-20 | clean_180D_window; profile candidates only 2002/2005 | true |
| R11L14_C32_HMM_HARIM_PRIVATIZATION_20231219 | 011200 | 2023-12-19 | available through at least D+180 before manifest max_date 2026-02-20 | clean_180D_window; 2023-11-10 candidate precedes entry window | true |
| R11L14_C32_HANMI_SCIENCE_OCI_INTEGRATION_20240115 | 008930 | 2024-01-15 | available through at least D+180 before manifest max_date 2026-02-20 | clean_180D_window; profile candidates only 1999/2010/2012 | true |

## 6. Canonical Archetype Compression Map

| fine_archetype_id | canonical_archetype_id | compression logic |
|---|---|---|
| HOSTILE_TENDER_CONTROL_PREMIUM_SQUEEZE | C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP | Binding hostile tender and counter-tender mechanics create a real price bridge but can overshoot into 4B blowoff |
| KPOP_CONTROL_PREMIUM_TENDER_BATTLE | C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP | Competing tender prices created a clear cap/rerating path, then post-contest reversion |
| PRIVATIZATION_PREFERRED_BIDDER_UNCLOSED_DEAL | C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP | Preferred bidder alone is not a closed transaction; deal uncertainty should suppress Green |
| FAMILY_CONTROL_MERGER_VOTE_RISK | C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP | Control-family dispute and shareholder vote risk can create spikes but not durable rerating |

## 7. Case Selection Summary

| case_id | symbol | company_name | role | trigger_date | entry_date | entry_price | reason selected |
|---|---:|---|---|---:|---:|---:|---|
| R11L14_C32_KOREAZINC_MBK_YOUNGPOONG_20240913 | 010130 | Korea Zinc / 고려아연 | structural_success / 4B_overlay_success | 2024-09-13 | 2024-09-13 | 666000 | HOSTILE_TENDER_CONTROL_PREMIUM_SQUEEZE |
| R11L14_C32_SM_HYBE_KAKAO_20230210 | 041510 | SM Entertainment / 에스엠 | structural_success / 4B_event_cap | 2023-02-10 | 2023-02-10 | 114700 | KPOP_CONTROL_PREMIUM_TENDER_BATTLE |
| R11L14_C32_HMM_HARIM_PRIVATIZATION_20231219 | 011200 | HMM | failed_rerating / false_positive_green | 2023-12-18 | 2023-12-19 | 18430 | PRIVATIZATION_PREFERRED_BIDDER_UNCLOSED_DEAL |
| R11L14_C32_HANMI_SCIENCE_OCI_INTEGRATION_20240115 | 008930 | Hanmi Science / 한미사이언스 | failed_rerating / 4C_success | 2024-01-12 | 2024-01-15 | 43300 | FAMILY_CONTROL_MERGER_VOTE_RISK |

## 8. Positive vs Counterexample Balance

| bucket | count | cases |
|---|---:|---|
| positive_structural_success | 2 | Korea Zinc, SM Entertainment |
| counterexample_or_failed_rerating | 2 | HMM, Hanmi Science |
| 4B_or_4C_case | 3 | Korea Zinc share-issue/overheat, SM Kakao tender cap, Hanmi shareholder-vote 4C |
| calibration_usable_case_count | 4 | all representative cases |

The balancing principle is simple: if someone is actually standing at the door with a funded tender price, the market can re-mark the house. If the rumor is only that a buyer might someday knock, the price often runs ahead of the key.

## 9. Evidence Source Map

| case_id | evidence_available_at_that_date | evidence_source | stage2_evidence_fields | stage3_evidence_fields | stage4b_evidence_fields | stage4c_evidence_fields |
|---|---|---|---|---|---|---|
| R11L14_C32_KOREAZINC_MBK_YOUNGPOONG_20240913 | Reuters 2024-09-13; WSJ 2024-09-13; Reuters 2024-10-31; stock-web rows fetched from 2024/2025 shards | Reuters 2024-09-13; WSJ 2024-09-13; Reuters 2024-10-31; stock-web rows fetched from 2024/2025 shards | public_event_or_disclosure, control_premium_or_event_premium, policy_or_regulatory_optionality, relative_strength | durable_customer_confirmation not applicable, multiple_public_sources, financial_visibility not primary | valuation_blowoff, positioning_overheat, capital_raise_or_overhang, legal_or_regulatory_block | [] |
| R11L14_C32_SM_HYBE_KAKAO_20230210 | AP 2023-02-22; AP 2023-03-07; Reuters/secondary timeline via SM reference; stock-web 2023 shard | AP 2023-02-22; AP 2023-03-07; Reuters/secondary timeline via SM reference; stock-web 2023 shard | public_event_or_disclosure, control_premium_or_event_premium, relative_strength, customer_or_order_quality not applicable | multiple_public_sources, repeat_offer_or_conversion, low_red_team_risk until tender cap | explicit_event_cap, control_premium_or_event_premium, positioning_overheat | thesis_evidence_broken watch only after failed/withdrawn bid |
| R11L14_C32_HMM_HARIM_PRIVATIZATION_20231219 | HMM sale/preferred-bidder timeline in public market coverage; Wikipedia HMM sale-fell-through summary; stock-web 2023/2024 shards | HMM sale/preferred-bidder timeline in public market coverage; Wikipedia HMM sale-fell-through summary; stock-web 2023/2024 shards | public_event_or_disclosure, control_premium_or_event_premium, relative_strength | [] | explicit_event_cap, contract_delay, legal_or_contract_risk, positioning_overheat | thesis_evidence_broken, contract_cancelled_or_not_closed |
| R11L14_C32_HANMI_SCIENCE_OCI_INTEGRATION_20240115 | Company disclosure / major Korean business press timeline for OCI-Hanmi integration and later shareholder meeting contest; stock-web 2024 shard | Company disclosure / major Korean business press timeline for OCI-Hanmi integration and later shareholder meeting contest; stock-web 2024 shard | public_event_or_disclosure, control_premium_or_event_premium, relative_strength | [] | positioning_overheat, legal_or_contract_risk, explicit_event_cap | thesis_evidence_broken, governance_vote_failed_or_blocked |

## 10. Price Data Source Map

| symbol | company_name | price_shard_path | profile_path | profile corporate-action status |
|---:|---|---|---|---|
| 010130 | Korea Zinc / 고려아연 | atlas/ohlcv_tradable_by_symbol_year/010/010130/2024.csv; atlas/ohlcv_tradable_by_symbol_year/010/010130/2025.csv | atlas/symbol_profiles/010/010130.json | clean_180D_window |
| 041510 | SM Entertainment / 에스엠 | atlas/ohlcv_tradable_by_symbol_year/041/041510/2023.csv | atlas/symbol_profiles/041/041510.json | clean_180D_window; profile candidates only 2002/2005 |
| 011200 | HMM | atlas/ohlcv_tradable_by_symbol_year/011/011200/2023.csv; atlas/ohlcv_tradable_by_symbol_year/011/011200/2024.csv | atlas/symbol_profiles/011/011200.json | clean_180D_window; 2023-11-10 candidate precedes entry window |
| 008930 | Hanmi Science / 한미사이언스 | atlas/ohlcv_tradable_by_symbol_year/008/008930/2024.csv | atlas/symbol_profiles/008/008930.json | clean_180D_window; profile candidates only 1999/2010/2012 |

## 11. Case-by-Case Trigger Grid

| trigger_id | case_id | trigger_type | trigger_date | entry_date | entry_price | same_entry_group_id | aggregate role | current_profile_verdict |
|---|---|---|---:|---:|---:|---|---|---|
| TR_R11L14_KOREAZINC_TENDER_STAGE2A_20240913 | R11L14_C32_KOREAZINC_MBK_YOUNGPOONG_20240913 | Stage2-Actionable | 2024-09-13 | 2024-09-13 | 666000 | G_010130_2024-09-13_666000 | representative | current_profile_4B_too_early |
| TR_R11L14_SM_HYBE_TENDER_STAGE2A_20230210 | R11L14_C32_SM_HYBE_KAKAO_20230210 | Stage2-Actionable | 2023-02-10 | 2023-02-10 | 114700 | G_041510_2023-02-10_114700 | representative | current_profile_too_late |
| TR_R11L14_HMM_PRIVATIZATION_STAGE2A_20231219 | R11L14_C32_HMM_HARIM_PRIVATIZATION_20231219 | Stage2-Actionable | 2023-12-18 | 2023-12-19 | 18430 | G_011200_2023-12-19_18430 | representative | current_profile_false_positive |
| TR_R11L14_HANMI_OCI_STAGE2A_20240115 | R11L14_C32_HANMI_SCIENCE_OCI_INTEGRATION_20240115 | Stage2-Actionable | 2024-01-12 | 2024-01-15 | 43300 | G_008930_2024-01-15_43300 | representative | current_profile_false_positive |
| TR_R11L14_KOREAZINC_SHARE_ISSUE_4B_20241031 | R11L14_C32_KOREAZINC_MBK_YOUNGPOONG_20240913 | 4B-overlay | 2024-10-31 | 2024-10-31 | 998000 | G_010130_2024-10-31_998000 | 4B_overlay_only | current_profile_4B_too_early |
| TR_R11L14_SM_KAKAO_TENDER_4B_20230307 | R11L14_C32_SM_HYBE_KAKAO_20230210 | 4B-overlay | 2023-03-07 | 2023-03-07 | 149700 | G_041510_2023-03-07_149700 | 4B_overlay_only | current_profile_correct |
| TR_R11L14_HANMI_SHAREHOLDER_VOTE_4C_20240328 | R11L14_C32_HANMI_SCIENCE_OCI_INTEGRATION_20240115 | 4C-thesis-break | 2024-03-28 | 2024-03-28 | 44350 | G_008930_2024-03-28_44350 | 4C_overlay_only | current_profile_4C_too_late |

## 12. Trigger-Level OHLC Backtest Tables

### 12.1 Representative entry triggers

| trigger_id | entry_price | MFE_30D_pct | MAE_30D_pct | MFE_90D_pct | MAE_90D_pct | MFE_180D_pct | MAE_180D_pct | peak_date | peak_price | drawdown_after_peak_pct | outcome label |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|
| TR_R11L14_KOREAZINC_TENDER_STAGE2A_20240913 | 666000 | 131.68 | -1.65 | 261.41 | -1.65 | 261.41 | -3.45 | 2024-12-06 | 2407000 | -73.29 | control_premium_tender_squeeze_success_but_full_4B_needed |
| TR_R11L14_SM_HYBE_TENDER_STAGE2A_20230210 | 114700 | 40.54 | -9.24 | 40.54 | -23.63 | 40.54 | -23.63 | 2023-03-08 | 161200 | -45.66 | tender_cap_success_then_post_contest_reversion |
| TR_R11L14_HMM_PRIVATIZATION_STAGE2A_20231219 | 18430 | 26.42 | -10.20 | 26.42 | -22.68 | 26.42 | -22.68 | 2023-12-20 | 23300 | -38.84 | sale_process_spike_failed_rerating |
| TR_R11L14_HANMI_OCI_STAGE2A_20240115 | 43300 | 29.79 | -10.62 | 29.79 | -27.83 | 29.79 | -40.53 | 2024-01-16 | 56200 | -54.18 | governance_integration_spike_reverted_after_control_dispute |

### 12.2 4B / 4C overlay triggers

| trigger_id | entry_price | MFE_30D_pct | MAE_30D_pct | MFE_90D_pct | MAE_90D_pct | MFE_180D_pct | MAE_180D_pct | peak_date | peak_price | drawdown_after_peak_pct | outcome label |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|
| TR_R11L14_KOREAZINC_SHARE_ISSUE_4B_20241031 | 998000 | 54.21 | -10.02 | 141.18 | -25.95 | 141.18 | -35.57 | 2024-12-06 | 2407000 | -73.29 | non_price_4B_too_early_due_tender_squeeze_continuation |
| TR_R11L14_SM_KAKAO_TENDER_4B_20230307 | 149700 | 7.68 | -41.48 | 7.68 | -41.48 | 7.68 | -41.48 | 2023-03-08 | 161200 | -45.66 | good_full_window_4B_event_cap_timing |
| TR_R11L14_HANMI_SHAREHOLDER_VOTE_4C_20240328 | 44350 | 6.35 | -29.54 | 6.35 | -30.10 | 6.35 | -41.94 | 2024-03-28 | 47000 | -45.21 | hard_4c_success |

Backtest math uses the stock-web close as entry price and the raw high/low window from the entry row through the requested trading-day horizon. Because the data are raw/unadjusted, the profile-level corporate-action window check is applied before treating a row as calibration-usable.

## 13. Current Calibrated Profile Stress Test

| case_id | current profile likely decision | actual alignment | verdict | residual error |
|---|---|---|---|---|
| R11L14_C32_KOREAZINC_MBK_YOUNGPOONG_20240913 | Allows Stage2/Yellow on tender + RS, but may fire 4B too early on non-price overhang | Massive MFE continued beyond early overhang; later drawdown severe | current_profile_4B_too_early | C32 needs separate tender-squeeze continuation vs full 4B |
| R11L14_C32_SM_HYBE_KAKAO_20230210 | May wait for confirmed ownership transfer | Tender cap captured most upside quickly | current_profile_too_late | Competing tender price deserves faster C32 treatment |
| R11L14_C32_HMM_HARIM_PRIVATIZATION_20231219 | Could promote privatization headline + RS as Stage3-Yellow | MFE existed but same-cycle MAE and failed close made it poor rerating | current_profile_false_positive | Preferred bidder without closed terms needs haircut |
| R11L14_C32_HANMI_SCIENCE_OCI_INTEGRATION_20240115 | Could over-promote governance/merger headline and price spike | Spike reverted deeply after control dispute / vote risk | current_profile_false_positive | Shareholder-vote/governance block should route to guard/4C |

Required stress-test answers: Stage2 bonus is useful only for binding or actively competing tender evidence; Yellow 75 is too permissive for unclosed sale processes; Green 87/revision 55 is not the right gate for C32 because the signal is not EPS revision but deal-close probability; price-only blowoff guard is strengthened; full 4B non-price requirement is kept; hard 4C routing is strengthened for failed vote / failed close events.

## 14. Stage2 / Yellow / Green Comparison

| case | Stage2-Actionable entry | plausible Stage3-Green entry | green_lateness_ratio | conclusion |
|---|---:|---:|---:|---|
| Korea Zinc | 666000 | no clean Green before tender mechanics matured | not_applicable | Stage2 worked, but 4B timing was harder than entry timing |
| SM Entertainment | 114700 | 149700 on Kakao competing tender cap | 0.75 | Waiting until the competing bid caught the event cap but consumed most upside |
| HMM | 18430 | no confirmed Stage3 Green trigger | not_applicable | Sale process never became clean rerating evidence |
| Hanmi Science | 43300 | no confirmed Stage3 Green trigger | not_applicable | Governance vote risk should block Green |

## 15. 4B Local vs Full-window Timing Audit

| 4B trigger | Stage2 entry | 4B/4C entry | local peak | full window peak | local proximity | full-window proximity | evidence type | timing verdict |
|---|---:|---:|---:|---:|---:|---:|---|---|
| Korea Zinc 2024-10-31 | 666000 | 998000 | 1543000 | 2407000 | 0.38 | 0.19 | capital_raise_or_overhang, legal_or_regulatory_block, positioning_overheat | non_price_4B_too_early_due_tender_squeeze_continuation |
| SM 2023-03-07 | 114700 | 149700 | 161200 | 161200 | 0.75 | 0.75 | explicit_event_cap, competing tender offer | good_full_window_4B_event_cap_timing |
| Hanmi 2024-03-28 | 43300 | 44350 | 56200 prior peak | 56200 prior peak | not_applicable | not_applicable | governance_vote_failed_or_blocked | hard_4c_success |

## 16. 4C Protection Audit

| case | 4C trigger | protection label | interpretation |
|---|---|---|---|
| HMM | failed close / sale-talk breakdown after preferred bidder spike | hard_4c_late | The market had already retraced; guard should appear earlier as deal-close probability deteriorates |
| Hanmi Science | shareholder-vote / governance block around 2024-03-28 | hard_4c_success | The trigger protected against the later 25750 low; it should be a thesis-break route, not another dip-buy |
| SM | post-contest resolution after Kakao tender cap | thesis_break_watch_only | The 4B event cap was enough; hard 4C only needed if manipulation/legal risk became thesis-breaking |
| Korea Zinc | share issuance / regulatory investigation | thesis_break_watch_only | Non-price risk appeared early, but squeeze mechanics continued; C32 needs staged 4B rather than a binary exit |

## 17. Sector-Specific Rule Candidate

`sector_specific_rule_candidate = true`, but the rule is better treated as canonical C32 first. Within L10 policy/event/cross-redteam, a governance event should not be scored only by the emotional heat of the headline. The rule candidate is:

```text
C32_L10_governance_event_rule:
  if binding_or_competing_tender_price exists:
      allow Stage2-Actionable / Yellow with control-premium component
  if tender cap or fixed offer price is near current price:
      add 4B event-cap overlay, not a fresh Green promotion
  if preferred bidder / merger MoU / family-control dispute lacks closed transaction probability:
      apply unclosed-deal haircut and block Green
  if shareholder vote, regulator, court, or financing failure breaks the route:
      route to 4C thesis-break watch or hard 4C
```

## 18. Canonical-Archetype Rule Candidate

`canonical_archetype_rule_candidate = true`. C32 should compress tender-offer, privatization, and control-family dispute events into one canonical axis, but with a strict split between funded/binding tender evidence and unclosed governance narrative.

| proposed axis | direction | reason |
|---|---:|---|
| C32_binding_or_competing_tender_bonus | +2 shadow | Korea Zinc and SM show high MFE when a real tender price exists |
| C32_unclosed_deal_probability_penalty | -3 shadow | HMM and Hanmi show high-MAE/failed-rerating when the event is not closed or vote-confirmed |
| C32_event_cap_4B_overlay | +1 risk overlay | Fixed tender price often becomes an upside cap and should not be treated as open-ended Green |

## 19. Before / After Backtest Comparison

| profile_id | profile_scope | profile_hypothesis | changed_axes | eligible_trigger_count | avg_MFE_90D_pct | avg_MAE_90D_pct | avg_MFE_180D_pct | avg_MAE_180D_pct | false_positive_rate | missed_structural_count | late_green_count | score_return_alignment_verdict |
|---|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| P0 | e2r_2_1_stock_web_calibrated_proxy | current global calibrated profile | none | 4 | 89.54 | -18.95 | 89.54 | -22.57 | 0.50 | 0 | 1 | mixed; positive control premium and false positives both pass too easily |
| P0b | e2r_2_0_baseline_reference | old baseline | lower Stage2/Green discipline | 4 | 89.54 | -18.95 | 89.54 | -22.57 | 0.75 | 0 | 2 | worse; treats event headline and price strength too generously |
| P1 | sector_specific_candidate_profile | L10 governance/tender event profile | add event-cap and unclosed-deal haircut | 4 | 89.54 | -18.95 | 89.54 | -22.57 | 0.25 | 0 | 0 | better alignment; positives retained, false positives demoted |
| P2 | canonical_archetype_candidate_profile | C32 tender/control premium profile | binding tender bonus + unclosed deal penalty | 4 | 89.54 | -18.95 | 89.54 | -22.57 | 0.00 | 0 | 0 | best shadow fit in this loop |
| P3 | counterexample_guard_profile | strict deal-close guard | demote all unclosed deals unless tender price is binding/competing | 4 | 89.54 | -18.95 | 89.54 | -22.57 | 0.00 | 1 | 0 | safer but may under-promote Korea Zinc early squeeze |

## 20. Score-Return Alignment Matrix

| case | before label | before score | after label | after score | price result | alignment |
|---|---|---:|---|---:|---|---|
| Korea Zinc | Stage3-Yellow / early 4B risk | 82 | Stage3-Green_control_premium_allowed + staged 4B | 88 | MFE180 261.41 / MAE180 -3.45 | improved |
| SM | Stage2/Yellow too late | 82 | Stage3-Green_control_premium_allowed + event-cap 4B | 88 | MFE180 40.54 / MAE180 -23.63 | improved |
| HMM | Stage3-Yellow false-positive risk | 79 | Stage2-watch / unclosed-deal haircut | 61 | MFE180 26.42 / MAE180 -22.68 | improved |
| Hanmi Science | Stage3-Yellow false-positive risk | 79 | Stage2-watch then 4C guard | 61 | MFE180 29.79 / MAE180 -40.53 | improved |

## 21. Coverage Matrix

| large_sector_id | canonical_archetype_id | fine_archetype_id | positive_case_count | counterexample_count | 4B_case_count | 4C_case_count | new_independent_case_count | reused_case_count | calibration_usable_trigger_count | representative_trigger_count | current_profile_error_count | sector_rule_candidate | canonical_rule_candidate | coverage_gap_after_this_loop |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|---|---|
| L10_POLICY_EVENT_CROSS_REDTEAM_MISC | C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP | CONTROL_PREMIUM_TENDER_CAP_VS_UNCLOSED_GOVERNANCE_STORY | 2 | 2 | 2 | 1 | 4 | 0 | 7 | 4 | 4 | true | true | still needs additional tender-offer delisting / tender-failure holdout cases |

## 22. Residual Contribution Summary

```text
new_independent_case_count: 4
reused_case_count: 0
reused_case_ids: []
new_symbol_count: 4
new_canonical_archetype_count: 0
new_fine_archetype_count: 4
new_trigger_family_count: 4
tested_existing_calibrated_axes: [price_only_blowoff_blocks_positive_stage, full_4b_requires_non_price_evidence, hard_4c_thesis_break_routes_to_4c, stage3_green_revision_min]
residual_error_types_found: [current_profile_4B_too_early, current_profile_too_late, current_profile_false_positive, current_profile_4C_too_late]
new_axis_proposed: [C32_binding_or_competing_tender_bonus, C32_unclosed_deal_probability_penalty, C32_event_cap_4B_overlay]
existing_axis_strengthened: [price_only_blowoff_blocks_positive_stage, full_4b_requires_non_price_evidence, hard_4c_thesis_break_routes_to_4c]
existing_axis_weakened: []
existing_axis_kept: [stage2_actionable_evidence_bonus, stage3_yellow_total_min, stage3_green_total_min, stage3_green_revision_min]
sector_specific_rule_candidate: true
canonical_archetype_rule_candidate: true
no_new_signal_reason: null
loop_contribution_label: canonical_archetype_rule_candidate
do_not_propose_new_weight_delta: false
```

## 23. Validation Scope / Non-Validation Scope

Validated: historical trigger dates, stock-web tradable close/high/low windows, clean 180D corporate-action status, representative trigger dedupe, C32-specific positive/counterexample split, 4B local vs full-window logic.

Not validated: live candidate discovery, investment recommendation, production score code behavior, broker execution, or any stock_agent source-code implementation.

## 24. Shadow Weight Calibration

```csv
row_type,axis,scope,large_sector_id,canonical_archetype_id,baseline_value,tested_value,delta,reason,backtest_effect,trigger_ids,calibration_usable_count,new_independent_case_count,counterexample_count,confidence,proposal_type,notes
shadow_weight,C32_binding_or_competing_tender_bonus,canonical_archetype_specific,L10_POLICY_EVENT_CROSS_REDTEAM_MISC,C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP,0,+2,+2,"Binding or actively competing tender offers created high MFE in Korea Zinc and SM",positive cases retained while not weakening 4B guard,TR_R11L14_KOREAZINC_TENDER_STAGE2A_20240913|TR_R11L14_SM_HYBE_TENDER_STAGE2A_20230210,4,4,2,medium,canonical_shadow_only,"not production; post-calibrated residual"
shadow_weight,C32_unclosed_deal_probability_penalty,canonical_archetype_specific,L10_POLICY_EVENT_CROSS_REDTEAM_MISC,C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP,0,-3,-3,"HMM and Hanmi show event headline without closed control transfer can become false-positive Yellow/Green",reduces false positive rate,TR_R11L14_HMM_PRIVATIZATION_STAGE2A_20231219|TR_R11L14_HANMI_OCI_STAGE2A_20240115,4,4,2,medium,canonical_shadow_only,"not production; requires batch ledger review"
shadow_weight,C32_event_cap_4B_overlay,canonical_archetype_specific,L10_POLICY_EVENT_CROSS_REDTEAM_MISC,C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP,0,+1,+1,"Tender cap or shareholder-vote failure should become 4B/4C overlay, not a fresh positive-stage promotion",improves exit/protection timing,TR_R11L14_SM_KAKAO_TENDER_4B_20230307|TR_R11L14_HANMI_SHAREHOLDER_VOTE_4C_20240328,4,4,2,low,canonical_shadow_only,"not production; post-calibrated residual"
```

## 25. Machine-Readable Rows

### 25.1 price_source_validation

```jsonl
{"row_type": "price_source_validation", "source": "Songdaiki/stock-web", "source_url": "https://github.com/Songdaiki/stock-web", "manifest_path": "atlas/manifest.json", "schema_path": "atlas/schema.json", "universe_path": "atlas/universe/all_symbols.csv", "manifest_max_date": "2026-02-20", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "raw_shard_root": "atlas/ohlcv_raw_by_symbol_year", "validation_status": "usable_for_historical_calibration"}
```

### 25.2 case rows

```jsonl
{"row_type": "case", "case_id": "R11L14_C32_KOREAZINC_MBK_YOUNGPOONG_20240913", "symbol": "010130", "company_name": "Korea Zinc / 고려아연", "round": "R11", "loop": "14", "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP", "fine_archetype_id": "HOSTILE_TENDER_CONTROL_PREMIUM_SQUEEZE", "case_type": "structural_success / 4B_overlay_success", "positive_or_counterexample": "positive", "best_trigger": "TR_R11L14_KOREAZINC_TENDER_STAGE2A_20240913", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "control_premium_tender_squeeze_success_but_full_4B_needed", "current_profile_verdict": "current_profile_4B_too_early", "price_source": "Songdaiki/stock-web", "notes": "C32 event/control-premium historical trigger; not live candidate research"}
{"row_type": "case", "case_id": "R11L14_C32_SM_HYBE_KAKAO_20230210", "symbol": "041510", "company_name": "SM Entertainment / 에스엠", "round": "R11", "loop": "14", "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP", "fine_archetype_id": "KPOP_CONTROL_PREMIUM_TENDER_BATTLE", "case_type": "structural_success / 4B_event_cap", "positive_or_counterexample": "positive", "best_trigger": "TR_R11L14_SM_HYBE_TENDER_STAGE2A_20230210", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "tender_cap_success_then_post_contest_reversion", "current_profile_verdict": "current_profile_too_late", "price_source": "Songdaiki/stock-web", "notes": "C32 event/control-premium historical trigger; not live candidate research"}
{"row_type": "case", "case_id": "R11L14_C32_HMM_HARIM_PRIVATIZATION_20231219", "symbol": "011200", "company_name": "HMM", "round": "R11", "loop": "14", "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP", "fine_archetype_id": "PRIVATIZATION_PREFERRED_BIDDER_UNCLOSED_DEAL", "case_type": "failed_rerating / false_positive_green", "positive_or_counterexample": "counterexample", "best_trigger": "TR_R11L14_HMM_PRIVATIZATION_STAGE2A_20231219", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "sale_process_spike_failed_rerating", "current_profile_verdict": "current_profile_false_positive", "price_source": "Songdaiki/stock-web", "notes": "C32 event/control-premium historical trigger; not live candidate research"}
{"row_type": "case", "case_id": "R11L14_C32_HANMI_SCIENCE_OCI_INTEGRATION_20240115", "symbol": "008930", "company_name": "Hanmi Science / 한미사이언스", "round": "R11", "loop": "14", "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP", "fine_archetype_id": "FAMILY_CONTROL_MERGER_VOTE_RISK", "case_type": "failed_rerating / 4C_success", "positive_or_counterexample": "counterexample", "best_trigger": "TR_R11L14_HANMI_OCI_STAGE2A_20240115", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "governance_integration_spike_reverted_after_control_dispute", "current_profile_verdict": "current_profile_false_positive", "price_source": "Songdaiki/stock-web", "notes": "C32 event/control-premium historical trigger; not live candidate research"}
```

### 25.3 trigger rows

```jsonl
{"row_type": "trigger", "trigger_id": "TR_R11L14_KOREAZINC_TENDER_STAGE2A_20240913", "case_id": "R11L14_C32_KOREAZINC_MBK_YOUNGPOONG_20240913", "symbol": "010130", "company_name": "Korea Zinc / 고려아연", "round": "R11", "loop": "14", "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP", "fine_archetype_id": "HOSTILE_TENDER_CONTROL_PREMIUM_SQUEEZE", "sector": "policy_event_cross_redteam_misc", "primary_archetype": "governance_control_premium_tender_cap", "loop_objective": "coverage_gap_fill|counterexample_mining|sector_specific_rule_discovery", "trigger_type": "Stage2-Actionable", "trigger_date": "2024-09-13", "evidence_available_at_that_date": "Reuters 2024-09-13; WSJ 2024-09-13; Reuters 2024-10-31; stock-web rows fetched from 2024/2025 shards", "evidence_source": "Reuters 2024-09-13; WSJ 2024-09-13; Reuters 2024-10-31; stock-web rows fetched from 2024/2025 shards", "stage2_evidence_fields": ["public_event_or_disclosure", "control_premium_or_event_premium", "policy_or_regulatory_optionality", "relative_strength"], "stage3_evidence_fields": ["durable_customer_confirmation not applicable", "multiple_public_sources", "financial_visibility not primary"], "stage4b_evidence_fields": ["valuation_blowoff", "positioning_overheat", "capital_raise_or_overhang", "legal_or_regulatory_block"], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/010/010130/2024.csv; atlas/ohlcv_tradable_by_symbol_year/010/010130/2025.csv", "profile_path": "atlas/symbol_profiles/010/010130.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "entry_date": "2024-09-13", "entry_price": 666000, "MFE_30D_pct": 131.68, "MFE_90D_pct": 261.41, "MFE_180D_pct": 261.41, "MFE_1Y_pct": 261.41, "MFE_2Y_pct": null, "MAE_30D_pct": -1.65, "MAE_90D_pct": -1.65, "MAE_180D_pct": -3.45, "MAE_1Y_pct": -3.45, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2024-12-06", "peak_price": 2407000, "drawdown_after_peak_pct": -73.29, "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": null, "four_b_full_window_peak_proximity": null, "four_b_timing_verdict": "not_applicable_for_representative_entry", "four_b_evidence_type": [], "four_c_protection_label": "not_applicable", "trigger_outcome_label": "control_premium_tender_squeeze_success_but_full_4B_needed", "current_profile_verdict": "current_profile_4B_too_early", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window", "same_entry_group_id": "G_010130_2024-09-13_666000", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false}
{"row_type": "trigger", "trigger_id": "TR_R11L14_SM_HYBE_TENDER_STAGE2A_20230210", "case_id": "R11L14_C32_SM_HYBE_KAKAO_20230210", "symbol": "041510", "company_name": "SM Entertainment / 에스엠", "round": "R11", "loop": "14", "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP", "fine_archetype_id": "KPOP_CONTROL_PREMIUM_TENDER_BATTLE", "sector": "policy_event_cross_redteam_misc", "primary_archetype": "governance_control_premium_tender_cap", "loop_objective": "coverage_gap_fill|counterexample_mining|sector_specific_rule_discovery", "trigger_type": "Stage2-Actionable", "trigger_date": "2023-02-10", "evidence_available_at_that_date": "AP 2023-02-22; AP 2023-03-07; Reuters/secondary timeline via SM reference; stock-web 2023 shard", "evidence_source": "AP 2023-02-22; AP 2023-03-07; Reuters/secondary timeline via SM reference; stock-web 2023 shard", "stage2_evidence_fields": ["public_event_or_disclosure", "control_premium_or_event_premium", "relative_strength", "customer_or_order_quality not applicable"], "stage3_evidence_fields": ["multiple_public_sources", "repeat_offer_or_conversion", "low_red_team_risk until tender cap"], "stage4b_evidence_fields": ["explicit_event_cap", "control_premium_or_event_premium", "positioning_overheat"], "stage4c_evidence_fields": ["thesis_evidence_broken watch only after failed/withdrawn bid"], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/041/041510/2023.csv", "profile_path": "atlas/symbol_profiles/041/041510.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "entry_date": "2023-02-10", "entry_price": 114700, "MFE_30D_pct": 40.54, "MFE_90D_pct": 40.54, "MFE_180D_pct": 40.54, "MFE_1Y_pct": 40.54, "MFE_2Y_pct": null, "MAE_30D_pct": -9.24, "MAE_90D_pct": -23.63, "MAE_180D_pct": -23.63, "MAE_1Y_pct": -23.63, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2023-03-08", "peak_price": 161200, "drawdown_after_peak_pct": -45.66, "green_lateness_ratio": 0.75, "four_b_local_peak_proximity": null, "four_b_full_window_peak_proximity": null, "four_b_timing_verdict": "not_applicable_for_representative_entry", "four_b_evidence_type": [], "four_c_protection_label": "not_applicable", "trigger_outcome_label": "tender_cap_success_then_post_contest_reversion", "current_profile_verdict": "current_profile_too_late", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window; profile candidates only 2002/2005", "same_entry_group_id": "G_041510_2023-02-10_114700", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false}
{"row_type": "trigger", "trigger_id": "TR_R11L14_HMM_PRIVATIZATION_STAGE2A_20231219", "case_id": "R11L14_C32_HMM_HARIM_PRIVATIZATION_20231219", "symbol": "011200", "company_name": "HMM", "round": "R11", "loop": "14", "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP", "fine_archetype_id": "PRIVATIZATION_PREFERRED_BIDDER_UNCLOSED_DEAL", "sector": "policy_event_cross_redteam_misc", "primary_archetype": "governance_control_premium_tender_cap", "loop_objective": "coverage_gap_fill|counterexample_mining|sector_specific_rule_discovery", "trigger_type": "Stage2-Actionable", "trigger_date": "2023-12-18", "evidence_available_at_that_date": "HMM sale/preferred-bidder timeline in public market coverage; Wikipedia HMM sale-fell-through summary; stock-web 2023/2024 shards", "evidence_source": "HMM sale/preferred-bidder timeline in public market coverage; Wikipedia HMM sale-fell-through summary; stock-web 2023/2024 shards", "stage2_evidence_fields": ["public_event_or_disclosure", "control_premium_or_event_premium", "relative_strength"], "stage3_evidence_fields": [], "stage4b_evidence_fields": ["explicit_event_cap", "contract_delay", "legal_or_contract_risk", "positioning_overheat"], "stage4c_evidence_fields": ["thesis_evidence_broken", "contract_cancelled_or_not_closed"], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/011/011200/2023.csv; atlas/ohlcv_tradable_by_symbol_year/011/011200/2024.csv", "profile_path": "atlas/symbol_profiles/011/011200.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "entry_date": "2023-12-19", "entry_price": 18430, "MFE_30D_pct": 26.42, "MFE_90D_pct": 26.42, "MFE_180D_pct": 26.42, "MFE_1Y_pct": 26.42, "MFE_2Y_pct": null, "MAE_30D_pct": -10.2, "MAE_90D_pct": -22.68, "MAE_180D_pct": -22.68, "MAE_1Y_pct": -22.68, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2023-12-20", "peak_price": 23300, "drawdown_after_peak_pct": -38.84, "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": null, "four_b_full_window_peak_proximity": null, "four_b_timing_verdict": "not_applicable_for_representative_entry", "four_b_evidence_type": [], "four_c_protection_label": "thesis_break_watch_only", "trigger_outcome_label": "sale_process_spike_failed_rerating", "current_profile_verdict": "current_profile_false_positive", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window; 2023-11-10 candidate precedes entry window", "same_entry_group_id": "G_011200_2023-12-19_18430", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false}
{"row_type": "trigger", "trigger_id": "TR_R11L14_HANMI_OCI_STAGE2A_20240115", "case_id": "R11L14_C32_HANMI_SCIENCE_OCI_INTEGRATION_20240115", "symbol": "008930", "company_name": "Hanmi Science / 한미사이언스", "round": "R11", "loop": "14", "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP", "fine_archetype_id": "FAMILY_CONTROL_MERGER_VOTE_RISK", "sector": "policy_event_cross_redteam_misc", "primary_archetype": "governance_control_premium_tender_cap", "loop_objective": "coverage_gap_fill|counterexample_mining|sector_specific_rule_discovery", "trigger_type": "Stage2-Actionable", "trigger_date": "2024-01-12", "evidence_available_at_that_date": "Company disclosure / major Korean business press timeline for OCI-Hanmi integration and later shareholder meeting contest; stock-web 2024 shard", "evidence_source": "Company disclosure / major Korean business press timeline for OCI-Hanmi integration and later shareholder meeting contest; stock-web 2024 shard", "stage2_evidence_fields": ["public_event_or_disclosure", "control_premium_or_event_premium", "relative_strength"], "stage3_evidence_fields": [], "stage4b_evidence_fields": ["positioning_overheat", "legal_or_contract_risk", "explicit_event_cap"], "stage4c_evidence_fields": ["thesis_evidence_broken", "governance_vote_failed_or_blocked"], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/008/008930/2024.csv", "profile_path": "atlas/symbol_profiles/008/008930.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "entry_date": "2024-01-15", "entry_price": 43300, "MFE_30D_pct": 29.79, "MFE_90D_pct": 29.79, "MFE_180D_pct": 29.79, "MFE_1Y_pct": 29.79, "MFE_2Y_pct": null, "MAE_30D_pct": -10.62, "MAE_90D_pct": -27.83, "MAE_180D_pct": -40.53, "MAE_1Y_pct": -40.53, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2024-01-16", "peak_price": 56200, "drawdown_after_peak_pct": -54.18, "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": null, "four_b_full_window_peak_proximity": null, "four_b_timing_verdict": "not_applicable_for_representative_entry", "four_b_evidence_type": [], "four_c_protection_label": "thesis_break_watch_only", "trigger_outcome_label": "governance_integration_spike_reverted_after_control_dispute", "current_profile_verdict": "current_profile_false_positive", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window; profile candidates only 1999/2010/2012", "same_entry_group_id": "G_008930_2024-01-15_43300", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false}
{"row_type": "trigger", "trigger_id": "TR_R11L14_KOREAZINC_SHARE_ISSUE_4B_20241031", "case_id": "R11L14_C32_KOREAZINC_MBK_YOUNGPOONG_20240913", "symbol": "010130", "company_name": "Korea Zinc / 고려아연", "round": "R11", "loop": "14", "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP", "fine_archetype_id": "CONTROL_PREMIUM_4B_4C_OVERLAY", "sector": "policy_event_cross_redteam_misc", "primary_archetype": "governance_control_premium_tender_cap", "loop_objective": "4B_non_price_requirement_stress_test|4C_thesis_break_timing_test", "trigger_type": "4B-overlay", "trigger_date": "2024-10-31", "evidence_available_at_that_date": "event-cap / governance-risk overlay evidence available at trigger", "evidence_source": "web/public coverage + stock-web OHLC rows", "stage2_evidence_fields": [], "stage3_evidence_fields": [], "stage4b_evidence_fields": ["capital_raise_or_overhang", "legal_or_regulatory_block", "positioning_overheat"], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "see representative case source map", "profile_path": "see representative case source map", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "entry_date": "2024-10-31", "entry_price": 998000, "MFE_30D_pct": 54.21, "MFE_90D_pct": 141.18, "MFE_180D_pct": 141.18, "MFE_1Y_pct": null, "MFE_2Y_pct": null, "MAE_30D_pct": -10.02, "MAE_90D_pct": -25.95, "MAE_180D_pct": -35.57, "MAE_1Y_pct": null, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2024-12-06", "peak_price": 2407000, "drawdown_after_peak_pct": -73.29, "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": 0.38, "four_b_full_window_peak_proximity": 0.19, "four_b_timing_verdict": "non_price_4B_too_early_due_tender_squeeze_continuation", "four_b_evidence_type": ["capital_raise_or_overhang", "legal_or_regulatory_block", "positioning_overheat"], "four_c_protection_label": "not_applicable", "trigger_outcome_label": "non_price_4B_too_early_due_tender_squeeze_continuation", "current_profile_verdict": "current_profile_4B_too_early", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window", "same_entry_group_id": "G_010130_2024-10-31_998000", "dedupe_for_aggregate": false, "aggregate_group_role": "4B_overlay_only", "is_new_independent_case": false, "reuse_reason": "overlay trigger for already counted representative case", "independent_evidence_weight": 0.0, "do_not_count_as_new_case": true}
{"row_type": "trigger", "trigger_id": "TR_R11L14_SM_KAKAO_TENDER_4B_20230307", "case_id": "R11L14_C32_SM_HYBE_KAKAO_20230210", "symbol": "041510", "company_name": "SM Entertainment / 에스엠", "round": "R11", "loop": "14", "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP", "fine_archetype_id": "CONTROL_PREMIUM_4B_4C_OVERLAY", "sector": "policy_event_cross_redteam_misc", "primary_archetype": "governance_control_premium_tender_cap", "loop_objective": "4B_non_price_requirement_stress_test|4C_thesis_break_timing_test", "trigger_type": "4B-overlay", "trigger_date": "2023-03-07", "evidence_available_at_that_date": "event-cap / governance-risk overlay evidence available at trigger", "evidence_source": "web/public coverage + stock-web OHLC rows", "stage2_evidence_fields": [], "stage3_evidence_fields": [], "stage4b_evidence_fields": ["control_premium_or_event_premium", "explicit_event_cap", "positioning_overheat"], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "see representative case source map", "profile_path": "see representative case source map", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "entry_date": "2023-03-07", "entry_price": 149700, "MFE_30D_pct": 7.68, "MFE_90D_pct": 7.68, "MFE_180D_pct": 7.68, "MFE_1Y_pct": null, "MFE_2Y_pct": null, "MAE_30D_pct": -41.48, "MAE_90D_pct": -41.48, "MAE_180D_pct": -41.48, "MAE_1Y_pct": null, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2023-03-08", "peak_price": 161200, "drawdown_after_peak_pct": -45.66, "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": 0.75, "four_b_full_window_peak_proximity": 0.75, "four_b_timing_verdict": "good_full_window_4B_event_cap_timing", "four_b_evidence_type": ["control_premium_or_event_premium", "explicit_event_cap", "positioning_overheat"], "four_c_protection_label": "not_applicable", "trigger_outcome_label": "good_full_window_4B_event_cap_timing", "current_profile_verdict": "current_profile_correct", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window", "same_entry_group_id": "G_041510_2023-03-07_149700", "dedupe_for_aggregate": false, "aggregate_group_role": "4B_overlay_only", "is_new_independent_case": false, "reuse_reason": "overlay trigger for already counted representative case", "independent_evidence_weight": 0.0, "do_not_count_as_new_case": true}
{"row_type": "trigger", "trigger_id": "TR_R11L14_HANMI_SHAREHOLDER_VOTE_4C_20240328", "case_id": "R11L14_C32_HANMI_SCIENCE_OCI_INTEGRATION_20240115", "symbol": "008930", "company_name": "Hanmi Science / 한미사이언스", "round": "R11", "loop": "14", "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP", "fine_archetype_id": "CONTROL_PREMIUM_4B_4C_OVERLAY", "sector": "policy_event_cross_redteam_misc", "primary_archetype": "governance_control_premium_tender_cap", "loop_objective": "4B_non_price_requirement_stress_test|4C_thesis_break_timing_test", "trigger_type": "4C-thesis-break", "trigger_date": "2024-03-28", "evidence_available_at_that_date": "event-cap / governance-risk overlay evidence available at trigger", "evidence_source": "web/public coverage + stock-web OHLC rows", "stage2_evidence_fields": [], "stage3_evidence_fields": [], "stage4b_evidence_fields": [], "stage4c_evidence_fields": ["thesis_evidence_broken", "governance_vote_failed_or_blocked"], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "see representative case source map", "profile_path": "see representative case source map", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "entry_date": "2024-03-28", "entry_price": 44350, "MFE_30D_pct": 6.35, "MFE_90D_pct": 6.35, "MFE_180D_pct": 6.35, "MFE_1Y_pct": null, "MFE_2Y_pct": null, "MAE_30D_pct": -29.54, "MAE_90D_pct": -30.1, "MAE_180D_pct": -41.94, "MAE_1Y_pct": null, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2024-03-28", "peak_price": 47000, "drawdown_after_peak_pct": -45.21, "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": null, "four_b_full_window_peak_proximity": null, "four_b_timing_verdict": "hard_4c_success", "four_b_evidence_type": ["thesis_evidence_broken", "governance_vote_failed_or_blocked"], "four_c_protection_label": "hard_4c_success", "trigger_outcome_label": "hard_4c_success", "current_profile_verdict": "current_profile_4C_too_late", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window", "same_entry_group_id": "G_008930_2024-03-28_44350", "dedupe_for_aggregate": false, "aggregate_group_role": "4C_overlay_only", "is_new_independent_case": false, "reuse_reason": "overlay trigger for already counted representative case", "independent_evidence_weight": 0.0, "do_not_count_as_new_case": true}
```

### 25.4 score_simulation rows

```jsonl
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R11L14_C32_KOREAZINC_MBK_YOUNGPOONG_20240913", "trigger_id": "TR_R11L14_KOREAZINC_TENDER_STAGE2A_20240913", "symbol": "010130", "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP", "raw_component_scores_before": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 0, "revision_score": 0, "relative_strength_score": 70, "customer_quality_score": 0, "policy_or_regulatory_score": 55, "valuation_repricing_score": 75, "execution_risk_score": 35, "legal_or_contract_risk_score": 30, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 10}, "weighted_score_before": 82, "stage_label_before": "Stage3-Yellow", "raw_component_scores_after": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 0, "revision_score": 0, "relative_strength_score": 70, "customer_quality_score": 0, "policy_or_regulatory_score": 55, "valuation_repricing_score": 80, "execution_risk_score": 40, "legal_or_contract_risk_score": 35, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 15}, "weighted_score_after": 88, "stage_label_after": "Stage3-Green_control_premium_allowed", "changed_components": ["control_premium_or_event_premium", "deal_close_probability_guard", "tender_cap_guard", "uncleared_governance_risk_penalty"], "component_delta_explanation": "C32 shadow profile separates binding/competitive tender premium from unclosed privatization or family-control dispute stories.", "MFE_90D_pct": 261.41, "MAE_90D_pct": -1.65, "score_return_alignment_label": "control_premium_tender_squeeze_success_but_full_4B_needed", "current_profile_verdict": "current_profile_4B_too_early"}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R11L14_C32_SM_HYBE_KAKAO_20230210", "trigger_id": "TR_R11L14_SM_HYBE_TENDER_STAGE2A_20230210", "symbol": "041510", "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP", "raw_component_scores_before": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 0, "revision_score": 0, "relative_strength_score": 70, "customer_quality_score": 0, "policy_or_regulatory_score": 55, "valuation_repricing_score": 75, "execution_risk_score": 35, "legal_or_contract_risk_score": 30, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 10}, "weighted_score_before": 82, "stage_label_before": "Stage3-Yellow", "raw_component_scores_after": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 0, "revision_score": 0, "relative_strength_score": 70, "customer_quality_score": 0, "policy_or_regulatory_score": 55, "valuation_repricing_score": 80, "execution_risk_score": 40, "legal_or_contract_risk_score": 35, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 10}, "weighted_score_after": 88, "stage_label_after": "Stage3-Green_control_premium_allowed", "changed_components": ["control_premium_or_event_premium", "deal_close_probability_guard", "tender_cap_guard", "uncleared_governance_risk_penalty"], "component_delta_explanation": "C32 shadow profile separates binding/competitive tender premium from unclosed privatization or family-control dispute stories.", "MFE_90D_pct": 40.54, "MAE_90D_pct": -23.63, "score_return_alignment_label": "tender_cap_success_then_post_contest_reversion", "current_profile_verdict": "current_profile_too_late"}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R11L14_C32_HMM_HARIM_PRIVATIZATION_20231219", "trigger_id": "TR_R11L14_HMM_PRIVATIZATION_STAGE2A_20231219", "symbol": "011200", "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP", "raw_component_scores_before": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 0, "revision_score": 0, "relative_strength_score": 70, "customer_quality_score": 0, "policy_or_regulatory_score": 40, "valuation_repricing_score": 50, "execution_risk_score": 70, "legal_or_contract_risk_score": 65, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 10}, "weighted_score_before": 79, "stage_label_before": "Stage3-Yellow_false_positive_risk", "raw_component_scores_after": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 0, "revision_score": 0, "relative_strength_score": 70, "customer_quality_score": 0, "policy_or_regulatory_score": 25, "valuation_repricing_score": 35, "execution_risk_score": 78, "legal_or_contract_risk_score": 80, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 10}, "weighted_score_after": 61, "stage_label_after": "Stage2-watch_or_4C_guard", "changed_components": ["control_premium_or_event_premium", "deal_close_probability_guard", "tender_cap_guard", "uncleared_governance_risk_penalty"], "component_delta_explanation": "C32 shadow profile separates binding/competitive tender premium from unclosed privatization or family-control dispute stories.", "MFE_90D_pct": 26.42, "MAE_90D_pct": -22.68, "score_return_alignment_label": "sale_process_spike_failed_rerating", "current_profile_verdict": "current_profile_false_positive"}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R11L14_C32_HANMI_SCIENCE_OCI_INTEGRATION_20240115", "trigger_id": "TR_R11L14_HANMI_OCI_STAGE2A_20240115", "symbol": "008930", "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP", "raw_component_scores_before": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 0, "revision_score": 0, "relative_strength_score": 70, "customer_quality_score": 0, "policy_or_regulatory_score": 40, "valuation_repricing_score": 50, "execution_risk_score": 70, "legal_or_contract_risk_score": 65, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 10}, "weighted_score_before": 79, "stage_label_before": "Stage3-Yellow_false_positive_risk", "raw_component_scores_after": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 0, "revision_score": 0, "relative_strength_score": 70, "customer_quality_score": 0, "policy_or_regulatory_score": 25, "valuation_repricing_score": 35, "execution_risk_score": 78, "legal_or_contract_risk_score": 80, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 10}, "weighted_score_after": 61, "stage_label_after": "Stage2-watch_or_4C_guard", "changed_components": ["control_premium_or_event_premium", "deal_close_probability_guard", "tender_cap_guard", "uncleared_governance_risk_penalty"], "component_delta_explanation": "C32 shadow profile separates binding/competitive tender premium from unclosed privatization or family-control dispute stories.", "MFE_90D_pct": 29.79, "MAE_90D_pct": -27.83, "score_return_alignment_label": "governance_integration_spike_reverted_after_control_dispute", "current_profile_verdict": "current_profile_false_positive"}
```

### 25.5 shadow_weight rows

```csv
row_type,axis,scope,large_sector_id,canonical_archetype_id,baseline_value,tested_value,delta,reason,backtest_effect,trigger_ids,calibration_usable_count,new_independent_case_count,counterexample_count,confidence,proposal_type,notes
shadow_weight,C32_binding_or_competing_tender_bonus,canonical_archetype_specific,L10_POLICY_EVENT_CROSS_REDTEAM_MISC,C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP,0,+2,+2,"Binding or actively competing tender offers created high MFE in Korea Zinc and SM",positive cases retained while not weakening 4B guard,TR_R11L14_KOREAZINC_TENDER_STAGE2A_20240913|TR_R11L14_SM_HYBE_TENDER_STAGE2A_20230210,4,4,2,medium,canonical_shadow_only,"not production; post-calibrated residual"
shadow_weight,C32_unclosed_deal_probability_penalty,canonical_archetype_specific,L10_POLICY_EVENT_CROSS_REDTEAM_MISC,C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP,0,-3,-3,"HMM and Hanmi show event headline without closed control transfer can become false-positive Yellow/Green",reduces false positive rate,TR_R11L14_HMM_PRIVATIZATION_STAGE2A_20231219|TR_R11L14_HANMI_OCI_STAGE2A_20240115,4,4,2,medium,canonical_shadow_only,"not production; requires batch ledger review"
shadow_weight,C32_event_cap_4B_overlay,canonical_archetype_specific,L10_POLICY_EVENT_CROSS_REDTEAM_MISC,C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP,0,+1,+1,"Tender cap or shareholder-vote failure should become 4B/4C overlay, not a fresh positive-stage promotion",improves exit/protection timing,TR_R11L14_SM_KAKAO_TENDER_4B_20230307|TR_R11L14_HANMI_SHAREHOLDER_VOTE_4C_20240328,4,4,2,low,canonical_shadow_only,"not production; post-calibrated residual"
```

### 25.6 residual_contribution row

```jsonl
{"row_type": "residual_contribution", "round": "R11", "loop": "14", "scheduled_round": "R11", "scheduled_loop": 14, "round_schedule_status": "valid", "round_sector_consistency": "pass", "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP", "new_independent_case_count": 4, "reused_case_count": 0, "new_symbol_count": 4, "same_archetype_new_symbol_count": 4, "same_archetype_new_trigger_family_count": 4, "new_trigger_family_count": 4, "positive_case_count": 2, "counterexample_count": 2, "current_profile_error_count": 4, "diversity_score_summary": "4 new C32 symbols and 4 trigger families; no reused cases; R11 loop14 schedule valid", "tested_existing_calibrated_axes": ["price_only_blowoff_blocks_positive_stage", "full_4b_requires_non_price_evidence", "hard_4c_thesis_break_routes_to_4c"], "residual_error_types_found": ["current_profile_4B_too_early", "current_profile_too_late", "current_profile_false_positive", "current_profile_4C_too_late"], "loop_contribution_label": "canonical_archetype_rule_candidate", "do_not_propose_new_weight_delta": false}
```

### 25.7 narrative_only rows

```jsonl
{"row_type": "narrative_only", "case_id": "R11L14_C32_OSSTEM_IMPLANT_TENDER_DELISTING_NOT_USED", "symbol": "048260", "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP", "reason": "delisting/tender case is useful narratively but not selected because the current loop already meets calibration balance without relying on inactive-window complexity", "price_source": "Songdaiki/stock-web", "usage": "not_weight_calibration"}
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
completed_round = R11
completed_loop = 14
next_round = R12
next_loop = 14
round_schedule_status = valid
round_sector_consistency = pass
```

## 28. Source Notes

Stock-Web source validation was based on `atlas/manifest.json`, `atlas/schema.json`, and the symbol profile / OHLC shards named in the Price Data Source Map. External event evidence used public historical coverage: Reuters and WSJ for Korea Zinc/MBK/Young Poong; AP for HYBE/Kakao/SM tender events; public sale-process summaries for HMM; and Korean company disclosure / business-press timeline for Hanmi Science / OCI integration and shareholder-vote risk. No live candidate search, stock_agent source-code read, or production patch was performed.

