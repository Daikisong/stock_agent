# stock-web v12 residual calibration research

```text
filename = e2r_stock_web_v12_residual_round_R1_loop_109_L1_INDUSTRIALS_INFRA_DEFENSE_GRID_C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY_research.md
mode = historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12
research_session = post_calibrated_sector_archetype_residual_research
selected_round = R1
selected_loop = 109
large_sector_id = L1_INDUSTRIALS_INFRA_DEFENSE_GRID
canonical_archetype_id = C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY
fine_archetype_id = NUCLEAR_FINAL_CONTRACT_LEGAL_CLEARANCE_PARENT_SCOPE_AND_OM_BRIDGE_VS_SMALL_SUPPLIER_THEME_FALSE_POSITIVE
shadow_weight_only = true
production_scoring_changed = false
handoff_prompt_embedded = true
handoff_prompt_executed_now = false
```

## 0. Guardrail compliance

This is not a coding run, not a live-stock discovery run, and not a production scoring patch.

The only intended output is this standalone historical calibration / sector-archetype residual research Markdown file. `stock_agent` code was not opened or inferred. `Songdaiki/stock-web` was used only as the committed OHLCV price atlas. `stock_agent` research artifacts were used only for no-repeat and coverage-gap awareness.

## 1. Selection rationale

`C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY` remains a Priority 1 coverage gap in `V12_Research_No_Repeat_Index.md`: 31 rows, 19 rows still needed to reach the 50-row practical calibration target. The stated research point is: separate preferred-bidder / policy headline from final contract / legal-delay resolution.

Prior C04 runs already used:

- Doosan Enerbility / KEPCO Engineering / BHI around the Czech preferred-bidder and final-contract sequence.
- KEPCO KPS / Woojin / Iljin Power around the same Czech event structure.

This run avoids those symbols and uses a fresh set:

- `015760` Korea Electric Power / KEPCO: KHNP parent-level read-through after final Czech contract and legal clearance.
- `130660` KEPCO Industrial Development / HanJeon Industrial: O&M / power-plant service theme with final-contract read-through and liquidity watch.
- `006910` Boseong Powertec: small nuclear supplier-theme counterexample around 2024 preferred-bidder headline.
- `032820` Woori Technology: nuclear control-system / small supplier-theme counterexample around 2024 preferred-bidder headline.

## 2. Price atlas basis

```text
price_repo = Songdaiki/stock-web
price_basis = tradable_raw
calibration_shard_root = atlas/ohlcv_tradable_by_symbol_year
source_name = FinanceData/marcap
price_adjustment_status = raw_unadjusted_marcap
max_date = 2026-02-20
corporate_action_contaminated_windows = blocked_by_default
```

Profiles checked:

- `015760` KEPCO: no corporate-action candidate in current profile; calibration usable.
- `130660` HanJeon Industrial: no corporate-action candidate in current profile; calibration usable.
- `006910` Boseong Powertec: historical corporate-action candidates exist, but not in the 2024 trigger window; calibration usable for this window with caveat.
- `032820` Woori Technology: historical corporate-action candidates exist, but not in the 2024 trigger window; calibration usable for this window with caveat.

## 3. External event spine

### 3.1 2024-07-17 Czech preferred-bidder headline

In July 2024, the Czech government selected South Korea's KHNP over France's EDF for the Dukovany nuclear tender. This was a powerful headline but not a final construction contract. Later Reuters coverage records that EDF and Westinghouse appealed the decision and that legal challenges remained part of the event path.

Calibration implication: before final contract and legal clearance, this belongs to `preferred_bidder_headline_watch`, not clean Stage3-Green evidence.

### 3.2 2025-05 to 2025-06 legal delay and final signing

On 2025-05-06, a Czech court blocked the signing of the contract with KHNP after EDF challenged the process. On 2025-06-04, the Czech government signed the deal with KHNP after an appeals court cleared the way. AP described the agreement as two new Dukovany reactors, with contract value around CZK 407bn / USD 18.7bn.

