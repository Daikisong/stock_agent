# E2R Stock-Web Historical Calibration / Sector-Archetype Residual Research Round

## 0. Research Metadata

```text
research_session = post_calibrated_sector_archetype_residual_research
mode = historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12
round = R1
loop = 11
sector = 산업재·수주·인프라
large_sector_id = L1_INDUSTRIALS_INFRA_DEFENSE_GRID
canonical_archetype_id = C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY
fine_archetype_id = CZECH_NUCLEAR_PREFERRED_BIDDER_LEGAL_APPEAL_DIRECT_SUPPLIER_VS_EPC_BETA
loop_objective = counterexample_mining | residual_false_positive_mining | 4B_non_price_requirement_stress_test | 4C_thesis_break_timing_test | sector_specific_rule_discovery | canonical_archetype_compression | coverage_gap_fill
output_file = e2r_stock_web_v12_residual_round_R1_loop_11_L1_INDUSTRIALS_INFRA_DEFENSE_GRID_C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY_research.md
production_scoring_changed = false
shadow_weight_only = true
stock_agent_code_access_allowed = false
stock_agent_code_patch_allowed = false
stock_web_price_atlas_access_required = true
```

This MD is a historical calibration artifact, not current/live stock discovery and not investment advice.

## 1. Current Calibrated Profile Assumption

Current profile proxy:

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

The already-applied calibration covered R1~R13 and loops 1~9, with 1,940 validated trigger rows and 1,376 representative aggregate trigger rows. The global axes are therefore treated as already applied, not re-proposed. fileciteturn107file0 The applied global changes include Stage2 actionable bonus, stricter Green, stronger revision requirement, non-price 4B requirement, and hard 4C thesis-break routing. fileciteturn108file0

## 2. Round / Large Sector / Canonical Archetype Scope

| field | value |
|---|---|
| round | R1 |
| loop | 11 |
| large_sector_id | L1_INDUSTRIALS_INFRA_DEFENSE_GRID |
| canonical_archetype_id | C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY |
| fine_archetype_id | CZECH_NUCLEAR_PREFERRED_BIDDER_LEGAL_APPEAL_DIRECT_SUPPLIER_VS_EPC_BETA |
| scope | Czech nuclear preferred-bidder policy event, legal appeal watch, direct supplier vs EPC beta split |
| rule scope target | canonical_archetype_specific first; sector_specific second |

## 3. Previous Coverage / Duplicate Avoidance Check

Accessible stock_agent artifact search did not return a direct prior C04/Czech-nuclear residual row for the specific 2024-07-17 KHNP preferred-bidder trigger set in this loop. The loop therefore treats all four symbols as new independent cases for this C04 research file.

Diversity gate:

```text
new_independent_case_count = 4
reused_case_count = 0
new_symbol_count = 4
same_archetype_new_symbol_count = 4
same_archetype_new_trigger_family_count = 2
minimum_new_independent_case_ratio = 1.00
duplicate_low_value_loop = false
schema_rematerialization_only = false
```

## 4. Stock-Web OHLC Input / Price Source Validation

Stock-Web manifest fields used in this loop:

| field | value |
|---|---|
| source_name | FinanceData/marcap |
| price_adjustment_status | raw_unadjusted_marcap |
| min_date | 1995-05-02 |
| max_date | 2026-02-20 |
| tradable_row_count | 14,354,401 |
| raw_row_count | 15,214,118 |
| symbol_count | 5,414 |
| active_like_symbol_count | 2,868 |
| inactive_or_delisted_like_symbol_count | 2,546 |
| markets | KONEX, KOSDAQ, KOSDAQ GLOBAL, KOSPI |
| calibration_shard_root | atlas/ohlcv_tradable_by_symbol_year |
| raw_shard_root | atlas/ohlcv_raw_by_symbol_year |
| schema_path | atlas/schema.json |
| universe_path | atlas/universe/all_symbols.csv |

The manifest states raw/unadjusted OHLC, excludes zero-volume and invalid OHLC rows from calibration shards, and blocks corporate-action-contaminated windows by default. fileciteturn109file0 The schema defines tradable columns `d/o/h/l/c/v/a/mc/s/m`, raw columns including `rs`, and MFE/MAE as max high/min low from entry through N tradable rows. fileciteturn110file0

## 5. Historical Eligibility Gate

| symbol | company | profile caveat | 180D forward window | corporate action overlap in 2024-07-18~D+180 | calibration usable |
|---|---|---:|---:|---:|---:|
| 034020 | 두산에너빌리티 | old corporate-action candidates only, no 2024 overlap | available | clean | true |
| 052690 | 한전기술 | none | available | clean | true |
| 083650 | 비에이치아이 | old corporate-action candidates only, no 2024 overlap | available | clean | true |
| 000720 | 현대건설 | old corporate-action candidates only, no 2024 overlap | available | clean | true |

Profiles used: 두산에너빌리티 fileciteturn126file0, 한전기술 fileciteturn127file0, 비에이치아이 fileciteturn128file0, 현대건설 fileciteturn135file0.

## 6. Canonical Archetype Compression Map

| fine route | canonical compression | reason |
|---|---|---|
| Czech preferred bidder direct supplier | C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY | policy project route with contract/legal completion risk |
| Nuclear engineering direct route | C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY | design/engineering beneficiary but contract timing still gates Green |
| Small-cap auxiliary nuclear supplier | C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY | policy project path plus delayed order/revision conversion |
| Construction EPC beta | C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY, with C30 spillover note | headline beneficiary can be dominated by construction margin/PF cycle |

## 7. Case Selection Summary

