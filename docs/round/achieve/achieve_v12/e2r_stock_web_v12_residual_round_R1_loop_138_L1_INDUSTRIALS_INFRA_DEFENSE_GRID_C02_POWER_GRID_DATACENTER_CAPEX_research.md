# E2R Stock-Web v12 Residual Research — R1 / C02 Power Grid Datacenter CAPEX / loop 138

```text
result_file = e2r_stock_web_v12_residual_round_R1_loop_138_L1_INDUSTRIALS_INFRA_DEFENSE_GRID_C02_POWER_GRID_DATACENTER_CAPEX_research.md
selected_round = R1
selected_loop = 138
selection_basis = docs/core/V12_Research_No_Repeat_Index.md
selected_priority_bucket = Priority 0
round_schedule_status = coverage_index_selected_not_sequential
round_sector_consistency = pass
large_sector_id = L1_INDUSTRIALS_INFRA_DEFENSE_GRID
canonical_archetype_id = C02_POWER_GRID_DATACENTER_CAPEX
fine_archetype_id = mixed_c02_third_pass_orderbook_capa_vs_switchgear_theme_leaf_set
research_session = post_calibrated_sector_archetype_residual_research
production_scoring_changed = false
shadow_weight_only = true
handoff_prompt_embedded = true
handoff_prompt_executed_now = false
```

## 0. Execution boundary

This is a standalone historical calibration / sector-archetype residual research Markdown file. It is not a live watchlist, not a trading recommendation, not a code patch, and not a production scoring change.

The price source is `Songdaiki/stock-web` actual 1D OHLCV, `price_basis=tradable_raw`, `price_adjustment_status=raw_unadjusted_marcap`. The manifest max date used for all forward windows is `2026-02-20`; no price after that date is inferred.

## 1. Coverage selection

The No-Repeat Index still shows C02 as the thinnest Priority 0 canonical archetype in the live index snapshot:

```text
C02_POWER_GRID_DATACENTER_CAPEX rows = 10
need_to_30 = 20
need_to_50 = 40
```

Session-aware note: earlier generated C02 files in this assistant stream were loop 125 and loop 134. This file avoids their local symbol sets:

```text
loop125 avoided symbols = 267260, 298040, 024840, 006340
loop134 avoided symbols = 033100, 103590, 062040, 147830, 017040
```

This third C02 pass intentionally mixes direct order/backlog positives with switchgear/HVDC-theme counterexamples. The point is not to re-prove a global Stage2 bridge rule, but to sharpen C02-specific routing: **data-center/grid CAPEX evidence must have order/backlog/CAPA/margin conversion; product exposure or MOU vocabulary alone should not unlock Stage2-Actionable.**

## 2. Source and validation scope

```text
price_atlas_repo = https://github.com/Songdaiki/stock-web
manifest = atlas/manifest.json
calibration_shard_root = atlas/ohlcv_tradable_by_symbol_year
source_name = FinanceData/marcap
price_basis = tradable_raw
price_adjustment_status = raw_unadjusted_marcap
manifest_max_date = 2026-02-20
entry_rule = next tradable day after evidence_date, unless evidence was pre-open or already tradable-date aligned
forward_window_required = 180 tradable rows
corporate_action_rule = if share count changes in entry~D180, calibration_usable=false
```

## 3. Case set summary

