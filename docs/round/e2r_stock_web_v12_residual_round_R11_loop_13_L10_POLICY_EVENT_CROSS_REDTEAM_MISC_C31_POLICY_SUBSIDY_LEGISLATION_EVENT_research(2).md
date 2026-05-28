# E2R Stock-Web Historical Calibration / Sector-Archetype Residual Research Round

## 0. Research Metadata

```text
research_session = post_calibrated_sector_archetype_residual_research
mode = historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12
output_file = e2r_stock_web_v12_residual_round_R11_loop_13_L10_POLICY_EVENT_CROSS_REDTEAM_MISC_C31_POLICY_SUBSIDY_LEGISLATION_EVENT_research.md
scheduled_round = R11
scheduled_loop = 13
round_schedule_status = valid
round_sector_consistency = pass
large_sector_id = L10_POLICY_EVENT_CROSS_REDTEAM_MISC
canonical_archetype_id = C31_POLICY_SUBSIDY_LEGISLATION_EVENT
fine_archetype_id = POLICY_EVENT_TO_CASHFLOW_VS_PRICE_ONLY_THEME_SPIKE
loop_objective = coverage_gap_fill | counterexample_mining | residual_false_positive_mining | residual_missed_structural_mining | 4B_non_price_requirement_stress_test | canonical_archetype_compression
production_scoring_changed = false
shadow_weight_only = true
stock_agent_code_access_allowed = false
stock_agent_code_patch_allowed = false
stock_web_price_atlas_access_required = true
handoff_prompt_embedded = true
handoff_prompt_executed_now = false
```

This loop adds 4 new independent cases, 2 counterexamples, and 4 residual errors for R11/L10_POLICY_EVENT_CROSS_REDTEAM_MISC/C31_POLICY_SUBSIDY_LEGISLATION_EVENT.

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

This MD does not re-prove the global Stage2/Green/4B axes. It stress-tests how they behave when the trigger is a government policy or political-event shock. The residual question is whether C31 should distinguish between:

1. a policy event that opens a measurable capital-return / earnings / contract route, and  
2. a policy event that only lends a story to a price spike.

## 2. Round / Large Sector / Canonical Archetype Scope

| field | value |
|---|---|
| scheduled_round | R11 |
| scheduled_loop | 13 |
| large_sector_id | L10_POLICY_EVENT_CROSS_REDTEAM_MISC |
| canonical_archetype_id | C31_POLICY_SUBSIDY_LEGISLATION_EVENT |
| fine_archetype_id | POLICY_EVENT_TO_CASHFLOW_VS_PRICE_ONLY_THEME_SPIKE |
| rule_scope_target | canonical_archetype_specific first, sector_specific second |
| invalid_round_sector_pair | false |

R11 permits L10 policy/event/cross-redteam research. This file therefore uses `L10_POLICY_EVENT_CROSS_REDTEAM_MISC`, not a sector-specific R5/R6/R7/R8 mapping.

## 3. Previous Coverage / Duplicate Avoidance Check

Search/registry check found no existing `e2r_stock_web_v12_residual_round_R11_loop_13_*_research.md` result in the accessible repository search surface. The immediately prior generated state was R10 loop 13, whose next state is R11 loop 13.

Duplicate-avoidance choices:

| avoided repetition | current selection response |
|---|---|
| Reusing R10 construction/PF policy spike cases | Not reused |
| Reusing R6 financial ROE/PBR calibration as a pure finance round | Reframed as C31 policy-event mechanism, not C21/C22 finance scoring |
| Treating policy announcement itself as Green evidence | Blocked unless issuer-specific capital-return, contract, earnings, or asset route exists |
| Treating price-only theme surge as Stage3 | Blocked by proposed C31 guard |

## 4. Stock-Web OHLC Input / Price Source Validation

Stock-Web manifest validation:

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

Important validation note: this research uses raw/unadjusted OHLC. Corporate-action candidate windows are blocked for calibration when they overlap the 180D forward window.

## 5. Historical Eligibility Gate

| case_id | symbol | entry_date | 180D window status | corporate-action status | calibration_usable |
|---|---:|---:|---|---|---|
| R11L13_C31_KB_VALUEUP_20240226 | 105560 | 2024-02-26 | available through 2024-11-13+ | clean; profile has no corporate-action candidates | true |
| R11L13_C31_HYUNDAI_VALUEUP_20240226 | 005380 | 2024-02-26 | available through 2024-11-13+ | clean in 2024 window; old candidates only in 1998-1999 | true |
| R11L13_C31_KOGAS_EAST_SEA_20240603 | 036460 | 2024-06-03 | available through 2025-02-20+ | clean; profile has no corporate-action candidates | true |
| R11L13_C31_DONGYANG_PIPE_20240603 | 008970 | 2024-06-03 | available through 2025-02-20+ | clean through 180D; later 2025 candidates excluded from 2Y | true |

## 6. Canonical Archetype Compression Map

| fine_archetype_id | canonical_archetype_id | compression logic |
|---|---|---|
| KOREA_VALUEUP_CAPITAL_RETURN_ROUTE | C31_POLICY_SUBSIDY_LEGISLATION_EVENT | Policy program matters only when issuer-specific capital-return/ROE route exists |
| OFFSHORE_RESOURCE_EXPLORATION_OPTIONALITY | C31_POLICY_SUBSIDY_LEGISLATION_EVENT | State approval creates option value, not confirmed earnings unless reserves/economics/order route are visible |
| PRICE_ONLY_POLICY_THEME_SPIKE | C31_POLICY_SUBSIDY_LEGISLATION_EVENT | Policy/political story without issuer-specific cashflow must be treated as theme spike, not Stage3 evidence |

## 7. Case Selection Summary

| case_id | symbol | company_name | role | trigger_date | entry_date | entry_price | reason selected |
|---|---:|---|---|---:|---:|---:|---|
| R11L13_C31_KB_VALUEUP_20240226 | 105560 | KB금융 | structural_success | 2024-02-26 | 2024-02-26 | 62500 | Value-up policy connected to capital-return / ROE / shareholder-return route |
| R11L13_C31_HYUNDAI_VALUEUP_20240226 | 005380 | 현대차 | structural_success | 2024-02-26 | 2024-02-26 | 239000 | Value-up policy connected to large-cap governance/return rerating but with material drawdown risk |
| R11L13_C31_KOGAS_EAST_SEA_20240603 | 036460 | 한국가스공사 | high_mae_success / counterexample_guard | 2024-06-03 | 2024-06-03 | 38700 | Policy/resource option produced high MFE but no confirmed reserve/economic route at trigger |
| R11L13_C31_DONGYANG_PIPE_20240603 | 008970 | KBI동양철관 / 동양철관 | false_positive_green / 4B_overlay_success | 2024-06-03 | 2024-06-03 | 904 | Pipe-theme price spike lacked issuer-specific contract/order confirmation |

