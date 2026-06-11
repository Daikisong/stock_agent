# E2R Stock-Web V12 Residual Research — R3 / Loop 107 / C13_BATTERY_JV_UTILIZATION_AMPC_IRA

```yaml
mode: historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12
research_session: post_calibrated_sector_archetype_residual_research
selected_round: R3
selected_loop: 107
large_sector_id: L3_BATTERY_EV_MOBILITY
canonical_archetype_id: C13_BATTERY_JV_UTILIZATION_AMPC_IRA
fine_archetype_id: IRA_FEOC_JV_FINANCING_AND_AMPC_UTILIZATION_BRIDGE_VS_LOCALIZATION_LABEL_HIGH_MAE_FADE
selection_basis: docs/core/V12_Research_No_Repeat_Index.md
selected_priority_bucket: Priority 0
round_schedule_status: coverage_index_selected
round_sector_consistency: pass
stock_agent_code_access_allowed: false
stock_agent_code_patch_allowed: false
production_scoring_changed: false
shadow_weight_only: true
stock_web_price_atlas_access_required: true
price_basis: tradable_raw
```

## 1. Execution boundary

This run follows the v12 execution boundary: the only output is a standalone historical calibration / sector-archetype residual research Markdown file. It does not open or patch `stock_agent` code, does not perform live discovery, and does not alter production scoring. The only allowed repository reads are coverage / duplicate avoidance artifacts from `stock_agent` and price rows from `Songdaiki/stock-web`.

## 2. Coverage and duplicate rationale

`C13_BATTERY_JV_UTILIZATION_AMPC_IRA` is still a Priority 0 archetype in the No-Repeat ledger: 27 rows, 17 symbols, 30-row stability target still short by 3 rows, 50-row practical calibration target still short by 23 rows.

Existing top-covered C13 symbols are concentrated in direct cell/JV names: `373220`, `393890`, `006400`, `014820`, `051910`, `096770`. This run therefore uses a mixed bridge set:

- `006400` Samsung SDI only because the trigger family is a distinct StarPlus DOE-loan/JV financing event.
- `348370` Enchem as electrolyte/localization/IRA beneficiary label.
- `247540` EcoPro BM as cathode-localization / SK On-Ford-EcoPro JV read-through.
- `020150` Lotte Energy Materials as copper-foil / midchain localization label.

The purpose is not to repeat generic “battery positive” evidence. The purpose is to separate:

```text
IRA/AMPC/JV label
  → actual JV ramp and plant utilization
  → AMPC / subsidy capture
  → shipment, gross margin, FCF, revision bridge
```

from:

```text
battery localization vocabulary
  → short beta rally
  → EV demand / utilization / customer call-off / subsidy uncertainty
  → high-MAE fade
```

## 3. Price atlas provenance

The run uses `Songdaiki/stock-web` calibration shards:

```yaml
source_name: FinanceData/marcap
price_adjustment_status: raw_unadjusted_marcap
max_date: 2026-02-20
calibration_shard_root: atlas/ohlcv_tradable_by_symbol_year
research_pack_default_price_basis: tradable_raw
```

Atlas caveat: zero-volume and invalid OHLC rows are excluded from calibration shards; corporate-action-contaminated windows are blocked by default. Raw OHLC is unadjusted unless explicitly added later.

## 4. Evidence spine

### 4.1 IRA / FEOC rule bridge

The 2024 final U.S. EV tax credit rules kept the IRA battery sourcing / FEOC framework but provided flexibility such as extra time for graphite sourcing. This is a useful trigger for C13 because it can create an equity reflex in Korea-listed battery materials, electrolyte, cathode, and copper-foil names. However, it should not be scored as a clean positive unless the company has real local production, JV utilization, AMPC capture, or customer shipment evidence.

### 4.2 JV-financing bridge

The 2024-12-02 DOE conditional commitment for the Stellantis–Samsung SDI StarPlus Energy JV was a direct battery JV financing event. It is a clean C13 test: large financing headline, identifiable JV, clear planned capacity. Yet the stock path shows that financing vocabulary alone did not create durable rerating without a visible utilization / demand / margin bridge.

### 4.3 JV reset / utilization risk

The later Ford–SK On JV reset confirms the core C13 failure mode: U.S. battery JVs can be real assets but still require demand visibility, ownership economics, utilization, and subsidy durability. JV formation is a door; it is not the destination.

## 5. Case table

| case_id | symbol | name | trigger_date | trigger_family | entry_date | entry_close | peak_high | trough_low | MFE | MAE | classification |
|---|---:|---|---|---|---|---:|---:|---:|---:|---:|---|
| C13-107-01 | 006400 | Samsung SDI | 2024-12-02 | StarPlus DOE-loan / JV financing | 2024-12-02 | 259,000 | 268,000 | 169,700 | +3.47% | -34.48% | hard counterexample |
| C13-107-02 | 348370 | Enchem | 2024-05-03 | IRA FEOC final rule / electrolyte localization | 2024-05-03 | 270,000 | 342,500 | 108,000 | +26.85% | -60.00% | high-MFE / high-MAE counterexample |
| C13-107-03 | 247540 | EcoPro BM | 2024-05-03 | IRA localization + cathode JV read-through | 2024-05-03 | 226,000 | 239,000 | 120,400 | +5.75% | -46.73% | cathode-JV label false positive |
| C13-107-04 | 020150 | Lotte Energy Materials | 2024-05-03 | copper-foil / local-content label | 2024-05-03 | 44,800 | 59,200 | 20,900 | +32.14% | -53.35% | midchain high-MFE / hard-fade counterexample |

