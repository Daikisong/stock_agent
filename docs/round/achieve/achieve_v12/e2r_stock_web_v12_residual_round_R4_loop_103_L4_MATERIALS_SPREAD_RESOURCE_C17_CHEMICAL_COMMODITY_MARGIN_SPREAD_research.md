# E2R v12 Stock-Web Residual Research — R4 Loop 103 — C17 Chemical / Commodity Margin Spread

```text
research_session = post_calibrated_sector_archetype_residual_research
mode = historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12
selected_round = R4
selected_loop = 103
large_sector_id = L4_MATERIALS_SPREAD_RESOURCE
canonical_archetype_id = C17_CHEMICAL_COMMODITY_MARGIN_SPREAD
fine_archetype_id = CHEMICAL_COMMODITY_SPREAD_OPM_FCF_BRIDGE_VS_RAW_MATERIAL_BETA_FALSE_POSITIVE
price_source = Songdaiki/stock-web
price_basis = tradable_raw
price_adjustment_status = raw_unadjusted_marcap
production_scoring_changed = false
shadow_weight_only = true
stock_agent_code_accessed = false
stock_agent_code_patch_written = false
handoff_prompt_embedded = true
handoff_prompt_executed_now = false
```

## 0. Selection and no-repeat check

The previous accepted conversation-local output ended at `C16_STRATEGIC_RESOURCE_POLICY_SUPPLY`. The next Priority 0 shortage in the visible No-Repeat index is `C17_CHEMICAL_COMMODITY_MARGIN_SPREAD`, listed at 12 rows with 18 still needed to reach 30. This run adds four new independent C17 cases.

```text
selection_basis = docs/core/V12_Research_No_Repeat_Index.md + conversation-local generated MD ledger
selected_priority_bucket = Priority 0
auto_selected_coverage_gap_static_index = C17 rows 12 -> 16 if accepted; still Priority 0, need 14 to 30
round_sector_consistency = pass
large_sector_id = L4_MATERIALS_SPREAD_RESOURCE
canonical_archetype_id = C17_CHEMICAL_COMMODITY_MARGIN_SPREAD
```

### Novelty / duplicate guard

| symbol | name | trigger date | trigger type | duplicate decision |
|---:|---|---:|---|---|
| 298020 | 효성티앤씨 | 2024-04-17 | Stage3-Yellow | new C17 symbol/trigger family in this local ledger |
| 011780 | 금호석유화학 | 2024-04-29 | Stage3-Yellow | new C17 symbol/trigger family in this local ledger |
| 011170 | 롯데케미칼 | 2024-04-29 | Stage2-Actionable | new C17 symbol/trigger family in this local ledger |
| 010950 | S-Oil | 2024-04-05 | Stage2-Actionable | new C17 symbol/trigger family in this local ledger |

Dedupe key format:

```text
canonical_archetype_id + symbol + trigger_type + entry_date
```

All four rows use fresh keys.

---

## 1. Thesis of the residual

C17 is the place where a model can easily confuse **commodity vocabulary** with **company economics**.

A chemical company is like a mill sitting between two rivers. One river is feedstock cost; the other is product ASP. The mill only creates value when the gap between the two rivers is wide enough and stable enough to move through utilization, inventory timing, operating margin, and finally FCF. A price spike caused only by “oil down,” “spread rebound,” “China reopening,” or “bottoming” is not yet the mill turning.

### New axis proposed

```text
C17_company_level_spread_margin_FCF_bridge_required
C17_inventory_utilization_guard
C17_raw_material_beta_false_positive_guard
C17_full_4B_requires_non_price_margin_evidence
```

### Practical rule candidate

A C17 candidate should not be treated as Stage3-Green unless at least two of the following are present:

```text
1. product-feedstock spread widening is visible at the company’s product mix level
2. utilization / shipment / ASP mix improves without working-capital deterioration
3. OPM or earnings revision confirms the spread thesis
4. FCF or cash conversion is not being eaten by inventory/revaluation losses
5. price action is not merely a local 4B bounce after commodity-beta selloff
```

---

## 2. Stock-Web price-source validation

This run used only Songdaiki/stock-web 1D OHLCV shards.