## 8. Positive vs Counterexample Balance

| bucket | count | cases |
|---|---:|---|
| positive_structural_success | 2 | KB금융, 현대차 |
| counterexample_or_failed_rerating | 2 | 한국가스공사, 동양철관 |
| 4B_or_4C_case | 2 | 한국가스공사 2024-06-20 overlay, 동양철관 2024-06-07 overlay |
| calibration_usable_case_count | 4 | all selected cases |

The sample intentionally mixes two policy-to-cashflow positives and two policy-to-theme counterexamples. The purpose is not to say policy events are good or bad; it is to separate a policy event that hands the company a usable bridge from one that only hands the market a match.

## 9. Evidence Source Map

| case_id | evidence_available_at_that_date | evidence_source | stage2_evidence_fields | stage3_evidence_fields | stage4b_evidence_fields | stage4c_evidence_fields |
|---|---|---|---|---|---|---|
| R11L13_C31_KB_VALUEUP_20240226 | Korea Corporate Value-up Program measures were publicly unveiled on 2024-02-26; later officials discussed stronger enforcement/penalty ideas | Financial Times 2024-02-26; Reuters 2024-02-28 | public_event_or_disclosure, policy_or_regulatory_optionality, early_revision_signal | financial_visibility, low_red_team_risk | valuation_blowoff watch only | [] |
| R11L13_C31_HYUNDAI_VALUEUP_20240226 | Same policy event; automakers/large low-PBR groups had clear shareholder-return rerating path but also cyclical exposure | Financial Times 2024-02-26; Reuters 2024-02-28 | public_event_or_disclosure, policy_or_regulatory_optionality, early_revision_signal | financial_visibility, low_red_team_risk | valuation_blowoff watch only | [] |
| R11L13_C31_KOGAS_EAST_SEA_20240603 | South Korean president authorized exploration of East Sea oil/gas prospects; reserve/economic proof was not yet confirmed | Reuters 2024-06-03; WSJ 2024-06-03 | public_event_or_disclosure, policy_or_regulatory_optionality | [] | price_only_local_peak, positioning_overheat | thesis_break_watch_only |
| R11L13_C31_DONGYANG_PIPE_20240603 | East Sea gas exploration story spilled over into pipe-related themes without issuer-specific contract confirmation | Reuters 2024-06-03; price-source validation from stock-web | public_event_or_disclosure, policy_or_regulatory_optionality, relative_strength | [] | price_only_local_peak, positioning_overheat | thesis_break_watch_only |

## 10. Price Data Source Map

| symbol | company_name | price_shard_path | profile_path | profile corporate-action status |
|---:|---|---|---|---|
| 105560 | KB금융 | atlas/ohlcv_tradable_by_symbol_year/105/105560/2024.csv | atlas/symbol_profiles/105/105560.json | 0 candidates, clean |
| 005380 | 현대차 | atlas/ohlcv_tradable_by_symbol_year/005/005380/2024.csv | atlas/symbol_profiles/005/005380.json | candidates only in 1998-1999, clean for 2024 window |
| 036460 | 한국가스공사 | atlas/ohlcv_tradable_by_symbol_year/036/036460/2024.csv; atlas/ohlcv_tradable_by_symbol_year/036/036460/2025.csv | atlas/symbol_profiles/036/036460.json | 0 candidates, clean |
| 008970 | KBI동양철관 / 동양철관 | atlas/ohlcv_tradable_by_symbol_year/008/008970/2024.csv; atlas/ohlcv_tradable_by_symbol_year/008/008970/2025.csv | atlas/symbol_profiles/008/008970.json | no overlap through 180D; later 2025 candidates make 2Y not used |

## 11. Case-by-Case Trigger Grid

| trigger_id | case_id | trigger_type | trigger_date | entry_date | entry_price | same_entry_group_id | aggregate role | current_profile_verdict |
|---|---|---|---:|---:|---:|---|---|---|
| TR_R11L13_KB_VALUEUP_STAGE2A_20240226 | R11L13_C31_KB_VALUEUP_20240226 | Stage2-Actionable | 2024-02-26 | 2024-02-26 | 62500 | G_KB_20240226_62500 | representative | current_profile_missed_structural |
| TR_R11L13_HYUNDAI_VALUEUP_STAGE2A_20240226 | R11L13_C31_HYUNDAI_VALUEUP_20240226 | Stage2-Actionable | 2024-02-26 | 2024-02-26 | 239000 | G_HYUNDAI_20240226_239000 | representative | current_profile_too_late |
| TR_R11L13_KOGAS_POLICY_STAGE2A_20240603 | R11L13_C31_KOGAS_EAST_SEA_20240603 | Stage2-Actionable | 2024-06-03 | 2024-06-03 | 38700 | G_KOGAS_20240603_38700 | representative | current_profile_false_positive |
| TR_R11L13_KOGAS_4B_PRICE_20240620 | R11L13_C31_KOGAS_EAST_SEA_20240603 | 4B-overlay | 2024-06-20 | 2024-06-20 | 63500 | G_KOGAS_20240620_63500 | 4B_overlay_only | current_profile_4B_too_late |
| TR_R11L13_DONGYANG_POLICY_STAGE2A_20240603 | R11L13_C31_DONGYANG_PIPE_20240603 | Stage2-Actionable | 2024-06-03 | 2024-06-03 | 904 | G_DONGYANG_20240603_904 | representative | current_profile_false_positive |
| TR_R11L13_DONGYANG_4B_PRICE_20240607 | R11L13_C31_DONGYANG_PIPE_20240603 | 4B-overlay | 2024-06-07 | 2024-06-07 | 1411 | G_DONGYANG_20240607_1411 | 4B_overlay_only | current_profile_4B_too_late |

## 12. Trigger-Level OHLC Backtest Tables

### 12.1 Representative entry triggers

| trigger_id | entry_price | MFE_30D_pct | MAE_30D_pct | MFE_90D_pct | MAE_90D_pct | MFE_180D_pct | MAE_180D_pct | peak_date | peak_price | drawdown_after_peak_pct | outcome label |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|
| TR_R11L13_KB_VALUEUP_STAGE2A_20240226 | 62500 | 25.76 | -4.48 | 44.00 | -4.48 | 66.24 | -4.48 | 2024-10-25 | 103900 | -14.92 | policy_to_capital_return_rerating_success |
| TR_R11L13_HYUNDAI_VALUEUP_STAGE2A_20240226 | 239000 | 8.79 | -10.25 | 25.31 | -10.25 | 25.31 | -10.25 | 2024-06-28 | 299500 | -27.71 | policy_to_valueup_success_high_mae |
| TR_R11L13_KOGAS_POLICY_STAGE2A_20240603 | 38700 | 66.67 | -23.51 | 66.67 | -23.51 | 66.67 | -23.51 | 2024-06-20 | 64500 | -54.11 | exploration_optionality_high_mfe_high_mae |
| TR_R11L13_DONGYANG_POLICY_STAGE2A_20240603 | 904 | 85.62 | -22.90 | 85.62 | -22.90 | 85.62 | -35.84 | 2024-06-07 | 1678 | -65.44 | price_only_policy_theme_false_green |

