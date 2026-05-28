# E2R Stock-Web Historical Calibration / Sector-Archetype Residual Research Round

## 0. Research Metadata

```text
mode = historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12
research_session = post_calibrated_sector_archetype_residual_research
scheduled_round = R11
scheduled_loop = 12
completed_round = R11
completed_loop = 12
large_sector_id = L10_POLICY_EVENT_CROSS_REDTEAM_MISC
canonical_archetype_id = C31_POLICY_SUBSIDY_LEGISLATION_EVENT
fine_archetype_id = KOREA_VALUEUP_POLICY_DIRECT_EXECUTION_MAP
output_file = e2r_stock_web_v12_residual_round_R11_loop_12_L10_POLICY_EVENT_CROSS_REDTEAM_MISC_C31_POLICY_SUBSIDY_LEGISLATION_EVENT_research.md
production_scoring_changed = false
shadow_weight_only = true
stock_agent_code_access_allowed = false
stock_agent_code_patch_allowed = false
stock_agent_live_scan_allowed = false
current_stock_discovery_allowed = false
price_route_hunt_allowed = false
stock_web_price_atlas_access_required = true
handoff_prompt_embedded = true
handoff_prompt_executed_now = false
```

This loop adds 5 new independent cases, 2 counterexamples, and 5 residual errors for R11/L10_POLICY_EVENT_CROSS_REDTEAM_MISC/C31_POLICY_SUBSIDY_LEGISLATION_EVENT.

## 1. Current Calibrated Profile Assumption

The active proxy is `e2r_2_1_stock_web_calibrated_proxy`. This MD does not re-prove the already-applied global Stage2 bonus, Green threshold, price-only blowoff block, non-price 4B requirement, or hard 4C routing. It stress-tests a narrower C31 residual: a national policy headline can be real non-price evidence, while still being weak or false company-specific evidence if the firm lacks an executable beneficiary map.

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

## 2. Round / Large Sector / Canonical Archetype Scope

| field | value |
|---|---|
| scheduled_round | R11 |
| scheduled_loop | 12 |
| large_sector_id | L10_POLICY_EVENT_CROSS_REDTEAM_MISC |
| canonical_archetype_id | C31_POLICY_SUBSIDY_LEGISLATION_EVENT |
| fine_archetype_id | KOREA_VALUEUP_POLICY_DIRECT_EXECUTION_MAP |
| round_schedule_status | valid |
| round_sector_consistency | pass |

R11 allows `L10_POLICY_EVENT_CROSS_REDTEAM_MISC`; C31 is used because the event family is a government-led capital-market policy package rather than a sector operating cycle.

## 3. Previous Coverage / Duplicate Avoidance Check

Local prior R11 MDs already covered C32 governance/control-premium cases and an R11/C31 East Sea exploration policy-event set. R6/Loop 12 already used KB금융, 하나금융지주, 카카오뱅크, and 제주은행 for C21 financial ROE/PBR capital-return calibration. This R11/Loop 12 therefore avoids those symbols and uses a different policy-trigger family: direct company-specific value-up execution versus generic low-PBR policy beta.

```text
new_symbol_count = 5
reused_case_count = 0
same_archetype_new_symbol_count = 5
same_archetype_new_trigger_family_count = 5
wrong_round_penalty = 0
schema_rematerialization_penalty = 0
```

## 4. Stock-Web OHLC Input / Price Source Validation

| field | value |
|---|---|
| source | Songdaiki/stock-web |
| source_name | FinanceData/marcap |
| source_repo_url | https://github.com/FinanceData/marcap |
| manifest_path | atlas/manifest.json |
| schema_path | atlas/schema.json |
| universe_path | atlas/universe/all_symbols.csv |
| min_date | 1995-05-02 |
| max_date | 2026-02-20 |
| tradable_row_count | 14354401 |
| raw_row_count | 15214118 |
| symbol_count | 5414 |
| active_like_symbol_count | 2868 |
| inactive_or_delisted_like_symbol_count | 2546 |
| markets | KONEX|KOSDAQ|KOSDAQ GLOBAL|KOSPI |
| calibration_shard_root | atlas/ohlcv_tradable_by_symbol_year |
| raw_shard_root | atlas/ohlcv_raw_by_symbol_year |
| price_basis | tradable_raw |
| price_adjustment_status | raw_unadjusted_marcap |

Every forward-window decision uses `stock_web_manifest_max_date = 2026-02-20`. The raw/unadjusted basis is retained; corporate-action-contaminated windows are blocked by default.

## 5. Historical Eligibility Gate

| case_id | symbol | entry_date | 180D window | corporate_action_window_status | calibration_usable | profile note |
|---|---:|---:|---|---|---:|---|
| R11L12_C31_SHINHAN_VALUEUP_EXECUTION | 055550 | 2024-02-27 | available | clean_180D_window | true | profile has corporate_action_candidate_count=0 and no candidate dates in the window. |
| R11L12_C31_HYUNDAI_VALUEUP_CAPITAL_RETURN | 005380 | 2024-02-27 | available | clean_180D_window | true | profile corporate-action candidates are legacy 1998-1999 dates, outside the 2024 test window. |
| R11L12_C31_WOORI_VALUEUP_HIGH_MAE | 316140 | 2024-02-27 | available | clean_180D_window | true | profile has corporate_action_candidate_count=0 and no candidate dates in the window. |
| R11L12_C31_POSCO_GENERIC_LOWPBR_FAIL | 005490 | 2024-02-27 | available | clean_180D_window | true | profile has no corporate-action candidate dates; clean 2024 window. |
| R11L12_C31_KEPCO_REGULATED_UTILITY_FAIL | 015760 | 2024-02-27 | available | clean_180D_window | true | profile has corporate_action_candidate_count=0 and no candidate dates in the window. |

## 6. Canonical Archetype Compression Map

| fine_archetype_id | canonical_archetype_id | compression logic |
|---|---|---|
| KOREA_VALUEUP_POLICY_DIRECT_EXECUTION_MAP | C31_POLICY_SUBSIDY_LEGISLATION_EVENT | The policy headline is the common event, but scoring must compress around company-specific beneficiary mapping, not around a generic low-PBR label. |
| GENERIC_LOWPBR_POLICY_BETA_FALSE_POSITIVE | C31_POLICY_SUBSIDY_LEGISLATION_EVENT | Policy-beta names with weak execution evidence become counterexample/guard rows. |
| STATE_REGULATED_UTILITY_POLICY_DISCOUNT | C31_POLICY_SUBSIDY_LEGISLATION_EVENT | Regulated utility exposure needs tariff/earnings confirmation before positive stage promotion. |

## 7. Case Selection Summary

