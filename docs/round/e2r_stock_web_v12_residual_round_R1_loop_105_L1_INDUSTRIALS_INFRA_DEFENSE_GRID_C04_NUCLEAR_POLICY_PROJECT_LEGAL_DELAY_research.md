# E2R Stock-Web v12 Residual Research — R1 / Loop 105 / C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY

```yaml
schema_family: v12_sector_archetype_residual
research_session: post_calibrated_sector_archetype_residual_research
mode: historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12
selected_round: R1
selected_loop: 105
large_sector_id: L1_INDUSTRIALS_INFRA_DEFENSE_GRID
canonical_archetype_id: C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY
fine_archetype_id: CZECH_NUCLEAR_PREFERRED_BIDDER_FINAL_CONTRACT_AND_LEGAL_DELAY_BRIDGE_VS_HEADLINE_SPIKE
selection_basis: docs/core/V12_Research_No_Repeat_Index.md
selected_priority_bucket: Priority 1
round_schedule_status: coverage_index_selected
round_sector_consistency: pass
price_source: Songdaiki/stock-web
price_basis: tradable_raw
price_adjustment_status: raw_unadjusted_marcap
stock_web_manifest_max_date: 2026-02-20
live_candidate_mode: false
stock_agent_code_access_allowed: false
stock_agent_code_patch_allowed: false
production_scoring_changed: false
shadow_weight_only: true
handoff_prompt_embedded: true
handoff_prompt_executed_now: false
```

## 1. Why this loop exists

`C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY` is a nuclear policy/project archetype where headline timing and investable timing can diverge sharply. The same project can move through several gates:

1. policy or preferred-bidder headline,
2. rival appeals / technology-license dispute / anti-monopoly review,
3. court or regulator clearance,
4. final contract signing,
5. delivery schedule, localization, financing, and margin bridge.

The July 2024 Czech Dukovany preferred-bidder event moved Korean nuclear names, but several Korean listed beneficiaries gave back the move quickly. The June 2025 signed-contract event created a cleaner positive bridge for the prime equipment beneficiary. This loop therefore tests a C04-specific split:

```text
preferred_bidder_headline_only != final_contract_legal_clearance_bridge
```

## 2. Non-price evidence anchors

- 2024-07-17: Czech Republic selected South Korea's KHNP over EDF as preferred bidder for at least two Dukovany reactors.
- 2024-08-27: EDF and Westinghouse appealed the Czech tender decision; the Westinghouse licensing/export-right dispute became a visible legal-delay risk.
- 2024-10-30: Czech anti-monopoly watchdog temporarily prohibited final contract signing while appeals were pending.
- 2025-06-04: Czech Republic signed the KHNP contract after a court cleared the way.

These anchors are used only to define historical trigger dates. They are not used as live candidate discovery.

## 3. Stock-Web price-source validation

```jsonl
{"row_type":"price_source_validation","symbol":"034020","name":"두산에너빌리티","price_repo":"Songdaiki/stock-web","profile_path":"atlas/symbol_profiles/034/034020.json","year_file":"atlas/ohlcv_tradable_by_symbol_year/034/034020/2025.csv","price_basis":"tradable_raw","adjustment_status":"raw_unadjusted_marcap","corporate_action_window_blocked":false}
{"row_type":"price_source_validation","symbol":"052690","name":"한전기술","price_repo":"Songdaiki/stock-web","profile_path":"atlas/symbol_profiles/052/052690.json","year_file":"atlas/ohlcv_tradable_by_symbol_year/052/052690/2024.csv","price_basis":"tradable_raw","adjustment_status":"raw_unadjusted_marcap","corporate_action_window_blocked":false}
{"row_type":"price_source_validation","symbol":"083650","name":"비에이치아이","price_repo":"Songdaiki/stock-web","profile_path":"atlas/symbol_profiles/083/083650.json","year_file":"atlas/ohlcv_tradable_by_symbol_year/083/083650/2024.csv","price_basis":"tradable_raw","adjustment_status":"raw_unadjusted_marcap","corporate_action_window_blocked":false}
```

## 4. Case set

### Case A — 034020 두산에너빌리티: final-contract legal clearance bridge

