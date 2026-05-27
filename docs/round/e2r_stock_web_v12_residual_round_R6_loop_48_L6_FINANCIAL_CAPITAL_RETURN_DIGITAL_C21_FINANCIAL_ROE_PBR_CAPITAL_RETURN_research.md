# E2R Stock-Web Historical Calibration / Sector-Archetype Residual Research Round

## 0. Research Metadata

- research_session: post_calibrated_sector_archetype_residual_research
- mode: historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12
- round: R6
- loop: 48
- large_sector_id: L6_FINANCIAL_CAPITAL_RETURN_DIGITAL
- canonical_archetype_id: C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN
- fine_archetype_id: K_BANK_VALUEUP_CET1_CAPITAL_RETURN_BRIDGE
- output_file: `e2r_stock_web_v12_residual_round_R6_loop_48_L6_FINANCIAL_CAPITAL_RETURN_DIGITAL_C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN_research.md`
- production_scoring_changed: false
- shadow_weight_only: true
- current_stock_discovery_allowed: false
- stock_agent_code_access_allowed: false
- stock_agent_code_patch_allowed: false
- stock_web_price_atlas_access_required: true

This MD is historical calibration research only. It is not an investment recommendation, not a live scan, and not a production scoring patch.

## 1. Current Calibrated Profile Assumption

The assumed current profile is `e2r_2_1_stock_web_calibrated_proxy`. The old `e2r_2_0_baseline_reference` is used only as rollback/reference. Existing global axes are not re-proposed globally; this loop tests whether C21 needs a canonical-archetype-specific split between policy-only value-up sympathy and real capital-return bridge evidence.

## 2. Round / Large Sector / Canonical Archetype Scope

| Field | Value |
|---|---|
| round | R6 |
| loop | 48 |
| large_sector_id | L6_FINANCIAL_CAPITAL_RETURN_DIGITAL |
| canonical_archetype_id | C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN |
| fine_archetype_id | K_BANK_VALUEUP_CET1_CAPITAL_RETURN_BRIDGE |
| loop_objective | coverage_gap_fill; counterexample_mining; sector_specific_rule_discovery; canonical_archetype_compression; 4B_non_price_requirement_stress_test |

## 3. Previous Coverage / Duplicate Avoidance Check

Allowed `stock_agent` research-artifact search returned no direct `C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN` hits in the accessible search index, so this loop treats C21 bank/financial-holding capital-return coverage as a fresh gap. It deliberately avoids the immediately prior C22 insurance-rate-cycle work and does not re-use the C22 life-insurer rows.

Novelty accounting: new_independent_case_count=3, reused_case_count=0, new_symbol_count=3, same_archetype_new_symbol_count=3, new_trigger_family_count=5, counterexample_count=1.

## 4. Stock-Web OHLC Input / Price Source Validation

The stock-web manifest identifies FinanceData/marcap as the upstream source, raw/unadjusted OHLC, max_date 2026-02-20, tradable_row_count 14,354,401, raw_row_count 15,214,118, symbol_count 5,414, and calibration_shard_root `atlas/ohlcv_tradable_by_symbol_year`. fileciteturn961file0

| Manifest field | Value |
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
| markets | ['KONEX', 'KOSDAQ', 'KOSDAQ GLOBAL', 'KOSPI'] |
| calibration_shard_root | atlas/ohlcv_tradable_by_symbol_year |
| raw_shard_root | atlas/ohlcv_raw_by_symbol_year |
| schema_path | atlas/schema.json |
| universe_path | atlas/universe/all_symbols.csv |

## 5. Historical Eligibility Gate

| Symbol | Company | Profile status | Corporate action status | Calibration eligibility | Source |
|---|---|---|---|---|---|
| 105560 | KB금융 | active_like; available years include 2024-2026 | corporate_action_candidate_count=0 | clean 180D | fileciteturn966file0 |
| 086790 | 하나금융지주 | active_like; available years include 2024-2026 | corporate_action_candidate_count=0 | clean 180D | fileciteturn967file0 |
| 323410 | 카카오뱅크 | active_like; available years include 2024-2026 | corporate_action_candidate_count=0 | clean 180D | fileciteturn972file0 |

All representative rows have entry dates inside tradable stock-web shards and at least 180 forward trading days available by the manifest max date. 2Y/504D is not used for weight calibration because the 2024 entries do not all have full 504-trading-day windows before 2026-02-20.

## 6. Canonical Archetype Compression Map

| Fine archetype | Canonical archetype | Compression reason |
|---|---|---|
| K_BANK_VALUEUP_CET1_CAPITAL_RETURN_BRIDGE | C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN | Low-PBR financial rerating only works when policy option, ROE/CET1 visibility, and repeatable shareholder-return evidence close together. |
| DIGITAL_BANK_POLICY_ONLY_FALSE_POSITIVE | C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN | Digital-bank price sympathy is a counterexample when it lacks low-PBR/capital-return bridge and trades on a different valuation grammar. |

## 7. Case Selection Summary

| case_id | symbol | company | role | best_trigger | calibration_usable | current_profile_verdict |
|---|---:|---|---|---|---|---|
| R6L48_C21_KB_2024_CAPITAL_RETURN_BRIDGE | 105560 | KB금융 | positive | KB_STAGE3_CAPRETURN_2024_04_26 | True | current_profile_correct |
| R6L48_C21_HANA_2024_CAPITAL_RETURN_BRIDGE | 086790 | 하나금융지주 | positive | HANA_STAGE3_CAPRETURN_2024_04_26 | True | current_profile_correct |
| R6L48_C21_KAKAOBANK_2024_POLICY_ONLY_FALSE_POSITIVE | 323410 | 카카오뱅크 | counterexample | KAKAO_POLICY_ONLY_2024_02_26 | True | current_profile_false_positive |

## 8. Positive vs Counterexample Balance

- positive_case_count: 2
- counterexample_count: 1
- 4B_case_count: 2
- 4C_case_count: 1 watch/routing counterexample
- calibration_usable_case_count: 3

Positive rows show that KB/Hana policy sensitivity became more usable after explicit capital-return/financial confirmation windows. The KakaoBank row is the negative control: it had financial-sector sympathy around the same policy window, but not the C21 low-PBR capital-return bridge, and the price path failed sharply.

## 9. Evidence Source Map

The policy context comes from the Korea Corporate Value-up Programme coverage: the programme was announced in February 2024 to encourage shareholder returns and reduce the Korea discount, later supplemented by discussion of faster follow-up and possible penalties for firms failing to improve shareholder returns. citeturn582949news1turn582949news3turn582949news4

| evidence family | Used for | Limitation |
|---|---|---|
| Corporate Value-up policy | Stage2 policy optionality | Not enough for C21 Green by itself. |
| Post-correction capital-return / financial confirmation window | Stage3 bridge for KB/Hana | Exact IR link should be reattached in implementation batch; this loop validates price/trigger behavior. |
| High-valuation digital-bank sympathy | Counterexample / false positive | Same financial-sector event does not imply C21 low-PBR rerating. |
| Valuation/positioning full-window proximity | 4B overlay | Overlay only; not a hard 4C thesis break unless capital-return thesis breaks. |

## 10. Price Data Source Map

