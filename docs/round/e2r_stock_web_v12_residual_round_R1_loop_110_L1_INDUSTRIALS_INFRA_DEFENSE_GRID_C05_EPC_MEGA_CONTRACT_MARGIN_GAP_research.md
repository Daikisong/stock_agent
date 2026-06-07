# stock-web v12 residual research — R1 / loop 110 / C05_EPC_MEGA_CONTRACT_MARGIN_GAP

```text
mode = historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12
research_session = post_calibrated_sector_archetype_residual_research
output_format = one_standalone_markdown_file
handoff_prompt_embedded = true
handoff_prompt_executed_now = false

selected_round = R1
selected_loop = 110
large_sector_id = L1_INDUSTRIALS_INFRA_DEFENSE_GRID
canonical_archetype_id = C05_EPC_MEGA_CONTRACT_MARGIN_GAP
fine_archetype_id = EPC_INFRA_PROJECT_CONTRACT_SCOPE_MARGIN_WORKING_CAPITAL_BRIDGE_VS_PROJECT_HEADLINE_AND_PF_FAILURE

stock_agent_code_access_allowed = false
stock_agent_code_patch_allowed = false
production_scoring_changed = false
shadow_weight_only = true
stock_web_price_atlas_access_required = true
price_route_hunt_allowed = false
```

## 1. Selection rationale

`C05_EPC_MEGA_CONTRACT_MARGIN_GAP` remains a Priority 1 residual bucket in the no-repeat coverage ledger: 33 rows, 17 more rows needed to reach the 50-row practical calibration zone. The explicit investigation point is **Mega EPC contract, cost overrun, working capital, and margin gap**.

Recent C05 outputs already used the following case sets and are therefore avoided here:

- DL이앤씨, 대우건설, 삼성E&A benchmark/control.
- GS건설, 현대건설, HDC현대산업개발.

This run adds a new C05 slice:

1. Samsung C&T — real construction project bridge, but holding-company / non-EPC rerating contamination.
2. Taeyoung E&C — PF / working-capital failure and trading/capital-action contamination.
3. Dong-Ah Geological Engineering — specialized infrastructure/TBM capability headline without confirmed margin/backlog conversion.

## 2. Price source and calibration caveat

All price rows are from `Songdaiki/stock-web`:

```text
price_basis = tradable_raw
calibration_shard_root = atlas/ohlcv_tradable_by_symbol_year
price_adjustment_status = raw_unadjusted_marcap
max_date = 2026-02-20
```

Corporate-action contaminated windows are blocked from calibration by default. For this run, Taeyoung E&C has a 2024-10-31 corporate-action candidate and a discontinuous trading window; its **local post-trigger stress path** is usable, while the full post-restructuring window is not used as a clean C05 calibration path.

## 3. Case table

| case_id | symbol | name | trigger_date | entry_date | entry_price | peak_date | peak_high | trough_date | trough_low | MFE | MAE | classification |
|---|---:|---|---|---|---:|---|---:|---|---:|---:|---:|---|
| C05_R1L110_CASE01 | 028260 | 삼성물산 | 2023-06-20 | 2023-06-20 | 107,100 | 2023-12-14 | 135,000 | 2023-07-26 | 99,300 | +26.05% | -7.28% | positive_with_cross_attribute_4B_watch |
| C05_R1L110_CASE02 | 009410 | 태영건설 | 2023-12-28 | 2023-12-28 | 2,315 | 2024-01-11 | 4,110 | 2024-01-25 | 2,180 | +77.54% | -5.83% | hard_4C_working_capital_failure_full_window_blocked |
| C05_R1L110_CASE03 | 028100 | 동아지질 | 2024-06-14 | 2024-06-14 | 13,430 | 2024-07-30 | 15,570 | 2024-08-05 | 11,550 | +15.93% | -14.00% | high_MAE_specialized_infra_headline_counterexample |

## 4. Case notes

### 4.1 Samsung C&T — project bridge, but not clean EPC margin evidence

External trigger spine:

- Fubon Aozihdi is a large Taiwan mixed-use development.
- Samsung C&T was part of the construction JV.
- Samsung C&T's share of the project is reported around 750bn KRW out of roughly 1tn KRW estimated project cost.

Price path:

```text
entry = 2023-06-20 close 107,100
peak = 2023-12-14 high 135,000
trough = 2023-07-26 low 99,300
MFE = +26.05%
MAE = -7.28%
```

Interpretation:

The price path eventually worked, but the attribution is impure. Samsung C&T is not a pure EPC contractor; it carries holding-company, Samsung group, dividend/capital-allocation, bio/commerce, and broad value-up sensitivities. This is a C05 positive only as a **project-scope bridge with cross-attribute 4B watch**. A future scoring rule should not give full Green credit merely for a headline construction project unless it can map to EPC margin, backlog, payment terms, and working-capital conversion.

### 4.2 Taeyoung E&C — working-capital failure and contaminated rebound

External trigger spine:

- Reuters reported Korean government support measures for small businesses and builders in March 2024 and noted that Taeyoung E&C had said in December 2023 it planned to reschedule debt, raising broader construction-firm liquidity concerns.
- Reuters also reported tougher real-estate project-financing scrutiny in May 2024, after delinquency rates in project financing rose sharply and after a mid-sized builder's debt rescheduling decision.

Price path:

```text
entry = 2023-12-28 close 2,315
local_peak = 2024-01-11 high 4,110
local_trough = 2024-01-25 low 2,180
local_MFE = +77.54%
local_MAE = -5.83%
full_window = blocked because 2024-10-31 corporate-action candidate / discontinuous trading window
```

Interpretation:

Price-only logic can be fooled here. A distressed builder can show violent rescue / restructuring bounces, but that does not mean the original EPC/project-financing signal is positive. The correct label is **working-capital failure / 4C**, with the post-restructuring full window blocked. This strengthens the C05 rule that liquidity, PF rollover, receivables, and debt schedule must override contract-size or project headlines.

### 4.3 Dong-Ah Geological Engineering — capability headline without margin conversion

External trigger spine:

- Dong-Ah Geological Engineering is a civil-engineering company.
- The public source proxy notes that it succeeded in manufacturing a tunnel-boring machine in 2024 and is involved in infrastructure works including the Philippines North-South Commuter Railway.

Price path:

```text
entry = 2024-06-14 close 13,430
peak = 2024-07-30 high 15,570
trough = 2024-08-05 low 11,550
MFE = +15.93%
MAE = -14.00%
```

Interpretation:

This is a useful C05 stress case: technical capability and project participation can create tradable upside, but the path is unstable unless supported by contract value, margin visibility, advance payments, and execution schedule. The case should not be allowed to graduate to Stage3-Green without confirmed cash conversion.

## 5. Residual error diagnosis

The current calibrated profile can still make the following C05 mistakes:

1. **Headline-size over-credit**
   A large or visible construction/project headline can receive too much credit even when margin and working-capital visibility are unknown.

2. **Rescue-rally false positive**
   Distressed builders can rebound sharply after workout/support headlines. This is not the same as an investable EPC margin bridge.

3. **Technical-capability over-credit**
   TBM, plant, or infrastructure capability labels can be mistaken for earnings conversion.

4. **Full-window contamination**
   Corporate-action, trading-halt, recapitalization, or restructuring windows can distort MFE/MAE. These must be blocked or isolated into local-window stress rows.

## 6. Shadow rule proposal

```text
rule_id = c05_margin_cash_working_capital_bridge_required_for_stage2_actionable_shadow_only
scope = C05_EPC_MEGA_CONTRACT_MARGIN_GAP
production_scoring_changed = false
```

### Rule mechanics

For C05, do not promote a project / EPC / construction headline above Stage2 unless at least two of the following are present:

```text
- signed contract value attributable to the listed company
- company-specific scope clarity
- backlog addition or order-book bridge
- margin / cost pass-through evidence
- advance payment, milestone payment, or working-capital relief
- financing closure / PF rollover clarity
- no trading halt, recapitalization, workout, or corporate-action contamination
```