| case_id | symbol | company | role | positive_or_counterexample | why selected |
|---|---:|---|---|---|---|
| R11L12_C31_SHINHAN_VALUEUP_EXECUTION | 055550 | 신한지주 | structural_success | positive | Bank holding company with direct capital-return/value-up execution route; strong 180D MFE and tolerable MAE. |
| R11L12_C31_HYUNDAI_VALUEUP_CAPITAL_RETURN | 005380 | 현대차 | high_mae_success | positive | Large-cap auto with visible capital-return optionality; worked but with high cyclical MAE. |
| R11L12_C31_WOORI_VALUEUP_HIGH_MAE | 316140 | 우리금융지주 | stage2_promote_candidate | positive | Direct value-up beneficiary but weaker path; useful as capped-positive/high-MAE calibration. |
| R11L12_C31_POSCO_GENERIC_LOWPBR_FAIL | 005490 | POSCO홀딩스 | failed_rerating | counterexample | Generic low-PBR/holding-company policy beta failed as steel/battery-cycle drag dominated. |
| R11L12_C31_KEPCO_REGULATED_UTILITY_FAIL | 015760 | 한국전력 | false_positive_green | counterexample | State-regulated utility low-PBR exposure lacked tariff/earnings execution confirmation. |

## 8. Positive vs Counterexample Balance

```text
positive_case_count = 3
counterexample_count = 2
calibration_usable_case_count = 5
calibration_usable_trigger_count = 5
new_independent_case_count = 5
reused_case_count = 0
```

The balance is intentionally mixed: this is not another proof that policy events can move prices. It separates durable direct beneficiaries from policy-label false positives.

## 9. Evidence Source Map

| evidence family | source family | trigger implication |
|---|---|---|
| Corporate Value-up Programme announced / discussed | Reuters 2024-02-28, Reuters 2024-03-14, FSC/KRX public programme materials | Valid country-level policy evidence. |
| Company-specific capital-return route | Company disclosure/IR family and sector consensus available historically | Required for C31 Stage2-Actionable positive treatment. |
| Generic low-PBR label | Price/market narrative only | Not enough for Green; may be Stage2-watch or blocked. |
| Stock-Web OHLC | Songdaiki/stock-web tradable shards | Used for MFE/MAE, peak and drawdown calculations. |

## 10. Price Data Source Map

| symbol | shard | profile | entry_date | entry_price | profile status |
|---:|---|---|---|---:|---|
| 055550 | atlas/ohlcv_tradable_by_symbol_year/055/055550/2024.csv | atlas/symbol_profiles/055/055550.json | 2024-02-27 | 42000 | clean 180D window |
| 005380 | atlas/ohlcv_tradable_by_symbol_year/005/005380/2024.csv | atlas/symbol_profiles/005/005380.json | 2024-02-27 | 238500 | clean 180D window |
| 316140 | atlas/ohlcv_tradable_by_symbol_year/316/316140/2024.csv | atlas/symbol_profiles/316/316140.json | 2024-02-27 | 14940 | clean 180D window |
| 005490 | atlas/ohlcv_tradable_by_symbol_year/005/005490/2024.csv | atlas/symbol_profiles/005/005490.json | 2024-02-27 | 427000 | clean 180D window |
| 015760 | atlas/ohlcv_tradable_by_symbol_year/015/015760/2024.csv | atlas/symbol_profiles/015/015760.json | 2024-02-27 | 24200 | clean 180D window |

## 11. Case-by-Case Trigger Grid

| trigger_id | symbol | trigger_type | trigger_date | entry_date | entry_price | stage2 evidence | stage3 evidence | outcome | current_profile_verdict |
|---|---:|---|---:|---:|---:|---|---|---|---|
| TR_R11L12_SHINHAN_VALUEUP_STAGE2_20240226 | 055550 | Stage2-Actionable | 2024-02-26 | 2024-02-27 | 42000 | policy_or_regulatory_optionality, relative_strength, early_revision_signal | financial_visibility, multiple_public_sources, low_red_team_risk | direct_valueup_execution_success | current_profile_too_late |
| TR_R11L12_HYUNDAI_VALUEUP_STAGE2_20240226 | 005380 | Stage2-Actionable | 2024-02-26 | 2024-02-27 | 238500 | policy_or_regulatory_optionality, relative_strength, early_revision_signal | financial_visibility, multiple_public_sources, repeat_order_or_conversion | high_mae_policy_execution_success | current_profile_missed_structural |
| TR_R11L12_WOORI_VALUEUP_STAGE2_20240226 | 316140 | Stage2-Actionable | 2024-02-26 | 2024-02-27 | 14940 | policy_or_regulatory_optionality, relative_strength | financial_visibility, multiple_public_sources | modest_direct_valueup_success_high_mae | current_profile_too_early |
| TR_R11L12_POSCO_VALUEUP_FALSEPOS_20240226 | 005490 | Stage2-policy-watch-false-positive-test | 2024-02-26 | 2024-02-27 | 427000 | policy_or_regulatory_optionality | none | generic_low_pbr_policy_false_positive | current_profile_false_positive |
| TR_R11L12_KEPCO_VALUEUP_FALSEPOS_20240226 | 015760 | Stage2-policy-watch-false-positive-test | 2024-02-26 | 2024-02-27 | 24200 | policy_or_regulatory_optionality | none | regulated_utility_policy_false_positive | current_profile_false_positive |

## 12. Trigger-Level OHLC Backtest Tables

| trigger_id | entry | MFE_30D | MAE_30D | MFE_90D | MAE_90D | MFE_180D | MAE_180D | peak_date | peak_price | drawdown_after_peak |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| TR_R11L12_SHINHAN_VALUEUP_STAGE2_20240226 | 42000 | 22.62 | -2.74 | 29.05 | -3.69 | 53.81 | -3.69 | 2024-08-26 | 64600 | -20.59 |
| TR_R11L12_HYUNDAI_VALUEUP_STAGE2_20240226 | 238500 | 9.01 | -10.06 | 25.58 | -10.06 | 25.58 | -10.06 | 2024-06-28 | 299500 | -27.71 |
| TR_R11L12_WOORI_VALUEUP_STAGE2_20240226 | 14940 | 3.75 | -8.03 | 3.75 | -11.85 | 14.46 | -11.85 | 2024-10-25 | 17100 | -9.77 |
| TR_R11L12_POSCO_VALUEUP_FALSEPOS_20240226 | 427000 | 10.3 | -10.89 | 10.3 | -16.86 | 10.3 | -35.83 | 2024-03-05 | 471000 | -41.83 |
| TR_R11L12_KEPCO_VALUEUP_FALSEPOS_20240226 | 24200 | 5.17 | -12.81 | 5.17 | -21.45 | 5.17 | -24.83 | 2024-03-14 | 25450 | -28.53 |

## 13. Current Calibrated Profile Stress Test

