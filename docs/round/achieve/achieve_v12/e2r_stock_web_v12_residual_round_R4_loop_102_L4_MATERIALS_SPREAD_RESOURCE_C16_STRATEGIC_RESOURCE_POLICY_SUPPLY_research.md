# E2R v12 Stock-Web Residual Research — R4 / Loop 102 / C16 Strategic Resource Policy Supply

```yaml
schema_family: v12_sector_archetype_residual
research_session: post_calibrated_sector_archetype_residual_research
mode: historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12
selected_round: R4
selected_loop: 102
large_sector_id: L4_MATERIALS_SPREAD_RESOURCE
canonical_archetype_id: C16_STRATEGIC_RESOURCE_POLICY_SUPPLY
fine_archetype_id: STRATEGIC_RESOURCE_POLICY_OFFTAKE_SUPPLY_CHAIN_EXECUTION_BRIDGE_VS_RESOURCE_LABEL_FALSE_POSITIVE
price_source: Songdaiki/stock-web
price_basis: tradable_raw
price_adjustment_status: raw_unadjusted_marcap
stock_web_manifest_max_date: "2026-02-20"
selection_basis: "docs/core/V12_Research_No_Repeat_Index.md + conversation-local generated MD ledger"
selected_priority_bucket: "Priority 0"
round_schedule_status: coverage_index_selected
production_scoring_changed: false
shadow_weight_only: true
handoff_prompt_embedded: true
handoff_prompt_executed_now: false
evidence_url_pending: true
source_proxy_only: true
```

## 0. Execution boundary

This file is a standalone historical calibration / sector-archetype residual research Markdown artifact.  
It is not a live recommendation, not a current stock scan, not a broker/API task, and not a production code patch.

The run follows the v12 constraints:

- actual 1D OHLCV rows were checked from `Songdaiki/stock-web`;
- `stock_agent` code was not opened or patched;
- the no-repeat index was used only for coverage and duplication control;
- non-price event evidence is intentionally marked `source_proxy_only / evidence_url_pending=true`.

## 1. Selection rationale

`V12_Research_No_Repeat_Index.md` currently marks `C16_STRATEGIC_RESOURCE_POLICY_SUPPLY` as Priority 0 with 12 rows and 18 rows still needed to reach the 30-row floor. This pass adds four independent C16 cases.

```text
auto_selected_coverage_gap_static_index: C16 rows 12 -> 16 if accepted
need_to_30_after_if_accepted: 14
round_sector_consistency: pass
large_sector_id: L4_MATERIALS_SPREAD_RESOURCE
canonical_archetype_id: C16_STRATEGIC_RESOURCE_POLICY_SUPPLY
```

Novelty guard:

```text
new_independent_case_count = 4
reused_case_count = 0
same_archetype_new_symbol_count = 4
same_archetype_new_trigger_family_count = 4
dedupe_key_format = canonical_archetype_id|symbol|trigger_type|entry_date
```

## 2. Price source validation

| symbol | profile checked | 2024 shard checked | data caveat | usable? |
|---:|---|---|---|---|
| 047050 | `atlas/symbol_profiles/047/047050.json` | `atlas/ohlcv_tradable_by_symbol_year/047/047050/2024.csv` | profile has old 2023 corporate-action candidate; 2024 window usable | yes |
| 001120 | `atlas/symbol_profiles/001/001120.json` | `atlas/ohlcv_tradable_by_symbol_year/001/001120/2024.csv` | old corporate-action candidates; 2024 window usable | yes |
| 005490 | `atlas/symbol_profiles/005/005490.json` | `atlas/ohlcv_tradable_by_symbol_year/005/005490/2024.csv` | no major raw discontinuity in 2024 profile caveat | yes |
| 011810 | `atlas/symbol_profiles/011/011810.json` | `atlas/ohlcv_tradable_by_symbol_year/011/011810/2024.csv` | 2024-01-05 corporate-action candidate; selected trigger is after blocked window | yes-with-caveat |

