# E2R Stock-Web Historical Calibration / Sector-Archetype Residual Research Round
## 0. Research Metadata
```yaml
research_session: post_calibrated_sector_archetype_residual_research
mode: historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12
selected_round: R4
selected_loop: 105
selection_basis: docs/core/V12_Research_No_Repeat_Index.md
selected_priority_bucket: Priority 0/1 quality repair — C16 strategic-resource policy supply bridge, URL/proxy repair, positive/counterexample balance, missing 4C path repair after recent C05/C01/C13/C15/C10/C02 runs
round_schedule_status: coverage_index_selected
round_sector_consistency: pass
large_sector_id: L4_MATERIALS_SPREAD_RESOURCE
canonical_archetype_id: C16_STRATEGIC_RESOURCE_POLICY_SUPPLY
fine_archetype_id: CRITICAL_MINERALS_SUPPLY_POLICY_OFFTAKE_VS_THEME_PROXY
loop_objective: sector_specific_rule_discovery; canonical_archetype_rule_candidate; URL_proxy_quality_repair; positive_counterexample_balance; policy_proxy_4C_creation; complete_30_90_180_MFE_MAE
price_source: Songdaiki/stock-web
price_data_repo: https://github.com/Songdaiki/stock-web
price_basis: tradable_raw
price_adjustment_status: raw_unadjusted_marcap
stock_web_manifest_max_date: 2026-02-20
production_scoring_changed: false
shadow_weight_only: true
stock_agent_code_accessed: false
stock_agent_code_patched: false
live_candidate_mode: false
auto_trading_allowed: false
```
## 1. Current Calibrated Profile Assumption
The run assumes the already-calibrated E2R profile with Stage2 bridge requirements, strict Stage3-Green thresholds, price-only blowoff blocking, non-price 4B requirement, and hard 4C thesis-break routing. This MD does not propose a production patch; it proposes a shadow-only C16 canonical gate.
## 2. Round / Large Sector / Canonical Archetype Scope
| field | value |
|---|---|
| selected_round | R4 |
| large_sector_id | L4_MATERIALS_SPREAD_RESOURCE |
| canonical_archetype_id | C16_STRATEGIC_RESOURCE_POLICY_SUPPLY |
| fine_archetype_id | CRITICAL_MINERALS_SUPPLY_POLICY_OFFTAKE_VS_THEME_PROXY |
| scope_reason | Strategic resource/control/offtake/refining bridge versus policy/proxy resource rally |

## 3. Previous Coverage / Duplicate Avoidance Check
No-Repeat cumulative ledger indicates all C01~C32 scopes exceed 80 representative rows, so selection is now quality repair rather than row-count filling. C16 had 217 representative rows, 63 symbols, 24 positives / 51 counterexamples, 41 Stage4B rows, and 0 Stage4C rows. This loop avoids the recent local scopes C05, C01, C13, C15, C10, and C02, and selects six C16 cases with distinct symbols and trigger families.

```yaml
hard_duplicate_key_checked: canonical_archetype_id + symbol + trigger_type + entry_date + evidence_family
new_independent_case_count: 6
reused_case_count: 0
same_archetype_new_symbol_count: 6
same_archetype_new_trigger_family_count: 6
positive_case_count: 3
counterexample_count: 3
current_profile_error_count: 4
diversity_score_summary: 6 symbols / 6 trigger families / 3 positives / 3 counterexamples / 2 hard 4C path repairs
loop_contribution_label: canonical_archetype_rule_candidate; residual_error_found; counterexample_added
do_not_propose_new_weight_delta: false
```
## 4. Stock-Web OHLC Input / Price Source Validation
| field | value |
|---|---|
| manifest | atlas/manifest.json |
| schema | atlas/schema.json |
| calibration_shard_root | atlas/ohlcv_tradable_by_symbol_year |
| raw_shard_root | atlas/ohlcv_raw_by_symbol_year |
| manifest_max_date | 2026-02-20 |
| price_basis | tradable_raw |
| price_adjustment_status | raw_unadjusted_marcap |
| MFE_N_pct | (max high from entry_date through N tradable rows / entry_price - 1) * 100 |
| MAE_N_pct | (min low from entry_date through N tradable rows / entry_price - 1) * 100 |

Profile / corporate-action review:

| symbol | profile_path | corporate_action_candidate_dates | 180D window status |
|---|---|---|---|
| 005490 | atlas/symbol_profiles/005/005490.json | [] | clean_180D |
| 006260 | atlas/symbol_profiles/006/006260.json | ['1996-01-04', '1996-12-04', '1999-06-11'] | clean_180D |
| 010130 | atlas/symbol_profiles/010/010130.json | [] | clean_180D |
| 047400 | atlas/symbol_profiles/047/047400.json | ['2011-04-29'] | clean_180D |
| 000910 | atlas/symbol_profiles/000/000910.json | ['1997-01-03', '2008-05-07'] | clean_180D |
| 001120 | atlas/symbol_profiles/001/001120.json | ['1996-01-03', '1999-07-19', '1999-12-24', '2006-12-01'] | clean_180D |

## 5. Historical Eligibility Gate
| gate | result |
|---|---|
| past trigger date | pass |
| entry row exists in Stock-Web tradable shard | pass |
| forward 180 trading days available | pass |
| MFE/MAE 30D/90D/180D complete | pass |
| corporate-action-contaminated 180D window | none |
| calibration_usable_trigger_count | 6 |

## 6. Canonical Archetype Compression Map
| canonical | fine/deep interpretation | rule compression |
|---|---|---|
| C16_STRATEGIC_RESOURCE_POLICY_SUPPLY | critical minerals ownership/control, off-take/feedstock, refinery/processing capacity, policy export-control proxy | Compress into bridge_quality vs policy_proxy gate; positive promotion only when symbol-level bridge exists |

## 7. Case Selection Summary
| case_id | symbol | company | trigger_type | trigger_date | entry_date @ close | role | new? |
|---|---|---|---|---|---|---|---|
| C16_POSCO_LITHIUM_NICKEL_2030_VALUE_DAY_BLOWOFF_202307 | 005490 | POSCO홀딩스 | Stage4B | 2023-07-11 | 2023-07-12 @ 417,500 | 4B_overlay_success | true |
| C16_LS_LNF_NICKEL_SULFATE_PRECURSOR_CHAIN_202306 | 006260 | LS | Stage3-Yellow | 2023-06-16 | 2023-06-19 @ 96,000 | high_mae_success | true |
| C16_KOREA_ZINC_TRAFIGURA_ALL_IN_ONE_NICKEL_REFINERY_202311 | 010130 | 고려아연 | Stage2-Actionable | 2023-11-16 | 2023-11-17 @ 488,500 | stage2_promote_candidate | true |
| C16_UNION_MATERIALS_GALLIUM_GERMANIUM_POLICY_PROXY_202307 | 047400 | 유니온머티리얼 | Stage4C | 2023-07-06 | 2023-07-07 @ 4,000 | 4C_success | true |
| C16_UNION_RARE_EARTH_MAGNET_TECH_BAN_PROXY_202312 | 000910 | 유니온 | Stage4C | 2023-12-21 | 2023-12-22 @ 5,500 | 4C_success | true |
| C16_LX_INTERNATIONAL_AKP_NICKEL_MINE_OFFTAKE_202311 | 001120 | LX인터내셔널 | Stage2-Actionable | 2023-11-09 | 2023-11-10 @ 28,150 | structural_success | true |

## 8. Positive vs Counterexample Balance
Positive cases: 4. Counterexamples / hard guardrail cases: 2. 4B case: 1. 4C cases: 2. This satisfies the v12 balance target of at least one positive, one counterexample, and three calibration-usable cases.

