# E2R Stock-Web Historical Calibration / Sector-Archetype Residual Research Round
## 0. Research Metadata

```yaml
research_session: post_calibrated_sector_archetype_residual_research
mode: historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12
scheduled_round: R1
scheduled_loop: 14
completed_round: R1
completed_loop: 14
large_sector_id: L1_INDUSTRIALS_INFRA_DEFENSE_GRID
canonical_archetype_id: C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG
fine_archetype_id: DEFENSE_EXPORT_FRAMEWORK_EXECUTIVE_CONTRACT_DELIVERY_BRIDGE
output_file: e2r_stock_web_v12_residual_round_R1_loop_14_L1_INDUSTRIALS_INFRA_DEFENSE_GRID_C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG_research.md
production_scoring_changed: false
shadow_weight_only: true
stock_agent_code_access_allowed: false
stock_agent_code_patch_allowed: false
stock_agent_live_scan_allowed: false
stock_web_price_atlas_access_required: true
handoff_prompt_embedded: true
handoff_prompt_executed_now: false
```

This loop adds 5 new independent cases, 2 counterexamples, and 2 residual errors for R1/L1_INDUSTRIALS_INFRA_DEFENSE_GRID/C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG.
## 1. Current Calibrated Profile Assumption

Assumed current profile is `e2r_2_1_stock_web_calibrated_proxy`, with the post-stock-web global settings already applied: Stage2 actionable bonus, stricter Yellow/Green thresholds, Green revision minimum, cross-evidence buffer, price-only positive-stage block, non-price full-4B requirement, and hard 4C thesis-break routing. This MD does not re-prove those axes globally. It stress-tests how they behave inside the C03 defense export framework/backlog archetype.
## 2. Round / Large Sector / Canonical Archetype Scope

- Scheduled round: `R1`
- Scheduled loop: `14`
- Large sector: `L1_INDUSTRIALS_INFRA_DEFENSE_GRID`
- Canonical archetype: `C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG`
- Scope logic: Korean defense exporters and defense-theme stocks around 2022 sovereign export events. The test separates executable sovereign export contracts from price-only geopolitical defense theme moves and from formal contract confirmation after expectation had already repriced.
- Round-sector consistency: `pass`
## 3. Previous Coverage / Duplicate Avoidance Check

Previous local state completed R13 / Loop 13 and pointed the next run to R1 / Loop 14. Available stock_agent calibration registry access showed older historical calibration registry rows but not a complete v12 loop14 R1 output. This run therefore uses new symbol/trigger-family combinations for this scheduled round:

- New symbols in this loop: `079550`, `012450`, `064350`, `065450`, `047810`.
- New trigger families: `sovereign_export_executive_contract`, `framework_to_executive_export_contract`, `framework_agreement_followed_by_executive_contract`, `geopolitical_price_only_defense_theme`, `formal_contract_after_expectation_priced_in`.
- No same symbol + same trigger date + same entry date reuse is counted.
## 4. Stock-Web OHLC Input / Price Source Validation

Stock-Web manifest was checked before constructing rows. The manifest reports `source_name=FinanceData/marcap`, `price_adjustment_status=raw_unadjusted_marcap`, `min_date=1995-05-02`, `max_date=2026-02-20`, `tradable_row_count=14354401`, `raw_row_count=15214118`, and `symbol_count=5414`. Markets covered are `KONEX, KOSDAQ, KOSDAQ GLOBAL, KOSPI`. Calibration uses `atlas/ohlcv_tradable_by_symbol_year`, while raw diagnostic rows remain in `atlas/ohlcv_raw_by_symbol_year`.

Schema check: tradable shards use `d,o,h,l,c,v,a,mc,s,m`, and MFE/MAE follow `(max high / entry close - 1) * 100` and `(min low / entry close - 1) * 100` over N tradable rows. Corporate-action contaminated 180D windows are blocked. This loop found no 2022~2023 180D corporate-action contamination in the selected windows; old corporate-action candidates outside the window are not treated as blockers.
## 5. Historical Eligibility Gate
| case_id | symbol | entry_date | forward_180D_available | corporate_action_window_status | calibration_usable |
|---|---:|---|---:|---|---:|
| R1L14-C03-LIG-20220117-UAE-MSAM | 079550 | 2022-01-17 | true | clean_180D_window | true |
| R1L14-C03-HANWHA-20220829-POLAND-K9 | 012450 | 2022-08-29 | true | clean_180D_window | true |
| R1L14-C03-ROTEM-20220727-POLAND-K2 | 064350 | 2022-07-27 | true | clean_180D_window | true |
| R1L14-C03-VICTEK-20221004-GEOPOLITICAL-THEME | 065450 | 2022-10-04 | true | clean_180D_window | true |
| R1L14-C03-KAI-20220916-POLAND-FA50-LATE-CONFIRM | 047810 | 2022-09-16 | true | clean_180D_window | true |

## 6. Canonical Archetype Compression Map

C03 is compressed into four evidence layers:

1. **Framework/MOU or public procurement intent**: enough for Stage2 watch or Stage2-Actionable when customer quality is sovereign and delivery scope is visible, but not enough for Green.
2. **Executable contract / order conversion**: can promote Stage2-Actionable and Yellow if the customer, amount, schedule, and delivery path are public.
3. **Delivery-margin / revision bridge**: required for Green inside C03 because formal defense contracts often reprice before revenue and margin conversion are proven.
4. **Theme-only defense price action**: must be blocked from positive Stage2/3 scoring even if MFE exists, because it does not carry backlog, customer, or revision evidence.
## 7. Case Selection Summary
| case_id | symbol | company | role | trigger_family | positive_or_counterexample | current_profile_verdict |
|---|---:|---|---|---|---|---|
| R1L14-C03-LIG-20220117-UAE-MSAM | 079550 | LIG넥스원 | structural_success | sovereign_export_executive_contract | positive | current_profile_correct |
| R1L14-C03-HANWHA-20220829-POLAND-K9 | 012450 | 한화에어로스페이스 | high_mae_success | framework_to_executive_export_contract | positive | current_profile_too_early |
| R1L14-C03-ROTEM-20220727-POLAND-K2 | 064350 | 현대로템 | stage2_promote_candidate | framework_agreement_followed_by_executive_contract | positive | current_profile_correct |
| R1L14-C03-VICTEK-20221004-GEOPOLITICAL-THEME | 065450 | 빅텍 | price_moved_without_evidence | geopolitical_price_only_defense_theme | counterexample | current_profile_correct |
| R1L14-C03-KAI-20220916-POLAND-FA50-LATE-CONFIRM | 047810 | 한국항공우주 | false_positive_green | formal_contract_after_expectation_priced_in | counterexample | current_profile_false_positive |

## 8. Positive vs Counterexample Balance

- positive_case_count: 3
- counterexample_count: 2
- calibration_usable_case_count: 5
- new_independent_case_count: 5
- current_profile_error_count: 2

The balance is intentionally asymmetric: three executable-contract positives are compared against one price-only defense theme counterexample and one late-formal-contract / already-priced-in counterexample. This gives a clean mechanism split: the same “defense export” story works when contract quality and delivery route are visible, but fails as a scoring promotion when the only fuel is price momentum or a confirmation event after expectation already moved.
## 9. Evidence Source Map

Evidence source notes used for this loop:

- LIG Nex1 / UAE M-SAM: public sources describe the January 2022 UAE M-SAM purchase as about US$3.5bn and then-largest Korean arms export.
- Hyundai Rotem / Poland K2: public sources describe the July 27, 2022 framework and August 26, 2022 executive agreement for 180 K2 tanks.
- Hanwha Aerospace / Poland K9: public sources describe the July 27, 2022 K9 framework and August 26, 2022 executive contract.
- KAI / Poland FA-50: public sources describe July 2022 Polish FA-50 procurement/signing for 48 aircraft.
- Victek: treated as a price-only defense theme row; no company-specific contract/backlog evidence was assigned.