Calibration implication: `final_contract_signed_after_legal_clearance` is a materially stronger C04 gate than `preferred_bidder_selected`.

## 4. Case matrix

| case_id | symbol | company | trigger_date | trigger_type | entry_date | entry_price | peak_date | peak_high | trough_date | trough_low | MFE | MAE | classification |
|---|---:|---|---|---|---|---:|---|---:|---|---:|---:|---:|---|
| C04_R1L109_001 | 015760 | 한국전력 | 2025-06-04 | final_contract_legal_clearance_parent_readthrough | 2025-06-04 | 29,650 | 2026-01-21 | 69,500 | 2025-06-10 | 26,700 | +134.40% | -9.95% | positive_with_full_4B_parent_policy_watch |
| C04_R1L109_002 | 130660 | 한전산업 | 2025-06-04 | final_contract_legal_clearance_om_service_readthrough | 2025-06-04 | 11,400 | 2026-02-20 | 27,800 | 2026-01-09 | 10,150 | +143.86% | -10.96% | delayed_positive_liquidity_full_4B_watch |
| C04_R1L109_003 | 006910 | 보성파워텍 | 2024-07-17 | preferred_bidder_small_supplier_theme | 2024-07-17 | 3,625 | 2024-07-18 | 4,280 | 2024-08-05 | 2,560 | +18.07% | -29.38% | counterexample_preferred_bidder_supplier_theme_fade |
| C04_R1L109_004 | 032820 | 우리기술 | 2024-07-17 | preferred_bidder_control_system_supplier_theme | 2024-07-17 | 2,645 | 2024-07-18 | 3,300 | 2024-08-05 | 1,800 | +24.76% | -31.95% | counterexample_preferred_bidder_control_theme_fade |

Formula:

```text
MFE = (forward_peak_high - entry_close) / entry_close
MAE = (forward_trough_low - entry_close) / entry_close
```

## 5. Case notes

### 5.1 KEPCO / 015760 — final legal clearance parent bridge

KHNP is a KEPCO subsidiary, so the Czech final contract has a cleaner parent-level read-through than a generic nuclear equipment theme. The 2025-06-04 final-signing date is qualitatively different from the 2024 preferred-bidder date because the legal block was cleared and the contract was actually signed.

Price path:

- Entry: 2025-06-04 close 29,650.
- Early drawdown: 2025-06-10 low 26,700, MAE -9.95%.
- Full-window peak: 2026-01-21 high 69,500, MFE +134.40%.

Interpretation:

- Positive for C04, but not automatically clean Stage3-Green because KEPCO also carries broad regulated-utility, tariff, political, and power-policy beta.
- Best label: `positive_with_full_4B_parent_policy_watch`.
- Shadow rule: final-contract legal clearance can lift C04 score materially, but parent-company mapping and non-nuclear contamination should be tagged explicitly.

### 5.2 HanJeon Industrial / 130660 — O&M/service read-through with liquidity watch

HanJeon Industrial is not the direct Czech contract winner. The run treats it as an O&M / power-plant service read-through case around the legally cleared final contract.

Price path:

- Entry: 2025-06-04 close 11,400.
- Local post-event breakout: 2025-06-25 high 16,990, local MFE +49.04%.
- Full-window peak: 2026-02-20 high 27,800, full MFE +143.86%.
- Full-window trough: 2026-01-09 low 10,150, MAE -10.96%.

Interpretation:

- Positive, but the full-window high arrives much later and may contain fresh theme/liquidity/policy contamination.
- Best label: `delayed_positive_liquidity_full_4B_watch`.
- Shadow rule: O&M/service read-through is Stage2-Actionable only if the firm has explicit scope/backlog or recurring service visibility; otherwise keep as 4B watch.

### 5.3 Boseong Powertec / 006910 — preferred-bidder supplier-theme fade

Boseong Powertec is a small nuclear-theme supplier read-through. The 2024-07-17 preferred-bidder headline produced a one-day spike, but the move failed quickly.