## 3. Case matrix

| case_id | symbol | name | trigger_date | label | entry | MFE30/MAE30 | MFE90/MAE90 | MFE180/MAE180 |
|---|---:|---|---|---|---:|---:|---:|---:|
| C16-2024-047050-RESOURCE-GAS-OFFTAKE-EXECUTION | 047050 | 포스코인터내셔널 | 2024-06-03 | positive | 51,200 | 42.19% / -10.84% | 42.19% / -10.84% | 42.19% / -13.87% |
| C16-2024-001120-NICKEL-RESOURCE-LABEL-MIXED | 001120 | LX인터내셔널 | 2024-05-20 | mixed_positive | 32,900 | 9.27% / -14.74% | 9.27% / -15.96% | 9.27% / -19.00% |
| C16-2024-005490-LITHIUM-UPSTREAM-LABEL-COUNTER | 005490 | POSCO홀딩스 | 2024-03-04 | counterexample | 458,000 | 2.84% / -13.00% | 2.84% / -19.87% | 2.84% / -30.79% |
| C16-2024-011810-LITHIUM-NICKEL-TRADING-LABEL-COUNTER | 011810 | STX | 2024-02-16 | counterexample | 10,950 | 8.68% / -23.56% | 8.68% / -35.43% | 8.68% / -49.95% |

## 4. Interpretation

C16 should not behave like a simple keyword detector for lithium, nickel, copper, gas, critical minerals, or strategic supply-chain policy. A resource label is just a sign on the mine gate. The score should move higher only when the ore actually travels down the belt: company-level reserve or supply access, offtake, funded capex, production/shipment timing, ASP/margin and cash conversion.

The four cases split that mechanism cleanly:

- `047050` shows the useful side of C16. The trigger produced strong MFE because the resource/energy story had a route into company economics. Still, the move was sharp enough that full 4B should require non-price confirmation.
- `001120` is the “resource exposure but weak bridge” middle case. The market recognized the strategic-resource label, but follow-through faded unless the model can see durable offtake/margin.
- `005490` is a large-cap upstream label counterexample. Resource ownership and lithium narrative alone were not enough when commodity cycle and cash conversion were unfavorable.
- `011810` is the high-MAE guardrail case. Resource trading vocabulary without funded offtake and balance-sheet capacity should not receive positive Stage3 credit.

## 5. Current calibrated profile stress test

Current profile proxy:

```text
current_default_profile_proxy = e2r_2_1_stock_web_calibrated
stage2_actionable_evidence_bonus = +2.0
stage3_yellow_total_min = 75.0
stage3_green_total_min = 87.0
stage3_green_revision_min = 55.0
price_only_blowoff_blocks_positive_stage = true
full_4b_requires_non_price_evidence = true
hard_4c_thesis_break_routes_to_4c = true
```

Residual error found:

```text
current_profile_error_count = 4
error_type_1 = C16 resource label can be over-credited when offtake/margin/cash bridge is absent
error_type_2 = strategic resource policy can produce local 4B spikes that are not full-window positive unless non-price evidence confirms the bridge
error_type_3 = high MAE appears when resource vocabulary is not tied to funded supply-chain execution
```

## 6. Shadow rule candidate

```text
rule_id = C16_STRATEGIC_RESOURCE_OFFTAKE_SUPPLY_CHAIN_BRIDGE_REQUIRED
scope = canonical_archetype_specific
apply_now = false
shadow_weight_only = true
```

Proposed logic:

```text
IF canonical_archetype_id == C16_STRATEGIC_RESOURCE_POLICY_SUPPLY
AND resource/policy label exists
THEN positive C16 credit requires at least two of:
  - named offtake/customer/supply agreement
  - reserve/resource access with company-level economic interest
  - funded capex or commissioning schedule
  - shipment/production volume evidence
  - ASP/margin/revision/FCF bridge
ELSE cap at Stage2-Watch or Stage2-Actionable, and block Stage3-Green.
```