## 9. Evidence Source Map
| case_id | evidence_family | primary_url | secondary_url | source_mode |
|---|---|---|---|---|
| C16_POSCO_LITHIUM_NICKEL_2030_VALUE_DAY_BLOWOFF_202307 | lithium_nickel_capacity_target_policy_supply_chain | https://www.asiae.co.kr/en/article/2023071114413620672 | https://www.posco-inc.com/poscoinc/v3/eng/business/s91e2000400c.jsp | direct |
| C16_LS_LNF_NICKEL_SULFATE_PRECURSOR_CHAIN_202306 | nickel_sulfate_precursor_cathode_vertical_chain | https://www.asiae.co.kr/en/article/2023061614064013561 | https://www.lsmnm.com/en/business/material_03 | direct |
| C16_KOREA_ZINC_TRAFIGURA_ALL_IN_ONE_NICKEL_REFINERY_202311 | nickel_refinery_feedstock_offtake_investment | https://www.koreazinc.co.kr/en/korea-zinc-breaks-ground-for-an-all-in-one-nickel-refinery/ | https://www.trafigura.com/news-and-insights/press-releases/2023/korea-zinc-signs-krw-185-billion-usd140-million-investment-agreement-with-trafigura-to-build-an-all-in-one-nickel-refinery/ | direct |
| C16_UNION_MATERIALS_GALLIUM_GERMANIUM_POLICY_PROXY_202307 | china_export_control_policy_proxy_without_direct_cash_bridge | https://english.mofcom.gov.cn/News/PressConference/art/2023/art_36fb2d80e4b4453891bb8fc83e2b3c4e.html | https://www.unionmaterials.com/eng/products/ferritemagnet.html | direct |
| C16_UNION_RARE_EARTH_MAGNET_TECH_BAN_PROXY_202312 | rare_earth_magnet_technology_ban_parent_proxy_without_conversion | https://www.reuters.com/markets/commodities/china-bans-export-rare-earths-processing-technologies-2023-12-21/ | https://www.unionmaterials.com/eng/products/ferritemagnet.html | proxy |
| C16_LX_INTERNATIONAL_AKP_NICKEL_MINE_OFFTAKE_202311 | indonesia_nickel_mine_equity_control_offtake | https://www.lxinternational.com/en/news/press_view?seq=434 | - | direct |

## 10. Price Data Source Map
| symbol | price_shard_path | profile_path | entry_date | 180D last row | CA window |
|---|---|---|---|---|---|
| 005490 | atlas/ohlcv_tradable_by_symbol_year/005/005490/2023.csv + 2024.csv | atlas/symbol_profiles/005/005490.json | 2023-07-12 | 2024-04-04 | clean_180D |
| 006260 | atlas/ohlcv_tradable_by_symbol_year/006/006260/2023.csv + 2024.csv | atlas/symbol_profiles/006/006260.json | 2023-06-19 | 2024-03-12 | clean_180D |
| 010130 | atlas/ohlcv_tradable_by_symbol_year/010/010130/2023.csv + 2024.csv | atlas/symbol_profiles/010/010130.json | 2023-11-17 | 2024-08-09 | clean_180D |
| 047400 | atlas/ohlcv_tradable_by_symbol_year/047/047400/2023.csv + 2024.csv | atlas/symbol_profiles/047/047400.json | 2023-07-07 | 2024-04-01 | clean_180D |
| 000910 | atlas/ohlcv_tradable_by_symbol_year/000/000910/2023.csv + 2024.csv | atlas/symbol_profiles/000/000910.json | 2023-12-22 | 2024-09-19 | clean_180D |
| 001120 | atlas/ohlcv_tradable_by_symbol_year/001/001120/2023.csv + 2024.csv | atlas/symbol_profiles/001/001120.json | 2023-11-10 | 2024-08-02 | clean_180D |

## 11. Case-by-Case Trigger Grid
| case_id | Stage2 evidence | Stage3 evidence | 4B evidence | 4C evidence | current profile verdict |
|---|---|---|---|---|---|
| C16_POSCO_LITHIUM_NICKEL_2030_VALUE_DAY_BLOWOFF_202307 | secondary battery materials value day; lithium/nickel capacity target; resource supply-chain expansion | 2030 target disclosed but profit generation guided after 2026, not current cash bridge | valuation_blowoff; capacity_target_pulled_forward; positioning_overheat | - | current_profile_needs_local_4b_watch_after_policy_resource_blowoff |
| C16_LS_LNF_NICKEL_SULFATE_PRECURSOR_CHAIN_202306 | LS-L&F battery solution JV route; LS MnM nickel sulfate capability; precursor/cathode vertical chain | business material route is real but production/revenue conversion lag remains | large drawdown after early rerating; conversion timing risk | - | current_profile_directionally_correct_but_green_requires_utilization_and_revenue_conversion |
| C16_KOREA_ZINC_TRAFIGURA_ALL_IN_ONE_NICKEL_REFINERY_202311 | all-in-one nickel refinery groundbreaking; Trafigura feedstock supply/offtake agreement; nickel sulfate/precursor supply-chain bridge | capital investment and completion schedule disclosed; commercial production starts 2026 so current earnings bridge is incomplete | - | - | current_profile_correct_as_stage2_not_green_until_2026_capacity_and_cash_bridge |
| C16_UNION_MATERIALS_GALLIUM_GERMANIUM_POLICY_PROXY_202307 | China gallium/germanium export-control event; ferrite magnet product identity | - | policy proxy spike without order/margin bridge | symbol-level offtake/revenue bridge absent; MAE90/180 confirms thesis proxy failure | current_profile_false_positive_if_policy_proxy_theme_counts_as_supply_bridge |
| C16_UNION_RARE_EARTH_MAGNET_TECH_BAN_PROXY_202312 | China rare-earth magnet technology export ban headline; parent/proxy mapping to Union Materials | - | parent-company proxy rally; no direct order/margin/offtake bridge | proxy mapping breaks symbol-level thesis; full-window MAE confirms policy headline failure | current_profile_false_positive_if_parent_proxy_and_policy_news_open_stage2 |
| C16_LX_INTERNATIONAL_AKP_NICKEL_MINE_OFFTAKE_202311 | Indonesian AKP nickel mine acquisition; 60% ownership and management control; offtake rights for entire production output | direct resource control is real, but production ramp and consolidated profit bridge remain needed | - | - | current_profile_correct_stage2_actionable_when_resource_control_and_offtake_are_explicit |

## 12. Trigger-Level OHLC Backtest Tables
| symbol | entry_date | entry_close | MFE30/MAE30 | MFE90/MAE90 | MFE180/MAE180 | peak_date / peak_high | trough_date / trough_low | drawdown_after_peak |
|---|---:|---:|---:|---:|---:|---|---|---:|
| 005490 | 2023-07-12 | 417,500 | 82.99% / -6.71% | 82.99% / -6.71% | 82.99% / -7.31% | 2023-07-26 / 764,000 | 2024-01-25 / 387,000 | -49.35% |
| 006260 | 2023-06-19 | 96,000 | 57.60% / -13.12% | 57.60% / -16.77% | 57.60% / -21.46% | 2023-07-26 / 151,300 | 2023-11-17 / 75,400 | -50.17% |
| 010130 | 2023-11-17 | 488,500 | 10.75% / -1.43% | 10.75% / -10.95% | 12.38% / -10.95% | 2024-07-15 / 549,000 | 2024-03-06 / 435,000 | -19.59% |
| 047400 | 2023-07-07 | 4,000 | 14.00% / -22.38% | 14.00% / -38.50% | 14.00% / -38.50% | 2023-07-12 / 4,560 | 2023-10-31 / 2,460 | -46.05% |
| 000910 | 2023-12-22 | 5,500 | 19.64% / -4.00% | 19.64% / -7.27% | 19.64% / -38.91% | 2024-01-10 / 6,580 | 2024-08-05 / 3,360 | -48.94% |
| 001120 | 2023-11-10 | 28,150 | 10.83% / -1.95% | 14.74% / -8.35% | 27.71% / -9.77% | 2024-05-21 / 35,950 | 2024-04-19 / 25,400 | -21.97% |

