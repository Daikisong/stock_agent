# E2R Stock-Web Historical Calibration / Sector-Archetype Residual Research Round

## 0. Research Metadata

```text
research_session = post_calibrated_sector_archetype_residual_research
mode = historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12
output_format = one_standalone_markdown_file
created_at_kst = 2026-06-06
selected_round = R1
selected_loop = 106
selection_basis = docs/core/V12_Research_No_Repeat_Index.md
selected_priority_bucket = Priority 1
round_schedule_status = coverage_index_selected
round_sector_consistency = pass
large_sector_id = L1_INDUSTRIALS_INFRA_DEFENSE_GRID
canonical_archetype_id = C05_EPC_MEGA_CONTRACT_MARGIN_GAP
fine_archetype_id = EPC_INFRA_PROJECT_MILESTONE_HANDOVER_AND_CONTRACT_SCALE_VS_MARGIN_CASH_BRIDGE_GAP
loop_objective = priority1_50row_pullup | counterexample_mining | stage2_actionable_bonus_stress_test | 4B_non_price_requirement_stress_test | canonical_archetype_compression
price_source = Songdaiki/stock-web
stock_web_manifest_max_date = 2026-02-20
production_scoring_changed = false
shadow_weight_only = true
handoff_prompt_embedded = true
handoff_prompt_executed_now = false
```

This MD is historical calibration research only. It is not a live watchlist, not investment advice, not a production scoring patch, and not a code implementation request.

## 1. Current Calibrated Profile Assumption

```text
current_default_profile_proxy = e2r_2_1_stock_web_calibrated
active_runtime_profile_context = e2r_2_2_rolling_calibrated
previous_baseline_reference = e2r_2_0_baseline
stage2_actionable_evidence_bonus = +2.0
stage3_yellow_total_min = 75.0
stage3_green_total_min = 87.0
stage3_green_revision_min = 55.0
price_only_blowoff_blocks_positive_stage = true
full_4b_requires_non_price_evidence = true
hard_4c_thesis_break_routes_to_4c = true
```

C05 is the archetype where the market often treats a project headline as a full bridge. The problem is that an EPC award is only the front gate. The project still has to pass through execution risk, cost escalation, working capital, change orders, margin recognition, and cash collection. In this run, the project headline is treated as a valve opening, not as fuel already reaching the engine.

## 2. Round / Large Sector / Canonical Archetype Scope

| field | value |
|---|---|
| selected_round | R1 |
| selected_loop | 106 |
| large_sector_id | L1_INDUSTRIALS_INFRA_DEFENSE_GRID |
| canonical_archetype_id | C05_EPC_MEGA_CONTRACT_MARGIN_GAP |
| fine_archetype_id | EPC_INFRA_PROJECT_MILESTONE_HANDOVER_AND_CONTRACT_SCALE_VS_MARGIN_CASH_BRIDGE_GAP |
| selected_priority_bucket | Priority 1 |
| round_sector_consistency | pass |

Scope logic:

```text
R1 -> L1_INDUSTRIALS_INFRA_DEFENSE_GRID
C05_EPC_MEGA_CONTRACT_MARGIN_GAP -> R1 / L1
```

## 3. Coverage / Duplicate Avoidance Check

Latest No-Repeat ledger snapshot used:

```text
C05_EPC_MEGA_CONTRACT_MARGIN_GAP rows = 33
need_to_50 = 17
investigation_point = Mega EPC contract, cost overrun, working capital, margin gap
```

Hard duplicate key checked:

```text
canonical_archetype_id + symbol + trigger_type + entry_date
```

Duplicate gate for this run:

| candidate | symbol | canonical | trigger_type | entry_date | verdict |
|---|---:|---|---|---|---|
| DL이앤씨 / Shaheen EPC-scale proxy | 375500 | C05 | Stage2 | 2022-11-18 | soft symbol already in C05 ledger, new disclosed trigger family in this run |
| 대우건설 / Grand Faw handover-operation milestone | 047040 | C05 | Stage2-Watch | 2024-11-13 | soft symbol already in C05 ledger, new milestone/hand-over trigger family |
| 삼성E&A / Fadhili benchmark control | 028050 | C05 | Stage2 | 2024-04-03 | reused control from prior C05 run; not counted as new independent case |

