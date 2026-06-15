# e2r stock-web v12 residual research — R3 / loop 106 / C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK

```yaml
schema_family: v12_sector_archetype_residual
mode: historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12
research_session: post_calibrated_sector_archetype_residual_research
selected_round: R3
selected_loop: 106
large_sector_id: L3_BATTERY_EV_MOBILITY
canonical_archetype_id: C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK
fine_archetype_id: FORD_EV_CONTRACT_TERMINATION_AND_BATTERY_SUPPLY_CHAIN_CALLOFF_RISK_VS_ESS_PARENT_MIX_AND_MIDCHAIN_RELIEF_RALLY
selected_priority_bucket: Priority 0
selection_basis: docs/core/V12_Research_No_Repeat_Index.md
round_sector_consistency: pass
stock_agent_code_access_allowed: false
stock_agent_code_patch_allowed: false
stock_agent_live_scan_allowed: false
production_scoring_changed: false
shadow_weight_only: true
price_source: Songdaiki/stock-web atlas/ohlcv_tradable_by_symbol_year
price_basis: tradable_raw
price_adjustment_status: raw_unadjusted_marcap
atlas_max_date: 2026-02-20
short_post_trigger_window: true
```

## 1. Selection rationale

C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK remains a Priority 0 coverage-gap archetype.
Current coverage snapshot: 27 rows / 21 symbols / 2024-01-02~2025-03-05, with top-covered symbols concentrated in `066970`, `361610`, `011790`, `078600`, `002710`, and `003670`.

This run avoids the highest-frequency C12 symbols and uses a late-2025 Ford reset as a clean customer-calloff stress test:

- direct EV battery-supply contract termination,
- battery JV restructuring / customer production schedule reset,
- Korean battery supply-chain read-through,
- midchain copper-foil read-through that rebounds despite the call-off headline.

Because the atlas ends at 2026-02-20, all four cases are tagged as `short_window_due_atlas_max_date`. They are still useful for C12 because the key question is not long-run rerating but the immediate customer-calloff transmission path: does the contract/JV cancellation turn into hard 4C, or is it absorbed by parent mix, ESS pivot, balance-sheet support, or short-covering?

## 2. Evidence spine

### 2.1 Ford / LG Energy Solution battery-supply contract termination

Reuters reported on 2025-12-17 that Ford terminated a roughly 9.6 trillion won / $6.5 billion EV battery-supply deal with LG Energy Solution. The termination followed Ford's decision to halt production of some EV models due to policy changes and shifts in EV demand outlook.

C12 interpretation:

```text
trigger_family = customer_contract_termination
customer = Ford
supplier = LG Energy Solution
risk = direct contract call-off / lower expected EV battery volume
```

### 2.2 Ford / SK On joint-venture reset

Reuters reported on 2025-12-11 that SK On and Ford would end their U.S. battery JV. Ford would take full ownership of Kentucky plants, SK On would take the Tennessee facility, and the Tennessee production start schedule would remain flexible.

C12 interpretation:

```text
trigger_family = customer_jv_reset_and_volume_schedule_flex
customer = Ford
supplier = SK On / SK Innovation parent
risk = customer-production schedule reset + fixed-cost absorption pressure
```

### 2.3 Korean battery supply-chain read-through

MarketWatch reported that Ford's EV pullback hit Korean battery-supply-chain equities, including SK Innovation, LG Energy Solution, SK IE Technology, and EcoPro Materials. It also cited lower battery content for a range-extended replacement versus the cancelled pure EV plan.

C12 interpretation:

```text
trigger_family = customer_calloff_readthrough
affected_symbols = LGES / SK Innovation / EcoPro Materials / separator and midchain suppliers
risk = sector read-through can be real, but not all read-through should become hard_4C
```

## 3. Price source validation

Price rows were pulled only from `Songdaiki/stock-web` calibration shards:

```text
atlas/ohlcv_tradable_by_symbol_year/{prefix}/{symbol}/{year}.csv
```

Manifest facts used:

```text
source_name = FinanceData/marcap
price_adjustment_status = raw_unadjusted_marcap
calibration_shard_root = atlas/ohlcv_tradable_by_symbol_year
max_date = 2026-02-20
zero-volume / invalid OHLC rows excluded from calibration shards
corporate-action-contaminated windows blocked by default
```