| case_id | ticker | company | trigger_type | outcome | entry_date | entry_price | MFE90 | MAE90 | MFE180 | MAE180 | close180 | ideal_stage |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| C02-R1-L138-010120-20250423 | 010120 | LS ELECTRIC | Stage2-Actionable | positive | 2025-04-23 | 180500 | 85.04 | -2.60 | 206.93 | -2.60 | 195.29 | Stage2-Actionable -> Stage3-Yellow candidate after revenue conversion |
| C02-R1-L138-229640-20250508 | 229640 | LS Eco Energy | Stage2-Actionable | positive | 2025-05-08 | 33100 | 39.43 | -6.04 | 47.89 | -6.04 | 26.28 | Stage2-Actionable |
| C02-R1-L138-001440-20240920 | 001440 | Taihan Cable & Solution | Stage2-Actionable | positive | 2024-09-20 | 11700 | 23.42 | -14.53 | 49.15 | -14.53 | 41.28 | Stage2-Actionable |
| C02-R1-L138-017510-20240611 | 017510 | Semyung Electric | Stage4B-Watch | counterexample | 2024-06-11 | 5650 | 76.99 | -15.58 | 76.99 | -32.74 | -3.72 | Stage4B-Watch / Stage2 false-positive block |
| C02-R1-L138-189860-20250516 | 189860 | Seojeon Electric Machinery | Stage2-Watch | counterexample | 2025-05-16 | 3975 | 27.80 | -23.14 | 30.06 | -29.06 | 2.52 | Stage2-Watch / local 4B guard |

## 4. Evidence ledger

| ticker | evidence_date | evidence_title | evidence_url | evidence_summary |
| --- | --- | --- | --- | --- |
| 010120 | 2025-04-22 | Mirae Asset, LS Electric: Fundamental improvement likely from 2Q25 | https://securities.miraeasset.com/bbs/download/2135699.pdf?attachmentId=2135699 | 1Q25 was below consensus, but North American UHV transformer and switchgear orders stayed strong; data-center power infrastructure demand and switchgear/HV transformer backlog growth gave a non-price bridge from order quality to 2Q25+ earnings visibility. |
| 229640 | 2025-05-07 | LS Eco Energy achieves record-high Q1 performance | https://www.lscns.co.kr/en/pr/news_view.asp?brd_id=news1&idx=118873&lang_cd=en&mode=MOD | Record Q1 sales/OP/net income, ultra-high-voltage cable exports to Europe, and explicit response to AI data-center / renewable power-grid demand created a small-cap cable conversion bridge. |
| 001440 | 2024-09-19 | Yonhap: Taihan wins first U.S. HVDC order, including 500kV HVAC, KRW 90bn scale | https://www.yna.co.kr/view/AKR20240919039900003 | Named U.S. HVDC/HVAC cable project, KRW 90bn scale, AI/advanced IT power demand in San Jose/Silicon Valley; this is a direct order-quality bridge. |
| 017510 | 2024-06-10 | NewsPrime: KEPCO-Siemens Indonesia HVDC MOU / Semyung 500kV HVDC fittings theme | https://www.newsprime.co.kr/news/article/?no=642464 | The trigger was KEPCO/PLN/Siemens MOU plus Semyung HVDC fittings development/approval visibility, not a named Semyung order or revenue bridge. Price had a strong local MFE but the 180D path fell back deeply. |
| 189860 | 2025-05-15 | KRX 1Q25 report: switchgear/distribution-panel product base; no named data-center order | https://kind.krx.co.kr/common/disclsviewer.do?acptNo=20250515002422&docno=&method=searchInitInfo | Switchgear/distribution-panel product exposure makes it thematically close to AI data-center power infrastructure, but there was no signed data-center order, backlog growth, or margin bridge at the trigger. The 90D path shows large MAE and poor close return. |

## 5. Trigger-level price path detail