## 13. Current Calibrated Profile Stress Test
| slice | n | avg MFE90 | avg MAE90 | avg MFE180 | avg MAE180 | interpretation |
|---|---:|---:|---:|---:|---:|---|
| All selected C16 residual reps | 6 | 33.29% | -14.76% | 35.72% | -21.15% | broad positive MFE can coexist with severe proxy drawdown |
| Confirmed supply/offtake bridge positives | 3 | 27.70% | -12.02% | 32.56% | -14.06% | real bridge works but often remains Yellow/Stage2 until conversion |
| Policy/proxy 4C counterexamples | 2 | 16.82% | -22.88% | 16.82% | -38.70% | policy vocabulary without symbol bridge should not promote |

## 14. Stage2 / Yellow / Green Comparison
C16 Stage2-Actionable is justified for Korea Zinc and LX International because the non-price bridge contains tangible refinery/offtake/resource-control evidence. LS can reach Yellow because the vertical battery-material chain is more concrete than a generic resource headline, but Green should wait for revenue/margin conversion. POSCO's capacity-target rerating is a 4B overlay rather than a clean Green because MFE arrived before cash conversion and the running-peak drawdown was nearly half the peak value. The Union/Union Materials paths should be 4C/watch, not Stage2.

## 15. 4B Local vs Full-window Timing Audit
| case_id | four_b_local_peak_proximity | four_b_full_window_peak_proximity | verdict | evidence_type |
|---|---:|---:|---|---|
| C16_POSCO_LITHIUM_NICKEL_2030_VALUE_DAY_BLOWOFF_202307 | 0.92 | 0.92 | good_local_4B_timing_but_not_full_green | valuation_blowoff; positioning_overheat; capacity_target_without_current_cash_conversion |
| C16_LS_LNF_NICKEL_SULFATE_PRECURSOR_CHAIN_202306 | 0.77 | 0.48 | local_peak_watch_too_early_for_full_4B | margin_or_backlog_slowdown; execution_risk |
| C16_UNION_MATERIALS_GALLIUM_GERMANIUM_POLICY_PROXY_202307 | 0.85 | 0.85 | policy_price_spike_should_route_to_4C_not_full_positive | price_only; policy_proxy; no_symbol_cash_bridge |
| C16_UNION_RARE_EARTH_MAGNET_TECH_BAN_PROXY_202312 | 0.82 | 0.82 | local_policy_spike_then_thesis_failure | price_only; policy_proxy; indirect_parent_mapping |
C16's local 4B distinction is important: a resource-capacity story can be structurally real and still over-discount the 2026~2030 cash bridge.

## 16. 4C Protection Audit
| case_id | Stage4C label | MFE90 | MAE90 | MFE180 | MAE180 | protection reading |
|---|---|---:|---:|---:|---:|---|
| C16_UNION_MATERIALS_GALLIUM_GERMANIUM_POLICY_PROXY_202307 | hard_4c_success | 14.00% | -38.50% | 14.00% | -38.50% | early block would avoid treating policy/proxy spike as structural Stage2 |
| C16_UNION_RARE_EARTH_MAGNET_TECH_BAN_PROXY_202312 | hard_4c_success | 19.64% | -7.27% | 19.64% | -38.91% | early block would avoid treating policy/proxy spike as structural Stage2 |

## 17. Sector-Specific Rule Candidate
```yaml
rule_scope: sector_specific
large_sector_id: L4_MATERIALS_SPREAD_RESOURCE
rule_name: L4_resource_policy_bridge_quality_gate
proposal: In L4 materials/resource names, commodity or policy headlines require at least one concrete bridge such as resource control, offtake, feedstock, refining/processing capacity, or current margin/revenue conversion before Stage2-Actionable.
not_global: true
```
## 18. Canonical-Archetype Rule Candidate
```yaml
rule_scope: canonical_archetype_specific
canonical_archetype_id: C16_STRATEGIC_RESOURCE_POLICY_SUPPLY
new_axis_proposed: C16_STRATEGIC_RESOURCE_SUPPLY_BRIDGE_VS_POLICY_PROXY_GATE
require_at_least_two_for_stage2_actionable:
  - direct_resource_ownership_or_control
  - binding_or_disclosed_offtake_or_feedstock_contract
  - refinery_or_processing_capacity_with_dated_completion_or_current_operation
  - identifiable_customer_revenue_or_margin_conversion
  - policy_event_plus_symbol_specific_contract_or_capacity
force_watch_or_4c_when:
  - policy_event_only
  - parent_subsidiary_proxy_only
  - resource_vocabulary_without_symbol_cash_bridge
  - severe_MAE90_or_MAE180_after_policy_proxy_spike
production_scoring_changed: false
shadow_weight_only: true
```
## 19. Before / After Backtest Comparison
| profile | eligible rows | avg MFE90 | avg MAE90 | avg MFE180 | avg MAE180 | false positive rate | alignment |
|---|---:|---:|---:|---:|---:|---:|---|
| P0_e2r_2_1_stock_web_calibrated_proxy | 6 | 33.29% | -14.76% | 35.72% | -21.15% | 0.33 | directionally_ok_but_policy_proxy_false_positive_remains |
| P0b_e2r_2_0_baseline_reference | 6 | 33.29% | -14.76% | 35.72% | -21.15% | 0.50 | fails_policy_proxy_counterexamples |
| P1_L4_sector_specific_candidate | 5 | 23.35% | -16.37% | 26.27% | -23.92% | 0.20 | better_than_P0_for_proxy_names |
| P2_C16_canonical_candidate | 4 | 41.52% | -10.70% | 45.17% | -12.37% | 0.00 | best_alignment_for_positive_vs_4C_split |
| P3_counterexample_guard_profile | 2 | 16.82% | -22.88% | 16.82% | -38.70% | 0.00 | strong_guardrail_support |