Price path:

- Entry: 2024-07-17 close 3,625.
- Peak: 2024-07-18 high 4,280, MFE +18.07%.
- Trough: 2024-08-05 low 2,560, MAE -29.38%.

Interpretation:

- Counterexample: preferred-bidder headline + small supplier theme is not enough for C04 Stage3.
- This should be treated as `supplier_theme_4B_or_4C_watch` unless company-specific scope/backlog appears.

### 5.4 Woori Technology / 032820 — control-system theme fade

Woori Technology has a stronger “nuclear control system” narrative than a generic parts name, but the 2024 preferred-bidder price path still behaved like theme beta.

Price path:

- Entry: 2024-07-17 close 2,645.
- Peak: 2024-07-18 high 3,300, MFE +24.76%.
- Trough: 2024-08-05 low 1,800, MAE -31.95%.

Interpretation:

- Counterexample: control-system label without explicit Czech scope/backlog still fades like supplier-theme beta.
- This strengthens the hard split between `final_contract_legal_clearance` and `preferred_bidder_supplier_readthrough`.

## 6. Residual error diagnosis

The residual error is not that the model misses nuclear headlines. It is that it can still over-credit the *shape* of the headline:

```text
preferred bidder headline
  != final signed contract
  != legal risk cleared
  != company-specific scope
  != backlog / margin conversion
```

For C04, price action behaves like a bridge with three locks:

1. **Legal lock** — EDF / Westinghouse / court / competition objections must be cleared or discounted.
2. **Contract lock** — preferred bidder is weaker than signed final contract.
3. **Scope lock** — direct contract, parent/subsidiary mapping, O&M scope, or named supplier backlog must be visible.

If any lock is missing, a headline can still generate a fast MFE spike, but the cases show MAE can quickly become large.

## 7. Proposed shadow rule

```text
rule_id = c04_final_contract_legal_clearance_scope_bridge_required_shadow_only
status = proposed_shadow_only
production_change_now = false
```

### 7.1 Positive score lift

Apply C04 positive lift only when at least one of the following is present:

```text
- final_contract_signed = true
- court_injunction_or_major_appeal_cleared = true
- direct_contract_counterparty_or_parent_mapping = true
- explicit company-level scope / O&M / supply / service backlog = true
```

### 7.2 Preferred-bidder haircut

For `preferred_bidder_selected` without final contract:

```text
stage_cap = Stage2-Actionable max
stage3_green_allowed = false
legal_delay_haircut = required
small_supplier_theme_multiplier = <= 0.45
```

### 7.3 Supplier theme reject / watch condition

For small nuclear-theme suppliers:

```text
if no company_specific_scope and no signed_backlog:
    classify_as = 4B_watch_or_4C_counterexample
    do_not_use_price_spike_as_green_evidence = true
```

## 8. Machine-readable rows

### case rows