```text
symbol: 034020
name: 두산에너빌리티
trigger_date: 2025-06-04
trigger_type: c04_final_contract_legal_clearance
entry_date: 2025-06-04
entry_price: 42650
future_peak_date: 2025-06-30
future_peak_high: 72200
future_trough_date: 2025-06-05
future_trough_low: 43100
MFE_pct: +69.28
MAE_pct: 0.00
classification: positive_with_full_4b_watch
```

The June 2025 event is no longer just a policy headline. A court cleared the way and the Czech-KHNP contract was signed. Doosan Enerbility, as the equipment-heavy Korean nuclear beneficiary, showed a strong price path after this legal-clearance gate: entry close 42,650 on 2025-06-04 and peak high 72,200 on 2025-06-30. The first future low after entry was above entry, so MAE is recorded as 0.00% under close-entry/future-window convention.

```jsonl
{"row_type":"case","case_id":"C04_R1_L105_034020_20250604_FINAL_CONTRACT","symbol":"034020","name":"두산에너빌리티","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY","fine_archetype_id":"CZECH_NUCLEAR_FINAL_CONTRACT_LEGAL_CLEARANCE","trigger_date":"2025-06-04","trigger_type":"c04_final_contract_legal_clearance","entry_date":"2025-06-04","entry_price":42650,"future_peak_date":"2025-06-30","future_peak_high":72200,"future_trough_date":"2025-06-05","future_trough_low":43100,"mfe_pct":69.28,"mae_pct":0.0,"classification":"positive_with_full_4b_watch","current_profile_error":false}
{"row_type":"trigger","case_id":"C04_R1_L105_034020_20250604_FINAL_CONTRACT","symbol":"034020","trigger_family":"final_contract_legal_clearance","evidence_family":"court_clearance_signed_contract","entry_date":"2025-06-04","entry_price":42650,"mfe_pct":69.28,"mae_pct":0.0,"dedupe_key":"C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY|034020|c04_final_contract_legal_clearance|2025-06-04"}
```

### Case B — 052690 한전기술: preferred-bidder headline spike, then legal-delay drawdown

```text
symbol: 052690
name: 한전기술
trigger_date: 2024-07-17
trigger_type: c04_preferred_bidder_headline
entry_date: 2024-07-17
entry_price: 76600
future_peak_date: 2024-07-18
future_peak_high: 98100
future_trough_date: 2024-08-05
future_trough_low: 61600
MFE_pct: +28.07
MAE_pct: -19.58
classification: counterexample_high_MFE_high_MAE_4B_watch
```

The preferred-bidder headline produced a large next-day spike. But before any final contract or legal-clearance bridge existed, the move lacked a stable non-price conversion path. The price path is exactly the C04 trap: MFE was high enough to tempt Stage2/Yellow, but MAE quickly widened to almost -20%.

```jsonl
{"row_type":"case","case_id":"C04_R1_L105_052690_20240717_PREFERRED_BIDDER","symbol":"052690","name":"한전기술","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY","fine_archetype_id":"CZECH_NUCLEAR_PREFERRED_BIDDER_HEADLINE_SPIKE","trigger_date":"2024-07-17","trigger_type":"c04_preferred_bidder_headline","entry_date":"2024-07-17","entry_price":76600,"future_peak_date":"2024-07-18","future_peak_high":98100,"future_trough_date":"2024-08-05","future_trough_low":61600,"mfe_pct":28.07,"mae_pct":-19.58,"classification":"counterexample_high_MFE_high_MAE_4B_watch","current_profile_error":true}
{"row_type":"trigger","case_id":"C04_R1_L105_052690_20240717_PREFERRED_BIDDER","symbol":"052690","trigger_family":"preferred_bidder_headline","evidence_family":"policy_headline_before_final_contract","entry_date":"2024-07-17","entry_price":76600,"mfe_pct":28.07,"mae_pct":-19.58,"dedupe_key":"C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY|052690|c04_preferred_bidder_headline|2024-07-17"}
```

### Case C — 083650 비에이치아이: supplier-theme beta without confirmed contract bridge