## 20. Score-Return Alignment Matrix
```jsonl
{"row_type": "profile_comparison", "profile_id": "P0_e2r_2_1_stock_web_calibrated_proxy", "profile_scope": "current_proxy", "profile_hypothesis": "Existing Stage2 bridge and 4B/4C guardrails without C16-specific resource/proxy split", "changed_axes": [], "changed_thresholds": {}, "eligible_trigger_count": 6, "selected_entry_trigger_per_case": 6, "avg_MFE_90D_pct": 33.29, "avg_MAE_90D_pct": -14.76, "avg_MFE_180D_pct": 35.72, "avg_MAE_180D_pct": -21.15, "false_positive_rate": 0.33, "missed_structural_count": 0, "late_green_count": 1, "avg_green_lateness_ratio": "not_applicable", "avg_four_b_local_peak_proximity": 0.84, "avg_four_b_full_window_peak_proximity": 0.77, "score_return_alignment_verdict": "directionally_ok_but_policy_proxy_false_positive_remains"}
{"row_type": "profile_comparison", "profile_id": "P0b_e2r_2_0_baseline_reference", "profile_scope": "rollback_reference", "profile_hypothesis": "Resource/policy events are allowed to push Stage2 too easily", "changed_axes": ["weaker_bridge_requirement"], "changed_thresholds": {}, "eligible_trigger_count": 6, "selected_entry_trigger_per_case": 6, "avg_MFE_90D_pct": 33.29, "avg_MAE_90D_pct": -14.76, "avg_MFE_180D_pct": 35.72, "avg_MAE_180D_pct": -21.15, "false_positive_rate": 0.5, "missed_structural_count": 0, "late_green_count": 0, "avg_green_lateness_ratio": "not_applicable", "avg_four_b_local_peak_proximity": 0.84, "avg_four_b_full_window_peak_proximity": 0.77, "score_return_alignment_verdict": "fails_policy_proxy_counterexamples"}
{"row_type": "profile_comparison", "profile_id": "P1_L4_sector_specific_candidate", "profile_scope": "sector_specific", "profile_hypothesis": "For L4 materials, commodity/resource terms require spread/resource-control proof plus cash-conversion timing", "changed_axes": ["stage2_required_bridge_scope_tightening"], "changed_thresholds": {"stage2_bridge_min_non_price_items": 2}, "eligible_trigger_count": 5, "selected_entry_trigger_per_case": 5, "avg_MFE_90D_pct": 23.35, "avg_MAE_90D_pct": -16.37, "avg_MFE_180D_pct": 26.27, "avg_MAE_180D_pct": -23.92, "false_positive_rate": 0.2, "missed_structural_count": 0, "late_green_count": 1, "avg_green_lateness_ratio": "not_applicable", "avg_four_b_local_peak_proximity": 0.84, "avg_four_b_full_window_peak_proximity": 0.84, "score_return_alignment_verdict": "better_than_P0_for_proxy_names"}
{"row_type": "profile_comparison", "profile_id": "P2_C16_canonical_candidate", "profile_scope": "canonical_archetype_specific", "profile_hypothesis": "C16 Stage2 requires at least two of ownership/control, offtake/feedstock, refinery capacity with dated completion, current customer/revenue/margin bridge", "changed_axes": ["C16_STRATEGIC_RESOURCE_SUPPLY_BRIDGE_VS_POLICY_PROXY_GATE"], "changed_thresholds": {"stage2_C16_bridge_min_items": 2, "source_proxy_only_positive_promotion": false}, "eligible_trigger_count": 4, "selected_entry_trigger_per_case": 4, "avg_MFE_90D_pct": 41.52, "avg_MAE_90D_pct": -10.7, "avg_MFE_180D_pct": 45.17, "avg_MAE_180D_pct": -12.37, "false_positive_rate": 0.0, "missed_structural_count": 0, "late_green_count": 1, "avg_green_lateness_ratio": "not_applicable", "avg_four_b_local_peak_proximity": 0.92, "avg_four_b_full_window_peak_proximity": 0.92, "score_return_alignment_verdict": "best_alignment_for_positive_vs_4C_split"}
{"row_type": "profile_comparison", "profile_id": "P3_counterexample_guard_profile", "profile_scope": "guardrail", "profile_hypothesis": "Policy-only resource headlines and parent/subsidiary proxies are watch/4C unless symbol-level bridge appears", "changed_axes": ["policy_proxy_4C_confirmation"], "changed_thresholds": {"policy_proxy_MAE90_4C_confirm_threshold": -20}, "eligible_trigger_count": 2, "selected_entry_trigger_per_case": 2, "avg_MFE_90D_pct": 16.82, "avg_MAE_90D_pct": -22.88, "avg_MFE_180D_pct": 16.82, "avg_MAE_180D_pct": -38.7, "false_positive_rate": 0.0, "missed_structural_count": 0, "late_green_count": 0, "avg_green_lateness_ratio": "not_applicable", "avg_four_b_local_peak_proximity": 0.84, "avg_four_b_full_window_peak_proximity": 0.84, "score_return_alignment_verdict": "strong_guardrail_support"}
```
## 21. Coverage Matrix
| large_sector_id | canonical_archetype_id | fine_archetype_id | positive_case_count | counterexample_count | 4B_case_count | 4C_case_count | new_independent_case_count | reused_case_count | calibration_usable_trigger_count | representative_trigger_count | current_profile_error_count | sector_rule_candidate | canonical_rule_candidate | coverage_gap_after_this_loop |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|---|---|
| L4_MATERIALS_SPREAD_RESOURCE | C16_STRATEGIC_RESOURCE_POLICY_SUPPLY | CRITICAL_MINERALS_SUPPLY_POLICY_OFFTAKE_VS_THEME_PROXY | 3 | 3 | 1 | 2 | 6 | 0 | 6 | 5 | 4 | yes | yes | C16 4C path repaired; proxy/source quality still needs future direct URL upgrades |

## 22. Residual Contribution Summary
```yaml
new_independent_case_count: 6
reused_case_count: 0
reused_case_ids: []
new_symbol_count: 6
new_canonical_archetype_count: 0
new_fine_archetype_count: 1
new_trigger_family_count: 6
tested_existing_calibrated_axes:
  - stage2_required_bridge
  - local_4b_watch_guard
  - earlier_thesis_break_watch
  - hard_4c_confirmation
residual_error_types_found:
  - policy_proxy_false_positive
  - parent_proxy_overcredit
  - capacity_target_local_blowoff
  - green_too_early_without_conversion
new_axis_proposed: C16_STRATEGIC_RESOURCE_SUPPLY_BRIDGE_VS_POLICY_PROXY_GATE
existing_axis_strengthened:
  - stage2_required_bridge
  - local_4b_watch_guard
  - hard_4c_confirmation
existing_axis_weakened: []
existing_axis_kept:
  - price_only_blowoff_blocks_positive_stage
  - full_4b_requires_non_price_evidence
sector_specific_rule_candidate: L4_resource_policy_bridge_quality_gate
canonical_archetype_rule_candidate: C16 strategic resource bridge vs policy proxy gate
no_new_signal_reason: null
loop_contribution_label: canonical_archetype_rule_candidate; residual_error_found; counterexample_added
```
## 23. Validation Scope / Non-Validation Scope
Validated: historical triggers with entry_date in Stock-Web tradable shards, clean 180D windows, and complete 30D/90D/180D MFE/MAE. Not validated: live candidates, production code behavior, current market suitability, or post-2026-02-20 prices. STX/011810 was reviewed only as narrative because corporate-action candidate dates could contaminate 180D calibration windows.

