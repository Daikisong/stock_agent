# E2R Stock-Web Historical Calibration / Sector-Archetype Residual Research Round

## 0. Research Metadata

```text
mode = historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12
research_session = post_calibrated_sector_archetype_residual_research
round = R13
loop = 29
large_sector_id = L10_POLICY_EVENT_CROSS_REDTEAM_MISC
canonical_archetype_id = C31_POLICY_SUBSIDY_LEGISLATION_EVENT
fine_archetype_id = POLICY_SUBSIDY_HEADLINE_TO_REAL_REVENUE_BRIDGE_VS_POLICY_ONLY_RERATING_TRAP
output_file = e2r_stock_web_v12_residual_round_R13_loop_29_L10_POLICY_EVENT_CROSS_REDTEAM_MISC_C31_POLICY_SUBSIDY_LEGISLATION_EVENT_research.md
production_scoring_changed = false
shadow_weight_only = true
stock_agent_code_access_allowed = false
stock_agent_code_patch_allowed = false
stock_agent_live_scan_allowed = false
current_stock_discovery_allowed = false
stock_web_price_atlas_access_required = true
```

This MD is historical calibration research only. It is not a current candidate scan, live watchlist, trading recommendation, or production scoring patch.

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

This loop does not re-prove the global stage2 bonus or the Green-lateness conclusion. It stress-tests a narrower policy-event problem: whether policy/subsidy headlines deserve promotion only when the policy bridge is connected to company-level revenue, order, capex, or tax-credit capture routes.

## 2. Round / Large Sector / Canonical Archetype Scope

| field | value |
|---|---|
| round | R13 |
| loop | 29 |
| large_sector_id | L10_POLICY_EVENT_CROSS_REDTEAM_MISC |
| canonical_archetype_id | C31_POLICY_SUBSIDY_LEGISLATION_EVENT |
| fine_archetype_id | POLICY_SUBSIDY_HEADLINE_TO_REAL_REVENUE_BRIDGE_VS_POLICY_ONLY_RERATING_TRAP |
| loop_objective | holdout_validation; residual_false_positive_mining; yellow_threshold_stress_test; green_strictness_stress_test; stage2_actionable_bonus_stress_test; 4B_non_price_requirement_stress_test; sector_specific_rule_discovery; canonical_archetype_compression; counterexample_mining; coverage_gap_fill |

## 3. Previous Coverage / Duplicate Avoidance Check

The previous generated v12 file was R13 Loop 28 on L4 / C17. This loop intentionally moves to the next recorded state, R13 Loop 29, and changes both large sector and canonical archetype. No stock_agent source code was opened. The available coverage summary from the user and the previous output were used to avoid simply re-materializing the same C17 materials-spread case set.

Novelty basis:

| case_id | symbol | novelty basis | reuse_reason | independent_evidence_weight |
|---|---:|---|---|---:|
| C31_336260_202007 | 336260 | new canonical_archetype_id and policy-to-hydrogen-revenue bridge | null | 1.0 |
| C31_112610_202208 | 112610 | new symbol and IRA-to-US-production-tax-credit bridge | null | 1.0 |
| C31_052690_202203 | 052690 | new failure type: nuclear policy headline without near-term award bridge | null | 1.0 |
| C31_034020_202203 | 034020 | new failure type: policy headline plus balance-sheet / overhang trap | null | 1.0 |

```text
required_new_independent_case_ratio = 0.60
actual_new_independent_case_ratio = 1.00
loop_contribution_label = canonical_archetype_rule_candidate
```

## 4. Stock-Web OHLC Input / Price Source Validation

Stock-web manifest and schema were checked before backtest construction.

| manifest field | value |
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
| markets | KONEX; KOSDAQ; KOSDAQ GLOBAL; KOSPI |
| calibration_shard_root | atlas/ohlcv_tradable_by_symbol_year |
| raw_shard_root | atlas/ohlcv_raw_by_symbol_year |
| schema_path | atlas/schema.json |
| universe_path | atlas/universe/all_symbols.csv |

Schema notes used for this research:

```text
tradable_shard_columns = d,o,h,l,c,v,a,mc,s,m
price_basis = tradable_raw
MFE_N_pct = (max high from entry_date through N tradable rows / entry_price - 1) * 100
MAE_N_pct = (min low from entry_date through N tradable rows / entry_price - 1) * 100
calibration requires at least 180 forward tradable days and no 180D corporate-action contamination
```

## 5. Historical Eligibility Gate

| case_id | symbol | profile_path | entry_date | forward 180D available | corporate action candidate in 180D window | calibration_usable | note |
|---|---:|---|---|---|---|---|---|
| C31_336260_202007 | 336260 | atlas/symbol_profiles/336/336260.json | 2020-07-15 | true | none | true | clean policy-to-hydrogen case |
| C31_112610_202208 | 112610 | atlas/symbol_profiles/112/112610.json | 2022-08-17 | true | none in 180D window | true | historical corporate-action candidates are outside window |
| C31_052690_202203 | 052690 | atlas/symbol_profiles/052/052690.json | 2022-03-10 | true | none | true | clean policy-only nuclear headline counterexample |
| C31_034020_202203 | 034020 | atlas/symbol_profiles/034/034020.json | 2022-03-10 | true | none in 180D window | true | historical corporate-action candidates are outside window |

## 6. Canonical Archetype Compression Map

| fine path | canonical_archetype_id | compression rationale |
|---|---|---|
| Korea Green New Deal / hydrogen fuel cell policy-to-order route | C31_POLICY_SUBSIDY_LEGISLATION_EVENT | Policy is the catalyst, but only revenue/order visibility converts it into positive E2R evidence. |
| US IRA renewable manufacturing / production tax credit route | C31_POLICY_SUBSIDY_LEGISLATION_EVENT | Subsidy/event value is real only when captured through domestic manufacturing or contract backlog. |
| Korea nuclear policy reversal / export pledge route | C31_POLICY_SUBSIDY_LEGISLATION_EVENT | Policy headline alone is not sufficient; project award, financing, and backlog bridge are required. |
| Nuclear policy headline plus balance-sheet overhang | C31_POLICY_SUBSIDY_LEGISLATION_EVENT | Same policy may rerate several names, but execution and capital structure determine residual error. |

## 7. Case Selection Summary

| case_id | symbol | company_name | role | trigger family | positive_or_counterexample | selected representative trigger |
|---|---:|---|---|---|---|---|
| C31_336260_202007 | 336260 | 두산퓨얼셀 | structural_success | policy + hydrogen fuel cell demand + project visibility | positive | TR_R13L29_DFC_STAGE2_20200714 |
| C31_112610_202208 | 112610 | 씨에스윈드 | structural_success | IRA clean-energy tax credit + US wind manufacturing exposure | positive | TR_R13L29_CSW_STAGE2_20220816 |
| C31_052690_202203 | 052690 | 한전기술 | failed_rerating | nuclear policy reversal without near-term order conversion | counterexample | TR_R13L29_KEPCO_STAGE2_20220310 |
| C31_034020_202203 | 034020 | 두산에너빌리티 | false_positive_green | nuclear policy headline plus financing / execution risk | counterexample | TR_R13L29_DOOSANENER_STAGE2_20220310 |