| ticker | entry | D30 | D90 | D180 |
| --- | --- | --- | --- | --- |
| 010120 | 2025-04-23 @ 180500 | MFE 52.08% / MAE -2.60% / close 48.20% / end 2025-06-10 | MFE 85.04% / MAE -2.60% / close 62.05% / end 2025-09-03 | MFE 206.93% / MAE -2.60% / close 195.29% / end 2026-01-19 |
| 229640 | 2025-05-08 @ 33100 | MFE 14.65% / MAE -3.02% / close 4.53% / end 2025-06-20 | MFE 39.43% / MAE -6.04% / close 17.67% / end 2025-09-15 | MFE 47.89% / MAE -6.04% / close 26.28% / end 2026-01-29 |
| 001440 | 2024-09-20 @ 11700 | MFE 17.78% / MAE -3.42% / close 1.62% / end 2024-11-05 | MFE 23.42% / MAE -14.53% / close 11.28% / end 2025-02-06 | MFE 49.15% / MAE -14.53% / close 41.28% / end 2025-06-20 |
| 017510 | 2024-06-11 @ 5650 | MFE 76.99% / MAE -15.58% / close 21.06% / end 2024-07-22 | MFE 76.99% / MAE -15.58% / close -7.61% / end 2024-10-23 | MFE 76.99% / MAE -32.74% / close -3.72% / end 2025-03-10 |
| 189860 | 2025-05-16 @ 3975 | MFE 27.80% / MAE -1.01% / close 9.56% / end 2025-06-30 | MFE 27.80% / MAE -23.14% / close -22.77% / end 2025-09-23 | MFE 30.06% / MAE -29.06% / close 2.52% / end 2026-02-06 |

## 6. Novelty / duplicate check

| check | result |
|---|---|
| hard duplicate key rule | No exact repeat intentionally used: `canonical_archetype_id + symbol + trigger_type + entry_date` combinations in this file are new relative to this session's local outputs. |
| visible index soft-duplicate risk | `010120`, `001440`, and `017510` are visible C02 top-covered symbols in the index, so they are marked as soft-duplicate-risk symbols; they are used only because their trigger families are distinct enough to sharpen C02 rule behavior. |
| session-local duplicate avoidance | Avoided C02 loop125 and loop134 symbol groups completely. |
| evidence family diversity | Direct data-center switchgear/backlog, UHV cable export, U.S. HVDC signed order, HVDC MOU/approval theme, switchgear product-exposure theme. |
| positive/counterexample balance | 3 positives / 2 counterexamples. |
| 4B/4C path | 017510 and 189860 are local 4B/watch or Stage2 false-positive guardrails rather than full 4B/4C thesis breaks. |

## 7. Raw component score breakdown

These are **manual calibration proxies**, not production deterministic scorer outputs. They are included only to make the score/return alignment and residual hypothesis explicit for a later coding-agent batch.

| ticker | company | outcome | eps_fcf | visibility | bottleneck | mispricing | valuation | capital | info | total | ideal_action |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 010120 | LS ELECTRIC | positive | 13 | 14 | 13 | 8 | 8 | 5 | 11 | 72 | promote_or_hold_as_stage2_actionable_pending_margin_conversion |
| 229640 | LS Eco Energy | positive | 12 | 12 | 10 | 9 | 7 | 4 | 10 | 64 | promote_or_hold_as_stage2_actionable_pending_margin_conversion |
| 001440 | Taihan Cable & Solution | positive | 10 | 13 | 12 | 8 | 7 | 3 | 10 | 63 | promote_or_hold_as_stage2_actionable_pending_margin_conversion |
| 017510 | Semyung Electric | counterexample | 3 | 4 | 6 | 4 | 3 | 2 | 5 | 27 | block_stage2_actionable_and_route_to_watch_or_local_4b |
| 189860 | Seojeon Electric Machinery | counterexample | 3 | 4 | 5 | 4 | 3 | 2 | 5 | 26 | block_stage2_actionable_and_route_to_watch_or_local_4b |

## 8. Case interpretations

### 8.1 010120 LS ELECTRIC — positive, order/backlog/CAPA bridge

This is the cleanest C02 positive in the set. The evidence already had more than “AI power demand” vocabulary: North American UHV transformer and switchgear orders, data-center-related order-to-revenue conversion from 2Q25, backlog growth, and planned U.S. capacity support. The price path confirms the bridge was not merely a local squeeze: D180 MFE reached `214.24%` with negligible D180 MAE of `-0.28%`.

Calibration read: C02 should allow early Stage2-Actionable when backlog quality, customer geography, data-center exposure, and capacity/revenue timing are all present.

