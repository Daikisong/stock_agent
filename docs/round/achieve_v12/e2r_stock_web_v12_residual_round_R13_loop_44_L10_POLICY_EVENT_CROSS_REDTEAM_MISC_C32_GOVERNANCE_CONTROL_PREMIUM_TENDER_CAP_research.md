# E2R Stock-Web Historical Calibration / Sector-Archetype Residual Research Round

## 0. Research Metadata

```text
research_session = post_calibrated_sector_archetype_residual_research
mode = historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12
created_at = 2026-05-26 Asia/Seoul
round = R13
loop = 44
large_sector_id = L10_POLICY_EVENT_CROSS_REDTEAM_MISC
canonical_archetype_id = C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP
fine_archetype_id = HOSTILE_TENDER_CONTROL_PREMIUM_EVENT_CAP
selection_mode = auto_coverage_gap_fill
output_format = one_standalone_markdown_file
production_scoring_changed = false
shadow_weight_only = true
handoff_prompt_embedded = true
handoff_prompt_executed_now = false
```

This file is historical calibration research, not live stock discovery, not a recommendation, and not a `stock_agent` code patch. The selected gap is C32: explicit tender / counter-tender / governance-control premium events. These events often move prices violently, but they are not the same thing as durable EPS/revision rerating. The calibration problem is therefore not "did price go up?" but "when should event premium be Stage2, when should it become 4B/event-cap, and when should it be blocked from Green?"

## 1. Current Calibrated Profile Assumption

```text
current_default_profile_proxy = e2r_2_1_stock_web_calibrated
previous_baseline_reference = e2r_2_0_baseline

stage2_actionable_evidence_bonus = +2.0
stage3_yellow_total_min = 75.0
stage3_green_total_min = 87.0
stage3_green_revision_min = 55.0
stage3_cross_evidence_green_buffer = +1.5
price_only_blowoff_blocks_positive_stage = true
full_4b_requires_non_price_evidence = true
hard_4c_thesis_break_routes_to_4c = true
```

The new research does not re-prove those global rules. It stress-tests them inside a governance/control-premium canonical archetype and proposes only shadow rules.

## 2. Round / Large Sector / Canonical Archetype Scope

```text
round = R13
large_sector_id = L10_POLICY_EVENT_CROSS_REDTEAM_MISC
canonical_archetype_id = C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP
fine_archetype_id = HOSTILE_TENDER_CONTROL_PREMIUM_EVENT_CAP
loop_objective = coverage_gap_fill, counterexample_mining, sector_specific_rule_discovery, canonical_archetype_compression, 4B_non_price_requirement_stress_test
```

The archetype compresses three fine patterns:

```text
HOSTILE_TENDER_CONTROL_PREMIUM
COUNTER_TENDER_EVENT_CAP
CAPITAL_RAISE_OR_REGULATORY_OVERHANG_DURING_PROXY_BATTLE
```

## 3. Previous Coverage / Duplicate Avoidance Check

Allowed research artifact search returned no direct hit for `C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP`. The prior generated loop was L7/C23, so this loop shifts to L10/C32 to avoid the same sector and symbol cluster.

```text
auto_selected_coverage_gap = C32 missing explicit tender/counter-tender/event-cap calibration
new_independent_case_count = 3
reused_case_count = 0
new_symbol_count = 2
same_archetype_new_symbol_count = 2
same_archetype_new_trigger_family_count = 3
new_canonical_archetype_count = 1
new_trigger_family_count = 4
minimum_new_independent_case_ratio = 1.00
```

## 4. Stock-Web OHLC Input / Price Source Validation

```json
{"row_type": "price_source_validation", "source": "Songdaiki/stock-web", "source_url": "https://github.com/Songdaiki/stock-web", "manifest_path": "atlas/manifest.json", "schema_path": "atlas/schema.json", "universe_path": "atlas/universe/all_symbols.csv", "manifest_max_date": "2026-02-20", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "raw_shard_root": "atlas/ohlcv_raw_by_symbol_year", "validation_status": "usable_for_historical_calibration"}
```

Manifest validation:

```text
source_name = FinanceData/marcap
source_repo_url = https://github.com/FinanceData/marcap
price_adjustment_status = raw_unadjusted_marcap
min_date = 1995-05-02
max_date = 2026-02-20
tradable_row_count = 14354401
raw_row_count = 15214118
symbol_count = 5414
active_like_symbol_count = 2868
inactive_or_delisted_like_symbol_count = 2546
markets = ['KONEX', 'KOSDAQ', 'KOSDAQ GLOBAL', 'KOSPI']
calibration_shard_root = atlas/ohlcv_tradable_by_symbol_year
raw_shard_root = atlas/ohlcv_raw_by_symbol_year
schema_path = atlas/schema.json
universe_path = atlas/universe/all_symbols.csv
```

## 5. Historical Eligibility Gate

|symbol|company_name|profile_path|entry_windows|corporate_action_window_status|forward_180D_available|calibration_usable|
|---|---|---|---|---|---|---|
|041510|에스엠|atlas/symbol_profiles/041/041510.json|2023-02-10; 2023-03-07|clean_180D_window; profile corporate-action dates only 2002/2005|true|true|
|010130|고려아연|atlas/symbol_profiles/010/010130.json|2024-09-13; 2024-10-31; 2024-12-06|clean_180D_window in selected window|true|true|

## 6. Canonical Archetype Compression Map

| fine_archetype_id | canonical_archetype_id | compression reason |
|---|---|---|
| HOSTILE_TENDER_CONTROL_PREMIUM | C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP | Public tender price creates explicit event-premium route. |
| COUNTER_TENDER_EVENT_CAP | C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP | Counter-tender price often becomes visible upside cap. |
| CAPITAL_RAISE_OR_REGULATORY_OVERHANG_DURING_PROXY_BATTLE | C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP | Overhang is 4B/watch unless cycle status is closed. |

## 7. Case Selection Summary

|case_id|symbol|company_name|case_type|positive_or_counterexample|best_trigger|current_profile_verdict|independent_evidence_weight|
|---|---|---|---|---|---|---|---|
|R13L44_C32_SM_20230210_TENDER_ESCALATION|041510|에스엠|4B_overlay_success|positive|TR_R13L44_SM_STAGE2_HYBE_TENDER_20230210|current_profile_correct|1.0|
|R13L44_C32_KZ_20240913_HOSTILE_TENDER|010130|고려아연|structural_success|positive|TR_R13L44_KZ_STAGE2_MBK_TENDER_20240913|current_profile_correct|1.0|
|R13L44_C32_KZ_20241031_CAPITAL_RAISE_OVERHANG|010130|고려아연|4B_too_early|counterexample|TR_R13L44_KZ_4B_CAPITAL_RAISE_FSS_20241031|current_profile_4B_too_early|0.5|