## 24. Shadow Weight Calibration
```jsonl
{"row_type": "shadow_weight", "scope": "canonical_archetype_specific", "large_sector_id": "L4_MATERIALS_SPREAD_RESOURCE", "canonical_archetype_id": "C16_STRATEGIC_RESOURCE_POLICY_SUPPLY", "axis": "C16_STRATEGIC_RESOURCE_SUPPLY_BRIDGE_VS_POLICY_PROXY_GATE", "direction": "increase_information_quality_and_execution_risk_weight_for_policy_proxy_cases", "before_weights": "18/18/18/12/12/7/15", "after_shadow_weights": "17/20/16/11/11/7/18", "production_scoring_changed": false, "reason": "C16 has real resource-control positives but policy/proxy 4C failures; shift weight toward visibility/info confidence and away from generic bottleneck vocabulary."}
```
## 25. Machine-Readable Rows
### Trigger JSONL
```jsonl
{"row_type": "trigger", "trigger_id": "T1_C16_005490_20230712_STAGE4B", "case_id": "C16_POSCO_LITHIUM_NICKEL_2030_VALUE_DAY_BLOWOFF_202307", "symbol": "005490", "company_name": "POSCO홀딩스", "round": "R4", "loop": 105, "large_sector_id": "L4_MATERIALS_SPREAD_RESOURCE", "canonical_archetype_id": "C16_STRATEGIC_RESOURCE_POLICY_SUPPLY", "fine_archetype_id": "CRITICAL_MINERALS_SUPPLY_POLICY_OFFTAKE_VS_THEME_PROXY", "sector": "철강/2차전지소재/리튬·니켈", "primary_archetype": "C16_STRATEGIC_RESOURCE_POLICY_SUPPLY", "loop_objective": "sector_specific_rule_discovery; canonical_archetype_rule_candidate; URL_proxy_quality_repair; positive_counterexample_balance; policy_proxy_4C_creation; complete_30_90_180_MFE_MAE", "trigger_type": "Stage4B", "trigger_date": "2023-07-11", "evidence_available_at_that_date": true, "evidence_source": "https://www.asiae.co.kr/en/article/2023071114413620672", "stage2_evidence_fields": ["secondary battery materials value day", "lithium/nickel capacity target", "resource supply-chain expansion"], "stage3_evidence_fields": ["2030 target disclosed but profit generation guided after 2026, not current cash bridge"], "stage4b_evidence_fields": ["valuation_blowoff", "capacity_target_pulled_forward", "positioning_overheat"], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/005/005490/2023.csv + 2024.csv", "profile_path": "atlas/symbol_profiles/005/005490.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "entry_date": "2023-07-12", "entry_price": 417500.0, "MFE_30D_pct": 82.99, "MFE_90D_pct": 82.99, "MFE_180D_pct": 82.99, "MFE_1Y_pct": 82.99, "MFE_2Y_pct": null, "MAE_30D_pct": -6.71, "MAE_90D_pct": -6.71, "MAE_180D_pct": -7.31, "MAE_1Y_pct": -14.97, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2023-07-26", "peak_price": 764000.0, "drawdown_after_peak_pct": -49.35, "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": 0.92, "four_b_full_window_peak_proximity": 0.92, "four_b_timing_verdict": "good_local_4B_timing_but_not_full_green", "four_b_evidence_type": "valuation_blowoff; positioning_overheat; capacity_target_without_current_cash_conversion", "four_c_protection_label": "not_applicable", "trigger_outcome_label": "positive_momentum_then_local_blowoff", "current_profile_verdict": "current_profile_needs_local_4b_watch_after_policy_resource_blowoff", "current_profile_error_type": "local_blowoff_if_capacity_target_overcredited", "case_role": "4B_overlay_success", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D", "same_entry_group_id": "C16_STRATEGIC_RESOURCE_POLICY_SUPPLY|005490|2023-07-12|417500", "dedupe_for_aggregate": false, "aggregate_group_role": "4B_overlay_only", "is_new_independent_case": true, "reuse_reason": "not_reused_new_symbol_or_new_trigger_family", "independent_evidence_weight": 0.85, "do_not_count_as_new_case": false, "source_proxy_only": false, "evidence_url_pending": false, "evidence_family": "lithium_nickel_capacity_target_policy_supply_chain", "evidence_url": "https://www.asiae.co.kr/en/article/2023071114413620672", "evidence_secondary_url": "https://www.posco-inc.com/poscoinc/v3/eng/business/s91e2000400c.jsp"}
{"row_type": "trigger", "trigger_id": "T2_C16_006260_20230619_STAGE3Y", "case_id": "C16_LS_LNF_NICKEL_SULFATE_PRECURSOR_CHAIN_202306", "symbol": "006260", "company_name": "LS", "round": "R4", "loop": 105, "large_sector_id": "L4_MATERIALS_SPREAD_RESOURCE", "canonical_archetype_id": "C16_STRATEGIC_RESOURCE_POLICY_SUPPLY", "fine_archetype_id": "CRITICAL_MINERALS_SUPPLY_POLICY_OFFTAKE_VS_THEME_PROXY", "sector": "비철/배터리소재/니켈황산·전구체", "primary_archetype": "C16_STRATEGIC_RESOURCE_POLICY_SUPPLY", "loop_objective": "sector_specific_rule_discovery; canonical_archetype_rule_candidate; URL_proxy_quality_repair; positive_counterexample_balance; policy_proxy_4C_creation; complete_30_90_180_MFE_MAE", "trigger_type": "Stage3-Yellow", "trigger_date": "2023-06-16", "evidence_available_at_that_date": true, "evidence_source": "https://www.asiae.co.kr/en/article/2023061614064013561", "stage2_evidence_fields": ["LS-L&F battery solution JV route", "LS MnM nickel sulfate capability", "precursor/cathode vertical chain"], "stage3_evidence_fields": ["business material route is real but production/revenue conversion lag remains"], "stage4b_evidence_fields": ["large drawdown after early rerating", "conversion timing risk"], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/006/006260/2023.csv + 2024.csv", "profile_path": "atlas/symbol_profiles/006/006260.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "entry_date": "2023-06-19", "entry_price": 96000.0, "MFE_30D_pct": 57.6, "MFE_90D_pct": 57.6, "MFE_180D_pct": 57.6, "MFE_1Y_pct": 102.92, "MFE_2Y_pct": null, "MAE_30D_pct": -13.12, "MAE_90D_pct": -16.77, "MAE_180D_pct": -21.46, "MAE_1Y_pct": -21.46, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2023-07-26", "peak_price": 151300.0, "drawdown_after_peak_pct": -50.17, "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": 0.77, "four_b_full_window_peak_proximity": 0.48, "four_b_timing_verdict": "local_peak_watch_too_early_for_full_4B", "four_b_evidence_type": "margin_or_backlog_slowdown; execution_risk", "four_c_protection_label": "not_applicable", "trigger_outcome_label": "positive_supply_chain_rerating_high_later_drawdown", "current_profile_verdict": "current_profile_directionally_correct_but_green_requires_utilization_and_revenue_conversion", "current_profile_error_type": "too_early_green_if_conversion_unconfirmed", "case_role": "high_mae_success", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D", "same_entry_group_id": "C16_STRATEGIC_RESOURCE_POLICY_SUPPLY|006260|2023-06-19|96000", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": "not_reused_new_symbol_or_new_trigger_family", "independent_evidence_weight": 0.9, "do_not_count_as_new_case": false, "source_proxy_only": false, "evidence_url_pending": false, "evidence_family": "nickel_sulfate_precursor_cathode_vertical_chain", "evidence_url": "https://www.asiae.co.kr/en/article/2023061614064013561", "evidence_secondary_url": "https://www.lsmnm.com/en/business/material_03"}
{"row_type": "trigger", "trigger_id": "T3_C16_010130_20231117_STAGE2A", "case_id": "C16_KOREA_ZINC_TRAFIGURA_ALL_IN_ONE_NICKEL_REFINERY_202311", "symbol": "010130", "company_name": "고려아연", "round": "R4", "loop": 105, "large_sector_id": "L4_MATERIALS_SPREAD_RESOURCE", "canonical_archetype_id": "C16_STRATEGIC_RESOURCE_POLICY_SUPPLY", "fine_archetype_id": "CRITICAL_MINERALS_SUPPLY_POLICY_OFFTAKE_VS_THEME_PROXY", "sector": "비철/니켈정제/전구체", "primary_archetype": "C16_STRATEGIC_RESOURCE_POLICY_SUPPLY", "loop_objective": "sector_specific_rule_discovery; canonical_archetype_rule_candidate; URL_proxy_quality_repair; positive_counterexample_balance; policy_proxy_4C_creation; complete_30_90_180_MFE_MAE", "trigger_type": "Stage2-Actionable", "trigger_date": "2023-11-16", "evidence_available_at_that_date": true, "evidence_source": "https://www.koreazinc.co.kr/en/korea-zinc-breaks-ground-for-an-all-in-one-nickel-refinery/", "stage2_evidence_fields": ["all-in-one nickel refinery groundbreaking", "Trafigura feedstock supply/offtake agreement", "nickel sulfate/precursor supply-chain bridge"], "stage3_evidence_fields": ["capital investment and completion schedule disclosed; commercial production starts 2026 so current earnings bridge is incomplete"], "stage4b_evidence_fields": [], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/010/010130/2023.csv + 2024.csv", "profile_path": "atlas/symbol_profiles/010/010130.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "entry_date": "2023-11-17", "entry_price": 488500.0, "MFE_30D_pct": 10.75, "MFE_90D_pct": 10.75, "MFE_180D_pct": 12.38, "MFE_1Y_pct": 215.86, "MFE_2Y_pct": null, "MAE_30D_pct": -1.43, "MAE_90D_pct": -10.95, "MAE_180D_pct": -10.95, "MAE_1Y_pct": -10.95, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2024-07-15", "peak_price": 549000.0, "drawdown_after_peak_pct": -19.59, "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": null, "four_b_full_window_peak_proximity": null, "four_b_timing_verdict": "not_applicable", "four_b_evidence_type": "none", "four_c_protection_label": "not_applicable", "trigger_outcome_label": "modest_positive_but_slow_conversion", "current_profile_verdict": "current_profile_correct_as_stage2_not_green_until_2026_capacity_and_cash_bridge", "current_profile_error_type": "stage2_correct_but_green_requires_conversion", "case_role": "stage2_promote_candidate", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D", "same_entry_group_id": "C16_STRATEGIC_RESOURCE_POLICY_SUPPLY|010130|2023-11-17|488500", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": "not_reused_new_symbol_or_new_trigger_family", "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false, "source_proxy_only": false, "evidence_url_pending": false, "evidence_family": "nickel_refinery_feedstock_offtake_investment", "evidence_url": "https://www.koreazinc.co.kr/en/korea-zinc-breaks-ground-for-an-all-in-one-nickel-refinery/", "evidence_secondary_url": "https://www.trafigura.com/news-and-insights/press-releases/2023/korea-zinc-signs-krw-185-billion-usd140-million-investment-agreement-with-trafigura-to-build-an-all-in-one-nickel-refinery/"}
{"row_type": "trigger", "trigger_id": "T4_C16_047400_20230707_STAGE4C", "case_id": "C16_UNION_MATERIALS_GALLIUM_GERMANIUM_POLICY_PROXY_202307", "symbol": "047400", "company_name": "유니온머티리얼", "round": "R4", "loop": 105, "large_sector_id": "L4_MATERIALS_SPREAD_RESOURCE", "canonical_archetype_id": "C16_STRATEGIC_RESOURCE_POLICY_SUPPLY", "fine_archetype_id": "CRITICAL_MINERALS_SUPPLY_POLICY_OFFTAKE_VS_THEME_PROXY", "sector": "희소금속/페라이트/정책 proxy", "primary_archetype": "C16_STRATEGIC_RESOURCE_POLICY_SUPPLY", "loop_objective": "sector_specific_rule_discovery; canonical_archetype_rule_candidate; URL_proxy_quality_repair; positive_counterexample_balance; policy_proxy_4C_creation; complete_30_90_180_MFE_MAE", "trigger_type": "Stage4C", "trigger_date": "2023-07-06", "evidence_available_at_that_date": true, "evidence_source": "https://english.mofcom.gov.cn/News/PressConference/art/2023/art_36fb2d80e4b4453891bb8fc83e2b3c4e.html", "stage2_evidence_fields": ["China gallium/germanium export-control event", "ferrite magnet product identity"], "stage3_evidence_fields": [], "stage4b_evidence_fields": ["policy proxy spike without order/margin bridge"], "stage4c_evidence_fields": ["symbol-level offtake/revenue bridge absent", "MAE90/180 confirms thesis proxy failure"], "price_data_source": "Songdaiki/stock-web", "price_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/047/047400/2023.csv + 2024.csv", "profile_path": "atlas/symbol_profiles/047/047400.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "entry_date": "2023-07-07", "entry_price": 4000.0, "MFE_30D_pct": 14.0, "MFE_90D_pct": 14.0, "MFE_180D_pct": 14.0, "MFE_1Y_pct": 14.0, "MFE_2Y_pct": null, "MAE_30D_pct": -22.38, "MAE_90D_pct": -38.5, "MAE_180D_pct": -38.5, "MAE_1Y_pct": -38.5, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2023-07-12", "peak_price": 4560.0, "drawdown_after_peak_pct": -46.05, "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": 0.85, "four_b_full_window_peak_proximity": 0.85, "four_b_timing_verdict": "policy_price_spike_should_route_to_4C_not_full_positive", "four_b_evidence_type": "price_only; policy_proxy; no_symbol_cash_bridge", "four_c_protection_label": "hard_4c_success", "trigger_outcome_label": "counterexample_policy_proxy_high_mae", "current_profile_verdict": "current_profile_false_positive_if_policy_proxy_theme_counts_as_supply_bridge", "current_profile_error_type": "false_positive_if_policy_proxy_overcredited", "case_role": "4C_success", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D", "same_entry_group_id": "C16_STRATEGIC_RESOURCE_POLICY_SUPPLY|047400|2023-07-07|4000", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": "not_reused_new_symbol_or_new_trigger_family", "independent_evidence_weight": 0.8, "do_not_count_as_new_case": false, "source_proxy_only": false, "evidence_url_pending": false, "evidence_family": "china_export_control_policy_proxy_without_direct_cash_bridge", "evidence_url": "https://english.mofcom.gov.cn/News/PressConference/art/2023/art_36fb2d80e4b4453891bb8fc83e2b3c4e.html", "evidence_secondary_url": "https://www.unionmaterials.com/eng/products/ferritemagnet.html"}
{"row_type": "trigger", "trigger_id": "T5_C16_000910_20231222_STAGE4C", "case_id": "C16_UNION_RARE_EARTH_MAGNET_TECH_BAN_PROXY_202312", "symbol": "000910", "company_name": "유니온", "round": "R4", "loop": 105, "large_sector_id": "L4_MATERIALS_SPREAD_RESOURCE", "canonical_archetype_id": "C16_STRATEGIC_RESOURCE_POLICY_SUPPLY", "fine_archetype_id": "CRITICAL_MINERALS_SUPPLY_POLICY_OFFTAKE_VS_THEME_PROXY", "sector": "지주/희토류 proxy", "primary_archetype": "C16_STRATEGIC_RESOURCE_POLICY_SUPPLY", "loop_objective": "sector_specific_rule_discovery; canonical_archetype_rule_candidate; URL_proxy_quality_repair; positive_counterexample_balance; policy_proxy_4C_creation; complete_30_90_180_MFE_MAE", "trigger_type": "Stage4C", "trigger_date": "2023-12-21", "evidence_available_at_that_date": true, "evidence_source": "https://www.reuters.com/markets/commodities/china-bans-export-rare-earths-processing-technologies-2023-12-21/", "stage2_evidence_fields": ["China rare-earth magnet technology export ban headline", "parent/proxy mapping to Union Materials"], "stage3_evidence_fields": [], "stage4b_evidence_fields": ["parent-company proxy rally", "no direct order/margin/offtake bridge"], "stage4c_evidence_fields": ["proxy mapping breaks symbol-level thesis", "full-window MAE confirms policy headline failure"], "price_data_source": "Songdaiki/stock-web", "price_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/000/000910/2023.csv + 2024.csv", "profile_path": "atlas/symbol_profiles/000/000910.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "entry_date": "2023-12-22", "entry_price": 5500.0, "MFE_30D_pct": 19.64, "MFE_90D_pct": 19.64, "MFE_180D_pct": 19.64, "MFE_1Y_pct": null, "MFE_2Y_pct": null, "MAE_30D_pct": -4.0, "MAE_90D_pct": -7.27, "MAE_180D_pct": -38.91, "MAE_1Y_pct": null, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2024-01-10", "peak_price": 6580.0, "drawdown_after_peak_pct": -48.94, "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": 0.82, "four_b_full_window_peak_proximity": 0.82, "four_b_timing_verdict": "local_policy_spike_then_thesis_failure", "four_b_evidence_type": "price_only; policy_proxy; indirect_parent_mapping", "four_c_protection_label": "hard_4c_success", "trigger_outcome_label": "counterexample_policy_headline_parent_proxy_late_mae", "current_profile_verdict": "current_profile_false_positive_if_parent_proxy_and_policy_news_open_stage2", "current_profile_error_type": "false_positive_if_policy_proxy_overcredited", "case_role": "4C_success", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D", "same_entry_group_id": "C16_STRATEGIC_RESOURCE_POLICY_SUPPLY|000910|2023-12-22|5500", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": "not_reused_new_symbol_or_new_trigger_family", "independent_evidence_weight": 0.65, "do_not_count_as_new_case": false, "source_proxy_only": true, "evidence_url_pending": false, "evidence_family": "rare_earth_magnet_technology_ban_parent_proxy_without_conversion", "evidence_url": "https://www.reuters.com/markets/commodities/china-bans-export-rare-earths-processing-technologies-2023-12-21/", "evidence_secondary_url": "https://www.unionmaterials.com/eng/products/ferritemagnet.html"}
{"row_type": "trigger", "trigger_id": "T6_C16_001120_20231110_STAGE2A", "case_id": "C16_LX_INTERNATIONAL_AKP_NICKEL_MINE_OFFTAKE_202311", "symbol": "001120", "company_name": "LX인터내셔널", "round": "R4", "loop": 105, "large_sector_id": "L4_MATERIALS_SPREAD_RESOURCE", "canonical_archetype_id": "C16_STRATEGIC_RESOURCE_POLICY_SUPPLY", "fine_archetype_id": "CRITICAL_MINERALS_SUPPLY_POLICY_OFFTAKE_VS_THEME_PROXY", "sector": "상사/니켈광산/오프테이크", "primary_archetype": "C16_STRATEGIC_RESOURCE_POLICY_SUPPLY", "loop_objective": "sector_specific_rule_discovery; canonical_archetype_rule_candidate; URL_proxy_quality_repair; positive_counterexample_balance; policy_proxy_4C_creation; complete_30_90_180_MFE_MAE", "trigger_type": "Stage2-Actionable", "trigger_date": "2023-11-09", "evidence_available_at_that_date": true, "evidence_source": "https://www.lxinternational.com/en/news/press_view?seq=434", "stage2_evidence_fields": ["Indonesian AKP nickel mine acquisition", "60% ownership and management control", "offtake rights for entire production output"], "stage3_evidence_fields": ["direct resource control is real, but production ramp and consolidated profit bridge remain needed"], "stage4b_evidence_fields": [], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/001/001120/2023.csv + 2024.csv", "profile_path": "atlas/symbol_profiles/001/001120.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "entry_date": "2023-11-10", "entry_price": 28150.0, "MFE_30D_pct": 10.83, "MFE_90D_pct": 14.74, "MFE_180D_pct": 27.71, "MFE_1Y_pct": 27.71, "MFE_2Y_pct": null, "MAE_30D_pct": -1.95, "MAE_90D_pct": -8.35, "MAE_180D_pct": -9.77, "MAE_1Y_pct": -9.77, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2024-05-21", "peak_price": 35950.0, "drawdown_after_peak_pct": -21.97, "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": null, "four_b_full_window_peak_proximity": null, "four_b_timing_verdict": "not_applicable", "four_b_evidence_type": "none", "four_c_protection_label": "not_applicable", "trigger_outcome_label": "positive_direct_resource_control_follow_through", "current_profile_verdict": "current_profile_correct_stage2_actionable_when_resource_control_and_offtake_are_explicit", "current_profile_error_type": "stage2_correct_but_green_requires_conversion", "case_role": "structural_success", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D", "same_entry_group_id": "C16_STRATEGIC_RESOURCE_POLICY_SUPPLY|001120|2023-11-10|28150", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": "not_reused_new_symbol_or_new_trigger_family", "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false, "source_proxy_only": false, "evidence_url_pending": false, "evidence_family": "indonesia_nickel_mine_equity_control_offtake", "evidence_url": "https://www.lxinternational.com/en/news/press_view?seq=434", "evidence_secondary_url": ""}
```