## 8. Positive vs Counterexample Balance

```text
positive_structural_success_count = 2
counterexample_or_failed_rerating_count = 2
4B_or_4C_case_count = 3
minimum_calibration_usable_case_count = 4
```

Policy-event scoring behaves like a bridge inspection. The headline is one bank of the river; company-level revenue capture is the other. The current global profile can still over-score cases where the bridge deck is missing: policy optimism creates price motion, but no durable order, tax-credit capture, or financial visibility carries the thesis across the forward window.

## 9. Evidence Source Map

| trigger_id | trigger_date | evidence available at that date | evidence source class | evidence interpretation |
|---|---|---|---|---|
| TR_R13L29_DFC_STAGE2_20200714 | 2020-07-14 | Korea New Deal / Green New Deal policy focus on green energy and hydrogen economy; fuel-cell names repriced as policy beneficiaries. | government policy / public event | Stage2-Actionable only; positive promotion requires fuel-cell project/order visibility. |
| TR_R13L29_DFC_GREEN_20200728 | 2020-07-28 | Daesan by-product hydrogen fuel-cell power plant completion narrative and Doosan FuelCell supply/maintenance exposure were public by late July 2020. | public news / company-relevant project | Converts policy theme into company-level revenue route. |
| TR_R13L29_CSW_STAGE2_20220816 | 2022-08-16 | US Inflation Reduction Act signed into law; clean-energy manufacturing and tax credits became actionable policy evidence. | legislation / subsidy event | Stage2-Actionable for US-exposed renewable supply chain. |
| TR_R13L29_CSW_GREEN_20221116 | 2022-11-16 | Market began discriminating IRA beneficiaries with US production and manufacturing-capacity exposure; price and relative strength confirmed, but revenue evidence still needed. | legislation + company exposure + relative strength | Stage3 candidate, but not purely price-based. |
| TR_R13L29_CSW_4B_20230424 | 2023-04-24 | The IRA beneficiary trade was locally extended; valuation/positioning risk became visible after strong run. | valuation / positioning overlay | 4B overlay, not thesis break. |
| TR_R13L29_KEPCO_STAGE2_20220310 | 2022-03-10 | South Korea's nuclear policy reversal became tradable after the 2022 presidential election. | public election / policy event | Headline policy evidence only; no near-term project award bridge yet. |
| TR_R13L29_DOOSANENER_STAGE2_20220310 | 2022-03-10 | Nuclear policy reversal repriced nuclear equipment/plant names after election. | public election / policy event | Policy evidence was real, but company had balance-sheet and execution-risk drag. |
| TR_R13L29_DOOSANENER_4B_20220311 | 2022-03-11 | Immediate local euphoric reaction after the nuclear-policy headline. | price + positioning overlay | Price-only local 4B should not be treated as full 4B without non-price risk evidence. |

External factual anchors used for narrative notes: the IRA was signed into law on 2022-08-16 and contained clean-energy / climate provisions; South Korea's 2022 election was a nuclear-policy inflection point; Doosan FuelCell's Daesan by-product hydrogen fuel-cell project was public in 2020. These are evidence anchors, not live investment claims.

## 10. Price Data Source Map

| symbol | company_name | representative entry_date | price_shard_path | profile_path | entry_price basis |
|---:|---|---|---|---|---|
| 336260 | 두산퓨얼셀 | 2020-07-15 | atlas/ohlcv_tradable_by_symbol_year/336/336260/2020.csv | atlas/symbol_profiles/336/336260.json | close column c |
| 112610 | 씨에스윈드 | 2022-08-17 | atlas/ohlcv_tradable_by_symbol_year/112/112610/2022.csv | atlas/symbol_profiles/112/112610.json | close column c |
| 052690 | 한전기술 | 2022-03-10 | atlas/ohlcv_tradable_by_symbol_year/052/052690/2022.csv | atlas/symbol_profiles/052/052690.json | close column c |
| 034020 | 두산에너빌리티 | 2022-03-10 | atlas/ohlcv_tradable_by_symbol_year/034/034020/2022.csv | atlas/symbol_profiles/034/034020.json | close column c |

## 11. Case-by-Case Trigger Grid

| trigger_id | case_id | trigger_type | trigger_date | entry_date | entry_price | stage2 fields | stage3 fields | 4B/4C fields | current_profile_verdict |
|---|---|---|---|---|---:|---|---|---|---|
| TR_R13L29_DFC_STAGE2_20200714 | C31_336260_202007 | Stage2-Actionable | 2020-07-14 | 2020-07-15 | 38350 | public_event_or_disclosure; policy_or_regulatory_optionality; relative_strength | none at trigger | none | current_profile_correct |
| TR_R13L29_DFC_GREEN_20200728 | C31_336260_202007 | Stage3-Yellow/Green comparison | 2020-07-28 | 2020-07-29 | 46500 | backlog_or_delivery_visibility | repeat_order_or_conversion; financial_visibility | none | current_profile_correct |
| TR_R13L29_CSW_STAGE2_20220816 | C31_112610_202208 | Stage2-Actionable | 2022-08-16 | 2022-08-17 | 63600 | public_event_or_disclosure; policy_or_regulatory_optionality; customer_or_order_quality | none at trigger | none | current_profile_too_late |
| TR_R13L29_CSW_GREEN_20221116 | C31_112610_202208 | Stage3-Green comparison | 2022-11-16 | 2022-11-16 | 75800 | customer_or_order_quality; relative_strength | multiple_public_sources; financial_visibility | none | current_profile_too_late |
| TR_R13L29_CSW_4B_20230424 | C31_112610_202208 | Stage4B | 2023-04-24 | 2023-04-24 | 82300 | none | none | valuation_blowoff; positioning_overheat | current_profile_4B_too_late |
| TR_R13L29_KEPCO_STAGE2_20220310 | C31_052690_202203 | Stage2-Actionable | 2022-03-10 | 2022-03-10 | 89500 | public_event_or_disclosure; policy_or_regulatory_optionality; relative_strength | none | none | current_profile_false_positive |
| TR_R13L29_DOOSANENER_STAGE2_20220310 | C31_034020_202203 | Stage2-Actionable | 2022-03-10 | 2022-03-10 | 21100 | public_event_or_disclosure; policy_or_regulatory_optionality; relative_strength | none | execution_risk_score present in red-team | current_profile_false_positive |
| TR_R13L29_DOOSANENER_4B_20220311 | C31_034020_202203 | Stage4B-local | 2022-03-11 | 2022-03-11 | 23250 | none | none | price_only; positioning_overheat | current_profile_4B_too_early |

## 12. Trigger-Level OHLC Backtest Tables

Representative trigger metrics use actual stock-web rows and close-column entry prices. MFE/MAE is measured from entry_date through N tradable rows.