| symbol | stock-web profile | 2024 shard used | status |
|---:|---|---|---|
| 298020 | `atlas/symbol_profiles/298/298020.json` | `atlas/ohlcv_tradable_by_symbol_year/298/298020/2024.csv` | active-like; no corporate-action caveat in used 2024 window |
| 011780 | `atlas/symbol_profiles/011/011780.json` | `atlas/ohlcv_tradable_by_symbol_year/011/011780/2024.csv` | active-like; name-history caveat only, used 2024 window tradable |
| 011170 | `atlas/symbol_profiles/011/011170.json` | `atlas/ohlcv_tradable_by_symbol_year/011/011170/2024.csv` | active-like; corporate-action candidate is outside used 2024 trigger window |
| 010950 | `atlas/symbol_profiles/010/010950.json` | `atlas/ohlcv_tradable_by_symbol_year/010/010950/2024.csv` | active-like; corporate-action candidate is historical and outside used 2024 trigger window |

```text
validation_scope = stock-web 1D OHLCV only
non_price_evidence = source_proxy_only
evidence_url_pending = true
do_not_use_as_live_candidate = true
```

---

## 3. Trigger-level price path results

| case | symbol | entry | entry price | 30D MFE / MAE | 90D MFE / MAE | 180D MFE / MAE | result |
|---:|---:|---:|---:|---:|---:|---:|---|
| 1 | 298020 | 2024-04-17 | 340,500 | +23.79% / -9.84% | +23.79% / -19.97% | +23.79% / -22.76% | positive with full-window guard |
| 2 | 011780 | 2024-04-29 | 138,300 | +16.05% / -2.39% | +20.61% / -7.09% | +20.61% / -29.28% | mixed positive |
| 3 | 011170 | 2024-04-29 | 107,700 | +16.53% / -3.62% | +16.53% / -20.89% | +16.53% / -39.83% | counterexample |
| 4 | 010950 | 2024-04-05 | 83,500 | +1.20% / -16.05% | +1.20% / -20.60% | +1.20% / -35.69% | counterexample |

Aggregate:

```text
new_independent_case_count = 4
calibration_usable_case_count = 4
calibration_usable_trigger_count = 4
positive_case_count = 1
mixed_positive_count = 1
counterexample_count = 2
local_4b_watch_count = 2
current_profile_error_count = 4
mean_30d_MFE = 14.39%
mean_180d_MAE = -31.89%
```

---

## 4. Case notes

### Case 1 — 298020 효성티앤씨 — C17 positive local path, but full-window guard needed

Entry was fixed at the 2024-04-17 close of 340,500. The price path moved to a 421,500 high by 2024-05-17, a +23.79% local MFE. That is a real calibration-positive local move. The problem is the 180-day window: the same path later printed 263,000 by 2024-09-19, a -22.76% MAE from entry.

Interpretation:

```text
positive_evidence = product spread/local price alignment
residual = full-window persistence requires company-level spread and OPM/FCF bridge
stage_view = Stage3-Yellow can be allowed; Stage3-Green should require margin confirmation
```

This is not a “block all chemical spread cases” result. It says the model must know whether the mill is really earning the spread, not only hearing the river move.

### Case 2 — 011780 금호석유화학 — synthetic rubber / chemical spread mixed positive

Entry was fixed at the 2024-04-29 close of 138,300. The price path reached 166,800 by 2024-07-12, a +20.61% MFE. That is strong enough to preserve the C17 pathway as usable. But the same case later fell to 97,800 by 2024-11-15, a -29.28% MAE.

Interpretation:

```text
positive_evidence = 30/90d price alignment
residual = spread durability and downstream margin conversion cannot be assumed
guard = high_MAE guard should activate once spread thesis stops showing cash conversion
```

This is the classic C17 trap: the first half of the chart behaves like a valid spread thesis, the second half behaves like a commodity beta.

### Case 3 — 011170 롯데케미칼 — petrochemical bottoming false positive

Entry was fixed at the 2024-04-29 close of 107,700. The case had a local peak of 125,500 by 2024-05-20, so price-only logic could read it as a valid early rebound. But the full path reached a 64,800 low by 2024-11-18, a -39.83% MAE.

Interpretation:

```text
false_positive_driver = NCC/petrochemical bottoming vocabulary
missing_bridge = product spread -> utilization -> OPM -> FCF
stage_view = Stage2-Actionable should not upgrade unless company-level margin bridge is visible
```

This is a clean counterexample for C17: “spread rebound” language without realized company economics is not enough.

