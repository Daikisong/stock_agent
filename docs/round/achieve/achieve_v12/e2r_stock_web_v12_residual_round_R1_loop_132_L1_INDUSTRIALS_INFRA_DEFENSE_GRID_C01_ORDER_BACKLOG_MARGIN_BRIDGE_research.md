# stock-web v12 residual calibration research

- filename: `e2r_stock_web_v12_residual_round_R1_loop_132_L1_INDUSTRIALS_INFRA_DEFENSE_GRID_C01_ORDER_BACKLOG_MARGIN_BRIDGE_research.md`
- mode: `historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12`
- selected_round: `R1`
- selected_loop: `132`
- selection_basis: `docs/core/V12_Research_No_Repeat_Index.md`
- selected_priority_bucket: `Priority 0`
- round_schedule_status: `coverage_index_selected_not_sequential`
- round_sector_consistency: `pass`
- large_sector_id: `L1_INDUSTRIALS_INFRA_DEFENSE_GRID`
- canonical_archetype_id: `C01_ORDER_BACKLOG_MARGIN_BRIDGE`
- fine_archetype_id: `mixed_c01_shipbuilding_backlog_price_quality_margin_bridge_leaf_set`
- loop_objective: `coverage_gap_fill|positive_vs_counterexample_balance|backlog_quality_gate|margin_bridge_timing_test|4B_non_price_requirement_stress_test`
- price_source: `Songdaiki/stock-web`
- price_basis: `tradable_raw`
- price_adjustment_status: `raw_unadjusted_marcap`
- stock_web_manifest_max_date: `2026-02-20`
- do_not_propose_new_weight_delta: `false`
- production_scoring_patch_executed: `false`
- shadow_weight_only: `true`

---

## 1. Scheduler decision

The No-Repeat Index was used only as the duplicate and coverage ledger. C01 was selected because the latest visible Priority 0 table showed C01 at 19 representative rows, behind the already-covered session targets C02, C09, C14, C10, C06, C07, and C11. R1 was then derived from the selected canonical archetype and large sector.

This run deliberately avoids the visible top-covered C01 cluster where possible. The Index showed the largest visible C01 repeat names as `012450`, `064350`, `079550`, `000720`, `004960`, and `006360`; this MD instead uses shipbuilding and industrial backlog/margin bridge names `010140`, `009540`, `329180`, `010620`, and `042660`.

```yaml
coverage_before:
  canonical_archetype_id: C01_ORDER_BACKLOG_MARGIN_BRIDGE
  representative_rows: 19
  selected_priority_bucket: Priority 0
coverage_after_if_accepted:
  added_representative_trigger_rows: 6
  representative_rows: 25
  need_to_30_after_if_accepted: 5
  need_to_50_after_if_accepted: 25
same_archetype_new_symbol_count: 5
same_archetype_new_trigger_family_count: 6
new_independent_case_count: 5
usable_trigger_row_count: 6
representative_trigger_count: 6
positive_case_count: 4
counterexample_count: 2
stage4b_watch_or_overlay_count: 2
stage4c_success_count: 0
current_profile_error_count: 4
```

---

## 2. Archetype hypothesis

C01 is not simply “order backlog is high.” It should require a bridge from orderbook to earnings quality:

1. backlog/order intake quality,
2. high-value vessel or industrial product mix,
3. delivery/revenue recognition visibility,
4. margin or revision bridge,
5. working-capital / execution risk check.

For shipbuilding, the good C01 signal behaves like a shipyard dry dock filling with high-priced vessels: the orderbook is only the hull; the rerating starts when price, delivery slot, and margin steel plates are welded into one cash-flow vessel. If the model only sees “large order” or “target nearly achieved,” it can enter after the share price has already sailed and then suffer large MAE.

### Proposed C01 rule candidate

`C01_BACKLOG_PRICE_QUALITY_MARGIN_BRIDGE_GATE_V1`