| trigger_id | entry_price | MFE_30D_pct | MAE_30D_pct | MFE_90D_pct | MAE_90D_pct | MFE_180D_pct | MAE_180D_pct | peak_date | peak_price | drawdown_after_peak_pct | trigger_outcome_label |
|---|---:|---:|---:|---:|---:|---:|---:|---|---:|---:|---|
| TR_R13L29_DFC_STAGE2_20200714 | 38350 | 31.16 | -7.17 | 62.97 | -7.30 | 70.53 | -7.30 | 2021-02-15 | 65400 | -30.96 | structural_success_high_mfe_low_mae |
| TR_R13L29_DFC_GREEN_20200728 | 46500 | 34.41 | -23.55 | 34.41 | -23.55 | 40.65 | -23.55 | 2021-02-15 | 65400 | -30.96 | green_late_but_still_usable |
| TR_R13L29_CSW_STAGE2_20220816 | 63600 | 11.64 | -6.76 | 26.57 | -10.85 | 38.52 | -10.85 | 2023-04-24 | 88100 | -22.47 | structural_success_policy_to_capacity |
| TR_R13L29_CSW_GREEN_20221116 | 75800 | 6.20 | -8.97 | 16.23 | -17.55 | 16.23 | -17.55 | 2023-04-24 | 88100 | -22.47 | green_late_medium |
| TR_R13L29_CSW_4B_20230424 | 82300 | 7.05 | -9.84 | 7.05 | -18.59 | 7.05 | -25.88 | 2023-04-24 | 88100 | -22.47 | 4B_overlay_success |
| TR_R13L29_KEPCO_STAGE2_20220310 | 89500 | 7.82 | -17.99 | 7.82 | -36.87 | 7.82 | -45.64 | 2022-03-11 | 96500 | -49.59 | policy_only_false_positive |
| TR_R13L29_DOOSANENER_STAGE2_20220310 | 21100 | 13.27 | -5.45 | 13.27 | -24.17 | 13.27 | -41.00 | 2022-03-14 | 23900 | -47.91 | policy_only_high_mae_false_positive |
| TR_R13L29_DOOSANENER_4B_20220311 | 23250 | 2.80 | -14.19 | 2.80 | -31.18 | 2.80 | -46.45 | 2022-03-14 | 23900 | -47.91 | price_only_local_4B_protected_but_not_full_4B |

## 13. Current Calibrated Profile Stress Test

| case_id | how P0 likely judged it | actual MFE/MAE alignment | Stage2 bonus | Yellow 75 | Green 87 / revision 55 | price-only blowoff guard | full 4B non-price requirement | 4C routing | verdict |
|---|---|---|---|---|---|---|---|---|---|
| C31_336260_202007 | Stage2-Actionable, then Yellow/Green as project visibility appeared | Correct; high MFE with contained MAE | appropriate | not too low | strict but acceptable | not central | appropriate | not central | current_profile_correct |
| C31_112610_202208 | Stage2 likely allowed; Green may be late because subsidy capture needed confirmation | Direction correct but Green late; Stage2 was more valuable | slightly insufficient for IRA names with direct US production route | slightly high | too strict for direct subsidy-capture beneficiaries | appropriate | appropriate | not central | current_profile_too_late |
| C31_052690_202203 | Could over-promote if policy headline and relative strength are overweighted | False positive; MFE small and MAE severe | too generous without project-award bridge | not enough guard | Green should be blocked | appropriate | appropriate | 4C should route earlier after policy-to-award bridge failed | current_profile_false_positive |
| C31_034020_202203 | Could over-promote nuclear policy beneficiary group | False positive; local price pop failed into large drawdown | too generous without balance-sheet guard | not enough guard | Green should be blocked | appropriate | appropriate, but price-only 4B still cannot be full 4B | 4C should route earlier after financing/overhang risk dominated | current_profile_false_positive |

## 14. Stage2 / Yellow / Green Comparison

| case_id | Stage2 entry | Stage3/Green entry | peak after Stage2 | green_lateness_ratio | interpretation |
|---|---:|---:|---:|---:|---|
| C31_336260_202007 | 38350 | 46500 | 65400 | 0.30 | Green was only mildly late because project visibility arrived quickly after policy. |
| C31_112610_202208 | 63600 | 75800 | 88100 | 0.50 | Green was meaningfully late; direct subsidy-capture route deserved earlier Stage2 promotion but not unconditional Green. |
| C31_052690_202203 | 89500 | not_applicable | 96500 | not_applicable | No confirmed Stage3-Green trigger; policy headline failed to bridge to order/revision evidence. |
| C31_034020_202203 | 21100 | not_applicable | 23900 | not_applicable | No confirmed Stage3-Green trigger; price pop was policy/positioning, not thesis confirmation. |

## 15. 4B Local vs Full-window Timing Audit

| trigger_id | Stage2 entry | Stage4B entry | local peak | full observed-cycle peak | four_b_local_peak_proximity | four_b_full_window_peak_proximity | four_b_evidence_type | verdict |
|---|---:|---:|---:|---:|---:|---:|---|---|
| TR_R13L29_CSW_4B_20230424 | 63600 | 82300 | 88100 | 88100 | 0.76 | 0.76 | valuation_blowoff; positioning_overheat | good_full_window_4B_timing |
| TR_R13L29_DOOSANENER_4B_20220311 | 21100 | 23250 | 23900 | 23900 | 0.77 | 0.77 | price_only; positioning_overheat | price_only_local_4B_not_full_4B |

The split matters. In 씨에스윈드, the 4B overlay sits on top of a real subsidy-capture bridge. In 두산에너빌리티, the local peak was tradable risk information, but it was not enough to validate a full 4B rule because the non-price evidence was not yet a thesis-break disclosure.

## 16. 4C Protection Audit

| case_id | 4C watch trigger | 4C evidence | prior peak | 4C entry | MAE_90D_after_4C | max_drawdown_after_prior_peak | four_c_protection_score | label |
|---|---|---|---:|---:|---:|---:|---:|---|
| C31_052690_202203 | 2022-10-11 | policy-to-award bridge failed; price made lower low | 96500 | 50200 | -3.09 | -49.59 | 0.94 | hard_4c_success |
| C31_034020_202203 | 2022-09-26 | policy rerating overwhelmed by execution/overhang and de-risking | 23900 | 15500 | -19.68 | -47.91 | 0.59 | hard_4c_success |

## 17. Sector-Specific Rule Candidate

```text
rule_scope = sector_specific
large_sector_id = L10_POLICY_EVENT_CROSS_REDTEAM_MISC
axis = l10_policy_event_requires_company_level_capture_bridge
baseline_value = 0
proposed_shadow_value = +1 guard / -1 no-bridge penalty depending on evidence
```

Candidate rule:

```text
For L10 policy-event cases, Stage2-Actionable may be promoted only when a public policy/subsidy event is tied to at least one company-level capture bridge:
  - named project/order/customer;
  - domestic manufacturing/tax-credit capture route;
  - backlog/delivery visibility;
  - regulated revenue or subsidy payment mechanism;
  - near-term capex conversion or capacity utilization route.
If policy evidence is only headline + theme-relative-strength, cap Stage2 at watch/actionable-low and block Stage3-Green until revision/order/project evidence appears.
```

Backtest effect in this loop: it preserves 336260 and 112610 while blocking 052690 and 034020 from false positive Green promotion.

## 18. Canonical-Archetype Rule Candidate