The third row is intentionally kept as a benchmark/control, not as a new independent expansion. The useful new contribution comes from the contrast between (a) project scale or milestone evidence and (b) the absence or delay of margin/cash follow-through.

## 4. Stock-Web OHLC Input / Price Source Validation

| field | value |
|---|---|
| source | Songdaiki/stock-web |
| upstream source | FinanceData/marcap |
| price_basis | tradable_raw |
| price_adjustment_status | raw_unadjusted_marcap |
| calibration_shard_root | atlas/ohlcv_tradable_by_symbol_year |
| manifest_max_date | 2026-02-20 |
| schema | d,o,h,l,c,v,a,mc,s,m |

Profile caveats:

| symbol | profile | corporate action caveat | calibration use |
|---:|---|---|---|
| 375500 | atlas/symbol_profiles/375/375500.json | corporate-action candidates in Apr 2022 only; outside Nov 2022 trigger window | usable for 180D window |
| 047040 | atlas/symbol_profiles/047/047040.json | no relevant corporate-action contamination flagged in shown profile section | usable for 180D window |
| 028050 | atlas/symbol_profiles/028/028050.json | reused benchmark control | usable but not counted as new independent case |

## 5. Case Selection Summary

| case_id | symbol | company | trigger family | trigger_date | entry_date | polarity | outcome |
|---|---:|---|---|---|---|---|---|
| C05_R1L106_CASE_375500_SHAHEEN_SCALE_20221117 | 375500 | DL이앤씨 | SHAHEEN_EPC_SCALE_AND_DOMESTIC_PETROCHEM_PROJECT_BRIDGE | 2022-11-17 | 2022-11-18 | counterexample | low-MFE/high-MAE after project-scale proxy; margin/cash bridge not visible enough |
| C05_R1L106_CASE_047040_GRAND_FAW_HANDOVER_20241112 | 047040 | 대우건설 | GRAND_FAW_PORT_HANDOVER_OPERATION_MILESTONE | 2024-11-12 | 2024-11-13 | delayed_positive | handover milestone first sold off, then later recovered; entry MAE was large |
| C05_R1L106_CONTROL_028050_FADHILI_20240402 | 028050 | 삼성E&A | FADHILI_GAS_PLANT_EPC_AWARD_CONTROL | 2024-04-02 | 2024-04-03 | reused_control | contract scale alone did not prevent drawdown after the initial reaction |

## 6. Price-Path Backtest Summary

Formula:

```text
MFE_pct = (max_high_forward_window / entry_price - 1) * 100
MAE_pct = (min_low_forward_window / entry_price - 1) * 100
```

| case | entry_price | forward high | MFE | forward low | MAE | interpretation |
|---|---:|---:|---:|---:|---:|---|
| 375500 DL이앤씨 | 39,400 | 42,500 | +7.87% | 31,000 | -21.32% | project scale did not translate into durable rerating |
| 047040 대우건설 | 3,445 | 4,805 | +39.48% | 2,940 | -14.66% | delayed positive, but too volatile for clean Stage2-Actionable at trigger |
| 028050 삼성E&A control | 25,300 | 27,000 | +6.72% | 21,600 | -14.62% | useful control showing contract-size shock is not Green evidence |

## 7. Case Notes

### 7.1 375500 DL이앤씨 — project-scale proxy without margin/cash proof

The November 2022 entry row is usable because the profile-level corporate-action candidates are in April 2022, outside the trigger window. The price path had a small 2022 year-end MFE but then broke into a deeper 1Q23 drawdown. This is the classical C05 trap: a large project can raise backlog optics while the market still asks whether project margin and cash conversion are visible.

```text
entry_date = 2022-11-18
entry_price = 39400
forward_high = 42500
forward_low = 31000
MFE = +7.87
MAE = -21.32
stage_path = Stage2-Watch -> 4B/4C watch if no margin bridge appears
calibration_usable = true
```

### 7.2 047040 대우건설 — milestone/handover delayed positive with high MAE

