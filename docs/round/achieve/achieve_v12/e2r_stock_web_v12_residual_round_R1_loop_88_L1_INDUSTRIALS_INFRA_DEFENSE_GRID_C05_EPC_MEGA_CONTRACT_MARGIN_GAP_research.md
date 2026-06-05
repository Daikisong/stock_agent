# E2R Stock-Web V12 Residual Research — R1 Loop 88 — L1 / C05 EPC Mega Contract Margin Gap

```text
schema_family: v12_sector_archetype_residual
scheduled_round: R1
scheduled_loop: 88
large_sector_id: L1_INDUSTRIALS_INFRA_DEFENSE_GRID
canonical_archetype_id: C05_EPC_MEGA_CONTRACT_MARGIN_GAP
fine_archetype_id: SAUDI_FADHILI_MEGA_EPC_CONTRACT_MARGIN_CONVERSION_BRIDGE
research_session: post_calibrated_sector_archetype_residual_research
mode: historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12
production_scoring_changed: false
shadow_weight_only: true
handoff_prompt_executed_now: false
```

## 1. Scope and scheduler check

This file follows the R1 slot of the v12 round cycle after the prior R13 / loop 87 completion.

```text
previous_completed_round: R13
previous_completed_loop: 87
scheduled_round: R1
scheduled_loop: 88
round_sector_consistency: pass
allowed_large_sector_for_R1: L1_INDUSTRIALS_INFRA_DEFENSE_GRID
selected_large_sector_id: L1_INDUSTRIALS_INFRA_DEFENSE_GRID
```

R1 is used here for the industrials / infrastructure / EPC branch.  Within R1, this run chooses `C05_EPC_MEGA_CONTRACT_MARGIN_GAP` because the No-Repeat snapshot shows low C05 coverage versus other L1 scopes:

```text
C05 current snapshot from No-Repeat Index:
rows = 10
symbols = 9
date_range = 2023-03-31~2024-07-12
good/bad Stage2 = 3/4
4B/4C = 0/0
```

## 2. Price source validation

```text
price_data_source = Songdaiki/stock-web
upstream_source = FinanceData/marcap
price_basis = tradable_raw
price_adjustment_status = raw_unadjusted_marcap
stock_web_manifest_max_date = 2026-02-20
calibration_shard_root = atlas/ohlcv_tradable_by_symbol_year
```

Profile checks:

| symbol | profile | name | last_date | corp-action window status |
|---|---|---|---|---|
| 028050 | atlas/symbol_profiles/028/028050.json | 삼성E&A | 2026-02-20 | candidate dates only before 2024; entry~D180 clear |
| 006360 | atlas/symbol_profiles/006/006360.json | GS건설 | 2026-02-20 | candidate dates only before 2024; entry~D180 clear |
| 000720 | atlas/symbol_profiles/000/000720.json | 현대건설 | 2026-02-20 | candidate dates only before 2024; entry~D180 clear |

## 3. Research thesis

C05 should not treat every mega EPC headline as identical.  The useful Stage2 signal is not simply “large contract exists.”  It is the bridge from a mega contract into visible backlog, margin quality, working-capital control, and execution-risk containment.

The April 2024 Fadhili gas expansion contract cluster is a good R1/C05 residual test because Aramco awarded a large EPC package to Samsung Engineering / Samsung E&A and GS E&C, but the subsequent price paths diverged in timing and risk shape.  Samsung E&A looked closer to a clean plant-EPC backlog case.  GS E&C had the same headline but still needed a balance-sheet and construction-overhang guard.  Hyundai E&C is used as a negative-control peer-beta row: the sector can move with EPC headlines, but without direct contract and margin bridge evidence it should not unlock Green.

## 4. Evidence summary

| case_id | symbol | role | as-of evidence | interpretation |
|---|---|---|---|---|
| R1L88_C05_028050_FADHILI | 028050 | positive / high-MAE | Fadhili mega EPC award; about $6bn Samsung E&A exposure reported | Stage2-Actionable allowed, Green delayed until margin/backlog conversion |
| R1L88_C05_006360_FADHILI | 006360 | delayed positive with overhang guard | Fadhili co-award to GS E&C | Stage2-Watch; do not convert to Green until margin and balance-sheet overhang bridge |
| R1L88_C05_000720_NEGCTRL | 000720 | counterexample / negative control | broad EPC peer beta without direct Fadhili contract evidence in this run | peer beta must not receive C05 contract-quality credit |

## 5. Machine-readable trigger rows JSONL

