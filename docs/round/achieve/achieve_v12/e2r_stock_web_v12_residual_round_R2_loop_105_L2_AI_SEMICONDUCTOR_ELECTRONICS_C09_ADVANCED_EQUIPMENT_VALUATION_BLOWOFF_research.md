# E2R v12 Sector-Archetype Residual Research
## C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF — advanced process/test equipment valuation blowoff guard

```yaml
schema_family: v12_sector_archetype_residual
research_session: post_calibrated_sector_archetype_residual_research
mode: historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12
selected_round: R2
selected_loop: 105
large_sector_id: L2_AI_SEMICONDUCTOR_ELECTRONICS
canonical_archetype_id: C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF
fine_archetype_id: ADVANCED_PROCESS_AND_TEST_EQUIPMENT_VALUATION_BLOWOFF_VS_ORDER_REVISION_BRIDGE
selected_priority_bucket: Priority 0
selection_basis: docs/core/V12_Research_No_Repeat_Index.md
round_schedule_status: coverage_index_selected
round_sector_consistency: pass
stock_agent_code_access_allowed: false
stock_agent_code_patch_allowed: false
stock_agent_live_scan_allowed: false
production_scoring_changed: false
shadow_weight_only: true
price_data_source: Songdaiki/stock-web
upstream_source: FinanceData/marcap
price_basis: tradable_raw
price_adjustment_status: raw_unadjusted_marcap
manifest_max_date: 2026-02-20
```

---

## 1. Selection rationale

The coverage-index scheduler selects **C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF** because the no-repeat index shows C09 at only **15 representative rows**, still below the 30-row minimum stability zone and far below the 50-row practical calibration zone.

This loop intentionally avoids the currently top-covered C09 symbols listed in the index: `039030`, `084370`, `140860`, `240810`, `036810`, and `036930`.

Chosen symbols:

| symbol | name | reason for inclusion |
|---|---|---|
| `403870` | HPSP | advanced process equipment repricing with severe later drawdown |
| `031980` | 피에스케이홀딩스 | extreme HBM/advanced-packaging equipment route, but peak-fade demands 4B guard |
| `122640` | 예스티 | advanced annealing/equipment theme spike followed by hard collapse |
| `253590` | 네오셈 | CXL/SSD test-equipment theme beta with high-MFE/high-MAE profile |

---

## 2. Price source validation

```jsonl
{"row_type":"price_source_validation","repo":"Songdaiki/stock-web","manifest":"atlas/manifest.json","source_name":"FinanceData/marcap","price_adjustment_status":"raw_unadjusted_marcap","manifest_max_date":"2026-02-20","calibration_shard_root":"atlas/ohlcv_tradable_by_symbol_year","note":"Zero-volume and invalid OHLC rows are excluded from tradable shards; corporate-action contaminated windows are blocked by default."}
{"row_type":"price_source_validation","symbol":"403870","profile":"atlas/symbol_profiles/403/403870.json","corporate_action_candidate_dates":["2023-03-16","2023-04-11"],"selected_window_corporate_action_contaminated":false}
{"row_type":"price_source_validation","symbol":"031980","profile":"atlas/symbol_profiles/031/031980.json","corporate_action_candidate_dates":["1998-07-28","2000-04-20","2007-03-16","2019-05-10","2020-02-21"],"selected_window_corporate_action_contaminated":false}
{"row_type":"price_source_validation","symbol":"122640","profile":"atlas/symbol_profiles/122/122640.json","corporate_action_candidate_dates":["2015-08-24","2018-02-08","2018-03-07"],"selected_window_corporate_action_contaminated":false}
{"row_type":"price_source_validation","symbol":"253590","profile":"atlas/symbol_profiles/253/253590.json","corporate_action_candidate_dates":["2019-01-31"],"selected_window_corporate_action_contaminated":false}
```

---

## 3. Trigger rows

