# E2R Stock-Web Historical Calibration / Sector-Archetype Residual Research Round

## 0. Research Metadata

```text
mode = historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12
research_session = post_calibrated_sector_archetype_residual_research
scheduled_round = R7
scheduled_loop = 73
large_sector_id = L7_BIO_HEALTHCARE_MEDICAL
canonical_archetype_id = C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION
fine_archetype_id = BIO_APPROVAL_COMMERCIALIZATION_BINARY_EVENT_GUARD
output_file = e2r_stock_web_v12_residual_round_R7_loop_73_L7_BIO_HEALTHCARE_MEDICAL_C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION_research.md
production_scoring_changed = false
shadow_weight_only = true
handoff_prompt_embedded = true
handoff_prompt_executed_now = false
```

This loop adds 4 new independent cases, 2 counterexamples, and 3 residual errors for R7/L7_BIO_HEALTHCARE_MEDICAL/C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION.

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

Applied global axes are treated as already active. This MD does not re-propose them globally; it stress-tests their residual fit inside R7/C23.

## 2. Round / Large Sector / Canonical Archetype Scope

```text
round = R7
loop = 73
round_sector_consistency = pass
allowed_large_sector_for_R7 = L7_BIO_HEALTHCARE_MEDICAL
selected_large_sector_id = L7_BIO_HEALTHCARE_MEDICAL
selected_canonical_archetype_id = C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION
```

R7 is a direct sector round, not an R13 cross-archetype checkpoint. C23 was selected because regulatory approval / commercialization cases often look deceptively simple: approval headlines can be real demand bridges, or merely a flash bulb that burns out before earnings conversion. The residual rule is not “approval is good”; it is “approval plus commercial conversion is good.”

## 3. Previous Coverage / Duplicate Avoidance Check

Search against accessible research artifacts did not return a matching R7 loop 73 C23 output. This run therefore uses the previous chat state `R6 Loop 73 -> next_round=R7 / next_loop=73`.

Duplicate key policy:

```text
hard_duplicate_key = canonical_archetype_id + symbol + trigger_type + entry_date
duplicate_key_conflict_count = 0
new_independent_case_count = 4
reused_case_count = 0
new_symbol_count = 4
same_archetype_new_symbol_count = 4
same_archetype_new_trigger_family_count = 4
```

## 4. Stock-Web OHLC Input / Price Source Validation

Manifest validation:

```text
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
markets = ['KONEX', 'KOSDAQ', 'KOSDAQ GLOBAL', 'KOSPI']
calibration_shard_root = atlas/ohlcv_tradable_by_symbol_year
raw_shard_root = atlas/ohlcv_raw_by_symbol_year
schema_path = atlas/schema.json
universe_path = atlas/universe/all_symbols.csv
```

Schema validation:

```text
tradable columns = d,o,h,l,c,v,a,mc,s,m
raw columns = d,o,h,l,c,v,a,mc,s,m,rs
MFE_N_pct = (max high from entry_date through N tradable rows / entry_price - 1) * 100
MAE_N_pct = (min low from entry_date through N tradable rows / entry_price - 1) * 100
calibration_basis = tradable_raw
```

## 5. Historical Eligibility Gate

All four representative calibration cases satisfy the 180D eligibility gate:

```text
trigger_date_is_historical = true
entry_date_exists_in_stock_web_tradable_shard = true
forward_180D_available_by_manifest_max_date = true
price_fields_present = true
MFE_MAE_30_90_180D_computed = true
corporate_action_contaminated_180D_window = false
```

Profile caveats:

| symbol | profile path | profile summary | 180D corporate action status |
|---:|---|---|---|
| 196170 | atlas/symbol_profiles/196/196170.json | first_date=2014-12-12; last_date=2026-02-20; trading_day_count=2745; corporate_action_candidate_dates=[2017-12-07,2017-12-28,2020-07-23,2020-08-13,2021-04-12]; no 2024 180D overlap. | clean_180D_window |
| 145020 | atlas/symbol_profiles/145/145020.json | first_date=2015-12-24; last_date=2026-02-20; trading_day_count=2489; corporate_action_candidate_dates=[2017-07-31,2020-07-08,2020-07-31]; no 2024 180D overlap. | clean_180D_window |
| 302440 | atlas/symbol_profiles/302/302440.json | first_date=2021-03-18; last_date=2026-02-20; trading_day_count=1208; corporate_action_candidate_count=0. | clean_180D_window |
| 028300 | atlas/symbol_profiles/028/028300.json | first_date=1996-09-02; last_date=2026-02-20; trading_day_count=7065; corporate action candidates end at 2021-04-01; no 2024 180D overlap. | clean_180D_window |

## 6. Canonical Archetype Compression Map

```text
canonical_archetype_id = C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION
fine_archetype_id = BIO_APPROVAL_COMMERCIALIZATION_BINARY_EVENT_GUARD
compressed_fine_paths =
  - platform_or_partner_commercialization_route
  - regulatory_approval_with_launch_or_channel_conversion
  - approval_headline_without_demand_conversion
  - pre_approval_binary_event_risk
  - hard_4c_regulatory_non_approval
```

C23 should not split into endless small labels. The useful compression is evidence quality, not product modality: approval / partner route / channel conversion / demand conversion / binary-event failure.

## 7. Case Selection Summary

| case_id | symbol | company | role | trigger | entry | MFE90 | MAE90 | MFE180 | MAE180 | verdict |
|---|---:|---|---|---|---|---:|---:|---:|---:|---|
| R7L73_C23_ALT_196170_20240223 | 196170 | 알테오젠 | positive | Stage2-Actionable 2024-02-22 | 2024-02-23 @ 131,200 | 127.52 | -9.3 | 247.18 | -9.3 | current_profile_correct |
| R7L73_C23_HUGEL_145020_20240304 | 145020 | 휴젤 | positive | Stage2-Actionable 2024-02-29 | 2024-03-04 @ 202,500 | 29.63 | -14.91 | 60.99 | -14.91 | current_profile_too_late |
| R7L73_C23_SKBIO_302440_20220629 | 302440 | SK바이오사이언스 | counterexample | Stage2-ApprovalHeadline 2022-06-29 | 2022-06-29 @ 109,000 | 43.58 | -38.17 | 43.58 | -40.18 | current_profile_false_positive |
| R7L73_C23_HLB_028300_20240422 | 028300 | HLB | counterexample | Stage2-PreApprovalBinaryEvent 2024-04-22 | 2024-04-22 @ 106,300 | 7.53 | -55.79 | 7.53 | -55.79 | current_profile_false_positive |

## 8. Positive vs Counterexample Balance

```text
positive_case_count = 2
counterexample_count = 2
4B_case_count = 3
4C_case_count = 1
calibration_usable_case_count = 4
calibration_usable_representative_trigger_count = 4
calibration_usable_total_trigger_count = 8
```

Balance logic:

- Positive: ALT/Alteogen and Hugel show approval/commercialization evidence that can survive beyond a one-day headline.
- Counterexample: SK Bioscience and HLB show why approval-only or pre-approval binary events need a canonical guard. One had an approval spike but poor demand conversion; the other had hard regulatory non-approval.

## 9. Evidence Source Map

