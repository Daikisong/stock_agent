# E2R Stock-Web Historical Calibration / Sector-Archetype Residual Research Round

## 0. Research Metadata

```text
research_session = post_calibrated_sector_archetype_residual_research
mode = historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12
round = R8
loop = 31
large_sector_id = L8_PLATFORM_CONTENT_SW_SECURITY
canonical_archetype_id = C27_CONTENT_IP_GLOBAL_MONETIZATION
fine_archetype_id = GAME_IP_GLOBAL_LIVE_SERVICE_MONETIZATION; WEBTOON_TO_GAME_IP_LAUNCH_WITH_WEAK_RETENTION; P2E_TOKENIZED_GAME_IP_THESIS_BREAK
output_file = e2r_stock_web_v12_residual_round_R8_loop_31_L8_PLATFORM_CONTENT_SW_SECURITY_C27_CONTENT_IP_GLOBAL_MONETIZATION_research.md
production_scoring_changed = false
shadow_weight_only = true
stock_agent_code_access_allowed = false
stock_agent_code_patch_allowed = false
current_stock_discovery_allowed = false
auto_trading_allowed = false
brokerage_api_allowed = false
```

This file is historical calibration research only. It is not a live candidate scan, not an investment recommendation, and not a production patch.

## 1. Current Calibrated Profile Assumption

Current assumed profile: `e2r_2_1_stock_web_calibrated_proxy`.
Rollback/reference profile: `e2r_2_0_baseline_reference`.

Applied global axes are treated as already active: Stage2 actionable bonus, Yellow 75, Green 87, Green revision 55, cross-evidence Green buffer, price-only blowoff guard, 4B non-price requirement, and hard 4C thesis-break routing.

This loop does not re-prove those axes globally. It tests a C27-specific residual: game/IP monetization works when live-service or repeat monetization is visible, but launch-only IP spikes and tokenized/P2E narratives can be false positives unless routed to 4B/4C.

## 2. Round / Large Sector / Canonical Archetype Scope

| Field | Value |
|---|---|
| round | R8 |
| loop | 31 |
| large_sector_id | L8_PLATFORM_CONTENT_SW_SECURITY |
| canonical_archetype_id | C27_CONTENT_IP_GLOBAL_MONETIZATION |
| fine_archetype_id | GAME_IP_GLOBAL_LIVE_SERVICE_MONETIZATION; WEBTOON_TO_GAME_IP_LAUNCH_WITH_WEAK_RETENTION; P2E_TOKENIZED_GAME_IP_THESIS_BREAK |
| loop_objective | coverage_gap_fill|counterexample_mining|4B_non_price_requirement_stress_test|4C_thesis_break_timing_test|canonical_archetype_compression|green_strictness_stress_test |

## 3. Previous Coverage / Duplicate Avoidance Check

Allowed research artifacts were used only for coverage and duplicate avoidance. Previous local/generated R8 C27 coverage contained K-pop global album/tour, multi-label portfolio IP, and K-drama OTT narrative cases. The remaining gap was non-K-pop game IP, launch-retention failure, and hard 4C/tokenized-IP path.

Diversity decision:

```text
same_canonical_archetype_research = allowed
same_archetype_new_symbol_count = 3
same_archetype_new_trigger_family_count = 3
reused_case_count = 0
new_independent_case_ratio = 1.00
auto_selected_coverage_gap = non-K-pop game IP / launch-retention counterexample / tokenized-P2E 4C path
```

## 4. Stock-Web OHLC Input / Price Source Validation

| Field | Value |
|---|---|
| source | Songdaiki/stock-web |
| source_name | FinanceData/marcap |
| price_basis | tradable_raw |
| price_adjustment_status | raw_unadjusted_marcap |
| manifest_max_date | 2026-02-20 |
| calibration_shard_root | atlas/ohlcv_tradable_by_symbol_year |
| raw_shard_root | atlas/ohlcv_raw_by_symbol_year |
| schema_path | atlas/schema.json |
| universe_path | atlas/universe/all_symbols.csv |

Manifest and schema basis are from the Stock-Web atlas: manifest max_date is 2026-02-20, the calibration root is `atlas/ohlcv_tradable_by_symbol_year`, and the schema defines tradable OHLC columns `d,o,h,l,c,v,a,mc,s,m`. Corporate-action contaminated windows are blocked by default.

## 5. Historical Eligibility Gate

| case_id | symbol | profile_path | first_date / last_date | corporate action status | calibration_usable |
|---|---:|---|---|---|---|
| R8L31_C27_259960_KRAFTON_GLOBAL_LIVE_SERVICE_POS | 259960 | atlas/symbol_profiles/259/259960.json | 2021-08-10 / 2026-02-20 | no corporate-action candidates | True |
| R8L31_C27_251270_NETMARBLE_IP_LAUNCH_HIGH_MAE_COUNTER | 251270 | atlas/symbol_profiles/251/251270.json | 2017-05-12 / 2026-02-20 | no corporate-action candidates | True |
| R8L31_C27_112040_WEMADE_P2E_TOKENIZED_IP_4C_COUNTER | 112040 | atlas/symbol_profiles/112/112040.json | 2009-12-18 / 2026-02-20 | candidates exist before 2021-11 entry; no overlap with selected entry->D180 window | True |

## 6. Canonical Archetype Compression Map

| fine_archetype_id | canonical_archetype_id | Compression rule |
|---|---|---|
| GAME_IP_GLOBAL_LIVE_SERVICE_MONETIZATION | C27_CONTENT_IP_GLOBAL_MONETIZATION | Owned game IP + live-service monetization + global demand can qualify as C27 positive if margin/revision bridge is visible. |
| WEBTOON_TO_GAME_IP_LAUNCH_WITH_WEAK_RETENTION | C27_CONTENT_IP_GLOBAL_MONETIZATION | Launch-day IP evidence remains C27 but should be capped unless retention, payer conversion, or repeat monetization is visible. |
| P2E_TOKENIZED_GAME_IP_THESIS_BREAK | C27_CONTENT_IP_GLOBAL_MONETIZATION | Tokenized/P2E IP is C27 only as a guard/4B/4C path when token trust or regulatory risk dominates the thesis. |

## 7. Case Selection Summary

| case_id | symbol | company | role | best_trigger | positive/counterexample | current_profile_verdict |
|---|---:|---|---|---|---|---|
| R8L31_C27_259960_KRAFTON_GLOBAL_LIVE_SERVICE_POS | 259960 | 크래프톤 | structural_success | R8L31_C27_KRAFTON_STAGE2_BGMI_PUBG_20231108 | positive | current_profile_too_late |
| R8L31_C27_251270_NETMARBLE_IP_LAUNCH_HIGH_MAE_COUNTER | 251270 | 넷마블 | failed_rerating | R8L31_C27_NETMARBLE_SOLO_LEVELING_LAUNCH_20240508 | counterexample | current_profile_false_positive |
| R8L31_C27_112040_WEMADE_P2E_TOKENIZED_IP_4C_COUNTER | 112040 | 위메이드 | false_positive_green | R8L31_C27_WEMADE_P2E_TOKENIZED_IP_20211119 | counterexample | current_profile_false_positive |


## 8. Positive vs Counterexample Balance

```text
positive_case_count = 1
counterexample_count = 2
4B_case_count = 1
4C_case_count = 1
calibration_usable_case_count = 3
calibration_usable_trigger_count = 6
representative_trigger_count = 3
```

The balance is intentionally conservative: one clean non-K-pop game-IP positive against two counterexamples. This prevents a broad C27 promotion that would turn launch hype or token economics into a false Green path.