Guardrail:

```text
IF C16 trigger is mostly price momentum or policy headline
AND 30D/90D MFE is local but 90D/180D MAE is large
THEN route to local_4b_watch, not full_4b_positive.
```

## 7. Machine-readable rows

### 7.1 Case rows

```jsonl
{"row_type":"case","case_id":"C16-2024-047050-RESOURCE-GAS-OFFTAKE-EXECUTION","symbol":"047050","name":"포스코인터내셔널","large_sector_id":"L4_MATERIALS_SPREAD_RESOURCE","canonical_archetype_id":"C16_STRATEGIC_RESOURCE_POLICY_SUPPLY","fine_archetype_id":"STRATEGIC_RESOURCE_POLICY_OFFTAKE_SUPPLY_CHAIN_EXECUTION_BRIDGE_VS_RESOURCE_LABEL_FALSE_POSITIVE","case_label":"positive","event_proxy":"가스전·에너지/자원 개발 및 공급망 실행 기대가 실제 가격 follow-through로 연결된 구간. 다만 spike aftershock가 있어 full 4B는 비가격 bridge 필요.","profile_error":"current profile can under-recognize C16 when resource policy headline is backed by company-level reserve/offtake/production route; price-only 4B still must be capped.","source_proxy_only":true,"evidence_url_pending":true}
{"row_type":"case","case_id":"C16-2024-001120-NICKEL-RESOURCE-LABEL-MIXED","symbol":"001120","name":"LX인터내셔널","large_sector_id":"L4_MATERIALS_SPREAD_RESOURCE","canonical_archetype_id":"C16_STRATEGIC_RESOURCE_POLICY_SUPPLY","fine_archetype_id":"STRATEGIC_RESOURCE_POLICY_OFFTAKE_SUPPLY_CHAIN_EXECUTION_BRIDGE_VS_RESOURCE_LABEL_FALSE_POSITIVE","case_label":"mixed_positive","event_proxy":"니켈·광산·트레이딩 자원 exposure 라벨은 작동했으나 company-level offtake/margin bridge가 얕아 30D 이후 수익률이 눌림.","profile_error":"stage2_actionable bonus can over-credit commodity/resource label unless margin/revision/offtake durability is visible.","source_proxy_only":true,"evidence_url_pending":true}
{"row_type":"case","case_id":"C16-2024-005490-LITHIUM-UPSTREAM-LABEL-COUNTER","symbol":"005490","name":"POSCO홀딩스","large_sector_id":"L4_MATERIALS_SPREAD_RESOURCE","canonical_archetype_id":"C16_STRATEGIC_RESOURCE_POLICY_SUPPLY","fine_archetype_id":"STRATEGIC_RESOURCE_POLICY_OFFTAKE_SUPPLY_CHAIN_EXECUTION_BRIDGE_VS_RESOURCE_LABEL_FALSE_POSITIVE","case_label":"counterexample","event_proxy":"리튬·니켈·전략자원 upstream narrative는 강했지만 원자재 가격/배터리 cycle 및 cash conversion 지연이 price path를 압박.","profile_error":"C16 resource-policy score should not route to Green on resource ownership alone; offtake, unit economics, capex schedule and FCF visibility are needed.","source_proxy_only":true,"evidence_url_pending":true}
{"row_type":"case","case_id":"C16-2024-011810-LITHIUM-NICKEL-TRADING-LABEL-COUNTER","symbol":"011810","name":"STX","large_sector_id":"L4_MATERIALS_SPREAD_RESOURCE","canonical_archetype_id":"C16_STRATEGIC_RESOURCE_POLICY_SUPPLY","fine_archetype_id":"STRATEGIC_RESOURCE_POLICY_OFFTAKE_SUPPLY_CHAIN_EXECUTION_BRIDGE_VS_RESOURCE_LABEL_FALSE_POSITIVE","case_label":"counterexample","event_proxy":"리튬·니켈·자원 트레이딩 headline은 있었지만 실물 offtake·balance-sheet·margin bridge가 약했고 180D MAE가 매우 컸음.","profile_error":"resource-trading vocabulary without funded offtake/working-capital capacity should be capped at Stage2 watch or 4B-local watch, not positive Stage3.","source_proxy_only":true,"evidence_url_pending":true}
```