## 6. Case notes

### C13-107-01 — Samsung SDI / StarPlus DOE loan

- Symbol profile confirms Samsung SDI as active-like KOSPI and usable in the 2024/2025 calibration window.
- Trigger: 2024-12-02 DOE proposed loan of up to $7.54B to the Stellantis–Samsung SDI StarPlus Energy JV.
- Price route:
  - Entry: 2024-12-02 close 259,000.
  - Peak: 2024-12-16 high 268,000.
  - Trough: 2025-07-09 low 169,700.
  - MFE +3.47%, MAE -34.48%.

Interpretation: This is a direct C13 event, but the equity route failed. A JV financing headline does not automatically mean Stage2-Actionable, because the missing bridge is utilization, EV demand, subsidy durability, and margin conversion.

### C13-107-02 — Enchem / electrolyte localization

- Symbol profile confirms Enchem as active-like KOSDAQ, no corporate-action block in the relevant 2024 window.
- Trigger: 2024-05-03 IRA final-rule / FEOC-localization rule context.
- Price route:
  - Entry: 2024-05-03 close 270,000.
  - Peak: 2024-05-21 high 342,500.
  - Trough: 2024-11-15 low 108,000.
  - MFE +26.85%, MAE -60.00%.

Interpretation: The stock had a strong localization / electrolyte beta response, but the later collapse shows why C13 must require company-specific offtake, local production, customer ramp, AMPC/subsidy accounting, and margin evidence.

### C13-107-03 — EcoPro BM / cathode JV read-through

- Symbol profile confirms EcoPro BM as active-like KOSDAQ GLOBAL, with earlier corporate-action candidates blocked before 2024.
- Trigger: 2024-05-03 IRA final-rule context plus previously established SK On–Ford–EcoPro BM cathode-localization JV exposure.
- Price route:
  - Entry: 2024-05-03 close 226,000.
  - Peak: 2024-05-03 high 239,000.
  - Trough: 2024-11-15 low 120,400.
  - MFE +5.75%, MAE -46.73%.

Interpretation: Cathode JV / localization vocabulary was not enough. This is a clean false positive unless the model sees confirmed plant timing, customer order pull, utilization, spread, and earnings revision.

### C13-107-04 — Lotte Energy Materials / copper-foil localization label

- Symbol profile confirms Lotte Energy Materials as active-like KOSPI, no corporate-action block in 2024.
- Trigger: 2024-05-03 IRA final-rule / local-content read-through.
- Price route:
  - Entry: 2024-05-03 close 44,800.
  - Peak: 2024-06-18 high 59,200.
  - Trough: 2024-12-09 low 20,900.
  - MFE +32.14%, MAE -53.35%.

Interpretation: Copper-foil / battery-material localization can produce a tradable 4B rally, but the full-window path turns into a severe fade when customer call-off, utilization, and margin evidence are absent.

## 7. Residual error pattern

Current profile likely over-rewards the following phrases:

```text
- IRA beneficiary
- AMPC beneficiary
- U.S. battery JV
- local content
- Korean battery supply chain
- cathode / electrolyte / copper foil localization
```

The residual error is not that these phrases are irrelevant. The error is that they are upstream nouns. A scoring model must wait for the verbs:

```text
- plant started production
- utilization rising
- AMPC recognized in earnings
- shipment volume confirmed
- customer offtake firm
- gross margin / OPM revised upward
- FCF bridge visible
```

Without those verbs, C13 cases often become Stage4B or Stage4C.

## 8. Shadow rule candidate

```yaml
shadow_rule_id: c13_jv_ampc_utilization_bridge_required_v1
scope:
  large_sector_id: L3_BATTERY_EV_MOBILITY
  canonical_archetype_id: C13_BATTERY_JV_UTILIZATION_AMPC_IRA
rule_type: penalty_and_bridge_requirement
intent: prevent_Stage2_or_Stage3_upgrade_from_IRA_JV_AMPC_label_only
positive_bridge_required:
  any_2_of:
    - confirmed_JV_production_start_or_capacity_ramp
    - utilization_or_customer_pull_evidence
    - AMPC_or_subsidy_recognition_in_reported_earnings
    - firm_customer_volume_or_of_take_schedule
    - OPM_or_gross_margin_revision
    - FCF_or_working_capital_improvement
penalty_triggers:
  - localization_label_only
  - IRA_AMPC_beneficiary_without_recognized_credit_or_volume
  - JV_financing_without_utilization_schedule
  - midchain_material_readthrough_without_customer_specific_evidence
  - EV_demand_slowdown_or_customer_calloff_present
stage_effect:
  if label_only_and_no_bridge: cap_at_Stage4B_watch
  if label_only_and_MAE_gt_25pct: downgrade_to_Stage4C_candidate
  if direct_JV_financing_but_no_utilization_and_MAE_gt_20pct: block_Stage2_Actionable
  if AMPC_recognition_and_utilization_confirmed: allow_Stage2_Actionable_review
```