### Case 4 — 010950 S-Oil — refining spread / inventory timing counterexample

Entry was fixed at the 2024-04-05 close of 83,500. The local high after entry was only 84,500 on 2024-04-08, while the full path fell to roughly 53,700 in the later window. The 180-day MAE is -35.69%.

Interpretation:

```text
false_positive_driver = refining crack spread / oil beta headline
missing_bridge = crack spread + inventory valuation + OPM + dividend/cash bridge
stage_view = Stage2-Actionable should be capped or rejected without earnings bridge
```

In refining, a spread headline is not a bridge. The model must check whether the barrel margin survives inventory timing and crude direction.

---

## 5. Current calibrated profile stress test

The current proxy profile is assumed to be:

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

### Where the current profile still fails or is incomplete

| failure mode | case evidence | current behavior risk | C17 shadow fix |
|---|---|---|---|
| Commodity beta mistaken for spread economics | 011170, 010950 | Stage2/Yellow may be granted on sector bottoming vocabulary | require company-level spread → OPM/FCF bridge |
| Local 4B bounce mistaken for durable thesis | 011170, 011780, 298020 | local MFE hides full-window MAE | split local 4B vs full-window 4B |
| Product spread without inventory/working-capital check | 010950, 011170 | refining/petrochemical inventory losses can erase spread | inventory / utilization / cash conversion guard |
| Strong price action with later decay | 298020, 011780 | early path looks valid, later path is high-MAE | allow Yellow; require margin evidence for Green |

---

## 6. Score simulation

| symbol | baseline-like proxy | current calibrated proxy | C17 shadow-adjusted proxy | decision |
|---:|---:|---:|---:|---|
| 298020 | 79 | 86 | 83 | keep Stage3-Yellow, block Green until margin bridge |
| 011780 | 74 | 80 | 76 | keep Yellow/watch, require spread durability |
| 011170 | 70 | 76 | 58 | downgrade to Stage2/watch or reject |
| 010950 | 63 | 67 | 45 | reject positive stage; counterexample |

### Shadow scoring interpretation

```text
C17_company_level_spread_margin_FCF_bridge_required = +2.0 to +3.0 only when real bridge exists
C17_raw_material_beta_without_margin_bridge_penalty = -3.0 to -5.0
C17_inventory_or_utilization_uncertainty_penalty = -2.0
C17_full_4B_requires_non_price_margin_evidence = hard gate
```

No production scoring change is proposed in this MD. This is a handoff candidate only.

---

## 7. Machine-readable JSONL rows