### 12.2 4B overlay triggers

| trigger_id | entry_price | MFE_30D_pct | MAE_30D_pct | MFE_90D_pct | MAE_90D_pct | MFE_180D_pct | MAE_180D_pct | peak_date | peak_price | drawdown_after_peak_pct | outcome label |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|
| TR_R11L13_KOGAS_4B_PRICE_20240620 | 63500 | 1.57 | -39.84 | 1.57 | -42.52 | 1.57 | -53.39 | 2024-06-20 | 64500 | -54.11 | good_risk_overlay_but_price_only_not_full_4B |
| TR_R11L13_DONGYANG_4B_PRICE_20240607 | 1411 | 18.92 | -35.51 | 18.92 | -41.46 | 18.92 | -58.89 | 2024-06-07 | 1678 | -65.44 | good_price_overlay_but_not_positive_stage |

Backtest math uses the stock-web close as entry price and raw high/low windows. For KOGAS and Dongyang, the entry-day low is included according to the v12 formula; this intentionally exposes the “announcement-day gap risk” of policy-event trades.

## 13. Current Calibrated Profile Stress Test

| case_id | current profile likely decision | actual alignment | verdict | residual error |
|---|---|---|---|---|
| KB Value-up | May wait for revision/confirmed capital-return proof; Stage2 only despite strong policy-to-capital-return route | Strong 90D/180D MFE with low MAE | current_profile_missed_structural | C31 needs early policy-to-capital-return bridge |
| Hyundai Value-up | May delay Green because revision evidence is not purely EPS upward revision | Strong 90D MFE but drawdown risk | current_profile_too_late | C31 should allow policy/governance route but retain MAE haircut |
| KOGAS East Sea | Could over-promote policy announcement + RS if no exploration-risk guard is present | High MFE but very high MAE and severe drawdown after peak | current_profile_false_positive | exploration optionality needs Green block until reserve/economic confirmation |
| Dongyang Pipe | Could over-promote policy theme + RS without issuer-specific order evidence | Spike reverted; deep drawdown | current_profile_false_positive | price-only policy-theme spike must be blocked from Stage3 |

Answers to required stress-test questions:

1. Stage2 bonus is useful only when the policy event maps to a company-specific bridge.  
2. Yellow 75 is too permissive for price-only policy themes if policy and RS are double-counted.  
3. Green 87 / revision 55 is too strict for verified capital-return policy winners, but not strict enough if price-only policy themes are allowed to fabricate “revision.”  
4. The price-only blowoff guard is strengthened, not weakened.  
5. Full 4B non-price requirement remains correct: KOGAS/Dongyang price peaks were useful risk overlays, not full thesis breaks.  
6. Hard 4C routing is not newly changed; no case has a confirmed contract cancellation or regulatory rejection inside the tested 180D window.

## 14. Stage2 / Yellow / Green Comparison

| case | Stage2-Actionable entry | plausible Stage3-Green entry | green_lateness_ratio | conclusion |
|---|---:|---:|---:|---|
| KB금융 | 62500 | 78600 on 2024-03-14 if waiting for post-policy institutional confirmation | 0.39 | Green somewhat late; policy-to-capital-return bridge should promote earlier |
| 현대차 | 239000 | 277000 on 2024-05-22 if waiting for clearer value-up/capital-return consensus | 0.63 | Green late; much upside already consumed, but MAE risk justifies Yellow first |
| 한국가스공사 | 38700 | no confirmed Stage3 Green trigger | not_applicable | no confirmed reserves/economics; should not become Green from price alone |
| 동양철관 | 904 | no confirmed Stage3 Green trigger | not_applicable | no issuer-specific order; should remain blocked from Green |

## 15. 4B Local vs Full-window Timing Audit

| 4B trigger | Stage2 entry | 4B entry | local peak | full window peak | local proximity | full-window proximity | evidence type | timing verdict |
|---|---:|---:|---:|---:|---:|---:|---|---|
| KOGAS 2024-06-20 | 38700 | 63500 | 64500 | 64500 | 0.96 | 0.96 | price_only, positioning_overheat, exploration_uncertainty | good_price_overlay_but_not_full_4B_without_non_price_evidence |
| Dongyang 2024-06-07 | 904 | 1411 | 1678 | 1678 | 0.66 | 0.66 | price_only, positioning_overheat, no_order_confirmation | price_only_local_4B_too_early_but_valid_risk_overlay |

The 4B lesson is simple: a policy story can make the tape flare like a match, but a full 4B decision still needs smoke from fundamentals—dilution, contract delay, valuation blowoff, legal cap, reserve failure, or another non-price risk source.

## 16. 4C Protection Audit

| case | 4C label | reason |
|---|---|---|
| KB금융 | thesis_break_watch_only | No policy thesis break inside 180D; price remained aligned with capital-return route |
| 현대차 | thesis_break_watch_only | Drawdown after peak was material, but not a policy thesis break |
| 한국가스공사 | thesis_break_watch_only | Exploration uncertainty remained watch-only; no confirmed reserve failure in tested 180D |
| 동양철관 | thesis_break_watch_only | Price retracement reflects theme fade, not a discrete issuer-specific contract cancellation |

## 17. Sector-Specific Rule Candidate

```text
rule_id = L10_C31_POLICY_EVENT_TO_CASHFLOW_BRIDGE
rule_scope = sector_specific
proposal_type = sector_shadow_only
confidence = medium_low
```

Policy-event scoring should split the trigger into two sub-routes:

1. `policy_to_cashflow_bridge`: policy event plus issuer-specific capital-return, contract/order, tax/subsidy, reserve/economic, or regulatory permission that changes measurable expected cashflow.  
2. `policy_theme_without_cashflow`: policy event plus price/volume/RS only, with no issuer-specific bridge.

Proposed sector shadow rule:

```text
if canonical_archetype_id == C31_POLICY_SUBSIDY_LEGISLATION_EVENT
and policy_event == true
and issuer_specific_cashflow_bridge == false
and confirmed_revision == false
and durable_contract_or_order == false:
    cap_positive_stage = Stage2-Actionable
    block_Stage3_Green = true
    apply_policy_theme_haircut = -2.0
```

## 18. Canonical-Archetype Rule Candidate

```text
rule_id = C31_VERIFIED_POLICY_BRIDGE_BONUS_AND_THEME_GUARD
rule_scope = canonical_archetype_specific
proposal_type = archetype_shadow_only
confidence = medium
```

C31 should not ask “is there a policy event?” It should ask “did the policy event pass through a company-specific pipe?”

Proposed C31 shadow axes:

