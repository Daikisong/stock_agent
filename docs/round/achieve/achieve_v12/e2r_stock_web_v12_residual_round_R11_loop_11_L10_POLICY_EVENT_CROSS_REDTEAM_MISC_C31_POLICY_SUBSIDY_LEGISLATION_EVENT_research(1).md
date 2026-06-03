# E2R Stock-Web Historical Calibration / Sector-Archetype Residual Research Round

## 0. Research Metadata

```text
research_session = post_calibrated_sector_archetype_residual_research
mode = historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12
output_format = one_standalone_markdown_file
scheduled_round = R11
scheduled_loop = 11
completed_round = R11
completed_loop = 11
next_round = R12
next_loop = 11
round_schedule_status = valid
round_sector_consistency = pass
large_sector_id = L10_POLICY_EVENT_CROSS_REDTEAM_MISC
canonical_archetype_id = C31_POLICY_SUBSIDY_LEGISLATION_EVENT
fine_archetype_id = POLICY_EVENT_QUALITY_SPLIT_VALUEUP_VS_HEADLINE_BETA
output_file = e2r_stock_web_v12_residual_round_R11_loop_11_L10_POLICY_EVENT_CROSS_REDTEAM_MISC_C31_POLICY_SUBSIDY_LEGISLATION_EVENT_research.md
price_source = Songdaiki/stock-web
stock_web_manifest_max_date = 2026-02-20
production_scoring_changed = false
shadow_weight_only = true
```

This loop adds 6 new independent cases, 4 counterexamples, and 6 residual errors for R11/L10_POLICY_EVENT_CROSS_REDTEAM_MISC/C31_POLICY_SUBSIDY_LEGISLATION_EVENT.

## 1. Current Calibrated Profile Assumption

```text
current_default_profile_proxy = e2r_2_1_stock_web_calibrated_proxy
previous_baseline_reference = e2r_2_0_baseline_reference
stage2_actionable_evidence_bonus = +2.0
stage3_yellow_total_min = 75.0
stage3_green_total_min = 87.0
stage3_green_revision_min = 55.0
stage3_cross_evidence_green_buffer = +1.5
price_only_blowoff_blocks_positive_stage = true
full_4b_requires_non_price_evidence = true
hard_4c_thesis_break_routes_to_4c = true
```

The stress test is not another proof that Stage2 should be earlier than Green. The residual question here is narrower: when a policy or public event hits the tape, should the signal be treated as a true economic transmission path, or merely as combustible headline fuel?

## 2. Round / Large Sector / Canonical Archetype Scope

```text
scheduled_round = R11
scheduled_loop = 11
large_sector_id = L10_POLICY_EVENT_CROSS_REDTEAM_MISC
canonical_archetype_id = C31_POLICY_SUBSIDY_LEGISLATION_EVENT
fine_archetype_id = POLICY_EVENT_QUALITY_SPLIT_VALUEUP_VS_HEADLINE_BETA
round_sector_consistency = pass
```

R11 is used as a policy/event checkpoint. The selected cases compare two policy channels:

1. **Corporate Value-up / capital-return transmission**: policy supports rerating only when company-level capital return, asset-value bridge, or financial visibility exists.
2. **East Sea oil/gas exploration headline beta**: policy headline creates price movement, but without order, subsidy, contract, reserve confirmation, or near-term cashflow bridge.

## 3. Previous Coverage / Duplicate Avoidance Check

Local v12 result files show Loop 11 already completed R1 through R10. The prior R10 output state pointed to R11/Loop 11. Existing R6 research already used KB금융 and 하나금융지주 as C21 capital-return cases, so this R11 MD avoids those as representative rows. 현대차 appeared in R9/C29 for a 2023 OEM margin trigger; here it is included only as a different policy-value-up trigger family with reduced independent evidence weight.

```text
scheduled_round = R11
scheduled_loop = 11
selected_scope = C31_POLICY_SUBSIDY_LEGISLATION_EVENT
same_symbol_same_trigger_duplicate = none
same_symbol_new_trigger_family = 005380 only, allowed with reuse_reason
minimum_new_symbol_count = 5
minimum_counterexample_count = 4
```

## 4. Stock-Web OHLC Input / Price Source Validation

```text
source = Songdaiki/stock-web
upstream_source = FinanceData/marcap
manifest_path = atlas/manifest.json
schema_path = atlas/schema.json
universe_path = atlas/universe/all_symbols.csv
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
markets = KONEX|KOSDAQ|KOSDAQ GLOBAL|KOSPI
calibration_shard_root = atlas/ohlcv_tradable_by_symbol_year
raw_shard_root = atlas/ohlcv_raw_by_symbol_year
price_basis = tradable_raw
```

The schema states that tradable shards contain `d,o,h,l,c,v,a,mc,s,m`; raw shards add `rs=row_status`. Calibration uses tradable rows only. Raw rows are not used for weight calibration.

## 5. Historical Eligibility Gate

| Symbol | Company | Entry date | 180D forward available by manifest max date | Corporate action status | Calibration usable |
|---|---:|---:|---:|---:|---:|
| 005380 | 현대차 | 2024-02-27 | yes | old corporate-action candidates only, no 2024 overlap | true |
| 402340 | SK스퀘어 | 2024-02-27 | yes | clean | true |
| 316140 | 우리금융지주 | 2024-02-27 | yes | clean | true |
| 036460 | 한국가스공사 | 2024-06-03 | yes | clean | true |
| 004090 | 한국석유 | 2024-06-03 | yes | old corporate-action candidates only, no 2024 overlap | true |
| 024060 | 흥구석유 | 2024-06-03 | yes | old corporate-action candidates only, no 2024 overlap | true |

All representative triggers are calibration-usable under stock-web `tradable_raw` 180D rules.

## 6. Canonical Archetype Compression Map

```text
canonical_archetype_id = C31_POLICY_SUBSIDY_LEGISLATION_EVENT
compression_rule = 정책/입법/보조금/공공 이벤트는 headline이 아니라 economic transmission route로 압축한다.
```

Fine archetypes are compressed as follows:

| Fine archetype | Canonical mapping | Promotion condition |
|---|---|---|
| KOREA_VALUEUP_POLICY_CAPITAL_RETURN_EXECUTION | C31 | value-up policy + capital return / margin / asset route |
| KOREA_VALUEUP_HOLDCO_DISCOUNT_ACTIVIST_ASSET_ROUTE | C31 | value-up policy + asset discount close route |
| KOREA_VALUEUP_POLICY_BETA_WITHOUT_SUPERIOR_EXECUTION | C31 | policy beta only; cap to Stage2-watch |
| EAST_SEA_OIL_GAS_EXPLORATION_POLICY_EVENT_CAP | C31 | headline event only; attach 4B/4C watch |
| EAST_SEA_OIL_GAS_THEMATIC_SUPPLIER_EVENT_FALSE_POSITIVE | C31 | price-only event beta; block Stage3 promotion |
| EAST_SEA_OIL_GAS_THEMATIC_MICROCAP_EVENT_FALSE_POSITIVE | C31 | price-only event beta; block Stage3 promotion |

## 7. Case Selection Summary

| Case ID | Symbol | Company | Case type | Role | Trigger date | Entry date | Entry price | MFE 180D | MAE 180D | Current profile verdict |
|---|---:|---|---|---|---:|---:|---:|---:|---:|---|
| R11L11_C31_005380_HYUNDAI_VALUEUP_POLICY_CAPITAL_RETURN_20240226 | 005380 | 현대차 | structural_success | positive | 2024-02-26 | 2024-02-27 | 238,500 | 25.58% | -10.06% | current_profile_too_late |
| R11L11_C31_402340_SK_SQUARE_VALUEUP_HOLDCO_DISCOUNT_AI_ASSET_20240226 | 402340 | SK스퀘어 | stage2_promote_candidate | positive | 2024-02-26 | 2024-02-27 | 65,300 | 66.92% | -1.68% | current_profile_missed_structural |
| R11L11_C31_316140_WOORI_VALUEUP_POLICY_BETA_WEAK_EXECUTION_20240226 | 316140 | 우리금융지주 | failed_rerating | counterexample | 2024-02-26 | 2024-02-27 | 14,940 | 14.46% | -11.98% | current_profile_false_positive |
| R11L11_C31_036460_KOGAS_EAST_SEA_DRILLING_EVENT_CAP_20240603 | 036460 | 한국가스공사 | price_moved_without_evidence | counterexample | 2024-06-03 | 2024-06-03 | 38,700 | 66.67% | -23.26% | current_profile_false_positive |
| R11L11_C31_004090_KOREA_PETROLEUM_EAST_SEA_THEMATIC_EVENT_20240603 | 004090 | 한국석유 | price_moved_without_evidence | counterexample | 2024-06-03 | 2024-06-03 | 17,950 | 56.55% | -31.81% | current_profile_false_positive |
| R11L11_C31_024060_HEUNGGU_OIL_EAST_SEA_THEMATIC_EVENT_20240603 | 024060 | 흥구석유 | price_moved_without_evidence | counterexample | 2024-06-03 | 2024-06-03 | 16,250 | 34.77% | -26.46% | current_profile_false_positive |

