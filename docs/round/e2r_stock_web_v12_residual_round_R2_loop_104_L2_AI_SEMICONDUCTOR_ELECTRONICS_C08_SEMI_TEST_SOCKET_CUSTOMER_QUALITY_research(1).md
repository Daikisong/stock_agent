---
schema_family: v12_sector_archetype_residual
research_session: post_calibrated_sector_archetype_residual_research
mode: historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12
selected_round: R2
selected_loop: 104
large_sector_id: L2_AI_SEMICONDUCTOR_ELECTRONICS
canonical_archetype_id: C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY
fine_archetype_id: TEST_SOCKET_PROBE_CARD_CUSTOMER_QUALITY_BRIDGE_VS_HBM_AI_THEME_HIGH_MAE_FADE
selected_priority_bucket: Priority 0
round_schedule_status: coverage_index_selected
round_sector_consistency: pass
stock_agent_code_access_allowed: false
stock_agent_code_patch_allowed: false
production_scoring_changed: false
shadow_weight_only: true
price_source_repo: Songdaiki/stock-web
price_basis: tradable_raw
price_adjustment_status: raw_unadjusted_marcap
---

# E2R v12 residual research — R2 / C08 semi test socket customer quality

## 0. Selection note

`V12_Research_No_Repeat_Index.md` places `C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY` in Priority 0 with only 14 rows.
The current C08 top-covered symbols are `098120`, `080580`, `058470`, `067310`, `092870`, and `097800`; this run uses `095340`, `131290`, `425420`, and `252990` to avoid hard repeat of the visible coverage spine.

This file follows the v12 rule that this is not live stock discovery, not a stock_agent code patch, and not a production scoring change. It is a standalone historical calibration / residual research MD using `Songdaiki/stock-web` 1D OHLC rows.

## 1. Price source validation

```text
price_atlas_repo = Songdaiki/stock-web
source_name = FinanceData/marcap
price_basis = tradable_raw
price_adjustment_status = raw_unadjusted_marcap
manifest_max_date = 2026-02-20
calibration_shard_root = atlas/ohlcv_tradable_by_symbol_year
corporate_action_policy = block contaminated windows by default
```

Profile checks:

| symbol | profile status | corporate-action caveat | usable note |
|---|---|---|---|
| 095340 ISC | active_like | 2014-12-26, 2023-10-20 | 2024 windows after 2023-10-20 are usable, but prior discontinuity caveat noted |
| 131290 티에스이 | active_like | 2011-04-05, 2011-04-28 | 2024 window usable |
| 425420 티에프이 | active_like | none | 2024 window usable |
| 252990 샘씨엔에스 | active_like | none | 2024 window usable |

## 2. Core residual question

C08 is not “semiconductor smallcap rose with AI/HBM.”
The useful bridge should be narrower:

```text
AI/HBM/server demand
  -> customer qualification / socket design win / probe-card or interface-board adoption
  -> recurring consumable order or high-repeat replacement cycle
  -> gross-margin or revision evidence
  -> Stage2-Actionable / Stage3 candidate
```

The failure pattern is equally important:

```text
HBM/test-socket/probe-card label
  -> local price MFE
  -> no verified customer qualification or order bridge
  -> fade / high MAE
  -> 4B watch or counterexample, not Stage3-Green
```

## 3. Case table

| symbol | name | trigger | entry | peak / MFE | trough / MAE | classification |
|---|---|---:|---:|---:|---:|---|
| 095340 | ISC | 2024-01-19 | 84,100 | 2024-03-28 high 108,000 / +28.42% | 2024-11-18 low 44,700 / -46.85% | counterexample_high_mfe_high_mae |
| 131290 | 티에스이 | 2024-02-13 | 57,000 | 2024-05-03 high 87,800 / +54.04% | 2024-12-09 low 35,000 / -38.60% | positive_local_with_full_4b_high_mae_watch |
| 425420 | 티에프이 | 2024-01-19 | 32,650 | 2024-03-20 high 43,850 / +34.30% | 2024-07-18 low 24,350 / -25.42% | counterexample_test_socket_label_high_mae |
| 252990 | 샘씨엔에스 | 2024-01-19 | 5,680 | 2024-04-18 high 9,280 / +63.38% | 2024-12-09 low 3,520 / -38.03% | positive_local_but_theme_fade_4b_watch |