### Hard reject / 4C triggers

```text
- workout / debt rescheduling headline without clean post-restructuring price continuity
- PF default or liquidity crisis
- construction-quality accident / legal liability
- contract-size headline with no margin or cash bridge
- pure technical-capability headline without backlog or order conversion
```

## 7. Machine-readable rows

### case rows

```jsonl
{"row_type":"case","case_id":"C05_R1L110_CASE01","round":"R1","loop":110,"large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C05_EPC_MEGA_CONTRACT_MARGIN_GAP","fine_archetype_id":"EPC_INFRA_PROJECT_CONTRACT_SCOPE_MARGIN_WORKING_CAPITAL_BRIDGE_VS_PROJECT_HEADLINE_AND_PF_FAILURE","symbol":"028260","name":"삼성물산","trigger_date":"2023-06-20","entry_date":"2023-06-20","entry_price":107100,"peak_date":"2023-12-14","peak_high":135000,"trough_date":"2023-07-26","trough_low":99300,"mfe_pct":26.05,"mae_pct":-7.28,"classification":"positive_with_cross_attribute_4B_watch","calibration_usable":true,"reused_case":false}
{"row_type":"case","case_id":"C05_R1L110_CASE02","round":"R1","loop":110,"large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C05_EPC_MEGA_CONTRACT_MARGIN_GAP","fine_archetype_id":"EPC_INFRA_PROJECT_CONTRACT_SCOPE_MARGIN_WORKING_CAPITAL_BRIDGE_VS_PROJECT_HEADLINE_AND_PF_FAILURE","symbol":"009410","name":"태영건설","trigger_date":"2023-12-28","entry_date":"2023-12-28","entry_price":2315,"peak_date":"2024-01-11","peak_high":4110,"trough_date":"2024-01-25","trough_low":2180,"mfe_pct":77.54,"mae_pct":-5.83,"classification":"hard_4C_working_capital_failure_full_window_blocked","calibration_usable":true,"reused_case":false,"full_window_blocked":true}
{"row_type":"case","case_id":"C05_R1L110_CASE03","round":"R1","loop":110,"large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C05_EPC_MEGA_CONTRACT_MARGIN_GAP","fine_archetype_id":"EPC_INFRA_PROJECT_CONTRACT_SCOPE_MARGIN_WORKING_CAPITAL_BRIDGE_VS_PROJECT_HEADLINE_AND_PF_FAILURE","symbol":"028100","name":"동아지질","trigger_date":"2024-06-14","entry_date":"2024-06-14","entry_price":13430,"peak_date":"2024-07-30","peak_high":15570,"trough_date":"2024-08-05","trough_low":11550,"mfe_pct":15.93,"mae_pct":-14.00,"classification":"high_MAE_specialized_infra_headline_counterexample","calibration_usable":true,"reused_case":false}
```

### trigger rows

```jsonl
{"row_type":"trigger","case_id":"C05_R1L110_CASE01","trigger_type":"project_award_or_project_participation","trigger_quality":"scope_visible_margin_unknown","stage_if_current_profile":"Stage2_or_Stage2_Actionable","stage_after_shadow_rule":"Stage2_watch_4B","reason":"Samsung C&T project scope exists, but pure EPC margin bridge is diluted by holding-company attributes."}
{"row_type":"trigger","case_id":"C05_R1L110_CASE02","trigger_type":"working_capital_failure_debt_rescheduling","trigger_quality":"distress_event","stage_if_current_profile":"price_only_false_positive_possible","stage_after_shadow_rule":"4C_or_blocked","reason":"Restructuring bounce must not be treated as EPC margin conversion; full window blocked by corporate-action candidate."}
{"row_type":"trigger","case_id":"C05_R1L110_CASE03","trigger_type":"technical_capability_infrastructure_project_proxy","trigger_quality":"capability_without_cash_bridge","stage_if_current_profile":"Stage2","stage_after_shadow_rule":"Stage2_watch_or_4B","reason":"TBM/infrastructure capability needs contract value, margin and payment bridge before C05 upgrade."}
```