## 9. Evidence Source Map

| case_id | evidence summary | evidence_source | timing rule |
|---|---|---|---|
| R8L31_C27_259960_KRAFTON_GLOBAL_LIVE_SERVICE_POS | PUBG/BGMI live-service monetization and global game IP durability; later confirmation validates the earlier Stage2 signal. | Public Krafton/BGMI/PUBG evidence family plus Stock-Web rows. | 2023-11-08 close; event/earnings window visible around the date. |
| R8L31_C27_251270_NETMARBLE_IP_LAUNCH_HIGH_MAE_COUNTER | Solo Leveling: ARISE launch made the IP route visible, but repeat monetization/retention was not yet proven. | Public release-date evidence plus Stock-Web rows. | 2024-05-08 close; launch day. |
| R8L31_C27_112040_WEMADE_P2E_TOKENIZED_IP_4C_COUNTER | MIR4/P2E/tokenized IP narrative produced a blowoff; token/regulatory trust risk dominated ordinary content-IP monetization. | Public P2E/MIR4/WEMIX evidence family plus Stock-Web rows. | 2021-11-19 close and 2022-02-10 4C row. |

## 10. Price Data Source Map

| symbol | tradable shard(s) used | profile_path |
|---:|---|---|
| 259960 | atlas/ohlcv_tradable_by_symbol_year/259/259960/2023.csv; atlas/ohlcv_tradable_by_symbol_year/259/259960/2024.csv | atlas/symbol_profiles/259/259960.json |
| 251270 | atlas/ohlcv_tradable_by_symbol_year/251/251270/2024.csv; atlas/ohlcv_tradable_by_symbol_year/251/251270/2025.csv | atlas/symbol_profiles/251/251270.json |
| 112040 | atlas/ohlcv_tradable_by_symbol_year/112/112040/2021.csv; atlas/ohlcv_tradable_by_symbol_year/112/112040/2022.csv | atlas/symbol_profiles/112/112040.json |

## 11. Case-by-Case Trigger Grid

| trigger_id | symbol | type | trigger_date | entry_date | entry_price | stage2 evidence | stage3 evidence | 4B/4C evidence | current_profile_verdict |
|---|---:|---|---|---|---:|---|---|---|---|
| R8L31_C27_KRAFTON_STAGE2_BGMI_PUBG_20231108 | 259960 | Stage2-Actionable | 2023-11-08 | 2023-11-08 | 190,800 | public_event_or_disclosure, customer_or_order_quality, capacity_or_volume_route, early_revision_signal | financial_visibility, margin_bridge, durable_customer_confirmation | - | current_profile_too_late |
| R8L31_C27_KRAFTON_GREEN_CONFIRMATION_20240213 | 259960 | Stage3-Green-comparison | 2024-02-13 | 2024-02-13 | 230,000 | public_event_or_disclosure, customer_or_order_quality | confirmed_revision, financial_visibility, multiple_public_sources, durable_customer_confirmation | - | current_profile_correct |
| R8L31_C27_NETMARBLE_SOLO_LEVELING_LAUNCH_20240508 | 251270 | Stage2-Actionable-stress | 2024-05-08 | 2024-05-08 | 60,700 | public_event_or_disclosure, customer_or_order_quality, relative_strength | - | valuation_blowoff, positioning_overheat, margin_or_backlog_slowdown, thesis_evidence_broken | current_profile_false_positive |
| R8L31_C27_NETMARBLE_LOCAL_4B_20240510 | 251270 | Stage4B-Overlay | 2024-05-10 | 2024-05-10 | 69,400 | - | - | valuation_blowoff, positioning_overheat, price_only_local_peak, margin_or_backlog_slowdown, thesis_evidence_broken | current_profile_4B_too_late |
| R8L31_C27_WEMADE_P2E_TOKENIZED_IP_20211119 | 112040 | Stage2-false-positive-stress | 2021-11-19 | 2021-11-19 | 237,000 | public_event_or_disclosure, relative_strength, policy_or_regulatory_optionality | - | valuation_blowoff, positioning_overheat, legal_or_regulatory_block, regulatory_rejection, accounting_or_trust_break, thesis_evidence_broken | current_profile_false_positive |
| R8L31_C27_WEMADE_4C_TOKEN_BREAK_20220210 | 112040 | Stage4C-ThesisBreak | 2022-02-10 | 2022-02-10 | 106,600 | - | - | legal_or_regulatory_block, valuation_blowoff, regulatory_rejection, accounting_or_trust_break, forced_liquidation_or_crash, thesis_evidence_broken | current_profile_4C_too_late |


## 12. Trigger-Level OHLC Backtest Tables

| trigger_id | entry | MFE30 | MAE30 | MFE90 | MAE90 | MFE180 | MAE180 | peak | drawdown_after_peak | aggregate_role |
|---|---:|---:|---:|---:|---:|---:|---:|---|---:|---|
| R8L31_C27_KRAFTON_STAGE2_BGMI_PUBG_20231108 | 190,800 | 16.09 | -2.36 | 38.89 | -7.23 | 56.71 | -7.23 | 2024-06-24 / 299,000 | -10.37 | representative |
| R8L31_C27_KRAFTON_GREEN_CONFIRMATION_20240213 | 230,000 | 15.22 | -8.7 | 30.0 | -8.7 | 31.3 | -8.7 | 2024-07-30 / 302,000 | -10.6 | label_comparison_only |
| R8L31_C27_NETMARBLE_SOLO_LEVELING_LAUNCH_20240508 | 60,700 | 19.28 | -12.03 | 19.28 | -13.67 | 19.28 | -30.23 | 2024-05-10 / 72,400 | -41.51 | representative |
| R8L31_C27_NETMARBLE_LOCAL_4B_20240510 | 69,400 | 4.32 | -24.5 | 4.32 | -24.5 | 4.32 | -38.98 | 2024-05-10 / 72,400 | -41.51 | 4B_overlay_only |
| R8L31_C27_WEMADE_P2E_TOKENIZED_IP_20211119 | 237,000 | 3.67 | -37.43 | 3.67 | -60.42 | 3.67 | -78.06 | 2021-11-22 / 245,700 | -78.84 | representative |
| R8L31_C27_WEMADE_4C_TOKEN_BREAK_20220210 | 106,600 | 6.75 | -14.45 | 6.75 | -41.93 | 6.75 | -51.97 | 2022-04-06 / 113,500 | -54.89 | 4C_overlay_only |


Calculation basis:

```text
MFE_N_pct = (max(high from entry_date through N trading days) / entry_price - 1) * 100
MAE_N_pct = (min(low from entry_date through N trading days) / entry_price - 1) * 100
entry_price = c column on entry_date
price_basis = tradable_raw
```

## 13. Current Calibrated Profile Stress Test

| case_id | current profile likely behavior | actual MFE/MAE path | verdict | implication |
|---|---|---|---|---|
| Krafton | Would likely wait for stronger revision/Green confirmation. | Stage2 from 2023-11-08 produced +56.71% MFE180 with -7.23% MAE180. | current_profile_too_late | C27 game-IP live-service needs earlier shadow credit when monetization and margin bridge are visible. |
| Netmarble | Could over-read launch IP and price strength as C27 rerating. | +19.28% MFE180 but -30.23% MAE180 and -41.51% post-peak drawdown. | current_profile_false_positive | Launch-only IP requires retention/payer-conversion guard. |
| Wemade | Could mistake tokenized/P2E IP price strength for content-IP monetization. | +3.67% MFE180 but -78.06% MAE180 from blowoff entry. | current_profile_false_positive | Tokenized/P2E IP must route to 4B/4C unless token trust/regulatory risk is clean. |