| case | event evidence | source confidence | source URLs |
|---|---|---|---|
| R7L73_C23_ALT_196170_20240223 | ALT-B4/SC formulation commercialization route repricing after public partner-route licensing amendment; follow-on Merck/Keytruda SC disclosure context later reinforced route. | medium_high | https://www.reuters.com/business/healthcare-pharmaceuticals/merck-says-keytruda-injection-par-with-approved-iv-version-trial-2024-11-19/; https://www.reuters.com/business/healthcare-pharmaceuticals/merck-plans-us-launch-subcutaneous-version-keytruda-october-1-2025-03-27/ |
| R7L73_C23_HUGEL_145020_20240304 | U.S. approval/commercialization route for letibotulinumtoxinA/Letybo; approval headline had clearer commercial channel than generic binary biotech approval. | medium_high | https://www.allure.com/story/letybo-neuromodulator-injectable; https://en.wikipedia.org/wiki/Botulinum_toxin |
| R7L73_C23_SKBIO_302440_20220629 | Domestic COVID vaccine approval created a fast approval-headline spike, but demand conversion/reorder visibility later failed; 180D path had severe MAE and drawdown. | medium | https://en.wikipedia.org/wiki/Skycovione |
| R7L73_C23_HLB_028300_20240422 | Pre-PDUFA/regulatory approval expectation priced before decision; FDA Complete Response Letter then triggered hard thesis-break path. | medium | public regulatory/news flow; later source normalization required |

## 10. Price Data Source Map

| symbol | shard | entry_date | entry_price | price_basis |
|---:|---|---|---:|---|
| 196170 | atlas/ohlcv_tradable_by_symbol_year/196/196170/2024.csv | 2024-02-23 | 131200 | tradable_raw |
| 145020 | atlas/ohlcv_tradable_by_symbol_year/145/145020/2024.csv | 2024-03-04 | 202500 | tradable_raw |
| 302440 | atlas/ohlcv_tradable_by_symbol_year/302/302440/2022.csv | 2022-06-29 | 109000 | tradable_raw |
| 028300 | atlas/ohlcv_tradable_by_symbol_year/028/028300/2024.csv | 2024-04-22 | 106300 | tradable_raw |

## 11. Case-by-Case Trigger Grid

| trigger_id | type | evidence split | entry | current verdict | aggregate_role |
|---|---|---|---|---|---|
| TRG_R7L73_ALT_20240223_S2A | Stage2-Actionable | S2=public_event_or_disclosure,customer_or_order_quality,relative_strength,policy_or_regulatory_optionality / S3=durable_customer_confirmation,multiple_public_sources,financial_visibility / 4B=valuation_blowoff,positioning_overheat,price_only_local_peak / 4C=- | 2024-02-23 @ 131200 | current_profile_correct | representative |
| TRG_R7L73_ALT_20240223_4B | Stage4B-Overlay | S2=- / S3=- / 4B=valuation_blowoff,positioning_overheat,price_only_local_peak / 4C=- | 2024-11-11 @ 445500 | current_profile_correct | 4B_overlay_only |
| TRG_R7L73_HUGEL_20240304_S2A | Stage2-Actionable | S2=public_event_or_disclosure,policy_or_regulatory_optionality,capacity_or_volume_route / S3=repeat_order_or_conversion,financial_visibility,multiple_public_sources,low_red_team_risk / 4B=valuation_blowoff,price_only_local_peak / 4C=- | 2024-03-04 @ 202500 | current_profile_too_late | representative |
| TRG_R7L73_HUGEL_20240304_4B | Stage4B-Overlay | S2=- / S3=- / 4B=valuation_blowoff,price_only_local_peak / 4C=- | 2024-11-06 @ 321000 | current_profile_correct | 4B_overlay_only |
| TRG_R7L73_SKBIO_20220629_APPROVAL | Stage2-ApprovalHeadline | S2=public_event_or_disclosure,policy_or_regulatory_optionality,relative_strength / S3=- / 4B=valuation_blowoff,positioning_overheat,margin_or_backlog_slowdown / 4C=call_off_or_order_cut,thesis_evidence_broken | 2022-06-29 @ 109000 | current_profile_false_positive | representative |
| TRG_R7L73_SKBIO_20220629_4B | Stage4B-Overlay | S2=- / S3=- / 4B=valuation_blowoff,positioning_overheat,margin_or_backlog_slowdown / 4C=- | 2022-07-14 @ 150000 | current_profile_correct | 4B_overlay_only |
| TRG_R7L73_HLB_20240422_PREPDUFA | Stage2-PreApprovalBinaryEvent | S2=public_event_or_disclosure,relative_strength,policy_or_regulatory_optionality / S3=- / 4B=positioning_overheat,explicit_event_cap / 4C=regulatory_rejection,thesis_evidence_broken | 2024-04-22 @ 106300 | current_profile_false_positive | representative |
| TRG_R7L73_HLB_20240517_4C | Stage4C-HardThesisBreak | S2=- / S3=- / 4B=explicit_event_cap / 4C=regulatory_rejection,thesis_evidence_broken | 2024-05-17 @ 67100 | current_profile_correct | 4C_overlay_only |

## 12. Trigger-Level OHLC Backtest Tables

Representative trigger backtest:

| trigger_id | entry_price | MFE30 | MAE30 | MFE90 | MAE90 | MFE180 | MAE180 | peak_date | peak_price | drawdown_after_peak | usable |
|---|---:|---:|---:|---:|---:|---:|---:|---|---:|---:|---|
| TRG_R7L73_ALT_20240223_S2A | 131,200 | 71.88 | -9.3 | 127.52 | -9.3 | 247.18 | -9.3 | 2024-11-11 | 455,500 | -38.75 | true |
| TRG_R7L73_HUGEL_20240304_S2A | 202,500 | 8.15 | -14.91 | 29.63 | -14.91 | 60.99 | -14.91 | 2024-11-07 | 326,000 | -27.3 | true |
| TRG_R7L73_SKBIO_20220629_APPROVAL | 109,000 | 43.58 | -11.65 | 43.58 | -38.17 | 43.58 | -40.18 | 2022-07-13 | 156,500 | -58.34 | true |
| TRG_R7L73_HLB_20240422_PREPDUFA | 106,300 | 7.53 | -55.79 | 7.53 | -55.79 | 7.53 | -55.79 | 2024-04-30 | 114,300 | -58.88 | true |

Computed metrics use actual stock-web 1D OHLC rows fetched from tradable shards. 1Y/2Y fields are included in machine rows as null because this loop’s quantitative gate is clean 180D calibration; 1Y/2Y were not used for weight proposal.

## 13. Current Calibrated Profile Stress Test

### ALT / 196170

The current profile correctly rewards non-price commercialization evidence, but it should treat the November local peak as 4B watch only. Price-only local peak proximity is 0.969, yet full 4B remains blocked without non-price thesis deterioration. Existing axis status: `existing_axis_kept`.

### Hugel / 145020

The current profile is too late if it waits for financial confirmation rather than recognizing U.S. approval plus launch/channel conversion. Green lateness ratio is 0.316. Existing axis status: `existing_axis_kept`; new C23 route bonus proposed.

### SK Bioscience / 302440

The current profile is vulnerable to a false positive or high-MAE success if it treats domestic approval as enough. The case had MFE30 +43.58%, but 180D MAE -40.18% and post-peak drawdown -58.34%. Existing axis status: `existing_axis_strengthened` for price-only blowoff / 4B guard.