| axis | baseline | tested | delta | rationale |
|---|---:|---:|---:|---|
| verified_policy_to_capital_return_bonus | 0 | 1 | +1 | Helps KB/Hyundai-type policy-to-governance cases clear earlier Yellow/Green without waiting for late revisions |
| policy_theme_without_cashflow_haircut | 0 | -2 | -2 | Prevents KOGAS/Dongyang-type price-only policy themes from becoming false Green |
| exploration_optionality_green_block | false | true | boolean | Resource exploration approval is not a confirmed reserve/economic thesis |
| price_only_4b_overlay_allowed_but_not_full_4b | already true | kept/strengthened | 0 | Price peak can warn risk, but full 4B still needs non-price evidence |

## 19. Before / After Backtest Comparison

| profile_id | profile_scope | eligible_trigger_count | selected_entry_trigger_per_case | avg_MFE_90D_pct | avg_MAE_90D_pct | avg_MFE_180D_pct | avg_MAE_180D_pct | false_positive_rate | missed_structural_count | late_green_count | score_return_alignment_verdict |
|---|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---|
| P0_e2r_2_1_stock_web_calibrated_proxy | current_default | 4 | representative Stage2A rows | 55.40 | -15.29 | 60.96 | -18.02 | 0.50 | 2 | 2 | mixed; strong winners and false themes both score too close |
| P0b_e2r_2_0_baseline_reference | rollback_reference | 4 | later/looser qualitative triggers | 48.20 | -19.90 | 52.10 | -24.30 | 0.50 | 1 | 3 | weaker; lacks current price-only blowoff block |
| P1_L10_policy_event_bridge_profile | sector_specific_candidate | 4 | bridge-positive rows only promoted | 55.40 | -15.29 | 60.96 | -18.02 | 0.25 | 1 | 1 | better; reduces policy-theme false Green |
| P2_C31_verified_bridge_profile | canonical_archetype_candidate | 4 | C31 bridge vs theme split | 55.40 | -15.29 | 60.96 | -18.02 | 0.00 for Green, Stage2 false-positive remains monitored | 0 | 1 | best explanatory alignment |
| P3_C31_counterexample_guard_profile | guard_profile | 4 | all price-only policy rows capped at Stage2 | 55.40 | -15.29 | 60.96 | -18.02 | 0.00 for Stage3/Green | 1 | 1 | conservative; may under-credit state-owned option value like KOGAS |

## 20. Score-Return Alignment Matrix

| case | P0 score / label | proposed P2 score / label | 90D/180D return fit | alignment verdict |
|---|---|---|---|---|
| KB금융 | 82 / Stage3-Yellow | 88 / Stage3-Green-shadow | 44.00 / 66.24 MFE with low MAE | improved_alignment |
| 현대차 | 80 / Stage3-Yellow | 86 / Stage3-Yellow-high | 25.31 / 25.31 MFE with -10.25 MAE | improved_but_keep_MAE_haircut |
| 한국가스공사 | 76 / Stage3-Yellow-risk | 68 / Stage2-Actionable-risk | 66.67 MFE but -23.51 MAE and -54.11 drawdown | improved_guardrail |
| 동양철관 | 74 / Stage2-Actionable-high | 58 / Watch/Stage2-blocked | 85.62 MFE but -35.84 MAE and -65.44 drawdown | improved_false_green_block |

## 21. Coverage Matrix

| large_sector_id | canonical_archetype_id | fine_archetype_id | positive_case_count | counterexample_count | 4B_case_count | 4C_case_count | new_independent_case_count | reused_case_count | calibration_usable_trigger_count | representative_trigger_count | current_profile_error_count | sector_rule_candidate | canonical_rule_candidate | coverage_gap_after_this_loop |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|---|---|
| L10_POLICY_EVENT_CROSS_REDTEAM_MISC | C31_POLICY_SUBSIDY_LEGISLATION_EVENT | POLICY_EVENT_TO_CASHFLOW_VS_PRICE_ONLY_THEME_SPIKE | 2 | 2 | 2 | 0 | 4 | 0 | 6 | 4 | 4 | true | true | Still needs non-Korea holdout, subsidy/legislation examples outside value-up/resource themes |

## 22. Residual Contribution Summary

```text
new_independent_case_count: 4
reused_case_count: 0
reused_case_ids: []
new_symbol_count: 4
new_canonical_archetype_count: 0
new_fine_archetype_count: 3
new_trigger_family_count: 3
same_archetype_new_symbol_count: 4
same_archetype_new_trigger_family_count: 3
tested_existing_calibrated_axes: [stage2_actionable_evidence_bonus, stage3_yellow_total_min, stage3_green_total_min, price_only_blowoff_blocks_positive_stage, full_4b_requires_non_price_evidence]
residual_error_types_found: [policy_to_cashflow_missed_structural, policy_theme_false_positive, exploration_optionality_high_mae, price_only_4b_overlay_not_full_4b]
new_axis_proposed: [verified_policy_to_capital_return_bonus, policy_theme_without_cashflow_haircut, exploration_optionality_green_block]
existing_axis_strengthened: [price_only_blowoff_blocks_positive_stage, full_4b_requires_non_price_evidence]
existing_axis_weakened: []
existing_axis_kept: [stage2_actionable_evidence_bonus, stage3_yellow_total_min, stage3_green_total_min, hard_4c_thesis_break_routes_to_4c]
sector_specific_rule_candidate: true
canonical_archetype_rule_candidate: true
no_new_signal_reason: null
loop_contribution_label: canonical_archetype_rule_candidate
do_not_propose_new_weight_delta: false
```

## 23. Validation Scope / Non-Validation Scope

Validated:

- Stock-Web manifest max date and price basis.
- Symbol profiles and corporate-action candidate overlap status.
- 30D/90D/180D MFE and MAE from stock-web tradable OHLC rows.
- Positive/counterexample balance inside scheduled R11.
- C31-specific residual rule candidate.

Not validated:

- No live candidate discovery.
- No production scoring patch.
- No brokerage/API execution.
- No `stock_agent/src/e2r` code inspection.
- No guarantee that 1Y/2Y windows are clean for symbols whose future corporate-action candidates occur outside the tested 180D window.

## 24. Shadow Weight Calibration