## 9. Machine-readable rows

```jsonl
{"row_type":"case","case_id":"C13-107-01","symbol":"006400","name":"삼성SDI","canonical_archetype_id":"C13_BATTERY_JV_UTILIZATION_AMPC_IRA","trigger_date":"2024-12-02","entry_date":"2024-12-02","entry_price":259000,"peak_high":268000,"trough_low":169700,"mfe_pct":3.47,"mae_pct":-34.48,"classification":"hard_counterexample","bridge_missing":["JV_utilization","EV_demand","margin_revision","subsidy_durability"],"usable_for_shadow_rule":true}
{"row_type":"case","case_id":"C13-107-02","symbol":"348370","name":"엔켐","canonical_archetype_id":"C13_BATTERY_JV_UTILIZATION_AMPC_IRA","trigger_date":"2024-05-03","entry_date":"2024-05-03","entry_price":270000,"peak_high":342500,"trough_low":108000,"mfe_pct":26.85,"mae_pct":-60.00,"classification":"high_mfe_high_mae_counterexample","bridge_missing":["confirmed_customer_offtake","recognized_AMPC","utilization","margin_revision"],"usable_for_shadow_rule":true}
{"row_type":"case","case_id":"C13-107-03","symbol":"247540","name":"에코프로비엠","canonical_archetype_id":"C13_BATTERY_JV_UTILIZATION_AMPC_IRA","trigger_date":"2024-05-03","entry_date":"2024-05-03","entry_price":226000,"peak_high":239000,"trough_low":120400,"mfe_pct":5.75,"mae_pct":-46.73,"classification":"cathode_JV_label_false_positive","bridge_missing":["JV_utilization","customer_ramp","spread_margin","revision"],"usable_for_shadow_rule":true}
{"row_type":"case","case_id":"C13-107-04","symbol":"020150","name":"롯데에너지머티리얼즈","canonical_archetype_id":"C13_BATTERY_JV_UTILIZATION_AMPC_IRA","trigger_date":"2024-05-03","entry_date":"2024-05-03","entry_price":44800,"peak_high":59200,"trough_low":20900,"mfe_pct":32.14,"mae_pct":-53.35,"classification":"midchain_localization_label_high_mfe_hard_fade","bridge_missing":["direct_customer_program","utilization","margin_revision","FCF"],"usable_for_shadow_rule":true}
{"row_type":"aggregate","canonical_archetype_id":"C13_BATTERY_JV_UTILIZATION_AMPC_IRA","case_count":4,"positive_case_count":0,"counterexample_count":4,"hard_4c_candidate_count":3,"boundary_case_count":1,"new_axis_proposed":"c13_jv_ampc_utilization_bridge_required_v1","production_scoring_changed":false,"shadow_weight_only":true}
```

## 10. Deferred Coding Agent Handoff Prompt

```text
You are the coding agent for Songdaiki/stock_agent.

Do not treat this research MD as an immediate production patch. Batch it with other v12 residual MDs.

Research artifact:
- e2r_stock_web_v12_residual_round_R3_loop_107_L3_BATTERY_EV_MOBILITY_C13_BATTERY_JV_UTILIZATION_AMPC_IRA_research.md

Extract only machine-readable rows with row_type in:
- case
- aggregate
- shadow_weight
- residual_contribution

Candidate rule:
- c13_jv_ampc_utilization_bridge_required_v1

Implement only as shadow/scoring-simulation if enough corroborating C13 research artifacts agree. Do not change production scoring from this single MD alone.

Guardrail:
- IRA / AMPC / JV / localization labels alone must not promote to Stage2-Actionable or Stage3.
- Require utilization, recognized subsidy, customer volume, margin, or FCF bridge.
```

## 11. Final status

```yaml
new_independent_case_count: 4
reused_case_count: 0
same_archetype_new_symbol_count: 4
same_archetype_new_trigger_family_count: 3
calibration_usable_case_count: 4
positive_case_count: 0
counterexample_count: 4
boundary_case_count: 1
hard_4c_candidate_count: 3
current_profile_error_count: 4
verified_url_repair_needed_count: 2
do_not_propose_new_weight_delta: false
auto_selected_coverage_gap: C13 rows 27, 30-row target까지 3 부족, 50-row target까지 23 부족
sector_specific_rule_candidate: true
canonical_archetype_rule_candidate: true
loop_contribution_label: canonical_archetype_rule_candidate
new_axis_proposed: c13_jv_ampc_utilization_bridge_required_v1
existing_axis_strengthened: full_4b_requires_non_price_evidence scoped to C13 IRA/AMPC/JV/local-content battery rallies
existing_axis_weakened: null
next_recommended_archetypes:
  - C24_BIO_TRIAL_DATA_EVENT_RISK
  - C28_SOFTWARE_SECURITY_CONTRACT_RETENTION
  - C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION
```