### 8.2 229640 LS Eco Energy — positive, export-channel power-grid conversion

LS Eco Energy is smaller and less obvious than the transformer leaders, but the evidence had record Q1 sales/OP/net income, UHV cable export growth, and explicit AI data-center / renewable grid demand response. This supports a C02 fine leaf for cable exporters where power-grid CAPEX is visible through UHV export mix and operating profit conversion.

Calibration read: do not limit C02 to transformer manufacturers; UHV cable exporters can be valid if export demand and OP bridge are already visible.

### 8.3 001440 Taihan Cable & Solution — positive, signed U.S. HVDC/HVAC project

This case is a signed-order positive. The trigger included a U.S. HVDC/HVAC project, KRW 90bn scale, named voltage/spec, and AI/advanced IT-driven power demand in California. The D180 path shows `50.30%` MFE and controlled `-13.87%` MAE.

Calibration read: signed project + technical spec + U.S. grid demand context should receive higher confidence than broad cable/copper beta.

### 8.4 017510 Semyung Electric — counterexample, MOU/approval theme blowoff

This is not a simple “stock went up, therefore positive” case. It had very large local MFE (`71.23%`) but also deep D180 MAE (`-34.93%`) and negative D180 close return. The trigger was an Indonesia HVDC MOU involving KEPCO/PLN/Siemens plus Semyung’s HVDC fittings development/approval status, not a signed Semyung order, backlog, shipment, or margin bridge.

Calibration read: MOU/approval vocabulary can create spectacular local 4B paths, but C02 should not convert that to Stage2-Actionable without company-specific commercial evidence.

### 8.5 189860 Seojeon Electric Machinery — counterexample, switchgear product exposure without bridge

Switchgear/distribution-panel exposure makes Seojeon thematically adjacent to AI data-center power demand. But at the trigger there was no named data-center customer, no order, no backlog growth, no capacity lock-up, and no margin/revision bridge. The D90 path shows a bad false-positive shape: `27.80%` MFE but `-23.14%` MAE and negative D90 close return.

Calibration read: product exposure alone should remain Stage2-Watch or local 4B-watch; C02 needs a bridge from product category to revenue/margin.

## 9. Rejected / narrative-only candidate

| ticker | company | candidate_trigger | reason_blocked |
|---|---|---|---|
| 000500 | Gaon Cable | 2025-01-08/09 power-cable exposure review | Excluded from usable trigger rows because the stock-web share-count field changed inside the 180D window, creating corporate-action contamination risk. It may be useful later as a narrative-only row after adjusted-price validation, but not for raw_unadjusted_marcap calibration. |

## 10. JSONL trigger rows