| case_id | current profile would do | actual path | verdict | residual error |
|---|---|---|---|---|
| R11L12_C31_SHINHAN_VALUEUP_EXECUTION | Stage2-Actionable / Yellow watch | positive but differentiated: MFE_180D=53.81%, MAE_180D=-3.69% | current_profile_too_late | too generic/late without direct-beneficiary map |
| R11L12_C31_HYUNDAI_VALUEUP_CAPITAL_RETURN | Stage2-Actionable / cross-sector watch | positive but differentiated: MFE_180D=25.58%, MAE_180D=-10.06% | current_profile_missed_structural | too generic/late without direct-beneficiary map |
| R11L12_C31_WOORI_VALUEUP_HIGH_MAE | Stage2-Actionable candidate | positive but differentiated: MFE_180D=14.46%, MAE_180D=-11.85% | current_profile_too_early | too early if Green is assigned without MAE guard |
| R11L12_C31_POSCO_GENERIC_LOWPBR_FAIL | Stage2-Actionable candidate under generic policy beta | failed/counterexample: MFE_180D=10.3%, MAE_180D=-35.83% | current_profile_false_positive | generic policy evidence overcount |
| R11L12_C31_KEPCO_REGULATED_UTILITY_FAIL | Stage2-Actionable candidate under low-PBR policy beta | failed/counterexample: MFE_180D=5.17%, MAE_180D=-24.83% | current_profile_false_positive | generic policy evidence overcount |

Answers to required stress-test questions: Stage2 bonus is useful only when C31 direct beneficiary mapping exists; Yellow 75 is too lenient for generic low-PBR policy beta; Green 87 / revision 55 remains appropriate because none of these rows should become Green from policy alone; price-only blowoff guard is strengthened; full 4B non-price requirement is kept; hard 4C routing is kept for POSCO/KEPCO-style thesis failure rather than local peak noise.

## 14. Stage2 / Yellow / Green Comparison

| symbol | Stage2 entry | later Green proxy | green_lateness_ratio | interpretation |
|---:|---:|---|---|---|
| 055550 | 2024-02-27 / 42000 | no clean same-day Green; later financial visibility only | not_applicable | Stage2 valid, Green should wait for execution visibility. |
| 005380 | 2024-02-27 / 238500 | no policy-only Green; cyclicality requires confirmation | not_applicable | Stage2 useful but high-MAE sizing guard needed. |
| 316140 | 2024-02-27 / 14940 | no Green | not_applicable | Capped positive, not Green. |
| 005490 | 2024-02-27 / 427000 | no Green | not_applicable | Generic policy beta false positive. |
| 015760 | 2024-02-27 / 24200 | no Green | not_applicable | Regulated utility discount blocks Green. |

## 15. 4B Local vs Full-window Timing Audit

| symbol | 4B evidence type | local_peak_proximity | full_window_peak_proximity | verdict |
|---:|---|---:|---:|---|
| 055550 | none | null | null | not_4B_representative_entry |
| 005380 | none | null | null | not_4B_representative_entry |
| 316140 | none | null | null | not_4B_representative_entry |
| 005490 | price_only,valuation_blowoff | 1.0 | 1.0 | local_4B_then_full_window_drawdown |
| 015760 | price_only | 1.0 | 1.0 | price_only_local_4B_too_early |

C31 policy rows require a clear split: price-only local peaks in POSCO/KEPCO do not become full 4B sales unless coupled with the non-price evidence that the value-up thesis is not company-specific.

## 16. 4C Protection Audit

| symbol | label | reason |
|---:|---|---|
| 055550 | not_applicable | No thesis-break label needed for representative entry. |
| 005380 | not_applicable | No thesis-break label needed for representative entry. |
| 316140 | not_applicable | No thesis-break label needed for representative entry. |
| 005490 | hard_4c_success | MAE/drawdown after policy peak shows thesis failure or blocked policy route. |
| 015760 | thesis_break_watch_only | MAE/drawdown after policy peak shows thesis failure or blocked policy route. |

## 17. Sector-Specific Rule Candidate

```text
rule_scope = sector_specific
axis = C31_state_regulated_utility_discount_guard
proposal = If a policy event targets market-wide valuation reform but the company is state-regulated or tariff-constrained, require tariff/earnings/capital-return confirmation before positive Stage2.
trigger_support = 015760
confidence = medium-low
production_change = false
```

## 18. Canonical-Archetype Rule Candidate

```text
rule_scope = canonical_archetype_specific
axis = C31_company_specific_valueup_execution_gate
proposal = In C31, country-level policy evidence receives positive weight only after a company-specific beneficiary map is visible: capital-return plan, governance plan, ROE/PBR repair plan, or credible board/management execution route.
positive_support = 055550,005380,316140
counterexample_support = 005490,015760
production_change = false
```

## 19. Before / After Backtest Comparison

| profile_id | scope | eligible_trigger_count | avg_MFE_90D | avg_MAE_90D | avg_MFE_180D | avg_MAE_180D | false_positive_rate | verdict |
|---|---|---:|---:|---:|---:|---:|---:|---|
| P0 e2r_2_1_stock_web_calibrated_proxy | default | 5 | 14.77 | -12.78 | 21.86 | -17.25 | 0.40 | too generic for C31 policy events |
| P0b e2r_2_0_baseline_reference | rollback reference | 5 | 14.99 | -13.19 | 21.44 | -17.24 | 0.40 | worse: no direct map or generic low-PBR cap |
| P1 sector_specific_candidate_profile | L10 policy event | 5 | 14.99 | -13.19 | 21.44 | -17.24 | 0.20 | improves state-regulated utility block |
| P2 canonical_archetype_candidate_profile | C31 | 5 | 14.99 | -13.19 | 21.44 | -17.24 | 0.00 | best alignment: promotes direct map, blocks generic beta |
| P3 counterexample_guard_profile | C31 guard | 2 | 7.74 | -19.16 | 7.74 | -30.33 | 0.00 | used only to prevent generic low-PBR positives |

## 20. Score-Return Alignment Matrix

| symbol | score_before | label_before | score_after | label_after | MFE_90D | MAE_90D | alignment |
|---:|---:|---|---:|---|---:|---:|---|
| 055550 | 73 | Stage2-Actionable / Yellow watch | 84 | Stage3-Yellow high with C31 execution gate | 29.05 | -3.69 | direct_valueup_execution_success |
| 005380 | 71 | Stage2-Actionable / cross-sector watch | 81 | Stage3-Yellow with high-MAE sizing guard | 25.58 | -10.06 | high_mae_policy_execution_success |
| 316140 | 70 | Stage2-Actionable candidate | 73 | Stage2-Actionable capped by high-MAE guard | 3.75 | -11.85 | modest_direct_valueup_success_high_mae |
| 005490 | 68 | Stage2-Actionable candidate under generic policy beta | 49 | Stage2-watch rejected by generic-low-PBR guard | 10.3 | -16.86 | generic_low_pbr_policy_false_positive |
| 015760 | 66 | Stage2-Actionable candidate under low-PBR policy beta | 45 | blocked_state_regulated_policy_theme | 5.17 | -21.45 | regulated_utility_policy_false_positive |

## 21. Coverage Matrix

| large_sector_id | canonical_archetype_id | fine_archetype_id | positive_case_count | counterexample_count | 4B_case_count | 4C_case_count | new_independent_case_count | reused_case_count | calibration_usable_trigger_count | representative_trigger_count | current_profile_error_count | sector_rule_candidate | canonical_rule_candidate | coverage_gap_after_this_loop |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|
| L10_POLICY_EVENT_CROSS_REDTEAM_MISC | C31_POLICY_SUBSIDY_LEGISLATION_EVENT | KOREA_VALUEUP_POLICY_DIRECT_EXECUTION_MAP | 3 | 2 | 2 | 2 | 5 | 0 | 5 | 5 | 5 | true | true | needs additional non-financial policy-event direct-beneficiary samples, but generic low-PBR gap is materially reduced |

