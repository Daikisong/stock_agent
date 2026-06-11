# E2R Stock-Web v12 Residual Research — R1 Loop 110 — C04 Nuclear Policy / Project Legal Delay

```text
completed_round = R1
completed_loop = 110
selection_basis = docs/core/V12_Research_No_Repeat_Index.md
selected_priority_bucket = Priority 0
round_schedule_status = coverage_index_selected
round_sector_consistency = pass

large_sector_id = L1_INDUSTRIALS_INFRA_DEFENSE_GRID
canonical_archetype_id = C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY
fine_archetype_id = CZECH_DUKOVANY_PREFERRED_BIDDER_FINAL_CONTRACT_LEGAL_DELAY_VS_SUPPLIER_THEME_SPIKE

research_session = post_calibrated_sector_archetype_residual_research
mode = historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12
price_source = Songdaiki/stock-web
price_basis = tradable_raw
price_adjustment_status = raw_unadjusted_marcap
stock_web_manifest_max_date = 2026-02-20

production_scoring_changed = false
shadow_weight_only = true
stock_agent_code_access_allowed = false
stock_agent_code_patch_allowed = false
handoff_prompt_executed_now = false
```

## 1. Selection and novelty check

`V12_Research_No_Repeat_Index.md` still lists `C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY` as a Priority 0 shortage pocket: 6 representative rows, 24 rows short of 30 and 44 rows short of 50. The current top covered C04 symbols are `046120`, `019990`, `034020`, `083650`, and `126720`; this loop deliberately uses `052690`, `051600`, and `011700` to avoid repeating the existing top-covered C04 symbol set.

Loop selection follows the v12 rule:

```text
selected_loop = max(existing loop for selected_round and selected_canonical_archetype_id) + 1
```

Existing R1/C04 files were found at loops 105, 106, and 109, so this file uses `R1_loop_110`.

## 2. External event basis

The historical policy event is the Czech Dukovany nuclear tender. On 2024-07-17, KHNP was selected as preferred bidder for two Czech nuclear reactors, but the contract was not final at the trigger point and deal completion was still expected later. Later, on 2024-10-31, Czech antitrust proceedings rejected or stopped EDF/Westinghouse appeals, but the decisions were still not final. This makes C04 a clean testbed for separating:

- direct project/service visibility,
- preferred-bidder headline without final contract,
- supplier-theme price spikes without project economics,
- legal challenge / final contract delay risk.

Source URLs used for non-price event context:

```text
https://www.reuters.com/business/energy/south-koreas-winning-bid-czech-nuclear-power-project-2024-07-17/
https://www.reuters.com/business/energy/czech-watchdog-rejects-appeals-nuclear-power-tender-2024-10-31/
https://github.com/Songdaiki/stock-web
https://github.com/Songdaiki/stock_agent/blob/main/docs/core/V12_Research_No_Repeat_Index.md
```

## 3. Price source validation

All trigger rows use `Songdaiki/stock-web` calibration shards:

```text
atlas/ohlcv_tradable_by_symbol_year/052/052690/2024.csv
atlas/ohlcv_tradable_by_symbol_year/052/052690/2025.csv
atlas/ohlcv_tradable_by_symbol_year/051/051600/2024.csv
atlas/ohlcv_tradable_by_symbol_year/051/051600/2025.csv
atlas/ohlcv_tradable_by_symbol_year/011/011700/2024.csv
atlas/ohlcv_tradable_by_symbol_year/011/011700/2025.csv
```

The stock-web manifest reports:

```text
source_name = FinanceData/marcap
price_adjustment_status = raw_unadjusted_marcap
calibration_shard_root = atlas/ohlcv_tradable_by_symbol_year
research_pack_default_price_basis = tradable_raw
max_date = 2026-02-20
```

## 4. Case table

| case_id | symbol | name | entry_date | entry_price | role | MFE_30D | MAE_30D | MFE_90D | MAE_90D | MFE_180D | MAE_180D | interpretation |
|---|---:|---|---|---:|---|---:|---:|---:|---:|---:|---:|---|
| C04-R1L110-A | 052690 | 한전기술 | 2024-07-18 | 82,000 | counterexample / high-MAE direct-scope | 19.63 | -24.88 | 19.63 | -24.88 | 19.63 | -39.94 | Direct engineering-adjacent name did spike on the preferred-bidder headline, but the final-contract/legal-delay bridge was not strong enough for unguarded Stage3. |
| C04-R1L110-B | 051600 | 한전KPS | 2024-07-18 | 38,900 | positive / lower-MAE service visibility | 21.98 | -7.84 | 21.98 | -7.84 | 26.22 | -7.84 | O&M/service-adjacent visibility retained a better risk-adjusted path than pure supplier-theme names. |
| C04-R1L110-C | 011700 | 한신기계 | 2024-07-18 | 4,585 | counterexample / supplier theme decay | 14.94 | -32.82 | 14.94 | -33.91 | 14.94 | -48.53 | Small supplier vocabulary produced a one-day spike but failed the final-contract/cashflow bridge. |