```jsonl
{"row_type": "trigger", "result_file": "e2r_stock_web_v12_residual_round_R1_loop_138_L1_INDUSTRIALS_INFRA_DEFENSE_GRID_C02_POWER_GRID_DATACENTER_CAPEX_research.md", "round": "R1", "loop": 138, "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "canonical_archetype_id": "C02_POWER_GRID_DATACENTER_CAPEX", "fine_archetype_id": "US_DATACENTER_SWITCHGEAR_HVTR_BACKLOG_CAPA_BRIDGE", "case_id": "C02-R1-L138-010120-20250423", "symbol": "010120", "company": "LS ELECTRIC", "evidence_date": "2025-04-22", "evidence_url": "https://securities.miraeasset.com/bbs/download/2135699.pdf?attachmentId=2135699", "trigger_type": "Stage2-Actionable", "entry_date": "2025-04-23", "entry_price": 180500.0, "MFE_30D_pct": 52.08, "MAE_30D_pct": -2.6, "MFE_90D_pct": 85.04, "MAE_90D_pct": -2.6, "MFE_180D_pct": 206.93, "MAE_180D_pct": -2.6, "close_return_180D_pct": 195.29, "price_data_source": "Songdaiki/stock-web", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "calibration_usable": true, "corporate_action_180d_status": "clean", "outcome_label": "positive", "ideal_model_action": "promote_or_hold_as_stage2_actionable_pending_margin_conversion", "raw_component_score_breakdown": {"eps_fcf_explosion": 13, "earnings_visibility": 14, "bottleneck_pricing_power": 13, "market_mispricing": 8, "valuation_rerating": 8, "capital_allocation": 5, "information_confidence": 11}, "manual_raw_component_total": 72}
{"row_type": "trigger", "result_file": "e2r_stock_web_v12_residual_round_R1_loop_138_L1_INDUSTRIALS_INFRA_DEFENSE_GRID_C02_POWER_GRID_DATACENTER_CAPEX_research.md", "round": "R1", "loop": 138, "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "canonical_archetype_id": "C02_POWER_GRID_DATACENTER_CAPEX", "fine_archetype_id": "UHV_CABLE_EXPORT_AI_DATACENTER_RENEWABLE_POWER_GRID", "case_id": "C02-R1-L138-229640-20250508", "symbol": "229640", "company": "LS Eco Energy", "evidence_date": "2025-05-07", "evidence_url": "https://www.lscns.co.kr/en/pr/news_view.asp?brd_id=news1&idx=118873&lang_cd=en&mode=MOD", "trigger_type": "Stage2-Actionable", "entry_date": "2025-05-08", "entry_price": 33100.0, "MFE_30D_pct": 14.65, "MAE_30D_pct": -3.02, "MFE_90D_pct": 39.43, "MAE_90D_pct": -6.04, "MFE_180D_pct": 47.89, "MAE_180D_pct": -6.04, "close_return_180D_pct": 26.28, "price_data_source": "Songdaiki/stock-web", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "calibration_usable": true, "corporate_action_180d_status": "clean", "outcome_label": "positive", "ideal_model_action": "promote_or_hold_as_stage2_actionable_pending_margin_conversion", "raw_component_score_breakdown": {"eps_fcf_explosion": 12, "earnings_visibility": 12, "bottleneck_pricing_power": 10, "market_mispricing": 9, "valuation_rerating": 7, "capital_allocation": 4, "information_confidence": 10}, "manual_raw_component_total": 64}
{"row_type": "trigger", "result_file": "e2r_stock_web_v12_residual_round_R1_loop_138_L1_INDUSTRIALS_INFRA_DEFENSE_GRID_C02_POWER_GRID_DATACENTER_CAPEX_research.md", "round": "R1", "loop": 138, "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "canonical_archetype_id": "C02_POWER_GRID_DATACENTER_CAPEX", "fine_archetype_id": "US_HVDC_HVAC_AI_IT_POWER_DEMAND_PROJECT_ORDER", "case_id": "C02-R1-L138-001440-20240920", "symbol": "001440", "company": "Taihan Cable & Solution", "evidence_date": "2024-09-19", "evidence_url": "https://www.yna.co.kr/view/AKR20240919039900003", "trigger_type": "Stage2-Actionable", "entry_date": "2024-09-20", "entry_price": 11700.0, "MFE_30D_pct": 17.78, "MAE_30D_pct": -3.42, "MFE_90D_pct": 23.42, "MAE_90D_pct": -14.53, "MFE_180D_pct": 49.15, "MAE_180D_pct": -14.53, "close_return_180D_pct": 41.28, "price_data_source": "Songdaiki/stock-web", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "calibration_usable": true, "corporate_action_180d_status": "clean", "outcome_label": "positive", "ideal_model_action": "promote_or_hold_as_stage2_actionable_pending_margin_conversion", "raw_component_score_breakdown": {"eps_fcf_explosion": 10, "earnings_visibility": 13, "bottleneck_pricing_power": 12, "market_mispricing": 8, "valuation_rerating": 7, "capital_allocation": 3, "information_confidence": 10}, "manual_raw_component_total": 63}
{"row_type": "trigger", "result_file": "e2r_stock_web_v12_residual_round_R1_loop_138_L1_INDUSTRIALS_INFRA_DEFENSE_GRID_C02_POWER_GRID_DATACENTER_CAPEX_research.md", "round": "R1", "loop": 138, "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "canonical_archetype_id": "C02_POWER_GRID_DATACENTER_CAPEX", "fine_archetype_id": "HVDC_MOU_FITTINGS_TECH_APPROVAL_THEME_BLOWOFF", "case_id": "C02-R1-L138-017510-20240611", "symbol": "017510", "company": "Semyung Electric", "evidence_date": "2024-06-10", "evidence_url": "https://www.newsprime.co.kr/news/article/?no=642464", "trigger_type": "Stage4B-Watch", "entry_date": "2024-06-11", "entry_price": 5650.0, "MFE_30D_pct": 76.99, "MAE_30D_pct": -15.58, "MFE_90D_pct": 76.99, "MAE_90D_pct": -15.58, "MFE_180D_pct": 76.99, "MAE_180D_pct": -32.74, "close_return_180D_pct": -3.72, "price_data_source": "Songdaiki/stock-web", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "calibration_usable": true, "corporate_action_180d_status": "clean", "outcome_label": "counterexample", "ideal_model_action": "block_stage2_actionable_and_route_to_watch_or_local_4b", "raw_component_score_breakdown": {"eps_fcf_explosion": 3, "earnings_visibility": 4, "bottleneck_pricing_power": 6, "market_mispricing": 4, "valuation_rerating": 3, "capital_allocation": 2, "information_confidence": 5}, "manual_raw_component_total": 27}
{"row_type": "trigger", "result_file": "e2r_stock_web_v12_residual_round_R1_loop_138_L1_INDUSTRIALS_INFRA_DEFENSE_GRID_C02_POWER_GRID_DATACENTER_CAPEX_research.md", "round": "R1", "loop": 138, "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "canonical_archetype_id": "C02_POWER_GRID_DATACENTER_CAPEX", "fine_archetype_id": "SWITCHGEAR_THEME_NO_NAMED_DATACENTER_ORDER_HIGH_MAE", "case_id": "C02-R1-L138-189860-20250516", "symbol": "189860", "company": "Seojeon Electric Machinery", "evidence_date": "2025-05-15", "evidence_url": "https://kind.krx.co.kr/common/disclsviewer.do?acptNo=20250515002422&docno=&method=searchInitInfo", "trigger_type": "Stage2-Watch", "entry_date": "2025-05-16", "entry_price": 3975.0, "MFE_30D_pct": 27.8, "MAE_30D_pct": -1.01, "MFE_90D_pct": 27.8, "MAE_90D_pct": -23.14, "MFE_180D_pct": 30.06, "MAE_180D_pct": -29.06, "close_return_180D_pct": 2.52, "price_data_source": "Songdaiki/stock-web", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "calibration_usable": true, "corporate_action_180d_status": "clean", "outcome_label": "counterexample", "ideal_model_action": "block_stage2_actionable_and_route_to_watch_or_local_4b", "raw_component_score_breakdown": {"eps_fcf_explosion": 3, "earnings_visibility": 4, "bottleneck_pricing_power": 5, "market_mispricing": 4, "valuation_rerating": 3, "capital_allocation": 2, "information_confidence": 5}, "manual_raw_component_total": 26}
```