## 8. Positive vs Counterexample Balance

```text
positive_case_count = 2
counterexample_count = 1
4B_case_count = 2
4C_case_count = 0 full hard-4C, 1 thesis_break_watch_only
calibration_usable_case_count = 3
```

Balance verdict: usable. The two positive cases show explicit event premium. The counterexample shows that even non-price 4B evidence can be too early if the tender/proxy cycle is not closed.

## 9. Evidence Source Map

| case_id | event evidence | source class | caveat |
|---|---|---|---|
| R13L44_C32_SM_20230210_TENDER_ESCALATION | HYBE tender, Kakao counter-tender at KRW 150,000 | AP / public news / later DART validation | Used only as historical event evidence, not live signal. |
| R13L44_C32_KZ_20240913_HOSTILE_TENDER | MBK/Young Poong tender at KRW 660,000 | Reuters / regulatory filing report | Used as public tender event evidence. |
| R13L44_C32_KZ_20241031_CAPITAL_RAISE_OVERHANG | FSS probe after share-issuance plan following buyback/tender sequence | Reuters / regulator report | Used as counterexample to full 4B timing, not as investment advice. |

## 10. Price Data Source Map

|symbol|company_name|price_shards_used|profile_path|price_basis|price_adjustment_status|
|---|---|---|---|---|---|
|041510|에스엠|atlas/ohlcv_tradable_by_symbol_year/041/041510/2023.csv|atlas/symbol_profiles/041/041510.json|tradable_raw|raw_unadjusted_marcap|
|010130|고려아연|atlas/ohlcv_tradable_by_symbol_year/010/010130/2024.csv; 2025.csv|atlas/symbol_profiles/010/010130.json|tradable_raw|raw_unadjusted_marcap|

## 11. Case-by-Case Trigger Grid

|trigger_id|case_id|trigger_type|trigger_date|entry_date|entry_price|stage2_evidence_fields|stage4b_evidence_fields|current_profile_verdict|aggregate_group_role|
|---|---|---|---|---|---|---|---|---|---|
|TR_R13L44_SM_STAGE2_HYBE_TENDER_20230210|R13L44_C32_SM_20230210_TENDER_ESCALATION|Stage2-Actionable|2023-02-10|2023-02-10|114700|public_event_or_disclosure,customer_or_order_quality,relative_strength,policy_or_regulatory_optionality||current_profile_correct|representative|
|TR_R13L44_SM_4B_KAKAO_COUNTER_TENDER_20230307|R13L44_C32_SM_20230210_TENDER_ESCALATION|Stage4B|2023-03-07|2023-03-07|149700||explicit_event_cap,valuation_blowoff,positioning_overheat,control_premium_or_event_premium|current_profile_correct|4B_overlay_only|
|TR_R13L44_KZ_STAGE2_MBK_TENDER_20240913|R13L44_C32_KZ_20240913_HOSTILE_TENDER|Stage2-Actionable|2024-09-13|2024-09-13|666000|public_event_or_disclosure,policy_or_regulatory_optionality,relative_strength||current_profile_correct|representative|
|TR_R13L44_KZ_4B_CAPITAL_RAISE_FSS_20241031|R13L44_C32_KZ_20241031_CAPITAL_RAISE_OVERHANG|Stage4B|2024-10-31|2024-10-31|998000||capital_raise_or_overhang,legal_or_regulatory_block,positioning_overheat,control_premium_or_event_premium|current_profile_4B_too_early|representative|
|TR_R13L44_KZ_PRICE_ONLY_PEAK_20241206|R13L44_C32_KZ_20241031_CAPITAL_RAISE_OVERHANG|Stage4B-PriceOnly-Local|2024-12-06|2024-12-06|1813000||price_only_local_peak,positioning_overheat|current_profile_correct|4B_overlay_only|

## 12. Trigger-Level OHLC Backtest Tables

|trigger_id|entry_date|entry_price|MFE_30D_pct|MAE_30D_pct|MFE_90D_pct|MAE_90D_pct|MFE_180D_pct|MAE_180D_pct|peak_date|peak_price|drawdown_after_peak_pct|calibration_usable|
|---|---|---|---|---|---|---|---|---|---|---|---|---|
|TR_R13L44_SM_STAGE2_HYBE_TENDER_20230210|2023-02-10|114700|40.54|-9.24|40.54|-23.63|40.54|-23.63|2023-03-08|161200|-45.66|True|
|TR_R13L44_SM_4B_KAKAO_COUNTER_TENDER_20230307|2023-03-07|149700|7.68|-41.48|7.68|-41.48|7.68|-41.48|2023-03-08|161200|-45.66|True|
|TR_R13L44_KZ_STAGE2_MBK_TENDER_20240913|2024-09-13|666000|131.68|-1.65|261.41|-1.65|261.41|-3.45|2024-12-06|2407000|-73.29|True|
|TR_R13L44_KZ_4B_CAPITAL_RAISE_FSS_20241031|2024-10-31|998000|141.18|-16.83|141.18|-30.26|141.18|-35.57|2024-12-06|2407000|-73.29|True|
|TR_R13L44_KZ_PRICE_ONLY_PEAK_20241206|2024-12-06|1813000|32.76|-54.99|32.76|-64.53|32.76|-64.53|2024-12-06|2407000|-73.29|True|

Key interpretation:

- 에스엠's Stage2 tender trigger had excellent event-premium MFE but also showed why this is not Stage3 Green: the peak arrived around the counter-tender cap and then the stock drew down sharply.
- 고려아연's tender-launch trigger had extreme event-premium MFE, but the later capital-raise/regulatory-overhang trigger shows why a simple "non-price 4B exists => full exit" rule is still too blunt during an unresolved proxy battle.

## 13. Current Calibrated Profile Stress Test

| case_id | current profile likely action | actual OHLC alignment | verdict |
|---|---|---|---|
| R13L44_C32_SM_20230210_TENDER_ESCALATION | Stage2-Actionable allowed; Green blocked without durable operating bridge; 4B event-cap on Kakao tender. | Good: 40.54% 90D MFE from HYBE trigger, but large drawdown after cap. | current_profile_correct |
| R13L44_C32_KZ_20240913_HOSTILE_TENDER | Stage2-Actionable allowed due public tender/control premium; Green blocked without EPS/revision bridge. | Good: 261.41% 180D MFE but event nature remains non-Green. | current_profile_correct |
| R13L44_C32_KZ_20241031_CAPITAL_RAISE_OVERHANG | Full 4B might fire because non-price legal/capital-raise evidence exists. | Mixed: the risk was real, but full-window peak came later; watch-only would align better. | current_profile_4B_too_early |

Axis answers:

```text
stage2_actionable_evidence_bonus = kept; C32 explicit tender deserves Stage2 but not Green.
Yellow threshold 75 = kept; event premium can pass Yellow-like score but should be tagged event-premium.
Green threshold 87 / revision 55 = strengthened for C32; no Green without operating bridge.
price_only_blowoff guard = kept.
full_4b_non_price_requirement = strengthened but refined; non-price evidence also needs cycle-status closure.
hard_4c routing = kept; no hard 4C until deal failure, regulatory rejection, accounting break, or forced unwind.
```

## 14. Stage2 / Yellow / Green Comparison

No confirmed Stage3-Green trigger is accepted in this MD. Governance/tender events may carry high total scores, but the mechanism is event-premium repricing, not durable earnings revision.

```text
green_lateness_ratio = not_applicable
reason = no_confirmed_Stage3_Green_trigger
```

The important calibration decision is not "Green too late" but "Green should not be assigned without operating/revision bridge."

## 15. 4B Local vs Full-window Timing Audit

|trigger_id|four_b_local_peak_proximity|four_b_full_window_peak_proximity|four_b_timing_verdict|four_b_evidence_type|
|---|---|---|---|---|
|TR_R13L44_SM_4B_KAKAO_COUNTER_TENDER_20230307|0.753|0.753|good_full_window_4B_timing|control_premium_or_event_premium,explicit_event_cap,valuation_blowoff|
|TR_R13L44_KZ_4B_CAPITAL_RAISE_FSS_20241031|0.379|0.191|non_price_4B_real_but_full_window_too_early|capital_raise_or_overhang,legal_or_regulatory_block,positioning_overheat|
|TR_R13L44_KZ_PRICE_ONLY_PEAK_20241206|1.0|1.0|price_only_local_peak_do_not_treat_as_full_4B_without_non_price_evidence|price_only,positioning_overheat|

The SM case is a clean example of a tender cap. The Korea Zinc October 31 row is the residual error: real non-price 4B evidence appeared, but the full-window peak was still ahead because the control/proxy contest had not closed.

## 16. 4C Protection Audit

```text
hard_4c_success = SM event cap / deal outcome after Kakao counter-tender, but treated as 4B/event-cap rather than full hard-4C.
thesis_break_watch_only = Korea Zinc 2024-10-31 capital raise / regulator probe; not full 4C because control contest remained open.
hard_4c_late = price-only Korea Zinc 2024-12-06 peak row; no independent thesis-break evidence at the exact peak.
```

## 17. Sector-Specific Rule Candidate

```text
rule_scope = sector_specific
large_sector_id = L10_POLICY_EVENT_CROSS_REDTEAM_MISC
sector_specific_rule_candidate = true
```

Proposed L10 shadow rule:

```text
L10 governance/control event premium may qualify for Stage2-Actionable when:
- public tender / counter-tender / court / regulator event is disclosed,
- the event price or control premium is explicit,
- the entry window is clean in stock-web,
- the row is not price-only.

But Stage3-Green remains blocked unless:
- durable operating bridge exists, or
- financial visibility/revision evidence exists outside the control event.
```

## 18. Canonical-Archetype Rule Candidate

```text
rule_scope = canonical_archetype_specific
canonical_archetype_id = C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP
canonical_archetype_rule_candidate = true
```

Proposed C32 shadow rules:

```text
C32_explicit_tender_stage2_bonus = +1
C32_no_green_without_operating_bridge = true
C32_tender_cap_4B_overlay = true
C32_open_proxy_battle_full_4B_delay_guard = true
```

Mechanism: a tender offer is like a magnet price. It pulls the stock toward a visible price, but the magnet is not an engine. If there is no operating engine behind it, the signal should live in Stage2/EventPremium or 4B/EventCap, not Stage3 Green.

## 19. Before / After Backtest Comparison

|profile_id|profile_scope|eligible_trigger_count|avg_MFE_90D_pct|avg_MAE_90D_pct|avg_MFE_180D_pct|avg_MAE_180D_pct|false_positive_rate|score_return_alignment_verdict|
|---|---|---|---|---|---|---|---|---|
|P0_e2r_2_1_stock_web_calibrated_proxy|current_global_proxy|3|147.71|-18.51|147.71|-20.88|0.33|mostly_aligned_but_4B_too_early_on_KZ_capital_raise|
|P0b_e2r_2_0_baseline_reference|rollback_reference|3|147.71|-18.51|147.71|-20.88|0.67|weaker_due_to_event_premium_green_confusion|
|P1_sector_specific_candidate_profile|L10_POLICY_EVENT_CROSS_REDTEAM_MISC|3|147.71|-18.51|147.71|-20.88|0.33|aligned_for_event_premium_without_green_promotion|
|P2_canonical_archetype_candidate_profile|C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP|3|147.71|-18.51|147.71|-20.88|0.0|best_alignment|
|P3_counterexample_guard_profile|C32 counterexample guard|3|147.71|-18.51|147.71|-20.88|0.0|improves_KZ_residual_4B_too_early|

## 20. Score-Return Alignment Matrix

|trigger_id|weighted_score_before|stage_label_before|weighted_score_after|stage_label_after|MFE_90D_pct|MAE_90D_pct|score_return_alignment_label|
|---|---|---|---|---|---|---|---|
|TR_R13L44_SM_STAGE2_HYBE_TENDER_20230210|77|Stage3-Yellow|80|Stage2-Actionable/EventPremium|40.54|-23.63|aligned|
|TR_R13L44_SM_4B_KAKAO_COUNTER_TENDER_20230307|85|Stage3-Yellow|58|Stage4B-EventCap|7.68|-41.48|aligned|
|TR_R13L44_KZ_STAGE2_MBK_TENDER_20240913|83|Stage3-Yellow|82|Stage2-Actionable/EventPremium|261.41|-1.65|aligned|
|TR_R13L44_KZ_4B_CAPITAL_RAISE_FSS_20241031|92|Stage4B|64|Stage4B-WatchOnlyUntilProxyCycleCloses|141.18|-30.26|residual_error_4B_too_early|
|TR_R13L44_KZ_PRICE_ONLY_PEAK_20241206|65|BlockedByPriceOnly|40|BlockedByPriceOnly|32.76|-64.53|aligned|

Component principle:

```text
valuation_repricing_score and relative_strength_score can lift event-premium Stage2.
revision_score and margin_bridge_score must remain near zero unless operating evidence exists.
legal_or_contract_risk_score, dilution_cb_risk_score, and accounting_trust_risk_score route to 4B/watch or 4C, not positive promotion.
```

## 21. Coverage Matrix

| large_sector_id | canonical_archetype_id | fine_archetype_id | positive_case_count | counterexample_count | 4B_case_count | 4C_case_count | new_independent_case_count | reused_case_count | calibration_usable_trigger_count | representative_trigger_count | current_profile_error_count | sector_rule_candidate | canonical_rule_candidate | coverage_gap_after_this_loop |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|---|---|
| L10_POLICY_EVENT_CROSS_REDTEAM_MISC | C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP | HOSTILE_TENDER_CONTROL_PREMIUM_EVENT_CAP | 2 | 1 | 3 | 0 full / 1 watch | 3 | 0 | 5 | 3 | 1 | true | true | Need more failed tender / deal-collapse holdout cases. |