### 7.2 Trigger rows

```jsonl
{"row_type":"trigger","schema_family":"v12_sector_archetype_residual","large_sector_id":"L4_MATERIALS_SPREAD_RESOURCE","canonical_archetype_id":"C16_STRATEGIC_RESOURCE_POLICY_SUPPLY","fine_archetype_id":"STRATEGIC_RESOURCE_POLICY_OFFTAKE_SUPPLY_CHAIN_EXECUTION_BRIDGE_VS_RESOURCE_LABEL_FALSE_POSITIVE","symbol":"047050","name":"포스코인터내셔널","entry_date":"2024-06-03","entry_price":51200,"trigger_type":"Stage3-Yellow","case_label":"positive","MFE_30D_pct":42.19,"MAE_30D_pct":-10.84,"MFE_90D_pct":42.19,"MAE_90D_pct":-10.84,"MFE_180D_pct":42.19,"MAE_180D_pct":-13.87,"peak_date":"2024-06-14","peak_price":72800,"trough_date":"2024-11-15","trough_price":44100,"price_source":"Songdaiki/stock-web","price_source_path":"atlas/ohlcv_tradable_by_symbol_year/047/047050/2024.csv","source_proxy_only":true,"evidence_url_pending":true,"dedupe_key":"C16_STRATEGIC_RESOURCE_POLICY_SUPPLY|047050|Stage3-Yellow|2024-06-03","calibration_usable":true}
{"row_type":"trigger","schema_family":"v12_sector_archetype_residual","large_sector_id":"L4_MATERIALS_SPREAD_RESOURCE","canonical_archetype_id":"C16_STRATEGIC_RESOURCE_POLICY_SUPPLY","fine_archetype_id":"STRATEGIC_RESOURCE_POLICY_OFFTAKE_SUPPLY_CHAIN_EXECUTION_BRIDGE_VS_RESOURCE_LABEL_FALSE_POSITIVE","symbol":"001120","name":"LX인터내셔널","entry_date":"2024-05-20","entry_price":32900,"trigger_type":"Stage2-Actionable","case_label":"mixed_positive","MFE_30D_pct":9.27,"MAE_30D_pct":-14.74,"MFE_90D_pct":9.27,"MAE_90D_pct":-15.96,"MFE_180D_pct":9.27,"MAE_180D_pct":-19.0,"peak_date":"2024-05-21","peak_price":35950,"trough_date":"2024-11-15","trough_price":26650,"price_source":"Songdaiki/stock-web","price_source_path":"atlas/ohlcv_tradable_by_symbol_year/001/001120/2024.csv","source_proxy_only":true,"evidence_url_pending":true,"dedupe_key":"C16_STRATEGIC_RESOURCE_POLICY_SUPPLY|001120|Stage2-Actionable|2024-05-20","calibration_usable":true}
{"row_type":"trigger","schema_family":"v12_sector_archetype_residual","large_sector_id":"L4_MATERIALS_SPREAD_RESOURCE","canonical_archetype_id":"C16_STRATEGIC_RESOURCE_POLICY_SUPPLY","fine_archetype_id":"STRATEGIC_RESOURCE_POLICY_OFFTAKE_SUPPLY_CHAIN_EXECUTION_BRIDGE_VS_RESOURCE_LABEL_FALSE_POSITIVE","symbol":"005490","name":"POSCO홀딩스","entry_date":"2024-03-04","entry_price":458000,"trigger_type":"Stage3-Yellow","case_label":"counterexample","MFE_30D_pct":2.84,"MAE_30D_pct":-13.0,"MFE_90D_pct":2.84,"MAE_90D_pct":-19.87,"MFE_180D_pct":2.84,"MAE_180D_pct":-30.79,"peak_date":"2024-03-05","peak_price":471000,"trough_date":"2024-08-08","trough_price":317000,"price_source":"Songdaiki/stock-web","price_source_path":"atlas/ohlcv_tradable_by_symbol_year/005/005490/2024.csv","source_proxy_only":true,"evidence_url_pending":true,"dedupe_key":"C16_STRATEGIC_RESOURCE_POLICY_SUPPLY|005490|Stage3-Yellow|2024-03-04","calibration_usable":true}
{"row_type":"trigger","schema_family":"v12_sector_archetype_residual","large_sector_id":"L4_MATERIALS_SPREAD_RESOURCE","canonical_archetype_id":"C16_STRATEGIC_RESOURCE_POLICY_SUPPLY","fine_archetype_id":"STRATEGIC_RESOURCE_POLICY_OFFTAKE_SUPPLY_CHAIN_EXECUTION_BRIDGE_VS_RESOURCE_LABEL_FALSE_POSITIVE","symbol":"011810","name":"STX","entry_date":"2024-02-16","entry_price":10950,"trigger_type":"Stage2-Actionable","case_label":"counterexample","MFE_30D_pct":8.68,"MAE_30D_pct":-23.56,"MFE_90D_pct":8.68,"MAE_90D_pct":-35.43,"MFE_180D_pct":8.68,"MAE_180D_pct":-49.95,"peak_date":"2024-02-16","peak_price":11900,"trough_date":"2024-08-08","trough_price":5480,"price_source":"Songdaiki/stock-web","price_source_path":"atlas/ohlcv_tradable_by_symbol_year/011/011810/2024.csv","source_proxy_only":true,"evidence_url_pending":true,"dedupe_key":"C16_STRATEGIC_RESOURCE_POLICY_SUPPLY|011810|Stage2-Actionable|2024-02-16","calibration_usable":true}
```