| symbol | tradable_shard | profile_path | checked rows |
|---:|---|---|---|
| 105560 | atlas/ohlcv_tradable_by_symbol_year/105/105560/2024.csv | atlas/symbol_profiles/105/105560.json | 2024-02-26, 2024-04-26, 2024-10-25, post-peak lows. fileciteturn964file0 fileciteturn965file0 |
| 086790 | atlas/ohlcv_tradable_by_symbol_year/086/086790/2024.csv | atlas/symbol_profiles/086/086790.json | 2024-02-26, 2024-04-26, 2024-08-26/27, post-peak lows. fileciteturn968file0 fileciteturn969file0 |
| 323410 | atlas/ohlcv_tradable_by_symbol_year/323/323410/2024.csv | atlas/symbol_profiles/323/323410.json | 2024-02-26 entry, June/July drawdown lows. fileciteturn973file0 |

## 11. Case-by-Case Trigger Grid

| trigger_id | symbol | trigger_type | trigger_date | entry_date | entry_price | stage2 | stage3 | 4B | 4C | representative | outcome |
|---|---:|---|---|---|---:|---|---|---|---|---|---|
| KB_STAGE2_POLICY_2024_02_26 | 105560 | Stage2-Actionable | 2024-02-26 | 2024-02-26 | 62500 | policy_or_regulatory_optionality,relative_strength,early_revision_signal |  |  |  | False | early_positive_but_not_green_quality |
| KB_STAGE3_CAPRETURN_2024_04_26 | 105560 | Stage3-Green | 2024-04-26 | 2024-04-26 | 76000 | policy_or_regulatory_optionality,relative_strength | confirmed_revision,financial_visibility,margin_bridge,low_red_team_risk |  |  | True | structural_success |
| KB_4B_VALUATION_2024_10_25 | 105560 | Stage4B | 2024-10-25 | 2024-10-25 | 101000 |  |  | valuation_blowoff,positioning_overheat |  | False | 4B_overlay_success |
| HANA_STAGE2_POLICY_2024_02_26 | 086790 | Stage2-Actionable | 2024-02-26 | 2024-02-26 | 55400 | policy_or_regulatory_optionality,relative_strength,early_revision_signal |  |  |  | False | moderate_positive_but_policy_only |
| HANA_STAGE3_CAPRETURN_2024_04_26 | 086790 | Stage3-Yellow | 2024-04-26 | 2024-04-26 | 60000 | policy_or_regulatory_optionality,relative_strength | confirmed_revision,financial_visibility,margin_bridge |  |  | True | structural_success_lower_convexity |
| HANA_4B_VALUATION_2024_08_26 | 086790 | Stage4B | 2024-08-26 | 2024-08-26 | 68800 |  |  | valuation_blowoff,positioning_overheat |  | False | 4B_overlay_success |
| KAKAO_POLICY_ONLY_2024_02_26 | 323410 | Stage2-Actionable | 2024-02-26 | 2024-02-26 | 30150 | policy_or_regulatory_optionality |  | price_only_local_peak | thesis_evidence_broken | True | failed_rerating_false_positive |

## 12. Trigger-Level OHLC Backtest Tables

| trigger_id | entry_price | MFE_30D | MAE_30D | MFE_90D | MAE_90D | MFE_180D | MAE_180D | peak_date | peak_price | drawdown_after_peak |
|---|---:|---:|---:|---:|---:|---:|---:|---|---:|---:|
| KB_STAGE2_POLICY_2024_02_26 | 62500 | 25.76 | -4.48 | 44.0 | -4.48 | 66.24 | -4.48 | 2024-10-25 | 103900 | -21.46 |
| KB_STAGE3_CAPRETURN_2024_04_26 | 76000 | 9.74 | -5.39 | 21.58 | -5.39 | 36.71 | -5.39 | 2024-10-25 | 103900 | -21.46 |
| KB_4B_VALUATION_2024_10_25 | 101000 | 2.87 | -12.57 | 2.87 | -19.21 | None | None | 2024-10-25 | 103900 | -21.46 |
| HANA_STAGE2_POLICY_2024_02_26 | 55400 | 17.69 | -4.69 | 22.38 | -6.86 | 25.09 | -6.86 | 2024-08-27 | 69300 | -18.47 |
| HANA_STAGE3_CAPRETURN_2024_04_26 | 60000 | 8.83 | -5.33 | 13.0 | -5.33 | 15.5 | -5.83 | 2024-08-27 | 69300 | -18.47 |
| HANA_4B_VALUATION_2024_08_26 | 68800 | 0.73 | -10.47 | 0.73 | -17.88 | None | None | 2024-08-27 | 69300 | -18.47 |
| KAKAO_POLICY_ONLY_2024_02_26 | 30150 | 1.0 | -17.74 | 1.0 | -33.5 | 1.0 | -33.77 | 2024-02-26 | 30450 | -34.42 |

## 13. Current Calibrated Profile Stress Test

The current calibrated profile is broadly correct for KB/Hana if it keeps policy-only rows at Stage2 and waits for the capital-return/financial bridge before Stage3. The residual error is KakaoBank: a naive financial-sector policy score can over-promote a high-valuation digital bank that lacks the C21 low-PBR/capital-return grammar.

| question | answer |
|---|---|
| Stage2 bonus too high? | Not for KB/Hana; too high for policy-only digital-bank sympathy unless capped by C21 bridge filters. |
| Yellow threshold 75 too high/low? | Kept. Hana belongs in Yellow/low-Green because MFE_180D is positive but convexity is modest. |
| Green 87 / revision 55 too high/low? | Kept for generic profile; C21 needs a bridge-specific buffer rather than global easing. |
| price-only blowoff guard? | Strengthened; KakaoBank and late KB/Hana peaks show price-only should not promote positive stage. |
| full 4B non-price requirement? | Kept; 4B rows are overlay after large rerating, not hard 4C. |
| hard 4C routing? | Kept; only route to 4C when capital-return/ROE/PBR thesis breaks, not merely after local peak. |

## 14. Stage2 / Yellow / Green Comparison

| case | Stage2 entry | Stage3 entry | peak_after_stage2 | green_lateness_ratio | interpretation |
|---|---:|---:|---:|---:|---|
| KB금융 | 62,500 | 76,000 | 103,900 | 0.326 | Green not fatally late; Stage2 captured broad move, Stage3 confirmed quality. |
| 하나금융지주 | 55,400 | 60,000 | 69,300 | 0.331 | Green/Yellow slightly late but acceptable; lower convexity argues against aggressive Green. |
| 카카오뱅크 | 30,150 | not applicable | 30,450 | not_applicable | No real Stage3; policy-only row should be blocked from C21 promotion. |

## 15. 4B Local vs Full-window Timing Audit

| trigger_id | four_b_local_peak_proximity | four_b_full_window_peak_proximity | verdict |
|---|---:|---:|---|
| KB_4B_VALUATION_2024_10_25 | 0.93 | 0.93 | good_full_window_4B_timing |
| HANA_4B_VALUATION_2024_08_26 | 0.964 | 0.964 | good_full_window_4B_timing |
| KAKAO_POLICY_ONLY_2024_02_26 | 0.0 | 0.0 | not full 4B; this is a failed positive-stage filter / 4C watch. |

## 16. 4C Protection Audit

KakaoBank is the only hard 4C-style protection candidate in this loop. If the C21 guard rejects policy-only/high-valuation digital bank rows, it prevents a -33% to -34% drawdown after the policy trigger. KB/Hana are not 4C thesis breaks; their late rows are 4B overlay/fatigue only.