| case_id | symbol | company | role | trigger | entry | entry_price | current_profile_verdict |
|---|---:|---|---|---|---:|---:|---|
| R1L11_C04_034020_CZ_NUCLEAR_DIRECT_SUPPLIER | 034020 | 두산에너빌리티 | high_mae_success | KHNP preferred bidder | 2024-07-18 | 21,000 | current_profile_too_early |
| R1L11_C04_052690_CZ_NUCLEAR_ENGINEERING_DIRECT | 052690 | 한전기술 | high_mae_success | KHNP preferred bidder | 2024-07-18 | 82,000 | current_profile_too_early |
| R1L11_C04_083650_CZ_NUCLEAR_AUXILIARY_SUPPLIER | 083650 | 비에이치아이 | structural_success | KHNP preferred bidder | 2024-07-18 | 8,810 | current_profile_correct |
| R1L11_C04_000720_CZ_NUCLEAR_EPC_BETA_FALSE_GREEN | 000720 | 현대건설 | failed_rerating | KHNP preferred bidder | 2024-07-18 | 33,400 | current_profile_false_positive |

## 8. Positive vs Counterexample Balance

```text
positive_case_count = 3
counterexample_count = 1
4B_case_count = 3
4C_case_count = 2 watch-only / false-break
calibration_usable_case_count = 4
calibration_usable_trigger_count = 4
```

The loop is not trying to prove “nuclear policy good.” It separates the mechanical chain:

```text
policy/project selection
→ direct supplier/engineering exposure
→ legal appeal and contract signing risk
→ actual margin/revision/order conversion
→ price path
```

The useful signal is not the policy headline itself. The useful signal is whether the policy headline can be bridged into direct scope, customer quality, contract timing, and revision.

## 9. Evidence Source Map

Primary public evidence:

| date | event | use in calibration |
|---|---|---|
| 2024-07-17 | Czech government selected KHNP as preferred bidder for two Dukovany units, potentially with additional Temelín option; Reuters noted each unit around 200bn crowns and contract details to be finalized later. | Stage2-Actionable policy/project trigger, not automatic Green. citeturn118157news1 |
| 2024-07-17 | Reuters also framed the event as South Korea's first major nuclear export win since 2009 and noted stock gains in related Korean companies. | Relative-strength / policy optionality support, but still not full Stage3-Green. citeturn118157news0 |
| 2024-08-27 to 2024-09-03 | EDF and Westinghouse appealed the Czech tender decision; UOHS began reviewing appeals. | 4B/4C watch overlay; not hard 4C without contract cancellation or license failure. citeturn872724news2turn872724news0 |
| 2024-10-30 | Czech watchdog temporarily prohibited final contract signing while appeals proceeded. | Legal/regulatory block overlay; not full thesis break by itself. citeturn872724news1 |
| 2025-05-06 | Czech court temporarily halted KHNP signing after EDF complaint. | Out-of-window legal-delay validation: confirms why C04 Green needs legal/contract bridge. citeturn118157news2 |

## 10. Price Data Source Map

| symbol | profile_path | 2024 shard | 2025 shard |
|---:|---|---|---|
| 034020 | atlas/symbol_profiles/034/034020.json | atlas/ohlcv_tradable_by_symbol_year/034/034020/2024.csv | atlas/ohlcv_tradable_by_symbol_year/034/034020/2025.csv |
| 052690 | atlas/symbol_profiles/052/052690.json | atlas/ohlcv_tradable_by_symbol_year/052/052690/2024.csv | atlas/ohlcv_tradable_by_symbol_year/052/052690/2025.csv |
| 083650 | atlas/symbol_profiles/083/083650.json | atlas/ohlcv_tradable_by_symbol_year/083/083650/2024.csv | atlas/ohlcv_tradable_by_symbol_year/083/083650/2025.csv |
| 000720 | atlas/symbol_profiles/000/000720.json | atlas/ohlcv_tradable_by_symbol_year/000/000720/2024.csv | atlas/ohlcv_tradable_by_symbol_year/000/000720/2025.csv |

OHLC rows used: 034020 2024/2025 fileciteturn129file0turn130file0, 052690 2024/2025 fileciteturn131file0turn132file0, 083650 2024/2025 fileciteturn133file0turn134file0, 000720 2024/2025 fileciteturn136file0turn137file0.

## 11. Case-by-Case Trigger Grid

| trigger_id | symbol | trigger_type | trigger_date | entry_date | entry_price | stage2 evidence | stage3 evidence | 4B evidence | 4C label |
|---|---:|---|---:|---:|---:|---|---|---|---|
| T034020_STAGE2_20240717_CZ_PREFERRED_BIDDER | 034020 | Stage2-Actionable | 2024-07-17 | 2024-07-18 | 21,000 | policy, customer, event, RS | partial visibility only | price-only local peak + legal block | false_break |
| T052690_STAGE2_20240717_CZ_PREFERRED_BIDDER | 052690 | Stage2-Actionable | 2024-07-17 | 2024-07-18 | 82,000 | policy, customer, event, RS | partial visibility only | price-only local peak + legal block | false_break |
| T083650_STAGE2_20240717_CZ_PREFERRED_BIDDER | 083650 | Stage2-Actionable | 2024-07-17 | 2024-07-18 | 8,810 | policy, event, RS | delayed conversion | price-only local + positioning | watch_only |
| T000720_STAGE2_20240717_CZ_PREFERRED_BIDDER | 000720 | Stage2-Watch / false-positive stress | 2024-07-17 | 2024-07-18 | 33,400 | policy headline | unsupported | margin/PF/EPC beta | watch_only |

## 12. Trigger-Level OHLC Backtest Tables

Formula:

```text
MFE_N_pct = (max high from entry_date through N trading days / entry_price - 1) * 100
MAE_N_pct = (min low from entry_date through N trading days / entry_price - 1) * 100
```

| symbol | entry | entry_price | MFE_30D | MAE_30D | MFE_90D | MAE_90D | MFE_180D | MAE_180D | MFE_1Y | MAE_1Y | peak_date | peak_price | drawdown_after_peak |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 034020 | 2024-07-18 | 21,000 | 19.05% | -27.86% | 19.05% | -27.86% | 47.14% | -27.86% | 243.81% | -27.86% | 2025-06-30 | 72,200 | -14.54% |
| 052690 | 2024-07-18 | 82,000 | 19.63% | -24.88% | 19.63% | -24.88% | 19.63% | -39.27% | 48.41% | -39.27% | 2025-06-25 | 121,700 | -19.06% |
| 083650 | 2024-07-18 | 8,810 | 19.52% | -19.41% | 126.11% | -20.54% | 181.50% | -20.54% | 440.30% | -20.54% | 2025-06-17 | 47,600 | -17.96% |
| 000720 | 2024-07-18 | 33,400 | 4.34% | -13.02% | 4.34% | -17.96% | 14.37% | -27.84% | 154.79% | -27.84% | 2025-06-25 | 85,100 | -10.34% |