- **Promote to Stage2-Actionable / Stage3-Yellow candidate** only when backlog growth is tied to price-quality mix and margin conversion evidence.
- **Keep Stage2-Watch** when backlog is visible but the current quarter still shows losses or there is no margin bridge.
- **Apply 4B-watch overlay** when headline orders arrive after a sharp local price run and forward MFE is small relative to MAE.
- **Do not route to 4C** on a single quarterly loss if backlog quality and later margin evidence remain intact.

---

## 3. Case table

| case_id | symbol | company | trigger_date | entry_date | entry_price | canonical trigger | label | fine leaf | short diagnosis |
|---|---:|---|---:|---:|---:|---|---|---|---|
| C01-132-01 | 010140 | Samsung Heavy Industries | 2023-06-13 | 2023-06-13 | 6500 | Stage2-Actionable | positive | LNG_backlog_price_quality | LNG carrier order + backlog mix gave early price-path confirmation. |
| C01-132-02 | 009540 | HD Korea Shipbuilding & Offshore Engineering | 2023-08-04 | 2023-08-04 | 121500 | 4B-Watch | counterexample | late_order_target_high_MAE | Order target almost filled but entry came after shipbuilding beta move; poor 90D MAE. |
| C01-132-03 | 329180 | HD Hyundai Heavy Industries | 2024-07-25 | 2024-07-25 | 177500 | Stage2-Actionable | positive | order_screening_margin_recovery | Q2 profit recovery and order-screening/cost reduction bridge led to durable rerating. |
| C01-132-04 | 010620 | HD Hyundai Mipo | 2024-07-25 | 2024-07-25 | 102600 | Stage2-Actionable | positive | loss_to_profit_margin_bridge | Q2 profit swing converted backlog skepticism into margin evidence. |
| C01-132-05 | 042660 | Hanwha Ocean | 2024-02-22 | 2024-02-22 | 21750 | Stage2-Watch | positive_after_watch | loss_narrowing_then_turnaround | Still loss-making, but loss narrowing + later Q1 profit made hard block too strict. |
| C01-132-06 | 042660 | Hanwha Ocean | 2024-07-26 | 2024-07-26 | 30950 | 4B-Watch | counterexample | quarterly_loss_high_MAE | Q2 return to operating loss produced immediate high MAE before later theme recovery. |

---

## 4. Evidence map

### 4.1 Samsung Heavy Industries — C01-132-01

- Evidence date: 2023-06-13.
- Evidence URL: `https://en.yna.co.kr/view/AEN20230613005100320`
- Evidence summary: Samsung Heavy secured a 659bn-won order for two LNG carriers. The same article reported backlog of $27bn / 147 vessels and LNG carriers accounting for 70% of backlog.
- Interpretation: This is a clean C01 signal because the order was not generic capacity talk. The backlog was tied to high-value LNG carrier mix.
- Price path source: `stock-web/atlas/ohlcv_tradable_by_symbol_year/010/010140/2023.csv`
- Corporate-action status: clean for this 2023-06 entry window; profile CA candidates predate the trigger window.

### 4.2 HD Korea Shipbuilding & Offshore Engineering — C01-132-02

- Evidence date: 2023-08-04.
- Evidence URL: `https://www.kedglobal.com/shipping-shipbuilding/newsView/ked202308040013`
- Evidence summary: HD KSOE won two LNG carriers and had achieved 96.9% of its 2023 order target. The article also cited LNG carrier newbuilding prices at $260m as of June, up 36.8% from June 2021.
- Interpretation: Strong backlog/price environment, but the price trigger arrived after a sector run. This should be Stage2-Watch or local 4B-watch rather than fresh Actionable without relative-strength decay check.
- Price path source: `stock-web/atlas/ohlcv_tradable_by_symbol_year/009/009540/2023.csv` and 2024 continuation shard.
- Corporate-action status: clean for this 2023-08 entry window.

### 4.3 HD Hyundai Heavy Industries — C01-132-03