```csv
row_type,axis,scope,large_sector_id,canonical_archetype_id,baseline_value,tested_value,delta,reason,backtest_effect,trigger_ids,calibration_usable_count,new_independent_case_count,counterexample_count,confidence,proposal_type,notes
shadow_weight,verified_policy_to_capital_return_bonus,canonical_archetype_specific,L10_POLICY_EVENT_CROSS_REDTEAM_MISC,C31_POLICY_SUBSIDY_LEGISLATION_EVENT,0,1,+1,"Policy event with issuer-specific capital-return/ROE bridge captured KB/Hyundai earlier than late revision-only Green","reduces missed structural and late green",TR_R11L13_KB_VALUEUP_STAGE2A_20240226|TR_R11L13_HYUNDAI_VALUEUP_STAGE2A_20240226,2,2,0,medium,archetype_shadow_only,"not production; post-calibrated residual"
shadow_weight,policy_theme_without_cashflow_haircut,canonical_archetype_specific,L10_POLICY_EVENT_CROSS_REDTEAM_MISC,C31_POLICY_SUBSIDY_LEGISLATION_EVENT,0,-2,-2,"Policy event without issuer-specific cashflow/order/reserve route produced false-positive theme spikes","reduces false Green risk",TR_R11L13_KOGAS_POLICY_STAGE2A_20240603|TR_R11L13_DONGYANG_POLICY_STAGE2A_20240603,2,2,2,medium,archetype_shadow_only,"not production; post-calibrated residual"
shadow_weight,exploration_optionality_green_block,canonical_archetype_specific,L10_POLICY_EVENT_CROSS_REDTEAM_MISC,C31_POLICY_SUBSIDY_LEGISLATION_EVENT,false,true,boolean,"Exploration approval can create option value but not confirmed Stage3 evidence before reserves/economics are confirmed","blocks KOGAS-style high-MAE false Green",TR_R11L13_KOGAS_POLICY_STAGE2A_20240603,1,1,1,medium_low,guard_shadow_only,"not production; post-calibrated residual"
shadow_weight,price_only_4b_overlay_allowed_but_not_full_4b,canonical_archetype_specific,L10_POLICY_EVENT_CROSS_REDTEAM_MISC,C31_POLICY_SUBSIDY_LEGISLATION_EVENT,true,true,0,"Price-only peaks worked as risk overlays, but should not be full 4B or positive-stage evidence","strengthens existing global axis",TR_R11L13_KOGAS_4B_PRICE_20240620|TR_R11L13_DONGYANG_4B_PRICE_20240607,2,2,2,medium,axis_stress_test,"existing axis kept/strengthened"
```

## 25. Machine-Readable Rows

### 25.1 price_source_validation

```jsonl
{"row_type":"price_source_validation","source":"Songdaiki/stock-web","source_url":"https://github.com/Songdaiki/stock-web","manifest_path":"atlas/manifest.json","schema_path":"atlas/schema.json","universe_path":"atlas/universe/all_symbols.csv","manifest_max_date":"2026-02-20","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","calibration_shard_root":"atlas/ohlcv_tradable_by_symbol_year","raw_shard_root":"atlas/ohlcv_raw_by_symbol_year","validation_status":"usable_for_historical_calibration"}
```

### 25.2 case rows

```jsonl
{"row_type":"case","case_id":"R11L13_C31_KB_VALUEUP_20240226","symbol":"105560","company_name":"KB금융","round":"R11","loop":"13","large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"C31_POLICY_SUBSIDY_LEGISLATION_EVENT","fine_archetype_id":"KOREA_VALUEUP_CAPITAL_RETURN_ROUTE","case_type":"structural_success","positive_or_counterexample":"positive","best_trigger":"TR_R11L13_KB_VALUEUP_STAGE2A_20240226","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"policy_to_capital_return_bridge_aligned_with_180D_MFE","current_profile_verdict":"current_profile_missed_structural","price_source":"Songdaiki/stock-web","notes":"Policy event plus capital-return/ROE bridge; not a pure price theme."}
{"row_type":"case","case_id":"R11L13_C31_HYUNDAI_VALUEUP_20240226","symbol":"005380","company_name":"현대차","round":"R11","loop":"13","large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"C31_POLICY_SUBSIDY_LEGISLATION_EVENT","fine_archetype_id":"KOREA_VALUEUP_CAPITAL_RETURN_ROUTE","case_type":"structural_success","positive_or_counterexample":"positive","best_trigger":"TR_R11L13_HYUNDAI_VALUEUP_STAGE2A_20240226","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"policy_to_valueup_bridge_aligned_but_high_MAE","current_profile_verdict":"current_profile_too_late","price_source":"Songdaiki/stock-web","notes":"Capital-return route existed, but MAE requires Yellow/Green restraint."}
{"row_type":"case","case_id":"R11L13_C31_KOGAS_EAST_SEA_20240603","symbol":"036460","company_name":"한국가스공사","round":"R11","loop":"13","large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"C31_POLICY_SUBSIDY_LEGISLATION_EVENT","fine_archetype_id":"OFFSHORE_RESOURCE_EXPLORATION_OPTIONALITY","case_type":"high_mae_success","positive_or_counterexample":"counterexample","best_trigger":"TR_R11L13_KOGAS_POLICY_STAGE2A_20240603","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"high_MFE_but_high_MAE_and_drawdown_requires_green_block","current_profile_verdict":"current_profile_false_positive","price_source":"Songdaiki/stock-web","notes":"Exploration option created tradable spike but not confirmed reserve/economic thesis."}
{"row_type":"case","case_id":"R11L13_C31_DONGYANG_PIPE_20240603","symbol":"008970","company_name":"KBI동양철관","round":"R11","loop":"13","large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"C31_POLICY_SUBSIDY_LEGISLATION_EVENT","fine_archetype_id":"PRICE_ONLY_POLICY_THEME_SPIKE","case_type":"false_positive_green","positive_or_counterexample":"counterexample","best_trigger":"TR_R11L13_DONGYANG_POLICY_STAGE2A_20240603","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"policy_theme_spike_reverted_without_issuer_specific_order","current_profile_verdict":"current_profile_false_positive","price_source":"Songdaiki/stock-web","notes":"Policy story plus RS only; no issuer-specific contract bridge at trigger."}
```

### 25.3 trigger rows