## 5. Trigger rows JSONL

```jsonl
{"MAE_180D_pct": -39.94, "MAE_30D_pct": -24.88, "MAE_90D_pct": -24.88, "MFE_180D_pct": 19.63, "MFE_30D_pct": 19.63, "MFE_90D_pct": 19.63, "calibration_label": "counterexample_current_profile_false_positive", "canonical_archetype_id": "C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY", "case_role": "legal_delay_high_MAE_direct_scope_counterexample", "corporate_action_window_blocked": false, "current_profile_error": true, "dedupe_key": "052690|C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY|Stage2-Actionable|2024-07-18|2024-07-18|preferred_bidder_direct_engineering_scope_but_final_contract_legal_delay", "entry_date": "2024-07-18", "entry_price": 82000, "evidence_as_of_date": "2024-07-18", "fine_archetype_id": "CZECH_DUKOVANY_PREFERRED_BIDDER_FINAL_CONTRACT_LEGAL_DELAY_VS_SUPPLIER_THEME_SPIKE", "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "mae_180d_price": 49250, "mfe_180d_price": 98100, "non_price_evidence_family": "KHNP preferred bidder headline; final contract not yet signed; later appeal/legality path remained material", "price_adjustment_status": "raw_unadjusted_marcap", "price_basis": "tradable_raw", "price_source": "Songdaiki/stock-web", "row_type": "trigger", "schema_family": "v12_sector_archetype_residual", "selected_loop": 110, "selected_round": "R1", "symbol": "052690", "symbol_name": "한전기술", "trigger_family": "preferred_bidder_direct_engineering_scope_but_final_contract_legal_delay", "trigger_type": "Stage2-Actionable"}
{"MAE_180D_pct": -7.84, "MAE_30D_pct": -7.84, "MAE_90D_pct": -7.84, "MFE_180D_pct": 26.22, "MFE_30D_pct": 21.98, "MFE_90D_pct": 21.98, "calibration_label": "positive_profile_alignment", "canonical_archetype_id": "C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY", "case_role": "positive_lower_MAE_project_service_visibility", "corporate_action_window_blocked": false, "current_profile_error": false, "dedupe_key": "051600|C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY|Stage2-Actionable|2024-07-18|2024-07-18|preferred_bidder_OandM_maintenance_visibility_with_lower_drawdown", "entry_date": "2024-07-18", "entry_price": 38900, "evidence_as_of_date": "2024-07-18", "fine_archetype_id": "CZECH_DUKOVANY_PREFERRED_BIDDER_FINAL_CONTRACT_LEGAL_DELAY_VS_SUPPLIER_THEME_SPIKE", "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "mae_180d_price": 35850, "mfe_180d_price": 49100, "non_price_evidence_family": "nuclear project service/O&M adjacency; less pure one-day supplier spike; return path retained despite project legal overhang", "price_adjustment_status": "raw_unadjusted_marcap", "price_basis": "tradable_raw", "price_source": "Songdaiki/stock-web", "row_type": "trigger", "schema_family": "v12_sector_archetype_residual", "selected_loop": 110, "selected_round": "R1", "symbol": "051600", "symbol_name": "한전KPS", "trigger_family": "preferred_bidder_OandM_maintenance_visibility_with_lower_drawdown", "trigger_type": "Stage2-Actionable"}
{"MAE_180D_pct": -48.53, "MAE_30D_pct": -32.82, "MAE_90D_pct": -33.91, "MFE_180D_pct": 14.94, "MFE_30D_pct": 14.94, "MFE_90D_pct": 14.94, "calibration_label": "counterexample_current_profile_false_positive", "canonical_archetype_id": "C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY", "case_role": "supplier_theme_price_only_spike_decay", "corporate_action_window_blocked": false, "current_profile_error": true, "dedupe_key": "011700|C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY|Stage2-Actionable|2024-07-18|2024-07-18|small_supplier_theme_spike_without_final_contract_cash_bridge", "entry_date": "2024-07-18", "entry_price": 4585, "evidence_as_of_date": "2024-07-18", "fine_archetype_id": "CZECH_DUKOVANY_PREFERRED_BIDDER_FINAL_CONTRACT_LEGAL_DELAY_VS_SUPPLIER_THEME_SPIKE", "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "mae_180d_price": 2360, "mfe_180d_price": 5270, "non_price_evidence_family": "nuclear supplier vocabulary; no named project contract/economics; price-only spike quickly decayed", "price_adjustment_status": "raw_unadjusted_marcap", "price_basis": "tradable_raw", "price_source": "Songdaiki/stock-web", "row_type": "trigger", "schema_family": "v12_sector_archetype_residual", "selected_loop": 110, "selected_round": "R1", "symbol": "011700", "symbol_name": "한신기계", "trigger_family": "small_supplier_theme_spike_without_final_contract_cash_bridge", "trigger_type": "Stage2-Actionable"}
```

## 6. Raw component score breakdown

The following numbers are qualitative v12 calibration scores for row-level stress testing, not production changes.