Axis notes:

```text
stage2_actionable_evidence_bonus: kept; in C27 it should be conditional on monetization quality.
stage3_yellow_total_min: kept; Yellow can work for early game-IP evidence.
stage3_green_total_min / revision_min: strengthened within C27; launch-only IP should not cross Green without retention/margin bridge.
price_only_blowoff_blocks_positive_stage: strengthened.
full_4b_requires_non_price_evidence: kept; Netmarble local 4B has event/retention-risk context, not pure price-only.
hard_4c_thesis_break_routes_to_4c: strengthened for tokenized/P2E IP.
```

## 14. Stage2 / Yellow / Green Comparison

| case_id | Stage2 entry | later Green/comparison | green_lateness_ratio | interpretation |
|---|---:|---:|---:|---|
| Krafton | 190,800 | 230,000 | 0.362 | Green confirmation was valid but entered after roughly 36% of the Stage2-to-peak move had already accrued. |
| Netmarble | 60,700 | none | not_applicable | No clean Stage3-Green; launch signal should cap at watch/Yellow unless retention/repeat monetization appears. |
| Wemade | 237,000 | none | not_applicable | Tokenized/P2E blowoff should not receive Green at all. |

## 15. 4B Local vs Full-window Timing Audit

| case_id | 4B trigger | local proximity | full-window proximity | evidence type | verdict |
|---|---|---:|---:|---|---|
| Netmarble | R8L31_C27_NETMARBLE_LOCAL_4B_20240510 | 0.744 | 0.744 | valuation_blowoff; positioning_overheat; price_only; margin_or_backlog_slowdown | good_local_4B_timing_when_no_repeat_retention_evidence |
| Wemade | R8L31_C27_WEMADE_P2E_TOKENIZED_IP_20211119 | n/a | n/a | valuation_blowoff; positioning_overheat; legal_or_regulatory_block | tokenized_ip_blowoff_should_not_train_c27_positive |

## 16. 4C Protection Audit

| case_id | 4C trigger | label | note |
|---|---|---|---|
| Wemade | R8L31_C27_WEMADE_4C_TOKEN_BREAK_20220210 | hard_4c_success_after_blowoff_not_positive_entry | The row is used as protection/thesis-break calibration only. It does not train positive C27 weights. |
| Netmarble | n/a | thesis_break_watch_only | High MAE and failed retention bridge justify watch/guard, but no hard 4C row is asserted. |

## 17. Sector-Specific Rule Candidate

```text
sector_specific_rule_candidate = true
rule_scope = L8_PLATFORM_CONTENT_SW_SECURITY
candidate = In platform/content/software, IP launch or theme strength is insufficient unless repeat monetization/retention closes the loop.
```

This is sector-specific because the failure mode is common to platform/content/SW: a visible product launch can act like a bright storefront, but the register behind the counter must ring repeatedly. Without retention, payer conversion, renewal, or margin bridge, the early crowd is not yet a business moat.

## 18. Canonical-Archetype Rule Candidate

```text
canonical_archetype_rule_candidate = true
rule_scope = C27_CONTENT_IP_GLOBAL_MONETIZATION
candidate_rule_1 = c27_game_ip_live_service_monetization_bonus
candidate_rule_2 = c27_ip_launch_without_retention_green_cap
candidate_rule_3 = c27_tokenized_p2e_ip_4c_guard
```

Mechanism:

```text
if C27 evidence is owned/live-service IP + repeat monetization + margin/revision bridge:
    allow earlier Stage2/Yellow shadow promotion

if C27 evidence is one-time launch, chart rank, or event premium without retention/payer conversion:
    cap at Watch/Yellow and block Green

if C27 evidence depends on token economics or regulatory/trust-sensitive P2E route:
    route to 4B/4C guard unless trust risk is clean
```

## 19. Before / After Backtest Comparison

| profile_id | scope | eligible representative triggers | avg_MFE_90D | avg_MAE_90D | avg_MFE_180D | avg_MAE_180D | false_positive_rate | missed_structural_count | score_return_alignment_verdict |
|---|---|---:|---:|---:|---:|---:|---:|---:|---|
| P0 e2r_2_1_stock_web_calibrated_proxy | current | 3 | 20.61 | -33.77 | 26.55 | -38.51 | 0.67 | 1 | mixed: Krafton late; Netmarble/Wemade false positive risk |
| P0b e2r_2_0_baseline_reference | rollback | 3 | 20.61 | -33.77 | 26.55 | -38.51 | 0.67 | 1 | weaker guards would over-credit event/theme strength |
| P1 sector_specific_candidate_profile | L8 | 3 | 38.89* | -7.23* | 56.71* | -7.23* | 0.00 | 0 | filters to clean live-service monetization only |
| P2 canonical_archetype_candidate_profile | C27 | 3 | 38.89* | -7.23* | 56.71* | -7.23* | 0.00 | 0 | best precision; keeps Krafton and blocks launch/token false positives |
| P3 counterexample_guard_profile | C27 guard | 3 | 38.89* | -7.23* | 56.71* | -7.23* | 0.00 | 1 | safest, but may under-promote borderline new-IP launches |

`*` Guard-filtered averages include only selected positive representative trigger(s); counterexamples remain in false-positive audit, not positive-return averaging.

## 20. Score-Return Alignment Matrix

| trigger_id | weighted_score_before | stage_before | weighted_score_after | stage_after | score_return_alignment_label |
|---|---:|---|---:|---|---|
| R8L31_C27_KRAFTON_STAGE2_BGMI_PUBG_20231108 | 82 | Stage3-Yellow | 88 | Stage3-Green-shadow | aligned_positive |
| R8L31_C27_KRAFTON_GREEN_CONFIRMATION_20240213 | 89 | Stage3-Green | 89 | Stage3-Green | aligned_positive |
| R8L31_C27_NETMARBLE_SOLO_LEVELING_LAUNCH_20240508 | 77 | Stage3-Yellow-risk | 60 | Watch/Stage2-blocked | guard_improves_alignment |
| R8L31_C27_NETMARBLE_LOCAL_4B_20240510 | 70 | 4B-risk | 50 | 4B-overlay-only | guard_improves_alignment |
| R8L31_C27_WEMADE_P2E_TOKENIZED_IP_20211119 | 84 | False Stage3-Yellow/Green risk | 42 | 4B/4C-guard | guard_improves_alignment |
| R8L31_C27_WEMADE_4C_TOKEN_BREAK_20220210 | 45 | Stage4C-watch | 30 | Stage4C | guard_improves_alignment |

## 21. Coverage Matrix

| large_sector_id | canonical_archetype_id | fine_archetype_id | positive_case_count | counterexample_count | 4B_case_count | 4C_case_count | new_independent_case_count | reused_case_count | calibration_usable_trigger_count | representative_trigger_count | current_profile_error_count | sector_rule_candidate | canonical_rule_candidate | coverage_gap_after_this_loop |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|---|---|
| L8_PLATFORM_CONTENT_SW_SECURITY | C27_CONTENT_IP_GLOBAL_MONETIZATION | GAME_IP_GLOBAL_LIVE_SERVICE_MONETIZATION; WEBTOON_TO_GAME_IP_LAUNCH_WITH_WEAK_RETENTION; P2E_TOKENIZED_GAME_IP_THESIS_BREAK | 1 | 2 | 1 | 1 | 3 | 0 | 6 | 3 | 4 | true | true | Still needs additional C27 hard 4C cases involving artist/contract loss, platform take-rate deterioration, and cancellation risk. |