## 17. Sector-Specific Rule Candidate

sector_specific_rule_candidate: true

For L6 financials, policy programmes can create broad beta, but bank/financial-holding rerating requires explicit capital-return execution. The sector-specific rule should cap policy-only rows at Stage2 unless ROE/PBR valuation gap, CET1/solvency buffer, and repeatable shareholder-return route are present.

## 18. Canonical-Archetype Rule Candidate

canonical_archetype_rule_candidate: true

Proposed C21 rule:

```text
if canonical_archetype_id == C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN:
    if policy_or_regulatory_score is high but capital_return_bridge_score is missing:
        cap positive label at Stage2-Actionable
    if low_pbr_gap + recurring capital_return + ROE/CET1 visibility are all present:
        allow Stage3-Yellow/Green based on score and MAE discipline
    if high-valuation digital-bank profile lacks low-PBR/capital-return bridge:
        block C21 promotion and route to counterexample/watch-only
```

## 19. Before / After Backtest Comparison

| profile_id | scope | selected_entries | avg_MFE_90D | avg_MAE_90D | avg_MFE_180D | avg_MAE_180D | false_positive_rate | verdict |
|---|---|---|---:|---:|---:|---:|---:|---|
| P0 e2r_2_1_stock_web_calibrated_proxy | global | KB/Hana Stage2 + Kakao policy allowed as Stage2 | 22.46 | -14.61 | 30.44 | -15.04 | 0.33 | good but leaves C21 policy-only false positive |
| P0b e2r_2_0_baseline_reference | global old | more price/RS-sensitive | 22.46 | -14.61 | 30.44 | -15.04 | 0.33 | worse interpretability; can overpromote Kakao |
| P1 sector_specific_candidate_profile | L6 | cap policy-only; prefer KB/Hana bridge entries | 17.29 | -5.36 | 26.10 | -5.61 | 0.00 | improved MAE and removes false positive |
| P2 canonical_archetype_candidate_profile | C21 | require capital-return bridge | 17.29 | -5.36 | 26.10 | -5.61 | 0.00 | best score-return alignment for C21 |
| P3 counterexample_guard_profile | C21 guard | rejects high-valuation digital-bank policy-only row | 17.29 | -5.36 | 26.10 | -5.61 | 0.00 | protects against -33% Kakao drawdown |

## 20. Score-Return Alignment Matrix

| trigger_id | weighted_score_before | stage_before | weighted_score_after | stage_after | MFE_90D | MAE_90D | alignment |
|---|---:|---|---:|---|---:|---:|---|
| KB_STAGE2_POLICY_2024_02_26 | 74 | Stage2-Actionable | 74 | Stage2-Actionable | 44.0 | -4.48 | early_policy_signal_not_final_green |
| KB_STAGE3_CAPRETURN_2024_04_26 | 86 | Stage3-Yellow | 90 | Stage3-Green | 21.58 | -5.39 | score_return_aligned_positive |
| KB_4B_VALUATION_2024_10_25 | 90 | Stage3-Green + watch | 82 | Stage4B overlay | 2.87 | -19.21 | overlay_aligns_with_drawdown_risk |
| HANA_STAGE2_POLICY_2024_02_26 | 74 | Stage2-Actionable | 74 | Stage2-Actionable | 22.38 | -6.86 | early_policy_signal_not_final_green |
| HANA_STAGE3_CAPRETURN_2024_04_26 | 79 | Stage3-Yellow | 83 | Stage3-Yellow | 13.0 | -5.33 | score_return_aligned_but_lower_convexity |
| HANA_4B_VALUATION_2024_08_26 | 90 | Stage3-Green + watch | 82 | Stage4B overlay | 0.73 | -17.88 | overlay_aligns_with_drawdown_risk |
| KAKAO_POLICY_ONLY_2024_02_26 | 74 | Stage2-Actionable | 51 | No positive stage / watch-only | 1.0 | -33.5 | false_positive_blocked_after_guard |

## 21. Coverage Matrix

| large_sector_id | canonical_archetype_id | fine_archetype_id | positive_case_count | counterexample_count | 4B_case_count | 4C_case_count | new_independent_case_count | reused_case_count | calibration_usable_trigger_count | representative_trigger_count | current_profile_error_count | sector_rule_candidate | canonical_rule_candidate | coverage_gap_after_this_loop |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|---|---|
| L6_FINANCIAL_CAPITAL_RETURN_DIGITAL | C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN | K_BANK_VALUEUP_CET1_CAPITAL_RETURN_BRIDGE | 2 | 1 | 2 | 1 watch | 3 | 0 | 7 | 3 | 1 | true | true | Need 2025 holdout and non-bank securities/capital-return cases. |

## 22. Residual Contribution Summary

new_independent_case_count: 3
reused_case_count: 0
reused_case_ids: []
new_symbol_count: 3
same_archetype_new_symbol_count: 3
same_archetype_new_trigger_family_count: 5
new_canonical_archetype_count: 0
new_fine_archetype_count: 2
new_trigger_family_count: 5
tested_existing_calibrated_axes: stage2_actionable_evidence_bonus; stage3_yellow_total_min; stage3_green_total_min; price_only_blowoff_blocks_positive_stage; full_4b_requires_non_price_evidence; hard_4c_thesis_break_routes_to_4c
residual_error_types_found: policy_only_valueup_false_positive; high_valuation_digital_bank_not_C21_low_PBR; Stage3_convexity_depends_on_capital_return_bridge_quality
new_axis_proposed: C21_policy_only_valueup_stage2_cap; C21_capital_return_bridge_green_buffer; C21_positioning_valuation_4B_overlay
existing_axis_strengthened: price_only_blowoff_blocks_positive_stage; full_4b_requires_non_price_evidence; hard_4c_thesis_break_routes_to_4c
existing_axis_weakened: none
existing_axis_kept: stage2_actionable_evidence_bonus; stage3_yellow_total_min; stage3_green_total_min; stage3_green_revision_min; stage3_cross_evidence_green_buffer
sector_specific_rule_candidate: true
canonical_archetype_rule_candidate: true
no_new_signal_reason: null
loop_contribution_label: canonical_archetype_rule_candidate
do_not_propose_new_weight_delta: false
auto_selected_coverage_gap: C21 bank/financial-holding capital-return rerating gap after C22 insurance loop
diversity_score_summary: high

## 23. Validation Scope / Non-Validation Scope

Validation scope: stock-web manifest, symbol profiles, 2024 tradable OHLC rows, trigger-level entry price, MFE/MAE, green lateness, 4B peak-proximity split, score-return alignment proxy, and machine-readable rows.

Non-validation scope: no live candidate discovery, no investment recommendation, no stock_agent source-code inspection, no production scoring patch, no brokerage/API integration, no price-route hunt, no current watchlist.

## 24. Shadow Weight Calibration