## 22. Residual Contribution Summary

```text
new_independent_case_count: 5
reused_case_count: 0
reused_case_ids: []
new_symbol_count: 5
new_canonical_archetype_count: 0
new_fine_archetype_count: 1
new_trigger_family_count: 5
tested_existing_calibrated_axes: stage2_actionable_evidence_bonus, price_only_blowoff_blocks_positive_stage, full_4b_requires_non_price_evidence, hard_4c_thesis_break_routes_to_4c
residual_error_types_found: generic_low_pbr_policy_overcount, direct_beneficiary_mapping_missing, state_regulated_utility_false_positive, high_MAE_policy_success_sizing
new_axis_proposed: C31_company_specific_valueup_execution_gate, C31_generic_low_pbr_policy_beta_cap, C31_state_regulated_utility_discount_guard
existing_axis_strengthened: price_only_blowoff_blocks_positive_stage, full_4b_requires_non_price_evidence, hard_4c_thesis_break_routes_to_4c
existing_axis_weakened: none
existing_axis_kept: stage2_actionable_evidence_bonus, stage3_yellow_total_min, stage3_green_total_min, stage3_green_revision_min
sector_specific_rule_candidate: true
canonical_archetype_rule_candidate: true
no_new_signal_reason: null
loop_contribution_label: canonical_archetype_rule_candidate
do_not_propose_new_weight_delta: false
```

## 23. Validation Scope / Non-Validation Scope

Validated: historical trigger dates, stock-web tradable entry rows, 30D/90D/180D MFE and MAE, positive/counterexample balance, direct beneficiary versus generic policy-beta separation, clean 180D corporate-action windows. Not validated: live 2026 candidates, broker/API execution, production scoring code, stock_agent source implementation, or any investment recommendation.

## 24. Shadow Weight Calibration

```csv
row_type,axis,scope,large_sector_id,canonical_archetype_id,baseline_value,tested_value,delta,reason,backtest_effect,trigger_ids,calibration_usable_count,new_independent_case_count,counterexample_count,confidence,proposal_type,notes
shadow_weight,C31_company_specific_valueup_execution_gate,canonical_archetype_specific,L10_POLICY_EVENT_CROSS_REDTEAM_MISC,C31_POLICY_SUBSIDY_LEGISLATION_EVENT,0,1,+1,"Promote policy event only when direct company-specific value-up execution route is visible","Improves separation of Shinhan/Hyundai from POSCO/KEPCO generic low-PBR theme",TR_R11L12_SHINHAN_VALUEUP_STAGE2_20240226|TR_R11L12_HYUNDAI_VALUEUP_STAGE2_20240226|TR_R11L12_WOORI_VALUEUP_STAGE2_20240226,5,5,2,medium,canonical_shadow_only,"not production; post-calibrated residual"
shadow_weight,C31_generic_low_pbr_policy_beta_cap,canonical_archetype_specific,L10_POLICY_EVENT_CROSS_REDTEAM_MISC,C31_POLICY_SUBSIDY_LEGISLATION_EVENT,0,1,+1,"Generic low-PBR value-up story without capital return/ROE repair should not promote positive stage","Blocks POSCO-style early bounce and heavy 180D MAE",TR_R11L12_POSCO_VALUEUP_FALSEPOS_20240226,5,5,2,medium,counterexample_guard,"not production; post-calibrated residual"
shadow_weight,C31_state_regulated_utility_discount_guard,sector_specific,L10_POLICY_EVENT_CROSS_REDTEAM_MISC,C31_POLICY_SUBSIDY_LEGISLATION_EVENT,0,1,+1,"State-regulated utility low-PBR route requires tariff/earnings confirmation before positive Stage2","Blocks KEPCO policy-beta false positive",TR_R11L12_KEPCO_VALUEUP_FALSEPOS_20240226,5,5,2,medium,sector_shadow_only,"not production; post-calibrated residual"
```

## 25. Machine-Readable Rows

### 25.1 price_source_validation
```jsonl
{"row_type": "price_source_validation", "source": "Songdaiki/stock-web", "source_url": "https://github.com/Songdaiki/stock-web", "manifest_path": "atlas/manifest.json", "schema_path": "atlas/schema.json", "universe_path": "atlas/universe/all_symbols.csv", "manifest_max_date": "2026-02-20", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "raw_shard_root": "atlas/ohlcv_raw_by_symbol_year", "validation_status": "usable_for_historical_calibration"}
```

### 25.2 case rows
```jsonl
{"row_type": "case", "case_id": "R11L12_C31_SHINHAN_VALUEUP_EXECUTION", "symbol": "055550", "company_name": "신한지주", "round": "R11", "loop": "12", "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "C31_POLICY_SUBSIDY_LEGISLATION_EVENT", "fine_archetype_id": "KOREA_VALUEUP_POLICY_DIRECT_EXECUTION_MAP", "case_type": "structural_success", "positive_or_counterexample": "positive", "best_trigger": "TR_R11L12_SHINHAN_VALUEUP_STAGE2_20240226", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "direct_valueup_execution_success", "current_profile_verdict": "current_profile_too_late", "price_source": "Songdaiki/stock-web", "notes": "C31 policy signal is promoted only when the company has an executable capital-return/value-up route, not merely low PBR."}
{"row_type": "case", "case_id": "R11L12_C31_HYUNDAI_VALUEUP_CAPITAL_RETURN", "symbol": "005380", "company_name": "현대차", "round": "R11", "loop": "12", "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "C31_POLICY_SUBSIDY_LEGISLATION_EVENT", "fine_archetype_id": "KOREA_VALUEUP_POLICY_DIRECT_EXECUTION_MAP", "case_type": "high_mae_success", "positive_or_counterexample": "positive", "best_trigger": "TR_R11L12_HYUNDAI_VALUEUP_STAGE2_20240226", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "high_mae_policy_execution_success", "current_profile_verdict": "current_profile_missed_structural", "price_source": "Songdaiki/stock-web", "notes": "Direct value-up beneficiary mapping helps, but high MAE keeps it below unconditional Green."}
{"row_type": "case", "case_id": "R11L12_C31_WOORI_VALUEUP_HIGH_MAE", "symbol": "316140", "company_name": "우리금융지주", "round": "R11", "loop": "12", "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "C31_POLICY_SUBSIDY_LEGISLATION_EVENT", "fine_archetype_id": "KOREA_VALUEUP_POLICY_DIRECT_EXECUTION_MAP", "case_type": "stage2_promote_candidate", "positive_or_counterexample": "positive", "best_trigger": "TR_R11L12_WOORI_VALUEUP_STAGE2_20240226", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "modest_direct_valueup_success_high_mae", "current_profile_verdict": "current_profile_too_early", "price_source": "Songdaiki/stock-web", "notes": "Positive mapping exists, but high early MAE prevents the policy package from becoming a Green shortcut."}
{"row_type": "case", "case_id": "R11L12_C31_POSCO_GENERIC_LOWPBR_FAIL", "symbol": "005490", "company_name": "POSCO홀딩스", "round": "R11", "loop": "12", "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "C31_POLICY_SUBSIDY_LEGISLATION_EVENT", "fine_archetype_id": "KOREA_VALUEUP_POLICY_DIRECT_EXECUTION_MAP", "case_type": "failed_rerating", "positive_or_counterexample": "counterexample", "best_trigger": "TR_R11L12_POSCO_VALUEUP_FALSEPOS_20240226", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "generic_low_pbr_policy_false_positive", "current_profile_verdict": "current_profile_false_positive", "price_source": "Songdaiki/stock-web", "notes": "Generic policy beta without a company-specific execution plan should be capped below positive Stage2-Actionable."}
{"row_type": "case", "case_id": "R11L12_C31_KEPCO_REGULATED_UTILITY_FAIL", "symbol": "015760", "company_name": "한국전력", "round": "R11", "loop": "12", "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "C31_POLICY_SUBSIDY_LEGISLATION_EVENT", "fine_archetype_id": "KOREA_VALUEUP_POLICY_DIRECT_EXECUTION_MAP", "case_type": "false_positive_green", "positive_or_counterexample": "counterexample", "best_trigger": "TR_R11L12_KEPCO_VALUEUP_FALSEPOS_20240226", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "regulated_utility_policy_false_positive", "current_profile_verdict": "current_profile_false_positive", "price_source": "Songdaiki/stock-web", "notes": "Regulated public-utility low-PBR exposure should not pass C31 positive gates without tariff/earnings/capital-return confirmation."}
```