### aggregate / residual rows

```jsonl
{"row_type":"aggregate","round":"R1","loop":110,"large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C05_EPC_MEGA_CONTRACT_MARGIN_GAP","new_independent_case_count":3,"reused_case_count":0,"positive_case_count":1,"counterexample_count":2,"full_window_blocked_count":1,"current_profile_error_count":3}
{"row_type":"shadow_weight","rule_id":"c05_margin_cash_working_capital_bridge_required_for_stage2_actionable_shadow_only","canonical_archetype_id":"C05_EPC_MEGA_CONTRACT_MARGIN_GAP","direction":"tighten","target_stage":"Stage2_Actionable_to_Stage3","weight_delta_proposed":0,"production_scoring_changed":false,"evidence_count":3}
{"row_type":"residual_contribution","round":"R1","loop":110,"canonical_archetype_id":"C05_EPC_MEGA_CONTRACT_MARGIN_GAP","contribution_label":"canonical_archetype_rule_candidate","new_axis_proposed":"c05_margin_cash_working_capital_bridge_required_for_stage2_actionable_shadow_only","existing_axis_strengthened":"full_4b_requires_non_price_evidence scoped to EPC/project-size/PF/liquidity headlines"}
{"row_type":"narrative_only","source_label":"Golden_Pass_LNG_EPC_overrun_bankruptcy_reference","calibration_usable":false,"reason":"Non-Korean stock / no stock-web OHLC row, but supports the general C05 mechanism that EPC cost overrun and working-capital failure can dominate headline project size."}
```

## 8. Deferred Coding Agent Handoff Prompt

```text
You are a coding agent operating on Songdaiki/stock_agent in a later batch-reflection session.

Do not treat this Markdown as a command to modify production scoring immediately.
Read this MD as one C05 residual calibration input.

Task:
- Parse the machine-readable JSONL rows in this file.
- Add the C05 cases to the calibration registry if their no-repeat keys are absent:
  canonical_archetype_id + symbol + trigger_type + entry_date.
- Preserve the distinction between:
  (1) EPC/project headline with margin/cash bridge,
  (2) restructuring/workout rescue bounce,
  (3) technical capability without backlog conversion.
- Implement only shadow simulation or candidate rule rows unless a separate human-approved batch prompt authorizes production scoring changes.
- Respect corporate-action/trading-halt contamination flags.
- Do not use this file to create live stock recommendations.
```

## 9. Final loop summary

```text
selected_round = R1
selected_loop = 110
selected_priority_bucket = Priority 1
round_schedule_status = coverage_index_selected
round_sector_consistency = pass
large_sector_id = L1_INDUSTRIALS_INFRA_DEFENSE_GRID
canonical_archetype_id = C05_EPC_MEGA_CONTRACT_MARGIN_GAP
fine_archetype_id = EPC_INFRA_PROJECT_CONTRACT_SCOPE_MARGIN_WORKING_CAPITAL_BRIDGE_VS_PROJECT_HEADLINE_AND_PF_FAILURE

new_independent_case_count = 3
reused_case_count = 0
calibration_usable_case_count = 3
positive_case_count = 1
counterexample_count = 2
full_window_blocked_count = 1
current_profile_error_count = 3

do_not_propose_new_weight_delta = false
sector_specific_rule_candidate = true
canonical_archetype_rule_candidate = true
loop_contribution_label = canonical_archetype_rule_candidate
new_axis_proposed = c05_margin_cash_working_capital_bridge_required_for_stage2_actionable_shadow_only
existing_axis_strengthened = full_4b_requires_non_price_evidence scoped to C05 EPC/project-size/PF/liquidity headlines
next_recommended_archetypes = C15_MATERIAL_SPREAD_SUPERCYCLE, C18_CONSUMER_EXPORT_CHANNEL_REORDER, C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION
```