```csv
row_type,axis,scope,large_sector_id,canonical_archetype_id,baseline_value,tested_value,delta,reason,backtest_effect,trigger_ids,calibration_usable_count,new_independent_case_count,counterexample_count,confidence,proposal_type,notes
shadow_weight,C21_policy_only_valueup_stage2_cap,canonical_archetype_specific,L6_FINANCIAL_CAPITAL_RETURN_DIGITAL,C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN,0,1,+1,"Policy-only financial-sector sympathy must not promote Green without low-PBR and explicit capital-return bridge.","Blocks KAKAO false positive while keeping KB/Hana as Stage2 only until follow-through.",KB_STAGE2_POLICY_2024_02_26|HANA_STAGE2_POLICY_2024_02_26|KAKAO_POLICY_ONLY_2024_02_26,3,3,1,medium,canonical_shadow_only,"not production; post-calibrated residual"
shadow_weight,C21_capital_return_bridge_green_buffer,canonical_archetype_specific,L6_FINANCIAL_CAPITAL_RETURN_DIGITAL,C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN,0,1,+1,"Green requires repeatable capital-return evidence: CET1 buffer, buyback/cancellation/dividend policy, and ROE/PBR visibility.","Improves score-return alignment for KB/Hana and prevents policy-only promotion.",KB_STAGE3_CAPRETURN_2024_04_26|HANA_STAGE3_CAPRETURN_2024_04_26,2,2,0,medium,canonical_shadow_only,"not production; post-calibrated residual"
shadow_weight,C21_positioning_valuation_4B_overlay,canonical_archetype_specific,L6_FINANCIAL_CAPITAL_RETURN_DIGITAL,C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN,0,1,+1,"After large ROE/PBR rerating, local/full-window peak proximity plus valuation fatigue should create 4B overlay, not 4C.","KB/Hana 4B rows align with later drawdown while preserving positive thesis.",KB_4B_VALUATION_2024_10_25|HANA_4B_VALUATION_2024_08_26,2,2,0,medium,canonical_shadow_only,"not production; post-calibrated residual"
```

## 25. Machine-Readable Rows

### 25.1 price_source_validation
```jsonl
{"row_type": "price_source_validation", "source": "Songdaiki/stock-web", "source_url": "https://github.com/Songdaiki/stock-web", "manifest_path": "atlas/manifest.json", "schema_path": "atlas/schema.json", "universe_path": "atlas/universe/all_symbols.csv", "manifest_max_date": "2026-02-20", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "raw_shard_root": "atlas/ohlcv_raw_by_symbol_year", "validation_status": "usable_for_historical_calibration"}
```

### 25.2 case rows
```jsonl
{"row_type": "case", "case_id": "R6L48_C21_KB_2024_CAPITAL_RETURN_BRIDGE", "symbol": "105560", "company_name": "KB금융", "round": "R6", "loop": "48", "large_sector_id": "L6_FINANCIAL_CAPITAL_RETURN_DIGITAL", "canonical_archetype_id": "C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN", "fine_archetype_id": "K_BANK_VALUEUP_CET1_CAPITAL_RETURN_BRIDGE", "case_type": "structural_success", "positive_or_counterexample": "positive", "best_trigger": "KB_STAGE3_CAPRETURN_2024_04_26", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "strong_positive_after_capital_return_bridge; policy-only was early but not fatal", "current_profile_verdict": "current_profile_correct", "price_source": "Songdaiki/stock-web", "notes": "2024-02-26 policy row, 2024-04-26 Stage3 row, and 2024-10-25 4B row were checked in stock-web 2024 shards. fileciteturn964file0 fileciteturn965file0"}
{"row_type": "case", "case_id": "R6L48_C21_HANA_2024_CAPITAL_RETURN_BRIDGE", "symbol": "086790", "company_name": "하나금융지주", "round": "R6", "loop": "48", "large_sector_id": "L6_FINANCIAL_CAPITAL_RETURN_DIGITAL", "canonical_archetype_id": "C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN", "fine_archetype_id": "K_BANK_VALUEUP_CET1_CAPITAL_RETURN_BRIDGE", "case_type": "structural_success", "positive_or_counterexample": "positive", "best_trigger": "HANA_STAGE3_CAPRETURN_2024_04_26", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "positive_but_lower_convexity_than_KB; capital-return evidence improves signal quality", "current_profile_verdict": "current_profile_correct", "price_source": "Songdaiki/stock-web", "notes": "2024-02-26 policy row, 2024-04-26 Stage3 row, and 2024-08-26 4B row were checked in stock-web 2024 shards. fileciteturn968file0 fileciteturn969file0"}
{"row_type": "case", "case_id": "R6L48_C21_KAKAOBANK_2024_POLICY_ONLY_FALSE_POSITIVE", "symbol": "323410", "company_name": "카카오뱅크", "round": "R6", "loop": "48", "large_sector_id": "L6_FINANCIAL_CAPITAL_RETURN_DIGITAL", "canonical_archetype_id": "C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN", "fine_archetype_id": "K_BANK_VALUEUP_CET1_CAPITAL_RETURN_BRIDGE", "case_type": "false_positive_green", "positive_or_counterexample": "counterexample", "best_trigger": "KAKAO_POLICY_ONLY_2024_02_26", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "policy-only financial-sector sympathy failed without low-PBR/capital-return bridge", "current_profile_verdict": "current_profile_false_positive", "price_source": "Songdaiki/stock-web", "notes": "The 2024-02-26 entry and subsequent low window were checked in the stock-web 2024 shard. fileciteturn973file0"}
```