### HLB / 028300

The current profile is false-positive if pre-PDUFA expectation can cross Yellow/Green without actual approval. Hard 4C routing is correct after CRL/non-approval. Existing axis status: `existing_axis_strengthened`.

## 14. Stage2 / Yellow / Green Comparison

| case | Stage2/Actionable entry | Stage3 Green proxy | green_lateness_ratio | interpretation |
|---|---:|---:|---:|---|
| ALT | 131,200 | 269,000 | 0.425 | Green is later but still before full-window peak; Stage2-Actionable matters |
| Hugel | 202,500 | 242,000 | 0.316 | Green is modestly late; commercial-route bonus helps |
| SKBIO | 109,000 | n/a | n/a | no clean durable Green; approval spike lacks demand conversion |
| HLB | 106,300 | n/a | n/a | binary event should stay watch until decision |

The loop does not re-prove global Stage2 > Green. It adds a C23-specific distinction: `approval headline` is not equal to `commercialization route`.

## 15. 4B Local vs Full-window Timing Audit

| case | 4B date | 4B entry | local proximity | full-window proximity | verdict |
|---|---|---:|---:|---:|---|
| ALT | 2024-11-11 | 445,500 | 0.969 | 0.969 | price-only local 4B watch; not full 4B without non-price evidence |
| Hugel | 2024-11-06 | 321,000 | 0.960 | 0.960 | price-only local 4B watch; not full 4B without non-price evidence |
| SKBIO | 2022-07-14 | 150,000 | 0.863 | 0.863 | strong local 4B watch; later demand failure validates guard |
| HLB | n/a | n/a | n/a | n/a | hard 4C, not 4B, is the important route |

## 16. 4C Protection Audit

HLB is the main 4C row:

```text
4C trigger = TRG_R7L73_HLB_20240517_4C
entry_price_after_4C = 67,100
MFE_90D_after_4C = 46.20
MAE_90D_after_4C = -32.71
label = hard_4c_success
```

The 4C row is not used to train positive entry weights. It proves that regulatory non-approval must override earlier Stage2/Stage3 candidate states.

## 17. Sector-Specific Rule Candidate

```text
rule_scope = sector_specific
large_sector_id = L7_BIO_HEALTHCARE_MEDICAL
candidate_rule = approval headline in bio/healthcare only upgrades when commercial conversion route is visible
```

Proposed guardrail:

```text
if large_sector_id == L7_BIO_HEALTHCARE_MEDICAL
and canonical_archetype_id == C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION
and evidence_family == approval_headline_only
and no demand_conversion/reorder/reimbursement/launch_channel/margin_bridge:
    cap_positive_stage = Stage2-Watch or Stage3-Yellow max
```

## 18. Canonical-Archetype Rule Candidate

```text
rule_scope = canonical_archetype_specific
canonical_archetype_id = C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION
candidate_axis_1 = c23_partner_or_launch_commercialization_route_bonus
candidate_axis_2 = c23_pre_approval_binary_event_cap
candidate_axis_3 = c23_approval_without_demand_conversion_guard
candidate_axis_4 = c23_price_only_local_4b_watch_overlay
```

C23 behaves like a lock with two tumblers. The first tumbler is approval or partner route. The second is conversion into real commercial path. If only one turns, the door should not open to Green.

## 19. Before / After Backtest Comparison

| profile_id | scope | selected entries | avg MFE90 | avg MAE90 | avg MFE180 | avg MAE180 | false_positive_rate | verdict |
|---|---|---:|---:|---:|---:|---:|---:|---|
| P0 e2r_2_1_stock_web_calibrated_proxy | current | 4 | 52.06 | -29.54 | 89.82 | -30.05 | 50% | current profile still over-credits pre-approval/approval-only paths |
| P0b e2r_2_0_baseline_reference | rollback | 4 | 52.06 | -29.54 | 89.82 | -30.05 | 50%+ | weaker guard; not preferred |
| P1 sector_specific_candidate_profile | L7 sector | 3 | 60.91 | -21.13 | 117.25 | -21.13 | 33% | better but still admits SKBIO high-MAE approval spike |
| P2 canonical_archetype_candidate_profile | C23 | 2 | 78.58 | -12.11 | 154.09 | -12.11 | 0% | best score-return alignment in this loop |
| P3 counterexample_guard_profile | C23 guard | 2 positives + 2 blocked/watch | 78.58 | -12.11 | 154.09 | -12.11 | 0% | recommended shadow-only ledger candidate |


## 20. Score-Return Alignment Matrix

| case | before score/stage | after score/stage | MFE90/MAE90 | alignment |
|---|---|---|---|---|
| R7L73_C23_ALT_196170_20240223 | 86.0 / Stage3-Yellow | 89.0 / Stage3-Green | 127.52 / -9.3 | aligned after C23 route bonus |
| R7L73_C23_HUGEL_145020_20240304 | 83.0 / Stage3-Yellow | 87.5 / Stage3-Green | 29.63 / -14.91 | aligned after C23 route bonus |
| R7L73_C23_SKBIO_302440_20220629 | 78.0 / Stage3-Yellow | 68.0 / Stage2-Watch | 43.58 / -38.17 | blocked/guarded after C23 counterexample rule |
| R7L73_C23_HLB_028300_20240422 | 76.0 / Stage3-Yellow | 62.0 / Stage2-Watch_until_decision_or_4C_after_CRL | 7.53 / -55.79 | blocked/guarded after C23 counterexample rule |

## 21. Coverage Matrix

| large_sector_id | canonical_archetype_id | fine_archetype_id | positive_case_count | counterexample_count | 4B_case_count | 4C_case_count | new_independent_case_count | reused_case_count | calibration_usable_trigger_count | representative_trigger_count | current_profile_error_count | sector_rule_candidate | canonical_rule_candidate | coverage_gap_after_this_loop |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|---|---|
| L7_BIO_HEALTHCARE_MEDICAL | C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION | BIO_APPROVAL_COMMERCIALIZATION_BINARY_EVENT_GUARD | 2 | 2 | 3 | 1 | 4 | 0 | 8 | 4 | 3 | true | true | positive/counterexample balance improved; needs more pure C25 medical-device holdout later |

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
  - stage3_yellow_total_min
  - stage3_green_total_min
  - price_only_blowoff_blocks_positive_stage
  - full_4b_requires_non_price_evidence
  - hard_4c_thesis_break_routes_to_4c
residual_error_types_found:
  - approval_headline_false_positive
  - pre_approval_binary_event_green_risk
  - high_mae_approval_spike
  - price_only_local_4b_too_early
new_axis_proposed:
  - c23_partner_or_launch_commercialization_route_bonus
  - c23_pre_approval_binary_event_cap
  - c23_approval_without_demand_conversion_guard
  - c23_price_only_local_4b_watch_overlay
existing_axis_strengthened:
  - price_only_blowoff_blocks_positive_stage
  - full_4b_requires_non_price_evidence
  - hard_4c_thesis_break_routes_to_4c
existing_axis_weakened: null
existing_axis_kept:
  - stage2_actionable_evidence_bonus
  - stage3_yellow_total_min
  - stage3_green_total_min