## 22. Residual Contribution Summary

```text
new_independent_case_count: 3
reused_case_count: 0
reused_case_ids: []
new_symbol_count: 2
same_archetype_new_symbol_count: 2
same_archetype_new_trigger_family_count: 3
new_canonical_archetype_count: 1
new_fine_archetype_count: 3
new_trigger_family_count: 4
positive_case_count: 2
counterexample_count: 1
current_profile_error_count: 1

tested_existing_calibrated_axes:
- price_only_blowoff_blocks_positive_stage
- full_4b_requires_non_price_evidence
- hard_4c_thesis_break_routes_to_4c

residual_error_types_found:
- current_profile_4B_too_early
- event_premium_green_confusion_risk

new_axis_proposed:
- C32_explicit_tender_stage2_bonus
- C32_no_green_without_operating_bridge
- C32_tender_cap_4B_overlay
- C32_open_proxy_battle_full_4B_delay_guard

existing_axis_strengthened:
- full_4b_requires_non_price_evidence
- price_only_blowoff_blocks_positive_stage

existing_axis_weakened:
- none

existing_axis_kept:
- stage2_actionable_evidence_bonus
- stage3_yellow_total_min
- stage3_green_total_min
- stage3_green_revision_min
- stage3_cross_evidence_green_buffer
- hard_4c_thesis_break_routes_to_4c

sector_specific_rule_candidate: true
canonical_archetype_rule_candidate: true
no_new_signal_reason: null

loop_contribution_label: canonical_archetype_rule_candidate
do_not_propose_new_weight_delta: false
auto_selected_coverage_gap: C32 governance/control-premium tender-cap calibration
diversity_score_summary: high; new large sector/canonical, two new symbols, three trigger families, one residual 4B timing counterexample.
```

## 23. Validation Scope / Non-Validation Scope

Validated:

```text
- Songdaiki/stock-web manifest max_date = 2026-02-20
- tradable_raw OHLC rows for 041510 and 010130
- 30D / 90D / 180D MFE and MAE from actual stock-web rows
- profile corporate-action caveats for selected windows
- C32 positive/counterexample balance
```

Not validated:

```text
- no production scoring code inspected
- no stock_agent src/e2r code opened
- no live candidate scan
- no brokerage API or auto-trading
- no global production score change
```

## 24. Shadow Weight Calibration

```csv
row_type,axis,scope,large_sector_id,canonical_archetype_id,baseline_value,tested_value,delta,reason,backtest_effect,trigger_ids,calibration_usable_count,new_independent_case_count,counterexample_count,confidence,proposal_type,notes
shadow_weight,C32_explicit_tender_stage2_bonus,canonical_archetype_specific,L10_POLICY_EVENT_CROSS_REDTEAM_MISC,C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP,0,+1,+1,"Public tender/counter-tender price creates explicit event-premium route but not durable Green","Improves SM/Korea Zinc Stage2 event recognition without changing Green",TR_R13L44_SM_STAGE2_HYBE_TENDER_20230210|TR_R13L44_KZ_STAGE2_MBK_TENDER_20240913,3,3,1,medium,canonical_shadow_only,"not production; post-calibrated residual"
shadow_weight,C32_no_green_without_operating_bridge,canonical_archetype_specific,L10_POLICY_EVENT_CROSS_REDTEAM_MISC,C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP,false,true,+1,"Control premium is not EPS/revision bridge; Green requires operating or cash-flow bridge beyond event premium","Avoids event premium Green false positives",TR_R13L44_SM_STAGE2_HYBE_TENDER_20230210|TR_R13L44_KZ_STAGE2_MBK_TENDER_20240913,3,3,1,medium,canonical_shadow_only,"not production; post-calibrated residual"
shadow_weight,C32_open_proxy_battle_full_4B_delay_guard,canonical_archetype_specific,L10_POLICY_EVENT_CROSS_REDTEAM_MISC,C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP,false,true,+1,"Non-price 4B evidence is real but can be too early while proxy/tender cycle remains open","Fixes KZ 2024-10-31 residual 4B too-early error",TR_R13L44_KZ_4B_CAPITAL_RAISE_FSS_20241031,3,3,1,low_to_medium,canonical_shadow_only,"not production; post-calibrated residual"
```

## 25. Machine-Readable Rows

### 25.1 price_source_validation

```jsonl
{"row_type": "price_source_validation", "source": "Songdaiki/stock-web", "source_url": "https://github.com/Songdaiki/stock-web", "manifest_path": "atlas/manifest.json", "schema_path": "atlas/schema.json", "universe_path": "atlas/universe/all_symbols.csv", "manifest_max_date": "2026-02-20", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "raw_shard_root": "atlas/ohlcv_raw_by_symbol_year", "validation_status": "usable_for_historical_calibration"}
```

### 25.2 case rows

```jsonl
{"row_type": "case", "case_id": "R13L44_C32_SM_20230210_TENDER_ESCALATION", "symbol": "041510", "company_name": "에스엠", "round": "R13", "loop": "44", "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP", "fine_archetype_id": "HOSTILE_TENDER_CONTROL_PREMIUM_EVENT_CAP", "case_type": "4B_overlay_success", "positive_or_counterexample": "positive", "best_trigger": "TR_R13L44_SM_STAGE2_HYBE_TENDER_20230210", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "aligned", "current_profile_verdict": "current_profile_correct", "price_source": "Songdaiki/stock-web", "notes": "HYBE tender offer created explicit control-premium floor/optionality; Kakao counter-tender became full-window cap, not durable Stage3 Green."}
{"row_type": "case", "case_id": "R13L44_C32_KZ_20240913_HOSTILE_TENDER", "symbol": "010130", "company_name": "고려아연", "round": "R13", "loop": "44", "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP", "fine_archetype_id": "HOSTILE_TENDER_CONTROL_PREMIUM_EVENT_CAP", "case_type": "structural_success", "positive_or_counterexample": "positive", "best_trigger": "TR_R13L44_KZ_STAGE2_MBK_TENDER_20240913", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "aligned", "current_profile_verdict": "current_profile_correct", "price_source": "Songdaiki/stock-web", "notes": "Hostile tender offer produced explicit premium and active control battle; strong event-premium path but not EPS/revision Green."}
{"row_type": "case", "case_id": "R13L44_C32_KZ_20241031_CAPITAL_RAISE_OVERHANG", "symbol": "010130", "company_name": "고려아연", "round": "R13", "loop": "44", "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP", "fine_archetype_id": "HOSTILE_TENDER_CONTROL_PREMIUM_EVENT_CAP", "case_type": "4B_too_early", "positive_or_counterexample": "counterexample", "best_trigger": "TR_R13L44_KZ_4B_CAPITAL_RAISE_FSS_20241031", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": "same_symbol_as_prior_case_in_this_md_but_new_trigger_family_capital_raise_overhang_vs_tender_launch", "independent_evidence_weight": 0.5, "score_price_alignment": "residual_error_4B_too_early", "current_profile_verdict": "current_profile_4B_too_early", "price_source": "Songdaiki/stock-web", "notes": "Non-price risk was real, but unresolved proxy/tender mechanics allowed another full-window squeeze; full 4B needs cycle-status guard."}
```