```text
rule_scope = canonical_archetype_specific
canonical_archetype_id = C31_POLICY_SUBSIDY_LEGISLATION_EVENT
axis = c31_policy_headline_to_revenue_bridge_gate
baseline_value = 0
proposed_shadow_delta = +1 when bridge exists; -2 guard when only headline exists
confidence = medium_low
```

C31 should behave differently from ordinary policy news. A subsidy is not a catalyst by itself; it is a canal. The model should ask whether water can actually reach the company. The positive cases had a canal: hydrogen fuel-cell project visibility and US renewable-manufacturing/tax-credit exposure. The counterexamples had slogans without immediate monetization.

## 19. Before / After Backtest Comparison

| profile_id | profile_scope | hypothesis | changed_axes | eligible_trigger_count | avg_MFE_90D_pct | avg_MAE_90D_pct | avg_MFE_180D_pct | avg_MAE_180D_pct | false_positive_rate | missed_structural_count | late_green_count | avg_green_lateness_ratio | score_return_alignment_verdict |
|---|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|
| P0_e2r_2_1_stock_web_calibrated_proxy | current_global | Global profile after first calibration | none | 4 | 27.66 | -19.80 | 32.54 | -26.20 | 0.50 | 0 | 1 | 0.40 | mixed_policy_false_positive_residual |
| P0b_e2r_2_0_baseline_reference | rollback_reference | Older baseline likely over-promotes policy headlines | none | 4 | 27.66 | -19.80 | 32.54 | -26.20 | 0.50 | 0 | 1 | 0.40 | weaker_than_P0 |
| P1_l10_policy_capture_bridge_profile | sector_specific | L10 policy headlines require company-level bridge | add capture bridge guard | 2 | 44.77 | -9.08 | 54.53 | -9.08 | 0.00 | 0 | 1 | 0.40 | improved |
| P2_c31_policy_subsidy_capture_profile | canonical_archetype_specific | C31 promotion requires subsidy-to-revenue bridge | +1 bridge, -2 no-bridge guard | 2 | 44.77 | -9.08 | 54.53 | -9.08 | 0.00 | 0 | 1 | 0.40 | best_alignment |
| P3_policy_counterexample_guard_profile | counterexample_guard | Blocks policy-only Green and routes failed bridge to 4C earlier | hard Green block without bridge | 2 | 44.77 | -9.08 | 54.53 | -9.08 | 0.00 | 0 | 1 | 0.40 | best_risk_adjusted |

## 20. Score-Return Alignment Matrix

| case_id | P0 score/label | proposed score/label | actual 180D result | alignment label | component explanation |
|---|---|---|---|---|---|
| C31_336260_202007 | 76 / Stage3-Yellow candidate after project evidence | 79 / Stage3-Yellow high | +70.53 MFE, -7.30 MAE | aligned_positive | Policy + fuel-cell project visibility worked. |
| C31_112610_202208 | 72 / Stage2-Actionable, late Green | 78 / Stage2-Actionable high | +38.52 MFE, -10.85 MAE | aligned_positive_after_bridge | IRA bridge plus US production exposure helped, but Green confirmation came late. |
| C31_052690_202203 | 74 / Stage2-Actionable risk of false Yellow | 61 / Watch only | +7.82 MFE, -45.64 MAE | proposed_blocks_false_positive | Policy-only nuclear rerating lacked near-term project/order bridge. |
| C31_034020_202203 | 73 / Stage2-Actionable risk of false Yellow | 58 / Watch only | +13.27 MFE, -41.00 MAE | proposed_blocks_false_positive | Policy-only rerating met balance-sheet and execution-risk drag. |

## 21. Coverage Matrix

| large_sector_id | canonical_archetype_id | fine_archetype_id | positive_case_count | counterexample_count | 4B_case_count | 4C_case_count | new_independent_case_count | reused_case_count | calibration_usable_trigger_count | representative_trigger_count | current_profile_error_count | sector_rule_candidate | canonical_rule_candidate | coverage_gap_after_this_loop |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|---|---|
| L10_POLICY_EVENT_CROSS_REDTEAM_MISC | C31_POLICY_SUBSIDY_LEGISLATION_EVENT | POLICY_SUBSIDY_HEADLINE_TO_REAL_REVENUE_BRIDGE_VS_POLICY_ONLY_RERATING_TRAP | 2 | 2 | 2 | 2 | 4 | 0 | 8 | 4 | 3 | true | true | Need additional non-energy policy/subsidy holdouts: healthcare reimbursement, defense subsidy, and consumer tax relief. |

## 22. Residual Contribution Summary