Important interpretation: the 1Y rallies in 034020/052690/083650 validate the C04 supplier/engineering route. The 1Y rally in 000720 is not credited to the July C04 trigger without a clean nuclear margin/revision bridge; it is treated as a later construction/capital-flow cycle overlap.

## 13. Current Calibrated Profile Stress Test

| symbol | P0 likely action | actual path | verdict |
|---:|---|---|---|
| 034020 | Stage2-Actionable / Yellow, but event-day RS could tempt early Green | -27.9% MAE before later re-rating | current_profile_too_early |
| 052690 | Stage2-Actionable / Yellow | -39.3% 180D MAE, later 1Y recovery | current_profile_too_early |
| 083650 | Stage2/Yellow with optionality | 126.1% 90D and 181.5% 180D MFE | current_profile_correct |
| 000720 | Event-only policy score may overpromote EPC beta | only 14.4% 180D MFE with -27.8% MAE | current_profile_false_positive |

Answers to mandatory stress-test questions:

1. Current calibrated profile catches the direct-supplier route but risks being too permissive on policy-only/EPC beta.
2. Direct supplier path fits later MFE, but with high MAE; EPC beta does not align inside 180D.
3. Stage2 bonus is useful, not excessive, for 034020/052690/083650; it is too permissive if applied to 000720 without margin/revision bridge.
4. Yellow 75 is useful as a holding pen.
5. Green 87/revision 55 should be strengthened only inside C04 when legal/contract uncertainty remains.
6. Price-only blowoff guard is correct.
7. Full 4B non-price requirement is correct and strengthened here.
8. Hard 4C routing should not fire on appeal/temporary signing delay alone; it should require cancellation/license failure/contract loss.

## 14. Stage2 / Yellow / Green Comparison

C04 behaves like a long fuse, not like a standard order announcement. The event lights the fuse; legal and contract evidence decides whether the flame reaches earnings.

| stage | C04 interpretation | observed lesson |
|---|---|---|
| Stage2 | policy selection / preferred bidder / direct route | valid for all four but weaker for EPC beta |
| Stage2-Actionable | direct supplier or engineering exposure with customer quality | valid for 034020/052690/083650 |
| Stage3-Yellow | event plus multi-source confirmation, but legal/contract bridge still open | best state for 034020/052690 before contract clarity |
| Stage3-Green | confirmed revision/margin/order bridge plus legal risk contained | premature for 034020/052690 at July trigger; possible later for 083650 |
| Stage3-Green cap | policy-only + no margin bridge + high legal risk | needed for 000720 |

`green_lateness_ratio` is not applicable at the July trigger because no clean Stage3-Green trigger is assigned in this MD. This is intentional: assigning Green from outcome would leak future price path.

## 15. 4B Local vs Full-window Timing Audit

| symbol | event-day/local high | full observed peak | local 4B read | full-window read | verdict |
|---:|---:|---:|---|---|---|
| 034020 | 25,000 | 72,200 | local spike looked like exhaustion | full cycle had far more upside | price_only_local_4B_too_early |
| 052690 | 98,100 | 121,700 | event-day blowoff was meaningful | later upside remained but MAE was harsh | price_only_local_4B_too_early |
| 083650 | 10,530 | 47,600 | local spike was tiny vs full cycle | full cycle re-rating dominated | price_only_local_4B_too_early |
| 000720 | 34,850 | 85,100 | local spike was not full 4B | later rally not clean C04 evidence | event_overlay_not_structural_rerating |

Rule implication:

```text
if C04 local peak is price-only:
    do_not_treat_as_full_4B = true
if legal appeal exists but no cancellation/license failure:
    legal_overlay = 4B/4C_watch
    hard_4C = false
```

## 16. 4C Protection Audit

| event | hard 4C? | reason |
|---|---:|---|
| 2024-08-27 EDF/Westinghouse appeal | false | appeals raised legal risk but did not cancel KHNP selection |
| 2024-09-03 UOHS review | false | review process is a legal/regulatory block overlay |
| 2024-10-30 signing prohibition | false / watch | temporary procedural block; not a thesis break without contract loss |
| 2025-05-06 court halt | watch | confirms legal risk was real, but the 2024 rows should not be routed as hard 4C ex ante |

Hard 4C in C04 should require one of:

```text
contract_cancelled
license_or_IP_export_failure
preferred_bidder_status_lost
project_scope materially removed
financing/state-aid structure rejected in a way that ends the route
```

## 17. Sector-Specific Rule Candidate

```text
rule_scope = sector_specific
large_sector_id = L1_INDUSTRIALS_INFRA_DEFENSE_GRID
axis = c04_policy_event_green_cap
candidate = true
```

Proposed shadow rule:

```text
For L1 nuclear policy/project cases, a preferred-bidder or policy-selection event can promote Stage2/Yellow,
but cannot promote Stage3-Green unless at least two of the following are present:
- direct supplier/engineering scope, not merely EPC/construction beta
- contract/order/backlog path visible
- margin or revision bridge visible
- legal appeal risk contained or procedurally non-fatal
- customer/project counterparty quality confirmed by multiple public sources
```

## 18. Canonical-Archetype Rule Candidate

```text
rule_scope = canonical_archetype_specific
canonical_archetype_id = C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY
axis_1 = c04_policy_event_green_cap
axis_2 = c04_legal_appeal_not_hard_4c
axis_3 = c04_direct_supplier_bridge_bonus
```

Shadow rule:

```text
C04 positive promotion:
    Stage2 = policy/project selection + direct route
    Stage3-Yellow = direct route + multi-source confirmation, while contract/legal bridge remains open
    Stage3-Green = direct route + contract/margin/revision bridge + legal risk not thesis-breaking

C04 negative protection:
    appeal/temporary injunction = 4B/4C watch
    cancellation/license failure/preferred-bidder loss = hard 4C
```

## 19. Before / After Backtest Comparison

| profile | eligible triggers | selected entries | avg MFE_90D | avg MAE_90D | avg MFE_180D | avg MAE_180D | false positive rate | score-return alignment |
|---|---:|---:|---:|---:|---:|---:|---:|---|
| P0 e2r_2_1_stock_web_calibrated_proxy | 4 | 4 | 42.31% | -22.73% | 65.66% | -28.88% | 25% | mixed |
| P0b e2r_2_0_baseline_reference | 4 | 4 | 42.31% | -22.73% | 65.66% | -28.88% | 25% | weaker Green guard |
| P1 L1 sector-specific candidate | 4 | 4 | 42.31% | -22.73% | 65.66% | -28.88% | 0% after EPC cap | better |
| P2 C04 canonical candidate | 4 | 4 | 42.31% | -22.73% | 65.66% | -28.88% | 0% after policy-only Green cap | better |
| P3 counterexample guard profile | 4 | 3 positive + 1 watch | 54.96% ex-counterexample | -24.29% | 82.76% ex-counterexample | -29.22% | 0% | best for C04 |

## 20. Score-Return Alignment Matrix

| symbol | weighted_score_before | stage_before | weighted_score_after | stage_after | alignment |
|---:|---:|---|---:|---|---|
| 034020 | 76 | Stage3-Yellow | 78 | Stage3-Yellow | good if not Green |
| 052690 | 74 | Stage2-Actionable | 76 | Stage3-Yellow | good if not Green |
| 083650 | 82 | Stage3-Yellow | 87 | Stage3-Green | good after delayed supplier conversion |
| 000720 | 78 | Stage3-Yellow | 66 | Stage2-Watch | improved false-positive control |

## 21. Coverage Matrix

| large_sector_id | canonical_archetype_id | fine_archetype_id | positive_case_count | counterexample_count | 4B_case_count | 4C_case_count | new_independent_case_count | reused_case_count | calibration_usable_trigger_count | representative_trigger_count | current_profile_error_count | sector_rule_candidate | canonical_rule_candidate | coverage_gap_after_this_loop |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|
| L1_INDUSTRIALS_INFRA_DEFENSE_GRID | C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY | CZECH_NUCLEAR_PREFERRED_BIDDER_LEGAL_APPEAL_DIRECT_SUPPLIER_VS_EPC_BETA | 3 | 1 | 3 | 2 watch-only | 4 | 0 | 4 | 4 | 3 | true | true | C04 now has direct supplier, engineering, small-cap supplier, and EPC-beta counterexample rows |

## 22. Residual Contribution Summary

```text
new_independent_case_count: 4
reused_case_count: 0
reused_case_ids: []
new_symbol_count: 4
same_archetype_new_symbol_count: 4
same_archetype_new_trigger_family_count: 2
new_canonical_archetype_count: 0
new_fine_archetype_count: 1
new_trigger_family_count: 2
tested_existing_calibrated_axes:
  - stage3_green_revision_min
  - full_4b_requires_non_price_evidence
  - hard_4c_thesis_break_routes_to_4c
residual_error_types_found:
  - event_only_policy_false_positive
  - legal_appeal_false_4C
  - direct_supplier_high_MAE_success
new_axis_proposed:
  - c04_policy_event_green_cap
  - c04_legal_appeal_not_hard_4c
  - c04_direct_supplier_bridge_bonus
existing_axis_strengthened:
  - stage3_green_revision_min in C04 only
  - full_4b_requires_non_price_evidence in C04 only
existing_axis_weakened: null
existing_axis_kept:
  - hard_4c_thesis_break_routes_to_4c, but only after cancellation/license/project loss
sector_specific_rule_candidate: true
canonical_archetype_rule_candidate: true
no_new_signal_reason: null
loop_contribution_label: canonical_archetype_rule_candidate
do_not_propose_new_weight_delta: false
```

## 23. Validation Scope / Non-Validation Scope

Validated:

```text
- stock-web manifest/schema fields
- symbol profile availability
- clean 180D corporate-action window for the selected 2024 trigger
- entry_date and entry_price from tradable shard
- MFE/MAE 30D/90D/180D from actual OHLC rows
- positive/counterexample balance
- current calibrated profile stress test
```

Not validated:

```text
- production scoring code
- live candidate status
- broker/API integration
- official DART financial restatement
- exact future contract economics after stock-web max_date
```

## 24. Shadow Weight Calibration

```csv
row_type,axis,scope,large_sector_id,canonical_archetype_id,baseline_value,tested_value,delta,reason,backtest_effect,trigger_ids,calibration_usable_count,new_independent_case_count,counterexample_count,confidence,proposal_type,notes
shadow_weight,c04_policy_event_green_cap,canonical_archetype_specific,L1_INDUSTRIALS_INFRA_DEFENSE_GRID,C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY,0,1,+1,"C04 policy headline alone created high-MAE or false-positive paths; direct supplier evidence survived but EPC-beta needed cap.","Reduced false Green on 000720 while preserving supplier Stage2/Yellow entries.","T034020_STAGE2_20240717_CZ_PREFERRED_BIDDER|T052690_STAGE2_20240717_CZ_PREFERRED_BIDDER|T083650_STAGE2_20240717_CZ_PREFERRED_BIDDER|T000720_STAGE2_20240717_CZ_PREFERRED_BIDDER",4,4,1,medium,canonical_shadow_only,"not production; post-calibrated residual"
shadow_weight,c04_legal_appeal_not_hard_4c,canonical_archetype_specific,L1_INDUSTRIALS_INFRA_DEFENSE_GRID,C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY,0,1,+1,"EDF/Westinghouse appeals and temporary signing blocks are 4B/4C watch overlays, not hard 4C unless contract cancellation or license failure appears.","Avoids false 4C on direct suppliers that later produced 1Y upside.","T034020_STAGE2_20240717_CZ_PREFERRED_BIDDER|T052690_STAGE2_20240717_CZ_PREFERRED_BIDDER|T083650_STAGE2_20240717_CZ_PREFERRED_BIDDER",3,3,0,medium,canonical_shadow_only,"not production; post-calibrated residual"
```

