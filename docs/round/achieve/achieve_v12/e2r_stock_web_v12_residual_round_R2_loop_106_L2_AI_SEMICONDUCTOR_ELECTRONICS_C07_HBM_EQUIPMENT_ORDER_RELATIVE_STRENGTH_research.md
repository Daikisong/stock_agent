# E2R Stock-Web v12 Residual Research — R2 / Loop 106 / C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH

```yaml
schema_family: v12_sector_archetype_residual
research_session: post_calibrated_sector_archetype_residual_research
mode: historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12
selected_round: R2
selected_loop: 106
large_sector_id: L2_AI_SEMICONDUCTOR_ELECTRONICS
canonical_archetype_id: C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH
fine_archetype_id: HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH_AND_TC_BONDER_TEST_HANDLER_BRIDGE_VS_EQUIPMENT_BETA_FADE
selection_basis: docs/core/V12_Research_No_Repeat_Index.md
selected_priority_bucket: Priority 0
round_schedule_status: coverage_index_selected
round_sector_consistency: pass
production_scoring_changed: false
shadow_weight_only: true
stock_agent_code_access_allowed: false
stock_agent_code_patch_allowed: false
stock_agent_live_scan_allowed: false
current_stock_discovery_allowed: false
price_data_source: Songdaiki/stock-web
upstream_source: FinanceData/marcap
price_basis: tradable_raw
price_adjustment_status: raw_unadjusted_marcap
calibration_shard_root: atlas/ohlcv_tradable_by_symbol_year
manifest_max_date: 2026-02-20
```

## 1. Selection rationale

`C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH` remains a thin Priority 0 bucket in the no-repeat ledger. The ledger snapshot used for selection shows C07 at 18 representative rows and highlights repeated coverage around `084370`, `232140`, `036200`, `036930`, `039030`, and `039440`. This run therefore avoids those already-crowded symbols and adds four new C07-adjacent symbols:

- `042700` Hanmi Semiconductor — TC bonder / HBM equipment direct route.
- `089030` Techwing — test handler / HBM test equipment relative-strength route.
- `083310` LOT Vacuum — semiconductor equipment beta / weak direct-HBM bridge.
- `079370` Zeus — semiconductor equipment and cleaning/robotics beta / post-corporate-action boundary case.

A short false start occurred during selection: a C01 power-equipment candidate set was opened for inspection, but it was rejected before output because the previous completed run had already covered C01. The completed output in this file is only C07.

## 2. External evidence spine

The evidence spine is intentionally narrow. It is not a live recommendation. The historical backdrop is the 2024–2026 AI/HBM investment wave, where HBM demand became structurally tied to AI accelerator supply. Reuters later described SK Hynix as Nvidia’s key HBM supplier and reported that SK Hynix held a dominant HBM share in Q1 2026, while management warned of memory bottlenecks through 2030. Reuters also separately reported that SK Hynix expected the AI-memory/HBM market to grow around 30% annually through 2030. These sources support the broad HBM demand environment, but not company-specific orders for every Korean equipment stock.

Because this run lacks clean company-specific order URLs for every case, all four rows remain `verified_url_repair_needed=true`. That is precisely the residual lesson: C07 should not promote an equipment stock merely because it sits near the HBM vocabulary cloud. The bridge must be customer qualification, order conversion, recurring tool demand, revision, or margin.

Evidence URLs used as source-proxy context:

```text
https://www.reuters.com/world/asia-pacific/sk-hynix-plans-double-wafer-capacity-next-five-years-group-chairman-says-2026-06-02/
https://www.reuters.com/world/asia-pacific/sk-hynix-expects-ai-memory-market-grow-30-year-2030-2025-08-10/
```

## 3. Price-source validation

Stock-Web manifest basis:

```text
source_name = FinanceData/marcap
price_adjustment_status = raw_unadjusted_marcap
min_date = 1995-05-02
max_date = 2026-02-20
calibration_shard_root = atlas/ohlcv_tradable_by_symbol_year
raw_shard_root = atlas/ohlcv_raw_by_symbol_year
```

Corporate-action handling:

```text
- Use tradable shard only for calibration.
- Raw/unadjusted OHLC is not split-adjusted.
- Corporate-action-contaminated windows are blocked by default.
- If a corporate-action candidate overlaps entry~D+180, calibration_usable=false.
- If corporate action is before entry and not in the forward window, the row can be usable with caveat.
```

## 4. Case summary