## 8. Positive vs Counterexample Balance

```text
positive_case_count = 2
counterexample_count = 4
calibration_usable_case_count = 6
new_independent_case_count = 6
new_symbol_count = 5
reused_case_count = 1
```

This loop intentionally overweights counterexamples because R11/C31 already has a natural tendency to be contaminated by headline-driven price action. The point is not to suppress policy signals; it is to require the policy signal to pass through a visible economic pipe before it is allowed to become a Stage3 thesis.

## 9. Evidence Source Map

| Symbol | Evidence source family | Price shard | Profile |
|---:|---|---|---|
| 005380 | Reuters/FT corporate value-up policy context; issuer-specific return details require URL enrichment before production promotion | atlas/ohlcv_tradable_by_symbol_year/005/005380/2024.csv | atlas/symbol_profiles/005/005380.json |
| 402340 | FT/Reuters value-up context; WSJ activist SK Square context; exact URL enrichment required before production promotion | atlas/ohlcv_tradable_by_symbol_year/402/402340/2024.csv | atlas/symbol_profiles/402/402340.json |
| 316140 | Reuters/FT corporate value-up policy context; issuer-specific capital-return proof requires later enrichment | atlas/ohlcv_tradable_by_symbol_year/316/316140/2024.csv | atlas/symbol_profiles/316/316140.json |
| 036460 | Reuters 2024-06-03 East Sea oil/gas exploration approval | atlas/ohlcv_tradable_by_symbol_year/036/036460/2024.csv | atlas/symbol_profiles/036/036460.json |
| 004090 | Reuters 2024-06-03 East Sea oil/gas exploration approval; stock-web price path confirms blowoff/giveback | atlas/ohlcv_tradable_by_symbol_year/004/004090/2024.csv | atlas/symbol_profiles/004/004090.json |
| 024060 | Reuters 2024-06-03 East Sea oil/gas exploration approval; stock-web price path confirms blowoff/giveback | atlas/ohlcv_tradable_by_symbol_year/024/024060/2024.csv | atlas/symbol_profiles/024/024060.json |

External evidence anchors used for narrative timing:

- Corporate Value-up Programme context: Financial Times, 2024-02-26; Reuters, 2024-02-28 and 2024-03-14.
- East Sea oil/gas exploration approval: Reuters, 2024-06-03; WSJ market-reaction summary.
- SK Square activist/value route context: WSJ activist coverage, used only as later qualitative support, not to backdate the initial policy trigger.

## 10. Price Data Source Map

| Symbol | Shard path | Profile path | Entry date | Entry price |
|---:|---|---|---:|---:|
| 005380 | atlas/ohlcv_tradable_by_symbol_year/005/005380/2024.csv | atlas/symbol_profiles/005/005380.json | 2024-02-27 | 238,500 |
| 402340 | atlas/ohlcv_tradable_by_symbol_year/402/402340/2024.csv | atlas/symbol_profiles/402/402340.json | 2024-02-27 | 65,300 |
| 316140 | atlas/ohlcv_tradable_by_symbol_year/316/316140/2024.csv | atlas/symbol_profiles/316/316140.json | 2024-02-27 | 14,940 |
| 036460 | atlas/ohlcv_tradable_by_symbol_year/036/036460/2024.csv | atlas/symbol_profiles/036/036460.json | 2024-06-03 | 38,700 |
| 004090 | atlas/ohlcv_tradable_by_symbol_year/004/004090/2024.csv | atlas/symbol_profiles/004/004090.json | 2024-06-03 | 17,950 |
| 024060 | atlas/ohlcv_tradable_by_symbol_year/024/024060/2024.csv | atlas/symbol_profiles/024/024060.json | 2024-06-03 | 16,250 |

## 11. Case-by-Case Trigger Grid

| Trigger ID | Trigger type | Symbol | Trigger date | Entry date | Entry price | Stage2 evidence | Stage3 evidence | 4B evidence | 4C evidence |
|---|---|---:|---:|---:|---:|---|---|---|---|
| R11L11_T_005380_20240226_Stage2_Actionable | Stage2-Actionable | 005380 | 2024-02-26 | 2024-02-27 | 238,500 | public_event_or_disclosure, policy_or_regulatory_optionality, relative_strength, early_revision_signal | financial_visibility, margin_bridge, multiple_public_sources, low_red_team_risk | - | - |
| R11L11_T_402340_20240226_Stage2_Actionable | Stage2-Actionable | 402340 | 2024-02-26 | 2024-02-27 | 65,300 | public_event_or_disclosure, policy_or_regulatory_optionality, relative_strength, customer_or_order_quality | financial_visibility, multiple_public_sources, durable_customer_confirmation, low_red_team_risk | valuation_blowoff, positioning_overheat | - |
| R11L11_T_316140_20240226_Stage2_Actionable | Stage2-Actionable | 316140 | 2024-02-26 | 2024-02-27 | 14,940 | public_event_or_disclosure, policy_or_regulatory_optionality, relative_strength | financial_visibility | - | - |
| R11L11_T_036460_20240603_Stage2_Event_Watch | Stage2-Event-Watch | 036460 | 2024-06-03 | 2024-06-03 | 38,700 | public_event_or_disclosure, policy_or_regulatory_optionality, relative_strength | - | valuation_blowoff, positioning_overheat, explicit_event_cap, price_only_local_peak | thesis_evidence_broken |
| R11L11_T_004090_20240603_Stage2_Event_Watch | Stage2-Event-Watch | 004090 | 2024-06-03 | 2024-06-03 | 17,950 | public_event_or_disclosure, policy_or_regulatory_optionality, relative_strength | - | valuation_blowoff, positioning_overheat, price_only_local_peak, explicit_event_cap | thesis_evidence_broken |
| R11L11_T_024060_20240603_Stage2_Event_Watch | Stage2-Event-Watch | 024060 | 2024-06-03 | 2024-06-03 | 16,250 | public_event_or_disclosure, policy_or_regulatory_optionality, relative_strength | - | valuation_blowoff, positioning_overheat, price_only_local_peak, explicit_event_cap | thesis_evidence_broken |

## 12. Trigger-Level OHLC Backtest Tables

| Trigger ID | Entry price | MFE 30D | MAE 30D | MFE 90D | MAE 90D | MFE 180D | MAE 180D | Peak date | Peak price | Drawdown after peak | Corporate action status |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|
| R11L11_T_005380_20240226_Stage2_Actionable | 238,500 | 9.01 | -10.06 | 25.58 | -10.06 | 25.58 | -10.06 | 2024-06-28 | 299,500 | -26.38 | clean_180D_window |
| R11L11_T_402340_20240226_Stage2_Actionable | 65,300 | 24.96 | -1.68 | 63.25 | -1.68 | 66.92 | -1.68 | 2024-07-11 | 109,000 | -37.98 | clean_180D_window |
| R11L11_T_316140_20240226_Stage2_Actionable | 14,940 | 3.75 | -11.24 | 3.75 | -11.98 | 14.46 | -11.98 | 2024-10-25 | 17,100 | -10.76 | clean_180D_window |
| R11L11_T_036460_20240603_Stage2_Event_Watch | 38,700 | 66.67 | -23.26 | 66.67 | -23.26 | 66.67 | -23.26 | 2024-06-20 | 64,500 | -43.41 | clean_180D_window |
| R11L11_T_004090_20240603_Stage2_Event_Watch | 17,950 | 56.55 | -22.84 | 56.55 | -22.84 | 56.55 | -31.81 | 2024-06-05 | 28,100 | -56.44 | clean_180D_window |
| R11L11_T_024060_20240603_Stage2_Event_Watch | 16,250 | 28.92 | -23.02 | 34.77 | -23.94 | 34.77 | -26.46 | 2024-08-13 | 21,900 | -45.43 | clean_180D_window |