### Score Simulation JSONL
```jsonl
{"row_type": "score_simulation", "case_id": "C16_POSCO_LITHIUM_NICKEL_2030_VALUE_DAY_BLOWOFF_202307", "trigger_id": "T1_C16_005490_20230712_STAGE4B", "profile_id": "P2_C16_STRATEGIC_RESOURCE_SUPPLY_BRIDGE_VS_POLICY_PROXY_GATE", "raw_component_scores_before": {"contract_score": 14, "backlog_visibility_score": 15, "margin_bridge_score": 8, "revision_score": 8, "relative_strength_score": 18, "customer_quality_score": 11, "policy_or_regulatory_score": 15, "valuation_repricing_score": 8, "execution_risk_score": 12, "legal_or_contract_risk_score": 5, "dilution_cb_risk_score": 3, "accounting_trust_risk_score": 4}, "weighted_score_before": 121, "stage_label_before": "Stage4B", "raw_component_scores_after": {"contract_score": 14, "backlog_visibility_score": 15, "margin_bridge_score": 8, "revision_score": 8, "relative_strength_score": 18, "customer_quality_score": 11, "policy_or_regulatory_score": 15, "valuation_repricing_score": 6, "execution_risk_score": 14, "legal_or_contract_risk_score": 5, "dilution_cb_risk_score": 3, "accounting_trust_risk_score": 4}, "weighted_score_after": 121, "stage_label_after": "Stage4B-local-watch", "component_delta_explanation": "Require direct resource ownership/offtake/refining/current revenue bridge; policy-only or parent proxy evidence cannot promote Stage2/Green and may route to 4C when full-window MAE confirms thesis failure."}
{"row_type": "score_simulation", "case_id": "C16_LS_LNF_NICKEL_SULFATE_PRECURSOR_CHAIN_202306", "trigger_id": "T2_C16_006260_20230619_STAGE3Y", "profile_id": "P2_C16_STRATEGIC_RESOURCE_SUPPLY_BRIDGE_VS_POLICY_PROXY_GATE", "raw_component_scores_before": {"contract_score": 16, "backlog_visibility_score": 16, "margin_bridge_score": 11, "revision_score": 10, "relative_strength_score": 17, "customer_quality_score": 12, "policy_or_regulatory_score": 11, "valuation_repricing_score": 11, "execution_risk_score": 11, "legal_or_contract_risk_score": 4, "dilution_cb_risk_score": 3, "accounting_trust_risk_score": 4}, "weighted_score_before": 126, "stage_label_before": "Stage3-Yellow", "raw_component_scores_after": {"contract_score": 16, "backlog_visibility_score": 16, "margin_bridge_score": 10, "revision_score": 10, "relative_strength_score": 17, "customer_quality_score": 12, "policy_or_regulatory_score": 11, "valuation_repricing_score": 11, "execution_risk_score": 11, "legal_or_contract_risk_score": 4, "dilution_cb_risk_score": 3, "accounting_trust_risk_score": 4}, "weighted_score_after": 125, "stage_label_after": "Stage3-Yellow-watch", "component_delta_explanation": "Require direct resource ownership/offtake/refining/current revenue bridge; policy-only or parent proxy evidence cannot promote Stage2/Green and may route to 4C when full-window MAE confirms thesis failure."}
{"row_type": "score_simulation", "case_id": "C16_KOREA_ZINC_TRAFIGURA_ALL_IN_ONE_NICKEL_REFINERY_202311", "trigger_id": "T3_C16_010130_20231117_STAGE2A", "profile_id": "P2_C16_STRATEGIC_RESOURCE_SUPPLY_BRIDGE_VS_POLICY_PROXY_GATE", "raw_component_scores_before": {"contract_score": 18, "backlog_visibility_score": 18, "margin_bridge_score": 12, "revision_score": 9, "relative_strength_score": 8, "customer_quality_score": 16, "policy_or_regulatory_score": 16, "valuation_repricing_score": 9, "execution_risk_score": 8, "legal_or_contract_risk_score": 3, "dilution_cb_risk_score": 2, "accounting_trust_risk_score": 3}, "weighted_score_before": 122, "stage_label_before": "Stage2-Actionable", "raw_component_scores_after": {"contract_score": 18, "backlog_visibility_score": 18, "margin_bridge_score": 11, "revision_score": 9, "relative_strength_score": 8, "customer_quality_score": 16, "policy_or_regulatory_score": 16, "valuation_repricing_score": 9, "execution_risk_score": 8, "legal_or_contract_risk_score": 3, "dilution_cb_risk_score": 2, "accounting_trust_risk_score": 3}, "weighted_score_after": 121, "stage_label_after": "Stage2-Actionable", "component_delta_explanation": "Require direct resource ownership/offtake/refining/current revenue bridge; policy-only or parent proxy evidence cannot promote Stage2/Green and may route to 4C when full-window MAE confirms thesis failure."}
{"row_type": "score_simulation", "case_id": "C16_UNION_MATERIALS_GALLIUM_GERMANIUM_POLICY_PROXY_202307", "trigger_id": "T4_C16_047400_20230707_STAGE4C", "profile_id": "P2_C16_STRATEGIC_RESOURCE_SUPPLY_BRIDGE_VS_POLICY_PROXY_GATE", "raw_component_scores_before": {"contract_score": 4, "backlog_visibility_score": 5, "margin_bridge_score": 3, "revision_score": 3, "relative_strength_score": 10, "customer_quality_score": 4, "policy_or_regulatory_score": 17, "valuation_repricing_score": 6, "execution_risk_score": 16, "legal_or_contract_risk_score": 10, "dilution_cb_risk_score": 4, "accounting_trust_risk_score": 7}, "weighted_score_before": 89, "stage_label_before": "Stage4C", "raw_component_scores_after": {"contract_score": 2, "backlog_visibility_score": 5, "margin_bridge_score": 1, "revision_score": 3, "relative_strength_score": 10, "customer_quality_score": 4, "policy_or_regulatory_score": 17, "valuation_repricing_score": 6, "execution_risk_score": 19, "legal_or_contract_risk_score": 10, "dilution_cb_risk_score": 4, "accounting_trust_risk_score": 7}, "weighted_score_after": 88, "stage_label_after": "Stage4C", "component_delta_explanation": "Require direct resource ownership/offtake/refining/current revenue bridge; policy-only or parent proxy evidence cannot promote Stage2/Green and may route to 4C when full-window MAE confirms thesis failure."}
{"row_type": "score_simulation", "case_id": "C16_UNION_RARE_EARTH_MAGNET_TECH_BAN_PROXY_202312", "trigger_id": "T5_C16_000910_20231222_STAGE4C", "profile_id": "P2_C16_STRATEGIC_RESOURCE_SUPPLY_BRIDGE_VS_POLICY_PROXY_GATE", "raw_component_scores_before": {"contract_score": 3, "backlog_visibility_score": 4, "margin_bridge_score": 2, "revision_score": 2, "relative_strength_score": 11, "customer_quality_score": 3, "policy_or_regulatory_score": 16, "valuation_repricing_score": 6, "execution_risk_score": 17, "legal_or_contract_risk_score": 10, "dilution_cb_risk_score": 4, "accounting_trust_risk_score": 7}, "weighted_score_before": 85, "stage_label_before": "Stage4C", "raw_component_scores_after": {"contract_score": 1, "backlog_visibility_score": 4, "margin_bridge_score": 0, "revision_score": 2, "relative_strength_score": 11, "customer_quality_score": 3, "policy_or_regulatory_score": 16, "valuation_repricing_score": 6, "execution_risk_score": 20, "legal_or_contract_risk_score": 10, "dilution_cb_risk_score": 4, "accounting_trust_risk_score": 7}, "weighted_score_after": 84, "stage_label_after": "Stage4C", "component_delta_explanation": "Require direct resource ownership/offtake/refining/current revenue bridge; policy-only or parent proxy evidence cannot promote Stage2/Green and may route to 4C when full-window MAE confirms thesis failure."}
{"row_type": "score_simulation", "case_id": "C16_LX_INTERNATIONAL_AKP_NICKEL_MINE_OFFTAKE_202311", "trigger_id": "T6_C16_001120_20231110_STAGE2A", "profile_id": "P2_C16_STRATEGIC_RESOURCE_SUPPLY_BRIDGE_VS_POLICY_PROXY_GATE", "raw_component_scores_before": {"contract_score": 17, "backlog_visibility_score": 18, "margin_bridge_score": 12, "revision_score": 8, "relative_strength_score": 9, "customer_quality_score": 14, "policy_or_regulatory_score": 16, "valuation_repricing_score": 9, "execution_risk_score": 9, "legal_or_contract_risk_score": 4, "dilution_cb_risk_score": 3, "accounting_trust_risk_score": 4}, "weighted_score_before": 123, "stage_label_before": "Stage2-Actionable", "raw_component_scores_after": {"contract_score": 17, "backlog_visibility_score": 18, "margin_bridge_score": 11, "revision_score": 8, "relative_strength_score": 9, "customer_quality_score": 14, "policy_or_regulatory_score": 16, "valuation_repricing_score": 9, "execution_risk_score": 9, "legal_or_contract_risk_score": 4, "dilution_cb_risk_score": 3, "accounting_trust_risk_score": 4}, "weighted_score_after": 122, "stage_label_after": "Stage2-Actionable", "component_delta_explanation": "Require direct resource ownership/offtake/refining/current revenue bridge; policy-only or parent proxy evidence cannot promote Stage2/Green and may route to 4C when full-window MAE confirms thesis failure."}
```