### 25.3 trigger rows
```jsonl
{"row_type": "trigger", "trigger_id": "KB_STAGE2_POLICY_2024_02_26", "case_id": "R6L48_C21_KB_2024_CAPITAL_RETURN_BRIDGE", "symbol": "105560", "company_name": "KB금융", "round": "R6", "loop": "48", "large_sector_id": "L6_FINANCIAL_CAPITAL_RETURN_DIGITAL", "canonical_archetype_id": "C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN", "fine_archetype_id": "K_BANK_VALUEUP_CET1_CAPITAL_RETURN_BRIDGE", "sector": "financials", "primary_archetype": "ROE/PBR capital return rerating", "loop_objective": "coverage_gap_fill;counterexample_mining;sector_specific_rule_discovery;4B_non_price_requirement_stress_test", "trigger_type": "Stage2-Actionable", "trigger_date": "2024-02-26", "evidence_available_at_that_date": "Korea Corporate Value-up policy day; large-bank low-PBR/capital-return optionality visible, but company-level repeat-return evidence not yet fully closed.", "evidence_source": "FSC/Korea Corporate Value-up public policy coverage; Reuters/FT policy context. citeturn582949news1turn582949news3turn582949news4", "stage2_evidence_fields": ["policy_or_regulatory_optionality", "relative_strength", "early_revision_signal"], "stage3_evidence_fields": [], "stage4b_evidence_fields": [], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/105/105560/2024.csv", "profile_path": "atlas/symbol_profiles/105/105560.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "entry_date": "2024-02-26", "entry_price": 62500, "MFE_30D_pct": 25.76, "MFE_90D_pct": 44.0, "MFE_180D_pct": 66.24, "MFE_1Y_pct": 66.24, "MFE_2Y_pct": null, "MAE_30D_pct": -4.48, "MAE_90D_pct": -4.48, "MAE_180D_pct": -4.48, "MAE_1Y_pct": -4.48, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2024-10-25", "peak_price": 103900, "drawdown_after_peak_pct": -21.46, "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": null, "four_b_full_window_peak_proximity": null, "four_b_timing_verdict": null, "four_b_evidence_type": [], "four_c_protection_label": "not_applicable", "trigger_outcome_label": "early_positive_but_not_green_quality", "current_profile_verdict": "current_profile_correct", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window", "same_entry_group_id": "KB_2024_POLICY_ENTRY", "dedupe_for_aggregate": false, "aggregate_group_role": "label_comparison_only", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false}
{"row_type": "trigger", "trigger_id": "KB_STAGE3_CAPRETURN_2024_04_26", "case_id": "R6L48_C21_KB_2024_CAPITAL_RETURN_BRIDGE", "symbol": "105560", "company_name": "KB금융", "round": "R6", "loop": "48", "large_sector_id": "L6_FINANCIAL_CAPITAL_RETURN_DIGITAL", "canonical_archetype_id": "C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN", "fine_archetype_id": "K_BANK_VALUEUP_CET1_CAPITAL_RETURN_BRIDGE", "sector": "financials", "primary_archetype": "ROE/PBR capital return rerating", "loop_objective": "coverage_gap_fill;counterexample_mining;sector_specific_rule_discovery;4B_non_price_requirement_stress_test", "trigger_type": "Stage3-Green", "trigger_date": "2024-04-26", "evidence_available_at_that_date": "Q1/return-confirmation window: price reaction occurred after the policy-theme run had corrected, so this is treated as a cleaner Stage3 bridge than the February policy trigger.", "evidence_source": "stock-web OHLC confirmation plus public value-up/capital-return framework; exact IR document should be re-linked in implementation batch.", "stage2_evidence_fields": ["policy_or_regulatory_optionality", "relative_strength"], "stage3_evidence_fields": ["confirmed_revision", "financial_visibility", "margin_bridge", "low_red_team_risk"], "stage4b_evidence_fields": [], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/105/105560/2024.csv", "profile_path": "atlas/symbol_profiles/105/105560.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "entry_date": "2024-04-26", "entry_price": 76000, "MFE_30D_pct": 9.74, "MFE_90D_pct": 21.58, "MFE_180D_pct": 36.71, "MFE_1Y_pct": 36.71, "MFE_2Y_pct": null, "MAE_30D_pct": -5.39, "MAE_90D_pct": -5.39, "MAE_180D_pct": -5.39, "MAE_1Y_pct": -5.39, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2024-10-25", "peak_price": 103900, "drawdown_after_peak_pct": -21.46, "green_lateness_ratio": 0.326, "four_b_local_peak_proximity": null, "four_b_full_window_peak_proximity": null, "four_b_timing_verdict": null, "four_b_evidence_type": [], "four_c_protection_label": "not_applicable", "trigger_outcome_label": "structural_success", "current_profile_verdict": "current_profile_correct", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window", "same_entry_group_id": "KB_2024_CAPRETURN_ENTRY", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false}
{"row_type": "trigger", "trigger_id": "KB_4B_VALUATION_2024_10_25", "case_id": "R6L48_C21_KB_2024_CAPITAL_RETURN_BRIDGE", "symbol": "105560", "company_name": "KB금융", "round": "R6", "loop": "48", "large_sector_id": "L6_FINANCIAL_CAPITAL_RETURN_DIGITAL", "canonical_archetype_id": "C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN", "fine_archetype_id": "K_BANK_VALUEUP_CET1_CAPITAL_RETURN_BRIDGE", "sector": "financials", "primary_archetype": "ROE/PBR capital return rerating", "loop_objective": "coverage_gap_fill;counterexample_mining;sector_specific_rule_discovery;4B_non_price_requirement_stress_test", "trigger_type": "Stage4B", "trigger_date": "2024-10-25", "evidence_available_at_that_date": "Near full-window high after strong rerating; used only as overlay, not positive-stage promotion.", "evidence_source": "stock-web OHLC local/full peak check. fileciteturn965file0", "stage2_evidence_fields": [], "stage3_evidence_fields": [], "stage4b_evidence_fields": ["valuation_blowoff", "positioning_overheat"], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/105/105560/2024.csv", "profile_path": "atlas/symbol_profiles/105/105560.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "entry_date": "2024-10-25", "entry_price": 101000, "MFE_30D_pct": 2.87, "MFE_90D_pct": 2.87, "MFE_180D_pct": null, "MFE_1Y_pct": null, "MFE_2Y_pct": null, "MAE_30D_pct": -12.57, "MAE_90D_pct": -19.21, "MAE_180D_pct": null, "MAE_1Y_pct": null, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2024-10-25", "peak_price": 103900, "drawdown_after_peak_pct": -21.46, "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": 0.93, "four_b_full_window_peak_proximity": 0.93, "four_b_timing_verdict": "good_full_window_4B_timing", "four_b_evidence_type": ["valuation_blowoff", "positioning_overheat"], "four_c_protection_label": "thesis_break_watch_only", "trigger_outcome_label": "4B_overlay_success", "current_profile_verdict": "current_profile_correct", "calibration_usable": true, "forward_window_trading_days": 90, "calibration_block_reasons": ["overlay_row_not_representative_for_positive_weight"], "corporate_action_window_status": "clean_180D_window", "same_entry_group_id": "KB_2024_4B_ENTRY", "dedupe_for_aggregate": false, "aggregate_group_role": "4B_overlay_only", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 0.5, "do_not_count_as_new_case": false}
{"row_type": "trigger", "trigger_id": "HANA_STAGE2_POLICY_2024_02_26", "case_id": "R6L48_C21_HANA_2024_CAPITAL_RETURN_BRIDGE", "symbol": "086790", "company_name": "하나금융지주", "round": "R6", "loop": "48", "large_sector_id": "L6_FINANCIAL_CAPITAL_RETURN_DIGITAL", "canonical_archetype_id": "C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN", "fine_archetype_id": "K_BANK_VALUEUP_CET1_CAPITAL_RETURN_BRIDGE", "sector": "financials", "primary_archetype": "ROE/PBR capital return rerating", "loop_objective": "coverage_gap_fill;counterexample_mining;sector_specific_rule_discovery;4B_non_price_requirement_stress_test", "trigger_type": "Stage2-Actionable", "trigger_date": "2024-02-26", "evidence_available_at_that_date": "Korea Corporate Value-up policy day; low-PBR bank rerating optionality existed, but this row alone does not prove durable capital-return quality.", "evidence_source": "FSC/Korea Corporate Value-up public policy coverage; Reuters/FT policy context. citeturn582949news1turn582949news3turn582949news4", "stage2_evidence_fields": ["policy_or_regulatory_optionality", "relative_strength", "early_revision_signal"], "stage3_evidence_fields": [], "stage4b_evidence_fields": [], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/086/086790/2024.csv", "profile_path": "atlas/symbol_profiles/086/086790.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "entry_date": "2024-02-26", "entry_price": 55400, "MFE_30D_pct": 17.69, "MFE_90D_pct": 22.38, "MFE_180D_pct": 25.09, "MFE_1Y_pct": 25.09, "MFE_2Y_pct": null, "MAE_30D_pct": -4.69, "MAE_90D_pct": -6.86, "MAE_180D_pct": -6.86, "MAE_1Y_pct": -6.86, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2024-08-27", "peak_price": 69300, "drawdown_after_peak_pct": -18.47, "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": null, "four_b_full_window_peak_proximity": null, "four_b_timing_verdict": null, "four_b_evidence_type": [], "four_c_protection_label": "not_applicable", "trigger_outcome_label": "moderate_positive_but_policy_only", "current_profile_verdict": "current_profile_correct", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window", "same_entry_group_id": "HANA_2024_POLICY_ENTRY", "dedupe_for_aggregate": false, "aggregate_group_role": "label_comparison_only", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false}
{"row_type": "trigger", "trigger_id": "HANA_STAGE3_CAPRETURN_2024_04_26", "case_id": "R6L48_C21_HANA_2024_CAPITAL_RETURN_BRIDGE", "symbol": "086790", "company_name": "하나금융지주", "round": "R6", "loop": "48", "large_sector_id": "L6_FINANCIAL_CAPITAL_RETURN_DIGITAL", "canonical_archetype_id": "C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN", "fine_archetype_id": "K_BANK_VALUEUP_CET1_CAPITAL_RETURN_BRIDGE", "sector": "financials", "primary_archetype": "ROE/PBR capital return rerating", "loop_objective": "coverage_gap_fill;counterexample_mining;sector_specific_rule_discovery;4B_non_price_requirement_stress_test", "trigger_type": "Stage3-Yellow", "trigger_date": "2024-04-26", "evidence_available_at_that_date": "Post-correction financial/capital-return confirmation window; positive, but less convex than KB and therefore kept Yellow/low-Green instead of unconditional Green.", "evidence_source": "stock-web OHLC confirmation plus public value-up/capital-return framework; exact IR document should be re-linked in implementation batch.", "stage2_evidence_fields": ["policy_or_regulatory_optionality", "relative_strength"], "stage3_evidence_fields": ["confirmed_revision", "financial_visibility", "margin_bridge"], "stage4b_evidence_fields": [], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/086/086790/2024.csv", "profile_path": "atlas/symbol_profiles/086/086790.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "entry_date": "2024-04-26", "entry_price": 60000, "MFE_30D_pct": 8.83, "MFE_90D_pct": 13.0, "MFE_180D_pct": 15.5, "MFE_1Y_pct": 15.5, "MFE_2Y_pct": null, "MAE_30D_pct": -5.33, "MAE_90D_pct": -5.33, "MAE_180D_pct": -5.83, "MAE_1Y_pct": -5.83, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2024-08-27", "peak_price": 69300, "drawdown_after_peak_pct": -18.47, "green_lateness_ratio": 0.331, "four_b_local_peak_proximity": null, "four_b_full_window_peak_proximity": null, "four_b_timing_verdict": null, "four_b_evidence_type": [], "four_c_protection_label": "not_applicable", "trigger_outcome_label": "structural_success_lower_convexity", "current_profile_verdict": "current_profile_correct", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window", "same_entry_group_id": "HANA_2024_CAPRETURN_ENTRY", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false}
{"row_type": "trigger", "trigger_id": "HANA_4B_VALUATION_2024_08_26", "case_id": "R6L48_C21_HANA_2024_CAPITAL_RETURN_BRIDGE", "symbol": "086790", "company_name": "하나금융지주", "round": "R6", "loop": "48", "large_sector_id": "L6_FINANCIAL_CAPITAL_RETURN_DIGITAL", "canonical_archetype_id": "C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN", "fine_archetype_id": "K_BANK_VALUEUP_CET1_CAPITAL_RETURN_BRIDGE", "sector": "financials", "primary_archetype": "ROE/PBR capital return rerating", "loop_objective": "coverage_gap_fill;counterexample_mining;sector_specific_rule_discovery;4B_non_price_requirement_stress_test", "trigger_type": "Stage4B", "trigger_date": "2024-08-26", "evidence_available_at_that_date": "Full-window peak proximity was high before a drawdown to 56,500; use as valuation/positioning 4B overlay.", "evidence_source": "stock-web OHLC local/full peak check. fileciteturn969file0", "stage2_evidence_fields": [], "stage3_evidence_fields": [], "stage4b_evidence_fields": ["valuation_blowoff", "positioning_overheat"], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/086/086790/2024.csv", "profile_path": "atlas/symbol_profiles/086/086790.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "entry_date": "2024-08-26", "entry_price": 68800, "MFE_30D_pct": 0.73, "MFE_90D_pct": 0.73, "MFE_180D_pct": null, "MFE_1Y_pct": null, "MFE_2Y_pct": null, "MAE_30D_pct": -10.47, "MAE_90D_pct": -17.88, "MAE_180D_pct": null, "MAE_1Y_pct": null, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2024-08-27", "peak_price": 69300, "drawdown_after_peak_pct": -18.47, "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": 0.964, "four_b_full_window_peak_proximity": 0.964, "four_b_timing_verdict": "good_full_window_4B_timing", "four_b_evidence_type": ["valuation_blowoff", "positioning_overheat"], "four_c_protection_label": "thesis_break_watch_only", "trigger_outcome_label": "4B_overlay_success", "current_profile_verdict": "current_profile_correct", "calibration_usable": true, "forward_window_trading_days": 90, "calibration_block_reasons": ["overlay_row_not_representative_for_positive_weight"], "corporate_action_window_status": "clean_180D_window", "same_entry_group_id": "HANA_2024_4B_ENTRY", "dedupe_for_aggregate": false, "aggregate_group_role": "4B_overlay_only", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 0.5, "do_not_count_as_new_case": false}
{"row_type": "trigger", "trigger_id": "KAKAO_POLICY_ONLY_2024_02_26", "case_id": "R6L48_C21_KAKAOBANK_2024_POLICY_ONLY_FALSE_POSITIVE", "symbol": "323410", "company_name": "카카오뱅크", "round": "R6", "loop": "48", "large_sector_id": "L6_FINANCIAL_CAPITAL_RETURN_DIGITAL", "canonical_archetype_id": "C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN", "fine_archetype_id": "K_BANK_VALUEUP_CET1_CAPITAL_RETURN_BRIDGE", "sector": "financials", "primary_archetype": "ROE/PBR capital return rerating", "loop_objective": "coverage_gap_fill;counterexample_mining;sector_specific_rule_discovery;4B_non_price_requirement_stress_test", "trigger_type": "Stage2-Actionable", "trigger_date": "2024-02-26", "evidence_available_at_that_date": "Financial-sector policy sympathy without low-PBR/capital-return bridge; high-valuation digital bank profile did not fit C21 value-up rerating mechanics.", "evidence_source": "Korea Corporate Value-up policy context plus stock-web OHLC counterexample. citeturn582949news1turn582949news4 fileciteturn973file0", "stage2_evidence_fields": ["policy_or_regulatory_optionality"], "stage3_evidence_fields": [], "stage4b_evidence_fields": ["price_only_local_peak"], "stage4c_evidence_fields": ["thesis_evidence_broken"], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/323/323410/2024.csv", "profile_path": "atlas/symbol_profiles/323/323410.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "entry_date": "2024-02-26", "entry_price": 30150, "MFE_30D_pct": 1.0, "MFE_90D_pct": 1.0, "MFE_180D_pct": 1.0, "MFE_1Y_pct": null, "MFE_2Y_pct": null, "MAE_30D_pct": -17.74, "MAE_90D_pct": -33.5, "MAE_180D_pct": -33.77, "MAE_1Y_pct": null, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2024-02-26", "peak_price": 30450, "drawdown_after_peak_pct": -34.42, "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": 0.0, "four_b_full_window_peak_proximity": 0.0, "four_b_timing_verdict": "policy_only_not_full_4B_until_break", "four_b_evidence_type": ["price_only"], "four_c_protection_label": "hard_4c_success_if_routed_after_low_pbr_filter_failure", "trigger_outcome_label": "failed_rerating_false_positive", "current_profile_verdict": "current_profile_false_positive", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window", "same_entry_group_id": "KAKAO_2024_POLICY_ENTRY", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false}
```