## 4. Case notes

### 4.1 ISC / 095340 — socket quality label with high-MAE fade

ISC produced a local MFE route: entry close 84,100 on 2024-01-19, then high 108,000 on 2024-03-28.
But the same route later reached low 44,700 on 2024-11-18. That is a C08 residual trap: price strength looked like high-quality test-socket exposure, but the path did not preserve enough evidence for Stage3-Green without verified customer/order/revision confirmation.

Classification:

```text
Stage2 label: allowed only as 4B watch
Stage3-Yellow: reject without non-price bridge
Stage3-Green: reject
4B: yes, local MFE but full-window high-MAE
4C: no hard thesis break proven in this run
```

### 4.2 TSE / 131290 — strong local positive, but full-window 4B watch

TSE is the best local positive in this set. The price route from 2024-02-13 close 57,000 to 2024-05-03 high 87,800 gives +54.04% MFE.
However, the same 2024 route later hit 35,000 on 2024-12-09. C08 should therefore separate **local product-cycle MFE** from **validated customer-quality bridge**.

Classification:

```text
Stage2: possible
Stage2-Actionable: only if customer qualification / recurring socket or probe-card order is verified
Stage3-Yellow: watch
Stage3-Green: block unless revision/customer bridge exists
4B: yes
```

### 4.3 TFE / 425420 — test-socket label false positive

TFE rose from 2024-01-19 close 32,650 to 2024-03-20 high 43,850, +34.30% MFE.
But the route quickly deteriorated to 24,350 on 2024-07-18, -25.42% MAE. This is the cleanest C08 counterexample in this file: product vocabulary alone is not enough.

Classification:

```text
Stage2: weak
Stage2-Actionable: reject without firm order/customer bridge
Stage3-Yellow: reject
Stage3-Green: reject
4B: yes, local spike
4C: not confirmed, but high-MAE failure
```

### 4.4 SamCNS / 252990 — probe-card substrate route with full-window fade

SamCNS shows why “recurring consumable adjacent” needs evidence. It had strong local MFE from 5,680 to 9,280, +63.38%, but full-window low 3,520 means -38.03% MAE.
The route should not be discarded as pure noise, because probe-card substrate supply can be a real bottleneck. But it should remain Stage2/4B watch unless customer qualification and repeat-order evidence is verified.

Classification:

```text
Stage2: possible
Stage2-Actionable: require customer qualification + recurring order bridge
Stage3-Yellow: only with revision evidence
Stage3-Green: block in this run
4B: yes
```

## 5. Raw component score breakdown — shadow only

| component | ISC | TSE | TFE | SamCNS |
|---|---:|---:|---:|---:|
| direct product relevance | 22 | 20 | 18 | 17 |
| customer-quality / qualification evidence | 8 | 9 | 5 | 6 |
| recurring consumable / order bridge | 8 | 9 | 5 | 7 |
| revision / margin bridge | 4 | 5 | 3 | 4 |
| price alignment local | 14 | 18 | 14 | 18 |
| full-window penalty | -18 | -14 | -12 | -15 |
| source-repair penalty | -6 | -6 | -6 | -6 |
| indicative total | 32 | 41 | 27 | 31 |

Interpretation:

```text
This run does not propose immediate production weight changes.
It proposes a C08-specific bridge requirement:
test_socket_score should be gated by customer_qualification + recurring_order + revision/margin confirmation.
Price-only or product-vocabulary-only rallies stay 4B watch.
```

## 6. Machine-readable JSONL