## 4. Case table

| case_id | symbol | name | trigger_date | entry_date | entry_close | post-trigger peak high | peak date | MFE | post-trigger low | low date | MAE | classification |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|
| C12_CASE_001 | 373220 | LG에너지솔루션 | 2025-12-17 | 2025-12-17 | 415,500 | 455,000 | 2026-01-28 | +9.51% | 358,500 | 2026-01-02 | -13.72% | direct_calloff_boundary_4B_4C |
| C12_CASE_002 | 096770 | SK이노베이션 | 2025-12-11 | 2025-12-11 | 112,300 | 128,700 | 2026-02-20 | +14.60% | 99,500 | 2026-01-02 | -11.40% | parent_mix_boundary_not_hard4c |
| C12_CASE_003 | 450080 | 에코프로머티 | 2025-12-16 | 2025-12-16 | 59,900 | 78,900 | 2026-01-29 | +31.72% | 50,100 | 2026-01-02 | -16.36% | readthrough_high_mae_relief_rally_counterexample |
| C12_CASE_004 | 020150 | 롯데에너지머티리얼즈 | 2025-12-17 | 2025-12-17 | 34,250 | 50,500 | 2026-02-05 | +47.45% | 28,050 | 2026-01-09 | -18.10% | copperfoil_midchain_readthrough_relief_counterexample |

## 5. Case notes

### 5.1 C12_CASE_001 — LG Energy Solution: direct Ford contract termination, but not automatic hard 4C

**Company profile**

```text
symbol = 373220
name = LG에너지솔루션
market = KOSPI
status_inferred = active_like
corporate_action_candidate_count = 0
```

**Trigger**

```text
trigger_date = 2025-12-17
trigger_type = direct_customer_contract_termination
source = Reuters
customer = Ford
contract_value = approx. 9.6tn KRW / $6.5bn
```

**Observed path**

```text
entry_date = 2025-12-17
entry_close = 415500
peak_high = 455000 on 2026-01-28
mfe_pct = +9.51
low = 358500 on 2026-01-02
mae_pct = -13.72
```

**Interpretation**

LGES is the cleanest direct C12 case in this run. The trigger is not a vague EV slowdown headline; it is an actual customer contract termination.

However, the price path is not a clean collapse. It first dropped hard into early January, then recovered to a modest positive MFE before the atlas cut-off. That means C12 should not simply mark every direct battery-customer contract termination as hard 4C. The correct shadow rule is narrower:

```text
direct_customer_calloff = negative event
hard_4C only if:
  customer concentration high
  replacement demand / ESS buffer weak
  contract cancellation translates into revenue / utilization / margin revision
  no near-term offsetting orders or capital-policy buffer
```

### 5.2 C12_CASE_002 — SK Innovation: Ford/SK On JV reset, parent mix buffers the headline

**Company profile**

```text
symbol = 096770
name = SK이노베이션
market = KOSPI
status_inferred = active_like
corporate_action_candidate_count = 1
corporate_action_candidate_dates = [2024-11-20]
```

The 2025-12 trigger window is not in the corporate-action-candidate zone.

**Trigger**

```text
trigger_date = 2025-12-11
trigger_type = customer_jv_reset_and_volume_schedule_flex
source = Reuters
customer = Ford
battery_subsidiary = SK On
```

**Observed path**

```text
entry_date = 2025-12-11
entry_close = 112300
peak_high = 128700 on 2026-02-20
mfe_pct = +14.60
low = 99500 on 2026-01-02
mae_pct = -11.40
```

**Interpretation**

The trigger is directly C12: Ford and SK On reset a major U.S. battery JV, and the Tennessee schedule stayed flexible.

Yet SK Innovation is not a pure-play SK On equity. It is a parent/holding operating mix with energy, refining, chemicals, and battery exposure. This creates an important C12 guardrail:

```text
battery_customer_calloff on subsidiary != automatic parent hard_4C
```

The event is a true negative, but the parent-mix balance sheet and non-battery earnings stream can turn hard 4C into 4B boundary unless the battery losses / capex burden / debt pressure overwhelms the rest of the group.

### 5.3 C12_CASE_003 — EcoPro Materials: supply-chain read-through can be volatile, not deterministic