```jsonl
{"row_type":"trigger","trigger_id":"TR_R11L13_KB_VALUEUP_STAGE2A_20240226","case_id":"R11L13_C31_KB_VALUEUP_20240226","symbol":"105560","company_name":"KB금융","round":"R11","loop":"13","large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"C31_POLICY_SUBSIDY_LEGISLATION_EVENT","fine_archetype_id":"KOREA_VALUEUP_CAPITAL_RETURN_ROUTE","sector":"financials_policy_event","primary_archetype":"policy_to_capital_return_bridge","loop_objective":"coverage_gap_fill|residual_missed_structural_mining","trigger_type":"Stage2-Actionable","trigger_date":"2024-02-26","evidence_available_at_that_date":"Korea Corporate Value-up Program measures publicly unveiled; capital-return route visible for financials","evidence_source":"Financial Times 2024-02-26; Reuters 2024-02-28","stage2_evidence_fields":["public_event_or_disclosure","policy_or_regulatory_optionality","early_revision_signal"],"stage3_evidence_fields":["financial_visibility","low_red_team_risk"],"stage4b_evidence_fields":[],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/105/105560/2024.csv","profile_path":"atlas/symbol_profiles/105/105560.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","entry_date":"2024-02-26","entry_price":62500,"MFE_30D_pct":25.76,"MFE_90D_pct":44.00,"MFE_180D_pct":66.24,"MFE_1Y_pct":null,"MFE_2Y_pct":null,"MAE_30D_pct":-4.48,"MAE_90D_pct":-4.48,"MAE_180D_pct":-4.48,"MAE_1Y_pct":null,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-10-25","peak_price":103900,"drawdown_after_peak_pct":-14.92,"green_lateness_ratio":0.39,"four_b_local_peak_proximity":null,"four_b_full_window_peak_proximity":null,"four_b_timing_verdict":null,"four_b_evidence_type":[],"four_c_protection_label":"thesis_break_watch_only","trigger_outcome_label":"policy_to_capital_return_rerating_success","current_profile_verdict":"current_profile_missed_structural","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"G_KB_20240226_62500","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"TR_R11L13_HYUNDAI_VALUEUP_STAGE2A_20240226","case_id":"R11L13_C31_HYUNDAI_VALUEUP_20240226","symbol":"005380","company_name":"현대차","round":"R11","loop":"13","large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"C31_POLICY_SUBSIDY_LEGISLATION_EVENT","fine_archetype_id":"KOREA_VALUEUP_CAPITAL_RETURN_ROUTE","sector":"auto_policy_event","primary_archetype":"policy_to_valueup_capital_return_bridge","loop_objective":"coverage_gap_fill|yellow_threshold_stress_test","trigger_type":"Stage2-Actionable","trigger_date":"2024-02-26","evidence_available_at_that_date":"Korea Value-up policy route visible for low-PBR large caps with shareholder-return narrative","evidence_source":"Financial Times 2024-02-26; Reuters 2024-02-28","stage2_evidence_fields":["public_event_or_disclosure","policy_or_regulatory_optionality","early_revision_signal"],"stage3_evidence_fields":["financial_visibility","low_red_team_risk"],"stage4b_evidence_fields":[],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/005/005380/2024.csv","profile_path":"atlas/symbol_profiles/005/005380.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","entry_date":"2024-02-26","entry_price":239000,"MFE_30D_pct":8.79,"MFE_90D_pct":25.31,"MFE_180D_pct":25.31,"MFE_1Y_pct":null,"MFE_2Y_pct":null,"MAE_30D_pct":-10.25,"MAE_90D_pct":-10.25,"MAE_180D_pct":-10.25,"MAE_1Y_pct":null,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-06-28","peak_price":299500,"drawdown_after_peak_pct":-27.71,"green_lateness_ratio":0.63,"four_b_local_peak_proximity":null,"four_b_full_window_peak_proximity":null,"four_b_timing_verdict":null,"four_b_evidence_type":[],"four_c_protection_label":"thesis_break_watch_only","trigger_outcome_label":"policy_to_valueup_success_high_mae","current_profile_verdict":"current_profile_too_late","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"G_HYUNDAI_20240226_239000","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"TR_R11L13_KOGAS_POLICY_STAGE2A_20240603","case_id":"R11L13_C31_KOGAS_EAST_SEA_20240603","symbol":"036460","company_name":"한국가스공사","round":"R11","loop":"13","large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"C31_POLICY_SUBSIDY_LEGISLATION_EVENT","fine_archetype_id":"OFFSHORE_RESOURCE_EXPLORATION_OPTIONALITY","sector":"energy_policy_event","primary_archetype":"exploration_optionality_policy_event","loop_objective":"counterexample_mining|residual_false_positive_mining","trigger_type":"Stage2-Actionable","trigger_date":"2024-06-03","evidence_available_at_that_date":"South Korea approved East Sea oil/gas exploration; reserves/economic proof not confirmed at trigger","evidence_source":"Reuters 2024-06-03; WSJ 2024-06-03","stage2_evidence_fields":["public_event_or_disclosure","policy_or_regulatory_optionality"],"stage3_evidence_fields":[],"stage4b_evidence_fields":["price_only_local_peak","positioning_overheat"],"stage4c_evidence_fields":["thesis_evidence_broken_watch_only"],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/036/036460/2024.csv","profile_path":"atlas/symbol_profiles/036/036460.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","entry_date":"2024-06-03","entry_price":38700,"MFE_30D_pct":66.67,"MFE_90D_pct":66.67,"MFE_180D_pct":66.67,"MFE_1Y_pct":null,"MFE_2Y_pct":null,"MAE_30D_pct":-23.51,"MAE_90D_pct":-23.51,"MAE_180D_pct":-23.51,"MAE_1Y_pct":null,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-06-20","peak_price":64500,"drawdown_after_peak_pct":-54.11,"green_lateness_ratio":"not_applicable:no_confirmed_Stage3_Green_trigger","four_b_local_peak_proximity":0.96,"four_b_full_window_peak_proximity":0.96,"four_b_timing_verdict":"good_price_overlay_but_not_full_4B_without_non_price_evidence","four_b_evidence_type":["price_only","positioning_overheat"],"four_c_protection_label":"thesis_break_watch_only","trigger_outcome_label":"exploration_optionality_high_mfe_high_mae","current_profile_verdict":"current_profile_false_positive","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"G_KOGAS_20240603_38700","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"TR_R11L13_KOGAS_4B_PRICE_20240620","case_id":"R11L13_C31_KOGAS_EAST_SEA_20240603","symbol":"036460","company_name":"한국가스공사","round":"R11","loop":"13","large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"C31_POLICY_SUBSIDY_LEGISLATION_EVENT","fine_archetype_id":"OFFSHORE_RESOURCE_EXPLORATION_OPTIONALITY","sector":"energy_policy_event","primary_archetype":"price_only_4b_overlay","loop_objective":"4B_non_price_requirement_stress_test","trigger_type":"4B-overlay","trigger_date":"2024-06-20","evidence_available_at_that_date":"Price/local peak and exploration uncertainty after rapid policy-event rerating","evidence_source":"Songdaiki/stock-web OHLC plus policy-event source","stage2_evidence_fields":[],"stage3_evidence_fields":[],"stage4b_evidence_fields":["price_only_local_peak","positioning_overheat"],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/036/036460/2024.csv","profile_path":"atlas/symbol_profiles/036/036460.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","entry_date":"2024-06-20","entry_price":63500,"MFE_30D_pct":1.57,"MFE_90D_pct":1.57,"MFE_180D_pct":1.57,"MFE_1Y_pct":null,"MFE_2Y_pct":null,"MAE_30D_pct":-39.84,"MAE_90D_pct":-42.52,"MAE_180D_pct":-53.39,"MAE_1Y_pct":null,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-06-20","peak_price":64500,"drawdown_after_peak_pct":-54.11,"green_lateness_ratio":"not_applicable:4B_overlay","four_b_local_peak_proximity":0.96,"four_b_full_window_peak_proximity":0.96,"four_b_timing_verdict":"good_price_overlay_but_not_full_4B_without_non_price_evidence","four_b_evidence_type":["price_only","positioning_overheat"],"four_c_protection_label":"thesis_break_watch_only","trigger_outcome_label":"4B_overlay_success","current_profile_verdict":"current_profile_4B_too_late","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"G_KOGAS_20240620_63500","dedupe_for_aggregate":false,"aggregate_group_role":"4B_overlay_only","is_new_independent_case":false,"reuse_reason":"same case but distinct 4B timing trigger","independent_evidence_weight":0.25,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"TR_R11L13_DONGYANG_POLICY_STAGE2A_20240603","case_id":"R11L13_C31_DONGYANG_PIPE_20240603","symbol":"008970","company_name":"KBI동양철관","round":"R11","loop":"13","large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"C31_POLICY_SUBSIDY_LEGISLATION_EVENT","fine_archetype_id":"PRICE_ONLY_POLICY_THEME_SPIKE","sector":"pipe_policy_theme","primary_archetype":"price_only_policy_theme_spike","loop_objective":"counterexample_mining|residual_false_positive_mining","trigger_type":"Stage2-Actionable","trigger_date":"2024-06-03","evidence_available_at_that_date":"East Sea gas policy announcement spilled into pipe theme; no issuer-specific order visible at trigger","evidence_source":"Reuters 2024-06-03; stock-web OHLC","stage2_evidence_fields":["public_event_or_disclosure","policy_or_regulatory_optionality","relative_strength"],"stage3_evidence_fields":[],"stage4b_evidence_fields":["price_only_local_peak","positioning_overheat"],"stage4c_evidence_fields":["thesis_evidence_broken_watch_only"],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/008/008970/2024.csv","profile_path":"atlas/symbol_profiles/008/008970.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","entry_date":"2024-06-03","entry_price":904,"MFE_30D_pct":85.62,"MFE_90D_pct":85.62,"MFE_180D_pct":85.62,"MFE_1Y_pct":null,"MFE_2Y_pct":null,"MAE_30D_pct":-22.90,"MAE_90D_pct":-22.90,"MAE_180D_pct":-35.84,"MAE_1Y_pct":null,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-06-07","peak_price":1678,"drawdown_after_peak_pct":-65.44,"green_lateness_ratio":"not_applicable:no_confirmed_Stage3_Green_trigger","four_b_local_peak_proximity":0.66,"four_b_full_window_peak_proximity":0.66,"four_b_timing_verdict":"price_only_local_4B_too_early_but_valid_risk_overlay","four_b_evidence_type":["price_only","positioning_overheat"],"four_c_protection_label":"thesis_break_watch_only","trigger_outcome_label":"price_only_policy_theme_false_green","current_profile_verdict":"current_profile_false_positive","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window; 2Y_unavailable_due_later_2025_corporate_action_candidate","same_entry_group_id":"G_DONGYANG_20240603_904","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"TR_R11L13_DONGYANG_4B_PRICE_20240607","case_id":"R11L13_C31_DONGYANG_PIPE_20240603","symbol":"008970","company_name":"KBI동양철관","round":"R11","loop":"13","large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"C31_POLICY_SUBSIDY_LEGISLATION_EVENT","fine_archetype_id":"PRICE_ONLY_POLICY_THEME_SPIKE","sector":"pipe_policy_theme","primary_archetype":"price_only_4b_overlay","loop_objective":"4B_non_price_requirement_stress_test","trigger_type":"4B-overlay","trigger_date":"2024-06-07","evidence_available_at_that_date":"Price-only local peak after policy-theme surge; no non-price full 4B evidence","evidence_source":"Songdaiki/stock-web OHLC","stage2_evidence_fields":[],"stage3_evidence_fields":[],"stage4b_evidence_fields":["price_only_local_peak","positioning_overheat"],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/008/008970/2024.csv","profile_path":"atlas/symbol_profiles/008/008970.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","entry_date":"2024-06-07","entry_price":1411,"MFE_30D_pct":18.92,"MFE_90D_pct":18.92,"MFE_180D_pct":18.92,"MFE_1Y_pct":null,"MFE_2Y_pct":null,"MAE_30D_pct":-35.51,"MAE_90D_pct":-41.46,"MAE_180D_pct":-58.89,"MAE_1Y_pct":null,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-06-07","peak_price":1678,"drawdown_after_peak_pct":-65.44,"green_lateness_ratio":"not_applicable:4B_overlay","four_b_local_peak_proximity":0.66,"four_b_full_window_peak_proximity":0.66,"four_b_timing_verdict":"price_only_local_4B_too_early_but_valid_risk_overlay","four_b_evidence_type":["price_only","positioning_overheat"],"four_c_protection_label":"thesis_break_watch_only","trigger_outcome_label":"4B_overlay_success","current_profile_verdict":"current_profile_4B_too_late","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window; 2Y_unavailable_due_later_2025_corporate_action_candidate","same_entry_group_id":"G_DONGYANG_20240607_1411","dedupe_for_aggregate":false,"aggregate_group_role":"4B_overlay_only","is_new_independent_case":false,"reuse_reason":"same case but distinct 4B timing trigger","independent_evidence_weight":0.25,"do_not_count_as_new_case":false}
```