- Evidence date: 2024-07-25 / 2024-07-31.
- Evidence URLs:
  - `https://en.yna.co.kr/view/AEN20240725006800320`
  - `https://www.imarinenews.com/12422.html`
- Evidence summary: HD Hyundai Heavy reported Q2 net profit of 154.1bn won, up 539.4% YoY; a separate HD Hyundai group report tied profit improvement to order-screening strategy and production-cost stabilization.
- Interpretation: This is the C01 “backlog converts to margin” bridge. It does not rely on orderbook size alone; the profit bridge is already visible.
- Price path source: `stock-web/atlas/ohlcv_tradable_by_symbol_year/329/329180/2024.csv` and 2025 continuation shard.
- Corporate-action status: clean; stock-web profile shows no corporate-action candidates for the symbol.

### 4.4 HD Hyundai Mipo — C01-132-04

- Evidence date: 2024-07-25.
- Evidence URL: `https://en.yna.co.kr/view/AEN20240725007000320`
- Evidence summary: HD Hyundai Mipo shifted to Q2 operating profit of 17.4bn won from an operating loss a year earlier, with sales up 9.3%.
- Interpretation: Earlier loss-stage skepticism was reasonable, but the Q2 print created an actual margin bridge. This is Stage2-Actionable with high-MAE guard, not blind Green.
- Price path source: `stock-web/atlas/ohlcv_tradable_by_symbol_year/010/010620/2024.csv` and 2025 continuation shard.
- Corporate-action status: clean inside the D180 window; later inactive/delisted-like profile status does not contaminate the 2024-07 to 2025-04 path.

### 4.5 Hanwha Ocean — C01-132-05 and C01-132-06

- Evidence date 1: 2024-02-21/2024-02-22.
- Evidence URLs:
  - `https://www.imarinenews.com/6257.html`
  - `https://en.yna.co.kr/view/AEN20240221005751320`
- Evidence summary: 2023 sales rose strongly and losses narrowed sharply, but the company was still operating-loss positive/negative mixed at Q4 level.
- Interpretation: The right label is Stage2-Watch, not Actionable and not 4C. It needed later profit confirmation.

- Evidence date 2: 2024-07-26.
- Evidence URL: `https://www.asiae.co.kr/en/article/2024072614321195934`
- Evidence summary: Hanwha Ocean recorded a Q2 operating loss of 9.6bn won and turned back to a deficit.
- Interpretation: This is a 4B-watch trigger because the price path immediately suffered high MAE. However, later theme recovery means it should not automatically become 4C unless orderbook/margin thesis also breaks.
- Price path source: `stock-web/atlas/ohlcv_tradable_by_symbol_year/042/042660/2024.csv` and 2025 continuation shard.
- Corporate-action status: clean for 2024 triggers after the 2023-11-28 corporate-action candidate date.

---

## 5. Trigger-level stock-web price path rows

MFE/MAE formula: entry after trigger uses the stock-web tradable row close as `entry_price`; `MFE_ND_pct = (max(high over next N tradable rows) / entry_price - 1) * 100`; `MAE_ND_pct = (min(low over next N tradable rows) / entry_price - 1) * 100`.