**Company profile**

```text
symbol = 450080
name = 에코프로머티
market = KOSPI
status_inferred = active_like
corporate_action_candidate_count = 0
```

**Trigger**

```text
trigger_date = 2025-12-16
trigger_type = korea_battery_supply_chain_readthrough_from_ford_ev_cut
source = MarketWatch
```

**Observed path**

```text
entry_date = 2025-12-16
entry_close = 59900
peak_high = 78900 on 2026-01-29
mfe_pct = +31.72
low = 50100 on 2026-01-02
mae_pct = -16.36
```

**Interpretation**

EcoPro Materials was mentioned in the Korean battery-supply-chain reaction to Ford's pivot. That makes it a useful C12 read-through case, but not a direct contract call-off case.

The stock did suffer a large drawdown after the trigger, but then produced a sharp relief rally. This is the key residual lesson:

```text
supplier_readthrough_calloff_risk is not enough for hard_4C
```

For C12, a supplier-readthrough penalty should require a bridge:

```text
named customer or program exposure
confirmed volume reduction / call-off
inventory overhang
margin / utilization / revision hit
```

Without that bridge, the event is 4B watch or high-MAE risk, not confirmed 4C.

### 5.4 C12_CASE_004 — Lotte Energy Materials: copper-foil midchain read-through, severe MAE then larger MFE

**Company profile**

```text
symbol = 020150
name = 롯데에너지머티리얼즈
market = KOSPI
status_inferred = active_like
corporate_action_candidate_count = 0
```

**Trigger**

```text
trigger_date = 2025-12-17
trigger_type = copperfoil_midchain_readthrough_from_battery_customer_calloff
source_status = sector_readthrough_source_proxy_only
```

**Observed path**

```text
entry_date = 2025-12-17
entry_close = 34250
peak_high = 50500 on 2026-02-05
mfe_pct = +47.45
low = 28050 on 2026-01-09
mae_pct = -18.10
```

**Interpretation**

This is the strongest counterexample to overbroad C12 scoring in the run. It had a very real post-trigger drawdown, but then a larger MFE.

For C12 scoring, copper-foil / midchain battery-material exposure should be treated like a second-order pressure sensor, not the contract itself. It can respond to customer call-off fear, but it can also rebound on:

- short-covering,
- restocking narratives,
- commodity/copper dynamics,
- balance-sheet or capacity-adjustment expectations,
- broad battery-beta relief.

Thus:

```text
midchain_battery_supplier + customer_calloff_headline = 4B watch
hard_4C requires direct customer exposure + utilization or margin revision evidence
```

## 6. Residual error diagnosis

### 6.1 What the current calibrated profile can still get wrong

A simple C12 rule such as:

```text
EV customer contract cut -> battery chain hard_4C
```

is too blunt. It would over-penalize:

- LGES when ESS/customer diversification offsets part of the damage,
- SK Innovation when parent-company earnings mix absorbs battery shock,
- EcoPro Materials when supplier read-through rebounds,
- Lotte Energy Materials when copper-foil/midchain beta squeezes upward after a first selloff.

The more accurate structure is:

```text
customer calloff headline
  -> identify exposure depth
  -> direct contract? JV schedule? named program? supplier read-through only?
  -> test revenue/utilization/margin/revision bridge
  -> then decide hard_4C vs 4B watch
```

### 6.2 Failure mode found

```text
failure_mode_id = c12_overbroad_customer_calloff_penalty
symptom = hard_4C assigned too early to every Korean battery supply-chain stock
cause = customer call-off evidence not mapped to company-level volume / utilization / margin impact
fix = add exposure-depth gate and short-window relief-rally guardrail
```

## 7. Shadow rule candidate

```yaml
shadow_rule_id: c12_customer_calloff_exposure_depth_gate_v1
canonical_archetype_id: C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK
rule_type: negative_gate_with_4b_boundary

positive_for_hard_4c:
  - named customer contract termination
  - named JV / project cancellation or schedule slip
  - confirmed production halt or lower battery-content substitution
  - high customer/program concentration
  - direct revenue / utilization / margin revision evidence
  - no credible ESS / replacement customer / parent-mix buffer

downgrade_to_4b_watch:
  - sector read-through only
  - parent company with non-battery earnings buffer
  - midchain material supplier with no named program exposure
  - short-window relief rally after initial selloff
  - high MFE and high MAE coexist without revision confirmation

blocked_for_stage3_green:
  - price-only rebound after call-off headline
  - generic battery beta without customer/program bridge
  - supplier vocabulary only: cathode, precursor, copper foil, separator, electrolyte
```