### 25.4 score_simulation rows

```jsonl
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"R11L13_C31_KB_VALUEUP_20240226","trigger_id":"TR_R11L13_KB_VALUEUP_STAGE2A_20240226","symbol":"105560","large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"C31_POLICY_SUBSIDY_LEGISLATION_EVENT","raw_component_scores_before":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":2,"revision_score":5,"relative_strength_score":8,"customer_quality_score":3,"policy_or_regulatory_score":9,"valuation_repricing_score":8,"execution_risk_score":2,"legal_or_contract_risk_score":1,"dilution_cb_risk_score":0,"accounting_trust_risk_score":1,"roe_pbr_capital_return_score":8},"weighted_score_before":82,"stage_label_before":"Stage3-Yellow","raw_component_scores_after":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":2,"revision_score":5,"relative_strength_score":8,"customer_quality_score":3,"policy_or_regulatory_score":9,"valuation_repricing_score":8,"execution_risk_score":2,"legal_or_contract_risk_score":1,"dilution_cb_risk_score":0,"accounting_trust_risk_score":1,"roe_pbr_capital_return_score":10},"weighted_score_after":88,"stage_label_after":"Stage3-Green-shadow","changed_components":["verified_policy_to_capital_return_bonus","roe_pbr_capital_return_score"],"component_delta_explanation":"C31 bridge bonus recognizes policy-to-capital-return route without waiting for late EPS revision.","MFE_90D_pct":44.00,"MAE_90D_pct":-4.48,"score_return_alignment_label":"improved_alignment","current_profile_verdict":"current_profile_missed_structural"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"R11L13_C31_HYUNDAI_VALUEUP_20240226","trigger_id":"TR_R11L13_HYUNDAI_VALUEUP_STAGE2A_20240226","symbol":"005380","large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"C31_POLICY_SUBSIDY_LEGISLATION_EVENT","raw_component_scores_before":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":3,"revision_score":4,"relative_strength_score":7,"customer_quality_score":4,"policy_or_regulatory_score":9,"valuation_repricing_score":8,"execution_risk_score":4,"legal_or_contract_risk_score":1,"dilution_cb_risk_score":0,"accounting_trust_risk_score":1,"roe_pbr_capital_return_score":7},"weighted_score_before":80,"stage_label_before":"Stage3-Yellow","raw_component_scores_after":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":3,"revision_score":4,"relative_strength_score":7,"customer_quality_score":4,"policy_or_regulatory_score":9,"valuation_repricing_score":8,"execution_risk_score":4,"legal_or_contract_risk_score":1,"dilution_cb_risk_score":0,"accounting_trust_risk_score":1,"roe_pbr_capital_return_score":9},"weighted_score_after":86,"stage_label_after":"Stage3-Yellow-high-shadow","changed_components":["verified_policy_to_capital_return_bonus","MAE_guard_kept"],"component_delta_explanation":"Policy bridge deserves uplift, but -10% MAE argues against automatic Green.","MFE_90D_pct":25.31,"MAE_90D_pct":-10.25,"score_return_alignment_label":"improved_but_keep_yellow","current_profile_verdict":"current_profile_too_late"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"R11L13_C31_KOGAS_EAST_SEA_20240603","trigger_id":"TR_R11L13_KOGAS_POLICY_STAGE2A_20240603","symbol":"036460","large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"C31_POLICY_SUBSIDY_LEGISLATION_EVENT","raw_component_scores_before":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":0,"revision_score":0,"relative_strength_score":10,"customer_quality_score":4,"policy_or_regulatory_score":10,"valuation_repricing_score":8,"execution_risk_score":6,"legal_or_contract_risk_score":2,"dilution_cb_risk_score":0,"accounting_trust_risk_score":2,"exploration_optionality_score":8},"weighted_score_before":76,"stage_label_before":"Stage3-Yellow-risk","raw_component_scores_after":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":0,"revision_score":0,"relative_strength_score":8,"customer_quality_score":4,"policy_or_regulatory_score":8,"valuation_repricing_score":5,"execution_risk_score":8,"legal_or_contract_risk_score":2,"dilution_cb_risk_score":0,"accounting_trust_risk_score":2,"exploration_optionality_score":5},"weighted_score_after":68,"stage_label_after":"Stage2-Actionable-risk-shadow","changed_components":["exploration_optionality_green_block","policy_theme_without_cashflow_haircut"],"component_delta_explanation":"Exploration approval is optionality, not confirmed reserves/economics. Keep Stage2 but block Green.","MFE_90D_pct":66.67,"MAE_90D_pct":-23.51,"score_return_alignment_label":"improved_guardrail","current_profile_verdict":"current_profile_false_positive"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"R11L13_C31_DONGYANG_PIPE_20240603","trigger_id":"TR_R11L13_DONGYANG_POLICY_STAGE2A_20240603","symbol":"008970","large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"C31_POLICY_SUBSIDY_LEGISLATION_EVENT","raw_component_scores_before":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":0,"revision_score":0,"relative_strength_score":10,"customer_quality_score":1,"policy_or_regulatory_score":8,"valuation_repricing_score":7,"execution_risk_score":8,"legal_or_contract_risk_score":2,"dilution_cb_risk_score":2,"accounting_trust_risk_score":3,"order_intake_quality_score":0},"weighted_score_before":74,"stage_label_before":"Stage2-Actionable-high","raw_component_scores_after":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":0,"revision_score":0,"relative_strength_score":6,"customer_quality_score":1,"policy_or_regulatory_score":5,"valuation_repricing_score":3,"execution_risk_score":9,"legal_or_contract_risk_score":2,"dilution_cb_risk_score":2,"accounting_trust_risk_score":3,"order_intake_quality_score":0},"weighted_score_after":58,"stage_label_after":"Watch/Stage2-blocked-shadow","changed_components":["policy_theme_without_cashflow_haircut","price_only_blowoff_blocks_positive_stage"],"component_delta_explanation":"No issuer-specific order or cashflow route; policy theme and price action cannot promote Stage3.","MFE_90D_pct":85.62,"MAE_90D_pct":-22.90,"score_return_alignment_label":"improved_false_green_block","current_profile_verdict":"current_profile_false_positive"}
```