```jsonl
{"row_type": "trigger", "schema_family": "v12_sector_archetype_residual", "research_session": "post_calibrated_sector_archetype_residual_research", "mode": "historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12", "round": "R2", "loop": 104, "large_sector_id": "L2_AI_SEMICONDUCTOR_ELECTRONICS", "canonical_archetype_id": "C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY", "fine_archetype_id": "TEST_SOCKET_PROBE_CARD_CUSTOMER_QUALITY_BRIDGE_VS_HBM_AI_THEME_HIGH_MAE_FADE", "symbol": "095340", "name": "ISC", "trigger_type": "C08_AI_HBM_TEST_SOCKET_PROBE_CARD_CUSTOMER_QUALITY_SOURCE_PROXY", "trigger_date": "2024-01-19", "entry_date": "2024-01-19", "entry_price": 84100, "peak_date": "2024-03-28", "peak_price": 108000, "mfe_pct": 28.42, "trough_date": "2024-11-18", "trough_price": 44700, "mae_pct": -46.85, "classification": "counterexample_high_mfe_high_mae", "calibration_usable": true, "source_status": "source_proxy_only_url_repair_required", "price_source": "Songdaiki/stock-web atlas/ohlcv_tradable_by_symbol_year", "duplicate_check": "new_symbol_vs_C08_top_covered_symbols_in_index"}
{"row_type": "trigger", "schema_family": "v12_sector_archetype_residual", "research_session": "post_calibrated_sector_archetype_residual_research", "mode": "historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12", "round": "R2", "loop": 104, "large_sector_id": "L2_AI_SEMICONDUCTOR_ELECTRONICS", "canonical_archetype_id": "C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY", "fine_archetype_id": "TEST_SOCKET_PROBE_CARD_CUSTOMER_QUALITY_BRIDGE_VS_HBM_AI_THEME_HIGH_MAE_FADE", "symbol": "131290", "name": "티에스이", "trigger_type": "C08_AI_HBM_TEST_SOCKET_PROBE_CARD_CUSTOMER_QUALITY_SOURCE_PROXY", "trigger_date": "2024-02-13", "entry_date": "2024-02-13", "entry_price": 57000, "peak_date": "2024-05-03", "peak_price": 87800, "mfe_pct": 54.04, "trough_date": "2024-12-09", "trough_price": 35000, "mae_pct": -38.6, "classification": "positive_local_with_full_4b_high_mae_watch", "calibration_usable": true, "source_status": "source_proxy_only_url_repair_required", "price_source": "Songdaiki/stock-web atlas/ohlcv_tradable_by_symbol_year", "duplicate_check": "new_symbol_vs_C08_top_covered_symbols_in_index"}
{"row_type": "trigger", "schema_family": "v12_sector_archetype_residual", "research_session": "post_calibrated_sector_archetype_residual_research", "mode": "historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12", "round": "R2", "loop": 104, "large_sector_id": "L2_AI_SEMICONDUCTOR_ELECTRONICS", "canonical_archetype_id": "C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY", "fine_archetype_id": "TEST_SOCKET_PROBE_CARD_CUSTOMER_QUALITY_BRIDGE_VS_HBM_AI_THEME_HIGH_MAE_FADE", "symbol": "425420", "name": "티에프이", "trigger_type": "C08_AI_HBM_TEST_SOCKET_PROBE_CARD_CUSTOMER_QUALITY_SOURCE_PROXY", "trigger_date": "2024-01-19", "entry_date": "2024-01-19", "entry_price": 32650, "peak_date": "2024-03-20", "peak_price": 43850, "mfe_pct": 34.3, "trough_date": "2024-07-18", "trough_price": 24350, "mae_pct": -25.42, "classification": "counterexample_test_socket_label_high_mae", "calibration_usable": true, "source_status": "source_proxy_only_url_repair_required", "price_source": "Songdaiki/stock-web atlas/ohlcv_tradable_by_symbol_year", "duplicate_check": "new_symbol_vs_C08_top_covered_symbols_in_index"}
{"row_type": "trigger", "schema_family": "v12_sector_archetype_residual", "research_session": "post_calibrated_sector_archetype_residual_research", "mode": "historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12", "round": "R2", "loop": 104, "large_sector_id": "L2_AI_SEMICONDUCTOR_ELECTRONICS", "canonical_archetype_id": "C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY", "fine_archetype_id": "TEST_SOCKET_PROBE_CARD_CUSTOMER_QUALITY_BRIDGE_VS_HBM_AI_THEME_HIGH_MAE_FADE", "symbol": "252990", "name": "샘씨엔에스", "trigger_type": "C08_AI_HBM_TEST_SOCKET_PROBE_CARD_CUSTOMER_QUALITY_SOURCE_PROXY", "trigger_date": "2024-01-19", "entry_date": "2024-01-19", "entry_price": 5680, "peak_date": "2024-04-18", "peak_price": 9280, "mfe_pct": 63.38, "trough_date": "2024-12-09", "trough_price": 3520, "mae_pct": -38.03, "classification": "positive_local_but_theme_fade_4b_watch", "calibration_usable": true, "source_status": "source_proxy_only_url_repair_required", "price_source": "Songdaiki/stock-web atlas/ohlcv_tradable_by_symbol_year", "duplicate_check": "new_symbol_vs_C08_top_covered_symbols_in_index"}
```