| case | symbol | name | entry_date | entry_close | peak_date | peak_high | trough_date | trough_low | MFE | MAE | classification |
|---|---:|---|---|---:|---|---:|---|---:|---:|---:|---|
| 1 | 042700 | 한미반도체 | 2024-01-19 | 57,700 | 2024-06-14 | 196,200 | 2024-02-01 | 56,000 | +240.03% | -2.95% | clean_positive |
| 2 | 089030 | 테크윙 | 2024-01-19 | 14,600 | 2024-07-11 | 70,800 | 2024-01-19 | 12,890 | +384.93% | -11.71% | positive_high_MAE_watch |
| 3 | 083310 | 엘오티베큠 | 2024-01-19 | 20,300 | 2024-02-23 | 24,450 | 2024-07-22 | 13,000 | +20.44% | -35.96% | equipment_beta_false_positive |
| 4 | 079370 | 제우스 | 2024-02-13 | 17,980 | 2024-02-28 | 22,800 | 2024-07-22 | 14,180 | +26.81% | -21.13% | post_CA_boundary_counterexample |

## 5. Case notes

### 5.1 Hanmi Semiconductor / 042700 — clean TC-bonder route

Hanmi is the cleanest C07 positive in this set. The entry row uses `2024-01-19` close 57,700. The forward path reached 196,200 high on `2024-06-14`, producing +240.03% MFE, while the worst observed low after entry was 56,000 on `2024-02-01`, giving only -2.95% MAE.

Interpretation:

```text
C07_positive = true
direct_HBM_equipment_route = true
price_path_quality = strong
drawdown_quality = clean
promotion_note = eligible for positive C07 evidence only if later URL repair confirms TC-bonder/order/customer bridge.
```

Residual contribution: Hanmi supports C07 but should not be used to bless all HBM equipment vocabulary. It is a “proper bridge” archetype candidate, not a sector-wide beta rule.

### 5.2 Techwing / 089030 — strong relative-strength route, but high-MAE watch

Techwing entered at 14,600 on `2024-01-19` and reached 70,800 high on `2024-07-11`, producing +384.93% MFE. However, the entry-day low was 12,890, and the path later had large volatility. This keeps the row as `positive_high_MAE_watch`, not a frictionless Green.

Interpretation:

```text
C07_positive = true
relative_strength_signal = very_strong
direct_order_bridge = source_proxy_only
risk_label = high_MAE_watch
```

Residual contribution: Techwing shows that C07 can capture large winners, but promotion should require a test-handler/test-equipment order bridge, not just relative price strength.

### 5.3 LOT Vacuum / 083310 — equipment beta false positive

LOT Vacuum entered at 20,300 on `2024-01-19`. It briefly reached 24,450 high on `2024-02-23`, giving +20.44% MFE, but later fell to 13,000 low on `2024-07-22`, a -35.96% MAE. That is a classic equipment-beta fade: the stock caught some of the semiconductor equipment wind, but the direct C07 HBM-order bridge was weak.

Interpretation:

```text
C07_positive = false
equipment_beta = true
direct_HBM_order_bridge = weak_or_unverified
classification = counterexample_high_MAE
```

Residual contribution: C07 needs a vocabulary filter. Vacuum/equipment exposure is not enough without customer qualification, order backlog, and revision evidence.

### 5.4 Zeus / 079370 — post-corporate-action boundary counterexample

Zeus has corporate-action candidates on `2024-01-16` and `2024-02-08`, so the entry was moved to `2024-02-13`. From entry close 17,980, it reached 22,800 high on `2024-02-28`, producing +26.81% MFE, but by `2024-07-22` it touched 14,180, producing -21.13% MAE.

Interpretation:

```text
corporate_action_handling = entry_after_CA_candidate
C07_positive = false
classification = boundary_counterexample
reason = semicap equipment vocabulary produced a tradable burst but did not sustain a C07 order-quality bridge.
```

Residual contribution: Post-CA windows can still be used if the entry is after the contaminated date, but the row should be handled as a boundary/watch case.

## 6. Current calibrated profile stress test

Current proxy profile premise:

```text
current_default_profile_proxy = e2r_2_1_stock_web_calibrated / rolling v12 profile
stage2_actionable_evidence_bonus = +2.0
stage3_yellow_total_min = 75.0
stage3_green_total_min = 87.0
stage3_green_revision_min = 55.0
price_only_blowoff_blocks_positive_stage = true
full_4b_requires_non_price_evidence = true
hard_4c_thesis_break_routes_to_4c = true
```