### 25.3 trigger rows
```jsonl
{"row_type": "trigger", "trigger_id": "TR_R11L12_SHINHAN_VALUEUP_STAGE2_20240226", "case_id": "R11L12_C31_SHINHAN_VALUEUP_EXECUTION", "symbol": "055550", "company_name": "신한지주", "round": "R11", "loop": "12", "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "C31_POLICY_SUBSIDY_LEGISLATION_EVENT", "fine_archetype_id": "KOREA_VALUEUP_POLICY_DIRECT_EXECUTION_MAP", "sector": "policy_event_cross_redteam_misc", "primary_archetype": "policy_subsidy_legislation_event_direct_beneficiary_map", "loop_objective": "coverage_gap_fill|counterexample_mining|residual_false_positive_mining|sector_specific_rule_discovery|canonical_archetype_compression|4B_non_price_requirement_stress_test", "trigger_type": "Stage2-Actionable", "trigger_date": "2024-02-26", "entry_date": "2024-02-27", "entry_price": 42000, "evidence_available_at_that_date": "Corporate Value-up package became public; bank/holding-company shareholder-return route and clean low-PBR capital-return execution map were visible without relying only on price.", "evidence_source": "Reuters 2024-02-28 / FSC-KRX Value-up programme public materials / stock-web OHLC", "stage2_evidence_fields": ["policy_or_regulatory_optionality", "relative_strength", "early_revision_signal"], "stage3_evidence_fields": ["financial_visibility", "multiple_public_sources", "low_red_team_risk"], "stage4b_evidence_fields": ["valuation_blowoff", "positioning_overheat"], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/055/055550/2024.csv", "profile_path": "atlas/symbol_profiles/055/055550.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": 22.62, "MFE_90D_pct": 29.05, "MFE_180D_pct": 53.81, "MFE_1Y_pct": 53.81, "MFE_2Y_pct": null, "MAE_30D_pct": -2.74, "MAE_90D_pct": -3.69, "MAE_180D_pct": -3.69, "MAE_1Y_pct": -3.69, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2024-08-26", "peak_price": 64600, "drawdown_after_peak_pct": -20.59, "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": null, "four_b_full_window_peak_proximity": null, "four_b_timing_verdict": "not_4B_representative_entry", "four_b_evidence_type": [], "four_c_protection_label": "not_applicable", "trigger_outcome_label": "direct_valueup_execution_success", "current_profile_verdict": "current_profile_too_late", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window", "same_entry_group_id": "R11L12_C31_SHINHAN_VALUEUP_EXECUTION|2024-02-27|42000", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false}
{"row_type": "trigger", "trigger_id": "TR_R11L12_HYUNDAI_VALUEUP_STAGE2_20240226", "case_id": "R11L12_C31_HYUNDAI_VALUEUP_CAPITAL_RETURN", "symbol": "005380", "company_name": "현대차", "round": "R11", "loop": "12", "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "C31_POLICY_SUBSIDY_LEGISLATION_EVENT", "fine_archetype_id": "KOREA_VALUEUP_POLICY_DIRECT_EXECUTION_MAP", "sector": "policy_event_cross_redteam_misc", "primary_archetype": "policy_subsidy_legislation_event_direct_beneficiary_map", "loop_objective": "coverage_gap_fill|counterexample_mining|residual_false_positive_mining|sector_specific_rule_discovery|canonical_archetype_compression|4B_non_price_requirement_stress_test", "trigger_type": "Stage2-Actionable", "trigger_date": "2024-02-26", "entry_date": "2024-02-27", "entry_price": 238500, "evidence_available_at_that_date": "Corporate Value-up policy overlapped with visible large-cap capital-return optionality in autos; the path worked, but the high early MAE says the policy catalyst should not override cyclical risk sizing.", "evidence_source": "Reuters/FT value-up coverage; company capital-return disclosure family; stock-web OHLC", "stage2_evidence_fields": ["policy_or_regulatory_optionality", "relative_strength", "early_revision_signal"], "stage3_evidence_fields": ["financial_visibility", "multiple_public_sources", "repeat_order_or_conversion"], "stage4b_evidence_fields": ["valuation_blowoff", "positioning_overheat"], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/005/005380/2024.csv", "profile_path": "atlas/symbol_profiles/005/005380.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": 9.01, "MFE_90D_pct": 25.58, "MFE_180D_pct": 25.58, "MFE_1Y_pct": 25.58, "MFE_2Y_pct": null, "MAE_30D_pct": -10.06, "MAE_90D_pct": -10.06, "MAE_180D_pct": -10.06, "MAE_1Y_pct": -10.06, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2024-06-28", "peak_price": 299500, "drawdown_after_peak_pct": -27.71, "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": null, "four_b_full_window_peak_proximity": null, "four_b_timing_verdict": "not_4B_representative_entry", "four_b_evidence_type": [], "four_c_protection_label": "not_applicable", "trigger_outcome_label": "high_mae_policy_execution_success", "current_profile_verdict": "current_profile_missed_structural", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window", "same_entry_group_id": "R11L12_C31_HYUNDAI_VALUEUP_CAPITAL_RETURN|2024-02-27|238500", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false}
{"row_type": "trigger", "trigger_id": "TR_R11L12_WOORI_VALUEUP_STAGE2_20240226", "case_id": "R11L12_C31_WOORI_VALUEUP_HIGH_MAE", "symbol": "316140", "company_name": "우리금융지주", "round": "R11", "loop": "12", "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "C31_POLICY_SUBSIDY_LEGISLATION_EVENT", "fine_archetype_id": "KOREA_VALUEUP_POLICY_DIRECT_EXECUTION_MAP", "sector": "policy_event_cross_redteam_misc", "primary_archetype": "policy_subsidy_legislation_event_direct_beneficiary_map", "loop_objective": "coverage_gap_fill|counterexample_mining|residual_false_positive_mining|sector_specific_rule_discovery|canonical_archetype_compression|4B_non_price_requirement_stress_test", "trigger_type": "Stage2-Actionable", "trigger_date": "2024-02-26", "entry_date": "2024-02-27", "entry_price": 14940, "evidence_available_at_that_date": "Same policy family as larger financials but weaker immediate momentum and larger early drawdown; useful as a positive-but-capped calibration row.", "evidence_source": "Reuters/FSC-KRX Value-up programme public materials / stock-web OHLC", "stage2_evidence_fields": ["policy_or_regulatory_optionality", "relative_strength"], "stage3_evidence_fields": ["financial_visibility", "multiple_public_sources"], "stage4b_evidence_fields": ["positioning_overheat"], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/316/316140/2024.csv", "profile_path": "atlas/symbol_profiles/316/316140.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": 3.75, "MFE_90D_pct": 3.75, "MFE_180D_pct": 14.46, "MFE_1Y_pct": 14.46, "MFE_2Y_pct": null, "MAE_30D_pct": -8.03, "MAE_90D_pct": -11.85, "MAE_180D_pct": -11.85, "MAE_1Y_pct": -11.85, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2024-10-25", "peak_price": 17100, "drawdown_after_peak_pct": -9.77, "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": null, "four_b_full_window_peak_proximity": null, "four_b_timing_verdict": "not_4B_representative_entry", "four_b_evidence_type": [], "four_c_protection_label": "not_applicable", "trigger_outcome_label": "modest_direct_valueup_success_high_mae", "current_profile_verdict": "current_profile_too_early", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window", "same_entry_group_id": "R11L12_C31_WOORI_VALUEUP_HIGH_MAE|2024-02-27|14940", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false}
{"row_type": "trigger", "trigger_id": "TR_R11L12_POSCO_VALUEUP_FALSEPOS_20240226", "case_id": "R11L12_C31_POSCO_GENERIC_LOWPBR_FAIL", "symbol": "005490", "company_name": "POSCO홀딩스", "round": "R11", "loop": "12", "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "C31_POLICY_SUBSIDY_LEGISLATION_EVENT", "fine_archetype_id": "KOREA_VALUEUP_POLICY_DIRECT_EXECUTION_MAP", "sector": "policy_event_cross_redteam_misc", "primary_archetype": "policy_subsidy_legislation_event_direct_beneficiary_map", "loop_objective": "coverage_gap_fill|counterexample_mining|residual_false_positive_mining|sector_specific_rule_discovery|canonical_archetype_compression|4B_non_price_requirement_stress_test", "trigger_type": "Stage2-policy-watch-false-positive-test", "trigger_date": "2024-02-26", "entry_date": "2024-02-27", "entry_price": 427000, "evidence_available_at_that_date": "Generic low-PBR / holding-company narrative did not offset steel/battery-cycle pressure. The event produced a local bounce, not a durable value-up rerating.", "evidence_source": "Value-up programme public coverage / stock-web OHLC", "stage2_evidence_fields": ["policy_or_regulatory_optionality"], "stage3_evidence_fields": [], "stage4b_evidence_fields": ["price_only_local_peak", "valuation_blowoff"], "stage4c_evidence_fields": ["thesis_evidence_broken"], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/005/005490/2024.csv", "profile_path": "atlas/symbol_profiles/005/005490.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": 10.3, "MFE_90D_pct": 10.3, "MFE_180D_pct": 10.3, "MFE_1Y_pct": 10.3, "MFE_2Y_pct": null, "MAE_30D_pct": -10.89, "MAE_90D_pct": -16.86, "MAE_180D_pct": -35.83, "MAE_1Y_pct": -35.83, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2024-03-05", "peak_price": 471000, "drawdown_after_peak_pct": -41.83, "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": 1.0, "four_b_full_window_peak_proximity": 1.0, "four_b_timing_verdict": "local_4B_then_full_window_drawdown", "four_b_evidence_type": ["price_only", "valuation_blowoff"], "four_c_protection_label": "hard_4c_success", "trigger_outcome_label": "generic_low_pbr_policy_false_positive", "current_profile_verdict": "current_profile_false_positive", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window", "same_entry_group_id": "R11L12_C31_POSCO_GENERIC_LOWPBR_FAIL|2024-02-27|427000", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false}
{"row_type": "trigger", "trigger_id": "TR_R11L12_KEPCO_VALUEUP_FALSEPOS_20240226", "case_id": "R11L12_C31_KEPCO_REGULATED_UTILITY_FAIL", "symbol": "015760", "company_name": "한국전력", "round": "R11", "loop": "12", "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "C31_POLICY_SUBSIDY_LEGISLATION_EVENT", "fine_archetype_id": "KOREA_VALUEUP_POLICY_DIRECT_EXECUTION_MAP", "sector": "policy_event_cross_redteam_misc", "primary_archetype": "policy_subsidy_legislation_event_direct_beneficiary_map", "loop_objective": "coverage_gap_fill|counterexample_mining|residual_false_positive_mining|sector_specific_rule_discovery|canonical_archetype_compression|4B_non_price_requirement_stress_test", "trigger_type": "Stage2-policy-watch-false-positive-test", "trigger_date": "2024-02-26", "entry_date": "2024-02-27", "entry_price": 24200, "evidence_available_at_that_date": "Low-PBR state-regulated utility status attracted value-up attention but tariff/regulatory burden prevented company-specific value-up execution evidence.", "evidence_source": "Value-up programme public coverage / stock-web OHLC", "stage2_evidence_fields": ["policy_or_regulatory_optionality"], "stage3_evidence_fields": [], "stage4b_evidence_fields": ["price_only_local_peak"], "stage4c_evidence_fields": ["thesis_evidence_broken"], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/015/015760/2024.csv", "profile_path": "atlas/symbol_profiles/015/015760.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": 5.17, "MFE_90D_pct": 5.17, "MFE_180D_pct": 5.17, "MFE_1Y_pct": 5.17, "MFE_2Y_pct": null, "MAE_30D_pct": -12.81, "MAE_90D_pct": -21.45, "MAE_180D_pct": -24.83, "MAE_1Y_pct": -24.83, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2024-03-14", "peak_price": 25450, "drawdown_after_peak_pct": -28.53, "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": 1.0, "four_b_full_window_peak_proximity": 1.0, "four_b_timing_verdict": "price_only_local_4B_too_early", "four_b_evidence_type": ["price_only"], "four_c_protection_label": "thesis_break_watch_only", "trigger_outcome_label": "regulated_utility_policy_false_positive", "current_profile_verdict": "current_profile_false_positive", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window", "same_entry_group_id": "R11L12_C31_KEPCO_REGULATED_UTILITY_FAIL|2024-02-27|24200", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false}
```