```jsonl
{"case_id":"C01-132-01","symbol":"010140","company":"Samsung Heavy Industries","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C01_ORDER_BACKLOG_MARGIN_BRIDGE","fine_archetype_id":"LNG_backlog_price_quality","trigger_type":"Stage2-Actionable","trigger_date":"2023-06-13","entry_date":"2023-06-13","entry_price":6500.0,"MFE_30D_pct":34.92,"MAE_30D_pct":-0.62,"MFE_90D_pct":45.69,"MAE_90D_pct":-0.62,"MFE_180D_pct":45.69,"MAE_180D_pct":-0.62,"outcome_label":"positive","evidence_url":"https://en.yna.co.kr/view/AEN20230613005100320","price_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","corporate_action_contamination":"none_detected_in_window","dedupe_key":"C01_ORDER_BACKLOG_MARGIN_BRIDGE|010140|Stage2-Actionable|2023-06-13"}
{"case_id":"C01-132-02","symbol":"009540","company":"HD Korea Shipbuilding & Offshore Engineering","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C01_ORDER_BACKLOG_MARGIN_BRIDGE","fine_archetype_id":"late_order_target_high_MAE","trigger_type":"4B-Watch","trigger_date":"2023-08-04","entry_date":"2023-08-04","entry_price":121500.0,"MFE_30D_pct":2.47,"MAE_30D_pct":-9.30,"MFE_90D_pct":2.47,"MAE_90D_pct":-26.75,"MFE_180D_pct":9.88,"MAE_180D_pct":-26.75,"outcome_label":"counterexample","evidence_url":"https://www.kedglobal.com/shipping-shipbuilding/newsView/ked202308040013","price_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","corporate_action_contamination":"none_detected_in_window","dedupe_key":"C01_ORDER_BACKLOG_MARGIN_BRIDGE|009540|4B-Watch|2023-08-04"}
{"case_id":"C01-132-03","symbol":"329180","company":"HD Hyundai Heavy Industries","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C01_ORDER_BACKLOG_MARGIN_BRIDGE","fine_archetype_id":"order_screening_margin_recovery","trigger_type":"Stage2-Actionable","trigger_date":"2024-07-25","entry_date":"2024-07-25","entry_price":177500.0,"MFE_30D_pct":25.35,"MAE_30D_pct":-4.28,"MFE_90D_pct":37.75,"MAE_90D_pct":-4.28,"MFE_180D_pct":128.73,"MAE_180D_pct":-4.28,"outcome_label":"positive","evidence_url":"https://en.yna.co.kr/view/AEN20240725006800320","secondary_evidence_url":"https://www.imarinenews.com/12422.html","price_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","corporate_action_contamination":"none_detected_in_window","dedupe_key":"C01_ORDER_BACKLOG_MARGIN_BRIDGE|329180|Stage2-Actionable|2024-07-25"}
{"case_id":"C01-132-04","symbol":"010620","company":"HD Hyundai Mipo","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C01_ORDER_BACKLOG_MARGIN_BRIDGE","fine_archetype_id":"loss_to_profit_margin_bridge","trigger_type":"Stage2-Actionable","trigger_date":"2024-07-25","entry_date":"2024-07-25","entry_price":102600.0,"MFE_30D_pct":19.69,"MAE_30D_pct":-9.65,"MFE_90D_pct":19.69,"MAE_90D_pct":-10.33,"MFE_180D_pct":40.64,"MAE_180D_pct":-10.33,"outcome_label":"positive_high_MAE_guard_required","evidence_url":"https://en.yna.co.kr/view/AEN20240725007000320","price_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","corporate_action_contamination":"none_detected_in_window","dedupe_key":"C01_ORDER_BACKLOG_MARGIN_BRIDGE|010620|Stage2-Actionable|2024-07-25"}
{"case_id":"C01-132-05","symbol":"042660","company":"Hanwha Ocean","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C01_ORDER_BACKLOG_MARGIN_BRIDGE","fine_archetype_id":"loss_narrowing_then_turnaround","trigger_type":"Stage2-Watch","trigger_date":"2024-02-22","entry_date":"2024-02-22","entry_price":21750.0,"MFE_30D_pct":42.07,"MAE_30D_pct":-1.15,"MFE_90D_pct":53.56,"MAE_90D_pct":-1.15,"MFE_180D_pct":80.92,"MAE_180D_pct":-1.15,"outcome_label":"positive_after_watch","evidence_url":"https://www.imarinenews.com/6257.html","secondary_evidence_url":"https://en.yna.co.kr/view/AEN20240221005751320","price_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","corporate_action_contamination":"none_detected_in_window","dedupe_key":"C01_ORDER_BACKLOG_MARGIN_BRIDGE|042660|Stage2-Watch|2024-02-22"}
{"case_id":"C01-132-06","symbol":"042660","company":"Hanwha Ocean","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C01_ORDER_BACKLOG_MARGIN_BRIDGE","fine_archetype_id":"quarterly_loss_high_MAE","trigger_type":"4B-Watch","trigger_date":"2024-07-26","entry_date":"2024-07-26","entry_price":30950.0,"MFE_30D_pct":14.05,"MAE_30D_pct":-17.93,"MFE_90D_pct":14.05,"MAE_90D_pct":-17.93,"MFE_180D_pct":77.71,"MAE_180D_pct":-17.93,"outcome_label":"counterexample_high_MAE_then_theme_recovery","evidence_url":"https://www.asiae.co.kr/en/article/2024072614321195934","price_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","corporate_action_contamination":"none_detected_in_window","dedupe_key":"C01_ORDER_BACKLOG_MARGIN_BRIDGE|042660|4B-Watch|2024-07-26"}
```