## 22. Residual Contribution Summary

```text
new_independent_case_count: 3
reused_case_count: 0
reused_case_ids: []
new_symbol_count: 3
same_archetype_new_symbol_count: 3
same_archetype_new_trigger_family_count: 3
new_canonical_archetype_count: 0
new_fine_archetype_count: 3
new_trigger_family_count: 3
positive_case_count: 1
counterexample_count: 2
current_profile_error_count: 4
tested_existing_calibrated_axes:
  - stage2_actionable_evidence_bonus
  - stage3_green_revision_min
  - price_only_blowoff_blocks_positive_stage
  - full_4b_requires_non_price_evidence
  - hard_4c_thesis_break_routes_to_4c
residual_error_types_found:
  - game_ip_launch_without_retention_high_mae
  - tokenized_p2e_ip_false_positive
  - green_confirmation_partially_late_for_live_service_ip
new_axis_proposed:
  - c27_game_ip_live_service_monetization_bonus
  - c27_ip_launch_without_retention_green_cap
  - c27_tokenized_p2e_ip_4c_guard
existing_axis_strengthened:
  - stage3_green_revision_min within C27 only
  - price_only_blowoff_blocks_positive_stage
  - hard_4c_thesis_break_routes_to_4c
existing_axis_weakened: null
existing_axis_kept:
  - stage2_actionable_evidence_bonus
  - full_4b_requires_non_price_evidence
sector_specific_rule_candidate: true
canonical_archetype_rule_candidate: true
no_new_signal_reason: null
loop_contribution_label: canonical_archetype_rule_candidate
do_not_propose_new_weight_delta: false
auto_selected_coverage_gap: R8/C27 needed non-K-pop game IP, launch-retention counterexample, and tokenized/P2E 4C path.
diversity_score_summary: high; 3 same-archetype new symbols, 3 new trigger families, 1 positive, 2 counterexamples, no reused cases.
```

## 23. Validation Scope / Non-Validation Scope

Validated:

```text
- Stock-Web manifest/schema basis
- symbol profile availability and corporate-action caveats
- entry_date / entry_price from tradable raw close
- 30D / 90D / 180D MFE and MAE for representative rows
- 4B local vs full-window proximity for Netmarble
- 4C/protection-only routing for Wemade
```

Not validated:

```text
- production code behavior inside src/e2r
- live candidate scan
- brokerage/trading execution
- final production scoring weights
- 1Y/2Y calibration fields; present as null because this loop is 180D-first
```

## 24. Shadow Weight Calibration

```csv
row_type,axis,scope,large_sector_id,canonical_archetype_id,baseline_value,tested_value,delta,reason,backtest_effect,trigger_ids,calibration_usable_count,new_independent_case_count,counterexample_count,confidence,proposal_type,notes
shadow_weight,c27_game_ip_live_service_monetization_bonus,canonical_archetype_specific,L8_PLATFORM_CONTENT_SW_SECURITY,C27_CONTENT_IP_GLOBAL_MONETIZATION,0,+2,+2,"Krafton showed clean global game-IP/live-service monetization with +56.71% 180D MFE and only -7.23% 180D MAE from Stage2","reduces missed/late structural signal for non-K-pop game IP",R8L31_C27_KRAFTON_STAGE2_BGMI_PUBG_20231108,1,1,0,medium,canonical_shadow_only,"not production; requires explicit monetization and margin/revision bridge"
shadow_weight,c27_ip_launch_without_retention_green_cap,canonical_archetype_specific,L8_PLATFORM_CONTENT_SW_SECURITY,C27_CONTENT_IP_GLOBAL_MONETIZATION,absent,active,guard,"Netmarble launch evidence produced local event premium but -30.23% 180D MAE without durable retention/repeat monetization evidence","blocks launch-only C27 false positives from training positive Green",R8L31_C27_NETMARBLE_SOLO_LEVELING_LAUNCH_20240508|R8L31_C27_NETMARBLE_LOCAL_4B_20240510,2,1,1,medium,counterexample_guard,"not production; launch evidence must bridge to retention or payer conversion"
shadow_weight,c27_tokenized_p2e_ip_4c_guard,canonical_archetype_specific,L8_PLATFORM_CONTENT_SW_SECURITY,C27_CONTENT_IP_GLOBAL_MONETIZATION,absent,active,guard,"Wemade P2E/tokenized IP had +3.67% 180D MFE but -78.06% 180D MAE from the blowoff entry","routes token-trust/regulatory breaks to 4B/4C instead of positive C27",R8L31_C27_WEMADE_P2E_TOKENIZED_IP_20211119|R8L31_C27_WEMADE_4C_TOKEN_BREAK_20220210,2,1,1,medium,4C_guard,"4C/protection calibration only"
```

## 25. Machine-Readable Rows