```jsonl
{"row_type": "trigger", "trigger_id": "R1L88_C05_T01", "case_id": "R1L88_C05_028050_FADHILI", "symbol": "028050", "company_name": "삼성E&A", "round": "R1", "loop": "88", "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "canonical_archetype_id": "C05_EPC_MEGA_CONTRACT_MARGIN_GAP", "fine_archetype_id": "SAUDI_FADHILI_MEGA_EPC_CONTRACT_MARGIN_CONVERSION_BRIDGE", "sector": "industrial_epc_plant", "primary_archetype": "mega_epc_award_with_margin_conversion", "loop_objective": "coverage_gap_fill | counterexample_mining | 4B_non_price_requirement_stress_test | canonical_archetype_compression", "trigger_type": "Stage2-Actionable / MegaEPCAwardWithMarginBridge", "trigger_date": "2024-04-03", "evidence_available_at_that_date": "Aramco Fadhili gas plant expansion EPC awards: Samsung Engineering / GS E&C / Nesma; Samsung E&A share rally on about $6bn contract report.", "evidence_source": "Reuters 2024-04-02; WSJ 2024-04-03; stock-web 1D tradable shard", "stage2_evidence_fields": "mega_epc_contract_award; government/Aramco customer; long project completion to 2027; contract value large enough versus ordinary annual order intake", "stage3_evidence_fields": "needs disclosed contract economics, margin bridge, backlog-to-revenue schedule, execution risk control", "stage4b_evidence_fields": "valuation/local peak only unless revision slowdown or margin issue appears", "stage4c_evidence_fields": "hard thesis break only if contract delay/cost overrun/accounting issue emerges", "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/028/028050/2024.csv", "profile_path": "atlas/symbol_profiles/028/028050.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "entry_date": "2024-04-03", "entry_price": 25300.0, "MFE_30D_pct": 6.72, "MFE_90D_pct": 15.81, "MFE_180D_pct": 15.81, "MFE_1Y_pct": "not_required", "MFE_2Y_pct": "not_required", "MAE_30D_pct": -4.94, "MAE_90D_pct": -14.62, "MAE_180D_pct": -16.6, "MAE_1Y_pct": "not_required", "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2024-07-30", "peak_price": 29300.0, "drawdown_after_peak_pct": -27.99, "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": 0.97, "four_b_full_window_peak_proximity": 1.0, "four_b_timing_verdict": "price_local_peak_not_full_4B_without_non_price_evidence", "four_b_evidence_type": "price_only", "four_c_protection_label": "not_applicable", "trigger_outcome_label": "positive_but_high_MAE_delayed_repricing", "current_profile_verdict": "partial_miss: Stage2 credit works, but Green must wait for margin/backlog conversion", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clear_for_entry_to_D180; profile corporate action candidates are historical pre-2024", "same_entry_group_id": "028050_2024-04-03_25300", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": "", "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false}
{"row_type": "trigger", "trigger_id": "R1L88_C05_T02", "case_id": "R1L88_C05_006360_FADHILI", "symbol": "006360", "company_name": "GS건설", "round": "R1", "loop": "88", "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "canonical_archetype_id": "C05_EPC_MEGA_CONTRACT_MARGIN_GAP", "fine_archetype_id": "SAUDI_FADHILI_MEGA_EPC_CONTRACT_MARGIN_CONVERSION_BRIDGE", "sector": "industrial_epc_plant", "primary_archetype": "mega_epc_award_with_balance_sheet_and_margin_guard", "loop_objective": "coverage_gap_fill | counterexample_mining | 4B_non_price_requirement_stress_test | canonical_archetype_compression", "trigger_type": "Stage2-Watch / MegaEPCAwardButMarginAndBSGuard", "trigger_date": "2024-04-03", "evidence_available_at_that_date": "Aramco awarded Fadhili expansion EPC contracts to Samsung Engineering and GS E&C; GS E&C also carries construction/PF and domestic execution overhang, so contract headline needs margin/BS bridge.", "evidence_source": "Reuters 2024-04-02; stock-web 1D tradable shard", "stage2_evidence_fields": "mega_epc_award; Aramco customer; peer co-award", "stage3_evidence_fields": "requires explicit margin, execution, and balance-sheet overhang repair before Green", "stage4b_evidence_fields": "local overheat after delayed rerating; full 4B requires non-price revision/overhang evidence", "stage4c_evidence_fields": "thesis break if project margin or balance-sheet repair fails", "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/006/006360/2024.csv", "profile_path": "atlas/symbol_profiles/006/006360.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "entry_date": "2024-04-03", "entry_price": 15630.0, "MFE_30D_pct": 6.97, "MFE_90D_pct": 30.52, "MFE_180D_pct": 39.15, "MFE_1Y_pct": "not_required", "MFE_2Y_pct": "not_required", "MAE_30D_pct": -9.92, "MAE_90D_pct": -9.92, "MAE_180D_pct": -9.92, "MAE_1Y_pct": "not_required", "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2024-08-27", "peak_price": 21750.0, "drawdown_after_peak_pct": -19.31, "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": 0.88, "four_b_full_window_peak_proximity": 1.0, "four_b_timing_verdict": "good_local_4B_watch_but_full_4B_needs_non_price_evidence", "four_b_evidence_type": "price_only | balance_sheet_overhang_watch", "four_c_protection_label": "not_applicable", "trigger_outcome_label": "positive_delayed_rerating_with_overhang_watch", "current_profile_verdict": "kept: Stage2-Watch rather than Green until balance-sheet and margin bridge improves", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clear_for_entry_to_D180; profile corporate action candidates are pre-2024", "same_entry_group_id": "006360_2024-04-03_15630", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": "same symbol appears in C30 history but this is a different canonical and trigger family", "independent_evidence_weight": 0.75, "do_not_count_as_new_case": false}
{"row_type": "trigger", "trigger_id": "R1L88_C05_T03", "case_id": "R1L88_C05_000720_NEGCTRL", "symbol": "000720", "company_name": "현대건설", "round": "R1", "loop": "88", "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "canonical_archetype_id": "C05_EPC_MEGA_CONTRACT_MARGIN_GAP", "fine_archetype_id": "MEGA_EPC_PEER_BASKET_NEGATIVE_CONTROL_MARGIN_GAP", "sector": "industrial_epc_construction_peer", "primary_archetype": "peer_beta_without_case_specific_contract_margin_bridge", "loop_objective": "coverage_gap_fill | counterexample_mining | 4B_non_price_requirement_stress_test | canonical_archetype_compression", "trigger_type": "Stage2-FalsePositive-Candidate / PeerEPCBasketsWithoutDirectContractBridge", "trigger_date": "2024-04-03", "evidence_available_at_that_date": "Negative-control peer: broad overseas EPC/construction beta can move with mega-contract headlines, but without case-specific contract economics it should not receive C05 Green credit.", "evidence_source": "stock-web 1D tradable shard; source_proxy_only peer-beta negative control", "stage2_evidence_fields": "large contractor peer; no direct Fadhili award evidence in this run", "stage3_evidence_fields": "not eligible without direct contract value, margin bridge, backlog conversion", "stage4b_evidence_fields": "not applicable", "stage4c_evidence_fields": "not applicable", "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/000/000720/2024.csv", "profile_path": "atlas/symbol_profiles/000/000720.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "entry_date": "2024-04-03", "entry_price": 32650.0, "MFE_30D_pct": 10.26, "MFE_90D_pct": 10.26, "MFE_180D_pct": 10.26, "MFE_1Y_pct": "not_required", "MFE_2Y_pct": "not_required", "MAE_30D_pct": -4.44, "MAE_90D_pct": -3.68, "MAE_180D_pct": -3.68, "MAE_1Y_pct": "not_required", "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2024-05-09", "peak_price": 36000.0, "drawdown_after_peak_pct": -12.64, "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": 0.99, "four_b_full_window_peak_proximity": 1.0, "four_b_timing_verdict": "negative_control_no_full_4B", "four_b_evidence_type": "price_only", "four_c_protection_label": "not_applicable", "trigger_outcome_label": "counterexample_peer_beta_not_structural_C05", "current_profile_verdict": "would_be_false_positive_if_peer_beta_counted_as_C05_contract_quality", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": ["source_proxy_only_negative_control_for_promotion"], "corporate_action_window_status": "clear_for_entry_to_D180; profile corporate action candidates are pre-2024", "same_entry_group_id": "000720_2024-04-03_32650", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": "", "independent_evidence_weight": 0.5, "do_not_count_as_new_case": false}
```