```jsonl
{"row_type":"case","case_id":"C04_R1L109_001","round":"R1","loop":109,"large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY","fine_archetype_id":"NUCLEAR_FINAL_CONTRACT_LEGAL_CLEARANCE_PARENT_SCOPE_AND_OM_BRIDGE_VS_SMALL_SUPPLIER_THEME_FALSE_POSITIVE","symbol":"015760","company":"한국전력","trigger_date":"2025-06-04","entry_date":"2025-06-04","entry_price":29650,"peak_date":"2026-01-21","peak_high":69500,"trough_date":"2025-06-10","trough_low":26700,"mfe_pct":134.40,"mae_pct":-9.95,"classification":"positive_with_full_4B_parent_policy_watch","calibration_usable":true,"source_url":"https://apnews.com/article/3e411cd3693ee4f0c4ecf4fe1d0f799f"}
{"row_type":"case","case_id":"C04_R1L109_002","round":"R1","loop":109,"large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY","fine_archetype_id":"NUCLEAR_FINAL_CONTRACT_LEGAL_CLEARANCE_PARENT_SCOPE_AND_OM_BRIDGE_VS_SMALL_SUPPLIER_THEME_FALSE_POSITIVE","symbol":"130660","company":"한전산업","trigger_date":"2025-06-04","entry_date":"2025-06-04","entry_price":11400,"peak_date":"2026-02-20","peak_high":27800,"trough_date":"2026-01-09","trough_low":10150,"mfe_pct":143.86,"mae_pct":-10.96,"classification":"delayed_positive_liquidity_full_4B_watch","calibration_usable":true,"source_url":"https://apnews.com/article/3e411cd3693ee4f0c4ecf4fe1d0f799f"}
{"row_type":"case","case_id":"C04_R1L109_003","round":"R1","loop":109,"large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY","fine_archetype_id":"NUCLEAR_FINAL_CONTRACT_LEGAL_CLEARANCE_PARENT_SCOPE_AND_OM_BRIDGE_VS_SMALL_SUPPLIER_THEME_FALSE_POSITIVE","symbol":"006910","company":"보성파워텍","trigger_date":"2024-07-17","entry_date":"2024-07-17","entry_price":3625,"peak_date":"2024-07-18","peak_high":4280,"trough_date":"2024-08-05","trough_low":2560,"mfe_pct":18.07,"mae_pct":-29.38,"classification":"counterexample_preferred_bidder_supplier_theme_fade","calibration_usable":true,"source_url":"https://www.reuters.com/business/energy/edf-westinghouse-appeal-against-czech-nuclear-tender-2024-08-27/"}
{"row_type":"case","case_id":"C04_R1L109_004","round":"R1","loop":109,"large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY","fine_archetype_id":"NUCLEAR_FINAL_CONTRACT_LEGAL_CLEARANCE_PARENT_SCOPE_AND_OM_BRIDGE_VS_SMALL_SUPPLIER_THEME_FALSE_POSITIVE","symbol":"032820","company":"우리기술","trigger_date":"2024-07-17","entry_date":"2024-07-17","entry_price":2645,"peak_date":"2024-07-18","peak_high":3300,"trough_date":"2024-08-05","trough_low":1800,"mfe_pct":24.76,"mae_pct":-31.95,"classification":"counterexample_preferred_bidder_control_theme_fade","calibration_usable":true,"source_url":"https://www.reuters.com/business/energy/edf-westinghouse-appeal-against-czech-nuclear-tender-2024-08-27/"}
```

### score_simulation rows

```jsonl
{"row_type":"score_simulation","rule_id":"c04_final_contract_legal_clearance_scope_bridge_required_shadow_only","case_id":"C04_R1L109_001","old_behavior":"parent nuclear read-through may be under-separated from generic utility beta","new_behavior":"allow C04 positive lift but tag parent_policy_4B_watch","expected_error_delta":"reduce false negative without allowing generic nuclear-theme green"}
{"row_type":"score_simulation","rule_id":"c04_final_contract_legal_clearance_scope_bridge_required_shadow_only","case_id":"C04_R1L109_002","old_behavior":"O&M/service read-through may be over-promoted after delayed full-window rally","new_behavior":"Stage2-Actionable watch only unless explicit O&M scope/backlog is verified","expected_error_delta":"reduce late-theme contamination"}
{"row_type":"score_simulation","rule_id":"c04_final_contract_legal_clearance_scope_bridge_required_shadow_only","case_id":"C04_R1L109_003","old_behavior":"small supplier preferred-bidder spike can look like actionable nuclear evidence","new_behavior":"cap at Stage2, usually 4B/4C unless company scope appears","expected_error_delta":"reduce high-MAE false positives"}
{"row_type":"score_simulation","rule_id":"c04_final_contract_legal_clearance_scope_bridge_required_shadow_only","case_id":"C04_R1L109_004","old_behavior":"control-system label can be over-weighted as if direct project scope were confirmed","new_behavior":"require explicit signed scope/backlog before Stage3","expected_error_delta":"reduce high-MAE control-theme false positives"}
```