```jsonl
{"row_type": "price_source_validation", "source": "Songdaiki/stock-web", "source_url": "https://github.com/Songdaiki/stock-web", "manifest_path": "atlas/manifest.json", "schema_path": "atlas/schema.json", "universe_path": "atlas/universe/all_symbols.csv", "manifest_max_date": "2026-02-20", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "raw_shard_root": "atlas/ohlcv_raw_by_symbol_year", "validation_status": "usable_for_historical_calibration"}
{"row_type": "case", "case_id": "R8L31_C27_259960_KRAFTON_GLOBAL_LIVE_SERVICE_POS", "symbol": "259960", "company_name": "크래프톤", "round": "R8", "loop": "31", "large_sector_id": "L8_PLATFORM_CONTENT_SW_SECURITY", "canonical_archetype_id": "C27_CONTENT_IP_GLOBAL_MONETIZATION", "fine_archetype_id": "GAME_IP_GLOBAL_LIVE_SERVICE_MONETIZATION; WEBTOON_TO_GAME_IP_LAUNCH_WITH_WEAK_RETENTION; P2E_TOKENIZED_GAME_IP_THESIS_BREAK", "case_type": "structural_success", "positive_or_counterexample": "positive", "best_trigger": "R8L31_C27_KRAFTON_STAGE2_BGMI_PUBG_20231108", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "aligned_positive", "current_profile_verdict": "current_profile_too_late", "price_source": "Songdaiki/stock-web", "notes": "Positive non-K-pop C27: live-service game IP monetization with low early MAE and large 180D MFE."}
{"row_type": "case", "case_id": "R8L31_C27_251270_NETMARBLE_IP_LAUNCH_HIGH_MAE_COUNTER", "symbol": "251270", "company_name": "넷마블", "round": "R8", "loop": "31", "large_sector_id": "L8_PLATFORM_CONTENT_SW_SECURITY", "canonical_archetype_id": "C27_CONTENT_IP_GLOBAL_MONETIZATION", "fine_archetype_id": "GAME_IP_GLOBAL_LIVE_SERVICE_MONETIZATION; WEBTOON_TO_GAME_IP_LAUNCH_WITH_WEAK_RETENTION; P2E_TOKENIZED_GAME_IP_THESIS_BREAK", "case_type": "failed_rerating", "positive_or_counterexample": "counterexample", "best_trigger": "R8L31_C27_NETMARBLE_SOLO_LEVELING_LAUNCH_20240508", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "counterexample_guard_needed", "current_profile_verdict": "current_profile_false_positive", "price_source": "Songdaiki/stock-web", "notes": "Launch-day IP evidence produced only modest local MFE and then deep 180D MAE; needs retention/repeat-monetization guard."}
{"row_type": "case", "case_id": "R8L31_C27_112040_WEMADE_P2E_TOKENIZED_IP_4C_COUNTER", "symbol": "112040", "company_name": "위메이드", "round": "R8", "loop": "31", "large_sector_id": "L8_PLATFORM_CONTENT_SW_SECURITY", "canonical_archetype_id": "C27_CONTENT_IP_GLOBAL_MONETIZATION", "fine_archetype_id": "GAME_IP_GLOBAL_LIVE_SERVICE_MONETIZATION; WEBTOON_TO_GAME_IP_LAUNCH_WITH_WEAK_RETENTION; P2E_TOKENIZED_GAME_IP_THESIS_BREAK", "case_type": "false_positive_green", "positive_or_counterexample": "counterexample", "best_trigger": "R8L31_C27_WEMADE_P2E_TOKENIZED_IP_20211119", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "counterexample_guard_needed", "current_profile_verdict": "current_profile_false_positive", "price_source": "Songdaiki/stock-web", "notes": "Tokenized game-IP/P2E narrative should be a C27 guard/4C route rather than positive content-IP monetization."}
{"row_type": "trigger", "trigger_id": "R8L31_C27_KRAFTON_STAGE2_BGMI_PUBG_20231108", "case_id": "R8L31_C27_259960_KRAFTON_GLOBAL_LIVE_SERVICE_POS", "symbol": "259960", "company_name": "크래프톤", "round": "R8", "loop": "31", "large_sector_id": "L8_PLATFORM_CONTENT_SW_SECURITY", "canonical_archetype_id": "C27_CONTENT_IP_GLOBAL_MONETIZATION", "fine_archetype_id": "GAME_IP_GLOBAL_LIVE_SERVICE_MONETIZATION", "sector": "플랫폼·콘텐츠·SW·보안", "primary_archetype": "global_game_ip_live_service_monetization", "loop_objective": "coverage_gap_fill|counterexample_mining|4B_non_price_requirement_stress_test|4C_thesis_break_timing_test|canonical_archetype_compression|green_strictness_stress_test", "trigger_type": "Stage2-Actionable", "trigger_date": "2023-11-08", "evidence_available_at_that_date": "After the November 2023 earnings/event window, PUBG/BGMI live-service monetization and global game IP durability were visible before the later 2024 full rerating. Entry uses 2023-11-08 close from Stock-Web.", "evidence_source": "Krafton historical Q3/live-service and BGMI/PUBG public evidence family; OHLC verified in Stock-Web 2023/2024 tradable shards.", "stage2_evidence_fields": ["public_event_or_disclosure", "customer_or_order_quality", "capacity_or_volume_route", "early_revision_signal"], "stage3_evidence_fields": ["financial_visibility", "margin_bridge", "durable_customer_confirmation"], "stage4b_evidence_fields": [], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/259/259960/2023.csv", "profile_path": "atlas/symbol_profiles/259/259960.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "entry_date": "2023-11-08", "entry_price": 190800, "MFE_30D_pct": 16.09, "MFE_90D_pct": 38.89, "MFE_180D_pct": 56.71, "MFE_1Y_pct": null, "MFE_2Y_pct": null, "MAE_30D_pct": -2.36, "MAE_90D_pct": -7.23, "MAE_180D_pct": -7.23, "MAE_1Y_pct": null, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2024-06-24", "peak_price": 299000, "drawdown_after_peak_pct": -10.37, "green_lateness_ratio": null, "four_b_local_peak_proximity": null, "four_b_full_window_peak_proximity": null, "four_b_timing_verdict": "not_applicable", "four_b_evidence_type": [], "four_c_protection_label": "not_applicable", "trigger_outcome_label": "structural_success_global_live_service_ip", "current_profile_verdict": "current_profile_too_late", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window", "same_entry_group_id": "R8L31_G01_259960_2023-11-08_190800", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false}
{"row_type": "trigger", "trigger_id": "R8L31_C27_KRAFTON_GREEN_CONFIRMATION_20240213", "case_id": "R8L31_C27_259960_KRAFTON_GLOBAL_LIVE_SERVICE_POS", "symbol": "259960", "company_name": "크래프톤", "round": "R8", "loop": "31", "large_sector_id": "L8_PLATFORM_CONTENT_SW_SECURITY", "canonical_archetype_id": "C27_CONTENT_IP_GLOBAL_MONETIZATION", "fine_archetype_id": "GAME_IP_GLOBAL_LIVE_SERVICE_MONETIZATION", "sector": "플랫폼·콘텐츠·SW·보안", "primary_archetype": "global_game_ip_live_service_monetization", "loop_objective": "coverage_gap_fill|counterexample_mining|4B_non_price_requirement_stress_test|4C_thesis_break_timing_test|canonical_archetype_compression|green_strictness_stress_test", "trigger_type": "Stage3-Green-comparison", "trigger_date": "2024-02-13", "evidence_available_at_that_date": "Later confirmation made Green reasonable, but the Stock-Web path shows part of the upside had already accrued from the Stage2 reference.", "evidence_source": "Stock-Web 2024 tradable shard around 2024-02-13; historical earnings confirmation family.", "stage2_evidence_fields": ["public_event_or_disclosure", "customer_or_order_quality"], "stage3_evidence_fields": ["confirmed_revision", "financial_visibility", "multiple_public_sources", "durable_customer_confirmation"], "stage4b_evidence_fields": [], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/259/259960/2024.csv", "profile_path": "atlas/symbol_profiles/259/259960.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "entry_date": "2024-02-13", "entry_price": 230000, "MFE_30D_pct": 15.22, "MFE_90D_pct": 30.0, "MFE_180D_pct": 31.3, "MFE_1Y_pct": null, "MFE_2Y_pct": null, "MAE_30D_pct": -8.7, "MAE_90D_pct": -8.7, "MAE_180D_pct": -8.7, "MAE_1Y_pct": null, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2024-07-30", "peak_price": 302000, "drawdown_after_peak_pct": -10.6, "green_lateness_ratio": 0.362, "four_b_local_peak_proximity": null, "four_b_full_window_peak_proximity": null, "four_b_timing_verdict": "not_applicable", "four_b_evidence_type": [], "four_c_protection_label": "not_applicable", "trigger_outcome_label": "green_valid_but_partially_late", "current_profile_verdict": "current_profile_correct", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window", "same_entry_group_id": "R8L31_G02_259960_2024-02-13_230000", "dedupe_for_aggregate": false, "aggregate_group_role": "label_comparison_only", "is_new_independent_case": true, "reuse_reason": "same_symbol_new_green_lateness_comparison", "independent_evidence_weight": 0.25, "do_not_count_as_new_case": false}
{"row_type": "trigger", "trigger_id": "R8L31_C27_NETMARBLE_SOLO_LEVELING_LAUNCH_20240508", "case_id": "R8L31_C27_251270_NETMARBLE_IP_LAUNCH_HIGH_MAE_COUNTER", "symbol": "251270", "company_name": "넷마블", "round": "R8", "loop": "31", "large_sector_id": "L8_PLATFORM_CONTENT_SW_SECURITY", "canonical_archetype_id": "C27_CONTENT_IP_GLOBAL_MONETIZATION", "fine_archetype_id": "WEBTOON_TO_GAME_IP_LAUNCH_WITH_WEAK_RETENTION", "sector": "플랫폼·콘텐츠·SW·보안", "primary_archetype": "webtoon_to_game_ip_launch_monetization", "loop_objective": "coverage_gap_fill|counterexample_mining|4B_non_price_requirement_stress_test|4C_thesis_break_timing_test|canonical_archetype_compression|green_strictness_stress_test", "trigger_type": "Stage2-Actionable-stress", "trigger_date": "2024-05-08", "evidence_available_at_that_date": "Solo Leveling: ARISE launch made the IP route visible, but at trigger date the evidence did not yet prove repeat monetization/retention or margin durability. Stock-Web confirms modest MFE but deep 180D MAE.", "evidence_source": "Solo Leveling: ARISE release timing and Stock-Web 2024/2025 tradable shards.", "stage2_evidence_fields": ["public_event_or_disclosure", "customer_or_order_quality", "relative_strength"], "stage3_evidence_fields": [], "stage4b_evidence_fields": ["valuation_blowoff", "positioning_overheat", "margin_or_backlog_slowdown"], "stage4c_evidence_fields": ["thesis_evidence_broken"], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/251/251270/2024.csv", "profile_path": "atlas/symbol_profiles/251/251270.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "entry_date": "2024-05-08", "entry_price": 60700, "MFE_30D_pct": 19.28, "MFE_90D_pct": 19.28, "MFE_180D_pct": 19.28, "MFE_1Y_pct": null, "MFE_2Y_pct": null, "MAE_30D_pct": -12.03, "MAE_90D_pct": -13.67, "MAE_180D_pct": -30.23, "MAE_1Y_pct": null, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2024-05-10", "peak_price": 72400, "drawdown_after_peak_pct": -41.51, "green_lateness_ratio": "not_applicable:no_confirmed_Stage3_Green_trigger", "four_b_local_peak_proximity": null, "four_b_full_window_peak_proximity": null, "four_b_timing_verdict": "stage2_positive_requires_retention_or_repeat_monetization_guard", "four_b_evidence_type": [], "four_c_protection_label": "thesis_break_watch_only", "trigger_outcome_label": "failed_rerating_high_mae_after_ip_launch", "current_profile_verdict": "current_profile_false_positive", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window", "same_entry_group_id": "R8L31_G03_251270_2024-05-08_60700", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false}
{"row_type": "trigger", "trigger_id": "R8L31_C27_NETMARBLE_LOCAL_4B_20240510", "case_id": "R8L31_C27_251270_NETMARBLE_IP_LAUNCH_HIGH_MAE_COUNTER", "symbol": "251270", "company_name": "넷마블", "round": "R8", "loop": "31", "large_sector_id": "L8_PLATFORM_CONTENT_SW_SECURITY", "canonical_archetype_id": "C27_CONTENT_IP_GLOBAL_MONETIZATION", "fine_archetype_id": "WEBTOON_TO_GAME_IP_LAUNCH_WITH_WEAK_RETENTION", "sector": "플랫폼·콘텐츠·SW·보안", "primary_archetype": "webtoon_to_game_ip_launch_monetization", "loop_objective": "coverage_gap_fill|counterexample_mining|4B_non_price_requirement_stress_test|4C_thesis_break_timing_test|canonical_archetype_compression|green_strictness_stress_test", "trigger_type": "Stage4B-Overlay", "trigger_date": "2024-05-10", "evidence_available_at_that_date": "Two sessions after the launch trigger, price had already entered local event-premium territory while repeat monetization remained unproven.", "evidence_source": "Stock-Web 2024/2025 tradable shards; Solo Leveling release event family.", "stage2_evidence_fields": [], "stage3_evidence_fields": [], "stage4b_evidence_fields": ["valuation_blowoff", "positioning_overheat", "price_only_local_peak", "margin_or_backlog_slowdown"], "stage4c_evidence_fields": ["thesis_evidence_broken"], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/251/251270/2024.csv", "profile_path": "atlas/symbol_profiles/251/251270.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "entry_date": "2024-05-10", "entry_price": 69400, "MFE_30D_pct": 4.32, "MFE_90D_pct": 4.32, "MFE_180D_pct": 4.32, "MFE_1Y_pct": null, "MFE_2Y_pct": null, "MAE_30D_pct": -24.5, "MAE_90D_pct": -24.5, "MAE_180D_pct": -38.98, "MAE_1Y_pct": null, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2024-05-10", "peak_price": 72400, "drawdown_after_peak_pct": -41.51, "green_lateness_ratio": "not_applicable:4B_overlay", "four_b_local_peak_proximity": 0.744, "four_b_full_window_peak_proximity": 0.744, "four_b_timing_verdict": "good_local_4B_timing_when_no_repeat_retention_evidence", "four_b_evidence_type": ["valuation_blowoff", "positioning_overheat", "price_only", "margin_or_backlog_slowdown"], "four_c_protection_label": "thesis_break_watch_only", "trigger_outcome_label": "4B_overlay_success_after_ip_launch_spike", "current_profile_verdict": "current_profile_4B_too_late", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window", "same_entry_group_id": "R8L31_G04_251270_2024-05-10_69400", "dedupe_for_aggregate": false, "aggregate_group_role": "4B_overlay_only", "is_new_independent_case": true, "reuse_reason": "same_case_new_4B_overlay_path", "independent_evidence_weight": 0.25, "do_not_count_as_new_case": false}
{"row_type": "trigger", "trigger_id": "R8L31_C27_WEMADE_P2E_TOKENIZED_IP_20211119", "case_id": "R8L31_C27_112040_WEMADE_P2E_TOKENIZED_IP_4C_COUNTER", "symbol": "112040", "company_name": "위메이드", "round": "R8", "loop": "31", "large_sector_id": "L8_PLATFORM_CONTENT_SW_SECURITY", "canonical_archetype_id": "C27_CONTENT_IP_GLOBAL_MONETIZATION", "fine_archetype_id": "P2E_TOKENIZED_GAME_IP_THESIS_BREAK", "sector": "플랫폼·콘텐츠·SW·보안", "primary_archetype": "tokenized_game_ip_p2e_monetization", "loop_objective": "coverage_gap_fill|counterexample_mining|4B_non_price_requirement_stress_test|4C_thesis_break_timing_test|canonical_archetype_compression|green_strictness_stress_test", "trigger_type": "Stage2-false-positive-stress", "trigger_date": "2021-11-19", "evidence_available_at_that_date": "MIR4/P2E and tokenized IP narrative was visible, but the driver was not conventional content-IP monetization with controllable retention. The 180D path is a severe counterexample.", "evidence_source": "MIR4/P2E public event family; Stock-Web 2021/2022 tradable shards.", "stage2_evidence_fields": ["public_event_or_disclosure", "relative_strength", "policy_or_regulatory_optionality"], "stage3_evidence_fields": [], "stage4b_evidence_fields": ["valuation_blowoff", "positioning_overheat", "legal_or_regulatory_block"], "stage4c_evidence_fields": ["regulatory_rejection", "accounting_or_trust_break", "thesis_evidence_broken"], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/112/112040/2021.csv", "profile_path": "atlas/symbol_profiles/112/112040.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "entry_date": "2021-11-19", "entry_price": 237000, "MFE_30D_pct": 3.67, "MFE_90D_pct": 3.67, "MFE_180D_pct": 3.67, "MFE_1Y_pct": null, "MFE_2Y_pct": null, "MAE_30D_pct": -37.43, "MAE_90D_pct": -60.42, "MAE_180D_pct": -78.06, "MAE_1Y_pct": null, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2021-11-22", "peak_price": 245700, "drawdown_after_peak_pct": -78.84, "green_lateness_ratio": "not_applicable:no_confirmed_Stage3_Green_trigger", "four_b_local_peak_proximity": null, "four_b_full_window_peak_proximity": null, "four_b_timing_verdict": "tokenized_ip_blowoff_should_not_train_c27_positive", "four_b_evidence_type": ["valuation_blowoff", "positioning_overheat", "price_only", "legal_or_regulatory_block"], "four_c_protection_label": "hard_4c_late", "trigger_outcome_label": "false_positive_tokenized_ip_blowoff", "current_profile_verdict": "current_profile_false_positive", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_after_prior_2021-10-06_candidate; no candidate inside entry_to_D180", "same_entry_group_id": "R8L31_G05_112040_2021-11-19_237000", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false}
{"row_type": "trigger", "trigger_id": "R8L31_C27_WEMADE_4C_TOKEN_BREAK_20220210", "case_id": "R8L31_C27_112040_WEMADE_P2E_TOKENIZED_IP_4C_COUNTER", "symbol": "112040", "company_name": "위메이드", "round": "R8", "loop": "31", "large_sector_id": "L8_PLATFORM_CONTENT_SW_SECURITY", "canonical_archetype_id": "C27_CONTENT_IP_GLOBAL_MONETIZATION", "fine_archetype_id": "P2E_TOKENIZED_GAME_IP_THESIS_BREAK", "sector": "플랫폼·콘텐츠·SW·보안", "primary_archetype": "tokenized_game_ip_p2e_monetization", "loop_objective": "coverage_gap_fill|counterexample_mining|4B_non_price_requirement_stress_test|4C_thesis_break_timing_test|canonical_archetype_compression|green_strictness_stress_test", "trigger_type": "Stage4C-ThesisBreak", "trigger_date": "2022-02-10", "evidence_available_at_that_date": "After the tokenized-IP blowoff had begun to break, the row is used only as 4C/protection calibration, never as a new positive entry.", "evidence_source": "Stock-Web 2022 tradable shard; token-economics/regulatory trust-break public event family.", "stage2_evidence_fields": [], "stage3_evidence_fields": [], "stage4b_evidence_fields": ["legal_or_regulatory_block", "valuation_blowoff"], "stage4c_evidence_fields": ["regulatory_rejection", "accounting_or_trust_break", "forced_liquidation_or_crash", "thesis_evidence_broken"], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/112/112040/2022.csv", "profile_path": "atlas/symbol_profiles/112/112040.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "entry_date": "2022-02-10", "entry_price": 106600, "MFE_30D_pct": 6.75, "MFE_90D_pct": 6.75, "MFE_180D_pct": 6.75, "MFE_1Y_pct": null, "MFE_2Y_pct": null, "MAE_30D_pct": -14.45, "MAE_90D_pct": -41.93, "MAE_180D_pct": -51.97, "MAE_1Y_pct": null, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2022-04-06", "peak_price": 113500, "drawdown_after_peak_pct": -54.89, "green_lateness_ratio": "not_applicable:4C_overlay", "four_b_local_peak_proximity": null, "four_b_full_window_peak_proximity": null, "four_b_timing_verdict": "not_applicable", "four_b_evidence_type": ["legal_or_regulatory_block", "accounting_or_trust_break"], "four_c_protection_label": "hard_4c_success_after_blowoff_not_positive_entry", "trigger_outcome_label": "4C_protection_after_tokenized_ip_break", "current_profile_verdict": "current_profile_4C_too_late", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window", "same_entry_group_id": "R8L31_G06_112040_2022-02-10_106600", "dedupe_for_aggregate": false, "aggregate_group_role": "4C_overlay_only", "is_new_independent_case": true, "reuse_reason": "same_symbol_new_4C_timing_path", "independent_evidence_weight": 0.25, "do_not_count_as_new_case": false}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy_to_C27_shadow", "case_id": "R8L31_C27_259960_KRAFTON_GLOBAL_LIVE_SERVICE_POS", "trigger_id": "R8L31_C27_KRAFTON_STAGE2_BGMI_PUBG_20231108", "symbol": "259960", "large_sector_id": "L8_PLATFORM_CONTENT_SW_SECURITY", "canonical_archetype_id": "C27_CONTENT_IP_GLOBAL_MONETIZATION", "raw_component_scores_before": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 12, "revision_score": 12, "relative_strength_score": 10, "customer_quality_score": 15, "policy_or_regulatory_score": 0, "valuation_repricing_score": 8, "execution_risk_score": -2, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_before": 82, "stage_label_before": "Stage3-Yellow", "raw_component_scores_after": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 14, "revision_score": 14, "relative_strength_score": 10, "customer_quality_score": 17, "policy_or_regulatory_score": 0, "valuation_repricing_score": 8, "execution_risk_score": -2, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_after": 88, "stage_label_after": "Stage3-Green-shadow", "changed_components": ["customer_quality_score", "margin_bridge_score", "revision_score"], "component_delta_explanation": "C27 game-IP live-service route deserves promotion only when public monetization and margin/revision bridge are visible, not just price strength.", "MFE_90D_pct": 38.89, "MAE_90D_pct": -7.23, "score_return_alignment_label": "aligned_positive", "current_profile_verdict": "current_profile_too_late"}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy_to_C27_shadow", "case_id": "R8L31_C27_259960_KRAFTON_GLOBAL_LIVE_SERVICE_POS", "trigger_id": "R8L31_C27_KRAFTON_GREEN_CONFIRMATION_20240213", "symbol": "259960", "large_sector_id": "L8_PLATFORM_CONTENT_SW_SECURITY", "canonical_archetype_id": "C27_CONTENT_IP_GLOBAL_MONETIZATION", "raw_component_scores_before": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 14, "revision_score": 16, "relative_strength_score": 13, "customer_quality_score": 17, "policy_or_regulatory_score": 0, "valuation_repricing_score": 9, "execution_risk_score": 0, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_before": 89, "stage_label_before": "Stage3-Green", "raw_component_scores_after": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 14, "revision_score": 16, "relative_strength_score": 13, "customer_quality_score": 17, "policy_or_regulatory_score": 0, "valuation_repricing_score": 9, "execution_risk_score": 0, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_after": 89, "stage_label_after": "Stage3-Green", "changed_components": [], "component_delta_explanation": "Green confirmation row is valid but partially late versus the Stage2 reference.", "MFE_90D_pct": 30.0, "MAE_90D_pct": -8.7, "score_return_alignment_label": "aligned_positive", "current_profile_verdict": "current_profile_correct"}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy_to_C27_shadow", "case_id": "R8L31_C27_251270_NETMARBLE_IP_LAUNCH_HIGH_MAE_COUNTER", "trigger_id": "R8L31_C27_NETMARBLE_SOLO_LEVELING_LAUNCH_20240508", "symbol": "251270", "large_sector_id": "L8_PLATFORM_CONTENT_SW_SECURITY", "canonical_archetype_id": "C27_CONTENT_IP_GLOBAL_MONETIZATION", "raw_component_scores_before": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 0, "revision_score": 6, "relative_strength_score": 12, "customer_quality_score": 10, "policy_or_regulatory_score": 0, "valuation_repricing_score": 11, "execution_risk_score": -4, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_before": 77, "stage_label_before": "Stage3-Yellow-risk", "raw_component_scores_after": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 0, "revision_score": 2, "relative_strength_score": 12, "customer_quality_score": 5, "policy_or_regulatory_score": 0, "valuation_repricing_score": 5, "execution_risk_score": -14, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_after": 60, "stage_label_after": "Watch/Stage2-blocked", "changed_components": ["revision_score", "customer_quality_score", "execution_risk_score", "valuation_repricing_score"], "component_delta_explanation": "Launch-day IP signal is capped unless repeat retention, payer conversion, or margin bridge is visible.", "MFE_90D_pct": 19.28, "MAE_90D_pct": -13.67, "score_return_alignment_label": "guard_improves_alignment", "current_profile_verdict": "current_profile_false_positive"}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy_to_C27_shadow", "case_id": "R8L31_C27_251270_NETMARBLE_IP_LAUNCH_HIGH_MAE_COUNTER", "trigger_id": "R8L31_C27_NETMARBLE_LOCAL_4B_20240510", "symbol": "251270", "large_sector_id": "L8_PLATFORM_CONTENT_SW_SECURITY", "canonical_archetype_id": "C27_CONTENT_IP_GLOBAL_MONETIZATION", "raw_component_scores_before": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 0, "revision_score": 0, "relative_strength_score": 14, "customer_quality_score": 0, "policy_or_regulatory_score": 0, "valuation_repricing_score": 15, "execution_risk_score": -8, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_before": 70, "stage_label_before": "4B-risk", "raw_component_scores_after": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 0, "revision_score": 0, "relative_strength_score": 14, "customer_quality_score": 0, "policy_or_regulatory_score": 0, "valuation_repricing_score": 6, "execution_risk_score": -18, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_after": 50, "stage_label_after": "4B-overlay-only", "changed_components": ["execution_risk_score", "valuation_repricing_score"], "component_delta_explanation": "Local event-premium 4B is treated as overlay only, never as positive C27 training.", "MFE_90D_pct": 4.32, "MAE_90D_pct": -24.5, "score_return_alignment_label": "guard_improves_alignment", "current_profile_verdict": "current_profile_4B_too_late"}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy_to_C27_shadow", "case_id": "R8L31_C27_112040_WEMADE_P2E_TOKENIZED_IP_4C_COUNTER", "trigger_id": "R8L31_C27_WEMADE_P2E_TOKENIZED_IP_20211119", "symbol": "112040", "large_sector_id": "L8_PLATFORM_CONTENT_SW_SECURITY", "canonical_archetype_id": "C27_CONTENT_IP_GLOBAL_MONETIZATION", "raw_component_scores_before": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 0, "revision_score": 0, "relative_strength_score": 20, "customer_quality_score": 8, "policy_or_regulatory_score": 10, "valuation_repricing_score": 18, "execution_risk_score": -8, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_before": 84, "stage_label_before": "False Stage3-Yellow/Green risk", "raw_component_scores_after": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 0, "revision_score": 0, "relative_strength_score": 20, "customer_quality_score": 2, "policy_or_regulatory_score": -8, "valuation_repricing_score": 18, "execution_risk_score": -20, "legal_or_contract_risk_score": -14, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": -12}, "weighted_score_after": 42, "stage_label_after": "4B/4C-guard", "changed_components": ["customer_quality_score", "policy_or_regulatory_score", "execution_risk_score", "legal_or_contract_risk_score", "accounting_trust_risk_score"], "component_delta_explanation": "Tokenized/P2E game-IP is not clean C27 monetization when token trust/regulatory risk dominates the thesis.", "MFE_90D_pct": 3.67, "MAE_90D_pct": -60.42, "score_return_alignment_label": "guard_improves_alignment", "current_profile_verdict": "current_profile_false_positive"}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy_to_C27_shadow", "case_id": "R8L31_C27_112040_WEMADE_P2E_TOKENIZED_IP_4C_COUNTER", "trigger_id": "R8L31_C27_WEMADE_4C_TOKEN_BREAK_20220210", "symbol": "112040", "large_sector_id": "L8_PLATFORM_CONTENT_SW_SECURITY", "canonical_archetype_id": "C27_CONTENT_IP_GLOBAL_MONETIZATION", "raw_component_scores_before": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 0, "revision_score": 0, "relative_strength_score": 0, "customer_quality_score": 0, "policy_or_regulatory_score": 0, "valuation_repricing_score": 0, "execution_risk_score": -12, "legal_or_contract_risk_score": -10, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": -10}, "weighted_score_before": 45, "stage_label_before": "Stage4C-watch", "raw_component_scores_after": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 0, "revision_score": 0, "relative_strength_score": 0, "customer_quality_score": 0, "policy_or_regulatory_score": 0, "valuation_repricing_score": 0, "execution_risk_score": -18, "legal_or_contract_risk_score": -18, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": -18}, "weighted_score_after": 30, "stage_label_after": "Stage4C", "changed_components": ["legal_or_contract_risk_score", "accounting_trust_risk_score", "execution_risk_score"], "component_delta_explanation": "4C timing row: thesis-break/protection only, no positive entry weight.", "MFE_90D_pct": 6.75, "MAE_90D_pct": -41.93, "score_return_alignment_label": "guard_improves_alignment", "current_profile_verdict": "current_profile_4C_too_late"}
{"row_type": "residual_contribution", "round": "R8", "loop": "31", "large_sector_id": "L8_PLATFORM_CONTENT_SW_SECURITY", "canonical_archetype_id": "C27_CONTENT_IP_GLOBAL_MONETIZATION", "new_independent_case_count": 3, "reused_case_count": 0, "new_symbol_count": 3, "same_archetype_new_symbol_count": 3, "same_archetype_new_trigger_family_count": 3, "new_canonical_archetype_count": 0, "new_trigger_family_count": 3, "positive_case_count": 1, "counterexample_count": 2, "current_profile_error_count": 4, "tested_existing_calibrated_axes": ["stage2_actionable_evidence_bonus", "stage3_green_revision_min", "price_only_blowoff_blocks_positive_stage", "full_4b_requires_non_price_evidence", "hard_4c_thesis_break_routes_to_4c"], "residual_error_types_found": ["game_ip_launch_without_retention_high_mae", "tokenized_p2e_ip_false_positive", "green_confirmation_partially_late_for_live_service_ip"], "loop_contribution_label": "canonical_archetype_rule_candidate", "do_not_propose_new_weight_delta": false, "auto_selected_coverage_gap": "R8/C27 prior loop had K-pop and OTT cases; this loop adds non-K-pop game IP, launch-retention counterexample, and tokenized/P2E 4C path."}
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
next_round = R8 / C28 holdout or R9 / C29 mobility volume-margin operating leverage
preferred_next_gap = C27 hard 4C artist/contract-loss case OR C28 renewal-loss 4C case
```

## 28. Source Notes

Stock-Web source validation was based on the manifest/schema and tradable shard paths. The relevant Stock-Web files checked for this loop include:

- `atlas/manifest.json` and `atlas/schema.json`.
- `atlas/symbol_profiles/259/259960.json`, `atlas/ohlcv_tradable_by_symbol_year/259/259960/2023.csv`, `atlas/ohlcv_tradable_by_symbol_year/259/259960/2024.csv`.
- `atlas/symbol_profiles/251/251270.json`, `atlas/ohlcv_tradable_by_symbol_year/251/251270/2024.csv`, `atlas/ohlcv_tradable_by_symbol_year/251/251270/2025.csv`.
- `atlas/symbol_profiles/112/112040.json`, `atlas/ohlcv_tradable_by_symbol_year/112/112040/2021.csv`, `atlas/ohlcv_tradable_by_symbol_year/112/112040/2022.csv`.

External historical context was used only to classify evidence families: Krafton/PUBG/BGMI live-service IP, Netmarble/Solo Leveling: ARISE launch, and Wemade/MIR4-P2E/tokenized IP. Quantitative calibration uses Stock-Web OHLC only.