Observed residual issue:

```text
If C07 scores relative strength too generously, it will correctly catch Hanmi and Techwing but also over-score LOT Vacuum and Zeus-like equipment beta.
If C07 scores only direct customer/order/revision bridges, it keeps the positive winners while demoting vocabulary-only equipment rallies.
```

## 7. Raw component score simulation

| case | evidence_bridge | revision_bridge | order_quality | relative_strength | valuation_blowoff_risk | drawdown_penalty | simulated_total | profile_result |
|---|---:|---:|---:|---:|---:|---:|---:|---|
| Hanmi | 22 | 14 | 18 | 24 | -4 | -1 | 73 | Stage2-Actionable / needs URL repair for Yellow |
| Techwing | 16 | 10 | 13 | 25 | -8 | -5 | 51 | Stage2 watch / 4B local-positive |
| LOT Vacuum | 7 | 4 | 5 | 10 | -8 | -14 | 4 | Counterexample / 4C-prone |
| Zeus | 8 | 5 | 6 | 12 | -6 | -10 | 15 | Boundary counterexample |

Simulation result:

```text
C07 should not simply add a high relative-strength bonus.
relative_strength_bonus must be gated by:
1. customer_qualification_or_tool_adoption evidence
2. order/backlog/revision evidence
3. direct HBM process relevance
4. post-spike drawdown guard
```

## 8. JSONL rows

```jsonl
{"row_type":"case","schema_family":"v12_sector_archetype_residual","round":"R2","loop":106,"large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH","fine_archetype_id":"HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH_AND_TC_BONDER_TEST_HANDLER_BRIDGE_VS_EQUIPMENT_BETA_FADE","symbol":"042700","name":"한미반도체","trigger_type":"HBM_EQUIPMENT_RELATIVE_STRENGTH_TC_BONDER_ROUTE","trigger_date":"2024-01-19","entry_date":"2024-01-19","entry_price":57700,"peak_date":"2024-06-14","peak_high":196200,"trough_date":"2024-02-01","trough_low":56000,"mfe_pct":240.03,"mae_pct":-2.95,"classification":"clean_positive","calibration_usable":true,"verified_url_repair_needed":true,"source_proxy_only":true}
{"row_type":"case","schema_family":"v12_sector_archetype_residual","round":"R2","loop":106,"large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH","fine_archetype_id":"HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH_AND_TC_BONDER_TEST_HANDLER_BRIDGE_VS_EQUIPMENT_BETA_FADE","symbol":"089030","name":"테크윙","trigger_type":"HBM_TEST_HANDLER_RELATIVE_STRENGTH_ROUTE","trigger_date":"2024-01-19","entry_date":"2024-01-19","entry_price":14600,"peak_date":"2024-07-11","peak_high":70800,"trough_date":"2024-01-19","trough_low":12890,"mfe_pct":384.93,"mae_pct":-11.71,"classification":"positive_high_MAE_watch","calibration_usable":true,"verified_url_repair_needed":true,"source_proxy_only":true}
{"row_type":"case","schema_family":"v12_sector_archetype_residual","round":"R2","loop":106,"large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH","fine_archetype_id":"HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH_AND_TC_BONDER_TEST_HANDLER_BRIDGE_VS_EQUIPMENT_BETA_FADE","symbol":"083310","name":"엘오티베큠","trigger_type":"SEMICAP_EQUIPMENT_BETA_WEAK_HBM_BRIDGE","trigger_date":"2024-01-19","entry_date":"2024-01-19","entry_price":20300,"peak_date":"2024-02-23","peak_high":24450,"trough_date":"2024-07-22","trough_low":13000,"mfe_pct":20.44,"mae_pct":-35.96,"classification":"counterexample_high_MAE","calibration_usable":true,"verified_url_repair_needed":true,"source_proxy_only":true}
{"row_type":"case","schema_family":"v12_sector_archetype_residual","round":"R2","loop":106,"large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH","fine_archetype_id":"HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH_AND_TC_BONDER_TEST_HANDLER_BRIDGE_VS_EQUIPMENT_BETA_FADE","symbol":"079370","name":"제우스","trigger_type":"POST_CA_SEMICAP_EQUIPMENT_BETA_BOUNDARY","trigger_date":"2024-02-13","entry_date":"2024-02-13","entry_price":17980,"peak_date":"2024-02-28","peak_high":22800,"trough_date":"2024-07-22","trough_low":14180,"mfe_pct":26.81,"mae_pct":-21.13,"classification":"boundary_counterexample","calibration_usable":true,"verified_url_repair_needed":true,"source_proxy_only":true}
{"row_type":"aggregate_metric","round":"R2","loop":106,"large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH","new_independent_case_count":4,"reused_case_count":0,"same_archetype_new_symbol_count":4,"same_archetype_new_trigger_family_count":4,"positive_case_count":2,"counterexample_count":2,"current_profile_error_count":4,"verified_url_repair_needed_count":4}
{"row_type":"shadow_weight","round":"R2","loop":106,"large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH","new_axis_proposed":"c07_customer_order_revision_bridge_required_for_hbm_equipment_relative_strength","shadow_weight_only":true,"production_scoring_changed":false,"expected_effect":"preserve Hanmi/Techwing-style winners while demoting LOT Vacuum/Zeus-style equipment-beta fades"}
{"row_type":"residual_contribution","round":"R2","loop":106,"canonical_archetype_id":"C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH","contribution_label":"canonical_archetype_rule_candidate","summary":"C07 should reward direct HBM equipment order/revision bridges but penalize semicap vocabulary-only relative strength without customer qualification or sustained order evidence."}
```