### 25.4 score_simulation rows
```jsonl
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R6L48_C21_KB_2024_CAPITAL_RETURN_BRIDGE", "trigger_id": "KB_STAGE2_POLICY_2024_02_26", "symbol": "105560", "large_sector_id": "L6_FINANCIAL_CAPITAL_RETURN_DIGITAL", "canonical_archetype_id": "C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN", "raw_component_scores_before": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 0, "revision_score": 0, "relative_strength_score": 8, "customer_quality_score": 0, "policy_or_regulatory_score": 12, "valuation_repricing_score": 8, "execution_risk_score": -1, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_before": 74, "stage_label_before": "Stage2-Actionable", "raw_component_scores_after": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 0, "revision_score": 0, "relative_strength_score": 8, "customer_quality_score": 0, "policy_or_regulatory_score": 12, "valuation_repricing_score": 8, "execution_risk_score": -1, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_after": 74, "stage_label_after": "Stage2-Actionable", "changed_components": [], "component_delta_explanation": "C21 shadow profile separates policy-only value-up optionality from repeatable CET1/ROE/PBR capital-return bridge; price-only or high-valuation digital-bank sympathy is capped.", "MFE_90D_pct": 44.0, "MAE_90D_pct": -4.48, "score_return_alignment_label": "early_policy_signal_not_final_green", "current_profile_verdict": "current_profile_correct"}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R6L48_C21_KB_2024_CAPITAL_RETURN_BRIDGE", "trigger_id": "KB_STAGE3_CAPRETURN_2024_04_26", "symbol": "105560", "large_sector_id": "L6_FINANCIAL_CAPITAL_RETURN_DIGITAL", "canonical_archetype_id": "C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN", "raw_component_scores_before": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 13, "revision_score": 15, "relative_strength_score": 13, "customer_quality_score": 0, "policy_or_regulatory_score": 12, "valuation_repricing_score": 13, "execution_risk_score": -2, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_before": 86, "stage_label_before": "Stage3-Yellow", "raw_component_scores_after": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 15, "revision_score": 16, "relative_strength_score": 13, "customer_quality_score": 0, "policy_or_regulatory_score": 12, "valuation_repricing_score": 15, "execution_risk_score": -1, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_after": 90, "stage_label_after": "Stage3-Green", "changed_components": ["valuation_repricing_score", "margin_bridge_score", "execution_risk_score"], "component_delta_explanation": "C21 shadow profile separates policy-only value-up optionality from repeatable CET1/ROE/PBR capital-return bridge; price-only or high-valuation digital-bank sympathy is capped.", "MFE_90D_pct": 21.58, "MAE_90D_pct": -5.39, "score_return_alignment_label": "score_return_aligned_positive", "current_profile_verdict": "current_profile_correct"}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R6L48_C21_KB_2024_CAPITAL_RETURN_BRIDGE", "trigger_id": "KB_4B_VALUATION_2024_10_25", "symbol": "105560", "large_sector_id": "L6_FINANCIAL_CAPITAL_RETURN_DIGITAL", "canonical_archetype_id": "C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN", "raw_component_scores_before": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 0, "revision_score": 0, "relative_strength_score": 14, "customer_quality_score": 0, "policy_or_regulatory_score": 8, "valuation_repricing_score": 18, "execution_risk_score": -2, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_before": 90, "stage_label_before": "Stage3-Green + watch", "raw_component_scores_after": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 0, "revision_score": 0, "relative_strength_score": 14, "customer_quality_score": 0, "policy_or_regulatory_score": 8, "valuation_repricing_score": 18, "execution_risk_score": -8, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_after": 82, "stage_label_after": "Stage4B overlay", "changed_components": ["execution_risk_score"], "component_delta_explanation": "C21 shadow profile separates policy-only value-up optionality from repeatable CET1/ROE/PBR capital-return bridge; price-only or high-valuation digital-bank sympathy is capped.", "MFE_90D_pct": 2.87, "MAE_90D_pct": -19.21, "score_return_alignment_label": "overlay_aligns_with_drawdown_risk", "current_profile_verdict": "current_profile_correct"}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R6L48_C21_HANA_2024_CAPITAL_RETURN_BRIDGE", "trigger_id": "HANA_STAGE2_POLICY_2024_02_26", "symbol": "086790", "large_sector_id": "L6_FINANCIAL_CAPITAL_RETURN_DIGITAL", "canonical_archetype_id": "C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN", "raw_component_scores_before": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 0, "revision_score": 0, "relative_strength_score": 8, "customer_quality_score": 0, "policy_or_regulatory_score": 12, "valuation_repricing_score": 8, "execution_risk_score": -1, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_before": 74, "stage_label_before": "Stage2-Actionable", "raw_component_scores_after": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 0, "revision_score": 0, "relative_strength_score": 8, "customer_quality_score": 0, "policy_or_regulatory_score": 12, "valuation_repricing_score": 8, "execution_risk_score": -1, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_after": 74, "stage_label_after": "Stage2-Actionable", "changed_components": [], "component_delta_explanation": "C21 shadow profile separates policy-only value-up optionality from repeatable CET1/ROE/PBR capital-return bridge; price-only or high-valuation digital-bank sympathy is capped.", "MFE_90D_pct": 22.38, "MAE_90D_pct": -6.86, "score_return_alignment_label": "early_policy_signal_not_final_green", "current_profile_verdict": "current_profile_correct"}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R6L48_C21_HANA_2024_CAPITAL_RETURN_BRIDGE", "trigger_id": "HANA_STAGE3_CAPRETURN_2024_04_26", "symbol": "086790", "large_sector_id": "L6_FINANCIAL_CAPITAL_RETURN_DIGITAL", "canonical_archetype_id": "C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN", "raw_component_scores_before": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 12, "revision_score": 13, "relative_strength_score": 10, "customer_quality_score": 0, "policy_or_regulatory_score": 12, "valuation_repricing_score": 11, "execution_risk_score": -2, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_before": 79, "stage_label_before": "Stage3-Yellow", "raw_component_scores_after": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 13, "revision_score": 14, "relative_strength_score": 10, "customer_quality_score": 0, "policy_or_regulatory_score": 12, "valuation_repricing_score": 12, "execution_risk_score": -2, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_after": 83, "stage_label_after": "Stage3-Yellow", "changed_components": ["margin_bridge_score", "revision_score", "valuation_repricing_score"], "component_delta_explanation": "C21 shadow profile separates policy-only value-up optionality from repeatable CET1/ROE/PBR capital-return bridge; price-only or high-valuation digital-bank sympathy is capped.", "MFE_90D_pct": 13.0, "MAE_90D_pct": -5.33, "score_return_alignment_label": "score_return_aligned_but_lower_convexity", "current_profile_verdict": "current_profile_correct"}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R6L48_C21_HANA_2024_CAPITAL_RETURN_BRIDGE", "trigger_id": "HANA_4B_VALUATION_2024_08_26", "symbol": "086790", "large_sector_id": "L6_FINANCIAL_CAPITAL_RETURN_DIGITAL", "canonical_archetype_id": "C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN", "raw_component_scores_before": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 0, "revision_score": 0, "relative_strength_score": 14, "customer_quality_score": 0, "policy_or_regulatory_score": 8, "valuation_repricing_score": 18, "execution_risk_score": -2, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_before": 90, "stage_label_before": "Stage3-Green + watch", "raw_component_scores_after": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 0, "revision_score": 0, "relative_strength_score": 14, "customer_quality_score": 0, "policy_or_regulatory_score": 8, "valuation_repricing_score": 18, "execution_risk_score": -8, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_after": 82, "stage_label_after": "Stage4B overlay", "changed_components": ["execution_risk_score"], "component_delta_explanation": "C21 shadow profile separates policy-only value-up optionality from repeatable CET1/ROE/PBR capital-return bridge; price-only or high-valuation digital-bank sympathy is capped.", "MFE_90D_pct": 0.73, "MAE_90D_pct": -17.88, "score_return_alignment_label": "overlay_aligns_with_drawdown_risk", "current_profile_verdict": "current_profile_correct"}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R6L48_C21_KAKAOBANK_2024_POLICY_ONLY_FALSE_POSITIVE", "trigger_id": "KAKAO_POLICY_ONLY_2024_02_26", "symbol": "323410", "large_sector_id": "L6_FINANCIAL_CAPITAL_RETURN_DIGITAL", "canonical_archetype_id": "C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN", "raw_component_scores_before": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 0, "revision_score": 0, "relative_strength_score": 4, "customer_quality_score": 0, "policy_or_regulatory_score": 12, "valuation_repricing_score": 7, "execution_risk_score": -3, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_before": 74, "stage_label_before": "Stage2-Actionable", "raw_component_scores_after": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 0, "revision_score": 0, "relative_strength_score": 1, "customer_quality_score": 0, "policy_or_regulatory_score": 3, "valuation_repricing_score": 0, "execution_risk_score": -9, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_after": 51, "stage_label_after": "No positive stage / watch-only", "changed_components": ["policy_or_regulatory_score", "valuation_repricing_score", "execution_risk_score"], "component_delta_explanation": "C21 shadow profile separates policy-only value-up optionality from repeatable CET1/ROE/PBR capital-return bridge; price-only or high-valuation digital-bank sympathy is capped.", "MFE_90D_pct": 1.0, "MAE_90D_pct": -33.5, "score_return_alignment_label": "false_positive_blocked_after_guard", "current_profile_verdict": "current_profile_false_positive"}
```