### 7.3 Score simulation rows

```jsonl
{"row_type":"score_simulation","symbol":"047050","entry_date":"2024-06-03","current_profile_proxy":"e2r_2_1_stock_web_calibrated","raw_component_score_breakdown":{"stage2_base":62.0,"stage2_actionable_bonus":2.0,"resource_policy_label":5.5,"offtake_or_reserve_bridge":7.0,"margin_cash_conversion":4.0,"price_only_blowoff_penalty":-2.5,"data_quality_penalty":0.0,"total_proxy":78.0},"current_profile_expected_stage":"Stage3-Yellow","observed_alignment":"aligned_positive_but_full_4B_requires_non_price_evidence","large_sector_id":"L4_MATERIALS_SPREAD_RESOURCE","canonical_archetype_id":"C16_STRATEGIC_RESOURCE_POLICY_SUPPLY"}
{"row_type":"score_simulation","symbol":"001120","entry_date":"2024-05-20","current_profile_proxy":"e2r_2_1_stock_web_calibrated","raw_component_score_breakdown":{"stage2_base":60.0,"stage2_actionable_bonus":2.0,"resource_policy_label":5.0,"offtake_or_reserve_bridge":2.0,"margin_cash_conversion":1.0,"price_only_blowoff_penalty":-1.0,"data_quality_penalty":0.0,"total_proxy":69.0},"current_profile_expected_stage":"Stage2-Actionable","observed_alignment":"mixed_followthrough_requires_bridge_filter","large_sector_id":"L4_MATERIALS_SPREAD_RESOURCE","canonical_archetype_id":"C16_STRATEGIC_RESOURCE_POLICY_SUPPLY"}
{"row_type":"score_simulation","symbol":"005490","entry_date":"2024-03-04","current_profile_proxy":"e2r_2_1_stock_web_calibrated","raw_component_score_breakdown":{"stage2_base":63.0,"stage2_actionable_bonus":2.0,"resource_policy_label":7.0,"offtake_or_reserve_bridge":2.0,"margin_cash_conversion":-1.0,"cycle_headwind_penalty":-5.0,"price_only_blowoff_penalty":-3.0,"data_quality_penalty":0.0,"total_proxy":65.0},"current_profile_expected_stage":"Stage2-Watch","observed_alignment":"counterexample_if_resource_label_overweighted","large_sector_id":"L4_MATERIALS_SPREAD_RESOURCE","canonical_archetype_id":"C16_STRATEGIC_RESOURCE_POLICY_SUPPLY"}
{"row_type":"score_simulation","symbol":"011810","entry_date":"2024-02-16","current_profile_proxy":"e2r_2_1_stock_web_calibrated","raw_component_score_breakdown":{"stage2_base":58.0,"stage2_actionable_bonus":2.0,"resource_policy_label":6.0,"offtake_or_reserve_bridge":0.0,"balance_sheet_working_capital":-5.0,"price_only_blowoff_penalty":-4.0,"data_quality_penalty":-1.5,"total_proxy":55.5},"current_profile_expected_stage":"Rejected/Stage2-Watch","observed_alignment":"counterexample_high_MAE","large_sector_id":"L4_MATERIALS_SPREAD_RESOURCE","canonical_archetype_id":"C16_STRATEGIC_RESOURCE_POLICY_SUPPLY"}
```