## 7. Aggregate metric row

```json
{
  "row_type": "aggregate_metric",
  "schema_family": "v12_sector_archetype_residual",
  "round": "R2",
  "loop": 104,
  "large_sector_id": "L2_AI_SEMICONDUCTOR_ELECTRONICS",
  "canonical_archetype_id": "C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY",
  "fine_archetype_id": "TEST_SOCKET_PROBE_CARD_CUSTOMER_QUALITY_BRIDGE_VS_HBM_AI_THEME_HIGH_MAE_FADE",
  "new_independent_case_count": 4,
  "reused_case_count": 0,
  "same_archetype_new_symbol_count": 4,
  "same_archetype_new_trigger_family_count": 2,
  "calibration_usable_case_count": 4,
  "calibration_usable_trigger_count": 4,
  "positive_case_count": 2,
  "counterexample_count": 2,
  "current_profile_error_count": 4,
  "verified_url_repair_needed_count": 4,
  "selection_basis": "docs/core/V12_Research_No_Repeat_Index.md",
  "selected_priority_bucket": "Priority 0",
  "coverage_gap": "C08 rows 14, 30-row target까지 16 부족, 50-row target까지 36 부족",
  "loop_contribution_label": "canonical_archetype_rule_candidate"
}
```

## 8. Shadow rule candidate

```text
new_axis_proposed = c08_customer_qualification_recurring_order_revision_bridge_required_v1

Rule candidate:
- If canonical_archetype_id == C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY:
    - Product vocabulary alone (socket, probe card, interface board, HBM, AI semiconductor) is insufficient for Stage2-Actionable.
    - Stage2-Actionable requires at least one non-price bridge:
        1. customer qualification/design-win evidence,
        2. recurring consumable/socket/probe-card order evidence,
        3. revision / margin / utilization evidence.
    - Stage3-Green requires at least two bridge families plus non-price revision/margin support.
    - If MFE >= 25% but MAE <= -20% and bridge evidence is missing, route to 4B watch / high-MAE guardrail.
```

## 9. Deferred Coding Agent Handoff Prompt

```text
Do not execute this handoff in the research session.

Read this MD and batch-apply only after multiple v12 residual MD files are accumulated.

Task:
- Add/adjust shadow-only C08 guardrail candidate:
  c08_customer_qualification_recurring_order_revision_bridge_required_v1
- Do not change production scoring directly without aggregate validation.
- Use trigger rows in this MD as evidence candidates only.
- Confirm duplicates against canonical_archetype_id + symbol + trigger_type + entry_date.
- Keep price-only HBM/test-socket/probe-card rallies as 4B watch unless customer/order/revision bridge is present.
```

## 10. Next research state

```text
completed_round = R2
completed_loop = 104
selection_basis = docs/core/V12_Research_No_Repeat_Index.md
selected_priority_bucket = Priority 0
round_schedule_status = coverage_index_selected
round_sector_consistency = pass

next_recommended_archetypes = C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF, C01_ORDER_BACKLOG_MARGIN_BRIDGE, C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH
```

## 11. Residual contribution summary

```text
new_independent_case_count = 4
reused_case_count = 0
same_archetype_new_symbol_count = 4
same_archetype_new_trigger_family_count = 2
calibration_usable case 수 = 4
calibration_usable trigger 수 = 4
positive_case_count = 2
counterexample_count = 2
current_profile_error_count = 4
verified_url_repair_needed_count = 4

diversity_score_summary = C08 Priority 0 보강 + ISC/TFE high-MAE counterexamples + TSE/SamCNS local positive 4B watch
do_not_propose_new_weight_delta = false
sector_specific_rule_candidate = true
canonical_archetype_rule_candidate = true
loop_contribution_label = canonical_archetype_rule_candidate
existing_axis_strengthened = full_4b_requires_non_price_evidence scoped to C08 socket/probe-card/customer-quality rallies
existing_axis_weakened = null
```