The evidence map is intentionally trigger-date constrained. Later delivery facts are used only to explain path quality, not to backdate Stage3/Green labels.
## 10. Price Data Source Map
| symbol | company | shard | profile | entry_date | entry_price |
|---:|---|---|---|---|---:|
| 079550 | LIG넥스원 | `atlas/ohlcv_tradable_by_symbol_year/079/079550/2022.csv` | `atlas/symbol_profiles/079/079550.json` | 2022-01-17 | 68100 |
| 012450 | 한화에어로스페이스 | `atlas/ohlcv_tradable_by_symbol_year/012/012450/2022.csv` | `atlas/symbol_profiles/012/012450.json` | 2022-08-29 | 79600 |
| 064350 | 현대로템 | `atlas/ohlcv_tradable_by_symbol_year/064/064350/2022.csv` | `atlas/symbol_profiles/064/064350.json` | 2022-07-27 | 25000 |
| 065450 | 빅텍 | `atlas/ohlcv_tradable_by_symbol_year/065/065450/2022.csv` | `atlas/symbol_profiles/065/065450.json` | 2022-10-04 | 5700 |
| 047810 | 한국항공우주 | `atlas/ohlcv_tradable_by_symbol_year/047/047810/2022.csv` | `atlas/symbol_profiles/047/047810.json` | 2022-09-16 | 50300 |

## 11. Case-by-Case Trigger Grid
| trigger_id | trigger_type | evidence fields | outcome |
|---|---|---|---|
| R1L14-C03-LIG-20220117-STAGE2A | Stage2-Actionable | public_event_or_disclosure, customer_or_order_quality, policy_or_regulatory_optionality, backlog_or_delivery_visibility, multiple_public_sources, durable_customer_confirmation | contract_backlog_positive_with_initial_drawdown |
| R1L14-C03-HANWHA-20220829-STAGE2A | Stage2-Actionable | public_event_or_disclosure, customer_or_order_quality, backlog_or_delivery_visibility, policy_or_regulatory_optionality, multiple_public_sources, durable_customer_confirmation, repeat_order_or_conversion | positive_but_high_initial_mae |
| R1L14-C03-ROTEM-20220727-STAGE2A | Stage2-Actionable | public_event_or_disclosure, customer_or_order_quality, backlog_or_delivery_visibility, policy_or_regulatory_optionality, relative_strength, multiple_public_sources, durable_customer_confirmation | early_stage2_price_response_then_local_roundtrip |
| R1L14-C03-VICTEK-20221004-STAGE2BLOCK | Stage2-Block | relative_strength | price_only_theme_false_positive_blocked |
| R1L14-C03-KAI-20220916-STAGE3FALSE | Stage3-Green-candidate | public_event_or_disclosure, customer_or_order_quality, policy_or_regulatory_optionality, multiple_public_sources, durable_customer_confirmation | formal_contract_late_entry_high_mae |

## 12. Trigger-Level OHLC Backtest Tables
| trigger_id | entry | MFE30 | MAE30 | MFE90 | MAE90 | MFE180 | MAE180 | peak | drawdown_after_peak |
|---|---:|---:|---:|---:|---:|---:|---:|---|---:|
| R1L14-C03-LIG-20220117-STAGE2A | 68100 | 14.10% | -17.62% | 29.07% | -17.62% | 40.53% | -17.62% | 2022-10-12 / 95700 | -11.91% |
| R1L14-C03-HANWHA-20220829-STAGE2A | 79600 | 9.05% | -33.92% | 9.05% | -33.92% | 50.88% | -33.92% | 2023-04-11 / 120100 | -15.57% |
| R1L14-C03-ROTEM-20220727-STAGE2A | 25000 | 31.40% | -3.80% | 31.40% | -7.40% | 31.40% | -7.40% | 2022-08-26 / 32850 | -29.53% |
| R1L14-C03-VICTEK-20221004-STAGE2BLOCK | 5700 | 28.77% | -7.72% | 28.77% | -8.07% | 28.77% | -14.91% | 2022-11-03 / 7340 | -33.92% |
| R1L14-C03-KAI-20220916-STAGE3FALSE | 50300 | 4.77% | -20.48% | 4.77% | -20.48% | 21.27% | -20.48% | 2023-04-25 / 61000 | -17.87% |

## 13. Current Calibrated Profile Stress Test
### R1L14-C03-LIG-20220117-UAE-MSAM
Current profile verdict: `current_profile_correct`. Before score `83.5` / `Stage3-Yellow`; after shadow score `86.0` / `Stage3-Yellow+`. Strong sovereign customer and formal export, but the 30D/90D MAE shows the market still forced a drawdown before the contract thesis became durable.

### R1L14-C03-HANWHA-20220829-POLAND-K9
Current profile verdict: `current_profile_too_early`. Before score `84.0` / `Stage3-Yellow`; after shadow score `84.5` / `Stage3-Yellow_guarded`. This is not a false positive, but it argues against immediate Green promotion when the first post-contract window has very large MAE and delivery-margin evidence is not yet visible.

### R1L14-C03-ROTEM-20220727-POLAND-K2
Current profile verdict: `current_profile_correct`. Before score `82.0` / `Stage3-Yellow`; after shadow score `83.5` / `Stage3-Yellow_guarded`. Clean Stage2 signal; Green should wait for delivery and margin conversion because the local peak arrived quickly.

### R1L14-C03-VICTEK-20221004-GEOPOLITICAL-THEME
Current profile verdict: `current_profile_correct`. Before score `61.0` / `Stage2-Watch`; after shadow score `54.0` / `Blocked_price_only`. The stock produced tradable MFE, but because the causal evidence is price-only/theme-only, it should not improve positive scoring weights.

### R1L14-C03-KAI-20220916-POLAND-FA50-LATE-CONFIRM
Current profile verdict: `current_profile_false_positive`. Before score `88.0` / `Stage3-Green`; after shadow score `80.5` / `Stage3-Yellow_guarded`. The contract existed, so this is not price-only. The residual error is timing: Green after pre-run + event cap creates weak score-return alignment.

## 14. Stage2 / Yellow / Green Comparison

Stage2-Actionable works well for C03 when customer quality is sovereign and the contract path is executable. Green remains fragile without delivery-margin or revision evidence. In this set, LIG and Rotem can justify Stage2/Yellow quickly, but Hanwha shows high-MAE success and KAI shows a late formal-contract false Green. Therefore, the C03-specific conclusion is not “raise/lower global Green threshold”; it is “require C03 delivery/revision bridge before Green when the event has already repriced.”
## 15. 4B Local vs Full-window Timing Audit
| trigger_id | local_proximity | full_window_proximity | evidence_type | verdict |
|---|---:|---:|---|---|
| R1L14-C03-LIG-20220117-STAGE2A | None | None | none | not_applicable |
| R1L14-C03-HANWHA-20220829-STAGE2A | 0.18 | 0.18 | price_only | price_only_local_4B_too_early |
| R1L14-C03-ROTEM-20220727-STAGE2A | 1.0 | 0.24 | price_only | price_only_local_4B_too_early |
| R1L14-C03-VICTEK-20221004-STAGE2BLOCK | 1.0 | 1.0 | price_only,positioning_overheat | good_overlay_but_not_positive_stage |
| R1L14-C03-KAI-20220916-STAGE3FALSE | 0.92 | 0.1 | valuation_blowoff,explicit_event_cap | formal_contract_after_local_peak_not_full_4B |