sector_specific_rule_candidate: true
canonical_archetype_rule_candidate: true
no_new_signal_reason: null
loop_contribution_label: canonical_archetype_rule_candidate
do_not_propose_new_weight_delta: false
```

## 23. Validation Scope / Non-Validation Scope

Validated:

```text
- actual stock-web tradable_raw 1D OHLC rows
- 30D/90D/180D MFE/MAE
- clean 180D corporate-action gate by profile candidate dates
- same_entry_group_id dedupe
- positive/counterexample balance
- 4B local vs full-window split
- 4C thesis-break label for HLB
```

Not validated:

```text
- production code implementation
- live/current candidate discovery
- broker/API/trading route
- 1Y/2Y weight calibration
- full external evidence-source normalization for every narrative note
```

## 24. Shadow Weight Calibration

```csv
row_type,axis,scope,large_sector_id,canonical_archetype_id,baseline_value,tested_value,delta,reason,backtest_effect,trigger_ids,calibration_usable_count,new_independent_case_count,counterexample_count,confidence,proposal_type,notes
shadow_weight,c23_partner_or_launch_commercialization_route_bonus,canonical_archetype_specific,L7_BIO_HEALTHCARE_MEDICAL,C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION,0,1.5,+1.5,"Positive cases require explicit partner/launch/commercial conversion, not just regulatory narrative.","Selected positives avg MFE90 78.58 / avg MAE90 -12.11 versus all reps avg MFE90 52.06 / avg MAE90 -29.54","TRG_R7L73_ALT_20240223_S2A|TRG_R7L73_HUGEL_20240304_S2A",4,4,2,medium,canonical_shadow_only,"not production; post-calibrated residual"
shadow_weight,c23_pre_approval_binary_event_cap,canonical_archetype_specific,L7_BIO_HEALTHCARE_MEDICAL,C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION,false,true,cap_to_watch,"Pre-PDUFA approval expectation has binary risk and must not cross Green without decision result.","HLB pre-approval representative had MFE90 7.53 and MAE90 -55.79 before hard 4C.","TRG_R7L73_HLB_20240422_PREPDUFA|TRG_R7L73_HLB_20240517_4C",4,4,2,medium,canonical_shadow_only,"strengthens existing hard_4c routing; no production change"
shadow_weight,c23_approval_without_demand_conversion_guard,sector_specific,L7_BIO_HEALTHCARE_MEDICAL,C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION,false,true,guard,"Approval headline must be paired with demand, reorder, reimbursement, launch conversion, or margin route.","SKBIO approval spike MFE30 43.58 but 180D MAE -40.18 and post-peak drawdown -58.34.","TRG_R7L73_SKBIO_20220629_APPROVAL",4,4,2,medium,sector_shadow_only,"not production; filters approval-headline traps"
shadow_weight,c23_price_only_local_4b_watch_overlay,canonical_archetype_specific,L7_BIO_HEALTHCARE_MEDICAL,C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION,false,true,overlay_only,"Local price peak proximity can mark watch overlay but cannot become full 4B without non-price evidence.","ALT/Hugel price-only 4B proximity near 0.96 but later thesis not necessarily broken.","TRG_R7L73_ALT_20240223_4B|TRG_R7L73_HUGEL_20240304_4B",4,4,2,low,canonical_shadow_only,"keeps existing full_4b_requires_non_price_evidence"
```

## 25. Machine-Readable Rows

### 25.1 price_source_validation

```jsonl
{"row_type":"price_source_validation","source":"Songdaiki/stock-web","source_url":"https://github.com/Songdaiki/stock-web","manifest_path":"atlas/manifest.json","schema_path":"atlas/schema.json","universe_path":"atlas/universe/all_symbols.csv","manifest_max_date":"2026-02-20","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","calibration_shard_root":"atlas/ohlcv_tradable_by_symbol_year","raw_shard_root":"atlas/ohlcv_raw_by_symbol_year","validation_status":"usable_for_historical_calibration"}
```

### 25.2 case rows

```jsonl
{"row_type":"case","case_id":"R7L73_C23_ALT_196170_20240223","symbol":"196170","company_name":"알테오젠","round":"R7","loop":"73","large_sector_id":"L7_BIO_HEALTHCARE_MEDICAL","canonical_archetype_id":"C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION","fine_archetype_id":"BIO_APPROVAL_COMMERCIALIZATION_BINARY_EVENT_GUARD","case_type":"structural_success","positive_or_counterexample":"positive","best_trigger":"TRG_R7L73_ALT_20240223_S2A","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"aligned","current_profile_verdict":"current_profile_correct","price_source":"Songdaiki/stock-web","notes":"ALT-B4/SC formulation commercialization route repricing after public partner-route licensing amendment; follow-on Merck/Keytruda SC disclosure context later reinforced route."}
{"row_type":"case","case_id":"R7L73_C23_HUGEL_145020_20240304","symbol":"145020","company_name":"휴젤","round":"R7","loop":"73","large_sector_id":"L7_BIO_HEALTHCARE_MEDICAL","canonical_archetype_id":"C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION","fine_archetype_id":"BIO_APPROVAL_COMMERCIALIZATION_BINARY_EVENT_GUARD","case_type":"structural_success","positive_or_counterexample":"positive","best_trigger":"TRG_R7L73_HUGEL_20240304_S2A","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"aligned","current_profile_verdict":"current_profile_too_late","price_source":"Songdaiki/stock-web","notes":"U.S. approval/commercialization route for letibotulinumtoxinA/Letybo; approval headline had clearer commercial channel than generic binary biotech approval."}
{"row_type":"case","case_id":"R7L73_C23_SKBIO_302440_20220629","symbol":"302440","company_name":"SK바이오사이언스","round":"R7","loop":"73","large_sector_id":"L7_BIO_HEALTHCARE_MEDICAL","canonical_archetype_id":"C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION","fine_archetype_id":"BIO_APPROVAL_COMMERCIALIZATION_BINARY_EVENT_GUARD","case_type":"high_mae_success_failed_rerating","positive_or_counterexample":"counterexample","best_trigger":"TRG_R7L73_SKBIO_20220629_APPROVAL","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"misaligned_or_high_mae","current_profile_verdict":"current_profile_false_positive","price_source":"Songdaiki/stock-web","notes":"Domestic COVID vaccine approval created a fast approval-headline spike, but demand conversion/reorder visibility later failed; 180D path had severe MAE and drawdown."}
{"row_type":"case","case_id":"R7L73_C23_HLB_028300_20240422","symbol":"028300","company_name":"HLB","round":"R7","loop":"73","large_sector_id":"L7_BIO_HEALTHCARE_MEDICAL","canonical_archetype_id":"C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION","fine_archetype_id":"BIO_APPROVAL_COMMERCIALIZATION_BINARY_EVENT_GUARD","case_type":"false_positive_green_4c_success","positive_or_counterexample":"counterexample","best_trigger":"TRG_R7L73_HLB_20240422_PREPDUFA","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"misaligned_or_high_mae","current_profile_verdict":"current_profile_false_positive","price_source":"Songdaiki/stock-web","notes":"Pre-PDUFA/regulatory approval expectation priced before decision; FDA Complete Response Letter then triggered hard thesis-break path."}
```

### 25.3 trigger rows

```jsonl
{"row_type":"trigger","trigger_id":"TRG_R7L73_ALT_20240223_S2A","case_id":"R7L73_C23_ALT_196170_20240223","symbol":"196170","company_name":"알테오젠","round":"R7","loop":"73","large_sector_id":"L7_BIO_HEALTHCARE_MEDICAL","canonical_archetype_id":"C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION","fine_archetype_id":"BIO_APPROVAL_COMMERCIALIZATION_BINARY_EVENT_GUARD","sector":"bio_healthcare_medical","primary_archetype":"regulatory_approval_to_commercialization","loop_objective":"sector_specific_rule_discovery|canonical_archetype_compression|counterexample_mining","trigger_type":"Stage2-Actionable","trigger_date":"2024-02-22","entry_date":"2024-02-23","entry_price":131200,"evidence_available_at_that_date":"ALT-B4/SC formulation commercialization route repricing after public partner-route licensing amendment; follow-on Merck/Keytruda SC disclosure context later reinforced route.","evidence_source":"public company/disclosure/news flow; Reuters later confirmed Merck's SC Keytruda uses an Alteogen-developed enzyme.","stage2_evidence_fields":["public_event_or_disclosure","customer_or_order_quality","relative_strength","policy_or_regulatory_optionality"],"stage3_evidence_fields":["durable_customer_confirmation","multiple_public_sources","financial_visibility"],"stage4b_evidence_fields":["valuation_blowoff","positioning_overheat","price_only_local_peak"],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/196/196170/2024.csv","profile_path":"atlas/symbol_profiles/196/196170.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":71.88,"MFE_90D_pct":127.52,"MFE_180D_pct":247.18,"MFE_1Y_pct":null,"MFE_2Y_pct":null,"MAE_30D_pct":-9.3,"MAE_90D_pct":-9.3,"MAE_180D_pct":-9.3,"MAE_1Y_pct":null,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-11-11","peak_price":455500,"drawdown_after_peak_pct":-38.75,"green_lateness_ratio":0.425,"four_b_local_peak_proximity":0.969,"four_b_full_window_peak_proximity":0.969,"four_b_timing_verdict":"price_only_local_4B_too_early","four_b_evidence_type":["price_only","valuation_blowoff","positioning_overheat"],"four_c_protection_label":null,"trigger_outcome_label":"structural_success","current_profile_verdict":"current_profile_correct","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"R7L73_C23_ALT_196170_20240223|2024-02-23","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"TRG_R7L73_ALT_20240223_4B","case_id":"R7L73_C23_ALT_196170_20240223","symbol":"196170","company_name":"알테오젠","round":"R7","loop":"73","large_sector_id":"L7_BIO_HEALTHCARE_MEDICAL","canonical_archetype_id":"C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION","fine_archetype_id":"BIO_APPROVAL_COMMERCIALIZATION_BINARY_EVENT_GUARD","sector":"bio_healthcare_medical","primary_archetype":"regulatory_approval_to_commercialization","loop_objective":"4B_non_price_requirement_stress_test","trigger_type":"Stage4B-Overlay","trigger_date":"2024-11-11","entry_date":"2024-11-11","entry_price":445500,"evidence_available_at_that_date":"price/valuation local peak only; no non-price thesis-break evidence","evidence_source":"stock-web OHLC path plus narrative valuation/positioning overlay","stage2_evidence_fields":[],"stage3_evidence_fields":[],"stage4b_evidence_fields":["valuation_blowoff","positioning_overheat","price_only_local_peak"],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/196/196170/2024.csv","profile_path":"atlas/symbol_profiles/196/196170.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":null,"MFE_90D_pct":null,"MFE_180D_pct":null,"MFE_1Y_pct":null,"MFE_2Y_pct":null,"MAE_30D_pct":null,"MAE_90D_pct":null,"MAE_180D_pct":null,"MAE_1Y_pct":null,"below_entry_price_flag_30D":null,"below_entry_price_flag_90D":null,"peak_date":"2024-11-11","peak_price":455500,"drawdown_after_peak_pct":-38.75,"green_lateness_ratio":0.425,"four_b_local_peak_proximity":0.969,"four_b_full_window_peak_proximity":0.969,"four_b_timing_verdict":"price_only_local_4B_too_early","four_b_evidence_type":["price_only","valuation_blowoff","positioning_overheat"],"four_c_protection_label":null,"trigger_outcome_label":"4B_overlay_only","current_profile_verdict":"current_profile_correct","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"R7L73_C23_ALT_196170_20240223|2024-02-23","dedupe_for_aggregate":false,"aggregate_group_role":"4B_overlay_only","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":0.25,"do_not_count_as_new_case":true}
{"row_type":"trigger","trigger_id":"TRG_R7L73_HUGEL_20240304_S2A","case_id":"R7L73_C23_HUGEL_145020_20240304","symbol":"145020","company_name":"휴젤","round":"R7","loop":"73","large_sector_id":"L7_BIO_HEALTHCARE_MEDICAL","canonical_archetype_id":"C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION","fine_archetype_id":"BIO_APPROVAL_COMMERCIALIZATION_BINARY_EVENT_GUARD","sector":"bio_healthcare_medical","primary_archetype":"regulatory_approval_to_commercialization","loop_objective":"sector_specific_rule_discovery|canonical_archetype_compression|counterexample_mining","trigger_type":"Stage2-Actionable","trigger_date":"2024-02-29","entry_date":"2024-03-04","entry_price":202500,"evidence_available_at_that_date":"U.S. approval/commercialization route for letibotulinumtoxinA/Letybo; approval headline had clearer commercial channel than generic binary biotech approval.","evidence_source":"FDA approval/news summaries for Letybo; public launch/US availability reports.","stage2_evidence_fields":["public_event_or_disclosure","policy_or_regulatory_optionality","capacity_or_volume_route"],"stage3_evidence_fields":["repeat_order_or_conversion","financial_visibility","multiple_public_sources","low_red_team_risk"],"stage4b_evidence_fields":["valuation_blowoff","price_only_local_peak"],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/145/145020/2024.csv","profile_path":"atlas/symbol_profiles/145/145020.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":8.15,"MFE_90D_pct":29.63,"MFE_180D_pct":60.99,"MFE_1Y_pct":null,"MFE_2Y_pct":null,"MAE_30D_pct":-14.91,"MAE_90D_pct":-14.91,"MAE_180D_pct":-14.91,"MAE_1Y_pct":null,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-11-07","peak_price":326000,"drawdown_after_peak_pct":-27.3,"green_lateness_ratio":0.32,"four_b_local_peak_proximity":0.96,"four_b_full_window_peak_proximity":0.96,"four_b_timing_verdict":"price_only_local_4B_too_early","four_b_evidence_type":["price_only","valuation_blowoff"],"four_c_protection_label":null,"trigger_outcome_label":"structural_success","current_profile_verdict":"current_profile_too_late","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"R7L73_C23_HUGEL_145020_20240304|2024-03-04","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"TRG_R7L73_HUGEL_20240304_4B","case_id":"R7L73_C23_HUGEL_145020_20240304","symbol":"145020","company_name":"휴젤","round":"R7","loop":"73","large_sector_id":"L7_BIO_HEALTHCARE_MEDICAL","canonical_archetype_id":"C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION","fine_archetype_id":"BIO_APPROVAL_COMMERCIALIZATION_BINARY_EVENT_GUARD","sector":"bio_healthcare_medical","primary_archetype":"regulatory_approval_to_commercialization","loop_objective":"4B_non_price_requirement_stress_test","trigger_type":"Stage4B-Overlay","trigger_date":"2024-11-06","entry_date":"2024-11-06","entry_price":321000,"evidence_available_at_that_date":"price/valuation local peak only; no non-price thesis-break evidence","evidence_source":"stock-web OHLC path plus narrative valuation/positioning overlay","stage2_evidence_fields":[],"stage3_evidence_fields":[],"stage4b_evidence_fields":["valuation_blowoff","price_only_local_peak"],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/145/145020/2024.csv","profile_path":"atlas/symbol_profiles/145/145020.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":null,"MFE_90D_pct":null,"MFE_180D_pct":null,"MFE_1Y_pct":null,"MFE_2Y_pct":null,"MAE_30D_pct":null,"MAE_90D_pct":null,"MAE_180D_pct":null,"MAE_1Y_pct":null,"below_entry_price_flag_30D":null,"below_entry_price_flag_90D":null,"peak_date":"2024-11-07","peak_price":326000,"drawdown_after_peak_pct":-27.3,"green_lateness_ratio":0.32,"four_b_local_peak_proximity":0.96,"four_b_full_window_peak_proximity":0.96,"four_b_timing_verdict":"price_only_local_4B_too_early","four_b_evidence_type":["price_only","valuation_blowoff"],"four_c_protection_label":null,"trigger_outcome_label":"4B_overlay_only","current_profile_verdict":"current_profile_correct","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"R7L73_C23_HUGEL_145020_20240304|2024-03-04","dedupe_for_aggregate":false,"aggregate_group_role":"4B_overlay_only","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":0.25,"do_not_count_as_new_case":true}
{"row_type":"trigger","trigger_id":"TRG_R7L73_SKBIO_20220629_APPROVAL","case_id":"R7L73_C23_SKBIO_302440_20220629","symbol":"302440","company_name":"SK바이오사이언스","round":"R7","loop":"73","large_sector_id":"L7_BIO_HEALTHCARE_MEDICAL","canonical_archetype_id":"C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION","fine_archetype_id":"BIO_APPROVAL_COMMERCIALIZATION_BINARY_EVENT_GUARD","sector":"bio_healthcare_medical","primary_archetype":"regulatory_approval_to_commercialization","loop_objective":"sector_specific_rule_discovery|canonical_archetype_compression|counterexample_mining","trigger_type":"Stage2-ApprovalHeadline","trigger_date":"2022-06-29","entry_date":"2022-06-29","entry_price":109000,"evidence_available_at_that_date":"Domestic COVID vaccine approval created a fast approval-headline spike, but demand conversion/reorder visibility later failed; 180D path had severe MAE and drawdown.","evidence_source":"MFDS/SK bioscience approval news; later public reports discussed low demand and production suspension.","stage2_evidence_fields":["public_event_or_disclosure","policy_or_regulatory_optionality","relative_strength"],"stage3_evidence_fields":[],"stage4b_evidence_fields":["valuation_blowoff","positioning_overheat","margin_or_backlog_slowdown"],"stage4c_evidence_fields":["call_off_or_order_cut","thesis_evidence_broken"],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/302/302440/2022.csv","profile_path":"atlas/symbol_profiles/302/302440.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":43.58,"MFE_90D_pct":43.58,"MFE_180D_pct":43.58,"MFE_1Y_pct":null,"MFE_2Y_pct":null,"MAE_30D_pct":-11.65,"MAE_90D_pct":-38.17,"MAE_180D_pct":-40.18,"MAE_1Y_pct":null,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2022-07-13","peak_price":156500,"drawdown_after_peak_pct":-58.34,"green_lateness_ratio":null,"four_b_local_peak_proximity":0.863,"four_b_full_window_peak_proximity":0.863,"four_b_timing_verdict":"price_only_local_4B_too_early","four_b_evidence_type":["price_only","valuation_blowoff","positioning_overheat"],"four_c_protection_label":null,"trigger_outcome_label":"high_mae_success","current_profile_verdict":"current_profile_false_positive","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"R7L73_C23_SKBIO_302440_20220629|2022-06-29","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"TRG_R7L73_SKBIO_20220629_4B","case_id":"R7L73_C23_SKBIO_302440_20220629","symbol":"302440","company_name":"SK바이오사이언스","round":"R7","loop":"73","large_sector_id":"L7_BIO_HEALTHCARE_MEDICAL","canonical_archetype_id":"C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION","fine_archetype_id":"BIO_APPROVAL_COMMERCIALIZATION_BINARY_EVENT_GUARD","sector":"bio_healthcare_medical","primary_archetype":"regulatory_approval_to_commercialization","loop_objective":"4B_non_price_requirement_stress_test","trigger_type":"Stage4B-Overlay","trigger_date":"2022-07-14","entry_date":"2022-07-14","entry_price":150000,"evidence_available_at_that_date":"price/valuation local peak only; no non-price thesis-break evidence","evidence_source":"stock-web OHLC path plus narrative valuation/positioning overlay","stage2_evidence_fields":[],"stage3_evidence_fields":[],"stage4b_evidence_fields":["valuation_blowoff","positioning_overheat","margin_or_backlog_slowdown"],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/302/302440/2022.csv","profile_path":"atlas/symbol_profiles/302/302440.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":null,"MFE_90D_pct":null,"MFE_180D_pct":null,"MFE_1Y_pct":null,"MFE_2Y_pct":null,"MAE_30D_pct":null,"MAE_90D_pct":null,"MAE_180D_pct":null,"MAE_1Y_pct":null,"below_entry_price_flag_30D":null,"below_entry_price_flag_90D":null,"peak_date":"2022-07-13","peak_price":156500,"drawdown_after_peak_pct":-58.34,"green_lateness_ratio":null,"four_b_local_peak_proximity":0.863,"four_b_full_window_peak_proximity":0.863,"four_b_timing_verdict":"good_local_4B_watch_but_not_full_4B","four_b_evidence_type":["price_only","valuation_blowoff","positioning_overheat"],"four_c_protection_label":null,"trigger_outcome_label":"4B_overlay_only","current_profile_verdict":"current_profile_correct","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"R7L73_C23_SKBIO_302440_20220629|2022-06-29","dedupe_for_aggregate":false,"aggregate_group_role":"4B_overlay_only","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":0.25,"do_not_count_as_new_case":true}
{"row_type":"trigger","trigger_id":"TRG_R7L73_HLB_20240422_PREPDUFA","case_id":"R7L73_C23_HLB_028300_20240422","symbol":"028300","company_name":"HLB","round":"R7","loop":"73","large_sector_id":"L7_BIO_HEALTHCARE_MEDICAL","canonical_archetype_id":"C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION","fine_archetype_id":"BIO_APPROVAL_COMMERCIALIZATION_BINARY_EVENT_GUARD","sector":"bio_healthcare_medical","primary_archetype":"regulatory_approval_to_commercialization","loop_objective":"sector_specific_rule_discovery|canonical_archetype_compression|counterexample_mining","trigger_type":"Stage2-PreApprovalBinaryEvent","trigger_date":"2024-04-22","entry_date":"2024-04-22","entry_price":106300,"evidence_available_at_that_date":"Pre-PDUFA/regulatory approval expectation priced before decision; FDA Complete Response Letter then triggered hard thesis-break path.","evidence_source":"public regulatory-event/news flow around HLB/Elevar liver cancer application and May 2024 CRL; later source normalization required.","stage2_evidence_fields":["public_event_or_disclosure","relative_strength","policy_or_regulatory_optionality"],"stage3_evidence_fields":[],"stage4b_evidence_fields":["positioning_overheat","explicit_event_cap"],"stage4c_evidence_fields":["regulatory_rejection","thesis_evidence_broken"],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/028/028300/2024.csv","profile_path":"atlas/symbol_profiles/028/028300.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":7.53,"MFE_90D_pct":7.53,"MFE_180D_pct":7.53,"MFE_1Y_pct":null,"MFE_2Y_pct":null,"MAE_30D_pct":-55.79,"MAE_90D_pct":-55.79,"MAE_180D_pct":-55.79,"MAE_1Y_pct":null,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-04-30","peak_price":114300,"drawdown_after_peak_pct":-58.88,"green_lateness_ratio":null,"four_b_local_peak_proximity":null,"four_b_full_window_peak_proximity":null,"four_b_timing_verdict":null,"four_b_evidence_type":[],"four_c_protection_label":"hard_4c_success","trigger_outcome_label":"false_positive_green","current_profile_verdict":"current_profile_false_positive","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"R7L73_C23_HLB_028300_20240422|2024-04-22","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"TRG_R7L73_HLB_20240517_4C","case_id":"R7L73_C23_HLB_028300_20240422","symbol":"028300","company_name":"HLB","round":"R7","loop":"73","large_sector_id":"L7_BIO_HEALTHCARE_MEDICAL","canonical_archetype_id":"C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION","fine_archetype_id":"BIO_APPROVAL_COMMERCIALIZATION_BINARY_EVENT_GUARD","sector":"bio_healthcare_medical","primary_archetype":"regulatory_approval_to_commercialization","loop_objective":"4C_thesis_break_timing_test","trigger_type":"Stage4C-HardThesisBreak","trigger_date":"2024-05-17","entry_date":"2024-05-17","entry_price":67100,"evidence_available_at_that_date":"FDA complete response/regulatory non-approval event broke approval thesis.","evidence_source":"public regulatory-event/news flow around HLB/Elevar liver cancer application and May 2024 CRL; later source normalization required.","stage2_evidence_fields":[],"stage3_evidence_fields":[],"stage4b_evidence_fields":["explicit_event_cap"],"stage4c_evidence_fields":["regulatory_rejection","thesis_evidence_broken"],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/028/028300/2024.csv","profile_path":"atlas/symbol_profiles/028/028300.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":9.99,"MFE_90D_pct":46.2,"MFE_180D_pct":46.2,"MFE_1Y_pct":null,"MFE_2Y_pct":null,"MAE_30D_pct":-32.71,"MAE_90D_pct":-32.71,"MAE_180D_pct":-32.71,"MAE_1Y_pct":null,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-04-30","peak_price":114300,"drawdown_after_peak_pct":-58.88,"green_lateness_ratio":null,"four_b_local_peak_proximity":null,"four_b_full_window_peak_proximity":null,"four_b_timing_verdict":null,"four_b_evidence_type":[],"four_c_protection_label":"hard_4c_success","trigger_outcome_label":"4C_success","current_profile_verdict":"current_profile_correct","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"R7L73_C23_HLB_028300_20240422|2024-04-22","dedupe_for_aggregate":false,"aggregate_group_role":"4C_overlay_only","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":0.25,"do_not_count_as_new_case":true}
```

### 25.4 score_simulation rows

```jsonl
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy_to_C23_shadow","case_id":"R7L73_C23_ALT_196170_20240223","trigger_id":"TRG_R7L73_ALT_20240223_S2A","symbol":"196170","large_sector_id":"L7_BIO_HEALTHCARE_MEDICAL","canonical_archetype_id":"C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION","raw_component_scores_before":{"contract_score":8,"backlog_visibility_score":0,"margin_bridge_score":2,"revision_score":5,"relative_strength_score":9,"customer_quality_score":8,"policy_or_regulatory_score":6,"valuation_repricing_score":7,"execution_risk_score":3,"legal_or_contract_risk_score":2,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_before":86.0,"stage_label_before":"Stage3-Yellow","raw_component_scores_after":{"contract_score":9,"backlog_visibility_score":0,"margin_bridge_score":2,"revision_score":6,"relative_strength_score":9,"customer_quality_score":9,"policy_or_regulatory_score":7,"valuation_repricing_score":7,"execution_risk_score":3,"legal_or_contract_risk_score":2,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_after":89.0,"stage_label_after":"Stage3-Green","changed_components":["policy_or_regulatory_score","customer_quality_score","revision_score","relative_strength_score","execution_risk_score"],"component_delta_explanation":"C23 route bonus upgrades identified global-partner commercialization optionality; 4B remains overlay-only near peak.","MFE_90D_pct":127.52,"MAE_90D_pct":-9.3,"score_return_alignment_label":"aligned","current_profile_verdict":"current_profile_correct"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy_to_C23_shadow","case_id":"R7L73_C23_HUGEL_145020_20240304","trigger_id":"TRG_R7L73_HUGEL_20240304_S2A","symbol":"145020","large_sector_id":"L7_BIO_HEALTHCARE_MEDICAL","canonical_archetype_id":"C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION","raw_component_scores_before":{"contract_score":1,"backlog_visibility_score":0,"margin_bridge_score":4,"revision_score":6,"relative_strength_score":5,"customer_quality_score":6,"policy_or_regulatory_score":9,"valuation_repricing_score":5,"execution_risk_score":3,"legal_or_contract_risk_score":2,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_before":83.0,"stage_label_before":"Stage3-Yellow","raw_component_scores_after":{"contract_score":1,"backlog_visibility_score":0,"margin_bridge_score":5,"revision_score":7,"relative_strength_score":6,"customer_quality_score":7,"policy_or_regulatory_score":9,"valuation_repricing_score":5,"execution_risk_score":3,"legal_or_contract_risk_score":2,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_after":87.5,"stage_label_after":"Stage3-Green","changed_components":["policy_or_regulatory_score","customer_quality_score","revision_score","relative_strength_score","execution_risk_score"],"component_delta_explanation":"Approval is promoted only because launch/channel conversion is visible; pure approval headline without demand would not receive this uplift.","MFE_90D_pct":29.63,"MAE_90D_pct":-14.91,"score_return_alignment_label":"aligned","current_profile_verdict":"current_profile_too_late"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy_to_C23_shadow","case_id":"R7L73_C23_SKBIO_302440_20220629","trigger_id":"TRG_R7L73_SKBIO_20220629_APPROVAL","symbol":"302440","large_sector_id":"L7_BIO_HEALTHCARE_MEDICAL","canonical_archetype_id":"C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION","raw_component_scores_before":{"contract_score":1,"backlog_visibility_score":0,"margin_bridge_score":1,"revision_score":2,"relative_strength_score":8,"customer_quality_score":2,"policy_or_regulatory_score":8,"valuation_repricing_score":7,"execution_risk_score":7,"legal_or_contract_risk_score":2,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_before":78.0,"stage_label_before":"Stage3-Yellow","raw_component_scores_after":{"contract_score":1,"backlog_visibility_score":0,"margin_bridge_score":0,"revision_score":1,"relative_strength_score":5,"customer_quality_score":1,"policy_or_regulatory_score":8,"valuation_repricing_score":4,"execution_risk_score":9,"legal_or_contract_risk_score":2,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_after":68.0,"stage_label_after":"Stage2-Watch","changed_components":["policy_or_regulatory_score","customer_quality_score","revision_score","relative_strength_score","execution_risk_score"],"component_delta_explanation":"Approval-only spike is capped unless demand conversion, stockpile drawdown, reorder, or commercial margin route is visible.","MFE_90D_pct":43.58,"MAE_90D_pct":-38.17,"score_return_alignment_label":"counterexample_or_high_mae","current_profile_verdict":"current_profile_false_positive"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy_to_C23_shadow","case_id":"R7L73_C23_HLB_028300_20240422","trigger_id":"TRG_R7L73_HLB_20240422_PREPDUFA","symbol":"028300","large_sector_id":"L7_BIO_HEALTHCARE_MEDICAL","canonical_archetype_id":"C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION","raw_component_scores_before":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":0,"revision_score":1,"relative_strength_score":8,"customer_quality_score":2,"policy_or_regulatory_score":8,"valuation_repricing_score":8,"execution_risk_score":8,"legal_or_contract_risk_score":7,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_before":76.0,"stage_label_before":"Stage3-Yellow","raw_component_scores_after":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":0,"revision_score":0,"relative_strength_score":4,"customer_quality_score":1,"policy_or_regulatory_score":5,"valuation_repricing_score":3,"execution_risk_score":10,"legal_or_contract_risk_score":10,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_after":62.0,"stage_label_after":"Stage2-Watch_until_decision_or_4C_after_CRL","changed_components":["policy_or_regulatory_score","customer_quality_score","revision_score","relative_strength_score","execution_risk_score"],"component_delta_explanation":"Pre-approval binary events are not allowed to become Green without actual approval plus commercial conversion; CRL routes to hard 4C.","MFE_90D_pct":7.53,"MAE_90D_pct":-55.79,"score_return_alignment_label":"counterexample_or_high_mae","current_profile_verdict":"current_profile_false_positive"}
```

### 25.5 shadow_weight rows

```csv
row_type,axis,scope,large_sector_id,canonical_archetype_id,baseline_value,tested_value,delta,reason,backtest_effect,trigger_ids,calibration_usable_count,new_independent_case_count,counterexample_count,confidence,proposal_type,notes
shadow_weight,c23_partner_or_launch_commercialization_route_bonus,canonical_archetype_specific,L7_BIO_HEALTHCARE_MEDICAL,C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION,0,1.5,+1.5,"Positive cases require explicit partner/launch/commercial conversion, not just regulatory narrative.","Selected positives avg MFE90 78.58 / avg MAE90 -12.11 versus all reps avg MFE90 52.06 / avg MAE90 -29.54","TRG_R7L73_ALT_20240223_S2A|TRG_R7L73_HUGEL_20240304_S2A",4,4,2,medium,canonical_shadow_only,"not production; post-calibrated residual"
shadow_weight,c23_pre_approval_binary_event_cap,canonical_archetype_specific,L7_BIO_HEALTHCARE_MEDICAL,C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION,false,true,cap_to_watch,"Pre-PDUFA approval expectation has binary risk and must not cross Green without decision result.","HLB pre-approval representative had MFE90 7.53 and MAE90 -55.79 before hard 4C.","TRG_R7L73_HLB_20240422_PREPDUFA|TRG_R7L73_HLB_20240517_4C",4,4,2,medium,canonical_shadow_only,"strengthens existing hard_4c routing; no production change"
shadow_weight,c23_approval_without_demand_conversion_guard,sector_specific,L7_BIO_HEALTHCARE_MEDICAL,C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION,false,true,guard,"Approval headline must be paired with demand, reorder, reimbursement, launch conversion, or margin route.","SKBIO approval spike MFE30 43.58 but 180D MAE -40.18 and post-peak drawdown -58.34.","TRG_R7L73_SKBIO_20220629_APPROVAL",4,4,2,medium,sector_shadow_only,"not production; filters approval-headline traps"
shadow_weight,c23_price_only_local_4b_watch_overlay,canonical_archetype_specific,L7_BIO_HEALTHCARE_MEDICAL,C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION,false,true,overlay_only,"Local price peak proximity can mark watch overlay but cannot become full 4B without non-price evidence.","ALT/Hugel price-only 4B proximity near 0.96 but later thesis not necessarily broken.","TRG_R7L73_ALT_20240223_4B|TRG_R7L73_HUGEL_20240304_4B",4,4,2,low,canonical_shadow_only,"keeps existing full_4b_requires_non_price_evidence"
```

### 25.6 residual_contribution row

```jsonl
{"row_type":"residual_contribution","round":"R7","loop":"73","large_sector_id":"L7_BIO_HEALTHCARE_MEDICAL","canonical_archetype_id":"C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION","new_independent_case_count":4,"reused_case_count":0,"new_symbol_count":4,"new_trigger_family_count":4,"tested_existing_calibrated_axes":["stage2_actionable_evidence_bonus","stage3_yellow_total_min","stage3_green_total_min","price_only_blowoff_blocks_positive_stage","full_4b_requires_non_price_evidence","hard_4c_thesis_break_routes_to_4c"],"residual_error_types_found":["approval_headline_false_positive","pre_approval_binary_event_green_risk","high_mae_approval_spike","price_only_local_4b_too_early"],"loop_contribution_label":"canonical_archetype_rule_candidate","do_not_propose_new_weight_delta":false}
```

### 25.7 narrative_only rows

```jsonl
{"row_type":"narrative_only","case_id":"R7L73_C23_CELLTRION_068270_20231023","symbol":"068270","large_sector_id":"L7_BIO_HEALTHCARE_MEDICAL","canonical_archetype_id":"C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION","reason":"candidate positive regulatory approval case rejected for quantitative weight calibration because symbol profile has corporate_action_candidate_date 2024-01-12 inside the 180D forward window from 2023-10-23","price_source":"Songdaiki/stock-web","usage":"not_weight_calibration"}
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
completed_round = R7
completed_loop = 73
next_round = R8
next_loop = 73
round_schedule_status = valid
round_sector_consistency = pass
```

## 28. Source Notes

Stock-Web files inspected:

```text
atlas/manifest.json
atlas/schema.json
atlas/symbol_profiles/196/196170.json
atlas/symbol_profiles/145/145020.json
atlas/symbol_profiles/302/302440.json
atlas/symbol_profiles/028/028300.json
atlas/symbol_profiles/068/068270.json
atlas/ohlcv_tradable_by_symbol_year/196/196170/2024.csv
atlas/ohlcv_tradable_by_symbol_year/145/145020/2024.csv
atlas/ohlcv_tradable_by_symbol_year/302/302440/2022.csv
atlas/ohlcv_tradable_by_symbol_year/302/302440/2023.csv
atlas/ohlcv_tradable_by_symbol_year/028/028300/2024.csv
```

External narrative evidence notes:

```text
Reuters: Merck injectable Keytruda trial and Merck/Alteogen enzyme context.
Allure/FDA-summary pages: Letybo U.S. approval and launch context.
Skycovione public reference: approval and later demand/suspension context.
HLB CRL/non-approval note: public regulatory/news flow; later source normalization recommended before implementation.
```