## 9. Proposed shadow rule

```text
rule_id = c07_customer_order_revision_bridge_required_for_hbm_equipment_relative_strength
scope = C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH
status = shadow_only
production_scoring_changed = false

IF:
    canonical_archetype_id == C07
    AND relative_strength is strong
    AND evidence is only semicap/HBM vocabulary
    AND no customer qualification / order / backlog / revision bridge is present
THEN:
    block Stage3-Green
    route to Stage2-watch or 4B-watch
    apply high-MAE guard if post-entry trough <= -18%

IF:
    direct HBM equipment route is present
    AND customer/order/revision bridge is verified
    AND MAE remains controlled
THEN:
    allow Stage2-Actionable and possible Stage3-Yellow
    require company-specific URL repair before Stage3-Green
```

## 10. Deferred Coding Agent Handoff Prompt

```text
Do not execute now.

You are the later coding agent for Songdaiki/stock_agent.
Read this MD as a v12 residual calibration artifact only.
Do not treat it as a live recommendation.
Do not add production scoring directly from this single file.

Task:
1. Ingest the JSONL rows from this MD.
2. Deduplicate by canonical_archetype_id + symbol + trigger_type + entry_date.
3. Add the shadow-only candidate:
   c07_customer_order_revision_bridge_required_for_hbm_equipment_relative_strength
4. Use the rule only as a candidate for later batch calibration.
5. Preserve production_scoring_changed=false unless the full batch promotes the rule.
6. URL-repair these rows before allowing any Stage3-Green promotion.
```

## 11. Completion metadata

```text
completed_round = R2
completed_loop = 106
selection_basis = docs/core/V12_Research_No_Repeat_Index.md
selected_priority_bucket = Priority 0
round_schedule_status = coverage_index_selected
round_sector_consistency = pass

new_independent_case_count = 4
reused_case_count = 0
same_archetype_new_symbol_count = 4
same_archetype_new_trigger_family_count = 4
calibration_usable_case_count = 4
calibration_usable_trigger_count = 4
positive_case_count = 2
counterexample_count = 2
current_profile_error_count = 4
verified_url_repair_needed_count = 4

diversity_score_summary = C07 Priority 0 보강 + 한미반도체 direct TC-bonder clean positive + 테크윙 HBM/test-handler huge-MFE high-MAE watch + 엘오티베큠 equipment-beta false positive + 제우스 post-CA equipment-beta boundary counterexample
do_not_propose_new_weight_delta = false
auto_selected_coverage_gap = C07 rows 18, 30-row target까지 12 부족, 50-row target까지 32 부족
sector_specific_rule_candidate = true
canonical_archetype_rule_candidate = true
loop_contribution_label = canonical_archetype_rule_candidate
new_axis_proposed = c07_customer_order_revision_bridge_required_for_hbm_equipment_relative_strength
existing_axis_strengthened = full_4b_requires_non_price_evidence scoped to C07 HBM-equipment/order-relative-strength rallies
existing_axis_weakened = null
next_recommended_archetypes = C06_HBM_MEMORY_CUSTOMER_CAPACITY, C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE, C14_EV_DEMAND_SLOWDOWN_4B_4C
```