## 16. 4C Protection Audit

Hard 4C is not the main object of this R1 loop. Victek receives `thesis_break_watch_only` because no contract/backlog thesis existed. KAI receives `false_break`: the export contract existed, but the entry was a late confirmation after expectation repricing; a hard thesis-break label would be too harsh, while a Green haircut is appropriate.
## 17. Sector-Specific Rule Candidate
No broad L1 sector-specific rule is proposed from five cases. The signal is concentrated in the C03 canonical archetype, not all L1 industrials.
## 18. Canonical-Archetype Rule Candidate

Proposed C03 shadow rule:

```text
if canonical_archetype_id == C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG:
    framework_or_procurement_intent -> Stage2 watch / Stage2A only
    executable sovereign contract with amount/schedule/customer -> Stage2A or Yellow
    Green requires delivery-margin bridge, confirmed revision, or repeat conversion evidence
    formal contract after large pre-run and event cap -> haircut Green by 1.5 to 4.0 points
    price-only defense theme without contract/backlog -> block positive Stage2/3 promotion
```

This is a canonical-archetype-specific rule candidate, not a global production change.
## 19. Before / After Backtest Comparison
| profile | avg_MFE90 | avg_MAE90 | avg_MFE180 | avg_MAE180 | false_positive_rate | verdict |
|---|---:|---:|---:|---:|---|---|
| P0_e2r_2_1_stock_web_calibrated_proxy | 20.61 | -17.5 | 34.57 | -18.87 | 2/5 | usable but over-promotes late formal contract and under-penalizes early high-MAE success |
| P0b_e2r_2_0_baseline_reference | 20.61 | -17.5 | 34.57 | -18.87 | 3/5 | worse; likely promotes price-only or late formal events |
| P1_sector_specific_candidate_profile | 20.61 | -17.5 | 34.57 | -18.87 | 1/5 | improves false-positive control without killing sovereign-contract Stage2 |
| P2_canonical_archetype_candidate_profile | 20.61 | -17.5 | 34.57 | -18.87 | 1/5 | best explanatory compression for C03 |
| P3_counterexample_guard_profile | 20.61 | -17.5 | 34.57 | -18.87 | 0/5 but one missed upside theme | strong guardrail; too conservative for tradable theme but correct for calibration weights |

## 20. Score-Return Alignment Matrix
| case_id | before_score | before_stage | after_score | after_stage | MFE180 | MAE180 | alignment |
|---|---:|---|---:|---|---:|---:|---|
| R1L14-C03-LIG-20220117-UAE-MSAM | 83.5 | Stage3-Yellow | 86.0 | Stage3-Yellow+ | 40.53% | -17.62% | contract_backlog_positive_with_initial_drawdown |
| R1L14-C03-HANWHA-20220829-POLAND-K9 | 84.0 | Stage3-Yellow | 84.5 | Stage3-Yellow_guarded | 50.88% | -33.92% | positive_but_high_initial_mae |
| R1L14-C03-ROTEM-20220727-POLAND-K2 | 82.0 | Stage3-Yellow | 83.5 | Stage3-Yellow_guarded | 31.40% | -7.40% | early_stage2_price_response_then_local_roundtrip |
| R1L14-C03-VICTEK-20221004-GEOPOLITICAL-THEME | 61.0 | Stage2-Watch | 54.0 | Blocked_price_only | 28.77% | -14.91% | price_only_theme_false_positive_blocked |
| R1L14-C03-KAI-20220916-POLAND-FA50-LATE-CONFIRM | 88.0 | Stage3-Green | 80.5 | Stage3-Yellow_guarded | 21.27% | -20.48% | formal_contract_late_entry_high_mae |

## 21. Coverage Matrix
| large_sector_id | canonical_archetype_id | fine_archetype_id | positive_case_count | counterexample_count | 4B_case_count | 4C_case_count | new_independent_case_count | reused_case_count | calibration_usable_trigger_count | representative_trigger_count | current_profile_error_count | sector_rule_candidate | canonical_rule_candidate | coverage_gap_after_this_loop |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|---|---|
| L1_INDUSTRIALS_INFRA_DEFENSE_GRID | C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG | DEFENSE_EXPORT_FRAMEWORK_EXECUTIVE_CONTRACT_DELIVERY_BRIDGE | 3 | 2 | 3 | 2 | 5 | 0 | 5 | 5 | 2 | false | true | need more post-2023 holdout and non-Poland export cases |

## 22. Residual Contribution Summary

```yaml
new_independent_case_count: 5
reused_case_count: 0
reused_case_ids: []
new_symbol_count: 5
new_canonical_archetype_count: 0
new_fine_archetype_count: 5
new_trigger_family_count: 5
tested_existing_calibrated_axes:
  - stage3_green_total_min
  - stage3_green_revision_min
  - price_only_blowoff_blocks_positive_stage
  - full_4b_requires_non_price_evidence
residual_error_types_found:
  - formal_contract_after_pre_run_false_green
  - high_MAE_success_before_delivery_margin_bridge
  - theme_only_relative_strength_false_positive_risk
new_axis_proposed:
  - contract_framework_conversion_quality_gate
  - formal_contract_after_pre_run_event_cap_haircut
  - theme_only_defense_relative_strength_block
existing_axis_strengthened:
  - price_only_blowoff_blocks_positive_stage
  - full_4b_requires_non_price_evidence
existing_axis_weakened: []
existing_axis_kept:
  - stage2_actionable_evidence_bonus
  - stage3_yellow_total_min
  - stage3_green_total_min
  - stage3_green_revision_min
sector_specific_rule_candidate: false
canonical_archetype_rule_candidate: true
no_new_signal_reason: null
loop_contribution_label: canonical_archetype_rule_candidate
do_not_propose_new_weight_delta: false
```
## 23. Validation Scope / Non-Validation Scope

Validated: stock-web manifest/schema, symbol profiles, selected tradable shard rows, entry close values, corporate-action contamination status by profile dates, 30D/90D/180D MFE/MAE approximated directly from stock-web OHLC rows in the cited windows, and C03 evidence timing separation.