```jsonl
{"row_type": "trigger", "schema_version": "v12_sector_archetype_residual", "large_sector_id": "L2_AI_SEMICONDUCTOR_ELECTRONICS", "canonical_archetype_id": "C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF", "fine_archetype_id": "ADVANCED_PROCESS_AND_TEST_EQUIPMENT_VALUATION_BLOWOFF_VS_ORDER_REVISION_BRIDGE", "calibration_usable": true, "symbol": "403870", "name": "HPSP", "entry_date": "2024-01-19", "entry_price": 47800, "peak_date": "2024-02-15", "peak_high": 63900, "trough_date": "2024-12-09", "trough_low": 25200, "mfe_180d_pct": 33.68, "mae_180d_pct": -47.28, "peak_to_later_dd_pct": -60.56, "classification": "counterexample_high_mae", "trigger_type": "advanced_process_equipment_ai_hbm_theme_without_confirmed_order_bridge", "evidence_quality": "source_proxy_only_url_repair_required", "note": "High-pressure/advanced process equipment label created early MFE, but full-window drawdown was severe."}
{"row_type": "trigger", "schema_version": "v12_sector_archetype_residual", "large_sector_id": "L2_AI_SEMICONDUCTOR_ELECTRONICS", "canonical_archetype_id": "C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF", "fine_archetype_id": "ADVANCED_PROCESS_AND_TEST_EQUIPMENT_VALUATION_BLOWOFF_VS_ORDER_REVISION_BRIDGE", "calibration_usable": true, "symbol": "031980", "name": "피에스케이홀딩스", "entry_date": "2024-01-19", "entry_price": 27250, "peak_date": "2024-06-19", "peak_high": 85300, "trough_date": "2024-02-01", "trough_low": 25700, "mfe_180d_pct": 213.03, "mae_180d_pct": -5.69, "peak_to_later_dd_pct": -67.53, "classification": "positive_route_but_valuation_blowoff_4b_watch", "trigger_type": "hbm_advanced_packaging_equipment_repricing_without_full_order_revision_bridge", "evidence_quality": "source_proxy_only_url_repair_required", "note": "Very strong route and low entry-MAE, but peak-to-later drawdown argues for 4B valuation-blowoff guard unless order/revision bridge is verified."}
{"row_type": "trigger", "schema_version": "v12_sector_archetype_residual", "large_sector_id": "L2_AI_SEMICONDUCTOR_ELECTRONICS", "canonical_archetype_id": "C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF", "fine_archetype_id": "ADVANCED_PROCESS_AND_TEST_EQUIPMENT_VALUATION_BLOWOFF_VS_ORDER_REVISION_BRIDGE", "calibration_usable": true, "symbol": "122640", "name": "예스티", "entry_date": "2024-02-22", "entry_price": 19000, "peak_date": "2024-03-27", "peak_high": 29900, "trough_date": "2024-12-09", "trough_low": 7710, "mfe_180d_pct": 57.37, "mae_180d_pct": -59.42, "peak_to_later_dd_pct": -74.21, "classification": "hard_counterexample_high_mae", "trigger_type": "advanced_annealing_equipment_theme_spike_without_durable_customer_quality_bridge", "evidence_quality": "source_proxy_only_url_repair_required", "note": "The route looked like advanced equipment rerating, but the late-year collapse is a hard valuation-blowoff guardrail case."}
{"row_type": "trigger", "schema_version": "v12_sector_archetype_residual", "large_sector_id": "L2_AI_SEMICONDUCTOR_ELECTRONICS", "canonical_archetype_id": "C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF", "fine_archetype_id": "ADVANCED_PROCESS_AND_TEST_EQUIPMENT_VALUATION_BLOWOFF_VS_ORDER_REVISION_BRIDGE", "calibration_usable": true, "symbol": "253590", "name": "네오셈", "entry_date": "2024-01-19", "entry_price": 11080, "peak_date": "2024-03-07", "peak_high": 17150, "trough_date": "2024-12-09", "trough_low": 8190, "mfe_180d_pct": 54.78, "mae_180d_pct": -26.08, "peak_to_later_dd_pct": -52.24, "classification": "counterexample_high_mae", "trigger_type": "cxl_ssd_test_equipment_theme_beta_without_recurring_order_bridge", "evidence_quality": "source_proxy_only_url_repair_required", "note": "CXL/test-equipment theme produced a strong spike, but MAE and peak fade show why C09 needs customer/order/revision evidence."}
```

---

## 4. Case analysis

### 4.1 HPSP (`403870`) — advanced process equipment label did not survive full-window stress

Entry was set to **2024-01-19 close 47,800** after the early AI/HBM/advanced-equipment repricing impulse became visible. The stock reached **63,900 high on 2024-02-15**, producing **MFE +33.68%**. But by **2024-12-09**, the low was **25,200**, giving **MAE -47.28%** and peak-to-later drawdown of **-60.56%**.

Interpretation: C09 should not promote an advanced process equipment label without a verified order/revision/customer bridge. The price action was an engine revving in neutral: loud, fast, and directionally exciting, but not mechanically coupled to durable earnings evidence.

### 4.2 피에스케이홀딩스 (`031980`) — strong route, but valuation-blowoff guard still needed

Entry was set to **2024-01-19 close 27,250**. The local route was extremely strong, reaching **85,300 high on 2024-06-19**, for **MFE +213.03%**. Entry-MAE was only **-5.69%** using the 2024-02-01 low of 25,700. But the same route later faded to a **2024-12-09 low of 27,700**, implying **peak-to-later drawdown -67.53%**.

Interpretation: this is not a simple failure. It is a high-quality route candidate with a severe valuation-blowoff tail. It should be allowed as a C09 positive route only when accompanied by confirmed customer/order/revision evidence. Without that bridge, it belongs in 4B watch rather than Stage3-Green.

### 4.3 예스티 (`122640`) — advanced-equipment theme spike collapsed into hard counterexample