### 25.3 trigger rows

```jsonl
{"row_type": "trigger", "trigger_id": "TR_R13L44_SM_STAGE2_HYBE_TENDER_20230210", "case_id": "R13L44_C32_SM_20230210_TENDER_ESCALATION", "symbol": "041510", "company_name": "에스엠", "round": "R13", "loop": "44", "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP", "fine_archetype_id": "HOSTILE_TENDER_CONTROL_PREMIUM_EVENT_CAP", "sector": "정책·지정학·재난·이벤트 / governance-control event", "primary_archetype": "governance_control_premium_tender_cap", "loop_objective": "coverage_gap_fill;counterexample_mining;sector_specific_rule_discovery;4B_non_price_requirement_stress_test", "trigger_type": "Stage2-Actionable", "trigger_date": "2023-02-10", "entry_date": "2023-02-10", "entry_price": 114700, "evidence_available_at_that_date": "HYBE disclosed acquisition of founder stake and tender offer at KRW 120,000 per share; explicit control-premium route visible before durable earnings/revision confirmation.", "evidence_source": "AP/Reuters-family public reports; stock-web OHLC shard 041/041510/2023.csv", "stage2_evidence_fields": ["public_event_or_disclosure", "customer_or_order_quality", "relative_strength", "policy_or_regulatory_optionality"], "stage3_evidence_fields": ["multiple_public_sources"], "stage4b_evidence_fields": [], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/041/041510/2023.csv", "profile_path": "atlas/symbol_profiles/041/041510.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": 40.54, "MFE_90D_pct": 40.54, "MFE_180D_pct": 40.54, "MFE_1Y_pct": 40.54, "MFE_2Y_pct": null, "MAE_30D_pct": -9.24, "MAE_90D_pct": -23.63, "MAE_180D_pct": -23.63, "MAE_1Y_pct": -28.07, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2023-03-08", "peak_price": 161200, "drawdown_after_peak_pct": -45.66, "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": null, "four_b_full_window_peak_proximity": null, "four_b_timing_verdict": null, "four_b_evidence_type": [], "four_c_protection_label": "not_applicable", "trigger_outcome_label": "event_premium_success_but_not_stage3_green", "current_profile_verdict": "current_profile_correct", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window", "same_entry_group_id": "SEG_SM_20230210_114700", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false}
{"row_type": "trigger", "trigger_id": "TR_R13L44_SM_4B_KAKAO_COUNTER_TENDER_20230307", "case_id": "R13L44_C32_SM_20230210_TENDER_ESCALATION", "symbol": "041510", "company_name": "에스엠", "round": "R13", "loop": "44", "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP", "fine_archetype_id": "HOSTILE_TENDER_CONTROL_PREMIUM_EVENT_CAP", "sector": "정책·지정학·재난·이벤트 / governance-control event", "primary_archetype": "governance_control_premium_tender_cap", "loop_objective": "coverage_gap_fill;counterexample_mining;sector_specific_rule_discovery;4B_non_price_requirement_stress_test", "trigger_type": "Stage4B", "trigger_date": "2023-03-07", "entry_date": "2023-03-07", "entry_price": 149700, "evidence_available_at_that_date": "Kakao counter-tender at KRW 150,000 per share defined a visible event cap; this was an overlay rather than a fresh Stage3 upgrade.", "evidence_source": "AP report on Kakao tender offer; stock-web OHLC shard 041/041510/2023.csv", "stage2_evidence_fields": [], "stage3_evidence_fields": [], "stage4b_evidence_fields": ["explicit_event_cap", "valuation_blowoff", "positioning_overheat", "control_premium_or_event_premium"], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/041/041510/2023.csv", "profile_path": "atlas/symbol_profiles/041/041510.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": 7.68, "MFE_90D_pct": 7.68, "MFE_180D_pct": 7.68, "MFE_1Y_pct": 7.68, "MFE_2Y_pct": null, "MAE_30D_pct": -41.48, "MAE_90D_pct": -41.48, "MAE_180D_pct": -41.48, "MAE_1Y_pct": -44.89, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2023-03-08", "peak_price": 161200, "drawdown_after_peak_pct": -45.66, "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": 0.753, "four_b_full_window_peak_proximity": 0.753, "four_b_timing_verdict": "good_full_window_4B_timing", "four_b_evidence_type": ["control_premium_or_event_premium", "explicit_event_cap", "valuation_blowoff"], "four_c_protection_label": "hard_4c_success", "trigger_outcome_label": "good_event_cap_4B", "current_profile_verdict": "current_profile_correct", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window", "same_entry_group_id": "SEG_SM_20230307_149700", "dedupe_for_aggregate": false, "aggregate_group_role": "4B_overlay_only", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false}
{"row_type": "trigger", "trigger_id": "TR_R13L44_KZ_STAGE2_MBK_TENDER_20240913", "case_id": "R13L44_C32_KZ_20240913_HOSTILE_TENDER", "symbol": "010130", "company_name": "고려아연", "round": "R13", "loop": "44", "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP", "fine_archetype_id": "HOSTILE_TENDER_CONTROL_PREMIUM_EVENT_CAP", "sector": "정책·지정학·재난·이벤트 / governance-control event", "primary_archetype": "governance_control_premium_tender_cap", "loop_objective": "coverage_gap_fill;counterexample_mining;sector_specific_rule_discovery;4B_non_price_requirement_stress_test", "trigger_type": "Stage2-Actionable", "trigger_date": "2024-09-13", "entry_date": "2024-09-13", "entry_price": 666000, "evidence_available_at_that_date": "MBK/Young Poong launched tender offer at KRW 660,000 after prior close near KRW 556,000; explicit hostile-control premium and governance battle became public.", "evidence_source": "Reuters tender-offer report; stock-web OHLC shard 010/010130/2024.csv", "stage2_evidence_fields": ["public_event_or_disclosure", "policy_or_regulatory_optionality", "relative_strength"], "stage3_evidence_fields": ["multiple_public_sources"], "stage4b_evidence_fields": [], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/010/010130/2024.csv", "profile_path": "atlas/symbol_profiles/010/010130.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": 131.68, "MFE_90D_pct": 261.41, "MFE_180D_pct": 261.41, "MFE_1Y_pct": 261.41, "MFE_2Y_pct": null, "MAE_30D_pct": -1.65, "MAE_90D_pct": -1.65, "MAE_180D_pct": -3.45, "MAE_1Y_pct": -3.45, "below_entry_price_flag_30D": false, "below_entry_price_flag_90D": false, "peak_date": "2024-12-06", "peak_price": 2407000, "drawdown_after_peak_pct": -73.29, "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": null, "four_b_full_window_peak_proximity": null, "four_b_timing_verdict": null, "four_b_evidence_type": [], "four_c_protection_label": "not_applicable", "trigger_outcome_label": "control_premium_event_success", "current_profile_verdict": "current_profile_correct", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window", "same_entry_group_id": "SEG_KZ_20240913_666000", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false}
{"row_type": "trigger", "trigger_id": "TR_R13L44_KZ_4B_CAPITAL_RAISE_FSS_20241031", "case_id": "R13L44_C32_KZ_20241031_CAPITAL_RAISE_OVERHANG", "symbol": "010130", "company_name": "고려아연", "round": "R13", "loop": "44", "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP", "fine_archetype_id": "HOSTILE_TENDER_CONTROL_PREMIUM_EVENT_CAP", "sector": "정책·지정학·재난·이벤트 / governance-control event", "primary_archetype": "governance_control_premium_tender_cap", "loop_objective": "coverage_gap_fill;counterexample_mining;sector_specific_rule_discovery;4B_non_price_requirement_stress_test", "trigger_type": "Stage4B", "trigger_date": "2024-10-31", "entry_date": "2024-10-31", "entry_price": 998000, "evidence_available_at_that_date": "FSS investigation into planned share issuance after buyback/tender sequence created real capital-raise and governance-risk evidence, but proxy battle remained open.", "evidence_source": "Reuters FSS/share-issuance investigation report; stock-web OHLC shard 010/010130/2024.csv", "stage2_evidence_fields": [], "stage3_evidence_fields": [], "stage4b_evidence_fields": ["capital_raise_or_overhang", "legal_or_regulatory_block", "positioning_overheat", "control_premium_or_event_premium"], "stage4c_evidence_fields": ["accounting_or_trust_break"], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/010/010130/2024.csv", "profile_path": "atlas/symbol_profiles/010/010130.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": 141.18, "MFE_90D_pct": 141.18, "MFE_180D_pct": 141.18, "MFE_1Y_pct": 141.18, "MFE_2Y_pct": null, "MAE_30D_pct": -16.83, "MAE_90D_pct": -30.26, "MAE_180D_pct": -35.57, "MAE_1Y_pct": -35.57, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2024-12-06", "peak_price": 2407000, "drawdown_after_peak_pct": -73.29, "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": 0.379, "four_b_full_window_peak_proximity": 0.191, "four_b_timing_verdict": "non_price_4B_real_but_full_window_too_early", "four_b_evidence_type": ["capital_raise_or_overhang", "legal_or_regulatory_block", "positioning_overheat"], "four_c_protection_label": "thesis_break_watch_only", "trigger_outcome_label": "residual_4B_too_early_counterexample", "current_profile_verdict": "current_profile_4B_too_early", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window", "same_entry_group_id": "SEG_KZ_20241031_998000", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": "same_symbol_as_R13L44_C32_KZ_20240913_HOSTILE_TENDER_but_new_trigger_family_capital_raise_legal_overhang", "independent_evidence_weight": 0.5, "do_not_count_as_new_case": false}
{"row_type": "trigger", "trigger_id": "TR_R13L44_KZ_PRICE_ONLY_PEAK_20241206", "case_id": "R13L44_C32_KZ_20241031_CAPITAL_RAISE_OVERHANG", "symbol": "010130", "company_name": "고려아연", "round": "R13", "loop": "44", "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP", "fine_archetype_id": "HOSTILE_TENDER_CONTROL_PREMIUM_EVENT_CAP", "sector": "정책·지정학·재난·이벤트 / governance-control event", "primary_archetype": "governance_control_premium_tender_cap", "loop_objective": "coverage_gap_fill;counterexample_mining;sector_specific_rule_discovery;4B_non_price_requirement_stress_test", "trigger_type": "Stage4B-PriceOnly-Local", "trigger_date": "2024-12-06", "entry_date": "2024-12-06", "entry_price": 1813000, "evidence_available_at_that_date": "Extreme price squeeze reached observed high, but no fresh non-price evidence in this row; used only to stress-test price-only blowoff block.", "evidence_source": "stock-web OHLC shard 010/010130/2024.csv", "stage2_evidence_fields": [], "stage3_evidence_fields": [], "stage4b_evidence_fields": ["price_only_local_peak", "positioning_overheat"], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/010/010130/2024.csv", "profile_path": "atlas/symbol_profiles/010/010130.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": 32.76, "MFE_90D_pct": 32.76, "MFE_180D_pct": 32.76, "MFE_1Y_pct": 32.76, "MFE_2Y_pct": null, "MAE_30D_pct": -54.99, "MAE_90D_pct": -64.53, "MAE_180D_pct": -64.53, "MAE_1Y_pct": -64.53, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2024-12-06", "peak_price": 2407000, "drawdown_after_peak_pct": -73.29, "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": 1.0, "four_b_full_window_peak_proximity": 1.0, "four_b_timing_verdict": "price_only_local_peak_do_not_treat_as_full_4B_without_non_price_evidence", "four_b_evidence_type": ["price_only", "positioning_overheat"], "four_c_protection_label": "hard_4c_late", "trigger_outcome_label": "price_only_peak_block_kept", "current_profile_verdict": "current_profile_correct", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window", "same_entry_group_id": "SEG_KZ_20241206_1813000", "dedupe_for_aggregate": false, "aggregate_group_role": "4B_overlay_only", "is_new_independent_case": true, "reuse_reason": "same_symbol_new_trigger_family_price_only_peak_stress_test", "independent_evidence_weight": 0.25, "do_not_count_as_new_case": false}
```