The 2024 Grand Faw milestone row is useful because it is not a fresh EPC award headline; it is a handover/operation-readiness evidence family. That makes it a good stress test for C05. The market did not reward it immediately. The entry fell to the April 2025 low before recovering into May-June 2025. This argues for a C05 rule that milestone evidence can support Stage2-Watch, but Stage2-Actionable needs margin/backlog/cash bridge and not merely project completion language.

```text
entry_date = 2024-11-13
entry_price = 3445
forward_high = 4805
forward_low = 2940
MFE = +39.48
MAE = -14.66
stage_path = Stage2-Watch -> delayed Stage2-Actionable only after follow-through
calibration_usable = true
```

### 7.3 028050 삼성E&A — reused Fadhili control

This case is included as a control row because Fadhili is the cleanest recent EPC contract-size shock in the existing C05 set. It is not counted as a new independent case in this MD. The control reinforces the same rule: even a named EPC award with strong contract size still needs explicit gross margin, execution-risk, and cash-conversion support before becoming Stage2-Actionable or Yellow.

```text
entry_date = 2024-04-03
entry_price = 25300
forward_high = 27000
forward_low = 21600
MFE = +6.72
MAE = -14.62
stage_path = Stage2 -> 4B watch / no Green
calibration_usable = true
independent_case_counted = false
```

## 8. Raw Component Score Simulation

| component | max | 375500 | 047040 | 028050 control | comment |
|---|---:|---:|---:|---:|---|
| structural_growth | 20 | 9 | 10 | 12 | project scale exists, but not enough alone |
| eps_revision | 20 | 6 | 7 | 7 | revision bridge weak at trigger |
| fcf_quality | 15 | 4 | 5 | 5 | working capital/cash collection uncertain |
| balance_sheet_risk | 10 | 5 | 5 | 6 | construction/EPC risk requires penalty |
| valuation_mispricing | 15 | 7 | 7 | 6 | cheapness does not solve project margin |
| information_confidence | 20 | 11 | 12 | 14 | named project/milestone evidence but incomplete margin detail |
| total_raw | 100 | 42 | 46 | 50 | none should be clean Stage2-Actionable without bridge |

Current-profile stress result:

```text
stage2_actionable_evidence_bonus remains useful, but C05 needs a stricter local bridge.
Project-scale evidence should not receive the +2.0 actionable bonus unless margin/cash bridge is present.
```

## 9. JSONL Rows