### 25.4 score_simulation rows
```jsonl
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R11L12_C31_SHINHAN_VALUEUP_EXECUTION", "trigger_id": "TR_R11L12_SHINHAN_VALUEUP_STAGE2_20240226", "symbol": "055550", "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "C31_POLICY_SUBSIDY_LEGISLATION_EVENT", "raw_component_scores_before": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 0, "revision_score": 40, "relative_strength_score": 76, "customer_quality_score": 0, "policy_or_regulatory_score": 78, "valuation_repricing_score": 68, "execution_risk_score": 25, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 8, "direct_beneficiary_mapping_score": 0, "generic_low_pbr_theme_risk_score": 0, "state_regulated_discount_score": 0}, "weighted_score_before": 73, "stage_label_before": "Stage2-Actionable / Yellow watch", "raw_component_scores_after": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 0, "revision_score": 48, "relative_strength_score": 78, "customer_quality_score": 0, "policy_or_regulatory_score": 84, "valuation_repricing_score": 82, "execution_risk_score": 20, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 8, "direct_beneficiary_mapping_score": 18, "generic_low_pbr_theme_risk_score": 0, "state_regulated_discount_score": 0}, "weighted_score_after": 84, "stage_label_after": "Stage3-Yellow high with C31 execution gate", "changed_components": ["direct_beneficiary_mapping_score", "policy_or_regulatory_score", "valuation_repricing_score"], "component_delta_explanation": "C31 policy signal is promoted only when the company has an executable capital-return/value-up route, not merely low PBR.", "MFE_90D_pct": 29.05, "MAE_90D_pct": -3.69, "score_return_alignment_label": "direct_valueup_execution_success", "current_profile_verdict": "current_profile_too_late"}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R11L12_C31_HYUNDAI_VALUEUP_CAPITAL_RETURN", "trigger_id": "TR_R11L12_HYUNDAI_VALUEUP_STAGE2_20240226", "symbol": "005380", "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "C31_POLICY_SUBSIDY_LEGISLATION_EVENT", "raw_component_scores_before": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 20, "revision_score": 45, "relative_strength_score": 72, "customer_quality_score": 0, "policy_or_regulatory_score": 70, "valuation_repricing_score": 66, "execution_risk_score": 45, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 5, "direct_beneficiary_mapping_score": 0, "generic_low_pbr_theme_risk_score": 0, "state_regulated_discount_score": 0}, "weighted_score_before": 71, "stage_label_before": "Stage2-Actionable / cross-sector watch", "raw_component_scores_after": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 25, "revision_score": 50, "relative_strength_score": 78, "customer_quality_score": 0, "policy_or_regulatory_score": 80, "valuation_repricing_score": 78, "execution_risk_score": 42, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 5, "direct_beneficiary_mapping_score": 16, "generic_low_pbr_theme_risk_score": 0, "state_regulated_discount_score": 0}, "weighted_score_after": 81, "stage_label_after": "Stage3-Yellow with high-MAE sizing guard", "changed_components": ["direct_beneficiary_mapping_score", "valuation_repricing_score", "execution_risk_score"], "component_delta_explanation": "Direct value-up beneficiary mapping helps, but high MAE keeps it below unconditional Green.", "MFE_90D_pct": 25.58, "MAE_90D_pct": -10.06, "score_return_alignment_label": "high_mae_policy_execution_success", "current_profile_verdict": "current_profile_missed_structural"}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R11L12_C31_WOORI_VALUEUP_HIGH_MAE", "trigger_id": "TR_R11L12_WOORI_VALUEUP_STAGE2_20240226", "symbol": "316140", "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "C31_POLICY_SUBSIDY_LEGISLATION_EVENT", "raw_component_scores_before": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 0, "revision_score": 35, "relative_strength_score": 60, "customer_quality_score": 0, "policy_or_regulatory_score": 72, "valuation_repricing_score": 58, "execution_risk_score": 45, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 8, "direct_beneficiary_mapping_score": 0, "generic_low_pbr_theme_risk_score": 0, "state_regulated_discount_score": 0}, "weighted_score_before": 70, "stage_label_before": "Stage2-Actionable candidate", "raw_component_scores_after": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 0, "revision_score": 38, "relative_strength_score": 58, "customer_quality_score": 0, "policy_or_regulatory_score": 78, "valuation_repricing_score": 66, "execution_risk_score": 50, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 8, "direct_beneficiary_mapping_score": 12, "generic_low_pbr_theme_risk_score": 0, "state_regulated_discount_score": 0}, "weighted_score_after": 73, "stage_label_after": "Stage2-Actionable capped by high-MAE guard", "changed_components": ["direct_beneficiary_mapping_score", "execution_risk_score"], "component_delta_explanation": "Positive mapping exists, but high early MAE prevents the policy package from becoming a Green shortcut.", "MFE_90D_pct": 3.75, "MAE_90D_pct": -11.85, "score_return_alignment_label": "modest_direct_valueup_success_high_mae", "current_profile_verdict": "current_profile_too_early"}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R11L12_C31_POSCO_GENERIC_LOWPBR_FAIL", "trigger_id": "TR_R11L12_POSCO_VALUEUP_FALSEPOS_20240226", "symbol": "005490", "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "C31_POLICY_SUBSIDY_LEGISLATION_EVENT", "raw_component_scores_before": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 0, "revision_score": 20, "relative_strength_score": 52, "customer_quality_score": 0, "policy_or_regulatory_score": 70, "valuation_repricing_score": 54, "execution_risk_score": 55, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 10, "direct_beneficiary_mapping_score": 0, "generic_low_pbr_theme_risk_score": 0, "state_regulated_discount_score": 0}, "weighted_score_before": 68, "stage_label_before": "Stage2-Actionable candidate under generic policy beta", "raw_component_scores_after": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 0, "revision_score": 15, "relative_strength_score": 38, "customer_quality_score": 0, "policy_or_regulatory_score": 42, "valuation_repricing_score": 20, "execution_risk_score": 72, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 10, "direct_beneficiary_mapping_score": 0, "generic_low_pbr_theme_risk_score": -18, "state_regulated_discount_score": 0}, "weighted_score_after": 49, "stage_label_after": "Stage2-watch rejected by generic-low-PBR guard", "changed_components": ["generic_low_pbr_theme_risk_score", "policy_or_regulatory_score", "valuation_repricing_score", "execution_risk_score"], "component_delta_explanation": "Generic policy beta without a company-specific execution plan should be capped below positive Stage2-Actionable.", "MFE_90D_pct": 10.3, "MAE_90D_pct": -16.86, "score_return_alignment_label": "generic_low_pbr_policy_false_positive", "current_profile_verdict": "current_profile_false_positive"}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R11L12_C31_KEPCO_REGULATED_UTILITY_FAIL", "trigger_id": "TR_R11L12_KEPCO_VALUEUP_FALSEPOS_20240226", "symbol": "015760", "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "C31_POLICY_SUBSIDY_LEGISLATION_EVENT", "raw_component_scores_before": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 0, "revision_score": 10, "relative_strength_score": 46, "customer_quality_score": 0, "policy_or_regulatory_score": 68, "valuation_repricing_score": 50, "execution_risk_score": 60, "legal_or_contract_risk_score": 20, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 10, "direct_beneficiary_mapping_score": 0, "generic_low_pbr_theme_risk_score": 0, "state_regulated_discount_score": 0}, "weighted_score_before": 66, "stage_label_before": "Stage2-Actionable candidate under low-PBR policy beta", "raw_component_scores_after": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 0, "revision_score": 5, "relative_strength_score": 28, "customer_quality_score": 0, "policy_or_regulatory_score": 36, "valuation_repricing_score": 14, "execution_risk_score": 78, "legal_or_contract_risk_score": 28, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 10, "direct_beneficiary_mapping_score": 0, "generic_low_pbr_theme_risk_score": -12, "state_regulated_discount_score": -14}, "weighted_score_after": 45, "stage_label_after": "blocked_state_regulated_policy_theme", "changed_components": ["state_regulated_discount_score", "generic_low_pbr_theme_risk_score", "policy_or_regulatory_score", "execution_risk_score"], "component_delta_explanation": "Regulated public-utility low-PBR exposure should not pass C31 positive gates without tariff/earnings/capital-return confirmation.", "MFE_90D_pct": 5.17, "MAE_90D_pct": -21.45, "score_return_alignment_label": "regulated_utility_policy_false_positive", "current_profile_verdict": "current_profile_false_positive"}
```