### 25.4 score_simulation rows

```jsonl
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R13L44_C32_SM_20230210_TENDER_ESCALATION", "trigger_id": "TR_R13L44_SM_STAGE2_HYBE_TENDER_20230210", "symbol": "041510", "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP", "raw_component_scores_before": {"contract_score": 8, "backlog_visibility_score": 0, "margin_bridge_score": 0, "revision_score": 5, "relative_strength_score": 14, "customer_quality_score": 10, "policy_or_regulatory_score": 12, "valuation_repricing_score": 15, "execution_risk_score": 5, "legal_or_contract_risk_score": 8, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_before": 77, "stage_label_before": "Stage3-Yellow", "raw_component_scores_after": {"contract_score": 8, "backlog_visibility_score": 0, "margin_bridge_score": 0, "revision_score": 5, "relative_strength_score": 14, "customer_quality_score": 10, "policy_or_regulatory_score": 12, "valuation_repricing_score": 18, "execution_risk_score": 8, "legal_or_contract_risk_score": 8, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_after": 80, "stage_label_after": "Stage2-Actionable/EventPremium", "changed_components": ["valuation_repricing_score", "execution_risk_score"], "component_delta_explanation": "C32 shadow profile separates explicit tender/control-premium evidence from durable Stage3 evidence, and routes cap/overhang to overlay rather than Green promotion.", "MFE_90D_pct": 40.54, "MAE_90D_pct": -23.63, "score_return_alignment_label": "aligned", "current_profile_verdict": "current_profile_correct"}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R13L44_C32_SM_20230210_TENDER_ESCALATION", "trigger_id": "TR_R13L44_SM_4B_KAKAO_COUNTER_TENDER_20230307", "symbol": "041510", "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP", "raw_component_scores_before": {"contract_score": 5, "backlog_visibility_score": 0, "margin_bridge_score": 0, "revision_score": 0, "relative_strength_score": 15, "customer_quality_score": 10, "policy_or_regulatory_score": 15, "valuation_repricing_score": 20, "execution_risk_score": 10, "legal_or_contract_risk_score": 10, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_before": 85, "stage_label_before": "Stage3-Yellow", "raw_component_scores_after": {"contract_score": 5, "backlog_visibility_score": 0, "margin_bridge_score": 0, "revision_score": 0, "relative_strength_score": 15, "customer_quality_score": 10, "policy_or_regulatory_score": 15, "valuation_repricing_score": 25, "execution_risk_score": 18, "legal_or_contract_risk_score": 15, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_after": 58, "stage_label_after": "Stage4B-EventCap", "changed_components": ["valuation_repricing_score", "execution_risk_score", "legal_or_contract_risk_score"], "component_delta_explanation": "C32 shadow profile separates explicit tender/control-premium evidence from durable Stage3 evidence, and routes cap/overhang to overlay rather than Green promotion.", "MFE_90D_pct": 7.68, "MAE_90D_pct": -41.48, "score_return_alignment_label": "aligned", "current_profile_verdict": "current_profile_correct"}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R13L44_C32_KZ_20240913_HOSTILE_TENDER", "trigger_id": "TR_R13L44_KZ_STAGE2_MBK_TENDER_20240913", "symbol": "010130", "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP", "raw_component_scores_before": {"contract_score": 6, "backlog_visibility_score": 0, "margin_bridge_score": 0, "revision_score": 0, "relative_strength_score": 18, "customer_quality_score": 8, "policy_or_regulatory_score": 15, "valuation_repricing_score": 18, "execution_risk_score": 8, "legal_or_contract_risk_score": 10, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_before": 83, "stage_label_before": "Stage3-Yellow", "raw_component_scores_after": {"contract_score": 6, "backlog_visibility_score": 0, "margin_bridge_score": 0, "revision_score": 0, "relative_strength_score": 18, "customer_quality_score": 8, "policy_or_regulatory_score": 15, "valuation_repricing_score": 21, "execution_risk_score": 8, "legal_or_contract_risk_score": 12, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_after": 82, "stage_label_after": "Stage2-Actionable/EventPremium", "changed_components": ["valuation_repricing_score", "legal_or_contract_risk_score"], "component_delta_explanation": "C32 shadow profile separates explicit tender/control-premium evidence from durable Stage3 evidence, and routes cap/overhang to overlay rather than Green promotion.", "MFE_90D_pct": 261.41, "MAE_90D_pct": -1.65, "score_return_alignment_label": "aligned", "current_profile_verdict": "current_profile_correct"}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R13L44_C32_KZ_20241031_CAPITAL_RAISE_OVERHANG", "trigger_id": "TR_R13L44_KZ_4B_CAPITAL_RAISE_FSS_20241031", "symbol": "010130", "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP", "raw_component_scores_before": {"contract_score": 4, "backlog_visibility_score": 0, "margin_bridge_score": 0, "revision_score": 0, "relative_strength_score": 18, "customer_quality_score": 5, "policy_or_regulatory_score": 12, "valuation_repricing_score": 22, "execution_risk_score": 16, "legal_or_contract_risk_score": 18, "dilution_cb_risk_score": 12, "accounting_trust_risk_score": 5}, "weighted_score_before": 92, "stage_label_before": "Stage4B", "raw_component_scores_after": {"contract_score": 4, "backlog_visibility_score": 0, "margin_bridge_score": 0, "revision_score": 0, "relative_strength_score": 18, "customer_quality_score": 5, "policy_or_regulatory_score": 12, "valuation_repricing_score": 22, "execution_risk_score": 18, "legal_or_contract_risk_score": 22, "dilution_cb_risk_score": 18, "accounting_trust_risk_score": 8}, "weighted_score_after": 64, "stage_label_after": "Stage4B-WatchOnlyUntilProxyCycleCloses", "changed_components": ["execution_risk_score", "legal_or_contract_risk_score", "dilution_cb_risk_score", "accounting_trust_risk_score"], "component_delta_explanation": "C32 shadow profile separates explicit tender/control-premium evidence from durable Stage3 evidence, and routes cap/overhang to overlay rather than Green promotion.", "MFE_90D_pct": 141.18, "MAE_90D_pct": -30.26, "score_return_alignment_label": "residual_error_4B_too_early", "current_profile_verdict": "current_profile_4B_too_early"}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R13L44_C32_KZ_20241031_CAPITAL_RAISE_OVERHANG", "trigger_id": "TR_R13L44_KZ_PRICE_ONLY_PEAK_20241206", "symbol": "010130", "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP", "raw_component_scores_before": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 0, "revision_score": 0, "relative_strength_score": 20, "customer_quality_score": 0, "policy_or_regulatory_score": 0, "valuation_repricing_score": 25, "execution_risk_score": 20, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_before": 65, "stage_label_before": "BlockedByPriceOnly", "raw_component_scores_after": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 0, "revision_score": 0, "relative_strength_score": 20, "customer_quality_score": 0, "policy_or_regulatory_score": 0, "valuation_repricing_score": 25, "execution_risk_score": 22, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_after": 40, "stage_label_after": "BlockedByPriceOnly", "changed_components": ["execution_risk_score", "valuation_repricing_score"], "component_delta_explanation": "C32 shadow profile separates explicit tender/control-premium evidence from durable Stage3 evidence, and routes cap/overhang to overlay rather than Green promotion.", "MFE_90D_pct": 32.76, "MAE_90D_pct": -64.53, "score_return_alignment_label": "aligned", "current_profile_verdict": "current_profile_correct"}
```