```jsonl
{"row_type": "case", "case_id": "C17_case_01_298020_2024-04-17", "canonical_archetype_id": "C17_CHEMICAL_COMMODITY_MARGIN_SPREAD", "symbol": "298020", "name": "효성티앤씨", "entry_date": "2024-04-17", "entry_price": 340500, "outcome_label": "positive_with_full_window_guard", "dedupe_key": "C17_CHEMICAL_COMMODITY_MARGIN_SPREAD|298020|Stage3-Yellow|2024-04-17", "novelty_status": "new_symbol_or_new_trigger_family_in_conversation_local_ledger"}
{"row_type": "case", "case_id": "C17_case_02_011780_2024-04-29", "canonical_archetype_id": "C17_CHEMICAL_COMMODITY_MARGIN_SPREAD", "symbol": "011780", "name": "금호석유화학", "entry_date": "2024-04-29", "entry_price": 138300, "outcome_label": "mixed_positive", "dedupe_key": "C17_CHEMICAL_COMMODITY_MARGIN_SPREAD|011780|Stage3-Yellow|2024-04-29", "novelty_status": "new_symbol_or_new_trigger_family_in_conversation_local_ledger"}
{"row_type": "case", "case_id": "C17_case_03_011170_2024-04-29", "canonical_archetype_id": "C17_CHEMICAL_COMMODITY_MARGIN_SPREAD", "symbol": "011170", "name": "롯데케미칼", "entry_date": "2024-04-29", "entry_price": 107700, "outcome_label": "counterexample", "dedupe_key": "C17_CHEMICAL_COMMODITY_MARGIN_SPREAD|011170|Stage2-Actionable|2024-04-29", "novelty_status": "new_symbol_or_new_trigger_family_in_conversation_local_ledger"}
{"row_type": "case", "case_id": "C17_case_04_010950_2024-04-05", "canonical_archetype_id": "C17_CHEMICAL_COMMODITY_MARGIN_SPREAD", "symbol": "010950", "name": "S-Oil", "entry_date": "2024-04-05", "entry_price": 83500, "outcome_label": "counterexample", "dedupe_key": "C17_CHEMICAL_COMMODITY_MARGIN_SPREAD|010950|Stage2-Actionable|2024-04-05", "novelty_status": "new_symbol_or_new_trigger_family_in_conversation_local_ledger"}
{"row_type": "trigger", "schema_family": "v12_sector_archetype_residual", "round": "R4", "loop": 103, "large_sector_id": "L4_MATERIALS_SPREAD_RESOURCE", "canonical_archetype_id": "C17_CHEMICAL_COMMODITY_MARGIN_SPREAD", "fine_archetype_id": "CHEMICAL_COMMODITY_SPREAD_OPM_FCF_BRIDGE_VS_RAW_MATERIAL_BETA_FALSE_POSITIVE", "symbol": "298020", "name": "효성티앤씨", "trigger_type": "Stage3-Yellow", "entry_date": "2024-04-17", "entry_price": 340500, "entry_price_basis": "close", "price_source": "Songdaiki/stock-web atlas/ohlcv_tradable_by_symbol_year/298/298020/2024.csv", "trigger_summary": "스판덱스/섬유화학 spread 회복 기대가 가격에 먼저 반영된 구간. 실제 가격은 30일 내 421,500까지 확장했지만 이후 spread/수요 확인 부족 구간에서는 263,000대까지 되돌림.", "mfe_30d_pct": 23.79, "mae_30d_pct": -9.84, "mfe_90d_pct": 23.79, "mae_90d_pct": -19.97, "mfe_180d_pct": 23.79, "mae_180d_pct": -22.76, "peak_price_180d": 421500, "peak_date_180d": "2024-05-17", "trough_price_180d": 263000, "trough_date_180d": "2024-09-19", "local_4b_proximity": "positive_local_4b", "full_window_4b_status": "blocked_by_later_high_MAE_without_sustained_spread_bridge", "outcome_label": "positive_with_full_window_guard", "raw_component_score_breakdown": {"evidence": 18.0, "price_action": 25.0, "revision_or_margin": 18.0, "risk_penalty": -5.0, "total_proxy": 86.0}, "current_profile_stress_test": "current profile would allow Yellow/near-Green if price strength and theme evidence dominate; needs C17 spread-to-margin-to-FCF bridge to prevent late overstay.", "evidence_quality": "price_exact_stock_web; non_price_source_proxy_only; evidence_url_pending=true"}
{"row_type": "trigger", "schema_family": "v12_sector_archetype_residual", "round": "R4", "loop": 103, "large_sector_id": "L4_MATERIALS_SPREAD_RESOURCE", "canonical_archetype_id": "C17_CHEMICAL_COMMODITY_MARGIN_SPREAD", "fine_archetype_id": "SYNTHETIC_RUBBER_SPREAD_MARGIN_BRIDGE_VS_CHEMICAL_LABEL_HIGH_MAE", "symbol": "011780", "name": "금호석유화학", "trigger_type": "Stage3-Yellow", "entry_date": "2024-04-29", "entry_price": 138300, "entry_price_basis": "close", "price_source": "Songdaiki/stock-web atlas/ohlcv_tradable_by_symbol_year/011/011780/2024.csv", "trigger_summary": "합성고무/페놀/원재료 spread 회복 기대가 4~7월 가격에 반영. 30~90일 구간은 유효했지만 180일에는 102,800까지 밀려 spread 지속성/FCF 전환 확인이 필수.", "mfe_30d_pct": 16.05, "mae_30d_pct": -2.39, "mfe_90d_pct": 20.61, "mae_90d_pct": -7.09, "mfe_180d_pct": 20.61, "mae_180d_pct": -29.28, "peak_price_180d": 166800, "peak_date_180d": "2024-07-12", "trough_price_180d": 97800, "trough_date_180d": "2024-11-15", "local_4b_proximity": "positive_local_4b", "full_window_4b_status": "blocked_by_180d_high_MAE", "outcome_label": "mixed_positive", "raw_component_score_breakdown": {"evidence": 17.0, "price_action": 23.5, "revision_or_margin": 17.0, "risk_penalty": -7.5, "total_proxy": 80.0}, "current_profile_stress_test": "current profile captures 30/90d price alignment but still needs explicit spread durability and inventory/cash bridge before Green.", "evidence_quality": "price_exact_stock_web; non_price_source_proxy_only; evidence_url_pending=true"}
{"row_type": "trigger", "schema_family": "v12_sector_archetype_residual", "round": "R4", "loop": 103, "large_sector_id": "L4_MATERIALS_SPREAD_RESOURCE", "canonical_archetype_id": "C17_CHEMICAL_COMMODITY_MARGIN_SPREAD", "fine_archetype_id": "PETROCHEMICAL_NCC_SPREAD_REBOUND_FALSE_POSITIVE_VS_UTILIZATION_AND_FCF", "symbol": "011170", "name": "롯데케미칼", "trigger_type": "Stage2-Actionable", "entry_date": "2024-04-29", "entry_price": 107700, "entry_price_basis": "close", "price_source": "Songdaiki/stock-web atlas/ohlcv_tradable_by_symbol_year/011/011170/2024.csv", "trigger_summary": "NCC/석화 bottoming과 spread 회복 언어가 붙었으나 5월 단기 반등 이후 11월 64,800까지 하락. 제품 spread 회복이 utilisation, OPM, FCF로 이어지지 않으면 Stage2 이상은 위험.", "mfe_30d_pct": 16.53, "mae_30d_pct": -3.62, "mfe_90d_pct": 16.53, "mae_90d_pct": -20.89, "mfe_180d_pct": 16.53, "mae_180d_pct": -39.83, "peak_price_180d": 125500, "peak_date_180d": "2024-05-20", "trough_price_180d": 64800, "trough_date_180d": "2024-11-18", "local_4b_proximity": "local_bounce_only", "full_window_4b_status": "false_positive_block", "outcome_label": "counterexample", "raw_component_score_breakdown": {"evidence": 13.0, "price_action": 18.0, "revision_or_margin": 8.0, "risk_penalty": -14.0, "total_proxy": 58.0}, "current_profile_stress_test": "current profile can be fooled by price rebound + sector bottoming narrative; C17 requires company-level spread-to-margin-to-FCF proof.", "evidence_quality": "price_exact_stock_web; non_price_source_proxy_only; evidence_url_pending=true"}
{"row_type": "trigger", "schema_family": "v12_sector_archetype_residual", "round": "R4", "loop": 103, "large_sector_id": "L4_MATERIALS_SPREAD_RESOURCE", "canonical_archetype_id": "C17_CHEMICAL_COMMODITY_MARGIN_SPREAD", "fine_archetype_id": "REFINING_CRACK_SPREAD_INVENTORY_MARGIN_VOLATILITY_GUARD", "symbol": "010950", "name": "S-Oil", "trigger_type": "Stage2-Actionable", "entry_date": "2024-04-05", "entry_price": 83500, "entry_price_basis": "close", "price_source": "Songdaiki/stock-web atlas/ohlcv_tradable_by_symbol_year/010/010950/2024.csv", "trigger_summary": "정제마진/crack spread 회복성 언어가 있었지만 4월 초 이후 5~11월 가격은 하락 압력이 우세. 정유는 crack spread, 유가 방향, 재고평가, 배당 체력이 동시에 맞아야 한다.", "mfe_30d_pct": 1.2, "mae_30d_pct": -16.05, "mfe_90d_pct": 1.2, "mae_90d_pct": -20.6, "mfe_180d_pct": 1.2, "mae_180d_pct": -35.69, "peak_price_180d": 84500, "peak_date_180d": "2024-04-08", "trough_price_180d": 53700, "trough_date_180d": "2024-11-13", "local_4b_proximity": "none", "full_window_4b_status": "false_positive_block", "outcome_label": "counterexample", "raw_component_score_breakdown": {"evidence": 12.0, "price_action": 8.0, "revision_or_margin": 7.0, "risk_penalty": -16.0, "total_proxy": 45.0}, "current_profile_stress_test": "current profile should suppress Stage3 when spread signal is not confirmed by refining margin and inventory/earnings bridge.", "evidence_quality": "price_exact_stock_web; non_price_source_proxy_only; evidence_url_pending=true"}
{"row_type": "aggregate_metric", "canonical_archetype_id": "C17_CHEMICAL_COMMODITY_MARGIN_SPREAD", "case_count": 4, "trigger_count": 4, "positive_case_count": 1, "mixed_positive_count": 1, "counterexample_count": 2, "local_4b_watch_count": 2, "current_profile_error_count": 4, "mean_mfe_30d_pct": 14.39, "mean_mae_180d_pct": -31.89, "main_residual": "C17 needs company-level spread → utilisation/ASP → OPM/FCF bridge; commodity price beta and sector bottoming language alone produce high-MAE false positives."}
{"row_type": "shadow_weight", "canonical_archetype_id": "C17_CHEMICAL_COMMODITY_MARGIN_SPREAD", "production_scoring_changed": false, "shadow_rule_candidate": "C17_spread_to_margin_FCF_bridge_required", "suggested_shadow_delta_if_later_implemented": {"company_level_spread_margin_fcf_bridge_bonus": "+2.0 to +3.0", "raw_material_beta_without_margin_bridge_penalty": "-3.0 to -5.0", "inventory_or_utilization_uncertainty_penalty": "-2.0", "full_4b_requires_non_price_margin_evidence": "hard gate"}, "rationale": "Positive local price paths existed, but every weak bridge sample suffered large full-window MAE."}
{"row_type": "residual_contribution", "canonical_archetype_id": "C17_CHEMICAL_COMMODITY_MARGIN_SPREAD", "new_axis_proposed": "C17_company_level_spread_margin_FCF_bridge_required | C17_inventory_utilization_guard | C17_raw_material_beta_false_positive_guard", "existing_axis_strengthened": "stage2_required_bridge | price_only_blowoff_blocks_positive_stage | full_4b_requires_non_price_evidence | local_4b_watch_guard | high_MAE_guardrail", "existing_axis_weakened": null, "do_not_propose_new_weight_delta": false}
```