### 7.4 Aggregate metric row

```jsonl
{"row_type":"aggregate_metric","large_sector_id":"L4_MATERIALS_SPREAD_RESOURCE","canonical_archetype_id":"C16_STRATEGIC_RESOURCE_POLICY_SUPPLY","case_count":4,"trigger_count":4,"positive_case_count":1,"mixed_positive_count":1,"counterexample_count":2,"local_4b_watch_count":2,"current_profile_error_count":4,"MFE_30D_avg_pct":15.74,"MAE_30D_avg_pct":-15.54,"MFE_90D_avg_pct":15.74,"MAE_90D_avg_pct":-20.52,"MFE_180D_avg_pct":15.74,"MAE_180D_avg_pct":-28.4,"static_coverage_before":12,"static_coverage_after_if_accepted":16,"need_to_30_after_if_accepted":14}
```

### 7.5 Shadow weight rows

```jsonl
{"row_type":"shadow_weight","rule_id":"C16_STRATEGIC_RESOURCE_OFFTAKE_SUPPLY_CHAIN_BRIDGE_REQUIRED","large_sector_id":"L4_MATERIALS_SPREAD_RESOURCE","canonical_archetype_id":"C16_STRATEGIC_RESOURCE_POLICY_SUPPLY","proposed_effect":"Add positive C16 credit only when policy/resource label is linked to company-level reserve, offtake, funded capex, shipment or customer contract evidence.","direction":"positive_filter","do_not_apply_now":true,"shadow_weight_only":true}
{"row_type":"shadow_weight","rule_id":"C16_RESOURCE_LABEL_WITHOUT_MARGIN_CASH_BRIDGE_CAP","large_sector_id":"L4_MATERIALS_SPREAD_RESOURCE","canonical_archetype_id":"C16_STRATEGIC_RESOURCE_POLICY_SUPPLY","proposed_effect":"Cap Stage3-Yellow/Green when lithium/nickel/copper/critical-mineral keyword appears without margin, ASP, offtake or FCF visibility.","direction":"negative_guard","do_not_apply_now":true,"shadow_weight_only":true}
{"row_type":"shadow_weight","rule_id":"C16_HIGH_MAE_COMMODITY_BETA_GUARD","large_sector_id":"L4_MATERIALS_SPREAD_RESOURCE","canonical_archetype_id":"C16_STRATEGIC_RESOURCE_POLICY_SUPPLY","proposed_effect":"If 90D/180D historical analogs show high MAE after resource label spike, require non-price bridge before positive 4B.","direction":"risk_guard","do_not_apply_now":true,"shadow_weight_only":true}
```