## 8. Machine-readable rows

```jsonl
{"row_type":"case","schema_family":"v12_sector_archetype_residual","round":"R3","loop":"106","large_sector_id":"L3_BATTERY_EV_MOBILITY","canonical_archetype_id":"C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK","fine_archetype_id":"FORD_EV_CONTRACT_TERMINATION_AND_BATTERY_SUPPLY_CHAIN_CALLOFF_RISK_VS_ESS_PARENT_MIX_AND_MIDCHAIN_RELIEF_RALLY","symbol":"373220","name":"LG에너지솔루션","trigger_date":"2025-12-17","entry_date":"2025-12-17","entry_price":415500,"peak_date":"2026-01-28","peak_high":455000,"mfe_pct":9.51,"low_date":"2026-01-02","low":358500,"mae_pct":-13.72,"classification":"direct_calloff_boundary_4B_4C","short_window_due_atlas_max_date":true,"source_status":"verified_reuters_trigger"}
{"row_type":"case","schema_family":"v12_sector_archetype_residual","round":"R3","loop":"106","large_sector_id":"L3_BATTERY_EV_MOBILITY","canonical_archetype_id":"C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK","fine_archetype_id":"FORD_EV_CONTRACT_TERMINATION_AND_BATTERY_SUPPLY_CHAIN_CALLOFF_RISK_VS_ESS_PARENT_MIX_AND_MIDCHAIN_RELIEF_RALLY","symbol":"096770","name":"SK이노베이션","trigger_date":"2025-12-11","entry_date":"2025-12-11","entry_price":112300,"peak_date":"2026-02-20","peak_high":128700,"mfe_pct":14.60,"low_date":"2026-01-02","low":99500,"mae_pct":-11.40,"classification":"parent_mix_boundary_not_hard4c","short_window_due_atlas_max_date":true,"source_status":"verified_reuters_trigger"}
{"row_type":"case","schema_family":"v12_sector_archetype_residual","round":"R3","loop":"106","large_sector_id":"L3_BATTERY_EV_MOBILITY","canonical_archetype_id":"C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK","fine_archetype_id":"FORD_EV_CONTRACT_TERMINATION_AND_BATTERY_SUPPLY_CHAIN_CALLOFF_RISK_VS_ESS_PARENT_MIX_AND_MIDCHAIN_RELIEF_RALLY","symbol":"450080","name":"에코프로머티","trigger_date":"2025-12-16","entry_date":"2025-12-16","entry_price":59900,"peak_date":"2026-01-29","peak_high":78900,"mfe_pct":31.72,"low_date":"2026-01-02","low":50100,"mae_pct":-16.36,"classification":"readthrough_high_mae_relief_rally_counterexample","short_window_due_atlas_max_date":true,"source_status":"marketwatch_supply_chain_readthrough_proxy"}
{"row_type":"case","schema_family":"v12_sector_archetype_residual","round":"R3","loop":"106","large_sector_id":"L3_BATTERY_EV_MOBILITY","canonical_archetype_id":"C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK","fine_archetype_id":"FORD_EV_CONTRACT_TERMINATION_AND_BATTERY_SUPPLY_CHAIN_CALLOFF_RISK_VS_ESS_PARENT_MIX_AND_MIDCHAIN_RELIEF_RALLY","symbol":"020150","name":"롯데에너지머티리얼즈","trigger_date":"2025-12-17","entry_date":"2025-12-17","entry_price":34250,"peak_date":"2026-02-05","peak_high":50500,"mfe_pct":47.45,"low_date":"2026-01-09","low":28050,"mae_pct":-18.10,"classification":"copperfoil_midchain_readthrough_relief_counterexample","short_window_due_atlas_max_date":true,"source_status":"sector_readthrough_proxy_only"}
{"row_type":"aggregate_metric","schema_family":"v12_sector_archetype_residual","round":"R3","loop":"106","canonical_archetype_id":"C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK","case_count":4,"new_independent_case_count":4,"same_archetype_new_symbol_count":4,"positive_case_count":0,"counterexample_count":2,"boundary_case_count":4,"hard_4c_confirmed_count":0,"hard_4c_candidate_count":1,"current_profile_error_count":4,"verified_url_repair_needed_count":1}
{"row_type":"shadow_weight","schema_family":"v12_sector_archetype_residual","round":"R3","loop":"106","canonical_archetype_id":"C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK","shadow_rule_id":"c12_customer_calloff_exposure_depth_gate_v1","do_not_apply_directly":true,"hard_4c_requires":"named_customer_contract_or_jv_calloff + customer/program concentration + utilization/margin/revision bridge","downgrade_to_4b_watch":"sector readthrough only OR parent-mix buffer OR midchain supplier without named program OR short-window relief rally"}
{"row_type":"residual_contribution","schema_family":"v12_sector_archetype_residual","round":"R3","loop":"106","canonical_archetype_id":"C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK","contribution_label":"canonical_archetype_rule_candidate","new_axis_proposed":"c12_customer_calloff_exposure_depth_gate_v1","existing_axis_strengthened":"full_4b_requires_non_price_evidence scoped to battery customer contract / JV / call-off readthrough events"}
```