---

## 6. Current profile stress test

### Positive path correctly captured if C01 gate is evidence-aware

- `010140`: order + backlog mix + high-value LNG exposure. Low MAE and fast MFE. The model should allow Stage2-Actionable and early Yellow consideration.
- `329180`: profit bridge was already visible. Strong D180 MFE with limited MAE. This is the cleanest margin-conversion success.
- `010620`: Q2 profit swing validates the margin bridge, but MAE over 10% says the entry still needs risk guard.
- `042660` February: hard block on operating loss would have missed a strong watch-to-confirmation path. Better label is Stage2-Watch until Q1 profit confirmation.

### False-positive / 4B risk path

- `009540`: excellent orderbook environment but poor near/mid-term path after the trigger. This is a late-cycle order headline after price run; it needs relative-strength decay and high-MAE guard.
- `042660` July: Q2 loss created a real 4B-watch event. Yet later recovery warns that “one-quarter loss” should not be hard 4C unless backlog/margin thesis breaks permanently.

---

## 7. Raw component score breakdown

This is a shadow-only score sketch. It is not a production patch.

| case_id | eps_fcf_explosion | visibility | bottleneck_pricing | market_mispricing | valuation_rerating | capital_allocation | info_confidence | score_sketch | suggested_stage |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| C01-132-01 | 16 | 20 | 18 | 12 | 11 | 4 | 8 | 89 | Stage3-Yellow candidate |
| C01-132-02 | 8 | 18 | 16 | 2 | -8 | 3 | 7 | 46 | 4B-Watch / reject Actionable |
| C01-132-03 | 18 | 22 | 17 | 13 | 14 | 4 | 9 | 97 | Stage3-Yellow/Green review |
| C01-132-04 | 14 | 17 | 12 | 9 | 9 | 3 | 8 | 72 | Stage2-Actionable with MAE guard |
| C01-132-05 | 9 | 14 | 11 | 15 | 8 | 4 | 7 | 68 | Stage2-Watch, confirmation needed |
| C01-132-06 | 4 | 8 | 9 | 6 | -6 | 3 | 8 | 32 | 4B-Watch, not automatic 4C |

---

## 8. Residual contribution