### 25.5 shadow_weight rows

```csv
row_type,axis,scope,large_sector_id,canonical_archetype_id,baseline_value,tested_value,delta,reason,backtest_effect,trigger_ids,calibration_usable_count,new_independent_case_count,counterexample_count,confidence,proposal_type,notes
shadow_weight,C32_explicit_tender_stage2_bonus,canonical_archetype_specific,L10_POLICY_EVENT_CROSS_REDTEAM_MISC,C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP,0,+1,+1,"Public tender/counter-tender price creates explicit event-premium route but not durable Green","Improves SM/Korea Zinc Stage2 event recognition without changing Green",TR_R13L44_SM_STAGE2_HYBE_TENDER_20230210|TR_R13L44_KZ_STAGE2_MBK_TENDER_20240913,3,3,1,medium,canonical_shadow_only,"not production; post-calibrated residual"
shadow_weight,C32_no_green_without_operating_bridge,canonical_archetype_specific,L10_POLICY_EVENT_CROSS_REDTEAM_MISC,C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP,false,true,+1,"Control premium is not EPS/revision bridge; Green requires operating or cash-flow bridge beyond event premium","Avoids event premium Green false positives",TR_R13L44_SM_STAGE2_HYBE_TENDER_20230210|TR_R13L44_KZ_STAGE2_MBK_TENDER_20240913,3,3,1,medium,canonical_shadow_only,"not production; post-calibrated residual"
shadow_weight,C32_open_proxy_battle_full_4B_delay_guard,canonical_archetype_specific,L10_POLICY_EVENT_CROSS_REDTEAM_MISC,C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP,false,true,+1,"Non-price 4B evidence is real but can be too early while proxy/tender cycle remains open","Fixes KZ 2024-10-31 residual 4B too-early error",TR_R13L44_KZ_4B_CAPITAL_RAISE_FSS_20241031,3,3,1,low_to_medium,canonical_shadow_only,"not production; post-calibrated residual"
```