### 7.6 Residual contribution rows

```jsonl
{"row_type":"residual_contribution","large_sector_id":"L4_MATERIALS_SPREAD_RESOURCE","canonical_archetype_id":"C16_STRATEGIC_RESOURCE_POLICY_SUPPLY","new_axis_proposed":"C16_offtake_reserve_funded_capex_margin_bridge_required","existing_axis_strengthened":["stage2_required_bridge","price_only_blowoff_blocks_positive_stage","full_4b_requires_non_price_evidence","local_4b_watch_guard","high_MAE_guardrail"],"existing_axis_weakened":[],"contribution_label":"canonical_archetype_rule_candidate"}
{"row_type":"residual_contribution","large_sector_id":"L4_MATERIALS_SPREAD_RESOURCE","canonical_archetype_id":"C16_STRATEGIC_RESOURCE_POLICY_SUPPLY","error_pattern":"resource_policy_headline_without_company_cash_bridge","affected_cases":["001120","005490","011810"],"fix_hypothesis":"C16 needs a company-level bridge from policy/resource label to offtake, funded capex, production volume, ASP/margin and FCF; otherwise label is a theme beta."}
```

### 7.7 Narrative-only rows

```jsonl
{"row_type":"narrative_only","large_sector_id":"L4_MATERIALS_SPREAD_RESOURCE","canonical_archetype_id":"C16_STRATEGIC_RESOURCE_POLICY_SUPPLY","message":"C16 behaves like a mine mouth connected to a factory: policy headline is the mine signboard, but scoring should reward only when ore actually travels through offtake, processing, margin and cash conversion."}
```

## 8. Residual contribution summary

```text
new_axis_proposed:
- C16_offtake_reserve_funded_capex_margin_bridge_required
- C16_resource_label_without_margin_cash_bridge_cap
- C16_high_MAE_commodity_beta_guard

existing_axis_strengthened:
- stage2_required_bridge
- price_only_blowoff_blocks_positive_stage
- full_4b_requires_non_price_evidence
- local_4b_watch_guard
- high_MAE_guardrail

existing_axis_weakened:
- null

loop_contribution_label:
- canonical_archetype_rule_candidate
```

## 9. Deferred Coding Agent Handoff Prompt

Do not execute this prompt in the research session. It is included for a later batch implementation session only.

```text
You are the coding agent for Songdaiki/stock_agent.

Input artifact:
- e2r_stock_web_v12_residual_round_R4_loop_102_L4_MATERIALS_SPREAD_RESOURCE_C16_STRATEGIC_RESOURCE_POLICY_SUPPLY_research.md

Task:
1. Parse the v12 JSONL rows in the artifact.
2. Validate that each trigger row has entry_date, entry_price, trigger_type, large_sector_id, canonical_archetype_id, and all six MFE/MAE fields.
3. Add the rows to the calibration ingest pipeline only if dedupe_key is absent:
   C16_STRATEGIC_RESOURCE_POLICY_SUPPLY|symbol|trigger_type|entry_date
4. Do not alter production scoring directly.
5. Implement as shadow rule candidate only:
   C16_STRATEGIC_RESOURCE_OFFTAKE_SUPPLY_CHAIN_BRIDGE_REQUIRED
6. Re-run v12 calibration aggregation and report:
   - C16 row count before/after
   - C16 positive/mixed/counterexample balance
   - changes in high-MAE false-positive rate
   - rejected rows and reasons
7. If rule is promoted later, require explicit human approval.
```

## 10. Next recommended archetypes

```text
next_recommended_archetypes:
- C17_CHEMICAL_COMMODITY_MARGIN_SPREAD
- C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION
- C05_EPC_MEGA_CONTRACT_MARGIN_GAP
- C24_BIO_TRIAL_DATA_EVENT_RISK
- C13_BATTERY_JV_UTILIZATION_AMPC_IRA
- C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK
```