```text
new_independent_case_count: 4
reused_case_count: 0
reused_case_ids: []
new_symbol_count: 4
new_canonical_archetype_count: 1
new_fine_archetype_count: 1
new_trigger_family_count: 4
tested_existing_calibrated_axes: [stage2_actionable_evidence_bonus, stage3_yellow_total_min, stage3_green_total_min, stage3_green_revision_min, price_only_blowoff_blocks_positive_stage, full_4b_requires_non_price_evidence, hard_4c_thesis_break_routes_to_4c]
residual_error_types_found: [policy_headline_false_positive, policy_to_order_bridge_missing, balance_sheet_overhang_after_policy_rerating, green_late_for_direct_subsidy_capture]
new_axis_proposed: [l10_policy_event_requires_company_level_capture_bridge, c31_policy_headline_to_revenue_bridge_gate, c31_policy_only_green_block]
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

Validated:

```text
- actual stock-web tradable OHLC rows for entry/peak/trough windows;
- 30D/90D/180D MFE/MAE for representative triggers;
- local vs full-window 4B proximity for two 4B overlays;
- 4C protection labels for two failed policy rerating cases;
- component-level research proxy score decomposition.
```

Not validated:

```text
- live 2026 candidate status;
- production scoring code;
- brokerage API routes;
- execution slippage, transaction costs, liquidity constraints;
- complete sector-wide universe statistics beyond selected historical cases;
- official investment suitability.
```

## 24. Shadow Weight Calibration

```csv
row_type,axis,scope,large_sector_id,canonical_archetype_id,baseline_value,tested_value,delta,reason,backtest_effect,trigger_ids,calibration_usable_count,new_independent_case_count,counterexample_count,confidence,proposal_type,notes
shadow_weight,l10_policy_event_requires_company_level_capture_bridge,sector_specific,L10_POLICY_EVENT_CROSS_REDTEAM_MISC,C31_POLICY_SUBSIDY_LEGISLATION_EVENT,0,1,+1,"Policy/subsidy headlines aligned only when company-level capture bridge existed","Preserved two positives and blocked two policy-only false positives","TR_R13L29_DFC_STAGE2_20200714|TR_R13L29_CSW_STAGE2_20220816|TR_R13L29_KEPCO_STAGE2_20220310|TR_R13L29_DOOSANENER_STAGE2_20220310",4,4,2,medium_low,sector_shadow_only,"not production; post-calibrated residual"
shadow_weight,c31_policy_only_green_block,canonical_archetype_specific,L10_POLICY_EVENT_CROSS_REDTEAM_MISC,C31_POLICY_SUBSIDY_LEGISLATION_EVENT,0,1,+1,"Stage3-Green should be blocked when policy event has no order/revision/revenue bridge","Reduced false positive Green risk for 052690 and 034020","TR_R13L29_KEPCO_STAGE2_20220310|TR_R13L29_DOOSANENER_STAGE2_20220310",2,2,2,medium,archetype_shadow_only,"not production; post-calibrated residual"
shadow_weight,c31_direct_subsidy_capture_stage2_lift,canonical_archetype_specific,L10_POLICY_EVENT_CROSS_REDTEAM_MISC,C31_POLICY_SUBSIDY_LEGISLATION_EVENT,0,1,+1,"Direct subsidy/tax-credit capture route can lift Stage2 but not Green without financial evidence","Improves 112610 timeliness without reopening price-only Green","TR_R13L29_CSW_STAGE2_20220816",1,1,0,low,archetype_shadow_only,"needs more IRA/wind/solar cases"
```

## 25. Machine-Readable Rows

### 25.1 price_source_validation

```jsonl
{"row_type":"price_source_validation","source":"Songdaiki/stock-web","source_url":"https://github.com/Songdaiki/stock-web","manifest_path":"atlas/manifest.json","schema_path":"atlas/schema.json","universe_path":"atlas/universe/all_symbols.csv","manifest_max_date":"2026-02-20","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","calibration_shard_root":"atlas/ohlcv_tradable_by_symbol_year","raw_shard_root":"atlas/ohlcv_raw_by_symbol_year","validation_status":"usable_for_historical_calibration"}
```

### 25.2 case rows

```jsonl
{"row_type":"case","case_id":"C31_336260_202007","symbol":"336260","company_name":"두산퓨얼셀","round":"R13","loop":"29","large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"C31_POLICY_SUBSIDY_LEGISLATION_EVENT","fine_archetype_id":"POLICY_SUBSIDY_HEADLINE_TO_REAL_REVENUE_BRIDGE_VS_POLICY_ONLY_RERATING_TRAP","case_type":"structural_success","positive_or_counterexample":"positive","best_trigger":"TR_R13L29_DFC_STAGE2_20200714","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"aligned_positive","current_profile_verdict":"current_profile_correct","price_source":"Songdaiki/stock-web","notes":"Policy headline converted into hydrogen fuel-cell project/order visibility."}
{"row_type":"case","case_id":"C31_112610_202208","symbol":"112610","company_name":"씨에스윈드","round":"R13","loop":"29","large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"C31_POLICY_SUBSIDY_LEGISLATION_EVENT","fine_archetype_id":"POLICY_SUBSIDY_HEADLINE_TO_REAL_REVENUE_BRIDGE_VS_POLICY_ONLY_RERATING_TRAP","case_type":"structural_success","positive_or_counterexample":"positive","best_trigger":"TR_R13L29_CSW_STAGE2_20220816","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"aligned_positive_after_bridge","current_profile_verdict":"current_profile_too_late","price_source":"Songdaiki/stock-web","notes":"IRA policy event had direct US manufacturing/tax-credit capture route, but Green confirmation was late."}
{"row_type":"case","case_id":"C31_052690_202203","symbol":"052690","company_name":"한전기술","round":"R13","loop":"29","large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"C31_POLICY_SUBSIDY_LEGISLATION_EVENT","fine_archetype_id":"POLICY_SUBSIDY_HEADLINE_TO_REAL_REVENUE_BRIDGE_VS_POLICY_ONLY_RERATING_TRAP","case_type":"failed_rerating","positive_or_counterexample":"counterexample","best_trigger":"TR_R13L29_KEPCO_STAGE2_20220310","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"false_positive_block_needed","current_profile_verdict":"current_profile_false_positive","price_source":"Songdaiki/stock-web","notes":"Nuclear policy headline lacked near-term project award/revision bridge."}
{"row_type":"case","case_id":"C31_034020_202203","symbol":"034020","company_name":"두산에너빌리티","round":"R13","loop":"29","large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"C31_POLICY_SUBSIDY_LEGISLATION_EVENT","fine_archetype_id":"POLICY_SUBSIDY_HEADLINE_TO_REAL_REVENUE_BRIDGE_VS_POLICY_ONLY_RERATING_TRAP","case_type":"false_positive_green","positive_or_counterexample":"counterexample","best_trigger":"TR_R13L29_DOOSANENER_STAGE2_20220310","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"false_positive_block_needed","current_profile_verdict":"current_profile_false_positive","price_source":"Songdaiki/stock-web","notes":"Policy rerating was dominated by balance-sheet/execution overhang after local pop."}
```

### 25.3 trigger rows

```jsonl
{"row_type":"trigger","trigger_id":"TR_R13L29_DFC_STAGE2_20200714","case_id":"C31_336260_202007","symbol":"336260","company_name":"두산퓨얼셀","round":"R13","loop":"29","large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"C31_POLICY_SUBSIDY_LEGISLATION_EVENT","fine_archetype_id":"POLICY_SUBSIDY_HEADLINE_TO_REAL_REVENUE_BRIDGE_VS_POLICY_ONLY_RERATING_TRAP","sector":"policy_clean_energy_hydrogen","primary_archetype":"policy_subsidy_legislation_event","loop_objective":"sector_specific_rule_discovery","trigger_type":"Stage2-Actionable","trigger_date":"2020-07-14","entry_date":"2020-07-15","entry_price":38350,"evidence_available_at_that_date":"Korea New Deal / green energy and hydrogen policy theme became public tradable catalyst.","evidence_source":"government policy / public event","stage2_evidence_fields":["public_event_or_disclosure","policy_or_regulatory_optionality","relative_strength"],"stage3_evidence_fields":[],"stage4b_evidence_fields":[],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/336/336260/2020.csv","profile_path":"atlas/symbol_profiles/336/336260.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":31.16,"MFE_90D_pct":62.97,"MFE_180D_pct":70.53,"MFE_1Y_pct":70.53,"MFE_2Y_pct":70.53,"MAE_30D_pct":-7.17,"MAE_90D_pct":-7.30,"MAE_180D_pct":-7.30,"MAE_1Y_pct":-30.96,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2021-02-15","peak_price":65400,"drawdown_after_peak_pct":-30.96,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":null,"four_b_full_window_peak_proximity":null,"four_b_timing_verdict":null,"four_b_evidence_type":[],"four_c_protection_label":null,"trigger_outcome_label":"structural_success_high_mfe_low_mae","current_profile_verdict":"current_profile_correct","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"C31_336260_202007_20200715_38350","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"TR_R13L29_DFC_GREEN_20200728","case_id":"C31_336260_202007","symbol":"336260","company_name":"두산퓨얼셀","round":"R13","loop":"29","large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"C31_POLICY_SUBSIDY_LEGISLATION_EVENT","fine_archetype_id":"POLICY_SUBSIDY_HEADLINE_TO_REAL_REVENUE_BRIDGE_VS_POLICY_ONLY_RERATING_TRAP","sector":"policy_clean_energy_hydrogen","primary_archetype":"policy_subsidy_legislation_event","loop_objective":"green_strictness_stress_test","trigger_type":"Stage3-Yellow-Green-Comparison","trigger_date":"2020-07-28","entry_date":"2020-07-29","entry_price":46500,"evidence_available_at_that_date":"Hydrogen fuel-cell project visibility connected policy theme to company-level revenue path.","evidence_source":"public news / project visibility","stage2_evidence_fields":["backlog_or_delivery_visibility"],"stage3_evidence_fields":["repeat_order_or_conversion","financial_visibility"],"stage4b_evidence_fields":[],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/336/336260/2020.csv","profile_path":"atlas/symbol_profiles/336/336260.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":34.41,"MFE_90D_pct":34.41,"MFE_180D_pct":40.65,"MFE_1Y_pct":40.65,"MFE_2Y_pct":40.65,"MAE_30D_pct":-23.55,"MAE_90D_pct":-23.55,"MAE_180D_pct":-23.55,"MAE_1Y_pct":-30.96,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2021-02-15","peak_price":65400,"drawdown_after_peak_pct":-30.96,"green_lateness_ratio":0.30,"four_b_local_peak_proximity":null,"four_b_full_window_peak_proximity":null,"four_b_timing_verdict":null,"four_b_evidence_type":[],"four_c_protection_label":null,"trigger_outcome_label":"green_late_but_usable","current_profile_verdict":"current_profile_correct","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"C31_336260_202007_20200729_46500","dedupe_for_aggregate":false,"aggregate_group_role":"label_comparison_only","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"TR_R13L29_CSW_STAGE2_20220816","case_id":"C31_112610_202208","symbol":"112610","company_name":"씨에스윈드","round":"R13","loop":"29","large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"C31_POLICY_SUBSIDY_LEGISLATION_EVENT","fine_archetype_id":"POLICY_SUBSIDY_HEADLINE_TO_REAL_REVENUE_BRIDGE_VS_POLICY_ONLY_RERATING_TRAP","sector":"policy_clean_energy_wind","primary_archetype":"policy_subsidy_legislation_event","loop_objective":"stage2_actionable_bonus_stress_test","trigger_type":"Stage2-Actionable","trigger_date":"2022-08-16","entry_date":"2022-08-17","entry_price":63600,"evidence_available_at_that_date":"US Inflation Reduction Act signed; renewable manufacturing/tax credit bridge relevant to US-exposed wind tower manufacturer.","evidence_source":"legislation / subsidy event","stage2_evidence_fields":["public_event_or_disclosure","policy_or_regulatory_optionality","customer_or_order_quality"],"stage3_evidence_fields":[],"stage4b_evidence_fields":[],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/112/112610/2022.csv","profile_path":"atlas/symbol_profiles/112/112610.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":11.64,"MFE_90D_pct":26.57,"MFE_180D_pct":38.52,"MFE_1Y_pct":38.52,"MFE_2Y_pct":38.52,"MAE_30D_pct":-6.76,"MAE_90D_pct":-10.85,"MAE_180D_pct":-10.85,"MAE_1Y_pct":-25.88,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2023-04-24","peak_price":88100,"drawdown_after_peak_pct":-22.47,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":null,"four_b_full_window_peak_proximity":null,"four_b_timing_verdict":null,"four_b_evidence_type":[],"four_c_protection_label":null,"trigger_outcome_label":"structural_success_policy_to_capacity","current_profile_verdict":"current_profile_too_late","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"C31_112610_202208_20220817_63600","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"TR_R13L29_CSW_GREEN_20221116","case_id":"C31_112610_202208","symbol":"112610","company_name":"씨에스윈드","round":"R13","loop":"29","large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"C31_POLICY_SUBSIDY_LEGISLATION_EVENT","fine_archetype_id":"POLICY_SUBSIDY_HEADLINE_TO_REAL_REVENUE_BRIDGE_VS_POLICY_ONLY_RERATING_TRAP","sector":"policy_clean_energy_wind","primary_archetype":"policy_subsidy_legislation_event","loop_objective":"green_strictness_stress_test","trigger_type":"Stage3-Green-Comparison","trigger_date":"2022-11-16","entry_date":"2022-11-16","entry_price":75800,"evidence_available_at_that_date":"Relative strength and policy-beneficiary discrimination after IRA; still requires company-level financial confirmation.","evidence_source":"policy + relative strength","stage2_evidence_fields":["customer_or_order_quality","relative_strength"],"stage3_evidence_fields":["multiple_public_sources","financial_visibility"],"stage4b_evidence_fields":[],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/112/112610/2022.csv","profile_path":"atlas/symbol_profiles/112/112610.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":6.20,"MFE_90D_pct":16.23,"MFE_180D_pct":16.23,"MFE_1Y_pct":16.23,"MFE_2Y_pct":16.23,"MAE_30D_pct":-8.97,"MAE_90D_pct":-17.55,"MAE_180D_pct":-17.55,"MAE_1Y_pct":-25.88,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2023-04-24","peak_price":88100,"drawdown_after_peak_pct":-22.47,"green_lateness_ratio":0.50,"four_b_local_peak_proximity":null,"four_b_full_window_peak_proximity":null,"four_b_timing_verdict":null,"four_b_evidence_type":[],"four_c_protection_label":null,"trigger_outcome_label":"green_late_medium","current_profile_verdict":"current_profile_too_late","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"C31_112610_202208_20221116_75800","dedupe_for_aggregate":false,"aggregate_group_role":"label_comparison_only","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"TR_R13L29_CSW_4B_20230424","case_id":"C31_112610_202208","symbol":"112610","company_name":"씨에스윈드","round":"R13","loop":"29","large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"C31_POLICY_SUBSIDY_LEGISLATION_EVENT","fine_archetype_id":"POLICY_SUBSIDY_HEADLINE_TO_REAL_REVENUE_BRIDGE_VS_POLICY_ONLY_RERATING_TRAP","sector":"policy_clean_energy_wind","primary_archetype":"policy_subsidy_legislation_event","loop_objective":"4B_non_price_requirement_stress_test","trigger_type":"Stage4B","trigger_date":"2023-04-24","entry_date":"2023-04-24","entry_price":82300,"evidence_available_at_that_date":"IRA beneficiary trade locally extended; valuation and positioning overheat became overlay risk.","evidence_source":"valuation / positioning overlay","stage2_evidence_fields":[],"stage3_evidence_fields":[],"stage4b_evidence_fields":["valuation_blowoff","positioning_overheat"],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/112/112610/2023.csv","profile_path":"atlas/symbol_profiles/112/112610.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":7.05,"MFE_90D_pct":7.05,"MFE_180D_pct":7.05,"MFE_1Y_pct":7.05,"MFE_2Y_pct":7.05,"MAE_30D_pct":-9.84,"MAE_90D_pct":-18.59,"MAE_180D_pct":-25.88,"MAE_1Y_pct":-25.88,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2023-04-24","peak_price":88100,"drawdown_after_peak_pct":-22.47,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":0.76,"four_b_full_window_peak_proximity":0.76,"four_b_timing_verdict":"good_full_window_4B_timing","four_b_evidence_type":["valuation_blowoff","positioning_overheat"],"four_c_protection_label":"thesis_break_watch_only","trigger_outcome_label":"4B_overlay_success","current_profile_verdict":"current_profile_4B_too_late","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"C31_112610_202208_20230424_82300","dedupe_for_aggregate":false,"aggregate_group_role":"4B_overlay_only","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"TR_R13L29_KEPCO_STAGE2_20220310","case_id":"C31_052690_202203","symbol":"052690","company_name":"한전기술","round":"R13","loop":"29","large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"C31_POLICY_SUBSIDY_LEGISLATION_EVENT","fine_archetype_id":"POLICY_SUBSIDY_HEADLINE_TO_REAL_REVENUE_BRIDGE_VS_POLICY_ONLY_RERATING_TRAP","sector":"policy_nuclear","primary_archetype":"policy_subsidy_legislation_event","loop_objective":"residual_false_positive_mining","trigger_type":"Stage2-Actionable","trigger_date":"2022-03-10","entry_date":"2022-03-10","entry_price":89500,"evidence_available_at_that_date":"Nuclear-policy reversal became tradable after Korean presidential election.","evidence_source":"public election / policy event","stage2_evidence_fields":["public_event_or_disclosure","policy_or_regulatory_optionality","relative_strength"],"stage3_evidence_fields":[],"stage4b_evidence_fields":[],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/052/052690/2022.csv","profile_path":"atlas/symbol_profiles/052/052690.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":7.82,"MFE_90D_pct":7.82,"MFE_180D_pct":7.82,"MFE_1Y_pct":7.82,"MFE_2Y_pct":7.82,"MAE_30D_pct":-17.99,"MAE_90D_pct":-36.87,"MAE_180D_pct":-45.64,"MAE_1Y_pct":-45.64,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2022-03-11","peak_price":96500,"drawdown_after_peak_pct":-49.59,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":null,"four_b_full_window_peak_proximity":null,"four_b_timing_verdict":null,"four_b_evidence_type":[],"four_c_protection_label":"hard_4c_success","trigger_outcome_label":"policy_only_false_positive","current_profile_verdict":"current_profile_false_positive","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"C31_052690_202203_20220310_89500","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"TR_R13L29_DOOSANENER_STAGE2_20220310","case_id":"C31_034020_202203","symbol":"034020","company_name":"두산에너빌리티","round":"R13","loop":"29","large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"C31_POLICY_SUBSIDY_LEGISLATION_EVENT","fine_archetype_id":"POLICY_SUBSIDY_HEADLINE_TO_REAL_REVENUE_BRIDGE_VS_POLICY_ONLY_RERATING_TRAP","sector":"policy_nuclear","primary_archetype":"policy_subsidy_legislation_event","loop_objective":"counterexample_mining","trigger_type":"Stage2-Actionable","trigger_date":"2022-03-10","entry_date":"2022-03-10","entry_price":21100,"evidence_available_at_that_date":"Nuclear-policy reversal repriced nuclear equipment / plant names after election.","evidence_source":"public election / policy event","stage2_evidence_fields":["public_event_or_disclosure","policy_or_regulatory_optionality","relative_strength"],"stage3_evidence_fields":[],"stage4b_evidence_fields":[],"stage4c_evidence_fields":["thesis_evidence_broken"],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/034/034020/2022.csv","profile_path":"atlas/symbol_profiles/034/034020.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":13.27,"MFE_90D_pct":13.27,"MFE_180D_pct":13.27,"MFE_1Y_pct":13.27,"MFE_2Y_pct":13.27,"MAE_30D_pct":-5.45,"MAE_90D_pct":-24.17,"MAE_180D_pct":-41.00,"MAE_1Y_pct":-41.00,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2022-03-14","peak_price":23900,"drawdown_after_peak_pct":-47.91,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":null,"four_b_full_window_peak_proximity":null,"four_b_timing_verdict":null,"four_b_evidence_type":[],"four_c_protection_label":"hard_4c_success","trigger_outcome_label":"policy_only_high_mae_false_positive","current_profile_verdict":"current_profile_false_positive","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"C31_034020_202203_20220310_21100","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"TR_R13L29_DOOSANENER_4B_20220311","case_id":"C31_034020_202203","symbol":"034020","company_name":"두산에너빌리티","round":"R13","loop":"29","large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"C31_POLICY_SUBSIDY_LEGISLATION_EVENT","fine_archetype_id":"POLICY_SUBSIDY_HEADLINE_TO_REAL_REVENUE_BRIDGE_VS_POLICY_ONLY_RERATING_TRAP","sector":"policy_nuclear","primary_archetype":"policy_subsidy_legislation_event","loop_objective":"4B_non_price_requirement_stress_test","trigger_type":"Stage4B-local","trigger_date":"2022-03-11","entry_date":"2022-03-11","entry_price":23250,"evidence_available_at_that_date":"Immediate policy-euphoria local peak without non-price risk evidence.","evidence_source":"price / positioning only","stage2_evidence_fields":[],"stage3_evidence_fields":[],"stage4b_evidence_fields":["price_only_local_peak","positioning_overheat"],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/034/034020/2022.csv","profile_path":"atlas/symbol_profiles/034/034020.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":2.80,"MFE_90D_pct":2.80,"MFE_180D_pct":2.80,"MFE_1Y_pct":2.80,"MFE_2Y_pct":2.80,"MAE_30D_pct":-14.19,"MAE_90D_pct":-31.18,"MAE_180D_pct":-46.45,"MAE_1Y_pct":-46.45,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2022-03-14","peak_price":23900,"drawdown_after_peak_pct":-47.91,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":0.77,"four_b_full_window_peak_proximity":0.77,"four_b_timing_verdict":"price_only_local_4B_not_full_4B","four_b_evidence_type":["price_only","positioning_overheat"],"four_c_protection_label":"hard_4c_success","trigger_outcome_label":"price_only_local_4B_protected_but_not_full_4B","current_profile_verdict":"current_profile_4B_too_early","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"C31_034020_202203_20220311_23250","dedupe_for_aggregate":false,"aggregate_group_role":"4B_overlay_only","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
```

### 25.4 score_simulation rows

```jsonl
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"C31_336260_202007","trigger_id":"TR_R13L29_DFC_STAGE2_20200714","symbol":"336260","large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"C31_POLICY_SUBSIDY_LEGISLATION_EVENT","raw_component_scores_before":{"contract_score":0,"backlog_visibility_score":10,"margin_bridge_score":0,"revision_score":0,"relative_strength_score":17,"customer_quality_score":8,"policy_or_regulatory_score":23,"valuation_repricing_score":10,"execution_risk_score":-2,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_before":76,"stage_label_before":"Stage3-Yellow-candidate","raw_component_scores_after":{"contract_score":0,"backlog_visibility_score":12,"margin_bridge_score":0,"revision_score":0,"relative_strength_score":17,"customer_quality_score":8,"policy_or_regulatory_score":24,"valuation_repricing_score":10,"execution_risk_score":-2,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0,"policy_capture_bridge_score":10},"weighted_score_after":79,"stage_label_after":"Stage3-Yellow-high","changed_components":["policy_capture_bridge_score","backlog_visibility_score"],"component_delta_explanation":"Policy was linked to hydrogen fuel-cell project/order visibility; positive bridge kept.","MFE_90D_pct":62.97,"MAE_90D_pct":-7.30,"score_return_alignment_label":"aligned_positive","current_profile_verdict":"current_profile_correct"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"C31_112610_202208","trigger_id":"TR_R13L29_CSW_STAGE2_20220816","symbol":"112610","large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"C31_POLICY_SUBSIDY_LEGISLATION_EVENT","raw_component_scores_before":{"contract_score":0,"backlog_visibility_score":8,"margin_bridge_score":0,"revision_score":0,"relative_strength_score":14,"customer_quality_score":11,"policy_or_regulatory_score":24,"valuation_repricing_score":8,"execution_risk_score":-3,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_before":72,"stage_label_before":"Stage2-Actionable","raw_component_scores_after":{"contract_score":0,"backlog_visibility_score":9,"margin_bridge_score":0,"revision_score":0,"relative_strength_score":14,"customer_quality_score":13,"policy_or_regulatory_score":25,"valuation_repricing_score":8,"execution_risk_score":-3,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0,"policy_capture_bridge_score":12},"weighted_score_after":78,"stage_label_after":"Stage2-Actionable-high","changed_components":["policy_capture_bridge_score","customer_quality_score"],"component_delta_explanation":"IRA subsidy bridge had direct US wind-manufacturing capture route; Stage2 lifted, Green still not automatic.","MFE_90D_pct":26.57,"MAE_90D_pct":-10.85,"score_return_alignment_label":"aligned_positive_after_bridge","current_profile_verdict":"current_profile_too_late"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"C31_052690_202203","trigger_id":"TR_R13L29_KEPCO_STAGE2_20220310","symbol":"052690","large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"C31_POLICY_SUBSIDY_LEGISLATION_EVENT","raw_component_scores_before":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":0,"revision_score":0,"relative_strength_score":20,"customer_quality_score":4,"policy_or_regulatory_score":26,"valuation_repricing_score":14,"execution_risk_score":-4,"legal_or_contract_risk_score":-2,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_before":74,"stage_label_before":"Stage2-Actionable-risk-of-Yellow","raw_component_scores_after":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":0,"revision_score":0,"relative_strength_score":12,"customer_quality_score":2,"policy_or_regulatory_score":20,"valuation_repricing_score":10,"execution_risk_score":-8,"legal_or_contract_risk_score":-4,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0,"policy_capture_bridge_score":-12},"weighted_score_after":61,"stage_label_after":"Watch-only","changed_components":["policy_capture_bridge_score","relative_strength_score","execution_risk_score"],"component_delta_explanation":"Policy headline lacked project-award/order bridge; proposed guard blocks false positive.","MFE_90D_pct":7.82,"MAE_90D_pct":-36.87,"score_return_alignment_label":"false_positive_blocked","current_profile_verdict":"current_profile_false_positive"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"C31_034020_202203","trigger_id":"TR_R13L29_DOOSANENER_STAGE2_20220310","symbol":"034020","large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"C31_POLICY_SUBSIDY_LEGISLATION_EVENT","raw_component_scores_before":{"contract_score":0,"backlog_visibility_score":2,"margin_bridge_score":0,"revision_score":0,"relative_strength_score":18,"customer_quality_score":5,"policy_or_regulatory_score":26,"valuation_repricing_score":13,"execution_risk_score":-5,"legal_or_contract_risk_score":-2,"dilution_cb_risk_score":-4,"accounting_trust_risk_score":0},"weighted_score_before":73,"stage_label_before":"Stage2-Actionable-risk-of-Yellow","raw_component_scores_after":{"contract_score":0,"backlog_visibility_score":1,"margin_bridge_score":0,"revision_score":0,"relative_strength_score":11,"customer_quality_score":2,"policy_or_regulatory_score":20,"valuation_repricing_score":9,"execution_risk_score":-11,"legal_or_contract_risk_score":-4,"dilution_cb_risk_score":-8,"accounting_trust_risk_score":0,"policy_capture_bridge_score":-12},"weighted_score_after":58,"stage_label_after":"Watch-only","changed_components":["policy_capture_bridge_score","execution_risk_score","dilution_cb_risk_score"],"component_delta_explanation":"Policy-only rerating plus balance-sheet/overhang risk produced high MAE; proposed guard blocks Green/Yellow promotion.","MFE_90D_pct":13.27,"MAE_90D_pct":-24.17,"score_return_alignment_label":"false_positive_blocked","current_profile_verdict":"current_profile_false_positive"}
```

### 25.5 residual_contribution rows

```jsonl
{"row_type":"residual_contribution","round":"R13","loop":"29","large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"C31_POLICY_SUBSIDY_LEGISLATION_EVENT","new_independent_case_count":4,"reused_case_count":0,"new_symbol_count":4,"new_trigger_family_count":4,"tested_existing_calibrated_axes":["stage2_actionable_evidence_bonus","stage3_yellow_total_min","stage3_green_total_min","stage3_green_revision_min","price_only_blowoff_blocks_positive_stage","full_4b_requires_non_price_evidence","hard_4c_thesis_break_routes_to_4c"],"residual_error_types_found":["policy_headline_false_positive","policy_to_order_bridge_missing","balance_sheet_overhang_after_policy_rerating","green_late_for_direct_subsidy_capture"],"loop_contribution_label":"canonical_archetype_rule_candidate","do_not_propose_new_weight_delta":false}
```

### 25.6 narrative_only rows

```jsonl
{"row_type":"narrative_only","case_id":"none","symbol":null,"large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"C31_POLICY_SUBSIDY_LEGISLATION_EVENT","reason":"all selected cases had usable 180D stock-web forward windows","price_source":"Songdaiki/stock-web","usage":"not_weight_calibration"}
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
next_round = R13_loop_30
suggested_large_sector_id = L6_FINANCIAL_CAPITAL_RETURN_DIGITAL
suggested_canonical_archetype_id = C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN
reason = after policy-event residual guard, test whether capital-return / ROE-PBR cases have sector-specific false positives and late Green triggers
```

## 28. Source Notes

Stock-web files checked:

```text
atlas/manifest.json
atlas/schema.json
diagnostics/chatgpt_bundle.txt
atlas/symbol_profiles/336/336260.json
atlas/symbol_profiles/112/112610.json
atlas/symbol_profiles/052/052690.json
atlas/symbol_profiles/034/034020.json
atlas/ohlcv_tradable_by_symbol_year/336/336260/2020.csv
atlas/ohlcv_tradable_by_symbol_year/336/336260/2021.csv
atlas/ohlcv_tradable_by_symbol_year/112/112610/2022.csv
atlas/ohlcv_tradable_by_symbol_year/112/112610/2023.csv
atlas/ohlcv_tradable_by_symbol_year/052/052690/2022.csv
atlas/ohlcv_tradable_by_symbol_year/034/034020/2022.csv
```

External narrative anchors searched for historical evidence context:

```text
- Inflation Reduction Act signed into law on 2022-08-16; clean-energy / climate provisions and renewable tax-credit context.
- Korea New Deal / Green New Deal and hydrogen policy context around July 2020.
- South Korea 2022 presidential election as nuclear-policy inflection point.
- Doosan FuelCell Daesan hydrogen fuel-cell project visibility around July 2020.
```

The external anchors are used only for event-timing narrative. Quantitative calibration uses stock-web OHLC rows only.