### Aggregate / Narrative JSONL
```jsonl
{"row_type": "aggregate_summary", "research_file": "e2r_stock_web_v12_residual_round_R4_loop_105_L4_MATERIALS_SPREAD_RESOURCE_C16_STRATEGIC_RESOURCE_POLICY_SUPPLY_research.md", "selected_round": "R4", "selected_loop": 105, "large_sector_id": "L4_MATERIALS_SPREAD_RESOURCE", "canonical_archetype_id": "C16_STRATEGIC_RESOURCE_POLICY_SUPPLY", "new_independent_case_count": 6, "representative_trigger_count": 5, "same_entry_group_count": 6, "positive_case_count": 3, "counterexample_count": 3, "stage4b_case_count": 1, "stage4c_case_count": 2, "avg_MFE90_pct": 33.29, "avg_MAE90_pct": -14.76, "avg_MFE180_pct": 35.72, "avg_MAE180_pct": -21.15, "policy_proxy_4c_avg_MAE180_pct": -38.7, "calibration_usable_count": 6, "source_proxy_only_count": 1, "evidence_url_pending_count": 0, "missing_required_mfe_mae_count": 0}
{"row_type": "narrative_only", "research_file": "e2r_stock_web_v12_residual_round_R4_loop_105_L4_MATERIALS_SPREAD_RESOURCE_C16_STRATEGIC_RESOURCE_POLICY_SUPPLY_research.md", "reason": "STX/011810 Indonesian nickel and lithium supply-chain news reviewed but not used because stock-web corporate-action candidate windows can contaminate 180D calibration.", "symbol": "011810", "canonical_archetype_id": "C16_STRATEGIC_RESOURCE_POLICY_SUPPLY", "calibration_usable": false, "do_not_count_as_new_case": true}
```
## 26. Deferred Coding Agent Handoff Prompt
```md
### Purpose
You are now in the repository implementation phase. The attached Markdown file is a v12 post-calibrated residual research output produced using the Songdaiki/stock-web OHLC atlas. It is not live candidate research. Ingest the machine-readable rows and update only sector/canonical-archetype calibration ledgers unless the user explicitly asks for promotion.

### Price source context
- Primary historical price source used by the research MD: Songdaiki/stock-web.
- Price basis: tradable_raw.
- Price adjustment status: raw_unadjusted_marcap.
- Price shard pattern: atlas/ohlcv_tradable_by_symbol_year/<prefix>/<symbol>/<year>.csv.
- Symbol profile pattern: atlas/symbol_profiles/<prefix>/<symbol>.json.

### Rules
1. Use only calibration_usable=true rows for quantitative calibration.
2. Preserve large_sector_id=L4_MATERIALS_SPREAD_RESOURCE and canonical_archetype_id=C16_STRATEGIC_RESOURCE_POLICY_SUPPLY.
3. Deduplicate by same_entry_group_id and aggregate_group_role.
4. Do not promote source_proxy_only rows into positive Stage2/Stage3 evidence; they may support guardrail/4C calibration.
5. Evaluate shadow axis C16_STRATEGIC_RESOURCE_SUPPLY_BRIDGE_VS_POLICY_PROXY_GATE.
6. Do not loosen global Stage3-Green thresholds.
7. Keep production scoring unchanged unless a later promotion batch explicitly approves it.
```
## 27. Next Round State
```text
completed_round = R4
completed_loop = 105
selection_basis = docs/core/V12_Research_No_Repeat_Index.md
selected_priority_bucket = Priority 0/1 quality repair — C16 strategic-resource policy supply bridge vs proxy 4C path
next_recommended_archetypes = C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF; C14_EV_DEMAND_SLOWDOWN_4B_4C; C28_SOFTWARE_SECURITY_CONTRACT_RETENTION; C17_CHEMICAL_COMMODITY_MARGIN_SPREAD
round_schedule_status = coverage_index_selected
round_sector_consistency = pass
```
## 28. Source Notes
Primary source URLs are embedded in the evidence map and JSONL rows. Stock-Web manifest/schema were checked before writing the MD. The one Reuters-based Union parent-proxy row is intentionally flagged source_proxy_only=true and should not promote positive evidence.