### aggregate row

```jsonl
{"row_type":"aggregate","round":"R1","loop":109,"large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY","new_independent_case_count":4,"reused_case_count":0,"same_archetype_new_symbol_count":4,"calibration_usable_case_count":4,"positive_case_count":2,"counterexample_count":2,"current_profile_error_count":3,"sector_specific_rule_candidate":true,"canonical_archetype_rule_candidate":true,"loop_contribution_label":"canonical_archetype_rule_candidate"}
```

### shadow_weight row

```jsonl
{"row_type":"shadow_weight","rule_id":"c04_final_contract_legal_clearance_scope_bridge_required_shadow_only","production_scoring_changed":false,"positive_lift_condition":"final contract signed + legal clearance + direct/parent/O&M/scope bridge","haircut_condition":"preferred bidder only, pending appeal, small supplier theme, no explicit company scope","stage_cap_for_supplier_theme":"Stage2-Actionable max; often 4B/4C watch"}
```

## 9. Deferred Coding Agent Handoff Prompt

Do not execute this prompt in the current research session.

```text
You are a coding agent working on Songdaiki/stock_agent.

Batch-ingest this standalone v12 residual research Markdown as evidence for C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY. Do not treat it as production truth by itself. Convert only the machine-readable JSONL rows into candidate registry rows. Preserve `shadow_weight_only=true`.

Candidate shadow rule:
- id: c04_final_contract_legal_clearance_scope_bridge_required_shadow_only
- apply only to C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY
- positive lift requires final contract signed, legal injunction/appeal cleared, and direct/parent/O&M/scope bridge.
- preferred-bidder-only headlines must receive legal-delay haircut and Stage3-Green block.
- small supplier / control-system theme names require explicit signed scope/backlog; otherwise classify as 4B/4C watch.

Do not patch production scoring until this rule is batch-tested across the complete C04 registry and against C03/C05 adjacent industrial archetypes.
```

## 10. Final metadata

```text
selected_round = R1
selected_loop = 109
selection_basis = docs/core/V12_Research_No_Repeat_Index.md
selected_priority_bucket = Priority 1
round_schedule_status = coverage_index_selected
round_sector_consistency = pass
large_sector_id = L1_INDUSTRIALS_INFRA_DEFENSE_GRID
canonical_archetype_id = C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY
fine_archetype_id = NUCLEAR_FINAL_CONTRACT_LEGAL_CLEARANCE_PARENT_SCOPE_AND_OM_BRIDGE_VS_SMALL_SUPPLIER_THEME_FALSE_POSITIVE

new_independent_case_count = 4
reused_case_count = 0
same_archetype_new_symbol_count = 4
same_archetype_new_trigger_family_count = 3
calibration_usable case 수 = 4
calibration_usable trigger 수 = 4
positive_case_count = 2
counterexample_count = 2
current_profile_error_count = 3
verified_url_repair_needed_count = 2

diversity_score_summary = C04 Priority 1 보강 + KEPCO final-contract parent positive + HanJeon Industrial O&M/service delayed positive/full-4B watch + Boseong/Woori small supplier-theme high-MAE counterexamples
do_not_propose_new_weight_delta = false
auto_selected_coverage_gap = C04 rows 31, 50-row target까지 19 부족
sector_specific_rule_candidate = true
canonical_archetype_rule_candidate = true
loop_contribution_label = canonical_archetype_rule_candidate
new_axis_proposed = c04_final_contract_legal_clearance_scope_bridge_required_shadow_only
existing_axis_strengthened = full_4b_requires_non_price_evidence scoped to C04 nuclear preferred-bidder / supplier-theme rallies
existing_axis_weakened = null
next_recommended_archetypes = C05_EPC_MEGA_CONTRACT_MARGIN_GAP, C15_MATERIAL_SPREAD_SUPERCYCLE, C18_CONSUMER_EXPORT_CHANNEL_REORDER
```