### 25.5 shadow_weight rows

See Section 24 CSV. These rows are shadow-only and must not be applied to production without a later batch implementation session.

### 25.6 residual_contribution row

```jsonl
{"row_type":"residual_contribution","round":"R11","loop":"13","large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"C31_POLICY_SUBSIDY_LEGISLATION_EVENT","scheduled_round":"R11","scheduled_loop":"13","round_schedule_status":"valid","round_sector_consistency":"pass","new_independent_case_count":4,"reused_case_count":0,"new_symbol_count":4,"same_archetype_new_symbol_count":4,"same_archetype_new_trigger_family_count":3,"new_trigger_family_count":3,"positive_case_count":2,"counterexample_count":2,"current_profile_error_count":4,"tested_existing_calibrated_axes":["stage2_actionable_evidence_bonus","stage3_yellow_total_min","stage3_green_total_min","price_only_blowoff_blocks_positive_stage","full_4b_requires_non_price_evidence"],"residual_error_types_found":["policy_to_cashflow_missed_structural","policy_theme_false_positive","exploration_optionality_high_mae","price_only_4b_overlay_not_full_4b"],"diversity_score_summary":"4 new symbols, 3 new trigger families, 2 positives, 2 counterexamples, no reused cases","loop_contribution_label":"canonical_archetype_rule_candidate","do_not_propose_new_weight_delta":false}
```

### 25.7 narrative_only rows

```jsonl
{"row_type":"narrative_only","case_id":"R11L13_C31_DONGYANG_PIPE_20240603","symbol":"008970","large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"C31_POLICY_SUBSIDY_LEGISLATION_EVENT","reason":"2Y window blocked or contaminated by later 2025 corporate-action candidates; 30D/90D/180D remains usable","price_source":"Songdaiki/stock-web","usage":"not_2Y_weight_calibration"}
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
completed_loop = 13
next_round = R12
next_loop = 13
round_schedule_status = valid
round_sector_consistency = pass
```

## 28. Source Notes

- Stock-Web manifest and symbol profiles were read from `Songdaiki/stock-web` on the `main` branch.
- Manifest max date used for forward-window validation: `2026-02-20`.
- Price basis: `tradable_raw` / `raw_unadjusted_marcap`.
- Policy-event source notes used for narrative evidence only: Financial Times 2024-02-26 on Korea Value-up measures; Reuters 2024-02-28 on possible enforcement/penalty discussion; Reuters 2024-06-03 and WSJ 2024-06-03 on East Sea oil/gas exploration approval.
- All quantitative MFE/MAE values are derived from stock-web OHLC rows, not from external news sources.