## 9. Deferred Coding Agent Handoff Prompt

Do not execute this in the current research session.

```text
You are the coding agent for Songdaiki/stock_agent.

Input artifact:
- e2r_stock_web_v12_residual_round_R3_loop_106_L3_BATTERY_EV_MOBILITY_C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK_research.md

Task:
1. Parse the machine-readable JSONL rows.
2. Add cases to the v12 calibration registry only if duplicate key checks pass:
   canonical_archetype_id + symbol + trigger_type + entry_date.
3. Do not promote production scoring directly.
4. Add shadow-only rule candidate:
   c12_customer_calloff_exposure_depth_gate_v1.
5. For C12 hard_4C, require:
   named customer contract/JV call-off,
   customer/program concentration,
   direct utilization/revenue/margin/revision evidence.
6. Downgrade to 4B watch where:
   sector read-through only,
   parent company mix buffers battery exposure,
   midchain supplier has no named program exposure,
   short-window relief rally invalidates hard_4C.
7. Keep evidence_url_repair_needed flag for Lotte Energy Materials until a company-level customer/program source is added.
```

## 10. Final summary

```text
selected_round: R3
selected_loop: 106
large_sector_id: L3_BATTERY_EV_MOBILITY
canonical_archetype_id: C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK
fine_archetype_id: FORD_EV_CONTRACT_TERMINATION_AND_BATTERY_SUPPLY_CHAIN_CALLOFF_RISK_VS_ESS_PARENT_MIX_AND_MIDCHAIN_RELIEF_RALLY

new_independent_case_count: 4
reused_case_count: 0
same_archetype_new_symbol_count: 4
same_archetype_new_trigger_family_count: 3
calibration_usable case 수: 4
positive_case_count: 0
counterexample_count: 2
boundary_case_count: 4
hard_4c_confirmed_count: 0
hard_4c_candidate_count: 1
current_profile_error_count: 4
verified_url_repair_needed_count: 1

diversity_score_summary: C12 Priority 0 보강 + LGES direct Ford contract cancellation boundary + SK Innovation/SK On Ford JV reset parent-mix boundary + EcoPro Materials read-through relief-rally counterexample + Lotte Energy Materials copper-foil midchain relief-rally counterexample
do_not_propose_new_weight_delta: false
auto_selected_coverage_gap: C12 rows 27, 30-row target까지 3 부족, 50-row target까지 23 부족
sector_specific_rule_candidate: true
canonical_archetype_rule_candidate: true
loop_contribution_label: canonical_archetype_rule_candidate
new_axis_proposed: c12_customer_calloff_exposure_depth_gate_v1
existing_axis_strengthened: full_4b_requires_non_price_evidence scoped to C12 battery customer call-off / JV reset / supply-chain read-through events
existing_axis_weakened: null
next_recommended_archetypes: C13_BATTERY_JV_UTILIZATION_AMPC_IRA, C24_BIO_TRIAL_DATA_EVENT_RISK, C28_SOFTWARE_SECURITY_CONTRACT_RETENTION
```