## 13. Current Calibrated Profile Stress Test

| Case ID | P0 score / label | Proposed score / label | 90D MFE / MAE | Current profile verdict | Alignment note |
|---|---|---|---|---|---|
| R11L11_C31_005380_HYUNDAI_VALUEUP_POLICY_CAPITAL_RETURN_20240226 | 82.0 / Stage3-Yellow | 89.0 / Stage3-Green-shadow | 25.58% / -10.06% | current_profile_too_late | structural_success_policy_plus_execution |
| R11L11_C31_402340_SK_SQUARE_VALUEUP_HOLDCO_DISCOUNT_AI_ASSET_20240226 | 78.0 / Stage3-Yellow-low | 88.5 / Stage3-Green-shadow | 63.25% / -1.68% | current_profile_missed_structural | structural_success_policy_plus_asset_route |
| R11L11_C31_316140_WOORI_VALUEUP_POLICY_BETA_WEAK_EXECUTION_20240226 | 76.0 / Stage3-Yellow | 68.0 / Stage2-watch | 3.75% / -11.98% | current_profile_false_positive | policy_beta_low_quality_counterexample |
| R11L11_C31_036460_KOGAS_EAST_SEA_DRILLING_EVENT_CAP_20240603 | 80.0 / Stage3-Yellow-price-risk | 61.0 / Stage2-Event-Watch/4B-overlay | 66.67% / -23.26% | current_profile_false_positive | policy_event_price_spike_without_cashflow_bridge |
| R11L11_C31_004090_KOREA_PETROLEUM_EAST_SEA_THEMATIC_EVENT_20240603 | 78.0 / Stage3-Yellow-price-risk | 54.0 / Stage2-Event-Watch/4B-overlay | 56.55% / -22.84% | current_profile_false_positive | thematic_event_false_positive_high_MAE |
| R11L11_C31_024060_HEUNGGU_OIL_EAST_SEA_THEMATIC_EVENT_20240603 | 77.0 / Stage3-Yellow-price-risk | 52.0 / Stage2-Event-Watch/4B-overlay | 34.77% / -23.94% | current_profile_false_positive | thematic_event_false_positive_delayed_second_spike |

Stress-test answers:

1. Current profile is too permissive when policy evidence is merely public headline + relative strength.
2. Actual MFE can be high even for false positives; therefore MFE alone cannot distinguish structural policy transmission from event blowoff.
3. Stage2 actionable bonus is acceptable for policy events, but only as **watch/actionable**, not as automatic Stage3 promotion.
4. Yellow threshold 75 is too easy for C31 if relative strength and policy scores are both high but cashflow bridge is zero.
5. Green threshold 87 / revision 55 is adequate; the residual problem is that event-only names can be given too much pre-Green authority.
6. Price-only blowoff guard is strongly supported.
7. Full 4B non-price requirement is kept: price-only local peaks can be early, but event-cap + no cashflow bridge should still create a 4B overlay.
8. Hard 4C routing should be watch-only until a thesis-break fact appears; for exploration events, missing reserve confirmation is not automatically a same-day 4C.

## 14. Stage2 / Yellow / Green Comparison

For C31, Stage2 should be allowed when a policy event is real and tradable. Yellow/Green needs a second bridge: tax/legal implementation, subsidy award, tariff/capital-return action, reserve confirmation, contract/order, or company-specific capital allocation.

| Case | Stage2 timing | Yellow/Green risk | Lateness / residual |
|---|---|---|---|
| 현대차 | Stage2 on 2024-02-27 catches most of the move | Green should require capital-return execution proof | Green lateness ratio ~0.37 |
| SK스퀘어 | Stage2 on 2024-02-27 catches structural asset-discount rerating | Green should accept asset route, not only policy headline | Green lateness ratio ~0.29 |
| 우리금융지주 | Stage2 acceptable, Yellow too generous | Weak 180D MFE and high MAE relative to stronger peers | residual false positive |
| 한국가스공사 | Event-watch acceptable | Yellow/Green would confuse drilling optionality with earnings visibility | event-cap false positive |
| 한국석유 | Event-watch only | No direct order/revision route | event-thematic false positive |
| 흥구석유 | Event-watch only | Microcap event beta, not durable Stage3 | delayed second-spike false positive |

## 15. 4B Local vs Full-window Timing Audit

| Case | 4B evidence type | Local proximity | Full-window proximity | Verdict |
|---|---|---:|---:|---|
| 한국가스공사 | price_only, valuation_blowoff, positioning_overheat, explicit_event_cap | 0.96 | 0.96 | event-cap overlay, not standalone sell rule |
| 한국석유 | price_only, valuation_blowoff, positioning_overheat, explicit_event_cap | 0.53 | 0.53 | price-only 4B not enough for full thesis break |
| 흥구석유 | price_only, valuation_blowoff, positioning_overheat, explicit_event_cap | 0.64 | 0.53 | early local 4B before delayed full-window spike |
| 현대차 / SK스퀘어 / 우리금융지주 | not primary 4B rows | n/a | n/a | positive-stage or weak-policy-beta comparison only |

## 16. 4C Protection Audit

Event-only C31 rows should not be routed to hard 4C on the announcement date. A cleaner rule is:

```text
if event headline exists and direct_cashflow_bridge_score == 0:
    stage = Stage2-Event-Watch
    attach 4B event-cap overlay when price/valuation overheats
    route to 4C only after reserve/contract/subsidy/legal thesis breaks
```

In the oil/gas thematic rows, hard 4C would have been useful only after the market started treating the exploration probability and timeline as insufficient evidence. The 180D drawdowns show why a 4C watch flag is needed, but the trigger date itself is not enough for hard 4C.

## 17. Sector-Specific Rule Candidate

```text
rule_scope = sector_specific
large_sector_id = L10_POLICY_EVENT_CROSS_REDTEAM_MISC
axis = l10_policy_event_cashflow_bridge_gate
baseline_value = absent
tested_value = required_for_positive_stage
proposal_type = sector_shadow_only
```

Candidate rule:

> In L10 policy/event cases, public-policy evidence can create Stage2-Actionable or Stage2-Event-Watch, but Stage3-Yellow/Green requires a direct economic transmission bridge: capital return execution, subsidy award, contract/order, tariff change, legal implementation, reserve confirmation, or issuer-specific asset monetization.

## 18. Canonical-Archetype Rule Candidate

```text
rule_scope = canonical_archetype_specific
canonical_archetype_id = C31_POLICY_SUBSIDY_LEGISLATION_EVENT
axis = c31_headline_event_cap_guard
baseline_value = absent
tested_value = event_cap_score >= 85 blocks Stage3 unless direct_cashflow_bridge_score >= 55
proposal_type = canonical_shadow_only
```

This is the core residual contribution. C31 needs to stop treating policy headlines as a completed bridge. A policy event is a door opening; Stage3 needs proof that someone actually walks through it with cashflow, order, capital allocation, or legal enforceability.

## 19. Before / After Backtest Comparison

| Profile | Scope | Eligible triggers | Avg MFE 90D | Avg MAE 90D | Avg MFE 180D | Avg MAE 180D | False positive rate | Missed structural count | Alignment verdict |
|---|---|---:|---:|---:|---:|---:|---|---:|---|
| P0_e2r_2_1_stock_web_calibrated_proxy | current_global_proxy | 6 | 41.76 | -15.63 | 44.16 | -17.54 | 4/6 | 1 | mixed; policy events over-promoted without cashflow bridge |
| P0b_e2r_2_0_baseline_reference | rollback_reference | 6 | 41.76 | -15.63 | 44.16 | -17.54 | 4/6 higher severity | 1 | worse due to price-only policy event promotion |
| P1_l10_policy_event_quality_split_shadow_profile | sector_specific | 6 | 41.76 | -15.63 | 44.16 | -17.54 | 1/6 | 0 | better: keeps Hyundai/SK Square, blocks oil/gas thematic promotion |
| P2_c31_policy_subsidy_legislation_shadow_profile | canonical_archetype_specific | 6 | 41.76 | -15.63 | 44.16 | -17.54 | 1/6 | 0 | best shadow candidate for R11 |
| P3_counterexample_guard_profile | guard_profile | 6 | 41.76 | -15.63 | 44.16 | -17.54 | 0/4 event-only cases promoted | 1 | safe but can miss SK Square unless asset/capital route is accepted |