```jsonl
{"row_type":"trigger","research_file":"e2r_stock_web_v12_residual_round_R1_loop_106_L1_INDUSTRIALS_INFRA_DEFENSE_GRID_C05_EPC_MEGA_CONTRACT_MARGIN_GAP_research.md","selected_round":"R1","selected_loop":106,"large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C05_EPC_MEGA_CONTRACT_MARGIN_GAP","fine_archetype_id":"EPC_INFRA_PROJECT_MILESTONE_HANDOVER_AND_CONTRACT_SCALE_VS_MARGIN_CASH_BRIDGE_GAP","symbol":"375500","company":"DL이앤씨","trigger_date":"2022-11-17","entry_date":"2022-11-18","entry_price":39400,"trigger_type":"Stage2","trigger_family":"SHAHEEN_EPC_SCALE_AND_DOMESTIC_PETROCHEM_PROJECT_BRIDGE","evidence_family":"project_scale_without_margin_cash_bridge","mfe_180d_pct":7.87,"mae_180d_pct":-21.32,"calibration_usable":true,"representative":true,"independent_case_counted":true,"polarity":"counterexample"}
{"row_type":"trigger","research_file":"e2r_stock_web_v12_residual_round_R1_loop_106_L1_INDUSTRIALS_INFRA_DEFENSE_GRID_C05_EPC_MEGA_CONTRACT_MARGIN_GAP_research.md","selected_round":"R1","selected_loop":106,"large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C05_EPC_MEGA_CONTRACT_MARGIN_GAP","fine_archetype_id":"EPC_INFRA_PROJECT_MILESTONE_HANDOVER_AND_CONTRACT_SCALE_VS_MARGIN_CASH_BRIDGE_GAP","symbol":"047040","company":"대우건설","trigger_date":"2024-11-12","entry_date":"2024-11-13","entry_price":3445,"trigger_type":"Stage2-Watch","trigger_family":"GRAND_FAW_PORT_HANDOVER_OPERATION_MILESTONE","evidence_family":"handover_milestone_without_immediate_margin_bridge","mfe_180d_pct":39.48,"mae_180d_pct":-14.66,"calibration_usable":true,"representative":true,"independent_case_counted":true,"polarity":"delayed_positive_high_mae"}
{"row_type":"trigger","research_file":"e2r_stock_web_v12_residual_round_R1_loop_106_L1_INDUSTRIALS_INFRA_DEFENSE_GRID_C05_EPC_MEGA_CONTRACT_MARGIN_GAP_research.md","selected_round":"R1","selected_loop":106,"large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C05_EPC_MEGA_CONTRACT_MARGIN_GAP","fine_archetype_id":"EPC_INFRA_PROJECT_MILESTONE_HANDOVER_AND_CONTRACT_SCALE_VS_MARGIN_CASH_BRIDGE_GAP","symbol":"028050","company":"삼성E&A","trigger_date":"2024-04-02","entry_date":"2024-04-03","entry_price":25300,"trigger_type":"Stage2","trigger_family":"FADHILI_GAS_PLANT_EPC_AWARD_CONTROL","evidence_family":"contract_size_control_row","mfe_180d_pct":6.72,"mae_180d_pct":-14.62,"calibration_usable":true,"representative":false,"independent_case_counted":false,"polarity":"reused_control"}
{"row_type":"aggregate","selected_round":"R1","selected_loop":106,"large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C05_EPC_MEGA_CONTRACT_MARGIN_GAP","new_independent_case_count":2,"reused_control_case_count":1,"calibration_usable_trigger_count":3,"positive_case_count":0,"delayed_positive_count":1,"counterexample_count":2,"current_profile_error_count":2,"rule_candidate":"c05_margin_cash_working_capital_bridge_required_for_stage2_actionable_shadow_only"}
{"row_type":"shadow_rule_candidate","axis":"c05_margin_cash_working_capital_bridge_required_for_stage2_actionable_shadow_only","scope":"canonical_archetype_id == C05_EPC_MEGA_CONTRACT_MARGIN_GAP","effect":"Block Stage2-Actionable bonus when evidence is only contract size, project milestone, handover, or backlog optics without explicit margin/cash/working-capital bridge.","status":"shadow_only","production_scoring_changed":false}
```

## 10. Residual Contribution Summary

```text
new_independent_case_count = 2
reused_control_case_count = 1
same_archetype_new_trigger_family_count = 2
calibration_usable_trigger_count = 3
positive_case_count = 0
counterexample_count = 2
delayed_positive_count = 1
current_profile_error_count = 2
```

Residual learned:

```text
C05 should distinguish:
1. signed/large EPC award,
2. project handover or operation milestone,
3. margin/cash bridge,
4. working-capital pressure,
5. delayed recognition after the first drawdown.

The sector-specific failure is not lack of project evidence. It is premature conversion of project evidence into quality evidence.
```

## 11. Proposed Shadow Rule

```text
rule_id = c05_margin_cash_working_capital_bridge_required_for_stage2_actionable_shadow_only
scope = canonical_archetype_id == C05_EPC_MEGA_CONTRACT_MARGIN_GAP
condition = evidence_family in {contract_size, project_scale, handover_milestone, backlog_optics} AND missing explicit margin_cash_working_capital_bridge
then = cap at Stage2-Watch or Stage2; do not grant Stage2-Actionable bonus; do not allow Yellow/Green from contract scale alone
exceptions = signed contract + visible margin guide + backlog quality + cash conversion or working-capital relief
status = shadow_only
production_scoring_changed = false
```

## 12. Deferred Coding Agent Handoff Prompt

```text
Do not execute during this research run.

Later coding agent task:
- Add a C05 scoped shadow rule candidate:
  c05_margin_cash_working_capital_bridge_required_for_stage2_actionable_shadow_only.
- Scope only to canonical_archetype_id == C05_EPC_MEGA_CONTRACT_MARGIN_GAP.
- Use this MD as research evidence only, not as a direct production patch.
- Require batch validation with all C05 representative rows before applying any runtime change.
```