| symbol | EPS/revision | visibility | bottleneck | mispricing | valuation | capital | info/trust | raw_score | profile verdict | return alignment |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|---|
| 052690 | 8 | 17 | 8 | 11 | 7 | 5 | 18 | 74 | Stage2-Actionable but Green blocked | Correct to block Green: 180D MAE reached -39.94%. |
| 051600 | 10 | 18 | 7 | 12 | 9 | 7 | 14 | 77 | Stage2-Actionable / guarded Yellow | Better alignment: 180D MFE 26.22% with MAE only -7.84%. |
| 011700 | 3 | 6 | 5 | 10 | 4 | 2 | 20 | 50 | Theme spike should be capped at Watch/4B | Correct to penalize: 180D MAE reached -48.53%. |

## 7. Score-return alignment

C04 should not treat “preferred bidder” as equivalent to “contracted revenue.” The Czech event behaves like a bridge with a missing center plank:

```text
policy headline -> preferred bidder -> legal/appeal window -> final contract -> named project scope -> revenue/margin/FCF
```

The price path confirms this. The market initially bought the headline across direct and peripheral names, but the divergence appeared quickly:

- `052690` had a large same-day MFE but then a deep 180D drawdown.
- `051600` retained a better path, suggesting service/O&M visibility deserves more credit than supplier vocabulary.
- `011700` was almost a pure nuclear-label spike and should not receive Stage2-Actionable credit without project economics.

## 8. 4B local vs full-window split

| symbol | local 4B proximity | full-window 4B proximity | action |
|---:|---|---|---|
| 052690 | yes — 2024-07-18 spike into 98,100 followed by rapid drawdown | yes — 180D MAE -39.94% | keep Stage2 only if legal/final-contract bridge exists; otherwise cap at Yellow/Watch |
| 051600 | no severe local 4B after entry | no severe full-window 4B; 180D MFE/MAE ratio acceptable | allow guarded Stage2-Actionable |
| 011700 | yes — one-day supplier-theme spike | yes — 180D MAE -48.53% | Stage2 block unless signed project economics appear |

## 9. Residual contribution summary

```text
new_independent_case_count = 3
reused_case_count = 0
same_archetype_new_symbol_count = 3
same_archetype_new_trigger_family_count = 3
calibration_usable_case_count = 3
calibration_usable_trigger_count = 3
positive_case_count = 1
counterexample_count = 2
current_profile_error_count = 2

sector_specific_rule_candidate = false
canonical_archetype_rule_candidate = true
loop_contribution_label = canonical_archetype_rule_candidate

new_axis_proposed = null
existing_axis_strengthened = C04_final_contract_legal_clearance_bridge_requirement; C04_supplier_theme_stage2_block_without_named_project_economics; C04_preferred_bidder_local_4b_watch_guard
existing_axis_weakened = null
do_not_propose_new_weight_delta = false
```

## 10. Shadow rule candidate

No production scoring change is applied in this MD. For later batch implementation only:

```text
if canonical_archetype_id == C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY:
    if evidence == preferred_bidder_headline_only and final_contract_not_signed:
        cap_stage = Stage2-Actionable or Stage3-Yellow
        block_stage3_green = true

    if legal_challenge_or_antitrust_appeal_window_open:
        require contract_closure_or_named_project_scope_before_green = true

    if symbol_role == small_supplier_theme and no named contract/revenue/margin bridge:
        block_stage2_actionable_bonus = true
        classify_as_watch_or_4B_local_if_price_spike_present = true

    if symbol_role == service_OandM_or_engineering_with lower_MAE and durable visibility:
        allow_guarded_stage2 = true
        but require follow-up confirmation before Green
```

## 11. Deferred Coding Agent Handoff Prompt

Do not execute this section in the research runner.

```text
You are the later batch coding agent for stock_agent.

Input artifact:
e2r_stock_web_v12_residual_round_R1_loop_110_L1_INDUSTRIALS_INFRA_DEFENSE_GRID_C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY_research.md

Task:
1. Parse all JSONL rows.
2. Validate that every trigger row contains complete 30/90/180D MFE/MAE fields.
3. Deduplicate by symbol + canonical_archetype_id + trigger_type + entry_date + evidence_family.
4. Treat the shadow rule as candidate-only; do not alter production scoring without aggregate corroboration.
5. Add these rows to v12 calibration ingest only if price_source == Songdaiki/stock-web, price_basis == tradable_raw, and price_adjustment_status == raw_unadjusted_marcap.
6. Preserve the distinction between preferred-bidder headline, final contract/legal clearance, and supplier-theme price spike.
```

## 12. Next research state

```text
completed_round = R1
completed_loop = 110
selection_basis = docs/core/V12_Research_No_Repeat_Index.md
selected_priority_bucket = Priority 0
next_recommended_archetypes = C15_MATERIAL_SPREAD_SUPERCYCLE, C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION, C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN, C22_INSURANCE_RATE_CYCLE_RESERVE, C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT
round_schedule_status = coverage_index_selected
round_sector_consistency = pass
```