```text
symbol: 083650
name: 비에이치아이
trigger_date: 2024-07-17
trigger_type: c04_supplier_theme_headline
entry_date: 2024-07-17
entry_price: 9270
future_peak_date: 2024-07-18
future_peak_high: 10530
future_trough_date: 2024-08-05
future_trough_low: 7100
MFE_pct: +13.59
MAE_pct: -23.41
classification: counterexample_supplier_theme_beta_fade
```

This is the small/mid-cap nuclear supplier version of the same residual error. The headline made the symbol jump, but the company-level bridge from Czech project to signed order/backlog/margin was not visible at trigger time. Price confirmed the weakness: one-day MFE was quickly overwhelmed by a deeper drawdown.

```jsonl
{"row_type":"case","case_id":"C04_R1_L105_083650_20240717_SUPPLIER_THEME","symbol":"083650","name":"비에이치아이","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY","fine_archetype_id":"NUCLEAR_SUPPLIER_THEME_WITHOUT_CONTRACT_BRIDGE","trigger_date":"2024-07-17","trigger_type":"c04_supplier_theme_headline","entry_date":"2024-07-17","entry_price":9270,"future_peak_date":"2024-07-18","future_peak_high":10530,"future_trough_date":"2024-08-05","future_trough_low":7100,"mfe_pct":13.59,"mae_pct":-23.41,"classification":"counterexample_supplier_theme_beta_fade","current_profile_error":true}
{"row_type":"trigger","case_id":"C04_R1_L105_083650_20240717_SUPPLIER_THEME","symbol":"083650","trigger_family":"supplier_theme_headline","evidence_family":"nuclear_policy_supplier_beta_without_order","entry_date":"2024-07-17","entry_price":9270,"mfe_pct":13.59,"mae_pct":-23.41,"dedupe_key":"C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY|083650|c04_supplier_theme_headline|2024-07-17"}
```

## 5. Score simulation

```jsonl
{"row_type":"score_simulation","case_id":"C04_R1_L105_034020_20250604_FINAL_CONTRACT","baseline_stage":"Stage2-Actionable","current_profile_stage":"Stage2-Actionable_to_Stage3-Yellow_watch","proposed_shadow_stage":"Stage2-Actionable_with_full_4B_watch","score_return_alignment":"aligned_positive","raw_component_score_breakdown":{"policy_project":22,"legal_clearance":18,"contract_finality":20,"company_backlog_bridge":14,"margin_visibility":9,"valuation_risk":-6}}
{"row_type":"score_simulation","case_id":"C04_R1_L105_052690_20240717_PREFERRED_BIDDER","baseline_stage":"Stage2-Actionable","current_profile_stage":"Stage2-Actionable_or_Yellow_risk","proposed_shadow_stage":"4B-watch_until_final_contract","score_return_alignment":"misaligned_high_MAE","raw_component_score_breakdown":{"policy_project":22,"legal_clearance":0,"contract_finality":0,"company_backlog_bridge":5,"margin_visibility":2,"valuation_risk":-14}}
{"row_type":"score_simulation","case_id":"C04_R1_L105_083650_20240717_SUPPLIER_THEME","baseline_stage":"Stage2","current_profile_stage":"Stage2-Actionable_risk_from_theme_bonus","proposed_shadow_stage":"4B-watch_theme_only","score_return_alignment":"misaligned_high_MAE","raw_component_score_breakdown":{"policy_project":18,"legal_clearance":0,"contract_finality":0,"company_backlog_bridge":1,"margin_visibility":0,"valuation_risk":-12}}
```

## 6. Aggregate result

```jsonl
{"row_type":"aggregate_metric","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY","loop":105,"case_count":3,"trigger_count":3,"positive_case_count":1,"counterexample_count":2,"current_profile_error_count":2,"median_mfe_pct":28.07,"median_mae_pct":-19.58,"best_mfe_pct":69.28,"worst_mae_pct":-23.41,"residual_pattern":"preferred_bidder_headline_without_final_contract_or_legal_clearance_can_generate_high_MFE_but_wide_MAE"}
```

## 7. Shadow rule candidate

```text
new_axis_proposed:
c04_final_contract_legal_clearance_required_for_stage2_actionable_shadow_only
```

Proposed C04-specific shadow behavior:

1. If evidence is only `preferred_bidder`, `policy headline`, or `MOU`, do not promote beyond Stage2 watch unless there is company-level signed contract / backlog / delivery / margin evidence.
2. If there is active appeal, anti-monopoly review, court injunction, export-license dispute, or technology-license dispute, route to `4B-watch` even when price MFE is high.
3. If final contract is signed after legal clearance and company-level beneficiary path is identifiable, Stage2-Actionable is allowed, but full 4B overlay remains until margin/backlog conversion is visible.
4. Supplier-theme names require stricter company-specific evidence than prime EPC/equipment beneficiaries.

```jsonl
{"row_type":"shadow_weight","axis":"c04_final_contract_legal_clearance_required_for_stage2_actionable_shadow_only","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY","applies_to":["preferred_bidder_headline","policy_headline","MOU","supplier_theme_headline"],"guardrail":"require_final_contract_or_legal_clearance_plus_company_backlog_bridge_before_stage2_actionable","status":"shadow_only","production_scoring_changed":false}
```

## 8. Residual contribution

```jsonl
{"row_type":"residual_contribution","loop":105,"large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY","new_axis_proposed":"c04_final_contract_legal_clearance_required_for_stage2_actionable_shadow_only","existing_axis_strengthened":"full_4b_requires_non_price_evidence scoped to nuclear preferred-bidder and supplier-theme headlines","evidence":"1 positive final-contract/legal-clearance case vs 2 preferred-bidder/supplier-theme high-MAE counterexamples","recommended_next":"C05_EPC_MEGA_CONTRACT_MARGIN_GAP or C15_MATERIAL_SPREAD_SUPERCYCLE"}
```

## 9. Coverage / novelty statement

```jsonl
{"row_type":"coverage_matrix","selected_priority_bucket":"Priority 1","auto_selected_coverage_gap":"C04 rows 31, 50-row target까지 19 부족","new_independent_case_count":3,"reused_case_count":0,"same_archetype_new_symbol_count":3,"same_archetype_new_trigger_family_count":3,"diversity_score_summary":"C04 Priority 1 보강 + final contract legal clearance positive vs preferred-bidder/supplier-theme counterexamples","do_not_propose_new_weight_delta":false}
```

## 10. Deferred Coding Agent Handoff Prompt

```text
Do not execute during research session.

When batching v12 residual MDs into stock_agent, parse this file as a C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY candidate. Consider a shadow-only guardrail named:

c04_final_contract_legal_clearance_required_for_stage2_actionable_shadow_only

Scope:
- large_sector_id: L1_INDUSTRIALS_INFRA_DEFENSE_GRID
- canonical_archetype_id: C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY

Rule candidate:
- preferred-bidder / policy headline / MOU / supplier-theme evidence should remain Stage2-watch or 4B-watch unless final contract, legal clearance, company-level backlog, delivery schedule, or margin bridge is present.
- active appeal, anti-monopoly review, court injunction, export-license dispute, or reactor technology-license dispute should suppress Stage2-Actionable and Stage3-Yellow promotion.
- signed final contract after legal clearance may allow Stage2-Actionable, but full 4B overlay remains until backlog/margin conversion is visible.
```

## 11. Final machine-readable summary

```jsonl
{"row_type":"narrative_only","filename":"e2r_stock_web_v12_residual_round_R1_loop_105_L1_INDUSTRIALS_INFRA_DEFENSE_GRID_C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY_research.md","selected_round":"R1","selected_loop":105,"large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY","fine_archetype_id":"CZECH_NUCLEAR_PREFERRED_BIDDER_FINAL_CONTRACT_AND_LEGAL_DELAY_BRIDGE_VS_HEADLINE_SPIKE","new_independent_case_count":3,"reused_case_count":0,"calibration_usable_case_count":3,"calibration_usable_trigger_count":3,"positive_case_count":1,"counterexample_count":2,"current_profile_error_count":2,"new_axis_proposed":"c04_final_contract_legal_clearance_required_for_stage2_actionable_shadow_only","existing_axis_strengthened":"full_4b_requires_non_price_evidence scoped to nuclear preferred-bidder and supplier-theme headlines","next_recommended_archetypes":["C05_EPC_MEGA_CONTRACT_MARGIN_GAP","C15_MATERIAL_SPREAD_SUPERCYCLE","C18_CONSUMER_EXPORT_CHANNEL_REORDER"]}
```