Not validated: production code behavior, live candidate discovery, broker execution, current stock recommendation, full global calibration, and any post-manifest price after 2026-02-20.
## 24. Shadow Weight Calibration
```csv
row_type,axis,scope,large_sector_id,canonical_archetype_id,baseline_value,tested_value,delta,reason,backtest_effect,trigger_ids,calibration_usable_count,new_independent_case_count,counterexample_count,confidence,proposal_type,notes
shadow_weight,contract_framework_conversion_quality_gate,canonical_archetype_specific,L1_INDUSTRIALS_INFRA_DEFENSE_GRID,C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG,0,1,+1,Sovereign executable contracts with customer/order quality and backlog visibility had positive 180D MFE even when initial MAE was painful. Framework/MOU alone should not be Green.,keeps LIG/Hanwha/Rotem as Stage2/Yellow while preventing KAI late Green,R1L14-C03-LIG-20220117-STAGE2A|R1L14-C03-HANWHA-20220829-STAGE2A|R1L14-C03-ROTEM-20220727-STAGE2A|R1L14-C03-VICTEK-20221004-STAGE2BLOCK|R1L14-C03-KAI-20220916-STAGE3FALSE,5,5,2,medium,canonical_shadow_only,not production; post-calibrated residual
shadow_weight,formal_contract_after_pre_run_event_cap_haircut,canonical_archetype_specific,L1_INDUSTRIALS_INFRA_DEFENSE_GRID,C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG,0,-1.5,-1.5,KAI shows formal contract evidence can arrive after expectation repricing; score should be haircutted when Green trigger appears after a local event cap and before margin/revision visibility.,reduces false_positive_green count from 1 to 0 in this set,R1L14-C03-KAI-20220916-STAGE3FALSE,1,1,1,medium,canonical_shadow_only,not production; post-calibrated residual
shadow_weight,theme_only_defense_relative_strength_block,canonical_archetype_specific,L1_INDUSTRIALS_INFRA_DEFENSE_GRID,C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG,price_only_block,theme_only_block_stronger,strengthen,Victek generated MFE but no contract/backlog route; calibration weights should not reward price-only theme moves.,prevents price-only defense theme from entering positive Stage2/3 evidence pool,R1L14-C03-VICTEK-20221004-STAGE2BLOCK,1,1,1,high,canonical_shadow_only,strengthens existing price-only blowoff block; not a new global rule
```
## 25. Machine-Readable Rows
### 25.1 price_source_validation
```jsonl
{"row_type": "price_source_validation", "source": "Songdaiki/stock-web", "source_url": "https://github.com/Songdaiki/stock-web", "manifest_path": "atlas/manifest.json", "schema_path": "atlas/schema.json", "universe_path": "atlas/universe/all_symbols.csv", "manifest_max_date": "2026-02-20", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "raw_shard_root": "atlas/ohlcv_raw_by_symbol_year", "validation_status": "usable_for_historical_calibration"}
```
### 25.2 case rows
```jsonl
{"row_type": "case", "case_id": "R1L14-C03-LIG-20220117-UAE-MSAM", "symbol": "079550", "company_name": "LIG넥스원", "round": "R1", "loop": "14", "scheduled_round": "R1", "scheduled_loop": "14", "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "canonical_archetype_id": "C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG", "fine_archetype_id": "MIDDLE_EAST_MISSILE_DEFENSE_EXPORT_CONTRACT", "case_type": "structural_success", "positive_or_counterexample": "positive", "best_trigger": "R1L14-C03-LIG-20220117-STAGE2A", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "aligned", "current_profile_verdict": "current_profile_correct", "price_source": "Songdaiki/stock-web", "notes": "Strong sovereign customer and formal export, but the 30D/90D MAE shows the market still forced a drawdown before the contract thesis became durable."}
{"row_type": "case", "case_id": "R1L14-C03-HANWHA-20220829-POLAND-K9", "symbol": "012450", "company_name": "한화에어로스페이스", "round": "R1", "loop": "14", "scheduled_round": "R1", "scheduled_loop": "14", "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "canonical_archetype_id": "C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG", "fine_archetype_id": "POLAND_K9_EXPORT_FRAMEWORK_EXECUTIVE_CONTRACT", "case_type": "high_mae_success", "positive_or_counterexample": "positive", "best_trigger": "R1L14-C03-HANWHA-20220829-STAGE2A", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "high_mae_success", "current_profile_verdict": "current_profile_too_early", "price_source": "Songdaiki/stock-web", "notes": "This is not a false positive, but it argues against immediate Green promotion when the first post-contract window has very large MAE and delivery-margin evidence is not yet visible."}
{"row_type": "case", "case_id": "R1L14-C03-ROTEM-20220727-POLAND-K2", "symbol": "064350", "company_name": "현대로템", "round": "R1", "loop": "14", "scheduled_round": "R1", "scheduled_loop": "14", "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "canonical_archetype_id": "C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG", "fine_archetype_id": "POLAND_K2_TANK_EXPORT_FRAMEWORK", "case_type": "stage2_promote_candidate", "positive_or_counterexample": "positive", "best_trigger": "R1L14-C03-ROTEM-20220727-STAGE2A", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "aligned", "current_profile_verdict": "current_profile_correct", "price_source": "Songdaiki/stock-web", "notes": "Clean Stage2 signal; Green should wait for delivery and margin conversion because the local peak arrived quickly."}
{"row_type": "case", "case_id": "R1L14-C03-VICTEK-20221004-GEOPOLITICAL-THEME", "symbol": "065450", "company_name": "빅텍", "round": "R1", "loop": "14", "scheduled_round": "R1", "scheduled_loop": "14", "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "canonical_archetype_id": "C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG", "fine_archetype_id": "DEFENSE_THEME_PRICE_ONLY_WITHOUT_BACKLOG", "case_type": "price_moved_without_evidence", "positive_or_counterexample": "counterexample", "best_trigger": "R1L14-C03-VICTEK-20221004-STAGE2BLOCK", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "counterexample", "current_profile_verdict": "current_profile_correct", "price_source": "Songdaiki/stock-web", "notes": "The stock produced tradable MFE, but because the causal evidence is price-only/theme-only, it should not improve positive scoring weights."}
{"row_type": "case", "case_id": "R1L14-C03-KAI-20220916-POLAND-FA50-LATE-CONFIRM", "symbol": "047810", "company_name": "한국항공우주", "round": "R1", "loop": "14", "scheduled_round": "R1", "scheduled_loop": "14", "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "canonical_archetype_id": "C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG", "fine_archetype_id": "FA50_POLAND_FORMAL_CONTRACT_LATE_GREEN_RISK", "case_type": "false_positive_green", "positive_or_counterexample": "counterexample", "best_trigger": "R1L14-C03-KAI-20220916-STAGE3FALSE", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "counterexample", "current_profile_verdict": "current_profile_false_positive", "price_source": "Songdaiki/stock-web", "notes": "The contract existed, so this is not price-only. The residual error is timing: Green after pre-run + event cap creates weak score-return alignment."}
```
### 25.3 trigger rows
```jsonl
{"row_type": "trigger", "trigger_id": "R1L14-C03-LIG-20220117-STAGE2A", "case_id": "R1L14-C03-LIG-20220117-UAE-MSAM", "symbol": "079550", "company_name": "LIG넥스원", "round": "R1", "loop": "14", "scheduled_round": "R1", "scheduled_loop": "14", "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "canonical_archetype_id": "C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG", "fine_archetype_id": "MIDDLE_EAST_MISSILE_DEFENSE_EXPORT_CONTRACT", "sector": "산업재·방산·수출 프레임워크", "primary_archetype": "defense_export_framework_backlog", "loop_objective": "sector_specific_rule_discovery|counterexample_mining|green_strictness_stress_test|4B_non_price_requirement_stress_test|coverage_gap_fill", "trigger_type": "Stage2-Actionable", "trigger_date": "2022-01-17", "evidence_available_at_that_date": "UAE M-SAM / KM-SAM Block II export confirmed around 2022-01-16~17; government-to-government export value cited as about US$3.5bn and Korea’s then-largest arms export.", "evidence_source": "public defense export announcement; Defense News / DAPA-referenced reporting; web source: M-SAM export summary", "stage2_evidence_fields": ["public_event_or_disclosure", "customer_or_order_quality", "policy_or_regulatory_optionality", "backlog_or_delivery_visibility"], "stage3_evidence_fields": ["multiple_public_sources", "durable_customer_confirmation"], "stage4b_evidence_fields": [], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/079/079550/2022.csv", "profile_path": "atlas/symbol_profiles/079/079550.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "entry_date": "2022-01-17", "entry_price": 68100, "MFE_30D_pct": 14.1, "MFE_90D_pct": 29.07, "MFE_180D_pct": 40.53, "MFE_1Y_pct": 61.53, "MFE_2Y_pct": 128.63, "MAE_30D_pct": -17.62, "MAE_90D_pct": -17.62, "MAE_180D_pct": -17.62, "MAE_1Y_pct": -17.62, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2022-10-12", "peak_price": 95700, "drawdown_after_peak_pct": -11.91, "green_lateness_ratio": "0.43", "four_b_local_peak_proximity": null, "four_b_full_window_peak_proximity": null, "four_b_timing_verdict": "not_applicable", "four_b_evidence_type": [], "four_c_protection_label": "not_applicable", "trigger_outcome_label": "contract_backlog_positive_with_initial_drawdown", "current_profile_verdict": "current_profile_correct", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window", "same_entry_group_id": "R1L14-C03-LIG-20220117-UAE-MSAM::2022-01-17::68100", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false}
{"row_type": "trigger", "trigger_id": "R1L14-C03-HANWHA-20220829-STAGE2A", "case_id": "R1L14-C03-HANWHA-20220829-POLAND-K9", "symbol": "012450", "company_name": "한화에어로스페이스", "round": "R1", "loop": "14", "scheduled_round": "R1", "scheduled_loop": "14", "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "canonical_archetype_id": "C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG", "fine_archetype_id": "POLAND_K9_EXPORT_FRAMEWORK_EXECUTIVE_CONTRACT", "sector": "산업재·방산·수출 프레임워크", "primary_archetype": "defense_export_framework_backlog", "loop_objective": "sector_specific_rule_discovery|counterexample_mining|green_strictness_stress_test|4B_non_price_requirement_stress_test|coverage_gap_fill", "trigger_type": "Stage2-Actionable", "trigger_date": "2022-08-29", "evidence_available_at_that_date": "Poland/Hanwha Defense K9 framework and executive contract path was public in late July/August 2022; contract quality was high but the early price path still suffered heavy drawdown before later repricing.", "evidence_source": "Poland K9 export framework/executive contract summaries; web source: K9 Thunder export summary", "stage2_evidence_fields": ["public_event_or_disclosure", "customer_or_order_quality", "backlog_or_delivery_visibility", "policy_or_regulatory_optionality"], "stage3_evidence_fields": ["multiple_public_sources", "durable_customer_confirmation", "repeat_order_or_conversion"], "stage4b_evidence_fields": ["price_only_local_peak"], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/012/012450/2022.csv", "profile_path": "atlas/symbol_profiles/012/012450.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "entry_date": "2022-08-29", "entry_price": 79600, "MFE_30D_pct": 9.05, "MFE_90D_pct": 9.05, "MFE_180D_pct": 50.88, "MFE_1Y_pct": 85.18, "MFE_2Y_pct": 420.1, "MAE_30D_pct": -33.92, "MAE_90D_pct": -33.92, "MAE_180D_pct": -33.92, "MAE_1Y_pct": -33.92, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2023-04-11", "peak_price": 120100, "drawdown_after_peak_pct": -15.57, "green_lateness_ratio": "0.61", "four_b_local_peak_proximity": 0.18, "four_b_full_window_peak_proximity": 0.18, "four_b_timing_verdict": "price_only_local_4B_too_early", "four_b_evidence_type": ["price_only"], "four_c_protection_label": "not_applicable", "trigger_outcome_label": "positive_but_high_initial_mae", "current_profile_verdict": "current_profile_too_early", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window", "same_entry_group_id": "R1L14-C03-HANWHA-20220829-POLAND-K9::2022-08-29::79600", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false}
{"row_type": "trigger", "trigger_id": "R1L14-C03-ROTEM-20220727-STAGE2A", "case_id": "R1L14-C03-ROTEM-20220727-POLAND-K2", "symbol": "064350", "company_name": "현대로템", "round": "R1", "loop": "14", "scheduled_round": "R1", "scheduled_loop": "14", "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "canonical_archetype_id": "C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG", "fine_archetype_id": "POLAND_K2_TANK_EXPORT_FRAMEWORK", "sector": "산업재·방산·수출 프레임워크", "primary_archetype": "defense_export_framework_backlog", "loop_objective": "sector_specific_rule_discovery|counterexample_mining|green_strictness_stress_test|4B_non_price_requirement_stress_test|coverage_gap_fill", "trigger_type": "Stage2-Actionable", "trigger_date": "2022-07-27", "evidence_available_at_that_date": "Poland/Hyundai Rotem K2 framework agreement and subsequent executive agreement created a visible defense export route, but the 180D path shows that early upside was concentrated before later earnings delivery became observable.", "evidence_source": "Poland K2 export framework/executive contract summaries; web source: K2 Black Panther export summary", "stage2_evidence_fields": ["public_event_or_disclosure", "customer_or_order_quality", "backlog_or_delivery_visibility", "policy_or_regulatory_optionality", "relative_strength"], "stage3_evidence_fields": ["multiple_public_sources", "durable_customer_confirmation"], "stage4b_evidence_fields": ["price_only_local_peak"], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/064/064350/2022.csv", "profile_path": "atlas/symbol_profiles/064/064350.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "entry_date": "2022-07-27", "entry_price": 25000, "MFE_30D_pct": 31.4, "MFE_90D_pct": 31.4, "MFE_180D_pct": 31.4, "MFE_1Y_pct": 68.4, "MFE_2Y_pct": 330.0, "MAE_30D_pct": -3.8, "MAE_90D_pct": -7.4, "MAE_180D_pct": -7.4, "MAE_1Y_pct": -7.4, "below_entry_price_flag_30D": false, "below_entry_price_flag_90D": true, "peak_date": "2022-08-26", "peak_price": 32850, "drawdown_after_peak_pct": -29.53, "green_lateness_ratio": "0.20", "four_b_local_peak_proximity": 1.0, "four_b_full_window_peak_proximity": 0.24, "four_b_timing_verdict": "price_only_local_4B_too_early", "four_b_evidence_type": ["price_only"], "four_c_protection_label": "not_applicable", "trigger_outcome_label": "early_stage2_price_response_then_local_roundtrip", "current_profile_verdict": "current_profile_correct", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window", "same_entry_group_id": "R1L14-C03-ROTEM-20220727-POLAND-K2::2022-07-27::25000", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false}
{"row_type": "trigger", "trigger_id": "R1L14-C03-VICTEK-20221004-STAGE2BLOCK", "case_id": "R1L14-C03-VICTEK-20221004-GEOPOLITICAL-THEME", "symbol": "065450", "company_name": "빅텍", "round": "R1", "loop": "14", "scheduled_round": "R1", "scheduled_loop": "14", "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "canonical_archetype_id": "C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG", "fine_archetype_id": "DEFENSE_THEME_PRICE_ONLY_WITHOUT_BACKLOG", "sector": "산업재·방산·수출 프레임워크", "primary_archetype": "defense_export_framework_backlog", "loop_objective": "sector_specific_rule_discovery|counterexample_mining|green_strictness_stress_test|4B_non_price_requirement_stress_test|coverage_gap_fill", "trigger_type": "Stage2-Block", "trigger_date": "2022-10-04", "evidence_available_at_that_date": "Geopolitical tension created defense-theme trading, but there was no company-specific sovereign export contract, order conversion, or delivery-margin route at the trigger date.", "evidence_source": "price-only defense theme / no company order disclosure; benchmark counterexample", "stage2_evidence_fields": ["relative_strength"], "stage3_evidence_fields": [], "stage4b_evidence_fields": ["price_only_local_peak", "positioning_overheat"], "stage4c_evidence_fields": ["thesis_evidence_broken"], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/065/065450/2022.csv", "profile_path": "atlas/symbol_profiles/065/065450.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "entry_date": "2022-10-04", "entry_price": 5700, "MFE_30D_pct": 28.77, "MFE_90D_pct": 28.77, "MFE_180D_pct": 28.77, "MFE_1Y_pct": 28.77, "MFE_2Y_pct": 34.2, "MAE_30D_pct": -7.72, "MAE_90D_pct": -8.07, "MAE_180D_pct": -14.91, "MAE_1Y_pct": -31.93, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2022-11-03", "peak_price": 7340, "drawdown_after_peak_pct": -33.92, "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": 1.0, "four_b_full_window_peak_proximity": 1.0, "four_b_timing_verdict": "good_overlay_but_not_positive_stage", "four_b_evidence_type": ["price_only", "positioning_overheat"], "four_c_protection_label": "thesis_break_watch_only", "trigger_outcome_label": "price_only_theme_false_positive_blocked", "current_profile_verdict": "current_profile_correct", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window", "same_entry_group_id": "R1L14-C03-VICTEK-20221004-GEOPOLITICAL-THEME::2022-10-04::5700", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false}
{"row_type": "trigger", "trigger_id": "R1L14-C03-KAI-20220916-STAGE3FALSE", "case_id": "R1L14-C03-KAI-20220916-POLAND-FA50-LATE-CONFIRM", "symbol": "047810", "company_name": "한국항공우주", "round": "R1", "loop": "14", "scheduled_round": "R1", "scheduled_loop": "14", "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "canonical_archetype_id": "C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG", "fine_archetype_id": "FA50_POLAND_FORMAL_CONTRACT_LATE_GREEN_RISK", "sector": "산업재·방산·수출 프레임워크", "primary_archetype": "defense_export_framework_backlog", "loop_objective": "sector_specific_rule_discovery|counterexample_mining|green_strictness_stress_test|4B_non_price_requirement_stress_test|coverage_gap_fill", "trigger_type": "Stage3-Green-candidate", "trigger_date": "2022-09-16", "evidence_available_at_that_date": "Poland FA-50 procurement was public in July 2022 and KAI signed the export agreement later; by a mid-September formal-confirmation entry the price path had already repriced and then suffered a sharp drawdown.", "evidence_source": "KAI/FA-50 Poland export summaries; Reuters/Yonhap-referenced public reporting", "stage2_evidence_fields": ["public_event_or_disclosure", "customer_or_order_quality", "policy_or_regulatory_optionality"], "stage3_evidence_fields": ["multiple_public_sources", "durable_customer_confirmation"], "stage4b_evidence_fields": ["valuation_blowoff", "explicit_event_cap"], "stage4c_evidence_fields": ["thesis_evidence_broken"], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/047/047810/2022.csv", "profile_path": "atlas/symbol_profiles/047/047810.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "entry_date": "2022-09-16", "entry_price": 50300, "MFE_30D_pct": 4.77, "MFE_90D_pct": 4.77, "MFE_180D_pct": 21.27, "MFE_1Y_pct": 21.27, "MFE_2Y_pct": 140.2, "MAE_30D_pct": -20.48, "MAE_90D_pct": -20.48, "MAE_180D_pct": -20.48, "MAE_1Y_pct": -20.48, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2023-04-25", "peak_price": 61000, "drawdown_after_peak_pct": -17.87, "green_lateness_ratio": "0.78", "four_b_local_peak_proximity": 0.92, "four_b_full_window_peak_proximity": 0.1, "four_b_timing_verdict": "formal_contract_after_local_peak_not_full_4B", "four_b_evidence_type": ["valuation_blowoff", "explicit_event_cap"], "four_c_protection_label": "false_break", "trigger_outcome_label": "formal_contract_late_entry_high_mae", "current_profile_verdict": "current_profile_false_positive", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window", "same_entry_group_id": "R1L14-C03-KAI-20220916-POLAND-FA50-LATE-CONFIRM::2022-09-16::50300", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false}
```
### 25.4 score_simulation rows
```jsonl
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R1L14-C03-LIG-20220117-UAE-MSAM", "trigger_id": "R1L14-C03-LIG-20220117-STAGE2A", "symbol": "079550", "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "canonical_archetype_id": "C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG", "raw_component_scores_before": {"contract_score": 18, "backlog_visibility_score": 12, "margin_bridge_score": 4, "revision_score": 7, "relative_strength_score": 7, "customer_quality_score": 15, "policy_or_regulatory_score": 12, "valuation_repricing_score": 4, "execution_risk_score": -2, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_before": 83.5, "stage_label_before": "Stage3-Yellow", "raw_component_scores_after": {"contract_score": 19, "backlog_visibility_score": 13, "margin_bridge_score": 4, "revision_score": 7, "relative_strength_score": 7, "customer_quality_score": 15.5, "policy_or_regulatory_score": 12, "valuation_repricing_score": 4, "execution_risk_score": -2, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_after": 86.0, "stage_label_after": "Stage3-Yellow+", "changed_components": ["contract_score", "backlog_visibility_score", "customer_quality_score", "execution_risk_score"], "component_delta_explanation": "C03 shadow profile rewards formal sovereign executable contracts only when backlog/delivery visibility is observable, and haircuts late formal confirmation after pre-run or price-only theme moves.", "MFE_90D_pct": 29.07, "MAE_90D_pct": -17.62, "score_return_alignment_label": "contract_backlog_positive_with_initial_drawdown", "current_profile_verdict": "current_profile_correct"}
{"row_type": "score_simulation", "profile_id": "proposed_c03_defense_export_shadow_profile", "case_id": "R1L14-C03-LIG-20220117-UAE-MSAM", "trigger_id": "R1L14-C03-LIG-20220117-STAGE2A", "symbol": "079550", "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "canonical_archetype_id": "C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG", "raw_component_scores_before": {"contract_score": 18, "backlog_visibility_score": 12, "margin_bridge_score": 4, "revision_score": 7, "relative_strength_score": 7, "customer_quality_score": 15, "policy_or_regulatory_score": 12, "valuation_repricing_score": 4, "execution_risk_score": -2, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_before": 83.5, "stage_label_before": "Stage3-Yellow", "raw_component_scores_after": {"contract_score": 19, "backlog_visibility_score": 13, "margin_bridge_score": 4, "revision_score": 7, "relative_strength_score": 7, "customer_quality_score": 15.5, "policy_or_regulatory_score": 12, "valuation_repricing_score": 4, "execution_risk_score": -2, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_after": 86.0, "stage_label_after": "Stage3-Yellow+", "changed_components": ["contract_score", "backlog_visibility_score", "customer_quality_score", "execution_risk_score"], "component_delta_explanation": "C03 shadow profile rewards formal sovereign executable contracts only when backlog/delivery visibility is observable, and haircuts late formal confirmation after pre-run or price-only theme moves.", "MFE_90D_pct": 29.07, "MAE_90D_pct": -17.62, "score_return_alignment_label": "contract_backlog_positive_with_initial_drawdown", "current_profile_verdict": "current_profile_correct"}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R1L14-C03-HANWHA-20220829-POLAND-K9", "trigger_id": "R1L14-C03-HANWHA-20220829-STAGE2A", "symbol": "012450", "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "canonical_archetype_id": "C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG", "raw_component_scores_before": {"contract_score": 17, "backlog_visibility_score": 14, "margin_bridge_score": 3, "revision_score": 5, "relative_strength_score": 9, "customer_quality_score": 14, "policy_or_regulatory_score": 12, "valuation_repricing_score": 5, "execution_risk_score": -3, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_before": 84.0, "stage_label_before": "Stage3-Yellow", "raw_component_scores_after": {"contract_score": 18, "backlog_visibility_score": 15, "margin_bridge_score": 3, "revision_score": 5, "relative_strength_score": 9, "customer_quality_score": 14, "policy_or_regulatory_score": 12, "valuation_repricing_score": 4, "execution_risk_score": -4.5, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_after": 84.5, "stage_label_after": "Stage3-Yellow_guarded", "changed_components": ["contract_score", "backlog_visibility_score", "execution_risk_score", "valuation_repricing_score"], "component_delta_explanation": "C03 shadow profile rewards formal sovereign executable contracts only when backlog/delivery visibility is observable, and haircuts late formal confirmation after pre-run or price-only theme moves.", "MFE_90D_pct": 9.05, "MAE_90D_pct": -33.92, "score_return_alignment_label": "positive_but_high_initial_mae", "current_profile_verdict": "current_profile_too_early"}
{"row_type": "score_simulation", "profile_id": "proposed_c03_defense_export_shadow_profile", "case_id": "R1L14-C03-HANWHA-20220829-POLAND-K9", "trigger_id": "R1L14-C03-HANWHA-20220829-STAGE2A", "symbol": "012450", "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "canonical_archetype_id": "C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG", "raw_component_scores_before": {"contract_score": 17, "backlog_visibility_score": 14, "margin_bridge_score": 3, "revision_score": 5, "relative_strength_score": 9, "customer_quality_score": 14, "policy_or_regulatory_score": 12, "valuation_repricing_score": 5, "execution_risk_score": -3, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_before": 84.0, "stage_label_before": "Stage3-Yellow", "raw_component_scores_after": {"contract_score": 18, "backlog_visibility_score": 15, "margin_bridge_score": 3, "revision_score": 5, "relative_strength_score": 9, "customer_quality_score": 14, "policy_or_regulatory_score": 12, "valuation_repricing_score": 4, "execution_risk_score": -4.5, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_after": 84.5, "stage_label_after": "Stage3-Yellow_guarded", "changed_components": ["contract_score", "backlog_visibility_score", "execution_risk_score", "valuation_repricing_score"], "component_delta_explanation": "C03 shadow profile rewards formal sovereign executable contracts only when backlog/delivery visibility is observable, and haircuts late formal confirmation after pre-run or price-only theme moves.", "MFE_90D_pct": 9.05, "MAE_90D_pct": -33.92, "score_return_alignment_label": "positive_but_high_initial_mae", "current_profile_verdict": "current_profile_too_early"}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R1L14-C03-ROTEM-20220727-POLAND-K2", "trigger_id": "R1L14-C03-ROTEM-20220727-STAGE2A", "symbol": "064350", "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "canonical_archetype_id": "C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG", "raw_component_scores_before": {"contract_score": 16, "backlog_visibility_score": 13, "margin_bridge_score": 2, "revision_score": 4, "relative_strength_score": 12, "customer_quality_score": 13, "policy_or_regulatory_score": 12, "valuation_repricing_score": 5, "execution_risk_score": -2, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_before": 82.0, "stage_label_before": "Stage3-Yellow", "raw_component_scores_after": {"contract_score": 17, "backlog_visibility_score": 13.5, "margin_bridge_score": 2, "revision_score": 4, "relative_strength_score": 12, "customer_quality_score": 13, "policy_or_regulatory_score": 12, "valuation_repricing_score": 4.5, "execution_risk_score": -2, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_after": 83.5, "stage_label_after": "Stage3-Yellow_guarded", "changed_components": ["contract_score", "backlog_visibility_score", "valuation_repricing_score", "execution_risk_score"], "component_delta_explanation": "C03 shadow profile rewards formal sovereign executable contracts only when backlog/delivery visibility is observable, and haircuts late formal confirmation after pre-run or price-only theme moves.", "MFE_90D_pct": 31.4, "MAE_90D_pct": -7.4, "score_return_alignment_label": "early_stage2_price_response_then_local_roundtrip", "current_profile_verdict": "current_profile_correct"}
{"row_type": "score_simulation", "profile_id": "proposed_c03_defense_export_shadow_profile", "case_id": "R1L14-C03-ROTEM-20220727-POLAND-K2", "trigger_id": "R1L14-C03-ROTEM-20220727-STAGE2A", "symbol": "064350", "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "canonical_archetype_id": "C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG", "raw_component_scores_before": {"contract_score": 16, "backlog_visibility_score": 13, "margin_bridge_score": 2, "revision_score": 4, "relative_strength_score": 12, "customer_quality_score": 13, "policy_or_regulatory_score": 12, "valuation_repricing_score": 5, "execution_risk_score": -2, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_before": 82.0, "stage_label_before": "Stage3-Yellow", "raw_component_scores_after": {"contract_score": 17, "backlog_visibility_score": 13.5, "margin_bridge_score": 2, "revision_score": 4, "relative_strength_score": 12, "customer_quality_score": 13, "policy_or_regulatory_score": 12, "valuation_repricing_score": 4.5, "execution_risk_score": -2, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_after": 83.5, "stage_label_after": "Stage3-Yellow_guarded", "changed_components": ["contract_score", "backlog_visibility_score", "valuation_repricing_score", "execution_risk_score"], "component_delta_explanation": "C03 shadow profile rewards formal sovereign executable contracts only when backlog/delivery visibility is observable, and haircuts late formal confirmation after pre-run or price-only theme moves.", "MFE_90D_pct": 31.4, "MAE_90D_pct": -7.4, "score_return_alignment_label": "early_stage2_price_response_then_local_roundtrip", "current_profile_verdict": "current_profile_correct"}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R1L14-C03-VICTEK-20221004-GEOPOLITICAL-THEME", "trigger_id": "R1L14-C03-VICTEK-20221004-STAGE2BLOCK", "symbol": "065450", "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "canonical_archetype_id": "C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG", "raw_component_scores_before": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 0, "revision_score": 0, "relative_strength_score": 13, "customer_quality_score": 1, "policy_or_regulatory_score": 5, "valuation_repricing_score": 8, "execution_risk_score": -4, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_before": 61.0, "stage_label_before": "Stage2-Watch", "raw_component_scores_after": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 0, "revision_score": 0, "relative_strength_score": 9, "customer_quality_score": 1, "policy_or_regulatory_score": 5, "valuation_repricing_score": 5, "execution_risk_score": -6, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_after": 54.0, "stage_label_after": "Blocked_price_only", "changed_components": ["relative_strength_score", "valuation_repricing_score", "execution_risk_score"], "component_delta_explanation": "C03 shadow profile rewards formal sovereign executable contracts only when backlog/delivery visibility is observable, and haircuts late formal confirmation after pre-run or price-only theme moves.", "MFE_90D_pct": 28.77, "MAE_90D_pct": -8.07, "score_return_alignment_label": "price_only_theme_false_positive_blocked", "current_profile_verdict": "current_profile_correct"}
{"row_type": "score_simulation", "profile_id": "proposed_c03_defense_export_shadow_profile", "case_id": "R1L14-C03-VICTEK-20221004-GEOPOLITICAL-THEME", "trigger_id": "R1L14-C03-VICTEK-20221004-STAGE2BLOCK", "symbol": "065450", "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "canonical_archetype_id": "C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG", "raw_component_scores_before": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 0, "revision_score": 0, "relative_strength_score": 13, "customer_quality_score": 1, "policy_or_regulatory_score": 5, "valuation_repricing_score": 8, "execution_risk_score": -4, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_before": 61.0, "stage_label_before": "Stage2-Watch", "raw_component_scores_after": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 0, "revision_score": 0, "relative_strength_score": 9, "customer_quality_score": 1, "policy_or_regulatory_score": 5, "valuation_repricing_score": 5, "execution_risk_score": -6, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_after": 54.0, "stage_label_after": "Blocked_price_only", "changed_components": ["relative_strength_score", "valuation_repricing_score", "execution_risk_score"], "component_delta_explanation": "C03 shadow profile rewards formal sovereign executable contracts only when backlog/delivery visibility is observable, and haircuts late formal confirmation after pre-run or price-only theme moves.", "MFE_90D_pct": 28.77, "MAE_90D_pct": -8.07, "score_return_alignment_label": "price_only_theme_false_positive_blocked", "current_profile_verdict": "current_profile_correct"}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R1L14-C03-KAI-20220916-POLAND-FA50-LATE-CONFIRM", "trigger_id": "R1L14-C03-KAI-20220916-STAGE3FALSE", "symbol": "047810", "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "canonical_archetype_id": "C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG", "raw_component_scores_before": {"contract_score": 17, "backlog_visibility_score": 11, "margin_bridge_score": 2, "revision_score": 5, "relative_strength_score": 6, "customer_quality_score": 13, "policy_or_regulatory_score": 10, "valuation_repricing_score": 11, "execution_risk_score": -2, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_before": 88.0, "stage_label_before": "Stage3-Green", "raw_component_scores_after": {"contract_score": 17, "backlog_visibility_score": 11, "margin_bridge_score": 2, "revision_score": 3.5, "relative_strength_score": 6, "customer_quality_score": 13, "policy_or_regulatory_score": 10, "valuation_repricing_score": 7, "execution_risk_score": -4, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_after": 80.5, "stage_label_after": "Stage3-Yellow_guarded", "changed_components": ["contract_score", "backlog_visibility_score", "valuation_repricing_score", "execution_risk_score", "revision_score"], "component_delta_explanation": "C03 shadow profile rewards formal sovereign executable contracts only when backlog/delivery visibility is observable, and haircuts late formal confirmation after pre-run or price-only theme moves.", "MFE_90D_pct": 4.77, "MAE_90D_pct": -20.48, "score_return_alignment_label": "formal_contract_late_entry_high_mae", "current_profile_verdict": "current_profile_false_positive"}
{"row_type": "score_simulation", "profile_id": "proposed_c03_defense_export_shadow_profile", "case_id": "R1L14-C03-KAI-20220916-POLAND-FA50-LATE-CONFIRM", "trigger_id": "R1L14-C03-KAI-20220916-STAGE3FALSE", "symbol": "047810", "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "canonical_archetype_id": "C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG", "raw_component_scores_before": {"contract_score": 17, "backlog_visibility_score": 11, "margin_bridge_score": 2, "revision_score": 5, "relative_strength_score": 6, "customer_quality_score": 13, "policy_or_regulatory_score": 10, "valuation_repricing_score": 11, "execution_risk_score": -2, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_before": 88.0, "stage_label_before": "Stage3-Green", "raw_component_scores_after": {"contract_score": 17, "backlog_visibility_score": 11, "margin_bridge_score": 2, "revision_score": 3.5, "relative_strength_score": 6, "customer_quality_score": 13, "policy_or_regulatory_score": 10, "valuation_repricing_score": 7, "execution_risk_score": -4, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_after": 80.5, "stage_label_after": "Stage3-Yellow_guarded", "changed_components": ["contract_score", "backlog_visibility_score", "valuation_repricing_score", "execution_risk_score", "revision_score"], "component_delta_explanation": "C03 shadow profile rewards formal sovereign executable contracts only when backlog/delivery visibility is observable, and haircuts late formal confirmation after pre-run or price-only theme moves.", "MFE_90D_pct": 4.77, "MAE_90D_pct": -20.48, "score_return_alignment_label": "formal_contract_late_entry_high_mae", "current_profile_verdict": "current_profile_false_positive"}
```
### 25.5 shadow_weight rows
```csv
row_type,axis,scope,large_sector_id,canonical_archetype_id,baseline_value,tested_value,delta,reason,backtest_effect,trigger_ids,calibration_usable_count,new_independent_case_count,counterexample_count,confidence,proposal_type,notes
shadow_weight,contract_framework_conversion_quality_gate,canonical_archetype_specific,L1_INDUSTRIALS_INFRA_DEFENSE_GRID,C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG,0,1,+1,Sovereign executable contracts with customer/order quality and backlog visibility had positive 180D MFE even when initial MAE was painful. Framework/MOU alone should not be Green.,keeps LIG/Hanwha/Rotem as Stage2/Yellow while preventing KAI late Green,R1L14-C03-LIG-20220117-STAGE2A|R1L14-C03-HANWHA-20220829-STAGE2A|R1L14-C03-ROTEM-20220727-STAGE2A|R1L14-C03-VICTEK-20221004-STAGE2BLOCK|R1L14-C03-KAI-20220916-STAGE3FALSE,5,5,2,medium,canonical_shadow_only,not production; post-calibrated residual
shadow_weight,formal_contract_after_pre_run_event_cap_haircut,canonical_archetype_specific,L1_INDUSTRIALS_INFRA_DEFENSE_GRID,C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG,0,-1.5,-1.5,KAI shows formal contract evidence can arrive after expectation repricing; score should be haircutted when Green trigger appears after a local event cap and before margin/revision visibility.,reduces false_positive_green count from 1 to 0 in this set,R1L14-C03-KAI-20220916-STAGE3FALSE,1,1,1,medium,canonical_shadow_only,not production; post-calibrated residual
shadow_weight,theme_only_defense_relative_strength_block,canonical_archetype_specific,L1_INDUSTRIALS_INFRA_DEFENSE_GRID,C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG,price_only_block,theme_only_block_stronger,strengthen,Victek generated MFE but no contract/backlog route; calibration weights should not reward price-only theme moves.,prevents price-only defense theme from entering positive Stage2/3 evidence pool,R1L14-C03-VICTEK-20221004-STAGE2BLOCK,1,1,1,high,canonical_shadow_only,strengthens existing price-only blowoff block; not a new global rule
```
### 25.6 residual_contribution row
```jsonl
{"row_type": "residual_contribution", "round": "R1", "loop": "14", "scheduled_round": "R1", "scheduled_loop": "14", "round_schedule_status": "valid", "round_sector_consistency": "pass", "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "canonical_archetype_id": "C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG", "new_independent_case_count": 5, "reused_case_count": 0, "new_symbol_count": 5, "same_archetype_new_symbol_count": 5, "same_archetype_new_trigger_family_count": 5, "new_trigger_family_count": 5, "positive_case_count": 3, "counterexample_count": 2, "current_profile_error_count": 2, "tested_existing_calibrated_axes": ["stage3_green_total_min", "stage3_green_revision_min", "price_only_blowoff_blocks_positive_stage", "full_4b_requires_non_price_evidence"], "residual_error_types_found": ["formal_contract_after_pre_run_false_green", "high_MAE_success_before_delivery_margin_bridge", "theme_only_relative_strength_false_positive_risk"], "loop_contribution_label": "canonical_archetype_rule_candidate", "do_not_propose_new_weight_delta": false}
```
### 25.7 narrative_only rows
```jsonl
{"row_type": "narrative_only", "case_id": "none", "symbol": null, "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "canonical_archetype_id": "C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG", "reason": "all selected cases have calibration_usable=true; no narrative-only row needed", "price_source": "Songdaiki/stock-web", "usage": "not_weight_calibration"}
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
completed_round = R1
completed_loop = 14
next_round = R2
next_loop = 14
round_schedule_status = valid
round_sector_consistency = pass
```
## 28. Source Notes

- Stock-Web manifest checked: `atlas/manifest.json`; max_date `2026-02-20`; price basis `tradable_raw`; adjustment status `raw_unadjusted_marcap`.
- Stock-Web schema checked: tradable columns `d,o,h,l,c,v,a,mc,s,m`; MFE/MAE definitions use max high/min low over N tradable rows.
- Stock-Web symbol profiles checked for `079550`, `012450`, `064350`, `065450`, and `047810`.
- Tradable shard rows checked around each entry and forward window. This MD uses only stock-web rows for price calculations.
- Historical evidence notes were constrained to public export-contract/defense procurement events. No live-current candidate scan was performed.