## 20. Score-Return Alignment Matrix

| Bucket | Cases | Return behavior | Score implication |
|---|---|---|---|
| policy + execution / asset bridge | 현대차, SK스퀘어 | strong MFE with explainable route | allow Stage3-shadow if bridge verified |
| policy beta weak execution | 우리금융지주 | low 90D MFE, high MAE vs stronger peers | cap at Stage2-watch until execution proof |
| headline event + no bridge | 한국가스공사, 한국석유, 흥구석유 | high MFE but severe giveback | Stage2-Event-Watch + 4B overlay, no Stage3 |

## 21. Coverage Matrix

| large_sector_id | canonical_archetype_id | fine_archetype_id | positive_case_count | counterexample_count | 4B_case_count | 4C_case_count | new_independent_case_count | reused_case_count | calibration_usable_trigger_count | representative_trigger_count | current_profile_error_count | sector_rule_candidate | canonical_rule_candidate | coverage_gap_after_this_loop |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|---|---|
| L10_POLICY_EVENT_CROSS_REDTEAM_MISC | C31_POLICY_SUBSIDY_LEGISLATION_EVENT | POLICY_EVENT_QUALITY_SPLIT_VALUEUP_VS_HEADLINE_BETA | 2 | 4 | 3 | 3 | 6 | 1 | 6 | 6 | 6 | true | true | still needs legislation/subsidy award cases outside Korea value-up and East Sea event |

## 22. Residual Contribution Summary

```text
new_independent_case_count: 6
reused_case_count: 1
reused_case_ids: R11L11_C31_005380_HYUNDAI_VALUEUP_POLICY_CAPITAL_RETURN_20240226
new_symbol_count: 5
same_archetype_new_symbol_count: 5
same_archetype_new_trigger_family_count: 6
new_canonical_archetype_count: 1
new_fine_archetype_count: 6
new_trigger_family_count: 6
positive_case_count: 2
counterexample_count: 4
current_profile_error_count: 6
tested_existing_calibrated_axes: price_only_blowoff_blocks_positive_stage, full_4b_requires_non_price_evidence, hard_4c_thesis_break_routes_to_4c, stage3_green_revision_min
residual_error_types_found: policy_event_without_cashflow_bridge_false_positive, policy_beta_weak_execution_counterexample, asset_route_missed_structural, price_only_4B_not_full
new_axis_proposed: l10_policy_event_cashflow_bridge_gate, c31_headline_event_cap_guard, c31_direct_economic_transmission_bonus, c31_event_cap_overheat_penalty
existing_axis_strengthened: price_only_blowoff_blocks_positive_stage, full_4b_requires_non_price_evidence, hard_4c_thesis_break_routes_to_4c
existing_axis_weakened: null
existing_axis_kept: stage2_actionable_evidence_bonus, stage3_green_revision_min
sector_specific_rule_candidate: true
canonical_archetype_rule_candidate: true
no_new_signal_reason: null
loop_contribution_label: canonical_archetype_rule_candidate
do_not_propose_new_weight_delta: false
```

## 23. Validation Scope / Non-Validation Scope

Validated:

- Actual stock-web `tradable_raw` entry rows.
- 30D/90D/180D MFE and MAE using OHLC high/low windows.
- Corporate-action window status from symbol profiles.
- Current-profile residual classification.
- 4B local vs full-window separation for event names.

Not validated here:

- Production scoring code.
- Live candidates.
- Broker execution.
- Current 2026 watchlist.
- Full issuer-level disclosure URL enrichment for every capital-return fact.

## 24. Shadow Weight Calibration

```csv
row_type,axis,scope,large_sector_id,canonical_archetype_id,baseline_value,tested_value,delta,reason,backtest_effect,trigger_ids,calibration_usable_count,new_independent_case_count,counterexample_count,confidence,proposal_type,notes
shadow_weight,l10_policy_event_cashflow_bridge_gate,sector_specific,L10_POLICY_EVENT_CROSS_REDTEAM_MISC,C31_POLICY_SUBSIDY_LEGISLATION_EVENT,0,1,+1,"Require visible economic transmission for positive policy-stage promotion","reduces oil/gas headline false positives while keeping Hyundai/SK Square", "R11L11_T_005380_20240226_Stage2_Actionable|R11L11_T_402340_20240226_Stage2_Actionable|R11L11_T_036460_20240603_Stage2_Event_Watch|R11L11_T_004090_20240603_Stage2_Event_Watch|R11L11_T_024060_20240603_Stage2_Event_Watch",6,6,4,medium,sector_shadow_only,"not production; post-calibrated residual"
shadow_weight,c31_headline_event_cap_guard,canonical_archetype_specific,L10_POLICY_EVENT_CROSS_REDTEAM_MISC,C31_POLICY_SUBSIDY_LEGISLATION_EVENT,0,1,+1,"Headline+RS event rows should remain Stage2-watch and 4B overlay unless direct bridge exists","blocks Stage3 false positives in KOGAS/Korea Petroleum/Heunggu", "R11L11_T_036460_20240603_Stage2_Event_Watch|R11L11_T_004090_20240603_Stage2_Event_Watch|R11L11_T_024060_20240603_Stage2_Event_Watch",3,3,3,medium,canonical_shadow_only,"not production; supports existing price-only blowoff guard"
shadow_weight,c31_direct_economic_transmission_bonus,canonical_archetype_specific,L10_POLICY_EVENT_CROSS_REDTEAM_MISC,C31_POLICY_SUBSIDY_LEGISLATION_EVENT,0,1,+1,"Capital return, asset monetization, subsidy award, tariff, contract, or reserve confirmation can promote policy event to positive stage","keeps Hyundai/SK Square positives", "R11L11_T_005380_20240226_Stage2_Actionable|R11L11_T_402340_20240226_Stage2_Actionable",2,2,0,low,canonical_shadow_only,"needs more R11 policy award cases"
```

## 25. Machine-Readable Rows