## 6. Case table

| case | symbol | entry | entry_price | MFE30 | MAE30 | MFE90 | MAE90 | MFE180 | MAE180 | verdict |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| Fadhili Samsung E&A | 028050 | 2024-04-03 | 25,300 | +6.72% | -4.94% | +15.81% | -14.62% | +15.81% | -16.60% | positive but high-MAE; Green needs margin bridge |
| Fadhili GS E&C | 006360 | 2024-04-03 | 15,630 | +6.97% | -9.92% | +30.52% | -9.92% | +39.15% | -9.92% | delayed positive; balance-sheet overhang guard |
| Hyundai E&C peer control | 000720 | 2024-04-03 | 32,650 | +10.26% | -4.44% | +10.26% | -3.68% | +10.26% | -3.68% | counterexample if peer beta is misread as C05 contract evidence |

## 7. 4B local vs full-window audit

| symbol | local peak | full-window peak | local proximity | full proximity | 4B conclusion |
|---|---:|---:|---:|---:|---|
| 028050 | 29,300 | 29,300 | 0.97 | 1.00 | price-only local peak; not full 4B without non-price evidence |
| 006360 | 21,750 | 21,750 | 0.88 | 1.00 | good local 4B watch, but full 4B needs margin/revision/overhang evidence |
| 000720 | 36,000 | 36,000 | 0.99 | 1.00 | negative-control peak; do not treat as C05 full 4B |