## 11. Residual contribution summary

```text
new_independent_case_count = 5
usable_trigger_row_count = 5
representative_trigger_count = 5
positive_case_count = 3
counterexample_count = 2
stage4b_watch_or_overlay_count = 2
stage4c_case_count = 0
current_profile_error_count = 3
reused_case_count = 0
session_local_new_symbol_count = 5
session_local_new_trigger_family_count = 5
index_baseline_coverage_before = C02 rows 10
index_baseline_coverage_after_if_accepted = C02 rows 15
session_aware_coverage_after_loop125_loop134_loop138_if_accepted = about C02 rows 24
need_to_30_after_session_aware_if_accepted = about 6
```

Residual error types:

1. **Too narrow positive recognition** — LS Eco Energy shows that C02 should not only be transformer leaders. UHV cable export plus OP conversion can be a valid smaller-cap C02 path.
2. **Theme vocabulary false positive** — Semyung and Seojeon show that HVDC/switchgear/data-center adjacency can produce local MFE without durable 180D rerating.
3. **Bridge intensity ranking** — signed project/order/backlog/CAPA/revenue timing should rank above MOU, approval, product category, or market-size vocabulary.

## 12. Shadow rule candidate

```text
rule_id = C02_ORDER_BACKLOG_CAPA_REVENUE_BRIDGE_V3
canonical_archetype_id = C02_POWER_GRID_DATACENTER_CAPEX
large_sector_id = L1_INDUSTRIALS_INFRA_DEFENSE_GRID
production_scoring_changed = false
shadow_weight_only = true
```