### 25.5 shadow_weight rows
```csv
row_type,axis,scope,large_sector_id,canonical_archetype_id,baseline_value,tested_value,delta,reason,backtest_effect,trigger_ids,calibration_usable_count,new_independent_case_count,counterexample_count,confidence,proposal_type,notes
shadow_weight,C31_company_specific_valueup_execution_gate,canonical_archetype_specific,L10_POLICY_EVENT_CROSS_REDTEAM_MISC,C31_POLICY_SUBSIDY_LEGISLATION_EVENT,0,1,+1,"Promote policy event only when direct company-specific value-up execution route is visible","Improves separation of Shinhan/Hyundai from POSCO/KEPCO generic low-PBR theme",TR_R11L12_SHINHAN_VALUEUP_STAGE2_20240226|TR_R11L12_HYUNDAI_VALUEUP_STAGE2_20240226|TR_R11L12_WOORI_VALUEUP_STAGE2_20240226,5,5,2,medium,canonical_shadow_only,"not production; post-calibrated residual"
shadow_weight,C31_generic_low_pbr_policy_beta_cap,canonical_archetype_specific,L10_POLICY_EVENT_CROSS_REDTEAM_MISC,C31_POLICY_SUBSIDY_LEGISLATION_EVENT,0,1,+1,"Generic low-PBR value-up story without capital return/ROE repair should not promote positive stage","Blocks POSCO-style early bounce and heavy 180D MAE",TR_R11L12_POSCO_VALUEUP_FALSEPOS_20240226,5,5,2,medium,counterexample_guard,"not production; post-calibrated residual"
shadow_weight,C31_state_regulated_utility_discount_guard,sector_specific,L10_POLICY_EVENT_CROSS_REDTEAM_MISC,C31_POLICY_SUBSIDY_LEGISLATION_EVENT,0,1,+1,"State-regulated utility low-PBR route requires tariff/earnings confirmation before positive Stage2","Blocks KEPCO policy-beta false positive",TR_R11L12_KEPCO_VALUEUP_FALSEPOS_20240226,5,5,2,medium,sector_shadow_only,"not production; post-calibrated residual"
```