```json
{
  "canonical_archetype_id": "C01_ORDER_BACKLOG_MARGIN_BRIDGE",
  "new_axis_proposed": "c01_backlog_price_quality_margin_bridge_gate",
  "existing_axis_strengthened": [
    "full_4b_requires_non_price_evidence",
    "price_only_blowoff_blocks_positive_stage",
    "high_mae_guard_on_late_order_headline"
  ],
  "existing_axis_weakened": [
    "hard_block_on_single_quarter_loss_when_backlog_quality_remains_intact"
  ],
  "rule_candidate": "C01_BACKLOG_PRICE_QUALITY_MARGIN_BRIDGE_GATE_V1",
  "safe_patch_candidate": {
    "stage2_actionable_require_any_two_of": [
      "named_or_contractual_backlog_growth",
      "high_value_mix_or_pricing_evidence",
      "delivery_or_revenue_recognition_visibility",
      "actual_margin_or_revision_bridge"
    ],
    "stage2_watch_allowed_when": [
      "loss_narrowing_or_turnaround_setup_visible",
      "backlog_quality_visible_but_current_quarter_still_loss_making"
    ],
    "local_4b_watch_when": [
      "order_target_or_backlog_headline_after_sector_price_run",
      "MFE_90D_pct_less_than_5_and_MAE_90D_pct_less_than_minus_15",
      "quarterly_loss_reappears_after_turnaround_expectation"
    ],
    "do_not_4c_unless": [
      "backlog_quality_break",
      "customer_or_delivery_cancellation",
      "margin_thesis_break_persists_beyond_one_quarter",
      "working_capital_or_balance_sheet stress confirms thesis break"
    ]
  },
  "current_profile_error_count": 4,
  "positive_case_count": 4,
  "counterexample_count": 2
}
```

---

## 9. Rejected / narrative-only rows

```jsonl
{"symbol":"241560","company":"Doosan Bobcat","reason":"not_used","note":"industrial margin/cycle case but weaker C01 backlog-specific evidence than shipbuilding samples; better reserved for industrial machinery or macro-capex rerating leaf."}
{"symbol":"000720","company":"Hyundai Engineering & Construction","reason":"not_used_due_visible_C01_top_cluster","note":"Index visible top-covered symbols already include 000720; avoided to improve no-repeat diversity."}
{"symbol":"006360","company":"GS Engineering & Construction","reason":"not_used_due_visible_C01_top_cluster","note":"Index visible top-covered symbols already include 006360; avoided to improve no-repeat diversity."}
```

---

## 10. Validation checklist

```yaml
validation:
  standalone_markdown: true
  standard_filename_regex: pass
  live_stock_discovery: false
  code_patch_executed: false
  production_scoring_changed: false
  no_repeat_index_used_as_ledger_only: true
  actual_stock_web_ohlcv_used: true
  all_usable_rows_have_30_90_180_mfe_mae: true
  price_source_fields_present: true
  canonical_archetype_present: true
  large_sector_round_consistency: pass
  r1_l1_c01_consistency: pass
  corporate_action_reviewed: true
  compact_filename_used: false
  dedupe_key_present: true
```

---

## 11. Deferred coding-agent handoff prompt

Do not execute inside this research session.

```text
Read this MD and ingest only the JSONL trigger rows whose validation block passes. Apply no production scoring change automatically. If enough C01 rows accumulate, test a shadow patch named C01_BACKLOG_PRICE_QUALITY_MARGIN_BRIDGE_GATE_V1. The patch should require at least two of backlog quality, price/mix evidence, delivery/revenue visibility, and margin/revision bridge for Stage2-Actionable. It should route late order headlines with poor MFE/MAE symmetry to local 4B-Watch, and it should avoid hard 4C on a single quarterly loss unless backlog quality or margin thesis breaks persistently.
```

---

## 12. Next research state required

```yaml
completed_round: R1
completed_loop: 132
completed_large_sector_id: L1_INDUSTRIALS_INFRA_DEFENSE_GRID
completed_canonical_archetype_id: C01_ORDER_BACKLOG_MARGIN_BRIDGE
selection_basis: docs/core/V12_Research_No_Repeat_Index.md
selected_priority_bucket: Priority 0
round_schedule_status: coverage_index_selected_not_sequential
round_sector_consistency: pass
coverage_after_if_accepted:
  C01_ORDER_BACKLOG_MARGIN_BRIDGE: 25
next_recommended_archetypes:
  - C28_SOFTWARE_SECURITY_CONTRACT_RETENTION
  - C02_POWER_GRID_DATACENTER_CAPEX
  - C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF
  - C14_EV_DEMAND_SLOWDOWN_4B_4C
  - C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE
  - C06_HBM_MEMORY_CUSTOMER_CAPACITY
```