### 25.5 shadow_weight rows
```csv
row_type,axis,scope,large_sector_id,canonical_archetype_id,baseline_value,tested_value,delta,reason,backtest_effect,trigger_ids,calibration_usable_count,new_independent_case_count,counterexample_count,confidence,proposal_type,notes
shadow_weight,C21_policy_only_valueup_stage2_cap,canonical_archetype_specific,L6_FINANCIAL_CAPITAL_RETURN_DIGITAL,C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN,0,1,+1,"Policy-only financial-sector sympathy must not promote Green without low-PBR and explicit capital-return bridge.","Blocks KAKAO false positive while keeping KB/Hana as Stage2 only until follow-through.",KB_STAGE2_POLICY_2024_02_26|HANA_STAGE2_POLICY_2024_02_26|KAKAO_POLICY_ONLY_2024_02_26,3,3,1,medium,canonical_shadow_only,"not production; post-calibrated residual"
shadow_weight,C21_capital_return_bridge_green_buffer,canonical_archetype_specific,L6_FINANCIAL_CAPITAL_RETURN_DIGITAL,C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN,0,1,+1,"Green requires repeatable capital-return evidence: CET1 buffer, buyback/cancellation/dividend policy, and ROE/PBR visibility.","Improves score-return alignment for KB/Hana and prevents policy-only promotion.",KB_STAGE3_CAPRETURN_2024_04_26|HANA_STAGE3_CAPRETURN_2024_04_26,2,2,0,medium,canonical_shadow_only,"not production; post-calibrated residual"
shadow_weight,C21_positioning_valuation_4B_overlay,canonical_archetype_specific,L6_FINANCIAL_CAPITAL_RETURN_DIGITAL,C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN,0,1,+1,"After large ROE/PBR rerating, local/full-window peak proximity plus valuation fatigue should create 4B overlay, not 4C.","KB/Hana 4B rows align with later drawdown while preserving positive thesis.",KB_4B_VALUATION_2024_10_25|HANA_4B_VALUATION_2024_08_26,2,2,0,medium,canonical_shadow_only,"not production; post-calibrated residual"
```