## 25. Machine-Readable Rows

```jsonl
{"row_type": "price_source_validation", "source": "Songdaiki/stock-web", "source_url": "https://github.com/Songdaiki/stock-web", "manifest_path": "atlas/manifest.json", "schema_path": "atlas/schema.json", "universe_path": "atlas/universe/all_symbols.csv", "manifest_max_date": "2026-02-20", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "raw_shard_root": "atlas/ohlcv_raw_by_symbol_year", "validation_status": "usable_for_historical_calibration"}
{"row_type": "case", "case_id": "R1L11_C04_034020_CZ_NUCLEAR_DIRECT_SUPPLIER", "symbol": "034020", "company_name": "두산에너빌리티", "round": "R1", "loop": "11", "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "canonical_archetype_id": "C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY", "fine_archetype_id": "CZECH_NUCLEAR_PREFERRED_BIDDER_LEGAL_APPEAL_DIRECT_SUPPLIER_VS_EPC_BETA", "case_type": "high_mae_success", "positive_or_counterexample": "positive", "best_trigger": "T034020_STAGE2_20240717_CZ_PREFERRED_BIDDER", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "high_mae_success", "current_profile_verdict": "current_profile_too_early", "price_source": "Songdaiki/stock-web", "notes": "Direct nuclear equipment/supplier route. The July 2024 event-day spike was not a full 4B because full-window upside later exceeded the local spike."}
{"row_type": "case", "case_id": "R1L11_C04_052690_CZ_NUCLEAR_ENGINEERING_DIRECT", "symbol": "052690", "company_name": "한전기술", "round": "R1", "loop": "11", "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "canonical_archetype_id": "C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY", "fine_archetype_id": "CZECH_NUCLEAR_PREFERRED_BIDDER_LEGAL_APPEAL_DIRECT_SUPPLIER_VS_EPC_BETA", "case_type": "high_mae_success", "positive_or_counterexample": "positive", "best_trigger": "T052690_STAGE2_20240717_CZ_PREFERRED_BIDDER", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "high_mae_success", "current_profile_verdict": "current_profile_too_early", "price_source": "Songdaiki/stock-web", "notes": "Direct nuclear engineering route; immediate event gap did not convert into clean 180D path, but later 2025 nuclear policy re-rating revived the case."}
{"row_type": "case", "case_id": "R1L11_C04_083650_CZ_NUCLEAR_AUXILIARY_SUPPLIER", "symbol": "083650", "company_name": "비에이치아이", "round": "R1", "loop": "11", "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "canonical_archetype_id": "C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY", "fine_archetype_id": "CZECH_NUCLEAR_PREFERRED_BIDDER_LEGAL_APPEAL_DIRECT_SUPPLIER_VS_EPC_BETA", "case_type": "structural_success", "positive_or_counterexample": "positive", "best_trigger": "T083650_STAGE2_20240717_CZ_PREFERRED_BIDDER", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "structural_success", "current_profile_verdict": "current_profile_correct", "price_source": "Songdaiki/stock-web", "notes": "Small-cap auxiliary supplier path: initial drawdown was meaningful, but 90D/180D MFE confirmed a stronger delayed re-rating than the large caps."}
{"row_type": "case", "case_id": "R1L11_C04_000720_CZ_NUCLEAR_EPC_BETA_FALSE_GREEN", "symbol": "000720", "company_name": "현대건설", "round": "R1", "loop": "11", "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "canonical_archetype_id": "C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY", "fine_archetype_id": "CZECH_NUCLEAR_PREFERRED_BIDDER_LEGAL_APPEAL_DIRECT_SUPPLIER_VS_EPC_BETA", "case_type": "failed_rerating", "positive_or_counterexample": "counterexample", "best_trigger": "T000720_STAGE2_20240717_CZ_PREFERRED_BIDDER", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "failed_rerating", "current_profile_verdict": "current_profile_false_positive", "price_source": "Songdaiki/stock-web", "notes": "EPC/construction beta counterexample: 2024 policy headline alone did not close a margin/revision bridge inside 180D; later 2025 rally should not be credited to the July C04 trigger."}
{"row_type": "trigger", "trigger_id": "T034020_STAGE2_20240717_CZ_PREFERRED_BIDDER", "case_id": "R1L11_C04_034020_CZ_NUCLEAR_DIRECT_SUPPLIER", "symbol": "034020", "company_name": "두산에너빌리티", "round": "R1", "loop": "11", "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "canonical_archetype_id": "C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY", "fine_archetype_id": "CZECH_NUCLEAR_PREFERRED_BIDDER_LEGAL_APPEAL_DIRECT_SUPPLIER_VS_EPC_BETA", "sector": "산업재·수주·인프라", "primary_archetype": "nuclear_policy_project_legal_delay", "loop_objective": "counterexample_mining | residual_false_positive_mining | 4B_non_price_requirement_stress_test | 4C_thesis_break_timing_test | sector_specific_rule_discovery | canonical_archetype_compression | coverage_gap_fill", "trigger_type": "Stage2-Actionable", "trigger_date": "2024-07-17", "evidence_available_at_that_date": "Czech government selected KHNP as preferred bidder for Dukovany nuclear units; evidence treated as next KRX tradable close.", "evidence_source": "Reuters 2024-07-17; later Reuters appeal/legal-block reports used only as 4B/4C watch overlays.", "stage2_evidence_fields": ["public_event_or_disclosure", "customer_or_order_quality", "policy_or_regulatory_optionality", "relative_strength"], "stage3_evidence_fields": ["multiple_public_sources", "financial_visibility"], "stage4b_evidence_fields": ["price_only_local_peak", "legal_or_regulatory_block"], "stage4c_evidence_fields": ["thesis_evidence_broken"], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/034/034020/2024.csv", "profile_path": "atlas/symbol_profiles/034/034020.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "entry_date": "2024-07-18", "entry_price": 21000, "MFE_30D_pct": 19.05, "MFE_90D_pct": 19.05, "MFE_180D_pct": 47.14, "MFE_1Y_pct": 243.81, "MFE_2Y_pct": null, "MAE_30D_pct": -27.86, "MAE_90D_pct": -27.86, "MAE_180D_pct": -27.86, "MAE_1Y_pct": -27.86, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2025-06-30", "peak_price": 72200, "drawdown_after_peak_pct": -14.54, "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": 1.0, "four_b_full_window_peak_proximity": 0.08, "four_b_timing_verdict": "price_only_local_4B_too_early", "four_b_evidence_type": ["price_only", "legal_or_regulatory_block"], "four_c_protection_label": "false_break", "trigger_outcome_label": "high_mae_success", "current_profile_verdict": "current_profile_too_early", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window", "same_entry_group_id": "R1L11_C04_034020_CZ_NUCLEAR_DIRECT_SUPPLIER__2024-07-18__21000", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false}
{"row_type": "trigger", "trigger_id": "T052690_STAGE2_20240717_CZ_PREFERRED_BIDDER", "case_id": "R1L11_C04_052690_CZ_NUCLEAR_ENGINEERING_DIRECT", "symbol": "052690", "company_name": "한전기술", "round": "R1", "loop": "11", "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "canonical_archetype_id": "C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY", "fine_archetype_id": "CZECH_NUCLEAR_PREFERRED_BIDDER_LEGAL_APPEAL_DIRECT_SUPPLIER_VS_EPC_BETA", "sector": "산업재·수주·인프라", "primary_archetype": "nuclear_policy_project_legal_delay", "loop_objective": "counterexample_mining | residual_false_positive_mining | 4B_non_price_requirement_stress_test | 4C_thesis_break_timing_test | sector_specific_rule_discovery | canonical_archetype_compression | coverage_gap_fill", "trigger_type": "Stage2-Actionable", "trigger_date": "2024-07-17", "evidence_available_at_that_date": "Czech government selected KHNP as preferred bidder for Dukovany nuclear units; evidence treated as next KRX tradable close.", "evidence_source": "Reuters 2024-07-17; later Reuters appeal/legal-block reports used only as 4B/4C watch overlays.", "stage2_evidence_fields": ["public_event_or_disclosure", "customer_or_order_quality", "policy_or_regulatory_optionality", "relative_strength"], "stage3_evidence_fields": ["multiple_public_sources", "financial_visibility"], "stage4b_evidence_fields": ["price_only_local_peak", "legal_or_regulatory_block"], "stage4c_evidence_fields": ["thesis_evidence_broken"], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/052/052690/2024.csv", "profile_path": "atlas/symbol_profiles/052/052690.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "entry_date": "2024-07-18", "entry_price": 82000, "MFE_30D_pct": 19.63, "MFE_90D_pct": 19.63, "MFE_180D_pct": 19.63, "MFE_1Y_pct": 48.41, "MFE_2Y_pct": null, "MAE_30D_pct": -24.88, "MAE_90D_pct": -24.88, "MAE_180D_pct": -39.27, "MAE_1Y_pct": -39.27, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2025-06-25", "peak_price": 121700, "drawdown_after_peak_pct": -19.06, "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": 1.0, "four_b_full_window_peak_proximity": 0.41, "four_b_timing_verdict": "price_only_local_4B_too_early", "four_b_evidence_type": ["price_only", "legal_or_regulatory_block"], "four_c_protection_label": "false_break", "trigger_outcome_label": "high_mae_success", "current_profile_verdict": "current_profile_too_early", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window", "same_entry_group_id": "R1L11_C04_052690_CZ_NUCLEAR_ENGINEERING_DIRECT__2024-07-18__82000", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false}
{"row_type": "trigger", "trigger_id": "T083650_STAGE2_20240717_CZ_PREFERRED_BIDDER", "case_id": "R1L11_C04_083650_CZ_NUCLEAR_AUXILIARY_SUPPLIER", "symbol": "083650", "company_name": "비에이치아이", "round": "R1", "loop": "11", "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "canonical_archetype_id": "C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY", "fine_archetype_id": "CZECH_NUCLEAR_PREFERRED_BIDDER_LEGAL_APPEAL_DIRECT_SUPPLIER_VS_EPC_BETA", "sector": "산업재·수주·인프라", "primary_archetype": "nuclear_policy_project_legal_delay", "loop_objective": "counterexample_mining | residual_false_positive_mining | 4B_non_price_requirement_stress_test | 4C_thesis_break_timing_test | sector_specific_rule_discovery | canonical_archetype_compression | coverage_gap_fill", "trigger_type": "Stage2-Actionable", "trigger_date": "2024-07-17", "evidence_available_at_that_date": "Czech government selected KHNP as preferred bidder for Dukovany nuclear units; evidence treated as next KRX tradable close.", "evidence_source": "Reuters 2024-07-17; later Reuters appeal/legal-block reports used only as 4B/4C watch overlays.", "stage2_evidence_fields": ["public_event_or_disclosure", "policy_or_regulatory_optionality", "relative_strength"], "stage3_evidence_fields": ["multiple_public_sources", "repeat_order_or_conversion", "low_red_team_risk"], "stage4b_evidence_fields": ["price_only_local_peak", "positioning_overheat"], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/083/083650/2024.csv", "profile_path": "atlas/symbol_profiles/083/083650.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "entry_date": "2024-07-18", "entry_price": 8810, "MFE_30D_pct": 19.52, "MFE_90D_pct": 126.11, "MFE_180D_pct": 181.5, "MFE_1Y_pct": 440.3, "MFE_2Y_pct": null, "MAE_30D_pct": -19.41, "MAE_90D_pct": -20.54, "MAE_180D_pct": -20.54, "MAE_1Y_pct": -20.54, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2025-06-17", "peak_price": 47600, "drawdown_after_peak_pct": -17.96, "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": 1.0, "four_b_full_window_peak_proximity": 0.04, "four_b_timing_verdict": "price_only_local_4B_too_early", "four_b_evidence_type": ["price_only", "positioning_overheat"], "four_c_protection_label": "thesis_break_watch_only", "trigger_outcome_label": "structural_success", "current_profile_verdict": "current_profile_correct", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window", "same_entry_group_id": "R1L11_C04_083650_CZ_NUCLEAR_AUXILIARY_SUPPLIER__2024-07-18__8810", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false}
{"row_type": "trigger", "trigger_id": "T000720_STAGE2_20240717_CZ_PREFERRED_BIDDER", "case_id": "R1L11_C04_000720_CZ_NUCLEAR_EPC_BETA_FALSE_GREEN", "symbol": "000720", "company_name": "현대건설", "round": "R1", "loop": "11", "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "canonical_archetype_id": "C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY", "fine_archetype_id": "CZECH_NUCLEAR_PREFERRED_BIDDER_LEGAL_APPEAL_DIRECT_SUPPLIER_VS_EPC_BETA", "sector": "산업재·수주·인프라", "primary_archetype": "nuclear_policy_project_legal_delay", "loop_objective": "counterexample_mining | residual_false_positive_mining | 4B_non_price_requirement_stress_test | 4C_thesis_break_timing_test | sector_specific_rule_discovery | canonical_archetype_compression | coverage_gap_fill", "trigger_type": "Stage2-Actionable", "trigger_date": "2024-07-17", "evidence_available_at_that_date": "Czech government selected KHNP as preferred bidder for Dukovany nuclear units; evidence treated as next KRX tradable close.", "evidence_source": "Reuters 2024-07-17; later Reuters appeal/legal-block reports used only as 4B/4C watch overlays.", "stage2_evidence_fields": ["public_event_or_disclosure", "policy_or_regulatory_optionality"], "stage3_evidence_fields": [], "stage4b_evidence_fields": ["legal_or_regulatory_block", "margin_or_backlog_slowdown"], "stage4c_evidence_fields": ["thesis_evidence_broken"], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/000/000720/2024.csv", "profile_path": "atlas/symbol_profiles/000/000720.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "entry_date": "2024-07-18", "entry_price": 33400, "MFE_30D_pct": 4.34, "MFE_90D_pct": 4.34, "MFE_180D_pct": 14.37, "MFE_1Y_pct": 154.79, "MFE_2Y_pct": null, "MAE_30D_pct": -13.02, "MAE_90D_pct": -17.96, "MAE_180D_pct": -27.84, "MAE_1Y_pct": -27.84, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2025-06-25", "peak_price": 85100, "drawdown_after_peak_pct": -10.34, "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": 1.0, "four_b_full_window_peak_proximity": 0.03, "four_b_timing_verdict": "price_only_local_4B_too_early", "four_b_evidence_type": ["price_only", "margin_or_backlog_slowdown"], "four_c_protection_label": "thesis_break_watch_only", "trigger_outcome_label": "failed_rerating", "current_profile_verdict": "current_profile_false_positive", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window", "same_entry_group_id": "R1L11_C04_000720_CZ_NUCLEAR_EPC_BETA_FALSE_GREEN__2024-07-18__33400", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R1L11_C04_034020_CZ_NUCLEAR_DIRECT_SUPPLIER", "trigger_id": "T034020_STAGE2_20240717_CZ_PREFERRED_BIDDER", "symbol": "034020", "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "canonical_archetype_id": "C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY", "raw_component_scores_before": {"contract_score": 5, "backlog_visibility_score": 4, "margin_bridge_score": 4, "revision_score": 4, "relative_strength_score": 6, "customer_quality_score": 8, "policy_or_regulatory_score": 9, "valuation_repricing_score": 4, "execution_risk_score": 5, "legal_or_contract_risk_score": 4, "dilution_cb_risk_score": 1, "accounting_trust_risk_score": 1}, "weighted_score_before": 76, "stage_label_before": "Stage3-Yellow", "raw_component_scores_after": {"contract_score": 5, "backlog_visibility_score": 4, "margin_bridge_score": 5, "revision_score": 4, "relative_strength_score": 6, "customer_quality_score": 8, "policy_or_regulatory_score": 9, "valuation_repricing_score": 4, "execution_risk_score": 5, "legal_or_contract_risk_score": 5, "dilution_cb_risk_score": 1, "accounting_trust_risk_score": 1}, "weighted_score_after": 78, "stage_label_after": "Stage3-Yellow", "changed_components": ["policy_or_regulatory_score", "margin_bridge_score", "legal_or_contract_risk_score", "execution_risk_score"], "component_delta_explanation": "C04 shadow profile caps event-only policy score unless contract/margin/revision bridge appears; supplier routes can remain Stage2/Yellow through legal watch, while EPC-beta without bridge is capped.", "MFE_90D_pct": 19.05, "MAE_90D_pct": -27.86, "score_return_alignment_label": "high_mae_success", "current_profile_verdict": "current_profile_too_early"}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R1L11_C04_052690_CZ_NUCLEAR_ENGINEERING_DIRECT", "trigger_id": "T052690_STAGE2_20240717_CZ_PREFERRED_BIDDER", "symbol": "052690", "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "canonical_archetype_id": "C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY", "raw_component_scores_before": {"contract_score": 4, "backlog_visibility_score": 4, "margin_bridge_score": 3, "revision_score": 3, "relative_strength_score": 6, "customer_quality_score": 8, "policy_or_regulatory_score": 9, "valuation_repricing_score": 4, "execution_risk_score": 5, "legal_or_contract_risk_score": 4, "dilution_cb_risk_score": 1, "accounting_trust_risk_score": 1}, "weighted_score_before": 74, "stage_label_before": "Stage2-Actionable", "raw_component_scores_after": {"contract_score": 4, "backlog_visibility_score": 4, "margin_bridge_score": 4, "revision_score": 3, "relative_strength_score": 6, "customer_quality_score": 8, "policy_or_regulatory_score": 9, "valuation_repricing_score": 4, "execution_risk_score": 5, "legal_or_contract_risk_score": 5, "dilution_cb_risk_score": 1, "accounting_trust_risk_score": 1}, "weighted_score_after": 76, "stage_label_after": "Stage3-Yellow", "changed_components": ["policy_or_regulatory_score", "margin_bridge_score", "legal_or_contract_risk_score", "execution_risk_score"], "component_delta_explanation": "C04 shadow profile caps event-only policy score unless contract/margin/revision bridge appears; supplier routes can remain Stage2/Yellow through legal watch, while EPC-beta without bridge is capped.", "MFE_90D_pct": 19.63, "MAE_90D_pct": -24.88, "score_return_alignment_label": "high_mae_success", "current_profile_verdict": "current_profile_too_early"}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R1L11_C04_083650_CZ_NUCLEAR_AUXILIARY_SUPPLIER", "trigger_id": "T083650_STAGE2_20240717_CZ_PREFERRED_BIDDER", "symbol": "083650", "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "canonical_archetype_id": "C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY", "raw_component_scores_before": {"contract_score": 5, "backlog_visibility_score": 4, "margin_bridge_score": 5, "revision_score": 5, "relative_strength_score": 7, "customer_quality_score": 6, "policy_or_regulatory_score": 8, "valuation_repricing_score": 5, "execution_risk_score": 4, "legal_or_contract_risk_score": 3, "dilution_cb_risk_score": 1, "accounting_trust_risk_score": 1}, "weighted_score_before": 82, "stage_label_before": "Stage3-Yellow", "raw_component_scores_after": {"contract_score": 5, "backlog_visibility_score": 4, "margin_bridge_score": 6, "revision_score": 5, "relative_strength_score": 8, "customer_quality_score": 6, "policy_or_regulatory_score": 8, "valuation_repricing_score": 6, "execution_risk_score": 4, "legal_or_contract_risk_score": 3, "dilution_cb_risk_score": 1, "accounting_trust_risk_score": 1}, "weighted_score_after": 87, "stage_label_after": "Stage3-Green", "changed_components": ["policy_or_regulatory_score", "margin_bridge_score", "legal_or_contract_risk_score", "execution_risk_score"], "component_delta_explanation": "C04 shadow profile caps event-only policy score unless contract/margin/revision bridge appears; supplier routes can remain Stage2/Yellow through legal watch, while EPC-beta without bridge is capped.", "MFE_90D_pct": 126.11, "MAE_90D_pct": -20.54, "score_return_alignment_label": "structural_success", "current_profile_verdict": "current_profile_correct"}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R1L11_C04_000720_CZ_NUCLEAR_EPC_BETA_FALSE_GREEN", "trigger_id": "T000720_STAGE2_20240717_CZ_PREFERRED_BIDDER", "symbol": "000720", "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "canonical_archetype_id": "C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY", "raw_component_scores_before": {"contract_score": 2, "backlog_visibility_score": 2, "margin_bridge_score": 1, "revision_score": 2, "relative_strength_score": 3, "customer_quality_score": 5, "policy_or_regulatory_score": 8, "valuation_repricing_score": 2, "execution_risk_score": 7, "legal_or_contract_risk_score": 5, "dilution_cb_risk_score": 1, "accounting_trust_risk_score": 1}, "weighted_score_before": 78, "stage_label_before": "Stage3-Yellow", "raw_component_scores_after": {"contract_score": 2, "backlog_visibility_score": 2, "margin_bridge_score": 1, "revision_score": 2, "relative_strength_score": 3, "customer_quality_score": 5, "policy_or_regulatory_score": 5, "valuation_repricing_score": 2, "execution_risk_score": 8, "legal_or_contract_risk_score": 5, "dilution_cb_risk_score": 1, "accounting_trust_risk_score": 1}, "weighted_score_after": 66, "stage_label_after": "Stage2-Watch", "changed_components": ["policy_or_regulatory_score", "margin_bridge_score", "legal_or_contract_risk_score", "execution_risk_score"], "component_delta_explanation": "C04 shadow profile caps event-only policy score unless contract/margin/revision bridge appears; supplier routes can remain Stage2/Yellow through legal watch, while EPC-beta without bridge is capped.", "MFE_90D_pct": 4.34, "MAE_90D_pct": -17.96, "score_return_alignment_label": "failed_rerating", "current_profile_verdict": "current_profile_false_positive"}
{"row_type": "residual_contribution", "round": "R1", "loop": "11", "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "canonical_archetype_id": "C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY", "new_independent_case_count": 4, "reused_case_count": 0, "new_symbol_count": 4, "same_archetype_new_symbol_count": 4, "same_archetype_new_trigger_family_count": 2, "new_canonical_archetype_count": 0, "new_trigger_family_count": 2, "tested_existing_calibrated_axes": ["stage3_green_revision_min", "full_4b_requires_non_price_evidence", "hard_4c_thesis_break_routes_to_4c"], "residual_error_types_found": ["event_only_policy_false_positive", "legal_appeal_false_4C", "direct_supplier_high_MAE_success"], "loop_contribution_label": "canonical_archetype_rule_candidate", "do_not_propose_new_weight_delta": false}
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
next_round = R1_holdout_or_R2_loop11_restart
suggested_next_scope = C05_EPC_MEGA_CONTRACT_MARGIN_GAP or C07/C08 holdout, avoiding already repeated representative HBM/grid names
```

## 28. Source Notes

- Prompt constraints: supplied v12 prompt in conversation. fileciteturn125file0
- Stock-agent calibration ingest and applied scoring diff: fileciteturn107file0turn108file0
- Stock-web manifest and schema: fileciteturn109file0turn110file0
- Profiles: fileciteturn126file0turn127file0turn128file0turn135file0
- OHLC rows: fileciteturn129file0turn130file0turn131file0turn132file0turn133file0turn134file0turn136file0turn137file0
- Historical public evidence: citeturn118157news1turn118157news0turn872724news2turn872724news0turn872724news1turn118157news2