## 8. Score simulation proxy

### P0 — current calibrated proxy

```text
profile_id: P0_e2r_2_1_stock_web_calibrated_proxy
profile_scope: current_global_proxy
changed_axes: none
eligible_trigger_count: 3
avg_MFE_90D_pct: 18.86
avg_MAE_90D_pct: -9.41
false_positive_rate: 0.33
score_return_alignment_verdict: mixed; needs C05-specific margin bridge
```

### P1 — sector-specific candidate

```text
profile_id: P1_L1_EPC_margin_bridge_candidate
profile_scope: L1_INDUSTRIALS_INFRA_DEFENSE_GRID
changed_axes:
  - require direct contract or verified package share
  - require project margin / working-capital bridge before Green
eligible_trigger_count: 2
avg_MFE_90D_pct: 23.17
avg_MAE_90D_pct: -12.27
false_positive_rate: 0.00
score_return_alignment_verdict: better, but still high MAE; do not promote without more rows
```

### P2 — canonical archetype candidate

```text
profile_id: P2_C05_contract_quality_router
profile_scope: C05_EPC_MEGA_CONTRACT_MARGIN_GAP
changed_axes:
  - mega contract headline gives Stage2-Watch
  - Stage2-Actionable requires direct package value and execution visibility
  - Green requires margin bridge, backlog conversion, and working-capital check
eligible_trigger_count: 2
avg_MFE_180D_pct: 27.48
avg_MAE_180D_pct: -13.26
false_positive_rate: 0.00
score_return_alignment_verdict: candidate rule, but no new production delta due small sample
```

### P3 — counterexample guard profile

```text
profile_id: P3_peer_beta_negative_control_guard
profile_scope: C05 negative control
changed_axes:
  - peer beta without direct contract = no C05 Green
  - price-only sector sympathy = watch / narrative-only
eligible_trigger_count: 1
avg_MFE_90D_pct: 10.26
avg_MAE_90D_pct: -3.68
false_positive_rate: 1.00 if treated as direct C05
score_return_alignment_verdict: useful guard
```

## 9. Residual contribution summary

```text
new_independent_case_count: 3
reused_case_count: 0
reused_case_ids: []
new_symbol_count: 3
new_canonical_archetype_count: 0
new_fine_archetype_count: 2
new_trigger_family_count: 3

tested_existing_calibrated_axes:
  - stage2_actionable_evidence_bonus
  - full_4b_requires_non_price_evidence
  - price_only_blowoff_blocks_positive_stage

residual_error_types_found:
  - direct_mega_contract_vs_peer_beta_confusion
  - high_MAE_after_valid_stage2
  - full_4B_must_not_be_price_only
  - contract_headline_without_margin_bridge_should_not_unlock_Green

new_axis_proposed: null
existing_axis_strengthened: full_4b_requires_non_price_evidence; stage2_required_bridge_for_C05_candidate
existing_axis_weakened: null
existing_axis_kept: stage2_actionable_evidence_bonus; price_only_blowoff_blocks_positive_stage

sector_specific_rule_candidate: false
canonical_archetype_rule_candidate: true_but_hold_for_more_evidence
no_new_signal_reason: sample still small and one row is negative-control source_proxy_only

loop_contribution_label: residual_error_found
do_not_propose_new_weight_delta: true
```

## 10. Coverage matrix

| large_sector_id | canonical_archetype_id | fine_archetype_id | positive_case_count | counterexample_count | 4B_case_count | 4C_case_count | new_symbol_count |
|---|---|---|---:|---:|---:|---:|---:|
| L1_INDUSTRIALS_INFRA_DEFENSE_GRID | C05_EPC_MEGA_CONTRACT_MARGIN_GAP | SAUDI_FADHILI_MEGA_EPC_CONTRACT_MARGIN_CONVERSION_BRIDGE | 2 | 1 | 2 | 0 | 3 |

## 11. Deferred Coding Agent Handoff Prompt

```text
Do not execute now.

When batch-applying v12 research artifacts, ingest this MD as a C05 canonical-archetype residual row.
Treat 028050 and 006360 as direct Fadhili mega-EPC rows.
Treat 000720 as a negative-control peer-beta row and do not use it as positive promotion evidence.
Potential safe future rule after more rows:
  For C05_EPC_MEGA_CONTRACT_MARGIN_GAP, direct contract headline may support Stage2-Watch/Actionable,
  but Stage3-Green requires margin bridge, backlog conversion, working-capital evidence, and no execution overhang.
Keep full 4B gated by non-price evidence.
```

## 12. Round state

```text
completed_round = R1
completed_loop = 88
next_round = R2
next_loop = 88
round_schedule_status = valid
round_sector_consistency = pass
```