### 25.6 residual_contribution row
```jsonl
{"row_type": "residual_contribution", "round": "R11", "loop": "12", "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "C31_POLICY_SUBSIDY_LEGISLATION_EVENT", "scheduled_round": "R11", "scheduled_loop": "12", "round_schedule_status": "valid", "round_sector_consistency": "pass", "new_independent_case_count": 5, "reused_case_count": 0, "new_symbol_count": 5, "same_archetype_new_symbol_count": 5, "same_archetype_new_trigger_family_count": 5, "new_trigger_family_count": 5, "positive_case_count": 3, "counterexample_count": 2, "current_profile_error_count": 5, "tested_existing_calibrated_axes": ["stage2_actionable_evidence_bonus", "price_only_blowoff_blocks_positive_stage", "full_4b_requires_non_price_evidence", "hard_4c_thesis_break_routes_to_4c"], "residual_error_types_found": ["generic_low_pbr_policy_overcount", "direct_beneficiary_mapping_missing", "state_regulated_utility_false_positive", "high_MAE_policy_success_sizing"], "diversity_score_summary": "new_symbol=5; same_archetype_new_trigger_family=5; counterexample=2; residual_error=5; wrong_round_penalty=0; duplicate_penalty=0", "loop_contribution_label": "canonical_archetype_rule_candidate", "do_not_propose_new_weight_delta": false}
```

### 25.7 narrative_only rows
```jsonl
{"row_type": "narrative_only", "case_id": "R11L12_C31_NO_LIVE_SCAN", "symbol": "MULTI", "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "C31_POLICY_SUBSIDY_LEGISLATION_EVENT", "reason": "No 2026 current/live candidate discovery was performed; this is historical calibration only.", "price_source": "Songdaiki/stock-web", "usage": "not_weight_calibration"}
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
completed_loop = 12
next_round = R12
next_loop = 12
round_schedule_status = valid
round_sector_consistency = pass
```

## 28. Source Notes

- Price atlas manifest: `atlas/manifest.json` reports `source_name=FinanceData/marcap`, `price_adjustment_status=raw_unadjusted_marcap`, `max_date=2026-02-20`, `tradable_row_count=14354401`, `raw_row_count=15214118`, `symbol_count=5414`, and `calibration_shard_root=atlas/ohlcv_tradable_by_symbol_year`.
- Schema: `atlas/schema.json` defines tradable columns `d,o,h,l,c,v,a,mc,s,m`, calibration basis `tradable_raw`, and MFE/MAE formulas based on max high / min low over N tradable rows.
- Evidence source family: South Korea's Corporate Value-up Programme public coverage, including Reuters 2024-02-28 and Reuters 2024-03-14 follow-up coverage, plus FSC/KRX public programme materials. This MD uses those only as historical event evidence, not as live investment research.
- Stock-Web row anchors used: 055550 entry 2024-02-27 c=42000 and later high 2024-08-26 h=64600; 005380 entry 2024-02-27 c=238500 and peak 2024-06-28 h=299500; 316140 entry 2024-02-27 c=14940 and peak 2024-10-25 h=17100; 005490 entry 2024-02-27 c=427000 and drawdown low 2024-11-15 l=274000; 015760 entry 2024-02-27 c=24200 and drawdown low 2024-08-05 l=18190.