---

## 8. Residual contribution summary

```text
loop_contribution_label = canonical_archetype_rule_candidate
sector_specific_rule_candidate = true
canonical_archetype_rule_candidate = true

new_axis_proposed:
- C17_company_level_spread_margin_FCF_bridge_required
- C17_inventory_utilization_guard
- C17_raw_material_beta_false_positive_guard
- C17_full_4B_requires_non_price_margin_evidence

existing_axis_strengthened:
- stage2_required_bridge
- price_only_blowoff_blocks_positive_stage
- full_4b_requires_non_price_evidence
- local_4b_watch_guard
- high_MAE_guardrail

existing_axis_weakened = null
do_not_propose_new_weight_delta = false
```

### Coverage contribution

```text
static_index_C17_rows_before = 12
new_rows_this_md = 4
static_index_C17_rows_after_if_accepted = 16
remaining_to_30 = 14
```

### Next recommended archetypes

```text
C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION
C05_EPC_MEGA_CONTRACT_MARGIN_GAP
C24_BIO_TRIAL_DATA_EVENT_RISK
C13_BATTERY_JV_UTILIZATION_AMPC_IRA
C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK
C28_SOFTWARE_SECURITY_CONTRACT_RETENTION
```

---

## 9. Deferred Coding Agent Handoff Prompt

Do not execute this prompt in this research session.

```text
You are the coding agent for Songdaiki/stock_agent.

Input artifact:
- e2r_stock_web_v12_residual_round_R4_loop_103_L4_MATERIALS_SPREAD_RESOURCE_C17_CHEMICAL_COMMODITY_MARGIN_SPREAD_research.md

Task:
1. Parse machine-readable rows from the JSONL block.
2. Add the trigger/case rows to the v12 calibration registry only after dedupe by:
   canonical_archetype_id + symbol + trigger_type + entry_date.
3. Do not overwrite production scoring from this single MD.
4. Stage all proposed C17 rules as shadow-rule candidates:
   - C17_company_level_spread_margin_FCF_bridge_required
   - C17_inventory_utilization_guard
   - C17_raw_material_beta_false_positive_guard
   - C17_full_4B_requires_non_price_margin_evidence
5. If multiple later C17 MDs confirm the same axis, promote the rule through the batch calibration process.
6. Keep price-only local 4B and full-window 4B separate.
7. Preserve evidence_url_pending=true rows as low-confidence non-price evidence until URLs are attached or source verification is completed.
```