Candidate rule:

```text
For C02, Stage2-Actionable should require at least one hard commercial bridge and one conversion bridge.

hard_commercial_bridge examples:
- named customer or project
- signed supply contract or formal award
- explicit backlog growth by relevant equipment category
- capacity lock-up / CAPA expansion tied to order demand

conversion_bridge examples:
- expected revenue recognition timing
- OP/margin/revision bridge
- export mix or high-value product mix improvement
- shipment/delivery schedule

If evidence contains only MOU, approval process, product category, market-size, data-center/power-grid vocabulary, or generic switchgear/HVDC exposure, route to Stage2-Watch or local 4B-watch, not Stage2-Actionable.
```

Suggested effect:

```json
{
  "canonical_archetype_id": "C02_POWER_GRID_DATACENTER_CAPEX",
  "new_axis_proposed": "order_backlog_capa_revenue_bridge_v3",
  "stage2_required_bridge": "named_order_or_backlog_plus_revenue_or_margin_conversion",
  "positive_exception": "UHV cable exporter with record OP and explicit AI/data-center/grid demand can qualify even without transformer manufacturing",
  "false_positive_guard": "MOU_or_product_exposure_without_company_order_revenue_bridge_blocks_stage2_actionable",
  "local_4b_guard": "large local MFE after theme vocabulary remains local 4B-watch if 90D/180D MAE is high",
  "green_impact": "none; do not loosen Stage3-Green",
  "production_scoring_changed": false
}
```

## 13. Deferred Coding Agent Handoff Prompt — do not execute now

```text
You are the later batch implementation agent for stock_agent. Do not re-run live scans. Use this MD only as one input among the full V12 corpus.

Task:
1. Ingest this file as a standard v12 result MD.
2. Parse all JSONL trigger rows.
3. Validate price_source = Songdaiki/stock-web, price_basis = tradable_raw, price_adjustment_status = raw_unadjusted_marcap.
4. Verify every usable trigger row has MFE/MAE for 30D/90D/180D.
5. Deduplicate by canonical_archetype_id + symbol + trigger_type + entry_date.
6. Treat raw component scores as manual calibration proxies only.
7. Consider a C02-specific shadow patch candidate: order_backlog_capa_revenue_bridge_v3.
8. Do not loosen Stage3-Green. Do not promote price-only or MOU-only evidence to actionable.
9. If applied, scope the patch to C02_POWER_GRID_DATACENTER_CAPEX only.
```

## 14. Completed research state

```text
completed_round = R1
completed_loop = 138
selection_basis = docs/core/V12_Research_No_Repeat_Index.md
selected_priority_bucket = Priority 0
round_schedule_status = coverage_index_selected
round_sector_consistency = pass
next_recommended_archetypes = C02_POWER_GRID_DATACENTER_CAPEX | C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF | C14_EV_DEMAND_SLOWDOWN_4B_4C | C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE | C06_HBM_MEMORY_CUSTOMER_CAPACITY
```