Entry was set to **2024-02-22 close 19,000**. The stock reached **29,900 high on 2024-03-27**, for **MFE +57.37%**. But the 2024-12-09 low was **7,710**, giving **MAE -59.42%** and peak-to-later drawdown of **-74.21%**.

Interpretation: this is a clean C09 hard counterexample. Advanced equipment vocabulary can pull the price like a magnet, but if customer qualification, actual tool order, delivery schedule, and revision bridge do not arrive, the magnet becomes a trapdoor.

### 4.4 네오셈 (`253590`) — CXL/test-equipment beta produced high MFE but weak persistence

Entry was set to **2024-01-19 close 11,080**. The stock reached **17,150 high on 2024-03-07**, producing **MFE +54.78%**. The later low was **8,190 on 2024-12-09**, giving **MAE -26.08%** and peak-to-later drawdown **-52.24%**.

Interpretation: this is the classic C09 boundary case. The equipment/test theme produced enough upside to tempt Stage2/Yellow, but the path did not prove durable without recurring order and revision evidence.

---

## 5. Score-return alignment stress test

| symbol | classification | MFE % | MAE % | peak-to-later DD % | calibrated profile stress |
|---|---:|---:|---:|---:|---|
| 403870 | counterexample_high_mae | 33.68 | -47.28 | -60.56 | Stage2/Yellow should be blocked unless verified order/revision bridge exists |
| 031980 | positive_route_but_4B_watch | 213.03 | -5.69 | -67.53 | Price route is strong, but Green requires non-price evidence |
| 122640 | hard_counterexample_high_mae | 57.37 | -59.42 | -74.21 | Advanced-equipment label alone must not promote |
| 253590 | counterexample_high_mae | 54.78 | -26.08 | -52.24 | Theme beta is not enough for Stage3 |

---

## 6. Shadow rule proposal

```jsonl
{"row_type":"shadow_weight","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF","axis":"c09_order_revision_customer_quality_bridge_required","proposed_effect":"demote price-only advanced-equipment blowoff from Stage2-Actionable/Stage3 to 4B watch unless verified order/customer/revision evidence exists","production_scoring_changed":false,"shadow_weight_only":true}
{"row_type":"shadow_weight","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF","axis":"c09_peak_fade_penalty_after_high_mfe","proposed_effect":"if MFE is high but peak-to-later drawdown exceeds 50 percent and non-price bridge is source_proxy_only, require 4B or 4C stress label","production_scoring_changed":false,"shadow_weight_only":true}
```

---

## 7. Aggregate metric

```jsonl
{"row_type":"aggregate_metric","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF","new_independent_case_count":4,"reused_case_count":0,"same_archetype_new_symbol_count":4,"same_archetype_new_trigger_family_count":3,"calibration_usable_case_count":4,"positive_case_count":1,"counterexample_count":3,"current_profile_error_count":4,"verified_url_repair_needed_count":4,"coverage_gap_before":"C09 rows 15; need 15 to 30; need 35 to 50","loop_contribution_label":"canonical_archetype_rule_candidate"}
```

---

## 8. Residual contribution summary

```text
new_axis_proposed:
  c09_order_revision_customer_quality_bridge_required

existing_axis_strengthened:
  full_4b_requires_non_price_evidence scoped to C09 advanced-equipment / HBM / CXL / high-pressure-process rallies

existing_axis_weakened:
  null

why_this_matters:
  C09 often shows visually attractive MFE before the earnings bridge arrives.
  The calibration error is not missing the price route; the error is trusting the route too early.
  High-MFE plus high peak-fade should be treated like a flare, not a lighthouse, unless order/revision evidence confirms durability.
```

---

## 9. Deferred Coding Agent Handoff Prompt

```text
Do not execute this handoff in the research session.

Later coding-agent task:
- Read this MD as one v12 residual research artifact.
- Do not treat the proposed rule as production truth by default.
- Add/merge rows into the v12 calibration corpus only after parser validation.
- Candidate shadow axes:
  1. c09_order_revision_customer_quality_bridge_required
  2. c09_peak_fade_penalty_after_high_mfe
- Scope:
  canonical_archetype_id = C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF
  large_sector_id = L2_AI_SEMICONDUCTOR_ELECTRONICS
- Guard:
  If evidence_url is source_proxy_only_url_repair_required, keep rows usable for residual research but do not promote them as verified positive scoring weights without URL repair.
```

---

## 10. Next research state

```text
completed_round = R2
completed_loop = 105
selection_basis = docs/core/V12_Research_No_Repeat_Index.md
selected_priority_bucket = Priority 0
round_schedule_status = coverage_index_selected
round_sector_consistency = pass
next_recommended_archetypes = C01_ORDER_BACKLOG_MARGIN_BRIDGE, C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH, C06_HBM_MEMORY_CUSTOMER_CAPACITY
```