### 25.6 residual_contribution row
```jsonl
{"row_type": "residual_contribution", "round": "R6", "loop": "48", "large_sector_id": "L6_FINANCIAL_CAPITAL_RETURN_DIGITAL", "canonical_archetype_id": "C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN", "new_independent_case_count": 3, "reused_case_count": 0, "new_symbol_count": 3, "same_archetype_new_symbol_count": 3, "same_archetype_new_trigger_family_count": 5, "new_canonical_archetype_count": 0, "new_trigger_family_count": 5, "positive_case_count": 2, "counterexample_count": 1, "current_profile_error_count": 1, "tested_existing_calibrated_axes": ["stage2_actionable_evidence_bonus", "stage3_green_revision_min", "price_only_blowoff_blocks_positive_stage", "full_4b_requires_non_price_evidence", "hard_4c_thesis_break_routes_to_4c"], "residual_error_types_found": ["policy_only_valueup_false_positive", "high_valuation_digital_bank_not_C21_low_PBR", "Stage3_convexity_depends_on_capital_return_bridge_quality"], "loop_contribution_label": "canonical_archetype_rule_candidate", "do_not_propose_new_weight_delta": false, "diversity_score_summary": "high: three new symbols, new C21-specific trigger families, and one clean false-positive counterexample"}
```

### 25.7 narrative_only rows
```jsonl
{"row_type": "narrative_only", "case_id": "NONE", "symbol": null, "large_sector_id": "L6_FINANCIAL_CAPITAL_RETURN_DIGITAL", "canonical_archetype_id": "C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN", "reason": "No narrative-only rows required; all selected representative cases have clean 180D stock-web forward windows.", "price_source": "Songdaiki/stock-web", "usage": "not_weight_calibration"}
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

Recommended next round: R6 / C21 holdout validation on 2025 bank-financial holding rows and non-bank securities/capital-return cases. Priority: verify whether the C21 capital-return bridge rule still holds after the 2024 value-up beta fades, and add at least one non-bank counterexample.

## 28. Source Notes

- Stock-web manifest and symbol profiles are treated as source of truth for price availability and corporate-action contamination. fileciteturn961file0 fileciteturn966file0 fileciteturn967file0 fileciteturn972file0
- OHLC rows are from stock-web tradable shards, not adjusted-price data. KB rows: fileciteturn964file0 fileciteturn965file0; Hana rows: fileciteturn968file0 fileciteturn969file0; KakaoBank rows: fileciteturn973file0.
- Public policy context is based on contemporary coverage of the Korean Corporate Value-up Programme and subsequent regulator comments. citeturn582949news1turn582949news3turn582949news4
- This file intentionally leaves exact company IR hyperlink reattachment to the later implementation batch; the quantitative calibration rows here use stock-web OHLC and conservative proxy evidence labels only.