### 25.6 residual_contribution row

```jsonl
{"row_type": "residual_contribution", "round": "R13", "loop": "44", "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP", "new_independent_case_count": 3, "reused_case_count": 0, "new_symbol_count": 2, "same_archetype_new_symbol_count": 2, "same_archetype_new_trigger_family_count": 3, "new_canonical_archetype_count": 1, "new_trigger_family_count": 4, "tested_existing_calibrated_axes": ["price_only_blowoff_blocks_positive_stage", "full_4b_requires_non_price_evidence", "hard_4c_thesis_break_routes_to_4c"], "residual_error_types_found": ["current_profile_4B_too_early", "event_premium_green_confusion_risk"], "loop_contribution_label": "canonical_archetype_rule_candidate", "do_not_propose_new_weight_delta": false}
```

### 25.7 narrative_only rows

```jsonl
{"row_type":"narrative_only","case_id":"HMM_011200_DEAL_COLLAPSE_HOLDOUT","symbol":"011200","large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP","reason":"potential_failed_tender_or_sale_process_counterexample_identified_but_evidence_source_not_cleanly_resolved_in_this_loop","price_source":"Songdaiki/stock-web","usage":"not_weight_calibration"}
```

## 26. Deferred Coding Agent Handoff Prompt

### Purpose

You are now in the repository implementation phase. The attached Markdown files are v12 post-calibrated residual research outputs produced using the Songdaiki/stock-web OHLC atlas.

These MDs are not live candidate research. They are historical calibration research designed to extend the already-applied e2r_2_1_stock_web_calibrated profile.

Do not blindly apply every shadow row.
Ingest the machine-readable rows and update the sector/canonical-archetype calibration ledger.

### Price source context

- Primary historical price source used by the research MD: Songdaiki/stock-web.
- Price basis: tradable_raw.
- Price adjustment status: raw_unadjusted_marcap.
- Price shard pattern: atlas/ohlcv_tradable_by_symbol_year/<prefix>/<ticker>/<year>.csv.
- Symbol profile pattern: atlas/symbol_profiles/<prefix>/<ticker>.json.

### Rules

- Use only calibration_usable=true rows for quantitative calibration.
- Do not count reused cases as new independent evidence unless independent_evidence_weight > 0.
- Do not treat schema_rematerialization_only or duplicate_low_value_loop as new evidence.
- Do not apply global deltas unless multiple large_sector_id values support the same direction.
- Prefer sector_specific or canonical_archetype_specific shadow profiles.
- Positive score promotion requires non-price evidence and clean 180D MFE/MAE.
- 4B rows are overlay/risk calibration only.
- 4C rows are thesis-break/protection calibration only.
- price-only rows cannot promote Stage2/Stage3.
- If a v12 MD weakens an already applied axis, log it as residual counterexample rather than immediately reverting.
- Production scoring must not change unless the user explicitly asks for another promotion batch.

### Expected repository tasks

1. Parse case / trigger / score_simulation / shadow_weight / residual_contribution rows.
2. Validate stock-web price source fields.
3. Validate large_sector_id and canonical_archetype_id.
4. Validate novelty and reuse fields.
5. Deduplicate same_entry_group_id and reused cases.
6. Aggregate by large_sector_id and canonical_archetype_id.
7. Update sector_shadow_profile and archetype_shadow_profile only.
8. Preserve global calibrated profile unless explicitly promoted.
9. Report new independent cases, counterexamples, and residual error types.
10. Add tests that duplicate low-value loops cannot change weights.

### Expected output

- Concise implementation summary.
- Rows accepted/rejected.
- New sector/canonical archetype coverage.
- Existing axis strengthened/weakened/kept.
- No investment recommendation language.

## 27. Next Round State

```text
next_round = R13 or R10 holdout
recommended_next_scope = failed tender / deal-collapse cases for C32, or C30 PF balance-sheet break cases
recommended_next_objective = counterexample_mining + 4C_thesis_break_timing_test
avoid_repeating = Korea Zinc 2024-09-13 and SM 2023-02-10/2023-03-07 same evidence family
```

## 28. Source Notes

Stock-Web source files inspected:

```text
atlas/manifest.json
atlas/symbol_profiles/041/041510.json
atlas/ohlcv_tradable_by_symbol_year/041/041510/2023.csv
atlas/symbol_profiles/010/010130.json
atlas/ohlcv_tradable_by_symbol_year/010/010130/2024.csv
atlas/ohlcv_tradable_by_symbol_year/010/010130/2025.csv
```

Public event sources used for evidence family:

```text
- AP: Kakao tender offer for SM Entertainment at KRW 150,000 per share, March 7, 2023.
- Reuters: MBK/Young Poong tender offer for Korea Zinc at KRW 660,000 per share, September 13, 2024.
- Reuters: Korea Zinc court / buyback offer context, October 21, 2024.
- Reuters: Korea Zinc FSS investigation into share-issuance plan, October 31, 2024.
```