```jsonl
{"row_type": "price_source_validation", "source": "Songdaiki/stock-web", "source_url": "https://github.com/Songdaiki/stock-web", "manifest_path": "atlas/manifest.json", "schema_path": "atlas/schema.json", "universe_path": "atlas/universe/all_symbols.csv", "manifest_max_date": "2026-02-20", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "raw_shard_root": "atlas/ohlcv_raw_by_symbol_year", "validation_status": "usable_for_historical_calibration"}
{"row_type": "case", "case_id": "R11L11_C31_005380_HYUNDAI_VALUEUP_POLICY_CAPITAL_RETURN_20240226", "symbol": "005380", "company_name": "현대차", "round": "R11", "loop": "11", "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "C31_POLICY_SUBSIDY_LEGISLATION_EVENT", "fine_archetype_id": "KOREA_VALUEUP_POLICY_CAPITAL_RETURN_EXECUTION", "case_type": "structural_success", "positive_or_counterexample": "positive", "best_trigger": "R11L11_T_005380_20240226_Stage2_Actionable", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": "same symbol appeared in R9/C29 with 2023 OEM margin trigger; this is a new C31 policy-value-up trigger family", "independent_evidence_weight": 0.5, "score_price_alignment": "structural_success_policy_plus_execution", "current_profile_verdict": "current_profile_too_late", "price_source": "Songdaiki/stock-web", "notes": "Corporate Value-up policy tailwind met an already visible shareholder-return/low-PBR rerating route; same symbol was previously studied for 2023 OEM margin, but this is a different policy-trigger family."}
{"row_type": "trigger", "trigger_id": "R11L11_T_005380_20240226_Stage2_Actionable", "case_id": "R11L11_C31_005380_HYUNDAI_VALUEUP_POLICY_CAPITAL_RETURN_20240226", "symbol": "005380", "company_name": "현대차", "round": "R11", "loop": "11", "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "C31_POLICY_SUBSIDY_LEGISLATION_EVENT", "fine_archetype_id": "KOREA_VALUEUP_POLICY_CAPITAL_RETURN_EXECUTION", "sector": "자동차·정책가치업", "primary_archetype": "policy value-up with capital return proof", "loop_objective": "coverage_gap_fill|residual_false_positive_mining|sector_specific_rule_discovery|canonical_archetype_compression|4B_non_price_requirement_stress_test", "trigger_type": "Stage2-Actionable", "trigger_date": "2024-02-26", "evidence_available_at_that_date": "Corporate Value-up policy tailwind met an already visible shareholder-return/low-PBR rerating route; same symbol was previously studied for 2023 OEM margin, but this is a different policy-trigger family.", "evidence_source": "Reuters/FT corporate value-up policy context; issuer-specific return details require URL enrichment before production promotion", "stage2_evidence_fields": ["public_event_or_disclosure", "policy_or_regulatory_optionality", "relative_strength", "early_revision_signal"], "stage3_evidence_fields": ["financial_visibility", "margin_bridge", "multiple_public_sources", "low_red_team_risk"], "stage4b_evidence_fields": [], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/005/005380/2024.csv", "profile_path": "atlas/symbol_profiles/005/005380.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "entry_date": "2024-02-27", "entry_price": 238500, "MFE_30D_pct": 9.01, "MFE_90D_pct": 25.58, "MFE_180D_pct": 25.58, "MFE_1Y_pct": 25.58, "MFE_2Y_pct": null, "MAE_30D_pct": -10.06, "MAE_90D_pct": -10.06, "MAE_180D_pct": -10.06, "MAE_1Y_pct": -10.06, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2024-06-28", "peak_price": 299500, "drawdown_after_peak_pct": -26.38, "green_lateness_ratio": 0.37, "four_b_local_peak_proximity": null, "four_b_full_window_peak_proximity": null, "four_b_timing_verdict": "not_4B", "four_b_evidence_type": [], "four_c_protection_label": "not_applicable", "trigger_outcome_label": "structural_success_policy_plus_execution", "current_profile_verdict": "current_profile_too_late", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window", "same_entry_group_id": "R11L11_005380_2024-02-27_238500", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": "same symbol appeared in R9/C29 with 2023 OEM margin trigger; this is a new C31 policy-value-up trigger family", "independent_evidence_weight": 0.5, "do_not_count_as_new_case": false}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R11L11_C31_005380_HYUNDAI_VALUEUP_POLICY_CAPITAL_RETURN_20240226", "trigger_id": "R11L11_T_005380_20240226_Stage2_Actionable", "symbol": "005380", "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "C31_POLICY_SUBSIDY_LEGISLATION_EVENT", "raw_component_scores_before": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 0, "revision_score": 54, "relative_strength_score": 70, "customer_quality_score": 0, "policy_or_regulatory_score": 72, "valuation_repricing_score": 72, "execution_risk_score": 34, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0, "policy_event_specificity_score": 74, "capital_return_execution_score": 64, "event_cap_score": 0, "direct_cashflow_bridge_score": 62, "positioning_overheat_score": 0, "thesis_break_score": 0}, "weighted_score_before": 82.0, "stage_label_before": "Stage3-Yellow", "raw_component_scores_after": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 0, "revision_score": 60, "relative_strength_score": 74, "customer_quality_score": 0, "policy_or_regulatory_score": 82, "valuation_repricing_score": 78, "execution_risk_score": 32, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0, "policy_event_specificity_score": 84, "capital_return_execution_score": 86, "event_cap_score": 0, "direct_cashflow_bridge_score": 82, "positioning_overheat_score": 0, "thesis_break_score": 0}, "weighted_score_after": 89.0, "stage_label_after": "Stage3-Green-shadow", "changed_components": ["policy_event_specificity_score", "direct_cashflow_bridge_score", "capital_return_execution_score", "event_cap_score", "positioning_overheat_score"], "component_delta_explanation": "C31 shadow profile rewards policy events only when the legal/economic transmission path is visible; headline-only event beta is capped and moved to 4B/4C watch.", "MFE_90D_pct": 25.58, "MAE_90D_pct": -10.06, "score_return_alignment_label": "structural_success_policy_plus_execution", "current_profile_verdict": "current_profile_too_late"}
{"row_type": "case", "case_id": "R11L11_C31_402340_SK_SQUARE_VALUEUP_HOLDCO_DISCOUNT_AI_ASSET_20240226", "symbol": "402340", "company_name": "SK스퀘어", "round": "R11", "loop": "11", "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "C31_POLICY_SUBSIDY_LEGISLATION_EVENT", "fine_archetype_id": "KOREA_VALUEUP_HOLDCO_DISCOUNT_ACTIVIST_ASSET_ROUTE", "case_type": "stage2_promote_candidate", "positive_or_counterexample": "positive", "best_trigger": "R11L11_T_402340_20240226_Stage2_Actionable", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "structural_success_policy_plus_asset_route", "current_profile_verdict": "current_profile_missed_structural", "price_source": "Songdaiki/stock-web", "notes": "Corporate Value-up policy and holding-company discount narrative had a concrete asset route through SK Hynix exposure and later activist pressure; score should reward policy only when asset/capital-route is visible."}
{"row_type": "trigger", "trigger_id": "R11L11_T_402340_20240226_Stage2_Actionable", "case_id": "R11L11_C31_402340_SK_SQUARE_VALUEUP_HOLDCO_DISCOUNT_AI_ASSET_20240226", "symbol": "402340", "company_name": "SK스퀘어", "round": "R11", "loop": "11", "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "C31_POLICY_SUBSIDY_LEGISLATION_EVENT", "fine_archetype_id": "KOREA_VALUEUP_HOLDCO_DISCOUNT_ACTIVIST_ASSET_ROUTE", "sector": "지주·플랫폼자산·정책가치업", "primary_archetype": "policy value-up with holdco discount plus asset catalyst", "loop_objective": "coverage_gap_fill|residual_false_positive_mining|sector_specific_rule_discovery|canonical_archetype_compression|4B_non_price_requirement_stress_test", "trigger_type": "Stage2-Actionable", "trigger_date": "2024-02-26", "evidence_available_at_that_date": "Corporate Value-up policy and holding-company discount narrative had a concrete asset route through SK Hynix exposure and later activist pressure; score should reward policy only when asset/capital-route is visible.", "evidence_source": "FT/Reuters value-up context; WSJ activist SK Square context; exact URL enrichment required before production promotion", "stage2_evidence_fields": ["public_event_or_disclosure", "policy_or_regulatory_optionality", "relative_strength", "customer_or_order_quality"], "stage3_evidence_fields": ["financial_visibility", "multiple_public_sources", "durable_customer_confirmation", "low_red_team_risk"], "stage4b_evidence_fields": ["valuation_blowoff", "positioning_overheat"], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/402/402340/2024.csv", "profile_path": "atlas/symbol_profiles/402/402340.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "entry_date": "2024-02-27", "entry_price": 65300, "MFE_30D_pct": 24.96, "MFE_90D_pct": 63.25, "MFE_180D_pct": 66.92, "MFE_1Y_pct": 66.92, "MFE_2Y_pct": null, "MAE_30D_pct": -1.68, "MAE_90D_pct": -1.68, "MAE_180D_pct": -1.68, "MAE_1Y_pct": -1.68, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2024-07-11", "peak_price": 109000, "drawdown_after_peak_pct": -37.98, "green_lateness_ratio": 0.29, "four_b_local_peak_proximity": null, "four_b_full_window_peak_proximity": null, "four_b_timing_verdict": "not_full_4B_without_non_price_overheat", "four_b_evidence_type": ["valuation_blowoff", "positioning_overheat"], "four_c_protection_label": "not_applicable", "trigger_outcome_label": "structural_success_policy_plus_asset_route", "current_profile_verdict": "current_profile_missed_structural", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window", "same_entry_group_id": "R11L11_402340_2024-02-27_65300", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R11L11_C31_402340_SK_SQUARE_VALUEUP_HOLDCO_DISCOUNT_AI_ASSET_20240226", "trigger_id": "R11L11_T_402340_20240226_Stage2_Actionable", "symbol": "402340", "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "C31_POLICY_SUBSIDY_LEGISLATION_EVENT", "raw_component_scores_before": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 0, "revision_score": 42, "relative_strength_score": 76, "customer_quality_score": 0, "policy_or_regulatory_score": 70, "valuation_repricing_score": 84, "execution_risk_score": 42, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0, "policy_event_specificity_score": 76, "capital_return_execution_score": 44, "event_cap_score": 0, "direct_cashflow_bridge_score": 58, "positioning_overheat_score": 0, "thesis_break_score": 0}, "weighted_score_before": 78.0, "stage_label_before": "Stage3-Yellow-low", "raw_component_scores_after": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 0, "revision_score": 48, "relative_strength_score": 86, "customer_quality_score": 0, "policy_or_regulatory_score": 84, "valuation_repricing_score": 88, "execution_risk_score": 40, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0, "policy_event_specificity_score": 88, "capital_return_execution_score": 56, "event_cap_score": 0, "direct_cashflow_bridge_score": 78, "positioning_overheat_score": 0, "thesis_break_score": 0}, "weighted_score_after": 88.5, "stage_label_after": "Stage3-Green-shadow", "changed_components": ["policy_event_specificity_score", "direct_cashflow_bridge_score", "capital_return_execution_score", "event_cap_score", "positioning_overheat_score"], "component_delta_explanation": "C31 shadow profile rewards policy events only when the legal/economic transmission path is visible; headline-only event beta is capped and moved to 4B/4C watch.", "MFE_90D_pct": 63.25, "MAE_90D_pct": -1.68, "score_return_alignment_label": "structural_success_policy_plus_asset_route", "current_profile_verdict": "current_profile_missed_structural"}
{"row_type": "case", "case_id": "R11L11_C31_316140_WOORI_VALUEUP_POLICY_BETA_WEAK_EXECUTION_20240226", "symbol": "316140", "company_name": "우리금융지주", "round": "R11", "loop": "11", "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "C31_POLICY_SUBSIDY_LEGISLATION_EVENT", "fine_archetype_id": "KOREA_VALUEUP_POLICY_BETA_WITHOUT_SUPERIOR_EXECUTION", "case_type": "failed_rerating", "positive_or_counterexample": "counterexample", "best_trigger": "R11L11_T_316140_20240226_Stage2_Actionable", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "policy_beta_low_quality_counterexample", "current_profile_verdict": "current_profile_false_positive", "price_source": "Songdaiki/stock-web", "notes": "Same value-up policy tailwind, but near-term 180D return profile was far weaker until later capital-return proof; policy beta alone should not receive full C31 promotion."}
{"row_type": "trigger", "trigger_id": "R11L11_T_316140_20240226_Stage2_Actionable", "case_id": "R11L11_C31_316140_WOORI_VALUEUP_POLICY_BETA_WEAK_EXECUTION_20240226", "symbol": "316140", "company_name": "우리금융지주", "round": "R11", "loop": "11", "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "C31_POLICY_SUBSIDY_LEGISLATION_EVENT", "fine_archetype_id": "KOREA_VALUEUP_POLICY_BETA_WITHOUT_SUPERIOR_EXECUTION", "sector": "금융·정책가치업", "primary_archetype": "policy beta without differentiated execution", "loop_objective": "coverage_gap_fill|residual_false_positive_mining|sector_specific_rule_discovery|canonical_archetype_compression|4B_non_price_requirement_stress_test", "trigger_type": "Stage2-Actionable", "trigger_date": "2024-02-26", "evidence_available_at_that_date": "Same value-up policy tailwind, but near-term 180D return profile was far weaker until later capital-return proof; policy beta alone should not receive full C31 promotion.", "evidence_source": "Reuters/FT corporate value-up policy context; issuer-specific capital-return proof requires later enrichment", "stage2_evidence_fields": ["public_event_or_disclosure", "policy_or_regulatory_optionality", "relative_strength"], "stage3_evidence_fields": ["financial_visibility"], "stage4b_evidence_fields": [], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/316/316140/2024.csv", "profile_path": "atlas/symbol_profiles/316/316140.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "entry_date": "2024-02-27", "entry_price": 14940, "MFE_30D_pct": 3.75, "MFE_90D_pct": 3.75, "MFE_180D_pct": 14.46, "MFE_1Y_pct": 14.46, "MFE_2Y_pct": null, "MAE_30D_pct": -11.24, "MAE_90D_pct": -11.98, "MAE_180D_pct": -11.98, "MAE_1Y_pct": -11.98, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2024-10-25", "peak_price": 17100, "drawdown_after_peak_pct": -10.76, "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": null, "four_b_full_window_peak_proximity": null, "four_b_timing_verdict": "not_4B", "four_b_evidence_type": [], "four_c_protection_label": "not_applicable", "trigger_outcome_label": "policy_beta_low_quality_counterexample", "current_profile_verdict": "current_profile_false_positive", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window", "same_entry_group_id": "R11L11_316140_2024-02-27_14940", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R11L11_C31_316140_WOORI_VALUEUP_POLICY_BETA_WEAK_EXECUTION_20240226", "trigger_id": "R11L11_T_316140_20240226_Stage2_Actionable", "symbol": "316140", "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "C31_POLICY_SUBSIDY_LEGISLATION_EVENT", "raw_component_scores_before": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 0, "revision_score": 38, "relative_strength_score": 58, "customer_quality_score": 0, "policy_or_regulatory_score": 70, "valuation_repricing_score": 62, "execution_risk_score": 46, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0, "policy_event_specificity_score": 72, "capital_return_execution_score": 48, "event_cap_score": 0, "direct_cashflow_bridge_score": 38, "positioning_overheat_score": 0, "thesis_break_score": 0}, "weighted_score_before": 76.0, "stage_label_before": "Stage3-Yellow", "raw_component_scores_after": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 0, "revision_score": 38, "relative_strength_score": 58, "customer_quality_score": 0, "policy_or_regulatory_score": 60, "valuation_repricing_score": 58, "execution_risk_score": 48, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0, "policy_event_specificity_score": 54, "capital_return_execution_score": 44, "event_cap_score": 0, "direct_cashflow_bridge_score": 34, "positioning_overheat_score": 0, "thesis_break_score": 0}, "weighted_score_after": 68.0, "stage_label_after": "Stage2-watch", "changed_components": ["policy_event_specificity_score", "direct_cashflow_bridge_score", "capital_return_execution_score", "event_cap_score", "positioning_overheat_score"], "component_delta_explanation": "C31 shadow profile rewards policy events only when the legal/economic transmission path is visible; headline-only event beta is capped and moved to 4B/4C watch.", "MFE_90D_pct": 3.75, "MAE_90D_pct": -11.98, "score_return_alignment_label": "policy_beta_low_quality_counterexample", "current_profile_verdict": "current_profile_false_positive"}
{"row_type": "case", "case_id": "R11L11_C31_036460_KOGAS_EAST_SEA_DRILLING_EVENT_CAP_20240603", "symbol": "036460", "company_name": "한국가스공사", "round": "R11", "loop": "11", "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "C31_POLICY_SUBSIDY_LEGISLATION_EVENT", "fine_archetype_id": "EAST_SEA_OIL_GAS_EXPLORATION_POLICY_EVENT_CAP", "case_type": "price_moved_without_evidence", "positive_or_counterexample": "counterexample", "best_trigger": "R11L11_T_036460_20240603_Stage2_Event_Watch", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "policy_event_price_spike_without_cashflow_bridge", "current_profile_verdict": "current_profile_false_positive", "price_source": "Songdaiki/stock-web", "notes": "Presidential approval for exploratory drilling created a policy/event shock; Reuters noted the opportunity size but also uncertainty, success-rate caveat, cost and long commercialization horizon."}
{"row_type": "trigger", "trigger_id": "R11L11_T_036460_20240603_Stage2_Event_Watch", "case_id": "R11L11_C31_036460_KOGAS_EAST_SEA_DRILLING_EVENT_CAP_20240603", "symbol": "036460", "company_name": "한국가스공사", "round": "R11", "loop": "11", "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "C31_POLICY_SUBSIDY_LEGISLATION_EVENT", "fine_archetype_id": "EAST_SEA_OIL_GAS_EXPLORATION_POLICY_EVENT_CAP", "sector": "에너지·정책이벤트", "primary_archetype": "government exploration approval without near-term cashflow bridge", "loop_objective": "coverage_gap_fill|residual_false_positive_mining|sector_specific_rule_discovery|canonical_archetype_compression|4B_non_price_requirement_stress_test", "trigger_type": "Stage2-Event-Watch", "trigger_date": "2024-06-03", "evidence_available_at_that_date": "Presidential approval for exploratory drilling created a policy/event shock; Reuters noted the opportunity size but also uncertainty, success-rate caveat, cost and long commercialization horizon.", "evidence_source": "Reuters 2024-06-03 East Sea oil/gas exploration approval", "stage2_evidence_fields": ["public_event_or_disclosure", "policy_or_regulatory_optionality", "relative_strength"], "stage3_evidence_fields": [], "stage4b_evidence_fields": ["valuation_blowoff", "positioning_overheat", "explicit_event_cap", "price_only_local_peak"], "stage4c_evidence_fields": ["thesis_evidence_broken"], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/036/036460/2024.csv", "profile_path": "atlas/symbol_profiles/036/036460.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "entry_date": "2024-06-03", "entry_price": 38700, "MFE_30D_pct": 66.67, "MFE_90D_pct": 66.67, "MFE_180D_pct": 66.67, "MFE_1Y_pct": 66.67, "MFE_2Y_pct": null, "MAE_30D_pct": -23.26, "MAE_90D_pct": -23.26, "MAE_180D_pct": -23.26, "MAE_1Y_pct": -23.26, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2024-06-20", "peak_price": 64500, "drawdown_after_peak_pct": -43.41, "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": 0.96, "four_b_full_window_peak_proximity": 0.96, "four_b_timing_verdict": "price_only_local_4B_not_full_without_non_price_confirmation", "four_b_evidence_type": ["price_only", "valuation_blowoff", "positioning_overheat", "explicit_event_cap"], "four_c_protection_label": "thesis_break_watch_only", "trigger_outcome_label": "policy_event_price_spike_without_cashflow_bridge", "current_profile_verdict": "current_profile_false_positive", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window", "same_entry_group_id": "R11L11_036460_2024-06-03_38700", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R11L11_C31_036460_KOGAS_EAST_SEA_DRILLING_EVENT_CAP_20240603", "trigger_id": "R11L11_T_036460_20240603_Stage2_Event_Watch", "symbol": "036460", "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "C31_POLICY_SUBSIDY_LEGISLATION_EVENT", "raw_component_scores_before": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 0, "revision_score": 0, "relative_strength_score": 92, "customer_quality_score": 0, "policy_or_regulatory_score": 88, "valuation_repricing_score": 86, "execution_risk_score": 72, "legal_or_contract_risk_score": 38, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0, "policy_event_specificity_score": 84, "capital_return_execution_score": 0, "event_cap_score": 90, "direct_cashflow_bridge_score": 8, "positioning_overheat_score": 90, "thesis_break_score": 0}, "weighted_score_before": 80.0, "stage_label_before": "Stage3-Yellow-price-risk", "raw_component_scores_after": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 0, "revision_score": 0, "relative_strength_score": 82, "customer_quality_score": 0, "policy_or_regulatory_score": 70, "valuation_repricing_score": 66, "execution_risk_score": 82, "legal_or_contract_risk_score": 48, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0, "policy_event_specificity_score": 58, "capital_return_execution_score": 0, "event_cap_score": 96, "direct_cashflow_bridge_score": 6, "positioning_overheat_score": 94, "thesis_break_score": 0}, "weighted_score_after": 61.0, "stage_label_after": "Stage2-Event-Watch/4B-overlay", "changed_components": ["policy_event_specificity_score", "direct_cashflow_bridge_score", "capital_return_execution_score", "event_cap_score", "positioning_overheat_score"], "component_delta_explanation": "C31 shadow profile rewards policy events only when the legal/economic transmission path is visible; headline-only event beta is capped and moved to 4B/4C watch.", "MFE_90D_pct": 66.67, "MAE_90D_pct": -23.26, "score_return_alignment_label": "policy_event_price_spike_without_cashflow_bridge", "current_profile_verdict": "current_profile_false_positive"}
{"row_type": "case", "case_id": "R11L11_C31_004090_KOREA_PETROLEUM_EAST_SEA_THEMATIC_EVENT_20240603", "symbol": "004090", "company_name": "한국석유", "round": "R11", "loop": "11", "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "C31_POLICY_SUBSIDY_LEGISLATION_EVENT", "fine_archetype_id": "EAST_SEA_OIL_GAS_THEMATIC_SUPPLIER_EVENT_FALSE_POSITIVE", "case_type": "price_moved_without_evidence", "positive_or_counterexample": "counterexample", "best_trigger": "R11L11_T_004090_20240603_Stage2_Event_Watch", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "thematic_event_false_positive_high_MAE", "current_profile_verdict": "current_profile_false_positive", "price_source": "Songdaiki/stock-web", "notes": "East Sea exploration announcement spilled into oil-related thematic names. The price path produced quick upside, then gave back most of it without confirmed contract/order/revision evidence."}
{"row_type": "trigger", "trigger_id": "R11L11_T_004090_20240603_Stage2_Event_Watch", "case_id": "R11L11_C31_004090_KOREA_PETROLEUM_EAST_SEA_THEMATIC_EVENT_20240603", "symbol": "004090", "company_name": "한국석유", "round": "R11", "loop": "11", "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "C31_POLICY_SUBSIDY_LEGISLATION_EVENT", "fine_archetype_id": "EAST_SEA_OIL_GAS_THEMATIC_SUPPLIER_EVENT_FALSE_POSITIVE", "sector": "석유제품·정책테마", "primary_archetype": "event-thematic supplier without confirmed order/revision", "loop_objective": "coverage_gap_fill|residual_false_positive_mining|sector_specific_rule_discovery|canonical_archetype_compression|4B_non_price_requirement_stress_test", "trigger_type": "Stage2-Event-Watch", "trigger_date": "2024-06-03", "evidence_available_at_that_date": "East Sea exploration announcement spilled into oil-related thematic names. The price path produced quick upside, then gave back most of it without confirmed contract/order/revision evidence.", "evidence_source": "Reuters 2024-06-03 East Sea oil/gas exploration approval; stock-web price path confirms blowoff/giveback", "stage2_evidence_fields": ["public_event_or_disclosure", "policy_or_regulatory_optionality", "relative_strength"], "stage3_evidence_fields": [], "stage4b_evidence_fields": ["valuation_blowoff", "positioning_overheat", "price_only_local_peak", "explicit_event_cap"], "stage4c_evidence_fields": ["thesis_evidence_broken"], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/004/004090/2024.csv", "profile_path": "atlas/symbol_profiles/004/004090.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "entry_date": "2024-06-03", "entry_price": 17950, "MFE_30D_pct": 56.55, "MFE_90D_pct": 56.55, "MFE_180D_pct": 56.55, "MFE_1Y_pct": 56.55, "MFE_2Y_pct": null, "MAE_30D_pct": -22.84, "MAE_90D_pct": -22.84, "MAE_180D_pct": -31.81, "MAE_1Y_pct": -31.81, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2024-06-05", "peak_price": 28100, "drawdown_after_peak_pct": -56.44, "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": 0.53, "four_b_full_window_peak_proximity": 0.53, "four_b_timing_verdict": "price_only_local_4B_not_full_without_non_price_confirmation", "four_b_evidence_type": ["price_only", "valuation_blowoff", "positioning_overheat", "explicit_event_cap"], "four_c_protection_label": "hard_4c_late", "trigger_outcome_label": "thematic_event_false_positive_high_MAE", "current_profile_verdict": "current_profile_false_positive", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window", "same_entry_group_id": "R11L11_004090_2024-06-03_17950", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R11L11_C31_004090_KOREA_PETROLEUM_EAST_SEA_THEMATIC_EVENT_20240603", "trigger_id": "R11L11_T_004090_20240603_Stage2_Event_Watch", "symbol": "004090", "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "C31_POLICY_SUBSIDY_LEGISLATION_EVENT", "raw_component_scores_before": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 0, "revision_score": 0, "relative_strength_score": 94, "customer_quality_score": 0, "policy_or_regulatory_score": 74, "valuation_repricing_score": 92, "execution_risk_score": 84, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0, "policy_event_specificity_score": 50, "capital_return_execution_score": 0, "event_cap_score": 96, "direct_cashflow_bridge_score": 0, "positioning_overheat_score": 96, "thesis_break_score": 0}, "weighted_score_before": 78.0, "stage_label_before": "Stage3-Yellow-price-risk", "raw_component_scores_after": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 0, "revision_score": 0, "relative_strength_score": 78, "customer_quality_score": 0, "policy_or_regulatory_score": 52, "valuation_repricing_score": 58, "execution_risk_score": 90, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0, "policy_event_specificity_score": 34, "capital_return_execution_score": 0, "event_cap_score": 98, "direct_cashflow_bridge_score": 0, "positioning_overheat_score": 98, "thesis_break_score": 0}, "weighted_score_after": 54.0, "stage_label_after": "Stage2-Event-Watch/4B-overlay", "changed_components": ["policy_event_specificity_score", "direct_cashflow_bridge_score", "capital_return_execution_score", "event_cap_score", "positioning_overheat_score"], "component_delta_explanation": "C31 shadow profile rewards policy events only when the legal/economic transmission path is visible; headline-only event beta is capped and moved to 4B/4C watch.", "MFE_90D_pct": 56.55, "MAE_90D_pct": -22.84, "score_return_alignment_label": "thematic_event_false_positive_high_MAE", "current_profile_verdict": "current_profile_false_positive"}
{"row_type": "case", "case_id": "R11L11_C31_024060_HEUNGGU_OIL_EAST_SEA_THEMATIC_EVENT_20240603", "symbol": "024060", "company_name": "흥구석유", "round": "R11", "loop": "11", "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "C31_POLICY_SUBSIDY_LEGISLATION_EVENT", "fine_archetype_id": "EAST_SEA_OIL_GAS_THEMATIC_MICROCAP_EVENT_FALSE_POSITIVE", "case_type": "price_moved_without_evidence", "positive_or_counterexample": "counterexample", "best_trigger": "R11L11_T_024060_20240603_Stage2_Event_Watch", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "thematic_event_false_positive_delayed_second_spike", "current_profile_verdict": "current_profile_false_positive", "price_source": "Songdaiki/stock-web", "notes": "The policy event produced tradable momentum but not durable evidence; later lower lows show that policy-event beta needed an event-cap/overheat guard rather than Stage3 promotion."}
{"row_type": "trigger", "trigger_id": "R11L11_T_024060_20240603_Stage2_Event_Watch", "case_id": "R11L11_C31_024060_HEUNGGU_OIL_EAST_SEA_THEMATIC_EVENT_20240603", "symbol": "024060", "company_name": "흥구석유", "round": "R11", "loop": "11", "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "C31_POLICY_SUBSIDY_LEGISLATION_EVENT", "fine_archetype_id": "EAST_SEA_OIL_GAS_THEMATIC_MICROCAP_EVENT_FALSE_POSITIVE", "sector": "석유유통·정책테마", "primary_archetype": "event-thematic microcap without contract/revision bridge", "loop_objective": "coverage_gap_fill|residual_false_positive_mining|sector_specific_rule_discovery|canonical_archetype_compression|4B_non_price_requirement_stress_test", "trigger_type": "Stage2-Event-Watch", "trigger_date": "2024-06-03", "evidence_available_at_that_date": "The policy event produced tradable momentum but not durable evidence; later lower lows show that policy-event beta needed an event-cap/overheat guard rather than Stage3 promotion.", "evidence_source": "Reuters 2024-06-03 East Sea oil/gas exploration approval; stock-web price path confirms blowoff/giveback", "stage2_evidence_fields": ["public_event_or_disclosure", "policy_or_regulatory_optionality", "relative_strength"], "stage3_evidence_fields": [], "stage4b_evidence_fields": ["valuation_blowoff", "positioning_overheat", "price_only_local_peak", "explicit_event_cap"], "stage4c_evidence_fields": ["thesis_evidence_broken"], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/024/024060/2024.csv", "profile_path": "atlas/symbol_profiles/024/024060.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "entry_date": "2024-06-03", "entry_price": 16250, "MFE_30D_pct": 28.92, "MFE_90D_pct": 34.77, "MFE_180D_pct": 34.77, "MFE_1Y_pct": 34.77, "MFE_2Y_pct": null, "MAE_30D_pct": -23.02, "MAE_90D_pct": -23.94, "MAE_180D_pct": -26.46, "MAE_1Y_pct": -26.46, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2024-08-13", "peak_price": 21900, "drawdown_after_peak_pct": -45.43, "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": 0.64, "four_b_full_window_peak_proximity": 0.53, "four_b_timing_verdict": "price_only_local_4B_too_early_then_full_window_event_peak", "four_b_evidence_type": ["price_only", "valuation_blowoff", "positioning_overheat", "explicit_event_cap"], "four_c_protection_label": "hard_4c_late", "trigger_outcome_label": "thematic_event_false_positive_delayed_second_spike", "current_profile_verdict": "current_profile_false_positive", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window", "same_entry_group_id": "R11L11_024060_2024-06-03_16250", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R11L11_C31_024060_HEUNGGU_OIL_EAST_SEA_THEMATIC_EVENT_20240603", "trigger_id": "R11L11_T_024060_20240603_Stage2_Event_Watch", "symbol": "024060", "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "C31_POLICY_SUBSIDY_LEGISLATION_EVENT", "raw_component_scores_before": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 0, "revision_score": 0, "relative_strength_score": 94, "customer_quality_score": 0, "policy_or_regulatory_score": 72, "valuation_repricing_score": 92, "execution_risk_score": 88, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0, "policy_event_specificity_score": 42, "capital_return_execution_score": 0, "event_cap_score": 96, "direct_cashflow_bridge_score": 0, "positioning_overheat_score": 96, "thesis_break_score": 0}, "weighted_score_before": 77.0, "stage_label_before": "Stage3-Yellow-price-risk", "raw_component_scores_after": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 0, "revision_score": 0, "relative_strength_score": 76, "customer_quality_score": 0, "policy_or_regulatory_score": 50, "valuation_repricing_score": 54, "execution_risk_score": 92, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0, "policy_event_specificity_score": 30, "capital_return_execution_score": 0, "event_cap_score": 98, "direct_cashflow_bridge_score": 0, "positioning_overheat_score": 98, "thesis_break_score": 0}, "weighted_score_after": 52.0, "stage_label_after": "Stage2-Event-Watch/4B-overlay", "changed_components": ["policy_event_specificity_score", "direct_cashflow_bridge_score", "capital_return_execution_score", "event_cap_score", "positioning_overheat_score"], "component_delta_explanation": "C31 shadow profile rewards policy events only when the legal/economic transmission path is visible; headline-only event beta is capped and moved to 4B/4C watch.", "MFE_90D_pct": 34.77, "MAE_90D_pct": -23.94, "score_return_alignment_label": "thematic_event_false_positive_delayed_second_spike", "current_profile_verdict": "current_profile_false_positive"}
{"row_type": "residual_contribution", "round": "R11", "loop": "11", "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "C31_POLICY_SUBSIDY_LEGISLATION_EVENT", "new_independent_case_count": 6, "reused_case_count": 1, "new_symbol_count": 5, "same_archetype_new_symbol_count": 5, "same_archetype_new_trigger_family_count": 6, "new_trigger_family_count": 6, "positive_case_count": 2, "counterexample_count": 4, "current_profile_error_count": 6, "tested_existing_calibrated_axes": ["price_only_blowoff_blocks_positive_stage", "full_4b_requires_non_price_evidence", "hard_4c_thesis_break_routes_to_4c", "stage3_green_revision_min"], "residual_error_types_found": ["policy_event_without_cashflow_bridge_false_positive", "policy_beta_weak_execution_counterexample", "asset_route_missed_structural", "price_only_4B_not_full"], "loop_contribution_label": "canonical_archetype_rule_candidate", "do_not_propose_new_weight_delta": false}
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
completed_loop = 11
next_round = R12
next_loop = 11
round_schedule_status = valid
round_sector_consistency = pass
```

## 28. Source Notes

- stock-web manifest: atlas/manifest.json, max_date 2026-02-20.
- stock-web schema: atlas/schema.json, tradable shard columns `d,o,h,l,c,v,a,mc,s,m`.
- Symbol profiles checked: 005380, 402340, 316140, 036460, 004090, 024060.
- OHLC shards checked: 2024 tradable shards for all representative triggers.
- External evidence anchors: Reuters and FT on Korea Corporate Value-up Programme; Reuters/WSJ on South Korea East Sea oil/gas exploration approval. These are narrative evidence anchors only; quantitative calibration uses stock-web rows.
- This document is historical calibration research only, not investment advice and not a live candidate scan.
